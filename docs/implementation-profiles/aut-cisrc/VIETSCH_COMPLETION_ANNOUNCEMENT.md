# SILT Core v0.1 research pilot: delegation and revocation for federated research infrastructure

**Public dissemination note — 23 October 2026**  
**Research lead:** Gareth Farry  
**With support from:** Stichting Vietsch (Vietsch Foundation)

How can a researcher or research assistant present a delegated right to act in a way another digital system can inspect, without pretending that the system itself created or verified the underlying authority?

That question motivated a six-month, Vietsch-supported SILT Core **v0.1** research proof of concept. The work developed a deliberately narrow example of university research governance: a supervisor grants a research assistant a bounded, time-limited delegation for a defined dataset-related action; the assistant's request is checked against the represented issuer chain, delegate, action, resource, purpose, time and applicable revocation.

The resulting **open reference implementation** includes a non-normative AUT CISRC implementation profile, five JSON Schemas, synthetic authority and request fixtures, a Python validation prototype, regression tests and a documented pilot evaluation. In the final recorded suite, **21 of 21 automated tests passed**, including negative cases, malformed-input handling and representative schema-conformance checks.

The result is significant but bounded. It demonstrates **inspectable, reproducible evaluation of an asserted delegation within a synthetic workflow**. It does **not** validate whether a supposed university authority is genuine, verify cryptographic credentials, issue live access rights, or establish official Auckland University of Technology endorsement. The AUT example is illustrative; it was not integrated into a production research information system and did not test interoperability between operational institutions.

### What this contributes

Delegation is often buried in application permissions, organisation-specific role lists or identity-provider policy. This pilot shows one approach to carrying an explicit, scoped delegation with an auditable expiry and revocation path, while leaving substantive institutional recognition and enforcement to the receiving systems. The implementation also surfaced an important distinction: an authority chain may be **structurally consistent without establishing its real-world legitimacy**.

The pilot applies the **historical SILT Core v0.1** delegation and revocation model. Its profile-specific JSON schemas are an implementation adaptation, not normative substitutes for the original v0.1 schemas. It is **not a migration to SILT Core v0.2**, which is a separate semantic architecture and publication.

### Read, inspect and reproduce

- **Permanent research record:** [Zenodo record 23579725](https://zenodo.org/records/23579725), [DOI 10.5281/zenodo.23579725](https://doi.org/10.5281/zenodo.23579725)
- **Versioned GitHub release:** [Vietsch AUT CISRC v0.1 pilot](https://github.com/Sugarlicks/silt-identity-core/releases/tag/aut-cisrc-v0.1-pilot-2026)
- **Detailed evaluation:** [Phase 3 pilot evaluation](phase-3-pilot-evaluation.md)
- **Executable tests:** [21/21 passing GitHub Actions evidence](https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516)
- **Project status:** [Public status and project record](VIETSCH_PUBLIC_STATUS.md)

The curated GitHub archive includes software under Apache License 2.0 and explicitly identified project-authored narrative work additionally available under CC BY 4.0 while historical Apache permissions remain. Five PNG diagrams were omitted from the archive pending a separate rights check.

The record is open for scrutiny, replication and research dialogue about the relationship between technical validation, delegation and authority across institutional boundaries. Any production adoption would require independent evidence authentication, institutional policy determination and further testing.

**Acknowledgement:** This work was made possible through financial support from Stichting Vietsch (Vietsch Foundation) for public-benefit research and education infrastructure. The foundation is not represented as an operational participant or certifier of the prototype.

*This announcement records the research and technical-publication outcome. Financial close-out is being handled separately under the signed MoU.*
