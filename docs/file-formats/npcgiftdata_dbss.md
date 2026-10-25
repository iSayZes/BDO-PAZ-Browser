# `npcgiftdata.dbss` Format

## Purpose

The NPC's reply to a confession (the Confess button of the gift window): one
variable-length record per NPC with the Korean text. The NPC IDs are the same
24 as in [`npcgift.dbss`](npcgift_dbss.md), which holds the accepted gift
items. LOC type 54 has the reply in the user's language, keyed by `npc_id`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records            | Row bytes                 |
| ------ | -------------- | ------------------------ | ----- | ------------------ | ------------------------- |
| 1      | 1346 and later | `npcgiftdata.dbss`       | 6,702 | 24 Dialogue Record | 32 to 462, 279 on average |
| 1      | 1346 and later | `npcgiftdataoffset.dbss` | 244   | 24 Offset Record   | 10                        |

| Layout | File                     | Known           | Unknown      |
| ------ | ------------------------ | --------------- | ------------ |
| 1      | `npcgiftdata.dbss`       | 6,510 B (97.1%) | 192 B (2.9%) |
| 1      | `npcgiftdataoffset.dbss` | 196 B (80.3%)   | 48 B (19.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `c1ce3fc0a8e8`  |
| 3482   | Layout 1             | `c1ce3fc0a8e8`  |
| 3474   | Layout 1             | `c1ce3fc0a8e8`  |
| 3473   | Layout 1             | `c1ce3fc0a8e8`  |
| 3464   | Layout 1             | `c1ce3fc0a8e8`  |
| 3458   | Layout 1             | `c1ce3fc0a8e8`  |
| 3454   | Layout 1             | `c1ce3fc0a8e8`  |
| 3444   | Layout 1             | `c1ce3fc0a8e8`  |
| 3435   | Layout 1             | `c1ce3fc0a8e8`  |
| 3426   | Layout 1             | `c1ce3fc0a8e8`  |
| 3418   | Layout 1             | `c1ce3fc0a8e8`  |
| 3412   | Layout 1             | `c1ce3fc0a8e8`  |
| 3402   | Layout 1             | `c1ce3fc0a8e8`  |
| 3396   | Layout 1             | `c1ce3fc0a8e8`  |
| 3387   | Layout 1             | `c1ce3fc0a8e8`  |
| 3381   | Layout 1             | `c1ce3fc0a8e8`  |
| 3373   | Layout 1             | `c1ce3fc0a8e8`  |
| 3364   | Layout 1             | `c1ce3fc0a8e8`  |
| 3356   | Layout 1             | `c1ce3fc0a8e8`  |
| 3349   | Layout 1             | `c1ce3fc0a8e8`  |
| 3342   | Layout 1             | `c1ce3fc0a8e8`  |
| 3335   | Layout 1             | `c1ce3fc0a8e8`  |
| 3326   | Layout 1             | `c1ce3fc0a8e8`  |
| 3321   | Layout 1             | `c1ce3fc0a8e8`  |
| 3314   | Layout 1             | `c1ce3fc0a8e8`  |
| 3303   | Layout 1             | `c1ce3fc0a8e8`  |
| 3302   | Layout 1             | `c1ce3fc0a8e8`  |
| 3293   | Layout 1             | `c1ce3fc0a8e8`  |
| 3283   | Layout 1             | `c1ce3fc0a8e8`  |
| 3275   | Layout 1             | `c1ce3fc0a8e8`  |
| 3267   | Layout 1             | `c1ce3fc0a8e8`  |
| 3258   | Layout 1             | `c1ce3fc0a8e8`  |
| 3251   | Layout 1             | `c1ce3fc0a8e8`  |
| 3242   | Layout 1             | `c1ce3fc0a8e8`  |
| 3235   | Layout 1             | `c1ce3fc0a8e8`  |
| 3229   | Layout 1             | `c1ce3fc0a8e8`  |
| 3212   | Layout 1             | `c1ce3fc0a8e8`  |
| 3203   | Layout 1             | `c1ce3fc0a8e8`  |
| 3193   | Layout 1             | `c1ce3fc0a8e8`  |
| 3186   | Layout 1             | `c1ce3fc0a8e8`  |
| 3177   | Layout 1             | `c1ce3fc0a8e8`  |
| 3169   | Layout 1             | `c1ce3fc0a8e8`  |
| 3158   | Layout 1             | `c1ce3fc0a8e8`  |
| 3151   | Layout 1             | `c1ce3fc0a8e8`  |
| 3144   | Layout 1             | `c1ce3fc0a8e8`  |
| 3133   | Layout 1             | `c1ce3fc0a8e8`  |
| 3125   | Layout 1             | `c1ce3fc0a8e8`  |
| 3118   | Layout 1             | `c1ce3fc0a8e8`  |
| 3111   | Layout 1             | `c1ce3fc0a8e8`  |
| 3103   | Layout 1             | `c1ce3fc0a8e8`  |
| 3095   | Layout 1             | `c1ce3fc0a8e8`  |
| 3086   | Layout 1             | `c1ce3fc0a8e8`  |
| 3072   | Layout 1             | `c1ce3fc0a8e8`  |
| 3062   | Layout 1             | `c1ce3fc0a8e8`  |
| 3052   | Layout 1             | `c1ce3fc0a8e8`  |
| 3045   | Layout 1             | `c1ce3fc0a8e8`  |
| 3037   | Layout 1             | `c1ce3fc0a8e8`  |
| 3030   | Layout 1             | `c1ce3fc0a8e8`  |
| 3021   | Layout 1             | `c1ce3fc0a8e8`  |
| 3012   | Layout 1             | `c1ce3fc0a8e8`  |
| 3002   | Layout 1             | `c1ce3fc0a8e8`  |
| 2995   | Layout 1             | `c1ce3fc0a8e8`  |
| 2987   | Layout 1             | `c1ce3fc0a8e8`  |
| 2978   | Layout 1             | `c1ce3fc0a8e8`  |
| 2970   | Layout 1             | `c1ce3fc0a8e8`  |
| 2959   | Layout 1             | `c1ce3fc0a8e8`  |
| 2951   | Layout 1             | `c1ce3fc0a8e8`  |
| 2942   | Layout 1             | `c1ce3fc0a8e8`  |
| 2935   | Layout 1             | `c1ce3fc0a8e8`  |
| 2932   | Layout 1             | `c1ce3fc0a8e8`  |
| 2923   | Layout 1             | `c1ce3fc0a8e8`  |
| 2919   | Layout 1             | `c1ce3fc0a8e8`  |
| 2907   | Layout 1             | `c1ce3fc0a8e8`  |
| 2900   | Layout 1             | `c1ce3fc0a8e8`  |
| 2891   | Layout 1             | `c1ce3fc0a8e8`  |
| 2882   | Layout 1             | `c1ce3fc0a8e8`  |
| 2872   | Layout 1             | `c1ce3fc0a8e8`  |
| 2863   | Layout 1             | `c1ce3fc0a8e8`  |
| 2855   | Layout 1             | `c1ce3fc0a8e8`  |
| 2849   | Layout 1             | `c1ce3fc0a8e8`  |
| 2844   | Layout 1             | `c1ce3fc0a8e8`  |
| 2834   | Layout 1             | `c1ce3fc0a8e8`  |
| 2825   | Layout 1             | `c1ce3fc0a8e8`  |
| 2819   | Layout 1             | `c1ce3fc0a8e8`  |
| 2811   | Layout 1             | `c1ce3fc0a8e8`  |
| 2803   | Layout 1             | `c1ce3fc0a8e8`  |
| 2794   | Layout 1             | `c1ce3fc0a8e8`  |
| 2783   | Layout 1             | `c1ce3fc0a8e8`  |
| 2774   | Layout 1             | `c1ce3fc0a8e8`  |
| 2765   | Layout 1             | `c1ce3fc0a8e8`  |
| 2756   | Layout 1             | `c1ce3fc0a8e8`  |
| 2750   | Layout 1             | `c1ce3fc0a8e8`  |
| 2743   | Layout 1             | `c1ce3fc0a8e8`  |
| 2736   | Layout 1             | `c1ce3fc0a8e8`  |
| 2726   | Layout 1             | `c1ce3fc0a8e8`  |
| 2717   | Layout 1             | `c1ce3fc0a8e8`  |
| 2709   | Layout 1             | `c1ce3fc0a8e8`  |
| 2703   | Layout 1             | `c1ce3fc0a8e8`  |
| 2695   | Layout 1             | `c1ce3fc0a8e8`  |
| 2684   | Layout 1             | `c1ce3fc0a8e8`  |
| 2672   | Layout 1             | `c1ce3fc0a8e8`  |
| 2665   | Layout 1             | `c1ce3fc0a8e8`  |
| 2657   | Layout 1             | `c1ce3fc0a8e8`  |
| 2649   | Layout 1             | `c1ce3fc0a8e8`  |
| 2644   | Layout 1             | `c1ce3fc0a8e8`  |
| 2637   | Layout 1             | `c1ce3fc0a8e8`  |
| 2629   | Layout 1             | `c1ce3fc0a8e8`  |
| 2619   | Layout 1             | `c1ce3fc0a8e8`  |
| 2612   | Layout 1             | `c1ce3fc0a8e8`  |
| 2606   | Layout 1             | `c1ce3fc0a8e8`  |
| 2602   | Layout 1             | `c1ce3fc0a8e8`  |
| 2601   | Layout 1             | `c1ce3fc0a8e8`  |
| 2592   | Layout 1             | `c1ce3fc0a8e8`  |
| 2583   | Layout 1             | `c1ce3fc0a8e8`  |
| 2575   | Layout 1             | `c1ce3fc0a8e8`  |
| 2567   | Layout 1             | `c1ce3fc0a8e8`  |
| 2560   | Layout 1             | `c1ce3fc0a8e8`  |
| 2553   | Layout 1             | `c1ce3fc0a8e8`  |
| 2545   | Layout 1             | `c1ce3fc0a8e8`  |
| 2538   | Layout 1             | `c1ce3fc0a8e8`  |
| 2529   | Layout 1             | `c1ce3fc0a8e8`  |
| 2519   | Layout 1             | `c1ce3fc0a8e8`  |
| 2513   | Layout 1             | `c1ce3fc0a8e8`  |
| 2510   | Layout 1             | `c1ce3fc0a8e8`  |
| 2507   | Layout 1             | `c1ce3fc0a8e8`  |
| 2503   | Layout 1             | `c1ce3fc0a8e8`  |
| 2498   | Layout 1             | `c1ce3fc0a8e8`  |
| 2492   | Layout 1             | `c1ce3fc0a8e8`  |
| 2487   | Layout 1             | `c1ce3fc0a8e8`  |
| 2480   | Layout 1             | `c1ce3fc0a8e8`  |
| 2474   | Layout 1             | `c1ce3fc0a8e8`  |
| 2468   | Layout 1             | `c1ce3fc0a8e8`  |
| 2460   | Layout 1             | `c1ce3fc0a8e8`  |
| 2453   | Layout 1             | `c1ce3fc0a8e8`  |
| 2444   | Layout 1             | `c1ce3fc0a8e8`  |
| 2438   | Layout 1             | `c1ce3fc0a8e8`  |
| 2434   | Layout 1             | `c1ce3fc0a8e8`  |
| 2429   | Layout 1             | `c1ce3fc0a8e8`  |
| 2421   | Layout 1             | `c1ce3fc0a8e8`  |
| 2414   | Layout 1             | `c1ce3fc0a8e8`  |
| 2407   | Layout 1             | `c1ce3fc0a8e8`  |
| 2401   | Layout 1             | `c1ce3fc0a8e8`  |
| 2397   | Layout 1             | `c1ce3fc0a8e8`  |
| 2393   | Layout 1             | `c1ce3fc0a8e8`  |
| 2384   | Layout 1             | `c1ce3fc0a8e8`  |
| 2378   | Layout 1             | `c1ce3fc0a8e8`  |
| 2372   | Layout 1             | `c1ce3fc0a8e8`  |
| 2358   | Layout 1             | `c1ce3fc0a8e8`  |
| 2352   | Layout 1             | `c1ce3fc0a8e8`  |
| 2347   | Layout 1             | `c1ce3fc0a8e8`  |
| 2343   | Layout 1             | `c1ce3fc0a8e8`  |
| 2335   | Layout 1             | `c1ce3fc0a8e8`  |
| 2327   | Layout 1             | `c1ce3fc0a8e8`  |
| 2324   | Layout 1             | `c1ce3fc0a8e8`  |
| 2319   | Layout 1             | `c1ce3fc0a8e8`  |
| 2313   | Layout 1             | `c1ce3fc0a8e8`  |
| 2308   | Layout 1             | `c1ce3fc0a8e8`  |
| 2302   | Layout 1             | `c1ce3fc0a8e8`  |
| 2295   | Layout 1             | `c1ce3fc0a8e8`  |
| 2290   | Layout 1             | `c1ce3fc0a8e8`  |
| 2284   | Layout 1             | `c1ce3fc0a8e8`  |
| 2276   | Layout 1             | `c1ce3fc0a8e8`  |
| 2269   | Layout 1             | `c1ce3fc0a8e8`  |
| 2259   | Layout 1             | `c1ce3fc0a8e8`  |
| 2250   | Layout 1             | `c1ce3fc0a8e8`  |
| 2243   | Layout 1             | `c1ce3fc0a8e8`  |
| 2235   | Layout 1             | `c1ce3fc0a8e8`  |
| 2229   | Layout 1             | `c1ce3fc0a8e8`  |
| 2224   | Layout 1             | `c1ce3fc0a8e8`  |
| 2218   | Layout 1             | `c1ce3fc0a8e8`  |
| 2215   | Layout 1             | `c1ce3fc0a8e8`  |
| 2207   | Layout 1             | `c1ce3fc0a8e8`  |
| 2203   | Layout 1             | `c1ce3fc0a8e8`  |
| 2196   | Layout 1             | `c1ce3fc0a8e8`  |
| 2192   | Layout 1             | `c1ce3fc0a8e8`  |
| 2189   | Layout 1             | `c1ce3fc0a8e8`  |
| 2183   | Layout 1             | `c1ce3fc0a8e8`  |
| 2179   | Layout 1             | `c1ce3fc0a8e8`  |
| 2171   | Layout 1             | `c1ce3fc0a8e8`  |
| 2163   | Layout 1             | `c1ce3fc0a8e8`  |
| 2156   | Layout 1             | `c1ce3fc0a8e8`  |
| 2151   | Layout 1             | `c1ce3fc0a8e8`  |
| 2147   | Layout 1             | `c1ce3fc0a8e8`  |
| 2142   | Layout 1             | `c1ce3fc0a8e8`  |
| 2138   | Layout 1             | `c1ce3fc0a8e8`  |
| 2134   | Layout 1             | `c1ce3fc0a8e8`  |
| 2130   | Layout 1             | `c1ce3fc0a8e8`  |
| 2122   | Layout 1             | `c1ce3fc0a8e8`  |
| 2107   | Layout 1             | `c1ce3fc0a8e8`  |
| 2098   | Layout 1             | `c1ce3fc0a8e8`  |
| 2089   | Layout 1             | `c1ce3fc0a8e8`  |
| 2081   | Layout 1             | `c1ce3fc0a8e8`  |
| 2073   | Layout 1             | `c1ce3fc0a8e8`  |
| 2067   | Layout 1             | `c1ce3fc0a8e8`  |
| 2063   | Layout 1             | `c1ce3fc0a8e8`  |
| 2059   | Layout 1             | `c1ce3fc0a8e8`  |
| 2052   | Layout 1             | `c1ce3fc0a8e8`  |
| 2044   | Layout 1             | `c1ce3fc0a8e8`  |
| 2039   | Layout 1             | `c1ce3fc0a8e8`  |
| 2032   | Layout 1             | `c1ce3fc0a8e8`  |
| 2025   | Layout 1             | `c1ce3fc0a8e8`  |
| 2011   | Layout 1             | `c1ce3fc0a8e8`  |
| 2005   | Layout 1             | `c1ce3fc0a8e8`  |
| 2000   | Layout 1             | `c1ce3fc0a8e8`  |
| 1996   | Layout 1             | `c1ce3fc0a8e8`  |
| 1991   | Layout 1             | `c1ce3fc0a8e8`  |
| 1985   | Layout 1             | `c1ce3fc0a8e8`  |
| 1980   | Layout 1             | `c1ce3fc0a8e8`  |
| 1969   | Layout 1             | `c1ce3fc0a8e8`  |
| 1964   | Layout 1             | `c1ce3fc0a8e8`  |
| 1958   | Layout 1             | `c1ce3fc0a8e8`  |
| 1950   | Layout 1             | `c1ce3fc0a8e8`  |
| 1945   | Layout 1             | `c1ce3fc0a8e8`  |
| 1937   | Layout 1             | `c1ce3fc0a8e8`  |
| 1933   | Layout 1             | `c1ce3fc0a8e8`  |
| 1927   | Layout 1             | `c1ce3fc0a8e8`  |
| 1921   | Layout 1             | `c1ce3fc0a8e8`  |
| 1914   | Layout 1             | `c1ce3fc0a8e8`  |
| 1908   | Layout 1             | `c1ce3fc0a8e8`  |
| 1897   | Layout 1             | `c1ce3fc0a8e8`  |
| 1892   | Layout 1             | `c1ce3fc0a8e8`  |
| 1886   | Layout 1             | `c1ce3fc0a8e8`  |
| 1881   | Layout 1             | `c1ce3fc0a8e8`  |
| 1871   | Layout 1             | `c1ce3fc0a8e8`  |
| 1866   | Layout 1             | `c1ce3fc0a8e8`  |
| 1862   | Layout 1             | `c1ce3fc0a8e8`  |
| 1854   | Layout 1             | `c1ce3fc0a8e8`  |
| 1846   | Layout 1             | `c1ce3fc0a8e8`  |
| 1838   | Layout 1             | `c1ce3fc0a8e8`  |
| 1832   | Layout 1             | `c1ce3fc0a8e8`  |
| 1826   | Layout 1             | `c1ce3fc0a8e8`  |
| 1822   | Layout 1             | `c1ce3fc0a8e8`  |
| 1818   | Layout 1             | `c1ce3fc0a8e8`  |
| 1804   | Layout 1             | `c1ce3fc0a8e8`  |
| 1794   | Layout 1             | `c1ce3fc0a8e8`  |
| 1790   | Layout 1             | `c1ce3fc0a8e8`  |
| 1784   | Layout 1             | `c1ce3fc0a8e8`  |
| 1774   | Layout 1             | `c1ce3fc0a8e8`  |
| 1771   | Layout 1             | `c1ce3fc0a8e8`  |
| 1762   | Layout 1             | `c1ce3fc0a8e8`  |
| 1759   | Layout 1             | `c1ce3fc0a8e8`  |
| 1754   | Layout 1             | `c1ce3fc0a8e8`  |
| 1749   | Layout 1             | `c1ce3fc0a8e8`  |
| 1743   | Layout 1             | `c1ce3fc0a8e8`  |
| 1737   | Layout 1             | `c1ce3fc0a8e8`  |
| 1731   | Layout 1             | `c1ce3fc0a8e8`  |
| 1725   | Layout 1             | `c1ce3fc0a8e8`  |
| 1717   | Layout 1             | `c1ce3fc0a8e8`  |
| 1710   | Layout 1             | `c1ce3fc0a8e8`  |
| 1704   | Layout 1             | `c1ce3fc0a8e8`  |
| 1698   | Layout 1             | `c1ce3fc0a8e8`  |
| 1690   | Layout 1             | `c1ce3fc0a8e8`  |
| 1685   | Layout 1             | `c1ce3fc0a8e8`  |
| 1680   | Layout 1             | `c1ce3fc0a8e8`  |
| 1674   | Layout 1             | `c1ce3fc0a8e8`  |
| 1668   | Layout 1             | `c1ce3fc0a8e8`  |
| 1659   | Layout 1             | `c1ce3fc0a8e8`  |
| 1649   | Layout 1             | `c1ce3fc0a8e8`  |
| 1642   | Layout 1             | `c1ce3fc0a8e8`  |
| 1636   | Layout 1             | `c1ce3fc0a8e8`  |
| 1628   | Layout 1             | `c1ce3fc0a8e8`  |
| 1622   | Layout 1             | `c1ce3fc0a8e8`  |
| 1614   | Layout 1             | `c1ce3fc0a8e8`  |
| 1608   | Layout 1             | `c1ce3fc0a8e8`  |
| 1602   | Layout 1             | `c1ce3fc0a8e8`  |
| 1598   | Layout 1             | `c1ce3fc0a8e8`  |
| 1594   | Layout 1             | `c1ce3fc0a8e8`  |
| 1590   | Layout 1             | `c1ce3fc0a8e8`  |
| 1587   | Layout 1             | `c1ce3fc0a8e8`  |
| 1584   | Layout 1             | `c1ce3fc0a8e8`  |
| 1579   | Layout 1             | `c1ce3fc0a8e8`  |
| 1572   | Layout 1             | `c1ce3fc0a8e8`  |
| 1565   | Layout 1             | `c1ce3fc0a8e8`  |
| 1559   | Layout 1             | `c1ce3fc0a8e8`  |
| 1554   | Layout 1             | `c1ce3fc0a8e8`  |
| 1547   | Layout 1             | `c1ce3fc0a8e8`  |
| 1537   | Layout 1             | `c1ce3fc0a8e8`  |
| 1529   | Layout 1             | `c1ce3fc0a8e8`  |
| 1524   | Layout 1             | `c1ce3fc0a8e8`  |
| 1519   | Layout 1             | `c1ce3fc0a8e8`  |
| 1509   | Layout 1             | `c1ce3fc0a8e8`  |
| 1506   | Layout 1             | `c1ce3fc0a8e8`  |
| 1504   | Layout 1             | `c1ce3fc0a8e8`  |
| 1500   | Layout 1             | `c1ce3fc0a8e8`  |
| 1493   | Layout 1             | `c1ce3fc0a8e8`  |
| 1489   | Layout 1             | `c1ce3fc0a8e8`  |
| 1485   | Layout 1             | `c1ce3fc0a8e8`  |
| 1481   | Layout 1             | `c1ce3fc0a8e8`  |
| 1474   | Layout 1             | `c1ce3fc0a8e8`  |
| 1466   | Layout 1             | `c1ce3fc0a8e8`  |
| 1462   | Layout 1             | `c1ce3fc0a8e8`  |
| 1459   | Layout 1             | `c1ce3fc0a8e8`  |
| 1453   | Layout 1             | `c1ce3fc0a8e8`  |
| 1450   | Layout 1             | `c1ce3fc0a8e8`  |
| 1445   | Layout 1             | `c1ce3fc0a8e8`  |
| 1439   | Layout 1             | `c1ce3fc0a8e8`  |
| 1433   | Layout 1             | `c1ce3fc0a8e8`  |
| 1430   | Layout 1             | `c1ce3fc0a8e8`  |
| 1426   | Layout 1             | `c1ce3fc0a8e8`  |
| 1421   | Layout 1             | `c1ce3fc0a8e8`  |
| 1417   | Layout 1             | `c1ce3fc0a8e8`  |
| 1416   | Layout 1             | `c1ce3fc0a8e8`  |
| 1409   | Layout 1             | `c1ce3fc0a8e8`  |
| 1405   | Layout 1             | `c1ce3fc0a8e8`  |
| 1401   | Layout 1             | `c1ce3fc0a8e8`  |
| 1396   | Layout 1             | `c1ce3fc0a8e8`  |
| 1391   | Layout 1             | `c1ce3fc0a8e8`  |
| 1390   | Layout 1             | `c1ce3fc0a8e8`  |
| 1386   | Layout 1             | `c1ce3fc0a8e8`  |
| 1381   | Layout 1             | `c1ce3fc0a8e8`  |
| 1379   | Layout 1             | `c1ce3fc0a8e8`  |
| 1372   | Layout 1             | `c1ce3fc0a8e8`  |
| 1366   | Layout 1             | `c1ce3fc0a8e8`  |
| 1364   | Layout 1             | `c1ce3fc0a8e8`  |
| 1363   | Layout 1             | `c1ce3fc0a8e8`  |
| 1360   | Layout 1             | `c1ce3fc0a8e8`  |
| 1358   | Layout 1             | `c1ce3fc0a8e8`  |
| 1355   | Layout 1             | `c1ce3fc0a8e8`  |
| 1351   | Layout 1             | `c1ce3fc0a8e8`  |
| 1348   | Layout 1             | `c1ce3fc0a8e8`  |
| 1346   | Layout 1             | `c1ce3fc0a8e8`  |
| 1341   | No documented layout | `c1ce3fc0a8e8`  |
| 1340   | No documented layout | `c1ce3fc0a8e8`  |
| 1338   | No documented layout | `c1ce3fc0a8e8`  |
| 1335   | No documented layout | `c1ce3fc0a8e8`  |
| 1333   | No documented layout | `c1ce3fc0a8e8`  |
| 1329   | No documented layout | `c1ce3fc0a8e8`  |
| 1327   | No documented layout | `c1ce3fc0a8e8`  |
| 1324   | No documented layout | `c1ce3fc0a8e8`  |
| 1321   | No documented layout | `c1ce3fc0a8e8`  |
| 1319   | No documented layout | `c1ce3fc0a8e8`  |
| 1318   | No documented layout | `c1ce3fc0a8e8`  |
| 1316   | No documented layout | `c1ce3fc0a8e8`  |
| 1313   | No documented layout | `c1ce3fc0a8e8`  |
| 1311   | No documented layout | `c1ce3fc0a8e8`  |
| 1309   | No documented layout | `c1ce3fc0a8e8`  |
| 1304   | No documented layout | `c1ce3fc0a8e8`  |
| 1292   | No documented layout | `c1ce3fc0a8e8`  |
| 1286   | No documented layout | `c1ce3fc0a8e8`  |
| 1280   | No file              | `c1ce3fc0a8e8`  |
| 1276   | No file              | `c1ce3fc0a8e8`  |
| 1267   | No file              | `c1ce3fc0a8e8`  |
| 1261   | No file              | `c1ce3fc0a8e8`  |
| 1256   | No file              | `c1ce3fc0a8e8`  |
| 1250   | No file              | `c1ce3fc0a8e8`  |
| 1246   | No file              | `c1ce3fc0a8e8`  |
| 1239   | No file              | `c1ce3fc0a8e8`  |
| 1230   | No file              | `c1ce3fc0a8e8`  |
| 1226   | No file              | `c1ce3fc0a8e8`  |
| 1220   | No file              | `c1ce3fc0a8e8`  |
| 1217   | No file              | `c1ce3fc0a8e8`  |
| 1211   | No file              | `c1ce3fc0a8e8`  |
| 1210   | No file              | `c1ce3fc0a8e8`  |
| 1208   | No file              | `c1ce3fc0a8e8`  |
| 1203   | No file              | `c1ce3fc0a8e8`  |
| 1197   | No file              | `c1ce3fc0a8e8`  |
| 1194   | No file              | `c1ce3fc0a8e8`  |
| 1192   | No file              | `c1ce3fc0a8e8`  |
| 1187   | No file              | `c1ce3fc0a8e8`  |
| 1183   | No file              | `c1ce3fc0a8e8`  |
| 1177   | No file              | `c1ce3fc0a8e8`  |
| 1173   | No file              | `c1ce3fc0a8e8`  |
| 1167   | No file              | `c1ce3fc0a8e8`  |
| 1164   | No file              | `c1ce3fc0a8e8`  |
| 1156   | No file              | `c1ce3fc0a8e8`  |
| 1149   | No file              | `c1ce3fc0a8e8`  |
| 1144   | No file              | `c1ce3fc0a8e8`  |
| 1137   | No file              | `c1ce3fc0a8e8`  |
| 1132   | No file              | `c1ce3fc0a8e8`  |
| 1127   | No file              | `c1ce3fc0a8e8`  |
| 1122   | No file              | `c1ce3fc0a8e8`  |
| 1118   | No file              | `c1ce3fc0a8e8`  |
| 1114   | No file              | `c1ce3fc0a8e8`  |
| 1109   | No file              | `c1ce3fc0a8e8`  |
| 1102   | No file              | `c1ce3fc0a8e8`  |
| 1096   | No file              | `c1ce3fc0a8e8`  |
| 1088   | No file              | `c1ce3fc0a8e8`  |
| 1081   | No file              | `c1ce3fc0a8e8`  |
| 1076   | No file              | `c1ce3fc0a8e8`  |
| 1069   | No file              | `c1ce3fc0a8e8`  |
| 1064   | No file              | `c1ce3fc0a8e8`  |
| 1058   | No file              | `c1ce3fc0a8e8`  |
| 1051   | No file              | `c1ce3fc0a8e8`  |
| 1044   | No file              | `c1ce3fc0a8e8`  |
| 1036   | No file              | `c1ce3fc0a8e8`  |
| 1026   | No file              | `c1ce3fc0a8e8`  |
| 1016   | No file              | `c1ce3fc0a8e8`  |
| 1009   | No file              | `c1ce3fc0a8e8`  |
| 1005   | No file              | `c1ce3fc0a8e8`  |
| 1000   | No file              | `c1ce3fc0a8e8`  |
| 998    | No file              | `c1ce3fc0a8e8`  |
| 990    | No file              | `c1ce3fc0a8e8`  |
| 979    | No file              | `c1ce3fc0a8e8`  |
| 972    | No file              | `c1ce3fc0a8e8`  |
| 963    | No file              | `c1ce3fc0a8e8`  |
| 955    | No file              | `c1ce3fc0a8e8`  |
| 946    | No file              | `c1ce3fc0a8e8`  |
| 938    | No file              | `c1ce3fc0a8e8`  |
| 927    | No file              | `c1ce3fc0a8e8`  |
| 911    | No file              | `c1ce3fc0a8e8`  |
| 904    | No file              | `c1ce3fc0a8e8`  |
| 899    | No file              | `c1ce3fc0a8e8`  |
| 894    | No file              | `c1ce3fc0a8e8`  |
| 885    | No file              | `c1ce3fc0a8e8`  |
| 879    | No file              | `c1ce3fc0a8e8`  |
| 872    | No file              | `c1ce3fc0a8e8`  |
| 864    | No file              | `c1ce3fc0a8e8`  |
| 855    | No file              | `c1ce3fc0a8e8`  |
| 853    | No file              | `c1ce3fc0a8e8`  |
| 845    | No file              | `c1ce3fc0a8e8`  |
| 837    | No file              | `c1ce3fc0a8e8`  |
| 829    | No file              | `c1ce3fc0a8e8`  |
| 822    | No file              | `c1ce3fc0a8e8`  |
| 814    | No file              | `c1ce3fc0a8e8`  |
| 805    | No file              | `c1ce3fc0a8e8`  |
| 794    | No file              | `c1ce3fc0a8e8`  |
| 787    | No file              | `c1ce3fc0a8e8`  |
| 780    | No file              | `c1ce3fc0a8e8`  |
| 771    | No file              | `c1ce3fc0a8e8`  |
| 760    | No file              | `c1ce3fc0a8e8`  |
| 748    | No file              | `c1ce3fc0a8e8`  |
| 741    | No file              | `c1ce3fc0a8e8`  |
| 736    | No file              | `c1ce3fc0a8e8`  |
| 731    | No file              | `c1ce3fc0a8e8`  |
| 723    | No file              | `c1ce3fc0a8e8`  |
| 711    | No file              | `c1ce3fc0a8e8`  |
| 707    | No file              | `c1ce3fc0a8e8`  |
| 697    | No file              | `c1ce3fc0a8e8`  |
| 689    | No file              | `c1ce3fc0a8e8`  |
| 683    | No file              | `c1ce3fc0a8e8`  |
| 678    | No file              | `c1ce3fc0a8e8`  |
| 670    | No file              | `c1ce3fc0a8e8`  |
| 661    | No file              | `c1ce3fc0a8e8`  |
| 656    | No file              | `c1ce3fc0a8e8`  |
| 652    | No file              | `c1ce3fc0a8e8`  |
| 643    | No file              | `c1ce3fc0a8e8`  |
| 637    | No file              | `c1ce3fc0a8e8`  |
| 630    | No file              | `c1ce3fc0a8e8`  |
| 627    | No file              | `c1ce3fc0a8e8`  |
| 621    | No file              | `c1ce3fc0a8e8`  |
| 617    | No file              | `c1ce3fc0a8e8`  |
| 615    | No file              | `c1ce3fc0a8e8`  |
| 606    | No file              | `c1ce3fc0a8e8`  |
| 599    | No file              | `c1ce3fc0a8e8`  |
| 592    | No file              | `c1ce3fc0a8e8`  |
| 586    | No file              | `c1ce3fc0a8e8`  |
| 577    | No file              | `c1ce3fc0a8e8`  |
| 569    | No file              | `c1ce3fc0a8e8`  |
| 561    | No file              | `c1ce3fc0a8e8`  |
| 554    | No file              | `c1ce3fc0a8e8`  |
| 542    | No file              | `c1ce3fc0a8e8`  |
| 532    | No file              | `c1ce3fc0a8e8`  |
| 531    | No file              | `c1ce3fc0a8e8`  |
| 526    | No file              | `c1ce3fc0a8e8`  |
| 521    | No file              | `c1ce3fc0a8e8`  |
| 517    | No file              | `c1ce3fc0a8e8`  |
| 510    | No file              | `c1ce3fc0a8e8`  |
| 508    | No file              | `c1ce3fc0a8e8`  |
| 504    | No file              | `c1ce3fc0a8e8`  |
| 497    | No file              | `c1ce3fc0a8e8`  |
| 491    | No file              | `c1ce3fc0a8e8`  |
| 485    | No file              | `c1ce3fc0a8e8`  |
| 478    | No file              | `c1ce3fc0a8e8`  |
| 472    | No file              | `c1ce3fc0a8e8`  |
| 466    | No file              | `c1ce3fc0a8e8`  |
| 457    | No file              | `c1ce3fc0a8e8`  |
| 452    | No file              | `c1ce3fc0a8e8`  |
| 449    | No file              | `c1ce3fc0a8e8`  |
| 435    | No file              | `c1ce3fc0a8e8`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                       |
| --------------------- | -------- | ------------------------------------------ |
| `languagedata_en.loc` | Optional | NPC names (6), confession replies (54)     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                   | Field   | Notes                                     |
| ------- | ---------------------- | ------- | ----------------------------------------- |
| `+0x00` | u32                    | count   | Number of dialogue records (observed: 24) |
| `+0x04` | Dialogue Record[count] | records | See Dialogue Record                       |

### Dialogue Record (variable: 18 bytes + text)

| Offset      | Type   | Field           | Notes                                                                                                                        |
| ----------- | ------ | --------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `+0x00`     | u16    | npc_id          | NPC key                                                                                                                      |
| `+0x02`     | u32    | unknown_02      | Observed: 70 for 23 records, 35 for NPC 43408. Not the LOC type.                                                             |
| `+0x06`     | str16  | text            | Korean confession reply; the count is the number of visible UTF-16 code units                                                |
| `text+0x00` | u16[2] | unknown_tail_00 | Two trailing code units after `text`; observed values include `00 00 00 00`, `FF FF FF FF`, `00 00 41 DF`, and `00 00 3D E6` |

### `npcgiftdataoffset.dbss`

The 10-byte offset record layout of
[`npcgiftoffset.dbss`](npcgift_dbss.md#npcgiftoffsetdbss), but offsets point
into `npcgiftdata.dbss`. The `data_size` equals `12 + 2 x` the `text` count `+ 4`,
excluding the leading `npc_id`.

| Offset  | Type                 | Field   | Notes                                     |
| ------- | -------------------- | ------- | ----------------------------------------- |
| `+0x00` | u32                  | count   | Number of dialogue records (observed: 24) |
| `+0x04` | Offset Record[count] | records | See Offset Record                         |

### Offset Record (10 bytes)

| Offset  | Type | Field       | Notes                                                                     |
| ------- | ---- | ----------- | ------------------------------------------------------------------------- |
| `+0x00` | u16  | npc_id      | NPC key; matches the record's leading `npc_id`                            |
| `+0x02` | u32  | data_offset | Byte offset into `npcgiftdata.dbss`; points 2 bytes past the record start |
| `+0x06` | u16  | data_size   | Byte count after the leading `npc_id`                                     |
| `+0x08` | u16  | unknown_08  | Observed: 0                                                               |

## Notes

- `npcgift.dbss` and `npcgiftdata.dbss` share the same 24 NPC IDs and offset
  record order.
- The gift window Lua (`panel_dialog_npcgift_all_1`, `_2`) wires
  `btn_confession` to `HandleEventLUp_DialogNpcGift_All_Propose`, which calls
  `ToClient_proposeToNpc`; on `FromClient_SuccessProposeToNpc` it shows
  `LUA_SUCCESS_PROPOSETONPC`, and `panel_dialog_main_all_2` puts the reply in
  the dialog through `ToClient_getNpcProposeTalk`.
- Every reply answers a confession ("I am confused and shocked by your
  confession", Brego Williar).

## Open Questions

### Dialogue Tail Bytes

The two trailing UTF-16 code units after dialogue text (`unknown_tail_00`) carry values including `FF FF FF FF` and non-zero pairs; their purpose is unknown.

## In-Game Checks

### Confession Amity for `unknown_02`

Needs NPC (all):

- [Luwensley](https://bdocodex.com/us/npc/43408/)
- [Crio](https://bdocodex.com/us/npc/40012/)

`unknown_02` is 70 for 23 records and 35 for Luwensley (43408); earlier versions of this doc called it `unknown_param`. The gift window and dialog Lua read the reply text but have no getter for this value. Note the lowest Amity at which the Confess button works for each NPC, and the Amity change after the confession. If Luwensley accepts a confession from about half the Amity Crio needs, or the change after it is half as large, `unknown_02` is an Amity value for the confession; the same numbers for both NPCs rule that out.
