# Vietsch v0.1 AUT pilot — specification provenance and conformance boundary

**Prepared:** 23 October 2026  
**Status:** Research publication provenance note; no normative specification change.

## Original v0.1 provenance

The historical **SILT Core v0.1** GitHub release was published on 14 April 2026: https://github.com/Sugarlicks/silt-identity-core/releases/tag/v0.1

Preserved original source documents within the repository:

- `archive/v0.1/spec/delegation.md` — defines explicit delegation, principal, agent, capacity, scope, duration and revocation reference.
- `archive/v0.1/spec/revocation.md` — defines revocation event, checkability, expiry, supersession and non-reliance on uncertain state.
- `archive/v0.1/schemas/delegation.schema.json` — original v0.1 delegation JSON Schema.
- `archive/v0.1/schemas/revocation.schema.json` — original v0.1 revocation JSON Schema.
- Other v0.1 historical materials are preserved under `archive/v0.1/`.

The original release predates the Vietsch MoU signed in April 2026. The funded project **applied and tested v0.1 delegation and revocation semantics** in a constrained research-infrastructure pilot; it did not originate the historic v0.1 publication. Do not claim the original v0.1 release was a Vietsch-funded release or backdate the pilot.

## AUT CISRC implementation boundary

The non-normative AUT CISRC profile defines distinct profile-specific JSON Schema shapes for authority chains, delegations, requests, revocations and validation results. In particular:

| Concept | Archived v0.1 schema | AUT implementation-profile schema |
| --- | --- | --- |
| Delegation identifier | `delegation_id` | `delegationId` |
| Authority origin | `principal.principal_id` | `issuer.actorId` plus authority-chain reference |
| Delegate | `agent.agent_id` | `delegate.actorId` |
| Scope | `scope[]` | `permittedActions[]`, resource and purpose |
| Revocation | `revocation.revocation_ref` | separate revocation log/event carrying `revokedBy` and `revocationAuthorityBasis` |

The profile schemas are **not identical to, nor directly interchangeable with, the historical v0.1 schemas**. The automated 21/21 test result validates the profile-specific semantics, fixtures and output structures, not the claim that AUT JSON fixtures conform unchanged to the archived Core schemas. The relationship is **non-normative implementation adaptation**. Formal cross-schema mapping or interoperability conformance was not tested.

## Required archival wording

Suggested archival language:

> This release records the Vietsch-supported AUT CISRC synthetic pilot applying the archived SILT Core v0.1 delegation and revocation model. It includes non-normative implementation-profile schemas, a reference validator and test evidence. The profile's data shapes are an implementation-specific adaptation and should not be represented as normative v0.1 schema conformance. The original SILT Core v0.1 specification was publicly released before the funded pilot, and the later SILT Core v0.2 architecture is out of scope.

## Release rule

Create **a separate pilot-specific tag/release** from a reviewed immutable commit rather than retagging `v0.1` or `v0.2.0`. Include a file manifest identifying original archived normative sources separately from the AUT profile material, test evidence and research report.
