# Vietsch-supported SILT Core v0.1 AUT CISRC pilot

**Release scope:** Standalone archival research package of the constrained AUT CISRC delegation/revocation pilot funded by Stichting Vietsch, not the historical SILT v0.1 Core release and not the v0.2 Semantic Architecture.

The original SILT Core v0.1 release was published on **14 April 2026** at https://github.com/Sugarlicks/silt-identity-core/releases/tag/v0.1. This research package includes the historical delegation and revocation specification texts and schemas from `archive/v0.1/` for provenance, along with the later **non-normative** university-pilot implementation profile.

## Research result

A Python validator evaluates synthetic research delegations over an asserted university authority chain, checking actor, action, resource, purpose, time and revocation conditions. The recorded expanded regression suite passed **21/21 tests**, including representative schema conformance and malformed-input cases: https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516

The AUT profile's JSON data model differs from the original v0.1 Core schemas; a passing result **does not establish direct normative schema conformance**. Its asserted authority chain is synthetic: the pilot neither authenticates institutional powers nor integrates into live AUT IAM, and it is not officially endorsed by AUT.

## Reproduction

Install Python 3.11 or later and `jsonschema>=4.20,<5`; from the unpacked archive root:

```bash
python -m pip install 'jsonschema>=4.20,<5'
python -m unittest discover -s tests/aut-cisrc -p 'test_*.py' -v
```

The reference validator, five AUT implementation-profile schemas, original v0.1 delegation/revocation specifications, examples, evaluation report and diagrams are within the package. See `RELEASE_MANIFEST.json` for every archived path and SHA-256.

## Source and acknowledgement

Original public repository: https://github.com/Sugarlicks/silt-identity-core  
Funding: Stichting Vietsch (Vietsch Foundation).  
Project lead: Gareth Farry.  
Report: `docs/implementation-profiles/aut-cisrc/phase-3-pilot-evaluation.md`.

## Rights and versioning

See `release/vietsch-v01/LICENCE_STATUS.md` and per-file notices. **A universal single licence is not declared for this mixed research archive.** No Creative Commons relicensing of historical files is performed by this packaging step.

No DOI is assigned by this README. Cite the final archive DOI only once Zenodo has accepted a corresponding deposit.
