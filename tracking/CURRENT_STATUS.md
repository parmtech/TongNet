# CURRENT_STATUS — TongNet

**Last human-authored update:** 2026-10-25 (Australia/Sydney).  
**Current project phase:** G0 governance remains in progress; E0 Rust workspace and CI foundation has started on TN-ENG-001.  
**Project confidence:** Design/research plus an in-progress test-only Rust workspace scaffold. No blockchain executable, running node, financial state machine, Wallet, BFT testnet, verified metrics or real TONG issuance.  
**Tracking:** 47 GitHub issues created across parallel tracking work; 25 canonical OPEN issues (#24–#47 and unique #3), 22 CLOSED AS DUPLICATES (not completed); see [TASKS.md](TASKS.md) and [live GitHub Issues](https://github.com/manbir6-ux/TongNet/issues).

## Phase scoreboard (evidence, NOT % completion)
| Gate | Status | What actually exists | Release allowed |
|---|---|---|---|
| G0 - spec/risk/architecture | IN PROGRESS | V1.1 whitepaper, prior research and the new project-control system | No |
| E0 - engineering foundation | IN PROGRESS | TN-ENG-001 draft PR contains the Rust workspace/CI scaffold; GitHub Actions is blocked by the account billing limit | No |
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
