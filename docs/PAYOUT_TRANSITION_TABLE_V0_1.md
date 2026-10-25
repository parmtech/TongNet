# TongNet payout transition table v0.1

**Status: proposal for owner ratification.** This is a candidate deterministic policy for test fixtures, not an approved financial rule, production implementation, or authority to move real value. It must be accepted or revised by the owner before any fund-moving implementation relies on its candidate timing semantics.

## Authority and candidate

Confirmed direction preserved from C-002/C-003:

- A receiver's `CLAIM_REQUEST` does not pay an escrow.
- Payment requires a separate Sender BlackBox `FINAL_ACCEPT` for the exact claim.
- The receiver has a nominal 24-hour exclusive priority; the Sender then has the following 60 full days to manually reclaim.
- There is no automatic refund at 24 hours and no 3-hour Trigger.

L-01 recommends BFT-final `LOCK` as `t0`, but U-001 says this anchor and its boundary/exclusion rules are not owner-ratified. The table below is one explicit candidate for that decision. L-35 also leaves the consensus clock, height mapping, and clock-drift assumptions open.

Candidate parameters:

- `t0`: canonical consensus time attached to the BFT-final `LOCK` block.
- `D_receiver = 86,400` seconds.
- `D_sender = 5,184,000` seconds (60 full days).
- `t_receiver = t0 + D_receiver`.
- `t_sender_end = t_receiver + D_sender = t0 + 5,270,400` seconds (61 days after `t0`).

These intervals are exact candidate semantics only. The timestamp source must be a ratified, versioned consensus-time policy; wall-clock values from clients, RPC, or mempool are never deadline evidence.

## Candidate transition table

| Current state | Operation / finalized-time condition | Required authorization and evidence | Next state | Monetary effect |
|---|---|---|---|---|
| None | Valid `LOCK` is BFT-final | Sender-authenticated lock; verified finalized block context; unique escrow ID | `LOCKED` | Debit Sender spendable and credit this escrow atomically |
| `LOCKED` | Receiver `CLAIM_REQUEST` finalizes at `t0 <= t < t_receiver` | Addressed Receiver; valid one-use claim proof; verified finality context | `CLAIM_PENDING` | None |
| `LOCKED` or `CLAIM_PENDING` | Sender `FINAL_ACCEPT` finalizes at `t0 <= t < t_receiver` | Sender BlackBox authorization bound to escrow, claim ID, Receiver, and exact amount; verified finality context | `PAID` | Credit that Receiver once; debit escrow once |
| `LOCKED` or `CLAIM_PENDING` | Sender `SENDER_RECLAIM` finalizes at `t_receiver <= t < t_sender_end` | Sender authorization; eligible Sender signing capability; verified finality context | `RECLAIMED` | Credit original Sender once; debit escrow once |
| `LOCKED` or `CLAIM_PENDING` | Evaluated at `t >= t_sender_end` | Verified finalized context under the same versioned policy | `POLICY_PENDING` (derived eligibility label) | None; no automatic refund, reserve transfer, or burn |

### Exact boundary behavior in this candidate

- At `t0`, the Receiver-priority interval is open for eligible operations.
- At `t_receiver` exactly, Receiver-priority `CLAIM_REQUEST` and `FINAL_ACCEPT` are ineligible; the Sender's manual reclaim interval begins and is inclusive.
- At `t_sender_end` exactly, Sender reclaim is ineligible; the escrow becomes `POLICY_PENDING` with no automatic money movement.
- A request that is still `CLAIM_PENDING` at `t_receiver` expires for this candidate's receiver-priority rule. This is a consequential interpretation and requires an explicit owner decision.
- Eligibility labels are derived from finalized context; elapsed local time does not itself mutate a stored escrow state.
- `PAID` and `RECLAIMED` are mutually exclusive terminal outcomes. Once either is committed, every later payout/reclaim operation fails atomically with no balance, supply-counter, or nonce effect under the test-only rule in TN-SPEC-001.
- Multiple transactions in one finalized block are interpreted by increasing transaction index. Across blocks, use finalized (epoch, height) order. The first valid terminal operation consumes the escrow; a later conflicting operation cannot win by timestamp, retry, or replay.

## Finality evidence boundary

The ledger transition function accepts a `VerifiedFinalizedTx` context only after the consensus adapter verifies finality under the active, versioned validator-set rules. The context must bind at least:

`chain_id`, `protocol_version`, `epoch`, `height`, `block_hash`, `validator_set_hash`, `consensus_time`, `transaction_index`, `transaction_hash`, and the verified block-inclusion/finality evidence.

The ledger does not trust an unverified client-supplied timestamp or independently invent a quorum threshold. Mempool acceptance, block proposal, RPC observation, local clocks, and unfinalized votes do not change payout eligibility or balances. A missing, invalid, cross-chain, wrong-version, or inconsistent finality context fails closed.

## Owner decisions required before fund movement

1. Ratify or replace `t0 = BFT-final LOCK consensus time` (U-001 / L-01).
2. Ratify the exact receiver and Sender intervals, including the inclusive/exclusive cutoffs above.
3. Decide whether an outstanding `CLAIM_PENDING` at `t_receiver` expires, remains eligible for later Sender approval, or follows another rule.
4. Approve a canonical consensus-time representation, height/time mapping, drift bounds, and delay-compensation treatment (L-35 / L-05).
5. Resolve Sender `K_S` availability if the Sender BlackBox is lost after 24 hours but before reclaim (U-002); the table does not invent a replacement key or bypass.
6. Ratify the legal and consent-safe post-window treatment. This proposal leaves funds in `POLICY_PENDING`; it does not authorize reserve transfer (U-005 / L-04).
7. Decide open-escrow rights if the Sender wallet becomes DEAD (U-004 / L-08).

No production financial action is permitted by this proposal. The branch is stacked on TN-SPEC-001 PR #49 to avoid duplicating that specification's current tracking changes; review PR #50 against that base, then retarget it to `main` after PR #49 is merged.
