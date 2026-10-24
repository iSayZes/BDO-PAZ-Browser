# `fairyskillchange.dbss` Format

## Purpose

Defines the cost of rerolling a fairy's skills. Each fairy level (`1`–`50`) maps to the number of Theiah's Orbs consumed by a skill change at that level, rising from `1` to `5` in fixed level bands.

This is the data behind the well-known rerolling advice: keep a fairy at a low level while rerolling, because the orb cost scales with its level.

`fairyskillchangeoffset.dbss` provides a level-keyed index into the main file, which is needed because the records are **not** stored in level order.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | ------------- | --------- |
| 1      | 1346 and later | 3483    | `fairyskillchange.dbss`       | 604   | 50 Record     | 12        |
| 1      | 1346 and later | 3483    | `fairyskillchangeoffset.dbss` | 604   | 50 Offset Row | 12        |

| Layout | File                          | Known          | Unknown    |
| ------ | ----------------------------- | -------------- | ---------- |
| 1      | `fairyskillchange.dbss`       | 604 B (100.0%) | 0 B (0.0%) |
| 1      | `fairyskillchangeoffset.dbss` | 604 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `d11cc94de7b4`  |
| 3482   | Layout 1             | `d11cc94de7b4`  |
| 3474   | Layout 1             | `d11cc94de7b4`  |
| 3473   | Layout 1             | `d11cc94de7b4`  |
| 3464   | Layout 1             | `d11cc94de7b4`  |
| 3458   | Layout 1             | `d11cc94de7b4`  |
| 3454   | Layout 1             | `d11cc94de7b4`  |
| 3444   | Layout 1             | `d11cc94de7b4`  |
| 3435   | Layout 1             | `d11cc94de7b4`  |
| 3426   | Layout 1             | `d11cc94de7b4`  |
| 3418   | Layout 1             | `d11cc94de7b4`  |
| 3412   | Layout 1             | `d11cc94de7b4`  |
| 3402   | Layout 1             | `d11cc94de7b4`  |
| 3396   | Layout 1             | `d11cc94de7b4`  |
| 3387   | Layout 1             | `d11cc94de7b4`  |
| 3381   | Layout 1             | `d11cc94de7b4`  |
| 3373   | Layout 1             | `d11cc94de7b4`  |
| 3364   | Layout 1             | `d11cc94de7b4`  |
| 3356   | Layout 1             | `d11cc94de7b4`  |
| 3349   | Layout 1             | `d11cc94de7b4`  |
| 3342   | Layout 1             | `d11cc94de7b4`  |
| 3335   | Layout 1             | `d11cc94de7b4`  |
| 3326   | Layout 1             | `d11cc94de7b4`  |
| 3321   | Layout 1             | `d11cc94de7b4`  |
| 3314   | Layout 1             | `d11cc94de7b4`  |
| 3303   | Layout 1             | `d11cc94de7b4`  |
| 3302   | Layout 1             | `d11cc94de7b4`  |
| 3293   | Layout 1             | `d11cc94de7b4`  |
| 3283   | Layout 1             | `d11cc94de7b4`  |
| 3275   | Layout 1             | `d11cc94de7b4`  |
| 3267   | Layout 1             | `d11cc94de7b4`  |
| 3258   | Layout 1             | `d11cc94de7b4`  |
| 3251   | Layout 1             | `d11cc94de7b4`  |
| 3242   | Layout 1             | `d11cc94de7b4`  |
| 3235   | Layout 1             | `d11cc94de7b4`  |
| 3229   | Layout 1             | `d11cc94de7b4`  |
| 3212   | Layout 1             | `d11cc94de7b4`  |
| 3203   | Layout 1             | `d11cc94de7b4`  |
| 3193   | Layout 1             | `d11cc94de7b4`  |
| 3186   | Layout 1             | `d11cc94de7b4`  |
| 3177   | Layout 1             | `d11cc94de7b4`  |
| 3169   | Layout 1             | `d11cc94de7b4`  |
| 3158   | Layout 1             | `d11cc94de7b4`  |
| 3151   | Layout 1             | `d11cc94de7b4`  |
| 3144   | Layout 1             | `d11cc94de7b4`  |
| 3133   | Layout 1             | `d11cc94de7b4`  |
| 3125   | Layout 1             | `d11cc94de7b4`  |
| 3118   | Layout 1             | `d11cc94de7b4`  |
| 3111   | Layout 1             | `d11cc94de7b4`  |
| 3103   | Layout 1             | `d11cc94de7b4`  |
| 3095   | Layout 1             | `d11cc94de7b4`  |
| 3086   | Layout 1             | `d11cc94de7b4`  |
| 3072   | Layout 1             | `d11cc94de7b4`  |
| 3062   | Layout 1             | `d11cc94de7b4`  |
| 3052   | Layout 1             | `d11cc94de7b4`  |
| 3045   | Layout 1             | `d11cc94de7b4`  |
| 3037   | Layout 1             | `d11cc94de7b4`  |
| 3030   | Layout 1             | `d11cc94de7b4`  |
| 3021   | Layout 1             | `d11cc94de7b4`  |
| 3012   | Layout 1             | `d11cc94de7b4`  |
| 3002   | Layout 1             | `d11cc94de7b4`  |
| 2995   | Layout 1             | `d11cc94de7b4`  |
| 2987   | Layout 1             | `d11cc94de7b4`  |
| 2978   | Layout 1             | `d11cc94de7b4`  |
| 2970   | Layout 1             | `d11cc94de7b4`  |
| 2959   | Layout 1             | `d11cc94de7b4`  |
| 2951   | Layout 1             | `d11cc94de7b4`  |
| 2942   | Layout 1             | `d11cc94de7b4`  |
| 2935   | Layout 1             | `d11cc94de7b4`  |
| 2932   | Layout 1             | `d11cc94de7b4`  |
| 2923   | Layout 1             | `d11cc94de7b4`  |
| 2919   | Layout 1             | `d11cc94de7b4`  |
| 2907   | Layout 1             | `d11cc94de7b4`  |
| 2900   | Layout 1             | `d11cc94de7b4`  |
| 2891   | Layout 1             | `d11cc94de7b4`  |
| 2882   | Layout 1             | `d11cc94de7b4`  |
| 2872   | Layout 1             | `d11cc94de7b4`  |
| 2863   | Layout 1             | `d11cc94de7b4`  |
| 2855   | Layout 1             | `d11cc94de7b4`  |
| 2849   | Layout 1             | `d11cc94de7b4`  |
| 2844   | Layout 1             | `d11cc94de7b4`  |
| 2834   | Layout 1             | `d11cc94de7b4`  |
| 2825   | Layout 1             | `d11cc94de7b4`  |
| 2819   | Layout 1             | `d11cc94de7b4`  |
| 2811   | Layout 1             | `d11cc94de7b4`  |
| 2803   | Layout 1             | `d11cc94de7b4`  |
| 2794   | Layout 1             | `d11cc94de7b4`  |
| 2783   | Layout 1             | `d11cc94de7b4`  |
| 2774   | Layout 1             | `d11cc94de7b4`  |
| 2765   | Layout 1             | `d11cc94de7b4`  |
| 2756   | Layout 1             | `d11cc94de7b4`  |
| 2750   | Layout 1             | `d11cc94de7b4`  |
| 2743   | Layout 1             | `d11cc94de7b4`  |
| 2736   | Layout 1             | `d11cc94de7b4`  |
| 2726   | Layout 1             | `d11cc94de7b4`  |
| 2717   | Layout 1             | `d11cc94de7b4`  |
| 2709   | Layout 1             | `d11cc94de7b4`  |
| 2703   | Layout 1             | `d11cc94de7b4`  |
| 2695   | Layout 1             | `d11cc94de7b4`  |
| 2684   | Layout 1             | `d11cc94de7b4`  |
| 2672   | Layout 1             | `d11cc94de7b4`  |
| 2665   | Layout 1             | `d11cc94de7b4`  |
| 2657   | Layout 1             | `d11cc94de7b4`  |
| 2649   | Layout 1             | `d11cc94de7b4`  |
| 2644   | Layout 1             | `d11cc94de7b4`  |
| 2637   | Layout 1             | `d11cc94de7b4`  |
| 2629   | Layout 1             | `d11cc94de7b4`  |
| 2619   | Layout 1             | `d11cc94de7b4`  |
| 2612   | Layout 1             | `d11cc94de7b4`  |
| 2606   | Layout 1             | `d11cc94de7b4`  |
| 2602   | Layout 1             | `d11cc94de7b4`  |
| 2601   | Layout 1             | `d11cc94de7b4`  |
| 2592   | Layout 1             | `d11cc94de7b4`  |
| 2583   | Layout 1             | `d11cc94de7b4`  |
| 2575   | Layout 1             | `d11cc94de7b4`  |
| 2567   | Layout 1             | `d11cc94de7b4`  |
| 2560   | Layout 1             | `d11cc94de7b4`  |
| 2553   | Layout 1             | `d11cc94de7b4`  |
| 2545   | Layout 1             | `d11cc94de7b4`  |
| 2538   | Layout 1             | `d11cc94de7b4`  |
| 2529   | Layout 1             | `d11cc94de7b4`  |
| 2519   | Layout 1             | `d11cc94de7b4`  |
| 2513   | Layout 1             | `d11cc94de7b4`  |
| 2510   | Layout 1             | `d11cc94de7b4`  |
| 2507   | Layout 1             | `d11cc94de7b4`  |
| 2503   | Layout 1             | `d11cc94de7b4`  |
| 2498   | Layout 1             | `d11cc94de7b4`  |
| 2492   | Layout 1             | `d11cc94de7b4`  |
| 2487   | Layout 1             | `d11cc94de7b4`  |
| 2480   | Layout 1             | `d11cc94de7b4`  |
| 2474   | Layout 1             | `d11cc94de7b4`  |
| 2468   | Layout 1             | `d11cc94de7b4`  |
| 2460   | Layout 1             | `d11cc94de7b4`  |
| 2453   | Layout 1             | `d11cc94de7b4`  |
| 2444   | Layout 1             | `d11cc94de7b4`  |
| 2438   | Layout 1             | `d11cc94de7b4`  |
| 2434   | Layout 1             | `d11cc94de7b4`  |
| 2429   | Layout 1             | `d11cc94de7b4`  |
| 2421   | Layout 1             | `d11cc94de7b4`  |
| 2414   | Layout 1             | `d11cc94de7b4`  |
| 2407   | Layout 1             | `d11cc94de7b4`  |
| 2401   | Layout 1             | `d11cc94de7b4`  |
| 2397   | Layout 1             | `d11cc94de7b4`  |
| 2393   | Layout 1             | `d11cc94de7b4`  |
| 2384   | Layout 1             | `d11cc94de7b4`  |
| 2378   | Layout 1             | `d11cc94de7b4`  |
| 2372   | Layout 1             | `d11cc94de7b4`  |
| 2358   | Layout 1             | `d11cc94de7b4`  |
| 2352   | Layout 1             | `d11cc94de7b4`  |
| 2347   | Layout 1             | `d11cc94de7b4`  |
| 2343   | Layout 1             | `d11cc94de7b4`  |
| 2335   | Layout 1             | `d11cc94de7b4`  |
| 2327   | Layout 1             | `d11cc94de7b4`  |
| 2324   | Layout 1             | `d11cc94de7b4`  |
| 2319   | Layout 1             | `d11cc94de7b4`  |
| 2313   | Layout 1             | `d11cc94de7b4`  |
| 2308   | Layout 1             | `d11cc94de7b4`  |
| 2302   | Layout 1             | `d11cc94de7b4`  |
| 2295   | Layout 1             | `d11cc94de7b4`  |
| 2290   | Layout 1             | `d11cc94de7b4`  |
| 2284   | Layout 1             | `d11cc94de7b4`  |
| 2276   | Layout 1             | `d11cc94de7b4`  |
| 2269   | Layout 1             | `d11cc94de7b4`  |
| 2259   | Layout 1             | `d11cc94de7b4`  |
| 2250   | Layout 1             | `d11cc94de7b4`  |
| 2243   | Layout 1             | `d11cc94de7b4`  |
| 2235   | Layout 1             | `d11cc94de7b4`  |
| 2229   | Layout 1             | `d11cc94de7b4`  |
| 2224   | Layout 1             | `d11cc94de7b4`  |
| 2218   | Layout 1             | `d11cc94de7b4`  |
| 2215   | Layout 1             | `d11cc94de7b4`  |
| 2207   | Layout 1             | `d11cc94de7b4`  |
| 2203   | Layout 1             | `d11cc94de7b4`  |
| 2196   | Layout 1             | `d11cc94de7b4`  |
| 2192   | Layout 1             | `d11cc94de7b4`  |
| 2189   | Layout 1             | `d11cc94de7b4`  |
| 2183   | Layout 1             | `d11cc94de7b4`  |
| 2179   | Layout 1             | `d11cc94de7b4`  |
| 2171   | Layout 1             | `d11cc94de7b4`  |
| 2163   | Layout 1             | `d11cc94de7b4`  |
| 2156   | Layout 1             | `d11cc94de7b4`  |
| 2151   | Layout 1             | `d11cc94de7b4`  |
| 2147   | Layout 1             | `d11cc94de7b4`  |
| 2142   | Layout 1             | `d11cc94de7b4`  |
| 2138   | Layout 1             | `d11cc94de7b4`  |
| 2134   | Layout 1             | `d11cc94de7b4`  |
| 2130   | Layout 1             | `d11cc94de7b4`  |
| 2122   | Layout 1             | `d11cc94de7b4`  |
| 2107   | Layout 1             | `d11cc94de7b4`  |
| 2098   | Layout 1             | `d11cc94de7b4`  |
| 2089   | Layout 1             | `d11cc94de7b4`  |
| 2081   | Layout 1             | `d11cc94de7b4`  |
| 2073   | Layout 1             | `d11cc94de7b4`  |
| 2067   | Layout 1             | `d11cc94de7b4`  |
| 2063   | Layout 1             | `d11cc94de7b4`  |
| 2059   | Layout 1             | `d11cc94de7b4`  |
| 2052   | Layout 1             | `d11cc94de7b4`  |
| 2044   | Layout 1             | `d11cc94de7b4`  |
| 2039   | Layout 1             | `d11cc94de7b4`  |
| 2032   | Layout 1             | `d11cc94de7b4`  |
| 2025   | Layout 1             | `d11cc94de7b4`  |
| 2011   | Layout 1             | `d11cc94de7b4`  |
| 2005   | Layout 1             | `d11cc94de7b4`  |
| 2000   | Layout 1             | `d11cc94de7b4`  |
| 1996   | Layout 1             | `d11cc94de7b4`  |
| 1991   | Layout 1             | `d11cc94de7b4`  |
| 1985   | Layout 1             | `d11cc94de7b4`  |
| 1980   | Layout 1             | `d11cc94de7b4`  |
| 1969   | Layout 1             | `d11cc94de7b4`  |
| 1964   | Layout 1             | `d11cc94de7b4`  |
| 1958   | Layout 1             | `d11cc94de7b4`  |
| 1950   | Layout 1             | `d11cc94de7b4`  |
| 1945   | Layout 1             | `d11cc94de7b4`  |
| 1937   | Layout 1             | `d11cc94de7b4`  |
| 1933   | Layout 1             | `d11cc94de7b4`  |
| 1927   | Layout 1             | `d11cc94de7b4`  |
| 1921   | Layout 1             | `d11cc94de7b4`  |
| 1914   | Layout 1             | `d11cc94de7b4`  |
| 1908   | Layout 1             | `d11cc94de7b4`  |
| 1897   | Layout 1             | `d11cc94de7b4`  |
| 1892   | Layout 1             | `d11cc94de7b4`  |
| 1886   | Layout 1             | `d11cc94de7b4`  |
| 1881   | Layout 1             | `d11cc94de7b4`  |
| 1871   | Layout 1             | `d11cc94de7b4`  |
| 1866   | Layout 1             | `d11cc94de7b4`  |
| 1862   | Layout 1             | `d11cc94de7b4`  |
| 1854   | Layout 1             | `d11cc94de7b4`  |
| 1846   | Layout 1             | `d11cc94de7b4`  |
| 1838   | Layout 1             | `d11cc94de7b4`  |
| 1832   | Layout 1             | `d11cc94de7b4`  |
| 1826   | Layout 1             | `d11cc94de7b4`  |
| 1822   | Layout 1             | `d11cc94de7b4`  |
| 1818   | Layout 1             | `d11cc94de7b4`  |
| 1804   | Layout 1             | `d11cc94de7b4`  |
| 1794   | Layout 1             | `d11cc94de7b4`  |
| 1790   | Layout 1             | `d11cc94de7b4`  |
| 1784   | Layout 1             | `d11cc94de7b4`  |
| 1774   | Layout 1             | `d11cc94de7b4`  |
| 1771   | Layout 1             | `d11cc94de7b4`  |
| 1762   | Layout 1             | `d11cc94de7b4`  |
| 1759   | Layout 1             | `d11cc94de7b4`  |
| 1754   | Layout 1             | `d11cc94de7b4`  |
| 1749   | Layout 1             | `d11cc94de7b4`  |
| 1743   | Layout 1             | `d11cc94de7b4`  |
| 1737   | Layout 1             | `d11cc94de7b4`  |
| 1731   | Layout 1             | `d11cc94de7b4`  |
| 1725   | Layout 1             | `d11cc94de7b4`  |
| 1717   | Layout 1             | `d11cc94de7b4`  |
| 1710   | Layout 1             | `d11cc94de7b4`  |
| 1704   | Layout 1             | `d11cc94de7b4`  |
| 1698   | Layout 1             | `d11cc94de7b4`  |
| 1690   | Layout 1             | `d11cc94de7b4`  |
| 1685   | Layout 1             | `d11cc94de7b4`  |
| 1680   | Layout 1             | `d11cc94de7b4`  |
| 1674   | Layout 1             | `d11cc94de7b4`  |
| 1668   | Layout 1             | `d11cc94de7b4`  |
| 1659   | Layout 1             | `d11cc94de7b4`  |
| 1649   | Layout 1             | `d11cc94de7b4`  |
| 1642   | Layout 1             | `d11cc94de7b4`  |
| 1636   | Layout 1             | `d11cc94de7b4`  |
| 1628   | Layout 1             | `d11cc94de7b4`  |
| 1622   | Layout 1             | `d11cc94de7b4`  |
| 1614   | Layout 1             | `d11cc94de7b4`  |
| 1608   | Layout 1             | `d11cc94de7b4`  |
| 1602   | Layout 1             | `d11cc94de7b4`  |
| 1598   | Layout 1             | `d11cc94de7b4`  |
| 1594   | Layout 1             | `d11cc94de7b4`  |
| 1590   | Layout 1             | `d11cc94de7b4`  |
| 1587   | Layout 1             | `d11cc94de7b4`  |
| 1584   | Layout 1             | `d11cc94de7b4`  |
| 1579   | Layout 1             | `d11cc94de7b4`  |
| 1572   | Layout 1             | `d11cc94de7b4`  |
| 1565   | Layout 1             | `d11cc94de7b4`  |
| 1559   | Layout 1             | `d11cc94de7b4`  |
| 1554   | Layout 1             | `d11cc94de7b4`  |
| 1547   | Layout 1             | `d11cc94de7b4`  |
| 1537   | Layout 1             | `d11cc94de7b4`  |
| 1529   | Layout 1             | `d11cc94de7b4`  |
| 1524   | Layout 1             | `d11cc94de7b4`  |
| 1519   | Layout 1             | `d11cc94de7b4`  |
| 1509   | Layout 1             | `d11cc94de7b4`  |
| 1506   | Layout 1             | `d11cc94de7b4`  |
| 1504   | Layout 1             | `d11cc94de7b4`  |
| 1500   | Layout 1             | `d11cc94de7b4`  |
| 1493   | Layout 1             | `d11cc94de7b4`  |
| 1489   | Layout 1             | `d11cc94de7b4`  |
| 1485   | Layout 1             | `d11cc94de7b4`  |
| 1481   | Layout 1             | `d11cc94de7b4`  |
| 1474   | Layout 1             | `d11cc94de7b4`  |
| 1466   | Layout 1             | `d11cc94de7b4`  |
| 1462   | Layout 1             | `d11cc94de7b4`  |
| 1459   | Layout 1             | `d11cc94de7b4`  |
| 1453   | Layout 1             | `d11cc94de7b4`  |
| 1450   | Layout 1             | `d11cc94de7b4`  |
| 1445   | Layout 1             | `d11cc94de7b4`  |
| 1439   | Layout 1             | `d11cc94de7b4`  |
| 1433   | Layout 1             | `d11cc94de7b4`  |
| 1430   | Layout 1             | `d11cc94de7b4`  |
| 1426   | Layout 1             | `d11cc94de7b4`  |
| 1421   | Layout 1             | `d11cc94de7b4`  |
| 1417   | Layout 1             | `d11cc94de7b4`  |
| 1416   | Layout 1             | `d11cc94de7b4`  |
| 1409   | Layout 1             | `d11cc94de7b4`  |
| 1405   | Layout 1             | `d11cc94de7b4`  |
| 1401   | Layout 1             | `d11cc94de7b4`  |
| 1396   | Layout 1             | `d11cc94de7b4`  |
| 1391   | Layout 1             | `d11cc94de7b4`  |
| 1390   | Layout 1             | `d11cc94de7b4`  |
| 1386   | Layout 1             | `d11cc94de7b4`  |
| 1381   | Layout 1             | `d11cc94de7b4`  |
| 1379   | Layout 1             | `d11cc94de7b4`  |
| 1372   | Layout 1             | `d11cc94de7b4`  |
| 1366   | Layout 1             | `d11cc94de7b4`  |
| 1364   | Layout 1             | `d11cc94de7b4`  |
| 1363   | Layout 1             | `d11cc94de7b4`  |
| 1360   | Layout 1             | `d11cc94de7b4`  |
| 1358   | Layout 1             | `d11cc94de7b4`  |
| 1355   | Layout 1             | `d11cc94de7b4`  |
| 1351   | Layout 1             | `d11cc94de7b4`  |
| 1348   | Layout 1             | `d11cc94de7b4`  |
| 1346   | Layout 1             | `d11cc94de7b4`  |
| 1341   | No documented layout | `d11cc94de7b4`  |
| 1340   | No documented layout | `d11cc94de7b4`  |
| 1338   | No documented layout | `d11cc94de7b4`  |
| 1335   | No documented layout | `d11cc94de7b4`  |
| 1333   | No documented layout | `d11cc94de7b4`  |
| 1329   | No documented layout | `d11cc94de7b4`  |
| 1327   | No documented layout | `d11cc94de7b4`  |
| 1324   | No documented layout | `d11cc94de7b4`  |
| 1321   | No documented layout | `d11cc94de7b4`  |
| 1319   | No documented layout | `d11cc94de7b4`  |
| 1318   | No documented layout | `d11cc94de7b4`  |
| 1316   | No documented layout | `d11cc94de7b4`  |
| 1313   | No documented layout | `d11cc94de7b4`  |
| 1311   | No file              | `d11cc94de7b4`  |
| 1309   | No file              | `d11cc94de7b4`  |
| 1304   | No file              | `d11cc94de7b4`  |
| 1292   | No file              | `d11cc94de7b4`  |
| 1286   | No file              | `d11cc94de7b4`  |
| 1280   | No file              | `d11cc94de7b4`  |
| 1276   | No file              | `d11cc94de7b4`  |
| 1267   | No file              | `d11cc94de7b4`  |
| 1261   | No file              | `d11cc94de7b4`  |
| 1256   | No file              | `d11cc94de7b4`  |
| 1250   | No file              | `d11cc94de7b4`  |
| 1246   | No file              | `d11cc94de7b4`  |
| 1239   | No file              | `d11cc94de7b4`  |
| 1230   | No file              | `d11cc94de7b4`  |
| 1226   | No file              | `d11cc94de7b4`  |
| 1220   | No file              | `d11cc94de7b4`  |
| 1217   | No file              | `d11cc94de7b4`  |
| 1211   | No file              | `d11cc94de7b4`  |
| 1210   | No file              | `d11cc94de7b4`  |
| 1208   | No file              | `d11cc94de7b4`  |
| 1203   | No file              | `d11cc94de7b4`  |
| 1197   | No file              | `d11cc94de7b4`  |
| 1194   | No file              | `d11cc94de7b4`  |
| 1192   | No file              | `d11cc94de7b4`  |
| 1187   | No file              | `d11cc94de7b4`  |
| 1183   | No file              | `d11cc94de7b4`  |
| 1177   | No file              | `d11cc94de7b4`  |
| 1173   | No file              | `d11cc94de7b4`  |
| 1167   | No file              | `d11cc94de7b4`  |
| 1164   | No file              | `d11cc94de7b4`  |
| 1156   | No file              | `d11cc94de7b4`  |
| 1149   | No file              | `d11cc94de7b4`  |
| 1144   | No file              | `d11cc94de7b4`  |
| 1137   | No file              | `d11cc94de7b4`  |
| 1132   | No file              | `d11cc94de7b4`  |
| 1127   | No file              | `d11cc94de7b4`  |
| 1122   | No file              | `d11cc94de7b4`  |
| 1118   | No file              | `d11cc94de7b4`  |
| 1114   | No file              | `d11cc94de7b4`  |
| 1109   | No file              | `d11cc94de7b4`  |
| 1102   | No file              | `d11cc94de7b4`  |
| 1096   | No file              | `d11cc94de7b4`  |
| 1088   | No file              | `d11cc94de7b4`  |
| 1081   | No file              | `d11cc94de7b4`  |
| 1076   | No file              | `d11cc94de7b4`  |
| 1069   | No file              | `d11cc94de7b4`  |
| 1064   | No file              | `d11cc94de7b4`  |
| 1058   | No file              | `d11cc94de7b4`  |
| 1051   | No file              | `d11cc94de7b4`  |
| 1044   | No file              | `d11cc94de7b4`  |
| 1036   | No file              | `d11cc94de7b4`  |
| 1026   | No file              | `d11cc94de7b4`  |
| 1016   | No file              | `d11cc94de7b4`  |
| 1009   | No file              | `d11cc94de7b4`  |
| 1005   | No file              | `d11cc94de7b4`  |
| 1000   | No file              | `d11cc94de7b4`  |
| 998    | No file              | `d11cc94de7b4`  |
| 990    | No file              | `d11cc94de7b4`  |
| 979    | No file              | `d11cc94de7b4`  |
| 972    | No file              | `d11cc94de7b4`  |
| 963    | No file              | `d11cc94de7b4`  |
| 955    | No file              | `d11cc94de7b4`  |
| 946    | No file              | `d11cc94de7b4`  |
| 938    | No file              | `d11cc94de7b4`  |
| 927    | No file              | `d11cc94de7b4`  |
| 911    | No file              | `d11cc94de7b4`  |
| 904    | No file              | `d11cc94de7b4`  |
| 899    | No file              | `d11cc94de7b4`  |
| 894    | No file              | `d11cc94de7b4`  |
| 885    | No file              | `d11cc94de7b4`  |
| 879    | No file              | `d11cc94de7b4`  |
| 872    | No file              | `d11cc94de7b4`  |
| 864    | No file              | `d11cc94de7b4`  |
| 855    | No file              | `d11cc94de7b4`  |
| 853    | No file              | `d11cc94de7b4`  |
| 845    | No file              | `d11cc94de7b4`  |
| 837    | No file              | `d11cc94de7b4`  |
| 829    | No file              | `d11cc94de7b4`  |
| 822    | No file              | `d11cc94de7b4`  |
| 814    | No file              | `d11cc94de7b4`  |
| 805    | No file              | `d11cc94de7b4`  |
| 794    | No file              | `d11cc94de7b4`  |
| 787    | No file              | `d11cc94de7b4`  |
| 780    | No file              | `d11cc94de7b4`  |
| 771    | No file              | `d11cc94de7b4`  |
| 760    | No file              | `d11cc94de7b4`  |
| 748    | No file              | `d11cc94de7b4`  |
| 741    | No file              | `d11cc94de7b4`  |
| 736    | No file              | `d11cc94de7b4`  |
| 731    | No file              | `d11cc94de7b4`  |
| 723    | No file              | `d11cc94de7b4`  |
| 711    | No file              | `d11cc94de7b4`  |
| 707    | No file              | `d11cc94de7b4`  |
| 697    | No file              | `d11cc94de7b4`  |
| 689    | No file              | `d11cc94de7b4`  |
| 683    | No file              | `d11cc94de7b4`  |
| 678    | No file              | `d11cc94de7b4`  |
| 670    | No file              | `d11cc94de7b4`  |
| 661    | No file              | `d11cc94de7b4`  |
| 656    | No file              | `d11cc94de7b4`  |
| 652    | No file              | `d11cc94de7b4`  |
| 643    | No file              | `d11cc94de7b4`  |
| 637    | No file              | `d11cc94de7b4`  |
| 630    | No file              | `d11cc94de7b4`  |
| 627    | No file              | `d11cc94de7b4`  |
| 621    | No file              | `d11cc94de7b4`  |
| 617    | No file              | `d11cc94de7b4`  |
| 615    | No file              | `d11cc94de7b4`  |
| 606    | No file              | `d11cc94de7b4`  |
| 599    | No file              | `d11cc94de7b4`  |
| 592    | No file              | `d11cc94de7b4`  |
| 586    | No file              | `d11cc94de7b4`  |
| 577    | No file              | `d11cc94de7b4`  |
| 569    | No file              | `d11cc94de7b4`  |
| 561    | No file              | `d11cc94de7b4`  |
| 554    | No file              | `d11cc94de7b4`  |
| 542    | No file              | `d11cc94de7b4`  |
| 532    | No file              | `d11cc94de7b4`  |
| 531    | No file              | `d11cc94de7b4`  |
| 526    | No file              | `d11cc94de7b4`  |
| 521    | No file              | `d11cc94de7b4`  |
| 517    | No file              | `d11cc94de7b4`  |
| 510    | No file              | `d11cc94de7b4`  |
| 508    | No file              | `d11cc94de7b4`  |
| 504    | No file              | `d11cc94de7b4`  |
| 497    | No file              | `d11cc94de7b4`  |
| 491    | No file              | `d11cc94de7b4`  |
| 485    | No file              | `d11cc94de7b4`  |
| 478    | No file              | `d11cc94de7b4`  |
| 472    | No file              | `d11cc94de7b4`  |
| 466    | No file              | `d11cc94de7b4`  |
| 457    | No file              | `d11cc94de7b4`  |
| 452    | No file              | `d11cc94de7b4`  |
| 449    | No file              | `d11cc94de7b4`  |
| 435    | No file              | `d11cc94de7b4`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                     |
| ----------------------------- | -------- | ---------------------------------------- |
| `fairyskillchangeoffset.dbss` | Optional | `level → (data_offset, data_size)` index |

