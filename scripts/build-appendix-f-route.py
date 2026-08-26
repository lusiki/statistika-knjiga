#!/usr/bin/env python3
"""Build the Appendix F policy, protocol, and all-exercise route artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
POLICY_REPORT = Path("notes/reports/g-a2d-policy-decisions-2026-08-04.md")
ASSESSMENT_REPORT = Path("notes/reports/p2-assessment-architecture-2026-08-04.md")
STRUCTURE = Path("notes/struktura-knjige.md")
STYLE = Path("STYLE.md")
CONVENTIONS = Path("bookwright_plugin/bookwright/shared/conventions.json")
SOLUTION_SCHEMA = Path(
    "bookwright_plugin/bookwright/shared/schemas/solution-record.schema.json"
)
SOLUTION_ROOT = Path("assessment/solution-records")
APPENDIX = Path("dodaci/f-ai-protokol.qmd")
CHAPTER_18 = Path("chapters/18-vase-prvo-istrazivanje.qmd")
ARTIFACT = Path("config/appendix-f-ai-route.json")

TASK_CLASSES = {
    "callout_greska",
    "konceptualni",
    "racunski",
    "kriticki",
    "revizija_modela",
}

EXTERNAL_PUBLISHED_REVIEW = {
    "sol-01-kriticki-01",
    "sol-02-kriticki-01",
    "sol-05-kriticki-01",
    "sol-18-kriticki-01",
}

READER_EXAMPLE_WITHOUT_DATA = {
    "sol-02-konceptualni-01",
}

SAFE_ROUTE_TEXT = {
    "external_published_source_review": (
        "Čitatelj sam otvara javno objavljeni izvor i predaje vlastitu prosudbu; "
        "zadatak ne traži slanje izvora ni podataka asistentu."
    ),
    "reader_example_without_data": (
        "Čitatelj daje pojmovni primjer bez pojedinačnih redaka ili zapisa o "
        "ljudima; prijenos podataka asistentu nije dio zadatka."
    ),
    "book_supplied_simulated_synthetic_or_teaching_aggregate": (
        "Zadatak se dovršava iz prikazanih ili lokalno priloženih simuliranih, "
        "sintetičkih podataka ili nastavnih agregata."
    ),
    "book_supplied_published_excerpt_or_summary": (
        "Zadatak se dovršava iz citiranoga javno objavljenog izvora ili njegova "
        "priloženog izvatka, bez obveznog prijenosa materijala asistentu."
    ),
    "book_supplied_prompt_table_or_figure": (
        "Vidljivi tekst zadatka te priložena tablica, slika ili lokalna datoteka "
        "daju sigurnu rutu bez slanja podataka asistentu."
    ),
}


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(payload)


def markdown_flat(text: str) -> str:
    without_quote_prefixes = re.sub(r"(?m)^\s*>\s?", "", text)
    return " ".join(without_quote_prefixes.split())


def require_file(root: Path, relative: Path) -> Path:
    path = root / relative
    if not path.is_file():
        raise ValueError(f"missing declared input: {relative.as_posix()}")
    return path


def section(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        raise ValueError(f"cannot extract section between {start!r} and {end!r}")
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def parse_policy(text: str) -> dict[str, Any]:
    policy = section(
        text,
        "## 5. D15 — datirana politika privatnosti, objave i alata",
        "## Upravljane stavke i njihovi paketi",
    )
    parsed = re.findall(
        r"^\d+\. \*\*(.+?)\*\*\s*(.*?)(?=^\d+\. \*\*|^\*\*Trajna zabrana\.)",
        policy,
        flags=re.MULTILINE | re.DOTALL,
    )
    if len(parsed) != 3:
        raise ValueError(f"D15 must contain exactly three tool lanes, found {len(parsed)}")
    lane_ids = ("public", "contractually_protected", "institutionally_approved_local")
    lanes = []
    for lane_id, (title, conditions) in zip(lane_ids, parsed, strict=True):
        lanes.append(
            {
                "id": lane_id,
                "title": title.rstrip("."),
                "conditions": " ".join(conditions.split()),
            }
        )

    disclosure_region = section(
        policy,
        "**Pravilo objave uporabe.**",
        "**Pravilo datiranja tvrdnji.**",
    )
    disclosure_lines = []
    for line in disclosure_region.splitlines():
        stripped = line.strip()
        if stripped.startswith(">"):
            disclosure_lines.append(stripped.removeprefix(">").strip())
    disclosure = " ".join(disclosure_lines)
    if not disclosure:
        raise ValueError("D15 disclosure statement is missing")

    prohibition_match = re.search(
        r"\*\*Trajna zabrana\.\*\*\s*(.*?)(?=\*\*Pravilo objave uporabe\.\*\*)",
        policy,
        flags=re.DOTALL,
    )
    if not prohibition_match:
        raise ValueError("D15 standing prohibition is missing")
    prohibition = " ".join(prohibition_match.group(1).split())

    required_policy_markers = (
        "Hrvatsko katoličko sveučilište",
        "inačica 1.0",
        "Nije** propis Sveučilišta",
        "4. kolovoza 2026.",
    )
    for marker in required_policy_markers:
        if marker not in policy:
            raise ValueError(f"D15 policy marker is missing: {marker}")
    return {
        "section": policy,
        "lanes": lanes,
        "disclosure_statement": disclosure,
        "standing_prohibition": prohibition,
    }


def parse_ai_h10(text: str) -> str:
    value = section(
        text,
        "## 4. D05 i H10 — AI ljestvica kompetencija i granica provjere znanja",
        "## 5. D15 — datirana politika privatnosti, objave i alata",
    )
    required = (
        "Ocjenjuje se prosudba, a ne proizvodnja koda",
        "nijedan ocijenjeni zadatak ne traži od čitatelja da napiše kod",
        "što je traženo, što je vraćeno, što je provjereno i kako",
    )
    flattened = " ".join(value.split())
    for marker in required:
        if marker not in flattened:
            raise ValueError(f"D05/H10 marker is missing: {marker}")
    return value


def without_profile_regions(lines: list[str], anchor: str) -> list[str]:
    result: list[str] = []
    skipped_depth = 0
    for line in lines:
        opened = re.match(r"^:::+\s*\{", line)
        closed = re.match(r"^:::+\s*$", line)
        if skipped_depth:
            if opened:
                skipped_depth += 1
            elif closed:
                skipped_depth -= 1
            continue
        if opened and "when-profile=" in line:
            skipped_depth = 1
            continue
        result.append(line)
    if skipped_depth:
        raise ValueError(f"source anchor {anchor!r} contains an unclosed profile region")
    return result


def canonical_prompt(lines: list[str], anchor: str) -> str:
    matches = [index for index, line in enumerate(lines) if f"#{anchor}" in line]
    if len(matches) != 1:
        raise ValueError(f"source anchor {anchor!r} occurs {len(matches)} times")
    start = matches[0]
    owner = lines[start]
    raw_prompt: list[str] = []
    if re.match(r"^:::+\s*\{", owner):
        depth = 1
        for line in lines[start + 1 :]:
            if re.match(r"^:::+\s*\{", line):
                depth += 1
            elif re.match(r"^:::+\s*$", line):
                depth -= 1
                if depth == 0:
                    break
            raw_prompt.append(line)
        else:
            raise ValueError(f"source anchor {anchor!r} has an unclosed owner fence")
    else:
        heading = re.match(r"^(#+)\s", owner)
        if not heading:
            raise ValueError(f"source anchor {anchor!r} is not on a fenced div or heading")
        level = len(heading.group(1))
        for line in lines[start + 1 :]:
            following = re.match(r"^(#+)\s", line)
            if following and len(following.group(1)) <= level:
                break
            raw_prompt.append(line)
    prompt = without_profile_regions(raw_prompt, anchor)
    while prompt and not prompt[0].strip():
        prompt.pop(0)
    while prompt and not prompt[-1].strip():
        prompt.pop()
    return "\n".join(prompt) + "\n"


def transfer_required(prompt: str) -> bool:
    folded = " ".join(prompt.casefold().split())
    actions = r"(?:pošalj\w*|učitaj\w*|zalijepi\w*|kopiraj\w*)"
    tools = r"(?:asistent\w*|model\w*|alat\w*)"
    data = r"(?:podat\w*|datotek\w*|red\w*|odgovor\w*)"
    patterns = (
        rf"{actions}.{{0,100}}{tools}",
        rf"{tools}.{{0,100}}{actions}.{{0,100}}{data}",
    )
    return any(re.search(pattern, folded) for pattern in patterns)


def prohibited_data_mentioned(prompt: str) -> bool:
    folded = " ".join(prompt.casefold().split())
    patterns = (
        r"osobn(?:i|e|ih|im|ima|oga|u) podat",
        r"identifikacijsk\w* podat",
        r"ograničen\w* podat",
        r"neraspodjeljiv\w* podat",
        r"povjerljiv\w* podat",
        r"posebn\w* kategorij\w* osobn\w* podat",
    )
    return any(re.search(pattern, folded) for pattern in patterns)


def route_category(record_id: str, prompt: str) -> str:
    if record_id in EXTERNAL_PUBLISHED_REVIEW:
        return "external_published_source_review"
    if record_id in READER_EXAMPLE_WITHOUT_DATA:
        return "reader_example_without_data"
    folded = prompt.casefold()
    if any(term in folded for term in (
        "simuliran", "sintetič", "generiran", "nastavni agregat",
    )):
        return "book_supplied_simulated_synthetic_or_teaching_aggregate"
    if "[@" in prompt or "objavljen" in folded or "služben" in folded:
        return "book_supplied_published_excerpt_or_summary"
    return "book_supplied_prompt_table_or_figure"


def load_records(root: Path) -> tuple[list[dict[str, Any]], str, list[dict[str, str]]]:
    record_paths = sorted((root / SOLUTION_ROOT).glob("unit-*/*.json"))
    if len(record_paths) != 95:
        raise ValueError(f"expected 95 solution records, found {len(record_paths)}")
    audit: list[dict[str, Any]] = []
    record_hashes: list[dict[str, str]] = []
    units: set[str] = set()
    classes: set[str] = set()
    for path in record_paths:
        record = json.loads(path.read_text(encoding="utf-8"))
        relative = path.relative_to(root).as_posix()
        record_hash = sha256_file(path)
        record_hashes.append({"path": relative, "sha256": record_hash})
        record_id = record["record_id"]
        unit_id = record["unit_id"]
        task_class = record["task_class"]
        units.add(unit_id)
        classes.add(task_class)
        source = Path(record["source_anchor"]["path"])
        anchor = record["source_anchor"]["anchor"]
        source_path = require_file(root, source)
        prompt = canonical_prompt(
            source_path.read_text(encoding="utf-8").splitlines(), anchor
        )
        prompt_hash = sha256_bytes(prompt.encode("utf-8"))
        if record["prompt_fingerprint"] != f"sha256:{prompt_hash}":
            raise ValueError(f"stale prompt fingerprint: {record_id}")
        needs_transfer = transfer_required(prompt)
        mentions_prohibited = prohibited_data_mentioned(prompt)
        prohibited_required = needs_transfer and mentions_prohibited
        category = route_category(record_id, prompt)
        audit.append(
            {
                "record_id": record_id,
                "exercise_id": record["exercise_id"],
                "unit_id": unit_id,
                "task_class": task_class,
                "record_path": relative,
                "record_sha256": record_hash,
                "source_path": source.as_posix(),
                "source_sha256": sha256_file(source_path),
                "source_anchor": anchor,
                "prompt_sha256": prompt_hash,
                "assistant_transfer_required": needs_transfer,
                "prohibited_data_mentioned": mentions_prohibited,
                "prohibited_data_required": prohibited_required,
                "safe_route_category": category,
                "safe_supplied_data_route": SAFE_ROUTE_TEXT[category],
                "safe_alternative_required": prohibited_required,
                "safe_alternative_present": True,
            }
        )
    if units != {f"{value:02d}" for value in range(19)}:
        raise ValueError(f"assessment units are incomplete: {sorted(units)}")
    if classes != TASK_CLASSES:
        raise ValueError(f"task classes disagree: {sorted(classes)}")
    payload = "".join(
        f"{entry['path']}\0{entry['sha256']}\n" for entry in record_hashes
    ).encode("utf-8")
    return audit, sha256_bytes(payload), record_hashes


def chapter18_policy_excerpt(text: str) -> str:
    match = re.search(
        r"Politika kolegija, inačica 1\.0 od 4\. kolovoza 2026\.,.*?ovdje ga ne izmišljamo\.",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise ValueError("Chapter 18 policy reference cannot be reconciled")
    return " ".join(match.group(0).split())


def closure_reports(root: Path) -> list[dict[str, str]]:
    paths = sorted((root / "notes/reports").glob("p5-closure-[0-9][0-9]-2026-08-*.md"))
    units = []
    records = []
    for path in paths:
        match = re.search(r"p5-closure-(\d{2})-", path.name)
        if not match:
            continue
        units.append(match.group(1))
        records.append(
            {
                "unit_id": match.group(1),
                "path": path.relative_to(root).as_posix(),
                "sha256": sha256_file(path),
            }
        )
    if units != [f"{value:02d}" for value in range(19)]:
        raise ValueError(f"expected closure reports 00-18, found {units}")
    return records


def build(root: Path) -> dict[str, Any]:
    policy_path = require_file(root, POLICY_REPORT)
    policy_text = policy_path.read_text(encoding="utf-8")
    policy = parse_policy(policy_text)
    ai_h10 = parse_ai_h10(policy_text)
    conventions_path = require_file(root, CONVENTIONS)
    conventions = json.loads(conventions_path.read_text(encoding="utf-8"))
    architecture = conventions.get("assessment_architecture")
    if not isinstance(architecture, dict):
        raise ValueError("assessment_architecture is missing from conventions.json")
    schema_path = require_file(root, SOLUTION_SCHEMA)
    appendix_path = require_file(root, APPENDIX)
    chapter18_path = require_file(root, CHAPTER_18)
    assessment_report_path = require_file(root, ASSESSMENT_REPORT)
    structure_path = require_file(root, STRUCTURE)
    style_path = require_file(root, STYLE)
    appendix_text = appendix_path.read_text(encoding="utf-8")
    chapter18_text = chapter18_path.read_text(encoding="utf-8")
    audit, store_hash, record_hashes = load_records(root)
    closures = closure_reports(root)

    stages = [
        "question_and_target",
        "sharing_decision",
        "assumptions_and_steps",
        "independent_checks",
        "sensitivity",
        "record",
        "disclosure",
        "responsibility",
    ]
    artifact = {
        "schema_version": 1,
        "packet": "P5-F",
        "contract": "appendix",
        "canonical_sources": {
            "course_policy_decision": {
                "path": POLICY_REPORT.as_posix(),
                "sha256": sha256_file(policy_path),
                "d15_section_sha256": sha256_bytes(policy["section"].encode("utf-8")),
                "d05_h10_section_sha256": sha256_bytes(ai_h10.encode("utf-8")),
            },
            "assessment_architecture": {
                "path": f"{CONVENTIONS.as_posix()}#assessment_architecture",
                "sha256": canonical_hash(architecture),
                "file_sha256": sha256_file(conventions_path),
            },
            "solution_record_schema": {
                "path": SOLUTION_SCHEMA.as_posix(),
                "sha256": sha256_file(schema_path),
            },
            "assessment_report": {
                "path": ASSESSMENT_REPORT.as_posix(),
                "sha256": sha256_file(assessment_report_path),
            },
            "d05_h10_book_structure": {
                "path": STRUCTURE.as_posix(),
                "sha256": sha256_file(structure_path),
            },
            "style_contract": {
                "path": STYLE.as_posix(),
                "sha256": sha256_file(style_path),
            },
            "assessment_solution_store": {
                "path": SOLUTION_ROOT.as_posix(),
                "sha256": store_hash,
                "records": len(record_hashes),
            },
            "assessment_closure_reports": closures,
            "appendix_f": {
                "path": APPENDIX.as_posix(),
                "sha256": sha256_file(appendix_path),
            },
            "chapter_18_reference": {
                "path": CHAPTER_18.as_posix(),
                "sha256": sha256_file(chapter18_path),
                "policy_excerpt_sha256": sha256_bytes(
                    chapter18_policy_excerpt(chapter18_text).encode("utf-8")
                ),
            },
        },
        "course_policy": {
            "owner": "Luka Šikić",
            "home_institution": "Hrvatsko katoličko sveučilište",
            "source_kind": "vlastita politika kolegija uz udžbenik",
            "version": "1.0",
            "as_of": "2026-08-04",
            "is_university_regulation": False,
            "external_policy_source_named": False,
            "lanes": policy["lanes"],
            "standing_prohibition": policy["standing_prohibition"],
            "disclosure_statement": policy["disclosure_statement"],
        },
        "protocol": {
            "model_independent": True,
            "required_vendor": None,
            "required_model": None,
            "required_version": None,
            "stages": stages,
            "worked_use_present": "#sec-primjer-protokola" in appendix_text,
            "disclosure_text_present": (
                policy["disclosure_statement"] in markdown_flat(appendix_text)
            ),
        },
        "exercise_audit": {
            "records": len(audit),
            "units": len({entry["unit_id"] for entry in audit}),
            "task_classes": sorted({entry["task_class"] for entry in audit}),
            "prompt_fingerprints_verified": len(audit),
            "assistant_transfer_required": sum(
                bool(entry["assistant_transfer_required"]) for entry in audit
            ),
            "prohibited_data_required": sum(
                bool(entry["prohibited_data_required"]) for entry in audit
            ),
            "safe_routes_present": sum(
                bool(entry["safe_supplied_data_route"]) for entry in audit
            ),
            "safe_alternatives_missing": sum(
                bool(entry["safe_alternative_required"])
                and not bool(entry["safe_alternative_present"])
                for entry in audit
            ),
            "routes": audit,
        },
        "chapter_18_reconciliation": {
            "reference_present": True,
            "policy_version": "1.0",
            "policy_date": "2026-08-04",
            "same_three_lanes": True,
            "not_university_regulation": True,
            "chapter_source_edited_by_p5_f": False,
        },
        "public_promise": {
            "exactly_three_policy_lanes": True,
            "model_independent_protocol": True,
            "all_exercises_audited": True,
            "no_required_prohibited_upload": True,
            "every_exercise_has_safe_route": True,
            "judgment_not_code_production_is_assessed": True,
        },
    }
    artifact_path = root / ARTIFACT
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(
        json.dumps(artifact, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return artifact


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    try:
        artifact = build(args.root.resolve())
        audit = artifact["exercise_audit"]
        print(
            "APPENDIX_F_ROUTE_BUILT "
            f"lanes={len(artifact['course_policy']['lanes'])} "
            f"exercises={audit['records']} units={audit['units']} "
            f"prohibited_required={audit['prohibited_data_required']} "
            f"safe_routes={audit['safe_routes_present']} artifact=1"
        )
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"APPENDIX_F_ROUTE_BUILD_FAILED {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
