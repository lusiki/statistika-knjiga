#!/usr/bin/env python3
"""Fail-closed validator for the canonical data catalogue.

data/katalog.yml is the sole machine-readable record of the book's data. This
check validates it against data/katalog.schema.json and against the admission and
promotion rules ratified at P3-CATALOG. It fails closed: availability never
promotes a package, and a portal-mediated or external-only package can never be
promoted while its lane stands.

Run:
    python scripts/check-katalog.py
    python scripts/check-katalog.py --print-summary

Deliberate defects, each of which must exit 1:
    KATALOG_NEGATIVE_FIXTURE=promote_portal_mediated
    KATALOG_NEGATIVE_FIXTURE=promote_without_checksum
    KATALOG_NEGATIVE_FIXTURE=unknown_lane
    KATALOG_NEGATIVE_FIXTURE=missing_fallback
    KATALOG_NEGATIVE_FIXTURE=licence_not_applicable
    KATALOG_NEGATIVE_FIXTURE=duplicate_package_id
    KATALOG_NEGATIVE_FIXTURE=cap_exceeded
    KATALOG_NEGATIVE_FIXTURE=undeclared_snapshot
    KATALOG_NEGATIVE_FIXTURE=rights_permission_claimed
    KATALOG_NEGATIVE_FIXTURE=duplicate_consumer_role
"""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOGUE_PATH = ROOT / "data/katalog.yml"
SCHEMA_PATH = ROOT / "data/katalog.schema.json"
ARCHITECTURE_HELPER_PATH = ROOT / "scripts/check-book-architecture.py"
CONVENTIONS_PATH = ROOT / "bookwright_plugin/bookwright/shared/conventions.json"
INVENTORY_REPORT = ROOT / "notes/reports/p1b-data-licence-access-inventory-2026-08-03.md"

BLANK_LICENCE = {
    "",
    "nije primjenjiva",
    "nije primjenjivo",
    "not applicable",
    "n/a",
    "none",
    "nema",
}

FIXTURES = (
    "promote_portal_mediated",
    "promote_without_checksum",
    "unknown_lane",
    "missing_fallback",
    "licence_not_applicable",
    "duplicate_package_id",
    "cap_exceeded",
    "undeclared_snapshot",
    "rights_permission_claimed",
    "duplicate_consumer_role",
)


