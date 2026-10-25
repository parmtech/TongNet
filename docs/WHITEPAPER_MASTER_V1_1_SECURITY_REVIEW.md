# TONGNET — MASTER NETWORK WHITEPAPER V1.1 / ADVERSARIAL REVIEW
## Corrected single-native-coin architecture | Security-reviewed DESIGN baseline, not independently audited

**Date:** 25 October 2026 (Australia/Sydney)  
**Project author:** ParmTech  
**Original concept creator and developer:** Manjinder Singh  
**Origin story:** Concept originated 2015; first public disclosure 2026, both creator-reported rather than independently verified.  
**Document:** Version 1.1 adversarial logic audit and revised architecture-decision whitepaper; **NOT deployed technology, audited security, an offer of securities, a completed cryptocurrency, or a guarantee of monetary value.**
**Authority rule:** The user's recent explicit product decisions are **CONFIRMED**. The many numerical and engineering decisions delegated to the architect in the latest request are **SELECTED REFERENCE BASELINE (PROPOSED)** until tests, independent audit and documented owner ratification. Research blockers are labeled **BLOCKED**. Earlier stale Trigger/72h/frozen-recovery statements do NOT override latest rules.

> **One-sentence vision:** TongNet is an independently verifiable, Bitcoin-purpose single-currency network whose native TONG coins use a narrow, purpose-built secure two-party payment protocol with explicit Sender BlackBox approval, low accountable fees, bonded user-operated BFT validation and privacy-preserving active disaster-recovery mirroring.

---

> **AUDIT CORRECTIONS V1.1 (supersedes V1.0 engineering guesses):** Fee budget must pay for each of 3 state transitions, not offer adversary unlimited unpaid CLAIM attempts. Do not lock TONG before the Sender securely persists high-entropy K_R. Coin supply cap 100m is *only a reference candidate*; 12m genesis, 17.6m first-four-year emission and 50%-potentially-related genesis allocations are **withdrawn, not approved**. The 2 MiB/4sec worst-case saturation implied ~45.3GB/day and ~16.5TB/year before indices, too high for a low-fee small-node target; revised experimental baseline 256KiB/6sec implies ~3.77GB/day and ~1.38TB/year maximum just for raw block bytes (still substantial). 100 actions/s was a target not proven with 64 BFT nodes; use a 20-actions/s starting adversarial test gate. Recovery of **validator stake cannot instantaneously evict an active signer from its committee**. Parent encrypted archive conditional key-release, late Sender K_S, exact network delay credit, post-60d forfeiture, initial staking distribution and legal treatment remain **HARD LAUNCH BLOCKERS**. Detailed findings below and in the associated V1.1 logic-audit report.

# 1. Nonnegotiable Scope & Design Philosophy

**Owner-confirmed:** Standalone TongNet blockchain, one native monetary asset **TONG**, self-custody TongNet Wallet, Sender BlackBox, Authenticator, chosen bilateral trusted-counterparty payments and optional active recovery wallet. No Ethereum EVM, public arbitrary smart contracts, third-party token creator, dApp marketplace, social platform, music platform, forced deal arbiter, admin fund override or dedicated ASIC Proof-of-Work mining. Necessary wallet, node, explorer and backup interfaces are first-party infrastructure rather than public dApps.

Principle order: **(1)** never incorrectly release or duplicate funds; **(2)** no unbounded operator or private-key trust; **(3)** simple publicly auditable rules; **(4)** reliable uptime and recoverability; **(5)** low transparent fee; **(6)** improve measured throughput without degrading security. "More secure than Bitcoin" is an aspiration, not established fact. Never market absolute invulnerability, mathematically zero risk, guaranteed execution latency, guaranteed reclaimability from lost keys or an unconditionally fee-free chain.

TongNet is an open cryptocurrency, **not a bank, fiat-backed stablecoin, investment with guaranteed yield, or anti-fraud marketplace**. Two voluntarily trusting parties are responsible for non-cryptographic delivery of goods/services. Sender can refuse final approval, so off-chain fair exchange is not guaranteed.

# 2. Design Choices & Explicitly Rejected Alternatives

| Dimension | Reference decision and reason |
|---|---|
| Monetary function | One native TONG coin; fixed on-chain currency logic, not a general-purpose chain |
| Ledger | **Deterministic account-based native state** with monotonic nonces and segregated balance categories. Easier to express LOCK, CLAIM, FINAL_ACCEPT and Recovery than general-purpose UTXO scripts, while retaining full public validation. UTXO comparison stays a measurable alternative. |
| Consensus | **Mature BFT engine** such as version-pinned CometBFT; stable stake-weighted validator set per epoch. Do not invent new chain finality cryptography for v1. |
| Stake | Explicit opt-in **bonded PoS**, independently slashable validator signing keys. Merely holding coins or having many addresses earns no consensus votes. |
| Transaction-work | Sender INITIATE, Receiver CLAIM_REQUEST and Sender BlackBox FINAL_ACCEPT may perform **bounded off-critical-path check of an unrelated finality proof** and generate auditable receipts. Neither sender nor receiver thereby votes on their own transaction; PoTP does NOT secure canonical state. |
| Fees | Small resource-aware fee plus earned separate validator rewards. Bond is refundable *after safe unbonding subject to slash*, ordinary network fee is not automatically refunded. No direct rewards for fake self-transfer. |
| Identity | Pseudonymous self-custody by default. No public biometrics/fingerprint register and no one-phone-one-vote assumption. |
| Device | Wallet may be offline; **online full validator** must continuously run on a computer/server, phone as wallet/light verifier, optional delegated staking only in later gated phase. |
| Governance | Public time-locked on-chain protocol changes; no single ParmTech/creator backdoor. |
| Future evolution | Versioned changes, reproducible builds and tested cryptographic agility, including post-quantum research; no unfounded quantum resistance claim. |

Prior PoW has a substantial multi-year record of use and a different economic trust model; replacing it does not automatically increase security. Pure transactions-only / no always-online validators is **rejected as insecure/insufficiently live** without independent Sybil-resistant scarcity. A finite collection of free pseudonyms and 10 self-chosen votes is not defensible.

# 3. Reference Deployment Profile (Design Targets, NOT Measured Capabilities)

| Parameter | Selected baseline / gate |
|---|---|
| Development localnet | 4–7 validators, disposable zero-value TONG |
| Public attack testnet | First 21 independent volunteer validators; expand to 64, plus ≥32 rotating eligible standbys |
| Mainnet release GATE | Aim 64 active consensus validators from genuinely separate operators, ≥32 eligible standbys, ≥128 reachable independent full nodes and ≥16 independently hosted archive replicas before inviting material user funds. **Counts never substitute for stake distribution or independent control.** |
| Growth policy | Raise to 96 or 128 active validators only after latency, geographic independence and quorum safety tests. No arbitrary expansion on marketing grounds. |
| Vote threshold | **>2/3 of active epoch voting power** under precise BFT assumptions; if >1/3 offline/faulty, liveness can halt. Never lower threshold during partition. |
| Voting power | Bonded TONG weighted by audited formula; splitting one stake over 100 accounts does NOT multiply voting chances. Wealth concentration remains a meaningful vulnerability. |
| Minimum self-bond trial | **NO hard-coded mainnet bond** until coin distribution, value-at-risk and external attacker acquisition costs are known; testnet may choose arbitrary faucet-denominated bond. A fixed 25k TONG is NOT a security guarantee. |
| Staking activation trial | 7-day reference maturity, epoch-bound activation, registered consensus key, verified synced online node; no age-based multiplying vote power. |
| Exit trial | 28-day **test-only** slashable unbond after duty ends, which MUST exceed the effective evidence age and historical fault challenge period; align to evidence window/settlement audit before adopting. |
| Epoch / committee | 24-hour epoch for stake snapshots / activation; use one globally consistent validator set per consensus height, formally quorum-intersecting transitions, not independent committees finalising each payment. |
| Block target | **6-second** nominal first testnet target, not guaranteed; observed finality under network health only. |
| Block bytes target | Initial **256 KiB max** and resource gas with 512 KiB only as a separately benchmarked upper experiment; profile network and BFT overhead before adjustment. |
| Performance **go/no-go** | Sustain ≥20 *native state-action* tx/s (not 20 completed 3-step payments/s) in 5-region hostile test scenario with p95 event finality under 20 seconds during healthy conditions, 72h soak, 0 inconsistent finality, without unbounded resource queues. This is a **test target**, not a claim of current TPS. A full payment often has 2–3 finalised actions, so payment/s lower. |
| State/network | Authenticated Merkle state commitment, multi-peer bootstrapping, untrusted full/light peer verification, deterministic snapshots, limited pruning with archive incentives |
| Hardware trial | For validator: modern 4–8 CPU cores, 16–32 GB RAM, NVMe SSD, reliable symmetric internet and guarded signing key. Benchmarks determine real minimum; ASIC mining hardware unnecessary. |

