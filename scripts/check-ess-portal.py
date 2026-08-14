#!/usr/bin/env python3
"""Fail-closed check for the deliberately non-local ESS Round 11 route.

The check never contacts the ESS portal. It validates the exact author-approved
catalogue contract, the passport and preparation recipe, the open rights gate,
and the absence of ESS microdata and a repository-owned checksum.

Deliberate in-memory defects:
    ESS_PORTAL_NEGATIVE_FIXTURE=local_copy_added
    ESS_PORTAL_NEGATIVE_FIXTURE=checksum_invented
    ESS_PORTAL_NEGATIVE_FIXTURE=promotion_enabled
    ESS_PORTAL_NEGATIVE_FIXTURE=wrong_consumers
    ESS_PORTAL_NEGATIVE_FIXTURE=source_drift
    ESS_PORTAL_NEGATIVE_FIXTURE=reconciliation_missing
    ESS_PORTAL_NEGATIVE_FIXTURE=passport_contract_removed
    ESS_PORTAL_NEGATIVE_FIXTURE=recipe_guard_removed
    ESS_PORTAL_NEGATIVE_FIXTURE=rights_boundary_lost
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOGUE_CHECK = ROOT / "scripts/check-katalog.py"
CATALOGUE = ROOT / "data/katalog.yml"
REGISTER = ROOT / "notes/reports/comprehensive-review-implementation-register.yml"
PASSPORT = ROOT / "data/ess_r11_hr/PUTOVNICA.md"
RECIPE = ROOT / "scripts/prepare-ess-r11-hr.R"
ALLOWED_ESS_DIRECTORY_FILES = {PASSPORT.resolve()}

IDENTITY_VARIABLES = ("essround", "edition", "proddate", "idno", "cntry")
DESIGN_VARIABLES = (
    "dweight", "pspwght", "pweight", "anweight", "prob", "stratum", "psu"
)
TEACHING_VARIABLES = ("vote", "trstprl", "stflife", "gndr", "agea", "eisced")
EXPECTED_VARIABLES = IDENTITY_VARIABLES + DESIGN_VARIABLES + TEACHING_VARIABLES
EXPECTED_CONSUMERS = {"WC-C08", "WD-C13", "WD-C14", "WD-C15", "WD-C16"}
FIXTURES = {
    "",
    "local_copy_added",
    "checksum_invented",
    "promotion_enabled",
    "wrong_consumers",
    "source_drift",
    "reconciliation_missing",
    "passport_contract_removed",
    "recipe_guard_removed",
    "rights_boundary_lost",
}


def load_catalogue_check() -> Any:
    spec = importlib.util.spec_from_file_location("check_katalog", CATALOGUE_CHECK)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load scripts/check-katalog.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    fixture = os.environ.get("ESS_PORTAL_NEGATIVE_FIXTURE", "")
    if fixture not in FIXTURES:
        print(f"ESS_PORTAL_FAIL unknown negative fixture: {fixture}", file=sys.stderr)
        return 1

    module = load_catalogue_check()
    catalogue, _ = module.read_yaml(CATALOGUE)
    register, _ = module.read_yaml(REGISTER)
    package = next(
        (item for item in catalogue.get("packages", []) if item.get("id") == "ess_r11_hr"),
        None,
    )
    if package is None:
        print("ESS_PORTAL_FAIL ess_r11_hr is absent from the catalogue", file=sys.stderr)
        return 1

    passport = PASSPORT.read_text(encoding="utf-8") if PASSPORT.is_file() else ""
    recipe = RECIPE.read_text(encoding="utf-8") if RECIPE.is_file() else ""

    if fixture == "local_copy_added":
        package["files"] = ["data/ess_r11_hr/ESS11e03_0.sav"]
    elif fixture == "checksum_invented":
        package.setdefault("integrity", {})["checksum"] = "invented"
    elif fixture == "promotion_enabled":
        package["promoted"] = True
    elif fixture == "wrong_consumers":
        package["consumers"] = ["WD-C13", "WD-C14", "WD-C15", "WD-C16"]
    elif fixture == "source_drift":
        package["version"] = "Round 11, edition 2.0"
    elif fixture == "reconciliation_missing":
        package.setdefault("integrity", {})["official_reconciliation"] = None
    elif fixture == "passport_contract_removed":
        passport = passport.replace("`na_values`", "removed-missing-values-token")
    elif fixture == "recipe_guard_removed":
        recipe = recipe.replace(
            'stop("ESS output would be inside the repository; choose an external directory.", call. = FALSE)',
            'message("repository output accepted")',
        )
    elif fixture == "rights_boundary_lost":
        package["redistribution"] = "bundling permitted"

    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    integrity = package.get("integrity") or {}
    require(package.get("status") == "validated_portal_route_not_promoted",
            "ess_r11_hr must declare the validated, unpromoted portal status")
    require(package.get("lane") == "portal-mediated",
            "ess_r11_hr must remain portal-mediated")
    require(package.get("promoted") is False,
            "ess_r11_hr must remain unpromoted")
    require(not package.get("promoted_by"),
            "an unpromoted ESS route may not name a promoting packet")
    require(not package.get("promoting_gate"),
            "the ESS portal route may not retain a decision gate as promoter")
    require(package.get("files") == [],
            "the ESS portal record may not declare local microdata")
    require(integrity.get("checksum") is None,
            "the ESS portal record may not invent a repository-owned checksum")
    reconciliation = integrity.get("official_reconciliation")
    require(isinstance(reconciliation, str) and bool(reconciliation.strip()),
            "the ESS portal record needs the official metadata reconciliation")
    if isinstance(reconciliation, str):
        for token in ("ESS11", "edition 3.0", "SAV", "codebook"):
            require(token in reconciliation,
                    f"ESS official reconciliation is missing: {token}")

    require(set(package.get("consumers") or []) == EXPECTED_CONSUMERS,
            "ESS consumers must be exactly WC-C08 and WD-C13 through WD-C16")
    require(package.get("version") == "Round 11, edition 3.0",
            "ESS version must remain Round 11, edition 3.0")
    require(package.get("passport") == "data/ess_r11_hr/PUTOVNICA.md",
            "ESS catalogue entry must point to its portal passport")
    require("anweight" in str(package.get("role", "")),
            "ESS role must name anweight as the default analysis weight")
    require("vote" in str(package.get("question", "")) and
            "anweight" in str(package.get("question", "")),
            "ESS question must remain the bounded vote comparison")
    fallback = str(package.get("fallback", ""))
    require("WC-C08" in fallback and "sintetick" in fallback and "13-16" in fallback,
            "ESS fallback must separate the synthetic Chapter 8 and local Chapter 13-16 paths")
    redistribution = str(package.get("redistribution", "")).lower()
    require("ne odobrava bundling" in redistribution,
            "ESS redistribution text must keep bundling unapproved")

    promotion_entries = catalogue.get("promotion_contract", {}).get("promotion_log", [])
    promoted_names = {
        name
        for entry in promotion_entries
        for name in (entry.get("packages") or [])
    }
    require("ess_r11_hr" not in promoted_names,
            "ess_r11_hr may not appear in the promotion log")

    source_dir = ROOT / "data/ess_r11_hr"
    unexpected: list[str] = []
    if source_dir.is_dir():
        unexpected = [
            path.relative_to(ROOT).as_posix()
            for path in source_dir.rglob("*")
            if path.is_file() and path.resolve() not in ALLOWED_ESS_DIRECTORY_FILES
        ]
    require(not unexpected,
            "the ESS portal directory contains non-passport bytes: " + ", ".join(unexpected))

    required_passport_tokens = (
        "https://ess.sikt.no/en/",
        "ESS Round 11 integrated main file, edition 3.0",
        "Get-FileHash -Algorithm SHA256",
        "shasum -a 256",
        "`na_values`",
        "`na_range`",
        "analitički",
        "OA-G-A3-ESS-RIGHTS",
        "bundling je zabranjen",
        "sintetičku konačnu populaciju",
        "populacija_medija",
    ) + tuple(f"`{name}`" for name in EXPECTED_VARIABLES)
    for token in required_passport_tokens:
        require(token in passport, f"ESS passport is missing required evidence: {token}")

    required_recipe_tokens = (
        'haven::read_sav(input_path, user_na = TRUE)',
        'subset = "cntry == HR"',
        'default_analysis_weight = "anweight"',
        'metadata_record',
        'is_source_missing',
        'saveRDS(selected',
        'jsonlite::write_json',
        'ESS output would be inside the repository',
        'ESS input is inside the repository',
    ) + tuple(f'"{name}"' for name in EXPECTED_VARIABLES)
    for token in required_recipe_tokens:
        require(token in recipe, f"ESS preparation recipe is missing: {token}")

    forbidden_network_patterns = (
        r"\bdownload[.]file\s*\(",
        r"\bhttr(?:::|2::)",
        r"\bcurl::",
        r"\bGET\s*\(",
    )
    for pattern in forbidden_network_patterns:
        require(re.search(pattern, recipe) is None,
                f"ESS preparation recipe contains a network operation: {pattern}")

    rights_ask = (register.get("outside_asks") or {}).get("OA-G-A3-ESS-RIGHTS") or {}
    require(rights_ask.get("status") == "drafted_unsent",
            "OA-G-A3-ESS-RIGHTS must remain open and unsent")
    require(rights_ask.get("external_message_sent") is False,
            "the ESS rights inquiry may not be marked sent")

    if errors:
        for error in errors:
            print(f"ESS_PORTAL_FAIL {error}", file=sys.stderr)
        return 1

    print(
        "ESS_PORTAL_OK "
        "round=11 edition=3.0 subset=HR variables=18 consumers=5 "
        "default_weight=anweight lane=portal-mediated promoted=false "
        "local_data_files=0 checksum=null rights_ask=open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
