# TongNet — A-to-Z Long-Horizon Architecture & Risk Audit
**Audit date:** 2026-10-25, Australia/Sydney. **Review:** internal forward-looking engineering analysis, not independent security certification. **Basis:** latest owner-directed TongNet single-coin product, V1.1 Master Whitepaper, Active Recovery Mirror V4, 24h Receiver + next 60 days Sender BlackBox payment and PoS/PoTP candidate. **Purpose:** anticipate problems before months of development lock in irreversible financial protocol choices.

## 0. Audit rules and authority
- Preserve USER-CONFIRMED behavior; do not overwrite owner rights via "suggested fix". Distinguish: **C** owner confirmed, **R** architect recommendation, **U** unresolved/needs consent, **B** launch blocker, **D** already demonstrated by passing code/test evidence. No code or cryptographic proof exists just because an item is described.
- Do not misrepresent earlier frozen-R, 3h Trigger, 72h reclaim, general-purpose tokens/dApps, or genesis token figures as latest active product scope. Old docs are historical and often internally inconsistent. Latest hierarchy: owner explicit decisions > [Active Recovery Mirror V4](ACTIVE_RECOVERY_MIRROR_V4.md) / [Secure P2P V3](SECURE_P2P_V3_RECOVERY_DECISIONS.md) > [V1.1 design](WHITEPAPER_MASTER_V1_1_SECURITY_REVIEW.md) > older drafts.
- Prioritise real value conservation and inability to forge sender approval over UX speed, high TPS or consensus novelty. Fail CLOSED if quorum/state/clock proof doubtful.
- A perfect "no misuse possible" guarantee cannot be delivered in an open adversarial cryptocurrency; each claim needs explicit fault/collusion assumptions, proofs, tests and incident handling.

## 1. Root architectural contradictions to resolve before building monetary behavior
**L-01 [P0, B] Payment clock origin.** The 3-hour Trigger was eliminated, so **BFT-final LOCK as receiver 24h t0** is an architect recommendation, not the owner's explicitly ratified deadline anchor. Every timeline/penalty depends on it. Action: ADR with crisp scenarios at t0±1 block, timezone-independent integer canonical consensus time, owner ratification.

**L-02 [P0, B] Lost/DEAD Sender BlackBox cannot generate K_S after 24h.** If device dies at hour 5, post-24h newly generated secret cannot be mirrored from the past. Action: design one-time sealed precommit/derivation bound to LOCK that remains cryptographically unusable until receiver window ends, with protected keys/threshold release and successor-specific rights. This materially changes earlier late-generation literal rule and REQUIRES owner consent; otherwise halt live funds.

**L-03 [P0, B] Conditional BlackBox decryption paradox.** If ACTIVE R already holds S archive ciphertext AND complete decrypt material while S ACTIVE, R can decrypt offline irrespective of BFT. Action: security-model independent threshold keyshares or guarded user-held secret, with collusion thresholds, rotation, denial-of-service, disaster scenarios, consent proofs, failure recovery, ciphertext rollback/retention; independent cryptographic review before asserting privacy.

**L-04 [P0, B] Post-60d forfeiture to Network Reserve.** Cannot confiscate real user funds solely based on failed phones, disabled users, network outage or manipulated deadlines. User had proposed confiscation; not authorised for live implementation. Action: owner decision + specific risk/legal opinion, explicit pre-transaction consent, outage handling, constitutional limits on treasury. Until closed use *testnet-only* protected unresolved state; indefinite suspense is itself a liveness bug, not a final production fix.

**L-05 [P0, B] Universal exactly one-to-one network delay credits.** In asynchronous networks, nodes cannot always attribute per-second latency to culpable network versus censored messages, intentionally offline devices or fake evidence. Action: versioned partial synchrony model, bounded independently signed receipts, global incident intervals with set union and deterministic proof cutoff, no retroactive contradictory settlement; proof + owner agreement on irreducible ambiguity and indefinite suspense exits.

**L-06 [P0, U] Fresh recovery R vs independently ACTIVE R.** Latest R remains usable after pairing, but earlier owner initial-binding virginity not explicitly revoked. Action: formal test for "R zero financial history at ACCEPT finality, then normal use allowed"; owner review only if changing it. Never freeze R after binding.

**L-07 [P0, B] Recovery target DEAD first.** R consensus-DEAD triggers atomic auto-unbind S->R with S UNPROTECTED, NOT automatic forward S to R's successor C. Need alerting, backup retention/wipe model, S lost credentials, replay/race modeling.

