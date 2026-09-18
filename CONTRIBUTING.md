# Contributing

SILT Core welcomes critique, research, conformance work, implementation evidence and carefully scoped contributions that strengthen the public specification without collapsing plural semantic relations into a single technical or institutional model.

The controlling v0.2 semantic reference is:

[`spec/v0.2/semantic-architecture.md`](./spec/v0.2/semantic-architecture.md)

The canonical v0.2 seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

If a proposed contribution conflicts with the canonical semantic architecture, the conflict should be surfaced explicitly. It should not be resolved by silently altering terminology or importing assumptions from older repository material.

---

## Current release position

### v0.1

v0.1 is released and remains the implementation basis for work that began against that architecture.

The **Vietsch / AUT CISRC research-delegation implementation remains a SILT Core v0.1 implementation to completion**. Contributions to that implementation should preserve its v0.1 basis unless a later, explicitly separate migration phase is opened.

### v0.2

SILT Core v0.2 is at **Freeze Candidate 1**. Repository reconciliation, conformance packaging and release-level licensing classification are complete; final release packaging remains underway.

The pre-freeze gate has already been completed through worked encounters, machine-readable conformance validation and an experimental adjacent-protocol mapping. Contribution work during this phase should therefore preserve the frozen architecture rather than reopen it through implementation convenience.

---

## Types of contribution

Contributions may fall into different categories. Please identify the intended category clearly.

### Normative semantic specification

Changes to the canonical semantic architecture or formal errata.

These require the highest level of scrutiny because they may alter the meaning of SILT Core itself.

### Explanatory or companion documentation

Material that explains, compares or positions the architecture without changing Core semantics.

Examples include:

- adjacent-standards mappings;
- domain explanations;
- implementation guidance;
- research notes;
- ecosystem positioning.

### Conformance material

Worked encounters, fixtures, test vectors, runners and semantic non-inference tests used to pressure-test the architecture.

Conformance notation does not automatically become a normative SILT wire format.

### Implementation profiles and examples

Bounded applications of SILT in a particular institutional, customary, commercial, technical or agentic setting.

Implementation profiles are non-normative unless a future specification expressly says otherwise.

### Reference code

Validators, adapters, utilities and experimental implementation code.

Reference code does not define Core semantics merely because it executes them.

---

## Preferred contribution areas

Useful contributions include:

- clearer treatment of Source-grounded Standing;
- worked examples of Presentation at real encounters;
- Profile Expression examples that preserve the independence of the originating substrate;
- adversarial tests involving Indigenous or collective authority;
- private-ordering and trust encounters;
- institutional delegation;
- AI-agent and recursive delegation scenarios;
- Evidence / semantic-relation separation;
- Technical Capability / Authority separation;
- semantic continuity under key or credential change;
- Attribution, Obligation and Revocation tests;
- multi-Profile-Expression encounters;
- misuse cases and semantic non-inference tests;
- interoperability work that identifies the layer occupied by adjacent standards;
- implementation evidence showing where the existing architecture succeeds or fails.

---

## Contribution boundary

Please do not submit changes that silently:

- reintroduce `Status` as a SILT Core object;
- reintroduce universal `Capacity` as a Core primitive;
- treat credentials, signatures, registries or issuer trust as universal Sources of Standing;
- collapse Standing into identity, membership, credential possession or system recognition;
- collapse Authority into Technical Capability, access permission or successful execution;
- equate Presentation with a particular credential or message format;
- treat Profile Expression as a complete representation of an originating normative order;
- impose a universal ranking or merger rule across Profile Expressions;
- infer Binding, liability or legal enforceability from successful SILT evaluation alone;
- require every normative condition to be machine-evaluable;
- make one wallet, chain, protocol, identity system, agent framework or registry a mandatory SILT substrate;
- convert an implementation-specific rule into a universal Core rule without evidence that the semantic distinction recurs across domains.

The project should remain **semantically thick and operationally thin**.

---

## Scope-discipline test for proposed Core changes

A new Core primitive, new universal rule or architectural change should be proposed only where there is evidence of a **recurring semantic distinction** that the existing v0.2 architecture cannot represent faithfully without material distortion.

Before proposing such a change, please address the following questions:

1. **What exact semantic distinction is missing?**  
   Name the distinction rather than the desired field, class or implementation object.

2. **Where does the problem recur?**  
   Show more than one materially different encounter or order where possible.

3. **Why can the existing architecture not express it?**  
   Test Source, Standing, Presentation, Profile Expression, Evidence, Authority, Consent, Reliance, Action, Attribution, Obligation and Revocation before proposing a new primitive.

