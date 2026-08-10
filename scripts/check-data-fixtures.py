#!/usr/bin/env python3
"""Prove that every declared data defect fails closed, and fails for its own reason.

P3-CATALOG proved ten catalogue-level defects. P3-EXISTING registered real
files, so the defect classes the review names -- keys, row bands, domains,
totals, units, weights and official aggregates -- can finally be exercised
against bytes on disk rather than against an empty catalogue.

Two harnesses run here:

* catalogue defects are injected in memory through KATALOG_NEGATIVE_FIXTURE and
  never touch a file;
* data defects are injected into a throwaway copy of the repository's data,
  R and script inputs, so the checked-out tree is never mutated.

Each case must exit non-zero AND print the message belonging to its own rule.
Exit status alone is too weak a proof: a fixture that fails for an unrelated
reason would otherwise look like evidence for a rule it never exercised.

Run:
    python scripts/check-data-fixtures.py
"""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "bookwright_plugin/bookwright/scripts/run_rscript.py"

ANALYSIS = "data/anketa-mreze.csv"
AGGREGATE = "data/anketa-mreze-agregat.csv"
NOTICE = "data/anketa-mreze.LICENCA.md"

# --- catalogue defects: fixture name -> the message it must produce ---------
CATALOGUE_CASES: tuple[tuple[str, str], ...] = (
    ("promote_portal_mediated", "only a bundled package may be promoted"),
    ("promote_without_checksum", "promotion requires a recorded checksum"),
    ("unknown_lane", "lane is not one of the three ratified lanes"),
    ("missing_fallback", "needs one lawful fallback"),
    ("licence_not_applicable", "licence may never be blank"),
    ("duplicate_package_id", "duplicate package id"),
    ("cap_exceeded", "registered packages exceed the cap"),
    ("undeclared_snapshot", "are not declared by any catalogue entry"),
    ("rights_permission_claimed", "may not permit a rights-holder permission claim"),
    ("duplicate_consumer_role", "two packages share one consumer role"),
    ("checksum_mismatch", "but the catalogue records"),
    ("missing_declared_file", "declared file is absent from disk"),
    ("snapshot_notice_missing", "declared snapshot licence notice is absent"),
    ("promoted_without_its_gate", "must record promoted_by equal to its"),
    ("promotion_log_disagrees", "the promotion log accounts for"),
    ("storage_disposition_missing", "promotion requires a storage-fidelity disposition"),
    ("undeclared_consumer", "uses the package without being declared"),
    ("promoted_under_decision_gate", "a decision gate may not be the promoting gate"),
    ("ratifying_record_missing", "moved the promoting gate names no existing record"),
    ("promotion_log_omits_package", "promotions but names"),
    ("notice_without_own_licence", "no direct link to the package's own licence"),
    ("non_official_substitute_incomplete",
     "satisfied non-official substitute with all three tests"),
)

DZS_MONTHLY = "data/dzs-turizam-mjesecno.csv"
DZS_COUNTY = "data/dzs-turizam-zupanije-2025.csv"
DZS_SURVEY = "data/dzs-putovanja-stanovnistva-2024.csv"


def run(command: list[str], cwd: Path, env: dict[str, str] | None = None) -> tuple[int, str]:
    result = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.returncode, result.stdout


def expect_failure(name: str, expected: str, code: int, output: str) -> None:
    encoding = sys.stdout.encoding or "utf-8"
    print(f"===== EXPECTED FAILURE: {name} =====")
    print(output.encode(encoding, errors="replace").decode(encoding), end="")
    if code == 0:
        raise RuntimeError(f"{name}: fixture unexpectedly passed")
    if expected not in output:
        raise RuntimeError(
            f"{name}: exited {code} but never printed its own message: {expected!r}"
        )
    print(f"EXPECTED_FAILURE fixture={name} exit={code}")


def edit_lines(path: Path, mutate) -> None:
    lines = path.read_text(encoding="utf-8").split("\n")
    path.write_text("\n".join(mutate(lines)), encoding="utf-8", newline="")


def replace_field(line: str, index: int, value: str) -> str:
    fields = line.split(",")
    fields[index] = value
    return ",".join(fields)


# --- data defects: name -> (mutation, the message it must produce) ----------

def mutate_duplicate_key(root: Path) -> None:
    def change(lines: list[str]) -> list[str]:
        lines[2] = replace_field(lines[2], 0, lines[1].split(",")[0])
        return lines
    edit_lines(root / ANALYSIS, change)


