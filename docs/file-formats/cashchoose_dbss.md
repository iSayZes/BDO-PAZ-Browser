# `cashchoose.dbss` Format

## Purpose

The Pearl Shop choice packs: a pack lists up to ten
[`cashproduct.dbss`](cashproduct_dbss.md) products and how many of them a
buyer picks (key 1 is a pick-3-of-6 pet pack). The Pearl Shop Lua
(`panel_pearlshop.luac`, `panel_ingamecashshop.luac`) reads a pack through
the getters of the cash product that sells it: `isChooseCash()`,
`mustChooseCount()`, `isChooseDuplicaite()`, `chooseCashCount()` and
`getChooseCashByIndex(index)`, which returns the product in slot `index`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes   | Records          | Row bytes                  |
| ------ | -------------- | ------- | ----------------------- | ------- | ---------------- | -------------------------- |
| 3      | 1590 and later | 3483    | `cashchoose.dbss`       | 191,114 | 1,329 Row        | 139 to 168, 144 on average |
| 3      | 1590 and later | 3483    | `cashchooseoffset.dbss` | 13,294  | 1,329 Offset Row | 10                         |
| 2      | 1327 to 1587   | 1587    | `cashchoose.dbss`       | 52,142  | 398 Row          | 131                        |
| 2      | 1327 to 1587   | 1587    | `cashchooseoffset.dbss` | 3,984   | 398 Offset Row   | 10                         |
| 1      | 1286 to 1324   | 1324    | `cashchoose.dbss`       | 23,758  | 214 Row          | 111                        |
| 1      | 1286 to 1324   | 1324    | `cashchooseoffset.dbss` | 2,144   | 214 Offset Row   | 10                         |