**Launch gate:** Resist concentration by documenting effective connected operator clusters; no one known-controlled cluster >10% voting weight and no known small colluding cluster with ≥1/3. This is a screening and transparency target, **not a cryptographic guarantee of independence**. If initial distribution or operator diversity cannot meet these thresholds, delay permissionless mainnet rather than pretend genesis bonds create trust. Test stake-acquisition economics, weak token market conditions and bribery/borrowed-stake attacks.

# 4. Consensus Protocol & Validator Operations

Use a **reviewed round-based BFT engine**, e.g. CometBFT as consensus/P2P layer (Go binary) with **Rust deterministic ledger engine** over audited ABCI++/equivalent interface. Existing Rust-primary owner decision applies to TongNet native logic and wallet, but does not mandate rewriting reviewed BFT internals in Rust. Version-pin, check software licences and supply chain; validate engine compatibility, state-sync and voting-key features. Do **not** claim CometBFT is itself a full staking ledger, tokenomics or application.

Consensus events: mempool ingress → parallel stateless/prevalidation → propose → independent validator state-check → prevote/precommit → >2/3 certificate → deterministic app finalization → state-root / receipts. Never mutate canonical state on CheckTx or tentative proposal. All validators re-execute native state transitions deterministically.

Staking lifecycle: **UNBONDED → BONDING_PENDING → ELIGIBLE → ACTIVE_DUTY → EXIT_PENDING → UNBONDING_SLASHABLE → WITHDRAWABLE**. Stake locked distinctly from liquid TONG, BlackBox secret, pending escrow, and recovery wallet funds. Self-bond requires owner-signed opt-in; registered validator consensus signer separate from ordinary spending signer and Authenticator. Cannot convert merely-aged balances into votes without consent. Reserve voting eligibility snapshot before publicly knowable proposer randomness to reduce grinding.

Double-sign / provable equivocation: quarantine node, preserve evidence, slash precommitted percentage after an evidence-valid final state transition, prohibit that signer from silent reuse. Trial schedule: evidence-backed equivocation causes loss of some or all attributable bonded collateral in a simulated parameter set; **NO mainnet % is selected** before modelling attack rewards, stake market liquidity, evidence age and slashing causality. Normal short outages earn 0 rewards and can trigger orderly deactivation but should not automatically burn user stake. Never assume punishment deters a 2/3-capital adversary. **Never slash based solely on reported geography, failure to click fingerprint, third-party allegation or no Internet.** Significant evidence retention/unbonding interaction must be implemented.

No automatic "return coins on loss" for validator bond before exposure period ends. No whitelist-only permanent control. Validator selection randomness is not derived from manipulable Sender transaction hash. A majority-wallet count does not replace bonded-weight quorum. On 60/40 network split neither partition can independently create new validator set and claim finality; allow service outage rather than contradictory money history.

# 5. Network Actors & Data/Trust Boundaries

- **Ordinary Wallet / user:** hold/spend unlocked TONG, initiate and claim payments, locally sign, store secrets. Not required to be validator and may go offline.
- **BlackBox:** locally protected secret inbox with sender/receiver claim secrets and private sender acceptance, plus signed state receipts and separate sealed recovery archives.
- **Full validating node:** downloads and verifies chain and app state, relays independently; no stake and no consensus signing privilege needed.
- **Bonded consensus validator:** full online node + dedicated signer + slashing bond + vote power; checks every finalised native state action.
- **Standby eligible validator:** synced full node and opt-in bond but outside active consensus snapshot, joins only under formally valid epoch reconfiguration.
- **Archive / mirror relay:** stores historical blocks or encrypted BlackBox ciphertext, not plaintext or user signing authority. Proof of ciphertext availability remains a researched liveness issue.
- **Observer/light client:** verifies signed finality certificates and Merkle proofs from multiple untrusted endpoints, with correct trust-period expiry.
- **Governance electorate:** owners/validators under defined multi-stakeholder transparent change mechanism; no privileged unilateral hidden update or refund key.

**Three spending domains must stay separated:** financial Wallet private key; Authenticator / BlackBox sender-accept capability; validator consensus key. A compromised validator server alone must not spend user TONG or decrypt a parent archive.

# 6. Ledger, Balances and Native Operations

TongNet v1 chooses **account balances with nonces and event-indexed deterministic native escrow state**. Per wallet state includes spendable liquid, escrow-locked outbound value, slashable validator-bond shares/withdrawal rights, protocol-owned rewards and time-bounded entitlements. Do not count one unit of TONG in more than one category.

