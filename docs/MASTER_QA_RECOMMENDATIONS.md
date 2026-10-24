# TongNet — Master 95-Question Architecture Review: Questions and Proposed Answers

**2026-10-25. Status:** Research/specification ONLY; every unconfirmed response below is an ENGINEERING RECOMMENDATION, not a statement that the user approved it or the feature was built. Original question wording is preserved from `DEEP_QUESTIONS.md`. Any contradictory older snippets are superseded ONLY for purposes of recommendations and must be reconciled before deployment.

**Mandate:** high throughput, low-latency deterministic finality, anti-Sybil decentralisation, no single operator or runtime cloud dependency, economically sustainable near-zero user-visible fees, original coherent protocol compositions, future cryptographic and validator agility. PoS *hybrid eligibility/bond* is permitted; avoid pure wealth-weighted governance. Prove each component, not novelty by declaration. See `TONGNET_FUTURE_ARCHITECTURE.md` for architecture and hard blockers.

**Status key:** CONFIRMED = explicitly chosen in conversation (sometimes implementation caveat or current user right is already recorded); RECOMMENDATION = best proposed resolution requiring design verification and, where changing user rights, further owner ratification. Nothing here means mainnet-ready or secure by assertion.

### DQ-001 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Initial immutable Disaster Recovery Wallet address registration: **Option A, Wallet Private Key AND TongNet Authenticator**, confirmed 2026-10-24. See docs/DECISIONS.md.
**Answer:** CONFIRMED: Initial immutable destination request requires original wallet private-key authorisation AND TongNet Authenticator, followed by explicit R acceptance.

### DQ-002 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Only R BlackBox explicit ACCEPT makes S→R recovery pairing permanently final and creates one-time secret in R. Source request alone is PENDING and NOT_CONFIGURED; REJECT sends notice to source BlackBox. Exact proof technology remains to design.
**Answer:** CONFIRMED: No recovery pairing/key until destination R explicitly accepts inside its own BlackBox and network finality records the binding.

### DQ-003 — RECOMMENDATION
**Question:** If a typo enters the irreversible recovery destination and its key is created, should the entire original wallet be flagged as unsafe and user advised to migrate by ordinary transfers?
**Answer:** Recommend safety-first warning, independent destination confirmation and small-value test. After an irrevocable misbinding, allow ordinary balance migration to new wallet where authorised; do not silently mutate destination.

### DQ-004 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Preserve receiver's 24h claim; sweep only unlocked; then permit sender Claim Key via linked recovery wallet during next 72h after completed disaster recovery, if unclaimed.
**Answer:** CONFIRMED: Recovery sweeps spendable balance only. Triggered escrow keeps original recipient-first 24h and sender-next 72h claims, adjusted by proven network delay.

### DQ-005 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** What if disaster recovery starts while a receiver has a valid 24-hour claim on a triggered transfer? Must the receiver's entitlement survive?
**Answer:** CONFIRMED via Q6: Receiver entitlement stays enforceable after source is marked DEAD; recovery cannot withdraw escrow early.

### DQ-006 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** What if user has a sender-only recovery entitlement for an unclaimed outgoing transfer when their original wallet turns DEAD? Where can the eventual returned money legally and technically go?
**Answer:** CONFIRMED via Q6: Sender's original one-use claim, if possessed, credits immutable R after completed disaster recovery; cannot issue a replacement key.

### DQ-007 — RECOMMENDATION
**Question:** What happens to future incoming transfers attempted to a permanently DEAD address: reject before debit, refund, or burn? Which consensus evidence proves DEAD?
**Answer:** Reject new sends to a consensus-final DEAD destination before debit; if already locked and recipient later becomes DEAD, preserve sender recovery under transaction rules, never silently burn.

### DQ-008 — RECOMMENDATION
**Question:** Should an active wallet with no recovery destination be permitted unlimited balance, or warn/limit until backup configured?
**Answer:** Recommend clear high-risk warnings and optional conservative transfer/balance limits; do not prohibit unlimited balances purely for missing optional recovery unless user expressly chooses.

### DQ-009 — RECOMMENDATION
**Question:** How should users prove they've safely backed up the permanent disaster recovery key without the app retaining a plaintext copy?
**Answer:** Offer offline recovery-key verification challenge and hardware/storage guidance, never upload plaintext or show full key later.

