# TongNet — A-to-Z Research and Development Roadmap

> **LATEST 2026-10-25:** Receiver-only 24h then Sender-only **60 DAYS** (72h superseded), verified delay credit where provable. Unclaimed funds to Network Reserve after expiry = owner intent, **blocked for real-money use pending legal and safety review**. Recovery Wallet must be fresh at pairing and RECOVERY_RESERVED (no ordinary Send/Receive), permits setup metadata acceptance; on final Disaster Recovery it inherits successor authority and becomes ACTIVE, original S becomes DEAD. Historical ledger remains immutable but view is linked; restoring encrypted BlackBox requires previously accessible encrypted backups, NOT spontaneous re-creation of lost secrets. Web clients MUST NOT transmit root/master/private keys to server. How to generate K_S after loss/DEAD of S and how to inherit pending rights remain OPEN. No third-party deal arbitrator. Full latest spec: [Secure P2P v3](SECURE_P2P_V3_RECOVERY_DECISIONS.md) (from repo root: docs/SECURE_P2P_V3_RECOVERY_DECISIONS.md). Older 72h and 3h Trigger records historical.


> **LATEST OWNER REQUIREMENTS — 2026-10-25:** Trusted two-party P2P with no deal arbitrator; validators verify signatures/finality, not buyer/seller disputes. The RECEIVER has the first 24h (clock at final LOCK proposed, not yet ratified). The SENDER then has **60 DAYS**, replacing earlier 72h, to manually reclaim; after that, creator wants remaining unclaimed escrow sent to Network Reserve (OWNER INTENT, **REAL-MONEY DEPLOYMENT BLOCKED** by unresolved legal/consumer protection safety). A special *fresh*, zero-prior-financial-transactions RECOVERY_RESERVED address may complete recovery pairing metadata but CANNOT ordinarily send/receive before one-time disaster-recovery settlement. After successful recovery, S becomes DEAD and R is successor NORMAL_ACTIVE; owner wants historical receipts, BlackBox encrypted backup and pending entitlements shown in R, not destructive rewriting of immutable ledger. Preexisting recoverable encrypted BlackBox backup is REQUIRED to restore lost device data; a lost unbacked secret cannot be resurrected, and wallet/master root secrets must never be sent to a website server. Late sender claim key K_S with LOST/DEAD BlackBox, pending consent migration, exact 24h anchor, and legal forfeiture remain OPEN. See [canonical 2026-10-25 decisions](docs/SECURE_P2P_V3_RECOVERY_DECISIONS.md). Older Trigger/72h/recovery-descriptions are HISTORICAL.


> **CURRENT RULE — 2026-10-25 (SUPERSEDES ALL OLD 3h TRIGGER CONTENT):** User REMOVED separate three-hour Trigger and its 3h automatic refund. Current TongNet Secure Manual P2P: Sender network-final LOCK -> Sender BlackBox makes and privately shares one-time Receiver Claim Code K_R -> exact addressed receiver wallet signs Claim Request -> Sender BlackBox must manually FINAL_ACCEPT exact transaction/recipient/amount -> BFT may finalise receiver settlement. No FINAL_ACCEPT means no receiver payout. No separate Trigger remains. Receiver 24h then Sender's following 72h manually redeemable via fresh Sender BlackBox K_S (verified attributable network delay extensions still apply); 24h from BFT-final LOCK is recommended but not explicitly ratified. No valid absolute guarantee against mistaken approval, stolen signing authority or third-party fraud. Old 3h Q7 disaster refund is obsolete; source DEAD + late K_S needs safe redesigned handling. See [canonical Secure P2P v2](docs/SECURE_P2P_V2.md) (for docs/ files: [canonical v2](SECURE_P2P_V2.md)).


**Stage:** Requirements elicitation only. Phases are planning milestones, **not** work already performed.

