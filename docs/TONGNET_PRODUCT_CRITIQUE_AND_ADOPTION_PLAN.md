# TongNet — Critical Product Review, User Trust, Payments and Banking Adoption Plan
**Date:** 2026-10-25 (Australia/Sydney)
**Status:** Proposed strategy and engineering research, **not** owner ratification of changes to previously confirmed immutable protocol rights; no live chain, bank, custody operation, source code, exchange listing, security certification, fiat redemption or proven originality.

**Reviewed alongside:** DECISIONS.md, TONGNET_FUTURE_ARCHITECTURE.md, MASTER_QA_RECOMMENDATIONS.md, PROTOCOL.md. This document is intended to expose severe flaws and propose testable improvements rather than praise every previous choice.

## 1. Problem statement: why would a real user switch?
A separate currency and blockchain must solve an identifiable problem better than existing payment rails. "Fast/secure/low fee" is insufficient: Solana already offers sub-cent consumer payments and fee abstraction, and Stellar targets ~5-second settlement with sub-cent costs. Ethereum L2s and Sui provide mature programmable accounts/onboarding. TongNet should not promise uniqueness of BFT, anti-Sybil committees, encrypted wallets, recovery or fast settlement individually.

**Proposed differentiated value proposition:** A payment-first **User-Controlled Payment Safety Network** combining (1) truly instant normal final transfers, (2) *optional* explicit two-phase protected payments with encrypted, transaction-bound claims, (3) secure recovery without custodial support bypass, (4) understandable bank-grade receipts/reconciliation/invoices for merchants, and (5) auditable fee sponsorship and decentralised safety/finality proofs, all behind one simple wallet. This is a potential differentiated bundle, not independently verified patent novelty.

### Critical conflict with user-confirmed old payment flow
The original user-confirmed protocol requires Send lock -> separate Trigger by 3h -> receiver Claim within 24h -> sender recover next 72h, no cancellation after Trigger and some irreversible DEAD/recovery rights. **If that were the ONLY way to pay, TongNet would be a poor everyday retail payment rail:** a cafe cannot wait for a separate trigger AND receiver Claim to confirm an ordinary $5 sale; merchants need clear reliable final settlement seconds, not multi-day expiry queues. The old flow must NOT be silently replaced or reinterpreted.

**RECOMMENDATION, OWNER APPROVAL REQUIRED:** Add a new opt-in **TongNet Instant Pay** transaction type, disjoint from the old **TongNet Protected Pay** type; original old rules remain exactly intact for Protected Pay. Instant Pay uses one transaction-bound approval, consensus-final atomic transfer, clear irrevocability, and immediate signed receipt. No extra manual Trigger or receiver Claim (though larger/unknown payees can trigger extra authentication before finalisation). No escrow forfeiture for the Instant Pay mode. Protected Pay continues old timings and extra keys as already chosen, while a future merchant escrow mode requires separately approved and fully specified rights. Making Instant Pay the default wallet UX is a RECOMMENDATION that is NOT currently user-authorised.

## 2. Payment product lanes (candidate)
| Lane | Who uses it | Sender experience | Actual settlement and protection |
|---|---|---|---|
| **Instant Pay** (NEW proposal) | Shops, friends, invoices, business payouts | Scan/enter, confirm once, finality | Short target finality after healthy BFT quorum; no receiver action or 24h Claim; no after-finality crypto reversal, ordinary fraud/payment-law questions remain |
| **Protected Pay** (CONFIRMED old flow) | Higher-risk deliberate payments, some escrow-like transfers | Send-lock <=3h, separate BlackBox Trigger, receiver 24h Claim, sender following 72h reclaim | Enforce strict finality before delay-adjusted effective deadlines, one-use keys, noncancellable after Trigger, only one claim; extreme UX complexity must be disclosed |
| **Merchant Request / Invoice** (NEW) | B2B and e-commerce | Signed request and verified merchant identity; user chooses Instant or Protected | Receipt/reconciliation, merchant SDK, refunds as new authorised transactions, no pretending crypto transfer is retractable |
| **Batch / Scheduled Payouts** (NEW) | Payroll, remittances, business | Multiple signed payments with limits/controls | Atomic batch semantics if same ledger; scheduler is not an unauthorised custodial operator |
| **Regulated Fiat/Stable Asset Interop** (FUTURE) | User wants amounts in AUD and other fiat | Interface displays fiat amount, issuer/exchange disclosure and FX quote | Licensed third-party issuer/redemption + settlement audit; on-chain TONG cannot be promised stable unless actual reserve, redemption and issuer obligations exist |

