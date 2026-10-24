# TongNet Disaster Recovery Wallet — Current Design (2026-10-24)

> **LATEST 2026-10-25 OWNER OVERRIDE — ACTIVE Recovery Target (V4):** An accepted S→R recovery pairing does **NOT** freeze, reclassify, or disable R's ordinary wallet. Both S and R remain `NORMAL_ACTIVE` with separate wallets, balances, transfers, BlackBoxes and signing keys. R can independently set its OWN further recovery C even while it carries a **separate sealed parent S BlackBox archive**. ONLY S's encrypted BlackBox records are mirrored, never S's blockchain transaction history/balance. S archive is not readable before authenticated BFT-final `RUN_DISASTER_RECOVERY(S,R)`, which makes S `DEAD`, transfers only S eligible unlocked funds once into ALREADY-ACTIVE R and authorises unlocking S archive with permanent original S provenance. R's own records are unaffected. Prior FREEZE / blocked-SEND-RECEIVE / delayed-activation rules are **SUPERSEDED**. **R must still be fresh/never financially used AT INITIAL BINDING**, until the owner explicitly changes that earlier requirement; AFTER binding it remains NORMAL_ACTIVE for ordinary transactions. But separate archive lock versus normal R wallet functions must be enforced. Key-release decryption cannot be honestly promised without a reviewed conditional cryptographic scheme; S claim K_S late creation and R dying earlier through R→C recovery are OPEN. See [Latest Active Recovery Mirror V4](ACTIVE_RECOVERY_MIRROR_V4.md).


> **LATEST 2026-10-25:** Receiver-only 24h then Sender-only **60 DAYS** (72h superseded), verified delay credit where provable. Unclaimed funds to Network Reserve after expiry = owner intent, **blocked for real-money use pending legal and safety review**. Recovery Wallet must be fresh at pairing and RECOVERY_RESERVED (no ordinary Send/Receive), permits setup metadata acceptance; on final Disaster Recovery it inherits successor authority and becomes ACTIVE, original S becomes DEAD. Historical ledger remains immutable but view is linked; restoring encrypted BlackBox requires previously accessible encrypted backups, NOT spontaneous re-creation of lost secrets. Web clients MUST NOT transmit root/master/private keys to server. How to generate K_S after loss/DEAD of S and how to inherit pending rights remain OPEN. No third-party deal arbitrator. Full latest spec: [Secure P2P v3](SECURE_P2P_V3_RECOVERY_DECISIONS.md) (from repo root: docs/SECURE_P2P_V3_RECOVERY_DECISIONS.md). Older 72h and 3h Trigger records historical.


> **LATEST OWNER REQUIREMENTS — 2026-10-25:** Trusted two-party P2P with no deal arbitrator; validators verify signatures/finality, not buyer/seller disputes. The RECEIVER has the first 24h (clock at final LOCK proposed, not yet ratified). The SENDER then has **60 DAYS**, replacing earlier 72h, to manually reclaim; after that, creator wants remaining unclaimed escrow sent to Network Reserve (OWNER INTENT, **REAL-MONEY DEPLOYMENT BLOCKED** by unresolved legal/consumer protection safety). A special *fresh*, zero-prior-financial-transactions RECOVERY_RESERVED address may complete recovery pairing metadata but CANNOT ordinarily send/receive before one-time disaster-recovery settlement. After successful recovery, S becomes DEAD and R is successor NORMAL_ACTIVE; owner wants historical receipts, BlackBox encrypted backup and pending entitlements shown in R, not destructive rewriting of immutable ledger. Preexisting recoverable encrypted BlackBox backup is REQUIRED to restore lost device data; a lost unbacked secret cannot be resurrected, and wallet/master root secrets must never be sent to a website server. Late sender claim key K_S with LOST/DEAD BlackBox, pending consent migration, exact 24h anchor, and legal forfeiture remain OPEN. See [canonical 2026-10-25 decisions](SECURE_P2P_V3_RECOVERY_DECISIONS.md). Older Trigger/72h/recovery-descriptions are HISTORICAL.


