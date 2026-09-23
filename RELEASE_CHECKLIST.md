# SILT Core v0.2.0 — final release checklist

**Target public release:** 23 September 2026

## Completed before release day

- [x] Canonical architecture fixed at Source -> Standing -> Presentation -> evaluation at the encounter.
- [x] Status removed from Core; no universal Capacity object.
- [x] Profile Expression consolidated with provenance, plurality and non-absorption rules.
- [x] Exactly three evaluation outcomes enforced.
- [x] Deliberate non-expression separated from INDETERMINATE and from absence.
- [x] WE01-WE04 adversarial pressure tests completed.
- [x] Unified minimal semantic conformance suite and JSON Schema produced.
- [x] Negative-test semantics normalised.
- [x] Experimental SILT <-> LCP mapping completed without exposing a missing Core primitive.
- [x] Invariant 24 narrowed to conditions that have entered evaluation.
- [x] Reader-facing editorial pass completed; review-process residue removed from the Semantic Architecture.
- [x] CC BY 4.0 and Apache 2.0 licence texts added with explicit path-level licence scope.
- [x] Interim governance and change-control process published.
- [x] Interim specification IPR policy published without implying a patent promise that does not exist.
- [x] Interim trademark and conformance-claim policy published.
- [x] Contribution policy updated for v0.2 architecture and IPR boundary.
- [x] Machine validation script and GitHub Actions workflow added for the conformance suite.
- [x] Public repository URL confirmed.
- [x] v0.1 -> v0.2 migration guidance drafted for repository materials actually being migrated.
- [x] AUT CISRC retained as a SILT Core v0.1 implementation profile and removed from v0.2 migration scope.
- [x] v0.1-era generic schemas, consent validator and misuse-case material classified as historical.
- [x] Ecosystem-positioning companion produced and kept non-normative.
- [x] v0.2 README, governance, contribution, licensing/IPR, security, positioning and conformance-claim material applied on the release branch.
- [x] Complete machine-readable conformance suite installed on the release branch.
- [x] Repository conformance CI passed on the complete suite: 4 base fixtures, 30 adversarial variants, outcome vocabulary locked.
- [x] Rights chain fixed: Gareth Farry is author and copyright holder; SILT Core is the project / publishing identity.
- [x] Single canonical specification created at `spec/SILT_Core_v0.2.0_Semantic_Architecture.md`.
- [x] Temporary segmented specification and conformance source parts removed from the public release tree.
- [x] `CITATION.cff` prepared for v0.2.0 with release date 23 September 2026.
- [x] `.zenodo.json` prepared for archival metadata.
- [x] Final GitHub release notes prepared in `RELEASE_v0.2.0.md`.
- [x] Release-day procedure prepared in `RELEASE_DAY.md`.
- [x] CI rerun after release-tree cleanup and passed.

## Release-day actions

- [x] Merge PR #4 to `main`, create tag `v0.2.0`, and publish the GitHub release from the reviewed commit.
- [x] Archive the immutable `v0.2.0` release in Zenodo, mint the DOI, then insert the DOI into the living repository citation metadata.

**Version DOI:** https://doi.org/10.5281/zenodo.22908026  
**Concept DOI:** https://doi.org/10.5281/zenodo.22908025

## Post-v0.2 governance work

- [ ] Replace the interim patent/IPR position with a formal royalty-free or non-assertion contributor regime before SILT enters a mature multi-contributor standards process.
- [ ] Decide whether/when stewardship should move to a multi-stakeholder or neutral vehicle.
- [ ] Establish a formal certification programme only after trademark, scope, test-basis, revocation and appeal rules are ready.

## Freeze discipline

No further Core semantic change should enter v0.2.0 unless a concrete blocking defect is found. After release, semantic changes belong to a subsequent version and require a concrete conformance, implementation or external-mapping failure that exposes an otherwise inexpressible semantic distinction.
