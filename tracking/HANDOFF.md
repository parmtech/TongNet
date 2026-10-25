# RESUME HERE — TongNet Handoff

**Last verified session:** 2026-10-26, Australia/Sydney.  
**Repo:** https://github.com/parmtech/TongNet (private)  
**Default branch:** main  
**Current mode:** TN-SPEC-001 PR #49 and TN-ARC-001 PR #51 are draft proposals; no blockchain runtime or Rust tests.  
**Do NOT claim a working blockchain.**

## Immediate next step for any new human/AI worker
0. Review [TN-ARC-001 draft PR #51](https://github.com/parmtech/TongNet/pull/51), branch `work/TN-ARC-001-payout-transitions`, candidate commit `5c130b951c36af82e87710291f53c841cef9aea4`, stacked on TN-SPEC-001 [PR #49](https://github.com/parmtech/TongNet/pull/49). The candidate boundary rule is not owner-ratified. On PR #49, CI run `40163434903` and two checks on head `602088ca691ad16278e0d2a7117057a4446dd70c` failed before runner startup because GitHub reported failed recent payments or a spending-limit issue; no code checks ran. PR #49 has no reviews yet. Keep both issues open and do not allow real-value movement. After PR #49 merges, retarget PR #51 to `main`.
1. Read `AGENTS.md`, `tracking/TASKS.md`, `tracking/RISKS.md`, `docs/DECISION_REGISTER_CURRENT.md`, `docs/LONG_HORIZON_RISK_AUDIT.md`, `docs/LONG_HORIZON_AUDIT_SUPPLEMENT.md` and `docs/BUILD_EXECUTION_PLAN.md`.
2. **Canonical task set:** [24 structured TN-ID issues #24–#47](https://github.com/parmtech/TongNet/issues) plus [#3 = TN-SEC-004 original S private-key-loss critical blocker](https://github.com/parmtech/TongNet/issues/3). The remaining 22 older #1–#23 issues were CLOSED AS DUPLICATES, NOT completed. Do not work or close them as built features.
3. Earliest independent unblocked work: [TN-ARC-001 #25](https://github.com/parmtech/TongNet/issues/25), [TN-SPEC-001 #29](https://github.com/parmtech/TongNet/issues/29), [TN-MONEY-001 #34](https://github.com/parmtech/TongNet/issues/34), [TN-ENG-001 #35](https://github.com/parmtech/TongNet/issues/35). Root-key recovery [TN-SEC-004 #3](https://github.com/parmtech/TongNet/issues/3) needs OWNER DECISION; no silent signer bypass.
4. Project-control issue [TN-GOV-001 #24](https://github.com/parmtech/TongNet/issues/24) remains IN_REVIEW until one actual successful [status-sync](https://github.com/parmtech/TongNet/actions/workflows/status-sync.yml) run and valid status commit are VERIFIED. Files committed ≠ workflow successfully executed.
5. For each session use a per-issue branch, actual tests, issue update and append factual `tracking/DAILY_LOG.md`. Update this handoff BEFORE stopping: issue, branch, SHA, tests, next exact task, blockers.
6. Do not launch money/claim complete chain from docs. Latest owner rules: native TONG only; BlackBox Sender FINAL_ACCEPT, Receiver 24h then Sender next 60d, both recovery wallets ACTIVE, sealed S-parent archive, no S→C cascade when B dies. Read Active R V4.

## What is done / not done (2026-10-25)
- **Draft proposal:** TN-SPEC-001 #29 has test-only accounting categories, invariants, operation envelope, escrow eligibility model, deterministic-state requirements and a bounded test matrix in PR #49. This does not resolve timer boundaries, production crypto/encoding, post-window rights, or recovery security.
- **Done (documents):** V1.1 master whitepaper, 50 + 15 long-horizon conceptual risks, detailed G0–G11 plan, canonical issue tracker, issue-migration, GitHub worker instructions, two GitHub workflows committed (one checks, one status-sync).
- **Not verified:** Actual passing workflow run, independent crypto review, blockchain code, tests, full nodes, any mined/minted TONG or mainnet. No code-execution success claim.
- **Last branch/commit to resume:** Re-read live HEAD in GitHub; this static file avoids inventing a SHA because concurrent workers created commits. GitHub Issues and PRs are authoritative.
