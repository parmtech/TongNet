# TongNet owner blueprint discussion — 2026-10-25

Related issue: [TN-ARC-001 #25](https://github.com/manbir6-ux/TongNet/issues/25).

## Scope and authorization
The owner wants the complete build blueprint, independently of launch, and requests one question at a time after checking existing GitHub decisions. The owner explicitly authorized saving this discussion to GitHub and updating it as answers arrive. This record preserves discussion; it does not claim all blueprint gaps are resolved.

## Timer discussion in order
1. Assistant proposed starting the receiver 24-hour timer at finalized LOCK. Owner instead said: “जदों receiver claim करे, उस टाइम तो start होने चाहीदे” and “ते नाल ही टाइम शुरू होजेगा”.
2. Asked when sender could reclaim if receiver never claims, owner answered “24 घंटे दे बाद”. The start event was not established by that answer.
3. Owner subsequently corrected the interpretation: “जदों transaction receiver वल्लों पे जी गई request accept करलूगा sender उधों ही शुरू होऊ”. Latest stated trigger: sender acceptance of the request sent by receiver, rather than LOCK or receiver request alone.
4. Owner asked to check GitHub first because this flow had already been discussed. GitHub confirms receiver CLAIM_REQUEST and mandatory Sender BlackBox FINAL_ACCEPT already exist. The current decision register still lists the exact timer anchor as unresolved.

## Interpretation still pending
Which acceptance event the owner means must be reconciled with existing FINAL_ACCEPT settlement semantics. Do not assume a new 24-hour delay after settlement, automatically refund funds, or replace the existing following 60-day manual sender reclaim window. Earlier assistant interpretations are provisional and superseded by the latest correction. Ask one concrete step question only after comparing existing records. Network-final timing and cutoff details have not yet been ratified.

## Next step
Show the existing request/accept/settlement steps to the owner, identify the intended timer event, then prepare a specific ADR and canonical decision-register update. Keep #25 open; no code, tests, merge, or complete-blueprint claim follows from this intake.


## Owner clarification — no receiver action after sender acceptance
Owner stated: “Receiver ने बस अपना code claim request करनी है। उस तो बाद जे तो sender उनो accept कर लेगा, then... कुछ नहीं करना फिर”. Confirmed user flow: receiver submits a code-backed claim request; sender accepts it; receiver has no further manual action. This reinforces the existing CLAIM_REQUEST -> Sender FINAL_ACCEPT flow. It does not separately establish a post-acceptance 24-hour hold or resolve the purpose/start of the disputed timer. Do not introduce another receiver claim step.
Next single question: if sender acceptance completes the payment flow, what is the 24-hour window intended to allow or limit? Establish its purpose before proposing another anchor.


## 2026-10-25 — Owner confirms acceptance completes payment/window
In response to the explicit question whether sender acceptance sends funds to the receiver and ends the transaction's 24-hour window, the owner said: “बिल्कुल, बिल्कुल यही समझो तुसी की फिर पैसे चले जाणे ऐ receiver नू”. This confirms sender acceptance completes the receiver payment flow and ends the applicable window; there is no additional receiver action or deliberate post-acceptance 24-hour waiting period. Ledger settlement still requires valid transaction execution and network finality; a local button click alone is not proof of payout. Settled escrow cannot subsequently be reclaimed.
The window START remains unresolved: earlier voice wording placed start at acceptance, which now also ends payment/window. Preserve the latest completion clarification, but do not invent a start anchor. Next single question: does the 24-hour countdown begin when receiver submits the code-backed claim request, giving sender that period to accept? This is a question, not an approved rule. Existing following 60-day reclaim policy is not changed here.
Documentation intake on draft PR #50 for issue #25; no implementation or runtime test result claimed.


## 2026-10-25 — Explicit owner override: automatic return if sender does not accept
Owner stated: “जे sender request नू accept ना करे तां 24 घंटे बाद sender दे कोल पैसे वापस आ जाणगे”, in response to the choice between automatic return and remaining pending.
Confirmed product decision: if sender does not accept the receiver request within the applicable 24-hour window, the locked payment amount returns automatically to sender. No separate manual reclaim is required for this specific timeout. This latest explicit decision supersedes the previous no-auto-refund / following 60-day manual reclaim rule for this scenario. Do not extend the override to unrelated recovery or other escrow cases. Fee treatment has not been selected.
Still unresolved: exact start event for these 24 hours (the owner answered timeout behavior, not the preceding start-event question), deterministic cutoff/finality and outage handling. Do not infer the start from the assistant's compound question. Before implementation, update the canonical register through an ADR, reconcile settlement-versus-timeout ordering and test exactly-once payout/refund. No code or runtime test claim.
Next single owner question: do these 24 hours start when receiver submits the code-backed claim request?


## 2026-10-25 — Owner correction withdraws automatic-refund interpretation
Owner explicitly corrected: “sender नू पैसे नहीं जाणगे, sender नू पैसे नहीं जाणगे” and described a claim opportunity after 24 hours (remaining transcript wording ambiguous).
The immediately preceding automatic-return entry and assistant's asserted removal of the 60-day manual reclaim rule are SUPERSEDED; do not implement automatic return or treat the 60-day rule as revoked on that basis. Confirmed correction: no automatic payment back to sender at the 24-hour cutoff. Exact post-cutoff claim eligibility must be clarified with one question. Proposed interpretation to ask, not an approved new decision: does sender gain a manual reclaim opportunity after receiver window expires? Existing canonical manual reclaim policy remains the baseline pending explicit clarification. The timer start is also still unresolved. No implementation changes.


## 2026-10-25 — Owner confirms manual sender reclaim after receiver window
Asked explicitly whether the receiver window closes after 24 hours and sender then gains the option to claim their own funds manually, owner answered “बिलकुल” (yes, exactly).
Confirmed: receiver eligibility ends at the applicable 24-hour cutoff; sender manual reclaim becomes available. Funds do not automatically return. This reconfirms the existing manual reclaim policy, superseding the erroneous automatic-refund interpretation above. No change to the existing following 60-day duration was authorized by this answer. A successful finalized receiver payout consumes escrow and leaves nothing to reclaim. Exact timer START and cutoff/finality rules remain unresolved. Next question must address the start without conflating it with completed payment: does the receiver's 24-hour window start when the funded transaction becomes network-final LOCK?
Documentation only; canonical ADR consolidation remains pending and no runtime tests were run.


## 2026-10-25 — Latest owner decision: 24-hour window starts at transaction initiation
Owner explicitly clarified: “actual च 24 घंटे कुल शुरू हुंदे है जदों transaction initiate हुंदी ऐ”. Product timer starts at transaction INITIATE, not at receiver CLAIM_REQUEST or sender FINAL_ACCEPT. This latest explicit clarification supersedes the earlier ambiguous trigger statements in this intake.
Consolidated confirmed product flow: transaction initiation starts the nominal 24-hour receiver window; receiver submits code-backed claim request; sender acceptance completes receiver payment subject to valid network finality and ends that escrow; absent successful settlement by the cutoff, receiver window closes and sender gains manual reclaim eligibility, with no automatic refund. The existing following 60-day manual reclaim duration remains unchanged.
Engineering detail still to specify: authoritative initiation means a consensus-recorded INITIATE/LOCK event versus a local submission click; owner did not explicitly choose that technical distinction here. Do not base consensus state on device clock or claim exact boundary/outage policy is resolved. Canonical ADR consolidation and cutoff/replay/race tests remain pending.
Next design topic: safe preservation of sender reclaim credential if original BlackBox is lost before the 24-hour cutoff. Any pre-generation/sealed activation changes the earlier literal after-expiry generation rule and needs explicit owner approval.


## 2026-10-25 — Owner direction: reclaim credential reaches recovery wallet after source death
Owner stated the key should go to the recovery wallet when the original wallet becomes DEAD, and nobody has access to the DEAD wallet; they also described the DEAD wallet's remaining work continuing.
Record as product intent: following valid authorized source-to-recovery disaster, the transaction-bound sender reclaim capability must be available in the designated recovery wallet without reopening user access to the DEAD source. Do not interpret remaining work as permission for the DEAD source to sign new transactions, resurrect, disclose all secrets, or bypass receiver priority. Deterministic network processing of existing obligations and successor-authorized claims are distinct from user operation of a DEAD wallet.
Engineering remains unresolved: a destroyed BlackBox cannot generate or transmit a future secret. Specify independently recoverable derivation or sealed precommit and conditional delivery, exact successor authorization, 24-hour eligibility and single consumption; do not claim mere key migration solves generation. Owner has stated the desired destination, not explicitly approved a cryptographic method or early key generation. Next single clarification: does 'DEAD wallet continues work' mean the network completes existing timed obligations while only recovery wallet can authorize eligible new claims?
