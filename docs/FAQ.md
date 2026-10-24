# TongNet — Living FAQ (planning)

> **CURRENT RULE — 2026-10-25 (SUPERSEDES ALL OLD 3h TRIGGER CONTENT):** User REMOVED separate three-hour Trigger and its 3h automatic refund. Current TongNet Secure Manual P2P: Sender network-final LOCK -> Sender BlackBox makes and privately shares one-time Receiver Claim Code K_R -> exact addressed receiver wallet signs Claim Request -> Sender BlackBox must manually FINAL_ACCEPT exact transaction/recipient/amount -> BFT may finalise receiver settlement. No FINAL_ACCEPT means no receiver payout. No separate Trigger remains. Receiver 24h then Sender's following 72h manually redeemable via fresh Sender BlackBox K_S (verified attributable network delay extensions still apply); 24h from BFT-final LOCK is recommended but not explicitly ratified. No valid absolute guarantee against mistaken approval, stolen signing authority or third-party fraud. Old 3h Q7 disaster refund is obsolete; source DEAD + late K_S needs safe redesigned handling. See [canonical Secure P2P v2](docs/SECURE_P2P_V2.md) (for docs/ files: [canonical v2](SECURE_P2P_V2.md)).


**Read with:** [DECISIONS.md](DECISIONS.md), [PROTOCOL.md](PROTOCOL.md), [SECURITY.md](SECURITY.md).  
**Status legend:** CONFIRMED REQUIREMENT = user-stated design instruction; PROPOSAL = explored, not finally agreed; OPEN = needs a user decision, research, or feasibility verification. A confirmed *requirement* does not mean the system is built or safe.

## Identity, goals and origin

**Q: What is TongNet?**  
A: A proposed fully decentralised financial transfer network with the TONG native coin. No PoW mining or traditional PoS dependency is desired. **CONFIRMED GOAL; no consensus design selected.**

**Q: Who created it?**  
A: Project author/company ParmTech; original concept creator and developer Manjinder Singh. Concept-origin year **2015** (creator-stated), kept private until the creator-reported first disclosure in **2026**. The former working name SIFAR Mesh is superseded by TongNet. **CONFIRMED naming/attribution and creator-stated timeline.**

**Q: Is TongNet demonstrably original?**  
A: Not verified. Escrow, HTLCs, secret-based claims, multisig, TOTP and private messaging have prior art. Distinctive combinations require rigorous prior-art and legal review. **OPEN research.**

**Q: Is TONG asset-backed or pegged?**  
A: The user wants genuine economic value; an AUD-backed redeemable unit was floated as an illustration, **NOT an adopted peg**. Reserve, custody, redemption and tokenomics are **OPEN**.

## Wallet and authenticator

**Q: What is created with a wallet?**  
A: A wallet address/key set and separately protected TongNet BlackBox; a one-time authenticator setup credential. **CONFIRMED DESIGN.**

**Q: Is the BlackBox key the wallet key?**  
A: No. User wants separate security boundaries, with a separate TongNet Authenticator. The BlackBox must not be operable using only a compromised wallet key. **CONFIRMED REQUIREMENT.**

**Q: How is TongNet Authenticator enrolled?**  
A: Earlier recorded specification: use wallet private-key authorisation plus one-time setup credential, without requiring initial BlackBox login. The setup credential becomes invalid after enrolment. **RECORDED REQUIREMENT, cryptographic details OPEN.**

**Q: What if enrolment does not occur within 72 hours?**  
A: **CONFIRMED again in Question 2 (2026-10-24):** when the first 72 hours after wallet creation end without completed TongNet Authenticator activation, wallet becomes permanently **DEAD**. It can never be reactivated, including through any administrator or later possession of the old keys. SEND, RECEIVE and CLAIM remain unavailable. A new wallet must be generated. Real implementation still requires protocol tests and expiry boundary definition.

**Q: Does the master secret change every minute?**  
A: No: a stable, separate authenticator root secret yields **60-second rotating access codes**. A code is not itself a robust transaction signature. **CONFIRMED BEHAVIOUR; implementation OPEN.**

**Q: Can an authenticator root secret alone reveal a wallet or unlock its BlackBox?**  
A: Requirement is **no**, as long as other cryptographic factors are required. Proof against actual attacks remains **OPEN**.