The main file has a fixed record stride and a count in its header, so it can be scanned linearly without the offset companion. The index only matters for direct seeks by level.

All multi-byte values are little-endian.

## Layout 1

### File Layout

Total file size: 604 bytes = 4 (count) + 50 × 12 (records).

| Offset  | Type          | Field   | Notes                            |
| ------- | ------------- | ------- | -------------------------------- |
| `+0x00` | u32           | count   | Number of records; observed `50` |
| `+0x04` | Record[count] | records | See Record                       |

### Record (12 bytes)

| Offset  | Type | Field    | Notes                                              |
| ------- | ---- | -------- | -------------------------------------------------- |
| `+0x00` | u32  | key      | Record key, the fairy level; equals `level`       |
| `+0x04` | u32  | level    | Fairy level, `1`–`50`                              |
| `+0x08` | u32  | orb_cost | Theiah's Orbs required to reroll skills, `1`–`5`   |

The leading `key` is the file key prefix and is identical to `level` in all 50 observed records. The offset companion points at `record_start + 4`, so the addressable payload is the trailing 8 bytes (`level`, `orb_cost`).

### `fairyskillchangeoffset.dbss`

Total file size: 604 bytes = 4 (count) + 50 × 12 (rows).

| Offset  | Type              | Field | Notes                                           |
| ------- | ----------------- | ----- | ----------------------------------------------- |
| `+0x00` | u32               | count | Must equal `fairyskillchange.dbss` count (`50`) |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                  |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                 |
| ------- | ---- | ----------- | ----------------------------------------------------- |
| `+0x00` | u32  | level       | Fairy level key, `1`–`50`                             |
| `+0x04` | u32  | data_offset | Absolute offset in the main file, past the 4-byte key |
| `+0x08` | u32  | data_size   | Always `8` (`12 - 4-byte key prefix`)                 |

