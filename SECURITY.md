# Security Policy

SILT Core is a specification-first project defining a semantic architecture for encounters across plural legal, cultural, customary, private, institutional and technical orders.

The controlling v0.2 semantic reference is:

[`spec/v0.2/semantic-architecture.md`](./spec/v0.2/semantic-architecture.md)

Security issues may arise in two materially different ways:

1. **technical vulnerabilities** in reference code, schemas, fixtures, examples or implementation profiles;
2. **semantic or governance vulnerabilities** where an implementation or document manufactures, collapses or misstates a SILT relation in a way that could lead to unsafe reliance, execution or representation.

Both matter, but they should not be confused.

---

## Current status

### v0.1

v0.1 is released and remains the implementation basis for work that began against that architecture.

The **Vietsch / AUT CISRC research-delegation implementation remains a SILT Core v0.1 implementation to completion**. Security issues in that profile should therefore be assessed against its v0.1 implementation basis unless a later migration phase is explicitly opened.

### v0.2

SILT Core v0.2 is at **Freeze Candidate 1** and is undergoing release packaging and repository reconciliation.

Reference code, conformance fixtures and implementation profiles are non-normative unless expressly stated otherwise.

SILT Core should not be treated as a production security product or as a substitute for independent technical, legal, governance or operational review.

---

## Supported scope

Security review is welcome for:

- reference validators and adapters;
- schemas and fixtures;
- worked encounters and conformance tests;
- misuse cases;
- Source handling;
- Standing and Presentation semantics;
- Profile Expression provenance and evaluation handling;
- Authority containment and delegation lineage;
- Consent and Reliance modelling;
- Attribution and Obligation handling;
- Revocation semantics;
- semantic / cryptographic continuity boundaries;
- documentation that could create unsafe implementation assumptions;
- implementation behaviour that silently changes SILT semantic meaning.

Security review may therefore be technical, semantic, governance-related, or some combination of these.

---

## Semantic security failures

A SILT implementation can be technically correct and still be semantically unsafe.

The following classes of failure are especially relevant to v0.2.

### Technical Capability mistaken for Authority

A key, token, capability, wallet, session, account or runtime permission may allow an Action to execute.

That technical ability does not by itself establish SILT Authority.

A system that converts successful execution into a semantic Authority conclusion without the required Source, Standing, Presentation or Profile Expression basis creates a semantic security failure.

### Credential validity mistaken for Standing

A credential or verifiable presentation may be cryptographically valid while the Standing or Authority it is offered to evidence is stale, disputed, insufficient or no longer applicable.

Credential validity is not a universal substitute for Source-grounded Standing.

### Cryptographic continuity mistaken for semantic continuity

Key rotation, credential replacement, account migration or infrastructure change does not by itself terminate Standing, Authority, Attribution or Obligation.

Conversely, continued control of a key, account or credential does not prove that the underlying semantic relation remains current.

Implementations should avoid coupling semantic continuity mechanically to technical identifier or credential continuity unless an applicable Profile Expression expressly requires it.

### Profile Expression overreach

A Profile Expression is a bounded encounter-relevant expression.

It must not be treated as if it captured, exhausted, modified or governed the originating legal, customary, cultural, private, contractual or institutional order as a whole.

An implementation that silently extends a bounded expression into universal jurisdiction or ontology creates both semantic and governance risk.

### Silent aggregation or precedence

Where multiple Profile Expressions apply, SILT does not silently merge, rank or privilege them.

Results must remain linked to the Profile Expression under which they were produced unless an expressed composition rule provides otherwise.

An implementation that manufactures one aggregate result or treats one expression as universally superior without an expressed basis creates a semantic security failure.

### Attribution mistaken for Binding or liability

Attribution links an Action to a Participant, Authority context or relational position.

It does not by itself establish Binding effect, liability, enforceability or legal responsibility.

Systems should not promote an Attribution result into those downstream conclusions without an applicable external or Profile-defined rule.

### Evaluation mistaken for compulsory acceptance

A `SATISFIED` result does not mean that every receiving party or order is universally obliged to accept the Presentation.

Likewise, `NOT_SATISFIED` under one Profile Expression does not extinguish the underlying Source-grounded Standing.

### INDETERMINATE mistaken for invalidity

`INDETERMINATE` means that an expressed condition cannot be concluded from the supplied bounded material.

It is not a universal `INVALID` result.

Implementations should not silently convert uncertainty into semantic failure.

### Deliberate non-expression mistaken for failure

A condition deliberately left unexpressed because bounded expression would materially distort it remains outside SILT evaluation for that encounter.

It is not a fourth outcome and must not be coerced into `NOT_SATISFIED` or `INDETERMINATE` merely because a machine cannot evaluate it.

---

## Examples of relevant issues

Relevant reports may include:

