# TongNet Protocol Specification — Draft 0.1

**NOT IMPLEMENTED OR AUDITED.** Requirements below describe desired behaviour, not cryptographic proof.

## Actors and boundaries

- **Sender Wallet:** initiates a transfer; holds wallet-signing authority.
- **Sender TongNet BlackBox:** separate encrypted, second-factor-gated operation space, including Trigger and later refund credential.
- **TongNet Authenticator:** separately provisioned secret, 60-second access code; transaction approval must use stronger challenge-bound cryptographic proof than a copyable OTP alone.
- **Receiver Wallet and BlackBox:** receiver-address-bound one-time claim.
- **Decentralised verification layer (TBD):** enforces canonical final state across participants; no single trusted actor permitted by project goals.
- **TongNet Network Reserve:** proposed operational funding pool; separate from any monetary backing or redemption reserve.

## Wallet activation lifecycle (confirmed requirement)

- At wallet creation, create an address, wallet credential, separately protected TongNet BlackBox and one-time TongNet Authenticator enrolment credential.
- Until activation, wallet must not be permitted to SEND, RECEIVE or CLAIM; this must be enforced by the network, not merely the UI.
- Successful independent authenticator enrolment before 72h moves the wallet to ACTIVE and consumes the initial setup credential.
- **If no successful enrolment by creation + 72h, transition irrevocably to DEAD.** Any later attempt to activate/revive the same wallet MUST be rejected; no lost initial setup-code replacement, privileged admin reset, or expiry extension is permitted (Q2 confirmed 2026-10-24).
- An unauthenticated network cannot detect a person's lost physical key: only completed enrolment, deadline and state are verifiable.
- Exact distributed deadline semantics, activation replay protection and network partition safety remain engineering questions.

## Optional TongNet Disaster Recovery Wallet — Q3

**New key requirement (2026-10-24):** The product has three separately designated key categories: (1) wallet private key, (2) authenticator master key, (3) optional disaster recovery key generated/provisioned if recovery is enabled. Their secret materials and permissions must be distinct. The third key is generated **inside the destination wallet's own encrypted BlackBox ONLY AFTER the destination ACCEPTS its incoming recovery pairing request** and is required **together with** original Wallet Private Key for Run Disaster Recovery. It is usable once only. Recovery destination wallet address is separate from recovery key.


- In normal SOURCE wallet settings, source Wallet Private Key PLUS source TongNet Authenticator authorize **SUBMIT_REQUEST(S,R)**. This places a request in DESTINATION R's BlackBox, **PENDING_ACCEPTANCE**; no permanent registration or recovery key exists yet.
- R's own BlackBox can **ACCEPT**: only then issue/generate the unique one-use Disaster Recovery Key **inside R BlackBox** and finalize the immutable S→R link. **REJECT**: do not generate key/link; send a rejection notice to S's BlackBox. **No response**: PENDING and NOT_CONFIGURED for S until original request + **24 hours**; then automatically EXPIRED, still NOT_CONFIGURED, with no key/binding. Accept after expiry invalid (Q10 Option A).
- After successful ACCEPT, destination address and key cannot be changed, reissued or reset. Source normal two-factor request authorization was confirmed Q5; destination BlackBox approval is Q9.
- When BlackBox/Authenticator is inaccessible but original Wallet Private Key and the independent Disaster Recovery Key are held, **Run Disaster Recovery** requires BOTH proofs and does NOT require BlackBox access or a rotating Authenticator code. It consumes the disaster key once.
- Intended outcome: atomic full sweep of **eligible** wallet balance, minus actual applicable fee, to **previously registered** recovery address; then original wallet enters a permanently DEAD state. Recovery never permits arbitrary destination changes at execution.
- **Q6 confirmed for Triggered escrow:** Run Disaster Recovery immediately sweeps *available* funds, not outstanding locked value. Triggered/receiver-claimable escrow survives the source-wallet DEAD transition, including receiver's full 24h priority. If receiver did not claim, the same original transaction-bound Sender Claim Key can be submitted during the subsequent 72h via the pre-bound recovery wallet, **only if the source's disaster recovery had already finalised**. This is a delegated destination for the same one-use entitlement, not minting a replacement key or a double claim. A missing Claim Key still prevents sender claim. **Q7 ANSWERED (Option A):** if S becomes permanently DEAD after disaster recovery while Send is untriggered, retain the original 3h lock and automatically refund at deadline to the immutable, prebound disaster destination R. Trigger after DEAD is invalid.
- **Q5 decided:** attacker holding only Wallet Private Key cannot register recovery destination; FIRST setup requires Wallet Private Key + TongNet Authenticator approval. Binding the approval to the destination shown to user, preventing phishing and replay, and preventing a shared-compromise attack still require implementation. Destination cannot subsequently be changed. See [DISASTER_RECOVERY.md](DISASTER_RECOVERY.md).

