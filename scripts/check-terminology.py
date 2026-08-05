#!/usr/bin/env python3
"""Validate the ratified terminology registry against its G-A2c decision.

The registry lives in bookwright_plugin/bookwright/shared/conventions.json under
`terminology_registry`. It deliberately does not restate the 166 canonical forms
the nineteen ratified chapter spines already carry, so this check reads the spine
registry as the source of those forms and validates that the terminology registry
adds to them without duplicating or contradicting them.

Run:
    python scripts/check-terminology.py
"""

from __future__ import annotations

import copy
import importlib.util
import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONVENTIONS_PATH = ROOT / "bookwright_plugin/bookwright/shared/conventions.json"
CONVENTIONS_SCHEMA_PATH = ROOT / "bookwright_plugin/bookwright/shared/schemas/conventions.schema.json"
SPINE_PATH = ROOT / "bookwright_plugin/bookwright/shared/chapter-spine.json"
LEDGER_PATH = ROOT / "bookwright_plugin/bookwright/shared/concept-ledger.json"
ARCHITECTURE_HELPER_PATH = ROOT / "scripts/check-book-architecture.py"
CONCEPT_HELPER_PATH = ROOT / "scripts/check-concepts.py"

FIXTURES = (
    "duplicate_canonical_form",
    "superseded_form_made_canonical",
    "independent_review_claimed",
)


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Could not load {path.relative_to(ROOT)}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise AssertionError(f"Missing terminology input: {path.relative_to(ROOT)}") from None
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from None


def fold(value: str) -> str:
    return " ".join(value.casefold().split())


