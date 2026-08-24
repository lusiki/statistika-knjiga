#!/usr/bin/env python3
"""Validate the ratified G-A2d assessment architecture without new dependencies."""

from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import json
import math
import os
import re
import sys
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONVENTIONS_PATH = ROOT / "bookwright_plugin/bookwright/shared/conventions.json"
CONVENTIONS_SCHEMA_PATH = ROOT / "bookwright_plugin/bookwright/shared/schemas/conventions.schema.json"
SOLUTION_SCHEMA_PATH = ROOT / "bookwright_plugin/bookwright/shared/schemas/solution-record.schema.json"
SOLUTION_RECORD_ROOT = ROOT / "assessment/solution-records"
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


def schema_ref(schema_root: dict[str, Any], reference: str) -> dict[str, Any]:
    node: Any = schema_root
    for part in reference.removeprefix("#/").split("/"):
        node = node[part]
    if not isinstance(node, dict):
        raise AssertionError(f"Solution schema reference is not an object: {reference}")
    return node


def schema_type_matches(value: Any, expected: str) -> bool:
    checks = {
        "object": lambda candidate: isinstance(candidate, dict),
        "array": lambda candidate: isinstance(candidate, list),
        "string": lambda candidate: isinstance(candidate, str),
        "boolean": lambda candidate: isinstance(candidate, bool),
        "integer": lambda candidate: isinstance(candidate, int) and not isinstance(candidate, bool),
        "number": lambda candidate: isinstance(candidate, (int, float)) and not isinstance(candidate, bool),
        "null": lambda candidate: candidate is None,
    }
    return expected in checks and checks[expected](value)


def validate_solution_schema(
    value: Any,
    schema: dict[str, Any],
    schema_root: dict[str, Any],
    location: str = "$",
) -> list[str]:
    """Validate the dependency-free JSON-Schema subset used by solution records."""
    if "$ref" in schema:
        return validate_solution_schema(value, schema_ref(schema_root, schema["$ref"]), schema_root, location)

    errors: list[str] = []
    if "const" in schema and value != schema["const"]:
        errors.append(f"{location}: expected constant {schema['const']!r}, found {value!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{location}: value {value!r} is outside {schema['enum']!r}")

    expected_types = schema.get("type")
    if isinstance(expected_types, str):
        expected_types = [expected_types]
    if isinstance(expected_types, list) and not any(schema_type_matches(value, item) for item in expected_types):
        return errors + [f"{location}: expected one of {expected_types!r}, found {type(value).__name__}"]

    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{location}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{location}: unexpected property {key!r}")
        for key, child_schema in properties.items():
            if key in value:
                errors.extend(
                    validate_solution_schema(value[key], child_schema, schema_root, f"{location}.{key}")
                )

    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{location}: fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{location}: more than {schema['maxItems']} items")
        for index, child_schema in enumerate(schema.get("prefixItems", [])):
            if index < len(value):
                errors.extend(
                    validate_solution_schema(value[index], child_schema, schema_root, f"{location}[{index}]")
                )
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                errors.extend(validate_solution_schema(item, item_schema, schema_root, f"{location}[{index}]"))

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{location}: string is shorter than {schema['minLength']}")
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            errors.append(f"{location}: string does not match {schema['pattern']!r}")

    return errors


def without_profile_regions(lines: list[str], anchor: str) -> list[str]:
    """Remove complete nested when-profile fenced divs while preserving other markup."""
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
        raise AssertionError(f"Source anchor {anchor!r} contains an unclosed when-profile region")
    return result


def canonical_prompt(lines: list[str], anchor: str) -> str:
    """Return the LF-normalized, default-visible prompt body bound to an anchor."""
    matches = [index for index, line in enumerate(lines) if f"#{anchor}" in line]
    if len(matches) != 1:
        raise AssertionError(f"Source anchor {anchor!r} occurs {len(matches)} times")
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
            raise AssertionError(f"Source anchor {anchor!r} has an unclosed owner fence")
    else:
        heading = re.match(r"^(#+)\s", owner)
        if not heading:
            raise AssertionError(f"Source anchor {anchor!r} is not on a fenced div or heading")
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


def profile_visible_regions(lines: list[str], profile: str) -> list[str]:
    """Collect content-visible regions assigned to one Quarto profile."""
    regions: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if (
            re.match(r"^:::+\s*\{", line)
            and "content-visible" in line
            and re.search(rf'when-profile=["\']{re.escape(profile)}["\']', line)
        ):
            depth = 1
            body: list[str] = []
            index += 1
            while index < len(lines) and depth:
                nested = lines[index]
                if re.match(r"^:::+\s*\{", nested):
                    depth += 1
                elif re.match(r"^:::+\s*$", nested):
                    depth -= 1
                    if depth == 0:
                        break
                if depth:
                    body.append(nested)
                index += 1
            regions.append("\n".join(body).strip())
        index += 1
    return regions


def profile_projection(lines: list[str], profile: str | None) -> str:
    """Project profile-conditional fenced-div content without invoking a render."""
    active_stack: list[bool] = []
    output: list[str] = []
    for line in lines:
        opened = re.match(r"^:::+\s*\{(.*)\}\s*$", line)
        if opened:
            attrs = opened.group(1)
            inherited = all(active_stack) if active_stack else True
            profile_match = re.search(r'when-profile=["\']([^"\']+)["\']', attrs)
            active = inherited
            if profile_match and "content-visible" in attrs:
                active = inherited and profile == profile_match.group(1)
            elif profile_match and "content-hidden" in attrs:
                active = inherited and profile != profile_match.group(1)
            active_stack.append(active)
            continue
        if re.match(r"^:::+\s*$", line) and active_stack:
            active_stack.pop()
            continue
        if all(active_stack) if active_stack else True:
            output.append(line)
    return "\n".join(output)


def normalize_for_leak_check(value: str) -> str:
    return " ".join(value.split()).casefold()


def protected_record_strings(record: dict[str, Any]) -> list[str]:
    rubric = record["answer_components"]["severity_ranked_rubric"]
    values: list[str] = []
    for criterion in rubric["criteria"]:
        values.extend([criterion["description"], criterion["observable_evidence"]])
    for alternative in record["alternatives"]:
        values.extend([alternative["description"], alternative["acceptance_boundary"]])
    values.extend(record["instructor_notes"])
    return [value for value in values if len(normalize_for_leak_check(value)) >= 40]


def applicability_errors(record: dict[str, Any], location: str) -> list[str]:
    errors: list[str] = []
    components = record["answer_components"]
    content_fields = {
        "planted_error": ["error_id", "statement", "why_wrong"],
        "revealing_diagnostic": ["procedure", "expected_evidence"],
        "plausible_non_answers": ["responses"],
        "model_response_components": ["components"],
        "numerical_check": [
            "expected_result",
            "tolerance_or_acceptance_rule",
            "independent_method",
            "evidence_reference",
        ],
    }
    for component_name, fields in content_fields.items():
        component = components[component_name]
        applicable = component["applicable"]
        reason = component["not_applicable_reason"]
        values = [component[field] for field in fields]
        if applicable:
            if reason is not None:
                errors.append(f"{location}.{component_name}: applicable component has a not-applicable reason")
            for field, value in zip(fields, values):
                if value is None or value == [] or value == "":
                    errors.append(f"{location}.{component_name}.{field}: applicable content is empty")
        else:
            if not isinstance(reason, str) or not reason.strip():
                errors.append(f"{location}.{component_name}: not-applicable reason is missing")
            for field, value in zip(fields, values):
                if value not in (None, []):
                    errors.append(f"{location}.{component_name}.{field}: not-applicable content must be empty")
    return errors


def unit_00_numerical_check(lines: list[str], records: list[dict[str, Any]]) -> tuple[list[str], dict[str, str]]:
    """Recompute every unit 00 numerical answer from the chapter's stated table."""
    errors: list[str] = []
    table_rows: dict[str, tuple[int, Decimal]] = {}
    for line in lines:
        match = re.match(r"^\|\s*([^|]+?)\s*\|\s*([0-9.]+)\s*\|\s*([0-9,]+)\s*%\s*\|$", line)
        if not match:
            continue
        label = match.group(1).strip()
        count = int(match.group(2).replace(".", ""))
        stated_share = Decimal(match.group(3).replace(",", ".")) / Decimal(100)
        table_rows[label] = (count, stated_share)

    required_labels = {"portal", "društvene mreže", "TV", "radio", "tisak"}
    if set(table_rows) != required_labels:
        return [f"Unit 00 table rows disagree with the five declared categories: {sorted(table_rows)}"], {}

    total = sum(count for count, _ in table_rows.values())
    portal_count, portal_stated = table_rows["portal"]
    network_count, network_stated = table_rows["društvene mreže"]
    portal_share = Decimal(portal_count) / Decimal(total)
    network_share = Decimal(network_count) / Decimal(total)
    gap = portal_share - network_share
    if portal_share != portal_stated:
        errors.append("Unit 00 portal share does not reproduce from the chapter table.")
    if network_share != network_stated:
        errors.append("Unit 00 social-network share does not reproduce from the chapter table.")
    if portal_count >= total // 2:
        errors.append("Unit 00 planted-error premise drifted: portal is no longer below half the stated total.")

    by_class = {record["task_class"]: record for record in records}
    applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_applicable = {"callout_greska", "racunski", "revizija_modela"}
    if applicable != expected_applicable:
        errors.append(f"Unit 00 numerical applicability mismatch: {sorted(applicable)}")

    hr_integer = lambda value: f"{value:,}".replace(",", ".")
    hr_decimal = lambda value: f"{value:.3f}".replace(".", ",")
    hr_percent = lambda value: hr_decimal(value * 100) + " %"
    expected_tokens = {
        "callout_greska": [
            f"{hr_integer(portal_count)} / {hr_integer(total)}",
            hr_percent(portal_share),
            f"{hr_integer(portal_count)} < {hr_integer(total // 2)}",
        ],
        "racunski": [
            f"{hr_integer(network_count)} / {hr_integer(total)}",
            hr_percent(network_share),
            f"{hr_decimal(gap * 100)} postotnih bodova",
            f"{hr_integer(portal_count - network_count)} zapisa",
        ],
        "revizija_modela": [
            f"{hr_integer(network_count)} / {hr_integer(total)}",
            hr_percent(network_share),
        ],
    }
    for task_class, tokens in expected_tokens.items():
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        missing = [token for token in tokens if token not in result]
        if missing:
            errors.append(f"Unit 00 {task_class} numerical result lacks recomputed tokens: {missing}")

    evidence = {
        "total": str(total),
        "portal_share": f"{portal_share * 100:.3f}",
        "network_share": f"{network_share * 100:.3f}",
        "gap_pp": f"{gap * 100:.3f}",
        "count_gap": str(portal_count - network_count),
        "applicable_records": str(len(applicable)),
    }
    return errors, evidence


def unit_01_numerical_check(
    lines: list[str], records: list[dict[str, Any]], data_path: Path
) -> tuple[list[str], dict[str, str]]:
    """Recompute every unit 01 numerical answer from its CSV and stated simulation."""
    errors: list[str] = []
    try:
        with data_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        return [f"Unit 01 data could not be read independently: {exc}"], {}

    required_labels = {"portal", "društvene mreže", "tisak"}
    by_label = {row.get("izvor_vijesti", ""): row for row in rows}
    missing = required_labels - set(by_label)
    if missing:
        return [f"Unit 01 data lacks required categories: {sorted(missing)}"], {}

    paid: dict[str, tuple[int, int, Decimal]] = {}
    for label in required_labels:
        row = by_label[label]
        try:
            denominator = int(row["broj"])
            numerator = int(row["broj_platio"])
            stored_share = Decimal(row["udio_platio"])
        except (KeyError, ValueError, ArithmeticError) as exc:
            errors.append(f"Unit 01 {label} payment fields are invalid: {exc}")
            continue
        share = Decimal(numerator) / Decimal(denominator)
        if abs(share - stored_share) > Decimal("1e-15"):
            errors.append(f"Unit 01 {label} stored payment share does not reproduce.")
        paid[label] = (numerator, denominator, share)
    if len(paid) != len(required_labels):
        return errors, {}

    try:
        numerical_prompt = canonical_prompt(lines, "ex-01-racunski-01")
    except AssertionError as exc:
        return errors + [f"Unit 01 numerical prompt is unavailable: {exc}"], {}
    normalized_numerical_prompt = " ".join(numerical_prompt.split())
    if (
        "ručno podijelite" not in normalized_numerical_prompt
        or "možete provjeriti widgetom" not in normalized_numerical_prompt
    ):
        errors.append(
            "Unit 01 print path must require a hand calculation and describe the widget only as an optional check."
        )
    simulation = re.search(
        r"stope skupine A.*?(\d+)\s*%\s*i\s*(\d+)\s*%.*?"
        r"stope skupine B\s*(\d+)\s*%\s*i\s*(\d+)\s*%.*?"
        r"obje skupine imaju po\s*(\d+)\s*%",
        numerical_prompt,
        flags=re.DOTALL,
    )
    if not simulation:
        return errors + ["Unit 01 Simpson exercise values could not be parsed from the source prompt."], {}
    a_high, a_low, b_high, b_low, common_weight = (
        Decimal(value) / Decimal(100) for value in simulation.groups()
    )
    a_aggregate = common_weight * a_high + (Decimal(1) - common_weight) * a_low
    b_aggregate = common_weight * b_high + (Decimal(1) - common_weight) * b_low
    if not (b_high > a_high and b_low > a_low and b_aggregate > a_aggregate):
        errors.append("Unit 01 equal-weight Simpson exercise no longer supports its stated no-reversal conclusion.")

    by_class = {record["task_class"]: record for record in records}
    applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_applicable = {"callout_greska", "racunski", "revizija_modela"}
    if applicable != expected_applicable:
        errors.append(f"Unit 01 numerical applicability mismatch: {sorted(applicable)}")

    portal_n, portal_d, portal_share = paid["portal"]
    print_n, print_d, print_share = paid["tisak"]
    network_n, network_d, network_share = paid["društvene mreže"]
    print_network_gap = print_share - network_share
    hr_integer = lambda value: f"{value:,}".replace(",", ".")
    hr_decimal = lambda value: f"{value:.2f}".replace(".", ",")
    hr_percent = lambda value: hr_decimal(value * 100) + " %"
    expected_tokens = {
        "callout_greska": [
            f"{hr_integer(portal_n)} / {hr_integer(portal_d)}",
            hr_percent(portal_share),
            f"{hr_integer(print_n)} / {hr_integer(print_d)}",
            hr_percent(print_share),
        ],
        "racunski": [
            f"{hr_integer(portal_n)} / {hr_integer(portal_d)}",
            hr_percent(portal_share),
            f"{hr_integer(print_n)} / {hr_integer(print_d)}",
            hr_percent(print_share),
            f"{hr_integer(network_n)} / {hr_integer(network_d)}",
            hr_percent(network_share),
            f"{hr_decimal(print_network_gap * 100)} postotnih bodova",
            hr_percent(a_aggregate),
            hr_percent(b_aggregate),
        ],
        "revizija_modela": [
            f"{hr_integer(portal_n)} / {hr_integer(portal_d)}",
            hr_percent(portal_share),
            f"{hr_integer(print_n)} / {hr_integer(print_d)}",
            hr_percent(print_share),
        ],
    }
    for task_class, tokens in expected_tokens.items():
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        missing_tokens = [token for token in tokens if token not in result]
        if missing_tokens:
            errors.append(f"Unit 01 {task_class} numerical result lacks recomputed tokens: {missing_tokens}")

    evidence = {
        "portal_share": f"{portal_share * 100:.5f}",
        "print_share": f"{print_share * 100:.5f}",
        "network_share": f"{network_share * 100:.5f}",
        "print_network_gap_pp": f"{print_network_gap * 100:.5f}",
        "simpson_a": f"{a_aggregate * 100:.2f}",
        "simpson_b": f"{b_aggregate * 100:.2f}",
        "applicable_records": str(len(applicable)),
        "print_path": "hand-calculation-with-optional-widget-check",
    }
    return errors, evidence


def unit_02_numerical_check(
    lines: list[str], records: list[dict[str, Any]]
) -> tuple[list[str], dict[str, str]]:
    """Recompute every unit 02 numerical answer from the authored response rows."""
    errors: list[str] = []
    rows: dict[str, tuple[int, int, int, int]] = {}
    in_response_data = False
    for line in lines:
        if line.strip() == "s2_odgovori <- tribble(":
            in_response_data = True
            continue
        if in_response_data and line.strip() == ")":
            break
        if not in_response_data:
            continue
        match = re.match(
            r'^\s*"(I\d{2})",\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),?\s*$',
            line,
        )
        if match:
            rows[match.group(1)] = tuple(int(value) for value in match.groups()[1:])

    expected_ids = {f"I{index:02d}" for index in range(1, 13)}
    if set(rows) != expected_ids:
        return [f"Unit 02 response rows disagree with I01-I12: {sorted(rows)}"], {}

    try:
        numerical_prompt = canonical_prompt(lines, "ex-02-racunski-01")
    except AssertionError as exc:
        return [f"Unit 02 numerical prompt is unavailable: {exc}"], {}
    normalized_prompt = " ".join(numerical_prompt.split())
    required_print_tokens = (
        "tablicu povezanosti stavki",
        "ručno provjerite",
        "iz tablice s odgovorima",
        "izračunajte prosjek",
        "nalazi se u praktikumu",
    )
    if not all(token in normalized_prompt for token in required_print_tokens):
        errors.append(
            "Unit 02 print path must require hand calculation from the displayed tables and leave the full-data praktikum as an optional extension."
        )

    scale = re.search(r"od\s+(\d+)\s+do\s+(\d+)", numerical_prompt)
    if not scale:
        return errors + ["Unit 02 reverse-coding scale endpoints are absent from the source prompt."], {}
    scale_low, scale_high = (int(value) for value in scale.groups())
    reverse_constant = scale_low + scale_high
    mapping = {value: reverse_constant - value for value in range(scale_low, scale_high + 1)}
    expected_mapping = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
    if mapping != expected_mapping:
        errors.append(f"Unit 02 reverse-coding map drifted: {mapping}")

    means: dict[str, tuple[Decimal, Decimal]] = {}
    for respondent in ("I01", "I02", "I03"):
        original = rows[respondent]
        reversed_values = (*original[:3], mapping[original[3]])
        before = Decimal(sum(original)) / Decimal(len(original))
        after = Decimal(sum(reversed_values)) / Decimal(len(reversed_values))
        means[respondent] = (before, after)

    by_class = {record["task_class"]: record for record in records}
    applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_applicable = {"racunski"}
    if applicable != expected_applicable:
        errors.append(f"Unit 02 numerical applicability mismatch: {sorted(applicable)}")

    hr_decimal = lambda value: f"{value:.2f}".replace(".", ",")
    mapping_token = ", ".join(f"{source}→{target}" for source, target in mapping.items())
    expected_tokens = [mapping_token]
    expected_tokens.extend(
        f"{respondent} prije {hr_decimal(before)} i nakon {hr_decimal(after)}"
        for respondent, (before, after) in means.items()
    )
    result = str(by_class["racunski"]["answer_components"]["numerical_check"]["expected_result"])
    missing_tokens = [token for token in expected_tokens if token not in result]
    if missing_tokens:
        errors.append(f"Unit 02 racunski numerical result lacks recomputed tokens: {missing_tokens}")

    evidence = {
        "mapping": "/".join(f"{source}-to-{target}" for source, target in mapping.items()),
        "i01": f"{means['I01'][0]:.2f}/{means['I01'][1]:.2f}",
        "i02": f"{means['I02'][0]:.2f}/{means['I02'][1]:.2f}",
        "i03": f"{means['I03'][0]:.2f}/{means['I03'][1]:.2f}",
        "applicable_records": str(len(applicable)),
        "print_path": "hand-calculation-from-rendered-tables-with-optional-full-data-praktikum",
    }
    return errors, evidence


