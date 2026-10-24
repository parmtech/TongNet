# TongNet

**A proposed decentralized financial network and digital currency protocol.**  
**Native coin:** TONG | **Wallet:** TongNet Wallet | **Secret inbox:** TongNet BlackBox | **Authenticator:** TongNet Authenticator

> **Status: protocol research and design. NOT a launched chain, deployed coin, audited wallet, security-certified system, or financial product.** Nothing in this repository constitutes a promise of zero fees, guaranteed value, perfect privacy, or security.

## Attribution

- **Project author / company:** ParmTech
- **Original concept creator and developer:** Manjinder Singh
- **Concept origin:** 2015 *(creator-stated; documentary proof not yet independently examined)*
- **Private concept period:** 2015–2026 *(creator-stated)*
- **First public disclosure:** 2026 *(creator-stated; note this GitHub repository is currently private)*
- **Previous working name:** SIFAR Mesh (historical only). **Current name is TongNet.**

© 2026 ParmTech. All rights reserved. No open-source licence has been granted by this repository. Ownership and use rights are subject to applicable law and any agreements.

## The research goal

Explore a genuinely decentralised, fast, privacy-oriented payments architecture without proof-of-work mining or traditional proof-of-stake, and with no or negligible end-user transfer fees. Seek meaningful economic utility for TONG rather than asserting an unbacked price. **These are design goals, not proven results or a verified claim of novelty.**

Core concepts:
1. Wallet creation provisions a separate encrypted **TongNet BlackBox**, plus a one-time authenticator-enrolment secret.
2. **TongNet Authenticator** is an independent factor; its access code changes every 60 seconds. The root secret does **not** rotate every minute.
3. A sender initiates a transfer, locking funds, and must separately authorise a **Trigger** from their BlackBox.
4. No trigger by 3 hours after initiation ⇒ automatic return to sender; **no manual cancellation** during those 3 hours.
5. After triggering, only the addressed recipient can use its BlackBox claim credential during a **24-hour receiver window**.
6. If unclaimed, the recipient credential expires; only the sender can reclaim during the following **72-hour recovery window**.
7. The creator's current proposed rule sends funds still unclaimed after that window to the **TongNet Network Reserve** to subsidise network transaction costs. **This forfeiture rule must NOT be deployed with real money until consent, ownership, regulatory and consumer-protection issues are resolved.**

## Emergency recovery (new proposal)

An **optional TongNet Disaster Recovery Wallet** address may be preconfigured in ordinary wallet settings. When source requests the optional destination, **SOURCE Wallet Private Key + TongNet Authenticator** must authorize a request delivered to **DESTINATION Recovery Wallet's own BlackBox**. Until destination explicitly **ACCEPTS**, setup is **PENDING, NOT_CONFIGURED**, with no recovery key or immutable link; unanswered requests automatically EXPIRE after **24 hours** (Q10), and late acceptance is invalid. On ACCEPT, the unique one-time **Disaster Recovery Key is generated in the destination BlackBox** and the source→destination link becomes permanently immutable. REJECT sends notification to source BlackBox and installs nothing. To run recovery, the owner needs **both Wallet Private Key and Disaster Recovery Key**, without BlackBox or TongNet Authenticator; successful atomic sweep of eligible funds (less actual fee) moves value to the fixed destination and permanently marks the source wallet DEAD. Disaster key and address can never be changed/reset/reissued; losing that key makes this route unavailable. Initial registration requires Wallet Private Key plus TongNet Authenticator (Q5). Q6 confirms that only available value is swept immediately: previously Triggered locked payments preserve receiver 24h claim rights, followed by the sender's 72h opportunity using the original one-use Sender Claim Key through the pre-bound disaster wallet if the disaster operation has completed. Missing sender Claim Key cannot be bypassed. **Q7 confirmed:** if source is permanently DEAD after disaster recovery while an outgoing Send remains untriggered and locked, it stays locked until original 3h expiry and its automatic refund goes to the prebound disaster recovery wallet. **Q8 clarified:** recovery key is created/stored inside recovery destination's own BlackBox; **Q9 confirmed:** destination BlackBox must Accept before pairing becomes final; Q10 confirmed unanswered request expires after 24 hours; Q11 pending source withdrawal/replace policy is open. See [docs/DISASTER_RECOVERY.md](docs/DISASTER_RECOVERY.md).

## Read before doing work

1. [NEXT_SESSION.md](NEXT_SESSION.md) — where to resume and the next unanswered question.
2. [PROGRESS.md](PROGRESS.md) — actual status and blockers.
3. [docs/DECISIONS.md](docs/DECISIONS.md) — user-confirmed requirements vs proposed mechanisms and pending questions.
4. [docs/PROTOCOL.md](docs/PROTOCOL.md) — versioned transfer flow and state machine.
5. [docs/FAQ.md](docs/FAQ.md) — accumulated product decisions in question/answer form.
6. [docs/SECURITY.md](docs/SECURITY.md) — assumptions, risks and attack scenarios.
7. [docs/HISTORY.md](docs/HISTORY.md) — provenance and naming.
8. [ROADMAP.md](ROADMAP.md) and [CHANGELOG.md](CHANGELOG.md).

