# Migration guidance — SILT v0.1-era materials to v0.2

This note is deliberately semantic rather than field-by-field. Older SILT implementations were built while the Core model was still moving, so a mechanical rename can preserve the wrong architecture.

## Migration rule

Classify every v0.1-era element as one of:

`UNCHANGED` · `RENAMED/REMAPPED` · `SPLIT` · `NO LONGER CORE` · `MISSING`

Do not map an older term into v0.2 merely because the names look similar.

## Principal remappings

| Older concept / pattern | v0.2 treatment | Migration class |
| --- | --- | --- |
| Status as a universal object | Remove. Ask whether the underlying claim is relational Standing, Evidence, a Profile Expression condition, or an implementation-specific state. | NO LONGER CORE / REMAPPED |
| Standing as credential-like state | Re-model as Source-grounded relational position. | REMAPPED |
| Implicit encounter payload | Make Presentation explicit where a Participant brings a bounded projection into an encounter. | MISSING / SPLIT |
| Lex / broad Profile / interpretive envelope | Map to Profile Expression only where it is a bounded, selective, non-exhaustive expression of encounter conditions. Do not treat it as the originating order. | RENAMED/REMAPPED |
| Capacity as a universal primitive | Remove. Domain-specific legal capacity, office, role or representative basis may remain relevant under Source / Profile Expression, but is not a universal Core object. | NO LONGER CORE |
| Capability / token / credential as Authority | Separate Technical Capability and Evidence from semantic Authority. | SPLIT |
| Verifier success as semantic validity | Replace with condition-level encounter evaluation. | SPLIT |
| Binary pass/fail or ad hoc result strings | Use SATISFIED / NOT_SATISFIED / INDETERMINATE only. Keep not-evaluated states separate. | REMAPPED |
| Binding as automatic Core conclusion | Move to Profile-defined or other downstream effect. | NO LONGER CORE / REMAPPED |
| Collective membership implies power to represent | Separate collective Standing from representational Authority. | SPLIT |
| Full-chain replay for every downstream agent action | Preserve reconstructable semantic lineage; repeated upstream Presentation is not universally required. | REMAPPED |

## Existing validators

A v0.1-era validator can remain useful where it checks delegation, scope, revocation or evidence integrity, but its outputs must be reclassified against the v0.2 seam. In particular, a validator MUST NOT treat technical success, credential validity, key control or capability possession as a substitute for Source-grounded Standing or Authority.

## AUT CISRC is outside this migration scope

The AUT CISRC delegation / revocation work remains a **SILT Core v0.1 implementation profile**. It is not being migrated to v0.2 and MUST NOT be retrofitted, renamed or reclassified merely to resemble the v0.2 architecture.

The AUT artefacts should be completed, tested, documented and archived under the v0.1 model against which they were built. Their continued presence in the repository is historical and implementation evidence, not a claim of v0.2 conformance. Any future decision to build an AUT use case against v0.2 would constitute a new implementation exercise rather than a migration requirement.
