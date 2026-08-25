#!/usr/bin/env python3
"""Provjeri samostalnu R-rutu i čitateljsku putanju Dodatka A."""

from __future__ import annotations

import csv
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QMD = ROOT / "dodaci" / "a-praktikum.qmd"
ROUTE = ROOT / "scripts" / "appendix-a-route.R"
WRAPPER = ROOT / "bookwright_plugin" / "bookwright" / "scripts" / "run_rscript.py"

EXPECTED_MD5 = {
    "data/anketa-mreze.csv": "b988c25a8017e2d4dcd26be160890e89",
    "data/populacija-medija.csv": "07e158ca6385fe406dd6741e680fd756",
}

EXPECTED_VALUES = {
    ("6", "pearson_r"): 0.179849462681741,
    ("7", "p_mreze_dob_le_29"): 0.458576051779935,
    ("8", "se_povjerenje_n_100"): 0.198409986684138,
    ("9", "mean_povjerenje"): 4.815,
    ("9", "ci95_lower"): 4.52485748398763,
    ("9", "ci95_upper"): 5.10514251601237,
    ("10", "mean_difference_portal_minus_tisak"): -0.640938989801461,
    ("10", "permutation_p_two_sided"): 0.0117470632341915,
    ("11", "cohen_d_portal_minus_tisak"): -0.388897632206793,
    ("12", "raw_fixed_effect_estimate"): 0.026765925060349,
    ("12", "raw_ci95_lower"): -0.107693099301188,
    ("12", "raw_ci95_upper"): 0.161224949421886,
    ("12", "standardized_fixed_effect_estimate"): 0.0141509286792652,
    ("12", "standardized_ci95_lower"): -0.0761906831634761,
    ("12", "standardized_ci95_upper"): 0.104492540522006,
    ("13", "chi_squared"): 6.03709187333708,
    ("13", "cramers_v"): 0.0501543113523033,
    ("14", "mean_difference_tv_minus_mreze"): 1.18571428571429,
    ("14", "welch_ci95_lower"): 0.446686471420565,
    ("14", "welch_ci95_upper"): 1.92474210000801,
    ("15", "anova_f"): 8.38181295740898,
    ("15", "eta_squared"): 0.102053183237968,
    ("16", "slope_dob"): 0.0268851731781231,
    ("16", "coefficient_drustvene_mreze"): -0.533533786572297,
    ("16", "adjusted_r_squared"): 0.122189733503462,
    ("A-tekst", "prepared_rows"): 2698.0,
}

EXPECTED_QUESTIONS = {
    "anketa_mreze": "Koliko vremena ljudi provode na mrežama i kako to ide uz povjerenje?",
    "populacija_medija": "Kako se povjerenje u medije mijenja s dobi i izvorom vijesti?",
    "rrr_lab_effects": "Koliki je zajednički učinak laboratorijskih replikacija RRR-a?",
    "parlasent_hr": "Kako se ton parlamentarnih iskaza razlikuje s obzirom na stranačku pripadnost?",
}


def fail(message: str) -> None:
    raise SystemExit(f"APPENDIX_A_CHECK_FAIL: {message}")


def md5(path: Path) -> str:
    digest = hashlib.md5()  # nosec B324 -- canonical file identity, not security
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_sources() -> None:
    qmd = QMD.read_text(encoding="utf-8")
    route = ROUTE.read_text(encoding="utf-8")

    required_qmd = (
        "{#sec-a-ucitavanje}",
        "{#sec-a-rute-06-16}",
        "{#sec-a-tekst-transformacija}",
        "#| label: tbl-a-rute-provjera",
        "../scripts/appendix-a-route.R",
        '"data/anketa-mreze.csv"',
        '"data/populacija-medija.csv"',
        "(#sec-a-ucitavanje)",
        "(#sec-a-rute-06-16)",
        "(#tbl-a-rute-provjera)",
        "scripts/build-text-package.py",
        "data/parlament_oznake.csv",
    )
    for fragment in required_qmd:
        if fragment not in qmd:
            fail(f"Dodatku A nedostaje obvezni izvorni trag: {fragment}")

    lowered = qmd.lower()
    for forbidden in ("ucbadmissions", "anscombe", "data/anketa.csv"):
        if forbidden in lowered:
            fail(f"Dodatak A još sadrži zabranjenu ili nepostojeću rutu: {forbidden}")

    if 'source("R/setup.R")' in route or "source('R/setup.R')" in route:
        fail("samostalna ruta ovisi o R/setup.R")
    for fragment in (
        "APPENDIX_A_ROUTE_OK",
        "chapters=6-16",
        "--text-candidate",
        "build-text-package.py",
        "data/anketa-mreze.csv",
        "data/populacija-medija.csv",
        "p3-evidence12-rrr-lab-effects.csv",
    ):
        if fragment not in route:
            fail(f"samostalnoj ruti nedostaje ugovorni trag: {fragment}")

    for relative, expected in EXPECTED_MD5.items():
        actual = md5(ROOT / relative)
        if actual != expected:
            fail(f"MD5 {relative} je {actual}, a očekuje se {expected}")


