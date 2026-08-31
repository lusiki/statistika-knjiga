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
SEVERITY_LABELS = {
    "fatal": "Presudni nedostatak",
    "major": "Veliki nedostatak",
    "minor": "Manji nedostatak",
    "useful_improvement": "Korisno poboljšanje",
}
PROSE_OVERRIDES = {
    ("sol-06-konceptualni-01", "numerical.expected_result"): (
        "Glavni par ima 27 potpunih država. Par s ranim napuštanjem obrazovanja "
        "ima najviše 26 jer je luksemburška vrijednost označena dvotočkom, dok "
        "hrvatskih 2,1 uz status u ostaje uključeno."
    ),
    ("sol-09-racunski-01", "numerical.expected_result"): (
        "Za A širina iznosi 0,619806421393 uz 3 promašaja. Za B širina iznosi "
        "0,814602725259 uz 0 promašaja. Za C širina iznosi 0,309903210697 uz 1 "
        "promašaj. Analitička datoteka ima 50000 redaka; portal ima 15101 redak "
        "od ukupno 50000, zbroj povjerenja 72101, udio 15101/50000 = 0,30202 i "
        "prosjek 72101/15101 = 4,7745844646."
    ),
    ("sol-14-racunski-01", "numerical.expected_result"): (
        "Za televiziju vrijedi 58098/10827 = 5,366029371017, a za društvene "
        "mreže 54432/13378 = 4,068769621767. Televizija minus društvene mreže "
        "iznosi 1,297259749250 boda; d uz SD 1,6 = 0,810787343281, a d uz SD "
        "3,2 = 0,405393671641."
    ),
    ("sol-15-kriticki-01", "numerical.expected_result"): (
        "Za televiziju vrijedi 58098/10827 = 5,366029371017, a za društvene "
        "mreže 54432/13378 = 4,068769621767. Populacijska razlika televizije i "
        "društvenih mreža iznosi 1,297259749250 boda. Sud o važnosti ovisi o "
        "unaprijed zapisanu pragu, a ne o naknadnom prilagođavanju praga rezultatu."
    ),
    ("sol-16-callout-greska-01", "numerical.expected_result"): (
        "Obje prijavljene veličine pripadaju istih n redaka skupa za učenje. "
        "R-kvadrat je 1 − SSE/SST na tom skupu, a `pogreska` je sqrt(SSE/n) iz "
        "istih reziduala. Nula redaka odvojene provjere ulazi u račun."
    ),
    ("sol-16-kriticki-01", "instructor_notes.0"): (
        "Ne zahtijevati račun apsolutne vjerojatnosti jer izvadak namjerno ne "
        "daje polazišnu vjerojatnost ni cijeli model."
    ),
    ("sol-16-revizija-modela-01", "diagnostic.procedure"): (
        "Provjeriti redak po redak. Potvrditi da su formula i vremenski dostupni "
        "prediktori dopušteni, označiti da `pogreska` uspoređuje ishod `uzorak` "
        "s `fitted(model)` iz istoga uzorka te utvrditi što oba broja mogu i ne "
        "mogu poduprijeti."
    ),
    ("sol-16-callout-greska-01", "nonanswers.0.reason"): (
        "Broj prediktora može povećati optimizam, ali središnji nedostatak "
        "postoji i za mali model. Ocjena je provedena na istim ishodima koji su "
        "služili procjeni."
    ),
    ("sol-16-konceptualni-01", "nonanswers.2.reason"): (
        "Nijedna skupina nema taj nagib. A raste 0,6, a B pada 0,2 po jedinici."
    ),
    ("sol-17-revizija-modela-01", "rubric.0.observable_evidence"): (
        "Središnja namjerna pogreška ili granica korpusa ostaje nepopravljena."
    ),
    ("sol-18-revizija-modela-01", "rubric.0.observable_evidence"): (
        "Središnja namjerna pogreška ili granica presječnoga dizajna ostaje nepopravljena."
    ),
    ("sol-18-revizija-modela-01", "rubric.1.observable_evidence"): (
        "Provjera rada čovjeka i asistenta nije potpuna završna potvrda odgovornosti."
    ),
    ("sol-18-revizija-modela-01", "alternatives.0.acceptance_boundary"): (
        "Mora zadržati sve brojke, ispraviti istu namjernu pogrešku, navesti jedno "
        "određeno ograničenje, granicu sljedeće delegacije i ljudsku odgovornost."
    ),
}
MAINTAINER_TERM = re.compile(
    r"(?i)\b(?:prompt(?:a|u|om|i|e)?|callout(?:-greska)?|error_id|"
    r"planted-error(?:\s+ID)?|human-ai|capstone)\b"
)


