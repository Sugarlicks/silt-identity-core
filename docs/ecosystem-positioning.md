# SILT Core v0.2 ecosystem positioning

**Status:** Non-normative companion, 18 September 2026.

SILT Core should be compared with adjacent standards by layer and function, not by vocabulary resemblance. The key question is whether another system carries evidence, credentials, governance rules, technical authorisation, legal context or execution machinery, and whether importing it into SILT would preserve or collapse the semantic boundary.

The canonical SILT seam remains:

> **Source -> Standing -> Presentation -> evaluation at the encounter**

SILT is therefore not a competitor to every identity, credential or authorisation protocol. In many cases it is the semantic layer that tells those systems what a presented or delegated artefact means in a particular encounter.

## Layer map

| Family / initiative | Primary layer | Relationship to SILT | Boundary to preserve |
| --- | --- | --- | --- |
| W3C Verifiable Credentials Data Model 2.0 | Credential data model and cryptographically verifiable claims | Complementary | A VC can provide Evidence or carry a presentation. Issuer/holder/verifier roles do not universally determine SILT Source, Standing or Authority. |
| OpenID4VP / OpenID4VCI | Credential presentation and issuance protocols | Complementary, mainly below Presentation | These protocols move credentials and presentations. SILT determines the encounter-relevant semantic claim, not the transport or credential-exchange protocol. |
| KERI / ACDC / CESR | Cryptographic identifier continuity, authentic provenance and chained data | Strong complement with semantic overlap around provenance | KERI/ACDC can preserve cryptographic provenance and delegation artefacts. SILT still asks what Source gives those artefacts semantic effect and what Standing or Authority follows in the encounter. |
| UCAN | Distributed capability delegation and invocation | Complementary below the semantic Authority line | A UCAN capability can carry or enforce scoped technical authority. Possession or valid delegation does not universally establish SILT Authority. |
| zcap | Object-capability delegation and invocation | Complementary below the semantic Authority line | zcaps model capability chains and attenuation. SILT must not collapse authority-by-possession into Source-grounded relational legitimacy. |
| GNAP (RFC 9635) | Dynamic grant negotiation and authorisation | Complementary operational layer | GNAP negotiates and conveys authorisation to software. SILT can supply semantics that precede or inform the grant without becoming the grant protocol. |
| DIF Trusted AI Agents / KYA-OS | Agent identity, delegation, signed proofs and agent trust stack | Adjacent and partially overlapping | Useful for carrying agent identity and delegation evidence. SILT's distinctive question is whether the delegated act is semantically legitimate under the relevant Source and encounter conditions. |
| Microsoft Entra Agent ID | Enterprise identity, authentication, access governance and lifecycle for AI agents | Complementary commercial infrastructure | Agent identity and access governance are operationally powerful but do not by themselves establish SILT Standing or Authority. |
| ToIP Governance Metamodel | Governance-framework structure and accountability documents | Complementary governance layer | A governance framework may be a Source, contribute Evidence or produce Profile Expressions, but SILT does not require ToIP governance form or reduce Source to governance documents. |
| CARE Principles | Indigenous data governance principles | Normative/ethical neighbour, not an implementation substrate | CARE centres collective benefit, authority to control, responsibility and ethics. SILT should enable such conditions to become legible without encoding CARE as a universal ontology. |
| OCAP® | First Nations data sovereignty and governance | Normative/governance neighbour | Ownership, Control, Access and Possession are Nation-grounded principles. SILT should not universalise or appropriate them; Profile Expressions may carry encounter-relevant conditions where authorised. |
| Te Mana Raraunga | Māori Data Sovereignty principles | Normative/governance neighbour | Māori rights and interests in data arise from Māori authority and relationships. SILT's role is encounter legibility, not to represent or exhaust tikanga or Māori data sovereignty. |
| UNDRIP | International rights instrument | Normative background | UNDRIP can inform Source and encounter conditions where relevant. It is not a credential or universal SILT Source. |
| Utah SEDI | Rights-first digital identity framework | Conceptually adjacent | SEDI's endorsement-vs-origination distinction is unusually close to SILT's refusal to treat system recognition as the source of identity or Standing. SEDI remains an individual digital-identity regime rather than a general plural-order encounter grammar. |
| Legal Context Protocol (LCP) | Discoverable legal terms and agentic-commerce context | Complementary carrier with bounded semantic overlap | LCP can carry terms, hashes, acceptance and dispute metadata. It cannot safely stand in for plural Profile Expressions, contested authority-to-express or deliberate non-expression. The SILT-LCP adapter is therefore intentionally partial. |

