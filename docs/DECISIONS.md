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
| CLOSED-003 | **ANSWERED 2026-10-24** | User chose optional TongNet Disaster Recovery Wallet, configured in normal Wallet settings, NOT BlackBox. An original-wallet-private-key holder can Run Disaster Recovery WITHOUT BlackBox/Authenticator; intend full eligible-balance sweep less any applicable fee to preconfigured recovery address, followed by permanently DEAD source wallet. Does NOT restore BlackBox. Pending treatment of already locked funds. |
| OPEN-016 | **NEXT / CRITICAL** | Is TongNet Authenticator approval required when registering/changing Disaster Recovery destination, or can a wallet private key alone change it? Execution remains BlackBox-free. |
| OPEN-017 | Critical | Define whether pending/triggered/escrow funds may be swept without violating receiver claim or sender expiry rules. |
| OPEN-018 | High | Destination address confirmation, change delays, ownership proof, attack resistance, atomic sweep and fees. |
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

## Q3 — Disaster Recovery Wallet (2026-10-24)
- Optional, pre-registered second wallet address in ordinary wallet settings.
- Recovery executable using wallet private-key authority alone, without BlackBox or Authenticator factor.
- Sweep entire eligible source balance to fixed destination less any applicable fee, then permanently DEAD source wallet.
- **Security risk:** if stolen wallet key can also change recovery destination, an attacker can drain funds. Destination registration/update authorization is undecided.
- **Protocol conflict:** in-flight locked transfers might have receiver claim rights; treatment undecided. See [DISASTER_RECOVERY.md](DISASTER_RECOVERY.md).
