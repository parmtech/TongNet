# TongNet — Deep Logic & Security Audit V1.1

**Date:** 2026-10-25. **Status:** Internal design review, NOT external independent audit. 24 specific weaknesses, competing failure states and candidate corrections; 20+ protocol assertions, no proof of absolute safety. Reviewed in context of latest owner decisions.

**Canonical revised plan:** [WHITEPAPER_MASTER_V1_1_SECURITY_REVIEW.md](WHITEPAPER_MASTER_V1_1_SECURITY_REVIEW.md). **Historical predecessor:** [V1.0 master](WHITEPAPER_MASTER_V1_0.md). All owner-confirmed rules outrank architect suggestions. Mainnet must not proceed while red blockers remain.

---

# 26. V1.1 Adversarial Logic Audit — Consolidated Corrections

**Audit status:** Internal architecture scrutiny, not external smart-contract, crypto, consensus, financial or legal audit. Important findings are documented honestly; any unresolved RED issue blocks handling real user value. This addendum corrects logical omissions and a few misleading V1.0 numeric proposals.

## A. Critical money/control invariants

**A1 — Validator-set revocation vs immutable BFT epoch:** V1.0 wrongly implied S becoming DEAD could *immediately* remove its bonded voting power. Arbitrarily reducing an active validator set midheight can yield conflicting quorums. Fix: S wallet spending becomes DEAD atomically; validator eligibility enters exit scheduling; active voting-set membership changes only by consensus-final epoch transition preserving quorum intersection. Signer key compromise may require evidence-driven quarantine, but live committee disruption must fail closed. Successor R inherits only residual bond withdrawal entitlement after slash/evidence obligations; no auto-activation of S validator.

**A2 — No safe invariant for node counts alone:** 64 active keys, 32 standbys, 128 full nodes and 16 archives are *coverage targets*, not guaranteed independent operators. Require independent beneficial-control and stake-distribution audits with adversarial stress testing. Hidden operator grouping is an unavoidable uncertainty. Limit launch reliance on founder/related stake; no account-based voting caps bypassable by Sybil wallet splits.

**A3 — Emission/treasury capture:** Previous 12m genesis + 17.6m first-four-year emission would inflate circulating/genesis stock dramatically (146.7% potential new issuance vs genesis). And former 25/15/10 validator-bootstrap/treasury/team slices could have aligned control of up to 50% genesis. Both proposed schedules are withdrawn. No mainnet supply issuance parameters should be coded until market cost-of-corruption, reward-budget sustainability and independent distribution are analysed. A 100m cap is still only a *candidate*, not monetary authority.

**A4 — Token-denominated min bond has no fixed economic cost:** 25k TONG cannot secure anything when TONG has unknown initial exchange value or liquidity; replace with bonded stake whose effect is assessed relative to actual circulating stake, stake acquisition/borrow markets and validator real expense. The testnet can have a fixed dummy bond to exercise logic; production requires separate security/economics review.

**A5 — Slashing and exit overlap:** Protocol evidence age in both seconds AND block heights must be strictly shorter than slashable unbonding retention under worst-case slowdown and checkpoint retention. Cite CometBFT evidence parameters and test after upgrade. An operator can otherwise equivocate, exit and withdraw before objective evidence is processed. Normal phone loss should not automatically confiscate a security bond.

**A6 — Block size overwhelms a lean chain:** 2MiB every 4sec is 45.3GB/day and 16.5TB/365 days of RAW block bytes; with indexes and archives more. Reduce exploratory max to 256KiB/6sec (3.77GB/day, 1.38TB/year fully occupied) and explicitly estimate on-disk/index growth. A 512KiB expansion needs multi-region storage/fee tests; design pruning/snapshot and archive proofs separately. State action throughput should be measured in *complete 3-phase payments* as well as raw actions.

**A7 — Three-stage fees not actually paid by the proper actors:** Receiver may have 0 TONG but must CLAIM. Initial Sender LOCK must prepay bounded, non-transferable escrow operations budget for one valid Receiver claim and one Sender accept or later sender reclaim; protect relays against unbounded wrong-code spam through stateless rejection, replay nonces, fair P2P bandwidth budgeting. Fees are charged for executed operations; unused budget returns under known outcome. All fee escrow and future network storage liabilities count toward conservation and wallet recovery rules.

**A8 — Fee farming / thin liquidity:** Ordinary self-transfer must be net-costly and pay independently eligible unrelated validator committee. No reward for creating a payment or merely signing an external receipt. A randomized committee still can be bribed; reward allocation can't claim proof of genuinely expensive computation from a signature alone. At low traffic 64 always-online validators and archive nodes cannot be sustainably financed solely from tiny fees without transparently defined issuance/sponsorship; stress cost assumptions and don't promise profit.

## B. BlackBox and escrow correctness

