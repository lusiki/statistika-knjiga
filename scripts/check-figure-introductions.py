#!/usr/bin/env python3
"""Make checkout-local figure-introduction findings fail closed."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys


CHECKOUT_ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = CHECKOUT_ROOT / "bookwright_plugin/bookwright/scripts/run_rscript.py"
CHECKER = CHECKOUT_ROOT / "bookwright_plugin/bookwright/skills/book-figure/scripts/figure_intro_check.R"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=CHECKOUT_ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    debt_path = root / "scripts/integrity-debt.json"
    try:
        debt = json.loads(debt_path.read_text(encoding="utf-8"))
        expected = {
            (entry["file"].replace("\\", "/"), entry["figure"])
            for entry in debt.get("figure_introductions", [])
        }
        result = subprocess.run(
            [
                sys.executable,
                str(LAUNCHER),
                str(CHECKER),
                str(root / "chapters/*.qmd"),
            ],
            cwd=root,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        print(result.stdout, end="")
        if result.returncode:
            raise RuntimeError(f"figure_intro_check.R exited {result.returncode}")

        actual: set[tuple[str, str]] = set()
        current_file = ""
        for line in result.stdout.splitlines():
            heading = re.match(r"^==\s+(.+?)\s+\(\d+ conceptual figure", line)
            if heading:
                path = Path(heading.group(1))
                try:
                    current_file = path.resolve().relative_to(root).as_posix()
                except ValueError:
                    current_file = path.as_posix()
                continue
            finding = re.match(r"^\s+L\d+\s+(fig-[A-Za-z0-9_-]+)\s+", line)
            if finding and current_file:
                actual.add((current_file, finding.group(1)))

        unexpected = sorted(actual - expected)
        stale = sorted(expected - actual)
        if unexpected or stale:
            details = []
            if unexpected:
                details.append(f"unregistered missing introductions: {unexpected}")
            if stale:
                details.append(f"stale debt entries must be removed: {stale}")
            raise RuntimeError("; ".join(details))
        print(
            "FIGURE_INTRO_OK "
            f"registered_debt={len(expected)} unexpected=0 stale_debt=0"
        )
        return 0
    except (OSError, KeyError, ValueError, json.JSONDecodeError, RuntimeError) as error:
        print(f"figure introduction integrity: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
