# SILT Identity Core

SILT Core is an identity layer that formalises status, standing, and authority before attributes, agency, or credentials.

## What this repository is
This repository defines a small, composable set of open identity primitives for expressing:

- **Principal** – who can bind themselves or another party
- **Status and standing** – the capacity in which a principal acts
- **Authority and delegation** – acting “for and on behalf of” with explicit scope
- **Consent** – enforceable constraints, not interface convention
- **Revocation** – the right to withdraw authority and end reliance

The goal is infrastructure: specifications, schemas, threat models, and a minimal reference implementation that downstream systems can adopt incrementally. SILT models not only who is acting, but in what capacity, under what authority, with what consent, and under what conditions that action may be relied upon or revoked.

Expression of standing must be coupled with a verifiable structure of authority, scope, and revocation.

Standing is expressed through declared capacity and scoped authority. Recognition may follow, but does not define validity.

## Positioning & Scope

SILT Core defines a semantic layer for expressing **capacity, authority, consent, and revocation** as preconditions for digital action.

It does not:
- issue identifiers (DIDs)
- define credential formats (VCs)
- execute policy decisions (e.g. Zanzibar, Cedar)
- provide wallets, chains, or applications

Instead, SILT operates **between identity/credential layers and policy execution**, providing a **capacity-aware gating layer** for action.

**Stack placement:**

- Identification → DIDs, keys  
- Assertion → VCs, relationship graphs  
- **SILT (this layer)** → capacity, authority, mandate, consent, revocation  
- Execution → policy engines, contracts, APIs  

SILT answers:

> In what capacity is an actor acting, under what authority, with what scope, and is that authority valid now?

This layer is required before evaluating what actions are permitted.

### Key Terms (v0)

- **Capacity** – the mode in which an actor is operating in a given action
- **Authority Source** – the origin from which that capacity is derived
- **Mandate** – the scoped expression of that authority
- **Consent** – explicit agreement to the act under defined conditions
- **Revocation** – termination of authority or consent

All actions SHOULD reference:
- declared capacity
- authority source
- scope (mandate)
- consent conditions
- revocation pathway

  ## Action Gating Model

SILT operates as a **precondition layer for action**, introducing a semantic gate prior to execution.

An action request should be evaluated against:

- declared capacity  
- authority source  
- mandate scope  
- consent condition  
- revocation status  

SILT supports three enforcement patterns:

### 1. Pre-flight Validation (middleware)
Requests are evaluated before reaching execution systems (APIs, policy engines).  
Invalid authority → request rejected.

### 2. Embedded Constraint (execution layer)
Capacity and authority constraints are included within transactions or contract calls.  
Invalid conditions → execution fails.

### 3. Reliance Gating (post-action)
Third parties evaluate whether an action was performed under valid authority.  
Invalid authority → action is not relied upon or treated as binding.

SILT does not replace execution systems.  
It ensures that only **validly authorised actions** reach them.

## Design Axioms

### 1. Authority Source Plurality
SILT does not assume a single source of authority. Authority must be explicitly referenced and scoped.

### 2. Capacity is Contextual
Capacity is defined by how an actor is acting in a given context, not by identity alone.

### 3. Revocation is First-Class
All authority and delegation must include explicit revocation and expiry pathways.

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