## Contracted time windows

Let `t0` = network-accepted transfer initiation, `tt` = network-accepted Trigger. Network clock and boundary rules **TBD**.

```
At t0: lock sender funds; transaction=PENDING_TRIGGER
t0 ... t0+3h: sender may authenticate and Trigger. No manual cancel/refund.
If no successful Trigger before deadline: PENDING_TRIGGER -> AUTO_REFUNDED
At tt: sender Trigger becomes IRREVOCABLE / NON-CANCELLABLE, including mistyped destination; create/deliver receiver claim entitlement to target BlackBox
tt ... tt+24h: only bound receiver may redeem -> FINAL_RECEIVER_CLAIMED
If receiver does not claim by deadline: receiver entitlement expires; RECOVERY_ONLY
tt+24h ... tt+96h: only bound sender with one-time recovery credential may redeem -> FINAL_SENDER_RECOVERED
If neither redeem by tt+96h: proposed -> NETWORK_RESERVE_FINAL (blocked from real-world release pending legal/consent review)
```

**Notes:**
- The 3-hour pre-trigger period and the 24+72-hour post-trigger period are **different stages**.
- If Trigger occurs near t0+3h, receiver's 24h window runs from `tt` (not `t0`).
- **Confirmed 2026-10-24 (Question 1, Option B):** NO sender cancellation or emergency stop after Trigger, even when recipient wallet address is incorrect. A wrongly addressed but otherwise valid receiver can claim; only if unclaimed after 24h may sender reclaim in the subsequent 72h. Display recipient address, amount and irreversible-trigger warning before approving.
- Exactly-at-boundary ordering, clock source and network partition behaviour require formal design.
- Credential issuance/delivery mechanisms are not yet defined; no email/SMS/manual code-sharing dependency is intended.

## Required logical transaction fields (proposed, not a standard)

```text
transaction_id
sender_address
receiver_address
asset_id_and_amount
locked_value_reference
created_at_network_time
triggered_at_network_time? 
receiver_claim_deadline?
sender_recovery_deadline?
state
spent_nullifier_or_atomic_consumption_record
sender_credential_commitment?
receiver_credential_commitment?
protocol_version
```

**Do not write plaintext secrets, private keys, authentication master secrets, or claim codes to public state.**

## Safety invariants to formally prove

1. **Conservation:** locked value is resolved exactly once, without duplication.
2. **Mutual exclusion:** receiver settlement, sender refund and reserve allocation cannot each succeed for the same value.
3. **Recipient binding:** claim credential alone is insufficient; wallet authority for the exact addressed receiver is required.
4. **Sender binding:** recovery requires authenticated authorisation from the exact original sender.
5. **Trigger authorisation:** possession of wallet private key alone cannot Trigger.
6. **Deadline enforcement:** all honest verifiers agree on acceptance order and settled state despite latency/partitions.
7. **Replay protection:** no claim/trigger proof can be reused in a different transaction, network or epoch.
8. **Resource limits:** attackers cannot cheaply exhaust validator resources with unlimited fake wallets/claims.
9. **No hidden central override:** no provider can unilaterally bypass agreed transaction states.

