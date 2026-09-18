# SILT Core v0.2 — Semantic Architecture

**Freeze Candidate 1 — post-stress-test close-out**

| **Status**   | Freeze Candidate 1 for semantic freeze                                                                                                                                                        |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Role**     | Canonical semantic reference for SILT Core v0.2, pending release tag                                                                                                                          |
| **Scope**    | Semantic architecture, not implementation specification                                                                                                                                       |
| **Revision** | RC4.1 close-out: WE01-WE04 pre-freeze gate completed; machine-readable conformance suite and experimental LCP mapping reviewed; no Core reopening triggered. Editorial freeze candidate only. |

> Source -> Standing -> Presentation -> evaluation at the encounter

# 0. Purpose

SILT Core provides a semantic architecture through which participants, collectives and systems operating under different legal, cultural, customary, private, institutional or technical orders may become mutually legible at moments of encounter without requiring those orders to collapse into a single ontology or surrender their own sources of authority.

SILT is therefore concerned with encounter rather than assimilation.

> Source -> Standing -> Presentation -> evaluation at the encounter

This sequence expresses semantic dependency, not a mandatory one-to-one processing pipeline.

A Standing may be grounded in multiple Sources. A Source may support multiple relational positions. A Presentation may contain more than one relevant semantic claim. An encounter need not require a substantive Standing claim where none is necessary.

SILT standardises the boundary at which relational legitimacy may become selectively legible to another order.

It does not standardise the originating ontology or normative substrate itself.

A receiving Participant, order or system encounters a Presentation of Standing. It does not thereby become the source of that Standing.

SILT Core is semantically thick and operationally thin. It models semantic distinctions where cross-domain meaning depends upon them while remaining deliberately thin about authentication, credential formats, key management, transport, registries, runtime policy, technical capabilities and execution machinery.

> semantic hand-off, not semantic surrender.
>
> SILT makes normative difference legible. It does not guarantee agreement between normative orders.

## 0.1 Normative language

Throughout this document, 'SILT Core' refers to the semantic architecture defined here. 'SILT' may be used descriptively for the wider project, but normative requirements are stated against SILT-conformant implementations, evaluators or representations.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in all capitals. Lower-case forms are descriptive rather than normative.

# 1. Architectural boundary

SILT Core is not any of the following, and this list is non-exhaustive:

- a universal identity model;
- a universal legal ontology;
- a universal authorisation engine;
- a credential system;
- a conflict-of-laws system;
- a universal verifier;
- a law engine.

SILT does not determine what a Participant ultimately is.

It provides a grammar through which relevant relational position, authority and associated semantic conditions may become intelligible within an encounter.

The principal architectural movement remains:

> SOURCE  
> |  
> v  
> STANDING  
> |  
> v  
> PRESENTATION  
> |  
> v  
> EVALUATION AT THE ENCOUNTER

One or more Profile Expressions may inform evaluation at an encounter. A Profile Expression may arise from legal, customary, cultural, relational, contractual, institutional, governance or other normative contexts and expresses only encounter-relevant semantic conditions.

> PROFILE EXPRESSION(S) -> encounter-relevant conditions -> EVALUATION AT THE ENCOUNTER

Profile Expression does not form a second architectural spine. The principal seam remains Source -> Standing -> Presentation -> evaluation at the encounter.

Evaluation may concern Standing and, where relevant, Authority, Consent, Reliance, Action, Attribution, Revocation and Obligation.

Binding, liability, settlement, remedies, institutional recognition and other downstream effects may be indicated by an applicable Profile Expression or otherwise determined outside Core. A Profile Expression does not itself manufacture those effects.

A SILT-conformant evaluator MUST NOT infer an unstated legal, cultural, institutional or normative rule merely to produce a determinate result.

Where the expressed semantic conditions are insufficient, a SILT-conformant evaluator MUST permit an INDETERMINATE result.

# 2. Profile Expression

Profile Expression is a bounded, selective and non-exhaustive expression of semantic conditions relevant to evaluation at an encounter.

A Profile Expression does not replace Presentation and does not itself constitute a Participant's Presentation of Standing.

A Profile Expression may arise from one or more legal, customary, cultural, relational, contractual, institutional, governance or other normative contexts.

It does not represent or exhaust those contexts.

> The order exceeds its expression.

## 2.1 Function

A Profile Expression supplies encounter-relevant conditions for evaluation without requiring SILT to model the full normative or relational substrate from which those conditions arise.

A Profile Expression may express, where relevant, conditions including, but not limited to:

- which Sources are relevant;
- what Standing conditions matter;
- what may need to be Presented;
- what Evidence may support a claim;
- what Authority conditions apply;
- whether Consent or Reliance is required;
- how Revocation is to be evaluated;
- what Actions may have semantic effect;
- how Attribution is to be understood;
- how Obligation may arise or change;
- what downstream effects an applicable order or relationship indicates may follow.

A Profile Expression does not imply that a complete representation of the originating order exists, is knowable, or is capable of representation.

