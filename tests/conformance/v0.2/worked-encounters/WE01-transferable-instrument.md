# WE01 - Transferable Instrument Encounter

**Persistent Obligation, changing Standing, and the non-collapse of technical control**

**Status:** FC1 normalised semantic fixture. Companion conformance material; non-normative except where it reproduces requirements from the canonical semantic architecture.

**Suite discipline:** Semantic conformance, not implementation conformance. The fixture tests whether an implementation preserves SILT distinctions without importing an unstated rule or universalising the originating order.

| SATISFIED | NOT_SATISFIED | INDETERMINATE |
|---|---|---|
| Expressed condition is met. | Expressed condition is known not to be met. | No conclusion without importing an unstated rule, missing fact or external judgement. |

No other SILT evaluation outcome is introduced by this fixture. Where a condition does not enter SILT evaluation at all, no evaluation object should be created.

## Purpose and pressure test

**Purpose:** test whether SILT can preserve an enduring Obligation while the relational position entitled to performance changes.

**Pressure test:** electronic control, transfer, endorsement and possession must not be collapsed into Standing, Authority, ownership or Obligation.

## Encounter

Participant B currently occupies the relevant instrument-holder position concerning NOTE-001. B undertakes a purported transfer or endorsement to Participant C. C subsequently Presents the resulting claimed Standing for an encounter concerning enforcement or further dealing with the instrument.

```text
A -> pay NZD 1000 -> holder of NOTE-001
```

| Field | Normalised fixture value |
|---|---|
| Participants | A = obligor; B = current instrument holder / transferor; C = claimed successor holder / presenting Participant |
| Primary Source | Instrument and relevant transfer relation, including NOTE-001, the prior recognised holder relation, and the relevant transfer or endorsement event. |
| Profile Expression | PE-INSTRUMENT |
| Primary semantic stress | Standing can change while Obligation persists. |

## Normalised semantic objects

### Source and Standing

```text
SRC-01
  type: instrument_and_relevant_transfer_relation
  grounds:
    - NOTE-001
    - prior recognised holder relation
    - applicable transfer / endorsement event

STAND-B
  participant_ref: B
  relation: instrument_holder
  object_ref: NOTE-001

STAND-C
  participant_ref: C
  relation: instrument_holder
  object_ref: NOTE-001
  claimed_basis:
    transfer_action_ref: ACT-TRANSFER-01
```

The record or document may evidence the Source-grounded relation. It is not automatically identical with that relation.

### Profile Expression

- B must occupy the relevant transferor position.
- The required transfer or endorsement conditions must be satisfied.
- C's resulting holder position must be sufficiently evidenced.
- Technical control alone is not sufficient unless the Profile Expression expressly makes it sufficient.
- The continuing Obligation survives holder change unless an expressed condition provides otherwise.

### Presentation and Evidence

```text
PRES-01
  participant_ref: C
  standing_refs:
    - STAND-C
  evidence_refs:
    - EVID-TRANSFER-01
    - EVID-CONTROL-01
  purpose:
    establish encounter-relevant holder Standing concerning NOTE-001

EVID-TRANSFER-01
  type: transfer_or_endorsement_record

EVID-CONTROL-01
  type: technical_control_evidence
```

### Obligation and Action

```text
OBL-01
  obligor_ref: A
  entitled_position:
    instrument_holder(NOTE-001)
  required_performance:
    pay NZD 1000
  state: OUTSTANDING

ACT-TRANSFER-01
  actor_ref: B
  type: transfer_or_endorsement
  object_ref: NOTE-001
  target_participant_ref: C
```

## Expected base evaluation

```text
B relevant Standing:              SATISFIED
transfer / endorsement condition: SATISFIED
C resulting Standing:             SATISFIED
continuity of OBL-01:              SATISFIED
aggregate SILT result:             absent unless PE-INSTRUMENT defines one
```

## Adversarial variants

### WE01-A - Wrongful technical control

```text
technical_control_present: true
C holder Standing: NOT_SATISFIED
```

Technical control supports neither universal holder Standing nor ownership by itself.

### WE01-B - Incomplete transfer lineage

```text
C holder Standing: INDETERMINATE
```

Missing evidence is not automatically a known failure. NOT_SATISFIED is appropriate only where an expressed condition is known not to have been met.

### WE01-C - Revoked agent attempts transfer

```text
agent technical execution: possible
agent Authority: NOT_SATISFIED
resulting transfer condition: evaluated under PE-INSTRUMENT
```

### WE01-D - Holder changes, Obligation remains

```text
STAND-B: no longer operative as current holder
STAND-C: SATISFIED
OBL-01: OUTSTANDING
```

The holder change does not itself extinguish and recreate the underlying Obligation. Transfer is not delegation.

## Conformance assertions

A conforming implementation MUST preserve:

- Technical control is distinct from Standing.
- Standing is distinct from ownership.
- Transfer is distinct from delegation.
- Standing may change without recreating the underlying Obligation.
- Evidence is distinct from the Source-grounded relation it supports.

A conforming implementation MUST NOT infer:

- wallet or technical control implies holder Standing
- holder Standing implies ownership
- transfer implies delegation
- new holder implies a new underlying Obligation

## Fixture verdict

This fixture does not expose a missing SILT Core primitive. It tests a domain-specific configuration of the existing grammar. A failure should reopen only the affected semantic seam, not the architecture wholesale.
