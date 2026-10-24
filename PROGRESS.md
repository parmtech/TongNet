# TongNet — Progress Tracker

> **LATEST 2026-10-25 OWNER OVERRIDE — ACTIVE Recovery Target (V4):** An accepted S→R recovery pairing does **NOT** freeze, reclassify, or disable R's ordinary wallet. Both S and R remain `NORMAL_ACTIVE` with separate wallets, balances, transfers, BlackBoxes and signing keys. R can independently set its OWN further recovery C even while it carries a **separate sealed parent S BlackBox archive**. ONLY S's encrypted BlackBox records are mirrored, never S's blockchain transaction history/balance. S archive is not readable before authenticated BFT-final `RUN_DISASTER_RECOVERY(S,R)`, which makes S `DEAD`, transfers only S eligible unlocked funds once into ALREADY-ACTIVE R and authorises unlocking S archive with permanent original S provenance. R's own records are unaffected. Prior FREEZE and blocked financial operation rules are superseded; original fresh-at-first-binding eligibility remains until changed. But separate archive lock versus normal R wallet functions must be enforced. Key-release decryption cannot be honestly promised without a reviewed conditional cryptographic scheme; S claim K_S late creation and R dying earlier through R→C recovery are OPEN. See [Latest Active Recovery Mirror V4](docs/ACTIVE_RECOVERY_MIRROR_V4.md).


> **MOST RECENT PRODUCT DECISIONS — 2026-10-25:** Trusted bilateral P2P with no third-party deal arbiter; Receiver 24h followed by Sender **60 DAYS**, replacing earlier 72h; after that creator proposes network-reserve forfeiture but **real-money deployment legally/safety BLOCKED**. Special Recovery Wallet must start a new unused address, accept only recovery pairing metadata while RECOVERY_RESERVED, block ordinary incoming/outgoing transactions, and only upon Disaster Recovery succeed old S as ACTIVE while S becomes DEAD. Recovering BlackBox carbon-copy **requires pre-existing authenticated encrypted backup**; old blockchain history remains immutable and is verifiably linked, not copied to rewrite the ledger. Local restore on new device with surviving keys is distinct from disaster transition. Website cannot receive plaintext Wallet Private Key and Authenticator Master Key. Late K_S creation after loss/DEAD still unresolved. Canonical spec: docs/SECURE_P2P_V3_RECOVERY_DECISIONS.md.


> **LATEST OWNER REQUIREMENTS — 2026-10-25:** Trusted two-party P2P with no deal arbitrator; validators verify signatures/finality, not buyer/seller disputes. The RECEIVER has the first 24h (clock at final LOCK proposed, not yet ratified). The SENDER then has **60 DAYS**, replacing earlier 72h, to manually reclaim; after that, creator wants remaining unclaimed escrow sent to Network Reserve (OWNER INTENT, **REAL-MONEY DEPLOYMENT BLOCKED** by unresolved legal/consumer protection safety). A special *fresh*, zero-prior-financial-transactions RECOVERY_RESERVED address may complete recovery pairing metadata but CANNOT ordinarily send/receive before one-time disaster-recovery settlement. After successful recovery, S becomes DEAD and R is successor NORMAL_ACTIVE; owner wants historical receipts, BlackBox encrypted backup and pending entitlements shown in R, not destructive rewriting of immutable ledger. Preexisting recoverable encrypted BlackBox backup is REQUIRED to restore lost device data; a lost unbacked secret cannot be resurrected, and wallet/master root secrets must never be sent to a website server. Late sender claim key K_S with LOST/DEAD BlackBox, pending consent migration, exact 24h anchor, and legal forfeiture remain OPEN. See [canonical 2026-10-25 decisions](docs/SECURE_P2P_V3_RECOVERY_DECISIONS.md). Older Trigger/72h/recovery-descriptions are HISTORICAL.


