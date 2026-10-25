# TongNet — CANONICAL Issue-backed Task Register

**Updated 2026-10-25.** **25 unique canonical work items, issue status comes ONLY from GitHub.** #24–#47 are the task set created by parallel project-control work. Critical private-signing-key-loss issue [#3](https://github.com/manbir6-ux/TongNet/issues/3) is additionally retained as unique TN-SEC-004, because no canonical #24–#47 task fully covers it. **The other 22 older #1–#23 issues were marked CLOSED AS DUPLICATES on 2026-10-25, NOT DONE.** See [migration map](../docs/LEGACY_ISSUE_MIGRATION.md). A closed duplicate must never count as a completed engineering deliverable.

**LIVE status:** [GitHub Issues](https://github.com/manbir6-ux/TongNet/issues) — issue OPEN/CLOSED, body status, accepted PR and CI logs. The published [auto status](../docs/PROJECT_STATUS.md) and [dated snapshots](auto/) are mirrors, not separate task authorities.

| Stable ID | Canonical GitHub issue | Release gate | Dependencies (blocked if incomplete) | Deliverable |
|---|---|---|---|---|
| TN-GOV-001 | [#24](https://github.com/manbir6-ux/TongNet/issues/24) | G0 | None | Issue-led continuity and daily sync |
| TN-ARC-001 | [#25](https://github.com/manbir6-ux/TongNet/issues/25) | G1 | None | Canonical protocol / t0 decisions |
| TN-SEC-001 | [#26](https://github.com/manbir6-ux/TongNet/issues/26) | G1 | TN-ARC-001 | Claim K_R before LOCK |
| TN-SEC-002 | [#27](https://github.com/manbir6-ux/TongNet/issues/27) | G1 | TN-ARC-001 | Cryptographic sealed archive |
| TN-SEC-003 | [#28](https://github.com/manbir6-ux/TongNet/issues/28) | G1 | TN-ARC-001, TN-SEC-001 | Late K_S loss |
| TN-SEC-004 | [#3](https://github.com/manbir6-ux/TongNet/issues/3) | G1 | TN-ARC-001, TN-SPEC-005 | Lost original S private key (separate RED blocker) |
| TN-SPEC-001 | [#29](https://github.com/manbir6-ux/TongNet/issues/29) | G2 | None | Monetary state and invariants |
| TN-SPEC-002 | [#30](https://github.com/manbir6-ux/TongNet/issues/30) | G2 | TN-ARC-001, TN-SEC-001, TN-SPEC-001 | Native manual escrow |
| TN-SPEC-003 | [#31](https://github.com/manbir6-ux/TongNet/issues/31) | G1 | TN-ARC-001 | Network delay compensation |
| TN-SPEC-004 | [#32](https://github.com/manbir6-ux/TongNet/issues/32) | G1 | TN-ARC-001, TN-SPEC-003 | Post-60d funds rights |
| TN-SPEC-005 | [#33](https://github.com/manbir6-ux/TongNet/issues/33) | G1 | TN-ARC-001 | ACTIVE R and DEAD target recovery |
| TN-MONEY-001 | [#34](https://github.com/manbir6-ux/TongNet/issues/34) | G1 | None | TONG distribution/PoS economics |
| TN-ENG-001 | [#35](https://github.com/manbir6-ux/TongNet/issues/35) | E0 | None | Rust workspace and CI |
| TN-TEST-001 | [#36](https://github.com/manbir6-ux/TongNet/issues/36) | G2 | TN-SPEC-001, TN-ENG-001 | Money property tests |
| TN-CONS-001 | [#37](https://github.com/manbir6-ux/TongNet/issues/37) | G3 | TN-ENG-001, TN-TEST-001 | Pinned BFT localnet |
| TN-CONS-002 | [#38](https://github.com/manbir6-ux/TongNet/issues/38) | G4 | TN-CONS-001, TN-MONEY-001 | Bonded PoS and safe epoch |
| TN-ECON-001 | [#39](https://github.com/manbir6-ux/TongNet/issues/39) | G4 | TN-SPEC-002, TN-MONEY-001, TN-CONS-001 | Fee+Earn budget and anti-farming |
| TN-ENG-002 | [#40](https://github.com/manbir6-ux/TongNet/issues/40) | G5 | TN-SPEC-002, TN-SEC-001, TN-ENG-001 | Wallet, Sender BlackBox |
| TN-ENG-003 | [#41](https://github.com/manbir6-ux/TongNet/issues/41) | G6 | TN-SPEC-005, TN-SEC-002, TN-SEC-003, TN-CONS-001, TN-SEC-004 | Recovery mirror and encryption |
| TN-OPS-001 | [#42](https://github.com/manbir6-ux/TongNet/issues/42) | G3–G8 | TN-ENG-001 | Network archive/seed/build safety |
| TN-TEST-002 | [#43](https://github.com/manbir6-ux/TongNet/issues/43) | G7 | TN-TEST-001, TN-CONS-001 | Adversarial model/chaos tests |
| TN-NET-001 | [#44](https://github.com/manbir6-ux/TongNet/issues/44) | G8 | TN-CONS-001, TN-CONS-002, TN-TEST-002 | Independent 90d testnet |
| TN-LEGAL-001 | [#45](https://github.com/manbir6-ux/TongNet/issues/45) | G1–G9 | None | Legal/consumer/privacy assessment |
| TN-LAUNCH-001 | [#46](https://github.com/manbir6-ux/TongNet/issues/46) | G9–G10 | All critical | Independent go/no-go |
| TN-MAINT-001 | [#47](https://github.com/manbir6-ux/TongNet/issues/47) | G11 | TN-LAUNCH-001 | 3/6/12/24mo maintenance |

## Required order & worker allocation
- Product/rights decisions **G1** and cryptographic RED issues are gate blockers, not a reason to skip safe independent **E0** Rust test-only scaffolding. Resolve dependencies before production financial flow coding.
- Existing [G0–G11 detailed delivery plan](../docs/BUILD_EXECUTION_PLAN.md) defines technical exit gates; early [G0/G1/G2/G3/G4] titles on the CLOSED legacy #1–#23 issues are NOT those full gates.
- All new issues use stable `[TN-AREA-NNN]` names; add one row here whenever a new issue is accepted. Never reissue a retired task ID.
- Every worker owns one issue/branch at a time. Define tests before work. Close only with merged reviewed evidence (code vs spec must be distinguished).
- `tracking/HANDOFF.md` indicates exact next unblocked work; append factual notes in `tracking/DAILY_LOG.md`. Do not count periodic bot statuses as implemented work.

## Duplicate issue migration (not completed)
**Historical #1-#23** have status `closed` and reason `duplicate` (or equivalent GitHub UI wording) except **#3 remains OPEN unique critical key-loss blocker**. Relevant definitions are preserved in their issue bodies for audit; refer to canonical issue number above for execution. No source-code task was completed by this migration.
