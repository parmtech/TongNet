## 2026-10-25 — Master architecture whitepaper v1.0 published (design only)

> **NEW 2026-10-25 ARCHITECT-SELECTED MASTER DESIGN / NOT DEPLOYED:** The [TongNet Master Network Whitepaper v1.0](docs/WHITEPAPER_MASTER_V1_0.md) contains the end-to-end reference plan: one native TONG coin, native account-based escrow state, voluntary bonded PoS with reviewed BFT, 64 active / 32 standby validator and full-node **targets**, optional PoTP audits only (never own-transaction voting), 24h Receiver + 60d Sender with manual BlackBox FINAL_ACCEPT, ACTIVE Recovery Mirror V4/DEAD-target auto-unbinding, safety/collusion threat model, candidate 100m monetary cap/12m genesis and 25 engineering/risk sections with 65 FAQs. **Numerical/economic choices are reference candidates, NOT earlier owner-ratified parameters, audited implementations, minted TONG, performance measurements or launch promises. Hard blockers remain: conditional archive decryption, late K_S loss, network delay compensation, reserve forfeiture legality, stake succession, genesis distribution, independent audits. Latest owner payment/recovery overrides still take precedence over obsolete text below.**

## 2026-10-25 — Owner narrows TongNet to Bitcoin-like single native-coin blockchain

**LATEST OWNER PRODUCT SCOPE — Single native TONG coin, Bitcoin-like chain (2026-10-25):** TongNet is a dedicated independent cryptocurrency/blockchain for its own native **TONG** coin and its built-in secure bilateral BlackBox P2P/recovery protocol. Owner expressly REJECTED assistant-proposed Ethereum-like general-purpose application platform: **no public arbitrary smart contracts/EVM, no user-created tokens, no dApp ecosystems or app marketplace**. Wallet, BlackBox, Authenticator, explorer and node tools are first-party network clients, not a general-purpose dApp platform. Aspirations: improved practical user security and faster secure settlement compared with aspects of Bitcoin, **not an unproven claim of being mathematically more secure than Bitcoin**. Bitcoin-like use case does NOT automatically mandate Bitcoin Proof-of-Work mining: PoW vs hybrid BFT (and issuance/monetary policy) remain explicitly UNDECIDED. UTXO is a proposed accounting baseline, not approved. Latest [scope specification](docs/TONGNET_BITCOIN_LIKE_SCOPE.md); prior general-purpose/token platform proposals are historical/unapproved.

## 2026-10-25 — auto-unbind recovery destination on consensus-final DEAD (owner confirmed)

The recovery destination R must be ACTIVE. Pairing source S→R is fixed while R ACTIVE, but if R becomes finally DEAD for ANY cause, consensus automatically revokes active S→R recovery entitlement while preserving audit history. S stays ACTIVE but immediately has **NO RECOVERY**, so S may enroll a fresh eligible ACTIVE R2 with R2 BlackBox approval. No automatic fallback through R's own recovery wallet (S→R, R→C does NOT mean S→C when R dies). No ordinary offline status can cause unbinding; chain-final DEAD required. Enforce atomic reverse-index updates, ACTIVE checks at recovery-execution finality, deterministic races, no double transfers or sealed-parent BlackBox disclosure to R's successor. User must be visibly warned that original S loses protection until new pairing succeeds; if S keys are already missing, A→new-R may be impossible. Retention/cryptographic shredding of old mirrored ciphertext remains research. Latest [Active Recovery Mirror V4](docs/ACTIVE_RECOVERY_MIRROR_V4.md). Product decision only, no code/security proof.

## 2026-10-25 — Recovery target remains fully active; independent sealed parent archive