## Exhaustive security and technical questioning

The backlog currently tracks **95 deep architecture questions** in [docs/DEEP_QUESTIONS.md](docs/DEEP_QUESTIONS.md), with every candidate answer reviewed in [docs/MASTER_QA_RECOMMENDATIONS.md](docs/MASTER_QA_RECOMMENDATIONS.md). See [docs/TONGNET_FUTURE_ARCHITECTURE.md](docs/TONGNET_FUTURE_ARCHITECTURE.md) for the new safety-first, future-proof and high-performance architecture research. Not all answers are user-approved, proven or built; more questions may arise.

## Continuing-work policy

- **User updated workflow on 2026-10-25:** review all deep questions and candidate answers together and batch-save when explicitly asked; do not automatically force one-question-per-turn.
- Clearly separate explicit user-confirmed requirements from engineering recommendations and hard release blockers in **docs/DECISIONS.md** and the two master reviews.
- Never label a feature **implemented**, **verified**, **audited** or **released** unless actual evidence exists.
- Never commit wallet private keys, setup secrets, authenticator master secrets, real claim codes or production credentials.

## Licensing and publication

The repository is **private** at initialisation. No licence file is intentionally supplied pending a licensing/IP decision. Git history records changes, but does not independently prove the 2015 date, uniqueness, patents, or ownership of broad ideas.

**Maintained by ParmTech · Original concept and development by Manjinder Singh.**

**Q11 decision:** Source cannot cancel or replace a pending recovery setup request. It must wait for destination rejection or the unchanged 24-hour expiry. **Q12 confirmed:** the recipient Recovery Wallet's Accept must be network-finalized before the original 24-hour pairing deadline; early button press but late finality is EXPIRED. **Q13 direction:** running timers unaffected by network speed; new requests queue under load and new payment timers start only on network acceptance (recommend consensus finality, not queue admission). **Q14 confirmed Option A:** receiver/sender financial Claim queued early but final after existing deadline is EXPIRED; only consensus-final before cutoff counts. **Q15 clarified:** every time-sensitive network operation affected by verifiable TongNet processing/outage delay gets equal extra time on its effective deadline (Send/Trigger, Claims, Disaster Recovery setup and other timed tasks). Q12/Q14 still require final network confirmation strictly before the ADJUSTED deadline, not queue admission. **NEXT Q16:** whether network delay is measured individually or globally. Reserve forfeiture remains blocked for real funds pending law/consent review.

## Latest 2026-10-25 architecture direction

User confirmed Q16 C (hybrid per-operation + global one-for-one network delay), Q17 C (independent anti-fake-delay proof), Q18 C (evidence consensus or protected escrow), Q19–20 C (anti-Sybil and phased decentralisation), Q21 C (automated validator governance), Q22 B (quarantine), Q23 B (standby replacements), Q24 C (quorum in partitions), Q25 B (pre-committed safe replacement). Long-term goals: fast, highly capable and secure; avoid PoW and pure wealth-dominant PoS but *hybrid stake/bond is allowed*; aim for user-visible near-zero fees and genuine decentralisation without an indispensable vendor/cloud. **Engineering proposal:** proven BFT core, measured parallelisation, hybrid eligibility and fee sponsorship, crypto agility; optional later DAG experiments. See [future architecture](docs/TONGNET_FUTURE_ARCHITECTURE.md) and [all 95 Q&A](docs/MASTER_QA_RECOMMENDATIONS.md). Originality, safety, real-world throughput and 100% decentralisation are not proved. The earlier proposed Network Reserve forfeiture remains a major legal and consumer-safety blocker.

## Primary programming language (selected 2026-10-25)

**Rust** is the chosen primary engineering language for TongNet blockchain core, BFT consensus integration, node/P2P networking, transaction state machine, hybrid validator and Network Delay Calculator, cryptographic wallet/recovery engine, and cross-platform shared libraries. The owner delegated language selection to the assistant, which selected Rust over C/C++ for performance + default memory-safety + maintainability; this is an architecture decision, **not implemented software**. UI applications may use Kotlin/Swift and appropriate desktop/frontend technologies while sharing a single Rust security-critical core via narrowly versioned bindings. Mature audited cryptographic libraries are appropriate; minimise unsafe FFI. Rust does not, by itself, make a protocol free, fully decentralised, or secure. See [Future Architecture](docs/TONGNET_FUTURE_ARCHITECTURE.md).

## Product and adoption critique

[Critical TongNet product review](docs/TONGNET_PRODUCT_CRITIQUE_AND_ADOPTION_PLAN.md) covers user trust, bank/merchant needs, competitive alternatives, 20 red-team questions and historical, now-superseded Instant Pay suggestion. **The user confirmed Secure Manual Two-Party P2P only, NOT Instant Pay**; existing Send/Trigger/receiver-Claim rules remain. proposed TONG supply is not final. No mainnet exists.

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