**Q: How is the authenticator reset?**  
A: Prior recorded design proposes requiring current authenticator master secret plus wallet private-key proof, then issuing a fresh one-time enrolment secret. **RECORDED REQUIREMENT; loss recovery OPEN.**

**Q: If the initial one-time Authenticator Setup Key is lost before activation?**  
A: **CONFIRMED — Question 2 (2026-10-24):** no new/replacement setup key is issued to save that wallet. If activation has not completed by the original 72-hour deadline, that wallet becomes forever DEAD and cannot be made active again. The protocol observes non-activation and expiry; it cannot detect a missing physical key. Create a new wallet instead.

**Q: What if the Authenticator Master Key is lost AFTER successful activation?**  
A: **Q3 CONFIRMED (2026-10-24):** owner may have preconfigured an optional **TongNet Disaster Recovery Wallet** address in normal wallet settings (not BlackBox). With BOTH the original Wallet Private Key and the optional one-use Disaster Recovery Key, they can run one-way recovery without BlackBox or Authenticator. Intention: move all eligible wallet funds (less actual fee if any) to the preconfigured address, then make the old wallet permanently DEAD. BlackBox access itself is not restored. Recovery destination and key are **immutable after first setup**. **First setup must use Wallet Private Key and TongNet Authenticator together (Q5 Option A)**; Q6 clarifies already Triggered locked transfers; Q7 now confirms pre-trigger 3h expiry returns locked amount to linked recovery wallet after DEAD source.

**Q: Must a disaster recovery address be configured?**  
A: No, this is optional.

**Q: Can a recovery execution choose a fresh destination?**  
A: No: it must send to the **previously registered** recovery wallet, not a new arbitrary payout address.

**Q: What happens to locked funds when Disaster Recovery runs?**  
A: **Q6 CONFIRMED (2026-10-24):** Only currently unlocked balance sweeps immediately to the fixed Disaster Recovery Wallet. Already Triggered transaction funds remain escrowed; receiver retains a 24-hour Claim Key right. If receiver does not claim, sender gets their existing additional 72-hour window. The same one-time sender Claim Key can be submitted through the pre-bound recovery wallet **only after source wallet disaster recovery has actually completed** and with network-verifiable destination binding and control of new wallet. If sender Claim Key is lost in inaccessible BlackBox, disaster recovery does not replace it or entitle payment. Expiry / proposed network reserve transfer still applies. See [DISASTER_RECOVERY.md](DISASTER_RECOVERY.md).

**Q: Can the network assume both wallets have the same human owner?**  
A: No: a cryptographic, authenticator-approved recovery address registration proves an **authorised link**, not natural-person identity. Sender-claim rights must be tied to original transaction and fixed destination; a key alone must not be redirected to any third wallet.

**Q: What happens to still-untriggered locked funds after Run Disaster Recovery?**  
A: **Q7 CONFIRMED — Option A (2026-10-24):** They stay locked until the original 3-hour pre-trigger expiry. Run Disaster Recovery sweeps available funds without waiting and permanently deactivates original sender S. Since S is then DEAD and the still-pending Send cannot be triggered, at its original 3-hour deadline the automatic refund goes directly to previously registered, immutable Disaster Recovery Wallet R. No early cancellation or separate Sender Claim Key is needed in this untriggered refund route. Network must ensure no payout to both wallets.

**Q: Where and when is the one-time Disaster Recovery Key generated?**  
A: **Q8/Q9 confirmed 2026-10-24:** The source sends a disaster recovery request from ordinary Wallet settings. Only when the chosen recovery wallet **ACCEPTS** that request inside **its own TongNet BlackBox** is the unique one-use Disaster Recovery Key generated there, NOT in the source wallet's BlackBox. This same key is later presented alongside the original source Wallet Private Key to run the single-use recovery; the source Authenticator/BlackBox is not needed at that time. The key is permanently unreplaceable and the association immutable once complete.

**Q: What if destination REJECTS or ignores disaster recovery request?**  
A: **Q9 confirmed:** REJECT creates no key or final association, and notifies the source wallet's BlackBox. If destination neither accepts nor rejects, request stays PENDING for **at most 24 hours**, during which there is no key/immutable binding and source is NOT_CONFIGURED. At 24 hours without successful approval, request automatically **EXPIRES** with no key/binding; a late Accept is invalid. Q10 confirmed Option A.

