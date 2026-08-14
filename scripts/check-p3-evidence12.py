#!/usr/bin/env python3
"""Verify the bounded Chapter 12 RRR evidence artifact.

The repository deliberately does not bundle the OSF participant-level data.
Without ``--audit-root`` this checker validates the committed, non-identifying
derived record and its aggregate invariants. With ``--audit-root`` it also
checks the three portal-downloaded source artifacts and reconstructs every
derived row from ``data.zip``. The audit root must contain ``data.zip``,
``analysis.zip`` and ``plan.pdf`` downloaded from the exact URLs recorded in
the P3-EVIDENCE12 report.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
from pathlib import Path
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "notes" / "reports" / "p3-evidence12-rrr-lab-effects.csv"
Z = 1.959963984540054

EXPECTED_SOURCE_HASHES = {
    "analysis.zip": "c648a1d8a65c496dc6b4bdabd86c7ae71716f50cbd6ca5d0287d5e9f66da7c69",
    "data.zip": "6e3e14d9a7eebd03aa45bcf1928ad62395745052e20dc20107878a8118ae7348",
    "plan.pdf": "86d9d3289d51bd1b4243aced531bec3e58cf7cd68216ac689022215742c27bfc",
}

FIELDS = [
    "study_order",
    "lab",
    "n_smile",
    "n_pout",
    "n_total",
    "mean_smile",
    "sd_smile",
    "mean_pout",
    "sd_pout",
    "raw_mean_difference",
    "raw_se",
    "raw_ci_low",
    "raw_ci_high",
    "cohen_d",
    "d_se",
    "d_ci_low",
    "d_ci_high",
]

LAB_LABELS = {
    "Albohn": "Albohn",
    "Allard": "Allard",
    "Benning": "Benning",
    "Bulnes": "Bulnes",
    "Capaldi": "Capaldi",
    "Chasten": "Chasten",
    "Holmes": "Holmes",
    "Koch": "Koch",
    "Korb": "Korb",
    "Lynott": "Lynott",
    "Oosterwijk": "Oosterwijk",
    "Özdogru": "Özdoğru",
    "Pacheco-Unguetti": "Pacheco-Unguetti",
    "Talarico": "Talarico",
    "Wagenmakers": "Wagenmakers",
    "Wayand": "Wayand",
    "Zeelenberg": "Zeelenberg",
}
LAB_ORDER = [
    "Albohn",
    "Allard",
    "Benning",
    "Bulnes",
    "Capaldi",
    "Chasten",
    "Holmes",
    "Koch",
    "Korb",
    "Lynott",
    "Oosterwijk",
    "Özdogru",
    "Pacheco-Unguetti",
    "Talarico",
    "Wagenmakers",
    "Wayand",
    "Zeelenberg",
]
PUBLISHED_TABLE1 = {
    "Albohn": (139, 4.20, 1.30, 4.06, 1.84),
    "Allard": (125, 5.05, 1.56, 4.89, 1.76),
    "Benning": (115, 4.69, 1.34, 4.70, 1.43),
    "Bulnes": (101, 4.61, 1.52, 4.49, 1.29),
    "Capaldi": (117, 4.91, 1.54, 5.02, 1.64),
    "Chasten": (94, 5.01, 1.54, 5.06, 1.41),
    "Holmes": (99, 4.91, 1.49, 4.71, 1.31),
    "Koch": (100, 4.93, 1.32, 5.12, 1.43),
    "Korb": (101, 4.14, 1.72, 4.12, 1.71),
    "Lynott": (126, 4.54, 1.42, 4.18, 1.73),
    "Oosterwijk": (110, 4.63, 1.48, 4.87, 1.32),
    "Özdoğru": (87, 3.77, 1.95, 4.34, 1.94),
    "Pacheco-Unguetti": (120, 3.78, 1.65, 3.91, 1.84),
    "Talarico": (112, 4.36, 1.30, 4.34, 1.60),
    "Wagenmakers": (130, 4.94, 1.14, 4.79, 1.30),
    "Wayand": (110, 4.75, 1.39, 4.95, 1.49),
    "Zeelenberg": (108, 4.93, 1.40, 4.58, 1.41),
}


def fail(message: str) -> None:
    raise ValueError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def number(value: str | None) -> float | None:
    if value is None:
        return None
    value = value.strip()
    if not value or value.upper() == "NA":
        return None
    return float(value)


def mean(values: list[float]) -> float:
    if not values:
        fail("mean requested for an empty vector")
    return sum(values) / len(values)


def sample_sd(values: list[float]) -> float:
    if len(values) < 2:
        fail("sample standard deviation requires at least two values")
    centre = mean(values)
    return math.sqrt(sum((value - centre) ** 2 for value in values) / (len(values) - 1))


def participant_mean(row: dict[str, str]) -> float:
    values: list[float] = []
    for index in range(1, 5):
        correct = number(row[f"performedCorrectlyCartoon{index}"])
        rating = number(row[f"ratingCartoon{index}"])
        if correct == 1 and rating is not None:
            values.append(rating)
    return mean(values)


def analyse_lab(payload: bytes, order: int, source_name: str) -> dict[str, str]:
    try:
        text = payload.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = payload.decode("cp1252")
    raw_rows = list(csv.reader(io.StringIO(text, newline="")))
    if len(raw_rows) < 3:
        fail(f"{source_name}: empty CSV")
    canonical_names = [
        "subjectNo",
        "participantID",
        "condition",
        "performedCorrectlyCartoon1",
        "performedCorrectlyCartoon2",
        "performedCorrectlyCartoon3",
        "performedCorrectlyCartoon4",
        "performedCorrectlyTotal",
        "ratingTask1",
        "ratingTask2",
        "ratingCartoon1",
        "ratingCartoon2",
        "ratingCartoon3",
        "ratingCartoon4",
        "selfReportedPerformance",
        "comprehensionCartoons",
        "awareOfGoal",
        "participantsGuessedGoal",
        "age",
        "gender",
        "student",
        "occupationFieldOfStudy",
    ]
    normalised_rows: list[list[str]] = []
    for row in raw_rows:
        if not row or not any(cell.strip() for cell in row):
            continue
        if len(row) < len(canonical_names):
            fail(
                f"{source_name}: {len(row)} columns, "
                f"expected at least {len(canonical_names)}"
            )
        # Some archived exports carry spreadsheet-width empty columns, and a
        # few free-text occupation cells contain unquoted commas after the 22
        # analysis columns. The official analysis never uses those fields;
        # this verifier likewise takes exactly the first 22 positional fields.
        normalised_rows.append(row[: len(canonical_names)])
    raw_rows = normalised_rows
    # R's read.csv consumes row 1 as names; the official script then removes
    # row 2 (the units/subheaders) and assigns these canonical names by index.
    source_rows = [dict(zip(canonical_names, row)) for row in raw_rows[2:]]
    rating_names = [f"ratingCartoon{index}" for index in range(1, 5)]
    usable = [
        row
        for row in source_rows
        if any(number(row[name]) is not None for name in rating_names)
    ]
    filtered = [
        row
        for row in usable
        if number(row["performedCorrectlyTotal"]) is not None
        and number(row["performedCorrectlyTotal"]) >= 3
        and number(row["comprehensionCartoons"]) == 1
        and number(row["awareOfGoal"]) == 0
    ]
    prepared = [
        (int(number(row["condition"])), participant_mean(row))  # type: ignore[arg-type]
        for row in filtered
    ]

    preliminary = {
        condition: [rating for observed, rating in prepared if observed == condition]
        for condition in (0, 1)
    }
    centres = {condition: mean(values) for condition, values in preliminary.items()}
    sds = {condition: sample_sd(values) for condition, values in preliminary.items()}
    retained = [
        (condition, rating)
        for condition, rating in prepared
        if rating <= centres[condition] + 2.5 * sds[condition]
        and rating >= centres[condition] - 2.5 * sds[condition]
    ]
    groups = {
        condition: [rating for observed, rating in retained if observed == condition]
        for condition in (0, 1)
    }

    smile = groups[1]
    pout = groups[0]
    n_smile, n_pout = len(smile), len(pout)
    mean_smile, mean_pout = mean(smile), mean(pout)
    sd_smile, sd_pout = sample_sd(smile), sample_sd(pout)
    pooled_sd = math.sqrt(
        ((n_smile - 1) * sd_smile**2 + (n_pout - 1) * sd_pout**2)
        / (n_smile + n_pout - 2)
    )
    raw = mean_smile - mean_pout
    raw_se = pooled_sd * math.sqrt(1 / n_smile + 1 / n_pout)
    d_value = raw / pooled_sd
    d_variance = (
        (n_smile + n_pout) / (n_smile * n_pout)
        + d_value**2 / (2 * (n_smile + n_pout))
    )
    d_se = math.sqrt(d_variance)

    source_stem = Path(source_name).stem.removesuffix("_Data")
    if source_stem not in LAB_LABELS:
        fail(f"unexpected lab file: {source_name}")

    values: dict[str, str | int | float] = {
        "study_order": order,
        "lab": LAB_LABELS[source_stem],
        "n_smile": n_smile,
        "n_pout": n_pout,
        "n_total": n_smile + n_pout,
        "mean_smile": mean_smile,
        "sd_smile": sd_smile,
        "mean_pout": mean_pout,
        "sd_pout": sd_pout,
        "raw_mean_difference": raw,
        "raw_se": raw_se,
        "raw_ci_low": raw - Z * raw_se,
        "raw_ci_high": raw + Z * raw_se,
        "cohen_d": d_value,
        "d_se": d_se,
        "d_ci_low": d_value - Z * d_se,
        "d_ci_high": d_value + Z * d_se,
    }
    return {
        field: str(values[field]) if field in {"study_order", "lab", "n_smile", "n_pout", "n_total"}
        else f"{float(values[field]):.6f}"
        for field in FIELDS
    }


def reconstruct(audit_root: Path) -> list[dict[str, str]]:
    for name, expected in EXPECTED_SOURCE_HASHES.items():
        path = audit_root / name
        if not path.is_file():
            fail(f"missing portal-downloaded source artifact: {path}")
        observed = sha256(path)
        if observed != expected:
            fail(f"{name}: SHA-256 {observed} does not match {expected}")

    with zipfile.ZipFile(audit_root / "data.zip") as archive:
        available = {
            Path(name).stem.removesuffix("_Data"): name
            for name in archive.namelist()
            if name.startswith("Data/") and name.endswith("_Data.csv")
        }
        if set(available) != set(LAB_ORDER):
            fail("data.zip lab inventory does not match the published 17-lab table")
        names = [available[lab] for lab in LAB_ORDER]
        return [
            analyse_lab(archive.read(name), order, Path(name).name)
            for order, name in enumerate(names, start=1)
        ]


def load_artifact() -> list[dict[str, str]]:
    if not ARTIFACT.is_file():
        fail(f"missing derived artifact: {ARTIFACT}")
    with ARTIFACT.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            fail(f"unexpected artifact columns: {reader.fieldnames}")
        return list(reader)


def reml(values: list[float], variances: list[float]) -> tuple[float, float, float]:
    def objective(tau2: float) -> float:
        weights = [1 / (variance + tau2) for variance in variances]
        total_weight = sum(weights)
        pooled = sum(weight * value for weight, value in zip(weights, values)) / total_weight
        residual = sum(
            weight * (value - pooled) ** 2
            for weight, value in zip(weights, values)
        )
        return 0.5 * (
            sum(math.log(variance + tau2) for variance in variances)
            + math.log(total_weight)
            + residual
        )

    lower, upper = 0.0, max(1.0, 10 * max(values) ** 2, 10 * max(variances))
    ratio = (math.sqrt(5) - 1) / 2
    left = upper - ratio * (upper - lower)
    right = lower + ratio * (upper - lower)
    for _ in range(250):
        if objective(left) <= objective(right):
            upper, right = right, left
            left = upper - ratio * (upper - lower)
        else:
            lower, left = left, right
            right = lower + ratio * (upper - lower)
    candidate = (lower + upper) / 2
    tau2 = candidate if objective(candidate) < objective(0.0) else 0.0
    weights = [1 / (variance + tau2) for variance in variances]
    pooled = sum(weight * value for weight, value in zip(weights, values)) / sum(weights)
    se = math.sqrt(1 / sum(weights))
    return pooled, se, tau2


def validate(rows: list[dict[str, str]]) -> dict[str, float]:
    if len(rows) != 17:
        fail(f"derived artifact has {len(rows)} rows, expected 17")
    if [int(row["study_order"]) for row in rows] != list(range(1, 18)):
        fail("study_order must be the exact sequence 1..17")
    if len({row["lab"] for row in rows}) != 17:
        fail("lab identifiers are not unique")

    total_n = sum(int(row["n_total"]) for row in rows)
    if total_n != 1894:
        fail(f"included N is {total_n}, expected 1894")
    for row in rows:
        if int(row["n_smile"]) + int(row["n_pout"]) != int(row["n_total"]):
            fail(f"{row['lab']}: group counts do not add to n_total")
        for estimate, low, high in (
            ("raw_mean_difference", "raw_ci_low", "raw_ci_high"),
            ("cohen_d", "d_ci_low", "d_ci_high"),
        ):
            if not float(row[low]) < float(row[estimate]) < float(row[high]):
                fail(f"{row['lab']}: {estimate} is outside its interval")
        published = PUBLISHED_TABLE1[row["lab"]]
        observed = (
            int(row["n_total"]),
            *(
                float(f"{float(row[field]):.2f}")
                for field in ("mean_smile", "sd_smile", "mean_pout", "sd_pout")
            ),
        )
        if observed != published:
            known_talarico_discrepancy = (
                row["lab"] == "Talarico"
                and observed == (112, 4.36, 1.30, 4.34, 1.59)
                and published == (112, 4.36, 1.30, 4.34, 1.60)
            )
            if not known_talarico_discrepancy:
                fail(
                    f"{row['lab']}: derived descriptives {observed} do not "
                    f"reconcile to published Table 1 {published}"
                )

    raw = [float(row["raw_mean_difference"]) for row in rows]
    raw_variances = [float(row["raw_se"]) ** 2 for row in rows]
    d_values = [float(row["cohen_d"]) for row in rows]
    d_variances = [float(row["d_se"]) ** 2 for row in rows]
    pooled_raw, pooled_raw_se, raw_tau2 = reml(raw, raw_variances)
    pooled_d, pooled_d_se, d_tau2 = reml(d_values, d_variances)

    if round(pooled_raw, 2) != 0.03:
        fail(f"pooled raw difference rounds to {pooled_raw:.2f}, expected 0.03")
    if round(pooled_raw - Z * pooled_raw_se, 2) != -0.11:
        fail("pooled raw lower limit does not reconcile to -0.11")
    if round(pooled_raw + Z * pooled_raw_se, 2) != 0.16:
        fail("pooled raw upper limit does not reconcile to 0.16")

    positive_raw = sum(value > 0 for value in raw)
    strictly_positive = sum(float(row["raw_ci_low"]) > 0 for row in rows)
    overlap_original = sum(
        float(row["raw_ci_low"]) <= 0.82 <= float(row["raw_ci_high"])
        for row in rows
    )
    if positive_raw != 9 or strictly_positive != 0 or overlap_original != 2:
        fail(
            "derived direction and interval counts do not reconcile to the "
            "published 9/17, 0/17 and 2/17 statements"
        )

    return {
        "total_n": float(total_n),
        "positive_raw": float(positive_raw),
        "strictly_positive_raw_ci": float(strictly_positive),
        "raw_overlap_original_082": float(overlap_original),
        "pooled_raw": pooled_raw,
        "pooled_raw_se": pooled_raw_se,
        "pooled_raw_low": pooled_raw - Z * pooled_raw_se,
        "pooled_raw_high": pooled_raw + Z * pooled_raw_se,
        "raw_tau2": raw_tau2,
        "pooled_d": pooled_d,
        "pooled_d_se": pooled_d_se,
        "pooled_d_low": pooled_d - Z * pooled_d_se,
        "pooled_d_high": pooled_d + Z * pooled_d_se,
        "d_tau2": d_tau2,
    }


def compare(expected: list[dict[str, str]], observed: list[dict[str, str]]) -> None:
    if len(expected) != len(observed):
        fail("reconstructed and committed row counts differ")
    for expected_row, observed_row in zip(expected, observed):
        for field in FIELDS:
            if field in {"study_order", "lab", "n_smile", "n_pout", "n_total"}:
                if expected_row[field] != observed_row[field]:
                    fail(
                        f"{observed_row.get('lab', '?')} {field}: "
                        f"{observed_row[field]} != {expected_row[field]}"
                    )
            elif abs(float(expected_row[field]) - float(observed_row[field])) > 5e-7:
                fail(
                    f"{observed_row.get('lab', '?')} {field}: "
                    f"{observed_row[field]} != {expected_row[field]}"
                )


def print_csv(rows: list[dict[str, str]]) -> None:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    sys.stdout.write(output.getvalue())


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-root", type=Path)
    parser.add_argument("--print-derived", action="store_true")
    parser.add_argument(
        "--fixture",
        choices=("wrong-total", "broken-interval"),
        help="apply one in-memory defect; the checker must fail closed",
    )
    args = parser.parse_args()

    try:
        reconstructed = reconstruct(args.audit_root) if args.audit_root else None
        if args.print_derived:
            if reconstructed is None:
                fail("--print-derived requires --audit-root")
            print_csv(reconstructed)
            return 0

        committed = load_artifact()
        if args.fixture == "wrong-total":
            committed[0]["n_total"] = str(int(committed[0]["n_total"]) + 1)
        elif args.fixture == "broken-interval":
            committed[0]["raw_ci_low"] = committed[0]["raw_ci_high"]
        if reconstructed is not None:
            compare(reconstructed, committed)
        summary = validate(committed)
    except (OSError, ValueError, zipfile.BadZipFile, csv.Error) as exc:
        print(f"P3_EVIDENCE12_FAILED: {exc}", file=sys.stderr)
        return 1

    print(
        "P3_EVIDENCE12_OK "
        f"labs={len(committed)} total_n={int(summary['total_n'])} "
        f"raw={summary['pooled_raw']:.6f} "
        f"raw_ci=[{summary['pooled_raw_low']:.6f},{summary['pooled_raw_high']:.6f}] "
        f"d={summary['pooled_d']:.6f} "
        f"d_ci=[{summary['pooled_d_low']:.6f},{summary['pooled_d_high']:.6f}]"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
