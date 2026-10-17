# Confidentiality Enforcement Rules

## Runtime Data Labeling
Every text span and note chunk must carry one of:
- `shared_session`
- `private_partner_a`
- `private_partner_b`
- `system_internal`

Generation in couple context may read only `shared_session` and `system_internal` policy snippets.

## Leakage Guard Pipeline
1. Build response draft.
2. Classify each sentence for source provenance.
3. Block response if any sentence depends on `private_partner_*` data.
4. Regenerate with allowed sources only.
5. Log decision artifact.

## Safe Perspective Recitation
When Corda explains a partner perspective in couple sessions, she must:
- cite only current shared-session utterances,
- avoid memory joins from private threads,
- use uncertainty language when inference confidence is low.

## Ephemeral Conversation Memory
- Raw conversational details should not persist across sessions.
- New sessions start with clean conversational memory state.
- Persistent storage is limited to structured coaching profile signals and consented analytics fields.

## Recommendation Adherence Tracking
Private adherence tracking may update analytics models but must be separated by visibility scope:
- `private_analytics` visible only to the owning partner and system,
- `shared_analytics` visible to both partners.

## Failure Mode Behavior
If provenance is uncertain, Corda must:
- withhold detail,
- provide generalized guidance,
- prompt user to voluntarily share context directly.

