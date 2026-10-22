# Vietsch SILT Core v0.1 — publication and close-out readiness

**Status:** Release-preparation checklist; no separate v0.1 deposit or DOI asserted  
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
| Canonical v0.1 formal specification | Identify immutable, complete v0.1 specification in the repo, or prepare one from the agreed v0.1 source documents | **Unverified**. The present `spec/` README identifies v0.2, and `archive/v0.1/README.md` is historical overview rather than clearly labelled formal delegation specification |
| Licence compliance | Check signed MoU's **Apache 2.0 for source code** and **Creative Commons for other information** against the existing repository's statement that historical v0.1 materials retain Apache 2.0 | **Needs express resolution** without assuming old licences can be withdrawn; do not relabel rights silently |
| Version identity | Select an unambiguous project-specific archival tag or immutable commit for the funded v0.1 pilot; avoid overwriting the existing v0.2 release | **To decide**; candidate `aut-cisrc-v0.1-pilot-2026`, subject to checking tag availability |
| Provenance | Pin final commit SHA, note merged PRs and 21-test CI result; include accurate synthetic-fixture disclosure | **Partly ready** |
| AUT attribution | Keep initial directional review distinct from institutional authorisation; confirm any external acknowledgements | **No formal endorsement evidenced** |
| Zenodo archive | Deposit an actual versioned package and confirm the assigned DOI | **Not done**; do not reuse the v0.2 DOI |
| Public update | Publish bimonthly status / final dissemination note and record its URL | **Draft prepared**, publication not verified |
| Financial claim | Reconcile genuine costs and invoices against MoU's donation-claim requirements and prior amounts requested | **Do not invent cost amounts or assert payment** |

## Minimum proposed archival package

1. A version-fixed, clearly identified **v0.1 delegation and revocation specification** (if actually available and vetted).
2. The non-normative [AUT implementation profile](AUT-CISRC-Implementation-Profile.md), [authority-chain model](authority-chain.md), [pilot workflow](pilot-workflow.md), and [validation logic](validation-logic.md).
3. Five profile-specific JSON Schemas under `schemas/implementation-profiles/aut-cisrc/`.
4. The Python reference validator under `reference/validators/aut-cisrc-delegation/`.
5. Synthetic JSON fixtures, test suite and `test-results.md`.
6. [Phase 3 pilot evaluation report](phase-3-pilot-evaluation.md), with 21/21 CI link and bounded claims.
7. `README` for reproducibility, accurate licences and attribution, and release metadata.

Archive the *specific historical v0.1 implementation*, not the evolving repository's default `main` as an unversioned snapshot. The existing v0.2.0 Zenodo DOI belongs to a different publication and must not be represented as this project's deposit.

## Agreed MoU reporting context

Annex I requires refinement and publication via GitHub and Zenodo, and dissemination to the research and education community. The signed MoU additionally calls for public progress reporting on a **bimonthly** basis and a public status page. A GitHub commit alone does not demonstrate that status-page and dissemination obligations were discharged.

## Release gate

Only declare the funded v0.1 project **published and complete** when specification provenance, licences, versioned archive, Zenodo DOI, public dissemination URL and end-of-project reporting are verified. The *pilot technical testing* is substantially complete; the *grant publication and reporting obligations* remain open.