## Illustrative example (no Trigger)

- 10:00 Send locks 1,000 TONG.
- Before 13:00 sender may Trigger, but cannot Cancel.
- At 13:00, if no Trigger accepted, auto-refund entire 1,000 TONG to sender.
- Receiver receives no claim credential.

## Illustrative example (Trigger at 11:00)

- 10:00 Send locks 1,000 TONG.
- 11:00 sender second-factor-authorised Trigger.
- Until 11:00 next day, only bound receiver can claim.
- Next 72h (until 11:00 four days after Trigger), only sender can reclaim if receiver did not claim.
- Beyond that, the *creator-proposed* network reserve allocation is final, **subject to unresolved laws/consent**.

## Unresolved difficult cases

Wrong target address is non-cancellable after Trigger (confirmed); account theft during pending transfer; lost root secret; network downtime; blackbox message delivery and acknowledgement; simultaneous valid claims across partitions; payment amount denomination; upgrade governance; fees and cost coverage; validator incentives and Sybil resistance.

No feature is safe to deploy solely because this state chart appears internally consistent.

## Lost one-time disaster key rule (confirmed 2026-10-24)

A lost Disaster Recovery Key cannot be reissued, regenerated, recovered or swapped, and its destination remains immutable. If the owner still has Wallet Private Key **and** Authenticator Master Key, normal sends to a different wallet remain possible under existing Send → 3h Trigger → 24h receiver claim → subsequent 72h sender recovery rules. Do not assume that normal transfers instantly move all locked funds or bypass triggered transactions.

## Q5 — Initial recovery-destination setup (confirmed)

First and only registration of the optional permanently immutable disaster destination MUST validate both source Wallet Private Key and TongNet Authenticator approval. Then send a pending request to R's BlackBox; **only after R explicitly ACCEPTS** issue the separate one-use Disaster Recovery Key in R's BlackBox and finalize the irreversible S→R link. Later emergency execution requires Wallet Private Key plus that third key, but no Authenticator. Need cryptographic signature over full registration payload (wallet ID, target recovery address, action, nonce and expiry), not just reusable OTP. Q6 next: treatment of locked/triggered transfers during recovery.

## Q6 — Outstanding Triggered transfer after source disaster recovery (confirmed)

Model the **escrow/locked transaction** as independent of wallet ACTIVE/DEAD status. The original transfer's lock remains inviolate while the receiver's 24-hour priority claim remains possible; no disaster recovery operation may cancel or steal it.

State example: Source S has 700 spendable + 300 Triggered escrow. Immutable linked recovery destination R was approved by S's Wallet Private Key and TongNet Authenticator. With S's private key and unique Disaster Recovery Key, the terminal atomic transition sweeps 700 (minus fee) S→R, consumes disaster key and marks S DEAD; 300 stays in original escrow. Receiver may claim the 300 within 24h after Trigger. If unclaimed, sender Claim Key (the SAME pre-existing, transaction-bound key) may be submitted during subsequent 72h for a claim **to R**, conditioned on FINAL proof of S→R pre-registered binding and completed disaster recovery. Network requires R wallet private-key control, verifies sender entitlement, exact transaction/amount, credential not spent, timeframe and original claim cryptography. Do not infer that two addresses correspond to the same human: only cryptographic authorization is knowable.

If the user lost access to the sender Claim Key stored in old BlackBox, neither S's private key alone nor Disaster Recovery Key substitutes for the missing sender claim proof; no payout. Unless receiver claimed earlier, expiry continues to the user's proposed reserve allocation after 24+72h (subject to legal review).

**Q7 CONFIRMED:** When S becomes DEAD while Send is still PENDING_TRIGGER, the lock is untouched until original t0+3h. It cannot be triggered by DEAD S. At original timeout the automatically refunded amount credits immutable prebound R (the Disaster Recovery Wallet). No cancellation or accelerated settlement. Deterministically resolve any Trigger/DEAD/timeout finality races.

