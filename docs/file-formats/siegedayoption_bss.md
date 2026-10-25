# `siegedayoption.bss` Format

## Purpose

The Node War schedule: for each day of the week, Sunday to Saturday, the
territories whose nodes hold a node war that day. One record of seven
u64-counted lists of u16 territory keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes | Records                | Row bytes |
| ------ | -------------- | -------------------- | ----- | ---------------------- | --------- |
| 1      | 1250 and later | `siegedayoption.bss` | 108   | 1 Days, 1 String Table | 92        |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 1      | `siegedayoption.bss` | 108 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d2c8e91844d3`  |
| 3482   | Layout 1 | `d2c8e91844d3`  |
| 3474   | Layout 1 | `d2c8e91844d3`  |
| 3473   | Layout 1 | `d2c8e91844d3`  |
| 3464   | Layout 1 | `d2c8e91844d3`  |
| 3458   | Layout 1 | `d2c8e91844d3`  |
| 3454   | Layout 1 | `d2c8e91844d3`  |
| 3444   | Layout 1 | `d2c8e91844d3`  |
| 3435   | Layout 1 | `d2c8e91844d3`  |
| 3426   | Layout 1 | `d2c8e91844d3`  |
| 3418   | Layout 1 | `d2c8e91844d3`  |
| 3412   | Layout 1 | `d2c8e91844d3`  |
| 3402   | Layout 1 | `d2c8e91844d3`  |
| 3396   | Layout 1 | `d2c8e91844d3`  |
| 3387   | Layout 1 | `d2c8e91844d3`  |
| 3381   | Layout 1 | `d2c8e91844d3`  |
| 3373   | Layout 1 | `d2c8e91844d3`  |
| 3364   | Layout 1 | `d2c8e91844d3`  |
| 3356   | Layout 1 | `d2c8e91844d3`  |
| 3349   | Layout 1 | `d2c8e91844d3`  |
| 3342   | Layout 1 | `d2c8e91844d3`  |
| 3335   | Layout 1 | `d2c8e91844d3`  |
| 3326   | Layout 1 | `d2c8e91844d3`  |
| 3321   | Layout 1 | `d2c8e91844d3`  |
| 3314   | Layout 1 | `d2c8e91844d3`  |
| 3303   | Layout 1 | `d2c8e91844d3`  |
| 3302   | Layout 1 | `d2c8e91844d3`  |
| 3293   | Layout 1 | `d2c8e91844d3`  |
| 3283   | Layout 1 | `d2c8e91844d3`  |
| 3275   | Layout 1 | `d2c8e91844d3`  |
| 3267   | Layout 1 | `d2c8e91844d3`  |
| 3258   | Layout 1 | `d2c8e91844d3`  |
| 3251   | Layout 1 | `d2c8e91844d3`  |
| 3242   | Layout 1 | `d2c8e91844d3`  |
| 3235   | Layout 1 | `d2c8e91844d3`  |
| 3229   | Layout 1 | `d2c8e91844d3`  |
| 3212   | Layout 1 | `d2c8e91844d3`  |
| 3203   | Layout 1 | `d2c8e91844d3`  |
| 3193   | Layout 1 | `d2c8e91844d3`  |
| 3186   | Layout 1 | `d2c8e91844d3`  |
| 3177   | Layout 1 | `d2c8e91844d3`  |
| 3169   | Layout 1 | `d2c8e91844d3`  |
| 3158   | Layout 1 | `d2c8e91844d3`  |
| 3151   | Layout 1 | `d2c8e91844d3`  |
| 3144   | Layout 1 | `d2c8e91844d3`  |
| 3133   | Layout 1 | `d2c8e91844d3`  |
| 3125   | Layout 1 | `d2c8e91844d3`  |
| 3118   | Layout 1 | `d2c8e91844d3`  |
| 3111   | Layout 1 | `d2c8e91844d3`  |
| 3103   | Layout 1 | `d2c8e91844d3`  |
| 3095   | Layout 1 | `d2c8e91844d3`  |
| 3086   | Layout 1 | `d2c8e91844d3`  |
| 3072   | Layout 1 | `d2c8e91844d3`  |
| 3062   | Layout 1 | `d2c8e91844d3`  |
| 3052   | Layout 1 | `d2c8e91844d3`  |
| 3045   | Layout 1 | `d2c8e91844d3`  |
| 3037   | Layout 1 | `d2c8e91844d3`  |
| 3030   | Layout 1 | `d2c8e91844d3`  |
| 3021   | Layout 1 | `d2c8e91844d3`  |
| 3012   | Layout 1 | `d2c8e91844d3`  |
| 3002   | Layout 1 | `d2c8e91844d3`  |
| 2995   | Layout 1 | `d2c8e91844d3`  |
| 2987   | Layout 1 | `d2c8e91844d3`  |
| 2978   | Layout 1 | `d2c8e91844d3`  |
| 2970   | Layout 1 | `d2c8e91844d3`  |
| 2959   | Layout 1 | `d2c8e91844d3`  |
| 2951   | Layout 1 | `d2c8e91844d3`  |
| 2942   | Layout 1 | `d2c8e91844d3`  |
| 2935   | Layout 1 | `d2c8e91844d3`  |
| 2932   | Layout 1 | `d2c8e91844d3`  |
| 2923   | Layout 1 | `d2c8e91844d3`  |
| 2919   | Layout 1 | `d2c8e91844d3`  |
| 2907   | Layout 1 | `d2c8e91844d3`  |
| 2900   | Layout 1 | `d2c8e91844d3`  |
| 2891   | Layout 1 | `d2c8e91844d3`  |
| 2882   | Layout 1 | `d2c8e91844d3`  |
| 2872   | Layout 1 | `d2c8e91844d3`  |
| 2863   | Layout 1 | `d2c8e91844d3`  |
| 2855   | Layout 1 | `d2c8e91844d3`  |
| 2849   | Layout 1 | `d2c8e91844d3`  |
| 2844   | Layout 1 | `d2c8e91844d3`  |
| 2834   | Layout 1 | `d2c8e91844d3`  |
| 2825   | Layout 1 | `d2c8e91844d3`  |
| 2819   | Layout 1 | `d2c8e91844d3`  |
| 2811   | Layout 1 | `d2c8e91844d3`  |
| 2803   | Layout 1 | `d2c8e91844d3`  |
| 2794   | Layout 1 | `d2c8e91844d3`  |
| 2783   | Layout 1 | `d2c8e91844d3`  |
| 2774   | Layout 1 | `d2c8e91844d3`  |
| 2765   | Layout 1 | `d2c8e91844d3`  |
| 2756   | Layout 1 | `d2c8e91844d3`  |
| 2750   | Layout 1 | `d2c8e91844d3`  |
| 2743   | Layout 1 | `d2c8e91844d3`  |
| 2736   | Layout 1 | `d2c8e91844d3`  |
| 2726   | Layout 1 | `d2c8e91844d3`  |
| 2717   | Layout 1 | `d2c8e91844d3`  |
| 2709   | Layout 1 | `d2c8e91844d3`  |
| 2703   | Layout 1 | `d2c8e91844d3`  |
| 2695   | Layout 1 | `d2c8e91844d3`  |
| 2684   | Layout 1 | `d2c8e91844d3`  |
| 2672   | Layout 1 | `d2c8e91844d3`  |
| 2665   | Layout 1 | `d2c8e91844d3`  |
| 2657   | Layout 1 | `d2c8e91844d3`  |
| 2649   | Layout 1 | `d2c8e91844d3`  |
| 2644   | Layout 1 | `d2c8e91844d3`  |
| 2637   | Layout 1 | `d2c8e91844d3`  |
| 2629   | Layout 1 | `d2c8e91844d3`  |
| 2619   | Layout 1 | `d2c8e91844d3`  |
| 2612   | Layout 1 | `d2c8e91844d3`  |
| 2606   | Layout 1 | `d2c8e91844d3`  |
| 2602   | Layout 1 | `d2c8e91844d3`  |
| 2601   | Layout 1 | `d2c8e91844d3`  |
| 2592   | Layout 1 | `d2c8e91844d3`  |
| 2583   | Layout 1 | `d2c8e91844d3`  |
| 2575   | Layout 1 | `d2c8e91844d3`  |
| 2567   | Layout 1 | `d2c8e91844d3`  |
| 2560   | Layout 1 | `d2c8e91844d3`  |
| 2553   | Layout 1 | `d2c8e91844d3`  |
| 2545   | Layout 1 | `d2c8e91844d3`  |
| 2538   | Layout 1 | `d2c8e91844d3`  |
| 2529   | Layout 1 | `d2c8e91844d3`  |
| 2519   | Layout 1 | `d2c8e91844d3`  |
| 2513   | Layout 1 | `d2c8e91844d3`  |
| 2510   | Layout 1 | `d2c8e91844d3`  |
| 2507   | Layout 1 | `d2c8e91844d3`  |
| 2503   | Layout 1 | `d2c8e91844d3`  |
| 2498   | Layout 1 | `d2c8e91844d3`  |
| 2492   | Layout 1 | `d2c8e91844d3`  |
| 2487   | Layout 1 | `d2c8e91844d3`  |
| 2480   | Layout 1 | `d2c8e91844d3`  |
| 2474   | Layout 1 | `d2c8e91844d3`  |
| 2468   | Layout 1 | `d2c8e91844d3`  |
| 2460   | Layout 1 | `d2c8e91844d3`  |
| 2453   | Layout 1 | `d2c8e91844d3`  |
| 2444   | Layout 1 | `d2c8e91844d3`  |
| 2438   | Layout 1 | `d2c8e91844d3`  |
| 2434   | Layout 1 | `d2c8e91844d3`  |
| 2429   | Layout 1 | `d2c8e91844d3`  |
| 2421   | Layout 1 | `d2c8e91844d3`  |
| 2414   | Layout 1 | `d2c8e91844d3`  |
| 2407   | Layout 1 | `d2c8e91844d3`  |
| 2401   | Layout 1 | `d2c8e91844d3`  |
| 2397   | Layout 1 | `d2c8e91844d3`  |
| 2393   | Layout 1 | `d2c8e91844d3`  |
| 2384   | Layout 1 | `d2c8e91844d3`  |
| 2378   | Layout 1 | `d2c8e91844d3`  |
| 2372   | Layout 1 | `d2c8e91844d3`  |
| 2358   | Layout 1 | `d2c8e91844d3`  |
| 2352   | Layout 1 | `d2c8e91844d3`  |
| 2347   | Layout 1 | `d2c8e91844d3`  |
| 2343   | Layout 1 | `d2c8e91844d3`  |
| 2335   | Layout 1 | `d2c8e91844d3`  |
| 2327   | Layout 1 | `d2c8e91844d3`  |
| 2324   | Layout 1 | `d2c8e91844d3`  |
| 2319   | Layout 1 | `d2c8e91844d3`  |
| 2313   | Layout 1 | `d2c8e91844d3`  |
| 2308   | Layout 1 | `d2c8e91844d3`  |
| 2302   | Layout 1 | `d2c8e91844d3`  |
| 2295   | Layout 1 | `d2c8e91844d3`  |
| 2290   | Layout 1 | `d2c8e91844d3`  |
| 2284   | Layout 1 | `d2c8e91844d3`  |
| 2276   | Layout 1 | `d2c8e91844d3`  |
| 2269   | Layout 1 | `d2c8e91844d3`  |
| 2259   | Layout 1 | `d2c8e91844d3`  |
| 2250   | Layout 1 | `d2c8e91844d3`  |
| 2243   | Layout 1 | `d2c8e91844d3`  |
| 2235   | Layout 1 | `d2c8e91844d3`  |
| 2229   | Layout 1 | `d2c8e91844d3`  |
| 2224   | Layout 1 | `d2c8e91844d3`  |
| 2218   | Layout 1 | `d2c8e91844d3`  |
| 2215   | Layout 1 | `d2c8e91844d3`  |
| 2207   | Layout 1 | `d2c8e91844d3`  |
| 2203   | Layout 1 | `d2c8e91844d3`  |
| 2196   | Layout 1 | `d2c8e91844d3`  |
| 2192   | Layout 1 | `d2c8e91844d3`  |
| 2189   | Layout 1 | `d2c8e91844d3`  |
| 2183   | Layout 1 | `d2c8e91844d3`  |
| 2179   | Layout 1 | `d2c8e91844d3`  |
| 2171   | Layout 1 | `d2c8e91844d3`  |
| 2163   | Layout 1 | `d2c8e91844d3`  |
| 2156   | Layout 1 | `d2c8e91844d3`  |
| 2151   | Layout 1 | `d2c8e91844d3`  |
| 2147   | Layout 1 | `d2c8e91844d3`  |
| 2142   | Layout 1 | `d2c8e91844d3`  |
| 2138   | Layout 1 | `d2c8e91844d3`  |
| 2134   | Layout 1 | `d2c8e91844d3`  |
| 2130   | Layout 1 | `d2c8e91844d3`  |
| 2122   | Layout 1 | `d2c8e91844d3`  |
| 2107   | Layout 1 | `d2c8e91844d3`  |
| 2098   | Layout 1 | `d2c8e91844d3`  |
| 2089   | Layout 1 | `d2c8e91844d3`  |
| 2081   | Layout 1 | `d2c8e91844d3`  |
| 2073   | Layout 1 | `d2c8e91844d3`  |
| 2067   | Layout 1 | `d2c8e91844d3`  |
| 2063   | Layout 1 | `d2c8e91844d3`  |
| 2059   | Layout 1 | `d2c8e91844d3`  |
| 2052   | Layout 1 | `d2c8e91844d3`  |
| 2044   | Layout 1 | `d2c8e91844d3`  |
| 2039   | Layout 1 | `d2c8e91844d3`  |
| 2032   | Layout 1 | `d2c8e91844d3`  |
| 2025   | Layout 1 | `d2c8e91844d3`  |
| 2011   | Layout 1 | `d2c8e91844d3`  |
| 2005   | Layout 1 | `d2c8e91844d3`  |
| 2000   | Layout 1 | `d2c8e91844d3`  |
| 1996   | Layout 1 | `d2c8e91844d3`  |
| 1991   | Layout 1 | `d2c8e91844d3`  |
| 1985   | Layout 1 | `d2c8e91844d3`  |
| 1980   | Layout 1 | `d2c8e91844d3`  |
| 1969   | Layout 1 | `d2c8e91844d3`  |
| 1964   | Layout 1 | `d2c8e91844d3`  |
| 1958   | Layout 1 | `d2c8e91844d3`  |
| 1950   | Layout 1 | `d2c8e91844d3`  |
| 1945   | Layout 1 | `d2c8e91844d3`  |
| 1937   | Layout 1 | `d2c8e91844d3`  |
| 1933   | Layout 1 | `d2c8e91844d3`  |
| 1927   | Layout 1 | `d2c8e91844d3`  |
| 1921   | Layout 1 | `d2c8e91844d3`  |
| 1914   | Layout 1 | `d2c8e91844d3`  |
| 1908   | Layout 1 | `d2c8e91844d3`  |
| 1897   | Layout 1 | `d2c8e91844d3`  |
| 1892   | Layout 1 | `d2c8e91844d3`  |
| 1886   | Layout 1 | `d2c8e91844d3`  |
| 1881   | Layout 1 | `d2c8e91844d3`  |
| 1871   | Layout 1 | `d2c8e91844d3`  |
| 1866   | Layout 1 | `d2c8e91844d3`  |
| 1862   | Layout 1 | `d2c8e91844d3`  |
| 1854   | Layout 1 | `d2c8e91844d3`  |
| 1846   | Layout 1 | `d2c8e91844d3`  |
| 1838   | Layout 1 | `d2c8e91844d3`  |
| 1832   | Layout 1 | `d2c8e91844d3`  |
| 1826   | Layout 1 | `d2c8e91844d3`  |
| 1822   | Layout 1 | `d2c8e91844d3`  |
| 1818   | Layout 1 | `d2c8e91844d3`  |
| 1804   | Layout 1 | `d2c8e91844d3`  |
| 1794   | Layout 1 | `d2c8e91844d3`  |
| 1790   | Layout 1 | `d2c8e91844d3`  |
| 1784   | Layout 1 | `d2c8e91844d3`  |
| 1774   | Layout 1 | `d2c8e91844d3`  |
| 1771   | Layout 1 | `d2c8e91844d3`  |
| 1762   | Layout 1 | `d2c8e91844d3`  |
| 1759   | Layout 1 | `d2c8e91844d3`  |
| 1754   | Layout 1 | `d2c8e91844d3`  |
| 1749   | Layout 1 | `d2c8e91844d3`  |
| 1743   | Layout 1 | `d2c8e91844d3`  |
| 1737   | Layout 1 | `d2c8e91844d3`  |
| 1731   | Layout 1 | `d2c8e91844d3`  |
| 1725   | Layout 1 | `d2c8e91844d3`  |
| 1717   | Layout 1 | `d2c8e91844d3`  |
| 1710   | Layout 1 | `d2c8e91844d3`  |
| 1704   | Layout 1 | `d2c8e91844d3`  |
| 1698   | Layout 1 | `d2c8e91844d3`  |
| 1690   | Layout 1 | `d2c8e91844d3`  |
| 1685   | Layout 1 | `d2c8e91844d3`  |
| 1680   | Layout 1 | `d2c8e91844d3`  |
| 1674   | Layout 1 | `d2c8e91844d3`  |
| 1668   | Layout 1 | `d2c8e91844d3`  |
| 1659   | Layout 1 | `d2c8e91844d3`  |
| 1649   | Layout 1 | `d2c8e91844d3`  |
| 1642   | Layout 1 | `d2c8e91844d3`  |
| 1636   | Layout 1 | `d2c8e91844d3`  |
| 1628   | Layout 1 | `d2c8e91844d3`  |
| 1622   | Layout 1 | `d2c8e91844d3`  |
| 1614   | Layout 1 | `d2c8e91844d3`  |
| 1608   | Layout 1 | `d2c8e91844d3`  |
| 1602   | Layout 1 | `d2c8e91844d3`  |
| 1598   | Layout 1 | `d2c8e91844d3`  |
| 1594   | Layout 1 | `d2c8e91844d3`  |
| 1590   | Layout 1 | `d2c8e91844d3`  |
| 1587   | Layout 1 | `d2c8e91844d3`  |
| 1584   | Layout 1 | `d2c8e91844d3`  |
| 1579   | Layout 1 | `d2c8e91844d3`  |
| 1572   | Layout 1 | `d2c8e91844d3`  |
| 1565   | Layout 1 | `d2c8e91844d3`  |
| 1559   | Layout 1 | `d2c8e91844d3`  |
| 1554   | Layout 1 | `d2c8e91844d3`  |
| 1547   | Layout 1 | `d2c8e91844d3`  |
| 1537   | Layout 1 | `d2c8e91844d3`  |
| 1529   | Layout 1 | `d2c8e91844d3`  |
| 1524   | Layout 1 | `d2c8e91844d3`  |
| 1519   | Layout 1 | `d2c8e91844d3`  |
| 1509   | Layout 1 | `d2c8e91844d3`  |
| 1506   | Layout 1 | `d2c8e91844d3`  |
| 1504   | Layout 1 | `d2c8e91844d3`  |
| 1500   | Layout 1 | `d2c8e91844d3`  |
| 1493   | Layout 1 | `d2c8e91844d3`  |
| 1489   | Layout 1 | `d2c8e91844d3`  |
| 1485   | Layout 1 | `d2c8e91844d3`  |
| 1481   | Layout 1 | `d2c8e91844d3`  |
| 1474   | Layout 1 | `d2c8e91844d3`  |
| 1466   | Layout 1 | `d2c8e91844d3`  |
| 1462   | Layout 1 | `d2c8e91844d3`  |
| 1459   | Layout 1 | `d2c8e91844d3`  |
| 1453   | Layout 1 | `d2c8e91844d3`  |
| 1450   | Layout 1 | `d2c8e91844d3`  |
| 1445   | Layout 1 | `d2c8e91844d3`  |
| 1439   | Layout 1 | `d2c8e91844d3`  |
| 1433   | Layout 1 | `d2c8e91844d3`  |
| 1430   | Layout 1 | `d2c8e91844d3`  |
| 1426   | Layout 1 | `d2c8e91844d3`  |
| 1421   | Layout 1 | `d2c8e91844d3`  |
| 1417   | Layout 1 | `d2c8e91844d3`  |
| 1416   | Layout 1 | `d2c8e91844d3`  |
| 1409   | Layout 1 | `d2c8e91844d3`  |
| 1405   | Layout 1 | `d2c8e91844d3`  |
| 1401   | Layout 1 | `d2c8e91844d3`  |
| 1396   | Layout 1 | `d2c8e91844d3`  |
| 1391   | Layout 1 | `d2c8e91844d3`  |
| 1390   | Layout 1 | `d2c8e91844d3`  |
| 1386   | Layout 1 | `d2c8e91844d3`  |
| 1381   | Layout 1 | `d2c8e91844d3`  |
| 1379   | Layout 1 | `d2c8e91844d3`  |
| 1372   | Layout 1 | `d2c8e91844d3`  |
| 1366   | Layout 1 | `d2c8e91844d3`  |
| 1364   | Layout 1 | `d2c8e91844d3`  |
| 1363   | Layout 1 | `d2c8e91844d3`  |
| 1360   | Layout 1 | `d2c8e91844d3`  |
| 1358   | Layout 1 | `d2c8e91844d3`  |
| 1355   | Layout 1 | `d2c8e91844d3`  |
| 1351   | Layout 1 | `d2c8e91844d3`  |
| 1348   | Layout 1 | `d2c8e91844d3`  |
| 1346   | Layout 1 | `d2c8e91844d3`  |
| 1341   | Layout 1 | `d2c8e91844d3`  |
| 1340   | Layout 1 | `d2c8e91844d3`  |
| 1338   | Layout 1 | `d2c8e91844d3`  |
| 1335   | Layout 1 | `d2c8e91844d3`  |
| 1333   | Layout 1 | `d2c8e91844d3`  |
| 1329   | Layout 1 | `d2c8e91844d3`  |
| 1327   | Layout 1 | `d2c8e91844d3`  |
| 1324   | Layout 1 | `d2c8e91844d3`  |
| 1321   | Layout 1 | `d2c8e91844d3`  |
| 1319   | Layout 1 | `d2c8e91844d3`  |
| 1318   | Layout 1 | `d2c8e91844d3`  |
| 1316   | Layout 1 | `d2c8e91844d3`  |
| 1313   | Layout 1 | `d2c8e91844d3`  |
| 1311   | Layout 1 | `d2c8e91844d3`  |
| 1309   | Layout 1 | `d2c8e91844d3`  |
| 1304   | Layout 1 | `d2c8e91844d3`  |
| 1292   | Layout 1 | `d2c8e91844d3`  |
| 1286   | Layout 1 | `d2c8e91844d3`  |
| 1280   | Layout 1 | `d2c8e91844d3`  |
| 1276   | Layout 1 | `d2c8e91844d3`  |
| 1267   | Layout 1 | `d2c8e91844d3`  |
| 1261   | Layout 1 | `d2c8e91844d3`  |
| 1256   | Layout 1 | `d2c8e91844d3`  |
| 1250   | Layout 1 | `d2c8e91844d3`  |
| 1246   | No file  | `d2c8e91844d3`  |
| 1239   | No file  | `d2c8e91844d3`  |
| 1230   | No file  | `d2c8e91844d3`  |
| 1226   | No file  | `d2c8e91844d3`  |
| 1220   | No file  | `d2c8e91844d3`  |
| 1217   | No file  | `d2c8e91844d3`  |
| 1211   | No file  | `d2c8e91844d3`  |
| 1210   | No file  | `d2c8e91844d3`  |
| 1208   | No file  | `d2c8e91844d3`  |
| 1203   | No file  | `d2c8e91844d3`  |
| 1197   | No file  | `d2c8e91844d3`  |
| 1194   | No file  | `d2c8e91844d3`  |
| 1192   | No file  | `d2c8e91844d3`  |
| 1187   | No file  | `d2c8e91844d3`  |
| 1183   | No file  | `d2c8e91844d3`  |
| 1177   | No file  | `d2c8e91844d3`  |
| 1173   | No file  | `d2c8e91844d3`  |
| 1167   | No file  | `d2c8e91844d3`  |
| 1164   | No file  | `d2c8e91844d3`  |
| 1156   | No file  | `d2c8e91844d3`  |
| 1149   | No file  | `d2c8e91844d3`  |
| 1144   | No file  | `d2c8e91844d3`  |
| 1137   | No file  | `d2c8e91844d3`  |
| 1132   | No file  | `d2c8e91844d3`  |
| 1127   | No file  | `d2c8e91844d3`  |
| 1122   | No file  | `d2c8e91844d3`  |
| 1118   | No file  | `d2c8e91844d3`  |
| 1114   | No file  | `d2c8e91844d3`  |
| 1109   | No file  | `d2c8e91844d3`  |
| 1102   | No file  | `d2c8e91844d3`  |
| 1096   | No file  | `d2c8e91844d3`  |
| 1088   | No file  | `d2c8e91844d3`  |
| 1081   | No file  | `d2c8e91844d3`  |
| 1076   | No file  | `d2c8e91844d3`  |
| 1069   | No file  | `d2c8e91844d3`  |
| 1064   | No file  | `d2c8e91844d3`  |
| 1058   | No file  | `d2c8e91844d3`  |
| 1051   | No file  | `d2c8e91844d3`  |
| 1044   | No file  | `d2c8e91844d3`  |
| 1036   | No file  | `d2c8e91844d3`  |
| 1026   | No file  | `d2c8e91844d3`  |
| 1016   | No file  | `d2c8e91844d3`  |
| 1009   | No file  | `d2c8e91844d3`  |
| 1005   | No file  | `d2c8e91844d3`  |
| 1000   | No file  | `d2c8e91844d3`  |
| 998    | No file  | `d2c8e91844d3`  |
| 990    | No file  | `d2c8e91844d3`  |
| 979    | No file  | `d2c8e91844d3`  |
| 972    | No file  | `d2c8e91844d3`  |
| 963    | No file  | `d2c8e91844d3`  |
| 955    | No file  | `d2c8e91844d3`  |
| 946    | No file  | `d2c8e91844d3`  |
| 938    | No file  | `d2c8e91844d3`  |
| 927    | No file  | `d2c8e91844d3`  |
| 911    | No file  | `d2c8e91844d3`  |
| 904    | No file  | `d2c8e91844d3`  |
| 899    | No file  | `d2c8e91844d3`  |
| 894    | No file  | `d2c8e91844d3`  |
| 885    | No file  | `d2c8e91844d3`  |
| 879    | No file  | `d2c8e91844d3`  |
| 872    | No file  | `d2c8e91844d3`  |
| 864    | No file  | `d2c8e91844d3`  |
| 855    | No file  | `d2c8e91844d3`  |
| 853    | No file  | `d2c8e91844d3`  |
| 845    | No file  | `d2c8e91844d3`  |
| 837    | No file  | `d2c8e91844d3`  |
| 829    | No file  | `d2c8e91844d3`  |
| 822    | No file  | `d2c8e91844d3`  |
| 814    | No file  | `d2c8e91844d3`  |
| 805    | No file  | `d2c8e91844d3`  |
| 794    | No file  | `d2c8e91844d3`  |
| 787    | No file  | `d2c8e91844d3`  |
| 780    | No file  | `d2c8e91844d3`  |
| 771    | No file  | `d2c8e91844d3`  |
| 760    | No file  | `d2c8e91844d3`  |
| 748    | No file  | `d2c8e91844d3`  |
| 741    | No file  | `d2c8e91844d3`  |
| 736    | No file  | `d2c8e91844d3`  |
| 731    | No file  | `d2c8e91844d3`  |
| 723    | No file  | `d2c8e91844d3`  |
| 711    | No file  | `d2c8e91844d3`  |
| 707    | No file  | `d2c8e91844d3`  |
| 697    | No file  | `d2c8e91844d3`  |
| 689    | No file  | `d2c8e91844d3`  |
| 683    | No file  | `d2c8e91844d3`  |
| 678    | No file  | `d2c8e91844d3`  |
| 670    | No file  | `d2c8e91844d3`  |
| 661    | No file  | `d2c8e91844d3`  |
| 656    | No file  | `d2c8e91844d3`  |
| 652    | No file  | `d2c8e91844d3`  |
| 643    | No file  | `d2c8e91844d3`  |
| 637    | No file  | `d2c8e91844d3`  |
| 630    | No file  | `d2c8e91844d3`  |
| 627    | No file  | `d2c8e91844d3`  |
| 621    | No file  | `d2c8e91844d3`  |
| 617    | No file  | `d2c8e91844d3`  |
| 615    | No file  | `d2c8e91844d3`  |
| 606    | No file  | `d2c8e91844d3`  |
| 599    | No file  | `d2c8e91844d3`  |
| 592    | No file  | `d2c8e91844d3`  |
| 586    | No file  | `d2c8e91844d3`  |
| 577    | No file  | `d2c8e91844d3`  |
| 569    | No file  | `d2c8e91844d3`  |
| 561    | No file  | `d2c8e91844d3`  |
| 554    | No file  | `d2c8e91844d3`  |
| 542    | No file  | `d2c8e91844d3`  |
| 532    | No file  | `d2c8e91844d3`  |
| 531    | No file  | `d2c8e91844d3`  |
| 526    | No file  | `d2c8e91844d3`  |
| 521    | No file  | `d2c8e91844d3`  |
| 517    | No file  | `d2c8e91844d3`  |
| 510    | No file  | `d2c8e91844d3`  |
| 508    | No file  | `d2c8e91844d3`  |
| 504    | No file  | `d2c8e91844d3`  |
| 497    | No file  | `d2c8e91844d3`  |
| 491    | No file  | `d2c8e91844d3`  |
| 485    | No file  | `d2c8e91844d3`  |
| 478    | No file  | `d2c8e91844d3`  |
| 472    | No file  | `d2c8e91844d3`  |
| 466    | No file  | `d2c8e91844d3`  |
| 457    | No file  | `d2c8e91844d3`  |
| 452    | No file  | `d2c8e91844d3`  |
| 449    | No file  | `d2c8e91844d3`  |
| 435    | No file  | `d2c8e91844d3`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                           |
| ------------------- | ------------ | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                    |
| `+0x04`             | Days         | days         | See Days; no row count, the file has one record |
| `days+0x00`         | String Table | string_table | See String Table                                |
| `string_table+0x00` | u32          | table_start  | Offset of the string table, where `days` ends   |
| `string_table+0x04` | u32          | zero         | Always `0`                                      |

### Days (variable: 56 bytes + territory keys)

| Offset                       | Type                               | Field                          | Notes                                                                              |
| ---------------------------- | ---------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------- |
| `+0x00`                      | u64                                | sunday_territory_key_count     | Number of `sunday_territory_keys`                                                  |
| `+0x08`                      | u16[sunday_territory_key_count]    | sunday_territory_keys          | `territoryinfo.bss` keys, LOC type 12 names. See Schedule                          |
| `sunday_territory_keys+0x00` | u64                                | monday_territory_key_count     |                                                                                    |
| `sunday_territory_keys+0x08` | u16[monday_territory_key_count]    | monday_territory_keys          |                                                                                    |
| `monday_territory_keys+0x00` | u64                                | tuesday_territory_key_count    |                                                                                    |
| `monday_territory_keys+0x08` | u16[tuesday_territory_key_count]   | tuesday_territory_keys         |                                                                                    |
| `tuesday_territory_keys+0x00` | u64                               | wednesday_territory_key_count  |                                                                                    |
| `tuesday_territory_keys+0x08` | u16[wednesday_territory_key_count] | wednesday_territory_keys      |                                                                                    |
| `wednesday_territory_keys+0x00` | u64                             | thursday_territory_key_count   |                                                                                    |
| `wednesday_territory_keys+0x08` | u16[thursday_territory_key_count] | thursday_territory_keys      |                                                                                    |
| `thursday_territory_keys+0x00` | u64                              | friday_territory_key_count     |                                                                                    |
| `thursday_territory_keys+0x08` | u16[friday_territory_key_count]  | friday_territory_keys          |                                                                                    |
| `friday_territory_keys+0x00` | u64                                | saturday_territory_key_count   | `0` on every client checked                                                        |
| `friday_territory_keys+0x08` | u16[saturday_territory_key_count]  | saturday_territory_keys        |                                                                                    |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Schedule

The territories of each day. The keys are those of
`_eTerritoryKeyRaw` in `panel_window_villagesiegemenu_all.luac` (client
3482): `0` Balenos, `1` Serendia, `2` Calpheon, `3` Mediah, `4` Valencia,
`6` Kamasylvia.

| Day       | Client 3482                                           | Client 1784                                           |
| --------- | ----------------------------------------------------- | ----------------------------------------------------- |
| Sunday    | Balenos, Serendia, Calpheon, Mediah, Valencia, Kamasylvia | Balenos, Serendia, Calpheon, Mediah, Valencia, Kamasylvia |
| Monday    | Balenos, Calpheon, Kamasylvia                         | none                                                  |
| Tuesday   | Serendia, Mediah                                      | all six                                               |
| Wednesday | Calpheon, Valencia                                    | all six                                               |
| Thursday  | Balenos, Mediah, Kamasylvia                           | all six                                               |
| Friday    | Serendia, Valencia                                    | all six                                               |
| Saturday  | none                                                  | none                                                  |

## Field Names

The `MinorSiegeDayOption` sheet of a private server's `DataSheets.bexcel`
on client 1784 (Node War is `MinorSiege` in the client's names, the
Conquest War `MajorSiege`) has one row with the columns `Sunday` to
`Saturday`, each a comma list. All seven lists equal the lists of the
client 3482 file in order and value (7 of 7); `Saturday` is `<null>`.
The client 1784 file holds other lists: all six territories on Sunday
and Tuesday to Friday, none on Monday; its `ForeignMinorSiegeDayOption`
sheet has all six on Monday too. The day order is that of `CppEnums.VillageSiegeType` (Sunday `0`
to Saturday `6`).

## Notes

- The file holds no row count: `+0x04` starts the first list, and the
  string table follows the Saturday list.
- No client Lua reads the file; the node war menu takes the day from
  `ToClient_GetDayOfWeekByVillageSiege()`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: one column per day with the
  territory names.
