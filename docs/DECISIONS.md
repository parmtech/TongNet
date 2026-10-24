# TongNet — Decision Register

> **LATEST OWNER REQUIREMENTS — 2026-10-25:** Trusted two-party P2P with no deal arbitrator; validators verify signatures/finality, not buyer/seller disputes. The RECEIVER has the first 24h (clock at final LOCK proposed, not yet ratified). The SENDER then has **60 DAYS**, replacing earlier 72h, to manually reclaim; after that, creator wants remaining unclaimed escrow sent to Network Reserve (OWNER INTENT, **REAL-MONEY DEPLOYMENT BLOCKED** by unresolved legal/consumer protection safety). A special *fresh*, zero-prior-financial-transactions RECOVERY_RESERVED address may complete recovery pairing metadata but CANNOT ordinarily send/receive before one-time disaster-recovery settlement. After successful recovery, S becomes DEAD and R is successor NORMAL_ACTIVE; owner wants historical receipts, BlackBox encrypted backup and pending entitlements shown in R, not destructive rewriting of immutable ledger. Preexisting recoverable encrypted BlackBox backup is REQUIRED to restore lost device data; a lost unbacked secret cannot be resurrected, and wallet/master root secrets must never be sent to a website server. Late sender claim key K_S with LOST/DEAD BlackBox, pending consent migration, exact 24h anchor, and legal forfeiture remain OPEN. See [canonical 2026-10-25 decisions](SECURE_P2P_V3_RECOVERY_DECISIONS.md). Older Trigger/72h/recovery-descriptions are HISTORICAL.


> **CURRENT RULE — 2026-10-25 (SUPERSEDES ALL OLD 3h TRIGGER CONTENT):** User REMOVED separate three-hour Trigger and its 3h automatic refund. Current TongNet Secure Manual P2P: Sender network-final LOCK -> Sender BlackBox makes and privately shares one-time Receiver Claim Code K_R -> exact addressed receiver wallet signs Claim Request -> Sender BlackBox must manually FINAL_ACCEPT exact transaction/recipient/amount -> BFT may finalise receiver settlement. No FINAL_ACCEPT means no receiver payout. No separate Trigger remains. Receiver 24h then Sender's following 72h manually redeemable via fresh Sender BlackBox K_S (verified attributable network delay extensions still apply); 24h from BFT-final LOCK is recommended but not explicitly ratified. No valid absolute guarantee against mistaken approval, stolen signing authority or third-party fraud. Old 3h Q7 disaster refund is obsolete; source DEAD + late K_S needs safe redesigned handling. See [canonical Secure P2P v2](docs/SECURE_P2P_V2.md) (for docs/ files: [canonical v2](SECURE_P2P_V2.md)).


**Convention:** `D-###` = recorded requirement/design decision. `OPEN-###` = undecided or verification-blocked item. User authority controls requirements; engineering feasibility, safety and law still need verification.

## Confirmed names, ownership and goals

| ID | Subject | Current record | Type |
|---|---|---|---|
| D-001 | Name | **TongNet**, replacing historical SIFAR Mesh | Confirmed |
| D-002 | Coin | **TONG** | Confirmed |
| D-003 | Product names | TongNet Wallet / TongNet BlackBox / TongNet Authenticator | Confirmed |
| D-004 | Shared network fund | TongNet Network Reserve | Confirmed name |
| D-005 | Attribution | ParmTech = project author/company; Manjinder Singh = original concept creator and developer | Confirmed |
| D-006 | Timeline | Concept conceived 2015, private until claimed first disclosure 2026 | Creator-stated, proof pending |
| D-007 | Principles | Strong decentralisation, high speed, low/zero user-visible fees, privacy, real TONG utility | Goals not verified |
| D-008 | Constraints | Avoid PoW mining, traditional PoS, single central controlling server | Design requirements |

## Wallet and authentication

| ID | Subject | Recorded requirement |
|---|---|---|
| D-009 | Provisioning | Create wallet and separate protected BlackBox at wallet creation |
| D-010 | Secret separation | Wallet credential, one-time authenticator enrollment credential and authenticator root secret are separate |
| D-011 | Enrolment | Earlier recorded rule: use wallet authority plus one-time setup secret, no BlackBox login required initially |
| D-012 | 60-second code | Authenticator generates rotating login codes; stable root secret does not rotate |
| D-013 | Access gate | Wallet-key compromise alone must not permit BlackBox operation/transaction trigger |
| D-014 | Activation | **User reconfirmed 2026-10-24 (Q2):** if TongNet Authenticator is not enrolled within 72h of wallet creation, the wallet becomes **permanently DEAD**, cannot ever reactivate, and cannot send, receive or claim. No owner/admin backdoor or reset after expiry. Any wallet requiring enrollment must be replaced with a newly generated wallet. |
| D-015 | Reset | Earlier recorded proposal: current authenticator secret plus wallet proof needed for re-enrolment of an already active wallet; this does **not** allow reviving a permanently DEAD wallet. Actual lost-master-secret policy remains OPEN-003. |

## Payment state machine — Latest known user requirements

| ID | Rule |
|---|---|
| D-016 | Sending a payment **locks** funds; initiation is not recipient settlement |
| D-017 | **SUPERSEDED:** independent Trigger removed. Sender BlackBox FINAL_ACCEPT for receiver Claim Request is the sole final release approval (2026-10-25). |
| D-018 | **OBSOLETE:** no distinct pre-trigger 3h period exists in Secure P2P v2. |
| D-019 | **REMOVED:** no 3-hour Trigger/automatic refund in Secure P2P v2. |
| D-020 | **LATEST:** Sender BlackBox creates Receiver Claim Code K_R on INITIATE/LOCK; receiver submits signed Claim Request; no separate Trigger. Proposed 24h starts after final LOCK, pending exact-clock approval. |
| D-021 | **2026-10-25 CONFIRMED:** Sender BlackBox generates Receiver Claim Code; Sender privately gives code to intended recipient. Final Trigger activates its usability for the cryptographically bound on-chain recipient only, NOT automatic plaintext delivery to Receiver BlackBox |
| D-022 | **2026-10-25 strengthened:** Receiver submits Claim Request within 24h after Trigger using K_R and bound wallet authority; FINAL receiver settlement additionally requires Sender's distinct signed ACCEPT in Sender BlackBox and network finality strictly within adjusted receiver deadline |
| D-023 | Sender cannot reclaim during recipient's 24-hour window |
| D-024 | **LATEST 2026-10-25:** following adjusted receiver 24h, a Sender K_S recovery right persists for **60 DAYS**, not 72 hours. Claim key issuance in lost/DEAD BlackBox remains engineering OPEN. |
| D-025 | One successful claim/refund consumes entitlement and must atomically prevent any competing payout |
| D-026 | **LATEST 2026-10-25 OWNER INTENT:** funds still unclaimed at adjusted receiver 24h + following 60 DAYS move to TongNet Network Reserve, NOT approved for real-money deployment absent user consent, jurisdiction-specific legal and safety/economic review. |
| D-027 | **HISTORIC 2026-10-24:** Trigger-based rights replaced by 2026-10-25 two-party manual final ACCEPT. Correct-code receiver cannot claim without authentic Sender approval. Already BFT-final approved transfer remains irreversible. |

