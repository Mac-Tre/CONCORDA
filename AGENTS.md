# Concorda Agent Instructions

## Product definition
Concorda is a private relationship conflict intelligence product. Its first MVP is Rose Mirror™, a participant-facing assessment that analyzes a difficult relationship exchange and returns private, firm, fair feedback for one participant.

Concorda is not a therapy platform, truth detector, infidelity judge, moral ranking engine, investigator, or fact finder. It analyzes observable communication behavior, reduces escalation, and converts conflict into structured repair tasks.

## Non-negotiable product rules
- **No-leakage privacy rule:** participant-specific coaching, inferred vulnerabilities, private report content, and private memory must never be shown to the other participant.
- **Safety-first routing:** if input indicates threats, coercion, intimidation, stalking, physical violence, sexual coercion, self-harm, fear-based compliance, isolation, or monitoring, route to safety-first guidance and do not produce a couples repair plan.
- **Observable-behavior-only analysis:** describe what participants said or did in the artifact. Do not infer diagnoses, motives as facts, moral rank, or hidden truth.
- **No diagnosis or fact-finding conclusions:** do not decide who is lying, cheating, abusive, manipulative, disordered, or morally superior. Allegations remain allegations unless the user-provided artifact clearly states an admitted fact, and even then the product should focus on communication behavior and repair boundaries.
- **Separate raw artifacts from derived analysis:** raw conversation artifacts must remain structurally separate from classifications, reports, scores, coaching, and memory recommendations.
- **Consent-gated memory:** memory updates are recommendations only until an explicit participant consent action approves them. Do not implement automatic memory storage.

## Future PR requirements
Every future PR must include:
- Clear scope.
- Explicit excluded scope.
- Tests, validation notes, or a documented reason tests are not applicable.
- Privacy impact notes.
- Safety impact notes.

## Architecture restrictions
Generated code may not introduce telemetry, analytics, remote logging, authentication, payment, database persistence, real memory storage, or persistent sensitive storage without an explicit reviewed architecture decision.