## 2.2 Selective expression and unencumbered substrate

The normative or relational substrate from which a Profile Expression arises remains prior to and independent of the expression.

A Profile Expression does not capture, constitute, modify, constrain, govern or otherwise encumber that substrate.

Its role is selective expression for the purposes of evaluation at the encounter.

Evaluation of a Profile Expression applies only to the encounter. It does not confer authority over, or alter the meaning of, the originating substrate.

> The substrate remains unencumbered by the expression.

Presentation is an encounter-specific act or envelope by a Participant. Profile Expression is a bounded expression of encounter-relevant conditions arising from a normative or relational substrate. They are distinct constructs and are not assumed to be structurally parallel.

### 2.3 Bounded expression

SILT operates on bounded expressions relevant to an encounter. A Presentation does not exhaust the Source-grounded Standing from which it arises, and a Profile Expression does not exhaust the normative or relational substrate that informs it.

Neither expression acquires authority over, modifies or encumbers its underlying substrate merely by being represented within SILT.

## 2.4 Provenance and authority to express

Where a Profile Expression purports to express conditions arising from a collective, institution, community or other normative order, its provenance is material.

Where provenance is material to evaluation, a SILT-conformant representation of a Profile Expression SHOULD identify the authority, relationship or process under which it was authored, adopted, recognised, contributed to or maintained.

Standing within a collective does not by itself confer Authority to define or express the collective's encounter conditions.

Authority to author, adopt, maintain or contribute to a Profile Expression is itself a relational question. A SILT-conformant evaluator MUST NOT infer that Authority merely from membership, identity or technical control.

Where that Authority is material to the encounter, authoring, adopting, maintaining or contributing to a Profile Expression may itself be evaluated as an Action subject to relevant Authority conditions, with Evidence supplied where appropriate.

Authority to express a Profile Expression may be grounded directly in Source. SILT does not require it to derive from a prior Profile Expression or parent Authority.

SILT Core does not prescribe the technical mechanism by which such Authority is authenticated or verified.

SILT conformance does not manufacture the legitimacy of a Profile Expression.

## 2.5 Plural and collective expression

A Profile Expression may be individual, collective, composite, layered, collectively authored, contested or provisional.

An encounter may involve multiple Profile Expressions, including expressions arising from different normative orders or from different positions within the same collective.

A SILT-conformant implementation MUST NOT assume that a collective, community or normative order speaks with one voice merely because a machine-readable expression is required.

Where several Profile Expressions are applicable, they need not resolve into a single canonical expression.

A Profile Expression does not acquire applicability, precedence or binding effect over another Participant merely by being present in an encounter.

Where applicability, composition or precedence between Profile Expressions matters, any basis for doing so arises from an expressed rule, relevant Source, relationship, agreement or other applicable encounter condition. In the absence of such a basis, SILT does not invent one.

## 2.6 Disagreement and non-absorption

Different Profile Expressions may express different conditions for evaluation of the same Presentation.

SILT Core does not impose a universal meta-expression for resolving conflicts between normative orders.

Where encounter-relevant conditions conflict, a SILT-conformant evaluator MAY preserve that disagreement explicitly rather than collapse it into false consensus.

Cross-order negotiation, translation and conflict resolution are outside the mandatory scope of SILT Core v0.2.

A SILT-conformant implementation MUST NOT treat a Profile Expression as a complete representation of customary law, religious law, private law, institutional governance, community practice or any other originating order.

# 3. Participant

Participant is the deliberately thin Core referent for something participating in an encounter.

SILT Core does not require a Participant to be an individual human.

Depending on the encounter, a Participant may include, but is not limited to:

- an individual;
- a collective;
- an office;
- an institution;
- a trust;
- a technical or machine agent;
- another recognised participant form.

A SILT-conformant implementation MUST NOT treat Participant as implying a universal theory of personhood, legal personality or identity.

The substantive meaning of a Participant's position lies in Source, Standing, Presentation, Authority and the conditions relevant to the encounter.

A SILT-conformant implementation MUST NOT require a collective Participant to decompose collective Standing or Authority into individual ownership merely to become legible within SILT.

# 4. Source

Source identifies the referenced origin or ground from which Standing, Authority, Obligation or another SILT semantic relation derives its claimed meaning or legitimacy.

Source means ground or provenance.

It does not necessarily mean:

- issuer;
- grantor;
- credential authority;
- state registry;
- document;
- technical attestor.

A Source may include, but is not limited to:

- relationship;
- genealogical or kinship relations;
- customary process;
- agreement;
- trust;
- mandate;
- constitution;
- appointment;
- community recognition;
- governance event;
- institutional instrument;
- private instrument;
- prior Authority;
- another relevant ground.

A Source may be composite.

It need not correspond to a single issuer, credential or artefact.

A SILT-conformant representation of Source MUST identify or reference the claimed ground sufficiently for that ground to be distinguished from Evidence concerning it.

SILT Core does not prescribe one universal Source of Standing or Authority.