> **CURRENT RULE — 2026-10-25 (SUPERSEDES ALL OLD 3h TRIGGER CONTENT):** User REMOVED separate three-hour Trigger and its 3h automatic refund. Current TongNet Secure Manual P2P: Sender network-final LOCK -> Sender BlackBox makes and privately shares one-time Receiver Claim Code K_R -> exact addressed receiver wallet signs Claim Request -> Sender BlackBox must manually FINAL_ACCEPT exact transaction/recipient/amount -> BFT may finalise receiver settlement. No FINAL_ACCEPT means no receiver payout. No separate Trigger remains. Receiver 24h then Sender's following 72h manually redeemable via fresh Sender BlackBox K_S (verified attributable network delay extensions still apply); 24h from BFT-final LOCK is recommended but not explicitly ratified. No valid absolute guarantee against mistaken approval, stolen signing authority or third-party fraud. Old 3h Q7 disaster refund is obsolete; source DEAD + late K_S needs safe redesigned handling. See [canonical Secure P2P v2](docs/SECURE_P2P_V2.md) (for docs/ files: [canonical v2](SECURE_P2P_V2.md)).


**Design only:** not implemented, verified, audited or ready for real-money use.

## Product and three independent keys

The user can optionally REQUEST a one-time disaster recovery destination address from **normal SOURCE Wallet Settings**, NOT from source BlackBox. Source Wallet Private Key + source TongNet Authenticator authorise the request. This request goes to the **DESTINATION Recovery Wallet's own TongNet BlackBox**. Only if destination independently **ACCEPTS** does the unique one-time **Disaster Recovery Key get generated and delivered INSIDE that destination BlackBox** and the source→destination link become permanently immutable. A PENDING or REJECTED request is **NOT configured recovery**. The key is distinct from that destination's private key and Authenticator Master Key.

The project now has three secret-key categories:
1. **Wallet Private Key** — ordinary wallet access and initiating payment.
2. **TongNet Authenticator Master Key** — independent TongNet BlackBox authorization factor (60-second changing access codes, not a rotating master key).
3. **Disaster Recovery Key** — exists only for wallets whose disaster recovery option was configured; a **one-use secret GENERATED IN THE DESTINATION WALLET'S BLACKBOX** at initial setup, required later to authorize emergency sweep from source. It is NOT the backup wallet's address, wallet private key, or Authenticator Master Key.

## Permanent configuration rules — confirmed by user

- Register the optional disaster destination **once and only after destination ACCEPT**. The pending request is not yet permanent. **After acceptance it cannot ever be changed.**
- **Only after destination acceptance** the corresponding Disaster Recovery Key is generated in destination BlackBox; it cannot be changed, replaced, regenerated, or reset once issued.
- If the Disaster Recovery Key is **lost**, this disaster recovery route is permanently unavailable for that wallet. Possessing Wallet Private Key alone does **not** bypass the missing recovery secret.
- If Wallet Private Key **and** Authenticator Master Key remain available, the user may still normally send the wallet's funds to another active wallet using the regular BlackBox-triggered transaction process. **That does not change the old immutable disaster destination or its recovery key.**
- Provide very clear warnings and require accurate, explicit confirmation of the destination and key backup at setup; no administrative override is allowed under these requirements.
- **Q5 CONFIRMED — Option A (2026-10-24):** INITIAL irrevocable recovery address registration requires both valid **Wallet Private Key authorization AND TongNet Authenticator approval**. A stolen wallet private key alone cannot set the destination. No further change is allowed once the address and key are committed.

## One-time emergency execution — confirmed

**Precondition:** source has a FINAL, accepted and CONFIGURED disaster destination (not PENDING or REJECTED) and its immutable one-use Disaster Recovery Key from the destination BlackBox. A pending request affords **NO disaster rescue route**.

1. Owner has access to source **Wallet Private Key** but lost the SOURCE Authenticator Master Key / SOURCE BlackBox access. The separate destination wallet's BlackBox originally holds the recovery key, which the user must have obtained securely.
2. Open source Wallet using Wallet Private Key.
3. Select **Run Disaster Recovery** and enter the **one-time Disaster Recovery Key** originally generated in the DESTINATION Recovery Wallet's own BlackBox.
4. **Both** source Wallet Private Key authorization **AND** the independent Disaster Recovery Key must be verified. **No TongNet BlackBox or Authenticator code is required.**
5. Network settles all **eligible** funds, minus any actual transaction fee, to **only the permanently registered destination** and atomically consumes the one-time key.
6. In the same atomic irreversible state transition, the original source Wallet becomes **DEAD** forever; it cannot be reactivated.
7. Never accept a different address at Run Disaster Recovery time. Never allow reuse of a successfully consumed recovery secret.

