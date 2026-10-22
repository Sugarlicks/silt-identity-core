# SILT Core v0.1 — Phase 3 Pilot Evaluation Report

**Project:** Delegation and Revocation Semantics for Federated Research Infrastructure  
**Funder:** Stichting Vietsch (Vietsch Foundation)  
**Project lead:** Gareth Farry  
**Implementation context:** AUT Computer and Information Sciences Research Centre (CISRC)  
**Report date:** 23 October 2026 (New Zealand)  
**Status:** Phase 3 evaluation report; proposed for project publication review  
**Scope:** SILT Core **v0.1** and its non-normative AUT CISRC implementation profile only

## Executive summary

This report evaluates the constrained proof-of-concept developed under the Vietsch-funded SILT Core v0.1 project. Its purpose is to test whether a portable, inspectable record of delegated research authority can support repeatable assessment of permitted action, resource, purpose, temporal validity and revocation within a university research-governance example.

The pilot models a supervisor or project lead granting a research assistant limited, time-bound permission to submit a defined research dataset. It uses JSON artefacts, profile-specific JSON Schemas and a lightweight Python reference validator. Its authority chain is **synthetic** and represents an asserted institutional path for testing; it is not an authenticated or officially approved AUT authority structure.

Phase 2 supplied the implementation profile, schemas, reference validator and seven documented scenarios. In Phase 3, missing example fixtures were restored, issuer and revoker chain checks were tightened, schema validation was incorporated into the validator and an automated regression suite was added. The final expanded suite covered **21 test methods, all passing** in the recorded GitHub Actions execution.

The result is a reproducible implementation demonstration within the agreed narrow workflow. It **does not** establish the legal validity of delegated power, cryptographic validity of evidence, interoperability across deployed institutional systems, or production readiness.

## 1. Project mandate and evaluation boundary

The signed Vietsch Memorandum of Understanding and Annex I call for (i) a formal delegation and revocation model, (ii) machine-readable schemas, (iii) a lightweight validator checking scope, expiry and revocation, and (iv) validation through a constrained pilot workflow. The original proposal positions the work as a limited proof of concept for federated research infrastructure rather than a replacement for authentication, IAM or application authorisation.

This report addresses **Phase 3: refinement and evaluation** of the delivered pilot. Final repository release, Zenodo publication, dissemination and final project reporting remain separate publication/close-out activities unless and until completed.

SILT Core v0.1 is the version used throughout this implementation. The AUT CISRC profile is a **non-normative** application of v0.1 concepts. It does not alter the v0.1 normative specification and **must not be relabelled or migrated as v0.2 conformance**. The public repository's later v0.2 materials have their own architecture and release boundary.

## 2. Pilot scenario

The test scenario is an illustrative university research workflow:

1. A synthetic authority-chain artefact records an asserted institutional path relevant to research data.
2. A project supervisor (issuer) presents a limited delegation to a research assistant (delegate).
3. The delegation specifies a permitted action, identified dataset, purpose and effective period.
4. The research assistant submits a request carrying the relevant actor, action, resource, purpose, timestamp and delegation identifier.
5. A reference validator evaluates the supplied records and applicable revocation information.
6. The validator returns an `ALLOW` or `DENY` result with a machine-readable reason code and recorded checks.

In this prototype `ALLOW` means **the synthetic request satisfies the implemented pilot rules**. It is not an access grant issued by AUT or a claim of general legal authorisation.

### Principal artefacts

| Artefact | Function |
| --- | --- |
| Authority chain | Describes the asserted root, governance domain, nodes and parent relationships relevant to the pilot |
| Delegation | Identifies issuer and delegate, action, resource, purpose, effective interval, status and evidence references |
| Access request | Identifies the requested actor, action, resource, purpose, timestamp and delegation reference |
| Revocation event/log | Records purported revocation, revoker, asserted authority basis and effective time |
| Validation result | Records outcome, reason code, validator version, execution time and check details |

All five have profile-specific JSON Schemas using JSON Schema Draft 2020-12. The evidence-document references carried by examples are metadata, **not independently verified legal or cryptographic proofs**.

## 3. Implementation history and sources of evidence

