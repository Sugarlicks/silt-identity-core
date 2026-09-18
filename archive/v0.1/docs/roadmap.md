# Roadmap

This roadmap reflects SILT Core’s deliberate specification-first posture.

SILT Core prioritises semantic clarity, resilience, and interoperability over premature optimisation, platform lock-in, or implementation claims.

The purpose of this repository is to define a stable authority semantics layer that multiple implementations may later adopt, critique, test, or extend.

This roadmap does not commit future releases beyond the current public release and the next planning cycle.

---

## Current release

### v0.1 — Initial public specification

Released.

v0.1 establishes the initial SILT Core framing:

* the authority problem
* the distinction between identity, permission, and authority
* the initial semantic frame for lawful digital action
* the foundational primitives
* the first misuse-case orientation
* the specification-first posture of the project

v0.1 is not intended to be a production implementation.

It provides a public basis for critique, review, refinement, and further specification work.

---

## Current reference work

A reference consent validator is available under:

```text
/reference/validators/consent
```

The validator is experimental and non-normative.

It is provided to test early implementation patterns only.

It does not define the SILT Core specification and does not constrain future v0.2 schema design.

Reference code should be treated as illustrative unless and until a future specification expressly makes a component normative.

---

## Next planning cycle

### v0.2 — Planned next release

v0.2 is being planned.

No final scope is asserted in this document.

The v0.2 planning process may consider:

* structured authority claims
* validation logic
* revocation and expiry handling
* expanded primitive definitions
* AI-agent execution contexts
* legal and governance workflow examples
* digital commerce examples
* DID/VC interoperability mapping
* misuse-case tests

These are planning areas, not release commitments.

The final v0.2 scope will be determined separately and should not be inferred from this roadmap.

---

## Planning principles

v0.2 planning should remain guided by the following principles:

### 1. Specification before implementation

Implementation should follow semantic clarity.

SILT Core should not lock itself into a wallet, chain, credential system, validator architecture, or governance framework before the underlying authority model is sufficiently clear.

### 2. Authority before action

The project should continue to centre the core question:

> Is this action legitimately authorised, in this context, right now?

Future work should strengthen the ability to express, inspect, validate, and revoke authority conditions before digital action is executed or relied upon.

### 3. Capacity before credential

SILT Core should preserve the distinction between identity, credential, account, and acting capacity.

A participant may be identifiable without being authorised.

A credential may attest a claim without proving mandate.

A signature may show approval without proving capacity.

### 4. Revocation as first-class

Delegation, consent, mandate, and reliance should not silently persist beyond scope.

Future work should continue to treat revocation, expiry, suspension, and supersession as structural features, not edge cases.

### 5. Plural authority sources

SILT Core should not assume a single source of authority.

Authority may arise through legal, contractual, organisational, institutional, customary, associative, technical, or community frameworks.

The grammar should remain plural-source and technology-agnostic.

### 6. Limited claims travel further

SILT Core should avoid overstating what it does.

It does not determine ultimate legal enforceability.

It does not replace courts, contracts, governance systems, identity systems, or professional advice.

It makes authority conditions explicit, structured, auditable, and revocable.

---

## Out of scope unless later adopted

The following are not currently committed as release deliverables:

* production wallets
* chain-specific implementations
* public registries
* certification schemes
* commercial validator services
* governance platforms
* legal advice products
* production AI-agent control systems
* fixed conformance levels
* stable implementation APIs

These may be considered separately in future work, but they are not asserted by this roadmap.

---

## Repository focus

The current repository focus is:

* specification development
* schema design
* reference validation experiments
* misuse cases
* interoperability notes
* conceptual documentation
* implementation-facing examples

The repository should remain clear about the difference between:

* normative specification
* exploratory planning
* illustrative examples
* experimental reference code

That distinction is load-bearing.

---

## Guiding principle

SILT Core values clarity before scale, semantics before software, and revocation before lock-in.

Implementations may come and go.

The integrity of the authority layer must endure.
