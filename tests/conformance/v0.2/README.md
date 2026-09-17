# SILT Core v0.2 conformance material

This directory contains companion conformance and falsification material for **SILT Core v0.2**.

It does **not** define a second specification, a universal SILT serialisation, a wire format, or a mandatory implementation stack. The controlling semantic reference is:

[`spec/v0.2/semantic-architecture.md`](../../../spec/v0.2/semantic-architecture.md)

The architectural seam remains:

> **Source → Standing → Presentation → evaluation at the encounter**

The purpose of this material is narrower: to test whether worked encounters, fixtures, adapters and implementations preserve the semantic distinctions required by the canonical architecture when SILT is applied across different kinds of encounter.

## Status

The material under this path is **companion test material**. It is non-normative except where it reproduces or points directly to requirements already established by the canonical semantic architecture.

An implementation does not conform merely because it serialises data in the same shape as a fixture. Conversely, an implementation may use a different technical representation and still preserve the v0.2 semantic discipline.

## What conformance means here

The tests are concerned with semantic preservation rather than protocol uniformity. In particular, an implementation should not:

- manufacture Standing, Authority, Consent, Obligation or another relation from identity, credential possession, account state or technical capability alone;
- collapse Evidence into the relation evidenced;
- treat Technical Capability as Authority;
- treat cryptographic continuity as semantic continuity;
- treat a Profile Expression as a complete representation of the originating legal, customary, cultural, relational, contractual, institutional or other normative substrate;
- silently merge, rank or privilege multiple Profile Expressions without an expressed composition rule;
- elevate a bounded evaluation result into universal Binding, liability, enforceability or compulsory acceptance; or
- force semantic content into Core where deliberate non-expression is the faithful result.

The complementary misuse cases live at [`tests/misuse-cases/`](../../misuse-cases/README.md).

## Evaluation outcomes

Where an expressed condition is evaluated under a Profile Expression, SILT Core v0.2 uses exactly three semantic outcomes:

- `SATISFIED`
- `NOT_SATISFIED`
- `INDETERMINATE`

`INDETERMINATE` must not be collapsed into a negative result.

Deliberate non-expression is distinct from those outcomes. It is not a fourth evaluation result.

Results remain linked to the Profile Expression under which they were produced. SILT Core does not supply a universal rule for merging, ranking or resolving multiple Profile Expressions.

## Fixture and schema boundary

Any JSON fixtures or JSON Schema placed under this directory are **test notation only**.

They may provide a common machine-readable form for running and comparing conformance scenarios, but they are not:

- normative schemas for SILT Core objects;
- a universal SILT object model;
- a prescribed interchange or wire format;
- a replacement for the semantic architecture; or
- evidence that every SILT relation or encounter condition must be machine-evaluable.

Implementations may translate the same semantic encounter into other data models, protocols or execution environments so long as the relevant v0.2 distinctions are preserved.

## Worked encounters

Worked encounters in this tree are falsification devices rather than templates for universal legal or institutional treatment. Their role is to expose architectural failure under different conditions — including private ordering, institutional authority, plural or collective authority, and recursive AI delegation — without making any one encounter type the default ontology of SILT.

A worked encounter should therefore distinguish clearly between:

- what is asserted or presented by the Participant;
- the Source-grounded Standing or other relation being projected;
- the applicable Profile Expression or Profile Expressions;
- Evidence supporting the Presentation;
- the semantic evaluation result or results;
- any downstream operational mapping; and
- any downstream Binding or other effect supplied by the relevant normative order rather than by SILT Core itself.

## Implementation boundary

Authentication, key management, capability tokens, sessions, dynamic authorisation, runtime policy and execution machinery remain below the Presentation line architecturally unless a future semantic reason justifies revisiting that boundary.

Accordingly, a downstream system may map SILT semantic results into operational decisions such as `ALLOW`, `DENY`, execution, refusal or escalation. Those operational decisions are not SILT Core evaluation outcomes and must not be conflated with them.

The governing discipline remains:

> **semantically thick, operationally thin**
