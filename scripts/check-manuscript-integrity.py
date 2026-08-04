#!/usr/bin/env python3
"""Fail-closed hard-style and fixed-core manuscript checks.

The checkout-local Bookwright diagnostics remain useful human-readable tools.
This wrapper turns only their deterministic hard-rule and fixed-core findings
into process exit status. S7 rhythm candidates remain a judgment pass and are
not silently promoted into hard failures.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys


CHECKOUT_ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = CHECKOUT_ROOT / "bookwright_plugin/bookwright/scripts/run_rscript.py"
STYLE_LINT = CHECKOUT_ROOT / "bookwright_plugin/bookwright/skills/book-style/scripts/style_lint.R"
STRUCTURE_SCAN = CHECKOUT_ROOT / "bookwright_plugin/bookwright/skills/book-continuity/scripts/structure_scan.R"


def run_r(script: Path, root: Path, *args: str) -> str:
    result = subprocess.run(
        [sys.executable, str(LAUNCHER), str(script), *args],
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
        raise RuntimeError(f"{script.name} exited {result.returncode}")
    return result.stdout


def check_style(root: Path) -> None:
    output = run_r(
        STYLE_LINT,
        root,
        str(root / "chapters/*.qmd"),
        str(root / "dodaci/*.qmd"),
    )
    match = re.search(r"(?m)^(\d+) candidate\(s\) across (\d+) file\(s\)\.$", output)
    if not match:
        raise RuntimeError("style lint did not emit its deterministic summary")
    findings, files = map(int, match.groups())
    if findings:
        raise RuntimeError(f"hard-style gate found {findings} candidate(s)")
    print(f"MANUSCRIPT_STYLE_OK files={files}")


def check_structure(root: Path) -> None:
    output = run_r(STRUCTURE_SCAN, root, str(root / "chapters/*.qmd"))
    record_re = re.compile(
        r"(?m)^(?P<file>\S+\.qmd)\s+"
        r"vinjeta\s+(?P<vinjeta>\S+)\s+"
        r"def\s+(?P<definitions>\S+)\s+"
        r"fig\s+(?P<figures>.+?)\s+"
        r"divljina\s+(?P<divljina>\S+)\s+"
        r"ai\s+(?P<ai>\S+)\s+"
        r"zadaci\s+(?P<tasks>\d+/4)$"
    )
    records = [match.groupdict() for match in record_re.finditer(output)]
    expected = sorted(path.name for path in (root / "chapters").glob("*.qmd"))
    observed = sorted(record["file"] for record in records)
    failures: list[str] = []
    if observed != expected:
        failures.append(f"chapter inventory differs: expected {expected}, observed {observed}")
    if len(expected) != 19:
        failures.append(f"canonical chapter count is {len(expected)}, expected 19")
    if expected and [name[:2] for name in expected] != [f"{i:02d}" for i in range(19)]:
        failures.append("chapter basenames do not cover the contiguous 00-18 sequence")

    for record in records:
        name = record["file"]
        if record["vinjeta"] != "yes":
            failures.append(f"{name}: vinjeta missing or empty ({record['vinjeta']})")
        if record["divljina"] != "1":
            failures.append(f"{name}: callout-divljina count/content is {record['divljina']}")
        if record["ai"] != "2":
            failures.append(f"{name}: model/error callout count/content is {record['ai']}")
        if record["tasks"] != "4/4":
            failures.append(f"{name}: exercise tiers are {record['tasks']}")
        placeholder = re.search(r"placeholder\s+(\d+)", record["figures"])
        if not placeholder:
            failures.append(f"{name}: figure placeholder receipt is unreadable")
        elif int(placeholder.group(1)):
            failures.append(f"{name}: placeholder figure remains")

    if failures:
        raise RuntimeError("fixed-core structure gate failed:\n- " + "\n- ".join(failures))
    print(f"MANUSCRIPT_STRUCTURE_OK chapters={len(records)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=CHECKOUT_ROOT)
    parser.add_argument("--lane", choices=("all", "style", "structure"), default="all")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.lane in ("all", "style"):
            check_style(root)
        if args.lane in ("all", "structure"):
            check_structure(root)
    except (OSError, RuntimeError) as error:
        print(f"manuscript integrity: {error}", file=sys.stderr)
        return 1
    print(f"MANUSCRIPT_INTEGRITY_OK lane={args.lane}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
