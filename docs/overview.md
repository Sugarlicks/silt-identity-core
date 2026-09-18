# SILT Core — Overview

**A fuller introduction to the SILT Core v0.2 semantic architecture.**

This document explains the purpose, architecture, semantic objects, encounter model, boundaries and current release position of SILT Core v0.2.

It is explanatory material. The controlling v0.2 semantic reference is:

[`spec/v0.2/semantic-architecture.md`](../spec/v0.2/semantic-architecture.md)

If this overview and the semantic architecture ever diverge, the semantic architecture controls.

For the shorter repository introduction, see [`README.md`](../README.md).

---

## 1. What SILT Core is trying to preserve

Digital systems increasingly mediate encounters between people, collectives, institutions, commercial arrangements, automated agents and other forms of organisation that do not necessarily derive legitimacy from the same source.

A customary order may recognise a relational position through whakapapa, collective process or community recognition. A private arrangement may ground authority in a trust, contract, instrument or appointment. An institution may rely on office, mandate or governance process. A technical system may recognise a key, account, credential or capability.

Those things are not interchangeable.

SILT Core addresses the boundary at which different orders meet.

Its purpose is to allow the minimum relevant semantic conditions of an encounter to become legible without requiring the originating order to collapse into the ontology of the receiving system.

The canonical architectural seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

This is the conceptual centre of v0.2.

SILT is therefore concerned with **encounter rather than assimilation**.

---

## 2. The architectural seam

### Source

A **Source** is the referenced ground or provenance of a relevant semantic relation.

A Source may be a relationship, genealogy or kinship connection, customary process, agreement, trust, mandate, constitution, appointment, governance event, community recognition, institutional instrument, private instrument, prior Authority or another recognised ground.

A Source is not automatically an issuer, registry, credential authority or document.

A document, credential, signature or registry entry may be **Evidence** of a Source-grounded relation without becoming the Source itself.

There is no universal Source.

### Standing

**Standing** is a relational position grounded in Source.

It is not a universal credential, status label or globally portable claim about what a Participant is.

Standing may concern a relationship, order, collective, object, office, domain, context or other bounded normative setting.

Standing may be distributed, contested or layered. In collective settings, recognised belonging or relational position does not automatically establish Authority to speak for, represent or bind the collective.

SILT Core v0.2 does **not** contain a `Status` object.

### Presentation

A **Presentation** is the encounter-specific, purpose-relevant act or envelope through which a Participant brings the minimum relevant projection of Standing, Authority or another semantic claim into a particular encounter.

Presentation does not create Standing.

A receiving Participant or system does not become the source of the underlying Standing merely because it evaluates a Presentation.

Presentation is intentionally broader than any one technical format. A verifiable presentation, signed message, legal instrument, API payload or other carrier may transport a Presentation, but the carrier is not the semantic definition.

### Evaluation at the encounter

Evaluation asks whether the Presentation satisfies the **expressed conditions relevant to that encounter**.

It is not a universal determination of legitimacy, truth or legal validity.

Evaluation does not compel acceptance, and it does not constitute, extinguish or redefine the underlying Source-grounded relation.

The Core semantic outcomes are:

- `SATISFIED`
- `NOT_SATISFIED`
- `INDETERMINATE`

SILT does not use a universal `INVALID` conclusion.

Missing or non-resolvable information is not silently converted into false invalidity.

---

## 3. Profile Expression

A **Profile Expression** is a bounded, encounter-relevant expression of the semantic conditions under which a Presentation will be evaluated.

It is not a representation of the full legal, customary, cultural, relational, contractual, institutional or other normative order from which it arises.

The originating substrate exceeds and remains independent of the Profile Expression.

A Profile Expression may express conditions concerning matters such as:

- relevant Sources;
- Standing conditions;
- what may need to be Presented;
- Evidence requirements;
- Authority conditions;
- Consent or Reliance conditions;
- Revocation;
- relevant Actions;
- Attribution;
- Obligation;
- downstream effects.

Multiple Profile Expressions may coexist within an encounter.

They may agree, overlap or conflict.

SILT does not silently merge, rank or privilege them. A result remains linked to the Profile Expression under which it was produced unless an expressed composition rule provides otherwise.

This is important in plural encounters. Mutual legibility does not require a universal meta-order.

---

## 4. Deliberate non-expression

Some conditions cannot be usefully or faithfully reduced into a bounded machine-readable expression without distortion.

SILT Core v0.2 therefore allows a condition to remain deliberately unexpressed where expressing it would materially misrepresent the originating order.

That condition does not acquire a fourth evaluation outcome.

It remains outside SILT evaluation for that encounter.

This distinction matters:

```text
INDETERMINATE
```

means that an expressed condition cannot presently be resolved.

A deliberately non-expressed condition is different: it was not placed inside the evaluation frame in the first place.

