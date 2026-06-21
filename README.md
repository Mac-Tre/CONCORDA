# Concorda

Concorda is a private relationship conflict intelligence product. It helps a participant review a difficult relationship exchange, understand the observable communication pattern, reduce escalation, and convert the conflict into bounded repair tasks.

Concorda is not therapy, a truth detector, an infidelity judge, a surveillance tool, or a moral ranking engine.

## Rose Mirror™

Rose Mirror™ is the first Concorda MVP. It is a participant-facing assessment that produces private, firm, fair feedback for one participant without leaking private coaching intended for another participant.

The MVP analyzes a submitted conversation artifact, screens for safety issues, classifies the conflict pattern, generates a structured Rose Mirror report, suggests a next best message, and recommends memory updates only after explicit consent.

## Repository contents

This foundation package contains:

- Product and UX documentation in `docs/`.
- Modular prompt templates in `prompts/`.
- JSON Schemas for raw artifacts, classifications, reports, and memory update proposals in `schemas/`.
- Synthetic redacted fixtures in `fixtures/`.
- A future testing strategy in `tests/`.
- Repository-level agent instructions in `AGENTS.md`.

## Intentionally out of scope

This repository foundation does not include production UI, database persistence, authentication, payments, analytics, telemetry, remote logging, real memory storage, or a production model integration.

## Development approach

Future development should preserve strict separation between raw conversation artifacts, derived analysis, participant-facing reports, and memory recommendations. Work should be implemented in small PRs with privacy and safety impact notes.

## Suggested first implementation PRs

1. PR1: Add prompt compiler and template loader.
2. PR2: Add conversation artifact validation.
3. PR3: Add conflict classification contract.
4. PR4: Add Rose Mirror report generator using fixture data.
5. PR5: Add minimal UI prototype from Figma design.
6. PR6: Add PDF export from structured report JSON.
