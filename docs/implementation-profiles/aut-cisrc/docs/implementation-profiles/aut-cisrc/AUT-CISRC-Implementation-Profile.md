# SILT Core v0.1 AUT CISRC Implementation Profile

**Status:** Draft v0.1
**Profile type:** Non-normative implementation profile
**Project:** SILT Core – Delegation and Revocation Semantics for Federated Research Infrastructure
**Pilot context:** AUT Computer and Information Sciences Research Centre (CISRC)
**Prepared by:** Gareth Farry
**Repository path:** `/docs/implementation-profiles/aut-cisrc/AUT-CISRC-Implementation-Profile.md`

---

## 1. Purpose

This implementation profile demonstrates how **SILT Core v0.1** can be applied to a constrained university research-governance workflow.

The profile supports the Vietsch-funded SILT Core project by providing a concrete pilot context for:

* delegation and revocation modelling;
* authority-chain representation;
* JSON schema development;
* validator logic;
* pilot test cases;
* implementation findings that may later inform SILT Core v0.2.

This profile does **not** alter the SILT Core v0.1 specification. It is a worked implementation example.

---

## 2. Relationship to SILT Core v0.1

SILT Core v0.1 remains the stable core model.

This AUT CISRC profile applies the v0.1 concepts of:

* delegated authority;
* scope;
* permitted action;
* temporal validity;
* expiry;
* revocation;
* validation result.

The profile provides one research-institution implementation context. Lessons from this profile may be recorded as candidate inputs for SILT Core v0.2, but they do not automatically become part of the core specification.

In short:

> SILT Core is generic.
> AUT CISRC is one implementation example.
> Candidate v0.2 findings are recorded separately.

---

## 3. Implementation Status

This profile is based on:

* AUT CISRC pilot modelling artefacts;
* semantic architecture and UML diagrams;
* clarification received from AUT on authority hierarchy, delegation, and revocation;
* the Phase 2 delivery plan for schema, validator, and pilot execution.

The implementation profile is intended to guide the next deliverables:

* JSON schema v0;
* lightweight validator prototype;
* example delegation and revocation artefacts;
* AUT CISRC pilot test pack;
* light AUT review.

---

## 4. Scope

### 4.1 In Scope

This profile covers one constrained research-governance workflow:

> A supervisor or project lead delegates limited authority to a research assistant or student to access, submit, or interact with a restricted research dataset or repository item for a defined project, purpose, action, and time period. The delegate then makes a request, and the SILT Core validator checks authority chain, actor match, action, resource, purpose, expiry, and revocation status before returning ALLOW or DENY.

The profile includes:

* an institutional authority-chain model;
* a delegation artefact model;
* a revocation event model;
* an access request model;
* a validation result model;
* validator logic;
* test cases.

### 4.2 Out of Scope

This profile does not attempt to model or build:

* a general IAM system;
* KYC;
* three-factor authentication;
* behavioural monitoring;
* profile-based risk scoring;
* a legal compliance engine;
* an ethicality conformance engine;
* a production access-control system;
* the university funding chain;
* the full structure of university committees and subunits;
* appeal or review processes;
* live integration with AUT systems.

Appeal and review processes may exist institutionally, but they are outside this Phase 2 validator scope.

---

## 5. AUT CISRC Pilot Context

The AUT CISRC pilot context is a university research-governance workflow involving delegated authority over restricted research access.

The pilot tests whether delegated authority can be represented as a portable, inspectable artefact and evaluated independently at the point of request.

The workflow is deliberately narrow:

1. An authorised role-holder issues a delegation.
2. The delegation defines delegate, scope, resource, permitted action, purpose, effective date, and expiry.
3. The delegate makes an access or submission request.
4. The validator evaluates the request against the delegation artefact and any revocation record.
5. The validator returns an allow/deny result with a reason code.

The pilot is not intended to replace existing university systems. It tests whether delegated authority can be expressed and validated semantically.

---

## 6. Authority Chain Model

