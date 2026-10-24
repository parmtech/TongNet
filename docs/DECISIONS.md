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
| D-014 | Activation | Earlier recorded requirement: enrol within 72h or wallet permanently DEAD and barred from sending/receiving/claiming (confirm recovery/legal edge cases before shipping) |
| D-015 | Reset | Earlier recorded proposal: current authenticator secret plus wallet proof needed for re-enrolment |

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

## Historical/superseded

- Earlier receiver claim window: 60 minutes → replaced by **24 hours**.
- Earlier sender recovery: 3 days versus 7 days discussed → latest **additional 72 hours**.
- Earlier pre-trigger "cancel/refund now" proposal → explicitly rejected; **wait full 3h**.
- Earlier automatic sender return at end of sender recovery suggested → later user specified **reserve forfeiture after unclaimed 24+72h**; legality and consent **unresolved**.
- Earlier project name SIFAR Mesh → replaced by **TongNet**.
- Concept-origin year mistakenly listed 2016 → **corrected by creator to 2015**.
- AUD 1:1 peg discussed only as an **illustration**, not a confirmed tokenomics decision.

## Pending / blocked decisions

| ID | Priority | Question / problem |
|---|---|---|
| OPEN-001 | **NEXT** | After Trigger, if recipient address is incorrect, can sender emergency-stop an unclaimed transfer, or must recipient window be immutable? |
| OPEN-002 | Critical | Lost setup code within 72h: any regeneration? |
| OPEN-003 | Critical | Lost authenticator root secret: recovery policy without enabling takeover? |
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
