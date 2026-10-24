# TongNet — Deep Technical, Logical & Security Question Backlog

**Status:** Active discovery backlog, 86 explicit questions; initially prepared 2026-10-24. **Not evidence that these answers exist.**

**Workflow:** Ask one meaningful unresolved question at a time in easy Punjabi; user answers → record as a decision in docs/DECISIONS.md → amend FAQ / protocol / security docs → update PROGRESS.md, NEXT_SESSION.md, this backlog and CHANGELOG.md → commit to connected GitHub → ask next question.

**Q5 ANSWERED (2026-10-24):** Option A — Initial one-time setup of immutable Disaster Recovery Wallet address requires BOTH Wallet Private Key and TongNet Authenticator. The address and one-time recovery key can never change/reset. **NEXT Q6:** If outgoing funds are already locked, what may a terminal Disaster Recovery sweep, and what happens to later refunds without violating receiver rights?

**Do not re-ask settled decisions:** 3h noncancellable pre-trigger; 24h receiver claim after Trigger; following 72h sender recovery; permanent 72h unenrolled DEAD wallet; no cancellation after Trigger even wrong address; optional immutable disaster destination and one-use Disaster Recovery Key plus Wallet Private Key to execute, with no BlackBox/Authenticator; one-way old-wallet DEAD.

**Safety precedence:** Never silently change user-confirmed requirements, but clearly highlight contradictions and deployment blockers. At most mark a question "answered" when user explicitly resolves it, not from design guess.

---

## Recovery key, wallet lifecycle and physical security

- [x] **DQ-001** Initial immutable Disaster Recovery Wallet address registration: **Option A, Wallet Private Key AND TongNet Authenticator**, confirmed 2026-10-24. See docs/DECISIONS.md.
- [ ] **DQ-002** Should an initial recovery-wallet destination require a signed proof that the owner controls the destination private key, or is a checksum/address confirmation enough?
- [ ] **DQ-003** If a typo enters the irreversible recovery destination and its key is created, should the entire original wallet be flagged as unsafe and user advised to migrate by ordinary transfers?
- [ ] **DQ-004 [NEXT Q6]** What if disaster recovery is invoked while some funds are already locked in PENDING_TRIGGER or a receiver has an active 24h claim? Sweep only spendable funds with eventual refunds redirected to recovery wallet, or wait for all unsettled transfers to finish?
- [ ] **DQ-005** What if disaster recovery starts while a receiver has a valid 24-hour claim on a triggered transfer? Must the receiver's entitlement survive?
- [ ] **DQ-006** What if user has a sender-only recovery entitlement for an unclaimed outgoing transfer when their original wallet turns DEAD? Where can the eventual returned money legally and technically go?
- [ ] **DQ-007** What happens to future incoming transfers attempted to a permanently DEAD address: reject before debit, refund, or burn? Which consensus evidence proves DEAD?
- [ ] **DQ-008** Should an active wallet with no recovery destination be permitted unlimited balance, or warn/limit until backup configured?
- [ ] **DQ-009** How should users prove they've safely backed up the permanent disaster recovery key without the app retaining a plaintext copy?
- [ ] **DQ-010** If the disaster key is stolen but wallet key is safe, can attacker cause damage by submitting bogus proofs, or is proof bound to wallet signature?
- [ ] **DQ-011** Can the authenticator master key be exported to a second secure device, or is it one-device only? What if the phone is lost?
- [ ] **DQ-012** How does the wallet secure private keys against malware, clipboard substitution and screen recording, particularly on rooted phones?
- [ ] **DQ-013** Are wallet keys derived from an industry-standard seed phrase, from hardware keys, or both? What is the recovery story for loss of the wallet key?
- [ ] **DQ-014** If someone loses BOTH the wallet private key and the authenticator root secret but has disaster key, is there intentionally no recovery?
- [ ] **DQ-015** Can a user change the wallet password/PIN without changing their underlying wallet private key?
- [ ] **DQ-016** What prevents a thief with a stolen wallet key from repeatedly initiating irreversible 3-hour lockups to deny normal use?
- [ ] **DQ-017** Can original wallet's pending transfers be viewed, audited or exported after the disaster sweep permanently deactivates it?
- [ ] **DQ-018** Should destination wallets be required ACTIVE at the time of initial setup, at recovery execution, or both?
- [ ] **DQ-019** If the recovery wallet itself has its own immutable recovery destination, are self-reference or cyclic recovery configurations permitted?
- [ ] **DQ-020** How is a user notified that an immutable disaster destination was originally set, without leaking the key or personal data?

