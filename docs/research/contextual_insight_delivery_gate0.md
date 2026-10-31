# Research note — Contextual insight delivery for Rose Mirror™ (draft, no approval)

**Status:** Research/architecture candidate only, synthetic-only. **Tracking:** #10. **Date:** 2026-10-31. **Authority:** None to capture audio, process personal data, deploy, merge, or enable notifications.

## 1. Competitive evidence ledger

| Claim | Evidence | Confidence / qualification |
|---|---|---|
| Co–Star builds personalized readings from birth time/place and astronomical data interpreted with human insight and AI | https://www.costarastrology.com/about ; https://www.costarastrology.com/faq | Vendor-described product behavior; no access to proprietary code. |
| Co–Star offers daily push notifications and friend compatibility | https://apps.apple.com/us/app/co-star-personalized-astrology/id1264782561 | Published product listing. |
| Co–Star's privacy policy describes account-provided information, in-app interactions, device metadata, and derived inferences | https://www.costarastrology.com/privacy (updated Dec 11, 2025) | Vendor disclosure; not proof of any undisclosed collection. |
| Co–Star covertly or continuously listens via microphone | No technical evidence established | **Unverified; do not claim.** Perceived accuracy does not establish microphone capture. |
| iPhone microphone access requires permission and has system-use indicators | https://support.apple.com/en-us/108331 ; https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/RequestingPermission/RequestingPermission.html | OS documentation; assess current API and App Store requirements independently. |

**Transferable product insight, not proprietary architecture:** a stable, user-supplied context model + timely contextual triggers + an interpretation layer + concise, relevant content + optional notifications. It does **not** require surveillance.

## 2. Concorda candidate architecture (not approved)

```text
participant-initiated artifact input (text/upload; optionally later explicit recording)
  -> explicit purpose/visibility consent and content-boundary checks
  -> ephemeral validation, redaction options and participant labeling
  -> safety router (threats, coercion, stalking, intimidation, etc.)
  -> observable-behavior classification with cited artifact spans
  -> private, bounded reflection + uncertainty qualifiers
  -> OPTIONAL proposal for private memory (consent-gated, not auto-saved)
  -> OPTIONAL user-controlled insight scheduler (opt-in, frequency/cap/quiet hours)
  -> generic lock-screen notification -> private in-app detail
```

Use existing `schemas/conversation_artifact`, `schemas/conflict_classification`, `schemas/rose_mirror_report`, and `schemas/memory_update` as compatibility targets, **not** as permission to add persistent memory. Keep private outputs separate from cross-participant shared agreements, and do not infer motives, diagnoses, abusive identities, or hidden events. Any safety-triggered case must avoid generating a couples repair plan. A notification should never expose a private accusation, diagnosis, inferred vulnerability, partner content, or safety status to a lock-screen observer. Entire opt-in experience must be dismissible or disabled.

## 3. Research alternatives to present at G1 input/capture gate

| Input mode | Utility | Complexity | Main risks | Rollback |
|---|---|---|---|---|
| A. User-submitted artifacts only | Useful contextual insight; matches current MVP | Low | Third-party privacy, provenance, biased excerpts | Stop ingest / erase artifact |
| B. User-controlled **in-session** recording, clearly indicated, with jurisdiction-aware consent flow | Better capture fidelity where lawful and welcomed | High | Third-party recording consent, security, coercion, retention | Stop recording, delete session, revoke access |
| C. Passive or background ambient capture | Could collect more context but is not needed for stated MVP | Very high | Surveillance, legal compliance, partner safety, app platform policies | Do **not** pursue without an entirely separate design and legal gate |

**Default until G1:** A, because it is already embedded in the foundation, but this note does not make a new capture-mode decision for the owner.

## 4. Independent test and review requirements

- No artifact or voice input accessed without explicit user action and appropriate notice/consent; third-party content is handled with extra scrutiny.
- No automatic persistence of raw artifacts or analysis; zero memory write without explicit approval.
- Synthetic fixture tests: no cross-participant data leakage, unsupported assertion rejection, safety router overrides repair, notification lock-screen redaction, revoke/erase semantics, opt-in/off enforcement, audit of each data access.
- Independent adversarial review: coercive partner/device-sharing use, protected location privacy, notifications revealing conflict, fabricated context, manipulative personalization and confirmation bias, side-channel metadata leaks.
- All user-facing claims distinguish direct quotes, observed patterns, tentative interpretations, and explicit unknowns.
- Privacy and safety verification before any live input, integration, microphone feature, storage, production AI service, merge, or launch.

## 5. Architecture decision gates

- **G1:** Input/capture modality and third-party recording/consent posture.
- **G2:** Retention, storage, local-vs-cloud inference, private-vs-shared memory boundaries.
- **G3:** Personalized insight schedule, push-notification content and opt-in UX.
- **G4:** Security/privacy/safety validation and launch.

At each consequential gate, ask the owner **one** interactive, single-select question, with two or three alternatives and balanced value/complexity/risks. Do not silently choose. Continue only with reversible documentation and synthetic fixtures until approved. No user data, deployment, merges or external communications.

## Non-goals

Reverse engineering proprietary Co–Star internals without evidence; astrology as causal prediction; covert microphone access; surreptitious text/app capture; monitoring a partner; auto-inferred personal facts; abuse-detection certification; therapy, surveillance or automated intervention.