A Source recognised in one encounter need not be recognised in another.

No Source becomes universally authoritative merely because SILT can represent it.

## 4.1 Source plurality

Standing need not originate in the receiving order in order to be capable of effect within an encounter.

A Participant's Standing may arise within an order whose ontology, history, law or forms of recognition differ materially from those of the receiving system.

The role of SILT is not to reconcile those orders into one truth.

Its role is to provide a disciplined boundary at which relevant meaning may become legible.

## 4.2 Source is not evidence alone

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

Accordingly, Presentation is a bounded disclosure or projection of Standing, while Profile Expression is a bounded expression of encounter-relevant conditions. Neither is exhaustive of its underlying substrate.

SILT favours expression or disclosure proportionate to the purpose and expressed conditions of the encounter.

SILT does not prescribe a particular privacy technology.

Forms and mechanisms of selective expression or disclosure may include, but are not limited to:

- oral, witnessed or relational testimony;
- genealogical, kinship or community-recognised forms of expression;
- customary, ceremonial, performative or collective processes;
- community or collective attestation;
- documentary, contractual or private instruments;
- credentials and attestations;
- selective-disclosure mechanisms;
- zero-knowledge proofs;
- other culturally, legally, institutionally or technically appropriate forms.

SILT does not privilege technical forms of disclosure over cultural, relational, customary or documentary forms. The appropriate form depends upon the nature of the Standing, Source and encounter. A technical mechanism may carry or support a cultural or relational expression, but does not replace the meaning or authority of that expression.

Selective disclosure is not compulsory concealment. A Participant or originating order may deliberately disclose more where appropriate.

Participation in an encounter does not give another order a general entitlement to the underlying ontology or substrate.

# 8. Presentation

Presentation is the encounter-specific act or envelope through which a Participant makes a bounded and purpose-relevant projection of Standing available for evaluation in a particular encounter.

Presentation is the architectural seam at which one order becomes encounterable by another.

> for this encounter and this purpose.

It does not describe the totality of the Participant.

A Presentation may include, but is not limited to:

- a predicate;
- a relational claim;
- selected Evidence;
- an instrument;
- a governance record;
- richer disclosure where required.

SILT favours the minimum disclosure sufficient for the expressed conditions of the encounter.

Presentation is semantically first-class and implementation-light.

A Presentation may be made or carried through forms and mechanisms including, but not limited to:

- oral or witnessed testimony;
- genealogical, kinship or community-recognised forms of expression;
- customary, ceremonial, performative or collective processes;
- collective or community attestation;
- a signed message;
- a Verifiable Presentation;
- a zero-knowledge proof exchange;
- a private, commercial or security instrument;
- a governance or institutional record;
- a trust response;
- a validator request;
- a capability-related message;
- another culturally, legally, institutionally or technically appropriate form or mechanism.

No one cultural, legal, documentary or technical form defines SILT Presentation. The form of a Presentation does not determine its semantic sufficiency. Evaluation concerns what is expressed for the encounter, not whether the Presentation uses a preferred documentary or technical format.

## 8.1 Presentation does not create Standing

The act of Presentation does not, merely by presenting it, generate the Standing being Presented.

An invalid, stale, disputed, incomplete or no-longer-operative claim may still be Presented.

Evaluation concerns what has been Presented.

## 8.2 Evaluation does not constitute Standing

An evaluator considers whether the Presentation satisfies the conditions relevant to the encounter.

That evaluation applies to the encounter.

Mere evaluation does not retroactively:

- constitute;
- extinguish;
- redefine;
- universally validate;
- universally invalidate

the Source-grounded Standing from which the Presentation arose.

This is a Core invariant.

An evaluator may conclude:

> Presentation condition:  
> NOT_SATISFIED

without SILT concluding:

> Underlying Standing:  
> DOES_NOT_EXIST

These are different propositions.

## 8.3 Constitutive Action is distinct from evaluation

Some encounters contain Actions that may legitimately create, alter or terminate relational positions.

Examples may include:

- appointment;
- admission;
- adoption;
- election;
- endorsement;
- transfer;
- agreement;
- formation of membership.

Where the relevant Source and expressed encounter conditions give such an Action constitutive effect, resulting Standing may change.

The resulting Standing is grounded in the Source and constitutive Action.

It is not created merely by the evaluator's act of verification.

> verification is not constitution.
>
> a valid constitutive Action may alter relational Standing.

# 9. Evaluation at the encounter

Evaluation asks whether semantic conditions expressed through a Presentation are satisfied under the applicable Profile Expression or Profile Expressions for the encounter being considered.

An encounter need not be instantaneous or reducible to a single evaluation event. It may extend across time, include multiple Presentations, Participants or Profile Expressions, and involve iterative, staged, contested or provisional evaluation.

A SILT-conformant implementation MUST NOT require a processual, collective or relational condition to be reduced to a punctual determination merely because a technical implementation is capable of producing one.

