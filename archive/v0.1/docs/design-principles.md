# Design principles

## Spec-first, implementation-later

SILT Core is intentionally **spec-first**. This repository exists to define semantics, constraints, and failure modes before committing to any particular implementation architecture.

The project will prioritise:
- clear normative specifications (`spec/`)
- threat modelling and misuse-case testing (`docs/` and `tests/`)
- minimal, flexible schemas for interoperability (`schemas/`)

Reference implementations, adapters, and integration code are downstream concerns and will be approached only when the semantics are sufficiently stable and the real-world requirements are clearer.

This posture is deliberate. It reduces lock-in, avoids premature optimisation, and allows the underlying model of status, standing, authority, consent, and revocation to mature through research, writing, and plural-context evaluation.

## Capacity before claim
Acts must be attributable to a principal in a stated capacity. If capacity is unclear, the default posture is non-reliance.

## Authority before action
Authority must be explicit and referenceable. Delegation is never inferred from role titles, login state, or platform defaults.

## Consent as constraint
Consent is purpose-bound, minimal by default, time-boxed where feasible, and revocable.

## Revocation as a right
Revocation is first-class. Systems must make withdrawal of authority and consent checkable and practical.
