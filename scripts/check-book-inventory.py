#!/usr/bin/env python3
"""Fail closed when sanctioned pages, routes, or Quarto projections drift."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.dont_write_bytecode = True

from book_inventory import (
    InventoryError,
    appendix_pages,
    chapter_pages,
    inventory_sha256,
    load_inventory,
    solution_pages,
    sync_projections,
)


CHECKOUT_ROOT = Path(__file__).resolve().parents[1]


def validate_consumers(root: Path, inventory: dict[str, object]) -> None:
    required_fragments = {
        "scripts/check-rendered-html.py": [
            "from book_inventory import",
            'inventory["pages"]',
        ],
        "scripts/audit-rendered-html.js": [
            '"config", "book-inventory.json"',
            "bookInventory.pages.map",
        ],
        "scripts/embed-404-assets.py": [
            "from book_inventory import",
            "portable_assets",
        ],
        "styles/book-include.html": [
            "BEGIN GENERATED: book-inventory runtime-routes",
            "var SAMOSTALNE =",
            "var NAVBAR_SKUPINE =",
            "var PUTOVI_STRANICA =",
            "var AI_PUTOVI_POGLAVLJA =",
        ],
        "scripts/render-book-pdf.ps1": ["scripts\\check-book-inventory.py"],
        "scripts/render-book-docx.ps1": ["scripts\\check-book-inventory.py"],
        ".github/workflows/publish.yml": [
            "python scripts/check-book-inventory.py",
            "python scripts/check-book-inventory-fixtures.py",
        ],
    }
    texts: dict[str, str] = {}
    for relative, fragments in required_fragments.items():
        path = root / relative
        if not path.is_file():
            raise InventoryError(f"inventory consumer is missing: {relative}")
        text = path.read_text(encoding="utf-8")
        texts[relative] = text
        for fragment in fragments:
            if fragment not in text:
                raise InventoryError(
                    f"inventory consumer {relative} does not use the canonical source: {fragment}"
                )

    wrapper_paths = [
        "scripts/render-book-pdf.ps1",
        "scripts/render-book-docx.ps1",
        "scripts/check-pdf-release-path.ps1",
        "scripts/check-rendered-html.py",
        "scripts/audit-rendered-html.js",
        "scripts/embed-404-assets.py",
    ]
    canonical_literals = {
        value
        for page in inventory["pages"]
        for value in (page["source"], page["output"])
        if page["kind"] in {"chapter", "preface", "appendix"}
    }
    for relative in wrapper_paths:
        text = texts.get(relative)
        if text is None:
            text = (root / relative).read_text(encoding="utf-8")
        copied = sorted(value for value in canonical_literals if value in text)
        if copied:
            raise InventoryError(f"hard-coded route copy remains in {relative}: {copied}")

    for profile in root.glob("_quarto-*.yml"):
        text = profile.read_text(encoding="utf-8")
        if any(
            line.startswith(("  chapters:", "  appendices:", "  navbar:", "  page-footer:"))
            for line in text.splitlines()
        ):
            raise InventoryError(
                f"profile declares a competing page or navigation inventory: {profile.name}"
            )

    workflow = texts[".github/workflows/publish.yml"]
    inventory_step = workflow.index("python scripts/check-book-inventory.py")
    render_step = workflow.index("quarto render")
    pages_step = workflow.index("actions/configure-pages")
    if not inventory_step < render_step < pages_step:
        raise InventoryError("blocking inventory check must precede render and Pages setup")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=CHECKOUT_ROOT)
    parser.add_argument(
        "--write",
        action="store_true",
        help="refresh only the marked _quarto.yml projections from the canonical inventory",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        inventory = load_inventory(root)
        drift = sync_projections(root, inventory, write=args.write)
        if drift and not args.write:
            raise InventoryError(
                "generated book inventory drift; run python scripts/check-book-inventory.py --write"
            )
        if args.write and drift:
            inventory = load_inventory(root)
            if sync_projections(root, inventory, write=False):
                raise InventoryError("generated inventory projections are still stale after --write")
            print("BOOK_INVENTORY_SYNC_OK targets=_quarto.yml,styles/book-include.html")
        validate_consumers(root, inventory)
        chapters = chapter_pages(inventory, include_landing=False)
        appendices = appendix_pages(inventory)
        solutions = solution_pages(inventory)
        print(
            "BOOK_INVENTORY_OK "
            f"pages={len(inventory['pages'])} chapters={len(chapters)} "
            f"appendices={len(appendices)} solutions={len(solutions)} "
            f"navbar={len(inventory['navigation']['navbar'])} "
            f"footer={len(inventory['navigation']['footer'])} "
            f"sha256={inventory_sha256(root)}"
        )
        return 0
    except (OSError, InventoryError) as error:
        print(f"book inventory: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
