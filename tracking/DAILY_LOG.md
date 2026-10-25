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

## 2026-10-25 — TN-SPEC-001 test-only ledger proposal (Australia/Sydney)
**Worker/owner:** Codex; issue assigned to `manbir6-ux`.  
**Issue / branch / commit:** #29 / `work/TN-SPEC-001-ledger-invariants` / `4ba70965503992ec23cbd1d3f084f19478821b4a`; draft PR #49.  
**Changed files:** `docs/LEDGER_STATE_MODEL_V0_1.md`, `docs/ledger/ledger-state-model.v0.1.json`, `docs/ledger/transaction-envelope.v0.1.schema.json`.  
**Test command and actual PASS/FAIL results:** Local Node JSON parse — PASS for both JSON files; local structural consistency check for operation enum vs `oneOf`, payload references and required object keys — PASS (8 operation arms); `git diff --check` — PASS, no output. No Rust tests or full Draft 2020-12 validator were run. GitHub combined status returned no status entries at check time.  
**New risk / decision / owner approval:** Proposal only; no owner financial-right decision added. Timer origin/cutoffs, production encoding/crypto, rejected-transaction fee/nonce behavior, post-60-day outcome and recovery money effects remain unresolved.  
**Completed acceptance criteria (with PR/evidence):** Added categories, checked integer/conservation model, chain/protocol/signer/nonce/role/action/payload/validity authorization binding, typed finite envelope (including `TRANSFER`), replay and atomicity invariants, deterministic finalized-state/root requirements, and bounded property-test matrix. Draft [PR #49](https://github.com/manbir6-ux/TongNet/pull/49); issue #29 remains OPEN.  
**Remaining blockers and exact next action:** Owner/architect review and explicit decisions are needed before ratification; subsequent implementation/tests still required. Review PR #49 and address review feedback on the same issue branch.  
**Updated HANDOFF/CURRENT_STATUS:** yes.
