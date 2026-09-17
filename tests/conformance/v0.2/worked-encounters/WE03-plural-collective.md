# WE03 - Plural / Collective Encounter

**Separate evaluation under distinct Profile Expressions without a meta-order**

**Status:** Pre-freeze normalised semantic fixture. Non-normative until the v0.2 conformance suite is frozen.

**Suite discipline:** Semantic conformance, not implementation conformance. This fixture tests whether SILT preserves distinct normative orders, distinct provenance and distinct evaluative results without silently merging, ranking or subordinating them.

| SATISFIED | NOT_SATISFIED | INDETERMINATE |
|---|---|---|
| Expressed condition is met. | Expressed condition is known not to be met. | No conclusion without importing an unstated rule, missing fact or external judgement. |

Deliberate non-expression is not a fourth evaluation outcome. Where a condition is not expressed into the encounter, SILT creates no evaluation object for that condition.

## Purpose and pressure test

**Purpose:** test whether one Presentation can be evaluated separately under more than one applicable Profile Expression without SILT manufacturing a meta-order between them.

**Pressure test:** collective Standing, representational Authority, Profile Expression provenance, receiver-side requirements and deliberate non-expression must remain distinguishable.

## Encounter

A collective C governs access to a place, resource or arrangement according to its own relationships and decision processes. Participant P has C-recognised Standing and is claimed to have Authority arising from a collective process to act in the encounter.

A receiving order R also evaluates the encounter. Under R's expressed conditions, the requested act requires a registered, formally signed resolution. That condition is not satisfied.

Two Profile Expressions therefore apply:

```text
PE-C  collective expression
PE-R  receiving-order expression
```

PE-C's provenance is itself contested at the encounter: the substantive collective conditions are expressed, but whether the body or working group that produced PE-C had Authority to express those conditions remains unresolved.

One further collective condition is deliberately not expressed into SILT because faithful bounded expression is not available or appropriate.

## Normalised semantic objects

### Source and Standing

```text
SRC-C
  type: collective_relational_source
  grounds:
    - recognised relationship to Collective C
    - relevant collective practice / process

STAND-P-C
  participant_ref: P
  relation: C-recognised relational standing
  source_ref: SRC-C
```

P's relational Standing does not by itself establish Authority to represent, bind or speak for C.

### Presentation and Evidence

```text
PRES-03
  participant_ref: P
  standing_refs:
    - STAND-P-C
  claimed_authority_ref:
    - AUTH-P-C
  evidence_refs:
    - EVID-C-RELATION
    - EVID-C-PROCESS
  purpose:
    establish encounter-relevant Standing and claimed Authority for the proposed access arrangement

EVID-C-RELATION
  type: evidence_of_collective_relationship

EVID-C-PROCESS
  type: evidence_of_collective_process
```

### Authority and Action

```text
AUTH-P-C
  participant_ref: P
  claimed_relation: authority_to_act_for_collective_in_this_encounter
  source_ref: SRC-C

ACT-ACCESS-ARRANGEMENT
  actor_ref: P
  type: proposed_access_arrangement
  authority_ref: AUTH-P-C
```

### Profile Expressions

```text
PE-C
  provenance:
    claimed_expressing_body: WG-C
  expressed_conditions:
    - P has the relevant C-recognised Standing
    - the relevant collective process supports P's claimed Authority
  deliberately_non_expressed_conditions:
    - C-CONDITION-X

PE-R
  expressed_conditions:
    - P occupies the relevant relational position
    - a registered and signed resolution exists
    - that resolution supports the requested Authority
```

The Profile Expressions are bounded encounter-relevant expressions. Neither is a complete model of the order from which it arises.

## Expected base evaluation

### Under PE-C

```text
P relational Standing:                  SATISFIED
P claimed Authority under collective process: SATISFIED
WG-C Authority to express PE-C:         INDETERMINATE
C-CONDITION-X:                           NO SILT EVALUATION
```

The substantive Authority result under PE-C remains `SATISFIED`. The unresolved provenance of PE-C is recorded separately as `INDETERMINATE`; it does not silently rewrite the substantive condition into a different outcome.

### Under PE-R

```text
P relevant relational position:         SATISFIED
registered signed resolution condition:  NOT_SATISFIED
requested Authority under PE-R:          NOT_SATISFIED
```

### Cross-expression result