## Historical/superseded

- Earlier receiver claim window: 60 minutes → replaced by **24 hours**.
- Earlier sender recovery: 3 days versus 7 days discussed → latest **additional 72 hours**.
- Earlier pre-trigger "cancel/refund now" proposal → explicitly rejected; **wait full 3h**.
- Earlier automatic sender return at end of sender recovery suggested → later user specified **reserve forfeiture after unclaimed 24+72h**; legality and consent **unresolved**.
- Earlier project name SIFAR Mesh → replaced by **TongNet**.
- Concept-origin year mistakenly listed 2016 → **corrected by creator to 2015**.
- AUD 1:1 peg discussed only as an **illustration**, not a confirmed tokenomics decision.

## Decision follow-up 2026-10-24

- **Q1 answered (Option B)**: Trigger is non-cancellable, even for mistyped/misdirected receiver addresses. This is a high-risk user-experience and loss scenario to clearly warn users about before Trigger. A receiver who validly claims the wrongly addressed payment can keep it according to these protocol rules; no guaranteed refund. No off-protocol administrator override is specified.

## Q2 confirmation — 2026-10-24

- **Permanent expiry:** If initial TongNet Authenticator activation is not completed inside 72h, wallet enters a terminal DEAD state; it never becomes ACTIVE later. A lost one-time setup key has **no regeneration/recovery route** to extend or bypass this deadline.
- **Protocol feasibility note:** Network can validate an activation deadline, but cannot directly detect physical loss of a key. DEAD means permanently unusable for normal transactions, not deletion of historical records. Since pre-activation receiving is blocked, wallet is intended to contain no funds. Define edge cases before production.

## Pending / blocked decisions

