# WE04 - Recursive AI Delegation Encounter

**Authority containment, semantic lineage, revocation, and execution without semantic collapse**

**Status:** FC1 normalised semantic fixture. Companion conformance material; non-normative except where it reproduces requirements from the canonical semantic architecture.

**Suite discipline:** Semantic conformance, not implementation conformance. The fixture tests whether an implementation preserves SILT distinctions without importing an unstated rule or universalising the originating order.

| SATISFIED | NOT_SATISFIED | INDETERMINATE |
|---|---|---|
| Expressed condition is met. | Expressed condition is known not to be met. | No conclusion without importing an unstated rule, missing fact or external judgement. |

No other SILT evaluation outcome is introduced by this fixture. Where a condition does not enter SILT evaluation at all, no evaluation object should be created.

## Purpose and pressure test

**Purpose:** test whether SILT can preserve semantic Authority through recursive machine delegation while leaving operational agent machinery downstream.

**Pressure test:** Authority containment, semantic lineage, validity dependency, revocation and technical execution.

## Encounter

Participant P establishes bounded Authority AUTH-A. Agent A receives derived Authority and subsequently delegates a narrower Authority to Agent B. Agent B attempts ACT-X. A downstream technical system possesses valid keys or capabilities sufficient to execute the Action. SILT evaluates whether the semantic Authority supporting ACT-X remains valid at the encounter.

| Field | Normalised fixture value |
|---|---|
| Participants | P = originating authorising Participant; Agent-A = delegated agent; Agent-B = recursively delegated agent; R = receiving or relying system / counterparty |
| Primary Source | Originating mandate, institutional, contractual or other recognised ground, SRC-P. |
| Profile Expression | PE-AGENT |
| Primary semantic stress | Execution capability does not prove Authority; lineage does not automatically determine continuing validity. |

## Normalised semantic objects

### Source and Authorities

```text
SRC-P
  type: originating_mandate_or_other_recognised_ground

AUTH-A
  source_ref: SRC-P
  actor_ref: Agent-A
  permitted_action:
    - negotiate
    - commit_up_to_10000
  delegation_allowed: true
  delegable_scope:
    commit_up_to_5000

AUTH-B
  actor_ref: Agent-B
  parent_authority_ref: AUTH-A
  permitted_action:
    commit_up_to_3000
  lineage_refs:
    - AUTH-A
```

### Profile Expression

- Required Authority must be current.
- The proposed Action must fall within scope.
- Derived Authority must remain within the delegable envelope unless another recognised Source supplies additional Authority.
- Any required validity dependencies must be satisfied.
- Applicable Revocation must be evaluated.
- Technical execution capability alone is insufficient unless expressly made sufficient.

### Presentation and Action

```text
PRES-04
  participant_ref: Agent-B
  authority_refs:
    - AUTH-B
  evidence_refs:
    - CAPABILITY-01
    - DELEGATION-EVIDENCE-01
  proposed_action_ref:
    ACT-X

ACT-X
  actor_ref: Agent-B
  type: commit
  amount: 2500
```

Presentation remains implementation-light. In a machine encounter it may be carried by a message, capability-related invocation or other transient mechanism without becoming a new agent credential format.

## Expected base evaluation

```text
AUTH-A current:                         SATISFIED
AUTH-B within delegable envelope:        SATISFIED
AUTH-B current:                          SATISFIED
ACT-X within AUTH-B scope:               SATISFIED
Authority-mediated Attribution:          SATISFIED
external liability / Binding conclusion: not determined by Core
```

## Adversarial variants

### WE04-A - Scope overrun

```text
technical_execution_possible: true
AUTH-B scope for Action:      NOT_SATISFIED
```

### WE04-B - Missing validity-dependency rule

AUTH-A has expired, but PE-AGENT does not state whether AUTH-B remains independently operative.

```text
AUTH-B current validity: INDETERMINATE
```

SILT must not invent cascade behaviour.

### WE04-C - Expressed cascade

```text
AUTH-A: REVOKED
AUTH-B for subsequent exercise: NOT_SATISFIED
```

This result is justified only because the relevant dependency or cascade rule is expressly supplied.

### WE04-D - Lineage without continuing dependency

```text
AUTH-A: REVOKED
AUTH-B: may remain operative if the expressed conditions give AUTH-B independent continuing validity
```

Lineage records where Authority came from. It does not automatically say which upstream object must remain valid forever.

### WE04-E - Separate additional Source

Agent B may possess an additional Authority independently grounded in SRC-OTHER. An Action outside AUTH-A's delegable envelope is not automatically invalid if that separate recognised Source validly supplies the additional Authority.

## Revocation

```text
REV-01
  target_ref: AUTH-B
  effective_at: T
  authorised_revoker_ref: P

after T:
  AUTH-B for subsequent exercise: NOT_SATISFIED
```

A later Revocation does not retroactively rewrite a correctly performed earlier Action unless the expressed conditions specifically provide for such an effect.

## Conformance assertions

A conforming implementation MUST preserve:

- Technical Capability is distinct from Authority.
- Agent identity is distinct from Authority.
- Delegation is distinct from identity.
- Lineage is distinct from validity dependency.
- Parent Authority does not imply unlimited child Authority.
- Execution success is distinct from semantic validity.

A conforming implementation MUST NOT infer:

- valid token implies valid SILT Authority
- successful technical execution implies SATISFIED
- parent revocation automatically revokes every descendant
- AI agent requires a special universal Participant ontology
- recursive delegation requires an AI-specific Core primitive

## Fixture verdict

This fixture does not expose a missing SILT Core primitive. It tests a domain-specific configuration of the existing grammar. A failure should reopen only the affected semantic seam, not the architecture wholesale.
