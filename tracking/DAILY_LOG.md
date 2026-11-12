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

## 2026-11-12 — TN-GOV-001 tracking integrity repair (Australia/Sydney)

**Branch:** `work/TN-GOV-001-tracking-integrity-20261112`, based on main `886329931341c4faa1d5fdb59c90493d9ff9fe38`. The existing structural checker failed locally: it required two deleted/renamed files and parsed only obsolete task IDs and the previous owner URL. The workflow also syntax-checked a missing script, and status-sync's repository guard still named the previous owner. This draft checks the current 25 canonical rows and current files, tests duplicate/missing/mismatched rows, updates the workflow syntax target and updates the guard to the current repository.

**Validation:** `python -m unittest discover -s tests -p test_tracking_integrity.py -v` — four tests passed; `python scripts/check_tracking.py` — passed; `python -m py_compile scripts/check_tracking.py .github/scripts/build_status.py` — passed; staged whitespace check — passed. These are local structural checks only, not live issue status, successful Actions execution, or blockchain/security evidence. No hosted workflow was run.

**Review and effects:** If merged, the existing scheduled/issue-triggered status-sync job can run in the current repository and may write its existing status snapshots to main, subject to GitHub permissions and branch protections. Review that behavior and its permissions before merge. Mainnet, protocol, ownership, money and cryptographic decisions are unchanged. Next: review this draft and authorize an actual workflow run; verify its exact-head result and snapshot behavior. TN-GOV-001 remains open until its required evidence exists.

Follow-up: added exact stable-ID-to-issue mapping checks so swapped IDs cannot pass with the same issue-number set. Five structural regression tests and the tracking checker passed locally after this refinement; hosted CI remains unverified.
