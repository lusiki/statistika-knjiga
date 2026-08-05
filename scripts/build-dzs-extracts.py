#!/usr/bin/env python3
"""Build the bounded DZS tourism extracts from the author's local mirror.

The full DZS tourism database stays OUTSIDE this repository. The author holds a
complete local mirror of it, downloaded 2026-07-27 from the DZS PxWeb API and
transcoded from the API's windows-1250 to UTF-8; that mirror, together with its
own `_refresh-download.ps1`, is the provenance chain this repository records.
This script copies only the bounded extract that `G-A3-DZS` ratified, as amended
on 2026-08-05, and nothing else. It never touches the network.

Run:
    python scripts/build-dzs-extracts.py --mirror <path>            # verify
    python scripts/build-dzs-extracts.py --mirror <path> --write    # write

Without --write the script rebuilds every extract in memory and compares it byte
for byte with the file on disk, so a drifted extract is caught rather than
silently overwritten. The mirror is not part of the repository, so this
verification runs only where the mirror exists; in CI the recorded MD5 in
data/katalog.yml is what stands behind these bytes.

Four shape rules, the same four the generated snapshots obey:

  1. UTF-8 without BOM, LF line endings, comma as the field separator.
  2. No value contains a comma, a quote or a line break, so the files read in any
     tool without quoting rules.
  3. Source labels are copied VERBATIM. Where two DZS tables spell the same
     concept differently, both spellings survive; this script harmonises nothing.
  4. Published missing-value codes are copied verbatim and stay distinct from one
     another and from zero. Nothing is collapsed to NA, to blank or to zero.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --- the bounded selection --------------------------------------------------
#
# Every bound here is a ratified decision, not a convenience. The complete-year
# rule excludes 2026 because it carries only five of twelve months; the county
# cross-section is one year because the gate ratified one cross-section; the
# household survey is 2024 because that is the latest year its series reaches.

TU11 = "CSV/Dolasci i noćenja turista u komercijalnim smještajnim o/BS_TU11.csv"
TU12 = "CSV/Dolasci i noćenja turista u komercijalnim smještajnim o/BS_TU12.csv"
T03 = "CSV/Turistička aktivnost stanovništva Republike Hrvatske/T03.csv"

FIRST_YEAR = 2005
LAST_COMPLETE_YEAR = 2025
COUNTY_YEAR = "2025"
SURVEY_YEAR = "2024"

# BS_TU11 spells residency in lower case and BS_TU12 in title case. Both are
# copied as published; the disagreement is a fact about the source.
TU11_TURIST = ("ukupno", "domaći", "strani")
TU12_TURIST = ("Ukupno", "Domaći", "Strani")

MJESECI = (
    "Siječanj", "Veljača", "Ožujak", "Travanj", "Svibanj", "Lipanj",
    "Srpanj", "Kolovoz", "Rujan", "Listopad", "Studeni", "Prosinac",
)
TU12_MJESECI = ("I", "II", "III", "IV", "V", "VI",
                "VII", "VIII", "IX", "X", "XI", "XII")

DRZAVA = "REPUBLIKA HRVATSKA"

DOBNE_SKUPINE = ("Ukupno", "15 - 29", "30 - 49", "50 i više")
TIPOVI_PUTOVANJA = ("Privatno", "Poslovno")
DESTINACIJE = ("Ukupno", "Inozemstvo", "Hrvatska")
TRAJANJA = ("1 i više noćenja", "1 - 3 noćenja", "4 i više noćenja")
MJERE = ("Putovanja", "Noćenja", "Izdaci (euro)", "Izdaci (kuna)")


def read_mirror_csv(mirror: Path, relative: str) -> list[list[str]]:
    """Read one tidy long table from the mirror. The mirror ships UTF-8 with BOM."""
    path = mirror / relative
    if not path.is_file():
        raise SystemExit(f"Mirror table is missing: {path}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))
    if len(rows) < 2:
        raise SystemExit(f"Mirror table has no data rows: {path}")
    return rows[1:]


def index(rows: list[list[str]], key_columns: tuple[int, ...], value_column: int) -> dict:
    table: dict[tuple[str, ...], str] = {}
    for row in rows:
        key = tuple(row[i] for i in key_columns)
        if key in table:
            raise SystemExit(f"Mirror table repeats a key: {key}")
        table[key] = row[value_column]
    return table


def build_mjesecno(mirror: Path) -> list[list[str]]:
    """BS_TU11, monthly rows only, complete calendar years."""
    cells = index(read_mirror_csv(mirror, TU11), (0, 1, 2, 3), 4)
    out = [["godina", "mjesec_redni", "mjesec", "turist", "dolasci", "nocenja"]]
    for year in range(FIRST_YEAR, LAST_COMPLETE_YEAR + 1):
        for ordinal, month in enumerate(MJESECI, start=1):
            for turist in TU11_TURIST:
                out.append([
                    str(year), str(ordinal), month, turist,
                    cells[(month, str(year), turist, "dolasci")],
                    cells[(month, str(year), turist, "noćenja")],
                ])
    return out


def build_godisnje(mirror: Path) -> list[list[str]]:
    """BS_TU11, the published annual total rows, kept in their own file.

    The annual row is not the twelve monthly rows added up by this script: it is
    what DZS itself publishes on the 'Ukupno' member of the month dimension.
    Keeping it in a separate file is what makes double counting impossible
    rather than merely discouraged.
    """
    cells = index(read_mirror_csv(mirror, TU11), (0, 1, 2, 3), 4)
    out = [["godina", "turist", "dolasci", "nocenja"]]
    for year in range(FIRST_YEAR, LAST_COMPLETE_YEAR + 1):
        for turist in TU11_TURIST:
            out.append([
                str(year), turist,
                cells[("Ukupno", str(year), turist, "dolasci")],
                cells[("Ukupno", str(year), turist, "noćenja")],
            ])
    return out


def build_zupanije(mirror: Path) -> list[list[str]]:
    """BS_TU12, one county cross-section, annual rows.

    `razina` is the one derived column in the whole package. It is not new data:
    it marks which rows are the country total and which are its parts, which the
    published table leaves to the reader to know. Without it the obvious sum is
    a double count, and that is the mistake the column exists to prevent.
    """
    rows = read_mirror_csv(mirror, TU12)
    cells = index(rows, (0, 1, 2, 3, 4), 5)
    units = []
    for row in rows:
        if row[0] not in units:
            units.append(row[0])
    out = [["godina", "razina", "zupanija", "turist", "dolasci", "nocenja"]]
    for unit in units:
        razina = "država" if unit == DRZAVA else "županija"
        for turist in TU12_TURIST:
            out.append([
                COUNTY_YEAR, razina, unit, turist,
                cells[(unit, "UKUPNO", "Dolasci", COUNTY_YEAR, turist)],
                cells[(unit, "UKUPNO", "Noćenja", COUNTY_YEAR, turist)],
            ])
    return out


def build_putovanja(mirror: Path) -> list[list[str]]:
    """Household survey T03, one year, measures pivoted into their own columns.

    The published table carries all four measures in one value column, so a long
    copy would give that column four different units. Pivoting gives every column
    one unit, which is the storage convention the catalogue enforces. Nothing is
    aggregated, dropped or recomputed: 288 published cells become 72 rows of four.
    """
    cells = index(read_mirror_csv(mirror, T03), (0, 1, 2, 3, 4, 5), 6)
    out = [["godina", "dobna_skupina", "tip_putovanja", "destinacija", "trajanje",
            "putovanja", "nocenja", "izdaci_eur", "izdaci_hrk"]]
    for dob in DOBNE_SKUPINE:
        for tip in TIPOVI_PUTOVANJA:
            for destinacija in DESTINACIJE:
                for trajanje in TRAJANJA:
                    values = [
                        cells[(dob, SURVEY_YEAR, tip, mjera, destinacija, trajanje)]
                        for mjera in MJERE
                    ]
                    out.append([SURVEY_YEAR, dob, tip, destinacija, trajanje] + values)
    return out


EXTRACTS = {
    "data/dzs-turizam-mjesecno.csv": build_mjesecno,
    "data/dzs-turizam-godisnje.csv": build_godisnje,
    "data/dzs-turizam-zupanije-2025.csv": build_zupanije,
    "data/dzs-putovanja-stanovnistva-2024.csv": build_putovanja,
}


def serialise(rows: list[list[str]]) -> bytes:
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise SystemExit("A row has a different number of fields than the header.")
        for cell in row:
            if cell == "":
                raise SystemExit(
                    "Empty cell: a missing value carries its own published code."
                )
            if any(bad in cell for bad in (",", '"', "\n", "\r")):
                raise SystemExit(f"Value contains a separator, quote or break: {cell!r}")
    text = "".join(",".join(row) + "\n" for row in rows)
    return text.encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mirror", required=True,
                        help="Path to the author's local DZS tourism mirror.")
    parser.add_argument("--write", action="store_true",
                        help="Write the extracts; without it they are only verified.")
    args = parser.parse_args()

    mirror = Path(args.mirror)
    if not mirror.is_dir():
        raise SystemExit(f"Mirror directory does not exist: {mirror}")

    drift: list[str] = []
    for relative, builder in EXTRACTS.items():
        payload = serialise(builder(mirror))
        target = ROOT / relative
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
        elif not target.is_file():
            drift.append(f"{relative}: extract does not exist")
        elif target.read_bytes() != payload:
            drift.append(f"{relative}: extract no longer reproduces from the mirror")

    if drift:
        print("DZS_EXTRACTS_FAILED")
        for message in drift:
            print(f"- {message}")
        return 1

    print(f"DZS_EXTRACTS_OK extracts={len(EXTRACTS)} "
          f"mode={'write' if args.write else 'verify'} retrieved=2026-07-27")
    return 0


if __name__ == "__main__":
    sys.exit(main())
