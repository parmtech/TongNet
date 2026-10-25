# TongNet Persistent Project Control

**Purpose:** All future workers use this repository as a shared memory across days, months and parallel agents, and distinguish *documented plan* from *coded/tested software*.

## Canonical information, in priority order
- **GitHub Issues** [issue list](https://github.com/manbir6-ux/TongNet/issues): individual task status and acceptance evidence; issue OPEN vs CLOSED is the single source of truth.
- [TASKS.md](TASKS.md): indexed build dependencies/priority; IDs never recycled.
- [HANDOFF.md](HANDOFF.md): immediate resume state; always read first.
- [DAILY_LOG.md](DAILY_LOG.md): human/agent day-by-day immutable appended work journal; record full date and tests.
- [AUTO_STATUS.md](AUTO_STATUS.md) and `auto/YYYY-MM-DD.md`: generated GitHub Actions snapshots of issue status/commits (when Actions runs); **snapshots are not evidence that actual tests passed**.
- [DECISIONS.md](DECISIONS.md): versioned architecture decision records with owner-confirmed vs recommended vs rejected status.
- [RISKS.md](RISKS.md): issue-linked severity, owner and mitigation; RED release blockers.
- [CURRENT_STATUS.md](CURRENT_STATUS.md): latest manually curated stable phase/milestone status.
- [AGENTS.md](../AGENTS.md): required worker protocol.
- [long-term review](../docs/A_TO_Z_LONG_TERM_REVIEW_V2.md), [build plan](../docs/BUILD_EXECUTION_PLAN_V2.md).

## Status definitions
- `OPEN`: ticket is not proven complete; may be PLANNED, RESEARCH, ACTIVE or BLOCKED in its text/PR.
- `CLOSED`: accepted deliverable with evidence link (for docs tasks, published/reviewed document; for implementation tasks, reviewed code and passing automated tests).
- `BLOCKED`: do NOT code a financial assumption as an accepted rule; record the exact decision or missing evidence.
- `FAILED`: a test or audit failed; no concealment or imaginary percentage.
- `MAINNET_READY`: not a label a worker may set without security, legal, economic and owner gates.

## Anti-staleness mechanism
Run `python3 scripts/check_tracking.py` on each PR; `.github/workflows/project-tracking.yml` validates references. A separate GitHub Actions workflow `tracking-daily.yml` can write a repository snapshot once daily and on issue events. Automatic snapshots only use verifiable issue states and GitHub commits; manual journal still requires worker action. Protected branches/disabled Actions may prevent automation; read workflow run health.
