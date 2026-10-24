# TongNet Secure P2P v2 — Sender Manual Final ACCEPT (latest canonical direction)

**UPDATE 2026-10-25:** User explicitly chose trusted bilateral P2P/no deal-arbitrating third party; 24h Receiver exclusive priority followed by **60 FULL DAYS** Sender-exclusive manual reclaim (previous 72h replaced), then creator intends Reserve transfer but real-money forfeiture BLOCKED for safety/legal review. Recovery destination R must be FRESH/no prior financial transfers, stay RECOVERY_RESERVED with normal send/receive disabled until a successful recovery; R then succeeds S as ACTIVE, S becomes DEAD. Historic ledger is linked, not rewritten, and BlackBox copy requires preexisting encrypted backup. Network-final LOCK as new receiver 24h clock anchor remains proposed. Source-BlackBox lost/DEAD and late K_S are unresolved. See [LATEST canonical owner decisions](SECURE_P2P_V3_RECOVERY_DECISIONS.md). Historical contradictory older rules below are superseded.

**Date:** 2026-10-25 Australia/Sydney. **Status:** User-confirmed product change; engineering remains an UNTESTED DESIGN, not code, launched network or security proof.
**Authority:** Latest owner instructions override conflicting historical 3-hour Trigger, automatic 3-hour refund, and earlier payment-claim finality texts. No owner-authorised Instant Pay.

## Confirmed user requirements
1. TongNet is designed for fast **manual, bilateral, secure P2P**, generally coordinated over independent external WhatsApp, voice calls or another third-party communication service.
2. **REMOVE** the extra 3-hour Trigger stage and its timeout refund. Sender's subsequent manual **FINAL ACCEPT** of Receiver Claim Request replaces that separate Trigger. There is no pre-Claim Trigger step in the new payment lifecycle.
3. Sender enters intended receiver wallet address and initiates a network-finalised **LOCK** of amount/asset into transaction-specific escrow, without paying Receiver yet. Sender's separate secured BlackBox originates high-entropy one-use **Receiver Claim Code K_R** for (chain ID, transaction ID, exact receiver wallet public key, amount, asset, receiver phase, expiry).
4. Sender explicitly shares K_R out of band via WhatsApp, call or equivalent. The network and receiver wallet do NOT automatically get the plaintext code just because Sender entered an address.
5. ONLY the cryptographically bound receiver wallet can sign **CLAIM_REQUEST**, proving wallet authority and knowledge of K_R. This is a request, **not** a final payout.
6. That authenticated request arrives securely in **Sender BlackBox**. Sender reads the FULL bound receiver wallet/address, amount/asset, transaction ID, request ID, and manually signs **FINAL_ACCEPT** for those exact immutable details. Final network settlement requires all of: valid K_R evidence, exact receiver wallet signature, Sender BlackBox final signature, valid receiver deadline, unique single-spend, BFT finality. **No authentic Sender ACCEPT = no receiver payout.**
7. No extra manual **Reject** button is needed. Sender may withhold approval; unless network-final ACCEPT occurs before the receiver window's adjusted expiry, no payout to receiver. Not accepting is not an immediate refund; Sender can manually reclaim after Receiver right expires.
8. Preserve previous **receiver priority 24h** followed by **sender reclaim 72h**, subject to verifiable network-caused delay credit (one-to-one, without double counting). Receiver K_R expires at adjusted receiver deadline. If unresolved/unclaimed, a DISTINCT **NEW one-use Sender Claim Key K_S is generated inside the SENDER BlackBox** only after receiver expiry, exclusively for original Sender reclaim over following 72h. Sender reclaim needs original wallet authority plus K_S; expires at its adjusted deadline. No automatic refund immediately at 24h.
9. Distinguish ordinary transaction keys K_R/K_S from optional **Disaster Recovery Key**, which originates in accepted Recovery DESTINATION Wallet BlackBox; do not change that separate confirmed rule.
10. The previous after-24+72h irreversible transfer to network reserve remains a controversial **creator proposal**, not authorised for real-money deployment until legal/consumer risk resolved.

