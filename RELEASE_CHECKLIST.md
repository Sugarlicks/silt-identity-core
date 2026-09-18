# SILT Core v0.2 - Release checklist

## Completed in Release Candidate 2.1

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
- [x] v0.1 -> v0.2 migration guidance drafted for repository materials that are actually being migrated.
- [x] AUT CISRC explicitly retained as a SILT Core v0.1 implementation profile and removed from the v0.2 migration scope.
- [x] Draft GitHub migration PR prepared on `release/v0.2-rc2.1` (PR #4); no merge or final tag performed.
- [x] v0.1-era generic schemas, consent validator and misuse-case material classified as historical for repository migration; AUT implementation artefacts remain v0.1.
- [x] Ecosystem-positioning companion produced and kept non-normative.
- [x] v0.2 README, governance, contribution, licensing/IPR, security, positioning and conformance-claim material applied on the release branch.
- [x] Complete machine-readable conformance suite installed on the release branch.
- [x] Repository conformance CI passed on the complete suite: 4 base fixtures, 30 adversarial variants, outcome vocabulary locked.
- [x] Rights chain confirmed: Gareth Farry is author and copyright holder; SILT Core is the project/publishing identity.
- [x] Single canonical v0.2.0 specification artefact published at `spec/SILT_Core_v0.2.0_Semantic_Architecture.md`.

## Required before public v0.2.0 tag

- [ ] Project sign-off on Release Candidate 2.1 wording and release authority.
- [ ] Confirm final citation metadata and add DOI only after the final tag is archived.
- [ ] Merge PR #4 after publication checks pass.
- [ ] Create release tag `v0.2.0` only after the publication checks above pass.
- [ ] Archive the tagged release and mint the Zenodo DOI.

## Post-v0.2 governance work

- [ ] Replace the interim patent/IPR position with a formal royalty-free or non-assertion contributor regime before SILT enters a mature multi-contributor standards process.
- [ ] Decide whether/when stewardship should move to a multi-stakeholder or neutral vehicle.
- [ ] Establish a formal certification programme only after trademark, scope, test-basis, revocation and appeal rules are ready.

## Freeze discipline

A further Core semantic change requires a concrete failure in conformance, external mapping or implementation that exposes an otherwise inexpressible semantic distinction. Preference, elegance or adjacent-standard fashion is not enough.
