# `itemeffectchange.dbss` Format

## Purpose

The model an equipment mesh switches to at each enhancement level. A group
holds one item mesh key and one entry per level from `0` up, and each entry
names the `.pac` model the mesh uses at that level. Most groups keep the base
model for the low levels and switch to a `_01`/`_02` or `_ef1`/`_ef2` model at
the top levels.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes   | Records                          | Row bytes               |
| ------ | -------------- | ------- | ----------------------------- | ------- | -------------------------------- | ----------------------- |
| 2      | 3387 and later | 3483    | `itemeffectchange.dbss`       | 385,623 | 6,141 Entry, 596 Group           | 57 to 78, 62 on average |
| 2      | 3387 and later | 3483    | `itemeffectchangeoffset.dbss` | 78,464  | 6,141 Index Row, 596 Index Group | 12                      |
| 1      | 1276 to 3381   | 3381    | `itemeffectchange.dbss`       | 365,245 | 6,009 Entry, 584 Group           | 55 to 76, 60 on average |
| 1      | 1276 to 3381   | 3381    | `itemeffectchangeoffset.dbss` | 75,616  | 6,009 Index Row, 584 Index Group | 12                      |

| Layout | File                          | Known              | Unknown    |
| ------ | ----------------------------- | ------------------ | ---------- |
| 2      | `itemeffectchange.dbss`       | 385,623 B (100.0%) | 0 B (0.0%) |
| 2      | `itemeffectchangeoffset.dbss` | 78,464 B (100.0%)  | 0 B (0.0%) |
| 1      | `itemeffectchange.dbss`       | 365,245 B (100.0%) | 0 B (0.0%) |
| 1      | `itemeffectchangeoffset.dbss` | 75,616 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `a7e2d31efc31`  |
| 3482   | Layout 2 | `a7e2d31efc31`  |
| 3474   | Layout 2 | `a7e2d31efc31`  |
| 3473   | Layout 2 | `a7e2d31efc31`  |
| 3464   | Layout 2 | `a7e2d31efc31`  |
| 3458   | Layout 2 | `a7e2d31efc31`  |
| 3454   | Layout 2 | `a7e2d31efc31`  |
| 3444   | Layout 2 | `a7e2d31efc31`  |
| 3435   | Layout 2 | `a7e2d31efc31`  |
| 3426   | Layout 2 | `a7e2d31efc31`  |
| 3418   | Layout 2 | `a7e2d31efc31`  |
| 3412   | Layout 2 | `a7e2d31efc31`  |
| 3402   | Layout 2 | `a7e2d31efc31`  |
| 3396   | Layout 2 | `a7e2d31efc31`  |
| 3387   | Layout 2 | `a7e2d31efc31`  |
| 3381   | Layout 1 | `a7e2d31efc31`  |
| 3373   | Layout 1 | `a7e2d31efc31`  |
| 3364   | Layout 1 | `a7e2d31efc31`  |
| 3356   | Layout 1 | `a7e2d31efc31`  |
| 3349   | Layout 1 | `a7e2d31efc31`  |
| 3342   | Layout 1 | `a7e2d31efc31`  |
| 3335   | Layout 1 | `a7e2d31efc31`  |
| 3326   | Layout 1 | `a7e2d31efc31`  |
| 3321   | Layout 1 | `a7e2d31efc31`  |
| 3314   | Layout 1 | `a7e2d31efc31`  |
| 3303   | Layout 1 | `a7e2d31efc31`  |
| 3302   | Layout 1 | `a7e2d31efc31`  |
| 3293   | Layout 1 | `a7e2d31efc31`  |
| 3283   | Layout 1 | `a7e2d31efc31`  |
| 3275   | Layout 1 | `a7e2d31efc31`  |
| 3267   | Layout 1 | `a7e2d31efc31`  |
| 3258   | Layout 1 | `a7e2d31efc31`  |
| 3251   | Layout 1 | `a7e2d31efc31`  |
| 3242   | Layout 1 | `a7e2d31efc31`  |
| 3235   | Layout 1 | `a7e2d31efc31`  |
| 3229   | Layout 1 | `a7e2d31efc31`  |
| 3212   | Layout 1 | `a7e2d31efc31`  |
| 3203   | Layout 1 | `a7e2d31efc31`  |
| 3193   | Layout 1 | `a7e2d31efc31`  |
| 3186   | Layout 1 | `a7e2d31efc31`  |
| 3177   | Layout 1 | `a7e2d31efc31`  |
| 3169   | Layout 1 | `a7e2d31efc31`  |
| 3158   | Layout 1 | `a7e2d31efc31`  |
| 3151   | Layout 1 | `a7e2d31efc31`  |
| 3144   | Layout 1 | `a7e2d31efc31`  |
| 3133   | Layout 1 | `a7e2d31efc31`  |
| 3125   | Layout 1 | `a7e2d31efc31`  |
| 3118   | Layout 1 | `a7e2d31efc31`  |
| 3111   | Layout 1 | `a7e2d31efc31`  |
| 3103   | Layout 1 | `a7e2d31efc31`  |
| 3095   | Layout 1 | `a7e2d31efc31`  |
| 3086   | Layout 1 | `a7e2d31efc31`  |
| 3072   | Layout 1 | `a7e2d31efc31`  |
| 3062   | Layout 1 | `a7e2d31efc31`  |
| 3052   | Layout 1 | `a7e2d31efc31`  |
| 3045   | Layout 1 | `a7e2d31efc31`  |
| 3037   | Layout 1 | `a7e2d31efc31`  |
| 3030   | Layout 1 | `a7e2d31efc31`  |
| 3021   | Layout 1 | `a7e2d31efc31`  |
| 3012   | Layout 1 | `a7e2d31efc31`  |
| 3002   | Layout 1 | `a7e2d31efc31`  |
| 2995   | Layout 1 | `a7e2d31efc31`  |
| 2987   | Layout 1 | `a7e2d31efc31`  |
| 2978   | Layout 1 | `a7e2d31efc31`  |
| 2970   | Layout 1 | `a7e2d31efc31`  |
| 2959   | Layout 1 | `a7e2d31efc31`  |
| 2951   | Layout 1 | `a7e2d31efc31`  |
| 2942   | Layout 1 | `a7e2d31efc31`  |
| 2935   | Layout 1 | `a7e2d31efc31`  |
| 2932   | Layout 1 | `a7e2d31efc31`  |
| 2923   | Layout 1 | `a7e2d31efc31`  |
| 2919   | Layout 1 | `a7e2d31efc31`  |
| 2907   | Layout 1 | `a7e2d31efc31`  |
| 2900   | Layout 1 | `a7e2d31efc31`  |
| 2891   | Layout 1 | `a7e2d31efc31`  |
| 2882   | Layout 1 | `a7e2d31efc31`  |
| 2872   | Layout 1 | `a7e2d31efc31`  |
| 2863   | Layout 1 | `a7e2d31efc31`  |
| 2855   | Layout 1 | `a7e2d31efc31`  |
| 2849   | Layout 1 | `a7e2d31efc31`  |
| 2844   | Layout 1 | `a7e2d31efc31`  |
| 2834   | Layout 1 | `a7e2d31efc31`  |
| 2825   | Layout 1 | `a7e2d31efc31`  |
| 2819   | Layout 1 | `a7e2d31efc31`  |
| 2811   | Layout 1 | `a7e2d31efc31`  |
| 2803   | Layout 1 | `a7e2d31efc31`  |
| 2794   | Layout 1 | `a7e2d31efc31`  |
| 2783   | Layout 1 | `a7e2d31efc31`  |
| 2774   | Layout 1 | `a7e2d31efc31`  |
| 2765   | Layout 1 | `a7e2d31efc31`  |
| 2756   | Layout 1 | `a7e2d31efc31`  |
| 2750   | Layout 1 | `a7e2d31efc31`  |
| 2743   | Layout 1 | `a7e2d31efc31`  |
| 2736   | Layout 1 | `a7e2d31efc31`  |
| 2726   | Layout 1 | `a7e2d31efc31`  |
| 2717   | Layout 1 | `a7e2d31efc31`  |
| 2709   | Layout 1 | `a7e2d31efc31`  |
| 2703   | Layout 1 | `a7e2d31efc31`  |
| 2695   | Layout 1 | `a7e2d31efc31`  |
| 2684   | Layout 1 | `a7e2d31efc31`  |
| 2672   | Layout 1 | `a7e2d31efc31`  |
| 2665   | Layout 1 | `a7e2d31efc31`  |
| 2657   | Layout 1 | `a7e2d31efc31`  |
| 2649   | Layout 1 | `a7e2d31efc31`  |
| 2644   | Layout 1 | `a7e2d31efc31`  |
| 2637   | Layout 1 | `a7e2d31efc31`  |
| 2629   | Layout 1 | `a7e2d31efc31`  |
| 2619   | Layout 1 | `a7e2d31efc31`  |
| 2612   | Layout 1 | `a7e2d31efc31`  |
| 2606   | Layout 1 | `a7e2d31efc31`  |
| 2602   | Layout 1 | `a7e2d31efc31`  |
| 2601   | Layout 1 | `a7e2d31efc31`  |
| 2592   | Layout 1 | `a7e2d31efc31`  |
| 2583   | Layout 1 | `a7e2d31efc31`  |
| 2575   | Layout 1 | `a7e2d31efc31`  |
| 2567   | Layout 1 | `a7e2d31efc31`  |
| 2560   | Layout 1 | `a7e2d31efc31`  |
| 2553   | Layout 1 | `a7e2d31efc31`  |
| 2545   | Layout 1 | `a7e2d31efc31`  |
| 2538   | Layout 1 | `a7e2d31efc31`  |
| 2529   | Layout 1 | `a7e2d31efc31`  |
| 2519   | Layout 1 | `a7e2d31efc31`  |
| 2513   | Layout 1 | `a7e2d31efc31`  |
| 2510   | Layout 1 | `a7e2d31efc31`  |
| 2507   | Layout 1 | `a7e2d31efc31`  |
| 2503   | Layout 1 | `a7e2d31efc31`  |
| 2498   | Layout 1 | `a7e2d31efc31`  |
| 2492   | Layout 1 | `a7e2d31efc31`  |
| 2487   | Layout 1 | `a7e2d31efc31`  |
| 2480   | Layout 1 | `a7e2d31efc31`  |
| 2474   | Layout 1 | `a7e2d31efc31`  |
| 2468   | Layout 1 | `a7e2d31efc31`  |
| 2460   | Layout 1 | `a7e2d31efc31`  |
| 2453   | Layout 1 | `a7e2d31efc31`  |
| 2444   | Layout 1 | `a7e2d31efc31`  |
| 2438   | Layout 1 | `a7e2d31efc31`  |
| 2434   | Layout 1 | `a7e2d31efc31`  |
| 2429   | Layout 1 | `a7e2d31efc31`  |
| 2421   | Layout 1 | `a7e2d31efc31`  |
| 2414   | Layout 1 | `a7e2d31efc31`  |
| 2407   | Layout 1 | `a7e2d31efc31`  |
| 2401   | Layout 1 | `a7e2d31efc31`  |
| 2397   | Layout 1 | `a7e2d31efc31`  |
| 2393   | Layout 1 | `a7e2d31efc31`  |
| 2384   | Layout 1 | `a7e2d31efc31`  |
| 2378   | Layout 1 | `a7e2d31efc31`  |
| 2372   | Layout 1 | `a7e2d31efc31`  |
| 2358   | Layout 1 | `a7e2d31efc31`  |
| 2352   | Layout 1 | `a7e2d31efc31`  |
| 2347   | Layout 1 | `a7e2d31efc31`  |
| 2343   | Layout 1 | `a7e2d31efc31`  |
| 2335   | Layout 1 | `a7e2d31efc31`  |
| 2327   | Layout 1 | `a7e2d31efc31`  |
| 2324   | Layout 1 | `a7e2d31efc31`  |
| 2319   | Layout 1 | `a7e2d31efc31`  |
| 2313   | Layout 1 | `a7e2d31efc31`  |
| 2308   | Layout 1 | `a7e2d31efc31`  |
| 2302   | Layout 1 | `a7e2d31efc31`  |
| 2295   | Layout 1 | `a7e2d31efc31`  |
| 2290   | Layout 1 | `a7e2d31efc31`  |
| 2284   | Layout 1 | `a7e2d31efc31`  |
| 2276   | Layout 1 | `a7e2d31efc31`  |
| 2269   | Layout 1 | `a7e2d31efc31`  |
| 2259   | Layout 1 | `a7e2d31efc31`  |
| 2250   | Layout 1 | `a7e2d31efc31`  |
| 2243   | Layout 1 | `a7e2d31efc31`  |
| 2235   | Layout 1 | `a7e2d31efc31`  |
| 2229   | Layout 1 | `a7e2d31efc31`  |
| 2224   | Layout 1 | `a7e2d31efc31`  |
| 2218   | Layout 1 | `a7e2d31efc31`  |
| 2215   | Layout 1 | `a7e2d31efc31`  |
| 2207   | Layout 1 | `a7e2d31efc31`  |
| 2203   | Layout 1 | `a7e2d31efc31`  |
| 2196   | Layout 1 | `a7e2d31efc31`  |
| 2192   | Layout 1 | `a7e2d31efc31`  |
| 2189   | Layout 1 | `a7e2d31efc31`  |
| 2183   | Layout 1 | `a7e2d31efc31`  |
| 2179   | Layout 1 | `a7e2d31efc31`  |
| 2171   | Layout 1 | `a7e2d31efc31`  |
| 2163   | Layout 1 | `a7e2d31efc31`  |
| 2156   | Layout 1 | `a7e2d31efc31`  |
| 2151   | Layout 1 | `a7e2d31efc31`  |
| 2147   | Layout 1 | `a7e2d31efc31`  |
| 2142   | Layout 1 | `a7e2d31efc31`  |
| 2138   | Layout 1 | `a7e2d31efc31`  |
| 2134   | Layout 1 | `a7e2d31efc31`  |
| 2130   | Layout 1 | `a7e2d31efc31`  |
| 2122   | Layout 1 | `a7e2d31efc31`  |
| 2107   | Layout 1 | `a7e2d31efc31`  |
| 2098   | Layout 1 | `a7e2d31efc31`  |
| 2089   | Layout 1 | `a7e2d31efc31`  |
| 2081   | Layout 1 | `a7e2d31efc31`  |
| 2073   | Layout 1 | `a7e2d31efc31`  |
| 2067   | Layout 1 | `a7e2d31efc31`  |
| 2063   | Layout 1 | `a7e2d31efc31`  |
| 2059   | Layout 1 | `a7e2d31efc31`  |
| 2052   | Layout 1 | `a7e2d31efc31`  |
| 2044   | Layout 1 | `a7e2d31efc31`  |
| 2039   | Layout 1 | `a7e2d31efc31`  |
| 2032   | Layout 1 | `a7e2d31efc31`  |
| 2025   | Layout 1 | `a7e2d31efc31`  |
| 2011   | Layout 1 | `a7e2d31efc31`  |
| 2005   | Layout 1 | `a7e2d31efc31`  |
| 2000   | Layout 1 | `a7e2d31efc31`  |
| 1996   | Layout 1 | `a7e2d31efc31`  |
| 1991   | Layout 1 | `a7e2d31efc31`  |
| 1985   | Layout 1 | `a7e2d31efc31`  |
| 1980   | Layout 1 | `a7e2d31efc31`  |
| 1969   | Layout 1 | `a7e2d31efc31`  |
| 1964   | Layout 1 | `a7e2d31efc31`  |
| 1958   | Layout 1 | `a7e2d31efc31`  |
| 1950   | Layout 1 | `a7e2d31efc31`  |
| 1945   | Layout 1 | `a7e2d31efc31`  |
| 1937   | Layout 1 | `a7e2d31efc31`  |
| 1933   | Layout 1 | `a7e2d31efc31`  |
| 1927   | Layout 1 | `a7e2d31efc31`  |
| 1921   | Layout 1 | `a7e2d31efc31`  |
| 1914   | Layout 1 | `a7e2d31efc31`  |
| 1908   | Layout 1 | `a7e2d31efc31`  |
| 1897   | Layout 1 | `a7e2d31efc31`  |
| 1892   | Layout 1 | `a7e2d31efc31`  |
| 1886   | Layout 1 | `a7e2d31efc31`  |
| 1881   | Layout 1 | `a7e2d31efc31`  |
| 1871   | Layout 1 | `a7e2d31efc31`  |
| 1866   | Layout 1 | `a7e2d31efc31`  |
| 1862   | Layout 1 | `a7e2d31efc31`  |
| 1854   | Layout 1 | `a7e2d31efc31`  |
| 1846   | Layout 1 | `a7e2d31efc31`  |
| 1838   | Layout 1 | `a7e2d31efc31`  |
| 1832   | Layout 1 | `a7e2d31efc31`  |
| 1826   | Layout 1 | `a7e2d31efc31`  |
| 1822   | Layout 1 | `a7e2d31efc31`  |
| 1818   | Layout 1 | `a7e2d31efc31`  |
| 1804   | Layout 1 | `a7e2d31efc31`  |
| 1794   | Layout 1 | `a7e2d31efc31`  |
| 1790   | Layout 1 | `a7e2d31efc31`  |
| 1784   | Layout 1 | `a7e2d31efc31`  |
| 1774   | Layout 1 | `a7e2d31efc31`  |
| 1771   | Layout 1 | `a7e2d31efc31`  |
| 1762   | Layout 1 | `a7e2d31efc31`  |
| 1759   | Layout 1 | `a7e2d31efc31`  |
| 1754   | Layout 1 | `a7e2d31efc31`  |
| 1749   | Layout 1 | `a7e2d31efc31`  |
| 1743   | Layout 1 | `a7e2d31efc31`  |
| 1737   | Layout 1 | `a7e2d31efc31`  |
| 1731   | Layout 1 | `a7e2d31efc31`  |
| 1725   | Layout 1 | `a7e2d31efc31`  |
| 1717   | Layout 1 | `a7e2d31efc31`  |
| 1710   | Layout 1 | `a7e2d31efc31`  |
| 1704   | Layout 1 | `a7e2d31efc31`  |
| 1698   | Layout 1 | `a7e2d31efc31`  |
| 1690   | Layout 1 | `a7e2d31efc31`  |
| 1685   | Layout 1 | `a7e2d31efc31`  |
| 1680   | Layout 1 | `a7e2d31efc31`  |
| 1674   | Layout 1 | `a7e2d31efc31`  |
| 1668   | Layout 1 | `a7e2d31efc31`  |
| 1659   | Layout 1 | `a7e2d31efc31`  |
| 1649   | Layout 1 | `a7e2d31efc31`  |
| 1642   | Layout 1 | `a7e2d31efc31`  |
| 1636   | Layout 1 | `a7e2d31efc31`  |
| 1628   | Layout 1 | `a7e2d31efc31`  |
| 1622   | Layout 1 | `a7e2d31efc31`  |
| 1614   | Layout 1 | `a7e2d31efc31`  |
| 1608   | Layout 1 | `a7e2d31efc31`  |
| 1602   | Layout 1 | `a7e2d31efc31`  |
| 1598   | Layout 1 | `a7e2d31efc31`  |
| 1594   | Layout 1 | `a7e2d31efc31`  |
| 1590   | Layout 1 | `a7e2d31efc31`  |
| 1587   | Layout 1 | `a7e2d31efc31`  |
| 1584   | Layout 1 | `a7e2d31efc31`  |
| 1579   | Layout 1 | `a7e2d31efc31`  |
| 1572   | Layout 1 | `a7e2d31efc31`  |
| 1565   | Layout 1 | `a7e2d31efc31`  |
| 1559   | Layout 1 | `a7e2d31efc31`  |
| 1554   | Layout 1 | `a7e2d31efc31`  |
| 1547   | Layout 1 | `a7e2d31efc31`  |
| 1537   | Layout 1 | `a7e2d31efc31`  |
| 1529   | Layout 1 | `a7e2d31efc31`  |
| 1524   | Layout 1 | `a7e2d31efc31`  |
| 1519   | Layout 1 | `a7e2d31efc31`  |
| 1509   | Layout 1 | `a7e2d31efc31`  |
| 1506   | Layout 1 | `a7e2d31efc31`  |
| 1504   | Layout 1 | `a7e2d31efc31`  |
| 1500   | Layout 1 | `a7e2d31efc31`  |
| 1493   | Layout 1 | `a7e2d31efc31`  |
| 1489   | Layout 1 | `a7e2d31efc31`  |
| 1485   | Layout 1 | `a7e2d31efc31`  |
| 1481   | Layout 1 | `a7e2d31efc31`  |
| 1474   | Layout 1 | `a7e2d31efc31`  |
| 1466   | Layout 1 | `a7e2d31efc31`  |
| 1462   | Layout 1 | `a7e2d31efc31`  |
| 1459   | Layout 1 | `a7e2d31efc31`  |
| 1453   | Layout 1 | `a7e2d31efc31`  |
| 1450   | Layout 1 | `a7e2d31efc31`  |
| 1445   | Layout 1 | `a7e2d31efc31`  |
| 1439   | Layout 1 | `a7e2d31efc31`  |
| 1433   | Layout 1 | `a7e2d31efc31`  |
| 1430   | Layout 1 | `a7e2d31efc31`  |
| 1426   | Layout 1 | `a7e2d31efc31`  |
| 1421   | Layout 1 | `a7e2d31efc31`  |
| 1417   | Layout 1 | `a7e2d31efc31`  |
| 1416   | Layout 1 | `a7e2d31efc31`  |
| 1409   | Layout 1 | `a7e2d31efc31`  |
| 1405   | Layout 1 | `a7e2d31efc31`  |
| 1401   | Layout 1 | `a7e2d31efc31`  |
| 1396   | Layout 1 | `a7e2d31efc31`  |
| 1391   | Layout 1 | `a7e2d31efc31`  |
| 1390   | Layout 1 | `a7e2d31efc31`  |
| 1386   | Layout 1 | `a7e2d31efc31`  |
| 1381   | Layout 1 | `a7e2d31efc31`  |
| 1379   | Layout 1 | `a7e2d31efc31`  |
| 1372   | Layout 1 | `a7e2d31efc31`  |
| 1366   | Layout 1 | `a7e2d31efc31`  |
| 1364   | Layout 1 | `a7e2d31efc31`  |
| 1363   | Layout 1 | `a7e2d31efc31`  |
| 1360   | Layout 1 | `a7e2d31efc31`  |
| 1358   | Layout 1 | `a7e2d31efc31`  |
| 1355   | Layout 1 | `a7e2d31efc31`  |
| 1351   | Layout 1 | `a7e2d31efc31`  |
| 1348   | Layout 1 | `a7e2d31efc31`  |
| 1346   | Layout 1 | `a7e2d31efc31`  |
| 1341   | Layout 1 | `a7e2d31efc31`  |
| 1340   | Layout 1 | `a7e2d31efc31`  |
| 1338   | Layout 1 | `a7e2d31efc31`  |
| 1335   | Layout 1 | `a7e2d31efc31`  |
| 1333   | Layout 1 | `a7e2d31efc31`  |
| 1329   | Layout 1 | `a7e2d31efc31`  |
| 1327   | Layout 1 | `a7e2d31efc31`  |
| 1324   | Layout 1 | `a7e2d31efc31`  |
| 1321   | Layout 1 | `a7e2d31efc31`  |
| 1319   | Layout 1 | `a7e2d31efc31`  |
| 1318   | Layout 1 | `a7e2d31efc31`  |
| 1316   | Layout 1 | `a7e2d31efc31`  |
| 1313   | Layout 1 | `a7e2d31efc31`  |
| 1311   | Layout 1 | `a7e2d31efc31`  |
| 1309   | Layout 1 | `a7e2d31efc31`  |
| 1304   | Layout 1 | `a7e2d31efc31`  |
| 1292   | Layout 1 | `a7e2d31efc31`  |
| 1286   | Layout 1 | `a7e2d31efc31`  |
| 1280   | Layout 1 | `a7e2d31efc31`  |
| 1276   | Layout 1 | `a7e2d31efc31`  |
| 1267   | No file  | `a7e2d31efc31`  |
| 1261   | No file  | `a7e2d31efc31`  |
| 1256   | No file  | `a7e2d31efc31`  |
| 1250   | No file  | `a7e2d31efc31`  |
| 1246   | No file  | `a7e2d31efc31`  |
| 1239   | No file  | `a7e2d31efc31`  |
| 1230   | No file  | `a7e2d31efc31`  |
| 1226   | No file  | `a7e2d31efc31`  |
| 1220   | No file  | `a7e2d31efc31`  |
| 1217   | No file  | `a7e2d31efc31`  |
| 1211   | No file  | `a7e2d31efc31`  |
| 1210   | No file  | `a7e2d31efc31`  |
| 1208   | No file  | `a7e2d31efc31`  |
| 1203   | No file  | `a7e2d31efc31`  |
| 1197   | No file  | `a7e2d31efc31`  |
| 1194   | No file  | `a7e2d31efc31`  |
| 1192   | No file  | `a7e2d31efc31`  |
| 1187   | No file  | `a7e2d31efc31`  |
| 1183   | No file  | `a7e2d31efc31`  |
| 1177   | No file  | `a7e2d31efc31`  |
| 1173   | No file  | `a7e2d31efc31`  |
| 1167   | No file  | `a7e2d31efc31`  |
| 1164   | No file  | `a7e2d31efc31`  |
| 1156   | No file  | `a7e2d31efc31`  |
| 1149   | No file  | `a7e2d31efc31`  |
| 1144   | No file  | `a7e2d31efc31`  |
| 1137   | No file  | `a7e2d31efc31`  |
| 1132   | No file  | `a7e2d31efc31`  |
| 1127   | No file  | `a7e2d31efc31`  |
| 1122   | No file  | `a7e2d31efc31`  |
| 1118   | No file  | `a7e2d31efc31`  |
| 1114   | No file  | `a7e2d31efc31`  |
| 1109   | No file  | `a7e2d31efc31`  |
| 1102   | No file  | `a7e2d31efc31`  |
| 1096   | No file  | `a7e2d31efc31`  |
| 1088   | No file  | `a7e2d31efc31`  |
| 1081   | No file  | `a7e2d31efc31`  |
| 1076   | No file  | `a7e2d31efc31`  |
| 1069   | No file  | `a7e2d31efc31`  |
| 1064   | No file  | `a7e2d31efc31`  |
| 1058   | No file  | `a7e2d31efc31`  |
| 1051   | No file  | `a7e2d31efc31`  |
| 1044   | No file  | `a7e2d31efc31`  |
| 1036   | No file  | `a7e2d31efc31`  |
| 1026   | No file  | `a7e2d31efc31`  |
| 1016   | No file  | `a7e2d31efc31`  |
| 1009   | No file  | `a7e2d31efc31`  |
| 1005   | No file  | `a7e2d31efc31`  |
| 1000   | No file  | `a7e2d31efc31`  |
| 998    | No file  | `a7e2d31efc31`  |
| 990    | No file  | `a7e2d31efc31`  |
| 979    | No file  | `a7e2d31efc31`  |
| 972    | No file  | `a7e2d31efc31`  |
| 963    | No file  | `a7e2d31efc31`  |
| 955    | No file  | `a7e2d31efc31`  |
| 946    | No file  | `a7e2d31efc31`  |
| 938    | No file  | `a7e2d31efc31`  |
| 927    | No file  | `a7e2d31efc31`  |
| 911    | No file  | `a7e2d31efc31`  |
| 904    | No file  | `a7e2d31efc31`  |
| 899    | No file  | `a7e2d31efc31`  |
| 894    | No file  | `a7e2d31efc31`  |
| 885    | No file  | `a7e2d31efc31`  |
| 879    | No file  | `a7e2d31efc31`  |
| 872    | No file  | `a7e2d31efc31`  |
| 864    | No file  | `a7e2d31efc31`  |
| 855    | No file  | `a7e2d31efc31`  |
| 853    | No file  | `a7e2d31efc31`  |
| 845    | No file  | `a7e2d31efc31`  |
| 837    | No file  | `a7e2d31efc31`  |
| 829    | No file  | `a7e2d31efc31`  |
| 822    | No file  | `a7e2d31efc31`  |
| 814    | No file  | `a7e2d31efc31`  |
| 805    | No file  | `a7e2d31efc31`  |
| 794    | No file  | `a7e2d31efc31`  |
| 787    | No file  | `a7e2d31efc31`  |
| 780    | No file  | `a7e2d31efc31`  |
| 771    | No file  | `a7e2d31efc31`  |
| 760    | No file  | `a7e2d31efc31`  |
| 748    | No file  | `a7e2d31efc31`  |
| 741    | No file  | `a7e2d31efc31`  |
| 736    | No file  | `a7e2d31efc31`  |
| 731    | No file  | `a7e2d31efc31`  |
| 723    | No file  | `a7e2d31efc31`  |
| 711    | No file  | `a7e2d31efc31`  |
| 707    | No file  | `a7e2d31efc31`  |
| 697    | No file  | `a7e2d31efc31`  |
| 689    | No file  | `a7e2d31efc31`  |
| 683    | No file  | `a7e2d31efc31`  |
| 678    | No file  | `a7e2d31efc31`  |
| 670    | No file  | `a7e2d31efc31`  |
| 661    | No file  | `a7e2d31efc31`  |
| 656    | No file  | `a7e2d31efc31`  |
| 652    | No file  | `a7e2d31efc31`  |
| 643    | No file  | `a7e2d31efc31`  |
| 637    | No file  | `a7e2d31efc31`  |
| 630    | No file  | `a7e2d31efc31`  |
| 627    | No file  | `a7e2d31efc31`  |
| 621    | No file  | `a7e2d31efc31`  |
| 617    | No file  | `a7e2d31efc31`  |
| 615    | No file  | `a7e2d31efc31`  |
| 606    | No file  | `a7e2d31efc31`  |
| 599    | No file  | `a7e2d31efc31`  |
| 592    | No file  | `a7e2d31efc31`  |
| 586    | No file  | `a7e2d31efc31`  |
| 577    | No file  | `a7e2d31efc31`  |
| 569    | No file  | `a7e2d31efc31`  |
| 561    | No file  | `a7e2d31efc31`  |
| 554    | No file  | `a7e2d31efc31`  |
| 542    | No file  | `a7e2d31efc31`  |
| 532    | No file  | `a7e2d31efc31`  |
| 531    | No file  | `a7e2d31efc31`  |
| 526    | No file  | `a7e2d31efc31`  |
| 521    | No file  | `a7e2d31efc31`  |
| 517    | No file  | `a7e2d31efc31`  |
| 510    | No file  | `a7e2d31efc31`  |
| 508    | No file  | `a7e2d31efc31`  |
| 504    | No file  | `a7e2d31efc31`  |
| 497    | No file  | `a7e2d31efc31`  |
| 491    | No file  | `a7e2d31efc31`  |
| 485    | No file  | `a7e2d31efc31`  |
| 478    | No file  | `a7e2d31efc31`  |
| 472    | No file  | `a7e2d31efc31`  |
| 466    | No file  | `a7e2d31efc31`  |
| 457    | No file  | `a7e2d31efc31`  |
| 452    | No file  | `a7e2d31efc31`  |
| 449    | No file  | `a7e2d31efc31`  |
| 435    | No file  | `a7e2d31efc31`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                   |
| ----------------------------- | -------- | ------------------------------------------------------ |
| `itemeffectchangeoffset.dbss` | No       | Index of every entry by mesh key and level; the handler reads the groups in file order and does not need it |
| `itemenchant.dbss`            | No       | The items that wear each mesh, for the Items column; the handler reads them from the `MESH_KEY_ITEMS` lookup index, not as a companion |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A group count, then the groups back to
back; the file ends after the last group.

