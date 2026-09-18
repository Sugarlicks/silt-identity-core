# Changelog

This changelog records material changes to the public SILT Core specification and release surface.

SILT Core v0.2 is currently at **Freeze Candidate 1**. The canonical semantic reference is [`spec/v0.2/semantic-architecture.md`](./spec/v0.2/semantic-architecture.md). The v0.2.0 entry below will remain marked **Unreleased** until the release tag is created.

## v0.2.0 — Unreleased

### Architectural centre

- Reframed SILT Core around the canonical encounter seam:

  > **Source → Standing → Presentation → evaluation at the encounter**

- Repositioned SILT from a capacity-aware identity / authority layer towards a semantic architecture for encounters across plural legal, customary, cultural, private, institutional and technical orders.
- Made explicit that SILT standardises the boundary at which relevant relational meaning becomes legible. It does not standardise the originating ontology or normative substrate.
- Strengthened the project discipline of remaining **semantically thick and operationally thin**.

### Added

- **Source** as the referenced ground or provenance from which Standing, Authority, Obligation or another semantic relation derives its claimed meaning.
- **Presentation** as the bounded, encounter-specific act or envelope through which a Participant brings the minimum relevant projection of Standing, Authority or another semantic claim into an encounter.
- **Profile Expression** as a bounded, selective and non-exhaustive expression of encounter-relevant semantic conditions.
- Explicit treatment of **Evidence** as distinct from the semantic relation evidenced.
- **Obligation** as a persistent relational state distinct from Authority and from the Action or artefact that may constitute, evidence, transfer, alter or discharge it.
- Explicit distinction between **semantic continuity** and **cryptographic continuity**.
- Explicit treatment of **Technical Capability** as operational ability distinct from semantic Authority.
- Explicit support for multiple, conflicting or overlapping Profile Expressions without a universal precedence, merger or aggregation rule.
- Explicit treatment of **deliberate non-expression** where bounded expression would materially distort an encounter-relevant condition. Deliberate non-expression remains outside SILT evaluation and is not a fourth evaluation outcome.
- Normative use of the semantic outcomes `SATISFIED`, `NOT_SATISFIED` and `INDETERMINATE`.
- Clearer treatment of Profile Expression provenance and the Authority to author, adopt, maintain or contribute to an expression.
- Explicit distinction between collective Standing and representational Authority.
- Explicit treatment of Attribution as distinct from technical execution, Binding and liability.
- Explicit semantic / operational boundary language covering authentication, key continuity, credentials, capability tokens, sessions, dynamic authorisation, access control, policy execution and runtime execution.

### Changed

- **Standing** is now explicitly relational and Source-grounded rather than a universal status-like property or credential-backed state.
- **Participant** replaces the earlier foundational `Principal` framing as a deliberately thin encounter referent. SILT does not attach a universal theory of personhood, identity or legal personality to Participant.
- **Authority** is treated as bounded power relevant to an Action or class of Action and may arise through multiple formation paths recognised by the applicable Source and encounter conditions.
- **Delegation** is no longer treated as a universal Core primitive. Where relevant, delegation is represented as an Action through which derived Authority may be constituted.
- **Consent** is treated as a bounded semantic relation of agreement or permission rather than one universal consent artefact or technical assent event.
- **Reliance** is kept distinct from Authority validity and from downstream legal doctrines such as apparent authority or estoppel unless expressly introduced by the applicable conditions.
- **Revocation** is treated as affecting the relevant revocable relation without assuming one universal cascade rule. Standing has no universal SILT lifecycle.
- **Evaluation** is Profile-Expression-specific and encounter-bounded rather than a universal validity judgement.
- A receiving order may conclude that its own conditions are not satisfied without thereby creating, extinguishing or redefining the underlying Source-grounded Standing.
- Technical success, key possession, credential validity, account state, capability possession or runtime execution no longer stand in as semantic proxies for Standing or Authority.
- Binding, liability, settlement, enforceability, recognition and similar effects are treated as downstream, Profile-defined or otherwise externally determined rather than universal Core conclusions.

### Removed from universal Core

- `Status` as a SILT Core object.
- `Capacity` as a universal SILT Core primitive.
- The older `Lex/Profile` split. v0.2 uses **Profile Expression**.
- `Principal` as the foundational Core subject model.
- Delegation as a standalone universal Core primitive or artefact.
- Universal `ALLOW` / `DENY` semantics as Core evaluation results.
- Any implication that Binding is a universal consequence of successful SILT evaluation.
- Generic v0.1 root schemas for Principal, Delegation, Consent and Revocation from the active v0.2 release surface.
- The generic v0.1 Consent reference validator and obsolete empty placeholder surfaces from the active v0.2 branch.