## Q8 — Disaster credential issuance in destination wallet BlackBox

User instruction (2026-10-24): When S **REQUESTS** a permanently immutable recovery destination R (requires S Wallet Private Key and S TongNet Authenticator), deliver request into R's encrypted BlackBox. **Only after R explicitly ACCEPTS** generate the unique one-time disaster recovery credential **inside R's encrypted BlackBox** and finalize immutable S→R registration. The key belongs to the source→destination rescue association but its protected place of creation/retrieval is R's own BlackBox, not S's BlackBox. To run rescue at a later time, require S's Wallet Private Key + the SAME recovery credential; no current source Authenticator approval. Consume it once in the atomic S→R sweep and permanent S DEAD transition.

Nodes should verify a securely bound credential commitment for exactly (network, source S, immutable destination R, action, nonce), without exposing the plaintext recovery secret. Key creation in R's BlackBox requires independent authenticated/encrypted messaging and consistent distributed registration. Q9 confirms R must explicitly ACCEPT within its BlackBox; the exact cryptographic signing/enforcement mechanism remains to be designed. This is evidence of network-verified authorization, not shared human identity. Security of registration/expiry, recipient mailbox unavailability, and avoiding attacker's unsolicited associations remain open.

## Q9 — Two-party recovery request and acceptance state machine (confirmed)

```text
S_NORMAL_SETTINGS (S Wallet Private Key + S Authenticator)
  -- submit recovery destination request(S,R,requestId) --> PENDING_ACCEPTANCE
  PENDING_ACCEPTANCE: recoveryConfigured(S) = false; no recovery key; no final S-R binding
R_BLACKBOX:
  ACCEPT(requestId) -> issue one-use Disaster Recovery Key INSIDE R BlackBox,
     then finalize immutable pair S-R and mark recoveryConfigured(S) = true
  REJECT(requestId) -> no recovery key/binding, notify S BlackBox, state REJECTED
  no response until accepted time + 24h -> request EXPIRED and recoveryConfigured(S) = false; no key or binding
  late ACCEPT on EXPIRED -> REJECT request; do not issue key/binding
```

The system must not expose a valid disaster key or mark a wallet protected **before** a properly verified R BlackBox acceptance. Requirement for end-to-end correctness: verify S/R/request ID and acceptance authenticity, prevent duplicate issuance under concurrent Accept/Reject, assure durable delivery/ability to retrieve the resulting key, ensure permanent binding and key commitment are consistent. Q10 sets **24 hours** for unanswered requests. **Q11 forbids source cancellation/withdrawal/replacement while PENDING**; a fresh request can be initiated only after target REJECT or 24h EXPIRED, never after ACCEPT. Edge-time consensus ordering is NEXT Q12.

## Q10 — Recovery pairing PENDING TTL (confirmed user choice)

Unanswered R BlackBox recovery association requests have a **24-hour time-to-live** from canonical network-accepted request creation (exact clock/finality procedure TBD). During that time status is PENDING_ACCEPTANCE and S recoveryConfigured=false. If no valid destination acceptance has finalized before deadline, transition once to EXPIRED; no recovery key or permanent association exists and any later ACCEPT must be rejected. REJECT remains a terminal rejection with S BlackBox notice under Q9. A request cannot be revived by replay or duplicate submission.

**Critical network design work:** ordering of simultaneous ACCEPT/REJECT/EXPIRED operations, authentic timestamp, delayed delivery, request uniqueness and immutable status in consensus. Exact boundary finality rules not yet formalised. **Q11 confirmed Option B:** S may neither withdraw nor replace a PENDING recovery request. Wait for R's REJECT or 24h EXPIRED before a new attempt; R ACCEPT permanently binds and prevents later setup. **Next Q12:** which network event qualifies an ACCEPT sent near the 24h expiry?

## Q11 — Pending request non-cancellation (confirmed)

