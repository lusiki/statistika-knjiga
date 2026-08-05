#!/usr/bin/env python3
"""Build the bounded CroAIcon extracts from the author's local project checkout.

Two teaching packages come out of the AI.econ / CroAIcon analytical project:

  * `rdp_potpore`  — concentration of Croatian state aid, 2017-2025, computed
    from the public state-aid registry at https://rdp.gov.hr/javno;
  * `bdp_dugi_niz` — Croatian GDP per capita 1870-2025, held as five separate
    published estimates and as one spliced series.

Neither package is fetched. CroAIcon's own `outputs/tables/` are gitignored in
that repository, so the author's local checkout is the source of record, exactly
as the DZS mirror is for `scripts/build-dzs-extracts.py`. This script never
touches the network and never reads the GFI/FINA tables: those stay
`external-only` under the catalogue's `gfi_fina` entry and nothing derived from
them enters this repository.

Run:
    python scripts/build-croaicon-extracts.py --checkout <path>            # verify
    python scripts/build-croaicon-extracts.py --checkout <path> --write    # write

Without --write every extract is rebuilt in memory and compared byte for byte
with the file on disk, so a drifted extract is caught rather than silently
overwritten.

Five shape rules, the same ones the DZS extracts obey:

  1. UTF-8 without BOM, LF line endings, comma as the field separator.
  2. No value contains a comma, a quote or a line break, so the files read in any
     tool without quoting rules.
  3. Source labels are copied VERBATIM. Croatian column names are added; the
     upstream column name is recorded in the licence notice, never replaced
     silently.
  4. A missing value carries a code and never an empty cell. `..` means the named
     estimate does not cover that year. Zero, missing and unpublished stay
     distinct.
  5. Full numeric precision is preserved. Rounding exists only in display.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NEDOSTUPNO = ".."

# --- the bounded selection --------------------------------------------------
#
# The state-aid package takes the six published aggregate tables and the headline
# fact file. It deliberately excludes `state_aid_concentration_by_sector.csv` and
# `state_aid_concentration_within_type.csv`: both are useful analytically but
# neither adds a teaching move the six below do not already carry, and the
# portfolio is capped.
#
# The GDP package takes the five separate estimates, the spliced series and the
# era table. It excludes the Chow-Lin monthly interpolation for 1991-1992, which
# is a modelled quantity, not an observation, and would need its own gate.

SA_GROUPS = "outputs/tables/state_aid_concentration_groups.csv"
SA_YEAR = "outputs/tables/state_aid_concentration_by_year.csv"
SA_SIZE = "outputs/tables/state_aid_concentration_by_size.csv"
SA_TYPE = "outputs/tables/state_aid_concentration_by_type.csv"
SA_COVER = "outputs/tables/state_aid_coverage_comparison.csv"
SA_FACTS = "outputs/facts/state_aid_concentration.json"

GDP_RAW = "outputs/tables/gdp_raw.csv"
GDP_LONG = "outputs/tables/gdp_long.csv"
GDP_ERAS = "outputs/tables/gdp_growth_eras.csv"


def read_table(checkout: Path, relative: str) -> list[dict[str, str]]:
    """Read one upstream table. CroAIcon writes some files with a BOM."""
    path = checkout / relative
    if not path.is_file():
        raise SystemExit(f"Checkout table is missing: {path}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise SystemExit(f"Checkout table has no data rows: {path}")
    return rows


def read_facts(checkout: Path, relative: str) -> dict:
    path = checkout / relative
    if not path.is_file():
        raise SystemExit(f"Checkout fact file is missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def num(value: str) -> str:
    """Copy a number through at full precision, without inventing a format."""
    text = value.strip()
    if text in ("", "NA", "NaN", "None"):
        return NEDOSTUPNO
    return text


# --- rdp_potpore ------------------------------------------------------------


def build_potpore_skupine(checkout: Path) -> list[list[str]]:
    """Top 1 percent, next 9, bottom 90 — recipients against amount.

    Both the numerator and the denominator of every share survive in the file:
    `primatelji` against the recipient total, `iznos_eur` against the amount
    total. A reader can rebuild each percentage by hand.
    """
    rows = read_table(checkout, SA_GROUPS)
    ukupno_primatelja = sum(int(r["recipient_count"]) for r in rows)
    ukupno_iznos = sum(float(r["amount_eur"]) for r in rows)
    out = [["skupina", "redoslijed", "primatelji", "primatelji_ukupno",
            "udio_primatelja_pct", "iznos_eur", "iznos_ukupno_eur",
            "udio_iznosa_pct"]]
    for r in sorted(rows, key=lambda x: int(x["display_order"])):
        out.append([
            r["group"].replace(" ", "_"),
            r["display_order"],
            r["recipient_count"],
            str(ukupno_primatelja),
            num(r["recipient_share_pct"]),
            num(r["amount_eur"]),
            repr(ukupno_iznos),
            num(r["amount_share_pct"]),
        ])
    return out


def build_potpore_godisnje(checkout: Path) -> list[list[str]]:
    """One row per year. NOT a national time series — see the coverage table."""
    rows = read_table(checkout, SA_YEAR)
    out = [["godina", "dodjele", "primatelji", "iznos_eur"]]
    for r in sorted(rows, key=lambda x: int(x["year"])):
        out.append([r["year"], r["award_count"], r["recipient_count"],
                    num(r["amount_eur"])])
    return out


def build_potpore_velicina(checkout: Path) -> list[list[str]]:
    """Recipient size class. `Nepoznato` is a published class, not a gap."""
    rows = read_table(checkout, SA_SIZE)
    out = [["velicina", "redoslijed", "dodjele", "primatelji", "iznos_eur",
            "udio_iznosa_pct", "prosjecna_dodjela_eur"]]
    for r in sorted(rows, key=lambda x: int(x["display_order"])):
        out.append([
            r["company_size"].replace(" ", "_"),
            r["display_order"],
            r["award_count"],
            r["recipient_count"],
            num(r["amount_eur"]),
            num(r["amount_share_pct"]),
            num(r["average_award_eur"]),
        ])
    return out


def build_potpore_vrsta(checkout: Path) -> list[list[str]]:
    """Aid type. The registry's own labels are long; they are copied verbatim
    with spaces turned into underscores so the file needs no quoting."""
    rows = read_table(checkout, SA_TYPE)
    out = [["vrsta", "dodjele", "primatelji", "iznos_eur", "udio_iznosa_pct"]]
    for r in sorted(rows, key=lambda x: -float(x["amount_eur"])):
        out.append([
            r["aid_type"].replace(" ", "_"),
            r["award_count"],
            r["recipient_count"],
            num(r["amount_eur"]),
            num(r["amount_share_pct"]),
        ])
    return out


def build_potpore_obuhvat(checkout: Path) -> list[list[str]]:
    """The registry snapshot against the ministry's official annual total.

    This is the table that stops the package being read as a national series.
    In 2021 the snapshot reproduces 0.9 percent of the official total and in
    2023 it reproduces 95 percent. The `scope` and `source_url` columns are
    constant across the three rows and live in the licence notice instead, so
    that no cell needs quoting.
    """
    rows = read_table(checkout, SA_COVER)
    out = [["godina", "sluzbeni_iznos_eur", "sluzbeni_udio_bdp_pct",
            "registar_dodjele", "registar_iznos_eur",
            "analiticke_dodjele", "analiticki_iznos_eur",
            "registar_prema_sluzbenom_pct", "analiticki_prema_sluzbenom_pct"]]
    for r in sorted(rows, key=lambda x: int(x["year"])):
        out.append([
            r["year"],
            num(r["official_total_amount_eur"]),
            num(r["official_gdp_share_pct"]),
            r["registry_award_count_all"],
            num(r["registry_amount_all_eur"]),
            r["registry_award_count_valid_oib"],
            num(r["registry_amount_valid_oib_eur"]),
            num(r["registry_to_official_pct"]),
            num(r["analytical_to_official_pct"]),
        ])
    return out


def build_potpore_sazetak(checkout: Path) -> list[list[str]]:
    """The headline numbers, one per row, each with its own unit.

    A long file rather than a wide one, because the quantities do not share a
    unit and a wide row would invite a nonsense column mean. The median against
    the mean is the point: 7.000 euro against roughly 210.000.
    """
    f = read_facts(checkout, SA_FACTS)
    prosjek = f["amount_eur"] / f["recipient_count"]
    out = [["pokazatelj", "vrijednost", "jedinica"]]
    stavke = [
        ("razdoblje_od", f["period_start"], "godina"),
        ("razdoblje_do", f["period_end"], "godina"),
        ("primatelji", f["recipient_count"], "broj"),
        ("dodjele", f["award_count_oib"], "broj"),
        ("iznos_ukupno", f["amount_eur"], "euro"),
        ("iznos_prosjek_po_primatelju", prosjek, "euro"),
        ("iznos_medijan_po_primatelju", f["median_recipient_amount_eur"], "euro"),
        ("gini", f["gini"], "koeficijent"),
        ("gornjih_1_pct_primatelja", f["top_1_recipient_count"], "broj"),
        ("gornjih_1_pct_udio_iznosa", f["top_1_amount_share_pct"], "posto"),
        ("gornjih_10_pct_primatelja", f["top_10pct_recipient_count"], "broj"),
        ("gornjih_10_pct_udio_iznosa", f["top_10pct_share_pct"], "posto"),
        ("dodjele_ukupno_ukljucene", f["included_awards_all"], "broj"),
        ("dodjele_s_valjanim_oib", f["included_awards_valid_oib"], "broj"),
        ("iznos_iskljucenog_upozorenja_max", f["excluded_warning_max_eur"], "euro"),
    ]
    for naziv, vrijednost, jedinica in stavke:
        out.append([naziv, repr(vrijednost) if isinstance(vrijednost, float)
                    else str(vrijednost), jedinica])
    return out


# --- bdp_dugi_niz -----------------------------------------------------------


def build_bdp_izvori(checkout: Path) -> list[list[str]]:
    """Five published estimates side by side, each in its own unit.

    The columns are NOT comparable levels and must never be averaged across.
    Their units differ: chain-linked euro, 2011 international dollars, 2017 US
    dollars, constant 2015 US dollars and Tica's own 1990 Geary-Khamis base.
    `..` marks a year the named estimate does not cover.
    """
    rows = read_table(checkout, GDP_RAW)
    out = [["godina", "eurostat_eur_clv", "maddison_int2011",
            "pwt_usd2017", "svjetska_banka_usd2015", "tica_gk1990"]]
    for r in sorted(rows, key=lambda x: int(x["year"])):
        out.append([
            r["year"],
            num(r["gdppc_modern_eur_clv"]),
            num(r["gdppc_maddison_int2011"]),
            num(r["gdppc_pwt_usd2017"]),
            num(r["gdppc_wb_usd2015"]),
            num(r["gdppc_tica"]),
        ])
    return out


def build_bdp_spojeni(checkout: Path) -> list[list[str]]:
    """The one spliced series, with the seam and the war years marked.

    `segment` names which estimate supplied each stretch, `granulacija`
    separates the four pre-1910 benchmark points from annual observations, and
    `prekid` marks 1991-1995, which is reconstructed rather than observed. The
    index is anchored at 2015 = 100, where the level is 11.760 euro.
    """
    rows = read_table(checkout, GDP_LONG)
    out = [["godina", "bdp_pc_eur", "segment", "granulacija",
            "indeks_2015_100", "prekid"]]
    for r in sorted(rows, key=lambda x: int(x["year"])):
        out.append([
            r["year"],
            num(r["value"]),
            r["segment"],
            r["granularity"],
            num(r["index"]),
            "da" if r["break_period"] == "TRUE" else "ne",
        ])
    return out


def build_bdp_razdoblja(checkout: Path) -> list[list[str]]:
    """Named eras with their compound annual growth and total change."""
    rows = read_table(checkout, GDP_ERAS)
    out = [["razdoblje", "godina_od", "godina_do", "prosjecni_godisnji_rast_pct",
            "ukupna_promjena_pct", "rast"]]
    for r in rows:
        out.append([
            r["era"].replace(" ", "_"),
            r["year0"],
            r["year1"],
            num(r["cagr"]),
            num(r["total"]),
            "da" if r["positive"] == "TRUE" else "ne",
        ])
    return out


EXTRACTS = {
    "data/rdp-potpore-skupine.csv": build_potpore_skupine,
    "data/rdp-potpore-godisnje.csv": build_potpore_godisnje,
    "data/rdp-potpore-velicina.csv": build_potpore_velicina,
    "data/rdp-potpore-vrsta.csv": build_potpore_vrsta,
    "data/rdp-potpore-obuhvat.csv": build_potpore_obuhvat,
    "data/rdp-potpore-sazetak.csv": build_potpore_sazetak,
    "data/bdp-hrvatska-izvori.csv": build_bdp_izvori,
    "data/bdp-hrvatska-spojeni.csv": build_bdp_spojeni,
    "data/bdp-hrvatska-razdoblja.csv": build_bdp_razdoblja,
}


def serialise(rows: list[list[str]]) -> bytes:
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise SystemExit("A row has a different number of fields than the header.")
        for cell in row:
            if cell == "":
                raise SystemExit(
                    "Empty cell: a missing value carries its own code."
                )
            if any(bad in cell for bad in (",", '"', "\n", "\r")):
                raise SystemExit(f"Value contains a separator, quote or break: {cell!r}")
    text = "".join(",".join(row) + "\n" for row in rows)
    return text.encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", required=True,
                        help="Path to the author's local CroAIcon checkout.")
    parser.add_argument("--write", action="store_true",
                        help="Write the extracts; without it they are only verified.")
    args = parser.parse_args()

    checkout = Path(args.checkout)
    if not checkout.is_dir():
        raise SystemExit(f"Checkout directory does not exist: {checkout}")

    drift: list[str] = []
    for relative, builder in EXTRACTS.items():
        payload = serialise(builder(checkout))
        target = ROOT / relative
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
        elif not target.is_file():
            drift.append(f"{relative}: extract does not exist")
        elif target.read_bytes() != payload:
            drift.append(f"{relative}: extract no longer reproduces from the checkout")

    if drift:
        print("CROAICON_EXTRACTS_FAILED")
        for message in drift:
            print(f"- {message}")
        return 1

    print(f"CROAICON_EXTRACTS_OK extracts={len(EXTRACTS)} "
          f"mode={'write' if args.write else 'verify'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
