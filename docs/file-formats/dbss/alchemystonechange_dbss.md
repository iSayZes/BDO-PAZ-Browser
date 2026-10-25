# `alchemystonechange.dbss` Format

## Purpose

The Growth recipes for items that grow into a higher tier: alchemy stones,
Vell's and Khan's Hearts and Behelit's Hearts with Brimming Essence of Aether
at Alchemy Apprentice 1, and Totems of the Sea with a Black Stone at a
Fishing level. A row is the item, its Growth material and count, the life
skill condition as an inline script, and the item it grows into.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                            | Bytes  | Records       | Row bytes |
| ------ | -------------- | ------------------------------- | ------ | ------------- | --------- |
| 2      | 3045 and later | `alchemystonechange.dbss`       | 12,506 | 133 Row       | 94        |
| 2      | 3045 and later | `alchemystonechangeoffset.dbss` | 1,600  | 133 Index Row | 12        |
| 1      | 1346 to 2717   | `alchemystonechange.dbss`       | 13,732 | 176 Row       | 78        |
| 1      | 1346 to 2717   | `alchemystonechangeoffset.dbss` | 2,116  | 176 Index Row | 12        |

| Layout | File                            | Known            | Unknown         |
| ------ | ------------------------------- | ---------------- | --------------- |
| 2      | `alchemystonechange.dbss`       | 8,782 B (70.2%)  | 3,724 B (29.8%) |
| 2      | `alchemystonechangeoffset.dbss` | 1,600 B (100.0%) | 0 B (0.0%)      |
| 1      | `alchemystonechange.dbss`       | 10,916 B (79.5%) | 2,816 B (20.5%) |
| 1      | `alchemystonechangeoffset.dbss` | 2,116 B (100.0%) | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `f3dce9c1fba2`  |
| 3482   | Layout 2             | `f3dce9c1fba2`  |
| 3474   | Layout 2             | `f3dce9c1fba2`  |
| 3473   | Layout 2             | `f3dce9c1fba2`  |
| 3464   | Layout 2             | `f3dce9c1fba2`  |
| 3458   | Layout 2             | `f3dce9c1fba2`  |
| 3454   | Layout 2             | `f3dce9c1fba2`  |
| 3444   | Layout 2             | `f3dce9c1fba2`  |
| 3435   | Layout 2             | `f3dce9c1fba2`  |
| 3426   | Layout 2             | `f3dce9c1fba2`  |
| 3418   | Layout 2             | `f3dce9c1fba2`  |
| 3412   | Layout 2             | `f3dce9c1fba2`  |
| 3402   | Layout 2             | `f3dce9c1fba2`  |
| 3396   | Layout 2             | `f3dce9c1fba2`  |
| 3387   | Layout 2             | `f3dce9c1fba2`  |
| 3381   | Layout 2             | `f3dce9c1fba2`  |
| 3373   | Layout 2             | `f3dce9c1fba2`  |
| 3364   | Layout 2             | `f3dce9c1fba2`  |
| 3356   | Layout 2             | `f3dce9c1fba2`  |
| 3349   | Layout 2             | `f3dce9c1fba2`  |
| 3342   | Layout 2             | `f3dce9c1fba2`  |
| 3335   | Layout 2             | `f3dce9c1fba2`  |
| 3326   | Layout 2             | `f3dce9c1fba2`  |
| 3321   | Layout 2             | `f3dce9c1fba2`  |
| 3314   | Layout 2             | `f3dce9c1fba2`  |
| 3303   | Layout 2             | `f3dce9c1fba2`  |
| 3302   | Layout 2             | `f3dce9c1fba2`  |
| 3293   | Layout 2             | `f3dce9c1fba2`  |
| 3283   | Layout 2             | `f3dce9c1fba2`  |
| 3275   | Layout 2             | `f3dce9c1fba2`  |
| 3267   | Layout 2             | `f3dce9c1fba2`  |
| 3258   | Layout 2             | `f3dce9c1fba2`  |
| 3251   | Layout 2             | `f3dce9c1fba2`  |
| 3242   | Layout 2             | `f3dce9c1fba2`  |
| 3235   | Layout 2             | `f3dce9c1fba2`  |
| 3229   | Layout 2             | `f3dce9c1fba2`  |
| 3212   | Layout 2             | `f3dce9c1fba2`  |
| 3203   | Layout 2             | `f3dce9c1fba2`  |
| 3193   | Layout 2             | `f3dce9c1fba2`  |
| 3186   | Layout 2             | `f3dce9c1fba2`  |
| 3177   | Layout 2             | `f3dce9c1fba2`  |
| 3169   | Layout 2             | `f3dce9c1fba2`  |
| 3158   | Layout 2             | `f3dce9c1fba2`  |
| 3151   | Layout 2             | `f3dce9c1fba2`  |
| 3144   | Layout 2             | `f3dce9c1fba2`  |
| 3133   | Layout 2             | `f3dce9c1fba2`  |
| 3125   | Layout 2             | `f3dce9c1fba2`  |
| 3118   | Layout 2             | `f3dce9c1fba2`  |
| 3111   | Layout 2             | `f3dce9c1fba2`  |
| 3103   | Layout 2             | `f3dce9c1fba2`  |
| 3095   | Layout 2             | `f3dce9c1fba2`  |
| 3086   | Layout 2             | `f3dce9c1fba2`  |
| 3072   | Layout 2             | `f3dce9c1fba2`  |
| 3062   | Layout 2             | `f3dce9c1fba2`  |
| 3052   | Layout 2             | `f3dce9c1fba2`  |
| 3045   | Layout 2             | `f3dce9c1fba2`  |
| 3037   | No documented layout | `f3dce9c1fba2`  |
| 3030   | No documented layout | `f3dce9c1fba2`  |
| 3021   | No documented layout | `f3dce9c1fba2`  |
| 3012   | No documented layout | `f3dce9c1fba2`  |
| 3002   | No documented layout | `f3dce9c1fba2`  |
| 2995   | No documented layout | `f3dce9c1fba2`  |
| 2987   | No documented layout | `f3dce9c1fba2`  |
| 2978   | No documented layout | `f3dce9c1fba2`  |
| 2970   | No documented layout | `f3dce9c1fba2`  |
| 2959   | No documented layout | `f3dce9c1fba2`  |
| 2951   | No documented layout | `f3dce9c1fba2`  |
| 2942   | No documented layout | `f3dce9c1fba2`  |
| 2935   | No documented layout | `f3dce9c1fba2`  |
| 2932   | No documented layout | `f3dce9c1fba2`  |
| 2923   | No documented layout | `f3dce9c1fba2`  |
| 2919   | No documented layout | `f3dce9c1fba2`  |
| 2907   | No documented layout | `f3dce9c1fba2`  |
| 2900   | No documented layout | `f3dce9c1fba2`  |
| 2891   | No documented layout | `f3dce9c1fba2`  |
| 2882   | No documented layout | `f3dce9c1fba2`  |
| 2872   | No documented layout | `f3dce9c1fba2`  |
| 2863   | No documented layout | `f3dce9c1fba2`  |
| 2855   | No documented layout | `f3dce9c1fba2`  |
| 2849   | No documented layout | `f3dce9c1fba2`  |
| 2844   | No documented layout | `f3dce9c1fba2`  |
| 2834   | No documented layout | `f3dce9c1fba2`  |
| 2825   | No documented layout | `f3dce9c1fba2`  |
| 2819   | No documented layout | `f3dce9c1fba2`  |
| 2811   | No documented layout | `f3dce9c1fba2`  |
| 2803   | No documented layout | `f3dce9c1fba2`  |
| 2794   | No documented layout | `f3dce9c1fba2`  |
| 2783   | No documented layout | `f3dce9c1fba2`  |
| 2774   | No documented layout | `f3dce9c1fba2`  |
| 2765   | No documented layout | `f3dce9c1fba2`  |
| 2756   | No documented layout | `f3dce9c1fba2`  |
| 2750   | No documented layout | `f3dce9c1fba2`  |
| 2743   | No documented layout | `f3dce9c1fba2`  |
| 2736   | No documented layout | `f3dce9c1fba2`  |
| 2726   | No documented layout | `f3dce9c1fba2`  |
| 2717   | Layout 1             | `f3dce9c1fba2`  |
| 2709   | Layout 1             | `f3dce9c1fba2`  |
| 2703   | Layout 1             | `f3dce9c1fba2`  |
| 2695   | Layout 1             | `f3dce9c1fba2`  |
| 2684   | Layout 1             | `f3dce9c1fba2`  |
| 2672   | Layout 1             | `f3dce9c1fba2`  |
| 2665   | Layout 1             | `f3dce9c1fba2`  |
| 2657   | Layout 1             | `f3dce9c1fba2`  |
| 2649   | Layout 1             | `f3dce9c1fba2`  |
| 2644   | Layout 1             | `f3dce9c1fba2`  |
| 2637   | Layout 1             | `f3dce9c1fba2`  |
| 2629   | Layout 1             | `f3dce9c1fba2`  |
| 2619   | Layout 1             | `f3dce9c1fba2`  |
| 2612   | Layout 1             | `f3dce9c1fba2`  |
| 2606   | Layout 1             | `f3dce9c1fba2`  |
| 2602   | Layout 1             | `f3dce9c1fba2`  |
| 2601   | Layout 1             | `f3dce9c1fba2`  |
| 2592   | Layout 1             | `f3dce9c1fba2`  |
| 2583   | Layout 1             | `f3dce9c1fba2`  |
| 2575   | Layout 1             | `f3dce9c1fba2`  |
| 2567   | Layout 1             | `f3dce9c1fba2`  |
| 2560   | Layout 1             | `f3dce9c1fba2`  |
| 2553   | Layout 1             | `f3dce9c1fba2`  |
| 2545   | Layout 1             | `f3dce9c1fba2`  |
| 2538   | Layout 1             | `f3dce9c1fba2`  |
| 2529   | Layout 1             | `f3dce9c1fba2`  |
| 2519   | Layout 1             | `f3dce9c1fba2`  |
| 2513   | Layout 1             | `f3dce9c1fba2`  |
| 2510   | Layout 1             | `f3dce9c1fba2`  |
| 2507   | Layout 1             | `f3dce9c1fba2`  |
| 2503   | Layout 1             | `f3dce9c1fba2`  |
| 2498   | Layout 1             | `f3dce9c1fba2`  |
| 2492   | Layout 1             | `f3dce9c1fba2`  |
| 2487   | Layout 1             | `f3dce9c1fba2`  |
| 2480   | Layout 1             | `f3dce9c1fba2`  |
| 2474   | Layout 1             | `f3dce9c1fba2`  |
| 2468   | Layout 1             | `f3dce9c1fba2`  |
| 2460   | Layout 1             | `f3dce9c1fba2`  |
| 2453   | Layout 1             | `f3dce9c1fba2`  |
| 2444   | Layout 1             | `f3dce9c1fba2`  |
| 2438   | Layout 1             | `f3dce9c1fba2`  |
| 2434   | Layout 1             | `f3dce9c1fba2`  |
| 2429   | Layout 1             | `f3dce9c1fba2`  |
| 2421   | Layout 1             | `f3dce9c1fba2`  |
| 2414   | Layout 1             | `f3dce9c1fba2`  |
| 2407   | Layout 1             | `f3dce9c1fba2`  |
| 2401   | Layout 1             | `f3dce9c1fba2`  |
| 2397   | Layout 1             | `f3dce9c1fba2`  |
| 2393   | Layout 1             | `f3dce9c1fba2`  |
| 2384   | Layout 1             | `f3dce9c1fba2`  |
| 2378   | Layout 1             | `f3dce9c1fba2`  |
| 2372   | Layout 1             | `f3dce9c1fba2`  |
| 2358   | Layout 1             | `f3dce9c1fba2`  |
| 2352   | Layout 1             | `f3dce9c1fba2`  |
| 2347   | Layout 1             | `f3dce9c1fba2`  |
| 2343   | Layout 1             | `f3dce9c1fba2`  |
| 2335   | Layout 1             | `f3dce9c1fba2`  |
| 2327   | Layout 1             | `f3dce9c1fba2`  |
| 2324   | Layout 1             | `f3dce9c1fba2`  |
| 2319   | Layout 1             | `f3dce9c1fba2`  |
| 2313   | Layout 1             | `f3dce9c1fba2`  |
| 2308   | Layout 1             | `f3dce9c1fba2`  |
| 2302   | Layout 1             | `f3dce9c1fba2`  |
| 2295   | Layout 1             | `f3dce9c1fba2`  |
| 2290   | Layout 1             | `f3dce9c1fba2`  |
| 2284   | Layout 1             | `f3dce9c1fba2`  |
| 2276   | Layout 1             | `f3dce9c1fba2`  |
| 2269   | Layout 1             | `f3dce9c1fba2`  |
| 2259   | Layout 1             | `f3dce9c1fba2`  |
| 2250   | Layout 1             | `f3dce9c1fba2`  |
| 2243   | Layout 1             | `f3dce9c1fba2`  |
| 2235   | Layout 1             | `f3dce9c1fba2`  |
| 2229   | Layout 1             | `f3dce9c1fba2`  |
| 2224   | Layout 1             | `f3dce9c1fba2`  |
| 2218   | Layout 1             | `f3dce9c1fba2`  |
| 2215   | Layout 1             | `f3dce9c1fba2`  |
| 2207   | Layout 1             | `f3dce9c1fba2`  |
| 2203   | Layout 1             | `f3dce9c1fba2`  |
| 2196   | Layout 1             | `f3dce9c1fba2`  |
| 2192   | Layout 1             | `f3dce9c1fba2`  |
| 2189   | Layout 1             | `f3dce9c1fba2`  |
| 2183   | Layout 1             | `f3dce9c1fba2`  |
| 2179   | Layout 1             | `f3dce9c1fba2`  |
| 2171   | Layout 1             | `f3dce9c1fba2`  |
| 2163   | Layout 1             | `f3dce9c1fba2`  |
| 2156   | Layout 1             | `f3dce9c1fba2`  |
| 2151   | Layout 1             | `f3dce9c1fba2`  |
| 2147   | Layout 1             | `f3dce9c1fba2`  |
| 2142   | Layout 1             | `f3dce9c1fba2`  |
| 2138   | Layout 1             | `f3dce9c1fba2`  |
| 2134   | Layout 1             | `f3dce9c1fba2`  |
| 2130   | Layout 1             | `f3dce9c1fba2`  |
| 2122   | Layout 1             | `f3dce9c1fba2`  |
| 2107   | Layout 1             | `f3dce9c1fba2`  |
| 2098   | Layout 1             | `f3dce9c1fba2`  |
| 2089   | Layout 1             | `f3dce9c1fba2`  |
| 2081   | Layout 1             | `f3dce9c1fba2`  |
| 2073   | Layout 1             | `f3dce9c1fba2`  |
| 2067   | Layout 1             | `f3dce9c1fba2`  |
| 2063   | Layout 1             | `f3dce9c1fba2`  |
| 2059   | Layout 1             | `f3dce9c1fba2`  |
| 2052   | Layout 1             | `f3dce9c1fba2`  |
| 2044   | Layout 1             | `f3dce9c1fba2`  |
| 2039   | Layout 1             | `f3dce9c1fba2`  |
| 2032   | Layout 1             | `f3dce9c1fba2`  |
| 2025   | Layout 1             | `f3dce9c1fba2`  |
| 2011   | Layout 1             | `f3dce9c1fba2`  |
| 2005   | Layout 1             | `f3dce9c1fba2`  |
| 2000   | Layout 1             | `f3dce9c1fba2`  |
| 1996   | Layout 1             | `f3dce9c1fba2`  |
| 1991   | Layout 1             | `f3dce9c1fba2`  |
| 1985   | Layout 1             | `f3dce9c1fba2`  |
| 1980   | Layout 1             | `f3dce9c1fba2`  |
| 1969   | Layout 1             | `f3dce9c1fba2`  |
| 1964   | Layout 1             | `f3dce9c1fba2`  |
| 1958   | Layout 1             | `f3dce9c1fba2`  |
| 1950   | Layout 1             | `f3dce9c1fba2`  |
| 1945   | Layout 1             | `f3dce9c1fba2`  |
| 1937   | Layout 1             | `f3dce9c1fba2`  |
| 1933   | Layout 1             | `f3dce9c1fba2`  |
| 1927   | Layout 1             | `f3dce9c1fba2`  |
| 1921   | Layout 1             | `f3dce9c1fba2`  |
| 1914   | Layout 1             | `f3dce9c1fba2`  |
| 1908   | Layout 1             | `f3dce9c1fba2`  |
| 1897   | Layout 1             | `f3dce9c1fba2`  |
| 1892   | Layout 1             | `f3dce9c1fba2`  |
| 1886   | Layout 1             | `f3dce9c1fba2`  |
| 1881   | Layout 1             | `f3dce9c1fba2`  |
| 1871   | Layout 1             | `f3dce9c1fba2`  |
| 1866   | Layout 1             | `f3dce9c1fba2`  |
| 1862   | Layout 1             | `f3dce9c1fba2`  |
| 1854   | Layout 1             | `f3dce9c1fba2`  |
| 1846   | Layout 1             | `f3dce9c1fba2`  |
| 1838   | Layout 1             | `f3dce9c1fba2`  |
| 1832   | Layout 1             | `f3dce9c1fba2`  |
| 1826   | Layout 1             | `f3dce9c1fba2`  |
| 1822   | Layout 1             | `f3dce9c1fba2`  |
| 1818   | Layout 1             | `f3dce9c1fba2`  |
| 1804   | Layout 1             | `f3dce9c1fba2`  |
| 1794   | Layout 1             | `f3dce9c1fba2`  |
| 1790   | Layout 1             | `f3dce9c1fba2`  |
| 1784   | Layout 1             | `f3dce9c1fba2`  |
| 1774   | Layout 1             | `f3dce9c1fba2`  |
| 1771   | Layout 1             | `f3dce9c1fba2`  |
| 1762   | Layout 1             | `f3dce9c1fba2`  |
| 1759   | Layout 1             | `f3dce9c1fba2`  |
| 1754   | Layout 1             | `f3dce9c1fba2`  |
| 1749   | Layout 1             | `f3dce9c1fba2`  |
| 1743   | Layout 1             | `f3dce9c1fba2`  |
| 1737   | Layout 1             | `f3dce9c1fba2`  |
| 1731   | Layout 1             | `f3dce9c1fba2`  |
| 1725   | Layout 1             | `f3dce9c1fba2`  |
| 1717   | Layout 1             | `f3dce9c1fba2`  |
| 1710   | Layout 1             | `f3dce9c1fba2`  |
| 1704   | Layout 1             | `f3dce9c1fba2`  |
| 1698   | Layout 1             | `f3dce9c1fba2`  |
| 1690   | Layout 1             | `f3dce9c1fba2`  |
| 1685   | Layout 1             | `f3dce9c1fba2`  |
| 1680   | Layout 1             | `f3dce9c1fba2`  |
| 1674   | Layout 1             | `f3dce9c1fba2`  |
| 1668   | Layout 1             | `f3dce9c1fba2`  |
| 1659   | Layout 1             | `f3dce9c1fba2`  |
| 1649   | Layout 1             | `f3dce9c1fba2`  |
| 1642   | Layout 1             | `f3dce9c1fba2`  |
| 1636   | Layout 1             | `f3dce9c1fba2`  |
| 1628   | Layout 1             | `f3dce9c1fba2`  |
| 1622   | Layout 1             | `f3dce9c1fba2`  |
| 1614   | Layout 1             | `f3dce9c1fba2`  |
| 1608   | Layout 1             | `f3dce9c1fba2`  |
| 1602   | Layout 1             | `f3dce9c1fba2`  |
| 1598   | Layout 1             | `f3dce9c1fba2`  |
| 1594   | Layout 1             | `f3dce9c1fba2`  |
| 1590   | Layout 1             | `f3dce9c1fba2`  |
| 1587   | Layout 1             | `f3dce9c1fba2`  |
| 1584   | Layout 1             | `f3dce9c1fba2`  |
| 1579   | Layout 1             | `f3dce9c1fba2`  |
| 1572   | Layout 1             | `f3dce9c1fba2`  |
| 1565   | Layout 1             | `f3dce9c1fba2`  |
| 1559   | Layout 1             | `f3dce9c1fba2`  |
| 1554   | Layout 1             | `f3dce9c1fba2`  |
| 1547   | Layout 1             | `f3dce9c1fba2`  |
| 1537   | Layout 1             | `f3dce9c1fba2`  |
| 1529   | Layout 1             | `f3dce9c1fba2`  |
| 1524   | Layout 1             | `f3dce9c1fba2`  |
| 1519   | Layout 1             | `f3dce9c1fba2`  |
| 1509   | Layout 1             | `f3dce9c1fba2`  |
| 1506   | Layout 1             | `f3dce9c1fba2`  |
| 1504   | Layout 1             | `f3dce9c1fba2`  |
| 1500   | Layout 1             | `f3dce9c1fba2`  |
| 1493   | Layout 1             | `f3dce9c1fba2`  |
| 1489   | Layout 1             | `f3dce9c1fba2`  |
| 1485   | Layout 1             | `f3dce9c1fba2`  |
| 1481   | Layout 1             | `f3dce9c1fba2`  |
| 1474   | Layout 1             | `f3dce9c1fba2`  |
| 1466   | Layout 1             | `f3dce9c1fba2`  |
| 1462   | Layout 1             | `f3dce9c1fba2`  |
| 1459   | Layout 1             | `f3dce9c1fba2`  |
| 1453   | Layout 1             | `f3dce9c1fba2`  |
| 1450   | Layout 1             | `f3dce9c1fba2`  |
| 1445   | Layout 1             | `f3dce9c1fba2`  |
| 1439   | Layout 1             | `f3dce9c1fba2`  |
| 1433   | Layout 1             | `f3dce9c1fba2`  |
| 1430   | Layout 1             | `f3dce9c1fba2`  |
| 1426   | Layout 1             | `f3dce9c1fba2`  |
| 1421   | Layout 1             | `f3dce9c1fba2`  |
| 1417   | Layout 1             | `f3dce9c1fba2`  |
| 1416   | Layout 1             | `f3dce9c1fba2`  |
| 1409   | Layout 1             | `f3dce9c1fba2`  |
| 1405   | Layout 1             | `f3dce9c1fba2`  |
| 1401   | Layout 1             | `f3dce9c1fba2`  |
| 1396   | Layout 1             | `f3dce9c1fba2`  |
| 1391   | Layout 1             | `f3dce9c1fba2`  |
| 1390   | Layout 1             | `f3dce9c1fba2`  |
| 1386   | Layout 1             | `f3dce9c1fba2`  |
| 1381   | Layout 1             | `f3dce9c1fba2`  |
| 1379   | Layout 1             | `f3dce9c1fba2`  |
| 1372   | Layout 1             | `f3dce9c1fba2`  |
| 1366   | Layout 1             | `f3dce9c1fba2`  |
| 1364   | Layout 1             | `f3dce9c1fba2`  |
| 1363   | Layout 1             | `f3dce9c1fba2`  |
| 1360   | Layout 1             | `f3dce9c1fba2`  |
| 1358   | Layout 1             | `f3dce9c1fba2`  |
| 1355   | Layout 1             | `f3dce9c1fba2`  |
| 1351   | Layout 1             | `f3dce9c1fba2`  |
| 1348   | Layout 1             | `f3dce9c1fba2`  |
| 1346   | Layout 1             | `f3dce9c1fba2`  |
| 1341   | No documented layout | `f3dce9c1fba2`  |
| 1340   | No documented layout | `f3dce9c1fba2`  |
| 1338   | No documented layout | `f3dce9c1fba2`  |
| 1335   | No documented layout | `f3dce9c1fba2`  |
| 1333   | No documented layout | `f3dce9c1fba2`  |
| 1329   | No documented layout | `f3dce9c1fba2`  |
| 1327   | No documented layout | `f3dce9c1fba2`  |
| 1324   | No documented layout | `f3dce9c1fba2`  |
| 1321   | No documented layout | `f3dce9c1fba2`  |
| 1319   | No documented layout | `f3dce9c1fba2`  |
| 1318   | No documented layout | `f3dce9c1fba2`  |
| 1316   | No documented layout | `f3dce9c1fba2`  |
| 1313   | No documented layout | `f3dce9c1fba2`  |
| 1311   | No documented layout | `f3dce9c1fba2`  |
| 1309   | No documented layout | `f3dce9c1fba2`  |
| 1304   | No documented layout | `f3dce9c1fba2`  |
| 1292   | No documented layout | `f3dce9c1fba2`  |
| 1286   | No documented layout | `f3dce9c1fba2`  |
| 1280   | No documented layout | `f3dce9c1fba2`  |
| 1276   | No documented layout | `f3dce9c1fba2`  |
| 1267   | No documented layout | `f3dce9c1fba2`  |
| 1261   | No documented layout | `f3dce9c1fba2`  |
| 1256   | No documented layout | `f3dce9c1fba2`  |
| 1250   | No file              | `f3dce9c1fba2`  |
| 1246   | No file              | `f3dce9c1fba2`  |
| 1239   | No file              | `f3dce9c1fba2`  |
| 1230   | No file              | `f3dce9c1fba2`  |
| 1226   | No file              | `f3dce9c1fba2`  |
| 1220   | No file              | `f3dce9c1fba2`  |
| 1217   | No file              | `f3dce9c1fba2`  |
| 1211   | No file              | `f3dce9c1fba2`  |
| 1210   | No file              | `f3dce9c1fba2`  |
| 1208   | No file              | `f3dce9c1fba2`  |
| 1203   | No file              | `f3dce9c1fba2`  |
| 1197   | No file              | `f3dce9c1fba2`  |
| 1194   | No file              | `f3dce9c1fba2`  |
| 1192   | No file              | `f3dce9c1fba2`  |
| 1187   | No file              | `f3dce9c1fba2`  |
| 1183   | No file              | `f3dce9c1fba2`  |
| 1177   | No file              | `f3dce9c1fba2`  |
| 1173   | No file              | `f3dce9c1fba2`  |
| 1167   | No file              | `f3dce9c1fba2`  |
| 1164   | No file              | `f3dce9c1fba2`  |
| 1156   | No file              | `f3dce9c1fba2`  |
| 1149   | No file              | `f3dce9c1fba2`  |
| 1144   | No file              | `f3dce9c1fba2`  |
| 1137   | No file              | `f3dce9c1fba2`  |
| 1132   | No file              | `f3dce9c1fba2`  |
| 1127   | No file              | `f3dce9c1fba2`  |
| 1122   | No file              | `f3dce9c1fba2`  |
| 1118   | No file              | `f3dce9c1fba2`  |
| 1114   | No file              | `f3dce9c1fba2`  |
| 1109   | No file              | `f3dce9c1fba2`  |
| 1102   | No file              | `f3dce9c1fba2`  |
| 1096   | No file              | `f3dce9c1fba2`  |
| 1088   | No file              | `f3dce9c1fba2`  |
| 1081   | No file              | `f3dce9c1fba2`  |
| 1076   | No file              | `f3dce9c1fba2`  |
| 1069   | No file              | `f3dce9c1fba2`  |
| 1064   | No file              | `f3dce9c1fba2`  |
| 1058   | No file              | `f3dce9c1fba2`  |
| 1051   | No file              | `f3dce9c1fba2`  |
| 1044   | No file              | `f3dce9c1fba2`  |
| 1036   | No file              | `f3dce9c1fba2`  |
| 1026   | No file              | `f3dce9c1fba2`  |
| 1016   | No file              | `f3dce9c1fba2`  |
| 1009   | No file              | `f3dce9c1fba2`  |
| 1005   | No file              | `f3dce9c1fba2`  |
| 1000   | No file              | `f3dce9c1fba2`  |
| 998    | No file              | `f3dce9c1fba2`  |
| 990    | No file              | `f3dce9c1fba2`  |
| 979    | No file              | `f3dce9c1fba2`  |
| 972    | No file              | `f3dce9c1fba2`  |
| 963    | No file              | `f3dce9c1fba2`  |
| 955    | No file              | `f3dce9c1fba2`  |
| 946    | No file              | `f3dce9c1fba2`  |
| 938    | No file              | `f3dce9c1fba2`  |
| 927    | No file              | `f3dce9c1fba2`  |
| 911    | No file              | `f3dce9c1fba2`  |
| 904    | No file              | `f3dce9c1fba2`  |
| 899    | No file              | `f3dce9c1fba2`  |
| 894    | No file              | `f3dce9c1fba2`  |
| 885    | No file              | `f3dce9c1fba2`  |
| 879    | No file              | `f3dce9c1fba2`  |
| 872    | No file              | `f3dce9c1fba2`  |
| 864    | No file              | `f3dce9c1fba2`  |
| 855    | No file              | `f3dce9c1fba2`  |
| 853    | No file              | `f3dce9c1fba2`  |
| 845    | No file              | `f3dce9c1fba2`  |
| 837    | No file              | `f3dce9c1fba2`  |
| 829    | No file              | `f3dce9c1fba2`  |
| 822    | No file              | `f3dce9c1fba2`  |
| 814    | No file              | `f3dce9c1fba2`  |
| 805    | No file              | `f3dce9c1fba2`  |
| 794    | No file              | `f3dce9c1fba2`  |
| 787    | No file              | `f3dce9c1fba2`  |
| 780    | No file              | `f3dce9c1fba2`  |
| 771    | No file              | `f3dce9c1fba2`  |
| 760    | No file              | `f3dce9c1fba2`  |
| 748    | No file              | `f3dce9c1fba2`  |
| 741    | No file              | `f3dce9c1fba2`  |
| 736    | No file              | `f3dce9c1fba2`  |
| 731    | No file              | `f3dce9c1fba2`  |
| 723    | No file              | `f3dce9c1fba2`  |
| 711    | No file              | `f3dce9c1fba2`  |
| 707    | No file              | `f3dce9c1fba2`  |
| 697    | No file              | `f3dce9c1fba2`  |
| 689    | No file              | `f3dce9c1fba2`  |
| 683    | No file              | `f3dce9c1fba2`  |
| 678    | No file              | `f3dce9c1fba2`  |
| 670    | No file              | `f3dce9c1fba2`  |
| 661    | No file              | `f3dce9c1fba2`  |
| 656    | No file              | `f3dce9c1fba2`  |
| 652    | No file              | `f3dce9c1fba2`  |
| 643    | No file              | `f3dce9c1fba2`  |
| 637    | No file              | `f3dce9c1fba2`  |
| 630    | No file              | `f3dce9c1fba2`  |
| 627    | No file              | `f3dce9c1fba2`  |
| 621    | No file              | `f3dce9c1fba2`  |
| 617    | No file              | `f3dce9c1fba2`  |
| 615    | No file              | `f3dce9c1fba2`  |
| 606    | No file              | `f3dce9c1fba2`  |
| 599    | No file              | `f3dce9c1fba2`  |
| 592    | No file              | `f3dce9c1fba2`  |
| 586    | No file              | `f3dce9c1fba2`  |
| 577    | No file              | `f3dce9c1fba2`  |
| 569    | No file              | `f3dce9c1fba2`  |
| 561    | No file              | `f3dce9c1fba2`  |
| 554    | No file              | `f3dce9c1fba2`  |
| 542    | No file              | `f3dce9c1fba2`  |
| 532    | No file              | `f3dce9c1fba2`  |
| 531    | No file              | `f3dce9c1fba2`  |
| 526    | No file              | `f3dce9c1fba2`  |
| 521    | No file              | `f3dce9c1fba2`  |
| 517    | No file              | `f3dce9c1fba2`  |
| 510    | No file              | `f3dce9c1fba2`  |
| 508    | No file              | `f3dce9c1fba2`  |
| 504    | No file              | `f3dce9c1fba2`  |
| 497    | No file              | `f3dce9c1fba2`  |
| 491    | No file              | `f3dce9c1fba2`  |
| 485    | No file              | `f3dce9c1fba2`  |
| 478    | No file              | `f3dce9c1fba2`  |
| 472    | No file              | `f3dce9c1fba2`  |
| 466    | No file              | `f3dce9c1fba2`  |
| 457    | No file              | `f3dce9c1fba2`  |
| 452    | No file              | `f3dce9c1fba2`  |
| 449    | No file              | `f3dce9c1fba2`  |
| 435    | No file              | `f3dce9c1fba2`  |

