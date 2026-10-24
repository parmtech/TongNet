# TongNet Disaster Recovery Wallet — Current Design (2026-10-24)

**Design only:** not implemented, verified, audited or ready for real-money use.

## Product and three independent keys

The user can optionally REQUEST a one-time disaster recovery destination address from **normal SOURCE Wallet Settings**, NOT from source BlackBox. Source Wallet Private Key + source TongNet Authenticator authorise the request. This request goes to the **DESTINATION Recovery Wallet's own TongNet BlackBox**. Only if destination independently **ACCEPTS** does the unique one-time **Disaster Recovery Key get generated and delivered INSIDE that destination BlackBox** and the source→destination link become permanently immutable. A PENDING or REJECTED request is **NOT configured recovery**. The key is distinct from that destination's private key and Authenticator Master Key.

The project now has three secret-key categories:
1. **Wallet Private Key** — ordinary wallet access and initiating payment.
2. **TongNet Authenticator Master Key** — independent TongNet BlackBox authorization factor (60-second changing access codes, not a rotating master key).
3. **Disaster Recovery Key** — exists only for wallets whose disaster recovery option was configured; a **one-use secret GENERATED IN THE DESTINATION WALLET'S BLACKBOX** at initial setup, required later to authorize emergency sweep from source. It is NOT the backup wallet's address, wallet private key, or Authenticator Master Key.

## Permanent configuration rules — confirmed by user

- Register the optional disaster destination **once and only after destination ACCEPT**. The pending request is not yet permanent. **After acceptance it cannot ever be changed.**
- **Only after destination acceptance** the corresponding Disaster Recovery Key is generated in destination BlackBox; it cannot be changed, replaced, regenerated, or reset once issued.
- If the Disaster Recovery Key is **lost**, this disaster recovery route is permanently unavailable for that wallet. Possessing Wallet Private Key alone does **not** bypass the missing recovery secret.
- If Wallet Private Key **and** Authenticator Master Key remain available, the user may still normally send the wallet's funds to another active wallet using the regular BlackBox-triggered transaction process. **That does not change the old immutable disaster destination or its recovery key.**
- Provide very clear warnings and require accurate, explicit confirmation of the destination and key backup at setup; no administrative override is allowed under these requirements.
- **Q5 CONFIRMED — Option A (2026-10-24):** INITIAL irrevocable recovery address registration requires both valid **Wallet Private Key authorization AND TongNet Authenticator approval**. A stolen wallet private key alone cannot set the destination. No further change is allowed once the address and key are committed.

## One-time emergency execution — confirmed

**Precondition:** source has a FINAL, accepted and CONFIGURED disaster destination (not PENDING or REJECTED) and its immutable one-use Disaster Recovery Key from the destination BlackBox. A pending request affords **NO disaster rescue route**.

1. Owner has access to source **Wallet Private Key** but lost the SOURCE Authenticator Master Key / SOURCE BlackBox access. The separate destination wallet's BlackBox originally holds the recovery key, which the user must have obtained securely.
2. Open source Wallet using Wallet Private Key.
3. Select **Run Disaster Recovery** and enter the **one-time Disaster Recovery Key** originally generated in the DESTINATION Recovery Wallet's own BlackBox.
4. **Both** source Wallet Private Key authorization **AND** the independent Disaster Recovery Key must be verified. **No TongNet BlackBox or Authenticator code is required.**
5. Network settles all **eligible** funds, minus any actual transaction fee, to **only the permanently registered destination** and atomically consumes the one-time key.
6. In the same atomic irreversible state transition, the original source Wallet becomes **DEAD** forever; it cannot be reactivated.
7. Never accept a different address at Run Disaster Recovery time. Never allow reuse of a successfully consumed recovery secret.

## Q6 — Explicit linked sender-claim entitlement after disaster (confirmed 2026-10-24)

- Example: 1,000 TONG original wallet balance; 700 unlocked, 300 already Triggered and locked. Running disaster recovery moves 700 (less any applicable fee) to the fixed recovery wallet immediately. Original wallet becomes DEAD; 300 remains in transaction escrow, never duplicated.
- 24 hours after original Trigger: only receiver has the right to claim those 300. If receiver claims, final payment is theirs and recovery wallet is not entitled to the same value.
- On receiver nonclaim, for the following 72 hours **the same already-issued sender Claim Key** can be submitted through the **previously immutable-linked Disaster Recovery Wallet**, *only if* the original wallet has actually completed Run Disaster Recovery.
- Recovery-wallet claimant must demonstrate control of its own private key, provide original transaction-bound unspent sender Claim Key, and network must verify an authentic **pre-registered binding** from original wallet to destination. This is **not evidence that both addresses are held by the same natural person**; it is proof of prior cryptographic authorization to link them.
- If the sender cannot access/present their original sender Claim Key, they cannot rescue that escrow merely with the disaster secret; the 72-hour sender-claim opportunity expires. The user's proposed reserve allocation after 96 hours remains a separate unresolved legal/economic blocker.
- Claim right delegation is scoped to **these specific outstanding original-wallet transactions only**, not a transferable master ability to claim arbitrary wallets' payments. Claim always consumes entitlement once, including in racing/partitioned network conditions.
- **Q7 RESOLVED:** A not-yet-triggered original transfer remains locked until its original three-hour deadline; after completed Disaster Recovery kills its source wallet, the no-trigger automatic refund is credited directly to the cryptographically pre-bound recovery wallet at deadline. No early return and no manual cancel.

