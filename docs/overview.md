
# SILT Core — Overview

**Authority semantics for digital action.**

This document provides a fuller overview of SILT Core: its purpose, primitives, use cases, design principles, relationship to existing systems, threat model, current status, and v0.2 planning direction.

For the short introduction, see [`README.md`](../README.md).
For normative specifications, see [`/spec`](../spec).
For schemas, reference material, validators, and misuse cases, see [`/schemas`](../schemas), [`/reference`](../reference), and [`/tests/misuse-cases`](../tests/misuse-cases).

---

## Why SILT exists

Current digital systems are built on a hidden assumption: legitimacy flows from external validation.

A government issues your identity.
A credential authority attests your attributes.
A platform recognises your account.
A system grants your permissions.

You exist, digitally, to the extent that external systems confirm you.

SILT begins from the other direction.

What a person, collective, institution, agent, or system carries into a moment of digital action — standing, authority source, mandate, obligation, consent, reliance, and revocation — does not begin with system recognition. It precedes it.

Current infrastructure has no stable grammar for this. It can model who you are, what attributes you hold, and what permissions you have been granted. It struggles to model what you bring into an action, in what capacity you are acting, by whose authority, under what mandate, and whether others may safely rely on the act.

SILT builds that grammar.

SILT Core is a semantic layer for expressing the conditions of lawful digital action across plural systems.

It is not a credential system.
It is not a permission layer.
It is not a blockchain protocol.
It is not a legaltech-only product.

It is the missing authority layer beneath these systems: the layer that asks not merely:

> Has this action been permitted?

but:

> By what source of authority is this action being taken, in what capacity, under what mandate, within what scope, with what consent, and how can that authority be revoked?

---

## Core question

SILT Core exists to answer one question:

> Is this action legitimately authorised, in this context, right now?

Most identity systems ask:

> Who is this?

Most permission systems ask:

> What is this account allowed to do?

SILT asks:

> What is the authority structure behind this action?

That distinction matters.

An action may be technically permitted but not legitimately authorised.

A key may sign.
A system may approve.
A workflow may execute.
An agent may transact.
A DAO may vote.
A platform may record the event.

None of that proves, by itself, that the action was taken in the right capacity, under a valid authority source, within mandate, with scoped consent, and with revocation conditions still intact.

SILT Core is concerned with that missing layer.

---

## Why this matters

Digital systems are shifting from passive tools to active execution environments.

AI agents, automated workflows, DAOs, digital commerce systems, legal platforms, civic infrastructure, and institutional governance tools are increasingly capable of executing actions with real-world consequences.

They can sign, approve, route, vote, transact, file, trigger, delegate, and coordinate.

Yet most systems still treat legitimacy as a by-product of authentication, permission, or platform role.

That is not enough.

A valid action requires more than identity.

It requires standing.
It requires capacity.
It requires authority.
It requires consent.
It requires reliance boundaries.
It requires revocation.

Without these semantics, digital systems risk executing actions that are technically permitted but not legitimately authorised.

This problem becomes urgent as software becomes more agentic. The question is no longer only whether a system can act. The deeper question is whether the action can be traced to a valid authority source, bounded by an intelligible mandate, and revoked when the conditions of authority no longer hold.

In an agentic environment, authority can no longer remain implicit.

---

## What SILT Core provides

SILT Core formalises authority conditions as interoperable primitives.

The current focus is on:

* **Status** — the recognised basis from which a person, collective, institution, agent, or system participates
* **Standing** — the contextual basis on which participation or action becomes legitimate
* **Capacity** — the role in which an action is taken
* **Authority Source** — the mandate, agreement, policy, relationship, instrument, governance process, or recognised source from which authority derives
* **Mandate Scope** — the permitted boundaries of action
* **Consent** — expressed acceptance under defined conditions
* **Delegation** — the transfer or extension of authority within defined limits
* **Reliance** — when others may safely treat an action as valid
* **Revocation** — how authority expires, is withdrawn, superseded, suspended, or terminated

These primitives are designed to be technology-agnostic and may be implemented across APIs, DID/VC systems, smart contracts, AI-agent frameworks, governance platforms, registries, secure execution environments, or other verification substrates.

SILT Core does not dictate a single worldview, legal system, identity model, or governance structure.

It provides a grammar through which different authority structures can become legible to digital systems.

