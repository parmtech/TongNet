# TongNet — Hybrid Proof-of-Stake + Transaction Participation + BFT

**2026-10-25 | OWNER ASKED FOR DESIGN RESEARCH, NOT YET APPROVED PARAMETERS OR CONSENSUS.**
TongNet remains a single native TONG coin Bitcoin-like blockchain, with separate Wallet, BlackBox, Authenticator, Active Recovery Mirror V4, bilateral manual Secure P2P and no third-party dApp/token platform. There is NO implemented/tested mainnet, PoS, validator or TONG emission schedule.

## Owner's specific design idea
If someone holds a threshold amount of TONG for an eligible length of time, their wallet can begin working as an optional Validator. Simultaneously, every regular payment's three actions (Sender INITIATE and network LOCK; Receiver signed CLAIM_REQUEST proving K_R knowledge; Sender independent BlackBox FINAL_ACCEPT) should contribute checkable work useful to third-party transactions. Preserve reciprocal validation/funding and reduce fee, while resisting fake wallets and misuse.

## Recommended candidate (research label: TongNet Bonded PoS + PoTP + BFT)
Three layers with disjoint security roles:

1. **Bonded proof of stake for Sybil cost and accountable voting:** users explicitly opt in and commit/spend-lock a native TONG `VALIDATOR_BOND` as distinct from ordinary balance, pending payment escrow, receiver claim code, recovery code and spending key. Merely holding coins in a wallet or waiting N days does NOT cause automatic consensus voting. A signed validator registration binds independent `validator_key`, `bond_owner_wallet`, activation epoch, and withdrawal address. The node must continuously verify ledger and be online when selected. Separate validation keys from wallet spending and BlackBox authorisation, as in Algorand's participation-key design. Wallet can continue normal operations with its *unlocked* funds. Opt-in required, no stealth lock.
2. **PoTP as separately verifiable reciprocal work:** at INITIATE, CLAIM_REQUEST, FINAL_ACCEPT, a lightweight phone can verify unrelated already-finalised proof/receipt / perform a small anti-spam work challenge if needed, then return a domain-separated `WORK_RECEIPT`. These are signed audit contributions, NOT any consensus votes unless the payer's separate bonded validator node was independently selected for those *other transactions*. Sender and receiver never confer independent votes on their own transfer merely through three signatures. No mandatory puzzle delaying FinalAccept before its expiry; offload work or perform asynchronously. Don't expose claim code plaintext.
3. **BFT consensus with stable epoch validator-set / weighted quorum:** independently selected online active validators run a proven multi-round round/height state-machine protocol on canonical blocks and all payment phases. Proposer is selected with verifiable entropy and unpredictable future-epoch stake set registration; snapshots freeze voting weights for rounds and prevent committee-grinding by transaction author. Finality requires >2/3 of voting power within the defined consensus security and partial-synchrony assumptions, not simply 7 out of 10 wallets. Safety assumes <1/3 Byzantine voting power; >1/3 absent prevents progress. Use independent full nodes to revalidate canonical state. Block finality is GLOBAL; choosing unrelated independent 10-person committees afresh per transaction without overlapping safety conditions can produce conflicting authorisations. Use epoch-anchored quorum certificates; investigate efficient VRF sampling only after safety proofs.

### Candidate validator life cycle (NO FINAL NUMBERS)
```text
NORMAL WALLET with unlocked TONG
 -> OPT_IN: user explicitly locks B >= B_min TONG for validator bond
 -> ACTIVATION_PENDING: stake finalised and held through maturation M epochs
 -> ELIGIBLE: registered separate validator key, data-synced node, eligibility/uptime checks
 -> SELECTED: weighted block proposal/prevote/precommit during assigned duty
 -> VERIFIED_SERVICE: consensus finality receipt, fee/reward allocation
 -> EXIT_REQUESTED: ineligible for new duty at designated epoch, but historical equivocation proofs still valid
 -> UNBONDING: locked bond continues slashable for safety challenge period U
 -> UNLOCKED: withdraw eligible remaining balance after release finality
```
Example prototype values **only** for simulations: M=7 days, U=21 days, B_min chosen relative to actual TONG supply and adversarial acquisition cost, not fixed to a fiat price. These are placeholders with no consensus-safe authority. Actual maturity and unbonding must be derived from maximum slashing evidence windows, chain synchrony/finality and validator attack economics. Time held > M grants NO compounding voting weight merely for age.