**Q: Does destination-side key generation establish the same person owns both addresses?**  
A: No. A cryptographic link/approval demonstrates authorization according to the system's rules, not natural-person identity. Merely placing a secret inside R's encrypted inbox is not by itself a signature with R's private key or an explicit acceptance.

**Q: When does the recovery address become permanently attached?**  
A: **Only after an explicit ACCEPT from destination BlackBox**. Request initiation alone never attaches it. At ACCEPT the one-time key is created in destination BlackBox and the association becomes irreversible. **Q9 confirmed**.

**Q: How long does an unanswered Disaster Recovery pairing request stay pending?**  
A: **Q10 confirmed — Option A:** 24 hours. If R has not accepted/rejected by the deadline, the request expires automatically. S has NO active disaster recovery before Accept; no key or irreversible link is created by timeout. Accept after expiry must be rejected; exact network race/clock implementation requires tests.

**Q: Can the source cancel a pending recovery setup request?**  
A: **NO — Q11 Option B confirmed (2026-10-24).** While PENDING the source cannot withdraw, redirect or send a replacement request. It must wait for the destination to REJECT or for automatic EXPIRED after 24 hours. Only then may the source try another recovery address (with fresh initial two-factor approval). If target ACCEPTS the live request, immutable registration takes effect and cannot ever be changed.

**Q: What if Recovery Wallet clicks Accept before 24h but network finalizes it after expiry?**  
A: **Q12 CONFIRMED, Option A:** The request **EXPIRES**. Only ACCEPT that becomes **network-final before the original 24-hour cutoff** is valid. Earlier button-press, device signature or intermediary delivery does not save it. No Disaster Recovery Key or permanent link is created for a late-finalized ACCEPT. Network timing/finality engineering and outages remain unresolved.

**Q: What next?**  
A: **Q13:** If the whole TongNet network suffers an outage during someone’s 24h receiver-claim or 72h sender-recovery period, should timers continue as normal and possibly send unclaimed funds to Network Reserve, or pause during a verifiably network-wide outage?

## Payment flow

**Q: What happens on Send?**  
A: Funds are locked and transfer enters PENDING_TRIGGER; no recipient claim key yet. **CONFIRMED.**

**Q: Can sender cancel before triggering?**  
A: **No.** Even if they change their mind, funds stay locked until sender triggers or the 3-hour timer expires. **CONFIRMED.**

**Q: What happens if sender never triggers?**  
A: **Exactly 3 hours after initiation, automatically release locked funds back to sender.** **CONFIRMED.**

**Q: How is a transaction triggered?**  
A: Sender accesses own TongNet BlackBox with wallet authorisation plus rotating authenticator approval, then explicitly presses Trigger. Only then can the recipient receive an address-bound claim credential in its own encrypted BlackBox. **CONFIRMED DESIGN.**

**Q: Is receiver's claim code publicly visible or sent manually?**  
A: No. It is delivered specifically to the receiver's BlackBox, not shown to the sender for onward forwarding. **CONFIRMED.**

**Q: What is the receiver's time limit?**  
A: **24 hours from successful Trigger**, not simply from Send. Only the specified receiver address may claim, with proof of wallet control; at most once. **CONFIRMED.**

**Q: Can sender take money back during the 24-hour receiver window?**  
A: **No.** **CONFIRMED.**

**Q: If receiver never claims?**  
A: Receiver claim credential expires at +24h from Trigger; sender-only recovery runs for the **next 72 hours**, using a one-time sender recovery credential. **CONFIRMED.**

**Q: What happens after those extra 72 hours?**  
A: User's latest proposed rule: permanently reallocate the transfer to TongNet Network Reserve for network costs, with both claim credentials void. **USER-SPECIFIED PROTOCOL INTENT, deployment BLOCKED pending legal/economic/consent review.** This conflicts with an earlier suggestion for automatic sender refund after 72h; the latest user intent takes precedence as a design request.

**Q: Does a claim consume the credential?**  
A: Yes, it is one-use and a final successful claim must disable all rival claim paths. **CONFIRMED; atomic enforcement OPEN.**

**Q: What if receiver address is wrong after Trigger?**  
A: **CONFIRMED — Question 1, Option B (2026-10-24).** Sender cannot cancel, stop, or reverse after successful Trigger, even for a wrong receiver address. If the addressed receiver claims within 24h, the transfer is settled. If the receiver does not claim in that window, sender-only recovery is available for the next 72h. No guaranteed refund if a wrong receiver validly claims. Wallet should clearly display the destination and irreversible-trigger warning before authorisation. This confirmation does not imply any central emergency override.