> **LATEST 2026-10-25 OWNER OVERRIDE — ACTIVE Recovery Target (V4):** Pairing S→R no longer freezes R. BOTH S and R remain NORMAL_ACTIVE independently, and R may set its own successor C; sealed encrypted **S BlackBox archive only** mirrors to R, with permanent parent S provenance and no S ledger transaction migration. R's own BlackBox/payments stay usable. On BFT-final authorised disaster S→R, S becomes DEAD, only eligible unlocked S funds transfer once to already-active R, and archive S may decrypt; R stays active. Old freeze and ordinary-transaction block rules superseded; fresh-at-binding requirement remains. A separate audited conditional key-release scheme is needed for real pre-recovery unreadability; B becoming DEAD before A needs an explicit rule. Canonical V4: docs/ACTIVE_RECOVERY_MIRROR_V4.md. [V4 specification](docs/ACTIVE_RECOVERY_MIRROR_V4.md)

## 2026-10-25 — User decisions: trusted-only bilateral P2P; 60-day sender reclaim; recovery-only successor wallet

**UPDATE 2026-10-25:** User explicitly chose trusted bilateral P2P/no deal-arbitrating third party; 24h Receiver exclusive priority followed by **60 FULL DAYS** Sender-exclusive manual reclaim (previous 72h replaced), then creator intends Reserve transfer but real-money forfeiture BLOCKED for safety/legal review. Recovery destination R must be FRESH/no prior financial transfers, stay RECOVERY_RESERVED with normal send/receive disabled until a successful recovery; R then succeeds S as ACTIVE, S becomes DEAD. Historic ledger is linked, not rewritten, and BlackBox copy requires preexisting encrypted backup. Network-final LOCK as new receiver 24h clock anchor remains proposed. Source-BlackBox lost/DEAD and late K_S are unresolved. See [LATEST canonical owner decisions](SECURE_P2P_V3_RECOVERY_DECISIONS.md). Historical contradictory older rules below are superseded.

## 2026-10-25 — Trusted bilateral P2P; 60-day sender recovery; reserved successor Recovery Wallet

**LATEST OWNER REQUIREMENTS — 2026-10-25:** Trusted two-party P2P with no deal arbitrator; validators verify signatures/finality, not buyer/seller disputes. The RECEIVER has the first 24h (clock at final LOCK proposed, not yet ratified). The SENDER then has **60 DAYS**, replacing earlier 72h, to manually reclaim; after that, creator wants remaining unclaimed escrow sent to Network Reserve (OWNER INTENT, **REAL-MONEY DEPLOYMENT BLOCKED** by unresolved legal/consumer protection safety). A special *fresh*, zero-prior-financial-transactions RECOVERY_RESERVED address may complete recovery pairing metadata but CANNOT ordinarily send/receive before one-time disaster-recovery settlement. After successful recovery, S becomes DEAD and R is successor NORMAL_ACTIVE; owner wants historical receipts, BlackBox encrypted backup and pending entitlements shown in R, not destructive rewriting of immutable ledger. Preexisting recoverable encrypted BlackBox backup is REQUIRED to restore lost device data; a lost unbacked secret cannot be resurrected, and wallet/master root secrets must never be sent to a website server. Late sender claim key K_S with LOST/DEAD BlackBox, pending consent migration, exact 24h anchor, and legal forfeiture remain OPEN. See [canonical 2026-10-25 decisions](docs/SECURE_P2P_V3_RECOVERY_DECISIONS.md). Older Trigger/72h/recovery-descriptions are HISTORICAL.

## 2026-10-25 — owner removes 3h Trigger; Sender final ACCEPT is sole release gate

