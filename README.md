# SILT Core

**A semantic architecture for encounters across plural orders.**

SILT Core enables participants operating under different legal, cultural, customary, private, institutional or technical orders to become mutually legible at moments of encounter without requiring those orders to collapse into a single ontology or surrender their own sources of authority.

Its canonical architectural seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

SILT is concerned with encounter rather than assimilation.

A **Source** is the referenced ground or provenance of a relevant relation. **Standing** is a relational position grounded in Source. **Presentation** is the present-tense, purpose-relevant act or envelope through which a Participant brings the minimum relevant projection of that Standing into a particular encounter. Evaluation then asks whether the Presentation satisfies the expressed conditions applicable to that encounter.

A **Profile Expression** may supply those encounter-relevant conditions. It is a bounded expression, not a representation of the whole legal, cultural, customary, contractual, institutional or other normative order from which it arises. The originating substrate remains independent of, and exceeds, any Profile Expression.

SILT therefore standardises a boundary at which relational legitimacy can become selectively legible. It does not standardise the underlying ontology.

---

## What SILT Core is for

Digital systems are good at recognising accounts, identifiers, credentials, signatures, permissions and technical capabilities.

Those things matter, but they do not answer every semantic question that arises when different participants or orders meet.

A key can sign without establishing Standing.  
A credential can be valid without establishing current Authority.  
A capability can permit execution without establishing that the action is semantically authorised.  
A successful transaction does not by itself determine Attribution, Obligation or Binding effect.

SILT keeps those distinctions visible.

The v0.2 architecture includes semantic treatment of:

- **Participant** — a deliberately thin encounter referent;
- **Source** — the claimed ground or provenance of a relevant relation;
- **Standing** — a relational position grounded in Source;
- **Presentation** — the bounded present-tense projection brought into an encounter;
- **Profile Expression** — encounter-relevant conditions without ontological capture;
- **Evidence** — material supporting a claim, distinct from the claim itself;
- **Authority** — bounded power relevant to an Action or class of Action;
- **Consent** — a bounded relation of agreement or permission;
- **Reliance** — expressed conditions under which another Participant may act on a Presentation or Authority;
- **Action** — an event capable of being evaluated or, where the applicable order gives it effect, changing relational states;
- **Attribution** — the semantic linking of an Action to a Participant, Authority context or relational position;
- **Obligation** — a persistent relational state of required performance, responsibility or constraint;
- **Revocation** — the prospective withdrawal or alteration of a revocable relation, especially Authority.

**Binding is not a universal SILT Core conclusion.** The downstream effect of an encounter remains defined by the applicable Profile Expression or other recognised normative mechanism.

---

## The boundary SILT protects

SILT Core is **semantically thick and operationally thin**.

It preserves distinctions needed for meaning across an encounter while leaving authentication, credential formats, key management, capability tokens, sessions, runtime authorisation, policy engines, transport and execution machinery to downstream systems.

This means SILT deliberately distinguishes:

```text
semantic Standing        != credential possession
semantic Authority       != technical capability
semantic continuity      != cryptographic continuity
evaluation               != compulsory acceptance
Attribution              != Binding or liability
```

Existing systems such as DID/VC infrastructure, capability systems, agent identity frameworks, access-control systems and execution environments may carry Evidence, transport Presentations or execute resulting actions. They do not thereby become the universal source of the semantic relations SILT represents.

> Technical systems may carry execution. SILT preserves meaning.

---

## Evaluation

SILT evaluation is scoped to the conditions expressed for the encounter.

The Core semantic outcomes are:

- `SATISFIED`
- `NOT_SATISFIED`
- `INDETERMINATE`

A condition that has deliberately not been expressed because bounded expression would materially distort it does **not** acquire a fourth SILT outcome. It remains outside SILT evaluation for that encounter.

Where multiple Profile Expressions apply, a Presentation is evaluated separately under each applicable expression unless an explicit composition rule says otherwise. SILT does not silently merge, rank or privilege them.

Legibility does not compel recognition. Evaluation does not constitute, extinguish or redefine the underlying Source-grounded Standing.

---

## Current status

### v0.1

**v0.1 is released.** It established the initial public framing, early semantic objects, schemas, misuse cases and reference validation experiments.

Some v0.1 terminology and artefact structures have been superseded by v0.2. In particular, **Status is not a SILT Core v0.2 object**, and **Capacity is not retained as a universal Core primitive**.

### v0.2

**SILT Core v0.2 is at Freeze Candidate 1 and is undergoing release packaging and repository reconciliation.**

The canonical semantic reference is:

[`spec/v0.2/semantic-architecture.md`](./spec/v0.2/semantic-architecture.md)

FC1 is based on the RC4.1 close-out and follows four worked-encounter pressure tests, machine-readable conformance validation and an experimental adjacent-protocol mapping. No new Core primitive was required by that pre-freeze gate.

The repository is being reconciled so that older v0.1 topic specifications, schemas and examples do not appear to override the v0.2 semantic architecture. Until that work is complete, **the v0.2 semantic architecture above is the controlling v0.2 reference**.

---

## Vietsch / AUT CISRC implementation profile

The AUT CISRC research-delegation work remains intentionally a **SILT Core v0.1 implementation**.

It is being completed on its original v0.1 basis rather than being rewritten mid-stream as a v0.2 implementation. The profile, schemas, examples and reference validator remain non-normative implementation material.

A later migration analysis may compare the completed v0.1 implementation against v0.2, but that is separate work and does not change the basis of the Vietsch / AUT CISRC implementation.

Profile documentation:

`docs/implementation-profiles/aut-cisrc/`

Profile schemas:

`schemas/implementation-profiles/aut-cisrc/`

Example artefacts and tests:

`examples/aut-cisrc-research-delegation/`

Reference validator prototype:

`reference/validators/aut-cisrc-delegation/`

---

## What SILT Core is not

SILT Core is not:

- a universal identity system;
- a credential issuer;
- a wallet or blockchain protocol;
- an authentication or access-control stack;
- a universal authorisation engine;
- a registry of legitimate people, communities or authorities;
- a complete representation of any legal, cultural or customary order;
- a conflict-of-laws engine;
- a claim that a Presentation must be accepted;
- a universal determination of legal validity or Binding effect.

Its role is narrower and more exact: to make the minimum relevant semantic conditions of an encounter legible without requiring the originating order to surrender the basis on which those conditions have meaning.

---

## Repository orientation

The repository currently contains:

- the v0.2 canonical semantic architecture under [`spec/v0.2/`](./spec/v0.2/);
- v0.1-era topic specifications and schemas undergoing release reconciliation;
- documentation and threat-model material;
- non-normative implementation profiles;
- experimental reference validators and examples;
- misuse-case and conformance material.

The distinction between **normative semantic architecture**, **companion documentation**, **implementation profiles**, **test notation** and **reference code** is load-bearing and will remain explicit through the v0.2 release process.

For the fuller repository overview, see [`docs/overview.md`](./docs/overview.md). That document is itself being reconciled against FC1 during the v0.2 release pass.

---

## Licence

The repository currently includes an Apache License 2.0 root licence. The v0.2 release packaging will state the licence boundary for specification/documentation and reference code explicitly.

---

## Contact

Website: [siltcore.org](https://siltcore.org)  
Repository: [github.com/Sugarlicks/silt-identity-core](https://github.com/Sugarlicks/silt-identity-core)

---

> **Source → Standing → Presentation → evaluation at the encounter**
>
> Mutual legibility without ontological collapse.
