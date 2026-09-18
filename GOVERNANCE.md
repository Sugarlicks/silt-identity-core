# Governance

SILT Core is a specification-first project defining a semantic architecture for encounters across plural legal, cultural, customary, private, institutional and technical orders.

The controlling v0.2 semantic reference is:

[`spec/v0.2/semantic-architecture.md`](./spec/v0.2/semantic-architecture.md)

The canonical v0.2 seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

SILT Core is independently stewarded, versioned and maintained.

This governance document describes the current stewardship and change-control posture for the public SILT Core specification. It does **not** yet settle the project’s full Governance & IPR framework, patent policy, contribution licensing model or commercial implementation arrangements. Those matters require separate explicit treatment before substantive external contribution and adoption expand.

---

## Principles

Governance of SILT Core is guided by the following principles:

- **Source-grounded Standing** — Standing is relational and grounded in Source, not conferred universally by a receiving system.
- **Presentation at the encounter** — the minimum relevant projection is brought into a particular encounter without surrendering the originating order.
- **Profile Expression without ontological capture** — encounter-relevant conditions may be expressed without representing or governing the originating normative substrate as a whole.
- **Authority distinct from Technical Capability** — technical ability to execute does not by itself establish semantic Authority.
- **Evidence distinct from the relation evidenced** — credentials, signatures, registries and technical proofs do not silently become Standing or Authority.
- **Plurality without universal precedence** — multiple Profile Expressions may coexist or conflict without SILT imposing a universal meta-order.
- **Revocation and semantic continuity** — revocable relations must remain intelligible without collapsing semantic continuity into key or credential continuity.
- **Specification before implementation** — implementation machinery should not drive silent changes to the semantic architecture.
- **Semantically thick, operationally thin** — Core should retain necessary semantic distinctions while leaving authentication, transport, capability and execution machinery downstream.

The project prioritises semantic clarity, long-term resilience, plural applicability and careful versioning over speed or implementation convenience.

---

## Stewardship

SILT Core is independently developed, versioned and stewarded.

External collaboration is encouraged, including participation in standards bodies, working groups, research forums, institutional pilots, Indigenous and collective-authority encounters, implementation partnerships and adjacent-protocol discussions.

SILT Core nevertheless maintains its own:

- specification direction;
- versioning;
- terminology;
- release boundaries;
- conformance posture;
- architectural change process.

External discussion, adoption or implementation does not by itself alter the SILT Core specification.

Likewise, adoption by a particular platform, credential system, registry, legal order or standards body does not make that system the universal source of SILT Standing, Authority or legitimacy.

---

## Canonical architecture and release hierarchy

For v0.2, the canonical semantic architecture controls over older repository material.

The hierarchy is:

1. **Canonical semantic architecture** — the controlling v0.2 semantic reference.
2. **Release errata**, where formally published after v0.2.0.
3. **Explanatory and companion documentation** — useful for interpretation but not a substitute for the canonical architecture.
4. **Conformance fixtures and test notation** — used to pressure-test and validate semantic distinctions, not to define a universal wire format.
5. **Implementation profiles, examples and reference code** — non-normative unless a future specification expressly states otherwise.

Where older v0.1 documents, schemas or examples conflict with v0.2, the conflict should be made explicit rather than silently harmonised.

---

## Current release position

### v0.1

v0.1 is released and remains the implementation basis for work that began against that architecture.

In particular, the **Vietsch / AUT CISRC research-delegation implementation remains a SILT Core v0.1 implementation to completion**. It is not being migrated mid-stream to v0.2.

A later migration analysis may compare the completed implementation against v0.2, but that will not alter the basis of the funded v0.1 work.

### v0.2

SILT Core v0.2 is at **Freeze Candidate 1**. Repository reconciliation, conformance packaging and release-level licensing classification are complete; final release packaging remains underway.

The pre-freeze pressure-test gate has been completed through four worked encounters, machine-readable conformance validation and an experimental adjacent-protocol mapping. No new Core primitive was required by that gate.

Release work should therefore preserve the frozen architecture rather than reopening it through documentation, schema or implementation convenience.

---

## Decision making

Changes are assessed according to whether they improve or preserve:

- semantic clarity;
- fidelity to the Source → Standing → Presentation → evaluation seam;
- distinction between semantic and technical layers;
- plural applicability across legal, customary, private and institutional orders;
- misuse-case and adversarial resilience;
- interoperability without semantic collapse;
- long-term coherence and implementability.

Speed is secondary to correctness.

A change should not be adopted merely because it is convenient for a particular platform, wallet, blockchain, credential format, agent framework, validator architecture or implementation environment.

---

## Post-freeze scope discipline

After v0.2 semantic freeze, a proposed Core change should meet a high threshold.

A new primitive or architectural change should not be added merely because:

- another standard uses a similar noun;
- an implementation prefers a different data structure;
- a validator is easier to build with an additional field or object;
- one jurisdiction, institution or platform treats a concept as universal within its own system;
- a technical protocol provides a mechanism that resembles a SILT semantic relation.

A Core change should be considered only where implementation, research or encounter evidence exposes a recurring semantic distinction that cannot be expressed faithfully through the existing architecture without material distortion.

After release, semantic changes should be handled transparently through errata or a subsequent version rather than through silent revision of v0.2.

---

## Normative and non-normative material

SILT Core distinguishes between:

- normative semantic architecture;
- explanatory and positioning documentation;
- companion mappings;
- worked encounters and conformance fixtures;
- implementation profiles;
- illustrative examples;
- experimental reference code;
- threat-model and misuse-case material.

Reference code is non-normative unless expressly stated otherwise in a specification document.

Conformance fixtures test the semantic architecture but do not define a mandatory serialisation format.

Implementation profiles apply SILT in bounded domains. They do not acquire normative status merely because they are deployed in a real institution or funded implementation.

---

## Contribution boundary

Contributions are welcome where they improve the public semantic specification, its explanation, conformance evidence or implementation understanding.

Contributions should not:

- reintroduce `Status` as a Core object;
- reintroduce universal `Capacity` as a Core primitive;
- collapse Standing into credential possession, identity or system recognition;
- collapse Authority into Technical Capability or runtime permission;
- treat Profile Expression as a complete representation of an originating normative order;
- impose a universal precedence rule across Profile Expressions;
- infer Binding, liability or legal enforceability from successful SILT evaluation alone;
- require one technical implementation substrate;
- turn SILT into a universal identity, authorisation or conflict-of-laws system;
- weaken the distinction between normative semantics and implementation machinery.

Major contributions should begin with an issue or equivalent design discussion before a pull request.

---

## Governance & IPR direction

The v0.2 repository licensing boundary is now stated in [`LICENSING.md`](./LICENSING.md): **CC BY 4.0** for the canonical specification and human-readable documentation, and **Apache License 2.0** for reference code and implementation-oriented machine-readable artefacts.

That resolves the release-level licence classification for those materials. It does **not** settle the project’s full Governance & IPR framework.

The project still requires separate explicit treatment of matters including:

- contributor rights and contribution terms;
- patent/IPR and any standards-essential patent commitments;
- change control and maintainer authority beyond the current release process;
- trademark, certification, assurance and endorsement policy;
- future working-group or standards-body participation;
- commercial implementation and partnership boundaries where they involve official SILT status or representation;
- stewardship continuity.

The release direction remains to keep the semantic specification openly available while preserving room for sustainable implementation, assurance, training, tooling and advisory activity around it.

Open licensing does not itself confer certification, endorsement, trademark rights, stewardship authority or a right to represent an implementation as official SILT infrastructure.

Until the broader Governance & IPR framework is adopted, no contributor or adopter should assume that repository governance or open licensing alone resolves patent, certification, trademark, standards-participation, commercialisation or broader stewardship questions.

---

## Governance posture

SILT Core is open to critique, adoption, implementation and extension.

It may participate in, contribute to and learn from external standards and institutional processes without subordinating its semantic architecture to any one of them.

SILT Core should remain:

- plural-order;
- Source-grounded;
- encounter-centred;
- technology-agnostic;
- implementation-neutral at the semantic layer;
- semantically thick and operationally thin;
- explicit about what is normative and what is not.

The purpose of governance is to protect the integrity of the semantic encounter layer while allowing the project to become usable, institutionally credible and sustainable infrastructure.