## Not yet decided (engineering safety problems)

- **Q6 CONFIRMED, Triggered transfers:** immediately sweep ONLY currently unlocked/spendable funds. Keep the locked amount inside its existing transaction escrow and preserve receiver's entire 24-hour claim entitlement. If unclaimed, the already issued sender's one-use Claim Key may be used **from the original wallet's previously linked recovery wallet** during the following 72 hours, even after the original wallet has become DEAD. If the sender has lost that Claim Key / BlackBox access and cannot present it, recovery alone does NOT bypass it; the existing expiry and proposed network-reserve rule still apply. **Q7 confirmed:** for a still-untriggered 3h PENDING_TRIGGER transfer, hold the lock until its existing expiry and pay the automatic refund to pre-bound rescue wallet after source has become DEAD.
- **First-setup authentication confirmed:** BOTH Wallet Private Key authorization and TongNet Authenticator approval. Exact phishing-resistant transaction-bound proof, device compromise resistance and atomic enrollment still require formal protocol design.
- Recovery destination activation status, cryptographic binding and proof of control; wrong address irreversible.
- Can a wallet with no setup still be safe? Yes, standard wallet remains active; disaster feature absent.
- Key format, secure one-time commitment, replay resistance, consensus deadlines, network partitions, fees, expiry with insufficient spendable balance, and fault-tolerant atomic finality.
- Alternative normal transfers after loss of disaster key (if both other keys survive) still use the already confirmed 3-hour trigger, 24-hour receiver claim, and 72-hour sender recovery. Merely initiating a standard send does not instantly credit a new wallet.

## Q9 — Two-sided request/accept handshake (confirmed 2026-10-24)

User-defined phases:

```text
SOURCE S: propose R in normal settings + authorise S private key & S Authenticator
  -> REQUEST_PENDING; recovery_enabled=false; no key issued
DESTINATION R BlackBox: show request and Accept / Reject
  -> Reject: send notification to S BlackBox; recovery_enabled=false; no key/link
  -> No action before 24h: remains pending; recovery_enabled=false; no key/link
  -> 24h deadline with no accepted response: state EXPIRED; recovery_enabled=false; no key/link; stale Accept rejected
  -> Accept: generate unique one-time Disaster Recovery Key in R BlackBox;
             commit irrevocable S→R association; recovery_enabled=true
```

Actual protocol must make destination acceptance, final binding, and key commitment logically atomic; generating an inaccessible key or finalizing binding before it can be safely delivered could strand funds. Network proof should authenticate acceptance and bind it to S, R, action, nonce and exact immutable address. BlackBox approval does not prove two humans are the same person. Existing two-factor SOURCE authorization remains required before request issuance.

## Current priority / Next single product question

**Q5 ANSWERED:** Option A. Register immutable disaster destination only when **Wallet Private Key + TongNet Authenticator** both approve initial setup. After registration, destination and one-use secret are immutable forever.

**Q6 CONFIRMED:** Active disaster recovery moves available/unlocked funds immediately. Any already-triggered transfer retains its receiver's 24-hour claim right. If receiver does not claim, during the subsequent 72-hour sender recovery window a one-time sender Claim Key that the owner already possesses can instead authorise claim **to the bound recovery wallet**, but ONLY when Run Disaster Recovery was actually finalised for the original source wallet. The Claim Key is still required, expiry is unchanged, and one-time spending is enforced. No automatically fabricated Claim Key. A missing sender Claim Key cannot be bypassed. Proposed 96-hour reserve rule stays as described, subject to legal review.

**Q7 ANSWERED (Option A, 2026-10-24):** A lock from an **untriggered** outgoing Send is NOT swept early. The original 3h timer continues. If Run Disaster Recovery has finalized in the meantime, source is DEAD and cannot authorise any new Trigger; when its original deadline arrives, the automatic untriggered refund must be paid **directly to the pre-registered bound Disaster Recovery Wallet**, not to DEAD source and not to receiver. Disaster Recovery does not wait. Atomically settle once; preserve original no-manual-cancel rule.

**Q8 new clarification (2026-10-24):** The one-time Disaster Recovery Key originates **inside the registered DESTINATION wallet's own BlackBox**, rather than being minted or shown in the SOURCE wallet. This is a custody/delivery rule, but is **not by itself a cryptographic destination private-key signature** or proof the same natural person controls both addresses.