def strip_diacritics(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value.casefold())
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def main() -> int:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    try:
        helper = load_module(ARCHITECTURE_HELPER_PATH, "book_architecture_check")
        concepts = load_module(CONCEPT_HELPER_PATH, "concept_check")
        conventions = load_json(CONVENTIONS_PATH)
        schema = load_json(CONVENTIONS_SCHEMA_PATH)
        spines = load_json(SPINE_PATH)
        ledger = load_json(LEDGER_PATH)
        definitions = concepts.extract_definitions(ROOT)
    except (AssertionError, ValueError) as exc:
        print(f"Terminology: FAILED\n- {exc}")
        return 1

    conventions = copy.deepcopy(conventions)
    registry = conventions.get("terminology_registry")
    if not isinstance(registry, dict):
        print("Terminology: FAILED\n- conventions.json carries no terminology_registry.")
        return 1

    fixture = os.environ.get("TERMINOLOGY_NEGATIVE_FIXTURE", "")
    if fixture == "duplicate_canonical_form":
        # One canonical Croatian form recorded twice. The registry must never
        # carry two entries for the same form, however their English differs.
        first = copy.deepcopy(registry["canonical_forms"][0])
        first["en"] = first["en"] + " (duplicate)"
        registry["canonical_forms"].append(first)
    elif fixture == "superseded_form_made_canonical":
        # A form the gate retired is promoted back into the canonical register.
        retired = registry["superseded_forms"][0]["form"]
        registry["canonical_forms"].append({
            "hr": retired,
            "en": "reintroduced",
            "source": "gate",
            "reason": "deliberate fixture defect",
        })
    elif fixture == "independent_review_claimed":
        # The withdrawn independent review is claimed again.
        registry["review_route"]["independent_review_claim_permitted"] = True
    elif fixture:
        errors.append(f"Unknown terminology negative fixture: {fixture}")

    errors.extend(helper.validate_schema(conventions, schema, schema))

    # --- spine confirmation -------------------------------------------------
    chapters = spines.get("chapters", [])
    ratified = [c for c in chapters if c.get("ratified") is True]
    slots: list[str] = []
    units_of_form: dict[str, list[str]] = {}
    for chapter in ratified:
        for term in chapter.get("key_terms", []):
            slots.append(term)
            units_of_form.setdefault(fold(term), []).append(chapter.get("id", "<missing>"))
    distinct = set(units_of_form)
    two_unit_forms = sorted(form for form, units in units_of_form.items() if len(units) > 1)

    confirmation = registry.get("spine_confirmation", {})
    check(confirmation.get("ratified_units") == len(ratified),
          f"spine_confirmation.ratified_units must equal the live {len(ratified)} ratified spines.")
    check(confirmation.get("key_term_slots") == len(slots),
          f"spine_confirmation.key_term_slots must equal the live {len(slots)} key-term slots.")
    check(confirmation.get("distinct_forms") == len(distinct),
          f"spine_confirmation.distinct_forms must equal the live {len(distinct)} distinct forms.")
    declared_two_unit = sorted(fold(form) for form in confirmation.get("forms_carried_by_two_units", []))
    check(declared_two_unit == two_unit_forms,
          "spine_confirmation.forms_carried_by_two_units must equal the forms two ratified spines share.")
    check(Path(ROOT / confirmation.get("spine_registry", "")).exists(),
          "spine_confirmation.spine_registry must point at an existing registry file.")

    # --- canonical forms ----------------------------------------------------
    canonical = registry.get("canonical_forms", [])
    canonical_forms = [entry.get("hr", "") for entry in canonical]
    folded_canonical = [fold(form) for form in canonical_forms]
    duplicates = sorted({form for form in folded_canonical if folded_canonical.count(form) > 1})
    check(not duplicates,
          f"canonical_forms repeats a Croatian form: {duplicates}")
    restated = sorted(set(folded_canonical) & distinct)
    check(not restated,
          "canonical_forms must not restate a form the ratified spines already carry: "
          f"{restated}")
    for entry in canonical:
        unit = entry.get("unit")
        if unit is not None:
            check(unit in [c.get("id") for c in chapters],
                  f"canonical form {entry.get('hr')!r} names an unknown unit: {unit}")

    known_forms = set(folded_canonical) | distinct

    # --- superseded forms ---------------------------------------------------
    superseded = registry.get("superseded_forms", [])
    for entry in superseded:
        form = fold(entry.get("form", ""))
        target = fold(entry.get("canonical", ""))
        check(form not in known_forms,
              f"superseded form {entry.get('form')!r} is also recorded as canonical.")
        check(target in known_forms,
              f"superseded form {entry.get('form')!r} points at an unknown canonical form: "
              f"{entry.get('canonical')!r}")
    superseded_forms = {fold(entry.get("form", "")) for entry in superseded}

    # --- deliberate departures and meaning rules ---------------------------
    for entry in registry.get("deliberate_departures", []):
        check(fold(entry.get("form", "")) in known_forms,
              f"deliberate departure {entry.get('form')!r} is not a canonical form.")
    for rule in registry.get("meaning_rules", []):
        check(fold(rule.get("term", "")) in known_forms,
              f"meaning rule {rule.get('term')!r} is not a canonical form.")

    # --- review route -------------------------------------------------------
    route = registry.get("review_route", {})
    check(route.get("independent_review_obtained") is False,
          "review_route must record that no independent terminology review was obtained.")
    check(route.get("independent_review_claim_permitted") is False,
          "review_route must forbid any independent-review claim; the reviewer is withdrawn.")
    check(registry.get("authority_boundary", {}).get("independent_review_claim_authorised") is False,
          "authority_boundary must not authorise an independent-review claim.")

    # --- stable identifiers -------------------------------------------------
    live_ids = {entry["id"]: entry["term"] for entry in definitions}
    for entry in registry.get("stable_identifiers", []):
        identifier = entry.get("id", "")
        check(identifier in live_ids,
              f"stable identifier {identifier!r} has no live #def- block.")
        if identifier in live_ids:
            check(fold(live_ids[identifier]) == fold(entry.get("canonical_term", "")),
                  f"stable identifier {identifier!r} declares {entry.get('canonical_term')!r} "
                  f"but the live block is bolded {live_ids[identifier]!r}.")
            slug = re.sub(r"[^a-z0-9]+", "-", strip_diacritics(live_ids[identifier])).strip("-")
            check(slug != identifier,
                  f"stable identifier {identifier!r} already matches its term and needs no exception.")

    # --- definition map -----------------------------------------------------
    mapping = registry.get("definition_map", {})
    baseline = mapping.get("frozen_baseline")
    total = mapping.get("approved_total")
    deltas = mapping.get("deltas", [])
    if isinstance(baseline, int) and isinstance(total, int):
        summed = baseline + sum(entry.get("delta", 0) for entry in deltas)
        check(summed == total,
              f"definition_map deltas sum to {summed} but approved_total is {total}.")
    check(mapping.get("live_count") == len(definitions),
          f"definition_map.live_count must equal the live {len(definitions)} #def- blocks.")
    check(mapping.get("implemented") is False or mapping.get("live_count") == total,
          "definition_map may be marked implemented only when the live count reaches the approved total.")

    # --- concept ledger agreement ------------------------------------------
    ledger_terms = {fold(entry["term"]) for entry in ledger.get("concepts", [])}
    live_terms = {fold(entry["term"]) for entry in definitions}
    check(ledger_terms == live_terms,
          "the concept ledger and the live #def- blocks must carry the same canonical terms.")
    for entry in superseded:
        form = fold(entry.get("form", ""))
        check(form not in ledger_terms,
              f"the concept ledger still carries the superseded form {entry.get('form')!r}.")

    # --- live divergences ---------------------------------------------------
    divergences = registry.get("live_divergences", [])
    for entry in divergences:
        target = ROOT / entry.get("file", "")
        if not target.exists():
            errors.append(f"live divergence names a missing file: {entry.get('file')}")
            continue
        text = target.read_text(encoding="utf-8").casefold()
        check(entry.get("live_form", "").casefold() in text,
              f"live divergence {entry.get('live_form')!r} no longer occurs in {entry.get('file')}; "
              "remove the entry once its owning packet has repaired the prose.")
        check(fold(entry.get("canonical", "")) in known_forms,
              f"live divergence points at an unknown canonical form: {entry.get('canonical')!r}")
    for entry in registry.get("excluded_from_divergences", []):
        target = ROOT / entry.get("file", "")
        check(target.exists(),
              f"excluded divergence names a missing file: {entry.get('file')}")

    if errors:
        print("Terminology: FAILED")
        for message in errors:
            print(f"- {message}")
        return 1

    print(
        "TERMINOLOGY_OK "
        f"spine_forms={len(distinct)} slots={len(slots)} "
        f"gate_forms={len(canonical)} superseded={len(superseded_forms)} "
        f"departures={len(registry.get('deliberate_departures', []))} "
        f"rules={len(registry.get('meaning_rules', []))} "
        f"stable_ids={len(registry.get('stable_identifiers', []))} "
        f"live_definitions={len(definitions)} approved_total={total} "
        f"divergences={len(divergences)} independent_review_claim=false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
