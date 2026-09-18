# Candidate SILT Core v0.2 Findings

**Status:** Historical v0.1 implementation learning record  
**Source:** AUT CISRC Implementation Profile  
**Relationship to SILT Core:** Pre-FC1 candidate findings only; not a current v0.2 proposal surface

> **Archival notice — SILT Core v0.2 is now at Freeze Candidate 1.**
>
> This document records questions and possible directions generated from the AUT CISRC v0.1 implementation before the v0.2 architecture was settled. It is retained as a development and migration record. The candidate questions and possible directions below are **not** outstanding v0.2 requirements and must not be read as amendments to, or gaps in, the canonical v0.2 semantic architecture.
>
> The controlling v0.2 reference is [`spec/v0.2/semantic-architecture.md`](../../../spec/v0.2/semantic-architecture.md). The AUT CISRC / Vietsch implementation remains on its **v0.1 semantic basis through completion**.

## Purpose

This document records implementation findings from the AUT CISRC profile that were originally intended to inform SILT Core v0.2 development.

They are not changes to SILT Core v0.1, and they are not current changes to SILT Core v0.2 FC1.

The AUT CISRC implementation profile applies SILT Core v0.1 to one constrained university research-governance workflow. Its findings remain useful as a record of what that implementation exposed in a real delegated-authority environment.

This document should be treated as a historical learning record, not as a specification or current v0.2 design backlog.

Unless separately reopened through the post-freeze change process, the candidate questions and possible directions below remain historical.

## 1. Higher-Order Revocation

The AUT CISRC implementation demonstrates that a higher-order authority may need to revoke delegated authority at a lower level where it has standing over the relevant governance domain, resource, action, or role.

In the implementation profile, revocation may be valid where the revoking actor is:

* the original delegator;
* a higher-order authority in the relevant authority chain;
* an authorised committee, agency, or subunit with delegated authority over the relevant governance domain.

Candidate v0.2 question:

> Should SILT Core define a generic higher-order revocation rule, or should this remain implementation-profile specific?

Possible v0.2 direction:

SILT Core may need to distinguish between:

* revocation by original issuer;
* revocation by superior authority;
* revocation by delegated committee or subunit;
* invalid revocation by unrelated authority.

Potential reason code:

```text
REVOCATION_AUTHORITY_INVALID
```

## 2. Class/Object Authority Nodes

The AUT CISRC implementation suggests that authority nodes may need both a class and object structure.

A **class** describes the type of authority node.

Examples:

* `StatutoryAuthority`
* `UniversityCouncil`
* `ViceChancellor`
* `Dean`
* `HeadOfSchool`
* `HeadOfDepartment`
* `Supervisor`
* `EthicsCommittee`
* `ResearchAdministrationUnit`

An **object** describes the specific instance of that class.

Examples:

* `AUT Council`
* `AUT Vice-Chancellor`
* `Faculty Dean`
* `AUT Ethics Committee`
* `Named Project Supervisor`

Candidate v0.2 question:

> Should authority nodes include explicit class/object fields in the core schema?

Possible v0.2 direction:

Authority-chain nodes may need a structure such as:

```json
{
  "authorityNodeId": "node-001",
  "class": "Supervisor",
  "object": "Named Project Supervisor",
  "level": 7,
  "parentNodeId": "node-006",
  "authorityDomain": ["research.data", "repository.submission"]
}
```

This would allow SILT Core to remain generic while supporting concrete implementations.

## 3. Evidential Authority Chains

The AUT CISRC implementation confirms that authority claims may need to resolve to documentary evidence.

Examples of supporting evidence include:

* statute or enabling legislation;
* university governance instrument;
* terms of reference;
* appointment document;
* delegation policy;
* role description;
* ethics approval;
* research access policy;
* project governance document;
* repository or dataset access rule.

Candidate v0.2 question:

> Should evidence references become mandatory for authority-chain validation, or remain optional audit metadata?

Possible v0.2 direction:

SILT Core may need a clearer evidence model, allowing each authority node or delegation relationship to reference supporting documents.

Possible fields:

