# SILT Core v0.1 — Vietsch project public status

**Updated:** 23 October 2026 (New Zealand)  
**Project:** Delegation and Revocation Semantics for Federated Research Infrastructure  
**Funded by:** Stichting Vietsch (Vietsch Foundation)  
**Project lead:** Gareth Farry  
**Delivery status:** GitHub pilot release complete; independent Zenodo archival deposit and project financial close-out pending.

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
| Long-term Zenodo archive | Separate record for the **curated release ZIP**, not entire v0.2 repository snapshot | **Not yet deposited / DOI unverified** |
| Final public dissemination and financial close-out | Project summary and expenditure record / final donation claim if substantiated | Outstanding |

## Current research result

The reference validator demonstrates that one deliberately limited delegated research action can be represented, inspected and assessed against asserted issuer-chain relationships, requested action/resource/purpose, effective time/expiry and revocation. The automated pilot suite has **21 passing tests**. These tests do **not** authenticate the origin of institutional authority, validate signatures or demonstrate live cross-institution interoperability. The original archived v0.1 JSON Schemas and the AUT implementation-profile JSON Schemas have different structures; the suite checks the latter.

## Public release access

- **Official pilot release:** https://github.com/Sugarlicks/silt-identity-core/releases/tag/aut-cisrc-v0.1-pilot-2026
- **Curated archive ZIP:** https://github.com/Sugarlicks/silt-identity-core/releases/download/aut-cisrc-v0.1-pilot-2026/silt-vietsch-aut-cisrc-v01-pilot.zip
- **Checksum:** https://github.com/Sugarlicks/silt-identity-core/releases/download/aut-cisrc-v0.1-pilot-2026/silt-vietsch-aut-cisrc-v01-pilot.zip.sha256
- **Test evidence:** https://github.com/Sugarlicks/silt-identity-core/actions/runs/39859824052
- **Evaluation:** [Phase 3 pilot evaluation](phase-3-pilot-evaluation.md)

The five illustrative PNG diagrams are excluded from the curated release pending a separate image-provenance/rights review. The published narrative licence only applies to explicitly identified author-owned content; see `release/vietsch-v01/LICENCE_STATUS.md`.

## Next actions and reporting

The signed MoU calls for **bimonthly public project reporting and a public status page**. This page serves as the dated public status record, without representing unverified historical reporting as completed.

The final release milestone will be archived on Zenodo by depositing the **curated v0.1 ZIP** and verifying the actual assigned DOI; GitHub's automatically generated source archives contain the wider repository and are not the intended curated research deposit. An [upload guide](VIETSCH_ZENODO_MANUAL_DEPOSIT.md) is available. The remaining financial reporting must be based on substantiated research costs and payment records. The previously requested donation amounts are **not confirmation of funds received**.

**Acknowledgement:** This open research is supported by Stichting Vietsch (Vietsch Foundation).