Rows appear in the same order as the main file's records, so `data_offset` runs `8, 20, 32, …` while the keys do not ascend. Recover the full record with `record_start = data_offset - 4`.

## Level → Orb Cost

All 50 levels are present exactly once.

| Theiah's Orbs | Levels | Count |
| ------------- | ------ | ----- |
| 1             | 1–19   | 19    |
| 2             | 20–29  | 10    |
| 3             | 30–39  | 10    |
| 4             | 40–49  | 10    |
| 5             | 50     | 1     |

The in-game cost table is usually quoted as starting at level 10 (`10`–`19` → 1 orb). The file covers levels `1`–`9` with the same cost of `1`; those rows are not reachable in practice, since a fairy is not rerolled below level 10.

## Record Order

Records are stored out of level order. The first stored keys are `47, 46, 45, 44, 43, 42, 41, 40`, and the file continues in descending runs that jump between bands. This is why the offset companion exists: a reader seeking a specific level must use the index rather than computing `4 + (level - 1) * 12`.


## Lookup Recipe

```python
def orb_cost_for_level(main: bytes, level: int) -> int | None:
    count = u32(main, 0)
    for index in range(count):
        pos = 4 + index * 12
        if u32(main, pos + 4) == level:
            return u32(main, pos + 8)
    return None
```

