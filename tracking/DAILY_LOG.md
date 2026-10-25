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
