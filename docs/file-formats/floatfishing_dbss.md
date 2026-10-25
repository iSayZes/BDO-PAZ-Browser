# `floatfishing.dbss` Format

## Purpose

The fish drop groups of the fishing points that float on open water (the
`Fishing Point` and `Clearwater Fishing Point` characters that
[`floatfishingpoint.dbss`](floatfishingpoint_dbss.md) spawns). Each row is
one fishing group: five drop slots (treasure, rare, large, general, junk),
each an item drop group and its chance. Companion `floatfishingoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------------------------- | ------ | -------------- | --------- |
| 2      | 2726 and later | `floatfishing.dbss`       | 29,264 | 418 Row        | 70        |
| 2      | 2726 and later | `floatfishingoffset.dbss` | 4,184  | 418 Offset Row | 10        |
| 1      | 1267 to 2717   | `floatfishing.dbss`       | 25,084 | 418 Row        | 60        |
| 1      | 1267 to 2717   | `floatfishingoffset.dbss` | 4,184  | 418 Offset Row | 10        |

| Layout | File                      | Known            | Unknown          |
| ------ | ------------------------- | ---------------- | ---------------- |
| 2      | `floatfishing.dbss`       | 17,560 B (60.0%) | 11,704 B (40.0%) |
| 2      | `floatfishingoffset.dbss` | 4,184 B (100.0%) | 0 B (0.0%)       |
| 1      | `floatfishing.dbss`       | 13,380 B (53.3%) | 11,704 B (46.7%) |
| 1      | `floatfishingoffset.dbss` | 4,184 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `c3a2e9a87917`  |
| 3482   | Layout 2 | `c3a2e9a87917`  |
| 3474   | Layout 2 | `c3a2e9a87917`  |
| 3473   | Layout 2 | `c3a2e9a87917`  |
| 3464   | Layout 2 | `c3a2e9a87917`  |
| 3458   | Layout 2 | `c3a2e9a87917`  |
| 3454   | Layout 2 | `c3a2e9a87917`  |
| 3444   | Layout 2 | `c3a2e9a87917`  |
| 3435   | Layout 2 | `c3a2e9a87917`  |
| 3426   | Layout 2 | `c3a2e9a87917`  |
| 3418   | Layout 2 | `c3a2e9a87917`  |
| 3412   | Layout 2 | `c3a2e9a87917`  |
| 3402   | Layout 2 | `c3a2e9a87917`  |
| 3396   | Layout 2 | `c3a2e9a87917`  |
| 3387   | Layout 2 | `c3a2e9a87917`  |
| 3381   | Layout 2 | `c3a2e9a87917`  |
| 3373   | Layout 2 | `c3a2e9a87917`  |
| 3364   | Layout 2 | `c3a2e9a87917`  |
| 3356   | Layout 2 | `c3a2e9a87917`  |
| 3349   | Layout 2 | `c3a2e9a87917`  |
| 3342   | Layout 2 | `c3a2e9a87917`  |
| 3335   | Layout 2 | `c3a2e9a87917`  |
| 3326   | Layout 2 | `c3a2e9a87917`  |
| 3321   | Layout 2 | `c3a2e9a87917`  |
| 3314   | Layout 2 | `c3a2e9a87917`  |
| 3303   | Layout 2 | `c3a2e9a87917`  |
| 3302   | Layout 2 | `c3a2e9a87917`  |
| 3293   | Layout 2 | `c3a2e9a87917`  |
| 3283   | Layout 2 | `c3a2e9a87917`  |
| 3275   | Layout 2 | `c3a2e9a87917`  |
| 3267   | Layout 2 | `c3a2e9a87917`  |
| 3258   | Layout 2 | `c3a2e9a87917`  |
| 3251   | Layout 2 | `c3a2e9a87917`  |
| 3242   | Layout 2 | `c3a2e9a87917`  |
| 3235   | Layout 2 | `c3a2e9a87917`  |
| 3229   | Layout 2 | `c3a2e9a87917`  |
| 3212   | Layout 2 | `c3a2e9a87917`  |
| 3203   | Layout 2 | `c3a2e9a87917`  |
| 3193   | Layout 2 | `c3a2e9a87917`  |
| 3186   | Layout 2 | `c3a2e9a87917`  |
| 3177   | Layout 2 | `c3a2e9a87917`  |
| 3169   | Layout 2 | `c3a2e9a87917`  |
| 3158   | Layout 2 | `c3a2e9a87917`  |
| 3151   | Layout 2 | `c3a2e9a87917`  |
| 3144   | Layout 2 | `c3a2e9a87917`  |
| 3133   | Layout 2 | `c3a2e9a87917`  |
| 3125   | Layout 2 | `c3a2e9a87917`  |
| 3118   | Layout 2 | `c3a2e9a87917`  |
| 3111   | Layout 2 | `c3a2e9a87917`  |
| 3103   | Layout 2 | `c3a2e9a87917`  |
| 3095   | Layout 2 | `c3a2e9a87917`  |
| 3086   | Layout 2 | `c3a2e9a87917`  |
| 3072   | Layout 2 | `c3a2e9a87917`  |
| 3062   | Layout 2 | `c3a2e9a87917`  |
| 3052   | Layout 2 | `c3a2e9a87917`  |
| 3045   | Layout 2 | `c3a2e9a87917`  |
| 3037   | Layout 2 | `c3a2e9a87917`  |
| 3030   | Layout 2 | `c3a2e9a87917`  |
| 3021   | Layout 2 | `c3a2e9a87917`  |
| 3012   | Layout 2 | `c3a2e9a87917`  |
| 3002   | Layout 2 | `c3a2e9a87917`  |
| 2995   | Layout 2 | `c3a2e9a87917`  |
| 2987   | Layout 2 | `c3a2e9a87917`  |
| 2978   | Layout 2 | `c3a2e9a87917`  |
| 2970   | Layout 2 | `c3a2e9a87917`  |
| 2959   | Layout 2 | `c3a2e9a87917`  |
| 2951   | Layout 2 | `c3a2e9a87917`  |
| 2942   | Layout 2 | `c3a2e9a87917`  |
| 2935   | Layout 2 | `c3a2e9a87917`  |
| 2932   | Layout 2 | `c3a2e9a87917`  |
| 2923   | Layout 2 | `c3a2e9a87917`  |
| 2919   | Layout 2 | `c3a2e9a87917`  |
| 2907   | Layout 2 | `c3a2e9a87917`  |
| 2900   | Layout 2 | `c3a2e9a87917`  |
| 2891   | Layout 2 | `c3a2e9a87917`  |
| 2882   | Layout 2 | `c3a2e9a87917`  |
| 2872   | Layout 2 | `c3a2e9a87917`  |
| 2863   | Layout 2 | `c3a2e9a87917`  |
| 2855   | Layout 2 | `c3a2e9a87917`  |
| 2849   | Layout 2 | `c3a2e9a87917`  |
| 2844   | Layout 2 | `c3a2e9a87917`  |
| 2834   | Layout 2 | `c3a2e9a87917`  |
| 2825   | Layout 2 | `c3a2e9a87917`  |
| 2819   | Layout 2 | `c3a2e9a87917`  |
| 2811   | Layout 2 | `c3a2e9a87917`  |
| 2803   | Layout 2 | `c3a2e9a87917`  |
| 2794   | Layout 2 | `c3a2e9a87917`  |
| 2783   | Layout 2 | `c3a2e9a87917`  |
| 2774   | Layout 2 | `c3a2e9a87917`  |
| 2765   | Layout 2 | `c3a2e9a87917`  |
| 2756   | Layout 2 | `c3a2e9a87917`  |
| 2750   | Layout 2 | `c3a2e9a87917`  |
| 2743   | Layout 2 | `c3a2e9a87917`  |
| 2736   | Layout 2 | `c3a2e9a87917`  |
| 2726   | Layout 2 | `c3a2e9a87917`  |
| 2717   | Layout 1 | `c3a2e9a87917`  |
| 2709   | Layout 1 | `c3a2e9a87917`  |
| 2703   | Layout 1 | `c3a2e9a87917`  |
| 2695   | Layout 1 | `c3a2e9a87917`  |
| 2684   | Layout 1 | `c3a2e9a87917`  |
| 2672   | Layout 1 | `c3a2e9a87917`  |
| 2665   | Layout 1 | `c3a2e9a87917`  |
| 2657   | Layout 1 | `c3a2e9a87917`  |
| 2649   | Layout 1 | `c3a2e9a87917`  |
| 2644   | Layout 1 | `c3a2e9a87917`  |
| 2637   | Layout 1 | `c3a2e9a87917`  |
| 2629   | Layout 1 | `c3a2e9a87917`  |
| 2619   | Layout 1 | `c3a2e9a87917`  |
| 2612   | Layout 1 | `c3a2e9a87917`  |
| 2606   | Layout 1 | `c3a2e9a87917`  |
| 2602   | Layout 1 | `c3a2e9a87917`  |
| 2601   | Layout 1 | `c3a2e9a87917`  |
| 2592   | Layout 1 | `c3a2e9a87917`  |
| 2583   | Layout 1 | `c3a2e9a87917`  |
| 2575   | Layout 1 | `c3a2e9a87917`  |
| 2567   | Layout 1 | `c3a2e9a87917`  |
| 2560   | Layout 1 | `c3a2e9a87917`  |
| 2553   | Layout 1 | `c3a2e9a87917`  |
| 2545   | Layout 1 | `c3a2e9a87917`  |
| 2538   | Layout 1 | `c3a2e9a87917`  |
| 2529   | Layout 1 | `c3a2e9a87917`  |
| 2519   | Layout 1 | `c3a2e9a87917`  |
| 2513   | Layout 1 | `c3a2e9a87917`  |
| 2510   | Layout 1 | `c3a2e9a87917`  |
| 2507   | Layout 1 | `c3a2e9a87917`  |
| 2503   | Layout 1 | `c3a2e9a87917`  |
| 2498   | Layout 1 | `c3a2e9a87917`  |
| 2492   | Layout 1 | `c3a2e9a87917`  |
| 2487   | Layout 1 | `c3a2e9a87917`  |
| 2480   | Layout 1 | `c3a2e9a87917`  |
| 2474   | Layout 1 | `c3a2e9a87917`  |
| 2468   | Layout 1 | `c3a2e9a87917`  |
| 2460   | Layout 1 | `c3a2e9a87917`  |
| 2453   | Layout 1 | `c3a2e9a87917`  |
| 2444   | Layout 1 | `c3a2e9a87917`  |
| 2438   | Layout 1 | `c3a2e9a87917`  |
| 2434   | Layout 1 | `c3a2e9a87917`  |
| 2429   | Layout 1 | `c3a2e9a87917`  |
| 2421   | Layout 1 | `c3a2e9a87917`  |
| 2414   | Layout 1 | `c3a2e9a87917`  |
| 2407   | Layout 1 | `c3a2e9a87917`  |
| 2401   | Layout 1 | `c3a2e9a87917`  |
| 2397   | Layout 1 | `c3a2e9a87917`  |
| 2393   | Layout 1 | `c3a2e9a87917`  |
| 2384   | Layout 1 | `c3a2e9a87917`  |
| 2378   | Layout 1 | `c3a2e9a87917`  |
| 2372   | Layout 1 | `c3a2e9a87917`  |
| 2358   | Layout 1 | `c3a2e9a87917`  |
| 2352   | Layout 1 | `c3a2e9a87917`  |
| 2347   | Layout 1 | `c3a2e9a87917`  |
| 2343   | Layout 1 | `c3a2e9a87917`  |
| 2335   | Layout 1 | `c3a2e9a87917`  |
| 2327   | Layout 1 | `c3a2e9a87917`  |
| 2324   | Layout 1 | `c3a2e9a87917`  |
| 2319   | Layout 1 | `c3a2e9a87917`  |
| 2313   | Layout 1 | `c3a2e9a87917`  |
| 2308   | Layout 1 | `c3a2e9a87917`  |
| 2302   | Layout 1 | `c3a2e9a87917`  |
| 2295   | Layout 1 | `c3a2e9a87917`  |
| 2290   | Layout 1 | `c3a2e9a87917`  |
| 2284   | Layout 1 | `c3a2e9a87917`  |
| 2276   | Layout 1 | `c3a2e9a87917`  |
| 2269   | Layout 1 | `c3a2e9a87917`  |
| 2259   | Layout 1 | `c3a2e9a87917`  |
| 2250   | Layout 1 | `c3a2e9a87917`  |
| 2243   | Layout 1 | `c3a2e9a87917`  |
| 2235   | Layout 1 | `c3a2e9a87917`  |
| 2229   | Layout 1 | `c3a2e9a87917`  |
| 2224   | Layout 1 | `c3a2e9a87917`  |
| 2218   | Layout 1 | `c3a2e9a87917`  |
| 2215   | Layout 1 | `c3a2e9a87917`  |
| 2207   | Layout 1 | `c3a2e9a87917`  |
| 2203   | Layout 1 | `c3a2e9a87917`  |
| 2196   | Layout 1 | `c3a2e9a87917`  |
| 2192   | Layout 1 | `c3a2e9a87917`  |
| 2189   | Layout 1 | `c3a2e9a87917`  |
| 2183   | Layout 1 | `c3a2e9a87917`  |
| 2179   | Layout 1 | `c3a2e9a87917`  |
| 2171   | Layout 1 | `c3a2e9a87917`  |
| 2163   | Layout 1 | `c3a2e9a87917`  |
| 2156   | Layout 1 | `c3a2e9a87917`  |
| 2151   | Layout 1 | `c3a2e9a87917`  |
| 2147   | Layout 1 | `c3a2e9a87917`  |
| 2142   | Layout 1 | `c3a2e9a87917`  |
| 2138   | Layout 1 | `c3a2e9a87917`  |
| 2134   | Layout 1 | `c3a2e9a87917`  |
| 2130   | Layout 1 | `c3a2e9a87917`  |
| 2122   | Layout 1 | `c3a2e9a87917`  |
| 2107   | Layout 1 | `c3a2e9a87917`  |
| 2098   | Layout 1 | `c3a2e9a87917`  |
| 2089   | Layout 1 | `c3a2e9a87917`  |
| 2081   | Layout 1 | `c3a2e9a87917`  |
| 2073   | Layout 1 | `c3a2e9a87917`  |
| 2067   | Layout 1 | `c3a2e9a87917`  |
| 2063   | Layout 1 | `c3a2e9a87917`  |
| 2059   | Layout 1 | `c3a2e9a87917`  |
| 2052   | Layout 1 | `c3a2e9a87917`  |
| 2044   | Layout 1 | `c3a2e9a87917`  |
| 2039   | Layout 1 | `c3a2e9a87917`  |
| 2032   | Layout 1 | `c3a2e9a87917`  |
| 2025   | Layout 1 | `c3a2e9a87917`  |
| 2011   | Layout 1 | `c3a2e9a87917`  |
| 2005   | Layout 1 | `c3a2e9a87917`  |
| 2000   | Layout 1 | `c3a2e9a87917`  |
| 1996   | Layout 1 | `c3a2e9a87917`  |
| 1991   | Layout 1 | `c3a2e9a87917`  |
| 1985   | Layout 1 | `c3a2e9a87917`  |
| 1980   | Layout 1 | `c3a2e9a87917`  |
| 1969   | Layout 1 | `c3a2e9a87917`  |
| 1964   | Layout 1 | `c3a2e9a87917`  |
| 1958   | Layout 1 | `c3a2e9a87917`  |
| 1950   | Layout 1 | `c3a2e9a87917`  |
| 1945   | Layout 1 | `c3a2e9a87917`  |
| 1937   | Layout 1 | `c3a2e9a87917`  |
| 1933   | Layout 1 | `c3a2e9a87917`  |
| 1927   | Layout 1 | `c3a2e9a87917`  |
| 1921   | Layout 1 | `c3a2e9a87917`  |
| 1914   | Layout 1 | `c3a2e9a87917`  |
| 1908   | Layout 1 | `c3a2e9a87917`  |
| 1897   | Layout 1 | `c3a2e9a87917`  |
| 1892   | Layout 1 | `c3a2e9a87917`  |
| 1886   | Layout 1 | `c3a2e9a87917`  |
| 1881   | Layout 1 | `c3a2e9a87917`  |
| 1871   | Layout 1 | `c3a2e9a87917`  |
| 1866   | Layout 1 | `c3a2e9a87917`  |
| 1862   | Layout 1 | `c3a2e9a87917`  |
| 1854   | Layout 1 | `c3a2e9a87917`  |
| 1846   | Layout 1 | `c3a2e9a87917`  |
| 1838   | Layout 1 | `c3a2e9a87917`  |
| 1832   | Layout 1 | `c3a2e9a87917`  |
| 1826   | Layout 1 | `c3a2e9a87917`  |
| 1822   | Layout 1 | `c3a2e9a87917`  |
| 1818   | Layout 1 | `c3a2e9a87917`  |
| 1804   | Layout 1 | `c3a2e9a87917`  |
| 1794   | Layout 1 | `c3a2e9a87917`  |
| 1790   | Layout 1 | `c3a2e9a87917`  |
| 1784   | Layout 1 | `c3a2e9a87917`  |
| 1774   | Layout 1 | `c3a2e9a87917`  |
| 1771   | Layout 1 | `c3a2e9a87917`  |
| 1762   | Layout 1 | `c3a2e9a87917`  |
| 1759   | Layout 1 | `c3a2e9a87917`  |
| 1754   | Layout 1 | `c3a2e9a87917`  |
| 1749   | Layout 1 | `c3a2e9a87917`  |
| 1743   | Layout 1 | `c3a2e9a87917`  |
| 1737   | Layout 1 | `c3a2e9a87917`  |
| 1731   | Layout 1 | `c3a2e9a87917`  |
| 1725   | Layout 1 | `c3a2e9a87917`  |
| 1717   | Layout 1 | `c3a2e9a87917`  |
| 1710   | Layout 1 | `c3a2e9a87917`  |
| 1704   | Layout 1 | `c3a2e9a87917`  |
| 1698   | Layout 1 | `c3a2e9a87917`  |
| 1690   | Layout 1 | `c3a2e9a87917`  |
| 1685   | Layout 1 | `c3a2e9a87917`  |
| 1680   | Layout 1 | `c3a2e9a87917`  |
| 1674   | Layout 1 | `c3a2e9a87917`  |
| 1668   | Layout 1 | `c3a2e9a87917`  |
| 1659   | Layout 1 | `c3a2e9a87917`  |
| 1649   | Layout 1 | `c3a2e9a87917`  |
| 1642   | Layout 1 | `c3a2e9a87917`  |
| 1636   | Layout 1 | `c3a2e9a87917`  |
| 1628   | Layout 1 | `c3a2e9a87917`  |
| 1622   | Layout 1 | `c3a2e9a87917`  |
| 1614   | Layout 1 | `c3a2e9a87917`  |
| 1608   | Layout 1 | `c3a2e9a87917`  |
| 1602   | Layout 1 | `c3a2e9a87917`  |
| 1598   | Layout 1 | `c3a2e9a87917`  |
| 1594   | Layout 1 | `c3a2e9a87917`  |
| 1590   | Layout 1 | `c3a2e9a87917`  |
| 1587   | Layout 1 | `c3a2e9a87917`  |
| 1584   | Layout 1 | `c3a2e9a87917`  |
| 1579   | Layout 1 | `c3a2e9a87917`  |
| 1572   | Layout 1 | `c3a2e9a87917`  |
| 1565   | Layout 1 | `c3a2e9a87917`  |
| 1559   | Layout 1 | `c3a2e9a87917`  |
| 1554   | Layout 1 | `c3a2e9a87917`  |
| 1547   | Layout 1 | `c3a2e9a87917`  |
| 1537   | Layout 1 | `c3a2e9a87917`  |
| 1529   | Layout 1 | `c3a2e9a87917`  |
| 1524   | Layout 1 | `c3a2e9a87917`  |
| 1519   | Layout 1 | `c3a2e9a87917`  |
| 1509   | Layout 1 | `c3a2e9a87917`  |
| 1506   | Layout 1 | `c3a2e9a87917`  |
| 1504   | Layout 1 | `c3a2e9a87917`  |
| 1500   | Layout 1 | `c3a2e9a87917`  |
| 1493   | Layout 1 | `c3a2e9a87917`  |
| 1489   | Layout 1 | `c3a2e9a87917`  |
| 1485   | Layout 1 | `c3a2e9a87917`  |
| 1481   | Layout 1 | `c3a2e9a87917`  |
| 1474   | Layout 1 | `c3a2e9a87917`  |
| 1466   | Layout 1 | `c3a2e9a87917`  |
| 1462   | Layout 1 | `c3a2e9a87917`  |
| 1459   | Layout 1 | `c3a2e9a87917`  |
| 1453   | Layout 1 | `c3a2e9a87917`  |
| 1450   | Layout 1 | `c3a2e9a87917`  |
| 1445   | Layout 1 | `c3a2e9a87917`  |
| 1439   | Layout 1 | `c3a2e9a87917`  |
| 1433   | Layout 1 | `c3a2e9a87917`  |
| 1430   | Layout 1 | `c3a2e9a87917`  |
| 1426   | Layout 1 | `c3a2e9a87917`  |
| 1421   | Layout 1 | `c3a2e9a87917`  |
| 1417   | Layout 1 | `c3a2e9a87917`  |
| 1416   | Layout 1 | `c3a2e9a87917`  |
| 1409   | Layout 1 | `c3a2e9a87917`  |
| 1405   | Layout 1 | `c3a2e9a87917`  |
| 1401   | Layout 1 | `c3a2e9a87917`  |
| 1396   | Layout 1 | `c3a2e9a87917`  |
| 1391   | Layout 1 | `c3a2e9a87917`  |
| 1390   | Layout 1 | `c3a2e9a87917`  |
| 1386   | Layout 1 | `c3a2e9a87917`  |
| 1381   | Layout 1 | `c3a2e9a87917`  |
| 1379   | Layout 1 | `c3a2e9a87917`  |
| 1372   | Layout 1 | `c3a2e9a87917`  |
| 1366   | Layout 1 | `c3a2e9a87917`  |
| 1364   | Layout 1 | `c3a2e9a87917`  |
| 1363   | Layout 1 | `c3a2e9a87917`  |
| 1360   | Layout 1 | `c3a2e9a87917`  |
| 1358   | Layout 1 | `c3a2e9a87917`  |
| 1355   | Layout 1 | `c3a2e9a87917`  |
| 1351   | Layout 1 | `c3a2e9a87917`  |
| 1348   | Layout 1 | `c3a2e9a87917`  |
| 1346   | Layout 1 | `c3a2e9a87917`  |
| 1341   | Layout 1 | `c3a2e9a87917`  |
| 1340   | Layout 1 | `c3a2e9a87917`  |
| 1338   | Layout 1 | `c3a2e9a87917`  |
| 1335   | Layout 1 | `c3a2e9a87917`  |
| 1333   | Layout 1 | `c3a2e9a87917`  |
| 1329   | Layout 1 | `c3a2e9a87917`  |
| 1327   | Layout 1 | `c3a2e9a87917`  |
| 1324   | Layout 1 | `c3a2e9a87917`  |
| 1321   | Layout 1 | `c3a2e9a87917`  |
| 1319   | Layout 1 | `c3a2e9a87917`  |
| 1318   | Layout 1 | `c3a2e9a87917`  |
| 1316   | Layout 1 | `c3a2e9a87917`  |
| 1313   | Layout 1 | `c3a2e9a87917`  |
| 1311   | Layout 1 | `c3a2e9a87917`  |
| 1309   | Layout 1 | `c3a2e9a87917`  |
| 1304   | Layout 1 | `c3a2e9a87917`  |
| 1292   | Layout 1 | `c3a2e9a87917`  |
| 1286   | Layout 1 | `c3a2e9a87917`  |
| 1280   | Layout 1 | `c3a2e9a87917`  |
| 1276   | Layout 1 | `c3a2e9a87917`  |
| 1267   | Layout 1 | `c3a2e9a87917`  |
| 1261   | No file  | `c3a2e9a87917`  |
| 1256   | No file  | `c3a2e9a87917`  |
| 1250   | No file  | `c3a2e9a87917`  |
| 1246   | No file  | `c3a2e9a87917`  |
| 1239   | No file  | `c3a2e9a87917`  |
| 1230   | No file  | `c3a2e9a87917`  |
| 1226   | No file  | `c3a2e9a87917`  |
| 1220   | No file  | `c3a2e9a87917`  |
| 1217   | No file  | `c3a2e9a87917`  |
| 1211   | No file  | `c3a2e9a87917`  |
| 1210   | No file  | `c3a2e9a87917`  |
| 1208   | No file  | `c3a2e9a87917`  |
| 1203   | No file  | `c3a2e9a87917`  |
| 1197   | No file  | `c3a2e9a87917`  |
| 1194   | No file  | `c3a2e9a87917`  |
| 1192   | No file  | `c3a2e9a87917`  |
| 1187   | No file  | `c3a2e9a87917`  |
| 1183   | No file  | `c3a2e9a87917`  |
| 1177   | No file  | `c3a2e9a87917`  |
| 1173   | No file  | `c3a2e9a87917`  |
| 1167   | No file  | `c3a2e9a87917`  |
| 1164   | No file  | `c3a2e9a87917`  |
| 1156   | No file  | `c3a2e9a87917`  |
| 1149   | No file  | `c3a2e9a87917`  |
| 1144   | No file  | `c3a2e9a87917`  |
| 1137   | No file  | `c3a2e9a87917`  |
| 1132   | No file  | `c3a2e9a87917`  |
| 1127   | No file  | `c3a2e9a87917`  |
| 1122   | No file  | `c3a2e9a87917`  |
| 1118   | No file  | `c3a2e9a87917`  |
| 1114   | No file  | `c3a2e9a87917`  |
| 1109   | No file  | `c3a2e9a87917`  |
| 1102   | No file  | `c3a2e9a87917`  |
| 1096   | No file  | `c3a2e9a87917`  |
| 1088   | No file  | `c3a2e9a87917`  |
| 1081   | No file  | `c3a2e9a87917`  |
| 1076   | No file  | `c3a2e9a87917`  |
| 1069   | No file  | `c3a2e9a87917`  |
| 1064   | No file  | `c3a2e9a87917`  |
| 1058   | No file  | `c3a2e9a87917`  |
| 1051   | No file  | `c3a2e9a87917`  |
| 1044   | No file  | `c3a2e9a87917`  |
| 1036   | No file  | `c3a2e9a87917`  |
| 1026   | No file  | `c3a2e9a87917`  |
| 1016   | No file  | `c3a2e9a87917`  |
| 1009   | No file  | `c3a2e9a87917`  |
| 1005   | No file  | `c3a2e9a87917`  |
| 1000   | No file  | `c3a2e9a87917`  |
| 998    | No file  | `c3a2e9a87917`  |
| 990    | No file  | `c3a2e9a87917`  |
| 979    | No file  | `c3a2e9a87917`  |
| 972    | No file  | `c3a2e9a87917`  |
| 963    | No file  | `c3a2e9a87917`  |
| 955    | No file  | `c3a2e9a87917`  |
| 946    | No file  | `c3a2e9a87917`  |
| 938    | No file  | `c3a2e9a87917`  |
| 927    | No file  | `c3a2e9a87917`  |
| 911    | No file  | `c3a2e9a87917`  |
| 904    | No file  | `c3a2e9a87917`  |
| 899    | No file  | `c3a2e9a87917`  |
| 894    | No file  | `c3a2e9a87917`  |
| 885    | No file  | `c3a2e9a87917`  |
| 879    | No file  | `c3a2e9a87917`  |
| 872    | No file  | `c3a2e9a87917`  |
| 864    | No file  | `c3a2e9a87917`  |
| 855    | No file  | `c3a2e9a87917`  |
| 853    | No file  | `c3a2e9a87917`  |
| 845    | No file  | `c3a2e9a87917`  |
| 837    | No file  | `c3a2e9a87917`  |
| 829    | No file  | `c3a2e9a87917`  |
| 822    | No file  | `c3a2e9a87917`  |
| 814    | No file  | `c3a2e9a87917`  |
| 805    | No file  | `c3a2e9a87917`  |
| 794    | No file  | `c3a2e9a87917`  |
| 787    | No file  | `c3a2e9a87917`  |
| 780    | No file  | `c3a2e9a87917`  |
| 771    | No file  | `c3a2e9a87917`  |
| 760    | No file  | `c3a2e9a87917`  |
| 748    | No file  | `c3a2e9a87917`  |
| 741    | No file  | `c3a2e9a87917`  |
| 736    | No file  | `c3a2e9a87917`  |
| 731    | No file  | `c3a2e9a87917`  |
| 723    | No file  | `c3a2e9a87917`  |
| 711    | No file  | `c3a2e9a87917`  |
| 707    | No file  | `c3a2e9a87917`  |
| 697    | No file  | `c3a2e9a87917`  |
| 689    | No file  | `c3a2e9a87917`  |
| 683    | No file  | `c3a2e9a87917`  |
| 678    | No file  | `c3a2e9a87917`  |
| 670    | No file  | `c3a2e9a87917`  |
| 661    | No file  | `c3a2e9a87917`  |
| 656    | No file  | `c3a2e9a87917`  |
| 652    | No file  | `c3a2e9a87917`  |
| 643    | No file  | `c3a2e9a87917`  |
| 637    | No file  | `c3a2e9a87917`  |
| 630    | No file  | `c3a2e9a87917`  |
| 627    | No file  | `c3a2e9a87917`  |
| 621    | No file  | `c3a2e9a87917`  |
| 617    | No file  | `c3a2e9a87917`  |
| 615    | No file  | `c3a2e9a87917`  |
| 606    | No file  | `c3a2e9a87917`  |
| 599    | No file  | `c3a2e9a87917`  |
| 592    | No file  | `c3a2e9a87917`  |
| 586    | No file  | `c3a2e9a87917`  |
| 577    | No file  | `c3a2e9a87917`  |
| 569    | No file  | `c3a2e9a87917`  |
| 561    | No file  | `c3a2e9a87917`  |
| 554    | No file  | `c3a2e9a87917`  |
| 542    | No file  | `c3a2e9a87917`  |
| 532    | No file  | `c3a2e9a87917`  |
| 531    | No file  | `c3a2e9a87917`  |
| 526    | No file  | `c3a2e9a87917`  |
| 521    | No file  | `c3a2e9a87917`  |
| 517    | No file  | `c3a2e9a87917`  |
| 510    | No file  | `c3a2e9a87917`  |
| 508    | No file  | `c3a2e9a87917`  |
| 504    | No file  | `c3a2e9a87917`  |
| 497    | No file  | `c3a2e9a87917`  |
| 491    | No file  | `c3a2e9a87917`  |
| 485    | No file  | `c3a2e9a87917`  |
| 478    | No file  | `c3a2e9a87917`  |
| 472    | No file  | `c3a2e9a87917`  |
| 466    | No file  | `c3a2e9a87917`  |
| 457    | No file  | `c3a2e9a87917`  |
| 452    | No file  | `c3a2e9a87917`  |
| 449    | No file  | `c3a2e9a87917`  |
| 435    | No file  | `c3a2e9a87917`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                                   |
| ------------------------- | -------- | -------------------------------------------------------------------------------------- |
| `floatfishingoffset.dbss` | Optional | `fishing_group_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `floatfishingpoint.dbss`  | Optional | The fishing points that use each group, for the Points column                          |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then 70-byte rows; the
file ends after the last row.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 418 x 70 = 29,264 bytes.

