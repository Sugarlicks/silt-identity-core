#!/usr/bin/env python3
"""
AUT CISRC Delegation Validator

Non-normative reference prototype for the AUT CISRC implementation profile.

This validator checks whether an access request is valid against:
- a delegation artefact;
- an access request;
- a revocation log or revocation event;
- authority-chain information.

It does not connect to live AUT systems.
It does not replace IAM.
It does not perform KYC.
It does not assess legal validity of source documents.
It does not modify SILT Core v0.1.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


VALIDATOR_VERSION = "aut-cisrc-profile-v0.1"


def load_json(path: str) -> Dict[str, Any]:
    """Load a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def parse_datetime(value: str) -> datetime:
    """Parse an ISO 8601 datetime string."""
    if value.endswith("Z"):
        value = value.replace("Z", "+00:00")
    return datetime.fromisoformat(value).astimezone(timezone.utc)


def result(
    request_id: str,
    delegation_id: str,
    outcome: str,
    reason_code: str,
    reason: str,
    checked_at: Optional[List[Dict[str, Any]]] = None,
    warnings: Optional[List[Dict[str, str]]] = None
) -> Dict[str, Any]:
    """Build a validation result object."""
    return {
        "requestId": request_id,
        "delegationId": delegation_id,
        "result": outcome,
        "reasonCode": reason_code,
        "reason": reason,
        "validatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "validatorVersion": VALIDATOR_VERSION,
        "warnings": warnings or [],
        "checkedAt": checked_at or []
    }


def deny(
    request_id: str,
    delegation_id: str,
    reason_code: str,
    reason: str,
    checked_at: Optional[List[Dict[str, Any]]] = None,
    warnings: Optional[List[Dict[str, str]]] = None
) -> Dict[str, Any]:
    """Return a DENY validation result."""
    return result(
        request_id=request_id,
        delegation_id=delegation_id,
        outcome="DENY",
        reason_code=reason_code,
        reason=reason,
        checked_at=checked_at,
        warnings=warnings
    )


def allow(
    request_id: str,
    delegation_id: str,
    checked_at: Optional[List[Dict[str, Any]]] = None,
    warnings: Optional[List[Dict[str, str]]] = None
) -> Dict[str, Any]:
    """Return an ALLOW validation result."""
    return result(
        request_id=request_id,
        delegation_id=delegation_id,
        outcome="ALLOW",
        reason_code="ALLOW",
        reason="The request is within delegated scope and no revocation applies.",
        checked_at=checked_at,
        warnings=warnings
    )


def add_check(
    checked_at: List[Dict[str, Any]],
    check: str,
    passed: bool,
    reason_code: str,
    detail: str
) -> None:
    """Append a validation check result."""
    checked_at.append({
        "check": check,
        "passed": passed,
        "reasonCode": reason_code,
        "detail": detail
    })


