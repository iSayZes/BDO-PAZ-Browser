# `planttown.bss` Format

## Purpose

Town table of the worker system: one row per town node where workers can be hired, with the keys of its warehouse and worker capacity upgrades, its max upgrade level and its upgrade cost group. Node IDs resolve through LOC type `29`; most rows are towns, villages, guard posts, islands, or trade-zone nodes.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File            | Bytes | Records           | Row bytes |
| ------ | ------------- | --------------- | ----- | ----------------- | --------- |
| 1      | 805 and later | `planttown.bss` | 572   | 46 Plant Town Row | 12        |

| Layout | File            | Known          | Unknown    |
| ------ | --------------- | -------------- | ---------- |
| 1      | `planttown.bss` | 572 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `b6b2d9557376`  |
| 3482   | Layout 1             | `b6b2d9557376`  |
| 3474   | Layout 1             | `b6b2d9557376`  |
| 3473   | Layout 1             | `b6b2d9557376`  |
| 3464   | Layout 1             | `b6b2d9557376`  |
| 3458   | Layout 1             | `b6b2d9557376`  |
| 3454   | Layout 1             | `b6b2d9557376`  |
| 3444   | Layout 1             | `b6b2d9557376`  |
| 3435   | Layout 1             | `b6b2d9557376`  |
| 3426   | Layout 1             | `b6b2d9557376`  |
| 3418   | Layout 1             | `b6b2d9557376`  |
| 3412   | Layout 1             | `b6b2d9557376`  |
| 3402   | Layout 1             | `b6b2d9557376`  |
| 3396   | Layout 1             | `b6b2d9557376`  |
| 3387   | Layout 1             | `b6b2d9557376`  |
| 3381   | Layout 1             | `b6b2d9557376`  |
| 3373   | Layout 1             | `b6b2d9557376`  |
| 3364   | Layout 1             | `b6b2d9557376`  |
| 3356   | Layout 1             | `b6b2d9557376`  |
| 3349   | Layout 1             | `b6b2d9557376`  |
| 3342   | Layout 1             | `b6b2d9557376`  |
| 3335   | Layout 1             | `b6b2d9557376`  |
| 3326   | Layout 1             | `b6b2d9557376`  |
| 3321   | Layout 1             | `b6b2d9557376`  |
| 3314   | Layout 1             | `b6b2d9557376`  |
| 3303   | Layout 1             | `b6b2d9557376`  |
| 3302   | Layout 1             | `b6b2d9557376`  |
| 3293   | Layout 1             | `b6b2d9557376`  |
| 3283   | Layout 1             | `b6b2d9557376`  |
| 3275   | Layout 1             | `b6b2d9557376`  |
| 3267   | Layout 1             | `b6b2d9557376`  |
| 3258   | Layout 1             | `b6b2d9557376`  |
| 3251   | Layout 1             | `b6b2d9557376`  |
| 3242   | Layout 1             | `b6b2d9557376`  |
| 3235   | Layout 1             | `b6b2d9557376`  |
| 3229   | Layout 1             | `b6b2d9557376`  |
| 3212   | Layout 1             | `b6b2d9557376`  |
| 3203   | Layout 1             | `b6b2d9557376`  |
| 3193   | Layout 1             | `b6b2d9557376`  |
| 3186   | Layout 1             | `b6b2d9557376`  |
| 3177   | Layout 1             | `b6b2d9557376`  |
| 3169   | Layout 1             | `b6b2d9557376`  |
| 3158   | Layout 1             | `b6b2d9557376`  |
| 3151   | Layout 1             | `b6b2d9557376`  |
| 3144   | Layout 1             | `b6b2d9557376`  |
| 3133   | Layout 1             | `b6b2d9557376`  |
| 3125   | Layout 1             | `b6b2d9557376`  |
| 3118   | Layout 1             | `b6b2d9557376`  |
| 3111   | Layout 1             | `b6b2d9557376`  |
| 3103   | Layout 1             | `b6b2d9557376`  |
| 3095   | Layout 1             | `b6b2d9557376`  |
| 3086   | Layout 1             | `b6b2d9557376`  |
| 3072   | Layout 1             | `b6b2d9557376`  |
| 3062   | Layout 1             | `b6b2d9557376`  |
| 3052   | Layout 1             | `b6b2d9557376`  |
| 3045   | Layout 1             | `b6b2d9557376`  |
| 3037   | Layout 1             | `b6b2d9557376`  |
| 3030   | Layout 1             | `b6b2d9557376`  |
| 3021   | Layout 1             | `b6b2d9557376`  |
| 3012   | Layout 1             | `b6b2d9557376`  |
| 3002   | Layout 1             | `b6b2d9557376`  |
| 2995   | Layout 1             | `b6b2d9557376`  |
| 2987   | Layout 1             | `b6b2d9557376`  |
| 2978   | Layout 1             | `b6b2d9557376`  |
| 2970   | Layout 1             | `b6b2d9557376`  |
| 2959   | Layout 1             | `b6b2d9557376`  |
| 2951   | Layout 1             | `b6b2d9557376`  |
| 2942   | Layout 1             | `b6b2d9557376`  |
| 2935   | Layout 1             | `b6b2d9557376`  |
| 2932   | Layout 1             | `b6b2d9557376`  |
| 2923   | Layout 1             | `b6b2d9557376`  |
| 2919   | Layout 1             | `b6b2d9557376`  |
| 2907   | Layout 1             | `b6b2d9557376`  |
| 2900   | Layout 1             | `b6b2d9557376`  |
| 2891   | Layout 1             | `b6b2d9557376`  |
| 2882   | Layout 1             | `b6b2d9557376`  |
| 2872   | Layout 1             | `b6b2d9557376`  |
| 2863   | Layout 1             | `b6b2d9557376`  |
| 2855   | Layout 1             | `b6b2d9557376`  |
| 2849   | Layout 1             | `b6b2d9557376`  |
| 2844   | Layout 1             | `b6b2d9557376`  |
| 2834   | Layout 1             | `b6b2d9557376`  |
| 2825   | Layout 1             | `b6b2d9557376`  |
| 2819   | Layout 1             | `b6b2d9557376`  |
| 2811   | Layout 1             | `b6b2d9557376`  |
| 2803   | Layout 1             | `b6b2d9557376`  |
| 2794   | Layout 1             | `b6b2d9557376`  |
| 2783   | Layout 1             | `b6b2d9557376`  |
| 2774   | Layout 1             | `b6b2d9557376`  |
| 2765   | Layout 1             | `b6b2d9557376`  |
| 2756   | Layout 1             | `b6b2d9557376`  |
| 2750   | Layout 1             | `b6b2d9557376`  |
| 2743   | Layout 1             | `b6b2d9557376`  |
| 2736   | Layout 1             | `b6b2d9557376`  |
| 2726   | Layout 1             | `b6b2d9557376`  |
| 2717   | Layout 1             | `b6b2d9557376`  |
| 2709   | Layout 1             | `b6b2d9557376`  |
| 2703   | Layout 1             | `b6b2d9557376`  |
| 2695   | Layout 1             | `b6b2d9557376`  |
| 2684   | Layout 1             | `b6b2d9557376`  |
| 2672   | Layout 1             | `b6b2d9557376`  |
| 2665   | Layout 1             | `b6b2d9557376`  |
| 2657   | Layout 1             | `b6b2d9557376`  |
| 2649   | Layout 1             | `b6b2d9557376`  |
| 2644   | Layout 1             | `b6b2d9557376`  |
| 2637   | Layout 1             | `b6b2d9557376`  |
| 2629   | Layout 1             | `b6b2d9557376`  |
| 2619   | Layout 1             | `b6b2d9557376`  |
| 2612   | Layout 1             | `b6b2d9557376`  |
| 2606   | Layout 1             | `b6b2d9557376`  |
| 2602   | Layout 1             | `b6b2d9557376`  |
| 2601   | Layout 1             | `b6b2d9557376`  |
| 2592   | Layout 1             | `b6b2d9557376`  |
| 2583   | Layout 1             | `b6b2d9557376`  |
| 2575   | Layout 1             | `b6b2d9557376`  |
| 2567   | Layout 1             | `b6b2d9557376`  |
| 2560   | Layout 1             | `b6b2d9557376`  |
| 2553   | Layout 1             | `b6b2d9557376`  |
| 2545   | Layout 1             | `b6b2d9557376`  |
| 2538   | Layout 1             | `b6b2d9557376`  |
| 2529   | Layout 1             | `b6b2d9557376`  |
| 2519   | Layout 1             | `b6b2d9557376`  |
| 2513   | Layout 1             | `b6b2d9557376`  |
| 2510   | Layout 1             | `b6b2d9557376`  |
| 2507   | Layout 1             | `b6b2d9557376`  |
| 2503   | Layout 1             | `b6b2d9557376`  |
| 2498   | Layout 1             | `b6b2d9557376`  |
| 2492   | Layout 1             | `b6b2d9557376`  |
| 2487   | Layout 1             | `b6b2d9557376`  |
| 2480   | Layout 1             | `b6b2d9557376`  |
| 2474   | Layout 1             | `b6b2d9557376`  |
| 2468   | Layout 1             | `b6b2d9557376`  |
| 2460   | Layout 1             | `b6b2d9557376`  |
| 2453   | Layout 1             | `b6b2d9557376`  |
| 2444   | Layout 1             | `b6b2d9557376`  |
| 2438   | Layout 1             | `b6b2d9557376`  |
| 2434   | Layout 1             | `b6b2d9557376`  |
| 2429   | Layout 1             | `b6b2d9557376`  |
| 2421   | Layout 1             | `b6b2d9557376`  |
| 2414   | Layout 1             | `b6b2d9557376`  |
| 2407   | Layout 1             | `b6b2d9557376`  |
| 2401   | Layout 1             | `b6b2d9557376`  |
| 2397   | Layout 1             | `b6b2d9557376`  |
| 2393   | Layout 1             | `b6b2d9557376`  |
| 2384   | Layout 1             | `b6b2d9557376`  |
| 2378   | Layout 1             | `b6b2d9557376`  |
| 2372   | Layout 1             | `b6b2d9557376`  |
| 2358   | Layout 1             | `b6b2d9557376`  |
| 2352   | Layout 1             | `b6b2d9557376`  |
| 2347   | Layout 1             | `b6b2d9557376`  |
| 2343   | Layout 1             | `b6b2d9557376`  |
| 2335   | Layout 1             | `b6b2d9557376`  |
| 2327   | Layout 1             | `b6b2d9557376`  |
| 2324   | Layout 1             | `b6b2d9557376`  |
| 2319   | Layout 1             | `b6b2d9557376`  |
| 2313   | Layout 1             | `b6b2d9557376`  |
| 2308   | Layout 1             | `b6b2d9557376`  |
| 2302   | Layout 1             | `b6b2d9557376`  |
| 2295   | Layout 1             | `b6b2d9557376`  |
| 2290   | Layout 1             | `b6b2d9557376`  |
| 2284   | Layout 1             | `b6b2d9557376`  |
| 2276   | Layout 1             | `b6b2d9557376`  |
| 2269   | Layout 1             | `b6b2d9557376`  |
| 2259   | Layout 1             | `b6b2d9557376`  |
| 2250   | Layout 1             | `b6b2d9557376`  |
| 2243   | Layout 1             | `b6b2d9557376`  |
| 2235   | Layout 1             | `b6b2d9557376`  |
| 2229   | Layout 1             | `b6b2d9557376`  |
| 2224   | Layout 1             | `b6b2d9557376`  |
| 2218   | Layout 1             | `b6b2d9557376`  |
| 2215   | Layout 1             | `b6b2d9557376`  |
| 2207   | Layout 1             | `b6b2d9557376`  |
| 2203   | Layout 1             | `b6b2d9557376`  |
| 2196   | Layout 1             | `b6b2d9557376`  |
| 2192   | Layout 1             | `b6b2d9557376`  |
| 2189   | Layout 1             | `b6b2d9557376`  |
| 2183   | Layout 1             | `b6b2d9557376`  |
| 2179   | Layout 1             | `b6b2d9557376`  |
| 2171   | Layout 1             | `b6b2d9557376`  |
| 2163   | Layout 1             | `b6b2d9557376`  |
| 2156   | Layout 1             | `b6b2d9557376`  |
| 2151   | Layout 1             | `b6b2d9557376`  |
| 2147   | Layout 1             | `b6b2d9557376`  |
| 2142   | Layout 1             | `b6b2d9557376`  |
| 2138   | Layout 1             | `b6b2d9557376`  |
| 2134   | Layout 1             | `b6b2d9557376`  |
| 2130   | Layout 1             | `b6b2d9557376`  |
| 2122   | Layout 1             | `b6b2d9557376`  |
| 2107   | Layout 1             | `b6b2d9557376`  |
| 2098   | Layout 1             | `b6b2d9557376`  |
| 2089   | Layout 1             | `b6b2d9557376`  |
| 2081   | Layout 1             | `b6b2d9557376`  |
| 2073   | Layout 1             | `b6b2d9557376`  |
| 2067   | Layout 1             | `b6b2d9557376`  |
| 2063   | Layout 1             | `b6b2d9557376`  |
| 2059   | Layout 1             | `b6b2d9557376`  |
| 2052   | Layout 1             | `b6b2d9557376`  |
| 2044   | Layout 1             | `b6b2d9557376`  |
| 2039   | Layout 1             | `b6b2d9557376`  |
| 2032   | Layout 1             | `b6b2d9557376`  |
| 2025   | Layout 1             | `b6b2d9557376`  |
| 2011   | Layout 1             | `b6b2d9557376`  |
| 2005   | Layout 1             | `b6b2d9557376`  |
| 2000   | Layout 1             | `b6b2d9557376`  |
| 1996   | Layout 1             | `b6b2d9557376`  |
| 1991   | Layout 1             | `b6b2d9557376`  |
| 1985   | Layout 1             | `b6b2d9557376`  |
| 1980   | Layout 1             | `b6b2d9557376`  |
| 1969   | Layout 1             | `b6b2d9557376`  |
| 1964   | Layout 1             | `b6b2d9557376`  |
| 1958   | Layout 1             | `b6b2d9557376`  |
| 1950   | Layout 1             | `b6b2d9557376`  |
| 1945   | Layout 1             | `b6b2d9557376`  |
| 1937   | Layout 1             | `b6b2d9557376`  |
| 1933   | Layout 1             | `b6b2d9557376`  |
| 1927   | Layout 1             | `b6b2d9557376`  |
| 1921   | Layout 1             | `b6b2d9557376`  |
| 1914   | Layout 1             | `b6b2d9557376`  |
| 1908   | Layout 1             | `b6b2d9557376`  |
| 1897   | Layout 1             | `b6b2d9557376`  |
| 1892   | Layout 1             | `b6b2d9557376`  |
| 1886   | Layout 1             | `b6b2d9557376`  |
| 1881   | Layout 1             | `b6b2d9557376`  |
| 1871   | Layout 1             | `b6b2d9557376`  |
| 1866   | Layout 1             | `b6b2d9557376`  |
| 1862   | Layout 1             | `b6b2d9557376`  |
| 1854   | Layout 1             | `b6b2d9557376`  |
| 1846   | Layout 1             | `b6b2d9557376`  |
| 1838   | Layout 1             | `b6b2d9557376`  |
| 1832   | Layout 1             | `b6b2d9557376`  |
| 1826   | Layout 1             | `b6b2d9557376`  |
| 1822   | Layout 1             | `b6b2d9557376`  |
| 1818   | Layout 1             | `b6b2d9557376`  |
| 1804   | Layout 1             | `b6b2d9557376`  |
| 1794   | Layout 1             | `b6b2d9557376`  |
| 1790   | Layout 1             | `b6b2d9557376`  |
| 1784   | Layout 1             | `b6b2d9557376`  |
| 1774   | Layout 1             | `b6b2d9557376`  |
| 1771   | Layout 1             | `b6b2d9557376`  |
| 1762   | Layout 1             | `b6b2d9557376`  |
| 1759   | Layout 1             | `b6b2d9557376`  |
| 1754   | Layout 1             | `b6b2d9557376`  |
| 1749   | Layout 1             | `b6b2d9557376`  |
| 1743   | Layout 1             | `b6b2d9557376`  |
| 1737   | Layout 1             | `b6b2d9557376`  |
| 1731   | Layout 1             | `b6b2d9557376`  |
| 1725   | Layout 1             | `b6b2d9557376`  |
| 1717   | Layout 1             | `b6b2d9557376`  |
| 1710   | Layout 1             | `b6b2d9557376`  |
| 1704   | Layout 1             | `b6b2d9557376`  |
| 1698   | Layout 1             | `b6b2d9557376`  |
| 1690   | Layout 1             | `b6b2d9557376`  |
| 1685   | Layout 1             | `b6b2d9557376`  |
| 1680   | Layout 1             | `b6b2d9557376`  |
| 1674   | Layout 1             | `b6b2d9557376`  |
| 1668   | Layout 1             | `b6b2d9557376`  |
| 1659   | Layout 1             | `b6b2d9557376`  |
| 1649   | Layout 1             | `b6b2d9557376`  |
| 1642   | Layout 1             | `b6b2d9557376`  |
| 1636   | Layout 1             | `b6b2d9557376`  |
| 1628   | Layout 1             | `b6b2d9557376`  |
| 1622   | Layout 1             | `b6b2d9557376`  |
| 1614   | Layout 1             | `b6b2d9557376`  |
| 1608   | Layout 1             | `b6b2d9557376`  |
| 1602   | Layout 1             | `b6b2d9557376`  |
| 1598   | Layout 1             | `b6b2d9557376`  |
| 1594   | Layout 1             | `b6b2d9557376`  |
| 1590   | Layout 1             | `b6b2d9557376`  |
| 1587   | Layout 1             | `b6b2d9557376`  |
| 1584   | Layout 1             | `b6b2d9557376`  |
| 1579   | Layout 1             | `b6b2d9557376`  |
| 1572   | Layout 1             | `b6b2d9557376`  |
| 1565   | Layout 1             | `b6b2d9557376`  |
| 1559   | Layout 1             | `b6b2d9557376`  |
| 1554   | Layout 1             | `b6b2d9557376`  |
| 1547   | Layout 1             | `b6b2d9557376`  |
| 1537   | Layout 1             | `b6b2d9557376`  |
| 1529   | Layout 1             | `b6b2d9557376`  |
| 1524   | Layout 1             | `b6b2d9557376`  |
| 1519   | Layout 1             | `b6b2d9557376`  |
| 1509   | Layout 1             | `b6b2d9557376`  |
| 1506   | Layout 1             | `b6b2d9557376`  |
| 1504   | Layout 1             | `b6b2d9557376`  |
| 1500   | Layout 1             | `b6b2d9557376`  |
| 1493   | Layout 1             | `b6b2d9557376`  |
| 1489   | Layout 1             | `b6b2d9557376`  |
| 1485   | Layout 1             | `b6b2d9557376`  |
| 1481   | Layout 1             | `b6b2d9557376`  |
| 1474   | Layout 1             | `b6b2d9557376`  |
| 1466   | Layout 1             | `b6b2d9557376`  |
| 1462   | Layout 1             | `b6b2d9557376`  |
| 1459   | Layout 1             | `b6b2d9557376`  |
| 1453   | Layout 1             | `b6b2d9557376`  |
| 1450   | Layout 1             | `b6b2d9557376`  |
| 1445   | Layout 1             | `b6b2d9557376`  |
| 1439   | Layout 1             | `b6b2d9557376`  |
| 1433   | Layout 1             | `b6b2d9557376`  |
| 1430   | Layout 1             | `b6b2d9557376`  |
| 1426   | Layout 1             | `b6b2d9557376`  |
| 1421   | Layout 1             | `b6b2d9557376`  |
| 1417   | Layout 1             | `b6b2d9557376`  |
| 1416   | Layout 1             | `b6b2d9557376`  |
| 1409   | Layout 1             | `b6b2d9557376`  |
| 1405   | Layout 1             | `b6b2d9557376`  |
| 1401   | Layout 1             | `b6b2d9557376`  |
| 1396   | Layout 1             | `b6b2d9557376`  |
| 1391   | Layout 1             | `b6b2d9557376`  |
| 1390   | Layout 1             | `b6b2d9557376`  |
| 1386   | Layout 1             | `b6b2d9557376`  |
| 1381   | Layout 1             | `b6b2d9557376`  |
| 1379   | Layout 1             | `b6b2d9557376`  |
| 1372   | Layout 1             | `b6b2d9557376`  |
| 1366   | Layout 1             | `b6b2d9557376`  |
| 1364   | Layout 1             | `b6b2d9557376`  |
| 1363   | Layout 1             | `b6b2d9557376`  |
| 1360   | Layout 1             | `b6b2d9557376`  |
| 1358   | Layout 1             | `b6b2d9557376`  |
| 1355   | Layout 1             | `b6b2d9557376`  |
| 1351   | Layout 1             | `b6b2d9557376`  |
| 1348   | Layout 1             | `b6b2d9557376`  |
| 1346   | Layout 1             | `b6b2d9557376`  |
| 1341   | Layout 1             | `b6b2d9557376`  |
| 1340   | Layout 1             | `b6b2d9557376`  |
| 1338   | Layout 1             | `b6b2d9557376`  |
| 1335   | Layout 1             | `b6b2d9557376`  |
| 1333   | Layout 1             | `b6b2d9557376`  |
| 1329   | Layout 1             | `b6b2d9557376`  |
| 1327   | Layout 1             | `b6b2d9557376`  |
| 1324   | Layout 1             | `b6b2d9557376`  |
| 1321   | Layout 1             | `b6b2d9557376`  |
| 1319   | Layout 1             | `b6b2d9557376`  |
| 1318   | Layout 1             | `b6b2d9557376`  |
| 1316   | Layout 1             | `b6b2d9557376`  |
| 1313   | Layout 1             | `b6b2d9557376`  |
| 1311   | Layout 1             | `b6b2d9557376`  |
| 1309   | Layout 1             | `b6b2d9557376`  |
| 1304   | Layout 1             | `b6b2d9557376`  |
| 1292   | Layout 1             | `b6b2d9557376`  |
| 1286   | Layout 1             | `b6b2d9557376`  |
| 1280   | Layout 1             | `b6b2d9557376`  |
| 1276   | Layout 1             | `b6b2d9557376`  |
| 1267   | Layout 1             | `b6b2d9557376`  |
| 1261   | Layout 1             | `b6b2d9557376`  |
| 1256   | Layout 1             | `b6b2d9557376`  |
| 1250   | Layout 1             | `b6b2d9557376`  |
| 1246   | Layout 1             | `b6b2d9557376`  |
| 1239   | Layout 1             | `b6b2d9557376`  |
| 1230   | Layout 1             | `b6b2d9557376`  |
| 1226   | Layout 1             | `b6b2d9557376`  |
| 1220   | Layout 1             | `b6b2d9557376`  |
| 1217   | Layout 1             | `b6b2d9557376`  |
| 1211   | Layout 1             | `b6b2d9557376`  |
| 1210   | Layout 1             | `b6b2d9557376`  |
| 1208   | Layout 1             | `b6b2d9557376`  |
| 1203   | Layout 1             | `b6b2d9557376`  |
| 1197   | Layout 1             | `b6b2d9557376`  |
| 1194   | Layout 1             | `b6b2d9557376`  |
| 1192   | Layout 1             | `b6b2d9557376`  |
| 1187   | Layout 1             | `b6b2d9557376`  |
| 1183   | Layout 1             | `b6b2d9557376`  |
| 1177   | Layout 1             | `b6b2d9557376`  |
| 1173   | Layout 1             | `b6b2d9557376`  |
| 1167   | Layout 1             | `b6b2d9557376`  |
| 1164   | Layout 1             | `b6b2d9557376`  |
| 1156   | Layout 1             | `b6b2d9557376`  |
| 1149   | Layout 1             | `b6b2d9557376`  |
| 1144   | Layout 1             | `b6b2d9557376`  |
| 1137   | Layout 1             | `b6b2d9557376`  |
| 1132   | Layout 1             | `b6b2d9557376`  |
| 1127   | Layout 1             | `b6b2d9557376`  |
| 1122   | Layout 1             | `b6b2d9557376`  |
| 1118   | Layout 1             | `b6b2d9557376`  |
| 1114   | Layout 1             | `b6b2d9557376`  |
| 1109   | Layout 1             | `b6b2d9557376`  |
| 1102   | No file              | `b6b2d9557376`  |
| 1096   | No file              | `b6b2d9557376`  |
| 1088   | No file              | `b6b2d9557376`  |
| 1081   | No file              | `b6b2d9557376`  |
| 1076   | No file              | `b6b2d9557376`  |
| 1069   | No file              | `b6b2d9557376`  |
| 1064   | No file              | `b6b2d9557376`  |
| 1058   | No file              | `b6b2d9557376`  |
| 1051   | No file              | `b6b2d9557376`  |
| 1044   | No file              | `b6b2d9557376`  |
| 1036   | No file              | `b6b2d9557376`  |
| 1026   | No file              | `b6b2d9557376`  |
| 1016   | No file              | `b6b2d9557376`  |
| 1009   | No file              | `b6b2d9557376`  |
| 1005   | No file              | `b6b2d9557376`  |
| 1000   | No file              | `b6b2d9557376`  |
| 998    | No file              | `b6b2d9557376`  |
| 990    | No file              | `b6b2d9557376`  |
| 979    | No file              | `b6b2d9557376`  |
| 972    | No file              | `b6b2d9557376`  |
| 963    | No file              | `b6b2d9557376`  |
| 955    | No file              | `b6b2d9557376`  |
| 946    | No file              | `b6b2d9557376`  |
| 938    | No file              | `b6b2d9557376`  |
| 927    | No file              | `b6b2d9557376`  |
| 911    | No file              | `b6b2d9557376`  |
| 904    | No file              | `b6b2d9557376`  |
| 899    | No file              | `b6b2d9557376`  |
| 894    | No file              | `b6b2d9557376`  |
| 885    | No file              | `b6b2d9557376`  |
| 879    | No file              | `b6b2d9557376`  |
| 872    | No file              | `b6b2d9557376`  |
| 864    | No file              | `b6b2d9557376`  |
| 855    | No file              | `b6b2d9557376`  |
| 853    | No file              | `b6b2d9557376`  |
| 845    | No file              | `b6b2d9557376`  |
| 837    | No file              | `b6b2d9557376`  |
| 829    | Layout 1             | `b6b2d9557376`  |
| 822    | Layout 1             | `b6b2d9557376`  |
| 814    | Layout 1             | `b6b2d9557376`  |
| 805    | Layout 1             | `b6b2d9557376`  |
| 794    | No documented layout | `b6b2d9557376`  |
| 787    | No documented layout | `b6b2d9557376`  |
| 780    | No documented layout | `b6b2d9557376`  |
| 771    | No documented layout | `b6b2d9557376`  |
| 760    | No documented layout | `b6b2d9557376`  |
| 748    | No documented layout | `b6b2d9557376`  |
| 741    | No documented layout | `b6b2d9557376`  |
| 736    | No documented layout | `b6b2d9557376`  |
| 731    | No documented layout | `b6b2d9557376`  |
| 723    | No documented layout | `b6b2d9557376`  |
| 711    | No documented layout | `b6b2d9557376`  |
| 707    | No documented layout | `b6b2d9557376`  |
| 697    | No documented layout | `b6b2d9557376`  |
| 689    | No documented layout | `b6b2d9557376`  |
| 683    | No documented layout | `b6b2d9557376`  |
| 678    | No documented layout | `b6b2d9557376`  |
| 670    | No documented layout | `b6b2d9557376`  |
| 661    | No documented layout | `b6b2d9557376`  |
| 656    | No documented layout | `b6b2d9557376`  |
| 652    | No documented layout | `b6b2d9557376`  |
| 643    | No documented layout | `b6b2d9557376`  |
| 637    | No documented layout | `b6b2d9557376`  |
| 630    | No documented layout | `b6b2d9557376`  |
| 627    | No documented layout | `b6b2d9557376`  |
| 621    | No documented layout | `b6b2d9557376`  |
| 617    | No documented layout | `b6b2d9557376`  |
| 615    | No documented layout | `b6b2d9557376`  |
| 606    | No documented layout | `b6b2d9557376`  |
| 599    | No documented layout | `b6b2d9557376`  |
| 592    | No documented layout | `b6b2d9557376`  |
| 586    | No documented layout | `b6b2d9557376`  |
| 577    | No documented layout | `b6b2d9557376`  |
| 569    | No documented layout | `b6b2d9557376`  |
| 561    | No documented layout | `b6b2d9557376`  |
| 554    | No documented layout | `b6b2d9557376`  |
| 542    | No documented layout | `b6b2d9557376`  |
| 532    | No documented layout | `b6b2d9557376`  |
| 531    | No documented layout | `b6b2d9557376`  |
| 526    | No documented layout | `b6b2d9557376`  |
| 521    | No documented layout | `b6b2d9557376`  |
| 517    | No documented layout | `b6b2d9557376`  |
| 510    | No documented layout | `b6b2d9557376`  |
| 508    | No documented layout | `b6b2d9557376`  |
| 504    | No documented layout | `b6b2d9557376`  |
| 497    | No documented layout | `b6b2d9557376`  |
| 491    | No documented layout | `b6b2d9557376`  |
| 485    | No documented layout | `b6b2d9557376`  |
| 478    | No documented layout | `b6b2d9557376`  |
| 472    | No documented layout | `b6b2d9557376`  |
| 466    | No documented layout | `b6b2d9557376`  |
| 457    | No documented layout | `b6b2d9557376`  |
| 452    | No documented layout | `b6b2d9557376`  |
| 449    | No documented layout | `b6b2d9557376`  |
| 435    | No documented layout | `b6b2d9557376`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                           |
| --------------------- | -------- | ---------------------------------------------- |
| `languagedata_en.loc` | Optional | Resolves `node_id` display names via type `29` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

