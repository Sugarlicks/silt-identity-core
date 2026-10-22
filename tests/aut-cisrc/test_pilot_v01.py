#!/usr/bin/env python3
"""SILT Core v0.1 AUT profile: reproducible synthetic pilot regression tests.

Run from any working directory: python -m unittest discover -s tests/aut-cisrc -v
No external Python dependencies. This is NOT formal AUT institutional approval.
"""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / "examples/aut-cisrc-research-delegation"
VALIDATOR = ROOT / "reference/validators/aut-cisrc-delegation/validate.py"
spec = importlib.util.spec_from_file_location("aut_cisrc_validator_v01", VALIDATOR)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def fixture(path):
    return json.loads((FIX / path).read_text(encoding="utf-8"))


class AUTPilotV01Tests(unittest.TestCase):
    def evaluate(self, delegation="delegations/valid-delegation.json",
                 request="requests/valid-request.json",
                 revocations="revocations/no-revocations.json",
                 authority_chain=None, strict=False):
        chain = fixture("authority-chain.json") if authority_chain is None else authority_chain
        return validator.validate(fixture(delegation), fixture(request),
                                  fixture(revocations), chain, strict=strict)

    def assert_outcome(self, expected_result, expected_reason, **kwargs):
        result = self.evaluate(**kwargs)
        self.assertEqual((result["result"], result["reasonCode"]),
                         (expected_result, expected_reason), result)

    def test_01_valid_delegation(self):
        self.assert_outcome("ALLOW", "ALLOW")

    def test_02_expired(self):
        self.assert_outcome("DENY", "DELEGATION_EXPIRED",
                            delegation="delegations/expired-delegation.json")

    def test_03_wrong_delegate(self):
        self.assert_outcome("DENY", "ACTOR_NOT_DELEGATE",
                            request="requests/wrong-delegate-request.json")

    def test_04_wrong_action(self):
        self.assert_outcome("DENY", "ACTION_NOT_PERMITTED",
                            request="requests/action-not-permitted-request.json")

    def test_05_revoked(self):
        self.assert_outcome("DENY", "DELEGATION_REVOKED",
                            revocations="revocations/revoked-delegation.json")

    def test_06_wrong_resource(self):
        self.assert_outcome("DENY", "RESOURCE_OUT_OF_SCOPE",
                            request="requests/resource-mismatch-request.json")

    def test_07_wrong_purpose(self):
        self.assert_outcome("DENY", "PURPOSE_OUT_OF_SCOPE",
                            request="requests/purpose-mismatch-request.json")

    def test_08_missing_chain(self):
        self.assert_outcome("DENY", "AUTHORITY_CHAIN_MISSING", authority_chain={})

    def test_09_unknown_issuer_node(self):
        chain = fixture("authority-chain.json")
        chain["authorityNodes"] = [n for n in chain["authorityNodes"]
                                   if n["authorityNodeId"] != "node-006"]
        self.assert_outcome("DENY", "ISSUER_NOT_AUTHORISED", authority_chain=chain)

    def test_10_invalid_revoker(self):
        event = fixture("revocations/revoked-delegation.json")["revocations"][0]
        event["revokedBy"] = {"actorId": "unrecognised", "authorityNodeId": "not-a-node", "role": "ExternalActor"}
        event["revocationAuthorityBasis"] = {
            "basisType": "committee_or_subunit", "authorityNodeId": "not-a-node", "description": "Synthetic invalid revoker"}
        result = validator.validate(fixture("delegations/valid-delegation.json"),
                                    fixture("requests/valid-request.json"),
                                    {"revocations": [event]}, fixture("authority-chain.json"))
        self.assertEqual((result["result"], result["reasonCode"]),
                         ("DENY", "REVOCATION_AUTHORITY_INVALID"), result)

    def test_11_higher_order_revocation(self):
        event = fixture("revocations/revoked-delegation.json")["revocations"][0]
        event["revokedBy"] = {"actorId": "actor-university-001", "authorityNodeId": "node-005", "role": "School"}
        event["revocationAuthorityBasis"] = {
            "basisType": "higher_order_authority", "authorityNodeId": "node-005", "description": "Synthetic higher-order revocation"}
        result = validator.validate(fixture("delegations/valid-delegation.json"),
                                    fixture("requests/valid-request.json"),
                                    {"revocations": [event]}, fixture("authority-chain.json"))
        self.assertEqual((result["result"], result["reasonCode"]),
                         ("DENY", "DELEGATION_REVOKED"), result)

    def test_13_request_delegation_mismatch(self):
        delegation = fixture("delegations/valid-delegation.json")
        request = fixture("requests/valid-request.json")
        request["delegationId"] = "other-delegation"
        result = validator.validate(delegation, request,
                                    fixture("revocations/no-revocations.json"),
                                    fixture("authority-chain.json"))
        self.assertEqual(result["reasonCode"], "SCHEMA_INVALID")

    def test_14_invalid_request_timestamp(self):
        request = fixture("requests/valid-request.json")
        request["timestamp"] = "not-a-date"
        result = validator.validate(fixture("delegations/valid-delegation.json"), request,
                                    fixture("revocations/no-revocations.json"),
                                    fixture("authority-chain.json"))
        self.assertEqual(result["reasonCode"], "SCHEMA_INVALID")

    def test_15_missing_required_request_action(self):
        request = fixture("requests/valid-request.json")
        del request["action"]
        result = validator.validate(fixture("delegations/valid-delegation.json"), request,
                                    fixture("revocations/no-revocations.json"),
                                    fixture("authority-chain.json"))
        self.assertEqual(result["reasonCode"], "SCHEMA_INVALID")

    def test_16_invalid_revocation_log_shape(self):
        result = validator.validate(fixture("delegations/valid-delegation.json"),
                                    fixture("requests/valid-request.json"),
                                    {"revocations": "not an array"}, fixture("authority-chain.json"))
        self.assertEqual(result["reasonCode"], "SCHEMA_INVALID")

    def test_17_exact_expiry_boundary(self):
        delegation = fixture("delegations/valid-delegation.json")
        request = fixture("requests/valid-request.json")
        request["timestamp"] = delegation["expiresAt"]
        result = validator.validate(delegation, request,
                                    fixture("revocations/no-revocations.json"),
                                    fixture("authority-chain.json"))
        self.assertEqual(result["reasonCode"], "ALLOW")

    def test_18_one_second_after_expiry(self):
        delegation = fixture("delegations/valid-delegation.json")
        request = fixture("requests/valid-request.json")
        request["timestamp"] = "2026-09-01T00:00:00Z"
        result = validator.validate(delegation, request,
                                    fixture("revocations/no-revocations.json"),
                                    fixture("authority-chain.json"))
        self.assertEqual(result["reasonCode"], "DELEGATION_EXPIRED")

    def test_19_invalid_fixture_schema(self):
        delegation = fixture("delegations/valid-delegation.json")
        delegation["permittedActions"] = "dataset.submit"
        self.assertTrue(validator.schema_errors(delegation, "delegation.schema.json"))

    def test_20_result_matches_profile_schema(self):
        result = self.evaluate()
        self.assertEqual(validator.schema_errors(result, "validation-result.schema.json"), [])

    def test_12_strict_missing_evidence(self):
        delegation = fixture("delegations/valid-delegation.json")
        delegation.pop("evidenceDocuments", None)
        result = validator.validate(delegation, fixture("requests/valid-request.json"),
                                    fixture("revocations/no-revocations.json"),
                                    fixture("authority-chain.json"), strict=True)
        self.assertEqual((result["result"], result["reasonCode"]),
                         ("DENY", "EVIDENCE_CHAIN_MISSING"), result)


if __name__ == "__main__":
    unittest.main()
