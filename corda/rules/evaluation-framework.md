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