<!-- versions:end -->

## Companion Files

None. The handler reads the rows in file order and does not need
`alchemystonechangeoffset.dbss` (see below). Item names come from LOC type 0
and icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | `133` on client 3464 |
| `+0x04` | Row[row_count] | rows      | See Row              |

### Row (variable: 56 bytes + condition text)

A fixed head, an inline condition script and a 12-byte tail. Every
condition on client 3464 is 19 characters long, so every row is 94 bytes
there; a reader takes the length from the count of `condition`.

| Offset           | Type      | Field            | Notes                                                    |
| ---------------- | --------- | ---------------- | -------------------------------------------------------- |
| `+0x00`          | u32       | key              | Row key; equals `item_id` on every row                   |
| `+0x04`          | u32       | item_id          | The item that grows; unique per row                      |
| `+0x08`          | u32       | unknown_08       | `0` on every row (client 3464)                           |
| `+0x0C`          | u32       | material_item_id | Growth material                                          |
| `+0x10`          | u32       | material_count   | Material units one Growth attempt takes                  |
| `+0x14`          | bytes[16] | unknown_14       | All zero on every row (client 3464)                      |
| `+0x24`          | str16     | condition        | Client condition script, see Conditions                  |
| `condition+0x00` | u32       | result_item_id   | The item a successful Growth gives; `0` on Totem rows    |
| `condition+0x04` | u32       | unknown_tail_04  | Falls with the stone tier; see Open Questions            |
| `condition+0x08` | u32       | unknown_tail_08  | `0` on every row (client 3464)                           |