---

## 5. The semantic objects around the seam

The seam is the organising architecture, but several other semantic distinctions are needed to preserve meaning at the encounter.

### Participant

A **Participant** is deliberately thin.

It may refer to an individual, collective, office, institution, trust, DAO, machine agent or another relevant actor or entity.

SILT does not attempt to settle universal questions of personhood or identity through the Participant object.

### Evidence

**Evidence** supports a semantic claim. It is not the claim itself.

Examples may include credentials, signed records, documents, attestations, registries, transaction records, witness records or technical proofs.

A cryptographically valid credential may be Evidence while the current Standing or Authority it is offered to support remains unresolved.

### Authority

**Authority** is bounded power relevant to an Action or class of Action.

Authority may be grounded directly in Source, arise through Standing, be constituted through an Action such as appointment or delegation, or arise through another expressed path recognised by the applicable order.

Authority may be bounded by:

- action class;
- resource;
- value;
- purpose;
- time;
- place;
- delegation depth;
- formation conditions;
- exercise conditions;
- validity dependencies;
- revocation conditions.

SILT does not require Authority always to pass mechanically through Standing.

### Delegation

Delegation is not a separate universal Core primitive in v0.2.

It is modelled as an **Action** through which derived Authority may be constituted where the applicable Source and Profile Expression give that Action such effect.

Derived Authority cannot exceed the parent delegable envelope unless another recognised Source independently supplies additional Authority.

Lineage and current validity dependency are distinct. The fact that Authority descends historically from another Authority does not by itself mean that every later change automatically cascades through the lineage.

### Consent

**Consent** is a bounded relation of agreement or permission.

It is not reducible to a signature, checkbox, login state or technical assent event.

Those may be Actions or Evidence concerning Consent, depending on the applicable conditions.

Collective Consent must not be inferred from individual assent without the relevant Authority and conditions.

### Reliance

**Reliance** expresses the conditions under which another Participant may act on a Presentation, Authority or related semantic state.

Reliance is distinct from Authority validity.

SILT does not silently import doctrines such as apparent authority, estoppel or reliance-based liability. Those remain downstream or Profile-defined unless expressly modelled for the encounter.

### Action

An **Action** is an event capable of evaluation or, where the applicable order gives it constitutive effect, changing a semantic relation.

Examples may include appointment, admission, election, endorsement, transfer, agreement, delegation, revocation, discharge or another relevant event.

SILT separates an Action from the semantic consequence attributed to it.

### Attribution

**Attribution** is the semantic linking of an Action to a Participant, Authority context or relational position.

The factual actor and the Attribution target may differ.

For example, an agent may technically execute an Action while the applicable Authority relation supports Attribution to another Participant or office.

Attribution does not by itself establish Binding, liability or legal responsibility.

### Obligation

**Obligation** is a persistent relational state of required performance, responsibility or constraint.

It is distinct from Authority.

An Obligation may persist while:

- Standing changes;
- Authority changes;
- the Participant occupying an entitled position changes.

This distinction is especially important in transferable instruments and other settings where relational positions change while an underlying obligation survives.

### Revocation

**Revocation** alters or withdraws a revocable relation, especially Authority.

Authority may have lifecycle states such as active, revoked, expired, superseded or suspended where the relevant implementation or Profile Expression uses them.

Revocation is prospective by default unless another rule is expressly stated.

SILT does not impose a universal lifecycle on Standing.

---

## 6. What is not a Core primitive in v0.2

Several concepts present in earlier SILT material are intentionally not retained as universal Core objects.

### Status

`Status` is not a SILT Core v0.2 object.

The work previously carried by Status is better handled through Source-grounded Standing and encounter-specific Presentation.

### Capacity

`Capacity` is not a universal SILT Core v0.2 primitive.

A role, office, trusteeship, agency relation, representational position or other acting basis may remain highly relevant in a particular legal or institutional order. SILT does not deny those concepts.

It declines to impose one universal Capacity object across all orders.

Where relevant, those meanings are expressed through Source, Standing, Authority, Presentation and Profile Expression.

### Binding

**Binding** is not a universal Core conclusion.

An encounter may lead to:

- formation of an Obligation;
- change of Standing;
- creation or alteration of Authority;
- Revocation;
- discharge;
- settlement;
- institutional recognition;
- another downstream effect.

What follows depends on the applicable Profile Expression or other recognised normative mechanism.

SILT therefore separates semantic evaluation from the false proposition that successful evaluation means “legally binding everywhere”.

---

## 7. Technical Capability is not semantic Authority

SILT is deliberately strict about the boundary between semantic relations and technical machinery.

A key may sign.  
A token may authorise an API call.  
A wallet may control an asset.  
A session may be valid.  
An access-control system may permit execution.  
An agent framework may successfully perform a task.