## Network state machine (candidate formalization)
```text
INITIATE -> FINAL_LOCK(t0) -> RECEIVER_WINDOW
SENDER_GENERATE_AND_EXTERNALLY_SHARE(K_R)
RECEIVER_CLAIM_REQUEST(K_R proof + exact addressed-wallet signature)
SENDER_BLACKBOX_FINAL_ACCEPT(exact request ID, wallet, value, expiry)
  -> BFT finality strictly before adjusted receiver cutoff -> RECEIVER_PAID_FINAL
OR no final ACCEPT/Claim by adjusted receiver cutoff:
  -> RECEIVER_CODE_EXPIRED
  -> SENDER_RECOVERY_WINDOW (next 72h), CREATE_NEW_SENDER_KEY_K_S_IN_SENDER_BLACKBOX
  -> authenticated original sender claims using K_S
  -> SENDER_RECLAIMED_FINAL
OR 72h sender expiry -> UNRESOLVED_ESCROW_RIGHTS (reserve-forfeiture policy BLOCKED)
```

**CLOCK PROPOSAL — not yet separately owner ratified:** Now that Trigger no longer exists, start the nominal 24h receiver window **at BFT-final LOCK t0**, never when local device queues, sends an external message or opens BlackBox; start the subsequent 72h sender window when receiver's *adjusted* priority ends. Both parties may complete immediately while online; 24h is a MAXIMUM, not a mandatory delay. Require consensus-level strict finality before adjusted deadline, not button click/queued receipt.

## Why this helps mistakes / fraud, and remaining risks
- If Sender intends A but types wallet B, then gives K_R to A, A lacks B signing key; B holds B key but lacks K_R. Even B plus intercepted K_R cannot finish without authentic Sender BlackBox FINAL_ACCEPT.
- The Sender BlackBox displays the bound wallet B before approval, offering last-minute identification of misaddressing. If no final approval, after receiver deadline Sender may reclaim with K_S if eligible.
- **NOT 100% fraud-proof:** Sender can be socially engineered into approving B; a compromised or coerced sender signer can approve; external WhatsApp/call identity can be spoofed; secret intercepted; valid B claim finality irreversible. Cryptography validates key control/explicit signatures, NOT the human identity or correctness of the business deal.
- **Receiver fairness issue:** Sender can simply withhold FINAL_ACCEPT until expiry, even after receiver has delivered goods. The system is bilateral-consent escrow, not automatic buyer/seller protection. No goods/services delivery should be treated as paid until final confirmation.
- Safe anti-phishing display, independently authenticated BlackBox signature, transaction-bound commitments, replay-nullifiers, long Claim Code / QR, signed receiver proofs, encrypted resilient request delivery, BFT atomic state transitions, secure fee/anti-spam budgets and adversarial tests are still NOT implemented.

## Known clashes with historical Disaster Recovery
- Old Q7 handled 3-hour untriggered refund to prebound Recovery Wallet after source DEAD. **OBSOLETE** when 3h Trigger removed. A replacement policy for permanently DEAD source with pending INITIATE/LOCK is OPEN; do not automatically refund or send to reserve in new protocol.
- Old Q6 assumed pre-existing Sender Claim Key could be presented from linked Recovery Wallet after Source DEAD. New user rule literally generates K_S in source Sender BlackBox only when receiver 24h ends. If source BlackBox lost/DEAD before then, how to produce/prove K_S remains an **unresolved conflict**, not silently fixed. Precommit/seal alternative would need explicit owner approval, and must not allow premature claim.
- Formal proofs needed: no double-settlement between late sender acceptance/receiver cutoff/sender reclaim; no fake approvals, robust replay protection and consensus timestamp/partition rules; no indefinite funds loss.

**This document defines product intentions, not a security guarantee.** User may refine the suggested new receiver clock anchor and emergency recovery cases.

**Attribution:** ParmTech, creator/developer Manjinder Singh; 2015 origin is creator-stated and public 2026 disclosure is creator-stated, not independently verified.
