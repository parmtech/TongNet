# RESUME HERE — TongNet Handoff

**Last verified session:** 2026-10-25, Australia/Sydney.  
**Repo:** https://github.com/manbir6-ux/TongNet (private at setup)  
**Default branch:** main  
**Current mode:** TN-ENG-001 E0 Rust workspace and CI scaffold in progress on `work/TN-ENG-001-rust-workspace`; no financial state machine or blockchain behavior.  
**Do NOT claim a working blockchain.**

## Immediate next step for any new human/AI worker
1. Continue TN-ENG-001 on `work/TN-ENG-001-rust-workspace` and draft PR [TN-ENG-001 Rust workspace and CI](https://github.com/manbir6-ux/TongNet/pull/48). Current GitHub head before the cargo-deny workflow correction is `030fc14a2106db9f54fcf7cb3b43f2039ed3672d`; publish the local follow-up and record its returned head before stopping.
2. Read `AGENTS.md`, `tracking/TASKS.md`, `tracking/RISKS.md`, `docs/DECISION_REGISTER_CURRENT.md`, `docs/LONG_HORIZON_RISK_AUDIT.md`, `docs/LONG_HORIZON_AUDIT_SUPPLEMENT.md` and `docs/BUILD_EXECUTION_PLAN.md`.
3. **Canonical task set:** [24 structured TN-ID issues #24–#47](https://github.com/manbir6-ux/TongNet/issues) plus [#3 = TN-SEC-004 original S private-key-loss critical blocker](https://github.com/manbir6-ux/TongNet/issues/3). The remaining 22 older #1–#23 issues were CLOSED AS DUPLICATES, NOT completed. Do not work or close them as built features.
4. The independent follow-on tasks remain [TN-ARC-001 #25](https://github.com/manbir6-ux/TongNet/issues/25), [TN-SPEC-001 #29](https://github.com/manbir6-ux/TongNet/issues/29), and [TN-MONEY-001 #34](https://github.com/manbir6-ux/TongNet/issues/34). Root-key recovery [TN-SEC-004 #3](https://github.com/manbir6-ux/TongNet/issues/3) needs OWNER DECISION; no silent signer bypass.
5. Project-control issue [TN-GOV-001 #24](https://github.com/manbir6-ux/TongNet/issues/24) remains IN_REVIEW until one actual successful [status-sync](https://github.com/manbir6-ux/TongNet/actions/workflows/status-sync.yml) run and valid status commit are VERIFIED. Files committed ≠ workflow successfully executed.
6. For each session use a per-issue branch, actual tests, issue update and append factual `tracking/DAILY_LOG.md`. Update this handoff BEFORE stopping: issue, branch, SHA, tests, next exact task, blockers.
7. Do not launch money/claim complete chain from docs. Latest owner rules: native TONG only; BlackBox Sender FINAL_ACCEPT, Receiver 24h then Sender next 60d, both recovery wallets ACTIVE, sealed S-parent archive, no S→C cascade when B dies. Read Active R V4.

## What is done / not done (2026-10-25)
- **In progress (code scaffold):** `Cargo.toml` workspace with `ledger-core`, `protocol-types`, `crypto-types`, and `model-tests`; Rust 1.99.1 pin; dependency policy config; Rust CI. No ledger transitions or cryptographic behavior exist.
- **Local checks:** `cargo fmt --all -- --check`, `cargo clippy --workspace --all-targets --locked -- -D warnings`, `cargo metadata --locked --no-deps --format-version 1`, and `cargo deny check` PASS. `cargo test --workspace --all-targets --locked` could not link on this Windows host because Visual Studio C++ Build Tools are absent. GitHub Actions jobs did not start because the account's Actions billing limit blocks runner usage; remote test status remains unverified.
- **Next exact action:** publish the cargo-deny workflow correction to the existing branch and rerun checks after GitHub Actions billing is available. Keep the draft PR and issue open until the automated run and review are complete.
- **Done (documents):** V1.1 master whitepaper, 50 + 15 long-horizon conceptual risks, detailed G0–G11 plan, canonical issue tracker, issue-migration, GitHub worker instructions, two GitHub workflows committed (one checks, one status-sync).
- **Not verified:** Actual passing workflow run, independent crypto review, blockchain code, tests, full nodes, any mined/minted TONG or mainnet. No code-execution success claim.
- **Last branch/commit to resume:** Re-read live HEAD in GitHub; this static file avoids inventing a SHA because concurrent workers created commits. GitHub Issues and PRs are authoritative.
