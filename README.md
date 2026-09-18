# SILT Core v0.2 - Release Candidate 2.1

**Status:** Release Candidate 2.1  
**Date:** 18 September 2026  
**Repository:** https://github.com/Sugarlicks/silt-identity-core  
**Website:** https://siltcore.org  
**Author:** Gareth Farry  
**Copyright:** © 2026 Gareth Farry

SILT Core is a semantic architecture for moments of encounter between Participants and systems grounded in different legal, customary, cultural, private, institutional or technical orders.

Its canonical architectural seam is:

> **Source -> Standing -> Presentation -> evaluation at the encounter**

SILT makes relevant relational legitimacy mutually legible without requiring originating orders to collapse into a single ontology or surrender their own sources of authority. It is semantically thick and operationally thin.

## Release-candidate result

The v0.2 architecture has passed four planned semantic pressure domains under a common conformance discipline: electronic transferable instruments, credential-carried institutional Standing, plural and collective Profile Expressions, and recursive AI-agent delegation. The unified suite contains 4 base fixtures and 30 adversarial variants.

An experimental mapping to Legal Context Protocol v1.0 was then used as an external carrier pressure test. The mapping is intentionally partial where carrier convenience would otherwise erase plural Profile Expressions or deliberate non-expression. No current test requires a new universal Core object.

This supports semantic freeze. It does not mean that SILT determines substantive legal validity, cultural legitimacy or institutional recognition.

## Core distinctions

SILT Core v0.2 does not contain a universal `Status` object or a universal `Capacity` object. Standing is relational and grounded in Source. Presentation is encounter-specific. Profile Expression supplies bounded encounter conditions without becoming a second architectural spine. Technical Capability remains distinct from Authority. Binding remains a downstream effect rather than a universal Core conclusion.

Evaluation has exactly three outcomes:

- `SATISFIED`
- `NOT_SATISFIED`
- `INDETERMINATE`

A condition deliberately outside evaluation is not a fourth outcome.

## Package contents

- `spec/SILT_Core_v0.2.0_Semantic_Architecture.md` - the single canonical v0.2.0 Semantic Architecture publication candidate.
- `conformance/` - the unified machine-validatable conformance suite and JSON Schema.
- `bindings/` - the experimental, non-normative SILT <-> LCP mapping.
- `docs/` - changelog, migration guidance and repository transition notes.
- `GOVERNANCE.md` - interim stewardship and change-control process.
- `CONTRIBUTING.md` - contribution boundary and semantic-change discipline.
- `IPR_POLICY.md` - interim specification IPR position.
- `TRADEMARK_AND_CONFORMANCE.md` - interim mark and conformance-claim policy.
- `LICENSING.md` and `LICENSES/` - licence scope and full licence texts.
- `ci/` and `.github/workflows/` - machine validation of the conformance suite.

## Licensing

The **v0.2** specification and narrative public documentation are licensed under **CC BY 4.0**. Machine-readable v0.2 conformance artefacts, bindings, examples and reference code are licensed under **Apache License 2.0**, unless a file states otherwise. Preserved v0.1 material, including AUT CISRC, retains its existing Apache 2.0 licence. Trademark, certification and patent rights are not granted merely by those copyright/software licences.

See `LICENSING.md`, `IPR_POLICY.md` and `TRADEMARK_AND_CONFORMANCE.md`.

## Governance posture

v0.2 uses interim maintainer stewardship with public change control. SILT does not yet claim foundation governance or institutional neutrality. Core semantic changes must be earned by a concrete conformance failure, implementation failure or external mapping that exposes an otherwise inexpressible semantic distinction.

## Release discipline

Release Candidate 2.1 is intended to be the publication base for `v0.2.0`. The rights chain is now fixed for this release: Gareth Farry is author and copyright holder, and SILT Core is the project/publishing identity. The single canonical specification artefact is present in `spec/`. Remaining work before the public tag is final project sign-off, merge of PR #4, tagging, archival deposit and DOI metadata.

AUT CISRC remains a separate **SILT Core v0.1 implementation profile**. It is not part of the v0.2 migration or conformance claim.
