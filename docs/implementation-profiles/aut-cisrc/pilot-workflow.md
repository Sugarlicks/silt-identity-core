# AUT CISRC Pilot Workflow

**Status:** Draft
**Profile:** AUT CISRC Implementation Profile
**Relationship to SILT Core:** Non-normative implementation example

## Purpose

This document describes the constrained pilot workflow used for the AUT CISRC implementation profile.

The workflow applies SILT Core v0.1 delegation and revocation concepts to one university research-governance scenario.

This document does not alter SILT Core v0.1.

## Pilot Scenario

A supervisor or project lead delegates limited authority to a research assistant or student to access, submit, or interact with a restricted research dataset or repository item for a defined project, purpose, action, and time period.

The delegate then makes a request.

The SILT Core validator checks the request against:

* authority chain;
* actor match;
* permitted action;
* resource;
* purpose;
* effective date;
* expiry;
* revocation status.

The validator returns:

```text
ALLOW
```

or

```text
DENY
```

with a reason code.

## Workflow Steps

1. An authorised role-holder issues a delegation.
2. The delegation defines the delegate, resource, action, purpose, effective date, and expiry.
3. The delegate submits an access or repository request.
4. The validator checks the request against the delegation artefact.
5. The validator checks whether the delegation has expired.
6. The validator checks whether the delegation has been revoked.
7. The validator returns an allow/deny result with a reason code.

## Example Delegation

```text
Issuer: Project Supervisor
Delegate: Research Assistant
Resource: Dataset123
Permitted Action: dataset.submit
Purpose: ProjectX research submission
Effective From: 2026-08-01
Expires At: 2026-09-30
```

## Example Request

```text
Actor: Research Assistant
Action: dataset.submit
Resource: Dataset123
Purpose: ProjectX research submission
Timestamp: 2026-08-15
```

## Expected Result

```text
ALLOW
```

The request is allowed because the actor, action, resource, purpose, and timestamp match the delegation and no revocation event applies.

## Denial Examples

The same validator should return `DENY` where the request falls outside the delegated authority.

Examples include:

* the request actor does not match the delegate;
* the requested action is not permitted;
* the requested resource is outside scope;
* the requested purpose is outside scope;
* the delegation is not yet active;
* the delegation has expired;
* the delegation has been revoked;
* the revocation was issued by an actor without recognised revocation authority;
* the authority chain is missing or invalid.

## Out of Scope

This pilot workflow does not model:

* production AUT access systems;
* IAM replacement;
* KYC;
* behavioural monitoring;
* appeal or review processes;
* full committee structures;
* the university funding chain;
* live system integration.

The workflow is deliberately narrow so the validator can test one thing clearly: whether a delegated authority claim can be expressed, checked, expired, and revoked.