### DQ-010 — RECOMMENDATION
**Question:** If the disaster key is stolen but wallet key is safe, can attacker cause damage by submitting bogus proofs, or is proof bound to wallet signature?
**Answer:** Disaster execution requires BOTH distinct original wallet key signature and transaction-bound one-use recovery secret; stolen recovery secret alone must not sweep funds.

### DQ-011 — RECOMMENDATION
**Question:** Can the authenticator master key be exported to a second secure device, or is it one-device only? What if the phone is lost?
**Answer:** Recommend hardware-backed single active Authenticator with verified re-enrolment rules, and explicitly document loss scenarios; multi-device master export adds attack surface.

### DQ-012 — RECOMMENDATION
**Question:** How does the wallet secure private keys against malware, clipboard substitution and screen recording, particularly on rooted phones?
**Answer:** Use hardware-backed Keystore/Secure Enclave, anti-phishing transaction preview, clipboard/overlay defenses and signed builds; rooted/compromised OS cannot be guaranteed safe.

### DQ-013 — RECOMMENDATION
**Question:** Are wallet keys derived from an industry-standard seed phrase, from hardware keys, or both? What is the recovery story for loss of the wallet key?
**Answer:** Recommend audited hierarchical seed/hardware wallet key generation with independent recovery warnings; avoid custom entropy or silent account resurrection.

### DQ-014 — RECOMMENDATION
**Question:** If someone loses BOTH the wallet private key and the authenticator root secret but has disaster key, is there intentionally no recovery?
**Answer:** By current irreversible policy, without original private key recovery fails even if disaster key exists; high-loss scenario is a consumer safety blocker needing clear warnings.

### DQ-015 — RECOMMENDATION
**Question:** Can a user change the wallet password/PIN without changing their underlying wallet private key?
**Answer:** Change login PIN using local authenticated key rewrapping, not replacing blockchain private key; require rate limiting, anti-tamper and secure backup.

### DQ-016 — RECOMMENDATION
**Question:** What prevents a thief with a stolen wallet key from repeatedly initiating irreversible 3-hour lockups to deny normal use?
**Answer:** Require transaction-bound BlackBox approval AND Authenticator and explicit high-risk prompts; investigate compromised key events without a privileged owner cancellation backdoor.

### DQ-017 — RECOMMENDATION
**Question:** Can original wallet's pending transfers be viewed, audited or exported after the disaster sweep permanently deactivates it?
**Answer:** Maintain read-only signed history and exportable receipts for DEAD wallet; never permit signing new operations.

### DQ-018 — RECOMMENDATION
**Question:** Should destination wallets be required ACTIVE at the time of initial setup, at recovery execution, or both?
**Answer:** Destination must be ACTIVE at both pairing finality and execution; if later DEAD, pause recovery instead of burning funds; formally specify self-referential chains.

### DQ-019 — RECOMMENDATION
**Question:** If the recovery wallet itself has its own immutable recovery destination, are self-reference or cyclic recovery configurations permitted?
**Answer:** Reject S=R and circular recovery graphs via global state validation; keep recovery chain acyclic with deterministic bounded lookup.

### DQ-020 — RECOMMENDATION
**Question:** How is a user notified that an immutable disaster destination was originally set, without leaking the key or personal data?
**Answer:** Display permanent association state, destination fingerprint, change prohibition, status, and warnings without revealing key material.

### DQ-021 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Does the 3-hour non-cancellable pending period start when signed locally or when network finality acknowledges the lock?
**Answer:** CONFIRMED via Q13: 3h starts only when original Send lock is network-final, not on local click or queue admission.

### DQ-022 — RECOMMENDATION
**Question:** If the sender submits Trigger at exactly t0 + 3 hours while the auto-refund happens concurrently, which action wins?
**Answer:** Set strict boundary: Trigger finality must be < effective 3h deadline; otherwise exactly-one refund commits. Delay credits must be final/protected before either wins.

### DQ-023 — RECOMMENDATION
**Question:** Does receiver's 24-hour window begin at Trigger consensus finality, or when its BlackBox successfully downloads the claim credential?
**Answer:** Begin receiver's 24h at Trigger consensus finality. BlackBox offline delivery needs redundant encrypted retrieval but cannot redefine issuance time.