**Q: Are the two credential-generation times fully specified?**  
A: Sender recovery credential is intended for sender's BlackBox and receiver credential only after Trigger. Whether sender credential is minted immediately on Send or on Trigger remains a low-level implementation decision. **OPEN.**

## Network and security

**Q: Does the BlackBox make theft impossible?**  
A: No. It should prevent a stolen wallet key **alone** from authorising final payment; compromise of multiple factors, coercion, phishing, client compromise and consensus failures remain threats.

**Q: How is double-spend prevented?**  
A: Must use atomic, authenticated state transitions and secure decentralised finality across untrusted nodes. **UNSOLVED.**

**Q: Zero transaction fees?**  
A: Zero or negligible **user-visible** fees is a goal, not proof of zero underlying costs. Funding via independently governed contributions, merchant services or network reserve requires an attack- and legally-sound model. **OPEN.**

**Q: What is TongNet Network Reserve?**  
A: A separate proposed pool for paying network expenses; do not confuse it with any separate coin-backing collateral reserve. **DESIGN DIRECTION.**

**Q: Can personal data be avoided?**  
A: Minimise data collection, not promise literally zero transaction state or anonymous fiat redemption. Regulatory obligations are separate. **GOAL; implementation OPEN.**

**Q: Is the repo/product public and complete?**  
A: This repository currently starts **private**. No consensus implementation, mainnet, audited wallet, token issuance or deployed payments have been verified. **ACTUAL STATUS.**

---

**Maintenance rule:** update this FAQ after each confirmed answer; preserve wording conflicts and versioned design changes in DECISIONS and CHANGELOG rather than silently erasing history.

**Q: What happens if TongNet gets slow? When does a new transaction timer start?**  
A: **Q13 user direction (2026-10-24):** slow/fast network does not alter a timer already started. New transactions/tasks can wait in a queue during congestion. Their timer begins only after network acceptance. **Engineering recommendation:** make acceptance mean authoritative network consensus finality, not a relay's QUEUED acknowledgment. No code or consensus proof exists yet.

**Q: Does putting an existing Claim request in a queue preserve its deadline?**  
A: **NO — Q14 CONFIRMED, Option A (2026-10-24).** A Receiver must have its Claim fully network-final **before** the 24h receiver deadline, and a Sender reclaim must be final **before** its subsequent 72h deadline. A claim signed/queued before cutoff but finalized late is EXPIRED. Neither a queue ticket nor prior submission is a guaranteed settlement. This is distinct from a NEW Send's timer beginning at network acceptance.

**Q: What if network-wide downtime makes all Claims impossible until after expiry?**  
A: **OPEN — NEXT Q15.** Running countdown and claim finality rules are defined, but whether expired unclaimed escrow is automatically assigned to Network Reserve or protected pending a network-restoration review/grace policy is not agreed. A forced forfeiture is a serious launch blocker without informed consent and legal review.

**Q: Is the network-delay time credit only for Claim operations?**  
A: **NO — Q15 broadened by user (2026-10-25).** The TongNet Network Delay Calculator must add one-to-one extra time for **every affected time-bound network operation**: Send/Trigger, receiver Claim, sender reclaim, disaster recovery requests/approvals and similar timed tasks. Clocks don't change speed; their effective deadlines move by verifiable network-attributable delay. Q12 and Q14 still require final network confirmation **before their adjusted deadline**. A queued action is not a finalized action.

**Q: How does this affect the original 3h, 24h, 72h windows?**  
A: Their nominal base duration remains. A proven 20-minute eligible delay grants a 20-minute deadline credit to the affected operation; dependent receiver/sender/refund/reserve stages must shift so two parties never have overlapping exclusive rights. Queue delay on a brand-new transaction BEFORE it receives first network acceptance cannot count twice (timer has not started). Exact consensus proof and attribution are NEXT Q16.

**Q: What happens to funds during a delay dispute?**  
A: The system cannot safely forfeit escrow to Network Reserve before all verified/applicable deadline credits have been included. The proposed automatic transfer of unclaimed funds to Reserve remains blocked for real users pending consent, legal review, consensus-liveness and consumer safeguards.

## 2026-10-25 architecture revision FAQ

