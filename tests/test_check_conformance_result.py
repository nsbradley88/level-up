from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from check_conformance_result import (  # noqa: E402
    ConformanceFormatError,
    _load_json,
    validate_result,
)

PACKET_SHA256 = "a" * 64
OPEN_IDS = sorted(
    ["i001-p5-claude-004"]
    + [f"i001-p5-sol-{index:03d}" for index in range(1, 13)]
)
NOT_CHECKABLE = sorted(
    [
        "candidate_immutability_without_digest",
        "cohort_freshness_and_independence",
        "evidence_truth",
        "finding_completeness",
        "model_slot_and_cohort_identity_truth",
        "review_adequacy",
        "synthesis_fidelity",
    ]
)


def contract() -> dict:
    return {
        "schema_version": 1,
        "contract_version": "level-up-conformance-v1",
        "packet_sha256": PACKET_SHA256,
        "adjudication_ids": ["case-a", "case-b", "case-c", "case-d"],
        "condition_ids": ["C1", "C2", "C3", "C4", "C5"],
        "candidate_ids": OPEN_IDS,
        "required_not_checkable": NOT_CHECKABLE,
    }


def result() -> dict:
    return {
        "schema_version": 1,
        "contract_version": "level-up-conformance-v1",
        "packet_sha256": PACKET_SHA256,
        "results": [
            {
                "adjudication_id": "case-a",
                "verdict": "non-conformant",
                "condition_ids": ["C2", "C4"],
                "candidate_ids": OPEN_IDS,
                "missing_information": [],
                "not_checkable": NOT_CHECKABLE,
                "advisory": True,
                "rationale": "Open material candidates and a mechanical-assurance claim violate the supplied conditions.",
            },
            {
                "adjudication_id": "case-b",
                "verdict": "conformant",
                "condition_ids": [],
                "candidate_ids": [],
                "missing_information": [],
                "not_checkable": NOT_CHECKABLE,
                "advisory": True,
                "rationale": "The bounded-convergence draft preserves the supplied record.",
            },
            {
                "adjudication_id": "case-c",
                "verdict": "indeterminate",
                "condition_ids": [],
                "candidate_ids": [],
                "missing_information": ["objective O2 is not supplied"],
                "not_checkable": NOT_CHECKABLE,
                "advisory": True,
                "rationale": "The requested objective is absent from the packet.",
            },
            {
                "adjudication_id": "case-d",
                "verdict": "non-conformant",
                "condition_ids": ["C3", "C5"],
                "candidate_ids": ["i001-p5-sol-001"],
                "missing_information": [],
                "not_checkable": NOT_CHECKABLE,
                "advisory": True,
                "rationale": "No supplied authority can change the frozen disposition or waive the constraint.",
            },
        ],
    }


def issue_code(value: dict) -> str:
    with unittest.TestCase().assertRaises(ConformanceFormatError) as caught:
        validate_result(contract(), value)
    return caught.exception.issues[0]["code"]


class ConformanceResultTests(unittest.TestCase):
    def test_replication_packet_is_structurally_conformant(self) -> None:
        report = validate_result(contract(), result())
        self.assertEqual(report["result"], "STRUCTURALLY_CONFORMANT")
        self.assertEqual(report["adjudications"], 4)

    def test_compact_candidate_range_is_rejected(self) -> None:
        value = result()
        value["results"][0]["candidate_ids"] = [
            "i001-p5-claude-004",
            "i001-p5-sol-001...i001-p5-sol-012",
        ]
        self.assertEqual(issue_code(value), "unknown_candidate_id")

    def test_short_candidate_suffix_is_rejected(self) -> None:
        value = result()
        value["results"][0]["candidate_ids"] = ["-002", "i001-p5-sol-001"]
        self.assertEqual(issue_code(value), "unknown_candidate_id")

    def test_unknown_condition_is_rejected(self) -> None:
        value = result()
        value["results"][0]["condition_ids"] = ["C2", "C9"]
        self.assertEqual(issue_code(value), "unknown_condition_id")

    def test_missing_not_checkable_property_is_rejected(self) -> None:
        value = result()
        value["results"][0]["not_checkable"] = NOT_CHECKABLE[:-1]
        self.assertEqual(issue_code(value), "not_checkable_mismatch")

    def test_conformant_cannot_carry_ids(self) -> None:
        value = result()
        value["results"][1]["condition_ids"] = ["C1"]
        self.assertEqual(issue_code(value), "inconsistent_conformant")

    def test_non_conformant_requires_a_condition(self) -> None:
        value = result()
        value["results"][0]["condition_ids"] = []
        self.assertEqual(issue_code(value), "inconsistent_non_conformant")

    def test_indeterminate_requires_only_missing_information(self) -> None:
        value = result()
        value["results"][2]["candidate_ids"] = ["i001-p5-sol-001"]
        self.assertEqual(issue_code(value), "inconsistent_indeterminate")

    def test_unauthorized_risk_case_requires_existing_id(self) -> None:
        value = result()
        value["results"][3]["candidate_ids"] = ["new-risk-finding"]
        self.assertEqual(issue_code(value), "unknown_candidate_id")

    def test_result_order_must_match_contract(self) -> None:
        value = result()
        value["results"][0], value["results"][1] = value["results"][1], value["results"][0]
        self.assertEqual(issue_code(value), "adjudication_coverage_mismatch")

    def test_packet_digest_must_match(self) -> None:
        value = result()
        value["packet_sha256"] = "b" * 64
        self.assertEqual(issue_code(value), "packet_digest_mismatch")

    def test_arrays_must_be_sorted_and_unique(self) -> None:
        value = result()
        value["results"][0]["condition_ids"] = ["C4", "C2"]
        self.assertEqual(issue_code(value), "noncanonical_string_list")

    def test_advisory_boundary_is_required(self) -> None:
        value = result()
        value["results"][0]["advisory"] = False
        self.assertEqual(issue_code(value), "advisory_boundary_missing")

    def test_duplicate_json_keys_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "duplicate.json"
            path.write_text('{"schema_version":1,"schema_version":1}', encoding="utf-8")
            with self.assertRaises(ConformanceFormatError) as caught:
                _load_json(path)
            self.assertEqual(caught.exception.issues[0]["code"], "json_not_loadable")

    def test_validation_does_not_mutate_inputs(self) -> None:
        expected_contract = contract()
        expected_result = result()
        actual_contract = copy.deepcopy(expected_contract)
        actual_result = copy.deepcopy(expected_result)
        validate_result(actual_contract, actual_result)
        self.assertEqual(actual_contract, expected_contract)
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
