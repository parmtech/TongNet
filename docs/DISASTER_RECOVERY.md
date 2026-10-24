# TongNet Disaster Recovery Wallet — Living Design Specification

**Status:** user-confirmed functional requirements, not implemented, security-audited or approved for real money. Updated 2026-10-24.  
**Product name:** TongNet Disaster Recovery Wallet (optional).  
**Action:** Run Disaster Recovery.

## Three key categories — confirmed

1. **Wallet Private Key** — main wallet access, transfers and transaction initiation.
2. **TongNet Authenticator Master Key** — separate security factor, generating 60-second rotating access codes for TongNet BlackBox. The master secret itself does not rotate each minute.
3. **Disaster Recovery Key** — OPTIONAL separate one-time secret, issued **only when a disaster recovery destination wallet address is set**. A distinct key from both other keys; NOT the recovery wallet address.

## Enrollment / configuration — user requirement

- In **normal wallet settings**, NOT inside BlackBox, the owner may optionally add the address of another TongNet wallet as a disaster destination.
- When the destination is successfully configured, the owner receives a **new Disaster Recovery Key**.
- If no recovery destination is configured, this optional key/function is not available.
- **CRITICAL OPEN:** authorization to initially register, replace, or remove the recovery destination and handling of key reissuance or multiple attempts have not been settled. We must not assume a stolen wallet key can freely change the destination.

## Emergency execution — confirmed in latest answer

1. The owner has **lost access to the TongNet Authenticator Master Key / BlackBox**, but **still has the original Wallet Private Key**.
2. Owner opens the original Wallet with the Wallet Private Key.
3. If the previously configured disaster destination is present, select **Run Disaster Recovery**.
4. Owner **must enter the separate one-time Disaster Recovery Key**. This is **in addition to original wallet private-key authorisation**.
5. Execution requires **neither BlackBox authentication nor TongNet Authenticator code**.
6. Network must verify wallet authority, recovery-key proof, binding to the pre-set destination and that the key was never successfully consumed.
7. All **eligible** source wallet funds, minus actual network fee if any, move **only to the previously registered disaster destination**. User intent is to rescue the **entire** balance, not choose a partial amount.
8. In the same **atomic final settlement**, recovery key is consumed permanently and original wallet enters **DEAD** state forever. No later access/reactivation/spending of the source wallet.

### Proposed state machine (not implemented)

```text
ACTIVE wallet, no disaster destination
  -> (optional, approved setup) -> ACTIVE + stored recovery address + unique one-time recovery-key commitment
  -> (original wallet private key AND distinct recovery key) Run Disaster Recovery
  -> network verifies bound destination, unspent recovery-key commitment, eligible value and fee
  -> ATOMIC FINAL: pay fixed destination / consume one-time key / mark source wallet DEAD
```

A new or arbitrary destination must never be accepted in the same call that executes emergency recovery.

## Crucial unresolved security questions

- **NEXT Q5**: When initially adding or changing the Disaster Recovery Wallet address in normal settings, does it require **TongNet Authenticator approval**, or is original Wallet Private Key enough? If stolen wallet access permits replacing the destination and generating a fresh Disaster Recovery Key, total theft is possible even though ordinary payments need BlackBox approval.
- What does **all money** mean for values locked in still-pending transfers or already-triggered receiver claim windows? Existing no-cancellation/receiver rights and disaster sweep cannot both spend the same locked amount; define safe eligible balance and later settlement ownership.
- How to handle lost or leaked Disaster Recovery Key prior to use? A key alone must not enable execution. Should regeneration/rotation be forbidden or require authorisation and delay? Undecided.
- Prevent replay/double execution, destination switching, address substitution, insufficient fee, false network clocks, concurrent claims, wrong backup address and lost backup wallet.
- User must see that the disaster action **permanently destroys the original wallet's ability to spend**.
- Issue only a **nonreversible cryptographically random secret** and store a secure commitment/hash, **not the plaintext recovery key** on network nodes or GitHub. Never put real user secrets in project files.
- The existing **72-hour initial activation deadline / permanent DEAD** rule is a separate lifecycle path; this emergency feature cannot bypass a wallet that never activated.

## Important difference from old preliminary notes

Earlier design discussion described wallet-private-key-only disaster execution. **Superseded by newest user clarification (2026-10-24): execution requires BOTH Wallet Private Key AND the newly defined OPTIONAL one-time Disaster Recovery Key; still no BlackBox or Authenticator.** All future protocol and UI documents must follow this version.

## Research status

No prototype exists. Every state transition, signer policy, destination-change rule, key commitment, fee calculation and atomic network settlement requires implementation, tests, threat analysis and audit before real assets.
