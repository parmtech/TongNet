# TongNet — GitHub Issue-derived Project Status

**Initial snapshot:** 2026-10-25. **Source:** actual repository GitHub Issues (not CI). When Actions run, workflow will generate this file automatically.

**Snapshot counts:** 24 canonical TN issues; 23 pre-existing legacy Issues. No production code or completed monetary features implied.

## Canonical TN tasks

| Issue | Reported status | Priority | Gate | Dependencies |
|---|---|---|---|---|
| [TN-GOV-001 — Install GitHub worker resume / issue-based project control](https://github.com/manbir6-ux/TongNet/issues/24) | IN_REVIEW | P0 | G0 | None |
| [TN-ARC-001 — Resolve protocol authority, 24h timer t0 and exact payout state transitions](https://github.com/manbir6-ux/TongNet/issues/25) | READY | P0 | G1 | None |
| [TN-SEC-001 — Specify secure claim K_R lifecycle before funded LOCK](https://github.com/manbir6-ux/TongNet/issues/26) | READY | P0 | G1 | TN-ARC-001 |
| [TN-SEC-002 — Solve parent BlackBox archive conditional decryption or mark impossible](https://github.com/manbir6-ux/TongNet/issues/27) | BLOCKED | P0 | G1 | TN-ARC-001 |
| [TN-SEC-003 — Resolve late Sender K_S reclaim secret after original BlackBox loss](https://github.com/manbir6-ux/TongNet/issues/28) | BLOCKED | P0 | G1 | TN-ARC-001, TN-SEC-001 |
| [TN-SPEC-001 — Formal native account ledger invariants and immutable transaction schema](https://github.com/manbir6-ux/TongNet/issues/29) | READY | P0 | G2 | None |
| [TN-SPEC-002 — Formal three-phase BlackBox escrow flow with bound receiver](https://github.com/manbir6-ux/TongNet/issues/30) | BLOCKED | P0 | G2 | TN-ARC-001, TN-SEC-001, TN-SPEC-001 |
| [TN-SPEC-003 — Design verifiable network-delay compensation / protected-suspense exit](https://github.com/manbir6-ux/TongNet/issues/31) | BLOCKED | P0 | G1 | TN-ARC-001 |
| [TN-SPEC-004 — Ratify 60-day post-window unclaimed escrow owner rights](https://github.com/manbir6-ux/TongNet/issues/32) | BLOCKED | P0 | G1 | TN-ARC-001, TN-SPEC-003 |
| [TN-SPEC-005 — Formal active Recovery R lifecycle and S->R DEAD edge cases](https://github.com/manbir6-ux/TongNet/issues/33) | BLOCKED | P0 | G1 | TN-ARC-001 |
| [TN-MONEY-001 — Model TONG hard cap, emission, genesis distribution and stake attack cost](https://github.com/manbir6-ux/TongNet/issues/34) | READY | P0 | G1 | None |
| [TN-ENG-001 — Scaffold Rust test-only ledger workspace and CI](https://github.com/manbir6-ux/TongNet/issues/35) | READY | P0 | E0 | None |
| [TN-TEST-001 — Implement property-based money conservation and escrow state model](https://github.com/manbir6-ux/TongNet/issues/36) | BLOCKED | P0 | G2 | TN-SPEC-001, TN-ENG-001 |
| [TN-CONS-001 — Integrate pinned CometBFT with Rust deterministic state localnet](https://github.com/manbir6-ux/TongNet/issues/37) | BLOCKED | P0 | G3 | TN-ENG-001, TN-TEST-001 |
| [TN-CONS-002 — Implement bonded PoS eligibility, safe epoch changes and slashing evidence](https://github.com/manbir6-ux/TongNet/issues/38) | BLOCKED | P0 | G4 | TN-CONS-001, TN-MONEY-001 |
| [TN-ECON-001 — Implement 3-stage sender fee budget, rewards and anti-farming](https://github.com/manbir6-ux/TongNet/issues/39) | BLOCKED | P1 | G4 | TN-SPEC-002, TN-MONEY-001, TN-CONS-001 |
| [TN-ENG-002 — Build wallet signer and BlackBox manual FINAL_ACCEPT test client](https://github.com/manbir6-ux/TongNet/issues/40) | BLOCKED | P0 | G5 | TN-SPEC-002, TN-SEC-001, TN-ENG-001 |
| [TN-ENG-003 — Build encrypted Active Recovery Mirror with independent key-release review](https://github.com/manbir6-ux/TongNet/issues/41) | BLOCKED | P0 | G6 | TN-SPEC-005, TN-SEC-002, TN-SEC-003, TN-CONS-001 |
| [TN-OPS-001 — Implement P2P, state-sync, archives, signed builds and incident baseline](https://github.com/manbir6-ux/TongNet/issues/42) | BLOCKED | P1 | G3 | TN-CONS-001 |
| [TN-TEST-002 — Build full adversarial formal/differential and chaos test harness](https://github.com/manbir6-ux/TongNet/issues/43) | BLOCKED | P0 | G7 | TN-CONS-002, TN-ENG-002, TN-ENG-003 |
| [TN-NET-001 — Recruit independent operators and run public 90-day adversarial testnet](https://github.com/manbir6-ux/TongNet/issues/44) | BLOCKED | P0 | G8 | TN-TEST-002, TN-OPS-001, TN-ECON-001 |
| [TN-LEGAL-001 — Obtain external Australian crypto, privacy and cross-border legal assessment](https://github.com/manbir6-ux/TongNet/issues/45) | READY | P0 | G9 | None |
| [TN-LAUNCH-001 — Mainnet go/no-go after independent technical and monetary audits](https://github.com/manbir6-ux/TongNet/issues/46) | BLOCKED | P0 | G9 | TN-NET-001, TN-LEGAL-001, TN-MONEY-001, TN-SPEC-004, TN-ENG-003 |
| [TN-MAINT-001 — Quarterly/annual protocol, tokenomics and long-lived recovery maintenance](https://github.com/manbir6-ux/TongNet/issues/47) | BLOCKED | P1 | G11 | TN-LAUNCH-001 |

## Legacy pre-existing Issues (preserved until triaged)

- [#1 [G0][P0] Establish canonical spec and supersession map](https://github.com/manbir6-ux/TongNet/issues/1)
- [#2 [G0][P0] Formal money and lifecycle threat model](https://github.com/manbir6-ux/TongNet/issues/2)
- [#3 [G0][P0] Resolve private-key-loss recovery paradox](https://github.com/manbir6-ux/TongNet/issues/3)
- [#4 [G0][P0] Sealed BlackBox archive conditional decryption](https://github.com/manbir6-ux/TongNet/issues/4)
- [#5 [G0][P0] Sender K_S 24-hour generation and loss paradox](https://github.com/manbir6-ux/TongNet/issues/5)
- [#6 [G0][P0] Specify deterministic deadline and delay-credit protocol](https://github.com/manbir6-ux/TongNet/issues/6)
- [#7 [G0][P0] Review post-60d network-reserve forfeiture](https://github.com/manbir6-ux/TongNet/issues/7)
- [#8 [G0][P0] Lock/Claim/Accept credential and fee-preflight design](https://github.com/manbir6-ux/TongNet/issues/8)
- [#9 [G0][P0] PoS security and vote concentration economics](https://github.com/manbir6-ux/TongNet/issues/9)
- [#10 [G0][P0] Decide TONG issuance and genesis distribution](https://github.com/manbir6-ux/TongNet/issues/10)
- [#11 [G0][P0] Australia and cross-border legal/privacy classification](https://github.com/manbir6-ux/TongNet/issues/11)
- [#12 [G0][P0] Staking bond succession when wallet DEAD](https://github.com/manbir6-ux/TongNet/issues/12)
- [#13 [G1][P1] Bootstrap deterministic Rust repository workspace](https://github.com/manbir6-ux/TongNet/issues/13)
- [#14 [G1][P1] Implement conservative TONG ledger and supply invariants](https://github.com/manbir6-ux/TongNet/issues/14)
- [#15 [G1][P1] Model-check three-stage escrow state machine](https://github.com/manbir6-ux/TongNet/issues/15)
- [#16 [G2][P1] Integrate reviewed BFT engine and 4/7-node localnet](https://github.com/manbir6-ux/TongNet/issues/16)
- [#17 [G2][P1] Bonded PoS lifecycle, slashing and epoch handover](https://github.com/manbir6-ux/TongNet/issues/17)
- [#18 [G2][P1] Implement transaction fee budget and anti-spam](https://github.com/manbir6-ux/TongNet/issues/18)
- [#19 [G3][P1] Native noncustodial Wallet and Sender BlackBox](https://github.com/manbir6-ux/TongNet/issues/19)
- [#20 [G3][P0] Active Recovery Mirror production-grade subsystem](https://github.com/manbir6-ux/TongNet/issues/20)
- [#21 [G4][P1] Testnet operator infrastructure and adversarial load](https://github.com/manbir6-ux/TongNet/issues/21)
- [#22 [G4][P0] Security, legal and economics signoff before mainnet](https://github.com/manbir6-ux/TongNet/issues/22)
- [#23 [G0][P0] Persistent GitHub project control and worker handoff](https://github.com/manbir6-ux/TongNet/issues/23)

## Resume instructions

Read [AGENTS.md](../AGENTS.md), [Project Control](PROJECT_CONTROL.md), [Decisions](DECISION_REGISTER_CURRENT.md), [Work Log](WORK_LOG.md), [50-risk audit](LONG_HORIZON_RISK_AUDIT.md), and [Build plan](BUILD_EXECUTION_PLAN.md); check selected issue's current comments/PRs. A daily status refresh is NOT new coding activity.
