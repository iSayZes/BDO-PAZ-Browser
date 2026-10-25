# `plantupgradeparam.bss` Format

## Purpose

Upgrade parameter groups of the worker system: one entry per group with its highest upgrade level. Towns in [planttown.bss](planttown_bss.md) point at groups 1 (warehouse) and 2 (worker capacity), plant zones in [plantzone.dbss](../dbss/plantzone_dbss.md) at 101 (base efficiency) and 201 (luck efficiency). The per-level values the groups stand for are not in the client file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                    | Bytes | Records | Row bytes |
| ------ | ------------- | ----------------------- | ----- | ------- | --------- |
| 1      | 805 and later | `plantupgradeparam.bss` | 44    | 4 Entry | 6         |

| Layout | File                    | Known         | Unknown    |
| ------ | ----------------------- | ------------- | ---------- |
| 1      | `plantupgradeparam.bss` | 44 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `f867dfdef1f3`  |
| 3482   | Layout 1             | `f867dfdef1f3`  |
| 3474   | Layout 1             | `f867dfdef1f3`  |
| 3473   | Layout 1             | `f867dfdef1f3`  |
| 3464   | Layout 1             | `f867dfdef1f3`  |
| 3458   | Layout 1             | `f867dfdef1f3`  |
| 3454   | Layout 1             | `f867dfdef1f3`  |
| 3444   | Layout 1             | `f867dfdef1f3`  |
| 3435   | Layout 1             | `f867dfdef1f3`  |
| 3426   | Layout 1             | `f867dfdef1f3`  |
| 3418   | Layout 1             | `f867dfdef1f3`  |
| 3412   | Layout 1             | `f867dfdef1f3`  |
| 3402   | Layout 1             | `f867dfdef1f3`  |
| 3396   | Layout 1             | `f867dfdef1f3`  |
| 3387   | Layout 1             | `f867dfdef1f3`  |
| 3381   | Layout 1             | `f867dfdef1f3`  |
| 3373   | Layout 1             | `f867dfdef1f3`  |
| 3364   | Layout 1             | `f867dfdef1f3`  |
| 3356   | Layout 1             | `f867dfdef1f3`  |
| 3349   | Layout 1             | `f867dfdef1f3`  |
| 3342   | Layout 1             | `f867dfdef1f3`  |
| 3335   | Layout 1             | `f867dfdef1f3`  |
| 3326   | Layout 1             | `f867dfdef1f3`  |
| 3321   | Layout 1             | `f867dfdef1f3`  |
| 3314   | Layout 1             | `f867dfdef1f3`  |
| 3303   | Layout 1             | `f867dfdef1f3`  |
| 3302   | Layout 1             | `f867dfdef1f3`  |
| 3293   | Layout 1             | `f867dfdef1f3`  |
| 3283   | Layout 1             | `f867dfdef1f3`  |
| 3275   | Layout 1             | `f867dfdef1f3`  |
| 3267   | Layout 1             | `f867dfdef1f3`  |
| 3258   | Layout 1             | `f867dfdef1f3`  |
| 3251   | Layout 1             | `f867dfdef1f3`  |
| 3242   | Layout 1             | `f867dfdef1f3`  |
| 3235   | Layout 1             | `f867dfdef1f3`  |
| 3229   | Layout 1             | `f867dfdef1f3`  |
| 3212   | Layout 1             | `f867dfdef1f3`  |
| 3203   | Layout 1             | `f867dfdef1f3`  |
| 3193   | Layout 1             | `f867dfdef1f3`  |
| 3186   | Layout 1             | `f867dfdef1f3`  |
| 3177   | Layout 1             | `f867dfdef1f3`  |
| 3169   | Layout 1             | `f867dfdef1f3`  |
| 3158   | Layout 1             | `f867dfdef1f3`  |
| 3151   | Layout 1             | `f867dfdef1f3`  |
| 3144   | Layout 1             | `f867dfdef1f3`  |
| 3133   | Layout 1             | `f867dfdef1f3`  |
| 3125   | Layout 1             | `f867dfdef1f3`  |
| 3118   | Layout 1             | `f867dfdef1f3`  |
| 3111   | Layout 1             | `f867dfdef1f3`  |
| 3103   | Layout 1             | `f867dfdef1f3`  |
| 3095   | Layout 1             | `f867dfdef1f3`  |
| 3086   | Layout 1             | `f867dfdef1f3`  |
| 3072   | Layout 1             | `f867dfdef1f3`  |
| 3062   | Layout 1             | `f867dfdef1f3`  |
| 3052   | Layout 1             | `f867dfdef1f3`  |
| 3045   | Layout 1             | `f867dfdef1f3`  |
| 3037   | Layout 1             | `f867dfdef1f3`  |
| 3030   | Layout 1             | `f867dfdef1f3`  |
| 3021   | Layout 1             | `f867dfdef1f3`  |
| 3012   | Layout 1             | `f867dfdef1f3`  |
| 3002   | Layout 1             | `f867dfdef1f3`  |
| 2995   | Layout 1             | `f867dfdef1f3`  |
| 2987   | Layout 1             | `f867dfdef1f3`  |
| 2978   | Layout 1             | `f867dfdef1f3`  |
| 2970   | Layout 1             | `f867dfdef1f3`  |
| 2959   | Layout 1             | `f867dfdef1f3`  |
| 2951   | Layout 1             | `f867dfdef1f3`  |
| 2942   | Layout 1             | `f867dfdef1f3`  |
| 2935   | Layout 1             | `f867dfdef1f3`  |
| 2932   | Layout 1             | `f867dfdef1f3`  |
| 2923   | Layout 1             | `f867dfdef1f3`  |
| 2919   | Layout 1             | `f867dfdef1f3`  |
| 2907   | Layout 1             | `f867dfdef1f3`  |
| 2900   | Layout 1             | `f867dfdef1f3`  |
| 2891   | Layout 1             | `f867dfdef1f3`  |
| 2882   | Layout 1             | `f867dfdef1f3`  |
| 2872   | Layout 1             | `f867dfdef1f3`  |
| 2863   | Layout 1             | `f867dfdef1f3`  |
| 2855   | Layout 1             | `f867dfdef1f3`  |
| 2849   | Layout 1             | `f867dfdef1f3`  |
| 2844   | Layout 1             | `f867dfdef1f3`  |
| 2834   | Layout 1             | `f867dfdef1f3`  |
| 2825   | Layout 1             | `f867dfdef1f3`  |
| 2819   | Layout 1             | `f867dfdef1f3`  |
| 2811   | Layout 1             | `f867dfdef1f3`  |
| 2803   | Layout 1             | `f867dfdef1f3`  |
| 2794   | Layout 1             | `f867dfdef1f3`  |
| 2783   | Layout 1             | `f867dfdef1f3`  |
| 2774   | Layout 1             | `f867dfdef1f3`  |
| 2765   | Layout 1             | `f867dfdef1f3`  |
| 2756   | Layout 1             | `f867dfdef1f3`  |
| 2750   | Layout 1             | `f867dfdef1f3`  |
| 2743   | Layout 1             | `f867dfdef1f3`  |
| 2736   | Layout 1             | `f867dfdef1f3`  |
| 2726   | Layout 1             | `f867dfdef1f3`  |
| 2717   | Layout 1             | `f867dfdef1f3`  |
| 2709   | Layout 1             | `f867dfdef1f3`  |
| 2703   | Layout 1             | `f867dfdef1f3`  |
| 2695   | Layout 1             | `f867dfdef1f3`  |
| 2684   | Layout 1             | `f867dfdef1f3`  |
| 2672   | Layout 1             | `f867dfdef1f3`  |
| 2665   | Layout 1             | `f867dfdef1f3`  |
| 2657   | Layout 1             | `f867dfdef1f3`  |
| 2649   | Layout 1             | `f867dfdef1f3`  |
| 2644   | Layout 1             | `f867dfdef1f3`  |
| 2637   | Layout 1             | `f867dfdef1f3`  |
| 2629   | Layout 1             | `f867dfdef1f3`  |
| 2619   | Layout 1             | `f867dfdef1f3`  |
| 2612   | Layout 1             | `f867dfdef1f3`  |
| 2606   | Layout 1             | `f867dfdef1f3`  |
| 2602   | Layout 1             | `f867dfdef1f3`  |
| 2601   | Layout 1             | `f867dfdef1f3`  |
| 2592   | Layout 1             | `f867dfdef1f3`  |
| 2583   | Layout 1             | `f867dfdef1f3`  |
| 2575   | Layout 1             | `f867dfdef1f3`  |
| 2567   | Layout 1             | `f867dfdef1f3`  |
| 2560   | Layout 1             | `f867dfdef1f3`  |
| 2553   | Layout 1             | `f867dfdef1f3`  |
| 2545   | Layout 1             | `f867dfdef1f3`  |
| 2538   | Layout 1             | `f867dfdef1f3`  |
| 2529   | Layout 1             | `f867dfdef1f3`  |
| 2519   | Layout 1             | `f867dfdef1f3`  |
| 2513   | Layout 1             | `f867dfdef1f3`  |
| 2510   | Layout 1             | `f867dfdef1f3`  |
| 2507   | Layout 1             | `f867dfdef1f3`  |
| 2503   | Layout 1             | `f867dfdef1f3`  |
| 2498   | Layout 1             | `f867dfdef1f3`  |
| 2492   | Layout 1             | `f867dfdef1f3`  |
| 2487   | Layout 1             | `f867dfdef1f3`  |
| 2480   | Layout 1             | `f867dfdef1f3`  |
| 2474   | Layout 1             | `f867dfdef1f3`  |
| 2468   | Layout 1             | `f867dfdef1f3`  |
| 2460   | Layout 1             | `f867dfdef1f3`  |
| 2453   | Layout 1             | `f867dfdef1f3`  |
| 2444   | Layout 1             | `f867dfdef1f3`  |
| 2438   | Layout 1             | `f867dfdef1f3`  |
| 2434   | Layout 1             | `f867dfdef1f3`  |
| 2429   | Layout 1             | `f867dfdef1f3`  |
| 2421   | Layout 1             | `f867dfdef1f3`  |
| 2414   | Layout 1             | `f867dfdef1f3`  |
| 2407   | Layout 1             | `f867dfdef1f3`  |
| 2401   | Layout 1             | `f867dfdef1f3`  |
| 2397   | Layout 1             | `f867dfdef1f3`  |
| 2393   | Layout 1             | `f867dfdef1f3`  |
| 2384   | Layout 1             | `f867dfdef1f3`  |
| 2378   | Layout 1             | `f867dfdef1f3`  |
| 2372   | Layout 1             | `f867dfdef1f3`  |
| 2358   | Layout 1             | `f867dfdef1f3`  |
| 2352   | Layout 1             | `f867dfdef1f3`  |
| 2347   | Layout 1             | `f867dfdef1f3`  |
| 2343   | Layout 1             | `f867dfdef1f3`  |
| 2335   | Layout 1             | `f867dfdef1f3`  |
| 2327   | Layout 1             | `f867dfdef1f3`  |
| 2324   | Layout 1             | `f867dfdef1f3`  |
| 2319   | Layout 1             | `f867dfdef1f3`  |
| 2313   | Layout 1             | `f867dfdef1f3`  |
| 2308   | Layout 1             | `f867dfdef1f3`  |
| 2302   | Layout 1             | `f867dfdef1f3`  |
| 2295   | Layout 1             | `f867dfdef1f3`  |
| 2290   | Layout 1             | `f867dfdef1f3`  |
| 2284   | Layout 1             | `f867dfdef1f3`  |
| 2276   | Layout 1             | `f867dfdef1f3`  |
| 2269   | Layout 1             | `f867dfdef1f3`  |
| 2259   | Layout 1             | `f867dfdef1f3`  |
| 2250   | Layout 1             | `f867dfdef1f3`  |
| 2243   | Layout 1             | `f867dfdef1f3`  |
| 2235   | Layout 1             | `f867dfdef1f3`  |
| 2229   | Layout 1             | `f867dfdef1f3`  |
| 2224   | Layout 1             | `f867dfdef1f3`  |
| 2218   | Layout 1             | `f867dfdef1f3`  |
| 2215   | Layout 1             | `f867dfdef1f3`  |
| 2207   | Layout 1             | `f867dfdef1f3`  |
| 2203   | Layout 1             | `f867dfdef1f3`  |
| 2196   | Layout 1             | `f867dfdef1f3`  |
| 2192   | Layout 1             | `f867dfdef1f3`  |
| 2189   | Layout 1             | `f867dfdef1f3`  |
| 2183   | Layout 1             | `f867dfdef1f3`  |
| 2179   | Layout 1             | `f867dfdef1f3`  |
| 2171   | Layout 1             | `f867dfdef1f3`  |
| 2163   | Layout 1             | `f867dfdef1f3`  |
| 2156   | Layout 1             | `f867dfdef1f3`  |
| 2151   | Layout 1             | `f867dfdef1f3`  |
| 2147   | Layout 1             | `f867dfdef1f3`  |
| 2142   | Layout 1             | `f867dfdef1f3`  |
| 2138   | Layout 1             | `f867dfdef1f3`  |
| 2134   | Layout 1             | `f867dfdef1f3`  |
| 2130   | Layout 1             | `f867dfdef1f3`  |
| 2122   | Layout 1             | `f867dfdef1f3`  |
| 2107   | Layout 1             | `f867dfdef1f3`  |
| 2098   | Layout 1             | `f867dfdef1f3`  |
| 2089   | Layout 1             | `f867dfdef1f3`  |
| 2081   | Layout 1             | `f867dfdef1f3`  |
| 2073   | Layout 1             | `f867dfdef1f3`  |
| 2067   | Layout 1             | `f867dfdef1f3`  |
| 2063   | Layout 1             | `f867dfdef1f3`  |
| 2059   | Layout 1             | `f867dfdef1f3`  |
| 2052   | Layout 1             | `f867dfdef1f3`  |
| 2044   | Layout 1             | `f867dfdef1f3`  |
| 2039   | Layout 1             | `f867dfdef1f3`  |
| 2032   | Layout 1             | `f867dfdef1f3`  |
| 2025   | Layout 1             | `f867dfdef1f3`  |
| 2011   | Layout 1             | `f867dfdef1f3`  |
| 2005   | Layout 1             | `f867dfdef1f3`  |
| 2000   | Layout 1             | `f867dfdef1f3`  |
| 1996   | Layout 1             | `f867dfdef1f3`  |
| 1991   | Layout 1             | `f867dfdef1f3`  |
| 1985   | Layout 1             | `f867dfdef1f3`  |
| 1980   | Layout 1             | `f867dfdef1f3`  |
| 1969   | Layout 1             | `f867dfdef1f3`  |
| 1964   | Layout 1             | `f867dfdef1f3`  |
| 1958   | Layout 1             | `f867dfdef1f3`  |
| 1950   | Layout 1             | `f867dfdef1f3`  |
| 1945   | Layout 1             | `f867dfdef1f3`  |
| 1937   | Layout 1             | `f867dfdef1f3`  |
| 1933   | Layout 1             | `f867dfdef1f3`  |
| 1927   | Layout 1             | `f867dfdef1f3`  |
| 1921   | Layout 1             | `f867dfdef1f3`  |
| 1914   | Layout 1             | `f867dfdef1f3`  |
| 1908   | Layout 1             | `f867dfdef1f3`  |
| 1897   | Layout 1             | `f867dfdef1f3`  |
| 1892   | Layout 1             | `f867dfdef1f3`  |
| 1886   | Layout 1             | `f867dfdef1f3`  |
| 1881   | Layout 1             | `f867dfdef1f3`  |
| 1871   | Layout 1             | `f867dfdef1f3`  |
| 1866   | Layout 1             | `f867dfdef1f3`  |
| 1862   | Layout 1             | `f867dfdef1f3`  |
| 1854   | Layout 1             | `f867dfdef1f3`  |
| 1846   | Layout 1             | `f867dfdef1f3`  |
| 1838   | Layout 1             | `f867dfdef1f3`  |
| 1832   | Layout 1             | `f867dfdef1f3`  |
| 1826   | Layout 1             | `f867dfdef1f3`  |
| 1822   | Layout 1             | `f867dfdef1f3`  |
| 1818   | Layout 1             | `f867dfdef1f3`  |
| 1804   | Layout 1             | `f867dfdef1f3`  |
| 1794   | Layout 1             | `f867dfdef1f3`  |
| 1790   | Layout 1             | `f867dfdef1f3`  |
| 1784   | Layout 1             | `f867dfdef1f3`  |
| 1774   | Layout 1             | `f867dfdef1f3`  |
| 1771   | Layout 1             | `f867dfdef1f3`  |
| 1762   | Layout 1             | `f867dfdef1f3`  |
| 1759   | Layout 1             | `f867dfdef1f3`  |
| 1754   | Layout 1             | `f867dfdef1f3`  |
| 1749   | Layout 1             | `f867dfdef1f3`  |
| 1743   | Layout 1             | `f867dfdef1f3`  |
| 1737   | Layout 1             | `f867dfdef1f3`  |
| 1731   | Layout 1             | `f867dfdef1f3`  |
| 1725   | Layout 1             | `f867dfdef1f3`  |
| 1717   | Layout 1             | `f867dfdef1f3`  |
| 1710   | Layout 1             | `f867dfdef1f3`  |
| 1704   | Layout 1             | `f867dfdef1f3`  |
| 1698   | Layout 1             | `f867dfdef1f3`  |
| 1690   | Layout 1             | `f867dfdef1f3`  |
| 1685   | Layout 1             | `f867dfdef1f3`  |
| 1680   | Layout 1             | `f867dfdef1f3`  |
| 1674   | Layout 1             | `f867dfdef1f3`  |
| 1668   | Layout 1             | `f867dfdef1f3`  |
| 1659   | Layout 1             | `f867dfdef1f3`  |
| 1649   | Layout 1             | `f867dfdef1f3`  |
| 1642   | Layout 1             | `f867dfdef1f3`  |
| 1636   | Layout 1             | `f867dfdef1f3`  |
| 1628   | Layout 1             | `f867dfdef1f3`  |
| 1622   | Layout 1             | `f867dfdef1f3`  |
| 1614   | Layout 1             | `f867dfdef1f3`  |
| 1608   | Layout 1             | `f867dfdef1f3`  |
| 1602   | Layout 1             | `f867dfdef1f3`  |
| 1598   | Layout 1             | `f867dfdef1f3`  |
| 1594   | Layout 1             | `f867dfdef1f3`  |
| 1590   | Layout 1             | `f867dfdef1f3`  |
| 1587   | Layout 1             | `f867dfdef1f3`  |
| 1584   | Layout 1             | `f867dfdef1f3`  |
| 1579   | Layout 1             | `f867dfdef1f3`  |
| 1572   | Layout 1             | `f867dfdef1f3`  |
| 1565   | Layout 1             | `f867dfdef1f3`  |
| 1559   | Layout 1             | `f867dfdef1f3`  |
| 1554   | Layout 1             | `f867dfdef1f3`  |
| 1547   | Layout 1             | `f867dfdef1f3`  |
| 1537   | Layout 1             | `f867dfdef1f3`  |
| 1529   | Layout 1             | `f867dfdef1f3`  |
| 1524   | Layout 1             | `f867dfdef1f3`  |
| 1519   | Layout 1             | `f867dfdef1f3`  |
| 1509   | Layout 1             | `f867dfdef1f3`  |
| 1506   | Layout 1             | `f867dfdef1f3`  |
| 1504   | Layout 1             | `f867dfdef1f3`  |
| 1500   | Layout 1             | `f867dfdef1f3`  |
| 1493   | Layout 1             | `f867dfdef1f3`  |
| 1489   | Layout 1             | `f867dfdef1f3`  |
| 1485   | Layout 1             | `f867dfdef1f3`  |
| 1481   | Layout 1             | `f867dfdef1f3`  |
| 1474   | Layout 1             | `f867dfdef1f3`  |
| 1466   | Layout 1             | `f867dfdef1f3`  |
| 1462   | Layout 1             | `f867dfdef1f3`  |
| 1459   | Layout 1             | `f867dfdef1f3`  |
| 1453   | Layout 1             | `f867dfdef1f3`  |
| 1450   | Layout 1             | `f867dfdef1f3`  |
| 1445   | Layout 1             | `f867dfdef1f3`  |
| 1439   | Layout 1             | `f867dfdef1f3`  |
| 1433   | Layout 1             | `f867dfdef1f3`  |
| 1430   | Layout 1             | `f867dfdef1f3`  |
| 1426   | Layout 1             | `f867dfdef1f3`  |
| 1421   | Layout 1             | `f867dfdef1f3`  |
| 1417   | Layout 1             | `f867dfdef1f3`  |
| 1416   | Layout 1             | `f867dfdef1f3`  |
| 1409   | Layout 1             | `f867dfdef1f3`  |
| 1405   | Layout 1             | `f867dfdef1f3`  |
| 1401   | Layout 1             | `f867dfdef1f3`  |
| 1396   | Layout 1             | `f867dfdef1f3`  |
| 1391   | Layout 1             | `f867dfdef1f3`  |
| 1390   | Layout 1             | `f867dfdef1f3`  |
| 1386   | Layout 1             | `f867dfdef1f3`  |
| 1381   | Layout 1             | `f867dfdef1f3`  |
| 1379   | Layout 1             | `f867dfdef1f3`  |
| 1372   | Layout 1             | `f867dfdef1f3`  |
| 1366   | Layout 1             | `f867dfdef1f3`  |
| 1364   | Layout 1             | `f867dfdef1f3`  |
| 1363   | Layout 1             | `f867dfdef1f3`  |
| 1360   | Layout 1             | `f867dfdef1f3`  |
| 1358   | Layout 1             | `f867dfdef1f3`  |
| 1355   | Layout 1             | `f867dfdef1f3`  |
| 1351   | Layout 1             | `f867dfdef1f3`  |
| 1348   | Layout 1             | `f867dfdef1f3`  |
| 1346   | Layout 1             | `f867dfdef1f3`  |
| 1341   | Layout 1             | `f867dfdef1f3`  |
| 1340   | Layout 1             | `f867dfdef1f3`  |
| 1338   | Layout 1             | `f867dfdef1f3`  |
| 1335   | Layout 1             | `f867dfdef1f3`  |
| 1333   | Layout 1             | `f867dfdef1f3`  |
| 1329   | Layout 1             | `f867dfdef1f3`  |
| 1327   | Layout 1             | `f867dfdef1f3`  |
| 1324   | Layout 1             | `f867dfdef1f3`  |
| 1321   | Layout 1             | `f867dfdef1f3`  |
| 1319   | Layout 1             | `f867dfdef1f3`  |
| 1318   | Layout 1             | `f867dfdef1f3`  |
| 1316   | Layout 1             | `f867dfdef1f3`  |
| 1313   | Layout 1             | `f867dfdef1f3`  |
| 1311   | Layout 1             | `f867dfdef1f3`  |
| 1309   | Layout 1             | `f867dfdef1f3`  |
| 1304   | Layout 1             | `f867dfdef1f3`  |
| 1292   | Layout 1             | `f867dfdef1f3`  |
| 1286   | Layout 1             | `f867dfdef1f3`  |
| 1280   | Layout 1             | `f867dfdef1f3`  |
| 1276   | Layout 1             | `f867dfdef1f3`  |
| 1267   | Layout 1             | `f867dfdef1f3`  |
| 1261   | Layout 1             | `f867dfdef1f3`  |
| 1256   | Layout 1             | `f867dfdef1f3`  |
| 1250   | Layout 1             | `f867dfdef1f3`  |
| 1246   | Layout 1             | `f867dfdef1f3`  |
| 1239   | Layout 1             | `f867dfdef1f3`  |
| 1230   | Layout 1             | `f867dfdef1f3`  |
| 1226   | Layout 1             | `f867dfdef1f3`  |
| 1220   | Layout 1             | `f867dfdef1f3`  |
| 1217   | Layout 1             | `f867dfdef1f3`  |
| 1211   | Layout 1             | `f867dfdef1f3`  |
| 1210   | Layout 1             | `f867dfdef1f3`  |
| 1208   | Layout 1             | `f867dfdef1f3`  |
| 1203   | Layout 1             | `f867dfdef1f3`  |
| 1197   | Layout 1             | `f867dfdef1f3`  |
| 1194   | Layout 1             | `f867dfdef1f3`  |
| 1192   | Layout 1             | `f867dfdef1f3`  |
| 1187   | Layout 1             | `f867dfdef1f3`  |
| 1183   | Layout 1             | `f867dfdef1f3`  |
| 1177   | Layout 1             | `f867dfdef1f3`  |
| 1173   | Layout 1             | `f867dfdef1f3`  |
| 1167   | Layout 1             | `f867dfdef1f3`  |
| 1164   | Layout 1             | `f867dfdef1f3`  |
| 1156   | Layout 1             | `f867dfdef1f3`  |
| 1149   | Layout 1             | `f867dfdef1f3`  |
| 1144   | Layout 1             | `f867dfdef1f3`  |
| 1137   | Layout 1             | `f867dfdef1f3`  |
| 1132   | Layout 1             | `f867dfdef1f3`  |
| 1127   | Layout 1             | `f867dfdef1f3`  |
| 1122   | Layout 1             | `f867dfdef1f3`  |
| 1118   | Layout 1             | `f867dfdef1f3`  |
| 1114   | Layout 1             | `f867dfdef1f3`  |
| 1109   | Layout 1             | `f867dfdef1f3`  |
| 1102   | No file              | `f867dfdef1f3`  |
| 1096   | No file              | `f867dfdef1f3`  |
| 1088   | No file              | `f867dfdef1f3`  |
| 1081   | No file              | `f867dfdef1f3`  |
| 1076   | No file              | `f867dfdef1f3`  |
| 1069   | No file              | `f867dfdef1f3`  |
| 1064   | No file              | `f867dfdef1f3`  |
| 1058   | No file              | `f867dfdef1f3`  |
| 1051   | No file              | `f867dfdef1f3`  |
| 1044   | No file              | `f867dfdef1f3`  |
| 1036   | No file              | `f867dfdef1f3`  |
| 1026   | No file              | `f867dfdef1f3`  |
| 1016   | No file              | `f867dfdef1f3`  |
| 1009   | No file              | `f867dfdef1f3`  |
| 1005   | No file              | `f867dfdef1f3`  |
| 1000   | No file              | `f867dfdef1f3`  |
| 998    | No file              | `f867dfdef1f3`  |
| 990    | No file              | `f867dfdef1f3`  |
| 979    | No file              | `f867dfdef1f3`  |
| 972    | No file              | `f867dfdef1f3`  |
| 963    | No file              | `f867dfdef1f3`  |
| 955    | No file              | `f867dfdef1f3`  |
| 946    | No file              | `f867dfdef1f3`  |
| 938    | No file              | `f867dfdef1f3`  |
| 927    | No file              | `f867dfdef1f3`  |
| 911    | No file              | `f867dfdef1f3`  |
| 904    | No file              | `f867dfdef1f3`  |
| 899    | No file              | `f867dfdef1f3`  |
| 894    | No file              | `f867dfdef1f3`  |
| 885    | No file              | `f867dfdef1f3`  |
| 879    | No file              | `f867dfdef1f3`  |
| 872    | No file              | `f867dfdef1f3`  |
| 864    | No file              | `f867dfdef1f3`  |
| 855    | No file              | `f867dfdef1f3`  |
| 853    | No file              | `f867dfdef1f3`  |
| 845    | No file              | `f867dfdef1f3`  |
| 837    | No file              | `f867dfdef1f3`  |
| 829    | Layout 1             | `f867dfdef1f3`  |
| 822    | Layout 1             | `f867dfdef1f3`  |
| 814    | Layout 1             | `f867dfdef1f3`  |
| 805    | Layout 1             | `f867dfdef1f3`  |
| 794    | No documented layout | `f867dfdef1f3`  |
| 787    | No documented layout | `f867dfdef1f3`  |
| 780    | No documented layout | `f867dfdef1f3`  |
| 771    | No documented layout | `f867dfdef1f3`  |
| 760    | No documented layout | `f867dfdef1f3`  |
| 748    | No documented layout | `f867dfdef1f3`  |
| 741    | No documented layout | `f867dfdef1f3`  |
| 736    | No documented layout | `f867dfdef1f3`  |
| 731    | No documented layout | `f867dfdef1f3`  |
| 723    | No documented layout | `f867dfdef1f3`  |
| 711    | No documented layout | `f867dfdef1f3`  |
| 707    | No documented layout | `f867dfdef1f3`  |
| 697    | No documented layout | `f867dfdef1f3`  |
| 689    | No documented layout | `f867dfdef1f3`  |
| 683    | No documented layout | `f867dfdef1f3`  |
| 678    | No documented layout | `f867dfdef1f3`  |
| 670    | No documented layout | `f867dfdef1f3`  |
| 661    | No documented layout | `f867dfdef1f3`  |
| 656    | No documented layout | `f867dfdef1f3`  |
| 652    | No documented layout | `f867dfdef1f3`  |
| 643    | No documented layout | `f867dfdef1f3`  |
| 637    | No documented layout | `f867dfdef1f3`  |
| 630    | No documented layout | `f867dfdef1f3`  |
| 627    | No documented layout | `f867dfdef1f3`  |
| 621    | No documented layout | `f867dfdef1f3`  |
| 617    | No documented layout | `f867dfdef1f3`  |
| 615    | No documented layout | `f867dfdef1f3`  |
| 606    | No documented layout | `f867dfdef1f3`  |
| 599    | No documented layout | `f867dfdef1f3`  |
| 592    | No documented layout | `f867dfdef1f3`  |
| 586    | No documented layout | `f867dfdef1f3`  |
| 577    | No documented layout | `f867dfdef1f3`  |
| 569    | No documented layout | `f867dfdef1f3`  |
| 561    | No documented layout | `f867dfdef1f3`  |
| 554    | No documented layout | `f867dfdef1f3`  |
| 542    | No documented layout | `f867dfdef1f3`  |
| 532    | No documented layout | `f867dfdef1f3`  |
| 531    | No documented layout | `f867dfdef1f3`  |
| 526    | No documented layout | `f867dfdef1f3`  |
| 521    | No documented layout | `f867dfdef1f3`  |
| 517    | No documented layout | `f867dfdef1f3`  |
| 510    | No documented layout | `f867dfdef1f3`  |
| 508    | No documented layout | `f867dfdef1f3`  |
| 504    | No documented layout | `f867dfdef1f3`  |
| 497    | No documented layout | `f867dfdef1f3`  |
| 491    | No documented layout | `f867dfdef1f3`  |
| 485    | No documented layout | `f867dfdef1f3`  |
| 478    | No documented layout | `f867dfdef1f3`  |
| 472    | No documented layout | `f867dfdef1f3`  |
| 466    | No documented layout | `f867dfdef1f3`  |
| 457    | No documented layout | `f867dfdef1f3`  |
| 452    | No documented layout | `f867dfdef1f3`  |
| 449    | No documented layout | `f867dfdef1f3`  |
| 435    | No documented layout | `f867dfdef1f3`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                     |
| ------------------- | ------------ | ------------ | ------------------------- |
| `+0x00`             | char[4]      | magic        | `PABR`                    |
| `+0x04`             | u32          | count        | Number of entries; `4` on client 3473 |
| `+0x08`             | Entry[count] | entries      | See Entry                 |
| `entries+0x00`      | String Table | string_table | See String Table          |
| `string_table+0x00` | u32          | data_end     | `8 + count × 6`, the offset of the trailer |
| `string_table+0x04` | u32          | zero         | `0` |