**CURRENT RULE — 2026-10-25 (SUPERSEDES ALL OLD 3h TRIGGER CONTENT):** User REMOVED separate three-hour Trigger and its 3h automatic refund. Current TongNet Secure Manual P2P: Sender network-final LOCK -> Sender BlackBox makes and privately shares one-time Receiver Claim Code K_R -> exact addressed receiver wallet signs Claim Request -> Sender BlackBox must manually FINAL_ACCEPT exact transaction/recipient/amount -> BFT may finalise receiver settlement. No FINAL_ACCEPT means no receiver payout. No separate Trigger remains. Receiver 24h then Sender's following 72h manually redeemable via fresh Sender BlackBox K_S (verified attributable network delay extensions still apply); 24h from BFT-final LOCK is recommended but not explicitly ratified. No valid absolute guarantee against mistaken approval, stolen signing authority or third-party fraud. Old 3h Q7 disaster refund is obsolete; source DEAD + late K_S needs safe redesigned handling. See [canonical Secure P2P v2](docs/SECURE_P2P_V2.md) (for docs/ files: [canonical v2](SECURE_P2P_V2.md)).

## 2026-10-25 — New manual sender approval for receiver claim

- User explicitly added requirement that receiver's externally shared K_R and wallet signature only submit CLAIM REQUEST. Request returns to Sender BlackBox; Sender manually ACCEPTS; only BFT-final cryptographic approval settles funds to recipient.
- No manual Reject necessary; lack of acceptance by receiver's adjusted 24h deadline results in Receiver claim expiry and following 72h sender-only reclaim key stage. No automatic 24h refund.
- Preserved previously confirmed 3h Sender Trigger as distinct until owner explicitly requests merging it with ACCEPT; no extra unilateral cancellation right was introduced.
- Added transaction-bound final approval, wrong-recipient displayed detail, replay prevention and BFT deadline/race testing gates. No software/security proof has been completed.

## 2026-10-25 — User-confirmed TWO Claim Keys generated in Sender BlackBox

- User clarified normal transaction receiver claim code K_R originates in Sender BlackBox at setup and is manually given to intended receiver; unlike previous spec it is NOT generated/delivered automatically by Receiver BlackBox. It only becomes usable after final Trigger, for up to 24h by the transaction's addressed receiver wallet + code.
- Upon nonclaim at adjusted receiver cutoff, first code expires and a NEW sender-only K_S is generated by Sender BlackBox for the following 72h, after which it expires. Eligible verified network delay extensions apply; sender's claim is manual, NOT automatic refund at 24h.
- Wrong address recovery follows because code without bound wallet authority (or wallet authority without code) is insufficient. Wrong recipient who also learns code can still claim.
- Recorded unresolved technical contradiction with prior Q6 disaster recovery: lost/DEAD sender BlackBox cannot guarantee generation of a NEW later sender key; user needs to decide literal late creation vs previously sealed later activation. Preserved independent destination-generated permanent Disaster Recovery Key.
- All changes are documentation/specification only; no software, testnet or security audit completed.

## 2026-10-25 — USER CORRECTION: fast manual secure P2P, NOT Instant Pay

- User explicitly rejected the prior assistant-suggested Instant Pay direction. TongNet's defining transfer is intentionally **manual two-sided P2P**, requiring sender Send + independent BlackBox Trigger and receiver independent BlackBox Claim; original 3h/24h/72h maximum windows remain, and online parties need not wait for window expiry.
- Instant Pay is NOT the accepted default/implementation; earlier product critique's instant checkout concept is historical/rejected for present scope.
- Investigating one-time receiver-signed Receive Request for wrong-address protection; mandatory vs optional not yet authorised. Distinguish public receiving invitation from private recipient Claim Key; signatures do not prove off-chain identity.
- No running chain, measured fast finality, audited encryption or live transfer exists yet.

## 2026-10-25 — Red-team product review: who will use TongNet and why?

