# SILT Core v0.2.0

**Status:** Public release  
**Release date:** 23 September 2026  
**Repository:** https://github.com/Sugarlicks/silt-identity-core  
**Release:** https://github.com/Sugarlicks/silt-identity-core/releases/tag/v0.2.0  
**DOI:** https://doi.org/10.5281/zenodo.22908026  
**Website:** https://siltcore.org  
**Author:** Gareth Farry  
**Copyright:** © 2026 Gareth Farry

SILT Core is a semantic architecture for moments of encounter between Participants and systems grounded in different legal, customary, cultural, private, institutional or technical orders.

Its canonical architectural seam is:

> **Source -> Standing -> Presentation -> evaluation at the encounter**

SILT makes relevant relational legitimacy mutually legible without requiring originating orders to collapse into a single ontology or surrender their own sources of authority. It is semantically thick and operationally thin.

## v0.2.0 result

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

- `spec/SILT_Core_v0.2.0_Semantic_Architecture.md` - the canonical v0.2.0 Semantic Architecture.
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

## Citation

Farry, Gareth. 2026. *SILT Core v0.2: Semantic Architecture*. Version 0.2.0. SILT Core. Zenodo. https://doi.org/10.5281/zenodo.22908026

For citation metadata and the concept DOI covering future SILT Core versions, see `CITATION.md`.

## Historical implementation material

AUT CISRC remains a separate **SILT Core v0.1 implementation profile**. It is not part of the v0.2 migration or conformance claim.
