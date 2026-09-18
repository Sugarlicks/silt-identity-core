# Roadmap

This roadmap reflects SILT Core’s deliberate specification-first posture and the current transition from semantic design into release, conformance and implementation work.

The controlling v0.2 semantic reference is:

[`spec/v0.2/semantic-architecture.md`](../spec/v0.2/semantic-architecture.md)

The canonical v0.2 seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

SILT Core remains **semantically thick and operationally thin**. The roadmap should not be used to pull authentication, credential transport, dynamic authorisation, capability machinery or execution systems into Core merely because implementation work becomes more concrete.

---

## Current release position

### v0.1 — Initial public specification

Released.

v0.1 established the first public SILT Core framing, early semantic objects, schemas, misuse cases and reference implementation experiments.

It remains historically important and operationally relevant for work that began against that architecture.

In particular, the **Vietsch / AUT CISRC research-delegation implementation remains a SILT Core v0.1 implementation to completion**. It will not be rewritten mid-stream as a v0.2 implementation.

A later migration analysis may compare the completed v0.1 implementation against v0.2, but that is separate work.

### v0.2 — Freeze Candidate 1

SILT Core v0.2 is at **Freeze Candidate 1**. Repository reconciliation, external review, conformance packaging and validation, migration documentation, release-level licensing classification, release notes and citation/archive metadata preparation are complete.

The pre-freeze gate has been completed through four worked encounters, machine-readable conformance validation and an experimental adjacent-protocol mapping. No new Core primitive was required by that gate. The external reviewer found no BLOCKER or MAJOR issue requiring FC2.

The current task is therefore publication mechanics: website cut-over, merge to `main`, final link verification, release dating, tag, GitHub release and Zenodo/DOI publication. It is not further open-ended semantic modelling.

---

## FC1 release work completed

The following work is complete on the FC1 branch and should not be treated as an open release gap.

### 1. Repository reconciliation

- FC1 is the unambiguous controlling v0.2 semantic reference;
- README, overview, positioning, roadmap and governance-facing documentation are aligned;
- active v0.1 material that conflicts with v0.2 has been removed or explicitly archived;
- `Status`, universal `Capacity`, older `Lex/Profile` language and old validation assumptions no longer appear as current Core architecture;
- historical v0.1 implementation material is distinguished from v0.2 normative material.

### 2. Conformance packaging and validation

The pre-freeze pressure-test material is installed in the release structure:

- WE01 — Transferable Instrument Encounter;
- WE02 — Credential-Carried Institutional Encounter;
- WE03 — Plural / Collective Encounter;
- WE04 — Recursive AI Delegation Encounter;
- machine-readable fixture schema;
- normalised fixtures;
- conformance validation material;
- corrected experimental SILT ↔ LCP mapping.

The machine-readable fixture schema is **test notation**, not a normative SILT wire format.

A reproducible GitHub Actions validation workflow now validates the fixture schema, WE01–WE04, manifest inventory, internal reference consistency and the FC1 basis of the experimental LCP mapping. The final release-candidate run passed.

### 3. Migration documentation

The v0.1 → v0.2 migration and repository-reconciliation record is published and covers, at minimum:

- removal of `Status` from Core;
- removal of universal `Capacity` from Core;
- Source-grounded relational Standing;
- Presentation as the encounter projection;
- Profile Expression replacing older Lex/Profile framing;
- strict semantic outcomes: `SATISFIED`, `NOT_SATISFIED`, `INDETERMINATE`;
- deliberate non-expression outside the outcome model;
- Technical Capability distinct from Authority;
- Delegation represented through Action and derived Authority;
- Obligation as a first-class persistent relational state;
- Binding as a downstream effect;
- multiple Profile Expressions without universal precedence or silent aggregation;
- semantic continuity distinct from cryptographic continuity.

### 4. Governance, licensing and IPR

The v0.2 release-level licensing boundary is defined in [`LICENSING.md`](../LICENSING.md): **CC BY 4.0** for the canonical specification and human-readable documentation, and **Apache License 2.0** for reference code and implementation-oriented machine-readable artefacts.

That licensing classification is completed FC1 release work. The broader Governance & IPR framework remains outstanding.

Before substantive external contribution and adoption expand, remaining institutional work should include:

- contributor rights and contribution terms;
- patent/IPR and any standards-essential patent commitments;
- trademark, certification, assurance and endorsement policy;
- longer-term change-control and maintainer authority;
- standards-body and working-group participation terms;
- stewardship continuity;
- clear commercial and partnership boundaries where official SILT status or representation is involved.

Scope discipline for future Core changes is already reflected in the current governance and contribution material and should remain a continuing governance requirement.

This is institutional infrastructure, not semantic expansion.

### 5. Release, citation and archive preparation

The following release material is now prepared:

- `CHANGELOG.md` with a `v0.2.0 — Unreleased` entry;
- versioned v0.2 release notes;
- external-review brief and final disposition record;
- final machine-readable validation record;
- `CITATION.cff` for v0.2.0 citation metadata;
- Zenodo/archive metadata plan under `docs/release/v0.2-zenodo-metadata.md`;
- Apache 2.0 and CC BY 4.0 release notices under `LICENSES/`.

Publication-derived values such as the release date, DOI, concept DOI and tagged release commit SHA remain intentionally unset until the release exists.