Request state transitions are PENDING_ACCEPTANCE → ACCEPTED, REJECTED or EXPIRED, with **no SOURCE_CANCELLED state and no PENDING_REPLACED transition**. Reject or expiry releases the source's outstanding-request slot and permits a new properly authenticated association attempt. Accept atomically creates permanent binding and the one-time key in destination BlackBox, prohibiting all later attempts to replace the destination. While request PENDING, mark source NOT_CONFIGURED. The 24h expiry remains unaltered by user polling or reopening BlackBox.

**Q12 CONFIRMED, Option A:** a destination ACCEPT is valid ONLY when successfully network-finalized strictly before original request's 24-hour deadline. Signing, clicking or intermediate network receipt before deadline is not sufficient; after-deadline finality must result in EXPIRED with no key/binding. Canonical clock and finality ordering remain engineering work. **NEXT Q13:** claim-window behavior during serious network outages.

## Q12 — Strict network-finality cutoff on disaster request Accept

User confirmed Option A. For each pending pairing request with canonical creation-finality timestamp t_req, define deadline D=t_req+24 hours. Valid ACCEPT requires proof that the acceptance entered **final network consensus state with finality_time < D** (strictly earlier); only then may the target's BlackBox securely generate one-use Disaster Recovery Key and S→R permanent pair be committed. A device click, cryptographic signature, or relay receipt time alone must NOT qualify. If finality at or after D, request is EXPIRED and no key or irreversible link may be issued. Treat expiry as idempotent and prohibit replay/late approval resurrection. Actual blockchain time and deterministic finality function are NOT specified or deployed. Do not silently apply this pairing rule to payments until their own timing rules are explicitly decided (next Q13).

## Q13 — Network queue and timer semantics (user intent + recommended implementation)

**User-defined goals 2026-10-24:** network load, whether fast or slow, must NOT change running timers; under congestion tasks and transaction requests may be queued and load-balanced; a NEW transaction's timer only starts once the **network accepts it**, not when user taps Send.

**Engineering proposal to be accepted/tested, not implemented:**

```text
CREATED_LOCAL -> SIGNED -> QUEUED_NONFINAL -> CONSENSUS_ACCEPTED_FINAL
                                              -> timer_start = consensus_final_time
QUEUED_NONFINAL -> REJECTED/DROPPED/RETRYABLE (no payment accepted; no new timer)
```

- Queue entries are requests, **not final transfers**. Do not debit final spendable balance/credit receiver, establish a permanent credential, or display CONFIRMED based on queue admission. Upon final network acceptance, verify signatures/nonces, current balance/state, perform atomic state transition, and establish the proper timer(s).
- **New Send:** 3h Trigger timeout starts at canonical final network acceptance of Send. **Triggered payment:** receiver 24h starts at final Trigger; following sender 72h derives from the same final Trigger time. **Recovery-pairing request:** its 24h pending deadline starts at final acceptance of the pairing REQUEST; R's later ACCEPT must finalize before deadline as Q12 prescribes.
- **Existing timers are unaffected by queue length.** A claim submitted during an active 24h/72h window is NOT automatically preserved merely because it joined a queue. **Q14 CONFIRMED (Option A):** financial receiver/sender Claims MUST reach network finality strictly before their pre-existing 24h/72h claim deadline. Queue admission or prior signature does not confer rights after expiry. Distinguish from NEW Send timer beginning on initial network acceptance.
- Proposed implementation: bounded and persistent queues, request IDs/nonces/idempotency, per-account fairness and anti-spam rate limiting, separate processing lanes for claims/expiry/recovery, safe backpressure, signed status receipts, retriable delivery and multi-node redundant submission. Validate again at consensus finality to prevent stale/double spending; queue order alone cannot guarantee safety.
- Severe outage can make consensus acceptance impossible. A queue during downtime cannot offer guaranteed eventual payment if funds/claim rights expire meanwhile. Exact full-outage exception vs strict continuing deadlines and proposed Network Reserve forfeiture remain unresolved and subject to legal/consumer safety review.

