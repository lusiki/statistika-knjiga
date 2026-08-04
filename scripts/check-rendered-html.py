"""Fail a release build when the rendered HTML is stale or incomplete."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from book_inventory import appendix_pages, chapter_pages, load_inventory

CHECKOUT_ROOT = Path(__file__).resolve().parents[1]

STALE_MARKERS = [
    "STATUS: kostur",
    "Naslov prvog odjeljka",
    "Interaktivni graf još nije izrađen",
    "Specifikacija je u <code>data/widgets.json</code>",
]


def main() -> int:
    inventory = load_inventory(CHECKOUT_ROOT)
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "docs").resolve()
    expected = [output / Path(page["output"]) for page in inventory["pages"]]

    errors: list[str] = []
    for path in expected:
        if not path.is_file():
            errors.append(f"Nedostaje renderirana stranica: {path}")

    for path in expected:
        if not path.is_file():
            continue
        html = path.read_text(encoding="utf-8")
        for marker in STALE_MARKERS:
            if marker in html:
                errors.append(f"{path}: pronađen zastarjeli marker {marker!r}")

    for page in chapter_pages(inventory, include_landing=False):
        if not page.get("widget"):
            continue
        number = page["chapter_number"]
        path = output / Path(page["output"])
        if path.is_file():
            label = f"fig-w{number:02d}"
            html = path.read_text(encoding="utf-8")
            if label not in html:
                errors.append(f"{path}: nedostaje interakcija {label}")

    appendix_pattern = re.compile(r"Appendix\s+[A-Z]\s*[—–-]\s*Dodatak", re.I)
    for page in appendix_pages(inventory):
        path = output / Path(page["output"])
        if path.is_file() and appendix_pattern.search(
            path.read_text(encoding="utf-8")
        ):
            errors.append(f"{path}: dvostruki ili pomaknuti naslov dodatka")

    if errors:
        print("Provjera renderiranog HTML-a nije prošla:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Provjereno je {len(expected)} kanonskih HTML stranica.")
    print("Nema kostura, razvojnih widgeta ni dvostrukih naslova dodataka.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