def mutate_row_band(root: Path) -> None:
    def change(lines: list[str]) -> list[str]:
        del lines[-2]
        return lines
    edit_lines(root / ANALYSIS, change)


def mutate_domain(root: Path) -> None:
    def change(lines: list[str]) -> list[str]:
        lines[1] = replace_field(lines[1], 5, "11")
        return lines
    edit_lines(root / ANALYSIS, change)


def mutate_code_label(root: Path) -> None:
    def change(lines: list[str]) -> list[str]:
        lines[1] = replace_field(lines[1], 3, "45 i više")
        return lines
    edit_lines(root / ANALYSIS, change)


def mutate_empty_cell(root: Path) -> None:
    def change(lines: list[str]) -> list[str]:
        lines[1] = replace_field(lines[1], 4, "")
        return lines
    edit_lines(root / ANALYSIS, change)


def mutate_rounded_mean(root: Path) -> None:
    def change(lines: list[str]) -> list[str]:
        lines[1] = replace_field(lines[1], 6, "81.54")
        return lines
    edit_lines(root / AGGREGATE, change)


def mutate_total(root: Path) -> None:
    def change(lines: list[str]) -> list[str]:
        lines[1] = replace_field(lines[1], 5, "7340")
        return lines
    edit_lines(root / AGGREGATE, change)


def mutate_share(root: Path) -> None:
    def change(lines: list[str]) -> list[str]:
        lines[1] = replace_field(lines[1], 4, "0.31")
        return lines
    edit_lines(root / AGGREGATE, change)


def mutate_notice(root: Path) -> None:
    target = root / NOTICE
    text = target.read_text(encoding="utf-8")
    target.write_text(
        text.replace("https://creativecommons.org/licenses/by/4.0/legalcode", "poveznica"),
        encoding="utf-8",
    )


def mutate_snapshot_drift(root: Path) -> None:
    def change(lines: list[str]) -> list[str]:
        lines[1] = replace_field(lines[1], 4, "70")
        return lines
    edit_lines(root / ANALYSIS, change)


def mutate_undeclared(root: Path) -> None:
    (root / "data/fixture-neprijavljena.csv").write_text("a,b\n1,2\n", encoding="utf-8")


def mutate_missing_file(root: Path) -> None:
    (root / AGGREGATE).unlink()


def mutate_weights_column(root: Path) -> None:
    target = root / "data/katalog.yml"
    text = target.read_text(encoding="utf-8")
    marker = "      weights: null\n"
    if marker not in text:
        raise RuntimeError("no weights disposition to mutate")
    target.write_text(
        text.replace(marker, '      weights: "tezina_uzorkovanja"\n', 1),
        encoding="utf-8",
    )


# --- the external-source half, which only a published package can exercise ---

def mutate_source_total(root: Path) -> None:
    """Move one county figure. The published national total no longer matches."""
    def change(lines: list[str]) -> list[str]:
        lines[4] = replace_field(lines[4], 4, "999999")
        return lines
    edit_lines(root / DZS_COUNTY, change)


def mutate_recorded_residual(root: Path) -> None:
    """Claim the survey reconciles exactly. It does not, and by exactly one."""
    target = root / "data/katalog.yml"
    text = target.read_text(encoding="utf-8")
    marker = """        tolerance: 1
        max_abs_residual: 1
        comparisons: 72"""
    if marker not in text:
        raise RuntimeError("no recorded survey residual to mutate")
    target.write_text(text.replace(marker, marker.replace(
        "max_abs_residual: 1", "max_abs_residual: 0"), 1), encoding="utf-8")


def mutate_composite_key(root: Path) -> None:
    """Drop one column from a composite key. The remaining pair repeats."""
    target = root / "data/katalog.yml"
    text = target.read_text(encoding="utf-8")
    marker = 'key: "godina+mjesec_redni+turist"'
    if marker not in text:
        raise RuntimeError("no composite key to mutate")
    target.write_text(text.replace(marker, 'key: "godina+mjesec_redni"', 1),
                      encoding="utf-8")


def mutate_undeclared_missing_token(root: Path) -> None:
    """Swap one published absence code for another the column does not declare."""
    def change(lines: list[str]) -> list[str]:
        lines[1] = replace_field(lines[1], 8, "..")
        return lines
    edit_lines(root / DZS_SURVEY, change)


def mutate_level_outside(root: Path) -> None:
    """Rename a published category. A quietly renamed level is a real defect."""
    def change(lines: list[str]) -> list[str]:
        lines[1] = replace_field(lines[1], 3, "Siječanj ")
        return lines
    edit_lines(root / DZS_MONTHLY, change)


