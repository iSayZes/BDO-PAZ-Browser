# `servantupgrade.dbss` Format

## Purpose

Ship upgrade recipes: for each ship that can be upgraded, the ships it can
become, with the four equipped gear pieces (and their enhancement level)
the upgrade takes and up to ten material stacks. On client 3474 the file has
13 upgrades from 8 ships, such as Bartali Sailboat (31053) to Epheria
Sailboat (31001) and Epheria Caravel (31048) to Epheria Carrack: Advance
(31054).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                        | Bytes | Records                       | Row bytes |
| ------ | -------------- | --------------------------- | ----- | ----------------------------- | --------- |
| 1      | 1346 and later | `servantupgrade.dbss`       | 2,272 | 182 Item, 13 Upgrade, 8 Group | 12        |
| 1      | 1346 and later | `servantupgradeoffset.dbss` | 182   | 13 Offset Row, 8 Offset Group | 10        |

| Layout | File                        | Known            | Unknown    |
| ------ | --------------------------- | ---------------- | ---------- |
| 1      | `servantupgrade.dbss`       | 2,272 B (100.0%) | 0 B (0.0%) |
| 1      | `servantupgradeoffset.dbss` | 182 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `adc17c7cba57`  |
| 3482   | Layout 1             | `adc17c7cba57`  |
| 3474   | Layout 1             | `adc17c7cba57`  |
| 3473   | Layout 1             | `adc17c7cba57`  |
| 3464   | Layout 1             | `adc17c7cba57`  |
| 3458   | Layout 1             | `adc17c7cba57`  |
| 3454   | Layout 1             | `adc17c7cba57`  |
| 3444   | Layout 1             | `adc17c7cba57`  |
| 3435   | Layout 1             | `adc17c7cba57`  |
| 3426   | Layout 1             | `adc17c7cba57`  |
| 3418   | Layout 1             | `adc17c7cba57`  |
| 3412   | Layout 1             | `adc17c7cba57`  |
| 3402   | Layout 1             | `adc17c7cba57`  |
| 3396   | Layout 1             | `adc17c7cba57`  |
| 3387   | Layout 1             | `adc17c7cba57`  |
| 3381   | Layout 1             | `adc17c7cba57`  |
| 3373   | Layout 1             | `adc17c7cba57`  |
| 3364   | Layout 1             | `adc17c7cba57`  |
| 3356   | Layout 1             | `adc17c7cba57`  |
| 3349   | Layout 1             | `adc17c7cba57`  |
| 3342   | Layout 1             | `adc17c7cba57`  |
| 3335   | Layout 1             | `adc17c7cba57`  |
| 3326   | Layout 1             | `adc17c7cba57`  |
| 3321   | Layout 1             | `adc17c7cba57`  |
| 3314   | Layout 1             | `adc17c7cba57`  |
| 3303   | Layout 1             | `adc17c7cba57`  |
| 3302   | Layout 1             | `adc17c7cba57`  |
| 3293   | Layout 1             | `adc17c7cba57`  |
| 3283   | Layout 1             | `adc17c7cba57`  |
| 3275   | Layout 1             | `adc17c7cba57`  |
| 3267   | Layout 1             | `adc17c7cba57`  |
| 3258   | Layout 1             | `adc17c7cba57`  |
| 3251   | Layout 1             | `adc17c7cba57`  |
| 3242   | Layout 1             | `adc17c7cba57`  |
| 3235   | Layout 1             | `adc17c7cba57`  |
| 3229   | Layout 1             | `adc17c7cba57`  |
| 3212   | Layout 1             | `adc17c7cba57`  |
| 3203   | Layout 1             | `adc17c7cba57`  |
| 3193   | Layout 1             | `adc17c7cba57`  |
| 3186   | Layout 1             | `adc17c7cba57`  |
| 3177   | Layout 1             | `adc17c7cba57`  |
| 3169   | Layout 1             | `adc17c7cba57`  |
| 3158   | Layout 1             | `adc17c7cba57`  |
| 3151   | Layout 1             | `adc17c7cba57`  |
| 3144   | Layout 1             | `adc17c7cba57`  |
| 3133   | Layout 1             | `adc17c7cba57`  |
| 3125   | Layout 1             | `adc17c7cba57`  |
| 3118   | Layout 1             | `adc17c7cba57`  |
| 3111   | Layout 1             | `adc17c7cba57`  |
| 3103   | Layout 1             | `adc17c7cba57`  |
| 3095   | Layout 1             | `adc17c7cba57`  |
| 3086   | Layout 1             | `adc17c7cba57`  |
| 3072   | Layout 1             | `adc17c7cba57`  |
| 3062   | Layout 1             | `adc17c7cba57`  |
| 3052   | Layout 1             | `adc17c7cba57`  |
| 3045   | Layout 1             | `adc17c7cba57`  |
| 3037   | Layout 1             | `adc17c7cba57`  |
| 3030   | Layout 1             | `adc17c7cba57`  |
| 3021   | Layout 1             | `adc17c7cba57`  |
| 3012   | Layout 1             | `adc17c7cba57`  |
| 3002   | Layout 1             | `adc17c7cba57`  |
| 2995   | Layout 1             | `adc17c7cba57`  |
| 2987   | Layout 1             | `adc17c7cba57`  |
| 2978   | Layout 1             | `adc17c7cba57`  |
| 2970   | Layout 1             | `adc17c7cba57`  |
| 2959   | Layout 1             | `adc17c7cba57`  |
| 2951   | Layout 1             | `adc17c7cba57`  |
| 2942   | Layout 1             | `adc17c7cba57`  |
| 2935   | Layout 1             | `adc17c7cba57`  |
| 2932   | Layout 1             | `adc17c7cba57`  |
| 2923   | Layout 1             | `adc17c7cba57`  |
| 2919   | Layout 1             | `adc17c7cba57`  |
| 2907   | Layout 1             | `adc17c7cba57`  |
| 2900   | Layout 1             | `adc17c7cba57`  |
| 2891   | Layout 1             | `adc17c7cba57`  |
| 2882   | Layout 1             | `adc17c7cba57`  |
| 2872   | Layout 1             | `adc17c7cba57`  |
| 2863   | Layout 1             | `adc17c7cba57`  |
| 2855   | Layout 1             | `adc17c7cba57`  |
| 2849   | Layout 1             | `adc17c7cba57`  |
| 2844   | Layout 1             | `adc17c7cba57`  |
| 2834   | Layout 1             | `adc17c7cba57`  |
| 2825   | Layout 1             | `adc17c7cba57`  |
| 2819   | Layout 1             | `adc17c7cba57`  |
| 2811   | Layout 1             | `adc17c7cba57`  |
| 2803   | Layout 1             | `adc17c7cba57`  |
| 2794   | Layout 1             | `adc17c7cba57`  |
| 2783   | Layout 1             | `adc17c7cba57`  |
| 2774   | Layout 1             | `adc17c7cba57`  |
| 2765   | Layout 1             | `adc17c7cba57`  |
| 2756   | Layout 1             | `adc17c7cba57`  |
| 2750   | Layout 1             | `adc17c7cba57`  |
| 2743   | Layout 1             | `adc17c7cba57`  |
| 2736   | Layout 1             | `adc17c7cba57`  |
| 2726   | Layout 1             | `adc17c7cba57`  |
| 2717   | Layout 1             | `adc17c7cba57`  |
| 2709   | Layout 1             | `adc17c7cba57`  |
| 2703   | Layout 1             | `adc17c7cba57`  |
| 2695   | Layout 1             | `adc17c7cba57`  |
| 2684   | Layout 1             | `adc17c7cba57`  |
| 2672   | Layout 1             | `adc17c7cba57`  |
| 2665   | Layout 1             | `adc17c7cba57`  |
| 2657   | Layout 1             | `adc17c7cba57`  |
| 2649   | Layout 1             | `adc17c7cba57`  |
| 2644   | Layout 1             | `adc17c7cba57`  |
| 2637   | Layout 1             | `adc17c7cba57`  |
| 2629   | Layout 1             | `adc17c7cba57`  |
| 2619   | Layout 1             | `adc17c7cba57`  |
| 2612   | Layout 1             | `adc17c7cba57`  |
| 2606   | Layout 1             | `adc17c7cba57`  |
| 2602   | Layout 1             | `adc17c7cba57`  |
| 2601   | Layout 1             | `adc17c7cba57`  |
| 2592   | Layout 1             | `adc17c7cba57`  |
| 2583   | Layout 1             | `adc17c7cba57`  |
| 2575   | Layout 1             | `adc17c7cba57`  |
| 2567   | Layout 1             | `adc17c7cba57`  |
| 2560   | Layout 1             | `adc17c7cba57`  |
| 2553   | Layout 1             | `adc17c7cba57`  |
| 2545   | Layout 1             | `adc17c7cba57`  |
| 2538   | Layout 1             | `adc17c7cba57`  |
| 2529   | Layout 1             | `adc17c7cba57`  |
| 2519   | Layout 1             | `adc17c7cba57`  |
| 2513   | Layout 1             | `adc17c7cba57`  |
| 2510   | Layout 1             | `adc17c7cba57`  |
| 2507   | Layout 1             | `adc17c7cba57`  |
| 2503   | Layout 1             | `adc17c7cba57`  |
| 2498   | Layout 1             | `adc17c7cba57`  |
| 2492   | Layout 1             | `adc17c7cba57`  |
| 2487   | Layout 1             | `adc17c7cba57`  |
| 2480   | Layout 1             | `adc17c7cba57`  |
| 2474   | Layout 1             | `adc17c7cba57`  |
| 2468   | Layout 1             | `adc17c7cba57`  |
| 2460   | Layout 1             | `adc17c7cba57`  |
| 2453   | Layout 1             | `adc17c7cba57`  |
| 2444   | Layout 1             | `adc17c7cba57`  |
| 2438   | Layout 1             | `adc17c7cba57`  |
| 2434   | Layout 1             | `adc17c7cba57`  |
| 2429   | Layout 1             | `adc17c7cba57`  |
| 2421   | Layout 1             | `adc17c7cba57`  |
| 2414   | Layout 1             | `adc17c7cba57`  |
| 2407   | Layout 1             | `adc17c7cba57`  |
| 2401   | Layout 1             | `adc17c7cba57`  |
| 2397   | Layout 1             | `adc17c7cba57`  |
| 2393   | Layout 1             | `adc17c7cba57`  |
| 2384   | Layout 1             | `adc17c7cba57`  |
| 2378   | Layout 1             | `adc17c7cba57`  |
| 2372   | Layout 1             | `adc17c7cba57`  |
| 2358   | Layout 1             | `adc17c7cba57`  |
| 2352   | Layout 1             | `adc17c7cba57`  |
| 2347   | Layout 1             | `adc17c7cba57`  |
| 2343   | Layout 1             | `adc17c7cba57`  |
| 2335   | Layout 1             | `adc17c7cba57`  |
| 2327   | Layout 1             | `adc17c7cba57`  |
| 2324   | Layout 1             | `adc17c7cba57`  |
| 2319   | Layout 1             | `adc17c7cba57`  |
| 2313   | Layout 1             | `adc17c7cba57`  |
| 2308   | Layout 1             | `adc17c7cba57`  |
| 2302   | Layout 1             | `adc17c7cba57`  |
| 2295   | Layout 1             | `adc17c7cba57`  |
| 2290   | Layout 1             | `adc17c7cba57`  |
| 2284   | Layout 1             | `adc17c7cba57`  |
| 2276   | Layout 1             | `adc17c7cba57`  |
| 2269   | Layout 1             | `adc17c7cba57`  |
| 2259   | Layout 1             | `adc17c7cba57`  |
| 2250   | Layout 1             | `adc17c7cba57`  |
| 2243   | Layout 1             | `adc17c7cba57`  |
| 2235   | Layout 1             | `adc17c7cba57`  |
| 2229   | Layout 1             | `adc17c7cba57`  |
| 2224   | Layout 1             | `adc17c7cba57`  |
| 2218   | Layout 1             | `adc17c7cba57`  |
| 2215   | Layout 1             | `adc17c7cba57`  |
| 2207   | Layout 1             | `adc17c7cba57`  |
| 2203   | Layout 1             | `adc17c7cba57`  |
| 2196   | Layout 1             | `adc17c7cba57`  |
| 2192   | Layout 1             | `adc17c7cba57`  |
| 2189   | Layout 1             | `adc17c7cba57`  |
| 2183   | Layout 1             | `adc17c7cba57`  |
| 2179   | Layout 1             | `adc17c7cba57`  |
| 2171   | Layout 1             | `adc17c7cba57`  |
| 2163   | Layout 1             | `adc17c7cba57`  |
| 2156   | Layout 1             | `adc17c7cba57`  |
| 2151   | Layout 1             | `adc17c7cba57`  |
| 2147   | Layout 1             | `adc17c7cba57`  |
| 2142   | Layout 1             | `adc17c7cba57`  |
| 2138   | Layout 1             | `adc17c7cba57`  |
| 2134   | Layout 1             | `adc17c7cba57`  |
| 2130   | Layout 1             | `adc17c7cba57`  |
| 2122   | Layout 1             | `adc17c7cba57`  |
| 2107   | Layout 1             | `adc17c7cba57`  |
| 2098   | Layout 1             | `adc17c7cba57`  |
| 2089   | Layout 1             | `adc17c7cba57`  |
| 2081   | Layout 1             | `adc17c7cba57`  |
| 2073   | Layout 1             | `adc17c7cba57`  |
| 2067   | Layout 1             | `adc17c7cba57`  |
| 2063   | Layout 1             | `adc17c7cba57`  |
| 2059   | Layout 1             | `adc17c7cba57`  |
| 2052   | Layout 1             | `adc17c7cba57`  |
| 2044   | Layout 1             | `adc17c7cba57`  |
| 2039   | Layout 1             | `adc17c7cba57`  |
| 2032   | Layout 1             | `adc17c7cba57`  |
| 2025   | Layout 1             | `adc17c7cba57`  |
| 2011   | Layout 1             | `adc17c7cba57`  |
| 2005   | Layout 1             | `adc17c7cba57`  |
| 2000   | Layout 1             | `adc17c7cba57`  |
| 1996   | Layout 1             | `adc17c7cba57`  |
| 1991   | Layout 1             | `adc17c7cba57`  |
| 1985   | Layout 1             | `adc17c7cba57`  |
| 1980   | Layout 1             | `adc17c7cba57`  |
| 1969   | Layout 1             | `adc17c7cba57`  |
| 1964   | Layout 1             | `adc17c7cba57`  |
| 1958   | Layout 1             | `adc17c7cba57`  |
| 1950   | Layout 1             | `adc17c7cba57`  |
| 1945   | Layout 1             | `adc17c7cba57`  |
| 1937   | Layout 1             | `adc17c7cba57`  |
| 1933   | Layout 1             | `adc17c7cba57`  |
| 1927   | Layout 1             | `adc17c7cba57`  |
| 1921   | Layout 1             | `adc17c7cba57`  |
| 1914   | Layout 1             | `adc17c7cba57`  |
| 1908   | Layout 1             | `adc17c7cba57`  |
| 1897   | Layout 1             | `adc17c7cba57`  |
| 1892   | Layout 1             | `adc17c7cba57`  |
| 1886   | Layout 1             | `adc17c7cba57`  |
| 1881   | Layout 1             | `adc17c7cba57`  |
| 1871   | Layout 1             | `adc17c7cba57`  |
| 1866   | Layout 1             | `adc17c7cba57`  |
| 1862   | Layout 1             | `adc17c7cba57`  |
| 1854   | Layout 1             | `adc17c7cba57`  |
| 1846   | Layout 1             | `adc17c7cba57`  |
| 1838   | Layout 1             | `adc17c7cba57`  |
| 1832   | Layout 1             | `adc17c7cba57`  |
| 1826   | Layout 1             | `adc17c7cba57`  |
| 1822   | Layout 1             | `adc17c7cba57`  |
| 1818   | Layout 1             | `adc17c7cba57`  |
| 1804   | Layout 1             | `adc17c7cba57`  |
| 1794   | Layout 1             | `adc17c7cba57`  |
| 1790   | Layout 1             | `adc17c7cba57`  |
| 1784   | Layout 1             | `adc17c7cba57`  |
| 1774   | Layout 1             | `adc17c7cba57`  |
| 1771   | Layout 1             | `adc17c7cba57`  |
| 1762   | Layout 1             | `adc17c7cba57`  |
| 1759   | Layout 1             | `adc17c7cba57`  |
| 1754   | Layout 1             | `adc17c7cba57`  |
| 1749   | Layout 1             | `adc17c7cba57`  |
| 1743   | Layout 1             | `adc17c7cba57`  |
| 1737   | Layout 1             | `adc17c7cba57`  |
| 1731   | Layout 1             | `adc17c7cba57`  |
| 1725   | Layout 1             | `adc17c7cba57`  |
| 1717   | Layout 1             | `adc17c7cba57`  |
| 1710   | Layout 1             | `adc17c7cba57`  |
| 1704   | Layout 1             | `adc17c7cba57`  |
| 1698   | Layout 1             | `adc17c7cba57`  |
| 1690   | Layout 1             | `adc17c7cba57`  |
| 1685   | Layout 1             | `adc17c7cba57`  |
| 1680   | Layout 1             | `adc17c7cba57`  |
| 1674   | Layout 1             | `adc17c7cba57`  |
| 1668   | Layout 1             | `adc17c7cba57`  |
| 1659   | Layout 1             | `adc17c7cba57`  |
| 1649   | Layout 1             | `adc17c7cba57`  |
| 1642   | Layout 1             | `adc17c7cba57`  |
| 1636   | Layout 1             | `adc17c7cba57`  |
| 1628   | Layout 1             | `adc17c7cba57`  |
| 1622   | Layout 1             | `adc17c7cba57`  |
| 1614   | Layout 1             | `adc17c7cba57`  |
| 1608   | Layout 1             | `adc17c7cba57`  |
| 1602   | Layout 1             | `adc17c7cba57`  |
| 1598   | Layout 1             | `adc17c7cba57`  |
| 1594   | Layout 1             | `adc17c7cba57`  |
| 1590   | Layout 1             | `adc17c7cba57`  |
| 1587   | Layout 1             | `adc17c7cba57`  |
| 1584   | Layout 1             | `adc17c7cba57`  |
| 1579   | Layout 1             | `adc17c7cba57`  |
| 1572   | Layout 1             | `adc17c7cba57`  |
| 1565   | Layout 1             | `adc17c7cba57`  |
| 1559   | Layout 1             | `adc17c7cba57`  |
| 1554   | Layout 1             | `adc17c7cba57`  |
| 1547   | Layout 1             | `adc17c7cba57`  |
| 1537   | Layout 1             | `adc17c7cba57`  |
| 1529   | Layout 1             | `adc17c7cba57`  |
| 1524   | Layout 1             | `adc17c7cba57`  |
| 1519   | Layout 1             | `adc17c7cba57`  |
| 1509   | Layout 1             | `adc17c7cba57`  |
| 1506   | Layout 1             | `adc17c7cba57`  |
| 1504   | Layout 1             | `adc17c7cba57`  |
| 1500   | Layout 1             | `adc17c7cba57`  |
| 1493   | Layout 1             | `adc17c7cba57`  |
| 1489   | Layout 1             | `adc17c7cba57`  |
| 1485   | Layout 1             | `adc17c7cba57`  |
| 1481   | Layout 1             | `adc17c7cba57`  |
| 1474   | Layout 1             | `adc17c7cba57`  |
| 1466   | Layout 1             | `adc17c7cba57`  |
| 1462   | Layout 1             | `adc17c7cba57`  |
| 1459   | Layout 1             | `adc17c7cba57`  |
| 1453   | Layout 1             | `adc17c7cba57`  |
| 1450   | Layout 1             | `adc17c7cba57`  |
| 1445   | Layout 1             | `adc17c7cba57`  |
| 1439   | Layout 1             | `adc17c7cba57`  |
| 1433   | Layout 1             | `adc17c7cba57`  |
| 1430   | Layout 1             | `adc17c7cba57`  |
| 1426   | Layout 1             | `adc17c7cba57`  |
| 1421   | Layout 1             | `adc17c7cba57`  |
| 1417   | Layout 1             | `adc17c7cba57`  |
| 1416   | Layout 1             | `adc17c7cba57`  |
| 1409   | Layout 1             | `adc17c7cba57`  |
| 1405   | Layout 1             | `adc17c7cba57`  |
| 1401   | Layout 1             | `adc17c7cba57`  |
| 1396   | Layout 1             | `adc17c7cba57`  |
| 1391   | Layout 1             | `adc17c7cba57`  |
| 1390   | Layout 1             | `adc17c7cba57`  |
| 1386   | Layout 1             | `adc17c7cba57`  |
| 1381   | Layout 1             | `adc17c7cba57`  |
| 1379   | Layout 1             | `adc17c7cba57`  |
| 1372   | Layout 1             | `adc17c7cba57`  |
| 1366   | Layout 1             | `adc17c7cba57`  |
| 1364   | Layout 1             | `adc17c7cba57`  |
| 1363   | Layout 1             | `adc17c7cba57`  |
| 1360   | Layout 1             | `adc17c7cba57`  |
| 1358   | Layout 1             | `adc17c7cba57`  |
| 1355   | Layout 1             | `adc17c7cba57`  |
| 1351   | Layout 1             | `adc17c7cba57`  |
| 1348   | Layout 1             | `adc17c7cba57`  |
| 1346   | Layout 1             | `adc17c7cba57`  |
| 1341   | No documented layout | `adc17c7cba57`  |
| 1340   | No documented layout | `adc17c7cba57`  |
| 1338   | No documented layout | `adc17c7cba57`  |
| 1335   | No documented layout | `adc17c7cba57`  |
| 1333   | No documented layout | `adc17c7cba57`  |
| 1329   | No documented layout | `adc17c7cba57`  |
| 1327   | No documented layout | `adc17c7cba57`  |
| 1324   | No documented layout | `adc17c7cba57`  |
| 1321   | No documented layout | `adc17c7cba57`  |
| 1319   | No documented layout | `adc17c7cba57`  |
| 1318   | No documented layout | `adc17c7cba57`  |
| 1316   | No documented layout | `adc17c7cba57`  |
| 1313   | No documented layout | `adc17c7cba57`  |
| 1311   | No documented layout | `adc17c7cba57`  |
| 1309   | No documented layout | `adc17c7cba57`  |
| 1304   | No documented layout | `adc17c7cba57`  |
| 1292   | No documented layout | `adc17c7cba57`  |
| 1286   | No documented layout | `adc17c7cba57`  |
| 1280   | No documented layout | `adc17c7cba57`  |
| 1276   | No documented layout | `adc17c7cba57`  |
| 1267   | No file              | `adc17c7cba57`  |
| 1261   | No file              | `adc17c7cba57`  |
| 1256   | No documented layout | `adc17c7cba57`  |
| 1250   | No file              | `adc17c7cba57`  |
| 1246   | No file              | `adc17c7cba57`  |
| 1239   | No file              | `adc17c7cba57`  |
| 1230   | No file              | `adc17c7cba57`  |
| 1226   | No file              | `adc17c7cba57`  |
| 1220   | No file              | `adc17c7cba57`  |
| 1217   | No file              | `adc17c7cba57`  |
| 1211   | No file              | `adc17c7cba57`  |
| 1210   | No file              | `adc17c7cba57`  |
| 1208   | No file              | `adc17c7cba57`  |
| 1203   | No file              | `adc17c7cba57`  |
| 1197   | No file              | `adc17c7cba57`  |
| 1194   | No file              | `adc17c7cba57`  |
| 1192   | No file              | `adc17c7cba57`  |
| 1187   | No file              | `adc17c7cba57`  |
| 1183   | No file              | `adc17c7cba57`  |
| 1177   | No file              | `adc17c7cba57`  |
| 1173   | No file              | `adc17c7cba57`  |
| 1167   | No file              | `adc17c7cba57`  |
| 1164   | No file              | `adc17c7cba57`  |
| 1156   | No file              | `adc17c7cba57`  |
| 1149   | No file              | `adc17c7cba57`  |
| 1144   | No file              | `adc17c7cba57`  |
| 1137   | No file              | `adc17c7cba57`  |
| 1132   | No file              | `adc17c7cba57`  |
| 1127   | No file              | `adc17c7cba57`  |
| 1122   | No file              | `adc17c7cba57`  |
| 1118   | No file              | `adc17c7cba57`  |
| 1114   | No file              | `adc17c7cba57`  |
| 1109   | No file              | `adc17c7cba57`  |
| 1102   | No file              | `adc17c7cba57`  |
| 1096   | No file              | `adc17c7cba57`  |
| 1088   | No file              | `adc17c7cba57`  |
| 1081   | No file              | `adc17c7cba57`  |
| 1076   | No file              | `adc17c7cba57`  |
| 1069   | No file              | `adc17c7cba57`  |
| 1064   | No file              | `adc17c7cba57`  |
| 1058   | No file              | `adc17c7cba57`  |
| 1051   | No file              | `adc17c7cba57`  |
| 1044   | No file              | `adc17c7cba57`  |
| 1036   | No file              | `adc17c7cba57`  |
| 1026   | No file              | `adc17c7cba57`  |
| 1016   | No file              | `adc17c7cba57`  |
| 1009   | No file              | `adc17c7cba57`  |
| 1005   | No file              | `adc17c7cba57`  |
| 1000   | No file              | `adc17c7cba57`  |
| 998    | No file              | `adc17c7cba57`  |
| 990    | No file              | `adc17c7cba57`  |
| 979    | No file              | `adc17c7cba57`  |
| 972    | No file              | `adc17c7cba57`  |
| 963    | No file              | `adc17c7cba57`  |
| 955    | No file              | `adc17c7cba57`  |
| 946    | No file              | `adc17c7cba57`  |
| 938    | No file              | `adc17c7cba57`  |
| 927    | No file              | `adc17c7cba57`  |
| 911    | No file              | `adc17c7cba57`  |
| 904    | No file              | `adc17c7cba57`  |
| 899    | No file              | `adc17c7cba57`  |
| 894    | No file              | `adc17c7cba57`  |
| 885    | No file              | `adc17c7cba57`  |
| 879    | No file              | `adc17c7cba57`  |
| 872    | No file              | `adc17c7cba57`  |
| 864    | No file              | `adc17c7cba57`  |
| 855    | No file              | `adc17c7cba57`  |
| 853    | No file              | `adc17c7cba57`  |
| 845    | No file              | `adc17c7cba57`  |
| 837    | No file              | `adc17c7cba57`  |
| 829    | No file              | `adc17c7cba57`  |
| 822    | No file              | `adc17c7cba57`  |
| 814    | No file              | `adc17c7cba57`  |
| 805    | No file              | `adc17c7cba57`  |
| 794    | No file              | `adc17c7cba57`  |
| 787    | No file              | `adc17c7cba57`  |
| 780    | No file              | `adc17c7cba57`  |
| 771    | No file              | `adc17c7cba57`  |
| 760    | No file              | `adc17c7cba57`  |
| 748    | No file              | `adc17c7cba57`  |
| 741    | No file              | `adc17c7cba57`  |
| 736    | No file              | `adc17c7cba57`  |
| 731    | No file              | `adc17c7cba57`  |
| 723    | No file              | `adc17c7cba57`  |
| 711    | No file              | `adc17c7cba57`  |
| 707    | No file              | `adc17c7cba57`  |
| 697    | No file              | `adc17c7cba57`  |
| 689    | No file              | `adc17c7cba57`  |
| 683    | No file              | `adc17c7cba57`  |
| 678    | No file              | `adc17c7cba57`  |
| 670    | No file              | `adc17c7cba57`  |
| 661    | No file              | `adc17c7cba57`  |
| 656    | No file              | `adc17c7cba57`  |
| 652    | No file              | `adc17c7cba57`  |
| 643    | No file              | `adc17c7cba57`  |
| 637    | No file              | `adc17c7cba57`  |
| 630    | No file              | `adc17c7cba57`  |
| 627    | No file              | `adc17c7cba57`  |
| 621    | No file              | `adc17c7cba57`  |
| 617    | No file              | `adc17c7cba57`  |
| 615    | No file              | `adc17c7cba57`  |
| 606    | No file              | `adc17c7cba57`  |
| 599    | No file              | `adc17c7cba57`  |
| 592    | No file              | `adc17c7cba57`  |
| 586    | No file              | `adc17c7cba57`  |
| 577    | No file              | `adc17c7cba57`  |
| 569    | No file              | `adc17c7cba57`  |
| 561    | No file              | `adc17c7cba57`  |
| 554    | No file              | `adc17c7cba57`  |
| 542    | No file              | `adc17c7cba57`  |
| 532    | No file              | `adc17c7cba57`  |
| 531    | No file              | `adc17c7cba57`  |
| 526    | No file              | `adc17c7cba57`  |
| 521    | No file              | `adc17c7cba57`  |
| 517    | No file              | `adc17c7cba57`  |
| 510    | No file              | `adc17c7cba57`  |
| 508    | No file              | `adc17c7cba57`  |
| 504    | No file              | `adc17c7cba57`  |
| 497    | No file              | `adc17c7cba57`  |
| 491    | No file              | `adc17c7cba57`  |
| 485    | No file              | `adc17c7cba57`  |
| 478    | No file              | `adc17c7cba57`  |
| 472    | No file              | `adc17c7cba57`  |
| 466    | No file              | `adc17c7cba57`  |
| 457    | No file              | `adc17c7cba57`  |
| 452    | No file              | `adc17c7cba57`  |
| 449    | No file              | `adc17c7cba57`  |
| 435    | No file              | `adc17c7cba57`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                    |
| ----------------------------- | -------- | ------------------------------------------------------- |
| `servantupgradeoffset.dbss`   | Optional | Index: per ship, per target ship, the upgrade's offset and size |
| `languagedata_en.loc`         | Optional | Ship names (LOC type 6) and item names (LOC type 0)     |
| `characterstaticoffset.dbss`  | Optional | Every `characterstatic.dbss` key, so a ship ID without a row shows as plain text instead of a link |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                | Field       | Notes                                          |
| ------- | ------------------- | ----------- | ---------------------------------------------- |
| `+0x00` | u32                 | group_count | Ships with upgrades: 8 on client 3474          |
| `+0x04` | Group[group_count]  | groups      | Back to back, up to EOF                        |

