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
> \|  
> v  
> Authority may be constituted  
>   
> endorsement  
> \|  
> v  
> Standing may change  
>   
> agreement  
> \|  
> v  
> Obligation may arise  
>   
> revocation  
> \|  
> v  
> Authority may become REVOKED  
>   
> performance  
> \|  
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

