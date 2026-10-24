# TongNet — A-to-Z Research and Development Roadmap

> **LATEST OWNER PRODUCT SCOPE — Single native TONG coin, Bitcoin-like chain (2026-10-25):** TongNet is a dedicated independent cryptocurrency/blockchain for its own native **TONG** coin and its built-in secure bilateral BlackBox P2P/recovery protocol. Owner expressly REJECTED assistant-proposed Ethereum-like general-purpose application platform: **no public arbitrary smart contracts/EVM, no user-created tokens, no dApp ecosystems or app marketplace**. Wallet, BlackBox, Authenticator, explorer and node tools are first-party network clients, not a general-purpose dApp platform. Aspirations: improved practical user security and faster secure settlement compared with aspects of Bitcoin, **not an unproven claim of being mathematically more secure than Bitcoin**. Bitcoin-like use case does NOT automatically mandate Bitcoin Proof-of-Work mining: PoW vs hybrid BFT (and issuance/monetary policy) remain explicitly UNDECIDED. UTXO is a proposed accounting baseline, not approved. Latest [scope specification](docs/TONGNET_BITCOIN_LIKE_SCOPE.md); prior general-purpose/token platform proposals are historical/unapproved.


> **LATEST 2026-10-25 OWNER OVERRIDE — ACTIVE Recovery Target (V4):** An accepted S→R recovery pairing does **NOT** freeze, reclassify, or disable R's ordinary wallet. Both S and R remain `NORMAL_ACTIVE` with separate wallets, balances, transfers, BlackBoxes and signing keys. R can independently set its OWN further recovery C even while it carries a **separate sealed parent S BlackBox archive**. ONLY S's encrypted BlackBox records are mirrored, never S's blockchain transaction history/balance. S archive is not readable before authenticated BFT-final `RUN_DISASTER_RECOVERY(S,R)`, which makes S `DEAD`, transfers only S eligible unlocked funds once into ALREADY-ACTIVE R and authorises unlocking S archive with permanent original S provenance. R's own records are unaffected. Prior FREEZE and blocked financial operation rules are superseded; original fresh-at-first-binding eligibility remains until changed. But separate archive lock versus normal R wallet functions must be enforced. Key-release decryption cannot be honestly promised without a reviewed conditional cryptographic scheme; S claim K_S late creation and R dying earlier through R→C recovery are OPEN. See [Latest Active Recovery Mirror V4](docs/ACTIVE_RECOVERY_MIRROR_V4.md).


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

## 2026-10-25 owner decision — live encrypted Recovery Mirror
After immutable S→R pairing is ACCEPTED, S's BlackBox records, pending claim metadata, receipts and wallet history must be **continuously encrypted and synchronized to R's RECOVERY_RESERVED mirror**. S remains solely NORMAL_ACTIVE and owns spendable balance; R must have NO ordinary receive/send/claim/spend permission before one-time FINAL `RUN_DISASTER_RECOVERY`. Mirror is data + successor rights, NOT a second ledger balance or unilateral signing backdoor. After valid one-time disaster activation, S is permanently DEAD, R becomes only NORMAL_ACTIVE successor; pending escrow rights and history remain verifiably linked, and only eligible unlocked balance actually moves. Backups must exist and be verifiable *before device loss*; offline or unsynced secrets cannot be recovered magically. Ciphertext encrypted with a key held by R might still be decrypted early offline, so pre-activation READ confidentiality is a separate UNSOLVED key-release problem: cryptographic protocol can prevent preactivation SPENDING but cannot make decryption secrets unknowable after already given away. Sender post-24h new K_S with destroyed S BlackBox remains unresolved; 24h receiver then 60 full days sender reclamation is current rule (older 72h superseded). See [Recovery Mirror Protocol](docs/RECOVERY_MIRROR_PROTOCOL.md) (repo root: docs/RECOVERY_MIRROR_PROTOCOL.md). This is a user-confirmed product direction, NOT built or audited.

## 2026-10-25 — OWNER-CONFIRMED: Recovery successor can later register ITS OWN future recovery

**Latest exact lifecycle, replacing any interpretation that a Recovery Address is permanently recovery-only:**

