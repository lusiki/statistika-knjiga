#!/usr/bin/env python3
"""Validate ratified chapter spines against their G-A2b decisions without new dependencies."""

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
SPINE_PATH = ROOT / "bookwright_plugin/bookwright/shared/chapter-spine.json"
SPINE_SCHEMA_PATH = ROOT / "bookwright_plugin/bookwright/shared/schemas/chapter-spine.schema.json"
LEDGER_PATH = ROOT / "bookwright_plugin/bookwright/shared/chapter-ledger.json"
INVENTORY_PATH = ROOT / "config/book-inventory.json"
ARCHITECTURE_HELPER_PATH = ROOT / "scripts/check-book-architecture.py"

UNIT_ORDER = [
    "00-predgovor",
    "01-zasto-statistika",
    "02-mjerenje-i-dizajn",
    "03-kako-brojke-zavode",
    "04-sazimanje-podataka",
    "05-vizualizacija",
    "06-povezanost",
    "07-vjerojatnost",
    "08-uzorkovanje",
    "09-procjena",
    "10-logika-testiranja",
    "11-velicina-ucinka-i-snaga",
    "12-kriza-i-obnova",
    "13-kategoricki-podaci",
    "14-dvije-grupe",
    "15-vise-grupa",
    "16-regresija",
    "17-doba-algoritama",
    "18-vase-prvo-istrazivanje",
]

# Which G-A2b gate owns each unit's spine. A ratified spine may name no other gate.
GATE_OF_UNIT = {
    "00-predgovor": "G-A2b-PREFACE",
    "01-zasto-statistika": "G-A2b-I",
    "02-mjerenje-i-dizajn": "G-A2b-I",
    "03-kako-brojke-zavode": "G-A2b-I",
    "04-sazimanje-podataka": "G-A2b-II",
    "05-vizualizacija": "G-A2b-II",
    "06-povezanost": "G-A2b-II",
    "07-vjerojatnost": "G-A2b-III",
    "08-uzorkovanje": "G-A2b-III",
    "09-procjena": "G-A2b-III",
    "10-logika-testiranja": "G-A2b-IV",
    "11-velicina-ucinka-i-snaga": "G-A2b-IV",
    "12-kriza-i-obnova": "G-A2b-IV",
    "13-kategoricki-podaci": "G-A2b-V",
    "14-dvije-grupe": "G-A2b-V",
    "15-vise-grupa": "G-A2b-V",
    "16-regresija": "G-A2b-V",
    "17-doba-algoritama": "G-A2b-V",
    "18-vase-prvo-istrazivanje": "G-A2b-FINALE",
}

# Ratified obligations that a spine must state, keyed by unit.
REQUIRED_EXCLUSION_MARKERS = {
    "00-predgovor": [
        "vidljivi blok koda",
        "vidljivoga koda u predgovoru i Dijelu I",
        "Dodatku B",
        "#def-",
    ],
    "01-zasto-statistika": ["vidljivi blok koda"],
    "02-mjerenje-i-dizajn": ["vidljivi blok koda"],
    "03-kako-brojke-zavode": ["vidljivi blok koda"],
}

NO_VISIBLE_CODE_UNITS = [
    "00-predgovor",
    "01-zasto-statistika",
    "02-mjerenje-i-dizajn",
    "03-kako-brojke-zavode",
]


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
        raise AssertionError(f"Missing chapter-spine input: {path.relative_to(ROOT)}") from None
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from None


