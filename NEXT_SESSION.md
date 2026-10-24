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

## Q10 answered — 24-hour expiry (Option A, confirmed 2026-10-24)

If R does not Accept or Reject a recovery pairing request within **24 hours**, it automatically enters EXPIRED, without link/key. While PENDING or after EXPIRED, S's Disaster Recovery is NOT_CONFIGURED. A late Accept cannot resurrect it. REJECT during the period notifies S BlackBox under Q9. Time starts from canonical network-accepted request creation; detailed clock and acceptance boundary ordering require engineering.

## Q11 confirmed — Option B (2026-10-24)

A SOURCE Wallet cannot cancel, withdraw, redirect or replace any pending disaster pairing request during its 24-hour window. It MUST wait for destination BlackBox REJECT or automatic EXPIRED at 24 hours before starting another separately authenticated request. If destination ACCEPTS before expiry, pairing becomes irrevocable and one-use recovery secret is issued into destination BlackBox. While pending, source remains NOT_CONFIGURED; no key or association exists. This is user-confirmed design, not an implementation.

## Q12 confirmed — Option A, strict final network acceptance

User says any recovery-wallet BlackBox ACCEPT must achieve **decentralized network finality before the original 24-hour pairing deadline**. A signed/tapped/rebroadcast request before deadline that finalizes after deadline is **EXPIRED**. No one-use Disaster Recovery Key and no immutable S→R pairing in that situation. Device/relay arrival timestamps do not qualify. Implementation of consensus time/finality remains unsolved. This is specifically the *recovery pairing request*, not yet a decision for all payment claim expiries.

## Q13 user direction recorded (2026-10-24) — network queue and timers

The user said slow or fast network must NOT change how running timers elapse. Under overload, tasks/transactions may be queued or load-balanced until processing returns to normal. Crucially a NEW transaction's timer starts ONLY once the NETWORK ACCEPTS the transaction; not merely when the user submits it. Technical recommendation (not a separately ratified requirement): use consensus FINALITY as the acceptance boundary; QUEUED_NONFINAL does not debit/credit settled balance, mint a claim key, create final registration or start a new payment timer. Once new Send final: three-hour Trigger countdown starts; once Trigger final: receiver 24h, sender following 72h. Existing disaster pairing request's 24h starts when REQUEST is final; Q12 requires its destination ACCEPT to be final before deadline.

Open risk: an ALREADY RUNNING receiver/sender Claim period still elapses while a claim is waiting to finalize. Simply queued status doesn't preserve that Claim deadline; whether strict financial Claim finality vs earlier authenticated receipt qualifies remains for Q14. Full decentralized network halt and automatic reserve forfeiture during halt remain unresolved; preserve explicit consumer/legal launch blocker.

## Q14 answered (2026-10-24) — Option A, strict financial Claim finality

The user confirmed strict expiry for EXISTING receiver and sender Claim deadlines. For triggered transaction tT (Trigger consensus-finality time): Receiver Claim must be NETWORK-FINAL strictly BEFORE tT+24h. If receiver did not claim, the sender's distinct one-time Claim may finalize in the NEXT 72h, strictly BEFORE tT+96h. Clicking, signing, placing an operation in queue or relay receipt before its deadline DOES NOT preserve that entitlement if consensus finality happens after deadline. Late Claim rejected as EXPIRED. This is independent of Q13 rule for starting NEW transaction timers only at first network acceptance/finality. Atomicity and clock correctness unimplemented.

**Major safety blocker:** If all TongNet validators stop confirming transactions across a user's claim deadline, even an early queued Claim cannot finalize. Prior user proposed permanent transfer of unclaimed funds to TongNet Network Reserve after 24+72h, but this is potentially confiscatory and a major consumer/legal launch blocker. Q15 asks if post-outage escrow must be preserved rather than automatically forfeited; Q14's elapsed times remain unchanged unless user separately decides otherwise.

## Q15 answered and broadly clarified (2026-10-25) — Universal Network Delay Calculator

The user's direct instruction: if **ANY** transaction/network task is late due to TongNet network slowness, congestion or outage, calculate exact attributable network delay and grant **the exact same amount of EXTRA ALLOWED TIME**. This applies to EVERY affected time-bound operation, not just Claim: Send→Trigger 3h, Receiver Claim 24h, Sender reclaim 72h, Disaster Recovery pairing request's 24h and destination Accept, and other time-bound tasks. The local/canonical clock cadence remains unchanged; **effective deadline is extended**. New transactions' timers still start only after network accepts them (Q13; recommend consensus finality), and queueing before first acceptance should not create a timer nor double-credit time. Timing compensation requires no early finality exception: Q12/Q14 require consensus FINALITY before the appropriately **network-delay-adjusted deadline**. When receiver claim cutoff extends, sender-only reclaim must begin AFTER receiver exclusivity ends; proposed reserve disposition must await ALL adjusted rights. No keys, money or rights can be double settled.