- a validator treating possession of a capability token as proof of Authority;
- a credential-processing flow that infers current Standing solely from signature validity;
- a key-rotation event that incorrectly destroys a persistent semantic relation;
- a revoked or superseded Authority remaining executable because runtime permission still exists;
- derived Authority silently exceeding the parent delegable envelope;
- a collective participant being treated as authorised to represent the collective solely because membership or Standing is evidenced;
- a Profile Expression being treated as a complete representation of the originating order;
- results from two Profile Expressions being merged without an expressed composition rule;
- an implementation treating `INDETERMINATE` as `NOT_SATISFIED` or `INVALID`;
- a deliberately non-expressed condition being forced into an evaluation result;
- Attribution being promoted automatically into Binding, liability or legal responsibility;
- documentation implying that successful SILT evaluation proves universal legal validity;
- examples that blur normative Core semantics with downstream capability or execution machinery;
- reference code being presented as if it were the specification itself.

---

## Technical security versus semantic security

Some issues are conventional software vulnerabilities: injection, broken access control, unsafe deserialisation, signature-verification defects, dependency vulnerabilities or information leakage.

Others concern incorrect semantic inference.

For SILT, both are important because a technically secure system may still make unsafe claims about Standing, Authority, Consent, Reliance, Attribution, Obligation or Revocation.

Conversely, a semantically faithful model does not remove the need for ordinary software security controls.

The two layers should remain distinct.

---

## Implementation-profile security

Implementation profiles may introduce operational security rules that are stricter or more concrete than SILT Core itself.

For example, a profile may require:

- particular authentication mechanisms;
- mandatory revocation lookups;
- binary runtime `ALLOW` / `DENY` decisions;
- specific evidence chains;
- local authority hierarchies;
- particular key-management rules.

Those may be entirely appropriate within the profile.

They must not be silently promoted into universal SILT Core requirements.

The reverse also matters: an implementation profile must not claim Core conformance while using local technical shortcuts to manufacture semantic relations that the applicable Source or Profile Expression does not support.

---

## Out of scope

The following are generally out of scope for security reporting:

- general disagreement with SILT Core’s normative or philosophical framing;
- requests for legal advice;
- claims about legal enforceability in a specific jurisdiction that do not expose a repository defect;
- vulnerabilities solely in third-party systems not maintained here;
- speculative production risks in systems that have not adopted SILT Core;
- issues caused solely by modifying SILT materials outside this repository.

These may still be useful research or design topics, but they are not automatically security vulnerabilities in this repository.

---

## Reporting a security issue

If GitHub private vulnerability reporting is enabled, please use that channel.

If private reporting is not available, open a minimal public issue requesting a secure contact pathway.

Do not include sensitive exploit details, live keys, private credentials, personal data, confidential legal instruments, community-confidential material or production secrets in a public issue.

A useful report should include:

- affected file or component;
- description of the issue;
- why it matters;
- whether it is technical, semantic, governance-related or mixed;
- whether the issue affects Core, a companion document, a conformance fixture or an implementation profile;
- suggested mitigation, if known;
- whether public disclosure could create risk.

---

## Responsible disclosure

Please give the project maintainers reasonable time to review and respond before publicising a serious issue.

Issues may be handled as:

- code or validator corrections;
- documentation fixes;
- schema or fixture corrections;
- conformance-test additions;
- implementation-profile changes;
- release errata;
- research questions for a subsequent SILT version.

A semantic issue should not automatically reopen v0.2 Core. Post-freeze Core changes require evidence of a recurring semantic distinction that cannot be expressed faithfully through the existing architecture without material distortion.

---

## Security principles

SILT Core security includes more than software correctness.

The project therefore prioritises:

- Source-grounded semantic relations;
- bounded Presentation;
- explicit Profile Expression provenance;
- Authority distinct from Technical Capability;
- Evidence distinct from the relation evidenced;
- delegation containment without silent escalation;
- Revocation without assumed universal cascade;
- semantic continuity distinct from cryptographic continuity;
- Profile-Expression-specific evaluation;
- no silent aggregation across plural expressions;
- strict distinction between `SATISFIED`, `NOT_SATISFIED` and `INDETERMINATE`;
- deliberate non-expression remaining outside the evaluation model;
- Attribution distinct from Binding and liability;
- clear separation between normative specification and non-normative implementation machinery.

> A system may execute successfully and still be semantically unsafe.

---

## No production warranty

SILT Core materials are provided for specification, research, testing and public-interest infrastructure development.

They are not legal advice.

They are not a production security guarantee.

They do not determine legal enforceability in any specific jurisdiction.

Implementers remain responsible for independent security, legal, cultural, governance, privacy, compliance and operational review before using SILT concepts in live systems.

---

## Licence

The repository currently contains an Apache License 2.0 root licence. The v0.2 release process is separately reconciling the licence boundary between specification/documentation and reference code.

See [`LICENSE`](./LICENSE) for the current repository licence while that release work is completed.
