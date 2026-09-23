Release Candidate 2 | Unified WE01-WE04 suite

Source -> Standing -> Presentation -> evaluation at the encounter

# 1. Purpose

This document consolidates the four worked encounters into one minimal semantic conformance suite. It tests semantic discipline rather than prescribing a carrier, protocol, legal outcome or implementation stack.

The suite is intentionally narrow. A passing implementation preserves SILT distinctions and refuses prohibited inferences; it does not prove substantive legal validity or cultural legitimacy.

# 2. Normative fixture rules

- Only SATISFIED, NOT_SATISFIED and INDETERMINATE are SILT evaluation outcomes.

- A condition outside evaluation is recorded in not_evaluated_conditions and MUST NOT be encoded as a fourth outcome.

- Each evaluation is identified with the Profile Expression under which it is produced.

- No aggregate encounter result is inferred without an expressed composition rule.

- Deliberate non-expression remains outside evaluation and MUST NOT be treated as absence or failure.

- Negative tests distinguish expected implementation conformance from whether the architecture successfully detects the prohibited behaviour.

# 3. Normalisation corrections

The unification step exposed fixture vocabulary drift but no new Core concept. Three corrections are carried into the v0.2 release candidate:

- Removed SATISFIED_PROVISIONALLY as an invalid fourth outcome; provisionality is represented through separate conditions or encounter state.

- Moved NONE / not required / not inferred from evaluation outcomes into not_evaluated_conditions.

- Separated expected implementation conformance from architecture test result for negative tests.

These corrections matter because otherwise test data begins to create semantics the Core itself does not contain.

# 4. Worked encounter index

| **ID** | **Domain**                         | **Base result** | **Adversarial variants** | **Principal pressure**                                                               |
|--------|------------------------------------|-----------------|--------------------------|--------------------------------------------------------------------------------------|
| WE01   | Electronic transferable instrument | PASS            | 7                        | Control / holder-related Standing / Obligation / constitutive instrument             |
| WE02   | Credential-carried institutional   | PASS            | 7                        | Credential integrity / Source / Standing / Authority / selective disclosure          |
| WE03   | Plural and collective              | PASS            | 8                        | Conflicting Profile Expressions / provenance / non-expression / collective Authority |
| WE04   | AI-agent recursive delegation      | PASS            | 8                        | Derived Authority / capability churn / revocation / Attribution / lineage            |

# 5. Common test record

Every case uses the same semantic record shape: Profile Expression identity; condition-level evaluation; conditions explicitly outside evaluation; prohibited inferences; expected implementation conformance; and architecture test result. This separates what SILT evaluates from what a test harness says about an implementation.

| **Field**                           | **Meaning**                                                                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expected_evaluations                | Condition-level SILT results. Outcome is exactly SATISFIED, NOT_SATISFIED or INDETERMINATE.                                                                             |
| permitted_outcomes                  | A test expectation may allow more than one Core outcome when the supplied facts intentionally leave the evidentiary branch open. This does not create a fourth outcome. |
| not_evaluated_conditions            | Conditions that are outside evaluation, not required by the encounter, or lack an expressed composition rule.                                                           |
| prohibited_inferences               | Semantic collapses or unstated rules a conformant implementation must not invent.                                                                                       |
| expected_implementation_conformance | Whether the illustrated implementation behaviour is conforming or intentionally non-conforming.                                                                         |
| architecture_test_result            | Whether SILT can represent or reject the case without a new universal Core object.                                                                                      |

# 6. Negative-test semantics

WE03 contains deliberately bad implementation behaviours. For example, silently ranking PE-R above PE-C is expected implementation non-conformance. The architecture test still passes because SILT can identify the move as prohibited without inventing a new precedence object. This distinction replaces the earlier ambiguous PASS\* notation.

# 7. Conformance result

WE01-WE04 now form a single machine-validatable suite covering 4 base fixtures and 30 adversarial variants. The suite validates against the accompanying JSON Schema. No case requires a new universal Core object.

The companion experimental SILT <-> LCP mapping provides the external carrier pressure test. It likewise does not expose a missing Core primitive. Together, the unified suite and the external mapping support semantic freeze at the architecture level.

# 8. Files

- SILT_v0.2_Minimal_Semantic_Conformance_Schema.json

- SILT_v0.2_Minimal_Semantic_Conformance_Suite.json