- Created [Critical Product/Banking/Adoption Plan](docs/TONGNET_PRODUCT_CRITIQUE_AND_ADOPTION_PLAN.md) after user's request for strong critical questioning, competitive differentiation, real merchant usage, trust and system-level improvements.
- Found material UX gap: existing user-confirmed Send/Trigger + receiver 24h Claim is not an ordinary fast merchant payment mechanism. Suggested a **separate, unconfirmed `Instant Pay` mode**, preserving the entire old `Protected Pay` route rather than silently replacing confirmed rules.
- Added 20 adversarial questions/answers, competition review, low-fee funding, independent operator count safety, hypothetical 1B TONG supply denomination (NOT RATIFIED), bank/fiat integration and Australian legal gates, measured pilot/adoption plan.
- Synced README, decisions, architecture, roadmap, progress and session handoff. No software deployed, bank licence issued or coin minted by this documentary review.

## 2026-10-25 — Primary TongNet implementation language chosen: Rust

- At owner's explicit request to select the best language, selected **Rust** for the security-critical network, deterministic BFT state machine, validators, P2P, delay calculator, cryptographic wallet/BlackBox and shared cross-platform libraries. Keep Kotlin/Swift/native UI only where beneficial; don't make C/C++ a primary protocol implementation language.
- Updated research architecture, README, Decision Register, Roadmap, Progress and session handoff. **Planning only:** no Rust implementation, benchmark, audit or security guarantee exists yet.

## 2026-10-25 — Whole-project technical review, 95 Q&A and Q16–Q25 decisions

- Read all 95 tracked deep questions and generated [Master Q&A Recommendations](docs/MASTER_QA_RECOMMENDATIONS.md), preserving exact old questions and clearly distinguishing user-chosen rules from unapproved engineering recommendations. This is design, not implementation.
- Created [TongNet Future Architecture](docs/TONGNET_FUTURE_ARCHITECTURE.md): BFT deterministic-finality research baseline, parallel dissemination/execution candidates, hybrid anti-Sybil and optional stake-like bonding, cryptographic agility, measurable testnet targets and realistic sponsored-fee economics.
- User confirmed Q16 C hybrid global+individual delay, Q17 C independent fabricated delay checks, Q18 C evidence consensus/protected funds, Q19 C anti-Sybil committees, Q20 C staged opening, Q21 C rule-based automated validators, Q22 B quarantine, Q23 B standby replacements, Q24 C partition quorum, and Q25 B preauthorised safe epoch/backup rotation.
- Explicitly rejected unjustified claims that current TongNet has a running network, measured TPS, proven novelty, unconditional zero-fee sustainability, automatic full decentralisation or formal network delay attestation.
- Clearly flagged unresolved mandatory legal/consumer approval for proposed confiscation of 96h-unclaimed escrow into Network Reserve. Review does NOT unilaterally rewrite confirmed protocol rights.
- Synced README, project decisions, protocol, security, recovery, FAQ, progress, roadmap and session handoff. No secret material or live funds touched.

## 2026-10-25 — Q15 confirmed: universal network-delay compensation across EVERY timed operation
- User expanded the rule explicitly beyond Claims: **every** TongNet transaction/task with a network-affected deadline must get one-for-one extra allowed time equal to network-induced verified delay, using a proposed Network Delay Calculator. Included Send/Trigger, receiver and sender claims, recovery setup/BlackBox acceptance and other time-bound operations.
- Running clocks remain normal; compensated **effective deadlines** move. Q12 and Q14 still require consensus finality strictly before the adjusted deadline. Newly submitted tasks' clocks start only upon network acceptance, with queue wait before start not double-credited.
- Dependencies must shift deterministically: do not start sender reclaim while receiver's delay-adjusted priority survives, do not issue a 3h refund while Trigger remains eligible, and do not forfeit escrow to Network Reserve while a legitimate adjusted claim remains.
- Actual delay attribution, per-task vs network-wide calculation, Sybil resistance, validator consensus time and outage measurement are NOT yet resolved or implemented; legal/consumer safeguards on reserve forfeiture remain an absolute launch blocker.
- **NEXT Q16:** per-operation verifiable queue delay versus common network-wide slowdown calculation.