> **CURRENT RULE — 2026-10-25 (SUPERSEDES ALL OLD 3h TRIGGER CONTENT):** User REMOVED separate three-hour Trigger and its 3h automatic refund. Current TongNet Secure Manual P2P: Sender network-final LOCK -> Sender BlackBox makes and privately shares one-time Receiver Claim Code K_R -> exact addressed receiver wallet signs Claim Request -> Sender BlackBox must manually FINAL_ACCEPT exact transaction/recipient/amount -> BFT may finalise receiver settlement. No FINAL_ACCEPT means no receiver payout. No separate Trigger remains. Receiver 24h then Sender's following 72h manually redeemable via fresh Sender BlackBox K_S (verified attributable network delay extensions still apply); 24h from BFT-final LOCK is recommended but not explicitly ratified. No valid absolute guarantee against mistaken approval, stolen signing authority or third-party fraud. Old 3h Q7 disaster refund is obsolete; source DEAD + late K_S needs safe redesigned handling. See [canonical Secure P2P v2](docs/SECURE_P2P_V2.md) (for docs/ files: [canonical v2](SECURE_P2P_V2.md)).


**Updated:** 2026-10-24  
**Stage:** 0 / requirements and documentation  
**Overall:** Research/planning, not implementation  
**Repo:** `manbir6-ux/TongNet` (private, default branch `main`)

## Actually completed
- [x] Repository existence and edit permissions checked through connected GitHub account.
- [x] Existing placeholder README reviewed.
- [x] Canonical project branding and attribution documented.
- [x] Creator-stated 2015 concept origin and 2026 disclosure documented with evidence caveat.
- [x] Historical conversation FAQ, rules and major security risks recorded.
- [x] 3-hour noncancellable pre-trigger rule documented.
- [x] Receiver 24-hour and sender additional 72-hour windows documented.
- [x] Proposed permanent network reserve rule flagged for legal/security resolution.
- [x] Technical, roadmap, decision, changelog and future-session documents initialised.

## Still NOT done
- [x] Resolve Question 1: **Option B — no sender cancellation after Trigger, even for wrong recipient address** (2026-10-24).
- [x] **Q2 (2026-10-24):** Wallet never enrolled within 72h is permanently DEAD, with NO future reactivation or initial setup key regeneration.
- [x] **Q3 (2026-10-24):** Record optional TongNet Disaster Recovery Wallet; recovery execution requires Wallet Private Key **plus** one-use Disaster Recovery Key (no BlackBox/Authenticator), sweeping eligible funds to fixed destination and permanently DEAD source wallet (documentation only).
- [x] **Q4:** Confirm third optional Disaster Recovery Key's one-time execution role, irrevocably immutable address/key and lost-key handling (documentation only).
- [x] **Q5 (2026-10-24, Option A):** Initial recovery address registration requires **Wallet Private Key AND TongNet Authenticator**; immutable thereafter (design decision, not implementation).
- [ ] Answer remaining key loss, theft, recovery and consent questions (one at a time).
- [ ] Complete prior-art search.
- [ ] Prove a decentralised consensus and finality algorithm.
- [ ] Define TONG economics and whether it is asset-backed.
- [ ] Resolve legal treatment of unclaimed funds and payments.
- [ ] Implement any production code, simulations, mainnet or wallets.
- [ ] Execute tests, threat assessment, audits or live transaction benchmarks.

## Documentation note

Q2 updates to the security threat-model file have **not** yet been committed because the write was blocked. Other Q2 documentation has been updated; do not mark the security-file sync complete.

## Current next question

**LATEST 2026-10-25:** User confirmed Q16 C HYBRID per-operation/global delay, Q17 C independent validation, Q18 C evidence consensus/Protected Mode, Q19 C anti-Sybil committees, Q20 C hybrid decentralisation evolution, Q21 C automated validator governance, Q22 B quarantine/review, Q23 B backup validators, Q24 C quorum for partitions and Q25 B precommitted safe rotation. The 95 question backlog now has candidate answers in MASTER_QA_RECOMMENDATIONS.md, but no working blockchain/consensus implementation or audit exists. NEXT: formal safety model and prototype engineering gates, not re-asking Q16.

## Question discovery and tracking

- [x] Started [86-question deep technical/security/logic backlog](docs/DEEP_QUESTIONS.md) on GitHub (2026-10-24).
- [ ] Work through high-risk questions in order; keep recording decisions and updating next-session handoff.