## Q6 — Explicit linked sender-claim entitlement after disaster (confirmed 2026-10-24)

- Example: 1,000 TONG original wallet balance; 700 unlocked, 300 already Triggered and locked. Running disaster recovery moves 700 (less any applicable fee) to the fixed recovery wallet immediately. Original wallet becomes DEAD; 300 remains in transaction escrow, never duplicated.
- 24 hours after original Trigger: only receiver has the right to claim those 300. If receiver claims, final payment is theirs and recovery wallet is not entitled to the same value.
- On receiver nonclaim, for the following 72 hours **the same already-issued sender Claim Key** can be submitted through the **previously immutable-linked Disaster Recovery Wallet**, *only if* the original wallet has actually completed Run Disaster Recovery.
- Recovery-wallet claimant must demonstrate control of its own private key, provide original transaction-bound unspent sender Claim Key, and network must verify an authentic **pre-registered binding** from original wallet to destination. This is **not evidence that both addresses are held by the same natural person**; it is proof of prior cryptographic authorization to link them.
- If the sender cannot access/present their original sender Claim Key, they cannot rescue that escrow merely with the disaster secret; the 72-hour sender-claim opportunity expires. The user's proposed reserve allocation after 96 hours remains a separate unresolved legal/economic blocker.
- Claim right delegation is scoped to **these specific outstanding original-wallet transactions only**, not a transferable master ability to claim arbitrary wallets' payments. Claim always consumes entitlement once, including in racing/partitioned network conditions.
- **Q7 RESOLVED:** A not-yet-triggered original transfer remains locked until its original three-hour deadline; after completed Disaster Recovery kills its source wallet, the no-trigger automatic refund is credited directly to the cryptographically pre-bound recovery wallet at deadline. No early return and no manual cancel.

## Not yet decided (engineering safety problems)

- **Q6 CONFIRMED, Triggered transfers:** immediately sweep ONLY currently unlocked/spendable funds. Keep the locked amount inside its existing transaction escrow and preserve receiver's entire 24-hour claim entitlement. If unclaimed, the already issued sender's one-use Claim Key may be used **from the original wallet's previously linked recovery wallet** during the following 72 hours, even after the original wallet has become DEAD. If the sender has lost that Claim Key / BlackBox access and cannot present it, recovery alone does NOT bypass it; the existing expiry and proposed network-reserve rule still apply. **Q7 confirmed:** for a still-untriggered 3h PENDING_TRIGGER transfer, hold the lock until its existing expiry and pay the automatic refund to pre-bound rescue wallet after source has become DEAD.
- **First-setup authentication confirmed:** BOTH Wallet Private Key authorization and TongNet Authenticator approval. Exact phishing-resistant transaction-bound proof, device compromise resistance and atomic enrollment still require formal protocol design.
- Recovery destination activation status, cryptographic binding and proof of control; wrong address irreversible.
- Can a wallet with no setup still be safe? Yes, standard wallet remains active; disaster feature absent.
- Key format, secure one-time commitment, replay resistance, consensus deadlines, network partitions, fees, expiry with insufficient spendable balance, and fault-tolerant atomic finality.
- Alternative normal transfers after loss of disaster key (if both other keys survive) still use the already confirmed 3-hour trigger, 24-hour receiver claim, and 72-hour sender recovery. Merely initiating a standard send does not instantly credit a new wallet.

## Q9 — Two-sided request/accept handshake (confirmed 2026-10-24)

User-defined phases:

```text
SOURCE S: propose R in normal settings + authorise S private key & S Authenticator
  -> REQUEST_PENDING; recovery_enabled=false; no key issued
DESTINATION R BlackBox: show request and Accept / Reject
  -> Reject: send notification to S BlackBox; recovery_enabled=false; no key/link
  -> No action before 24h: remains pending; recovery_enabled=false; no key/link
  -> 24h deadline with no accepted response: state EXPIRED; recovery_enabled=false; no key/link; stale Accept rejected
  -> Accept: generate unique one-time Disaster Recovery Key in R BlackBox;
             commit irrevocable S→R association; recovery_enabled=true
```

