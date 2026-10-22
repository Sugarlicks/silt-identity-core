# Zenodo deposit hand-off — curated Vietsch SILT v0.1 pilot

**Prepared:** 23 October 2026 (NZ)  
**Deposit status:** Instructions and proposed metadata only. **No DOI has been minted or verified here.**

## Why manual upload

The GitHub repository includes later **SILT Core v0.2** material in its default source snapshot. The funded research output is the separate, curated 48-file **v0.1 AUT CISRC pilot** package. Zenodo's automatic GitHub integration may ingest a source snapshot of the *whole* tagged repository rather than only the release ZIP. For fidelity of the deposited research object, manually upload the **curated ZIP** from the published GitHub release and retain its manifest and checksum.

## Files to upload

1. [Curated ZIP — `silt-vietsch-aut-cisrc-v01-pilot.zip`](https://github.com/Sugarlicks/silt-identity-core/releases/download/aut-cisrc-v0.1-pilot-2026/silt-vietsch-aut-cisrc-v01-pilot.zip)
2. [External SHA-256 checksum — `silt-vietsch-aut-cisrc-v01-pilot.zip.sha256`](https://github.com/Sugarlicks/silt-identity-core/releases/download/aut-cisrc-v0.1-pilot-2026/silt-vietsch-aut-cisrc-v01-pilot.zip.sha256)

The ZIP itself includes `RELEASE_MANIFEST.json` with SHA-256 for each included file. Do **not** substitute either GitHub's automatically generated whole-repository source ZIP or the original `v0.1` historical release.

## Suggested metadata

- **Title:** SILT Core v0.1: Delegation and Revocation Semantics for Federated Research Infrastructure — AUT CISRC Research Pilot
- **Creator:** Gareth Farry
- **Resource type:** Software (research proof of concept with documentation)
- **Version:** `aut-cisrc-v0.1-pilot-2026`
- **Publisher:** Zenodo
- **Date:** Actual Zenodo publication date (do not backdate)
- **Keywords:** delegation; revocation; federated research infrastructure; semantic interoperability; university governance; JSON Schema; Python validator; reproducible research
- **Related identifier:** https://github.com/Sugarlicks/silt-identity-core/releases/tag/aut-cisrc-v0.1-pilot-2026 (is supplement to / is identical to only if accurate; generally use *is supplemented by* or *is documented by* appropriately)
- **Funding acknowledgement:** Financial support from Stichting Vietsch (Vietsch Foundation).
- **Licence:** Mixed licences; software and machine-readable implementation artefacts Apache 2.0; specifically listed Gareth Farry-authored narrative texts additionally CC BY 4.0, existing Apache permissions preserved. See `release/vietsch-v01/LICENCE_STATUS.md`. **Do not inaccurately claim a single licence applies to all files.**
- **Communities:** Optional; do not invent institutional memberships or endorsements.
- **DOI:** Zenodo assigns after deposit. Leave empty until issued.

### Abstract

This record preserves a constrained SILT Core v0.1 research proof of concept addressing inspectable delegation and revocation semantics within federated research infrastructure. A synthetic university research scenario associated with the AUT CISRC implementation context expresses asserted institutional authority, time-bound delegation, a scoped data-related request, and applicable revocation as JSON artefacts. A lightweight Python validator evaluates selected issuer-chain, delegate, action, resource, purpose, time and revocation conditions. The expanded automated regression suite passed 21 selected tests, including positive and negative cases, malformed-input handling and representative JSON Schema conformance. The AUT profile is non-normative; its JSON objects are implementation-specific and not directly interchangeable with the original archived v0.1 Core schemas. Neither the tests nor the synthetic chain establish formal AUT institutional approval, cryptographic proof of authority, live IAM integration or interoperability across operational universities. This record documents the implementation and its research limitations separately from the historical SILT v0.1 release and the subsequent v0.2 Semantic Architecture.

## Deposit actions

Open [Zenodo's new upload page](https://zenodo.org/uploads/new), sign in, upload the two files listed above, enter/review the metadata and mixed-licence disclosure, and publish the deposit. Verify that the published record lists the expected exact file names and archive size/checksum, then record the real version DOI and date in the [public status](VIETSCH_PUBLIC_STATUS.md), [Phase 3 evaluation](phase-3-pilot-evaluation.md), final Vietsch report and any dissemination announcement.

**Publication safeguard:** If a Zenodo GitHub-linked record appears for the full repository, review its files before treating it as the curated pilot archive. Avoid two competing deposits for the same file set unless the relationship is clearly recorded.

No deposit, DOI reservation or final claim submission is performed by this instruction document.
