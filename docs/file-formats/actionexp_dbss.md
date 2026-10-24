# `actionexp.dbss` Format

## Purpose

One row per class type and level with EXP amounts for action kinds: quests, gathering, processing, alchemy, fishing, horse taming, study, trade and farming on client 1784, where the client 3473 row has 8 bytes more. Every EXP byte is `0` on client 3473 and on client 1784, so the table holds the grid of class types and levels and nothing else. The 2016 client loads it into `gc::ActionExpStaticStatus` from the `ActionEXP_Table` sheet; no client Lua file names it. Companion `actionexpoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes   | Records                                             | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ------- | --------------------------------------------------- | --------- |
| 2      | 2171 and later | 3483    | `actionexp.dbss`       | 577,128 | 6,480 Level Row, 6,480 Level Entry, 102 Class Block | 85        |
| 2      | 2171 and later | 3483    | `actionexpoffset.dbss` | 78,164  | 6,480 Offset Row, 101 Offset Block                  | 12        |
| 1      | 1346 to 2163   | 2163    | `actionexp.dbss`       | 316,308 | 3,900 Level Row, 3,900 Level Entry, 102 Class Block | 77        |
| 1      | 1346 to 2163   | 2163    | `actionexpoffset.dbss` | 47,204  | 3,900 Offset Row, 101 Offset Block                  | 12        |

| Layout | File                   | Known              | Unknown           |
| ------ | ---------------------- | ------------------ | ----------------- |
| 2      | `actionexp.dbss`       | 58,728 B (10.2%)   | 518,400 B (89.8%) |
| 2      | `actionexpoffset.dbss` | 78,164 B (100.0%)  | 0 B (0.0%)        |
| 1      | `actionexp.dbss`       | 316,308 B (100.0%) | 0 B (0.0%)        |
| 1      | `actionexpoffset.dbss` | 47,204 B (100.0%)  | 0 B (0.0%)        |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `dfa599f0595c`  |
| 3482   | Layout 2             | `dfa599f0595c`  |
| 3474   | Layout 2             | `dfa599f0595c`  |
| 3473   | Layout 2             | `dfa599f0595c`  |
| 3464   | Layout 2             | `dfa599f0595c`  |
| 3458   | Layout 2             | `dfa599f0595c`  |
| 3454   | Layout 2             | `dfa599f0595c`  |
| 3444   | Layout 2             | `dfa599f0595c`  |
| 3435   | Layout 2             | `dfa599f0595c`  |
| 3426   | Layout 2             | `dfa599f0595c`  |
| 3418   | Layout 2             | `dfa599f0595c`  |
| 3412   | Layout 2             | `dfa599f0595c`  |
| 3402   | Layout 2             | `dfa599f0595c`  |
| 3396   | Layout 2             | `dfa599f0595c`  |
| 3387   | Layout 2             | `dfa599f0595c`  |
| 3381   | Layout 2             | `dfa599f0595c`  |
| 3373   | Layout 2             | `dfa599f0595c`  |
| 3364   | Layout 2             | `dfa599f0595c`  |
| 3356   | Layout 2             | `dfa599f0595c`  |
| 3349   | Layout 2             | `dfa599f0595c`  |
| 3342   | Layout 2             | `dfa599f0595c`  |
| 3335   | Layout 2             | `dfa599f0595c`  |
| 3326   | Layout 2             | `dfa599f0595c`  |
| 3321   | Layout 2             | `dfa599f0595c`  |
| 3314   | Layout 2             | `dfa599f0595c`  |
| 3303   | Layout 2             | `dfa599f0595c`  |
| 3302   | Layout 2             | `dfa599f0595c`  |
| 3293   | Layout 2             | `dfa599f0595c`  |
| 3283   | Layout 2             | `dfa599f0595c`  |
| 3275   | Layout 2             | `dfa599f0595c`  |
| 3267   | Layout 2             | `dfa599f0595c`  |
| 3258   | Layout 2             | `dfa599f0595c`  |
| 3251   | Layout 2             | `dfa599f0595c`  |
| 3242   | Layout 2             | `dfa599f0595c`  |
| 3235   | Layout 2             | `dfa599f0595c`  |
| 3229   | Layout 2             | `dfa599f0595c`  |
| 3212   | Layout 2             | `dfa599f0595c`  |
| 3203   | Layout 2             | `dfa599f0595c`  |
| 3193   | Layout 2             | `dfa599f0595c`  |
| 3186   | Layout 2             | `dfa599f0595c`  |
| 3177   | Layout 2             | `dfa599f0595c`  |
| 3169   | Layout 2             | `dfa599f0595c`  |
| 3158   | Layout 2             | `dfa599f0595c`  |
| 3151   | Layout 2             | `dfa599f0595c`  |
| 3144   | Layout 2             | `dfa599f0595c`  |
| 3133   | Layout 2             | `dfa599f0595c`  |
| 3125   | Layout 2             | `dfa599f0595c`  |
| 3118   | Layout 2             | `dfa599f0595c`  |
| 3111   | Layout 2             | `dfa599f0595c`  |
| 3103   | Layout 2             | `dfa599f0595c`  |
| 3095   | Layout 2             | `dfa599f0595c`  |
| 3086   | Layout 2             | `dfa599f0595c`  |
| 3072   | Layout 2             | `dfa599f0595c`  |
| 3062   | Layout 2             | `dfa599f0595c`  |
| 3052   | Layout 2             | `dfa599f0595c`  |
| 3045   | Layout 2             | `dfa599f0595c`  |
| 3037   | Layout 2             | `dfa599f0595c`  |
| 3030   | Layout 2             | `dfa599f0595c`  |
| 3021   | Layout 2             | `dfa599f0595c`  |
| 3012   | Layout 2             | `dfa599f0595c`  |
| 3002   | Layout 2             | `dfa599f0595c`  |
| 2995   | Layout 2             | `dfa599f0595c`  |
| 2987   | Layout 2             | `dfa599f0595c`  |
| 2978   | Layout 2             | `dfa599f0595c`  |
| 2970   | Layout 2             | `dfa599f0595c`  |
| 2959   | Layout 2             | `dfa599f0595c`  |
| 2951   | Layout 2             | `dfa599f0595c`  |
| 2942   | Layout 2             | `dfa599f0595c`  |
| 2935   | Layout 2             | `dfa599f0595c`  |
| 2932   | Layout 2             | `dfa599f0595c`  |
| 2923   | Layout 2             | `dfa599f0595c`  |
| 2919   | Layout 2             | `dfa599f0595c`  |
| 2907   | Layout 2             | `dfa599f0595c`  |
| 2900   | Layout 2             | `dfa599f0595c`  |
| 2891   | Layout 2             | `dfa599f0595c`  |
| 2882   | Layout 2             | `dfa599f0595c`  |
| 2872   | Layout 2             | `dfa599f0595c`  |
| 2863   | Layout 2             | `dfa599f0595c`  |
| 2855   | Layout 2             | `dfa599f0595c`  |
| 2849   | Layout 2             | `dfa599f0595c`  |
| 2844   | Layout 2             | `dfa599f0595c`  |
| 2834   | Layout 2             | `dfa599f0595c`  |
| 2825   | Layout 2             | `dfa599f0595c`  |
| 2819   | Layout 2             | `dfa599f0595c`  |
| 2811   | Layout 2             | `dfa599f0595c`  |
| 2803   | Layout 2             | `dfa599f0595c`  |
| 2794   | Layout 2             | `dfa599f0595c`  |
| 2783   | Layout 2             | `dfa599f0595c`  |
| 2774   | Layout 2             | `dfa599f0595c`  |
| 2765   | Layout 2             | `dfa599f0595c`  |
| 2756   | Layout 2             | `dfa599f0595c`  |
| 2750   | Layout 2             | `dfa599f0595c`  |
| 2743   | Layout 2             | `dfa599f0595c`  |
| 2736   | Layout 2             | `dfa599f0595c`  |
| 2726   | Layout 2             | `dfa599f0595c`  |
| 2717   | Layout 2             | `dfa599f0595c`  |
| 2709   | Layout 2             | `dfa599f0595c`  |
| 2703   | Layout 2             | `dfa599f0595c`  |
| 2695   | Layout 2             | `dfa599f0595c`  |
| 2684   | Layout 2             | `dfa599f0595c`  |
| 2672   | Layout 2             | `dfa599f0595c`  |
| 2665   | Layout 2             | `dfa599f0595c`  |
| 2657   | Layout 2             | `dfa599f0595c`  |
| 2649   | Layout 2             | `dfa599f0595c`  |
| 2644   | Layout 2             | `dfa599f0595c`  |
| 2637   | Layout 2             | `dfa599f0595c`  |
| 2629   | Layout 2             | `dfa599f0595c`  |
| 2619   | Layout 2             | `dfa599f0595c`  |
| 2612   | Layout 2             | `dfa599f0595c`  |
| 2606   | Layout 2             | `dfa599f0595c`  |
| 2602   | Layout 2             | `dfa599f0595c`  |
| 2601   | Layout 2             | `dfa599f0595c`  |
| 2592   | Layout 2             | `dfa599f0595c`  |
| 2583   | Layout 2             | `dfa599f0595c`  |
| 2575   | Layout 2             | `dfa599f0595c`  |
| 2567   | Layout 2             | `dfa599f0595c`  |
| 2560   | Layout 2             | `dfa599f0595c`  |
| 2553   | Layout 2             | `dfa599f0595c`  |
| 2545   | Layout 2             | `dfa599f0595c`  |
| 2538   | Layout 2             | `dfa599f0595c`  |
| 2529   | Layout 2             | `dfa599f0595c`  |
| 2519   | Layout 2             | `dfa599f0595c`  |
| 2513   | Layout 2             | `dfa599f0595c`  |
| 2510   | Layout 2             | `dfa599f0595c`  |
| 2507   | Layout 2             | `dfa599f0595c`  |
| 2503   | Layout 2             | `dfa599f0595c`  |
| 2498   | Layout 2             | `dfa599f0595c`  |
| 2492   | Layout 2             | `dfa599f0595c`  |
| 2487   | Layout 2             | `dfa599f0595c`  |
| 2480   | Layout 2             | `dfa599f0595c`  |
| 2474   | Layout 2             | `dfa599f0595c`  |
| 2468   | Layout 2             | `dfa599f0595c`  |
| 2460   | Layout 2             | `dfa599f0595c`  |
| 2453   | Layout 2             | `dfa599f0595c`  |
| 2444   | Layout 2             | `dfa599f0595c`  |
| 2438   | Layout 2             | `dfa599f0595c`  |
| 2434   | Layout 2             | `dfa599f0595c`  |
| 2429   | Layout 2             | `dfa599f0595c`  |
| 2421   | Layout 2             | `dfa599f0595c`  |
| 2414   | Layout 2             | `dfa599f0595c`  |
| 2407   | Layout 2             | `dfa599f0595c`  |
| 2401   | Layout 2             | `dfa599f0595c`  |
| 2397   | Layout 2             | `dfa599f0595c`  |
| 2393   | Layout 2             | `dfa599f0595c`  |
| 2384   | Layout 2             | `dfa599f0595c`  |
| 2378   | Layout 2             | `dfa599f0595c`  |
| 2372   | Layout 2             | `dfa599f0595c`  |
| 2358   | Layout 2             | `dfa599f0595c`  |
| 2352   | Layout 2             | `dfa599f0595c`  |
| 2347   | Layout 2             | `dfa599f0595c`  |
| 2343   | Layout 2             | `dfa599f0595c`  |
| 2335   | Layout 2             | `dfa599f0595c`  |
| 2327   | Layout 2             | `dfa599f0595c`  |
| 2324   | Layout 2             | `dfa599f0595c`  |
| 2319   | Layout 2             | `dfa599f0595c`  |
| 2313   | Layout 2             | `dfa599f0595c`  |
| 2308   | Layout 2             | `dfa599f0595c`  |
| 2302   | Layout 2             | `dfa599f0595c`  |
| 2295   | Layout 2             | `dfa599f0595c`  |
| 2290   | Layout 2             | `dfa599f0595c`  |
| 2284   | Layout 2             | `dfa599f0595c`  |
| 2276   | Layout 2             | `dfa599f0595c`  |
| 2269   | Layout 2             | `dfa599f0595c`  |
| 2259   | Layout 2             | `dfa599f0595c`  |
| 2250   | Layout 2             | `dfa599f0595c`  |
| 2243   | Layout 2             | `dfa599f0595c`  |
| 2235   | Layout 2             | `dfa599f0595c`  |
| 2229   | Layout 2             | `dfa599f0595c`  |
| 2224   | Layout 2             | `dfa599f0595c`  |
| 2218   | Layout 2             | `dfa599f0595c`  |
| 2215   | Layout 2             | `dfa599f0595c`  |
| 2207   | Layout 2             | `dfa599f0595c`  |
| 2203   | Layout 2             | `dfa599f0595c`  |
| 2196   | Layout 2             | `dfa599f0595c`  |
| 2192   | Layout 2             | `dfa599f0595c`  |
| 2189   | Layout 2             | `dfa599f0595c`  |
| 2183   | Layout 2             | `dfa599f0595c`  |
| 2179   | Layout 2             | `dfa599f0595c`  |
| 2171   | Layout 2             | `dfa599f0595c`  |
| 2163   | Layout 1             | `dfa599f0595c`  |
| 2156   | Layout 1             | `dfa599f0595c`  |
| 2151   | Layout 1             | `dfa599f0595c`  |
| 2147   | Layout 1             | `dfa599f0595c`  |
| 2142   | Layout 1             | `dfa599f0595c`  |
| 2138   | Layout 1             | `dfa599f0595c`  |
| 2134   | Layout 1             | `dfa599f0595c`  |
| 2130   | Layout 1             | `dfa599f0595c`  |
| 2122   | Layout 1             | `dfa599f0595c`  |
| 2107   | Layout 1             | `dfa599f0595c`  |
| 2098   | Layout 1             | `dfa599f0595c`  |
| 2089   | Layout 1             | `dfa599f0595c`  |
| 2081   | Layout 1             | `dfa599f0595c`  |
| 2073   | Layout 1             | `dfa599f0595c`  |
| 2067   | Layout 1             | `dfa599f0595c`  |
| 2063   | Layout 1             | `dfa599f0595c`  |
| 2059   | Layout 1             | `dfa599f0595c`  |
| 2052   | Layout 1             | `dfa599f0595c`  |
| 2044   | Layout 1             | `dfa599f0595c`  |
| 2039   | Layout 1             | `dfa599f0595c`  |
| 2032   | Layout 1             | `dfa599f0595c`  |
| 2025   | Layout 1             | `dfa599f0595c`  |
| 2011   | Layout 1             | `dfa599f0595c`  |
| 2005   | Layout 1             | `dfa599f0595c`  |
| 2000   | Layout 1             | `dfa599f0595c`  |
| 1996   | Layout 1             | `dfa599f0595c`  |
| 1991   | Layout 1             | `dfa599f0595c`  |
| 1985   | Layout 1             | `dfa599f0595c`  |
| 1980   | Layout 1             | `dfa599f0595c`  |
| 1969   | Layout 1             | `dfa599f0595c`  |
| 1964   | Layout 1             | `dfa599f0595c`  |
| 1958   | Layout 1             | `dfa599f0595c`  |
| 1950   | Layout 1             | `dfa599f0595c`  |
| 1945   | Layout 1             | `dfa599f0595c`  |
| 1937   | Layout 1             | `dfa599f0595c`  |
| 1933   | Layout 1             | `dfa599f0595c`  |
| 1927   | Layout 1             | `dfa599f0595c`  |
| 1921   | Layout 1             | `dfa599f0595c`  |
| 1914   | Layout 1             | `dfa599f0595c`  |
| 1908   | Layout 1             | `dfa599f0595c`  |
| 1897   | Layout 1             | `dfa599f0595c`  |
| 1892   | Layout 1             | `dfa599f0595c`  |
| 1886   | Layout 1             | `dfa599f0595c`  |
| 1881   | Layout 1             | `dfa599f0595c`  |
| 1871   | Layout 1             | `dfa599f0595c`  |
| 1866   | Layout 1             | `dfa599f0595c`  |
| 1862   | Layout 1             | `dfa599f0595c`  |
| 1854   | Layout 1             | `dfa599f0595c`  |
| 1846   | Layout 1             | `dfa599f0595c`  |
| 1838   | Layout 1             | `dfa599f0595c`  |
| 1832   | Layout 1             | `dfa599f0595c`  |
| 1826   | Layout 1             | `dfa599f0595c`  |
| 1822   | Layout 1             | `dfa599f0595c`  |
| 1818   | Layout 1             | `dfa599f0595c`  |
| 1804   | Layout 1             | `dfa599f0595c`  |
| 1794   | Layout 1             | `dfa599f0595c`  |
| 1790   | Layout 1             | `dfa599f0595c`  |
| 1784   | Layout 1             | `dfa599f0595c`  |
| 1774   | Layout 1             | `dfa599f0595c`  |
| 1771   | Layout 1             | `dfa599f0595c`  |
| 1762   | Layout 1             | `dfa599f0595c`  |
| 1759   | Layout 1             | `dfa599f0595c`  |
| 1754   | Layout 1             | `dfa599f0595c`  |
| 1749   | Layout 1             | `dfa599f0595c`  |
| 1743   | Layout 1             | `dfa599f0595c`  |
| 1737   | Layout 1             | `dfa599f0595c`  |
| 1731   | Layout 1             | `dfa599f0595c`  |
| 1725   | Layout 1             | `dfa599f0595c`  |
| 1717   | Layout 1             | `dfa599f0595c`  |
| 1710   | Layout 1             | `dfa599f0595c`  |
| 1704   | Layout 1             | `dfa599f0595c`  |
| 1698   | Layout 1             | `dfa599f0595c`  |
| 1690   | Layout 1             | `dfa599f0595c`  |
| 1685   | Layout 1             | `dfa599f0595c`  |
| 1680   | Layout 1             | `dfa599f0595c`  |
| 1674   | Layout 1             | `dfa599f0595c`  |
| 1668   | Layout 1             | `dfa599f0595c`  |
| 1659   | Layout 1             | `dfa599f0595c`  |
| 1649   | Layout 1             | `dfa599f0595c`  |
| 1642   | Layout 1             | `dfa599f0595c`  |
| 1636   | Layout 1             | `dfa599f0595c`  |
| 1628   | Layout 1             | `dfa599f0595c`  |
| 1622   | Layout 1             | `dfa599f0595c`  |
| 1614   | Layout 1             | `dfa599f0595c`  |
| 1608   | Layout 1             | `dfa599f0595c`  |
| 1602   | Layout 1             | `dfa599f0595c`  |
| 1598   | Layout 1             | `dfa599f0595c`  |
| 1594   | Layout 1             | `dfa599f0595c`  |
| 1590   | Layout 1             | `dfa599f0595c`  |
| 1587   | Layout 1             | `dfa599f0595c`  |
| 1584   | Layout 1             | `dfa599f0595c`  |
| 1579   | Layout 1             | `dfa599f0595c`  |
| 1572   | Layout 1             | `dfa599f0595c`  |
| 1565   | Layout 1             | `dfa599f0595c`  |
| 1559   | Layout 1             | `dfa599f0595c`  |
| 1554   | Layout 1             | `dfa599f0595c`  |
| 1547   | Layout 1             | `dfa599f0595c`  |
| 1537   | Layout 1             | `dfa599f0595c`  |
| 1529   | Layout 1             | `dfa599f0595c`  |
| 1524   | Layout 1             | `dfa599f0595c`  |
| 1519   | Layout 1             | `dfa599f0595c`  |
| 1509   | Layout 1             | `dfa599f0595c`  |
| 1506   | Layout 1             | `dfa599f0595c`  |
| 1504   | Layout 1             | `dfa599f0595c`  |
| 1500   | Layout 1             | `dfa599f0595c`  |
| 1493   | Layout 1             | `dfa599f0595c`  |
| 1489   | Layout 1             | `dfa599f0595c`  |
| 1485   | Layout 1             | `dfa599f0595c`  |
| 1481   | Layout 1             | `dfa599f0595c`  |
| 1474   | Layout 1             | `dfa599f0595c`  |
| 1466   | Layout 1             | `dfa599f0595c`  |
| 1462   | Layout 1             | `dfa599f0595c`  |
| 1459   | Layout 1             | `dfa599f0595c`  |
| 1453   | Layout 1             | `dfa599f0595c`  |
| 1450   | Layout 1             | `dfa599f0595c`  |
| 1445   | Layout 1             | `dfa599f0595c`  |
| 1439   | Layout 1             | `dfa599f0595c`  |
| 1433   | Layout 1             | `dfa599f0595c`  |
| 1430   | Layout 1             | `dfa599f0595c`  |
| 1426   | Layout 1             | `dfa599f0595c`  |
| 1421   | Layout 1             | `dfa599f0595c`  |
| 1417   | Layout 1             | `dfa599f0595c`  |
| 1416   | Layout 1             | `dfa599f0595c`  |
| 1409   | Layout 1             | `dfa599f0595c`  |
| 1405   | Layout 1             | `dfa599f0595c`  |
| 1401   | Layout 1             | `dfa599f0595c`  |
| 1396   | Layout 1             | `dfa599f0595c`  |
| 1391   | Layout 1             | `dfa599f0595c`  |
| 1390   | Layout 1             | `dfa599f0595c`  |
| 1386   | Layout 1             | `dfa599f0595c`  |
| 1381   | Layout 1             | `dfa599f0595c`  |
| 1379   | Layout 1             | `dfa599f0595c`  |
| 1372   | Layout 1             | `dfa599f0595c`  |
| 1366   | Layout 1             | `dfa599f0595c`  |
| 1364   | Layout 1             | `dfa599f0595c`  |
| 1363   | Layout 1             | `dfa599f0595c`  |
| 1360   | Layout 1             | `dfa599f0595c`  |
| 1358   | Layout 1             | `dfa599f0595c`  |
| 1355   | Layout 1             | `dfa599f0595c`  |
| 1351   | Layout 1             | `dfa599f0595c`  |
| 1348   | Layout 1             | `dfa599f0595c`  |
| 1346   | Layout 1             | `dfa599f0595c`  |
| 1341   | No documented layout | `dfa599f0595c`  |
| 1340   | No documented layout | `dfa599f0595c`  |
| 1338   | No documented layout | `dfa599f0595c`  |
| 1335   | No documented layout | `dfa599f0595c`  |
| 1333   | No documented layout | `dfa599f0595c`  |
| 1329   | No documented layout | `dfa599f0595c`  |
| 1327   | No documented layout | `dfa599f0595c`  |
| 1324   | No documented layout | `dfa599f0595c`  |
| 1321   | No documented layout | `dfa599f0595c`  |
| 1319   | No documented layout | `dfa599f0595c`  |
| 1318   | No documented layout | `dfa599f0595c`  |
| 1316   | No documented layout | `dfa599f0595c`  |
| 1313   | No documented layout | `dfa599f0595c`  |
| 1311   | No documented layout | `dfa599f0595c`  |
| 1309   | No documented layout | `dfa599f0595c`  |
| 1304   | No documented layout | `dfa599f0595c`  |
| 1292   | No documented layout | `dfa599f0595c`  |
| 1286   | No documented layout | `dfa599f0595c`  |
| 1280   | No documented layout | `dfa599f0595c`  |
| 1276   | No documented layout | `dfa599f0595c`  |
| 1267   | No file              | `dfa599f0595c`  |
| 1261   | No file              | `dfa599f0595c`  |
| 1256   | No file              | `dfa599f0595c`  |
| 1250   | No file              | `dfa599f0595c`  |
| 1246   | No file              | `dfa599f0595c`  |
| 1239   | No file              | `dfa599f0595c`  |
| 1230   | No file              | `dfa599f0595c`  |
| 1226   | No file              | `dfa599f0595c`  |
| 1220   | No file              | `dfa599f0595c`  |
| 1217   | No file              | `dfa599f0595c`  |
| 1211   | No file              | `dfa599f0595c`  |
| 1210   | No file              | `dfa599f0595c`  |
| 1208   | No file              | `dfa599f0595c`  |
| 1203   | No file              | `dfa599f0595c`  |
| 1197   | No file              | `dfa599f0595c`  |
| 1194   | No file              | `dfa599f0595c`  |
| 1192   | No file              | `dfa599f0595c`  |
| 1187   | No file              | `dfa599f0595c`  |
| 1183   | No file              | `dfa599f0595c`  |
| 1177   | No file              | `dfa599f0595c`  |
| 1173   | No file              | `dfa599f0595c`  |
| 1167   | No file              | `dfa599f0595c`  |
| 1164   | No file              | `dfa599f0595c`  |
| 1156   | No file              | `dfa599f0595c`  |
| 1149   | No file              | `dfa599f0595c`  |
| 1144   | No file              | `dfa599f0595c`  |
| 1137   | No file              | `dfa599f0595c`  |
| 1132   | No file              | `dfa599f0595c`  |
| 1127   | No file              | `dfa599f0595c`  |
| 1122   | No file              | `dfa599f0595c`  |
| 1118   | No file              | `dfa599f0595c`  |
| 1114   | No file              | `dfa599f0595c`  |
| 1109   | No file              | `dfa599f0595c`  |
| 1102   | No file              | `dfa599f0595c`  |
| 1096   | No file              | `dfa599f0595c`  |
| 1088   | No file              | `dfa599f0595c`  |
| 1081   | No file              | `dfa599f0595c`  |
| 1076   | No file              | `dfa599f0595c`  |
| 1069   | No file              | `dfa599f0595c`  |
| 1064   | No file              | `dfa599f0595c`  |
| 1058   | No file              | `dfa599f0595c`  |
| 1051   | No file              | `dfa599f0595c`  |
| 1044   | No file              | `dfa599f0595c`  |
| 1036   | No file              | `dfa599f0595c`  |
| 1026   | No file              | `dfa599f0595c`  |
| 1016   | No file              | `dfa599f0595c`  |
| 1009   | No file              | `dfa599f0595c`  |
| 1005   | No file              | `dfa599f0595c`  |
| 1000   | No file              | `dfa599f0595c`  |
| 998    | No file              | `dfa599f0595c`  |
| 990    | No file              | `dfa599f0595c`  |
| 979    | No file              | `dfa599f0595c`  |
| 972    | No file              | `dfa599f0595c`  |
| 963    | No file              | `dfa599f0595c`  |
| 955    | No file              | `dfa599f0595c`  |
| 946    | No file              | `dfa599f0595c`  |
| 938    | No file              | `dfa599f0595c`  |
| 927    | No file              | `dfa599f0595c`  |
| 911    | No file              | `dfa599f0595c`  |
| 904    | No file              | `dfa599f0595c`  |
| 899    | No file              | `dfa599f0595c`  |
| 894    | No file              | `dfa599f0595c`  |
| 885    | No file              | `dfa599f0595c`  |
| 879    | No file              | `dfa599f0595c`  |
| 872    | No file              | `dfa599f0595c`  |
| 864    | No file              | `dfa599f0595c`  |
| 855    | No file              | `dfa599f0595c`  |
| 853    | No file              | `dfa599f0595c`  |
| 845    | No file              | `dfa599f0595c`  |
| 837    | No file              | `dfa599f0595c`  |
| 829    | No file              | `dfa599f0595c`  |
| 822    | No file              | `dfa599f0595c`  |
| 814    | No file              | `dfa599f0595c`  |
| 805    | No file              | `dfa599f0595c`  |
| 794    | No file              | `dfa599f0595c`  |
| 787    | No file              | `dfa599f0595c`  |
| 780    | No file              | `dfa599f0595c`  |
| 771    | No file              | `dfa599f0595c`  |
| 760    | No file              | `dfa599f0595c`  |
| 748    | No file              | `dfa599f0595c`  |
| 741    | No file              | `dfa599f0595c`  |
| 736    | No file              | `dfa599f0595c`  |
| 731    | No file              | `dfa599f0595c`  |
| 723    | No file              | `dfa599f0595c`  |
| 711    | No file              | `dfa599f0595c`  |
| 707    | No file              | `dfa599f0595c`  |
| 697    | No file              | `dfa599f0595c`  |
| 689    | No file              | `dfa599f0595c`  |
| 683    | No file              | `dfa599f0595c`  |
| 678    | No file              | `dfa599f0595c`  |
| 670    | No file              | `dfa599f0595c`  |
| 661    | No file              | `dfa599f0595c`  |
| 656    | No file              | `dfa599f0595c`  |
| 652    | No file              | `dfa599f0595c`  |
| 643    | No file              | `dfa599f0595c`  |
| 637    | No file              | `dfa599f0595c`  |
| 630    | No file              | `dfa599f0595c`  |
| 627    | No file              | `dfa599f0595c`  |
| 621    | No file              | `dfa599f0595c`  |
| 617    | No file              | `dfa599f0595c`  |
| 615    | No file              | `dfa599f0595c`  |
| 606    | No file              | `dfa599f0595c`  |
| 599    | No file              | `dfa599f0595c`  |
| 592    | No file              | `dfa599f0595c`  |
| 586    | No file              | `dfa599f0595c`  |
| 577    | No file              | `dfa599f0595c`  |
| 569    | No file              | `dfa599f0595c`  |
| 561    | No file              | `dfa599f0595c`  |
| 554    | No file              | `dfa599f0595c`  |
| 542    | No file              | `dfa599f0595c`  |
| 532    | No file              | `dfa599f0595c`  |
| 531    | No file              | `dfa599f0595c`  |
| 526    | No file              | `dfa599f0595c`  |
| 521    | No file              | `dfa599f0595c`  |
| 517    | No file              | `dfa599f0595c`  |
| 510    | No file              | `dfa599f0595c`  |
| 508    | No file              | `dfa599f0595c`  |
| 504    | No file              | `dfa599f0595c`  |
| 497    | No file              | `dfa599f0595c`  |
| 491    | No file              | `dfa599f0595c`  |
| 485    | No file              | `dfa599f0595c`  |
| 478    | No file              | `dfa599f0595c`  |
| 472    | No file              | `dfa599f0595c`  |
| 466    | No file              | `dfa599f0595c`  |
| 457    | No file              | `dfa599f0595c`  |
| 452    | No file              | `dfa599f0595c`  |
| 449    | No file              | `dfa599f0595c`  |
| 435    | No file              | `dfa599f0595c`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                               |
| ---------------------- | -------- | -------------------------------------------------- |
| `actionexpoffset.dbss` | Required | `(class type, level) -> (offset, size)` of every row |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type               | Field  | Notes                                                  |
| ------- | ------------------ | ------ | ------------------------------------------------------ |
| `+0x00` | Class Block[..end] | blocks | One block per class type, from class type 0 up; see Class Block |

The file stores no block count. On client 3473 it holds 102 blocks: 36 with 180 rows (class types 0 to 36 without 18) and 66 empty ones (class type 18 and 37 to 101), 36 x (4 + 180 x 89) + 66 x 4 = 577,128 bytes.

### Class Block (variable: 4 bytes + entries)

| Offset  | Type                     | Field       | Notes                                              |
| ------- | ------------------------ | ----------- | -------------------------------------------------- |
| `+0x00` | u32                      | level_count | Rows in this block; `180` or `0` on client 3473    |
| `+0x04` | Level Entry[level_count] | entries     | See Level Entry                                    |

### Level Entry (89 bytes)

| Offset  | Type      | Field      | Notes                                         |
| ------- | --------- | ---------- | --------------------------------------------- |
| `+0x00` | u32       | key_prefix | Equals `level` of the row after it            |
| `+0x04` | Level Row | row        | See Level Row; the offset file points here    |

### Level Row (85 bytes)

| Offset  | Type      | Field      | Notes                                                        |
| ------- | --------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8        | class_type | Class type, the number `getClassType()` returns; equals the block index |
| `+0x01` | u32       | level      | `1` to `level_count`, ascending inside a block               |
| `+0x05` | bytes[80] | unknown_05 | Every byte `0` on client 3473; see Open Questions            |

### `actionexpoffset.dbss`

Index into `actionexp.dbss`, with the same block shape as the main file.

| Offset  | Type                | Field  | Notes                                     |
| ------- | ------------------- | ------ | ----------------------------------------- |
| `+0x00` | Offset Block[..end] | blocks | Blocks repeated until the end of the file |

The block index is the class type; the file stores no class type field. On client 3473 it holds 101 blocks (class types 0 to 100), one fewer than the main file: 36 x (4 + 180 x 12) + 65 x 4 = 78,164 bytes.

### Offset Block (variable: 4 bytes + rows)

| Offset  | Type                    | Field       | Notes                                       |
| ------- | ----------------------- | ----------- | ------------------------------------------- |
| `+0x00` | u32                     | level_count | Equals the main file block's `level_count`  |
| `+0x04` | Offset Row[level_count] | rows        | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | level       | Level of the row it points at                                      |
| `+0x04` | u32  | data_offset | Absolute byte offset of the Level Row in `actionexp.dbss`, just past its `key_prefix` |
| `+0x08` | u32  | data_size   | Always the Level Row size, `85` on client 3473                     |

The first row of class type 0 sits at `0x08`, after its block's `level_count` and the row's `key_prefix`. The parser reads the main file through these rows and checks that each row's `key_prefix`, `class_type` and `level` match the offset row's level and block.

## Layout 1

On client 1784 the Level Row holds nine i64 EXP fields (72 bytes) where Layout 2 has 80 bytes. The blocks keep their shape: 102 in the main file and 101 in `actionexpoffset.dbss`, 28 of them with 130 rows (class types 0 to 5, 7 to 12, 15 to 17 and 19 to 31), and `data_size` is `77`.

### Level Entry (81 bytes)

| Offset  | Type      | Field      | Notes                                         |
| ------- | --------- | ---------- | --------------------------------------------- |
| `+0x00` | u32       | key_prefix | Equals `level` of the row after it            |
| `+0x04` | Level Row | row        | See Level Row; the offset file points here    |

### Level Row (77 bytes)

| Offset  | Type | Field            | Notes                        |
| ------- | ---- | ---------------- | ---------------------------- |
| `+0x00` | u8   | class_type       | Equals the block index       |
| `+0x01` | u32  | level            | `1` to `130`                 |
| `+0x05` | i64  | quest_exp        | `0` on every row (client 1784) |
| `+0x0D` | i64  | collect_exp      | `0` on every row (client 1784) |
| `+0x15` | i64  | manufacture_exp  | `0` on every row (client 1784) |
| `+0x1D` | i64  | alchemy_exp      | `0` on every row (client 1784) |
| `+0x25` | i64  | fishing_exp      | `0` on every row (client 1784) |
| `+0x2D` | i64  | horse_taming_exp | `0` on every row (client 1784) |
| `+0x35` | i64  | study_exp        | `0` on every row (client 1784) |
| `+0x3D` | i64  | trade_exp        | `0` on every row (client 1784) |
| `+0x45` | i64  | farming_exp      | `0` on every row (client 1784) |

## Field Names

The 2016 `gc::ActionExpStaticStatus` (80 bytes in memory) holds `_class` (`gc::ClassType`, 1 byte), 3 bytes of alignment, `int _level` and nine `__int64` members `_questExp`, `_collectExp`, `_manufactureExp`, `_alchemytExp` (spelled so), `_fishingExp`, `_horseTamingExp`, `_studyExp`, `_tradeExp` and `_farmingExp`. The file packs these members without the alignment: 1 + 4 + 9 x 8 = 77 bytes, the client 1784 row size. The `ActionEXP_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 has the columns `Class`, `Level`, `Quest`, `Collect`, `Manufacture`, `Alchemy`, `Fishing`, `HorseTaming`, `Study`, `Trade` and `Farming` in the same order, and 3,640 rows (28 classes x 130 levels), as many as the client 1784 file.

