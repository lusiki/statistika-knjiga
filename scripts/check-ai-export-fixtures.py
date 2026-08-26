#!/usr/bin/env python3
"""Prove the P1C-EXPORT positive path and three fail-closed fixtures."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "bookwright_plugin/bookwright/scripts/run_rscript.py"
EXPORT_SCRIPT = ROOT / "R/build-ai-exports.R"


def export_command(project_root: Path, output_root: Path, *extra: str) -> list[str]:
    return [
        sys.executable,
        str(LAUNCHER),
        str(EXPORT_SCRIPT),
        "--release",
        f"--project-root={project_root}",
        f"--output-root={output_root}",
        *extra,
    ]


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def safe_print(output: str) -> None:
    encoding = sys.stdout.encoding or "utf-8"
    print(output.encode(encoding, errors="replace").decode(encoding), end="")


def require_success(name: str, result: subprocess.CompletedProcess[str]) -> None:
    print(f"===== POSITIVE: {name} =====")
    safe_print(result.stdout)
    if result.returncode != 0:
        raise RuntimeError(f"{name} failed with exit {result.returncode}")


def require_failure(
    name: str,
    result: subprocess.CompletedProcess[str],
    expected_fragment: str,
) -> None:
    print(f"===== EXPECTED FAILURE: {name} =====")
    safe_print(result.stdout)
    if result.returncode == 0:
        raise RuntimeError(f"{name} fixture unexpectedly passed")
    if expected_fragment.casefold() not in result.stdout.casefold():
        raise RuntimeError(
            f"{name} failed for the wrong reason; expected {expected_fragment!r}"
        )
    print(f"EXPECTED_FAILURE fixture={name} exit={result.returncode}")


def copy_export_sources(destination: Path) -> None:
    shutil.copy2(ROOT / "_quarto.yml", destination / "_quarto.yml")
    shutil.copy2(ROOT / "references.bib", destination / "references.bib")
    shutil.copy2(ROOT / "rjesenja.qmd", destination / "rjesenja.qmd")
    (destination / "config").mkdir()
    shutil.copy2(
        ROOT / "config/book-inventory.json",
        destination / "config/book-inventory.json",
    )
    shutil.copytree(ROOT / "chapters", destination / "chapters")
    shutil.copytree(ROOT / "dodaci", destination / "dodaci")
    (destination / "release").mkdir()
    shutil.copy2(
        ROOT / "release/governance.yml",
        destination / "release/governance.yml",
    )


def first_protected_body(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if "content-visible" in line and 'when-profile="kolegij"' in line:
            body: list[str] = []
            for candidate in lines[index + 1 :]:
                if candidate.strip().startswith(":::"):
                    break
                body.append(candidate)
            text = "\n".join(body).strip()
            if text:
                return text
    raise RuntimeError(f"no protected instructor block found in {path}")


def main() -> int:
    try:
        with tempfile.TemporaryDirectory(prefix="statistika-ai-export-") as directory:
            base = Path(directory).resolve()
            temp_root = Path(tempfile.gettempdir()).resolve()
            if temp_root not in base.parents:
                raise RuntimeError(f"unsafe fixture root: {base}")

            positive_output = base / "positive-output"
            require_success(
                "release-export",
                run(export_command(ROOT, positive_output)),
            )
            print("AI_EXPORT_POSITIVE_OK mode=release publish=false")

            build_root = base / "build-error-source"
            build_root.mkdir()
            copy_export_sources(build_root)
            missing_chapter = build_root / "chapters/18-vase-prvo-istrazivanje.qmd"
            missing_chapter.unlink()
            require_failure(
                "build-error",
                run(export_command(build_root, base / "build-error-output")),
                "nedostaje deklarirano poglavlje",
            )

            metadata_root = base / "metadata-drift-source"
            metadata_root.mkdir()
            copy_export_sources(metadata_root)
            quarto_path = metadata_root / "_quarto.yml"
            quarto = quarto_path.read_text(encoding="utf-8")
            original = '  title: "Osnove statistike za društvene znanosti"'
            drifted = '  title: "Namjerni metapodatkovni nesklad"'
            if quarto.count(original) != 1:
                raise RuntimeError("metadata fixture could not find the canonical title")
            quarto_path.write_text(quarto.replace(original, drifted), encoding="utf-8")
            require_failure(
                "metadata-drift",
                run(export_command(metadata_root, base / "metadata-drift-output")),
                "metadata drift",
            )

            leak_root = base / "protected-leak-source"
            leak_root.mkdir()
            copy_export_sources(leak_root)
            leak_output = base / "protected-leak-output"
            require_success(
                "protected-source-clean-build",
                run(export_command(leak_root, leak_output)),
            )
            # P5-ROUTES mora dokazati granicu stvarne odvojene rute rješenja,
            # a ne samo naslijediti probu nekoga profilnog bloka iz poglavlja.
            protected_body = first_protected_body(leak_root / "rjesenja.qmd")
            full_export = leak_output / "docs/llms-full.txt"
            with full_export.open("a", encoding="utf-8", newline="\n") as handle:
                handle.write(f"\n\n{protected_body}\n")
            require_failure(
                "protected-content-leak",
                run(
                    export_command(
                        leak_root,
                        leak_output,
                        "--validate-only",
                    )
                ),
                "protected-content leak",
            )

        print("AI_EXPORT_NEGATIVE_FIXTURES_OK fixtures=3 publish=false")
        return 0
    except (OSError, RuntimeError) as error:
        print(f"AI export fixture proof: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
