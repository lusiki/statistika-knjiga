"""Fail a release build when the rendered HTML is stale or incomplete."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT_PAGES = [
    "404.html",
    "index.html",
    "interakcije.html",
    "podaci.html",
    "pojmovnik.html",
    "predavanja.html",
    "raspored.html",
    "references.html",
    "resursi.html",
    "silabus.html",
    "uci-s-ai.html",
]

CHAPTERS = [
    "00-predgovor",
    "01-zasto-statistika",
    "02-mjerenje-i-dizajn",
    "03-kako-brojke-zavode",
    "04-sazimanje-podataka",
    "05-vizualizacija",
    "06-povezanost",
    "07-vjerojatnost",
    "08-uzorkovanje",
    "09-procjena",
    "10-logika-testiranja",
    "11-velicina-ucinka-i-snaga",
    "12-kriza-i-obnova",
    "13-kategoricki-podaci",
    "14-dvije-grupe",
    "15-vise-grupa",
    "16-regresija",
    "17-doba-algoritama",
    "18-vase-prvo-istrazivanje",
]

APPENDICES = [
    "a-praktikum",
    "b-jamovi",
    "c-katalog-podataka",
    "d-koji-test",
    "e-rjecnik",
    "f-ai-protokol",
]

STALE_MARKERS = [
    "STATUS: kostur",
    "Naslov prvog odjeljka",
    "Interaktivni graf još nije izrađen",
    "Specifikacija je u <code>data/widgets.json</code>",
]


def main() -> int:
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "docs").resolve()
    expected = (
        [output / page for page in ROOT_PAGES]
        + [output / "chapters" / f"{name}.html" for name in CHAPTERS]
        + [output / "dodaci" / f"{name}.html" for name in APPENDICES]
    )

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

    for number, name in enumerate(CHAPTERS[1:18], start=1):
        path = output / "chapters" / f"{name}.html"
        if path.is_file():
            label = f"fig-w{number:02d}"
            html = path.read_text(encoding="utf-8")
            if label not in html:
                errors.append(f"{path}: nedostaje interakcija {label}")

    appendix_pattern = re.compile(r"Appendix\s+[B-G]\s*[—–-]\s*Dodatak", re.I)
    for path in expected:
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
