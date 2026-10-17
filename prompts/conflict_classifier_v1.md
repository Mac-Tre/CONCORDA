# Conflict Classifier v1

Return JSON only. Do not include markdown, private coaching, report text, or memory content beyond the requested fields.

## Required fields
- `primary_conflict_type`
- `secondary_conflict_types`
- `escalation_level`
- `safety_flags`
- `repair_coaching_allowed`
- `recommended_module_ids`
- `memory_relevance`
- `brief_reasoning`

## Conflict types
- `trust_disclosure_conflict`
- `pursuer_defender_loop`
- `accountability_impasse`
- `repair_after_betrayal_or_perceived_betrayal`
- `power_agency_conflict`
- `future_versus_past_conflict`
- `definition_conflict`
- `attention_availability_conflict`
- `money_labor_ambition_conflict`
- `household_logistics_conflict`
- `parenting_family_system_conflict`
- `boundary_third_party_conflict`
- `meta_communication_conflict`
- `chronic_resentment_scorekeeping`
- `safety_coercion_crisis`
- `transparency_versus_amnesty`
- `disclosure_versus_confession`
- `mutual_disclosure_parity`
- `trauma_reactivation`
- `decision_relevant_facts`
- `answer_sufficiency_dispute`

## Classification rules
Use observable behavior only. Treat allegations as claims within the conversation, not verified facts. If safety flags are present, set `repair_coaching_allowed` to `false` and recommend safety routing.
