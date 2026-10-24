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

The living backlog of **86 deep architecture, cryptographic, economic, privacy, recovery and edge-case questions** is in [docs/DEEP_QUESTIONS.md](docs/DEEP_QUESTIONS.md). Answer one at a time, save each decision, and add more questions when new dependencies arise. Do not treat the backlog as a finite limit.

## Continuing-work policy

- Ask **one unanswered decision question at a time**, in simple Punjabi, unless the user asks otherwise.
- Once the user answers, record the exact requirement and any caveats in **docs/DECISIONS.md**, update applicable technical docs, **PROGRESS.md**, **NEXT_SESSION.md**, and **CHANGELOG.md**, and commit the changes.
- Never label a feature **implemented**, **verified**, **audited** or **released** unless actual evidence exists.
- Never commit wallet private keys, setup secrets, authenticator master secrets, real claim codes or production credentials.

## Licensing and publication

The repository is **private** at initialisation. No licence file is intentionally supplied pending a licensing/IP decision. Git history records changes, but does not independently prove the 2015 date, uniqueness, patents, or ownership of broad ideas.

**Maintained by ParmTech · Original concept and development by Manjinder Singh.**