**Receipts:** Plain language "Prepared", "Queued—NOT PAID", "Network Final—PAID", "Protected Awaiting Trigger", "Protected Awaiting Receiver Claim", "Sender Reclaim", "Disputed/Protected" with exact finality proof. No fake "instant" when only queued. Merchants should only deliver goods on suitable finality and mode.

## 3. Wallet UX and trust requirements
- Onboarding with a *simple*, auditable standard hardware-backed signing model and explicit recovery warnings; do not force a casual user through BlackBox/Authenticator *unless the selected transaction mode requires it*. The confirmed 72h unenrolled wallet DEAD rule applies where that legacy wallet type is used. **Separate new fast wallet profile** needs explicit new product approval. No stealth downgrade of security.
- Enforce phishing-resistant address verification/receiver aliases through multiple independent proofs and destination fingerprint; never trust human-readable name directory controlled by one server.
- Use transaction-bound hardware backed confirmation, minimum readable recipient and value, rate limits, high-risk prompts, no clipboard trust, open-source verifiable client releases.
- Non-custodial keys create real irreversible loss risk. Offer independent encrypted backups and verifiable backup drills, without claiming account-reset or social recovery exists inside old immutable rules.
- Fee transparency before confirmation; any "free" usage needs sustainable sponsor quota and anti-spam governance, no hidden spread/fees.
- Provide independently verifiable finality certificates and public incident/security history; independent external crypto and formal protocol audits before asking users to trust funds.
- Accessibility, fast low-bandwidth UX, lightweight clients, self-hostable access and real language localisation.
- Preserve BlackBox E2E confidentiality with multi-node resilient delivery; privacy claims limited to what is demonstrably hidden. Off-chain IP/timing metadata and public amount tracing are attack surfaces.

## 4. Network architecture and node/validator count
**Primary implementation:** Rust; deterministic-finality BFT research core; parallel ingress and nonconflicting execution; decentralised network transport without mandatory owner API/CDN/cloud; network timestamp/claim proof and safe epoch reconfiguration. Optional DAG should be separately tested against a simple BFT baseline before added. Standard audited cryptography and libraries preferable to unique experimental primitives.

**Validator count:** no magical one-number answer. Four nodes in an isolated simulator may model f=1; 7-25 independently controlled testnet validators test faults/regions; a genuine launch candidate could target **~25–100 distinct eligible operators** as an *aspirational design planning range*, subject to legally viable independence and latency/cost benchmarks. Each operator needs genuine independent control, not 100 aliases belonging to one company. In a 25 equal-power BFT set, 17 votes exceed 2/3 and the classic safety model tolerates up to 8 Byzantine operators, **only if assumptions of genuine independence, fixed membership and sufficiently correct BFT protocol hold**. Actual validator voting weights, shards, committee overlap, network synchrony and join/exit remain unspecified; 25–100 is NOT user-confirmed. Operator distribution measured by jurisdictions, ASNs, cloud providers and control clusters; publish concentration and censorship data. Two partitions must not each bootstrap contradictory quorums.

**Security critical:** no 'fully automated validator selection' without an independently defensible Sybil-cost model. Candidate limited bonded proof + independent operator attestations, publicly reproducible eligibility rules and committee randomness. Pure wealth voting would centralise power; signature alone never prevents fake independent operators. Stop malicious validators only with demonstrable evidence; quarantine cannot be weaponised to strip quorum. Predetermined standbys cannot create a second quorum after a split. If safe quorum impossible, stop finality and keep queued transactions NONFINAL.

