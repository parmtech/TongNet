# RESUME HERE — TongNet Handoff

**Last verified session:** 2026-10-25, Australia/Sydney.  
**Repo:** https://github.com/manbir6-ux/TongNet (private at setup)  
**Default branch:** main  
**Current mode:** planning and GitHub task-control setup; no actual blockchain build/test run.  
**Do NOT claim a working blockchain.**

## Immediate next step for any new human/AI worker
1. Pull latest main; read `AGENTS.md`, `tracking/CURRENT_STATUS.md`, `tracking/TASKS.md`, `tracking/RISKS.md`, `tracking/DECISIONS.md`, and `docs/A_TO_Z_LONG_TERM_REVIEW_V2.md`.
2. Read GitHub Issues [#1](https://github.com/manbir6-ux/TongNet/issues/1) (canonical spec), [#2](https://github.com/manbir6-ux/TongNet/issues/2) (formal invariants), [#3](https://github.com/manbir6-ux/TongNet/issues/3) (lost original private-key paradox), and [#23](https://github.com/manbir6-ux/TongNet/issues/23) (tracking system). Select earliest unblocked.
3. Begin a feature branch and narrow PR; do not duplicate unfinished work. Record actual branch, HEAD SHA, files and test commands in daily journal before session ends.
4. Owner-confirmed rules: native TONG-only chain; no 3h Trigger; Sender final BlackBox approval; Receiver 24h then Sender 60d; ACTIVE independent R with sealed S BlackBox copy; R DEAD auto-unbind A, **never** forward automatically to C. Prior fresh-at-binding R restriction preserved pending owner clarification.
5. Development candidate: Rust deterministic ledger; version-pinned reviewed BFT; voluntary bonded PoS; optional non-voting PoTP; Fee+Earn. **Mainnet token issuance, delegation, fee split, stake amount, validator counts and claim-key changes not ratified final rules.**
6. RED unresolved: lost key recovery, cryptographically sealed parent archive, late K_S, objective delay credit, reserve forfeiture legality, genesis-stake concentration and source staked bond successor. STOP before real funds.

## Important: continuity after weeks/months
**GitHub Issues define current task truth.** `tracking/AUTO_STATUS.md` when generated contains last verified snapshot; `tracking/DAILY_LOG.md` contains worker-by-worker factual notes. The next worker must cross-check GitHub main branch and current PR status, not copy old percent complete. If this handoff is stale, the *worker who resumes* must update it as their first documentation commit.

## Active assignment (as of this initial handoff)
- Owner instructed A-to-Z audit + persistent tracking; no dedicated implementation task in progress.
- Next recommended technical assignment: TN-001 (spec priority), TN-002 (invariants), followed by TN-013 (Rust workspace only after spec direction).
- Risk of outdated docs: V1.0 and earlier V2/V3 payment/frozen-recovery text still exists historically; use latest owner rules and V1.1 plus security audit as overrides.
- Never store API tokens, private keys or claim codes in the repository.