## 2026-10-24 — Q14: Strict claim finality before financial expiry
- User selected Option A: original 24h Receiver Claim and subsequent 72h Sender reclaim each require network consensus FINALITY strictly BEFORE their established deadline. A pre-deadline click, signature, relay receipt or placement in queue does not stop expiry if finality arrives late. A late-finalized Claim is EXPIRED.
- This is distinct from new Send timer starting upon initial network acceptance as discussed in Q13; no running protocol has yet implemented either rule. Validators must implement atomic ordering, replay protection and deadline checks.
- Outstanding launch risk: a complete network outage can make all Claims impossible and allow the proposed 96h reserve forfeiture to take away funds. No legal or consumer protection clearance is established. **NEXT Q15:** what happens to unclaimed escrow after a long network outage?
- Updated Decisions, Protocol, FAQ, Security, deep question backlog, Progress, next-session handoff, Roadmap, README and Disaster Recovery cross-reference.

## 2026-10-24 — Q13: queue requests; new timers start on network acceptance (user direction)
- User wants already-started timers to run at their original rate independent of slow/fast network; load-balancing and transaction/task queueing are desirable.
- A NEW transaction timer must begin only when the NETWORK ACCEPTS the new operation. Technical recommendation: define acceptance as network consensus finality, not local/relay queue-admission receipt. Proposed stages LOCAL → SIGNED → QUEUED_NONFINAL → CONSENSUS_FINAL, with timer starting only at finality.
- Do NOT represent QUEUED as successful funds movement, nor guarantee a late Claim will succeed. Existing receiver/sender claim windows that began earlier continue separately; handling congestion/full outage and proposed reserve forfeiture requires additional explicit decisions and legal/consumer review.
- Updated decision register, draft protocol, FAQ, security risk register, deep question backlog, progress, handoff, roadmap and README. These are design proposals; no running consensus network exists.
- **NEXT Q14:** queued before already-running claim deadline but finalized after: strict expiry vs securely provable early receipt?

## 2026-10-24 — Q12: Strict network-finalized acceptance before expiry
- User selected **Option A**: a Disaster Recovery Wallet request must receive an ACCEPT with definitive network finality strictly before its original 24-hour request deadline. Earlier button press, signature or intermediate network receipt cannot override late finality.
- If confirmation is finalized late, request remains EXPIRED and NO Disaster Recovery Key or permanent link is issued. Consensus clock, network partitions and deterministic race handling remain unimplemented and untested.
- The rule is specific to recovery-pairing registration; separate **Q13** will resolve receiver and sender payment-claim deadlines during network-wide outages.
- Canonical decision register, FAQ, protocol, threat model, deep question backlog, progress and next-session handoff revised.

# TongNet — Documentation & Project Change Log

## 2026-10-24 — Q10 confirmed: pending pairing request expires after 24 hours
- User chose **Option A**: unanswered Disaster Recovery pairing request automatically expires after **24 hours**.
- While PENDING and after EXPIRED the source wallet is NOT_CONFIGURED: no recovery key, no irreversible source→destination binding.
- Late destination Accept on expired request must be rejected. Exact network clock, accepted-before-expiry finality and concurrent action ordering still need design and tests.
- Updated disaster recovery requirements, decision register, FAQ, protocol, threat model, backlog, progress, and next-session handoff.
- **NEXT Q11:** may source withdraw/replace a pending request before destination responds?

## 2026-10-24 — Q9 confirmed: destination BlackBox Accept/Reject handshake
- An irreversible disaster recovery address is NOT linked immediately when SOURCE proposes it; S Wallet Private Key + S Authenticator sends an initial request to destination R's encrypted BlackBox.
- Until R actually ACCEPTS, status remains PENDING/NOT_CONFIGURED; no one-time secret is issued and no immutable source→destination pairing exists.
- R BlackBox ACCEPT generates the unique one-use Disaster Recovery Key INSIDE R BlackBox and permanently confirms the binding. REJECT generates no key/link and sends a rejection response into S's BlackBox. Ignoring the request leaves it PENDING and unconfigured.
- Actual authenticated Accept proofs, atomic finality, and request replay/races need implementation and audit; this is not proof of shared human identity.
- **NEXT Q10:** how long can unanswered pairing request remain pending before it expires?

