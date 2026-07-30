"""Validate the source contract for the book's seventeen chapter widgets."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def guidance_from_source(source: str) -> list[str]:
    """Return the ordered list immediately following the canonical heading."""
    lines = source.splitlines()
    try:
        index = lines.index("**Što isprobati.**") + 1
    except ValueError:
        return []

    items: list[str] = []
    started = False
    for line in lines[index:]:
        match = re.match(r"^\d+\.\s+(.*)", line)
        if match:
            started = True
            items.append(match.group(1).strip())
            continue
        if started and line.startswith("   "):
            items[-1] += f" {line.strip()}"
            continue
        if started and not line.strip():
            break
    return items


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    registry_path = root / "data" / "widgets.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    widgets = registry.get("widgets", [])
    errors: list[str] = []

    expected_ids = [f"w{number:02d}" for number in range(1, 18)]
    actual_ids = [item.get("id") for item in widgets]
    if actual_ids != expected_ids:
        errors.append(
            "data/widgets.json mora sadržavati w01–w17 kanonskim redoslijedom"
        )

    for item in widgets:
        widget_id = item.get("id", "")
        chapter = root / item.get("poglavlje", "")
        if not chapter.is_file():
            errors.append(f"{widget_id}: ne postoji izvor poglavlja {chapter}")
            continue

        source = chapter.read_text(encoding="utf-8")
        required = {
            "Inputs.form": "jedinstvena upravljačka ploča",
            f"label: fig-{widget_id}": "oznaka HTML figure",
            f"label: fig-{widget_id}-print": "oznaka statičkog blizanca",
            "fig-alt:": "alternativni opis",
            "when-format=\"html\"": "HTML formatni gate",
            "when-format=\"pdf\"": "tiskani formatni gate",
            "widget-frame": "okvir interakcije",
            "**Što isprobati.**": "blok pokusa",
        }
        for marker, description in required.items():
            if marker not in source:
                errors.append(f"{widget_id}: nedostaje {description} ({marker})")

        if "Interaktivni graf još nije izrađen" in source:
            errors.append(f"{widget_id}: razvojni placeholder još je u poglavlju")

        if len(re.findall(rf"label:\s*fig-{re.escape(widget_id)}\s*$", source, re.M)) != 1:
            errors.append(f"{widget_id}: HTML oznaka mora se pojaviti točno jednom")

        if not item.get("opis", "").strip():
            errors.append(f"{widget_id}: registar nema opis")
        registered_guidance = item.get("sto_isprobati", [])
        if len(registered_guidance) < 2:
            errors.append(f"{widget_id}: registar mora imati barem dva pokusa")
        source_guidance = guidance_from_source(source)
        if source_guidance != registered_guidance:
            errors.append(
                f"{widget_id}: pokusi u registru ne odgovaraju popisu u poglavlju"
            )
        frame_title = re.search(
            r'\.widget-frame\s+data-naslov="([^"]+)"', source
        )
        if not frame_title or frame_title.group(1) != item.get("naziv"):
            errors.append(
                f"{widget_id}: naziv registra ne odgovara data-naslov okviru"
            )
        if item.get("status") != "gotov":
            errors.append(f"{widget_id}: status registra mora biti 'gotov'")

    if errors:
        print("Provjera widgeta nije prošla:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Svih 17 widgeta ima HTML graf, statički blizanac i potpuni registar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
