# AUT CISRC Research Delegation Example

**Status:** Draft
**Profile:** AUT CISRC Implementation Profile
**Relationship to SILT Core:** Non-normative implementation example

## Purpose

This folder contains example artefacts for the AUT CISRC implementation profile.

It demonstrates how SILT Core v0.1 delegation and revocation concepts can be applied to a constrained university research-governance workflow.

This example does not modify SILT Core v0.1.

## Scenario

A supervisor or project lead delegates limited authority to a research assistant or student to access, submit, or interact with a restricted research dataset or repository item for a defined project, purpose, action, and time period.

The delegate then makes a request.

The validator checks:

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

## Folder Structure

```text
examples/aut-cisrc-research-delegation/
  README.md
  test-cases.md
  delegations/
  requests/
  revocations/
  expected-results/
```

## Artefact Types

This example uses the following artefact types:

* delegation artefact;
* access request;
* revocation event or revocation log;
* validation result.

## Non-Normative Status

This example is non-normative.

It is provided to test and demonstrate how SILT Core v0.1 can be applied in one constrained implementation profile.

Findings from this example may inform later SILT Core v0.2 consideration.
