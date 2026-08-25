#!/usr/bin/env python3
"""Provjeri P5-C: katalog, oba generirana prikaza, rutu i rucne provjere."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build-appendix-c-views.R"
WRAPPER = ROOT / "bookwright_plugin" / "bookwright" / "scripts" / "run_rscript.py"
CATALOGUE = ROOT / "data" / "katalog.yml"
PUBLIC = ROOT / "podaci.qmd"
APPENDIX = ROOT / "dodaci" / "c-katalog-podataka.qmd"
README = ROOT / "data" / "README.md"
ARTIFACT = ROOT / "config" / "appendix-c-data-route.json"

EXPECTED_ANKETA = {
    "18 do 24": ("90", "300"),
    "25 do 34": ("84", "300"),
    "35 do 44": ("66", "300"),
    "45 i više": ("60", "300"),
}

EXPECTED_POPULATION = {
    "portal": ("15101", "50000"),
    "društvene mreže": ("13378", "50000"),
    "TV": ("10827", "50000"),
    "radio": ("5839", "50000"),
    "tisak": ("4855", "50000"),
}


def fail(message: str) -> None:
    raise SystemExit(f"APPENDIX_C_CHECK_FAIL: {message}")


def md5(path: Path) -> str:
    digest = hashlib.md5()  # nosec B324 -- identity, not cryptographic security
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(command: list[str], *, cwd: Path = ROOT, timeout: int = 180) -> str:
    completed = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        check=False,
    )
    combined = completed.stdout + completed.stderr
    if completed.returncode != 0:
        fail(f"naredba nije prošla ({' '.join(command)}):\n{combined}")
    return combined


def load_artifact(path: Path = ARTIFACT) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"route artefakt nije čitljiv JSON: {error}")
    if not isinstance(value, dict):
        fail("route artefakt nije preslikavanje")
    return value


def copy_into(stage: Path, relative: str) -> None:
    source = ROOT / relative
    target = stage / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def check_artifact_contract(artifact: dict) -> None:
    if artifact.get("schema_version") != "appendix-c-data-route-v1":
        fail("pogrešna je inačica route artefakta")
    if artifact.get("packet") != "P5-C":
        fail("route artefakt nije vezan uz P5-C")

    source = artifact.get("canonical_catalogue", {})
    if source.get("path") != "data/katalog.yml":
        fail("route artefakt ne imenuje kanonski katalog")
    if source.get("sole_machine_readable_record") is not True:
        fail("route artefakt ne čuva granicu jedinoga strojnog izvora")
    if source.get("md5") != md5(CATALOGUE):
        fail("route artefakt nema kontrolni zbroj sadašnjega kataloga")

    counts = artifact.get("counts", {})
    if counts != {
        "packages": 20,
        "promoted": 6,
        "bundled": 9,
        "portal_mediated": 2,
        "external_only": 9,
    }:
        fail(f"brojnosti kataloga nisu kanonske: {counts}")

    views = {view.get("path"): view for view in artifact.get("generated_views", [])}
    if set(views) != {"podaci.qmd", "dodaci/c-katalog-podataka.qmd"}:
        fail("route artefakt ne imenuje točno oba javna prikaza")
    for relative, path in (
        ("podaci.qmd", PUBLIC),
        ("dodaci/c-katalog-podataka.qmd", APPENDIX),
    ):
        if views[relative].get("md5") != md5(path):
            fail(f"kontrolni zbroj javnoga prikaza nije svjež: {relative}")
        if views[relative].get("anchors") != 20:
            fail(f"javni prikaz nema 20 paketnih ruta: {relative}")


def check_aggregate_contract(artifact: dict, public: str, appendix: str) -> None:
    records = {
        record.get("id"): record
        for record in artifact.get("aggregate_hand_checks", [])
    }
    if set(records) != {"anketa_mreze", "populacija_medija"}:
        fail("artefakt nema oba kanonska agregatna prikaza")

    def check_package(
        package_id: str,
        group_column: str,
        expected: dict[str, tuple[str, str]],
    ) -> None:
        record = records[package_id]
        rows = record.get("rows", [])
        contract = record.get("reconciliation", {})
        by_group = {row[group_column]: row for row in rows}
        if set(by_group) != set(expected):
            fail(f"{package_id}: skupine javnoga prikaza nisu kanonske")

        for group, (numerator, denominator) in expected.items():
            row = by_group[group]
            if (row.get("broj"), row.get("ukupno")) != (numerator, denominator):
                fail(f"{package_id}/{group}: brojnik ili nazivnik nije kanonski")
            for source in (public, appendix):
                required = f"`{numerator}` / `{denominator}` = `{row['udio']}`"
                if required not in source:
                    fail(f"{package_id}/{group}: jedan javni prikaz nema brojnik i nazivnik")

        for share in contract.get("shares", []):
            for group, row in by_group.items():
                numerator = Decimal(row[share["numerator"]])
                denominator = Decimal(row[share["denominator"]])
                observed = Decimal(row[share["share"]])
                if abs(observed - numerator / denominator) > Decimal("1e-15"):
                    fail(f"{package_id}/{group}: udio se ne slaže s brojnikom i nazivnikom")
                display = (
                    f"`{row[share['numerator']]}` / "
                    f"`{row[share['denominator']]}` = `{row[share['share']]}`"
                )
                if display not in public or display not in appendix:
                    fail(f"{package_id}/{group}: javni prikazi ne nose cijelu provjeru udjela")

        for mean in contract.get("sums", []):
            for group, row in by_group.items():
                total = row[mean["total"]]
                if not re.fullmatch(r"-?[0-9]+", total):
                    fail(f"{package_id}/{group}: zbroj uz prosjek nije cijeli broj")
                pair = f"zbroj `{total}`; prosjek `{row[mean['mean']]}`"
                if pair not in public:
                    fail(f"{package_id}/{group}: javna stranica odvaja prosjek od zbroja")
                if pair not in appendix:
                    fail(f"{package_id}/{group}: Dodatak C odvaja prosjek od zbroja")

    check_package("anketa_mreze", "dobna_skupina", EXPECTED_ANKETA)
    check_package("populacija_medija", "izvor_vijesti", EXPECTED_POPULATION)


def check_dzs(artifact: dict, public: str, appendix: str) -> None:
    record = artifact.get("dzs_reconciliation", {})
    if record.get("measures_are_comparable_series") is not False:
        fail("DZS-ove dvije mjere ne smiju biti označene usporedivom serijom")
    administrative = record.get("administrative", [])
    survey = record.get("survey", [])
    if len(administrative) != 6 or any(
        item.get("tolerance") != 0 or item.get("max_abs_residual") != 0
        for item in administrative
    ):
        fail("administrativna usklađenja ne nose točan ostatak 0")
    if {item.get("id") for item in survey} != {
        "anketa-odrediste",
        "anketa-trajanje",
        "anketa-dobne-skupine",
    }:
        fail("nedostaje jedna od triju anketnih razgradnji")
    if any(item.get("tolerance") != 1 or item.get("max_abs_residual") != 1 for item in survey):
        fail("anketna usklađenja ne čuvaju točan najveći ostatak 1")
    for source in (public, appendix):
        for fragment in (
            "BS_TU11",
            "BS_TU12",
            "T03",
            "administrativne eVisitor dolaske",
            "uzoračka anketa",
            "najveći ostatak točno `0`",
            "najveći ostatak točno `1`",
            "ne prikazuju kao usporedive serije",
        ):
            if fragment not in source:
                fail(f"javni DZS prikaz nema granicu ili ostatak: {fragment}")


def check_routes_and_links(artifact: dict, public: str, appendix: str) -> None:
    routes = artifact.get("package_routes", [])
    if len(routes) != 20 or len({route.get("id") for route in routes}) != 20:
        fail("route artefakt nema 20 jedinstvenih paketa")

    for route in routes:
        public_route = route.get("public_anchor", "")
        appendix_route = route.get("appendix_anchor", "")
        if not public_route.startswith("podaci.qmd#"):
            fail(f"nevaljana javna ruta za {route.get('id')}")
        if not appendix_route.startswith("dodaci/c-katalog-podataka.qmd#"):
            fail(f"nevaljana ruta Dodatka C za {route.get('id')}")
        public_anchor = public_route.split("#", 1)[1]
        appendix_anchor = appendix_route.split("#", 1)[1]
        if f"{{#{public_anchor}}}" not in public:
            fail(f"podaci.qmd nema sidro {public_anchor}")
        if f"{{#{appendix_anchor}}}" not in appendix:
            fail(f"Dodatak C nema sidro {appendix_anchor}")
        if f"dodaci/c-katalog-podataka.qmd#{appendix_anchor}" not in public:
            fail(f"podaci.qmd nema poveznicu na {appendix_anchor}")
        if f"../podaci.qmd#{public_anchor}" not in appendix:
            fail(f"Dodatak C nema povratnu poveznicu na {public_anchor}")

    for path, source in ((PUBLIC, public), (APPENDIX, appendix)):
        ids = re.findall(r"\{#([a-z0-9-]+)\}", source)
        duplicates = sorted({value for value in ids if ids.count(value) > 1})
        if duplicates:
            fail(f"{path.name} ima udvostručena sidra: {duplicates}")

        definitions = set(re.findall(r"\{#(tbl-[a-z0-9-]+)\}", source))
        references = set(re.findall(r"@(tbl-[a-z0-9-]+)", source))
        if references - definitions:
            fail(f"{path.name} ima nerazriješene tablične reference: {references - definitions}")

        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source):
            if target.startswith(("http://", "https://")):
                parsed = urlsplit(target)
                if not parsed.scheme or not parsed.netloc:
                    fail(f"nevaljana vanjska poveznica u {path.name}: {target}")
                continue
            local = target.split("#", 1)[0]
            if not local:
                continue
            resolved = (path.parent / local).resolve()
            if not resolved.is_file():
                fail(f"lokalna poveznica ne postoji u {path.name}: {target}")


def check_readme(artifact: dict) -> None:
    readme = README.read_text(encoding="utf-8")
    expected = {
        record["id"]: (record["promoted"], record.get("promoted_by"))
        for record in artifact.get("readme_status", [])
    }
    if expected != {
        "digikat_mediji": (True, "P3-DIGIKAT"),
        "rdp_potpore": (False, None),
        "bdp_dugi_niz": (False, None),
    }:
        fail("route artefakt ne čuva kanonske statuse triju izvedenih paketa")
    for fragment in (
        "`digikat_mediji` promoviran je paketom",
        "`P3-DIGIKAT`",
        "`rdp_potpore` i `bdp_dugi_niz` nisu promovirani",
        "| `digikat_mediji` | promoviran paketom `P3-DIGIKAT` |",
        "| `rdp_potpore` | nije promoviran |",
        "| `bdp_dugi_niz` | nije promoviran |",
    ):
        if fragment not in readme:
            fail(f"data/README.md nije usklađen s katalogom: {fragment}")
    if "Sva tri su prijavljena, nijedan nije promoviran" in readme:
        fail("data/README.md još nosi zastarjelu tvrdnju")


def run_clean_pathway(artifact: dict) -> None:
    with tempfile.TemporaryDirectory(prefix="appendix-c-clean-") as directory:
        stage = Path(directory)
        for relative in (
            "scripts/build-appendix-c-views.R",
            "data/katalog.yml",
            "data/anketa-mreze-agregat.csv",
            "data/populacija-medija-agregat.csv",
        ):
            copy_into(stage, relative)

        combined = run(
            [
                sys.executable,
                str(WRAPPER),
                str(stage / "scripts" / "build-appendix-c-views.R"),
                "--root",
                str(stage),
                "--write",
            ]
        )
        expected_banner = (
            "APPENDIX_C_VIEWS_OK packages=20 promoted=6 views=2 routes=20 "
            "aggregate_rows=9 dzs_admin=6 dzs_survey=3"
        )
        if expected_banner not in combined:
            fail(f"izolirana regeneracija nije prijavila puni ugovor:\n{combined}")

        for relative, canonical in (
            ("podaci.qmd", PUBLIC),
            ("dodaci/c-katalog-podataka.qmd", APPENDIX),
            ("config/appendix-c-data-route.json", ARTIFACT),
        ):
            staged = stage / relative
            if staged.read_bytes() != canonical.read_bytes():
                fail(f"izolirana regeneracija nije reproducirala {relative}")
        if load_artifact(stage / "config" / "appendix-c-data-route.json") != artifact:
            fail("izolirana regeneracija nije reproducirala strukturirani artefakt")


def main() -> None:
    artifact = load_artifact()
    public = PUBLIC.read_text(encoding="utf-8")
    appendix = APPENDIX.read_text(encoding="utf-8")

    check_artifact_contract(artifact)
    check_aggregate_contract(artifact, public, appendix)
    check_dzs(artifact, public, appendix)
    check_routes_and_links(artifact, public, appendix)
    check_readme(artifact)
    run_clean_pathway(artifact)

    print(
        "APPENDIX_C_CHECK_OK "
        "catalogue=verified regeneration=2/2 clean_pathway=verified "
        "routes=20/20 xrefs=verified local_links=verified "
        "aggregate_rows=9 shares=14 means=23 "
        "dzs_admin_residual=0 dzs_survey_residual=1 "
        "readme=canonical print_tables=present"
    )


if __name__ == "__main__":
    main()