On client 3464 the rows fall into two families:

| Rows | Items                                                                 | Material                          | material_count   | condition              |
| ---- | --------------------------------------------------------------------- | --------------------------------- | ---------------- | ---------------------- |
| 53   | Alchemy stones (45201 Imperfect to 45292 Splendid), Blessed and Exalted alchemy stones (768181 to 768512), Vell's, Khan's and Behelit's Hearts (761839 to 761876) | 821322 Brimming Essence of Aether | `2` to `30`      | `getLifeLevel(4)>10;`  |
| 80   | Totems of the Sea (54201 to 54292)                                    | 16001 Black Stone                 | `1`              | `getLifeLevel(1)>30;`, `>40;` or `>50;` |

`material_count` and `unknown_tail_04` follow the tier the stone grows into
(client 3464):

| Growth                | material_count | unknown_tail_04 |
| --------------------- | -------------- | --------------- |
| Imperfect to Sturdy   | `2`            | `455000`        |
| Sturdy to Sharp       | `3`            | `176000`        |
| Sharp to Resplendent  | `10`           | `31400`         |
| Resplendent to Splendid | `20`         | `12000`         |
| Splendid to Shining   | `30`           | `3870`          |

The Blessed, Exalted and Heart chains use the same pairs for the same tier
step. Imperfect stones grow straight to Sturdy (45201 to 45216, 45233 to
45248, 45265 to 45280); no row starts at a Rough stone.

