# Experimental Semantic Mapping

_Non-normative interoperability experiment • 17 September 2026 • Pre-freeze review artefact_

Canonical SILT basis: SILT Core v0.2 Semantic Architecture, Freeze Candidate 1 (FC1), derived from RC4.1 pre-freeze stress-test revision.

Architecture-basis verification: Rechecked against RC4.1/FC1 after completion of the pre-freeze worked encounters. No mapping verdict changes. RC4.1-specific additions concerning deliberate non-expression and the INDETERMINATE/non-expressibility split are not relied upon by the LCP mapping. The technical-artefact/Authority clarification reinforces, rather than changes, the existing Technical Capability ≠ Authority conclusion. The Profile-Expression-specific evaluation rule directly strengthens the plural-treatment finding: seller-side and buyer-side conditions must remain separately evaluated unless an expressed composition rule applies.

**LCP basis:** Public LCP v1 materials reviewed on 17 September 2026, including the public repository, schema, examples, Level 4 guidance and launch materials.

## 1. Executive finding

The mapping does not break SILT Core v0.2 and does not justify reopening a Core primitive. LCP is a credible adjacent protocol with real semantic overlap, but it is not an alternative formulation of SILT. The strongest overlaps are around encounter conditions, Evidence, signing/acceptance Actions, agent constraints and downstream recourse. The most important non-overlaps are Source, Standing, SILT Reliance, persistent Obligation and Authority-mediated Attribution.

The central architectural finding is that LCP cannot be placed wholly “above” or “below” the Presentation line. It spans several layers. Seller terms and buyer-side policy constraints can contribute encounter conditions; hashes and signatures are evidentiary/technical mechanisms; key gating and protocol adapters are operational; dispute-resolution, returns and API hooks are downstream institutional hand-off. The correct SILT integration is therefore field-level and semantic, not protocol-level substitution.

The most important semantic tension is Consent. LCP describes Level 3 signed acceptance as cryptographic proof of explicit consent and its Level 1 examples describe proceeding after discovery as implicit consent. SILT Core is deliberately stricter: assent, signature or proceeding may provide Evidence concerning Consent, but are not universally equivalent to Consent. A SILT-LCP adapter must preserve that distinction rather than import LCP’s narrower agentic-commerce assumption as a universal SILT rule.

## 2. LCP surface being mapped

The current LCP public model is intentionally compact. A service exposes a legal-context.json document at a well-known URL. The only required field is a terms URL. Optional fields add a terms format, a SHA-256 atrHash, an acceptanceRequired flag, dispute-resolution metadata, returns/contact endpoints and a richer legal-context API. LCP also describes a buyer-side policy model for minimum trust level, acceptable jurisdictions, acceptable dispute methods, commitment caps and signing thresholds, including human-review gating above specified thresholds.

Its four advisory trust levels move from discoverable terms (Level 1), to hash-verifiable terms (Level 2), to signed acceptance (Level 3), to integrated legal/recourse infrastructure (Level 4). LCP also defines integration surfaces for agentic-commerce, payment and agent protocols rather than attempting to replace those rails.

## 3. Layer placement

A whole-protocol statement such as “LCP sits below SILT” is too crude. The mapping is more accurate when decomposed by construct:

```text
Originating legal / commercial / organisational orders  
|  
| selective encounter expression  
v  
Seller terms projection / Buyer policy semantic constraints  
| |  
+---- may contribute to PROFILE EXPRESSION(s)  
  
SOURCE -> STANDING -> PRESENTATION -> EVALUATION AT THE ENCOUNTER  
^ |  
| +--> semantic result / Attribution  
LCP hash, signature, ----+ |  
mandate metadata, v  
terms reference downstream effect / recourse  
(Evidence / carrier) (LCP Level 4 hooks)  
  
Signing keys, protocol adapters, payment rails, key gating  
= operational machinery below the Presentation line architecturally  
(though it may operate before, during or after a Presentation)
```

## 4. Concept-by-concept mapping