## 2026-10-24 — Q8 clarification: one-time key generated inside DESTINATION BlackBox
- Source wallet owner initiates optional irreversible disaster destination association from normal Wallet Settings, with source Private Key and TongNet Authenticator as already confirmed.
- User specifies the unique, immutable one-time Disaster Recovery Key MUST be generated within the selected recovery DESTINATION Wallet's own TongNet BlackBox, not the source BlackBox.
- Owner later supplies this very key together with source Wallet Private Key to execute Run Disaster Recovery once; source BlackBox and Authenticator are not needed at execution.
- Distinguish delivery/creation of a secret from a signed proof that recovery destination actually approved the pairing. No cryptographic destination acceptance requirement confirmed yet.
- **NEXT Q9:** Pairing final only after independent destination BlackBox acceptance, or immediately after source approval and destination-side key generation?

## 2026-10-24 — Q7 answered: original 3-hour expiry refund goes to bound recovery wallet
- User selected **Option A**. If original wallet becomes DEAD after a successful disaster sweep while a separate outgoing payment is **locked but NOT Triggered**, do not cancel or accelerate the original 3h window.
- At original t0+3h, automatically refund its untriggered locked amount directly to already-authenticated Disaster Recovery Wallet R, not DEAD source S. S cannot Trigger after DEAD; race order and atomic finality need formal proof.
- Updated FAQ, Decision Register, disaster design, security/protocol, question backlog, progress and session handoff.
- **Next Q8 / DQ-002:** Does destination Recovery Wallet have to sign consent/control proof at its irreversible initial registration?

## 2026-10-24 — Q6 answered: rescue spendable funds; preserve Triggered escrow
- User confirms terminal Disaster Recovery immediately transfers only available funds to immutable bound rescue wallet (minus any applicable fee), leaving all previously Triggered/locked escrow untouched.
- Receiver keeps original 24-hour claim priority; if unclaimed, during the next 72 hours the **same existing, unspent sender Claim Key** can be used from **the immutably linked rescue wallet**, but only if original source disaster recovery has already finalized.
- User must still possess that sender Claim Key; BlackBox loss does not magically reissue it. The sender claim remains single-use and original time window stays unchanged. If unclaimed at final deadline, creator-proposed reserve path remains a legal/consumer-protection blocker.
- The bound wallet address is cryptographically authorised; do NOT pretend it proves both wallet addresses belong to the same person.
- **Open Q7:** an original payment still in 3h PENDING_TRIGGER (not yet Triggered) must auto-refund. Where should its money go once the original wallet is DEAD?

## 2026-10-24 — Q5 answered: initial disaster setup is two-factor
- User selected **Option A**: immutable recovery wallet address can be registered only with BOTH Wallet Private Key and TongNet Authenticator approval.
- This applies to ONE-TIME initial registration, not to later Run Disaster Recovery (which still requires Wallet Private Key + Disaster Recovery Key, not Authenticator).
- Updated Decision Register, Disaster Recovery specification, FAQ, Protocol, Security, Deep Questions checklist, Progress and Next Session handoff.
- **NEXT Q6:** handle funds already locked in outgoing transfers when source wallet is terminally swept/dead; preserve prior receiver claim rights, avoid double-spend.

## 2026-10-24 — Exhaustive technical questioning backlog
- Added [docs/DEEP_QUESTIONS.md](docs/DEEP_QUESTIONS.md) with 86 unanswered security, logic, engineering, economics, privacy and governance questions.
- Agreed workflow: ask meaningful questions one-by-one, save decisions and update the active next-session handoff; keep extending backlog instead of stopping after a short questionnaire.
- **NEXT:** initial setup authorisation of irreversible disaster recovery destination, Q5.