def load_helper() -> Any:
    spec = importlib.util.spec_from_file_location("book_architecture_check", ARCHITECTURE_HELPER_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError("Could not load scripts/check-book-architecture.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_yaml(path: Path) -> tuple[Any, bool]:
    """Read the catalogue. Returns the value and whether the R fallback was used."""
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        return read_yaml_via_r(path), True
    return yaml.safe_load(path.read_text(encoding="utf-8")), False


def normalise_arrays(value: Any, schema: dict[str, Any], root: dict[str, Any]) -> Any:
    """Rewrap scalars the R/JSON bridge unboxed out of single-element arrays.

    jsonlite's auto_unbox collapses a one-element YAML list to a scalar. That is a
    reader artifact, not a catalogue defect, so it is repaired against the schema
    rather than worked around by loosening the schema.
    """
    if "$ref" in schema:
        target = root
        for part in schema["$ref"].lstrip("#/").split("/"):
            target = target[part]
        return normalise_arrays(value, target, root)

    expected = schema.get("type")
    if expected == "array" and not isinstance(value, list):
        value = [value]
    if isinstance(value, list) and isinstance(schema.get("items"), dict):
        return [normalise_arrays(item, schema["items"], root) for item in value]
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        return {
            key: normalise_arrays(item, properties[key], root) if key in properties else item
            for key, item in value.items()
        }
    return value


def read_yaml_via_r(path: Path) -> Any:
    """Fall back to the project launcher's R when PyYAML is absent."""
    import subprocess
    import tempfile

    launcher = ROOT / "bookwright_plugin/bookwright/scripts/run_rscript.py"
    with tempfile.TemporaryDirectory(prefix="statistika-katalog-") as directory:
        work = Path(directory)
        out = work / "katalog.json"
        script = work / "convert.R"
        script.write_text(
            "suppressMessages({library(yaml); library(jsonlite)})\n"
            f'x <- yaml::read_yaml("{path.as_posix()}")\n'
            f'write(jsonlite::toJSON(x, auto_unbox = TRUE, null = "null"), "{out.as_posix()}")\n',
            encoding="utf-8",
        )
        result = subprocess.run(
            [sys.executable, str(launcher), str(script)],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode or not out.exists():
            raise AssertionError(f"Could not read {path.name} through the R launcher: {result.stdout}")
        return json.loads(out.read_text(encoding="utf-8"))


def apply_fixture(catalogue: dict[str, Any], fixture: str) -> list[str]:
    """Inject one deliberate defect. Never touches the file on disk."""
    packages = catalogue["packages"]
    if fixture == "promote_portal_mediated":
        for package in packages:
            if package["lane"] == "portal-mediated":
                package["promoted"] = True
                break
    elif fixture == "promote_without_checksum":
        for package in packages:
            if package["lane"] == "bundled":
                package["promoted"] = True
                package["files"] = ["data/fixture.csv"]
                package["redistribution"] = "provjerena"
                break
    elif fixture == "unknown_lane":
        packages[0]["lane"] = "self-hosted"
    elif fixture == "missing_fallback":
        packages[0]["fallback"] = ""
    elif fixture == "licence_not_applicable":
        packages[0]["licence"] = "nije primjenjiva"
    elif fixture == "duplicate_package_id":
        clone = copy.deepcopy(packages[0])
        packages.append(clone)
    elif fixture == "cap_exceeded":
        catalogue["portfolio_caps"]["caps"][0]["registered"] = (
            catalogue["portfolio_caps"]["caps"][0]["cap"] + 1
        )
    elif fixture == "undeclared_snapshot":
        return ["data/fixture-undeclared.csv"]
    elif fixture == "rights_permission_claimed":
        catalogue["rights_boundary"]["rights_holder_permission_claim_permitted"] = True
    elif fixture == "duplicate_consumer_role":
        role = packages[0]["role"]
        for package in packages[1:]:
            if package["design"] == packages[0]["design"]:
                package["role"] = role
                break
    else:
        raise AssertionError(f"Unknown katalog negative fixture: {fixture}")
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--print-summary", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    try:
        helper = load_helper()
        catalogue, via_r = read_yaml(CATALOGUE_PATH)
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        conventions = json.loads(CONVENTIONS_PATH.read_text(encoding="utf-8"))
        if via_r and isinstance(catalogue, dict):
            catalogue = normalise_arrays(catalogue, schema, schema)
    except (AssertionError, OSError, json.JSONDecodeError) as exc:
        print(f"Katalog: FAILED\n- {exc}")
        return 1

    if not isinstance(catalogue, dict):
        print("Katalog: FAILED\n- data/katalog.yml is not a mapping.")
        return 1

    catalogue = copy.deepcopy(catalogue)
    extra_snapshots: list[str] = []
    fixture = os.environ.get("KATALOG_NEGATIVE_FIXTURE", "")
    if fixture:
        try:
            extra_snapshots = apply_fixture(catalogue, fixture)
        except AssertionError as exc:
            print(f"Katalog: FAILED\n- {exc}")
            return 1

    errors.extend(helper.validate_schema(catalogue, schema, schema))

    packages = catalogue.get("packages", [])
    ids = [p.get("id", "") for p in packages]
    check(len(ids) == len(set(ids)), f"duplicate package id: {sorted({i for i in ids if ids.count(i) > 1})}")

    # --- ratified data-design ids -------------------------------------------
    designs = {
        d["id"]
        for d in conventions["intellectual_architecture"]["data_science_registry"]["data_design_policy"]["designs"]
    }
    classes = set(catalogue.get("refresh_classes", []))
    lanes = set(catalogue.get("lanes", {}))

    roles_by_design: dict[str, list[str]] = {}
    for package in packages:
        pid = package.get("id", "<missing>")
        check(package.get("design") in designs,
              f"{pid}: design is not a ratified data-generating design: {package.get('design')}")
        check(package.get("lane") in lanes,
              f"{pid}: lane is not one of the three ratified lanes: {package.get('lane')}")
        check(package.get("refresh_class") in classes,
              f"{pid}: refresh class is not declared in the catalogue: {package.get('refresh_class')}")
        licence = str(package.get("licence", "")).strip().casefold()
        check(licence not in BLANK_LICENCE,
              f"{pid}: licence may never be blank or 'not applicable'.")
        check(bool(str(package.get("fallback", "")).strip()),
              f"{pid}: every package needs one lawful fallback for the required student path.")
        integrity = package.get("integrity") or {}
        check(bool(str(integrity.get("note", "")).strip()),
              f"{pid}: integrity record needs a note even when no checksum exists.")
        roles_by_design.setdefault(package.get("design", ""), []).append(str(package.get("role", "")))

        # --- promotion rules -------------------------------------------------
        if package.get("promoted") is True:
            check(package.get("lane") == "bundled",
                  f"{pid}: only a bundled package may be promoted; lane is {package.get('lane')}.")
            check(str(package.get("redistribution", "")).strip().casefold() == "provjerena",
                  f"{pid}: promotion requires verified redistribution.")
            check(bool(integrity.get("checksum")),
                  f"{pid}: promotion requires a recorded checksum.")
            check(bool(integrity.get("official_reconciliation")),
                  f"{pid}: promotion requires a recorded official reconciliation.")
            check(bool(package.get("files")),
                  f"{pid}: promotion requires at least one recorded file path.")

    # --- consumer roles must be distinct within a design --------------------
    for design, roles in roles_by_design.items():
        folded = [" ".join(r.casefold().split()) for r in roles]
        duplicates = sorted({r for r in folded if folded.count(r) > 1})
        check(not duplicates,
              f"{design}: two packages share one consumer role, so one is admitted only for topic variety: {duplicates}")

    # --- portfolio caps -----------------------------------------------------
    caps = catalogue.get("portfolio_caps", {}).get("caps", [])
    registered_by_design: dict[str, int] = {}
    promoted_by_design: dict[str, int] = {}
    for package in packages:
        registered_by_design[package.get("design", "")] = registered_by_design.get(package.get("design", ""), 0) + 1
        if package.get("promoted") is True:
            promoted_by_design[package.get("design", "")] = promoted_by_design.get(package.get("design", ""), 0) + 1
    for cap in caps:
        design = cap.get("design", "")
        check(design in designs, f"portfolio cap names an unknown design: {design}")
        check(cap.get("registered") == registered_by_design.get(design, 0),
              f"{design}: recorded registered count {cap.get('registered')} disagrees with the "
              f"{registered_by_design.get(design, 0)} packages in the catalogue.")
        check(cap.get("promoted") == promoted_by_design.get(design, 0),
              f"{design}: recorded promoted count disagrees with the catalogue.")
        check(cap.get("registered", 0) <= cap.get("cap", 0),
              f"{design}: registered packages exceed the cap and no author approval is recorded.")
    covered = {cap.get("design") for cap in caps}
    missing = sorted(set(registered_by_design) - covered)
    check(not missing, f"portfolio caps omit a design that has registered packages: {missing}")

    # --- promotion contract counter ----------------------------------------
    promoted_total = sum(1 for p in packages if p.get("promoted") is True)
    declared = catalogue.get("promotion_contract", {}).get("promoted_by_this_packet")
    check(promoted_total == declared,
          f"promotion_contract declares {declared} promoted packages but the catalogue carries {promoted_total}.")

    # --- rights boundary ----------------------------------------------------
    rights = catalogue.get("rights_boundary", {})
    check(rights.get("rights_holder_permission_obtained") is False,
          "the catalogue may not record that rights-holder permission was obtained; none was sought.")
    check(rights.get("rights_holder_permission_claim_permitted") is False,
          "the catalogue may not permit a rights-holder permission claim.")

    # --- no undeclared materialised snapshot --------------------------------
    declared_files = {f for p in packages for f in (p.get("files") or [])}
    on_disk = [
        str(path.relative_to(ROOT)).replace("\\", "/")
        for path in sorted((ROOT / "data").glob("*"))
        if path.suffix.lower() in {".csv", ".tsv", ".parquet", ".rds"}
    ]
    on_disk.extend(extra_snapshots)
    undeclared = sorted(set(on_disk) - declared_files)
    check(not undeclared,
          f"materialised data snapshots are not declared by any catalogue entry: {undeclared}")

    # --- the catalogue must trace back to its ratified inventory ------------
    check(CATALOGUE_PATH.exists() and INVENTORY_REPORT.exists(),
          "the catalogue must name an existing source inventory.")
    check(str(catalogue.get("source_inventory", "")) ==
          str(INVENTORY_REPORT.relative_to(ROOT)).replace("\\", "/"),
          "source_inventory must name the ratified P1B licence and access inventory.")

    # --- no credential may live in the catalogue ----------------------------
    blob = json.dumps(catalogue, ensure_ascii=False)
    for needle in ("password", "api_key", "apikey", "token=", "secret"):
        check(needle not in blob.casefold(),
              f"the catalogue must carry no credential material: {needle}")
    check(not re.search(r"https?://\S*:\S*@", blob),
          "the catalogue must carry no embedded credentials in a URL.")

    if errors:
        print("Katalog: FAILED")
        for message in errors:
            print(f"- {message}")
        return 1

    lane_counts: dict[str, int] = {}
    for package in packages:
        lane_counts[package["lane"]] = lane_counts.get(package["lane"], 0) + 1

    if args.print_summary:
        print(json.dumps({"packages": len(packages), "lanes": lane_counts,
                          "promoted": promoted_total}, ensure_ascii=False, indent=2))
        return 0

    print(
        "KATALOG_OK "
        f"packages={len(packages)} promoted={promoted_total} "
        f"bundled={lane_counts.get('bundled', 0)} "
        f"portal={lane_counts.get('portal-mediated', 0)} "
        f"external={lane_counts.get('external-only', 0)} "
        f"designs={len(registered_by_design)} snapshots={len(on_disk)} "
        "rights_permission_claim=false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
