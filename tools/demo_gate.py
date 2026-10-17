"""Review-manifest integrity check for Concorda; NOT a product-safety assessment."""
import json
import sys
from pathlib import Path

CHECKS = ("privacy", "consent", "safety_routing", "evidence_provenance", "html_escaping", "misuse_review")
STATES = {"FOUNDATION", "FIXTURE_DEMO", "PILOT_CANDIDATE", "RELEASED"}


def validate(record):
    if not isinstance(record, dict):
        return ["Manifest must be a JSON object."]
    errors = []
    state = record.get("state")
    if state not in STATES:
        errors.append("Unknown delivery state.")
        return errors
    if state in {"FIXTURE_DEMO", "PILOT_CANDIDATE", "RELEASED"} and record.get("data_class") != "synthetic":
        if state == "FIXTURE_DEMO":
            errors.append("Fixture demos require synthetic-only data.")
    if state in {"PILOT_CANDIDATE", "RELEASED"}:
        checks = record.get("checks", {})
        refs = record.get("check_evidence_refs", {})
        for check in CHECKS:
            if not isinstance(checks, dict) or checks.get(check) is not True:
                errors.append("Missing passing check: " + check)
            if not isinstance(refs, dict) or not isinstance(refs.get(check), str) or not refs[check].strip():
                errors.append("Missing independent evidence: " + check)
        if not record.get("owner_acceptance_ref"):
            errors.append("Product-owner approval evidence required.")
        if not record.get("independent_safety_review_ref"):
            errors.append("Independent safety evaluation reference required.")
    if state == "RELEASED" and not record.get("deployment_approval_ref"):
        errors.append("Deployment approval reference required.")
    return errors


def validate_register(data):
    if not isinstance(data, dict) or data.get("schema_version") != 1 or data.get("project") != "concorda":
        return ["Invalid decision register metadata."]
    errors = []
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["Entries must be a list."]
    ids = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"Entry {index} invalid.")
            continue
        id_ = entry.get("id")
        if not isinstance(id_, str) or not id_ or id_ in ids:
            errors.append(f"Entry {index} invalid or duplicate id.")
        ids.add(id_)
        if entry.get("approval_status") not in {"PROPOSED", "APPROVED"}:
            errors.append(f"Entry {index} has invalid approval status.")
        if entry.get("implementation_status") not in {"UNVERIFIED", "IN_PROGRESS", "IMPLEMENTED", "VERIFIED"}:
            errors.append(f"Entry {index} has invalid implementation status.")
        if not entry.get("decision") or not entry.get("decision_ref"):
            errors.append(f"Entry {index} missing decision or reference.")
        if entry.get("implementation_status") == "VERIFIED" and not entry.get("verification_refs"):
            errors.append(f"Entry {index} has no verification evidence.")
    return errors


def main(argv):
    if len(argv) != 3 or argv[1] not in {"--manifest", "--register"}:
        print("usage: python -m tools.demo_gate (--manifest | --register) file.json", file=sys.stderr)
        return 2
    try:
        payload = json.loads(Path(argv[2]).read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        print("Unable to read JSON:", exc, file=sys.stderr)
        return 2
    errors = validate(payload) if argv[1] == "--manifest" else validate_register(payload)
    for error in errors:
        print("FAIL: " + error)
    if errors:
        return 1
    print("PASS: manifest metadata only; no safety or clinical claims established.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
