#!/usr/bin/env python3
"""Block publication when any OJS/print-twin golden claim drifts.

The registry in data/widgets.json owns parameters, seed policies, tolerances,
adapter-specific golden values, source fingerprints, and claim boundaries.
This checker deliberately tests numeric claims only; browser layout and visual
inventory belong to other independently callable checks.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


EXPECTED_IDS = [f"w{index:02d}" for index in range(1, 18)]
EXPECTED_CLASS_COUNTS = {"exact": 6, "distributional": 11}
ADAPTERS = {
    "ojs": "scripts/widget-parity-ojs.mjs",
    "r": "scripts/widget-parity-r.R",
}


def normalized_block(block: str) -> str:
    return block.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n") + "\n"


def fenced_blocks(text: str, language: str) -> list[str]:
    pattern = re.compile(
        rf"^```\{{{re.escape(language)}\}}[ \t]*\n(.*?)^```[ \t]*$",
        re.MULTILINE | re.DOTALL,
    )
    return [normalized_block(match.group(1)) for match in pattern.finditer(text)]


def source_hashes(root: Path, widget: dict[str, Any]) -> dict[str, str]:
    chapter = root / widget["poglavlje"]
    text = chapter.read_text(encoding="utf-8")
    source = widget["parity"]["source"]

    ojs_blocks = fenced_blocks(text, "ojs")
    labelled_ojs = [block for block in ojs_blocks if f"//| label: {source['ojs_label']}" in block]
    if len(labelled_ojs) != 1 or not ojs_blocks:
        raise ValueError(
            f"{widget['id']}: expected one {source['ojs_label']} OJS block and at least one OJS block"
        )
    ojs_payload = "---PARITY-OJS-BLOCK---\n".join(ojs_blocks)

    r_blocks = fenced_blocks(text, "r")
    print_blocks = [block for block in r_blocks if f"#| label: {source['r_label']}" in block]
    if len(print_blocks) != 1:
        raise ValueError(f"{widget['id']}: expected one {source['r_label']} R block")
    r_payload = print_blocks[0]

    return {
        "ojs_sha256": hashlib.sha256(ojs_payload.encode("utf-8")).hexdigest(),
        "r_sha256": hashlib.sha256(r_payload.encode("utf-8")).hexdigest(),
    }


def run_json(command: list[str], root: Path) -> dict[str, Any]:
    completed = subprocess.run(
        command,
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if completed.returncode:
        detail = (completed.stderr or completed.stdout).strip()
        raise RuntimeError(f"command failed ({completed.returncode}): {' '.join(command)}\n{detail}")
    # renv may print a project-status advisory before the adapter's JSON on a
    # developer machine. The locked clean proof has no advisory, while this
    # keeps the independently callable local check focused on adapter output.
    json_start = completed.stdout.find("{")
    try:
        return json.loads(completed.stdout[json_start:] if json_start >= 0 else completed.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"command did not return JSON: {' '.join(command)}\n{completed.stdout.strip()}"
        ) from error


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def compare_value(actual: Any, expected: Any, tolerance: float) -> bool:
    if actual is None or expected is None:
        return actual is None and expected is None
    return is_number(actual) and is_number(expected) and abs(actual - expected) <= tolerance


def validate_adapter_payload(adapter: str, payload: dict[str, Any], errors: list[str]) -> None:
    if payload.get("schema_version") != 1:
        errors.append(f"[adapter] {adapter}: schema_version must be 1")
    if payload.get("adapter") != adapter:
        errors.append(f"[adapter] {adapter}: adapter identity mismatch")
    results = payload.get("results")
    if not isinstance(results, dict) or list(results) != EXPECTED_IDS:
        errors.append(f"[adapter] {adapter}: results must be ordered w01..w17")


def validate_invariant(
    widget_id: str,
    adapter: str,
    values: dict[str, Any],
    invariant: dict[str, Any],
    errors: list[str],
) -> None:
    if invariant.get("adapter") not in (adapter, "both"):
        return
    left_key = invariant.get("left")
    operator = invariant.get("operator")
    if left_key not in values:
        errors.append(f"[invariant] {widget_id}/{adapter}: missing left metric {left_key!r}")
        return
    left = values[left_key]
    if "right" in invariant:
        right_key = invariant["right"]
        if right_key not in values:
            errors.append(f"[invariant] {widget_id}/{adapter}: missing right metric {right_key!r}")
            return
        right = values[right_key]
    elif "value" in invariant:
        right = invariant["value"]
    else:
        errors.append(f"[invariant] {widget_id}/{adapter}: right or value is required")
        return
    operations = {
        "<": lambda a, b: a < b,
        "<=": lambda a, b: a <= b,
        ">": lambda a, b: a > b,
        ">=": lambda a, b: a >= b,
        "==": lambda a, b: a == b,
    }
    if operator not in operations:
        errors.append(f"[invariant] {widget_id}/{adapter}: unsupported operator {operator!r}")
        return
    if not is_number(left) or not is_number(right) or not operations[operator](left, right):
        errors.append(
            f"[invariant] {widget_id}/{adapter}: {left_key}={left!r} {operator} {right!r} failed"
        )


def check_registry(root: Path, registry: dict[str, Any], errors: list[str]) -> list[dict[str, Any]]:
    widgets = registry.get("widgets")
    if not isinstance(widgets, list) or [widget.get("id") for widget in widgets] != EXPECTED_IDS:
        errors.append("[registry] data/widgets.json must contain exactly ordered w01..w17")
        return []

    counts = {key: 0 for key in EXPECTED_CLASS_COUNTS}
    for widget in widgets:
        widget_id = widget["id"]
        parity = widget.get("parity")
        if not isinstance(parity, dict):
            errors.append(f"[registry] {widget_id}: parity record is required")
            continue
        classification = parity.get("classification")
        if classification not in counts:
            errors.append(f"[registry] {widget_id}: invalid classification {classification!r}")
        else:
            counts[classification] += 1
        if not isinstance(parity.get("parameters"), dict) or not parity["parameters"]:
            errors.append(f"[registry] {widget_id}: non-empty parameters are required")
        seed = parity.get("seed_policy")
        if not isinstance(seed, dict) or any(not seed.get(key) for key in ("ojs", "r", "shared")):
            errors.append(f"[registry] {widget_id}: complete ojs/r/shared seed policy is required")
        tolerance = parity.get("tolerance")
        if not isinstance(tolerance, dict) or not is_number(tolerance.get("golden_absolute")):
            errors.append(f"[registry] {widget_id}: numeric golden_absolute tolerance is required")
        elif tolerance["golden_absolute"] < 0:
            errors.append(f"[registry] {widget_id}: golden_absolute tolerance cannot be negative")
        pairs = tolerance.get("pair_absolute") if isinstance(tolerance, dict) else None
        if not isinstance(pairs, dict) or not pairs:
            errors.append(f"[registry] {widget_id}: non-empty pair_absolute tolerances are required")
        elif any(not is_number(value) or value < 0 for value in pairs.values()):
            errors.append(f"[registry] {widget_id}: pair tolerances must be finite non-negative numbers")
        expected = parity.get("expected")
        if (
            not isinstance(expected, dict)
            or any(not isinstance(expected.get(adapter), dict) or not expected[adapter] for adapter in ADAPTERS)
        ):
            errors.append(f"[registry] {widget_id}: non-empty ojs and r golden values are required")
        declared = parity.get("adapters")
        for adapter, path in ADAPTERS.items():
            if not isinstance(declared, dict) or declared.get(adapter) != f"{path}#{widget_id}":
                errors.append(f"[registry] {widget_id}: invalid {adapter} adapter declaration")
        source = parity.get("source")
        if not isinstance(source, dict):
            errors.append(f"[registry] {widget_id}: source contract is required")
        else:
            for adapter in ADAPTERS:
                digest = source.get(f"{adapter}_sha256", "")
                if not re.fullmatch(r"[0-9a-f]{64}", digest):
                    errors.append(f"[registry] {widget_id}: valid {adapter} SHA-256 is required")
        if not isinstance(parity.get("claim_boundary"), str) or not parity["claim_boundary"].strip():
            errors.append(f"[registry] {widget_id}: claim boundary is required")

    if counts != EXPECTED_CLASS_COUNTS:
        errors.append(f"[registry] classification counts {counts!r} != {EXPECTED_CLASS_COUNTS!r}")
    return widgets


def check_parity(root: Path, fixture: str | None) -> int:
    registry = json.loads((root / "data" / "widgets.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    widgets = check_registry(root, registry, errors)

    payloads: dict[str, dict[str, Any]] = {}
    try:
        ojs_command = ["node", str(root / ADAPTERS["ojs"]), str(root)]
        if fixture == "normal-cache-asymmetry":
            ojs_command.append("w09-cached-normal")
        elif fixture == "w10-normal-cache-asymmetry":
            ojs_command.append("w10-cached-normal")
        elif fixture == "w11-normal-cache-asymmetry":
            ojs_command.append("w11-cached-normal")
        elif fixture == "w14-normal-cache-asymmetry":
            ojs_command.append("w14-cached-normal")
        payloads["ojs"] = run_json(ojs_command, root)
        payloads["r"] = run_json(
            [
                sys.executable,
                str(root / "bookwright_plugin/bookwright/scripts/run_rscript.py"),
                str(root / ADAPTERS["r"]),
                str(root),
            ],
            root,
        )
    except (OSError, RuntimeError) as error:
        errors.append(f"[adapter] {error}")

    for adapter, payload in payloads.items():
        validate_adapter_payload(adapter, payload, errors)

    if fixture == "expected-value-regression" and "ojs" in payloads:
        payloads["ojs"]["results"]["w01"]["default.aggregate_a"] += 0.01

    if widgets and set(payloads) == set(ADAPTERS):
        for widget in widgets:
            widget_id = widget["id"]
            parity = widget["parity"]
            actual_by_adapter = {
                adapter: payloads[adapter]["results"].get(widget_id, {}) for adapter in ADAPTERS
            }
            for adapter, actual in actual_by_adapter.items():
                expected = parity["expected"][adapter]
                if not isinstance(actual, dict):
                    errors.append(f"[adapter] {widget_id}/{adapter}: result must be an object")
                    continue
                if set(actual) != set(expected):
                    errors.append(
                        f"[golden] {widget_id}/{adapter}: metric keys differ; "
                        f"actual={sorted(actual)} expected={sorted(expected)}"
                    )
                    continue
                golden_tolerance = parity["tolerance"]["golden_absolute"]
                for metric, expected_value in expected.items():
                    actual_value = actual[metric]
                    if not compare_value(actual_value, expected_value, golden_tolerance):
                        errors.append(
                            f"[golden] {widget_id}/{adapter}/{metric}: "
                            f"actual={actual_value!r} expected={expected_value!r} "
                            f"tolerance={golden_tolerance}"
                        )
                for invariant in parity["tolerance"].get("invariants", []):
                    validate_invariant(widget_id, adapter, actual, invariant, errors)

            ojs_values = actual_by_adapter["ojs"]
            r_values = actual_by_adapter["r"]
            if isinstance(ojs_values, dict) and isinstance(r_values, dict):
                if set(ojs_values) != set(r_values):
                    errors.append(f"[pair] {widget_id}: OJS/R metric keys differ")
                for pattern, tolerance in parity["tolerance"]["pair_absolute"].items():
                    matched = [metric for metric in ojs_values if fnmatch.fnmatchcase(metric, pattern)]
                    if not matched:
                        errors.append(f"[pair] {widget_id}: tolerance pattern {pattern!r} matches no metric")
                    for metric in matched:
                        if metric not in r_values or not compare_value(ojs_values[metric], r_values[metric], tolerance):
                            errors.append(
                                f"[pair] {widget_id}/{metric}: ojs={ojs_values.get(metric)!r} "
                                f"r={r_values.get(metric)!r} tolerance={tolerance}"
                            )

            try:
                current_hashes = source_hashes(root, widget)
                for key, current in current_hashes.items():
                    declared = parity["source"].get(key)
                    if current != declared:
                        errors.append(
                            f"[source] {widget_id}/{key}: current={current} declared={declared}"
                        )
            except (KeyError, OSError, ValueError) as error:
                errors.append(f"[source] {error}")

    if errors:
        for error in errors:
            print(f"WIDGET_PARITY_ERROR {error}", file=sys.stderr)
        print(f"WIDGET_PARITY_FAILED errors={len(errors)}", file=sys.stderr)
        return 1

    print("WIDGET_PARITY_OK pairs=17 exact=6 distributional=11")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument(
        "--fixture",
        choices=[
            "expected-value-regression",
            "normal-cache-asymmetry",
            "w10-normal-cache-asymmetry",
            "w11-normal-cache-asymmetry",
            "w14-normal-cache-asymmetry",
        ],
    )
    parser.add_argument("--print-source-hashes", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    if args.print_source_hashes:
        registry = json.loads((root / "data" / "widgets.json").read_text(encoding="utf-8"))
        output = {widget["id"]: source_hashes(root, widget) for widget in registry["widgets"]}
        print(json.dumps(output, indent=2, ensure_ascii=False))
        return 0
    return check_parity(root, args.fixture)


if __name__ == "__main__":
    raise SystemExit(main())
