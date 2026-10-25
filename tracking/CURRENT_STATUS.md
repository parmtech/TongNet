# CURRENT_STATUS — TongNet

**Last human-authored update:** 2026-10-25 (Australia/Sydney).  
**Current project phase:** G0 — canonical specification, adversarial security and economics review.  
**Project confidence:** Design/research ONLY. No blockchain executable, running node, Rust workspace, Wallet, BFT testnet, verified metrics or real TONG issuance found in the repository's initial tree (30 Markdown documents, no existing GitHub Issues).  
**Tracking:** 23 GitHub issues created 2026-10-25; see [TASKS.md](TASKS.md) and [live GitHub Issues](https://github.com/manbir6-ux/TongNet/issues).

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
1. Close spec supersession mapping **#1** and risk/invariants **#2** with documented evidence.
2. In parallel resolve design forks **#3**–**#12**; never silently authorise replacement signing/backups.
3. Begin executable work at **#13** Rust workspace followed by **#14** money accounting, **#15** escrow, **#16** BFT.
4. Add bond/fees and integrations only when dependencies valid, then open adversarial G4 testnet.
5. **Mainnet disallowed** while RED issues and owner confirmation requirements persist.

## Decision/change process
Issues canonical; actions bot snapshots optional; update this page at every *phase or critical risk change*. The 100m cap, 64 validators, 6s blocks and other numeric guesses are TEST PARAMETERS, not deployed claims or final economic choices.
