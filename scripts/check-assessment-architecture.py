#!/usr/bin/env python3
"""Validate the ratified G-A2d assessment architecture without new dependencies."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONVENTIONS_PATH = ROOT / "bookwright_plugin/bookwright/shared/conventions.json"
CONVENTIONS_SCHEMA_PATH = ROOT / "bookwright_plugin/bookwright/shared/schemas/conventions.schema.json"
SOLUTION_SCHEMA_PATH = ROOT / "bookwright_plugin/bookwright/shared/schemas/solution-record.schema.json"
SPINE_PATH = ROOT / "bookwright_plugin/bookwright/shared/chapter-spine.json"
INVENTORY_PATH = ROOT / "config/book-inventory.json"
STYLE_PATH = ROOT / "STYLE.md"
EXPORT_PATH = ROOT / "R/build-ai-exports.R"
ARCHITECTURE_HELPER_PATH = ROOT / "scripts/check-book-architecture.py"


def load_architecture_helper() -> Any:
    spec = importlib.util.spec_from_file_location("book_architecture_check", ARCHITECTURE_HELPER_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError("Could not load scripts/check-book-architecture.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise AssertionError(f"Missing assessment input: {path.relative_to(ROOT)}") from None
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from None


def ids(records: list[dict[str, Any]]) -> list[str]:
    return [record.get("id", "") for record in records]


def by_id(records: list[dict[str, Any]], record_id: str) -> dict[str, Any]:
    matches = [record for record in records if record.get("id") == record_id]
    return matches[0] if len(matches) == 1 else {}


def main() -> int:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    try:
        helper = load_architecture_helper()
        conventions = load_json(CONVENTIONS_PATH)
        conventions_schema = load_json(CONVENTIONS_SCHEMA_PATH)
        solution_schema = load_json(SOLUTION_SCHEMA_PATH)
        spines = load_json(SPINE_PATH)
        inventory = load_json(INVENTORY_PATH)
        style = STYLE_PATH.read_text(encoding="utf-8")
        exporter = EXPORT_PATH.read_text(encoding="utf-8")
    except (AssertionError, OSError) as exc:
        print(f"Assessment architecture: FAILED\n- {exc}")
        return 1

    schema_errors = helper.validate_schema(conventions, conventions_schema, conventions_schema)
    errors.extend(schema_errors)
    assessment = copy.deepcopy(conventions.get("assessment_architecture", {}))

    fixture = os.environ.get("ASSESSMENT_ARCHITECTURE_NEGATIVE_FIXTURE", "")
    if fixture == "protected_export_field":
        public_export = by_id(assessment.get("visibility_contract", {}).get("layers", []), "public_ai_export")
        public_export.setdefault("included_components", []).append("full_severity_ranked_rubric")
    elif fixture == "assessed_code_production":
        ladder = assessment.get("ai_competence_registry", {}).get("stage_ladder", [])
        if ladder:
            ladder[0]["assessed_code_production"] = True
    elif fixture:
        errors.append(f"Unknown assessment negative fixture: {fixture}")

    check(
        assessment.get("register_items")
        == [
            "R15-SCHEMA-closure",
            "R24-BOOK-human-AI-competence",
            "R24-BOOK-three-roles",
        ],
        "Assessment architecture must govern exactly the three P2-ASSESS items in stable order.",
    )
    check(assessment.get("decision") == "G-A2d", "Assessment architecture must remain tied to G-A2d.")

    solution_contract = assessment.get("solution_record_contract", {})
    expected_components = [
        "planted_error",
        "revealing_diagnostic",
        "plausible_non_answers",
        "model_response_components",
        "numerical_check",
        "severity_ranked_rubric",
    ]
    check(
        solution_contract.get("canonical_components") == expected_components,
        "Canonical solution contract must expose all six machine-identifiable components in order.",
    )
    check(
        solution_contract.get("one_record_per_exercise") is True
        and solution_contract.get("no_second_answer_source") is True,
        "Every exercise must have one canonical record and no second answer source.",
    )
    check(
        solution_contract.get("records_authored_in_this_packet") is False
        and inventory.get("solution_routes") == [],
        "P2-ASSESS may define the contract but may not author records or implement solution routes.",
    )

    top_required = solution_schema.get("required", [])
    check(
        all(
            key in top_required
            for key in (
                "record_id",
                "exercise_id",
                "unit_id",
                "source_anchor",
                "prompt_fingerprint",
                "answer_components",
                "visibility_contract",
                "human_responsibility",
            )
        ),
        "Solution schema lacks a required source-binding or responsibility field.",
    )
    answer_schema = solution_schema.get("properties", {}).get("answer_components", {})
    check(
        answer_schema.get("required") == expected_components
        and list(answer_schema.get("properties", {})) == expected_components,
        "Solution schema must require exactly the six canonical answer components in stable order.",
    )
    severity_prefix = (
        solution_schema.get("$defs", {})
        .get("severityRankedRubric", {})
        .get("properties", {})
        .get("severity_order", {})
        .get("prefixItems", [])
    )
    check(
        [item.get("const") for item in severity_prefix]
        == ["fatal", "major", "minor", "useful_improvement"],
        "Solution schema must rank rubric severity from fatal to useful improvement.",
    )
    scale = assessment.get("rubric_severity_scale", [])
    check(
        ids(scale) == ["fatal", "major", "minor", "useful_improvement"]
        and [record.get("rank") for record in scale] == [1, 2, 3, 4],
        "Assessment registry must carry the same explicit four-level severity order.",
    )

    visibility = assessment.get("visibility_contract", {})
    layers = visibility.get("layers", [])
    check(
        ids(layers)
        == ["main_student_text", "self_study_check", "kolegij_rubric", "print_check", "public_ai_export"],
        "Visibility contract must contain the five declared projections in stable order.",
    )
    self_study = by_id(layers, "self_study_check")
    kolegij = by_id(layers, "kolegij_rubric")
    print_check = by_id(layers, "print_check")
    public_export = by_id(layers, "public_ai_export")
    check(
        self_study.get("route") == "deliberately_separated_solution_route"
        and "full_severity_ranked_rubric" in self_study.get("excluded_components", []),
        "Self-study checks must be separated from protected rubric detail.",
    )
    check(
        kolegij.get("access") == "protected"
        and all(
            field in kolegij.get("included_components", [])
            for field in ("full_severity_ranked_rubric", "alternatives", "instructor_notes")
        ),
        "The kolegij layer must contain the full protected rubric, alternatives, and instructor notes.",
    )
    check(
        print_check.get("route") == "separated_print_solution_route"
        and print_check.get("included_components") == self_study.get("included_components"),
        "Print and self-study checks must project the same concise components from the canonical record.",
    )
    check(
        public_export.get("included_components") == []
        and public_export.get("excluded_components") == ["all_solution_record_content"],
        "Public AI exports must contain no solution-record content.",
    )
    enforcement = visibility.get("export_enforcement", {})
    check(
        enforcement.get("solution_routes_excluded_from_public_inputs") is True
        and enforcement.get("protected_in_source_content_requires_content_visible_when_profile") is True
        and enforcement.get("labels_are_not_an_access_control") is True
        and enforcement.get("protected_content_leak_fails") is True,
        "Export protection must be structural, label-independent, and fail closed.",
    )
    check(
        "when-profile\\\\s*=" in exporter
        and "protected-content leak" in exporter
        and "unexpected_ai" in exporter,
        "The live exporter lacks one structural protection named by the visibility contract.",
    )

    competence = assessment.get("ai_competence_registry", {})
    check(
        competence.get("assessment_target") == "human_judgment_not_code_syntax"
        and competence.get("computation_is_delegable") is True
        and competence.get("human_judgment_is_not_delegated") is True,
        "AI assessment must preserve delegable computation and non-delegable human judgment.",
    )
    check(
        ids(competence.get("roles", [])) == ["instrument", "fallible_analyst", "object_of_research"],
        "AI registry must preserve the three ratified roles in order.",
    )
    appearance = competence.get("substantive_appearance_contract", {})
    check(
        appearance.get("explicit_role_required") is True
        and appearance.get("human_responsibility_statement_required") is True,
        "Every substantive AI appearance must name its role and preserve human responsibility.",
    )
    receipt = competence.get("verification_receipt", {})
    check(
        receipt.get("required_from") == "end_of_part_i_forward"
        and receipt.get("fields", [])[:4]
        == ["what_was_asked", "what_was_returned", "what_was_checked", "how_it_was_checked"]
        and receipt.get("readable_without_code") is True
        and receipt.get("syntax_receipt_is_insufficient") is True,
        "Post-Part-I verification receipts must contain the four ratified readable fields and cannot reduce to syntax.",
    )
    dimensions = competence.get("competence_dimensions", [])
    check(
        ids(dimensions) == ["task_specification", "validation", "alternatives", "provenance", "responsibility"],
        "Competence registry must contain the five judgment dimensions in order.",
    )
    for dimension in dimensions:
        for stage in ("plant", "develop", "harvest"):
            placement = dimension.get(stage, {})
            check(
                bool(placement.get("locations")) and bool(placement.get("role")),
                f"Competence {dimension.get('id', '<missing>')} lacks an explicit {stage} role.",
            )
        check(bool(dimension.get("exclusions")), f"Competence {dimension.get('id', '<missing>')} lacks exclusions.")

    ladder = competence.get("stage_ladder", [])
    check(
        ids(ladder)
        == ["part_i", "part_ii", "part_iii", "part_iv", "part_v_models", "chapter_17", "finale"],
        "AI competence ladder must contain the seven ratified stages in order.",
    )
    check(
        ladder and ladder[0].get("required_receipt") is False
        and all(stage.get("required_receipt") is True for stage in ladder[1:]),
        "A readable verification receipt must be required after Part I.",
    )
    check(
        ladder and all(stage.get("assessed_code_production") is False for stage in ladder),
        "No stage may assess code production.",
    )

    h10 = assessment.get("h10_boundary", {})
    check(
        h10.get("preface_and_part_i_visible_code") is False
        and h10.get("hidden_plumbing_permitted") is True
        and h10.get("assessed_code_production") is False,
        "H10 must preserve no visible Part I code, permit hidden plumbing, and forbid assessed code production.",
    )
    style_normalized = " ".join(style.split())
    check(
        all(
            phrase in style_normalized
            for phrase in (
                "No assessed task anywhere in the book asks for code production.",
                "one canonical record",
                "No protected solution content enters public AI exports",
                "task specification, validation, alternatives, provenance, and responsibility rather than syntax",
            )
        ),
        "STYLE.md does not state the complete ratified D05/D06 boundary.",
    )

    authority = assessment.get("authority_boundary", {})
    check(authority and all(value is False for value in authority.values()), "Every P2-ASSESS excluded authority must remain false.")
    chapter_spines = spines.get("chapters", [])
    ratified_spines = [chapter for chapter in chapter_spines if chapter.get("ratified") is True]
    check(len(chapter_spines) == 19, "The chapter-spine registry must contain exactly 19 units.")
    check(
        authority.get("chapter_spine_ratification_authorised") is False
        and all(chapter.get("decision", "").startswith("G-A2b-") for chapter in ratified_spines),
        "The assessment architecture may not ratify a chapter spine; every ratified spine names its own G-A2b gate.",
    )

    if errors:
        print("Assessment architecture: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    digest = hashlib.sha256(
        json.dumps(assessment, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    print("ASSESSMENT_ARCHITECTURE_OK")
    print(f"- state: assessment:sha256-{digest}")
    print("- governed items: 3; canonical answer components: 6")
    print("- visibility projections: 5; public AI solution fields: 0")
    print("- rubric severity levels: fatal, major, minor, useful_improvement")
    print("- AI roles: 3; competence dimensions: 5; ladder stages: 7")
    print("- assessed code production: false in every stage")
    print("- solution records authored: 0; solution routes implemented: 0")
    print(f"- chapter spines ratified: {len(ratified_spines)} of {len(chapter_spines)}, each at its own G-A2b gate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