Evaluation is relative to the applicable Profile Expression. Where multiple Profile Expressions are applicable, a SILT-conformant evaluator MAY evaluate the same Presentation separately under each expression. Each evaluation result MUST identify the Profile Expression under which it was produced.

A SILT-conformant evaluator MUST NOT silently merge, rank or privilege conflicting Profile Expressions. Where an expressed rule governs their composition, precedence or mutual application, that rule may itself be evaluated. In the absence of such a rule, disagreement remains explicit.

A SILT-conformant evaluation MUST produce one of the following outcomes for each evaluated semantic condition:

**SATISFIED -** The supplied and expressed semantic conditions meet the relevant encounter condition.

**NOT_SATISFIED -** An expressed condition is known not to have been met.

**INDETERMINATE -** The supplied semantic state does not permit a conclusion without importing an unstated rule, missing fact or external judgement.

Where a condition has been brought into SILT evaluation but the available bounded expression is insufficient to support a conclusion, the result is INDETERMINATE.

Where a condition cannot be adequately expressed for SILT evaluation without material distortion, SILT Core does not require that condition to be evaluated. A SILT-conformant implementation MUST NOT represent the absence of an evaluation result in such a case as SATISFIED, NOT_SATISFIED or as a universal judgement about the underlying condition.

Where appropriate and authorised, a Profile Expression MAY indicate that one or more encounter-relevant conditions have been deliberately left unexpressed because bounded expression would risk material distortion. Such an indication need not characterise the underlying condition and MUST NOT be treated as satisfying, negating or otherwise evaluating it. The absence of such an indication MUST NOT support an inference that no unexpressed condition exists.

A Profile Expression may specify an aggregate encounter result.

SILT Core does not prescribe a universal rule for combining heterogeneous evaluation outcomes.

Where a Profile Expression defines an aggregate encounter result, a SILT-conformant representation MUST express the relevant composition conditions, including the treatment of INDETERMINATE where material.

In the absence of an expressed composition rule, a SILT-conformant evaluator MUST NOT infer an aggregate result.

SILT Core does not require heterogeneous semantic conditions to collapse into one undifferentiated validity judgement.

An encounter may therefore produce:

> Standing SATISFIED  
> Authority SATISFIED  
> Consent INDETERMINATE  
> Reliance NOT_SATISFIED

rather than simply:

> INVALID

SILT evaluates presented and expressed semantic conditions.

It does not answer the universal question:

> Is this Participant legitimate?

Nor:

> Is this Standing valid everywhere?

The narrower SILT questions are:

> Which expressed semantic conditions are satisfied, under which applicable Profile Expression or Profile Expressions, for this encounter?

## 9.1 Evaluation does not compel acceptance

Source-grounded Standing may be capable of effect within an encounter without originating in the receiving order.

That does not imply automatic acceptance.

A receiving party’s obligations, if any, arise from the relevant Source, law, agreement, relationship, normative order or other applicable ground, as relevantly expressed for the encounter. A Profile Expression may make such conditions legible; it does not by itself create the underlying obligation.

They do not arise merely because a Presentation exists.

SILT therefore distinguishes legibility from mandatory recognition.

## 9.2 Evaluation does not encumber either substrate

Evaluation operates on the bounded expressions brought to the encounter.

It does not acquire jurisdiction over the Participant's underlying Source-grounded relations.

It does not acquire jurisdiction over the normative or relational substrate from which a Profile Expression arose.

A SILT-conformant evaluator MUST NOT represent encounter-specific conclusions as universal determinations about either substrate.

# 10. Technical Capability

Technical Capability is the practical ability of a Participant or system to cause a technical effect.

Possession or control of technical mechanisms including, but not limited to:

- a key;
- a token;
- a session;
- a wallet;
- a capability;
- an account;
- an execution surface

may establish Technical Capability.

Technical Capability does not by itself establish SILT Authority.

> technical_execution_possible = true

does not entail:

> SILT_Authority_valid = true

A Profile Expression may express that, under the relevant Source or normative conditions, specified Technical Capability constitutes relevant Evidence or is sufficient to satisfy an Authority condition for a particular encounter. SILT Core does not impose that conclusion universally.

**10.1 Operational boundary**

Authentication, key continuity, credential and capability-token handling, session management, dynamic authorisation, access control, policy execution and runtime execution are operational mechanisms rather than SILT Core semantics.

These mechanisms may operate before, during or after a Presentation and may carry, substantiate, enforce or execute semantic relations expressed through SILT. Their position “below the Presentation line” is therefore architectural rather than temporal.

SILT Core does not prescribe how these mechanisms authenticate a Participant, maintain cryptographic continuity, distribute technical capabilities, manage sessions or execute an authorised Action. Existing or future technical systems may perform those functions.

Their outputs may provide Evidence relevant to evaluation at the encounter, but technical success does not by itself establish Standing, Authority, Attribution, Consent, Reliance or Obligation. Conversely, a change in the operational mechanism does not by itself extinguish those semantic relations.