```text
PE-C Authority result: SATISFIED
PE-R Authority result: NOT_SATISFIED
aggregate SILT result: absent
```

Neither result invalidates, supersedes or silently ranks the other. SILT Core does not supply a universal conflict-of-laws rule or hidden receiver precedence rule.

## Extended encounter

### Stage 1 - Separate evaluation

Evaluate `PRES-03` under PE-C and PE-R separately. Preserve provenance, substantive conditions and results as distinct records.

### Stage 2 - Identify the point of non-satisfaction

The PE-R failure is the registered signed resolution condition. That result does not extinguish P's underlying collective Standing or retroactively invalidate the PE-C evaluation.

### Stage 3 - Continue, challenge or decline

The encounter may proceed through further Evidence, revision of a Profile Expression, challenge to provenance, an exception process, refusal, or withdrawal. Those are encounter- or order-specific pathways, not universal Core rules.

### Stage 4 - Re-evaluate after provenance resolution

If later Evidence establishes or defeats WG-C's Authority to express PE-C, that provenance condition may be re-evaluated. SILT need not rewrite the earlier substantive evaluation as though the unresolved provenance question had never existed.

## Adversarial variants

### WE03-P1 - PE-C provenance later established

```text
WG-C Authority to express PE-C: SATISFIED
P Authority under PE-C:         SATISFIED
```

The earlier substantive result need not be changed merely because provenance becomes determinate later.

### WE03-P2 - PE-C provenance later defeated

```text
WG-C Authority to express PE-C: NOT_SATISFIED
```

This affects the standing of PE-C as an encounter expression. SILT does not infer from that result alone that P lacked all underlying collective Standing or that every proposition stated in PE-C was false.

### WE03-P3 - Receiver offers an expressed exception pathway

PE-R may itself provide an exception, alternative evidence route or composition rule. SILT may evaluate that expressed pathway. SILT does not invent one.

### WE03-P4 - Receiver silently ranks PE-R above PE-C

```text
implementation behaviour: choose PE-R as controlling without an expressed rule
conformance result: FAIL
```

Receiver-side technical or institutional position does not create semantic precedence by itself.

### WE03-P5 - Membership or belonging treated as representational Authority

```text
STAND-P-C: SATISFIED
AUTH-P-C:  not established merely from Standing
```

Collective Standing and Authority to represent or bind the collective remain distinct.

### WE03-P6 - Deliberate non-expression treated as failure

```text
C-CONDITION-X: NO SILT EVALUATION
```

An implementation fails if it converts deliberate non-expression into `NOT_SATISFIED`, `INDETERMINATE`, invalidity or absence of legitimacy.

### WE03-P7 - Authority later changes while Standing persists

```text
STAND-P-C: persists
AUTH-P-C:  revoked, expired, superseded or otherwise no longer operative
```

The change in representational Authority does not automatically extinguish the relational Standing from which P remains connected to C.

### WE03-P8 - Competing collective expressions

A second collective body or process produces `PE-C2` with different encounter-relevant conditions.

```text
PE-C result:  retained under PE-C
PE-C2 result: evaluated separately under PE-C2
aggregate result: absent unless an expressed composition rule exists
```

SILT does not choose which collective expression is "really" authoritative merely because both enter the encounter.

## Conformance assertions

A conforming implementation MUST preserve:

- collective Standing is distinct from representational Authority;
- Profile Expression provenance is distinct from substantive evaluation under that Profile Expression;
- PE-C and PE-R remain distinct interpretive envelopes;
- results remain linked to the Profile Expression under which they were produced;
- deliberate non-expression creates no evaluation outcome;
- Authority may change while Standing persists; and
- competing collective expressions may coexist without SILT manufacturing a meta-order.

A conforming implementation MUST NOT infer:

- belonging or membership implies Authority to represent the collective;
- receiver-side rules automatically outrank an originating collective expression;
- disagreement between Profile Expressions means one is invalid;
- contested Profile Expression provenance automatically negates every substantive relation presented under it;
- non-expression is a failed condition; or
- multiple Profile Expressions require a single aggregate SILT result.

## Fixture verdict

This fixture does not expose a missing SILT Core primitive. It confirms the need to preserve separate Profile Expression provenance, separate per-expression evaluation and the distinction between relational Standing and representational Authority.

The architectural seam remains intact:

> **Source → Standing → Presentation → evaluation at the encounter**
