# AUT CISRC Research Delegation Test Results

**Status:** Initial manual/prototype test record
**Profile:** AUT CISRC Implementation Profile
**Validator:** `reference/validators/aut-cisrc-delegation/validate.py`
**Relationship to SILT Core:** Non-normative implementation example

## Purpose

This document records initial validation results for the AUT CISRC research delegation example.

The purpose is to show that the AUT CISRC implementation profile can express a delegated authority claim, evaluate an access request, and return a deterministic validation result.

## Current Test Coverage

| Test | Delegation                          | Request                       | Revocation Log                    | Expected Result | Status                         |
| ---- | ----------------------------------- | ----------------------------- | --------------------------------- | --------------- | ------------------------------ |
| 01   | `delegations/valid-delegation.json` | `requests/valid-request.json` | `revocations/no-revocations.json` | `ALLOW`         | Ready for prototype validation |

## Test 01: Valid Delegation

### Input Artefacts

```text
authority-chain.json
delegations/valid-delegation.json
requests/valid-request.json
revocations/no-revocations.json
```

### Expected Result

```text
ALLOW
```

### Expected Reason Code

```text
ALLOW
```

### Expected Explanation

The request should be allowed because:

* the delegation artefact is present;
* the authority chain is present;
* the request actor matches the named delegate;
* the requested action is included in permitted actions;
* the requested resource matches the delegated resource;
* the requested purpose matches the delegated purpose;
* the request timestamp falls within the delegation period;
* no revocation event applies.

## Prototype Command

The intended prototype command is:

```bash
python reference/validators/aut-cisrc-delegation/validate.py \
  --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json \
  --request examples/aut-cisrc-research-delegation/requests/valid-request.json \
  --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json \
  --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json
```

## Expected Prototype Output

```json
{
  "result": "ALLOW",
  "reasonCode": "ALLOW",
  "reason": "The request is within delegated scope and no revocation applies."
}
```

## Notes

This is an initial test-results record.

Additional denial-path test results should be added for:

* expired delegation;
* revoked delegation;
* wrong delegate;
* action outside permitted scope;
* resource mismatch;
* purpose mismatch;
* missing authority chain;
* invalid revoker.

This document does not modify SILT Core v0.1.