Actual protocol must make destination acceptance, final binding, and key commitment logically atomic; generating an inaccessible key or finalizing binding before it can be safely delivered could strand funds. Network proof should authenticate acceptance and bind it to S, R, action, nonce and exact immutable address. BlackBox approval does not prove two humans are the same person. Existing two-factor SOURCE authorization remains required before request issuance.

## Current priority / Next single product question

**Q5 ANSWERED:** Option A. Register immutable disaster destination only when **Wallet Private Key + TongNet Authenticator** both approve initial setup. After registration, destination and one-use secret are immutable forever.

**Q6 CONFIRMED:** Active disaster recovery moves available/unlocked funds immediately. Any already-triggered transfer retains its receiver's 24-hour claim right. If receiver does not claim, during the subsequent 72-hour sender recovery window a one-time sender Claim Key that the owner already possesses can instead authorise claim **to the bound recovery wallet**, but ONLY when Run Disaster Recovery was actually finalised for the original source wallet. The Claim Key is still required, expiry is unchanged, and one-time spending is enforced. No automatically fabricated Claim Key. A missing sender Claim Key cannot be bypassed. Proposed 96-hour reserve rule stays as described, subject to legal review.

**Q7 ANSWERED (Option A, 2026-10-24):** A lock from an **untriggered** outgoing Send is NOT swept early. The original 3h timer continues. If Run Disaster Recovery has finalized in the meantime, source is DEAD and cannot authorise any new Trigger; when its original deadline arrives, the automatic untriggered refund must be paid **directly to the pre-registered bound Disaster Recovery Wallet**, not to DEAD source and not to receiver. Disaster Recovery does not wait. Atomically settle once; preserve original no-manual-cancel rule.

**Q8 new clarification (2026-10-24):** The one-time Disaster Recovery Key originates **inside the registered DESTINATION wallet's own BlackBox**, rather than being minted or shown in the SOURCE wallet. This is a custody/delivery rule, but is **not by itself a cryptographic destination private-key signature** or proof the same natural person controls both addresses.

**Q9 ANSWERED:** no pairing or key while pending; destination must explicitly ACCEPT in its own BlackBox; after acceptance key is generated there and irreversible link is committed. On REJECT, send notification to source BlackBox; no configuration. **Q10:** unanswered pairing requests expire after 24 hours. **Q11:** source cannot cancel a pending request; wait for Reject or Expired.

## Security warning

These are design requirements only. A stolen wallet key together with the recovery key can execute an irreversible sweep to the **fixed** destination, potentially causing loss or denial of service; if the destination is attacker-controlled because initial setup was compromised, it could cause total theft. Keys must never be committed in plaintext to public/shared repositories. Atomic settlement must be proven.

## Superseded design remarks

- Early discussion entertained recovery execution using only the Wallet Private Key. **Superseded:** recovery always requires Wallet Private Key **plus** the distinct Disaster Recovery Key.
- Early draft asked whether users could change or replace a recovery destination/key. **Resolved: no, never.**
- The independent TongNet Authenticator is **required at initial setup** (Q5 Option A), but is **not required to run emergency recovery**, which instead needs Wallet Private Key plus the one-use Disaster Recovery Key.

## Q7 — Pre-Trigger locks during completed disaster recovery (confirmed, 2026-10-24)

- Example: 1,000 TONG in original wallet, 700 immediately spendable and 300 locked in a Send never yet Triggered. Source performs authenticated Run Disaster Recovery with original wallet secret + one-use Disaster Recovery Key: available 700 (less applicable fee) transfers now to immutable linked recovery destination R and original source becomes permanently DEAD. The separate 300 remains locked until **its original t0+3h deadline**. This is not an early cancellation.
- With original sender permanently DEAD, **no further Trigger** may be authorized by it. If no Trigger was accepted before successful DEAD finality, at t0+3h the original lock is **automatically refunded straight to R** via the previously authorized S→R immutable recovery binding.
- If a Trigger had already become final **before** the source turned DEAD, treat that payment under Q6 receiver-claim/sender-reclaim rules instead. Define deterministic ordering for simultaneous Trigger vs DEAD vs expiry; prove no double-payment.
- No fresh credential is needed for untriggered **automatic** expiry refund. This rule must not be confused with a **Trigger-confirmed** transaction that requires the original sender Claim Key to reclaim after receiver nonclaim.
- The original three-hour lock remains noncancellable, cannot be accelerated by disaster recovery, and creates no recipient Claim Key in the untriggered path.

