# TongNet — Progress Tracker

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

**Q15 (NEXT):** During a TOTAL TongNet outage spanning an already-running Receiver/Sender claim deadline, after service is restored should the expired unpaid escrow go automatically to the proposed Network Reserve, or remain quarantined/preserved for a separate post-outage remedy? Q14 strict finality and the fixed countdown remain confirmed. Reserve forfeiture legal/consumer protection still blocked.

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
- [ ] **Q15:** settlement/disposition of funds whose claim windows expire during network-wide downtime.
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
- [ ] Q15 total network outage and proposed reserve forfeiture remain undecided and a launch blocker.

## Documentation sync note

Q11 is committed in Decisions, FAQ, Protocol, Disaster Recovery, Security, Deep Questions, Roadmap, Next Session, README and Progress. Updating the historical CHANGELOG file was blocked; the Q11 record remains preserved in the canonical Decision Register and other files. The changelog entry can be reconciled in a later edit.
