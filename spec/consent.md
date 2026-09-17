# Consent — v0.1 archival notice

This file is retained as a **SILT Core v0.1 specification artefact** for historical and migration reference.

The original v0.1 Consent specification defined Consent primarily as an explicit permission artefact for disclosure or use, granted by a Principal and constrained by recipient, purpose, scope, duration and revocation. It also imposed universal Core-level `MUST` requirements for a standard consent artefact and default non-disclosure / non-reliance behaviour.

Consent remains semantically important in SILT Core v0.2, but the v0.1 artefact model is **not the controlling v0.2 architecture**.

For v0.2, the canonical semantic reference is:

[`spec/v0.2/semantic-architecture.md`](./v0.2/semantic-architecture.md)

The settled v0.2 seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

In v0.2, **Consent is a bounded semantic relation of agreement or permission**. It is not restricted to a single universal disclosure artefact and is not reduced to a checkbox, signature, login state or technical assent event.

Those events may be Actions or Evidence concerning Consent, depending on the applicable Source, Presentation and Profile Expression.

Several concerns expressed in the v0.1 document remain useful, including:

- Consent should not be inferred merely from participation, login state or interface convention;
- Consent may be bounded by purpose, scope, duration, recipient or other expressed conditions;
- Revocation or withdrawal may be semantically relevant where the applicable relation is revocable;
- technical proof that an assent event occurred does not by itself settle the semantic sufficiency of Consent;
- collective Consent must not be inferred from individual assent without the relevant Authority and conditions.

What does **not** carry forward as universal v0.2 Core semantics is the v0.1 requirement that every Consent relation be expressed through one standard artefact containing a fixed mandatory field set, or that SILT Core itself must always produce default non-disclosure, non-reliance or `unauthorised` runtime conclusions when a consent reference or revocation check is unavailable.

Those may be appropriate rules in a particular implementation profile or legal regime. They are not universal SILT Core requirements.

There is therefore **no one-to-one mapping from the v0.1 Consent artefact to a single mandatory v0.2 representation**. A v0.1 consent artefact may provide Evidence of Consent, may itself be an Action or Presentation carrier, and may be evaluated under one or more Profile Expressions depending on the encounter.

The original v0.1 contents remain available through Git history. They should be read as historical specification material and, where relevant, as context for v0.1 implementations. They should not be used as normative v0.2 semantics.