| **SILT concept**            | **LCP construct**                                                                                      | **Relationship**           | **SILT treatment**                                                                                                                                                                                                                                                                                                                                                                 | **Semantic-loss risk**                                                                 |
|-----------------------------|--------------------------------------------------------------------------------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Participant                 | Buyer, seller/service, agent, principal, dispute-resolution actor                                      | PARTIAL                    | LCP supplies encounter roles. SILT keeps Participant deliberately thin and does not infer personhood, legal identity or legitimacy from the role label.                                                                                                                                                                                                                            | LOW                                                                                    |
| Source                      | No direct first-class equivalent                                                                       | NO EQUIVALENT              | Terms, mandates, entity attestations or organisational records may provide Evidence concerning Source, but LCP does not model the relational ground from which Standing or Authority arises.                                                                                                                                                                                       | HIGH if a terms publisher or identity artefact is silently treated as universal Source |
| Standing                    | No direct first-class equivalent                                                                       | NO EQUIVALENT              | LCP is primarily concerned with legal context of a transaction, not the Participant's Source-grounded relational position. Standing should remain a SILT semantic input where relevant.                                                                                                                                                                                            | HIGH if identity or participation is treated as Standing                               |
| Profile Expression          | Seller/service legal-context.json + referenced terms                                                   | PARTIAL / CARRIER          | The referenced terms can supply encounter-relevant conditions and may instantiate or contribute to a Profile Expression. The discovery JSON is better treated as a carrier/index unless it itself expresses the relevant conditions. Neither exhausts the originating legal or commercial order.                                                                                   | MEDIUM                                                                                 |
| Profile Expression          | Buyer Policy                                                                                           | PARTIAL                    | Acceptable jurisdictions, dispute methods, commitment caps and signing thresholds are strong candidates for encounter conditions. Operational key-gating and human-review mechanics remain below the Presentation line.                                                                                                                                                            | MEDIUM because one LCP construct mixes semantic constraints with operational controls  |
| Presentation                | Transaction-time legalContext reference, terms reference, signed acceptance, mandate-linked metadata   | PARTIAL / CARRIER          | LCP artefacts can carry part of a SILT Presentation, but do not define Presentation. A SILT Presentation may also carry Source-grounded Standing, Authority context and non-LCP Evidence.                                                                                                                                                                                          | MEDIUM                                                                                 |
| Evidence                    | atrHash, acceptance signature, clauseId, source URL, identity/authorisation attestations               | STRONG PARTIAL             | These are natural Evidence artefacts. Hashes establish integrity/version; signatures establish a cryptographic event tied to a key/identity mechanism; clause identifiers support retrieval and verification. None alone establishes Standing, Authority, Consent or Binding.                                                                                                      | LOW if kept evidentiary; HIGH if promoted into legitimacy                              |
| Authority                   | Buyer policy constraints; agent authorisation chains in adjacent protocols; human review threshold     | PARTIAL / MOSTLY ADJACENT  | LCP assumes other protocols handle much of authorisation. SILT can evaluate the semantic Authority represented by those artefacts. Commitment caps can express Authority scope, but possession of a signing key or mandate carrier does not itself establish SILT Authority.                                                                                                       | HIGH                                                                                   |
| Consent                     | acceptanceRequired + signed acceptance; Level 1 implicit-consent guidance                              | PARTIAL / SEMANTIC TENSION | Signed acceptance is an Action and Evidence concerning Consent. SILT does not universally equate assent or signature with Consent; the relevant Source and Profile Expression determine whether the evidence is sufficient. Proceeding with a transaction may likewise be an Action from which Consent follows only where the expressed conditions make that inference legitimate. | VERY HIGH                                                                              |
| Reliance                    | No direct first-class equivalent; trust level and verification material may support reliance decisions | NO DIRECT EQUIVALENT       | LCP improves the information on which a party may choose to rely, but SILT Reliance remains the expressed conditions under which a Participant may act on a representation. Do not silently import apparent authority or reasonable reliance.                                                                                                                                      | HIGH if inferred                                                                       |
| Action                      | discover, fetch, verify hash, sign/accept, transact, file dispute, return/claim                        | PARTIAL                    | Signing, accepting and transacting are encounter-relevant Actions. Whether an Action constitutes Consent, creates an Obligation or has another effect is determined by Source and expressed conditions, not by the technical event alone.                                                                                                                                          | LOW to MEDIUM                                                                          |
| Attribution                 | Acceptance signature; agent/principal identity or mandate context                                      | PARTIAL / EVIDENCE         | LCP can provide strong evidence about the factual signer or agent context. SILT separately asks how an Action is properly attributed through Authority. Technical actor and attribution target may differ.                                                                                                                                                                         | HIGH in delegated-agent transactions                                                   |
| Revocation                  | No general first-class semantic equivalent in core discovery document                                  | NO EQUIVALENT              | Updated terms, policy changes or adjacent mandate systems may affect future transactions, but SILT Revocation remains an explicit semantic Action with scope, effective time and cascade rules where relevant.                                                                                                                                                                     | MEDIUM                                                                                 |
| Obligation                  | Obligations may be stated inside terms; no first-class persistent relational-state object              | CONTENT-LEVEL ONLY         | LCP can identify and preserve the terms that describe obligations, but it does not itself provide the SILT persistent Obligation relation or lifecycle. This is a meaningful non-overlap.                                                                                                                                                                                          | MEDIUM if document terms are mistaken for live obligation state                        |
| Binding / downstream effect | Agreement context, governing jurisdiction, dispute resolution, settlement/recourse hooks               | DOWNSTREAM / PARTIAL       | LCP is explicitly designed to make legal context and recourse discoverable and provable. SILT must not translate LCP conformance or successful signature into universal Binding. Binding remains determined by the applicable legal/private/normative mechanism.                                                                                                                   | VERY HIGH                                                                              |
| Technical Capability        | Signing key, key gating, protocol integration surfaces, payment/agent rails                            | OPERATIONAL                | These mechanisms sit below the Presentation line architecturally, although they may operate before, during or after a Presentation. Their outputs may carry, substantiate or enforce semantics, but the mechanisms themselves must not be promoted into Standing or Authority by default.                                                                                          | LOW if boundary is respected                                                           |

