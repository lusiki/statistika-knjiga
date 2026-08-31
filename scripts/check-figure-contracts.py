#!/usr/bin/env python3
"""Verify captions, alt text, and widget/print-twin figure pairs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CHUNK = re.compile(
    r"^```\{(?P<language>r|ojs)\}\s*\n(?P<body>.*?)^```\s*$",
    re.MULTILINE | re.DOTALL,
)
LABEL = re.compile(r"^(?:#|//)\| label: (fig-[A-Za-z0-9_-]+)\s*$", re.MULTILINE)
CAPTION = re.compile(r"^(?:#|//)\| fig-cap: \S.*$", re.MULTILINE)
ALT = re.compile(r"^(?:#|//)\| fig-alt: \S.*$", re.MULTILINE)
DIV_FIGURE = re.compile(r"^(?P<fence>:{3,}) \{#(?P<label>fig-[A-Za-z0-9_-]+)[^}]*\}\s*$", re.MULTILINE)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    labelled: dict[str, tuple[Path, int, bool, bool]] = {}
    divs: dict[str, tuple[Path, int]] = {}

    for chapter in sorted((root / "chapters").glob("*.qmd")):
        text = chapter.read_text(encoding="utf-8")
        relative = chapter.relative_to(root)
        for match in CHUNK.finditer(text):
            body = match.group("body")
            label_match = LABEL.search(body)
            if not label_match:
                continue
            label = label_match.group(1)
            line = text.count("\n", 0, match.start()) + 1
            if label in labelled or label in divs:
                fail(errors, f"duplicate figure label {label}")
                continue
            has_caption = CAPTION.search(body) is not None
            has_alt = ALT.search(body) is not None
            labelled[label] = (relative, line, has_caption, has_alt)
            if not has_caption:
                fail(errors, f"{relative}:{line} {label}: missing fig-cap")
            if not has_alt:
                fail(errors, f"{relative}:{line} {label}: missing fig-alt")

        for match in DIV_FIGURE.finditer(text):
            label = match.group("label")
            fence = match.group("fence")
            line = text.count("\n", 0, match.start()) + 1
            closing = re.search(rf"^{re.escape(fence)}\s*$", text[match.end():], re.MULTILINE)
            if closing is None:
                fail(errors, f"{relative}:{line} {label}: unclosed figure div")
                continue
            segment = text[match.end():match.end() + closing.start()]
            if label in labelled or label in divs:
                fail(errors, f"duplicate figure label {label}")
                continue
            divs[label] = (relative, line)
            if ALT.search(segment) is None:
                fail(errors, f"{relative}:{line} {label}: missing figure-div alt text")
            plain_lines = [
                value.strip()
                for value in segment.splitlines()
                if value.strip()
                and not value.lstrip().startswith(("`", ":", "#|"))
            ]
            if not plain_lines or plain_lines[-1].startswith(("p_", "iscrtaj_")):
                fail(errors, f"{relative}:{line} {label}: missing figure-div caption")

    registry = json.loads((root / "data/widgets.json").read_text(encoding="utf-8"))
    widgets = registry.get("widgets", [])
    expected_ids = [f"w{number:02d}" for number in range(1, 18)]
    if [widget.get("id") for widget in widgets] != expected_ids:
        fail(errors, "widget registry must contain ordered w01..w17")
    for widget in widgets:
        widget_id = widget.get("id", "")
        chapter = Path(widget.get("poglavlje", ""))
        for label in (f"fig-{widget_id}", f"fig-{widget_id}-print"):
            record = labelled.get(label)
            if record is None:
                fail(errors, f"{widget_id}: expected figure label {label} exactly once")
            elif record[0] != chapter:
                fail(errors, f"{widget_id}: {label} is in {record[0]}, expected {chapter}")

    if errors:
        for error in errors:
            print(f"FIGURE_CONTRACT_ERROR {error}", file=sys.stderr)
        print(f"FIGURE_CONTRACTS_FAILED errors={len(errors)}", file=sys.stderr)
        return 1

    conceptual = {
        re.sub(r"-print$", "", label) for label in labelled
    } | set(divs)
    print(
        "FIGURE_CONTRACTS_OK "
        f"conceptual={len(conceptual)} labelled_chunks={len(labelled)} "
        f"figure_divs={len(divs)} widget_pairs={len(widgets)} captions=complete alt=complete"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
