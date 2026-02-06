# Threat Model

This threat model identifies common failure modes in digital identity systems where consent, delegation, and disclosure are treated as interface conventions rather than enforceable constraints. SILT Core defines primitives intended to reduce these risks by making status, standing, authority, and revocation first-class and auditable.

## Scope

In scope:
- Status and standing as the capacity in which a principal acts
- Delegation semantics (acting “for and on behalf of” another party) with explicit scope and duration
- Consent as an enforceable constraint with revocation and expiry
- Privacy-preserving disclosure patterns (data minimisation by default)
- Misuse cases and test vectors implementers can run against their own systems

Out of scope:
- Wallet UX and key management (except where required to express revocation and non-repudiation)
- Chain selection, custody models, and attestation markets
- KYC, identity proofing, and institutional credential issuance

## Assets to protect

- The principal’s capacity to act without coercion or silent substitution
- The integrity of delegation boundaries (scope, duration, and revocability)
- The integrity of consent boundaries (what was agreed, by whom, for how long)
- Privacy: prevention of linkability, correlation, and over-disclosure
- Auditability: the ability to reconstruct “who acted in what capacity” without leaking unnecessary personal data

## Adversaries and pressures

- Malicious counterparties seeking leverage through over-broad delegation or disclosure
- Platforms and intermediaries optimising for capture, lock-in, and behavioural profiling
- State or corporate actors seeking correlation and surveillance via identity exhaust
- Opportunistic attackers exploiting replay, spoofing, or ambiguous authority semantics
- Internal governance failure: unclear roles, informal approvals, and silent escalation of authority

## Core failure modes

### 1) Silent authority escalation
A party obtains or manufactures authority beyond what the principal intended (for example, through ambiguous role language, “helpful” defaults, or inherited permissions).

Mitigations (SILT Core intent):
- Explicit delegation objects with scope, duration, and revocation pointers
- Capacity-first signatures: the capacity line is not decorative, it is semantic
- Deny-by-default: actions must be attributable to an explicit authority grant

### 2) Coercion and compelled over-disclosure
A principal is pressured to reveal more than necessary to complete a transaction, or to bind themselves in a capacity they did not intend.

Mitigations:
- Minimal disclosure patterns and selective revelation by default
- Consent objects that are time-boxed, purpose-bound, and revocable
- Clear separation between status/standing proofs and personal attributes

### 3) Correlation and linkability
Identity actions are linkable across contexts, enabling profiling, surveillance, and inference of sensitive facts
even where explicit identifiers are not disclosed.

Mitigations:
- Ephemeral, context-bound proofs rather than global identifiers
- Separation of long-lived status substrates from short-lived transaction attestations
- Avoidance of static, re-used identifiers in routine transactions where possible

### 4) Replay and duplication of authority
An approval or proof is re-used outside its intended context (for example, a consent artefact is replayed for a new transaction).

Mitigations:
- Nonces and context binding (transaction identifiers, terms hashes, or event IDs)
- Expiry, revocation, and “spent” semantics where appropriate
- Verifier checks against revocation state

### 5) Substitution of the principal
A system treats a wallet, account, or platform identity as the principal, enabling impersonation, substitution, or forced custodianship.

Mitigations:
- The principal is defined independently of any platform account
- Capacity semantics make “who is acting” explicit and testable
- Delegation is explicit, not implied by login state

### 6) Irreversible identity binding
A principal cannot exit a relationship, withdraw consent, or revoke an authority grant without catastrophic loss of access.

Mitigations:
- Revocation is first-class, not an administrative afterthought
- Clear lifecycle semantics for delegation and consent
- Migration and portability assumptions: reliance is voluntary, not enforced by architecture

### 7) Ambiguous semantics and informal approvals
Systems treat authority as an informal social layer (“the admin said OK”), making disputes unresolvable and enabling abuse.

Mitigations:
- Machine-readable authority and consent artefacts
- Audit trails that record capacity, scope, and expiry without unnecessary personal data
- Test vectors for common ambiguity patterns

## Misuse-case driven testing

SILT Core treats misuse cases as first-class design inputs. The `tests/misuse-cases/` directory will maintain scenarios that implementers can run to validate:

- delegation scope enforcement
- consent expiry and revocation handling
- replay resistance
- correlation minimisation defaults
- capacity attribution and audit reconstruction

## Design principle summary

- Capacity before claim
- Authority before action
- Consent as constraint, not courtesy
- Revocation as a right, not a ticket
- Minimal disclosure by default
- Auditability without surveillance