A SILT-conformant implementation SHOULD expose only the semantic information required for interoperability with such systems. Operational machinery should not be elevated into Core unless interoperability testing demonstrates a semantic distinction that cannot otherwise be expressed.

# 11. Authority

Authority describes the bounded power claimed or recognised for an Action or class of Actions.

**Authority may arise through paths including, but not limited to:**

- Source;
- Standing;
- agreement;
- office;
- mandate;
- parent Authority;
- collective, customary or community-recognised process;
- private ordering;
- external authority artefact;
- another relevant formation path.

Standing is central to SILT's account of relational legitimacy.

A cryptographic capability, credential or technical authority artefact may provide Evidence concerning Authority, carry, constrain or enforce Authority, or form part of Source where the relevant conditions give it constitutive effect. It does not universally constitute the Source or ground of Authority.

Where such an artefact has constitutive effect, that effect arises under the relevant Source and encounter conditions, not from technical verifiability alone.

Consistent with §10, possession or technical validity of such an artefact does not by itself establish SILT Authority.

SILT does not require every Authority formation path to pass mechanically through a Standing object.

An encounter may recognise:

> Source -> Standing -> Authority  
>   
> Source -> Authority  
>   
> Standing + Source -> Authority  
>   
> External authority artefact  
> +  
> expressed encounter conditions  
> |  
> v  
> Authority

Authority may include, but is not limited to:

- scope;
- purpose;
- resource;
- temporal limits;
- formation conditions;
- exercise conditions;
- delegation limits;
- lineage;
- validity dependencies;
- Revocation rules.

A SILT-conformant evaluator MUST NOT infer Authority from Technical Capability unless the applicable Profile Expression expressly provides for that conclusion under the relevant Source or normative conditions.

# 12. Delegation and derived Authority

Delegation is an Action through which derived Authority may be constituted.

A SILT-conformant evaluator MUST NOT treat derived Authority as exceeding the delegable envelope of its parent Authority unless another recognised Source supplies the additional Authority.

Lineage and continuing dependency are distinct.

A child Authority may derive historically from another Authority without remaining permanently dependent upon the continued validity of every object in its lineage.

A SILT-conformant implementation MUST NOT presume cascade behaviour. Where cascade behaviour is material, it must be expressed by the relevant Source, Profile Expression or other applicable encounter condition.

## 12.1 Semantic lineage

Downstream exercise of derived Authority does not require repeated Presentation of every upstream Standing relation.

An encounter may rely upon preserved semantic lineage where:

- relevant Authority remains valid;
- required provenance can be reconstructed;
- applicable constraints remain satisfied.

This permits downstream systems to operate without forcing every runtime Action to repeat the full originating encounter.

Semantic lineage may be represented through relational graphs or other appropriate structures, but SILT Core does not prescribe a graph model.

# 13. Revocation

Revocation is an Action affecting a revocable semantic relation, most notably Authority.

Where Authority is revocable, a SILT-conformant representation SHOULD identify, through the relevant Source or Profile Expression, matters including, but not limited to:

- who may revoke;
- what may be revoked;
- effective time;
- scope;
- any cascading effect.

Revocation is prospective unless the relevant expressed conditions provide otherwise.

A later Revocation does not rewrite the validity of an Action correctly performed before Revocation took effect.

Authority may use lifecycle vocabulary such as:

- ACTIVE;
- SUSPENDED;
- REVOKED;
- EXPIRED;
- SUPERSEDED.

These describe current exercisability.

They do not constitute a universal ontology of legitimacy.

Standing does not inherit this lifecycle automatically.

# 14. Consent

Consent describes a bounded relation of agreement or permission concerning a specified Action, disclosure, terms, object or purpose, where relevant to the encounter.

The conditions under which Consent is expressed, recognised, evidenced, withheld or withdrawn may vary according to the relevant Source and Profile Expression.

An expression of assent may provide Evidence concerning Consent, but SILT does not treat assent and Consent as universally equivalent.

Where Consent is collective, representative or procedurally constituted, a SILT-conformant evaluator MUST NOT infer it merely from the assent of an individual Participant unless the relevant Authority and encounter conditions support that conclusion.

Consent is object-specific.

A bare value such as:

> consent = true

is normally semantically insufficient.

A SILT-conformant representation of Consent SHOULD identify, where relevant, matters including, but not limited to:

- Participant;
- terms or object;
- scope;
- purpose;
- context;
- effective conditions;
- withdrawal or termination conditions.

Consent capture, signature and technical enforcement may be implemented downstream.

SILT does not assume that every Action, vote, delegation, click or relationship is universally reducible to Consent.

# 15. Reliance

Reliance describes the expressed conditions under which another Participant may act upon a Presentation, Authority representation or related semantic claim.

Reliance is distinct from validity.

A semantic claim may be valid while a particular Participant is not entitled under the relevant encounter conditions to rely upon it.

SILT validates expressed Reliance conditions.

A SILT-conformant evaluator MUST NOT silently import external doctrines such as apparent authority, estoppel or reasonable reliance where they have not been expressed.

# 16. Action

