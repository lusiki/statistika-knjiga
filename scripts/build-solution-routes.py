#!/usr/bin/env python3
"""Izgradi javnu i kolegijsku projekciju iz kanonskih zapisa rješenja."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RECORD_ROOT = ROOT / "assessment/solution-records"
OUTPUT = ROOT / "rjesenja.qmd"
UNIT_ORDER = [f"{number:02d}" for number in range(19)]
TASK_ORDER = [
    "callout_greska",
    "konceptualni",
    "racunski",
    "kriticki",
    "revizija_modela",
]
TASK_LABELS = {
    "callout_greska": "Namjerna pogreška",
    "konceptualni": "Konceptualni zadatak",
    "racunski": "Računski zadatak",
    "kriticki": "Kritički zadatak",
    "revizija_modela": "Revizija modela",
}


def compact(value: str) -> str:
    return " ".join(value.split())


def table_cell(value: str) -> str:
    return compact(value).replace("|", "\\|")


def read_records(root: Path = ROOT) -> list[tuple[Path, dict[str, Any]]]:
    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / "assessment/solution-records").glob("unit-*/*.json")):
        records.append((path, json.loads(path.read_text(encoding="utf-8"))))
    order = {task: index for index, task in enumerate(TASK_ORDER)}
    records.sort(key=lambda item: (item[1]["unit_id"], order[item[1]["task_class"]], item[1]["record_id"]))
    return records


def record_state(records: list[tuple[Path, dict[str, Any]]], root: Path = ROOT) -> str:
    digest = hashlib.sha256()
    for path, _ in records:
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def source_title(root: Path, relative: str) -> str:
    text = (root / relative).read_text(encoding="utf-8")
    match = re.search(r'(?m)^title:\s*["\'](.+?)["\']\s*$', text)
    if not match:
        raise ValueError(f"izvor nema naslov: {relative}")
    return match.group(1)


def public_projection(record: dict[str, Any]) -> list[str]:
    answer = record["answer_components"]
    lines: list[str] = []

    planted = answer["planted_error"]
    if planted["applicable"]:
        lines.extend([
            f"**Namjerna pogreška.** {compact(planted['statement'])}",
            "",
            compact(planted["why_wrong"]),
            "",
        ])

    diagnostic = answer["revealing_diagnostic"]
    if diagnostic["applicable"]:
        lines.extend([
            f"**Provjera koja otkriva odgovor.** {compact(diagnostic['procedure'])}",
            "",
            f"Očekivani trag: {compact(diagnostic['expected_evidence'])}",
            "",
        ])

    components = answer["model_response_components"]
    if components["applicable"]:
        lines.extend(["**Što odgovor mora sadržavati.**", ""])
        for component in components["components"]:
            lines.append(
                f"- {compact(component['required_claim'])} Trag: {compact(component['required_evidence'])}"
            )
        lines.append("")

    numerical = answer["numerical_check"]
    if numerical["applicable"]:
        lines.extend([
            f"**Brojčana provjera.** {compact(numerical['expected_result'])}",
            "",
            f"Pravilo prihvaćanja: {compact(numerical['tolerance_or_acceptance_rule'])}",
            "",
            f"Neovisna provjera: {compact(numerical['independent_method'])}",
            "",
            f"Dokazni trag: {compact(numerical['evidence_reference'])}",
            "",
        ])

    non_answers = answer["plausible_non_answers"]
    if non_answers["applicable"]:
        lines.extend(["**Odgovori koji nisu dovoljni.**", ""])
        for response in non_answers["responses"]:
            lines.append(
                f"- {compact(response['response'])} Zašto nije dovoljno: {compact(response['why_insufficient'])}"
            )
        lines.append("")
    return lines


def protected_projection(record: dict[str, Any]) -> list[str]:
    rubric = record["answer_components"]["severity_ranked_rubric"]
    lines = [
        '::: {.content-visible when-profile="kolegij"}',
        "### Puna rubrika",
        "",
        "| Razina | Kriterij | Vidljivi dokaz |",
        "|---|---|---|",
    ]
    for criterion in rubric["criteria"]:
        lines.append(
            f"| `{criterion['severity']}` | {table_cell(criterion['description'])} | "
            f"{table_cell(criterion['observable_evidence'])} |"
        )
    lines.extend(["", "### Prihvatljive alternative", ""])
    for alternative in record["alternatives"]:
        lines.append(
            f"- {compact(alternative['description'])} Granica prihvaćanja: "
            f"{compact(alternative['acceptance_boundary'])}"
        )
    lines.extend(["", "### Bilješke nastavniku", ""])
    lines.extend(f"- {compact(note)}" for note in record["instructor_notes"])
    lines.extend(["", ":::", ""])
    return lines


def render(root: Path = ROOT) -> str:
    records = read_records(root)
    by_unit: dict[str, list[dict[str, Any]]] = {unit: [] for unit in UNIT_ORDER}
    for _, record in records:
        by_unit.setdefault(record["unit_id"], []).append(record)
    if list(by_unit) != UNIT_ORDER or any(len(by_unit[unit]) != 5 for unit in UNIT_ORDER):
        raise ValueError("kanonsko spremište mora sadržavati pet zapisa u svakoj od 19 jedinica")

    lines = [
        "---",
        'title: "Provjere rješenja"',
        'subtitle: "Sažete javne provjere i zaštićeni kolegijski kriteriji iz jednoga izvora"',
        "---",
        "",
        f"<!-- GENERATED: scripts/build-solution-routes.py records-sha256={record_state(records, root)} -->",
        "",
        "Ova je stranica odvojena od zadataka u glavnom slijedu knjige. Javna i",
        "tiskana inačica daju sažetu provjeru za samostalan rad. Nastavni profil",
        "`kolegij` uz istu provjeru prikazuje pune kriterije, prihvatljive alternative",
        "i bilješke nastavniku. Svaki prikaz nastaje iz odgovarajućega kanonskog",
        "zapisa u `assessment/solution-records`; ova stranica nije drugi izvor",
        "odgovora i nije dio javnoga AI izvoza.",
        "",
        "Provjeru otvorite tek nakon vlastitoga pokušaja. Brojčani trag i dalje",
        "treba usporediti s imenovanim izvorom, a odgovornost za zaključak ostaje",
        "na osobi koja odgovor predaje ili objavljuje.",
        "",
    ]
    for unit in UNIT_ORDER:
        records_for_unit = by_unit[unit]
        title = source_title(root, records_for_unit[0]["source_anchor"]["path"])
        heading = "Predgovor" if unit == "00" else f"Poglavlje {int(unit)} — {title}"
        lines.extend([f"# {heading}", ""])
        for record in records_for_unit:
            source = record["source_anchor"]
            lines.extend([
                f"## {TASK_LABELS[record['task_class']]} {{#{record['record_id']}}}",
                "",
                f"[Povratak na zadatak]({source['path']}#{source['anchor']})",
                "",
            ])
            lines.extend(public_projection(record))
            lines.extend(protected_projection(record))
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="ne piše datoteku, nego provjerava čistu regeneraciju")
    args = parser.parse_args()
    try:
        expected = render(ROOT)
        if args.check:
            actual = OUTPUT.read_text(encoding="utf-8")
            if actual != expected:
                raise ValueError("rjesenja.qmd ne odgovara kanonskim zapisima; pokrenite generator")
            print("SOLUTION_ROUTES_GENERATED_OK records=95 units=19 public=95 protected=95 drift=0")
            return 0
        OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
        print("SOLUTION_ROUTES_WRITE_OK records=95 units=19 output=rjesenja.qmd")
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"solution routes: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
