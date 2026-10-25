# TongNet PR — proof-based engineering review

**Tracking Issue:** Closes #___ (ONLY if tests/review actually satisfy criteria); otherwise Refs #___  
**Worker/branch:**  
**Change type:** Spec / Rust code / consensus / wallet / privacy / security / operations  
**Owner-confirmed financial rights modified?** No / Yes with explicit ADR and owner confirmation link:  

## Before / after and trust boundary
What deterministic state invariant, secret boundary or observable behavior changes?

## Dependency and risk check
Issue prerequisites closed? Relevant `L-NN` long-term risks and U/ADR conflicts reviewed?

## Reproducible evidence
Actual command(s) executed and PASS/FAIL stdout excerpt, CI links and exact commit SHA:

## Adversarial tests
Replay / double spend / wrong chain / deadline race / 1/3 BFT fault / lost keys / stake-split and fee farm / relevant tests:

## Operational/financial consequences
Node state migrations? In-flight 61-day escrows? Slashing evidence age? Tokenomics? Wallet compatibility? Encryption key escrow?

## Handoff and log update
- [ ] `tracking/DAILY_LOG.md` appended factually
- [ ] `tracking/HANDOFF.md` exact resume step updated
- [ ] `tracking/CURRENT_STATUS.md` and `tracking/RISKS.md` if state changed
- [ ] `tracking/DECISIONS.md` and ADR if protocol decision changed
- [ ] No secrets/passwords/claim codes committed
- [ ] No unsupported 'secure/mainnet ready' claim

**Definition of Done:** Reviewed merge + tests + issue closure evidence. Documentation existence alone never means chain is working.