## Current disaster recovery work
- [x] Location of one-time recovery secret clarified: recipient/recovery wallet encrypted BlackBox; not the main/source Wallet or public network.
- [ ] Prove integrity of source→destination binding, one-use verification, and encrypted destination-only delivery.
- [ ] Decide whether destination owner must accept registration before immutable binding is FINAL (Q9).
- [x] Create dedicated Disaster Recovery Wallet specification and record three key categories.
- [x] User confirmed one-time Disaster Recovery Key is issued when destination is set, cannot ever be changed or reissued, and must be supplied with Wallet Private Key to execute.
- [x] User confirmed recovery destination cannot ever be changed once set; lost disaster key means that route is unavailable; standard transfers are still possible if the other two keys survive.
- [x] Q5 resolved — Wallet Private Key + TongNet Authenticator on first/only destination enrollment.
- [x] **Q6 (2026-10-24):** While Triggered funds stay escrowed for receiver's 24h claim, immediately rescue only spendable funds; if unclaimed receiver, owner with original one-use Sender Claim Key may claim to the linked Recovery Wallet within next 72h after source disaster recovery (design rule only).
- [x] **Q7 (2026-10-24, Option A):** If an untriggered transfer survives a terminal source disaster recovery, preserve original 3h lock, then automatic refund directly to prebound recovery wallet after timeout (no early cancellation).
- [x] **Q8 clarification (2026-10-24):** The third one-use Disaster Recovery Key is GENERATED in the DESTINATION Recovery Wallet's own BlackBox, not source Wallet, and later consumed with source Wallet Private Key (specification only).
- [x] **Q9:** Destination BlackBox must Accept request before immutable pairing and key generation. Reject notifies source BlackBox; pending counts NOT_CONFIGURED (documentation only).
- [x] **Q10 (2026-10-24, Option A):** Unanswered pairing request automatically expires after 24 hours, without recovery Key/link. Pending/Expired means NOT_CONFIGURED; stale Accept invalid.
- [x] **Q11 (2026-10-24, Option B):** Source cannot cancel, withdraw or replace a PENDING pairing request, must wait for R REJECT or 24-hour EXPIRED before retrying (design rule only).
- [x] **Q12 (2026-10-24, Option A):** Accepted disaster pairing MUST be network-final BEFORE 24h cutoff; a late-finalized Accept is EXPIRED, regardless of earlier signing/submission.
- [x] **Q13 direction (2026-10-24):** user wants immutable rate of running timers regardless of slow/fast network, queue new tasks under congestion, and start NEW transaction timers only at network acceptance; implementation recommendation: define acceptance as consensus finality. Full outage claim-loss details still open.
- [x] **Q14 (2026-10-24 Option A):** both receiver 24h and subsequent sender 72h claims require network finality strictly BEFORE expiry; queued/signature/relay proof alone does not qualify. Late-finalized claim is EXPIRED (design only).
- [x] **Q15 (2026-10-25):** user broadened 1:1 compensation to ALL time-sensitive tasks delayed by network. Effective deadline gains exactly verifiable network delay, while clocks maintain normal cadence. Q12/Q14 require consensus finality strictly before adjusted deadline, not an early queue ticket (design only).
- [x] **Q16:** user chose HYBRID per-operation and global Delay Calculator input; implementation proof/anti-manipulation remains open.
- [x] **Q17–Q25:** user-confirmed network delay verification, protected state, decentralised validator automation/quarantine/backup/partition rules (specification only).
- [x] **95 questions:** reviewed all with candidate engineering answers; NOT all user-ratified; see docs/MASTER_QA_RECOMMENDATIONS.md.
- [x] **Architecture review:** versioned long-term design proposal in docs/TONGNET_FUTURE_ARCHITECTURE.md.
- [ ] Formal protocol specification/proofs, BFT integration, Sybil eligibility/clock rules, code, testnets and audits.
- [x] Define Triggered escrow and stored sender claim key delegation after terminal disaster recovery (design only).
- [x] Specify refund destination for PENDING_TRIGGER when source DEAD (Q7 design only).
- [ ] Implement/test strict Trigger-vs-DEAD-vs-timeout ordering and no double settlement.

## Outstanding safety requirements after Q6

- The original sender Claim Key must already be available to user; Disaster Recovery Key never substitutes for it.
- Pre-registered wallet destination binding is a cryptographic delegation, not proof that wallets belong to same real-life person.
- Sender/receiver/reserve race and already Triggered escrow survival still require network-level consensus and test evidence.
- Initial 3-hour untriggered expiry refund is resolved by Q7 Option A, pending formal implementation and testing.