1. While main wallet S is `NORMAL_ACTIVE`, its pre-accepted designated R stays `RECOVERY_RESERVED`. R is **exclusively a future successor**: no ordinary SEND / RECEIVE / CLAIM, no second recovery wallet associated *to R*, no `RUN_DISASTER_RECOVERY` initiated *from R*, no funds spending, nor any alternate activation. R can ACCEPT pairing protocol metadata, host continuously synchronized encrypted BlackBox mirror backups, and receive authenticated status/checkpoint events, but these are **not normal financial transactions**. The original S may have one immutable active S→R relationship as already confirmed.
2. `RUN_DISASTER_RECOVERY(S,R)` with the previously confirmed original S Wallet Private Key + one-time Recovery Key from R BlackBox, and previously accepted immutable binding, must have BFT finality and atomic state update: S `DEAD` (forever), R `NORMAL_ACTIVE` (ordinary financial controls restored) and exactly-once transfer of **only eligible unlocked S funds**. All pending locked escrow obligations and rights survive as successor-authorised entitlements without double spend or arbitrary retroactive finalisation; BlackBox mirror copy is unlocked/restored according to separately audited encryption/backups, and historic S transactions remain unchanged on ledger but linked to R for view/proofs.
3. **Only AFTER R is `NORMAL_ACTIVE` may it optionally request and pair a BRAND-NEW, NEVER-FINANCIALLY-USED successor address C as `RECOVERY_RESERVED`** using the normal recovery association protocol (R Wallet Private Key + R's separate Authenticator, C BlackBox explicit ACCEPT, no key/link before Accept). The old S→R permanently consumed/successful recovery record stays immutable. R may now spend/send/receive like any main Wallet, and C remains unusable for ordinary actions until `RUN_DISASTER_RECOVERY(R,C)` makes R `DEAD`, C `NORMAL_ACTIVE`. This may recur (S→R→C→D...). A reserved R may **never** preconfigure C in advance of its own activation.
4. Never treat S/R as simultaneously ACTIVE or as cloned funds. The state machine must reject transitions, loops, recycled/used successor addresses, multiple reserved successor registrations that conflict, claims by R while reserved, old S signatures post-death, and chained recovery before predecessor is dead. Domain-separate every source+destination+epoch transition and consume one-use recovery secret atomically.
5. The term "same wallet" means a logically continuous user history and entitlement, **not identical private keys, not a shared live signing authority, not a ledger rewrite, nor a universal decryption backdoor**. Source S private key never becomes R's wallet private key.
6. What happens to original locked sends and late-created Sender K_S when S dies, plus strong pre-activation confidentiality of R's encrypted mirror, remain critical engineering OPEN. Never quietly claim those are solved by replication.

**Decision status:** 1-3 are explicit owner-confirmed UX/protocol direction. 4-6 are safety interpretation and unresolved engineering constraints. No running chain or audited cryptographic key migration exists.

## 2026-10-25 — LATEST: Recovery Mirror covers only Parent BlackBox, NEVER parent's transaction ledger

User clarified: a brand-new NORMAL wallet R is designated by main wallet S, R BlackBox ACCEPT BFT-finalises immutable recovery binding, R becomes `RECOVERY_RESERVED_FROZEN`. During S ACTIVE, R's BlackBox stores only S's continuously replicated **ENCRYPTED BlackBox contents** (claims, codes, requests, messages), with every record permanently tagged `Parent/Origin Wallet Address: S`, original event ID and other protected provenance. No R-specific ordinary financial operations, and no mirrored S plaintext readable/visible until authorized Disaster Recovery finality. **S's OLD blockchain transaction records must STAY on S forever, even once S is DEAD**: do NOT copy/transfer/reassign S historical transaction ownership or mutate immutable ledger entries. Authorized one-time recovery funds transfer of still-spendable balance is a distinct NEW ledger transaction, not transfer of historical entries. On recovery S DEAD, R NORMAL_ACTIVE and parent-tagged BlackBox archive readable, while R's fresh transactions belong to R. R may register fresh recovery C later.

No PRIVATE key, Authenticator Master Key, Claim Code, decryption key or recovery secret goes into public ledger, app telemetry, or server. If protocol uses an **ephemeral secret handshake**, generate locally, keep hidden even from owner, zeroize promptly; however absolute 'forever erased' guarantees depend on hardware and backups and cannot be assumed. **R's own signing key, protected one-use Disaster Recovery Key, and future restore/decryption capability cannot all be destroyed or recovery would be impossible.** Public/nonsecret verification commitments may still be essential for BFT and can reveal address relationships without privacy mechanisms. Enforced frozen spending and cryptographically enforced unreadability are separate problems; release of mirror decrypt material only after authorized recovery is OPEN and not claimed solved. Separate unresolved late K_S and 60-day sender reclaim/forfeiture safety unchanged. Details: [latest Recovery Mirror protocol](docs/RECOVERY_MIRROR_PROTOCOL.md).

## 2026-10-25 — auto-unbind recovery destination on consensus-final DEAD (owner confirmed)

The recovery destination R must be ACTIVE. Pairing source S→R is fixed while R ACTIVE, but if R becomes finally DEAD for ANY cause, consensus automatically revokes active S→R recovery entitlement while preserving audit history. S stays ACTIVE but immediately has **NO RECOVERY**, so S may enroll a fresh eligible ACTIVE R2 with R2 BlackBox approval. No automatic fallback through R's own recovery wallet (S→R, R→C does NOT mean S→C when R dies). No ordinary offline status can cause unbinding; chain-final DEAD required. Enforce atomic reverse-index updates, ACTIVE checks at recovery-execution finality, deterministic races, no double transfers or sealed-parent BlackBox disclosure to R's successor. User must be visibly warned that original S loses protection until new pairing succeeds; if S keys are already missing, A→new-R may be impossible. Retention/cryptographic shredding of old mirrored ciphertext remains research. Latest [Active Recovery Mirror V4](docs/ACTIVE_RECOVERY_MIRROR_V4.md). Product decision only, no code/security proof.