## Payment, time, state transitions and failure cases

- [ ] **DQ-021** Does the 3-hour non-cancellable pending period start when signed locally or when network finality acknowledges the lock?
- [ ] **DQ-022** If the sender submits Trigger at exactly t0 + 3 hours while the auto-refund happens concurrently, which action wins?
- [ ] **DQ-023** Does receiver's 24-hour window begin at Trigger consensus finality, or when its BlackBox successfully downloads the claim credential?
- [ ] **DQ-024** If the receiver's device remains offline during all 24 hours, should the time still expire exactly as planned?
- [ ] **DQ-025** Can the sender send multiple pending transfers simultaneously using the same wallet balance, and how are reserves calculated?
- [ ] **DQ-026** Can the sender accidentally Trigger a different pending transfer because of stale UI state or deceptive transaction ID?
- [ ] **DQ-027** If receiver claim and sender recovery hit different network partitions near the 24-hour boundary, what protects against both succeeding?
- [ ] **DQ-028** If a claim is correctly signed but network finality is delayed past expiry, should submission-time or finalisation-time govern acceptance?
- [ ] **DQ-029** If fee/amount rounding creates dust, who receives the remaining smallest units?
- [ ] **DQ-030** What exactly counts as 'full balance' in a transaction model that has spendable value, locks, pending claims and reserve entitlements?
- [ ] **DQ-031** Must a user have enough native TONG for a final claim or refund fee if user-facing transaction fees are advertised as zero?
- [ ] **DQ-032** Can a transaction be partially claimed or is a receiver claim all-or-nothing?
- [ ] **DQ-033** What happens when a sender triggers payment but encrypted delivery to receiver BlackBox never reaches it?
- [ ] **DQ-034** Should receiver be able to reject an unsolicited transfer, or only ignore the claim and let timeout occur?
- [ ] **DQ-035** How do transaction IDs and one-use credentials prevent cross-network replay, copying or accidental reuse?
- [ ] **DQ-036** Should wallet display irreversible-trigger warning and exact address/amount in an independent, hardware-backed confirmation interface?
- [ ] **DQ-037** When the 24+72-hour window expires, is reserve forfeiture unconditional, or does user opt in to that rule at transaction creation?
- [ ] **DQ-038** What happens if a bug temporarily leaves locked money neither receivable nor refundable?
- [ ] **DQ-039** If the network is offline longer than an expiry period, should time deadlines pause or remain absolute?
- [ ] **DQ-040** What is the maximum value per transfer during the earliest experimental stage?

## Consensus, peer-to-peer structure, scale and network threat model

- [ ] **DQ-041** Are nodes fully permissionless to join as validators, or can validators join only after some decentralised qualification process?
- [ ] **DQ-042** What scarce resource or identity prevents one attacker from creating a million fake validator nodes if mining/staking are excluded?
- [ ] **DQ-043** How many independent witnesses must approve state changes, and how do you select them without manipulable randomness?
- [ ] **DQ-044** Who is authorised to update membership and remove malicious validators without any central company controlling it?
- [ ] **DQ-045** What percentage of malicious, offline or colluding nodes should the system tolerate while retaining safety?
- [ ] **DQ-046** Do you prefer never double-spending even during partitions, accepting temporary unavailable payments, or making progress and risking reconciliation conflicts?
- [ ] **DQ-047** Must every node store every spent credential, or can spend-state be partitioned without losing double-spend safety?
- [ ] **DQ-048** If a malicious majority censors one person's payments, what neutral escape or rotation mechanism exists?
- [ ] **DQ-049** Can attackers spam unlimited cost-free transactions, and how should zero-fee wallets be rate-limited without mandatory ID?
- [ ] **DQ-050** What are measurable targets for confirmation latency and throughput before claiming better speed than legacy networks?
- [ ] **DQ-051** Are receipt proofs durable/independently verifiable even after old network nodes shut down?
- [ ] **DQ-052** How should a new node safely bootstrap and verify history without trusting a single website or snapshot host?
- [ ] **DQ-053** How do nodes agree on time for 3-hour, 24-hour and 72-hour rules without trusting a central clock?
- [ ] **DQ-054** What happens if a cryptographic algorithm is broken or quantum attacks become viable; how can keys be migrated with no central override?
- [ ] **DQ-055** Should validators be unpaid volunteers, merchant-funded, subsidised by the network reserve or subject to a different economic model?
- [ ] **DQ-056** How will you measure the real cost per transaction (bandwidth, CPU, storage) across regions and under attack?
- [ ] **DQ-057** What prevents region-specific network partition attacks from freezing all recovery claims until after expiry?
- [ ] **DQ-058** Which protocol upgrades require global approval, and what happens to wallets that refuse an incompatible upgrade?

