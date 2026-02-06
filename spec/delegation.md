# Delegation

This specification defines **delegation** as the explicit granting of authority by a principal to another actor to perform specified acts in a specified capacity, for a bounded scope and duration.

Delegation in SILT Core is never implicit. It is not inferred from role titles, login state, organisational charts, or historical behaviour. Delegation exists only where it is explicitly granted and referenceable.

## 1. Definitions

**Delegation (Authority Grant)**  
A bounded permission issued by a principal that authorises an agent to perform specified acts on behalf of the principal, in a stated capacity.

**Principal**  
The entity whose authority is being delegated.

**Agent / Delegate**  
The actor authorised to perform acts under a delegation grant. An agent may be a natural person, organisation, software agent, or other recognised actor.

**Scope**  
The set of acts, domains, or action classes the agent is authorised to perform.

**Duration**  
The temporal bounds of the delegation, including start conditions, expiry, and any renewal semantics.

**Revocation reference**  
A pointer or mechanism by which verifiers can determine whether a delegation has been withdrawn or has expired.

## 2. Non-goals

This specification does not define:
- employment law, fiduciary duties, or liability allocation
- organisational hierarchies or internal governance rules
- enforcement or adjudication mechanisms beyond reference checks

These concerns may be layered on downstream.

## 3. Principle: explicit authority

SILT Core requires that any act performed by an agent on behalf of a principal reference an explicit delegation artefact.

Systems must not assume authority based on:
- role names
- membership lists
- prior approvals
- platform administrator status

If authority is not explicit and referenceable, the act must be treated as unauthorised by default.

## 4. Required elements of a delegation artefact

A delegation artefact MUST include, at minimum:

1. **Principal identifier**  
   Identifies the principal granting authority.

2. **Agent identifier**  
   Identifies the agent receiving authority.

3. **Capacity declaration**  
   States the capacity in which the agent is authorised to act (for example, “agent”, “trustee”, “representative”).

4. **Scope**  
   A machine-readable description of the permitted acts or action classes.

5. **Duration**  
   Start conditions and expiry. Open-ended delegations MUST be explicit and are discouraged by default.

6. **Revocation reference**  
   A mechanism or pointer enabling verifiers to determine revocation or expiry state.

7. **Delegation identifier**  
   A stable reference that acts can cite to bind reliance.

## 5. Delegation and acts

Any act performed by an agent under SILT Core semantics MUST:

- reference a delegation identifier
- be consistent with the delegation’s scope
- occur within the delegation’s duration
- be attributable to the principal in the stated capacity

Acts outside scope, duration, or capacity MUST be treated as unauthorised.

## 6. Chained delegation

SILT Core allows chained delegation only where explicitly authorised.

A delegation artefact MAY permit the agent to sub-delegate authority, but only where:
- the ability to sub-delegate is explicitly granted
- scope and duration constraints are preserved or narrowed
- each link in the chain is referenceable and auditable

Absent explicit permission, delegation is non-transferable.

## 7. Default posture: deny by default

Where:
- a delegation reference is missing
- scope is ambiguous
- duration cannot be verified
- revocation state cannot be checked

the system MUST default to non-reliance and treat the act as unauthorised.

This posture is intended to prevent silent escalation of authority and platform capture.

## 8. Revocation and expiry

Delegation is not permanent by default.

Implementations MUST provide:
- a means for principals to revoke delegation
- a means for verifiers to check revocation or expiry
- clear semantics for acts performed before and after revocation

Revocation does not retroactively invalidate acts performed while authority was valid, unless explicitly specified by downstream rules.

## 9. Notes on plural legal contexts

Delegation semantics in SILT Core are intentionally minimal and explicit so they can map onto diverse legal traditions, including agency, mandate, trust, and representation doctrines.

SILT Core does not resolve disputes. It defines the artefacts that make disputes legible without collapsing authority into institutional assumptions.

## 10. Implementation guidance (non-normative)

Implementers should:
- use machine-readable scope expressions rather than free text
- bind delegation artefacts cryptographically or by stable hash
- avoid long-lived, broad delegations where narrower, time-bound grants suffice
- expose revocation state without leaking unnecessary personal data