| Layout | File                    | Known              | Unknown    |
| ------ | ----------------------- | ------------------ | ---------- |
| 3      | `cashchoose.dbss`       | 191,114 B (100.0%) | 0 B (0.0%) |
| 3      | `cashchooseoffset.dbss` | 13,294 B (100.0%)  | 0 B (0.0%) |
| 2      | `cashchoose.dbss`       | 52,142 B (100.0%)  | 0 B (0.0%) |
| 2      | `cashchooseoffset.dbss` | 3,984 B (100.0%)   | 0 B (0.0%) |
| 1      | `cashchoose.dbss`       | 23,758 B (100.0%)  | 0 B (0.0%) |
| 1      | `cashchooseoffset.dbss` | 2,144 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `91de3b48d3d5`  |
| 3482   | Layout 3 | `91de3b48d3d5`  |
| 3474   | Layout 3 | `91de3b48d3d5`  |
| 3473   | Layout 3 | `91de3b48d3d5`  |
| 3464   | Layout 3 | `91de3b48d3d5`  |
| 3458   | Layout 3 | `91de3b48d3d5`  |
| 3454   | Layout 3 | `91de3b48d3d5`  |
| 3444   | Layout 3 | `91de3b48d3d5`  |
| 3435   | Layout 3 | `91de3b48d3d5`  |
| 3426   | Layout 3 | `91de3b48d3d5`  |
| 3418   | Layout 3 | `91de3b48d3d5`  |
| 3412   | Layout 3 | `91de3b48d3d5`  |
| 3402   | Layout 3 | `91de3b48d3d5`  |
| 3396   | Layout 3 | `91de3b48d3d5`  |
| 3387   | Layout 3 | `91de3b48d3d5`  |
| 3381   | Layout 3 | `91de3b48d3d5`  |
| 3373   | Layout 3 | `91de3b48d3d5`  |
| 3364   | Layout 3 | `91de3b48d3d5`  |
| 3356   | Layout 3 | `91de3b48d3d5`  |
| 3349   | Layout 3 | `91de3b48d3d5`  |
| 3342   | Layout 3 | `91de3b48d3d5`  |
| 3335   | Layout 3 | `91de3b48d3d5`  |
| 3326   | Layout 3 | `91de3b48d3d5`  |
| 3321   | Layout 3 | `91de3b48d3d5`  |
| 3314   | Layout 3 | `91de3b48d3d5`  |
| 3303   | Layout 3 | `91de3b48d3d5`  |
| 3302   | Layout 3 | `91de3b48d3d5`  |
| 3293   | Layout 3 | `91de3b48d3d5`  |
| 3283   | Layout 3 | `91de3b48d3d5`  |
| 3275   | Layout 3 | `91de3b48d3d5`  |
| 3267   | Layout 3 | `91de3b48d3d5`  |
| 3258   | Layout 3 | `91de3b48d3d5`  |
| 3251   | Layout 3 | `91de3b48d3d5`  |
| 3242   | Layout 3 | `91de3b48d3d5`  |
| 3235   | Layout 3 | `91de3b48d3d5`  |
| 3229   | Layout 3 | `91de3b48d3d5`  |
| 3212   | Layout 3 | `91de3b48d3d5`  |
| 3203   | Layout 3 | `91de3b48d3d5`  |
| 3193   | Layout 3 | `91de3b48d3d5`  |
| 3186   | Layout 3 | `91de3b48d3d5`  |
| 3177   | Layout 3 | `91de3b48d3d5`  |
| 3169   | Layout 3 | `91de3b48d3d5`  |
| 3158   | Layout 3 | `91de3b48d3d5`  |
| 3151   | Layout 3 | `91de3b48d3d5`  |
| 3144   | Layout 3 | `91de3b48d3d5`  |
| 3133   | Layout 3 | `91de3b48d3d5`  |
| 3125   | Layout 3 | `91de3b48d3d5`  |
| 3118   | Layout 3 | `91de3b48d3d5`  |
| 3111   | Layout 3 | `91de3b48d3d5`  |
| 3103   | Layout 3 | `91de3b48d3d5`  |
| 3095   | Layout 3 | `91de3b48d3d5`  |
| 3086   | Layout 3 | `91de3b48d3d5`  |
| 3072   | Layout 3 | `91de3b48d3d5`  |
| 3062   | Layout 3 | `91de3b48d3d5`  |
| 3052   | Layout 3 | `91de3b48d3d5`  |
| 3045   | Layout 3 | `91de3b48d3d5`  |
| 3037   | Layout 3 | `91de3b48d3d5`  |
| 3030   | Layout 3 | `91de3b48d3d5`  |
| 3021   | Layout 3 | `91de3b48d3d5`  |
| 3012   | Layout 3 | `91de3b48d3d5`  |
| 3002   | Layout 3 | `91de3b48d3d5`  |
| 2995   | Layout 3 | `91de3b48d3d5`  |
| 2987   | Layout 3 | `91de3b48d3d5`  |
| 2978   | Layout 3 | `91de3b48d3d5`  |
| 2970   | Layout 3 | `91de3b48d3d5`  |
| 2959   | Layout 3 | `91de3b48d3d5`  |
| 2951   | Layout 3 | `91de3b48d3d5`  |
| 2942   | Layout 3 | `91de3b48d3d5`  |
| 2935   | Layout 3 | `91de3b48d3d5`  |
| 2932   | Layout 3 | `91de3b48d3d5`  |
| 2923   | Layout 3 | `91de3b48d3d5`  |
| 2919   | Layout 3 | `91de3b48d3d5`  |
| 2907   | Layout 3 | `91de3b48d3d5`  |
| 2900   | Layout 3 | `91de3b48d3d5`  |
| 2891   | Layout 3 | `91de3b48d3d5`  |
| 2882   | Layout 3 | `91de3b48d3d5`  |
| 2872   | Layout 3 | `91de3b48d3d5`  |
| 2863   | Layout 3 | `91de3b48d3d5`  |
| 2855   | Layout 3 | `91de3b48d3d5`  |
| 2849   | Layout 3 | `91de3b48d3d5`  |
| 2844   | Layout 3 | `91de3b48d3d5`  |
| 2834   | Layout 3 | `91de3b48d3d5`  |
| 2825   | Layout 3 | `91de3b48d3d5`  |
| 2819   | Layout 3 | `91de3b48d3d5`  |
| 2811   | Layout 3 | `91de3b48d3d5`  |
| 2803   | Layout 3 | `91de3b48d3d5`  |
| 2794   | Layout 3 | `91de3b48d3d5`  |
| 2783   | Layout 3 | `91de3b48d3d5`  |
| 2774   | Layout 3 | `91de3b48d3d5`  |
| 2765   | Layout 3 | `91de3b48d3d5`  |
| 2756   | Layout 3 | `91de3b48d3d5`  |
| 2750   | Layout 3 | `91de3b48d3d5`  |
| 2743   | Layout 3 | `91de3b48d3d5`  |
| 2736   | Layout 3 | `91de3b48d3d5`  |
| 2726   | Layout 3 | `91de3b48d3d5`  |
| 2717   | Layout 3 | `91de3b48d3d5`  |
| 2709   | Layout 3 | `91de3b48d3d5`  |
| 2703   | Layout 3 | `91de3b48d3d5`  |
| 2695   | Layout 3 | `91de3b48d3d5`  |
| 2684   | Layout 3 | `91de3b48d3d5`  |
| 2672   | Layout 3 | `91de3b48d3d5`  |
| 2665   | Layout 3 | `91de3b48d3d5`  |
| 2657   | Layout 3 | `91de3b48d3d5`  |
| 2649   | Layout 3 | `91de3b48d3d5`  |
| 2644   | Layout 3 | `91de3b48d3d5`  |
| 2637   | Layout 3 | `91de3b48d3d5`  |
| 2629   | Layout 3 | `91de3b48d3d5`  |
| 2619   | Layout 3 | `91de3b48d3d5`  |
| 2612   | Layout 3 | `91de3b48d3d5`  |
| 2606   | Layout 3 | `91de3b48d3d5`  |
| 2602   | Layout 3 | `91de3b48d3d5`  |
| 2601   | Layout 3 | `91de3b48d3d5`  |
| 2592   | Layout 3 | `91de3b48d3d5`  |
| 2583   | Layout 3 | `91de3b48d3d5`  |
| 2575   | Layout 3 | `91de3b48d3d5`  |
| 2567   | Layout 3 | `91de3b48d3d5`  |
| 2560   | Layout 3 | `91de3b48d3d5`  |
| 2553   | Layout 3 | `91de3b48d3d5`  |
| 2545   | Layout 3 | `91de3b48d3d5`  |
| 2538   | Layout 3 | `91de3b48d3d5`  |
| 2529   | Layout 3 | `91de3b48d3d5`  |
| 2519   | Layout 3 | `91de3b48d3d5`  |
| 2513   | Layout 3 | `91de3b48d3d5`  |
| 2510   | Layout 3 | `91de3b48d3d5`  |
| 2507   | Layout 3 | `91de3b48d3d5`  |
| 2503   | Layout 3 | `91de3b48d3d5`  |
| 2498   | Layout 3 | `91de3b48d3d5`  |
| 2492   | Layout 3 | `91de3b48d3d5`  |
| 2487   | Layout 3 | `91de3b48d3d5`  |
| 2480   | Layout 3 | `91de3b48d3d5`  |
| 2474   | Layout 3 | `91de3b48d3d5`  |
| 2468   | Layout 3 | `91de3b48d3d5`  |
| 2460   | Layout 3 | `91de3b48d3d5`  |
| 2453   | Layout 3 | `91de3b48d3d5`  |
| 2444   | Layout 3 | `91de3b48d3d5`  |
| 2438   | Layout 3 | `91de3b48d3d5`  |
| 2434   | Layout 3 | `91de3b48d3d5`  |
| 2429   | Layout 3 | `91de3b48d3d5`  |
| 2421   | Layout 3 | `91de3b48d3d5`  |
| 2414   | Layout 3 | `91de3b48d3d5`  |
| 2407   | Layout 3 | `91de3b48d3d5`  |
| 2401   | Layout 3 | `91de3b48d3d5`  |
| 2397   | Layout 3 | `91de3b48d3d5`  |
| 2393   | Layout 3 | `91de3b48d3d5`  |
| 2384   | Layout 3 | `91de3b48d3d5`  |
| 2378   | Layout 3 | `91de3b48d3d5`  |
| 2372   | Layout 3 | `91de3b48d3d5`  |
| 2358   | Layout 3 | `91de3b48d3d5`  |
| 2352   | Layout 3 | `91de3b48d3d5`  |
| 2347   | Layout 3 | `91de3b48d3d5`  |
| 2343   | Layout 3 | `91de3b48d3d5`  |
| 2335   | Layout 3 | `91de3b48d3d5`  |
| 2327   | Layout 3 | `91de3b48d3d5`  |
| 2324   | Layout 3 | `91de3b48d3d5`  |
| 2319   | Layout 3 | `91de3b48d3d5`  |
| 2313   | Layout 3 | `91de3b48d3d5`  |
| 2308   | Layout 3 | `91de3b48d3d5`  |
| 2302   | Layout 3 | `91de3b48d3d5`  |
| 2295   | Layout 3 | `91de3b48d3d5`  |
| 2290   | Layout 3 | `91de3b48d3d5`  |
| 2284   | Layout 3 | `91de3b48d3d5`  |
| 2276   | Layout 3 | `91de3b48d3d5`  |
| 2269   | Layout 3 | `91de3b48d3d5`  |
| 2259   | Layout 3 | `91de3b48d3d5`  |
| 2250   | Layout 3 | `91de3b48d3d5`  |
| 2243   | Layout 3 | `91de3b48d3d5`  |
| 2235   | Layout 3 | `91de3b48d3d5`  |
| 2229   | Layout 3 | `91de3b48d3d5`  |
| 2224   | Layout 3 | `91de3b48d3d5`  |
| 2218   | Layout 3 | `91de3b48d3d5`  |
| 2215   | Layout 3 | `91de3b48d3d5`  |
| 2207   | Layout 3 | `91de3b48d3d5`  |
| 2203   | Layout 3 | `91de3b48d3d5`  |
| 2196   | Layout 3 | `91de3b48d3d5`  |
| 2192   | Layout 3 | `91de3b48d3d5`  |
| 2189   | Layout 3 | `91de3b48d3d5`  |
| 2183   | Layout 3 | `91de3b48d3d5`  |
| 2179   | Layout 3 | `91de3b48d3d5`  |
| 2171   | Layout 3 | `91de3b48d3d5`  |
| 2163   | Layout 3 | `91de3b48d3d5`  |
| 2156   | Layout 3 | `91de3b48d3d5`  |
| 2151   | Layout 3 | `91de3b48d3d5`  |
| 2147   | Layout 3 | `91de3b48d3d5`  |
| 2142   | Layout 3 | `91de3b48d3d5`  |
| 2138   | Layout 3 | `91de3b48d3d5`  |
| 2134   | Layout 3 | `91de3b48d3d5`  |
| 2130   | Layout 3 | `91de3b48d3d5`  |
| 2122   | Layout 3 | `91de3b48d3d5`  |
| 2107   | Layout 3 | `91de3b48d3d5`  |
| 2098   | Layout 3 | `91de3b48d3d5`  |
| 2089   | Layout 3 | `91de3b48d3d5`  |
| 2081   | Layout 3 | `91de3b48d3d5`  |
| 2073   | Layout 3 | `91de3b48d3d5`  |
| 2067   | Layout 3 | `91de3b48d3d5`  |
| 2063   | Layout 3 | `91de3b48d3d5`  |
| 2059   | Layout 3 | `91de3b48d3d5`  |
| 2052   | Layout 3 | `91de3b48d3d5`  |
| 2044   | Layout 3 | `91de3b48d3d5`  |
| 2039   | Layout 3 | `91de3b48d3d5`  |
| 2032   | Layout 3 | `91de3b48d3d5`  |
| 2025   | Layout 3 | `91de3b48d3d5`  |
| 2011   | Layout 3 | `91de3b48d3d5`  |
| 2005   | Layout 3 | `91de3b48d3d5`  |
| 2000   | Layout 3 | `91de3b48d3d5`  |
| 1996   | Layout 3 | `91de3b48d3d5`  |
| 1991   | Layout 3 | `91de3b48d3d5`  |
| 1985   | Layout 3 | `91de3b48d3d5`  |
| 1980   | Layout 3 | `91de3b48d3d5`  |
| 1969   | Layout 3 | `91de3b48d3d5`  |
| 1964   | Layout 3 | `91de3b48d3d5`  |
| 1958   | Layout 3 | `91de3b48d3d5`  |
| 1950   | Layout 3 | `91de3b48d3d5`  |
| 1945   | Layout 3 | `91de3b48d3d5`  |
| 1937   | Layout 3 | `91de3b48d3d5`  |
| 1933   | Layout 3 | `91de3b48d3d5`  |
| 1927   | Layout 3 | `91de3b48d3d5`  |
| 1921   | Layout 3 | `91de3b48d3d5`  |
| 1914   | Layout 3 | `91de3b48d3d5`  |
| 1908   | Layout 3 | `91de3b48d3d5`  |
| 1897   | Layout 3 | `91de3b48d3d5`  |
| 1892   | Layout 3 | `91de3b48d3d5`  |
| 1886   | Layout 3 | `91de3b48d3d5`  |
| 1881   | Layout 3 | `91de3b48d3d5`  |
| 1871   | Layout 3 | `91de3b48d3d5`  |
| 1866   | Layout 3 | `91de3b48d3d5`  |
| 1862   | Layout 3 | `91de3b48d3d5`  |
| 1854   | Layout 3 | `91de3b48d3d5`  |
| 1846   | Layout 3 | `91de3b48d3d5`  |
| 1838   | Layout 3 | `91de3b48d3d5`  |
| 1832   | Layout 3 | `91de3b48d3d5`  |
| 1826   | Layout 3 | `91de3b48d3d5`  |
| 1822   | Layout 3 | `91de3b48d3d5`  |
| 1818   | Layout 3 | `91de3b48d3d5`  |
| 1804   | Layout 3 | `91de3b48d3d5`  |
| 1794   | Layout 3 | `91de3b48d3d5`  |
| 1790   | Layout 3 | `91de3b48d3d5`  |
| 1784   | Layout 3 | `91de3b48d3d5`  |
| 1774   | Layout 3 | `91de3b48d3d5`  |
| 1771   | Layout 3 | `91de3b48d3d5`  |
| 1762   | Layout 3 | `91de3b48d3d5`  |
| 1759   | Layout 3 | `91de3b48d3d5`  |
| 1754   | Layout 3 | `91de3b48d3d5`  |
| 1749   | Layout 3 | `91de3b48d3d5`  |
| 1743   | Layout 3 | `91de3b48d3d5`  |
| 1737   | Layout 3 | `91de3b48d3d5`  |
| 1731   | Layout 3 | `91de3b48d3d5`  |
| 1725   | Layout 3 | `91de3b48d3d5`  |
| 1717   | Layout 3 | `91de3b48d3d5`  |
| 1710   | Layout 3 | `91de3b48d3d5`  |
| 1704   | Layout 3 | `91de3b48d3d5`  |
| 1698   | Layout 3 | `91de3b48d3d5`  |
| 1690   | Layout 3 | `91de3b48d3d5`  |
| 1685   | Layout 3 | `91de3b48d3d5`  |
| 1680   | Layout 3 | `91de3b48d3d5`  |
| 1674   | Layout 3 | `91de3b48d3d5`  |
| 1668   | Layout 3 | `91de3b48d3d5`  |
| 1659   | Layout 3 | `91de3b48d3d5`  |
| 1649   | Layout 3 | `91de3b48d3d5`  |
| 1642   | Layout 3 | `91de3b48d3d5`  |
| 1636   | Layout 3 | `91de3b48d3d5`  |
| 1628   | Layout 3 | `91de3b48d3d5`  |
| 1622   | Layout 3 | `91de3b48d3d5`  |
| 1614   | Layout 3 | `91de3b48d3d5`  |
| 1608   | Layout 3 | `91de3b48d3d5`  |
| 1602   | Layout 3 | `91de3b48d3d5`  |
| 1598   | Layout 3 | `91de3b48d3d5`  |
| 1594   | Layout 3 | `91de3b48d3d5`  |
| 1590   | Layout 3 | `91de3b48d3d5`  |
| 1587   | Layout 2 | `91de3b48d3d5`  |
| 1584   | Layout 2 | `91de3b48d3d5`  |
| 1579   | Layout 2 | `91de3b48d3d5`  |
| 1572   | Layout 2 | `91de3b48d3d5`  |
| 1565   | Layout 2 | `91de3b48d3d5`  |
| 1559   | Layout 2 | `91de3b48d3d5`  |
| 1554   | Layout 2 | `91de3b48d3d5`  |
| 1547   | Layout 2 | `91de3b48d3d5`  |
| 1537   | Layout 2 | `91de3b48d3d5`  |
| 1529   | Layout 2 | `91de3b48d3d5`  |
| 1524   | Layout 2 | `91de3b48d3d5`  |
| 1519   | Layout 2 | `91de3b48d3d5`  |
| 1509   | Layout 2 | `91de3b48d3d5`  |
| 1506   | Layout 2 | `91de3b48d3d5`  |
| 1504   | Layout 2 | `91de3b48d3d5`  |
| 1500   | Layout 2 | `91de3b48d3d5`  |
| 1493   | Layout 2 | `91de3b48d3d5`  |
| 1489   | Layout 2 | `91de3b48d3d5`  |
| 1485   | Layout 2 | `91de3b48d3d5`  |
| 1481   | Layout 2 | `91de3b48d3d5`  |
| 1474   | Layout 2 | `91de3b48d3d5`  |
| 1466   | Layout 2 | `91de3b48d3d5`  |
| 1462   | Layout 2 | `91de3b48d3d5`  |
| 1459   | Layout 2 | `91de3b48d3d5`  |
| 1453   | Layout 2 | `91de3b48d3d5`  |
| 1450   | Layout 2 | `91de3b48d3d5`  |
| 1445   | Layout 2 | `91de3b48d3d5`  |
| 1439   | Layout 2 | `91de3b48d3d5`  |
| 1433   | Layout 2 | `91de3b48d3d5`  |
| 1430   | Layout 2 | `91de3b48d3d5`  |
| 1426   | Layout 2 | `91de3b48d3d5`  |
| 1421   | Layout 2 | `91de3b48d3d5`  |
| 1417   | Layout 2 | `91de3b48d3d5`  |
| 1416   | Layout 2 | `91de3b48d3d5`  |
| 1409   | Layout 2 | `91de3b48d3d5`  |
| 1405   | Layout 2 | `91de3b48d3d5`  |
| 1401   | Layout 2 | `91de3b48d3d5`  |
| 1396   | Layout 2 | `91de3b48d3d5`  |
| 1391   | Layout 2 | `91de3b48d3d5`  |
| 1390   | Layout 2 | `91de3b48d3d5`  |
| 1386   | Layout 2 | `91de3b48d3d5`  |
| 1381   | Layout 2 | `91de3b48d3d5`  |
| 1379   | Layout 2 | `91de3b48d3d5`  |
| 1372   | Layout 2 | `91de3b48d3d5`  |
| 1366   | Layout 2 | `91de3b48d3d5`  |
| 1364   | Layout 2 | `91de3b48d3d5`  |
| 1363   | Layout 2 | `91de3b48d3d5`  |
| 1360   | Layout 2 | `91de3b48d3d5`  |
| 1358   | Layout 2 | `91de3b48d3d5`  |
| 1355   | Layout 2 | `91de3b48d3d5`  |
| 1351   | Layout 2 | `91de3b48d3d5`  |
| 1348   | Layout 2 | `91de3b48d3d5`  |
| 1346   | Layout 2 | `91de3b48d3d5`  |
| 1341   | Layout 2 | `91de3b48d3d5`  |
| 1340   | Layout 2 | `91de3b48d3d5`  |
| 1338   | Layout 2 | `91de3b48d3d5`  |
| 1335   | Layout 2 | `91de3b48d3d5`  |
| 1333   | Layout 2 | `91de3b48d3d5`  |
| 1329   | Layout 2 | `91de3b48d3d5`  |
| 1327   | Layout 2 | `91de3b48d3d5`  |
| 1324   | Layout 1 | `91de3b48d3d5`  |
| 1321   | Layout 1 | `91de3b48d3d5`  |
| 1319   | Layout 1 | `91de3b48d3d5`  |
| 1318   | Layout 1 | `91de3b48d3d5`  |
| 1316   | Layout 1 | `91de3b48d3d5`  |
| 1313   | Layout 1 | `91de3b48d3d5`  |
| 1311   | Layout 1 | `91de3b48d3d5`  |
| 1309   | Layout 1 | `91de3b48d3d5`  |
| 1304   | Layout 1 | `91de3b48d3d5`  |
| 1292   | Layout 1 | `91de3b48d3d5`  |
| 1286   | Layout 1 | `91de3b48d3d5`  |
| 1280   | No file  | `91de3b48d3d5`  |
| 1276   | No file  | `91de3b48d3d5`  |
| 1267   | No file  | `91de3b48d3d5`  |
| 1261   | No file  | `91de3b48d3d5`  |
| 1256   | No file  | `91de3b48d3d5`  |
| 1250   | No file  | `91de3b48d3d5`  |
| 1246   | No file  | `91de3b48d3d5`  |
| 1239   | No file  | `91de3b48d3d5`  |
| 1230   | No file  | `91de3b48d3d5`  |
| 1226   | No file  | `91de3b48d3d5`  |
| 1220   | No file  | `91de3b48d3d5`  |
| 1217   | No file  | `91de3b48d3d5`  |
| 1211   | No file  | `91de3b48d3d5`  |
| 1210   | No file  | `91de3b48d3d5`  |
| 1208   | No file  | `91de3b48d3d5`  |
| 1203   | No file  | `91de3b48d3d5`  |
| 1197   | No file  | `91de3b48d3d5`  |
| 1194   | No file  | `91de3b48d3d5`  |
| 1192   | No file  | `91de3b48d3d5`  |
| 1187   | No file  | `91de3b48d3d5`  |
| 1183   | No file  | `91de3b48d3d5`  |
| 1177   | No file  | `91de3b48d3d5`  |
| 1173   | No file  | `91de3b48d3d5`  |
| 1167   | No file  | `91de3b48d3d5`  |
| 1164   | No file  | `91de3b48d3d5`  |
| 1156   | No file  | `91de3b48d3d5`  |
| 1149   | No file  | `91de3b48d3d5`  |
| 1144   | No file  | `91de3b48d3d5`  |
| 1137   | No file  | `91de3b48d3d5`  |
| 1132   | No file  | `91de3b48d3d5`  |
| 1127   | No file  | `91de3b48d3d5`  |
| 1122   | No file  | `91de3b48d3d5`  |
| 1118   | No file  | `91de3b48d3d5`  |
| 1114   | No file  | `91de3b48d3d5`  |
| 1109   | No file  | `91de3b48d3d5`  |
| 1102   | No file  | `91de3b48d3d5`  |
| 1096   | No file  | `91de3b48d3d5`  |
| 1088   | No file  | `91de3b48d3d5`  |
| 1081   | No file  | `91de3b48d3d5`  |
| 1076   | No file  | `91de3b48d3d5`  |
| 1069   | No file  | `91de3b48d3d5`  |
| 1064   | No file  | `91de3b48d3d5`  |
| 1058   | No file  | `91de3b48d3d5`  |
| 1051   | No file  | `91de3b48d3d5`  |
| 1044   | No file  | `91de3b48d3d5`  |
| 1036   | No file  | `91de3b48d3d5`  |
| 1026   | No file  | `91de3b48d3d5`  |
| 1016   | No file  | `91de3b48d3d5`  |
| 1009   | No file  | `91de3b48d3d5`  |
| 1005   | No file  | `91de3b48d3d5`  |
| 1000   | No file  | `91de3b48d3d5`  |
| 998    | No file  | `91de3b48d3d5`  |
| 990    | No file  | `91de3b48d3d5`  |
| 979    | No file  | `91de3b48d3d5`  |
| 972    | No file  | `91de3b48d3d5`  |
| 963    | No file  | `91de3b48d3d5`  |
| 955    | No file  | `91de3b48d3d5`  |
| 946    | No file  | `91de3b48d3d5`  |
| 938    | No file  | `91de3b48d3d5`  |
| 927    | No file  | `91de3b48d3d5`  |
| 911    | No file  | `91de3b48d3d5`  |
| 904    | No file  | `91de3b48d3d5`  |
| 899    | No file  | `91de3b48d3d5`  |
| 894    | No file  | `91de3b48d3d5`  |
| 885    | No file  | `91de3b48d3d5`  |
| 879    | No file  | `91de3b48d3d5`  |
| 872    | No file  | `91de3b48d3d5`  |
| 864    | No file  | `91de3b48d3d5`  |
| 855    | No file  | `91de3b48d3d5`  |
| 853    | No file  | `91de3b48d3d5`  |
| 845    | No file  | `91de3b48d3d5`  |
| 837    | No file  | `91de3b48d3d5`  |
| 829    | No file  | `91de3b48d3d5`  |
| 822    | No file  | `91de3b48d3d5`  |
| 814    | No file  | `91de3b48d3d5`  |
| 805    | No file  | `91de3b48d3d5`  |
| 794    | No file  | `91de3b48d3d5`  |
| 787    | No file  | `91de3b48d3d5`  |
| 780    | No file  | `91de3b48d3d5`  |
| 771    | No file  | `91de3b48d3d5`  |
| 760    | No file  | `91de3b48d3d5`  |
| 748    | No file  | `91de3b48d3d5`  |
| 741    | No file  | `91de3b48d3d5`  |
| 736    | No file  | `91de3b48d3d5`  |
| 731    | No file  | `91de3b48d3d5`  |
| 723    | No file  | `91de3b48d3d5`  |
| 711    | No file  | `91de3b48d3d5`  |
| 707    | No file  | `91de3b48d3d5`  |
| 697    | No file  | `91de3b48d3d5`  |
| 689    | No file  | `91de3b48d3d5`  |
| 683    | No file  | `91de3b48d3d5`  |
| 678    | No file  | `91de3b48d3d5`  |
| 670    | No file  | `91de3b48d3d5`  |
| 661    | No file  | `91de3b48d3d5`  |
| 656    | No file  | `91de3b48d3d5`  |
| 652    | No file  | `91de3b48d3d5`  |
| 643    | No file  | `91de3b48d3d5`  |
| 637    | No file  | `91de3b48d3d5`  |
| 630    | No file  | `91de3b48d3d5`  |
| 627    | No file  | `91de3b48d3d5`  |
| 621    | No file  | `91de3b48d3d5`  |
| 617    | No file  | `91de3b48d3d5`  |
| 615    | No file  | `91de3b48d3d5`  |
| 606    | No file  | `91de3b48d3d5`  |
| 599    | No file  | `91de3b48d3d5`  |
| 592    | No file  | `91de3b48d3d5`  |
| 586    | No file  | `91de3b48d3d5`  |
| 577    | No file  | `91de3b48d3d5`  |
| 569    | No file  | `91de3b48d3d5`  |
| 561    | No file  | `91de3b48d3d5`  |
| 554    | No file  | `91de3b48d3d5`  |
| 542    | No file  | `91de3b48d3d5`  |
| 532    | No file  | `91de3b48d3d5`  |
| 531    | No file  | `91de3b48d3d5`  |
| 526    | No file  | `91de3b48d3d5`  |
| 521    | No file  | `91de3b48d3d5`  |
| 517    | No file  | `91de3b48d3d5`  |
| 510    | No file  | `91de3b48d3d5`  |
| 508    | No file  | `91de3b48d3d5`  |
| 504    | No file  | `91de3b48d3d5`  |
| 497    | No file  | `91de3b48d3d5`  |
| 491    | No file  | `91de3b48d3d5`  |
| 485    | No file  | `91de3b48d3d5`  |
| 478    | No file  | `91de3b48d3d5`  |
| 472    | No file  | `91de3b48d3d5`  |
| 466    | No file  | `91de3b48d3d5`  |
| 457    | No file  | `91de3b48d3d5`  |
| 452    | No file  | `91de3b48d3d5`  |
| 449    | No file  | `91de3b48d3d5`  |
| 435    | No file  | `91de3b48d3d5`  |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                                                                       |
| ----------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `cashchooseoffset.dbss` | Optional | `choose_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`   | Optional | Names of the listed products (LOC type 50)                                                 |

