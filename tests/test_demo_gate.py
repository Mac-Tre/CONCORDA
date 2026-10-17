import unittest

from tools.demo_gate import CHECKS, validate, validate_register


def candidate(state="PILOT_CANDIDATE"):
    return {
        "state": state,
        "data_class": "synthetic",
        "checks": {item: True for item in CHECKS},
        "check_evidence_refs": {item: "synthetic-review/" + item for item in CHECKS},
        "owner_acceptance_ref": "decision-log/approval",
        "independent_safety_review_ref": "reviews/safety",
    }


class DemoGateTest(unittest.TestCase):
    def test_proof_only_checks_structure(self):
        self.assertEqual(validate(candidate()), [])

    def test_missing_safety_blocks_pilot(self):
        obj = candidate()
        obj["checks"]["safety_routing"] = False
        self.assertTrue(any("safety_routing" in error for error in validate(obj)))

    def test_missing_review_blocks_pilot(self):
        obj = candidate()
        obj.pop("independent_safety_review_ref")
        self.assertTrue(any("safety evaluation" in error for error in validate(obj)))

    def test_fixture_demo_disallows_real_data(self):
        self.assertTrue(validate({"state": "FIXTURE_DEMO", "data_class": "real"}))

    def test_release_needs_deployment_authorization(self):
        self.assertTrue(any("Deployment" in x for x in validate(candidate("RELEASED"))))

    def test_register_unverified_claim_without_proof(self):
        obj = {"schema_version": 1, "project": "concorda", "entries": [{
            "id": "X", "decision": "test", "approval_status": "APPROVED",
            "implementation_status": "VERIFIED", "decision_ref": "test",
            "verification_refs": [],
        }]}
        self.assertTrue(any("verification" in x for x in validate_register(obj)))


if __name__ == "__main__":
    unittest.main()