## Phase 0 — Living decisions and provenance (IN PROGRESS)
- [x] Verify and document TongNet GitHub repository
- [x] Record latest known name, attribution (ParmTech / Manjinder Singh) and creator-stated 2015 origin
- [x] Initialise user decisions, FAQ, transaction flow, security list and session handoff
- [ ] Ask all unresolved product and security questions one by one and commit each answer
- [x] Document Q3: optional Disaster Recovery Wallet and permanent source-wallet DEAD state (design only)
- [x] Document immutable disaster destination, one-use/nonreplaceable Disaster Recovery Key, and lost-key policy (design requirements)
- [ ] Resolve security of **initial** one-time recovery destination registration (not changing, which is prohibited)
- [x] Record Q6: Triggered escrow rights survive terminal rescue; receiver 24h then sender key used through linked rescue wallet within 72h if unclaimed (design only)
- [x] Q7: confirmed immutable recovery wallet receives automatic pre-trigger refund at original 3h timeout after source DEAD (design only)
- [x] Q8 clarification: one-use recovery secret is generated inside the DESTINATION recovery wallet's encrypted BlackBox (design only)
- [x] Q9: destination BlackBox Accept required before one-time key generation and immutable source→destination pairing; Reject sends source BlackBox notice; Pending means NOT_CONFIGURED (design only)
- [x] Q10: unanswered destination BlackBox pairing requests auto-expire after 24 hours (design only)
- [x] Q11: source cannot cancel/replace pending pairing; wait for recipient Reject or 24h Expired (design only)
- [x] Q12: strict network finality BEFORE pairing 24h deadline required; earlier tapping/signing is insufficient (design only)
- [x] Q13 network-queue intent: immutable timer speed, queue overload requests, NEW timers start after network acceptance (design documented; consensus finality is recommendation)
- [x] Q14: strict Claim consensus finality required before receiver/sender cutoff, even if queue admission occurred earlier (design only)
- [x] Q15: user-confirmed universal one-for-one network delay compensation for every affected time-limited operation (design only)
- [x] Q16: HYBRID per-operation AND global network delay evidence (user confirmed C); consensus-safe verification remains to implement
- [x] Q17–Q25 user choices documented: fake-delay proof, protected suspense, anti-Sybil, staged validator openness, automated governance, quarantine, standbys, safe quorums and precommitted rotations
- [x] 95 original deep questions reviewed in docs/MASTER_QA_RECOMMENDATIONS.md (recommendations, not all user ratified)
- [x] Research architecture spec saved in docs/TONGNET_FUTURE_ARCHITECTURE.md (not audited or deployed)
- [ ] Implement deterministic adjusted deadline computation and exclusive claim-window transitions
- [ ] Prove prevention of fictitious network delay, duplicate credits and expiry-vs-finality races
- [ ] Forced reserve forfeiture requires legal/informed-consent/consumer safety review regardless of adjusted deadlines
- [ ] Specify total-network outage response and risks of reclaim/forfeiture while consensus cannot progress
- [ ] Build bounded queue/rate-limiting/dedup/status receipts and anti-Sybil fairness tests
- [ ] Formalize network clock, acceptance/expiry ordering, no stale key issuance
- [ ] Define authenticated BlackBox Accept/Reject, request IDs, state conflicts and all-or-nothing key/registration finality
- [ ] Design secure key commitment, authenticated destination BlackBox issuance and replay protection
- [ ] Prove single-use, destination-binding and atomic settlement under concurrent receiver/sender/reserve operations
- [ ] Identify all contradictions and create versioned, reviewable spec decisions
- [ ] Preserve evidence and clarify publication/licensing strategy

## Phase 1 — Research and rigorous threat model (NOT STARTED)
- [ ] Prior-art review of related cryptographic payments and messaging systems
- [ ] Define decentralisation model, adversary budget, validator/node membership and incentive assumptions
- [ ] Define privacy, availability, latency, safety, scale and fee targets
- [ ] Evaluate lost-key, stolen-device, coercion, clock-drift and malicious-node threat paths
- [ ] Verify regulation of payment, reserve, coin issuance and automatic unclaimed-fund forfeiture

## Phase 2 — Formal protocol design (NOT STARTED)
- [ ] Choose secure cryptographic primitives and avoid custom cryptography
- [ ] Specify wallet/account identity, separate factor enrollment and BlackBox messages
- [ ] Specify atomic claims, state, expiries, replay protection and failures
- [ ] Propose consensus/finality without PoW or traditional PoS and justify Sybil resistance
- [ ] Prove safety/liveness assumptions and derive testable invariants
- [ ] Define token economics, custody, backing and reserve governance

## Phase 3 — Local research simulator (NOT STARTED)
- [ ] Deterministic local ledger model with fake TONG and virtual network clock
- [ ] Transaction state machine: locked → Trigger → claim / recover / expiry
- [ ] Tests for 3h no-trigger noncancellable wait, 24h claim and subsequent 72h recovery
- [ ] Adversarial concurrency, duplicate spend, malicious time and partition tests
- [ ] Report failures and update specifications

## Phase 4 — Multi-node prototype/testnet (NOT STARTED)
- [ ] Node transport and state replication
- [ ] Distributed BlackBox E2E-encrypted messaging
- [ ] Secure authenticator and wallet proof interface
- [ ] Wallet app and independent authenticator app prototypes
- [ ] Governance and upgrade mechanism
- [ ] Testnet benchmarking: speed, cost, bandwidth, fault tolerance

## Phase 5 — Independent evaluation (NOT STARTED)
- [ ] External cryptographic/consensus audit and remediation
- [ ] Abuse/spam/censorship/privacy review
- [ ] Economic sustainability and actual end-user fees
- [ ] Financial, consumer and IP legal review
- [ ] Public whitepaper backed by evidence

