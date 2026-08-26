#!/usr/bin/env python3
"""Fail-closed citation-key, blanket-nocite, and bibliography metadata check."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys


CHECKOUT_ROOT = Path(__file__).resolve().parents[1]
CITE_RE = re.compile(
    r"(?<![\w])@([A-Za-z][A-Za-z0-9_:-]*(?:\.[A-Za-z0-9_:-]+)*)"
)
QUARTO_XREF_RE = re.compile(
    r"^(?:fig|tbl|sec|eq|lst|thm|lem|cor|prp|cnj|def|exm|exr)-"
)


@dataclass(frozen=True)
class Entry:
    entry_type: str
    key: str
    fields: dict[str, str]


def strip_percent_comments(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("%"))


def split_top_level(text: str) -> list[str]:
    parts: list[str] = []
    start = 0
    depth = 0
    quote = False
    escaped = False
    for index, char in enumerate(text):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"' and depth == 0:
            quote = not quote
        elif not quote:
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
            elif char == "," and depth == 0:
                parts.append(text[start:index])
                start = index + 1
    parts.append(text[start:])
    return parts


def parse_bibtex(path: Path) -> dict[str, Entry]:
    text = strip_percent_comments(path.read_text(encoding="utf-8"))
    entries: dict[str, Entry] = {}
    position = 0
    header_re = re.compile(r"@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,")
    while True:
        match = header_re.search(text, position)
        if not match:
            break
        depth = 1
        quote = False
        escaped = False
        index = match.end()
        while index < len(text) and depth:
            char = text[index]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quote = not quote
            elif not quote:
                if char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
            index += 1
        if depth:
            raise ValueError(f"unterminated BibTeX entry {match.group(2)}")
        entry_type = match.group(1).lower()
        key = match.group(2)
        body = text[match.end() : index - 1]
        fields: dict[str, str] = {}
        for part in split_top_level(body):
            if not part.strip():
                continue
            field = re.match(r"\s*([A-Za-z][A-Za-z0-9_-]*)\s*=\s*(.+?)\s*$", part, re.S)
            if not field:
                raise ValueError(f"malformed field in {key}: {part.strip()[:80]}")
            name = field.group(1).lower()
            if name in fields:
                raise ValueError(f"duplicate field {name} in {key}")
            fields[name] = field.group(2).strip()
        if key in entries:
            raise ValueError(f"duplicate bibliography key: {key}")
        entries[key] = Entry(entry_type, key, fields)
        position = index
    if not entries:
        raise ValueError("references.bib contains no entries")
    residue = header_re.sub("", text)
    if re.search(r"(?m)^\s*@[A-Za-z]+\s*[{(]", residue):
        raise ValueError("one or more bibliography entries could not be parsed")
    return entries


def manuscript_files(root: Path) -> list[Path]:
    files = list((root / "chapters").glob("*.qmd"))
    files.extend((root / "dodaci").glob("*.qmd"))
    files.extend(root.glob("*.qmd"))
    return sorted(set(path.resolve() for path in files))


def validate_metadata(entries: dict[str, Entry]) -> list[str]:
    failures: list[str] = []
    type_requirements = {
        "article": {"author", "title", "journal", "volume", "number", "pages", "year", "doi"},
        "book": {"author", "title", "publisher", "year"},
        "inproceedings": {"author", "title", "booktitle", "pages", "year", "doi"},
        "unpublished": {"author", "title", "note", "year", "url"},
    }
    for key, entry in entries.items():
        required = type_requirements.get(entry.entry_type)
        if required is None:
            failures.append(f"{key}: unsupported entry type {entry.entry_type}")
            continue
        missing = sorted(required - entry.fields.keys())
        if missing:
            failures.append(f"{key}: missing required fields {missing}")
        year = entry.fields.get("year", "")
        year_match = re.search(r"\b(\d{4})\b", year)
        if not year_match:
            failures.append(f"{key}: year is not a four-digit value")
        elif not key.lower().endswith(year_match.group(1)):
            failures.append(f"{key}: key/year convention disagrees with {year_match.group(1)}")
        doi = entry.fields.get("doi")
        if doi:
            value = doi.strip().strip("{}").strip('"')
            if not re.fullmatch(r"10\.\d{4,9}/\S+", value):
                failures.append(f"{key}: malformed DOI {value!r}")
        for field_name in required or ():
            value = entry.fields.get(field_name, "").strip().strip("{}").strip('"').strip()
            if field_name in entry.fields and not value:
                failures.append(f"{key}: empty required field {field_name}")
    return failures


def is_quarto_crossref(key: str) -> bool:
    """Razdvoji Quarto identifikator objekta od bibliografskoga ključa."""
    return QUARTO_XREF_RE.match(key) is not None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=CHECKOUT_ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        files = manuscript_files(root)
        if not files:
            raise ValueError("no manuscript .qmd files found")
        cited: set[str] = set()
        crossrefs: set[str] = set()
        blanket_hits: list[str] = []
        for path in files:
            text = path.read_text(encoding="utf-8")
            visible = re.sub(r"<!--.*?-->", "", text, flags=re.S)
            for key in CITE_RE.findall(visible):
                if is_quarto_crossref(key):
                    crossrefs.add(key)
                else:
                    cited.add(key)
            if re.search(r"(?im)^\s*nocite\s*:\s*.*@\*", visible):
                blanket_hits.append(path.relative_to(root).as_posix())
        for path in [root / "_quarto.yml", *root.glob("_quarto-*.yml")]:
            if path.exists() and re.search(
                r"(?im)^\s*nocite\s*:\s*.*@\*", path.read_text(encoding="utf-8")
            ):
                blanket_hits.append(path.relative_to(root).as_posix())

        entries = parse_bibtex(root / "references.bib")
        failures = validate_metadata(entries)
        unknown = sorted(cited - entries.keys())
        unused = sorted(entries.keys() - cited)
        if blanket_hits:
            failures.append(f"forbidden blanket nocite in {sorted(blanket_hits)}")
        if unknown:
            failures.append(f"unknown citation keys: {unknown}")
        if unused:
            failures.append(f"unused maintained bibliography records: {unused}")
        if failures:
            raise ValueError("\n- ".join(["citation gate failed", *failures]))
        print(
            "CITATION_INTEGRITY_OK "
            f"files={len(files)} live_keys={len(cited)} quarto_crossrefs={len(crossrefs)} "
            f"records={len(entries)} blanket_nocite=0"
        )
        return 0
    except (OSError, ValueError) as error:
        print(f"citation integrity: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
