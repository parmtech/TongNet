# TongNet — SINGLE mandatory worker entry point

**Every worker, human or AI, MUST read this before changing repository.** As of 2026-10-25 it contains research/specifications but NO verified functioning blockchain. Owner's most recent explicit rules outrank superseded docs; do not call a PDF production code.

## One source of truth, not two conflicting trackers
- **Live GitHub Issues [25 canonical tasks](https://github.com/manbir6-ux/TongNet/issues)** are the SINGLE source of truth for whether a task is OPEN/CLOSED and whether its acceptance evidence exists.
- **[tracking/TASKS.md](tracking/TASKS.md)** indexes exact issue numbers and stable `[TN-AREA-NNN]` task keys. This supersedes placeholders `TN-AREA-NNN`, `TN-SPEC-001` or `TN-ENG-001` in older pre-Issue draft documents.
- **[tracking/HANDOFF.md](tracking/HANDOFF.md)** immediate next action; **[tracking/CURRENT_STATUS.md](tracking/CURRENT_STATUS.md)** manually confirmed milestone; **[tracking/DAILY_LOG.md](tracking/DAILY_LOG.md)** append-only factual daily worker journal.
- **[docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md)** is the primary issue-derived automated dashboard; **[tracking/AUTO_STATUS.md](tracking/AUTO_STATUS.md)** plus `tracking/auto/YYYY-MM-DD.md` are copies maintained by the **single** scheduled [status-sync](.github/workflows/status-sync.yml) Action when enabled. Until first actual workflow run these mirrors may be missing or stale. `tracking/auto/YYYY-MM-DD.md` append-by-day snapshots. If missing or stale, read live GitHub Issues and git history; **no status bot is a security auditor**.
- **[docs/LONG_HORIZON_RISK_AUDIT.md](docs/LONG_HORIZON_RISK_AUDIT.md)** exhaustive 50-risk forward audit; [supplemental risks](docs/LONG_HORIZON_AUDIT_SUPPLEMENT.md) including missing S signing-key-loss failure; **[tracking/RISKS.md](tracking/RISKS.md)** concise indexed severity and issue links.
- **[docs/BUILD_EXECUTION_PLAN.md](docs/BUILD_EXECUTION_PLAN.md)** detailed G0–G11 engineering release gates; **[tracking/TASKS.md](tracking/TASKS.md)** coarse issue batches labelled G0–G4 for management, **not a contradictory replacement of the 12 release gates**.
- **[tracking/DECISIONS.md](tracking/DECISIONS.md)** current short ADR status; **[docs/DECISION_REGISTER_CURRENT.md](docs/DECISION_REGISTER_CURRENT.md)** existing detailed owner policy index; [V1.1 master whitepaper](docs/WHITEPAPER_MASTER_V1_1_SECURITY_REVIEW.md) and [active Recovery V4](docs/ACTIVE_RECOVERY_MIRROR_V4.md). Significant policy requires an actual `docs/ADR/NNNN-...` proposal with explicit owner's authorization for changes to funds rights.
- **[docs/WORK_LOG.md](docs/WORK_LOG.md)** remains preserved historical session record; **new work should append ONLY to tracking/DAILY_LOG.md** to prevent divergent duplicate logs. Never delete original historical entries.

## Every session workflow (mandatory)
1. Pull main and read ALL above core documents plus actual issue, dependencies, latest PRs, risk/ADR comments. Never assume chat context survives.
2. Choose earliest UNBLOCKED issue, comment worker/date/branch/scope, claim narrow area; avoid two agents editing same money-state files. For code use `work/TN-014-ledger` branch, reviewed PR; no direct untested merge to main.
3. State **expected acceptance evidence** before editing. Do not change owner-confirmed three-phase manual BlackBox payments/24h Receiver + following 60-day Sender/ACTIVE recovery mirror/no auto R→C/DEAD destination unbinding/native TONG-only without owner signoff.
4. Implement/test in branch, record actual commands and PASS/FAIL, include commit/PR URLs. Zero running code existed at project-tracker setup; DO NOT manufacture percentages, hash/benchmarks or token balances.
5. Append `tracking/DAILY_LOG.md` and update `tracking/HANDOFF.md` **before stopping** (exact next command, active issue/branch/last commit, blocker); change `tracking/CURRENT_STATUS.md` on gate/risk change. Update issue acceptance evidence; only close after reviewed verified criteria.
6. GitHub Actions `project-tracking.yml` validates tracking structure; a **single** `status-sync.yml` workflow records issue-derived snapshots. Bot snapshots do not automatically code, approve owner decisions, or prevent errors.
7. Absolutely NO public-value mainnet, financial marketing, minting/allocating real TONG or handling private keys before all RED cryptography, timing, economic and legal release blockers are addressed and independent audits pass. Tests use valueless localtest TONG.

## Emergency fail-closed rules
Do not assume a lost **S Wallet private key** can execute disaster requiring that very key; distinguish device loss and private signing-key loss. R's ciphertext cannot be secure against R if R has all decrypt keyshares, and R becoming network-final DEAD automatically de-registers the recovery binding. A validator signer key is NEVER the user spending or BlackBox key. Source S becoming DEAD cannot silently shrink live BFT quorum or double-release slashable bonds. Unproven network delay seconds cannot support irreversible forfeiture.

## Outcome reporting
Say **design documented**, **code exists**, **test passes**, **independently audited** and **deployed** only when each has separate linked evidence. An issue being closed by a bot does not prove financial protocol security.
