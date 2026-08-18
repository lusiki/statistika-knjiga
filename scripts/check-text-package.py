#!/usr/bin/env python3
"""Fail-closed audit of the ratified ParlaMint-HR/ParlaSent linkage."""

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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, default=DEFAULT_CANDIDATE)
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

    if args.expect_blocker:
        if not signature_ok:
            print(f"TEXT_BLOCKER_SIGNATURE_MISMATCH observed={blocker} expected={EXPECTED_BLOCKER}", file=sys.stderr)
            return 1
        print("TEXT_PACKAGE_BLOCKER_CONFIRMED selected_test_rows_are_not_uniquely_linkable")
        return 0
    if counts.get("test_no_link", 0) or counts.get("test_ambiguous", 0):
        print(
            "TEXT_PACKAGE_FAIL selected Croatian test rows lack one unique ParlaMint-HR link",
            file=sys.stderr,
        )
        return 1
    print("TEXT_PACKAGE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