## 5. LCP trust levels through the SILT lens

| **LCP level**           | **Primary LCP construct**                                               | **SILT treatment**                                                                                                                 | **Critical safeguard**                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Level 1 — Informational | terms URL discoverable                                                  | Terms document can supply or carry Profile Expression conditions; URL and retrieved document are Evidence/carrier.                 | LCP examples describe proceeding after discovery as implicit consent. SILT must represent proceeding as Action and only infer Consent where the applicable expressed conditions permit it. |
| Level 2 — Provable      | atrHash                                                                 | Evidence integrity and version continuity for the referenced terms/ATR.                                                            | Hash proves document integrity/version, not legitimacy of Source, Authority of publisher, Consent or Binding.                                                                              |
| Level 3 — Signed        | acceptanceRequired + signature + buyer policy                           | Acceptance condition, Action, Evidence concerning Consent; buyer-side semantic constraints may contribute to a Profile Expression. | Signature must not be hard-coded as universal Consent; buyer key gating is operational, not a SILT semantic primitive.                                                                     |
| Level 4 — Integrated    | disputeResolution, returns, api, private terms, escrow/compliance hooks | Mix of encounter conditions and downstream technical/institutional hand-off.                                                       | Do not collapse dispute/jurisdiction metadata into universal Binding or treat API availability as legal effect.                                                                            |

## 6. Worked mapping: autonomous purchase encounter

This worked mapping is deliberately small. It asks how an LCP-enabled agent purchase could be represented without letting LCP redefine SILT semantics.

- Seller S publishes legal-context.json pointing to Terms T, with atrHash H, acceptanceRequired=true and a dispute-resolution clause.

- Buyer principal P has a Buyer Policy allowing specified jurisdictions and dispute methods and capping autonomous commitments at NZD 5,000. Above that amount, an additional human approval or Authority condition is required; the technical review workflow itself remains operational.

- Agent A is technically capable of signing and paying, and holds an external mandate/agent-authorisation artefact recognised by the encounter.

- Agent A proposes a NZD 2,500 purchase from S.

### 6.1 SILT interpretation

| **Encounter element**     | **SILT interpretation**                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Seller Terms T            | May contribute to seller-side Profile Expression PE-S. The terms document itself is also documentary Evidence; its full content is not assumed to equal the originating legal order.                                                                                                                                                                                              |
| atrHash H                 | Evidence that the referenced terms/ATR are the expected version and have not changed. It says nothing by itself about who had Authority to publish them or whether they are binding.                                                                                                                                                                                              |
| Buyer Policy              | Buyer-side encounter conditions PE-P to the extent it expresses semantic limits: jurisdiction, dispute method and autonomous commitment cap. A requirement for additional human approval or Authority above the cap may itself be semantic if expressed; the human-review and key-gating workflow remains operational.                                                            |
| External agent mandate    | Evidence and/or an artefact carrying or contributing to an Authority claim. SILT evaluates whether the underlying semantic Authority is current, scoped to the purchase and attributable to P; the artefact is not itself universally equivalent to Authority.                                                                                                                    |
| Signed acceptance         | Action (signing/accepting) plus Evidence concerning Consent to Terms T. Consent is SATISFIED only under a Profile Expression that actually expresses a Consent condition and where the relevant Source and expressed conditions treat that evidence as sufficient. In this worked example PE-S does; PE-P does not unless a buyer-side Consent condition is separately expressed. |
| Payment execution         | Technical/operative Action. Successful execution does not retroactively establish Authority or Consent.                                                                                                                                                                                                                                                                           |
| Dispute-resolution clause | Encounter condition and downstream recourse mechanism. LCP clauseId/source can provide integrity/retrieval Evidence; actual jurisdiction or Binding effect may be indicated by an applicable Profile Expression or otherwise determined outside Core. The Profile Expression does not manufacture that effect.                                                                    |