### Row (70 bytes)

| Offset  | Type      | Field             | Notes                                                                                     |
| ------- | --------- | ----------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16       | fishing_group_key | Unique; the `fishing_group_key` of a [`floatfishingpoint.dbss`](floatfishingpoint_dbss.md) row points here |
| `+0x02` | bytes[28] | unknown_02        | `0` on every row of clients 1784 and 3474; see Open Questions                             |
| `+0x1E` | u32[5]    | drop_ids          | Item drop group per slot, see Drop Slots; `0` for an empty slot                           |
| `+0x32` | u32[5]    | drop_rates        | Chance of each slot on the 1,000,000 = 100% scale; `0` for an empty slot                  |

The rows are not sorted by key; the file starts with `239`, `238`, `237`.

### `floatfishingoffset.dbss`

Bare offset table into `floatfishing.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `floatfishing.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (10 bytes)

| Offset  | Type | Field             | Notes                                                            |
| ------- | ---- | ----------------- | ---------------------------------------------------------------- |
| `+0x00` | u16  | fishing_group_key | Key of the row it points at                                      |
| `+0x02` | u32  | data_offset       | Absolute offset of the row in `floatfishing.dbss`, at its key    |
| `+0x06` | u32  | data_size         | `70` on every row: the whole row                                 |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order, and on clients 1784 and 3474 every one points at
the row with its key.