### `alchemystonechangeoffset.dbss`

A row count equal to the main file's, then one index row per main row.

| Offset  | Type                 | Field     | Notes                              |
| ------- | -------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                      |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first three keys are 768512, 54205,
768189 where the main file has 768512, 768189, 768188).

### Index Row (12 bytes)

| Offset  | Type | Field   | Notes                                                    |
| ------- | ---- | ------- | -------------------------------------------------------- |
| `+0x00` | u32  | item_id | Row key, the main row's `key`                            |
| `+0x04` | u32  | offset  | Start of the row in `alchemystonechange.dbss` plus 4, at its `item_id` |
| `+0x08` | u32  | size    | Row length minus the 4-byte `key`; `90` on every row (client 3464) |

## Layout 1

On client 1784 the row has a u16 at `+0x08` where Layout 2 has a u32, 14
bytes of unknown fields before `condition` where Layout 2 has 16, and no
12-byte tail after `condition`. Only the Row differs from Layout 2.

### Row (variable: 40 bytes + condition text)

The index row `size` is `36` for a row with an empty `condition` and `74`
for one with a 19-character condition (client 1784).

| Offset  | Type     | Field            | Notes                                                            |
| ------- | -------- | ---------------- | ---------------------------------------------------------------- |
| `+0x00` | u32      | key              |                                                                  |
| `+0x04` | u32      | item_id          |                                                                  |
| `+0x08` | u16      | unknown_old_08   | `0` on Totem rows, an id near `item_id + 800` on alchemy stone rows |
| `+0x0A` | u32      | material_item_id | `16001` Black Stone on every row (client 1784)                   |
| `+0x0E` | u32      | material_count   | `1` or `50` (client 1784)                                        |
| `+0x12` | bytes[8] | unknown_12       | All zero on every row (client 1784)                              |
| `+0x1A` | u32      | unknown_1a       | `0`, `700000` or `850000` (client 1784)                          |
| `+0x1E` | u16      | unknown_1e       | `0`, or an id near `item_id + 870` on 24 alchemy stone rows (client 1784) |
| `+0x20` | str16    | condition        | Empty on every alchemy stone row (client 1784)                   |