## Q8 — Where the one-use disaster secret is created (confirmed 2026-10-24)

- First setup is initiated in the SOURCE wallet's ordinary settings and requires SOURCE Wallet Private Key plus its TongNet Authenticator. The target recovery address is permanently bound to the source once setup is final.
- **The one-time Disaster Recovery Key is generated within the TARGET/RECOVERY WALLET'S OWN TongNet BlackBox** only on destination ACCEPTANCE of the initial request, not within the original source wallet and not as an ordinary unsecured screen response. The key is meant to be accessed and backed up securely by whoever controls the target's BlackBox.
- In a later emergency, the original source wallet may lack its own Authenticator; the user proves source Wallet Private Key plus the SAME one-time Disaster Recovery Key from the destination BlackBox to invoke recovery. This execution requires neither source BlackBox nor a current source Authenticator code.
- The network must maintain a protected, verifiable commitment linking the one-use key to **this specific source wallet, exact immutable destination wallet and this particular recovery action**. Do not store the plaintext secret in public state or GitHub; only the destination's authorized encrypted vault should hold/display it.
- Destination BlackBox key generation and a **cryptographic signature by destination wallet private key** are different mechanisms. The owner's answer explicitly specifies the former. Whether destination must separately ACCEPT/sign, and when the irreversible link becomes final, is the NEXT question (Q9).
- Do not confuse the **Disaster Recovery Key** with one-time Sender Claim Keys from ordinary outgoing transactions. Different operations; different state/commitments.

## Q10 confirmed — 24-hour pending request expiry (Option A, 2026-10-24)

- Unanswered destination BlackBox pairing request automatically expires after **24 hours**. It does not generate a one-time Disaster Recovery Key or install an immutable source→destination binding.
- Pending means recovery is **NOT_CONFIGURED**; Expired also means **NOT_CONFIGURED**. Rejected is another closed, unconfigured state.
- **Q12 strict Option A:** a destination Accept is successful ONLY if **network-finalized before** the 24-hour expiry boundary. A late-finalized operation is rejected despite a pre-deadline click/submission/relay receipt. Accept/Reject/Expiry races, replay, timestamp definitions, offline delivery and network partition ordering must be deterministic and are not yet technically implemented.
- Pending expiry must be based on authoritative network-accepted request time, not the local device clock (exact consensus time procedure TBD). The user's rule is a 24-hour window, not a user-selected wall-clock date.
- The no-change-forever rule applies only **after an ACCEPT is finalized**, not to a request that expired without a key.

## Q11 confirmed — Option B

A PENDING disaster recovery association cannot be cancelled, withdrawn, replaced or redirected by its SOURCE wallet. The source must wait for the destination to REJECT or for the original 24-hour deadline to EXPIRE, before trying a new association. If destination ACCEPTS a valid request, the immutable link is final and cannot ever be changed. PENDING still means NOT_CONFIGURED.

## Next Q12

**Q12 ANSWERED, Option A:** destination BlackBox ACCEPT has to be fully **network-finalized before** its 24-hour request deadline. Even if a user tapped Accept or an intermediate node received the signature before the limit, **post-deadline finality means EXPIRED**; no immutable pairing or one-time recovery secret. Use canonical network finality order, not local clock. Implementation and consensus time model still require research.

**Next Q13:** During a serious TongNet network outage, should the 24h receiver and 72h sender *payment claim* deadlines remain absolute even if claims cannot be finalized, or be suspended under objectively provable network-outage rules?

## Q12 — Recovery pairing confirmation must finalize before deadline

**Option A confirmed, 2026-10-24.** A one-time recovery pairing request submitted by S has 24h. R's BlackBox ACCEPT must attain definitive decentralized network finality before its exact deadline to issue the unique recovery key and commit immutable S→R linking. An event signed, tapped, or relayed earlier but finalized after deadline is EXPIRED: no key, no binding, not configured. A timestamp asserted by a phone or one untrusted relay does not count. Consensus-finality and distributed-time properties require formal design and testing.

## Q13 — Pending recovery-pairing request in a congested network

