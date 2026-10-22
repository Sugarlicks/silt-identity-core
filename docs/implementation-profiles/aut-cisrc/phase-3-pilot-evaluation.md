# SILT Core v0.1 — AUT CISRC Phase 3 Pilot Evaluation (Draft)

**Status:** Draft for technical review, not final publication  
**Date:** 23 October 2026 (NZ)  
**Project:** Vietsch Foundation — Delegation and Revocation Semantics for Federated Research Infrastructure  
**Version boundary:** SILT Core **v0.1**. The AUT CISRC profile is **non-normative** and is not a v0.2 migration.

## 1. Evaluation question

Can a constrained, portable, inspectable, synthetic university research-delegation record be evaluated consistently for actor, permitted action, resource, purpose, effective time, expiry, and revocation using a lightweight validator?

The example models a project supervisor delegating dataset submission to a research assistant. No live AUT infrastructure is involved.

## 2. Basis and implementation

- Source: signed Vietsch MoU, Annex I, and April 2026 proposal.
- Phase 1: semantic model, early schemas, and research governance pilot planning (Donation Claim #1).
- Phase 2: AUT CISRC non-normative implementation profile, profile JSON Schemas, reference validator, seven example scenarios, initial directional review (Donation Claim #2).
- Phase 3: restore missing synthetic fixtures, implement structural issuer and revoker checks, add an automated regression harness, validate profile fixtures against JSON Schema Draft 2020-12, add malformed-input and boundary cases.

The pilot is an **illustrative** implementation: the chain expresses assertions for demonstration. It is not the official university authority structure.

## 3. Method

Run `python -m unittest discover -s tests/aut-cisrc -p 'test_*.py' -v` from the repository root after installing `jsonschema>=4.20,<5`. CI workflow: `.github/workflows/aut-cisrc-v01-tests.yml`.

The suite covers the original seven tests plus issuer/chain verification, revocation authority, missing evidence in strict mode, delegation ID mismatch, malformed input shapes and timestamp boundaries.

The assertions compare observed `ALLOW` or `DENY` outcomes and reason codes with expected results. A successful unit test means the implementation behaved as expected *for that fixture*.

## 4. Results and evidence

- Initial executable baseline, before schema conformance was integrated: **12/12 tests passed** on GitHub Actions run [39847362209](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39847362209).
- Expanded schema-based regression: **21/21 tests passed** on GitHub Actions run [39848903516](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516), including explicit validation of all five profile-specific artefact types. GitHub Actions execution logs reviewed.
- Implementation and evaluation changes are isolated in [draft pull request #6](https://github.com/Sugarlicks/silt-identity-core/pull/6), not merged into `main`.

The successful 21-test run includes test commit `35972ce574a49532c28349e6dd53a6d2cea59f71`; later documentation-only changes should not be represented as separately tested until their checks complete.

## 5. Preliminary findings

1. **Test-pack completeness:** The earlier example documentation referenced two files that were not present at the documented paths. Synthetic fixtures have been restored on the Phase 3 branch.
2. **Structural authority chain:** Presence of a chain alone does not demonstrate issuer authority. The Phase 3 validator checks an asserted parent relationship and declared governance domain; it does **not** validate the legal or organisational origin of that assertion.
3. **Revocation:** A revocation claim by a committee or higher-order actor requires a represented chain relationship, not simply a claimed node identifier.
4. **Schema conformance:** A structured schema check is required before applying validation logic. Bad JSON data should produce a controlled failure instead of an exception.
5. **Determinism:** Test assertions compare stable outcomes and reason codes. `validatedAt` records the execution time and is not itself deterministic.

## 6. Limitations

The pilot does **not** authenticate participant identities; cryptographically verify signatures, credentials or evidence; prove a university official's appointment or delegated legal power; determine legal compliance; integrate with AUT systems; replace IAM or grant production access. A modelled `ALLOW` represents a positive result under the narrow rules and synthetic inputs of this reference validator.

An earlier AUT directional review reported no major concerns about the pilot's shape, but **no formal AUT approval or certification has been obtained**. Claims of broader university portability require validation in additional institution-specific contexts.

## 7. Finalisation requirements

- [x] Observe a successful expanded CI run and reference its commit SHA, date, and test output.
- [ ] Review negative and boundary test coverage.
- [x] Confirm all five profile-specific schema types can validate the representative example artefacts in the dedicated regression test.
- [ ] Document remaining known limitations and avoid overclaiming real institutional authority.
- [ ] Decide whether the review branch is ready for merge.
- [ ] Prepare the final v0.1 release archive, DOI, dissemination summary, and Vietsch report.

## 8. Conclusion (provisional)

The AUT CISRC profile offers a constrained, inspectable demonstration of the v0.1 delegation and revocation workflow. Its strongest evidence will be the reproducible execution log, linked test fixtures, validator code, and explicit limitations. It is **research prototype evidence**, not institutional authorisation.