**Network Delay Calculator:** user-confirmed one-to-one time allowance for ALL affected timed operations from a hybrid global+individual network proof. Do not *add* overlapping intervals. Global complete-outage duration and individual delay cannot universally be known precisely under asynchronous censorship and split clocks. If entitlement is disputed, deterministic Protected Suspense must preserve funds without irreversible opposing outcomes, but avoid permanent capital freeze by proving safe exit and verifying liveness; not production ready.

## 5. Coin/tokenomics: what number of TONG coins?
**The count of coins does NOT create real value.** Price, liquidity, utility, distribution fairness, absence of hidden minting, and sustainable validator incentives matter. Do not promise profit, guaranteed scarcity value, or backing by Network Reserve.

**Candidate only — not approved supply:** use **1,000,000,000 maximum TONG** as a human-friendly design placeholder, **9 decimal places**, so smallest unit is 10^-9 TONG. This number is arbitrary, not mathematically optimal: may choose 100m or 10b after fee/liquidity/validator/security economics simulations. Genesis supply, vesting, circulating schedule, unlocked allocation, validator bond, community rewards, sustainable emissions/fee burn and whether eventual hard cap is even compatible with security budget MUST be independently modeled BEFORE choosing genesis. No automatic owner mint/backdoor or central right to change cap. Recommend **no public token presale or guaranteed-investment messaging** until legal classification and audit.

**Separate types of value:** TONG native network unit is not AUD and has variable purchasing power absent legally verified redemption. Retail users overwhelmingly need price stability. Support regulated AUD/stable asset integrations or users' chosen supported assets through legally approved on/off ramps, transparent 1:1 redemption where issuer contract truly warrants it. A 'banking' product also requires KYC/AML at regulated entities, payment disputes, custodial models and different customer rights.

## 6. Banking claims vs platform reality
**TongNet could become a payment / settlement rail and provide finance-facing APIs**, not automatically a licensed bank. Deposits, lending, interest, fiat account numbers, direct debit, card network access, chargebacks, deposit protection and trusted fiat redemption require regulated institutions, licences, third-party interoperability and specific consumer obligations. There is no honest fully-decentralised exemption from local laws. Start non-custodial payments, merchant payment SDK and wallet; partner with registered payment/exchange providers for fiat/on/off ramps. Banking-like dashboards and invoices are feasible; 'insured deposits', 'bank account' and 'instant fiat conversion' cannot be promised.

**Australian regulatory reality (2026):** AUSTRAC requires applicable virtual asset service providers to register prior to operating, with AML/CTF obligations and travel rule where applicable. ASIC considers the economic substance and use of tokens/platform arrangements, including some stablecoins and non-cash payment facilities, for Australian financial-product licensing. Enforce privacy minimisation while retaining data legally necessary for regulated providers. Seek Australian financial services and payments counsel BEFORE sale, custody, exchange, fiat rails or live launch.

## 7. Aggressive external product comparison (as of 2026 research)
- **Solana:** already promotes sub-cent fees, subsecond securing, parallel execution, stablecoin checkout and sponsored fee UX. TongNet cannot claim uniquely fast/cheap.
- **Stellar:** already markets ~5s final settlement and less-than-cent fee, regulated asset issuance and cross-border use. TongNet cannot claim uniqueness for remittance.
- **Sui:** already offers familiar OAuth-based zkLogin, sponsored transactions, fast asset handling. TongNet cannot claim simple login or sponsor as first-ever.
- **Ethereum L2s:** substantial application ecosystem and cheap execution; their tradeoffs include central sequencers in some rollups. TongNet must still justify adoption over established network effects.
- **Bank rails:** regulated recourse, stable AUD accounting, existing merchant integration. TongNet must demonstrate an objectively better experience in a chosen niche rather than promising to replace bank consumer protection.

