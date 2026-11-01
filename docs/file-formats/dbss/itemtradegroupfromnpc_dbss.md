# `itemtradegroupfromnpc.dbss` Format

## Purpose

Item groups per NPC, the counterpart by name of
[`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md). On client 3473
the file holds no records: it is a u32 count of `0`, and so is its offset
file. On client 1784 it holds 125 groups of item entries with a trade
category, keyed by character key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes  | Records                  | Row bytes                  |
| ------ | -------------- | ---------------------------------- | ------ | ------------------------ | -------------------------- |
| 2      | 2414 and later | `itemtradegroupfromnpc.dbss`       | 4      | -                        | -                          |
| 2      | 2414 and later | `itemtradegroupfromnpcoffset.dbss` | 4      | -                        | -                          |
| 1      | 1329 to 2407   | `itemtradegroupfromnpc.dbss`       | 30,790 | 214 Item Entry, 36 Group | 123 to 159, 143 on average |
| 1      | 1329 to 2407   | `itemtradegroupfromnpcoffset.dbss` | 364    | 36 Index Row             | 10                         |

| Layout | File                               | Known             | Unknown    |
| ------ | ---------------------------------- | ----------------- | ---------- |
| 2      | `itemtradegroupfromnpc.dbss`       | 4 B (100.0%)      | 0 B (0.0%) |
| 2      | `itemtradegroupfromnpcoffset.dbss` | 4 B (100.0%)      | 0 B (0.0%) |
| 1      | `itemtradegroupfromnpc.dbss`       | 30,790 B (100.0%) | 0 B (0.0%) |
| 1      | `itemtradegroupfromnpcoffset.dbss` | 364 B (100.0%)    | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `3e954510d8d3`  |
| 3482   | Layout 2             | `3e954510d8d3`  |
| 3474   | Layout 2             | `3e954510d8d3`  |
| 3473   | Layout 2             | `3e954510d8d3`  |
| 3464   | Layout 2             | `3e954510d8d3`  |
| 3458   | Layout 2             | `3e954510d8d3`  |
| 3454   | Layout 2             | `3e954510d8d3`  |
| 3444   | Layout 2             | `3e954510d8d3`  |
| 3435   | Layout 2             | `3e954510d8d3`  |
| 3426   | Layout 2             | `3e954510d8d3`  |
| 3418   | Layout 2             | `3e954510d8d3`  |
| 3412   | Layout 2             | `3e954510d8d3`  |
| 3402   | Layout 2             | `3e954510d8d3`  |
| 3396   | Layout 2             | `3e954510d8d3`  |
| 3387   | Layout 2             | `3e954510d8d3`  |
| 3381   | Layout 2             | `3e954510d8d3`  |
| 3373   | Layout 2             | `3e954510d8d3`  |
| 3364   | Layout 2             | `3e954510d8d3`  |
| 3356   | Layout 2             | `3e954510d8d3`  |
| 3349   | Layout 2             | `3e954510d8d3`  |
| 3342   | Layout 2             | `3e954510d8d3`  |
| 3335   | Layout 2             | `3e954510d8d3`  |
| 3326   | Layout 2             | `3e954510d8d3`  |
| 3321   | Layout 2             | `3e954510d8d3`  |
| 3314   | Layout 2             | `3e954510d8d3`  |
| 3303   | Layout 2             | `3e954510d8d3`  |
| 3302   | Layout 2             | `3e954510d8d3`  |
| 3293   | Layout 2             | `3e954510d8d3`  |
| 3283   | Layout 2             | `3e954510d8d3`  |
| 3275   | Layout 2             | `3e954510d8d3`  |
| 3267   | Layout 2             | `3e954510d8d3`  |
| 3258   | Layout 2             | `3e954510d8d3`  |
| 3251   | Layout 2             | `3e954510d8d3`  |
| 3242   | Layout 2             | `3e954510d8d3`  |
| 3235   | Layout 2             | `3e954510d8d3`  |
| 3229   | Layout 2             | `3e954510d8d3`  |
| 3212   | Layout 2             | `3e954510d8d3`  |
| 3203   | Layout 2             | `3e954510d8d3`  |
| 3193   | Layout 2             | `3e954510d8d3`  |
| 3186   | Layout 2             | `3e954510d8d3`  |
| 3177   | Layout 2             | `3e954510d8d3`  |
| 3169   | Layout 2             | `3e954510d8d3`  |
| 3158   | Layout 2             | `3e954510d8d3`  |
| 3151   | Layout 2             | `3e954510d8d3`  |
| 3144   | Layout 2             | `3e954510d8d3`  |
| 3133   | Layout 2             | `3e954510d8d3`  |
| 3125   | Layout 2             | `3e954510d8d3`  |
| 3118   | Layout 2             | `3e954510d8d3`  |
| 3111   | Layout 2             | `3e954510d8d3`  |
| 3103   | Layout 2             | `3e954510d8d3`  |
| 3095   | Layout 2             | `3e954510d8d3`  |
| 3086   | Layout 2             | `3e954510d8d3`  |
| 3072   | Layout 2             | `3e954510d8d3`  |
| 3062   | Layout 2             | `3e954510d8d3`  |
| 3052   | Layout 2             | `3e954510d8d3`  |
| 3045   | Layout 2             | `3e954510d8d3`  |
| 3037   | Layout 2             | `3e954510d8d3`  |
| 3030   | Layout 2             | `3e954510d8d3`  |
| 3021   | Layout 2             | `3e954510d8d3`  |
| 3012   | Layout 2             | `3e954510d8d3`  |
| 3002   | Layout 2             | `3e954510d8d3`  |
| 2995   | Layout 2             | `3e954510d8d3`  |
| 2987   | Layout 2             | `3e954510d8d3`  |
| 2978   | Layout 2             | `3e954510d8d3`  |
| 2970   | Layout 2             | `3e954510d8d3`  |
| 2959   | Layout 2             | `3e954510d8d3`  |
| 2951   | Layout 2             | `3e954510d8d3`  |
| 2942   | Layout 2             | `3e954510d8d3`  |
| 2935   | Layout 2             | `3e954510d8d3`  |
| 2932   | Layout 2             | `3e954510d8d3`  |
| 2923   | Layout 2             | `3e954510d8d3`  |
| 2919   | Layout 2             | `3e954510d8d3`  |
| 2907   | Layout 2             | `3e954510d8d3`  |
| 2900   | Layout 2             | `3e954510d8d3`  |
| 2891   | Layout 2             | `3e954510d8d3`  |
| 2882   | Layout 2             | `3e954510d8d3`  |
| 2872   | Layout 2             | `3e954510d8d3`  |
| 2863   | Layout 2             | `3e954510d8d3`  |
| 2855   | Layout 2             | `3e954510d8d3`  |
| 2849   | Layout 2             | `3e954510d8d3`  |
| 2844   | Layout 2             | `3e954510d8d3`  |
| 2834   | Layout 2             | `3e954510d8d3`  |
| 2825   | Layout 2             | `3e954510d8d3`  |
| 2819   | Layout 2             | `3e954510d8d3`  |
| 2811   | Layout 2             | `3e954510d8d3`  |
| 2803   | Layout 2             | `3e954510d8d3`  |
| 2794   | Layout 2             | `3e954510d8d3`  |
| 2783   | Layout 2             | `3e954510d8d3`  |
| 2774   | Layout 2             | `3e954510d8d3`  |
| 2765   | Layout 2             | `3e954510d8d3`  |
| 2756   | Layout 2             | `3e954510d8d3`  |
| 2750   | Layout 2             | `3e954510d8d3`  |
| 2743   | Layout 2             | `3e954510d8d3`  |
| 2736   | Layout 2             | `3e954510d8d3`  |
| 2726   | Layout 2             | `3e954510d8d3`  |
| 2717   | Layout 2             | `3e954510d8d3`  |
| 2709   | Layout 2             | `3e954510d8d3`  |
| 2703   | Layout 2             | `3e954510d8d3`  |
| 2695   | Layout 2             | `3e954510d8d3`  |
| 2684   | Layout 2             | `3e954510d8d3`  |
| 2672   | Layout 2             | `3e954510d8d3`  |
| 2665   | Layout 2             | `3e954510d8d3`  |
| 2657   | Layout 2             | `3e954510d8d3`  |
| 2649   | Layout 2             | `3e954510d8d3`  |
| 2644   | Layout 2             | `3e954510d8d3`  |
| 2637   | Layout 2             | `3e954510d8d3`  |
| 2629   | Layout 2             | `3e954510d8d3`  |
| 2619   | Layout 2             | `3e954510d8d3`  |
| 2612   | Layout 2             | `3e954510d8d3`  |
| 2606   | Layout 2             | `3e954510d8d3`  |
| 2602   | Layout 2             | `3e954510d8d3`  |
| 2601   | Layout 2             | `3e954510d8d3`  |
| 2592   | Layout 2             | `3e954510d8d3`  |
| 2583   | Layout 2             | `3e954510d8d3`  |
| 2575   | Layout 2             | `3e954510d8d3`  |
| 2567   | Layout 2             | `3e954510d8d3`  |
| 2560   | Layout 2             | `3e954510d8d3`  |
| 2553   | Layout 2             | `3e954510d8d3`  |
| 2545   | Layout 2             | `3e954510d8d3`  |
| 2538   | Layout 2             | `3e954510d8d3`  |
| 2529   | Layout 2             | `3e954510d8d3`  |
| 2519   | Layout 2             | `3e954510d8d3`  |
| 2513   | Layout 2             | `3e954510d8d3`  |
| 2510   | Layout 2             | `3e954510d8d3`  |
| 2507   | Layout 2             | `3e954510d8d3`  |
| 2503   | Layout 2             | `3e954510d8d3`  |
| 2498   | Layout 2             | `3e954510d8d3`  |
| 2492   | Layout 2             | `3e954510d8d3`  |
| 2487   | Layout 2             | `3e954510d8d3`  |
| 2480   | Layout 2             | `3e954510d8d3`  |
| 2474   | Layout 2             | `3e954510d8d3`  |
| 2468   | Layout 2             | `3e954510d8d3`  |
| 2460   | Layout 2             | `3e954510d8d3`  |
| 2453   | Layout 2             | `3e954510d8d3`  |
| 2444   | Layout 2             | `3e954510d8d3`  |
| 2438   | Layout 2             | `3e954510d8d3`  |
| 2434   | Layout 2             | `3e954510d8d3`  |
| 2429   | Layout 2             | `3e954510d8d3`  |
| 2421   | Layout 2             | `3e954510d8d3`  |
| 2414   | Layout 2             | `3e954510d8d3`  |
| 2407   | Layout 1             | `3e954510d8d3`  |
| 2401   | Layout 1             | `3e954510d8d3`  |
| 2397   | Layout 1             | `3e954510d8d3`  |
| 2393   | Layout 1             | `3e954510d8d3`  |
| 2384   | Layout 1             | `3e954510d8d3`  |
| 2378   | Layout 1             | `3e954510d8d3`  |
| 2372   | Layout 1             | `3e954510d8d3`  |
| 2358   | Layout 1             | `3e954510d8d3`  |
| 2352   | Layout 1             | `3e954510d8d3`  |
| 2347   | Layout 1             | `3e954510d8d3`  |
| 2343   | Layout 1             | `3e954510d8d3`  |
| 2335   | Layout 1             | `3e954510d8d3`  |
| 2327   | Layout 1             | `3e954510d8d3`  |
| 2324   | Layout 1             | `3e954510d8d3`  |
| 2319   | Layout 1             | `3e954510d8d3`  |
| 2313   | Layout 1             | `3e954510d8d3`  |
| 2308   | Layout 1             | `3e954510d8d3`  |
| 2302   | Layout 1             | `3e954510d8d3`  |
| 2295   | Layout 1             | `3e954510d8d3`  |
| 2290   | Layout 1             | `3e954510d8d3`  |
| 2284   | Layout 1             | `3e954510d8d3`  |
| 2276   | Layout 1             | `3e954510d8d3`  |
| 2269   | Layout 1             | `3e954510d8d3`  |
| 2259   | Layout 1             | `3e954510d8d3`  |
| 2250   | Layout 1             | `3e954510d8d3`  |
| 2243   | Layout 1             | `3e954510d8d3`  |
| 2235   | Layout 1             | `3e954510d8d3`  |
| 2229   | Layout 1             | `3e954510d8d3`  |
| 2224   | Layout 1             | `3e954510d8d3`  |
| 2218   | Layout 1             | `3e954510d8d3`  |
| 2215   | Layout 1             | `3e954510d8d3`  |
| 2207   | Layout 1             | `3e954510d8d3`  |
| 2203   | Layout 1             | `3e954510d8d3`  |
| 2196   | Layout 1             | `3e954510d8d3`  |
| 2192   | Layout 1             | `3e954510d8d3`  |
| 2189   | Layout 1             | `3e954510d8d3`  |
| 2183   | Layout 1             | `3e954510d8d3`  |
| 2179   | Layout 1             | `3e954510d8d3`  |
| 2171   | Layout 1             | `3e954510d8d3`  |
| 2163   | Layout 1             | `3e954510d8d3`  |
| 2156   | Layout 1             | `3e954510d8d3`  |
| 2151   | Layout 1             | `3e954510d8d3`  |
| 2147   | Layout 1             | `3e954510d8d3`  |
| 2142   | Layout 1             | `3e954510d8d3`  |
| 2138   | Layout 1             | `3e954510d8d3`  |
| 2134   | Layout 1             | `3e954510d8d3`  |
| 2130   | Layout 1             | `3e954510d8d3`  |
| 2122   | Layout 1             | `3e954510d8d3`  |
| 2107   | Layout 1             | `3e954510d8d3`  |
| 2098   | Layout 1             | `3e954510d8d3`  |
| 2089   | Layout 1             | `3e954510d8d3`  |
| 2081   | Layout 1             | `3e954510d8d3`  |
| 2073   | Layout 1             | `3e954510d8d3`  |
| 2067   | Layout 1             | `3e954510d8d3`  |
| 2063   | Layout 1             | `3e954510d8d3`  |
| 2059   | Layout 1             | `3e954510d8d3`  |
| 2052   | Layout 1             | `3e954510d8d3`  |
| 2044   | Layout 1             | `3e954510d8d3`  |
| 2039   | Layout 1             | `3e954510d8d3`  |
| 2032   | Layout 1             | `3e954510d8d3`  |
| 2025   | Layout 1             | `3e954510d8d3`  |
| 2011   | Layout 1             | `3e954510d8d3`  |
| 2005   | Layout 1             | `3e954510d8d3`  |
| 2000   | Layout 1             | `3e954510d8d3`  |
| 1996   | Layout 1             | `3e954510d8d3`  |
| 1991   | Layout 1             | `3e954510d8d3`  |
| 1985   | Layout 1             | `3e954510d8d3`  |
| 1980   | Layout 1             | `3e954510d8d3`  |
| 1969   | Layout 1             | `3e954510d8d3`  |
| 1964   | Layout 1             | `3e954510d8d3`  |
| 1958   | Layout 1             | `3e954510d8d3`  |
| 1950   | Layout 1             | `3e954510d8d3`  |
| 1945   | Layout 1             | `3e954510d8d3`  |
| 1937   | Layout 1             | `3e954510d8d3`  |
| 1933   | Layout 1             | `3e954510d8d3`  |
| 1927   | Layout 1             | `3e954510d8d3`  |
| 1921   | Layout 1             | `3e954510d8d3`  |
| 1914   | Layout 1             | `3e954510d8d3`  |
| 1908   | Layout 1             | `3e954510d8d3`  |
| 1897   | Layout 1             | `3e954510d8d3`  |
| 1892   | Layout 1             | `3e954510d8d3`  |
| 1886   | Layout 1             | `3e954510d8d3`  |
| 1881   | Layout 1             | `3e954510d8d3`  |
| 1871   | Layout 1             | `3e954510d8d3`  |
| 1866   | Layout 1             | `3e954510d8d3`  |
| 1862   | Layout 1             | `3e954510d8d3`  |
| 1854   | Layout 1             | `3e954510d8d3`  |
| 1846   | Layout 1             | `3e954510d8d3`  |
| 1838   | Layout 1             | `3e954510d8d3`  |
| 1832   | Layout 1             | `3e954510d8d3`  |
| 1826   | Layout 1             | `3e954510d8d3`  |
| 1822   | Layout 1             | `3e954510d8d3`  |
| 1818   | Layout 1             | `3e954510d8d3`  |
| 1804   | Layout 1             | `3e954510d8d3`  |
| 1794   | Layout 1             | `3e954510d8d3`  |
| 1790   | Layout 1             | `3e954510d8d3`  |
| 1784   | Layout 1             | `3e954510d8d3`  |
| 1774   | Layout 1             | `3e954510d8d3`  |
| 1771   | Layout 1             | `3e954510d8d3`  |
| 1762   | Layout 1             | `3e954510d8d3`  |
| 1759   | Layout 1             | `3e954510d8d3`  |
| 1754   | Layout 1             | `3e954510d8d3`  |
| 1749   | Layout 1             | `3e954510d8d3`  |
| 1743   | Layout 1             | `3e954510d8d3`  |
| 1737   | Layout 1             | `3e954510d8d3`  |
| 1731   | Layout 1             | `3e954510d8d3`  |
| 1725   | Layout 1             | `3e954510d8d3`  |
| 1717   | Layout 1             | `3e954510d8d3`  |
| 1710   | Layout 1             | `3e954510d8d3`  |
| 1704   | Layout 1             | `3e954510d8d3`  |
| 1698   | Layout 1             | `3e954510d8d3`  |
| 1690   | Layout 1             | `3e954510d8d3`  |
| 1685   | Layout 1             | `3e954510d8d3`  |
| 1680   | Layout 1             | `3e954510d8d3`  |
| 1674   | Layout 1             | `3e954510d8d3`  |
| 1668   | Layout 1             | `3e954510d8d3`  |
| 1659   | Layout 1             | `3e954510d8d3`  |
| 1649   | Layout 1             | `3e954510d8d3`  |
| 1642   | Layout 1             | `3e954510d8d3`  |
| 1636   | Layout 1             | `3e954510d8d3`  |
| 1628   | Layout 1             | `3e954510d8d3`  |
| 1622   | Layout 1             | `3e954510d8d3`  |
| 1614   | Layout 1             | `3e954510d8d3`  |
| 1608   | Layout 1             | `3e954510d8d3`  |
| 1602   | Layout 1             | `3e954510d8d3`  |
| 1598   | Layout 1             | `3e954510d8d3`  |
| 1594   | Layout 1             | `3e954510d8d3`  |
| 1590   | Layout 1             | `3e954510d8d3`  |
| 1587   | Layout 1             | `3e954510d8d3`  |
| 1584   | Layout 1             | `3e954510d8d3`  |
| 1579   | Layout 1             | `3e954510d8d3`  |
| 1572   | Layout 1             | `3e954510d8d3`  |
| 1565   | Layout 1             | `3e954510d8d3`  |
| 1559   | Layout 1             | `3e954510d8d3`  |
| 1554   | Layout 1             | `3e954510d8d3`  |
| 1547   | Layout 1             | `3e954510d8d3`  |
| 1537   | Layout 1             | `3e954510d8d3`  |
| 1529   | Layout 1             | `3e954510d8d3`  |
| 1524   | Layout 1             | `3e954510d8d3`  |
| 1519   | Layout 1             | `3e954510d8d3`  |
| 1509   | Layout 1             | `3e954510d8d3`  |
| 1506   | Layout 1             | `3e954510d8d3`  |
| 1504   | Layout 1             | `3e954510d8d3`  |
| 1500   | Layout 1             | `3e954510d8d3`  |
| 1493   | Layout 1             | `3e954510d8d3`  |
| 1489   | Layout 1             | `3e954510d8d3`  |
| 1485   | Layout 1             | `3e954510d8d3`  |
| 1481   | Layout 1             | `3e954510d8d3`  |
| 1474   | Layout 1             | `3e954510d8d3`  |
| 1466   | Layout 1             | `3e954510d8d3`  |
| 1462   | Layout 1             | `3e954510d8d3`  |
| 1459   | Layout 1             | `3e954510d8d3`  |
| 1453   | Layout 1             | `3e954510d8d3`  |
| 1450   | Layout 1             | `3e954510d8d3`  |
| 1445   | Layout 1             | `3e954510d8d3`  |
| 1439   | Layout 1             | `3e954510d8d3`  |
| 1433   | Layout 1             | `3e954510d8d3`  |
| 1430   | Layout 1             | `3e954510d8d3`  |
| 1426   | Layout 1             | `3e954510d8d3`  |
| 1421   | Layout 1             | `3e954510d8d3`  |
| 1417   | Layout 1             | `3e954510d8d3`  |
| 1416   | Layout 1             | `3e954510d8d3`  |
| 1409   | Layout 1             | `3e954510d8d3`  |
| 1405   | Layout 1             | `3e954510d8d3`  |
| 1401   | Layout 1             | `3e954510d8d3`  |
| 1396   | Layout 1             | `3e954510d8d3`  |
| 1391   | Layout 1             | `3e954510d8d3`  |
| 1390   | Layout 1             | `3e954510d8d3`  |
| 1386   | Layout 1             | `3e954510d8d3`  |
| 1381   | Layout 1             | `3e954510d8d3`  |
| 1379   | Layout 1             | `3e954510d8d3`  |
| 1372   | Layout 1             | `3e954510d8d3`  |
| 1366   | Layout 1             | `3e954510d8d3`  |
| 1364   | Layout 1             | `3e954510d8d3`  |
| 1363   | Layout 1             | `3e954510d8d3`  |
| 1360   | Layout 1             | `3e954510d8d3`  |
| 1358   | Layout 1             | `3e954510d8d3`  |
| 1355   | Layout 1             | `3e954510d8d3`  |
| 1351   | Layout 1             | `3e954510d8d3`  |
| 1348   | Layout 1             | `3e954510d8d3`  |
| 1346   | Layout 1             | `3e954510d8d3`  |
| 1341   | Layout 1             | `3e954510d8d3`  |
| 1340   | Layout 1             | `3e954510d8d3`  |
| 1338   | Layout 1             | `3e954510d8d3`  |
| 1335   | Layout 1             | `3e954510d8d3`  |
| 1333   | Layout 1             | `3e954510d8d3`  |
| 1329   | Layout 1             | `3e954510d8d3`  |
| 1327   | No file              | `3e954510d8d3`  |
| 1324   | No file              | `3e954510d8d3`  |
| 1321   | No file              | `3e954510d8d3`  |
| 1319   | No file              | `3e954510d8d3`  |
| 1318   | No file              | `3e954510d8d3`  |
| 1316   | No file              | `3e954510d8d3`  |
| 1313   | No file              | `3e954510d8d3`  |
| 1311   | No documented layout | `3e954510d8d3`  |
| 1309   | No documented layout | `3e954510d8d3`  |
| 1304   | No documented layout | `3e954510d8d3`  |
| 1292   | No documented layout | `3e954510d8d3`  |
| 1286   | No documented layout | `3e954510d8d3`  |
| 1280   | No documented layout | `3e954510d8d3`  |
| 1276   | No documented layout | `3e954510d8d3`  |
| 1267   | No file              | `3e954510d8d3`  |
| 1261   | No file              | `3e954510d8d3`  |
| 1256   | No file              | `3e954510d8d3`  |
| 1250   | No file              | `3e954510d8d3`  |
| 1246   | No file              | `3e954510d8d3`  |
| 1239   | No file              | `3e954510d8d3`  |
| 1230   | No file              | `3e954510d8d3`  |
| 1226   | No file              | `3e954510d8d3`  |
| 1220   | No file              | `3e954510d8d3`  |
| 1217   | No file              | `3e954510d8d3`  |
| 1211   | No file              | `3e954510d8d3`  |
| 1210   | No file              | `3e954510d8d3`  |
| 1208   | No file              | `3e954510d8d3`  |
| 1203   | No file              | `3e954510d8d3`  |
| 1197   | No file              | `3e954510d8d3`  |
| 1194   | No file              | `3e954510d8d3`  |
| 1192   | No file              | `3e954510d8d3`  |
| 1187   | No file              | `3e954510d8d3`  |
| 1183   | No file              | `3e954510d8d3`  |
| 1177   | No file              | `3e954510d8d3`  |
| 1173   | No file              | `3e954510d8d3`  |
| 1167   | No file              | `3e954510d8d3`  |
| 1164   | No file              | `3e954510d8d3`  |
| 1156   | No file              | `3e954510d8d3`  |
| 1149   | No file              | `3e954510d8d3`  |
| 1144   | No file              | `3e954510d8d3`  |
| 1137   | No file              | `3e954510d8d3`  |
| 1132   | No file              | `3e954510d8d3`  |
| 1127   | No file              | `3e954510d8d3`  |
| 1122   | No file              | `3e954510d8d3`  |
| 1118   | No file              | `3e954510d8d3`  |
| 1114   | No file              | `3e954510d8d3`  |
| 1109   | No file              | `3e954510d8d3`  |
| 1102   | No file              | `3e954510d8d3`  |
| 1096   | No file              | `3e954510d8d3`  |
| 1088   | No file              | `3e954510d8d3`  |
| 1081   | No file              | `3e954510d8d3`  |
| 1076   | No file              | `3e954510d8d3`  |
| 1069   | No file              | `3e954510d8d3`  |
| 1064   | No file              | `3e954510d8d3`  |
| 1058   | No file              | `3e954510d8d3`  |
| 1051   | No file              | `3e954510d8d3`  |
| 1044   | No file              | `3e954510d8d3`  |
| 1036   | No file              | `3e954510d8d3`  |
| 1026   | No file              | `3e954510d8d3`  |
| 1016   | No file              | `3e954510d8d3`  |
| 1009   | No file              | `3e954510d8d3`  |
| 1005   | No file              | `3e954510d8d3`  |
| 1000   | No file              | `3e954510d8d3`  |
| 998    | No file              | `3e954510d8d3`  |
| 990    | No file              | `3e954510d8d3`  |
| 979    | No file              | `3e954510d8d3`  |
| 972    | No file              | `3e954510d8d3`  |
| 963    | No file              | `3e954510d8d3`  |
| 955    | No file              | `3e954510d8d3`  |
| 946    | No file              | `3e954510d8d3`  |
| 938    | No file              | `3e954510d8d3`  |
| 927    | No file              | `3e954510d8d3`  |
| 911    | No file              | `3e954510d8d3`  |
| 904    | No file              | `3e954510d8d3`  |
| 899    | No file              | `3e954510d8d3`  |
| 894    | No file              | `3e954510d8d3`  |
| 885    | No file              | `3e954510d8d3`  |
| 879    | No file              | `3e954510d8d3`  |
| 872    | No file              | `3e954510d8d3`  |
| 864    | No file              | `3e954510d8d3`  |
| 855    | No file              | `3e954510d8d3`  |
| 853    | No file              | `3e954510d8d3`  |
| 845    | No file              | `3e954510d8d3`  |
| 837    | No file              | `3e954510d8d3`  |
| 829    | No file              | `3e954510d8d3`  |
| 822    | No file              | `3e954510d8d3`  |
| 814    | No file              | `3e954510d8d3`  |
| 805    | No file              | `3e954510d8d3`  |
| 794    | No file              | `3e954510d8d3`  |
| 787    | No file              | `3e954510d8d3`  |
| 780    | No file              | `3e954510d8d3`  |
| 771    | No file              | `3e954510d8d3`  |
| 760    | No file              | `3e954510d8d3`  |
| 748    | No file              | `3e954510d8d3`  |
| 741    | No file              | `3e954510d8d3`  |
| 736    | No file              | `3e954510d8d3`  |
| 731    | No file              | `3e954510d8d3`  |
| 723    | No file              | `3e954510d8d3`  |
| 711    | No file              | `3e954510d8d3`  |
| 707    | No file              | `3e954510d8d3`  |
| 697    | No file              | `3e954510d8d3`  |
| 689    | No file              | `3e954510d8d3`  |
| 683    | No file              | `3e954510d8d3`  |
| 678    | No file              | `3e954510d8d3`  |
| 670    | No file              | `3e954510d8d3`  |
| 661    | No file              | `3e954510d8d3`  |
| 656    | No file              | `3e954510d8d3`  |
| 652    | No file              | `3e954510d8d3`  |
| 643    | No file              | `3e954510d8d3`  |
| 637    | No file              | `3e954510d8d3`  |
| 630    | No file              | `3e954510d8d3`  |
| 627    | No file              | `3e954510d8d3`  |
| 621    | No file              | `3e954510d8d3`  |
| 617    | No file              | `3e954510d8d3`  |
| 615    | No file              | `3e954510d8d3`  |
| 606    | No file              | `3e954510d8d3`  |
| 599    | No file              | `3e954510d8d3`  |
| 592    | No file              | `3e954510d8d3`  |
| 586    | No file              | `3e954510d8d3`  |
| 577    | No file              | `3e954510d8d3`  |
| 569    | No file              | `3e954510d8d3`  |
| 561    | No file              | `3e954510d8d3`  |
| 554    | No file              | `3e954510d8d3`  |
| 542    | No file              | `3e954510d8d3`  |
| 532    | No file              | `3e954510d8d3`  |
| 531    | No file              | `3e954510d8d3`  |
| 526    | No file              | `3e954510d8d3`  |
| 521    | No file              | `3e954510d8d3`  |
| 517    | No file              | `3e954510d8d3`  |
| 510    | No file              | `3e954510d8d3`  |
| 508    | No file              | `3e954510d8d3`  |
| 504    | No file              | `3e954510d8d3`  |
| 497    | No file              | `3e954510d8d3`  |
| 491    | No file              | `3e954510d8d3`  |
| 485    | No file              | `3e954510d8d3`  |
| 478    | No file              | `3e954510d8d3`  |
| 472    | No file              | `3e954510d8d3`  |
| 466    | No file              | `3e954510d8d3`  |
| 457    | No file              | `3e954510d8d3`  |
| 452    | No file              | `3e954510d8d3`  |
| 449    | No file              | `3e954510d8d3`  |
| 435    | No file              | `3e954510d8d3`  |

<!-- versions:end -->

## Companion Files

None. `itemtradegroupfromnpcoffset.dbss` is the offset file of this table;
the PAZ Browser reads both with the Layout 1 groups and the
`itemtradegrouptonpc.dbss` columns, so client 3473 shows an empty table and
client 1784 its 451 item entries.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type | Field | Notes                                |
| ------- | ---- | ----- | ------------------------------------ |
| `+0x00` | u32  | count | Number of groups; `0` on client 3473 |

### `itemtradegroupfromnpcoffset.dbss`

| Offset  | Type | Field | Notes                                         |
| ------- | ---- | ----- | --------------------------------------------- |
| `+0x00` | u32  | count | Equals the `itemtradegroupfromnpc.dbss` count |

## Layout 1

The structures below match the Layout 1 structures of
[`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md#layout-1): groups
of item entries that open with a counted condition string.

### File Layout

| Offset  | Type         | Field  | Notes                |
| ------- | ------------ | ------ | -------------------- |
| `+0x00` | u32          | count  | `125` on client 1784 |
| `+0x04` | Group[count] | groups | See Group            |

### Group (variable: 6 bytes + item entries)

| Offset  | Type                   | Field        | Notes                       |
| ------- | ---------------------- | ------------ | --------------------------- |
| `+0x00` | u16                    | character_id | Character key, LOC type `6` |
| `+0x02` | u32                    | item_count   | Number of item entries      |
| `+0x06` | Item Entry[item_count] | entries      | See Item Entry              |

### Item Entry (variable: 123 bytes + condition text)

The fields after the condition are the members of the
[`itemtradegrouptonpc.dbss` Layout 1](itemtradegrouptonpc_dbss.md#layout-1)
entry, which the server reads with the same row reader; see Field Names.
Counts are from client 1784.

| Offset           | Type  | Field                            | Notes                                                                 |
| ---------------- | ----- | -------------------------------- | --------------------------------------------------------------------- |
| `+0x00`          | u16   | character_id                     | Repeats the group key                                                 |
| `+0x02`          | u32   | item_id                          | Item key, LOC type `0`                                                |
| `+0x06`          | str16 | condition                        | Empty, or a condition such as `getlifeLevel(7)>41`; 316 of the 451 entries hold one |
| `condition+0x00` | i32   | max_price_rate                   | `0` in every entry, as is every field up to `trade_group_type`        |
| `condition+0x04` | i32   | event_max_price_rate             |                                                                       |
| `condition+0x08` | i32   | min_price_rate                   |                                                                       |
| `condition+0x0C` | i32   | steady_price_rate                |                                                                       |
| `condition+0x10` | i32   | vary_amount_rate_per_sell_or_buy |                                                                       |
| `condition+0x14` | i32   | vary_amount_rate_per_tick        |                                                                       |
| `condition+0x18` | i32   | event_price_rate_per_tick        |                                                                       |
| `condition+0x1C` | i32   | price_maintain_tick              |                                                                       |
| `condition+0x20` | i64   | steady_price_tick_count          |                                                                       |
| `condition+0x28` | u8    | trade_group_type                 | `0` in every entry                                                    |
| `condition+0x29` | u8    | is_sell_to_npc                   | `0` in every entry; `1` in every `itemtradegrouptonpc.dbss` entry     |
| `condition+0x2A` | i64   | min_price                        | `0` in every entry, as is every field up to `territory_supply_no`     |
| `condition+0x32` | i64   | max_price                        |                                                                       |
| `condition+0x3A` | i64   | buyable_stock_amount_per_tick    |                                                                       |
| `condition+0x42` | i32   | intimacy_variation               |                                                                       |
| `condition+0x46` | u8    | is_individual                    |                                                                       |
| `condition+0x47` | i16   | exploration_point                |                                                                       |
| `condition+0x49` | i32   | get_exp_rate                     |                                                                       |
| `condition+0x4D` | i64   | min_stock_amount                 |                                                                       |
| `condition+0x55` | i64   | max_stock_amount                 |                                                                       |
| `condition+0x5D` | u16   | territory_supply_no              |                                                                       |
| `condition+0x5F` | u16   | territory_trade_no               | Non-zero on 60 entries, such as `301` to `303`                        |
| `condition+0x61` | i32   | get_selling_trade_exp_rate       | `1000000` in every entry                                              |
| `condition+0x65` | i32   | event_price_rate_per_sell        | `0` in every entry                                                    |
| `condition+0x69` | u8    | is_for_magnate                   | `1` on 14 entries                                                     |
| `condition+0x6A` | u8    | trade_type                       | `0`, `1` or `2`                                                       |
| `condition+0x6B` | u8    | commerce_type                    | `1` to `9`                                                            |
| `condition+0x6C` | u8    | price_type                       | `0` in every entry                                                    |

Earlier versions of this doc called `condition` `unknown_condition`, the
members up to `trade_group_type` `unknown_condition_00`, `is_sell_to_npc`
`unknown_37`, the members up to `territory_supply_no` `unknown_38`,
`territory_supply_no` `unknown_6b`, the four members from
`territory_trade_no` to `is_for_magnate` `unknown_6d`, `trade_type`
`unknown_7c` and `price_type` `unknown_7e`.

### `itemtradegroupfromnpcoffset.dbss`

| Offset  | Type             | Field | Notes                                         |
| ------- | ---------------- | ----- | --------------------------------------------- |
| `+0x00` | u32              | count | Equals the `itemtradegroupfromnpc.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row                                 |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                     |
| ------- | ---- | ------------ | ------------------------- |
| `+0x00` | u16  | character_id | Group key                 |
| `+0x02` | u32  | offset       | Start of the group header |
| `+0x06` | u32  | size         | Length of the whole group |

## Field Names

The server dump of a private server on client 1784 reads this file and
`itemtradegrouptonpc.dbss` into the same `ItemTradeGroupStaticStatus` rows
with the same row reader; the member list, the 2016 names and the sheet
columns are in the
[`itemtradegrouptonpc.dbss` Field Names](itemtradegrouptonpc_dbss.md#field-names).
Its sheet loader fills them for this file from `BuyingFromNpc_Table`, the
only sheet it reads `BuyableStockAmountPerTick`, `IntimacyVariation`,
`TerritoryTrade_No` and `IsForMagnate` from.

On the official client 1784 file all 451 entries are in the
`BuyingFromNpc_Table` sheet of that server's `DataSheets.bexcel` by
(`NPCKey`, `ItemKey`), and the bytes match the sheet:

- `territory_trade_no` equals `TerritoryTrade_No` on all 451, 60 of them
  non-zero, and `is_for_magnate` equals `IsForMagnate` on all 451, 14 of
  them `1`. These two place the four members after `territory_supply_no`
  by value; in `itemtradegrouptonpc.dbss`, where all four are `0`, only
  order and width place them.
- `MaxPriceRate`, `MinPriceRate`, `SteadyPriceRate`,
  `varyAmountRatePerSellOrBuy`, `varyAmountRatePerTick`,
  `PriceMaintainTick`, `SteadyPriceTickCount`,
  `BuyableStockAmountPerTick` and `IntimacyVariation` are `0` on every
  sheet row, as are their bytes.
- `is_sell_to_npc` is `0` in every entry; the loader writes `1` for
  `SellingToNpc_Table` rows only.
- `get_selling_trade_exp_rate` is `1000000` in every entry. This sheet has
  no such column, so the value is not from the sheet.
- `trade_type`, `commerce_type` and `price_type` are the item's
  `Item_Table` columns, as in `itemtradegrouptonpc.dbss`. The sheet's own
  `commerceType` column equals `commerce_type` on 341 of the 451 entries
  only, so the file does not take it from the sheet.

## Open Questions

### Current Record Layout

Client 3473 ships no records, so whether a filled table would read as
the client 1784 groups or as the 127-byte Item Entry of
`itemtradegrouptonpc.dbss` Layout 2 is unknown. The handler reads
a filled table as Layout 1 and raises an error when the bytes do not fit it.