The user distinguishes QUEUED work from network acceptance. A new source→destination recovery pairing request has no active 24h acceptance window merely because a local phone or relay placed its signed request in queue. **Recommended implementation:** its Q10/Q12 24h clock begins only at canonical NETWORK-FINAL acceptance of the pairing REQUEST; the destination's independent BlackBox ACCEPT still must become network-FINAL before that 24h cutoff under strict Q12. Overloaded queues cannot shorten or extend a running pairing deadline. This is an architecture recommendation consistent with user intention, not a tested consensus scheme. Already-running payment claims are a different question, Q14; do not allow queue-admission to create keys or irreversible links.

## Q14 — Strict deadlines apply to disaster-linked sender reclaim

Q14 confirmed Option A: the sender's original Claim Key used *from the linked recovery wallet* under Q6 must still obtain network finality strictly BEFORE its original sender reclaim deadline (following receiver 24h, next 72h). Prior queue admission, signature or relay receipt does not preserve a late-finalized reclaim; no new Claim Key is issued because the original wallet is DEAD. Network must not double-pay escrow. The fate of value whose claim deadlines pass during a **complete network outage** remains Q15, with any proposed transfer to reserve under legal and consumer-protection review.

## Q15 — Recovery operations also receive verified network delay compensation

The user's universal TongNet Network Delay Calculator requirement (2026-10-25) covers **disaster recovery pairing as well as financial payment windows**. A source→destination pairing request still has a NOMINAL 24h to receive target BlackBox ACCEPT (Q10). If genuine TongNet network processing/backlog/outage delay affects that timed approval, the **effective 24h deadline extends by exactly measured attributable network delay**. Q12 still demands consensus FINALITY strictly before the **ADJUSTED** cutoff, not before the unextended wall-clock timestamp; a queue ticket alone does not count.

Source requests remain noncancellable while legitimately PENDING (Q11), and only post-final ACCEPT creates a permanent binding and one-time recovery secret. A delayed network must not silently expire PENDING, release request slots or generate/replay a disaster key before the correct compensation window resolves. Similar attributable delay applies to any time-bound recovery task. Critical exception: a new pairing request QUEUED before the network initially accepts it has **no started 24h timer yet** under Q13; crediting the same waiting time again after initial acceptance would double-count. Network Delay Calculator, eligible intervals and anti-manipulation proofs are OPEN Q16. No tested implementation exists.

## 2026-10-25 reconciliation with high-security architecture research

The user confirmed Q16 **C** hybrid operation-specific/network-wide verified delay, Q17 **C** independent counterfeit-delay detection, Q18 **C** cryptographic evidence consensus or protected suspense, and Q19–Q25 anti-Sybil/quorum/membership protections. These apply to this module's pairing request, R BlackBox ACCEPT, 24h effective deadline and linked sender reclaim (without reissuing secrets or undoing immutability).

**Do not silently change earlier user-confirmed irreversible rules:** S/R pairing and disaster secret are immutable once properly accepted; R must accept before key generation; S needs original key + unique recovery key for execution; S becomes DEAD; only spendable balance moves immediately and already-locked original rights remain. Recommend user-visible warnings, key custody tests and objective pause if delay proof or finality is unavailable; real-money release requires an external assessment of irrecoverable user harm. No implemented crypto, recovery key issuance or finality proof is claimed. Architectural references: [TONGNET_FUTURE_ARCHITECTURE.md](TONGNET_FUTURE_ARCHITECTURE.md), [MASTER_QA_RECOMMENDATIONS.md](MASTER_QA_RECOMMENDATIONS.md).

## 2026-10-25 ordinary-transaction Sender Claim Key chronology conflict — unresolved

**User confirmed:** Both ordinary payment keys originate in SENDER BlackBox. Receiver Claim Code K_R is generated at Send setup, manually shared with intended receiver, activated after Trigger and receiver-only for next nominal 24h. If unclaimed, key K_R expires and a **NEW** Sender Claim Key K_S is generated in SENDER BlackBox at the end of receiver priority, sender-only for next 72h. This DOES NOT modify the unrelated Disaster Recovery Key (generated in DESTINATION Recovery Wallet BlackBox on ACCEPT).