---

## Remaining release and archive work

Before and at the v0.2.0 release:

- update the public website to v0.2 before or atomically with the release announcement;
- merge `release/v0.2-fc1` to `main`;
- confirm release links resolve correctly from `main`;
- replace `Unreleased` in `CHANGELOG.md` with the release date;
- add final publication-derived citation/archive fields when known;
- create the `v0.2.0` tag;
- publish the GitHub release;
- publish the Zenodo archive and DOI record;
- preserve the tagged release commit SHA and release checksum/manifest where practical.

Repository description and homepage metadata are already aligned with v0.2.

---

## Post-freeze implementation priorities

Once v0.2 is released, the project should move decisively towards implementation, institutional placement and real encounter testing.

### Real collective-authority encounter

A high-priority next step is a real collective or customary encounter in which Source-grounded Standing, Presentation, representational Authority and Profile Expression are tested with the originating community rather than only in synthetic fixtures.

This should test whether the architecture remains legible without requiring the community to restate its ontology in system-native terms.

### Private ordering

The worked transferable-instrument encounter pressure-tested important private-ordering semantics, but it is not identical to a broader non-state trust or private-ordering encounter.

A post-freeze worked implementation should test trusts, private agreements, arbitral conditions or comparable non-state ordering without reopening Core unless a genuine semantic gap appears.

### AI-agent implementation

Recursive delegation should now be tested against real agent/capability infrastructure while preserving the boundary:

> **Technical Capability ≠ Authority**

The implementation question is how SILT semantic lineage and constraints are carried into downstream capability and execution systems, not whether SILT should duplicate them.

### Institutional implementation

Institutional delegation remains an important implementation domain, including AUT CISRC.

However, the funded Vietsch/AUT implementation remains v0.1 to completion. A v0.2 institutional implementation or migration should be treated as a subsequent phase, not folded into the current funded work.

---

## Adjacent standards and ecosystem work

A major post-release task is to document the layer boundary between SILT and adjacent systems.

Priority mappings include:

- DID / VC infrastructure;
- UCAN and zcap capability systems;
- GNAP and dynamic authorisation;
- KERI / ACDC;
- agent identity and mandate systems;
- trust registries and issuer lists;
- electronic transferable-record frameworks including MLETR and the UK electronic-trade-document regime;
- Legal Context Protocol and related legal/agent protocol work.

The purpose of this work is not to claim that every adjacent system is either a competitor or an implementation of SILT.

The relevant questions are:

- what layer does the system occupy;
- what SILT semantics can it carry or evidence;
- what operational function does it perform downstream;
- where does it overlap;
- where might it accidentally collapse Source-grounded meaning into technical verification or system-issued authority?

These mappings belong in companion material unless they expose a genuine Core defect.

---

## Institutional and standards pathway

The v0.2 release should be used to support external engagement with standards, digital identity, plural-governance and agent-infrastructure communities.

The project should prioritise contexts where SILT’s distinct contribution can be tested rather than merely described.

Likely pathways include:

- standards and trust-framework working groups;
- institutional pilots;
- Indigenous and collective-authority encounters;
- digital commerce and private-ordering implementations;
- AI-agent authority and delegation work;
- research publications and implementation partnerships.

Institutional placement should not require SILT to collapse into another stack’s ontology in order to participate.

---

## Conformance and assurance

The v0.2 conformance work creates the basis for future assurance, but SILT should not rush into certification before the implementation evidence is strong enough.

Near-term conformance work should focus on:

- machine-readable fixtures;
- test runners;
- semantic non-inference tests;
- implementation guidance;
- worked encounter expansion;
- distinguishing semantic conformance from runtime enforcement.

Future assurance, certification, training or validator services may become commercially and institutionally important. They should be built on a stable public semantic specification rather than allowed to distort Core in order to create a product surface.

---

## What should not move into Core by default

The following remain implementation or companion concerns unless future evidence shows that a semantic distinction is genuinely missing:

- wallets;
- blockchains;
- credential formats;
- authentication protocols;
- key-management systems;
- capability-token formats;
- runtime policy engines;
- access-control systems;
- registries;
- transport protocols;
- production agent frameworks;
- universal conflict-of-laws rules;
- universal Profile Expression precedence;
- universal Binding rules;
- production certification machinery.

Scope discipline is a feature of the architecture.

---

## Reopening Core after v0.2

After semantic freeze, a request to change Core should meet a high threshold.

A new Core primitive or architectural change should not be introduced merely because:

- an implementation prefers a different data model;
- another standard uses a familiar noun;
- a validator would be easier to code;
- a particular platform expects a certain credential or role structure;
- one jurisdiction or institution treats a concept as universal within its own system.

Core should be reconsidered only where implementation or encounter evidence shows a recurring semantic distinction that cannot be expressed faithfully through the existing architecture without material distortion.

Changes after release should be handled transparently through errata or a subsequent version, not through silent revision of v0.2.

---

## Guiding direction

The work now changes character.

The principal challenge is no longer to keep adding semantic objects. It is to demonstrate that the architecture survives contact with real institutions, communities, private arrangements, AI systems and adjacent standards while remaining thin enough not to absorb their machinery.

> **Source → Standing → Presentation → evaluation at the encounter**
>
> **semantic hand-off, not semantic surrender**