## Layout 1

### Row (60 bytes)

The drop groups are u16; every other field is as in Layout 2.

| Offset  | Type      | Field             | Notes                                       |
| ------- | --------- | ----------------- | ------------------------------------------- |
| `+0x00` | u16       | fishing_group_key |                                             |
| `+0x02` | bytes[28] | unknown_02        |                                             |
| `+0x1E` | u16[5]    | drop_ids          |                                             |
| `+0x28` | u32[5]    | drop_rates        |                                             |

On client 1784 the file is 4 + 410 x 60 = 24,604 bytes, and the offset rows
give `60` as the size.

## Drop Slots

The slot names are the developer comments (`<주석>` row) of the
`FloatFishing_Table` sheet in a private server's `datasheet_regiondatatable.xlsm`
on client 1784.

| Slot | `drop_ids` / `drop_rates` index | Sheet columns          | Comment          |
| ---- | ------------------------------- | ---------------------- | ---------------- |
| 1    | 0                               | `DropID1`, `DropRate1` | Treasure (`보물`) |
| 2    | 1                               | `DropID2`, `DropRate2` | Rare (`희귀`)     |
| 3    | 2                               | `DropID3`, `DropRate3` | Large (`대형`)    |
| 4    | 3                               | `DropID4`, `DropRate4` | General (`일반`)  |
| 5    | 4                               | `DropID5`, `DropRate5` | Junk (`잡템`)     |