## Phase 6 — Release decision (NOT STARTED)
- [ ] Review all open risks, licence, reserve and custody policy
- [ ] Decide when or whether to publicise and issue TONG
- [ ] Production roll-out only if legal, security and economic gates are satisfied

**Development rule:** keep test money and experimental simulations separate from real user assets until all release gates pass.

## Research-gated TongNet Quorum Fabric roadmap — 2026-10-25

- [ ] Prove BFT epoch reconfiguration, automated Sybil eligibility and quorum intersection incl. 60/40 partitions and standby activation.
- [ ] Implement deterministic signed operation/health evidence and interval-union Network Delay Calculator in simulator.
- [ ] Prove exact-once adjusted deadline, no conflicting receiver/sender/refund/reserve rights and finite Protected Suspense exit.
- [ ] Validate reproducible 3h/24h/72h tests, optional irreversible disaster recovery and DEAD wallet conditions.
- [ ] Benchmark healthy/Byzantine regional latency, throughput, storage, committee scale and full sustained cost-per-transaction.
- [ ] Design sponsor quota + transparent microfee/anti-spam economics; no unconditional universal zero-cost claim.
- [ ] Review forced network-reserve confiscation and consumer rights, legal AUSTRAC/ASIC classification, licence/IP novelty, NIST crypto-agility.
- [ ] Complete independent consensus, wallet, economic and security audits before any real-money mainnet.

## Primary language and repository implementation sequence (2026-10-25)

- [x] Choose primary implementation language: **Rust**, selected at owner's request (architecture only).
- [ ] Set up version-pinned Rust Cargo workspace: `tongnet-types`, `tongnet-crypto`, `tongnet-state`, `tongnet-consensus`, `tongnet-network`, `tongnet-validator`, `tongnet-delay`, `tongnet-wallet-core`, `tongnet-node`, `tongnet-sim`; select actual audited dependency interfaces later.
- [ ] Implement strongly typed canonical transaction/state-machine invariants and simulator before multi-node network; no invented consensus cryptography.
- [ ] Add versioned mobile/desktop bindings and dedicated native UI only after audited shared core APIs exist.
- [ ] CI lint, format, unit/property/fuzz/integration tests, reproducible builds, software bill of materials, unsafe-code checks, external audit gates.

## New payment-product review checkpoint

- [x] Document competitive, consumer, merchant and bank-adoption critique in docs/TONGNET_PRODUCT_CRITIQUE_AND_ADOPTION_PLAN.md.
- [x] User REJECTED proposed Instant Pay; preserve existing mandatory Sender Send/BlackBox Trigger + Receiver BlackBox Claim secure P2P (specification only).
- [ ] Design verified receiver-issued one-time signed Receive Request and get owner decision on mandatory versus optional.
- [ ] Test fast two-sided online handshake, wrong-destination warnings, transfer finality, BlackBox claim delivery and race/expiry conditions.
- [ ] Assess supply, sponsorship, merchant testing and applicable banking/VASP regulation before issuing tokens or onboarding users.

## 2026-10-25 — Confirmed Sender-originated two-key payment claim flow

- [x] Record user correction: BOTH K_R and K_S originate in SENDER BlackBox, NOT Receiver BlackBox; Sender privately shares K_R and only designated receiver wallet + code can claim.
- [x] Record exact chronology: K_R generated at transaction setup but valid only after final Trigger during 24h; then expires; NEW K_S created in Sender BlackBox for following 72h only; eligible network delay extends adjusted cutoffs.
- [ ] Resolve Q6 disaster source-DEAD / inaccessible Sender BlackBox conflict with literal late K_S generation. Do NOT assume an early key without explicit user approval.
- [ ] Implement/verify code commitment, expiry, transaction/receiver binding, brute-force resistance, safe manual sharing, no key leakage to validators/receiver BlackBox, and no conflicting claims.
- [ ] Test wrong-address A/B scenario: A receives code but not bound wallet signing authority; B owns wallet but lacks code; recovery only after receiver window, NOT automatic refund at 24h.

## 2026-10-25 — Sender must final-ACCEPT Receiver Claim Request

- [x] Record latest owner confirmation: Receiver K_R + bound-wallet authority only raises CLAIM_REQUEST; mandatory independently signed Sender BlackBox ACCEPT before settlement; no ACCEPT until adjusted Receiver expiry means claim expires with no payout, then sender 72h recover eligibility.
- [ ] Formally specify separate 3h Trigger and late manual ACCEPT, protect under adjusted 24h and 72h windows; owner approval needed if later combining them.
- [ ] Prove atomic request+accept settlement before deadline; no replay/claim double-spend, fraudulent Sender Accept impersonation, false address display, malicious metadata, and bounded DoS.
- [ ] Build encrypted authenticated Claim Request delivery to Sender BlackBox, offline queue, clear safe confirmation, no public plaintext receiver code; test compromised Sender/Receiver, wrong destination A/B, auto-expiry and dynamic network delay.
