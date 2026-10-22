# SILT Core v0.1 — Vietsch project public status

**Updated:** 23 October 2026 (New Zealand)  
**Project:** Delegation and Revocation Semantics for Federated Research Infrastructure  
**Funded by:** Stichting Vietsch (Vietsch Foundation)  
**Project lead:** Gareth Farry  
**Delivery status:** GitHub pilot and Zenodo DOI recorded; public research dissemination note published in repository; website dissemination and financial close-out still to confirm.

## Purpose and agreed scope

The project develops a formal delegation/revocation model, machine-readable schemas and lightweight reference validator, then evaluates them through a constrained federated-research workflow. The AUT CISRC example is synthetic and non-normative: it is not a verified AUT governance chain, university certification or production IAM integration.

The project applies **SILT Core v0.1**. The later v0.2 Semantic Architecture is a separate public release and does not supersede the v0.1 pilot deliverables.

## Dated milestones and evidence

| Stage | Observed public output | Status |
| --- | --- | --- |
| Phase 1 — model and pilot planning | Initial delegation/revocation semantics and schema work, pilot definition; claim submitted/requested 23 June 2026 | Completed research stage |
| Phase 2 — non-normative university profile | Profile documents, schema prototypes, Python validator, seven original example scenarios; claim submitted/requested 4 August 2026 | Completed research stage |
| Phase 3 — technical refinement and evaluation | [PR #6](https://github.com/Sugarlicks/silt-identity-core/pull/6) and [Phase 3 report](phase-3-pilot-evaluation.md); [21/21 passing regression tests](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516) | Completed research stage |
| Release package and licensing | [PR #10](https://github.com/Sugarlicks/silt-identity-core/pull/10), CC BY 4.0 additional licence for specified author-owned prose while preserving Apache 2.0; 48 curated files | Complete |
| Public GitHub release | [Vietsch v0.1 AUT pilot release](https://github.com/Sugarlicks/silt-identity-core/releases/tag/aut-cisrc-v0.1-pilot-2026) with ZIP and SHA-256 checksum | **Published 23 October 2026 NZ** |
| Long-term Zenodo archive | [Zenodo record 23579725](https://zenodo.org/records/23579725); DOI [10.5281/zenodo.23579725](https://doi.org/10.5281/zenodo.23579725), supplied by depositor 23 October 2026 | **DOI received**; independent record-file and licence checks outstanding |
| Public dissemination | [Completion announcement](VIETSCH_COMPLETION_ANNOUNCEMENT.md) published in the public repository | Public research write-up available; posting to siltcore.org not yet verified |
| Financial close-out | Itemised cost record / final donation claim if substantiated | Outstanding |

## Current research result

The reference validator demonstrates that one deliberately limited delegated research action can be represented, inspected and assessed against asserted issuer-chain relationships, requested action/resource/purpose, effective time/expiry and revocation. The automated pilot suite has **21 passing tests**. These tests do **not** authenticate the origin of institutional authority, validate signatures or demonstrate live cross-institution interoperability. The original archived v0.1 JSON Schemas and the AUT implementation-profile JSON Schemas have different structures; the suite checks the latter.

## Public release access

- **Official pilot release:** https://github.com/Sugarlicks/silt-identity-core/releases/tag/aut-cisrc-v0.1-pilot-2026
- **Curated archive ZIP:** https://github.com/Sugarlicks/silt-identity-core/releases/download/aut-cisrc-v0.1-pilot-2026/silt-vietsch-aut-cisrc-v01-pilot.zip
- **Checksum:** https://github.com/Sugarlicks/silt-identity-core/releases/download/aut-cisrc-v0.1-pilot-2026/silt-vietsch-aut-cisrc-v01-pilot.zip.sha256
- **Test evidence:** https://github.com/Sugarlicks/silt-identity-core/actions/runs/39859824052
- **Evaluation:** [Phase 3 pilot evaluation](phase-3-pilot-evaluation.md)
- **Completion and dissemination write-up:** [Vietsch research outcome](VIETSCH_COMPLETION_ANNOUNCEMENT.md)
- **Zenodo record:** https://zenodo.org/records/23579725
- **DOI:** https://doi.org/10.5281/zenodo.23579725

The five illustrative PNG diagrams are excluded from the curated release pending a separate image-provenance/rights review. The published narrative licence only applies to explicitly identified author-owned content; see `release/vietsch-v01/LICENCE_STATUS.md`.

## Administrative verification and reporting

The signed MoU calls for **bimonthly public project reporting and a public status page**. This page serves as the dated public status record, without representing unverified historical reporting as completed.

The depositor supplied the newly published Zenodo record and DOI on 23 October 2026. The record's file list, SHA-256 match and displayed mixed licences have not been independently inspected through this workspace; verify these against the [curated pilot release](https://github.com/Sugarlicks/silt-identity-core/releases/tag/aut-cisrc-v0.1-pilot-2026). The [final technical report](VIETSCH_FINAL_TECHNICAL_REPORT.md) and [public completion announcement](VIETSCH_COMPLETION_ANNOUNCEMENT.md) are published in this repository; the separately intended posting at siltcore.org and any targeted distribution have not been verified. Financial reporting must be based on substantiated research costs and payment records. The previously requested donation amounts are **not confirmation of funds received**.

**Acknowledgement:** This open research is supported by Stichting Vietsch (Vietsch Foundation).
