# Revocation

This specification defines **revocation** as the explicit withdrawal of an authority grant (delegation) or consent by the principal, with semantics that are checkable by verifiers.

Revocation is a first-class feature in SILT Core. It is not an administrative afterthought. Systems that cannot represent revocation clearly will drift toward capture and irreversible binding.

## 1. Definitions

**Revocation**  
The withdrawal of a consent or delegation by the principal, effective per the revocation semantics of the system and the relevant artefact.

**Revocation reference**  
A mechanism or pointer enabling verifiers to check whether an artefact has been revoked or has expired.

**Revocation event**  
A record that a consent or delegation has been revoked, including who revoked it, what was revoked, and when.

**Verifier**  
A party checking whether an act, disclosure, consent, or delegation remains valid.

## 2. Principle: revocation as a right

SILT Core assumes the principal retains the right to withdraw:
- consent for disclosure or use
- delegated authority to act on their behalf

Revocation is not retroactive by default, but it must stop continued reliance or future acts where possible.

## 3. Required elements of a revocation event

A revocation event MUST include, at minimum:

1. **Target identifier**  
   The identifier of the artefact being revoked (consent ID or delegation ID).

2. **Principal identifier**  
   The principal withdrawing the consent or delegation.

3. **Timestamp**  
   The time at which revocation is asserted.

4. **Reason code (optional but recommended)**  
   A minimal reason classification (for example, “expiry”, “withdrawn”, “superseded”, “misuse detected”, “error”).

5. **Revocation event identifier**  
   A stable reference for audit and dispute reconstruction.

Implementations MAY include additional metadata, but should minimise personal data by default.

## 4. Checkability requirements

Implementations MUST provide a method for verifiers to check revocation state that is:

- **Deterministic**: verifiers can reach the same conclusion given the same inputs
- **Timely**: revocation state updates propagate within a defined and documented window
- **Accessible**: verifiers can check without privileged access to private attributes
- **Privacy-respecting**: revocation checks should not create new correlation channels unnecessarily

The revocation check mechanism may be a registry lookup, signed log, distributed bulletin, or other scheme. SILT Core defines the semantics, not the storage technology.

## 5. Revocation and acts

An act or disclosure that references a consent or delegation MUST be evaluated against the revocation state of that artefact.

- Acts performed **before** revocation remain valid by default, unless downstream rules specify otherwise.
- Acts performed **after** revocation MUST be treated as unauthorised.

Systems should bind acts to timestamps or sequence numbers to support dispute reconstruction without relying on informal narratives.

## 6. Supersession

A principal MAY revoke by superseding an artefact with a newer one.

Where supersession is used, the system should:
- link the old artefact to the new artefact
- preserve the audit trail
- avoid ambiguity about which artefact is current

Supersession is recommended for routine updates where the relationship continues but terms change.

## 7. Expiry and automatic termination

Expiry is distinct from revocation but should be treated similarly for verifier purposes.

Implementations SHOULD support:
- explicit expiry timestamps in consent and delegation artefacts
- automatic termination where conditions are met (for example, settlement completed, event ended)

Expiry reduces risk by making open-ended reliance harder by default.

## 8. Default posture: non-reliance

Where revocation state cannot be checked, the default posture is non-reliance.

If a verifier cannot determine whether an artefact is revoked or expired, the verifier must treat it as invalid for the purpose of authorising new acts or disclosures.

## 9. Implementation guidance (non-normative)

Implementers should:
- keep revocation records small and non-identifying by default
- avoid revocation mechanisms that leak behavioural patterns unnecessarily
- document propagation assumptions and worst-case delays
- provide a clear path for principals to revoke without specialised tooling
