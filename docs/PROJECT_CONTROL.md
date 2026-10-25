# TongNet Project Control — Day-to-Day GitHub Continuity

Established 2026-10-25. **Goal:** another developer/ChatGPT/agent resumes in months without relying on lost chat history.

## Single source of truth
- GitHub Issues with IDs [TN-AREA-NNN] are source for task descriptions, ownership, real state and linked PRs.
- docs/PROJECT_STATUS.md is automatically derived from Issues by a GitHub Action (when enabled). It is *not* handwritten and has a freshness timestamp.
- docs/WORK_LOG.md is append-only factual human/agent session notes. No fabricated work on days with no commits.
- docs/DECISION_REGISTER_CURRENT.md is owner-confirmed versus architect-selected versus blocked protocol rules; significant choices require docs/ADR entries.
- docs/LONG_HORIZON_RISK_AUDIT.md = 50 long-horizon threat items; docs/BUILD_EXECUTION_PLAN.md = G0–G11 dependencies/gates.
- AGENTS.md entry instructions apply to ALL workers, whether human, Codex, Github bot, or ChatGPT.

## Required issue fields
Title [TN-AREA-NNN] Specific deliverable.
- **Status:** TODO, READY, IN_PROGRESS, BLOCKED, IN_REVIEW, DONE
- **Priority:** P0/P1/P2
- **Gate:** G0–G11
- **Type:** SPEC/SECURITY/ENGINEERING/TEST/ECONOMICS/OPERATIONS/LEGAL
- **Depends on:** None, or comma-separated existing TN identifiers
- **Owner/worker:** Unassigned, or honest worker ID
- **Blocking decisions:** None, or U-... / L-... IDs
- **Definition of Done:** measurable reproducible evidence
- **Evidence:** None — not implemented, or verified PR/commit/test links
Issue closed state is canonical for completion, BUT only if evidence/review exists. Issue claiming DONE without closure is inconsistent.

## Work-cycle and handoff
Each coding session: read AGENTS, canonical decisions, open Issue and dependencies; claim via issue comment with worker/time/branch; work on work/TN-... branch, reviewable PR; run tests and link logs; append entry to WORK_LOG.md, provide exact next action and new blockers. Close after merged PR & repeatable tests. Never parallel-write same money state code. Never rewrite past WORK_LOG entries.

## Automation truth & limitations
Scheduled/issue-change GitHub Actions may regenerate PROJECT_STATUS.md from Issues using GitHub API. They do NOT run autonomous software development or attest correctness. Cron can skip/delay and disable after inactivity; Actions must be enabled and GITHUB_TOKEN must have content write. If unavailable, manually compare latest Issues/PR/commits. Workflow must never be used to move issue statuses or claim code passed. No passwords, secrets, wallets or personally identifying data in public issues/logs.

## Owner authority
Newest explicitly user-approved product requirement outranks newer architect suggestion, which outranks stale old docs. Latest rules: no 3-hour Trigger, Receiver 24 hours then Sender 60 days, manual final Sender BlackBox approval; R ACTIVE + sealed parent-only archive, R DEAD => unbind S. Older frozen-R and 72-hour sender texts are obsolete. Changed money rights or genesis issuance require written owner ratification; don't infer consent from this planning document.

## Work classifications
COMPLETE_DOCS: documented/merged but no code.
READY: all dependencies and major decisions closed.
IN_PROGRESS: worker explicitly active.
BLOCKED: dependencies/owner decisions/security proof unknown.
DONE: merged implementation with tests and review evidence.

## Routine reviews
After each session log; daily status snapshots if automation available; weekly P0/issues/deadlocks; monthly risks and dependency reconciliation; quarterly consensus/dependencies/economics/legal stress review; before release independent audits and 90-day adversarial testnet.

## Project readiness
Specifications documented do NOT mean crypto deployed. Real-value mainnet blocked by conditional decryption, lost K_S, deadline correctness, unsafe forfeiture, future stake distribution and legal/security audit. Any plan item making misleading "guaranteed safe/unhackable" claims must be revised.
