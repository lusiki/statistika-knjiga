#!/usr/bin/env python3
"""Provjeri verzioniranu jamovi rutu, izolirani put i paritet dodataka A/B."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QMD = ROOT / "dodaci" / "b-jamovi.qmd"
ARTIFACT = ROOT / "config" / "appendix-b-jamovi-route.json"
BUILDER = ROOT / "scripts" / "build-appendix-b-route.R"
APPENDIX_A_ROUTE = ROOT / "scripts" / "appendix-a-route.R"
WRAPPER = ROOT / "bookwright_plugin" / "bookwright" / "scripts" / "run_rscript.py"

EXPECTED_MD5 = {
    "data/anketa-mreze.csv": "b988c25a8017e2d4dcd26be160890e89",
    "data/populacija-medija.csv": "07e158ca6385fe406dd6741e680fd756",
    "data/parlament_oznake.csv": "55b1c4263009ab783911f094907312d9",
}

SUPPORTED = {
    "6:pearson_r",
    "7:p_mreze_dob_le_29",
    "8:se_povjerenje_n_100",
    "9:mean_povjerenje",
    "9:ci95_lower",
    "9:ci95_upper",
    "10:mean_difference_portal_minus_tisak",
    "11:cohen_d_portal_minus_tisak",
    "13:chi_squared",
    "13:cramers_v",
    "14:mean_difference_tv_minus_mreze",
    "14:welch_ci95_lower",
    "14:welch_ci95_upper",
    "15:anova_f",
    "15:eta_squared",
    "16:slope_dob",
    "16:coefficient_drustvene_mreze",
    "16:adjusted_r_squared",
    "A-tekst:prepared_rows",
}

GUARDED = {
    "10:permutation_p_two_sided",
    "12:raw_fixed_effect_estimate",
    "12:raw_ci95_lower",
    "12:raw_ci95_upper",
    "12:standardized_fixed_effect_estimate",
    "12:standardized_ci95_lower",
    "12:standardized_ci95_upper",
}


def fail(message: str) -> None:
    raise SystemExit(f"APPENDIX_B_CHECK_FAIL: {message}")


def md5(path: Path) -> str:
    digest = hashlib.md5()  # nosec B324 -- canonical identity, not security
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(command: list[str], *, cwd: Path = ROOT, timeout: int = 120) -> str:
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


def copy_into(stage: Path, relative: str) -> None:
    source = ROOT / relative
    target = stage / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def load_artifact(path: Path = ARTIFACT) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"artefakt nije čitljiv JSON: {error}")


def check_source_contract(artifact: dict) -> None:
    qmd = QMD.read_text(encoding="utf-8")
    builder = BUILDER.read_text(encoding="utf-8")
    catalogue = (ROOT / "data" / "katalog.yml").read_text(encoding="utf-8")

    required_qmd = (
        "jamovi 2.7.30.0",
        "jmv 2.7.7",
        "../config/appendix-b-jamovi-route.json",
        "{#sec-b-priprema}",
        "{#sec-b-rute}",
        "{#sec-b-granica}",
        "#| label: tbl-b-rute",
        "@tbl-b-rute",
        "(#sec-b-granica)",
        "data/anketa-mreze.csv",
        "data/populacija-medija.csv",
        "data/parlament_oznake.csv",
        "čistoj instalaciji",
        "Luka Sikic",
    )
    for fragment in required_qmd:
        if fragment not in qmd:
            fail(f"Dodatku B nedostaje obvezni trag: {fragment}")

    lowered = qmd.lower()
    for forbidden in ("ucbadmissions", "anscombe", "data/anketa.csv", "čista instalacija je prošla"):
        if forbidden in lowered:
            fail(f"Dodatak B sadrži zabranjenu rutu ili tvrdnju: {forbidden}")

    for fragment in (
        "APPENDIX_B_ROUTE_OK",
        "scripts/appendix-a-route.R",
        "pending_owner_verification",
        "product_version = \"2.7.30.0\"",
        "core_module_version = \"2.7.7\"",
    ):
        if fragment not in builder:
            fail(f"graditelju rute nedostaje ugovorni trag: {fragment}")

    for relative, expected in EXPECTED_MD5.items():
        actual = md5(ROOT / relative)
        if actual != expected:
            fail(f"MD5 {relative} je {actual}, a očekuje se {expected}")

    for required in (
        'id: "anketa_mreze"',
        'id: "populacija_medija"',
        'id: "parlasent"',
        'question: "Koliko vremena ljudi provode na mrezama i kako to ide uz povjerenje?"',
        'question: "Kako se povjerenje u medije mijenja s dobi i izvorom vijesti?"',
        'path: "data/parlament_oznake.csv"',
    ):
        if required not in catalogue:
            fail(f"katalog više ne nosi kanonski zapis: {required}")

    if artifact.get("schema_version") != "appendix-b-jamovi-route-v1":
        fail("pogrešna je inačica sheme artefakta")
    if artifact.get("packet") != "P5-B" or artifact.get("decision") != "D09":
        fail("artefakt nije vezan uz P5-B i D09")
    product = artifact.get("product", {})
    if product.get("product_version") != "2.7.30.0":
        fail("jamovi nije prikovan na 2.7.30.0")
    if product.get("core_module") != "jmv" or product.get("core_module_version") != "2.7.7":
        fail("ugrađeni jmv nije prikovan na 2.7.7")
    clean = artifact.get("clean_install", {})
    if clean.get("owner") != "Luka Sikic" or clean.get("status") != "pending_owner_verification":
        fail("vlasništvo ili stanje čiste instalacije nije sačuvano")
    if clean.get("claimed_by_packet") is not False:
        fail("P5-B ne smije tvrditi provjeru čiste instalacije")


def run_appendix_a(stage: Path) -> list[dict[str, str | float]]:
    output = stage / "appendix-a.csv"
    combined = run(
        [
            sys.executable,
            str(WRAPPER),
            str(stage / "scripts" / "appendix-a-route.R"),
            "--root",
            str(stage),
            "--output",
            str(output),
        ]
    )
    if "APPENDIX_A_ROUTE_OK chapters=6-16 checks=25" not in combined:
        fail(f"Dodatak A nije prijavio 25 brojčanih provjera:\n{combined}")
    with output.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    rows.append(
        {
            "chapter": "A-tekst",
            "dataset": "parlasent_hr",
            "file": "data/parlament_oznake.csv",
            "question": "Kako se ton parlamentarnih iskaza razlikuje s obzirom na stranačku pripadnost?",
            "metric": "prepared_rows",
            "value": 2698.0,
        }
    )
    return rows


def run_clean_pathway() -> tuple[dict, list[dict[str, str | float]]]:
    with tempfile.TemporaryDirectory(prefix="appendix-b-clean-") as temp:
        stage = Path(temp)
        for relative in (
            "scripts/build-appendix-b-route.R",
            "scripts/appendix-a-route.R",
            "config/appendix-b-jamovi-route.json",
            "data/anketa-mreze.csv",
            "data/populacija-medija.csv",
            "data/parlament_oznake.csv",
            "notes/reports/p3-evidence12-rrr-lab-effects.csv",
        ):
            copy_into(stage, relative)

        combined = run(
            [
                sys.executable,
                str(WRAPPER),
                str(stage / "scripts" / "build-appendix-b-route.R"),
                "--root",
                str(stage),
                "--artifact",
                "config/appendix-b-jamovi-route.json",
            ]
        )
        expected_banner = (
            "APPENDIX_B_ROUTE_OK product=2.7.30.0 module=2.7.7 "
            "supported=19 guarded=7 total=26 clean_install=pending_owner"
        )
        if expected_banner not in combined:
            fail(f"izolirana ruta nije prijavila puni ugovorni rezultat:\n{combined}")

        staged_artifact = load_artifact(stage / "config" / "appendix-b-jamovi-route.json")
        appendix_a_rows = run_appendix_a(stage)
        return staged_artifact, appendix_a_rows


def check_parity(artifact: dict, appendix_a_rows: list[dict[str, str | float]]) -> None:
    scope = artifact.get("scope", {})
    supported = set(scope.get("supported_metric_keys", []))
    guarded = set(scope.get("unsupported_metric_keys", []))
    all_keys = set(scope.get("all_appendix_a_metric_keys", []))
    golden = artifact.get("golden_values", {})
    appendix_a_values = {
        f"{row['chapter']}:{row['metric']}": float(row["value"])
        for row in appendix_a_rows
    }

    if supported != SUPPORTED:
        fail(f"promijenio se podržani skup metrika: {sorted(supported ^ SUPPORTED)}")
    if guarded != GUARDED:
        fail(f"promijenio se ograđeni skup metrika: {sorted(guarded ^ GUARDED)}")
    if supported & guarded:
        fail("podržane i ograđene metrike se preklapaju")
    if all_keys != supported | guarded or scope.get("no_extra_metrics") is not True:
        fail("artefakt nije točna particija svih vrijednosti Dodatka A")
    if set(golden) != set(appendix_a_values):
        fail("Dodatak B nema isti popis očekivanih vrijednosti kao Dodatak A")

    for key, expected in appendix_a_values.items():
        actual = float(golden[key])
        if abs(actual - expected) > 1e-12:
            fail(f"paritet A/B ne prolazi za {key}: {actual} != {expected}")

    expected_contract = {
        f"{row['chapter']}:{row['metric']}": row for row in appendix_a_rows
    }
    contract_rows = artifact.get("appendix_a_contract", [])
    actual_contract = {
        f"{row['chapter']}:{row['metric']}": row for row in contract_rows
    }
    if set(actual_contract) != set(expected_contract):
        fail("artefakt nema isti ugovor redaka kao Dodatak A")
    for key, expected in expected_contract.items():
        actual = actual_contract[key]
        for field in ("dataset", "file", "question"):
            if actual.get(field) != expected[field]:
                fail(f"paritet A/B ne prolazi za {key}#{field}")
        if abs(float(actual["value"]) - float(expected["value"])) > 1e-12:
            fail(f"paritet A/B ne prolazi za {key}#value")

    routes = artifact.get("routes", [])
    route_keys: set[str] = set()
    ids: set[str] = set()
    required_route_fields = {
        "id",
        "file",
        "question",
        "variables",
        "import_types",
        "analysis",
        "menu_path",
        "settings",
        "filter",
        "weights",
        "expected_output",
        "golden_values",
        "export",
        "verification",
        "interpretation",
        "claim_boundary",
        "documentation_checked_at",
        "support_status",
        "clean_install",
    }
    for route in routes:
        missing = required_route_fields - set(route)
        if missing:
            fail(f"ruta {route.get('id')} nema polja {sorted(missing)}")
        if route["id"] in ids:
            fail(f"udvostručena ruta {route['id']}")
        ids.add(route["id"])
        if route["support_status"] != "documented_pending_clean_install":
            fail(f"ruta {route['id']} prekomjerno tvrdi status")
        if route["clean_install"].get("claimed_by_packet") is not False:
            fail(f"ruta {route['id']} prekomjerno tvrdi čistu instalaciju")
        if not route["menu_path"] or not route["documentation"]:
            fail(f"ruta {route['id']} nema dokumentiran izbornik ili izvor")
        variables = route["variables"]
        if isinstance(variables, str):
            variables = [variables]
        if set(variables) != set(route["import_types"]):
            fail(f"ruta {route['id']} nema tip uvoza za svaku varijablu")
        outputs = route["expected_output"]
        if isinstance(outputs, str):
            outputs = [outputs]
        route_keys.update(outputs)
        if set(outputs) != set(route["golden_values"]):
            fail(f"ruta {route['id']} nema točne vlastite zlatne vrijednosti")

    if route_keys != supported:
        fail("pojedinačne rute ne pokrivaju točno podržani skup")

    route_files = {route["file"] for route in routes}
    allowed_files = {
        "data/anketa-mreze.csv",
        "data/populacija-medija.csv",
        "data/parlament_oznake.csv",
    }
    if route_files != allowed_files:
        fail(f"ruta koristi pogrešne datoteke: {sorted(route_files)}")

    unsupported = artifact.get("unsupported_in_pinned_core", [])
    unsupported_keys: set[str] = set()
    for record in unsupported:
        for field in ("dataset", "file", "question", "variables", "reason"):
            if not record.get(field):
                fail(f"ograđena ruta poglavlja {record.get('chapter')} nema {field}")
        keys = record.get("metric_keys", [])
        if isinstance(keys, str):
            keys = [keys]
        unsupported_keys.update(keys)
    if unsupported_keys != guarded:
        fail("ograničenja prikovanoga jezgrenog modula nisu potpuna")


def main() -> None:
    artifact = load_artifact()
    check_source_contract(artifact)
    staged_artifact, appendix_a_rows = run_clean_pathway()
    if staged_artifact != artifact:
        fail("izolirani put nije reproducirao kanonski artefakt")
    check_parity(artifact, appendix_a_rows)
    print(
        "APPENDIX_B_CHECK_OK "
        "route_artifact=verified clean_pathway=verified "
        "parity=26/26 supported=19 guarded=7 "
        "xrefs=verified print_table=present clean_install=pending_owner"
    )


if __name__ == "__main__":
    main()
