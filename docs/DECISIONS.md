# TongNet — Decision Register

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
| D-017 | Sender must separately **Trigger** it within authenticated BlackBox |
| D-018 | **NO sender manual cancellation** in the pre-trigger phase |
| D-019 | If not triggered by **3 hours after Send**, automatic full refund to sender |
| D-020 | **No receiver claim key** until a successful Trigger |
| D-021 | Successful Trigger delivers receiver-only, target-address-bound, one-use claim credential to receiver BlackBox |
| D-022 | Receiver can claim only within **24 hours after Trigger**, using valid wallet control and claim credential |
| D-023 | Sender cannot reclaim during recipient's 24-hour window |
| D-024 | If receiver does not claim, receiver credential expires; sender has **additional 72 hours** for one-use reclaim with sender credential |
| D-025 | One successful claim/refund consumes entitlement and must atomically prevent any competing payout |
| D-026 | Latest user intent: unrecovered funds after 24+72h go permanently to TongNet Network Reserve and support **network-only** transaction costs; **not authorised for real-money launch without legal, consent and economic review** |
| D-027 | **Confirmed 2026-10-24 (Question 1, Option B): After a successful Trigger, there is NO sender cancellation, emergency stop, or reversal, including when the recipient address was entered incorrectly. A valid addressed receiver may still claim in the 24h window; sender recovery is possible only after non-claim and expiry of that window.** |

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
| OPEN-029 | **NEXT Q16 — NETWORK DELAY CALCULATOR** | Should eligible extra time be calculated per individual operation from verifiable network processing/queue delay, or from one global network-wide congestion/outage value applied uniformly to affected operations? Prevent fabricated delays, clock drift, unfair priority and double credits. |
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
