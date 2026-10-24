# TongNet Disaster Recovery Wallet (TDRW) — Design Draft 0.1

**Status:** User-specified feature requirement (2026-10-24), not implemented, tested, audited or safe for real funds.

## Purpose
Provide an optional, user-designated safety destination for a wallet whose TongNet Authenticator Master Key or BlackBox access has become unavailable, while wallet private-key control remains.

### Product name
**TongNet Disaster Recovery Wallet**. The recovery action is **Run Disaster Recovery**.

## Updated key architecture (additional user clarification, 2026-10-24)

There are now **three distinct key categories**, with the third OPTIONAL:

1. **Wallet Private Key** — primary wallet authority.
2. **TongNet Authenticator Master Key** — independent second factor behind BlackBox/authentication.
3. **Disaster Recovery Key** — OPTIONAL, exists only if user opts into recovery. This must be logically distinct from the *recovery wallet address* and from the other two key categories.

**OPEN — crucial:** User has not yet specified whether the Disaster Recovery Key is required when invoking Run Disaster Recovery, only when enrolling/setting/changing its recovery address, or serves another purpose. Earlier Q3 says no BlackBox/Auth code is needed to run recovery and wallet private-key access remains. Do NOT silently assume the third key is required OR not required for recovery execution; ask the user. Do not confuse the backup wallet's own private key with the source wallet's recovery key.

## User-confirmed requirements (Q3 response)
1. A TongNet Wallet has an **optional recovery-wallet address** field in ordinary wallet settings; **not inside TongNet BlackBox**.
2. The user may register the address of **another TongNet wallet** under their control as recovery destination. The wallet remains usable if this feature is not enabled, subject to normal rules.
3. The recovery path is designed particularly for the situation where the original wallet's **Authenticator Master Key or BlackBox access is lost**, but its normal wallet private key/access remains available.
4. The original wallet user initiates the **Run Disaster Recovery** action from the original wallet. **Executing this action does NOT require BlackBox access or an Authenticator code**, unlike normal transfer triggering.
5. Once a valid recovery action commits, **all eligible value** of the source wallet must be moved to the **previously registered destination wallet**, minus any applicable network fee; the whole balance is intended to be swept, not just an amount selected by the user.
6. The source wallet then enters a **permanent DEAD state**, and cannot be activated or used again.
7. This is a **one-way, terminal action**, rather than a way to restore access to the old BlackBox or recover its Authenticator Master Key.
8. **No recovery destination configured:** this particular recovery function is unavailable; policies for other loss scenarios remain to be designed.

## Illustrative flow

```text
ACTIVE source wallet
   -> (optional, beforehand) save designated Disaster Recovery Wallet address
   -> lose TongNet Authenticator / BlackBox access
   -> open source wallet with original wallet private key
   -> Run Disaster Recovery [NO BlackBox / OTP prompt]
   -> network verifies signed recovery instruction + pre-registered address
   -> atomically sweep eligible funds minus applicable fee
   -> credit only the pre-registered destination
   -> permanently mark the source wallet DEAD
```

**Atomicity is mandatory:** it must never pay without marking the source wallet dead or mark the wallet dead before value is safely committed. Network finality and ordering are not yet designed.

## Critical security implications

- If a thief has the **original wallet private key**, they can invoke this no-BlackBox recovery path. When the destination is already securely fixed, the thief should not be able to redirect funds to an arbitrary attacker wallet, but **they could permanently disable the wallet and cause loss of access or grief**.
- **Most important unresolved choice:** What authentication is required to **register or change** the destination wallet address? If an attacker holding only the wallet private key can replace this destination, the recovery feature could bypass the entire BlackBox/Authenticator security model and allow total theft.
- A recommended design for consideration (NOT approved) is to pre-authorize registration and changes with a distinct stronger factor, cryptographic address confirmation, and a safety delay; action execution can then remain wallet-key-only as requested.
- Destination must be a valid, network-verifiable, ACTIVE TongNet wallet. Optional proof that the owner controls the receiving destination reduces misdirection risk. Neither rule has been fully specified yet.
- The user said **all funds A to Z**, but current protocol may already have **locked pending transfers, receiver windows, sender recovery claims or escrow**. Whether disaster recovery may touch locked funds is **UNDECIDED** and must not silently violate earlier irreversible Trigger and receiver claim rights.
- Fee behaviour: user permits deduction of any actual network fee from swept funds; exact fees, minimum balances, priority and refund policy remain open.
- Concurrency/atomicity: ongoing transfers and simultaneous recovery transactions cannot double-spend or contradict permanent DEAD state. Account deactivation and sweeping must have deterministic finality.
- Post-migration recovery target private key can itself be lost or compromised; circular recovery referrals or destination loops require deliberate rules.
- The existing **unactivated-wallet 72h DEAD rule** is separate: wallets that never completed initial authenticator enrollment cannot simply use disaster recovery to bypass activation (subject to explicit further decision).

## State model (proposed)
```
ACTIVE_WITH_RECOVERY_DESTINATION
  -- signed RunDisasterRecovery --> RECOVERY_FINALISING
  -- atomic sweep and terminal marking --> DEAD_AFTER_DISASTER_RECOVERY
```

In a network partition it is unsafe to consider the source DEAD locally if the sweep has not been globally finalised.

## Open decision — ask NEXT
**New Q4 clarification (higher priority):** What is the role of the optional Disaster Recovery Key? Must a Run Disaster Recovery use both original wallet private key AND recovery key, or is recovery key used for setup/address changes only (with original wallet key alone still sufficient to execute)? Avoid assuming the implementation.

## Following decision (after Q4)
**May the disaster recovery destination be registered or changed with only the normal wallet private key, or should initial registration/updates additionally require TongNet Authenticator approval, even though executing Run Disaster Recovery must NOT require it?**

This is specifically about setting/changing destination, NOT executing the already-configured recovery operation.
