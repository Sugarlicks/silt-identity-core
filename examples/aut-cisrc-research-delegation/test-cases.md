# AUT CISRC Research Delegation Test Cases

**Status:** Draft
**Profile:** AUT CISRC Implementation Profile
**Relationship to SILT Core:** Non-normative implementation example

## Purpose

This document defines the initial test cases for the AUT CISRC research delegation example.

The test cases are designed to show whether a delegated authority claim can be expressed, checked, expired, and revoked through portable JSON artefacts.

## Test Case Summary

| Test | Scenario                                  | Expected Result                                          |
| ---- | ----------------------------------------- | -------------------------------------------------------- |
| 01   | Valid delegation                          | ALLOW                                                    |
| 02   | Expired delegation                        | DENY: `DELEGATION_EXPIRED`                               |
| 03   | Revoked delegation                        | DENY: `DELEGATION_REVOKED`                               |
| 04   | Wrong delegate                            | DENY: `ACTOR_NOT_DELEGATE`                               |
| 05   | Action outside permitted scope            | DENY: `ACTION_NOT_PERMITTED`                             |
| 06   | Resource mismatch                         | DENY: `RESOURCE_OUT_OF_SCOPE`                            |
| 07   | Purpose mismatch                          | DENY: `PURPOSE_OUT_OF_SCOPE`                             |
| 08   | Missing authority chain                   | DENY: `AUTHORITY_CHAIN_MISSING`                          |
| 09   | Invalid revoker                           | DENY: `REVOCATION_AUTHORITY_INVALID`                     |
| 10   | Higher authority revokes lower delegation | DENY: `DELEGATION_REVOKED`                               |
| 11   | Missing evidence chain                    | WARNING or DENY in strict mode: `EVIDENCE_CHAIN_MISSING` |

## 01 Valid Delegation

A project supervisor delegates authority to a research assistant to submit `Dataset123` for `ProjectX`.

The request actor, action, resource, purpose, and timestamp all match the delegation.

Expected result:

```text
ALLOW
```

## 02 Expired Delegation

The research assistant submits a request after the delegation expiry date.

Expected result:

```text
DENY: DELEGATION_EXPIRED
```

## 03 Revoked Delegation

The delegation has been revoked before the request timestamp.

Expected result:

```text
DENY: DELEGATION_REVOKED
```

## 04 Wrong Delegate

The request is made by an actor who is not the named delegate.

Expected result:

```text
DENY: ACTOR_NOT_DELEGATE
```

## 05 Action Outside Permitted Scope

The delegation permits `dataset.submit`, but the request attempts a different action such as `dataset.delete` or `repository.update`.

Expected result:

```text
DENY: ACTION_NOT_PERMITTED
```

## 06 Resource Mismatch

The delegation applies to `Dataset123`, but the request concerns a different resource.

Expected result:

```text
DENY: RESOURCE_OUT_OF_SCOPE
```

## 07 Purpose Mismatch

The delegation is limited to `ProjectX research submission`, but the request is made for a different purpose.

Expected result:

```text
DENY: PURPOSE_OUT_OF_SCOPE
```

## 08 Missing Authority Chain

The delegation does not include or reference an authority chain.

Expected result:

```text
DENY: AUTHORITY_CHAIN_MISSING
```

## 09 Invalid Revoker

The delegation is revoked by an actor who is neither the original delegator, a higher-order authority, nor an authorised committee, agency, or subunit.

Expected result:

```text
DENY: REVOCATION_AUTHORITY_INVALID
```

## 10 Higher Authority Revokes Lower Delegation

A higher-order authority in the relevant authority chain revokes a delegation issued at a lower level.

Future requests relying on that delegation are denied.

Expected result:

```text
DENY: DELEGATION_REVOKED
```

## 11 Missing Evidence Chain

The delegation or authority chain does not include supporting evidence references.

In non-strict mode, this may produce a warning.

In strict mode, this may produce:

```text
EVIDENCE_CHAIN_MISSING
```

## Notes

These test cases are deliberately narrow.

They do not model production AUT systems, appeals, behavioural monitoring, IAM replacement, or legal verification of source documents.

They test only whether a request is valid under a delegated authority artefact at the time of validation.
