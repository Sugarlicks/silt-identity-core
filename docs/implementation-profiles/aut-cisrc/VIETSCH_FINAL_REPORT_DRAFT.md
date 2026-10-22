# Vietsch Foundation — SILT Core v0.1 final technical and publication report

**Draft for final close-out — DOI supplied by depositor; verify Zenodo files/licences and financial costs before submission**  
**Report date:** 23 October 2026 (NZ)  
**Agreement:** Signed MoU dated 28 April 2026 (Gareth Farry signature), Annex I  
**Project:** Delegation and Revocation Semantics for Federated Research Infrastructure  
**Project lead:** Gareth Farry  
**Funding body:** Stichting Vietsch (Vietsch Foundation)  
**Agreement reservation:** €20,000 (not proof of payment)

## Project objectives

The signed MoU and its Annex I set four technical goals: formalise delegation/revocation semantics, define machine-readable JSON Schemas, implement a lightweight scope/expiry/revocation validator, and test the model through a constrained research workflow. The MoU also requires open licensing and public progress reporting; Annex I specifies GitHub and Zenodo publication, dissemination and a final public release.

## Technical outcomes

The original SILT Core v0.1 specification (publicly released on 14 April 2026 before the signed grant) supplied historical semantics for explicit delegation, duration, scope, revocation and non-reliance. The funded pilot developed a separate non-normative AUT CISRC research-infrastructure implementation profile, including five machine-readable schemas (authority chain, delegation, request, revocation, validation result), a reference Python validator, illustrative synthetic inputs and a bounded evaluation protocol.

Phase 3 restored missing synthetic fixtures, strengthened structural issuer/revoker-chain validation, integrated JSON Schema validation and defensive malformed-input handling, and expanded the executable regression suite. **21 of 21 selected tests passed**, verified through GitHub Actions. The evaluation records that the pilot establishes reproducible *internal* rule evaluation, not that the underlying authority claims are true, legally valid, institutionally approved or cryptographically authenticated. Profile schema objects differ from the original archived v0.1 Core JSON Schemas.

## Public outputs

- Historic v0.1 Core release: https://github.com/Sugarlicks/silt-identity-core/releases/tag/v0.1
- Funded pilot GitHub release: https://github.com/Sugarlicks/silt-identity-core/releases/tag/aut-cisrc-v0.1-pilot-2026
- Curated 48-file ZIP and checksum attached to the pilot release
- Automated test evidence: https://github.com/Sugarlicks/silt-identity-core/actions/runs/39859824052
- Technical evaluation: https://github.com/Sugarlicks/silt-identity-core/blob/main/docs/implementation-profiles/aut-cisrc/phase-3-pilot-evaluation.md
- Public progress/status: https://github.com/Sugarlicks/silt-identity-core/blob/main/docs/implementation-profiles/aut-cisrc/VIETSCH_PUBLIC_STATUS.md
- **Zenodo record supplied by depositor 23 October 2026:** https://zenodo.org/records/23579725
- **Zenodo DOI supplied by depositor:** https://doi.org/10.5281/zenodo.23579725
- **Independent verification outstanding:** deposited filenames, checksum, displayed licence metadata and Zenodo publication date
- **Dissemination announcement: TO VERIFY URL AND DATE**

## Licensing and responsible attribution

The project lead approved additional CC BY 4.0 licensing for specific author-owned narrative files, retaining historical Apache permissions; the pilot code and machine-readable implementation artefacts remain Apache 2.0. The archive includes a licence notice specifying the file-level boundary. The five PNG diagrams have been excluded from the curated archive pending provenance and rights confirmation. All output remains non-normative and uses a synthetic university authority chain, with no claim of formal AUT certification.

## Delivery assessment

The four technical goals are evidenced at the scope of a constrained synthetic proof-of-concept. The funded work should **not** be described as deployment in a production research infrastructure or live federated cross-university pilot. A Zenodo record URL and DOI have been supplied by the depositor. Final publication reconciliation requires independent inspection of deposited filenames, checksum and displayed licences, plus a dissemination notice.

## Expenditure and donation reporting

The MoU provides for a reservation up to **€20,000** to support *research and development costs invested in the Project*. It permits donation claims for up to six months after the **proposed project end**; actual claims should list research costs invested. This is a charitable donation arrangement, **not an employment or procurement contract**.

Previous donation requests: **€4,500 on 23 June 2026** and **€5,500 on 4 August 2026**. Together they total €10,000 **requested**, not necessarily paid. **No Claim #3 amount is determined** without actual cost ledger and receipt/payment reconciliation. Do not include private bank account data in public reporting.

## Open close-out conditions

1. Check the supplied Zenodo record against the curated ZIP, SHA-256, publication date and mixed-licence notes; DOI: https://doi.org/10.5281/zenodo.23579725.
2. Confirm dissemination write-up and public project status URL.
3. Reconcile actual eligible R&D costs, prior amounts *received* versus merely requested, and any remaining claim.
4. Complete the public final status update and any courtesy notice to Vietsch.

**Project acknowledgement:** The open research and publication were supported by Stichting Vietsch (Vietsch Foundation).
