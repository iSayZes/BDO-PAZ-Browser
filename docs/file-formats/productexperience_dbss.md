# `productexperience.dbss` Format

## Purpose

Level table of the life skill points (skill point pool `2`, the client's "product" skill points): one row per level from 0 to 2000. On client 3474 every row holds its level, an `exp` of `0` and the flag `1`, and the client's life skill point gauge is never updated (Notes). Companion `productexperienceoffset.dbss` lists where every row sits. The container and offset table are the ones of [skillexperience](skillexperience_dbss.md); only the row differs. No `productexperiencemaxlevel.bss` exists.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ------ | ---------------- | --------- |
| 1      | 1276 and later | 3483    | `productexperience.dbss`       | 14,011 | 2,001 Level Row  | 7         |
| 1      | 1276 and later | 3483    | `productexperienceoffset.dbss` | 20,014 | 2,001 Offset Row | 10        |

| Layout | File                           | Known             | Unknown    |
| ------ | ------------------------------ | ----------------- | ---------- |
| 1      | `productexperience.dbss`       | 14,011 B (100.0%) | 0 B (0.0%) |
| 1      | `productexperienceoffset.dbss` | 20,014 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `f92acb827d5d`  |
| 3482   | Layout 1 | `f92acb827d5d`  |
| 3474   | Layout 1 | `f92acb827d5d`  |
| 3473   | Layout 1 | `f92acb827d5d`  |
| 3464   | Layout 1 | `f92acb827d5d`  |
| 3458   | Layout 1 | `f92acb827d5d`  |
| 3454   | Layout 1 | `f92acb827d5d`  |
| 3444   | Layout 1 | `f92acb827d5d`  |
| 3435   | Layout 1 | `f92acb827d5d`  |
| 3426   | Layout 1 | `f92acb827d5d`  |
| 3418   | Layout 1 | `f92acb827d5d`  |
| 3412   | Layout 1 | `f92acb827d5d`  |
| 3402   | Layout 1 | `f92acb827d5d`  |
| 3396   | Layout 1 | `f92acb827d5d`  |
| 3387   | Layout 1 | `f92acb827d5d`  |
| 3381   | Layout 1 | `f92acb827d5d`  |
| 3373   | Layout 1 | `f92acb827d5d`  |
| 3364   | Layout 1 | `f92acb827d5d`  |
| 3356   | Layout 1 | `f92acb827d5d`  |
| 3349   | Layout 1 | `f92acb827d5d`  |
| 3342   | Layout 1 | `f92acb827d5d`  |
| 3335   | Layout 1 | `f92acb827d5d`  |
| 3326   | Layout 1 | `f92acb827d5d`  |
| 3321   | Layout 1 | `f92acb827d5d`  |
| 3314   | Layout 1 | `f92acb827d5d`  |
| 3303   | Layout 1 | `f92acb827d5d`  |
| 3302   | Layout 1 | `f92acb827d5d`  |
| 3293   | Layout 1 | `f92acb827d5d`  |
| 3283   | Layout 1 | `f92acb827d5d`  |
| 3275   | Layout 1 | `f92acb827d5d`  |
| 3267   | Layout 1 | `f92acb827d5d`  |
| 3258   | Layout 1 | `f92acb827d5d`  |
| 3251   | Layout 1 | `f92acb827d5d`  |
| 3242   | Layout 1 | `f92acb827d5d`  |
| 3235   | Layout 1 | `f92acb827d5d`  |
| 3229   | Layout 1 | `f92acb827d5d`  |
| 3212   | Layout 1 | `f92acb827d5d`  |
| 3203   | Layout 1 | `f92acb827d5d`  |
| 3193   | Layout 1 | `f92acb827d5d`  |
| 3186   | Layout 1 | `f92acb827d5d`  |
| 3177   | Layout 1 | `f92acb827d5d`  |
| 3169   | Layout 1 | `f92acb827d5d`  |
| 3158   | Layout 1 | `f92acb827d5d`  |
| 3151   | Layout 1 | `f92acb827d5d`  |
| 3144   | Layout 1 | `f92acb827d5d`  |
| 3133   | Layout 1 | `f92acb827d5d`  |
| 3125   | Layout 1 | `f92acb827d5d`  |
| 3118   | Layout 1 | `f92acb827d5d`  |
| 3111   | Layout 1 | `f92acb827d5d`  |
| 3103   | Layout 1 | `f92acb827d5d`  |
| 3095   | Layout 1 | `f92acb827d5d`  |
| 3086   | Layout 1 | `f92acb827d5d`  |
| 3072   | Layout 1 | `f92acb827d5d`  |
| 3062   | Layout 1 | `f92acb827d5d`  |
| 3052   | Layout 1 | `f92acb827d5d`  |
| 3045   | Layout 1 | `f92acb827d5d`  |
| 3037   | Layout 1 | `f92acb827d5d`  |
| 3030   | Layout 1 | `f92acb827d5d`  |
| 3021   | Layout 1 | `f92acb827d5d`  |
| 3012   | Layout 1 | `f92acb827d5d`  |
| 3002   | Layout 1 | `f92acb827d5d`  |
| 2995   | Layout 1 | `f92acb827d5d`  |
| 2987   | Layout 1 | `f92acb827d5d`  |
| 2978   | Layout 1 | `f92acb827d5d`  |
| 2970   | Layout 1 | `f92acb827d5d`  |
| 2959   | Layout 1 | `f92acb827d5d`  |
| 2951   | Layout 1 | `f92acb827d5d`  |
| 2942   | Layout 1 | `f92acb827d5d`  |
| 2935   | Layout 1 | `f92acb827d5d`  |
| 2932   | Layout 1 | `f92acb827d5d`  |
| 2923   | Layout 1 | `f92acb827d5d`  |
| 2919   | Layout 1 | `f92acb827d5d`  |
| 2907   | Layout 1 | `f92acb827d5d`  |
| 2900   | Layout 1 | `f92acb827d5d`  |
| 2891   | Layout 1 | `f92acb827d5d`  |
| 2882   | Layout 1 | `f92acb827d5d`  |
| 2872   | Layout 1 | `f92acb827d5d`  |
| 2863   | Layout 1 | `f92acb827d5d`  |
| 2855   | Layout 1 | `f92acb827d5d`  |
| 2849   | Layout 1 | `f92acb827d5d`  |
| 2844   | Layout 1 | `f92acb827d5d`  |
| 2834   | Layout 1 | `f92acb827d5d`  |
| 2825   | Layout 1 | `f92acb827d5d`  |
| 2819   | Layout 1 | `f92acb827d5d`  |
| 2811   | Layout 1 | `f92acb827d5d`  |
| 2803   | Layout 1 | `f92acb827d5d`  |
| 2794   | Layout 1 | `f92acb827d5d`  |
| 2783   | Layout 1 | `f92acb827d5d`  |
| 2774   | Layout 1 | `f92acb827d5d`  |
| 2765   | Layout 1 | `f92acb827d5d`  |
| 2756   | Layout 1 | `f92acb827d5d`  |
| 2750   | Layout 1 | `f92acb827d5d`  |
| 2743   | Layout 1 | `f92acb827d5d`  |
| 2736   | Layout 1 | `f92acb827d5d`  |
| 2726   | Layout 1 | `f92acb827d5d`  |
| 2717   | Layout 1 | `f92acb827d5d`  |
| 2709   | Layout 1 | `f92acb827d5d`  |
| 2703   | Layout 1 | `f92acb827d5d`  |
| 2695   | Layout 1 | `f92acb827d5d`  |
| 2684   | Layout 1 | `f92acb827d5d`  |
| 2672   | Layout 1 | `f92acb827d5d`  |
| 2665   | Layout 1 | `f92acb827d5d`  |
| 2657   | Layout 1 | `f92acb827d5d`  |
| 2649   | Layout 1 | `f92acb827d5d`  |
| 2644   | Layout 1 | `f92acb827d5d`  |
| 2637   | Layout 1 | `f92acb827d5d`  |
| 2629   | Layout 1 | `f92acb827d5d`  |
| 2619   | Layout 1 | `f92acb827d5d`  |
| 2612   | Layout 1 | `f92acb827d5d`  |
| 2606   | Layout 1 | `f92acb827d5d`  |
| 2602   | Layout 1 | `f92acb827d5d`  |
| 2601   | Layout 1 | `f92acb827d5d`  |
| 2592   | Layout 1 | `f92acb827d5d`  |
| 2583   | Layout 1 | `f92acb827d5d`  |
| 2575   | Layout 1 | `f92acb827d5d`  |
| 2567   | Layout 1 | `f92acb827d5d`  |
| 2560   | Layout 1 | `f92acb827d5d`  |
| 2553   | Layout 1 | `f92acb827d5d`  |
| 2545   | Layout 1 | `f92acb827d5d`  |
| 2538   | Layout 1 | `f92acb827d5d`  |
| 2529   | Layout 1 | `f92acb827d5d`  |
| 2519   | Layout 1 | `f92acb827d5d`  |
| 2513   | Layout 1 | `f92acb827d5d`  |
| 2510   | Layout 1 | `f92acb827d5d`  |
| 2507   | Layout 1 | `f92acb827d5d`  |
| 2503   | Layout 1 | `f92acb827d5d`  |
| 2498   | Layout 1 | `f92acb827d5d`  |
| 2492   | Layout 1 | `f92acb827d5d`  |
| 2487   | Layout 1 | `f92acb827d5d`  |
| 2480   | Layout 1 | `f92acb827d5d`  |
| 2474   | Layout 1 | `f92acb827d5d`  |
| 2468   | Layout 1 | `f92acb827d5d`  |
| 2460   | Layout 1 | `f92acb827d5d`  |
| 2453   | Layout 1 | `f92acb827d5d`  |
| 2444   | Layout 1 | `f92acb827d5d`  |
| 2438   | Layout 1 | `f92acb827d5d`  |
| 2434   | Layout 1 | `f92acb827d5d`  |
| 2429   | Layout 1 | `f92acb827d5d`  |
| 2421   | Layout 1 | `f92acb827d5d`  |
| 2414   | Layout 1 | `f92acb827d5d`  |
| 2407   | Layout 1 | `f92acb827d5d`  |
| 2401   | Layout 1 | `f92acb827d5d`  |
| 2397   | Layout 1 | `f92acb827d5d`  |
| 2393   | Layout 1 | `f92acb827d5d`  |
| 2384   | Layout 1 | `f92acb827d5d`  |
| 2378   | Layout 1 | `f92acb827d5d`  |
| 2372   | Layout 1 | `f92acb827d5d`  |
| 2358   | Layout 1 | `f92acb827d5d`  |
| 2352   | Layout 1 | `f92acb827d5d`  |
| 2347   | Layout 1 | `f92acb827d5d`  |
| 2343   | Layout 1 | `f92acb827d5d`  |
| 2335   | Layout 1 | `f92acb827d5d`  |
| 2327   | Layout 1 | `f92acb827d5d`  |
| 2324   | Layout 1 | `f92acb827d5d`  |
| 2319   | Layout 1 | `f92acb827d5d`  |
| 2313   | Layout 1 | `f92acb827d5d`  |
| 2308   | Layout 1 | `f92acb827d5d`  |
| 2302   | Layout 1 | `f92acb827d5d`  |
| 2295   | Layout 1 | `f92acb827d5d`  |
| 2290   | Layout 1 | `f92acb827d5d`  |
| 2284   | Layout 1 | `f92acb827d5d`  |
| 2276   | Layout 1 | `f92acb827d5d`  |
| 2269   | Layout 1 | `f92acb827d5d`  |
| 2259   | Layout 1 | `f92acb827d5d`  |
| 2250   | Layout 1 | `f92acb827d5d`  |
| 2243   | Layout 1 | `f92acb827d5d`  |
| 2235   | Layout 1 | `f92acb827d5d`  |
| 2229   | Layout 1 | `f92acb827d5d`  |
| 2224   | Layout 1 | `f92acb827d5d`  |
| 2218   | Layout 1 | `f92acb827d5d`  |
| 2215   | Layout 1 | `f92acb827d5d`  |
| 2207   | Layout 1 | `f92acb827d5d`  |
| 2203   | Layout 1 | `f92acb827d5d`  |
| 2196   | Layout 1 | `f92acb827d5d`  |
| 2192   | Layout 1 | `f92acb827d5d`  |
| 2189   | Layout 1 | `f92acb827d5d`  |
| 2183   | Layout 1 | `f92acb827d5d`  |
| 2179   | Layout 1 | `f92acb827d5d`  |
| 2171   | Layout 1 | `f92acb827d5d`  |
| 2163   | Layout 1 | `f92acb827d5d`  |
| 2156   | Layout 1 | `f92acb827d5d`  |
| 2151   | Layout 1 | `f92acb827d5d`  |
| 2147   | Layout 1 | `f92acb827d5d`  |
| 2142   | Layout 1 | `f92acb827d5d`  |
| 2138   | Layout 1 | `f92acb827d5d`  |
| 2134   | Layout 1 | `f92acb827d5d`  |
| 2130   | Layout 1 | `f92acb827d5d`  |
| 2122   | Layout 1 | `f92acb827d5d`  |
| 2107   | Layout 1 | `f92acb827d5d`  |
| 2098   | Layout 1 | `f92acb827d5d`  |
| 2089   | Layout 1 | `f92acb827d5d`  |
| 2081   | Layout 1 | `f92acb827d5d`  |
| 2073   | Layout 1 | `f92acb827d5d`  |
| 2067   | Layout 1 | `f92acb827d5d`  |
| 2063   | Layout 1 | `f92acb827d5d`  |
| 2059   | Layout 1 | `f92acb827d5d`  |
| 2052   | Layout 1 | `f92acb827d5d`  |
| 2044   | Layout 1 | `f92acb827d5d`  |
| 2039   | Layout 1 | `f92acb827d5d`  |
| 2032   | Layout 1 | `f92acb827d5d`  |
| 2025   | Layout 1 | `f92acb827d5d`  |
| 2011   | Layout 1 | `f92acb827d5d`  |
| 2005   | Layout 1 | `f92acb827d5d`  |
| 2000   | Layout 1 | `f92acb827d5d`  |
| 1996   | Layout 1 | `f92acb827d5d`  |
| 1991   | Layout 1 | `f92acb827d5d`  |
| 1985   | Layout 1 | `f92acb827d5d`  |
| 1980   | Layout 1 | `f92acb827d5d`  |
| 1969   | Layout 1 | `f92acb827d5d`  |
| 1964   | Layout 1 | `f92acb827d5d`  |
| 1958   | Layout 1 | `f92acb827d5d`  |
| 1950   | Layout 1 | `f92acb827d5d`  |
| 1945   | Layout 1 | `f92acb827d5d`  |
| 1937   | Layout 1 | `f92acb827d5d`  |
| 1933   | Layout 1 | `f92acb827d5d`  |
| 1927   | Layout 1 | `f92acb827d5d`  |
| 1921   | Layout 1 | `f92acb827d5d`  |
| 1914   | Layout 1 | `f92acb827d5d`  |
| 1908   | Layout 1 | `f92acb827d5d`  |
| 1897   | Layout 1 | `f92acb827d5d`  |
| 1892   | Layout 1 | `f92acb827d5d`  |
| 1886   | Layout 1 | `f92acb827d5d`  |
| 1881   | Layout 1 | `f92acb827d5d`  |
| 1871   | Layout 1 | `f92acb827d5d`  |
| 1866   | Layout 1 | `f92acb827d5d`  |
| 1862   | Layout 1 | `f92acb827d5d`  |
| 1854   | Layout 1 | `f92acb827d5d`  |
| 1846   | Layout 1 | `f92acb827d5d`  |
| 1838   | Layout 1 | `f92acb827d5d`  |
| 1832   | Layout 1 | `f92acb827d5d`  |
| 1826   | Layout 1 | `f92acb827d5d`  |
| 1822   | Layout 1 | `f92acb827d5d`  |
| 1818   | Layout 1 | `f92acb827d5d`  |
| 1804   | Layout 1 | `f92acb827d5d`  |
| 1794   | Layout 1 | `f92acb827d5d`  |
| 1790   | Layout 1 | `f92acb827d5d`  |
| 1784   | Layout 1 | `f92acb827d5d`  |
| 1774   | Layout 1 | `f92acb827d5d`  |
| 1771   | Layout 1 | `f92acb827d5d`  |
| 1762   | Layout 1 | `f92acb827d5d`  |
| 1759   | Layout 1 | `f92acb827d5d`  |
| 1754   | Layout 1 | `f92acb827d5d`  |
| 1749   | Layout 1 | `f92acb827d5d`  |
| 1743   | Layout 1 | `f92acb827d5d`  |
| 1737   | Layout 1 | `f92acb827d5d`  |
| 1731   | Layout 1 | `f92acb827d5d`  |
| 1725   | Layout 1 | `f92acb827d5d`  |
| 1717   | Layout 1 | `f92acb827d5d`  |
| 1710   | Layout 1 | `f92acb827d5d`  |
| 1704   | Layout 1 | `f92acb827d5d`  |
| 1698   | Layout 1 | `f92acb827d5d`  |
| 1690   | Layout 1 | `f92acb827d5d`  |
| 1685   | Layout 1 | `f92acb827d5d`  |
| 1680   | Layout 1 | `f92acb827d5d`  |
| 1674   | Layout 1 | `f92acb827d5d`  |
| 1668   | Layout 1 | `f92acb827d5d`  |
| 1659   | Layout 1 | `f92acb827d5d`  |
| 1649   | Layout 1 | `f92acb827d5d`  |
| 1642   | Layout 1 | `f92acb827d5d`  |
| 1636   | Layout 1 | `f92acb827d5d`  |
| 1628   | Layout 1 | `f92acb827d5d`  |
| 1622   | Layout 1 | `f92acb827d5d`  |
| 1614   | Layout 1 | `f92acb827d5d`  |
| 1608   | Layout 1 | `f92acb827d5d`  |
| 1602   | Layout 1 | `f92acb827d5d`  |
| 1598   | Layout 1 | `f92acb827d5d`  |
| 1594   | Layout 1 | `f92acb827d5d`  |
| 1590   | Layout 1 | `f92acb827d5d`  |
| 1587   | Layout 1 | `f92acb827d5d`  |
| 1584   | Layout 1 | `f92acb827d5d`  |
| 1579   | Layout 1 | `f92acb827d5d`  |
| 1572   | Layout 1 | `f92acb827d5d`  |
| 1565   | Layout 1 | `f92acb827d5d`  |
| 1559   | Layout 1 | `f92acb827d5d`  |
| 1554   | Layout 1 | `f92acb827d5d`  |
| 1547   | Layout 1 | `f92acb827d5d`  |
| 1537   | Layout 1 | `f92acb827d5d`  |
| 1529   | Layout 1 | `f92acb827d5d`  |
| 1524   | Layout 1 | `f92acb827d5d`  |
| 1519   | Layout 1 | `f92acb827d5d`  |
| 1509   | Layout 1 | `f92acb827d5d`  |
| 1506   | Layout 1 | `f92acb827d5d`  |
| 1504   | Layout 1 | `f92acb827d5d`  |
| 1500   | Layout 1 | `f92acb827d5d`  |
| 1493   | Layout 1 | `f92acb827d5d`  |
| 1489   | Layout 1 | `f92acb827d5d`  |
| 1485   | Layout 1 | `f92acb827d5d`  |
| 1481   | Layout 1 | `f92acb827d5d`  |
| 1474   | Layout 1 | `f92acb827d5d`  |
| 1466   | Layout 1 | `f92acb827d5d`  |
| 1462   | Layout 1 | `f92acb827d5d`  |
| 1459   | Layout 1 | `f92acb827d5d`  |
| 1453   | Layout 1 | `f92acb827d5d`  |
| 1450   | Layout 1 | `f92acb827d5d`  |
| 1445   | Layout 1 | `f92acb827d5d`  |
| 1439   | Layout 1 | `f92acb827d5d`  |
| 1433   | Layout 1 | `f92acb827d5d`  |
| 1430   | Layout 1 | `f92acb827d5d`  |
| 1426   | Layout 1 | `f92acb827d5d`  |
| 1421   | Layout 1 | `f92acb827d5d`  |
| 1417   | Layout 1 | `f92acb827d5d`  |
| 1416   | Layout 1 | `f92acb827d5d`  |
| 1409   | Layout 1 | `f92acb827d5d`  |
| 1405   | Layout 1 | `f92acb827d5d`  |
| 1401   | Layout 1 | `f92acb827d5d`  |
| 1396   | Layout 1 | `f92acb827d5d`  |
| 1391   | Layout 1 | `f92acb827d5d`  |
| 1390   | Layout 1 | `f92acb827d5d`  |
| 1386   | Layout 1 | `f92acb827d5d`  |
| 1381   | Layout 1 | `f92acb827d5d`  |
| 1379   | Layout 1 | `f92acb827d5d`  |
| 1372   | Layout 1 | `f92acb827d5d`  |
| 1366   | Layout 1 | `f92acb827d5d`  |
| 1364   | Layout 1 | `f92acb827d5d`  |
| 1363   | Layout 1 | `f92acb827d5d`  |
| 1360   | Layout 1 | `f92acb827d5d`  |
| 1358   | Layout 1 | `f92acb827d5d`  |
| 1355   | Layout 1 | `f92acb827d5d`  |
| 1351   | Layout 1 | `f92acb827d5d`  |
| 1348   | Layout 1 | `f92acb827d5d`  |
| 1346   | Layout 1 | `f92acb827d5d`  |
| 1341   | Layout 1 | `f92acb827d5d`  |
| 1340   | Layout 1 | `f92acb827d5d`  |
| 1338   | Layout 1 | `f92acb827d5d`  |
| 1335   | Layout 1 | `f92acb827d5d`  |
| 1333   | Layout 1 | `f92acb827d5d`  |
| 1329   | Layout 1 | `f92acb827d5d`  |
| 1327   | Layout 1 | `f92acb827d5d`  |
| 1324   | Layout 1 | `f92acb827d5d`  |
| 1321   | Layout 1 | `f92acb827d5d`  |
| 1319   | Layout 1 | `f92acb827d5d`  |
| 1318   | Layout 1 | `f92acb827d5d`  |
| 1316   | Layout 1 | `f92acb827d5d`  |
| 1313   | Layout 1 | `f92acb827d5d`  |
| 1311   | Layout 1 | `f92acb827d5d`  |
| 1309   | Layout 1 | `f92acb827d5d`  |
| 1304   | Layout 1 | `f92acb827d5d`  |
| 1292   | Layout 1 | `f92acb827d5d`  |
| 1286   | Layout 1 | `f92acb827d5d`  |
| 1280   | Layout 1 | `f92acb827d5d`  |
| 1276   | Layout 1 | `f92acb827d5d`  |
| 1267   | No file  | `f92acb827d5d`  |
| 1261   | No file  | `f92acb827d5d`  |
| 1256   | No file  | `f92acb827d5d`  |
| 1250   | No file  | `f92acb827d5d`  |
| 1246   | No file  | `f92acb827d5d`  |
| 1239   | No file  | `f92acb827d5d`  |
| 1230   | No file  | `f92acb827d5d`  |
| 1226   | No file  | `f92acb827d5d`  |
| 1220   | No file  | `f92acb827d5d`  |
| 1217   | No file  | `f92acb827d5d`  |
| 1211   | No file  | `f92acb827d5d`  |
| 1210   | No file  | `f92acb827d5d`  |
| 1208   | No file  | `f92acb827d5d`  |
| 1203   | No file  | `f92acb827d5d`  |
| 1197   | No file  | `f92acb827d5d`  |
| 1194   | No file  | `f92acb827d5d`  |
| 1192   | No file  | `f92acb827d5d`  |
| 1187   | No file  | `f92acb827d5d`  |
| 1183   | No file  | `f92acb827d5d`  |
| 1177   | No file  | `f92acb827d5d`  |
| 1173   | No file  | `f92acb827d5d`  |
| 1167   | No file  | `f92acb827d5d`  |
| 1164   | No file  | `f92acb827d5d`  |
| 1156   | No file  | `f92acb827d5d`  |
| 1149   | No file  | `f92acb827d5d`  |
| 1144   | No file  | `f92acb827d5d`  |
| 1137   | No file  | `f92acb827d5d`  |
| 1132   | No file  | `f92acb827d5d`  |
| 1127   | No file  | `f92acb827d5d`  |
| 1122   | No file  | `f92acb827d5d`  |
| 1118   | No file  | `f92acb827d5d`  |
| 1114   | No file  | `f92acb827d5d`  |
| 1109   | No file  | `f92acb827d5d`  |
| 1102   | No file  | `f92acb827d5d`  |
| 1096   | No file  | `f92acb827d5d`  |
| 1088   | No file  | `f92acb827d5d`  |
| 1081   | No file  | `f92acb827d5d`  |
| 1076   | No file  | `f92acb827d5d`  |
| 1069   | No file  | `f92acb827d5d`  |
| 1064   | No file  | `f92acb827d5d`  |
| 1058   | No file  | `f92acb827d5d`  |
| 1051   | No file  | `f92acb827d5d`  |
| 1044   | No file  | `f92acb827d5d`  |
| 1036   | No file  | `f92acb827d5d`  |
| 1026   | No file  | `f92acb827d5d`  |
| 1016   | No file  | `f92acb827d5d`  |
| 1009   | No file  | `f92acb827d5d`  |
| 1005   | No file  | `f92acb827d5d`  |
| 1000   | No file  | `f92acb827d5d`  |
| 998    | No file  | `f92acb827d5d`  |
| 990    | No file  | `f92acb827d5d`  |
| 979    | No file  | `f92acb827d5d`  |
| 972    | No file  | `f92acb827d5d`  |
| 963    | No file  | `f92acb827d5d`  |
| 955    | No file  | `f92acb827d5d`  |
| 946    | No file  | `f92acb827d5d`  |
| 938    | No file  | `f92acb827d5d`  |
| 927    | No file  | `f92acb827d5d`  |
| 911    | No file  | `f92acb827d5d`  |
| 904    | No file  | `f92acb827d5d`  |
| 899    | No file  | `f92acb827d5d`  |
| 894    | No file  | `f92acb827d5d`  |
| 885    | No file  | `f92acb827d5d`  |
| 879    | No file  | `f92acb827d5d`  |
| 872    | No file  | `f92acb827d5d`  |
| 864    | No file  | `f92acb827d5d`  |
| 855    | No file  | `f92acb827d5d`  |
| 853    | No file  | `f92acb827d5d`  |
| 845    | No file  | `f92acb827d5d`  |
| 837    | No file  | `f92acb827d5d`  |
| 829    | No file  | `f92acb827d5d`  |
| 822    | No file  | `f92acb827d5d`  |
| 814    | No file  | `f92acb827d5d`  |
| 805    | No file  | `f92acb827d5d`  |
| 794    | No file  | `f92acb827d5d`  |
| 787    | No file  | `f92acb827d5d`  |
| 780    | No file  | `f92acb827d5d`  |
| 771    | No file  | `f92acb827d5d`  |
| 760    | No file  | `f92acb827d5d`  |
| 748    | No file  | `f92acb827d5d`  |
| 741    | No file  | `f92acb827d5d`  |
| 736    | No file  | `f92acb827d5d`  |
| 731    | No file  | `f92acb827d5d`  |
| 723    | No file  | `f92acb827d5d`  |
| 711    | No file  | `f92acb827d5d`  |
| 707    | No file  | `f92acb827d5d`  |
| 697    | No file  | `f92acb827d5d`  |
| 689    | No file  | `f92acb827d5d`  |
| 683    | No file  | `f92acb827d5d`  |
| 678    | No file  | `f92acb827d5d`  |
| 670    | No file  | `f92acb827d5d`  |
| 661    | No file  | `f92acb827d5d`  |
| 656    | No file  | `f92acb827d5d`  |
| 652    | No file  | `f92acb827d5d`  |
| 643    | No file  | `f92acb827d5d`  |
| 637    | No file  | `f92acb827d5d`  |
| 630    | No file  | `f92acb827d5d`  |
| 627    | No file  | `f92acb827d5d`  |
| 621    | No file  | `f92acb827d5d`  |
| 617    | No file  | `f92acb827d5d`  |
| 615    | No file  | `f92acb827d5d`  |
| 606    | No file  | `f92acb827d5d`  |
| 599    | No file  | `f92acb827d5d`  |
| 592    | No file  | `f92acb827d5d`  |
| 586    | No file  | `f92acb827d5d`  |
| 577    | No file  | `f92acb827d5d`  |
| 569    | No file  | `f92acb827d5d`  |
| 561    | No file  | `f92acb827d5d`  |
| 554    | No file  | `f92acb827d5d`  |
| 542    | No file  | `f92acb827d5d`  |
| 532    | No file  | `f92acb827d5d`  |
| 531    | No file  | `f92acb827d5d`  |
| 526    | No file  | `f92acb827d5d`  |
| 521    | No file  | `f92acb827d5d`  |
| 517    | No file  | `f92acb827d5d`  |
| 510    | No file  | `f92acb827d5d`  |
| 508    | No file  | `f92acb827d5d`  |
| 504    | No file  | `f92acb827d5d`  |
| 497    | No file  | `f92acb827d5d`  |
| 491    | No file  | `f92acb827d5d`  |
| 485    | No file  | `f92acb827d5d`  |
| 478    | No file  | `f92acb827d5d`  |
| 472    | No file  | `f92acb827d5d`  |
| 466    | No file  | `f92acb827d5d`  |
| 457    | No file  | `f92acb827d5d`  |
| 452    | No file  | `f92acb827d5d`  |
| 449    | No file  | `f92acb827d5d`  |
| 435    | No file  | `f92acb827d5d`  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                   |
| ------------------------------- | -------- | -------------------------------------- |
| `productexperienceoffset.dbss`  | Required | `level -> (offset, size)` of every row |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                 | Field     | Notes                                                   |
| ------- | -------------------- | --------- | ------------------------------------------------------- |
| `+0x00` | u32                  | row_count | Number of rows; 2,001 (levels 0 to 2000) on client 3464 |
| `+0x04` | Level Row[row_count] | rows      | `row_count` rows of 7 bytes, not in level order         |

The rows fill the file exactly: 4 + 2,001 x 7 = 14,011 bytes on client 3464.

### Level Row (7 bytes)

| Offset  | Type | Field          | Notes                                               |
| ------- | ---- | -------------- | --------------------------------------------------- |
| `+0x00` | u16  | level          | Life skill point level; equals the offset row's key |
| `+0x02` | u32  | exp            | `0` on every row (client 3474)                      |
| `+0x06` | u8   | is_exp_defined | `1` on every row (client 3474); see Field Names     |

### `productexperienceoffset.dbss`

The layout of `skillexperienceoffset.dbss` (see [skillexperience](skillexperience_dbss.md)): a u32 row count equal to the main file's, then 10-byte [u16 level][u32 data_offset][u32 data_size] rows with no magic and no trailer. `data_size` is always 7, and `data_offset` points at the row's `level`. The rows are not in level order (399, 1052, 0, ...); the parser returns the main rows sorted by level.

| Offset  | Type                  | Field     | Notes                                         |
| ------- | --------------------- | --------- | --------------------------------------------- |
| `+0x00` | u32                   | row_count | Equals the `productexperience.dbss` row count |
| `+0x04` | Offset Row[row_count] | rows      | `row_count` rows of 10 bytes                  |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                 |
| ------- | ---- | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | level       | Level of the row it points at                                         |
| `+0x02` | u32  | data_offset | Absolute byte offset of the row's `level` in `productexperience.dbss` |
| `+0x06` | u32  | data_size   | Always 7                                                              |

## Field Names

The row is the `ProductExp_Table` sheet of a private server on client 1784, read the way its server dump (`Instance_dumpFull.exe`) reads it. The dump fills one static status from the client's `productexperience.dbss` (row reader at VA `0x140bf39a0`) and from the sheet (column reads at VA `0x1408dbeaf` to `0x1408dbf10`):

| Field            | Member  | Read from the file | Sheet column        |
| ---------------- | ------- | ------------------ | ------------------- |
| `level`          | `+0x00` | u16                | `Index`             |
| `exp`            | `+0x04` | u32                | `ProductRequireEXP` |
| `is_exp_defined` | `+0x08` | u8                 | none                |

The sheet loader writes `1` to `is_exp_defined` for every row it loads and logs "skill point key(%#): EXP is not defined" for a row it rejects, the same flag [guildskillexperience](guildskillexperience_dbss.md) stores. `ProductRequireEXP` is `0` on all 2,001 sheet rows, as `exp` is on client 3474, and the sheet's note calls it "the EXP a production skill needs". So the row does have an EXP field, empty on every level. Earlier versions of this doc read the row as a u32 level, a u16 `unknown_04` and a u8 `unknown_06`; with the zero bytes the values are the same.

## Notes

- "Product" is the client's word for the life skill point pool. `panel_selfplayerexpgage.luac` defines `Panel_User_ProductSkillPoint_Update`, which reads `ToClient_getSkillPointInfo(2)` into the `StaticText_SkillPoint_p` / `CircularProgress_SkillExp_p` gauge, and `acquire.luac` announces a new point as `GainProductSkillPoint` with `ACQUIRE_OBJECTMESSAGE_1` ("Life Skill Points Obtained"). No client Lua script calls `Panel_User_ProductSkillPoint_Update` or registers it for an event on client 3464.
- Quest rewards of type `__eRewardLifeExp` give `_productExperience` / `getProductExperience()` (`panel_dialog_quest_all_1.luac`, `panel_window_questinfo_all_1.luac`), shown as "Production EXP" (`LUA_QUESTREWARD_SIMPLE_TOOLTIP_PRODUCTEXP`). Whether that reward feeds this pool or the per-skill tables in [lifeexp](lifeexp_dbss.md) is not visible in the Lua.
- See the [skillexperience](skillexperience_dbss.md) Notes for the three skill point pools.