## 8. Tough, adversarial questions and answers
1. **Why would I use TongNet instead of Solana/Stellar?** Only if the ONE-app instant/optional-protected payments + recovery + business receipts becomes demonstrably safer/easier/cheaper; no reason to migrate on whitepaper promises.
2. **Does two-step Send/Trigger make shopping cumbersome?** Yes as universal default. Recommend separate Instant Pay alongside unmodified Protected Pay.
3. **Is 24h Claim an advantage?** Only for deliberate protected transfers, not ordinary checkout. It can strand funds and create merchant uncertainty.
4. **Why trust custom new crypto?** Don't. Use audited standard primitives and external consensus evidence.
5. **What stops 10k fake validators?** Not signatures/rotating committees alone. Test real scarce eligibility, operator concentration and takeover cost.
6. **What if owner disappears?** Base chain, key ownership, bootstrap and governance must continue across independent providers with no owner-controlled master switch.
7. **What if malicious majority colludes?** BFT assurances fail above stated threshold; publish trust assumptions and fraud proofs where possible; no 'unhackable' claim.
8. **What if chain partitions?** Only actual quorum can finalise; other side stops. No fake double finality to improve availability.
9. **What if delay meter lies?** Evidence from independent nodes, union-of-overlap, threshold consensus; protected disputed escrow, formally proved resumption needed.
10. **What if funds unclaimed 96h?** Current forced Network Reserve forfeiture is not legally/ethically deployable as is; seek owner approval of safe refund/escrow policy.
11. **If lost device/keys are permanently DEAD, will ordinary users trust it?** Many won't. Need highly visible risk warnings; suggest a separate auditable recovery profile, but keep confirmed old irreversible rules unchanged until owner chooses.
12. **How can transfers be zero fee without spam?** A genuinely funded sponsorship quota and transparent, tiny paid overage; validator economics audited in fiat units.
13. **How does TONG have value?** Demand for useful payments/services, accessible liquidity, fair issuance and independent security; ticker and arbitrary supply do not create value.
14. **Can it replace banks?** Not without compliant regulated partners/licences for deposit and fiat rails; payment settlement rail first.
15. **What about chargebacks and fraud?** On-chain finality is not consumer dispute resolution. Voluntary refunds, merchant dispute infrastructure, legally mandated remedies via licensed providers where applicable.
16. **What if user wants rupees/AUD, not volatile TONG?** Asset interoperability and transparent conversion via regulated providers; don't pretend TONG is stable.
17. **Is it new, not copied?** Nothing automatically novel. Patent/prior art/licence check; strive for original design tradeoffs and UX while reusing safe public standard components.
18. **Why would merchants integrate?** Stable settlement asset, clear invoice/receipt APIs, transparent finality, cheap sponsored costs, POS plugins, prompt payouts and compliance support.
19. **Would 1B TONG be better than 21m?** No intrinsic difference for usability/value, decide based on denomination and actual economics; recommended number provisional.
20. **Will 1k TPS be enough?** Only for selected market niches. Real transaction mix, peak load, geographic validator distribution, state size and recovery latency must be measured; future sharding requires shared-spend safety.

## 9. Initial target market and product-market fit
**Start with one tractable wedge:** opt-in protected P2P cross-border transfers or low-fee invoice/merchant payouts in a jurisdiction with legal clearance. Validate real demand from 20–50 independent pilot users and 5–10 genuine merchants, not self-generated wallet counts. Measure signup completion, time-to-first-transfer, confirmation speed at P50/P95/P99, abandonment at Trigger/Claim, recovery task completion, user mistakes/loss, uptime and real full cost per success. Run testnet exclusively at first. A proof-of-use product may be built as an application atop established rails for validation before deciding that custom Layer-1 costs are warranted; this avoids unnecessarily promising a new coin to users without proven need.