---

## The problem SILT does not let systems avoid

Many systems collapse several distinct questions into one.

They treat identity, permission, authority, consent, and reliance as if they were the same thing.

They are not.

A verified identity does not prove capacity.
A permission does not prove authority.
A signature does not prove mandate.
A role does not prove standing.
A checkbox does not prove consent.
A successful execution does not prove legitimate reliance.
A prior grant of authority does not prove authority still exists.

SILT Core separates these layers.

The purpose is not to make systems more complicated.

The purpose is to make them honest.

---

## Conceptual model

At a high level, SILT Core treats digital action as an authority event.

An authority event asks whether a proposed action has enough contextual authority to proceed, be relied upon, or be recorded as valid within a given system.

A simplified authority context may be expressed as:

```text
Participant
+ Capacity
+ Authority Source
+ Mandate Scope
+ Consent Conditions
+ Reliance Conditions
+ Revocation State
= Action Validity Context
```

This is not a universal legal formula.

It is a semantic frame.

SILT Core does not claim that every action satisfying this structure is legally enforceable in every jurisdiction. Rather, it makes the relevant authority conditions explicit, structured, auditable, and checkable.

The value is not in replacing legal, governance, or identity systems.

The value is in making their authority conditions machine-legible.

---

## Example authority context

The following illustrative example shows how a digital action might be expressed in SILT-like terms.

```json
{
  "action_id": "action-2026-0001",
  "participant": {
    "identifier": "did:example:agent-123",
    "type": "ai_agent"
  },
  "capacity": {
    "role": "delegated_agent",
    "declared_by": "did:example:principal-456"
  },
  "authority_source": {
    "type": "mandate",
    "reference": "sha256:authority-source-hash",
    "issued_by": "did:example:principal-456",
    "issued_at": "2026-06-22T00:00:00Z"
  },
  "mandate_scope": {
    "permitted_actions": [
      "approve_invoice",
      "initiate_payment"
    ],
    "max_value": "5000 NZD",
    "context": "supplier-payment-workflow",
    "expires": "2026-12-31T23:59:59Z"
  },
  "consent": {
    "terms_reference": "sha256:terms-file-hash",
    "accepted_by": "did:example:principal-456",
    "accepted_at": "2026-06-22T00:00:00Z",
    "constraints": [
      "supplier_verified",
      "invoice_matched",
      "amount_within_scope"
    ]
  },
  "reliance": {
    "reliance_permitted": true,
    "reliance_limit": "within_mandate_scope_only",
    "third_party_visibility": "limited"
  },
  "revocation": {
    "status": "active",
    "revocation_registry": "https://example.org/revocations",
    "last_checked": "2026-06-22T12:00:00Z"
  }
}
```

This example is illustrative only.

It does not define a final schema.

Schemas, field names, and validation logic are subject to formal specification work.

---

## Authority is not the same as identity

SILT Core sits above identity infrastructure.

A person, organisation, agent, wallet, or system may be identifiable without being authorised.

A DID may show who controls an identifier.
A verifiable credential may attest a claim.
A digital signature may show that a key approved something.
A permission system may show what an account is technically allowed to do.

SILT asks what authority structure governs the action.

```text
DID:        Who controls this identifier?
VC:         What claim has been attested?
Signature:  Which key approved this?
Permission: What is this account allowed to do?
SILT:       In what capacity is this action being taken, under what
            authority, within what scope, with what consent, and with
            what revocation conditions?
```

This distinction is central.

Identity systems are necessary, but they do not exhaust legitimacy.

---

## Design principles

### 1. Status before attributes

Identity is not only a bundle of attributes.

A person, collective, institution, agent, or system may hold standing in a context before a system has issued a credential about them.

SILT Core begins with the conditions under which a participant may appear, act, or bind itself in context, not only the claims that can be verified about them.

### 2. Authority before permission

A permission flag can say that an account may perform an action.

It does not explain whether the action is validly authorised.

SILT separates technical permission from authority.

### 3. Capacity is contextual

Capacity is not a fixed identity label.

A participant may act personally, as agent, trustee, officer, delegate, steward, member, representative, system operator, AI agent, or under another mandate.

SILT models capacity as context-bound, declared, scoped, and verifiable.

### 4. Consent is constraint

Consent is not interface text.

Consent must be scoped, evidenced, limited, auditable, and capable of withdrawal.

