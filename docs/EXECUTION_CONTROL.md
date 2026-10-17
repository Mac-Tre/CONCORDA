# Concorda / Rose Mirror development controls

Status: PROPOSED on a branch stacked on foundation PR #3. No production capability or medical/clinical validation is implied.
Repo of record: Mac-Tre/CONCORDA. Prose is a different product/repository.

## Approved direction / live scope
- The consumer-first Rose Mirror MVP is the current product focus, not a professional/clinician-facing product.
- Foundation PR #3 is merged into main (commit f81486b409c9dda37da6a74f6e2fe38ded4947a5); the foundation supplies AGENTS.md, schemas, PRD, UX and synthetic fixtures. Production and independent domain validation remain incomplete.
- PR #5 contains an experimental synthetic-only Rose Mirror report demo, stacked on PR #3. Tests and execution are not independently verified. No real-data intake, live AI inference, deployment, auth or payments are established.
- PR #4 Couples Couch is a distinct proposal and must not be silently mixed into the Rose Mirror path.
- Preserve privacy and consent boundaries. Do not claim a model can reliably identify abuse, make a clinical diagnosis, infer intent, or safely formulate exit strategies without explicitly reviewed safety evidence and product scope.

## Repo decision protocol
- Before asking product owner a question, read docs/DECISIONS.json, AGENTS.md, PRD, privacy policy, open PRs and actual tests. Reuse approved decisions.
- Do not convert internal approval gates into redundant questions for end users.
- Record consequential choices as APPROVED or PROPOSED, and record actual delivery separately as UNVERIFIED, IN_PROGRESS, IMPLEMENTED, or VERIFIED.
- A VERIFIED milestone requires independent test evidence (CI result, reproducible run, reviewed report) and a link.
- When an approval is unclear, treat as PROPOSED and prefer a reversible synthetic-data-only implementation.
- Develop in narrow branches; open draft PRs. Do not merge, deploy, add user-data collection or network paths without product-owner authorization.

## Gate sequence
G0 Foundation: PR #3 merged; keep unmerged PR #2's conflicting policy/schema changes isolated and reconcile only if needed for an approved slice. Verify AGENTS.md and privacy constraints on the intended base.
G1 Synthetic executable demonstration: prove the PR #5 tests run (schema validation, HTML escaping, consent and safety behavior, real-data rejection) against reproducible fixtures. A green test is demonstration proof only, not clinical safety validation.
G2 Product prototype: implement a usable consumer Rose Mirror journey, minimal on-device/browser-local UI, consent and clear uncertainty. No production real-user analysis before G1 and dedicated safety/privacy review.
G3 Controlled pilot: independent threat-model/security and misuse evaluation; usability and content review; documented retention, deletion, safeguards, escalation, and rollback controls. Explicit product-owner acceptance required.
G4 Release: approved deployment, verified operational controls, current policy disclosures and documented evidence. No implicit auto-release from passing CI.

## Hourly scheduled agent
- Prefer one non-destructive reversible approved change per run.
- If no approved slice or working environment is accessible, produce exact blocker once; never claim passive progress.
- Never put sensitive relationships, user recordings, client data, private chat transcripts, or personal identifiers into this public repository.
- Alert only for verified milestone, genuine product-owner gate, or urgent defect.
- Next immediate technical task is to run PR #5's Node tests in an execution-capable environment, repair failures without changing privacy posture, and record the result.
- Follow repository-specific safety policy rather than using Prose's legal-document rules.

## Automated safety proof is limited
The script tools/demo_gate.py checks review-manifest completeness. It does not evaluate actual model safety, crisis response quality, downstream harms or whether a real-world coercion scenario was recognized. Those require reviewed, representative evaluation before pilot.