| ID | Priority | Question / problem |
|---|---|---|
| CLOSED-001 | **ANSWERED 2026-10-24** | Option B confirmed: after a successful Trigger, sender CANNOT cancel or emergency-stop the transaction, even if recipient address is wrong. Receiver 24-hour window remains valid; if no receiver claim, sender gets the next 72h for recovery. |
| CLOSED-002 | **ANSWERED 2026-10-24** | User chose **permanently DEAD** if never enrolled within 72h. No reissuing lost initial Setup Key to save that same wallet under the agreed rule. After expiry no key, support agent or administrator can activate it again. A new wallet is needed. |
| CLOSED-003 | **ANSWERED / REFINED 2026-10-24** | Optional TongNet Disaster Recovery Wallet in normal Wallet settings, NOT BlackBox. Run Disaster Recovery requires **original Wallet Private Key + distinct one-use Disaster Recovery Key**, NO BlackBox/Authenticator. Atomic sweep of eligible balance (less actual fee) to immutable preconfigured destination; old wallet permanently DEAD. Triggered escrow/sender-claim treatment confirmed Q6; untriggered 3h refund destination decided Q7 (Option A). |
| CLOSED-016 | **Q5 ANSWERED, Option A (2026-10-24)** | INITIAL one-time Disaster Recovery Wallet destination registration requires **both Wallet Private Key proof and TongNet Authenticator approval**. A wallet key alone must not configure it. After that the registered address and one-time Disaster Recovery Key are permanently immutable. |
| CLOSED-019 | **ANSWERED 2026-10-24** | Optional one-use Disaster Recovery Key is issued when destination is first configured; Run Disaster Recovery requires BOTH Wallet Private Key **and** Disaster Recovery Key, but NO BlackBox/Authenticator code. Key consumed once and source wallet permanently DEAD after atomic sweep. |
| D-028 | **CONFIRMED — IMMUTABILITY** | Once set, disaster destination address and Disaster Recovery Key can NEVER be changed, reset, regenerated or replaced. If disaster key is lost, this feature cannot be used. If Wallet Private Key and Authenticator Master Key both remain, normal transactions to another wallet may continue; old recovery configuration remains unchanged. |
| CLOSED-017 | **Q6 ANSWERED — Triggered Escrow (2026-10-24)** | Disaster Recovery immediately sweeps **only unlocked/spendable balance** to the fixed recovery address and marks original wallet DEAD; a previously triggered transaction stays locked; receiver can claim for full 24h after Trigger. If not claimed, during the next 72h sender recovery window the original one-use **Sender Claim Key** may be submitted via the pre-bound Disaster Recovery Wallet **ONLY after Run Disaster Recovery completed**. Missing sender claim key cannot be bypassed; one-time proof, recipient binding and timeouts persist. Pre-trigger pending state unresolved separately. |
| CLOSED-020 | **Q7 ANSWERED — Option A (2026-10-24)** | If original source wallet completes Run Disaster Recovery and becomes permanently DEAD while a transfer remains untriggered in the 3h PENDING_TRIGGER period, its lock remains until original t0+3h. At expiry, normal automatic refund pays **directly to immutable pre-bound Disaster Recovery Wallet**. Disaster Recovery does not wait; no early cancellation or Trigger after DEAD. Atomic deadline ordering and no-double-spend required. |
| OPEN-021 | **REFINED AFTER Q8 / CRITICAL** | Destination BlackBox key generation has been specified, but whether destination private-key signing or explicit acceptance is mandatory remains unresolved; see Q9. |
| D-029 | **Q8 + Q9 REFINED, CONFIRMED 2026-10-24** | Source first SENDS a recovery-pairing request via ordinary wallet Settings and source Wallet Private Key + Authenticator. Only on destination wallet **ACCEPT** from destination BlackBox is one-time **Disaster Recovery Key generated there** and source→destination binding irrevocably configured. If REJECTED or still PENDING, NO key, NO final binding and recovery is NOT configured. Key later works once with source Wallet Private Key; no source Authenticator needed to execute. |
| CLOSED-022 | **Q9 ANSWERED 2026-10-24** | Initial source Wallet settings request (source Wallet Private Key + TongNet Authenticator) arrives in destination R BlackBox. Until R **ACCEPTS**, pairing remains PENDING, not configured; **NO recovery key** is issued. On R ACCEPT, generate unique one-use Disaster Recovery Key **in R BlackBox** and make S→R association permanently immutable. On REJECT notify S BlackBox, no configuration/key. With no answer keep pending/not configured. |
| CLOSED-023 | **Q10 ANSWERED — Option A (2026-10-24)** | An unaccepted/unrejected Recovery Wallet pairing request expires automatically after **24 hours**. PENDING and EXPIRED mean NOT_CONFIGURED, no irreversible S→R binding and no Disaster Recovery Key. Late Accept after expiry is invalid. Deterministic time and race enforcement require engineering. |
| CLOSED-024 | **Q11 ANSWERED — Option B (2026-10-24)** | A source wallet **CANNOT cancel, withdraw, replace or redirect** a PENDING recovery association request. It must wait for target recovery wallet REJECT or automatic EXPIRED at 24h before making a fresh request. ACCEPT during validity finalizes the permanent link and one-use key, preventing any later changes. PENDING stays NOT_CONFIGURED. |
| CLOSED-025 | **Q12 ANSWERED — Option A (2026-10-24)** | **STRICT FINALITY DEADLINE:** R BlackBox ACCEPT must be **network-finalized strictly before original request creation + 24h**. A signed/tapped/submitted/network-received ACCEPT that only attains finality after the cutoff is invalid; request EXPIRED. No link/Disaster Recovery Key issued. Local device time never decides validity. Consensus clock, boundary and partitions not yet implemented. |
| PARTIAL-026 | **Q13 DIRECTION CONFIRMED (2026-10-24), FULL-OUTAGE EDGE CASE OPEN** | User wants already-started timers independent of network congestion, no pause just because slow/fast. New submissions can be QUEUED under load; a new transaction timer starts **only after network ACCEPTANCE**, not client click or queue admission. Recommended define acceptance as consensus finality, not mempool acknowledgment. Whether already-running receiver/sender windows during a total outage may expire into reserve remains an explicit open safety/legal decision. |
| CLOSED-027 | **Q14 ANSWERED — Option A (2026-10-24)** | A RECEIVER's 24h Claim or SENDER's subsequent 72h Claim must be **fully network-final strictly BEFORE its existing deadline**. Submission/signing/queue admission or third-party early receipt is insufficient. Late-finalized Claim EXPIRES; cannot retroactively defeat any already valid next-stage entitlement. Canonical consensus ordering, expiry and replays still require tests. |
| CLOSED-028 | **Q15 ANSWERED — UNIVERSAL NETWORK DELAY CREDIT (2026-10-25)** | Network must calculate its own attributable processing/congestion/outage delay and grant **equal extra time** to EVERY affected time-limited operation: Send/Trigger, receiver Claim, sender reclaim, Disaster Recovery request/Accept, and other timed tasks. This is one-for-one extension of the **effective deadline** while physical timer cadence stays unchanged. Network-finality strictness (Q12/Q14) applies before **adjusted deadline**. Exact calculator, delay attribution and abuse-proof consensus remain OPEN Q16; do not auto-forfeit escrow to Reserve before legitimate adjusted rights finish. |
| CLOSED-029 | **Q16 ANSWERED (2026-10-25), C HYBRID DELAY CALCULATOR** | User chose BOTH verifiable per-operation processing delay and global network congestion/outage evidence. Apply attributable delay one-for-one to EACH eligible timed operation with exact-once overlap accounting; do not blindly add individual+global duration. Fault proofs, network time, spoofing defence, protected resolution remain engineering research. |
| OPEN-018 | High | Destination address confirmation, ownership proof, attack resistance, atomic sweep and fees. Address changes are prohibited; no change-delay rule applicable. |
| OPEN-004 | Critical | If both wallet and second factor compromised: theft prevention, freeze and dispute controls? |
| OPEN-005 | Critical | Consensus algorithm and finality without PoW/traditional PoS or central trusted operator |
| OPEN-006 | Critical | Sybil, double spend, partitioning, censorship, replay, validator incentives and spam defence |
| OPEN-007 | Critical | Protocol-enforced BlackBox key separation, non-phishable authorisation and secure inbox delivery |
| OPEN-008 | Critical | Legal ownership, explicit consent, unclaimed-property laws and feasibility of reserve forfeiture |
| OPEN-009 | Critical | Native TONG issuance, real value, redemption, reserve custody, regulatory treatment |
| OPEN-010 | High | Fee funding, network economics and anti-abuse without simply pushing costs elsewhere |
| OPEN-011 | High | Exact timeout boundaries, clock skew, network outages and recovery/trigger races |
| OPEN-012 | High | Device loss, secure multi-device support, migration and independent backup |
| OPEN-013 | High | Public repository/release strategy, ownership evidence, patent and licence assessment |
| OPEN-014 | High | Privacy guarantees vs mandatory transaction-state data and compliance |
| OPEN-015 | Medium | Availability guarantees, messaging routing and validator performance targets |

**After each answer:** append a dated change, update corresponding open/closed items, FAQ, PROTOCOL, PROGRESS, NEXT_SESSION and CHANGELOG. Never silently remove a contradictory older decision.

## Q3 clarification — Three separate keys (2026-10-24)

- **Confirmed:** (1) Wallet Private Key, (2) TongNet Authenticator Master Key, (3) optional Disaster Recovery Key if recovery is enabled.
- **Recovery wallet address is not itself the Disaster Recovery Key.** Keep both conceptually separate.
- **Resolved:** the third key is generated on registering disaster address and required *together with* Wallet Private Key to Run Disaster Recovery; can be used once. No BlackBox/Authenticator is needed for execution.
- **Resolved:** Recovery destination and recovery key are immutable from initial setup; losing this key permanently disables this particular recovery path. Standard send may still work with both Wallet Private Key and Authenticator Master Key.
- **Q5 resolved:** First-time immutable setup requires **Wallet Private Key + TongNet Authenticator**, Option A. Q6 confirmed behaviour for previously TRIGGERED locked funds; Q7 resolved for still-untriggered 3h locks: expiry refund to linked disaster destination after source DEAD.

