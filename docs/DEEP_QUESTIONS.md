# TongNet — Deep Technical, Logical & Security Question Backlog

**Status:** Active discovery backlog, now 95 tracked questions (original 86 + new Q7, Q9, Q10, Q11, Q12, Q13, Q14, Q15 and Q16), initially prepared 2026-10-24. **Not evidence that these answers exist.**

**Workflow:** Ask one meaningful unresolved question at a time in easy Punjabi; user answers → record as a decision in docs/DECISIONS.md → amend FAQ / protocol / security docs → update PROGRESS.md, NEXT_SESSION.md, this backlog and CHANGELOG.md → commit to connected GitHub → ask next question.

**Q5 ANSWERED (2026-10-24):** Initial immutable Disaster Recovery Wallet setup requires Wallet Private Key and TongNet Authenticator. **Q6 ANSWERED (2026-10-24):** Immediately rescue *unlocked* balance; Triggered escrow stays locked for receiver's 24h right, then sender's 72h window. After completed disaster recovery, sender's same one-use Claim Key (if possessed) may claim via immutably linked recovery wallet. No automatic claim without key. **Q7 ANSWERED (Option A, 2026-10-24):** Untriggered 3h lock stays until original deadline and its automatic refund goes to the prebound disaster wallet after source DEAD, with no manual cancel or early release. **Q8 CLARIFIED 2026-10-24:** Single-use Disaster Recovery Key is GENERATED in recovery destination's own encrypted BlackBox during enrollment, not in source BlackBox. This does not itself establish that the destination privately signed/accepted. **Q9 ANSWERED (2026-10-24):** Source approval creates only a pending request in R BlackBox; R ACCEPT triggers one-use key generation there and permanent binding. REJECT notifies S BlackBox with no setup; pending/not accepted means NOT_CONFIGURED. **Q10 ANSWERED — Option A (2026-10-24):** unanswered pairing requests automatically EXPIRE after 24 hours; no Key or irrevocable binding and late Accept invalid. **Q11 ANSWERED Option B (2026-10-24):** no source cancellation or replacement while PENDING; wait for destination REJECT or 24-hour EXPIRED. **Q12 ANSWERED Option A (2026-10-24):** Accept valid only when NETWORK-FINAL strictly before pairing request's original 24h cutoff, even if user tapped/submitted earlier. Late-finalized Accept = EXPIRED, no key/link. **Q13 USER DIRECTION (2026-10-24):** running timers do not change speed for slow/fast networks; new requests may queue, and a NEW transaction timer begins only when network ACCEPTS it (consensus-finality recommended). Full network-down forfeiture exception remains OPEN. **Q14 ANSWERED Option A (2026-10-24):** Receiver Claim and subsequent sender reclaim each require network finality STRICTLY BEFORE their existing respective 24h/72h cutoff. A signed/QUEUED Claim finalized late is EXPIRED. **Q15 ANSWERED, UNIVERSAL RULE (2026-10-25):** ALL network-delay-affected time-bound operations, including Send/Trigger, receiver Claim, sender reclaim, Disaster Recovery pairing request/Accept and other deadlines, receive EXACTLY the attributable Network Delay Calculator time as an extra allowance. Strict Q12/Q14 consensus finality applies before the adjusted deadline. Clock cadence unchanged and no double count before initial acceptance. **NEXT Q16:** how to calculate verifiable per-operation vs global network delay.

**Do not re-ask settled decisions:** 3h noncancellable pre-trigger; 24h receiver claim after Trigger; following 72h sender recovery; permanent 72h unenrolled DEAD wallet; no cancellation after Trigger even wrong address; optional immutable disaster destination and one-use Disaster Recovery Key plus Wallet Private Key to execute, with no BlackBox/Authenticator; one-way old-wallet DEAD.

**Safety precedence:** Never silently change user-confirmed requirements, but clearly highlight contradictions and deployment blockers. At most mark a question "answered" when user explicitly resolves it, not from design guess.

---

## Recovery key, wallet lifecycle and physical security

- [x] **DQ-001** Initial immutable Disaster Recovery Wallet address registration: **Option A, Wallet Private Key AND TongNet Authenticator**, confirmed 2026-10-24. See docs/DECISIONS.md.
- [x] **DQ-002 [Q9 CONFIRMED 2026-10-24]** Only R BlackBox explicit ACCEPT makes S→R recovery pairing permanently final and creates one-time secret in R. Source request alone is PENDING and NOT_CONFIGURED; REJECT sends notice to source BlackBox. Exact proof technology remains to design.
- [ ] **DQ-003** If a typo enters the irreversible recovery destination and its key is created, should the entire original wallet be flagged as unsafe and user advised to migrate by ordinary transfers?
- [x] **DQ-004 (triggered escrow portion — Q6)** Preserve receiver's 24h claim; sweep only unlocked; then permit sender Claim Key via linked recovery wallet during next 72h after completed disaster recovery, if unclaimed.
- [x] **DQ-087 / Q7 (2026-10-24, Option A)** While a transfer is PENDING_TRIGGER and disaster recovery makes source DEAD, keep lock until original 3h timeout, then automatically refund into prebound disaster recovery wallet; no early cancellation.
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

