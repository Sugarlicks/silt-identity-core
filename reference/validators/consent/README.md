# SILT Core — Consent Validator

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
