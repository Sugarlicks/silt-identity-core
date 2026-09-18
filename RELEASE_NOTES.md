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

## Remaining before v0.2.0

The project still needs final rights-chain/project sign-off; repository replacement of conflicting v0.1 governance and README material; reconciliation of older schemas, examples and reference validators that are actually in the v0.2 release path; the ecosystem-positioning companion; and final tagged archival metadata/DOI.

## AUT CISRC release-boundary clarification

AUT CISRC is retained as a SILT Core v0.1 implementation profile. It is not scheduled for migration to v0.2 and is not part of the v0.2 conformance claim. This clarification removes an unnecessary and historically misleading release blocker.
