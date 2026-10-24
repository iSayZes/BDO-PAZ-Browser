# `plantworkerpassiveskill.bss` Format

## Purpose

Worker passive skill table. The file stores passive skill IDs, inline Korean fallback strings, DDS icon paths, and effect parameter fields used by worker skill UI rows. User-facing names and descriptions should prefer LOC type `22` when available.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes  | Records         | Row bytes               |
| ------ | -------------- | ------- | ----------------------------- | ------ | --------------- | ----------------------- |
| 1      | 1280 and later | 3483    | `plantworkerpassiveskill.bss` | 13,294 | 72 Skill Record | 56 to 72, 56 on average |

| Layout | File                          | Known            | Unknown      |
| ------ | ----------------------------- | ---------------- | ------------ |
| 1      | `plantworkerpassiveskill.bss` | 12,702 B (95.5%) | 592 B (4.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `0957d8a3a4a0`  |
| 3482   | Layout 1             | `0957d8a3a4a0`  |
| 3474   | Layout 1             | `0957d8a3a4a0`  |
| 3473   | Layout 1             | `0957d8a3a4a0`  |
| 3464   | Layout 1             | `0957d8a3a4a0`  |
| 3458   | Layout 1             | `0957d8a3a4a0`  |
| 3454   | Layout 1             | `0957d8a3a4a0`  |
| 3444   | Layout 1             | `0957d8a3a4a0`  |
| 3435   | Layout 1             | `0957d8a3a4a0`  |
| 3426   | Layout 1             | `0957d8a3a4a0`  |
| 3418   | Layout 1             | `0957d8a3a4a0`  |
| 3412   | Layout 1             | `0957d8a3a4a0`  |
| 3402   | Layout 1             | `0957d8a3a4a0`  |
| 3396   | Layout 1             | `0957d8a3a4a0`  |
| 3387   | Layout 1             | `0957d8a3a4a0`  |
| 3381   | Layout 1             | `0957d8a3a4a0`  |
| 3373   | Layout 1             | `0957d8a3a4a0`  |
| 3364   | Layout 1             | `0957d8a3a4a0`  |
| 3356   | Layout 1             | `0957d8a3a4a0`  |
| 3349   | Layout 1             | `0957d8a3a4a0`  |
| 3342   | Layout 1             | `0957d8a3a4a0`  |
| 3335   | Layout 1             | `0957d8a3a4a0`  |
| 3326   | Layout 1             | `0957d8a3a4a0`  |
| 3321   | Layout 1             | `0957d8a3a4a0`  |
| 3314   | Layout 1             | `0957d8a3a4a0`  |
| 3303   | Layout 1             | `0957d8a3a4a0`  |
| 3302   | Layout 1             | `0957d8a3a4a0`  |
| 3293   | Layout 1             | `0957d8a3a4a0`  |
| 3283   | Layout 1             | `0957d8a3a4a0`  |
| 3275   | Layout 1             | `0957d8a3a4a0`  |
| 3267   | Layout 1             | `0957d8a3a4a0`  |
| 3258   | Layout 1             | `0957d8a3a4a0`  |
| 3251   | Layout 1             | `0957d8a3a4a0`  |
| 3242   | Layout 1             | `0957d8a3a4a0`  |
| 3235   | Layout 1             | `0957d8a3a4a0`  |
| 3229   | Layout 1             | `0957d8a3a4a0`  |
| 3212   | Layout 1             | `0957d8a3a4a0`  |
| 3203   | Layout 1             | `0957d8a3a4a0`  |
| 3193   | Layout 1             | `0957d8a3a4a0`  |
| 3186   | Layout 1             | `0957d8a3a4a0`  |
| 3177   | Layout 1             | `0957d8a3a4a0`  |
| 3169   | Layout 1             | `0957d8a3a4a0`  |
| 3158   | Layout 1             | `0957d8a3a4a0`  |
| 3151   | Layout 1             | `0957d8a3a4a0`  |
| 3144   | Layout 1             | `0957d8a3a4a0`  |
| 3133   | Layout 1             | `0957d8a3a4a0`  |
| 3125   | Layout 1             | `0957d8a3a4a0`  |
| 3118   | Layout 1             | `0957d8a3a4a0`  |
| 3111   | Layout 1             | `0957d8a3a4a0`  |
| 3103   | Layout 1             | `0957d8a3a4a0`  |
| 3095   | Layout 1             | `0957d8a3a4a0`  |
| 3086   | Layout 1             | `0957d8a3a4a0`  |
| 3072   | Layout 1             | `0957d8a3a4a0`  |
| 3062   | Layout 1             | `0957d8a3a4a0`  |
| 3052   | Layout 1             | `0957d8a3a4a0`  |
| 3045   | Layout 1             | `0957d8a3a4a0`  |
| 3037   | Layout 1             | `0957d8a3a4a0`  |
| 3030   | Layout 1             | `0957d8a3a4a0`  |
| 3021   | Layout 1             | `0957d8a3a4a0`  |
| 3012   | Layout 1             | `0957d8a3a4a0`  |
| 3002   | Layout 1             | `0957d8a3a4a0`  |
| 2995   | Layout 1             | `0957d8a3a4a0`  |
| 2987   | Layout 1             | `0957d8a3a4a0`  |
| 2978   | Layout 1             | `0957d8a3a4a0`  |
| 2970   | Layout 1             | `0957d8a3a4a0`  |
| 2959   | Layout 1             | `0957d8a3a4a0`  |
| 2951   | Layout 1             | `0957d8a3a4a0`  |
| 2942   | Layout 1             | `0957d8a3a4a0`  |
| 2935   | Layout 1             | `0957d8a3a4a0`  |
| 2932   | Layout 1             | `0957d8a3a4a0`  |
| 2923   | Layout 1             | `0957d8a3a4a0`  |
| 2919   | Layout 1             | `0957d8a3a4a0`  |
| 2907   | Layout 1             | `0957d8a3a4a0`  |
| 2900   | Layout 1             | `0957d8a3a4a0`  |
| 2891   | Layout 1             | `0957d8a3a4a0`  |
| 2882   | Layout 1             | `0957d8a3a4a0`  |
| 2872   | Layout 1             | `0957d8a3a4a0`  |
| 2863   | Layout 1             | `0957d8a3a4a0`  |
| 2855   | Layout 1             | `0957d8a3a4a0`  |
| 2849   | Layout 1             | `0957d8a3a4a0`  |
| 2844   | Layout 1             | `0957d8a3a4a0`  |
| 2834   | Layout 1             | `0957d8a3a4a0`  |
| 2825   | Layout 1             | `0957d8a3a4a0`  |
| 2819   | Layout 1             | `0957d8a3a4a0`  |
| 2811   | Layout 1             | `0957d8a3a4a0`  |
| 2803   | Layout 1             | `0957d8a3a4a0`  |
| 2794   | Layout 1             | `0957d8a3a4a0`  |
| 2783   | Layout 1             | `0957d8a3a4a0`  |
| 2774   | Layout 1             | `0957d8a3a4a0`  |
| 2765   | Layout 1             | `0957d8a3a4a0`  |
| 2756   | Layout 1             | `0957d8a3a4a0`  |
| 2750   | Layout 1             | `0957d8a3a4a0`  |
| 2743   | Layout 1             | `0957d8a3a4a0`  |
| 2736   | Layout 1             | `0957d8a3a4a0`  |
| 2726   | Layout 1             | `0957d8a3a4a0`  |
| 2717   | Layout 1             | `0957d8a3a4a0`  |
| 2709   | Layout 1             | `0957d8a3a4a0`  |
| 2703   | Layout 1             | `0957d8a3a4a0`  |
| 2695   | Layout 1             | `0957d8a3a4a0`  |
| 2684   | Layout 1             | `0957d8a3a4a0`  |
| 2672   | Layout 1             | `0957d8a3a4a0`  |
| 2665   | Layout 1             | `0957d8a3a4a0`  |
| 2657   | Layout 1             | `0957d8a3a4a0`  |
| 2649   | Layout 1             | `0957d8a3a4a0`  |
| 2644   | Layout 1             | `0957d8a3a4a0`  |
| 2637   | Layout 1             | `0957d8a3a4a0`  |
| 2629   | Layout 1             | `0957d8a3a4a0`  |
| 2619   | Layout 1             | `0957d8a3a4a0`  |
| 2612   | Layout 1             | `0957d8a3a4a0`  |
| 2606   | Layout 1             | `0957d8a3a4a0`  |
| 2602   | Layout 1             | `0957d8a3a4a0`  |
| 2601   | Layout 1             | `0957d8a3a4a0`  |
| 2592   | Layout 1             | `0957d8a3a4a0`  |
| 2583   | Layout 1             | `0957d8a3a4a0`  |
| 2575   | Layout 1             | `0957d8a3a4a0`  |
| 2567   | Layout 1             | `0957d8a3a4a0`  |
| 2560   | Layout 1             | `0957d8a3a4a0`  |
| 2553   | Layout 1             | `0957d8a3a4a0`  |
| 2545   | Layout 1             | `0957d8a3a4a0`  |
| 2538   | Layout 1             | `0957d8a3a4a0`  |
| 2529   | Layout 1             | `0957d8a3a4a0`  |
| 2519   | Layout 1             | `0957d8a3a4a0`  |
| 2513   | Layout 1             | `0957d8a3a4a0`  |
| 2510   | Layout 1             | `0957d8a3a4a0`  |
| 2507   | Layout 1             | `0957d8a3a4a0`  |
| 2503   | Layout 1             | `0957d8a3a4a0`  |
| 2498   | Layout 1             | `0957d8a3a4a0`  |
| 2492   | Layout 1             | `0957d8a3a4a0`  |
| 2487   | Layout 1             | `0957d8a3a4a0`  |
| 2480   | Layout 1             | `0957d8a3a4a0`  |
| 2474   | Layout 1             | `0957d8a3a4a0`  |
| 2468   | Layout 1             | `0957d8a3a4a0`  |
| 2460   | Layout 1             | `0957d8a3a4a0`  |
| 2453   | Layout 1             | `0957d8a3a4a0`  |
| 2444   | Layout 1             | `0957d8a3a4a0`  |
| 2438   | Layout 1             | `0957d8a3a4a0`  |
| 2434   | Layout 1             | `0957d8a3a4a0`  |
| 2429   | Layout 1             | `0957d8a3a4a0`  |
| 2421   | Layout 1             | `0957d8a3a4a0`  |
| 2414   | Layout 1             | `0957d8a3a4a0`  |
| 2407   | Layout 1             | `0957d8a3a4a0`  |
| 2401   | Layout 1             | `0957d8a3a4a0`  |
| 2397   | Layout 1             | `0957d8a3a4a0`  |
| 2393   | Layout 1             | `0957d8a3a4a0`  |
| 2384   | Layout 1             | `0957d8a3a4a0`  |
| 2378   | Layout 1             | `0957d8a3a4a0`  |
| 2372   | Layout 1             | `0957d8a3a4a0`  |
| 2358   | Layout 1             | `0957d8a3a4a0`  |
| 2352   | Layout 1             | `0957d8a3a4a0`  |
| 2347   | Layout 1             | `0957d8a3a4a0`  |
| 2343   | Layout 1             | `0957d8a3a4a0`  |
| 2335   | Layout 1             | `0957d8a3a4a0`  |
| 2327   | Layout 1             | `0957d8a3a4a0`  |
| 2324   | Layout 1             | `0957d8a3a4a0`  |
| 2319   | Layout 1             | `0957d8a3a4a0`  |
| 2313   | Layout 1             | `0957d8a3a4a0`  |
| 2308   | Layout 1             | `0957d8a3a4a0`  |
| 2302   | Layout 1             | `0957d8a3a4a0`  |
| 2295   | Layout 1             | `0957d8a3a4a0`  |
| 2290   | Layout 1             | `0957d8a3a4a0`  |
| 2284   | Layout 1             | `0957d8a3a4a0`  |
| 2276   | Layout 1             | `0957d8a3a4a0`  |
| 2269   | Layout 1             | `0957d8a3a4a0`  |
| 2259   | Layout 1             | `0957d8a3a4a0`  |
| 2250   | Layout 1             | `0957d8a3a4a0`  |
| 2243   | Layout 1             | `0957d8a3a4a0`  |
| 2235   | Layout 1             | `0957d8a3a4a0`  |
| 2229   | Layout 1             | `0957d8a3a4a0`  |
| 2224   | Layout 1             | `0957d8a3a4a0`  |
| 2218   | Layout 1             | `0957d8a3a4a0`  |
| 2215   | Layout 1             | `0957d8a3a4a0`  |
| 2207   | Layout 1             | `0957d8a3a4a0`  |
| 2203   | Layout 1             | `0957d8a3a4a0`  |
| 2196   | Layout 1             | `0957d8a3a4a0`  |
| 2192   | Layout 1             | `0957d8a3a4a0`  |
| 2189   | Layout 1             | `0957d8a3a4a0`  |
| 2183   | Layout 1             | `0957d8a3a4a0`  |
| 2179   | Layout 1             | `0957d8a3a4a0`  |
| 2171   | Layout 1             | `0957d8a3a4a0`  |
| 2163   | Layout 1             | `0957d8a3a4a0`  |
| 2156   | Layout 1             | `0957d8a3a4a0`  |
| 2151   | Layout 1             | `0957d8a3a4a0`  |
| 2147   | Layout 1             | `0957d8a3a4a0`  |
| 2142   | Layout 1             | `0957d8a3a4a0`  |
| 2138   | Layout 1             | `0957d8a3a4a0`  |
| 2134   | Layout 1             | `0957d8a3a4a0`  |
| 2130   | Layout 1             | `0957d8a3a4a0`  |
| 2122   | Layout 1             | `0957d8a3a4a0`  |
| 2107   | Layout 1             | `0957d8a3a4a0`  |
| 2098   | Layout 1             | `0957d8a3a4a0`  |
| 2089   | Layout 1             | `0957d8a3a4a0`  |
| 2081   | Layout 1             | `0957d8a3a4a0`  |
| 2073   | Layout 1             | `0957d8a3a4a0`  |
| 2067   | Layout 1             | `0957d8a3a4a0`  |
| 2063   | Layout 1             | `0957d8a3a4a0`  |
| 2059   | Layout 1             | `0957d8a3a4a0`  |
| 2052   | Layout 1             | `0957d8a3a4a0`  |
| 2044   | Layout 1             | `0957d8a3a4a0`  |
| 2039   | Layout 1             | `0957d8a3a4a0`  |
| 2032   | Layout 1             | `0957d8a3a4a0`  |
| 2025   | Layout 1             | `0957d8a3a4a0`  |
| 2011   | Layout 1             | `0957d8a3a4a0`  |
| 2005   | Layout 1             | `0957d8a3a4a0`  |
| 2000   | Layout 1             | `0957d8a3a4a0`  |
| 1996   | Layout 1             | `0957d8a3a4a0`  |
| 1991   | Layout 1             | `0957d8a3a4a0`  |
| 1985   | Layout 1             | `0957d8a3a4a0`  |
| 1980   | Layout 1             | `0957d8a3a4a0`  |
| 1969   | Layout 1             | `0957d8a3a4a0`  |
| 1964   | Layout 1             | `0957d8a3a4a0`  |
| 1958   | Layout 1             | `0957d8a3a4a0`  |
| 1950   | Layout 1             | `0957d8a3a4a0`  |
| 1945   | Layout 1             | `0957d8a3a4a0`  |
| 1937   | Layout 1             | `0957d8a3a4a0`  |
| 1933   | Layout 1             | `0957d8a3a4a0`  |
| 1927   | Layout 1             | `0957d8a3a4a0`  |
| 1921   | Layout 1             | `0957d8a3a4a0`  |
| 1914   | Layout 1             | `0957d8a3a4a0`  |
| 1908   | Layout 1             | `0957d8a3a4a0`  |
| 1897   | Layout 1             | `0957d8a3a4a0`  |
| 1892   | Layout 1             | `0957d8a3a4a0`  |
| 1886   | Layout 1             | `0957d8a3a4a0`  |
| 1881   | Layout 1             | `0957d8a3a4a0`  |
| 1871   | Layout 1             | `0957d8a3a4a0`  |
| 1866   | Layout 1             | `0957d8a3a4a0`  |
| 1862   | Layout 1             | `0957d8a3a4a0`  |
| 1854   | Layout 1             | `0957d8a3a4a0`  |
| 1846   | Layout 1             | `0957d8a3a4a0`  |
| 1838   | Layout 1             | `0957d8a3a4a0`  |
| 1832   | Layout 1             | `0957d8a3a4a0`  |
| 1826   | Layout 1             | `0957d8a3a4a0`  |
| 1822   | Layout 1             | `0957d8a3a4a0`  |
| 1818   | Layout 1             | `0957d8a3a4a0`  |
| 1804   | Layout 1             | `0957d8a3a4a0`  |
| 1794   | Layout 1             | `0957d8a3a4a0`  |
| 1790   | Layout 1             | `0957d8a3a4a0`  |
| 1784   | Layout 1             | `0957d8a3a4a0`  |
| 1774   | Layout 1             | `0957d8a3a4a0`  |
| 1771   | Layout 1             | `0957d8a3a4a0`  |
| 1762   | Layout 1             | `0957d8a3a4a0`  |
| 1759   | Layout 1             | `0957d8a3a4a0`  |
| 1754   | Layout 1             | `0957d8a3a4a0`  |
| 1749   | Layout 1             | `0957d8a3a4a0`  |
| 1743   | Layout 1             | `0957d8a3a4a0`  |
| 1737   | Layout 1             | `0957d8a3a4a0`  |
| 1731   | Layout 1             | `0957d8a3a4a0`  |
| 1725   | Layout 1             | `0957d8a3a4a0`  |
| 1717   | Layout 1             | `0957d8a3a4a0`  |
| 1710   | Layout 1             | `0957d8a3a4a0`  |
| 1704   | Layout 1             | `0957d8a3a4a0`  |
| 1698   | Layout 1             | `0957d8a3a4a0`  |
| 1690   | Layout 1             | `0957d8a3a4a0`  |
| 1685   | Layout 1             | `0957d8a3a4a0`  |
| 1680   | Layout 1             | `0957d8a3a4a0`  |
| 1674   | Layout 1             | `0957d8a3a4a0`  |
| 1668   | Layout 1             | `0957d8a3a4a0`  |
| 1659   | Layout 1             | `0957d8a3a4a0`  |
| 1649   | Layout 1             | `0957d8a3a4a0`  |
| 1642   | Layout 1             | `0957d8a3a4a0`  |
| 1636   | Layout 1             | `0957d8a3a4a0`  |
| 1628   | Layout 1             | `0957d8a3a4a0`  |
| 1622   | Layout 1             | `0957d8a3a4a0`  |
| 1614   | Layout 1             | `0957d8a3a4a0`  |
| 1608   | Layout 1             | `0957d8a3a4a0`  |
| 1602   | Layout 1             | `0957d8a3a4a0`  |
| 1598   | Layout 1             | `0957d8a3a4a0`  |
| 1594   | Layout 1             | `0957d8a3a4a0`  |
| 1590   | Layout 1             | `0957d8a3a4a0`  |
| 1587   | Layout 1             | `0957d8a3a4a0`  |
| 1584   | Layout 1             | `0957d8a3a4a0`  |
| 1579   | Layout 1             | `0957d8a3a4a0`  |
| 1572   | Layout 1             | `0957d8a3a4a0`  |
| 1565   | Layout 1             | `0957d8a3a4a0`  |
| 1559   | Layout 1             | `0957d8a3a4a0`  |
| 1554   | Layout 1             | `0957d8a3a4a0`  |
| 1547   | Layout 1             | `0957d8a3a4a0`  |
| 1537   | Layout 1             | `0957d8a3a4a0`  |
| 1529   | Layout 1             | `0957d8a3a4a0`  |
| 1524   | Layout 1             | `0957d8a3a4a0`  |
| 1519   | Layout 1             | `0957d8a3a4a0`  |
| 1509   | Layout 1             | `0957d8a3a4a0`  |
| 1506   | Layout 1             | `0957d8a3a4a0`  |
| 1504   | Layout 1             | `0957d8a3a4a0`  |
| 1500   | Layout 1             | `0957d8a3a4a0`  |
| 1493   | Layout 1             | `0957d8a3a4a0`  |
| 1489   | Layout 1             | `0957d8a3a4a0`  |
| 1485   | Layout 1             | `0957d8a3a4a0`  |
| 1481   | Layout 1             | `0957d8a3a4a0`  |
| 1474   | Layout 1             | `0957d8a3a4a0`  |
| 1466   | Layout 1             | `0957d8a3a4a0`  |
| 1462   | Layout 1             | `0957d8a3a4a0`  |
| 1459   | Layout 1             | `0957d8a3a4a0`  |
| 1453   | Layout 1             | `0957d8a3a4a0`  |
| 1450   | Layout 1             | `0957d8a3a4a0`  |
| 1445   | Layout 1             | `0957d8a3a4a0`  |
| 1439   | Layout 1             | `0957d8a3a4a0`  |
| 1433   | Layout 1             | `0957d8a3a4a0`  |
| 1430   | Layout 1             | `0957d8a3a4a0`  |
| 1426   | Layout 1             | `0957d8a3a4a0`  |
| 1421   | Layout 1             | `0957d8a3a4a0`  |
| 1417   | Layout 1             | `0957d8a3a4a0`  |
| 1416   | Layout 1             | `0957d8a3a4a0`  |
| 1409   | Layout 1             | `0957d8a3a4a0`  |
| 1405   | Layout 1             | `0957d8a3a4a0`  |
| 1401   | Layout 1             | `0957d8a3a4a0`  |
| 1396   | Layout 1             | `0957d8a3a4a0`  |
| 1391   | Layout 1             | `0957d8a3a4a0`  |
| 1390   | Layout 1             | `0957d8a3a4a0`  |
| 1386   | Layout 1             | `0957d8a3a4a0`  |
| 1381   | Layout 1             | `0957d8a3a4a0`  |
| 1379   | Layout 1             | `0957d8a3a4a0`  |
| 1372   | Layout 1             | `0957d8a3a4a0`  |
| 1366   | Layout 1             | `0957d8a3a4a0`  |
| 1364   | Layout 1             | `0957d8a3a4a0`  |
| 1363   | Layout 1             | `0957d8a3a4a0`  |
| 1360   | Layout 1             | `0957d8a3a4a0`  |
| 1358   | Layout 1             | `0957d8a3a4a0`  |
| 1355   | Layout 1             | `0957d8a3a4a0`  |
| 1351   | Layout 1             | `0957d8a3a4a0`  |
| 1348   | Layout 1             | `0957d8a3a4a0`  |
| 1346   | Layout 1             | `0957d8a3a4a0`  |
| 1341   | Layout 1             | `0957d8a3a4a0`  |
| 1340   | Layout 1             | `0957d8a3a4a0`  |
| 1338   | Layout 1             | `0957d8a3a4a0`  |
| 1335   | Layout 1             | `0957d8a3a4a0`  |
| 1333   | Layout 1             | `0957d8a3a4a0`  |
| 1329   | Layout 1             | `0957d8a3a4a0`  |
| 1327   | Layout 1             | `0957d8a3a4a0`  |
| 1324   | Layout 1             | `0957d8a3a4a0`  |
| 1321   | Layout 1             | `0957d8a3a4a0`  |
| 1319   | Layout 1             | `0957d8a3a4a0`  |
| 1318   | Layout 1             | `0957d8a3a4a0`  |
| 1316   | Layout 1             | `0957d8a3a4a0`  |
| 1313   | Layout 1             | `0957d8a3a4a0`  |
| 1311   | Layout 1             | `0957d8a3a4a0`  |
| 1309   | Layout 1             | `0957d8a3a4a0`  |
| 1304   | Layout 1             | `0957d8a3a4a0`  |
| 1292   | Layout 1             | `0957d8a3a4a0`  |
| 1286   | Layout 1             | `0957d8a3a4a0`  |
| 1280   | Layout 1             | `0957d8a3a4a0`  |
| 1276   | No documented layout | `0957d8a3a4a0`  |
| 1267   | No documented layout | `0957d8a3a4a0`  |
| 1261   | No documented layout | `0957d8a3a4a0`  |
| 1256   | No documented layout | `0957d8a3a4a0`  |
| 1250   | No documented layout | `0957d8a3a4a0`  |
| 1246   | No documented layout | `0957d8a3a4a0`  |
| 1239   | No documented layout | `0957d8a3a4a0`  |
| 1230   | No documented layout | `0957d8a3a4a0`  |
| 1226   | No documented layout | `0957d8a3a4a0`  |
| 1220   | No documented layout | `0957d8a3a4a0`  |
| 1217   | No documented layout | `0957d8a3a4a0`  |
| 1211   | No documented layout | `0957d8a3a4a0`  |
| 1210   | No documented layout | `0957d8a3a4a0`  |
| 1208   | No documented layout | `0957d8a3a4a0`  |
| 1203   | No documented layout | `0957d8a3a4a0`  |
| 1197   | No documented layout | `0957d8a3a4a0`  |
| 1194   | No documented layout | `0957d8a3a4a0`  |
| 1192   | No documented layout | `0957d8a3a4a0`  |
| 1187   | No documented layout | `0957d8a3a4a0`  |
| 1183   | No documented layout | `0957d8a3a4a0`  |
| 1177   | No documented layout | `0957d8a3a4a0`  |
| 1173   | No documented layout | `0957d8a3a4a0`  |
| 1167   | No documented layout | `0957d8a3a4a0`  |
| 1164   | No documented layout | `0957d8a3a4a0`  |
| 1156   | No documented layout | `0957d8a3a4a0`  |
| 1149   | No documented layout | `0957d8a3a4a0`  |
| 1144   | No documented layout | `0957d8a3a4a0`  |
| 1137   | No documented layout | `0957d8a3a4a0`  |
| 1132   | No documented layout | `0957d8a3a4a0`  |
| 1127   | No documented layout | `0957d8a3a4a0`  |
| 1122   | No documented layout | `0957d8a3a4a0`  |
| 1118   | No documented layout | `0957d8a3a4a0`  |
| 1114   | No documented layout | `0957d8a3a4a0`  |
| 1109   | No documented layout | `0957d8a3a4a0`  |
| 1102   | No file              | `0957d8a3a4a0`  |
| 1096   | No file              | `0957d8a3a4a0`  |
| 1088   | No file              | `0957d8a3a4a0`  |
| 1081   | No file              | `0957d8a3a4a0`  |
| 1076   | No file              | `0957d8a3a4a0`  |
| 1069   | No file              | `0957d8a3a4a0`  |
| 1064   | No file              | `0957d8a3a4a0`  |
| 1058   | No file              | `0957d8a3a4a0`  |
| 1051   | No file              | `0957d8a3a4a0`  |
| 1044   | No file              | `0957d8a3a4a0`  |
| 1036   | No file              | `0957d8a3a4a0`  |
| 1026   | No file              | `0957d8a3a4a0`  |
| 1016   | No file              | `0957d8a3a4a0`  |
| 1009   | No file              | `0957d8a3a4a0`  |
| 1005   | No file              | `0957d8a3a4a0`  |
| 1000   | No file              | `0957d8a3a4a0`  |
| 998    | No file              | `0957d8a3a4a0`  |
| 990    | No file              | `0957d8a3a4a0`  |
| 979    | No file              | `0957d8a3a4a0`  |
| 972    | No file              | `0957d8a3a4a0`  |
| 963    | No file              | `0957d8a3a4a0`  |
| 955    | No file              | `0957d8a3a4a0`  |
| 946    | No file              | `0957d8a3a4a0`  |
| 938    | No file              | `0957d8a3a4a0`  |
| 927    | No file              | `0957d8a3a4a0`  |
| 911    | No file              | `0957d8a3a4a0`  |
| 904    | No file              | `0957d8a3a4a0`  |
| 899    | No file              | `0957d8a3a4a0`  |
| 894    | No file              | `0957d8a3a4a0`  |
| 885    | No file              | `0957d8a3a4a0`  |
| 879    | No file              | `0957d8a3a4a0`  |
| 872    | No file              | `0957d8a3a4a0`  |
| 864    | No file              | `0957d8a3a4a0`  |
| 855    | No file              | `0957d8a3a4a0`  |
| 853    | No file              | `0957d8a3a4a0`  |
| 845    | No file              | `0957d8a3a4a0`  |
| 837    | No file              | `0957d8a3a4a0`  |
| 829    | No documented layout | `0957d8a3a4a0`  |
| 822    | No documented layout | `0957d8a3a4a0`  |
| 814    | No documented layout | `0957d8a3a4a0`  |
| 805    | No documented layout | `0957d8a3a4a0`  |
| 794    | No documented layout | `0957d8a3a4a0`  |
| 787    | No documented layout | `0957d8a3a4a0`  |
| 780    | No documented layout | `0957d8a3a4a0`  |
| 771    | No documented layout | `0957d8a3a4a0`  |
| 760    | No documented layout | `0957d8a3a4a0`  |
| 748    | No documented layout | `0957d8a3a4a0`  |
| 741    | No documented layout | `0957d8a3a4a0`  |
| 736    | No documented layout | `0957d8a3a4a0`  |
| 731    | No documented layout | `0957d8a3a4a0`  |
| 723    | No documented layout | `0957d8a3a4a0`  |
| 711    | No documented layout | `0957d8a3a4a0`  |
| 707    | No documented layout | `0957d8a3a4a0`  |
| 697    | No documented layout | `0957d8a3a4a0`  |
| 689    | No documented layout | `0957d8a3a4a0`  |
| 683    | No documented layout | `0957d8a3a4a0`  |
| 678    | No documented layout | `0957d8a3a4a0`  |
| 670    | No documented layout | `0957d8a3a4a0`  |
| 661    | No documented layout | `0957d8a3a4a0`  |
| 656    | No documented layout | `0957d8a3a4a0`  |
| 652    | No documented layout | `0957d8a3a4a0`  |
| 643    | No documented layout | `0957d8a3a4a0`  |
| 637    | No documented layout | `0957d8a3a4a0`  |
| 630    | No documented layout | `0957d8a3a4a0`  |
| 627    | No documented layout | `0957d8a3a4a0`  |
| 621    | No documented layout | `0957d8a3a4a0`  |
| 617    | No documented layout | `0957d8a3a4a0`  |
| 615    | No documented layout | `0957d8a3a4a0`  |
| 606    | No documented layout | `0957d8a3a4a0`  |
| 599    | No documented layout | `0957d8a3a4a0`  |
| 592    | No documented layout | `0957d8a3a4a0`  |
| 586    | No documented layout | `0957d8a3a4a0`  |
| 577    | No documented layout | `0957d8a3a4a0`  |
| 569    | No documented layout | `0957d8a3a4a0`  |
| 561    | No documented layout | `0957d8a3a4a0`  |
| 554    | No documented layout | `0957d8a3a4a0`  |
| 542    | No documented layout | `0957d8a3a4a0`  |
| 532    | No documented layout | `0957d8a3a4a0`  |
| 531    | No documented layout | `0957d8a3a4a0`  |
| 526    | No documented layout | `0957d8a3a4a0`  |
| 521    | No documented layout | `0957d8a3a4a0`  |
| 517    | No documented layout | `0957d8a3a4a0`  |
| 510    | No documented layout | `0957d8a3a4a0`  |
| 508    | No documented layout | `0957d8a3a4a0`  |
| 504    | No documented layout | `0957d8a3a4a0`  |
| 497    | No documented layout | `0957d8a3a4a0`  |
| 491    | No documented layout | `0957d8a3a4a0`  |
| 485    | No documented layout | `0957d8a3a4a0`  |
| 478    | No documented layout | `0957d8a3a4a0`  |
| 472    | No documented layout | `0957d8a3a4a0`  |
| 466    | No documented layout | `0957d8a3a4a0`  |
| 457    | No documented layout | `0957d8a3a4a0`  |
| 452    | No documented layout | `0957d8a3a4a0`  |
| 449    | No documented layout | `0957d8a3a4a0`  |
| 435    | No documented layout | `0957d8a3a4a0`  |

<!-- versions:end -->

## Companion Files

No companion file is required to parse the file. Names and descriptions are stored inline as UTF-16LE Korean fallback strings. For user-facing display, `languagedata_en.loc` is optional and should be preferred when a matching LOC type `22` row exists.

| File                  | Required | Role                                                |
| --------------------- | -------- | --------------------------------------------------- |
| `languagedata_en.loc` | Optional | Provides localized skill names and descriptions via LOC type `22` |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type                             | Field              | Notes                                                   |
| ------------------- | -------------------------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]                          | magic              | `PABR` (ASCII)                                          |
| `+0x04`             | u32                              | skill_record_count | Number of skill records; observed `72` (also in the 2026-09-27 client) |
| `+0x08`             | Skill Record[skill_record_count] | skill_records      | Usually `0x38` bytes each; one observed extended record |
| `skill_records+0x00` | String Table                    | string_table       | Length-prefixed UTF-16LE strings                        |
| `string_table+0x00` | u32                              | string_table_start | Absolute file offset of `string_count`; observed `0xFD8` |
| `string_table+0x04` | u32                              | zero               | Observed `0`                                            |