All multi-byte values are little-endian.

## Layout 3

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type       | Field | Notes                |
| ------- | ---------- | ----- | -------------------- |
| `+0x00` | u32        | count | Number of packs      |
| `+0x04` | Row[count] | rows  | See Row              |

### Row (variable: 139 bytes + icon text)

| Offset                   | Type    | Field               | Notes                                                                                                   |
| ------------------------ | ------- | ------------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00`                  | u16     | choose_key          | Pack key; the `ChooseProduct` value of the cash products that sell the pack, see Field Names            |
| `+0x02`                  | u32     | choose_count        | Products the buyer picks, `mustChooseCount()`                                                           |
| `+0x06`                  | u8      | is_choose_duplicate | `1`: the buyer may pick one product more than once, `isChooseDuplicaite()`                              |
| `+0x07`                  | u32[10] | include_product_no  | `cashproduct.dbss` product IDs, `getChooseCashByIndex(index)`; filled from slot 0, `0` in unused slots  |
| `+0x2F`                  | u64[10] | stack_count         | Count per product slot; `1` in every filled slot and `0` in every unused one on clients 1784 and 3482   |
| `+0x7F`                  | str8    | display_icon_path   | Pack icon relative to `ui_texture/icon/` (`New_Icon/09_Cash/00021005.dds`), or empty                    |
| `display_icon_path+0x00` | u32     | choose_cash_count   | Filled product slots, `chooseCashCount()`; equals the nonzero `include_product_no` slots on every row of clients 1784 and 3482 |

A row is 139 bytes plus the icon path. On client 3482 the file holds
1,329 packs, 220 of them with an icon path (28 or 29 characters).

### `cashchooseoffset.dbss`

Bare offset table into `cashchoose.dbss` (no PABR magic, no trailer), read
by `parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type              | Field | Notes                              |
| ------- | ----------------- | ----- | ---------------------------------- |
| `+0x00` | u32               | count | Equals the `cashchoose.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                     |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                          |
| ------- | ---- | ----------- | -------------------------------------------------------------- |
| `+0x00` | u16  | choose_key  | Key of the row it points at                                    |
| `+0x02` | u32  | data_offset | Absolute offset of the row in `cashchoose.dbss`, at `choose_key` |
| `+0x06` | u32  | data_size   | The whole row                                                  |

The index rows are in another order than the file; on clients 1784 and
3482 every index row points at the row with its key and the rows tile the
file from byte 4 to its end.

## Layout 2

Older clients store no icon path: the row ends with `choose_cash_count`
right after `stack_count`. Only the Row differs from Layout 3.

### Row (131 bytes)

| Offset  | Type    | Field               | Notes |
| ------- | ------- | ------------------- | ----- |
| `+0x00` | u16     | choose_key          |       |
| `+0x02` | u32     | choose_count        |       |
| `+0x06` | u8      | is_choose_duplicate |       |
| `+0x07` | u32[10] | include_product_no  |       |
| `+0x2F` | u64[10] | stack_count         |       |
| `+0x7F` | u32     | choose_cash_count   |       |

## Layout 1

The oldest clients store the product IDs as u16 (the first row of client
1286 lists products 61509, 61506, 61507 and 61508) and no icon path. Only the Row differs
from Layout 2.

### Row (111 bytes)

| Offset  | Type    | Field               | Notes |
| ------- | ------- | ------------------- | ----- |
| `+0x00` | u16     | choose_key          |       |
| `+0x02` | u32     | choose_count        |       |
| `+0x06` | u8      | is_choose_duplicate |       |
| `+0x07` | u16[10] | include_product_no  |       |
| `+0x1B` | u64[10] | stack_count         |       |
| `+0x6B` | u32     | choose_cash_count   |       |

## Field Names

The names come from the `ChooseCashProduct_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784 (`Index`, `IsChooseDuplicate`,
`ChooseCount`, `IncludeProductNo0` to `9`, `StackCount0` to `9`,
`DisplayIconPath`) and from the Pearl Shop Lua getters above.
`choose_cash_count` has no sheet column; the name follows
`chooseCashCount()`, which the Lua loops over before it calls
`getChooseCashByIndex()`.