SILT treats consent as a constraint on action, not as a decorative record after the fact.

### 5. Delegation must not become capture

Authority may be delegated without collapsing the principal into the system that carries out the action.

SILT models delegation as bounded, traceable, and revocable.

### 6. Revocation is first-class

Authority must be able to end.

Revocation, expiry, suspension, and supersession are not edge cases.

They are core to legitimate action.

### 7. Plural systems need shared edge conditions

SILT Core does not standardise meaning itself.

It standardises the boundary conditions through which meaning becomes operationally legible across different legal, cultural, institutional, and governance traditions.

The grammar can be shared while the underlying traditions remain plural.

---

## Non-preclusion axioms

SILT Core must not become another cage.

The specification is therefore guided by three non-preclusion axioms.

### Axiom 1 — Authority source plurality

SILT Core does not assume a single source of authority.

Authority must be explicitly referenced and scoped, but its origin may vary across legal, contractual, organisational, institutional, customary, associative, technical, or community frameworks.

The specification should not require state-issued credentials as a precondition of standing.

It should not privilege institutional issuance over contractual, associative, relational, or community mandate.

It should accept any authority source that can be expressed, scoped, evaluated, relied upon, and revoked within the semantic grammar.

### Axiom 2 — Capacity is contextual, not ontological

SILT Core models acting capacity within a defined context.

It does not define what a person, collective, institution, agent, or system is in an ultimate sense.

It defines how that participant is acting within a specific transaction, governance event, workflow, or execution context.

This separates identity from capacity.

A participant may act in multiple capacities over time.

Capacity is declared, scoped, and verifiable, not inferred.

### Axiom 3 — Revocability as structural safeguard

All delegation, mandate, and authority expressions should include explicit revocation or expiry pathways.

Authority should not silently persist beyond scope.

Revocation protects against platform capture, stale authority, irreversible delegation, and identity collapse.

Revocability is not merely an administrative feature.

It is a structural safeguard for agency.

---

## Relationship to existing systems

SILT Core is designed to complement, not replace, existing identity, legal, governance, and trust infrastructure.

### DID and verifiable credential systems

DID and VC systems provide important tools for identifier control, claims, attestations, and selective disclosure.

SILT Core adds authority semantics.

It asks:

* In what capacity is this identifier acting?
* What authority source governs the action?
* What mandate limits apply?
* Has consent been expressed under defined conditions?
* Can reliance be safely placed on the action?
* Has authority expired or been revoked?

SILT can be layered over DID/VC infrastructure without requiring every authority source to be state-issued or platform-issued.

### Digital signatures

Digital signatures prove that a key signed something.

They do not, by themselves, prove that the signing party was acting in the correct capacity, under a valid mandate, or within scope.

SILT provides the surrounding authority context.

### Smart contracts

Smart contracts execute logic.

SILT helps define the authority conditions that should exist before execution and the revocation or reliance conditions that may matter after execution.

SILT is not “law as code”.

It is authority semantics before, during, and after digital execution.

### AI agents

SILT does not attempt to make AI systems legal persons.

It models authority provenance, mandate scope, delegation chains, reliance boundaries, and revocation pathways for autonomous and semi-autonomous systems.

This matters because agentic systems may act beyond immediate human instruction while still needing a traceable authority source.

An agent with a wallet is not the same thing as an agent with standing.

### Legal and governance workflows

Legal and governance systems already rely on concepts such as agency, mandate, role, consent, authority, reliance, delegation, and revocation.

SILT makes these conditions explicit and portable across digital environments.

It does not replace law or governance.

It makes their authority conditions more legible.

### Digital commerce

Commercial systems often involve delegated authority, settlement instructions, payment approvals, instruments, obligations, reliance, and revocation.

SILT can help clarify who may bind whom, under what authority, within what limits, and when reliance should terminate.

This is particularly relevant where digital commerce intersects with AI agents, private ordering, programmable settlement, or cross-platform workflows.

---

## Use cases

SILT Core is relevant wherever high-trust systems need authority to be explicit before execution.

Potential use cases include:

* AI agent actions
* legal automation
* DAO governance
* digital commerce
* civil society infrastructure
* institutional approval flows
* delegated authority systems
* cross-platform mandate continuity
* public-interest digital infrastructure
* consent-sensitive data sharing
* high-trust automated workflows
* human and machine coordination systems
* legal workflow validation
* governance approval processes
* fiduciary agent controls
* grant and treasury disbursement systems
* community mandate tracking
* platform exit and continuity mechanisms

Legaltech is one important application.

The deeper problem is broader: digital systems increasingly act before they can explain the authority behind the action.

SILT Core addresses that gap.

---

## What SILT Core is not

SILT Core is not:

* a wallet
* a blockchain
* a KYC system
* a credential issuer
* a general identity provider
* a legaltech-only product
* a replacement for legal advice
* a regulatory compliance product by itself
* a platform for centralising identity or authority
* a claim that every action is legally enforceable in every jurisdiction

SILT Core is authority semantics infrastructure.

It makes the conditions of action explicit, auditable, scoped, and revocable.

---

## Authority claim planning

Structured authority claims are a candidate area for v0.2 planning.

The purpose of this work would be to explore how authority context may attach to a proposed or completed digital action.

A possible authority claim may include:

* action reference
* participant reference
* declared capacity
* authority source
* mandate scope
* consent reference
* reliance conditions
* revocation state
* expiry or review condition
* evidence references
* validation result

This section is exploratory.

It does not define the v0.2 release scope and should not be treated as a commitment until formally adopted.

The purpose is not to create a new identity credential.

The purpose would be to make authority conditions inspectable at the point of action.

A system should be able to ask:

```text
Can this action proceed?
Can this action be relied upon?
Can this action be audited later?
Can this authority be revoked?
```

If those questions cannot be answered, the system may still execute technically, but it is operating with authority ambiguity.

---

## Validation model planning

Validation logic is a candidate area for v0.2 planning.

A basic validation flow may ask:

1. Is the participant identified?
2. Is the acting capacity declared?
3. Is an authority source referenced?
4. Is the mandate scope defined?
5. Is the proposed action within scope?
6. Is consent anchored to terms or defined conditions?
7. Are reliance conditions stated?
8. Is the authority currently active?
9. Has the authority expired, been revoked, or been superseded?
10. Can the validation result be recorded or audited?

The validator would not determine ultimate legal enforceability.

It would evaluate whether the authority semantics required for valid digital action are present, coherent, and checkable.

This is a deliberately limited claim.

Limited claims travel further.

This section is exploratory and does not commit v0.2 to a specific validator design.

---

## Reference consent validator

SILT Core v0.1 is a specification-first release.

A reference consent validator is available under [`/reference/validators/consent`](../reference/validators/consent).

The validator is experimental and non-normative. It is provided to test early implementation patterns only. It does not define the specification and does not constrain future v0.2 schema design.

---

## Threat model

SILT Core is being developed against recurring legitimacy failure modes.

### Silent escalation

Authority expands beyond its original scope without explicit approval.

Example: a workflow that begins with permission to schedule meetings later gains the ability to approve expenditure without a new mandate.

### Stale authority

Action continues after expiry, revocation, role change, board change, employment change, key rotation, or organisational transition.

Example: an API key continues approving actions after the human authority behind it has left the organisation.

### Overbroad delegation

A mandate grants more power than intended.

Example: an agent receives general execution authority when the intended authority was limited to a specific task, time period, or value threshold.

### Consent drift

Consent given for one purpose is reused for another.

Example: consent to share information for one transaction becomes assumed consent for ongoing profiling, disclosure, or automated decision-making.

### Platform capture

Authority becomes dependent on a platform account rather than an independent mandate.

Example: a platform role is treated as sufficient authority even where the underlying authority relationship has changed or ceased.

### Ambiguous capacity

An action is taken without declaring the capacity in which it is taken.

Example: a person signs personally when they intended to sign as trustee, officer, delegate, or agent.

### Irreversible consent

Systems provide no meaningful withdrawal pathway.

Example: consent is treated as permanent because the interface has no revocation state, expiry condition, or withdrawal mechanism.

### Unclear reliance

Third parties cannot determine whether they may safely rely on an action.

Example: a payment, vote, approval, or signature is visible, but its reliance conditions are not.

### Recursive delegation failure

Automated systems generate downstream actions without traceable authority lineage.

Example: an AI agent delegates to sub-agents or automated services, but the original authority source, scope, and revocation pathway are lost.

These are governance and legitimacy risks, not only software bugs.

