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

## 2026-10-25 — TN-ENG-001 Rust workspace foundation started (Australia/Sydney)
**Worker:** Codex.  
**Issue / branch / commit:** TN-ENG-001 / `work/TN-ENG-001-rust-workspace` / local scaffold commit `bf00e0ff8a6db3a8b4139a86a8ebf6671315f405`; GitHub branch created from `main`, code publication still pending.  
**Changed files:** Added a four-crate Cargo workspace (`ledger-core`, `protocol-types`, `crypto-types`, `model-tests`), Rust 1.99.1 toolchain pin, lockfile, dependency-policy config, Rust CI workflow, scaffold notes, and E0 status update. No transaction, monetary, or cryptographic logic was added.  
**Test command and actual PASS/FAIL results:** `cargo fmt --all -- --check` PASS after applying formatting; `cargo clippy --workspace --all-targets --locked -- -D warnings` PASS; `cargo metadata --locked --no-deps --format-version 1` PASS; `cargo test --workspace --all-targets --locked` FAIL on this Windows host because Visual Studio C++ linker/build tools are absent. Linux GitHub Actions and cargo-deny have not run yet.  
**New risk / decision / owner approval:** No financial-right decision changed. Local Git CLI authentication has no selected Git Credential Manager provider; the GitHub connector is being used for publication.  
**Completed acceptance criteria (with PR/evidence):** Local workspace parses, formats and passes Clippy. No PR or green remote run yet; issue remains open.  
**Remaining blockers and exact next action:** Publish the scaffold commit to `work/TN-ENG-001-rust-workspace`, open a draft PR, then inspect the Rust CI run.  
**Updated HANDOFF/CURRENT_STATUS:** yes.

## 2026-10-25 — TN-ENG-001 CI and dependency-check follow-up (Australia/Sydney)
**Worker:** Codex.  
**Issue / branch / commit:** TN-ENG-001 / `work/TN-ENG-001-rust-workspace` / draft PR [TN-ENG-001 Rust workspace and CI](https://github.com/manbir6-ux/TongNet/pull/48); GitHub head `030fc14a2106db9f54fcf7cb3b43f2039ed3672d` before the follow-up correction is pushed.  
**Changed files:** Refined local workspace dependency versions and `deny.toml`; corrected cargo-deny invocation in Rust CI. No financial behavior was added.  
**Test command and actual PASS/FAIL results:** `cargo fmt --all -- --check`, `cargo clippy --workspace --all-targets --locked -- -D warnings`, `cargo metadata --locked --no-deps --format-version 1`, and `cargo deny check` PASS locally. The local `cargo test --workspace --all-targets --locked` remains unable to link because this Windows host lacks Visual Studio C++ Build Tools.  
**New risk / decision / owner approval:** First remote CI checks were not started because GitHub reports the account's Actions billing limit prevents runner usage. The remote test result is unknown; this is not a code failure. No owner policy changed.  
**Completed acceptance criteria (with PR/evidence):** Workspace and dependency policy pass local checks; draft PR #48 exists. CI has not passed, so TN-ENG-001 remains open.  
**Remaining blockers and exact next action:** Publish the cargo-deny correction to the existing branch and rerun CI after Actions billing is available; keep the PR in draft until a green run and review.  
**Updated HANDOFF/CURRENT_STATUS:** yes.

## 2026-10-25 — TN-ENG-001 scaffold published for review (Australia/Sydney)
**Worker:** Codex.  
**Issue / branch / commit:** TN-ENG-001 / `work/TN-ENG-001-rust-workspace` / draft PR [TN-ENG-001 Rust workspace and CI](https://github.com/manbir6-ux/TongNet/pull/48), current remote head `8bda72c710ee96abd91d17d520b09afbe9ee8342`.  
**Changed files:** Published the workspace and its follow-up dependency-check correction, plus project handoff/status records.  
**Test command and actual PASS/FAIL results:** Formatting, Clippy, Cargo metadata, and `cargo deny check` PASS locally. Local workspace tests cannot link on this Windows host because Visual Studio C++ Build Tools are absent. GitHub Actions for the published head did not start because the account's Actions billing limit blocks runner usage.  
**New risk / decision / owner approval:** No financial rules or owner decisions changed. Remote test result remains unknown.  
**Completed acceptance criteria (with PR/evidence):** Draft PR is published and issue #35 is linked; scaffold structure and dependency policy pass local checks. The issue remains open pending green CI and review.  
**Remaining blockers and exact next action:** Restore GitHub Actions runner availability, then rerun PR checks. Do not close or merge while CI is unverified.  
**Updated HANDOFF/CURRENT_STATUS:** yes.

## 2026-10-25 — TN-ENG-001 continued local verification (Australia/Sydney)
**Worker:** Codex.  
**Issue / branch / commit:** TN-ENG-001 / `work/TN-ENG-001-rust-workspace` / draft PR [TN-ENG-001 Rust workspace and CI](https://github.com/manbir6-ux/TongNet/pull/48).  
**Changed files:** No protocol or workspace code changes; recorded an additional local compile check and current CI blocker.  
**Test command and actual PASS/FAIL results:** `cargo check --workspace --all-targets --locked` PASS. Prior local formatting, Clippy, Cargo metadata, and cargo-deny checks remain PASS. `cargo test` still cannot link locally; GitHub Actions still does not start because of the account billing limit.  
**New risk / decision / owner approval:** No design or owner decision changed. A Linux test environment is unavailable on this machine.  
**Completed acceptance criteria (with PR/evidence):** PR #48 remains open and draft; remote CI is still unverified.  
**Remaining blockers and exact next action:** Restore GitHub Actions runner availability and rerun PR checks; alternatively install a Windows C++ toolchain and rerun `cargo test` locally.  
**Updated HANDOFF/CURRENT_STATUS:** yes.
