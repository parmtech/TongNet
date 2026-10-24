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

## NEXT SINGLE QUESTION (unanswered — Q6)

**Punjabi:** "ਮੰਨ ਲਓ Wallet ਵਿੱਚ 1,000 TONG ਨੇ। 300 TONG ਪਹਿਲਾਂ ਦੀ transaction ਵਿੱਚ lock ਨੇ, ਤੇ 700 available ਨੇ। ਹੁਣ ਤੁਸੀਂ Disaster Recovery ਚਲਾਉਂਦੇ ਹੋ ਤੇ ਪੁਰਾਣਾ Wallet ਹਮੇਸ਼ਾ ਲਈ DEAD ਹੋਣਾ ਹੈ। 300 locked TONG ਦਾ ਕੀ ਕਰੀਏ? **A:** 700 ਹੁਣ backup wallet ਨੂੰ ਭੇਜੀਏ; 300 ਲਈ receiver ਦੇ ਪੁਰਾਣੇ ਹੱਕ ਜਿਉਂ ਦੇ ਤਿਉਂ ਰਹਿਣ, ਤੇ ਜੇ ਬਾਅਦ ਵਿੱਚ refund sender ਨੂੰ ਬਣੇ ਤਾਂ ਉਹ backup wallet ਵਿੱਚ ਜਾਵੇ। **B:** ਜਦ ਤੱਕ 300 ਵਾਲੀ transaction final ਨਹੀਂ ਹੁੰਦੀ, ਸਾਰੀ Disaster Recovery wait ਕਰੇ। ਜਾਂ ਤੁਹਾਡਾ ਹੋਰ ਤਰੀਕਾ?"

Do not assume the answer. Await user.

## Next steps after answer
1. Record decision ID and precise time/conditions in `docs/DECISIONS.md`.
2. Update `docs/FAQ.md` and relevant `docs/PROTOCOL.md` / `docs/SECURITY.md`.
3. Update `PROGRESS.md` and next open question here.
4. Append a dated entry to `CHANGELOG.md`.
5. Commit to GitHub and report success; then ask just the next question.

## Next open questions after wrong-address decision
Initial disaster address setup security; treatment of locked funds in disaster sweep; lost-key policy for different factors; wallet/authenticator simultaneous compromise; reserve forfeiture and consent; consensus/Sybil resistance; network race conditions.

## Not yet accomplished
No tested code, launched coin, proof of novelty, verified 2015 artifacts, audit, consensus mechanism or deployment.