### 6.2 Example condition-level evaluation

| **Condition**                                           | **Profile Expression**                                              | **Expected SILT result**                                                                                                         | **Reason**                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Agent Authority to commit NZD 2,500                     | PE-P / recognised mandate conditions                                | SATISFIED                                                                                                                        | Amount is within the expressed commitment scope and no contrary revocation/dependency is present.                                                                                                                                                                                 |
| Terms version integrity                                 | PE-S                                                                | SATISFIED                                                                                                                        | atrHash H verifies the referenced terms version.                                                                                                                                                                                                                                  |
| Terms accepted by relevant Participant/authorised agent | PE-S and PE-P, evaluated separately; no aggregate or merger implied | SATISFIED under each relevant expression                                                                                         | Signed acceptance is supplied. PE-S evaluates its acceptance condition; PE-P separately evaluates whether the agent has Authority to accept and whether buyer-side conditions are satisfied. No combined result is inferred.                                                      |
| Consent to Terms T                                      | PE-S; PE-P only if PE-P expressly includes a Consent condition      | SATISFIED under PE-S where PE-S treats the evidence as sufficient; no PE-P Consent evaluation unless PE-P expressly includes one | Signed acceptance is Evidence concerning Consent. The worked Buyer Policy as stated does not itself express a Consent condition, so SILT does not manufacture a PE-P Consent evaluation. If PE-P separately expresses such a condition, it is evaluated independently under PE-P. |
| Autonomous commitment threshold                         | PE-P                                                                | SATISFIED                                                                                                                        | The NZD 2,500 purchase is within the expressed autonomous commitment scope. Any human-review workflow above the threshold is operational and is not separately evaluated in this base case.                                                                                       |
| Universal Binding                                       | None                                                                | NO SILT EVALUATION AS UNIVERSAL QUESTION                                                                                         | SILT does not convert successful semantic evaluation into binding effect everywhere.                                                                                                                                                                                              |

## 7. Adversarial pressure test

| **ID** | **Pressure test**                           | **Mapping result**                  | **Architectural finding**                                                                                                                                                                          |
|--------|---------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P1     | Signature = Consent                         | FAIL if imported universally        | No Core change. Map signature to Action + Evidence; evaluate Consent under relevant Profile Expression.                                                                                            |
| P2     | Domain publication = Authority to set terms | FAIL if inferred                    | No Core change. Profile Expression provenance and authority to express remain independently material.                                                                                              |
| P3     | Buyer Policy = single SILT object           | FAIL if copied wholesale            | Split semantic conditions from operational key-gating/human-review mechanics.                                                                                                                      |
| P4     | LCP trust level = SILT aggregate validity   | FAIL                                | Trust level is LCP assurance classification. SILT keeps condition-level evaluation separate.                                                                                                       |
| P5     | Agent signing key = Authority               | FAIL                                | No Core change. Technical Capability and Authority remain distinct.                                                                                                                                |
| P6     | Signed terms = Binding everywhere           | FAIL                                | No Core change. Binding/downstream legal effect may be indicated by an applicable Profile Expression or otherwise determined outside Core; the Profile Expression does not manufacture the effect. |
| P7     | LCP has no Source/Standing fields           | PASS as non-equivalence             | This is evidence of complementarity, not a gap SILT should remove.                                                                                                                                 |
| P8     | Terms encode live Obligation state          | PARTIAL / insufficient              | LCP preserves/document-identifies terms; SILT Obligation remains distinct persistent relational state.                                                                                             |
| P9     | Seller terms + Buyer Policy conflict        | PASS if kept plural                 | Treat as separate encounter expressions/conditions; no silent precedence without expressed ground.                                                                                                 |
| P10    | LCP integration rail executes successfully  | FAIL if treated as semantic success | Execution can follow a SILT evaluation but does not prove it.                                                                                                                                      |

## 8. What the mapping tells us about SILT Core

- No new Core primitive is required. LCP’s constructs can be represented as encounter conditions, Evidence, Actions, operational machinery or downstream effects using the current architecture.