**L-08 [P0, B] Source DEAD during locked outgoing claims.** S owns different rights over its spendable, locked outgoing escrow, pending Sender FINAL_ACCEPT and post-receiver reclaim. Recovery S->R cannot rewrite transaction history, bypass waiting windows or silently impersonate S. Action: separate entitlement and successor authorization matrix per state and finality race.

**L-09 [P0, U/B] Validator bond vs DEAD S.** S immediate DEAD does NOT justify unilaterally shrinking active BFT validator set mid-round; bonded slash liabilities remain. Action: safe epoch exit/reconfiguration, successor residual withdrawal rights after unbond, separate voter/spender keys, formal owner approval of new class of succession.

**L-10 [P0, B] Wallet 72h activation DEAD.** Prefunded not-yet-activated wallets risk permanent unspendability. Action: reject transfers/preallocated economic value to unactivated addresses or ratify a no-loss safe alternative. State machine must distinguish local app stale from network-final DEAD.

## 2. Ledger and cryptographic correctness
**L-11 [P0] Cryptographic transaction domain mismatch.** Include chain ID, network version, account nonce, action, exact escrow ID, recipient, amount, authorisation role and expiry; block wrong-network relay/replay, duplicate CLAIM and acceptance.
**L-12 [P0] Recipient code guessing oracle.** No raw short 6-digit claim codes or plain hashes on-chain. Use pre-LOCK generated high-entropy one-time signing credential and commitment or independently audited ZK proof, wallet+claim secret dual signatures, safe one-time final state; user consent required for changed code UX.
**L-13 [P0] Post-lock code loss.** Encrypt + durably persist K_R with tested crash recovery BEFORE broadcasting LOCK; Sender shares only after BFT final LOCK; test crashes between every fsync, send, mempool and commit.
**L-14 [P0] Fee starvation / griefing.** Receiver may hold 0 TONG: Sender prepays bounded one claim and final accept/reclaim execution; malicious wrong-code requests cannot drain escrow budget or permanently block finality. One active claim, rate limits and independently budgeted non-chain relay layer.
**L-15 [P0] Circular Fee+Earn incentives.** Own transfers cannot create net-profitable credits; validators may be bribed, rewards must align with stake-weight risk. Simulate fake self-trades, low-volume funding deficits, independent fee recipients, treasury insolvency and proof-of-useful-work gaming.
**L-16 [P0] Supply issuance origin not justified.** 100m cap only candidate. V1.0 12m genesis, emission and genesis allocation withdrawn due to inflation/control. Build genesis only after fair transparent distribution, real corruption-cost budget, legal and supply economic stress test.
**L-17 [P0] Asset conservation and overflow.** Separate spendable, escrow, validator bonds, rewards, fee escrow and treasury under checked integer arithmetic; all state transitions preserve total supply except documented issuance/burn; no double counting on disaster.
**L-18 [P0] Consensus determinism boundary.** No application state changes from mempool CheckTx, proposal speculation, clock reading or RPC queries. Commit strictly through decided block execution, deterministic serialization, crash/replay simulation and state-root differential testing. Version-pin CometBFT ABCI++ behavior; don't assume v1.0 docs cover all future APIs.
**L-19 [P0] Cryptographic key roles confused.** Spending wallet, BlackBox FINAL_ACCEPT, Authenticator, validator votes, K_R, K_S, disaster key, archive keyshares all separate derivation domains and revocation authorities. No one validator/website obtains wallet/master keys. Threat model browser/phishing/copy-paste leakage.
**L-20 [P0] Quantum/agility and upgrades.** Ed25519 candidate is not quantum resistant. Versioned key/sig types, crypto registry, multiple signature tests and staged migration; avoid unreviewed PQ custom crypto and huge vote certificates.
**L-21 [P1] Fee budget expiration and refunds.** Who pays for 61-day escrow storage, multiple retries and pending archive, when unused budget returns; no dust exploit or stealth hidden fees.
**L-22 [P1] BlackBox off-chain metadata leak.** Code delivery, inbox locations, parent address tagging and mirror replication can correlate counterparties even with ciphertext. Threat-model access logs, social engineering and ciphertext retention.