DATA_CASES: tuple[tuple[str, object, str], ...] = (
    ("duplicate_key", mutate_duplicate_key, "key ispitanik is not unique"),
    ("row_band", mutate_row_band, "row count 299 differs from the declared 300"),
    ("domain_violation", mutate_domain, "rises above the declared maximum 10"),
    ("code_label_mismatch", mutate_code_label, "code and label disagree"),
    ("empty_cell", mutate_empty_cell, "declares no missing code, yet a cell is empty"),
    ("rounded_mean", mutate_rounded_mean, "a rounded mean cannot pass"),
    ("total_mismatch", mutate_total, "does not equal the sum of"),
    ("share_mismatch", mutate_share, "share udio does not equal broj / ukupno"),
    ("notice_without_licence", mutate_notice,
     "is missing https://creativecommons.org/licenses/by/4.0/legalcode"),
    ("snapshot_drift", mutate_snapshot_drift,
     "no longer reproduces from its declared generator and seed"),
    ("undeclared_snapshot_on_disk", mutate_undeclared,
     "are not declared by any catalogue entry"),
    ("missing_declared_snapshot", mutate_missing_file,
     "declared snapshot is missing from disk"),
    ("weights_column_absent", mutate_weights_column,
     "the declared weights column is absent from the analysis file"),
    ("source_total_mismatch", mutate_source_total,
     "above the declared tolerance 0"),
    ("recorded_residual_rounded_away", mutate_recorded_residual,
     "a residual is recorded exactly, never rounded away"),
    ("composite_key_not_unique", mutate_composite_key,
     "key godina+mjesec_redni is not unique"),
    ("undeclared_missing_token", mutate_undeclared_missing_token,
     "carries a missing token it does not declare"),
    ("level_outside_declared", mutate_level_outside,
     "carries a value outside its declared levels"),
)


def build_root(base: Path, name: str) -> Path:
    work = base / name
    work.mkdir()
    shutil.copytree(ROOT / "data", work / "data")
    (work / "R").mkdir()
    for source in ("podaci-nastavni.R", "snimke-nastavnih-podataka.R", "fetch-podaci.R"):
        shutil.copy2(ROOT / "R" / source, work / "R" / source)
    (work / "scripts").mkdir()
    shutil.copy2(ROOT / "scripts/check-katalog.py", work / "scripts/check-katalog.py")
    shutil.copy2(
        ROOT / "scripts/build-digikat-extracts.R",
        work / "scripts/build-digikat-extracts.R",
    )
    return work


def main() -> int:
    try:
        for fixture, expected in CATALOGUE_CASES:
            env = dict(os.environ, KATALOG_NEGATIVE_FIXTURE=fixture)
            code, output = run(
                [sys.executable, str(ROOT / "scripts/check-katalog.py")], ROOT, env
            )
            expect_failure(f"katalog:{fixture}", expected, code, output)

        env = dict(os.environ, KATALOG_NEGATIVE_FIXTURE="nepostojeca_greska")
        code, output = run(
            [sys.executable, str(ROOT / "scripts/check-katalog.py")], ROOT, env
        )
        expect_failure("katalog:unknown_fixture_name",
                       "Unknown katalog negative fixture", code, output)

        with tempfile.TemporaryDirectory(prefix="statistika-podaci-") as directory:
            base = Path(directory).resolve()
            if Path(tempfile.gettempdir()).resolve() not in base.parents:
                raise RuntimeError(f"unsafe fixture root: {base}")
            for name, mutate, expected in DATA_CASES:
                work = build_root(base, name)
                mutate(work)
                code, output = run(
                    [
                        sys.executable,
                        str(LAUNCHER),
                        str(ROOT / "scripts/check-data-integrity.R"),
                        "--root",
                        str(work),
                    ],
                    ROOT,
                )
                expect_failure(f"podaci:{name}", expected, code, output)

        code, output = run(
            [
                sys.executable,
                str(LAUNCHER),
                str(ROOT / "scripts/check-data-integrity.R"),
                "--fixture",
                "duplicate-key",
            ],
            ROOT,
        )
        expect_failure("podaci:in_memory_duplicate_key",
                       "contains a duplicate respondent key", code, output)

        total = len(CATALOGUE_CASES) + 1 + len(DATA_CASES) + 1
        print(f"DATA_NEGATIVE_FIXTURES_OK cases={total}")
        return 0
    except (OSError, RuntimeError) as error:
        print(f"data fixture proof: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
