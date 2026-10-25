# TASK REGISTER — TongNet (live GitHub Issues are the status authority)

**Created:** 2026-10-25. **Version:** first persistent issue-backed execution graph. All implementation issues were **OPEN at creation**. GitHub issue state may change; never rely on a stale hand-edited status table.

| Stable key | GitHub issue | Gate | Depends on | Deliverable |
|---|---|---|---|---|
| TN-001 | [#1](https://github.com/manbir6-ux/TongNet/issues/1) | G0 | — | Canonical spec / overrides |
| TN-002 | [#2](https://github.com/manbir6-ux/TongNet/issues/2) | G0 | 001 | Formal threat model |
| TN-003 | [#3](https://github.com/manbir6-ux/TongNet/issues/3) | G0 | 001 | Private-key-loss recovery paradox |
| TN-004 | [#4](https://github.com/manbir6-ux/TongNet/issues/4) | G0 | 003 | Sealed parent threshold decrypt |
| TN-005 | [#5](https://github.com/manbir6-ux/TongNet/issues/5) | G0 | 001,003 | Late K_S sender key loss |
| TN-006 | [#6](https://github.com/manbir6-ux/TongNet/issues/6) | G0 | 002 | Deadlines and network delay proofs |
| TN-007 | [#7](https://github.com/manbir6-ux/TongNet/issues/7) | G0 | 006,011 | Reserve forfeiture and rights |
| TN-008 | [#8](https://github.com/manbir6-ux/TongNet/issues/8) | G0 | 002,006 | K_R proof / fee preflight |
| TN-009 | [#9](https://github.com/manbir6-ux/TongNet/issues/9) | G0 | 002,010 | PoS voting economics |
| TN-010 | [#10](https://github.com/manbir6-ux/TongNet/issues/10) | G0 | 002,011 | TONG genesis and issuance |
| TN-011 | [#11](https://github.com/manbir6-ux/TongNet/issues/11) | G0 | 001 | Legal/privacy classification |
| TN-012 | [#12](https://github.com/manbir6-ux/TongNet/issues/12) | G0 | 002,003,009 | Staked DEAD-wallet succession |
| TN-013 | [#13](https://github.com/manbir6-ux/TongNet/issues/13) | G1 | 001,002 | Rust workspace/CI |
| TN-014 | [#14](https://github.com/manbir6-ux/TongNet/issues/14) | G1 | 013,010 | Conservation and ledger |
| TN-015 | [#15](https://github.com/manbir6-ux/TongNet/issues/15) | G1 | 014,008,006 | Escrow formal state machine |
| TN-016 | [#16](https://github.com/manbir6-ux/TongNet/issues/16) | G2 | 013,014,009 | 4/7 BFT localnet |
| TN-017 | [#17](https://github.com/manbir6-ux/TongNet/issues/17) | G2 | 016,009,012 | Bonded PoS lifecycle |
| TN-018 | [#18](https://github.com/manbir6-ux/TongNet/issues/18) | G2 | 015,017 | Fees and spam protection |
| TN-019 | [#19](https://github.com/manbir6-ux/TongNet/issues/19) | G3 | 015,016 | Wallet + Sender BlackBox |
| TN-020 | [#20](https://github.com/manbir6-ux/TongNet/issues/20) | G3 | 019,003,004,005,012 | Active Recovery Mirror |
| TN-021 | [#21](https://github.com/manbir6-ux/TongNet/issues/21) | G4 | 016,017,018,020 | Multi-operator testnet |
| TN-022 | [#22](https://github.com/manbir6-ux/TongNet/issues/22) | G4 | 007,011,020,021 | Audit/legal/economics mainnet gate |
| TN-023 | [#23](https://github.com/manbir6-ux/TongNet/issues/23) | G0 | — | Project tracking/handoff automation |
 
## How to work through this graph
- If all dependencies unclosed, do only independently scoped documentation/security research, **not money-moving production code**. Opening a parent implementation issue is not permission to invent owner policy.
- Use `Closes #N` in PR only if its full acceptance criteria and tests are satisfied. Otherwise link `Refs #N`.
- Preserve exact `TN-###` key even if GitHub issue number changes in a fork; update mapping in controlled PR.
- Separate production evidence status from research documents: a PDF never counts as completed code.
- This map is a dependency register; detailed acceptance criteria and current OPEN/CLOSED belong to each issue.