| Offset  | Type               | Field       | Notes                                   |
| ------- | ------------------ | ----------- | --------------------------------------- |
| `+0x00` | u32                | group_count | One group per mesh key                  |
| `+0x04` | Group[group_count] | groups      | See Group                               |

### Group (variable: 4 bytes + entries)

| Offset  | Type                 | Field       | Notes                                              |
| ------- | -------------------- | ----------- | -------------------------------------------------- |
| `+0x00` | u32                  | entry_count | `6`, `11` or `21` on client 3482; never `0`        |
| `+0x04` | Entry[entry_count]   | entries     | Levels `0` to `entry_count - 1` in order; see Entry |

### Entry (variable: 13 bytes + mesh file)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | mesh_key      | Item mesh key; the same in every entry of a group, unique per group    |
| `+0x04` | u8   | enchant_level | Enhancement level, equal to the entry's index in its group            |
| `+0x05` | str8 | mesh_file     | Lowercase `.pac` path under `character/model/`, e.g. `1_pc/1_phm/weapon/1_onehandsword/phm_01_ohs_0017_r.pac` |

### `itemeffectchangeoffset.dbss`

The same grouped walk with the mesh key moved into the group head. The groups
are in another order than in the main file, so a reader matches them by
`offset`, not by position.

| Offset  | Type                     | Field       | Notes                                |
| ------- | ------------------------ | ----------- | ------------------------------------ |
| `+0x00` | u32                      | group_count | Equals the main file's `group_count` |
| `+0x04` | Index Group[group_count] | groups      | See Index Group                      |