**Q: What was confirmed in Q16–Q25?**  
A: Q16 **C** combined independently proven per-task and network-wide delay (no double counting); Q17 **C** anti-fabrication; Q18 **C** consensus evidence or Protected Suspense; Q19 **C** decentralised Anti-Sybil committee; Q20 **C** phased hybrid evolution; Q21 **C** fully automated validator administration; Q22 **B** quarantine/investigate/restore-or-remove; Q23 **B** backup validators; Q24 **C** secure quorum on partitions; Q25 **B** preverified rotation that cannot create contradictory quorums. These are confirmed product choices only, not implemented or formally verified.

**Q: Is TongNet guaranteed 100% decentralised and completely free?**  
A: NO. Physical networks have dependencies and each transaction consumes node resources. Target no indispensable owner/cloud and affordable or sponsored user-visible payments, with a transparent minimal-fee fallback. Phase 1 verified-validator onboarding has real trust assumptions, to be openly disclosed; fully permissionless security must earn independent proof.

**Q: Is this an original novel algorithm not used anywhere else?**  
A: Novelty has not been verified. TongNet may compose distinctive payment/recovery/delay features; use reviewed BFT/crypto rather than invent risky primitives, check licences, and get prior-art review before saying 'world-first'.

**Q: What replaces all earlier one-by-one questions?**  
A: [Master architecture research](TONGNET_FUTURE_ARCHITECTURE.md) and [all 95 question-and-answer recommendations](MASTER_QA_RECOMMENDATIONS.md), with explicit user-confirmed vs engineer-proposed labels and real-money hard blockers.

## 2026-10-25 — User-confirmed payment key origin correction

**Q: Where are the TWO ordinary Claim Keys generated?**
A: BOTH in the **sender's TongNet BlackBox**. Receiver's claim code K_R is generated at transaction setup and Sender gives it to intended receiver. Its 24h use window starts only after final Trigger; K_R + exact addressed Receiver wallet authority both required. There is NO automatic secret delivery to Receiver BlackBox. If unclaimed, K_R expires and a NEW Sender Claim Key K_S is generated in Sender BlackBox after expiry, usable with Sender authority in the following 72h, then expires too (subject to proof-backed network-delay extensions).

**Q: If Sender types WRONG receiver address B and gives code to intended A?**
A: A has code but not B wallet's signing authority; B has signing authority but not the code, so neither normally can claim. After the adjusted 24h receiver window ends, Sender becomes eligible to manually reclaim during the next 72h with newly generated K_S. This is NOT an automatic refund at 24h. If B obtains correct code or controls A somehow, a valid B claim is possible; no automatic guaranteed recovery.

**Q: Are sender-generated payment keys the Disaster Recovery Key?**
A: NO. K_R and K_S are transaction-specific normal payment claim credentials. Unrelated permanent Disaster Recovery Key is generated inside the selected RECOVERY WALLET's BlackBox after its accepted pairing.

**Open:** late K_S generation on offline/lost/DEAD Sender BlackBox versus existing Q6 post-disaster Sender Claim Key support needs user decision and protocol proof. See [DECISIONS.md](DECISIONS.md).

## 2026-10-25 — Mandatory Sender BlackBox manual final ACCEPT

**Q: If Receiver has correct Claim Code and their wallet key, can they take funds?** NO. After Receiver submits a signed Claim Request, SENDER's separate BlackBox must display that exact request. Sender manually ACCEPTS only if the wallet address, amount, transaction and recipient match. A valid final settlement requires Sender ACCEPT too; simply having code and wallet doesn't transfer coins.

**Q: What if Sender ignores Claim Request?** A manual REJECT button is not required. No ACCEPT means no Receiver payout. Once Receiver's adjusted 24h right expires, its claim code is invalid, and Sender-exclusive following 72h reclaim window applies, requiring Sender's new Claim Key K_S and network finality within deadline. This is NOT an automatic refund at 24h.

**Q: Does this remove old 3h Trigger?** No, not without another decision. The existing 3h separate Trigger and its no-trigger refund remain. Final ACCEPT is an additional approval after the Receiver Claim Request. See [PROTOCOL.md](PROTOCOL.md).

**Q: Is an incorrect destination guaranteed safe?** No. Sender can withhold ACCEPT when actual bound wallet differs from intended. But Sender still may approve a scammer address or malware may compromise the approval factor; once BFT-final, the payment is irreversible.
