# `rosewarstaticstatus.bss` Format

## Purpose

The Rose War settings: one set of values after the PABR magic, with two
u64, 25 u32 and one f32 settings, the boss and the home region of each
team, the Rose War regions, an item and two weekly schedules. On client 3474 the
bosses are Narchillan and Sephir, the home regions Grána and O'draxxia,
and the item is Medal of Sylvia (`761066`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes | Records             | Row bytes |
| ------ | -------------- | ------------------------- | ----- | ------------------- | --------- |
| 1      | 2575 and later | `rosewarstaticstatus.bss` | 372   | 16 Time, 2 Schedule | 12        |

| Layout | File                      | Known         | Unknown       |
| ------ | ------------------------- | ------------- | ------------- |
| 1      | `rosewarstaticstatus.bss` | 250 B (67.2%) | 122 B (32.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `9a6c6c8b88f0`  |
| 3482   | Layout 1             | `9a6c6c8b88f0`  |
| 3474   | Layout 1             | `9a6c6c8b88f0`  |
| 3473   | Layout 1             | `9a6c6c8b88f0`  |
| 3464   | Layout 1             | `9a6c6c8b88f0`  |
| 3458   | Layout 1             | `9a6c6c8b88f0`  |
| 3454   | Layout 1             | `9a6c6c8b88f0`  |
| 3444   | Layout 1             | `9a6c6c8b88f0`  |
| 3435   | Layout 1             | `9a6c6c8b88f0`  |
| 3426   | Layout 1             | `9a6c6c8b88f0`  |
| 3418   | Layout 1             | `9a6c6c8b88f0`  |
| 3412   | Layout 1             | `9a6c6c8b88f0`  |
| 3402   | Layout 1             | `9a6c6c8b88f0`  |
| 3396   | Layout 1             | `9a6c6c8b88f0`  |
| 3387   | Layout 1             | `9a6c6c8b88f0`  |
| 3381   | Layout 1             | `9a6c6c8b88f0`  |
| 3373   | Layout 1             | `9a6c6c8b88f0`  |
| 3364   | Layout 1             | `9a6c6c8b88f0`  |
| 3356   | Layout 1             | `9a6c6c8b88f0`  |
| 3349   | Layout 1             | `9a6c6c8b88f0`  |
| 3342   | Layout 1             | `9a6c6c8b88f0`  |
| 3335   | Layout 1             | `9a6c6c8b88f0`  |
| 3326   | Layout 1             | `9a6c6c8b88f0`  |
| 3321   | Layout 1             | `9a6c6c8b88f0`  |
| 3314   | Layout 1             | `9a6c6c8b88f0`  |
| 3303   | Layout 1             | `9a6c6c8b88f0`  |
| 3302   | Layout 1             | `9a6c6c8b88f0`  |
| 3293   | Layout 1             | `9a6c6c8b88f0`  |
| 3283   | Layout 1             | `9a6c6c8b88f0`  |
| 3275   | Layout 1             | `9a6c6c8b88f0`  |
| 3267   | Layout 1             | `9a6c6c8b88f0`  |
| 3258   | Layout 1             | `9a6c6c8b88f0`  |
| 3251   | Layout 1             | `9a6c6c8b88f0`  |
| 3242   | Layout 1             | `9a6c6c8b88f0`  |
| 3235   | Layout 1             | `9a6c6c8b88f0`  |
| 3229   | Layout 1             | `9a6c6c8b88f0`  |
| 3212   | Layout 1             | `9a6c6c8b88f0`  |
| 3203   | Layout 1             | `9a6c6c8b88f0`  |
| 3193   | Layout 1             | `9a6c6c8b88f0`  |
| 3186   | Layout 1             | `9a6c6c8b88f0`  |
| 3177   | Layout 1             | `9a6c6c8b88f0`  |
| 3169   | Layout 1             | `9a6c6c8b88f0`  |
| 3158   | Layout 1             | `9a6c6c8b88f0`  |
| 3151   | Layout 1             | `9a6c6c8b88f0`  |
| 3144   | Layout 1             | `9a6c6c8b88f0`  |
| 3133   | Layout 1             | `9a6c6c8b88f0`  |
| 3125   | Layout 1             | `9a6c6c8b88f0`  |
| 3118   | Layout 1             | `9a6c6c8b88f0`  |
| 3111   | Layout 1             | `9a6c6c8b88f0`  |
| 3103   | Layout 1             | `9a6c6c8b88f0`  |
| 3095   | Layout 1             | `9a6c6c8b88f0`  |
| 3086   | Layout 1             | `9a6c6c8b88f0`  |
| 3072   | Layout 1             | `9a6c6c8b88f0`  |
| 3062   | Layout 1             | `9a6c6c8b88f0`  |
| 3052   | Layout 1             | `9a6c6c8b88f0`  |
| 3045   | Layout 1             | `9a6c6c8b88f0`  |
| 3037   | Layout 1             | `9a6c6c8b88f0`  |
| 3030   | Layout 1             | `9a6c6c8b88f0`  |
| 3021   | Layout 1             | `9a6c6c8b88f0`  |
| 3012   | Layout 1             | `9a6c6c8b88f0`  |
| 3002   | Layout 1             | `9a6c6c8b88f0`  |
| 2995   | Layout 1             | `9a6c6c8b88f0`  |
| 2987   | Layout 1             | `9a6c6c8b88f0`  |
| 2978   | Layout 1             | `9a6c6c8b88f0`  |
| 2970   | Layout 1             | `9a6c6c8b88f0`  |
| 2959   | Layout 1             | `9a6c6c8b88f0`  |
| 2951   | Layout 1             | `9a6c6c8b88f0`  |
| 2942   | Layout 1             | `9a6c6c8b88f0`  |
| 2935   | Layout 1             | `9a6c6c8b88f0`  |
| 2932   | Layout 1             | `9a6c6c8b88f0`  |
| 2923   | Layout 1             | `9a6c6c8b88f0`  |
| 2919   | Layout 1             | `9a6c6c8b88f0`  |
| 2907   | Layout 1             | `9a6c6c8b88f0`  |
| 2900   | Layout 1             | `9a6c6c8b88f0`  |
| 2891   | Layout 1             | `9a6c6c8b88f0`  |
| 2882   | Layout 1             | `9a6c6c8b88f0`  |
| 2872   | Layout 1             | `9a6c6c8b88f0`  |
| 2863   | Layout 1             | `9a6c6c8b88f0`  |
| 2855   | Layout 1             | `9a6c6c8b88f0`  |
| 2849   | Layout 1             | `9a6c6c8b88f0`  |
| 2844   | Layout 1             | `9a6c6c8b88f0`  |
| 2834   | Layout 1             | `9a6c6c8b88f0`  |
| 2825   | Layout 1             | `9a6c6c8b88f0`  |
| 2819   | Layout 1             | `9a6c6c8b88f0`  |
| 2811   | Layout 1             | `9a6c6c8b88f0`  |
| 2803   | Layout 1             | `9a6c6c8b88f0`  |
| 2794   | Layout 1             | `9a6c6c8b88f0`  |
| 2783   | Layout 1             | `9a6c6c8b88f0`  |
| 2774   | Layout 1             | `9a6c6c8b88f0`  |
| 2765   | Layout 1             | `9a6c6c8b88f0`  |
| 2756   | Layout 1             | `9a6c6c8b88f0`  |
| 2750   | Layout 1             | `9a6c6c8b88f0`  |
| 2743   | Layout 1             | `9a6c6c8b88f0`  |
| 2736   | Layout 1             | `9a6c6c8b88f0`  |
| 2726   | Layout 1             | `9a6c6c8b88f0`  |
| 2717   | Layout 1             | `9a6c6c8b88f0`  |
| 2709   | Layout 1             | `9a6c6c8b88f0`  |
| 2703   | Layout 1             | `9a6c6c8b88f0`  |
| 2695   | Layout 1             | `9a6c6c8b88f0`  |
| 2684   | Layout 1             | `9a6c6c8b88f0`  |
| 2672   | Layout 1             | `9a6c6c8b88f0`  |
| 2665   | Layout 1             | `9a6c6c8b88f0`  |
| 2657   | Layout 1             | `9a6c6c8b88f0`  |
| 2649   | Layout 1             | `9a6c6c8b88f0`  |
| 2644   | Layout 1             | `9a6c6c8b88f0`  |
| 2637   | Layout 1             | `9a6c6c8b88f0`  |
| 2629   | Layout 1             | `9a6c6c8b88f0`  |
| 2619   | Layout 1             | `9a6c6c8b88f0`  |
| 2612   | Layout 1             | `9a6c6c8b88f0`  |
| 2606   | Layout 1             | `9a6c6c8b88f0`  |
| 2602   | Layout 1             | `9a6c6c8b88f0`  |
| 2601   | Layout 1             | `9a6c6c8b88f0`  |
| 2592   | Layout 1             | `9a6c6c8b88f0`  |
| 2583   | Layout 1             | `9a6c6c8b88f0`  |
| 2575   | Layout 1             | `9a6c6c8b88f0`  |
| 2567   | No documented layout | `9a6c6c8b88f0`  |
| 2560   | No documented layout | `9a6c6c8b88f0`  |
| 2553   | No documented layout | `9a6c6c8b88f0`  |
| 2545   | No documented layout | `9a6c6c8b88f0`  |
| 2538   | No file              | `9a6c6c8b88f0`  |
| 2529   | No file              | `9a6c6c8b88f0`  |
| 2519   | No file              | `9a6c6c8b88f0`  |
| 2513   | No file              | `9a6c6c8b88f0`  |
| 2510   | No file              | `9a6c6c8b88f0`  |
| 2507   | No file              | `9a6c6c8b88f0`  |
| 2503   | No file              | `9a6c6c8b88f0`  |
| 2498   | No file              | `9a6c6c8b88f0`  |
| 2492   | No file              | `9a6c6c8b88f0`  |
| 2487   | No file              | `9a6c6c8b88f0`  |
| 2480   | No file              | `9a6c6c8b88f0`  |
| 2474   | No file              | `9a6c6c8b88f0`  |
| 2468   | No file              | `9a6c6c8b88f0`  |
| 2460   | No file              | `9a6c6c8b88f0`  |
| 2453   | No file              | `9a6c6c8b88f0`  |
| 2444   | No file              | `9a6c6c8b88f0`  |
| 2438   | No file              | `9a6c6c8b88f0`  |
| 2434   | No file              | `9a6c6c8b88f0`  |
| 2429   | No file              | `9a6c6c8b88f0`  |
| 2421   | No file              | `9a6c6c8b88f0`  |
| 2414   | No file              | `9a6c6c8b88f0`  |
| 2407   | No file              | `9a6c6c8b88f0`  |
| 2401   | No file              | `9a6c6c8b88f0`  |
| 2397   | No file              | `9a6c6c8b88f0`  |
| 2393   | No file              | `9a6c6c8b88f0`  |
| 2384   | No file              | `9a6c6c8b88f0`  |
| 2378   | No file              | `9a6c6c8b88f0`  |
| 2372   | No file              | `9a6c6c8b88f0`  |
| 2358   | No file              | `9a6c6c8b88f0`  |
| 2352   | No file              | `9a6c6c8b88f0`  |
| 2347   | No file              | `9a6c6c8b88f0`  |
| 2343   | No file              | `9a6c6c8b88f0`  |
| 2335   | No file              | `9a6c6c8b88f0`  |
| 2327   | No file              | `9a6c6c8b88f0`  |
| 2324   | No file              | `9a6c6c8b88f0`  |
| 2319   | No file              | `9a6c6c8b88f0`  |
| 2313   | No file              | `9a6c6c8b88f0`  |
| 2308   | No file              | `9a6c6c8b88f0`  |
| 2302   | No file              | `9a6c6c8b88f0`  |
| 2295   | No file              | `9a6c6c8b88f0`  |
| 2290   | No file              | `9a6c6c8b88f0`  |
| 2284   | No file              | `9a6c6c8b88f0`  |
| 2276   | No file              | `9a6c6c8b88f0`  |
| 2269   | No file              | `9a6c6c8b88f0`  |
| 2259   | No file              | `9a6c6c8b88f0`  |
| 2250   | No file              | `9a6c6c8b88f0`  |
| 2243   | No file              | `9a6c6c8b88f0`  |
| 2235   | No file              | `9a6c6c8b88f0`  |
| 2229   | No file              | `9a6c6c8b88f0`  |
| 2224   | No file              | `9a6c6c8b88f0`  |
| 2218   | No file              | `9a6c6c8b88f0`  |
| 2215   | No file              | `9a6c6c8b88f0`  |
| 2207   | No file              | `9a6c6c8b88f0`  |
| 2203   | No file              | `9a6c6c8b88f0`  |
| 2196   | No file              | `9a6c6c8b88f0`  |
| 2192   | No file              | `9a6c6c8b88f0`  |
| 2189   | No file              | `9a6c6c8b88f0`  |
| 2183   | No file              | `9a6c6c8b88f0`  |
| 2179   | No file              | `9a6c6c8b88f0`  |
| 2171   | No file              | `9a6c6c8b88f0`  |
| 2163   | No file              | `9a6c6c8b88f0`  |
| 2156   | No file              | `9a6c6c8b88f0`  |
| 2151   | No file              | `9a6c6c8b88f0`  |
| 2147   | No file              | `9a6c6c8b88f0`  |
| 2142   | No file              | `9a6c6c8b88f0`  |
| 2138   | No file              | `9a6c6c8b88f0`  |
| 2134   | No file              | `9a6c6c8b88f0`  |
| 2130   | No file              | `9a6c6c8b88f0`  |
| 2122   | No file              | `9a6c6c8b88f0`  |
| 2107   | No file              | `9a6c6c8b88f0`  |
| 2098   | No file              | `9a6c6c8b88f0`  |
| 2089   | No file              | `9a6c6c8b88f0`  |
| 2081   | No file              | `9a6c6c8b88f0`  |
| 2073   | No file              | `9a6c6c8b88f0`  |
| 2067   | No file              | `9a6c6c8b88f0`  |
| 2063   | No file              | `9a6c6c8b88f0`  |
| 2059   | No file              | `9a6c6c8b88f0`  |
| 2052   | No file              | `9a6c6c8b88f0`  |
| 2044   | No file              | `9a6c6c8b88f0`  |
| 2039   | No file              | `9a6c6c8b88f0`  |
| 2032   | No file              | `9a6c6c8b88f0`  |
| 2025   | No file              | `9a6c6c8b88f0`  |
| 2011   | No file              | `9a6c6c8b88f0`  |
| 2005   | No file              | `9a6c6c8b88f0`  |
| 2000   | No file              | `9a6c6c8b88f0`  |
| 1996   | No file              | `9a6c6c8b88f0`  |
| 1991   | No file              | `9a6c6c8b88f0`  |
| 1985   | No file              | `9a6c6c8b88f0`  |
| 1980   | No file              | `9a6c6c8b88f0`  |
| 1969   | No file              | `9a6c6c8b88f0`  |
| 1964   | No file              | `9a6c6c8b88f0`  |
| 1958   | No file              | `9a6c6c8b88f0`  |
| 1950   | No file              | `9a6c6c8b88f0`  |
| 1945   | No file              | `9a6c6c8b88f0`  |
| 1937   | No file              | `9a6c6c8b88f0`  |
| 1933   | No file              | `9a6c6c8b88f0`  |
| 1927   | No file              | `9a6c6c8b88f0`  |
| 1921   | No file              | `9a6c6c8b88f0`  |
| 1914   | No file              | `9a6c6c8b88f0`  |
| 1908   | No file              | `9a6c6c8b88f0`  |
| 1897   | No file              | `9a6c6c8b88f0`  |
| 1892   | No file              | `9a6c6c8b88f0`  |
| 1886   | No file              | `9a6c6c8b88f0`  |
| 1881   | No file              | `9a6c6c8b88f0`  |
| 1871   | No file              | `9a6c6c8b88f0`  |
| 1866   | No file              | `9a6c6c8b88f0`  |
| 1862   | No file              | `9a6c6c8b88f0`  |
| 1854   | No file              | `9a6c6c8b88f0`  |
| 1846   | No file              | `9a6c6c8b88f0`  |
| 1838   | No file              | `9a6c6c8b88f0`  |
| 1832   | No file              | `9a6c6c8b88f0`  |
| 1826   | No file              | `9a6c6c8b88f0`  |
| 1822   | No file              | `9a6c6c8b88f0`  |
| 1818   | No file              | `9a6c6c8b88f0`  |
| 1804   | No file              | `9a6c6c8b88f0`  |
| 1794   | No file              | `9a6c6c8b88f0`  |
| 1790   | No file              | `9a6c6c8b88f0`  |
| 1784   | No file              | `9a6c6c8b88f0`  |
| 1774   | No file              | `9a6c6c8b88f0`  |
| 1771   | No file              | `9a6c6c8b88f0`  |
| 1762   | No file              | `9a6c6c8b88f0`  |
| 1759   | No file              | `9a6c6c8b88f0`  |
| 1754   | No file              | `9a6c6c8b88f0`  |
| 1749   | No file              | `9a6c6c8b88f0`  |
| 1743   | No file              | `9a6c6c8b88f0`  |
| 1737   | No file              | `9a6c6c8b88f0`  |
| 1731   | No file              | `9a6c6c8b88f0`  |
| 1725   | No file              | `9a6c6c8b88f0`  |
| 1717   | No file              | `9a6c6c8b88f0`  |
| 1710   | No file              | `9a6c6c8b88f0`  |
| 1704   | No file              | `9a6c6c8b88f0`  |
| 1698   | No file              | `9a6c6c8b88f0`  |
| 1690   | No file              | `9a6c6c8b88f0`  |
| 1685   | No file              | `9a6c6c8b88f0`  |
| 1680   | No file              | `9a6c6c8b88f0`  |
| 1674   | No file              | `9a6c6c8b88f0`  |
| 1668   | No file              | `9a6c6c8b88f0`  |
| 1659   | No file              | `9a6c6c8b88f0`  |
| 1649   | No file              | `9a6c6c8b88f0`  |
| 1642   | No file              | `9a6c6c8b88f0`  |
| 1636   | No file              | `9a6c6c8b88f0`  |
| 1628   | No file              | `9a6c6c8b88f0`  |
| 1622   | No file              | `9a6c6c8b88f0`  |
| 1614   | No file              | `9a6c6c8b88f0`  |
| 1608   | No file              | `9a6c6c8b88f0`  |
| 1602   | No file              | `9a6c6c8b88f0`  |
| 1598   | No file              | `9a6c6c8b88f0`  |
| 1594   | No file              | `9a6c6c8b88f0`  |
| 1590   | No file              | `9a6c6c8b88f0`  |
| 1587   | No file              | `9a6c6c8b88f0`  |
| 1584   | No file              | `9a6c6c8b88f0`  |
| 1579   | No file              | `9a6c6c8b88f0`  |
| 1572   | No file              | `9a6c6c8b88f0`  |
| 1565   | No file              | `9a6c6c8b88f0`  |
| 1559   | No file              | `9a6c6c8b88f0`  |
| 1554   | No file              | `9a6c6c8b88f0`  |
| 1547   | No file              | `9a6c6c8b88f0`  |
| 1537   | No file              | `9a6c6c8b88f0`  |
| 1529   | No file              | `9a6c6c8b88f0`  |
| 1524   | No file              | `9a6c6c8b88f0`  |
| 1519   | No file              | `9a6c6c8b88f0`  |
| 1509   | No file              | `9a6c6c8b88f0`  |
| 1506   | No file              | `9a6c6c8b88f0`  |
| 1504   | No file              | `9a6c6c8b88f0`  |
| 1500   | No file              | `9a6c6c8b88f0`  |
| 1493   | No file              | `9a6c6c8b88f0`  |
| 1489   | No file              | `9a6c6c8b88f0`  |
| 1485   | No file              | `9a6c6c8b88f0`  |
| 1481   | No file              | `9a6c6c8b88f0`  |
| 1474   | No file              | `9a6c6c8b88f0`  |
| 1466   | No file              | `9a6c6c8b88f0`  |
| 1462   | No file              | `9a6c6c8b88f0`  |
| 1459   | No file              | `9a6c6c8b88f0`  |
| 1453   | No file              | `9a6c6c8b88f0`  |
| 1450   | No file              | `9a6c6c8b88f0`  |
| 1445   | No file              | `9a6c6c8b88f0`  |
| 1439   | No file              | `9a6c6c8b88f0`  |
| 1433   | No file              | `9a6c6c8b88f0`  |
| 1430   | No file              | `9a6c6c8b88f0`  |
| 1426   | No file              | `9a6c6c8b88f0`  |
| 1421   | No file              | `9a6c6c8b88f0`  |
| 1417   | No file              | `9a6c6c8b88f0`  |
| 1416   | No file              | `9a6c6c8b88f0`  |
| 1409   | No file              | `9a6c6c8b88f0`  |
| 1405   | No file              | `9a6c6c8b88f0`  |
| 1401   | No file              | `9a6c6c8b88f0`  |
| 1396   | No file              | `9a6c6c8b88f0`  |
| 1391   | No file              | `9a6c6c8b88f0`  |
| 1390   | No file              | `9a6c6c8b88f0`  |
| 1386   | No file              | `9a6c6c8b88f0`  |
| 1381   | No file              | `9a6c6c8b88f0`  |
| 1379   | No file              | `9a6c6c8b88f0`  |
| 1372   | No file              | `9a6c6c8b88f0`  |
| 1366   | No file              | `9a6c6c8b88f0`  |
| 1364   | No file              | `9a6c6c8b88f0`  |
| 1363   | No file              | `9a6c6c8b88f0`  |
| 1360   | No file              | `9a6c6c8b88f0`  |
| 1358   | No file              | `9a6c6c8b88f0`  |
| 1355   | No file              | `9a6c6c8b88f0`  |
| 1351   | No file              | `9a6c6c8b88f0`  |
| 1348   | No file              | `9a6c6c8b88f0`  |
| 1346   | No file              | `9a6c6c8b88f0`  |
| 1341   | No file              | `9a6c6c8b88f0`  |
| 1340   | No file              | `9a6c6c8b88f0`  |
| 1338   | No file              | `9a6c6c8b88f0`  |
| 1335   | No file              | `9a6c6c8b88f0`  |
| 1333   | No file              | `9a6c6c8b88f0`  |
| 1329   | No file              | `9a6c6c8b88f0`  |
| 1327   | No file              | `9a6c6c8b88f0`  |
| 1324   | No file              | `9a6c6c8b88f0`  |
| 1321   | No file              | `9a6c6c8b88f0`  |
| 1319   | No file              | `9a6c6c8b88f0`  |
| 1318   | No file              | `9a6c6c8b88f0`  |
| 1316   | No file              | `9a6c6c8b88f0`  |
| 1313   | No file              | `9a6c6c8b88f0`  |
| 1311   | No file              | `9a6c6c8b88f0`  |
| 1309   | No file              | `9a6c6c8b88f0`  |
| 1304   | No file              | `9a6c6c8b88f0`  |
| 1292   | No file              | `9a6c6c8b88f0`  |
| 1286   | No file              | `9a6c6c8b88f0`  |
| 1280   | No file              | `9a6c6c8b88f0`  |
| 1276   | No file              | `9a6c6c8b88f0`  |
| 1267   | No file              | `9a6c6c8b88f0`  |
| 1261   | No file              | `9a6c6c8b88f0`  |
| 1256   | No file              | `9a6c6c8b88f0`  |
| 1250   | No file              | `9a6c6c8b88f0`  |
| 1246   | No file              | `9a6c6c8b88f0`  |
| 1239   | No file              | `9a6c6c8b88f0`  |
| 1230   | No file              | `9a6c6c8b88f0`  |
| 1226   | No file              | `9a6c6c8b88f0`  |
| 1220   | No file              | `9a6c6c8b88f0`  |
| 1217   | No file              | `9a6c6c8b88f0`  |
| 1211   | No file              | `9a6c6c8b88f0`  |
| 1210   | No file              | `9a6c6c8b88f0`  |
| 1208   | No file              | `9a6c6c8b88f0`  |
| 1203   | No file              | `9a6c6c8b88f0`  |
| 1197   | No file              | `9a6c6c8b88f0`  |
| 1194   | No file              | `9a6c6c8b88f0`  |
| 1192   | No file              | `9a6c6c8b88f0`  |
| 1187   | No file              | `9a6c6c8b88f0`  |
| 1183   | No file              | `9a6c6c8b88f0`  |
| 1177   | No file              | `9a6c6c8b88f0`  |
| 1173   | No file              | `9a6c6c8b88f0`  |
| 1167   | No file              | `9a6c6c8b88f0`  |
| 1164   | No file              | `9a6c6c8b88f0`  |
| 1156   | No file              | `9a6c6c8b88f0`  |
| 1149   | No file              | `9a6c6c8b88f0`  |
| 1144   | No file              | `9a6c6c8b88f0`  |
| 1137   | No file              | `9a6c6c8b88f0`  |
| 1132   | No file              | `9a6c6c8b88f0`  |
| 1127   | No file              | `9a6c6c8b88f0`  |
| 1122   | No file              | `9a6c6c8b88f0`  |
| 1118   | No file              | `9a6c6c8b88f0`  |
| 1114   | No file              | `9a6c6c8b88f0`  |
| 1109   | No file              | `9a6c6c8b88f0`  |
| 1102   | No file              | `9a6c6c8b88f0`  |
| 1096   | No file              | `9a6c6c8b88f0`  |
| 1088   | No file              | `9a6c6c8b88f0`  |
| 1081   | No file              | `9a6c6c8b88f0`  |
| 1076   | No file              | `9a6c6c8b88f0`  |
| 1069   | No file              | `9a6c6c8b88f0`  |
| 1064   | No file              | `9a6c6c8b88f0`  |
| 1058   | No file              | `9a6c6c8b88f0`  |
| 1051   | No file              | `9a6c6c8b88f0`  |
| 1044   | No file              | `9a6c6c8b88f0`  |
| 1036   | No file              | `9a6c6c8b88f0`  |
| 1026   | No file              | `9a6c6c8b88f0`  |
| 1016   | No file              | `9a6c6c8b88f0`  |
| 1009   | No file              | `9a6c6c8b88f0`  |
| 1005   | No file              | `9a6c6c8b88f0`  |
| 1000   | No file              | `9a6c6c8b88f0`  |
| 998    | No file              | `9a6c6c8b88f0`  |
| 990    | No file              | `9a6c6c8b88f0`  |
| 979    | No file              | `9a6c6c8b88f0`  |
| 972    | No file              | `9a6c6c8b88f0`  |
| 963    | No file              | `9a6c6c8b88f0`  |
| 955    | No file              | `9a6c6c8b88f0`  |
| 946    | No file              | `9a6c6c8b88f0`  |
| 938    | No file              | `9a6c6c8b88f0`  |
| 927    | No file              | `9a6c6c8b88f0`  |
| 911    | No file              | `9a6c6c8b88f0`  |
| 904    | No file              | `9a6c6c8b88f0`  |
| 899    | No file              | `9a6c6c8b88f0`  |
| 894    | No file              | `9a6c6c8b88f0`  |
| 885    | No file              | `9a6c6c8b88f0`  |
| 879    | No file              | `9a6c6c8b88f0`  |
| 872    | No file              | `9a6c6c8b88f0`  |
| 864    | No file              | `9a6c6c8b88f0`  |
| 855    | No file              | `9a6c6c8b88f0`  |
| 853    | No file              | `9a6c6c8b88f0`  |
| 845    | No file              | `9a6c6c8b88f0`  |
| 837    | No file              | `9a6c6c8b88f0`  |
| 829    | No file              | `9a6c6c8b88f0`  |
| 822    | No file              | `9a6c6c8b88f0`  |
| 814    | No file              | `9a6c6c8b88f0`  |
| 805    | No file              | `9a6c6c8b88f0`  |
| 794    | No file              | `9a6c6c8b88f0`  |
| 787    | No file              | `9a6c6c8b88f0`  |
| 780    | No file              | `9a6c6c8b88f0`  |
| 771    | No file              | `9a6c6c8b88f0`  |
| 760    | No file              | `9a6c6c8b88f0`  |
| 748    | No file              | `9a6c6c8b88f0`  |
| 741    | No file              | `9a6c6c8b88f0`  |
| 736    | No file              | `9a6c6c8b88f0`  |
| 731    | No file              | `9a6c6c8b88f0`  |
| 723    | No file              | `9a6c6c8b88f0`  |
| 711    | No file              | `9a6c6c8b88f0`  |
| 707    | No file              | `9a6c6c8b88f0`  |
| 697    | No file              | `9a6c6c8b88f0`  |
| 689    | No file              | `9a6c6c8b88f0`  |
| 683    | No file              | `9a6c6c8b88f0`  |
| 678    | No file              | `9a6c6c8b88f0`  |
| 670    | No file              | `9a6c6c8b88f0`  |
| 661    | No file              | `9a6c6c8b88f0`  |
| 656    | No file              | `9a6c6c8b88f0`  |
| 652    | No file              | `9a6c6c8b88f0`  |
| 643    | No file              | `9a6c6c8b88f0`  |
| 637    | No file              | `9a6c6c8b88f0`  |
| 630    | No file              | `9a6c6c8b88f0`  |
| 627    | No file              | `9a6c6c8b88f0`  |
| 621    | No file              | `9a6c6c8b88f0`  |
| 617    | No file              | `9a6c6c8b88f0`  |
| 615    | No file              | `9a6c6c8b88f0`  |
| 606    | No file              | `9a6c6c8b88f0`  |
| 599    | No file              | `9a6c6c8b88f0`  |
| 592    | No file              | `9a6c6c8b88f0`  |
| 586    | No file              | `9a6c6c8b88f0`  |
| 577    | No file              | `9a6c6c8b88f0`  |
| 569    | No file              | `9a6c6c8b88f0`  |
| 561    | No file              | `9a6c6c8b88f0`  |
| 554    | No file              | `9a6c6c8b88f0`  |
| 542    | No file              | `9a6c6c8b88f0`  |
| 532    | No file              | `9a6c6c8b88f0`  |
| 531    | No file              | `9a6c6c8b88f0`  |
| 526    | No file              | `9a6c6c8b88f0`  |
| 521    | No file              | `9a6c6c8b88f0`  |
| 517    | No file              | `9a6c6c8b88f0`  |
| 510    | No file              | `9a6c6c8b88f0`  |
| 508    | No file              | `9a6c6c8b88f0`  |
| 504    | No file              | `9a6c6c8b88f0`  |
| 497    | No file              | `9a6c6c8b88f0`  |
| 491    | No file              | `9a6c6c8b88f0`  |
| 485    | No file              | `9a6c6c8b88f0`  |
| 478    | No file              | `9a6c6c8b88f0`  |
| 472    | No file              | `9a6c6c8b88f0`  |
| 466    | No file              | `9a6c6c8b88f0`  |
| 457    | No file              | `9a6c6c8b88f0`  |
| 452    | No file              | `9a6c6c8b88f0`  |
| 449    | No file              | `9a6c6c8b88f0`  |
| 435    | No file              | `9a6c6c8b88f0`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                           |
| --------------------- | -------- | -------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Character (type 6), region (type 17) and item (type 0) names   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                     | Field                         | Notes                                                       |
| ------------------- | ------------------------ | ----------------------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]                  | magic                         | ASCII `PABR`                                                |
| `+0x04`             | u64                      | unknown_04                    | `5,000,000,000` (client 3474); `10,000,000,000` on 3002     |
| `+0x0C`             | u64                      | unknown_0c                    | `500,000,000`                                               |
| `+0x14`             | u32                      | unknown_14                    | `400`                                                       |
| `+0x18`             | u32                      | unknown_18                    | `5`                                                         |
| `+0x1C`             | u32                      | unknown_1c                    | `6000`                                                      |
| `+0x20`             | u32                      | unknown_20                    | `20000`                                                     |
| `+0x24`             | u32                      | unknown_24                    | `60000`                                                     |
| `+0x28`             | u32                      | unknown_28                    | `3500`                                                      |
| `+0x2C`             | u32                      | unknown_2c                    | `100000`                                                    |
| `+0x30`             | u32                      | unknown_30                    | `10`                                                        |
| `+0x34`             | u32                      | unknown_34                    | `600`                                                       |
| `+0x38`             | u32                      | unknown_38                    | `40`                                                        |
| `+0x3C`             | u32                      | unknown_3c                    | `100`                                                       |
| `+0x40`             | u32                      | unknown_40                    | `1800`                                                      |
| `+0x44`             | f32                      | unknown_44                    | `700.0`                                                     |
| `+0x48`             | u32                      | unknown_48                    | `20` (client 3474); `30` on 3002                            |
| `+0x4C`             | u32                      | unknown_4c                    | `40`; `20` on 3002                                          |
| `+0x50`             | u32                      | unknown_50                    | `30`; `45` on 3002                                          |
| `+0x54`             | u32                      | unknown_54                    | `100`                                                       |
| `+0x58`             | u16                      | kamasylvia_boss_character_key | `21871` Narchillan (LOC type 6)                             |
| `+0x5A`             | u16                      | odyllita_boss_character_key   | `21872` Sephir                                              |
| `+0x5C`             | u32                      | unknown_5c                    | `10`                                                        |
| `+0x60`             | u32                      | unknown_60                    | `600`                                                       |
| `+0x64`             | u32                      | unknown_64                    | `600`                                                       |
| `+0x68`             | u32                      | unknown_68                    | `60`                                                        |
| `+0x6C`             | u32                      | unknown_6c                    | `10`                                                        |
| `+0x70`             | u32                      | unknown_70                    | `5`                                                         |
| `+0x74`             | u32                      | unknown_74                    | `15`                                                        |
| `+0x78`             | u16                      | kamasylvia_region_key         | `735` Grána (LOC type 17)                                   |
| `+0x7A`             | u16                      | odyllita_region_key           | `955` O'draxxia                                             |
| `+0x7C`             | u32                      | unknown_7c                    | `2700` (client 3474); `900` on 3002                         |
| `+0x80`             | u32                      | unknown_80                    | `300`                                                       |
| `+0x84`             | u32                      | region_count                  | Number of `region_keys`                                     |
| `+0x88`             | u16[region_count]        | region_keys                   | `regioninfo.bss` keys; see Regions                          |
| `region_keys+0x00`  | u32                      | item_id                       | `761066` Medal of Sylvia (LOC type 0)                       |
| `region_keys+0x04`  | u32                      | schedule_count                | Number of `schedules`; `2` on every client checked          |
| `region_keys+0x08`  | Schedule[schedule_count] | schedules                     | See Schedule                                                |
| `schedules+0x00`    | String Table             | string_table                  | See String Table                                            |
| `string_table+0x00` | u32                      | table_start                   | Offset of the string table, where `schedules` ends          |
| `string_table+0x04` | u32                      | zero                          | Always `0`                                                  |

### Schedule (97 bytes)

| Offset  | Type    | Field      | Notes                                         |
| ------- | ------- | ---------- | --------------------------------------------- |
| `+0x00` | u8      | unknown_00 | `0` and `1`, one per schedule                 |
| `+0x01` | Time[8] | times      | See Time and Schedules                        |

### Time (12 bytes)

| Offset  | Type | Field       | Notes                       |
| ------- | ---- | ----------- | --------------------------- |
| `+0x00` | u32  | day_of_week | `0` to `6`                  |
| `+0x04` | u32  | hour        | `0` to `23`                 |
| `+0x08` | u32  | minute      | `0` to `59`                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Regions

`region_keys` holds 11 keys on clients 3002 to 3474, each a LOC type 17
region name: `703` Lemoria Guard Post, `706` Old Wisdom Tree, `724`
Kamasylvia Castle, `727` Acher Guard Post, `735` Grána, `955` O'draxxia,
`956` O'dyllita Castle, `961` Bahit Sanctum, `966` Starry Midnight Port,
`1024` Mountain of Division and `1028` Dead Moon Post. Both team home
regions are in the list.

## Schedules

The eight times of each schedule as day, hour and minute (client 3474):

| Time | Schedule `0` | Schedule `1` |
| ---- | ------------ | ------------ |
| 1    | `0` 22:00    | `0` 15:00    |
| 2    | `1` 00:00    | `0` 17:00    |
| 3    | `6` 06:00    | `5` 23:00    |
| 4    | `0` 06:10    | `6` 23:10    |
| 5    | `0` 06:10    | `6` 23:10    |
| 6    | `0` 20:05    | `0` 13:05    |
| 7    | `0` 20:05    | `0` 13:05    |
| 8    | `0` 22:00    | `0` 15:00    |

Each time of schedule `1` is the same time of schedule `0` moved back 7
hours, across the day line where it falls before midnight; on client 3251
the shift is 6 hours (`0` 16:00 for time 1). The two schedules read as one
war calendar in two time zones. The client Lua names the war states
`__eRoseWar_GuildApplying`, `_GuildStopApplying`, `_MercenaryApplying`,
`_MercenaryStopApplying`, `_PreStart`, `_Start` and `_Stop` (plus
`_Count`), but not which time opens which.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. The named fields resolve by
value:

- The two boss keys are LOC type 6 Narchillan and Sephir; the Lua reads a
  team's boss with `ToClient_GetRoseWarBossInfoXXX(roseWarTeamNo)`, and
  [`rosewarteamnostaticstatus.bss`](rosewarteamnostaticstatus_bss.md) puts
  Narchillan's Blessing on team `0` (Kamasylvia) and Sephir's Blessing on
  team `1`.
- The two region keys are the capitals Grána (Kamasylvia) and O'draxxia
  (O'dyllita).
- `item_id` is LOC type 0 Medal of Sylvia.
- `day_of_week`, `hour` and `minute` stay in `0` to `6`, `0` to `23` and
  `0` to `59`, and both schedules shift by whole hours.

## Notes

- The file is 372 bytes on clients 3002, 3251 and 3474; the values that
  differ are in the layout table. The file is not in the archives of
  client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`
  as one row: the bosses, the home regions, the region list, the item and
  each schedule as `<unknown_00>: <day> <hh:mm>, ...`.

## Open Questions

### The Settings

The 25 unnamed u32 settings, the f32 and the two u64 have no name in any
source. The u64 values (`5,000,000,000` and `500,000,000`) read as silver
amounts, and `600`, `1800` and `2700` as seconds, but the menu Lua's
`ToClient_GetRoseWarGuildApplyPoint()`, `ToClient_GetRoseWarReviveTime()`
and `ToClient_GetRoseWarMiniMapDetectDistanceLimitForFierceBattle()`
return them without saying which offset they read.

### The Day Numbers

`day_of_week` runs `0` to `6`, but no source says whether `0` is Sunday or
Monday, or which time zone each schedule follows.