- [x] **DQ-088 [Q9 ANSWERED 2026-10-24]** Destination R must ACCEPT from its own BlackBox; issue key there and finalize irreversible binding only after acceptance. No acceptance means NOT_CONFIGURED. Cryptographic signature/proof engineering pending.
- [x] **DQ-089 / Q10 (2026-10-24, Option A)** Unanswered destination BlackBox pairing request expires after 24 hours and can never subsequently be accepted. No link/key in PENDING or EXPIRED. Exact consensus boundary implementation still open.
- [x] **DQ-090 / Q11 (2026-10-24, Option B)** Main source wallet cannot cancel, withdraw or supersede pending disaster pairing; waits for R Reject or auto Expired at 24 hours. No config until Accept.
- [x] **DQ-091 / Q12 (2026-10-24, Option A)** STRICT: destination BlackBox Accept must be consensus-final before original 24h pairing deadline. Late network finality means expired even if signed or clicked earlier. User's local clock cannot establish acceptance.
- [ ] **DQ-092 / Q13 PARTIAL** User wants no clock slowdown/pause for ordinary network congestion; queue new submissions and start NEW timers on network acceptance. What to do about total network inability to finalize an already-running claim before a loss/forfeiture deadline remains open.
- [x] **DQ-093 / Q14 (2026-10-24 Option A)** Receiver/Sender Claim queued or signed before cutoff but finalized after deadline is EXPIRED. Only strict network finality before each pre-existing receiver 24h / sender following 72h cutoff grants claim.
- [x] **DQ-094 / Q15 (2026-10-25)** User specified one-for-one time allowance for NETWORK-caused delay, UNIVERSAL to all affected timed operations. Affected funds must not be irreversibly forfeited to reserve before adjusted windows finish; total outage proof/calculation and forfeiture legality still unresolved.
- [ ] **DQ-095 / NEXT Q16** Should each network task's allowed extra time come from individually verifiable processing/queue delay, or a single global Network Delay Calculator measurement for all affected tasks? Define consensus proofs, exclude client-caused inactivity and avoid crediting the same interval twice.

## Answer log

- **2026-10-24 — DQ-001/Q5**: Option A confirmed. INITIAL recovery destination setup requires Wallet Private Key and TongNet Authenticator; immutable thereafter. Full decision in docs/DECISIONS.md.
- **2026-10-24 — Q6/DQ-004 (triggered):** User confirmed only unlocked funds sweep now. Already-triggered receiver window survives; sender may use original one-use Sender Claim Key from previously linked rescue wallet after completed disaster recovery in the following 72h. No sender key, no claim. Deadline/race proofs still needed.
- **2026-10-24 — Q7/DQ-087:** Option A selected. A still-untriggered lock waits out its original 3h; if S is now DEAD after recovery, its automatic refund is credited once to prebound rescue address R. No acceleration, manual cancellation or Trigger by DEAD S.
- **2026-10-24 — Q8 clarification:** The one-use disaster secret is minted inside destination wallet's own BlackBox during registration and is used later with source private key for the irreversible one-time recovery. No destination private-key signature requirement has been chosen.
- **2026-10-24 — Q9 / DQ-002 + DQ-088:** R receives a recovery setup request in its BlackBox and independently ACCEPTS/REJECTS. ACCEPT generates one-time key in R's BlackBox and finalizes immutable link; REJECT sends message to S's BlackBox; ignored PENDING request creates NO setup/key.
- **2026-10-24 — Q10 / DQ-089:** Option A confirmed: pending unanswered request expires after 24h, no recovery protection, permanent pairing, or recovery key. A stale Accept must fail.
- **2026-10-24 — Q11 / DQ-090:** Option B. Pending pairing cannot be cancelled/replaced by source; must await rejection or 24h expiration.
- **2026-10-24 — Q12/DQ-091:** User picked A. No pairing acceptance after the original 24h deadline regardless of earlier tap/submission; finality before deadline required.
- **2026-10-24 — Q13/DQ-092 partially answered:** network slow/fast never changes time speed. New transactions/tasks can queue and timers start only on NETWORK ACCEPT (recommend consensus finality); this does not solve inability to finalize active Claim during a total outage or lawful forfeiture.
- **2026-10-24 — Q14/DQ-093:** User picked A. A Receiver/Sender claim must be fully network-final BEFORE its existing 24h/72h deadline; early queue placement does not preserve it.
- **2026-10-25 — Q15 / DQ-094:** User extends network-delay compensation universally across all time-sensitive operations, crediting each actual network-caused delay one-to-one. Strict finality before the compensated effective cutoff continues. Reserve cannot preempt corrected legitimate rights; legal authorization still blocked.
- **NEXT Q16 / DQ-095:** robust network delay measurement — per-task verified queue time vs global consensus slowdown.
