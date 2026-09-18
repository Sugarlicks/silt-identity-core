# SILT Core v0.2.0 release-day procedure

**Target public release:** 23 September 2026, Aotearoa New Zealand  
**Release:** `v0.2.0`

The release branch is intended to be frozen before release day. No semantic changes should be made on release day unless a concrete blocking defect is discovered.

## Before release day

The following must already be true:

- the canonical specification is `spec/SILT_Core_v0.2.0_Semantic_Architecture.md`;
- Gareth Farry is recorded as author and copyright holder;
- SILT Core is recorded as the project / publishing identity;
- the conformance suite passes with 4 base fixtures and 30 adversarial variants;
- the evaluation outcome vocabulary is limited to `SATISFIED`, `NOT_SATISFIED`, `INDETERMINATE`;
- AUT CISRC remains explicitly versioned as a SILT Core v0.1 implementation profile and is not part of the v0.2 migration or conformance claim;
- licensing, governance, IPR, citation, security, ecosystem-positioning and conformance-claim documents are present;
- temporary segmented specification and conformance source parts are absent from the public release tree;
- `CITATION.cff` and `.zenodo.json` contain the 23 September 2026 release metadata;
- PR #4 is review-complete and ready to merge.

## Release-day action 1: publish the immutable GitHub release

1. Confirm PR #4 still points to the reviewed release head and CI is green.
2. Merge PR #4 to `main` without further semantic edits.
3. Create tag `v0.2.0` from the resulting `main` commit.
4. Create the GitHub release titled **SILT Core v0.2.0 — Semantic Architecture** using the prepared release notes.
5. Record the tag commit SHA.

The tag is the immutable public source for the archived release.

## Release-day action 2: archive and mint the DOI

1. Archive the `v0.2.0` GitHub release in Zenodo.
2. Mint the version DOI.
3. Update the living repository citation metadata (`CITATION.md`, `CITATION.cff`, README if useful) with the DOI.
4. Do not rewrite or move the tagged `v0.2.0` release merely to insert the DOI. The DOI update belongs to the post-tag living repository unless the archival service supplies a reserved DOI before publication.

## Release statement

> SILT Core v0.2.0 establishes a semantic architecture for moments of encounter between participants and systems grounded in different legal, customary, cultural, private, institutional or technical orders. Its canonical seam is Source → Standing → Presentation → evaluation at the encounter. The release enables relevant relational legitimacy to become mutually legible without requiring originating orders to collapse into a single ontology or surrender their own sources of authority.

## Freeze rule

After `v0.2.0`, further Core semantic changes belong to a subsequent version and require a concrete conformance, implementation or external-mapping failure that exposes an otherwise inexpressible semantic distinction.
