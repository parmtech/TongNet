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

**Q7 (NEXT):** If 300 TONG are locked in the **initial 3-hour PENDING_TRIGGER (not Triggered yet)** when Run Disaster Recovery kills the source Wallet, should the compulsory 3h no-trigger auto-refund be paid directly to the immutable pre-bound recovery wallet when due, or must disaster recovery wait for pre-trigger locks to resolve? **Undecided.**

## Question discovery and tracking

- [x] Started [86-question deep technical/security/logic backlog](docs/DEEP_QUESTIONS.md) on GitHub (2026-10-24).
- [ ] Work through high-risk questions in order; keep recording decisions and updating next-session handoff.

## Current disaster recovery work
- [x] Create dedicated Disaster Recovery Wallet specification and record three key categories.
- [x] User confirmed one-time Disaster Recovery Key is issued when destination is set, cannot ever be changed or reissued, and must be supplied with Wallet Private Key to execute.
- [x] User confirmed recovery destination cannot ever be changed once set; lost disaster key means that route is unavailable; standard transfers are still possible if the other two keys survive.
- [x] Q5 resolved — Wallet Private Key + TongNet Authenticator on first/only destination enrollment.
- [x] **Q6 (2026-10-24):** While Triggered funds stay escrowed for receiver's 24h claim, immediately rescue only spendable funds; if unclaimed receiver, owner with original one-use Sender Claim Key may claim to the linked Recovery Wallet within next 72h after source disaster recovery (design rule only).
- [ ] **Q7:** Resolve initial untriggered 3h refund routing after DEAD source.
- [x] Define Triggered escrow and stored sender claim key delegation after terminal disaster recovery (design only).
- [ ] Resolve refund routing for a transaction still in PENDING_TRIGGER at time source becomes DEAD, and implement atomic proofs.

## Outstanding safety requirements after Q6

- The original sender Claim Key must already be available to user; Disaster Recovery Key never substitutes for it.
- Pre-registered wallet destination binding is a cryptographic delegation, not proof that wallets belong to same real-life person.
- Sender/receiver/reserve race and already Triggered escrow survival still require network-level consensus and test evidence.
- Initial 3-hour non-triggered refund situation is NEXT Q7.

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