### DQ-024 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** If the receiver's device remains offline during all 24 hours, should the time still expire exactly as planned?
**Answer:** Local device offline is NOT proof of network-wide delay; normal window elapses, subject only to verifiable network-caused compensation.

### DQ-025 — RECOMMENDATION
**Question:** Can the sender send multiple pending transfers simultaneously using the same wallet balance, and how are reserves calculated?
**Answer:** Permit multiple simultaneous sends against available unencumbered balance; atomic per-wallet reservation and nonce ensure no overspending.

### DQ-026 — RECOMMENDATION
**Question:** Can the sender accidentally Trigger a different pending transfer because of stale UI state or deceptive transaction ID?
**Answer:** Bind Trigger to full transaction digest, amount, recipient, expiry and wallet; re-confirm independently in BlackBox, not ambiguous short IDs.

### DQ-027 — RECOMMENDATION
**Question:** If receiver claim and sender recovery hit different network partitions near the 24-hour boundary, what protects against both succeeding?
**Answer:** Quorum-intersecting finality and atomic escrow state prevent claim of same funds across partitions; no quorums means no settlement.

### DQ-028 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** If a claim is correctly signed but network finality is delayed past expiry, should submission-time or finalisation-time govern acceptance?
**Answer:** CONFIRMED Q14 refined Q15: queued earlier is not enough; signed Claim must finalise strictly BEFORE measured network-delay-adjusted deadline.

### DQ-029 — RECOMMENDATION
**Question:** If fee/amount rounding creates dust, who receives the remaining smallest units?
**Answer:** Use integer smallest denominations only, deterministic rounded fees, reject values below dust threshold or credit disclosed residual explicitly; never invisible loss.

### DQ-030 — RECOMMENDATION
**Question:** What exactly counts as 'full balance' in a transaction model that has spendable value, locks, pending claims and reserve entitlements?
**Answer:** Define total = spendable + untriggered locks + triggered escrows + pending incoming separately, and avoid reporting rights as spendable balance.

### DQ-031 — RECOMMENDATION
**Question:** Must a user have enough native TONG for a final claim or refund fee if user-facing transaction fees are advertised as zero?
**Answer:** Sponsored zero-visible-fee Claim/refund for normal quota only if funded; any actual fee must be disclosed, and fee starvation must not strand escrow.

### DQ-032 — RECOMMENDATION
**Question:** Can a transaction be partially claimed or is a receiver claim all-or-nothing?
**Answer:** Recommend indivisible all-or-nothing Claims per transaction to avoid partial replay, dust and disputed residual ownership.

### DQ-033 — RECOMMENDATION
**Question:** What happens when a sender triggers payment but encrypted delivery to receiver BlackBox never reaches it?
**Answer:** Keep receiver's encrypted credential available from independent replicated inboxes using commitment proofs, redundant notifications and retriable retrieval.

### DQ-034 — RECOMMENDATION
**Question:** Should receiver be able to reject an unsolicited transfer, or only ignore the claim and let timeout occur?
**Answer:** Recommend explicit recipient REJECT that waives receiver right by final transaction, safely activating sender-only reclaim once final, but requires separate user approval since earlier timing rules are strict.

### DQ-035 — RECOMMENDATION
**Question:** How do transaction IDs and one-use credentials prevent cross-network replay, copying or accidental reuse?
**Answer:** Domain-separated chain-ID/operation/transaction nonce, final spent/nullifier commitment and atomic transitions prevent cross-chain/replay.

### DQ-036 — RECOMMENDATION
**Question:** Should wallet display irreversible-trigger warning and exact address/amount in an independent, hardware-backed confirmation interface?
**Answer:** Yes: full untruncated recipient/address, amount, fees and irreversibility on hardware-backed trusted confirmation where supported.

### DQ-037 — RECOMMENDATION
**Question:** When the 24+72-hour window expires, is reserve forfeiture unconditional, or does user opt in to that rule at transaction creation?
**Answer:** Existing user proposed compulsory reserve forfeiture; recommend against it and BLOCK real-money deployment pending consent/legal review; prefer protected refund or explicit donation.

