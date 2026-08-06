#!/usr/bin/env python3
"""Validate the ratified P2-IDENTITY joint identity briefs without new dependencies."""

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
SPINE_PATH = ROOT / "bookwright_plugin/bookwright/shared/chapter-spine.json"
LEDGER_PATH = ROOT / "bookwright_plugin/bookwright/shared/chapter-ledger.json"
WIDGET_PATH = ROOT / "data/widgets.json"
ARCHITECTURE_HELPER_PATH = ROOT / "scripts/check-book-architecture.py"

PILLARS = ["03-kako-brojke-zavode", "12-kriza-i-obnova", "17-doba-algoritama"]
BRIEF_IDS = ["c03", "c12", "c17"]
BRIEF_GATES = ["G-A4-03", "G-A4-12", "G-A4-17"]
PROSE_PACKETS = ["WA-C03", "WC-C12", "WD-C17"]
CLAIM_DIMENSIONS = {
    "description",
    "association",
    "generalisation",
    "prediction",
    "causation",
    "decision",
}
LIFECYCLE_STAGES = {
    "question",
    "acquire",
    "validate",
    "prepare",
    "explore",
    "model",
    "evaluate",
    "communicate",
    "monitor",
}
CHAPTER_STAGES = {
    "stub",
    "draft",
    "enriched",
    "style_swept",
    "figures_done",
    "coauthor_review",
    "final",
}


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
        raise AssertionError(f"Missing identity-brief input: {path.relative_to(ROOT)}") from None
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from None


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
        spines = load_json(SPINE_PATH)
        ledger = load_json(LEDGER_PATH)
        widgets = load_json(WIDGET_PATH)
    except AssertionError as exc:
        print(f"Identity briefs: FAILED\n- {exc}")
        return 1

    errors.extend(helper.validate_schema(conventions, conventions_schema, conventions_schema))
    identity = copy.deepcopy(conventions.get("identity_briefs", {}))
    architecture = conventions.get("intellectual_architecture", {})

    fixture = os.environ.get("IDENTITY_BRIEFS_NEGATIVE_FIXTURE", "")
    if fixture == "fairness_widget_dropped":
        identity.get("joint_contract", {}).get("widget_policy", {})[
            "chapter_17_fairness_widget_retained"
        ] = False
    elif fixture == "nlp_implementation_admitted":
        module = by_id(identity.get("briefs", []), "c17").get("measurement_first_text_module", {})
        module["excludes"] = [
            value
            for value in module.get("excludes", [])
            if value != "tokenizer_or_preprocessing_implementation"
        ]
    elif fixture:
        errors.append(f"Unknown identity-brief negative fixture: {fixture}")

    check(identity.get("packet") == "P2-IDENTITY", "Identity briefs must remain tied to P2-IDENTITY.")
    check(
        identity.get("register_items") == ["R13-ARCH-measurement-first"],
        "Identity briefs must govern exactly the one P2-IDENTITY register item.",
    )
    for decision in ("D03", "D07", "D13", "G-A2a", "G-A2d"):
        check(
            decision in identity.get("governing_decisions", []),
            f"Identity briefs must name governing decision {decision}.",
        )

    joint = identity.get("joint_contract", {})
    check(joint.get("pillars") == PILLARS, "The joint contract must cover the three identity pillars in order.")
    check(
        joint.get("approval_tier") == "tier_F_full_identity_rewrite"
        and joint.get("one_argument_per_pillar") is True
        and joint.get("pillar_is_not_a_list_of_topics") is True
        and joint.get("assembled_from_isolated_insertions") is False,
        "Each pillar must be one Tier F argument rather than an assembled list.",
    )
    check(
        joint.get("evidence_precondition", {}).get("handoff") == "H-P0-REGISTER-007"
        and sorted(joint.get("evidence_precondition", {}).get("gates", [])) == sorted(BRIEF_GATES),
        "Pillar prose must wait for its governed evidence package and its approved brief gate.",
    )
    widget_policy = joint.get("widget_policy", {})
    check(
        widget_policy.get("new_central_widget") is False
        and widget_policy.get("chapter_17_fairness_widget_retained") is True
        and widget_policy.get("chapter_17_worked_example") == "text_analysis_under_D07"
        and widget_policy.get("widget_may_not_carry_the_explanatory_burden_alone") is True,
        "D07 requires the retained Chapter 17 fairness widget, text analysis as worked example, and no new central widget.",
    )
    check(
        "no_assessed_code_production_in_any_pillar" in joint.get("shared_prohibitions", []),
        "The joint contract must forbid assessed code production in every pillar.",
    )
    check(
        "no_invented_case_number_effect_size_study_or_citation" in joint.get("shared_prohibitions", []),
        "The joint contract must forbid invented cases, numbers, studies, and citations.",
    )

    records = identity.get("briefs", [])
    check([record.get("id") for record in records] == BRIEF_IDS, "Briefs must appear as c03, c12, c17 in order.")
    check([record.get("chapter") for record in records] == PILLARS, "Briefs must map to the three pillar chapters in order.")
    check([record.get("brief_gate") for record in records] == BRIEF_GATES, "Each brief must name its exact later author gate.")
    check([record.get("prose_packet") for record in records] == PROSE_PACKETS, "Each brief must name its exact prose packet.")

    for record in records:
        rid = record.get("id", "<missing>")
        for stage in ("plant", "develop", "harvest"):
            placement = record.get(stage, {})
            check(
                bool(placement.get("locations")) and bool(placement.get("role")),
                f"Brief {rid} lacks an explicit {stage} role.",
            )
        check(bool(record.get("exclusions")), f"Brief {rid} lacks exclusions.")
        check(
            len(record.get("argument_spine", [])) >= 5,
            f"Brief {rid} must carry one developed argument spine.",
        )
        supported = set(record.get("claim_dimensions_supported", []))
        check(
            supported and supported.issubset(CLAIM_DIMENSIONS),
            f"Brief {rid} names a claim dimension outside the ratified six.",
        )
        check(
            bool(record.get("claim_dimensions_unavailable")),
            f"Brief {rid} must state at least one unavailable claim dimension.",
        )
        check(
            supported.isdisjoint(set(record.get("claim_dimensions_unavailable", []))),
            f"Brief {rid} lists the same claim dimension as supported and unavailable.",
        )
        stages = set(record.get("lifecycle_stage_emphasis", []))
        check(
            stages and stages.issubset(LIFECYCLE_STAGES),
            f"Brief {rid} names a lifecycle stage outside the ratified nine.",
        )
        check(
            any("no_assessed_code_production" in value for value in record.get("exclusions", [])),
            f"Brief {rid} must exclude assessed code production.",
        )

    c03 = by_id(records, "c03")
    check(
        "no_ASA_episode_as_the_chapter_case" in c03.get("exclusions", []),
        "Chapter 3 must not use the ASA episode as its case; it belongs to Chapter 10.",
    )
    check(
        "no_visible_code_in_part_i" in c03.get("exclusions", []),
        "Chapter 3 must hold the D05 Part I no-visible-code boundary.",
    )
    check(
        any("dug prema poglavljima 8 i 9" in value for value in c03.get("required_components", [])),
        "Chapter 3 must record its explicit margin-of-error debt to Chapters 8 and 9.",
    )

    c12 = by_id(records, "c12")
    check(
        "no_invented_study_result_effect_size_or_forest_plot_input" in c12.get("exclusions", []),
        "Chapter 12 must forbid invented study results and forest-plot inputs.",
    )
    check(
        "no_significance_only_sensitivity_comparison" in c12.get("exclusions", []),
        "Chapter 12 sensitivity comparison may not reduce to significance and nonsignificance.",
    )

    c17 = by_id(records, "c17")
    module = c17.get("measurement_first_text_module", {})
    check(
        module.get("register_item") == "R13-ARCH-measurement-first"
        and module.get("home") == "17-doba-algoritama",
        "Chapter 17 must be the ratified home of the measurement-first text module.",
    )
    check(
        module.get("covers")
        == [
            "text_unit_and_corpus_boundary",
            "coding_frame_and_label_production",
            "human_dictionary_and_ai_labels_as_competing_measurements",
            "held_out_evaluation_and_thresholds",
            "fairness_error_burdens_and_base_rates",
            "language_models_as_predictive_generation",
            "institutions_notice_contestability_appeal_monitoring_and_feedback",
        ],
        "The text module must connect units, labels, evaluation, fairness, language models, and institutions in stable order.",
    )
    check(
        "tokenizer_or_preprocessing_implementation" in module.get("excludes", [])
        and "nlp_programming_course" in module.get("excludes", [])
        and "machine_learning_mathematics" in module.get("excludes", []),
        "The text module must exclude NLP implementation and machine-learning mathematics.",
    )
    check(
        "no_second_central_widget_and_no_removal_of_the_fairness_widget" in c17.get("exclusions", []),
        "Chapter 17 must retain exactly its existing fairness widget.",
    )
    check(
        "chapter_17_prerequisite_metadata_remains_unresolved_until_P2-SPINE-V" in c17.get("exclusions", []),
        "Chapter 17 prerequisites remain a P2-SPINE-V decision, not a P2-IDENTITY one.",
    )

    authority = identity.get("authority_boundary", {})
    check(
        authority and all(value is False for value in authority.values()),
        "Every P2-IDENTITY excluded authority must remain false.",
    )
    check(
        authority.get("chapter_prose_edit_authorised") is False
        and authority.get("chapter_spine_ratification_authorised") is False
        and authority.get("data_package_selection_or_promotion_authorised") is False,
        "P2-IDENTITY may not edit prose, ratify a spine, or select a data package.",
    )

    deferred_gates = {record.get("gate") for record in identity.get("deferred_to_later_gates", [])}
    for gate in BRIEF_GATES + ["G-A3-TEXT", "P2-SPINE-V", "P3-EVIDENCE12"]:
        check(gate in deferred_gates, f"Identity briefs must defer their open selection to {gate}.")

    check(
        architecture.get("decision") == "G-A2a",
        "The accepted G-A2a architecture must remain the governing claim and thread system.",
    )
    chapter_spines = spines.get("chapters", [])
    ratified_spines = [chapter for chapter in chapter_spines if chapter.get("ratified") is True]
    check(len(chapter_spines) == 19, "The chapter-spine registry must contain exactly 19 units.")
    check(
        authority.get("chapter_spine_ratification_authorised") is False
        and all(chapter.get("decision", "").startswith("G-A2b-") for chapter in ratified_spines),
        "The identity briefs may not ratify a chapter spine; every ratified spine names its own G-A2b gate.",
    )
    check(
        not any(chapter.get("id") in PILLARS and chapter.get("ratified") is True for chapter in chapter_spines)
        or all(
            chapter.get("decision") in ("G-A2b-I", "G-A2b-IV", "G-A2b-V")
            for chapter in chapter_spines
            if chapter.get("id") in PILLARS and chapter.get("ratified") is True
        ),
        "A ratified pillar spine must come from its own part gate, not from the identity briefs.",
    )
    ledger_units = ledger.get("chapters", [])
    ledger_ids = [unit.get("id") for unit in ledger_units]
    check(
        sorted(ledger_ids) == sorted(chapter.get("id") for chapter in chapter_spines),
        "The identity check requires the chapter ledger and spine registry to cover the same 19 units.",
    )
    check(
        all(unit.get("stage") in CHAPTER_STAGES for unit in ledger_units),
        "The chapter ledger contains a stage outside its canonical lifecycle.",
    )
    fairness_widgets = [
        widget
        for widget in widgets.get("widgets", [])
        if widget.get("poglavlje") == "chapters/17-doba-algoritama.qmd"
    ]
    check(
        len(fairness_widgets) == 1,
        "Chapter 17 must retain exactly one registered central widget.",
    )

    if errors:
        print("Identity briefs: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    digest = hashlib.sha256(
        json.dumps(identity, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    print("IDENTITY_BRIEFS_OK")
    print(f"- state: identity:sha256-{digest}")
    print("- governed items: 1; pillar briefs: 3")
    print("- plant/develop/harvest roles: 9; brief exclusion rules: "
          f"{sum(len(record.get('exclusions', [])) for record in records)}")
    print("- Chapter 17 central widgets registered: 1 (fairness, retained)")
    print("- measurement-first text module: 7 covered topics, implementation excluded")
    print("- assessed code production: excluded in every pillar")
    stage_counts = {
        stage: sum(1 for unit in ledger_units if unit.get("stage") == stage)
        for stage in sorted({unit.get("stage") for unit in ledger_units})
    }
    stage_summary = "; ".join(f"{count} {stage}" for stage, count in stage_counts.items())
    print(f"- chapter spines ratified: {len(ratified_spines)} of {len(chapter_spines)}; "
          f"chapter stages: {stage_summary}; acceptance authority checked by check-chapter-spines.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
