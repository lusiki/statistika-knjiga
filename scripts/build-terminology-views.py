#!/usr/bin/env python3
"""Generate the two glossary views and Appendix E terminology route artifact.

The terminology registry is the sole source for variant, departure, meaning,
stable-identifier, and review-route decisions. The concept ledger supplies
English equivalents, while the concept graph supplies the live definition
sentence and its stable #def- route.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from typing import Any


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
CONVENTIONS = Path("bookwright_plugin/bookwright/shared/conventions.json")
CONVENTIONS_SCHEMA = Path(
    "bookwright_plugin/bookwright/shared/schemas/conventions.schema.json"
)
CONCEPT_LEDGER = Path("bookwright_plugin/bookwright/shared/concept-ledger.json")
CONCEPT_GRAPH = Path("data/concept-graph.json")
APPENDIX = Path("dodaci/e-rjecnik.qmd")
GLOSSARY = Path("pojmovnik.qmd")
ROUTE_ARTIFACT = Path("config/appendix-e-terminology-route.json")

BEGIN_ROUTES = "<!-- BEGIN GENERATED TERMINOLOGY ROUTES -->"
END_ROUTES = "<!-- END GENERATED TERMINOLOGY ROUTES -->"


def load_json(root: Path, relative: Path) -> Any:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(payload)


def fold(value: str) -> str:
    return " ".join(value.casefold().split())


def display_sentence(value: object) -> str:
    """Remove extraction whitespace without altering the definition wording."""
    return re.sub(r"\s+([,.;:!?])", r"\1", str(value).strip())


def table_cell(value: object) -> str:
    text = re.sub(r"\s+", " ", str(value)).strip()
    return text.replace("|", "\\|")


def require_list(registry: dict[str, Any], key: str) -> list[dict[str, Any]]:
    value = registry.get(key)
    if not isinstance(value, list) or not value:
        raise ValueError(f"terminology_registry.{key} must be a non-empty array")
    if not all(isinstance(entry, dict) for entry in value):
        raise ValueError(f"terminology_registry.{key} must contain objects")
    return value


def render_routes(registry: dict[str, Any]) -> str:
    superseded = require_list(registry, "superseded_forms")
    departures = require_list(registry, "deliberate_departures")
    meaning_rules = require_list(registry, "meaning_rules")
    review = registry.get("review_route", {})
    if not isinstance(review, dict):
        raise ValueError("terminology_registry.review_route must be an object")
    if review.get("independent_review_obtained") is not False:
        raise ValueError("the registry must record that independent review was not obtained")
    if review.get("independent_review_claim_permitted") is not False:
        raise ValueError("the registry must forbid an independent-review claim")

    lines = [
        BEGIN_ROUTES,
        "",
        "## Uputnice za druge oblike {#sec-terminologija-uputnice}",
        "",
        "Oblici u sljedećoj tablici služe prepoznavanju nazivlja koje se može",
        "susresti u drugoj literaturi. Nijedan od njih nije prihvaćen sinonim",
        "kanonskoga oblika u ovoj knjizi i ne rabi se kao zamjenjiv naziv.",
        "",
        "| Oblik koji možete susresti | Kanonski oblik u knjizi | Dopuštena iznimka | Razlog |",
        "|---|---|---|---|",
    ]
    for entry in superseded:
        permitted = entry.get("permitted_only_in", "nema")
        lines.append(
            "| {form} | {canonical} | {permitted} | {reason} |".format(
                form=table_cell(entry["form"]),
                canonical=table_cell(entry["canonical"]),
                permitted=table_cell(permitted),
                reason=table_cell(entry["reason"]),
            )
        )
    lines.extend(
        [
            "",
            ": Uputnice prema kanonskim oblicima u knjizi. Izrada autora. {#tbl-terminologija-uputnice}",
            "",
            "## Namjerna odstupanja {#sec-terminologija-odstupanja}",
            "",
            "Tri su oblika odabrana namjerno. Razlog uz svaki oblik objašnjava",
            "zašto knjiga ne preuzima drugu moguću hrvatsku konvenciju.",
            "",
            "| Oblik u knjizi | Engleski termin | Razlog |",
            "|---|---|---|",
        ]
    )
    for entry in departures:
        lines.append(
            "| {form} | *{english}* | {reason} |".format(
                form=table_cell(entry["form"]),
                english=table_cell(entry["en"]),
                reason=table_cell(entry["reason"]),
            )
        )
    lines.extend(
        [
            "",
            ": Namjerna odstupanja od drugih mogućih hrvatskih oblika. Izrada autora. {#tbl-terminologija-odstupanja}",
            "",
            "## Razdvojena značenja {#sec-terminologija-znacenja}",
            "",
            "Ista riječ može upućivati na različite statističke ideje. Ova pravila",
            "čuvaju granicu značenja ondje gdje bi kratki oblik spojio nespojive",
            "veličine ili postupke.",
            "",
            "| Pojam | Značenje u knjizi | Ne rabiti za | Razlog |",
            "|---|---|---|---|",
        ]
    )
    for rule in meaning_rules:
        lines.append(
            "| {term} | {reserved} | {forbidden} | {reason} |".format(
                term=table_cell(rule["term"]),
                reserved=table_cell(rule["reserved_for"]),
                forbidden=table_cell(rule["forbidden_use"]),
                reason=table_cell(rule["reason"]),
            )
        )
    owner = table_cell(review.get("owner", "autor i urednik"))
    lines.extend(
        [
            "",
            ": Granice značenja za sporne oblike. Izrada autora. {#tbl-terminologija-znacenja}",
            "",
            "## Urednička odgovornost {#sec-terminologija-odgovornost}",
            "",
            f"Za kanonsko nazivlje odgovara {owner}. Neovisna terminološka",
            "recenzija nije pribavljena i knjiga je ne tvrdi.",
            "",
            END_ROUTES,
        ]
    )
    return "\n".join(lines)


def render_concept_list(
    ledger: dict[str, Any], graph: dict[str, Any]
) -> tuple[str, list[dict[str, str]]]:
    concepts = ledger.get("concepts")
    nodes = graph.get("nodes")
    if not isinstance(concepts, list) or not isinstance(nodes, list):
        raise ValueError("concept ledger and graph must contain arrays")
    ledger_by_term = {fold(entry["term"]): entry for entry in concepts}
    if len(ledger_by_term) != len(concepts):
        raise ValueError("concept ledger repeats a canonical term")
    if len(nodes) != len(concepts):
        raise ValueError("concept graph and ledger counts disagree")

    lines = ["::: {.terminology-list .terminology-list--glossary}"]
    routes: list[dict[str, str]] = []
    for node in nodes:
        term_key = fold(node["term"])
        if term_key not in ledger_by_term:
            raise ValueError(f"concept graph term is absent from ledger: {node['term']}")
        entry = ledger_by_term[term_key]
        chapter = Path(node["chapter"])
        if chapter.stem != entry["introduced_in"]:
            raise ValueError(f"concept route disagrees for {node['term']}")
        anchor = f"def-{node['id']}"
        href = f"../{chapter.as_posix()}#{anchor}"
        english = entry.get("english_term")
        if not isinstance(english, str) or not english.strip():
            raise ValueError(f"concept lacks an English term: {node['term']}")
        sentence = display_sentence(node.get("firstSentence", ""))
        if not sentence:
            raise ValueError(f"concept graph node lacks a definition: {node['term']}")
        chapter_title = str(node["chapterTitle"]).replace("—", "&mdash;")
        lines.extend(
            [
                f"<!-- GENERATED CONCEPT {node['id']} -->",
                f"[{node['term']}]({href}){{.terminology-list__hr lang=\"hr\"}}",
                f":   [*{english}*]{{.terminology-list__en lang=\"en\"}}",
                f"    [Poglavlje · {chapter_title}]{{.terminology-list__chapter}}",
                "",
                f"    {sentence}",
                "",
            ]
        )
        routes.append(
            {
                "id": str(node["id"]),
                "term": str(node["term"]),
                "english_term": english,
                "chapter": chapter.as_posix(),
                "chapter_title": str(node["chapterTitle"]),
                "anchor": anchor,
                "definition": sentence,
            }
        )
    lines.append(":::")
    return "\n".join(lines), routes


def render_appendix(concepts: str, routes: str, count: int) -> str:
    return "\n".join(
        [
            "---",
            'title: "Rječnik pojmova"',
            "---",
            "",
            "<!-- =====================================================================",
            "  GENERATED CANONICAL VIEW",
            "  Sources: conventions.json#terminology_registry, concept-ledger.json",
            "           and data/concept-graph.json",
            "  Regenerate: python scripts/build-terminology-views.py",
            "  Do not edit generated term, variant, departure, or rationale rows by hand.",
            "===================================================================== -->",
            "",
            "Rječnik uparuje hrvatske nazive s engleskim terminima pod kojima će ih",
            "čitatelj najčešće pronaći u međunarodnoj literaturi. Kanonski hrvatski",
            "oblik vodi, a poveznica uz svaki od {count} formalno definiranih pojmova".format(
                count=count
            ),
            "vodi do definicijskoga mjesta u knjizi. Popis nastaje iz istih",
            "definicijskih blokova i registara iz kojih nastaje mrežni Pojmovnik.",
            "",
            "## Kanonski pojmovi {#sec-rjecnik-kanonski-pojmovi}",
            "",
            concepts,
            "",
            routes,
            "",
        ]
    )


def replace_or_append_routes(source: str, routes: str) -> str:
    pattern = re.compile(
        rf"{re.escape(BEGIN_ROUTES)}.*?{re.escape(END_ROUTES)}", re.S
    )
    if pattern.search(source):
        result = pattern.sub(routes, source)
    else:
        result = source.rstrip() + "\n\n" + routes + "\n"
    return result.rstrip() + "\n"


def build(root: Path) -> dict[str, Any]:
    conventions = load_json(root, CONVENTIONS)
    schema = load_json(root, CONVENTIONS_SCHEMA)
    ledger = load_json(root, CONCEPT_LEDGER)
    graph = load_json(root, CONCEPT_GRAPH)
    registry = conventions.get("terminology_registry")
    if not isinstance(registry, dict):
        raise ValueError("conventions.json has no terminology_registry")
    if "terminology_registry" not in schema.get("properties", {}):
        raise ValueError("conventions schema does not admit terminology_registry")

    route_block = render_routes(registry)
    concept_block, concept_routes = render_concept_list(ledger, graph)
    appendix_text = render_appendix(concept_block, route_block, len(concept_routes))
    glossary_path = root / GLOSSARY
    glossary_source = glossary_path.read_text(encoding="utf-8")
    glossary_text = replace_or_append_routes(glossary_source, route_block)

    appendix_path = root / APPENDIX
    appendix_path.parent.mkdir(parents=True, exist_ok=True)
    appendix_path.write_text(appendix_text, encoding="utf-8", newline="\n")
    glossary_path.write_text(glossary_text, encoding="utf-8", newline="\n")

    superseded = [
        {**entry, "status": "superseded_not_accepted_synonym"}
        for entry in require_list(registry, "superseded_forms")
    ]
    artifact = {
        "schema_version": 1,
        "packet": "P5-E",
        "canonical_sources": {
            "terminology_registry": {
                "path": f"{CONVENTIONS.as_posix()}#terminology_registry",
                "sha256": canonical_hash(registry),
                "file_sha256": sha256_file(root / CONVENTIONS),
            },
            "concept_ledger": {
                "path": CONCEPT_LEDGER.as_posix(),
                "sha256": sha256_file(root / CONCEPT_LEDGER),
            },
            "concept_graph": {
                "path": CONCEPT_GRAPH.as_posix(),
                "sha256": sha256_file(root / CONCEPT_GRAPH),
            },
        },
        "public_promise": {
            "canonical_term_leads": True,
            "superseded_forms_are_not_accepted_synonyms": True,
            "departure_reasons_are_reader_visible": True,
            "independent_terminology_review_claimed": False,
        },
        "counts": {
            "concepts": len(concept_routes),
            "canonical_gate_forms": len(registry.get("canonical_forms", [])),
            "superseded_forms": len(superseded),
            "deliberate_departures": len(registry.get("deliberate_departures", [])),
            "meaning_rules": len(registry.get("meaning_rules", [])),
            "stable_identifiers": len(registry.get("stable_identifiers", [])),
        },
        "generated_views": [
            {
                "path": APPENDIX.as_posix(),
                "sha256": sha256_file(appendix_path),
                "concept_entries": len(concept_routes),
                "terminology_routes_sha256": sha256_bytes(route_block.encode("utf-8")),
            },
            {
                "path": GLOSSARY.as_posix(),
                "sha256": sha256_file(glossary_path),
                "concept_entries": len(graph.get("nodes", [])),
                "terminology_routes_sha256": sha256_bytes(route_block.encode("utf-8")),
            },
        ],
        "concept_routes": concept_routes,
        "superseded_routes": superseded,
        "deliberate_departures": registry["deliberate_departures"],
        "meaning_rules": registry["meaning_rules"],
        "stable_identifiers": registry["stable_identifiers"],
        "review_route": {
            "reviewer": registry["review_route"]["reviewer"],
            "owner": registry["review_route"]["owner"],
            "independent_review_obtained": False,
            "independent_review_claim_permitted": False,
        },
    }
    route_path = root / ROUTE_ARTIFACT
    route_path.parent.mkdir(parents=True, exist_ok=True)
    route_path.write_text(
        json.dumps(artifact, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return artifact


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        artifact = build(root)
        counts = artifact["counts"]
        print(
            "TERMINOLOGY_VIEWS_BUILT "
            f"concepts={counts['concepts']} "
            f"superseded={counts['superseded_forms']} "
            f"departures={counts['deliberate_departures']} "
            f"rules={counts['meaning_rules']} views=2 artifact=1"
        )
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"TERMINOLOGY_VIEWS_BUILD_FAILED {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