**Q9 ANSWERED:** no pairing or key while pending; destination must explicitly ACCEPT in its own BlackBox; after acceptance key is generated there and irreversible link is committed. On REJECT, send notification to source BlackBox; no configuration. **NEXT Q10:** how long may a request remain unanswered before it expires (or does it remain pending indefinitely)?

## Security warning

These are design requirements only. A stolen wallet key together with the recovery key can execute an irreversible sweep to the **fixed** destination, potentially causing loss or denial of service; if the destination is attacker-controlled because initial setup was compromised, it could cause total theft. Keys must never be committed in plaintext to public/shared repositories. Atomic settlement must be proven.

## Superseded design remarks

- Early discussion entertained recovery execution using only the Wallet Private Key. **Superseded:** recovery always requires Wallet Private Key **plus** the distinct Disaster Recovery Key.
- Early draft asked whether users could change or replace a recovery destination/key. **Resolved: no, never.**
- The independent TongNet Authenticator is **required at initial setup** (Q5 Option A), but is **not required to run emergency recovery**, which instead needs Wallet Private Key plus the one-use Disaster Recovery Key.

## Q7 — Pre-Trigger locks during completed disaster recovery (confirmed, 2026-10-24)

- Example: 1,000 TONG in original wallet, 700 immediately spendable and 300 locked in a Send never yet Triggered. Source performs authenticated Run Disaster Recovery with original wallet secret + one-use Disaster Recovery Key: available 700 (less applicable fee) transfers now to immutable linked recovery destination R and original source becomes permanently DEAD. The separate 300 remains locked until **its original t0+3h deadline**. This is not an early cancellation.
- With original sender permanently DEAD, **no further Trigger** may be authorized by it. If no Trigger was accepted before successful DEAD finality, at t0+3h the original lock is **automatically refunded straight to R** via the previously authorized S→R immutable recovery binding.
- If a Trigger had already become final **before** the source turned DEAD, treat that payment under Q6 receiver-claim/sender-reclaim rules instead. Define deterministic ordering for simultaneous Trigger vs DEAD vs expiry; prove no double-payment.
- No fresh credential is needed for untriggered **automatic** expiry refund. This rule must not be confused with a **Trigger-confirmed** transaction that requires the original sender Claim Key to reclaim after receiver nonclaim.
- The original three-hour lock remains noncancellable, cannot be accelerated by disaster recovery, and creates no recipient Claim Key in the untriggered path.

## Q8 — Where the one-use disaster secret is created (confirmed 2026-10-24)

- First setup is initiated in the SOURCE wallet's ordinary settings and requires SOURCE Wallet Private Key plus its TongNet Authenticator. The target recovery address is permanently bound to the source once setup is final.
- **The one-time Disaster Recovery Key is generated within the TARGET/RECOVERY WALLET'S OWN TongNet BlackBox** only on destination ACCEPTANCE of the initial request, not within the original source wallet and not as an ordinary unsecured screen response. The key is meant to be accessed and backed up securely by whoever controls the target's BlackBox.
- In a later emergency, the original source wallet may lack its own Authenticator; the user proves source Wallet Private Key plus the SAME one-time Disaster Recovery Key from the destination BlackBox to invoke recovery. This execution requires neither source BlackBox nor a current source Authenticator code.
- The network must maintain a protected, verifiable commitment linking the one-use key to **this specific source wallet, exact immutable destination wallet and this particular recovery action**. Do not store the plaintext secret in public state or GitHub; only the destination's authorized encrypted vault should hold/display it.
- Destination BlackBox key generation and a **cryptographic signature by destination wallet private key** are different mechanisms. The owner's answer explicitly specifies the former. Whether destination must separately ACCEPT/sign, and when the irreversible link becomes final, is the NEXT question (Q9).
- Do not confuse the **Disaster Recovery Key** with one-time Sender Claim Keys from ordinary outgoing transactions. Different operations; different state/commitments.

## Q10 confirmed — 24-hour pending request expiry (Option A, 2026-10-24)

- Unanswered destination BlackBox pairing request automatically expires after **24 hours**. It does not generate a one-time Disaster Recovery Key or install an immutable source→destination binding.
- Pending means recovery is **NOT_CONFIGURED**; Expired also means **NOT_CONFIGURED**. Rejected is another closed, unconfigured state.
- A destination Accept only succeeds if valid and finalized **before the expiry boundary**; after expiry it is invalid. Accept/Reject/Expiry races, replay, timestamp definitions, offline delivery and network partition ordering must be deterministic and are not yet technically implemented.
- Pending expiry must be based on authoritative network-accepted request time, not the local device clock (exact consensus time procedure TBD). The user's rule is a 24-hour window, not a user-selected wall-clock date.
- The no-change-forever rule applies only **after an ACCEPT is finalized**, not to a request that expired without a key.

## Next open question Q11

If S has already sent one PENDING disaster recovery request to R, can S **cancel it and submit another request** before R accepts, or must S wait for R Reject or the 24-hour automatic expiry? Also separately define acceptance-vs-withdrawal race ordering. No rule has been decided yet.
