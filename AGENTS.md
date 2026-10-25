# TongNet — Mandatory Worker Entry Point

**Every new worker or AI agent must read this BEFORE doing work.** A whitepaper is not deployed blockchain code. No running chain or audited money system has been verified.

## Resume checklist
1. Read [Project Control](docs/PROJECT_CONTROL.md), [Generated Issue Status](docs/PROJECT_STATUS.md), and [Session Log](docs/WORK_LOG.md). Confirm status freshness.
2. Read [Current Decisions](docs/DECISION_REGISTER_CURRENT.md), [Long-Horizon 50-Risk Audit](docs/LONG_HORIZON_RISK_AUDIT.md), [Execution Plan](docs/BUILD_EXECUTION_PLAN.md), and [Whitepaper V1.1](docs/WHITEPAPER_MASTER_V1_1_SECURITY_REVIEW.md).
3. Check the currently chosen issue [TN-AREA-NNN], all prerequisites, open PRs, attached test evidence and next steps.
4. Claim exactly one issue: comment worker, UTC time, intended branch and scope; change its body Status to IN_PROGRESS. Use branch work/TN-AREA-NNN-short-slug, not main. Avoid another agent writing same financial state files simultaneously.
5. Produce reviewable PR, tests/evidence, and append factual progress to docs/WORK_LOG.md; no fabricated daily activity. Never close implementation issue without merged code, meaningful tests and review.
6. Record changed protocol decisions in an ADR and update DECISION_REGISTER_CURRENT. Do not quietly override owner-confirmed money rights.
7. If actions are disabled or status report stale, use GitHub Issues + commits as truth; optionally use GitHub Actions workflow_dispatch for status regeneration. Scheduled workflow reports task state only; it does not autonomously do programming.

## Product invariants
One native TONG coin, no EVM/dApp/token creator. Sender initiates escrow LOCK; Receiver signs claim using secure K_R proof; **independent Sender BlackBox FINAL_ACCEPT mandatory** before payout. No 3h Trigger. Receiver nominal 24h, Sender following 60 days manual reclaim. Actual t0 for 24h needs owner ratification. No unreviewed automatic fund confiscation. Recovery R remains ACTIVE while hosting sealed S-parent BlackBox archive only; S old ledger transactions stay on S. If R consensus-final DEAD, S->R automatically unbinds; no chain redirect to C. Private keys, Authenticator, validator signing keys and BlackBox secrets separate.

## Highest priority security blockers
Late-generated Sender reclaim K_S after lost BlackBox; conditional decrypt release to R; verifiable one-for-one network delay; reserve forfeiture legal/consumer safety; validator stake successor entitlement after S DEAD; unknown genesis supply/control economics. See decisions U-001 to U-012.

## Build first
Governance/docs may complete independently of software. Safe first coding: test-only deterministic Rust native ledger and conservation/escrow property tests (TN-ENG-001, TN-SPEC-001, TN-TEST-001). No public TONG tokens/funds, releases, deployed wallet or verified BFT claimed.

## Multi-worker conflict rule
One task owner and code area at a time; link every PR to issue and every update to CI. Never merge conflicting quorum, ledger money, keys, deadlines or state format edits without coordinated ADR. Reject statements of "all secure" without reproducible independent evidence.
