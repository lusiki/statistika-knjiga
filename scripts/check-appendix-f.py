#!/usr/bin/env python3
"""Verify Appendix F policy lanes, protocol, exercise audit, and proof inputs."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BUILDER = Path("scripts/build-appendix-f-route.py")
ARTIFACT = Path("config/appendix-f-ai-route.json")
FIXTURES = (
    "lane_dropped",
    "sensitive_transfer_required",
    "vendor_required",
)


def load_builder(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("appendix_f_builder", path)
    if spec is None or spec.loader is None:
        raise AssertionError("cannot load Appendix F route builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILDER_MODULE = load_builder(ROOT / BUILDER)


def fail(message: str) -> None:
    raise AssertionError(message)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(base: Path, relative: Path) -> Any:
    path = base / relative
    if not path.is_file():
        fail(f"missing={relative.as_posix()}")
    return json.loads(path.read_text(encoding="utf-8"))


def fold(text: str) -> str:
    return " ".join(text.casefold().split())


def heading_id(text: str) -> str:
    text = re.sub(r"\s+\{.*\}\s*$", "", text.strip()).casefold()
    kept = []
    for character in text:
        category = unicodedata.category(character)
        if character.isspace():
            kept.append("-")
        elif category[0] in {"L", "N"} or character in {"_", "-", "."}:
            kept.append(character)
    return re.sub(r"-+", "-", "".join(kept)).strip("-")


def anchor_exists(path: Path, anchor: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if re.search(rf"#({re.escape(anchor)})(?:[\s}}]|$)", text):
        return True
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match and heading_id(match.group(1)) == anchor:
            return True
    return False


def policy_table_rows(text: str) -> list[str]:
    match = re.search(
        r"\| Traka \| Dopušteni podaci \| Točan uvjet \|\n"
        r"\|---\|---\|---\|\n(.*?)\n\n:",
        text,
        flags=re.DOTALL,
    )
    if not match:
        fail("reader-visible three-lane table is missing")
    return [line for line in match.group(1).splitlines() if line.startswith("|")]


def validate(base: Path, fixture: str = "", check_git_boundary: bool = False) -> dict[str, int | str]:
    builder = load_builder(base / BUILDER)
    artifact = copy.deepcopy(load_json(base, ARTIFACT))
    if fixture == "lane_dropped":
        artifact["course_policy"]["lanes"].pop()
    elif fixture == "sensitive_transfer_required":
        route = artifact["exercise_audit"]["routes"][0]
        route["assistant_transfer_required"] = True
        route["prohibited_data_mentioned"] = True
        route["prohibited_data_required"] = True
    elif fixture == "vendor_required":
        artifact["protocol"]["model_independent"] = False
        artifact["protocol"]["required_vendor"] = "obvezni proizvođač"
    elif fixture:
        fail(f"unknown negative fixture={fixture}")

    if artifact.get("schema_version") != 1 or artifact.get("packet") != "P5-F":
        fail("route artifact identity")
    if artifact.get("contract") != "appendix":
        fail("route artifact contract")

    policy_path = base / builder.POLICY_REPORT
    policy_text = policy_path.read_text(encoding="utf-8")
    policy = builder.parse_policy(policy_text)
    ai_h10 = builder.parse_ai_h10(policy_text)
    conventions = load_json(base, builder.CONVENTIONS)
    architecture = conventions.get("assessment_architecture")
    if not isinstance(architecture, dict):
        fail("assessment_architecture is missing")

    canonical = artifact.get("canonical_sources", {})
    decision_source = canonical.get("course_policy_decision", {})
    if decision_source.get("path") != builder.POLICY_REPORT.as_posix():
        fail("course policy source path")
    if decision_source.get("sha256") != sha256_file(policy_path):
        fail("course policy source hash is stale")
    if decision_source.get("d15_section_sha256") != hashlib.sha256(
        policy["section"].encode("utf-8")
    ).hexdigest():
        fail("D15 section hash is stale")
    if decision_source.get("d05_h10_section_sha256") != hashlib.sha256(
        ai_h10.encode("utf-8")
    ).hexdigest():
        fail("D05/H10 section hash is stale")

    architecture_source = canonical.get("assessment_architecture", {})
    if architecture_source.get("path") != (
        f"{builder.CONVENTIONS.as_posix()}#assessment_architecture"
    ):
        fail("assessment architecture source path")
    if architecture_source.get("sha256") != builder.canonical_hash(architecture):
        fail("assessment architecture hash is stale")
    if architecture_source.get("file_sha256") != sha256_file(base / builder.CONVENTIONS):
        fail("conventions file hash is stale")
    if canonical.get("solution_record_schema", {}).get("sha256") != sha256_file(
        base / builder.SOLUTION_SCHEMA
    ):
        fail("solution record schema hash is stale")
    for key, relative in (
        ("assessment_report", builder.ASSESSMENT_REPORT),
        ("d05_h10_book_structure", builder.STRUCTURE),
        ("style_contract", builder.STYLE),
        ("appendix_f", builder.APPENDIX),
        ("chapter_18_reference", builder.CHAPTER_18),
    ):
        entry = canonical.get(key, {})
        if entry.get("path") != relative.as_posix():
            fail(f"canonical source path={key}")
        if entry.get("sha256") != sha256_file(base / relative):
            fail(f"canonical source hash={key}")
    if canonical.get("assessment_closure_reports") != builder.closure_reports(base):
        fail("nineteen assessment closure report hashes are stale")

    course_policy = artifact.get("course_policy", {})
    expected_identity = {
        "owner": "Luka Šikić",
        "home_institution": "Hrvatsko katoličko sveučilište",
        "source_kind": "vlastita politika kolegija uz udžbenik",
        "version": "1.0",
        "as_of": "2026-08-04",
        "is_university_regulation": False,
        "external_policy_source_named": False,
    }
    for key, expected in expected_identity.items():
        if course_policy.get(key) != expected:
            fail(f"course policy identity={key}")
    if course_policy.get("lanes") != policy["lanes"]:
        fail("tool lanes disagree with D15")
    if len(course_policy.get("lanes", [])) != 3:
        fail("exactly three tool lanes are required")
    if [lane.get("id") for lane in course_policy["lanes"]] != [
        "public",
        "contractually_protected",
        "institutionally_approved_local",
    ]:
        fail("tool lane order or identity")
    if course_policy.get("standing_prohibition") != policy["standing_prohibition"]:
        fail("standing prohibition disagrees with D15")
    if course_policy.get("disclosure_statement") != policy["disclosure_statement"]:
        fail("disclosure statement disagrees with D15")

    lane_markers = {
        "public": (
            "javno objavljene podatke",
            "provjerena licencija",
            "simulirane i sintetičke podatke",
            "agregate pripremljene za nastavu",
        ),
        "contractually_protected": (
            "pisanim ugovorom",
            "isključuje uporabu unosa za treniranje modela",
            "utvrđuje rok čuvanja",
            "pseudonimizirane radne podatke",
        ),
        "institutionally_approved_local": (
            "institucijski odobreni lokalni alati",
            "bez izlaza podataka",
            "ograničene podatke",
            "uvjeta pristupa",
        ),
    }
    for lane in course_policy["lanes"]:
        folded = fold(f"{lane['title']} {lane['conditions']}")
        missing = [marker for marker in lane_markers[lane["id"]] if fold(marker) not in folded]
        if missing:
            fail(f"lane conditions={lane['id']} missing={','.join(missing)}")

    appendix_path = base / builder.APPENDIX
    appendix = appendix_path.read_text(encoding="utf-8")
    appendix_folded = fold(appendix)
    appendix_normalized = " ".join(appendix.split())
    stale_or_external = (
        "djelomični nacrt",
        "opće uredbe o zaštiti podataka",
        "gdpr",
        "sveučilište propisuje",
    )
    for phrase in stale_or_external:
        if phrase in appendix_folded:
            fail(f"stale or unsupported policy claim={phrase}")
    required_policy_phrases = (
        "Vlastita politika kolegija uz udžbenik",
        "Inačica.** 1.0",
        "Vrijedi od.** 4. kolovoza 2026.",
        "Matična ustanova kolegija.** Hrvatsko katoličko sveučilište",
        "Nije propis Hrvatskoga katoličkog sveučilišta",
        "nije opća pravna ocjena",
    )
    for phrase in required_policy_phrases:
        if phrase not in appendix_normalized:
            fail(f"dated policy block={phrase}")
    rows = policy_table_rows(appendix)
    if len(rows) != 3:
        fail(f"reader-visible lane count={len(rows)}")
    for marker in (
        "**Javni alati**",
        "**Ugovorno zaštićeni alati**",
        "**Institucijski odobreni lokalni alati**",
    ):
        if sum(marker in row for row in rows) != 1:
            fail(f"reader-visible lane={marker}")
    source_lane_markers = (
        "samo javno objavljeni podaci",
        "provjerena licencija dopušta takvu uporabu",
        "simulirani i sintetički podaci",
        "nastavni agregati",
        "pseudonimizirani radni podaci",
        "pisani sporazum koji izričito isključuje uporabu unosa za treniranje modela",
        "utvrđuje rok čuvanja",
        "nema izlaza podataka iz toga okruženja",
        "vlastitih uvjeta pristupa",
    )
    for marker in source_lane_markers:
        if marker not in appendix:
            fail(f"reader-visible lane condition={marker}")
    if policy["disclosure_statement"] not in builder.markdown_flat(appendix):
        fail("reader-visible disclosure statement is not the D15 text")

    protocol = artifact.get("protocol", {})
    expected_stages = [
        "question_and_target",
        "sharing_decision",
        "assumptions_and_steps",
        "independent_checks",
        "sensitivity",
        "record",
        "disclosure",
        "responsibility",
    ]
    if protocol.get("stages") != expected_stages:
        fail("protocol stage order")
    if protocol.get("model_independent") is not True:
        fail("protocol is not model-independent")
    if any(protocol.get(key) is not None for key in (
        "required_vendor", "required_model", "required_version"
    )):
        fail("protocol requires a vendor, model, or version")
    if protocol.get("worked_use_present") is not True:
        fail("worked protocol use is missing")
    if protocol.get("disclosure_text_present") is not True:
        fail("protocol disclosure is missing")
    for number, title in enumerate((
        "Pitanje i cilj",
        "Odluka o dijeljenju",
        "Pretpostavke i koraci",
        "Neovisne provjere",
        "Osjetljivost",
        "Zapis",
        "Objava uporabe",
        "Odgovornost",
    ), start=1):
        if f"**{number}. {title}.**" not in appendix:
            fail(f"copyable protocol stage={number}")
    protocol_section = appendix.split("## Protokol koji se može kopirati", 1)[1].split(
        "## Objava uporabe", 1
    )[0]
    vendor_names = (
        "ChatGPT", "OpenAI", "Codex", "Claude", "Anthropic",
        "Gemini", "Copilot", "Llama",
    )
    for vendor in vendor_names:
        if re.search(rf"\b{re.escape(vendor)}\b", protocol_section, re.IGNORECASE):
            fail(f"protocol names a required vendor or model={vendor}")
    if "Ocjenjuje se prosudba, a ne proizvodnja koda" not in appendix_normalized:
        fail("D05/H10 judgment boundary")
    if "nijedan ocijenjeni zadatak ne traži da ga napiše" not in appendix_normalized:
        fail("D05/H10 assessed code-production boundary")

    audit, store_hash, _ = builder.load_records(base)
    audit_block = artifact.get("exercise_audit", {})
    if audit_block.get("routes") != audit:
        fail("exercise audit routes are stale")
    store_source = canonical.get("assessment_solution_store", {})
    if store_source != {
        "path": builder.SOLUTION_ROOT.as_posix(),
        "sha256": store_hash,
        "records": 95,
    }:
        fail("assessment solution store state is stale")
    expected_counts = {
        "records": 95,
        "units": 19,
        "task_classes": sorted(builder.TASK_CLASSES),
        "prompt_fingerprints_verified": 95,
        "assistant_transfer_required": 0,
        "prohibited_data_required": 0,
        "safe_routes_present": 95,
        "safe_alternatives_missing": 0,
    }
    for key, expected in expected_counts.items():
        if audit_block.get(key) != expected:
            fail(f"exercise audit count={key}")
    if len({route["record_id"] for route in audit}) != 95:
        fail("exercise audit record identities")
    for route in audit_block["routes"]:
        if route.get("assistant_transfer_required") is not False:
            fail(f"exercise requires AI data transfer={route.get('record_id')}")
        if route.get("prohibited_data_required") is not False:
            fail(f"exercise requires prohibited data={route.get('record_id')}")
        if not route.get("safe_supplied_data_route"):
            fail(f"exercise lacks safe route={route.get('record_id')}")
        if route.get("safe_alternative_required") and not route.get("safe_alternative_present"):
            fail(f"exercise lacks required safe alternative={route.get('record_id')}")

    chapter18_path = base / builder.CHAPTER_18
    chapter18 = chapter18_path.read_text(encoding="utf-8")
    excerpt = builder.chapter18_policy_excerpt(chapter18)
    chapter18_source = canonical.get("chapter_18_reference", {})
    if chapter18_source.get("policy_excerpt_sha256") != hashlib.sha256(
        excerpt.encode("utf-8")
    ).hexdigest():
        fail("Chapter 18 policy excerpt hash is stale")
    expected_reconciliation = {
        "reference_present": True,
        "policy_version": "1.0",
        "policy_date": "2026-08-04",
        "same_three_lanes": True,
        "not_university_regulation": True,
        "chapter_source_edited_by_p5_f": False,
    }
    if artifact.get("chapter_18_reconciliation") != expected_reconciliation:
        fail("Chapter 18 reconciliation boundary")
    for phrase in (
        "Politika kolegija, inačica 1.0 od 4. kolovoza 2026.",
        "To je datirana i oprezna politika ovoga kolegija, a ne propis Hrvatskoga",
        "sigurnu simuliranu ili agregiranu alternativu",
    ):
        if phrase not in chapter18:
            fail(f"Chapter 18 policy reconciliation={phrase}")
    if check_git_boundary:
        changed = subprocess.run(
            ["git", "diff", "--quiet", "HEAD", "--", builder.CHAPTER_18.as_posix()],
            cwd=base,
            check=False,
        ).returncode
        if changed != 0:
            fail("Chapter 18 source was edited inside P5-F")

    links = re.findall(r"\]\((\.\./[^)#]+\.qmd)#([^)]+)\)", appendix)
    if len(links) < 2:
        fail(f"cross-reference count={len(links)}")
    for relative, anchor in links:
        target = (appendix_path.parent / relative).resolve()
        if not target.is_file():
            fail(f"cross-reference target={relative}")
        if not anchor_exists(target, anchor):
            fail(f"cross-reference anchor={relative}#{anchor}")
    if "content-visible" in appendix or "when-format" in appendix:
        fail("Appendix F print source is profile-gated")
    if "{#tbl-trake-alata}" not in appendix or "{#tbl-primjer-ai-protokola}" not in appendix:
        fail("print table anchors are missing")

    expected_promise = {
        "exactly_three_policy_lanes": True,
        "model_independent_protocol": True,
        "all_exercises_audited": True,
        "no_required_prohibited_upload": True,
        "every_exercise_has_safe_route": True,
        "judgment_not_code_production_is_assessed": True,
    }
    if artifact.get("public_promise") != expected_promise:
        fail("public promise")
    return {
        "lanes": len(course_policy["lanes"]),
        "exercises": len(audit),
        "units": len({entry["unit_id"] for entry in audit}),
        "xrefs": len(links),
        "closure_reports": len(builder.closure_reports(base)),
        "store_hash": store_hash,
    }


def copy_into(stage: Path, relative: Path) -> None:
    destination = stage / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / relative, destination)


def clean_regeneration(expected: dict[str, int | str]) -> None:
    builder = BUILDER_MODULE
    declared = (
        BUILDER,
        builder.POLICY_REPORT,
        builder.ASSESSMENT_REPORT,
        builder.STRUCTURE,
        builder.STYLE,
        builder.CONVENTIONS,
        builder.SOLUTION_SCHEMA,
        builder.APPENDIX,
        builder.CHAPTER_18,
    )
    with tempfile.TemporaryDirectory(prefix="appendix-f-clean-") as directory:
        stage = Path(directory)
        for relative in declared:
            copy_into(stage, relative)
        for path in sorted((ROOT / builder.SOLUTION_ROOT).glob("unit-*/*.json")):
            copy_into(stage, path.relative_to(ROOT))
        source_paths = {
            Path(json.loads(path.read_text(encoding="utf-8"))["source_anchor"]["path"])
            for path in sorted((ROOT / builder.SOLUTION_ROOT).glob("unit-*/*.json"))
        }
        for relative in sorted(source_paths):
            copy_into(stage, relative)
        for record in builder.closure_reports(ROOT):
            copy_into(stage, Path(record["path"]))
        result = subprocess.run(
            [sys.executable, str(stage / BUILDER), "--root", str(stage)],
            cwd=stage,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode:
            fail(f"clean generator failed={result.stdout.strip()}")
        isolated = validate(stage)
        if isolated != expected:
            fail("isolated clean regeneration disagrees")
        if (stage / ARTIFACT).read_bytes() != (ROOT / ARTIFACT).read_bytes():
            fail("clean regeneration is not byte-identical")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-clean", action="store_true")
    args = parser.parse_args()
    fixture = os.environ.get("APPENDIX_F_NEGATIVE_FIXTURE", "")
    try:
        result = validate(ROOT, fixture=fixture, check_git_boundary=not fixture)
        if not args.skip_clean and not fixture:
            clean_regeneration(result)
        print(
            "APPENDIX_F_CHECK_OK "
            f"lanes={result['lanes']} exercises={result['exercises']} "
            f"units={result['units']} closure_reports={result['closure_reports']} "
            "prohibited_required=0 safe_routes=95/95 disclosure=verified "
            f"protocol=8/8 xrefs={result['xrefs']} clean_pathway=verified "
            "print_source=present chapter18_edited=false"
        )
        return 0
    except (AssertionError, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"APPENDIX_F_CHECK_FAILED {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
