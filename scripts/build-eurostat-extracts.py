#!/usr/bin/env python3
"""Retrieve once and verify the ratified Eurostat 2025 EU-27 slice.

The only network mode is ``--fetch``. It performs exactly one bounded batch of
six requests against the official Eurostat dissemination API, without retries,
and refuses to run when any retrieval artifact already exists. Exact request
URLs, raw response bytes, retrieval time, response metadata and checksums are
retained under ``data/eurostat_drustvo``. No render invokes this script.

After retrieval, ``--write-derived`` materialises the one teaching CSV and its
machine-readable reconciliation entirely from the retained raw responses.
Without either flag the script is read-only: it reconstructs both derived files
in memory, checks every one of the 162 country-indicator keys against its raw
JSON-stat cell, and compares the result byte for byte with the repository.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIR = ROOT / "data" / "eurostat_drustvo"
RAW_DIR = PACKAGE_DIR / "raw"
QUERY_PATH = PACKAGE_DIR / "UPITI.json"
RETRIEVAL_PATH = PACKAGE_DIR / "PREUZIMANJE.json"
INCOMPLETE_PATH = PACKAGE_DIR / "PREUZIMANJE-NEPOTPUNO.json"
RECONCILIATION_PATH = PACKAGE_DIR / "USKLADJENJE.json"
OUTPUT_PATH = ROOT / "data" / "eurostat-drustvo-2025.csv"

API_ROOT = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"
REFERENCE_YEAR = "2025"
EU27 = (
    "AT", "BE", "BG", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "EL",
    "HR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT",
    "RO", "SK", "SI", "ES", "SE",
)
COUNTRY_HR = {
    "AT": "Austrija", "BE": "Belgija", "BG": "Bugarska", "CY": "Cipar",
    "CZ": "Češka", "DK": "Danska", "EE": "Estonija", "FI": "Finska",
    "FR": "Francuska", "DE": "Njemačka", "EL": "Grčka", "HR": "Hrvatska",
    "HU": "Mađarska", "IE": "Irska", "IT": "Italija", "LV": "Latvija",
    "LT": "Litva", "LU": "Luksemburg", "MT": "Malta", "NL": "Nizozemska",
    "PL": "Poljska", "PT": "Portugal", "RO": "Rumunjska", "SK": "Slovačka",
    "SI": "Slovenija", "ES": "Španjolska", "SE": "Švedska",
}

# Every selector below is a ratified concept translated into source codes. The
# retained responses are deliberately filtered only by year and geography: if a
# source code or dimension changes, the local derivation fails closed while the
# already-authorised raw response remains available for an offline diagnosis.
INDICATORS = (
    {
        "id": "stopa_zaposlenosti_20_64",
        "label_hr": "Stopa zaposlenosti stanovništva od 20 do 64 godine",
        "dataset": "lfsi_emp_a",
        "selectors": {
            "freq": "A", "indic_em": "EMP_LFS", "sex": "T",
            "age": "Y20-64", "unit": "PC_POP",
        },
    },
    {
        "id": "rizik_siromastva_ili_iskljucenosti",
        "label_hr": "Rizik od siromaštva ili socijalne isključenosti",
        "dataset": "ilc_peps01n",
        "selectors": {"freq": "A", "age": "TOTAL", "sex": "T", "unit": "PC"},
    },
    {
        "id": "tercijarno_obrazovanje_25_34",
        "label_hr": "Tercijarno obrazovanje stanovništva od 25 do 34 godine",
        "dataset": "sdg_04_20",
        "selectors": {
            "freq": "A", "sex": "T", "age": "Y25-34", "unit": "PC",
            "isced11": "ED5-8",
        },
    },
    {
        "id": "rano_napustanje_obrazovanja_18_24",
        "label_hr": "Rano napuštanje obrazovanja i osposobljavanja od 18 do 24 godine",
        "dataset": "edat_lfse_14",
        "selectors": {
            "freq": "A", "sex": "T", "wstatus": "POP", "age": "Y18-24",
            "unit": "PC",
        },
    },
    {
        "id": "uporaba_interneta_16_74",
        "label_hr": "Uporaba interneta u prethodna tri mjeseca od 16 do 74 godine",
        "dataset": "isoc_ci_ifp_iu",
        "selectors": {"freq": "A", "indic_is": "I_IU3", "unit": "PC_IND", "ind_type": "IND_TOTAL"},
    },
    {
        "id": "udio_stanovnistva_65_plus",
        "label_hr": "Udio stanovništva u dobi od 65 ili više godina",
        "dataset": "demo_pjanind",
        "selectors": {"freq": "A", "indic_de": "PC_Y65_MAX"},
    },
)


def digest(payload: bytes, algorithm: str) -> str:
    return hashlib.new(algorithm, payload).hexdigest()


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def request_url(dataset: str) -> str:
    params = [("lang", "en"), ("time", REFERENCE_YEAR)]
    params.extend(("geo", geo) for geo in EU27)
    return f"{API_ROOT}/{dataset}?{urllib.parse.urlencode(params)}"


def raw_relative(dataset: str) -> str:
    return f"data/eurostat_drustvo/raw/{dataset}-2025-eu27.json"


def query_plan() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "authority": "G-A3-EUROSTAT; author approval dated 2026-08-10",
        "operation": "one bounded six-request batch; official Eurostat API; no retries",
        "reference_year": int(REFERENCE_YEAR),
        "geographies": list(EU27),
        "request_count": len(INDICATORS),
        "requests": [
            {
                "ordinal": ordinal,
                "indicator": indicator["id"],
                "dataset": indicator["dataset"],
                "url": request_url(indicator["dataset"]),
                "raw_path": raw_relative(indicator["dataset"]),
            }
            for ordinal, indicator in enumerate(INDICATORS, start=1)
        ],
    }


def parse_json(payload: bytes, label: str) -> dict[str, Any]:
    try:
        parsed = json.loads(payload.decode("utf-8"), parse_float=Decimal)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label}: response is not valid UTF-8 JSON: {exc}") from exc
    if not isinstance(parsed, dict) or parsed.get("class") != "dataset":
        raise ValueError(f"{label}: response is not a JSON-stat dataset")
    return parsed


def fetch_once() -> int:
    protected = [QUERY_PATH, RETRIEVAL_PATH, INCOMPLETE_PATH]
    protected.extend(ROOT / raw_relative(i["dataset"]) for i in INDICATORS)
    existing = [path for path in protected if path.exists()]
    if existing:
        print("EUROSTAT_FETCH_REFUSED existing retrieval artifacts:")
        for path in existing:
            print(f"- {path.relative_to(ROOT)}")
        return 1

    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    plan = query_plan()
    QUERY_PATH.write_bytes(canonical_json(plan))
    started = datetime.now(timezone.utc)
    records: list[dict[str, Any]] = []

    try:
        for request_spec in plan["requests"]:
            url = request_spec["url"]
            parsed_url = urllib.parse.urlparse(url)
            if parsed_url.scheme != "https" or parsed_url.hostname != "ec.europa.eu":
                raise RuntimeError(f"non-official request target refused: {url}")
            request = urllib.request.Request(
                url,
                headers={
                    "Accept": "application/json",
                    "User-Agent": "Statistika-P3-EUROSTAT/1.0 (bounded archival retrieval)",
                },
                method="GET",
            )
            # One attempt per table. No retry loop is present or permitted.
            with urllib.request.urlopen(request, timeout=120) as response:
                final_url = response.geturl()
                final_host = urllib.parse.urlparse(final_url).hostname
                if final_host != "ec.europa.eu":
                    raise RuntimeError(f"redirect outside official host refused: {final_url}")
                payload = response.read()
                status = int(response.status)
                headers = response.headers
            if status != 200:
                raise RuntimeError(f"{request_spec['dataset']}: HTTP {status}")
            parsed = parse_json(payload, request_spec["dataset"])
            target = ROOT / request_spec["raw_path"]
            with target.open("xb") as handle:
                handle.write(payload)
            records.append({
                **request_spec,
                "final_url": final_url,
                "http_status": status,
                "content_type": headers.get("Content-Type"),
                "etag": headers.get("ETag"),
                "last_modified": headers.get("Last-Modified"),
                "response_bytes": len(payload),
                "md5": digest(payload, "md5"),
                "sha256": digest(payload, "sha256"),
                "jsonstat_label": parsed.get("label"),
                "jsonstat_updated": parsed.get("updated"),
            })
    except Exception as exc:
        failed = {
            "schema_version": 1,
            "batch_state": "incomplete_and_not_repeatable_without_new_authority",
            "started_at_utc": started.isoformat().replace("+00:00", "Z"),
            "failed_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "completed_requests": records,
            "error_type": type(exc).__name__,
            "error": str(exc),
        }
        INCOMPLETE_PATH.write_bytes(canonical_json(failed))
        print("EUROSTAT_FETCH_FAILED")
        print(f"- {type(exc).__name__}: {exc}")
        print("- no automatic retry was attempted")
        return 1

    finished = datetime.now(timezone.utc)
    retrieval = {
        "schema_version": 1,
        "batch_state": "complete",
        "authority": "conversation:G-A3-EUROSTAT-bounded-retrieval-approved-2026-08-10-Luka-Sikic",
        "started_at_utc": started.isoformat().replace("+00:00", "Z"),
        "completed_at_utc": finished.isoformat().replace("+00:00", "Z"),
        "retrieved_on": finished.date().isoformat(),
        "request_count": len(records),
        "automatic_retries": 0,
        "requests": records,
    }
    RETRIEVAL_PATH.write_bytes(canonical_json(retrieval))
    print(f"EUROSTAT_FETCH_OK requests={len(records)} date={finished.date().isoformat()} retries=0")
    return 0


def category_index(dimension: dict[str, Any], dimension_id: str) -> tuple[list[str], dict[str, int]]:
    category = dimension.get("category") or {}
    raw_index = category.get("index")
    if isinstance(raw_index, list):
        codes = [str(code) for code in raw_index]
        return codes, {code: position for position, code in enumerate(codes)}
    if isinstance(raw_index, dict):
        positions = {str(code): int(position) for code, position in raw_index.items()}
        codes = [code for code, _ in sorted(positions.items(), key=lambda item: item[1])]
        if sorted(positions.values()) != list(range(len(positions))):
            raise ValueError(f"{dimension_id}: category positions are not contiguous")
        return codes, positions
    raise ValueError(f"{dimension_id}: category.index is absent or malformed")


def flat_index(positions: list[int], sizes: list[int]) -> int:
    result = 0
    for position, size in zip(positions, sizes):
        if position < 0 or position >= size:
            raise ValueError("JSON-stat position is outside its dimension")
        result = result * size + position
    return result


def sparse_get(container: Any, index: int) -> Any:
    if isinstance(container, list):
        return container[index] if index < len(container) else None
    if isinstance(container, dict):
        return container.get(str(index))
    if container is None:
        return None
    raise ValueError("JSON-stat value/status container has an unsupported shape")


def scalar_text(value: Any) -> str:
    if isinstance(value, Decimal):
        return format(value, "f")
    if isinstance(value, bool):
        raise ValueError("boolean found where a numerical Eurostat value was expected")
    if isinstance(value, (int, float)):
        return str(value)
    raise ValueError(f"unsupported numerical value: {value!r}")


def build_from_raw() -> tuple[bytes, bytes, dict[str, Any]]:
    header = [
        "geo", "zemlja", "godina", "pokazatelj", "pokazatelj_hr",
        "eurostat_dataset", "vrijednost", "jedinica", "status_api",
        "obs_status", "conf_status", "vrijednost_dostupna",
    ]
    rows: list[list[str]] = [header]
    indicator_reports: list[dict[str, Any]] = []

    retrieval = json.loads(RETRIEVAL_PATH.read_text(encoding="utf-8"))
    if retrieval.get("batch_state") != "complete" or retrieval.get("request_count") != len(INDICATORS):
        raise ValueError("retained retrieval manifest does not describe the complete six-request batch")
    request_records = {record["dataset"]: record for record in retrieval.get("requests", [])}

    for indicator in INDICATORS:
        dataset = indicator["dataset"]
        raw_path = ROOT / raw_relative(dataset)
        payload = raw_path.read_bytes()
        record = request_records.get(dataset)
        if not record:
            raise ValueError(f"{dataset}: retrieval manifest has no request record")
        if digest(payload, "md5") != record.get("md5") or digest(payload, "sha256") != record.get("sha256"):
            raise ValueError(f"{dataset}: raw response checksum disagrees with retrieval manifest")
        source = parse_json(payload, dataset)
        if source.get("source") != "ESTAT":
            raise ValueError(f"{dataset}: actual response does not carry the Eurostat agency code ESTAT")
        extension = source.get("extension") or {}
        annotations = extension.get("annotation") or []
        source_institutions = {
            str(annotation.get("text"))
            for annotation in annotations
            if annotation.get("type") == "SOURCE_INSTITUTIONS"
        }
        if source_institutions != {"Eurostat"}:
            raise ValueError(
                f"{dataset}: SOURCE_INSTITUTIONS is not exactly Eurostat: "
                f"{sorted(source_institutions)!r}"
            )
        contrary_rights = [
            annotation for annotation in annotations
            if any(
                marker in " ".join(
                    str(annotation.get(field, "")) for field in ("type", "title", "text")
                ).upper()
                for marker in ("COPYRIGHT", "THIRD PARTY", "THIRD_PARTY", "LICENCE", "LICENSE")
            )
        ]
        if contrary_rights:
            raise ValueError(f"{dataset}: response carries a source-specific rights annotation")
        dimension_ids = [str(value) for value in source.get("id", [])]
        sizes = [int(value) for value in source.get("size", [])]
        if len(dimension_ids) != len(sizes) or len(dimension_ids) == 0:
            raise ValueError(f"{dataset}: malformed JSON-stat dimension shape")
        if "geo" not in dimension_ids or "time" not in dimension_ids:
            raise ValueError(f"{dataset}: response lacks geo or time")
        expected_dimensions = set(indicator["selectors"]) | {"geo", "time"}
        if set(dimension_ids) != expected_dimensions:
            raise ValueError(
                f"{dataset}: dimensions {dimension_ids!r} disagree with the bounded selector "
                f"{sorted(expected_dimensions)!r}"
            )

        dimensions = source.get("dimension") or {}
        code_lists: dict[str, list[str]] = {}
        positions: dict[str, dict[str, int]] = {}
        labels: dict[str, dict[str, str]] = {}
        for dimension_id in dimension_ids:
            dimension = dimensions.get(dimension_id)
            if not isinstance(dimension, dict):
                raise ValueError(f"{dataset}: missing dimension object {dimension_id}")
            codes, code_positions = category_index(dimension, dimension_id)
            if len(codes) != sizes[dimension_ids.index(dimension_id)]:
                raise ValueError(f"{dataset}: size disagrees for dimension {dimension_id}")
            code_lists[dimension_id] = codes
            positions[dimension_id] = code_positions
            category_labels = (dimension.get("category") or {}).get("label") or {}
            labels[dimension_id] = {str(code): str(label) for code, label in category_labels.items()}

        selected = {**indicator["selectors"], "time": REFERENCE_YEAR}
        for dimension_id, code in selected.items():
            if code not in positions[dimension_id]:
                raise ValueError(
                    f"{dataset}: required {dimension_id}={code!r} is absent; "
                    f"available={code_lists[dimension_id]!r}"
                )
        if set(code_lists["geo"]) != set(EU27) or len(code_lists["geo"]) != len(EU27):
            raise ValueError(
                f"{dataset}: response geography is not exactly the ratified EU-27; "
                f"received={code_lists['geo']!r}"
            )

        available = 0
        missing = 0
        status_counts: dict[str, int] = {}
        status_labels = ((extension.get("status") or {}).get("label") or {})
        source_indices: list[int] = []
        for geo in EU27:
            cell_codes = {**selected, "geo": geo}
            cell_positions = [positions[dimension_id][cell_codes[dimension_id]] for dimension_id in dimension_ids]
            index = flat_index(cell_positions, sizes)
            source_indices.append(index)
            raw_value = sparse_get(source.get("value"), index)
            raw_status = sparse_get(source.get("status"), index)
            status_api = "bez_objavljene_oznake" if raw_status in (None, "") else str(raw_status)
            if status_api == "bez_objavljene_oznake":
                status_description = "nema objavljene oznake"
                obs_status = status_api
                conf_status = status_api
            else:
                if status_api not in status_labels:
                    raise ValueError(f"{dataset}: status {status_api!r} has no source description")
                status_description = str(status_labels[status_api])
                if "confidential" in status_description.casefold():
                    obs_status = "bez_objavljene_oznake"
                    conf_status = status_api
                else:
                    obs_status = status_api
                    conf_status = "bez_objavljene_oznake"
            status_counts[status_api] = status_counts.get(status_api, 0) + 1
            if raw_value is None:
                value = ":"
                availability = "ne"
                missing += 1
            else:
                value = scalar_text(raw_value)
                availability = "da"
                available += 1
            rows.append([
                geo,
                COUNTRY_HR[geo],
                REFERENCE_YEAR,
                indicator["id"],
                indicator["label_hr"],
                dataset,
                value,
                indicator["selectors"].get("unit", "PC"),
                status_api,
                obs_status,
                conf_status,
                availability,
            ])

        indicator_reports.append({
            "indicator": indicator["id"],
            "dataset": dataset,
            "source_label": source.get("label"),
            "source_updated": source.get("updated"),
            "source": source.get("source"),
            "source_institutions": sorted(source_institutions),
            "datastructure_version": (extension.get("datastructure") or {}).get("version"),
            "contrary_rights_annotations": len(contrary_rights),
            "selected_dimensions": selected,
            "selected_dimension_labels": {
                dimension_id: labels[dimension_id].get(code)
                for dimension_id, code in selected.items()
            },
            "raw_path": raw_relative(dataset),
            "raw_md5": record["md5"],
            "raw_sha256": record["sha256"],
            "source_cell_indices_sha256": digest(
                ("\n".join(str(value) for value in source_indices) + "\n").encode("ascii"), "sha256"
            ),
            "rows": len(EU27),
            "available_values": available,
            "missing_values": missing,
            "status_counts": status_counts,
            "source_status_labels": {
                code: str(status_labels[code])
                for code in sorted(status_counts)
                if code != "bez_objavljene_oznake"
            },
            "comparison_tolerance": 0,
            "comparison_result": "passed",
        })

    if len(rows) != 1 + len(EU27) * len(INDICATORS):
        raise ValueError("derived table does not contain exactly 162 data rows")
    keys = [(row[0], row[2], row[3]) for row in rows[1:]]
    if len(keys) != len(set(keys)):
        raise ValueError("derived table repeats a geo+godina+pokazatelj key")

    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    for row in rows:
        if any(cell == "" for cell in row):
            raise ValueError("derived table contains an empty cell")
        if any(any(mark in cell for mark in (",", '"', "\r", "\n")) for cell in row):
            raise ValueError("derived table contains a separator, quote or line break")
        writer.writerow(row)
    csv_payload = buffer.getvalue().encode("utf-8")
    reconciliation = {
        "schema_version": 1,
        "result": "passed",
        "method": "every derived key rebuilt from its retained official JSON-stat cell without numerical tolerance",
        "analysis_file": "data/eurostat-drustvo-2025.csv",
        "analysis_md5": digest(csv_payload, "md5"),
        "analysis_sha256": digest(csv_payload, "sha256"),
        "reference_year": int(REFERENCE_YEAR),
        "countries_expected": len(EU27),
        "indicators_expected": len(INDICATORS),
        "keys_expected": len(EU27) * len(INDICATORS),
        "keys_observed": len(keys),
        "duplicate_keys": len(keys) - len(set(keys)),
        "available_values": sum(item["available_values"] for item in indicator_reports),
        "missing_values": sum(item["missing_values"] for item in indicator_reports),
        "comparison_tolerance": 0,
        "indicators": indicator_reports,
    }
    return csv_payload, canonical_json(reconciliation), reconciliation


def verify_or_write(write: bool) -> int:
    expected_plan = canonical_json(query_plan())
    if not QUERY_PATH.is_file() or QUERY_PATH.read_bytes() != expected_plan:
        print("EUROSTAT_EXTRACTS_FAILED")
        print("- retained query plan is absent or differs from the bounded six-query plan")
        return 1
    if not RETRIEVAL_PATH.is_file():
        print("EUROSTAT_EXTRACTS_FAILED")
        print("- complete retrieval manifest is absent")
        return 1
    try:
        csv_payload, reconciliation_payload, reconciliation = build_from_raw()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("EUROSTAT_EXTRACTS_FAILED")
        print(f"- {type(exc).__name__}: {exc}")
        return 1

    if write:
        OUTPUT_PATH.write_bytes(csv_payload)
        RECONCILIATION_PATH.write_bytes(reconciliation_payload)
    else:
        drift: list[str] = []
        if not OUTPUT_PATH.is_file() or OUTPUT_PATH.read_bytes() != csv_payload:
            drift.append("data/eurostat-drustvo-2025.csv does not reproduce byte for byte")
        if not RECONCILIATION_PATH.is_file() or RECONCILIATION_PATH.read_bytes() != reconciliation_payload:
            drift.append("data/eurostat_drustvo/USKLADJENJE.json does not reproduce byte for byte")
        if drift:
            print("EUROSTAT_EXTRACTS_FAILED")
            for message in drift:
                print(f"- {message}")
            return 1

    print(
        "EUROSTAT_EXTRACTS_OK "
        f"mode={'write-derived' if write else 'verify'} "
        f"keys={reconciliation['keys_observed']} "
        f"available={reconciliation['available_values']} "
        f"missing={reconciliation['missing_values']} tolerance=0"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--fetch", action="store_true", help="Run the one authorised official batch retrieval.")
    modes.add_argument("--write-derived", action="store_true", help="Write the derived CSV and reconciliation from retained raw bytes.")
    args = parser.parse_args()
    if args.fetch:
        return fetch_once()
    return verify_or_write(write=args.write_derived)


if __name__ == "__main__":
    sys.exit(main())
