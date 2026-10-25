# RESUME HERE — TongNet Handoff

**Last verified session:** 2026-10-25, Australia/Sydney.  
**Repo:** https://github.com/manbir6-ux/TongNet (private at setup)  
**Default branch:** main  
**Current mode:** planning and GitHub task-control setup; no actual blockchain build/test run.  
**Do NOT claim a working blockchain.**

## Immediate next step for any new human/AI worker
1. Read `AGENTS.md`, `tracking/TASKS.md`, `tracking/RISKS.md`, `docs/DECISION_REGISTER_CURRENT.md`, `docs/LONG_HORIZON_RISK_AUDIT.md`, `docs/LONG_HORIZON_AUDIT_SUPPLEMENT.md` and `docs/BUILD_EXECUTION_PLAN.md`.
2. **Canonical task set:** [24 structured TN-ID issues #24–#47](https://github.com/manbir6-ux/TongNet/issues) plus [#3 = TN-SEC-004 original S private-key-loss critical blocker](https://github.com/manbir6-ux/TongNet/issues/3). The remaining 22 older #1–#23 issues were CLOSED AS DUPLICATES, NOT completed. Do not work or close them as built features.
3. Earliest independent unblocked work: [TN-ARC-001 #25](https://github.com/manbir6-ux/TongNet/issues/25), [TN-SPEC-001 #29](https://github.com/manbir6-ux/TongNet/issues/29), [TN-MONEY-001 #34](https://github.com/manbir6-ux/TongNet/issues/34), [TN-ENG-001 #35](https://github.com/manbir6-ux/TongNet/issues/35). Root-key recovery [TN-SEC-004 #3](https://github.com/manbir6-ux/TongNet/issues/3) needs OWNER DECISION; no silent signer bypass.
4. Project-control issue [TN-GOV-001 #24](https://github.com/manbir6-ux/TongNet/issues/24) remains IN_REVIEW until one actual successful [status-sync](https://github.com/manbir6-ux/TongNet/actions/workflows/status-sync.yml) run and valid status commit are VERIFIED. Files committed ≠ workflow successfully executed.
5. For each session use a per-issue branch, actual tests, issue update and append factual `tracking/DAILY_LOG.md`. Update this handoff BEFORE stopping: issue, branch, SHA, tests, next exact task, blockers.
6. Do not launch money/claim complete chain from docs. Latest owner rules: native TONG only; BlackBox Sender FINAL_ACCEPT, Receiver 24h then Sender next 60d, both recovery wallets ACTIVE, sealed S-parent archive, no S→C cascade when B dies. Read Active R V4.

## What is done / not done (2026-10-25)
- **Done (documents):** V1.1 master whitepaper, 50 + 15 long-horizon conceptual risks, detailed G0–G11 plan, canonical issue tracker, issue-migration, GitHub worker instructions, two GitHub workflows committed (one checks, one status-sync).
- **Not verified:** Actual passing workflow run, independent crypto review, blockchain code, tests, full nodes, any mined/minted TONG or mainnet. No code-execution success claim.
- **Last branch/commit to resume:** Re-read live HEAD in GitHub; this static file avoids inventing a SHA because concurrent workers created commits. GitHub Issues and PRs are authoritative.


## 2026-10-25 — Owner blueprint intake
Issue: TN-ARC-001 #25. Branch: `work/TN-ARC-001-owner-blueprint-intake`. Discussion commit: `cdd41e39accb6ea541e20b6cb3a002014e09e9de`.
Saved `docs/OWNER_BLUEPRINT_DISCUSSION_2026_10_25.md` with the owner's timer corrections, request for one question at a time, and authorization for ongoing GitHub saves. Documentation intake only; no code or runtime tests. Canonical timer remains unresolved: latest owner wording starts time when sender accepts receiver request; reconcile with existing FINAL_ACCEPT settlement before ADR or implementation. Do not overwrite earlier rules from ambiguous transcript. Next: read the intake and existing manual P2P flow, identify exact event with owner, then draft ADR/canonical updates. Existing implementation PRs #48/#49 are separate; no completion or merge claimed.


## 2026-10-25 — Owner confirms acceptance completes payment/window
In response to the explicit question whether sender acceptance sends funds to the receiver and ends the transaction's 24-hour window, the owner said: “बिल्कुल, बिल्कुल यही समझो तुसी की फिर पैसे चले जाणे ऐ receiver नू”. This confirms sender acceptance completes the receiver payment flow and ends the applicable window; there is no additional receiver action or deliberate post-acceptance 24-hour waiting period. Ledger settlement still requires valid transaction execution and network finality; a local button click alone is not proof of payout. Settled escrow cannot subsequently be reclaimed.
The window START remains unresolved: earlier voice wording placed start at acceptance, which now also ends payment/window. Preserve the latest completion clarification, but do not invent a start anchor. Next single question: does the 24-hour countdown begin when receiver submits the code-backed claim request, giving sender that period to accept? This is a question, not an approved rule. Existing following 60-day reclaim policy is not changed here.
Documentation intake on draft PR #50 for issue #25; no implementation or runtime test result claimed.
