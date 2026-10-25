# `fitnessmaxlevel.bss` Format

## Purpose

Max level of every fitness stat. Value N is the max level of fitness type N, numbered as in the Fitness Type table of [fitnesslevel](fitnesslevel_dbss.md) (`0` Breath, `1` Strength, `2` Health). On client 3464 all three values are `50`, and each `fitnesslevel.dbss` block ends on that level (51 rows for levels 0 to 50).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------- | ----- | ------- | --------- |
| 1      | 1239 and later | `fitnessmaxlevel.bss` | 28    | -       | -         |

| Layout | File                  | Known         | Unknown    |
| ------ | --------------------- | ------------- | ---------- |
| 1      | `fitnessmaxlevel.bss` | 28 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a4c6e6b30a4a`  |
| 3482   | Layout 1 | `a4c6e6b30a4a`  |
| 3474   | Layout 1 | `a4c6e6b30a4a`  |
| 3473   | Layout 1 | `a4c6e6b30a4a`  |
| 3464   | Layout 1 | `a4c6e6b30a4a`  |
| 3458   | Layout 1 | `a4c6e6b30a4a`  |
| 3454   | Layout 1 | `a4c6e6b30a4a`  |
| 3444   | Layout 1 | `a4c6e6b30a4a`  |
| 3435   | Layout 1 | `a4c6e6b30a4a`  |
| 3426   | Layout 1 | `a4c6e6b30a4a`  |
| 3418   | Layout 1 | `a4c6e6b30a4a`  |
| 3412   | Layout 1 | `a4c6e6b30a4a`  |
| 3402   | Layout 1 | `a4c6e6b30a4a`  |
| 3396   | Layout 1 | `a4c6e6b30a4a`  |
| 3387   | Layout 1 | `a4c6e6b30a4a`  |
| 3381   | Layout 1 | `a4c6e6b30a4a`  |
| 3373   | Layout 1 | `a4c6e6b30a4a`  |
| 3364   | Layout 1 | `a4c6e6b30a4a`  |
| 3356   | Layout 1 | `a4c6e6b30a4a`  |
| 3349   | Layout 1 | `a4c6e6b30a4a`  |
| 3342   | Layout 1 | `a4c6e6b30a4a`  |
| 3335   | Layout 1 | `a4c6e6b30a4a`  |
| 3326   | Layout 1 | `a4c6e6b30a4a`  |
| 3321   | Layout 1 | `a4c6e6b30a4a`  |
| 3314   | Layout 1 | `a4c6e6b30a4a`  |
| 3303   | Layout 1 | `a4c6e6b30a4a`  |
| 3302   | Layout 1 | `a4c6e6b30a4a`  |
| 3293   | Layout 1 | `a4c6e6b30a4a`  |
| 3283   | Layout 1 | `a4c6e6b30a4a`  |
| 3275   | Layout 1 | `a4c6e6b30a4a`  |
| 3267   | Layout 1 | `a4c6e6b30a4a`  |
| 3258   | Layout 1 | `a4c6e6b30a4a`  |
| 3251   | Layout 1 | `a4c6e6b30a4a`  |
| 3242   | Layout 1 | `a4c6e6b30a4a`  |
| 3235   | Layout 1 | `a4c6e6b30a4a`  |
| 3229   | Layout 1 | `a4c6e6b30a4a`  |
| 3212   | Layout 1 | `a4c6e6b30a4a`  |
| 3203   | Layout 1 | `a4c6e6b30a4a`  |
| 3193   | Layout 1 | `a4c6e6b30a4a`  |
| 3186   | Layout 1 | `a4c6e6b30a4a`  |
| 3177   | Layout 1 | `a4c6e6b30a4a`  |
| 3169   | Layout 1 | `a4c6e6b30a4a`  |
| 3158   | Layout 1 | `a4c6e6b30a4a`  |
| 3151   | Layout 1 | `a4c6e6b30a4a`  |
| 3144   | Layout 1 | `a4c6e6b30a4a`  |
| 3133   | Layout 1 | `a4c6e6b30a4a`  |
| 3125   | Layout 1 | `a4c6e6b30a4a`  |
| 3118   | Layout 1 | `a4c6e6b30a4a`  |
| 3111   | Layout 1 | `a4c6e6b30a4a`  |
| 3103   | Layout 1 | `a4c6e6b30a4a`  |
| 3095   | Layout 1 | `a4c6e6b30a4a`  |
| 3086   | Layout 1 | `a4c6e6b30a4a`  |
| 3072   | Layout 1 | `a4c6e6b30a4a`  |
| 3062   | Layout 1 | `a4c6e6b30a4a`  |
| 3052   | Layout 1 | `a4c6e6b30a4a`  |
| 3045   | Layout 1 | `a4c6e6b30a4a`  |
| 3037   | Layout 1 | `a4c6e6b30a4a`  |
| 3030   | Layout 1 | `a4c6e6b30a4a`  |
| 3021   | Layout 1 | `a4c6e6b30a4a`  |
| 3012   | Layout 1 | `a4c6e6b30a4a`  |
| 3002   | Layout 1 | `a4c6e6b30a4a`  |
| 2995   | Layout 1 | `a4c6e6b30a4a`  |
| 2987   | Layout 1 | `a4c6e6b30a4a`  |
| 2978   | Layout 1 | `a4c6e6b30a4a`  |
| 2970   | Layout 1 | `a4c6e6b30a4a`  |
| 2959   | Layout 1 | `a4c6e6b30a4a`  |
| 2951   | Layout 1 | `a4c6e6b30a4a`  |
| 2942   | Layout 1 | `a4c6e6b30a4a`  |
| 2935   | Layout 1 | `a4c6e6b30a4a`  |
| 2932   | Layout 1 | `a4c6e6b30a4a`  |
| 2923   | Layout 1 | `a4c6e6b30a4a`  |
| 2919   | Layout 1 | `a4c6e6b30a4a`  |
| 2907   | Layout 1 | `a4c6e6b30a4a`  |
| 2900   | Layout 1 | `a4c6e6b30a4a`  |
| 2891   | Layout 1 | `a4c6e6b30a4a`  |
| 2882   | Layout 1 | `a4c6e6b30a4a`  |
| 2872   | Layout 1 | `a4c6e6b30a4a`  |
| 2863   | Layout 1 | `a4c6e6b30a4a`  |
| 2855   | Layout 1 | `a4c6e6b30a4a`  |
| 2849   | Layout 1 | `a4c6e6b30a4a`  |
| 2844   | Layout 1 | `a4c6e6b30a4a`  |
| 2834   | Layout 1 | `a4c6e6b30a4a`  |
| 2825   | Layout 1 | `a4c6e6b30a4a`  |
| 2819   | Layout 1 | `a4c6e6b30a4a`  |
| 2811   | Layout 1 | `a4c6e6b30a4a`  |
| 2803   | Layout 1 | `a4c6e6b30a4a`  |
| 2794   | Layout 1 | `a4c6e6b30a4a`  |
| 2783   | Layout 1 | `a4c6e6b30a4a`  |
| 2774   | Layout 1 | `a4c6e6b30a4a`  |
| 2765   | Layout 1 | `a4c6e6b30a4a`  |
| 2756   | Layout 1 | `a4c6e6b30a4a`  |
| 2750   | Layout 1 | `a4c6e6b30a4a`  |
| 2743   | Layout 1 | `a4c6e6b30a4a`  |
| 2736   | Layout 1 | `a4c6e6b30a4a`  |
| 2726   | Layout 1 | `a4c6e6b30a4a`  |
| 2717   | Layout 1 | `a4c6e6b30a4a`  |
| 2709   | Layout 1 | `a4c6e6b30a4a`  |
| 2703   | Layout 1 | `a4c6e6b30a4a`  |
| 2695   | Layout 1 | `a4c6e6b30a4a`  |
| 2684   | Layout 1 | `a4c6e6b30a4a`  |
| 2672   | Layout 1 | `a4c6e6b30a4a`  |
| 2665   | Layout 1 | `a4c6e6b30a4a`  |
| 2657   | Layout 1 | `a4c6e6b30a4a`  |
| 2649   | Layout 1 | `a4c6e6b30a4a`  |
| 2644   | Layout 1 | `a4c6e6b30a4a`  |
| 2637   | Layout 1 | `a4c6e6b30a4a`  |
| 2629   | Layout 1 | `a4c6e6b30a4a`  |
| 2619   | Layout 1 | `a4c6e6b30a4a`  |
| 2612   | Layout 1 | `a4c6e6b30a4a`  |
| 2606   | Layout 1 | `a4c6e6b30a4a`  |
| 2602   | Layout 1 | `a4c6e6b30a4a`  |
| 2601   | Layout 1 | `a4c6e6b30a4a`  |
| 2592   | Layout 1 | `a4c6e6b30a4a`  |
| 2583   | Layout 1 | `a4c6e6b30a4a`  |
| 2575   | Layout 1 | `a4c6e6b30a4a`  |
| 2567   | Layout 1 | `a4c6e6b30a4a`  |
| 2560   | Layout 1 | `a4c6e6b30a4a`  |
| 2553   | Layout 1 | `a4c6e6b30a4a`  |
| 2545   | Layout 1 | `a4c6e6b30a4a`  |
| 2538   | Layout 1 | `a4c6e6b30a4a`  |
| 2529   | Layout 1 | `a4c6e6b30a4a`  |
| 2519   | Layout 1 | `a4c6e6b30a4a`  |
| 2513   | Layout 1 | `a4c6e6b30a4a`  |
| 2510   | Layout 1 | `a4c6e6b30a4a`  |
| 2507   | Layout 1 | `a4c6e6b30a4a`  |
| 2503   | Layout 1 | `a4c6e6b30a4a`  |
| 2498   | Layout 1 | `a4c6e6b30a4a`  |
| 2492   | Layout 1 | `a4c6e6b30a4a`  |
| 2487   | Layout 1 | `a4c6e6b30a4a`  |
| 2480   | Layout 1 | `a4c6e6b30a4a`  |
| 2474   | Layout 1 | `a4c6e6b30a4a`  |
| 2468   | Layout 1 | `a4c6e6b30a4a`  |
| 2460   | Layout 1 | `a4c6e6b30a4a`  |
| 2453   | Layout 1 | `a4c6e6b30a4a`  |
| 2444   | Layout 1 | `a4c6e6b30a4a`  |
| 2438   | Layout 1 | `a4c6e6b30a4a`  |
| 2434   | Layout 1 | `a4c6e6b30a4a`  |
| 2429   | Layout 1 | `a4c6e6b30a4a`  |
| 2421   | Layout 1 | `a4c6e6b30a4a`  |
| 2414   | Layout 1 | `a4c6e6b30a4a`  |
| 2407   | Layout 1 | `a4c6e6b30a4a`  |
| 2401   | Layout 1 | `a4c6e6b30a4a`  |
| 2397   | Layout 1 | `a4c6e6b30a4a`  |
| 2393   | Layout 1 | `a4c6e6b30a4a`  |
| 2384   | Layout 1 | `a4c6e6b30a4a`  |
| 2378   | Layout 1 | `a4c6e6b30a4a`  |
| 2372   | Layout 1 | `a4c6e6b30a4a`  |
| 2358   | Layout 1 | `a4c6e6b30a4a`  |
| 2352   | Layout 1 | `a4c6e6b30a4a`  |
| 2347   | Layout 1 | `a4c6e6b30a4a`  |
| 2343   | Layout 1 | `a4c6e6b30a4a`  |
| 2335   | Layout 1 | `a4c6e6b30a4a`  |
| 2327   | Layout 1 | `a4c6e6b30a4a`  |
| 2324   | Layout 1 | `a4c6e6b30a4a`  |
| 2319   | Layout 1 | `a4c6e6b30a4a`  |
| 2313   | Layout 1 | `a4c6e6b30a4a`  |
| 2308   | Layout 1 | `a4c6e6b30a4a`  |
| 2302   | Layout 1 | `a4c6e6b30a4a`  |
| 2295   | Layout 1 | `a4c6e6b30a4a`  |
| 2290   | Layout 1 | `a4c6e6b30a4a`  |
| 2284   | Layout 1 | `a4c6e6b30a4a`  |
| 2276   | Layout 1 | `a4c6e6b30a4a`  |
| 2269   | Layout 1 | `a4c6e6b30a4a`  |
| 2259   | Layout 1 | `a4c6e6b30a4a`  |
| 2250   | Layout 1 | `a4c6e6b30a4a`  |
| 2243   | Layout 1 | `a4c6e6b30a4a`  |
| 2235   | Layout 1 | `a4c6e6b30a4a`  |
| 2229   | Layout 1 | `a4c6e6b30a4a`  |
| 2224   | Layout 1 | `a4c6e6b30a4a`  |
| 2218   | Layout 1 | `a4c6e6b30a4a`  |
| 2215   | Layout 1 | `a4c6e6b30a4a`  |
| 2207   | Layout 1 | `a4c6e6b30a4a`  |
| 2203   | Layout 1 | `a4c6e6b30a4a`  |
| 2196   | Layout 1 | `a4c6e6b30a4a`  |
| 2192   | Layout 1 | `a4c6e6b30a4a`  |
| 2189   | Layout 1 | `a4c6e6b30a4a`  |
| 2183   | Layout 1 | `a4c6e6b30a4a`  |
| 2179   | Layout 1 | `a4c6e6b30a4a`  |
| 2171   | Layout 1 | `a4c6e6b30a4a`  |
| 2163   | Layout 1 | `a4c6e6b30a4a`  |
| 2156   | Layout 1 | `a4c6e6b30a4a`  |
| 2151   | Layout 1 | `a4c6e6b30a4a`  |
| 2147   | Layout 1 | `a4c6e6b30a4a`  |
| 2142   | Layout 1 | `a4c6e6b30a4a`  |
| 2138   | Layout 1 | `a4c6e6b30a4a`  |
| 2134   | Layout 1 | `a4c6e6b30a4a`  |
| 2130   | Layout 1 | `a4c6e6b30a4a`  |
| 2122   | Layout 1 | `a4c6e6b30a4a`  |
| 2107   | Layout 1 | `a4c6e6b30a4a`  |
| 2098   | Layout 1 | `a4c6e6b30a4a`  |
| 2089   | Layout 1 | `a4c6e6b30a4a`  |
| 2081   | Layout 1 | `a4c6e6b30a4a`  |
| 2073   | Layout 1 | `a4c6e6b30a4a`  |
| 2067   | Layout 1 | `a4c6e6b30a4a`  |
| 2063   | Layout 1 | `a4c6e6b30a4a`  |
| 2059   | Layout 1 | `a4c6e6b30a4a`  |
| 2052   | Layout 1 | `a4c6e6b30a4a`  |
| 2044   | Layout 1 | `a4c6e6b30a4a`  |
| 2039   | Layout 1 | `a4c6e6b30a4a`  |
| 2032   | Layout 1 | `a4c6e6b30a4a`  |
| 2025   | Layout 1 | `a4c6e6b30a4a`  |
| 2011   | Layout 1 | `a4c6e6b30a4a`  |
| 2005   | Layout 1 | `a4c6e6b30a4a`  |
| 2000   | Layout 1 | `a4c6e6b30a4a`  |
| 1996   | Layout 1 | `a4c6e6b30a4a`  |
| 1991   | Layout 1 | `a4c6e6b30a4a`  |
| 1985   | Layout 1 | `a4c6e6b30a4a`  |
| 1980   | Layout 1 | `a4c6e6b30a4a`  |
| 1969   | Layout 1 | `a4c6e6b30a4a`  |
| 1964   | Layout 1 | `a4c6e6b30a4a`  |
| 1958   | Layout 1 | `a4c6e6b30a4a`  |
| 1950   | Layout 1 | `a4c6e6b30a4a`  |
| 1945   | Layout 1 | `a4c6e6b30a4a`  |
| 1937   | Layout 1 | `a4c6e6b30a4a`  |
| 1933   | Layout 1 | `a4c6e6b30a4a`  |
| 1927   | Layout 1 | `a4c6e6b30a4a`  |
| 1921   | Layout 1 | `a4c6e6b30a4a`  |
| 1914   | Layout 1 | `a4c6e6b30a4a`  |
| 1908   | Layout 1 | `a4c6e6b30a4a`  |
| 1897   | Layout 1 | `a4c6e6b30a4a`  |
| 1892   | Layout 1 | `a4c6e6b30a4a`  |
| 1886   | Layout 1 | `a4c6e6b30a4a`  |
| 1881   | Layout 1 | `a4c6e6b30a4a`  |
| 1871   | Layout 1 | `a4c6e6b30a4a`  |
| 1866   | Layout 1 | `a4c6e6b30a4a`  |
| 1862   | Layout 1 | `a4c6e6b30a4a`  |
| 1854   | Layout 1 | `a4c6e6b30a4a`  |
| 1846   | Layout 1 | `a4c6e6b30a4a`  |
| 1838   | Layout 1 | `a4c6e6b30a4a`  |
| 1832   | Layout 1 | `a4c6e6b30a4a`  |
| 1826   | Layout 1 | `a4c6e6b30a4a`  |
| 1822   | Layout 1 | `a4c6e6b30a4a`  |
| 1818   | Layout 1 | `a4c6e6b30a4a`  |
| 1804   | Layout 1 | `a4c6e6b30a4a`  |
| 1794   | Layout 1 | `a4c6e6b30a4a`  |
| 1790   | Layout 1 | `a4c6e6b30a4a`  |
| 1784   | Layout 1 | `a4c6e6b30a4a`  |
| 1774   | Layout 1 | `a4c6e6b30a4a`  |
| 1771   | Layout 1 | `a4c6e6b30a4a`  |
| 1762   | Layout 1 | `a4c6e6b30a4a`  |
| 1759   | Layout 1 | `a4c6e6b30a4a`  |
| 1754   | Layout 1 | `a4c6e6b30a4a`  |
| 1749   | Layout 1 | `a4c6e6b30a4a`  |
| 1743   | Layout 1 | `a4c6e6b30a4a`  |
| 1737   | Layout 1 | `a4c6e6b30a4a`  |
| 1731   | Layout 1 | `a4c6e6b30a4a`  |
| 1725   | Layout 1 | `a4c6e6b30a4a`  |
| 1717   | Layout 1 | `a4c6e6b30a4a`  |
| 1710   | Layout 1 | `a4c6e6b30a4a`  |
| 1704   | Layout 1 | `a4c6e6b30a4a`  |
| 1698   | Layout 1 | `a4c6e6b30a4a`  |
| 1690   | Layout 1 | `a4c6e6b30a4a`  |
| 1685   | Layout 1 | `a4c6e6b30a4a`  |
| 1680   | Layout 1 | `a4c6e6b30a4a`  |
| 1674   | Layout 1 | `a4c6e6b30a4a`  |
| 1668   | Layout 1 | `a4c6e6b30a4a`  |
| 1659   | Layout 1 | `a4c6e6b30a4a`  |
| 1649   | Layout 1 | `a4c6e6b30a4a`  |
| 1642   | Layout 1 | `a4c6e6b30a4a`  |
| 1636   | Layout 1 | `a4c6e6b30a4a`  |
| 1628   | Layout 1 | `a4c6e6b30a4a`  |
| 1622   | Layout 1 | `a4c6e6b30a4a`  |
| 1614   | Layout 1 | `a4c6e6b30a4a`  |
| 1608   | Layout 1 | `a4c6e6b30a4a`  |
| 1602   | Layout 1 | `a4c6e6b30a4a`  |
| 1598   | Layout 1 | `a4c6e6b30a4a`  |
| 1594   | Layout 1 | `a4c6e6b30a4a`  |
| 1590   | Layout 1 | `a4c6e6b30a4a`  |
| 1587   | Layout 1 | `a4c6e6b30a4a`  |
| 1584   | Layout 1 | `a4c6e6b30a4a`  |
| 1579   | Layout 1 | `a4c6e6b30a4a`  |
| 1572   | Layout 1 | `a4c6e6b30a4a`  |
| 1565   | Layout 1 | `a4c6e6b30a4a`  |
| 1559   | Layout 1 | `a4c6e6b30a4a`  |
| 1554   | Layout 1 | `a4c6e6b30a4a`  |
| 1547   | Layout 1 | `a4c6e6b30a4a`  |
| 1537   | Layout 1 | `a4c6e6b30a4a`  |
| 1529   | Layout 1 | `a4c6e6b30a4a`  |
| 1524   | Layout 1 | `a4c6e6b30a4a`  |
| 1519   | Layout 1 | `a4c6e6b30a4a`  |
| 1509   | Layout 1 | `a4c6e6b30a4a`  |
| 1506   | Layout 1 | `a4c6e6b30a4a`  |
| 1504   | Layout 1 | `a4c6e6b30a4a`  |
| 1500   | Layout 1 | `a4c6e6b30a4a`  |
| 1493   | Layout 1 | `a4c6e6b30a4a`  |
| 1489   | Layout 1 | `a4c6e6b30a4a`  |
| 1485   | Layout 1 | `a4c6e6b30a4a`  |
| 1481   | Layout 1 | `a4c6e6b30a4a`  |
| 1474   | Layout 1 | `a4c6e6b30a4a`  |
| 1466   | Layout 1 | `a4c6e6b30a4a`  |
| 1462   | Layout 1 | `a4c6e6b30a4a`  |
| 1459   | Layout 1 | `a4c6e6b30a4a`  |
| 1453   | Layout 1 | `a4c6e6b30a4a`  |
| 1450   | Layout 1 | `a4c6e6b30a4a`  |
| 1445   | Layout 1 | `a4c6e6b30a4a`  |
| 1439   | Layout 1 | `a4c6e6b30a4a`  |
| 1433   | Layout 1 | `a4c6e6b30a4a`  |
| 1430   | Layout 1 | `a4c6e6b30a4a`  |
| 1426   | Layout 1 | `a4c6e6b30a4a`  |
| 1421   | Layout 1 | `a4c6e6b30a4a`  |
| 1417   | Layout 1 | `a4c6e6b30a4a`  |
| 1416   | Layout 1 | `a4c6e6b30a4a`  |
| 1409   | Layout 1 | `a4c6e6b30a4a`  |
| 1405   | Layout 1 | `a4c6e6b30a4a`  |
| 1401   | Layout 1 | `a4c6e6b30a4a`  |
| 1396   | Layout 1 | `a4c6e6b30a4a`  |
| 1391   | Layout 1 | `a4c6e6b30a4a`  |
| 1390   | Layout 1 | `a4c6e6b30a4a`  |
| 1386   | Layout 1 | `a4c6e6b30a4a`  |
| 1381   | Layout 1 | `a4c6e6b30a4a`  |
| 1379   | Layout 1 | `a4c6e6b30a4a`  |
| 1372   | Layout 1 | `a4c6e6b30a4a`  |
| 1366   | Layout 1 | `a4c6e6b30a4a`  |
| 1364   | Layout 1 | `a4c6e6b30a4a`  |
| 1363   | Layout 1 | `a4c6e6b30a4a`  |
| 1360   | Layout 1 | `a4c6e6b30a4a`  |
| 1358   | Layout 1 | `a4c6e6b30a4a`  |
| 1355   | Layout 1 | `a4c6e6b30a4a`  |
| 1351   | Layout 1 | `a4c6e6b30a4a`  |
| 1348   | Layout 1 | `a4c6e6b30a4a`  |
| 1346   | Layout 1 | `a4c6e6b30a4a`  |
| 1341   | Layout 1 | `a4c6e6b30a4a`  |
| 1340   | Layout 1 | `a4c6e6b30a4a`  |
| 1338   | Layout 1 | `a4c6e6b30a4a`  |
| 1335   | Layout 1 | `a4c6e6b30a4a`  |
| 1333   | Layout 1 | `a4c6e6b30a4a`  |
| 1329   | Layout 1 | `a4c6e6b30a4a`  |
| 1327   | Layout 1 | `a4c6e6b30a4a`  |
| 1324   | Layout 1 | `a4c6e6b30a4a`  |
| 1321   | Layout 1 | `a4c6e6b30a4a`  |
| 1319   | Layout 1 | `a4c6e6b30a4a`  |
| 1318   | Layout 1 | `a4c6e6b30a4a`  |
| 1316   | Layout 1 | `a4c6e6b30a4a`  |
| 1313   | Layout 1 | `a4c6e6b30a4a`  |
| 1311   | Layout 1 | `a4c6e6b30a4a`  |
| 1309   | Layout 1 | `a4c6e6b30a4a`  |
| 1304   | Layout 1 | `a4c6e6b30a4a`  |
| 1292   | Layout 1 | `a4c6e6b30a4a`  |
| 1286   | Layout 1 | `a4c6e6b30a4a`  |
| 1280   | Layout 1 | `a4c6e6b30a4a`  |
| 1276   | Layout 1 | `a4c6e6b30a4a`  |
| 1267   | Layout 1 | `a4c6e6b30a4a`  |
| 1261   | Layout 1 | `a4c6e6b30a4a`  |
| 1256   | Layout 1 | `a4c6e6b30a4a`  |
| 1250   | Layout 1 | `a4c6e6b30a4a`  |
| 1246   | Layout 1 | `a4c6e6b30a4a`  |
| 1239   | Layout 1 | `a4c6e6b30a4a`  |
| 1230   | No file  | `a4c6e6b30a4a`  |
| 1226   | No file  | `a4c6e6b30a4a`  |
| 1220   | No file  | `a4c6e6b30a4a`  |
| 1217   | No file  | `a4c6e6b30a4a`  |
| 1211   | No file  | `a4c6e6b30a4a`  |
| 1210   | No file  | `a4c6e6b30a4a`  |
| 1208   | No file  | `a4c6e6b30a4a`  |
| 1203   | No file  | `a4c6e6b30a4a`  |
| 1197   | No file  | `a4c6e6b30a4a`  |
| 1194   | No file  | `a4c6e6b30a4a`  |
| 1192   | No file  | `a4c6e6b30a4a`  |
| 1187   | No file  | `a4c6e6b30a4a`  |
| 1183   | No file  | `a4c6e6b30a4a`  |
| 1177   | No file  | `a4c6e6b30a4a`  |
| 1173   | No file  | `a4c6e6b30a4a`  |
| 1167   | No file  | `a4c6e6b30a4a`  |
| 1164   | No file  | `a4c6e6b30a4a`  |
| 1156   | No file  | `a4c6e6b30a4a`  |
| 1149   | No file  | `a4c6e6b30a4a`  |
| 1144   | No file  | `a4c6e6b30a4a`  |
| 1137   | No file  | `a4c6e6b30a4a`  |
| 1132   | No file  | `a4c6e6b30a4a`  |
| 1127   | No file  | `a4c6e6b30a4a`  |
| 1122   | No file  | `a4c6e6b30a4a`  |
| 1118   | No file  | `a4c6e6b30a4a`  |
| 1114   | No file  | `a4c6e6b30a4a`  |
| 1109   | No file  | `a4c6e6b30a4a`  |
| 1102   | No file  | `a4c6e6b30a4a`  |
| 1096   | No file  | `a4c6e6b30a4a`  |
| 1088   | No file  | `a4c6e6b30a4a`  |
| 1081   | No file  | `a4c6e6b30a4a`  |
| 1076   | No file  | `a4c6e6b30a4a`  |
| 1069   | No file  | `a4c6e6b30a4a`  |
| 1064   | No file  | `a4c6e6b30a4a`  |
| 1058   | No file  | `a4c6e6b30a4a`  |
| 1051   | No file  | `a4c6e6b30a4a`  |
| 1044   | No file  | `a4c6e6b30a4a`  |
| 1036   | No file  | `a4c6e6b30a4a`  |
| 1026   | No file  | `a4c6e6b30a4a`  |
| 1016   | No file  | `a4c6e6b30a4a`  |
| 1009   | No file  | `a4c6e6b30a4a`  |
| 1005   | No file  | `a4c6e6b30a4a`  |
| 1000   | No file  | `a4c6e6b30a4a`  |
| 998    | No file  | `a4c6e6b30a4a`  |
| 990    | No file  | `a4c6e6b30a4a`  |
| 979    | No file  | `a4c6e6b30a4a`  |
| 972    | No file  | `a4c6e6b30a4a`  |
| 963    | No file  | `a4c6e6b30a4a`  |
| 955    | No file  | `a4c6e6b30a4a`  |
| 946    | No file  | `a4c6e6b30a4a`  |
| 938    | No file  | `a4c6e6b30a4a`  |
| 927    | No file  | `a4c6e6b30a4a`  |
| 911    | No file  | `a4c6e6b30a4a`  |
| 904    | No file  | `a4c6e6b30a4a`  |
| 899    | No file  | `a4c6e6b30a4a`  |
| 894    | No file  | `a4c6e6b30a4a`  |
| 885    | No file  | `a4c6e6b30a4a`  |
| 879    | No file  | `a4c6e6b30a4a`  |
| 872    | No file  | `a4c6e6b30a4a`  |
| 864    | No file  | `a4c6e6b30a4a`  |
| 855    | No file  | `a4c6e6b30a4a`  |
| 853    | No file  | `a4c6e6b30a4a`  |
| 845    | No file  | `a4c6e6b30a4a`  |
| 837    | No file  | `a4c6e6b30a4a`  |
| 829    | No file  | `a4c6e6b30a4a`  |
| 822    | No file  | `a4c6e6b30a4a`  |
| 814    | No file  | `a4c6e6b30a4a`  |
| 805    | No file  | `a4c6e6b30a4a`  |
| 794    | No file  | `a4c6e6b30a4a`  |
| 787    | No file  | `a4c6e6b30a4a`  |
| 780    | No file  | `a4c6e6b30a4a`  |
| 771    | No file  | `a4c6e6b30a4a`  |
| 760    | No file  | `a4c6e6b30a4a`  |
| 748    | No file  | `a4c6e6b30a4a`  |
| 741    | No file  | `a4c6e6b30a4a`  |
| 736    | No file  | `a4c6e6b30a4a`  |
| 731    | No file  | `a4c6e6b30a4a`  |
| 723    | No file  | `a4c6e6b30a4a`  |
| 711    | No file  | `a4c6e6b30a4a`  |
| 707    | No file  | `a4c6e6b30a4a`  |
| 697    | No file  | `a4c6e6b30a4a`  |
| 689    | No file  | `a4c6e6b30a4a`  |
| 683    | No file  | `a4c6e6b30a4a`  |
| 678    | No file  | `a4c6e6b30a4a`  |
| 670    | No file  | `a4c6e6b30a4a`  |
| 661    | No file  | `a4c6e6b30a4a`  |
| 656    | No file  | `a4c6e6b30a4a`  |
| 652    | No file  | `a4c6e6b30a4a`  |
| 643    | No file  | `a4c6e6b30a4a`  |
| 637    | No file  | `a4c6e6b30a4a`  |
| 630    | No file  | `a4c6e6b30a4a`  |
| 627    | No file  | `a4c6e6b30a4a`  |
| 621    | No file  | `a4c6e6b30a4a`  |
| 617    | No file  | `a4c6e6b30a4a`  |
| 615    | No file  | `a4c6e6b30a4a`  |
| 606    | No file  | `a4c6e6b30a4a`  |
| 599    | No file  | `a4c6e6b30a4a`  |
| 592    | No file  | `a4c6e6b30a4a`  |
| 586    | No file  | `a4c6e6b30a4a`  |
| 577    | No file  | `a4c6e6b30a4a`  |
| 569    | No file  | `a4c6e6b30a4a`  |
| 561    | No file  | `a4c6e6b30a4a`  |
| 554    | No file  | `a4c6e6b30a4a`  |
| 542    | No file  | `a4c6e6b30a4a`  |
| 532    | No file  | `a4c6e6b30a4a`  |
| 531    | No file  | `a4c6e6b30a4a`  |
| 526    | No file  | `a4c6e6b30a4a`  |
| 521    | No file  | `a4c6e6b30a4a`  |
| 517    | No file  | `a4c6e6b30a4a`  |
| 510    | No file  | `a4c6e6b30a4a`  |
| 508    | No file  | `a4c6e6b30a4a`  |
| 504    | No file  | `a4c6e6b30a4a`  |
| 497    | No file  | `a4c6e6b30a4a`  |
| 491    | No file  | `a4c6e6b30a4a`  |
| 485    | No file  | `a4c6e6b30a4a`  |
| 478    | No file  | `a4c6e6b30a4a`  |
| 472    | No file  | `a4c6e6b30a4a`  |
| 466    | No file  | `a4c6e6b30a4a`  |
| 457    | No file  | `a4c6e6b30a4a`  |
| 452    | No file  | `a4c6e6b30a4a`  |
| 449    | No file  | `a4c6e6b30a4a`  |
| 435    | No file  | `a4c6e6b30a4a`  |

<!-- versions:end -->

## Companion Files

None. The fitness type names come from `_dbss/fitnesslevel/labels.py` (see Notes).

All multi-byte values are little-endian.

## Layout 1

### File Layout

`PABR` magic, a bare u32 array with no count, then the 12-byte PABR trailer (the last three rows). 28 bytes on client 3464.

| Offset     | Type       | Field     | Notes                                                    |
| ---------- | ---------- | --------- | -------------------------------------------------------- |
| `+0x00`    | char[4]    | magic     | `PABR` (ASCII)                                           |
| `+0x04`    | u32[..end_of_data] | max_level | One per fitness type; value N is the max level of type N; runs up to `end_of_data` |
| `EOF-0x0C` | u32        | string_count | `0`: the empty PABR string table                      |
| `EOF-0x08` | u32        | end_of_data | `16`; byte offset right after the last `max_level`     |
| `EOF-0x04` | u32        | zero      | `0`                                                      |

The array length is not stored; the parser takes it from the trailer's `end_of_data`: `(end_of_data - 4) / 4` values.

The same trailer closes `acceptquest.bss` and the PABR offset files.

## Notes

- The fitness type names are the ones in [fitnesslevel](fitnesslevel_dbss.md); both handlers read them through `_dbss/fitnesslevel/labels.py`.
- Level 30 is the soft cap and this file does not store it. It shows only in the EXP column of `fitnesslevel.dbss`; see the [fitnesslevel](fitnesslevel_dbss.md) Notes.
- `lifeexpmaxlevel.bss` is the life skill counterpart, a bare u32 array with no magic and no trailer; see [lifeexpmaxlevel](lifeexpmaxlevel_bss.md).
- `skillexperiencemaxlevel.bss` and `guildskillexperiencemaxlevel.bss` (18 bytes each) use the same magic and trailer around a u16 array (`2000` and `1000`, trailer `end_of_data` `6`); see [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md).
