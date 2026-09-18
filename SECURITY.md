# Security policy

SILT Core v0.2 is a semantic specification with non-normative conformance, mapping and reference artefacts. Security concerns may therefore be technical, semantic or both.

## Current status

The current release line is SILT Core v0.2. Reference code, experimental bindings and implementation profiles are non-normative unless expressly stated otherwise. AUT CISRC remains a SILT Core v0.1 implementation profile and is outside the v0.2 conformance claim.

SILT Core should not be treated as a production security product or legal-validity engine.

## Relevant security issues

Useful reports include, but are not limited to:

- technical flaws in conformance tooling, schemas or reference code;
- semantic inferences that collapse credential validity into Standing or Authority;
- treatment of Technical Capability as semantic Authority;
- silent precedence or merger of conflicting Profile Expressions;
- inference that collective Standing authorises representation, binding or disclosure;
- revocation behaviour that assumes cascades not expressed by the relevant Source or conditions;
- failures to preserve semantic lineage through delegation or agent hand-off;
- treatment of deliberate non-expression as absence or failure;
- documentation that overstates legal, customary, cultural or institutional legitimacy; and
- implementation behaviour that invents unstated normative rules in order to force a determinate result.

## Cryptographic and semantic continuity

A change of keys, credentials, sessions or capability artefacts does not by itself terminate semantic Standing or Authority. Conversely, technical continuity or successful runtime execution does not prove semantic continuity. Implementations should keep these questions separate.

## Reporting

If GitHub private vulnerability reporting is enabled, use that channel. If it is not available, open a minimal public issue requesting a secure contact route and do not publish exploit details, live keys, confidential instruments, personal data or other sensitive material.

A useful report identifies the affected artefact, the failure, whether it is technical or semantic, the likely impact, and a reproducible test or worked encounter where possible.

## No warranty

SILT Core materials are provided for specification, research, interoperability and implementation work. They are not legal advice, a production security guarantee or a determination of enforceability in any jurisdiction or normative order.

See `LICENSING.md` and `IPR_POLICY.md`.
