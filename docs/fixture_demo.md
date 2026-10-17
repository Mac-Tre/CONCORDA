# Rose Mirror synthetic vertical-slice demo

This is a **deterministic preview renderer**, not a working live AI model or a production safety classifier.

## Run

```sh
npm install --ignore-scripts
npm test
npm run validate:fixtures
npm run demo:rose-mirror
```

Open `demo/rose-mirror-preview.html` locally to review the report.

## Scope and guardrails

- Only accepts the synthetic-redacted fixture currently shipped with the repository.
- Validates raw artifact, classification, and Rose Mirror report against the repository JSON Schemas.
- Rejects pre-approved memory and repair coaching paired with safety flags.
- Escapes HTML; writes local demo artifacts only. No credentials, logging, accounts, analytics, remote network requests, or persistent participant memory.
- No real transcript, production AI calls, automated safety-screen inference, or end-user upload is implemented.
- Future changes must add separate safety fixture cases and source-provenance controls before accepting actual participant input.

## Integration dependencies

The Rose Mirror foundation is now on main (merged PR #3). This executable fixture-only demo is built against main; development quality gates were integrated via PR #7. PR #2 (Corda/platform contracts) and PR #4 (Couples Couch) touch overlapping files and should be reconciled explicitly rather than merged automatically.
