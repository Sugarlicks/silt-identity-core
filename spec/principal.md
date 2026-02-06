# Principal

This document defines the **principal** as the foundational subject of action in SILT Core. A principal is not a wallet, account, platform profile, or credential. A principal is the entity capable of forming intent, granting authority, consenting to terms, and revoking that authority.

SILT Core treats the principal and the capacity in which they act as primary. Attributes and credentials may be attached downstream, but they do not define who is acting.

## 1. Definitions

**Principal**  
The entity whose intent and authority a system must respect. A principal may act personally or through explicit delegation.

**Capacity**  
The role or standing in which a principal acts for a given act (for example, acting personally; acting as agent; acting as trustee; acting for an organisation). Capacity is a semantic constraint, not a label.

**Act**  
A discrete action that creates reliance or alters obligations (for example, entering an agreement, issuing an instruction, signing a note, granting authority, disclosing an attribute).

**Reliance**  
A counterparty’s justified dependence on an act as binding, based on the principal’s capacity, authority, and consent as expressed in the artefact.

**Authority grant (Delegation)**  
An explicit, bounded permission enabling an actor to perform specified acts in a specified capacity on behalf of a principal.

**Consent**  
An explicit, bounded permission for a specified disclosure or use, including scope, purpose, duration, and revocation.

**Revocation**  
A principal’s withdrawal of an authority grant or consent, effective per the revocation semantics of the system and the relevant artefact.

## 2. Non-goals

This specification does not define:
- identity proofing (KYC), credential issuance, or institutional trust frameworks
- wallet UX, custody models, or chain-specific signing formats
- governance, adjudication, or enforcement forums beyond reference examples

## 3. Principle: capacity-first identity

SILT Core requires that acts be attributable to a principal **in a stated capacity**. Systems must not infer capacity from context, login state, or course-of-dealing. If the capacity is unclear, the act is ambiguous and must be treated as non-binding by default.

This is the central discipline: capacity is how authority becomes legible without collapsing the principal into an account.

## 4. Principal identifiers

SILT Core does not mandate a single identifier scheme. A principal may be represented by one or more identifiers, provided the following properties are satisfied:

- **Continuity**: the principal can maintain a stable identity across systems without being trapped in a single platform
- **Non-substitution**: no identifier scheme should allow a platform to silently substitute itself as the principal
- **Auditability**: it must be possible to reconstruct which principal acted, in what capacity, without leaking unnecessary attributes

Implementations may use DIDs, public keys, registry references, or hybrid schemes. The specification is concerned with semantics and enforceability, not naming fashion.

## 5. Binding acts: requirements

An act is considered attributable and binding within SILT Core semantics only where all of the following are satisfied:

1. **Principal attribution**  
   The artefact must identify the principal (directly or by reference).

2. **Capacity declaration**  
   The artefact must state the capacity in which the principal acts for this act.

3. **Authority sufficiency**  
   If the act is performed by an agent or delegate, the artefact must reference an authority grant sufficient in scope and duration for the act.

4. **Consent sufficiency**  
   If the act involves disclosure or use of personal data or attributes, the artefact must reference a consent object sufficient in scope, purpose, and duration.

5. **Revocation checkability**  
   The system must provide a means to check whether the referenced authority grant or consent has been revoked or expired.

If any of the above are missing or ambiguous, the default posture is **non-reliance**.

## 6. Default posture: non-reliance

SILT Core assumes that reliance is voluntary and explicit. Where a counterparty cannot verify capacity, authority, consent, or revocation state, the counterparty must treat the act as non-binding and seek clarification.

This posture is designed to reduce coercion, silent escalation, and platform capture.

## 7. Notes on plural legal contexts

SILT Core is intended to support plural legal settings by making the semantics of authority and capacity explicit. It does not assume that a state is the source of identity. It assumes only that parties can express intent, bind themselves in a stated capacity, and manage reliance through explicit artefacts.

Downstream systems may map these artefacts into statutory rails, arbitration clauses, or institutional policy. SILT Core itself remains an infrastructure layer: it defines the primitives that make such mappings possible without collapsing the principal into a credential.

## 8. Implementation guidance (non-normative)

Implementers should:
- treat capacity declarations as machine-readable fields, not prose
- bind delegation and consent artefacts to acts via hashes or stable references
- avoid re-usable global identifiers for routine transactions where correlation risk is high
- ensure revocation is practical and visible to verifiers without exposing unnecessary personal data