Action is the event being evaluated or represented.

An Action may include, but is not limited to:

- signing;
- submitting;
- presenting;
- accepting;
- transferring;
- appointing;
- delegating;
- revoking;
- endorsing;
- voting;
- paying;
- disclosing;
- another encounter-relevant event.

Some Actions may alter semantic relations.

For example:

> delegation  
> |  
> v  
> Authority may be constituted  
>   
> endorsement  
> |  
> v  
> Standing may change  
>   
> agreement  
> |  
> v  
> Obligation may arise  
>   
> revocation  
> |  
> v  
> Authority may become REVOKED  
>   
> performance  
> |  
> v  
> Obligation may become DISCHARGED

Transition is therefore not a separate universal primitive.

The relevant Source and expressed encounter conditions determine what semantic effect, if any, follows from a valid Action.

# 17. Attribution

Attribution connects an Action to the Participant, Authority context or relational position through which that Action is properly understood.

SILT distinguishes factual actor attribution from Authority-mediated attribution.

The Participant who technically performs an Action need not be the Participant to whom that Action may properly be attributed through Authority.

This distinction is particularly important in institutional, fiduciary, collective, customary or plural, delegated and autonomous-agent contexts.

Attribution does not itself establish:

- Binding;
- liability;
- responsibility under external law.

Those consequences remain downstream and encounter-specific.

# 18. Obligation

Obligation is a persistent relational state describing required performance, responsibility or constraint between relational positions.

Obligation is distinct from Authority.

An Obligation may persist while:

- Standing changes;
- Authority changes;
- the Participant occupying an entitled position changes.

This is especially important for transferable instruments and other relationships in which relational position changes while the underlying Obligation survives.

Obligation may use encounter-specific lifecycle states such as:

- CREATED;
- OUTSTANDING;
- PARTIALLY_PERFORMED;
- DISCHARGED;
- another expressed state.

The canonical field for what is required is required_performance.

Actual performance is an Action or other recognised cause of state change.

# 19. Binding as a downstream effect

Binding is not a universal Core conclusion.

This section defines an architectural boundary, not a SILT Core primitive.

After SILT evaluates a Presentation, Authority and relevant Action, the applicable Profile Expression or other recognised normative mechanism may indicate what downstream effect follows.

Possible downstream effects may include, but are not limited to:

- formation of an Obligation;
- change of Standing;
- creation of Authority;
- Revocation;
- discharge;
- settlement;
- institutional recognition;
- another consequence.

SILT therefore separates:

> semantic evaluation  
> |  
> v  
> Attribution  
> |  
> v  
> downstream effect

from the false universal proposition:

> valid semantic evaluation  
> =  
> legally binding everywhere

SILT makes no such claim.

# 20. Semantic continuity and cryptographic continuity

SILT distinguishes semantic continuity from cryptographic continuity.

Changes in technical elements including, but not limited to:

- keys;
- credentials;
- capability tokens;
- sessions;
- technical identifiers;
- execution infrastructure

do not by themselves alter:

- Standing;
- Authority;
- Attribution;
- Obligation.

Conversely, continued technical control of mechanisms including, but not limited to:

- a key;
- a credential;
- an account;
- a capability;
- a session

does not establish that corresponding SILT Authority remains valid.

A system may maintain cryptographic continuity while losing semantic Authority.

A Participant may retain semantic Standing despite:

- key replacement;
- credential rotation;
- technical migration;
- identifier change.

This distinction is fundamental to interoperability.

# 21. Semantic hand-off

Downstream systems may implement:

- authentication;
- key continuity;
- capability distribution;
- dynamic authorisation;
- access control;
- policy evaluation;
- transport;
- execution.

A SILT-conformant implementation SHOULD integrate with such systems rather than recreate them where interoperability permits.

Identity and credential infrastructure, authentication and authorisation protocols, capability systems, agent-security infrastructure and future equivalents may provide:

- Evidence;
- transport;
- technical authorisation;
- execution mechanisms.

Their technical outputs do not automatically replace SILT semantic distinctions.

SILT retains sufficient semantic continuity to answer questions such as:

- what Standing was Presented;
- from what Source it derived;
- what Authority was relevant;
- what Consent or Reliance conditions applied;
- what Action occurred;
- how the Action is attributable;
- what Obligation or other relational state remains.

The technical system carries execution.

> SILT preserves meaning.

# 22. External classification safeguard

SILT enables mutual legibility without granting the receiving order jurisdiction over the ontology of the originating order.

A SILT-conformant implementation MUST NOT use verification as a basis for universal classification.

A receiving Participant or order may establish what it requires for its own encounter.

A SILT-conformant evaluator MUST NOT represent failure of an encounter-specific condition as universal negation of underlying Standing.

The receiving order is not presumed, merely because it performs an evaluation, to possess authority to determine what the Participant, collective, Source or originating order ultimately is.

This safeguard is particularly important where Indigenous, customary, historically marginalised or internally plural communities encounter systems whose administrative categories were not created by those communities.

