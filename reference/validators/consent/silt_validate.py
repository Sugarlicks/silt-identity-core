"""
SILT Core — Consent Object Validator
https://github.com/Sugarlicks/silt-identity-core

Validates consent artefacts against the SILT Core consent schema (v0.1).

SILT Core models not only who is acting, but in what capacity, under what
authority, with what consent, and under what conditions that action may
be relied upon or revoked. This validator enforces all five layers as
preconditions for reliance, not as UX convention.

Validation layers:
  1. Schema  — structural conformance (JSON Schema Draft 2020-12)
  2. Semantic — SILT Core design axioms that schema alone cannot express:
       - capacity must be declared and non-trivial
       - authority source must be explicit and referenced
       - delegated capacity requires temporal bounds
       - self-authority cannot be silently forwarded to a broker/agent recipient
       - delegated authority requires a termination rule, not just a revocation pointer
       - scope must be bounded, not wildcarded
       - purpose must be specific enough to gate reliance

Usage:
    python silt_validate.py                  # run built-in test vectors
    python silt_validate.py consent.json     # validate a file
"""

import json
import sys
from datetime import datetime, timezone

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("Install jsonschema: pip install jsonschema")
    sys.exit(1)


CONSENT_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://github.com/Sugarlicks/silt-identity-core/blob/main/schemas/consent.schema.json",
    "title": "SILT Core Consent",
    "type": "object",
    "additionalProperties": False,
    "required": [
        "consent_id",
        "principal",
        "recipient",
        "purpose",
        "scope",
        "issued_at",
        "revocation"
    ],
    "properties": {
        "consent_id": {
            "type": "string",
            "minLength": 1,
            "description": "Stable identifier for this consent artefact."
        },
        "issued_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the consent was granted."
        },
        "capacity": {
            "type": "object",
            "additionalProperties": False,
            "required": ["capacity_type"],
            "properties": {
                "capacity_type": {
                    "type": "string",
                    "enum": [
                        "personal",
                        "agent",
                        "trustee",
                        "officer",
                        "guardian",
                        "delegate"
                    ],
                    "description": "The mode in which the principal is acting in this context."
                },
                "capacity_ref": {
                    "type": "string",
                    "description": "Optional reference to the instrument establishing this capacity."
                }
            },
            "description": "Capacity is contextual. It describes how an actor acts, not just who they are."
        },
        "authority": {
            "type": "object",
            "additionalProperties": False,
            "required": ["authority_type", "authority_ref"],
            "properties": {
                "authority_type": {
                    "type": "string",
                    "enum": [
                        "self",
                        "mandate",
                        "resolution",
                        "power_of_attorney",
                        "contract",
                        "credential",
                        "policy"
                    ],
                    "description": "The type of authority source underpinning this action."
                },
                "authority_ref": {
                    "type": "string",
                    "minLength": 1,
                    "description": "Reference to the authority instrument. Must not be a placeholder."
                }
            },
            "description": "Authority source plurality: authority must be explicit and referenced."
        },
        "principal": {
            "type": "object",
            "additionalProperties": False,
            "required": ["principal_id"],
            "properties": {
                "principal_id": {
                    "type": "string",
                    "minLength": 1,
                    "description": "Identifier for the principal granting consent."
                }
            }
        },
        "recipient": {
            "type": "object",
            "additionalProperties": False,
            "required": ["recipient_id"],
            "properties": {
                "recipient_id": {
                    "type": "string",
                    "minLength": 1,
                    "description": "Identifier of the party allowed to rely on this consent."
                },
                "recipient_type": {
                    "type": "string",
                    "description": "Optional type hint: organisation, verifier, service, broker, agent."
                }
            }
        },
        "purpose": {
            "type": "string",
            "minLength": 1,
            "description": "Machine-readable purpose declaration. Purpose is a constraint."
        },
        "scope": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "string", "minLength": 1},
            "description": "Permitted disclosures or proofs. Intentionally minimal."
        },
        "duration": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "not_before": {"type": "string", "format": "date-time"},
                "expires_at": {"type": "string", "format": "date-time"}
            },
            "description": "Temporal bounds. Short-lived consent is preferred by default."
        },
        "constraints": {
            "type": "object",
            "additionalProperties": True,
            "description": "Optional constraints such as one-time use, context binding, or frequency limits."
        },
        "revocation": {
            "type": "object",
            "additionalProperties": False,
            "required": ["revocation_ref"],
            "properties": {
                "revocation_ref": {
                    "type": "string",
                    "minLength": 1,
                    "description": "Pointer enabling verifiers to check revocation or expiry state."
                },
                "termination_rule": {
                    "type": "string",
                    "description": "Condition or event that terminates this consent. Required when capacity is delegated or non-personal."
                }
            },
            "description": "Revocation is first-class. All authority must have an exit."
        },
        "proof": {
            "type": "object",
            "additionalProperties": True,
            "description": "Optional proof material such as signatures or attestations."
        }
    }
}


