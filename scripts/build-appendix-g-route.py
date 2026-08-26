#!/usr/bin/env python3
"""Build the Appendix G numeracy and first-use route artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DECISION = Path("notes/reports/g-a2d-policy-decisions-2026-08-04.md")
INVENTORY = Path("config/book-inventory.json")
INVENTORY_GENERATOR = Path("scripts/book_inventory.py")
QUARTO = Path("_quarto.yml")
RUNTIME_ROUTES = Path("styles/book-include.html")
APPENDIX = Path("dodaci/g-numericki-podsjetnik.qmd")
STYLE = Path("STYLE.md")
WIDGETS = Path("data/widgets.json")
REFERENCES = Path("references.bib")
ARTIFACT = Path("config/appendix-g-numeracy-route.json")

TOPICS = (
    {
        "id": "percentages_percentage_points",
        "title": "Postotci i postotni bodovi",
        "decision_phrase": "postotke i postotne bodove",
        "appendix_anchor": "sec-ag-postotci-postotni-bodovi",
        "first_use_path": "chapters/01-zasto-statistika.qmd",
        "reminder_anchor": "podsjetnik-postotci-postotni-bodovi",
        "first_use_marker": "Bez imenovanoga nazivnika postotak nema potpuno značenje.",
    },
    {
        "id": "proportions_rates",
        "title": "Udjeli i stope",
        "decision_phrase": "udjele i stope",
        "appendix_anchor": "sec-ag-udjeli-stope",
        "first_use_path": "chapters/01-zasto-statistika.qmd",
        "reminder_anchor": "podsjetnik-udjeli-stope",
        "first_use_marker": "diskriminirali žene",
    },
    {
        "id": "slope",
        "title": "Nagib",
        "decision_phrase": "nagib",
        "appendix_anchor": "sec-ag-nagib",
        "first_use_path": "chapters/16-regresija.qmd",
        "reminder_anchor": "podsjetnik-nagib",
        "first_use_marker": "rast sažima jednim nagibom",
    },
    {
        "id": "logarithmic_scale",
        "title": "Logaritamska skala",
        "decision_phrase": "logaritamsku skalu",
        "appendix_anchor": "sec-ag-logaritamska-skala",
        "first_use_path": "chapters/04-sazimanje-podataka.qmd",
        "reminder_anchor": "podsjetnik-logaritamska-skala",
        "first_use_marker": "Kada strogo pozitivne vrijednosti imaju takav oblik",
    },
)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(payload)


def require_file(root: Path, relative: Path) -> Path:
    path = root / relative
    if not path.is_file():
        raise ValueError(f"missing declared input: {relative.as_posix()}")
    return path


def d10_section(text: str) -> str:
    start = "## 3. D10 — opseg Dodatka G (numerički podsjetnik)"
    end = "## 4. D05 i H10 — AI ljestvica kompetencija i granica provjere znanja"
    if start not in text or end not in text:
        raise ValueError("D10 decision section is missing")
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def source_entry(root: Path, relative: Path) -> dict[str, str]:
    path = require_file(root, relative)
    return {"path": relative.as_posix(), "sha256": sha256_file(path)}


def build(root: Path) -> dict[str, Any]:
    decision_path = require_file(root, DECISION)
    decision_text = decision_path.read_text(encoding="utf-8")
    decision = d10_section(decision_text)
    normalized_decision = " ".join(decision.split())
    exact_scope = (
        "Dodatak G obuhvaća točno četiri teme: postotke i postotne bodove, "
        "udjele i stope, nagib te logaritamsku skalu. Ništa se ne dodaje ni "
        "oduzima."
    )
    if exact_scope not in normalized_decision:
        raise ValueError("D10 exact four-topic scope is missing")

    inventory_path = require_file(root, INVENTORY)
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    page_by_id = {page["id"]: page for page in inventory["pages"]}
    expected_page = {
        "id": "app-g",
        "source": APPENDIX.as_posix(),
        "output": "dodaci/g-numericki-podsjetnik.html",
        "kind": "appendix",
        "appendix_letter": "G",
        "audit_label": "app-g",
        "standalone": False,
        "render_via": "book",
    }
    if page_by_id.get("app-g") != expected_page:
        raise ValueError("Appendix G inventory record is not exact")
    if inventory["book"]["appendices"] != [
        "app-a", "app-b", "app-c", "app-d", "app-e", "app-f", "app-g"
    ]:
        raise ValueError("book appendix order is not A-G")

    appendix_path = require_file(root, APPENDIX)
    appendix = appendix_path.read_text(encoding="utf-8")
    headings = re.findall(r"^##\s+(.+?)\s+\{#([^}\s]+)\}\s*$", appendix, re.MULTILINE)
    expected_headings = [(topic["title"], topic["appendix_anchor"]) for topic in TOPICS]
    if headings != expected_headings:
        raise ValueError("Appendix G headings do not equal the four D10 topics")

    routes = []
    chapter_sources: dict[str, dict[str, str]] = {}
    for topic in TOPICS:
        chapter = Path(topic["first_use_path"])
        chapter_path = require_file(root, chapter)
        chapter_text = chapter_path.read_text(encoding="utf-8")
        chapter_sources[chapter.as_posix()] = source_entry(root, chapter)
        target = f"../{APPENDIX.as_posix()}#{topic['appendix_anchor']}"
        routes.append(
            {
                "topic_id": topic["id"],
                "title": topic["title"],
                "appendix_path": APPENDIX.as_posix(),
                "appendix_anchor": topic["appendix_anchor"],
                "first_use_path": chapter.as_posix(),
                "first_use_anchor": topic["reminder_anchor"],
                "first_use_marker": topic["first_use_marker"],
                "target": target,
                "source_sha256": sha256_file(chapter_path),
                "reminder_present": f"#{topic['reminder_anchor']} .column-margin" in chapter_text,
                "target_present": target in chapter_text,
            }
        )

    widgets_path = require_file(root, WIDGETS)
    widgets = json.loads(widgets_path.read_text(encoding="utf-8"))["widgets"]
    static_twins = sum(
        bool(widget.get("parity", {}).get("source", {}).get("r_label"))
        for widget in widgets
    )
    chapter_count = sum(page.get("kind") in {"preface", "chapter"} for page in inventory["pages"])
    appendix_count = sum(page.get("kind") == "appendix" for page in inventory["pages"])
    solution_count = sum(page.get("kind") == "solution" for page in inventory["pages"])
    architecture = {
        "chapters": chapter_count,
        "appendices": appendix_count,
        # D10 je povijesna arhitekturna osnova prije zasebno odobrene D06
        # projekcije rješenja. Artefakt smije osvježiti ulazne sažetke, ali ne
        # smije prepisati broj koji je predan handoffom H-P5-G-001.
        "canonical_pages": len(inventory["pages"]) - solution_count,
        "widgets": len(widgets),
        "widgets_with_static_twins": static_twins,
        "callout_types": 4,
        "authorization": {
            "gate": "G-A2d",
            "decision": "D10",
            "approved_on": "2026-08-04",
        },
    }

    return {
        "schema_version": 1,
        "packet": "P5-G",
        "contract": "appendix",
        "canonical_sources": {
            "d10_decision": {
                **source_entry(root, DECISION),
                "section_sha256": sha256_bytes(decision.encode("utf-8")),
            },
            "book_inventory": source_entry(root, INVENTORY),
            "inventory_generator": source_entry(root, INVENTORY_GENERATOR),
            "quarto_projection": source_entry(root, QUARTO),
            "runtime_route_projection": source_entry(root, RUNTIME_ROUTES),
            "appendix_g": source_entry(root, APPENDIX),
            "first_use_sources": [chapter_sources[key] for key in sorted(chapter_sources)],
            "style_contract": source_entry(root, STYLE),
            "widget_inventory": source_entry(root, WIDGETS),
            "bibliography": source_entry(root, REFERENCES),
        },
        "topics": [
            {
                "id": topic["id"],
                "title": topic["title"],
                "decision_phrase": topic["decision_phrase"],
                "appendix_anchor": topic["appendix_anchor"],
            }
            for topic in TOPICS
        ],
        "first_use_routes": routes,
        "architecture_after_d10": architecture,
        "pathway": {
            "generator": "scripts/build-appendix-g-route.py",
            "checker": "scripts/check-appendix-g.py",
            "inventory_generator": "scripts/book_inventory.py",
            "declared_inputs_hash": canonical_hash(
                {
                    "decision": sha256_file(decision_path),
                    "inventory": sha256_file(inventory_path),
                    "appendix": sha256_file(appendix_path),
                    "chapters": {
                        key: value["sha256"] for key, value in sorted(chapter_sources.items())
                    },
                }
            ),
        },
        "public_promise": {
            "exactly_four_topics": True,
            "secondary_school_numeracy_only": True,
            "new_statistical_method": False,
            "chapter_mini_lessons_added": False,
            "print_safe": True,
            "sanctioned_first_use_mechanism": ".column-margin",
        },
    }


def write_artifact(root: Path, artifact: dict[str, Any]) -> None:
    path = root / ARTIFACT
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(artifact, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    artifact = build(root)
    write_artifact(root, artifact)
    print(
        "APPENDIX_G_ROUTE_BUILT "
        f"topics={len(artifact['topics'])} routes={len(artifact['first_use_routes'])} "
        f"pages={artifact['architecture_after_d10']['canonical_pages']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
