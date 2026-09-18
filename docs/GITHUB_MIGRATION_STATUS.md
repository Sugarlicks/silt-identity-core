# GitHub migration status — SILT Core v0.2 RC2.1

**Date:** 18 September 2026  
**Repository:** https://github.com/Sugarlicks/silt-identity-core  
**Branch:** `release/v0.2-rc2.1`  
**Draft pull request:** #4

The release branch replaces conflicting v0.1-era top-level framing with the v0.2 encounter architecture while preserving historical material rather than rewriting it. Superseded generic v0.1 Core material is moved under `archive/v0.1/`.

AUT CISRC remains a SILT Core v0.1 implementation profile. Its earlier `candidate-v0.2-findings.md` note is preserved as `historical-pre-v0.2-findings.md`; it is not a migration plan.

The branch also introduces the v0.2 governance, contribution, licensing, IPR, citation, trademark/conformance and ecosystem-positioning documents. v0.2 narrative material is separated from historical v0.1 licensing so that the new CC BY 4.0 documentation licence does not silently relicense the preserved Apache 2.0 v0.1 material.

The rights chain for v0.2 is now explicit: **Gareth Farry is the author and copyright holder; SILT Core is the project/publishing identity.**

The canonical specification is now published as a single repository artefact at `spec/SILT_Core_v0.2.0_Semantic_Architecture.md`. The complete conformance suite is present and repository CI has passed against 4 base fixtures and 30 adversarial variants.

The pull request remains deliberately **draft** pending final project sign-off. After sign-off, the remaining steps are merge, `v0.2.0` tag, archival deposit, DOI minting and insertion of the DOI into final citation metadata.
