# TongNet — Documentation & Project Change Log

## 2026-10-24 — Question 2 answered and committed
- User confirmed that failure to activate TongNet Authenticator within the wallet's first 72 hours makes that wallet **permanently DEAD** and it can never be reactivated, irrespective of later possession of its keys.
- No replacement of the lost first-time Setup Key to bypass the deadline. Wallet must be replaced; initial inactive wallets cannot SEND, RECEIVE or CLAIM.
- Updated decisions, FAQ, protocol, security, progress and next-session handoff. This is a requirement, not yet an implemented or tested safety property.
- **Next Q3:** loss of Authenticator Master Key/device after a wallet has successfully activated.

## 2026-10-24 — Question 1 answered and committed
- User explicitly chose **Option B** for wrong receiver address after Trigger: **no cancellation, no emergency stop, even for erroneous address**.
- Receiving address still has 24h to claim; sender can recover during subsequent 72h **only if no receiver claim succeeds**.
- Updated decision register, FAQ, draft protocol, threat model, progress and session handoff.
- **Next Q2:** lost one-time Authenticator Setup Key before completing 72-hour activation.

## 2026-10-24 — Initial project documentation on GitHub
- Verified `manbir6-ux/TongNet` is a private repository accessible for writing.
- Replaced placeholder README with branded TongNet scope and official credits.
- Prepared FAQ, decision register, protocol sketch, security risks, history, research architecture, prior-art ledger, roadmap, progress and session handoff.
- Reconciled historic working name SIFAR Mesh → **TongNet** and native asset **TONG**.
- Recorded corrected creator-reported concept origin **2015**, not 2016; public disclosure reported for 2026.
- Recorded locked/no-manual-cancel 3h pre-trigger rule; subsequent 24h receiver claim; 72h sender-only recovery; proposed final network reserve transfer.
- Documented unsolved consensus, value, key-loss and legally sensitive forfeiture issues.
- **Next:** ask user about wrong recipient address *after Trigger but before claim*, then commit answer.

## Historic discussion (not evidence of commits)
- 2026-10-24: initial zero-fee, no-mining/no-traditional-staking vision.
- 2026-10-24: separate BlackBox and TongNet Authenticator proposed.
- 2026-10-24: payment timed rules iterated from 1-hour claim to 24-hour claim and from various recovery windows to additional 72h.
- 2026-10-24: sender explicitly declined pre-trigger manual cancellation; no Trigger leads to refund at 3h.
- 2026-10-24: model renamed TongNet; company-author ParmTech and creator Manjinder Singh specified; concept year corrected to 2015.

**Change-log rule:** Append dated, factual entries for every new design answer, code change, test and release. Do not claim a task is completed without evidence.
