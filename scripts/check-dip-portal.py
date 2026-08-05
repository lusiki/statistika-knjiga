#!/usr/bin/env python3
"""Fail-closed check for the deliberately non-local DIP 2024 portal record.

The check never contacts the portal. It verifies the dated evidence recorded by
P3-DIP, the absence of election bytes, and the catalogue state that prevents a
portal-mediated source from masquerading as a promoted package.

Deliberate in-memory defects:
    DIP_PORTAL_NEGATIVE_FIXTURE=local_copy_added
    DIP_PORTAL_NEGATIVE_FIXTURE=checksum_invented
    DIP_PORTAL_NEGATIVE_FIXTURE=promoting_gate_retained
    DIP_PORTAL_NEGATIVE_FIXTURE=promotion_enabled
    DIP_PORTAL_NEGATIVE_FIXTURE=reconciliation_missing
    DIP_PORTAL_NEGATIVE_FIXTURE=passport_total_drift
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOGUE_CHECK = ROOT / "scripts/check-katalog.py"
PASSPORT = ROOT / "data/dip_2024/PUTOVNICA.md"
ALLOWED_LOCAL_FILES = {PASSPORT.resolve()}
FIXTURES = {
    "",
    "local_copy_added",
    "checksum_invented",
    "promoting_gate_retained",
    "promotion_enabled",
    "reconciliation_missing",
    "passport_total_drift",
}


def load_catalogue_check() -> Any:
    spec = importlib.util.spec_from_file_location("check_katalog", CATALOGUE_CHECK)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load scripts/check-katalog.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    fixture = os.environ.get("DIP_PORTAL_NEGATIVE_FIXTURE", "")
    if fixture not in FIXTURES:
        print(f"DIP_PORTAL_FAIL unknown negative fixture: {fixture}", file=sys.stderr)
        return 1

    module = load_catalogue_check()
    catalogue, _ = module.read_yaml(ROOT / "data/katalog.yml")
    packages = catalogue.get("packages", [])
    package = next((item for item in packages if item.get("id") == "dip_2024"), None)
    if package is None:
        print("DIP_PORTAL_FAIL dip_2024 is absent from the catalogue", file=sys.stderr)
        return 1

    passport = PASSPORT.read_text(encoding="utf-8") if PASSPORT.is_file() else ""
    if fixture == "local_copy_added":
        package["files"] = ["data/dip_2024/rezultati.csv"]
    elif fixture == "checksum_invented":
        package.setdefault("integrity", {})["checksum"] = "invented"
    elif fixture == "promoting_gate_retained":
        package["promoting_gate"] = "G-A3-DIP"
    elif fixture == "promotion_enabled":
        package["promoted"] = True
    elif fixture == "reconciliation_missing":
        package.setdefault("integrity", {})["official_reconciliation"] = None
    elif fixture == "passport_total_drift":
        passport = passport.replace("3558089", "3558090")

    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    integrity = package.get("integrity") or {}
    require(package.get("lane") == "portal-mediated",
            "dip_2024 must remain portal-mediated")
    require(package.get("promoted") is False,
            "dip_2024 must remain unpromoted")
    require(not package.get("promoted_by"),
            "an unpromoted portal record may not name a promoting packet")
    require(package.get("promoting_gate") is None,
            "the deliberately nonpromotable DIP route must clear promoting_gate")
    require(package.get("files") == [],
            "the DIP portal record may not declare a local election copy")
    require(integrity.get("checksum") is None,
            "the DIP portal record may not invent a local checksum")
    reconciliation = integrity.get("official_reconciliation")
    require(isinstance(reconciliation, str) and bool(reconciliation.strip()),
            "the DIP portal record needs the published-total reconciliation")

    promotion_entries = catalogue.get("promotion_contract", {}).get("promotion_log", [])
    promoted_names = {
        name
        for entry in promotion_entries
        for name in (entry.get("packages") or [])
    }
    require("dip_2024" not in promoted_names,
            "dip_2024 may not appear in the promotion log")

    source_dir = ROOT / "data/dip_2024"
    unexpected = []
    if source_dir.is_dir():
        unexpected = [
            path.relative_to(ROOT).as_posix()
            for path in source_dir.rglob("*")
            if path.is_file() and path.resolve() not in ALLOWED_LOCAL_FILES
        ]
    require(not unexpected,
            "the DIP portal directory contains a local election copy: " +
            ", ".join(unexpected))

    required_passport_tokens = (
        "https://www.izbori.hr/site/UserDocsImages/2024/rezultati_sabor.zip",
        "Izvje%C5%A1%C4%87e%20o%20provedenim%20izborima",
        "5. kolovoza 2026.",
        "3558089",
        "2216763",
        "2154733",
        "60476",
        "2215209",
        "1554",
        "checksum: null",
        "promoting_gate: null",
        "Nije provjeren sadržaj ZIP arhiva",
    )
    for token in required_passport_tokens:
        require(token in passport, f"DIP passport is missing required evidence: {token}")

    require(passport.count("3558089") >= 3,
            "DIP passport published denominator no longer reconciles across record, sum, and formula")
    require(passport.count("2216763") >= 3,
            "DIP passport published turnout numerator no longer reconciles across record, sum, and formula")

    if errors:
        for error in errors:
            print(f"DIP_PORTAL_FAIL {error}", file=sys.stderr)
        return 1

    print(
        "DIP_PORTAL_OK "
        "lane=portal-mediated promoted=false local_files=0 checksum=null "
        "published_denominator=3558089 published_approached=2216763 "
        "ballots=2215209 difference=1554"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
