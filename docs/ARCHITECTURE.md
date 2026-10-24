# TongNet — Architecture Research Map (Draft)

**Everything below is a possible architecture direction, not an adopted or implemented protocol.**

## Logical subsystems

1. **Client wallet:** generate/manage signing keys, addresses, balances, and payment-intent locks.
2. **Authenticator device/app:** enrol with one-use setup credential; derive rotating 60-second access codes and ideally require phishing-resistant hardware-backed transaction challenge signing.
3. **BlackBox layer:** privately receive per-transaction authorisation and claim entitlements, independently encrypted and protected, without plaintext secrets in a shared ledger.
4. **Pending transfer engine:** lock value at Send; require separately authorised Trigger; auto-refund at 3h if untouched.
5. **Claim engine:** receiver address + one-time entitlement + wallet authority for 24h from Trigger.
6. **Recovery engine:** sender address + one-time recovery authorisation for next 72h.
7. **Settlement and state agreement:** *unsolved primary research task*. Requires a consistent shared state across mutually distrustful independent nodes to prevent double spend and control deadline races.
8. **TongNet Network Reserve:** proposed network-operations fund, economically and legally separate from collateral backing the TONG currency.
9. **Economics, governance and upgrades:** fee subsidy, validators' incentives, anti-spam rules, ruleset amendments and reserve audits.

## Candidate design constraints

- Minimise persistent global transaction history and user data, but maintain enough authentic state to prevent duplicate value expenditure.
- Avoid global mining and traditional proof-of-stake; examine what assumptions can actually make Byzantine quorum or witness-based finality safe against fake nodes.
- An algorithm that just lets two interested users agree privately is not sufficient for a permissionless transfer of spendable money; independent verification of prior ownership is required.
- No dependence on a single cloud vendor, website, certificate provider, app store, messaging server or coordinator. Reliance on network hardware, time references, cryptography and economic incentives cannot be eliminated.
- Secure encrypted and replicated BlackBox delivery must not make an unread inbox credential a transferable bearer token.
- Claim, recovery, expiry and reserve movements must be atomic and idempotent.
- Define clock-source integrity, visibility under partitions, recovery after prolonged offline operation and transaction sizes.

## TONG economic value: unresolved

A "valuable coin" requires economic utility and/or reliable redemption backing, not a label. If pegged/redemption-backed, reserve issuance, independent custody, audit, legal rights, and AML/financial obligations become major dependencies. If floating-value, market value is not guaranteed. An AUD 1:1 peg was **only an illustrative idea**, not a product decision.

## Minimum useful prototype

Start with simulated balances in a deterministic local test harness and **no real funds**. Implement the full state machine, duplicate-claim detection, clocks and race conditions; then design a decentralised consensus algorithm and evaluate against partitions/adversarial nodes, not just happy-path transfers.

No honest performance, privacy, fee or security comparison with Bitcoin can yet be made before measurement.
