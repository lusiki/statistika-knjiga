#!/usr/bin/env python3
"""Prove one deliberate fail-closed fixture for every P1C integrity lane."""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "bookwright_plugin/bookwright/scripts/run_rscript.py"


def run_expected_failure(name: str, command: list[str], cwd: Path) -> None:
    result = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    print(f"===== EXPECTED FAILURE: {name} =====")
    encoding = sys.stdout.encoding or "utf-8"
    safe_output = result.stdout.encode(encoding, errors="replace").decode(encoding)
    print(safe_output, end="")
    if result.returncode == 0:
        raise RuntimeError(f"{name} fixture unexpectedly passed")
    print(f"EXPECTED_FAILURE lane={name} exit={result.returncode}")


def copy_manuscript(work: Path) -> None:
    shutil.copytree(ROOT / "chapters", work / "chapters")
    shutil.copytree(ROOT / "dodaci", work / "dodaci")


def main() -> int:
    try:
        run_expected_failure(
            "token",
            [
                sys.executable,
                str(LAUNCHER),
                str(ROOT / "scripts/check-tokens.R"),
                "--fixture",
                "token-drift",
            ],
            ROOT,
        )

        with tempfile.TemporaryDirectory(prefix="statistika-integrity-") as directory:
            base = Path(directory).resolve()
            temp_root = Path(tempfile.gettempdir()).resolve()
            if temp_root not in base.parents:
                raise RuntimeError(f"unsafe fixture root: {base}")

            style_root = base / "style"
            style_root.mkdir()
            copy_manuscript(style_root)
            style_file = style_root / "chapters/01-zasto-statistika.qmd"
            style_file.write_text(
                style_file.read_text(encoding="utf-8") + "\nOvo je namjerna greška: dvotočka.\n",
                encoding="utf-8",
            )
            run_expected_failure(
                "style",
                [
                    sys.executable,
                    str(ROOT / "scripts/check-manuscript-integrity.py"),
                    "--root",
                    str(style_root),
                    "--lane",
                    "style",
                ],
                ROOT,
            )

            structure_root = base / "structure"
            structure_root.mkdir()
            copy_manuscript(structure_root)
            structure_file = structure_root / "chapters/01-zasto-statistika.qmd"
            structure_text = structure_file.read_text(encoding="utf-8")
            structure_text, replacements = structure_text.replace(
                "::: {.callout-vinjeta}", "::: {.callout-integrity-fixture}", 1
            ), structure_text.count("::: {.callout-vinjeta}")
            if replacements < 1:
                raise RuntimeError("structure fixture could not find a vignette")
            structure_file.write_text(structure_text, encoding="utf-8")
            run_expected_failure(
                "structure",
                [
                    sys.executable,
                    str(ROOT / "scripts/check-manuscript-integrity.py"),
                    "--root",
                    str(structure_root),
                    "--lane",
                    "structure",
                ],
                ROOT,
            )

            figure_root = base / "figure"
            figure_root.mkdir()
            shutil.copytree(ROOT / "chapters", figure_root / "chapters")
            (figure_root / "scripts").mkdir()
            shutil.copy2(ROOT / "scripts/integrity-debt.json", figure_root / "scripts/integrity-debt.json")
            figure_file = figure_root / "chapters/01-zasto-statistika.qmd"
            figure_file.write_text(
                figure_file.read_text(encoding="utf-8")
                + "\n## Namjerna figura bez uvoda\n\n![Fixture](fixture.png){#fig-integrity-fixture}\n",
                encoding="utf-8",
            )
            run_expected_failure(
                "figure",
                [
                    sys.executable,
                    str(ROOT / "scripts/check-figure-introductions.py"),
                    "--root",
                    str(figure_root),
                ],
                ROOT,
            )

            citation_root = base / "citation"
            citation_root.mkdir()
            copy_manuscript(citation_root)
            for source in ROOT.glob("*.qmd"):
                shutil.copy2(source, citation_root / source.name)
            shutil.copy2(ROOT / "references.bib", citation_root / "references.bib")
            shutil.copy2(ROOT / "_quarto.yml", citation_root / "_quarto.yml")
            for source in ROOT.glob("_quarto-*.yml"):
                shutil.copy2(source, citation_root / source.name)
            citation_file = citation_root / "chapters/01-zasto-statistika.qmd"
            citation_file.write_text(
                citation_file.read_text(encoding="utf-8")
                + "\nNamjerni nepoznati citat [@integrityfixture2099].\n",
                encoding="utf-8",
            )
            run_expected_failure(
                "citation",
                [
                    sys.executable,
                    str(ROOT / "scripts/check-citations.py"),
                    "--root",
                    str(citation_root),
                ],
                ROOT,
            )

            concept_root = base / "concept"
            concept_root.mkdir()
            shutil.copytree(ROOT / "chapters", concept_root / "chapters")
            shutil.copy2(ROOT / "_quarto.yml", concept_root / "_quarto.yml")
            shutil.copytree(ROOT / "data", concept_root / "data")
            shutil.copy2(ROOT / "pojmovnik.qmd", concept_root / "pojmovnik.qmd")
            ledger_dir = concept_root / "bookwright_plugin/bookwright/shared"
            ledger_dir.mkdir(parents=True)
            shutil.copy2(
                ROOT / "bookwright_plugin/bookwright/shared/concept-ledger.json",
                ledger_dir / "concept-ledger.json",
            )
            (concept_root / "scripts").mkdir()
            shutil.copy2(ROOT / "scripts/integrity-debt.json", concept_root / "scripts/integrity-debt.json")
            concept_file = concept_root / "chapters/01-zasto-statistika.qmd"
            concept_file.write_text(
                concept_file.read_text(encoding="utf-8")
                + "\n::: {#def-operacionalizacija}\n**Operacionalizacija** je namjerna dvostruka definicija.\n:::\n",
                encoding="utf-8",
            )
            run_expected_failure(
                "concept",
                [
                    sys.executable,
                    str(ROOT / "scripts/check-concepts.py"),
                    "--root",
                    str(concept_root),
                ],
                ROOT,
            )

        run_expected_failure(
            "data",
            [
                sys.executable,
                str(LAUNCHER),
                str(ROOT / "scripts/check-data-integrity.R"),
                "--fixture",
                "duplicate-key",
            ],
            ROOT,
        )
        print("INTEGRITY_NEGATIVE_FIXTURES_OK lanes=7")
        return 0
    except (OSError, RuntimeError, json.JSONDecodeError) as error:
        print(f"integrity fixture proof: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
