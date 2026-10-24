# TongNet research proposal — Human Presence / Proof-of-Personhood as an OPTIONAL validator defense

**Date:** 2026-10-25 (Australia/Sydney). **Status:** UNAPPROVED RESEARCH PROPOSAL prompted by the owner exploring physical human check-ins, fingerprint, social-media/music participation, button presses and alternative Bitcoin-like mining. NOT a confirmed protocol change; NO deployed software, coin issuance, proven uniqueness or audit. Bitcoin-like single-native-TONG chain scope stays unchanged.

## Owner's question
Can TongNet replace conventional Proof of Work with real humans periodically completing a mobile fingerprint or other physical challenge, interacting with music/social-media content, doing a task daily, and enabling network transaction processing? Would an original human-work consensus be better than PoW or hybrid PoS+BFT?

## Research findings
- Proof of Work uses real-world scarce, objectively verifiable computation and typically costly Sybil identities; a social click/fingerprint/daily quiz is cheap to replay, outsource, fake or buy unless true **unique personhood** and challenge authenticity are solved.
- **Person presence ≠ unique person**: Android BiometricPrompt / Apple LocalAuthentication establish authentication of an enrolled biometric on that device, with protected local material, not globally one human/one blockchain identity. A person can use many devices/accounts; offline proofs cannot establish unique humans just from phones. Never store/upload raw fingerprints, iris scans or biometrics on-chain.
- **Human check-in ≠ consensus**: BFT validators still have to be online frequently proposing/voting, replicate data and validate balances and exact TongNet receiver Claim + Sender Final Accept. People checking in once daily cannot substitute for always-on nodes. Consensus safety must not depend on a daily task whose abstention/illness/locale/time-zone could halt or censor money settlement. CometBFT documents >2/3 voting power required for progress under its validator model.
- **Existing prior art**: Idena Proof-of-Person coordinates synchronous human image story-puzzle validation; World ID uses biometric-backed proof of unique humanity with specialized Orb and privacy-preserving attestations. Neither provides universally verified Sybil-free uniqueness with no privacy, collusion, platform trust or accessibility tradeoff.
- **Social/music task proof**: content likes, watch time, song listening/creation and social graph relations can be gamed by farms/bots, are dependent on external platforms, copyright/payout terms, opaque moderation and account bans, and do not prove consensus correctness. Human creative work is useful cultural participation, not automatically a trustworthy scarcity primitive. If ever used for community participation/rewards, isolate from base consensus and use independently verifiable anti-abuse rules.
- **PoS+BFT**: less energy use and typically faster deterministic-finality settlement under quorum/fault assumptions, but economic staking concentrates power, validator independence cannot be proven by counting keys, and availability drops when >1/3 voting power unavailable. PoW is well-established permissionless competition but energy-intensive and has probabilistic settlement and concentration risks. Neither is proven absolutely more secure without a threat model.

## Candidate proposal: Human Participation Credential (HPC) + independent settlement consensus
This is NOT a new proven Proof-of-Work primitive, but an experimental additional eligibility/anti-Sybil layer.

**Layer 1 — Voluntary human challenge (per epoch, not per transaction)**
- Owner on phone explicitly authorises a challenge-bound cryptographic signature on a network nonce (e.g., biometric locally authorises hardware-backed key, with accessible PIN or hardware-key fallback).
- To prevent one person using 100 phones to harvest weight, require **actual independent unique-personhood method** (privacy-protecting credentials/nullifiers with false positive/collusion/issuer controls), not merely a biometric click. Evaluate at least two candidate independent assurance methods and disclosure/consent/accessibility.
- ZK/anonymous credentials might show possession of accepted uniqueness proof and one participation per epoch, but cannot magically prove underlying verification wasn't fraudulently issued.
- Do not make unverified humans unable to hold, send, receive or recover TONG. If human participation is necessary for validation, provide opt-out financial access and accessibility alternative.
- Freshness window (e.g., weekly/monthly) and revocation are proposed test parameters; daily check-in should NOT pause all network transactions. Extra daily action for optional rewards should not override consensus liveness.

**Layer 2 — Validator eligibility and economics**
- Operators host real independently verifiable online nodes (hardware/storage/network). Candidate human uniqueness credential, independent operator controls, cryptographic node attestation and possibly economically slashable bond (bond amount/supply/issuance still undecided). Fraud evidence can slash; ordinary offline/disability/missed challenge should not be automatically treated as fraud.
- Random/rotating validator committee with an explicit corrupt voting-power threat model; no false claim that committee rotation defeats Sybils, pooled stake, coerced proof holders or delegation cartels.
- Human privilege cannot create an invisible centrally controlled credentialing authority or privacy-invasive biometric registry.

**Layer 3 — Actual block finality**
- BFT or PoW consensus elected through a separately owner-approved mechanism: validate transactions continuously, reject double spends, enforce Lock/ClaimRequest/Sender BlackBox FinalAccept, finality-before-expiry, sender 60-day reclaim and other TongNet invariants; never wait for daily human clicks.
- Fees/reward issuance independent from human puzzle participation unless carefully specified monetary/economic conservation rules approved by owner and audited. Do not create free TONG from every click without a supply limit and fraud-resistant subsidy budget.

## Experiments necessary before choosing
1. Sybil adversary controls many devices, bot farms, paid humans, compromised attesters, cloned apps and outsourced CAPTCHA solving: economic attack cost per accepted unique credential.
2. A whole region goes offline or misses challenge; validator committee quorum; fail-closed safety without global transfers halting on predictable daily deadline.
3. Biometric false rejection, inaccessible hardware, accessibility, geography, coercion and children; privacy threat model and consent.
4. Validator liveness/finality benchmark under honest, intermittent, malicious and colluding operators.
5. Social/music-related optional participation must not rely on commercial social-media API as a chain trust root or reward copyrighted work automatically.
6. Alternative consensus PoW baseline vs PoS+BFT baseline under similar adversary budget and independent validator assumptions; do not claim superiority by throughput alone.

## Architecture recommendation for review (NOT owner accepted)
**Native TONG-only blockchain** + independently secured continuously running validation/finality + **optional privacy-preserving Human Presence/Uniqueness participation layer** for eligibility, decentralized representation or controlled rewards only AFTER strong uniqueness proof is demonstrated. This best preserves payment availability and tests the owner's creative human-in-the-loop idea without tying every payment to daily taps. A pure daily-fingerprint/click consensus should be rejected as insecure and unavailable until a sound cryptographic Sybil-resistant model is proven.

## Primary public source pointers
- Idena Proof-of-Person technology: https://docs.idena.io/docs/wp/technology
- World ID personhood approach: https://support.world.org/hc/en-us/articles/55499979675667-What-are-World-ID-Proofs-and-how-do-I-use-them-in-World-ID-app
- NIST biometrics limitations: https://pages.nist.gov/800-63-4/sp800-63b.html
- Android biometric cryptographic auth: https://developer.android.com/identity/sign-in/biometric-auth
- Apple device biometric boundary: https://developer.apple.com/documentation/localauthentication
- CometBFT consensus and quorum: https://github.com/cometbft/cometbft/blob/main/spec/consensus/consensus.md
- Review on Sybil detection trade-offs: https://www.mdpi.com/2076-3417/16/14/6929

**Attribution:** Project author ParmTech; original creator/developer Manjinder Singh. Concept year 2015 and initial public disclosure 2026 per creator, not independently verified.