**Previous Q6 required:** after completed Disaster Recovery kills S and S BlackBox access may be lost, original sender's previously existing one-use Claim Key could be submitted from immutable R after receiver nonclaim. This assumes the sender key was already created/accessible. **NEW LATE-GENERATION POLICY CONFLICTS.** Preserve both user statements as dated historical requirements and mark exact reconciliation OPEN, NOT silently solved: if S BlackBox destroyed/irretrievable before 24h, late K_S may not be available, invalidating Q6's practical sender reclaim. Candidate A: late K_S generated only when source BlackBox available (loss possible); Candidate B: precommitted sealed future recovery secret generated earlier and only activated/unsealed after receiver window, with a strict formal proof and possible linked R custody. User must choose tradeoff. No claim bypass or network-generated plaintext secrets.

## 2026-10-25 owner decision — live encrypted Recovery Mirror
After immutable S→R pairing is ACCEPTED, S's BlackBox records, pending claim metadata, receipts and wallet history must be **continuously encrypted and synchronized to R's RECOVERY_RESERVED mirror**. S remains solely NORMAL_ACTIVE and owns spendable balance; R must have NO ordinary receive/send/claim/spend permission before one-time FINAL `RUN_DISASTER_RECOVERY`. Mirror is data + successor rights, NOT a second ledger balance or unilateral signing backdoor. After valid one-time disaster activation, S is permanently DEAD, R becomes only NORMAL_ACTIVE successor; pending escrow rights and history remain verifiably linked, and only eligible unlocked balance actually moves. Backups must exist and be verifiable *before device loss*; offline or unsynced secrets cannot be recovered magically. Ciphertext encrypted with a key held by R might still be decrypted early offline, so pre-activation READ confidentiality is a separate UNSOLVED key-release problem: cryptographic protocol can prevent preactivation SPENDING but cannot make decryption secrets unknowable after already given away. Sender post-24h new K_S with destroyed S BlackBox remains unresolved; 24h receiver then 60 full days sender reclamation is current rule (older 72h superseded). See [Recovery Mirror Protocol](RECOVERY_MIRROR_PROTOCOL.md) (repo root: docs/RECOVERY_MIRROR_PROTOCOL.md). This is a user-confirmed product direction, NOT built or audited.

## 2026-10-25 — OWNER-CONFIRMED: Recovery successor can later register ITS OWN future recovery

**Latest exact lifecycle, replacing any interpretation that a Recovery Address is permanently recovery-only:**

