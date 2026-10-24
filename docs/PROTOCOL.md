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

**New key requirement (2026-10-24):** The product has three separately designated key categories: (1) wallet private key, (2) authenticator master key, (3) optional disaster recovery key generated/provisioned if recovery is enabled. Their secret materials and permissions must be distinct. The third key's enforcement role is **UNDECIDED** pending Q4; do not implement a bypass on assumptions. Recovery destination wallet address is separate from recovery key.


- Optional destination is registered in normal Wallet settings, not BlackBox; the authentication needed to add/change it remains undecided.
- When BlackBox/Authenticator is inaccessible but the original wallet private key is available, **Run Disaster Recovery** executes WITHOUT requiring BlackBox access or a rotating Authenticator code.
- Intended outcome: atomic full sweep of **eligible** wallet balance, minus actual applicable fee, to **previously registered** recovery address; then original wallet enters a permanently DEAD state. Recovery never permits arbitrary destination changes at execution.
- Critical unresolved conflict: pending locked, triggered, and recipient-claimable transfers cannot be cancelled or double spent by a disaster sweep without explicitly reconciling earlier protocol rules.
- Critical security issue: wallet-key-only recovery plus wallet-key-only changing of destination could bypass the payment's two-factor protection. See [DISASTER_RECOVERY.md](DISASTER_RECOVERY.md).

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
