#!/usr/bin/env python3
"""Prove that caption, alt-text, and print-twin regressions fail closed."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts/check-figure-contracts.py"


def run_fixture(base: Path, name: str, old: str, new: str, expected: str) -> None:
    fixture_root = base / name
    shutil.copytree(ROOT / "chapters", fixture_root / "chapters")
    (fixture_root / "data").mkdir()
    shutil.copy2(ROOT / "data/widgets.json", fixture_root / "data/widgets.json")
    target = fixture_root / "chapters/01-zasto-statistika.qmd"
    text = target.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"{name}: mutation anchor is absent")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(CHECKER), "--root", str(fixture_root)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    diagnostic = f"{result.stdout}\n{result.stderr}"
    if result.returncode == 0 or expected not in diagnostic:
        raise RuntimeError(f"{name}: fixture did not fail with {expected!r}\n{diagnostic}")


def main() -> int:
    try:
        with tempfile.TemporaryDirectory(prefix="statistika-figure-contract-") as directory:
            base = Path(directory).resolve()
            run_fixture(base, "missing-caption", "//| fig-cap:", "//| fixture-cap:", "missing fig-cap")
            run_fixture(base, "missing-alt", "//| fig-alt:", "//| fixture-alt:", "missing fig-alt")
            run_fixture(
                base,
                "missing-print-twin",
                "#| label: fig-w01-print",
                "#| label: fig-w01-print-broken",
                "expected figure label fig-w01-print exactly once",
            )
        print("FIGURE_CONTRACT_NEGATIVE_FIXTURES_OK fixtures=3")
        return 0
    except (OSError, RuntimeError) as error:
        print(f"FIGURE_CONTRACT_FIXTURE_ERROR {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