### DQ-038 — RECOMMENDATION
**Question:** What happens if a bug temporarily leaves locked money neither receivable nor refundable?
**Answer:** Freeze disputed escrow safely, preserve proofs, test deterministic repair upgrade under quorum governance; NEVER silently mint/erase user holdings.

### DQ-039 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** If the network is offline longer than an expiry period, should time deadlines pause or remain absolute?
**Answer:** CONFIRMED Q15/Q16: clocks run normally, but eligible verifiable network delay gets one-for-one extension; disputed delay triggers protected suspension of conflicting settlement.

### DQ-040 — RECOMMENDATION
**Question:** What is the maximum value per transfer during the earliest experimental stage?
**Answer:** Testnet faucet tokens only until full audit. Then risk-based value limits and staged rollout, no unbacked real-money transfer cap claims.

### DQ-041 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Are nodes fully permissionless to join as validators, or can validators join only after some decentralised qualification process?
**Answer:** CONFIRMED Q20 C: begin with verifiably eligible independent validators and progressively open under tested anti-Sybil rules, with initial trust clearly disclosed.

### DQ-042 — RECOMMENDATION
**Question:** What scarce resource or identity prevents one attacker from creating a million fake validator nodes if mining/staking are excluded?
**Answer:** Candidate hybrid scarce-cost eligibility: slashable security bond + independent operator credentials/performance; bond caps alone DO NOT solve wealthy Sybils.

### DQ-043 — RECOMMENDATION
**Question:** How many independent witnesses must approve state changes, and how do you select them without manipulable randomness?
**Answer:** Use quorum certificates >2/3 effective voting weight, audited VRF/randomness and provable committee changes; selection rules must resist operator-cluster capture.

### DQ-044 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Who is authorised to update membership and remove malicious validators without any central company controlling it?
**Answer:** CONFIRMED Q21 C: deterministic on-chain eligibility, evidence-based suspensions and bounded reconfiguration without discretionary owner approval.

### DQ-045 — RECOMMENDATION
**Question:** What percentage of malicious, offline or colluding nodes should the system tolerate while retaining safety?
**Answer:** Conservative BFT model <1/3 faulty effective voting power for safety with safe epoch changes; progress additionally requires synchrony and enough responsive members.

### DQ-046 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Do you prefer never double-spending even during partitions, accepting temporary unavailable payments, or making progress and risking reconciliation conflicts?
**Answer:** CONFIRMED Q24 C: no double-spend ever; partition segments without valid overlapping secure quorum halt finality.

### DQ-047 — RECOMMENDATION
**Question:** Must every node store every spent credential, or can spend-state be partitioned without losing double-spend safety?
**Answer:** Globally unique consumed key/nullifier registry or proof-carrying partition with a single authoritative spend owner and cross-lane atomic finality.

### DQ-048 — RECOMMENDATION
**Question:** If a malicious majority censors one person's payments, what neutral escape or rotation mechanism exists?
**Answer:** Redundant ingress, enforced objective inclusion/fairness targets, committee rotation, evidence of censorship and protected deadlines; if malicious quorum, no guaranteed escape.

### DQ-049 — RECOMMENDATION
**Question:** Can attackers spam unlimited cost-free transactions, and how should zero-fee wallets be rate-limited without mandatory ID?
**Answer:** Bounded mempool, per-resource quotas, signed receipts, anti-Sybil rate buckets and optional micropayment/congestion fees; never unlimited free spam.

### DQ-050 — RECOMMENDATION
**Question:** What are measurable targets for confirmation latency and throughput before claiming better speed than legacy networks?
**Answer:** Benchmark targets (not claims): <2s median and <5s P95 basic finality at >=1k sustained TPS in realistic testnet, plus malicious-fault/load tails.

### DQ-051 — RECOMMENDATION
**Question:** Are receipt proofs durable/independently verifiable even after old network nodes shut down?
**Answer:** Durable signed quorum certificates, history commitments, archivers and light-client proofs; validate historical validator set chain rather than trust UI/server.

### DQ-052 — RECOMMENDATION
**Question:** How should a new node safely bootstrap and verify history without trusting a single website or snapshot host?
**Answer:** Multi-peer bootstrapping, genesis hardcoded from user-verified release, peer diversity, checkpoint audits and reproducible snapshots.