This refines earlier Q12/Q14 'strict fixed deadline' **only regarding the adjusted cutoff**, not strict finality. All delay measurements/thresholds, precise eligibility, decentralised clocks, queue fairness, anti-spam, attribution and no-double-credit require design. No working network or audited Network Delay Calculator. Proposed forced reserve forfeiture remains a legal and consumer launch blocker even after adjustment; do not infer consent or permission.

## NEXT SESSION — Architecture proofs, not unanswered Q16

On 2026-10-25 the user chose **Q16 C, Q17 C, Q18 C, Q19 C, Q20 C, Q21 C, Q22 B, Q23 B, Q24 C, Q25 B**, then requested the entire backlog and best safety-first, high-performance answers to be reviewed and batch-saved in GitHub. New master files:
- **docs/TONGNET_FUTURE_ARCHITECTURE.md:** architecture review with proven BFT research base, parallelisation research, hybrid anti-Sybil validators with optional security bonds/PoS component, delay compensation and strict deadlines, sponsored fees and launch blockers.
- **docs/MASTER_QA_RECOMMENDATIONS.md:** the 95 original deep questions with written engineering answers and separate explicit user-confirmed status. Candidate recommendations are NOT automatically user-ratified.

Current instruction: do NOT revert to the superseded 'one-question-at-a-time until 95 answered' workflow. User prioritises zero single-party runtime dependency (not literally zero physical dependencies), strong eventual decentralisation (first permissioned phase must be acknowledged), near-zero customer fees with sustainability and honest innovation. They allow rethinking previous suggestions but do not silently revoke previously confirmed wallet entitlement or immutability rules. Forced reserve confiscation is a legal/safety blocker: recommend voluntary sponsors or protected refund, owner acceptance required before a real-money protocol change. No blockchain code, consensus, audited keys, Delay Calculator, live transfer, benchmark or testnet was built from these documents.

**Next engineering work:** 1) canonical escrow/Claim/DEAD state transition table; 2) formal fault and committee membership assumptions, stable epochs; 3) credible exact-once hybrid Delay Calculator and recovery from disputed proofs; 4) simulator invariants; 5) testnet and external review. Do not claim proof or 'world-first'.

## Next steps after answer
1. Record decision ID and precise time/conditions in `docs/DECISIONS.md`.
2. Update `docs/FAQ.md` and relevant `docs/PROTOCOL.md` / `docs/SECURITY.md`.
3. Update `PROGRESS.md` and next open question here.
4. Append a dated entry to `CHANGELOG.md`.
5. Commit to GitHub and report success; then ask just the next question.

## Next open questions after wrong-address decision
Formalise hybrid per-operation + global delay credit and secure automatic validator membership (Q16–Q25 answered; engineering still open); destination BlackBox offline issues, authenticated Accept/Reject races, sender Claim Key loss/expiry, receiver-vs-sender races, wallet/authenticator compromise, reserve forfeiture legality, consensus/Sybil resistance.

## Not yet accomplished
No tested code, launched coin, proof of novelty, verified 2015 artifacts, audit, consensus mechanism or deployment.

## Language selection checkpoint — 2026-10-25

User explicitly delegated which programming language is best. **Use Rust as the primary blockchain and wallet core implementation language**; Kotlin/Swift or native UI wrappers only when necessary, shared crypto and transaction authority in Rust. Rationale: memory-safe by default, compiled native performance, concurrency and platform portability. No build or tests have been produced. Next engineering deliverable should be the safely versioned Cargo workspace and deterministic escrow/wallet state machine plus property tests, keeping research architecture and all open release blockers intact.

## Consumer adoption and banking critique (2026-10-25)

Read [Product Critique & Adoption Plan](docs/TONGNET_PRODUCT_CRITIQUE_AND_ADOPTION_PLAN.md) before discussing product uniqueness, TONG supply or banking. Main red-team result: the user-confirmed original 3h Send/Trigger, Receiver 24h Claim and sender 72h reclaim cannot alone work for ordinary instant retail checkout. **Recommendation only, not yet user-confirmed:** add a second direct Instant Pay transaction type, preserve exact old rules as Protected Pay; do not alter user's existing contractual entitlements by assumption. Price TONG independently of bank fiat redemption; proposed 1B maximum and 9 decimals are *examples*, not chosen coin monetary policy. Banking = future regulated partner/interoperability work, not a bank automatically. Real market trust needs audited independent validators, non-custodial verified safety, honest receipts, no hidden fees and sound loss recovery. Reserve confiscation risk remains unresolved.
