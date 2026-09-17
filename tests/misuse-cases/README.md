# Misuse cases

This directory captures adversarial scenarios and failure modes for **SILT Core v0.2**.

These are not universal runtime policy rules. They are semantic stress tests: each case asks whether an implementation preserves the distinctions defined by the canonical architecture rather than silently replacing them with identity, credential, platform, capability or legal assumptions.

The controlling v0.2 reference is:

[`spec/v0.2/semantic-architecture.md`](../../spec/v0.2/semantic-architecture.md)

The canonical seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

At FC1, these scenarios are companion test material rather than a separate normative specification. An implementation may use different technical mechanisms and still satisfy the semantic discipline.

Each misuse case asks a simple question:

> **Would this implementation manufacture, collapse or erase a semantic distinction that v0.2 requires it to preserve?**

---

## MC-01: Standing or Authority inferred from role, account or credential

**Scenario**: A platform treats an account marked `admin`, an organisational role, membership record, credential or verified identity as sufficient proof that a Participant has Standing or Authority in the encounter.

**Failure**: The implementation collapses identity, role or credential validity into a semantic relation that must instead be grounded in Source and evaluated through the relevant Presentation.

**Expected v0.2 posture**: Role, membership, account state and credentials may provide Evidence. They do not by themselves create Standing or Authority. Where the relevant semantic basis is absent or unresolved, the implementation must preserve that fact rather than infer the missing relation.

**Relevant architecture**: Source, Standing, Presentation, Evidence, Authority.

---

## MC-02: Technical Capability mistaken for Authority

**Scenario**: A key can sign, a capability token permits an API call, an agent possesses a tool, or a policy engine returns `ALLOW`; the implementation therefore concludes that the actor had SILT Authority to perform the Action.

**Failure**: Technical execution is treated as semantic legitimacy.

**Expected v0.2 posture**: Technical Capability and Authority remain distinct. Authentication, capability systems, dynamic authorisation and runtime enforcement may determine whether an Action can execute, but successful execution does not establish the semantic Authority from which the Action is claimed to arise.

**Relevant architecture**: Authority, Action, Presentation; machinery below the Presentation line.

---

## MC-03: Evidence mistaken for the relation evidenced

**Scenario**: A valid signature, credential, registry entry, attestation or cryptographic proof is treated as if it were itself the Source, Standing, Authority, Consent or other semantic relation being asserted.

**Failure**: Verification of Evidence is substituted for evaluation of the underlying semantic claim.

**Expected v0.2 posture**: Evidence and the relation it supports remain distinguishable. Cryptographic or institutional verification may strengthen a Presentation, but it does not automatically settle the meaning, sufficiency or legitimacy of the relation Presented.

**Relevant architecture**: Evidence, Source, Standing, Authority, Consent, Presentation.

---

## MC-04: Context or purpose escape

**Scenario**: A Presentation, Consent relation or expression of Authority that was sufficient for one encounter, purpose or Action is reused for a materially different encounter without re-evaluating the relevant conditions.

**Failure**: Encounter-bounded semantics are silently converted into a universal permission or durable credential.

**Expected v0.2 posture**: The relevant Presentation is evaluated in the encounter for which it is made. Consent, Authority and other relations may carry purpose, scope, duration, recipient or other constraints where those conditions are expressed. Reuse outside those conditions requires fresh evaluation rather than assumed continuity.

**Relevant architecture**: Presentation, Profile Expression, Consent, Authority, Action, Reliance.

---

## MC-05: Coerced or excessive Presentation

**Scenario**: A receiving system demands a complete identity record, full Source material, cultural or legal context, or raw personal attributes when only a narrow projection is relevant to the encounter.

**Failure**: Presentation becomes a vehicle for unnecessary disclosure or ontological capture.

**Expected v0.2 posture**: Presentation should carry the minimum encounter-relevant projection that can faithfully express the claim. SILT does not require the originating Source or normative substrate to be fully disclosed merely so an encounter can proceed.

**Relevant architecture**: Source, Standing, Presentation, Evidence.

---

## MC-06: Profile Expression treated as the originating order

