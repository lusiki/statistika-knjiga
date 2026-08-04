#!/usr/bin/env python3
"""Prove that the widget parity gate rejects a golden-value regression."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    completed = subprocess.run(
        [
            sys.executable,
            str(root / "scripts" / "check-widget-parity.py"),
            str(root),
            "--fixture",
            "expected-value-regression",
        ],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    diagnostic = f"{completed.stdout}\n{completed.stderr}"
    expected = "[golden] w01/ojs/default.aggregate_a"
    if completed.returncode == 0:
        print("WIDGET_PARITY_FIXTURE_ERROR regression fixture unexpectedly passed", file=sys.stderr)
        return 1
    if expected not in diagnostic:
        print("WIDGET_PARITY_FIXTURE_ERROR expected golden diagnostic was absent", file=sys.stderr)
        print(diagnostic.strip(), file=sys.stderr)
        return 1
    print("WIDGET_PARITY_NEGATIVE_FIXTURES_OK fixtures=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