## Q3 — Disaster Recovery Wallet (2026-10-24)
- Optional, pre-registered second wallet address in ordinary wallet settings.
- Recovery executable using **Wallet Private Key AND one-use Disaster Recovery Key**, without BlackBox or Authenticator factor.
- Sweep entire eligible source balance to fixed destination less any applicable fee, then permanently DEAD source wallet.
- **Q5 protection:** an attacker with only a stolen Wallet Private Key **cannot authorise initial recovery destination setup**, because independent TongNet Authenticator approval is mandatory. Multi-factor compromise and misleading displayed address remain risks. Once registered, destination and key are immutable.
- **Q6 resolves triggered transfers:** locked funds stay escrowed; receiver rights remain; same transaction-bound sender Claim Key can be used from already-linked recovery wallet only after original source has finished disaster recovery. Sender recovery is NOT automatic and remains key-gated. Pre-trigger 3h auto-refund routing decided Q7: expiry refund directly to pre-bound destination after source DEAD. See [DISASTER_RECOVERY.md](DISASTER_RECOVERY.md).

## Immutable disaster backup rule — confirmation 2026-10-24

- User explicitly ruled out changing the recovery address or recovering/changing the once-generated key under any circumstances after initial setup.
- Lost disaster key means disaster recovery cannot run. If both normal wallet and Authenticator secrets survive, user may use ordinary transactions to move their funds elsewhere, but cannot change the configured disaster address/key.
- User requires Run Disaster Recovery to consume the single-use disaster secret and terminally kill the wallet.
- **Q5 RESOLVED:** initial once-only recovery destination setup requires both Wallet Private Key and TongNet Authenticator (Option A). **Q6 RESOLVED for triggered escrow; Q7 RESOLVED for untriggered locks** (3h expiry auto-refund to pre-bound disaster wallet after DEAD). **NEXT Q8:** recovery destination proof of control at initial setup.

## Q5 — Initial immutable disaster address enrolment (answered 2026-10-24)

**User chose Option A:** Initial enrollment of the optional one-time disaster destination **MUST be authorized by BOTH the source Wallet Private Key and independent TongNet Authenticator**. No future address change or disaster key reset; disaster execution later still requires source Wallet Private Key plus once-only Disaster Recovery Key (without Authenticator). Cryptographic binding of the authorization to displayed destination address and replay prevention are engineering requirements, not implemented proof.

**Q6 RESOLVED for triggered escrow; Q7 RESOLVED for pre-trigger automatic refund:** original expiry still applies and funds credit immutable pre-bound rescue address after source DEAD. **NEXT Q8:** prove ownership/control of the recovery destination at first setup.

## Q6 — Disaster Recovery with previously Triggered escrow (confirmed 2026-10-24)

- **Immediately sweep available funds only.** Example 1,000 total; 700 available and 300 already Triggered/locked. Recovery moves 700 (less actual fee) to immutable rescue wallet; leaves 300 escrow and receiver rights intact. Source becomes permanently DEAD.
- **Receiver's 24-hour claim window** after Trigger is NOT cancelled, shortened, or overridden. A successful receiver claim is final.
- **Sender's additional 72-hour recovery window:** if receiver does not claim, a holder of the **same original transaction-bound unspent Sender Claim Key** may claim **to the original wallet's cryptographically pre-bound Disaster Recovery Wallet**, only if the source wallet's Run Disaster Recovery was finalised beforehand. No fresh sender claim secret is minted for this shortcut. Claim is one-time and subject to original expiry. The recovery wallet must prove control of its address; network verifies original consent/binding, not real-world identity.
- **If user cannot present Sender Claim Key, there is no claim bypass from disaster recovery**, even though wallet became DEAD. After the 72h window, user's controversial proposal for transfer to Network Reserve remains under legal/consumer review.
- **Q7 RESOLVED:** Existing still-untriggered 3h locks remain untouched until original timer expiry. With DEAD source from completed disaster recovery, auto-refund goes directly to prebound recovery wallet; no manual cancel, no accelerated refund or Trigger after DEAD.
- **Formal proof required:** no stolen cross-wallet sender claim, no double-settlement, destination binding, time-of-trigger vs time-of-recovery ordering, and atomic DEAD state finality.

## Q7 — Untriggered lock and irreversible source recovery (confirmed 2026-10-24)

**Option A confirmed:** If Run Disaster Recovery finalized, original source S becomes permanently DEAD while an earlier Send is still PENDING_TRIGGER, the previously locked amount stays escrowed until its original t0+3-hour no-trigger deadline. On deadline, **automatically refund to R**, the same originally registered immutable disaster destination. Recovery doesn't pause for this lock and doesn't cancel it early. DEAD S cannot issue a new Trigger; transactions triggered and final **before** DEAD follow Q6's receiver-claim path instead. Atomic ordering of Trigger/DEAD/timeout needs formal verification.

**Next Q8:** At permanent R registration, require a cryptographic signature from R proving wallet control/consent, or source-key + Authenticator approval and visible address confirmation alone?

## Q8 — Destination-side Disaster Recovery Key generation (2026-10-24)

The user clarified that at the initial irreversible association of SOURCE wallet S to Disaster Recovery Wallet R, the single-use Disaster Recovery Key must be **generated within R's own TongNet BlackBox only AFTER R explicitly ACCEPTS the incoming pairing request**, never during mere request initiation and never inside S's BlackBox. The exact SAME generated key authorizes later Run Disaster Recovery, together with S's Wallet Private Key. Registration still requires S's Wallet Private Key and S's TongNet Authenticator per Q5. Later recovery needs neither S's BlackBox nor Authenticator. Generation and availability of the key inside R's private encrypted vault are required; public ledger retains only binding/key verification commitments, NOT plaintext secrets.

