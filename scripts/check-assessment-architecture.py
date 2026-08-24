#!/usr/bin/env python3
"""Validate the ratified G-A2d assessment architecture without new dependencies."""

from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import json
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
    print(f"- chapter spines ratified: {len(ratified_spines)} of {len(chapter_spines)}, each at its own G-A2b gate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