**Phase 1 (Donation Claim #1, 23 June 2026):** initial semantic-object work, schema/object modelling, AUT workflow definition and validator logic outline. The claim expressly excluded final implementation and pilot execution.

**Phase 2 (Donation Claim #2, 4 August 2026):** public, non-normative AUT CISRC v0.1 implementation profile, authority-chain model, profile schemas, validator prototype, example JSON artefacts and the first seven expected-outcome scenarios. The claim did not assert AUT approval, production integration or final publication.

**Phase 3:** restoration of absent input fixtures referenced by the repository's example commands; structural checking of issuer and revoker relationships; pre-evaluation JSON Schema checks; defensive handling of malformed timestamps; a regression harness; expanded tests; and recorded CI outcomes.

Sources supporting the findings are the repository artefacts, the dated claim reports, the signed Vietsch MoU, the initial directional review record and the GitHub Actions logs linked below. No independent AUT production-system evidence was used.

## 4. Evaluation method and reproducibility

The prototype evaluates structured inputs with a Python command-line validator. The automated suite uses Python's standard `unittest` runner together with the `jsonschema` package.

From the repository root:

```bash
python -m pip install 'jsonschema>=4.20,<5'
python -m unittest discover -s tests/aut-cisrc -p 'test_*.py' -v
```

Relevant locations:

- Validator: `reference/validators/aut-cisrc-delegation/validate.py`
- Test suite: `tests/aut-cisrc/test_pilot_v01.py`
- Example fixtures: `examples/aut-cisrc-research-delegation/`
- Profile schemas: `schemas/implementation-profiles/aut-cisrc/`
- Workflow: `.github/workflows/aut-cisrc-v01-tests.yml`

Assertions compare expected and observed pilot outcomes and reason codes. An independent party can inspect, rerun and challenge these tests without access to AUT's operational systems.

**Determinism is bounded:** for a fixed valid fixture set, the tested rule decisions and reason codes are reproducible. The `validatedAt` field records actual execution time and is not byte-for-byte deterministic.

## 5. Results

### 5.1 Regression execution

| Evidence | Recorded result |
| --- | --- |
| First executable Phase 3 baseline | 12/12 tests passed |
| Final expanded Phase 3 test run | **21/21 tests passed** |
| JSON Schema conformance | Representative examples of all five artefact types validated in the test harness |
| CI environment | GitHub-hosted Ubuntu, Python 3.11, `jsonschema` 4.x |
| Production AUT integration | Not performed |
| Formal AUT certification/approval | Not obtained |

**Audit links:**

- Initial baseline: [GitHub Actions run 39847362209](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39847362209)
- Expanded 21-test result: [GitHub Actions run 39848903516](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516)
- Passing test commit: `35972ce574a49532c28349e6dd53a6d2cea59f71`
- Subsequent documentation updates recorded the verified result; [PR #6](https://github.com/Sugarlicks/silt-identity-core/pull/6) has been merged into `main`.

### 5.2 Coverage and observed behaviour

The original seven scenarios cover positive delegation, expiry, actor mismatch, action mismatch, applicable revocation, resource mismatch and purpose mismatch. All produced their expected pilot outcome and reason code.

Further tests cover absence of an authority chain, an unrecognised issuer node, an unauthorised revoker, revocation through a represented higher-order chain node, absence of evidence references in strict mode, inconsistent delegation identifiers, malformed timestamps, missing mandatory data, malformed revocation-log structure and expiry-boundary handling.

An additional conformance test validates representative examples against the five profile schemas, and validation-result schema conformance is also checked. **These are selected test cases, not exhaustive property-based or adversarial verification.**

### 5.3 Boundary findings

The time-limit rule treats a request at the stated expiry instant as within the interval and a request one second later as expired, consistent with the current implementation. This is a **pilot convention**, not a claim that all research institutions or future deployments must adopt this exact boundary.

When a revocation event applies before the request timestamp and the represented revocation authority passes the profile checks, the validator denies the request under the `DELEGATION_REVOKED` reason. Where the asserted revoker cannot be established by the model, the invalid-authority reason is returned under the tested scenario.

Malformed timestamps and structurally incomplete artefacts must not bypass the rule checks. Phase 3 introduced validation/error handling so the selected malformed inputs return controlled denials instead of unhandled exceptions.

## 6. Interpretation of the findings

### 6.1 Portable representation

The pilot demonstrates that the *representation* of an authority claim, a constrained delegation, a request and a revocation event can travel as ordinary inspectable JSON artefacts and be evaluated outside an application-specific role database. This is the key proof-of-concept contribution.

Portability of an artefact is not equivalent to acceptance of its claim. A receiving institution would still need a credible evidence source, trust arrangements and its own policy/authorisation environment.

### 6.2 Delegated authority and chain inspection

The original validator's authority-chain presence check was too weak to substantiate the documented issuer-authority condition. Phase 3 added structural membership, domain matching and parent-chain checks for the supplied synthetic model. Likewise, higher-order or committee revocation no longer succeeds solely because an event provides a seniority number or an arbitrary node identifier.

These checks demonstrate **internal structural consistency of the asserted chain**, not validation of the actual university powers behind the assertion. An otherwise well-formed but fabricated chain could still pass a purely structural evaluator.

### 6.3 Revocation as an auditable event

The tested revocation record provides a timestamped, inspectable basis for explaining why a request was denied. Within this narrow model, revocation is more transparent than an unexplained change of application role state. The prototype does not guarantee revocation propagation to other systems, continuous monitoring or reversal of previously executed actions.

### 6.4 Federated research relevance

The model offers a reviewable approach to representing cross-boundary delegation claims without replacing authentication federation or downstream access controls. This is a plausible integration point for research infrastructures, but **cross-institution interoperability was not tested** in this pilot. Wider applicability remains a research proposition rather than an observed deployment result.

## 7. Institutional review and limitations

The repository's initial directional review records no major concerns with the scoped proof-of-concept structure and notes that the underlying university-chain pattern is not AUT-exclusive. It describes committees, offices and agencies as potentially variable mediating nodes. The record is **not** evidence of a formal AUT technical sign-off, official university architecture, operational pilot, or legal endorsement.

The reference implementation does not:

- authenticate actors or verify their real-world appointments;
- validate signatures, credentials, document provenance or evidential truth;
- determine substantive institutional, statutory or legal validity;
- integrate with a live AUT service or enforce real dataset access;
- replace identity federation, IAM, KYC, access-control engines or institutional policy;
- prove multi-institution deployment, scalability or secure distributed revocation;
- establish universal precedence among institutional bodies or committees.

The workflow's `ALLOW`/`DENY` vocabulary is **specific to this v0.1 implementation profile**, and should not be projected into other SILT releases.

## 8. Phase 3 assessment against the funded objectives

| Funded objective | Phase 3 assessment |
| --- | --- |
| Formal delegation/revocation model | Established in preceding phases and exercised in the v0.1 implementation profile |
| Machine-readable schemas | Profile schemas are available; five representative artefact types passed schema checks |
| Lightweight validator | Implemented, refined and tested in the constrained workflow |
| Pilot validation | Reproducible synthetic workflow validated by 21 passing automated tests |
| Institutional approval or production integration | Not within the evidenced result |
| Final publication and dissemination | Separate release and reporting work remains |

Phase 3 provides adequate **prototype-level validation evidence** for the deliberately constrained proof-of-concept, subject to accurate characterisation in publication. It should not be presented as formal validation by AUT or proof of live federated interoperability.

## 9. Remaining release and closure tasks

Before claiming final public release of the *funded v0.1 project package*, complete the release checklist: verify repository paths and licence notices, identify the immutable release commit/tag, prepare archival metadata, publish the agreed Zenodo record, provide a concise dissemination notice and assemble final Vietsch progress/cost reporting as applicable.

The test evidence already published in GitHub can be cited directly. A Zenodo DOI or final publication status **must not be claimed until the deposit exists**. The report's existence within the broader SILT repository does not mean this specific v0.1 implementation has been separately archived.

## 10. Conclusion

The SILT Core v0.1 AUT CISRC implementation has demonstrated a bounded technical proposition: explicit delegation, time, scope and revocation information can be represented as portable JSON artefacts and evaluated through a lightweight, inspectable validator against a repeatable synthetic university research-governance scenario. The tested implementation returned the intended outcome across 21 automated regression tests, including schema conformance, negative cases and boundary conditions.

The most important qualification is equally clear. **Structural legibility is not institutional legitimacy.** The artefacts make an asserted authority relationship inspectable; they do not themselves establish that its origin is authentic or that a university must recognise it. That distinction gives the research a defensible boundary and points to the evidence and adoption work that any downstream implementation would require.

Within the funded v0.1 scope, Phase 3 is sufficiently evidenced for research reporting. Final release, archival publication and project close-out remain the next steps.

---

### Reproducibility and public research record

- [Merged Phase 3 implementation PR #6](https://github.com/Sugarlicks/silt-identity-core/pull/6)
- [AUT CISRC implementation profile](https://github.com/Sugarlicks/silt-identity-core/tree/main/docs/implementation-profiles/aut-cisrc)
- [Example artefacts and test record](https://github.com/Sugarlicks/silt-identity-core/tree/main/examples/aut-cisrc-research-delegation)
- [Reference validator](https://github.com/Sugarlicks/silt-identity-core/tree/main/reference/validators/aut-cisrc-delegation)
- [Final 21-test CI evidence](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516)

**Acknowledgement:** This project has received financial support from Stichting Vietsch (Vietsch Foundation) for open research and development benefiting research and education infrastructure.