def copy_into(stage: Path, relative: str) -> None:
    source = ROOT / relative
    target = stage / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def run_clean_pathway() -> tuple[list[dict[str, str]], str]:
    candidate_files = (
        "ParlaSent_BCS.jsonl",
        "ParlaSent_BCS_test.jsonl",
        "README.txt",
    )
    with tempfile.TemporaryDirectory(prefix="appendix-a-clean-") as temp:
        stage = Path(temp)
        for relative in (
            "scripts/appendix-a-route.R",
            "scripts/build-text-package.py",
            "data/anketa-mreze.csv",
            "data/populacija-medija.csv",
            "notes/reports/p3-evidence12-rrr-lab-effects.csv",
        ):
            copy_into(stage, relative)

        candidate = stage / "candidate"
        candidate.mkdir()
        for name in candidate_files:
            source = ROOT / "data" / "_kandidat" / "p3-text" / name
            if not source.exists():
                fail(f"nedostaje lokalni dokumentirani sirovi ulaz: {source}")
            shutil.copy2(source, candidate / name)

        output = stage / "route-results.csv"
        command = [
            sys.executable,
            str(WRAPPER),
            str(stage / "scripts" / "appendix-a-route.R"),
            "--root",
            str(stage),
            "--output",
            str(output),
            "--text-candidate",
            str(candidate),
            "--python",
            sys.executable,
        ]
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            check=False,
        )
        combined = completed.stdout + completed.stderr
        if completed.returncode != 0:
            fail(f"čista ruta nije prošla:\n{combined}")
        if "APPENDIX_A_ROUTE_OK chapters=6-16 checks=26 text_transform=verified" not in combined:
            fail(f"čista ruta nije prijavila puni ugovorni rezultat:\n{combined}")
        if not output.exists():
            fail("čista ruta nije proizvela izlazni CSV")
        with output.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        return rows, combined


def check_results(rows: list[dict[str, str]]) -> None:
    if len(rows) != len(EXPECTED_VALUES):
        fail(f"ruta je vratila {len(rows)} provjera; očekuju se {len(EXPECTED_VALUES)}")

    seen: set[tuple[str, str]] = set()
    chapters: set[int] = set()
    for row in rows:
        key = (row["chapter"], row["metric"])
        if key not in EXPECTED_VALUES:
            fail(f"neočekivana provjera u izlazu: {key}")
        if key in seen:
            fail(f"udvostručena provjera u izlazu: {key}")
        seen.add(key)
        actual = float(row["value"])
        if abs(actual - EXPECTED_VALUES[key]) > 1e-12:
            fail(f"{key} daje {actual}, a očekuje se {EXPECTED_VALUES[key]}")
        expected_question = EXPECTED_QUESTIONS[row["dataset"]]
        if row["question"] != expected_question:
            fail(f"pitanje za {row['dataset']} ne odgovara kanonskom zapisu")
        if row["chapter"].isdigit():
            chapters.add(int(row["chapter"]))

    if seen != set(EXPECTED_VALUES):
        fail("izlaz ne pokriva cijeli očekivani skup provjera")
    if chapters != set(range(6, 17)):
        fail(f"pokrivena su poglavlja {sorted(chapters)}, a očekuju se 6–16")


def main() -> None:
    check_sources()
    rows, _ = run_clean_pathway()
    check_results(rows)
    print(
        "APPENDIX_A_CHECK_OK "
        "route_artifact=verified clean_pathway=verified chapters=6-16 "
        "text_transform=verified xrefs=verified print_table=present"
    )


if __name__ == "__main__":
    main()