## 2026-10-24 — Q3/Q4 Disaster Recovery immutability and key rules
- Optional immutable Disaster Recovery Wallet destination registered in normal Wallet Settings; at setup user is issued a distinct optional one-time Disaster Recovery Key.
- THREE keys: Wallet Private Key, TongNet Authenticator Master Key, optional Disaster Recovery Key.
- Run Disaster Recovery requires original Wallet Private Key **and** the distinct Disaster Recovery Key; no BlackBox/Authenticator code needed.
- On successful final settlement, rescue all eligible funds less actual fee to *already recorded* destination, consume the recovery key once and irreversibly mark source wallet DEAD.
- Destination address and recovery key cannot **ever** be edited, replaced, regenerated or reset. Losing the disaster key means that route cannot be used.
- If Wallet Private Key and Authenticator Master Key are both accessible, owner can still use normal transfers to send to a different wallet, not change disaster configuration.
- Still undecided: initial setup authorization, conflicts with already locked/triggered transfers and atomic consensus.
- **NEXT Q5:** Wallet Private Key alone, or Wallet + TongNet Authenticator for initial recovery address configuration?

## 2026-10-24 — Question 2 answered and committed
- User confirmed that failure to activate TongNet Authenticator within the wallet's first 72 hours makes that wallet **permanently DEAD** and it can never be reactivated, irrespective of later possession of its keys.
- No replacement of the lost first-time Setup Key to bypass the deadline. Wallet must be replaced; initial inactive wallets cannot SEND, RECEIVE or CLAIM.
- Updated decisions, FAQ, protocol, progress and next-session handoff. Security threat-model update is still pending because the GitHub edit was blocked; no production protection is implemented or tested.
- **Next Q3:** loss of Authenticator Master Key/device after a wallet has successfully activated.

## 2026-10-24 — Question 1 answered and committed
- User explicitly chose **Option B** for wrong receiver address after Trigger: **no cancellation, no emergency stop, even for erroneous address**.
- Receiving address still has 24h to claim; sender can recover during subsequent 72h **only if no receiver claim succeeds**.
- Updated decision register, FAQ, draft protocol, threat model, progress and session handoff.
- **Next Q2:** lost one-time Authenticator Setup Key before completing 72-hour activation.

## 2026-10-24 — Initial project documentation on GitHub
- Verified `manbir6-ux/TongNet` is a private repository accessible for writing.
- Replaced placeholder README with branded TongNet scope and official credits.
- Prepared FAQ, decision register, protocol sketch, security risks, history, research architecture, prior-art ledger, roadmap, progress and session handoff.
- Reconciled historic working name SIFAR Mesh → **TongNet** and native asset **TONG**.
- Recorded corrected creator-reported concept origin **2015**, not 2016; public disclosure reported for 2026.
- Recorded locked/no-manual-cancel 3h pre-trigger rule; subsequent 24h receiver claim; 72h sender-only recovery; proposed final network reserve transfer.
- Documented unsolved consensus, value, key-loss and legally sensitive forfeiture issues.
- **Next:** ask user about wrong recipient address *after Trigger but before claim*, then commit answer.

## Historic discussion (not evidence of commits)
- 2026-10-24: initial zero-fee, no-mining/no-traditional-staking vision.
- 2026-10-24: separate BlackBox and TongNet Authenticator proposed.
- 2026-10-24: payment timed rules iterated from 1-hour claim to 24-hour claim and from various recovery windows to additional 72h.
- 2026-10-24: sender explicitly declined pre-trigger manual cancellation; no Trigger leads to refund at 3h.
- 2026-10-24: model renamed TongNet; company-author ParmTech and creator Manjinder Singh specified; concept year corrected to 2015.

**Change-log rule:** Append dated, factual entries for every new design answer, code change, test and release. Do not claim a task is completed without evidence.
