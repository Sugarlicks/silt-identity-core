# Vietsch v0.1 licensing reconciliation — decision record

**Status:** Proposed resolution; rights-holder review required before final archival licences are represented as settled.  
**Date:** 23 October 2026.

## Documentary basis

The signed Vietsch MoU says:

> The source code of the Project shall be made publicly available under Apache 2.0 license, or any later version. Information other than source code shall be made publicly available as Creative Commons.

The repository's existing `LICENSING.md` says archived v0.1 and preserved AUT CISRC implementation-profile material retain **Apache License 2.0**, unless individually specified otherwise. Historical `archive/v0.1/LICENSE` contains the Apache 2.0 licence text.

The agreement specifies **Creative Commons** for non-code information, but it does not identify a particular Creative Commons variant. **CC BY 4.0 is a proposed choice, not a term stated verbatim by the MoU.**

## Proposed resolution subject to review

1. **Do not revoke or purport to withdraw** historical Apache 2.0 permissions already granted.
2. Keep Python validator and other program source code under Apache 2.0. Treat JSON Schemas and executable fixtures as machine-readable implementation artefacts, noting that the agreement does not itself spell out their precise categorisation.
3. For project-authored narrative reports/specification materials to which the rights holder controls all relevant rights, consider offering **CC BY 4.0 alongside existing Apache 2.0 permission**, with an explicit file or package notice identifying dual licensing. Do not claim this is already in force until approved and recorded.
4. Check contributor rights and external material separately before adding CC permissions; third-party copyright is unaffected.
5. Use a separate metadata field or per-file notice for the mixed-licence Zenodo archive rather than falsely describing every file as solely CC BY or solely Apache.
6. Keep the repository's existing v0.2 licence and version identity untouched.

## Open decision

The project lead/rights holder should explicitly authorise the v0.1 publication licence map and decide whether **CC BY 4.0** is the intended Creative Commons option. The final release should include an updated file-specific notice and an accompanying licence inventory. This working paper **does not itself grant a new licence**.

## Scope

This decision applies only to the funded v0.1 research/pilot archival package; no changes to normative SILT Core v0.2 are proposed.