## Conditions

The condition is a client condition script, as in the quest tables
(`getLifeLevel(6)>80;` in `newquest.bss`). `getLifeLevel(n)` reads a life
skill level, and the item tooltips name the skill and the rank each
condition stands for:

| condition             | Tooltip text                                                      |
| --------------------- | ----------------------------------------------------------------- |
| `getLifeLevel(4)>10;` | Alchemy stones: "Growth Attempt: At least Alchemy Apprentice 1"   |
| `getLifeLevel(1)>30;` | 54201 Old Totem of the Sea: "Growth available for Fishing Professional 1 and higher." |
| `getLifeLevel(1)>40;` | 54280 Plain Totem of the Sea [Amberjack]: "Fishing Artisan 1"     |
| `getLifeLevel(1)>50;` | 54287 Refined Totem of the Sea [Amberjack]: "Fishing Master 1"    |

So life skill `4` is Alchemy, `1` is Fishing, and level `10` is Beginner 10
(the condition asks for level 11, Apprentice 1).

## Notes

- The Growth window reads its material from the stone's item key
  (`ToClient_GetAlchemyEvolveNeedItemKey`, `ToClient_GetAlchemyEvolveNeedItemCount`)
  and its result from `getAlchemyEvolveItemStaticStatusWrapper(itemKey, 0)`
  (`panel_window_alchemystoneevolve_all`). The rows agree: 821322 Brimming
  Essence of Aether lists "Usage #1: Alchemy Stone Growth", and every
  `result_item_id` is the next tier of `item_id` (45228 Splendid to 45232
  Shining Alchemy Stone of Destruction).
