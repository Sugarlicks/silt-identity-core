# SILT Core - Interim Governance and Change Control

**Applies to:** SILT Core v0.2 and its maintenance cycle  
**Status:** Interim maintainer stewardship pending any future multi-stakeholder governance vehicle

## 1. Purpose

SILT Core is public semantic infrastructure. Governance therefore has to protect two things at once: openness of the semantic grammar and discipline at the point where changes could alter its meaning.

The current architectural centre is:

> **Source -> Standing -> Presentation -> evaluation at the encounter**

Governance MUST NOT silently reintroduce discarded universal objects, collapse plural orders into a single ontology, or move authentication, dynamic authorisation or runtime capability machinery into Core merely because an implementation finds that convenient.

## 2. Current stewardship

Until a formal multi-stakeholder or neutral stewardship body is constituted, SILT Core is maintained under transparent maintainer stewardship through the public repository.

This is an interim governance arrangement. SILT MUST NOT describe itself as foundation-governed, institutionally neutral or controlled by a standards body unless and until that becomes true in practice.

Maintainers are responsible for release decisions, issue triage, pull-request review, conformance-suite integrity and publication of reserved-matter decisions. External adoption or participation does not transfer control of the specification by implication.

## 3. Decision classes

### Editorial and non-semantic changes

Typographical corrections, citation fixes, formatting changes and clarifications that do not alter normative meaning may be accepted through ordinary review. They may be released as v0.2.x errata.

### Conformance, examples and implementation changes

Changes to fixtures, reference code, mappings or examples may be accepted where they preserve Core semantics. If such work reveals an architecture gap, the gap is escalated rather than silently patched in an implementation-specific layer.

### Core semantic changes

A Core semantic change is a reserved matter. A proposal MUST identify:

- the concrete failure or ambiguity;
- the affected Core term, invariant or boundary;
- why the distinction cannot already be expressed by the current architecture;
- at least one worked encounter or negative test demonstrating the failure;
- foreseeable effects on plural/collective authority, private ordering, AI-agent delegation and institutional use where relevant.

Preference, elegance, terminology fashion or alignment pressure from an adjacent standard is not sufficient reason to reopen Core.

### Governance, licensing, IPR and marks

Changes to licence scope, patent/IPR commitments, trademark or certification policy, contribution rights, the canonical architecture seam, the three-valued evaluation vocabulary, or the authority to issue a release are reserved matters and require an explicit published decision.

## 4. Change process

Major changes SHOULD begin with a public issue before a pull request. The issue should state whether the proposal is normative, explanatory, illustrative, experimental or implementation-specific.

Where a proposal affects Core semantics, the associated conformance case should be added or updated before the normative change is merged. A semantic change that cannot be expressed as a testable difference requires exceptional justification.

Maintainers SHOULD record the rationale for accepted or rejected reserved-matter changes in the issue or pull-request history.

## 5. Versioning

- `v0.2.x` is reserved for editorial corrections, clarified wording and compatible conformance or implementation maintenance that does not change Core semantic meaning.
- A change that alters a primitive, invariant, required semantic distinction or evaluation rule requires a new minor architecture version, normally `v0.3` while SILT remains pre-1.0.
- Experimental bindings and implementation profiles are versioned independently and remain non-normative unless explicitly promoted through the Core change process.

## 6. Normative and non-normative material

The Semantic Architecture is the canonical normative reference for Core v0.2. Conformance fixtures test the architecture but do not create new semantics by accidental vocabulary. Experimental mappings, implementation profiles, commercial tools and advisory material are non-normative unless expressly stated otherwise.

Where older material conflicts with the current Semantic Architecture, the current Semantic Architecture governs and the older material must be migrated or marked historical.

## 7. Commercial and institutional boundary

The open Core may support commercial reference implementations, assurance, integration, training, specialist mappings and advisory work. Commercial participation does not purchase control of the public semantic language.

Certification, when introduced, may assess conformance to the published grammar. It MUST NOT claim to manufacture the legal, cultural, customary or institutional legitimacy of an underlying Source, Standing or Profile Expression.

## 8. Future stewardship

A later multi-stakeholder or neutral stewardship vehicle may be desirable as adoption broadens. Any transition SHOULD preserve public access, transparent change control, an implementable IPR position and representation of communities whose normative orders are likely to be affected by the standardisation process.
