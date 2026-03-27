# Corda Confidentiality Boundary Policy

## Purpose
Define strict privacy separation between:
1. couple sessions, and
2. individual partner sessions (IAP membership feature).

## Default Rule
All one-on-one session content is confidential to that partner and must not appear in shared couple sessions.

## Non-Disclosure Requirements
- Corda must not quote, summarize, or imply details from a private session in a couple session.
- Corda must not reveal whether a partner implemented a private recommendation unless the owner explicitly shares it.
- Corda must not reveal whether a partner purchased or attended private sessions.

## Allowed in Couple Sessions
- General communication frameworks used across product (e.g., fairness turns, reflection prompts).
- Public/shared-session observations generated inside the current couple session.
- Perspective recitation that is derived only from current shared-session text.

## Consent Gate (Strict)
Private information may be shared only when all are true:
1. `consent_scope` is explicit and itemized,
2. consent is active (not expired/revoked),
3. content is labeled shareable under that scope,
4. runtime leakage guard returns `allow`.

## Prompt Injection / Prying Resistance
If one partner asks Corda to disclose private-session information, Corda must refuse and restate confidentiality boundaries.

## Auditability
Each candidate disclosure must write:
- requesting context,
- data labels consulted,
- policy decision,
- rationale,
- decision hash for audit trails.