**B1 — Lock before K_R generation was unsafe:** Prepare entropy-bound claim signing credential and persist encrypted backup *before* network LOCK; public credential commitment bound to the escrow. Release to receiver ONLY after BFT-final LOCK. If client loses power between preflight and finality, safely replay/sync LOCK and persisted secret by tx id, never create a funded lock with missing key. Ensure an out-of-band copy or alternative controlled recovery matches owner intent.

**B2 — Human-short code can't be public-hash-verified safely:** A 6-digit code commits only ~20 bits; publishing hash/commitment leaks brute-force oracle. Recommend native one-time secret signing key with public verification key committed at LOCK, receiver signs unique request under both receiver own key and imported one-time key. Encode secret through trusted QR/long code; shorter UX needs a separately rate-limited cryptographic exchange and independent audit, not a public hash.

**B3 — Separate signed ACCEPT authority had no full failure model:** Binding must include unique tx id, chain id, receiver key, exact requested amount, claim request id, deadline version, and sender BlackBox one-time monotonic accept nonce. Validator requires the registered independent Sender BlackBox public authorization key plus S wallet authorization model. Compromised validator cannot conjure approval. Sender can refuse; do not claim merchant fair exchange.

**B4 — Inconsistent 24h/60d and delay-proof timing:** Receiver **claim plus Sender final accept must both BFT-finalize** within effective receiver window; receiver claim merely entered mempool before cutoff does not create ownership. Sender's subsequent 60 full days start only after adjusted receiver priority ends. Test exactly-at-cutoff determinism, epoch reorg impossibility under BFT assumption, and competing expiry ops. Exact causal network-delay seconds cannot be proven under arbitrary asynchronous adversaries; preserve owner intent but classify as unsolved, protect funds and prohibit retroactive inconsistent rights.

**B5 — Sender K_S paradox remains a real-money stopper:** Owner's late-only creation of a sender reclaim key after 24h is impossible to reproduce on a destroyed device/BlackBox, including from an earlier mirror. Proposed **consent-dependent** alternative: prepare sealed high-entropy reclaim seed/commitment at LOCK, derive or reveal the working K_S credential only after finalized receiver window expires under authenticated control; requires formal source/R roles, anti-early-use proof and owner approval because it alters the literal late-only secret-generation rule. Without that approval & audit, not deployable.

**B6 — Unsound confiscation of old escrow:** After sender 60d window owner has proposed loss of remaining funds to network treasury. Do not implement until applicable legal/regulatory analysis, explicit informed consent and recovery for provable outages; otherwise use no real-fund mainnet or narrowly defined PROTECTED_SUSPENSE on research testnet. Permanent protected suspense is itself an economic/liveness concern that must be resolved, not treated as a free solution.

**B7 — Receiver/claim griefing and storage pressure:** One signed Claim_REQUEST must not exhaust pre-funded fee budget to force forfeiture through recipient delay; enforce accepted receiver identity, one live claim id/escrow, replacement only under strictly defined explicit sender/receiver consent, and no negative fee budget. Price 61-day conditional state storage, limit payload size and max escrows per limited-resource account. Beware fee-on-failure unauthenticated spam.

## C. Recovery and validation boundary

**C1 — Encrypted archive is not cryptographically locked if R has key:** UI-hidden ciphertext is not unreadable if R device already possesses all decryption shares. Conditional key release anchored to a BFT-final authenticated S→R event requires an independently reviewed threshold/key-escrow architecture, explicit collusion and liveness assumptions, rotating keyshares across validator-set changes and backup key-retention rules. Neither network state nor smart contracts can prevent early offline decrypt by an already fully equipped recipient. No false guarantee of zero trust.

**C2 — Active R vs virgin-at-first-bind contradiction across stale docs:** Latest owner decided R remains independently NORMAL_ACTIVE while serving as S recovery and may own R→C; fresh at first binding was *not expressly revoked*. Treat fresh initial binding as preserved until owner clarifies. Any older RECOVERY_RESERVED_FROZEN description is historical only; latest S→R and DEAD-target auto-unbinding govern.

**C3 — R DEAD while parent archive copies exist:** Consensus-final R DEAD revokes active S→R immediately, never automatically recovers S into R's own successor C. A already-mirrored S ciphertext may remain in R→C encrypted backups; C must NOT obtain S parent decrypt authorization merely by B→C recovery. Data-retention/crypto-shredding and loss warnings require formal treatment.

**C4 — Active stake balances after disaster:** R receives only S unlocked TONG atomically; S outgoing escrows and validator bonds remain in segregated rights states. Source DEAD cannot directly vote with former S wallet key. Recovery carries a *pending withdrawal beneficiary* entitlement for non-slashed bond post unbonding rather than immediate spend. Still needs explicit owner sign-off: staking adds a new financial asset classification to earlier recovery rights.

