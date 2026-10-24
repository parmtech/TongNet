# TongNet — Next Session Handoff

**Read first:** [PROGRESS.md](PROGRESS.md) → [docs/DECISIONS.md](docs/DECISIONS.md) → [docs/FAQ.md](docs/FAQ.md) → [docs/PROTOCOL.md](docs/PROTOCOL.md).

## Deep questioning backlog

Read [docs/DEEP_QUESTIONS.md](docs/DEEP_QUESTIONS.md). There are **86 initial questions** across keys, disaster recovery, irreversible state, financial and legal edge cases, validators/consensus, zero-fee economics, privacy and operational resilience. User explicitly asks to continue posing as many deeper questions as needed, and to commit every resulting decision. **One question per turn** is still best for a reliable decision log, but keep adding questions to backlog as new risks are discovered.

## User communication preference
Speak simple, conversational **Punjabi**. Ask **exactly one product/security question at a time**. Wait for the user's answer. Record it accurately and commit the relevant docs before asking another question. Do not keep asking questions the user already settled.

## Current checked repo
- `manbir6-ux/TongNet`, private
- Owner/company **ParmTech**, original creator/developer **Manjinder Singh**
- Concept said by creator to originate **2015**, privately held through 2026
- Names: TongNet network; TONG coin; TongNet Wallet; TongNet BlackBox; TongNet Authenticator; TongNet Network Reserve.

## Key current flow
1. Sender sends → funds locked, no receiver claim code yet.
2. Sender MUST use independent authenticated BlackBox to Trigger; **NO pre-trigger manual cancellation**.
3. If no Trigger within **3 hours of Send**, automatic refund to sender.
4. After Trigger, receiver's BlackBox obtains recipient-address-bound code; receiver has **24 hours** to claim one time.
5. If no receiver claim, receiver credential expires; original sender has **additional 72 hours** to reclaim once.
6. Creator's proposed final rule: unreclaimed sum permanently transferred to TongNet Network Reserve for network-only expenses. **Potential forfeiture and legal risk: do not implement with real money before consent/legal review.**

## Last question answered
**Q1, Option B, confirmed 2026-10-24:** After Trigger, a sender cannot cancel or emergency-stop, **even for an incorrect recipient address**. The recipient retains the 24-hour claim window. If unclaimed, sender-only recovery during the next 72h applies. No guarantee of recovery if wrong receiver claims.

## Q2 answered (2026-10-24)
**Confirmed:** User selected permanent DEAD state: a wallet not authenticated/enrolled during the first 72 hours after creation can **never** activate later. A lost first Setup Key cannot be re-issued to bypass initial deadline. A newly generated wallet would be needed. Network can prove expired/non-enrolled status, not key loss itself.

## Latest decisions — Disaster Recovery Wallet (confirmed 2026-10-24)

The user specified an optional, one-time Disaster Recovery Wallet address in **normal Wallet Settings** (not inside BlackBox). When it is first set, a separate one-time **Disaster Recovery Key** is issued. This key is distinct from (1) Wallet Private Key and (2) TongNet Authenticator Master Key.

**Permanently immutable:** Recovery wallet address and disaster key can NEVER be changed, replaced, regenerated or reset, even if lost. If Disaster Recovery Key is lost, Run Disaster Recovery becomes unavailable. If Wallet Private Key AND Authenticator Master Key survive, user may continue **normal BlackBox-authorized transfers** to another wallet; this does not change immutable disaster configuration.

**Run Disaster Recovery:** Must prove original Wallet Private Key **AND** the one-use Disaster Recovery Key. **NO** BlackBox access or TongNet Authenticator code required. On atomic successful recovery, sweep all *eligible* value (less applicable fee) exclusively to preset destination, consume key once, and set source Wallet permanently DEAD.

**Unresolved contradiction:** The creator says ALL funds; but value may already be locked in a pending/triggered transfer whose receiver has prior claim rights. We must define eligible balances and ordering before implementing.

See [docs/DISASTER_RECOVERY.md](docs/DISASTER_RECOVERY.md), [docs/DECISIONS.md](docs/DECISIONS.md).

## Q5 confirmed (2026-10-24)
**Option A:** INITIAL Disaster Recovery Wallet address registration requires BOTH Wallet Private Key proof AND TongNet Authenticator approval. Once set, both destination and Disaster Recovery Key are permanently immutable. Later Run Disaster Recovery still needs Wallet Private Key + one-use Disaster Recovery Key, not BlackBox/Authenticator. See docs/DECISIONS.md.

## Q6 answered (2026-10-24) — Triggered escrow and recovery-wallet sender claims

1. Run Disaster Recovery immediately moves **only available/unlocked** wallet value (less any fee) into immutable pre-registered Disaster Recovery Wallet and marks source permanently DEAD. Funds previously Triggered stay locked in their **original escrow** (e.g. 300 locked + 700 unlocked → 700 rescued now, 300 remains conditional).
2. The receiver retains their **full 24h claim right** since Trigger. If receiver claims, it settles forever, no source recovery of that escrow.
3. If receiver fails to claim, original sender has the next **72h** opportunity. If owner already possesses the original **sender's one-time Claim Key** (normally in source BlackBox), they can submit **same key from linked Disaster Recovery Wallet** after the source's Run Disaster Recovery has actually finalized. The network validates immutable address-binding + destination wallet control + original transaction-scoped entitlement and time window. No new claim key is minted or copied.
4. If the user lost the sender Claim Key with inaccessible source BlackBox, they cannot use disaster recovery to bypass it. After expiry, the creator's proposed reserve forfeiture rule remains, subject to legal/consumer analysis.
5. A cryptographically pre-registered link does **NOT** prove the two wallets belong to the same human, only that the original wallet authorised this destination. Correctness and race handling remain unaudited.

**Special unresolved state:** Q6 dealt with payments already Triggered. A transaction only LOCKED but NOT yet Triggered is still inside initial 3h deadline and auto-refunds without a Claim Key if no Trigger. That case is NEXT Q7.

## Q7 confirmed on 2026-10-24

User selected Option A. If an older outgoing transfer remains locked but untriggered when terminal disaster recovery ends the source wallet, keep the lock until the original three-hour expiry. At expiry refund automatically to the original wallet's pre-registered immutable disaster recovery destination. Source is DEAD and cannot trigger later. No early release or manual cancellation. Implementation and finality testing remain pending.

## NEXT: Question 8

Ask in simple Punjabi, ONE question only: When the user initially registers the permanently immutable Disaster Recovery Wallet address, source Wallet Private Key plus TongNet Authenticator approval are already required. Should the DESTINATION wallet additionally sign with its own private key, proving the owner has access to that destination? Options: A = require destination signature; B = accept valid address with manual visual confirmation; C = other solution. Cryptographic control is not proof of real-world identity. Do not assume answer.

## Next steps after answer
1. Record decision ID and precise time/conditions in `docs/DECISIONS.md`.
2. Update `docs/FAQ.md` and relevant `docs/PROTOCOL.md` / `docs/SECURITY.md`.
3. Update `PROGRESS.md` and next open question here.
4. Append a dated entry to `CHANGELOG.md`.
5. Commit to GitHub and report success; then ask just the next question.

## Next open questions after wrong-address decision
Untriggered three-hour auto-refund into a now DEAD wallet (NEXT Q7); sender Claim Key loss and expiry handling; receiver-vs-sender races; wallet/authenticator compromise; reserve forfeiture legality; consensus/Sybil resistance; network partitions.

## Not yet accomplished
No tested code, launched coin, proof of novelty, verified 2015 artifacts, audit, consensus mechanism or deployment.