### DQ-053 — RECOMMENDATION
**Question:** How do nodes agree on time for 3-hour, 24-hour and 72-hour rules without trusting a central clock?
**Answer:** Avoid device clocks as authority; canonical consensus-time/epochs with bounded drift; cannot prove global exact real time under total asynchrony.

### DQ-054 — RECOMMENDATION
**Question:** What happens if a cryptographic algorithm is broken or quantum attacks become viable; how can keys be migrated with no central override?
**Answer:** Versioned crypto envelope and governance-timelocked key-migration epoch. Evaluate NIST ML-KEM/ML-DSA hybrid migration; no DIY postquantum algorithm.

### DQ-055 — RECOMMENDATION
**Question:** Should validators be unpaid volunteers, merchant-funded, subsidised by the network reserve or subject to a different economic model?
**Answer:** Economic hybrid: optional sponsor pool, eligible usage fees and contractually transparent validator rewards, all fully auditable; no unpaid assumption.

### DQ-056 — RECOMMENDATION
**Question:** How will you measure the real cost per transaction (bandwidth, CPU, storage) across regions and under attack?
**Answer:** Measure regional ingress bandwidth, disk growth, CPU verification, network latency, replica count, anti-spam cost and actual AUD/transfer.

### DQ-057 — RECOMMENDATION
**Question:** What prevents region-specific network partition attacks from freezing all recovery claims until after expiry?
**Answer:** Multi-route relay, quorum-safe halt, global/individual delay credits with evidence and protected escrow; persistent censorship is a liveness hard problem.

### DQ-058 — RECOMMENDATION
**Question:** Which protocol upgrades require global approval, and what happens to wallets that refuse an incompatible upgrade?
**Answer:** Publish change specs and reproducible implementations, on-chain timelocked approvals, protocol-version activation, verified rollback only pre-finality.

### DQ-059 — RECOMMENDATION
**Question:** Is TONG redeemable 1:1 against a national currency, backed by different assets, or designed as a floating-value network token?
**Answer:** Recommend TONG initially as non-redeemable network utility unit with explicit fixed or audited emission terms; no asserted 1:1 fiat value.

### DQ-060 — RECOMMENDATION
**Question:** If TONG is redeemable for external assets, who has legal custody of those assets without reintroducing central dependence?
**Answer:** Do NOT promise collateral-backed redeemability without verifiable independent custody, legal issuer, redemption rights and audit.

### DQ-061 — RECOMMENDATION
**Question:** Which entity promises redemption and what rights do holders have if that entity fails?
**Answer:** No external redemption promise until legally identifiable counterparty, licences, insolvency rights and trust model are documented.

### DQ-062 — RECOMMENDATION
**Question:** Can new TONG units ever be minted, and who verifies issuance and reserve proofs?
**Answer:** Deterministic genesis and minted-supply policy (ideally capped or fully specified emission curve); no hidden owner minting.

### DQ-063 — RECOMMENDATION
**Question:** What happens when the network reserve accumulates unclaimed funds; do users explicitly consent to permanent forfeiture?
**Answer:** Reject unconditional confiscation in recommended production design; user proposal is recorded separately and real-money-blocked by law/consent and outage fairness.

### DQ-064 — RECOMMENDATION
**Question:** Would voluntary donations or merchant-funded network costs be safer than automatically seizing expired payments?
**Answer:** Yes: voluntary opt-in donations, merchant subscriptions and sponsor fees are generally safer than automatic confiscation; test economic viability.

### DQ-065 — RECOMMENDATION
**Question:** Who authorises payments out of the network reserve, and how do all wallet owners audit those expenses?
**Answer:** On-chain budget caps, category-restricted expenses, timelocked committee-driven authorisation with attestations, immutable public ledger and audit reports.

### DQ-066 — RECOMMENDATION
**Question:** Does network reserve governance use one wallet one vote, knowing fake wallets make that Sybil-vulnerable, or a different rule?
**Answer:** Never one-wallet-one-vote; anti-Sybil governance must derive weight from scarce verifiable eligibility and resist wealth centralisation.

### DQ-067 — RECOMMENDATION
**Question:** If reserve funds are spent for fees, how is monetary supply, TONG purchasing power and backing maintained?
**Answer:** Separate Network Reserve expenses from token supply/redemption; transparent audited incentives, no hidden dilution or unsupported purchasing-power promises.