The user's Q8 answer establishes destination-side custody, NOT by itself an explicit signature with R's Wallet Private Key or proof that S and R have the same real-world owner. **Q9 ANSWERED:** R MUST explicitly ACCEPT request inside R BlackBox before immutable registration and key generation. REJECT delivers a failure response to S BlackBox; ignored requests remain pending and count as NOT_CONFIGURED. **NEXT Q10:** request expiry if R never responds.

## Q9 — Two-party disaster setup handshake (confirmed 2026-10-24)

The S wallet owner submits a recovery-wallet association request from S normal wallet settings using S Wallet Private Key + S TongNet Authenticator (Q5). This only puts the request in R's encrypted BlackBox as PENDING: **no active Disaster Recovery**, no one-time key, no irreversible link yet.

R opens its own BlackBox and decides. **ACCEPT**: generate the unique unchangeable one-time Disaster Recovery Key **inside R's BlackBox**, and permanently attach R as S's recovery destination (single final registration). **REJECT**: create no key or binding, send a rejection/status message to S's BlackBox. **IGNORE/PENDING**: no key or binding; S treated as lacking configured disaster recovery. If neither ACCEPT nor REJECT is finalized within 24h, the unanswered request automatically EXPIRES. No binding or key; stale Accept is rejected. Treat the accepted association as irrevocable; receiver consent should be verifiable and bound to request ID and source/target addresses, without proving real-world shared identity.

**Q10 CONFIRMED (Option A):** automatic EXPIRED at 24h without destination Accept/Reject; PENDING/EXPIRED count as NOT_CONFIGURED; no key/binding. **NEXT Q11:** May S cancel/replace an unaccepted pending request before 24h expiry? Immutable accepted configuration remains untouchable.

## Q10 — Recovery pairing request expiry (confirmed 2026-10-24)

- **Option A:** Once the recovery pairing request exists, R has at most **24 hours** to ACCEPT or REJECT it through R BlackBox. The original S→R recovery relationship is still NOT_CONFIGURED throughout PENDING.
- If no accepted action finalizes before the 24h boundary, the request is **EXPIRED** automatically. No Disaster Recovery Key ever issues on expiry, and no immutable pairing is created.
- A late ACCEPT of an already EXPIRED request must be rejected by the network. Duplicate/replayed request actions may not issue a key or reactivate it.
- The 24h starts from network-acknowledged request creation/finality as a practical protocol assumption; the exact network clock and simultaneous acceptance ordering still need design/tests.
- If R REJECTS, original rejection notice to S BlackBox remains the applicable rule, independent of automatic expiry. No new request/resubmission policy has been decided.
- **Next Q11:** Can original S withdraw or replace still-PENDING request before R's acceptance, rather than wait for 24h expiry or R's rejection?

## Q11 — Pending disaster recovery request cannot be cancelled (2026-10-24)

- **Option B confirmed:** While the request remains PENDING_ACCEPTANCE (max 24h), the source Main Wallet cannot manually cancel, withdraw, change the recovery destination or supersede its request with another.
- Source must wait for destination BlackBox REJECT or original 24h automatic EXPIRED to submit a fresh separate setup request. Until ACCEPT, disaster recovery is NOT_CONFIGURED and no key or binding exists.
- If recipient ACCEPTS while valid, immutable pairing and destination-BlackBox one-use recovery key are created. This cannot be changed thereafter.
- No admin override. Rejected/expired attempts are not permanently registered; they may be followed by a fresh request with source Wallet Private Key + TongNet Authenticator approval. Distinguish these from post-acceptance immutable setup.
- **Q12 resolved, Option A:** only network-finalized destination ACCEPT **before** the request's 24h deadline is valid; any later finality is EXPIRED, regardless of early button press or message arrival. **NEXT Q13:** network-wide outage while sender/receiver claim windows run.

## Q12 — Strict confirmation finality before recovery-pairing expiry (confirmed 2026-10-24)

- User chose **Option A**. The original request's 24h timer is strict; the destination's ACCEPT must acquire definitive **network finality before expiry**. It is insufficient for a person to tap Accept, a device to sign it, or a relay to receive it before expiry if the network finalizes it afterward.
- Late-finalized approval must NOT issue the one-time Disaster Recovery Key, create immutable S→R registration, or convert EXPIRED back to ACCEPTED. PENDING/EXPIRED still count as NOT_CONFIGURED.
- A deterministic decentralized ledger/network time and explicit boundary rule (strictly before, not exactly equal) are needed for implementation; network outages and dishonest validators may make this strict deadline costly for users. Do not claim finality technology currently exists.
- **NEXT Q13:** should payment Claim windows and proposed reserve forfeiture continue to elapse during substantial network outages, or should they pause in a protocol-verifiable way? This is separate from Q12's recovery-pairing deadline.

## Q13 — Queue-first network admission and independent timers (user direction 2026-10-24)

**Confirmed intent:** (i) timer elapsed time must not speed up/slow down with network load; (ii) accept incoming tasks into bounded queues during congestion; (iii) only after the *network accepts a new transaction* does its own applicable timer start; (iv) load-balancing and queue management are desirable.

**Engineering recommendation, NOT separately user-authorized protocol finality:** Distinguish CREATED_LOCAL → QUEUED_NONFINAL → ACCEPTED_FINAL, with timestamp t_accept from decentralised consensus finality. Do NOT reserve/spend funds, mint claim credentials, create irreversible pairing, or start newly created payment windows merely because a relay queued a message. Enforce existing claim deadlines with separately agreed expiry checks on finality. Existing Q12 already requires strict finality *before deadline* for disaster-pairing ACCEPT; it does not automatically decide payment claim timing.

**Unresolved consequential issue:** During full network outages, claims already in their 24h/72h windows may be unable to finalize. Queuing doesn't pause an already-running timer or prove timely claim. A timeout-to-network-reserve forfeiture under such circumstances is a serious user-loss, legal and consensus-safety launch blocker. Next Q14 asks for a direct decision about queued claims near deadline; full-outage/forfeiture policy still needs explicit confirmation.

## Q14 — Strict finality for financial Claims (confirmed 2026-10-24)

