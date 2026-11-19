"""Verify the separate prose edition against its pinned first-version sources."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EDITION = ROOT / "editions/v2"


def normalized(text):
    return " ".join(text.split())


def chunks(text):
    found = re.findall(r"(?ms)^```[^\n]*\n.*?^```\s*$", text)
    # Captions and accessibility descriptions may use the neutral dataset name.
    return [re.sub(r"(?m)^#\|\s*(?:fig-cap|tbl-cap|fig-alt):.*\n", "", x) for x in found]


def table_numbers(text):
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        line = re.sub(r"\]\([^)]*\)", "]", line)
        line = re.sub(r"https?://\S+", "", line)
        rows.append(re.findall(r"(?<![\w/])\d+(?:[.,]\d+)*(?![\w/])", line))
    return rows


def answer_fields(value, path=()):
    """Retain field boundaries so moving or deleting evidence is detected."""
    if isinstance(value, dict):
        return [item for key, child in value.items()
                for item in answer_fields(child, path + (key,))]
    if isinstance(value, list):
        return [item for index, child in enumerate(value)
                for item in answer_fields(child, path + (index,))]
    if not isinstance(value, str):
        return [(path, value)]
    return [(path, {
        "numbers": re.findall(r"\d+(?:[.,]\d+)*", value),
        "citations": re.findall(r"@[A-Za-z][\w-]*", value),
        "technical_paths": re.findall(r"(?:data|chapters)/[^\s,]+", value),
    })]


def main():
    manifest = json.loads((EDITION / "edition.json").read_text(encoding="utf-8"))
    errors = []
    expected = dict(manifest["sources"])
    expected.update({"data/" + k: v for k, v in manifest["unchanged_data"].items()})
    expected[manifest["baseline_pdf"]["path"]] = manifest["baseline_pdf"]["sha256"]
    for name, sha in expected.items():
        raw = (ROOT / name).read_bytes()
        exact = hashlib.sha256(raw).hexdigest() == sha
        text_sha = manifest.get("source_content_sha256", {}).get(name)
        same_text = text_sha and hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest() == text_sha
        if not exact and not same_text:
            errors.append(f"First-version file changed: {name}")
    count = 0
    answer_count = 0
    for name in manifest["sources"]:
        if name.startswith("assessment/solution-records/"):
            old_answer = json.loads((ROOT / name).read_text(encoding="utf-8"))
            new_answer = json.loads((EDITION / name).read_text(encoding="utf-8"))
            if answer_fields(old_answer) != answer_fields(new_answer):
                errors.append(f"{name}: changed answer structure, numbers or evidence")
            answer_count += 1
        if not name.endswith(".qmd"):
            continue
        old = (ROOT / name).read_text(encoding="utf-8")
        new = (EDITION / name).read_text(encoding="utf-8")
        count += 1
        checks = {
            "executable chunks": (chunks(old), chunks(new)),
            "inline R": ([normalized(x) for x in re.findall(r"`r [^`]*`", old)],
                         [normalized(x) for x in re.findall(r"`r [^`]*`", new)]),
            "citation keys": (re.findall(r"(?<!\w)@([A-Za-z][\w-]*\d{4}[\w-]*)", old),
                              re.findall(r"(?<!\w)@([A-Za-z][\w-]*\d{4}[\w-]*)", new)),
            "Markdown table numbers": (table_numbers(old), table_numbers(new)),
            "Quarto block boundaries": (re.findall(r"(?m)^:{3,}.*$", old), re.findall(r"(?m)^:{3,}.*$", new)),
            "displayed math": ([normalized(x) for x in re.findall(r"\$\$(.*?)\$\$", old, re.S)],
                               [normalized(x) for x in re.findall(r"\$\$(.*?)\$\$", new, re.S)]),
        }
        for label, (a, b) in checks.items():
            if a != b:
                errors.append(f"{name}: changed {label}")
        # The inherited technical paths and keys remain usable. Search only
        # visible text, excluding code, attributes, citations and link targets.
        visible = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", new)
        visible = re.sub(r"<!--.*?-->", "", visible, flags=re.S)
        visible = re.sub(r"\{[^}]*\}", "", visible)
        visible = re.sub(r"\]\([^)]*\)", "]", visible)
        visible = re.sub(r"@digikat2026", "", visible)
        if re.search(r"digi(?:kat|kut)", visible, re.I):
            errors.append(f"{name}: visible old dataset name")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"EDITION_V2_OK sources={count} answer_records={answer_count} original_files={len(expected)} code_inline_R_citations_tables_blocks_math=preserved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
