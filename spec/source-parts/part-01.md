SILT Core v0.2

Semantic Architecture

Release Candidate 2 | 18 September 2026

| **Status** | Release Candidate 2                                                        |
|------------|----------------------------------------------------------------------------|
| **Role**   | Canonical semantic reference for SILT Core v0.2, pending final release tag |
| **Scope**  | Semantic architecture, not implementation specification                    |
| Repository | https://github.com/Sugarlicks/silt-identity-core                           |
| Licence    | CC BY 4.0 for the specification text; see LICENSING.md for package scope   |

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

## 0.2 Specification status and licence

This document is the normative semantic architecture for SILT Core v0.2 Release Candidate 2. Normative requirements are identified by the capitalised BCP 14 terms defined above.

Supporting conformance fixtures and experimental mappings are non-normative unless expressly stated otherwise. They test and illustrate the architecture; they do not add Core semantics by implication.

This specification is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). That copyright licence does not itself grant patent, trademark or certification rights. The release package contains separate licensing, IPR and conformance notices.

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
> \|  
> v  
> STANDING  
> \|  
> v  
> PRESENTATION  
> \|  
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

