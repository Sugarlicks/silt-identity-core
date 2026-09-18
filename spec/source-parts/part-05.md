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
> \|  
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

