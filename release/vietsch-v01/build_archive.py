#!/usr/bin/env python3
"""Build an auditable, pilot-only SILT v0.1 research archive.

Run from repository root:
  python release/vietsch-v01/build_archive.py

The script never publishes, creates a GitHub release, or deposits with Zenodo.
It requires the exact source files and creates a manifest with SHA-256 hashes.
"""
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "dist"
ARCHIVE_NAME = "silt-vietsch-aut-cisrc-v01-pilot.zip"
SOURCES = [
    "archive/v0.1/spec/delegation.md",
    "archive/v0.1/spec/revocation.md",
    "archive/v0.1/schemas/delegation.schema.json",
    "archive/v0.1/schemas/revocation.schema.json",
    "archive/v0.1/LICENSE",
    "LICENSES/Apache-2.0.txt",
    "LICENSES/CC-BY-4.0.txt",
    "release/vietsch-v01/README.md",
    "release/vietsch-v01/RELEASE_NOTES.md",
    "release/vietsch-v01/LICENCE_STATUS.md",
    "docs/AUT_CISRC_v0.1_STATUS.md",
    "docs/implementation-profiles/aut-cisrc/README.md",
    "docs/implementation-profiles/aut-cisrc/AUT-CISRC-Implementation-Profile.md",
    "docs/implementation-profiles/aut-cisrc/authority-chain.md",
    "docs/implementation-profiles/aut-cisrc/pilot-workflow.md",
    "docs/implementation-profiles/aut-cisrc/validation-logic.md",
    "docs/implementation-profiles/aut-cisrc/initial-review.md",
    "docs/implementation-profiles/aut-cisrc/phase-3-pilot-evaluation.md",
    "docs/implementation-profiles/aut-cisrc/VIETSCH_V01_SPECIFICATION_PROVENANCE.md",
    "schemas/implementation-profiles/aut-cisrc/README.md",
    "schemas/implementation-profiles/aut-cisrc/authority-chain.schema.json",
    "schemas/implementation-profiles/aut-cisrc/delegation.schema.json",
    "schemas/implementation-profiles/aut-cisrc/access-request.schema.json",
    "schemas/implementation-profiles/aut-cisrc/revocation.schema.json",
    "schemas/implementation-profiles/aut-cisrc/validation-result.schema.json",
    "reference/validators/aut-cisrc-delegation/README.md",
    "reference/validators/aut-cisrc-delegation/validate.py",
    "tests/aut-cisrc/test_pilot_v01.py",
]
SOURCES += sorted(
    str(p.relative_to(ROOT))
    for p in (ROOT / "examples/aut-cisrc-research-delegation").rglob("*")
    if p.is_file() and p.name != ".gitkeep"
)
if len(SOURCES) != len(set(SOURCES)):
    raise SystemExit("Duplicate release path in manifest.")
missing = [p for p in SOURCES if not (ROOT / p).is_file()]
if missing:
    raise SystemExit("Missing release source files: " + ", ".join(missing))
if not all(p.startswith(("archive/v0.1/", "release/vietsch-v01/",
                         "docs/AUT_CISRC_v0.1_", "docs/implementation-profiles/aut-cisrc/",
                         "schemas/implementation-profiles/aut-cisrc/",
                         "reference/validators/aut-cisrc-delegation/",
                         "tests/aut-cisrc/", "examples/aut-cisrc-research-delegation/",
                         "LICENSES/Apache-2.0.txt", "LICENSES/CC-BY-4.0.txt")) for p in SOURCES):
    raise SystemExit("Archive contains path outside v0.1 package allowlist.")
try:
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
except (OSError, subprocess.CalledProcessError):
    commit = "unknown-commit"
files = [
    {"path": p, "sha256": hashlib.sha256((ROOT / p).read_bytes()).hexdigest(),
     "bytes": (ROOT / p).stat().st_size}
    for p in sorted(SOURCES)
]
manifest = {
    "project": "SILT Core v0.1 Vietsch AUT CISRC pilot",
    "archive_type": "synthetic-non-normative-research-implementation",
    "source_commit": commit,
    "file_count": len(files),
    "files": files,
    "license_note": "Project-authored narrative files specifically enumerated in release/vietsch-v01/LICENCE_STATUS.md are additionally CC BY 4.0; implementation code and machine-readable artefacts are Apache 2.0. Existing historical Apache grants are preserved.",
    "tested_evidence": "https://github.com/Sugarlicks/silt-identity-core/actions/runs/39848903516"
}
OUT.mkdir(exist_ok=True)
def add(zf, name, data):
    entry = zipfile.ZipInfo(name, date_time=(2026, 10, 23, 0, 0, 0))
    entry.compress_type = zipfile.ZIP_DEFLATED
    entry.external_attr = 0o644 << 16
    zf.writestr(entry, data)

target = OUT / ARCHIVE_NAME
with zipfile.ZipFile(target, "w") as z:
    for item in files:
        add(z, item["path"], (ROOT / item["path"]).read_bytes())
    add(z, "RELEASE_MANIFEST.json", (json.dumps(manifest, indent=2) + "\n").encode())
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files) + 1
    for item in files:
        assert hashlib.sha256(z.read(item["path"])).hexdigest() == item["sha256"]
print(json.dumps({"archive": str(target), "files": len(files),
                  "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                  "source_commit": commit}, indent=2))