Rows start immediately after the header at `+0x08`. The observed file is fully described by:

```text
8-byte header + (45 * 12-byte rows) + 12-byte trailer = 560 bytes
```

The 2026-09-27 client holds 46 rows in 572 bytes.

| Offset              | Type                   | Field        | Notes                                                |
| ------------------- | ---------------------- | ------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]                | magic        | `PABR` (ASCII)                                       |
| `+0x04`             | u32                    | count        | Number of rows; observed `45` in the pre-2026-09-27 fixture, `46` in the 2026-09-27 client |
| `+0x08`             | Plant Town Row[count]  | rows         | See Plant Town Row                                   |
| `rows+0x00`         | String Table           | string_table | The 12-byte trailer starts here; see String Table    |
| `string_table+0x00` | u32                    | end_of_rows  | Byte offset immediately after rows; `8 + count * 12`; observed `548` |
| `string_table+0x04` | u32                    | zero         | Observed zero                                        |

### Plant Town Row (12 bytes)

| Offset  | Type | Field                               | Notes                                         |
| ------- | ---- | ----------------------------------- | --------------------------------------------- |
| `+0x00` | u32  | node_id                             | LOC type `29`, `str_id1=node_id`, `str_id4=0` |
| `+0x04` | u16  | warehouse_upgrade_group_index       | Key into [plantupgradeparam.bss](plantupgradeparam_bss.md); `1` in every row |
| `+0x06` | u16  | worker_capacity_upgrade_group_index | Key into [plantupgradeparam.bss](plantupgradeparam_bss.md); `2` in every row |
| `+0x08` | i16  | max_level                           | Highest upgrade level; `10` in every row      |
| `+0x0A` | u16  | upgrade_resource_key                | Level group in [plantupgraderesource.bss](plantupgraderesource_bss.md); `1` in every row |