Every EXP value is `0` in the sheet and in both client files, so the values cannot tell the slots apart; the Layout 1 names rest on the slot count and the member order. The sheet's class set differs from the client file's (it has classes 6 and 18 and lacks 7 and 15), a private server edit.

## Enum Values

### Class Type

`class_type` and the block index are class types, named by LOC type 21 (`str_id1` = class type, `str_id4` = `0`). On client 3473 the main file has rows for class types 0 to 36 except 18 (`Shai Male`), including types no character can pick: 13 and 36 (`PBM`), 14 (`Ain (No Use)`) and 22 (`Temp Maehwa`). LOC type 21 numbers class types 0 to 100, the 101 blocks of `actionexpoffset.dbss`.

## Notes

- The level range follows the life skill levels of [lifeexp](lifeexp_dbss.md): levels 1 to 130 here and 0 to 130 there on client 1784, 1 to 180 here and 0 to 180 there on client 3473.
- The main file ends with one more empty block than the offset file on both clients (102 against 101). The parser reads the main file only through the offset rows, so the extra `level_count` of `0` is never read.
- The 2016 client keeps the rows in `gc::ActionExpStaticStatusManager` as an array of 32 maps, one per class type, keyed by level. Its loader is `GameCommonParameterLoaderFromExcel::LoadActionExpStaticInformation`.
- [lifeexp](lifeexp_dbss.md) and [fitnesslevel](fitnesslevel_dbss.md) use the same block shape, but their offset rows point at the row itself; here each row has a u32 `key_prefix` before it.

## Open Questions

### Which EXP Slot Is New in the 80-Byte Payload

The Layout 2 row has 80 bytes after `level`, 8 more than the nine i64 fields of client 1784, the size of one more i64 EXP slot. Every byte is `0` on client 3473, and no newer struct or sheet than client 1784 names the columns, so neither the new slot's position nor its action kind is known. The nine old fields stay unnamed in Layout 2 until a client fills a value or a newer source lists the columns.
