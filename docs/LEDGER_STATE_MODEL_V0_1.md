# TongNet ledger state model v0.1

**Status: proposal for a test-only reference model.** This document is evidence for TN-SPEC-001, not an owner-ratified financial protocol, production code, audit, or authorization to move value. The account-based structure is an architect-selected prototype baseline. Any changed financial right still requires explicit owner approval and an ADR.

## Authority and scope

This proposal preserves the current confirmed direction: one native TONG asset; a receiver claim request does not settle an escrow; the Sender must separately approve the exact request through the Sender BlackBox; the receiver has a nominal 24-hour priority followed by the Sender's manual 60-day reclaim period. No automatic transfer to the Network Reserve is specified. The exact timer origin and cutoff rules remain unresolved.

The reference model uses unsigned integer atomic amounts and checked arithmetic. Its prototype width is `u128`; the production width, decimal scale, encoding, and issuance policy remain unselected. The test faucet creates valueless localtest units only.

The companion files are:

- [`ledger-state-model.v0.1.json`](ledger/ledger-state-model.v0.1.json): machine-readable accounting categories, invariants, operations, and test matrix.
- [`transaction-envelope.v0.1.schema.json`](ledger/transaction-envelope.v0.1.schema.json): a test-only JSON Schema for the finite transaction envelope.

`TRANSFER` is included as the basic account-to-account operation needed to exercise conservation properties. Time-window labels below are derived eligibility from an explicit finalized, versioned policy context; no wall-clock or timer event independently mutates an escrow.

## Accounting model

Every live unit appears in exactly one category:

1. `spendable` — account balance available for an otherwise valid operation.
2. `escrow_locked` — value held for an identified escrow obligation.
3. `validator_bonded` — bonded value, kept separate from spendable value.
4. `fee_escrow` — value reserved for an explicitly authorized fee budget; fee rules are outside this proposal.
5. `pending_rewards` — earned but not yet spendable value.
6. `protocol_reserve` — value already transferred there by an explicitly authorized rule. This model defines no automatic 60-day transfer rule.

Let `live_supply` be the checked sum of those six categories across all accounts and escrow records. At every committed state:

```text
live_supply + cumulative_burned
  = initial_issued + test_faucet_issued + approved_issuance
```

For the test-only model, `approved_issuance` is zero. A faucet operation increments both the recipient's `spendable` amount and `test_faucet_issued` by the same amount. A burn operation is not part of the v0.1 transaction set; `cumulative_burned` is reserved for a later explicitly specified operation.

No amount uses floating point. Amounts, sums, debits, and any later fee multiplication use checked integer operations. Overflow, underflow, a zero-value financial action, or a debit exceeding its source category rejects the candidate transition atomically.

## Transaction and authorization rules

The envelope contains a chain identifier, protocol version, signer, signer nonce, finite operation tag, operation-specific payload, authorization records, and an explicit validity context. Signatures must bind the chain identifier, protocol version, signer, nonce, role, operation, canonical payload, and validity context. This prevents replay across networks, versions, accounts, operations, or authorization roles.

The JSON Schema is an implementation aid for fixtures. It does not select a production cryptographic algorithm, address format, binary codec, hash function, or deadline clock. Raw claim codes, private keys, authenticator secrets, and recovery secrets are not transaction payload fields. An authorization carries a signature or opaque proof reference, never plaintext secret material.

The nonce is a monotonically increasing per-signer value. A committed operation must match the current nonce and increment it in the same atomic state transition. A stale, duplicate, or future nonce cannot apply effects. In this test model, any rejected operation is state-neutral, including its nonce; production fee treatment for rejected transactions remains unresolved.

For byte-identical duplicate submissions, at most one transaction can take effect. Different transactions using the same signer and nonce are ordered by finalized block order; the first valid state transition consumes the nonce and later submissions are rejected without effects.

## Escrow lifecycle for model tests

The proposal models the confirmed manual approval sequence without deciding unresolved timer mechanics:

```text
LOCKED
  -> CLAIM_PENDING       on an addressed receiver's valid CLAIM_REQUEST
  -> PAID                 only after sender-authorized FINAL_ACCEPT
  -> SENDER_RECLAIMABLE   after the configured receiver-priority boundary
  -> RECLAIMED            on a valid sender-authorized SENDER_RECLAIM
  -> POLICY_PENDING       after the configured sender window; no automatic payout
```

`CLAIM_REQUEST` changes no monetary category. `FINAL_ACCEPT` must bind to one existing claim request and the exact escrow, receiver, and amount. It moves escrow to receiver spendable value once. `SENDER_RECLAIM` moves escrow to sender spendable value once, and only when a supplied, versioned deadline policy says reclaim is eligible. Repeated or conflicting terminal actions cannot release value twice. The receiver-priority origin, consensus clock, delay-compensation proof, exact exclusive cutoff, and treatment of an outstanding claim at that cutoff are not decided here.

The displayed eligibility labels are derived from the operation's explicit policy context and finalized chain context; they are not stored transitions caused by elapsed local time. A `FINAL_ACCEPT` must satisfy the owner-confirmed receiver-priority rule under that policy. The policy decides how an outstanding claim is treated at the boundary, which remains unresolved.

The `RECOVERY_PAIR` envelope is metadata-only in this proposal. `RECOVERY_RUN` has no modeled balance effects until the lost-key, late sender-claim, archive key-release, locked-entitlement, and destination-death cases are specified in their owning issues. This prevents the schema from implying a solved recovery mechanism.

## Deterministic execution and state roots

Only deterministic execution of finalized transactions may change ledger state. Mempool checks, block proposal, RPC queries, local clocks, and UI state are read-only. The state transition receives all validity and deadline inputs through explicit, versioned protocol context; it never reads wall-clock time itself.

For repeatable roots, implementations must define a canonical encoding, stable account and escrow ordering, domain-separated leaves and root, and a protocol-versioned root format. This issue records those requirements without selecting CBOR/Protobuf, a hash function, or a production state-root upgrade policy. Identical initial state plus identical finalized transaction order and context must produce byte-identical state and root on every implementation.

## Test cases ready for implementation

The machine-readable matrix defines the v0.1 cases for conservation across transfers, locks, and settlements; checked overflow; nonce/replay protection; failed-transition atomicity; one-winner escrow settlement; sender approval; deadline parameterization; recovery deferral; and deterministic replay. These are specifications for later code and tests; no test result is claimed by this document.

## Decisions still open

- Exact 24-hour timer origin, time source, boundary rule, and network-delay compensation.
- Production amount width, decimal scale, chain identifier encoding, canonical transaction codec, hash/signature algorithms, and address format.
- Whether a rejected finalized transaction consumes nonce or fees.
- Fee escrow settlement, reward issuance, validator bond/slashing accounting, and production supply/genesis rules.
- Rights after the Sender's 60-day reclaim window; reserve transfer remains blocked for real value.
- K_R and K_S lifecycle, recovery after loss of the source signing key, conditional archive decryption, and recovery execution around open escrows.
- State-root hash/codec and upgrade/migration rules.

Closing TN-SPEC-001 requires owner/architect review of this proposal and implementation-ready bounded invariants. It does not close TN-TEST-001, validate real assets, or clear any mainnet blocker.
