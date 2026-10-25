# ADR-0001 — Candidate native ledger and bonded BFT consensus
**Status:** ARCHITECT_SELECTED_PROTOTYPE, not owner-ratified mainnet emission/fund rights. **Date:** 2026-10-25.

## Decision proposed
TongNet v1 remains a single TONG currency with deterministic account/nonce/escrow lifecycle, no public EVM/contracts. Separate Rust native state machine communicates through a reviewed version-pinned ABCI++ BFT engine (candidate CometBFT). Stake-weighted, voluntarily bonded online validators supply Sybil cost; wallet transaction INITIATE, Receiver CLAIM and Sender BlackBox FINAL_ACCEPT contribute optional check/audit but DO NOT gain voting weight. No active validator set mid-height arbitrary changes.
## Alternatives considered
Custom transaction-only peer votes: free fake wallets seize approval and no transactions means no quorum; Bitcoin PoW: energy/resource demands and slower probabilistic finality; custom BFT: high original crypto/finality risk; smart-contract VM: user rejected.
## Guarantees and limits
No proven superiority to Bitcoin. 64 active validators etc are targets, not independence proof; CometBFT only orders blocks, native Rust handles finance. Per-height validator updates and speculative application calls must respect pinned engine semantics. Cannot run with real value until formal logic, economic stake independence and external security review pass.
## Owner decisions needed
K_S recovery, 24h t0, network delay proof, crypto mirror unlock, forfeiture, genesis/issued supply, R bonded funds migration and any change to latest owner rights.
## Validation
Bounded formal model + state property tests, deterministic replay, 4→64 node Byzantine/partition testnet, fee farm/Sybil stake split, recovery lost-device drills, genesis stake control and fee sustainability stress.
## Related issues
TN-ARC-001; TN-CONS-001; TN-SPEC-001; TN-MONEY-001.