def get_revocations(revocation_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Accept either:
    - {"revocations": [...]}
    - a single revocation event object
    """
    if "revocations" in revocation_data and isinstance(revocation_data["revocations"], list):
        return revocation_data["revocations"]

    if "revocationId" in revocation_data:
        return [revocation_data]

    return []


def actor_matches_delegate(delegation: Dict[str, Any], request: Dict[str, Any]) -> bool:
    """Check whether the request actor matches the named delegate."""
    return (
        delegation.get("delegate", {}).get("actorId")
        == request.get("actor", {}).get("actorId")
    )


def action_is_permitted(delegation: Dict[str, Any], request: Dict[str, Any]) -> bool:
    """Check whether the requested action is included in permittedActions."""
    return request.get("action") in delegation.get("permittedActions", [])


def resource_is_in_scope(delegation: Dict[str, Any], request: Dict[str, Any]) -> bool:
    """Check whether the requested resource matches the delegated resource."""
    return (
        delegation.get("resource", {}).get("resourceId")
        == request.get("resource", {}).get("resourceId")
    )


def purpose_is_in_scope(delegation: Dict[str, Any], request: Dict[str, Any]) -> bool:
    """Check whether the requested purpose matches the delegated purpose."""
    return delegation.get("purpose") == request.get("purpose")


def request_within_time_bounds(delegation: Dict[str, Any], request: Dict[str, Any]) -> Optional[str]:
    """
    Check delegation effective and expiry times.

    Returns:
    - None where valid;
    - DELEGATION_NOT_YET_ACTIVE;
    - DELEGATION_EXPIRED.
    """
    request_time = parse_datetime(request["timestamp"])
    effective_from = parse_datetime(delegation["effectiveFrom"])
    expires_at = parse_datetime(delegation["expiresAt"])

    if request_time < effective_from:
        return "DELEGATION_NOT_YET_ACTIVE"

    if request_time > expires_at:
        return "DELEGATION_EXPIRED"

    return None


def revocation_applies(
    delegation: Dict[str, Any],
    request: Dict[str, Any],
    revocations: List[Dict[str, Any]]
) -> Optional[Dict[str, Any]]:
    """Return the first revocation event that applies before the request timestamp."""
    request_time = parse_datetime(request["timestamp"])
    delegation_id = delegation.get("delegationId")

    for revocation in revocations:
        if revocation.get("delegationId") != delegation_id:
            continue

        revoked_at = parse_datetime(revocation["revokedAt"])

        if revoked_at <= request_time:
            return revocation

    return None


def chain_nodes(authority_chain: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Index the supplied synthetic authority chain by node identifier."""
    return {node.get("authorityNodeId"): node for node in authority_chain.get("authorityNodes", [])}


def is_ancestor(ancestor_id: str, child_id: str, nodes: Dict[str, Dict[str, Any]]) -> bool:
    """Follow explicit parent links; a numeric seniority level alone is insufficient."""
    seen = set()
    current = child_id
    while current and current not in seen:
        if current == ancestor_id:
            return True
        seen.add(current)
        current = nodes.get(current, {}).get("parentNodeId")
    return False


def issuer_has_profile_authority(delegation: Dict[str, Any], authority_chain: Dict[str, Any]) -> bool:
    """Check pilot chain membership, declared domain and issuer-to-delegate path.

    This is structural verification of a synthetic asserted chain, not proof
    of any real institutional appointment, statutory power or legal validity.
    """
    if delegation.get("authorityChain", {}).get("authorityChainId") != authority_chain.get("authorityChainId"):
        return False
    nodes = chain_nodes(authority_chain)
    issuer_id = delegation.get("issuer", {}).get("authorityNodeId")
    delegate_id = delegation.get("delegate", {}).get("authorityNodeId")
    issuer = nodes.get(issuer_id)
    if not issuer or delegate_id not in nodes:
        return False
    domain = authority_chain.get("governanceDomain")
    if domain not in issuer.get("authorityDomain", []):
        return False
    return is_ancestor(issuer_id, delegate_id, nodes)


def revocation_authority_is_valid(
    delegation: Dict[str, Any],
    revocation: Dict[str, Any],
    authority_chain: Dict[str, Any]
) -> bool:
    """Verify revoker's pilot authority node and explicit parent path.

    Committee/subunit authority cannot be inferred from a supplied node ID.
    Such a body must be present in the chain and ancestral to the issuer in
    this narrowly scoped prototype; other mandates need a later explicit
    evidence model and are not accepted by default.
    """
    revoked_by = revocation.get("revokedBy", {})
    issuer = delegation.get("issuer", {})
    if revoked_by.get("actorId") == issuer.get("actorId"):
        return True
    basis = revocation.get("revocationAuthorityBasis", {})
    if basis.get("basisType") not in ("higher_order_authority", "committee_or_subunit"):
        return False
    revoker_id = revoked_by.get("authorityNodeId")
    issuer_id = issuer.get("authorityNodeId")
    nodes = chain_nodes(authority_chain)
    revoker = nodes.get(revoker_id)
    if not revoker or issuer_id not in nodes:
        return False
    if basis.get("authorityNodeId") != revoker_id:
        return False
    if authority_chain.get("governanceDomain") not in revoker.get("authorityDomain", []):
        return False
    return revoker_id != issuer_id and is_ancestor(revoker_id, issuer_id, nodes)


def validate(
    delegation: Dict[str, Any],
    request: Dict[str, Any],
    revocation_data: Dict[str, Any],
    authority_chain: Dict[str, Any],
    strict: bool = False
) -> Dict[str, Any]:
    """Validate an access request against a delegation artefact."""
    checked_at: List[Dict[str, Any]] = []
    warnings: List[Dict[str, str]] = []

    request_id = request.get("requestId", "UNKNOWN_REQUEST")
    delegation_id = delegation.get("delegationId", "UNKNOWN_DELEGATION")

    if not delegation:
        return deny(
            request_id,
            delegation_id,
            "SCHEMA_INVALID",
            "Delegation artefact is missing or empty.",
            checked_at,
            warnings
        )

    add_check(
        checked_at,
        "delegation_present",
        True,
        "ALLOW",
        "Delegation artefact is present."
    )

    if not request:
        return deny(
            request_id,
            delegation_id,
            "SCHEMA_INVALID",
            "Access request is missing or empty.",
            checked_at,
            warnings
        )

    add_check(
        checked_at,
        "request_present",
        True,
        "ALLOW",
        "Access request is present."
    )

    if not authority_chain or not authority_chain.get("authorityNodes"):
        add_check(
            checked_at,
            "authority_chain_present",
            False,
            "AUTHORITY_CHAIN_MISSING",
            "Authority chain is missing."
        )
        return deny(
            request_id,
            delegation_id,
            "AUTHORITY_CHAIN_MISSING",
            "No authority chain is available for validation.",
            checked_at,
            warnings
        )

    add_check(
        checked_at,
        "authority_chain_present",
        True,
        "ALLOW",
        "Authority chain is present."
    )

    if not issuer_has_profile_authority(delegation, authority_chain):
        add_check(checked_at, "issuer_authorised", False, "ISSUER_NOT_AUTHORISED",
                  "Issuer does not have the required asserted chain path and domain.")
        return deny(request_id, delegation_id, "ISSUER_NOT_AUTHORISED",
                    "Issuer authority is not established by this pilot chain.", checked_at, warnings)
    add_check(checked_at, "issuer_authorised", True, "ALLOW",
              "Issuer chain membership, domain and ancestry match the pilot assertion.")

    if strict and not delegation.get("evidenceDocuments"):
        warnings.append({
            "warningCode": "EVIDENCE_CHAIN_MISSING",
            "warning": "Delegation does not include evidence document references."
        })
        return deny(
            request_id,
            delegation_id,
            "EVIDENCE_CHAIN_MISSING",
            "Evidence references are missing in strict mode.",
            checked_at,
            warnings
        )

    if not delegation.get("evidenceDocuments"):
        warnings.append({
            "warningCode": "EVIDENCE_CHAIN_MISSING",
            "warning": "Delegation does not include evidence document references."
        })

    if not actor_matches_delegate(delegation, request):
        add_check(
            checked_at,
            "actor_matches_delegate",
            False,
            "ACTOR_NOT_DELEGATE",
            "Request actor does not match the named delegate."
        )
        return deny(
            request_id,
            delegation_id,
            "ACTOR_NOT_DELEGATE",
            "The request actor does not match the named delegate.",
            checked_at,
            warnings
        )

    add_check(
        checked_at,
        "actor_matches_delegate",
        True,
        "ALLOW",
        "Request actor matches the named delegate."
    )

    if not action_is_permitted(delegation, request):
        add_check(
            checked_at,
            "action_permitted",
            False,
            "ACTION_NOT_PERMITTED",
            "Requested action is not included in permittedActions."
        )
        return deny(
            request_id,
            delegation_id,
            "ACTION_NOT_PERMITTED",
            "The requested action is not permitted by the delegation.",
            checked_at,
            warnings
        )

    add_check(
        checked_at,
        "action_permitted",
        True,
        "ALLOW",
        "Requested action is included in permittedActions."
    )

    if not resource_is_in_scope(delegation, request):
        add_check(
            checked_at,
            "resource_in_scope",
            False,
            "RESOURCE_OUT_OF_SCOPE",
            "Requested resource does not match delegated resource."
        )
        return deny(
            request_id,
            delegation_id,
            "RESOURCE_OUT_OF_SCOPE",
            "The requested resource is outside the delegated scope.",
            checked_at,
            warnings
        )

    add_check(
        checked_at,
        "resource_in_scope",
        True,
        "ALLOW",
        "Requested resource matches delegated resource."
    )

    if not purpose_is_in_scope(delegation, request):
        add_check(
            checked_at,
            "purpose_in_scope",
            False,
            "PURPOSE_OUT_OF_SCOPE",
            "Requested purpose does not match delegated purpose."
        )
        return deny(
            request_id,
            delegation_id,
            "PURPOSE_OUT_OF_SCOPE",
            "The requested purpose is outside the delegated scope.",
            checked_at,
            warnings
        )

    add_check(
        checked_at,
        "purpose_in_scope",
        True,
        "ALLOW",
        "Requested purpose matches delegated purpose."
    )

    time_error = request_within_time_bounds(delegation, request)

    if time_error == "DELEGATION_NOT_YET_ACTIVE":
        add_check(
            checked_at,
            "within_time_bounds",
            False,
            "DELEGATION_NOT_YET_ACTIVE",
            "Request timestamp is before the delegation effective date."
        )
        return deny(
            request_id,
            delegation_id,
            "DELEGATION_NOT_YET_ACTIVE",
            "The request occurs before the delegation effective date.",
            checked_at,
            warnings
        )

    if time_error == "DELEGATION_EXPIRED":
        add_check(
            checked_at,
            "within_time_bounds",
            False,
            "DELEGATION_EXPIRED",
            "Request timestamp is after the delegation expiry date."
        )
        return deny(
            request_id,
            delegation_id,
            "DELEGATION_EXPIRED",
            "The requested action occurred after the delegation expiry date.",
            checked_at,
            warnings
        )

    add_check(
        checked_at,
        "within_time_bounds",
        True,
        "ALLOW",
        "Request timestamp falls within delegation effective period."
    )

    revocations = get_revocations(revocation_data)
    applicable_revocation = revocation_applies(delegation, request, revocations)

    if applicable_revocation:
        if not revocation_authority_is_valid(delegation, applicable_revocation, authority_chain):
            add_check(
                checked_at,
                "revocation_authority_valid",
                False,
                "REVOCATION_AUTHORITY_INVALID",
                "Revocation actor does not have recognised revocation authority."
            )
            return deny(
                request_id,
                delegation_id,
                "REVOCATION_AUTHORITY_INVALID",
                "The revocation event was issued by an actor without recognised revocation authority.",
                checked_at,
                warnings
            )

        add_check(
            checked_at,
            "not_revoked",
            False,
            "DELEGATION_REVOKED",
            "A valid revocation event applies before the request timestamp."
        )
        return deny(
            request_id,
            delegation_id,
            "DELEGATION_REVOKED",
            "The delegation has been revoked before the request timestamp.",
            checked_at,
            warnings
        )

    add_check(
        checked_at,
        "not_revoked",
        True,
        "ALLOW",
        "No revocation event applies."
    )

    return allow(request_id, delegation_id, checked_at, warnings)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate an AUT CISRC delegation artefact against an access request."
    )
    parser.add_argument("--delegation", required=True, help="Path to delegation JSON file.")
    parser.add_argument("--request", required=True, help="Path to access request JSON file.")
    parser.add_argument("--revocations", required=True, help="Path to revocation log or revocation event JSON file.")
    parser.add_argument("--authority-chain", required=True, help="Path to authority chain JSON file.")
    parser.add_argument("--strict", action="store_true", help="Enable strict evidence-chain checks.")

    args = parser.parse_args()

    delegation = load_json(args.delegation)
    request = load_json(args.request)
    revocations = load_json(args.revocations)
    authority_chain = load_json(args.authority_chain)

    validation_result = validate(
        delegation=delegation,
        request=request,
        revocation_data=revocations,
        authority_chain=authority_chain,
        strict=args.strict
    )

    print(json.dumps(validation_result, indent=2))


if __name__ == "__main__":
    main()
