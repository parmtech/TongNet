# CURRENT_STATUS — TongNet

**Last human-authored update:** 2026-10-25 (Australia/Sydney).  
**Current project phase:** G0 — canonical specification, adversarial security and economics review.  
**Project confidence:** Design/research ONLY. No blockchain executable, running node, Rust workspace, Wallet, BFT testnet, verified metrics or real TONG issuance found in the repository's initial tree (30 Markdown documents, no existing GitHub Issues).  
**Tracking:** 47 GitHub issues created across parallel tracking work; 25 canonical OPEN issues (#24–#47 and unique #3), 22 CLOSED AS DUPLICATES (not completed); see [TASKS.md](TASKS.md) and [live GitHub Issues](https://github.com/parmtech/TongNet/issues).

## Phase scoreboard (evidence, NOT % completion)
| Gate | Status | What actually exists | Release allowed |
|---|---|---|---|
| G0 - spec/risk/architecture | IN PROGRESS | V1.1 whitepaper, prior research and the new project-control system | No |
| G1 - deterministic Rust money engine | NOT STARTED | No verified build/code | No |
| G2 - BFT localnet & staking | NOT STARTED | No verified nodes | No |
| G3 - wallet, BlackBox, recovery | NOT STARTED | No verified apps or cryptographic key-release | No |
| G4 - open adversarial testnet & legal audit | NOT STARTED | No public testnet or external audit | No |
| G5 - independent mainnet signoff | BLOCKED | Multiple unsolved loss/consent/cryptoeconomic risks | NO |

## Current RED blockers
**Key loss cannot be recovered with a policy that demands the lost S signing key; mirror decrypt conditional-release not designed/audited; Sender K_S lost-before-created paradox; objective delay-credit and protected suspense exits; legal legitimacy of confiscating unclaimed escrow; initial validator security and token allocation; stake-bond succession; no independently verified code.** See [RISKS.md](RISKS.md).

## Recommended first implementation sequence
1. Address canonical protocol **#25** and specification/invariants **#29** with documented evidence.
2. In parallel resolve design forks **#26–#34** and unique loss-of-S-key **#3**; never silently authorise replacement signing/backups.
3. Begin executable work at **#35** Rust workspace followed by **#36** money model, **#30** escrow, **#37** BFT.
4. Add bond/fees and integrations only when dependencies valid, then open adversarial G4 testnet.
5. **Mainnet disallowed** while RED issues and owner confirmation requirements persist.

## Decision/change process
Issues canonical; actions bot snapshots optional; update this page at every *phase or critical risk change*. The 100m cap, 64 validators, 6s blocks and other numeric guesses are TEST PARAMETERS, not deployed claims or final economic choices.

**Parallel issue reconciliation:** 22 old issues were closed for duplicate reason, not completed engineering. Single canonical set is 24 new structured issues #24–#47 and the unique #3 critical root-key-loss recovery paradox. Automated Status Sync execution not yet verified; do not count workflow declaration as a successful run.

## Active specification work (2026-10-26)
- TN-SPEC-001 #29 is assigned and has a draft test-only proposal in [PR #49](https://github.com/parmtech/TongNet/pull/49), head `bba95c659a695cc2368ebc74544887f592ceed3a` on `work/TN-SPEC-001-ledger-invariants`.
- Local JSON parsing and schema operation/reference consistency checks passed. No Rust implementation/tests or full JSON Schema validator are claimed. The proposal preserves unresolved financial and timing choices for review; issue #29 remains open.
- PR review and inline thread lists are empty. GitHub Actions run `40163434903` failed before a runner started due account billing/spending-limit status; no code checks ran.


## Active architecture proposal (2026-10-26)
- TN-ARC-001 #25 has a test-only candidate transition table in [draft PR #51](https://github.com/parmtech/TongNet/pull/51), branch `work/TN-ARC-001-payout-transitions`, candidate commit `5c130b951c36af82e87710291f53c841cef9aea4`. It is stacked on TN-SPEC-001 PR #49.
- Candidate intervals are Receiver `[t0, t0+24h)` and Sender manual reclaim `[t0+24h, t0+24h+60d)`, then no automatic money movement. `t0`, cutoff treatment, and consensus-clock rules require owner ratification; issue #25 remains open.