**C5 — Wallet 72h activation DEAD/initial loss:** On-chain address registration and fresh wallet deposits must reject pre-activation funding atomically, otherwise funds may permanently die when activation deadline expires. Define whether unactivated/never-funded addresses occupy consensus storage (state rent) and wallet restoration path.

## D. Network security, legal and implementation

**D1 — Upgrades cannot be only stakeholder-controlled on cheap early supply:** Publicly reveal parameter changes in advance, independent builds, minimum notice and fixed client constraints (especially supply cap and owner-signature requirements). Concentrated holdings still allow coercive forks, which users may refuse; no absolute governance guarantee.

**D2 — Crypto algorithm choices are not cryptographic proof:** Choose audited standard Ed25519 / SHA-2 or equivalent as supported by validator/wallet libraries, authenticated encryption/key derivation, disjoint key domains, test vectors across platforms and secure random-number generation. Distinguish post-quantum migration research from protection actually present today.

**D3 — Regulatory reality:** Australia's 2026 DAF Act has new regulated platform requirements commencing **9 April 2027**, potentially relevant depending on whether ParmTech operates a digital asset platform/custody service, and 2026 ASIC draft standards. Noncustodial chain software is not automatically a licensed financial service, nor automatically exempt. Obtain independent Australian legal classification before promotion/listing/custody. Preserve self-custody, no price/yield guarantee or unapproved reserve confiscation.

**D4 — Release gate is not number of documents:** No mainnet until correct monetary authority, audited escrow/recovery/key-release logic, formal state invariants, experimental committee attacks with independent stake, 90-day public adversarial testnet, no critical/high fund-loss findings and external legal/compliance advice. Research models can be "complete plans" without claiming deployed code or zero bugs.

# 27. V1.1 Reference Corrections: Explicit Design Parameters

| Parameter | V1.0 draft | V1.1 recommendation |
|---|---|---|
| Consensus | Bonded PoS + BFT | Unchanged. Reviewed BFT global finality, stable signed epochs and independent nodes. |
| Active/standby/full/archive targets | 64/32/128/16 | Retain as *scale targets only*; hard launch gate on independent voting control, not count. |
| Block target/max | 4s / 2MiB | 6s / 256KiB initial benchmark; 512KiB later optional. |
| Throughput | 100 state actions/s target | 20 state actions/s first adversarial test; measure complete 3-phase payments/s separately. |
| Genesis/supply | 100m cap, 12m genesis, 17.6m first-era, 50%-potential related entities | Keep 100m cap as **nonfinal reference**; **withdraw emission/genesis fractions** pending economic security+fair allocation audit. |
| Min bonded stake | 25,000 TONG | No mainnet absolute threshold before attack-cost pricing; disposable faucet testnet only. |
| Equivocation slash | 5% trial | Not selected pending attack/evidence modelling. |
| Validator maturity/unbond | 7d / 28d example | Retain only as research benchmarks; evidence lifetime must fit in unbonding. |
| Claim secret | Constructed at/after final LOCK | Prepare encrypted one-time proof key **before** LOCK broadcast, deliver only after final LOCK. |
| Receiver fee | Implicit / unfunded | Sender prepays bounded Receiver claim+Sender finalize/reclaim budget at LOCK. |
| Tx-driven votes | 3 actions sometimes described as verifying | Only optional unrelated receipt auditing; stake BFT decides canonical state. |
| BlackBox mirroring | R active, ciphertext sealed | Unchanged with serious unapproved conditional key-release implementation blocker. |
| DEAD-source validator | Immediate revoke in active quorum | Endorse wallet DEAD instantly, consensus validator exit only with quorum-safe epoch transition. |
| Post-60d treasury | Owner intent | Never irreversible mainnet confiscation without law/consent/outage closure; protected research state is not a complete solution. |

**Internal logic audit concluded:** V1.1 fixes contradictions in its design choices and measurement claims, but does **not** solve the real cryptographic impossibility/key-loss/permissionless economic risk classes. Readiness remains **NOT READY FOR REAL FUNDS**. Mainnet authorisation requires engineering evidence and owner approval for any change to owner-confirmed financial rights.


## Supporting technical sources

- CometBFT BFT <1/3 assumptions: https://github.com/cometbft/cometbft/blob/main/spec/README.md
- CometBFT evidence limitations and evidence age: https://github.com/cometbft/cometbft/blob/main/spec/consensus/evidence.md
- CometBFT genesis/evidence/unbond time coupling: https://github.com/cometbft/cometbft/blob/main/docs/core/using-cometbft.md
- Cosmos staking slashing and slashable unbond: https://github.com/cosmos/cosmos-sdk/blob/main/x/staking/README.md
- Australian Federal DAF legislation: https://www.legislation.gov.au/C2026A00038/latest/text
- ASIC consultation 15 October 2026: https://www.asic.gov.au/regulatory-resources/find-a-document/consultations/cp-392-digital-asset-law-reform-implementation-proposed-standards-and-guidance
