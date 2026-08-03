# AUT CISRC Validation Logic

**Status:** Draft
**Profile:** AUT CISRC Implementation Profile
**Relationship to SILT Core:** Non-normative implementation example

## Purpose

This document describes the lightweight validation pathway for the AUT CISRC implementation profile.

The validator checks whether an access request is valid against a delegation artefact and any applicable revocation event.

This document does not alter SILT Core v0.1.

## Validator Inputs

The Phase 2 prototype should accept:

* delegation artefact;
* access request;
* revocation log or revocation event;
* authority-chain information.

The validator does not connect to live AUT systems. It operates on portable JSON artefacts and returns a deterministic validation result.

## Validator Output

The validator should return one of two primary results:

```text
ALLOW
```

or

```text
DENY
```

with a reason code.

Example output:

```json
{
  "result": "DENY",
  "reasonCode": "DELEGATION_EXPIRED",
  "reason": "The requested action occurred after the delegation expiry date.",
  "validatedAt": "2026-08-15T10:00:00Z",
  "validatorVersion": "aut-cisrc-profile-v0.1"
}
```

## Validation Steps

The validator should perform the following checks:

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

## Initial Reason Codes

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

## Reason Code Meanings

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

## Allow Logic

The validator should return `ALLOW` where all of the following are true:

* the delegation artefact is structurally valid;
* the access request is structurally valid;
* the authority chain is present;
* the issuer is authorised to issue the delegation;
* the request actor matches the delegate;
* the requested action is included in the permitted actions;
* the requested resource is within the delegated scope;
* the requested purpose is within the delegated scope;
* the request timestamp is on or after the delegation effective date;
* the request timestamp is on or before the delegation expiry date;
* no valid revocation event applies before the request timestamp.

## Deny Logic

The validator should return `DENY` where any required validation check fails.

The validator should return the first applicable denial reason or the most specific reason available.

Examples:

* if the request actor does not match the delegate, return `ACTOR_NOT_DELEGATE`;
* if the requested action is not permitted, return `ACTION_NOT_PERMITTED`;
* if the requested resource is outside scope, return `RESOURCE_OUT_OF_SCOPE`;
* if the requested purpose is outside scope, return `PURPOSE_OUT_OF_SCOPE`;
* if the request occurs before the delegation effective date, return `DELEGATION_NOT_YET_ACTIVE`;
* if the request occurs after the delegation expiry date, return `DELEGATION_EXPIRED`;
* if the delegation has been revoked before the request timestamp, return `DELEGATION_REVOKED`;
* if the revocation was issued by an actor without recognised authority, return `REVOCATION_AUTHORITY_INVALID`.

## Revocation Logic

For this implementation profile, a revocation event is valid where the revoking actor is:

* the original delegator;
* a higher-order authority in the relevant authority chain;
* an authorised committee, agency, or subunit with delegated authority over the relevant governance domain.

A higher-order authority may revoke authority delegated at a lower level where it has standing over the relevant governance domain, resource, action, or role.

The validator should deny future requests where a valid revocation event applies before the request timestamp.

## Revocation Timing

For Phase 2, revocation affects future validation requests from the effective revocation timestamp.

Pending-action treatment is out of scope.

The validator does not attempt to reverse actions that were already validly completed before revocation.

## Evidence Handling

Authority resolves to an evidential chain based on documents.

Evidence documents may include:

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

For the Phase 2 lightweight prototype, evidence documents are treated as referenced metadata.

The validator may return a warning where evidence references are missing, but evidence verification is not required.

In non-strict mode, missing evidence may produce a warning.

In strict mode, missing evidence may produce:

```text
EVIDENCE_CHAIN_MISSING
```

## Out of Scope

This validation logic does not model:

* production AUT access systems;
* IAM replacement;
* KYC;
* behavioural monitoring;
* profile-based risk scoring;
* appeal or review processes;
* full committee structures;
* live integration with AUT systems;
* legal validity assessment of source documents.

The validator tests one narrow question:

> Is this requested action valid under the delegated authority artefact at the time of request?