## Fairy Background

Context for reading this file and [fairyequipskill.bss](fairyequipskill_bss.md) together. These
mechanics are established in-game behaviour, not values decoded from this file:

Fairies come in four grades, Faint (tier 1, 10 levels, 2 skills), Glimmering (tier 2, 20 levels,
3 skills), Brilliant (tier 3, 30 levels, 4 skills) and Radiant (tier 4, 50 levels, 6 skills). Every
fairy starts with Gift (Luck +1) and learns one random additional skill every 10 levels.

Each learned skill rolls a random level of `1`–`5`, which is what the `I`–`V` ladders in the skill
catalog represent. Higher-grade fairies have better odds of higher skill levels, and only Radiant
fairies can roll level 4 or above.

## Notes

- Both files are exactly 604 bytes and carry the same record count, stride, and ordering.
- Observed rows: 50 in the pre-2026-09-27 fixture and 50 in the 2026-09-27 client; both files are byte-identical between the two.
- `key` and `level` are identical in every record, so the two cannot be told apart from this data alone; the split is inferred from where the offset companion points.
- No localization is involved: the format contains no strings and no LOC IDs.
- The cost bands are uneven: 1 orb covers 19 levels while 2–4 orbs cover 10 each and 5 orbs applies only at level 50.
- `orb_cost` is **not** a fairy grade. Fairy grades run `1`–`4` (Faint through Radiant); this field runs `1`–`5` and is keyed by level, not grade.
- The `1`–`5` range coincidentally matches the `I`–`V` skill-level ladders in the catalog. The two are unrelated: this field is a reroll price, and the catalog ladder is the rolled skill's level.

## Open Questions

### Relationship to the skill catalog

The two files are not keyed to each other. If this file were indexed by `equip_skill_id` it would have to include key `0` and stop at `34`; instead it starts at `1`, runs to `50`, and 16 of its keys (`35`–`50`) match no skill in the catalog, while the catalog's `equip_skill_id 0` has no key here. A reroll draws from the catalog, but the file that constrains *which* entries and at what skill level, the per-grade roll table implied by "only Radiant fairies can roll level 4+", has not been located.

### Record ordering

The data section is stored out of level order in descending runs that jump between cost bands. Whether that order carries meaning (patch history, an authoring-tool artifact, or an intentional grouping) or is arbitrary is unknown.
