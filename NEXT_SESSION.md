# TongNet — Next Session Handoff

**Read first:** [PROGRESS.md](PROGRESS.md) → [docs/DECISIONS.md](docs/DECISIONS.md) → [docs/FAQ.md](docs/FAQ.md) → [docs/PROTOCOL.md](docs/PROTOCOL.md).

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

## NEXT SINGLE QUESTION (unanswered — Q3)
**Punjabi:** "ਮੰਨ ਲਓ ਤੁਹਾਡਾ TongNet Wallet ਪਹਿਲਾਂ ਹੀ ACTIVE ਹੋ ਚੁੱਕਿਆ ਹੈ ਤੇ ਉਸ ਵਿੱਚ ਪੈਸੇ ਵੀ ਹਨ। ਹੁਣ TongNet Authenticator ਦੀ Master Key ਜਾਂ ਫ਼ੋਨ ਗੁੰਮ ਹੋ ਜਾਂਦਾ ਹੈ, ਪਰ Wallet Private Key ਤੁਹਾਡੇ ਕੋਲ ਹੈ। ਕੀ ਕੋਈ ਵੱਖਰਾ secure recovery ਤਰੀਕਾ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ, ਜਾਂ ਫਿਰ BlackBox ਹਮੇਸ਼ਾ ਲਈ lock ਰਹੇ?"

Do **not** assume the answer. Await the user.

## Next steps after answer
1. Record decision ID and precise time/conditions in `docs/DECISIONS.md`.
2. Update `docs/FAQ.md` and relevant `docs/PROTOCOL.md` / `docs/SECURITY.md`.
3. Update `PROGRESS.md` and next open question here.
4. Append a dated entry to `CHANGELOG.md`.
5. Commit to GitHub and report success; then ask just the next question.

## Next open questions after wrong-address decision
Lost authenticator master secret; wallet/authenticator simultaneous compromise; reserve forfeiture and consent; Sybil-proof consensus; transaction race boundaries; backup and device loss.

## Not yet accomplished
No tested code, launched coin, proof of novelty, verified 2015 artifacts, audit, consensus mechanism or deployment.