On clients 1784 and 3474 every row fills slot 2 only, with rate
`1000000`. Client 3474 uses 20 drop groups there, `10916` to `10950`;
`10936` sits on 74 rows, `10935` on 44 and `10940` on 36. None of them is a
`group_id` of [`itemmaingroup.bss`](itemmaingroup_bss.md) or a subgroup of
`itemsubgroup.dbss`, so the client files do not say which fish they hold.

## Field Names

The `FloatFishing_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `FishingGroupKey`, `DropRate1`, `DropID1` to
`DropRate5`, `DropID5`, `MinWaitTime`, `MaxWaitTime`, `PointRemainTime`,
`MinFishCount`, `MaxFishCount`, `AvailableFishingLevel`,
`ObserveFishingLevel` and `ContentsGroupKey`. Its 410 rows match the 410
rows of client 1784 on the key, all five `DropID` values and `DropRate2`
(410 of 410). The sheet holds `100` in the empty slots' `DropRate`
columns; the client file holds `0` there.

## Notes

- Client 3474 holds the 410 groups of client 1784 unchanged and adds groups
  `440` to `447`.
- 16 groups have no fishing point in `floatfishingpoint.dbss` on client
  3474: `432` to `439`, the eight sheet rows with `ContentsGroupKey` `1633`
  whose points the client file leaves out, and the new `440` to `447`.
- The sheet's `ContentsGroupKey` column is not in the client file.

## Open Questions

### unknown_02

28 bytes that are `0` on every row of clients 1784 and 3474. The sheet
columns `MinWaitTime`, `MaxWaitTime`, `PointRemainTime`, `MinFishCount`,
`MaxFishCount`, `AvailableFishingLevel` and `ObserveFishingLevel` carry the
`%` (server-only) prefix in `datasheet_regiondatatable.xlsm` and are not
`0` there (`80830`, `110830`, `1282211`, `1`, `1`, `11`, `21` on group 1),
so a client build writes them as `0`. Seven u32 fill 28 bytes, but with
only zeros the order and widths cannot be read from the file.
