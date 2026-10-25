"""Read-only Croatian prose candidates and conservation checks for editorial passes.

No rewrite mode: every candidate needs contextual editorial judgment.
Snapshot files contain source text; keep them in ignored tmp/, never commit them.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sources():
    # Canonical order, excluding standalone site pages and generated apparatus.
    config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
    block = config.split("  chapters:\n", 1)[1].split("  # END GENERATED: book-inventory structure", 1)[0]
    return list(dict.fromkeys(re.findall(r"(?:chapters|dodaci)/[\w-]+\.qmd", block)))


def prose_lines(text):
    fence = None
    yaml = text.startswith("---\n")
    comment = False
    for n, line in enumerate(text.splitlines(), 1):
        if yaml:
            if n > 1 and line.strip() in {"---", "..."}:
                yaml = False
            continue
        if fence:
            if re.fullmatch(r"\s*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*", line):
                fence = None
            continue
        match = re.match(r"\s*(`{3,}|~{3,})", line)
        if match:
            fence = match[1]
            continue
        if "<!--" in line:
            comment = True
        if comment:
            if "-->" in line:
                comment = False
            continue
        if line.strip() and not re.match(r"\s*(:::|\|)", line):
            yield n, line


def protected(text):
    # Conservative invariants supplement, never replace, semantic review.
    lines = text.splitlines()
    blocks, current, fence = [], [], None
    for line in lines:
        if fence:
            current.append(line)
            if re.fullmatch(r"\s*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*", line):
                blocks.append("\n".join(current))
                current, fence = [], None
        else:
            match = re.match(r"\s*(`{3,}|~{3,})", line)
            if match:
                current, fence = [line], match[1]
    if fence:
        raise ValueError("Unclosed code fence")
    yaml = re.match(r"\A---\n.*?\n(?:---|\.\.\.)\n", text, re.S)
    return {
        "frontmatter": yaml[0] if yaml else "",
        "code_blocks": blocks,
        "inline_code": re.findall(r"`[^`\n]+`", text),
        "math": re.findall(r"\$\$[\s\S]*?\$\$|(?<!\$)\$[^$\n]+\$(?!\$)", text),
        "references": re.findall(r"(?<!\w)@[\w][\w:.-]*", text),
        "numbers": re.findall(r"(?<!\w)\d+(?:[.,]\d+)*(?:\s*%)?", text),
        "structure": [line for line in lines if re.match(r"\s*(#{1,6}\s|:::|\|)", line)],
        "attributes": re.findall(r"\{[^{}\n]*\}", text),
        "link_targets": re.findall(r"\]\(([^)]+)\)", text),
        "urls": re.findall(r"https?://[^\s<>\]\)]+", text),
        "comments": re.findall(r"<!--[\s\S]*?-->", text),
    }


PATTERNS = {
    "prazan_naglasak": r"\b(?:Važno je (?:naglasiti|istaknuti|napomenuti)|Valja (?:naglasiti|istaknuti|napomenuti)|Vrijedi (?:naglasiti|istaknuti|napomenuti)|ključno je (?:razumjeti|shvatiti)|u tom kontekstu)\b",
    "metatekst": r"\b(?:u ovom poglavlju|ovo poglavlje|u nastavku|sljedeći korak|time se|time smo|time je|ovdje se|ovdje je)\b",
    "kontrast_za_procjenu": r"\b(?:nije|nisu|ne znači|ne radi se|ne služi|nije riječ)\b[^.!?]{0,180}\b(?:nego|već|samo|ali)\b",
    "apstraktna_imenica": r"\b(?:čitateljsk\w*|inferencijaln\w*|epistemičk\w*|operacionalni|operativni|ugovor|kralježnic\w*|nosiv\w*|prag čitanja|kanonsk\w*|prikovan\w*|paritet\w*|promocij\w*|zlatn\w*|rut[aeiou])\b",
    "opci_zakljucak": r"\b(?:Pouka je|Zaključak je|To je razlog|Upravo (?:zato|stoga)|Drugim riječima|Naime|Točnije|Ukratko|Štoviše)\b",
}


def paragraphs(text):
    pending, start, last = [], 0, 0
    for n, line in prose_lines(text):
        if pending and (n != last + 1 or line.startswith("#")):
            yield start, " ".join(pending)
            pending = []
        if not pending:
            start = n
        pending.append(line.strip())
        last = n
    if pending:
        yield start, " ".join(pending)


def scan(paths):
    findings = []
    for path in paths:
        text = (ROOT / path).read_text(encoding="utf-8")
        for n, line in paragraphs(text):
            tags = [key for key, pattern in PATTERNS.items() if re.search(pattern, line, re.I)]
            if tags:
                findings.append({"file": path, "line": n, "candidates": tags, "text": line})
    return findings


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["snapshot", "scan", "verify", "read"])
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--files", nargs="*")
    args = parser.parse_args()
    paths = args.files or sources()
    if args.mode == "read":
        for path in paths:
            print("\n" + path)
            for n, line in paragraphs((ROOT / path).read_text(encoding="utf-8")):
                print(f"{n}: {line}")
        return
    if args.mode == "snapshot":
        result = {path: {"text": (ROOT / path).read_text(encoding="utf-8"),
                         "byte_sha256": hashlib.sha256((ROOT / path).read_bytes()).hexdigest()}
                  for path in paths}
    elif args.mode == "scan":
        result = {"notice": "Candidates only; no AI-origin score and no automatic edits.",
                  "files": paths, "findings": scan(paths)}
    else:
        if not args.baseline:
            parser.error("verify requires --baseline")
        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        result = {"files": [], "pass": True}
        for path, original in baseline.items():
            before = original["text"]
            after = (ROOT / path).read_text(encoding="utf-8")
            old, new = protected(before), protected(after)
            changed = [key for key in old if old[key] != new[key]]
            result["pass"] &= not changed
            changes = []
            a, b = before.splitlines(), after.splitlines()
            for tag, i, j, k, l in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
                if tag != "equal":
                    changes.append({"before_line": i + 1, "after_line": k + 1,
                                    "before": "\n".join(a[i:j]), "after": "\n".join(b[k:l])})
            result["files"].append({"file": path, "before_sha256": original["byte_sha256"],
                                    "after_sha256": hashlib.sha256((ROOT / path).read_bytes()).hexdigest(),
                                    "protected_changes": changed, "changes": changes})
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
        print(f"Wrote {args.output}")
        if args.mode == "verify":
            print(json.dumps({"pass": result["pass"], "changed_files": sum(bool(f['changes']) for f in result['files']),
                              "changed_passages": sum(len(f['changes']) for f in result['files']),
                              "protected_changes": {f['file']: f['protected_changes'] for f in result['files'] if f['protected_changes']}}))
    else:
        print(payload)
    if args.mode == "verify" and not result["pass"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
