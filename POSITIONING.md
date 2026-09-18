# SILT Positioning

SILT Core defines a semantic layer for encounters between participants operating under different legal, cultural, customary, private, institutional or technical orders.

Its purpose is not to make those orders identical. It is to let the minimum relevant conditions of an encounter become mutually legible without requiring the originating order to surrender its own source of authority or collapse into the ontology of the receiving system.

The canonical v0.2 seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

## What SILT contributes

Most digital systems are designed to answer questions such as:

- who controls an identifier;
- what a credential attests;
- what an account is permitted to do;
- whether a key, token or capability can cause a technical effect.

SILT asks a different class of question:

- what Source grounds the relevant relation;
- what Standing a Participant brings to this encounter;
- what minimum relevant projection is being Presented now;
- under which expressed conditions that Presentation is evaluated;
- what Authority, Consent, Reliance, Attribution, Obligation or Revocation semantics are relevant;
- what remains unresolved, contested or deliberately outside expression.

This is not a universal authority layer. Authority is one semantic relation within the wider encounter architecture.

## Profile Expression

A **Profile Expression** provides a bounded expression of the conditions under which a Presentation is evaluated in a particular encounter.

It does not capture, exhaust, modify or govern the originating legal, customary, cultural, contractual, institutional or other normative order.

Multiple Profile Expressions may coexist or conflict. SILT does not silently merge, rank or privilege them.

## Stack role

SILT is **semantically thick and operationally thin**.

It sits at the semantic boundary of an encounter rather than inside a particular identity, credential, authorisation or execution stack.

Authentication, key management, credentials, capability tokens, dynamic authorisation, policy engines and execution systems may carry Evidence, transport Presentations or implement downstream decisions. They remain separate from the semantic relations SILT represents.

The distinction is deliberate:

```text
Standing              != credential possession
Authority             != Technical Capability
Presentation          != a specific credential format
semantic continuity   != cryptographic continuity
evaluation            != compulsory acceptance
Attribution           != Binding or liability
```

Technical machinery may operate before, during or after a SILT encounter. “Below the Presentation line” is therefore an architectural boundary, not a temporal sequence.

## Encounter, not universal recognition

SILT does not certify every Source as universally valid and does not require a receiving party to accept a Presentation.

It provides a disciplined way for a Source-grounded relation to become legible at the boundary.

A receiving order may conclude that its own expressed conditions are not satisfied. That conclusion does not create, extinguish or redefine the underlying Standing.

> **Legibility does not compel recognition.**

## Relationship to adjacent standards

SILT is intended to complement infrastructure that handles identity, credentials, cryptographic continuity, technical delegation, dynamic authorisation and execution.

When assessing an adjacent standard, the relevant question is not merely whether it uses similar words. The question is which layer it occupies:

- does it carry or evidence a SILT semantic relation;
- does it execute a downstream decision;
- does it complement the SILT encounter layer;
- or does it collapse Source-grounded meaning into technical verification or system-issued authority?

SILT should not duplicate machinery that another layer already performs well.

## Boundary of claim

SILT Core does not claim to be:

- a universal identity system;
- a credential or trust-registry framework;
- a general authentication or access-control system;
- a universal authorisation engine;
- a complete model of law, custom or culture;
- a universal conflict-of-laws mechanism;
- a guarantee of legal enforceability or Binding effect.

Its claim is narrower and more durable:

> SILT provides a semantic architecture for making the minimum relevant conditions of plural encounters mutually legible without semantic surrender.

## Current release position

SILT Core v0.2 is at **Freeze Candidate 1**. The controlling semantic reference is:

[`spec/v0.2/semantic-architecture.md`](./spec/v0.2/semantic-architecture.md)

Repository reconciliation, conformance packaging and release-level licensing classification are complete. Final release packaging, release notes and archive metadata remain. These release tasks should not be used to reopen Core silently.
