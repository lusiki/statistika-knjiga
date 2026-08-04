#!/usr/bin/env python3
"""Prove that the P1C browser smoke audit fails on a broken browser route."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "scripts/audit-rendered-html.js"


def main() -> int:
    node = shutil.which("node")
    if not node:
        print("browser smoke fixture: node is not available", file=sys.stderr)
        return 1

    result = subprocess.run(
        [
            node,
            str(AUDIT),
            "--smoke",
            "--root",
            "docs",
            "--fixture",
            "missing-route",
        ],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    encoding = sys.stdout.encoding or "utf-8"
    safe_output = result.stdout.encode(
        encoding, errors="replace"
    ).decode(encoding)
    print("===== EXPECTED FAILURE: missing-route =====")
    print(safe_output, end="")
    if result.returncode == 0:
        print(
            "browser smoke fixture: missing route unexpectedly passed",
            file=sys.stderr,
        )
        return 1
    if "browser path returned HTTP 404" not in result.stdout:
        print(
            "browser smoke fixture failed for the wrong reason",
            file=sys.stderr,
        )
        return 1
    print(f"EXPECTED_FAILURE fixture=missing-route exit={result.returncode}")
    print("BROWSER_SMOKE_NEGATIVE_FIXTURES_OK fixtures=1 publish=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
