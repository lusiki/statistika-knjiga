#!/usr/bin/env python3
"""Validate the ParlaSent-only package and preserve the historical link audit."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from collections import Counter
from pathlib import Path
import re
import sys
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATE = ROOT / "data" / "_kandidat" / "p3-text"
DEFAULT_OUTPUT = ROOT / "data" / "parlament_oznake.csv"
EXPECTED_MD5 = {
    "ParlaMint-HR.tgz": "b852098ae5c2561aef1de43f44e09a77",
    "ParlaSent_BCS.jsonl": "c8b59c84c476b031cc553bc3c768e627",
    "ParlaSent_BCS_test.jsonl": "ee8699a4a7b1a834f79fe74b8ebdfaf1",
    "README.txt": "583856c8d470334e5638f6a078f727d5",
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
EXPECTED_BLOCKER = {
    "train_rows": 1387,
    "train_linked": 1340,
    "train_no_link": 18,
    "train_ambiguous": 29,
    "test_rows": 1336,
    "test_linked": 1297,
    "test_no_link": 24,
    "test_ambiguous": 15,
}
PARLASENT_SHA256 = {
    "ParlaSent_BCS.jsonl": "c6a6f51a819941c19f148405ed83adbabc38e3333305a44a7149b23d99b1cc98",
    "ParlaSent_BCS_test.jsonl": "412b3ba399dab24041ff11a0eb1d530b402511615c8206cb1838092bc22ea7a0",
    "README.txt": "848a892cede62d37f469532eba6d2f5e6f00d29234f0257a67737f8a8646c285",
}
OUTPUT_COLUMNS = [
    "record_id", "sentence_text", "country_source", "source_role",
    "source_line", "source_document_id", "source_sentence_id",
    "source_split", "derived_split", "annotator1_raw", "annotator2_raw",
    "reconciliation_raw", "recorded_label", "label_path",
]
MISSING_FROM_SOURCE = "nije_dostupno_iz_izvora"
SPLIT_SALT = "statistika-p3-text-parlasent-only-v1"
VALIDATION_THRESHOLD = 0.20
EXPECTED_OUTPUT_MD5 = "55b1c4263009ab783911f094907312d9"
EXPECTED_OUTPUT_SHA256 = "0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef"
EXPECTED_PACKAGE = {
    "train_hr_rows": 1387,
    "test_hr_rows": 1336,
    "overlap_documents_removed": 20,
    "overlap_rows_removed": 25,
    "retained_train_rows": 1362,
    "output_rows": 2698,
    "split_rows": {"ucenje": 1090, "provjera": 272, "ispitivanje": 1336},
    "split_documents": {"ucenje": 944, "provjera": 234, "ispitivanje": 1321},
    "split_labels": {
        "ucenje": {"Negative": 530, "Neutral": 343, "Positive": 217},
        "provjera": {"Negative": 122, "Neutral": 90, "Positive": 60},
        "ispitivanje": {"Negative": 560, "Neutral": 546, "Positive": 230},
    },
}


class AuditError(RuntimeError):
    pass


def md5(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def whitespace_key(value: str | None) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", value or "")).strip()


def token_key(value: str | None) -> str:
    value = whitespace_key(value).casefold()
    return " ".join(re.findall(r"[^\W_]+", value, flags=re.UNICODE))


def load_jsonl(path: Path, expected_keys: set[str], role: str) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            row = json.loads(line)
            if os.environ.get("TEXT_PACKAGE_NEGATIVE_FIXTURE") == "missing_test_country" and role == "test" and line_number == 1:
                row.pop("country", None)
            keys = set(row)
            if keys != expected_keys:
                raise AuditError(
                    f"{role} schema mismatch at line {line_number}: "
                    f"missing={sorted(expected_keys - keys)} extra={sorted(keys - expected_keys)}"
                )
            row["_source_role"] = role
            row["_source_line"] = line_number
            rows.append(row)
    return rows


def load_speeches(text_root: Path, dates: set[str]) -> dict[str, list[dict]]:
    if not text_root.is_dir():
        raise AuditError(
            "missing extracted ParlaMint-HR.txt candidate directory; "
            "extract it from the verified ParlaMint-HR.tgz"
        )
    result: dict[str, list[dict]] = {}
    for date in sorted(dates):
        speeches: list[dict] = []
        text_files = sorted((text_root / date[:4]).glob(f"ParlaMint-HR_{date}-*.txt"))
        if not text_files:
            raise AuditError(f"no ParlaMint-HR plain-text file for source date {date}")
        for text_path in text_files:
            meta_path = text_path.with_name(f"{text_path.stem}-meta.tsv")
            if not meta_path.is_file():
                raise AuditError(f"missing metadata twin for {text_path.name}")
            metadata: dict[str, dict] = {}
            with meta_path.open(encoding="utf-8-sig", newline="") as stream:
                for row in csv.DictReader(stream, delimiter="\t"):
                    metadata[row["ID"]] = row
            with text_path.open(encoding="utf-8-sig") as stream:
                for line_number, line in enumerate(stream, 1):
                    speech_id, separator, text = line.rstrip("\r\n").partition("\t")
                    if not separator:
                        raise AuditError(f"malformed speech row {text_path}:{line_number}")
                    meta = metadata.get(speech_id)
                    if meta is None:
                        raise AuditError(f"speech {speech_id} lacks metadata in {meta_path.name}")
                    speeches.append({
                        "speech_id": speech_id,
                        "text": whitespace_key(text),
                        "text_tokens": token_key(text),
                        "speaker_key": token_key(meta.get("Speaker_name")),
                    })
        result[date] = speeches
    return result


def resolve(row: dict, speeches: dict[str, list[dict]]) -> tuple[str, str | None]:
    target = token_key(row["sentence"])
    matches = [speech for speech in speeches[row["date"]] if target in speech["text_tokens"]]
    document_suffix = f".u{row['document_id']}"
    direct = [speech for speech in matches if speech["speech_id"].endswith(document_suffix)]
    named = [speech for speech in matches if speech["speaker_key"] == token_key(row["name"])]
    if len(direct) == 1:
        return "direct_id_text", direct[0]["speech_id"]
    if len(named) == 1:
        return "unique_named_text", named[0]["speech_id"]
    if len(matches) == 1:
        return "unique_text", matches[0]["speech_id"]
    if not matches:
        return "no_link", None
    return "ambiguous", None


def audit(
    candidate: Path,
    parlamint_archive: Path | None = None,
    parlamint_text_root: Path | None = None,
    parlamint_md5: str | None = None,
) -> tuple[dict[str, int], list[dict], dict[str, str]]:
    source_hashes: dict[str, str] = {}
    expected_sources = dict(EXPECTED_MD5)
    archive_name = "ParlaMint-HR.tgz"
    if parlamint_archive is not None:
        expected_sources.pop(archive_name)
        if parlamint_md5 is None:
            raise AuditError("research ParlaMint archive requires its published MD5")
        observed = md5(parlamint_archive)
        if observed != parlamint_md5:
            raise AuditError(
                f"source MD5 mismatch for {parlamint_archive.name}: "
                f"{observed} != {parlamint_md5}"
            )
        source_hashes[parlamint_archive.name] = sha256(parlamint_archive)
    for name, expected in expected_sources.items():
        path = candidate / name
        if not path.is_file():
            raise AuditError(f"missing pinned source file: {path}")
        observed = md5(path)
        if os.environ.get("TEXT_PACKAGE_NEGATIVE_FIXTURE") == "source_md5_mismatch" and name == "ParlaSent_BCS.jsonl":
            observed = "0" * 32
        if observed != expected:
            raise AuditError(f"source MD5 mismatch for {name}: {observed} != {expected}")
        source_hashes[name] = sha256(path)

    train = load_jsonl(candidate / "ParlaSent_BCS.jsonl", TRAIN_KEYS, "train")
    test = load_jsonl(candidate / "ParlaSent_BCS_test.jsonl", TEST_KEYS, "test")
    selected = [row for row in train + test if row["country"] == "HR"]
    countries = sorted({row["country"] for row in train + test})
    if countries != ["BiH", "HR", "SRB"]:
        raise AuditError(f"unexpected literal BCS country values: {countries}")
    text_root = parlamint_text_root or (candidate / "ParlaMint-HR.txt")
    speeches = load_speeches(text_root, {row["date"] for row in selected})

    counts: Counter[str] = Counter()
    failures: list[dict] = []
    resolved: list[dict] = []
    for row in selected:
        outcome, speech_id = resolve(row, speeches)
        prefix = row["_source_role"]
        counts[f"{prefix}_rows"] += 1
        if speech_id is None:
            counts[f"{prefix}_{outcome}"] += 1
            failures.append({
                "source_role": prefix,
                "source_line": row["_source_line"],
                "document_id": row["document_id"],
                "sentence_id": row["sentence_id"],
                "date": row["date"],
                "outcome": outcome,
            })
        else:
            counts[f"{prefix}_linked"] += 1
            resolved.append({"source_role": prefix, "speech_id": speech_id})

    train_documents = {row["document_id"] for row in selected if row["_source_role"] == "train"}
    test_documents = {row["document_id"] for row in selected if row["_source_role"] == "test"}
    counts["source_document_overlap"] = len(train_documents & test_documents)
    train_speeches = {row["speech_id"] for row in resolved if row["source_role"] == "train"}
    test_speeches = {row["speech_id"] for row in resolved if row["source_role"] == "test"}
    counts["resolved_speech_overlap"] = len(train_speeches & test_speeches)
    return dict(counts), failures, source_hashes


def grouped_split(document_id: str) -> str:
    material = f"{SPLIT_SALT}|{document_id}".encode("utf-8")
    first_64_bits = int(hashlib.sha256(material).hexdigest()[:16], 16)
    threshold = int(VALIDATION_THRESHOLD * (1 << 64))
    return "provjera" if first_64_bits < threshold else "ucenje"


def verify_parlasent_sources(candidate: Path) -> dict[str, str]:
    expected_md5 = {
        "ParlaSent_BCS.jsonl": EXPECTED_MD5["ParlaSent_BCS.jsonl"],
        "ParlaSent_BCS_test.jsonl": EXPECTED_MD5["ParlaSent_BCS_test.jsonl"],
        "README.txt": EXPECTED_MD5["README.txt"],
    }
    observed_sha256: dict[str, str] = {}
    for name, expected in expected_md5.items():
        path = candidate / name
        if not path.is_file():
            raise AuditError(f"missing pinned source file: {path}")
        observed_md5 = md5(path)
        if (
            os.environ.get("TEXT_PACKAGE_NEGATIVE_FIXTURE") == "source_md5_mismatch"
            and name == "ParlaSent_BCS.jsonl"
        ):
            observed_md5 = "0" * 32
        if observed_md5 != expected:
            raise AuditError(
                f"source MD5 mismatch for {name}: {observed_md5} != {expected}"
            )
        observed_sha256[name] = sha256(path)
        if observed_sha256[name] != PARLASENT_SHA256[name]:
            raise AuditError(
                f"source SHA-256 mismatch for {name}: "
                f"{observed_sha256[name]} != {PARLASENT_SHA256[name]}"
            )
    return observed_sha256


def expected_package_rows(candidate: Path) -> tuple[list[dict], dict[str, object]]:
    source_hashes = verify_parlasent_sources(candidate)
    train = load_jsonl(candidate / "ParlaSent_BCS.jsonl", TRAIN_KEYS, "train")
    test = load_jsonl(candidate / "ParlaSent_BCS_test.jsonl", TEST_KEYS, "test")
    if os.environ.get("TEXT_PACKAGE_NEGATIVE_FIXTURE") == "dropped_test_row":
        first_hr = next(index for index, row in enumerate(test) if row["country"] == "HR")
        del test[first_hr]

    countries = sorted({str(row["country"]) for row in train + test})
    if countries != ["BiH", "HR", "SRB"]:
        raise AuditError(f"unexpected literal BCS country values: {countries}")
    train_hr = [row for row in train if row["country"] == "HR"]
    test_hr = [row for row in test if row["country"] == "HR"]
    test_documents = {str(row["document_id"]) for row in test_hr}
    train_documents = {str(row["document_id"]) for row in train_hr}
    overlap_documents = train_documents & test_documents
    if os.environ.get("TEXT_PACKAGE_NEGATIVE_FIXTURE") == "document_leakage":
        retained_train = list(train_hr)
    else:
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
            "source_line": str(row["_source_line"]),
            "source_document_id": str(row["document_id"]),
            "source_sentence_id": str(row["sentence_id"]),
            "source_split": str(row["split"]),
            "derived_split": grouped_split(str(row["document_id"])),
            "annotator1_raw": str(row["annotator1"]),
            "annotator2_raw": str(row["annotator2"]),
            "reconciliation_raw": str(row["reconciliation"]),
            "recorded_label": str(row["label"]),
            "label_path": "dva_kodera_i_uskladjenje",
        })
    for row in test_hr:
        output.append({
            "record_id": f"test-{row['_source_line']:04d}",
            "sentence_text": row["sentence"],
            "country_source": row["country"],
            "source_role": "test_file",
            "source_line": str(row["_source_line"]),
            "source_document_id": str(row["document_id"]),
            "source_sentence_id": str(row["sentence_id"]),
            "source_split": MISSING_FROM_SOURCE,
            "derived_split": "ispitivanje",
            "annotator1_raw": str(row["annotator1"]),
            "annotator2_raw": MISSING_FROM_SOURCE,
            "reconciliation_raw": MISSING_FROM_SOURCE,
            "recorded_label": str(row["label"]),
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
    }
    return output, metadata


def serialized_rows(rows: list[dict]) -> bytes:
    from io import StringIO

    buffer = StringIO(newline="")
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


def validate_package(candidate: Path, output_path: Path) -> tuple[dict[str, object], str, str]:
    for forbidden in (
        ROOT / "data" / "parlament_govori.csv",
        ROOT / "data" / "parlament_mjere.csv",
    ):
        if forbidden.exists():
            raise AuditError(f"removed ParlaMint-only output exists: {forbidden}")
    expected_rows, metadata = expected_package_rows(candidate)
    for key in (
        "train_hr_rows", "test_hr_rows", "overlap_documents_removed",
        "overlap_rows_removed", "retained_train_rows", "output_rows",
    ):
        if metadata[key] != EXPECTED_PACKAGE[key]:
            raise AuditError(
                f"package count mismatch for {key}: "
                f"{metadata[key]} != {EXPECTED_PACKAGE[key]}"
            )

    if not output_path.is_file():
        raise AuditError(f"missing promoted output: {output_path}")
    with output_path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != OUTPUT_COLUMNS:
            raise AuditError(
                f"output schema mismatch: {reader.fieldnames} != {OUTPUT_COLUMNS}"
            )
        observed_rows = list(reader)
    fixture = os.environ.get("TEXT_PACKAGE_NEGATIVE_FIXTURE")
    if fixture == "split_drift":
        observed_rows[0]["derived_split"] = (
            "provjera" if observed_rows[0]["derived_split"] == "ucenje" else "ucenje"
        )
    if fixture == "fabricated_label_path":
        first_test = next(
            row for row in observed_rows if row["source_role"] == "test_file"
        )
        first_test["annotator2_raw"] = "Positive"
    if fixture == "output_tamper":
        observed_rows[0]["sentence_text"] += " namjerna-izmjena"

    if len({row["record_id"] for row in observed_rows}) != len(observed_rows):
        raise AuditError("record_id is not unique")
    if any(row["country_source"] != "HR" for row in observed_rows):
        raise AuditError("output contains a non-HR source row")
    if {row["recorded_label"] for row in observed_rows} != {
        "Negative", "Neutral", "Positive"
    }:
        raise AuditError("unexpected recorded-label domain")

    for row in observed_rows:
        document_id = row["source_document_id"]
        if row["source_role"] == "train_file":
            if row["derived_split"] != grouped_split(document_id):
                raise AuditError(f"split hash mismatch for {row['record_id']}")
            if row["label_path"] != "dva_kodera_i_uskladjenje":
                raise AuditError(f"wrong training label path for {row['record_id']}")
            if MISSING_FROM_SOURCE in {
                row["source_split"], row["annotator2_raw"], row["reconciliation_raw"]
            }:
                raise AuditError(f"training source value erased for {row['record_id']}")
        elif row["source_role"] == "test_file":
            if row["derived_split"] != "ispitivanje":
                raise AuditError(f"test row left final test split: {row['record_id']}")
            if row["label_path"] != "jedan_uvjezbani_koder":
                raise AuditError(f"wrong test label path for {row['record_id']}")
            if {
                row["source_split"], row["annotator2_raw"], row["reconciliation_raw"]
            } != {MISSING_FROM_SOURCE}:
                raise AuditError(f"test label path was fabricated for {row['record_id']}")
        else:
            raise AuditError(f"unexpected source role: {row['source_role']}")

    split_rows = Counter(row["derived_split"] for row in observed_rows)
    split_documents = {
        split: len({
            row["source_document_id"]
            for row in observed_rows
            if row["derived_split"] == split
        })
        for split in EXPECTED_PACKAGE["split_rows"]
    }
    split_labels = {
        split: dict(Counter(
            row["recorded_label"]
            for row in observed_rows
            if row["derived_split"] == split
        ))
        for split in EXPECTED_PACKAGE["split_rows"]
    }
    if dict(split_rows) != EXPECTED_PACKAGE["split_rows"]:
        raise AuditError(
            f"derived split row counts differ: {dict(split_rows)} != "
            f"{EXPECTED_PACKAGE['split_rows']}"
        )
    if split_documents != EXPECTED_PACKAGE["split_documents"]:
        raise AuditError(
            f"derived split document counts differ: {split_documents} != "
            f"{EXPECTED_PACKAGE['split_documents']}"
        )
    if split_labels != EXPECTED_PACKAGE["split_labels"]:
        raise AuditError(
            f"derived split label counts differ: {split_labels} != "
            f"{EXPECTED_PACKAGE['split_labels']}"
        )

    documents_by_split = {
        split: {
            row["source_document_id"]
            for row in observed_rows
            if row["derived_split"] == split
        }
        for split in EXPECTED_PACKAGE["split_rows"]
    }
    if documents_by_split["ucenje"] & documents_by_split["provjera"]:
        raise AuditError("document crosses training and validation splits")
    if (
        (documents_by_split["ucenje"] | documents_by_split["provjera"])
        & documents_by_split["ispitivanje"]
    ):
        raise AuditError("source document crosses the final test boundary")

    expected_bytes = serialized_rows(expected_rows)
    observed_bytes = output_path.read_bytes()
    observed_rows_bytes = serialized_rows(observed_rows)
    if observed_bytes != expected_bytes or observed_rows_bytes != expected_bytes:
        raise AuditError("promoted output is not byte-for-byte reproducible")
    output_md5 = hashlib.md5(observed_bytes, usedforsecurity=False).hexdigest()
    output_sha256 = hashlib.sha256(observed_bytes).hexdigest()
    if output_md5 != EXPECTED_OUTPUT_MD5:
        raise AuditError(
            f"output MD5 differs: {output_md5} != {EXPECTED_OUTPUT_MD5}"
        )
    if output_sha256 != EXPECTED_OUTPUT_SHA256:
        raise AuditError(
            f"output SHA-256 differs: {output_sha256} != {EXPECTED_OUTPUT_SHA256}"
        )
    metadata["split_rows"] = dict(split_rows)
    metadata["split_documents"] = split_documents
    metadata["split_labels"] = split_labels
    return metadata, output_md5, output_sha256


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, default=DEFAULT_CANDIDATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--expect-blocker", action="store_true")
    parser.add_argument("--research-parlamint-archive", type=Path)
    parser.add_argument("--research-text-root", type=Path)
    parser.add_argument("--research-parlamint-md5")
    args = parser.parse_args()
    research_values = (
        args.research_parlamint_archive,
        args.research_text_root,
        args.research_parlamint_md5,
    )
    if any(research_values) and not all(research_values):
        parser.error(
            "--research-parlamint-archive, --research-text-root and "
            "--research-parlamint-md5 must be supplied together"
        )
    legacy_link_audit = args.expect_blocker or any(research_values)
    if not legacy_link_audit:
        try:
            metadata, output_md5, output_sha256 = validate_package(
                args.candidate.resolve(), args.output.resolve()
            )
        except (AuditError, OSError, UnicodeError, json.JSONDecodeError) as error:
            print(f"TEXT_PACKAGE_FAIL {error}", file=sys.stderr)
            return 1
        print(
            "TEXT_PACKAGE_OK"
            f" rows={metadata['output_rows']}"
            f" train_hr={metadata['train_hr_rows']}"
            f" test_hr={metadata['test_hr_rows']}"
            f" removed_documents={metadata['overlap_documents_removed']}"
            f" removed_rows={metadata['overlap_rows_removed']}"
            f" retained_train={metadata['retained_train_rows']}"
            f" ucenje={metadata['split_rows']['ucenje']}"
            f" provjera={metadata['split_rows']['provjera']}"
            f" ispitivanje={metadata['split_rows']['ispitivanje']}"
            f" output_md5={output_md5} output_sha256={output_sha256}"
        )
        print(
            "SOURCE_SHA256 "
            + " ".join(
                f"{name}={value}"
                for name, value in sorted(metadata["source_hashes"].items())
            )
        )
        return 0

    try:
        counts, failures, source_hashes = audit(
            args.candidate.resolve(),
            args.research_parlamint_archive.resolve()
            if args.research_parlamint_archive else None,
            args.research_text_root.resolve() if args.research_text_root else None,
            args.research_parlamint_md5,
        )
    except (AuditError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"TEXT_PACKAGE_FAIL {error}", file=sys.stderr)
        return 1

    blocker = {key: counts.get(key, 0) for key in EXPECTED_BLOCKER}
    signature_ok = blocker == EXPECTED_BLOCKER
    print(
        "TEXT_LINK_AUDIT "
        + " ".join(f"{key}={counts.get(key, 0)}" for key in [
            "train_rows", "train_linked", "train_no_link", "train_ambiguous",
            "test_rows", "test_linked", "test_no_link", "test_ambiguous",
            "source_document_overlap", "resolved_speech_overlap",
        ])
    )
    print("SOURCE_SHA256 " + " ".join(f"{name}={value}" for name, value in sorted(source_hashes.items())))
    for failure in [row for row in failures if row["source_role"] == "test"][:10]:
        print("TEST_BLOCKER " + " ".join(f"{key}={value}" for key, value in failure.items()))

    if not signature_ok:
        print(
            f"TEXT_BLOCKER_SIGNATURE_MISMATCH observed={blocker} "
            f"expected={EXPECTED_BLOCKER}",
            file=sys.stderr,
        )
        return 1
    print("TEXT_PACKAGE_BLOCKER_CONFIRMED selected_test_rows_are_not_uniquely_linkable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