## Current status notes

As of September 2026, W3C VC Data Model 2.0 is a W3C Recommendation; OpenID4VP 1.0 and OpenID4VCI 1.0 are OpenID Final Specifications; GNAP is IETF RFC 9635; Microsoft Entra Agent ID is generally available; DIF's Trusted AI Agents Working Group is active; Utah SEDI is operating under Utah Code Title 63A, Chapter 20 with a 2026 implementation guide; and LCP v1.0 is still published as a draft for community review. KERI and ACDC remain active ToIP draft work rather than final ToIP standards. zcap remains draft Community Group work.

## What SILT contributes

Across these systems, SILT adds a narrow but consequential layer:

1. **Source-grounded Standing rather than system-issued status.** A credential, account, capability or registry can evidence or carry a relation without universally originating it.
2. **Presentation as an encounter act.** SILT distinguishes the participant's bounded presentation from the conditions against which it is evaluated.
3. **Plural Profile Expressions.** Multiple legal, customary, cultural, contractual or institutional orders may express different conditions without SILT silently merging or ranking them.
4. **Semantic Authority distinct from technical permission.** Capability and authorisation systems may implement or enforce a decision while remaining downstream from the legitimacy question.
5. **Non-inference and deliberate non-expression.** SILT allows uncertainty and limits of expression rather than forcing every normative condition into a machine-readable universal ontology.
6. **Semantic continuity across operational hand-off.** Keys, credentials, agents and capability tokens may change while the relevant Standing, Authority, Attribution or Obligation continues under its Source.

## Integration rule

An adjacent standard should enter SILT Core only if interoperability testing shows that a semantic distinction cannot be expressed without it. Otherwise the integration belongs in a Profile Expression, Presentation mechanism, Evidence relation, experimental binding, implementation profile or downstream operational layer.

That rule protects SILT from becoming another identity stack while still allowing it to work with the stacks that already exist.

## Reference sources

- W3C Verifiable Credentials Data Model 2.0: https://www.w3.org/TR/vc-data-model-2.0/
- OpenID for Verifiable Presentations 1.0: https://openid.net/specs/openid-4-verifiable-presentations-1_0.html
- OpenID for Verifiable Credential Issuance 1.0: https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0-final.html
- GNAP, RFC 9635: https://www.rfc-editor.org/info/rfc9635/
- UCAN specification: https://github.com/ucan-wg/spec
- Authorization Capabilities (zcap): https://w3c-ccg.github.io/zcap-spec/
- KERI / ACDC community and ToIP specifications: https://github.com/WebOfTrust/keri and https://www.trustoverip.org/our-work/deliverables/
- ToIP Governance Metamodel: https://www.trustoverip.org/wp-content/uploads/ToIP-Governance-Metamodel-Specification-V1.0-2021-12-21.pdf
- DIF Trusted AI Agents WG: https://identity.foundation/working-groups/trusted-agents.html
- Microsoft Entra Agent ID: https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
- CARE Principles: https://www.gida-global.org/careprinciples
- OCAP®: https://fnigc.ca/ocap-training/
- Te Mana Raraunga principles: https://www.temanararaunga.maori.nz/principles-of-maori-data-sovereignty
- Utah SEDI: https://sedi.utah.gov/
- Legal Context Protocol: https://legalcontextprotocol.org/
