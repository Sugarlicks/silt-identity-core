# SILT Core — Consent Validator

> [!WARNING]
> **Historical SILT Core v0.1 reference implementation.**
>
> This validator implements the v0.1 Consent model and is retained for historical, migration and research reference. It is **not** a SILT Core v0.2 validator and must not be used as evidence of v0.2 conformance.
>
> In SILT Core v0.2:
> - `Principal` is not a Core object;
> - there is no universal `Capacity` primitive;
> - Consent, Authority and Revocation remain semantically relevant, but the fixed artefact shapes and validation rules encoded here are not normative v0.2 representations;
> - the controlling semantic reference is [`spec/v0.2/semantic-architecture.md`](../../../spec/v0.2/semantic-architecture.md), centred on **Source → Standing → Presentation → evaluation at the encounter**.
>
> Do not mechanically translate this validator into a v0.2 wire schema. SILT Core v0.2 does not define a universal Consent artefact or universal executable policy for Consent.
>
> The separate `reference/validators/aut-cisrc-delegation/` tree is the AUT CISRC / Vietsch v0.1 implementation and is unaffected by this archival notice.

## Historical v0.1 description

This is an experimental reference validator for SILT Core consent artefacts.

It demonstrates how SILT Core primitives — capacity, authority, consent, scope, and revocation — can be expressed as executable validation logic.

## Status

The validator is experimental and non-normative. It does not constrain future SILT Core v2 schema design.

## What it validates

The validator performs two layers of validation:

1. Schema validation using JSON Schema Draft 2020-12
2. Semantic validation based on SILT Core design axioms

Semantic checks include:

- capacity must be declared
- authority source must be explicit and referenced
- delegated capacity should be temporally bounded
- self-authority must not be silently forwarded
- delegated authority requires a termination rule
- scope must be bounded
- purpose must be specific
- revocation must be first-class

## Repository position

This validator lives under:

/reference/validators/consent

This signals that it is a reference artefact, not the normative core specification.

It provides a bridge from SILT Core v0.1 toward executable semantics.