For this implementation profile, authority is modelled as a delegated institutional chain.

The simplified New Zealand university authority chain is:

```text
Act / Statute
→ University Board / Council
→ Vice-Chancellor
→ Dean
→ Head of School
→ Head of Department
→ Role Leader / Supervisor / Project Lead
→ Student / Research Assistant
```

This hierarchy is used as the pilot authority context. It concerns delegated institutional authority, not budgetary or funding authority.

### 6.1 Higher-Order Revocation

A higher-order authority may revoke authority delegated at a lower level where the higher-order authority has standing over the relevant governance domain, resource, action, or role.

For this implementation profile, revocation is valid where the revoking actor is:

* the original delegator; or
* a higher-order authority in the relevant authority chain; or
* an authorised committee, agency, or subunit with delegated authority over the relevant governance domain.

### 6.2 Committees, Agencies, and Subunits

Authority may also be held by committees, agencies, or institutional subunits operating within a particular layer of the hierarchy.

Examples may include:

* ethics committee;
* board of studies;
* research administration unit;
* data governance group;
* school or faculty committee;
* delegated project governance body.

These entities are treated as authority nodes where they hold delegated standing over a relevant governance domain.

### 6.3 Class/Object Framing

For implementation purposes, authority nodes may be represented using a class/object model.

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

This allows the authority chain to remain generic while still supporting concrete implementation examples.

---

## 7. Evidential Authority Chain

Authority resolves to an evidential chain based on documents.

This implementation profile therefore allows each authority node or delegation relationship to reference supporting evidence.

Examples of supporting evidence may include:

* statute or enabling legislation;
* university charter or governance instrument;
* terms of reference;
* appointment document;
* delegation policy;
* role description;
* ethics approval;
* research access policy;
* project governance document;
* repository or dataset access rule.

For Phase 2, evidence references are treated as audit metadata. The validator may check whether an evidence reference is present, but it does not need to verify the legal validity of each source document.

Document verification may be considered in future versions.

---

## 8. Core Artefacts

This implementation profile uses five core artefacts.

### 8.1 Authority Chain

The authority chain describes the institutional path through which authority is held, delegated, or revoked.

Minimum fields:

```text
authorityChainId
authorityNodes
rootAuthority
governanceDomain
evidenceDocuments
```

Each authority node may include:

```text
authorityNodeId
class
object
level
parentNodeId
authorityDomain
evidenceDocuments
```

### 8.2 Delegation Artefact

The delegation artefact records a specific grant of authority from one actor to another.

Minimum fields:

```text
delegationId
issuer
delegate
authorityChain
scope
resource
permittedActions
purpose
effectiveFrom
expiresAt
status
issuedAt
proof
evidenceDocuments
```

### 8.3 Revocation Event

The revocation event records the withdrawal of a delegation.

Minimum fields:

```text
revocationId
delegationId
revokedBy
revocationAuthorityBasis
revokedAt
reason
effect
evidenceDocuments
```

### 8.4 Access Request

The access request records the action attempted by the delegate.

Minimum fields:

```text
requestId
actor
action
resource
purpose
timestamp
delegationId
```

### 8.5 Validation Result

The validation result records the outcome of validator evaluation.

Minimum fields:

```text
requestId
delegationId
result
reasonCode
reason
validatedAt
validatorVersion
warnings
```

---

## 9. Validation Logic

The validator evaluates whether a request is permitted under a delegation artefact and any applicable revocation record.

The validator should return a deterministic result:

```text
ALLOW
```

or

```text
DENY
```

with a reason code.

### 9.1 Validation Steps

The Phase 2 validator should perform the following checks:

1. Check required artefacts are present.
2. Check delegation object is structurally valid.
3. Check access request object is structurally valid.
4. Check authority chain is present.
5. Check issuer has authority to issue the delegation.
6. Check request actor matches the delegate.
7. Check requested action is permitted.
8. Check requested resource is within scope.
9. Check requested purpose is within scope.
10. Check request timestamp is not before the delegation effective date.
11. Check request timestamp is not after the delegation expiry date.
12. Check whether the delegation has been revoked.
13. If revoked, check whether the revoking authority is valid.
14. Return ALLOW or DENY with reason code.

