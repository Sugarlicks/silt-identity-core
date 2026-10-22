# Zenodo deposit metadata — draft only

**Do not publish this metadata as a DOI claim until deposit completion.**  
**Deposit scope:** Vietsch-funded SILT Core v0.1 AUT CISRC delegation and revocation proof of concept; separate from SILT Core v0.2.0.

- **Proposed title:** SILT Core v0.1: Delegation and Revocation Semantics for Federated Research Infrastructure — AUT CISRC Proof of Concept
- **Creator:** Gareth Farry
- **Publication year:** 2026, subject to actual deposit date
- **Resource type:** Software / research output, depending on final archive contents and repository-to-Zenodo configuration
- **Version identifier:** To be determined from immutable final tag or commit
- **Publisher:** Zenodo (once deposited)
- **DOI:** Pending assignment; **none claimed**
- **Funding acknowledgement:** Supported by Stichting Vietsch (Vietsch Foundation)
- **Related identifier:** https://github.com/Sugarlicks/silt-identity-core
- **References:** Original signed MoU and project proposal; Phase 1 and 2 claim summaries; public implementation and evaluation records
- **Keywords:** delegated authority; revocation; research infrastructure; federated research; semantic interoperability; JSON Schema; inspectable authority chain; proof of concept

## Suggested abstract

This research release documents a constrained SILT Core v0.1 proof of concept addressing portable, inspectable delegation and revocation records for federated research infrastructure. Using a synthetic university research-governance workflow associated with the AUT CISRC implementation context, it represents an asserted institutional authority chain, limited delegation, access request, temporal conditions and revocation events as machine-readable artefacts. A lightweight Python reference validator checks the selected actor, action, resource, purpose, authority-chain, temporal and revocation conditions. The Phase 3 regression suite passed 21 selected automated tests, including representative schema-conformance and negative cases. The implementation profile is non-normative and does not establish formal AUT approval, verify the truth or legal validity of authority claims, authenticate signatures, integrate with live systems or demonstrate multi-institution deployment. The publication offers reproducible research artefacts for independent inspection and further evaluation.

## Rights preflight

The signed MoU calls for **Apache 2.0 source code and Creative Commons non-code materials**. The repository's current licensing file describes preserved v0.1 historical materials as Apache 2.0 unless otherwise specified. **Resolve this conflict explicitly with the rights holder and version-specific licence notices before applying deposit licences.** Do not claim that the present metadata automatically grants a new licence or revokes earlier Apache 2.0 terms.

## Required deposit steps

- Determine and verify canonical v0.1 specification file.
- Confirm precise archive contents, licence notices and checksum/commit.
- Create or select the immutable v0.1 pilot-specific GitHub release/tag.
- Deposit the exact corresponding archive into Zenodo.
- Verify the assigned version DOI and download files match the release.
- Insert DOI and actual publication date into the evaluation/reporting material.
- Publish a short dissemination announcement linking both archival and source records.

**Not a v0.2 archival supplement.** The existing v0.2 DOI must not be reused as the v0.1 deposit identifier.