4. **Is the proposed concept actually implementation machinery?**  
   Authentication, keys, credentials, capability tokens, dynamic authorisation, transport, policy engines and execution normally remain downstream.

5. **Does the proposal privilege one ontology or institutional model?**  
   A concept that appears universal inside one legal, technical or organisational system may not be universal across plural orders.

6. **What fails if the concept is left outside Core?**  
   Convenience is not enough. The question is whether meaning is lost or materially distorted.

7. **What adversarial case has been tested?**  
   Where relevant, test collective authority, private ordering, AI delegation, institutional representation and conflicting Profile Expressions.

If those questions cannot yet be answered, the proposal may belong in a companion document, implementation profile or research note rather than in Core.

---

## Terminology

Please use v0.2 terminology precisely.

Preferred Core terms include:

- Participant;
- Source;
- Standing;
- Presentation;
- Profile Expression;
- Evidence;
- Authority;
- Consent;
- Reliance;
- Action;
- Attribution;
- Obligation;
- Revocation;
- Technical Capability, where the distinction from semantic Authority matters.

Avoid treating `identity`, `account`, `credential holder`, `agent`, `actor`, `principal`, `user`, `member`, `office` or `representative` as interchangeable unless the domain actually warrants it.

Do not use `Status` as a current Core object.

Do not use `Capacity` as a universal Core primitive. Domain-specific legal or institutional capacity may still be relevant, but it should be expressed without silently restoring the retired universal object.

Do not reintroduce older `Lex/Profile` terminology. v0.2 uses **Profile Expression**.

---

## Before a major contribution

For any proposed normative change, new primitive, new conformance rule or significant architectural interpretation, please open an issue or equivalent design discussion before submitting a pull request.

A useful proposal should state:

- the problem or semantic gap;
- the affected architecture section or repository artefact;
- whether the contribution is normative, explanatory, conformance-related, implementation-specific or experimental;
- evidence or worked encounters supporting the change;
- known counterexamples or tensions;
- whether the proposal changes Core or only an implementation/companion layer;
- any migration impact on existing material.

Small editorial corrections that do not change meaning may be submitted directly by pull request.

---

## Reference code and implementation profiles

Reference validators, adapters and implementation profiles are useful learning instruments, but they remain downstream of the semantic architecture unless expressly promoted through a later specification process.

In particular:

- operational `ALLOW` / `DENY` decisions are not SILT Core semantic evaluation outcomes;
- SILT Core outcomes are `SATISFIED`, `NOT_SATISFIED` and `INDETERMINATE`;
- an implementation may map semantic evaluation into a downstream execution decision, but that mapping should be explicit;
- successful execution does not prove semantic Authority;
- implementation schemas should not be treated as universal Core object models merely because a validator uses them.

---

## Adjacent standards

When contributing an interoperability or standards mapping, please identify the layer occupied by the adjacent system.

Useful questions include:

- does it carry or evidence a SILT semantic relation;
- does it handle identifier or credential transport;
- does it manage cryptographic continuity;
- does it provide technical delegation or dynamic authorisation;
- does it execute a downstream decision;
- does it overlap with SILT semantics;
- does it risk collapsing Source-grounded meaning into technical verification or system-issued authority?

The purpose of comparison is not to claim that every adjacent system is either a competitor or an implementation of SILT.

---

## Governance, licensing and IPR

Please also read [`GOVERNANCE.md`](./GOVERNANCE.md) and [`LICENSING.md`](./LICENSING.md).

For the v0.2 release, the repository licensing boundary is defined as **CC BY 4.0** for the canonical specification and human-readable documentation, and **Apache License 2.0** for reference code and implementation-oriented machine-readable artefacts. `LICENSING.md` records the applicable classification, including treatment of mixed implementation profiles, conformance material and historical versions.

The broader Governance & IPR framework is not yet fully adopted. In particular, contributor terms, patent and standards-essential IPR commitments, trademark and certification policy, and longer-term stewardship arrangements remain to be made explicit.

Until those broader arrangements are adopted:

- contributors should rely only on the licences and notices expressly applicable to the material they contribute to;
- repository participation should not be interpreted as granting rights beyond those expressly provided by the applicable licence or contribution terms;
- contribution does not by itself confer SILT trademark rights, certification rights, endorsement, stewardship authority or commercial exclusivity;
- no broader patent, certification or standards-body commitment should be inferred from participation alone.

Nothing in this contribution guide should be read as overriding the terms of the repository’s applicable licence or the licensing boundary stated in `LICENSING.md`.

---

## Governing principle

The aim is not to make SILT describe everything.

The aim is to preserve the distinctions that must survive an encounter between different orders.

> **Source → Standing → Presentation → evaluation at the encounter**
>
> **semantic hand-off, not semantic surrender**