def unit_03_numerical_check(
    lines: list[str], records: list[dict[str, Any]], data_path: Path
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 03 turnout and simulated-media answers from source inputs."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-03-callout-greska-01")
        numerical_prompt = canonical_prompt(lines, "ex-03-racunski-01")
    except AssertionError as exc:
        return [f"Unit 03 numerical prompt is unavailable: {exc}"], {}

    turnout_match = re.search(
        r"(\d{1,3}(?:\.\d{3})+)\s+važećih.*?"
        r"(\d{1,3}(?:\.\d{3})+)\s+nevažećih.*?"
        r"(\d{1,3}(?:\.\d{3})+)\s+birača prema glasačkim listićima.*?"
        r"(\d{1,3}(?:\.\d{3})+)\s+manje od\s+"
        r"(\d{1,3}(?:\.\d{3})+)\s+pristupilih.*?"
        r"približno\s+([0-9]+,[0-9]+)\s*%",
        callout_prompt,
        flags=re.DOTALL,
    )
    if not turnout_match:
        return ["Unit 03 turnout values could not be parsed from the planted-error prompt."], {}

    parse_hr_integer = lambda value: int(value.replace(".", ""))
    valid, invalid, stated_ballots, stated_gap, accessed = (
        parse_hr_integer(value) for value in turnout_match.groups()[:5]
    )
    stated_relative_percent = Decimal(turnout_match.group(6).replace(",", "."))
    ballots = valid + invalid
    turnout_gap = accessed - ballots
    relative_gap_percent = Decimal(turnout_gap) / Decimal(accessed) * Decimal(100)
    if ballots != stated_ballots:
        errors.append("Unit 03 stated ballot total does not reproduce from valid and invalid ballots.")
    if turnout_gap != stated_gap:
        errors.append("Unit 03 stated turnout gap does not reproduce from the two operational totals.")
    if abs(relative_gap_percent - stated_relative_percent) > Decimal("0.005"):
        errors.append("Unit 03 stated relative turnout gap is not the rounded independent result.")

    try:
        with data_path.open(encoding="utf-8", newline="") as handle:
            data_rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        return errors + [f"Unit 03 data could not be read independently: {exc}"], {}
    by_label = {row.get("izvor_vijesti", ""): row for row in data_rows}
    missing_labels = {"portal", "TV"} - set(by_label)
    if missing_labels:
        return errors + [f"Unit 03 data lacks required categories: {sorted(missing_labels)}"], {}

    media: dict[str, tuple[int, int, Decimal]] = {}
    for label in ("portal", "TV"):
        row = by_label[label]
        try:
            count = int(row["broj"])
            total = int(row["ukupno"])
            stored_share = Decimal(row["udio"])
        except (KeyError, ValueError, ArithmeticError) as exc:
            errors.append(f"Unit 03 {label} aggregate fields are invalid: {exc}")
            continue
        share = Decimal(count) / Decimal(total)
        if share != stored_share:
            errors.append(f"Unit 03 {label} stored share does not reproduce.")
        media[label] = (count, total, share)
    if len(media) != 2:
        return errors, {}

    prompt_counts = re.search(
        r"portal je glavni izvor vijesti za\s+(\d{1,3}(?:\.\d{3})+)\s+od\s+"
        r"(\d{1,3}(?:\.\d{3})+)\s+generiranih osoba,\s+a\s+"
        r"televizija za\s+(\d{1,3}(?:\.\d{3})+)",
        numerical_prompt,
        flags=re.DOTALL,
    )
    if not prompt_counts:
        errors.append("Unit 03 simulated-media counts could not be parsed from the numerical prompt.")
    else:
        prompt_portal, prompt_total, prompt_tv = (
            parse_hr_integer(value) for value in prompt_counts.groups()
        )
        if (prompt_portal, prompt_total) != media["portal"][:2]:
            errors.append("Unit 03 portal prompt values disagree with the offline aggregate.")
        if (prompt_tv, prompt_total) != media["TV"][:2]:
            errors.append("Unit 03 television prompt values disagree with the offline aggregate.")

    normalized_prompt = " ".join(numerical_prompt.split()).casefold()
    required_print_tokens = (
        "15.101 od 50.000",
        "televizija za 10.827",
        "dopušten je kalkulator ili proračunska tablica",
        "ne predaje se kod",
    )
    if not all(token in normalized_prompt for token in required_print_tokens):
        errors.append(
            "Unit 03 print path must expose all counts, permit a calculator or spreadsheet, and require no code."
        )

    portal_count, portal_total, portal_share = media["portal"]
    tv_count, tv_total, tv_share = media["TV"]
    if portal_total != tv_total:
        errors.append("Unit 03 portal and television rows do not share the stated generated-population total.")
    share_gap = portal_share - tv_share
    relative_media_gap_percent = share_gap / tv_share * Decimal(100)

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 03 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    if planted_ids != {"small-relative-gap-erases-operational-distinction"}:
        errors.append(f"Unit 03 callout and model revision do not close one stable planted error: {planted_ids}")

    applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_applicable = {"callout_greska", "racunski", "revizija_modela"}
    if applicable != expected_applicable:
        errors.append(f"Unit 03 numerical applicability mismatch: {sorted(applicable)}")

    hr_integer = lambda value: f"{value:,}".replace(",", ".")
    hr_decimal = lambda value, digits: f"{value:.{digits}f}".replace(".", ",")
    turnout_tokens = [
        f"{hr_integer(valid)} + {hr_integer(invalid)} = {hr_integer(ballots)}",
        f"{hr_integer(accessed)} - {hr_integer(ballots)} = {hr_integer(turnout_gap)}",
    ]
    callout_tokens = turnout_tokens + [
        f"{hr_integer(turnout_gap)} / {hr_integer(accessed)} × 100 = "
        f"{hr_decimal(relative_gap_percent, 4)} %"
    ]
    computational_tokens = [
        f"{hr_integer(portal_count)} / {hr_integer(portal_total)} × 100 = "
        f"{hr_decimal(portal_share * 100, 3)} %",
        f"{hr_integer(tv_count)} / {hr_integer(tv_total)} × 100 = "
        f"{hr_decimal(tv_share * 100, 3)} %",
        f"{hr_decimal(portal_share * 100, 3)} % - {hr_decimal(tv_share * 100, 3)} % = "
        f"{hr_decimal(share_gap * 100, 3)} postotnih bodova",
        f"({hr_integer(portal_count)} - {hr_integer(tv_count)}) / {hr_integer(tv_count)} × 100 = "
        f"{hr_decimal(relative_media_gap_percent, 3)} %",
    ]
    expected_tokens = {
        "callout_greska": callout_tokens,
        "racunski": computational_tokens,
        "revizija_modela": turnout_tokens,
    }
    for task_class, tokens in expected_tokens.items():
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        missing_tokens = [token for token in tokens if token not in result]
        if missing_tokens:
            errors.append(f"Unit 03 {task_class} numerical result lacks recomputed tokens: {missing_tokens}")

    evidence = {
        "ballot_sum": str(ballots),
        "turnout_gap": str(turnout_gap),
        "turnout_relative_percent": f"{relative_gap_percent:.4f}",
        "portal_share": f"{portal_share * 100:.3f}",
        "tv_share": f"{tv_share * 100:.3f}",
        "share_gap_pp": f"{share_gap * 100:.3f}",
        "relative_media_gap_percent": f"{relative_media_gap_percent:.3f}",
        "applicable_records": str(len(applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "inline-counts-hand-calculation-with-calculator-or-spreadsheet-and-no-code",
    }
    return errors, evidence


def unit_04_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
    monthly_path: Path,
    annual_path: Path,
    aggregate_path: Path,
    sources_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 04 joins, preset summaries, aggregates, and source totals."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-04-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-04-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-04-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-04-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-04-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 04 prompt is unavailable: {exc}"], {}

    def read_rows(path: Path, label: str) -> list[dict[str, str]]:
        try:
            with path.open(encoding="utf-8", newline="") as handle:
                return list(csv.DictReader(handle))
        except (OSError, csv.Error) as exc:
            errors.append(f"Unit 04 {label} data could not be read independently: {exc}")
            return []

    monthly = read_rows(monthly_path, "monthly DigiKat")
    annual = read_rows(annual_path, "annual DigiKat")
    aggregate = read_rows(aggregate_path, "survey aggregate")
    sources = read_rows(sources_path, "DigiKat sources")
    if not all((monthly, annual, aggregate, sources)):
        return errors, {}

    try:
        monthly_values = [
            {
                "month": row["mjesec"],
                "year": row["godina"],
                "platform": row["platforma"],
                "posts": int(row["objave"]),
            }
            for row in monthly
        ]
        annual_keys = [(row["godina"], row["platforma"]) for row in annual]
    except (KeyError, ValueError) as exc:
        return errors + [f"Unit 04 DigiKat join fields are invalid: {exc}"], {}

    annual_by_year: dict[str, list[tuple[str, str]]] = {}
    for key in annual_keys:
        annual_by_year.setdefault(key[0], []).append(key)
    if len(annual_keys) != len(set(annual_keys)):
        errors.append("Unit 04 annual year-plus-platform key is not unique.")

    before_rows = len(monthly_values)
    before_keys = len({(row["month"], row["platform"]) for row in monthly_values})
    before_sum = sum(row["posts"] for row in monthly_values)
    missing_correct_keys = [
        (row["year"], row["platform"])
        for row in monthly_values
        if (row["year"], row["platform"]) not in set(annual_keys)
    ]
    if missing_correct_keys:
        errors.append(f"Unit 04 correct join lacks annual keys: {missing_correct_keys[:5]}")
    correct_rows = before_rows - len(missing_correct_keys)
    correct_keys = before_keys
    correct_sum = sum(
        row["posts"]
        for row in monthly_values
        if (row["year"], row["platform"]) in set(annual_keys)
    )
    wrong_rows = sum(len(annual_by_year.get(row["year"], [])) for row in monthly_values)
    wrong_keys = before_keys
    wrong_sum = sum(
        row["posts"] * len(annual_by_year.get(row["year"], []))
        for row in monthly_values
    )
    join_values = (
        before_rows,
        before_keys,
        before_sum,
        wrong_rows,
        wrong_keys,
        wrong_sum,
        correct_rows,
        correct_keys,
        correct_sum,
    )
    expected_join_values = (438, 438, 710307, 3571, 438, 5959081, 438, 438, 710307)
    if join_values != expected_join_values:
        errors.append(f"Unit 04 independent join state drifted: {join_values}")

    source_text = "\n".join(lines)
    preset_block = re.search(
        r"s4_w04_preseti\s*<-\s*tibble\(.*?Vrijednosti\s*=\s*c\((.*?)\),\s*"
        r"Sredina\s*=\s*c\((.*?)\),\s*Medijan\s*=\s*c\((.*?)\)\s*\)",
        source_text,
        flags=re.DOTALL,
    )
    if not preset_block:
        return errors + ["Unit 04 preset source values could not be parsed."], {}
    preset_strings = re.findall(r'"([0-9, ]+)"', preset_block.group(1))
    if len(preset_strings) < 2:
        return errors + ["Unit 04 lacks the two assessed preset series."], {}

    def parse_series(value: str) -> list[Decimal]:
        return [Decimal(token.strip()) for token in value.split(",")]

    def median(values: list[Decimal]) -> Decimal:
        ordered = sorted(values)
        middle = len(ordered) // 2
        if len(ordered) % 2:
            return ordered[middle]
        return (ordered[middle - 1] + ordered[middle]) / Decimal(2)

    compact = parse_series(preset_strings[0])
    extreme = parse_series(preset_strings[1])
    compact_sum = sum(compact, Decimal(0))
    compact_mean = compact_sum / Decimal(len(compact))
    compact_median = median(compact)
    extreme_sum = sum(extreme, Decimal(0))
    extreme_mean = extreme_sum / Decimal(len(extreme))
    extreme_median = median(extreme)
    mean_shift = extreme_mean - compact_mean
    median_shift = extreme_median - compact_median
    preset_values = (
        compact_sum,
        compact_mean,
        compact_median,
        extreme_sum,
        extreme_mean,
        extreme_median,
        mean_shift,
        median_shift,
    )
    expected_preset_values = tuple(
        Decimal(value) for value in ("110", "11", "11", "169", "16.9", "11.5", "5.9", "0.5")
    )
    if preset_values != expected_preset_values:
        errors.append(f"Unit 04 preset summaries drifted: {preset_values}")

    try:
        aggregate_by_code = {row["dobna_skupina_sifra"]: row for row in aggregate}
        first = aggregate_by_code["1"]
        first_count = int(first["broj"])
        first_total = int(first["ukupno"])
        first_minutes = int(first["zbroj_minuta"])
        first_mean_stored = Decimal(first["prosjek_minuta"])
        first_share_stored = Decimal(first["udio"])
        aggregate_count = sum(int(row["broj"]) for row in aggregate)
        aggregate_minutes = sum(int(row["zbroj_minuta"]) for row in aggregate)
    except (KeyError, ValueError, ArithmeticError) as exc:
        return errors + [f"Unit 04 survey aggregate fields are invalid: {exc}"], {}
    first_mean = Decimal(first_minutes) / Decimal(first_count)
    first_share = Decimal(first_count) / Decimal(first_total)
    if abs(first_mean - first_mean_stored) > Decimal("0.000000000001") or first_share != first_share_stored:
        errors.append("Unit 04 stored first aggregate row does not reproduce exactly.")
    if (first_count, first_total, first_minutes, aggregate_count, aggregate_minutes) != (
        90,
        300,
        7339,
        300,
        15019,
    ):
        errors.append("Unit 04 aggregate count or minute totals drifted.")

    try:
        source_counts = [int(row["objave"]) for row in sources]
    except (KeyError, ValueError) as exc:
        return errors + [f"Unit 04 DigiKat source counts are invalid: {exc}"], {}
    source_rows = len(source_counts)
    source_total = sum(source_counts)
    source_mean = Decimal(source_total) / Decimal(source_rows)
    source_median = median([Decimal(value) for value in source_counts])
    source_top_ten = sum(sorted(source_counts, reverse=True)[:10])
    source_top_share = Decimal(source_top_ten) / Decimal(source_total) * Decimal(100)
    if (source_rows, source_total, source_median, source_top_ten) != (3604, 551712, Decimal(4), 148748):
        errors.append("Unit 04 DigiKat source summary drifted.")

    normalized_numerical_prompt = " ".join(numerical_prompt.split()).casefold()
    required_print_tokens = (
        "zadatak je jednak u digitalnoj i tiskanoj inačici",
        "interakcija služi samo za dodatne pokuse",
        "zadatak ne zahtijeva pisanje koda",
        "u tisku su svi potrebni brojnici, nazivnici i provjereni odgovori već u tablici",
    )
    if not all(token in normalized_numerical_prompt for token in required_print_tokens):
        errors.append("Unit 04 print path must expose exact presets and aggregates without widget or code dependence.")
    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 04 {label} prompt is empty.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 04 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    if planted_ids != {"incomplete-join-key-multiplies-rows"}:
        errors.append(f"Unit 04 callout and model revision do not close one stable planted error: {planted_ids}")

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_applicable = {"callout_greska", "konceptualni", "racunski", "revizija_modela"}
    if numerical_applicable != expected_applicable:
        errors.append(f"Unit 04 numerical applicability mismatch: {sorted(numerical_applicable)}")

    hr_integer = lambda value: f"{value:,}".replace(",", ".")
    join_before = (
        f"{before_rows} redaka, {before_keys} jedinstvenih ključeva i "
        f"{hr_integer(before_sum)} objava"
    )
    join_wrong = (
        f"{hr_integer(wrong_rows)} redak, {wrong_keys} jedinstvenih ključeva i "
        f"{hr_integer(wrong_sum)} objava"
    )
    join_correct = (
        f"{correct_rows} redaka, {correct_keys} jedinstvenih ključeva i "
        f"{hr_integer(correct_sum)} objava"
    )
    expected_tokens = {
        "callout_greska": [join_before, join_wrong, join_correct],
        "konceptualni": [
            f"{before_rows} redaka, {before_keys} jedinstvenih mjesečnih ključeva i {hr_integer(before_sum)} objava",
            f"{hr_integer(wrong_rows)} redak, {wrong_keys} jedinstvenih mjesečnih ključeva i {hr_integer(wrong_sum)} objava",
        ],
        "racunski": [
            "110 / 10 = 11,0",
            "(11 + 11) / 2 = 11,0",
            "169 / 10 = 16,9",
            "(11 + 12) / 2 = 11,5",
            "pomak sredine 5,9 i medijana 0,5",
            "7.339 / 90 = 81,5444",
            "90 / 300 = 0,30 = 30 %",
            "90 + 84 + 66 + 60 = 300",
            "7.339 + 4.567 + 2.139 + 974 = 15.019",
        ],
        "revizija_modela": [join_wrong, join_correct],
    }
    for task_class, tokens in expected_tokens.items():
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        missing_tokens = [token for token in tokens if token not in result]
        if missing_tokens:
            errors.append(f"Unit 04 {task_class} numerical result lacks recomputed tokens: {missing_tokens}")

    critical_text = " ".join(
        component["required_claim"]
        for component in by_class["kriticki"]["answer_components"]["model_response_components"]["components"]
    )
    critical_tokens = (
        hr_integer(source_rows),
        f"{source_mean:.1f}".replace(".", ","),
        str(source_median),
        hr_integer(source_top_ten),
        hr_integer(source_total),
        f"{source_top_share:.2f}".replace(".", ","),
    )
    if not all(token in critical_text for token in critical_tokens):
        errors.append(f"Unit 04 critical answer lacks independently verified source tokens: {critical_tokens}")

    evidence = {
        "join_before": f"{before_rows}/{before_keys}/{before_sum}",
        "join_wrong": f"{wrong_rows}/{wrong_keys}/{wrong_sum}",
        "join_correct": f"{correct_rows}/{correct_keys}/{correct_sum}",
        "compact": f"{compact_mean:.1f}/{compact_median:.1f}",
        "extreme": f"{extreme_mean:.1f}/{extreme_median:.1f}",
        "aggregate_first": f"{first_mean:.4f}/{first_share * 100:.0f}%",
        "aggregate_totals": f"{aggregate_count}/{aggregate_minutes}",
        "source_summary": f"{source_rows}/{source_mean:.4f}/{source_median}/{source_top_ten}/{source_total}/{source_top_share:.4f}%",
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "rendered-preset-and-aggregate-tables-hand-calculation-widget-optional-no-code",
    }
    return errors, evidence


def unit_05_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
    aggregate_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 05 bar-area distortion and displayed group-mean comparison."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-05-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-05-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-05-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-05-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-05-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 05 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 05 {label} prompt is empty.")

    width_match = re.search(
        r"geom_col\s*\(\s*width\s*=\s*c\(([^)]*)\)",
        callout_prompt,
        flags=re.DOTALL,
    )
    if not width_match:
        return errors + ["Unit 05 planted-error width vector could not be parsed."], {}
    try:
        widths = [Decimal(value.strip()) for value in width_match.group(1).split(",")]
    except ArithmeticError as exc:
        return errors + [f"Unit 05 planted-error widths are invalid: {exc}"], {}
    if widths != [Decimal("0.6"), Decimal("0.6"), Decimal("0.9")]:
        errors.append(f"Unit 05 planted-error width vector drifted: {widths}")
    narrow_width = min(widths)
    wide_width = max(widths)
    area_ratio = wide_width / narrow_width
    area_increase = (area_ratio - Decimal(1)) * Decimal(100)
    if (area_ratio, area_increase) != (Decimal("1.5"), Decimal(50)):
        errors.append(
            f"Unit 05 independent area distortion drifted: ratio={area_ratio}, increase={area_increase}%"
        )

    try:
        with aggregate_path.open(encoding="utf-8", newline="") as handle:
            aggregate = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        return errors + [f"Unit 05 survey aggregate could not be read independently: {exc}"], {}
    if not aggregate:
        return errors + ["Unit 05 survey aggregate is empty."], {}

    try:
        group_means: list[tuple[str, Decimal, Decimal]] = []
        for row in aggregate:
            count = Decimal(row["broj"])
            minute_total = Decimal(row["zbroj_minuta"])
            recomputed = minute_total / count
            stored = Decimal(row["prosjek_minuta"])
            if abs(recomputed - stored) > Decimal("0.000000000001"):
                errors.append(
                    "Unit 05 stored group mean does not reproduce for "
                    f"{row['dobna_skupina']}: {stored} != {recomputed}"
                )
            group_means.append((row["dobna_skupina"], recomputed, stored))
    except (KeyError, ArithmeticError) as exc:
        return errors + [f"Unit 05 survey aggregate fields are invalid: {exc}"], {}

    maximum_group, maximum_mean, _ = max(group_means, key=lambda value: value[1])
    minimum_group, minimum_mean, _ = min(group_means, key=lambda value: value[1])
    exact_gap = maximum_mean - minimum_mean
    exact_percent = exact_gap / maximum_mean * Decimal(100)
    if (maximum_group, minimum_group) != ("18 do 24", "45 i više"):
        errors.append(
            f"Unit 05 extreme group identities drifted: {maximum_group!r}, {minimum_group!r}"
        )
    expected_exact = (
        Decimal(7339) / Decimal(90),
        Decimal(974) / Decimal(60),
        Decimal(7339) / Decimal(90) - Decimal(974) / Decimal(60),
    )
    if (maximum_mean, minimum_mean, exact_gap) != expected_exact:
        errors.append(
            "Unit 05 independent group means or absolute difference drifted: "
            f"{maximum_mean}, {minimum_mean}, {exact_gap}"
        )

    displayed_maximum = Decimal(f"{maximum_mean:.1f}")
    displayed_minimum = Decimal(f"{minimum_mean:.1f}")
    displayed_gap = displayed_maximum - displayed_minimum
    displayed_percent = displayed_gap / displayed_maximum * Decimal(100)
    if (
        displayed_maximum,
        displayed_minimum,
        displayed_gap,
        Decimal(f"{displayed_percent:.1f}"),
        Decimal(f"{exact_percent:.1f}"),
    ) != (
        Decimal("81.5"),
        Decimal("16.2"),
        Decimal("65.3"),
        Decimal("80.1"),
        Decimal("80.1"),
    ):
        errors.append("Unit 05 displayed or full-precision percentage calculation drifted.")

    normalized_source = " ".join(lines).casefold()
    normalized_numerical_prompt = " ".join(numerical_prompt.split()).casefold()
    if not all(
        token in normalized_source
        for token in ("label: tbl-s5-skupine", "label: fig-skraceni-raspon")
    ) or not all(
        token in normalized_numerical_prompt
        for token in (
            "#tbl-s5-skupine",
            "#fig-skraceni-raspon",
            "svi potrebni podaci nalaze se u tablici",
        )
    ):
        errors.append(
            "Unit 05 print path must expose the rendered summary table and static axis comparison."
        )
    if "bez pisanja ili popravljanja koda" not in " ".join(revision_prompt.split()).casefold():
        errors.append("Unit 05 revision deliverable must remain code-free.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 05 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    if planted_ids != {"unequal-bar-width-encodes-unsupported-area"}:
        errors.append(
            "Unit 05 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_applicable = {"callout_greska", "racunski", "revizija_modela"}
    if numerical_applicable != expected_applicable:
        errors.append(f"Unit 05 numerical applicability mismatch: {sorted(numerical_applicable)}")

    width_tokens = ["0,9 / 0,6 = 1,5", "50 %"]
    for task_class in ("callout_greska", "revizija_modela"):
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        missing_tokens = [token for token in width_tokens if token not in result]
        if missing_tokens:
            errors.append(
                f"Unit 05 {task_class} numerical result lacks recomputed tokens: {missing_tokens}"
            )

    numerical_record = by_class["racunski"]["answer_components"]["numerical_check"]
    displayed_tokens = ["81,5", "16,2", "65,3", "80,1 %"]
    missing_displayed = [
        token for token in displayed_tokens if token not in str(numerical_record["expected_result"])
    ]
    if missing_displayed:
        errors.append(f"Unit 05 numerical result lacks recomputed display tokens: {missing_displayed}")
    full_precision_tokens = ["65,3111", "80,0927 %"]
    numerical_acceptance = str(numerical_record["tolerance_or_acceptance_rule"])
    missing_precision = [token for token in full_precision_tokens if token not in numerical_acceptance]
    if missing_precision:
        errors.append(
            f"Unit 05 numerical acceptance lacks independent full-precision tokens: {missing_precision}"
        )

    evidence = {
        "widths": "/".join(f"{width:.1f}" for width in widths),
        "area_ratio": f"{area_ratio:.1f}",
        "area_increase_percent": f"{area_increase:.0f}",
        "maximum": f"{maximum_mean:.4f}",
        "minimum": f"{minimum_mean:.4f}",
        "gap": f"{exact_gap:.4f}",
        "relative_percent": f"{exact_percent:.4f}",
        "displayed": (
            f"{displayed_maximum:.1f}/{displayed_minimum:.1f}/"
            f"{displayed_gap:.1f}/{displayed_percent:.1f}%"
        ),
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "rendered-summary-table-and-static-axis-comparison-hand-calculation-no-code",
    }
    return errors, evidence


def unit_06_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
    survey_path: Path,
    eurostat_path: Path,
    widget_registry_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 06 correlations, filtered scope, Eurostat pairs and print deviations."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-06-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-06-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-06-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-06-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-06-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 06 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 06 {label} prompt is empty.")

    def pearson(left: list[float], right: list[float]) -> float:
        if len(left) != len(right) or len(left) < 2:
            raise ArithmeticError("correlation requires paired values")
        left_mean = sum(left) / len(left)
        right_mean = sum(right) / len(right)
        numerator = sum((x - left_mean) * (y - right_mean) for x, y in zip(left, right))
        left_ss = sum((x - left_mean) ** 2 for x in left)
        right_ss = sum((y - right_mean) ** 2 for y in right)
        denominator = math.sqrt(left_ss * right_ss)
        if denominator == 0:
            raise ArithmeticError("correlation denominator is zero")
        return numerator / denominator

    def average_ranks(values: list[float]) -> list[float]:
        order = sorted(range(len(values)), key=values.__getitem__)
        ranks = [0.0] * len(values)
        start = 0
        while start < len(order):
            end = start + 1
            while end < len(order) and values[order[end]] == values[order[start]]:
                end += 1
            average = (start + 1 + end) / 2
            for index in order[start:end]:
                ranks[index] = average
            start = end
        return ranks

    try:
        with survey_path.open(encoding="utf-8", newline="") as handle:
            survey = list(csv.DictReader(handle))
        if len(survey) != 300:
            errors.append(f"Unit 06 survey row count drifted: {len(survey)}")
        age = [float(row["dob"]) for row in survey]
        minutes = [float(row["minute_dnevno"]) for row in survey]
        trust = [float(row["povjerenje"]) for row in survey]
        youngest = [row for row in survey if row["dobna_skupina"] == "18 do 24"]
        youngest_age = [float(row["dob"]) for row in youngest]
        youngest_minutes = [float(row["minute_dnevno"]) for row in youngest]
        full_r = pearson(age, minutes)
        youngest_r = pearson(youngest_age, youngest_minutes)
        age_trust_r = pearson(age, trust)
        minutes_trust_r = pearson(minutes, trust)
        spearman_age_minutes = pearson(average_ranks(age), average_ranks(minutes))
    except (OSError, csv.Error, KeyError, ValueError, ArithmeticError) as exc:
        return errors + [f"Unit 06 survey could not be checked independently: {exc}"], {}

    expected_correlations = {
        "full": -0.559289315825884,
        "youngest": 0.180376722320621,
        "age_trust": -0.329040101725562,
        "minutes_trust": 0.179849462681741,
        "spearman_age_minutes": -0.680150964765922,
    }
    observed_correlations = {
        "full": full_r,
        "youngest": youngest_r,
        "age_trust": age_trust_r,
        "minutes_trust": minutes_trust_r,
        "spearman_age_minutes": spearman_age_minutes,
    }
    for label, expected in expected_correlations.items():
        observed = observed_correlations[label]
        if abs(observed - expected) > 1e-12:
            errors.append(
                f"Unit 06 {label} correlation drifted: {observed:.15f} != {expected:.15f}"
            )
    if len(youngest) != 90 or (min(youngest_age), max(youngest_age)) != (18, 24):
        errors.append(
            "Unit 06 filtered subgroup must contain 90 observations spanning ages 18 through 24."
        )

    try:
        with eurostat_path.open(encoding="utf-8", newline="") as handle:
            eurostat = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        return errors + [f"Unit 06 Eurostat extract could not be read independently: {exc}"], {}
    by_geo: dict[str, dict[str, dict[str, str]]] = {}
    for row in eurostat:
        by_geo.setdefault(row.get("geo", ""), {})[row.get("pokazatelj", "")] = row
    main_indicators = ("tercijarno_obrazovanje_25_34", "uporaba_interneta_16_74")
    early_indicator = "rano_napustanje_obrazovanja_18_24"

    def available(row: dict[str, str] | None) -> bool:
        return bool(row) and row.get("vrijednost_dostupna") == "da" and row.get("vrijednost") != ":"

    main_complete = [
        geo
        for geo, values in by_geo.items()
        if all(available(values.get(indicator)) for indicator in main_indicators)
    ]
    early_complete = [
        geo
        for geo, values in by_geo.items()
        if available(values.get(main_indicators[0])) and available(values.get(early_indicator))
    ]
    luxembourg_early = by_geo.get("LU", {}).get(early_indicator, {})
    croatia_early = by_geo.get("HR", {}).get(early_indicator, {})
    if len(by_geo) != 27 or len(main_complete) != 27 or len(early_complete) != 26:
        errors.append(
            "Unit 06 Eurostat pair counts drifted: "
            f"states={len(by_geo)}, main={len(main_complete)}, early={len(early_complete)}"
        )
    if not (
        luxembourg_early.get("vrijednost") == ":"
        and luxembourg_early.get("status_api") == "u"
        and luxembourg_early.get("vrijednost_dostupna") == "ne"
        and croatia_early.get("vrijednost") == "2.1"
        and croatia_early.get("status_api") == "u"
        and croatia_early.get("vrijednost_dostupna") == "da"
    ):
        errors.append("Unit 06 Eurostat absence-versus-status evidence drifted for LU or HR.")
    try:
        eurostat_tertiary = [
            float(by_geo[geo][main_indicators[0]]["vrijednost"]) for geo in main_complete
        ]
        eurostat_internet = [
            float(by_geo[geo][main_indicators[1]]["vrijednost"]) for geo in main_complete
        ]
        eurostat_main_r = pearson(eurostat_tertiary, eurostat_internet)
    except (KeyError, TypeError, ValueError, ArithmeticError) as exc:
        return errors + [f"Unit 06 Eurostat main correlation could not be checked: {exc}"], {}
    expected_eurostat_main_r = 0.4499935433452106
    if abs(eurostat_main_r - expected_eurostat_main_r) > 1e-12:
        errors.append(
            "Unit 06 Eurostat main correlation drifted: "
            f"{eurostat_main_r:.15f} != {expected_eurostat_main_r:.15f}"
        )

    try:
        widget_registry = load_json(widget_registry_path)
        widget_matches = [
            widget for widget in widget_registry.get("widgets", []) if widget.get("id") == "w06"
        ]
        if len(widget_matches) != 1:
            raise AssertionError(f"expected one w06 parity record, found {len(widget_matches)}")
        widget = widget_matches[0]
        r_expected = widget["parity"]["expected"]["r"]
        widget_correlations = [
            float(r_expected[f"cloud_{index}.correlation"]) for index in range(1, 5)
        ]
    except (AssertionError, KeyError, TypeError, ValueError) as exc:
        return errors + [f"Unit 06 w06 parity evidence is invalid: {exc}"], {}
    expected_widget = [
        -0.8481563468979553,
        -0.533683839737063,
        0.40057528730241643,
        0.7678317664817833,
    ]
    if any(abs(observed - expected) > 1e-12 for observed, expected in zip(widget_correlations, expected_widget)):
        errors.append(f"Unit 06 w06 R golden correlations drifted: {widget_correlations}")

    source_text = "\n".join(lines)
    preset_match = re.search(
        r"mutate\s*\(\s*procjena\s*=\s*c\(([^)]*)\)", source_text, flags=re.DOTALL
    )
    if not preset_match:
        return errors + ["Unit 06 print preset vector could not be parsed."], {}
    try:
        print_presets = [Decimal(value.strip()) for value in preset_match.group(1).split(",")]
    except ArithmeticError as exc:
        return errors + [f"Unit 06 print presets are invalid: {exc}"], {}
    if print_presets != [Decimal("-0.70"), Decimal("-0.20"), Decimal("0.20"), Decimal("0.50")]:
        errors.append(f"Unit 06 print presets drifted: {print_presets}")
    displayed_widget = [Decimal(f"{value:.2f}") for value in widget_correlations]
    print_deviations = [abs(value - preset) for value, preset in zip(displayed_widget, print_presets)]
    expected_deviations = [Decimal("0.15"), Decimal("0.33"), Decimal("0.20"), Decimal("0.27")]
    if print_deviations != expected_deviations:
        errors.append(f"Unit 06 print absolute deviations drifted: {print_deviations}")

    normalized_source = " ".join(lines).casefold()
    normalized_numerical_prompt = " ".join(numerical_prompt.split()).casefold()
    required_source_tokens = (
        "label: tbl-korelacije-anketa",
        "label: fig-zakrivljeno",
        "label: fig-w06-print",
        "label: tbl-w06-print-procjene",
    )
    required_prompt_tokens = (
        "tablicu korelacija triju varijabli",
        "u tisku uzmite četiri zadane procjene",
        "apsolutno odstupanje procjene",
    )
    if not all(token in normalized_source for token in required_source_tokens) or not all(
        token in normalized_numerical_prompt for token in required_prompt_tokens
    ):
        errors.append(
            "Unit 06 print path must expose the correlation table, scatterplot and fixed w06 preset table."
        )
    normalized_revision = " ".join(revision_prompt.split()).casefold()
    if "redak koda koji mijenja ciljnu skupinu" not in normalized_revision or any(
        phrase in normalized_revision for phrase in ("napišite kod", "popravite kod", "prepišite kod")
    ):
        errors.append("Unit 06 model revision must assess code reading without code production.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 06 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    if planted_ids != {"filtered-subgroup-generalized-to-full-sample"}:
        errors.append(
            "Unit 06 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_applicable = {"callout_greska", "konceptualni", "racunski", "revizija_modela"}
    if numerical_applicable != expected_applicable:
        errors.append(f"Unit 06 numerical applicability mismatch: {sorted(numerical_applicable)}")

    scope_tokens = ["n = 90", "r = 0,18", "n = 300", "r = -0,56"]
    for task_class in ("callout_greska", "revizija_modela"):
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        missing_tokens = [token for token in scope_tokens if token not in result]
        if missing_tokens:
            errors.append(
                f"Unit 06 {task_class} numerical result lacks recomputed tokens: {missing_tokens}"
            )
    conceptual_result = str(
        by_class["konceptualni"]["answer_components"]["numerical_check"]["expected_result"]
    )
    conceptual_tokens = ["27", "26", "2,1", "vrijednost :", "status u"]
    missing_conceptual = [token for token in conceptual_tokens if token not in conceptual_result]
    if missing_conceptual:
        errors.append(
            f"Unit 06 conceptual numerical result lacks source tokens: {missing_conceptual}"
        )
    numerical_result = str(
        by_class["racunski"]["answer_components"]["numerical_check"]["expected_result"]
    )
    numerical_tokens = [
        "-0,56",
        "-0,33",
        "0,18",
        "-0,68",
        "0,15",
        "0,33",
        "0,20",
        "0,27",
    ]
    missing_numerical = [token for token in numerical_tokens if token not in numerical_result]
    if missing_numerical:
        errors.append(f"Unit 06 numerical answer lacks recomputed tokens: {missing_numerical}")
    critical_components = " ".join(
        str(component.get("required_evidence", ""))
        for component in by_class["kriticki"]["answer_components"]["model_response_components"]["components"]
    )
    if "0,45" not in critical_components:
        errors.append("Unit 06 critical answer lacks the independently reproduced Eurostat r = 0,45.")

    evidence = {
        "full_sample": f"{len(survey)}/{full_r:.6f}/{spearman_age_minutes:.6f}",
        "youngest": f"{len(youngest)}/{youngest_r:.6f}/{int(min(youngest_age))}-{int(max(youngest_age))}",
        "pair_correlations": f"{full_r:.6f}/{age_trust_r:.6f}/{minutes_trust_r:.6f}",
        "eurostat_pairs": f"{len(main_complete)}/{len(early_complete)}/r-{eurostat_main_r:.6f}/HR-{croatia_early.get('vrijednost')}-u/LU-missing-u",
        "print_correlations": "/".join(f"{value:.2f}" for value in displayed_widget),
        "print_deviations": "/".join(f"{value:.2f}" for value in print_deviations),
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "rendered-correlation-table-scatterplot-and-fixed-w06-presets-no-code",
    }
    return errors, evidence


def unit_07_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
    chapter_03_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 07 complements and the chapter 03 verifier table."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-07-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-07-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-07-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-07-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-07-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 07 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 07 {label} prompt is empty.")

    p_failure = Decimal("0.98")
    no_success = p_failure**5
    at_least_one = Decimal("1") - no_success
    at_least_one_percent = Decimal("100") * at_least_one
    if no_success != Decimal("0.9039207968"):
        errors.append(f"Unit 07 no-success complement drifted: {no_success}")
    if at_least_one != Decimal("0.0960792032"):
        errors.append(f"Unit 07 at-least-one complement drifted: {at_least_one}")
    if at_least_one_percent != Decimal("9.6079203200"):
        errors.append(f"Unit 07 complement percentage drifted: {at_least_one_percent}")

    normalized_callout = " ".join(callout_prompt.split()).casefold()
    required_callout_tokens = (
        "p_viral <- 0.02",
        "1 - (1 - p_viral)^5",
        "zasebne jedinice iste kampanje",
        "račun potpun",
    )
    if not all(token in normalized_callout for token in required_callout_tokens):
        errors.append("Unit 07 callout no longer exposes the complete independence-dependent calculation.")

    try:
        chapter_03_text = chapter_03_path.read_text(encoding="utf-8")
    except OSError as exc:
        return errors + [f"Unit 07 chapter 03 reachback could not be read: {exc}"], {}
    verifier_match = re.search(
        r"Zamislimo\s+([\d.]+)\s+zapisa\.\s+Njih\s+([\d.]+).*?"
        r"Provjera\s+pronađe\s+([\d.]+)\s+od\s+tih\s+([\d.]+)\s+zapisa,\s+"
        r"ali\s+pogrešno\s+označi\s+i\s+([\d.]+)\s+ostalih\.\s+"
        r"Dobiva\s+([\d.]+)\s+upozorenja",
        chapter_03_text,
        flags=re.DOTALL,
    )
    if not verifier_match:
        return errors + ["Unit 07 chapter 03 verifier counts could not be parsed independently."], {}

    try:
        total, targets, true_alerts, repeated_targets, false_alerts, all_alerts = (
            int(value.replace(".", "")) for value in verifier_match.groups()
        )
    except ValueError as exc:
        return errors + [f"Unit 07 chapter 03 verifier counts are invalid: {exc}"], {}
    expected_counts = (10000, 100, 90, 100, 495, 585)
    observed_counts = (total, targets, true_alerts, repeated_targets, false_alerts, all_alerts)
    if observed_counts != expected_counts:
        errors.append(f"Unit 07 verifier counts drifted: {observed_counts} != {expected_counts}")
    if true_alerts + false_alerts != all_alerts:
        errors.append("Unit 07 verifier alert cells do not sum to all alerts.")
    missed_targets = targets - true_alerts
    true_negatives = total - targets - false_alerts
    sensitivity = Decimal(true_alerts) / Decimal(targets)
    precision = Decimal(true_alerts) / Decimal(all_alerts)
    base_rate = Decimal(targets) / Decimal(total)
    if (missed_targets, true_negatives) != (10, 9405):
        errors.append(
            f"Unit 07 verifier residual cells drifted: missed={missed_targets}, true_negative={true_negatives}"
        )
    if sensitivity != Decimal("0.9") or base_rate != Decimal("0.01"):
        errors.append(
            f"Unit 07 verifier exact rates drifted: sensitivity={sensitivity}, base={base_rate}"
        )
    if abs(precision - (Decimal(2) / Decimal(13))) > Decimal("1e-27"):
        errors.append(f"Unit 07 verifier precision drifted: {precision}")

    normalized_numerical = " ".join(numerical_prompt.split()).casefold()
    required_numerical_tokens = (
        "hipotetsku provjeru zapisa",
        "svih šest",
        "udio upozorenja među ciljanim zapisima",
        "udio ciljanih zapisa među svim upozorenjima",
        "temeljnu stopu",
        "kratku revizijsku tablicu",
        "dvije rečenice",
    )
    if not all(token in normalized_numerical for token in required_numerical_tokens):
        errors.append("Unit 07 numerical prompt no longer requires the full six-question reachback audit.")
    normalized_chapter_03 = " ".join(chapter_03_text.split()).casefold()
    if not all(
        token in normalized_chapter_03
        for token in ("10.000 zapisa", "90 od tih 100 zapisa", "495 ostalih", "585 upozorenja")
    ):
        errors.append("Unit 07 print reachback must preserve the rendered chapter 03 verifier counts.")

    normalized_conceptual = " ".join(conceptual_prompt.split()).casefold()
    if not all(
        token in normalized_conceptual
        for token in (
            "poštenoga novčića s poznatom vjerojatnošću",
            "stopa uspjeha nije poznata",
            "dokaz bio potreban",
            "velikom skupinom nula",
            "qq prikazu",
        )
    ):
        errors.append("Unit 07 conceptual prompt no longer separates a known model, unknown rate and QQ check.")
    normalized_critical = " ".join(critical_prompt.split()).casefold()
    if not all(
        token in normalized_critical
        for token in ("vrućoj ruci", "općenite tvrdnje", "ispravka mjere", "@gilovich1985", "@miller2018")
    ):
        errors.append("Unit 07 critical prompt no longer preserves the bounded hot-hand evidence comparison.")
    normalized_revision = " ".join(revision_prompt.split()).casefold()
    if (
        "označite račun koji vrijedi samo uz neovisnost" not in normalized_revision
        or "izdvojite rečenicu" not in normalized_revision
        or any(phrase in normalized_revision for phrase in ("napišite kod", "popravite kod", "prepišite kod"))
    ):
        errors.append("Unit 07 model revision must assess code reading without code production.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 07 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    expected_error_id = "separate-posts-assumed-independent-without-justification"
    if planted_ids != {expected_error_id}:
        errors.append(
            "Unit 07 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_applicable = {"callout_greska", "racunski", "revizija_modela"}
    if numerical_applicable != expected_applicable:
        errors.append(f"Unit 07 numerical applicability mismatch: {sorted(numerical_applicable)}")

    complement_tokens = ["0,0960792032", "9,6 %", "neovis"]
    for task_class in ("callout_greska", "revizija_modela"):
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        missing_tokens = [token for token in complement_tokens if token not in result.casefold()]
        if missing_tokens:
            errors.append(
                f"Unit 07 {task_class} numerical result lacks recomputed tokens: {missing_tokens}"
            )
    callout_result = str(
        by_class["callout_greska"]["answer_components"]["numerical_check"]["expected_result"]
    )
    if "9,60792032 %" not in callout_result:
        errors.append("Unit 07 callout numerical result lacks the exact percentage before rounding.")
    revision_result = str(
        by_class["revizija_modela"]["answer_components"]["numerical_check"]["expected_result"]
    )
    if "0,9039207968" not in revision_result:
        errors.append("Unit 07 revision numerical result lacks the exact no-success probability.")
    numerical_result = str(
        by_class["racunski"]["answer_components"]["numerical_check"]["expected_result"]
    )
    numerical_tokens = ["90/100", "90 %", "90/585", "15,4 %", "100/10.000", "1 %", "10 ", "9.405"]
    missing_numerical = [token for token in numerical_tokens if token not in numerical_result]
    if missing_numerical:
        errors.append(f"Unit 07 numerical answer lacks recomputed verifier tokens: {missing_numerical}")

    evidence = {
        "complement": f"{no_success}/{at_least_one}/{at_least_one_percent}%",
        "verifier_counts": f"{total}/{targets}/{true_alerts}/{false_alerts}/{all_alerts}/{missed_targets}/{true_negatives}",
        "verifier_rates": f"{sensitivity:.4f}/{precision:.6f}/{base_rate:.4f}",
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "chapter-03-rendered-inline-counts-and-unit-07-callout-hand-calculation-no-code",
    }
    return errors, evidence


def unit_08_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 08 weighted estimates and verify the two-level error."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-08-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-08-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-08-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-08-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-08-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 08 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 08 {label} prompt is empty.")

    source_text = "\n".join(lines)
    probability_match = re.search(
        r"vjerojatnost_ukljucivanja\s*=\s*c\(\s*"
        r"rep\((\d+(?:\.\d+)?),\s*(\d+)\),\s*"
        r"rep\((\d+(?:\.\d+)?),\s*(\d+)\)\s*\)",
        source_text,
    )
    response_match = re.search(r"odgovor\s*=\s*c\(([^)]+)\)", source_text)
    if not probability_match or not response_match:
        return errors + ["Unit 08 synthetic weighting rows could not be parsed independently."], {}

    p_first, n_first, p_second, n_second = probability_match.groups()
    probabilities = (
        [Decimal(p_first)] * int(n_first)
        + [Decimal(p_second)] * int(n_second)
    )
    try:
        responses = [
            Decimal(token.strip())
            for token in response_match.group(1).split(",")
        ]
    except Exception as exc:
        return errors + [f"Unit 08 synthetic responses are invalid: {exc}"], {}
    if len(probabilities) != len(responses):
        return errors + [
            "Unit 08 synthetic probability and response vectors have different lengths."
        ], {}

    weights = [Decimal("1") / probability for probability in probabilities]
    unweighted_numerator = sum(responses, Decimal("0"))
    unweighted_denominator = Decimal(len(responses))
    unweighted_estimate = unweighted_numerator / unweighted_denominator
    weighted_numerator = sum(
        (weight * response for weight, response in zip(weights, responses)),
        Decimal("0"),
    )
    weighted_denominator = sum(weights, Decimal("0"))
    weighted_estimate = weighted_numerator / weighted_denominator
    shift_pp = Decimal("100") * (weighted_estimate - unweighted_estimate)

    expected_values = (
        Decimal("3"),
        Decimal("6"),
        Decimal("0.5"),
        Decimal("6"),
        Decimal("16"),
        Decimal("0.375"),
        Decimal("-12.5"),
    )
    observed_values = (
        unweighted_numerator,
        unweighted_denominator,
        unweighted_estimate,
        weighted_numerator,
        weighted_denominator,
        weighted_estimate,
        shift_pp,
    )
    if observed_values != expected_values:
        errors.append(
            f"Unit 08 weighted estimates drifted: {observed_values} != {expected_values}"
        )

    normalized_callout = " ".join(callout_prompt.split()).casefold()
    required_callout_tokens = (
        "veći nasumični uzorak",
        "užu distribuciju uzoračkih sredina",
        "standardna pogreška manja",
        "vrijednosti pojedinaca",
        "međusobno sličnije",
    )
    if not all(token in normalized_callout for token in required_callout_tokens):
        errors.append("Unit 08 callout no longer exposes the complete two-level variation error.")

    normalized_conceptual = " ".join(conceptual_prompt.split()).casefold()
    if not all(
        token in normalized_conceptual
        for token in (
            "raspodjelu pojedinačnih opažanja",
            "distribucije uzoračkih sredina",
            "što joj je jedinica",
            "što mjeri njezina širina",
            "kada uzorak naraste",
            "skicu obiju raspodjela",
        )
    ):
        errors.append("Unit 08 conceptual prompt no longer requires both units, widths and n effects.")

    normalized_numerical = " ".join(numerical_prompt.split()).casefold()
    required_numerical_tokens = (
        "sintetičke konačne populacije",
        "bez programa",
        "brojnik, nazivnik i postotak prvo bez težina",
        "s težinama uzorkovanja",
        "zašto se procjena pomaknula prema dolje",
        "jednu pogrešku koju taj pomak ne može ispraviti",
        "neobvezna nadogradnja",
        "ess mikropodaci i rezultat te provjere nisu dio knjige ni obveznoga zadatka",
    )
    if not all(token in normalized_numerical for token in required_numerical_tokens):
        errors.append("Unit 08 numerical prompt no longer preserves the hand calculation and optional ESS boundary.")

    normalized_critical = " ".join(critical_prompt.split()).casefold()
    if not all(
        token in normalized_critical
        for token in (
            "literary digest",
            "[@squire1988]",
            "što je iz prikazanoga slučaja poznato, a što nije",
            "pogrešku pokrivenosti i neodgovor",
            "slučajne promjenjivosti",
            "ne dopunjujte nepoznata polja pretpostavkama",
        )
    ):
        errors.append("Unit 08 critical prompt no longer preserves the evidence-bounded survey audit.")

    normalized_revision = " ".join(revision_prompt.split()).casefold()
    if (
        "tvrdnju koja je točna" not in normalized_revision
        or "zamjenu dviju razina varijabilnosti" not in normalized_revision
        or "ispravljenu verziju druge rečenice" not in normalized_revision
        or any(
            phrase in normalized_revision
            for phrase in ("napišite kod", "popravite kod", "prepišite kod")
        )
    ):
        errors.append("Unit 08 model revision must diagnose and repair the two-level error without code production.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 08 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    expected_error_id = "smaller-standard-error-implies-smaller-individual-variation"
    if planted_ids != {expected_error_id}:
        errors.append(
            "Unit 08 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    if numerical_applicable != {"racunski"}:
        errors.append(f"Unit 08 numerical applicability mismatch: {sorted(numerical_applicable)}")

    numerical_result = str(
        by_class["racunski"]["answer_components"]["numerical_check"]["expected_result"]
    )
    numerical_tokens = ["3/6", "50 %", "6/16", "37,5 %", "-12,5 postotnih bodova"]
    missing_numerical = [token for token in numerical_tokens if token not in numerical_result]
    if missing_numerical:
        errors.append(f"Unit 08 numerical answer lacks recomputed weighting tokens: {missing_numerical}")
    if "ess" in numerical_result.casefold():
        errors.append("Unit 08 canonical numerical answer must not depend on optional ESS microdata.")

    evidence = {
        "unweighted": (
            f"{unweighted_numerator}/{unweighted_denominator}/{unweighted_estimate:.4f}"
        ),
        "weighted": (
            f"{weighted_numerator}/{weighted_denominator}/{weighted_estimate:.4f}"
        ),
        "shift_pp": f"{shift_pp:.4f}",
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "rendered-synthetic-weight-table-and-hand-calculation-no-code-or-ess",
    }
    return errors, evidence


def unit_09_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
    analytical_path: Path,
    aggregate_path: Path,
    chapter_03_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 09 interval, aggregate and reach-back quantities."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-09-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-09-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-09-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-09-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-09-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 09 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 09 {label} prompt is empty.")

    preset_parameters = {
        "A": (40, 1.960),
        "B": (40, 2.576),
        "C": (160, 1.960),
    }
    widths = {
        label: 2 * critical / math.sqrt(sample_size)
        for label, (sample_size, critical) in preset_parameters.items()
    }
    expected_widths = {
        "A": 0.6198064213930023,
        "B": 0.8146027252593745,
        "C": 0.3099032106965012,
    }
    for label in preset_parameters:
        if not math.isclose(widths[label], expected_widths[label], rel_tol=0, abs_tol=1e-12):
            errors.append(
                f"Unit 09 preset {label} width drifted: {widths[label]} != {expected_widths[label]}"
            )

    source_text = "\n".join(lines)
    for source_token in (
        "set.seed(919)",
        "matrix(rnorm(50 * 160)",
        's9_preset("A", 40, 1.960, "95 %")',
        's9_preset("B", 40, 2.576, "99 %")',
        's9_preset("C", 160, 1.960, "95 %")',
        '"data/populacija-medija-agregat.csv"',
    ):
        if source_token not in source_text:
            errors.append(f"Unit 09 source no longer exposes required numerical contract: {source_token}")

    try:
        with analytical_path.open(encoding="utf-8", newline="") as handle:
            analytical_rows = list(csv.DictReader(handle))
        with aggregate_path.open(encoding="utf-8", newline="") as handle:
            aggregate_rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        return errors + [f"Unit 09 data files could not be read independently: {exc}"], {}

    portal_rows = [row for row in analytical_rows if row.get("izvor_vijesti_sifra") == "1"]
    total_rows = len(analytical_rows)
    portal_count = len(portal_rows)
    try:
        trust_sum = sum(Decimal(row["povjerenje_medijima"]) for row in portal_rows)
    except (KeyError, ArithmeticError) as exc:
        return errors + [f"Unit 09 analytical trust values are invalid: {exc}"], {}
    portal_share = Decimal(portal_count) / Decimal(total_rows)
    portal_mean = trust_sum / Decimal(portal_count)

    expected_data = (
        50000,
        15101,
        Decimal("72101"),
        Decimal("0.30202"),
        Decimal("4.774584464604993"),
    )
    observed_data = (total_rows, portal_count, trust_sum, portal_share, portal_mean)
    if observed_data[:4] != expected_data[:4] or abs(portal_mean - expected_data[4]) > Decimal("1e-14"):
        errors.append(f"Unit 09 analytical values drifted: {observed_data} != {expected_data}")

    portal_aggregates = [row for row in aggregate_rows if row.get("izvor_vijesti_sifra") == "1"]
    if len(portal_aggregates) != 1:
        errors.append(f"Unit 09 aggregate portal row count is {len(portal_aggregates)}, expected 1.")
    else:
        aggregate = portal_aggregates[0]
        aggregate_values = (
            int(aggregate["broj"]),
            int(aggregate["ukupno"]),
            Decimal(aggregate["zbroj_povjerenja"]),
            Decimal(aggregate["udio"]),
            Decimal(aggregate["prosjek_povjerenja"]),
        )
        expected_aggregate = (
            portal_count,
            total_rows,
            trust_sum,
            portal_share,
            portal_mean,
        )
        if aggregate_values[:4] != expected_aggregate[:4] or abs(
            aggregate_values[4] - expected_aggregate[4]
        ) > Decimal("1e-14"):
            errors.append(
                f"Unit 09 analytical and aggregate portal values disagree: "
                f"{aggregate_values} != {expected_aggregate}"
            )

    estimate = 0.52
    sample_size = 1000
    selection_bias = 0.06
    margin = 1.96 * math.sqrt(estimate * (1 - estimate) / sample_size)
    lower = estimate - margin
    upper = estimate + margin
    target = estimate - selection_bias
    expected_reachback = (0.030965518887950193, 0.48903448111204983, 0.5509655188879502, 0.46)
    observed_reachback = (margin, lower, upper, target)
    if not all(
        math.isclose(observed, expected, rel_tol=0, abs_tol=1e-15)
        for observed, expected in zip(observed_reachback, expected_reachback)
    ):
        errors.append(f"Unit 09 Chapter 03 reach-back drifted: {observed_reachback}")

    try:
        chapter_03 = chapter_03_path.read_text(encoding="utf-8")
    except OSError as exc:
        return errors + [f"Unit 09 Chapter 03 reach-back source is unavailable: {exc}"], {}
    for token in (
        "const margina = 1.96 * Math.sqrt(",
        "const istina = procjena - pristranost;",
        '"n = 1 000, pristranost 6 bodova"',
        "Pristranost = c(0, 0, 0.06)",
        "#| label: fig-w03-print",
    ):
        if token not in chapter_03:
            errors.append(f"Unit 09 Chapter 03 reach-back contract is missing: {token}")

    normalized_callout = " ".join(callout_prompt.split()).casefold()
    if not all(
        token in normalized_callout
        for token in (
            "jednom vrijednošću po neovisno uzorkovanoj osobi",
            "replicate",
            "sample",
            "median",
            "quantile",
            "devedesetpetpostotna vjerojatnost",
            "fiksna populacijska vrijednost",
            "upravo ovog opaženog intervala",
        )
    ):
        errors.append("Unit 09 callout no longer exposes the complete fixed-parameter probability error.")

    normalized_conceptual = " ".join(conceptual_prompt.split()).casefold()
    if not all(
        token in normalized_conceptual
        for token in (
            "razina pouzdanosti pripada postupku",
            "što je u postupku slučajno, a što fiksno",
            "vjerojatnosti da parametar leži unutar zadanih granica",
            "bootstrap gotovih oznaka teksta",
            "nesigurnost pravila kodiranja",
            "predajte jedan odlomak",
        )
    ):
        errors.append("Unit 09 conceptual prompt no longer requires procedure, parameter and coding-uncertainty boundaries.")

    normalized_numerical = " ".join(numerical_prompt.split()).casefold()
    if not all(
        token in normalized_numerical
        for token in (
            "iz tiskane tablice s trima postavkama",
            "$2z^*/\\sqrt{n}$",
            "između postavki a i b",
            "između a i c",
            "data/populacija-medija.csv",
            "izvor_vijesti_sifra",
            "data/populacija-medija-agregat.csv",
            "pet reproduciranih vrijednosti",
            "ne pisanje koda",
        )
    ):
        errors.append("Unit 09 numerical prompt no longer preserves preset, file-reconciliation and no-code requirements.")

    normalized_critical = " ".join(critical_prompt.split()).casefold()
    if not all(
        token in normalized_critical
        for token in (
            "istraživač margine pogreške",
            "uzorkom od 1000 osoba bez pristranosti",
            "pristranošću od šest postotnih bodova",
            "oba pokazuju procjenu od 52 %",
            "ne može obuhvatiti pristranost odabira",
            "koji je izvor nesigurnosti unutar, a koji izvan intervala",
            "ispravljenu tvrdnju",
        )
    ):
        errors.append("Unit 09 critical prompt no longer preserves the Chapter 03 bias reach-back.")

    normalized_revision = " ".join(revision_prompt.split()).casefold()
    if (
        not all(
            token in normalized_revision
            for token in (
                "replicate",
                "sample",
                "median",
                "quantile",
                "jedinu pogrešnu rečenicu",
                "frekventistički ispravnu zamjenu",
                "zadržava razinu od 95 %",
                "kod ne treba prepisivati ni mijenjati",
            )
        )
        or any(phrase in normalized_revision for phrase in ("napišite kod", "popravite kod"))
    ):
        errors.append("Unit 09 model revision must map the trace and repair only the interpretation without code production.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 09 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    expected_error_id = "confidence-level-assigned-to-fixed-parameter-after-observed-interval"
    if planted_ids != {expected_error_id}:
        errors.append(
            "Unit 09 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    if numerical_applicable != {"racunski", "kriticki"}:
        errors.append(f"Unit 09 numerical applicability mismatch: {sorted(numerical_applicable)}")

    racunski_result = str(
        by_class["racunski"]["answer_components"]["numerical_check"]["expected_result"]
    )
    required_racunski_tokens = (
        "0,619806421393",
        "0,814602725259",
        "0,309903210697",
        "3 promašaja",
        "0 promašaja",
        "1 promašaj",
        "50000",
        "15101",
        "72101",
        "0,30202",
        "4,7745844646",
    )
    missing_racunski = [token for token in required_racunski_tokens if token not in racunski_result]
    if missing_racunski:
        errors.append(f"Unit 09 numerical answer lacks recomputed preset or aggregate tokens: {missing_racunski}")

    critical_result = str(
        by_class["kriticki"]["answer_components"]["numerical_check"]["expected_result"]
    )
    required_critical_tokens = (
        "0,0309655",
        "3,0966 postotnih bodova",
        "48,9034 %",
        "55,0966 %",
        "46 %",
    )
    missing_critical = [token for token in required_critical_tokens if token not in critical_result]
    if missing_critical:
        errors.append(f"Unit 09 critical answer lacks recomputed margin tokens: {missing_critical}")

    evidence = {
        "widths": "/".join(f"{label}-{widths[label]:.12f}" for label in ("A", "B", "C")),
        "misses": "A-3/B-0/C-1",
        "analytical": f"{total_rows}/{portal_count}/{trust_sum}/{portal_share}/{portal_mean:.10f}",
        "reachback": f"{100*margin:.10f}pp/{100*lower:.10f}-{100*upper:.10f}/{100*target:.4f}",
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "rendered-w09-preset-and-aggregate-tables-plus-w03-static-state-no-code",
    }
    return errors, evidence


def unit_10_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
    analytical_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 10 permutation, calibration and reporting quantities."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-10-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-10-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-10-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-10-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-10-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 10 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 10 {label} prompt is empty.")

    source_text = "\n".join(lines)
    for source_token in (
        "set.seed(1011)",
        "s10_n <- 300",
        "s10_nulte <- nulta_raspodjela",
        "4000)",
        "(sum(abs(nulte) >= abs(opazena)) + 1) / (length(nulte) + 1)",
        "set.seed(1012)",
        "s10_p_niz_nulta <- replicate(800",
        "nulte <- nulta_raspodjela(skupina, ishod, \"A\", \"B\", 300)",
        "#| label: tbl-stope-odbacivanja",
        "#| label: fig-w10-print",
    ):
        if source_token not in source_text:
            errors.append(f"Unit 10 source no longer exposes required numerical contract: {source_token}")

    try:
        with analytical_path.open(encoding="utf-8", newline="") as handle:
            analytical_rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        return errors + [f"Unit 10 analytical data could not be read independently: {exc}"], {}

    portal_rows = [row for row in analytical_rows if row.get("izvor_vijesti_sifra") == "1"]
    print_rows = [row for row in analytical_rows if row.get("izvor_vijesti_sifra") == "5"]
    try:
        portal_mean = sum(Decimal(row["povjerenje_medijima"]) for row in portal_rows) / Decimal(
            len(portal_rows)
        )
        print_mean = sum(Decimal(row["povjerenje_medijima"]) for row in print_rows) / Decimal(
            len(print_rows)
        )
    except (KeyError, ArithmeticError, ZeroDivisionError) as exc:
        return errors + [f"Unit 10 analytical trust values are invalid: {exc}"], {}
    population_difference = print_mean - portal_mean
    expected_population_difference = Decimal("0.743644165673070804881187577")
    if abs(population_difference - expected_population_difference) > Decimal("1e-15"):
        errors.append(
            f"Unit 10 population difference drifted: {population_difference} "
            f"!= {expected_population_difference}"
        )

    permutation_count = 4000
    extreme_count = 64
    corrected_p = Decimal(extreme_count + 1) / Decimal(permutation_count + 1)
    expected_p = Decimal("0.01624593851537115721069732567")
    if abs(corrected_p - expected_p) > Decimal("1e-27"):
        errors.append(f"Unit 10 corrected p-value drifted: {corrected_p} != {expected_p}")

    observed_difference = Decimal("0.640938989801461")
    lower = Decimal("0.174811193068577")
    upper = Decimal("1.10706678653434")
    null_sd = Decimal("0.255870611768815")
    empirical_boundary = Decimal("0.499607748476254")
    two_sigma = Decimal(2) * null_sd
    boundary_gap = abs(two_sigma - empirical_boundary)
    if abs((upper - lower) / Decimal(2) - (upper - observed_difference)) > Decimal("1e-14"):
        errors.append("Unit 10 observed interval is no longer symmetric around its estimate.")
    if two_sigma != Decimal("0.511741223537630"):
        errors.append(f"Unit 10 two-sigma boundary drifted: {two_sigma}")
    if boundary_gap != Decimal("0.012133475061376"):
        errors.append(f"Unit 10 empirical-boundary gap drifted: {boundary_gap}")

    calibration_rejections = 39
    calibration_repetitions = 800
    calibration_rate = Decimal(calibration_rejections) / Decimal(calibration_repetitions) * Decimal(100)
    if calibration_rate != Decimal("4.875"):
        errors.append(f"Unit 10 calibration rate drifted: {calibration_rate}")

    normalized_callout = " ".join(callout_prompt.split()).casefold()
    if not all(
        token in normalized_callout
        for token in (
            "nulti model pretpostavlja jednaku punu raspodjelu",
            "zasebne jedinice opažanja",
            "oznake smatraju zamjenjivima",
            "oznake su promatračke",
            "ne podupire uzročnu tvrdnju",
            "(b + 1) / (b + 1)",
            "vjerojatnost da između dviju skupina nema razlike",
        )
    ):
        errors.append("Unit 10 callout no longer exposes one complete reversed-conditional error.")

    normalized_conceptual = " ".join(conceptual_prompt.split()).casefold()
    if not all(
        token in normalized_conceptual
        for token in (
            "p-vrijednost nije vjerojatnost nulte hipoteze",
            "dvije rečenice koje se razlikuju samo po tome što je uvjet",
            "što zaključak",
            "podatak koji bi bio potreban",
        )
    ):
        errors.append("Unit 10 conceptual prompt no longer requires both conditionals and missing information.")

    normalized_numerical = " ".join(numerical_prompt.split()).casefold()
    if not all(
        token in normalized_numerical
        for token in (
            "sredinu nula i standardnu devijaciju",
            "dvije standardne devijacije udaljene od nule",
            "imenujte testnu statistiku",
            "postupak kojim je nulta raspodjela izgrađena",
            "dobrovoljnom poveznicom na jednom portalu",
            "koju tvrdnju o populaciji ni mala p-vrijednost ne bi mogla opravdati",
            "u html widgetu postavite stvarnu razliku na nulu",
            "u tiskanom ili dokumentnom izdanju",
            "prvoga retka tablice stopa odbacivanja",
        )
    ):
        errors.append("Unit 10 numerical prompt no longer preserves calculation, selection and print paths.")

    normalized_critical = " ".join(critical_prompt.split()).casefold()
    if not all(
        token in normalized_critical
        for token in (
            "strukovnom udruženju",
            "popis od dvadeset pet pogrešnih tumačenja",
            "jedno pravilo izvještavanja",
            "tko u glavnom primjeru snosi posljedice svake vrste pogreške",
            "referentnim oznakama ne dokazuje da su te oznake nepogrešive",
        )
    ):
        errors.append("Unit 10 critical prompt no longer preserves reporting, consequence and label audits.")

    normalized_revision = " ".join(revision_prompt.split()).casefold()
    if (
        not all(
            token in normalized_revision
            for token in (
                "analizu iz okvira o pogrešci",
                "korake koji su provedeni ispravno",
                "redak koda iz kojeg izlazi izvještajna brojka",
                "rečenicu koja iz nje ne slijedi",
                "njezinu ispravljenu inačicu",
            )
        )
        or any(phrase in normalized_revision for phrase in ("napišite kod", "popravite kod"))
    ):
        errors.append("Unit 10 model revision must diagnose the report without code production.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 10 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    expected_error_id = "p-value-interpreted-as-posterior-probability-of-null"
    if planted_ids != {expected_error_id}:
        errors.append(
            "Unit 10 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    if numerical_applicable != {"callout_greska", "racunski", "revizija_modela"}:
        errors.append(f"Unit 10 numerical applicability mismatch: {sorted(numerical_applicable)}")

    callout_result = str(
        by_class["callout_greska"]["answer_components"]["numerical_check"]["expected_result"]
    )
    for token in ("65/4001", "0,0162459385154", "0,6409389898", "0,1748111931", "1,1070667865"):
        if token not in callout_result:
            errors.append(f"Unit 10 callout answer lacks recomputed token: {token}")

    numerical_result = str(
        by_class["racunski"]["answer_components"]["numerical_check"]["expected_result"]
    )
    for token in ("0,255870611769", "0,511741223538", "0,499607748476", "0,0121334750614", "39/800", "4,875 %"):
        if token not in numerical_result:
            errors.append(f"Unit 10 numerical answer lacks recomputed token: {token}")

    revision_result = str(
        by_class["revizija_modela"]["answer_components"]["numerical_check"]["expected_result"]
    )
    for token in ("b = 64", "B = 4000", "65/4001", "0,0162459385154"):
        if token not in revision_result:
            errors.append(f"Unit 10 model-revision answer lacks recomputed token: {token}")

    evidence = {
        "population_truth": f"{print_mean:.10f}-{portal_mean:.10f}={population_difference:.12f}",
        "observed": f"{observed_difference}/{lower}-{upper}",
        "permutation": f"b-{extreme_count}/B-{permutation_count}/p-{corrected_p:.13f}",
        "null_shape": f"sd-{null_sd}/q95-{empirical_boundary}/two-sigma-{two_sigma}/gap-{boundary_gap}",
        "calibration": f"{calibration_rejections}/{calibration_repetitions}/{calibration_rate}%",
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "rendered-w10-calibration-table-and-static-widget-twin-no-code",
    }
    return errors, evidence


def unit_11_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
    analytical_path: Path,
    aggregate_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 11 effect-size, power and planning quantities."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-11-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-11-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-11-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-11-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-11-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 11 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 11 {label} prompt is empty.")

    source_text = "\n".join(lines)
    for source_token in (
        "set.seed(1111)",
        "s11_studija <- function(velicina, permutacija = 200)",
        "(b + 1) / (permutacija + 1)",
        "set.seed(1112)",
        "s11_male <- t(replicate(3000, s11_studija(60)))",
        "s11_ciljni_d <- 0.5 / 1.9",
        "s11_ciljni_n <- ceiling(power.t.test(",
        "#| label: fig-w11-print",
        "#| label: tbl-w11-print-agregat",
        "#| label: tbl-w11-print-snaga",
        "d_opazeni <- (mean(tisak) - mean(portal)) / sd_zdruzena",
        "power.t.test(n = 30, delta = d_opazeni, sd = 1,",
    ):
        if source_token not in source_text:
            errors.append(f"Unit 11 source no longer exposes required numerical contract: {source_token}")

    try:
        with analytical_path.open(encoding="utf-8", newline="") as handle:
            analytical_rows = list(csv.DictReader(handle))
        with aggregate_path.open(encoding="utf-8", newline="") as handle:
            aggregate_rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        return errors + [f"Unit 11 data could not be read independently: {exc}"], {}

    analytical_groups: dict[str, list[Decimal]] = {"portal": [], "tisak": []}
    code_to_group = {"1": "portal", "5": "tisak"}
    try:
        for row in analytical_rows:
            group = code_to_group.get(row.get("izvor_vijesti_sifra", ""))
            if group:
                analytical_groups[group].append(Decimal(row["povjerenje_medijima"]))
    except (KeyError, ArithmeticError) as exc:
        return errors + [f"Unit 11 analytical trust values are invalid: {exc}"], {}

    aggregate_by_group = {
        row.get("izvor_vijesti", ""): row
        for row in aggregate_rows
        if row.get("izvor_vijesti") in analytical_groups
    }
    expected_aggregate = {
        "portal": (15101, Decimal("72101"), Decimal("4.774584464604993")),
        "tisak": (4855, Decimal("26791"), Decimal("5.518228630278064")),
    }
    recomputed_means: dict[str, Decimal] = {}
    for group, (expected_count, expected_sum, stored_mean) in expected_aggregate.items():
        row = aggregate_by_group.get(group)
        if row is None:
            errors.append(f"Unit 11 aggregate lacks {group!r} row.")
            continue
        try:
            count = int(row["broj"])
            trust_sum = Decimal(row["zbroj_povjerenja"])
            aggregate_mean = Decimal(row["prosjek_povjerenja"])
        except (KeyError, ValueError, ArithmeticError) as exc:
            errors.append(f"Unit 11 aggregate {group!r} row is invalid: {exc}")
            continue
        analytical = analytical_groups[group]
        analytical_sum = sum(analytical, Decimal(0))
        recomputed_mean = trust_sum / Decimal(count)
        recomputed_means[group] = recomputed_mean
        if (count, trust_sum, aggregate_mean) != (expected_count, expected_sum, stored_mean):
            errors.append(
                f"Unit 11 aggregate {group!r} drifted: "
                f"{count}/{trust_sum}/{aggregate_mean}"
            )
        if count != len(analytical) or trust_sum != analytical_sum:
            errors.append(
                f"Unit 11 analytical/aggregate reconciliation failed for {group!r}: "
                f"{len(analytical)}/{analytical_sum} != {count}/{trust_sum}"
            )
        if abs(recomputed_mean - aggregate_mean) > Decimal("1e-15"):
            errors.append(
                f"Unit 11 stored mean drifted for {group!r}: "
                f"{aggregate_mean} != {recomputed_mean}"
            )

    if set(recomputed_means) != {"portal", "tisak"}:
        return errors + ["Unit 11 means could not be reconstructed for both groups."], {}

    mean_difference = recomputed_means["tisak"] - recomputed_means["portal"]
    expected_difference = Decimal("0.743644165673070804881187577")
    if abs(mean_difference - expected_difference) > Decimal("1e-15"):
        errors.append(f"Unit 11 mean difference drifted: {mean_difference} != {expected_difference}")

    portal_float = [float(value) for value in analytical_groups["portal"]]
    print_float = [float(value) for value in analytical_groups["tisak"]]

    def sample_variance(values: list[float]) -> float:
        mean_value = math.fsum(values) / len(values)
        return math.fsum((value - mean_value) ** 2 for value in values) / (len(values) - 1)

    portal_variance = sample_variance(portal_float)
    print_variance = sample_variance(print_float)
    pooled_sd = math.sqrt(
        ((len(portal_float) - 1) * portal_variance + (len(print_float) - 1) * print_variance)
        / (len(portal_float) + len(print_float) - 2)
    )
    standardized_difference = float(mean_difference) / pooled_sd
    if abs(pooled_sd - 1.9121848632846543) > 1e-12:
        errors.append(f"Unit 11 pooled standard deviation drifted: {pooled_sd}")
    if abs(standardized_difference - 0.3888976322067926) > 1e-12:
        errors.append(f"Unit 11 standardized difference drifted: {standardized_difference}")

    simulated_power = {40: 0.425, 80: 0.724, 160: 0.946, 300: 0.999}
    critical_z = 1.959963984540054

    def normal_cdf(value: float) -> float:
        return 0.5 * (1 + math.erf(value / math.sqrt(2)))

    analytical_power: dict[int, float] = {}
    for group_n, simulated in simulated_power.items():
        mean_z = 0.4 * math.sqrt(group_n / 2)
        exact = normal_cdf(-critical_z - mean_z) + 1 - normal_cdf(critical_z - mean_z)
        analytical_power[group_n] = exact
        if abs(simulated - exact) > 0.03:
            errors.append(
                f"Unit 11 printed power at n={group_n} is not within Monte Carlo tolerance: "
                f"{simulated} versus {exact}"
            )
    if not all(
        simulated_power[current] < simulated_power[following]
        for current, following in zip((40, 80, 160), (80, 160, 300))
    ):
        errors.append("Unit 11 printed power values are not strictly increasing with group size.")

    target_d = Decimal("0.5") / Decimal("1.9")
    expected_target_d = Decimal("0.2631578947368421052631578947")
    if abs(target_d - expected_target_d) > Decimal("1e-27"):
        errors.append(f"Unit 11 target standardized effect drifted: {target_d}")
    posthoc_power = Decimal("0.8438926")
    target_n_raw = Decimal("227.64002629604767")
    target_n_ceiling = 228

    normalized_callout = " ".join(callout_prompt.split()).casefold()
    if not all(
        token in normalized_callout
        for token in (
            "tridesetero ljudi po skupini",
            "delta = d_opazeni",
            "opažena razlika daje standardiziranu razliku oko 0,78",
            "snaga izračunata za tu vrijednost",
            "studija bila dovoljno velika",
            "procijenjenoj razlici može vjerovati",
        )
    ):
        errors.append("Unit 11 callout no longer exposes one complete observed-effect power error.")

    normalized_conceptual = " ".join(conceptual_prompt.split()).casefold()
    if not all(
        token in normalized_conceptual
        for token in (
            "podskup procjena koje su prešle prag",
            "prosjek svih procjena ostaje blizu istini",
            "korak u kojem nastaje iskrivljenje",
            "faktor ne smije prenijeti na svako područje",
        )
    ):
        errors.append("Unit 11 conceptual prompt no longer requires selection and transfer boundaries.")

    normalized_numerical = " ".join(numerical_prompt.split()).casefold()
    if not all(
        token in normalized_numerical
        for token in (
            "data/populacija-medija-agregat.csv",
            "podijelite zbroj povjerenja brojem osoba",
            "izračunajte razliku prosjeka",
            "pri 40, 80, 160 i 300",
            "u html-u upotrijebite widget",
            "u tiskanom izdanju tablicu",
            "veći uzorak istodobno sužava interval i povećava snagu",
            "ne mijenja unaprijed zadanu veličinu učinka",
            "ne pisanje koda",
        )
    ):
        errors.append("Unit 11 numerical prompt no longer preserves calculation, print and H10 paths.")

    normalized_critical = " ".join(critical_prompt.split()).casefold()
    if not all(
        token in normalized_critical
        for token in (
            "niska prosječna snaga nekog područja znači samo",
            "istraživanja propuštaju stvarne učinke",
            "kratku uredničku bilješku",
            "podatak koji bi vam trebao",
            "koliko je objavljena veličina učinka precijenjena",
        )
    ):
        errors.append("Unit 11 critical prompt no longer requires consequence and evidence judgments.")

    normalized_revision = " ".join(revision_prompt.split()).casefold()
    if (
        not all(
            token in normalized_revision
            for token in (
                "provjeru iz okvira o pogrešci",
                "što je u pozivu ispravno",
                "argument u kojem stoji kružnost",
                "redak koda u kojem ona ulazi u račun",
                "čime bi taj argument trebalo zamijeniti",
            )
        )
        or any(phrase in normalized_revision for phrase in ("napišite kod", "popravite kod"))
    ):
        errors.append("Unit 11 model revision must diagnose the input without code production.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 11 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    expected_error_id = "observed-effect-used-for-post-hoc-power"
    if planted_ids != {expected_error_id}:
        errors.append(
            "Unit 11 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    if numerical_applicable != {"callout_greska", "racunski", "revizija_modela"}:
        errors.append(f"Unit 11 numerical applicability mismatch: {sorted(numerical_applicable)}")

    for task_class in ("callout_greska", "revizija_modela"):
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        for token in ("0,8438926", "0,2631578947", "227,6400263", "228"):
            if token not in result:
                errors.append(f"Unit 11 {task_class} answer lacks recomputed token: {token}")

    numerical_result = str(
        by_class["racunski"]["answer_components"]["numerical_check"]["expected_result"]
    )
    for token in (
        "72101/15101",
        "4,774584464604993",
        "26791/4855",
        "5,518228630278064",
        "0,743644165673071",
        "42,5 %",
        "72,4 %",
        "94,6 %",
        "99,9 %",
    ):
        if token not in numerical_result:
            errors.append(f"Unit 11 numerical answer lacks recomputed token: {token}")

    evidence = {
        "aggregate": (
            f"portal-72101/15101/{recomputed_means['portal']:.15f}-"
            f"tisak-26791/4855/{recomputed_means['tisak']:.15f}-"
            f"gap-{mean_difference:.15f}"
        ),
        "effect": f"pooled-sd-{pooled_sd:.12f}/d-{standardized_difference:.12f}",
        "power_print": "/".join(f"{group_n}-{100*value:.1f}%" for group_n, value in simulated_power.items()),
        "power_analytic": "/".join(
            f"{group_n}-{100*value:.4f}%" for group_n, value in analytical_power.items()
        ),
        "posthoc": f"d-0.78/n-30/power-{posthoc_power}",
        "target": f"raw-d-{target_d:.12f}/n-{target_n_raw}/ceiling-{target_n_ceiling}",
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "rendered-w11-aggregate-and-power-preset-tables-no-code",
    }
    return errors, evidence


def unit_12_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
    rrr_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 12 RRR, multiplicity and planted-error quantities."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-12-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-12-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-12-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-12-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-12-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 12 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 12 {label} prompt is empty.")

    source_text = "\n".join(lines)
    for source_token in (
        'w12_rrr <- read.csv(',
        '"notes/reports/p3-evidence12-rrr-lab-effects.csv"',
        "#| label: fig-rrr-forest",
        "#| label: fig-w12",
        "#| label: fig-w12-print",
        "#| label: tbl-rrr-laboratoriji",
        "set.seed(1212)",
        "0.05 / 12",
        "stopifnot(nrow(rrr) == 17, sum(rrr$n_total) == 1894)",
        'procjena <- c(0.026766, 0.014151)',
        'donja <- c(-0.107693, -0.076191)',
        'gornja <- c(0.161225, 0.104493)',
    ):
        if source_token not in source_text:
            errors.append(f"Unit 12 source no longer exposes required numerical contract: {source_token}")

    try:
        with rrr_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        return errors + [f"Unit 12 RRR artifact could not be read independently: {exc}"], {}

    try:
        study_order = [int(row["study_order"]) for row in rows]
        labs = [row["lab"] for row in rows]
        total_n = sum(int(row["n_total"]) for row in rows)
        raw_effects = [float(row["raw_mean_difference"]) for row in rows]
        raw_ses = [float(row["raw_se"]) for row in rows]
        raw_lows = [float(row["raw_ci_low"]) for row in rows]
        raw_highs = [float(row["raw_ci_high"]) for row in rows]
        d_effects = [float(row["cohen_d"]) for row in rows]
        d_ses = [float(row["d_se"]) for row in rows]
    except (KeyError, ValueError, ArithmeticError) as exc:
        return errors + [f"Unit 12 RRR artifact contains invalid values: {exc}"], {}

    if len(rows) != 17 or study_order != list(range(1, 18)) or len(set(labs)) != 17:
        errors.append(
            f"Unit 12 RRR laboratory identity drifted: rows={len(rows)} "
            f"orders={study_order} unique_labs={len(set(labs))}"
        )
    if total_n != 1894:
        errors.append(f"Unit 12 RRR participant total drifted: {total_n} != 1894")

    positive_points = sum(effect > 0 for effect in raw_effects)
    positive_intervals = sum(low > 0 for low in raw_lows)
    includes_original = sum(low <= 0.82 <= high for low, high in zip(raw_lows, raw_highs))
    positive_share = positive_points / len(rows) if rows else math.nan
    if (positive_points, positive_intervals, includes_original) != (9, 0, 2):
        errors.append(
            "Unit 12 RRR point/interval counts drifted: "
            f"{positive_points}/{positive_intervals}/{includes_original} != 9/0/2"
        )
    if abs(positive_share - 9 / 17) > 1e-15:
        errors.append(f"Unit 12 positive-point share drifted: {positive_share}")

    critical_z = 1.959963984540054

    def inverse_variance_summary(effects: list[float], standard_errors: list[float]) -> tuple[float, float, float]:
        weights = [1 / standard_error**2 for standard_error in standard_errors]
        estimate = math.fsum(weight * effect for weight, effect in zip(weights, effects)) / math.fsum(weights)
        summary_se = math.sqrt(1 / math.fsum(weights))
        return estimate, estimate - critical_z * summary_se, estimate + critical_z * summary_se

    raw_summary = inverse_variance_summary(raw_effects, raw_ses)
    d_summary = inverse_variance_summary(d_effects, d_ses)
    expected_raw = (0.026766, -0.107693, 0.161225)
    expected_d = (0.014151, -0.076191, 0.104493)
    for label, observed, expected in (
        ("raw", raw_summary, expected_raw),
        ("standardized", d_summary, expected_d),
    ):
        for component, actual, target in zip(("estimate", "low", "high"), observed, expected):
            if abs(actual - target) > 1e-6:
                errors.append(
                    f"Unit 12 {label} {component} drifted: {actual:.9f} != {target:.6f}"
                )

    path_count = 12
    nominal_family_rate = 1 - (1 - 0.05) ** path_count
    corrected_threshold = 0.05 / path_count
    corrected_family_rate = 1 - (1 - corrected_threshold) ** path_count
    if abs(nominal_family_rate - 0.45963991233736334) > 1e-15:
        errors.append(f"Unit 12 nominal multiplicity probability drifted: {nominal_family_rate}")
    if abs(corrected_family_rate - 0.04886993281129881) > 1e-15:
        errors.append(f"Unit 12 corrected multiplicity probability drifted: {corrected_family_rate}")

    normalized_callout = " ".join(callout_prompt.split()).casefold()
    if not all(
        token in normalized_callout
        for token in (
            "unaprijed naveo glavni ishod",
            "objedinjena sirova razlika iznosi 0,03 boda",
            "interval od −0,11 do 0,16",
            "budući da je analiza predregistrirana",
            "zaključak nužno valjan",
        )
    ):
        errors.append("Unit 12 callout no longer exposes one complete preregistration-validity error.")

    normalized_conceptual = " ".join(conceptual_prompt.split()).casefold()
    if not all(
        token in normalized_conceptual
        for token in (
            "pet pravila isključivanja",
            "vrt račvajućih putova",
            "trag postupka",
            "analitička fleksibilnost",
            "reproducibilnost",
            "replikacije koja bi prikupila nove podatke",
        )
    ):
        errors.append("Unit 12 conceptual prompt no longer distinguishes mechanisms, traces and replication.")

    normalized_numerical = " ".join(numerical_prompt.split()).casefold()
    if not all(
        token in normalized_numerical
        for token in (
            "tiskanu tablicu laboratorijskih procjena",
            "bez pisanja koda",
            "17 točkastih procjena",
            "udio u postocima",
            "u cijelosti iznad nule",
            "obuhvaća izvornu procjenu 0,82",
            "nije stopa „uspjelih replikacija”",
        )
    ):
        errors.append("Unit 12 numerical prompt no longer preserves counts, interpretation and print/H10 path.")

    normalized_critical = " ".join(critical_prompt.split()).casefold()
    if not all(
        token in normalized_critical
        for token in (
            "dokazano da učinak ne postoji",
            "objedinjenu procjenu s intervalom",
            "što nula u prikazu znači",
            "standardiziranu analizu osjetljivosti",
            "populacijsku ili kontekstualnu granicu",
            "publikacijska pristranost",
        )
    ):
        errors.append("Unit 12 critical prompt no longer requires interval, sensitivity and selection judgments.")

    normalized_revision = " ".join(revision_prompt.split()).casefold()
    if (
        not all(
            token in normalized_revision
            for token in (
                "zapis s četiri polja",
                "provjerene brojke",
                "jedinu pogrešnu tvrdnju",
                "ispravljeni zaključak",
                "dokument ili redak postupka",
                "ne traži se novi kod",
            )
        )
        or any(phrase in normalized_revision for phrase in ("napišite kod", "popravite kod"))
    ):
        errors.append("Unit 12 model revision must diagnose one claim and name evidence without code production.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 12 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    expected_error_id = "preregistration-treated-as-validity-guarantee"
    if planted_ids != {expected_error_id}:
        errors.append(
            "Unit 12 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_numerical = {"callout_greska", "racunski", "kriticki", "revizija_modela"}
    if numerical_applicable != expected_numerical:
        errors.append(f"Unit 12 numerical applicability mismatch: {sorted(numerical_applicable)}")

    for task_class in ("callout_greska", "revizija_modela"):
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        for token in ("17", "1.894", "0,026766", "−0,107693", "0,161225"):
            if token not in result:
                errors.append(f"Unit 12 {task_class} answer lacks recomputed token: {token}")

    numerical_result = str(by_class["racunski"]["answer_components"]["numerical_check"]["expected_result"])
    for token in ("9/17", "0,5294117647", "52,9 %", "jest 0", "jest 2"):
        if token not in numerical_result:
            errors.append(f"Unit 12 numerical answer lacks recomputed token: {token}")

    critical_result = str(by_class["kriticki"]["answer_components"]["numerical_check"]["expected_result"])
    for token in (
        "0,026766",
        "−0,107693",
        "0,161225",
        "0,014151",
        "−0,076191",
        "0,104493",
    ):
        if token not in critical_result:
            errors.append(f"Unit 12 critical answer lacks recomputed token: {token}")

    evidence = {
        "rrr": f"labs-{len(rows)}/n-{total_n}",
        "counts": (
            f"positive-{positive_points}/{len(rows)}/{100*positive_share:.4f}%-"
            f"strict-positive-ci-{positive_intervals}/includes-0.82-{includes_original}"
        ),
        "raw": f"{raw_summary[0]:.6f}/[{raw_summary[1]:.6f},{raw_summary[2]:.6f}]",
        "standardized": f"{d_summary[0]:.6f}/[{d_summary[1]:.6f},{d_summary[2]:.6f}]",
        "multiplicity": (
            f"m-12/nominal-{100*nominal_family_rate:.4f}%/"
            f"threshold-{corrected_threshold:.12f}/corrected-{100*corrected_family_rate:.4f}%"
        ),
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "rendered-w12-laboratory-table-and-static-widget-twin-no-code",
    }
    return errors, evidence


def unit_13_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 13 contingency-table closure and planted-error boundaries."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-13-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-13-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-13-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-13-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-13-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 13 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 13 {label} prompt is empty.")

    source_text = "\n".join(lines)
    for source_token in (
        "set.seed(1313)",
        "s13_tablica <- table(",
        "s13_rez <- s13_test$stdres",
        "s13_v <- sqrt(",
        "#| label: fig-w13",
        "#| label: fig-w13-print",
        "#ex-13-callout-greska-01",
        "#ex-13-konceptualni-01",
        "#ex-13-racunski-01",
        "#ex-13-kriticki-01",
        "#ex-13-revizija-modela-01",
    ):
        if source_token not in source_text:
            errors.append(f"Unit 13 source no longer exposes required assessment contract: {source_token}")

    row_totals = (100, 100)
    column_totals = (120, 80)
    grand_total = sum(row_totals)
    expected = tuple(
        tuple(row_total * column_total / grand_total for column_total in column_totals)
        for row_total in row_totals
    )
    first_observed = 70
    observed = (
        (first_observed, row_totals[0] - first_observed),
        (column_totals[0] - first_observed, column_totals[1] - (row_totals[0] - first_observed)),
    )
    if tuple(map(sum, observed)) != row_totals:
        errors.append(f"Unit 13 observed row totals drifted: {observed}")
    if tuple(sum(row[column] for row in observed) for column in range(2)) != column_totals:
        errors.append(f"Unit 13 observed column totals drifted: {observed}")

    expected_target = ((60.0, 40.0), (60.0, 40.0))
    observed_target = ((70, 30), (50, 50))
    if expected != expected_target:
        errors.append(f"Unit 13 expected table drifted: {expected} != {expected_target}")
    if observed != observed_target:
        errors.append(f"Unit 13 observed table drifted: {observed} != {observed_target}")

    contributions = tuple(
        (observed[row][column] - expected[row][column]) ** 2 / expected[row][column]
        for row in range(2)
        for column in range(2)
    )
    chi_square = math.fsum(contributions)
    threshold = 3.84
    p_value_df1 = math.erfc(math.sqrt(chi_square / 2))
    cramer_v = math.sqrt(chi_square / grand_total)
    contribution_target = (5 / 3, 5 / 2, 5 / 3, 5 / 2)
    if any(abs(actual - target) > 1e-15 for actual, target in zip(contributions, contribution_target)):
        errors.append(f"Unit 13 cell contributions drifted: {contributions}")
    if abs(chi_square - 25 / 3) > 1e-15 or chi_square <= threshold:
        errors.append(f"Unit 13 chi-square comparison drifted: {chi_square} versus {threshold}")
    if abs(cramer_v - math.sqrt(1 / 24)) > 1e-15:
        errors.append(f"Unit 13 Cramer's V verification drifted: {cramer_v}")

    normalized_callout = " ".join(callout_prompt.split()).casefold()
    if not all(
        token in normalized_callout
        for token in (
            "očekivane frekvencije",
            "prilagođeni standardizirani reziduali",
            "značajan na razini ispod jedan promil",
            "veza između dobi i izvora vijesti vrlo je snažna",
        )
    ):
        errors.append("Unit 13 callout no longer exposes one complete p-value-as-strength error.")

    normalized_conceptual = " ".join(conceptual_prompt.split()).casefold()
    if not all(
        token in normalized_conceptual
        for token in (
            "testa nezavisnosti",
            "mjere jačine veze",
            "dvije rečenice",
            "što test kaže",
            "što v kaže",
        )
    ):
        errors.append("Unit 13 conceptual prompt no longer separates the test from effect strength.")

    normalized_numerical = " ".join(numerical_prompt.split()).casefold()
    if not all(
        token in normalized_numerical
        for token in (
            "dva retka s po sto ispitanika",
            "rubnim zbrojevima stodvadeset i osamdeset",
            "sve četiri očekivane frekvencije",
            "sa sedamdeset u prvoj ćeliji",
            "doprinos svake ćelije",
            "graničnom vrijednošću 3,84",
        )
    ):
        errors.append("Unit 13 numerical prompt no longer determines the complete 2x2 calculation.")

    normalized_critical = " ".join(critical_prompt.split()).casefold()
    if not all(
        token in normalized_critical
        for token in (
            "simpsonov paradoks",
            "berkeleyjev slučaj",
            "zbirnu tablicu spola i ishoda prijave",
            "skup odjelskih tablica",
            "razliku u sastavu prijava",
            "razlike u odlučivanju unutar odjela",
            "naziv varijable",
        )
    ):
        errors.append("Unit 13 critical prompt no longer requires aggregate and department-level schemes.")

    normalized_revision = " ".join(revision_prompt.split()).casefold()
    if not all(
        token in normalized_revision
        for token in (
            "dijagnostičke korake koji su provedeni ispravno",
            "jedan pogrešan zaključak",
            "koju bi veličinu izvještaj morao sadržavati",
        )
    ):
        errors.append("Unit 13 model revision no longer diagnoses one claim and names strength evidence.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 13 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    expected_error_id = "small-p-treated-as-strong-association"
    if planted_ids != {expected_error_id}:
        errors.append(
            "Unit 13 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    if numerical_applicable != {"racunski"}:
        errors.append(f"Unit 13 numerical applicability mismatch: {sorted(numerical_applicable)}")

    numerical_result = str(
        by_class["racunski"]["answer_components"]["numerical_check"]["expected_result"]
    )
    for token in (
        "[[60, 40], [60, 40]]",
        "[[70, 30], [50, 50]]",
        "1,666666666667",
        "2,5",
        "8,333333333333",
        "3,84",
        "jedan stupanj slobode",
    ):
        if token not in numerical_result:
            errors.append(f"Unit 13 numerical answer lacks recomputed token: {token}")

    evidence = {
        "expected": "60/40/60/40",
        "observed": "70/30/50/50",
        "contributions": "/".join(f"{value:.12f}" for value in contributions),
        "chi_square": f"{chi_square:.12f}>{threshold:.2f}",
        "p_value_df1": f"{p_value_df1:.12f}",
        "cramer_v": f"{cramer_v:.12f}",
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "source-embedded-2x2-margins-and-first-cell-no-code",
    }
    return errors, evidence


def unit_14_numerical_check(
    lines: list[str],
    records: list[dict[str, Any]],
    analytical_path: Path,
    aggregate_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Recompute unit 14 two-group claims, task answers and planted-error bounds."""
    errors: list[str] = []

    try:
        callout_prompt = canonical_prompt(lines, "ex-14-callout-greska-01")
        conceptual_prompt = canonical_prompt(lines, "ex-14-konceptualni-01")
        numerical_prompt = canonical_prompt(lines, "ex-14-racunski-01")
        critical_prompt = canonical_prompt(lines, "ex-14-kriticki-01")
        revision_prompt = canonical_prompt(lines, "ex-14-revizija-modela-01")
    except AssertionError as exc:
        return [f"Unit 14 prompt is unavailable: {exc}"], {}

    for label, prompt in (
        ("callout", callout_prompt),
        ("conceptual", conceptual_prompt),
        ("numerical", numerical_prompt),
        ("critical", critical_prompt),
        ("revision", revision_prompt),
    ):
        if not prompt.strip():
            errors.append(f"Unit 14 {label} prompt is empty.")

    source_text = "\n".join(lines)
    for source_token in (
        "set.seed(1414)",
        "slice_sample(n = 120)",
        "s14_welch <- t.test(s14_tv, s14_mreze)",
        "s14_model <- lm(povjerenje_medijima ~ izvor, data = dvije_skupine)",
        "set.seed(1415)",
        "s14_np <- 60",
        "s14_upareni <- t.test(s14_poslije, s14_prije, paired = TRUE)",
        "s14_kao_neovisni <- t.test(s14_poslije, s14_prije)",
        "s14_wilcoxon <- wilcox.test(s14_poslije, s14_prije, paired = TRUE)",
        "w14_par.sd * Math.sqrt(2 / w14_par.n)",
        "w14_par.sd * Math.sqrt(2 * (1 - korelacija) / w14_par.n)",
        "#| label: fig-w14",
        "#| label: fig-w14-print",
        "data/populacija-medija-agregat.csv",
        "#ex-14-callout-greska-01",
        "#ex-14-konceptualni-01",
        "#ex-14-racunski-01",
        "#ex-14-kriticki-01",
        "#ex-14-revizija-modela-01",
    ):
        if source_token not in source_text:
            errors.append(f"Unit 14 source no longer exposes required numerical contract: {source_token}")

    try:
        with analytical_path.open(encoding="utf-8", newline="") as handle:
            analytical_rows = list(csv.DictReader(handle))
        with aggregate_path.open(encoding="utf-8", newline="") as handle:
            aggregate_rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        return errors + [f"Unit 14 data could not be read independently: {exc}"], {}

    sampled_person_ids = (
        30471, 46889, 22647, 35627, 19019, 1181, 10746, 47263, 35626, 15485,
        6294, 39446, 20322, 38664, 4194, 42262, 44302, 37104, 32312, 24474,
        16309, 21421, 32668, 28807, 16014, 3018, 45151, 36272, 624, 956,
        3140, 21732, 36764, 28149, 308, 11309, 44960, 14251, 6150, 20691,
        12186, 24647, 2181, 39513, 4968, 41007, 32344, 16308, 3793, 43758,
        37188, 42529, 45594, 15090, 23642, 33477, 46262, 8718, 32546, 40995,
        34823, 45088, 22932, 9730, 18628, 29395, 12955, 15857, 5019, 26874,
        31916, 19814, 38891, 658, 7938, 43481, 30572, 2337, 44864, 1577,
        2438, 36635, 25005, 22885, 3293, 43171, 46320, 10022, 26130, 30427,
        29730, 25848, 7391, 3242, 737, 25583, 29286, 33452, 38097, 662,
        28631, 5952, 34793, 10684, 29469, 13233, 5525, 26484, 49775, 4995,
        47738, 49341, 15004, 4590, 9818, 31979, 23235, 24415, 22900, 31246,
    )
    if len(sampled_person_ids) != 120 or len(set(sampled_person_ids)) != 120:
        errors.append("Unit 14 fixed sample identifier receipt is not 120 unique persons.")

    row_by_person: dict[int, dict[str, str]] = {}
    try:
        for row in analytical_rows:
            row_by_person[int(row["osoba"])] = row
        sampled_rows = [row_by_person[person_id] for person_id in sampled_person_ids]
    except (KeyError, ValueError) as exc:
        return errors + [f"Unit 14 fixed sample could not be reconstructed: {exc}"], {}

    def sample_variance(values: list[float]) -> float:
        mean_value = math.fsum(values) / len(values)
        return math.fsum((value - mean_value) ** 2 for value in values) / (len(values) - 1)

    def beta_continued_fraction(a: float, b: float, x: float) -> float:
        max_iterations = 250
        epsilon = 3e-14
        tiny = 1e-300
        qab = a + b
        qap = a + 1.0
        qam = a - 1.0
        c = 1.0
        d = 1.0 - qab * x / qap
        if abs(d) < tiny:
            d = tiny
        d = 1.0 / d
        h = d
        for iteration in range(1, max_iterations + 1):
            twice = 2 * iteration
            aa = iteration * (b - iteration) * x / ((qam + twice) * (a + twice))
            d = 1.0 + aa * d
            if abs(d) < tiny:
                d = tiny
            c = 1.0 + aa / c
            if abs(c) < tiny:
                c = tiny
            d = 1.0 / d
            h *= d * c
            aa = -(a + iteration) * (qab + iteration) * x / (
                (a + twice) * (qap + twice)
            )
            d = 1.0 + aa * d
            if abs(d) < tiny:
                d = tiny
            c = 1.0 + aa / c
            if abs(c) < tiny:
                c = tiny
            d = 1.0 / d
            delta = d * c
            h *= delta
            if abs(delta - 1.0) < epsilon:
                return h
        raise AssertionError("Unit 14 incomplete-beta calculation did not converge.")

    def regularized_beta(x: float, a: float, b: float) -> float:
        if x <= 0:
            return 0.0
        if x >= 1:
            return 1.0
        factor = math.exp(
            math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
            + a * math.log(x) + b * math.log1p(-x)
        )
        if x < (a + 1.0) / (a + b + 2.0):
            return factor * beta_continued_fraction(a, b, x) / a
        return 1.0 - factor * beta_continued_fraction(b, a, 1.0 - x) / b

    def student_t_cdf(value: float, degrees_freedom: float) -> float:
        beta_value = regularized_beta(
            degrees_freedom / (degrees_freedom + value * value),
            degrees_freedom / 2.0,
            0.5,
        )
        return 1.0 - beta_value / 2.0 if value >= 0 else beta_value / 2.0

    def student_t_quantile(probability: float, degrees_freedom: float) -> float:
        lower = -16.0
        upper = 16.0
        for _ in range(120):
            midpoint = (lower + upper) / 2.0
            if student_t_cdf(midpoint, degrees_freedom) < probability:
                lower = midpoint
            else:
                upper = midpoint
        return (lower + upper) / 2.0

    def welch_summary(first: list[float], second: list[float]) -> dict[str, float]:
        first_mean = math.fsum(first) / len(first)
        second_mean = math.fsum(second) / len(second)
        first_variance = sample_variance(first)
        second_variance = sample_variance(second)
        difference = first_mean - second_mean
        standard_error = math.sqrt(
            first_variance / len(first) + second_variance / len(second)
        )
        degrees_freedom = (
            first_variance / len(first) + second_variance / len(second)
        ) ** 2 / (
            (first_variance / len(first)) ** 2 / (len(first) - 1)
            + (second_variance / len(second)) ** 2 / (len(second) - 1)
        )
        statistic = difference / standard_error
        critical = student_t_quantile(0.975, degrees_freedom)
        return {
            "first_mean": first_mean,
            "second_mean": second_mean,
            "first_variance": first_variance,
            "second_variance": second_variance,
            "difference": difference,
            "se": standard_error,
            "df": degrees_freedom,
            "t": statistic,
            "p": 2 * (1 - student_t_cdf(abs(statistic), degrees_freedom)),
            "lower": difference - critical * standard_error,
            "upper": difference + critical * standard_error,
        }

    sampled_groups: dict[str, list[float]] = {"networks": [], "tv": []}
    for row in sampled_rows:
        group = {"2": "networks", "3": "tv"}.get(row.get("izvor_vijesti_sifra", ""))
        if group is None:
            errors.append(f"Unit 14 sampled person has an unexpected news-source code: {row}")
            continue
        sampled_groups[group].append(float(row["povjerenje_medijima"]))

    main_welch = welch_summary(sampled_groups["tv"], sampled_groups["networks"])
    main_targets = {
        "first_mean": 5.7,
        "second_mean": 4.514285714285714,
        "first_variance": 4.214285714285714,
        "second_variance": 3.818633540372671,
        "difference": 1.185714285714286,
        "se": 0.372609208159600,
        "df": 102.471131550669,
        "t": 3.18219265586805,
        "p": 0.00193513804157212,
        "lower": 0.446686471420565,
        "upper": 1.92474210000801,
    }
    if (len(sampled_groups["networks"]), len(sampled_groups["tv"])) != (70, 50):
        errors.append(
            "Unit 14 sampled group sizes drifted: "
            f"{len(sampled_groups['networks'])}/{len(sampled_groups['tv'])}"
        )
    for key, target in main_targets.items():
        if abs(main_welch[key] - target) > 1e-12:
            errors.append(f"Unit 14 main Welch {key} drifted: {main_welch[key]} != {target}")

    pooled_variance = (
        (len(sampled_groups["tv"]) - 1) * main_welch["first_variance"]
        + (len(sampled_groups["networks"]) - 1) * main_welch["second_variance"]
    ) / (len(sampled_rows) - 2)
    pooled_sd = math.sqrt(pooled_variance)
    ols_df = len(sampled_rows) - 2
    ols_se = pooled_sd * math.sqrt(
        1 / len(sampled_groups["tv"]) + 1 / len(sampled_groups["networks"])
    )
    ols_t = main_welch["difference"] / ols_se
    ols_critical = student_t_quantile(0.975, ols_df)
    ols_p = 2 * (1 - student_t_cdf(abs(ols_t), ols_df))
    ols_lower = main_welch["difference"] - ols_critical * ols_se
    ols_upper = main_welch["difference"] + ols_critical * ols_se
    cohen_d = main_welch["difference"] / pooled_sd
    ols_targets = (0.369536997509771, 3.20864837270572, 0.0017174706905821,
                   0.453930424466036, 1.91749814696254, 0.594126231310689)
    ols_actual = (ols_se, ols_t, ols_p, ols_lower, ols_upper, cohen_d)
    if any(abs(actual - target) > 1e-12 for actual, target in zip(ols_actual, ols_targets)):
        errors.append(f"Unit 14 OLS/effect-size reconstruction drifted: {ols_actual}")

    population_groups: dict[str, list[dict[str, str]]] = {"networks": [], "tv": []}
    for row in analytical_rows:
        group = {"2": "networks", "3": "tv"}.get(row.get("izvor_vijesti_sifra", ""))
        if group:
            population_groups[group].append(row)

    def row_mean(rows: list[dict[str, str]], column: str) -> float:
        return math.fsum(float(row[column]) for row in rows) / len(rows)

    population_difference = (
        row_mean(population_groups["tv"], "povjerenje_medijima")
        - row_mean(population_groups["networks"], "povjerenje_medijima")
    )
    population_age_networks = row_mean(population_groups["networks"], "dob")
    population_age_tv = row_mean(population_groups["tv"], "dob")
    narrow_population = {
        group: [row for row in rows if 30 <= int(row["dob"]) <= 49]
        for group, rows in population_groups.items()
    }
    population_narrow_difference = (
        row_mean(narrow_population["tv"], "povjerenje_medijima")
        - row_mean(narrow_population["networks"], "povjerenje_medijima")
    )
    population_targets = (
        1.297259749249822,
        33.4296606368665,
        50.2448508358733,
        0.900295271035001,
    )
    population_actual = (
        population_difference,
        population_age_networks,
        population_age_tv,
        population_narrow_difference,
    )
    if any(abs(actual - target) > 1e-12 for actual, target in zip(population_actual, population_targets)):
        errors.append(f"Unit 14 population and sensitivity values drifted: {population_actual}")

    narrow_sample_rows = [row for row in sampled_rows if 30 <= int(row["dob"]) <= 49]
    narrow_tv = [
        float(row["povjerenje_medijima"])
        for row in narrow_sample_rows
        if row["izvor_vijesti_sifra"] == "3"
    ]
    narrow_networks = [
        float(row["povjerenje_medijima"])
        for row in narrow_sample_rows
        if row["izvor_vijesti_sifra"] == "2"
    ]
    narrow_welch = welch_summary(narrow_tv, narrow_networks)
    narrow_targets = (55, 0.770270270270270, -0.335616307974888, 1.87615684851543)
    narrow_actual = (
        len(narrow_sample_rows),
        narrow_welch["difference"],
        narrow_welch["lower"],
        narrow_welch["upper"],
    )
    if any(abs(float(actual) - float(target)) > 1e-12 for actual, target in zip(narrow_actual, narrow_targets)):
        errors.append(f"Unit 14 narrow-sample Welch values drifted: {narrow_actual}")

    aggregate_by_code = {
        row.get("izvor_vijesti_sifra", ""): row
        for row in aggregate_rows
        if row.get("izvor_vijesti_sifra") in {"2", "3"}
    }
    aggregate_expected = {
        "2": (13378, Decimal("54432"), Decimal("4.06876962176708")),
        "3": (10827, Decimal("58098"), Decimal("5.366029371016902")),
    }
    aggregate_means: dict[str, Decimal] = {}
    for code, (expected_count, expected_sum, expected_mean) in aggregate_expected.items():
        row = aggregate_by_code.get(code)
        if row is None:
            errors.append(f"Unit 14 aggregate lacks news-source code {code}.")
            continue
        count = int(row["broj"])
        total = Decimal(row["zbroj_povjerenja"])
        stored_mean = Decimal(row["prosjek_povjerenja"])
        recomputed_mean = total / Decimal(count)
        aggregate_means[code] = recomputed_mean
        analytical_sum = sum(
            (Decimal(row_value["povjerenje_medijima"]) for row_value in population_groups[
                "networks" if code == "2" else "tv"
            ]),
            Decimal(0),
        )
        if (count, total, stored_mean) != (expected_count, expected_sum, expected_mean):
            errors.append(f"Unit 14 aggregate code {code} drifted: {count}/{total}/{stored_mean}")
        if total != analytical_sum or count != len(population_groups["networks" if code == "2" else "tv"]):
            errors.append(f"Unit 14 aggregate/analytical reconciliation failed for code {code}.")
        if abs(recomputed_mean - stored_mean) > Decimal("1e-15"):
            errors.append(f"Unit 14 stored mean for code {code} drifted: {stored_mean}")

    if set(aggregate_means) != {"2", "3"}:
        return errors + ["Unit 14 aggregate means could not be reconstructed."], {}
    aggregate_difference = aggregate_means["3"] - aggregate_means["2"]
    aggregate_d_16 = aggregate_difference / Decimal("1.6")
    aggregate_d_32 = aggregate_difference / Decimal("3.2")
    aggregate_targets = (
        Decimal("1.297259749249822"),
        Decimal("0.810787343281139"),
        Decimal("0.405393671640569"),
    )
    aggregate_actual = (aggregate_difference, aggregate_d_16, aggregate_d_32)
    if any(abs(actual - target) > Decimal("1e-15") for actual, target in zip(aggregate_actual, aggregate_targets)):
        errors.append(f"Unit 14 aggregate task values drifted: {aggregate_actual}")

    paired_n = 60
    paired_correlation = 0.864746050662474
    paired_mean = 0.480290890185894
    paired_sd = 0.901343412520157
    paired_se = paired_sd / math.sqrt(paired_n)
    paired_df = paired_n - 1
    paired_t = paired_mean / paired_se
    paired_p = 2 * (1 - student_t_cdf(abs(paired_t), paired_df))
    paired_critical = student_t_quantile(0.975, paired_df)
    paired_lower = paired_mean - paired_critical * paired_se
    paired_upper = paired_mean + paired_critical * paired_se
    paired_d = paired_mean / paired_sd
    paired_targets = (
        0.116362934196811,
        4.12752474403535,
        0.000116826096963618,
        0.247449196677287,
        0.713132583694502,
        0.532861153156931,
    )
    paired_actual = (paired_se, paired_t, paired_p, paired_lower, paired_upper, paired_d)
    if any(abs(actual - target) > 1e-12 for actual, target in zip(paired_actual, paired_targets)):
        errors.append(f"Unit 14 paired reconstruction drifted: {paired_actual}")

    before_mean = 4.78142830282708
    after_mean = 5.26171919301298
    before_variance = 2.6251525432855
    after_variance = 3.19980332495503
    independent_difference = after_mean - before_mean
    independent_se = math.sqrt(before_variance / paired_n + after_variance / paired_n)
    independent_df = (before_variance / paired_n + after_variance / paired_n) ** 2 / (
        (before_variance / paired_n) ** 2 / (paired_n - 1)
        + (after_variance / paired_n) ** 2 / (paired_n - 1)
    )
    independent_t = independent_difference / independent_se
    independent_p = 2 * (1 - student_t_cdf(abs(independent_t), independent_df))
    independent_critical = student_t_quantile(0.975, independent_df)
    independent_lower = independent_difference - independent_critical * independent_se
    independent_upper = independent_difference + independent_critical * independent_se
    independent_targets = (
        0.311580804614163,
        116.86263878741,
        1.54146495250453,
        0.125907198174549,
        -0.136786144693963,
        1.09736792506575,
    )
    independent_actual = (
        independent_se,
        independent_df,
        independent_t,
        independent_p,
        independent_lower,
        independent_upper,
    )
    if any(abs(actual - target) > 1e-12 for actual, target in zip(independent_actual, independent_targets)):
        errors.append(f"Unit 14 independent-treatment-of-pairs values drifted: {independent_actual}")

    wilcoxon_statistic = 1391
    wilcoxon_mean = paired_n * (paired_n + 1) / 4
    wilcoxon_sd = math.sqrt(paired_n * (paired_n + 1) * (2 * paired_n + 1) / 24)
    wilcoxon_z = (wilcoxon_statistic - wilcoxon_mean - 0.5) / wilcoxon_sd
    wilcoxon_p = math.erfc(abs(wilcoxon_z) / math.sqrt(2))
    if abs(wilcoxon_p - 0.000464486906942119) > 1e-15:
        errors.append(f"Unit 14 Wilcoxon approximation drifted: {wilcoxon_p}")

    widget_independent_se = 10 * math.sqrt(2 / 50)
    widget_paired_se = 10 * math.sqrt(2 * (1 - 0.65) / 50)
    if widget_independent_se != 2 or abs(widget_paired_se - 1.18321595661992) > 1e-12:
        errors.append(
            "Unit 14 widget standard-error formulas drifted: "
            f"{widget_independent_se}/{widget_paired_se}"
        )

    normalized_callout = " ".join(callout_prompt.split()).casefold()
    if not all(
        token in normalized_callout
        for token in (
            "jedinica neovisnosti označena je kao osoba",
            "referentna skupina su društvene mreže",
            "welchov test ne traži jednake varijance",
            "od 30 do 49 godina",
            "interval razlike obuhvaća nulu",
            "nema veze s povjerenjem",
        )
    ):
        errors.append("Unit 14 callout no longer exposes one complete absence-from-nonsignificance error.")

    normalized_conceptual = " ".join(conceptual_prompt.split()).casefold()
    if not all(
        token in normalized_conceptual
        for token in (
            "tri istraživačke situacije",
            "jedinicu neovisnosti",
            "unaprijed zadanim pragom od pet bodova",
            "dvije skupine prema primarnom izvoru vijesti",
            "iste ispitanike prije i poslije kampanje",
        )
    ):
        errors.append("Unit 14 conceptual prompt no longer identifies all three designs.")

    normalized_numerical = " ".join(numerical_prompt.split()).casefold()
    if not all(
        token in normalized_numerical
        for token in (
            "data/populacija-medija-agregat.csv",
            "podijelite `zbroj_povjerenja` stupcem `broj`",
            "provjerite pohranjeni prosjek",
            "razliku aritmetičkih sredina",
            "standardne devijacije 1,6 pa 3,2",
            "standardiziranu razliku",
            "za rad bez datoteke upotrijebite izvadak",
        )
    ):
        errors.append("Unit 14 numerical prompt no longer preserves aggregate, print and H10 paths.")

    normalized_critical = " ".join(critical_prompt.split()).casefold()
    if not all(
        token in normalized_critical
        for token in (
            "što ljestvica povjerenja i kategorija izvora vijesti ne mjere",
            "bilo koja pozitivna razlika",
            "najmanje dva boda",
            "kratku bilješku recenzentu",
            "sama oznaka značajnosti",
            "problem mjerenja ni izbor praga",
        )
    ):
        errors.append("Unit 14 critical prompt no longer joins measurement and decision thresholds.")

    normalized_revision = " ".join(revision_prompt.split()).casefold()
    if not all(
        token in normalized_revision
        for token in (
            "imenujte referentnu skupinu",
            "što bi se promijenilo, a što ostalo isto",
            "jedinicu neovisnosti",
            "vrstu ishoda",
            "odnos prema varijancama",
            "doseg ciljne populacije",
            "jedinu tvrdnju koja iz rezultata ne slijedi",
            "rečenicu kojom bi je trebalo zamijeniti",
        )
    ):
        errors.append("Unit 14 model revision no longer requires the full audit and one replacement claim.")

    by_class = {record["task_class"]: record for record in records}
    planted_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["planted_error"]["applicable"]
    }
    if planted_applicable != {"callout_greska", "revizija_modela"}:
        errors.append(f"Unit 14 planted-error applicability mismatch: {sorted(planted_applicable)}")
    planted_ids = {
        by_class[task_class]["answer_components"]["planted_error"]["error_id"]
        for task_class in planted_applicable
    }
    expected_error_id = "nonsignificant-subgroup-treated-as-no-association"
    if planted_ids != {expected_error_id}:
        errors.append(
            "Unit 14 callout and model revision do not close one stable planted error: "
            f"{planted_ids}"
        )

    numerical_applicable = {
        task_class
        for task_class, record in by_class.items()
        if record["answer_components"]["numerical_check"]["applicable"]
    }
    expected_numerical = {"callout_greska", "racunski", "kriticki", "revizija_modela"}
    if numerical_applicable != expected_numerical:
        errors.append(f"Unit 14 numerical applicability mismatch: {sorted(numerical_applicable)}")

    required_result_tokens = {
        "callout_greska": ("55", "0,770270270270", "−0,335616307975", "1,876156848515", "0,900295271035"),
        "racunski": ("58098/10827", "5,366029371017", "54432/13378", "4,068769621767", "1,297259749250", "0,810787343281", "0,405393671641"),
        "kriticki": ("1,185714285714", "0,446686471421", "1,924742100008", "iznad 0", "ispod 2"),
        "revizija_modela": ("4,514285714286", "1,185714285714", "0,770270270270", "−0,335616307975", "1,876156848515"),
    }
    for task_class, tokens in required_result_tokens.items():
        result = str(by_class[task_class]["answer_components"]["numerical_check"]["expected_result"])
        for token in tokens:
            if token not in result:
                errors.append(f"Unit 14 {task_class} answer lacks recomputed token: {token}")

    evidence = {
        "sample": (
            f"n-120/groups-networks-{len(sampled_groups['networks'])}-tv-{len(sampled_groups['tv'])}/"
            f"means-{main_welch['second_mean']:.12f}-{main_welch['first_mean']:.12f}/"
            f"variances-{main_welch['second_variance']:.12f}-{main_welch['first_variance']:.12f}"
        ),
        "welch": (
            f"difference-{main_welch['difference']:.12f}/se-{main_welch['se']:.12f}/"
            f"df-{main_welch['df']:.12f}/t-{main_welch['t']:.12f}/p-{main_welch['p']:.15f}/"
            f"interval-{main_welch['lower']:.12f}-to-{main_welch['upper']:.12f}"
        ),
        "ols": (
            f"se-{ols_se:.12f}/df-{ols_df}/t-{ols_t:.12f}/p-{ols_p:.15f}/"
            f"interval-{ols_lower:.12f}-to-{ols_upper:.12f}/d-{cohen_d:.12f}"
        ),
        "paired": (
            f"n-{paired_n}/r-{paired_correlation:.12f}/mean-{paired_mean:.12f}/sd-{paired_sd:.12f}/"
            f"interval-{paired_lower:.12f}-to-{paired_upper:.12f}/p-{paired_p:.15f}/d-{paired_d:.12f}/"
            f"as-independent-{independent_lower:.12f}-to-{independent_upper:.12f}-p-{independent_p:.15f}/"
            f"wilcoxon-W-{wilcoxon_statistic}-p-{wilcoxon_p:.15f}"
        ),
        "population": (
            f"difference-{population_difference:.12f}/ages-{population_age_networks:.12f}-{population_age_tv:.12f}/"
            f"narrow-difference-{population_narrow_difference:.12f}/sample-narrow-n-{len(narrow_sample_rows)}/"
            f"sample-narrow-{narrow_welch['difference']:.12f}/"
            f"interval-{narrow_welch['lower']:.12f}-to-{narrow_welch['upper']:.12f}"
        ),
        "aggregate": (
            f"networks-54432/13378/{aggregate_means['2']:.15f}-"
            f"tv-58098/10827/{aggregate_means['3']:.15f}-"
            f"difference-{aggregate_difference:.15f}/d-{aggregate_d_16:.15f}-{aggregate_d_32:.15f}"
        ),
        "widget": f"se-independent-{widget_independent_se:.12f}/paired-{widget_paired_se:.12f}",
        "applicable_records": str(len(numerical_applicable)),
        "planted_error": next(iter(planted_ids), ""),
        "print_path": "rendered-aggregate-table-static-widget-and-source-values-no-code",
    }
    return errors, evidence


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
        record_paths = sorted(SOLUTION_RECORD_ROOT.glob("unit-*/*.json"))
        solution_records = [(path, load_json(path)) for path in record_paths]
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
    elif fixture == "invalid_solution_record":
        if solution_records:
            solution_records[0][1]["answer_components"].pop("planted_error", None)
        else:
            errors.append("The invalid_solution_record fixture requires at least one canonical record.")
    elif fixture == "protected_record_leak":
        pass
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
        solution_contract.get("records_authored_in_this_packet") is False,
        "The historical P2-ASSESS contract must still record that its architecture packet authored no records.",
    )
    check(
        inventory.get("solution_routes") == [],
        "Solution routes must remain empty until the separately governed P5-ROUTES packet.",
    )
    implementation = solution_contract.get("implementation_contract", {})
    check(
        implementation.get("settled_by_packet") == "P5-CLOSURE-00"
        and implementation.get("storage_root") == "assessment/solution-records"
        and implementation.get("file_layout") == "unit-<unit_id>/<record_id>.json"
        and implementation.get("one_schema_record_per_file") is True,
        "The P5-CLOSURE-00 canonical storage and one-record-per-file layout are incomplete.",
    )
    check(
        implementation.get("record_id_pattern")
        == solution_schema.get("properties", {}).get("record_id", {}).get("pattern")
        and implementation.get("exercise_id_pattern")
        == solution_schema.get("properties", {}).get("exercise_id", {}).get("pattern"),
        "Identifier patterns in the architecture and solution schema disagree.",
    )
    check(
        implementation.get("binding_packets")
        == ["P5-CLOSURE-00-through-P5-CLOSURE-18", "P5-ROUTES"]
        and "P5-ROUTES alone" in implementation.get("route_boundary", ""),
        "The first-unit implementation decisions must bind all later unit packets while reserving route assembly.",
    )
    prompt_contract_fixture = [
        "### Konceptualni {#ex-prompt-contract .zadaci-razina}",
        "Vidljivi prompt.",
        "",
        '::: {.content-visible when-profile="kolegij"}',
        "Zaštićeni ključ.",
        ":::",
        "",
        "### Sljedeći zadatak {.zadaci-razina}",
    ]
    check(
        canonical_prompt(prompt_contract_fixture, "ex-prompt-contract") == "Vidljivi prompt.\n",
        "Prompt fingerprint contract must exclude nested profile-only content under an anchored heading.",
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

    expected_task_classes = {
        "callout_greska",
        "konceptualni",
        "racunski",
        "kriticki",
        "revizija_modela",
    }
    task_slugs = {
        "callout_greska": "callout-greska",
        "konceptualni": "konceptualni",
        "racunski": "racunski",
        "kriticki": "kriticki",
        "revizija_modela": "revizija-modela",
    }
    records_by_unit: dict[str, list[dict[str, Any]]] = {}
    seen_record_ids: set[str] = set()
    seen_exercise_ids: set[str] = set()
    source_lines: dict[str, list[str]] = {}
    protected_strings: list[str] = []

    check(bool(solution_records), "At least one canonical solution record must exist from P5-CLOSURE-00 onward.")
    for path, record in solution_records:
        relative = path.relative_to(ROOT).as_posix()
        record_errors = validate_solution_schema(record, solution_schema, solution_schema, relative)
        errors.extend(record_errors)
        if record_errors:
            continue

        record_id = record["record_id"]
        exercise_id = record["exercise_id"]
        unit_id = record["unit_id"]
        task_class = record["task_class"]
        expected_record_id = "sol-" + exercise_id.removeprefix("ex-")
        expected_path = f"assessment/solution-records/unit-{unit_id}/{record_id}.json"
        check(relative == expected_path, f"Solution record file layout mismatch: {relative} != {expected_path}")
        check(record_id == expected_record_id, f"{relative}: record_id must derive exactly from exercise_id")
        check(record_id not in seen_record_ids, f"Duplicate canonical record_id: {record_id}")
        check(exercise_id not in seen_exercise_ids, f"Duplicate stable exercise_id: {exercise_id}")
        seen_record_ids.add(record_id)
        seen_exercise_ids.add(exercise_id)
        check(
            f"-{task_slugs[task_class]}-" in exercise_id,
            f"{relative}: exercise_id task slug disagrees with task_class",
        )
        check(
            record["source_anchor"]["anchor"] == exercise_id,
            f"{relative}: source anchor must equal the stable exercise_id",
        )
        check(
            record["visibility_contract"] == visibility.get("contract_id"),
            f"{relative}: record visibility contract disagrees with D06",
        )
        check(
            record["human_responsibility"]
            == {
                "judgment_owner": "student_or_submitting_author",
                "verification_required": True,
                "code_production_assessed": False,
            },
            f"{relative}: human-responsibility boundary is incomplete",
        )
        errors.extend(applicability_errors(record, relative))

        source_path = record["source_anchor"]["path"]
        if source_path not in source_lines:
            source = ROOT / source_path
            if not source.exists():
                errors.append(f"{relative}: missing bound source {source_path}")
                continue
            source_lines[source_path] = source.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n").splitlines()
        try:
            prompt = canonical_prompt(source_lines[source_path], exercise_id)
        except AssertionError as exc:
            errors.append(f"{relative}: {exc}")
        else:
            digest = "sha256:" + hashlib.sha256(prompt.encode("utf-8")).hexdigest()
            check(
                record["prompt_fingerprint"] == digest,
                f"{relative}: prompt fingerprint drift ({record['prompt_fingerprint']} != {digest})",
            )

        records_by_unit.setdefault(unit_id, []).append(record)
        protected_strings.extend(protected_record_strings(record))

    for unit_id, records in records_by_unit.items():
        classes = [record["task_class"] for record in records]
        check(
            len(records) == 5 and set(classes) == expected_task_classes and len(classes) == len(set(classes)),
            f"Unit {unit_id} must have exactly one record for callout-greska and each of the four Zadaci tiers.",
        )
    check(
        "00" in records_by_unit and len(records_by_unit["00"]) == 5,
        "P5-CLOSURE-00 must author exactly five canonical unit 00 records.",
    )
    unit_00_numerical: dict[str, str] = {}
    if (
        "00" in records_by_unit
        and len(records_by_unit["00"]) == 5
        and {record["task_class"] for record in records_by_unit["00"]} == expected_task_classes
        and "chapters/00-predgovor.qmd" in source_lines
    ):
        numerical_errors, unit_00_numerical = unit_00_numerical_check(
            source_lines["chapters/00-predgovor.qmd"], records_by_unit["00"]
        )
        errors.extend(numerical_errors)
    unit_01_numerical: dict[str, str] = {}
    if (
        "01" in records_by_unit
        and len(records_by_unit["01"]) == 5
        and {record["task_class"] for record in records_by_unit["01"]} == expected_task_classes
        and "chapters/01-zasto-statistika.qmd" in source_lines
    ):
        numerical_errors, unit_01_numerical = unit_01_numerical_check(
            source_lines["chapters/01-zasto-statistika.qmd"],
            records_by_unit["01"],
            ROOT / "data/populacija-medija-agregat.csv",
        )
        errors.extend(numerical_errors)
    unit_02_numerical: dict[str, str] = {}
    if (
        "02" in records_by_unit
        and len(records_by_unit["02"]) == 5
        and {record["task_class"] for record in records_by_unit["02"]} == expected_task_classes
        and "chapters/02-mjerenje-i-dizajn.qmd" in source_lines
    ):
        numerical_errors, unit_02_numerical = unit_02_numerical_check(
            source_lines["chapters/02-mjerenje-i-dizajn.qmd"],
            records_by_unit["02"],
        )
        errors.extend(numerical_errors)
    unit_03_numerical: dict[str, str] = {}
    if (
        "03" in records_by_unit
        and len(records_by_unit["03"]) == 5
        and {record["task_class"] for record in records_by_unit["03"]} == expected_task_classes
        and "chapters/03-kako-brojke-zavode.qmd" in source_lines
    ):
        numerical_errors, unit_03_numerical = unit_03_numerical_check(
            source_lines["chapters/03-kako-brojke-zavode.qmd"],
            records_by_unit["03"],
            ROOT / "data/populacija-medija-agregat.csv",
        )
        errors.extend(numerical_errors)
    unit_04_numerical: dict[str, str] = {}
    if (
        "04" in records_by_unit
        and len(records_by_unit["04"]) == 5
        and {record["task_class"] for record in records_by_unit["04"]} == expected_task_classes
        and "chapters/04-sazimanje-podataka.qmd" in source_lines
    ):
        numerical_errors, unit_04_numerical = unit_04_numerical_check(
            source_lines["chapters/04-sazimanje-podataka.qmd"],
            records_by_unit["04"],
            ROOT / "data/digikat-platforme-mjesecno.csv",
            ROOT / "data/digikat-platforme-godisnje.csv",
            ROOT / "data/anketa-mreze-agregat.csv",
            ROOT / "data/digikat-izvori.csv",
        )
        errors.extend(numerical_errors)
    unit_05_numerical: dict[str, str] = {}
    if (
        "05" in records_by_unit
        and len(records_by_unit["05"]) == 5
        and {record["task_class"] for record in records_by_unit["05"]} == expected_task_classes
        and "chapters/05-vizualizacija.qmd" in source_lines
    ):
        numerical_errors, unit_05_numerical = unit_05_numerical_check(
            source_lines["chapters/05-vizualizacija.qmd"],
            records_by_unit["05"],
            ROOT / "data/anketa-mreze-agregat.csv",
        )
        errors.extend(numerical_errors)
    unit_06_numerical: dict[str, str] = {}
    if (
        "06" in records_by_unit
        and len(records_by_unit["06"]) == 5
        and {record["task_class"] for record in records_by_unit["06"]} == expected_task_classes
        and "chapters/06-povezanost.qmd" in source_lines
    ):
        numerical_errors, unit_06_numerical = unit_06_numerical_check(
            source_lines["chapters/06-povezanost.qmd"],
            records_by_unit["06"],
            ROOT / "data/anketa-mreze.csv",
            ROOT / "data/eurostat-drustvo-2025.csv",
            ROOT / "data/widgets.json",
        )
        errors.extend(numerical_errors)
    unit_07_numerical: dict[str, str] = {}
    if (
        "07" in records_by_unit
        and len(records_by_unit["07"]) == 5
        and {record["task_class"] for record in records_by_unit["07"]} == expected_task_classes
        and "chapters/07-vjerojatnost.qmd" in source_lines
    ):
        numerical_errors, unit_07_numerical = unit_07_numerical_check(
            source_lines["chapters/07-vjerojatnost.qmd"],
            records_by_unit["07"],
            ROOT / "chapters/03-kako-brojke-zavode.qmd",
        )
        errors.extend(numerical_errors)
    unit_08_numerical: dict[str, str] = {}
    if (
        "08" in records_by_unit
        and len(records_by_unit["08"]) == 5
        and {record["task_class"] for record in records_by_unit["08"]} == expected_task_classes
        and "chapters/08-uzorkovanje.qmd" in source_lines
    ):
        numerical_errors, unit_08_numerical = unit_08_numerical_check(
            source_lines["chapters/08-uzorkovanje.qmd"],
            records_by_unit["08"],
        )
        errors.extend(numerical_errors)
    unit_09_numerical: dict[str, str] = {}
    if (
        "09" in records_by_unit
        and len(records_by_unit["09"]) == 5
        and {record["task_class"] for record in records_by_unit["09"]} == expected_task_classes
        and "chapters/09-procjena.qmd" in source_lines
    ):
        numerical_errors, unit_09_numerical = unit_09_numerical_check(
            source_lines["chapters/09-procjena.qmd"],
            records_by_unit["09"],
            ROOT / "data/populacija-medija.csv",
            ROOT / "data/populacija-medija-agregat.csv",
            ROOT / "chapters/03-kako-brojke-zavode.qmd",
        )
        errors.extend(numerical_errors)
    unit_10_numerical: dict[str, str] = {}
    if (
        "10" in records_by_unit
        and len(records_by_unit["10"]) == 5
        and {record["task_class"] for record in records_by_unit["10"]} == expected_task_classes
        and "chapters/10-logika-testiranja.qmd" in source_lines
    ):
        numerical_errors, unit_10_numerical = unit_10_numerical_check(
            source_lines["chapters/10-logika-testiranja.qmd"],
            records_by_unit["10"],
            ROOT / "data/populacija-medija.csv",
        )
        errors.extend(numerical_errors)
    unit_11_numerical: dict[str, str] = {}
    if (
        "11" in records_by_unit
        and len(records_by_unit["11"]) == 5
        and {record["task_class"] for record in records_by_unit["11"]} == expected_task_classes
        and "chapters/11-velicina-ucinka-i-snaga.qmd" in source_lines
    ):
        numerical_errors, unit_11_numerical = unit_11_numerical_check(
            source_lines["chapters/11-velicina-ucinka-i-snaga.qmd"],
            records_by_unit["11"],
            ROOT / "data/populacija-medija.csv",
            ROOT / "data/populacija-medija-agregat.csv",
        )
        errors.extend(numerical_errors)
    unit_12_numerical: dict[str, str] = {}
    if (
        "12" in records_by_unit
        and len(records_by_unit["12"]) == 5
        and {record["task_class"] for record in records_by_unit["12"]} == expected_task_classes
        and "chapters/12-kriza-i-obnova.qmd" in source_lines
    ):
        numerical_errors, unit_12_numerical = unit_12_numerical_check(
            source_lines["chapters/12-kriza-i-obnova.qmd"],
            records_by_unit["12"],
            ROOT / "notes/reports/p3-evidence12-rrr-lab-effects.csv",
        )
        errors.extend(numerical_errors)
    unit_13_numerical: dict[str, str] = {}
    if (
        "13" in records_by_unit
        and len(records_by_unit["13"]) == 5
        and {record["task_class"] for record in records_by_unit["13"]} == expected_task_classes
        and "chapters/13-kategoricki-podaci.qmd" in source_lines
    ):
        numerical_errors, unit_13_numerical = unit_13_numerical_check(
            source_lines["chapters/13-kategoricki-podaci.qmd"],
            records_by_unit["13"],
        )
        errors.extend(numerical_errors)
    unit_14_numerical: dict[str, str] = {}
    if (
        "14" in records_by_unit
        and len(records_by_unit["14"]) == 5
        and {record["task_class"] for record in records_by_unit["14"]} == expected_task_classes
        and "chapters/14-dvije-grupe.qmd" in source_lines
    ):
        numerical_errors, unit_14_numerical = unit_14_numerical_check(
            source_lines["chapters/14-dvije-grupe.qmd"],
            records_by_unit["14"],
            ROOT / "data/populacija-medija.csv",
            ROOT / "data/populacija-medija-agregat.csv",
        )
        errors.extend(numerical_errors)

    page_sources = {
        page.get("source")
        for page in inventory.get("pages", [])
        if page.get("kind") in {"preface", "chapter"}
    }
    check(
        not any(path.startswith(implementation.get("storage_root", "") + "/") for path in page_sources if path),
        "Canonical solution-record storage must not be a declared public AI-export input.",
    )
    check(
        implementation.get("storage_root", "") not in exporter,
        "The public AI exporter must not ingest canonical solution-record storage.",
    )

    profile_region_count = 0
    for source_path, lines in source_lines.items():
        regions = profile_visible_regions(lines, "kolegij")
        profile_region_count += len(regions)
        default_projection = normalize_for_leak_check(profile_projection(lines, None))
        kolegij_projection = normalize_for_leak_check(profile_projection(lines, "kolegij"))
        for region in regions:
            normalized = normalize_for_leak_check(region)
            if len(normalized) >= 40:
                check(normalized not in default_projection, f"{source_path}: protected profile content leaks into default")
                check(normalized in kolegij_projection, f"{source_path}: protected profile content is absent from kolegij")

    export_paths = sorted((ROOT / "docs/ai").glob("*.md"))
    export_paths.extend([ROOT / "docs/llms.txt", ROOT / "docs/llms-full.txt", ROOT / "data/ai-exports.json"])
    public_export_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace") for path in export_paths if path.exists()
    )
    public_export_normalized = normalize_for_leak_check(public_export_text)
    if fixture == "protected_record_leak" and protected_strings:
        public_export_normalized += " " + normalize_for_leak_check(protected_strings[0])
    leaked_protected = sorted(
        {
            value
            for value in protected_strings
            if normalize_for_leak_check(value) in public_export_normalized
        }
    )
    check(
        not leaked_protected,
        "Protected solution-record rubric, alternative, or instructor-note content reached a public AI export.",
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
    unit_record_digests = {
        unit_id: hashlib.sha256(
            json.dumps(
                sorted(records, key=lambda record: record["record_id"]),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        for unit_id, records in sorted(records_by_unit.items())
    }
    print("ASSESSMENT_ARCHITECTURE_OK")
    print(f"- state: assessment:sha256-{digest}")
    print("- governed items: 3; canonical answer components: 6")
    print("- visibility projections: 5; public AI solution fields: 0")
    print("- rubric severity levels: fatal, major, minor, useful_improvement")
    print("- AI roles: 3; competence dimensions: 5; ladder stages: 7")
    print("- assessed code production: false in every stage")
    print(
        f"- solution records authored: {len(solution_records)}; "
        f"units closed: {', '.join(sorted(records_by_unit))}; solution routes implemented: 0"
    )
    print(
        f"- source anchors and prompt SHA-256 bindings: {len(seen_exercise_ids)}; "
        f"kolegij-only source regions checked: {profile_region_count}"
    )
    print(
        "- unit record states: "
        + "; ".join(
            f"{unit_id}=assessment-unit:sha256-{record_digest}"
            for unit_id, record_digest in unit_record_digests.items()
        )
    )
    print(
        f"- protected rubric/alternative/instructor strings checked: {len(protected_strings)}; "
        "public export leaks: 0"
    )
    print(
        "- unit 00 independent numerics: "
        f"total={unit_00_numerical.get('total')} "
        f"portal={unit_00_numerical.get('portal_share')}% "
        f"networks={unit_00_numerical.get('network_share')}% "
        f"gap={unit_00_numerical.get('gap_pp')}pp "
        f"count_gap={unit_00_numerical.get('count_gap')} "
        f"records={unit_00_numerical.get('applicable_records')}"
    )
    if unit_01_numerical:
        print(
            "- unit 01 independent numerics: "
            f"portal={unit_01_numerical.get('portal_share')}% "
            f"print={unit_01_numerical.get('print_share')}% "
            f"networks={unit_01_numerical.get('network_share')}% "
            f"print_network_gap={unit_01_numerical.get('print_network_gap_pp')}pp "
            f"simpson={unit_01_numerical.get('simpson_a')}%/{unit_01_numerical.get('simpson_b')}% "
            f"records={unit_01_numerical.get('applicable_records')} "
            f"print_path={unit_01_numerical.get('print_path')}"
        )
    if unit_02_numerical:
        print(
            "- unit 02 independent numerics: "
            f"mapping={unit_02_numerical.get('mapping')} "
            f"I01={unit_02_numerical.get('i01')} "
            f"I02={unit_02_numerical.get('i02')} "
            f"I03={unit_02_numerical.get('i03')} "
            f"records={unit_02_numerical.get('applicable_records')} "
            f"print_path={unit_02_numerical.get('print_path')}"
        )
    if unit_03_numerical:
        print(
            "- unit 03 independent numerics: "
            f"ballots={unit_03_numerical.get('ballot_sum')} "
            f"turnout_gap={unit_03_numerical.get('turnout_gap')} "
            f"turnout_relative={unit_03_numerical.get('turnout_relative_percent')}% "
            f"portal={unit_03_numerical.get('portal_share')}% "
            f"tv={unit_03_numerical.get('tv_share')}% "
            f"gap={unit_03_numerical.get('share_gap_pp')}pp "
            f"relative_gap={unit_03_numerical.get('relative_media_gap_percent')}% "
            f"records={unit_03_numerical.get('applicable_records')} "
            f"planted_error={unit_03_numerical.get('planted_error')} "
            f"print_path={unit_03_numerical.get('print_path')}"
        )
    if unit_04_numerical:
        print(
            "- unit 04 independent numerics: "
            f"before={unit_04_numerical.get('join_before')} "
            f"wrong={unit_04_numerical.get('join_wrong')} "
            f"correct={unit_04_numerical.get('join_correct')} "
            f"presets={unit_04_numerical.get('compact')}|{unit_04_numerical.get('extreme')} "
            f"aggregate={unit_04_numerical.get('aggregate_first')} "
            f"totals={unit_04_numerical.get('aggregate_totals')} "
            f"sources={unit_04_numerical.get('source_summary')} "
            f"records={unit_04_numerical.get('applicable_records')} "
            f"planted_error={unit_04_numerical.get('planted_error')} "
            f"print_path={unit_04_numerical.get('print_path')}"
        )
    if unit_05_numerical:
        print(
            "- unit 05 independent numerics: "
            f"widths={unit_05_numerical.get('widths')} "
            f"area={unit_05_numerical.get('area_ratio')}x/"
            f"{unit_05_numerical.get('area_increase_percent')}% "
            f"means={unit_05_numerical.get('maximum')}/{unit_05_numerical.get('minimum')} "
            f"gap={unit_05_numerical.get('gap')} "
            f"relative={unit_05_numerical.get('relative_percent')}% "
            f"displayed={unit_05_numerical.get('displayed')} "
            f"records={unit_05_numerical.get('applicable_records')} "
            f"planted_error={unit_05_numerical.get('planted_error')} "
            f"print_path={unit_05_numerical.get('print_path')}"
        )
    if unit_06_numerical:
        print(
            "- unit 06 independent numerics: "
            f"full={unit_06_numerical.get('full_sample')} "
            f"youngest={unit_06_numerical.get('youngest')} "
            f"pairs={unit_06_numerical.get('pair_correlations')} "
            f"eurostat={unit_06_numerical.get('eurostat_pairs')} "
            f"print_r={unit_06_numerical.get('print_correlations')} "
            f"deviations={unit_06_numerical.get('print_deviations')} "
            f"records={unit_06_numerical.get('applicable_records')} "
            f"planted_error={unit_06_numerical.get('planted_error')} "
            f"print_path={unit_06_numerical.get('print_path')}"
        )
    if unit_07_numerical:
        print(
            "- unit 07 independent numerics: "
            f"complement={unit_07_numerical.get('complement')} "
            f"verifier_counts={unit_07_numerical.get('verifier_counts')} "
            f"verifier_rates={unit_07_numerical.get('verifier_rates')} "
            f"records={unit_07_numerical.get('applicable_records')} "
            f"planted_error={unit_07_numerical.get('planted_error')} "
            f"print_path={unit_07_numerical.get('print_path')}"
        )
    if unit_08_numerical:
        print(
            "- unit 08 independent numerics: "
            f"unweighted={unit_08_numerical.get('unweighted')} "
            f"weighted={unit_08_numerical.get('weighted')} "
            f"shift={unit_08_numerical.get('shift_pp')}pp "
            f"records={unit_08_numerical.get('applicable_records')} "
            f"planted_error={unit_08_numerical.get('planted_error')} "
            f"print_path={unit_08_numerical.get('print_path')}"
        )
    if unit_09_numerical:
        print(
            "- unit 09 independent numerics: "
            f"widths={unit_09_numerical.get('widths')} "
            f"misses={unit_09_numerical.get('misses')} "
            f"analytical={unit_09_numerical.get('analytical')} "
            f"reachback={unit_09_numerical.get('reachback')} "
            f"records={unit_09_numerical.get('applicable_records')} "
            f"planted_error={unit_09_numerical.get('planted_error')} "
            f"print_path={unit_09_numerical.get('print_path')}"
        )
    if unit_10_numerical:
        print(
            "- unit 10 independent numerics: "
            f"population={unit_10_numerical.get('population_truth')} "
            f"observed={unit_10_numerical.get('observed')} "
            f"permutation={unit_10_numerical.get('permutation')} "
            f"null_shape={unit_10_numerical.get('null_shape')} "
            f"calibration={unit_10_numerical.get('calibration')} "
            f"records={unit_10_numerical.get('applicable_records')} "
            f"planted_error={unit_10_numerical.get('planted_error')} "
            f"print_path={unit_10_numerical.get('print_path')}"
        )
    if unit_11_numerical:
        print(
            "- unit 11 independent numerics: "
            f"aggregate={unit_11_numerical.get('aggregate')} "
            f"effect={unit_11_numerical.get('effect')} "
            f"power_print={unit_11_numerical.get('power_print')} "
            f"power_analytic={unit_11_numerical.get('power_analytic')} "
            f"posthoc={unit_11_numerical.get('posthoc')} "
            f"target={unit_11_numerical.get('target')} "
            f"records={unit_11_numerical.get('applicable_records')} "
            f"planted_error={unit_11_numerical.get('planted_error')} "
            f"print_path={unit_11_numerical.get('print_path')}"
        )
    if unit_12_numerical:
        print(
            "- unit 12 independent numerics: "
            f"rrr={unit_12_numerical.get('rrr')} "
            f"counts={unit_12_numerical.get('counts')} "
            f"raw={unit_12_numerical.get('raw')} "
            f"standardized={unit_12_numerical.get('standardized')} "
            f"multiplicity={unit_12_numerical.get('multiplicity')} "
            f"records={unit_12_numerical.get('applicable_records')} "
            f"planted_error={unit_12_numerical.get('planted_error')} "
            f"print_path={unit_12_numerical.get('print_path')}"
        )
    if unit_13_numerical:
        print(
            "- unit 13 independent numerics: "
            f"expected={unit_13_numerical.get('expected')} "
            f"observed={unit_13_numerical.get('observed')} "
            f"contributions={unit_13_numerical.get('contributions')} "
            f"chi_square={unit_13_numerical.get('chi_square')} "
            f"p_df1={unit_13_numerical.get('p_value_df1')} "
            f"cramer_v={unit_13_numerical.get('cramer_v')} "
            f"records={unit_13_numerical.get('applicable_records')} "
            f"planted_error={unit_13_numerical.get('planted_error')} "
            f"print_path={unit_13_numerical.get('print_path')}"
        )
    if unit_14_numerical:
        print(
            "- unit 14 independent numerics: "
            f"sample={unit_14_numerical.get('sample')} "
            f"welch={unit_14_numerical.get('welch')} "
            f"ols={unit_14_numerical.get('ols')} "
            f"paired={unit_14_numerical.get('paired')} "
            f"population={unit_14_numerical.get('population')} "
            f"aggregate={unit_14_numerical.get('aggregate')} "
            f"widget={unit_14_numerical.get('widget')} "
            f"records={unit_14_numerical.get('applicable_records')} "
            f"planted_error={unit_14_numerical.get('planted_error')} "
            f"print_path={unit_14_numerical.get('print_path')}"
        )
    print(f"- chapter spines ratified: {len(ratified_spines)} of {len(chapter_spines)}, each at its own G-A2b gate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