## 10. Concrete recommended product improvements (approval status)
| Recommendation | Why | Approval category |
|---|---|---|
| Two payment modes: Instant Pay + original Protected Pay | Everyday payments need instant and simple; protected rights retained for power users | **NEW mode — owner decision required** |
| Signed receipts, business invoices/merchant SDK, honest status labels | Trust and practical integration | Engineering proposal, can design in testnet |
| User-selectable recovery profile for new wallet class | Irrevocable DEAD/immutable destination risk drives loss | **Would modify user rights — owner approval required** |
| Replace forced reserve-forfeiture with safe returned/protected funds and opt-in sponsorship | Prevent involuntary loss, legal exposure | **Critical owner approval and legal review** |
| Hybrid verifiable operator eligibility, BFT quorum and permissionless rollout | Defensible security not merely many pseudonymous nodes | Implement confirmed direction, formal proof required |
| 1B TONG supply cap + 9 decimals | Denomination working baseline, economically arbitrary | **PROVISIONAL / not minted or chosen** |
| Stable-asset / fiat integration only with licensed partners | Needed for merchant pricing, real banking | Business/financial legal approvals needed |
| Sustainable fee sponsorship + minimum overage cost | Zero-fee promises otherwise enable denial of service | Engineering recommendation |
| Audited open verification, incident reports, decentralisation metrics | Trust must be independently demonstrable | Essential testnet / launch gate |
| Rust immutable shared financial core plus native UIs | Memory safety and cross-platform consistency | Already owner-delegated language |

## 11. Staged development and go/no-go gates
**Stage 0 — Safety architecture:** freeze canonical financial rights, classify each as confirmed vs proposed; choose business wedge and legally suitable asset use; resolve reserve forfeiture risk; no public TONG selling. Define closed core model with Instant/Protected separated IF approved.

**Stage 1 — Rust deterministic simulator:** verify spend conservation and exactly-one receipt/claim, no mutually final partitions, immutable DEAD/recovery rules, delay extension/race, fee arithmetic and schema versioning with property-based/fuzz tests.

**Stage 2 — Multi-node adversarial testnet:** real BFT integration, dynamic committees/backup validators, blockchain access without central RPC, live fault injection, honest throughput/latency, exact network operation cost accounting.

**Stage 3 — Wallet and merchant pilot:** simple client, signed QR invoices, per-mode receipts, E2E BlackBox, independent keys, multi-device recovery drills and fake-money customer testing. Compare with existing Solana/Stellar integration product before proceeding to a custom L1 full launch.

**Stage 4 — Legal and security clearance:** separate cryptography/consensus, wallet, economic, privacy and consumer protection audits. AUSTRAC/ASIC status and licencing assessed with counsel, independent operator incentives funded. Public reports and disclosed limitations.

**Stage 5 — Measured mainnet:** modest limits, independent validator concentration reports, public block explorer and reproducible Rust builds, funded support/incident playbooks. Never claim perfect decentralisation, lowest fees or world's first absent proof.

## 12. References and attribution
- Owner/company: ParmTech; original concept creator/developer: Manjinder Singh; concept origin 2015 creator-stated, first public disclosure 2026 creator-stated (not independently verified).
- Solana payments & sponsored fees: https://solana.com/docs/payments
- Stellar payment/fees: https://developers.stellar.org/
- Sui zkLogin: https://docs.sui.io/sui-stack/zklogin-integration
- Ethereum scaling: https://ethereum.org/roadmap/scaling
- CometBFT BFT proof: https://github.com/cometbft/cometbft/blob/main/spec/consensus/consensus.md
- AUSTRAC VASP rules (2026): https://www.austrac.gov.au/industry-and-business/your-industry/virtual-asset-service-providers/virtual-asset-service-providers-overview
- ASIC financial-product analysis: https://www.asic.gov.au/regulatory-resources/digital-transformation/digital-assets-financial-products-and-services
- BIS monetary integrity discussion: https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system

**IMPORTANT:** This document records recommendations NOT implemented/verified operations, and is neither investment advice nor assurance of uniqueness or banking licence. Owner-confirmed product rules are preserved pending explicit replacement approval.
