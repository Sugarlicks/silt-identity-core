# Consent

This specification defines **consent** as an explicit, bounded permission granted by a principal for a specific disclosure or use, with clear scope, purpose, duration, and revocation semantics.

Consent in SILT Core is not implied by participation, login state, or interface convention. It exists only where it is explicitly granted and referenceable.

## 1. Definitions

**Consent**  
An explicit permission for a specified use or disclosure, bounded by scope, purpose, duration, and revocation.

**Principal**  
The entity granting consent.

**Recipient / Verifier**  
The party receiving a disclosure or relying on a consent artefact.

**Disclosure**  
The release of data or proof about the principal or their status in a given context.

**Purpose**  
The stated reason for the disclosure or use. Purpose is a constraint.

**Scope**  
The set of data items, predicates, or proof claims permitted for disclosure or use.

**Duration**  
The temporal bounds of the consent, including expiry.

**Revocation**  
The principal’s withdrawal of consent, effective per the checkable revocation semantics of the system.

## 2. Principle: consent as constraint

SILT Core treats consent as an enforceable constraint. Systems must not treat consent as:
- a generic acceptance of platform terms
- a blanket permission for future unspecified uses
- a permanent grant by default

If the consent constraints cannot be verified, the default posture is non-disclosure and non-reliance.

## 3. Required elements of a consent artefact

A consent artefact MUST include, at minimum:

1. **Principal identifier**  
   Identifies the principal granting consent.

2. **Recipient identifier (or recipient class)**  
   Identifies who may rely on the consent (a specific party, or a narrowly defined class).

3. **Purpose**  
   A machine-readable purpose declaration (for example, “age eligibility check”, “membership verification for event X”, “settlement instruction for contract Y”).

4. **Scope**  
   The permitted disclosures or proofs. Scope should be minimal by default.

5. **Duration**  
   Start and expiry. Open-ended consents MUST be explicit and are discouraged by default.

6. **Revocation reference**  
   A mechanism or pointer enabling verifiers to check revocation or expiry state.

7. **Consent identifier**  
   A stable reference that disclosures can cite to bind reliance.

## 4. Consent and disclosure

Any disclosure performed under SILT Core semantics MUST:
- reference a consent identifier
- be consistent with the consent scope and purpose
- occur within the consent duration
- be checkable for revocation or expiry

Disclosures outside scope, purpose, or duration MUST be treated as unauthorised.

## 5. Minimal disclosure by default

SILT Core assumes minimal disclosure as the baseline posture.

Implementations should prefer:
- predicates over values (prove “over 18” rather than disclose date of birth)
- context-bound proofs rather than global identifiers
- single-use or short-lived consent artefacts where feasible

## 6. Purpose limitation

A consent artefact MUST be purpose-bound. Reuse of consent for a materially different purpose is prohibited unless a new consent artefact is granted.

Purpose limitation is intended to reduce function creep and surveillance drift.

## 7. Revocation and expiry

Implementations MUST provide:
- a means for principals to revoke consent
- a means for verifiers to check revocation or expiry
- clear semantics for disclosures performed before and after revocation

Revocation does not retroactively invalidate disclosures already made, but it must prevent continued reliance or further disclosure where possible.

## 8. Default posture: non-disclosure

Where:
- a consent reference is missing
- purpose or scope is ambiguous
- duration cannot be verified
- revocation state cannot be checked

the system MUST default to non-disclosure and treat the requested disclosure as unauthorised.

This posture is designed to prevent coercion, over-disclosure, and silent expansion of data use.

## 9. Notes on plural legal contexts

Consent semantics in SILT Core are intentionally explicit and minimal so they can map across legal and cultural contexts while avoiding reliance on platform terms as the primary source of permission.

SILT Core defines the artefacts that make consent legible and contestable, regardless of the downstream forum used to resolve disputes.

## 10. Implementation guidance (non-normative)

Implementers should:
- use machine-readable purpose and scope fields
- bind consent artefacts to contexts via hashes or stable references
- design for short-lived consents by default
- expose revocation state without leaking unnecessary personal data
- ensure that refusal to disclose does not prevent unrelated acts
