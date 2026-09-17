# Delegation — v0.1 archival notice

This file is retained as a **SILT Core v0.1 specification artefact** for historical and migration reference.

The original v0.1 Delegation specification treated delegation as a standalone universal authority-grant artefact issued by a Principal to an Agent or Delegate, with mandatory fields for Capacity, Scope, Duration, Revocation reference and delegation identifier. It also imposed Core-level `MUST` rules around explicit delegation references and default non-reliance.

That model is **not the controlling SILT Core v0.2 architecture**.

For v0.2, the canonical semantic reference is:

[`spec/v0.2/semantic-architecture.md`](./v0.2/semantic-architecture.md)

The settled v0.2 seam is:

> **Source → Standing → Presentation → evaluation at the encounter**

In v0.2, **Delegation is not a standalone universal Core primitive or mandatory artefact type**.

Where an applicable order recognises delegation, it may be represented as an **Action** through which derived **Authority** is constituted. The semantic effect of that Action depends on the relevant Source, Standing, Authority conditions and Profile Expression.

Several concerns expressed in the v0.1 document remain important, but their architectural location has changed:

- role names, membership, login state or technical permission do not by themselves establish Authority;
- derived Authority should not exceed the parent delegable envelope unless another recognised Source independently supplies additional Authority;
- any ability to create further derived Authority must be supported by the applicable Authority conditions rather than inferred;
- lineage, scope, validity dependencies and Revocation remain relevant semantic questions;
- Revocation is prospective by default unless another expressed rule provides otherwise;
- technical execution or possession of a capability does not itself establish semantic Authority.

What does **not** carry forward as universal v0.2 Core semantics is the v0.1 assumption that every delegated Action must reference one standardised delegation artefact with a fixed set of mandatory fields, or that SILT Core itself must produce a universal binary `authorised` / `unauthorised` or deny-by-default runtime conclusion.

Those operational choices may be entirely appropriate in a particular implementation profile. They are not universal Core requirements.

There is therefore **no one-to-one mapping from the v0.1 Delegation artefact to a single v0.2 object**. A v0.1 delegation may map across Action, Authority, Source, Evidence, Presentation, Revocation and Profile Expression depending on the encounter.

The original v0.1 contents remain available through Git history. They should be read as historical specification material and, where relevant, as context for v0.1 implementations such as the Vietsch / AUT CISRC research-delegation profile. They should not be used as normative v0.2 semantics.