### 9.2 Revocation Timing

For Phase 2, revocation affects future validation requests from the effective revocation timestamp.

Pending-action treatment is out of scope for this implementation profile.

### 9.3 Evidence Handling

For Phase 2, evidence documents are treated as referenced metadata.

The validator may return a warning where evidence references are missing, but evidence verification is not required for the lightweight prototype.

---

## 10. Reason Codes

Initial reason codes:

```text
ALLOW
SCHEMA_INVALID
AUTHORITY_CHAIN_MISSING
ISSUER_NOT_AUTHORISED
ACTOR_NOT_DELEGATE
ACTION_NOT_PERMITTED
RESOURCE_OUT_OF_SCOPE
PURPOSE_OUT_OF_SCOPE
DELEGATION_NOT_YET_ACTIVE
DELEGATION_EXPIRED
DELEGATION_REVOKED
REVOCATION_AUTHORITY_INVALID
EVIDENCE_CHAIN_MISSING
```

### 10.1 Reason Code Meanings

| Reason Code                    | Result         | Meaning                                                                                                      |
| ------------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------ |
| `ALLOW`                        | ALLOW          | The delegation is valid for the requested action.                                                            |
| `SCHEMA_INVALID`               | DENY           | One or more required artefacts are structurally invalid.                                                     |
| `AUTHORITY_CHAIN_MISSING`      | DENY           | No authority chain is available for validation.                                                              |
| `ISSUER_NOT_AUTHORISED`        | DENY           | The issuer does not hold authority over the relevant resource, action, purpose, or delegate.                 |
| `ACTOR_NOT_DELEGATE`           | DENY           | The request actor does not match the named delegate.                                                         |
| `ACTION_NOT_PERMITTED`         | DENY           | The requested action is not permitted by the delegation.                                                     |
| `RESOURCE_OUT_OF_SCOPE`        | DENY           | The requested resource is outside the delegated scope.                                                       |
| `PURPOSE_OUT_OF_SCOPE`         | DENY           | The requested purpose is outside the delegated scope.                                                        |
| `DELEGATION_NOT_YET_ACTIVE`    | DENY           | The request occurs before the delegation effective date.                                                     |
| `DELEGATION_EXPIRED`           | DENY           | The request occurs after the delegation expiry date.                                                         |
| `DELEGATION_REVOKED`           | DENY           | The delegation has been revoked before the request timestamp.                                                |
| `REVOCATION_AUTHORITY_INVALID` | DENY           | The revocation event was issued by an actor without recognised revocation authority.                         |
| `EVIDENCE_CHAIN_MISSING`       | WARNING / DENY | Evidence references are missing. For Phase 2 this may be treated as a warning unless strict mode is enabled. |

---

## 11. Pilot Workflow

### 11.1 Scenario

A project supervisor delegates limited authority to a research assistant to submit a restricted dataset record to a research repository.

The delegation is limited by:

* delegate;
* resource;
* permitted action;
* project;
* purpose;
* effective date;
* expiry date.

The research assistant submits an access request.

The SILT Core validator checks whether the request falls within the delegated authority.

### 11.2 Example Delegation

```text
Issuer: Project Supervisor
Delegate: Research Assistant
Resource: Dataset123
Permitted Action: dataset.submit
Purpose: ProjectX research submission
Effective From: 2026-08-01
Expires At: 2026-09-30
```

### 11.3 Example Request

```text
Actor: Research Assistant
Action: dataset.submit
Resource: Dataset123
Purpose: ProjectX research submission
Timestamp: 2026-08-15
```

### 11.4 Expected Result

```text
ALLOW
```

The request is allowed because the actor, action, resource, purpose, and timestamp match the delegation and no revocation event applies.

---

