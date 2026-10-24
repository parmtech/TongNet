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

## Not yet decided (engineering safety problems)

- **Locked or triggered transfers:** user wants ALL funds swept. However, value already locked in a pending or triggered transfer can carry another person's claim entitlement, and triggering cannot be cancelled by sender. An emergency sweep must **not double spend** that value. Define eligible/unlocked value, pending-transfer handling and later resolution before coding.
- **First-setup authentication confirmed:** BOTH Wallet Private Key authorization and TongNet Authenticator approval. Exact phishing-resistant transaction-bound proof, device compromise resistance and atomic enrollment still require formal protocol design.
- Recovery destination activation status, cryptographic binding and proof of control; wrong address irreversible.
- Can a wallet with no setup still be safe? Yes, standard wallet remains active; disaster feature absent.
- Key format, secure one-time commitment, replay resistance, consensus deadlines, network partitions, fees, expiry with insufficient spendable balance, and fault-tolerant atomic finality.
- Alternative normal transfers after loss of disaster key (if both other keys survive) still use the already confirmed 3-hour trigger, 24-hour receiver claim, and 72-hour sender recovery. Merely initiating a standard send does not instantly credit a new wallet.

## Current priority / Next single product question

**Q5 ANSWERED:** Option A. Register immutable disaster destination only when **Wallet Private Key + TongNet Authenticator** both approve initial setup. After registration, destination and one-use secret are immutable forever.

**Q6 (OPEN):** If disaster recovery is run while ordinary outgoing transactions already have *locked* funds (including a triggered receiver claim window), should the system sweep only currently spendable value and preserve all existing recipient rights, redirecting any legitimate future refunds/recoveries to the pre-set Disaster Recovery Wallet as they become payable; or wait until every pending transaction resolves before executing the final sweep? Needs user decision and concurrency proof.

## Security warning

These are design requirements only. A stolen wallet key together with the recovery key can execute an irreversible sweep to the **fixed** destination, potentially causing loss or denial of service; if the destination is attacker-controlled because initial setup was compromised, it could cause total theft. Keys must never be committed in plaintext to public/shared repositories. Atomic settlement must be proven.

## Superseded design remarks

- Early discussion entertained recovery execution using only the Wallet Private Key. **Superseded:** recovery always requires Wallet Private Key **plus** the distinct Disaster Recovery Key.
- Early draft asked whether users could change or replace a recovery destination/key. **Resolved: no, never.**
- The independent TongNet Authenticator is **required at initial setup** (Q5 Option A), but is **not required to run emergency recovery**, which instead needs Wallet Private Key plus the one-use Disaster Recovery Key.
