# AUT CISRC Research Delegation Test Results

**Status:** Initial manual/prototype test record  
**Profile:** AUT CISRC Implementation Profile  
**Validator:** `reference/validators/aut-cisrc-delegation/validate.py`  
**Relationship to SILT Core:** Non-normative implementation example

## Purpose

This document records initial validation results for the AUT CISRC research delegation example.

The purpose is to show that the AUT CISRC implementation profile can express a delegated authority claim, evaluate access requests, and return deterministic validation results.

## Current Test Coverage

| Test | Delegation | Request | Revocation Log | Expected Result | Reason Code | Status |
|---|---|---|---|---|---|---|
| 01 | `delegations/valid-delegation.json` | `requests/valid-request.json` | `revocations/no-revocations.json` | `ALLOW` | `ALLOW` | Ready for prototype validation |
| 02 | `delegations/expired-delegation.json` | `requests/valid-request.json` | `revocations/no-revocations.json` | `DENY` | `DELEGATION_EXPIRED` | Ready for prototype validation |
| 03 | `delegations/valid-delegation.json` | `requests/wrong-delegate-request.json` | `revocations/no-revocations.json` | `DENY` | `ACTOR_NOT_DELEGATE` | Ready for prototype validation |
| 04 | `delegations/valid-delegation.json` | `requests/action-not-permitted-request.json` | `revocations/no-revocations.json` | `DENY` | `ACTION_NOT_PERMITTED` | Ready for prototype validation |
| 05 | `delegations/valid-delegation.json` | `requests/valid-request.json` | `revocations/revoked-delegation.json` | `DENY` | `DELEGATION_REVOKED` | Ready for prototype validation |
| 06 | `delegations/valid-delegation.json` | `requests/resource-mismatch-request.json` | `revocations/no-revocations.json` | `DENY` | `RESOURCE_OUT_OF_SCOPE` | Ready for prototype validation |
| 07 | `delegations/valid-delegation.json` | `requests/purpose-mismatch-request.json` | `revocations/no-revocations.json` | `DENY` | `PURPOSE_OUT_OF_SCOPE` | Ready for prototype validation |

## Test 01: Valid Delegation

### Input Artefacts

    authority-chain.json
    delegations/valid-delegation.json
    requests/valid-request.json
    revocations/no-revocations.json

### Expected Result

    ALLOW

### Expected Reason Code

    ALLOW

### Expected Explanation

The request should be allowed because:

- the delegation artefact is present;
- the authority chain is present;
- the request actor matches the named delegate;
- the requested action is included in permitted actions;
- the requested resource matches the delegated resource;
- the requested purpose matches the delegated purpose;
- the request timestamp falls within the delegation period;
- no revocation event applies.

## Test 02: Expired Delegation

### Input Artefacts

    authority-chain.json
    delegations/expired-delegation.json
    requests/valid-request.json
    revocations/no-revocations.json

### Expected Result

    DENY

### Expected Reason Code

    DELEGATION_EXPIRED

### Expected Explanation

The request should be denied because the request timestamp occurs after the delegation expiry date.

## Test 03: Wrong Delegate

### Input Artefacts

    authority-chain.json
    delegations/valid-delegation.json
    requests/wrong-delegate-request.json
    revocations/no-revocations.json

### Expected Result

    DENY

### Expected Reason Code

    ACTOR_NOT_DELEGATE

### Expected Explanation

The request should be denied because the request actor does not match the named delegate in the delegation artefact.

## Test 04: Action Outside Permitted Scope

### Input Artefacts

    authority-chain.json
    delegations/valid-delegation.json
    requests/action-not-permitted-request.json
    revocations/no-revocations.json

### Expected Result

    DENY

### Expected Reason Code

    ACTION_NOT_PERMITTED

### Expected Explanation

The request should be denied because the requested action is not included in the delegation's permitted actions.

## Test 05: Revoked Delegation

### Input Artefacts

    authority-chain.json
    delegations/valid-delegation.json
    requests/valid-request.json
    revocations/revoked-delegation.json

### Expected Result

    DENY

### Expected Reason Code

    DELEGATION_REVOKED

### Expected Explanation

The request should be denied because a valid revocation event applies before the request timestamp.

## Test 06: Resource Mismatch

### Input Artefacts

    authority-chain.json
    delegations/valid-delegation.json
    requests/resource-mismatch-request.json
    revocations/no-revocations.json

### Expected Result

    DENY

### Expected Reason Code

    RESOURCE_OUT_OF_SCOPE

### Expected Explanation

The request should be denied because the requested resource does not match the resource identified in the delegation artefact.

## Test 07: Purpose Mismatch

### Input Artefacts

    authority-chain.json
    delegations/valid-delegation.json
    requests/purpose-mismatch-request.json
    revocations/no-revocations.json

### Expected Result

    DENY

### Expected Reason Code

    PURPOSE_OUT_OF_SCOPE

### Expected Explanation

The request should be denied because the requested purpose does not match the purpose stated in the delegation artefact.

## Prototype Commands

Run these commands from the repository root.

### Test 01

    python reference/validators/aut-cisrc-delegation/validate.py --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json --request examples/aut-cisrc-research-delegation/requests/valid-request.json --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json

### Test 02

    python reference/validators/aut-cisrc-delegation/validate.py --delegation examples/aut-cisrc-research-delegation/delegations/expired-delegation.json --request examples/aut-cisrc-research-delegation/requests/valid-request.json --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json

### Test 03

    python reference/validators/aut-cisrc-delegation/validate.py --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json --request examples/aut-cisrc-research-delegation/requests/wrong-delegate-request.json --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json

### Test 04

    python reference/validators/aut-cisrc-delegation/validate.py --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json --request examples/aut-cisrc-research-delegation/requests/action-not-permitted-request.json --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json

### Test 05

    python reference/validators/aut-cisrc-delegation/validate.py --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json --request examples/aut-cisrc-research-delegation/requests/valid-request.json --revocations examples/aut-cisrc-research-delegation/revocations/revoked-delegation.json --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json

### Test 06

    python reference/validators/aut-cisrc-delegation/validate.py --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json --request examples/aut-cisrc-research-delegation/requests/resource-mismatch-request.json --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json

### Test 07

    python reference/validators/aut-cisrc-delegation/validate.py --delegation examples/aut-cisrc-research-delegation/delegations/valid-delegation.json --request examples/aut-cisrc-research-delegation/requests/purpose-mismatch-request.json --revocations examples/aut-cisrc-research-delegation/revocations/no-revocations.json --authority-chain examples/aut-cisrc-research-delegation/authority-chain.json

## Notes

This is an initial test-results record for the AUT CISRC implementation profile.

The current test set covers:

- one successful delegated-authority validation;
- expired delegation;
- wrong delegate;
- action outside permitted scope;
- revoked delegation;
- resource mismatch;
- purpose mismatch.

Additional future tests may cover:

- missing authority chain;
- invalid revoker;
- not-yet-active delegation;
- strict evidence-chain mode.

This document does not modify SILT Core v0.1.