None of those facts alone establishes SILT Standing or Authority.

SILT calls the practical ability to cause a technical effect **Technical Capability**.

Authentication, key continuity, credentials, capability tokens, sessions, access control, policy engines and execution systems are operational machinery. They sit architecturally below the Presentation line unless a semantic claim about them is itself relevant to the encounter.

The distinction is:

```text
Technical Capability ≠ Authority
execution ≠ origination
credential validity ≠ Standing
key continuity ≠ semantic continuity
```

This is an architectural boundary, not a chronological rule. Technical systems may operate before, during or after a Presentation in real implementations.

---

## 8. Semantic continuity and cryptographic continuity

SILT distinguishes continuity of meaning from continuity of technical control.

Changes to:

- keys;
- credentials;
- accounts;
- capability tokens;
- sessions;
- technical identifiers;
- execution infrastructure

do not by themselves alter Standing, Authority, Attribution or Obligation.

Conversely, continuing control of a key, account or credential does not guarantee that the underlying semantic relation still exists.

This allows SILT semantics to survive ordinary technical events such as key rotation, credential replacement or infrastructure migration without pretending those events are irrelevant operationally.

---

## 9. Relationship to existing infrastructure

SILT Core is designed to complement, not replace, identity, credential, capability, agent and execution systems.

### DID and verifiable credential systems

DIDs and verifiable credentials can provide identifier control, attestations, selective disclosure and transport for Evidence.

They do not automatically create Source-grounded Standing or Authority.

A verifiable presentation may carry a SILT Presentation, but the two are not identical concepts.

### Digital signatures

A signature is Evidence that a particular key performed a technical signing operation.

Whether that Action is sufficient for Standing, Consent, Authority, Attribution or another semantic conclusion depends on the applicable Source and Profile Expression.

### Capability and authorisation systems

Capability systems and dynamic authorisation protocols can express and enforce technical permission.

They are valuable downstream machinery.

SILT’s concern is the semantic meaning that precedes, accompanies or survives that technical capability.

### AI agents

SILT does not create a special AI ontology or require AI systems to be treated as legal persons.

The same architecture can represent a machine agent as a thin Participant, distinguish its Technical Capability from its Authority, and preserve delegation lineage, constraints, revocation and Attribution without adding an AI-specific Core primitive.

### Smart contracts and automated execution

Automated systems can execute logic once their operational conditions are met.

SILT does not replace that execution layer. It allows the semantic conditions surrounding an Action to remain legible before or alongside execution and after the technical mechanism changes.

### Trust registries and issuer lists

Trust lists and registries may be useful Evidence or implementation infrastructure.

SILT does not treat registry inclusion as the universal origin of Standing or Authority.

---

## 10. Why plural encounters matter

The architecture becomes most distinctive where the Source of Standing does not originate in the receiving system.

Standing may arise from:

- whakapapa;
- customary process;
- community recognition;
- a trust;
- a private agreement;
- institutional appointment;
- merchant practice;
- a governance process;
- another recognised relation.

SILT does not certify those Sources as universally valid.

It gives them a disciplined way to become legible at the boundary.

The receiving order can evaluate the minimum relevant Presentation without claiming jurisdiction over, or exhaustive representation of, the originating order.

A receiver may conclude that its own conditions are not satisfied. That conclusion does not erase the underlying Standing.

This is the point of the encounter architecture:

> **mutual legibility without ontological collapse**

---

## 11. Worked encounter pressure tests

The v0.2 architecture was pressure-tested before freeze through four normalised worked encounters.

### WE01 — Transferable instrument

Tested persistent Obligation, changing Standing, constitutive transfer or endorsement, wrongful technical control, custodial control and incomplete lineage.

It confirmed that technical possession or control does not automatically create Standing and that an Obligation may persist while the entitled relational position changes.

### WE02 — Credential-carried institutional encounter

Tested the relationship between credentials, Evidence, Standing, Authority, key rotation and selective disclosure.

It confirmed that credential validity and semantic sufficiency are distinct.

### WE03 — Plural / collective encounter

Tested collective Standing, representational Authority, contested Profile Expression provenance, incompatible conditions across Profile Expressions and deliberate non-expression.

It confirmed that SILT does not need a universal meta-order to rank competing normative expressions.

### WE04 — Recursive AI delegation

Tested derived Authority, delegation depth, scope containment, lineage, current validity dependencies, Revocation and successful execution without semantic Authority.

It confirmed that no special AI primitive is required for v0.2.

Across the four encounters, no recurring unnamed concept was identified that required a new Core primitive.

That is evidence for the v0.2 freeze decision, not a claim that SILT is complete for every future domain.

---

## 12. Threat and misuse posture

SILT Core is concerned with semantic failure as well as software failure.

Recurring risks include:

- technical permission being mistaken for Authority;
- stale Authority surviving after its semantic basis has changed;
- credentials being treated as the relation they evidence;
- collective membership being treated as representational Authority;
- delegation silently expanding beyond the parent envelope;
- one Profile Expression being treated as universally authoritative;
- deliberate non-expression being misclassified as failure;
- key continuity being mistaken for semantic continuity;
- successful execution being mistaken for Attribution or Binding;
- receiving systems treating verification as jurisdiction over the represented reality.

The point is not to make every encounter computationally decidable.

It is to prevent technical systems from silently manufacturing semantic conclusions that the originating order did not supply.

---

## 13. Use domains

SILT Core is intended to be domain-neutral, but the architecture has been developed against materially different encounter types, including:

- direct peer-to-peer interactions;
- digital commerce and transferable instruments;
- private ordering and trusts;
- institutional delegation;
- recursive AI-agent delegation;
- DAO and treasury governance;
- collective and customary authority;
- consent-only encounters;
- credential-carried institutional interactions.

These domains are tests of the grammar, not separate SILT ontologies.

---

## 14. Vietsch / AUT CISRC implementation profile

The Vietsch / AUT CISRC research-delegation implementation remains intentionally a **SILT Core v0.1 implementation**.

It is being completed on the architecture against which the funded implementation began.

The profile, schemas, examples and reference validator should therefore continue to be read as v0.1 implementation material. They are not being rewritten mid-stream to appear natively v0.2-compliant.

A later, separate migration analysis may compare the completed v0.1 implementation against v0.2 and classify elements as:

- `UNCHANGED`;
- `RENAMED / REMAPPED`;
- `SPLIT`;
- `NO LONGER CORE`;
- `MISSING`.

That later analysis will not alter the historical or funded basis of the Vietsch implementation.

---

## 15. Current release position

### v0.1

Released as the initial public SILT Core specification and implementation-learning baseline.

Some v0.1 concepts and artefacts remain useful historically and operationally, but several have been superseded by the v0.2 architecture.

### v0.2

SILT Core v0.2 is at **Freeze Candidate 1** and is undergoing final release packaging.

The canonical semantic reference is:

[`spec/v0.2/semantic-architecture.md`](../spec/v0.2/semantic-architecture.md)

FC1 is based on the RC4.1 close-out following the worked-encounter gate, machine-readable conformance validation and an experimental LCP mapping.

The v0.1 → v0.2 repository reconciliation is recorded in [`docs/migration/v0.1-to-v0.2-repository-audit.md`](./migration/v0.1-to-v0.2-repository-audit.md).

The current remaining release work is editorial, structural and publication-facing. It should not become a back door for semantic redesign.

---

## 16. Repository orientation

The v0.2 FC1 repository now contains more than one architectural generation, with explicit boundaries between them.

The intended hierarchy is:

```text
spec/v0.2/semantic-architecture.md
    canonical v0.2 semantic reference

docs/
    explanatory, positioning, migration, threat-model and companion material

tests/conformance/v0.2/
    worked encounters, fixture schema, machine-readable test material and experimental mappings

spec/ legacy topic files
    historical v0.1 material retained with explicit archival notices

schemas/implementation-profiles/
    protected implementation-profile schemas rather than generic v0.2 Core schemas

reference/
    non-normative implementation reference material, currently including the AUT/Vietsch v0.1 validator

examples/ and implementation profiles/
    non-normative implementation material
```

The generic v0.1 root schemas and obsolete empty placeholders have already been removed from the active FC1 surface. AUT/Vietsch remains intentionally on its v0.1 basis.

The distinction between normative semantic architecture, companion documentation, conformance notation, implementation profiles and reference code is load-bearing.

---

## 17. What SILT Core does not claim

SILT Core does not claim to be:

- a universal identity system;
- a credential system;
- a universal verifier;
- an authentication framework;
- a general access-control system;
- a complete model of law, custom or culture;
- a universal authorisation engine;
- a conflict-of-laws engine;
- a universal rule for combining Profile Expressions;
- a guarantee that every normative condition can be made machine-evaluable;
- a universal determination of Binding, liability or enforceability;
- a requirement that a receiving party accept a Presentation.

SILT’s claim is narrower:

> It provides a semantic architecture through which different orders can make the minimum relevant conditions of an encounter mutually legible without requiring semantic surrender.

---

## Closing note

SILT Core v0.2 does not begin from the proposition that one system must certify the legitimacy of all others.

It begins from the encounter.

A Participant may bring a Source-grounded relational position into that encounter through a bounded Presentation. One or more Profile Expressions may state what the receiving side needs to evaluate. The result may support action, reliance or another downstream effect, but SILT does not convert that result into universal recognition.

The originating relation remains where it began.

> **Source → Standing → Presentation → evaluation at the encounter**
>
> **semantic hand-off, not semantic surrender**