```text
evidenceDocuments
authorityBasis
documentType
documentRef
documentHash
issuedBy
effectiveFrom
sourceUrl
```

For v0.2, evidence could remain metadata rather than fully verified legal proof. The validator may confirm presence, while legal or institutional validity remains outside the validator’s role.

## 4. Committee and Subunit Authority

The AUT CISRC implementation shows that authority does not always flow only through named individual roles.

Committees, agencies, and institutional subunits may also hold delegated authority within specific domains.

Examples:

* ethics committee;
* board of studies;
* research administration unit;
* data governance group;
* school or faculty committee;
* delegated project governance body.

Candidate v0.2 question:

> Should SILT Core model committee and subunit authority as first-class authority node types?

Possible v0.2 direction:

SILT Core may need to support both individual and collective authority nodes.

Possible node types:

```text
individual
role
office
committee
subunit
agency
system
```

This would help distinguish authority held by a named person from authority held by an office, committee, or institutional body.

## 5. Strict and Non-Strict Validation Modes

The implementation suggests a possible distinction between strict and non-strict validation.

For example, missing evidence references may produce a warning in non-strict mode but a denial in strict mode.

Candidate v0.2 question:

> Should SILT Core define strict and non-strict validation modes?

Possible v0.2 direction:

The validator may support modes such as:

```text
non-strict
strict
audit-only
```

In non-strict mode, missing evidence could produce a warning.

In strict mode, missing evidence could return:

```text
EVIDENCE_CHAIN_MISSING
```

This distinction may be useful where some workflows need hard enforcement while others need inspectable audit support.

## 6. Revocation Timing and Pending Actions

The AUT CISRC implementation currently treats revocation as affecting future validation requests from the revocation timestamp.

It does not model pending actions or retroactive invalidation.

Candidate v0.2 question:

> Should SILT Core define rules for pending actions, completed actions, or retroactive revocation?

Possible v0.2 direction:

SILT Core may need to distinguish between:

* future actions;
* pending actions;
* completed actions;
* actions under review;
* actions invalidated by later authority.

For now, this remains outside the AUT CISRC implementation profile.

## 7. Authority Domain Matching

The AUT CISRC implementation suggests that higher-order revocation is not only a matter of hierarchy. The revoking actor should also have standing over the relevant governance domain.

For example, an ethics committee may have authority over ethics approval, but not necessarily over every operational repository submission. A project supervisor may have authority over a research assistant’s project work, but not necessarily over university-wide data governance.

Candidate v0.2 question:

> Should SILT Core require authority-domain matching between issuer, delegation, revocation, resource, and requested action?

Possible v0.2 direction:

Authority nodes may need one or more `authorityDomain` values, such as:

```text
research.data
research.ethics
repository.submission
student.supervision
project.governance
```

The validator could then check whether the issuer or revoker has standing over the relevant domain.

## 8. Implementation Profiles as Learning Instruments

The AUT CISRC work confirms the value of implementation profiles as separate from core SILT versions.

The implementation profile can test SILT Core v0.1 without changing the core specification.

Candidate v0.2 question:

> Should SILT Core define a standard structure for future implementation profiles?

Possible v0.2 direction:

Future implementation profiles could follow a common structure:

* profile context;
* authority chain;
* core artefacts;
* validation logic;
* test cases;
* non-goals;
* candidate core findings.

This would allow SILT Core to grow through examples without turning every use case into a core rule too early.

## Summary

The AUT CISRC implementation profile does not alter SILT Core v0.1.

It provides a worked example that contributed historical implementation evidence during v0.2 development. SILT Core v0.2 FC1 is now the controlling v0.2 semantic reference; this file does not reopen the candidate questions recorded above.

Historical candidate findings included:

* higher-order revocation;
* class/object authority modelling;
* evidential authority chains;
* committee and subunit authority;
* strict and non-strict validation modes;
* revocation timing and pending-action questions;
* authority-domain matching;
* implementation profiles as structured learning instruments.

The current guiding boundary is:

> AUT CISRC remains a SILT Core v0.1 implementation through completion.  
> Its historical findings do not constitute SILT Core v0.2 semantics.