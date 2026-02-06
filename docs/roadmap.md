# Roadmap

This roadmap reflects SILT Core’s deliberate **spec-first, implementation-later** posture. The project prioritises semantic clarity, resilience, and interoperability over premature optimisation or platform lock-in.

The purpose of this repository is to define a stable identity interface surface that multiple implementations can later adopt, critique, or extend.

## Phase 0 – Specification and resilience foundation (current)

Focus:
- Normative specifications for principal, delegation, consent, and revocation
- Explicit threat modelling and misuse-case definition
- Minimal, flexible schemas for validation and interoperability

Status:
- Specifications complete at v0 semantic level
- Schemas intentionally minimal and extensible
- Misuse cases documented as test vectors-in-waiting

Outcome:
A coherent, auditable identity infrastructure layer that can be reasoned about, cited, and reviewed independently of any particular technology stack.

## Phase 1 – Misuse-case validation and test vectors (future)

Focus:
- Translate misuse cases into concrete test vectors
- Define expected pass/fail conditions for delegation, consent, and revocation handling
- Enable implementers to self-assess conformance to SILT Core semantics

Non-goals:
- No production systems
- No user-facing applications
- No chain- or wallet-specific code

Outcome:
A practical resilience harness that helps prevent common identity failure modes without prescribing architecture.

## Phase 2 – Minimal reference checks (optional, downstream)

Focus:
- Minimal reference logic to demonstrate policy enforcement
- Examples of validation against schemas and misuse cases
- Demonstration of deny-by-default postures for unclear authority or consent

Constraints:
- Reference code remains minimal, illustrative, and replaceable
- No assumption of custody models, wallets, or governance frameworks

Outcome:
Demonstrative clarity, not a canonical implementation.

## Phase 3 – Adapters and plural implementations (out of scope for now)

Focus:
- Mapping SILT Core semantics into diverse ecosystems
- Civil society, governance, and public-interest identity contexts
- Plural legal and cultural interpretations

This phase is intentionally deferred until the underlying semantics are mature and informed by research, writing, and plural-context engagement.

## Guiding principle

SILT Core values **clarity before scale**, **semantics before software**, and **exit before lock-in**.

Implementations may come and go. The integrity of the identity layer must endure.