- Profile Expression survives the test, but the mapping confirms why it must remain bounded and provenance-sensitive. A legal-context.json endpoint or published terms document cannot automatically be treated as having legitimate Authority to express an organisation’s or collective’s conditions.

- Consent survives the test precisely because SILT refuses to collapse Consent into signature. This is not pedantry: it prevents a narrow agent-commerce convention from silently becoming a universal semantic rule.

- Source and Standing remain differentiated SILT contributions. Their absence from LCP is not a deficiency in LCP; it shows the standards address different questions.

- Authority remains semantically necessary even though LCP delegates much authorisation work to adjacent agent/payment protocols. SILT’s role is to preserve the meaning and bounds of that Authority across systems.

- Obligation remains justified as first-class SILT relational state. LCP can prove which terms described an obligation, but does not itself model the persistent live relation as counterparties, performance or entitled positions change.

- Binding remains correctly downstream. LCP’s purpose is close to the place where parties care about enforceability, jurisdiction and recourse, but SILT must not universalise those effects.

- The mapping supports a field-level adapter rather than an LCP-specific construct hard-coded into Core. LCP should remain an implementation/interoperability target.

## 9. Proposed non-normative interoperability rules

- Treat LCP terms and Buyer Policy as possible contributors to Profile Expression, never as automatic equivalents of the full originating normative order.

- Treat atrHash, clauseId and signatures as Evidence with stated integrity/provenance semantics, not as legitimacy or Binding proofs.

- Represent signed acceptance as Action + Evidence concerning Consent. Evaluate Consent separately.

- Represent LCP Level 1 “proceeding” as an Action. Do not infer Consent unless an applicable expressed condition makes that inference legitimate.

- Keep signing-key gating, payment rails, protocol adapters, sessions and capability mechanisms operational.

- Where LCP buyer and seller conditions differ, preserve them as separate encounter expressions/conditions. Do not silently merge or rank them.

- Use SILT Authority and Attribution where an agent acts for a principal; a signature identifies a technical actor but does not by itself settle authority-mediated attribution.

- Treat Level 4 recourse hooks as downstream hand-off unless a specific field expresses a condition that is itself relevant to encounter evaluation.

- Do not make LCP a required SILT transport. The mapping is one interoperability binding among potentially many.

## 10. Freeze verdict

**Result: NO CORE REOPENING TRIGGERED.** The experimental mapping creates semantic friction, especially around Consent, publisher authority, agent Authority and Binding, but every friction point is already expressible through the existing v0.2 distinctions. The exercise therefore strengthens rather than weakens the current architecture.

The strongest stopping-rule conclusion is that a future SILT ↔ LCP adapter should be deliberately asymmetric: it may consume LCP artefacts and expose SILT-relevant semantic results, but it should not redefine LCP fields as SILT primitives or force SILT’s richer Source/Standing semantics into the LCP wire format.

On the present evidence, the next standards step is a freeze review of Core v0.2 plus a clearly labelled non-normative adapter/mapping note. Core should only reopen if implementation of that adapter demonstrates a semantic distinction that cannot be expressed without distortion.

## Appendix A. Public LCP sources reviewed

- Legal Context Protocol GitHub repository: [https://github.com/legal-context-protocol/legal-context-protocol](https://github.com/legal-context-protocol/legal-context-protocol)

- LCP Schema — legal-context.json fields: [https://legalcontextprotocol.org/standard/schema](https://legalcontextprotocol.org/standard/schema)

- LCP Examples — Levels 1–4: [https://legalcontextprotocol.org/standard/examples](https://legalcontextprotocol.org/standard/examples)

- LCP Level 4 — Integrated: [https://legalcontextprotocol.org/levels/integrated](https://legalcontextprotocol.org/levels/integrated)

- AAA launch announcement, 24 June 2026: [https://www.adr.org/press-releases/aaa-and-industry-leaders-launch-legal-protocol-for-agentic-commerce/](https://www.adr.org/press-releases/aaa-and-industry-leaders-launch-legal-protocol-for-agentic-commerce/)

- LCP White Papers index: [https://legalcontextprotocol.org/papers](https://legalcontextprotocol.org/papers)

## Appendix B. Interpretation discipline

This document is a non-normative interoperability experiment. It does not amend the SILT Core v0.2 Semantic Architecture, does not claim LCP endorsement of SILT, and does not assert that LCP concepts are legally effective in every jurisdiction. “Mapping” here means identifying possible semantic relationships, carriers, evidence paths and hand-off boundaries. “No equivalent” is an acceptable and often important result.
