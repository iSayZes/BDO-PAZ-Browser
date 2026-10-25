# `mainquest.bss` Format

## Purpose

Defines the main-quest list: quest IDs grouped into main-quest chains, each group named by LOC type 43, with per quest a condition line (where and when it can be accepted) and two condition scripts. 120 groups and 3,268 quest references on client 3458. All text sits in a string table at the end of the file (Korean group names, Korean condition lines, scripts).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File            | Bytes   | Records                              | Row bytes |
| ------ | -------------- | --------------- | ------- | ------------------------------------ | --------- |
| 1      | 1304 and later | `mainquest.bss` | 447,220 | 3,269 Quest Reference Row, 120 Group | 17        |

| Layout | File            | Known             | Unknown      |
| ------ | --------------- | ----------------- | ------------ |
| 1      | `mainquest.bss` | 446,740 B (99.9%) | 480 B (0.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `b70f3a56726c`  |
| 3482   | Layout 1             | `b70f3a56726c`  |
| 3474   | Layout 1             | `b70f3a56726c`  |
| 3473   | Layout 1             | `b70f3a56726c`  |
| 3464   | Layout 1             | `b70f3a56726c`  |
| 3458   | Layout 1             | `b70f3a56726c`  |
| 3454   | Layout 1             | `b70f3a56726c`  |
| 3444   | Layout 1             | `b70f3a56726c`  |
| 3435   | Layout 1             | `b70f3a56726c`  |
| 3426   | Layout 1             | `b70f3a56726c`  |
| 3418   | Layout 1             | `b70f3a56726c`  |
| 3412   | Layout 1             | `b70f3a56726c`  |
| 3402   | Layout 1             | `b70f3a56726c`  |
| 3396   | Layout 1             | `b70f3a56726c`  |
| 3387   | Layout 1             | `b70f3a56726c`  |
| 3381   | Layout 1             | `b70f3a56726c`  |
| 3373   | Layout 1             | `b70f3a56726c`  |
| 3364   | Layout 1             | `b70f3a56726c`  |
| 3356   | Layout 1             | `b70f3a56726c`  |
| 3349   | Layout 1             | `b70f3a56726c`  |
| 3342   | Layout 1             | `b70f3a56726c`  |
| 3335   | Layout 1             | `b70f3a56726c`  |
| 3326   | Layout 1             | `b70f3a56726c`  |
| 3321   | Layout 1             | `b70f3a56726c`  |
| 3314   | Layout 1             | `b70f3a56726c`  |
| 3303   | Layout 1             | `b70f3a56726c`  |
| 3302   | Layout 1             | `b70f3a56726c`  |
| 3293   | Layout 1             | `b70f3a56726c`  |
| 3283   | Layout 1             | `b70f3a56726c`  |
| 3275   | Layout 1             | `b70f3a56726c`  |
| 3267   | Layout 1             | `b70f3a56726c`  |
| 3258   | Layout 1             | `b70f3a56726c`  |
| 3251   | Layout 1             | `b70f3a56726c`  |
| 3242   | Layout 1             | `b70f3a56726c`  |
| 3235   | Layout 1             | `b70f3a56726c`  |
| 3229   | Layout 1             | `b70f3a56726c`  |
| 3212   | Layout 1             | `b70f3a56726c`  |
| 3203   | Layout 1             | `b70f3a56726c`  |
| 3193   | Layout 1             | `b70f3a56726c`  |
| 3186   | Layout 1             | `b70f3a56726c`  |
| 3177   | Layout 1             | `b70f3a56726c`  |
| 3169   | Layout 1             | `b70f3a56726c`  |
| 3158   | Layout 1             | `b70f3a56726c`  |
| 3151   | Layout 1             | `b70f3a56726c`  |
| 3144   | Layout 1             | `b70f3a56726c`  |
| 3133   | Layout 1             | `b70f3a56726c`  |
| 3125   | Layout 1             | `b70f3a56726c`  |
| 3118   | Layout 1             | `b70f3a56726c`  |
| 3111   | Layout 1             | `b70f3a56726c`  |
| 3103   | Layout 1             | `b70f3a56726c`  |
| 3095   | Layout 1             | `b70f3a56726c`  |
| 3086   | Layout 1             | `b70f3a56726c`  |
| 3072   | Layout 1             | `b70f3a56726c`  |
| 3062   | Layout 1             | `b70f3a56726c`  |
| 3052   | Layout 1             | `b70f3a56726c`  |
| 3045   | Layout 1             | `b70f3a56726c`  |
| 3037   | Layout 1             | `b70f3a56726c`  |
| 3030   | Layout 1             | `b70f3a56726c`  |
| 3021   | Layout 1             | `b70f3a56726c`  |
| 3012   | Layout 1             | `b70f3a56726c`  |
| 3002   | Layout 1             | `b70f3a56726c`  |
| 2995   | Layout 1             | `b70f3a56726c`  |
| 2987   | Layout 1             | `b70f3a56726c`  |
| 2978   | Layout 1             | `b70f3a56726c`  |
| 2970   | Layout 1             | `b70f3a56726c`  |
| 2959   | Layout 1             | `b70f3a56726c`  |
| 2951   | Layout 1             | `b70f3a56726c`  |
| 2942   | Layout 1             | `b70f3a56726c`  |
| 2935   | Layout 1             | `b70f3a56726c`  |
| 2932   | Layout 1             | `b70f3a56726c`  |
| 2923   | Layout 1             | `b70f3a56726c`  |
| 2919   | Layout 1             | `b70f3a56726c`  |
| 2907   | Layout 1             | `b70f3a56726c`  |
| 2900   | Layout 1             | `b70f3a56726c`  |
| 2891   | Layout 1             | `b70f3a56726c`  |
| 2882   | Layout 1             | `b70f3a56726c`  |
| 2872   | Layout 1             | `b70f3a56726c`  |
| 2863   | Layout 1             | `b70f3a56726c`  |
| 2855   | Layout 1             | `b70f3a56726c`  |
| 2849   | Layout 1             | `b70f3a56726c`  |
| 2844   | Layout 1             | `b70f3a56726c`  |
| 2834   | Layout 1             | `b70f3a56726c`  |
| 2825   | Layout 1             | `b70f3a56726c`  |
| 2819   | Layout 1             | `b70f3a56726c`  |
| 2811   | Layout 1             | `b70f3a56726c`  |
| 2803   | Layout 1             | `b70f3a56726c`  |
| 2794   | Layout 1             | `b70f3a56726c`  |
| 2783   | Layout 1             | `b70f3a56726c`  |
| 2774   | Layout 1             | `b70f3a56726c`  |
| 2765   | Layout 1             | `b70f3a56726c`  |
| 2756   | Layout 1             | `b70f3a56726c`  |
| 2750   | Layout 1             | `b70f3a56726c`  |
| 2743   | Layout 1             | `b70f3a56726c`  |
| 2736   | Layout 1             | `b70f3a56726c`  |
| 2726   | Layout 1             | `b70f3a56726c`  |
| 2717   | Layout 1             | `b70f3a56726c`  |
| 2709   | Layout 1             | `b70f3a56726c`  |
| 2703   | Layout 1             | `b70f3a56726c`  |
| 2695   | Layout 1             | `b70f3a56726c`  |
| 2684   | Layout 1             | `b70f3a56726c`  |
| 2672   | Layout 1             | `b70f3a56726c`  |
| 2665   | Layout 1             | `b70f3a56726c`  |
| 2657   | Layout 1             | `b70f3a56726c`  |
| 2649   | Layout 1             | `b70f3a56726c`  |
| 2644   | Layout 1             | `b70f3a56726c`  |
| 2637   | Layout 1             | `b70f3a56726c`  |
| 2629   | Layout 1             | `b70f3a56726c`  |
| 2619   | Layout 1             | `b70f3a56726c`  |
| 2612   | Layout 1             | `b70f3a56726c`  |
| 2606   | Layout 1             | `b70f3a56726c`  |
| 2602   | Layout 1             | `b70f3a56726c`  |
| 2601   | Layout 1             | `b70f3a56726c`  |
| 2592   | Layout 1             | `b70f3a56726c`  |
| 2583   | Layout 1             | `b70f3a56726c`  |
| 2575   | Layout 1             | `b70f3a56726c`  |
| 2567   | Layout 1             | `b70f3a56726c`  |
| 2560   | Layout 1             | `b70f3a56726c`  |
| 2553   | Layout 1             | `b70f3a56726c`  |
| 2545   | Layout 1             | `b70f3a56726c`  |
| 2538   | Layout 1             | `b70f3a56726c`  |
| 2529   | Layout 1             | `b70f3a56726c`  |
| 2519   | Layout 1             | `b70f3a56726c`  |
| 2513   | Layout 1             | `b70f3a56726c`  |
| 2510   | Layout 1             | `b70f3a56726c`  |
| 2507   | Layout 1             | `b70f3a56726c`  |
| 2503   | Layout 1             | `b70f3a56726c`  |
| 2498   | Layout 1             | `b70f3a56726c`  |
| 2492   | Layout 1             | `b70f3a56726c`  |
| 2487   | Layout 1             | `b70f3a56726c`  |
| 2480   | Layout 1             | `b70f3a56726c`  |
| 2474   | Layout 1             | `b70f3a56726c`  |
| 2468   | Layout 1             | `b70f3a56726c`  |
| 2460   | Layout 1             | `b70f3a56726c`  |
| 2453   | Layout 1             | `b70f3a56726c`  |
| 2444   | Layout 1             | `b70f3a56726c`  |
| 2438   | Layout 1             | `b70f3a56726c`  |
| 2434   | Layout 1             | `b70f3a56726c`  |
| 2429   | Layout 1             | `b70f3a56726c`  |
| 2421   | Layout 1             | `b70f3a56726c`  |
| 2414   | Layout 1             | `b70f3a56726c`  |
| 2407   | Layout 1             | `b70f3a56726c`  |
| 2401   | Layout 1             | `b70f3a56726c`  |
| 2397   | Layout 1             | `b70f3a56726c`  |
| 2393   | Layout 1             | `b70f3a56726c`  |
| 2384   | Layout 1             | `b70f3a56726c`  |
| 2378   | Layout 1             | `b70f3a56726c`  |
| 2372   | Layout 1             | `b70f3a56726c`  |
| 2358   | Layout 1             | `b70f3a56726c`  |
| 2352   | Layout 1             | `b70f3a56726c`  |
| 2347   | Layout 1             | `b70f3a56726c`  |
| 2343   | Layout 1             | `b70f3a56726c`  |
| 2335   | Layout 1             | `b70f3a56726c`  |
| 2327   | Layout 1             | `b70f3a56726c`  |
| 2324   | Layout 1             | `b70f3a56726c`  |
| 2319   | Layout 1             | `b70f3a56726c`  |
| 2313   | Layout 1             | `b70f3a56726c`  |
| 2308   | Layout 1             | `b70f3a56726c`  |
| 2302   | Layout 1             | `b70f3a56726c`  |
| 2295   | Layout 1             | `b70f3a56726c`  |
| 2290   | Layout 1             | `b70f3a56726c`  |
| 2284   | Layout 1             | `b70f3a56726c`  |
| 2276   | Layout 1             | `b70f3a56726c`  |
| 2269   | Layout 1             | `b70f3a56726c`  |
| 2259   | Layout 1             | `b70f3a56726c`  |
| 2250   | Layout 1             | `b70f3a56726c`  |
| 2243   | Layout 1             | `b70f3a56726c`  |
| 2235   | Layout 1             | `b70f3a56726c`  |
| 2229   | Layout 1             | `b70f3a56726c`  |
| 2224   | Layout 1             | `b70f3a56726c`  |
| 2218   | Layout 1             | `b70f3a56726c`  |
| 2215   | Layout 1             | `b70f3a56726c`  |
| 2207   | Layout 1             | `b70f3a56726c`  |
| 2203   | Layout 1             | `b70f3a56726c`  |
| 2196   | Layout 1             | `b70f3a56726c`  |
| 2192   | Layout 1             | `b70f3a56726c`  |
| 2189   | Layout 1             | `b70f3a56726c`  |
| 2183   | Layout 1             | `b70f3a56726c`  |
| 2179   | Layout 1             | `b70f3a56726c`  |
| 2171   | Layout 1             | `b70f3a56726c`  |
| 2163   | Layout 1             | `b70f3a56726c`  |
| 2156   | Layout 1             | `b70f3a56726c`  |
| 2151   | Layout 1             | `b70f3a56726c`  |
| 2147   | Layout 1             | `b70f3a56726c`  |
| 2142   | Layout 1             | `b70f3a56726c`  |
| 2138   | Layout 1             | `b70f3a56726c`  |
| 2134   | Layout 1             | `b70f3a56726c`  |
| 2130   | Layout 1             | `b70f3a56726c`  |
| 2122   | Layout 1             | `b70f3a56726c`  |
| 2107   | Layout 1             | `b70f3a56726c`  |
| 2098   | Layout 1             | `b70f3a56726c`  |
| 2089   | Layout 1             | `b70f3a56726c`  |
| 2081   | Layout 1             | `b70f3a56726c`  |
| 2073   | Layout 1             | `b70f3a56726c`  |
| 2067   | Layout 1             | `b70f3a56726c`  |
| 2063   | Layout 1             | `b70f3a56726c`  |
| 2059   | Layout 1             | `b70f3a56726c`  |
| 2052   | Layout 1             | `b70f3a56726c`  |
| 2044   | Layout 1             | `b70f3a56726c`  |
| 2039   | Layout 1             | `b70f3a56726c`  |
| 2032   | Layout 1             | `b70f3a56726c`  |
| 2025   | Layout 1             | `b70f3a56726c`  |
| 2011   | Layout 1             | `b70f3a56726c`  |
| 2005   | Layout 1             | `b70f3a56726c`  |
| 2000   | Layout 1             | `b70f3a56726c`  |
| 1996   | Layout 1             | `b70f3a56726c`  |
| 1991   | Layout 1             | `b70f3a56726c`  |
| 1985   | Layout 1             | `b70f3a56726c`  |
| 1980   | Layout 1             | `b70f3a56726c`  |
| 1969   | Layout 1             | `b70f3a56726c`  |
| 1964   | Layout 1             | `b70f3a56726c`  |
| 1958   | Layout 1             | `b70f3a56726c`  |
| 1950   | Layout 1             | `b70f3a56726c`  |
| 1945   | Layout 1             | `b70f3a56726c`  |
| 1937   | Layout 1             | `b70f3a56726c`  |
| 1933   | Layout 1             | `b70f3a56726c`  |
| 1927   | Layout 1             | `b70f3a56726c`  |
| 1921   | Layout 1             | `b70f3a56726c`  |
| 1914   | Layout 1             | `b70f3a56726c`  |
| 1908   | Layout 1             | `b70f3a56726c`  |
| 1897   | Layout 1             | `b70f3a56726c`  |
| 1892   | Layout 1             | `b70f3a56726c`  |
| 1886   | Layout 1             | `b70f3a56726c`  |
| 1881   | Layout 1             | `b70f3a56726c`  |
| 1871   | Layout 1             | `b70f3a56726c`  |
| 1866   | Layout 1             | `b70f3a56726c`  |
| 1862   | Layout 1             | `b70f3a56726c`  |
| 1854   | Layout 1             | `b70f3a56726c`  |
| 1846   | Layout 1             | `b70f3a56726c`  |
| 1838   | Layout 1             | `b70f3a56726c`  |
| 1832   | Layout 1             | `b70f3a56726c`  |
| 1826   | Layout 1             | `b70f3a56726c`  |
| 1822   | Layout 1             | `b70f3a56726c`  |
| 1818   | Layout 1             | `b70f3a56726c`  |
| 1804   | Layout 1             | `b70f3a56726c`  |
| 1794   | Layout 1             | `b70f3a56726c`  |
| 1790   | Layout 1             | `b70f3a56726c`  |
| 1784   | Layout 1             | `b70f3a56726c`  |
| 1774   | Layout 1             | `b70f3a56726c`  |
| 1771   | Layout 1             | `b70f3a56726c`  |
| 1762   | Layout 1             | `b70f3a56726c`  |
| 1759   | Layout 1             | `b70f3a56726c`  |
| 1754   | Layout 1             | `b70f3a56726c`  |
| 1749   | Layout 1             | `b70f3a56726c`  |
| 1743   | Layout 1             | `b70f3a56726c`  |
| 1737   | Layout 1             | `b70f3a56726c`  |
| 1731   | Layout 1             | `b70f3a56726c`  |
| 1725   | Layout 1             | `b70f3a56726c`  |
| 1717   | Layout 1             | `b70f3a56726c`  |
| 1710   | Layout 1             | `b70f3a56726c`  |
| 1704   | Layout 1             | `b70f3a56726c`  |
| 1698   | Layout 1             | `b70f3a56726c`  |
| 1690   | Layout 1             | `b70f3a56726c`  |
| 1685   | Layout 1             | `b70f3a56726c`  |
| 1680   | Layout 1             | `b70f3a56726c`  |
| 1674   | Layout 1             | `b70f3a56726c`  |
| 1668   | Layout 1             | `b70f3a56726c`  |
| 1659   | Layout 1             | `b70f3a56726c`  |
| 1649   | Layout 1             | `b70f3a56726c`  |
| 1642   | Layout 1             | `b70f3a56726c`  |
| 1636   | Layout 1             | `b70f3a56726c`  |
| 1628   | Layout 1             | `b70f3a56726c`  |
| 1622   | Layout 1             | `b70f3a56726c`  |
| 1614   | Layout 1             | `b70f3a56726c`  |
| 1608   | Layout 1             | `b70f3a56726c`  |
| 1602   | Layout 1             | `b70f3a56726c`  |
| 1598   | Layout 1             | `b70f3a56726c`  |
| 1594   | Layout 1             | `b70f3a56726c`  |
| 1590   | Layout 1             | `b70f3a56726c`  |
| 1587   | Layout 1             | `b70f3a56726c`  |
| 1584   | Layout 1             | `b70f3a56726c`  |
| 1579   | Layout 1             | `b70f3a56726c`  |
| 1572   | Layout 1             | `b70f3a56726c`  |
| 1565   | Layout 1             | `b70f3a56726c`  |
| 1559   | Layout 1             | `b70f3a56726c`  |
| 1554   | Layout 1             | `b70f3a56726c`  |
| 1547   | Layout 1             | `b70f3a56726c`  |
| 1537   | Layout 1             | `b70f3a56726c`  |
| 1529   | Layout 1             | `b70f3a56726c`  |
| 1524   | Layout 1             | `b70f3a56726c`  |
| 1519   | Layout 1             | `b70f3a56726c`  |
| 1509   | Layout 1             | `b70f3a56726c`  |
| 1506   | Layout 1             | `b70f3a56726c`  |
| 1504   | Layout 1             | `b70f3a56726c`  |
| 1500   | Layout 1             | `b70f3a56726c`  |
| 1493   | Layout 1             | `b70f3a56726c`  |
| 1489   | Layout 1             | `b70f3a56726c`  |
| 1485   | Layout 1             | `b70f3a56726c`  |
| 1481   | Layout 1             | `b70f3a56726c`  |
| 1474   | Layout 1             | `b70f3a56726c`  |
| 1466   | Layout 1             | `b70f3a56726c`  |
| 1462   | Layout 1             | `b70f3a56726c`  |
| 1459   | Layout 1             | `b70f3a56726c`  |
| 1453   | Layout 1             | `b70f3a56726c`  |
| 1450   | Layout 1             | `b70f3a56726c`  |
| 1445   | Layout 1             | `b70f3a56726c`  |
| 1439   | Layout 1             | `b70f3a56726c`  |
| 1433   | Layout 1             | `b70f3a56726c`  |
| 1430   | Layout 1             | `b70f3a56726c`  |
| 1426   | Layout 1             | `b70f3a56726c`  |
| 1421   | Layout 1             | `b70f3a56726c`  |
| 1417   | Layout 1             | `b70f3a56726c`  |
| 1416   | Layout 1             | `b70f3a56726c`  |
| 1409   | Layout 1             | `b70f3a56726c`  |
| 1405   | Layout 1             | `b70f3a56726c`  |
| 1401   | Layout 1             | `b70f3a56726c`  |
| 1396   | Layout 1             | `b70f3a56726c`  |
| 1391   | Layout 1             | `b70f3a56726c`  |
| 1390   | Layout 1             | `b70f3a56726c`  |
| 1386   | Layout 1             | `b70f3a56726c`  |
| 1381   | Layout 1             | `b70f3a56726c`  |
| 1379   | Layout 1             | `b70f3a56726c`  |
| 1372   | Layout 1             | `b70f3a56726c`  |
| 1366   | Layout 1             | `b70f3a56726c`  |
| 1364   | Layout 1             | `b70f3a56726c`  |
| 1363   | Layout 1             | `b70f3a56726c`  |
| 1360   | Layout 1             | `b70f3a56726c`  |
| 1358   | Layout 1             | `b70f3a56726c`  |
| 1355   | Layout 1             | `b70f3a56726c`  |
| 1351   | Layout 1             | `b70f3a56726c`  |
| 1348   | Layout 1             | `b70f3a56726c`  |
| 1346   | Layout 1             | `b70f3a56726c`  |
| 1341   | Layout 1             | `b70f3a56726c`  |
| 1340   | Layout 1             | `b70f3a56726c`  |
| 1338   | Layout 1             | `b70f3a56726c`  |
| 1335   | Layout 1             | `b70f3a56726c`  |
| 1333   | Layout 1             | `b70f3a56726c`  |
| 1329   | Layout 1             | `b70f3a56726c`  |
| 1327   | Layout 1             | `b70f3a56726c`  |
| 1324   | Layout 1             | `b70f3a56726c`  |
| 1321   | Layout 1             | `b70f3a56726c`  |
| 1319   | Layout 1             | `b70f3a56726c`  |
| 1318   | Layout 1             | `b70f3a56726c`  |
| 1316   | Layout 1             | `b70f3a56726c`  |
| 1313   | Layout 1             | `b70f3a56726c`  |
| 1311   | Layout 1             | `b70f3a56726c`  |
| 1309   | Layout 1             | `b70f3a56726c`  |
| 1304   | Layout 1             | `b70f3a56726c`  |
| 1292   | No documented layout | `b70f3a56726c`  |
| 1286   | No documented layout | `b70f3a56726c`  |
| 1280   | No documented layout | `b70f3a56726c`  |
| 1276   | No documented layout | `b70f3a56726c`  |
| 1267   | No documented layout | `b70f3a56726c`  |
| 1261   | No documented layout | `b70f3a56726c`  |
| 1256   | No documented layout | `b70f3a56726c`  |
| 1250   | No documented layout | `b70f3a56726c`  |
| 1246   | No file              | `b70f3a56726c`  |
| 1239   | No file              | `b70f3a56726c`  |
| 1230   | No file              | `b70f3a56726c`  |
| 1226   | No file              | `b70f3a56726c`  |
| 1220   | No file              | `b70f3a56726c`  |
| 1217   | No file              | `b70f3a56726c`  |
| 1211   | No file              | `b70f3a56726c`  |
| 1210   | No file              | `b70f3a56726c`  |
| 1208   | No file              | `b70f3a56726c`  |
| 1203   | No file              | `b70f3a56726c`  |
| 1197   | No file              | `b70f3a56726c`  |
| 1194   | No file              | `b70f3a56726c`  |
| 1192   | No file              | `b70f3a56726c`  |
| 1187   | No file              | `b70f3a56726c`  |
| 1183   | No file              | `b70f3a56726c`  |
| 1177   | No file              | `b70f3a56726c`  |
| 1173   | No file              | `b70f3a56726c`  |
| 1167   | No file              | `b70f3a56726c`  |
| 1164   | No file              | `b70f3a56726c`  |
| 1156   | No file              | `b70f3a56726c`  |
| 1149   | No file              | `b70f3a56726c`  |
| 1144   | No documented layout | `b70f3a56726c`  |
| 1137   | No documented layout | `b70f3a56726c`  |
| 1132   | No documented layout | `b70f3a56726c`  |
| 1127   | No documented layout | `b70f3a56726c`  |
| 1122   | No documented layout | `b70f3a56726c`  |
| 1118   | No documented layout | `b70f3a56726c`  |
| 1114   | No documented layout | `b70f3a56726c`  |
| 1109   | No documented layout | `b70f3a56726c`  |
| 1102   | No file              | `b70f3a56726c`  |
| 1096   | No file              | `b70f3a56726c`  |
| 1088   | No file              | `b70f3a56726c`  |
| 1081   | No file              | `b70f3a56726c`  |
| 1076   | No file              | `b70f3a56726c`  |
| 1069   | No file              | `b70f3a56726c`  |
| 1064   | No file              | `b70f3a56726c`  |
| 1058   | No file              | `b70f3a56726c`  |
| 1051   | No file              | `b70f3a56726c`  |
| 1044   | No file              | `b70f3a56726c`  |
| 1036   | No file              | `b70f3a56726c`  |
| 1026   | No file              | `b70f3a56726c`  |
| 1016   | No file              | `b70f3a56726c`  |
| 1009   | No file              | `b70f3a56726c`  |
| 1005   | No file              | `b70f3a56726c`  |
| 1000   | No file              | `b70f3a56726c`  |
| 998    | No file              | `b70f3a56726c`  |
| 990    | No file              | `b70f3a56726c`  |
| 979    | No file              | `b70f3a56726c`  |
| 972    | No file              | `b70f3a56726c`  |
| 963    | No file              | `b70f3a56726c`  |
| 955    | No file              | `b70f3a56726c`  |
| 946    | No file              | `b70f3a56726c`  |
| 938    | No file              | `b70f3a56726c`  |
| 927    | No file              | `b70f3a56726c`  |
| 911    | No file              | `b70f3a56726c`  |
| 904    | No file              | `b70f3a56726c`  |
| 899    | No file              | `b70f3a56726c`  |
| 894    | No file              | `b70f3a56726c`  |
| 885    | No file              | `b70f3a56726c`  |
| 879    | No file              | `b70f3a56726c`  |
| 872    | No file              | `b70f3a56726c`  |
| 864    | No file              | `b70f3a56726c`  |
| 855    | No file              | `b70f3a56726c`  |
| 853    | No file              | `b70f3a56726c`  |
| 845    | No file              | `b70f3a56726c`  |
| 837    | No file              | `b70f3a56726c`  |
| 829    | No documented layout | `b70f3a56726c`  |
| 822    | No documented layout | `b70f3a56726c`  |
| 814    | No documented layout | `b70f3a56726c`  |
| 805    | No documented layout | `b70f3a56726c`  |
| 794    | No documented layout | `b70f3a56726c`  |
| 787    | No documented layout | `b70f3a56726c`  |
| 780    | No documented layout | `b70f3a56726c`  |
| 771    | No documented layout | `b70f3a56726c`  |
| 760    | No documented layout | `b70f3a56726c`  |
| 748    | No documented layout | `b70f3a56726c`  |
| 741    | No documented layout | `b70f3a56726c`  |
| 736    | No documented layout | `b70f3a56726c`  |
| 731    | No documented layout | `b70f3a56726c`  |
| 723    | No documented layout | `b70f3a56726c`  |
| 711    | No documented layout | `b70f3a56726c`  |
| 707    | No documented layout | `b70f3a56726c`  |
| 697    | No documented layout | `b70f3a56726c`  |
| 689    | No documented layout | `b70f3a56726c`  |
| 683    | No documented layout | `b70f3a56726c`  |
| 678    | No documented layout | `b70f3a56726c`  |
| 670    | No documented layout | `b70f3a56726c`  |
| 661    | No documented layout | `b70f3a56726c`  |
| 656    | No documented layout | `b70f3a56726c`  |
| 652    | No documented layout | `b70f3a56726c`  |
| 643    | No documented layout | `b70f3a56726c`  |
| 637    | No documented layout | `b70f3a56726c`  |
| 630    | No documented layout | `b70f3a56726c`  |
| 627    | No documented layout | `b70f3a56726c`  |
| 621    | No documented layout | `b70f3a56726c`  |
| 617    | No documented layout | `b70f3a56726c`  |
| 615    | No documented layout | `b70f3a56726c`  |
| 606    | No documented layout | `b70f3a56726c`  |
| 599    | No documented layout | `b70f3a56726c`  |
| 592    | No documented layout | `b70f3a56726c`  |
| 586    | No documented layout | `b70f3a56726c`  |
| 577    | No documented layout | `b70f3a56726c`  |
| 569    | No documented layout | `b70f3a56726c`  |
| 561    | No documented layout | `b70f3a56726c`  |
| 554    | No documented layout | `b70f3a56726c`  |
| 542    | No documented layout | `b70f3a56726c`  |
| 532    | No documented layout | `b70f3a56726c`  |
| 531    | No documented layout | `b70f3a56726c`  |
| 526    | No documented layout | `b70f3a56726c`  |
| 521    | No documented layout | `b70f3a56726c`  |
| 517    | No documented layout | `b70f3a56726c`  |
| 510    | No documented layout | `b70f3a56726c`  |
| 508    | No documented layout | `b70f3a56726c`  |
| 504    | No documented layout | `b70f3a56726c`  |
| 497    | No documented layout | `b70f3a56726c`  |
| 491    | No documented layout | `b70f3a56726c`  |
| 485    | No documented layout | `b70f3a56726c`  |
| 478    | No documented layout | `b70f3a56726c`  |
| 472    | No documented layout | `b70f3a56726c`  |
| 466    | No documented layout | `b70f3a56726c`  |
| 457    | No documented layout | `b70f3a56726c`  |
| 452    | No documented layout | `b70f3a56726c`  |
| 449    | No documented layout | `b70f3a56726c`  |
| 435    | No documented layout | `b70f3a56726c`  |

<!-- versions:end -->

## Observed Values

Same layout as [`newquest.bss`](newquest_bss.md), the layout reference: an 8-byte `PABR` header with a group count; per group an 11-byte header, 17-byte quest reference rows and a 12-byte trailer; a string table; an 8-byte file trailer. One handler reads all four quest lists. Values seen on client 3458:

| Field                                  | Observed                                              |
| -------------------------------------- | ----------------------------------------------------- |
| `group_count`                          | `120`                                                 |
| First group                            | key `104`, `14` rows                                  |
| Group header `group_type`              | `0`, except `1` on key 101 `[Invitation from I] Someone Beckons` |
| Group trailer start / end index        | Index `2`, the empty string: no event period          |
| Row `is_sub_quest`                       | `0`, except `1` on 7 rows, see Open Questions         |
| Row `hide_conditions_index`                   | Empty string on 2,667 rows, a script on 601           |
| Row `visible_conditions_index`                   | Empty string on 1,348 rows, a script on 1,920         |
| String table                           | `3,490` strings; `string_count` at `0x0000E3D4`       |

The scripts check prerequisite quests (`clearquest`, `progressquest`), class (`checkClass`), level and content groups (`isContentsGroupOpen`); see String Table in the `newquest.bss` doc for the two script roles.

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

## Localization

LOC type `43` holds the English text of this list, keyed by the group's `group_key`:

| Key                                                               | Text                                                 |
| ----------------------------------------------------------------- | ---------------------------------------------------- |
| `str_id1 = group_key`, `str_id4 = 0`                              | Group name, e.g. key 104 `[Special Growth] Taking My Own Path` |
| `str_id1 = packed_quest_id`, `str_id2 = group_key`, `str_id4 = 1` | The quest's condition line, e.g. `From <PAColor0xfff3d900>Alustin<PAOldColor> in Velia, complete ...` |

On client 3458 all 120 groups have a name (type 43 has 170, keys 1 to 171, so some belong to groups no longer in the file) and all 3,268 rows have a condition line. Condition lines carry `<PAColor>` tags (all but 6); group names do not. The string table holds the Korean source of both, which the handler shows where LOC has no row.

## Notes

- Decompressed size is `447,790` bytes on client 3458.
- No quest appears twice; every group key is unique.
- Earlier versions of this doc read the later group header as 22 bytes starting one byte later, so each row took its leading flag byte from the byte before it; the row values were the same. Up to client 3464 the flag was still read one row late, see the Notes of [`newquest.bss`](newquest_bss.md). They named the first header's `group_key` `unknown_00` and the later header's `group_key` `unknown_0c`.

## Open Questions

### What Does `is_sub_quest` Change?

`1` on only 7 rows, all in group key 51: quests 6603 / 2 to 8, which share one `hide_conditions` (client 3464). The server's `IsSubQuest` sets the same 7 rows; what the flag changes in the list is not confirmed.

### Shared Fields

What `group_type` selects is open for all four lists; see the Open Questions of [`newquest.bss`](newquest_bss.md).
