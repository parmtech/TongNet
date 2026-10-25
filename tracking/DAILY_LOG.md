# TongNet — Append-Only Daily Work Journal

All workers **append** a factual new session record, with local ISO date, timezone, task ID/issue, implementation or documentation status, actual commit hashes, run commands, result, blocked decisions and the exact next step. Do not replace previous entries. Daily bot snapshots under `auto/` supplement but never replace these human/agent evidence notes.

## 2026-10-25 — Initial long-term project-control setup (Australia/Sydney)
**Worker:** ChatGPT — GitHub connector.  
**Issues:** TN-001–TN-023 task breakdown, TN-023 tracking implementation.  
**Before:** Repository had 30 Markdown docs in root/docs and no GitHub issues from issue search; no executable source tree, CI or validated network was inspected.  
**Work:** Cross-read current whitepaper V1.1, active recovery V4 and secure bilateral P2P; identified critical S-private-key-loss disaster weakness and other long-term deployment risks; opened 23 real GitHub Issues grouped G0–G4; started persistent worker instructions, dependencies, risk register, ADR register and Actions checks.  
**Tests:** Only GitHub file and issue creation/verification and local syntax checks for tracking scripts are claimed when separately recorded. No Rust build or crypto/security audit occurred.  
**Next:** Confirm project-control files and GitHub Actions workflow are valid/accessible; resolve TN-001, TN-002 and TN-003 before coding production recovery.  
**Owner policy:** No mainnet or code/protocol authority was silently granted by documentation.  

### Template for next daily entry
```markdown
## YYYY-MM-DD — Short factual headline (TZ)
**Worker/owner:**
**Issue / branch / commit:**
**Changed files:**
**Test command and actual PASS/FAIL results:**
**New risk / decision / owner approval:**
**Completed acceptance criteria (with PR/evidence):**
**Remaining blockers and exact next action:**
**Updated HANDOFF/CURRENT_STATUS:** yes/no
```


## 2026-10-25 — Owner blueprint intake
Issue: TN-ARC-001 #25. Branch: `work/TN-ARC-001-owner-blueprint-intake`. Discussion commit: `cdd41e39accb6ea541e20b6cb3a002014e09e9de`.
Saved `docs/OWNER_BLUEPRINT_DISCUSSION_2026_10_25.md` with the owner's timer corrections, request for one question at a time, and authorization for ongoing GitHub saves. Documentation intake only; no code or runtime tests. Canonical timer remains unresolved: latest owner wording starts time when sender accepts receiver request; reconcile with existing FINAL_ACCEPT settlement before ADR or implementation. Do not overwrite earlier rules from ambiguous transcript. Next: read the intake and existing manual P2P flow, identify exact event with owner, then draft ADR/canonical updates. Existing implementation PRs #48/#49 are separate; no completion or merge claimed.


## 2026-10-25 — Receiver flow clarification
Owner confirmed receiver only submits code-backed CLAIM_REQUEST and has no further manual step after sender acceptance. Saved exact statement and interpretation in owner blueprint discussion on PR #50. Timer purpose remains unresolved; no new delay or fund right inferred. Documentation only; no runtime tests applicable.


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