## 3. Consensus, staking, network and independence
**L-23 [P0] Validator-key count is not independence.** 64 validators can be controlled by one business. Stake acquisition/borrowing, cloud-provider concentration, cartel identities and bootstrap allocations matter. Audit beneficial control where practicable; opaque actors remain irreducible risk. No naive one-wallet cap.
**L-24 [P0] Bond denominated only in unpriced TONG.** Token amount does not equal real attack cost. Model liquid market, borrowable stake, time-lock, slashing deterrence, bribery payoff and cartel consensus sabotage. Don't hardcode arbitrary mainnet 25k.
**L-25 [P0] Stake distribution at genesis.** Foundation/program/team allocations could dominate early consensus; 12m and 50%-influenced initial proposal rejected. Independent distribution and governance escrow needed before mainnet.
**L-26 [P0] BFT churn and mid-epoch safety.** Distinct validator sets must preserve quorum intersection and deterministic update height (e.g. CometBFT validator updates returned at H effective H+2 in some ABCI++ versions; verify exact pinned version). No panic replacement in partition.
**L-27 [P0] Evidence expires before unbond.** MaxAgeDuration and MaxAgeNumBlocks interplay must be tested against unbond/exits, downtimes, delayed blocks and evidence censorship. Slashing threshold cannot be absolute % divorced from attack economics.
**L-28 [P0] 1/3 offline vs 1/3 Byzantine ambiguity.** More than 1/3 absent prevents BFT liveness, and sufficiently corrupted voting can break safety assumptions. Never "lower quorum" to restore transactions.
**L-29 [P1] Weak VRF / committee-grinding.** Selection randomness cannot be manipulated by sender nonce, last block producer, transaction content or fresh stake identities. Snapshot stake before seed; epoch states and delayed proof tests.
**L-30 [P1] Phone never reliably 24h validator.** Background limits, thermal constraints, battery, mobile NAT, intermittent sleep. Wallet may do optional light work; robust full nodes require stable device/server or explicitly tested remote signer/delegation policy.
**L-31 [P1] RPC/seed DNS / cloud centralization.** Public network must survive ParmTech/Namecheap/cloud/DNS death and hostile eclipse. Independent peers, source bootstrapping, verified checkpoints, signature-authenticated versioned releases, P2P rate limits.
**L-32 [P1] State sync and archive economics.** 256KiB/6sec can generate ~3.77 GB/day raw saturated blocks before indexes; pruning and archival replication need signed snapshots, Merkle proof verification, archive proof/reward and storage retention budget.
**L-33 [P1] Network zero traffic.** Validators must stay live even without payment actions; exclusively active senders cannot provide quorum. Infra reward model can't rely on each transaction paying for permanently idle nodes in tiny market.
**L-34 [P1] DoS and fee auction.** Claim spam, empty block clogging, cheap self-transfers, log/metric blowup, mismatched mempool/app fee rules and priority censorship. Price resource, bounded queues and adversarial chaos.
**L-35 [P1] BFT finality vs time-of-day.** One proof of BFT-finality is stronger than a queued transaction. Every 24h/60d deadline must use consistent consensus time/height, replay across restart and tolerate clock drift only under specified assumptions.
**L-36 [P1] Node update and genesis splits.** Network upgrade can fork voting set or state roots if nodes run mismatched versions, chain IDs, migrations or unsupported serialization. Reproducible signed artifacts and deliberate upgrade epochs.
**L-37 [P1] Archive data availability and R mirror lag.** A backups cannot recover data never replicated, while stale provenance can present false completeness; periodic authenticated checkpoints and warnings.
**L-38 [P1] Evidence-based automated validator quarantine.** False accusations, arbitrary cloud bans and incomplete evidence must not let automation confiscate user stakes or strand network in conflicting sets.
**L-39 [P1] Long-range/weak-subjectivity replay.** PoS light clients and nodes coming online after months need trusted recent finality checkpoint/trust-period policy. Document trust root and rollback behavior; different from Bitcoin PoW validation.
**L-40 [P1] Mirror ciphertext storage and erasure rights.** Deleting active binding does not erase copies held by other parties. Model lawful privacy/deletion expectations without promising reversible public chain history.

