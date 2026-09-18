A Source may be evidenced through documents, credentials, attestations, testimony or technical proofs.

The evidence is not necessarily the Source itself.

A trust deed may evidence a trust relation.

A credential may evidence an institutional recognition.

A genealogical or kinship record may evidence a relational history.

A SILT-conformant implementation MUST NOT silently collapse the artefact and the relation into one another.

# 5. Standing

Standing is the relational position occupied by a Participant with respect to an order, relationship, context, object, collective or other relevant domain.

Standing is grounded in Source.

Standing may depend upon conditions including, but not limited to:

- genealogical or kinship relations;

- relationship;

- recognition;

- endorsement;

- history;

- agreement;

- participation;

- appointment;

- institutional position;

- customary position;

- other relevant conditions.

Standing is relational rather than merely attributive.

A Participant does not necessarily possess Standing in the manner that they possess a credential, identifier or account.

Standing exists through relations.

## 5.1 Standing is not Status

SILT Core v0.2 contains no universal Status object.

Terms such as active, suspended, recognised, contested, appointed or expired may remain meaningful within a particular order, relationship or encounter.

They do not constitute a universal SILT Status lifecycle.

A SILT-conformant implementation MUST NOT reconstruct Standing indirectly as a renamed Status object.

## 5.2 Standing is not self-certification

A Participant may articulate the Standing under which they appear.

That articulation does not by itself create all relational conditions that make the Standing meaningful.

Where the encounter requires relationship, genealogy, recognition, appointment, agreement or other grounding, those conditions remain relevant.

Presentation may therefore be self-articulated without Standing becoming universally self-certified.

## 5.3 Standing is not verifier-certification

The opposite error is equally important.

A SILT-conformant evaluator MUST NOT treat Standing as valid merely because an external verifier, government, institution, credential issuer, registry or technical system has certified it.

Such mechanisms may provide Evidence or Source material relevant to the encounter.

They do not thereby become the universal source of Standing.

A SILT-conformant implementation MUST preserve the distinction between Evidence concerning Standing and the relational reality from which Standing arises.

## 5.4 Collective Standing

A SILT-conformant implementation MUST NOT model Collective Standing by default as the Standing of a large legal person possessing one master credential.

Collective identity may be:

- layered;

- relational;

- internally differentiated;

- distributed;

- contested;

- historically disrupted.

A Participant may simultaneously occupy relational positions within family or kinship groups, communities, customary orders, institutions, professions, trusts, governance bodies and other formations.

A SILT-conformant implementation MUST NOT assume that every Standing has:

- a single authoritative issuer;

- one canonical verifier;

- one exhaustive community test.

For a collective encounter, it is sufficient that the relevant relational Standing required for that encounter can become legible.

The complete internal constitution of the collective need not be exposed.

## 5.5 Collective Standing does not imply representational Authority

Standing within or in relation to a collective does not by itself confer Authority to:

- represent the collective;

- speak for the collective;

- bind the collective;

- commit collective resources;

- disclose collective information.

Collective representational Authority must be grounded according to the relevant Source and encounter conditions.

Membership, belonging or relational connection is therefore distinct from Authority to act on behalf of the collective.

## 5.6 Standing has no universal lifecycle

Standing does not have a universal Core lifecycle.

Standing may persist even while it is not currently being Presented or while its operability within a particular encounter remains uncertain.

Within an encounter, evaluation determines whether the relevant Standing has been sufficiently expressed for that encounter.

This evaluation does not transform Standing into an ACTIVE/INACTIVE state machine.

# 6. Evidence and Proof

Evidence supports a semantic claim.

Evidence is not itself the semantic claim.

Evidence may include, but is not limited to, customary, cultural, oral, relational or community-recognised forms of evidence; testimony or witness attestation; evidence concerning genealogical or kinship relations; collective recognition or governance records; and documentary or technical artefacts such as DIDs, credentials, signatures, key-control proofs, registry entries, trust deeds, security instruments, resolutions, contracts, zero-knowledge proofs, relationship graphs or technical capability artefacts.

The relevance and sufficiency of any form of Evidence depends upon the conditions expressed for the encounter. SILT does not establish a universal hierarchy of evidentiary forms.

Accordingly:

> proof of key control  
> !=  
> Standing  
> !=  
> Authority  
> !=  
> Action

Evidence may substantiate a Presentation, but it is not itself the Presentation.

A SILT-conformant implementation MUST NOT silently replace Source-grounded Standing with Evidence. Evidence recognised in one encounter or normative order need not be recognised in another.

The ability to verify a representation does not confer jurisdiction over the reality represented.  
  
Relational or relationship-graph representations may also provide Evidence concerning Source, Standing, Authority, delegation or other semantic relations. Such graphs may include, but are not limited to, genealogical or kinship relations, collective relationships, institutional structures, trust relationships, Authority lineage or machine-agent delegation. A graph is a representation of relevant relations, not the relations themselves, and SILT does not require the underlying relational substrate to be exhaustively represented or disclosed.

# 7. Selective expression and disclosure at the encounter

SILT treats bounded and proportionate expression as a structural property of the encounter, not merely as a privacy feature.

The expressions brought into an encounter may arise from richer substrates than SILT should attempt to encode.

- Standing may be rich, durable, relational, historically deep and collectively sensitive.

- The normative or relational substrate informing a Profile Expression may likewise exceed what can or should be represented in SILT.