### DQ-068 — RECOMMENDATION
**Question:** How are irreversibly lost wallets and forgotten secrets treated in circulating supply calculations?
**Answer:** Track provably burned vs merely inaccessible separately; never claim lost coins can be retrieved or minted back.

### DQ-069 — RECOMMENDATION
**Question:** Do wallet transfers constitute final settlement, or is redeemability into external currency an additional legal obligation?
**Answer:** Distinguish final on-network TONG settlement from any off-chain fiat exchange/redemption; no promise of monetary equivalence.

### DQ-070 — RECOMMENDATION
**Question:** What requirements apply when serving Australia first, and what jurisdiction(s) would the operating entity target initially?
**Answer:** Australia-first legal review: AUSTRAC registration if VASP service triggers, ASIC financial product/non-cash-payment/custody review and tax/privacy obligations before mainnet money.

### DQ-071 — RECOMMENDATION
**Question:** Should the core project stay private until security/legal review, or is staged public specification review part of the strategy?
**Answer:** Keep private during security research, then publish staged specs and audited components for independent review before mainnet; avoid concealment of critical bugs.

### DQ-072 — RECOMMENDATION
**Question:** What is the intended licence for the source code, patents, trademark and validator implementations?
**Answer:** Maintain IP ownership analysis and licence inventory. Choose permissive or copyleft open-source policies deliberately with counsel; no infringement guarantee.

### DQ-073 — RECOMMENDATION
**Question:** Which information can recipients, validators, network monitors and ordinary public users each see (amount, addresses, timing, claim status)?
**Answer:** Default public chain reveals necessary state commitments only; define exact disclosure per peer/validator/recipient and privacy-focused addresses.

### DQ-074 — RECOMMENDATION
**Question:** Should amounts be confidential to the network or just sender/receiver? How will nodes verify conservation if amounts are hidden?
**Answer:** Start with openly auditable conservation commitments; add confidential-amount zero-knowledge proofs only after independent audit, never trust mere encryption.

### DQ-075 — RECOMMENDATION
**Question:** Can one-time payment identifiers be linked to other wallet transactions and physical IP addresses? What metadata leak is acceptable?
**Answer:** Use address rotation, no unnecessary phone/IP telemetry, multiple P2P relays; admit metadata anonymity is not guaranteed.

### DQ-076 — RECOMMENDATION
**Question:** Does sending a claim code to a private BlackBox require servers to know that sender/receiver relationship?
**Answer:** Route encrypted BlackBox messages through replicated blind relays with short-lived delivery tokens and minimal linkage; don't require gateway to decrypt.

### DQ-077 — RECOMMENDATION
**Question:** How does a user regain encrypted BlackBox history after losing a phone without introducing custodial keys?
**Answer:** Encrypted multi-provider backup only under user-controlled recovery key, with demonstrated restoration tests; if all original secrets lost, no custodial magic.

### DQ-078 — RECOMMENDATION
**Question:** Can one wallet be securely used on multiple devices simultaneously, including concurrent Authenticator tokens?
**Answer:** Prefer single active signing device initially; independent read-only secondaries okay, coordinated multisig/multi-device signing is later independently audited feature.

### DQ-079 — RECOMMENDATION
**Question:** Will TongNet Wallet and TongNet Authenticator be separate apps, hardware devices, or available in multiple configurations?
**Answer:** Separate Wallet and Authenticator apps by default; hardware second factor optional; secure OS integration with defensible recovery/risk model.

### DQ-080 — RECOMMENDATION
**Question:** How will users recognise phishing apps, malicious updates, deceptive QR codes and fake network nodes?
**Answer:** Reproducible signed binaries, attestable publisher keys, transaction content verification, security education and anti-clone app detection.

### DQ-081 — RECOMMENDATION
**Question:** What should happen if a software bug wrongly labels a wallet DEAD or falsely accepts a recovery? Is there any governance recourse consistent with immutability?
**Answer:** False DEAD/false pairing is a catastrophic safety invariant; fail-closed prior to finality, audit evidence and governance fixes going forward, no silent owner undo of completed ledger.