The constants hold on all 46 rows of client 3473. Earlier versions of this doc called the four fields `unknown_04` to `unknown_0a`, and before that `unknown_a` to `unknown_d`.

Derived field:

```text
node_name = LOC type 29, str_id1=node_id, str_id4=0
```

### String Table (variable: 4 bytes + strings)

The PABR string table, here with no strings.

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Observed zero           |
| `+0x04` | pstr[string_count] | strings      | Empty                   |

## Reference Rows

| Row | Node ID | Node Name              | Warehouse | Worker Capacity | Max Level | Upgrade Resource |
| --: | ------: | ---------------------- | --------: | --------------: | --------: | ---------------: |
|   0 |  `1785` | Nampo's Moodle Village |        `1` |        `2` |       `10` |        `1` |
|   1 |  `1781` | Dalbeol Village        |        `1` |        `2` |       `10` |        `1` |
|   8 |  `1623` | Grána                  |        `1` |        `2` |       `10` |        `1` |
|  18 |  `1141` | Tarif                  |        `1` |        `2` |       `10` |        `1` |
|  25 |  `1301` | Valencia City          |        `1` |        `2` |       `10` |        `1` |
|  32 |   `601` | Calpheon               |        `1` |        `2` |       `10` |        `1` |
|  42 |     `1` | Velia                  |        `1` |        `2` |       `10` |        `1` |
|  44 |   `301` | Heidel                 |        `1` |        `2` |       `10` |        `1` |

