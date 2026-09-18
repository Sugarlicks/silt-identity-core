#!/usr/bin/env python3
"""Validate the SILT Core v0.2 minimal semantic conformance suite."""
from pathlib import Path
import json, sys
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CONF = ROOT / "conformance"
SCHEMA_PATH = CONF / "SILT_v0.2_Minimal_Semantic_Conformance_Schema.json"
SUITE_PATH = CONF / "SILT_v0.2_Minimal_Semantic_Conformance_Suite.json"

schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
suite = json.loads(SUITE_PATH.read_text(encoding="utf-8"))
errors = sorted(Draft202012Validator(schema).iter_errors(suite), key=lambda e: list(e.path))
if errors:
    for e in errors:
        print("SCHEMA ERROR:", "/".join(map(str,e.path)), e.message)
    sys.exit(1)

allowed = ["SATISFIED", "NOT_SATISFIED", "INDETERMINATE"]
if suite.get("allowed_evaluation_outcomes") != allowed:
    raise SystemExit(f"Outcome vocabulary drift: {suite.get('allowed_evaluation_outcomes')!r}")

base_count = 0
variant_count = 0
for we in suite["worked_encounters"]:
    base_count += 1
    records = [(we["base_fixture"].get("case_id", we["id"]+"-base"), we["base_fixture"])]
    records += [(we["id"]+"-"+v["id"], v) for v in we.get("variants", [])]
    variant_count += len(we.get("variants", []))
    for rid, rec in records:
        for ev in rec.get("expected_evaluations", []):
            if "outcome" in ev:
                if ev.get("outcome") not in allowed:
                    raise SystemExit(f"{rid}: invalid evaluation outcome {ev.get('outcome')!r}")
            elif "permitted_outcomes" in ev:
                vals = ev.get("permitted_outcomes") or []
                if not vals or any(v not in allowed for v in vals):
                    raise SystemExit(f"{rid}: invalid permitted_outcomes {vals!r}")
            else:
                raise SystemExit(f"{rid}: evaluation must declare outcome or permitted_outcomes")
            if not ev.get("profile_expression_id"):
                raise SystemExit(f"{rid}: evaluation missing profile_expression_id")
        for ne in rec.get("not_evaluated_conditions", []):
            if "outcome" in ne:
                raise SystemExit(f"{rid}: not_evaluated condition must not contain an outcome")
        if "aggregate_result" in rec:
            raise SystemExit(f"{rid}: aggregate_result must not be inferred at record level")
        if rid != we["base_fixture"].get("case_id", we["id"]+"-base"):
            if rec.get("expected_implementation_conformance") not in {"CONFORMING", "NON_CONFORMING"}:
                raise SystemExit(f"{rid}: adversarial variant missing expected implementation conformance")
            if rec.get("architecture_test_result") not in {"PASS", "FAIL"}:
                raise SystemExit(f"{rid}: adversarial variant missing architecture test result")

summary = suite.get("suite_result", {})
if summary.get("worked_encounters") != base_count:
    raise SystemExit(f"Summary worked_encounters={summary.get('worked_encounters')} but counted {base_count}")
if summary.get("adversarial_variants") != variant_count:
    raise SystemExit(f"Summary adversarial_variants={summary.get('adversarial_variants')} but counted {variant_count}")
if summary.get("new_universal_core_object_required") is not False:
    raise SystemExit("Suite summary must explicitly record no new universal Core object required for this release candidate")

print(f"PASS: schema valid; {base_count} base fixtures; {variant_count} adversarial variants; outcome vocabulary locked.")
