#!/usr/bin/env python3
"""Verify Appendix D's decision, dependence, cross-reference, and print contract."""

from __future__ import annotations

import json
import re
import shutil
import struct
import tempfile
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("dodaci/d-koji-test.qmd")
ROUTE = Path("config/appendix-d-decision-route.json")
SVG = Path("images/infographics/koji-test-kada.svg")
PNG = Path("images/infographics/koji-test-kada.png")


def fail(message: str) -> None:
    raise SystemExit(f"APPENDIX_D_CHECK_FAILED {message}")


def heading_id(text: str) -> str:
    text = re.sub(r"\s+\{.*\}\s*$", "", text.strip()).lower()
    kept = []
    for char in text:
        category = unicodedata.category(char)
        if char.isspace():
            kept.append("-")
        elif category[0] in {"L", "N"} or char in {"_", "-", "."}:
            kept.append(char)
    value = re.sub(r"-+", "-", "".join(kept)).strip("-")
    return re.sub(r"^[^\w]+", "", value, flags=re.UNICODE)


def validate(base: Path) -> dict[str, int]:
    source_path = base / SOURCE
    route_path = base / ROUTE
    svg_path = base / SVG
    png_path = base / PNG
    for path in (source_path, route_path, svg_path, png_path):
        if not path.is_file():
            fail(f"missing={path.relative_to(base)}")

    prose = source_path.read_text(encoding="utf-8")
    if "djelomični nacrt" in prose or "~1500 riječi" in prose:
        fail("partial-draft-marker-remains")
    required_phrases = (
        "Vrsta ishoda jest važna, ali sama nikada ne određuje postupak.",
        "Svaki širi oblik ovisnosti zaustavlja običnu inferenciju neovisnih redaka.",
        "takav se postupak u ovoj knjizi ne poučava",
        "Kad knjiga nema postupak",
        "statističkom metodologu",
    )
    prose_flat = re.sub(r"\s+", " ", prose)
    for phrase in required_phrases:
        if phrase not in prose_flat:
            fail(f"missing-source-contract={phrase}")

    data = json.loads(route_path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("route-schema-version")
    expected_order = [
        "question",
        "outcome_type",
        "design_and_dependence",
        "estimand",
        "assumptions",
        "claim",
    ]
    if data.get("decision_order") != expected_order:
        fail("decision-order")
    promise = data.get("public_promise", {})
    if any(promise.get(key) is not True for key in (
        "starting_procedure", "dependence_rule", "route_out_of_book"
    )):
        fail("public-promise")

    supported = data.get("supported_routes", [])
    stopped = data.get("stop_routes", [])
    route_ids = [item.get("id") for item in supported + stopped]
    if len(route_ids) != len(set(route_ids)) or any(not item for item in route_ids):
        fail("duplicate-or-empty-route-id")
    required_supported_ids = {
        "D-DESCRIBE-NUMERIC",
        "D-ASSOCIATE-NUMERIC",
        "D-TWO-INDEPENDENT",
        "D-TWO-PAIRED",
        "D-MULTI-INDEPENDENT",
        "D-CATEGORICAL-ASSOCIATION",
        "D-POPULATION-ESTIMATE",
        "D-LINEAR-REGRESSION",
        "D-READ-BINARY-RESULT",
    }
    if {item["id"] for item in supported} != required_supported_ids:
        fail("supported-route-coverage")
    required_stop_ids = {
        "D-STOP-DEPENDENT",
        "D-STOP-REPEATED",
        "D-STOP-CLUSTERED",
        "D-STOP-TEMPORAL",
        "D-STOP-NETWORK",
        "D-STOP-COMPLEX-SURVEY",
        "D-STOP-BINARY-FIT",
        "D-STOP-CAUSAL",
        "D-STOP-META",
    }
    if {item["id"] for item in stopped} != required_stop_ids:
        fail("dependence-or-scope-stop-coverage")
    source_route_markers = {
        "D-DESCRIBE-NUMERIC": "Opis jedne brojčane varijable",
        "D-ASSOCIATE-NUMERIC": "Povezanost dviju brojčanih varijabli na neovisnim jedinicama",
        "D-TWO-INDEPENDENT": "Razlika brojčanoga ishoda između dviju neovisnih skupina",
        "D-TWO-PAIRED": "Promjena brojčanoga ishoda na istim jedinicama izmjerenima točno dvaput",
        "D-MULTI-INDEPENDENT": "Razlika brojčanoga ishoda između više neovisnih skupina",
        "D-CATEGORICAL-ASSOCIATION": "Povezanost dviju kategoričkih varijabli na neovisnim jedinicama",
        "D-POPULATION-ESTIMATE": "Procjena sredine ili udjela populacije iz uzorka",
        "D-LINEAR-REGRESSION": "Brojčani ishod s više prediktora na neovisnim jedinicama",
        "D-READ-BINARY-RESULT": "Čitanje objavljenoga rezultata za binarni ishod",
    }
    source_stop_markers = {
        "D-STOP-DEPENDENT": "način povezivanja redaka",
        "D-STOP-REPEATED": "Više mjerenja iste jedinice",
        "D-STOP-CLUSTERED": "Učenici u razredima",
        "D-STOP-TEMPORAL": "Vremenski niz",
        "D-STOP-NETWORK": "mrežnim vezama",
        "D-STOP-COMPLEX-SURVEY": "Anketna procjena s težinama",
        "D-STOP-BINARY-FIT": "Procjenjivanje modela za binarni ishod",
        "D-STOP-CAUSAL": "Procjena uzročnoga učinka",
        "D-STOP-META": "Računska sinteza rezultata više studija",
    }
    for route_id, marker in {**source_route_markers, **source_stop_markers}.items():
        if marker not in prose_flat:
            fail(f"source-route-marker={route_id}")
    if next(item for item in supported if item["id"] == "D-TWO-PAIRED")["design"] != (
        "the same unit measured exactly twice or a pair fixed by design"
    ):
        fail("paired-exception-boundary")

    tests = data.get("test_cases", [])
    test_ids = [item.get("id") for item in tests]
    if len(tests) != 20 or len(test_ids) != len(set(test_ids)):
        fail("pathway-test-inventory")
    unknown = sorted({item.get("expected_route") for item in tests} - set(route_ids))
    if unknown:
        fail(f"unknown-expected-routes={','.join(unknown)}")
    expected_cases = {
        "T04": "D-TWO-PAIRED",
        "T05": "D-STOP-REPEATED",
        "T06": "D-STOP-CLUSTERED",
        "T08": "D-STOP-REPEATED",
        "T09": "D-STOP-TEMPORAL",
        "T10": "D-STOP-NETWORK",
        "T14": "D-STOP-COMPLEX-SURVEY",
        "T17": "D-STOP-BINARY-FIT",
        "T18": "D-STOP-CAUSAL",
        "T19": "D-STOP-META",
        "T20": "D-STOP-DEPENDENT",
    }
    actual_cases = {item["id"]: item["expected_route"] for item in tests}
    for case_id, route_id in expected_cases.items():
        if actual_cases.get(case_id) != route_id:
            fail(f"pathway={case_id}")

    links = re.findall(r"\]\(\.\./(chapters/[^)#]+\.qmd)#([^)]+)\)", prose)
    if len(links) < 16:
        fail(f"cross-reference-count={len(links)}")
    for rel, anchor in links:
        target = base / rel
        if not target.is_file():
            fail(f"missing-cross-reference-target={rel}")
        headings = []
        for line in target.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
            if match:
                headings.append(heading_id(match.group(1)))
        if anchor not in headings:
            fail(f"missing-anchor={rel}#{anchor}")

    svg = svg_path.read_text(encoding="utf-8")
    if (
        'viewBox="0 0 800 1120"' not in svg
        or "STANI · IZVAN KNJIGE" not in svg
        or "Objavljeni binarni ishod" not in svg
    ):
        fail("svg-route-contract")
    if re.search(r"#[0-9A-Fa-f]{3,8}\b|font-family\s*=\s*['\"](?!monospace['\"])", svg):
        fail("svg-raw-design-value")
    png_header = png_path.read_bytes()[:24]
    if len(png_header) != 24 or png_header[:8] != b"\x89PNG\r\n\x1a\n":
        fail("png-signature")
    width, height = struct.unpack(">II", png_header[16:24])
    if width < 1600 or height < 2200:
        fail(f"png-resolution={width}x{height}")
    if prose.count("{#tbl-d-") != 3 or "{#fig-d-stablo" not in prose:
        fail("print-reference-spread-markers")

    return {
        "supported": len(supported),
        "stopped": len(stopped),
        "tests": len(tests),
        "xrefs": len(set(links)),
        "png_width": width,
        "png_height": height,
    }


def main() -> None:
    primary = validate(ROOT)
    source_text = (ROOT / SOURCE).read_text(encoding="utf-8")
    linked = {Path(rel) for rel, _ in re.findall(
        r"\]\(\.\./(chapters/[^)#]+\.qmd)#([^)]+)\)", source_text
    )}
    declared = {SOURCE, ROUTE, SVG, PNG, *linked}
    with tempfile.TemporaryDirectory(prefix="appendix-d-") as tmp:
        stage = Path(tmp)
        for rel in declared:
            destination = stage / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, destination)
        isolated = validate(stage)
    if isolated != primary:
        fail("isolated-clean-pathway-disagrees")
    print(
        "APPENDIX_D_CHECK_OK "
        f"routes={primary['supported']} "
        f"stops={primary['stopped']} "
        f"pathways={primary['tests']}/20 "
        "dependence=verified "
        "scope_stops=verified "
        f"xrefs={primary['xrefs']} "
        "clean_pathway=verified "
        f"png={primary['png_width']}x{primary['png_height']} "
        "print_spread=present"
    )


if __name__ == "__main__":
    main()
