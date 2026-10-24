# TongNet — Next Session Handoff

**Read first:** [PROGRESS.md](PROGRESS.md) → [docs/DECISIONS.md](docs/DECISIONS.md) → [docs/FAQ.md](docs/FAQ.md) → [docs/PROTOCOL.md](docs/PROTOCOL.md).

## Deep questioning backlog

Read [docs/DEEP_QUESTIONS.md](docs/DEEP_QUESTIONS.md). There were **86 initial questions**, now **88 tracked questions** across keys, disaster recovery, irreversible state, financial and legal edge cases, validators/consensus, zero-fee economics, privacy and operational resilience. User explicitly asks to continue posing as many deeper questions as needed, and to commit every resulting decision. **One question per turn** is still best for a reliable decision log, but keep adding questions to backlog as new risks are discovered.

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

## Q8 clarification confirmed on 2026-10-24

When S registers R (recovery destination) within S's NORMAL wallet settings, using Wallet Private Key + TongNet Authenticator (Q5), the distinct optional one-time Disaster Recovery Key MUST be generated **inside R's own encrypted TongNet BlackBox**, NOT S's BlackBox or unsecured interface. The same key is later needed alongside S Wallet Private Key to execute Run Disaster Recovery without S's Authenticator/BlackBox. Consumption of key and terminal S DEAD state are one-time; registered recovery address and key can never change or be reset.

**Important:** R's BlackBox key creation/delivery is NOT itself proof that R's wallet private key has approved and signed the association, nor that two wallets have the same natural owner. The user's Q8 statement has resolved key LOCATION, not exactly when an irreversible pairing becomes final.

## Q9 answered — Destination BlackBox Accept/Reject controls setup (2026-10-24)

- Main/source Wallet S user initiates a pairing request for recovery wallet R via normal Wallet Settings and S Wallet Private Key + S TongNet Authenticator (Q5).
- Request arrives in R's OWN encrypted TongNet BlackBox with Accept and Reject actions.
- **PENDING / no action**: source S is still **NOT_CONFIGURED** for Disaster Recovery, **NO Disaster Recovery Key exists** and **NO permanent S-R attachment** exists.
- **REJECT** by R: NO key, NO attachment, and a rejected/status response is returned to the requestor SOURCE wallet's BlackBox.
- **ACCEPT** by R: only now generate the immutable, unique, one-time Disaster Recovery Key **inside R's own BlackBox** and permanently attach R as recovery wallet of S. Once accepted, no destination/key changes allowed.
- Later emergency action uses S Wallet Private Key + that one-time key (NOT S's BlackBox or Authenticator) to rescue spendable balance to R and make S DEAD. Q6/Q7 remain intact for escrow.
- These are REQUIREMENTS, not implementation. Actual crypto binding, authenticated R approval, race/atomicity and duplicate handling need engineering. Do NOT claim two wallet addresses are proven to have the same person.

## NEXT SINGLE QUESTION — Q10 / DQ-089

Ask Punjabi: "ਜੇ Disaster Recovery ਵਾਲੇ Wallet ਦੇ BlackBox ਵਿੱਚ request ਆ ਗਈ, ਪਰ ਉਹ ਬੰਦਾ ਨਾ Accept ਕਰਦਾ ਤੇ ਨਾ Reject, ਤਾਂ request ਕਿੰਨਾ ਚਿਰ PENDING ਰਹੇ? **A:** 24 ਘੰਟੇ ਬਾਅਦ automatic EXPIRED. **B:** 72 ਘੰਟੇ ਬਾਅਦ EXPIRED. **C:** ਜਿੰਨਾ ਚਿਰ ਜਵਾਬ ਨਹੀਂ ਆਉਂਦਾ, pending ਹੀ ਰਹੇ. **D:** ਤੁਹਾਡਾ ਆਪਣਾ time. Pending ਦੌਰਾਨ ਕੋਈ Recovery Key ਜਾਂ link ਨਹੀਂ ਬਣੇਗਾ."

User requests one question at a time and next question only after relevant GitHub docs are committed. Never assume a pending timeout.

## Next steps after answer
1. Record decision ID and precise time/conditions in `docs/DECISIONS.md`.
2. Update `docs/FAQ.md` and relevant `docs/PROTOCOL.md` / `docs/SECURITY.md`.
3. Update `PROGRESS.md` and next open question here.
4. Append a dated entry to `CHANGELOG.md`.
5. Commit to GitHub and report success; then ask just the next question.

## Next open questions after wrong-address decision
Pending pairing request expiry (NEXT Q10), withdraw/resubmit rules, destination BlackBox offline issues, authenticated Accept/Reject races, sender Claim Key loss/expiry, receiver-vs-sender races, wallet/authenticator compromise, reserve forfeiture legality, consensus/Sybil resistance.

## Not yet accomplished
No tested code, launched coin, proof of novelty, verified 2015 artifacts, audit, consensus mechanism or deployment.
