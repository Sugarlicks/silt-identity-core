# Changelog — SILT Core

## v0.2 - Release Candidate 2.1 (18 September 2026)

This release candidate is a semantic re-architecture rather than a cosmetic revision.

### Release-boundary correction

- AUT CISRC is explicitly retained as a SILT Core v0.1 implementation profile. It is outside the v0.2 migration and conformance scope.

### Architectural centre

- Establishes **Source → Standing → Presentation → evaluation at the encounter** as the canonical seam.
- Makes the encounter, rather than identity or credential issuance, the conceptual centre.
- Keeps SILT semantically thick and operationally thin.

### Standing and Presentation

- Removes **Status** as a SILT Core object.
- Defines **Standing** as relational and grounded in Source, not a universal credential or self-certified state.
- Introduces / stabilises **Presentation** as the bounded, present-tense act or envelope through which a Participant brings the minimum relevant projection of Standing into an encounter.
- Clarifies that evaluation does not constitute Standing unless the relevant Source and conditions give an Action constitutive effect.

### Profile Expression

- Replaces earlier interpretive-envelope / Lex / generic Profile formulations with **Profile Expression**.
- Defines Profile Expression as a bounded, selective and non-exhaustive expression of encounter-relevant semantic conditions.
- Allows plural, collective, composite, contested and provisional Profile Expressions without silent precedence or merger.
- Adds provenance and Authority-to-express safeguards.
- Clarifies that the originating order exceeds its expression and remains unencumbered by it.

### Outcomes and bounded expression

- Fixes the Core evaluation vocabulary at exactly **SATISFIED / NOT_SATISFIED / INDETERMINATE**.
- Separates deliberate non-expression and conditions outside evaluation from the outcome set.
- Narrows semantic non-inference: missing semantics produce INDETERMINATE only for a condition that has entered evaluation.

### Authority, capability and continuity

- Separates semantic **Authority** from **Technical Capability**.
- Keeps authentication, key continuity, credentials / capabilities, sessions, dynamic authorisation, access control and runtime execution outside Core unless an implementation demonstrates a missing semantic distinction.
- Distinguishes cryptographic continuity from semantic continuity.
- Preserves semantic lineage across recursive delegation and downstream execution.

### Collective and plural authority

- Makes explicit that collective Standing does not imply Authority to represent, bind, disclose for or speak for a collective.
- Rejects a universal canonical collective voice or meta-expression.
- Keeps disagreement and conflicting Profile Expressions explicit where no expressed precedence rule exists.

### Other Core changes

- Removes **Capacity** as a universal Core object.
- Keeps **Binding** as a Profile-defined or otherwise downstream effect, not a universal Core primitive.
- Maintains separate semantics for Consent, Reliance, Action, Attribution, Revocation and Obligation.
- Clarifies that assent may evidence Consent but is not universally equivalent to Consent.

### Conformance and release gate

- Adds a unified minimal semantic conformance suite with 4 base fixtures and 30 adversarial variants.
- Tests electronic transferable instruments, credential-carried institutional Standing, plural / collective Profile Expressions, and AI-agent recursive delegation.
- Adds an experimental non-normative SILT ↔ Legal Context Protocol mapping.
- No current test requires a new universal Core object.

### Publication and governance pass

- Removes internal review/freeze-process residue from reader-facing normative documents without changing Core semantics.
- Publishes explicit CC BY 4.0 / Apache 2.0 licence scope and full licence texts.
- Adds interim governance, contribution, IPR and trademark/conformance policies.
- Adds machine validation and GitHub Actions CI for the unified conformance suite.
- Confirms the public repository and adds citation guidance.