### Selecting validators while limiting fake wallet attacks
- Select eligible validator-duty participants via committee from registered stakes committed **before** selection randomness can be anticipated (VRF/verifiable delayed beacon; risk of stake-grinding/seed manipulation separately analyzed). Weight proportional to economically bonded stake under an owner-approved vote-weight policy and use a stable chain-wide BFT quorum per epoch/height or a formally proven committee safety protocol.
- Attacker splitting 1000 TONG bonded across 100 addresses should not obtain 100 times the selection weight: selection probability depends on **total bonded TONG**, not wallet count. No arbitrary "one validator = one vote" without robust unique-personhood. Naive per-wallet weight CAP is Sybil-bypassable by splitting. Wealth concentration remains a real risk: stake-weight security is not human-identity independence.
- Minimum bond deters very cheap Sybils but large capital can still buy/collude into 1/3+ of the voting weight and censor or halt; 2/3+ can subvert BFT safety under its assumptions. Neither amount held nor maturity proves an independent human/owner. Need independent node operator incentives, self-hosting, no single issuer, geographic/network failure scenarios.
- Don't allow owner-restricted money / payment escrow as validator bond. Bond is slashable **only on cryptographic evidence of specified faults** (e.g. equivocation), and must not be silently lost because phone is offline. Availability policy separately pays less or deactivates after repeated offline missed duties; slashing for normal outage is risky.
- Register vote keys and vote-weight changes through consensus, apply only at later epoch after finality. BFT quorum certificates bind epoch validator-set hashes; never allow conflicting committee definitions to finalise conflicting blocks.

### 3 core payment actions + work contribution + BlackBox
```text
Sender Wallet signs INITIATE exact recipient, TONG amount, tx ID
 -> SENDER BlackBox locally generates random high-entropy K_R and privately shares externally
 -> OPTIONAL local PoTP verifies unrelated prior finalized checkpoint (or bounded spam proof)
 -> BFT committee verifies spendability, atomically LOCKs TONG, records canonical state/deadline t0 proposal

Receiver Wallet signs CLAIM_REQUEST for tx with ZK/hiding knowledge proof of K_R
 -> OPTIONAL local PoTP verifies independent unrelated checkpoint
 -> committee confirms exact recipient + request uniqueness, DOES NOT PAY YET
 -> securely deliver authenticated request to Sender BlackBox

Sender BlackBox signs FINAL_ACCEPT for exact immutable request/wallet/amount/asset/nonce
 -> no mandatory extra puzzle in critical path
 -> selected validator consensus verifies proof and settles BEFORE adjusted 24h receiver cutoff
 -> committee returns verifiable finality certificate and eligible service receipts

No accept by receiver expiry -> separate 60 FULL DAYS sender manual reclaim, K_S generation/recovery issue OPEN.
```
Receipt / private data mirrored to currently-active R Recovery Wallet's sealed *parent BlackBox archive only*, not rewriting old ledger transactions. Validator receives public proofs only, never raw K_R, Master Authenticator key, recovery secret or decrypt key.

### Reciprocal rewards, optional monetary fee
- A normal TONG transaction might pay a calibrated tiny fee of F TONG; fees are transferred (not minted) from sender to quorum reward pool/reserve under owner policy. This prevents unrestricted zero-cost Sybil spam while funding online validation. Dynamic bounded per-byte/per-signature fees can be researched to keep small payments usable.
- Verified independent validator service earns a share of fee pool by finalised protocol receipts, not just by self-assigned 'vote OK' declarations. Stake itself does not promise an investment return. Validator payouts cannot be guaranteed; depend on actual availability/fees/risk.
- A person's ordinary payment can optionally emit verifiable PoTP audit/check receipt about an unrelated transaction. If rewarded, budget it from explicitly funded pool and have independent assignment/anti-farming; **NEVER give PoTP receipts voting weight and NEVER mint TONG automatically on sending oneself coins or pressing FinalAccept**.
- Strong distinction: refundable bond B_min is collateral returned after unbonding minus justified slash. Transaction fee F is payment for network service; it is not by definition refundable. Earned validator reward E may offset F but is not guaranteed.

### Economic example (NOT policy)
User X owns 1000 TONG. They opt in to stake 200; 800 remain unlocked. Their computer or opt-in supported mobile node validates blocks while online. X's ordinary transfer pays a hypothetical 0.01 TONG (fee depends on load/policy). Separately, legitimate successful consensus duty yields a reward from the network fee pool. There is NO promise the reward equals 0.01 TONG. One person may create 20 wallets but cannot multiply its total 200 TONG stake by dividing them.

