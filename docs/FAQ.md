# TongNet — Living FAQ (planning)

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

**Q: What next?**  
A: **Q11:** During those 24 hours, may S cancel an unanswered PENDING request and send a different one before R accepts, or must S wait for R Reject or automatic expiry? Once accepted, an association and its one-use key can never be changed.

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
