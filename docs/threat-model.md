# SILT Core v0.2 semantic threat model

This note identifies semantic failure modes that an implementation can introduce even when its cryptography, identity verification or runtime authorisation succeeds. It is non-normative and should be read with the v0.2 Semantic Architecture and conformance suite.

## 1. Credential substitution

**Failure:** a valid credential or trusted issuer is treated as the Source of Standing or as proof of Authority without the relevant Source-grounded conditions.

**Control:** treat credentials as Evidence unless the originating order gives issuance constitutive effect.

## 2. Capability substitution

**Failure:** possession of a capability token, session or technical permission is treated as semantic Authority.

**Control:** evaluate Authority separately from Technical Capability. Runtime success may coexist with `NOT_SATISFIED` Authority.

## 3. Collective capture

**Failure:** belonging, membership or relational Standing is treated as power to represent, bind, disclose for or speak for a collective.

**Control:** require representational Authority to be separately grounded and evaluated.

## 4. Profile Expression capture

**Failure:** a bounded Profile Expression is treated as the full originating ontology, or one Profile Expression is silently made canonical over another.

**Control:** preserve plurality, provenance and boundedness. Do not infer a universal meta-expression.

## 5. Silence interpreted as absence

**Failure:** a condition deliberately left unexpressed because expression would materially distort it is treated as irrelevant, absent or failed.

**Control:** deliberate non-expression may be signalled without characterising the underlying condition. Absence of a signal does not prove that no unexpressed condition exists.

## 6. Forced determinacy

**Failure:** the evaluator invents a legal, cultural or institutional rule to avoid uncertainty.

**Control:** use only `SATISFIED`, `NOT_SATISFIED` and `INDETERMINATE` for conditions that enter evaluation.

## 7. Cryptographic-semantic conflation

**Failure:** key rotation or credential replacement is treated as loss of Standing or Authority, or technical continuity is treated as proof that those relations persist.

**Control:** maintain semantic provenance independently of operational artefact lifecycle.

## 8. Revocation overreach

**Failure:** revocation is presumed to cascade through all related Standing, Authority, obligations or delegated paths.

**Control:** model the scope and effect of Revocation according to the relevant Source and expressed conditions. No universal cascade is presumed.

## 9. Agent laundering

**Failure:** downstream AI agents or tools gain apparent legitimacy merely because an upstream system can authenticate them or because a capability chain executes successfully.

**Control:** preserve reconstructable semantic lineage. Derived Authority must remain within the delegable envelope or arise from a separate Source.

## 10. External classification capture

**Failure:** an external registry, identifier, trust list or legal-context pointer is treated as universally constitutive of Source or Standing.

**Control:** external artefacts may provide Evidence or have constitutive effect where the relevant order says so. Their technical existence alone does not create legitimacy.

## Security boundary

SILT does not replace cryptographic security, authentication, access control, key management or runtime policy. Those systems must be secured independently. The threat addressed here is loss or corruption of semantic meaning at the interoperability boundary.