- User chose **Option A**, distinct from but consistent with the earlier Q12 pairing rule: if a receiver CLAIM fails to reach network consensus finality **strictly before its 24-hour deadline** after Trigger, that Claim is expired, even if it was signed/queued/received earlier. The sender's original subsequent 72-hour recovery interval retains its priority as already designed.
- The **same rule applies to the sender's 72-hour one-time reclaim**: must reach finality strictly before the sender window expires. Neither queue admission nor pre-deadline relay receipt reserves the claim or extends the deadline.
- New transaction timers begin at network acceptance/finality under the proposed Q13 architecture; Q14 deals only with a **pre-existing running deadline**. Consensus must accept at most one mutually exclusive receiver claim, sender reclaim or later reserve disposition, with a verifiable total order and no stale queue replay.
- **CRITICAL UNRESOLVED:** A complete network outage might preclude valid claims for the whole remaining window; that risks loss of funds under the earlier proposed reserve-forfeiture plan. Q15 asks about post-outage escrow treatment **without silently suspending the fixed timers**. Do NOT deploy forfeiture with real funds absent legal/consumer-protection advice, explicit informed consent, and robust liveness security.

## Q15 — Universal 1:1 TongNet Network Delay Compensation (2026-10-25)

**User clarification expands the rule beyond claims:** ANY time-sensitive TongNet operation affected by actual network slowness/backlog/outage should receive an **additional time allowance equal to the network-attributable delay calculated by a Network Delay Calculator**. This includes outgoing Send/Trigger, receiver 24h Claim, sender following 72h Claim, disaster recovery pairing/request/BlackBox Accept, and any other real operation with a deadline. Timers maintain normal real-time cadence, but the **effective allowed deadline is extended by exactly credited network delay**, not arbitrarily paused or slowed.

**Interaction with prior confirmations:** Q12 strict network-finality before pairing Accept deadline and Q14 strict network-finality before financial Claim deadline remain valid, now relative to the properly **extended effective cutoff**. A queue ticket, signed local action, or submitted transaction is not itself finality. Q13 says a brand-new transaction timer begins only on actual network acceptance; queue waiting BEFORE that start must not automatically also be credited against the newly started timer (avoid counting one period twice; precise edge-case formula open).

**Conservation and fairness:** When receiver Claim time is extended, defer the exclusive sender 72h window and downstream reserve date consistently; if source's 3h Trigger timeout is extended, no automatic refund/receiver rights can conflict with valid Trigger. When disaster setup's 24h deadline is extended, an ACCEPT finalized within its legitimate adjusted cutoff may still attach R; never create credentials from queued events. No double claims or refunds. Hold escrow while a legitimate credit can alter entitlement; automatically forfeiting to reserve at unadjusted t+96h would contradict the user's new rule and remains a legal/consumer protection blocker.

**OPEN Q16:** exact network-wide versus operation-specific delay calculation, network truth source and anti-manipulation. No consensus implementation or verified Delay Calculator exists yet; different wallets must not be able to invent extra time by offline devices or deliberate spam.

## 2026-10-25 — User-confirmed Q16–Q25 and updated long-term objective

**Status:** Confirmed design requirements only; validators, blockchain, Delay Calculator, BFT safety and security audits have NOT been implemented.

- **Q16 — Option C:** HYBRID delay calculator: independently verifiable per-operation network delay **and** verifiable global network health; overlap must be counted ONCE, not summed twice. Apply universal Q15 exact-one-to-one eligible extensions to every time-sensitive operation.
- **Q17 — Option C:** cross-check multiple independent node proofs to reject invented or deliberately injected delay.
- **Q18 — Option C:** cryptographically authenticated consensus on delay evidence; if delay entitlement cannot safely be established, keep affected funds in PROTECTED_SUSPENSE instead of conflicting payout/reserve settlement; this needs a liveness-safe, rigorously specified exit mechanism.
- **Q19 — Option C:** verifiable decentralised anti-Sybil eligible validator committees; do not mistake distinct keys or raw node count for independent identity.
- **Q20 — Option C:** staged hybrid evolution from independently verified initial validators to progressively open permissionless participation ONLY after robust independent anti-Sybil proof and audits; early phase is not fully permissionless.
- **Q21 — Option C:** evidence/rule-based **fully automated** validator admission/removal, no discretionary single-owner overrides.
- **Q22 — Option B:** provable suspicious activity may cause temporary quarantine, with objective investigation and restoration if innocent or removal if misconduct proven; don't treat mere offline time as incontrovertible fraud.
- **Q23 — Option B:** automatically activate previously eligible standby validators whenever the existing consensus membership rules can safely authorise this; otherwise halt new finality.
- **Q24 — Option C:** partition safety via cryptographic quorum; group without quorum cannot independently finalise. No double-spend/irreversible conflicting forks for availability.
- **Q25 — Option B:** backup rotation preverified/authorised ahead of partitions, but NEVER permit two conflicting independent quorums; if safe epoch transition cannot be proved, fail closed.
- **User's latest design mandate:** best feasible high-throughput and secure future-proof network; no pure Proof-of-Work mining required; pure wealth-based Proof-of-Stake is not preferred but a hybrid PoS-like eligibility/bond **is allowed**. Aim for no single-party/cloud/vendor settlement dependency and extremely low or zero *visible* end-user fees **where sustainably feasible**. Every component must have a defensible purpose; differentiate honestly, without claims of unproven novelty.
- **Architecture recommendation vs confirmed mandate:** candidate TongNet Quorum Fabric, mature deterministic BFT core, hybrid cryptographic/operational/bond eligibility, parallel ingress/execution, delayed deadline proofs, sponsored transaction quotas, upgradeable cryptography. Full design in [TONGNET_FUTURE_ARCHITECTURE.md](TONGNET_FUTURE_ARCHITECTURE.md); all 95 answers in [MASTER_QA_RECOMMENDATIONS.md](MASTER_QA_RECOMMENDATIONS.md).
- **Hard distinction:** The user permitted architectural reconsideration, but did not specifically authorise replacing the previously confirmed irreversible wallet conditions or automatic reserve-forfeiture intent with a new property-rights policy. Proposed protections must remain plainly labelled RECOMMENDATION/LAUNCH BLOCKER until accepted and reviewed.

## 2026-10-25 — Primary implementation language, selected under owner-delegated choice

**Owner instruction:** "Jo best hai oh I chuno language" — choose the best language for TongNet rather than require owner to select C/Rust/etc. **Decision: RUST as the primary language for TongNet Core.** Selected by the assistant under delegated technical-design authority; this is NOT a claim that a chain/compiler project has been implemented or audited.