### Index Group (variable: 8 bytes + rows)

| Offset  | Type                 | Field     | Notes                                          |
| ------- | -------------------- | --------- | ---------------------------------------------- |
| `+0x00` | u32                  | row_count | Equals the `entry_count` of the main group with this mesh key |
| `+0x04` | u32                  | mesh_key  | The mesh key of every entry the rows point at  |
| `+0x08` | Index Row[row_count] | rows      | See Index Row                                  |

### Index Row (12 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | enchant_level | The entry's `enchant_level`                                  |
| `+0x04` | u32  | offset        | Start of the entry in `itemeffectchange.dbss`, at its `mesh_key` |
| `+0x08` | u32  | size          | Entry size: 13 plus the `mesh_file` length                   |

On client 3482 every one of the 6,141 index rows points at the main entry
with its mesh key and level and gives that entry's size, and the rows cover
every entry once. The first row of a group points 4 bytes past the main
group's start, after its `entry_count`.

## Layout 1

The mesh key is a u16 in both files. Only the Entry and the Index Group
differ from Layout 2.

### Entry (variable: 11 bytes + mesh file)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | mesh_key      | Item mesh key, the low 16 bits of the sheet's key (see Field Names) |
| `+0x02` | u8   | enchant_level | Enhancement level, equal to the entry's index in its group  |
| `+0x03` | str8 | mesh_file     | Lowercase `.pac` path                                       |