## 4. Security lifecycle, operations, funding and compliance
**L-41 [P0] No safe upgrade emergency key.** Security updates need owner-independent adoption and time-lock with narrow emergency shutdown; admin cannot bypass user approval or money conservation, and exposed validator key must not become network master.
**L-42 [P0] Mainnet funds before independent audits.** Block until independently reviewed escrow, consensus adapter, crypto key release, recovery succession, economics, legal and public adversarial testnet evidence; never use marketing dates as security gates.
**L-43 [P0] Australian and cross-border law.** Crypto platform/custody, token selling, token distribution, financial promotion, sanctions/AML/privacy/tax rules vary. No implicit assertion all permissionless software is exempt; legal review appropriate for actual ParmTech operating roles.
**L-44 [P1] Treasury capture and gifts.** Reserve donations/grants controlled by undisclosed admins can look like hidden tax, investment or fund misallocation; transparent public disclosure, capped purpose, timelock and audit.
**L-45 [P1] CI and supply-chain compromise.** GitHub Actions secrets, unpinned third-party Actions, AI-generated code, malicious dependencies, web build scripts and release binary swaps; signed commits/releases, restricted workflow write rights, least privilege CI, SBOM and reproducibility.
**L-46 [P1] Parallel-worker conflicts / stale documents.** Multiple agents change latest source and stale spec copies without reading override register, causing tests on incompatible facts. Every task needs one canonical GitHub Issue, isolated branch, dependencies and reviewable PR; no "implemented" without CI evidence.
**L-47 [P1] Dead project/resumption failure.** Day-by-day notes or ChatGPT memory are NOT canonical. Project state must be in GitHub Issues, structured registry, latest decision log, append-only session notes and generated dashboard. External agent reads AGENTS.md and repo status before changes.
**L-48 [P1] Fake automated progress.** Daily GitHub workflow can recompute status only from Issues/commits and report unchanged activity; must not claim coding happened, close tasks, or fabricate percentages. Scheduled Actions may be delayed or disabled after prolonged inactivity; manual workflow_dispatch and session updates remain supported.
**L-49 [P1] Off-chain secret loss and recovery false comfort.** Wallet recovery keys, Validator signer, BlackBox mirror decrypt capability, auto-unbinding and archive replica coverage all independent; users need realistic loss simulation, recovery drills and safe UX.
**L-50 [P1] 24/7 incident/response capacity.** A permissionless network cannot depend on sole creator being awake; published severity handling, independent monitoring and stop/fail-closed incident procedures with postmortems.

## 5. Priority, architectural answer and kill-gates
- **P0 financial blockers first:** L-01–L-19 (as applicable), L-23–L-28, L-41–L-43. Do not freeze a genesis while unapproved supply/distribution, unprovable delay/secret release or recovery transfer rights are unresolved.
- **Prefer simple, reviewable tested core:** Account-based native escrow/nonce/state categories and non-programmable single TONG. Rust deterministic state machine integrated through pinned ABCI++ boundary to existing-reviewed BFT network. No novel transaction-as-consensus votes.
- **Security costs must be explicit:** User-paid small fees + actual verified bonded validator service, funded archive and transparent reserve; PoTP optional non-voting audit/anti-spam. Fees refunded only as distinct funded rebates, never infinite fee-farm cycles.
- **Do not implement planned promises as verified features:** 64/32 nodes, <20sec p95, 6sec/256KiB, 100m cap, 7d maturity/28d exit are *reference hypotheses*. Runtime and economic attack testing decides final.
- **For a safe first executable step:** specify exact deterministic conservation/escrow state transitions and implement test-only Rust reference model with test coins, no market or public deposit addresses.
- **Evidence of completion:** cross-linked issue, commit/PR, test output, reviewer ACK and updated ADR/requirements, not a checkbox by itself.

## 6. Hard conditions to revisit at 3, 6, 12 and 24 months
3 months: pinned runtime compatibility, contributor workflow, deterministic tests, memory/resources, no fund migration.
6 months: consensus client known vulnerabilities/upgrade schedule, economic utility, attack-collusion stress, replication reliability.
12 months: validator identity/control concentration, treasury capture, crypto agility, legal shifts, database archival cost and disaster drills.
24 months: version migration, replay safety for old keys, cryptographic deprecations, partial loss of early operators, governance capture / hostile forks.
Each checkpoint is an action item not a promised automatic event. Open GitHub Issues and record results.

## 7. External reference anchors
- CometBFT ABCI++ deterministic app contract and finalisation: https://github.com/cometbft/cometbft/blob/main/spec/abci/abci%2B%2B_basic_concepts.md
- CometBFT consensus params/validator update effect at later heights: https://github.com/cometbft/cometbft/blob/main/spec/abci/abci%2B%2B_app_requirements.md
- GitHub Actions scheduled task caveats: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule
- Initial [V1.1 review](WHITEPAPER_MASTER_V1_1_SECURITY_REVIEW.md), and prior [24-point audit](LOGIC_SECURITY_AUDIT_V1_1.md).

**Summary:** 50 identified long-horizon risk items. None is independently audited. This file is a risk register and issue source, not proof that all risks are fixed.
