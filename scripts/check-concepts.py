#!/usr/bin/env python3
"""Fail-closed definition, concept-ledger, glossary, and graph integrity check."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


CHECKOUT_ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = CHECKOUT_ROOT / "bookwright_plugin/bookwright/scripts/run_rscript.py"
GRAPH_BUILDER = CHECKOUT_ROOT / "R/build-concept-graph.R"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r_env import r_subprocess_env  # noqa: E402


def normalized_term(value: str) -> str:
    return " ".join(value.casefold().split())


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def strip_html_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def extract_definitions(root: Path) -> list[dict[str, str]]:
    definitions: list[dict[str, str]] = []
    for path in sorted((root / "chapters").glob("*.qmd")):
        lines = strip_html_comments(path.read_text(encoding="utf-8")).splitlines()
        in_code = False
        fence = ""
        index = 0
        while index < len(lines):
            line = lines[index]
            candidate = re.match(r"^\s*(`{3,}|~{3,})", line)
            if candidate and not in_code:
                in_code = True
                fence = candidate.group(1)
                index += 1
                continue
            if in_code:
                if re.match(rf"^\s*{re.escape(fence[0])}{{{len(fence)},}}\s*$", line):
                    in_code = False
                    fence = ""
                index += 1
                continue
            opening = re.match(r"^:::+\s*\{#def-([^}]+)\}", line)
            if not opening:
                index += 1
                continue
            slug = opening.group(1)
            depth = 1
            body: list[str] = []
            index += 1
            while index < len(lines) and depth:
                current = lines[index]
                if re.match(r"^:::+\s*\{", current):
                    depth += 1
                elif re.match(r"^:::+\s*$", current):
                    depth -= 1
                    if depth == 0:
                        index += 1
                        break
                if depth:
                    body.append(current)
                index += 1
            if depth:
                raise ValueError(f"{path.name}: unclosed definition #{slug}")
            block = " ".join(body)
            bold = re.search(r"\*\*([^*]+)\*\*", block)
            if not bold:
                raise ValueError(f"{path.name}: definition #{slug} has no bold canonical term")
            clean = re.sub(r"\[[^]]*@[^]]*\]", "", block)
            clean = re.sub(r"@[A-Za-z0-9_:.-]+", "", clean)
            clean = re.sub(r"\*\*|\*", "", clean)
            clean = " ".join(clean.split())
            if not clean:
                raise ValueError(f"{path.name}: definition #{slug} is empty")
            definitions.append(
                {
                    "id": slug,
                    "term": bold.group(1).strip(),
                    "chapter": path.stem,
                }
            )
    return definitions


def validate_unique(records: list[dict[str, str]], field: str, label: str) -> None:
    values = [normalized_term(record[field]) for record in records]
    duplicates = sorted({value for value in values if values.count(value) > 1})
    if duplicates:
        raise ValueError(f"duplicate {label}: {duplicates}")


def concept_ledger_state(root: Path, definitions: list[dict[str, str]]) -> dict[str, object]:
    ledger_path = root / "bookwright_plugin/bookwright/shared/concept-ledger.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    concepts = ledger.get("concepts")
    notation = ledger.get("notation")
    if not isinstance(concepts, list) or not isinstance(notation, list):
        raise ValueError("concept ledger must contain concepts and notation arrays")
    validate_unique(concepts, "term", "concept-ledger term")
    symbols = [entry.get("symbol", "") for entry in notation]
    if any(not symbol for symbol in symbols):
        raise ValueError("notation entry without a symbol")
    duplicate_symbols = sorted({symbol for symbol in symbols if symbols.count(symbol) > 1})
    if duplicate_symbols:
        raise ValueError(f"duplicate notation symbols: {duplicate_symbols}")

    chapter_ids = {path.stem for path in (root / "chapters").glob("*.qmd")}
    for entry in [*concepts, *notation]:
        chapter = entry.get("introduced_in")
        if chapter not in chapter_ids:
            raise ValueError(f"ledger entry points to unknown chapter: {entry}")
    concept_terms = {normalized_term(entry["term"]) for entry in concepts}
    for entry in notation:
        concept = entry.get("concept")
        if concept and normalized_term(concept) not in concept_terms:
            raise ValueError(f"notation references unknown concept {concept!r}")

    source_pairs = sorted(
        (normalized_term(entry["term"]), entry["chapter"]) for entry in definitions
    )
    ledger_pairs = sorted(
        (normalized_term(entry["term"]), entry["introduced_in"]) for entry in concepts
    )
    source_set = set(source_pairs)
    ledger_set = set(ledger_pairs)
    mismatch = {
        "source_only": sorted(source_set - ledger_set),
        "ledger_only": sorted(ledger_set - source_set),
    }
    return {
        "register_item": "R04-TERMS-concept-regeneration",
        "retire_in_packet": "P2-TERMS",
        "source_terms_sha256": canonical_hash(source_pairs),
        "ledger_terms_sha256": canonical_hash(ledger_pairs),
        "mismatch_sha256": canonical_hash(mismatch),
        "mismatch_count": len(mismatch["source_only"]) + len(mismatch["ledger_only"]),
    }


def normalized_graph(graph: dict[str, object]) -> dict[str, object]:
    clean = dict(graph)
    clean.pop("generated", None)
    return clean


def build_fresh_graph(root: Path) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="statistika-concepts-") as directory:
        work = Path(directory).resolve()
        temp_root = Path(tempfile.gettempdir()).resolve()
        if temp_root not in work.parents:
            raise RuntimeError(f"unsafe temporary graph path: {work}")
        shutil.copy2(root / "_quarto.yml", work / "_quarto.yml")
        shutil.copytree(root / "chapters", work / "chapters")
        (work / "data").mkdir()
        result = subprocess.run(
            [sys.executable, str(LAUNCHER), str(GRAPH_BUILDER)],
            cwd=work,
            env=r_subprocess_env(root),
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        print(result.stdout, end="")
        if result.returncode:
            raise RuntimeError(f"build-concept-graph.R exited {result.returncode}")
        return json.loads((work / "data/concept-graph.json").read_text(encoding="utf-8"))


def graph_state(root: Path, definitions: list[dict[str, str]]) -> dict[str, object]:
    committed = json.loads((root / "data/concept-graph.json").read_text(encoding="utf-8"))
    nodes = committed.get("nodes")
    edges = committed.get("edges")
    if not isinstance(nodes, list) or not isinstance(edges, list):
        raise ValueError("concept graph must contain node and edge arrays")
    node_ids = [node.get("id") for node in nodes]
    if any(not node_id for node_id in node_ids) or len(node_ids) != len(set(node_ids)):
        raise ValueError("concept graph has missing or duplicate node IDs")
    definition_ids = {entry["id"] for entry in definitions}
    if set(node_ids) != definition_ids:
        raise ValueError("concept graph node IDs do not equal live #def- IDs")
    for edge in edges:
        if edge.get("source") not in definition_ids or edge.get("target") not in definition_ids:
            raise ValueError(f"concept graph edge references an unknown node: {edge}")
        if edge.get("source") == edge.get("target"):
            raise ValueError(f"concept graph contains a self-edge: {edge}")

    glossary = (root / "pojmovnik.qmd").read_text(encoding="utf-8")
    if 'FileAttachment("data/concept-graph.json")' not in glossary:
        raise ValueError("pojmovnik.qmd does not consume the canonical concept graph")
    if "#def-${n.id}" not in glossary:
        raise ValueError("pojmovnik.qmd no longer links nodes to their #def- anchors")

    fresh = build_fresh_graph(root)
    committed_clean = normalized_graph(committed)
    fresh_clean = normalized_graph(fresh)
    return {
        "register_item": "R04-TERMS-concept-regeneration",
        "retire_in_packet": "P2-TERMS",
        "committed_sha256": canonical_hash(committed_clean),
        "regenerated_sha256": canonical_hash(fresh_clean),
        "fresh": committed_clean == fresh_clean,
        "committed_nodes": len(nodes),
        "regenerated_nodes": len(fresh.get("nodes", [])),
        "committed_edges": len(edges),
        "regenerated_edges": len(fresh.get("edges", [])),
    }


def compare_debt(actual: dict[str, object], declared: object, label: str) -> None:
    is_clean = actual.get("mismatch_count", 0) == 0 if label == "concept_ledger" else actual.get("fresh") is True
    if is_clean:
        if declared is not None:
            raise ValueError(f"{label} debt is stale and must be removed")
        return
    if not isinstance(declared, dict):
        raise ValueError(f"{label} has undeclared integrity debt: {actual}")
    if declared != actual:
        raise ValueError(f"{label} debt changed; declared={declared}, actual={actual}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=CHECKOUT_ROOT)
    parser.add_argument("--print-debt", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        definitions = extract_definitions(root)
        if not definitions:
            raise ValueError("no live #def- blocks found")
        validate_unique(definitions, "id", "definition IDs")
        validate_unique(definitions, "term", "definition terms")
        ledger_state = concept_ledger_state(root, definitions)
        graph = graph_state(root, definitions)
        if args.print_debt:
            print(json.dumps({"concept_ledger": ledger_state, "concept_graph": graph}, ensure_ascii=False, indent=2))
            return 0
        debt = json.loads((root / "scripts/integrity-debt.json").read_text(encoding="utf-8"))
        compare_debt(ledger_state, debt.get("concept_ledger"), "concept_ledger")
        compare_debt(graph, debt.get("concept_graph"), "concept_graph")
        print(
            "CONCEPT_INTEGRITY_OK "
            f"definitions={len(definitions)} ledger_debt={ledger_state['mismatch_count']} "
            f"graph_fresh={str(graph['fresh']).lower()} graph_nodes={graph['committed_nodes']}"
        )
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError, RuntimeError) as error:
        print(f"concept integrity: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