---

## Historical and conceptual grounding

SILT Core is not nostalgia for older systems.

It is a response to a structural problem that older legal, commercial, and governance systems often understood more clearly than contemporary platforms do.

Across many traditions, action was not treated as valid merely because a person was identifiable.

Standing mattered.
Capacity mattered.
Witness mattered.
Mandate mattered.
Obligation mattered.
Reliance mattered.
Revocation or release mattered.

Trade, credit, governance, kinship, trust, and institutional decision-making have long depended on knowing who may act, in what capacity, under what authority, and with what consequences.

Modern digital systems often flatten these questions into authentication and permission.

SILT Core recovers the missing semantic layer without requiring a return to any single historical model.

History is evidence, not ornament.

It shows that coherent authority and exchange do not begin with central issuance alone.

They begin with recognisable standing, expressed authority, bounded obligation, and structured reliance.

---

## Current status

SILT Core is in active development.

**v0.1 has been released** as the initial public specification and framing layer.

v0.1 establishes:

* the authority problem
* the distinction between identity, permission, and authority
* the initial SILT Core semantic frame
* the foundational primitives
* the first misuse-case orientation
* the project’s specification-first posture

**v0.2 is being planned.**

The v0.2 planning process is focused on clarifying the next set of specification priorities before any new commitments are made.

Candidate areas under consideration include:

* structured authority claims
* validation logic
* revocation and expiry handling
* expanded primitive definitions
* AI-agent execution contexts
* legal and governance workflow examples
* digital commerce examples
* DID/VC interoperability mapping
* misuse-case tests

These are planning areas, not release commitments.

The final v0.2 scope will be determined separately and should not be inferred from this overview.

The project remains specification-first.

Implementation is downstream of semantic clarity.

---

## Release direction

### v0.1 — Initial public specification

Released.

v0.1 establishes:

* the authority problem
* the distinction between identity, permission, and authority
* the initial SILT Core semantic frame
* the foundational primitives
* the first misuse-case orientation
* the project’s specification-first posture

### v0.2 — Planned next release

v0.2 is being planned.

No final scope is asserted in this document.

Planning discussions may consider:

* structured authority claims
* validation logic
* revocation and expiry handling
* expanded primitive definitions
* AI-agent execution contexts
* legal and governance workflow examples
* digital commerce examples
* DID/VC interoperability mapping
* misuse-case tests

The final v0.2 scope will be determined separately and should not be inferred from this overview.

No future release scope beyond v0.2 is asserted in this document.

---

## Repository orientation

The repository currently includes:

```text
/
├── docs/
├── spec/
├── schemas/
├── reference/
│   └── validators/
│       └── consent/
├── tests/
│   └── misuse-cases/
├── README.md
└── LICENSE
```

The structure may evolve as the specification develops.

The current focus is on:

* specification development
* schema design
* reference validation logic
* misuse cases
* interoperability notes
* conceptual documentation
* implementation-facing examples

---

## Contributing

SILT Core is open to critique, contribution, and extension.

Useful contributions include:

* primitive definitions
* schema suggestions
* use case analysis
* threat models
* examples
* legal and governance mappings
* DID/VC interoperability notes
* AI-agent authority scenarios
* revocation models
* implementation experiments
* misuse-case tests
* authority claim examples

Before contributing, please review the project framing and preserve the core distinction between authentication, permission, and authority.

The project should remain technology-agnostic, plural-source, revocation-aware, and specification-first.

---

## Licence

Apache License 2.0.

See [`LICENSE`](../LICENSE).

---

## Disclaimer

SILT Core is an infrastructure and specification project.

It is not legal advice.
It does not determine legal enforceability in any specific jurisdiction.
It does not replace professional advice, regulatory compliance, or formal legal process.

Its purpose is to make authority conditions explicit, structured, auditable, and revocable across digital systems.

---

## Contact

Website: [siltcore.org](https://siltcore.org)
Repository: [github.com/Sugarlicks/silt-identity-core](https://github.com/Sugarlicks/silt-identity-core)

---

## Closing note

SILT Core starts from a simple premise:

Digital systems should not only ask whether an action can be performed.

They should ask whether the action is legitimately authorised.

As digital systems become more autonomous, the future problem is not only identity verification.

It is authority legibility.

SILT Core provides a grammar for that legibility.