- Write consensus/state transition/validator membership, node P2P/networking, ledger storage integration, mempool, delay calculator, transaction verification, BlackBox/Authenticator shared cryptographic logic and wallet core in idiomatic safe Rust wherever feasible.
- Explicit and narrowly reviewed `unsafe` only for unavoidable audited FFI/platform-specific work; don't assume Rust makes consensus or protocol logic correct. Require property/fuzz testing, sanitizers as applicable, reproducible pinned builds, third-party cryptography audits and independent security review.
- Cross-platform Rust libraries reused on Linux/Windows/macOS/Android/iOS; native user-interface bindings as appropriate (Kotlin on Android, Swift on iOS, TypeScript/WebView or native desktop as evaluated). These UI layers are NOT a reason to duplicate the financial state machine in another language.
- C/C++ may be used only for audited, technically justified platform interoperability with narrow interfaces; no blanket '100% Rust including every third-party dependency' promise.
- No single remote SaaS dependency for base settlement; mature cryptographic/open-source libraries are permitted and should be licence-audited and pinned. Language selection by itself doesn't prove superior performance, decentralisation, low fees or security.
- Canonical review: [TongNet Future Architecture](TONGNET_FUTURE_ARCHITECTURE.md). **Implementation status: NOT STARTED / no evidence of build or benchmarks.**

## Product review reference — 2026-10-25

[Critical Product and Banking Adoption Plan](TONGNET_PRODUCT_CRITIQUE_AND_ADOPTION_PLAN.md) recommends a separate Instant Pay transaction type to enable normal merchant checkout, without altering confirmed Protected Pay rights. Instant Pay, sample 1B TONG denomination, fiat/stablecoin partnerships and reserve reforms are proposals, NOT confirmed rules. Real-money release remains blocked pending safety and legal reviews.

## 2026-10-25 — CONFIRMED product correction: manual two-party P2P, NOT Instant Pay

**User instruction (clear and later than the instant-pay suggestion):** "Instant wale bahut system ne asi ehnu p2p secure system bna the aa not instant but ek fast manual treeka jithe receiver te sender dona nu kujh krna pve." TongNet is intentionally a **fast, manual, two-party-authorised secure P2P payment protocol**, not an instant-payment default/competing checkout coin. Previous assistant proposal to introduce/enable `Instant Pay` or make it the default is **SUPERSEDED AND NOT AUTHORISED**; do not implement it under current scope.

**Keep user-confirmed Protected P2P sequence:** sender initiates Send and network-final escrow lock; sender personally approves Trigger using independent BlackBox/authentication; addressed receiver personally Claims using its own BlackBox one-use Claim Key. Both parties act before final recipient settlement. No waiting requirement: if both are available they may complete the independent authorisations right away, subject to actual consensus latency. Original **maximum 3h before Trigger, receiver up to 24h to Claim, then sender-only next 72h** remain, with eligible Q15–Q18 one-for-one verified network delay extensions. Before Trigger auto-refund on adjusted 3h no-trigger expiry; after Trigger no sender cancellation, even wrong address; Claim strict finality before adjusted receiver deadline. Never promise seconds to finality without measurements.

**Wrong-address protection to investigate, NOT yet chosen by user:** propose a receiver-created, independently signed **one-use Receive Request (public payment invitation, not a private wallet key and NOT the Claim Key)** bound to destination wallet public key, unique request ID, optional amount and expiry. Sender must verify cryptographic binding, show full recipient fingerprint/details and manually approve exact operation; Trigger still separately signed; only receiver's BlackBox gets the separate confidential Claim Key on Trigger. A malicious party can still sign a legitimate request under the wrong identity and socially engineer approval; signatures prove key control, not real-world recipient identity. Whether a signed Receive Request is mandatory for all Send operations or optional (with warnings on manually-entered addresses) is NOT YET ratified.

**Adoption focus revised:** secure interpersonal escrow-like peer-to-peer exchanges, explicit bilateral authorisation and robust wrong-recipient defenses rather than frictionless cashier checkout or banking-rail competition. Banking/merchant modules are future research, not a change to product's chosen security-first operation. Existing 20-question market critique is historically valuable, but its recommendation for `Instant Pay` is explicitly rejected for present scope. `docs/TONGNET_PRODUCT_CRITIQUE_AND_ADOPTION_PLAN.md` must be read together with this newer decision.

## 2026-10-25 — NEWER USER-CONFIRMED RULE: Both payment Claim Keys originate in the SENDER BlackBox

**This rule explicitly SUPERSEDES older language that delivered/generated receiver Claim Key inside Receiver BlackBox or automatically delivered the key to R. It does NOT change the unrelated Disaster Recovery Key, which remains generated inside the Recovery DESTINATION's own BlackBox only on accepted recovery pairing.**

**Confirmed operation:** At transaction initiation, source Sender BlackBox generates/displays the unique **Receiver Claim Code K_R**, tied to exactly (TongNet chain, transaction ID, selected receiver address/public key, amount/asset, operation, expiry). Sender explicitly gives K_R to intended receiver by a private/out-of-band channel. The selected on-chain RECEIVER address, **not merely the person holding the code**, must independently authenticate and prove control of its wallet to claim. Sending/witnessing a code never credits funds by itself. Preserve existing separately authenticated sender BlackBox Trigger: after a successful network-final Send lock and final Trigger within the 3h window, K_R becomes exercisable for the receiver's **24h nominal** window, with Q15 verified eligible network delay adjustment. Generating K_R at Send is NOT payment settlement and its validity clock still begins on final Trigger. If no final Trigger, auto-refund after adjusted pre-trigger expiry; no receiver payout. Receiver need not create the code and network must NOT automatically supply plaintext K_R to whichever destination address Sender typed. Sender must deliver it to intended receiver.

**Next window:** At the end of receiver's adjusted 24h exclusive priority, the receiver entitlement becomes EXPIRED and **a fresh, transaction-specific Sender Reclaim Key K_S is generated in the SENDER's BlackBox**, accessible to/usable only by authenticated original Sender, never by Receiver. K_S is only valid in the following nominal **72h** (extended solely for eligible verified network delay). Sender must manually reclaim using valid K_S **plus original sender authority**, or after previously completed Disaster Recovery, the already confirmed immutable linked Recovery Wallet path IF its necessary original-claim-proof rules can be satisfied. K_S expires strictly at its adjusted expiry. No automatic full refund after 24h Triggered receiver nonclaim: rather funds become sender-claimable for next 72h. Existing user-proposed network-reserve allocation after total post-Trigger 24+72h remains legally/ethically blocked for real-money rollout.

