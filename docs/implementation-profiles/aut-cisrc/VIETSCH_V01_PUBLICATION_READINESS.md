# Vietsch SILT Core v0.1 — publication and close-out readiness

**Status:** Publication and grant-close-out tracker; depositor-supplied Zenodo DOI recorded  
**Date:** 23 October 2026 (New Zealand)  
**Project:** Delegation and Revocation Semantics for Federated Research Infrastructure  
**Version boundary:** The funded AUT CISRC implementation is **v0.1**, non-normative. It is not a SILT Core v0.2 conformance exercise.

## Already delivered and evidenced

- Phase 1 semantic/model and initial schema work (Donation Claim #1, 23 June 2026).
- Phase 2 AUT CISRC implementation profile, JSON Schemas, prototype and seven original scenarios (Donation Claim #2, 4 August 2026).
- Phase 3 reconstructed illustrative fixtures, improved chain/revocation checks, runtime schema validation, expanded regression tests, and the [evaluation report](phase-3-pilot-evaluation.md).
- Recorded GitHub Actions evidence: [21/21 passing tests](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516).
- Technical baseline [PR #6](https://github.com/Sugarlicks/silt-identity-core/pull/6) and evaluation report [PR #7](https://github.com/Sugarlicks/silt-identity-core/pull/7) were merged.

## Release blockers / decisions (do not present as completed)

| Item | Required before final release | Current position |
| --- | --- | --- |
| Original v0.1 specification provenance | Identify original delegation and revocation texts and schemas; do not substitute AUT profile schemas for them | **Located**: `archive/v0.1/spec/delegation.md`, `archive/v0.1/spec/revocation.md`, `archive/v0.1/schemas/delegation.schema.json`, `archive/v0.1/schemas/revocation.schema.json`. Original GitHub release `v0.1` published 14 April 2026. Confirm publication snapshot/tag alignment before depositing |
| Licence compliance | Preserve historic Apache 2.0 grants and identify the additional Creative Commons permission for author-owned prose | **Approved 23 October 2026:** CC BY 4.0 additional permission for expressly listed project-authored narrative material; Apache 2.0 code/machine-readable artefacts. See `release/vietsch-v01/LICENCE_STATUS.md` and `VIETSCH_V01_LICENSING_DECISION.md`; diagrams excluded pending provenance |
| Version identity | Publish a **new** pilot archival tag without modifying historical `v0.1` or `v0.2.0` | **Complete:** [aut-cisrc-v0.1-pilot-2026](https://github.com/Sugarlicks/silt-identity-core/releases/tag/aut-cisrc-v0.1-pilot-2026) |
| Provenance | Pin final commit SHA, note merged PRs and 21-test CI result; include accurate synthetic-fixture disclosure | **Complete for GitHub release:** dedicated tag, 48-file curated ZIP, checksum asset and 21/21 preflight tests; refer to [pilot release](https://github.com/Sugarlicks/silt-identity-core/releases/tag/aut-cisrc-v0.1-pilot-2026) |
| AUT attribution | Keep initial directional review distinct from institutional authorisation; confirm any external acknowledgements | **No formal endorsement evidenced.** Five PNG diagrams excluded from pilot ZIP pending rights check |
| Zenodo archive | Cross-check published record with the intended curated GitHub ZIP and mixed licensing | **DOI supplied by depositor:** [10.5281/zenodo.23579725](https://doi.org/10.5281/zenodo.23579725); record inventory and licence display not independently verified |
| Public update | Publish public project status and dissemination note | [Public status](VIETSCH_PUBLIC_STATUS.md) published; separate dissemination announcement outstanding |
| Financial claim | Reconcile genuine costs and invoices against MoU's donation-claim requirements and prior amounts requested | **Do not invent cost amounts or assert payment** |

## Minimum proposed archival package

1. The original archived **v0.1 delegation and revocation specifications and schemas** linked above, pinned to their original version identity (do not conflate them with the non-normative AUT profile schemas).
2. The non-normative [AUT implementation profile](AUT-CISRC-Implementation-Profile.md), [authority-chain model](authority-chain.md), [pilot workflow](pilot-workflow.md), and [validation logic](validation-logic.md).
3. Five profile-specific JSON Schemas under `schemas/implementation-profiles/aut-cisrc/`.
4. The Python reference validator under `reference/validators/aut-cisrc-delegation/`.
5. Synthetic JSON fixtures, test suite and `test-results.md`.
6. [Phase 3 pilot evaluation report](phase-3-pilot-evaluation.md), with 21/21 CI link and bounded claims.
7. `README` for reproducibility, accurate licences and attribution, and release metadata.

Archive the *specific historical v0.1 implementation*, not the evolving repository's default `main` as an unversioned snapshot. The existing v0.2.0 Zenodo DOI belongs to a different publication and must not be represented as this project's deposit.

## Agreed MoU reporting context

Annex I requires refinement and publication via GitHub and Zenodo, and dissemination to the research and education community. The signed MoU additionally calls for public progress reporting on a **bimonthly** basis and a public status page. A GitHub commit alone does not demonstrate that status-page and dissemination obligations were discharged.

## Material technical distinction

The original v0.1 schema uses `delegation_id`, `principal`, `agent`, `capacity`, `scope` and `revocation` references. The AUT pilot defines profile-specific `delegationId`, `issuer`, `delegate`, `authorityChain`, `permittedActions` and `revokedBy` structures. Its 21 passing tests validate **the AUT profile schemas**, not direct conformance of the AUT artefacts to the original archived v0.1 JSON Schemas. The pilot is an implementation application with its own declared extension/translation boundary, not a normative v0.1 schema update. See [provenance note](VIETSCH_V01_SPECIFICATION_PROVENANCE.md).

## Release gate

The technical pilot and versioned GitHub release are complete; the depositor has provided the Zenodo record URL and DOI. Close-out still requires checking the Zenodo file inventory/checksum and licence display, public dissemination and end-of-project financial/reporting verification.
