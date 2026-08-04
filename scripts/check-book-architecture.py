#!/usr/bin/env python3
"""Validate the ratified G-A2a architecture without undeclared dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "bookwright_plugin/bookwright/shared/conventions.json"
SCHEMA_PATH = ROOT / "bookwright_plugin/bookwright/shared/schemas/conventions.schema.json"
SPINE_PATH = ROOT / "bookwright_plugin/bookwright/shared/chapter-spine.json"


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise AssertionError(f"Missing architecture input: {path.relative_to(ROOT)}") from None
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from None


def resolve_ref(schema_root: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise AssertionError(f"Unsupported non-local schema reference: {ref}")
    node: Any = schema_root
    for raw_part in ref[2:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        node = node[part]
    if not isinstance(node, dict):
        raise AssertionError(f"Schema reference does not resolve to an object: {ref}")
    return node


def value_type_matches(value: Any, expected: str) -> bool:
    checks = {
        "object": lambda candidate: isinstance(candidate, dict),
        "array": lambda candidate: isinstance(candidate, list),
        "string": lambda candidate: isinstance(candidate, str),
        "boolean": lambda candidate: isinstance(candidate, bool),
        "integer": lambda candidate: isinstance(candidate, int) and not isinstance(candidate, bool),
        "number": lambda candidate: isinstance(candidate, (int, float)) and not isinstance(candidate, bool),
        "null": lambda candidate: candidate is None,
    }
    if expected not in checks:
        raise AssertionError(f"Unsupported schema type in local validator: {expected}")
    return checks[expected](value)


def validate_schema(
    value: Any,
    schema: dict[str, Any],
    schema_root: dict[str, Any],
    location: str = "$",
) -> list[str]:
    """Validate the JSON-Schema subset used by conventions.schema.json."""
    if "$ref" in schema:
        return validate_schema(value, resolve_ref(schema_root, schema["$ref"]), schema_root, location)

    errors: list[str] = []
    if "const" in schema and value != schema["const"]:
        errors.append(f"{location}: expected constant {schema['const']!r}, found {value!r}")

    expected_type = schema.get("type")
    if expected_type is not None and not value_type_matches(value, expected_type):
        return errors + [f"{location}: expected {expected_type}, found {type(value).__name__}"]

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{location}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{location}: unexpected property {key!r}")
        for key, child_schema in properties.items():
            if key in value:
                errors.extend(validate_schema(value[key], child_schema, schema_root, f"{location}.{key}"))

    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{location}: fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{location}: more than {schema['maxItems']} items")
        if schema.get("uniqueItems"):
            rendered = [json.dumps(item, ensure_ascii=False, sort_keys=True) for item in value]
            if len(rendered) != len(set(rendered)):
                errors.append(f"{location}: array items are not unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                errors.extend(validate_schema(item, item_schema, schema_root, f"{location}[{index}]"))

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{location}: string is shorter than {schema['minLength']}")
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            errors.append(f"{location}: string does not match {schema['pattern']!r}")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{location}: value is below {schema['minimum']}")

    return errors


def ids(records: list[dict[str, Any]]) -> list[str]:
    return [record["id"] for record in records]


def main() -> int:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    try:
        conventions = load_json(REGISTRY_PATH)
        schema = load_json(SCHEMA_PATH)
        spines = load_json(SPINE_PATH)
    except AssertionError as exc:
        print(f"Book architecture: FAILED\n- {exc}")
        return 1

    errors.extend(validate_schema(conventions, schema, schema))
    architecture = conventions.get("intellectual_architecture", {})

    expected_items = [
        "R08-DESIGN-policy",
        "R08-DESIGN-simulation-empirical",
        "R08-DESIGN-simulation",
        "R08-DESIGN-survey",
        "R08-DESIGN-administrative",
        "R08-DESIGN-official",
        "R08-DESIGN-expert",
        "R08-DESIGN-digital",
        "R08-DESIGN-volunteer",
        "R08-DESIGN-restricted",
        "R08-PORTFOLIO-text-priority",
        "R10-DS-workflow-scope",
        "R10-LIFECYCLE-stable",
        "R10-CLAIMS-six-dimensions",
        "R10-AUDIT-six-questions",
        "R10-THREAD-seven-map",
        "R12-POLL-card",
        "R17-REPORT-honest-standard",
        "R19-SENSITIVITY-standard",
        "R24-BOOK-four-activities",
        "R24-BOOK-ordinary-ethics",
        "R24-EVIDENCE-four-objects",
    ]
    check(
        architecture.get("register_items") == expected_items,
        "Architecture must govern exactly the 22 accepted G-A2a items in stable order.",
    )

    claims = architecture.get("claim_registry", {})
    check(
        ids(claims.get("dimensions", []))
        == ["description", "association", "generalisation", "prediction", "causation", "decision"],
        "Claim registry must contain the six ratified dimensions in order.",
    )
    check(
        claims.get("population_reach_is_independent_of_claim_type") is True,
        "Population reach must remain independent of claim type.",
    )
    check(
        ids(claims.get("audit_questions", []))
        == [
            "observation_unit",
            "absence_and_selection",
            "target_and_claim",
            "uncertainty_inside_and_outside",
            "reasonable_alternative",
            "error_consequences",
        ],
        "Audit registry must contain the six ratified questions in order.",
    )

    lifecycle = architecture.get("lifecycle_registry", {})
    check(
        lifecycle.get("stages")
        == ["question", "acquire", "validate", "prepare", "explore", "model", "evaluate", "communicate", "monitor"],
        "Lifecycle registry must contain the stable nine-stage sequence.",
    )
    check(
        ids(lifecycle.get("part_roles", []))
        == ["part_i", "part_ii", "part_iii", "part_iv", "part_v", "finale"],
        "Lifecycle must record the six ratified part/finale roles.",
    )

    threads = architecture.get("thread_registry", {}).get("threads", [])
    check(
        ids(threads)
        == [
            "unit_of_analysis",
            "selection_and_absence",
            "denominator",
            "uncertainty_budget",
            "consequences_of_error",
            "reproducibility_and_provenance",
            "communication_of_a_claim",
        ],
        "Thread registry must contain the seven ratified threads in order.",
    )
    for thread in threads:
        for stage in ("plant", "develop", "harvest"):
            placement = thread.get(stage, {})
            check(
                bool(placement.get("locations")) and bool(placement.get("role")),
                f"Thread {thread.get('id', '<missing>')} lacks an explicit {stage} role.",
            )
        check(
            bool(thread.get("exclusions")),
            f"Thread {thread.get('id', '<missing>')} lacks explicit exclusions.",
        )
    scope_control = architecture.get("thread_registry", {}).get("scope_control", {})
    check(
        scope_control.get("pattern") == "short_seed_one_substantial_harvest_later_retrieval"
        and scope_control.get("later_occurrences_are_retrieval_not_repeated_mini_lectures") is True,
        "Thread scope control must preserve seed, one substantial harvest, and later retrieval.",
    )
    check(
        all(
            scope_control.get(key) is False
            for key in ("new_numbered_chapter", "new_central_widget", "new_callout_type")
        ),
        "Thread architecture may not add a chapter, central widget, or callout type.",
    )

    data_science = architecture.get("data_science_registry", {})
    check(
        ids(data_science.get("activities", []))
        == ["statistics", "data_science", "machine_learning", "ai_system"],
        "The four activities must remain distinct and ordered.",
    )
    budget = data_science.get("attention_budget", {})
    check(
        [
            budget.get("statistical_reasoning_percent"),
            budget.get("lifecycle_and_reproducibility_percent"),
            budget.get("ai_and_algorithmic_systems_percent"),
        ]
        == [70, 20, 10],
        "The diagnostic attention budget must remain 70/20/10.",
    )
    check(
        budget.get("approximate") is True
        and all(
            budget.get(key) is False
            for key in ("binding", "page_count_formula", "quota", "may_require_or_refuse_content")
        ),
        "Every representation of 70/20/10 must remain explicitly non-binding.",
    )
    check(data_science.get("fifth_promise") is False, "Data science must remain a delivery mechanism, not a fifth promise.")

    design_policy = data_science.get("data_design_policy", {})
    check(
        ids(design_policy.get("designs", []))
        == [
            "seeded_simulation_known_population",
            "probability_survey_with_weights",
            "administrative_or_electoral_count",
            "official_aggregate_statistics",
            "expert_coded_latent_index",
            "digital_trace_or_selected_corpus",
            "volunteer_open_survey",
            "restricted_commercial_or_administrative_source",
        ],
        "Data-design registry must contain the eight ratified designs in order.",
    )
    check(
        design_policy.get("organising_principle") == "data_generating_design_not_discipline_or_dataset_count"
        and design_policy.get("package_selection_and_promotion_remain_exact_later_gates") is True,
        "Data-design architecture must not select or promote a package.",
    )
    priority = design_policy.get("priority_rule", {})
    check(
        priority.get("first") == "ParlaMint-HR_ParlaSent_text_package"
        and "optional_World_Bank_WDI" in priority.get("before", []),
        "The text package must retain priority over the optional World Bank extension.",
    )

    evidence_objects = architecture.get("ethics_registry", {}).get("evidence_objects", [])
    check(
        ids(evidence_objects)
        == [
            "known_mechanism_simulation",
            "synthetic_data",
            "model_generated_hypothetical_answers",
            "fabricated_empirical_observations",
        ],
        "Evidence registry must contain the four ratified objects in order.",
    )
    for evidence_object in evidence_objects:
        check(
            bool(evidence_object.get("permissible_use")) and bool(evidence_object.get("prohibited_claim")),
            f"Evidence object {evidence_object.get('id', '<missing>')} lacks a permissible use or prohibited claim.",
        )

    sensitivity = claims.get("sensitivity_standard", {})
    check(
        sensitivity.get("required_structure") == "primary_analysis_plus_one_defensible_alternative"
        and sensitivity.get("significance_only_comparison_forbidden") is True,
        "Sensitivity standard must compare a primary analysis with one defensible alternative.",
    )
    check(
        claims.get("poll_reading_card", {}).get("sampling_and_nonsampling_error_must_remain_distinct") is True,
        "Poll card must keep sampling and nonsampling errors distinct.",
    )

    authority = architecture.get("authority_boundary", {})
    check(
        len(authority) == 9 and all(value is False for value in authority.values()),
        "P2-CLAIMS authority boundary must keep all nine excluded actions false.",
    )
    chapter_spines = spines.get("chapters", [])
    check(
        len(chapter_spines) == 19 and not any(chapter.get("ratified") is True for chapter in chapter_spines),
        "P2-CLAIMS must leave all 19 chapter spines unratified.",
    )

    if errors:
        print("Book architecture: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("BOOK_ARCHITECTURE_OK")
    print("- schema: conventions.json valid against conventions.schema.json")
    print("- governed items: 22")
    print("- claim dimensions: 6; audit questions: 6")
    print("- lifecycle stages: 9; part/finale roles: 6")
    print("- threads: 7 with plant/develop/harvest roles and exclusions")
    print("- activities: 4; evidence objects: 4")
    print("- data-generating designs: 8; package selection deferred")
    print("- attention budget: 70/20/10 diagnostic and non-binding")
    print("- chapter spines ratified: 0 of 19")
    return 0


if __name__ == "__main__":
    sys.exit(main())