### Group (variable: 4 bytes + upgrades)

| Offset  | Type                   | Field         | Notes                                        |
| ------- | ---------------------- | ------------- | -------------------------------------------- |
| `+0x00` | u32                    | upgrade_count | 1 or 2                                       |
| `+0x04` | Upgrade[upgrade_count] | upgrades      | Every upgrade of a group has the same `character_id` |

### Upgrade (172 bytes)

| Offset  | Type      | Field                | Notes                                         |
| ------- | --------- | -------------------- | --------------------------------------------- |
| `+0x00` | u16       | character_id         | The ship before the upgrade (`servant.bss`)   |
| `+0x02` | u16       | upgrade_character_id | The ship after it                             |
| `+0x04` | Item[4]   | main_items           | The four gear pieces, such as `Bartali Sailboat: Old Figurehead` +10 |
| `+0x34` | Item[10]  | sub_items            | Materials; unused slots are all zero          |

### Item (12 bytes)

| Offset  | Type | Field    | Notes                                                          |
| ------- | ---- | -------- | -------------------------------------------------------------- |
| `+0x00` | u32  | item_key | `(enchant_level << 24) \| item_id`, the [itemenchant.dbss](itemenchant_dbss.md#key-packing) key |
| `+0x04` | u64  | count    | 1 on every main item                                           |

### `servantupgradeoffset.dbss`

| Offset  | Type                            | Field        | Notes                          |
| ------- | ------------------------------- | ------------ | ------------------------------ |
| `+0x00` | u32                             | group_count  | Equals the main file's count   |
| `+0x04` | Offset Group[group_count]       | groups       | Not in main file order         |

### Offset Group (variable: 6 bytes + entries)

| Offset  | Type                       | Field         | Notes                     |
| ------- | -------------------------- | ------------- | ------------------------- |
| `+0x00` | u16                        | character_id  | The group's ship          |
| `+0x02` | u32                        | upgrade_count | The group's upgrade count |
| `+0x06` | Offset Row[upgrade_count]  | entries       |                           |

### Offset Row (10 bytes)

| Offset  | Type | Field                | Notes                                            |
| ------- | ---- | -------------------- | ------------------------------------------------ |
| `+0x00` | u16  | upgrade_character_id | The upgrade's target ship                        |
| `+0x02` | u32  | offset               | Start of the upgrade in `servantupgrade.dbss`    |
| `+0x06` | u32  | size                 | 172 on every entry                               |

## Field Names

The names follow the `OceanShipUpgrade_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched value by value over the 12
upgrades it shares with clients 1784 and 3474:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `CharacterKeyShip`, `UpgradeCharacterKeyShip` | `character_id`, `upgrade_character_id` | 12 of 12 | 12 of 12 |
| `UpgradeMainItemKey_0` to `_3` | `main_items[0..3].item_key` low 24 bits | 12 | 12 |
| `MainItemEnchant_0` to `_3` | `main_items[0..3].item_key` high byte | 12 | 12 |
| `UpgradeSubItemKey_0` to `_9` | `sub_items[0..9].item_key` | 12 | 10 |
| `SubItemCount_0` to `_9` | `sub_items[0..9].count` | 12 | 6 |

The sheet has no count column for the main items. The client 3474 misses
are later changes: Bartali Sailboat (31053) to Epheria Sailboat and to
Epheria Frigate take fewer materials and 5 `Gold Bar 1,000G` (item 5) in
place of 100 `Hard Pillar` (4687), and the four upgrades to Epheria
Caravel (31048) and Epheria Galleass (31049) take 4 or 3 of one material
where client 1784 has 6. Client 3474
adds Galley (9090) to Improved Galley (9124).

## Notes

- Client 1784 has the same layout with 7 groups and 12 upgrades.
- `servantupgradeoffset.dbss` lists the groups in another order than the
  main file; on client 3474 its last entry, Galley to Improved Galley, points
  at offset 1,924, the main file's 12th upgrade.
