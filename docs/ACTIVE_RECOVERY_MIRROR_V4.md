# TongNet Active Recovery Mirror v4 — wallet stays ACTIVE while protecting another wallet's sealed BlackBox

**LATEST OWNER PRODUCT DIRECTION (2026-10-25, Australia/Sydney).** Supersedes *all* earlier RECOVERY_RESERVED_FROZEN wallet-operation constraints. Design only: no code, audited encryption, proven availability or testnet.
**Project author:** ParmTech; **original concept creator/developer:** Manjinder Singh. Concept origin 2015 and first public disclosure 2026 per creator statements, not independently verified.

## Explicit owner change
- Two completely separate normal wallet addresses S and R can both be **NORMAL_ACTIVE simultaneously** even after S nominates R as its immutable Disaster Recovery destination and R explicitly ACCEPTS the pairing inside its own BlackBox (earlier two-sided setup authorisations retained).
- R retains its independent wallet private key, Authenticator, BlackBox, balance, transaction history, ordinary SEND / RECEIVE / CLAIM and unrelated wallet business while S remains NORMAL_ACTIVE. **DO NOT freeze or block R's ordinary wallet operations merely because it is bound as S's recovery destination.**
- R may optionally designate its OWN further Recovery Wallet C (R -> C), with its own independent pairing process and rules, *while it already serves as recovery for S*. Example concurrently: A=NORMAL_ACTIVE, B=NORMAL_ACTIVE+BACKUP_ARCHIVE_OF(A), C=NORMAL_ACTIVE+BACKUP_ARCHIVE_OF(B). No duplicate balance/authority; these are independently functioning wallets plus passive mirrors.
- On an approved binding S -> R, R's BlackBox gains a **separate encrypted, append-only, parent-address-tagged archive namespace** for S, continuously receiving secure encrypted copies of S's BlackBox messages, transaction-specific claim codes/commitments, requests and private records. The S archive is inaccessible and unreadable to R while S has not undergone BFT-final valid S->R Disaster Recovery. R's OWN BlackBox data stays independently accessible and operational. Display the sealed archive's sync/backup checkpoint, not private contents. R's own transactions remain R's; S's on-chain transaction history remains permanently S's and is never relocated/reassigned to R, even after S dies.
- Only an **authentic, one-time, consensus-final RUN_DISASTER_RECOVERY(S,R)** using the earlier protocol's required original S Wallet Private Key plus distinct one-use Disaster Recovery Key held in R BlackBox permits source S to become DEAD, moves S's **eligible UNLOCKED balance only** once to R as a NEW on-chain recovery transaction, and releases the authenticated S-parent-archive decrypt capability to R. **R stays NORMAL_ACTIVE throughout**: it does NOT become active *because* S dies (it always was active). Parent S archive remains origin-tagged permanently; ordinary R BlackBox records stay separate. R's prior registered recovery successor C is preserved, not deleted or overwritten.
- Parent-archive unlock must require proof of the exact successful S->R disaster recovery, not arbitrary S DEAD (e.g. separate wallet activation expiry or fault). Old S signing authority must not pass to R; protocol-defined pending rights require specific successor rules, not automatic universal control over historical transactions.
- R may still be connected to its own successor C at time it receives S recovery funds. Existing R->C links are **not** automatically changed by S->R; no recursion, cycles or chained lookups are valid without explicit safety rules.
- **IMPORTANT PRIOR-DECISION PRESERVATION:** Owner has CONFIRMED R remains a functioning normal wallet **after binding**, but did **not expressly revoke** the earlier rule that it must be a fresh, never-financially-used address **at the instant of initial binding**. Therefore keep R virgin/zero prior financial history as the current eligibility rule unless owner explicitly changes it. Once R BlackBox ACCEPT reaches finality, R remains NORMAL_ACTIVE and may from that point send, receive, hold balance, claim and pair R->C independently; no freeze. Engineering proposals: require R control/explicit acceptance, reject S=R, cycles, DEAD R and ambiguous multi-source archives; multi-source policy still unratified.
- R is best described as `NORMAL_ACTIVE + RECOVERY_TARGET_FOR(S) + SEALED_PARENT_ARCHIVE(S)`, **NOT as a frozen wallet category**. The `SEALED` state is per ARCHIVE, not per WALLET.

