# TongNet Disaster Recovery Wallet — Current Design (2026-10-24)

**Design only:** not implemented, verified, audited or ready for real-money use.

## Product and three independent keys

The user can optionally set **one** disaster recovery destination address in **normal Wallet Settings**, **not inside TongNet BlackBox**. At that moment a distinct, optional, one-time-use **Disaster Recovery Key** is issued.

The project now has three secret-key categories:
1. **Wallet Private Key** — ordinary wallet access and initiating payment.
2. **TongNet Authenticator Master Key** — independent TongNet BlackBox authorization factor (60-second changing access codes, not a rotating master key).
3. **Disaster Recovery Key** — exists only for wallets whose disaster recovery option was configured; a **one-use secret** required for emergency sweeping. It is NOT the backup wallet's address or its private key.

## Permanent configuration rules — confirmed by user

- Register the optional disaster destination once. **After it is set, its address cannot ever be changed.**
- The corresponding **Disaster Recovery Key also cannot be changed, replaced, regenerated, or reset** once issued.
- If the Disaster Recovery Key is **lost**, this disaster recovery route is permanently unavailable for that wallet. Possessing Wallet Private Key alone does **not** bypass the missing recovery secret.
- If Wallet Private Key **and** Authenticator Master Key remain available, the user may still normally send the wallet's funds to another active wallet using the regular BlackBox-triggered transaction process. **That does not change the old immutable disaster destination or its recovery key.**
- Provide very clear warnings and require accurate, explicit confirmation of the destination and key backup at setup; no administrative override is allowed under these requirements.
- **Q5 CONFIRMED — Option A (2026-10-24):** INITIAL irrevocable recovery address registration requires both valid **Wallet Private Key authorization AND TongNet Authenticator approval**. A stolen wallet private key alone cannot set the destination. No further change is allowed once the address and key are committed.

## One-time emergency execution — confirmed

1. Owner has access to source **Wallet Private Key** but lost the Authenticator Master Key / BlackBox access.
2. Open source Wallet using Wallet Private Key.
3. Select **Run Disaster Recovery** and enter the **one-time Disaster Recovery Key**.
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
- Pre-trigger 3-hour autorefunda are **not resolved** in this decision; see Q7.

## Not yet decided (engineering safety problems)

- **Q6 CONFIRMED, Triggered transfers:** immediately sweep ONLY currently unlocked/spendable funds. Keep the locked amount inside its existing transaction escrow and preserve receiver's entire 24-hour claim entitlement. If unclaimed, the already issued sender's one-use Claim Key may be used **from the original wallet's previously linked recovery wallet** during the following 72 hours, even after the original wallet has become DEAD. If the sender has lost that Claim Key / BlackBox access and cannot present it, recovery alone does NOT bypass it; the existing expiry and proposed network-reserve rule still apply. **Special case not yet decided:** a transfer still in the separate 3-hour PENDING_TRIGGER phase must be discussed in Q7.
- **First-setup authentication confirmed:** BOTH Wallet Private Key authorization and TongNet Authenticator approval. Exact phishing-resistant transaction-bound proof, device compromise resistance and atomic enrollment still require formal protocol design.
- Recovery destination activation status, cryptographic binding and proof of control; wrong address irreversible.
- Can a wallet with no setup still be safe? Yes, standard wallet remains active; disaster feature absent.
- Key format, secure one-time commitment, replay resistance, consensus deadlines, network partitions, fees, expiry with insufficient spendable balance, and fault-tolerant atomic finality.
- Alternative normal transfers after loss of disaster key (if both other keys survive) still use the already confirmed 3-hour trigger, 24-hour receiver claim, and 72-hour sender recovery. Merely initiating a standard send does not instantly credit a new wallet.

## Current priority / Next single product question

**Q5 ANSWERED:** Option A. Register immutable disaster destination only when **Wallet Private Key + TongNet Authenticator** both approve initial setup. After registration, destination and one-use secret are immutable forever.

**Q6 CONFIRMED:** Active disaster recovery moves available/unlocked funds immediately. Any already-triggered transfer retains its receiver's 24-hour claim right. If receiver does not claim, during the subsequent 72-hour sender recovery window a one-time sender Claim Key that the owner already possesses can instead authorise claim **to the bound recovery wallet**, but ONLY when Run Disaster Recovery was actually finalised for the original source wallet. The Claim Key is still required, expiry is unchanged, and one-time spending is enforced. No automatically fabricated Claim Key. A missing sender Claim Key cannot be bypassed. Proposed 96-hour reserve rule stays as described, subject to legal review.

**NEXT Q7:** What if the locked transfer has NOT been Triggered yet? At the 3-hour auto-refund deadline, should the returning amount automatically credit the permanently linked Disaster Recovery Wallet of the now-DEAD original wallet, or should disaster recovery remain temporarily pending until pre-trigger locks have automatically refunded? The refund must never become stranded in a DEAD wallet.

## Security warning

These are design requirements only. A stolen wallet key together with the recovery key can execute an irreversible sweep to the **fixed** destination, potentially causing loss or denial of service; if the destination is attacker-controlled because initial setup was compromised, it could cause total theft. Keys must never be committed in plaintext to public/shared repositories. Atomic settlement must be proven.

## Superseded design remarks

- Early discussion entertained recovery execution using only the Wallet Private Key. **Superseded:** recovery always requires Wallet Private Key **plus** the distinct Disaster Recovery Key.
- Early draft asked whether users could change or replace a recovery destination/key. **Resolved: no, never.**
- The independent TongNet Authenticator is **required at initial setup** (Q5 Option A), but is **not required to run emergency recovery**, which instead needs Wallet Private Key plus the one-use Disaster Recovery Key.