## Important blockers
1. Consensus / Byzantine finality / Sybil security not designed.
2. Real-money forfeiture to TongNet Network Reserve cannot responsibly launch without clear owner consent and jurisdiction-specific review.
3. Wallet factor + TOTP alone may fail under phishing or compromised devices; secure challenge signing and independent key separation need research.
4. Real TONG value, reserve obligations and network fee budget unspecified.

## How to keep progress meaningful
- After **each** answer, update DECISIONS, FAQ, PROTOCOL (if needed), NEXT_SESSION, PROGRESS and CHANGELOG; commit.
- Describe each item as `planned`, `proposed`, `implemented`, `tested`, or `audited` with evidence.
- Never mark checkboxes done merely because they appear in documentation.
- Include actual links to code commits and tests once those exist.

## Q9 request status confirmation (2026-10-24)

- [x] Capture user-confirmed PENDING, ACCEPTED, REJECTED flow in GitHub specification.
- [x] Record no key and no permanent association until DESTINATION BlackBox ACCEPT.
- [x] Record REJECT response to source BlackBox.
- [ ] Implement and verify authenticated Accept/Reject, atomic key issuance, race and replay safety.
- [x] Q10 settled: maximum 24h unanswered PENDING; expiry keeps wallet NOT_CONFIGURED (documentation only).
- [x] Q11 resolved — no source cancellation or replacement while PENDING.
- [x] Q12 rule decided: finality timestamp strictly before 24h deadline for acceptance; no grace period (documentation only).
- [ ] Specify consensus clock, stable ordering and race tests; technical proof still outstanding.
- [x] Record Q13 queue/timer approach and distinguish admission from acceptance (documentation only).
- [x] Q14 strict claim-finality boundary chosen; no pre-deadline queue priority override.
- [x] Q15 user intent: affected deadlines grow by verified network delay; reserve transfer cannot preempt properly adjusted rights.
- [x] Q16 input model chosen: HYBRID; exact delay algorithm, full network outage, duplicate credits, anti-Sybil clock proofs and consensus IMPLEMENTATION remain unsolved.
- [ ] Real-money Network Reserve forfeiture remains a consumer-protection/legal launch blocker.

## Documentation sync note

Q11 is committed in Decisions, FAQ, Protocol, Disaster Recovery, Security, Deep Questions, Roadmap, Next Session, README and Progress. Updating the historical CHANGELOG file was blocked; the Q11 record remains preserved in the canonical Decision Register and other files. The changelog entry can be reconciled in a later edit.

## 2026-10-25 Master architecture checkpoint

[Review of all 95 DQ questions](docs/MASTER_QA_RECOMMENDATIONS.md) and [TongNet Future Architecture](docs/TONGNET_FUTURE_ARCHITECTURE.md) have been saved. Evidence-based research references include CometBFT, high-throughput DAG literature, NIST PQC and Australian AUSTRAC/ASIC obligations. Claims of being faster, cryptographically sound, fully decentralised, strictly fee-free or novel are UNSUBSTANTIATED until measured/reviewed. Forced Network Reserve forfeiture remains a consumer/legal hard launch blocker; no mainnet or end-user fund custody is authorised.

## 2026-10-25 Primary implementation language choice

Owner delegated language choice. Rust selected for security-critical TongNet core, networking, BFT state machine, delays and wallets; Kotlin/Swift or UI technology may wrap the same shared Rust library on supported clients. This is design only: no Cargo workspace, code build, tests, benchmarks or deployed protocol resulted. See README and docs/TONGNET_FUTURE_ARCHITECTURE.md.

## 2026-10-25 Product-market fit and critical trust review

Created [Critical TongNet Product/Banking Adoption and Red-team Plan](docs/TONGNET_PRODUCT_CRITIQUE_AND_ADOPTION_PLAN.md). Key finding: original 3h+Trigger+24h Claim is unsuitable as universal merchant payment checkout. **Proposed but NOT user-confirmed:** new Instant Pay mode in parallel with untouched user-confirmed Protected Pay; stable-value asset rails only with regulation; business invoices/receipts and customer-friendly key recovery where product rules allow. Coin amount `1,000,000,000 TONG` (9 decimals) is illustrative, NOT set. No real TONG minted, banks connected, merchant integration proven, code deployed, or BFT benchmark measured. Incumbent fast/cheap payment systems already exist; TongNet differentiator is only hypothesis. Token reserve/forced forfeiture still launch blocker.

