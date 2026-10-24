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
- [x] **Q3 (2026-10-24):** Record optional TongNet Disaster Recovery Wallet with wallet-key-only disaster transfer to preconfigured address and permanent original wallet DEAD state (documentation only).
- [ ] **Q4:** Define authorization for adding/changing disaster recovery address.
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

**Q3:** If an already ACTIVE wallet loses the Authenticator Master Key (or the Authenticator device), but the owner still has the wallet private key, should there be any independent secure recovery route to restore access to BlackBox, or should this access remain permanently locked? Await user answer.

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
