# SILT Identity Core

SILT Core is an identity layer that formalises status, standing, and authority before attributes, agency, or credentials.

## What this repository is
This repository defines a small, composable set of open identity primitives for expressing:

- **Principal** – who can bind themselves or another party
- **Status and standing** – the capacity in which a principal acts
- **Authority and delegation** – acting “for and on behalf of” with explicit scope
- **Consent** – enforceable constraints, not interface convention
- **Revocation** – the right to withdraw authority and end reliance

The goal is infrastructure: specifications, schemas, threat models, and a minimal reference implementation that downstream systems can adopt incrementally.

## What this repository is not
SILT Core is not:

- a wallet
- a chain-specific implementation
- a credential issuer or KYC system
- a governance platform
- a token model or tokenomics framework
Bitcoin scope (for this repo)
SILT Core defines wallet-layer semantics for bounded delegated signing authority (e.g. time-limited delegation, amount-constrained spending, revocable delegation). It does not require Bitcoin consensus changes or BIP-level modifications.

Bitcoin wallet use case (illustrative)
Alice controls a wallet and wants to grant Bob the ability to spend up to 0.05 BTC over the next 30 days, revocable at any time. Rather than sharing keys or rebuilding multisig policies, the wallet records a delegated authority grant with explicit scope constraints, temporal validity, and revocation state. Each signing request validates that the grant remains active, the spend falls within constraints, and no revocation has occurred.

## Why this matters
Across digital identity systems, consent and delegation are routinely treated as UX copy rather than enforceable technical constraints. This enables over-disclosure, silent authority escalation, coercion, correlation, and lock-in. SILT Core externalises these concerns into shared primitives so implementers can reduce fragility and attack surface.

## Repository structure
- `docs/` – overview, design principles, glossary, threat model
- `spec/` – normative definitions of principals, standing, delegation, consent, revocation
- `schemas/` – machine-readable schemas for interoperability and validation
- `reference/` – minimal reference implementations and examples
- `tests/misuse-cases/` – explicit misuse and failure-mode test vectors

## Status
This project is in early specification stage. The initial focus is to publish clear semantics, a threat model, and reference schemas, then iterate toward a minimal reference implementation and test suite.

## Licence
See `LICENSE`.