SILT makes difference encounterable.

> It does not domesticate difference into the categories of the receiver.

# 23. Non-compulsion of ontology

SILT Core does not require a Participant or originating order to expose or translate the entirety of its ontology or normative substrate merely to participate in a SILT-structured encounter.

SILT seeks sufficient mutual legibility at the boundary.

It does not require metaphysical agreement.

Where an originating order contains concepts that cannot be fully translated without distortion, a Presentation or Profile Expression may preserve those terms, relationships or limits rather than force false equivalence.

SILT therefore permits partial translation.

Partial translation is not architectural failure.

In some plural encounters, it may be the correct result.

SILT Core does not presume that every normative or relational condition is capable of adequate bounded expression.

Where bounded expression would materially distort the originating order, the semantically correct treatment may be partial translation, non-expression or, where the condition has entered evaluation but cannot be resolved, an INDETERMINATE result.

# 24. Core invariants

1. Source plurality. SILT Core does not prescribe one universal Source of Standing or Authority.
2. Source is ground, not merely artefact. Evidence of a relation is not necessarily the relation itself, although an artefact or issuance event may form part of Source where the relevant order gives it constitutive effect.
3. Relational Standing. Standing arises within relations and is not reducible to a portable attribute.
4. No universal Status object. Encounter-specific states do not become a Core Status primitive.
5. No universal self-certification. Articulation alone does not necessarily create relational Standing.
6. No universal verifier-certification. Verification does not become the universal source of Standing.
7. Encounter, not creation. A receiving Participant, order or system encounters a Presentation of Standing. Mere evaluation does not create that Standing.
8. Constitutive Action remains possible. A valid Action may create, alter or terminate relational Standing where the relevant Source and encounter conditions give it such effect.
9. Presentation is selective disclosure. Presentation exposes a bounded, purpose-relevant projection of Standing rather than the totality of the Participant.
10. Profile Expression is bounded expression. Profile Expression expresses encounter-relevant semantic conditions without representing or exhausting the originating normative or relational substrate.
11. The substrate remains unencumbered. Neither Presentation nor Profile Expression captures, modifies, constrains or governs the substrate from which it arises merely by being represented within SILT.
12. Evaluation is encounter-specific. Failure of a Presentation under an encounter condition does not universally invalidate underlying Standing.
13. Encounter need not be punctual. Evaluation may be extended, staged, iterative, contested or provisional where the relevant relations or processes require it.
14. Bounded expression has limits. SILT does not presume that every normative or relational condition can be adequately reduced to a bounded expression. A condition that cannot be adequately expressed need not enter SILT evaluation; where it does enter evaluation but the available expression is insufficient for a conclusion, the result is INDETERMINATE. Where appropriate and authorised, deliberate non-expression may be indicated without characterising the underlying condition; absence of such an indication does not imply absence of an unexpressed condition.
15. Legibility does not compel acceptance. A Presentation may become intelligible without obliging every receiving Participant or order to recognise it.
16. Evidence is not the semantic claim. Proof of a representation is distinct from the relational meaning represented.
17. Collective Standing is not a master credential. Collective identity and Standing may remain layered and internally plural.
18. Collective Standing does not imply representational Authority. Belonging is distinct from power to bind or speak for a collective.
19. Profile Expression may be plural. Multiple, composite, collective, contested or provisional expressions may coexist within an encounter.
20. Evaluation is Profile Expression-specific. Where multiple Profile Expressions are applicable, evaluation results remain distinct and identify the Profile Expression under which they were produced.
21. No silent Profile Expression precedence or merger. SILT does not merge, rank or privilege conflicting Profile Expressions without an expressed basis for doing so.
22. No universal meta-expression. Different normative orders may express different encounter conditions without SILT imposing a single superior expression.
23. Disagreement may remain explicit. SILT does not require false consensus between normative orders.
24. Semantic non-inference. For a condition that has entered SILT evaluation, missing semantics produce INDETERMINATE rather than invented law or normative meaning.
25. Authority is distinct from Technical Capability. Ability to execute does not prove legitimacy to execute.
26. No universal Capacity object. SILT Core does not model Capacity as a universal primitive. Encounter-specific roles, offices, representative bases or legal capacities may remain relevant within a particular order or encounter, but they do not constitute a separate SILT Core object.
27. Attribution is distinct from Binding and liability. Correct Attribution does not itself determine downstream legal consequence.
28. Obligation is distinct from Authority. Required performance may persist independently of current Authority.
29. Cryptographic continuity is distinct from semantic continuity. Technical persistence does not prove semantic persistence, and semantic persistence need not depend upon technical identity persistence.
30. Semantic hand-off is not semantic surrender. Downstream systems may execute while SILT preserves relevant legitimacy semantics.
31. Conformance does not manufacture legitimacy. Technical validity of a Presentation or Profile Expression cannot create the legitimacy it purports to describe.
32. Core supplies grammar; originating orders retain meaning. SILT makes plural orders mutually legible without claiming jurisdiction over their ultimate ontology.

