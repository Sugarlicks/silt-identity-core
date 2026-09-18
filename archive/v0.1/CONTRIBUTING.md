# Contributing

We welcome contributions that improve:

* clarity of definitions
* semantic consistency
* interoperability with identity systems
* threat modelling and misuse cases
* schema clarity
* reference examples
* revocation and consent modelling

SILT Core is a specification-first project focused on authority semantics for digital action.

The current public release is **v0.1**.

**v0.2 is being planned.**

---

## Scope of Contributions

Contributions should focus on the **public semantic layer**, including:

* capacity expression
* authority source referencing
* mandate scoping
* consent conditions
* reliance conditions
* revocation pathways
* misuse cases
* interoperability notes
* implementation-facing examples

Contributions should help make the distinction between identity, permission, capacity, authority, consent, reliance, and revocation clearer.

Please preserve the core distinction:

> A system may permit an action without proving that the action is legitimately authorised.

---

## Contribution Boundary

SILT Core defines a public semantic layer.

It may be discussed in external standards bodies, working groups, research forums, and implementation contexts.

However:

* contributions in external forums do not constitute transfer of the full SILT architecture
* SILT may include additional models, structures, instruments, and implementation pathways not disclosed publicly
* this repository reflects the **public specification layer only**
* reference code is experimental unless expressly marked as normative
* planning notes do not create release commitments

This boundary matters.

SILT Core is open at the semantic layer, but the full architecture may include additional private, commercial, legal, governance, or assurance components.

---

## Current Release Position

**v0.1** has been released as the initial public specification and framing layer.

v0.1 establishes:

* the authority problem
* the distinction between identity, permission, and authority
* the initial semantic frame
* the foundational primitives
* the specification-first posture of the project

**v0.2** is being planned.

Candidate areas may include structured authority claims, validation logic, revocation semantics, expanded primitive definitions, AI-agent execution contexts, legal and governance workflow examples, digital commerce examples, DID/VC interoperability mapping, and misuse-case tests.

These are planning areas, not release commitments.

---

## Reference Code

Reference code may exist in this repository.

For example, the reference consent validator under `/reference/validators/consent` is experimental and non-normative.

It is provided to test early implementation patterns only.

It does not define the specification and does not constrain future v0.2 schema design.

---

## Please Avoid

Please avoid contributions that:

* assume a specific platform, wallet, blockchain, or credential system
* collapse capacity into identity or permissions
* remove or weaken revocation logic
* imply that SILT Core guarantees legal enforceability
* treat reference code as normative specification
* impose a single source of authority
* narrow SILT Core into legaltech only
* create release commitments beyond v0.2 planning

---

## Preferred Language

Where possible, use precise language such as:

* participant
* action
* capacity
* authority source
* mandate scope
* consent conditions
* reliance conditions
* revocation state

Avoid treating “identity”, “account”, “holder”, “agent”, “actor”, and “user” as interchangeable unless the context clearly requires it.

---

## Before Major Contributions

Before major contributions, please open an issue for discussion.

A useful issue should explain:

* the problem or gap
* the affected primitive, schema, document, or misuse case
* the proposed change
* whether the contribution is intended to be normative, explanatory, illustrative, or experimental

Small documentation fixes may be submitted directly by pull request.

---

## Licence

By contributing to this repository, you agree that your contribution will be licensed under the repository licence unless otherwise stated.

This repository is licensed under the Apache License 2.0.

See [`LICENSE`](./LICENSE) for details.
