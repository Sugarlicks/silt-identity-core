# SILT Core

**Authority semantics for digital action.**

Current digital systems are built on an epistemological assumption: 
legitimacy flows from external validation.

A government issues your identity.
A credential authority attests your attributes.
A platform recognises your account.
A system grants your permissions.

You exist, digitally, to the extent that external systems confirm you.

SILT begins from the other direction.

What a person, collective, institution, or agent carries into a moment 
of digital action — standing, authority source, mandate, obligation, 
consent, reliance, and revocation — does not begin with system 
recognition. It precedes it.

Current infrastructure has no stable grammar for this. It can model 
who you are, what attributes you hold, and what permissions you have 
been granted. It cannot model what you bring into an action, in what 
capacity you are acting, by whose authority, under what mandate, and 
whether others may safely rely on the act.

SILT builds that grammar.

SILT Core is a semantic layer for expressing the conditions of lawful 
digital action across plural systems.

It is not a credential system.
It is not a permission layer.
It is not a blockchain protocol.
It is not a legaltech-only product.

It is the missing authority layer beneath these systems: the layer 
that asks not merely:

> Has this action been permitted?

but:

> By what source of authority is this action being taken, in what 
> capacity, under what mandate, within what scope, with what consent, 
> and how can that authority be revoked?

---

## The distinction that matters

Most identity systems ask: *Who is this?*

Most permission systems ask: *What is this account allowed to do?*

SILT asks: *What is the authority structure behind this action?*

An action may be technically permitted but not legitimately authorised. 
Every time a person, collective, AI agent, institution, or automated 
system touches a digital environment — signs, files, transfers, votes, 
delegates, consents, or instructs — the conditions of that touch are 
invisible to the system receiving it.

SILT makes them visible.

---

## Status

**v0.1** is released. It establishes the initial semantic layer, 
core primitives, machine-readable schemas, threat model, misuse case 
test vectors, and a reference consent validator under 
`/reference/validators/consent`.

**v0.2** is in active development. Current work is deepening the 
primitive set through primary research across agency law, fiduciary 
doctrine, legal pluralism, orality and institutional recognition, and 
the philosophical foundations of standing and obligation across legal 
traditions. The v0.2 work expands SILT's semantic scope to support 
plural legal and governance systems and to address non-individual and 
non-human holders: collectives, trusts, AI agents, tribal entities, 
and offices.

---

## Further reading

Full documentation, primitives, use cases, threat models, roadmap, 
and interoperability notes are in [`/docs/overview.md`](./docs/overview.md).

Normative specifications are in [`/spec`](./spec).

---

## Licence

Apache License 2.0. See [`LICENSE`](./LICENSE).

---

## Contact

Website: [siltcore.org](https://siltcore.org)
Repository: [github.com/Sugarlicks/silt-identity-core](https://github.com/Sugarlicks/silt-identity-core)

---

*As digital systems become more autonomous, the future problem is 
not only identity verification. It is authority legibility. SILT 
Core provides a grammar for that legibility.*