Row numbers are from the pre-2026-09-27 fixture. The 2026-09-27 client inserts Angavu Outpost (`2057`) as row 0, so every row above moves down by one.

## Notes

- Observed decompressed size is `560` bytes.
- `planttown.bss` has no same-stem companion file in the PAZ listing.
- All 45 `node_id` values resolve through LOC type `29` with `str_id4=0`.
- The row order follows neither the node IDs nor the sheet's row order, see Open Questions.
- `plantworkerselect.bss` uses related town selection data, but its IDs are not a direct match for this file; for example `planttown.bss` uses node `601` for Calpheon, while `plantworkerselect.bss` uses selection ID `77` for Calpheon City.

## Field Names

The names follow the `PlantTown_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (columns `WaypointKey`, `WarehouseUpgradeGroupIndex`, `WorkerCapacityUpgradeGroupIndex`, `MaxLevel`, `UpgradeResource`) and the 2016 `gc::PlantTownStaticStatus` member order (`_key`, `_isBlockedNpcWork`, `_warehouseParamKey`, `_workerCapacityParamKey`, `_maxLevel` as a short, `_upgradeResourceKey`). The sheet's 35 towns hold `1`, `2`, `10`, `1`, the values of the file's 34 shared rows, so the names rest on the column order and the 2016 member order, not on a value match. The 2016 `_isBlockedNpcWork` bool has no byte in the record. The client Lua enum `CppEnums.PlantTownLevelType` (`global_define_cpp_enum.luac`) lists the two town level types in the same order: `ePlantTownLevelType_Warehouse` (`0`) and `ePlantTownLevelType_WorkerCapacity` (`1`).

- `warehouse_upgrade_group_index` and `worker_capacity_upgrade_group_index` are keys of [plantupgradeparam.bss](plantupgradeparam_bss.md) (1 warehouse, 2 worker capacity).
- `upgrade_resource_key` is a level group of [plantupgraderesource.bss](plantupgraderesource_bss.md) (1, town, levels 1 to 16).

## Open Questions

### Row Order Meaning

The rows follow neither the node IDs nor the `PlantTown_Table` row order (the sheet starts Velia, Western Guard Camp, Olvia, Heidel, Glish; the file ends Olvia, Western Guard Camp, Velia, Glish, Heidel). The 2016 client loads the table into a `pa::BinaryUnorderedMap<gc::PlantKey, ...>`, a hash map keyed by node, so the order may only be that container's storage order. Whether any client code reads the rows in file order is not checked.