def compact(value: str) -> str:
    return " ".join(value.split())


def table_cell(value: str) -> str:
    return compact(value).replace("|", "\\|")


def reader_text(value: str, record_id: str, field: str) -> str:
    """Prevedi samo čitateljsku projekciju; strojni ID-jevi ostaju netaknuti."""
    text = PROSE_OVERRIDES.get((record_id, field), value)
    parts = re.split(
        r"(`[^`]*`|https?://\S+|(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_./-]+"
        r"(?:#[A-Za-z0-9_.-]+)?|#[A-Za-z0-9_.-]+)",
        compact(text),
    )
    replacements = [
        (r"(?i)\bplanted-error\s+ID\b", "identifikator namjerne pogreške"),
        (r"(?i)\bplanted-error\b", "namjerna pogreška"),
        (r"(?i)\berror_id\b", "identifikator pogreške"),
        (r"\bCallout-greska\b", "Okvir s namjernom pogreškom"),
        (r"\bcallout-greska\b", "okvir s namjernom pogreškom"),
        (r"\bCallout\b", "Okvir"),
        (r"\bcallout\b", "okvir"),
        (r"\bPrompta\b", "Zadatka"),
        (r"\bprompta\b", "zadatka"),
        (r"\bPromptu\b", "Zadatku"),
        (r"\bpromptu\b", "zadatku"),
        (r"\bPromptom\b", "Zadatkom"),
        (r"\bpromptom\b", "zadatkom"),
        (r"\bPrompte\b", "Zadatke"),
        (r"\bprompte\b", "zadatke"),
        (r"\bPrompt\b", "Zadatak"),
        (r"\bprompt\b", "zadatak"),
        (r"(?i)\bHuman-AI\b", "provjera rada čovjeka i asistenta"),
        (r"(?i)\bcapstone\b", "završni zadatak"),
    ]
    for index in range(0, len(parts), 2):
        for pattern, replacement in replacements:
            parts[index] = re.sub(pattern, replacement, parts[index])
    rendered = "".join(parts)
    visible = "".join(parts[::2])
    if MAINTAINER_TERM.search(visible):
        raise ValueError(f"nepreveden održavateljski izraz: {record_id} {field}")
    if field.startswith(("planted.", "diagnostic.")) and ":" in visible:
        raise ValueError(f"dvotočka u čitateljskoj prozi: {record_id} {field}")
    return rendered


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
    record_id = record["record_id"]
    lines: list[str] = []

    planted = answer["planted_error"]
    if planted["applicable"]:
        lines.extend([
            "Pogreška je u sljedećoj tvrdnji.",
            "",
            reader_text(planted["statement"], record_id, "planted.statement"),
            "",
            reader_text(planted["why_wrong"], record_id, "planted.why_wrong"),
            "",
        ])

    diagnostic = answer["revealing_diagnostic"]
    if diagnostic["applicable"]:
        lines.extend([
            "Odgovor se provjerava ovim postupkom.",
            "",
            reader_text(diagnostic["procedure"], record_id, "diagnostic.procedure"),
            "",
            reader_text(diagnostic["expected_evidence"], record_id, "diagnostic.expected_evidence"),
            "",
        ])

    components = answer["model_response_components"]
    if components["applicable"]:
        lines.extend([
            "Odgovor mora sadržavati sljedeće sastavnice.",
            "",
            "| Potrebna tvrdnja | Vidljivi dokaz |",
            "|---|---|",
        ])
        for index, component in enumerate(components["components"]):
            claim = reader_text(component["required_claim"], record_id, f"components.{index}.claim")
            evidence = reader_text(component["required_evidence"], record_id, f"components.{index}.evidence")
            lines.append(f"| {table_cell(claim)} | {table_cell(evidence)} |")
        lines.append("")

    numerical = answer["numerical_check"]
    if numerical["applicable"]:
        expected = reader_text(numerical["expected_result"], record_id, "numerical.expected_result")
        acceptance = reader_text(
            numerical["tolerance_or_acceptance_rule"], record_id, "numerical.acceptance_rule"
        )
        method = reader_text(numerical["independent_method"], record_id, "numerical.independent_method")
        evidence = reader_text(numerical["evidence_reference"], record_id, "numerical.evidence_reference")
        lines.extend([
            "Brojčani trag provjerava se ovako.",
            "",
            "| Stavka | Provjera |",
            "|---|---|",
            f"| Očekivani rezultat | {table_cell(expected)} |",
            f"| Pravilo prihvaćanja | {table_cell(acceptance)} |",
            f"| Neovisni postupak | {table_cell(method)} |",
            f"| Dokazni trag | {table_cell(evidence)} |",
            "",
        ])

    non_answers = answer["plausible_non_answers"]
    if non_answers["applicable"]:
        lines.extend([
            "Sljedeći odgovori nisu dovoljni.",
            "",
            "| Nedovoljan odgovor | Zašto ne prolazi |",
            "|---|---|",
        ])
        for index, response in enumerate(non_answers["responses"]):
            reply = reader_text(response["response"], record_id, f"nonanswers.{index}.response")
            reason = reader_text(response["why_insufficient"], record_id, f"nonanswers.{index}.reason")
            lines.append(f"| {table_cell(reply)} | {table_cell(reason)} |")
        lines.append("")
    return lines


