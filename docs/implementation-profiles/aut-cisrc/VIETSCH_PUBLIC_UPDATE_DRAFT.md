# Draft public project update — Vietsch SILT Core v0.1

**Publication status: Draft; not yet posted to project status page**  
**Prepared:** 23 October 2026

## SILT Core v0.1: AUT CISRC proof-of-concept evaluation

With support from Stichting Vietsch (Vietsch Foundation), SILT Core has completed the Phase 3 technical evaluation of a constrained delegation and revocation proof of concept for federated research infrastructure.

The implementation represents a limited research delegation, an asserted authority chain, a time-bound request and applicable revocation records as inspectable JSON artefacts. A lightweight Python validator checks the selected delegation, temporal and revocation conditions. The expanded regression suite passed **21 out of 21 automated tests**, including negative and JSON Schema conformance cases.

The AUT CISRC implementation profile is **non-normative**, built against **SILT Core v0.1**, and deliberately uses synthetic university example data. It does not describe a live AUT access system, constitute institutional endorsement or verify the legal origin of an asserted authority chain. A positive test result signifies satisfaction of the prototype's selected rules, not a university access grant.

The project now moves to the final release and archival package: a clearly identified v0.1 specification and versioned implementation record, licence reconciliation, Zenodo publication and a dissemination summary for the research and education infrastructure community.

**Public evidence:** [Merged technical work](https://github.com/Sugarlicks/silt-identity-core/pull/6) · [Pilot evaluation report](https://github.com/Sugarlicks/silt-identity-core/blob/main/docs/implementation-profiles/aut-cisrc/phase-3-pilot-evaluation.md) · [21-test CI record](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516)

This funded v0.1 implementation is separate from the later SILT Core v0.2 Semantic Architecture release.
