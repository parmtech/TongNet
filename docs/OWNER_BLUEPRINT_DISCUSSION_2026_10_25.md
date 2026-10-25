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