## Required independent state machines
```text
Wallet S: NORMAL_ACTIVE --(Final authorized RUN_DISASTER_RECOVERY(S,R))--> DEAD
Wallet R: NORMAL_ACTIVE -> stays NORMAL_ACTIVE before, during and after S recovery
R archive(S): NOT_BOUND --(R BlackBox ACCEPT + final pairing)--> SEALED_MIRRORING
             --(final authorized RUN_DISASTER_RECOVERY(S,R))--> VERIFIED_UNSEALED_PARENT_ARCHIVE
Wallet C: NORMAL_ACTIVE (if independently paired as R's recovery)
R archive(R) on C: SEALED_MIRRORING -> only unseal on separate valid RUN_DISASTER_RECOVERY(R,C)
```
These independent states must be transactionally consistent with BFT consensus; do not conflate a parent archive's sealed status with R's spendable-wallet status. Exactly-once recovery; no copying/minting balances; no double claims; no authentication circumvention.

## Storage layout proposal
```text
Wallet R / BlackBox
  OWN (normal readable inbox, own claim codes, own signing authority)
  RECOVERY_ARCHIVES
    S
      parent_wallet_address = S [provenance tag]
      status = SEALED
      verified_sync_checkpoint = height/hash
      encrypted_records = [...]
      historic transaction ownership = STILL S (not copied/migrated)
```
After authenticated successful S->R disaster only `RECOVERY_ARCHIVES/S` becomes VERIFIED_UNSEALED with permanent "Recovered from wallet S" origin marker. In addition, if R has its own recovery C, R's BlackBox changes should mirror safely to C without leaking any still-SEALED parent S data. Whether a now-unsealed S archive should onward-mirror to C is a **privacy and continuity policy question, NOT automatically approved**; use no recursive data disclosure by default unless separately authorised.

## Cryptographic feasibility / security
- Strong encryption and signed provenance must be per archive namespace, *not* reusing R's ordinary wallet spending private key as a universal decryption master. Backups need authenticated encryption, deterministic version/replay ordering, incremental snapshots, independent replication and continuity proof. No raw claim codes, wallet private keys, Authenticator Master Keys or disaster secrets on public ledger or server. Parent-address label may be a private encrypted metadata tag while public commitments minimally permit pair verification.
- **The key paradox persists:** if R holds the complete decryption key of S's archive while S is alive, R's active owner or malware can decrypt it offline despite hiding UI. For true pre-recovery unreadability, R must **not** hold sufficient decryption capability before S's authenticated recovery. Candidate is an audited conditional threshold decryption/key-release scheme involving independent validator/key-share custodians and cryptographic proof of BFT-final S->R recovery, with privacy, collusion threshold, rotation/resharing and availability assumptions; this adds parties supplying cryptographic key shares but NOT any third-party deal arbitration. Alternatives hardware-protected guarded release or protected user-held independent recovery share have their own device/provider trust and loss tradeoffs. No unilateral exact truth of on-chain state inside offline ciphertext. Research, formal model and audit mandatory.
- Source S generating its NEW sender reclaim key K_S only after 24h is incompatible with S BlackBox loss/death; continuous earlier mirror alone cannot copy a secret not yet generated. Recoverable derivation/precommit solution requires owner consent. Receiver 24h priority then following S 60-day manual reclaim remain in force; unresolved reserve forfeiture still blocked for real-money launch.
- **HIGH-PRIORITY new failure:** R may run its own R->C disaster first, becoming DEAD while it is still immutable recovery target for S. Then S->R cannot simply credit funds to DEAD R, nor release S archive to a dead recipient. Need an explicit choice about chaining authorised binding to currently active C versus reject/pause S recovery, with protections against redirection and cycles. Do NOT auto-forward S money to C without owner authorisation.
- If R's own BlackBox is compromised, it can sign ordinary R payments. That must not suffice to decrypt sealed S archive or trigger S disaster without independent S private-key and one-use Recovery proof, subject to approved key-custody threat model.
- Distinguish accepted pairing *permission* from disaster *execution*. Source S pairing accepts R's normal usage; R's state remains unchanged financially.

## Test requirements before real funds
1. S and R both send and receive independent payments throughout binding; no request/claim leakage from S seal.
2. R already has a balance and history; neither are overwritten or attributed to S.
3. S disaster transfers only eligible unlocked S balance once to R, atomically kills S, unlocks only S's sealed private archive, preserves R's ordinary records and R->C relationship.
4. Forged disaster signatures, wrong parent ID, early decryption share release, compromised mirror replica, wallet resurrection, parent archive rollback and validator split reject/fail closed.
5. R runs disaster R->C before S->R: no accidental credit to DEAD R or unauthorised C. Requires explicit selected design.
6. Concurrent S->R and R->C disaster, different network partitions, mid-rekey faults, recovery share holders refusing cooperation and source BlackBox offline/erased.
7. Never report implementation complete without code, adversarial simulation and independent review.

**Summary:** Owner wants R as a fully functioning NORMAL wallet that also carries a separate sealed parent S BlackBox archive, not a frozen wallet. This is an explicit product change. Engineering of actually unreadable archives, parent-right succession, and ancestor chain death remains OPEN.