### Index Group (variable: 6 bytes + rows)

| Offset  | Type                 | Field     | Notes                                          |
| ------- | -------------------- | --------- | ---------------------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main group's `entry_count`          |
| `+0x04` | u16                  | mesh_key  | The mesh key of every entry the rows point at  |
| `+0x06` | Index Row[row_count] | rows      | See Index Row; `size` is 11 plus the `mesh_file` length |

## Field Names

The names come from the `EffectsChange` sheet of a private server's
`DataSheets.bexcel` on client 1784 (columns `Index`, `EnchantLevel`,
`UseMeshFile`, `IsDevelopingContents`). The sheet's `UseMeshFile` keeps its
capitals; the files store it lowercase.

| Field           | Column         | Match                                                                 |
| --------------- | -------------- | --------------------------------------------------------------------- |
| `mesh_key`      | `Index`        | Key of each sheet row                                                 |
| `enchant_level` | `EnchantLevel` | Second key of each sheet row                                          |
| `mesh_file`     | `UseMeshFile`  | 2,205 of the 2,205 (key, level) pairs the sheet shares with client 3482; 1,083 of 1,083 on client 1784, with the sheet key cut to 16 bits |

- `Index` is an item mesh key: all 215 keys of the sheet are an `Index` of
  the same workbook's `Item_Mesh_Table`, and they are 215 of the 220 rows
  there with `EffectsChangeType` `1`. On 142 of the 215 the level `0` model
  is the mesh table's own `UseMeshFile`.
