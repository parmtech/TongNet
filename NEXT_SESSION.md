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

## NEXT SINGLE QUESTION (unanswered)
**Punjabi:** "ਮੰਨ ਲਓ ਤੁਸੀਂ ਗਲਤ receiver address ਉੱਤੇ ਪੈਸੇ ਭੇਜੇ ਅਤੇ ਆਪਣੇ BlackBox ਤੋਂ Trigger ਵੀ ਕਰ ਦਿੱਤਾ। ਜੇ receiver ਨੇ ਹਾਲੇ Claim ਨਹੀਂ ਕੀਤਾ, ਤਾਂ ਕੀ ਤੁਸੀਂ ਕੋਈ emergency Stop option ਚਾਹੁੰਦੇ ਹੋ, ਜਾਂ 24 ਘੰਟੇ ਵਾਲਾ rule ਬਿਨਾਂ ਕਿਸੇ exception ਦੇ ਚੱਲੇ?"

Do **not** assume the answer. Await the user.

## Next steps after answer
1. Record decision ID and precise time/conditions in `docs/DECISIONS.md`.
2. Update `docs/FAQ.md` and relevant `docs/PROTOCOL.md` / `docs/SECURITY.md`.
3. Update `PROGRESS.md` and next open question here.
4. Append a dated entry to `CHANGELOG.md`.
5. Commit to GitHub and report success; then ask just the next question.

## Next open questions after wrong-address decision
Lost one-time setup code within 72 hours; lost master secret; wallet/authenticator simultaneous compromise; reserve forfeiture and consent; Sybil-proof consensus; transaction race boundaries; backup and device loss.

## Not yet accomplished
No tested code, launched coin, proof of novelty, verified 2015 artifacts, audit, consensus mechanism or deployment.
