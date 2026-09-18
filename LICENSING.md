# SILT Core — Licensing Boundary

**Status:** v0.2 FC1 release licensing note  
**Purpose:** Establish the v0.2 release licensing boundary between the public SILT specification/documentation and implementation-oriented code and machine-readable artefacts.

This file defines the licensing structure for the SILT Core v0.2 release. It does not alter SILT Core semantics.

The repository has historically carried a root Apache License 2.0. That licence remains relevant to material previously distributed under it. The v0.2 release introduces a clearer forward-looking distinction between specification/documentation and implementation-oriented material.

## 1. Licensing model

SILT Core uses two principal licences:

- **Creative Commons Attribution 4.0 International (CC BY 4.0)** for the public semantic specification and human-readable documentation;
- **Apache License 2.0** for reference code and implementation-oriented machine-readable artefacts.

Release licence notices are packaged under [`LICENSES/`](./LICENSES/):

- [`LICENSES/CC-BY-4.0.txt`](./LICENSES/CC-BY-4.0.txt) identifies the CC BY 4.0 licence, SPDX identifier and canonical Creative Commons legal code;
- [`LICENSES/Apache-2.0.txt`](./LICENSES/Apache-2.0.txt) contains the Apache License 2.0 terms.

The historical root [`LICENSE`](./LICENSE) remains the Apache License 2.0 text and is retained for continuity with earlier releases.

The purpose of this split is straightforward: the semantic specification should remain openly readable, quotable, teachable, adaptable and implementable, while code and code-like artefacts should use a software licence with familiar implementation and patent terms.

This licensing structure does not make implementation code normative. Normative status is determined by the specification and governance hierarchy, not by licence type.

## 2. CC BY 4.0 material

Unless a file carries a more specific notice, the v0.2 release position is that the following human-readable material is licensed under **CC BY 4.0**:

- `spec/v0.2/**`;
- human-readable material under `docs/**`;
- `README.md`;
- `POSITIONING.md`;
- `GOVERNANCE.md`;
- `CONTRIBUTING.md`;
- `SECURITY.md`;
- `CODE_OF_CONDUCT.md`;
- human-readable migration notes, roadmaps, threat models, design principles and explanatory material;
- human-readable worked encounters, conformance notes and test explanations when added to the v0.2 release structure;
- diagrams and other documentation assets whose function is explanatory rather than executable, unless a third-party notice says otherwise.

The canonical SILT Core v0.2 Semantic Architecture is therefore licensed under CC BY 4.0 for the v0.2 release.

The canonical legal code is identified in [`LICENSES/CC-BY-4.0.txt`](./LICENSES/CC-BY-4.0.txt).

## 3. Apache 2.0 material

Unless a file carries a more specific notice, the following implementation-oriented material is licensed under the **Apache License 2.0**:

- executable reference code under `reference/**`;
- validators, adapters, utilities, scripts and software test runners;
- JSON Schemas and other implementation-oriented machine-readable schemas;
- machine-readable implementation examples and test vectors intended for direct use by software;
- machine-readable conformance fixtures and validation artefacts;
- implementation-profile schemas and executable tooling;
- other source code or code-like artefacts whose principal purpose is implementation rather than explanation.

The Apache License 2.0 text appears in [`LICENSES/Apache-2.0.txt`](./LICENSES/Apache-2.0.txt) and, for historical continuity, in the repository root as [`LICENSE`](./LICENSE).

Apache-licensed reference code and machine-readable artefacts remain non-normative unless the SILT specification expressly states otherwise.

## 4. Mixed implementation-profile material

Implementation profiles may contain both documentation and executable or machine-readable material. Their licensing follows the function of the artefact rather than the fact that the artefacts sit within one implementation profile.

For example:

- human-readable implementation-profile documentation and diagrams are licensed under **CC BY 4.0**;
- profile validators, scripts, schemas and machine-readable examples are licensed under **Apache 2.0**.

This functional distinction applies to the existing AUT CISRC / Vietsch v0.1 implementation material as a licensing classification only. It does **not** migrate that implementation to SILT Core v0.2 or alter its v0.1 semantic basis.

## 5. Conformance material

Conformance material should not silently become a normative wire format merely because it is machine-readable.

For licensing purposes:

- human-readable worked encounters, explanations and conformance reports are licensed under **CC BY 4.0**;
- machine-readable fixtures, schemas, validation scripts and executable test artefacts are licensed under **Apache 2.0**.

The licence boundary and the normative boundary are separate questions.

## 6. Historical versions and previously granted rights

This licensing note does not purport to revoke permissions already granted for copies or versions of SILT material previously distributed under Apache License 2.0 or another applicable licence.

The v0.2 licensing structure should therefore be understood prospectively for the v0.2 release and subsequent material to which it is expressly applied.

Where third-party contributions or third-party material are present, any applicable copyright, licence, attribution or notice requirements continue to apply. Nothing in this file overrides rights that the SILT project does not hold.

## 7. Attribution

For CC BY 4.0 material, reasonable attribution should identify:

- **SILT Core** as the work or project;
- the relevant version or document where practical;
- the source repository or canonical publication location;
- any modification where the reused material has been changed.

A release-specific copyright and attribution form may be added as part of final v0.2 packaging.

## 8. Trademarks, certification and endorsement

Neither CC BY 4.0 nor Apache License 2.0 grants a right to imply SILT endorsement, certification, accreditation or stewardship status.

No licence in this repository should be read as granting rights in SILT names, logos, certification marks, assurance marks or other project identifiers beyond uses permitted by applicable law or an express trademark policy.

Permission to implement, quote, adapt or distribute SILT material is therefore distinct from permission to claim that an implementation is certified, endorsed, official or stewarded by SILT.

## 9. Commercial implementation

The open licensing of the SILT specification and reference material does not prevent commercial implementation, support, assurance, certification, training, tooling, integration, research or advisory services.

Likewise, commercial activity does not confer authority to alter the public SILT specification or represent a product or service as officially endorsed unless that status has been granted through a separate process.

## 10. Patent and contribution policy

This file does **not** establish the full SILT patent or contribution-IPR policy.

The Apache License 2.0 patent grant applies to Apache-licensed contributions according to the terms of that licence. No broader patent commitment, standards-essential patent commitment or patent non-assertion should be inferred for CC BY 4.0 specification contributions merely from publication in this repository.

Before substantive external specification contribution expands, SILT should adopt an explicit Governance & IPR framework addressing at least:

- contributor rights and contribution terms;
- specification copyright;
- patent and standards-essential IPR commitments;
- maintainer and change-control authority;
- trademark and certification policy;
- standards-body participation;
- stewardship continuity.

Until that framework is adopted, contributors and adopters should rely only on rights expressly granted by the applicable licence and any specific contribution terms.

## 11. Precedence and file-specific notices

Where a file contains an explicit licence or third-party notice, that specific notice controls for that material.

Where no more specific notice exists, this licensing boundary states the v0.2 release classification.

If the licensing treatment of an artefact is genuinely ambiguous, it should be classified explicitly before release rather than inferred from convenience or directory location alone.

---

**Release direction:** open semantic specification, open reference implementation surface, explicit normative boundaries, and separate governance for trademark, certification, patent and stewardship rights.