def protected_projection(record: dict[str, Any]) -> list[str]:
    rubric = record["answer_components"]["severity_ranked_rubric"]
    record_id = record["record_id"]
    lines = [
        '::: {.content-visible when-profile="kolegij"}',
        "Puna rubrika za nastavnike slijedi u tablici.",
        "",
        "| Razina | Kriterij | Vidljivi dokaz |",
        "|---|---|---|",
    ]
    for index, criterion in enumerate(rubric["criteria"]):
        description = reader_text(criterion["description"], record_id, f"rubric.{index}.description")
        evidence = reader_text(
            criterion["observable_evidence"], record_id, f"rubric.{index}.observable_evidence"
        )
        lines.append(
            f"| {SEVERITY_LABELS[criterion['severity']]} | {table_cell(description)} | "
            f"{table_cell(evidence)} |"
        )
    lines.extend([
        "",
        "Prihvatljive alternative prikazane su u sljedećoj tablici.",
        "",
        "| Prihvatljiva mogućnost | Granica prihvaćanja |",
        "|---|---|",
    ])
    for index, alternative in enumerate(record["alternatives"]):
        description = reader_text(alternative["description"], record_id, f"alternatives.{index}.description")
        boundary = reader_text(
            alternative["acceptance_boundary"], record_id, f"alternatives.{index}.acceptance_boundary"
        )
        lines.append(f"| {table_cell(description)} | {table_cell(boundary)} |")
    lines.extend([
        "",
        "Bilješke nastavniku slijede u tablici.",
        "",
        "| Bilješka nastavniku |",
        "|---|",
    ])
    for index, note in enumerate(record["instructor_notes"]):
        rendered_note = reader_text(note, record_id, f"instructor_notes.{index}")
        lines.append(f"| {table_cell(rendered_note)} |")
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