The fixed/extended skill-record block begins at `0x08` and the string table starts at `0xFD8` in the observed file. Skill records reference string table entries by zero-based index.

### Skill Record (variable: 56 bytes + extension)

| Offset  | Type                         | Field              | Notes                                                   |
| ------- | ---------------------------- | ------------------ | ------------------------------------------------------- |
| `+0x00` | u16                          | skill_id           | Passive worker skill ID                                 |
| `+0x02` | u16                          | duplicate_skill_id | Always matches `skill_id` in observed records           |
| `+0x04` | u32                          | name_index         | Index into `string_table`; Korean skill name            |
| `+0x08` | u32                          | icon_index         | Index into `string_table`; DDS path                     |
| `+0x0C` | u32                          | description_index  | Index into `string_table`; Korean effect description    |
| `+0x10` | u32                          | acquisition_weight | Observed values: `1000`, `1050`, `1400`, `2100`, `2500`, `2800` |
| `+0x14` | u32                          | unknown_14         | Always observed as `0`                                  |
| `+0x18` | u32                          | effect_type        | `0` flat stats, `1` full refund, `2` stats per level up, `6` extra work; see Effect Types |
| `+0x1C` | u32                          | apply_mode         | Usually `7`; observed `0` for `skill_id=1012`           |
| `+0x20` | u32                          | apply_scope        | Always observed as `7`                                  |
| `+0x24` | u32                          | effect_type_copy   | Mirrors `effect_type` in many rows                      |
| `+0x28` | u32                          | effect_target      | Stat/category/chance target, depending on `effect_type` |
| `+0x2C` | u32                          | effect_value_a     | Primary scaled effect value                             |
| `+0x30` | u32                          | effect_value_b     | Secondary scaled effect value for some rows             |
| `+0x34` | u32                          | unknown_34         | Always observed as `0`                                  |
| `+0x38` | Extension if skill_id = 1012 | extension          | Only on `skill_id=1012`; the rule is open, see [Extended `1012` Record](#extended-1012-record) |

### Extension (16 bytes)

One observed record, `skill_id=1012` (`타고난 일꾼`), is followed by an extra 16-byte parameter block before the next record. The parser reads it on `skill_id=1012` when the bytes left before the string table hold it. The field names keep their offsets in the record, so `unknown_38` sits at `+0x00` here. Earlier versions of this doc called `unknown_3c` `extra_effect_value_a` and `unknown_40` `extra_effect_value_b`.

| Offset  | Type | Field      | Notes              |
| ------- | ---- | ---------- | ------------------ |
| `+0x00` | u32  | unknown_38 | Observed `0`       |
| `+0x04` | u32  | unknown_3c | Observed `2000000` |
| `+0x08` | u32  | unknown_40 | Observed `1`       |
| `+0x0C` | u32  | unknown_44 | Observed `0`       |

### String Table (variable: 4 bytes + strings)

The string table is a flat pool, not grouped records. Skill records choose any string indices; several records reuse icon/name/description entries. Each entry is a `pstr`: the `is_wide` byte (earlier versions of this doc called it `present`) is always observed as `1`, then the UTF-16LE byte length with no alignment, then the UTF-16LE text.

| Offset  | Type               | Field        | Notes                                    |
| ------- | ------------------ | ------------ | ---------------------------------------- |
| `+0x00` | u32                | string_count | Number of string entries; observed `174` |
| `+0x04` | pstr[string_count] | strings      | Repeated `string_count` times            |

Derived fields:

```text
inline_name = string_table[name_index]
icon_path = string_table[icon_index]
inline_description = string_table[description_index]
display_name = LOC type 22, str_id1=skill_id, str_id4=0; fallback inline_name
display_description = LOC type 22, str_id1=skill_id, str_id4=1; fallback inline_description
```

## Effect Types

The 2016 client (build of 2016-01-11) ships with debug symbols. Its
`gc::PlantWorkerPassiveSkillBuff::PassiveBuffType` numbers the effect types
`0` WorkEfficience, `1` ReturnItem, `2` LevelStatAdditional, `3`
AddActionPoint, `4` WorkEfficiencePercent, `5` WorkEfficienceStatic and `6`
RepeatWorking, which fit the four types this file uses. Each type has its own
`ApplyTypeIndex` enum that names its parameters in the order `effect_target`,
`effect_value_a`, `effect_value_b`:

| `effect_type` | `effect_target` | `effect_value_a` | `effect_value_b` |
| ------------- | --------------- | ---------------- | ---------------- |
| `0` WorkEfficience | WorkingType | ApplyValue | ApplyTargetType (`0` MoveSpeed, `1` WorkEfficience, `2` Luck) |
| `1` ReturnItem | ReturnPercents | ReturnCountPercentsMin | ReturnCountPercentsMax |
| `2` LevelStatAdditional | AdditionalType (`0` MoveSpeed, `1` WorkEfficience, `2` Luck) | AdditionalValue | |
| `6` RepeatWorking | WorkingGroup | ApplyValue | |

### `effect_type = 0` - Flat Stats

Direct stat and work-speed effects. `effect_target` is `0` for generic stat modifiers such as movement speed, work speed, and luck. For named work-speed knowledge skills, `effect_target` identifies the work category.

The work category is a `CppEnums.ApplyWorkingType` value
(`global_define_cpp_enum.luac`, the same members as the 2016 enum), and each
member fits the skills that store it.

| Effect Target | `ApplyWorkingType` | Meaning | Example Skill |
| ------------- | ------------------ | ------- | ------------- |
| `0` | All | Generic stat modifier | `1603` [Wings C](https://bdocodex.com/us/sskill/1603/), `1103` [Simple C](https://bdocodex.com/us/sskill/1103/), `1503` [Lucky Guy C](https://bdocodex.com/us/sskill/1503/) |
| `1` | Cutting | Jeweler work speed | `1001` [Polishing Knowledge](https://bdocodex.com/us/sskill/1001/) |
| `2` | LargeCraft | Mass production work speed | `1002` [Mass Production Knowledge](https://bdocodex.com/us/sskill/1002/) |
| `3` | WorkShop | Weapon/armor workshop speed | `1003` [Workshop Knowledge](https://bdocodex.com/us/sskill/1003/) |
| `4` | Tools | Tool workshop speed | `1004` [Tool Knowledge](https://bdocodex.com/us/sskill/1004/) |
| `5` | Furniture | Furniture workshop speed | `1005` [Furniture Knowledge](https://bdocodex.com/us/sskill/1005/) |
| `7` | Wardrobe | Costume workshop speed | `1007` [Costume Knowledge](https://bdocodex.com/us/sskill/1007/) |
| `8` | Normal | Refinery/specialty work speed | `1008` [General Knowledge](https://bdocodex.com/us/sskill/1008/) |
| `9` | SiegeWeapons | Cannon/siege weapon work speed | `1009` [Siege Knowledge](https://bdocodex.com/us/sskill/1009/) |
| `10` | WagonParts | Ship/wagon/horse gear work speed | `1010` [Mount Knowledge](https://bdocodex.com/us/sskill/1010/) |
| `11` | Zone | Node/farm work speed | `1011` [Farm Knowledge](https://bdocodex.com/us/sskill/1011/) |
| `13` | Monopoly | Specialty node work speed | `1013` [Specialty Node Knowledge](https://bdocodex.com/us/sskill/1013/) |

Observed scaling:

| Description Pattern | Value Field | Scaling |
| ------------------- | ----------- | ------- |
| Movement Speed +N% | `effect_value_a` | `N * 10000` |
| Work Speed +N | `effect_value_a` | `N * 1000000` |
| Luck +N | `effect_value_a` | `N * 10000` |

`effect_value_b` selects the stat for every `effect_type = 0` record: `0` movement speed, `1` work speed, `2` luck (the same codes `effect_type = 2` uses in `effect_target`). The named work-speed skills (targets `1` to `13`) all store `1`. This holds for every record and matches every English description in the 2026-09-27 client.

`skill_id=1012` combines two generic direct effects: the base record stores Movement Speed +7%, and the extra parameter block stores Work Speed +2.

### `effect_type = 1` - Full Refund

Material refund effects. `effect_target` is the chance scaled by `1,000,000`. `effect_value_a` is the share of the material refunded, on the same scale (`1000000` is a full refund). `effect_value_b` equals `effect_value_a` on every refund record in both clients (`100000` before the 2026-09-27 update, when the text read "10% of 1 Crafting Material", `1000000` after), so it is shown on the same scale. The 2016 names (ReturnCountPercentsMin and ReturnCountPercentsMax) read them as the low and high end of the refunded share, which are equal on every record.

| Example Skill | Effect Target | Meaning | Effect Values |
| ------------- | ------------- | ------- | ------------- |
| `1203` [Thrifty C](https://bdocodex.com/us/sskill/1203/) | `50000` | 5% chance | `100000`, `100000` |
| `1202` [Thrifty B](https://bdocodex.com/us/sskill/1202/) | `70000` | 7% chance | `100000`, `100000` |
| `1201` [Thrifty A](https://bdocodex.com/us/sskill/1201/) | `100000` | 10% chance | `100000`, `100000` |
| `2003` [Unexpected Luck C](https://bdocodex.com/us/sskill/2003/) | `1000` | Extremely low chance | `1000000`, `1000000` |
| `2002` [Unexpected Luck B](https://bdocodex.com/us/sskill/2002/) | `3000` | Very low chance | `1000000`, `1000000` |
| `2001` [Unexpected Luck A](https://bdocodex.com/us/sskill/2001/) | `5000` | Low chance | `1000000`, `1000000` |

### `effect_type = 2` - Stats per Level Up

Per-level stat growth effects. `effect_target` identifies the stat that grows on worker level-up.

| Effect Target | Meaning | Example Skill | Effect Value |
| ------------- | ------- | ------------- | ------------ |
| `0` | Movement speed | `1901` [Leg Work](https://bdocodex.com/us/sskill/1901/) | `5000` = Movement Speed +0.5% per level |
| `1` | Work speed | `1902` [Craftsmanship](https://bdocodex.com/us/sskill/1902/) | `200000` = Work Speed +0.2 per level |
| `2` | Luck | `1903` [Blessed Hand](https://bdocodex.com/us/sskill/1903/) | `2000` = Luck +0.2 per level |

### `effect_type = 6` - Extra Work

Extra-work effects. `effect_target` identifies the production category and `effect_value_a` is the extra work count.

| Effect Target | Meaning | Example Skill |
| ------------- | ------- | ------------- |
| `5001` | Weapon production | `1916` [Weapon Production](https://bdocodex.com/us/sskill/1916/) |
| `5002` | Armor production | `1917` [Armor Production](https://bdocodex.com/us/sskill/1917/) |
| `5003` | Life clothes production | `1918` [Life Clothes Production](https://bdocodex.com/us/sskill/1918/) |
| `5004` | Siege weapon production | `1922` [Siege Weapon Production](https://bdocodex.com/us/sskill/1922/) |
| `9001` | Produce packing | `1904` [Produce Packing](https://bdocodex.com/us/sskill/1904/) |
| `9002` | Herb packing | `1905` [Herb Packing](https://bdocodex.com/us/sskill/1905/) |
| `9003` | Mushroom packing | `1906` [Mushroom Packing](https://bdocodex.com/us/sskill/1906/) |
| `9004` | Fish packing | `1907` [Fish Packing](https://bdocodex.com/us/sskill/1907/) |
| `9005` | Timber packing | `1908` [Timber Packing](https://bdocodex.com/us/sskill/1908/) |
| `9006` | Ore packing | `1909` [Ore Packing](https://bdocodex.com/us/sskill/1909/) |

## Reference Rows

| Skill ID | Name | Icon | Description | Weight | Effect Values |
| -------- | ---- | ---- | ----------- | ------ | ------------- |
| `1603` | [Wings C](https://bdocodex.com/us/sskill/1603/) | `1303.dds` | Movement Speed +6% | `1000` | `60000`, `0` |
| `1602` | [Wings B](https://bdocodex.com/us/sskill/1602/) | `1302.dds` | Movement Speed +8% | `1050` | `80000`, `0` |
| `1601` | [Wings A](https://bdocodex.com/us/sskill/1601/) | `1301.dds` | Movement Speed +11% | `1400` | `110000`, `0` |
| `1923` | [Adv. Siege Weapon Production](https://bdocodex.com/us/sskill/1923/) | `1923.dds` | Extra Work (+3) Done for Siege Weapons | `2500` | `3`, `0` |
| `1203` | [Thrifty C](https://bdocodex.com/us/sskill/1203/) | `1203.dds` | 5% Chance to Return 10% of 1 Crafting Material | `1000` | `100000`, `100000` |
| `1012` | [Adept Worker](https://bdocodex.com/us/sskill/1012/) | `1012_N.dds` | Work Speed +2, Movement Speed +7% | `1050` | `70000`, `0`; extra `2000000`, `1` |

## Notes

- Observed file size is `13,090` bytes (2026-09-27 client: `13,294`).
- The 2026-09-27 client retunes the Thrifty skills: `effect_target` `50000`/`70000`/`100000` became `7000`/`10000`/`15000` for C/B/A, both effect values `100000` became `1000000`, and Thrifty C now reads "0.7% Chance to Fully Refund One Material, Selected with Equal Probability". The tables above show the pre-2026-09-27 values.
- BDO Codex lists every worker skill with Level `Naive` and Class `Warrior`. These look like the defaults for zero values (class `0` is Warrior), not data: no field in this record varies that way, and `unknown_14` / `unknown_34` are `0` on every skill.
- `acquisition_weight` is most likely the weight for rolling the skill when a worker learns one; the game does not show it, so it cannot be checked in game.
- The string table starts at `0xFD8`; the EOF trailer repeats this offset as `string_table_start`.
- The string table contains `174` entries: names, icon paths, and descriptions in one shared pool.
- Icon paths are UTF-16LE strings under `/New_UI_Common_forLua/Skill/WorkerSkill/`.
- Several records reuse string entries. For example, `1302` reuses the `1302.dds` icon entry from `1602`.
- LOC type `22` appears to carry worker skill localization. Use `str_id1=skill_id`, with `str_id4=0` for name and `str_id4=1` for description, when localized rows are available.

## Open Questions

### Extended `1012` Record

`skill_id=1012` has an extra 16-byte parameter block before the next record. The extra values encode its Work Speed +2 effect, but the general rule that determines when this extension appears is not confirmed.

### `effect_target` Is Not Fully Confirmed

`effect_target` means something different per `effect_type`, and not every reading is equally backed (2026-09-27 client):

| Reading | Evidence | Status |
| ------- | -------- | ------ |
| Refund chance (`effect_type = 1`) | All 6 refund skills match their text (`7000` is "0.7% Chance"), and the 2026-09-27 update changed value and text together (`50000`/`70000`/`100000` read 5/7/10% before, `7000`/`10000`/`15000` read 0.7/1/1.5% after) | Confirmed |
| Stat code (`effect_type = 2`) | `0`/`1`/`2` match the stat named in all 4 descriptions, with the same codes `effect_value_b` uses for `effect_type = 0` | Confirmed |
| Category key (`effect_type = 0` targets `1` to `13`) | The 2016 client names the slot WorkingType, and `CppEnums.ApplyWorkingType` names every stored value with a member that fits its skills (`1` Cutting on Polishing Knowledge, `13` Monopoly on Specialty Node Knowledge) | Confirmed |
| Category key (`effect_type = 6`) | The 2016 client names the slot WorkingGroup. Each value goes with exactly one category wording across its skills, and workermanjs applies the skills by the same categories (see In-Game Checks) | Very likely |
| Category names (`effect_type = 6`) | Taken from the descriptions; no client table names the `5001` to `9006` keys | Not confirmed |

## In-Game Checks

### Farm Knowledge Counts on Nodes Only

Needs worker: one with [Farm Knowledge](https://bdocodex.com/us/sskill/1011/) (`1011`, "Node Work Speed +5")

Whether the client reads `effect_target` to decide which work gets the bonus is not proven from the client files. [workermanjs](https://github.com/shrddr/workermanjs), a worker planner whose model is checked against observed yields, applies the skills with the same split (`src/stores/game.js`, `wspdBonus`, 2026-09-26): general work speed (target `0`) counts everywhere; target `11` (its `wspd_farm`, the skill now worded "Node Work Speed") counts on every node and in no workshop; a workshop adds only the skill of its own industry (`wspd_jewelry`, `wspd_weap` and so on, one per target `1` to `5`, `7` to `10` and `13`); and target `8` (`wspd_refine`, "Refinery/Specialty") also counts in the six packing workshops, which match the `effect_type = 6` targets `9001` to `9006` by name. Its hand-written skill list puts every skill ID in the same category as its `effect_target` here.

Put the worker on a node, then in a workshop of any industry, and compare the work time per cycle with the worker's base work speed. If the time matches work speed + 5 on the node and the base work speed in the workshop, the client applies the bonus by `effect_target` (`11`, node work) as read here. A +5 in the workshop too means the target does not limit it.
