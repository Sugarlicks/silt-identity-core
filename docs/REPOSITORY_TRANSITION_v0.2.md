# Repository transition notes for v0.2

The current public repository still contains v0.1-era top-level material that conflicts with the v0.2 architecture. In particular, the existing README, GOVERNANCE and CONTRIBUTING files describe `Status`, universal `Capacity`, mandate-centric primitives and v0.2 as future planning. Those files must not remain authoritative beside the v0.2 release.

Before tagging `v0.2.0`:

1. replace the repository README with the v0.2 release-facing README;
2. replace GOVERNANCE.md and CONTRIBUTING.md with the v0.2 versions in this package;
3. add LICENSING.md, IPR_POLICY.md and TRADEMARK_AND_CONFORMANCE.md;
4. add `LICENSES/CC-BY-4.0.txt` and `LICENSES/Apache-2.0.txt`, and ensure the root licence presentation no longer implies that all narrative specification material is Apache-licensed;
5. place the v0.2 Semantic Architecture in the normative spec path and mark conflicting v0.1 material historical or superseded;
6. add the conformance suite and CI workflow;
7. migrate or clearly label older schemas/examples using the v0.1 -> v0.2 classification rather than performing name-only replacements;
8. preserve AUT CISRC as a versioned SILT Core v0.1 implementation profile. It is outside the v0.2 migration scope and MUST NOT be relabelled as v0.2-conformant.

The repository URL confirmed for this release is:

https://github.com/Sugarlicks/silt-identity-core