## 2026-10-25 — CONFIRMED product correction: manual two-party P2P, NOT Instant Pay

**User instruction (clear and later than the instant-pay suggestion):** "Instant wale bahut system ne asi ehnu p2p secure system bna the aa not instant but ek fast manual treeka jithe receiver te sender dona nu kujh krna pve." TongNet is intentionally a **fast, manual, two-party-authorised secure P2P payment protocol**, not an instant-payment default/competing checkout coin. Previous assistant proposal to introduce/enable `Instant Pay` or make it the default is **SUPERSEDED AND NOT AUTHORISED**; do not implement it under current scope.

**Keep user-confirmed Protected P2P sequence:** sender initiates Send and network-final escrow lock; sender personally approves Trigger using independent BlackBox/authentication; addressed receiver personally Claims using its own BlackBox one-use Claim Key. Both parties act before final recipient settlement. No waiting requirement: if both are available they may complete the independent authorisations right away, subject to actual consensus latency. Original **maximum 3h before Trigger, receiver up to 24h to Claim, then sender-only next 72h** remain, with eligible Q15–Q18 one-for-one verified network delay extensions. Before Trigger auto-refund on adjusted 3h no-trigger expiry; after Trigger no sender cancellation, even wrong address; Claim strict finality before adjusted receiver deadline. Never promise seconds to finality without measurements.

**Wrong-address protection to investigate, NOT yet chosen by user:** propose a receiver-created, independently signed **one-use Receive Request (public payment invitation, not a private wallet key and NOT the Claim Key)** bound to destination wallet public key, unique request ID, optional amount and expiry. Sender must verify cryptographic binding, show full recipient fingerprint/details and manually approve exact operation; Trigger still separately signed; only receiver's BlackBox gets the separate confidential Claim Key on Trigger. A malicious party can still sign a legitimate request under the wrong identity and socially engineer approval; signatures prove key control, not real-world recipient identity. Whether a signed Receive Request is mandatory for all Send operations or optional (with warnings on manually-entered addresses) is NOT YET ratified.

**Adoption focus revised:** secure interpersonal escrow-like peer-to-peer exchanges, explicit bilateral authorisation and robust wrong-recipient defenses rather than frictionless cashier checkout or banking-rail competition. Banking/merchant modules are future research, not a change to product's chosen security-first operation. Existing 20-question market critique is historically valuable, but its recommendation for `Instant Pay` is explicitly rejected for present scope. `docs/TONGNET_PRODUCT_CRITIQUE_AND_ADOPTION_PLAN.md` must be read together with this newer decision.

**Status:** approved product direction and P2P requirement documented; one-use Receive Request proposal requires separate choice; no implementation/testing.

## 2026-10-25 — NEWER USER-CONFIRMED RULE: Both payment Claim Keys originate in the SENDER BlackBox

**This rule explicitly SUPERSEDES older language that delivered/generated receiver Claim Key inside Receiver BlackBox or automatically delivered the key to R. It does NOT change the unrelated Disaster Recovery Key, which remains generated inside the Recovery DESTINATION's own BlackBox only on accepted recovery pairing.**

**Confirmed operation:** At transaction initiation, source Sender BlackBox generates/displays the unique **Receiver Claim Code K_R**, tied to exactly (TongNet chain, transaction ID, selected receiver address/public key, amount/asset, operation, expiry). Sender explicitly gives K_R to intended receiver by a private/out-of-band channel. The selected on-chain RECEIVER address, **not merely the person holding the code**, must independently authenticate and prove control of its wallet to claim. Sending/witnessing a code never credits funds by itself. Preserve existing separately authenticated sender BlackBox Trigger: after a successful network-final Send lock and final Trigger within the 3h window, K_R becomes exercisable for the receiver's **24h nominal** window, with Q15 verified eligible network delay adjustment. Generating K_R at Send is NOT payment settlement and its validity clock still begins on final Trigger. If no final Trigger, auto-refund after adjusted pre-trigger expiry; no receiver payout. Receiver need not create the code and network must NOT automatically supply plaintext K_R to whichever destination address Sender typed. Sender must deliver it to intended receiver.