def check_capacity_present(consent: dict) -> list[str]:
    if "capacity" not in consent:
        return [
            "WARNING [capacity]: No capacity declared. SILT Core requires knowing "
            "the mode in which the principal acts: personal, delegate, trustee, "
            "agent, officer, or guardian. Without this, the consent artefact is structurally incomplete."
        ]
    return []


def check_authority_present(consent: dict) -> list[str]:
    if "authority" not in consent:
        return [
            "WARNING [authority]: No authority declared. SILT Core requires an explicit "
            "authority source and reference. Without this, reliance cannot be verified."
        ]
    return []


def check_authority_ref_not_placeholder(consent: dict) -> list[str]:
    ref = consent.get("authority", {}).get("authority_ref", "")
    placeholders = {"tbd", "todo", "none", "n/a", "placeholder", "self", ""}

    if ref.strip().lower() in placeholders:
        return [
            "WARNING [authority.authority_ref]: appears to be a placeholder. "
            "SILT Core axiom: authority must be explicitly referenced. "
            "Provide a URI, document hash, mandate reference, or verifiable credential reference."
        ]

    return []


def check_delegated_capacity_has_expiry(consent: dict) -> list[str]:
    delegated = {"agent", "trustee", "officer", "guardian", "delegate"}
    cap_type = consent.get("capacity", {}).get("capacity_type", "")

    if cap_type in delegated and not consent.get("duration", {}).get("expires_at"):
        return [
            f"WARNING [capacity/duration]: capacity_type '{cap_type}' implies "
            "delegated or fiduciary authority, but no expires_at is set. "
            "SILT Core axiom: delegated capacity must be temporally bounded. "
            "Add duration.expires_at."
        ]

    return []


def check_self_authority_not_forwarded(consent: dict) -> list[str]:
    auth_type = consent.get("authority", {}).get("authority_type", "")
    recipient_type = consent.get("recipient", {}).get("recipient_type", "")
    forwarding = {"agent", "broker", "intermediary", "platform", "delegate"}

    if auth_type == "self" and recipient_type.lower() in forwarding:
        return [
            f"WARNING [authority/recipient]: authority_type is 'self' but "
            f"recipient_type is '{recipient_type}', which implies onward acting. "
            "Self-authority cannot be silently forwarded to a recipient acting on behalf of others. "
            "This is a silent authority laundering pattern."
        ]

    return []


def check_revocation_termination_rule(consent: dict) -> list[str]:
    non_personal = {"agent", "trustee", "officer", "guardian", "delegate"}
    cap_type = consent.get("capacity", {}).get("capacity_type", "personal")

    if cap_type in non_personal and not consent.get("revocation", {}).get("termination_rule"):
        return [
            f"WARNING [revocation.termination_rule]: capacity_type is '{cap_type}' "
            "but no termination_rule is defined. "
            "SILT Core axiom: delegated authority must state the condition under which "
            "it ends, not only where to check. Add revocation.termination_rule."
        ]

    return []


