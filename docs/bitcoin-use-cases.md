Bitcoin Wallet Use Cases (Draft)
1) Time-limited, amount-constrained delegation

Goal: Allow a user to delegate limited spending authority without sharing keys.
Example: “Bob may spend up to 0.05 BTC total within 30 days. Revocable at any time.”

Key requirements: explicit scope constraints, temporal validity, revocation state, auditable delegation chain.

2) Organisational treasury controls

Goal: Express role-bounded authority for treasury operations (e.g. proposer vs approver vs executor).
Example: “Ops may initiate spends up to X; Finance must countersign above X; Security may revoke any delegation.”

Key requirements: clear capacity declaration per action, bounded delegation, reconstruction of authority provenance.

3) Inheritance and contingency workflows

Goal: Express constraints on authority transfer workflows without key disclosure.
Example: “After a defined trigger condition, designated parties may initiate a controlled transfer workflow with bounds and review.”

Key requirements: trigger representation, multi-party oversight, revocation/override paths, auditability.