**Next window:** At the end of receiver's adjusted 24h exclusive priority, the receiver entitlement becomes EXPIRED and **a fresh, transaction-specific Sender Reclaim Key K_S is generated in the SENDER's BlackBox**, accessible to/usable only by authenticated original Sender, never by Receiver. K_S is only valid in the following nominal **72h** (extended solely for eligible verified network delay). Sender must manually reclaim using valid K_S **plus original sender authority**, or after previously completed Disaster Recovery, the already confirmed immutable linked Recovery Wallet path IF its necessary original-claim-proof rules can be satisfied. K_S expires strictly at its adjusted expiry. No automatic full refund after 24h Triggered receiver nonclaim: rather funds become sender-claimable for next 72h. Existing user-proposed network-reserve allocation after total post-Trigger 24+72h remains legally/ethically blocked for real-money rollout.

**Wrong address failure analysis:** Sender intended wallet A, but transaction cryptographically binds to mistyped wallet B. If Sender sends K_R to A, A cannot redeem because A lacks B's wallet authority; B cannot redeem without K_R. After receiver window expires, original Sender can use K_S in the next 72h to reclaim. If B obtains K_R (through code theft, intentional sharing or phishing), B can claim before expiry. No system can guarantee refunds if both credentials satisfy the wrong recipient transaction.

**PROTOCOL ENGINEERING OPEN / conflict with earlier Q6:** Previous specification said the Sender Claim Key already existed before 24h and could be used even after Source S became DEAD by Disaster Recovery. Newly confirmed **late key generation in Sender BlackBox** conflicts with successful prior disaster recovery or lost/compromised Sender BlackBox before the 24h boundary. Do NOT silently replace the user's "new key after 24h" timing. Candidate solutions needing confirmation and formal verification include (A) Sender BlackBox generates fresh K_S after expiry while online and cannot reclaim if destroyed, OR (B) precommit an authenticated, encrypted, future sender key/derivation at Trigger, only cryptographically UNSEAL/ACTIVATE it once receiver window expires, including recovery-wallet handling. B preserves prior Q6 protection better but changes the literal issuance time. Network must not mint plaintext K_S or know secret by itself. Also prove secure commitment update at boundary, no claim if key issuance commitment missing, anti-replay, receipt binding and no permanent frozen funds.

**Naming:** Ordinary transaction keys K_R and K_S are NOT Wallet Private Keys, Authenticator/BlackBox master secrets, disaster-recovery keys, or a receiver-generated Receive Request. An extra signed Receive Request may still be a future optional defense but is NOT required/approved by this correction; do not assume mandatory upfront receiver request. The new flow is user-confirmed requirement only—not an implementation, audited code or measured performance.

## 2026-10-25 — Two-party BlackBox final consent rule recorded

Sender privately shares transaction-bound K_R via external communication. Receiver signs/submits Claim Request; Sender BlackBox shows exact address+amount and requires manual ACCEPT. Even possession of K_R + correct receiver wallet is insufficient to finalize. No accept by adjusted 24h -> receiver expiry, sender's following 72h manual key reclaim, NOT automatic refund. No manual Reject needed. Previous confirmed 3h Trigger preserved as an additional action until expressly revised; formal race/security proofs and implementation not yet done. See docs/DECISIONS.md and docs/PROTOCOL.md.

## 2026-10-25 — auto-unbind recovery destination on consensus-final DEAD (owner confirmed)

The recovery destination R must be ACTIVE. Pairing source S→R is fixed while R ACTIVE, but if R becomes finally DEAD for ANY cause, consensus automatically revokes active S→R recovery entitlement while preserving audit history. S stays ACTIVE but immediately has **NO RECOVERY**, so S may enroll a fresh eligible ACTIVE R2 with R2 BlackBox approval. No automatic fallback through R's own recovery wallet (S→R, R→C does NOT mean S→C when R dies). No ordinary offline status can cause unbinding; chain-final DEAD required. Enforce atomic reverse-index updates, ACTIVE checks at recovery-execution finality, deterministic races, no double transfers or sealed-parent BlackBox disclosure to R's successor. User must be visibly warned that original S loses protection until new pairing succeeds; if S keys are already missing, A→new-R may be impossible. Retention/cryptographic shredding of old mirrored ciphertext remains research. Latest [Active Recovery Mirror V4](docs/ACTIVE_RECOVERY_MIRROR_V4.md). Product decision only, no code/security proof.
