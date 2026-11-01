# `instancefieldrankingmanage.bss` Format

## Purpose

The season rankings of instance contents: per ranking key the instance
type, the time the ranking starts and ends and the `GAME` sheet key of the
season name. On client 3482 all 14 rows are instance type `11`, the Old
Moon Grand Prix: ranking `1` and `2` are the test seasons of 2021-02 and
`3` to `14` the season 1 rankings of the services, which end in 2099.
[`instancefieldranking.bss`](instancefieldranking_bss.md) picks the
rankings each instance field type shows. The file is the
`InstanceRankingManage` sheet compiled into a PABR table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes | Records | Row bytes |
| ------ | -------------- | -------------------------------- | ----- | ------- | --------- |
| 1      | 1506 and later | `instancefieldrankingmanage.bss` | 454   | 14 Row  | 26        |

| Layout | File                             | Known          | Unknown    |
| ------ | -------------------------------- | -------------- | ---------- |
| 1      | `instancefieldrankingmanage.bss` | 454 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `3b99adb6402d`  |
| 3482   | Layout 1 | `3b99adb6402d`  |
| 3474   | Layout 1 | `3b99adb6402d`  |
| 3473   | Layout 1 | `3b99adb6402d`  |
| 3464   | Layout 1 | `3b99adb6402d`  |
| 3458   | Layout 1 | `3b99adb6402d`  |
| 3454   | Layout 1 | `3b99adb6402d`  |
| 3444   | Layout 1 | `3b99adb6402d`  |
| 3435   | Layout 1 | `3b99adb6402d`  |
| 3426   | Layout 1 | `3b99adb6402d`  |
| 3418   | Layout 1 | `3b99adb6402d`  |
| 3412   | Layout 1 | `3b99adb6402d`  |
| 3402   | Layout 1 | `3b99adb6402d`  |
| 3396   | Layout 1 | `3b99adb6402d`  |
| 3387   | Layout 1 | `3b99adb6402d`  |
| 3381   | Layout 1 | `3b99adb6402d`  |
| 3373   | Layout 1 | `3b99adb6402d`  |
| 3364   | Layout 1 | `3b99adb6402d`  |
| 3356   | Layout 1 | `3b99adb6402d`  |
| 3349   | Layout 1 | `3b99adb6402d`  |
| 3342   | Layout 1 | `3b99adb6402d`  |
| 3335   | Layout 1 | `3b99adb6402d`  |
| 3326   | Layout 1 | `3b99adb6402d`  |
| 3321   | Layout 1 | `3b99adb6402d`  |
| 3314   | Layout 1 | `3b99adb6402d`  |
| 3303   | Layout 1 | `3b99adb6402d`  |
| 3302   | Layout 1 | `3b99adb6402d`  |
| 3293   | Layout 1 | `3b99adb6402d`  |
| 3283   | Layout 1 | `3b99adb6402d`  |
| 3275   | Layout 1 | `3b99adb6402d`  |
| 3267   | Layout 1 | `3b99adb6402d`  |
| 3258   | Layout 1 | `3b99adb6402d`  |
| 3251   | Layout 1 | `3b99adb6402d`  |
| 3242   | Layout 1 | `3b99adb6402d`  |
| 3235   | Layout 1 | `3b99adb6402d`  |
| 3229   | Layout 1 | `3b99adb6402d`  |
| 3212   | Layout 1 | `3b99adb6402d`  |
| 3203   | Layout 1 | `3b99adb6402d`  |
| 3193   | Layout 1 | `3b99adb6402d`  |
| 3186   | Layout 1 | `3b99adb6402d`  |
| 3177   | Layout 1 | `3b99adb6402d`  |
| 3169   | Layout 1 | `3b99adb6402d`  |
| 3158   | Layout 1 | `3b99adb6402d`  |
| 3151   | Layout 1 | `3b99adb6402d`  |
| 3144   | Layout 1 | `3b99adb6402d`  |
| 3133   | Layout 1 | `3b99adb6402d`  |
| 3125   | Layout 1 | `3b99adb6402d`  |
| 3118   | Layout 1 | `3b99adb6402d`  |
| 3111   | Layout 1 | `3b99adb6402d`  |
| 3103   | Layout 1 | `3b99adb6402d`  |
| 3095   | Layout 1 | `3b99adb6402d`  |
| 3086   | Layout 1 | `3b99adb6402d`  |
| 3072   | Layout 1 | `3b99adb6402d`  |
| 3062   | Layout 1 | `3b99adb6402d`  |
| 3052   | Layout 1 | `3b99adb6402d`  |
| 3045   | Layout 1 | `3b99adb6402d`  |
| 3037   | Layout 1 | `3b99adb6402d`  |
| 3030   | Layout 1 | `3b99adb6402d`  |
| 3021   | Layout 1 | `3b99adb6402d`  |
| 3012   | Layout 1 | `3b99adb6402d`  |
| 3002   | Layout 1 | `3b99adb6402d`  |
| 2995   | Layout 1 | `3b99adb6402d`  |
| 2987   | Layout 1 | `3b99adb6402d`  |
| 2978   | Layout 1 | `3b99adb6402d`  |
| 2970   | Layout 1 | `3b99adb6402d`  |
| 2959   | Layout 1 | `3b99adb6402d`  |
| 2951   | Layout 1 | `3b99adb6402d`  |
| 2942   | Layout 1 | `3b99adb6402d`  |
| 2935   | Layout 1 | `3b99adb6402d`  |
| 2932   | Layout 1 | `3b99adb6402d`  |
| 2923   | Layout 1 | `3b99adb6402d`  |
| 2919   | Layout 1 | `3b99adb6402d`  |
| 2907   | Layout 1 | `3b99adb6402d`  |
| 2900   | Layout 1 | `3b99adb6402d`  |
| 2891   | Layout 1 | `3b99adb6402d`  |
| 2882   | Layout 1 | `3b99adb6402d`  |
| 2872   | Layout 1 | `3b99adb6402d`  |
| 2863   | Layout 1 | `3b99adb6402d`  |
| 2855   | Layout 1 | `3b99adb6402d`  |
| 2849   | Layout 1 | `3b99adb6402d`  |
| 2844   | Layout 1 | `3b99adb6402d`  |
| 2834   | Layout 1 | `3b99adb6402d`  |
| 2825   | Layout 1 | `3b99adb6402d`  |
| 2819   | Layout 1 | `3b99adb6402d`  |
| 2811   | Layout 1 | `3b99adb6402d`  |
| 2803   | Layout 1 | `3b99adb6402d`  |
| 2794   | Layout 1 | `3b99adb6402d`  |
| 2783   | Layout 1 | `3b99adb6402d`  |
| 2774   | Layout 1 | `3b99adb6402d`  |
| 2765   | Layout 1 | `3b99adb6402d`  |
| 2756   | Layout 1 | `3b99adb6402d`  |
| 2750   | Layout 1 | `3b99adb6402d`  |
| 2743   | Layout 1 | `3b99adb6402d`  |
| 2736   | Layout 1 | `3b99adb6402d`  |
| 2726   | Layout 1 | `3b99adb6402d`  |
| 2717   | Layout 1 | `3b99adb6402d`  |
| 2709   | Layout 1 | `3b99adb6402d`  |
| 2703   | Layout 1 | `3b99adb6402d`  |
| 2695   | Layout 1 | `3b99adb6402d`  |
| 2684   | Layout 1 | `3b99adb6402d`  |
| 2672   | Layout 1 | `3b99adb6402d`  |
| 2665   | Layout 1 | `3b99adb6402d`  |
| 2657   | Layout 1 | `3b99adb6402d`  |
| 2649   | Layout 1 | `3b99adb6402d`  |
| 2644   | Layout 1 | `3b99adb6402d`  |
| 2637   | Layout 1 | `3b99adb6402d`  |
| 2629   | Layout 1 | `3b99adb6402d`  |
| 2619   | Layout 1 | `3b99adb6402d`  |
| 2612   | Layout 1 | `3b99adb6402d`  |
| 2606   | Layout 1 | `3b99adb6402d`  |
| 2602   | Layout 1 | `3b99adb6402d`  |
| 2601   | Layout 1 | `3b99adb6402d`  |
| 2592   | Layout 1 | `3b99adb6402d`  |
| 2583   | Layout 1 | `3b99adb6402d`  |
| 2575   | Layout 1 | `3b99adb6402d`  |
| 2567   | Layout 1 | `3b99adb6402d`  |
| 2560   | Layout 1 | `3b99adb6402d`  |
| 2553   | Layout 1 | `3b99adb6402d`  |
| 2545   | Layout 1 | `3b99adb6402d`  |
| 2538   | Layout 1 | `3b99adb6402d`  |
| 2529   | Layout 1 | `3b99adb6402d`  |
| 2519   | Layout 1 | `3b99adb6402d`  |
| 2513   | Layout 1 | `3b99adb6402d`  |
| 2510   | Layout 1 | `3b99adb6402d`  |
| 2507   | Layout 1 | `3b99adb6402d`  |
| 2503   | Layout 1 | `3b99adb6402d`  |
| 2498   | Layout 1 | `3b99adb6402d`  |
| 2492   | Layout 1 | `3b99adb6402d`  |
| 2487   | Layout 1 | `3b99adb6402d`  |
| 2480   | Layout 1 | `3b99adb6402d`  |
| 2474   | Layout 1 | `3b99adb6402d`  |
| 2468   | Layout 1 | `3b99adb6402d`  |
| 2460   | Layout 1 | `3b99adb6402d`  |
| 2453   | Layout 1 | `3b99adb6402d`  |
| 2444   | Layout 1 | `3b99adb6402d`  |
| 2438   | Layout 1 | `3b99adb6402d`  |
| 2434   | Layout 1 | `3b99adb6402d`  |
| 2429   | Layout 1 | `3b99adb6402d`  |
| 2421   | Layout 1 | `3b99adb6402d`  |
| 2414   | Layout 1 | `3b99adb6402d`  |
| 2407   | Layout 1 | `3b99adb6402d`  |
| 2401   | Layout 1 | `3b99adb6402d`  |
| 2397   | Layout 1 | `3b99adb6402d`  |
| 2393   | Layout 1 | `3b99adb6402d`  |
| 2384   | Layout 1 | `3b99adb6402d`  |
| 2378   | Layout 1 | `3b99adb6402d`  |
| 2372   | Layout 1 | `3b99adb6402d`  |
| 2358   | Layout 1 | `3b99adb6402d`  |
| 2352   | Layout 1 | `3b99adb6402d`  |
| 2347   | Layout 1 | `3b99adb6402d`  |
| 2343   | Layout 1 | `3b99adb6402d`  |
| 2335   | Layout 1 | `3b99adb6402d`  |
| 2327   | Layout 1 | `3b99adb6402d`  |
| 2324   | Layout 1 | `3b99adb6402d`  |
| 2319   | Layout 1 | `3b99adb6402d`  |
| 2313   | Layout 1 | `3b99adb6402d`  |
| 2308   | Layout 1 | `3b99adb6402d`  |
| 2302   | Layout 1 | `3b99adb6402d`  |
| 2295   | Layout 1 | `3b99adb6402d`  |
| 2290   | Layout 1 | `3b99adb6402d`  |
| 2284   | Layout 1 | `3b99adb6402d`  |
| 2276   | Layout 1 | `3b99adb6402d`  |
| 2269   | Layout 1 | `3b99adb6402d`  |
| 2259   | Layout 1 | `3b99adb6402d`  |
| 2250   | Layout 1 | `3b99adb6402d`  |
| 2243   | Layout 1 | `3b99adb6402d`  |
| 2235   | Layout 1 | `3b99adb6402d`  |
| 2229   | Layout 1 | `3b99adb6402d`  |
| 2224   | Layout 1 | `3b99adb6402d`  |
| 2218   | Layout 1 | `3b99adb6402d`  |
| 2215   | Layout 1 | `3b99adb6402d`  |
| 2207   | Layout 1 | `3b99adb6402d`  |
| 2203   | Layout 1 | `3b99adb6402d`  |
| 2196   | Layout 1 | `3b99adb6402d`  |
| 2192   | Layout 1 | `3b99adb6402d`  |
| 2189   | Layout 1 | `3b99adb6402d`  |
| 2183   | Layout 1 | `3b99adb6402d`  |
| 2179   | Layout 1 | `3b99adb6402d`  |
| 2171   | Layout 1 | `3b99adb6402d`  |
| 2163   | Layout 1 | `3b99adb6402d`  |
| 2156   | Layout 1 | `3b99adb6402d`  |
| 2151   | Layout 1 | `3b99adb6402d`  |
| 2147   | Layout 1 | `3b99adb6402d`  |
| 2142   | Layout 1 | `3b99adb6402d`  |
| 2138   | Layout 1 | `3b99adb6402d`  |
| 2134   | Layout 1 | `3b99adb6402d`  |
| 2130   | Layout 1 | `3b99adb6402d`  |
| 2122   | Layout 1 | `3b99adb6402d`  |
| 2107   | Layout 1 | `3b99adb6402d`  |
| 2098   | Layout 1 | `3b99adb6402d`  |
| 2089   | Layout 1 | `3b99adb6402d`  |
| 2081   | Layout 1 | `3b99adb6402d`  |
| 2073   | Layout 1 | `3b99adb6402d`  |
| 2067   | Layout 1 | `3b99adb6402d`  |
| 2063   | Layout 1 | `3b99adb6402d`  |
| 2059   | Layout 1 | `3b99adb6402d`  |
| 2052   | Layout 1 | `3b99adb6402d`  |
| 2044   | Layout 1 | `3b99adb6402d`  |
| 2039   | Layout 1 | `3b99adb6402d`  |
| 2032   | Layout 1 | `3b99adb6402d`  |
| 2025   | Layout 1 | `3b99adb6402d`  |
| 2011   | Layout 1 | `3b99adb6402d`  |
| 2005   | Layout 1 | `3b99adb6402d`  |
| 2000   | Layout 1 | `3b99adb6402d`  |
| 1996   | Layout 1 | `3b99adb6402d`  |
| 1991   | Layout 1 | `3b99adb6402d`  |
| 1985   | Layout 1 | `3b99adb6402d`  |
| 1980   | Layout 1 | `3b99adb6402d`  |
| 1969   | Layout 1 | `3b99adb6402d`  |
| 1964   | Layout 1 | `3b99adb6402d`  |
| 1958   | Layout 1 | `3b99adb6402d`  |
| 1950   | Layout 1 | `3b99adb6402d`  |
| 1945   | Layout 1 | `3b99adb6402d`  |
| 1937   | Layout 1 | `3b99adb6402d`  |
| 1933   | Layout 1 | `3b99adb6402d`  |
| 1927   | Layout 1 | `3b99adb6402d`  |
| 1921   | Layout 1 | `3b99adb6402d`  |
| 1914   | Layout 1 | `3b99adb6402d`  |
| 1908   | Layout 1 | `3b99adb6402d`  |
| 1897   | Layout 1 | `3b99adb6402d`  |
| 1892   | Layout 1 | `3b99adb6402d`  |
| 1886   | Layout 1 | `3b99adb6402d`  |
| 1881   | Layout 1 | `3b99adb6402d`  |
| 1871   | Layout 1 | `3b99adb6402d`  |
| 1866   | Layout 1 | `3b99adb6402d`  |
| 1862   | Layout 1 | `3b99adb6402d`  |
| 1854   | Layout 1 | `3b99adb6402d`  |
| 1846   | Layout 1 | `3b99adb6402d`  |
| 1838   | Layout 1 | `3b99adb6402d`  |
| 1832   | Layout 1 | `3b99adb6402d`  |
| 1826   | Layout 1 | `3b99adb6402d`  |
| 1822   | Layout 1 | `3b99adb6402d`  |
| 1818   | Layout 1 | `3b99adb6402d`  |
| 1804   | Layout 1 | `3b99adb6402d`  |
| 1794   | Layout 1 | `3b99adb6402d`  |
| 1790   | Layout 1 | `3b99adb6402d`  |
| 1784   | Layout 1 | `3b99adb6402d`  |
| 1774   | Layout 1 | `3b99adb6402d`  |
| 1771   | Layout 1 | `3b99adb6402d`  |
| 1762   | Layout 1 | `3b99adb6402d`  |
| 1759   | Layout 1 | `3b99adb6402d`  |
| 1754   | Layout 1 | `3b99adb6402d`  |
| 1749   | Layout 1 | `3b99adb6402d`  |
| 1743   | Layout 1 | `3b99adb6402d`  |
| 1737   | Layout 1 | `3b99adb6402d`  |
| 1731   | Layout 1 | `3b99adb6402d`  |
| 1725   | Layout 1 | `3b99adb6402d`  |
| 1717   | Layout 1 | `3b99adb6402d`  |
| 1710   | Layout 1 | `3b99adb6402d`  |
| 1704   | Layout 1 | `3b99adb6402d`  |
| 1698   | Layout 1 | `3b99adb6402d`  |
| 1690   | Layout 1 | `3b99adb6402d`  |
| 1685   | Layout 1 | `3b99adb6402d`  |
| 1680   | Layout 1 | `3b99adb6402d`  |
| 1674   | Layout 1 | `3b99adb6402d`  |
| 1668   | Layout 1 | `3b99adb6402d`  |
| 1659   | Layout 1 | `3b99adb6402d`  |
| 1649   | Layout 1 | `3b99adb6402d`  |
| 1642   | Layout 1 | `3b99adb6402d`  |
| 1636   | Layout 1 | `3b99adb6402d`  |
| 1628   | Layout 1 | `3b99adb6402d`  |
| 1622   | Layout 1 | `3b99adb6402d`  |
| 1614   | Layout 1 | `3b99adb6402d`  |
| 1608   | Layout 1 | `3b99adb6402d`  |
| 1602   | Layout 1 | `3b99adb6402d`  |
| 1598   | Layout 1 | `3b99adb6402d`  |
| 1594   | Layout 1 | `3b99adb6402d`  |
| 1590   | Layout 1 | `3b99adb6402d`  |
| 1587   | Layout 1 | `3b99adb6402d`  |
| 1584   | Layout 1 | `3b99adb6402d`  |
| 1579   | Layout 1 | `3b99adb6402d`  |
| 1572   | Layout 1 | `3b99adb6402d`  |
| 1565   | Layout 1 | `3b99adb6402d`  |
| 1559   | Layout 1 | `3b99adb6402d`  |
| 1554   | Layout 1 | `3b99adb6402d`  |
| 1547   | Layout 1 | `3b99adb6402d`  |
| 1537   | Layout 1 | `3b99adb6402d`  |
| 1529   | Layout 1 | `3b99adb6402d`  |
| 1524   | Layout 1 | `3b99adb6402d`  |
| 1519   | Layout 1 | `3b99adb6402d`  |
| 1509   | Layout 1 | `3b99adb6402d`  |
| 1506   | Layout 1 | `3b99adb6402d`  |
| 1504   | No file  | `3b99adb6402d`  |
| 1500   | No file  | `3b99adb6402d`  |
| 1493   | No file  | `3b99adb6402d`  |
| 1489   | No file  | `3b99adb6402d`  |
| 1485   | No file  | `3b99adb6402d`  |
| 1481   | No file  | `3b99adb6402d`  |
| 1474   | No file  | `3b99adb6402d`  |
| 1466   | No file  | `3b99adb6402d`  |
| 1462   | No file  | `3b99adb6402d`  |
| 1459   | No file  | `3b99adb6402d`  |
| 1453   | No file  | `3b99adb6402d`  |
| 1450   | No file  | `3b99adb6402d`  |
| 1445   | No file  | `3b99adb6402d`  |
| 1439   | No file  | `3b99adb6402d`  |
| 1433   | No file  | `3b99adb6402d`  |
| 1430   | No file  | `3b99adb6402d`  |
| 1426   | No file  | `3b99adb6402d`  |
| 1421   | No file  | `3b99adb6402d`  |
| 1417   | No file  | `3b99adb6402d`  |
| 1416   | No file  | `3b99adb6402d`  |
| 1409   | No file  | `3b99adb6402d`  |
| 1405   | No file  | `3b99adb6402d`  |
| 1401   | No file  | `3b99adb6402d`  |
| 1396   | No file  | `3b99adb6402d`  |
| 1391   | No file  | `3b99adb6402d`  |
| 1390   | No file  | `3b99adb6402d`  |
| 1386   | No file  | `3b99adb6402d`  |
| 1381   | No file  | `3b99adb6402d`  |
| 1379   | No file  | `3b99adb6402d`  |
| 1372   | No file  | `3b99adb6402d`  |
| 1366   | No file  | `3b99adb6402d`  |
| 1364   | No file  | `3b99adb6402d`  |
| 1363   | No file  | `3b99adb6402d`  |
| 1360   | No file  | `3b99adb6402d`  |
| 1358   | No file  | `3b99adb6402d`  |
| 1355   | No file  | `3b99adb6402d`  |
| 1351   | No file  | `3b99adb6402d`  |
| 1348   | No file  | `3b99adb6402d`  |
| 1346   | No file  | `3b99adb6402d`  |
| 1341   | No file  | `3b99adb6402d`  |
| 1340   | No file  | `3b99adb6402d`  |
| 1338   | No file  | `3b99adb6402d`  |
| 1335   | No file  | `3b99adb6402d`  |
| 1333   | No file  | `3b99adb6402d`  |
| 1329   | No file  | `3b99adb6402d`  |
| 1327   | No file  | `3b99adb6402d`  |
| 1324   | No file  | `3b99adb6402d`  |
| 1321   | No file  | `3b99adb6402d`  |
| 1319   | No file  | `3b99adb6402d`  |
| 1318   | No file  | `3b99adb6402d`  |
| 1316   | No file  | `3b99adb6402d`  |
| 1313   | No file  | `3b99adb6402d`  |
| 1311   | No file  | `3b99adb6402d`  |
| 1309   | No file  | `3b99adb6402d`  |
| 1304   | No file  | `3b99adb6402d`  |
| 1292   | No file  | `3b99adb6402d`  |
| 1286   | No file  | `3b99adb6402d`  |
| 1280   | No file  | `3b99adb6402d`  |
| 1276   | No file  | `3b99adb6402d`  |
| 1267   | No file  | `3b99adb6402d`  |
| 1261   | No file  | `3b99adb6402d`  |
| 1256   | No file  | `3b99adb6402d`  |
| 1250   | No file  | `3b99adb6402d`  |
| 1246   | No file  | `3b99adb6402d`  |
| 1239   | No file  | `3b99adb6402d`  |
| 1230   | No file  | `3b99adb6402d`  |
| 1226   | No file  | `3b99adb6402d`  |
| 1220   | No file  | `3b99adb6402d`  |
| 1217   | No file  | `3b99adb6402d`  |
| 1211   | No file  | `3b99adb6402d`  |
| 1210   | No file  | `3b99adb6402d`  |
| 1208   | No file  | `3b99adb6402d`  |
| 1203   | No file  | `3b99adb6402d`  |
| 1197   | No file  | `3b99adb6402d`  |
| 1194   | No file  | `3b99adb6402d`  |
| 1192   | No file  | `3b99adb6402d`  |
| 1187   | No file  | `3b99adb6402d`  |
| 1183   | No file  | `3b99adb6402d`  |
| 1177   | No file  | `3b99adb6402d`  |
| 1173   | No file  | `3b99adb6402d`  |
| 1167   | No file  | `3b99adb6402d`  |
| 1164   | No file  | `3b99adb6402d`  |
| 1156   | No file  | `3b99adb6402d`  |
| 1149   | No file  | `3b99adb6402d`  |
| 1144   | No file  | `3b99adb6402d`  |
| 1137   | No file  | `3b99adb6402d`  |
| 1132   | No file  | `3b99adb6402d`  |
| 1127   | No file  | `3b99adb6402d`  |
| 1122   | No file  | `3b99adb6402d`  |
| 1118   | No file  | `3b99adb6402d`  |
| 1114   | No file  | `3b99adb6402d`  |
| 1109   | No file  | `3b99adb6402d`  |
| 1102   | No file  | `3b99adb6402d`  |
| 1096   | No file  | `3b99adb6402d`  |
| 1088   | No file  | `3b99adb6402d`  |
| 1081   | No file  | `3b99adb6402d`  |
| 1076   | No file  | `3b99adb6402d`  |
| 1069   | No file  | `3b99adb6402d`  |
| 1064   | No file  | `3b99adb6402d`  |
| 1058   | No file  | `3b99adb6402d`  |
| 1051   | No file  | `3b99adb6402d`  |
| 1044   | No file  | `3b99adb6402d`  |
| 1036   | No file  | `3b99adb6402d`  |
| 1026   | No file  | `3b99adb6402d`  |
| 1016   | No file  | `3b99adb6402d`  |
| 1009   | No file  | `3b99adb6402d`  |
| 1005   | No file  | `3b99adb6402d`  |
| 1000   | No file  | `3b99adb6402d`  |
| 998    | No file  | `3b99adb6402d`  |
| 990    | No file  | `3b99adb6402d`  |
| 979    | No file  | `3b99adb6402d`  |
| 972    | No file  | `3b99adb6402d`  |
| 963    | No file  | `3b99adb6402d`  |
| 955    | No file  | `3b99adb6402d`  |
| 946    | No file  | `3b99adb6402d`  |
| 938    | No file  | `3b99adb6402d`  |
| 927    | No file  | `3b99adb6402d`  |
| 911    | No file  | `3b99adb6402d`  |
| 904    | No file  | `3b99adb6402d`  |
| 899    | No file  | `3b99adb6402d`  |
| 894    | No file  | `3b99adb6402d`  |
| 885    | No file  | `3b99adb6402d`  |
| 879    | No file  | `3b99adb6402d`  |
| 872    | No file  | `3b99adb6402d`  |
| 864    | No file  | `3b99adb6402d`  |
| 855    | No file  | `3b99adb6402d`  |
| 853    | No file  | `3b99adb6402d`  |
| 845    | No file  | `3b99adb6402d`  |
| 837    | No file  | `3b99adb6402d`  |
| 829    | No file  | `3b99adb6402d`  |
| 822    | No file  | `3b99adb6402d`  |
| 814    | No file  | `3b99adb6402d`  |
| 805    | No file  | `3b99adb6402d`  |
| 794    | No file  | `3b99adb6402d`  |
| 787    | No file  | `3b99adb6402d`  |
| 780    | No file  | `3b99adb6402d`  |
| 771    | No file  | `3b99adb6402d`  |
| 760    | No file  | `3b99adb6402d`  |
| 748    | No file  | `3b99adb6402d`  |
| 741    | No file  | `3b99adb6402d`  |
| 736    | No file  | `3b99adb6402d`  |
| 731    | No file  | `3b99adb6402d`  |
| 723    | No file  | `3b99adb6402d`  |
| 711    | No file  | `3b99adb6402d`  |
| 707    | No file  | `3b99adb6402d`  |
| 697    | No file  | `3b99adb6402d`  |
| 689    | No file  | `3b99adb6402d`  |
| 683    | No file  | `3b99adb6402d`  |
| 678    | No file  | `3b99adb6402d`  |
| 670    | No file  | `3b99adb6402d`  |
| 661    | No file  | `3b99adb6402d`  |
| 656    | No file  | `3b99adb6402d`  |
| 652    | No file  | `3b99adb6402d`  |
| 643    | No file  | `3b99adb6402d`  |
| 637    | No file  | `3b99adb6402d`  |
| 630    | No file  | `3b99adb6402d`  |
| 627    | No file  | `3b99adb6402d`  |
| 621    | No file  | `3b99adb6402d`  |
| 617    | No file  | `3b99adb6402d`  |
| 615    | No file  | `3b99adb6402d`  |
| 606    | No file  | `3b99adb6402d`  |
| 599    | No file  | `3b99adb6402d`  |
| 592    | No file  | `3b99adb6402d`  |
| 586    | No file  | `3b99adb6402d`  |
| 577    | No file  | `3b99adb6402d`  |
| 569    | No file  | `3b99adb6402d`  |
| 561    | No file  | `3b99adb6402d`  |
| 554    | No file  | `3b99adb6402d`  |
| 542    | No file  | `3b99adb6402d`  |
| 532    | No file  | `3b99adb6402d`  |
| 531    | No file  | `3b99adb6402d`  |
| 526    | No file  | `3b99adb6402d`  |
| 521    | No file  | `3b99adb6402d`  |
| 517    | No file  | `3b99adb6402d`  |
| 510    | No file  | `3b99adb6402d`  |
| 508    | No file  | `3b99adb6402d`  |
| 504    | No file  | `3b99adb6402d`  |
| 497    | No file  | `3b99adb6402d`  |
| 491    | No file  | `3b99adb6402d`  |
| 485    | No file  | `3b99adb6402d`  |
| 478    | No file  | `3b99adb6402d`  |
| 472    | No file  | `3b99adb6402d`  |
| 466    | No file  | `3b99adb6402d`  |
| 457    | No file  | `3b99adb6402d`  |
| 452    | No file  | `3b99adb6402d`  |
| 449    | No file  | `3b99adb6402d`  |
| 435    | No file  | `3b99adb6402d`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `stringtable.bss`     | Optional | Hash of the `ranking_name` key, for its LOC type 37 text |
| `languagedata_en.loc` | Optional | Season name in the user's language |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                              |
| ------------------- | ----------------- | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                             |
| `+0x04`             | u32               | record_count       | Number of rows                     |
| `+0x08`             | Row[record_count] | records            | See Row                            |
| `records+0x00`      | String Table      | string_table       | The season name keys               |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`  |
| `string_table+0x04` | u32               | zero               | `0`                                |

### Row (26 bytes)

| Offset  | Type | Field           | Notes |
| ------- | ---- | --------------- | ----- |
| `+0x00` | u32  | ranking_idx     | Row key, `1` up in file order |
| `+0x04` | u16  | instance_type   | `11` on every row (client 3482) |
| `+0x06` | u64  | start_date_rank | Start, seconds since 1970-01-01; see [Times](#times) |
| `+0x0E` | u64  | end_date_rank   | End, in the same unit |
| `+0x16` | u32  | ranking_name    | Index into `strings`: a `GAME` sheet key (`LUA_INSTANCE_SEASONRANK_NAME_1`, "Season 1") |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `2` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | `LUA_INSTANCE_SEASONRANK_NAME_1` and `_2`, UTF-8 (`is_wide` 0) |

## Times

The sheet writes the times as a date and a time of day. Read as UTC, the
values of client 3482 give the sheet's own times on all 12 rows client
1784 has (`2021-02-03 08:59` for the start of ranking `1`). The file of
client 1784 holds the same times 9 hours earlier, so they read back as
the sheet's times in Korean time (UTC+9). The tool that compiles the sheet
seems to convert the written time with its own time zone. The handler
shows the values as UTC.

## Field Names

The names follow the `InstanceRankingManage` sheet of a private server's
`DataSheets.bexcel` on client 1784 (`RankingIdx`, `InstanceType`,
`RankingName`, `StartDateRank`, `EndDateRank`). On the 12 keys the sheet
shares with client 1784, `instance_type` and `ranking_name` equal the
sheet on every row and both times equal it read in Korean time; on client
3482 the same 12 keys equal it read as UTC. The developer notes of the
sheet's `.xlsm` copy (`#Desc`) name ranking `1` and `2` "테스트용 그믐달
그랑프리 시즌 1 / 2" (test Old Moon Grand Prix season 1 and 2) and `3` to
`12` the season 1 of one service each (`7`: NA/EU).

## Notes

- Clients 2519 to 3482 have 14 rows; clients 1784 and 2107 have rows `1`
  to `12`.