### Entry (6 bytes)

| Offset  | Type | Field     | Notes |
| ------- | ---- | --------- | ----- |
| `+0x00` | u16  | key       | Map key |
| `+0x02` | u16  | param_key | Equals `key` in every entry |
| `+0x04` | i16  | max_level | Highest upgrade level |

### String Table (variable: 4 bytes + strings)

The PABR string table, here with no strings.

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Entries

The entries on client 3473, in file order. The use column follows the developer comments of the private server's sheet (see Field Names).

| Key | Max Level | Use | Referenced by |
| --: | --------: | --- | ------------- |
| 201 | 0 | Luck efficiency, levels 0 to 1: 100/120% | `plantzone.dbss` `luck_productivity_upgrade_group_index` |
| 101 | 0 | Base efficiency, levels 0 to 1: 100/120% | `plantzone.dbss` `productivity_upgrade_group_index` |
| 2   | 5 | Worker capacity, levels 0 to 5: 4/6/8/10/12/14 workers | `planttown.bss` `worker_capacity_upgrade_group_index` |
| 1   | 5 | Warehouse, levels 0 to 5: 40/50/60/70/80/90 slots | `planttown.bss` `warehouse_upgrade_group_index` |

## Notes

- Total size is `8 + count × 6 + 12`: 44 bytes on client 3473.
- `max_level` of groups 101 and 201 is `0` although their sheet comments list levels 0 to 1; only `Level0` is filled in the sheet for them.

## Field Names

The names follow the 2016 `gc::PlantUpgradeParamStaticStatus` (`_key`, `_param` as `int[6]`, `_maxLevel` as a short) and the `PlantUpgradeParam_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (columns `Index`, `Level0` to `Level5`). The sheet's four `Index` values are the file's four keys. Its note column `#참고용 Count` holds `5`, `5`, `0`, `0`, equal to `max_level` on all four entries, and the 2016 member order places `_maxLevel` after the key. The six `_param` values (`Level0` to `Level5`, 40 to 90 warehouse slots for key 1) have no bytes in the client file.

The client Lua enums in `global_define_cpp_enum.luac` name the two level types of each user: `CppEnums.PlantTownLevelType` (`ePlantTownLevelType_Warehouse` `0`, `ePlantTownLevelType_WorkerCapacity` `1`) for the town keys 1 and 2, and `CppEnums.PlantZoneLevelType` (`ePlantZoneLevelType_GeneralEfficiency` `0`, `ePlantZoneLevelType_LuckEfficiency` `1`) for the zone keys 101 and 201.
