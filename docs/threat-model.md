# Threat Model — SILT Core v0.2

This document describes the principal **semantic failure modes** SILT Core v0.2 is intended to expose or resist.

It is a companion document, not a separate normative specification. The controlling semantic reference is:

[`spec/v0.2/semantic-architecture.md`](../spec/v0.2/semantic-architecture.md)

The canonical seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

SILT operates at the boundary where different legal, customary, cultural, relational, private, institutional or technical orders meet. Its threat model therefore differs from a conventional identity or authorisation threat model: the central risk is not only that a message, credential or key is forged, but that an implementation **manufactures, collapses, erases or overstates semantic relations** at the encounter.

A technically secure implementation can still be semantically unsafe.

---

## 1. Scope

This threat model covers threats to the semantic integrity of SILT Core relations and encounter evaluation, including:

- Source-grounded Standing;
- Presentation as the bounded present-tense projection brought into an encounter;
- Profile Expression as an encounter-relevant expression rather than a representation of an entire originating order;
- Authority and its distinction from Technical Capability;
- Evidence and its distinction from the relation evidenced;
- Consent and Reliance where they are expressed;
- Action, Attribution and Obligation;
- Revocation and semantic continuity;
- evaluation outcomes;
- plurality between multiple Profile Expressions;
- deliberate non-expression where faithful bounded expression is not appropriate.

This threat model does **not** make SILT Core responsible for every security property required by an implementation.

Authentication, key custody, credential issuance, cryptographic proof systems, transport security, capability tokens, dynamic authorisation, sessions, policy engines, runtime enforcement and execution infrastructure remain below the Presentation line architecturally unless an encounter has a semantic reason to refer to them.

Those systems require their own security models.

SILT’s concern is whether their outputs are interpreted without semantic distortion.

---

## 2. Assets to protect

The primary assets are not merely identifiers or credentials. They are the integrity of the relations carried across the encounter.

SILT Core seeks to preserve:

- **Source integrity** — the claimed ground of a relation is not silently replaced by a platform, credential issuer, registry or receiving system;
- **Standing integrity** — Standing remains relational and Source-grounded rather than becoming a universal status or credential;
- **Presentation integrity** — only the minimum relevant projection is brought into the encounter, without forcing complete exposure of the originating substrate;
- **Profile Expression integrity** — a bounded encounter expression is not elevated into a complete ontology or universal governing order;
- **Authority integrity** — Authority is not inferred from identity, role, credential validity, key possession, technical permission or successful execution alone;
- **Consent and Reliance integrity** — expressed conditions are preserved without SILT inventing unstated law or universal effects;
- **semantic continuity** — changes in keys, accounts, credentials or technical infrastructure do not automatically create, extinguish or redefine the underlying semantic relation;
- **plurality** — distinct Profile Expressions can coexist or conflict without SILT silently ranking, merging or subordinating them;
- **evaluation integrity** — `SATISFIED`, `NOT_SATISFIED` and `INDETERMINATE` remain distinct, and deliberate non-expression is not forced into an outcome;
- **downstream boundary integrity** — evaluation, Attribution or technical execution are not silently converted into Binding, liability, enforceability or compulsory recognition.

---

## 3. Adversaries and pressures

Semantic failure does not require a malicious attacker. It can arise from institutional defaults, implementation convenience, legal overreach, ontology capture or ordinary system design.

Relevant adversaries and pressures include:

- platforms that treat account state or credential possession as sufficient semantic authority;
- receiving institutions that assume their own ontology is the universal frame for every encounter;
- credential issuers or registries that are treated as the source of Standing merely because they can verify a record;
- participants who overstate or misrepresent Standing, Authority, Consent or Attribution;
- agents or delegates operating outside the semantic bounds of their Authority;
- implementers who collapse semantic distinctions to simplify validation or runtime policy;
- systems that privilege technical executability over semantic legitimacy;
- governance structures that silently rank legal, cultural, customary or private orders;
- surveillance or data-extractive systems that demand unnecessary Source material or attributes;
- compromised or stale technical infrastructure that continues to execute after the relevant semantic Authority has changed;
- automated systems that convert uncertainty into rejection, invalidity or apparent certainty.

---

## 4. Core semantic threats

### T-01: Manufactured Standing

**Threat:** A system infers Standing from identity, account state, membership, credential possession, registry presence, role title or technical verification without identifying the Source from which the claimed Standing arises.

**Failure:** Standing is created by the receiving or technical system rather than remaining grounded in Source.

**Required discipline:** Standing must remain relational and Source-grounded. Identity or credential information may provide Evidence, but it does not by itself constitute Standing.

A receiving party may evaluate a Presentation of Standing. That evaluation does not make the receiver the source of the Standing.

---

### T-02: Evidence substituted for the relation evidenced

**Threat:** A signature, credential, attestation, registry entry, cryptographic proof or document is treated as though verification of that Evidence settles the existence or meaning of Standing, Authority, Consent, Attribution or another semantic relation.