**Wrong address failure analysis:** Sender intended wallet A, but transaction cryptographically binds to mistyped wallet B. If Sender sends K_R to A, A cannot redeem because A lacks B's wallet authority; B cannot redeem without K_R. After receiver window expires, original Sender can use K_S in the next 72h to reclaim. If B obtains K_R (through code theft, intentional sharing or phishing), B can claim before expiry. No system can guarantee refunds if both credentials satisfy the wrong recipient transaction.

**PROTOCOL ENGINEERING OPEN / conflict with earlier Q6:** Previous specification said the Sender Claim Key already existed before 24h and could be used even after Source S became DEAD by Disaster Recovery. Newly confirmed **late key generation in Sender BlackBox** conflicts with successful prior disaster recovery or lost/compromised Sender BlackBox before the 24h boundary. Do NOT silently replace the user's "new key after 24h" timing. Candidate solutions needing confirmation and formal verification include (A) Sender BlackBox generates fresh K_S after expiry while online and cannot reclaim if destroyed, OR (B) precommit an authenticated, encrypted, future sender key/derivation at Trigger, only cryptographically UNSEAL/ACTIVATE it once receiver window expires, including recovery-wallet handling. B preserves prior Q6 protection better but changes the literal issuance time. Network must not mint plaintext K_S or know secret by itself. Also prove secure commitment update at boundary, no claim if key issuance commitment missing, anti-replay, receipt binding and no permanent frozen funds.

**Naming:** Ordinary transaction keys K_R and K_S are NOT Wallet Private Keys, Authenticator/BlackBox master secrets, disaster-recovery keys, or a receiver-generated Receive Request. An extra signed Receive Request may still be a future optional defense but is NOT required/approved by this correction; do not assume mandatory upfront receiver request. The new flow is user-confirmed requirement only—not an implementation, audited code or measured performance.

## 2026-10-25 — USER-CONFIRMED: Sender's final BlackBox ACCEPT is mandatory after Receiver CLAIM REQUEST

**Owner scenario:** Sender and Receiver communicate on WhatsApp, voice call or another external channel. Sender obtains Receiver address, initiates a locked transaction, and Sender BlackBox generates the one-use Receiver Claim Code K_R. Sender privately shares K_R with intended recipient. Receiver signs/submits a CLAIM REQUEST with K_R from the precisely bound destination wallet. **This is NOT a successful Claim or settlement.** The Sender's **own BlackBox must receive the authenticated request and display a manual ACCEPT** action; only after Sender independently approves the exact Receiver wallet, amount, transaction and claim request, the network may finalize payment to Receiver. **NO Sender ACCEPT = NO Receiver payout, regardless of having K_R and Receiver Wallet key.** Sender prefers NO manual REJECT; lack of acceptance must expire at the existing 24h Receiver claim deadline, then Sender's exclusive 72h manual reclaim opportunity opens. The approved payout is irreversible once BFT-final.

**Supersedes:** earlier wallet-bound Claim Key + Receiver authorization being sufficient by itself. Claims now require (i) correct Receiver Wallet signing proof + (ii) one-use K_R knowledge proof / commitment + (iii) independently signed Sender BlackBox ACCEPT for that exact claim + (iv) final settlement before network-delay-adjusted Receiver expiry. Do not disclose plaintext K_R on public ledger. Authenticate all request/approval messages against chain ID, protocol version, transaction ID, sender/receiver, asset, amount, nonce, phase and deadline; no global master override or hidden server assent.

**Timing must preserve existing CONFIRMED rules unless owner separately changes them:** Send creates escrow, original Sender BlackBox **Trigger** must still finalise within 3h or auto-refund, Trigger finality starts the Receiver's 24h exclusive claim right, then following 72h Sender Key K_S reclaim right. This new ACCEPT is currently a SECOND post-Receiver-Request Sender action after Trigger. Sender cannot manually cancel Triggered escrow; withholding ACCEPT is *not* an early cancellation/refund. If no ACCEPT for a valid Receiver Claim before finality deadline, receiver cannot claim; after Receiver period Sender can use K_S once as already decided. Claim submitted early but ACCEPT finalizes after expiry is still expired (apart from verifiable adjusted network delay credit). Any suggestion to MERGE the existing 3h Trigger with this final ACCEPT is only a future design option requiring explicit owner consent, as merging would change rights and timing.

**Wrong-address example:** Sender intended A but input address B; K_R is shared to A. A has code but not B's wallet-signing key, B has wallet-signing key but not K_R; even with both compromised, B cannot settle *without genuine Sender ACCEPT*. Sender can detect wrong bound address B in BlackBox confirmation and simply withhold ACCEPT, then later reclaim after Receiver window. This reduces wrong-destination risk, but if Sender is deceived into approving B, funds can be finally lost; code leakage, coercion, malicious UI, a compromised Sender signing device or signing phishing are still risk factors. Network cannot cryptographically establish human identity from wallet keys alone.

**Implementation issues OPEN (not secretly presumed solved):** sender signing/approval factor separated from Wallet Private Key; authenticated delivery of pending claim to Sender BlackBox when offline, replay and denial-of-service controls, receiver-submitted pre-Trigger requests, concurrency and expiry, public plaintext secrecy, verifier-efficient proof scheme, proof-lifecycle when Sender BlackBox lost, prevention of approvals for altered address/amount, no double-settlement and no forced payments. Senders must be clearly shown the actual network-bound receiver address and have a second independent confirmation factor where appropriate. Existing late-generation K_S versus disaster-recovered/dead Sender BlackBox remains an independent unresolved blocker. User's controversial post-96h reserve forfeiture has NOT been authorised for real-money launch.

**Why this is distinct:** The user prioritizes voluntary bilateral **human-in-the-loop** release authorization rather than one-click instant payment. This is a defined protocol addition only; never claim the full system is coded, cryptographically sound or first-ever before engineering proof and audits.

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
