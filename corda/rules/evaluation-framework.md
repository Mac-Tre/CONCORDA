# Corda Evaluation Framework

## 1) Decision Principle
Corda optimizes for:
1. emotional safety,
2. mutual understanding,
3. repair feasibility,
4. long-term alignment.

Corda explicitly avoids winner/loser conclusions.

## 2) Turn-Level Evaluation
For each event:
- classify intent (information, emotion, repair, attack, boundary, withdrawal)
- extract claims and infer evidence level
- score empathy/accountability/respect signals
- detect escalation/de-escalation markers
- run abuse risk flagging

## 3) Evidence Grounding Model
Each claim gets:
- `evidence_level`: none/anecdotal/partial/strong/verified
- `verifiability`: not/internally/externally verifiable
- `truth_grounding_score` in [0,1]

### Suggested mapping
- none = 0.10
- anecdotal = 0.30
- partial = 0.55
- strong = 0.75
- verified = 0.95

Session evidence score:
- weighted average across all major claims
- higher weight for central conflict claims

## 4) Relationship Dynamics Metrics
### Initiation patterns
- who initiates difficult topics
- initiation style distribution (gentle vs critical etc.)

### Communication load
- talk-time percent by partner
- interruption frequency
- response latency
- reflection-to-rebuttal ratio

### Repair capacity
- repair attempts made
- repair attempts accepted
- recovery slope after escalation

## 5) Abuse / Coercion Signal Framework
Potential flags include:
- threat language
- coercive control patterns
- humiliation/degradation
- intimidation
- physical harm references
- sexual coercion
- financial control
- isolation demands

### Risk levels
- none: no active flags
- low: isolated concerning language without pattern
- moderate: repeated concerning language or one severe event
- high: clear coercive pattern or direct threat
- critical: imminent harm indicators

If risk >= high:
- disable normal optimization coaching,
- provide safety-focused guidance,
- prompt local emergency/support resource workflow.

## 6) Recommendation Confidence Gating
`confidence` should be reduced when:
- evidence grounding is weak,
- contradictions are unresolved,
- one-sided participation dominates,
- safety risk is elevated.

Do not present high-confidence advice when data quality is poor.

## 7) Longitudinal Analytics (for product insight)
Track over time:
- conflict recovery trend
- communication consistency trend
- shared goal alignment trend
- respect and accountability stability
- safety flag trend

Use trend direction and volatility to adapt recommendation intensity and sequencing.


## 8) Couples Couch Coaching Gate
For Couples Couch sessions, Corda must complete safety screening before repair coaching. Screen for threats, coercive control, fear, stalking, intimidation, physical violence, self-harm, forced disclosure, and isolation.

If any safety marker indicates high or critical risk:
- do not encourage vulnerability, shared sessions, or deeper disclosure,
- do not create a couples repair plan,
- recommend safety-first outside support,
- keep memory recommendations minimal and consent-gated.

When safety mode is not triggered, classify one primary conflict type and up to three secondary types from the Couples Couch taxonomy, then narrow the next move to the repair sequence: regulate, name the issue, ask one question, give one direct answer, reflect what was heard, identify one repair action, and pause.

## 9) Private Coaching Evaluation
Private coaching should be evaluated for channel separation:
- Participant A output contains only Participant A's coaching.
- Participant B output contains only Participant B's coaching.
- Private memories are never copied into shared memory.
- Accusations are not stored as facts.
- Sensitive sexual, medical, legal, financial, or third-party allegations are not stored unless explicitly requested by the participant.

## 10) Reset and Disclosure Parity Evaluation
Activate the reset, repair, and mutual disclosure parity module when transcripts include phrases such as turning over a new leaf, moving forward, fresh start, transparency, confess, tell me the truth, secrets, not rehashing trauma, reciprocal misconduct claims, inability to trust, or needing to know what happened.

Evaluate whether the exchange reflects:
- a legitimate reset,
- avoidant amnesty,
- a confession trap,
- a mutual disclosure impasse,
- trauma reactivation,
- or a decision-relevant facts conflict.

Coaching must keep disclosure bounded to decision-relevant facts: whether conduct happened, general timeframe, whether it is ongoing, current contact, impact on money/health/parenting/housing/safety/legal exposure, violated agreements, future boundaries, and verifiable repair actions. Do not encourage graphic, comparative, punitive, or already-answered details unless new material evidence changes the issue.

When both partners have trust injuries, evaluate mutuality by asking privately whether each participant is requesting a category of transparency they have also provided, whether the request is for repair rather than leverage, and whether they are willing to answer the same category of question.