**Failure:** Technical or institutional verifiability is confused with semantic sufficiency.

**Required discipline:** Evidence and the semantic relation it supports remain distinguishable. Verification may strengthen a Presentation without replacing evaluation of the claim itself.

---

### T-03: Technical Capability mistaken for Authority

**Threat:** A system concludes that an actor has SILT Authority because a key can sign, a wallet can spend, a capability token permits an operation, a policy engine returns `ALLOW`, an account has administrator privileges, or an agent successfully executes an Action.

**Failure:** Technical executability becomes semantic legitimacy.

**Required discipline:**

> **Technical Capability ≠ Authority**

Authority is evaluated according to its Source, conditions and applicable Profile Expression. Runtime permission and execution remain downstream technical concerns.

Key possession, including control of a cryptocurrency wallet or signing key, may be operationally decisive for execution while remaining semantically insufficient to establish Authority.

---

### T-04: Authority escape or delegation escalation

**Threat:** Derived Authority expands beyond the semantic envelope from which it arises, whether through role inference, uncontrolled sub-delegation, AI-agent recursion, organisational convenience or reuse in a new context.

**Failure:** An implementation manufactures additional Authority without an adequate semantic basis.

**Required discipline:** Where delegation is recognised, an Action may constitute derived Authority only where the applicable Source and conditions give it that effect. Derived Authority should remain bounded by the parent delegable envelope unless another recognised Source independently supplies additional Authority.

SILT does not require one universal delegation artefact, but it does require implementations not to infer Authority merely because technical delegation machinery exists.

---

### T-05: Excessive Presentation and Source extraction

**Threat:** A receiving system demands full identity records, complete Source material, cultural or legal context, genealogical information, institutional records or other data beyond what is necessary for the encounter.

**Failure:** Presentation becomes a mechanism of surveillance, coercion or ontological capture.

**Required discipline:** Presentation carries the minimum encounter-relevant projection that can faithfully express the claim. The originating Source or normative substrate does not need to be fully disclosed merely because a receiver wishes to evaluate the Presentation.

Selective disclosure, zero-knowledge techniques or other privacy-preserving mechanisms may support this discipline, but SILT Core does not mandate a particular technical method.

---

### T-06: Profile Expression capture

**Threat:** A Profile Expression is treated as a complete representation of the legal, customary, cultural, relational, contractual, institutional or other normative order from which it was drawn.

The receiving system then uses that expression to constrain, redefine or exhaust the originating order.

**Failure:** A bounded encounter expression becomes a master ontology or substitute for the originating substrate.

**Required discipline:** A Profile Expression is selective and encounter-relevant. The originating substrate exceeds and remains independent of its expression.

Where faithful bounded expression is not possible or appropriate, deliberate non-expression remains legitimate.

---

### T-07: Silent precedence between Profile Expressions

**Threat:** Multiple Profile Expressions apply to an encounter and the implementation silently merges them, ranks them, selects one as superior, or creates a single aggregate result without an expressed composition rule.

**Failure:** SILT invents a meta-order or conflict rule that the participating orders did not supply.

**Required discipline:** Results remain linked to the Profile Expression under which they were produced. SILT Core supplies no universal precedence rule between Profile Expressions.

An aggregate result is available only where an expressed composition rule provides one.

---

### T-08: Encounter escape and semantic replay

**Threat:** A Presentation, Consent relation, Authority expression, Evidence package or prior evaluation is replayed in a materially different encounter as if its earlier sufficiency automatically carried forward.

**Failure:** Encounter-bounded semantics become a durable universal permission, credential or conclusion.

**Required discipline:** The semantic question must be evaluated in the relevant encounter and under the applicable Profile Expression. Purpose, scope, recipient, temporal or other constraints remain effective where expressed.

Technical anti-replay measures such as nonces, hashes or transaction binding may be valuable implementation controls, but they do not replace the semantic requirement.

---

### T-09: Semantic and cryptographic continuity collapse

**Threat:** A system assumes that continuing possession of a key, credential, account or capability proves that Standing or Authority continues unchanged; or assumes that key rotation, credential replacement or infrastructure migration destroys the semantic relation.

**Failure:** Technical continuity is treated as the lifecycle of the semantic relation.

**Required discipline:**

> **semantic continuity ≠ cryptographic continuity**

Technical systems handle cryptographic continuity. SILT preserves the semantic distinction between those mechanisms and relations such as Standing, Authority, Attribution and Obligation.

---

### T-10: Revocation overreach or underreach

**Threat:** A Revocation is ignored because stale technical capability remains usable, or is overextended so that one Revocation silently invalidates every related Standing, Authority, Consent, Obligation or historical Action.

**Failure:** The semantic effect of Revocation is either weaker or broader than the applicable relation permits.

**Required discipline:** Revocation affects the relation that is revocable under the applicable Source, Authority conditions or Profile Expression.

Authority may have lifecycle states such as `Active`, `Revoked`, `Expired`, `Superseded` or `Suspended` where those states are applicable. They should not be collapsed into one universal event or cascade rule.

