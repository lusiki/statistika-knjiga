#!/usr/bin/env python3
"""Verify Appendix E registry parity, routes, clean regeneration, and proof inputs."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BUILDER = Path("scripts/build-terminology-views.py")
CONVENTIONS = Path("bookwright_plugin/bookwright/shared/conventions.json")
CONVENTIONS_SCHEMA = Path(
    "bookwright_plugin/bookwright/shared/schemas/conventions.schema.json"
)
CONCEPT_LEDGER = Path("bookwright_plugin/bookwright/shared/concept-ledger.json")
CONCEPT_GRAPH = Path("data/concept-graph.json")
APPENDIX = Path("dodaci/e-rjecnik.qmd")
GLOSSARY = Path("pojmovnik.qmd")
ROUTE = Path("config/appendix-e-terminology-route.json")
BEGIN = "<!-- BEGIN GENERATED TERMINOLOGY ROUTES -->"
END = "<!-- END GENERATED TERMINOLOGY ROUTES -->"

FIXTURES = (
    "superseded_as_accepted",
    "departure_dropped",
    "stable_id_renamed",
)


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(base: Path, relative: Path) -> Any:
    path = base / relative
    if not path.is_file():
        fail(f"missing={relative.as_posix()}")
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def fold(value: str) -> str:
    return " ".join(value.casefold().split())


def display_sentence(value: object) -> str:
    return re.sub(r"\s+([,.;:!?])", r"\1", str(value).strip())


def generated_block(text: str) -> str:
    match = re.search(rf"{re.escape(BEGIN)}.*?{re.escape(END)}", text, re.S)
    if not match:
        fail("generated terminology route block is missing")
    return match.group(0)


def source_has_definition(path: Path, identifier: str) -> bool:
    pattern = rf"^:::+\s*\{{#def-{re.escape(identifier)}\}}"
    return re.search(pattern, path.read_text(encoding="utf-8"), re.M) is not None


def validate(base: Path, fixture: str = "") -> dict[str, int | str]:
    conventions = load_json(base, CONVENTIONS)
    schema = load_json(base, CONVENTIONS_SCHEMA)
    ledger = load_json(base, CONCEPT_LEDGER)
    graph = load_json(base, CONCEPT_GRAPH)
    artifact = load_json(base, ROUTE)
    appendix_path = base / APPENDIX
    glossary_path = base / GLOSSARY
    for path in (appendix_path, glossary_path):
        if not path.is_file():
            fail(f"missing={path.relative_to(base).as_posix()}")
    appendix = appendix_path.read_text(encoding="utf-8")
    glossary = glossary_path.read_text(encoding="utf-8")
    registry = conventions.get("terminology_registry")
    if not isinstance(registry, dict):
        fail("terminology_registry is missing")
    if "terminology_registry" not in schema.get("properties", {}):
        fail("conventions schema does not admit terminology_registry")

    artifact = copy.deepcopy(artifact)
    if fixture == "superseded_as_accepted":
        artifact["superseded_routes"][0]["status"] = "accepted_synonym"
    elif fixture == "departure_dropped":
        artifact["deliberate_departures"].pop()
    elif fixture == "stable_id_renamed":
        artifact["stable_identifiers"][0]["id"] += "-renamed"
    elif fixture:
        fail(f"unknown negative fixture={fixture}")

    if artifact.get("schema_version") != 1 or artifact.get("packet") != "P5-E":
        fail("route artifact identity")
    canonical = artifact.get("canonical_sources", {})
    registry_source = canonical.get("terminology_registry", {})
    if registry_source.get("path") != f"{CONVENTIONS.as_posix()}#terminology_registry":
        fail("route artifact registry path")
    if registry_source.get("sha256") != canonical_hash(registry):
        fail("route artifact registry hash is stale")
    if registry_source.get("file_sha256") != sha256_file(base / CONVENTIONS):
        fail("route artifact conventions hash is stale")
    if canonical.get("concept_ledger", {}).get("sha256") != sha256_file(base / CONCEPT_LEDGER):
        fail("route artifact concept-ledger hash is stale")
    if canonical.get("concept_graph", {}).get("sha256") != sha256_file(base / CONCEPT_GRAPH):
        fail("route artifact concept-graph hash is stale")

    promise = artifact.get("public_promise", {})
    expected_promise = {
        "canonical_term_leads": True,
        "superseded_forms_are_not_accepted_synonyms": True,
        "departure_reasons_are_reader_visible": True,
        "independent_terminology_review_claimed": False,
    }
    if promise != expected_promise:
        fail("public promise disagrees with the registry boundary")

    expected_superseded = [
        {**entry, "status": "superseded_not_accepted_synonym"}
        for entry in registry.get("superseded_forms", [])
    ]
    if artifact.get("superseded_routes") != expected_superseded:
        fail("superseded routes disagree with terminology_registry")
    if artifact.get("deliberate_departures") != registry.get("deliberate_departures"):
        fail("deliberate departures disagree with terminology_registry")
    if artifact.get("meaning_rules") != registry.get("meaning_rules"):
        fail("meaning rules disagree with terminology_registry")
    if artifact.get("stable_identifiers") != registry.get("stable_identifiers"):
        fail("stable identifiers disagree with terminology_registry")

    review = artifact.get("review_route", {})
    if review.get("independent_review_obtained") is not False:
        fail("independent terminology review is falsely claimed as obtained")
    if review.get("independent_review_claim_permitted") is not False:
        fail("independent terminology review claim is falsely permitted")
    disclosure = (
        "Neovisna terminološka\nrecenzija nije pribavljena i knjiga je ne tvrdi."
    )
    if disclosure not in generated_block(appendix):
        fail("Appendix E lacks the exact independent-review boundary")

    appendix_block = generated_block(appendix)
    glossary_block = generated_block(glossary)
    if appendix_block != glossary_block:
        fail("reader-visible terminology route blocks disagree")
    view_records = {entry.get("path"): entry for entry in artifact.get("generated_views", [])}
    if set(view_records) != {APPENDIX.as_posix(), GLOSSARY.as_posix()}:
        fail("route artifact does not name exactly both glossary views")
    for relative, source in ((APPENDIX, appendix_path), (GLOSSARY, glossary_path)):
        if view_records[relative.as_posix()].get("sha256") != sha256_file(source):
            fail(f"generated view hash is stale={relative.as_posix()}")

    if "djelomični nacrt" in appendix.casefold() or "nakon ratifikacije kralježnice" in appendix.casefold():
        fail("stale partial-draft marker remains")
    if "Nijedan od njih nije prihvaćen sinonim" not in appendix_block:
        fail("superseded forms are not clearly excluded as accepted synonyms")
    for entry in expected_superseded:
        row_parts = (entry["form"], entry["canonical"], entry["reason"])
        if not all(part in appendix_block for part in row_parts):
            fail(f"superseded route is not reader-visible={entry['form']}")
    for entry in registry.get("deliberate_departures", []):
        if not all(entry[key] in appendix_block for key in ("form", "en", "reason")):
            fail(f"departure is not reader-visible={entry['form']}")
    for entry in registry.get("meaning_rules", []):
        if not all(entry[key] in appendix_block for key in ("term", "reserved_for", "forbidden_use", "reason")):
            fail(f"meaning rule is not reader-visible={entry['term']}")

    routes = artifact.get("concept_routes", [])
    nodes = graph.get("nodes", [])
    concepts = ledger.get("concepts", [])
    if len(routes) != len(nodes) or len(routes) != len(concepts):
        fail("concept route counts disagree")
    node_by_id = {entry.get("id"): entry for entry in nodes}
    ledger_terms = {fold(entry["term"]): entry for entry in concepts}
    if len(node_by_id) != len(nodes) or len(ledger_terms) != len(concepts):
        fail("concept source repeats an identity")
    for route in routes:
        identifier = route.get("id")
        if identifier not in node_by_id:
            fail(f"concept route has no graph node={identifier}")
        node = node_by_id[identifier]
        if fold(route.get("term", "")) not in ledger_terms:
            fail(f"concept route has no ledger term={route.get('term')}")
        target = base / route.get("chapter", "")
        if not target.is_file():
            fail(f"concept route target is missing={route.get('chapter')}")
        if route.get("anchor") != f"def-{identifier}":
            fail(f"concept route anchor disagrees={identifier}")
        if not source_has_definition(target, identifier):
            fail(f"stable definition anchor is missing={route.get('chapter')}#def-{identifier}")
        link = f"../{route['chapter']}#{route['anchor']}"
        if link not in appendix:
            fail(f"Appendix E lacks concept cross-reference={link}")
        if route.get("definition") != display_sentence(node.get("firstSentence", "")):
            fail(f"definition route disagrees with concept graph={identifier}")

    stable = {entry["id"]: entry for entry in registry.get("stable_identifiers", [])}
    for identifier, entry in stable.items():
        if identifier not in node_by_id:
            fail(f"stable identifier is missing from graph={identifier}")
        if fold(node_by_id[identifier]["term"]) != fold(entry["canonical_term"]):
            fail(f"stable identifier changed term={identifier}")
    if '#def-${n.id}' not in glossary or 'FileAttachment("data/concept-graph.json")' not in glossary:
        fail("Pojmovnik no longer uses stable concept-graph routes")

    edges = graph.get("edges", [])
    edge_keys: set[tuple[str, str]] = set()
    for edge in edges:
        source = edge.get("source")
        target = edge.get("target")
        if source not in node_by_id or target not in node_by_id or source == target:
            fail(f"invalid graph edge={edge}")
        key = tuple(sorted((source, target)))
        if key in edge_keys:
            fail(f"duplicate graph edge={key}")
        edge_keys.add(key)

    counts = artifact.get("counts", {})
    expected_counts = {
        "concepts": len(routes),
        "canonical_gate_forms": len(registry.get("canonical_forms", [])),
        "superseded_forms": len(expected_superseded),
        "deliberate_departures": len(registry.get("deliberate_departures", [])),
        "meaning_rules": len(registry.get("meaning_rules", [])),
        "stable_identifiers": len(stable),
    }
    if counts != expected_counts:
        fail("route artifact counts disagree")
    return {
        **expected_counts,
        "edges": len(edges),
        "route_block_sha256": hashlib.sha256(appendix_block.encode("utf-8")).hexdigest(),
    }


def copy_into(stage: Path, relative: Path) -> None:
    destination = stage / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / relative, destination)


def clean_regeneration(expected: dict[str, int | str]) -> None:
    declared = (
        BUILDER,
        CONVENTIONS,
        CONVENTIONS_SCHEMA,
        CONCEPT_LEDGER,
        CONCEPT_GRAPH,
        APPENDIX,
        GLOSSARY,
    )
    with tempfile.TemporaryDirectory(prefix="appendix-e-clean-") as directory:
        stage = Path(directory)
        for relative in declared:
            copy_into(stage, relative)
        for path in sorted((ROOT / "chapters").glob("*.qmd")):
            copy_into(stage, path.relative_to(ROOT))
        result = subprocess.run(
            [sys.executable, str(stage / BUILDER), "--root", str(stage)],
            cwd=stage,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode:
            fail(f"clean generator failed={result.stdout.strip()}")
        isolated = validate(stage)
        if isolated != expected:
            fail("isolated clean regeneration disagrees")
        for relative in (APPENDIX, GLOSSARY, ROUTE):
            if (stage / relative).read_bytes() != (ROOT / relative).read_bytes():
                fail(f"clean regeneration is not byte-identical={relative.as_posix()}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-clean", action="store_true")
    args = parser.parse_args()
    fixture = os.environ.get("APPENDIX_E_NEGATIVE_FIXTURE", "")
    try:
        result = validate(ROOT, fixture=fixture)
        if not args.skip_clean and not fixture:
            clean_regeneration(result)
        print(
            "APPENDIX_E_CHECK_OK "
            f"concepts={result['concepts']} edges={result['edges']} "
            f"superseded={result['superseded_forms']} "
            f"departures={result['deliberate_departures']} "
            f"rules={result['meaning_rules']} stable_ids={result['stable_identifiers']} "
            "views=2/2 xrefs=verified registry_parity=verified "
            "clean_pathway=verified print_source=present independent_review_claim=false"
        )
        return 0
    except (AssertionError, OSError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"APPENDIX_E_CHECK_FAILED {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
