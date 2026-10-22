# Proposed GitHub release notes — review before publication

**Suggested release title:** SILT Core v0.1 — Vietsch AUT CISRC Delegation and Revocation Pilot  
**Proposed pilot-specific tag:** `aut-cisrc-v0.1-pilot-2026` (availability to recheck before creation).  
**Status:** Release candidate notes, NOT evidence that a release or Zenodo deposit already exists.

This archival package documents the Vietsch-funded, constrained proof-of-concept applying the historical SILT Core v0.1 delegation and revocation semantics within a synthetic research-university workflow associated with AUT CISRC.

Delivered artefacts include original v0.1 delegation and revocation texts/schemas (historical provenance), five implementation-profile schemas, synthetic authority-chain and delegation/request fixtures, Python validator, 21-case automated regression suite and the Phase 3 evaluation report.

**Evidence:** 21/21 passing tests on [GitHub Actions](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516). Merged development and evaluation PRs: [#6](https://github.com/Sugarlicks/silt-identity-core/pull/6), [#7](https://github.com/Sugarlicks/silt-identity-core/pull/7).

**Interpretation:** The profile tests the structural consistency of asserted authority, not the factual or legal validity of a university office. It is not a live AUT deployment and is not v0.2 conformance. Original and profile JSON shapes differ.

This release is **separate from** the initial historical `v0.1` release dated 14 April 2026 and the later `v0.2.0` release. See the included file manifest and licensing status.

Funding acknowledgement: Stichting Vietsch (Vietsch Foundation).
