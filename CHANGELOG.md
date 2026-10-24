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