## 12. Test Cases

The Phase 2 pilot test pack should include the following cases.

| Test | Scenario                                  | Expected Result                                          |
| ---- | ----------------------------------------- | -------------------------------------------------------- |
| 1    | Valid delegation                          | ALLOW                                                    |
| 2    | Expired delegation                        | DENY: `DELEGATION_EXPIRED`                               |
| 3    | Revoked delegation                        | DENY: `DELEGATION_REVOKED`                               |
| 4    | Wrong delegate                            | DENY: `ACTOR_NOT_DELEGATE`                               |
| 5    | Action outside permitted scope            | DENY: `ACTION_NOT_PERMITTED`                             |
| 6    | Resource mismatch                         | DENY: `RESOURCE_OUT_OF_SCOPE`                            |
| 7    | Purpose mismatch                          | DENY: `PURPOSE_OUT_OF_SCOPE`                             |
| 8    | Missing authority chain                   | DENY: `AUTHORITY_CHAIN_MISSING`                          |
| 9    | Invalid revoker                           | DENY: `REVOCATION_AUTHORITY_INVALID`                     |
| 10   | Higher authority revokes lower delegation | DENY future request: `DELEGATION_REVOKED`                |
| 11   | Missing evidence chain                    | WARNING or DENY in strict mode: `EVIDENCE_CHAIN_MISSING` |

---

## 13. Implementation Files

This profile should be implemented through the following repository files.

```text
/docs/implementation-profiles/aut-cisrc/
  README.md
  AUT-CISRC-Implementation-Profile.md
  authority-chain.md
  pilot-workflow.md
  candidate-v0.2-findings.md
  diagrams/

/schemas/
  authority-chain.schema.json
  delegation.schema.json
  revocation.schema.json
  access-request.schema.json
  validation-result.schema.json

/validator/
  validate.py
  README.md

/examples/aut-cisrc-research-delegation/
  README.md
  test-cases.md
  delegations/
  requests/
  revocations/
  expected-results/
```

---

## 14. Candidate v0.2 Findings

The following findings from the AUT CISRC implementation profile should be recorded for possible SILT Core v0.2 consideration.

These are not changes to v0.1.

### 14.1 Higher-Order Revocation

The implementation demonstrates the importance of modelling revocation by higher-order authorities within a delegated hierarchy.

Candidate v0.2 question:

> Should SILT Core define a generic higher-order revocation rule, or should this remain implementation-profile specific?

### 14.2 Class/Object Authority Nodes

The implementation suggests that authority nodes may need both a class and object structure.

Candidate v0.2 question:

> Should authority nodes include explicit class/object fields in the core schema?

### 14.3 Evidential Authority Chains

The implementation confirms that authority claims resolve to documentary evidence.

Candidate v0.2 question:

> Should evidence references become mandatory for authority-chain validation, or remain optional audit metadata?

### 14.4 Committee and Subunit Authority

The implementation shows that authority does not always flow only through named individual roles. Committees and subunits may also hold delegated authority within specific domains.

Candidate v0.2 question:

> Should SILT Core model committee/subunit authority as a first-class authority node type?

---

## 15. Licensing and Publication

This implementation profile is intended for public release as part of the SILT Core Vietsch project deliverables.

Suggested licensing:

* documentation and profile material: Creative Commons Attribution 4.0 International;
* source code and validator prototype: Apache 2.0.

AUT CISRC materials should be clearly marked as pilot modelling inputs and non-normative implementation artefacts.

---

## 16. Summary

This profile demonstrates how SILT Core v0.1 can be applied to one constrained university research-governance workflow.

It tests whether delegated authority can be represented as a portable artefact, evaluated at the point of action, and revoked deterministically.

The implementation is intentionally narrow.

It does not model the whole university.
It does not replace IAM.
It does not build a compliance engine.
It does not alter SILT Core v0.1.

It shows one thing clearly:

> A delegated authority claim can be expressed, checked, expired, and revoked through a portable semantic artefact.
