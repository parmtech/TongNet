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
**Completed acceptance criteria (with PR/evidence):** Added categories, checked integer/conservation model, chain/protocol/signer/nonce/role/action/payload/validity authorization binding, typed finite envelope (including `TRANSFER`), replay and atomicity invariants, deterministic finalized-state/root requirements, and bounded property-test matrix. Draft [PR #49](https://github.com/parmtech/TongNet/pull/49); issue #29 remains OPEN.  
**Remaining blockers and exact next action:** Owner/architect review and explicit decisions are needed before ratification; subsequent implementation/tests still required. Review PR #49 and address review feedback on the same issue branch.  
**Updated HANDOFF/CURRENT_STATUS:** yes.

## 2026-10-26 — TN-SPEC-001 review and CI status (Australia/Sydney)
**Worker/owner:** Codex; issue remains assigned to `parmtech`.  
**Issue / branch / commit:** #29 / `work/TN-SPEC-001-ledger-invariants` / PR head `bba95c659a695cc2368ebc74544887f592ceed3a`; [draft PR #49](https://github.com/parmtech/TongNet/pull/49).  
**Changed files:** `tracking/HANDOFF.md`, `tracking/CURRENT_STATUS.md`, `tracking/DAILY_LOG.md`; GitHub PR #49 and issue #29 status/evidence text.  
**Test command and actual PASS/FAIL results:** No code tests run this session. PR review submissions and inline review threads: none. GitHub Actions run `40163434903` (`integrity`) failed before runner startup; annotation says recent payments failed or account spending limit needs increasing. This is an account billing block, not a code test failure.  
**New risk / decision / owner approval:** GitHub repository was renamed/transferred from `manbir6-ux/TongNet` to canonical `parmtech/TongNet`; old URL returns a redirect. No protocol decision or approval added.  
**Completed acceptance criteria (with PR/evidence):** Rechecked PR head, issue assignment/state, reviews, and CI diagnostics; updated PR body and issue #29 to IN_PROGRESS with exact billing blocker. PR remains draft and issue remains open.  
**Remaining blockers and exact next action:** Owner/architect review is pending. Restore GitHub Actions billing/spending-limit eligibility before expecting runner results; then re-check PR #49 on its current head and address any substantive review feedback.  
**Updated HANDOFF/CURRENT_STATUS:** yes.

## 2026-10-26 — TN-ARC-001 candidate payout boundaries (Australia/Sydney)
**Worker/owner:** Codex; issue #25 assigned to `parmtech`.  
**Issue / branch / commit:** #25 / `work/TN-ARC-001-payout-transitions` / candidate commit `5c130b951c36af82e87710291f53c841cef9aea4`; draft PR #51 stacked on #29 PR #49.  
**Changed files:** `docs/PAYOUT_TRANSITION_TABLE_V0_1.md`, `docs/ledger/payout-transition-candidate.v0.1.json`; tracking updates in this stacked branch.  
**Test command and actual PASS/FAIL results:** Machine-readable JSON parsed in the local JS runtime — PASS; 24h + 60d arithmetic check (`5,270,400` seconds from t0) — PASS. Documentation only; no Rust tests. PR #49 CI diagnostics on head `602088ca691ad16278e0d2a7117057a4446dd70c`: two `integrity` checks failed before runner startup due failed account payments/spending limit; no code ran.  
**New risk / decision / owner approval:** Candidate uses BFT-final LOCK as t0 and treats pending claims as expired for Receiver priority at t0+24h; both require owner ratification. Consensus time, Sender K_S loss, post-window rights, and open escrow under Sender DEAD remain unresolved. No real-value movement authorized.  
**Completed acceptance criteria (with PR/evidence):** Draft table and JSON define candidate inclusive/exclusive intervals, verified BFT-final evidence fields, deterministic conflict ordering, one-winner payouts, and cutoff/property cases. [PR #51](https://github.com/parmtech/TongNet/pull/51); issue #25 remains OPEN.  
**Remaining blockers and exact next action:** Owner must ratify or revise t0, cutoff behavior, and consensus-time assumptions. Keep PR #51 draft and stacked until PR #49 is merged; then retarget to main and address review. Resolve GitHub Actions billing eligibility before expecting runner validation.  
**Updated HANDOFF/CURRENT_STATUS:** yes.