# 25. Explicit non-goals

SILT Core v0.2 does not attempt to do any of the following, and this list is non-exhaustive:

- determine universal legal validity;
- define universal personhood;
- determine the authenticity of cultural, customary, Indigenous or collective identity or belonging;
- define a universal method for collective representation;
- establish one universal authority issuer;
- require government recognition;
- require decentralised recognition;
- encode or exhaust the full normative substrate of any legal, customary, cultural, private, institutional or other order;
- reconcile incompatible ontologies;
- adjudicate conflicts between normative orders;
- replace credential systems;
- replace DID/VC systems;
- replace authentication protocols;
- replace dynamic authorisation systems;
- replace capability systems;
- replace policy engines;
- replace courts, arbitration or governance processes;
- determine universal Binding or liability.
- prescribe a universal combining, precedence or conflict-resolution rule for Profile Expressions;
- require every normative or relational condition to be machine-evaluable or reducible to bounded expression.

These systems and processes may interact with SILT.

They do not become SILT Core merely because they are adjacent to it.

# 26. Architectural summary

The conceptual centre of SILT Core v0.2 is the encounter.

A Participant arrives from somewhere.

That 'somewhere' is not reduced to an issuer.

It is represented through Source.

From that Source arises or is grounded a relational position: Standing.

The Participant does not need to reveal the whole relation.

Instead, for the purposes of a particular encounter, the Participant makes a bounded projection: Presentation.

The encounter may also receive one or more Profile Expressions: bounded, selective expressions of semantic conditions relevant to evaluation, arising from normative or relational substrates that remain outside and unencumbered by the expression.

Evaluation occurs at the encounter.

The encounter may be extended, iterative, staged or provisional rather than instantaneous.

Where multiple Profile Expressions are applicable, evaluation may produce distinct results under each expression. SILT does not silently merge or rank those results.

That evaluation may establish that relevant conditions are SATISFIED, NOT_SATISFIED or INDETERMINATE.

The evaluation does not thereby acquire jurisdiction over the Source from which Standing arose or over the normative substrate from which a Profile Expression arose.

Where the encounter proceeds, Authority, Consent, Reliance, Action, Attribution, Revocation and Obligation may become relevant.

Downstream technical systems may authenticate, authorise and execute.

SILT preserves the semantic thread that explains what those actions mean.

In compact form:

> SOURCE -> STANDING -> PRESENTATION -> EVALUATION AT THE ENCOUNTER  
>   
> applicable PROFILE EXPRESSION(S) inform evaluation without altering the architectural seam  
>   
> semantic relations continue where relevant -> technical / institutional hand-off

The aim is neither universalisation nor isolation.

> mutual legibility without ontological collapse.

# Freeze note

This document is Freeze Candidate 1 for the SILT Core v0.2 semantic architecture. It is based on RC4.1 and is intended for semantic freeze, subject only to release packaging, copy-editing and publication-level naming decisions.

FC1 introduces no new Core object, no new architectural seam and no change to the settled movement Source -> Standing -> Presentation -> evaluation at the encounter. The close-out records completion of the pre-freeze pressure tests and preserves the RC4.1 semantic decisions.

The pre-freeze gate has been completed through four normalised worked encounters, followed by machine-readable conformance validation and an experimental adjacent-protocol mapping.

The completed test set comprised:

- WE01 - Transferable Instrument Encounter: persistent Obligation, changing Standing, constitutive transfer / endorsement, and the non-collapse of technical control into relational position.
- WE02 - Credential-Carried Institutional Encounter: credential Evidence, current Standing, semantic continuity and the distinction between cryptographic validity and relational sufficiency.
- WE03 - Plural / Collective Encounter: conflicting Profile Expressions, contested provenance, collective Standing, representational Authority and deliberate non-expression where bounded expression would risk material distortion.
- WE04 - Recursive AI Delegation Encounter: Authority containment, semantic lineage, validity dependency, Revocation and execution without semantic collapse.

Across WE01-WE04, the machine-readable conformance suite and the experimental SILT-LCP semantic mapping, no recurring unnamed semantic concept, informal convention or material distortion was identified that requires reopening Core. The no-new-Core-primitive hypothesis therefore survives the pre-freeze gate for v0.2; it is not a claim that the architecture is complete for all future domains.

A full ecosystem and adjacent-standards comparison, together with concrete serialization or carrier bindings, belongs in versioned companion documentation rather than in this canonical semantic architecture. Named comparison with KERI/ACDC, UCAN, zcap and related systems, together with government and wallet trust-list positioning, remains intentionally routed to that companion material.

Project naming remains a publication-level question rather than a semantic blocker: this document uses “SILT” and “SILT Core” as project and specification names and does not infer or invent an acronym expansion.

Subject to a final release audit confirming packaging and terminology consistency, this candidate is ready for semantic freeze. After freeze, semantic changes to v0.2 should be handled transparently as errata or proposed for a subsequent version rather than introduced through silent revision.
