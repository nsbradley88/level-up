#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
CONTRACT_VERSION = "level-up-conformance-v1"
VERDICTS = {"conformant", "non-conformant", "indeterminate"}
SHA256 = re.compile(r"[0-9a-f]{64}")


class ConformanceFormatError(Exception):
    def __init__(self, issues: list[dict[str, str]]) -> None:
        self.issues = issues
        super().__init__("; ".join(item["message"] for item in issues))

    def report(self) -> dict[str, Any]:
        return {
            "scope": "level-up-conformance-result-structure",
            "result": "INVALID",
            "errors": self.issues,
        }


def _issue(code: str, location: str, message: str) -> ConformanceFormatError:
    return ConformanceFormatError([{"code": code, "location": location, "message": message}])


def _exact_keys(value: Any, expected: set[str], location: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != expected:
        raise _issue("invalid_keys", location, f"{location} keys must be exactly {sorted(expected)}")
    return value


def _string_list(value: Any, location: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        raise _issue("invalid_string_list", location, f"{location} must be an array of nonempty strings")
    if value != sorted(set(value)):
        raise _issue("noncanonical_string_list", location, f"{location} must be sorted and contain no duplicates")
    return value


def validate_result(contract: Any, result: Any) -> dict[str, Any]:
    contract = _exact_keys(
        contract,
        {
            "schema_version",
            "contract_version",
            "packet_sha256",
            "adjudication_ids",
            "condition_ids",
            "candidate_ids",
            "required_not_checkable",
        },
        "contract",
    )
    result = _exact_keys(
        result,
        {"schema_version", "contract_version", "packet_sha256", "results"},
        "result",
    )
    if contract["schema_version"] != SCHEMA_VERSION or result["schema_version"] != SCHEMA_VERSION:
        raise _issue("unsupported_schema_version", "schema_version", f"schema_version must be {SCHEMA_VERSION}")
    if contract["contract_version"] != CONTRACT_VERSION or result["contract_version"] != CONTRACT_VERSION:
        raise _issue("unsupported_contract_version", "contract_version", f"contract_version must be {CONTRACT_VERSION}")
    packet_sha256 = contract["packet_sha256"]
    if not isinstance(packet_sha256, str) or SHA256.fullmatch(packet_sha256) is None:
        raise _issue("invalid_packet_sha256", "contract.packet_sha256", "packet_sha256 must be lowercase SHA-256")
    if result["packet_sha256"] != packet_sha256:
        raise _issue("packet_digest_mismatch", "result.packet_sha256", "result does not name the checked packet digest")

    adjudication_order = _string_list(contract["adjudication_ids"], "contract.adjudication_ids")
    adjudication_ids = set(adjudication_order)
    condition_ids = set(_string_list(contract["condition_ids"], "contract.condition_ids"))
    candidate_ids = set(_string_list(contract["candidate_ids"], "contract.candidate_ids"))
    required_not_checkable = set(
        _string_list(contract["required_not_checkable"], "contract.required_not_checkable")
    )
    rows = result["results"]
    if not isinstance(rows, list):
        raise _issue("invalid_results", "result.results", "results must be an array")

    seen: set[str] = set()
    actual_order: list[str] = []
    for index, row_value in enumerate(rows):
        location = f"result.results[{index}]"
        row = _exact_keys(
            row_value,
            {
                "adjudication_id",
                "verdict",
                "condition_ids",
                "candidate_ids",
                "missing_information",
                "not_checkable",
                "advisory",
                "rationale",
            },
            location,
        )
        adjudication_id = row["adjudication_id"]
        if adjudication_id not in adjudication_ids:
            raise _issue("unknown_adjudication_id", f"{location}.adjudication_id", "adjudication_id is not supplied")
        if adjudication_id in seen:
            raise _issue("duplicate_adjudication_id", f"{location}.adjudication_id", "adjudication_id is duplicated")
        seen.add(adjudication_id)
        actual_order.append(adjudication_id)
        verdict = row["verdict"]
        if verdict not in VERDICTS:
            raise _issue("invalid_verdict", f"{location}.verdict", f"verdict must be one of {sorted(VERDICTS)}")
        cited_conditions = set(_string_list(row["condition_ids"], f"{location}.condition_ids"))
        cited_candidates = set(_string_list(row["candidate_ids"], f"{location}.candidate_ids"))
        missing = _string_list(row["missing_information"], f"{location}.missing_information")
        not_checkable = set(_string_list(row["not_checkable"], f"{location}.not_checkable"))
        if not cited_conditions.issubset(condition_ids):
            raise _issue("unknown_condition_id", f"{location}.condition_ids", "condition IDs must be supplied in full")
        if not cited_candidates.issubset(candidate_ids):
            raise _issue("unknown_candidate_id", f"{location}.candidate_ids", "candidate IDs must be supplied in full")
        if not_checkable != required_not_checkable:
            raise _issue(
                "not_checkable_mismatch",
                f"{location}.not_checkable",
                "not_checkable must exactly enumerate the supplied required set",
            )
        if row["advisory"] is not True:
            raise _issue("advisory_boundary_missing", f"{location}.advisory", "advisory must be true")
        if not isinstance(row["rationale"], str) or not row["rationale"].strip():
            raise _issue("missing_rationale", f"{location}.rationale", "rationale must be a nonempty string")
        if verdict == "conformant" and (cited_conditions or cited_candidates or missing):
            raise _issue("inconsistent_conformant", location, "conformant cannot carry violations or missing information")
        if verdict == "non-conformant" and (not cited_conditions or missing):
            raise _issue(
                "inconsistent_non_conformant",
                location,
                "non-conformant requires a supplied condition and no missing-information entries",
            )
        if verdict == "indeterminate" and (cited_conditions or cited_candidates or not missing):
            raise _issue(
                "inconsistent_indeterminate",
                location,
                "indeterminate requires missing information and no violation IDs",
            )
    if actual_order != adjudication_order:
        raise _issue(
            "adjudication_coverage_mismatch",
            "result.results",
            "results must contain every adjudication exactly once in supplied order",
        )
    return {
        "scope": "level-up-conformance-result-structure",
        "result": "STRUCTURALLY_CONFORMANT",
        "adjudications": len(rows),
    }


def _load_json(path: Path) -> Any:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        value: dict[str, Any] = {}
        for key, item in pairs:
            if key in value:
                raise ValueError(f"duplicate JSON key: {key}")
            value[key] = item
        return value

    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicates,
            parse_constant=lambda value: (_ for _ in ()).throw(
                ValueError(f"invalid JSON constant: {value}")
            ),
        )
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise _issue("json_not_loadable", str(path), f"JSON could not be loaded: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 2:
        print("usage: check_conformance_result.py CONTRACT.json RESULT.json", file=sys.stderr)
        return 2
    try:
        report = validate_result(_load_json(Path(args[0])), _load_json(Path(args[1])))
    except ConformanceFormatError as exc:
        print(json.dumps(exc.report(), sort_keys=True), file=sys.stderr)
        return 1
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
