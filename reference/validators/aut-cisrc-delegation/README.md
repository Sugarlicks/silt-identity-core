# AUT CISRC Delegation Validator

**Status:** Draft prototype  
**Profile:** AUT CISRC Implementation Profile  
**Relationship to SILT Core:** Non-normative reference prototype

## Purpose

This folder contains the lightweight reference validator for the AUT CISRC implementation profile.

The validator checks whether an access request is valid against:

- a delegation artefact;
- an access request;
- a revocation event or revocation log;
- authority-chain information.

The validator is a prototype only.

It does not connect to live AUT systems.  
It does not replace IAM.  
It does not perform KYC.  
It does not assess legal validity of source documents.  
It does not modify SILT Core v0.1.

## Validator File

```text
reference/validators/aut-cisrc-delegation/validate.py
```

## Example Artefacts

The validator is intended to run against the AUT CISRC example artefacts in:

```text
examples/aut-cisrc-research-delegation/
```

Current example inputs include:

```text
examples/aut-cisrc-research-delegation/authority-chain.json
examples/aut-cisrc-research-delegation/delegations/valid-delegation.json
examples/aut-cisrc-research-delegation/delegations/expired-delegation.json
examples/aut-cisrc-research-delegation/requests/valid-request.json
examples/aut-cisrc-research-delegation/requests/wrong-delegate-request.json
examples/aut-cisrc-research-delegation/requests/action-not-permitted-request.json
examples/aut-cisrc-research-delegation/requests/resource-mismatch-request.json
examples/aut-cisrc-research-delegation/requests/purpose-mismatch-request.json
examples/aut-cisrc-research-delegation/revocations/no-revocations.json
examples/aut-cisrc-research-delegation/revocations/revoked-delegation.json
```

Expected results are recorded in:

```text
examples/aut-cisrc-research-delegation/expected-results/
```

A human-readable test record is available at:

```text
examples/aut-cisrc-research-delegation/test-results.md
```

## Intended Output

The validator returns a deterministic validation result.

Example allow result:

```json
{
  "result": "ALLOW",
  "reasonCode": "ALLOW",
  "reason": "The request is within delegated scope and no revocation applies."
}
```

Example deny result:

```json
{
  "result": "DENY",
  "reasonCode": "DELEGATION_EXPIRED",
  "reason": "The requested action occurred after the delegation expiry date."
}
```

## Initial Validation Checks

The validator checks:

1. Required artefacts are present.
2. Delegation object is present.
3. Access request object is present.
4. Authority chain is present.
5. Request actor matches the delegate.
6. Requested action is permitted.
7. Requested resource is within scope.
8. Requested purpose is within scope.
9. Request timestamp is within the effective period.
10. Delegation has not expired.
11. Delegation has not been revoked.
12. If revoked, the revoking authority is valid.

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

## Current Test Coverage

The current AUT CISRC example set covers:

| Test | Expected Result | Reason Code |
|---|---|---|
| Valid delegation | `ALLOW` | `ALLOW` |
| Expired delegation | `DENY` | `DELEGATION_EXPIRED` |
| Wrong delegate | `DENY` | `ACTOR_NOT_DELEGATE` |
| Action outside permitted scope | `DENY` | `ACTION_NOT_PERMITTED` |
| Revoked delegation | `DENY` | `DELEGATION_REVOKED` |
| Resource mismatch | `DENY` | `RESOURCE_OUT_OF_SCOPE` |
| Purpose mismatch | `DENY` | `PURPOSE_OUT_OF_SCOPE` |

## Example Commands

Run these commands from the repository root.

### Valid Delegation

```bash
python reference/validators/aut-cisrc-delegation/validate.py \
  --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json \
  --request examples/aut-cisrc-research-delegation/requests/valid-request.json \
  --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json \
  --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json
```

### Expired Delegation

```bash
python reference/validators/aut-cisrc-delegation/validate.py \
  --delegation examples/aut-cisrc-research-delegation/delegations/expired-delegation.json \
  --request examples/aut-cisrc-research-delegation/requests/valid-request.json \
  --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json \
  --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json
```

### Wrong Delegate

```bash
python reference/validators/aut-cisrc-delegation/validate.py \
  --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json \
  --request examples/aut-cisrc-research-delegation/requests/wrong-delegate-request.json \
  --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json \
  --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json
```

### Action Outside Permitted Scope

```bash
python reference/validators/aut-cisrc-delegation/validate.py \
  --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json \
  --request examples/aut-cisrc-research-delegation/requests/action-not-permitted-request.json \
  --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json \
  --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json
```

### Revoked Delegation

```bash
python reference/validators/aut-cisrc-delegation/validate.py \
  --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json \
  --request examples/aut-cisrc-research-delegation/requests/valid-request.json \
  --revocations examples/aut-cisrc-research-delegation/revocations/revoked-delegation.json \
  --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json
```

### Resource Mismatch

```bash
python reference/validators/aut-cisrc-delegation/validate.py \
  --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json \
  --request examples/aut-cisrc-research-delegation/requests/resource-mismatch-request.json \
  --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json \
  --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json
```

### Purpose Mismatch

```bash
python reference/validators/aut-cisrc-delegation/validate.py \
  --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json \
  --request examples/aut-cisrc-research-delegation/requests/purpose-mismatch-request.json \
  --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json \
  --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json
```

## Revocation Logic

For this implementation profile, a revocation event is valid where the revoking actor is:

- the original delegator;
- a higher-order authority in the relevant authority chain;
- an authorised committee, agency, or subunit with delegated authority over the relevant governance domain.

The validator denies future requests where a valid revocation event applies before the request timestamp.

For Phase 2, revocation affects future validation requests only. Pending-action treatment is out of scope.

## Evidence Handling

Authority resolves to an evidential chain based on documents.

For this lightweight prototype, evidence documents are treated as referenced metadata.

The validator may return a warning where evidence references are missing, but evidence verification is not required.

In strict mode, missing evidence may return:

```text
EVIDENCE_CHAIN_MISSING
```

## Non-Normative Status

This validator is a reference prototype for the AUT CISRC implementation profile.

It does not define SILT Core v0.1.

It does not modify SILT Core v0.1.

Findings from this validator may inform later SILT Core v0.2 consideration.