### Phone / infrastructure
- A wallet app can trigger full-node setup and notify the user when eligible. But phones routinely suspend background tasks; some mobile platforms do not support always-on full-node consensus reliably. Eligibility requires verified continuous operation; phone may be light-work/remote-controller, user computer/server runs a validator they control; alternative custody-free delegation is possible but centralises validators.
- Network operation and checkpoint progression must persist with no user payment volume; a newly arriving transaction still needs accessible validator quorum. Validator nodes in this architecture are dedicated online service providers in practice, even though controlled by ordinary users. "Only users who are currently transacting" is NOT sufficient for always-available consensus.
- Network backup costs, communications, evidence storage, recovery BlackBox mirrored ciphertext, data availability must be separately funded. Work receipts for casual phones cannot guarantee durable data storage.

### Recovery / key safety integration (CRITICAL)
- Validator signing key is neither spending private key nor BlackBox key nor wallet authenticator seed. On Source S permanent DEAD after successful S->R disaster, **stop/revoke S's validator participation**; do NOT continue signing with an archived S validator key. Bonded stake may be pending exit/unbonding and potential slashing for old misconduct; it must **NOT be double transferred as an unlocked balance**. Need a protocol-authorised succession claim for the bond's remaining withdrawal entitlement to R, retaining evidence and unbonding window, without auto-activating R as S validator. This modifies prior recovery-only-spendable rules and must be explicitly approved before release.
- The Recovery Target R is itself NORMAL_ACTIVE while bound; R may already have its own separate validator stake. Its own bond/validator credential must not be merged or overwritten by S recovery. If R network-final DEAD, S->R recovery binding auto-revokes as latest owner rule. If source gone/lost no pre-staged BlackBox K_S, late sender reclaim remains unresolved.
- Attackers with validator keys cannot forge S sender FINAL_ACCEPT or unlock parent archive; release policy for truly sealed archive remains open.

### Key attack simulations / kill criteria
1. Fake wallet/stake split: total stake unchanged => total expected vote weight unchanged; check small-stake election and per-wallet cap bypass.
2. Attacker controls >1/3 or >2/3 stake; partitions, equivocation, liveness failure; model network-scale attacker budget, no 'cannot be hacked' claim.
3. Fake traffic and reward farming: no own-tx-service rewards that exceed fees; constrain unrelated verification claims and nonce reuse.
4. Empty/mixed traffic periods: protocol produces finality/checkpoints even when no transactional flow and offers capacity for first new TX.
5. Validator phones offline/background killed; replacement respecting BFT committee safety; do not slash ordinary user for brief outage.
6. Stake-registration randomness grinding, front-running validator selection, adaptive DDoS, bribery, pool dominance, chain reorganisations, censorship.
7. Receiver claim races or BlackBox FinalAccept approaching deadline; always require independent canonical finality, keep PoTP asynchronous.
8. Stake exit vs Source S DEAD / Recovery R successor, locked bond entitlements, prior equivocation penalties, replay, double-credit.
9. Protect BlackBox K_R, S one-time Sender K_S, master and encrypted mirror vs compromised validator. Avoid exposing plaintext to committee.
10. Benchmark throughput/latency/fee, attack cost, bandwidth/storage, code complexity vs a conventional PoS+BFT baseline and Bitcoin PoW.

### Recommendation / approval questions
**Candidate for prototypes:** bonded stake permits validator eligibility, stable-epoch stake-weighted BFT security, VRF/research committee election, 3-stage transaction-linked *nonvoting* validation/audit contributions, fee reward mechanism and distinct BlackBox second consent. First prototype fixed/limited testnet with property-based attack tests, then research randomized committee and mobile participation. Restrict complexity: PoTP may only be optional audit work initially so it never creates extra consensus attack surface. No promise of zero fees/automatic validator earnings or superiority over Bitcoin.

**Open for user confirmation:** opt-in vs automatic onboarding (recommend explicit opt-in); whether B_min lock, maturation, unbonding and possible slash conditions acceptable; full validator participation from phone vs other hardware; initial fee/reward budget; what happens to staked S during recovery; whether PoTP must be mandatory in all three stages despite latency. Actual monetary/emission parameters remain unapproved.

### Public technical references
- Ethereum proof of stake and staking duties: https://ethereum.org/developers/docs/consensus-mechanisms/pos/
- Ethereum slashing/offline distinction: https://ethereum.org/staking/solo/
- CometBFT Byzantine consensus: https://github.com/cometbft/cometbft/blob/main/spec/consensus/consensus.md
- Algorand registered participation keys and VRF committee selection: https://dev.algorand.co/concepts/protocol/overview/
- Algorand stake weight per account rather than account count: https://dev.algorand.co/concepts/protocol/overview/

**Attribution:** ParmTech; original creator/developer Manjinder Singh. 2015 concept origin and first public disclosure 2026 creator-reported, not independently verified.
