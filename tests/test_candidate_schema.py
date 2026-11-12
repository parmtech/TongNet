"""Candidate schema checks only; never a funds or signature validator."""
import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "docs/ledger/transaction-envelope.v0.1.schema.json").read_text(encoding="utf-8"))
CANDIDATE = json.loads((ROOT / "docs/ledger/payout-transition-candidate.v0.1.json").read_text(encoding="utf-8"))


def envelope():
    return {
        "schema_version": "0.1.0", "chain_id": "test", "protocol_version": 1,
        "signer": "sender", "nonce": "0", "operation": "TRANSFER",
        "payload": {"recipient": "receiver", "amount_atomic": "1"},
        "authorizations": [{"role": "sender", "signer": "sender", "scheme_id": "test", "signature": "x"}],
        "validity": {"policy_id": "test", "not_before": "0", "expires_at": "1"},
    }


class CandidateSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Draft202012Validator.check_schema(SCHEMA)
        cls.validator = Draft202012Validator(SCHEMA)

    def test_valid_transfer_and_invalid_decimal_encodings(self):
        self.assertTrue(self.validator.is_valid(envelope()))
        for bad in ("1\n", "1\r", "1 ", "01", "+1", "-1", "١"):
            for field in ("amount", "nonce"):
                with self.subTest(bad=repr(bad), field=field):
                    item = copy.deepcopy(envelope())
                    if field == "amount":
                        item["payload"]["amount_atomic"] = bad
                    else:
                        item["nonce"] = bad
                    self.assertFalse(self.validator.is_valid(item))

    def test_wrong_operation_payload_and_extra_fields_rejected(self):
        item = envelope()
        item["operation"] = "LOCK"
        self.assertFalse(self.validator.is_valid(item))
        item = envelope()
        item["payload"]["unexpected"] = True
        self.assertFalse(self.validator.is_valid(item))

    def test_schema_alone_does_not_enforce_integer_range_or_signature(self):
        item = envelope()
        item["payload"]["amount_atomic"] = str(2**128)
        item["nonce"] = str(2**64)
        item["authorizations"][0]["signature"] = "not-base64!"
        self.assertTrue(self.validator.is_valid(item), "These remain parser/crypto checks, not schema guarantees")

    def test_candidate_boundaries_are_contiguous_and_unratified(self):
        policy = CANDIDATE["candidate_policy"]
        intervals = policy["intervals"]
        self.assertEqual(policy["receiver_duration_seconds"], 86400)
        self.assertEqual(policy["sender_duration_seconds"], 60 * 86400)
        self.assertEqual(intervals[0]["end_offset_seconds"], intervals[1]["start_offset_seconds"])
        self.assertEqual(intervals[1]["end_offset_seconds"], intervals[2]["start_offset_seconds"])
        self.assertFalse(intervals[0]["end_inclusive"])
        self.assertTrue(intervals[1]["start_inclusive"])
        self.assertFalse(intervals[2]["automatic_money_movement"])
        self.assertTrue(CANDIDATE["authority"]["owner_ratification_required_before_fund_movement"])


if __name__ == "__main__":
    unittest.main()