- The Totem tooltips read "Depending on the amount of EXP, it can be grown
  with Black Stone", which matches the 16001 Black Stone x1 rows.
- The Growth tab lists up to three results per stone
  (`getAlchemyEvolveItemSize`, slots `0` to `2` in `panel_window_alchemystone_all`);
  this file holds one `result_item_id` per row.
- The window shows the Growth chance from `ToClient_requestAlchemyEvolveRate`
  as `rate * 1e-4` with a `%` (`LUA_ALCHEMY_ENCHANT_RATE`), the
  1,000,000 = 100% scale of the Polishing EXP in `alchemyupgrade.dbss`. The
  Lua asks for the rate per stone slot, so it is not read from this file
  directly.

## Open Questions

### Totem Results

The 80 Totem rows hold `result_item_id` `0`, yet each Totem tooltip says it
can be grown. The tier the Totem grows into is not in this file; the
item IDs run in tier blocks per fish (54273 Old, 54280 Plain, 54287 Refined,
54292 Resplendent Totem of the Sea [Amberjack]), but that order is not a
link the client data states.

### unknown_08, unknown_14 and unknown_tail_08

All zero on client 3464. The 16 bytes of `unknown_14` fit two more
(item, count) pairs after `material_item_id` and `material_count`, but no
row fills them.

## In-Game Checks

### unknown_tail_04 as the Growth Chance

Needs item (all):

- [Splendid Alchemy Stone of Destruction](https://bdocodex.com/us/item/45228/)
- [Brimming Essence of Aether](https://bdocodex.com/us/item/821322/)

`unknown_tail_04` falls with the tier, from `455000` (Imperfect to Sturdy)
to `3870` (Splendid to Shining), and reads as a chance on the 1,000,000 =
100% scale the Growth window uses. Polish the stone to 100% and open Growth.
A chance of 0.387% means `unknown_tail_04` is the Growth chance at 100%
Polishing. Read it again at 80% and 150%: a chance that scales from 0.387%
with Polishing confirms it as the base the client scales.