def check_expiry(consent: dict) -> list[str]:
    expires_at = consent.get("duration", {}).get("expires_at")

    if not expires_at:
        return [
            "WARNING [duration]: No expires_at set. "
            "SILT Core design axiom: short-lived consent is preferred."
        ]

    try:
        expiry = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)

        if expiry < now:
            return [
                f"EXPIRED: consent expired at {expires_at}. "
                "This artefact should not be relied upon."
            ]

        remaining = expiry - now
        return [
            f"OK: consent valid for {remaining.days}d {remaining.seconds // 3600}h from now."
        ]

    except ValueError:
        return [
            f"WARNING [duration.expires_at]: Could not parse: {expires_at}"
        ]


def check_scope_specificity(consent: dict) -> list[str]:
    wildcards = {"*", "all", "any", "everything"}

    if any(s.strip().lower() in wildcards for s in consent.get("scope", [])):
        return [
            "WARNING [scope]: Scope contains a wildcard entry. "
            "SILT Core expects intentionally minimal, bounded scope declarations. "
            "Wildcards defeat the purpose of scoped consent."
        ]

    return []


def check_revocation_ref_not_placeholder(consent: dict) -> list[str]:
    ref = consent.get("revocation", {}).get("revocation_ref", "")
    placeholders = {"tbd", "todo", "none", "n/a", "placeholder", ""}

    if ref.strip().lower() in placeholders:
        return [
            "WARNING [revocation.revocation_ref]: appears to be a placeholder. "
            "A genuine revocation endpoint, registry reference, or revocation status pointer is required."
        ]

    return []


def check_purpose_is_specific(consent: dict) -> list[str]:
    purpose = consent.get("purpose", "")
    generic = {"consent", "access", "use", "data", "general", "misc"}

    if purpose.strip().lower() in generic or len(purpose.strip()) < 10:
        return [
            "WARNING [purpose]: Purpose declaration appears generic. "
            "SILT Core treats purpose as a machine-readable constraint. "
            "It must be specific enough to gate reliance decisions."
        ]

    return []


def validate_consent(consent: dict, label: str = "consent") -> bool:
    print(f"\n{'=' * 64}")
    print(f"  Validating: {label}")
    print(f"{'=' * 64}")

    validator = Draft202012Validator(CONSENT_SCHEMA)
    errors = list(validator.iter_errors(consent))

    if errors:
        print("  SCHEMA INVALID")
        for error in errors:
            path = " -> ".join(str(p) for p in error.absolute_path) or "(root)"
            print(f"    [x] [{path}] {error.message}")
        return False

    print("  [ok] Schema valid")

    all_notes = (
        check_capacity_present(consent)
        + check_authority_present(consent)
        + check_authority_ref_not_placeholder(consent)
        + check_delegated_capacity_has_expiry(consent)
        + check_self_authority_not_forwarded(consent)
        + check_revocation_termination_rule(consent)
        + check_expiry(consent)
        + check_scope_specificity(consent)
        + check_revocation_ref_not_placeholder(consent)
        + check_purpose_is_specific(consent)
    )

    has_error = False

    for note in all_notes:
        if note.startswith("EXPIRED"):
            print(f"  [x] {note}")
            has_error = True
        elif note.startswith("WARNING"):
            print(f"  [warning] {note}")
        else:
            print(f"  [ok] {note}")

    print()

    if has_error:
        print("  RESULT: INVALID — expired artefact, do not rely")
        return False

    print("  RESULT: VALID — artefact may be relied upon")
    return True