## TONG value, reserve governance, financial rights and compliance

- [ ] **DQ-059** Is TONG redeemable 1:1 against a national currency, backed by different assets, or designed as a floating-value network token?
- [ ] **DQ-060** If TONG is redeemable for external assets, who has legal custody of those assets without reintroducing central dependence?
- [ ] **DQ-061** Which entity promises redemption and what rights do holders have if that entity fails?
- [ ] **DQ-062** Can new TONG units ever be minted, and who verifies issuance and reserve proofs?
- [ ] **DQ-063** What happens when the network reserve accumulates unclaimed funds; do users explicitly consent to permanent forfeiture?
- [ ] **DQ-064** Would voluntary donations or merchant-funded network costs be safer than automatically seizing expired payments?
- [ ] **DQ-065** Who authorises payments out of the network reserve, and how do all wallet owners audit those expenses?
- [ ] **DQ-066** Does network reserve governance use one wallet one vote, knowing fake wallets make that Sybil-vulnerable, or a different rule?
- [ ] **DQ-067** If reserve funds are spent for fees, how is monetary supply, TONG purchasing power and backing maintained?
- [ ] **DQ-068** How are irreversibly lost wallets and forgotten secrets treated in circulating supply calculations?
- [ ] **DQ-069** Do wallet transfers constitute final settlement, or is redeemability into external currency an additional legal obligation?
- [ ] **DQ-070** What requirements apply when serving Australia first, and what jurisdiction(s) would the operating entity target initially?
- [ ] **DQ-071** Should the core project stay private until security/legal review, or is staged public specification review part of the strategy?
- [ ] **DQ-072** What is the intended licence for the source code, patents, trademark and validator implementations?

## Privacy, usability, governance, release and operational readiness

- [ ] **DQ-073** Which information can recipients, validators, network monitors and ordinary public users each see (amount, addresses, timing, claim status)?
- [ ] **DQ-074** Should amounts be confidential to the network or just sender/receiver? How will nodes verify conservation if amounts are hidden?
- [ ] **DQ-075** Can one-time payment identifiers be linked to other wallet transactions and physical IP addresses? What metadata leak is acceptable?
- [ ] **DQ-076** Does sending a claim code to a private BlackBox require servers to know that sender/receiver relationship?
- [ ] **DQ-077** How does a user regain encrypted BlackBox history after losing a phone without introducing custodial keys?
- [ ] **DQ-078** Can one wallet be securely used on multiple devices simultaneously, including concurrent Authenticator tokens?
- [ ] **DQ-079** Will TongNet Wallet and TongNet Authenticator be separate apps, hardware devices, or available in multiple configurations?
- [ ] **DQ-080** How will users recognise phishing apps, malicious updates, deceptive QR codes and fake network nodes?
- [ ] **DQ-081** What should happen if a software bug wrongly labels a wallet DEAD or falsely accepts a recovery? Is there any governance recourse consistent with immutability?
- [ ] **DQ-082** Who can change the protocol, and how are proposed rules published, approved and audited without unilateral ParmTech control?
- [ ] **DQ-083** How will privacy requests (e.g. deletion) interact with immutable spent-state evidence?
- [ ] **DQ-084** What should testnet success criteria be (e.g. verified double-spend invariant under partition, audited recovery state, reproducible test runs)?
- [ ] **DQ-085** How will critical vulnerabilities be privately reported and patched after public release?
- [ ] **DQ-086** What hard launch blockers should prevent any real-money adoption until solved?

## Answer log

- **2026-10-24 — DQ-001/Q5**: Option A confirmed. INITIAL recovery destination setup requires Wallet Private Key and TongNet Authenticator; immutable thereafter. Full decision in docs/DECISIONS.md.
- **Next Q6:** Locked fund treatment during one-way Disaster Recovery; no decision yet.
