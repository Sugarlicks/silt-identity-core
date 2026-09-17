# Revocation — v0.1 archival notice

This file is retained as a **SILT Core v0.1 specification artefact** for historical and migration reference.

The original v0.1 Revocation specification defined Revocation primarily as a Principal’s withdrawal of a Consent or Delegation artefact, with a universal revocation-event structure, mandatory verifier checkability requirements and a default non-reliance rule when revocation state could not be established.

Revocation remains semantically important in SILT Core v0.2, but that artefact-and-registry model is **not the controlling v0.2 architecture**.

For v0.2, the canonical semantic reference is:

[`spec/v0.2/semantic-architecture.md`](./v0.2/semantic-architecture.md)

The settled v0.2 seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

In v0.2, **Revocation is a semantic change affecting a relation where the applicable Source, Authority conditions or Profile Expression make that relation revocable**. It is not limited to one universal Consent-or-Delegation artefact type, and SILT does not require one universal technical revocation registry or lookup mechanism.

Several concerns expressed in the v0.1 document remain relevant, including:

- Revocation should be represented explicitly where a relation is revocable;
- the effect of Revocation should be distinguishable from the technical mechanism used to communicate or verify it;
- Revocation is prospective by default unless another expressed rule provides otherwise;
- stale technical permission or Technical Capability must not be mistaken for continuing semantic Authority after Revocation;
- Evidence of Revocation and the semantic effect of Revocation should remain distinguishable.

The v0.2 model is more precise about lifecycle and target relation:

- **Authority** may have lifecycle states such as `Active`, `Revoked`, `Expired`, `Superseded` or `Suspended` where the applicable Profile Expression or implementation uses them;
- `Expired`, `Superseded` and `Suspended` should not be collapsed automatically into one universal Revocation event;
- **Standing does not have a universal SILT lifecycle** and must not be treated as though every change in Standing is a revocation event;
- Revocation does not imply a universal cascade through every historically derived relation unless the applicable Authority conditions or Profile Expression make current validity dependent on that relation.

What does **not** carry forward as universal v0.2 Core semantics is the v0.1 requirement that every Revocation use one mandatory event structure, that all implementations expose one deterministic and timely verifier-check mechanism, or that failure to establish revocation state must always produce a universal `invalid`, `unauthorised` or deny-by-default runtime conclusion.

Those may be appropriate operational requirements in a particular implementation profile. They are not universal SILT Core requirements.

There is therefore **no one-to-one mapping from the v0.1 Revocation event artefact to a single mandatory v0.2 representation**. A v0.1 revocation event may provide Evidence of Revocation, may itself be an Action or Presentation carrier, and may affect Authority, Consent or another revocable relation according to the applicable encounter semantics.

The original v0.1 contents remain available through Git history. They should be read as historical specification material and, where relevant, as context for v0.1 implementations. They should not be used as normative v0.2 semantics.
