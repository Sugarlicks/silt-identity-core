# SILT Core v0.2 overview

SILT Core enables Indigenous, customary, private, institutional and other plural orders to become mutually legible at moments of encounter without requiring them to collapse into a single ontology or surrender their own sources of authority.

The canonical architectural seam is:

> **Source -> Standing -> Presentation -> evaluation at the encounter**

**Source** grounds a relational position. **Standing** is that Source-grounded relational position, not a universal credential or self-certified status. **Presentation** is the encounter-specific act or envelope through which a Participant brings the minimum relevant projection of Standing into a particular encounter. Evaluation occurs against one or more bounded **Profile Expressions**, which express encounter-relevant conditions without representing or exhausting the underlying order.

SILT is semantically thick and operationally thin. Authentication, key continuity, credentials, capability tokens, sessions, dynamic authorisation, access control, policy execution and runtime execution remain outside Core unless a semantic distinction cannot otherwise be expressed.

## What v0.2 fixes

SILT Core v0.2 removes `Status` and any universal `Capacity` object from Core. It separates Technical Capability from semantic Authority, treats Binding as a downstream effect, permits multiple and conflicting Profile Expressions, preserves deliberate non-expression, and restricts evaluation to three outcomes: `SATISFIED`, `NOT_SATISFIED`, and `INDETERMINATE`.

The specification also distinguishes cryptographic continuity from semantic continuity and adopts the principle of **semantic hand-off, not semantic surrender**.

## Conformance

The v0.2 minimal semantic conformance suite contains four base encounters and thirty adversarial variants across electronic transferable instruments, credential-carried institutional Standing, plural/collective Profile Expressions and recursive AI-agent delegation. The suite is intended to catch prohibited semantic inferences, not to certify the substantive legitimacy of an originating legal, cultural or institutional order.

## Canonical material

- Normative semantic architecture: `spec/SILT_Core_v0.2_Semantic_Architecture_Release_Candidate_2.md`
- Conformance suite: `conformance/`
- Experimental mappings: `bindings/`
- Governance and contribution rules: `GOVERNANCE.md` and `CONTRIBUTING.md`
- Ecosystem positioning: `docs/ecosystem-positioning.md`

Older material that conflicts with the v0.2 Semantic Architecture is historical. AUT CISRC remains intentionally versioned as a SILT Core v0.1 implementation profile.