**Q14 ANSWERED (Option A):** a Claim queued/submitted before its 24h/72h expiry but finalized afterward is EXPIRED. Queue receipts do not preserve payment claim priority; network finality must occur strictly before the claim deadline. Q15 next: long outage and reserve disposition.

## Q14 — Claim finality versus deadline (user-confirmed Option A)

For a Trigger that reached network finality at tT, the receiver's one-use Claim is eligible ONLY when consensus finality_time < tT+24 hours; an at-or-after-boundary receiver Claim is EXPIRED. The sender's distinct one-use Claim is eligible ONLY in the *subsequent* 72-hour window, and must be final BEFORE tT+96 hours. Implement the existing sender-window start and receiver-end boundary deterministically; no overlap or gap granting duplicate claims. A Claim signed, clicked, relayed or admitted to queue before the deadline but finalized afterward does not count. On finality, independently re-check state, correct credential, destination binding, window, and uniqueness; reject stale queued operations. No later state may double-settle the same escrow.

This is a product requirement and not an implemented consensus property. **Q15 OPEN:** what if the entire network is halted across the payment's final deadlines, making legitimate Claim confirmation impossible? Distinguish fixed countdown from the later handling of unclaimed escrow and the proposed reserve forfeiture. No production confiscation or reserve credit before safety/legal review.

## Q15 — Universal Network Delay Calculator and 1:1 deadline extension

**Confirmed by user, 2026-10-25:** Every network-time-limited task which incurs attributable TongNet network slowdown/outage/processing delay must get EXACTLY the same duration of additional eligible time. Scope is **not limited to payment Claims**: Send/Trigger 3h, Receiver Claim 24h, following Sender reclaim 72h, Disaster Recovery setup request/Accept 24h, and all other timed operations are included. Run clocks normally; expand the *effective cutoff* by verified network delay instead of changing clock speed. This revises the previous 'no deadline extension' interpretation of Q13/Q14 and the pairing deadline in Q12 only as to the **applicable cutoff**, not the strict-finality requirement.

Conceptual invariant (NOT an implemented calculator):
`effective_deadline(operation) = canonical_base_deadline + exactly_once_credit_of_proven_applicable_network_delay(operation)`.
A final action is valid only if its **CONSENSUS FINALITY** is strictly before `effective_deadline`, preserving Q12 and Q14. Pending/queued entry is not a finalized operation. Network delay compensation must be proved independently of client clock and arbitrary user inaction.

**Ordered entitlements:** If 3h Trigger opportunity extends, the no-Trigger refund cannot settle earlier than final adjusted Trigger expiry. If receiver Claim cutoff extends, sender reclaim begins strictly after receiver priority finishes and retains its own following 72h opportunity plus qualifying delay; the proposed Reserve deadline follows both corrected windows. Pairing expiry and BlackBox Accept use the adjusted 24h cutoff, still requiring finality first. Model future deadline updates deterministically so validators cannot settle a refund/reserve while extension evidence is pending.

**No double counting before start:** An original new Send or registration REQUEST admitted to queue has no running deadline until final network acceptance under Q13. Slow queue admission BEFORE timer start should not also be credited to that newly started timer as another extension of the same waiting period; exactly which intervals count for multiple concurrent windows is still OPEN Q16. This protects against inflation of time allowances.

**OPEN Q16:** How the Network Delay Calculator measures credible slowdowns for each affected operation vs global congestion, how multiple overlapping outages are counted exactly once, how validators agree on a canonical record without a central clock, and how to stop censorship or artificial slowdown to manufacture time. This is a specification, not working or tested code.

## 2026-10-25 design review — evidence-backed BFT and universal delay timing

The long-term high-performance proposal is an auditable deterministic-finality BFT state machine (not a fabricated novel algorithm); validator admission uses hybrid permissioned-to-open verified eligibility with optional security bonds, no pure PoW mining and no assumption of one-key-one-independent-person. Consensus requires >2/3 of eligible power under an explicit <1/3 Byzantine fault bound, safe committee reconfiguration, quarantine and preauthorised backup activation; in a 60/40 partition there is no quorum if equal weights. New transactions never finalise without genuine quorum. Parallel transaction dissemination/execution and a DAG-like fast path are RESEARCH options, not production claims.

