# Test Plan

This repository currently contains a foundation package only. Future implementation PRs should add deterministic tests for:

- Schema validation.
- No-leakage output.
- Safety routing.
- Classifier module selection.
- Answer-sufficiency detection.
- Constructive challenge presence.
- Memory recommendation consent requirement.
- Report JSON shape validation.

Recommended first check: validate all JSON files parse cleanly and then validate fixtures against their target JSON Schemas once a test runner is introduced.
