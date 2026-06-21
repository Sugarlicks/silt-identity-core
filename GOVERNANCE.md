# Governance

SILT Core is a specification-first project focused on authority semantics for digital action.

It defines a public semantic layer for modelling capacity, authority source, mandate scope, consent, reliance, delegation, and revocation across digital systems.

SILT Core is independently stewarded, versioned, and maintained.

---

## Principles

Governance of SILT Core is guided by the following principles:

* **Status before attributes**
* **Authority before permission**
* **Capacity before credential**
* **Consent as constraint**
* **Revocation before irreversibility**
* **Plural authority sources**
* **Specification before implementation**

The project prioritises semantic clarity, long-term resilience, and careful versioning over speed.

---

## Stewardship

SILT Core is independently developed and versioned.

External collaboration is encouraged, including participation in standards bodies, working groups, research forums, and implementation discussions.

However, SILT Core maintains its own:

* specification direction
* versioning
* terminology
* architectural evolution
* public release boundaries

External discussion, adoption, or contribution does not transfer control over the SILT architecture.

This repository reflects the public specification layer only. SILT may include additional models, structures, instruments, or implementation pathways not disclosed publicly.

---

## Decision Making

Changes are assessed according to whether they improve:

* semantic clarity
* primitive consistency
* revocation logic
* misuse-case resilience
* interoperability with existing identity and trust systems
* technology-agnostic implementation potential
* long-term coherence of the specification

Speed is secondary to correctness.

A change should not be adopted merely because it is convenient for a specific platform, wallet, blockchain, credential system, or implementation environment.

---

## Versioning

The current public release is **v0.1**.

**v0.2 is being planned.**

Planning areas may include structured authority claims, validation logic, revocation semantics, expanded primitive definitions, AI-agent execution contexts, legal and governance workflow examples, digital commerce examples, DID/VC interoperability mapping, and misuse-case tests.

These are planning areas, not release commitments.

The final v0.2 scope will be determined separately.

No future release scope beyond v0.2 is asserted by this governance document.

---

## Normative and Non-Normative Material

SILT Core distinguishes between:

* normative specification material
* explanatory documentation
* illustrative examples
* experimental reference code
* misuse-case and threat-model material

Reference code is non-normative unless expressly stated otherwise in a specification document.

The reference consent validator under `/reference/validators/consent` is experimental and non-normative. It is provided to test early implementation patterns only. It does not define the specification and does not constrain future v0.2 schema design.

---

## Contribution Boundary

Contributions are welcome where they improve the public semantic layer.

Contributions should not:

* collapse capacity into identity or permission
* remove or weaken revocation logic
* impose a single source of authority
* assume one implementation substrate
* narrow SILT Core into legaltech only
* imply legal enforceability beyond the scope of the specification
* create release commitments beyond v0.2 planning

Major contributions should begin with an issue before a pull request.

---

## Governance Posture

SILT Core is open to critique, adoption, and extension.

It is not governed by external standards bodies, platforms, or implementation vendors.

The project may interoperate with many systems, but it does not subordinate its semantic direction to any one of them.

SILT Core should remain:

* technology-agnostic
* plural-source
* revocation-aware
* specification-first
* implementation-neutral

The purpose of governance is to protect the integrity of the authority layer.