- The sheet's keys reach 336,075, past 16 bits. The client 1784 file stores
  336000 as 8320 (`0x52080` cut to `0x2080`), and no two sheet keys share
  their low 16 bits, so Layout 1 holds the low half of the same key. Layout
  2 stores the full key.
- `IsDevelopingContents` is `0` on every sheet row and has no field.
- The sheet has 150 rows client 3482 does not: mesh keys 42952 to 42976 with
  six levels each. Client 3482 has 3,936 rows the sheet lacks.

## Level Groups

On client 3482 the groups come in three lengths, and within each length the
model switches at the same levels:

| entry_count | Levels    | Groups (client 3482) | Model switches at                                              |
| ----------- | --------- | -------------------- | -------------------------------------------------------------- |
| `21`        | 0 to 20   | 97, all weapons      | 19 and 20 in all 97 (`_01`, then `_02`)                         |
| `11`        | 0 to 10   | 222                  | 5 and 8 in all 222 (`_ef1`, then `_ef2`)                       |
| `6`         | 0 to 5    | 277                  | 4 and 5 in 126, 5 only in 93, never in 58                      |

Levels 19 and 20 of a 21-entry group are TET and PEN on the item scale of
`+1` to `+15` then PRI to DEC (the LOC type 79 level names, see
[`specialenchantitem.bss`](specialenchantitem_bss.md)). The scale follows
the items that wear the mesh (see Items): on client 3482 the items behind the
6-entry groups enhance to level 5 (Labreska's Helmet, Dahn's Gloves), those
behind the 11-entry groups to level 10 (Sovereign Kibelius, Edana -
Heavensmite) and those behind the 21-entry groups to level 20 (Blackstar
Longsword). The other items on these meshes are appearance and temporary
versions with no or one level, such as the Edana appearance pieces and the
(Temp) Blackstar weapons.