Native transaction types only:
\`CREATE_WALLET\` (registration/proof-of-control and Authenticator activation), \`TRANSFER_LOCK\`, \`RECEIVER_CLAIM_REQUEST\`, \`SENDER_FINAL_ACCEPT\`, \`SENDER_RECLAIM\`, \`STAKE_BOND\`, \`VALIDATOR_REGISTER\`, \`VALIDATOR_EXIT\`, \`UNBOND_WITHDRAW\`, \`EVIDENCE_SUBMIT\`, \`RECOVERY_PAIR_REQUEST\`, \`RECOVERY_PAIR_ACCEPT/REJECT\`, \`RUN_DISASTER_RECOVERY\`, \`PARAM_UPGRADE\` and safe maintenance. The exact wire formats/versioned byte encodings are implementation deliverables.

No Turing-complete external contract interpreter. Every action signs canonical domain-separated \`chain_id/version/type/nonce/source/target/amount/escrow_id/expiry/state_reference\`. Use deterministic integer base units (no floating money maths), idempotent transaction IDs, replay protection, single-spend invariants, state-root commitments and strict object-size limits.

A lightweight ordinary non-escrow send mode is **NOT owner-confirmed**; v1 defines bilateral three-step payments as primary. If introduced later, it must be explicitly optional and separately approved, never silently bypass FINAL_ACCEPT.

# 7. BlackBox Three-Step Payment (OWNER-CONFIRMED DIRECTION)

The current protocol has **NO separate three-hour Trigger**. There is no automatic receiver settlement merely by knowing code or showing a claim request.

**Step P1 — INITIATE / BFT-final LOCK:** **Before** sending signed LOCK to the network, Sender BlackBox MUST generate, integrity-check and durably back up an encrypted high-entropy one-use credential **K_R** or ephemeral signing key; the LOCK binds its public verification commitment to exact receiver/escrow/chain. Sender spending wallet then signs exact TONG amount, bound receiver, fee budget and nonce. Validators verify spendability and atomically finalise escrow. **Only after FINAL LOCK** may Sender reveal/share K_R to Receiver using the trusted out-of-band channel. If local secret preparation/persistence fails, BLOCK LOCK broadcast instead of creating unrecoverable locked funds. A digital signing credential allows Receiver to prove secret possession with a signature while keeping secret off-chain; required extra Receiver wallet signature prevents address diversion. Human-entered 6-digit code does NOT qualify as secure public-verifiable commitment without rate-limited protected protocol. Optional bounded unrelated finality-proof verification may occur outside the payment-critical path.

**Step P2 — RECEIVER CLAIM_REQUEST:** Exact designated Receiver wallet submits domain-separated own wallet signature plus ephemeral K_R private-signing-key proof against the LOCK-committed public one-time key (or separately audited proof system). Raw K_R never enters chain, transaction hash preimages or telemetry. One valid receiver-request transition per escrow by default; no fee-draining retries. On-chain receiver claim event is **NOT payout**, and does not permit another address or repeat claim. Protect offline guessing, reuse, transaction ID collisions and targeted denial-of-service. Transport signed claim notification to Sender's authenticated BlackBox.

**Step P3 — SENDER BlackBox FINAL_ACCEPT:** Sender must consciously approve exact escrow, receiver, request, amount, expiry and chain, using separate authenticator/device capability as defined. Only a final BFT-validated canonical approval settles to Receiver once; an unapproved or expired claim must NEVER settle. No force-release by dispute resolver, validator operator, admin or network reserve.

**Timing:** Select network-final \`LOCK\` as **candidate t0** for receiver exclusive nominal **24 hours** (latest owner specified 24h, but original anchor not explicitly ratified). Then original Sender gets **60 complete additional days** of exclusive manual reclaim. There is no automatic 24h refund. Sender reclaim requires S signing authority plus distinct protected **K_S** under the previously confirmed owner policy. Initial K_S only generated in S BlackBox *after* 24h creates a severe unrecoverable-lost-BlackBox problem; changing to a recoverable precommitment or protected delayed derivation is **BLOCKED pending explicit approval**. Do not misrepresent that encrypted backups can restore never-created K_S. A 24h+60d expiry is nominal; verifiable network-caused delay credits remain safety-critical research.

Once Sender recovery right ends, owner's prior proposal to forfeit unclaimed locked TONG to Network Reserve is **RECORDED OWNER INTENT, BUT NOT SAFE FOR REAL-MONEY DEPLOYMENT**. Default research implementation keeps funds in \`PROTECTED_SUSPENSE\` with no third-party spending until exact legal/consent/fault safety protocol is agreed. This is a production blocker, not a covert owner requirement rewrite.

# 8. TongNet Transaction Participation (PoTP) — Reciprocal Work

At each of the three BlackBox stages, a consenting wallet may verify a **random, independently selected, unrelated FINALIZED** certificate/state inclusion proof, producing a signed bounded \`AUDIT_RECEIPT\`. A small client-local nonce puzzle may supplement dynamic anti-spam admission if fair across weak devices; benchmark before enabling. No automatic reward for clicking Accept, creating wallets, self-sending money or verifying only own payment. Phone-based participation must not leak K_R, K_S, spending key, validator signer or sealed parent encryption material.

**Invariants:** PoTP receipts are **not consensus votes, stake, human identity, new TONG issuance, or permission to change canonical history.** Their usefulness may include peer audit, client proof checking, and measurable/independently assigned small service credits, funded under explicit budget; do not advertise them as Bitcoin-work replacement. Do not add mandatory extra puzzle latency to a time-critical FINAL_ACCEPT. No circular requirement that one payment must wait for future payments to create a witness.

If zero future transactions arrive, validators remain online, keep state and can finalize first new activity. Truly only transaction-active peers at each moment is not sufficient for 24/7 decentralized availability.

# 9. Fees, Work Rewards and Spam Economics

Choose **small transparent Fee + Earn**, NOT unconditional refundable per-payment fee. The **validator bond** is a refundable/slashable capital guarantee after exit; the **network fee** pays network resources; a **reward** is compensation for verified independent consensus duty; these are distinct.

Recommended **resource-priced sender prepaid escrow fee budget**:
- On LOCK sender authorizes maximum three-stage budget, priced by signed bytes + signature proofs + persisted escrow size + state actions; the Receiver can submit legitimate CLAIM_REQUEST without needing to own dust TONG. Unspent budget is returned on normal completion/expiry under safe settlement rules.
- Dynamic **base-price floor and bounded congestion multiplier** adjust at finalized epochs with queue / block occupancy, parameter change governance and a hard user-visible maximum. Priority cannot be bought to bypass manual consent or finality proof.
- **Candidate budget only:** 80% of collected verified fees for qualifying consensus service, 10% for independently verified archive/availability, 10% for accountable on-chain security reserve. These are NOT entitlements; archive proof/payment and negative-budget cases require simulation before use. Exact fractions are proposal values and cannot be trusted unless service proofs genuinely bound payments to work, treasury governance is decentralized and overhead measured.
- Optional *non-transferable* PoTP earned-service rebate funded from capped transparent treasury budget; cannot convert it into voting power, extra crypto asset, or guaranteed return. Service receipts for unrelated work and nonce challenges can be gamed; run fake-wallet farming simulations.
- Reward paid from collected fees and separately defined monetary issuance, if approved; no magical fee refund or stable dollar value. Under weak network demand, issue/treasury subsidy may be needed; once subsidies end, fees must cover sustainable service cost.
- Rate limits per peer/IP alone are not Sybil security; use per-resource charges, bounded queues, mempool admission, fee sponsorship quotas guarded by external-cost abuse limits, and transaction-receipt fairness. Avoid expensive on-chain failed-code spam.

Important: 3 actions can be >3 times resource load of one typical transfer after proofs/storage. Cost the whole lifecycle, not 1-TONG sender debit only.

# 10. TONG Monetary Policy — Balanced Economic Reference (NOT OWNER APPROVED)

**Reference cap candidate ONLY:** 100,000,000 TONG and 8 decimal places (base unit 10^-8), with no peg to AUD/USD and no promised exchange value. **No mainnet monetary emission or genesis allocations are approved**; design cannot safely freeze allocations without an independently audited security budget, token distribution, reserve constraints and economic stress tests. Monetary invariants are no arbitrary mint, no negative balance, every emission under publicly fixed maximum and separately audited fully deterministic issuance. This cap is a selected candidate requiring owner consent/economic and legal scrutiny, not an already circulating asset.

**REJECTED V1.0 EMISSION DRAFT:** The old example of 12m genesis followed by up to 17.6m issuance over the first four years produces gross first-era issuance equal to **146.7% of the original 12m genesis supply**, an unbalanced bootstrap/incentive assumption. Do NOT implement that schedule. Replacement: model several explicit issuance alternatives (fixed supply with transparent vesting vs capped declining subsidies vs low capped annual security budget), taking validator actual expenses and bond economics into account. Select an emission function ONLY after credible attack-cost/market/liquidity and public legal review. For testnets, coins are valueless and issued by documented faucet; they are not mainnet allocation precedent.

**REJECTED V1.0 GENESIS PERCENTAGE DRAFT:** Previously suggested 25% bootstrap validator + 15% treasury + 10% team could place **50% of initial supply in foundation/related programme influence**, creating material early staking-capture risk even if formally vested. No genesis distribution ratio is selected in V1.1. Before mainnet, require independently governed, transparently signed recipient commitments, founder/treasury staking restrictions, time-locked allocations, genuine community acquisition route, anti-Sybil/fairness disclosure and effective independent voting-power distribution stress tests. If a credible distribution cannot be found, **do not launch**. Testnet faucet issuance has no financial value.

Nonprofit/offchain foundation, exchange listing, future investment return, market cap, fiat price, network reserve backing and regulatory status **are not inferred**. All financial projections are scenarios only.

# 11. Wallet UX, Activation, Identity and Keys

**Wallet activation owner rule:** first-time Authenticator activation window 72 hours, after which unactivated wallet becomes irreversibly DEAD. Prevent incoming monetary funding **before activation** or explicitly reject it atomically to avoid destroying funds by expiry; this protection is a selected implementation safeguard for an older owner rule, with exact stale-wallet semantics and backup safety to be tested.

Locally generate main spending key, independent BlackBox sender-accept key and Authenticator seed/master, secure RNG, secure key derivation and encrypted offline backup. Signature candidate **Ed25519** for v1, **SHA-256** commitments, **HKDF** domain-separated key derivation, **Argon2id** local passphrase hardening, audited **XChaCha20-Poly1305** for encrypted BlackBox data. Specific schemes/params subject to library review, cross-platform compatibility and crypto audit. No custom encryption constructions. On-device biometrics may *unlock* protected signing key, not prove global unique personhood and never upload raw fingerprints to chain.

No website/backend ever asks for or stores spending private key or Authenticator master in plaintext. Authenticated origin-bound client signatures and multiple independently verifiable proof endpoints. Pin network identity and trusted checkpoints, handle eclipse/phishing and stale light-client trust. Wallet UI distinguishes: locked pending, claim requested, waiting manual accept, receiver paid, sender reclaimable, sender reclaimed, recovery pending, dead recovery unbound, and protected suspense.

# 12. Active Recovery Mirror V4 (OWNER CONFIRMED)

Recovery is separate from lost-device restoration. **Source S and designated R both remain NORMAL_ACTIVE**. On **initial binding only**, preserve prior owner restriction that R be fresh with no prior ordinary financial transaction history unless owner later revokes it. S creates pairing with S Wallet Private Key + S Authenticator; R's BlackBox must explicitly ACCEPT with BFT finality within 24h adjusted deadline. Only after accepted pairing does distinct protected one-use **Disaster Recovery Key** get generated and retained inside R BlackBox. No generic change to active binding while R ACTIVE; a DEAD destination is an explicit exception.

S BlackBox's encrypted contents ONLY (not historic chain ledger transactions, and not a clone of funds) mirror continuously to separate **SEALED PARENT S ARCHIVE** inside R's BlackBox, with S-origin/event IDs. R can otherwise operate normally and independently designate its own Recovery C. R is not permitted to decrypt S archive merely because it holds ciphertext.

Only a valid BFT-final **RUN_DISASTER_RECOVERY(S,R)** using original S Private Key and R-protected unique Disaster Recovery Key makes S permanently DEAD and transfers *once* only spendable unlocked S coins as a **NEW recovery ledger transaction** into already ACTIVE R, with authorization to release S archive; R's own transactions/accounts remain distinct. Locked escrows, sender/receiver pending rights and slashable validator bonds are NEVER sweepable as ordinary unlocked coins; authorize defined successor claim/withdrawal rights without resetting deadlines or excluding penalties.

If R becomes **consensus-final DEAD** for any reason, atomically **REVOKE active S→R pairing** and notify S: S remains ACTIVE but has **no recovery** until it registers NEW eligible ACTIVE D, with new consent and fresh full encrypted baseline backup. **No automatic inheritance via R→C**; B/C may retain sealed S ciphertext without gaining ability to read S. Merely offline R does not count DEAD. Historical pairing/revocation receipts stay on-chain.

**Cryptographic blocker:** if R owns a full decrypt key to S archive while S active, hiding UI does not prevent malicious offline decrypt. True conditional post-BFT release needs independently auditable threshold/cryptographic escrow scheme with explicit fault/collusion thresholds or separate guarded recovery materials. Every scheme introduces availability and collusion assumptions; not solved by slogans. Lost unsynced BlackBox data cannot be rebuilt. K_S generated only later is still a separate critical paradox. No production confidence claim until scheme independently audited and recovery-with-loss tested.

# 13. Network Time, Deadlines, Disputes and Safety

Use consensus-canonical timestamps/height and tight monotonic rules; phones/individual relays do not have absolute trusted clocks. Owner intent **one-to-one verified network-caused delay compensation** for every time-limited operation is preserved. Propose combined independently attested per-operation and networkwide incident intervals, canonical **set union** (no double credit), consensus checkpoint receipt watermarks and strict non-retroactive deadlines.

In arbitrary asynchronous partitions, it is impossible to prove exactly whether each second was caused by malicious censorship, device loss, or network delay from untrusted timestamps alone. Therefore **equal exact compensation cannot be guaranteed under all attacks**. When unavailable/unprovable evidence is present, fail closed into bounded \`PROTECTED_SUSPENSE\` rather than settle mutually exclusive rights twice or confiscate. A final exit/appeal protocol that is decentralized, fair and live remains a **BLOCKED research problem**, not hidden admin discretion. Do not allow finality if approval only entered mempool before deadline but committed after adjusted cutoff.

No financial arbitrator can force an external trade refund or delivery judgment. No hidden platform administration funds key.

# 14. Validator Stake During Source Disaster

S may be a validator while registering R recovery. On final S→R disaster, atomically **freeze new validator registration/duties for S and schedule the validator key's safe exit at a BFT-authorised epoch boundary**; do NOT instantaneously rewrite a current voting set without quorum-intersection proof. Maintain any still-active prior consensus responsibilities or formally validated replacement state until transition, and preserve S's slashable bond until valid exit, evidence expiry and unbonding are complete. R obtains a protocol-delimited **withdrawal entitlement to the non-slashed bond** only after those rules, not spendable TONG at instant recovery, and **does not automatically become S validator**. Owner has not separately approved this consequential staking/recovery extension; it is a selected safe blueprint pending explicit ratification. Ensure no duplicate transfer and no release by DEAD destination. Report before mainnet.

# 15. Node Software, Infrastructure and Privacy

**Repo architecture proposal:** \`tongnet-ledger-rs/\` deterministic account/escrow/state, \`tongnet-consensus-adapter/\` ABCI++ bridge, \`tongnet-wallet-core/\` signatures, \`tongnet-blackbox/\` encrypted inbox and proof events, \`tongnet-recovery/\` delegated succession and ciphertext replication, \`tongnet-node-config/\`, \`tongnet-cli/\`, \`tongnet-light-client/\`, \`tongnet-testkit/\` with formal models, adversarial simulator and migration harness, \`docs/\` versioned specs, \`security/\` disclosure/threat models. Do not build application marketplace.

CometBFT binary & Rust application interop failure modes need reconnect, transaction duplication, deterministic replay and crash-recovery tests. Nodes should use rate-limited P2P gossip, independent seed discovery (not just ParmTech DNS), transport encryption with identity binding, network partitions handling, state sync with verified peers, public explorer with chain proof, noncustodial wallet APIs, archive retention policy and snapshots.

**BlackBox ciphertext** is not ordinary globally replicated blockchain data by default. Replication availability/storage costs, controlled metadata disclosure and GDPR/Privacy Act deletion expectations are distinct from immutable ledger records. No raw offchain claim code, root secret, decryption material or identifying biometrics ever published to validators/logs/metrics. BlackBox encrypted archive deletion and source revocation are separate from immutable history.

# 16. Security and Upgrade Governance

Set reproducible signed releases, multiple independent binary builders, source-code availability, dependency SBOM, pinned toolchains, security.txt and external vulnerability disclosure. Versioned hard forks require proposal publication, impact assessment, safety-critical compatibility tests, voting under transparent protocol with long timelock (trial **30 days** ordinary upgrade and **7 days minimum** emergency, with unusually high quorum and human review); no new mint or spending override by creator. These are **research parameters** and depend on fork-coordination mechanics. An on-chain majority under stake capture can still coordinate malicious rule changes; light clients must reject unauthorized monetary rule changes based on pinned protocol constraints where feasible.

Research post-quantum signature transition (NIST FIPS 204 ML-DSA etc.) in an isolated testnet; do not market v1 Ed25519 as quantum-resistant. Hybrid key migration, address upgrades and vote certificate sizes require hard tests first.

Threat model priorities: 1/3 BFT sabotage, 2/3 capture, stake lending/borrowing/re-hypothecation, fake account splitting, key/exchange loss, double sign, fee farming, relay eclipse/DDoS, timestamp manipulation, invalid finality certificates, transaction reorder, exploit in custom state machine, K_R guessing, K_S paradox, malicious BlackBox decrypt, recovery target DEAD, cartel validator hosting, cryptographic/side-channel compromise, chain upgrade splits and censorship. Economic bond alone does not render unknown early market secure.

# 17. Legal, Consumer and Ethical Risk

Australian-based ParmTech must obtain qualified legal review before launch; Australian crypto law and digital asset platform rules evolve. Token sales, validator rewards, exchange services, custody, marketing, tax/accounting, privacy and cross-border sanctions can carry different obligations. No ICO, fiat redeemability, value guarantee or yield representation is authorised here. Include plain-language self-custody loss and malicious receiver/sender scenarios. No forced escrow forfeiture on public-money chain while owner reserve intent lacks legal/consent/outage protection. Material owner policies may conflict with mandatory statutory rights; do not solve conflict by silently coding confiscation.

# 18. Formal Invariants — MUST PASS

1. TONG conservation \`genesis + issued = total liquid + escrow + bonds + treasury + fee pending + other explicit state\`, less explicit provable burns; ≤ hard cap. No floating arithmetic or overflow.
2. No escrow output twice; exactly one of FINAL_ACCEPT payout, authorised SENDER_RECLAIM, or legally authorised post-window resolution.
3. Sender's FINAL_ACCEPT is separately cryptographically necessary for receiver credit; Receiver request alone pays nothing.
4. No payment deadline activated by local UI click/mempool submission; canonical FINALIZED event state determines rights.
5. No incompatible receiver and sender rights at same height/state; no retroactive certificate invalidating finalized payout.
6. Old Wallet S DEAD cannot create fresh payments or validators; already finalized ledger history remains immutable.
7. Recovery destination DEAD means immediate network-canonical invalidation of all incoming active recovery bindings; never silently redirect to third wallet.
8. R cannot decrypt parent S mirror before properly authorised S→R recovery under explicit crypto threshold assumptions. No plaintext leaked in logs/chain.
9. Validator vote-weight changes cannot create two valid divergent quorum sets; fail closed in partition.
10. 1000 cloned wallets with fixed amount of stake cannot multiply total stake-weight voting influence or mint rewards via self-deal.
11. Slashed bonded entitlement not accidentally swept into liquid successor balance.
12. Invalid, replayed or wrong-chain code/proof/signature cannot authorise a state transition; expired 24h / 60d rights not revived without ratified verified-delay evidence.
13. Resource use bounded during mempool spam and state-sync; offline nodes/phones cannot be mistaken for live witnesses.
14. Full and light clients detect inconsistent state roots and expired proof trust.
15. Automated upgrades cannot secretly violate hard cap, signing authority, audit records or escrow law without an explicit fork/new chain warning.

# 19. Testing Matrix and Stop Conditions

**Foundational:** Rust unit tests; property-based state transition fuzzing; differential independent reference model; deterministic Byzantine tests; signed-message mutation fuzz; persistence/crash simulation; key misuse and K_R offline-guess attack tests; economic adversarial replay; formal TLA+/PlusCal/Apalache model for escrow rights and validator membership.

**Multi-node:** 4/7/21/64/96 validators; 5+ independent geographic regions; 100k Sybil wallet spam, 0 traffic overnight, 33% unavailable voting power, 34% corrupted/absent, conflicting double spends across partitions, vote reconfiguration during partition, evicted nodes, backups/version mismatch and simultaneous recoveries. Zero safety violation at all test scales under stated safe fault model; reject output outside threat assumptions.

**BlackBox:** late final acceptance, expired code, repeated wrong code, sender lost after lock, source DEAD before K_S, encrypted parent archive compromise/threshold-collusion, ciphertext lag, target R becomes DEAD during a pending recovery, R→C before S→R, validator-bond successor and pending receiver compensation.

**Release gates:** Independent BFT/app consensus audit; independent wallet cryptography/recovery audit; economic security simulation on actual token distribution; external pentest & public incentivized testnet; reproducible binaries; formal proof artefacts or documented bounded model-checking; no outstanding critical/high fund-loss defects; published vulnerability reporting and funded response; 90-day multi-operator public rehearsal; legal/compliance memorandum; operators truly independent. If any blocker unsolved, **do not launch real-value mainnet**.

# 20. Engineering Roadmap from Zero to Long-Term

| Gate | Deliverable | Exit criterion |
|---|---|---|
| 0 - Spec freeze | This whitepaper + override register, invariants, economics and threat model | Owner ratifies high-impact departures and safety blockers |
| 1 - Deterministic core | Rust coin ledger, accounts/nonces, signing, escrow state machine, property tests | No double spend/fund-loss in exhaustive bounded model |
| 2 - BFT integration | Version-pinned CometBFT, ABCI++ bridge, genesis, local 4–7 node net | Deterministic replay and stable state root, crash recovery |
| 3 - Wallet and BlackBox | Noncustodial wallet, authenticated sender approve, Receiver claim, integrity receipts | Key isolation / anti-replay tests; no unauthorised settlement |
| 4 - PoS/fees | Validator bond, stake snapshots, slashing, fees, issuance | Stake split and penalty economics review |
| 5 - Recovery | ACTIVE mirror, new R acceptance, deadline, DEAD→unbinding, threshold decryption, staked entitlements | Both technical recovery blockers solved and audited |
| 6 - Public testnet | 21→64 operators, ≥32 standbys, 128 full nodes target | 90-day stable public chaos and performance tests |
| 7 - Launch review | Independent audit, legal, user disclosures, genesis distribution/dilution, protocol governance | No critical blocker; explicit mainnet sign-off |
| 8 - Mainnet limited release | Measured daily limits and progressive decentralization | Observe incidents; public transparency; no unreviewed caps |
| 9 - Postlaunch | Delegation if proven noncustodial and safe, optional PoTP, dynamic upgrades, crypto agility | Separate audits and owner/community governance |

No calendar date, development percentage, source line count, running node, deployed wallet, mainnet supply or performance figure is claimed complete by documenting the gates.

# 21. Risk Register — RED / AMBER / GREEN

**RED - hard mainnet stops:** (R1) mathematically enforceable unreadable-to-R sealed mirrored parent archive with conditional key release; (R2) late-generated K_S after S BlackBox loss; (R3) objective one-for-one network delay proof under mixed censorship/partitions and valid suspense exits; (R4) user-proposed automatic escrow forfeiture legality/consent and malicious delay abuse; (R5) genesis distribution and stake purchase/collusion economics; (R6) recipient/sender consent evidence and balance handling when Source DEAD; (R7) stake-bond succession to R; (R8) audited reference implementation and independent testnet; (R9) precise legal classification / compliance. These are not solved by writing the paper.

**AMBER - tests required:** BFT engine Rust adapter crash; 64-node global latency; PoTP audit-work usefulness; 28-day unbond evidence coverage; fee viability when low traffic; checkpoint trust/availability; peer diversity; privacy metadata; upgrades.
**GREEN - clear conceptual scope:** Native TONG only, no EVM/dApps; distinct sender final accept; no 3h trigger; 24h Receiver and 60d Sender windows; ACTIVE recovery target rule with auto-unbinding if R DEAD; independent consensus witnesses rather than own-payment voting.

# 22. Decision Log, Override Priority and Open Ratifications

| Key | Status |
|---|---|
| One native TONG currency + independent chain, no dApps/tokens | **OWNER CONFIRMED** |
| Manual 3-phase payment, no 3h Trigger, R 24h then S 60d | **OWNER CONFIRMED** |
| No external deal arbiter, no validator power to forge Sender ACCEPT | **OWNER CONFIRMED** |
| Recovery destination remains independently ACTIVE, mirrors S BlackBox only; R DEAD auto-unbind | **OWNER CONFIRMED** |
| Fresh R at moment initial binding | Prior owner constraint **preserved pending clarification** |
| Bonded PoS + fixed-epoch BFT, trial counts / bonding times / candidate fees | **ARCHITECT SELECTED REFERENCE, to test/ratify** |
| Account-based native state, Rust + reviewed CometBFT | **ARCHITECT SELECTED REFERENCE** |
| 100m hard-cap reference only; **genesis amount, allocation and issuance ARE UNDECIDED** due to V1.0 attack/economic failures | **ARCHITECT SELECTED ECONOMIC CANDIDATE** |
| 24h t0 at FINAL LOCK | **ARCHITECT SELECTED CANDIDATE** (not explicitly confirmed by owner) |
| Conditional threshold archive key release & successor locked stake rights | **UNSOLVED / owner approval needed** |
| Replacing late-only K_S issuance and post-60d reserve forfeiture | **OWNER POLICY CONFLICT; NO unilateral change** |
| Attacks mathematically impossible, zero ongoing validator infrastructure | **REJECTED as unachievable guarantee** |

Legacy links contain older Trigger/72h/frozen-recovery language. Priority is **(1) latest explicit user rule → (2) newer canonical V4 recovery/secure bilateral payment docs → (3) this architect-selected v1 reference plan → (4) old proposals/history**. Never treat an older stale statement as a newly ratified feature.

# 23. 65 Design Questions and Recommended Answers

**Q01. What is TongNet?** One native TONG cryptocurrency blockchain, not Ethereum.  
**Q02. Does it mine Bitcoin-style PoW?** No for v1 reference; bonded PoS + independently reviewed BFT.  
**Q03. Can any person create a new TONG currency?** No; only one monetary asset.  
**Q04. Are third-party dApps allowed?** No.  
**Q05. Is there a public smart-contract VM?** No; native audited finite operations only.  
**Q06. Why not zero fees forever?** Nodes/storage cost money and unlimited costless requests allow spam.  
**Q07. Can fees be earned back?** Separately, after verified legitimate validator work; not guaranteed refunds.  
**Q08. Is bonded stake an investment return guarantee?** No, work-dependent rewards and slash risks.  
**Q09. Can wallet merely holding coins vote?** No; explicit bond, dedicated key and online node.  
**Q10. Must staking users keep phone on?** No if using a separate online validator or approved delegation later.  
**Q11. Does every user run a node?** No; any user can operate, full validators opt in.  
**Q12. Why 64 active validators?** Only a public-testnet/mainnet readiness target; scale and operator independence must be demonstrated.  
**Q13. Why >=32 standby?** Online transition capacity without weakening quorum; reconfiguration must be formally safe.  
**Q14. Does 7/10 signatures suffice?** Not without proven BFT protocol, independent stake and quorum.  
**Q15. What if attacker creates 1m wallets?** Free identities get zero votes; only economically scarce bonded weight qualifies.  
**Q16. Can attacker split stake across wallets?** Splitting does not increase total stake-weight, though stake cartel remains possible.  
**Q17. Can wealthy attacker control network?** Yes in principle if obtains/colludes for enough weight; monitor actual economics.  
**Q18. Does staking age grow voting power?** No; maturity is eligibility, not multiplicative vote subsidy.  
**Q19. Why unbonding wait?** Preserve liability for provable past double-sign/faults.  
**Q20. Slash ordinary offline phone?** No automatic slash for brief outage; no rewards, possible deactivation.  
**Q21. Can selected quorum be off?** Then finality halts rather than forging an unsafe approval.  
**Q22. What if network partitions 60/40?** No independent finality in either partition lacking >2/3 voting weight.  
**Q23. Can standby nodes force quorum?** Not without previously agreed quorum-safe membership transition.  
**Q24. Do three transaction actions add 3 voting rights?** No; only wallet authorization and optional separate auditing.  
**Q25. What does PoTP actually do?** Optional unrelated finalized-proof verification, anti-spam and auditable service.  
**Q26. Can self-payments mint credits?** Never automatically; no rewards for fake volume.  
**Q27. What does Receiver code alone do?** Eligible Claim Request, never final payment.  
**Q28. Can validator finalize without Sender?** Not without authentic Sender BlackBox FINAL_ACCEPT.  
**Q29. What if Sender never accepts?** Receiver cannot obtain TONG; sender-only reclaim later under agreed rights.  
**Q30. When starts 24h?** Proposed exact BFT-final LOCK; awaiting explicit owner ratification.  
**Q31. When starts 60 days?** After adjusted receiver exclusive deadline; no overlaps.  
**Q32. Is auto refund after 24h?** No.  
**Q33. Does an old 3h Trigger remain?** No, removed.  
**Q34. What if claim was queued just before deadline?** Need valid BFT finality before adjusted cutoff; queue alone insufficient.  
**Q35. Can network delays always be exactly proved?** No under arbitrary partitions/adversarial censorship; preserve funds in protected suspense when unknowable.  
**Q36. What after 60d no claim?** Owner proposed network forfeiture; blocked for real-money until explicit legal and safety solution.  
**Q37. Can claim codes be on-chain?** No, only hiding proofs/commitments and masked metadata.  
**Q38. Is BlackBox recoverable if never backed up?** No.  
**Q39. Can Recovery R pay while paired?** Yes, R stays NORMAL_ACTIVE (latest owner override).  
**Q40. Does R inherit S old transactions?** No, chain history immutable; display provenance-linked receipts separately.  
**Q41. What mirrors S to R?** S encrypted BlackBox contents only.  
**Q42. Can R read S data before authorised disaster?** Must not; this requires unsolved audited key-release cryptography, not UI hiding.  
**Q43. What if R dies first?** Network auto-revokes S→R, warns S, S may designate fresh eligible D.  
**Q44. Does B→C automatically mean A→C?** Absolutely not.  
**Q45. Does S become dead on lost phone?** No, lost-device restore is distinct; only valid FINAL disaster makes S DEAD (apart from separately defined 72h activation policy).  
**Q46. Who authorises disaster?** Original S private key + one-use R BlackBox disaster key, prior accepted pairing and BFT finality.  
**Q47. Can R receive slashable stake immediately?** No, successor withdraw rights remain exposure-limited.  
**Q48. Can R automatically use S validator key?** No.  
**Q49. What if new Sender reclaim K_S never got generated due to phone loss?** Major protocol blocker; cannot silently invent secret.  
**Q50. Is there an administrator rescue?** No unilateral funds-recovery backdoor.  
**Q51. Are password/master keys stored on ParmTech server?** No.  
**Q52. Can fingerprint prove unique global human?** No; optional local biometric key unlock only.  
**Q53. Will validator be a mobile device?** Light verification on phone; full online service usually a computer/server.  
**Q54. Why use Rust?** Memory-safe-by-default deterministic core and shared wallet cryptography; tested Go BFT may be retained via protocol boundary.  
**Q55. Why account-based rather than UTXO?** Native escrow/recovery transitions simpler; must test privacy and replay tradeoffs.  
**Q56. Can TONG transaction price stay fixed AUD 0.01?** Not without fiat price/oracle/peg assumptions; quote TONG transparently.  
**Q57. Are rewards minted on transaction clicks?** No, only defined issuance and legitimate validator duty.  
**Q58. Who gets genesis coins?** No real recipient until independent distribution/legal approval; reference allocation only.  
**Q59. Can creator secretly mint beyond cap?** The native protocol must reject any mint beyond its ratified cap; a coercive hard fork or unsafe upgrade remains possible and clients need trusted parameter pinning.  
**Q60. Are upgrades automatically safe?** No, timelock, public specs, independently verified binaries and fork governance necessary.  
**Q61. Is privacy complete?** No, public chain leaks some metadata; BlackBox ciphertext is private but key release unresolved.  
**Q62. Is network unhackable?** No, bounded threats and independent audits only.  
**Q63. Can this be launched now?** No. There is design, not coded audited mainnet and several hard blockers.  
**Q64. How know it is ready?** 90-day public adversarial testnet, stake/security/crypto audit, independent validator distribution, legal clearance and all RED items closed.  
**Q65. What should be implemented first?** Deterministic money/escrow state machine, time-aware invariant checks and monetary model review, then a BFT localnet, not premature mobile UI or token listing.

# 24. Authoritative Related TongNet Design Documents

- [Current single-coin product scope](TONGNET_BITCOIN_LIKE_SCOPE.md).
- [Confirmed active Recovery Mirror V4 and automatic dead-target unbinding](ACTIVE_RECOVERY_MIRROR_V4.md).
- [Latest trusted two-party P2P / 60-day sender rights](SECURE_P2P_V3_RECOVERY_DECISIONS.md).
- [Hybrid PoS + Transaction Participation security research](HYBRID_POS_POTP_BFT_RESEARCH.md).
- [Reciprocal validation and fee research](RECIPROCAL_TRANSACTION_VALIDATION_RESEARCH.md).
- [Transaction participation research](PROOF_OF_TRANSACTION_PARTICIPATION_RESEARCH.md).
- [All 95 historical deep questions](DEEP_QUESTIONS.md) and [proposed answers (including superseded drafts)](MASTER_QA_RECOMMENDATIONS.md); superseded answers require canonical reconciliation.

# 25. Technical References and Real-World Precedents

1. CometBFT Byzantine consensus specification: https://github.com/cometbft/cometbft/blob/main/spec/consensus/consensus.md ; safety/liveness assumptions and >2/3 precommit.
2. CometBFT ABCI++ application boundary and deterministic replication: https://github.com/cometbft/cometbft/blob/main/spec/abci/abci%2B%2B_basic_concepts.md
3. Cosmos SDK staking and slashable unbonding: https://github.com/cosmos/cosmos-sdk/blob/main/x/staking/README.md
4. Ethereum proof-of-stake penalties and consensus role: https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/
5. Nano PoW anti-spam & fairness (different from consensus): https://docs.nano.org/protocol-design/spam-work-and-prioritization/
6. Bitcoin UTXO/payment model: https://developer.bitcoin.org/devguide/transactions.html
7. NIST FIPS 204 post-quantum signatures: https://csrc.nist.gov/pubs/fips/204/final
8. ASIC Australia crypto offering obligations: https://asic.gov.au/regulatory-resources/digital-transformation/crypto-assets/
9. MoneySmart current Australian crypto risks and 2027 Digital Asset Platform reforms: https://moneysmart.gov.au/complex-investment-products/crypto-assets

**Final status:** This is a **complete end-to-end planning whitepaper**, not an implementation certification. The chosen baseline and full launch gates are stated; unresolved research/owner approvals are explicit rather than quietly overwritten. **No blockchain, tokens, wallets, recovery encryption, validator binary or test results were created merely by writing this document.**


# 26. V1.1 Adversarial Logic Audit — Consolidated Corrections

**Audit status:** Internal architecture scrutiny, not external smart-contract, crypto, consensus, financial or legal audit. Important findings are documented honestly; any unresolved RED issue blocks handling real user value. This addendum corrects logical omissions and a few misleading V1.0 numeric proposals.

## A. Critical money/control invariants

**A1 — Validator-set revocation vs immutable BFT epoch:** V1.0 wrongly implied S becoming DEAD could *immediately* remove its bonded voting power. Arbitrarily reducing an active validator set midheight can yield conflicting quorums. Fix: S wallet spending becomes DEAD atomically; validator eligibility enters exit scheduling; active voting-set membership changes only by consensus-final epoch transition preserving quorum intersection. Signer key compromise may require evidence-driven quarantine, but live committee disruption must fail closed. Successor R inherits only residual bond withdrawal entitlement after slash/evidence obligations; no auto-activation of S validator.

**A2 — No safe invariant for node counts alone:** 64 active keys, 32 standbys, 128 full nodes and 16 archives are *coverage targets*, not guaranteed independent operators. Require independent beneficial-control and stake-distribution audits with adversarial stress testing. Hidden operator grouping is an unavoidable uncertainty. Limit launch reliance on founder/related stake; no account-based voting caps bypassable by Sybil wallet splits.

**A3 — Emission/treasury capture:** Previous 12m genesis + 17.6m first-four-year emission would inflate circulating/genesis stock dramatically (146.7% potential new issuance vs genesis). And former 25/15/10 validator-bootstrap/treasury/team slices could have aligned control of up to 50% genesis. Both proposed schedules are withdrawn. No mainnet supply issuance parameters should be coded until market cost-of-corruption, reward-budget sustainability and independent distribution are analysed. A 100m cap is still only a *candidate*, not monetary authority.

**A4 — Token-denominated min bond has no fixed economic cost:** 25k TONG cannot secure anything when TONG has unknown initial exchange value or liquidity; replace with bonded stake whose effect is assessed relative to actual circulating stake, stake acquisition/borrow markets and validator real expense. The testnet can have a fixed dummy bond to exercise logic; production requires separate security/economics review.

**A5 — Slashing and exit overlap:** Protocol evidence age in both seconds AND block heights must be strictly shorter than slashable unbonding retention under worst-case slowdown and checkpoint retention. Cite CometBFT evidence parameters and test after upgrade. An operator can otherwise equivocate, exit and withdraw before objective evidence is processed. Normal phone loss should not automatically confiscate a security bond.

**A6 — Block size overwhelms a lean chain:** 2MiB every 4sec is 45.3GB/day and 16.5TB/365 days of RAW block bytes; with indexes and archives more. Reduce exploratory max to 256KiB/6sec (3.77GB/day, 1.38TB/year fully occupied) and explicitly estimate on-disk/index growth. A 512KiB expansion needs multi-region storage/fee tests; design pruning/snapshot and archive proofs separately. State action throughput should be measured in *complete 3-phase payments* as well as raw actions.

**A7 — Three-stage fees not actually paid by the proper actors:** Receiver may have 0 TONG but must CLAIM. Initial Sender LOCK must prepay bounded, non-transferable escrow operations budget for one valid Receiver claim and one Sender accept or later sender reclaim; protect relays against unbounded wrong-code spam through stateless rejection, replay nonces, fair P2P bandwidth budgeting. Fees are charged for executed operations; unused budget returns under known outcome. All fee escrow and future network storage liabilities count toward conservation and wallet recovery rules.

**A8 — Fee farming / thin liquidity:** Ordinary self-transfer must be net-costly and pay independently eligible unrelated validator committee. No reward for creating a payment or merely signing an external receipt. A randomized committee still can be bribed; reward allocation can't claim proof of genuinely expensive computation from a signature alone. At low traffic 64 always-online validators and archive nodes cannot be sustainably financed solely from tiny fees without transparently defined issuance/sponsorship; stress cost assumptions and don't promise profit.

## B. BlackBox and escrow correctness

**B1 — Lock before K_R generation was unsafe:** Prepare entropy-bound claim signing credential and persist encrypted backup *before* network LOCK; public credential commitment bound to the escrow. Release to receiver ONLY after BFT-final LOCK. If client loses power between preflight and finality, safely replay/sync LOCK and persisted secret by tx id, never create a funded lock with missing key. Ensure an out-of-band copy or alternative controlled recovery matches owner intent.

**B2 — Human-short code can't be public-hash-verified safely:** A 6-digit code commits only ~20 bits; publishing hash/commitment leaks brute-force oracle. Recommend native one-time secret signing key with public verification key committed at LOCK, receiver signs unique request under both receiver own key and imported one-time key. Encode secret through trusted QR/long code; shorter UX needs a separately rate-limited cryptographic exchange and independent audit, not a public hash.

**B3 — Separate signed ACCEPT authority had no full failure model:** Binding must include unique tx id, chain id, receiver key, exact requested amount, claim request id, deadline version, and sender BlackBox one-time monotonic accept nonce. Validator requires the registered independent Sender BlackBox public authorization key plus S wallet authorization model. Compromised validator cannot conjure approval. Sender can refuse; do not claim merchant fair exchange.

**B4 — Inconsistent 24h/60d and delay-proof timing:** Receiver **claim plus Sender final accept must both BFT-finalize** within effective receiver window; receiver claim merely entered mempool before cutoff does not create ownership. Sender's subsequent 60 full days start only after adjusted receiver priority ends. Test exactly-at-cutoff determinism, epoch reorg impossibility under BFT assumption, and competing expiry ops. Exact causal network-delay seconds cannot be proven under arbitrary asynchronous adversaries; preserve owner intent but classify as unsolved, protect funds and prohibit retroactive inconsistent rights.

**B5 — Sender K_S paradox remains a real-money stopper:** Owner's late-only creation of a sender reclaim key after 24h is impossible to reproduce on a destroyed device/BlackBox, including from an earlier mirror. Proposed **consent-dependent** alternative: prepare sealed high-entropy reclaim seed/commitment at LOCK, derive or reveal the working K_S credential only after finalized receiver window expires under authenticated control; requires formal source/R roles, anti-early-use proof and owner approval because it alters the literal late-only secret-generation rule. Without that approval & audit, not deployable.

**B6 — Unsound confiscation of old escrow:** After sender 60d window owner has proposed loss of remaining funds to network treasury. Do not implement until applicable legal/regulatory analysis, explicit informed consent and recovery for provable outages; otherwise use no real-fund mainnet or narrowly defined PROTECTED_SUSPENSE on research testnet. Permanent protected suspense is itself an economic/liveness concern that must be resolved, not treated as a free solution.

**B7 — Receiver/claim griefing and storage pressure:** One signed Claim_REQUEST must not exhaust pre-funded fee budget to force forfeiture through recipient delay; enforce accepted receiver identity, one live claim id/escrow, replacement only under strictly defined explicit sender/receiver consent, and no negative fee budget. Price 61-day conditional state storage, limit payload size and max escrows per limited-resource account. Beware fee-on-failure unauthenticated spam.

## C. Recovery and validation boundary

**C1 — Encrypted archive is not cryptographically locked if R has key:** UI-hidden ciphertext is not unreadable if R device already possesses all decryption shares. Conditional key release anchored to a BFT-final authenticated S→R event requires an independently reviewed threshold/key-escrow architecture, explicit collusion and liveness assumptions, rotating keyshares across validator-set changes and backup key-retention rules. Neither network state nor smart contracts can prevent early offline decrypt by an already fully equipped recipient. No false guarantee of zero trust.

**C2 — Active R vs virgin-at-first-bind contradiction across stale docs:** Latest owner decided R remains independently NORMAL_ACTIVE while serving as S recovery and may own R→C; fresh at first binding was *not expressly revoked*. Treat fresh initial binding as preserved until owner clarifies. Any older RECOVERY_RESERVED_FROZEN description is historical only; latest S→R and DEAD-target auto-unbinding govern.

**C3 — R DEAD while parent archive copies exist:** Consensus-final R DEAD revokes active S→R immediately, never automatically recovers S into R's own successor C. A already-mirrored S ciphertext may remain in R→C encrypted backups; C must NOT obtain S parent decrypt authorization merely by B→C recovery. Data-retention/crypto-shredding and loss warnings require formal treatment.

**C4 — Active stake balances after disaster:** R receives only S unlocked TONG atomically; S outgoing escrows and validator bonds remain in segregated rights states. Source DEAD cannot directly vote with former S wallet key. Recovery carries a *pending withdrawal beneficiary* entitlement for non-slashed bond post unbonding rather than immediate spend. Still needs explicit owner sign-off: staking adds a new financial asset classification to earlier recovery rights.

**C5 — Wallet 72h activation DEAD/initial loss:** On-chain address registration and fresh wallet deposits must reject pre-activation funding atomically, otherwise funds may permanently die when activation deadline expires. Define whether unactivated/never-funded addresses occupy consensus storage (state rent) and wallet restoration path.

## D. Network security, legal and implementation

**D1 — Upgrades cannot be only stakeholder-controlled on cheap early supply:** Publicly reveal parameter changes in advance, independent builds, minimum notice and fixed client constraints (especially supply cap and owner-signature requirements). Concentrated holdings still allow coercive forks, which users may refuse; no absolute governance guarantee.

**D2 — Crypto algorithm choices are not cryptographic proof:** Choose audited standard Ed25519 / SHA-2 or equivalent as supported by validator/wallet libraries, authenticated encryption/key derivation, disjoint key domains, test vectors across platforms and secure random-number generation. Distinguish post-quantum migration research from protection actually present today.

**D3 — Regulatory reality:** Australia's 2026 DAF Act has new regulated platform requirements commencing **9 April 2027**, potentially relevant depending on whether ParmTech operates a digital asset platform/custody service, and 2026 ASIC draft standards. Noncustodial chain software is not automatically a licensed financial service, nor automatically exempt. Obtain independent Australian legal classification before promotion/listing/custody. Preserve self-custody, no price/yield guarantee or unapproved reserve confiscation.

**D4 — Release gate is not number of documents:** No mainnet until correct monetary authority, audited escrow/recovery/key-release logic, formal state invariants, experimental committee attacks with independent stake, 90-day public adversarial testnet, no critical/high fund-loss findings and external legal/compliance advice. Research models can be "complete plans" without claiming deployed code or zero bugs.

# 27. V1.1 Reference Corrections: Explicit Design Parameters

| Parameter | V1.0 draft | V1.1 recommendation |
|---|---|---|
| Consensus | Bonded PoS + BFT | Unchanged. Reviewed BFT global finality, stable signed epochs and independent nodes. |
| Active/standby/full/archive targets | 64/32/128/16 | Retain as *scale targets only*; hard launch gate on independent voting control, not count. |
| Block target/max | 4s / 2MiB | 6s / 256KiB initial benchmark; 512KiB later optional. |
| Throughput | 100 state actions/s target | 20 state actions/s first adversarial test; measure complete 3-phase payments/s separately. |
| Genesis/supply | 100m cap, 12m genesis, 17.6m first-era, 50%-potential related entities | Keep 100m cap as **nonfinal reference**; **withdraw emission/genesis fractions** pending economic security+fair allocation audit. |
| Min bonded stake | 25,000 TONG | No mainnet absolute threshold before attack-cost pricing; disposable faucet testnet only. |
| Equivocation slash | 5% trial | Not selected pending attack/evidence modelling. |
| Validator maturity/unbond | 7d / 28d example | Retain only as research benchmarks; evidence lifetime must fit in unbonding. |
| Claim secret | Constructed at/after final LOCK | Prepare encrypted one-time proof key **before** LOCK broadcast, deliver only after final LOCK. |
| Receiver fee | Implicit / unfunded | Sender prepays bounded Receiver claim+Sender finalize/reclaim budget at LOCK. |
| Tx-driven votes | 3 actions sometimes described as verifying | Only optional unrelated receipt auditing; stake BFT decides canonical state. |
| BlackBox mirroring | R active, ciphertext sealed | Unchanged with serious unapproved conditional key-release implementation blocker. |
| DEAD-source validator | Immediate revoke in active quorum | Endorse wallet DEAD instantly, consensus validator exit only with quorum-safe epoch transition. |
| Post-60d treasury | Owner intent | Never irreversible mainnet confiscation without law/consent/outage closure; protected research state is not a complete solution. |

**Internal logic audit concluded:** V1.1 fixes contradictions in its design choices and measurement claims, but does **not** solve the real cryptographic impossibility/key-loss/permissionless economic risk classes. Readiness remains **NOT READY FOR REAL FUNDS**. Mainnet authorisation requires engineering evidence and owner approval for any change to owner-confirmed financial rights.
