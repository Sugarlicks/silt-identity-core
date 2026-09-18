# WE03 - Plural / Collective Encounter

**Conflicting Profile Expressions, contested provenance, and deliberate non-expression**

**Status:** FC1 normalised semantic fixture. Companion conformance material; non-normative except where it reproduces requirements from the canonical semantic architecture.

**Suite discipline:** Semantic conformance, not implementation conformance. The fixture tests whether an implementation preserves SILT distinctions without importing an unstated rule or universalising the originating order.

| SATISFIED | NOT_SATISFIED | INDETERMINATE |
|---|---|---|
| Expressed condition is met. | Expressed condition is known not to be met. | No conclusion without importing an unstated rule, missing fact or external judgement. |

No other SILT evaluation outcome is introduced by this fixture. Where a condition does not enter SILT evaluation at all, no evaluation object should be created.

## Purpose and pressure test

**Purpose:** test whether different normative orders can make themselves mutually legible at a single encounter while remaining distinct.

**Pressure test:** conflicting Profile Expressions, contested provenance, collective Standing, representational Authority and deliberate non-expression.

## Encounter

Collective C governs access to collectively held material. Participant P has recognised relational Standing within C and has completed a collective process that, under PE-C, is sufficient to authorise P to negotiate and approve a defined access arrangement. Receiving Institution R applies PE-R, under which representational Authority requires a digitally signed resolution in R's approved governance registry. P does not possess that artefact. A subgroup within C contests the Authority under which Working Group WG authored PE-C. C also indicates that another encounter-relevant condition exists but cannot be adequately expressed in SILT without material distortion.

| Field | Normalised fixture value |
|---|---|
| Participants | P = presenting Participant; C = collective / originating order; WG = author of PE-C; R = receiving institution |
| Primary Source | Collective relational and governance Source, SRC-C. |
| Profile Expressions | PE-C and PE-R, evaluated separately. |
| Primary semantic stress | Plural evaluation without a universal meta-order or forced translation. |

## Normalised semantic objects

### Source and Standing

```text
SRC-C
  type: collective_relational_and_governance_source

STAND-P-C
  participant_ref: P
  relation: recognised relational position within C
  source_ref: SRC-C
```

### Profile Expressions

```text
PE-C
  provenance:
    authored_by: WG
    authority_ref: AUTH-WG-PE-C
    authority_to_express: contested
  conditions:
    - P relational Standing
    - recognised collective process sufficient for the defined Authority
    - institutional registry resolution not required
    - one encounter-relevant condition deliberately remains outside bounded expression

PE-R
  conditions:
    - recognised position in relation to C
    - registered digitally signed resolution required for representational Authority
```

The same Presentation is evaluated under both expressions. SILT does not merge PE-C and PE-R into a synthetic rule set or silently rank one above the other.

### Presentation

```text
PRES-03
  participant_ref: P
  standing_refs:
    - STAND-P-C
  authority_refs:
    - AUTH-P-ACCESS
  evidence_refs:
    - EVID-C-RELATION
    - EVID-C-PROCESS
  proposed_action_ref:
    ACT-ACCESS-ARRANGEMENT
```

`AUTH-P-ACCESS` and `AUTH-WG-PE-C` are FC1 reference identifiers used to align this human-readable fixture with the machine-readable companion. They name relations already present in the source fixture; they do not add new encounter conditions.

## Expected evaluations

### Under PE-C

```text
P relational Standing:          SATISFIED
P Authority for defined Action: SATISFIED
WG Authority to express PE-C:   INDETERMINATE
```

The earlier phrase `SATISFIED provisionally` is not used. Uncertainty about PE-C provenance is represented separately through the `INDETERMINATE` provenance condition, rather than creating a qualified fourth outcome.

### Under PE-R

```text
P relational position:           SATISFIED
registry-backed resolution:       NOT_SATISFIED
P Authority for requested Action: NOT_SATISFIED
```

### Across Profile Expressions

```text
aggregate SILT result: absent
```

Any rule of precedence, mutual recognition, application or negotiated accommodation requires its own expressed ground. SILT does not supply one universally.

## Deliberate non-expression

```text
NONEXP-01
  indicated: true
  reason:
    bounded expression would risk material distortion
```

There is deliberately no evaluation object for the unexpressed condition. Non-expression is not `SATISFIED`, `NOT_SATISFIED` or `INDETERMINATE`. It means the condition did not enter SILT evaluation.

## Adversarial variants

- **P1:** provenance is resolved in favour of WG, so Authority to express PE-C becomes `SATISFIED`.
- **P2:** the provenance challenge succeeds against WG; PE-C remains legible as a claimed expression but is not treated as authoritatively applicable.
- **P3:** R accepts C's collective-process Evidence through an expressed exception or agreement.
- **P4:** R silently ranks PE-R above PE-C without an expressed precedence rule. This fails conformance.
- **P5:** collective membership or belonging is incorrectly treated as sufficient representational Authority. This fails conformance.
- **P6:** deliberate non-expression is treated as absence or `NOT_SATISFIED`. This fails conformance.
- **P7:** a later collective process changes P's Authority while P's relational Standing remains unchanged.
- **P8:** two competing collective Profile Expressions emerge within C; neither is silently canonicalised.

## Conformance assertions

A conforming implementation MUST preserve:

- Collective Standing is distinct from representational Authority.
- PE-C and PE-R remain distinct expressions.
- Substantive Authority evaluation is distinct from Profile Expression provenance evaluation.
- Non-expression is distinct from `INDETERMINATE`.
- Encounter disagreement is distinct from universal invalidity.

A conforming implementation MUST NOT infer:

- one Profile Expression has universal precedence without an expressed ground;
- membership implies Authority to bind the collective;
- an unexpressed condition has machine-inferable content;
- R's registry requirement constitutes C's internal governance; or
- cross-order disagreement must collapse into a single validity result.

## Fixture verdict

This fixture does not expose a missing SILT Core primitive. It tests a domain-specific configuration of the existing grammar. A failure should reopen only the affected semantic seam, not the architecture wholesale.