**Q16 confirmed C:** universal Q15 delay extension derives from *both* operation-specific cryptographically witnessed network processing evidence and network-wide stall proof. Count overlapping delayed intervals once, NOT individual wait + global congestion arithmetic sum. Q17 independent proof filtering, Q18 evidence consensus or protected suspense; validator Q19 C, Q20 C, Q21 C, Q22 B, Q23 B, Q24 C, Q25 B. Finality still strictly BEFORE the objectively delay-adjusted deadline. No mathematical proof of objectively attributed seconds under arbitrary partitions currently exists. Protected funds exit/resume rule and finite-time liveness are unsolved.

**Critical recommendation requiring owner reapproval and legal review:** do not confiscate escrow into Network Reserve simply because nominal 24+72h elapsed; an unbounded or forged time-extension procedure equally must not freeze owner rights forever. Preserve legacy user-confirmed proposals as non-deployable where unresolved. See [TONGNET_FUTURE_ARCHITECTURE.md](TONGNET_FUTURE_ARCHITECTURE.md) and [MASTER_QA_RECOMMENDATIONS.md](MASTER_QA_RECOMMENDATIONS.md).

## 2026-10-25 — CONFIRMED product correction: manual two-party P2P, NOT Instant Pay

**User instruction (clear and later than the instant-pay suggestion):** "Instant wale bahut system ne asi ehnu p2p secure system bna the aa not instant but ek fast manual treeka jithe receiver te sender dona nu kujh krna pve." TongNet is intentionally a **fast, manual, two-party-authorised secure P2P payment protocol**, not an instant-payment default/competing checkout coin. Previous assistant proposal to introduce/enable `Instant Pay` or make it the default is **SUPERSEDED AND NOT AUTHORISED**; do not implement it under current scope.

**Keep user-confirmed Protected P2P sequence:** sender initiates Send and network-final escrow lock; sender personally approves Trigger using independent BlackBox/authentication; addressed receiver personally Claims using its own BlackBox one-use Claim Key. Both parties act before final recipient settlement. No waiting requirement: if both are available they may complete the independent authorisations right away, subject to actual consensus latency. Original **maximum 3h before Trigger, receiver up to 24h to Claim, then sender-only next 72h** remain, with eligible Q15–Q18 one-for-one verified network delay extensions. Before Trigger auto-refund on adjusted 3h no-trigger expiry; after Trigger no sender cancellation, even wrong address; Claim strict finality before adjusted receiver deadline. Never promise seconds to finality without measurements.

**Wrong-address protection to investigate, NOT yet chosen by user:** propose a receiver-created, independently signed **one-use Receive Request (public payment invitation, not a private wallet key and NOT the Claim Key)** bound to destination wallet public key, unique request ID, optional amount and expiry. Sender must verify cryptographic binding, show full recipient fingerprint/details and manually approve exact operation; Trigger still separately signed; only receiver's BlackBox gets the separate confidential Claim Key on Trigger. A malicious party can still sign a legitimate request under the wrong identity and socially engineer approval; signatures prove key control, not real-world recipient identity. Whether a signed Receive Request is mandatory for all Send operations or optional (with warnings on manually-entered addresses) is NOT YET ratified.

**Adoption focus revised:** secure interpersonal escrow-like peer-to-peer exchanges, explicit bilateral authorisation and robust wrong-recipient defenses rather than frictionless cashier checkout or banking-rail competition. Banking/merchant modules are future research, not a change to product's chosen security-first operation. Existing 20-question market critique is historically valuable, but its recommendation for `Instant Pay` is explicitly rejected for present scope. `docs/TONGNET_PRODUCT_CRITIQUE_AND_ADOPTION_PLAN.md` must be read together with this newer decision.
