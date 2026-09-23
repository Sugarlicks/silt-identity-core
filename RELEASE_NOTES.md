# SILT Core v0.2 - Release Candidate 2.1 Notes

Release Candidate 2.1 carries the Semantic Freeze Candidate 1 architecture forward without adding a new Core primitive. The changes in this package are publication, governance, licensing and repository-readiness changes plus editorial removal of internal review-process residue from the reader-facing documents.

## Semantic freeze evidence

The unified conformance suite contains 4 base fixtures and 30 adversarial variants across four pressure domains. The experimental SILT <-> LCP mapping provides an external carrier test and records bounded loss rather than forcing SILT semantics into the carrier.

Two fixture-discipline corrections remain explicit: only `SATISFIED`, `NOT_SATISFIED` and `INDETERMINATE` are evaluation outcomes; and conditions outside evaluation are represented separately rather than as ad hoc outcomes.

## Publication changes

- Removed review-history and freeze-process residue from the Semantic Architecture.
- Added specification status and licence notice without changing Core semantics.
- Added explicit multi-licence scope and full CC BY 4.0 / Apache 2.0 texts.
- Added interim governance, contribution, IPR and trademark/conformance policies.
- Added machine validation script and GitHub Actions workflow for the conformance suite.
- Confirmed the public repository URL and added citation guidance.
- Confirmed Gareth Farry as author and copyright holder for the v0.2 Semantic Architecture, with SILT Core as project/publishing identity.
- Consolidated the release-candidate specification into the single canonical publication candidate at `spec/SILT_Core_v0.2.0_Semantic_Architecture.md`.

## Remaining before v0.2.0

The remaining publication gates are final project sign-off on the release candidate, merge of PR #4, creation of the `v0.2.0` tag, archival deposit, DOI minting and insertion of the final DOI into citation metadata.

## AUT CISRC release-boundary clarification

AUT CISRC is retained as a SILT Core v0.1 implementation profile. It is not scheduled for migration to v0.2 and is not part of the v0.2 conformance claim. This clarification removes an unnecessary and historically misleading release blocker.
