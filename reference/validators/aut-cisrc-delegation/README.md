# AUT CISRC Delegation Validator

**Status:** Draft
**Profile:** AUT CISRC Implementation Profile
**Relationship to SILT Core:** Non-normative reference prototype

## Purpose

This folder will contain the lightweight reference validator for the AUT CISRC implementation profile.

The validator checks whether an access request is valid against:

* a delegation artefact;
* an access request;
* a revocation event or revocation log;
* authority-chain information.

The validator is a prototype only.

It does not connect to live AUT systems.
It does not replace IAM.
It does not perform KYC.
It does not assess legal validity of source documents.
It does not modify SILT Core v0.1.

## Intended Input Files

The validator is expected to accept portable JSON artefacts such as:

```text
delegation.json
access-request.json
revocation-log.json
authority-chain.json
```

## Intended Output

The validator should return a deterministic validation result:

```json
{
  "result": "ALLOW",
  "reasonCode": "ALLOW",
  "reason": "The request is within delegated scope and no revocation applies.",
  "validatedAt": "2026-08-15T10:00:00Z",
  "validatorVersion": "aut-cisrc-profile-v0.1"
}
```

or:

```json
{
  "result": "DENY",
  "reasonCode": "DELEGATION_EXPIRED",
  "reason": "The requested action occurred after the delegation expiry date.",
  "validatedAt": "2026-08-15T10:00:00Z",
  "validatorVersion": "aut-cisrc-profile-v0.1"
}
```

## Initial Validation Checks

The validator should check:

1. Required artefacts are present.
2. Delegation object is structurally valid.
3. Access request object is structurally valid.
4. Authority chain is present.
5. Issuer has authority to issue the delegation.
6. Request actor matches the delegate.
7. Requested action is permitted.
8. Requested resource is within scope.
9. Requested purpose is within scope.
10. Request timestamp is within the effective period.
11. Delegation has not expired.
12. Delegation has not been revoked.
13. If revoked, the revoking authority is valid.

## Initial Reason Codes

```text
ALLOW
SCHEMA_INVALID
AUTHORITY_CHAIN_MISSING
ISSUER_NOT_AUTHORISED
ACTOR_NOT_DELEGATE
ACTION_NOT_PERMITTED
RESOURCE_OUT_OF_SCOPE
PURPOSE_OUT_OF_SCOPE
DELEGATION_NOT_YET_ACTIVE
DELEGATION_EXPIRED
DELEGATION_REVOKED
REVOCATION_AUTHORITY_INVALID
EVIDENCE_CHAIN_MISSING
```

## Revocation Logic

For this implementation profile, a revocation event is valid where the revoking actor is:

* the original delegator;
* a higher-order authority in the relevant authority chain;
* an authorised committee, agency, or subunit with delegated authority over the relevant governance domain.

The validator should deny future requests where a valid revocation event applies before the request timestamp.

For Phase 2, revocation affects future validation requests only. Pending-action treatment is out of scope.

## Evidence Handling

Authority resolves to an evidential chain based on documents.

For this lightweight prototype, evidence documents are treated as referenced metadata.

The validator may return a warning where evidence references are missing, but evidence verification is not required.

In strict mode, missing evidence may return:

```text
EVIDENCE_CHAIN_MISSING
```

## Example Command

The intended command-line pattern is:

```bash
python validate.py \
  --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json \
  --request examples/aut-cisrc-research-delegation/requests/valid-request.json \
  --revocations examples/aut-cisrc-research-delegation/revocations/no-revocation.json \
  --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json
```

The exact command may change once `validate.py` is implemented.

## Next Development Step

The next step is to create `validate.py`, a minimal command-line validator that can run against the example artefacts in:

```text
examples/aut-cisrc-research-delegation/
```

The validator should be able to return `ALLOW` or `DENY` with a reason code for the initial AUT CISRC test cases.

## Non-Normative Status

This README describes a reference prototype for the AUT CISRC implementation profile.

It does not define SILT Core v0.1.

It does not modify SILT Core v0.1.

Findings from this validator may inform later SILT Core v0.2 consideration.
