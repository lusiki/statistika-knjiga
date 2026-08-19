#!/usr/bin/env python3
"""Build the governed ParlaSent-only Croatian teaching extract."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATE = ROOT / "data" / "_kandidat" / "p3-text"
DEFAULT_OUTPUT = ROOT / "data" / "parlament_oznake.csv"

SOURCE_FILES = {
    "ParlaSent_BCS.jsonl": {
        "md5": "c8b59c84c476b031cc553bc3c768e627",
        "sha256": "c6a6f51a819941c19f148405ed83adbabc38e3333305a44a7149b23d99b1cc98",
    },
    "ParlaSent_BCS_test.jsonl": {
        "md5": "ee8699a4a7b1a834f79fe74b8ebdfaf1",
        "sha256": "412b3ba399dab24041ff11a0eb1d530b402511615c8206cb1838092bc22ea7a0",
    },
}
TRAIN_KEYS = {
    "sentence", "country", "annotator1", "annotator2", "reconciliation",
    "label", "document_id", "sentence_id", "term", "date", "name",
    "party", "gender", "birth_year", "split", "ruling",
}
TEST_KEYS = {
    "sentence", "country", "annotator1", "label", "document_id",
    "sentence_id", "term", "date", "name", "party", "gender",
    "birth_year", "ruling",
}
OUTPUT_COLUMNS = [
    "record_id",
    "sentence_text",
    "country_source",
    "source_role",
    "source_line",
    "source_document_id",
    "source_sentence_id",
    "source_split",
    "derived_split",
    "annotator1_raw",
    "annotator2_raw",
    "reconciliation_raw",
    "recorded_label",
    "label_path",
]
MISSING_FROM_SOURCE = "nije_dostupno_iz_izvora"
SPLIT_SALT = "statistika-p3-text-parlasent-only-v1"
VALIDATION_THRESHOLD = 0.20


class BuildError(RuntimeError):
    pass


def checksum(path: Path, algorithm: str) -> str:
    digest = hashlib.new(algorithm)
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_sources(candidate: Path) -> dict[str, dict[str, str]]:
    observed: dict[str, dict[str, str]] = {}
    for name, expected in SOURCE_FILES.items():
        path = candidate / name
        if not path.is_file():
            raise BuildError(f"missing pinned source file: {path}")
        found = {algorithm: checksum(path, algorithm) for algorithm in ("md5", "sha256")}
        for algorithm, value in expected.items():
            if found[algorithm] != value:
                raise BuildError(
                    f"source {algorithm.upper()} mismatch for {name}: "
                    f"{found[algorithm]} != {value}"
                )
        observed[name] = found
    return observed


def load_jsonl(path: Path, expected_keys: set[str], role: str) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            row = json.loads(line)
            keys = set(row)
            if keys != expected_keys:
                raise BuildError(
                    f"{role} schema mismatch at line {line_number}: "
                    f"missing={sorted(expected_keys - keys)} extra={sorted(keys - expected_keys)}"
                )
            row["_source_role"] = role
            row["_source_line"] = line_number
            rows.append(row)
    return rows


def grouped_split(document_id: str) -> str:
    material = f"{SPLIT_SALT}|{document_id}".encode("utf-8")
    first_64_bits = int(hashlib.sha256(material).hexdigest()[:16], 16)
    threshold = int(VALIDATION_THRESHOLD * (1 << 64))
    return "provjera" if first_64_bits < threshold else "ucenje"


def build_rows(candidate: Path) -> tuple[list[dict], dict[str, object]]:
    source_hashes = verify_sources(candidate)
    train = load_jsonl(candidate / "ParlaSent_BCS.jsonl", TRAIN_KEYS, "train")
    test = load_jsonl(candidate / "ParlaSent_BCS_test.jsonl", TEST_KEYS, "test")

    countries = sorted({str(row["country"]) for row in train + test})
    if countries != ["BiH", "HR", "SRB"]:
        raise BuildError(f"unexpected literal BCS country values: {countries}")

    train_hr = [row for row in train if row["country"] == "HR"]
    test_hr = [row for row in test if row["country"] == "HR"]
    test_documents = {str(row["document_id"]) for row in test_hr}
    overlap_documents = {
        str(row["document_id"]) for row in train_hr
    } & test_documents
    retained_train = [
        row for row in train_hr if str(row["document_id"]) not in test_documents
    ]

    output: list[dict] = []
    for row in retained_train:
        output.append({
            "record_id": f"train-{row['_source_line']:04d}",
            "sentence_text": row["sentence"],
            "country_source": row["country"],
            "source_role": "train_file",
            "source_line": row["_source_line"],
            "source_document_id": row["document_id"],
            "source_sentence_id": row["sentence_id"],
            "source_split": row["split"],
            "derived_split": grouped_split(str(row["document_id"])),
            "annotator1_raw": row["annotator1"],
            "annotator2_raw": row["annotator2"],
            "reconciliation_raw": row["reconciliation"],
            "recorded_label": row["label"],
            "label_path": "dva_kodera_i_uskladjenje",
        })
    for row in test_hr:
        output.append({
            "record_id": f"test-{row['_source_line']:04d}",
            "sentence_text": row["sentence"],
            "country_source": row["country"],
            "source_role": "test_file",
            "source_line": row["_source_line"],
            "source_document_id": row["document_id"],
            "source_sentence_id": row["sentence_id"],
            "source_split": MISSING_FROM_SOURCE,
            "derived_split": "ispitivanje",
            "annotator1_raw": row["annotator1"],
            "annotator2_raw": MISSING_FROM_SOURCE,
            "reconciliation_raw": MISSING_FROM_SOURCE,
            "recorded_label": row["label"],
            "label_path": "jedan_uvjezbani_koder",
        })

    metadata: dict[str, object] = {
        "source_hashes": source_hashes,
        "train_hr_rows": len(train_hr),
        "test_hr_rows": len(test_hr),
        "overlap_documents_removed": len(overlap_documents),
        "overlap_rows_removed": len(train_hr) - len(retained_train),
        "retained_train_rows": len(retained_train),
        "output_rows": len(output),
        "split_salt": SPLIT_SALT,
        "validation_threshold": VALIDATION_THRESHOLD,
    }
    return output, metadata


def csv_bytes(rows: list[dict]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=OUTPUT_COLUMNS,
        extrasaction="raise",
        lineterminator="\n",
        quoting=csv.QUOTE_MINIMAL,
    )
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, default=DEFAULT_CANDIDATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    try:
        rows, metadata = build_rows(args.candidate.resolve())
        content = csv_bytes(rows)
        output = args.output.resolve()
        if args.write:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(content)
            action = "wrote"
        else:
            if not output.is_file():
                raise BuildError(f"missing promoted output: {output}")
            if output.read_bytes() != content:
                raise BuildError(f"promoted output differs from deterministic build: {output}")
            action = "verified"
    except (BuildError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"TEXT_BUILD_FAIL {error}", file=sys.stderr)
        return 1

    print(
        "TEXT_BUILD_OK"
        f" action={action} rows={metadata['output_rows']}"
        f" train_hr={metadata['train_hr_rows']} test_hr={metadata['test_hr_rows']}"
        f" removed_documents={metadata['overlap_documents_removed']}"
        f" removed_rows={metadata['overlap_rows_removed']}"
        f" retained_train={metadata['retained_train_rows']}"
        f" split_salt={metadata['split_salt']}"
        f" output_sha256={hashlib.sha256(content).hexdigest()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