Standing does not have a universal SILT lifecycle.

Technical revocation registries, logs or status services may support implementation, but SILT Core does not mandate one universal mechanism.

---

### T-11: Outcome corruption

**Threat:** An implementation converts `INDETERMINATE` into `NOT_SATISFIED`, `INVALID`, `UNAUTHORISED` or another negative conclusion, or treats deliberate non-expression as though it were a failed condition.

**Failure:** Uncertainty or non-expression is replaced by a stronger semantic conclusion than the evaluation supports.

**Required discipline:** For expressed conditions, the Core outcomes remain:

- `SATISFIED`;
- `NOT_SATISFIED`;
- `INDETERMINATE`.

Deliberate non-expression is not a fourth outcome. It marks a boundary around what SILT has not attempted to evaluate.

---

### T-12: Evaluation converted into Binding or compulsory recognition

**Threat:** A Presentation satisfies the expressed conditions of a Profile Expression and the system therefore concludes that the receiver must accept it, that legal validity has been universally established, or that the Participant is bound or liable.

**Failure:** A bounded encounter evaluation is inflated into a universal downstream legal or normative effect.

**Required discipline:** Evaluation answers the bounded question expressed for the encounter.

It does not by itself establish universal Binding, enforceability, liability or compulsory recognition. Those effects depend on the applicable normative mechanism.

Attribution likewise remains distinct from Binding and liability.

---

### T-13: Collective authority reduced to individual identity

**Threat:** A collective, customary or institutional relation is forced into the identity or assent of one individual merely because that individual can authenticate, sign or present a credential.

**Failure:** Representation is mistaken for the Source of collective Standing or Authority.

**Required discipline:** A Participant claiming to act for a collective must present the relevant semantic basis for that Authority. Individual identity or membership alone does not establish representational Authority.

SILT must not manufacture collective Consent or Authority from individual assent where the originating order requires another basis.

---

### T-14: Agent execution mistaken for origination

**Threat:** An AI or software agent performs an Action successfully and the implementation attributes the semantic origin of that Action to the agent merely because it executed the operation.

**Failure:** Execution collapses into origination, Authority or Attribution.

**Required discipline:** The actor that executes an Action, the Source of Authority for that Action, and the target of Attribution may be different referents.

Recursive agent delegation must not create semantic Authority through technical recursion alone.

---

## 5. Privacy and correlation threats

SILT Core is not a privacy protocol, but its architecture should not force unnecessary disclosure.

Threats include:

- reuse of global identifiers across unrelated encounters;
- unnecessary exposure of Source material;
- Profile Expressions that demand more semantic detail than the encounter requires;
- correlation through Presentation or Evidence packaging;
- technical verification mechanisms that reveal relationship or revocation patterns.

Implementations should prefer context-appropriate disclosure and avoid assuming that auditability requires universal identifiability.

The exact privacy mechanism belongs to the implementation layer.

---

## 6. Technical security threats below the Presentation line

The following remain important but are not solved by SILT Core semantics alone:

- key theft or compromise;
- authentication bypass;
- credential forgery;
- replay at the protocol level;
- capability-token theft;
- session compromise;
- transport interception;
- registry compromise;
- implementation bugs;
- policy-engine failure;
- denial of service;
- malicious code execution.

A conforming SILT implementation must still address those risks through appropriate technical security controls.

The architectural boundary is important: solving a technical security problem must not silently redefine the semantic relation, and preserving a semantic relation does not eliminate the need for technical security.

---

## 7. Misuse-case driven testing

The companion misuse cases in [`tests/misuse-cases/`](../tests/misuse-cases/) provide adversarial scenarios for these threats.

They should be used to test whether documentation, adapters, conformance fixtures, implementation profiles and reference code:

- manufacture Standing or Authority;
- collapse Evidence into the relation evidenced;
- confuse Technical Capability with Authority;
- over-disclose through Presentation;
- treat Profile Expression as ontology;
- silently merge or rank plural results;
- collapse semantic and cryptographic continuity;
- corrupt `INDETERMINATE` or deliberate non-expression;
- infer Binding, liability or compulsory recognition from evaluation;
- reduce collective Authority or agentic Action to identity or execution alone.

These tests do not require every implementation to use the same operational control. They test preservation of the semantic distinction.

---

## 8. Design discipline

The threat model can be reduced to a small set of questions:

- What is the **Source** of the relation being claimed?
- What **Standing** or Authority actually arises from that Source?
- What minimum projection is being brought into this encounter through **Presentation**?
- Under which **Profile Expression** is that Presentation being evaluated?
- Has the implementation added, removed or merged a semantic conclusion that the participating orders did not express?
- Has technical capability or verification been mistaken for semantic legitimacy?
- Has an encounter-specific evaluation been converted into a universal downstream effect?

The governing posture remains:

> **semantically thick, operationally thin**
>
> **Source → Standing → Presentation → evaluation at the encounter**
>
> **semantic hand-off, not semantic surrender**
