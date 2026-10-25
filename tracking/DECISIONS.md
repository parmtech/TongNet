# TongNet — Architecture Decision Register (ADR)

This register is for *current decisive questions*, with **Confirmed Owner** distinguished from **Architect-selected Baseline**, **Proposal**, **Rejected**, **Blocked**. Historical source: [docs/DECISIONS.md](../docs/DECISIONS.md) and [v1.1 whitepaper](../docs/WHITEPAPER_MASTER_V1_1_SECURITY_REVIEW.md). One financial-right change needs explicit owner approval and an ADR; no automated GitHub bot approves financial policy.

| ADR | Status (2026-10-25) | Decision | Evidence / caveat |
|---|---|---|---|
| ADR-001 | CONFIRMED OWNER | Only one native TONG cryptocurrency; no EVM/dApps/tokens | [Scope](../docs/TONGNET_BITCOIN_LIKE_SCOPE.md) |
| ADR-002 | CONFIRMED OWNER | Manual Sender BlackBox Final Accept required; no old 3h Trigger | [Payment](../docs/SECURE_P2P_V3_RECOVERY_DECISIONS.md) |
| ADR-003 | CONFIRMED OWNER | Receiver 24h then Sender exclusive 60d reclaim; no automatic refund at 24h | Clock t0 at final LOCK still *unratified*. |
| ADR-004 | CONFIRMED OWNER | Both source S and recovery R ACTIVE; sealed S BlackBox only mirrored, no S historical chain transactions transferred | [Active R V4](../docs/ACTIVE_RECOVERY_MIRROR_V4.md) |
| ADR-005 | CONFIRMED OWNER | R final DEAD → auto-revoke S→R, S no recovery until new pairing; no hidden R→C cascade | [V4](../docs/ACTIVE_RECOVERY_MIRROR_V4.md) |
| ADR-006 | PRESERVED PENDING CLARIFICATION | R must be fresh/never-financially-used **at initial binding**; may operate normally after binding | Latest owner didn't explicitly revoke *first-binding* constraint. |
| ADR-007 | ARCHITECT BASELINE | Bonded voluntary PoS + BFT and nonvoting optional transaction-proof checking; no ASIC PoW | Requires attack-cost and formal proof testing. |
| ADR-008 | ARCHITECT BASELINE | Deterministic account ledger, Rust engine + reviewed BFT, low Fee+Earn | Proof/economics incomplete. |
| ADR-009 | PROPOSED ONLY | 64 active /32 standby node targets, 6s /256KiB testnet target | Not security guarantees or approved mainnet parameters. |
| ADR-010 | WITHDRAWN | V1.0 12m genesis / 17.6m first-era / founder-linked distribution guesses | Removed as unsafe/unbalanced; [V1.1](../docs/WHITEPAPER_MASTER_V1_1_SECURITY_REVIEW.md). |
| ADR-011 | BLOCKED — OWNER POLICY CONFLICT | K_S only generated after 24h vs lost/dead Sender BlackBox | Needs explicit owner ratification of alternative [#5](https://github.com/manbir6-ux/TongNet/issues/28). |
| ADR-012 | BLOCKED | S private key required for S disaster means lost key irrecoverable | [#3](https://github.com/manbir6-ux/TongNet/issues/3) must resolve; no unilateral admin bypass. |
| ADR-013 | BLOCKED | R genuinely unable to decrypt S archive before authorised recovery | Key-share threat model and independent audit [#4](https://github.com/manbir6-ux/TongNet/issues/27). |
| ADR-014 | CONFIRMED INTENT, BLOCKED RELEASE | Post-60d reserve transfer of unclaimed user funds | Consumer/legal/denial attacks [#7](https://github.com/manbir6-ux/TongNet/issues/32). No implementation into mainnet yet. |
| ADR-015 | BLOCKED DESIGN | Strict one-to-one network fault deadline compensation | Exact attribution impossible in all asynchronous adversarial settings [#6](https://github.com/manbir6-ux/TongNet/issues/31). |
| ADR-016 | ARCHITECT BASELINE/OWNER SIGNOFF NEEDED | S validator stake stays slashable after S DEAD, with R delayed withdrawal right | [#12](https://github.com/manbir6-ux/TongNet/issues/33), cannot evict active BFT signer mid-epoch. |

**ADR template:** `ADR-017 | YYYY-MM-DD | status | problem | considered alternatives | accepted solution | affected fund/legal/security guarantees | links owner decision/issue/PR | rollback/migration`. Do not edit confirmed owner rules because an old README says otherwise.