### DQ-082 — RECOMMENDATION
**Question:** Who can change the protocol, and how are proposed rules published, approved and audited without unilateral ParmTech control?
**Answer:** Versioned on-chain upgrade proposals, multi-epoch timelocks, independently verifiable approvals, code audit and optional user fork with documented split risks.

### DQ-083 — RECOMMENDATION
**Question:** How will privacy requests (e.g. deletion) interact with immutable spent-state evidence?
**Answer:** Do not store sensitive off-chain metadata longer than necessary; immutable ledger commitments cannot be selectively erased, disclose privacy limits clearly.

### DQ-084 — RECOMMENDATION
**Question:** What should testnet success criteria be (e.g. verified double-spend invariant under partition, audited recovery state, reproducible test runs)?
**Answer:** Formal model and property tests for money conservation, one-use keys, partition safety, delay credits, recovery, queued expiry and disaster edge cases, public reproducible testnets.

### DQ-085 — RECOMMENDATION
**Question:** How will critical vulnerabilities be privately reported and patched after public release?
**Answer:** Independent vulnerability disclosure, severity triage, audited security releases, on-chain time-locked upgrades and emergency pause of *new settlements* only under published rules.

### DQ-086 — RECOMMENDATION
**Question:** What hard launch blockers should prevent any real-money adoption until solved?
**Answer:** NO real money before audited BFT+reconfiguration, Sybil model, secure deadline calculator, safe reserve treatment, wallet and token economics, legal clearance and adversarial testnet.

### DQ-087 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** While a transfer is PENDING_TRIGGER and disaster recovery makes source DEAD, keep lock until original 3h timeout, then automatically refund into prebound disaster recovery wallet; no early cancellation.
**Answer:** CONFIRMED Q7: untriggered 3h lock returns automatically to pre-bound recovery wallet R if the source became DEAD; no early manual cancellation.

### DQ-088 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Destination R must ACCEPT from its own BlackBox; issue key there and finalize irreversible binding only after acceptance. No acceptance means NOT_CONFIGURED. Cryptographic signature/proof engineering pending.
**Answer:** CONFIRMED Q9: source request creates no pairing; R BlackBox Accept finality alone issues key there and permanently binds S→R.

### DQ-089 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Unanswered destination BlackBox pairing request expires after 24 hours and can never subsequently be accepted. No link/key in PENDING or EXPIRED. Exact consensus boundary implementation still open.
**Answer:** CONFIRMED Q10: nominal 24h pairing timeout; Q15 verifiable network delay adjusts effective deadline, so nominal expiry is not necessarily absolute.

### DQ-090 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Main source wallet cannot cancel, withdraw or supersede pending disaster pairing; waits for R Reject or auto Expired at 24 hours. No config until Accept.
**Answer:** CONFIRMED Q11: source cannot cancel/replace a PENDING pairing request; waits for R Reject or valid adjusted expiry.

### DQ-091 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** STRICT: destination BlackBox Accept must be consensus-final before original 24h pairing deadline. Late network finality means expired even if signed or clicked earlier. User's local clock cannot establish acceptance.
**Answer:** CONFIRMED Q12 adjusted Q15: only Accept network-final strictly before its verifiably extended effective cutoff creates key/binding.

### DQ-092 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** User wants no clock slowdown/pause for ordinary network congestion; queue new submissions and start NEW timers on network acceptance. What to do about total network inability to finalize an already-running claim before a loss/forfeiture deadline remains open.
**Answer:** CONFIRMED Q13 Q15: new task timer starts on network final acceptance, prior queue waiting does not also inflate the new timer; running deadline receives eligible network-induced compensation.

### DQ-093 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Receiver/Sender Claim queued or signed before cutoff but finalized after deadline is EXPIRED. Only strict network finality before each pre-existing receiver 24h / sender following 72h cutoff grants claim.
**Answer:** CONFIRMED Q14 adjusted Q15: recipient/sender Claim requires finality strictly before eligible compensated deadline, not queued/signature-only.

### DQ-094 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** User specified one-for-one time allowance for NETWORK-caused delay, UNIVERSAL to all affected timed operations. Affected funds must not be irreversibly forfeited to reserve before adjusted windows finish; total outage proof/calculation and forfeiture legality still unresolved.
**Answer:** CONFIRMED Q15: ALL timed tasks receive eligible network-delay time one-to-one; no automatic reserve forfeiture before adjusted rights finalise.

