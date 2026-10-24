# TongNet — A-to-Z Research and Development Roadmap

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