| Field                | Match with the sheet (client 1784, 497 keys) | Match (client 3482, 497 shared keys) |
| -------------------- | --------------------------------------------- | ------------------------------------- |
| `choose_key`         | 497 of 497 keys                               | 497 of 497 keys                       |
| `is_choose_duplicate`| 497                                           | 494                                   |
| `choose_count`       | 497                                           | 491                                   |
| `include_product_no` | 481                                           | 459                                   |
| `stack_count`        | 481                                           | 476                                   |
| `display_icon_path`  | 497 (empty in the sheet and the file)         | 492 (5 rows gained an icon)           |

On the 16 client 1784 rows that miss, the sheet lists one product more than
the file (key 514 adds product 29147 in slot 6), and every one of those 16
products is in the client 1784 `cashproduct.dbss`. The client 3482 misses
are rows changed after client 1784: 465 of the 497 shared keys hold the
same row on clients 1784 and 3482.

The `ChooseProduct` column of the `CashProduct_Table` sheet on client 1784
holds a choose key on 848 of 11,836 products; they point at 491 of the 497
keys of the client 1784 file.

## Notes

- `choose_count` is `1` on 855 of 1,329 packs and up to `10` (client
  3482). On 37 packs it is larger than `choose_cash_count`; all 37 have
  `is_choose_duplicate = 1`, so the buyer picks some products more than
  once.
- 7,732 product slots are filled on client 3482, and every one of those
  product IDs is a `cashproductoffset.dbss` key.
- Stored icon paths start at `New_Icon/`, as in
  [`itemenchant.dbss`](itemenchant_dbss.md), so the PAZ path is the stored
  value lowercased under `ui_texture/icon/`. 219 of the 220 paths of client
  3482 are under `New_Icon/09_Cash/`; one (key 993) is under `New_Icon/03_ETC/`.
- The client 1784 file has no icon paths; the column is empty in the sheet
  too.

## Open Questions

### Where cashproduct.dbss Holds the Choose Key

The Lua reads a pack through the cash product that sells it, and the
`CashProduct_Table` sheet stores that link in `ChooseProduct`. The
`cashproduct.dbss` block keeps it in its undecoded bytes, so the Parsed view
cannot list which products sell a pack yet. Decoding that field in
`cashproduct.dbss` would give the join.
