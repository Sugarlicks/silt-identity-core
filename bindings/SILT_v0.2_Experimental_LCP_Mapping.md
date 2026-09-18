Non-normative external-binding pressure test | 18 September 2026

Classification: complementary, partial and intentionally lossy.

# 1. Why this mapping exists

The v0.2 release process includes a real external payload test against Legal Context Protocol (LCP). LCP is a useful pressure surface because it is designed for agentic commerce, terms discovery, evidentiary integrity and signed acceptance, while SILT is concerned with Source-grounded Standing, bounded Presentation and semantic evaluation at the encounter.

The purpose is not to make LCP a SILT carrier of record. It is to see where the layers compose cleanly, where they overlap, and where a convenient mapping would collapse SILT semantics.

# 2. What LCP currently standardises

LCP v1.0 is published as a draft for community review dated 24 June 2026. Its normative conformance core is Section 2: a service publishes a JSON discovery document at /.well-known/legal-context.json, with a required HTTPS URL to a standalone terms document. The schema is extensible and permits additional properties. Later sections on trust levels, buyer policy, verification, private terms and protocol integration are advisory.

The specification itself draws a boundary with consumer-side authorisation systems: LCP records merchant terms and agreement context, while other protocols establish who authorised an agent and under what constraints. That makes it a strong adjacent test rather than a direct competitor to SILT.

# 3. Mapping

| **LCP element**                                          | **SILT treatment**                                                                                                                                                                                                                       |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| terms / terms document                                   | May provide Evidence and may form part of Source where the relevant order gives the instrument or terms constitutive effect. It is not universally Source.                                                                               |
| atrHash                                                  | Proof/Evidence of document integrity and identity. It does not establish Standing, Authority, Consent, Binding or legal validity.                                                                                                        |
| acceptanceRequired                                       | May express an encounter condition requiring explicit acceptance. It is not itself Consent.                                                                                                                                              |
| signed acceptance record (LCP Level 3 advisory guidance) | Evidence of assent/acceptance. Consent is evaluated under the relevant Source and Profile Expression; assent and Consent are not universally equivalent.                                                                                 |
| disputeResolution / jurisdiction index                   | May inform a Profile Expression and downstream Binding analysis. The index does not itself establish applicability, jurisdiction or Binding.                                                                                             |
| buyer policy (advisory)                                  | May partially express encounter conditions comparable to a Profile Expression, or may remain operational policy below the Presentation line. Classification depends on whether it expresses semantic conditions or merely enforces them. |
| authorization protocols referenced by LCP                | Complementary. SILT Authority is a semantic relation; credentials, mandates, signatures and capability artefacts may evidence/carry/enforce it but do not universally constitute it.                                                     |
| Level 3+ mutual agreement / binding language             | Treated as a downstream effect under applicable substantive conditions. SILT does not infer universal Binding from a signature or LCP level alone.                                                                                       |

# 4. The important non-equivalences

- A terms document is not universally Source. It may be Evidence, or a Source component where the relevant order gives it constitutive effect.

- atrHash is proof of document integrity, not proof of Standing, Authority, Consent, Binding or legal validity.

- acceptanceRequired states a condition. A signature supplies Evidence of assent or acceptance. SILT Consent remains a semantic relation evaluated under the relevant Source and Profile Expression.

- A jurisdiction or dispute-resolution index does not itself establish applicability, jurisdiction or Binding.

- A buyer policy may look like a Profile Expression when it expresses encounter conditions, but the same artefact may instead be operational policy below the Presentation line. SILT should classify by semantic function, not by file format.

# 5. Where the mapping is not lossless

| **SILT semantic**                            | **Why LCP cannot carry it losslessly**                                                                                                                                         |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| plural or conflicting Profile Expressions    | No native LCP concept for multiple coexisting normative expressions with no precedence rule. Adapter must preserve them outside the LCP terms index rather than collapse them. |
| deliberate non-expression                    | No native LCP representation. It must remain outside evaluation or be signalled only through a SILT-specific extension without characterising the hidden condition.            |
| Source-grounded relational Standing          | LCP discovers terms and legal context but does not model Source -> Standing. A legal-context pointer must not be promoted into Standing.                                      |
| collective provenance / authority to express | LCP does not natively model contested collective authority to author encounter conditions. SILT provenance semantics remain separate.                                          |

# 6. Experimental extension pattern

The current LCP JSON Schema allows unknown top-level properties. That makes a non-normative SILT pointer technically possible without changing LCP conformance. The package therefore includes an example using x-silt. The field name is deliberately provisional and is not proposed here as an LCP standard extension.

{  
"terms": "https://merchant.example/terms/txn-4821.md",  
"termsFormat": "markdown",  
"atrHash": "0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",  
"acceptanceRequired": true,  
"disputeResolution": {  
"method": "Institutional arbitration",  
"jurisdiction": "New Zealand"  
},  
"x-silt": {  
"version": "0.2",  
"mappingStatus": "experimental-non-normative",  
"encounterRef": "urn:silt:encounter:we04-lcp-01",  
"profileExpressionRefs": \[  
"urn:silt:pe:buyer-policy-01",  
"urn:silt:pe:merchant-terms-01"  
\],  
"presentationRef": "urn:silt:presentation:agent-b-01",  
"semanticRecordHash": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"  
}  
}

The extension carries references and a semantic-record hash only. It does not embed SILT meaning inside LCP or allow the LCP terms document to become a universal Profile Expression. A system that ignores x-silt remains LCP-conformant; a SILT-aware system may follow the pointer to the separate semantic record.

# 7. Pressure-test result

PASS WITH BOUNDED LOSS. LCP does not expose a missing SILT Core primitive. Instead, it confirms the architectural boundary: legal terms, hashes, signatures and transaction records can provide or carry Evidence, while Source, Standing, Consent, Authority and Binding remain semantic questions governed by the relevant order and encounter conditions.

The adapter must remain partial. In particular, plural Profile Expressions and deliberate non-expression cannot be forced into the LCP terms model without losing SILT's central claim. That is a carrier limitation, not a Core defect.

# 8. Sources checked

- Legal Context Protocol v1.0 specification, draft released for community review, 24 June 2026: https://github.com/legal-context-protocol/legal-context-protocol/blob/main/spec/legal-context-protocol-v1.md

- LCP JSON Schema: https://github.com/legal-context-protocol/legal-context-protocol/blob/main/spec/legal-context.schema.json

- Legal Context Protocol project site: https://legalcontextprotocol.org/
