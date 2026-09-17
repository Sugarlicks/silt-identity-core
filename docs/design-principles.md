# Design principles

SILT Core v0.2 is governed by a small number of architectural disciplines intended to preserve semantic meaning across plural encounters without absorbing the machinery or ontology of the systems that implement it.

The controlling v0.2 semantic reference is:

[`spec/v0.2/semantic-architecture.md`](../spec/v0.2/semantic-architecture.md)

The canonical seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

This document is explanatory. If a design principle appears to conflict with the canonical semantic architecture, the semantic architecture controls.

---

## 1. Source-grounded Standing

Standing is relational and grounded in Source.

It is not a universal credential, status label, account state or self-certified attribute.

A Source may arise from a legal, customary, cultural, relational, private, institutional or other recognised normative ground. SILT does not require that Source to originate in the receiving system.

The receiving system may evaluate a Presentation of Standing. It does not thereby become the source of that Standing.

SILT Core v0.2 therefore does **not** contain a universal `Status` object.

---

## 2. Presentation at the encounter

Presentation is the present-tense act or envelope through which a Participant brings the minimum relevant projection of Standing, Authority or another semantic claim into a particular encounter.

Presentation does not create the relation being Presented.

It should expose no more than is relevant to the encounter where selective expression is possible.

The architecture therefore centres the encounter rather than a permanently complete representation of the Participant.

---

## 3. Profile Expression without ontological capture

A **Profile Expression** states bounded encounter-relevant conditions under which a Presentation may be evaluated.

It is not a complete representation of the originating legal, customary, cultural, contractual, relational or institutional order.

The originating substrate exceeds and remains independent of its Profile Expression.

SILT must therefore resist designs that turn a bounded expression into:

- a universal ontology;
- a master legal profile;
- a complete cultural model;
- a registry-defined identity;
- a substitute for the originating order itself.

---

## 4. Authority is not Technical Capability

Semantic Authority and technical ability to cause an effect are distinct.

A key may sign.  
A capability may permit an API call.  
A wallet may control an asset.  
A policy engine may allow execution.  
An agent may successfully perform a task.

None of those facts alone establishes SILT Authority.

> **Technical Capability ≠ Authority**

Authentication, dynamic authorisation, capability tokens, sessions, runtime policy and execution machinery remain downstream of the semantic layer unless a particular encounter has a semantic reason to refer to them.

---

## 5. Evidence is not the relation evidenced

Credentials, signatures, attestations, registry entries, documents and technical proofs may be Evidence.

They do not automatically become Source, Standing, Authority, Consent or another SILT relation merely because they can be verified.

The semantic claim and the Evidence offered in support of it must remain distinguishable.

This prevents cryptographic validity from being mistaken for semantic sufficiency.

---

## 6. Plural expressions do not imply universal precedence

An encounter may involve more than one Profile Expression.

Those expressions may agree, overlap, diverge or conflict.

SILT does not silently:

- merge them;
- rank them;
- privilege one as the universal receiving order;
- infer a meta-order that resolves every conflict.

An evaluation result remains linked to the Profile Expression under which it was produced unless an expressed composition rule provides otherwise.

Mutual legibility does not require ontological or jurisdictional collapse.

---

## 7. Semantic continuity is not cryptographic continuity

Standing, Authority, Attribution and Obligation may persist across changes in:

- keys;
- credentials;
- technical identifiers;
- accounts;
- sessions;
- capability tokens;
- execution infrastructure.

Conversely, continuing control of a key, credential or account does not prove that the underlying semantic relation still exists.

> **semantic continuity ≠ cryptographic continuity**

This distinction protects SILT from becoming dependent on one identity or key-management substrate.

---

## 8. Deliberate non-expression is legitimate

Not every relevant normative condition can or should be reduced into a bounded machine-readable expression.

Where expression would materially distort the originating order, a condition may remain deliberately unexpressed.

That condition remains outside SILT evaluation for the encounter.

It does not become a fourth evaluation outcome, and it should not be coerced into `INDETERMINATE` or `NOT_SATISFIED` merely because a machine cannot evaluate it.

SILT should preserve the boundary between what can be expressed faithfully and what should remain with the originating order.

---

## 9. Three evaluation outcomes only

For expressed conditions, SILT Core v0.2 uses:

- `SATISFIED`;
- `NOT_SATISFIED`;
- `INDETERMINATE`.

`INDETERMINATE` is not a synonym for invalidity.

Likewise, successful evaluation is not a universal conclusion of legal validity, legitimacy or compulsory acceptance.

Evaluation answers only the bounded question posed by the applicable Profile Expression in the encounter.

---

## 10. Binding is downstream

Binding is not a universal SILT Core conclusion.

A successful evaluation may contribute to downstream effects such as:

- creation or discharge of an Obligation;
- change of Standing;
- creation or alteration of Authority;
- Revocation;
- institutional recognition;
- settlement;
- another Profile-defined effect.

Which consequence follows depends on the applicable normative mechanism.

> **evaluation ≠ Binding**

Attribution likewise does not, by itself, determine liability or legal responsibility.

---

## 11. Delegation does not require a universal delegation primitive

Delegation may be represented as an **Action** through which derived Authority is constituted where the relevant Source and Profile Expression give that Action such effect.

SILT does not require a universal delegation artefact or token format.

Derived Authority should remain bounded by its parent delegable envelope unless another recognised Source independently supplies additional Authority.

Lineage, validity dependency and Revocation should not be collapsed into one universal cascade rule.

---

## 12. Obligation is distinct from Authority

Obligation is a persistent relational state of required performance, responsibility or constraint.

It may persist while Standing changes, Authority changes or the Participant occupying a relational position changes.

SILT therefore keeps Obligation distinct from Authority and from the Action that may create, transfer, perform or discharge it.

This distinction is especially important in transferable instruments and other private-ordering contexts.

---

## 13. Semantically thick, operationally thin

SILT should model a semantic distinction where losing it would materially distort meaning across the encounter.

It should not absorb operational machinery merely because implementations need that machinery.

This means keeping Core thin around:

- authentication;
- credential formats;
- key management;
- registries;
- transport;
- dynamic authorisation;
- capability systems;
- policy engines;
- runtime enforcement;
- execution infrastructure.

The question is not whether those systems matter. They do.

The question is whether they belong in the semantic architecture.

---

## 14. No silent inference

A SILT-conformant implementation should not manufacture semantic conclusions merely because a technical or institutional shortcut is convenient.

In particular:

```text
identity does not imply Authority
credential validity does not imply Standing
membership does not imply representational Authority
execution does not imply origination
technical precedence does not imply semantic precedence
representation does not constitute legitimacy merely by representing it
```

Where the semantic basis is absent, contested or unresolved, the implementation should preserve that fact rather than infer the missing relation.

---

## 15. Post-freeze scope discipline

After v0.2 semantic freeze, a new primitive or universal rule should be introduced only where real implementation, research or encounter evidence exposes a recurring semantic distinction that cannot be represented faithfully through the existing architecture without material distortion.

A concept should not enter Core merely because:

- another standard uses the term;
- a particular institution treats it as universal;
- a validator would be simpler with an extra object;
- a specific protocol has a convenient data structure;
- one implementation prefers a particular workflow.

The default response to implementation-specific complexity is to keep it in the implementation or companion layer unless the semantic evidence proves otherwise.

---

## Guiding discipline

SILT Core should remain capable of carrying meaning across encounters without claiming ownership over the orders from which that meaning arises.

> **Source → Standing → Presentation → evaluation at the encounter**
>
> **semantic hand-off, not semantic surrender**
