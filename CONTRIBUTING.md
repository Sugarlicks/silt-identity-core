# Contributing to SILT Core

SILT Core welcomes critique, worked encounters, implementation evidence, documentation improvements and carefully scoped semantic proposals.

The v0.2 architectural seam is:

> **Source -> Standing -> Presentation -> evaluation at the encounter**

The current Semantic Architecture is canonical over older repository material.

## Contribution categories

A contribution should identify itself as one of: normative Core; conformance; explanatory documentation; experimental binding; implementation profile; reference code; research or issue evidence.

Small editorial corrections may be submitted directly. Major semantic changes SHOULD begin with an issue.

## Semantic contribution discipline

A proposal to change Core semantics MUST identify the concrete problem and why the current architecture cannot express it. Where possible it should include a worked encounter or negative test.

Please do not reintroduce the following as universal Core objects or assumptions without a demonstrated architecture failure:

- `Status`;
- `Capacity`;
- a universal Holder role;
- credential or verifier success as Standing;
- Technical Capability as Authority;
- collective belonging as authority to represent a collective;
- a single canonical Profile Expression or meta-order;
- Binding as an automatic Core conclusion.

Profile Expression is a bounded, selective and non-exhaustive expression of encounter-relevant conditions. Presentation is the encounter-specific act or envelope through which a Participant brings a bounded projection of Standing. They are distinct constructs and are not parallel architectural spines.

SILT Core has exactly three evaluation outcomes: `SATISFIED`, `NOT_SATISFIED`, and `INDETERMINATE`. Conditions outside evaluation must remain separate from that vocabulary.

## Tests and examples

A conformance contribution should distinguish:

- condition-level SILT evaluation;
- conditions not evaluated;
- prohibited inferences;
- expected implementation conformance; and
- whether the architecture successfully detects the tested behaviour.

Negative tests are especially useful where a technically successful implementation could still make an invalid semantic inference.

## Adjacent standards

When proposing an external standard or protocol, state what layer it occupies and whether it complements, overlaps with, competes with or risks collapsing the SILT semantic layer. Named external standards are non-normative unless explicitly incorporated through the Core change process.

## Licensing of contributions

Narrative specification and documentation contributions are accepted for publication under **CC BY 4.0**. Reference code and machine-readable implementation/conformance artefacts are accepted under **Apache License 2.0**, unless a file states otherwise.

By submitting a contribution, you represent that you have the right to submit it under the applicable licence. Do not submit third-party material that cannot lawfully be redistributed under that licence.

## Patent/IPR boundary

SILT's direction is royalty-free implementability of the public specification. The current interim IPR policy does not yet create a complete standards-body patent commitment for all contributors.

A normative contribution that may introduce a patent claim necessarily implicated by implementation MUST disclose that issue to the maintainers. Maintainers may defer or reject such a contribution until an adequate royalty-free or non-assertion position is documented. See `IPR_POLICY.md`.

## Before a major pull request

Please explain the problem, affected section or artefact, proposed change, normative status, conformance impact and any IPR concern. For a semantic change, include the failure case that earns reopening Core.