## Items

The item that wears a mesh is in [`itemenchant.dbss`](itemenchant_dbss.md):
its Class Entry list names an `item_mesh_key` per class type, and those keys
are the `mesh_key` of this file (Item Mesh Keys there). On client 3482, 471
of the 596 groups are named by 739 base items, and in all 1,482 of those
class entries the class type matches the class folder of the group's level
`0` model (class type `0` and `1_pc/1_phm/`, for one). Mesh `336000` is worn
by Blackstar Longsword (715001) and three more items. The `MESH_KEY_ITEMS`
lookup index turns the list around, and the Items column shows the items of
each entry's mesh.

## Notes

- All 6,141 paths on client 3482 start with `1_pc/` and end with `.pac`.
  6,129 are files under `character/model/`. The other 12, every level of
  mesh keys 43080 and 48100, name
  `1_pc/8_pwm/armor/12_foot/pwm_02_foot_0013.pac`, which client 3482 does
  not ship.
- The main groups follow neither key order nor the index's group order:
  client 3482 starts with 336000, 64640, 336001, 64641, 48066.
- The client Lua (client 3482) has no name with `EffectChange` or
  `EffectsChange` in it; the file has no Lua getter.
- The 2016 client's PDB has no `EffectsChange` or `ItemEffectChange` type.
- `itemeffectgroupstaticstatus.bss` shares the `itemeffect` prefix but is a
  different table.

## Open Questions

### Meshes Without an Item

On client 3482, 125 of the 596 mesh keys are in no `itemenchant.dbss` class
entry: 122 six-entry groups and three 21-entry groups, 95 with a weapon model
and 30 with armour, among them 17255 and 336071 to 336075. 103 of them are an `Index` of
the `Item_Mesh_Table` sheet in the private server's client 1784 workbook
(Field Names). Which item, if any, uses them is
open.