def main() -> int:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    try:
        helper = load_architecture_helper()
        spines = load_json(SPINE_PATH)
        spine_schema = load_json(SPINE_SCHEMA_PATH)
        ledger = load_json(LEDGER_PATH)
        inventory = load_json(INVENTORY_PATH)
    except AssertionError as exc:
        print(f"Chapter spines: FAILED\n- {exc}")
        return 1

    spines = copy.deepcopy(spines)

    fixture = os.environ.get("CHAPTER_SPINE_NEGATIVE_FIXTURE", "")
    if fixture == "ratified_without_decision":
        for chapter in spines.get("chapters", []):
            if chapter.get("ratified") is True:
                chapter.pop("decision", None)
                break
    elif fixture == "part_i_visible_code_admitted":
        for chapter in spines.get("chapters", []):
            if chapter.get("id") in NO_VISIBLE_CODE_UNITS and chapter.get("ratified") is True:
                chapter["exclusions"] = [
                    value for value in chapter.get("exclusions", []) if "vidljivi blok koda" not in value
                ]
                break
    elif fixture:
        errors.append(f"Unknown chapter-spine negative fixture: {fixture}")

    errors.extend(helper.validate_schema(spines, spine_schema, spine_schema))

    chapters = spines.get("chapters", [])
    check([chapter.get("id") for chapter in chapters] == UNIT_ORDER,
          "The chapter-spine registry must list all 19 units in canonical order.")

    ratified = [chapter for chapter in chapters if chapter.get("ratified") is True]
    unratified = [chapter for chapter in chapters if chapter.get("ratified") is not True]

    for chapter in ratified:
        unit = chapter.get("id", "<missing>")
        check(bool(chapter.get("key_aspects")), f"Ratified spine {unit} has no load-bearing aspect.")
        check(
            chapter.get("decision") == GATE_OF_UNIT.get(unit),
            f"Ratified spine {unit} must name gate {GATE_OF_UNIT.get(unit)}.",
        )
        check(bool(chapter.get("decision_record")), f"Ratified spine {unit} has no durable decision record.")
        check(bool(chapter.get("ratified_at")), f"Ratified spine {unit} has no ratification date.")
        check("prerequisites" in chapter, f"Ratified spine {unit} must state its prerequisites explicitly.")
        check(bool(chapter.get("exclusions")), f"Ratified spine {unit} has no exclusions.")
        for prerequisite in chapter.get("prerequisites", []):
            check(
                prerequisite in UNIT_ORDER,
                f"Ratified spine {unit} names an unknown prerequisite unit: {prerequisite}",
            )
            if prerequisite in UNIT_ORDER:
                check(
                    UNIT_ORDER.index(prerequisite) < UNIT_ORDER.index(unit),
                    f"Ratified spine {unit} names a later unit as its prerequisite: {prerequisite}",
                )
        markers = REQUIRED_EXCLUSION_MARKERS.get(unit, [])
        rendered = " ".join(chapter.get("exclusions", []))
        for marker in markers:
            check(
                marker in rendered,
                f"Ratified spine {unit} does not state its required exclusion about {marker!r}.",
            )

    for chapter in unratified:
        unit = chapter.get("id", "<missing>")
        check(
            not chapter.get("key_aspects") and not chapter.get("key_terms"),
            f"Unratified spine {unit} must stay empty until its gate passes.",
        )
        check(
            "decision" not in chapter and "exclusions" not in chapter,
            f"Unratified spine {unit} must not carry a decision or exclusions.",
        )

    stages = {unit.get("id"): unit.get("stage") for unit in ledger.get("chapters", [])}
    check(
        set(stages.values()) == {"draft"},
        "Spine ratification alone may not advance any chapter stage beyond draft.",
    )
    check(
        sorted(stages) == sorted(UNIT_ORDER),
        "The chapter ledger and the chapter-spine registry must cover the same 19 units.",
    )
    check(
        inventory.get("solution_routes") == [],
        "Spine ratification may not create a solution route.",
    )

    if errors:
        print("Chapter spines: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    digest = hashlib.sha256(
        json.dumps(spines, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    print("CHAPTER_SPINES_OK")
    print(f"- state: spine:sha256-{digest}")
    print(f"- units: {len(chapters)}; ratified: {len(ratified)}; unratified: {len(unratified)}")
    for chapter in ratified:
        print(
            f"- {chapter['id']}: gate {chapter['decision']}, "
            f"aspects {len(chapter.get('key_aspects', []))}, "
            f"terms {len(chapter.get('key_terms', []))}, "
            f"prerequisites {len(chapter.get('prerequisites', []))}, "
            f"exclusions {len(chapter.get('exclusions', []))}"
        )
    print("- chapter stages: 19 draft; solution routes: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
