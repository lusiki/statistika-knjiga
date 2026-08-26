#!/usr/bin/env python3
"""Verify Appendix G scope, inventory, first-use routes, and clean rebuild."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER = Path("scripts/build-appendix-g-route.py")
ARTIFACT = Path("config/appendix-g-numeracy-route.json")


def load_builder(root: Path):
    path = root / BUILDER
    spec = importlib.util.spec_from_file_location("appendix_g_builder", path)
    if spec is None or spec.loader is None:
        raise ValueError("cannot load Appendix G builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILDER_MODULE = load_builder(ROOT)


def fail(message: str) -> None:
    raise AssertionError(message)


def fenced_block(text: str, anchor: str) -> str:
    pattern = rf"^::: \{{#{re.escape(anchor)} \.column-margin\}}\n(.*?)\n:::$"
    matches = re.findall(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if len(matches) != 1:
        fail(f"podsjetnik block count={anchor}:{len(matches)}")
    return matches[0]


def validate(root: Path, fixture: str = "") -> dict[str, int]:
    builder = load_builder(root)
    artifact_path = root / ARTIFACT
    if not artifact_path.is_file():
        fail("route artifact is missing")
    artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
    expected = builder.build(root)
    if artifact != expected:
        fail("route artifact is stale")

    appendix_path = root / builder.APPENDIX
    appendix = appendix_path.read_text(encoding="utf-8")
    chapter_texts = {
        path: (root / path).read_text(encoding="utf-8")
        for path in {Path(topic["first_use_path"]) for topic in builder.TOPICS}
    }
    if fixture == "extra_topic":
        appendix += "\n## Dodatna tema {#sec-ag-dodatna}\n"
    elif fixture == "wrong_route":
        path = Path(builder.TOPICS[0]["first_use_path"])
        chapter_texts[path] = chapter_texts[path].replace(
            builder.TOPICS[0]["appendix_anchor"], "sec-ag-pogresno", 1
        )
    elif fixture == "raw_style":
        appendix += '\n<div style="color:red">pogreška</div>\n'

    headings = re.findall(r"^##\s+(.+?)\s+\{#([^}\s]+)\}\s*$", appendix, re.MULTILINE)
    expected_headings = [
        (topic["title"], topic["appendix_anchor"]) for topic in builder.TOPICS
    ]
    if headings != expected_headings:
        fail(f"four-topic scope={len(headings)}")
    if len(artifact.get("topics", [])) != 4:
        fail("artifact topic count")

    raw_or_profile_markers = (
        "<div", "style=", "content-visible", "when-format", "```{ojs}", "```{r}",
    )
    for marker in raw_or_profile_markers:
        if marker in appendix:
            fail(f"print-safe source marker={marker}")
    if re.search(r"\{#def-", appendix):
        fail("Appendix G must not add or rename a stable definition identifier")
    if re.search(r"^##\s+.*(?:test|regresij|korelacij|hipotez|interval|model)", appendix, re.I | re.M):
        fail("Appendix G became a methods chapter")

    references = (root / builder.REFERENCES).read_text(encoding="utf-8")
    citation_keys = set(re.findall(r"@([A-Za-z0-9:_-]+)", appendix))
    if citation_keys != {"dip2024", "sikic2026"}:
        fail(f"Appendix G citation set={sorted(citation_keys)}")
    for key in citation_keys:
        if not re.search(rf"^@\w+\{{{re.escape(key)},", references, re.MULTILINE):
            fail(f"missing bibliography key={key}")

    route_count = 0
    for topic in builder.TOPICS:
        path = Path(topic["first_use_path"])
        text = chapter_texts[path]
        block = fenced_block(text, topic["reminder_anchor"])
        expected_link = (
            f"**Podsjetnik.** [{topic['title']}]"
            f"(../{builder.APPENDIX.as_posix()}#{topic['appendix_anchor']})"
        )
        if block != expected_link:
            fail(f"podsjetnik content={topic['id']}")
        if len(block.splitlines()) != 1 or "$$" in block or "`" in block:
            fail(f"duplicate mini-lesson={topic['id']}")
        reminder_position = text.find(f"#{topic['reminder_anchor']} .column-margin")
        marker_position = text.find(topic["first_use_marker"])
        if reminder_position < 0 or marker_position < 0 or reminder_position > marker_position:
            fail(f"first-use placement={topic['id']}")
        if len(re.findall(rf"\{{#{re.escape(topic['appendix_anchor'])}\}}", appendix)) != 1:
            fail(f"appendix target count={topic['id']}")
        route_count += 1

    total_reminders = sum(
        text.count(".column-margin") for text in chapter_texts.values()
    )
    if total_reminders != 4:
        fail(f"sanctioned podsjetnik count={total_reminders}")
    inventory = json.loads((root / builder.INVENTORY).read_text(encoding="utf-8"))
    architecture = artifact.get("architecture_after_d10", {})
    expected_architecture = {
        "chapters": 19,
        "appendices": 7,
        "canonical_pages": 38,
        "widgets": 17,
        "widgets_with_static_twins": 17,
        "callout_types": 4,
        "authorization": {
            "gate": "G-A2d",
            "decision": "D10",
            "approved_on": "2026-08-04",
        },
    }
    if architecture != expected_architecture:
        fail(f"architecture counts={architecture}")
    if len(inventory["pages"]) != 39 or len(inventory["book"]["appendices"]) != 7:
        fail("inventory counts")
    quarto = (root / builder.QUARTO).read_text(encoding="utf-8")
    runtime = (root / builder.RUNTIME_ROUTES).read_text(encoding="utf-8")
    if quarto.count(f"- {builder.APPENDIX.as_posix()}") != 1:
        fail("generated Quarto navigation")
    if runtime.count('"app-g": "/dodaci/g-numericki-podsjetnik.html"') != 1:
        fail("generated runtime route")
    if inventory.get("solution_routes") != ["solutions"]:
        fail("post-P5-ROUTES solution route is not the single sanctioned projection")

    promise = artifact.get("public_promise", {})
    if promise != {
        "exactly_four_topics": True,
        "secondary_school_numeracy_only": True,
        "new_statistical_method": False,
        "chapter_mini_lessons_added": False,
        "print_safe": True,
        "sanctioned_first_use_mechanism": ".column-margin",
    }:
        fail("public promise")
    return {"topics": len(headings), "routes": route_count, "pages": len(inventory["pages"])}


def copy_into(stage: Path, source_root: Path, relative: Path) -> None:
    destination = stage / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_root / relative, destination)


def clean_regeneration(expected: dict[str, int]) -> None:
    builder = BUILDER_MODULE
    declared = {
        BUILDER,
        builder.DECISION,
        builder.INVENTORY,
        builder.INVENTORY_GENERATOR,
        builder.QUARTO,
        builder.RUNTIME_ROUTES,
        builder.APPENDIX,
        builder.STYLE,
        builder.WIDGETS,
        builder.REFERENCES,
        *(Path(topic["first_use_path"]) for topic in builder.TOPICS),
    }
    with tempfile.TemporaryDirectory(prefix="appendix-g-clean-") as directory:
        stage = Path(directory)
        for relative in sorted(declared):
            copy_into(stage, ROOT, relative)
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
        if (stage / ARTIFACT).read_bytes() != (ROOT / ARTIFACT).read_bytes():
            fail("clean regeneration is not byte-identical")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-clean", action="store_true")
    args = parser.parse_args()
    fixture = os.environ.get("APPENDIX_G_NEGATIVE_FIXTURE", "")
    try:
        result = validate(ROOT, fixture=fixture)
        if not args.skip_clean and not fixture:
            clean_regeneration(result)
        print(
            "APPENDIX_G_CHECK_OK "
            f"topics={result['topics']} first_use_routes={result['routes']} "
            f"pages={result['pages']} appendices=7 inventory=generated "
            "podsjetnik=column-margin xrefs=verified clean_pathway=verified "
            "print_source=present methods_added=0"
        )
        return 0
    except (AssertionError, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"APPENDIX_G_CHECK_FAILED {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
