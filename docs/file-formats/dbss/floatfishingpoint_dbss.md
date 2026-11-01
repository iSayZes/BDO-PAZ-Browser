# `floatfishingpoint.dbss` Format

## Purpose

The fishing points that float on open water: per point its size, a start
and an end position, the fish drop group of
[`floatfishing.dbss`](floatfishing_dbss.md) it uses, and the character it
spawns there (`917` Fishing Point or `915` Clearwater Fishing Point) with an
action index. Companion `floatfishingpointoffset.dbss` lists where every row
sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                           | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------------------------------ | ------ | -------------- | --------- |
| 1      | 1267 and later | `floatfishingpoint.dbss`       | 16,888 | 402 Row        | 42        |
| 1      | 1267 and later | `floatfishingpointoffset.dbss` | 4,024  | 402 Offset Row | 10        |

| Layout | File                           | Known            | Unknown         |
| ------ | ------------------------------ | ---------------- | --------------- |
| 1      | `floatfishingpoint.dbss`       | 12,466 B (73.8%) | 4,422 B (26.2%) |
| 1      | `floatfishingpointoffset.dbss` | 4,024 B (100.0%) | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a408e18f62e5`  |
| 3482   | Layout 1 | `a408e18f62e5`  |
| 3474   | Layout 1 | `a408e18f62e5`  |
| 3473   | Layout 1 | `a408e18f62e5`  |
| 3464   | Layout 1 | `a408e18f62e5`  |
| 3458   | Layout 1 | `a408e18f62e5`  |
| 3454   | Layout 1 | `a408e18f62e5`  |
| 3444   | Layout 1 | `a408e18f62e5`  |
| 3435   | Layout 1 | `a408e18f62e5`  |
| 3426   | Layout 1 | `a408e18f62e5`  |
| 3418   | Layout 1 | `a408e18f62e5`  |
| 3412   | Layout 1 | `a408e18f62e5`  |
| 3402   | Layout 1 | `a408e18f62e5`  |
| 3396   | Layout 1 | `a408e18f62e5`  |
| 3387   | Layout 1 | `a408e18f62e5`  |
| 3381   | Layout 1 | `a408e18f62e5`  |
| 3373   | Layout 1 | `a408e18f62e5`  |
| 3364   | Layout 1 | `a408e18f62e5`  |
| 3356   | Layout 1 | `a408e18f62e5`  |
| 3349   | Layout 1 | `a408e18f62e5`  |
| 3342   | Layout 1 | `a408e18f62e5`  |
| 3335   | Layout 1 | `a408e18f62e5`  |
| 3326   | Layout 1 | `a408e18f62e5`  |
| 3321   | Layout 1 | `a408e18f62e5`  |
| 3314   | Layout 1 | `a408e18f62e5`  |
| 3303   | Layout 1 | `a408e18f62e5`  |
| 3302   | Layout 1 | `a408e18f62e5`  |
| 3293   | Layout 1 | `a408e18f62e5`  |
| 3283   | Layout 1 | `a408e18f62e5`  |
| 3275   | Layout 1 | `a408e18f62e5`  |
| 3267   | Layout 1 | `a408e18f62e5`  |
| 3258   | Layout 1 | `a408e18f62e5`  |
| 3251   | Layout 1 | `a408e18f62e5`  |
| 3242   | Layout 1 | `a408e18f62e5`  |
| 3235   | Layout 1 | `a408e18f62e5`  |
| 3229   | Layout 1 | `a408e18f62e5`  |
| 3212   | Layout 1 | `a408e18f62e5`  |
| 3203   | Layout 1 | `a408e18f62e5`  |
| 3193   | Layout 1 | `a408e18f62e5`  |
| 3186   | Layout 1 | `a408e18f62e5`  |
| 3177   | Layout 1 | `a408e18f62e5`  |
| 3169   | Layout 1 | `a408e18f62e5`  |
| 3158   | Layout 1 | `a408e18f62e5`  |
| 3151   | Layout 1 | `a408e18f62e5`  |
| 3144   | Layout 1 | `a408e18f62e5`  |
| 3133   | Layout 1 | `a408e18f62e5`  |
| 3125   | Layout 1 | `a408e18f62e5`  |
| 3118   | Layout 1 | `a408e18f62e5`  |
| 3111   | Layout 1 | `a408e18f62e5`  |
| 3103   | Layout 1 | `a408e18f62e5`  |
| 3095   | Layout 1 | `a408e18f62e5`  |
| 3086   | Layout 1 | `a408e18f62e5`  |
| 3072   | Layout 1 | `a408e18f62e5`  |
| 3062   | Layout 1 | `a408e18f62e5`  |
| 3052   | Layout 1 | `a408e18f62e5`  |
| 3045   | Layout 1 | `a408e18f62e5`  |
| 3037   | Layout 1 | `a408e18f62e5`  |
| 3030   | Layout 1 | `a408e18f62e5`  |
| 3021   | Layout 1 | `a408e18f62e5`  |
| 3012   | Layout 1 | `a408e18f62e5`  |
| 3002   | Layout 1 | `a408e18f62e5`  |
| 2995   | Layout 1 | `a408e18f62e5`  |
| 2987   | Layout 1 | `a408e18f62e5`  |
| 2978   | Layout 1 | `a408e18f62e5`  |
| 2970   | Layout 1 | `a408e18f62e5`  |
| 2959   | Layout 1 | `a408e18f62e5`  |
| 2951   | Layout 1 | `a408e18f62e5`  |
| 2942   | Layout 1 | `a408e18f62e5`  |
| 2935   | Layout 1 | `a408e18f62e5`  |
| 2932   | Layout 1 | `a408e18f62e5`  |
| 2923   | Layout 1 | `a408e18f62e5`  |
| 2919   | Layout 1 | `a408e18f62e5`  |
| 2907   | Layout 1 | `a408e18f62e5`  |
| 2900   | Layout 1 | `a408e18f62e5`  |
| 2891   | Layout 1 | `a408e18f62e5`  |
| 2882   | Layout 1 | `a408e18f62e5`  |
| 2872   | Layout 1 | `a408e18f62e5`  |
| 2863   | Layout 1 | `a408e18f62e5`  |
| 2855   | Layout 1 | `a408e18f62e5`  |
| 2849   | Layout 1 | `a408e18f62e5`  |
| 2844   | Layout 1 | `a408e18f62e5`  |
| 2834   | Layout 1 | `a408e18f62e5`  |
| 2825   | Layout 1 | `a408e18f62e5`  |
| 2819   | Layout 1 | `a408e18f62e5`  |
| 2811   | Layout 1 | `a408e18f62e5`  |
| 2803   | Layout 1 | `a408e18f62e5`  |
| 2794   | Layout 1 | `a408e18f62e5`  |
| 2783   | Layout 1 | `a408e18f62e5`  |
| 2774   | Layout 1 | `a408e18f62e5`  |
| 2765   | Layout 1 | `a408e18f62e5`  |
| 2756   | Layout 1 | `a408e18f62e5`  |
| 2750   | Layout 1 | `a408e18f62e5`  |
| 2743   | Layout 1 | `a408e18f62e5`  |
| 2736   | Layout 1 | `a408e18f62e5`  |
| 2726   | Layout 1 | `a408e18f62e5`  |
| 2717   | Layout 1 | `a408e18f62e5`  |
| 2709   | Layout 1 | `a408e18f62e5`  |
| 2703   | Layout 1 | `a408e18f62e5`  |
| 2695   | Layout 1 | `a408e18f62e5`  |
| 2684   | Layout 1 | `a408e18f62e5`  |
| 2672   | Layout 1 | `a408e18f62e5`  |
| 2665   | Layout 1 | `a408e18f62e5`  |
| 2657   | Layout 1 | `a408e18f62e5`  |
| 2649   | Layout 1 | `a408e18f62e5`  |
| 2644   | Layout 1 | `a408e18f62e5`  |
| 2637   | Layout 1 | `a408e18f62e5`  |
| 2629   | Layout 1 | `a408e18f62e5`  |
| 2619   | Layout 1 | `a408e18f62e5`  |
| 2612   | Layout 1 | `a408e18f62e5`  |
| 2606   | Layout 1 | `a408e18f62e5`  |
| 2602   | Layout 1 | `a408e18f62e5`  |
| 2601   | Layout 1 | `a408e18f62e5`  |
| 2592   | Layout 1 | `a408e18f62e5`  |
| 2583   | Layout 1 | `a408e18f62e5`  |
| 2575   | Layout 1 | `a408e18f62e5`  |
| 2567   | Layout 1 | `a408e18f62e5`  |
| 2560   | Layout 1 | `a408e18f62e5`  |
| 2553   | Layout 1 | `a408e18f62e5`  |
| 2545   | Layout 1 | `a408e18f62e5`  |
| 2538   | Layout 1 | `a408e18f62e5`  |
| 2529   | Layout 1 | `a408e18f62e5`  |
| 2519   | Layout 1 | `a408e18f62e5`  |
| 2513   | Layout 1 | `a408e18f62e5`  |
| 2510   | Layout 1 | `a408e18f62e5`  |
| 2507   | Layout 1 | `a408e18f62e5`  |
| 2503   | Layout 1 | `a408e18f62e5`  |
| 2498   | Layout 1 | `a408e18f62e5`  |
| 2492   | Layout 1 | `a408e18f62e5`  |
| 2487   | Layout 1 | `a408e18f62e5`  |
| 2480   | Layout 1 | `a408e18f62e5`  |
| 2474   | Layout 1 | `a408e18f62e5`  |
| 2468   | Layout 1 | `a408e18f62e5`  |
| 2460   | Layout 1 | `a408e18f62e5`  |
| 2453   | Layout 1 | `a408e18f62e5`  |
| 2444   | Layout 1 | `a408e18f62e5`  |
| 2438   | Layout 1 | `a408e18f62e5`  |
| 2434   | Layout 1 | `a408e18f62e5`  |
| 2429   | Layout 1 | `a408e18f62e5`  |
| 2421   | Layout 1 | `a408e18f62e5`  |
| 2414   | Layout 1 | `a408e18f62e5`  |
| 2407   | Layout 1 | `a408e18f62e5`  |
| 2401   | Layout 1 | `a408e18f62e5`  |
| 2397   | Layout 1 | `a408e18f62e5`  |
| 2393   | Layout 1 | `a408e18f62e5`  |
| 2384   | Layout 1 | `a408e18f62e5`  |
| 2378   | Layout 1 | `a408e18f62e5`  |
| 2372   | Layout 1 | `a408e18f62e5`  |
| 2358   | Layout 1 | `a408e18f62e5`  |
| 2352   | Layout 1 | `a408e18f62e5`  |
| 2347   | Layout 1 | `a408e18f62e5`  |
| 2343   | Layout 1 | `a408e18f62e5`  |
| 2335   | Layout 1 | `a408e18f62e5`  |
| 2327   | Layout 1 | `a408e18f62e5`  |
| 2324   | Layout 1 | `a408e18f62e5`  |
| 2319   | Layout 1 | `a408e18f62e5`  |
| 2313   | Layout 1 | `a408e18f62e5`  |
| 2308   | Layout 1 | `a408e18f62e5`  |
| 2302   | Layout 1 | `a408e18f62e5`  |
| 2295   | Layout 1 | `a408e18f62e5`  |
| 2290   | Layout 1 | `a408e18f62e5`  |
| 2284   | Layout 1 | `a408e18f62e5`  |
| 2276   | Layout 1 | `a408e18f62e5`  |
| 2269   | Layout 1 | `a408e18f62e5`  |
| 2259   | Layout 1 | `a408e18f62e5`  |
| 2250   | Layout 1 | `a408e18f62e5`  |
| 2243   | Layout 1 | `a408e18f62e5`  |
| 2235   | Layout 1 | `a408e18f62e5`  |
| 2229   | Layout 1 | `a408e18f62e5`  |
| 2224   | Layout 1 | `a408e18f62e5`  |
| 2218   | Layout 1 | `a408e18f62e5`  |
| 2215   | Layout 1 | `a408e18f62e5`  |
| 2207   | Layout 1 | `a408e18f62e5`  |
| 2203   | Layout 1 | `a408e18f62e5`  |
| 2196   | Layout 1 | `a408e18f62e5`  |
| 2192   | Layout 1 | `a408e18f62e5`  |
| 2189   | Layout 1 | `a408e18f62e5`  |
| 2183   | Layout 1 | `a408e18f62e5`  |
| 2179   | Layout 1 | `a408e18f62e5`  |
| 2171   | Layout 1 | `a408e18f62e5`  |
| 2163   | Layout 1 | `a408e18f62e5`  |
| 2156   | Layout 1 | `a408e18f62e5`  |
| 2151   | Layout 1 | `a408e18f62e5`  |
| 2147   | Layout 1 | `a408e18f62e5`  |
| 2142   | Layout 1 | `a408e18f62e5`  |
| 2138   | Layout 1 | `a408e18f62e5`  |
| 2134   | Layout 1 | `a408e18f62e5`  |
| 2130   | Layout 1 | `a408e18f62e5`  |
| 2122   | Layout 1 | `a408e18f62e5`  |
| 2107   | Layout 1 | `a408e18f62e5`  |
| 2098   | Layout 1 | `a408e18f62e5`  |
| 2089   | Layout 1 | `a408e18f62e5`  |
| 2081   | Layout 1 | `a408e18f62e5`  |
| 2073   | Layout 1 | `a408e18f62e5`  |
| 2067   | Layout 1 | `a408e18f62e5`  |
| 2063   | Layout 1 | `a408e18f62e5`  |
| 2059   | Layout 1 | `a408e18f62e5`  |
| 2052   | Layout 1 | `a408e18f62e5`  |
| 2044   | Layout 1 | `a408e18f62e5`  |
| 2039   | Layout 1 | `a408e18f62e5`  |
| 2032   | Layout 1 | `a408e18f62e5`  |
| 2025   | Layout 1 | `a408e18f62e5`  |
| 2011   | Layout 1 | `a408e18f62e5`  |
| 2005   | Layout 1 | `a408e18f62e5`  |
| 2000   | Layout 1 | `a408e18f62e5`  |
| 1996   | Layout 1 | `a408e18f62e5`  |
| 1991   | Layout 1 | `a408e18f62e5`  |
| 1985   | Layout 1 | `a408e18f62e5`  |
| 1980   | Layout 1 | `a408e18f62e5`  |
| 1969   | Layout 1 | `a408e18f62e5`  |
| 1964   | Layout 1 | `a408e18f62e5`  |
| 1958   | Layout 1 | `a408e18f62e5`  |
| 1950   | Layout 1 | `a408e18f62e5`  |
| 1945   | Layout 1 | `a408e18f62e5`  |
| 1937   | Layout 1 | `a408e18f62e5`  |
| 1933   | Layout 1 | `a408e18f62e5`  |
| 1927   | Layout 1 | `a408e18f62e5`  |
| 1921   | Layout 1 | `a408e18f62e5`  |
| 1914   | Layout 1 | `a408e18f62e5`  |
| 1908   | Layout 1 | `a408e18f62e5`  |
| 1897   | Layout 1 | `a408e18f62e5`  |
| 1892   | Layout 1 | `a408e18f62e5`  |
| 1886   | Layout 1 | `a408e18f62e5`  |
| 1881   | Layout 1 | `a408e18f62e5`  |
| 1871   | Layout 1 | `a408e18f62e5`  |
| 1866   | Layout 1 | `a408e18f62e5`  |
| 1862   | Layout 1 | `a408e18f62e5`  |
| 1854   | Layout 1 | `a408e18f62e5`  |
| 1846   | Layout 1 | `a408e18f62e5`  |
| 1838   | Layout 1 | `a408e18f62e5`  |
| 1832   | Layout 1 | `a408e18f62e5`  |
| 1826   | Layout 1 | `a408e18f62e5`  |
| 1822   | Layout 1 | `a408e18f62e5`  |
| 1818   | Layout 1 | `a408e18f62e5`  |
| 1804   | Layout 1 | `a408e18f62e5`  |
| 1794   | Layout 1 | `a408e18f62e5`  |
| 1790   | Layout 1 | `a408e18f62e5`  |
| 1784   | Layout 1 | `a408e18f62e5`  |
| 1774   | Layout 1 | `a408e18f62e5`  |
| 1771   | Layout 1 | `a408e18f62e5`  |
| 1762   | Layout 1 | `a408e18f62e5`  |
| 1759   | Layout 1 | `a408e18f62e5`  |
| 1754   | Layout 1 | `a408e18f62e5`  |
| 1749   | Layout 1 | `a408e18f62e5`  |
| 1743   | Layout 1 | `a408e18f62e5`  |
| 1737   | Layout 1 | `a408e18f62e5`  |
| 1731   | Layout 1 | `a408e18f62e5`  |
| 1725   | Layout 1 | `a408e18f62e5`  |
| 1717   | Layout 1 | `a408e18f62e5`  |
| 1710   | Layout 1 | `a408e18f62e5`  |
| 1704   | Layout 1 | `a408e18f62e5`  |
| 1698   | Layout 1 | `a408e18f62e5`  |
| 1690   | Layout 1 | `a408e18f62e5`  |
| 1685   | Layout 1 | `a408e18f62e5`  |
| 1680   | Layout 1 | `a408e18f62e5`  |
| 1674   | Layout 1 | `a408e18f62e5`  |
| 1668   | Layout 1 | `a408e18f62e5`  |
| 1659   | Layout 1 | `a408e18f62e5`  |
| 1649   | Layout 1 | `a408e18f62e5`  |
| 1642   | Layout 1 | `a408e18f62e5`  |
| 1636   | Layout 1 | `a408e18f62e5`  |
| 1628   | Layout 1 | `a408e18f62e5`  |
| 1622   | Layout 1 | `a408e18f62e5`  |
| 1614   | Layout 1 | `a408e18f62e5`  |
| 1608   | Layout 1 | `a408e18f62e5`  |
| 1602   | Layout 1 | `a408e18f62e5`  |
| 1598   | Layout 1 | `a408e18f62e5`  |
| 1594   | Layout 1 | `a408e18f62e5`  |
| 1590   | Layout 1 | `a408e18f62e5`  |
| 1587   | Layout 1 | `a408e18f62e5`  |
| 1584   | Layout 1 | `a408e18f62e5`  |
| 1579   | Layout 1 | `a408e18f62e5`  |
| 1572   | Layout 1 | `a408e18f62e5`  |
| 1565   | Layout 1 | `a408e18f62e5`  |
| 1559   | Layout 1 | `a408e18f62e5`  |
| 1554   | Layout 1 | `a408e18f62e5`  |
| 1547   | Layout 1 | `a408e18f62e5`  |
| 1537   | Layout 1 | `a408e18f62e5`  |
| 1529   | Layout 1 | `a408e18f62e5`  |
| 1524   | Layout 1 | `a408e18f62e5`  |
| 1519   | Layout 1 | `a408e18f62e5`  |
| 1509   | Layout 1 | `a408e18f62e5`  |
| 1506   | Layout 1 | `a408e18f62e5`  |
| 1504   | Layout 1 | `a408e18f62e5`  |
| 1500   | Layout 1 | `a408e18f62e5`  |
| 1493   | Layout 1 | `a408e18f62e5`  |
| 1489   | Layout 1 | `a408e18f62e5`  |
| 1485   | Layout 1 | `a408e18f62e5`  |
| 1481   | Layout 1 | `a408e18f62e5`  |
| 1474   | Layout 1 | `a408e18f62e5`  |
| 1466   | Layout 1 | `a408e18f62e5`  |
| 1462   | Layout 1 | `a408e18f62e5`  |
| 1459   | Layout 1 | `a408e18f62e5`  |
| 1453   | Layout 1 | `a408e18f62e5`  |
| 1450   | Layout 1 | `a408e18f62e5`  |
| 1445   | Layout 1 | `a408e18f62e5`  |
| 1439   | Layout 1 | `a408e18f62e5`  |
| 1433   | Layout 1 | `a408e18f62e5`  |
| 1430   | Layout 1 | `a408e18f62e5`  |
| 1426   | Layout 1 | `a408e18f62e5`  |
| 1421   | Layout 1 | `a408e18f62e5`  |
| 1417   | Layout 1 | `a408e18f62e5`  |
| 1416   | Layout 1 | `a408e18f62e5`  |
| 1409   | Layout 1 | `a408e18f62e5`  |
| 1405   | Layout 1 | `a408e18f62e5`  |
| 1401   | Layout 1 | `a408e18f62e5`  |
| 1396   | Layout 1 | `a408e18f62e5`  |
| 1391   | Layout 1 | `a408e18f62e5`  |
| 1390   | Layout 1 | `a408e18f62e5`  |
| 1386   | Layout 1 | `a408e18f62e5`  |
| 1381   | Layout 1 | `a408e18f62e5`  |
| 1379   | Layout 1 | `a408e18f62e5`  |
| 1372   | Layout 1 | `a408e18f62e5`  |
| 1366   | Layout 1 | `a408e18f62e5`  |
| 1364   | Layout 1 | `a408e18f62e5`  |
| 1363   | Layout 1 | `a408e18f62e5`  |
| 1360   | Layout 1 | `a408e18f62e5`  |
| 1358   | Layout 1 | `a408e18f62e5`  |
| 1355   | Layout 1 | `a408e18f62e5`  |
| 1351   | Layout 1 | `a408e18f62e5`  |
| 1348   | Layout 1 | `a408e18f62e5`  |
| 1346   | Layout 1 | `a408e18f62e5`  |
| 1341   | Layout 1 | `a408e18f62e5`  |
| 1340   | Layout 1 | `a408e18f62e5`  |
| 1338   | Layout 1 | `a408e18f62e5`  |
| 1335   | Layout 1 | `a408e18f62e5`  |
| 1333   | Layout 1 | `a408e18f62e5`  |
| 1329   | Layout 1 | `a408e18f62e5`  |
| 1327   | Layout 1 | `a408e18f62e5`  |
| 1324   | Layout 1 | `a408e18f62e5`  |
| 1321   | Layout 1 | `a408e18f62e5`  |
| 1319   | Layout 1 | `a408e18f62e5`  |
| 1318   | Layout 1 | `a408e18f62e5`  |
| 1316   | Layout 1 | `a408e18f62e5`  |
| 1313   | Layout 1 | `a408e18f62e5`  |
| 1311   | Layout 1 | `a408e18f62e5`  |
| 1309   | Layout 1 | `a408e18f62e5`  |
| 1304   | Layout 1 | `a408e18f62e5`  |
| 1292   | Layout 1 | `a408e18f62e5`  |
| 1286   | Layout 1 | `a408e18f62e5`  |
| 1280   | Layout 1 | `a408e18f62e5`  |
| 1276   | Layout 1 | `a408e18f62e5`  |
| 1267   | Layout 1 | `a408e18f62e5`  |
| 1261   | No file  | `a408e18f62e5`  |
| 1256   | No file  | `a408e18f62e5`  |
| 1250   | No file  | `a408e18f62e5`  |
| 1246   | No file  | `a408e18f62e5`  |
| 1239   | No file  | `a408e18f62e5`  |
| 1230   | No file  | `a408e18f62e5`  |
| 1226   | No file  | `a408e18f62e5`  |
| 1220   | No file  | `a408e18f62e5`  |
| 1217   | No file  | `a408e18f62e5`  |
| 1211   | No file  | `a408e18f62e5`  |
| 1210   | No file  | `a408e18f62e5`  |
| 1208   | No file  | `a408e18f62e5`  |
| 1203   | No file  | `a408e18f62e5`  |
| 1197   | No file  | `a408e18f62e5`  |
| 1194   | No file  | `a408e18f62e5`  |
| 1192   | No file  | `a408e18f62e5`  |
| 1187   | No file  | `a408e18f62e5`  |
| 1183   | No file  | `a408e18f62e5`  |
| 1177   | No file  | `a408e18f62e5`  |
| 1173   | No file  | `a408e18f62e5`  |
| 1167   | No file  | `a408e18f62e5`  |
| 1164   | No file  | `a408e18f62e5`  |
| 1156   | No file  | `a408e18f62e5`  |
| 1149   | No file  | `a408e18f62e5`  |
| 1144   | No file  | `a408e18f62e5`  |
| 1137   | No file  | `a408e18f62e5`  |
| 1132   | No file  | `a408e18f62e5`  |
| 1127   | No file  | `a408e18f62e5`  |
| 1122   | No file  | `a408e18f62e5`  |
| 1118   | No file  | `a408e18f62e5`  |
| 1114   | No file  | `a408e18f62e5`  |
| 1109   | No file  | `a408e18f62e5`  |
| 1102   | No file  | `a408e18f62e5`  |
| 1096   | No file  | `a408e18f62e5`  |
| 1088   | No file  | `a408e18f62e5`  |
| 1081   | No file  | `a408e18f62e5`  |
| 1076   | No file  | `a408e18f62e5`  |
| 1069   | No file  | `a408e18f62e5`  |
| 1064   | No file  | `a408e18f62e5`  |
| 1058   | No file  | `a408e18f62e5`  |
| 1051   | No file  | `a408e18f62e5`  |
| 1044   | No file  | `a408e18f62e5`  |
| 1036   | No file  | `a408e18f62e5`  |
| 1026   | No file  | `a408e18f62e5`  |
| 1016   | No file  | `a408e18f62e5`  |
| 1009   | No file  | `a408e18f62e5`  |
| 1005   | No file  | `a408e18f62e5`  |
| 1000   | No file  | `a408e18f62e5`  |
| 998    | No file  | `a408e18f62e5`  |
| 990    | No file  | `a408e18f62e5`  |
| 979    | No file  | `a408e18f62e5`  |
| 972    | No file  | `a408e18f62e5`  |
| 963    | No file  | `a408e18f62e5`  |
| 955    | No file  | `a408e18f62e5`  |
| 946    | No file  | `a408e18f62e5`  |
| 938    | No file  | `a408e18f62e5`  |
| 927    | No file  | `a408e18f62e5`  |
| 911    | No file  | `a408e18f62e5`  |
| 904    | No file  | `a408e18f62e5`  |
| 899    | No file  | `a408e18f62e5`  |
| 894    | No file  | `a408e18f62e5`  |
| 885    | No file  | `a408e18f62e5`  |
| 879    | No file  | `a408e18f62e5`  |
| 872    | No file  | `a408e18f62e5`  |
| 864    | No file  | `a408e18f62e5`  |
| 855    | No file  | `a408e18f62e5`  |
| 853    | No file  | `a408e18f62e5`  |
| 845    | No file  | `a408e18f62e5`  |
| 837    | No file  | `a408e18f62e5`  |
| 829    | No file  | `a408e18f62e5`  |
| 822    | No file  | `a408e18f62e5`  |
| 814    | No file  | `a408e18f62e5`  |
| 805    | No file  | `a408e18f62e5`  |
| 794    | No file  | `a408e18f62e5`  |
| 787    | No file  | `a408e18f62e5`  |
| 780    | No file  | `a408e18f62e5`  |
| 771    | No file  | `a408e18f62e5`  |
| 760    | No file  | `a408e18f62e5`  |
| 748    | No file  | `a408e18f62e5`  |
| 741    | No file  | `a408e18f62e5`  |
| 736    | No file  | `a408e18f62e5`  |
| 731    | No file  | `a408e18f62e5`  |
| 723    | No file  | `a408e18f62e5`  |
| 711    | No file  | `a408e18f62e5`  |
| 707    | No file  | `a408e18f62e5`  |
| 697    | No file  | `a408e18f62e5`  |
| 689    | No file  | `a408e18f62e5`  |
| 683    | No file  | `a408e18f62e5`  |
| 678    | No file  | `a408e18f62e5`  |
| 670    | No file  | `a408e18f62e5`  |
| 661    | No file  | `a408e18f62e5`  |
| 656    | No file  | `a408e18f62e5`  |
| 652    | No file  | `a408e18f62e5`  |
| 643    | No file  | `a408e18f62e5`  |
| 637    | No file  | `a408e18f62e5`  |
| 630    | No file  | `a408e18f62e5`  |
| 627    | No file  | `a408e18f62e5`  |
| 621    | No file  | `a408e18f62e5`  |
| 617    | No file  | `a408e18f62e5`  |
| 615    | No file  | `a408e18f62e5`  |
| 606    | No file  | `a408e18f62e5`  |
| 599    | No file  | `a408e18f62e5`  |
| 592    | No file  | `a408e18f62e5`  |
| 586    | No file  | `a408e18f62e5`  |
| 577    | No file  | `a408e18f62e5`  |
| 569    | No file  | `a408e18f62e5`  |
| 561    | No file  | `a408e18f62e5`  |
| 554    | No file  | `a408e18f62e5`  |
| 542    | No file  | `a408e18f62e5`  |
| 532    | No file  | `a408e18f62e5`  |
| 531    | No file  | `a408e18f62e5`  |
| 526    | No file  | `a408e18f62e5`  |
| 521    | No file  | `a408e18f62e5`  |
| 517    | No file  | `a408e18f62e5`  |
| 510    | No file  | `a408e18f62e5`  |
| 508    | No file  | `a408e18f62e5`  |
| 504    | No file  | `a408e18f62e5`  |
| 497    | No file  | `a408e18f62e5`  |
| 491    | No file  | `a408e18f62e5`  |
| 485    | No file  | `a408e18f62e5`  |
| 478    | No file  | `a408e18f62e5`  |
| 472    | No file  | `a408e18f62e5`  |
| 466    | No file  | `a408e18f62e5`  |
| 457    | No file  | `a408e18f62e5`  |
| 452    | No file  | `a408e18f62e5`  |
| 449    | No file  | `a408e18f62e5`  |
| 435    | No file  | `a408e18f62e5`  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                                                 |
| ------------------------------ | -------- | ------------------------------------------------------------------------------------ |
| `floatfishingpointoffset.dbss` | Optional | `point_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`          | Optional | Names of the spawned characters (type `6`)                                           |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then 42-byte rows; the
file ends after the last row.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 402 x 42 = 16,888 bytes.

### Row (42 bytes)

| Offset  | Type     | Field               | Notes                                                                              |
| ------- | -------- | ------------------- | ---------------------------------------------------------------------------------- |
| `+0x00` | u16      | point_key           | Unique; `1` to `426` on client 3474                                                |
| `+0x02` | u32      | point_size          | `2000` on the 229 rows that spawn `917`, `1000` on the 173 that spawn `915` (client 3474) |
| `+0x06` | f32      | start_position_x    | World position of one end of the point's line                                      |
| `+0x0A` | f32      | start_position_y    | Height; `-8241.4` to `4003.35` on client 3474                                      |
| `+0x0E` | f32      | start_position_z    |                                                                                    |
| `+0x12` | f32      | end_position_x      | World position of the other end                                                    |
| `+0x16` | bytes[4] | unknown_16          | `0` on every row of clients 1784 and 3474                                          |
| `+0x1A` | f32      | end_position_z      |                                                                                    |
| `+0x1E` | u16      | fishing_group_key   | Drop group in [`floatfishing.dbss`](floatfishing_dbss.md); equals `point_key` on every row of clients 1784 and 3474 |
| `+0x20` | bytes[4] | unknown_20          | `0` on every row of clients 1784 and 3474; see Open Questions                      |
| `+0x24` | u16      | spawn_character_key | Character spawned at the point: `917` Fishing Point or `915` Clearwater Fishing Point (LOC type 6) |
| `+0x26` | u8       | spawn_action_index  | `1` to `7` (no `6`); `1` on 203 rows (client 3474)                                 |
| `+0x27` | bytes[3] | unknown_27          | `0` on every row of clients 1784 and 3474                                          |

The rows are not sorted by key.

### `floatfishingpointoffset.dbss`

Bare offset table into `floatfishingpoint.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                     |
| ------- | ----------------- | ----- | ----------------------------------------- |
| `+0x00` | u32               | count | Equals the `floatfishingpoint.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                            |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | point_key   | Key of the row it points at                                        |
| `+0x02` | u32  | data_offset | Absolute offset of the row in `floatfishingpoint.dbss`, at its key |
| `+0x06` | u32  | data_size   | `42` on every row: the whole row                                   |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order, and on clients 1784 and 3474 every one points at
the row with its key.

## Field Names

The `FloatFishingPoint_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `PointKey`, `PointSize`, `StartPositionX`,
`StartPositionY`, `StartPositionZ`, `EndPositionX`, `EndPositionZ`,
`FishingGroupKey`, `SpawnRate`, `SpawnCharacterKey`, `SpawnActionIndex` and
`ContentsGroupKey`, in the order of the named fields above. Its 402 rows with
`ContentsGroupKey` `0` match the 402 rows of client 1784 on the key and all
nine named values (the positions to 0.1), 402 of 402. The developer comments
in `datasheet_regiondatatable.xlsm` call `PointSize` the point size,
`FishingGroupKey` the fish drop group, `SpawnCharacterKey` the character to
spawn at the point and `SpawnActionIndex` its action index.

## Notes

- The sheet has no `EndPositionY` column; `unknown_16` sits where a Y would
  between `end_position_x` and `end_position_z`.
- The sheet's eight rows with `ContentsGroupKey` `1633` (points `432` to
  `439`) are not in the client file; their groups are in `floatfishing.dbss`.
- Client 3474 holds the same 402 rows as client 1784, byte for byte.

## Open Questions

### unknown_20

`0` on every row of clients 1784 and 3474. It sits where the sheet's
`SpawnRate` column falls in column order, which carries the `%`
(server-only) prefix in `datasheet_regiondatatable.xlsm` and is `220000` on
point 1 there; a client build writes server-only columns as `0`. With only
zeros the file cannot confirm it.
