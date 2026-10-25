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
