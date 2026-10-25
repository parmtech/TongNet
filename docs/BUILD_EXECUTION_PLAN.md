# TongNet — Implementation Execution Plan, Milestones, Dependencies & Exit Gates
**Version:** 2026-10-25 / Build Playbook 1. **Owner delegated architect choices:** plan and recommended defaults. **Status:** repo has specifications, no verified working chain or valid circulating TONG. Never represent plan tasks as built.

## Design baseline, latest first
- TongNet single native coin only; explicit three-phase manual bilateral BlackBox payment; Receiver exclusive 24h then Sender separate 60 full days reclaim; no 3h Trigger; ACTIVE independently functioning Recovery R and sealed parent-BlackBox-only mirror; R DEAD unbinds S without auto-forward C.
- Candidate simple Rust account-based native state machine, bounded fee budget and small PoTP receipt *without consensus voting*. Consensus prototype should use vetted CometBFT BFT with deterministic Rust ABCI++ adapter; volunteer bonded PoS participation only after state machine safety proven. No default public contracts, arbitrary assets, fiat peg, miner ASIC, unproven transaction voting.
- Never lock mainnet supply/minting, minimum stake, coin issue distribution, 64 validator counts or high throughput as "validated" from whitepaper guesses alone.

## Core workstreams and dependency graph