**Scenario**: An implementation treats a Profile Expression as a complete model of the legal, customary, cultural, relational, contractual or institutional order from which it was drawn, and then uses that expression to constrain or redefine the originating substrate.

**Failure**: A bounded encounter expression becomes an ontology, master profile or substitute for the Source order itself.

**Expected v0.2 posture**: A Profile Expression contains only encounter-relevant semantic conditions. The originating substrate exceeds and remains independent of that expression. Non-expression is legitimate where faithful bounded expression is not possible or appropriate.

**Relevant architecture**: Profile Expression, Source, Presentation; deliberate non-expression.

---

## MC-07: Silent merge, ranking or precedence between Profile Expressions

**Scenario**: Two or more Profile Expressions apply to an encounter and produce different or conflicting results. The implementation silently merges them, chooses one as superior, or produces a single aggregate result without an expressed composition rule.

**Failure**: The implementation invents a meta-order or universal conflict rule that SILT Core does not supply.

**Expected v0.2 posture**: Results remain linked to the Profile Expression under which they were produced. SILT does not silently merge, rank or privilege Profile Expressions. An aggregate conclusion is available only where an expressed composition rule provides for one.

**Relevant architecture**: Profile Expression, evaluation at the encounter.

---

## MC-08: Cryptographic continuity mistaken for semantic continuity

**Scenario**: A Participant retains the same key, credential, account or capability after relevant Authority has been revoked, expired, suspended or superseded; or a key rotates and the implementation therefore assumes the underlying semantic relation has disappeared.

**Failure**: Key or credential state is treated as the lifecycle of the semantic relation itself.

**Expected v0.2 posture**: Semantic continuity and cryptographic continuity remain distinct. Technical continuity does not prove continuing Standing or Authority, and technical change does not by itself extinguish them. Revocation affects the relevant semantic relation according to the applicable Source, Authority conditions or Profile Expression; it does not create a universal cascade into every related relation.

**Relevant architecture**: Authority, Revocation, Standing, Evidence; semantic continuity distinct from cryptographic continuity.

---

## MC-09: `INDETERMINATE` treated as invalidity

**Scenario**: A Profile Expression cannot determine whether an expressed condition is satisfied, so the implementation converts `INDETERMINATE` into `NOT_SATISFIED`, `INVALID`, `UNAUTHORISED` or another negative semantic conclusion.

**Failure**: Absence of a determinate evaluation is turned into a conclusion that the Profile Expression did not establish.

**Expected v0.2 posture**: For expressed conditions, the Core evaluation outcomes are `SATISFIED`, `NOT_SATISFIED` and `INDETERMINATE`. `INDETERMINATE` must remain distinct. Deliberate non-expression is separate again and is not a fourth outcome.

**Relevant architecture**: Profile Expression, evaluation outcomes, deliberate non-expression.

---

## MC-10: Evaluation treated as Binding, liability or compulsory acceptance

**Scenario**: A Presentation satisfies the expressed conditions of a Profile Expression and the implementation therefore concludes that the receiver is legally compelled to accept it, that the Participant is universally bound, or that liability or enforceability has been established.

**Failure**: A bounded semantic evaluation is silently elevated into a universal downstream legal effect.

**Expected v0.2 posture**: Evaluation answers the question posed by the applicable Profile Expression in the encounter. It does not by itself create universal Binding, liability, enforceability or compulsory recognition. Any downstream effect depends on the applicable normative mechanism. Attribution likewise remains distinct from Binding and liability.

**Relevant architecture**: Presentation, Profile Expression, Attribution, Obligation, Binding as downstream effect.

---

## Use of these cases

These misuse cases should be used to challenge documentation, schemas, adapters, conformance fixtures, implementation profiles and reference code.

They should not be converted mechanically into universal runtime rules. A failure may arise because an implementation:

- manufactures a relation that was never established;
- collapses two distinct SILT concepts;
- moves technical machinery into the semantic layer;
- treats one order or Profile Expression as universally authoritative;
- turns an encounter-specific result into a universal conclusion; or
- forces expression where the originating order should remain unexpressed.

The governing discipline remains:

> **semantically thick, operationally thin**
>
> **Source → Standing → Presentation → evaluation at the encounter**