### DQ-095 — CONFIRMED (or consistent with a previously confirmed user rule)
**Question:** Should each network task's allowed extra time come from individually verifiable processing/queue delay, or a single global Network Delay Calculator measurement for all affected tasks? Define consensus proofs, exclude client-caused inactivity and avoid crediting the same interval twice.
**Answer:** CONFIRMED Q16 C: HYBRID per-operation verified delay PLUS global network-health evidence, account each overlapping time interval once, not individual+global arithmetic sum.

## Additional explicit Q17–Q25 user decisions (not part of original 95 numbered DQ backlog)

| User question | User-confirmed choice | Interpretation / security requirement |
|---|---|---|
| Q17 | C | Compare independent relay/node proof to reject fabricated individual delays; signed evidence plus adversarial tests. |
| Q18 | C | Cryptographic consensus on delay evidence; when insufficient, no conflicting finalisation; affected escrow in PROTECTED_SUSPENSE until publicly defined resolution. |
| Q19 | C | Decentralised Anti-Sybil, verifiable independent validator eligibility, unpredictable committee selection; actual scarce-resource model remains research. |
| Q20 | C | Hybrid evolution: verified independent initial operators, eventually permissionless only after genuine Sybil-resistant enrollment; phase 1 cannot be honestly called 100% permissionless. |
| Q21 | C | Fully automated rules for add/remove/suspend; no manual single-owner override, provided objective evidence and eligible on-chain membership model. |
| Q22 | B | Quarantine on proved protocol-defined suspicious evidence, independently review cryptographic evidence, restore innocents/remove proven faulty validators. |
| Q23 | B | Automatically activate eligible preverified backups where safe; if quorum cannot be established, halt new finality. |
| Q24 | C | Only secure overlapping quorum can finalise after partition; neither 60 nor 40 of 100 satisfies a strict >2/3 equal-weight quorum. |
| Q25 | B | Precommitted backup rotation only if it cannot create two independently live conflicting committees; else fail-closed. |

## Corrections / supersession ledger

1. **Strict expiry Q12/Q14 must use Q15 network-delay-adjusted cutoff**; do not enforce obsolete unextended original deadline when eligible delay is proved. Still require FINALITY before adjusted cutoff.
2. **Q16 hybrid** and **Q17–Q18** are user-confirmed but proofs/algorithm remain missing. Never present the calculator as developed.
3. The original backlog contains entries marked OPEN even though user decisions Q5–Q25 settled portions of them. The Q&A above reconciles these without fabricating implementation evidence.
4. **Forced Network Reserve confiscation** after unclaimed 96h is prior user intent, NOT a legally cleared mechanism. Recommended change to protected/sender refund rather than confiscation is unapproved, high-priority owner decision and real-money launch blocker.
5. **Fully automated permissionless validators** cannot launch safely solely on node signatures, committee rotation, stake caps, AI reputation or 'unique' algorithms; an independently tested economic/identity Sybil resource and BFT finality guarantee remain necessary.
6. **Zero fees** cannot also mean unlimited free spam/no one pays network costs. Use sponsored quota plus transparent minimal excess fees as candidate policy, not a promise of zero cost.
7. **Research benchmarks** (<2s median, <5s P95 and >=1k sustained TPS) are suggested targets, not measured network figures.
8. **Originality:** novel product-level assembly may be protectable, but prior art/licences and patentability need specialist review; standard maths/cryptography intentionally reused for security.

## References
- CometBFT safety / weighted quorum: https://github.com/cometbft/cometbft/blob/main/spec/consensus/consensus.md
- Narwhal/Tusk BFT dissemination vs ordering: https://doi.org/10.1145/3492321.3519594
- Mysticeti low-latency DAG research: https://docs.sui.io/paper/mysticeti.pdf
- NIST postquantum: https://csrc.nist.gov/projects/post-quantum-cryptography
- AUSTRAC Australia VASP registration: https://www.austrac.gov.au/new-austrac/register-us/register-us-remittance-or-virtual-asset-service-provider
- ASIC classification/licensing: https://www.asic.gov.au/regulatory-resources/digital-transformation/digital-assets-financial-products-and-services
