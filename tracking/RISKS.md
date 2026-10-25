# TongNet — Master Risk Index and Release Blocker Dashboard

**As-of:** 2026-10-25. Existing [50-item A-to-Z audit](../docs/LONG_HORIZON_RISK_AUDIT.md) plus [15 new long-term gaps](../docs/LONG_HORIZON_AUDIT_SUPPLEMENT.md) provide **65 forward-looking conceptual risks**. These are *potential problems* and research, not claims of code vulnerabilities validated in a working chain. Track individual resolution evidence on linked GitHub Issues; do not mark RED solved just because a candidate design exists.

## RED — no real-value mainnet until independently resolved
| Risk refs | Main threat | Task link |
|---|---|---|
| L-51, L-53 | Lost S private key makes private-key-required disaster impossible; stolen S+R keys can kill S | [#3](https://github.com/manbir6-ux/TongNet/issues/3) |
| L-03, L-37, L-52, L-57 | R pre-recovery archive decrypt / archive availability and keyshare collusion | [#4](https://github.com/manbir6-ux/TongNet/issues/27) |
| L-02 | K_S not created until after window, S Box lost/dead | [#5](https://github.com/manbir6-ux/TongNet/issues/28) |
| L-01, L-05, L-35 | t0, exact network-delay compensation and cutoffs in partitions | [#6](https://github.com/manbir6-ux/TongNet/issues/31) |
| L-04 | After-60d locked TONG confiscation and user remedies | [#7](https://github.com/manbir6-ux/TongNet/issues/32) |
| L-12, L-13, L-14 | Claim-code guessing, lost code after LOCK, insufficient Receiver fees | [#8](https://github.com/manbir6-ux/TongNet/issues/26) |
| L-16, L-23, L-24, L-25, L-56 | Startup stake centralization, unpriced TONG bond, token issuance | [#9](https://github.com/manbir6-ux/TongNet/issues/34) [#10](https://github.com/manbir6-ux/TongNet/issues/34) |
| L-08, L-09, L-54 | S DEAD, existing claims and bonded validator voting/withdrawal | [#12](https://github.com/manbir6-ux/TongNet/issues/33) |
| L-17, L-18, L-26, L-27, L-28 | Conservation, consensus determinism, unsafe committee churn or false finality | [#14](https://github.com/manbir6-ux/TongNet/issues/29) [#17](https://github.com/manbir6-ux/TongNet/issues/38) |
| L-10 | 72h activation deadline can burn prefunded nonactivated funds | [#15](https://github.com/manbir6-ux/TongNet/issues/30) |
| L-43 | Australia, foreign law, AML/privacy/financial rights | [#11](https://github.com/manbir6-ux/TongNet/issues/45) |
| L-42 | No audited running implementation, independent operators or complete safe model | [#21](https://github.com/manbir6-ux/TongNet/issues/44) [#22](https://github.com/manbir6-ux/TongNet/issues/46) |

## AMBER — must manage/test over 3/6/12/24 months
L-20 crypto agility; L-21 & L-55 fee/storage bomb; L-22 & L-61 BlackBox privacy/deletion; L-29 committee grinding; L-30 phone uptime; L-31 vendor outage; L-32 archive costs; L-33 empty traffic; L-34 spam; L-36 & L-60 upgrade migration; L-38 malicious quarantine; L-39 & L-62 light-client trust; L-40 data deletion; L-41 upgrade keys; L-44 fund governance; L-45 & L-64 CI supply chain; L-46/47/48 & L-65 stale worker status; L-50 24/7 incident response; L-58 user understanding; L-59 honest operator economics; L-63 key rotation.

## Closure protocol
1. Refer to exact `L-NN` threat text. 2. Write counterexample/test reproducer, proposed mitigations and residual uncertainty in Issue/ADR. 3. Implement unit/property/model/fault/load tests. 4. Independent security review for financial-right severity. 5. Owner-approved change of rules if needed. 6. Close corresponding Issue only with linked evidence and update this dashboard.

**Top immediate blocker:** recoverability paradox when S **private signing key** is lost (#3). Existing method needs that same key; no QR backup can generate an unknown missing key. A new pre-authorised cryptographic recovery path would be a protocol change requiring owner consent.