1. While main wallet S is `NORMAL_ACTIVE`, its pre-accepted designated R stays `RECOVERY_RESERVED`. R is **exclusively a future successor**: no ordinary SEND / RECEIVE / CLAIM, no second recovery wallet associated *to R*, no `RUN_DISASTER_RECOVERY` initiated *from R*, no funds spending, nor any alternate activation. R can ACCEPT pairing protocol metadata, host continuously synchronized encrypted BlackBox mirror backups, and receive authenticated status/checkpoint events, but these are **not normal financial transactions**. The original S may have one immutable active S→R relationship as already confirmed.
2. `RUN_DISASTER_RECOVERY(S,R)` with the previously confirmed original S Wallet Private Key + one-time Recovery Key from R BlackBox, and previously accepted immutable binding, must have BFT finality and atomic state update: S `DEAD` (forever), R `NORMAL_ACTIVE` (ordinary financial controls restored) and exactly-once transfer of **only eligible unlocked S funds**. All pending locked escrow obligations and rights survive as successor-authorised entitlements without double spend or arbitrary retroactive finalisation; BlackBox mirror copy is unlocked/restored according to separately audited encryption/backups, and historic S transactions remain unchanged on ledger but linked to R for view/proofs.
3. **Only AFTER R is `NORMAL_ACTIVE` may it optionally request and pair a BRAND-NEW, NEVER-FINANCIALLY-USED successor address C as `RECOVERY_RESERVED`** using the normal recovery association protocol (R Wallet Private Key + R's separate Authenticator, C BlackBox explicit ACCEPT, no key/link before Accept). The old S→R permanently consumed/successful recovery record stays immutable. R may now spend/send/receive like any main Wallet, and C remains unusable for ordinary actions until `RUN_DISASTER_RECOVERY(R,C)` makes R `DEAD`, C `NORMAL_ACTIVE`. This may recur (S→R→C→D...). A reserved R may **never** preconfigure C in advance of its own activation.
4. Never treat S/R as simultaneously ACTIVE or as cloned funds. The state machine must reject transitions, loops, recycled/used successor addresses, multiple reserved successor registrations that conflict, claims by R while reserved, old S signatures post-death, and chained recovery before predecessor is dead. Domain-separate every source+destination+epoch transition and consume one-use recovery secret atomically.
5. The term "same wallet" means a logically continuous user history and entitlement, **not identical private keys, not a shared live signing authority, not a ledger rewrite, nor a universal decryption backdoor**. Source S private key never becomes R's wallet private key.
6. What happens to original locked sends and late-created Sender K_S when S dies, plus strong pre-activation confidentiality of R's encrypted mirror, remain critical engineering OPEN. Never quietly claim those are solved by replication.

**Decision status:** 1-3 are explicit owner-confirmed UX/protocol direction. 4-6 are safety interpretation and unresolved engineering constraints. No running chain or audited cryptographic key migration exists.

## 2026-10-25 — Frozen Mirror access semantics confirmed by owner

Recovery target R **STARTS NORMAL** with independent key/BlackBox but must be fresh/never financially used before pairing. R BlackBox acceptance and BFT-final immutable S->R attachment **atomically freezes R** as `RECOVERY_RESERVED_FROZEN`. Only R's own narrow protocol/backup operations remain; no ordinary financial transaction or own business data. The reserved BlackBox continuously receives encrypted append-only mirrors of S's history, inbox, claim codes, requests, status, and proofs, but it displays no readable source plaintext before successful authorized disaster recovery.

On BFT-final `RUN_DISASTER_RECOVERY(S,R)` with original source key + R-issued one-use disaster recovery secret, S becomes DEAD and R becomes NORMAL_ACTIVE; backed-up ciphertext is verified/decrypted and appears in R, old ledger remains immutable with provenance links, and successor can set a new fresh recovery C. Do NOT release mirrors on an unrelated S DEAD state. Cryptographic unreadability requires not merely hiding UI but actual key-release control; a holder of complete decrypt key can read offline before recovery. Mechanism pending approval/audit. See [Recovery Mirror Protocol](RECOVERY_MIRROR_PROTOCOL.md).

## 2026-10-25 — LATEST: Recovery Mirror covers only Parent BlackBox, NEVER parent's transaction ledger

User clarified: a brand-new NORMAL wallet R is designated by main wallet S, R BlackBox ACCEPT BFT-finalises immutable recovery binding, R becomes `RECOVERY_RESERVED_FROZEN`. During S ACTIVE, R's BlackBox stores only S's continuously replicated **ENCRYPTED BlackBox contents** (claims, codes, requests, messages), with every record permanently tagged `Parent/Origin Wallet Address: S`, original event ID and other protected provenance. No R-specific ordinary financial operations, and no mirrored S plaintext readable/visible until authorized Disaster Recovery finality. **S's OLD blockchain transaction records must STAY on S forever, even once S is DEAD**: do NOT copy/transfer/reassign S historical transaction ownership or mutate immutable ledger entries. Authorized one-time recovery funds transfer of still-spendable balance is a distinct NEW ledger transaction, not transfer of historical entries. On recovery S DEAD, R NORMAL_ACTIVE and parent-tagged BlackBox archive readable, while R's fresh transactions belong to R. R may register fresh recovery C later.

No PRIVATE key, Authenticator Master Key, Claim Code, decryption key or recovery secret goes into public ledger, app telemetry, or server. If protocol uses an **ephemeral secret handshake**, generate locally, keep hidden even from owner, zeroize promptly; however absolute 'forever erased' guarantees depend on hardware and backups and cannot be assumed. **R's own signing key, protected one-use Disaster Recovery Key, and future restore/decryption capability cannot all be destroyed or recovery would be impossible.** Public/nonsecret verification commitments may still be essential for BFT and can reveal address relationships without privacy mechanisms. Enforced frozen spending and cryptographically enforced unreadability are separate problems; release of mirror decrypt material only after authorized recovery is OPEN and not claimed solved. Separate unresolved late K_S and 60-day sender reclaim/forfeiture safety unchanged. Details: [latest Recovery Mirror protocol](RECOVERY_MIRROR_PROTOCOL.md).
