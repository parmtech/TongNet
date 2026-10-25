# TongNet — Current Decision & Conflict Register
**As of:** 2026-10-25. Older exploratory docs often contradict later owner decisions; this is the canonical short authority index.

## CONFIRMED_BY_OWNER
- **C-001:** TongNet independent Bitcoin-purpose single TONG coin; no public dApps/EVM, third-party tokens.
- **C-002:** Source Wallet INITIATE/LOCK, one-use K_R known out-of-band to receiver, receiver own-wallet CLAIM_REQUEST, **separate Sender BlackBox manual FINAL_ACCEPT** required to pay Receiver. No third-party deal arbiter; no 3h Trigger.
- **C-003:** Receiver exclusive nominal 24h, then Sender following 60 full days to MANUALLY reclaim; no auto-refund at 24h. Exact starting t0 after removal of Trigger awaits ratification.
- **C-004:** User seeks network-caused delay compensation 1:1 where independently proven, with hybrid global and per-operation evidence. No universally provable exact seconds under arbitrary partitions.
- **C-005:** Owner intent remaining unclaimed escrow after rights expire to Network Reserve; real-value implementation held pending safety/legal review, not a unilateral rewrite.
- **C-006:** Active Recovery R stays NORMAL_ACTIVE even while bound to S and independently may designate C. Only **encrypted S BlackBox data**, origin tagged, mirrored sealed; never S old ledger tx or duplicate balance. R must not decrypt while S ACTIVE.
- **C-007:** S Private Key + Authenticator initiate recovery request, R BlackBox signed ACCEPT final within original adjusted 24h; one-use disaster key generated in R BlackBox after accept. Authenticated S->R disaster makes S DEAD, only eligible liquid S funds transfer once as new ledger tx, and R stays ACTIVE.
- **C-008:** When R is consensus-final DEAD, S->R recovers NONE and is revoked automatically. S stays ACTIVE but unprotected until new eligible R2 accepts; no automatic inheritance via R->C.
- **C-009:** Earlier "R must be virgin at *initial* pairing" retained unless explicitly revoked; this doesn't freeze R after pairing.
- **C-010:** Trusted bilateral counterparty payment without merchant dispute arbitration.
## ARCHITECT_SELECTED_PROTOTYPE (NOT RATIFIED MAINNET)
- **A-001:** Tested BFT engine + voluntary bonded PoS; optional transaction-level PoTP audit does not confer consensus votes.
- **A-002:** Account-based deterministic native state interpreter and checked nonces/balances, no public contracts.
- **A-003:** Fee + Earn model; Sender prepaid bounded 3-phase budget, earned verified independent validator duty (not promised investment return).
- **A-004:** 4–7 localnet validators, aim for independent public testnet 21→64, ≥32 standby/128 full nodes, no magical safety from node count.
- **A-005:** 6sec / 256KiB and 20 state actions/s are INITIAL TEST TARGETS only, not achieved.
- **A-006:** Potential 100m TONG cap / 8 decimals only candidate; V1.0 12m genesis/17.6m first-era/percentage allocations WITHDRAWN; no real emission approved.
- **A-007:** Stake 7-day maturity / 28-day unbond merely test hypotheses. No absolute min TONG bond nor fixed slashing % ratified.
- **A-008:** High-entropy K_R prepared and durably encrypted **before** LOCK broadcast and shared only after final LOCK, to prevent stranded lock without claim key; change to user-facing code format awaits UX/crypto review.
## UNRESOLVED / OWNER APPROVAL OR INDEPENDENT PROOF
- **U-001:** Ratify exact LOCK as 24h t0 and boundary/exclusion logic.
- **U-002:** Sender K_S only generated after 24h conflicts with lost/dead BlackBox, need approved sealed precommit/recovery or explicit loss policy.
- **U-003:** Sealed S parent archive decrypt gating without giving R offline key, threshold assumptions and keyshare outage/collusion.
- **U-004:** S DEAD with outgoing locked escrow, receiver claims, pending FINAL_ACCEPT and bonded stake successor withdrawal rights.
- **U-005:** Post-60d Network Reserve confiscation lawful informed consent, disputes/outage remedy.
- **U-006:** Objective globally/locally compensated deadlines under censorship/partial network partitions.
- **U-007:** Supply cap/emission/genesis anti-capture distribution and effective stake attack cost.
- **U-008:** Short human-readable claim-code security vs long high-entropy code/signature/QR UX.
- **U-009:** Multiple S sources bound to R, independent mirrored archive retention, R initial virgin rule future clarification.
- **U-010:** Consensus-safe epoch validator exit when S DEAD and slashing bond held.
- **U-011:** Chain software financial/legal/custody/marketing classification and qualified advice.
- **U-012:** Initial wallet Authenticator required ≤72h else wallet DEAD, avoid funded unactivated irreversible loss.
## OBSOLETE
- Old 3-hour Trigger, 72-hour reclaim, recovery frozen while S ACTIVE, S->R->C auto-forward, publicly creatable custom tokens/EVM, old 12m genesis 17.6m emission and unchecked fee refund.
## Protocol change process
New owner decisions: open issue/ADR, cite the explicit approved choice, update canonical docs and property tests; NEVER silently replace financial ownership or authority with an architect guess. Work on source only behind test-only flags if U is unresolved.
