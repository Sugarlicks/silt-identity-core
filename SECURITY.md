# Security Policy

SILT Core is a specification-first project focused on authority semantics for digital action.

This repository may include specifications, schemas, misuse cases, documentation, and experimental reference code.

Security issues may arise in two different ways:

1. technical vulnerabilities in reference code, schemas, or examples
2. semantic or governance vulnerabilities in the authority model itself

Both matter.

---

## Current Status

The current public release is **v0.1**.

**v0.2 is being planned.**

Reference code in this repository is experimental and non-normative unless expressly stated otherwise in a specification document.

The reference consent validator under `/reference/validators/consent` is experimental and non-normative. It is provided to test early implementation patterns only. It does not define the specification and does not constrain future v0.2 schema design.

SILT Core should not be treated as production security infrastructure at this stage.

---

## Supported Scope

Security review is welcome for:

* reference validators
* schemas
* example authority claims
* misuse cases
* revocation logic
* consent modelling
* delegation modelling
* reliance conditions
* authority source handling
* documentation that could create unsafe implementation assumptions

Security review may include both technical and semantic concerns.

---

## Examples of Relevant Issues

Relevant issues include:

* validator logic that incorrectly treats invalid consent as valid
* examples that imply authority persists after revocation
* schemas that make revocation optional where it should be explicit
* examples that collapse identity, permission, and authority
* delegation flows that allow silent escalation
* misuse cases that miss obvious coercion or capture risks
* documentation that suggests reference code is normative when it is not
* ambiguity that could lead implementers to overstate legal enforceability
* patterns that encourage irreversible consent or stale authority

---

## Out of Scope

The following are generally out of scope for security reporting:

* general disagreement with SILT Core’s framing
* requests for legal advice
* claims about enforceability in a specific jurisdiction
* vulnerabilities in third-party systems not maintained by this repository
* speculative production risks in systems that have not adopted SILT Core
* issues caused by modifying SILT materials outside this repository

These may still be useful as discussion topics, but they are not security vulnerabilities in the repository itself.

---

## Reporting a Security Issue

If GitHub private vulnerability reporting is enabled, please use that channel.

If private reporting is not available, open a minimal public issue requesting a secure contact pathway.

Do not include sensitive exploit details, live keys, private credentials, real personal data, confidential legal instruments, or live production information in a public issue.

A useful security report should include:

* affected file or component
* description of the issue
* why it matters
* whether the issue is technical, semantic, or both
* suggested mitigation, if known
* whether public disclosure could create risk

---

## Responsible Disclosure

Please give the project maintainers reasonable time to review and respond before publicising a serious issue.

Because SILT Core is currently specification-first and early-stage, some issues may be handled as:

* documentation fixes
* schema clarifications
* misuse-case additions
* validator corrections
* non-normative warnings
* future v0.2 planning inputs

Not every issue will result in code changes.

---

## Security Principles

Security in SILT Core includes more than software correctness.

The project treats authority failure as a security concern.

SILT Core therefore prioritises:

* explicit capacity
* scoped authority
* revocable consent
* mandate boundaries
* reliance clarity
* prevention of silent escalation
* resistance to platform capture
* clear separation between normative specification and experimental reference code

A system may be technically functional while still being unsafe if it cannot explain whether an action was legitimately authorised.

---

## No Production Warranty

SILT Core materials are provided for specification, research, testing, and public-interest infrastructure development.

They are not legal advice.

They are not a production security guarantee.

They do not determine legal enforceability in any specific jurisdiction.

Implementers are responsible for independent security review, legal review, compliance review, and operational testing before using SILT Core concepts in live systems.

---

## Licence

This repository is licensed under the Apache License 2.0.

See [`LICENSE`](./LICENSE) for details.
