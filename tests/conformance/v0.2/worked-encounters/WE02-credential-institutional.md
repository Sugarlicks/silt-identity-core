# WE02 - Credential-Carried Institutional Encounter

**Credential Evidence, current Standing, and semantic continuity**

**Status:** FC1 normalised semantic fixture. Companion conformance material; non-normative except where it reproduces requirements from the canonical semantic architecture.

**Suite discipline:** Semantic conformance, not implementation conformance. The fixture tests whether an implementation preserves SILT distinctions without importing an unstated rule or universalising the originating order.

| SATISFIED | NOT_SATISFIED | INDETERMINATE |
|---|---|---|
| Expressed condition is met. | Expressed condition is known not to be met. | No conclusion without importing an unstated rule, missing fact or external judgement. |

No other SILT evaluation outcome is introduced by this fixture. Where a condition does not enter SILT evaluation at all, no evaluation object should be created.

## Purpose and pressure test

**Purpose:** test whether a credential can carry Evidence concerning Standing without becoming Source, Standing or Authority.

**Pressure test:** cryptographic validity must not manufacture relational validity.

## Encounter

Participant P Presents an institutional credential to Institution R in support of a claimed relational position and proposed Action. The credential verifies correctly cryptographically. The encounter asks whether the relevant institutional Standing and, where necessary, Authority remain operative now.

| Field | Normalised fixture value |
|---|---|
| Participants | P = presenting Participant; I = issuer / institutional actor; R = receiving institution |
| Primary Source | The underlying institutional relationship, recognition or appointment. |
| Profile Expression | PE-R |
| Primary semantic stress | Credential validity does not settle current Standing or Authority. |

## Normalised semantic objects

### Source and Standing

```text
SRC-INST
  type: institutional_relationship_or_appointment

STAND-P
  participant_ref: P
  relation: recognised_institutional_position
  source_ref: SRC-INST
```

The credential may evidence the institutional relation. It is not automatically identical with the relation or with its Source.

### Profile Expression

- Relevant institutional Standing must be current for this encounter.
- Specified Evidence may substantiate that Standing.
- Where the proposed Action requires Authority, current Authority must also be established.
- Cryptographic credential validity alone is insufficient unless the Profile Expression expressly makes it sufficient.

### Presentation and Evidence

```text
PRES-02
  participant_ref: P
  standing_refs:
    - STAND-P
  evidence_refs:
    - VC-01
  proposed_action_ref:
    ACT-02

VC-01
  type: verifiable_credential
  cryptographic_state: valid
```

## Expected base evaluation

```text
credential authenticity: SATISFIED
P relevant Standing:    SATISFIED
P Authority for ACT-02: SATISFIED  # only where separately required and established
```

## Adversarial variants

### WE02-A - Stale semantic relation

```text
credential authenticity: SATISFIED
Standing current:       NOT_SATISFIED
```

The credential may remain cryptographically valid even though the underlying appointment or recognition has ended.

### WE02-B - Current credential, unresolved current recognition

```text
credential authenticity: SATISFIED
Standing current:       INDETERMINATE
```

The supplied state does not establish whether the relevant recognition remains current. SILT must not invent the missing fact.

### WE02-C - Key rotation

```text
old key:   replaced
new key:   current
Standing:  unchanged unless the relevant semantic relation itself changed
```

### WE02-D - Credential proves affiliation, not Action Authority

```text
Standing: SATISFIED
Authority for ACT-02: INDETERMINATE
# or NOT_SATISFIED where an expressed Authority condition is known to fail
```

## Conformance assertions

A conforming implementation MUST preserve:

- Credential is distinct from Standing.
- Credential is distinct from Source.
- Issuer is not automatically a universal Source of legitimacy.
- Key control is distinct from Authority.
- Cryptographic continuity is distinct from semantic continuity.

A conforming implementation MUST NOT infer:

- valid credential implies current Standing
- trusted issuer implies universal legitimacy
- key control implies Authority
- institutional affiliation implies Authority for every Action

## Fixture verdict

This fixture does not expose a missing SILT Core primitive. It tests a domain-specific configuration of the existing grammar. A failure should reopen only the affected semantic seam, not the architecture wholesale.