\`\`\`text
[G0 governance + canonical requirements + 50-risk inventory]
        |                         |
        v                         v
[G1 owner-ratified financial-rights ADRs]    [E0 engineering repo + CI + signed release base]
        |                                     |
        v                                     |
[G2 native ledger/escrow executable model] <-+
        |
        +--> [G3 local BFT network / deterministic state roots] --> [G4 staking+fees]
        |                                                         |
        +--> [G5 BlackBox code+identity+manual approval] ---------+
        |              |
        |              +--> [G6 conditional crypto recovery research & audited implementation]
        |                                                         |
        +--> [G7 property tests, fuzz, temporal formal model] <----+
                                 |
                                 v
               [G8 public adversarial testnet & independent operators]
                                 |
                                 v
                [G9 economics/legal/security external go/no-go]
                                 |
                                 v
                        [G10 limited mainnet] --> [G11 long-term Ops]
\`\`\`

### Gate G0 — Governance & provenance (NOW)
Deliverables: AGENTS.md, WORKING_AGREEMENT, code freeze categories, project status dashboard, issue-backed canonical task inventory, risk register, ADRs, session history, CI/PR rules and schedule sync. Exit: external worker from zero context can name exact next approved ready item, blockers, tests and branch rules in under 15 minutes. Deliverable documents can be COMPLETE even when chain 0% complete.

### Gate G1 — formal financial rights before coding money movement (P0)
- Ratify LOCK t0 for 24h; define exactly when CLAIM and FINAL_ACCEPT must BFT-finalise and what happens at cutoff.
- Resolve K_S late-issued secret paradox and S/R survivor entitlements with owner explicit approval or stop affected live-funds feature.
- Design architect-selected K_R pre-LOCK persisting backed-up ephemeral key with accepted UX; no 6-digit on-chain guessing oracle.
- Pick lawful outcome for post-(24h+60d) unclaimed funds, including outage disputes. Do not implement automatic reserve forfeiture in money-bearing code before reviewed.
- Define canonical deterministic deadline policy and irreducible outage ambiguity, consensus timestamp source and fail-closed suspense exit.
- Clarify R initial virgin constraint only if owner wishes change; confirmed R remains normal ACTIVE afterward.

Exit: precise machine-readable transition table and BFT-finality predicates with counterexamples; owner-approved changed financial rules, reproducible bounded formal state tests, no contradictory interpretation.

### Gate E0 — engineering foundation (start immediately, separate from unratified finance)
- Initialise Cargo workspace with **no live TONG**: \`ledger-core\` deterministic state crate, \`crypto-types\`, \`protocol-types\`, \`model-tests\`, \`consensus-adapter\` (scaffold only).
- Rust pinned toolchain, \`cargo fmt --check\`, \`cargo clippy -- -D warnings\`, \`cargo test --workspace\`, \`cargo deny\` or independently evaluated license/SBOM task, multi-OS only after compatibility test. No unsafe money modules without explicit documented security review.
- Continuous integration for code; GitHub Issues→status sync for tracking is separate and must NOT be confused with product tests.
- Signed commits or reviewable PRs, CODEOWNERS where owners confirmed, repo secret scanning/branch protection manual setup steps.

Exit: reproducible builds and deterministic tests in CI. No claim of working BFT.

### Gate G2 — deterministic local value ledger (first real code)
- Wallet lifecycle incl. 72h activation safeguard, balance categories, nonce/chain ID, checked integer arithmetic, zero-value test Faucet and no real asset.
- \`LOCK\`, \`CLAIM_REQUEST\`, \`FINAL_ACCEPT\`, \`SENDER_RECLAIM\`, \`RECOVERY_PAIR\`, \`RECOVERY_RUN\` as test-only finite transitions. DO NOT silently choose production payout after 60d or recovery decrypt method.
- Make all transitions deterministic with explicit authorizations, immutable receipts and duplicate/replay rules.
- Test conservation, no two winners, no payout on CLAIM without signed Sender FINAL_ACCEPT, no pair with DEAD R and no spontaneous R→C forwarding.

Exit: property-based randomized tests, exhaustive small bounded model, tests for interrupt after every transition.

### Gate G3 — consensus integration (after local reference model)
- Version-pin CometBFT / ABCI++ compatibility; review its licensing, release security history and Rust application bridge. Proposal/mempool validation MUST NOT commit financial state; only FINALIZED blocks mutate state.
- Build 4–7 peer localnet; simulate Byzantine double-sign, 1/3 outage, 60/40 partition, delayed epoch validator updates, crash recovery and snapshots.
- No custom consensus claims. Produce stable roots under deterministic replay on diverse hosts.
Exit: repeated consistency tests + independent worker code review.

### Gate G4 — validator registration and economics (after G3)
- Explicit owner opt-in bonded stake, pending maturity, attested online node key (not wallet key), slashable unbonding longer than max evidence age, deterministic consensus epoch snapshots and weighted >2/3 quorum.
- Attack model 100k fake accounts splitting same bond, rapid loans/borrowed stake, colluding vendors/one cloud/one human in many nodes, cheap token capture.
- Introduce sender budget across 3 actions; validator work rewards only for actual independently chosen consensus duty, untrusted PoTP only optional.
- DO NOT assign production min stake or hard-genesis schedule before economics ADR and external security assumptions.
Exit: artificial faucet chain economic model and bounded queue/pricing under spam.

### Gate G5 — Wallet & BlackBox (can parallelize G3 only after G2 spec)
- High-entropy claim credential pre-persisted before LOCK; signed exact receiver and amount; sender manual independent FINAL_ACCEPT; no raw K_R on chain; separate BlackBox authority and local key stores.
- UI status exact finality vs pending; sender never pays just because receiver knows code; 24h/60d visually explained, unauthorized fake accept refused.
- Light client verifies quorum and state root, not only a single RPC response.
Exit: compromised validator signer cannot spend/send or open parent archive, expired claim rejects, no secret leakage in logs.

### Gate G6 — Optional Recovery (isolated and initially test-only)
- Active R has own funds/messages and may hold sealed parent S archive. First binding requires accepted R BlackBox and one-use disaster secret; verified BFT-finished recovery makes S DEAD, R remains ACTIVE; historical on-chain S tx never become R tx.
- Truly locked parent archive requires cryptographic key-release under explicit assumed threshold/collusion; independent audit. If R DEAD, automatic S->R unbind; no C inheritance.
- Pending escrow and slashable bond entitlements survive according to owner-ratified, formally tested rights.
- If conditional archive secrecy or K_S recovery cannot be solved and approved, mainnet should **not enable unrecoverable value-bearing flows or misrepresent security**; feature deferral needs owner consent because recovery/BlackBox are core product.
Exit: cold lost phone/keys restoration drills, malicious R, malicious threshold custodians, R DEAD while pairing and S funded pending escrows, two simultaneous recovery signatures.

### Gate G7 — formal tests and security proof obligations
Formalise small model TLA+/Apalache or comparable and separate independent reference interpreter. Property-based fuzz and invariants documented. Tests include 1m synthetic adversarial events and 90 days multiple operators (not a substitute for crypto proofs).
Report external vulnerability disclosure, CVE dependency support, metrics and threat coverage.
Exit: every P0 risk test/evidence linked and audit sign-off, not only successful build.

### Gate G8 — network rehearsals
Start 21 truly separate willing test operators; scale to 64 active, >=32 standby, >=128 independent full nodes as **targets** only. No assumed percentages of real persons; prove as much economic/control independence as practicable and state unknowable clusters. Geographic diversity, multi-cloud, multi-ISP, replacement/quorum recovery tests. Stress 256KiB/6sec **hypotheses** vs measured storage, gas/memory.
Exit: 90-day public adversarial testnet; no critical fund-loss/inconsistent state findings.

### Gate G9 / G10 — honest launch boundaries
Independent consensus/application audit; independent BlackBox/recovery key escrow audit; independent tokenomics and distribution modelling; Australian professional legal memo on issuer/operator role; transparent supply/time-lock governance; explicit owner sign-off. No launch if still any P0 unsolved.
After release, publish signed reproducible binaries, emergency patch procedures and fork communication. No marketing claim "unhackable", "guaranteed no fee", "$ value" or "world's first" without evidence.

### Gate G11 — multi-year maintenance
Version and incident policy with no universal admin funds key. Security release support, archive/state pruning, wallet migrations, compromised key recovery, economics telemetry, governance capture and legal monitoring. Quarterly (3 months), half-yearly, annual and two-year review issues.

## Suggested worker sequencing for multiple agents
**Spec worker:** formal native operations; **Risk/crypto worker:** key lifecycle and impossibility review; **Core worker:** only approved Rust money state; **Consensus worker:** pinned BFT integration; **Testing worker:** adversarial independent model/CI; **Ops worker:** GitHub status and procedures. Never assign two workers write ownership of same money file concurrently. Each worker opens exactly one issue, creates \`work/TN-XXX-short-slug\`, publishes draft PR and updates issue; merge one at a time on state machine. No worker may "solve" owner-confirmed financial conflicts without ratified ADR.

## Definition of Ready / Done
**Ready:** issue has canonical requirements, scope, dependencies, measurable acceptance and test plan, no unresolved blocking ADR. **Done:** linked merged PR/commit, green meaningful CI, updated decision/spec, independent review, reproducible evidence and no orphan P0 risk. Documentation alone cannot mark implementation tasks done.

## Concrete first work after project-control creation
1. Draft \`docs/ADR/0001-consensus-and-native-state.md\` and exact escrow transitions; ensure latest owner rules are understood.
2. Open/clarify G1 blocking financial-right issues, no fabricated assumption.
3. Scaffold Rust money-only workspace with CI, test-only supply; no live wallet or genesis.
4. Implement checked integer balance/invariant model; property tests and deterministic replay.
5. Only then run and verify local BFT integration, staging features behind flags.

All task IDs, evidence and actual state are tracked in GitHub Issues and \`docs/PROJECT_STATUS.md\`, NOT this narrative plan. This file is architecture roadmap and must be revised with an ADR on significant changes.
