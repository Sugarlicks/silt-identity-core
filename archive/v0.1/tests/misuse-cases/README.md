# Misuse cases

This directory captures misuse cases and failure modes that identity implementers repeatedly encounter when consent, delegation, and disclosure are treated as informal conventions rather than enforceable constraints.

At the current **spec-first** stage, these are scenario definitions and test vectors-in-waiting. They are intended to guide:
- normative clarity in `spec/`
- validation shapes in `schemas/`
- later reference implementations and automated checks

Each misuse case is written so an implementer can ask: “Would my system fail here?”

## MC-01: Silent authority escalation via role inference
**Scenario**: A platform infers that a user is authorised because they are “an admin” or “a moderator”, without a delegation artefact.  
**Expected posture**: Deny-by-default. Acts must reference a valid delegation with scope and duration.  
**Relevant specs**: `spec/delegation.md`, `spec/principal.md`

## MC-02: Over-broad delegation with no expiry
**Scenario**: An agent receives authority “to manage everything” with no expiry and no scope boundaries.  
**Expected posture**: Scope must be explicit and time-boxed where feasible. Broad delegations are discouraged and must be explicit.  
**Relevant specs**: `spec/delegation.md`, `spec/revocation.md`

## MC-03: Delegation replay outside intended context
**Scenario**: A valid delegation is replayed for a different act class or a different transaction context.  
**Expected posture**: Scope checks must fail. Where context binding is used, replay should be detectable.  
**Relevant specs**: `spec/delegation.md`, `docs/threat-model.md`

## MC-04: Consent used for a different purpose (function creep)
**Scenario**: Consent granted for one purpose is reused for another, materially different purpose.  
**Expected posture**: Purpose limitation must be enforced. New purpose requires new consent.  
**Relevant specs**: `spec/consent.md`, `docs/threat-model.md`

## MC-05: Coerced over-disclosure (“show me everything or no service”)
**Scenario**: A verifier demands raw attributes (full DOB, address, identifiers) rather than a minimal proof.  
**Expected posture**: Minimal disclosure by default. Refusal to disclose beyond scope should not invalidate unrelated acts.  
**Relevant specs**: `spec/consent.md`, `docs/threat-model.md`

## MC-06: Correlation through re-used identifiers
**Scenario**: A principal is forced to use a stable identifier across unrelated contexts, enabling profiling and surveillance.  
**Expected posture**: Prefer context-bound proofs and avoid re-used global identifiers in routine transactions where feasible.  
**Relevant specs**: `spec/principal.md`, `docs/threat-model.md`

## MC-07: Revocation not checkable (hidden or privileged)
**Scenario**: A principal revokes consent or delegation, but verifiers cannot check revocation state without privileged access.  
**Expected posture**: Revocation must be checkable in a privacy-respecting way. If it cannot be checked, default to non-reliance.  
**Relevant specs**: `spec/revocation.md`, `docs/threat-model.md`

## MC-08: Acts performed after revocation
**Scenario**: An agent continues acting after a delegation is revoked, or a verifier continues to rely on revoked consent.  
**Expected posture**: Post-revocation acts/disclosures are unauthorised. Systems must check revocation for new reliance.  
**Relevant specs**: `spec/revocation.md`, `spec/delegation.md`, `spec/consent.md`

## MC-09: Principal substitution by platform account
**Scenario**: A platform treats the platform account as the principal, enabling substitution or custodial capture.  
**Expected posture**: The principal must be defined independently of platform identity. Capacity semantics must remain explicit.  
**Relevant specs**: `spec/principal.md`, `docs/threat-model.md`

## MC-10: Ambiguous capacity (“signing, but as who?”)
**Scenario**: A signature or approval occurs without an explicit capacity declaration, later exploited in dispute or coercion.  
**Expected posture**: Capacity is semantic. If capacity is unclear, the default posture is non-reliance.  
**Relevant specs**: `spec/principal.md`, `docs/threat-model.md`