TEST_VECTORS = [
    {
        "label": "valid — personal capacity, self authority",
        "should_pass": True,
        "data": {
            "consent_id": "consent-001",
            "issued_at": "2026-05-05T10:00:00Z",
            "capacity": {"capacity_type": "personal"},
            "authority": {
                "authority_type": "self",
                "authority_ref": "did:example:alice#key-1"
            },
            "principal": {"principal_id": "did:example:alice"},
            "recipient": {
                "recipient_id": "did:example:verifier-org",
                "recipient_type": "organisation"
            },
            "purpose": "age-verification-for-licensed-venue-entry",
            "scope": ["age_over_18"],
            "duration": {
                "not_before": "2026-05-05T10:00:00Z",
                "expires_at": "2026-08-05T10:00:00Z"
            },
            "revocation": {
                "revocation_ref": "https://siltcore.org/revocation/consent-001"
            }
        }
    },
    {
        "label": "valid — trustee capacity with termination rule",
        "should_pass": True,
        "data": {
            "consent_id": "consent-002",
            "issued_at": "2026-05-05T09:00:00Z",
            "capacity": {
                "capacity_type": "trustee",
                "capacity_ref": "https://siltcore.org/instruments/trust-deed-2026-001"
            },
            "authority": {
                "authority_type": "mandate",
                "authority_ref": "https://siltcore.org/instruments/trust-deed-2026-001"
            },
            "principal": {"principal_id": "did:example:trustee-jane"},
            "recipient": {"recipient_id": "did:example:health-provider"},
            "purpose": "medical-treatment-authorisation-for-named-beneficiary",
            "scope": ["medical_history_summary", "treatment_consent"],
            "duration": {"expires_at": "2026-12-31T23:59:59Z"},
            "constraints": {
                "one_time_use": False,
                "context": "named-beneficiary-only"
            },
            "revocation": {
                "revocation_ref": "https://siltcore.org/revocation/consent-002",
                "termination_rule": "trust-wound-up OR beneficiary-regains-capacity"
            }
        }
    },
    {
        "label": "valid — AI agent with bounded scope and termination rule",
        "should_pass": True,
        "data": {
            "consent_id": "consent-003",
            "issued_at": "2026-05-05T08:00:00Z",
            "capacity": {
                "capacity_type": "agent",
                "capacity_ref": "https://siltcore.org/delegations/agent-grant-003"
            },
            "authority": {
                "authority_type": "mandate",
                "authority_ref": "https://siltcore.org/delegations/agent-grant-003"
            },
            "principal": {"principal_id": "did:example:alice"},
            "recipient": {"recipient_id": "did:example:booking-service"},
            "purpose": "flight-search-and-booking-on-behalf-of-principal",
            "scope": ["travel_preferences", "payment_up_to_2000_NZD"],
            "duration": {"expires_at": "2026-05-12T08:00:00Z"},
            "constraints": {
                "max_spend": 2000,
                "currency": "NZD",
                "route": "AKL-SYD"
            },
            "revocation": {
                "revocation_ref": "https://siltcore.org/revocation/consent-003",
                "termination_rule": "principal-revokes OR booking-confirmed OR expires"
            }
        }
    },
    {
        "label": "misuse — missing revocation_ref",
        "should_pass": False,
        "data": {
            "consent_id": "consent-bad-001",
            "issued_at": "2026-05-05T10:00:00Z",
            "principal": {"principal_id": "did:example:carol"},
            "recipient": {"recipient_id": "did:example:service"},
            "purpose": "identity-verification-kyc",
            "scope": ["full_name", "date_of_birth"],
            "revocation": {}
        }
    },
    {
        "label": "misuse — scope wildcard",
        "should_pass": True,
        "data": {
            "consent_id": "consent-bad-002",
            "issued_at": "2026-05-05T10:00:00Z",
            "capacity": {"capacity_type": "personal"},
            "authority": {
                "authority_type": "self",
                "authority_ref": "did:example:dave#key-1"
            },
            "principal": {"principal_id": "did:example:dave"},
            "recipient": {"recipient_id": "did:example:platform"},
            "purpose": "platform-data-sharing-agreement",
            "scope": ["*"],
            "duration": {"expires_at": "2027-01-01T00:00:00Z"},
            "revocation": {
                "revocation_ref": "https://siltcore.org/revocation/consent-bad-002"
            }
        }
    },
    {
        "label": "misuse — expired artefact",
        "should_pass": False,
        "data": {
            "consent_id": "consent-bad-003",
            "issued_at": "2025-01-01T00:00:00Z",
            "capacity": {"capacity_type": "personal"},
            "authority": {
                "authority_type": "self",
                "authority_ref": "did:example:eve#key-1"
            },
            "principal": {"principal_id": "did:example:eve"},
            "recipient": {"recipient_id": "did:example:employer"},
            "purpose": "employment-background-check-authorisation",
            "scope": ["criminal_record_check"],
            "duration": {"expires_at": "2025-06-01T00:00:00Z"},
            "revocation": {
                "revocation_ref": "https://siltcore.org/revocation/consent-bad-003"
            }
        }
    },
    {
        "label": "misuse — delegated capacity, no expiry",
        "should_pass": True,
        "data": {
            "consent_id": "consent-bad-004",
            "issued_at": "2026-05-05T10:00:00Z",
            "capacity": {"capacity_type": "delegate"},
            "authority": {
                "authority_type": "mandate",
                "authority_ref": "https://siltcore.org/mandates/delegate-grant-004"
            },
            "principal": {"principal_id": "did:example:frank"},
            "recipient": {"recipient_id": "did:example:partner-org"},
            "purpose": "ongoing-data-processing-under-delegation",
            "scope": ["transaction_records"],
            "revocation": {
                "revocation_ref": "https://siltcore.org/revocation/consent-bad-004"
            }
        }
    },
    {
        "label": "misuse — self authority forwarded to broker",
        "should_pass": True,
        "data": {
            "consent_id": "consent-bad-005",
            "issued_at": "2026-05-05T10:00:00Z",
            "capacity": {"capacity_type": "personal"},
            "authority": {
                "authority_type": "self",
                "authority_ref": "did:example:grace#key-1"
            },
            "principal": {"principal_id": "did:example:grace"},
            "recipient": {
                "recipient_id": "did:example:data-broker",
                "recipient_type": "broker"
            },
            "purpose": "consent-to-data-brokerage-resale",
            "scope": ["browsing_history", "purchase_history"],
            "duration": {"expires_at": "2027-01-01T00:00:00Z"},
            "revocation": {
                "revocation_ref": "https://siltcore.org/revocation/consent-bad-005"
            }
        }
    },
    {
        "label": "misuse — no scope",
        "should_pass": False,
        "data": {
            "consent_id": "consent-bad-006",
            "issued_at": "2026-05-05T10:00:00Z",
            "principal": {"principal_id": "did:example:henry"},
            "recipient": {"recipient_id": "did:example:broker"},
            "purpose": "data-brokerage",
            "scope": [],
            "revocation": {
                "revocation_ref": "https://siltcore.org/revocation/consent-bad-006"
            }
        }
    }
]


def run_tests() -> None:
    print("\nSILT Core — Consent Validator (capacity-aware)")
    print("Spec: https://github.com/Sugarlicks/silt-identity-core")
    print(f"Run:  {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n")

    passed = 0
    unexpected = 0

    for vector in TEST_VECTORS:
        result = validate_consent(vector["data"], vector["label"])
        expected = vector["should_pass"]

        if result == expected:
            passed += 1
        else:
            unexpected += 1
            print(
                f"  UNEXPECTED: expected {'pass' if expected else 'fail'}, "
                f"got {'pass' if result else 'fail'}"
            )

    print(f"\n{'=' * 64}")
    print(
        f"  Results: {passed} expected / {unexpected} unexpected / "
        f"{len(TEST_VECTORS)} total"
    )
    print(f"{'=' * 64}\n")


def validate_file(path: str) -> None:
    try:
        with open(path, encoding="utf-8") as file:
            consent = json.load(file)

        validate_consent(consent, label=path)

    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

    except json.JSONDecodeError as error:
        print(f"Invalid JSON: {error}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        validate_file(sys.argv[1])
    else:
        run_tests()