### Conformance and pressure testing

Added a non-normative v0.2 conformance surface under `tests/conformance/v0.2/`, including four worked encounters and aligned machine-readable fixtures:

- **WE01 — Transferable Instrument Encounter**: tests changing holder-related Standing, persistent Obligation, technical control, constitutive transfer and incomplete lineage.
- **WE02 — Credential-Carried Institutional Encounter**: tests credential validity, Evidence, Standing, Authority, key rotation, conflicting credentials and selective disclosure.
- **WE03 — Plural / Collective Encounter**: tests conflicting Profile Expressions, collective Standing, representational Authority, contested expression provenance and deliberate non-expression.
- **WE04 — Recursive AI Delegation Encounter**: tests derived Authority, scope containment, semantic lineage, Revocation, Attribution and technically successful execution without semantic Authority.

The worked encounters are falsification devices rather than universal domain templates. Across the pre-freeze gate, no recurring unnamed semantic distinction was identified that required a new Core primitive.

Also added:

- a machine-readable conformance fixture schema;
- normalised WE01–WE04 fixtures;
- a conformance suite manifest;
- companion misuse-case material aligned to v0.2;
- an experimental, non-normative SILT ↔ Legal Context Protocol mapping used to test the semantic boundary against an adjacent agentic-commerce protocol.

The fixture schema and fixtures are **test notation**, not a normative SILT object model, serialisation or wire format.

### Repository and documentation

- Added the canonical repository-readable v0.2 Semantic Architecture under `spec/v0.2/`.
- Rebuilt the public README and overview around the v0.2 encounter architecture.
- Reconciled positioning, roadmap, design principles, threat model, governance, contribution and security documentation to v0.2 terminology and scope discipline.
- Added a public v0.1 → v0.2 repository migration and reconciliation record.
- Converted surviving topic-specific v0.1 specification files into explicit archival / migration notices rather than co-equal v0.2 normative sources.
- Added a substantive SILT-specific Code of Conduct.
- Added explicit normative / non-normative hierarchy across specification, companion documentation, conformance material, implementation profiles and reference code.
- Protected the Vietsch / AUT CISRC research-delegation work as a **v0.1 implementation through completion**. It is not being rewritten mid-stream to appear natively v0.2-compliant.

### Licensing and governance

- Defined the v0.2 release licensing boundary in `LICENSING.md`:
  - **CC BY 4.0** for the canonical specification and human-readable documentation;
  - **Apache License 2.0** for reference code and implementation-oriented machine-readable artefacts.
- Clarified that the licensing boundary does not itself grant certification, endorsement, trademark or stewardship rights.
- Added release-level governance and change-control language protecting the v0.2 architecture from silent reintroduction of retired objects or implementation-specific assumptions.
- Kept the broader contributor, patent / SEP, trademark, certification, assurance and long-term stewardship framework as separate institutional work rather than a reason to reopen Core.

### Migration notes for v0.1 implementers

The most significant semantic changes from v0.1 are:

- `Status` → **removed from Core**;
- `Principal` → **Participant** as a thin referent;
- universal `Capacity` → **removed from Core**;
- identity/status-centred position → **Source-grounded relational Standing**;
- `Authority Source` → **Source**;
- `Profile` / `Lex` → **Profile Expression**;
- Delegation artefact / primitive → **Action + derived Authority** where applicable;
- `ALLOW` / `DENY` → **downstream implementation decisions**, not Core semantic outcomes;
- absent or distorted expression → **deliberate non-expression may remain outside evaluation**;
- technical control / capability → **Technical Capability**, distinct from Authority;
- cryptographic continuity → **distinct from semantic continuity**;
- Binding → **downstream effect**, not universal Core conclusion.

The detailed repository reconciliation record is in [`docs/migration/v0.1-to-v0.2-repository-audit.md`](./docs/migration/v0.1-to-v0.2-repository-audit.md).

## v0.1 — 2026-04-14

Initial public SILT Core release.

The v0.1 release established the first formal public model of SILT as capacity-aware identity infrastructure between identity / credential systems and execution environments. It introduced early treatment of Capacity, Authority, Consent and Revocation, together with stack positioning, action-gating concepts, design axioms and contribution boundaries.

v0.1 remains historically important and continues to be the semantic basis for implementations that began against it, including the current Vietsch / AUT CISRC research-delegation implementation.

The v0.2 release supersedes v0.1 as the controlling SILT Core semantic architecture once `v0.2.0` is tagged, but it does not retroactively rewrite v0.1 implementations or revoke rights already granted for previously published material.
