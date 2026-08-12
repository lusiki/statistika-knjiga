#!/usr/bin/env python3
"""Prove that the widget parity gate rejects two numeric regressions."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    fixtures = {
        "expected-value-regression": "[golden] w01/ojs/default.aggregate_a",
        "normal-cache-asymmetry": "[golden] w09/ojs/",
    }
    for fixture, expected in fixtures.items():
        completed = subprocess.run(
            [
                sys.executable,
                str(root / "scripts" / "check-widget-parity.py"),
                str(root),
                "--fixture",
                fixture,
            ],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        diagnostic = f"{completed.stdout}\n{completed.stderr}"
        if completed.returncode == 0:
            print(
                f"WIDGET_PARITY_FIXTURE_ERROR {fixture} unexpectedly passed",
                file=sys.stderr,
            )
            return 1
        if expected not in diagnostic:
            print(
                f"WIDGET_PARITY_FIXTURE_ERROR {fixture} diagnostic was absent",
                file=sys.stderr,
            )
            print(diagnostic.strip(), file=sys.stderr)
            return 1
    print("WIDGET_PARITY_NEGATIVE_FIXTURES_OK fixtures=2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
