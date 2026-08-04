# AUT CISRC Authority Chain

**Status:** Draft – Phase 3 refinement
**Profile:** AUT CISRC Implementation Profile
**Relationship to SILT Core:** Non-normative implementation example

## Purpose

This document describes the authority-chain model used in the AUT CISRC implementation profile.

It supports the constrained pilot workflow for applying SILT Core v0.1 to delegated research authority in a university setting.

AUT CISRC provides the concrete pilot context. The underlying authority-chain pattern is not exclusive to AUT and is intended to be portable across registered universities and comparable research institutions.

This document does not alter SILT Core v0.1.

## Scope and Interpretation

The authority chain represents the institutional basis through which a person, role, committee, office, or agency receives authority to issue or revoke a particular research delegation.

It is a semantic representation of the authority relevant to a specific delegation. It is not intended to reproduce the complete organisational structure of a university.

The model asks:

* where does the relevant authority originate;
* through which institutional roles or bodies does it pass;
* who holds authority to issue the delegation;
* what authority may be delegated;
* within what scope and time period the authority applies;
* who may revoke the delegation;
* what evidence supports the asserted authority path.

The authority chain must be explicit and inspectable enough to support the constrained validation workflow.

## Generic University Authority Pattern

For this implementation profile, authority is modelled as a delegated institutional chain.

A generic university research authority pattern may include:

```text
Act, statute, charter, or enabling authority
→ University council, board, or governing body
→ Vice-Chancellor or delegated executive authority
→ Faculty, institute, school, committee, or research office
→ Head of department, programme, project, or operational unit
→ Supervisor, principal investigator, or project lead
→ Researcher, research assistant, or student
```

This is a semantic pattern rather than a universal organisational chart.

The particular authority chain used for a delegation may contain fewer or more nodes, depending on the university, research context, resource, and action involved.

## Institutional Variation

Different universities may:

* omit some authority levels;
* combine several functions within one office or role;
* use different institutional titles;
* place committees or agencies between authority levels;
* delegate authority directly to an office or collective body;
* assign authority over a particular research domain to a specialist body;
* distinguish academic authority from operational, ethical, data-governance, or administrative authority.

These variations do not require the SILT Core semantic model to reproduce every institutional governance arrangement.

The relevant implementation profile or authority-chain instance should identify only the authority nodes necessary to establish the basis for the particular delegation being evaluated.

The validator does not require every institution to use an identical hierarchy. It requires the asserted authority path to be explicit, internally coherent, inspectable, and supported within the implementation context.

## Mediating Committees and Agencies

Committees, agencies, offices, and institutional subunits may act as mediating authority nodes where they hold delegated standing over a particular governance domain.

Examples may include:

* research ethics committees;
* data-governance committees;
* research administration offices;
* faculty or school committees;
* repository governance bodies;
* project steering groups;
* research centres or institutes;
* external or statutory research agencies.

A mediating body may:

* receive authority from a higher institutional source;
* define or constrain the scope of a research activity;
* approve a particular use of data or infrastructure;
* authorise a role-holder to issue a limited delegation;
* retain authority to suspend or revoke that delegation.

The inclusion of a committee, office, or agency as an authority node depends on the specific institutional context. Its inclusion does not create a new SILT Core primitive.

## Authority-Chain Nodes

An authority-chain node represents a relevant source, role, office, committee, agency, or institutional body within the asserted delegation path.

A node may identify:

* the authority source or body;
* the institutional role or capacity involved;
* the authority received;
* the authority passed to the next node;
* the scope or limitations applying to that authority;
* any supporting policy, appointment, resolution, mandate, or evidence reference.

The profile does not require every node to possess the same kind of evidence. Evidence may vary according to institutional practice and the type of authority being represented.

The chain should contain enough information to determine whether the delegator holds authority over the action, resource, purpose, and duration described in the delegation artefact.

## Pilot Workflow Application

The constrained AUT CISRC pilot applies the authority-chain model to one research-delegation workflow:

```text
Institutional research authority
→ Supervisor or project lead
→ Limited delegation to a researcher, research assistant, or student
→ Time-bound request involving a defined research resource
→ Validation of scope, duration, and revocation status
→ ALLOW or DENY result
```

The pilot does not claim to model the whole AUT governance structure.

It identifies only the authority relationship necessary to test whether a supervisor or project lead may issue a limited research delegation and whether a subsequent request remains within that delegation.

AUT CISRC is therefore the implementation context used to test the pattern. It does not define the architecture of every university and should not be read as formally approved AUT institutional architecture.

## Relationship to Delegation

The authority chain supports the delegation artefact by establishing the asserted basis on which the delegator acts.

The delegation artefact separately identifies:

* the delegator;
* the delegate;
* the permitted action;
* the relevant resource;
* the stated purpose;
* the effective time;
* the expiry time;
* any applicable limitations;
* the current delegation status.

The authority chain does not itself grant application access or allocate a resource. It provides a portable representation of the authority basis relevant to evaluating the delegation.

## Relationship to Revocation

Revocation authority may arise from:

* the original delegator;
* a superior authority within the same institutional chain;
* a committee, office, or agency holding relevant revocation authority;
* another authority expressly identified by the implementation context.

A revocation event must identify the basis on which the revoking actor or body acts.

The validator may evaluate whether the asserted revocation authority is consistent with the authority chain and the implementation-profile rules.

The model does not attempt to determine every legal or institutional question concerning revocation. It supports the constrained determination required by the pilot workflow.

## Relationship to Validation

Within this implementation profile, the validator may use the authority chain to evaluate whether:

* an authority chain is present;
* the delegator is represented within the relevant chain;
* the delegator holds authority over the stated action or resource;
* the delegation remains within the authority passed to the delegator;
* a revocation was issued by an actor or body with an asserted authority basis.

The authority-chain check forms one part of the wider validation path.

The validator must also evaluate:

* whether the requesting actor matches the delegate;
* whether the requested action is permitted;
* whether the resource is within scope;
* whether the stated purpose is within scope;
* whether the delegation is active;
* whether the delegation has expired;
* whether the delegation has been revoked.

The result remains a deterministic `ALLOW` or `DENY` decision for the constrained pilot request.

## Portability

The authority-chain pattern may be applied across different universities without requiring a universal university hierarchy.

Each implementation may describe its own relevant:

* governing bodies;
* executive authorities;
* faculties and schools;
* research offices;
* committees and agencies;
* project leadership roles;
* delegated research roles.

Portability arises from representing these relationships through a common semantic pattern, while allowing the particular institutional nodes and evidence references to vary.

The portable element is the structure of the authority claim, delegation, request, expiry, revocation, and validation process. The institutional content remains specific to the participating university or research environment.

## Non-Goals

This authority-chain model does not:

* define an official AUT governance architecture;
* prescribe a universal structure for universities;
* replace institutional policies or delegations;
* authenticate the identity of an actor;
* perform KYC or identity proofing;
* allocate application permissions or resources;
* replace an IAM or access-control system;
* monitor user behaviour;
* determine general legal or regulatory compliance;
* model every institutional committee or administrative process;
* modify SILT Core v0.1.

## Status

This document remains a non-normative implementation-profile artefact.

It records the authority-chain pattern used to support the AUT CISRC pilot and clarifies how the same pattern may accommodate institutional variation across other universities and research institutions.

Any finding that may require a future change to the SILT Core semantic model should be recorded separately as a candidate v0.2 finding. It should not be incorporated directly into SILT Core v0.1 through this implementation profile.
