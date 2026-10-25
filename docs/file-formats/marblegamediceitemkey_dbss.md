# `marblegamediceitemkey.dbss` Format

## Purpose

The keys of the Black Spirit's Adventure dice items: the dice and the board
cards (Pace of Delight, Lucky Day, Fated Encounter and more) a player rolls
or plays on the board. The file holds the keys only, 45 on client 3482 and
28 on client 1784. Which dice drop together is in
[`marblegamediceitemgroup.dbss`](marblegamediceitemgroup_dbss.md).
Companion `marblegamediceitemkeyoffset.dbss` lists where every key sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes | Records       | Row bytes |
| ------ | -------------- | ---------------------------------- | ----- | ------------- | --------- |
| 1      | 1396 and later | `marblegamediceitemkey.dbss`       | 184   | 45 Row        | 4         |
| 1      | 1396 and later | `marblegamediceitemkeyoffset.dbss` | 544   | 45 Offset Row | 12        |

| Layout | File                               | Known          | Unknown    |
| ------ | ---------------------------------- | -------------- | ---------- |
| 1      | `marblegamediceitemkey.dbss`       | 184 B (100.0%) | 0 B (0.0%) |
| 1      | `marblegamediceitemkeyoffset.dbss` | 544 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `f115b6d22c27`  |
| 3482   | Layout 1 | `f115b6d22c27`  |
| 3474   | Layout 1 | `f115b6d22c27`  |
| 3473   | Layout 1 | `f115b6d22c27`  |
| 3464   | Layout 1 | `f115b6d22c27`  |
| 3458   | Layout 1 | `f115b6d22c27`  |
| 3454   | Layout 1 | `f115b6d22c27`  |
| 3444   | Layout 1 | `f115b6d22c27`  |
| 3435   | Layout 1 | `f115b6d22c27`  |
| 3426   | Layout 1 | `f115b6d22c27`  |
| 3418   | Layout 1 | `f115b6d22c27`  |
| 3412   | Layout 1 | `f115b6d22c27`  |
| 3402   | Layout 1 | `f115b6d22c27`  |
| 3396   | Layout 1 | `f115b6d22c27`  |
| 3387   | Layout 1 | `f115b6d22c27`  |
| 3381   | Layout 1 | `f115b6d22c27`  |
| 3373   | Layout 1 | `f115b6d22c27`  |
| 3364   | Layout 1 | `f115b6d22c27`  |
| 3356   | Layout 1 | `f115b6d22c27`  |
| 3349   | Layout 1 | `f115b6d22c27`  |
| 3342   | Layout 1 | `f115b6d22c27`  |
| 3335   | Layout 1 | `f115b6d22c27`  |
| 3326   | Layout 1 | `f115b6d22c27`  |
| 3321   | Layout 1 | `f115b6d22c27`  |
| 3314   | Layout 1 | `f115b6d22c27`  |
| 3303   | Layout 1 | `f115b6d22c27`  |
| 3302   | Layout 1 | `f115b6d22c27`  |
| 3293   | Layout 1 | `f115b6d22c27`  |
| 3283   | Layout 1 | `f115b6d22c27`  |
| 3275   | Layout 1 | `f115b6d22c27`  |
| 3267   | Layout 1 | `f115b6d22c27`  |
| 3258   | Layout 1 | `f115b6d22c27`  |
| 3251   | Layout 1 | `f115b6d22c27`  |
| 3242   | Layout 1 | `f115b6d22c27`  |
| 3235   | Layout 1 | `f115b6d22c27`  |
| 3229   | Layout 1 | `f115b6d22c27`  |
| 3212   | Layout 1 | `f115b6d22c27`  |
| 3203   | Layout 1 | `f115b6d22c27`  |
| 3193   | Layout 1 | `f115b6d22c27`  |
| 3186   | Layout 1 | `f115b6d22c27`  |
| 3177   | Layout 1 | `f115b6d22c27`  |
| 3169   | Layout 1 | `f115b6d22c27`  |
| 3158   | Layout 1 | `f115b6d22c27`  |
| 3151   | Layout 1 | `f115b6d22c27`  |
| 3144   | Layout 1 | `f115b6d22c27`  |
| 3133   | Layout 1 | `f115b6d22c27`  |
| 3125   | Layout 1 | `f115b6d22c27`  |
| 3118   | Layout 1 | `f115b6d22c27`  |
| 3111   | Layout 1 | `f115b6d22c27`  |
| 3103   | Layout 1 | `f115b6d22c27`  |
| 3095   | Layout 1 | `f115b6d22c27`  |
| 3086   | Layout 1 | `f115b6d22c27`  |
| 3072   | Layout 1 | `f115b6d22c27`  |
| 3062   | Layout 1 | `f115b6d22c27`  |
| 3052   | Layout 1 | `f115b6d22c27`  |
| 3045   | Layout 1 | `f115b6d22c27`  |
| 3037   | Layout 1 | `f115b6d22c27`  |
| 3030   | Layout 1 | `f115b6d22c27`  |
| 3021   | Layout 1 | `f115b6d22c27`  |
| 3012   | Layout 1 | `f115b6d22c27`  |
| 3002   | Layout 1 | `f115b6d22c27`  |
| 2995   | Layout 1 | `f115b6d22c27`  |
| 2987   | Layout 1 | `f115b6d22c27`  |
| 2978   | Layout 1 | `f115b6d22c27`  |
| 2970   | Layout 1 | `f115b6d22c27`  |
| 2959   | Layout 1 | `f115b6d22c27`  |
| 2951   | Layout 1 | `f115b6d22c27`  |
| 2942   | Layout 1 | `f115b6d22c27`  |
| 2935   | Layout 1 | `f115b6d22c27`  |
| 2932   | Layout 1 | `f115b6d22c27`  |
| 2923   | Layout 1 | `f115b6d22c27`  |
| 2919   | Layout 1 | `f115b6d22c27`  |
| 2907   | Layout 1 | `f115b6d22c27`  |
| 2900   | Layout 1 | `f115b6d22c27`  |
| 2891   | Layout 1 | `f115b6d22c27`  |
| 2882   | Layout 1 | `f115b6d22c27`  |
| 2872   | Layout 1 | `f115b6d22c27`  |
| 2863   | Layout 1 | `f115b6d22c27`  |
| 2855   | Layout 1 | `f115b6d22c27`  |
| 2849   | Layout 1 | `f115b6d22c27`  |
| 2844   | Layout 1 | `f115b6d22c27`  |
| 2834   | Layout 1 | `f115b6d22c27`  |
| 2825   | Layout 1 | `f115b6d22c27`  |
| 2819   | Layout 1 | `f115b6d22c27`  |
| 2811   | Layout 1 | `f115b6d22c27`  |
| 2803   | Layout 1 | `f115b6d22c27`  |
| 2794   | Layout 1 | `f115b6d22c27`  |
| 2783   | Layout 1 | `f115b6d22c27`  |
| 2774   | Layout 1 | `f115b6d22c27`  |
| 2765   | Layout 1 | `f115b6d22c27`  |
| 2756   | Layout 1 | `f115b6d22c27`  |
| 2750   | Layout 1 | `f115b6d22c27`  |
| 2743   | Layout 1 | `f115b6d22c27`  |
| 2736   | Layout 1 | `f115b6d22c27`  |
| 2726   | Layout 1 | `f115b6d22c27`  |
| 2717   | Layout 1 | `f115b6d22c27`  |
| 2709   | Layout 1 | `f115b6d22c27`  |
| 2703   | Layout 1 | `f115b6d22c27`  |
| 2695   | Layout 1 | `f115b6d22c27`  |
| 2684   | Layout 1 | `f115b6d22c27`  |
| 2672   | Layout 1 | `f115b6d22c27`  |
| 2665   | Layout 1 | `f115b6d22c27`  |
| 2657   | Layout 1 | `f115b6d22c27`  |
| 2649   | Layout 1 | `f115b6d22c27`  |
| 2644   | Layout 1 | `f115b6d22c27`  |
| 2637   | Layout 1 | `f115b6d22c27`  |
| 2629   | Layout 1 | `f115b6d22c27`  |
| 2619   | Layout 1 | `f115b6d22c27`  |
| 2612   | Layout 1 | `f115b6d22c27`  |
| 2606   | Layout 1 | `f115b6d22c27`  |
| 2602   | Layout 1 | `f115b6d22c27`  |
| 2601   | Layout 1 | `f115b6d22c27`  |
| 2592   | Layout 1 | `f115b6d22c27`  |
| 2583   | Layout 1 | `f115b6d22c27`  |
| 2575   | Layout 1 | `f115b6d22c27`  |
| 2567   | Layout 1 | `f115b6d22c27`  |
| 2560   | Layout 1 | `f115b6d22c27`  |
| 2553   | Layout 1 | `f115b6d22c27`  |
| 2545   | Layout 1 | `f115b6d22c27`  |
| 2538   | Layout 1 | `f115b6d22c27`  |
| 2529   | Layout 1 | `f115b6d22c27`  |
| 2519   | Layout 1 | `f115b6d22c27`  |
| 2513   | Layout 1 | `f115b6d22c27`  |
| 2510   | Layout 1 | `f115b6d22c27`  |
| 2507   | Layout 1 | `f115b6d22c27`  |
| 2503   | Layout 1 | `f115b6d22c27`  |
| 2498   | Layout 1 | `f115b6d22c27`  |
| 2492   | Layout 1 | `f115b6d22c27`  |
| 2487   | Layout 1 | `f115b6d22c27`  |
| 2480   | Layout 1 | `f115b6d22c27`  |
| 2474   | Layout 1 | `f115b6d22c27`  |
| 2468   | Layout 1 | `f115b6d22c27`  |
| 2460   | Layout 1 | `f115b6d22c27`  |
| 2453   | Layout 1 | `f115b6d22c27`  |
| 2444   | Layout 1 | `f115b6d22c27`  |
| 2438   | Layout 1 | `f115b6d22c27`  |
| 2434   | Layout 1 | `f115b6d22c27`  |
| 2429   | Layout 1 | `f115b6d22c27`  |
| 2421   | Layout 1 | `f115b6d22c27`  |
| 2414   | Layout 1 | `f115b6d22c27`  |
| 2407   | Layout 1 | `f115b6d22c27`  |
| 2401   | Layout 1 | `f115b6d22c27`  |
| 2397   | Layout 1 | `f115b6d22c27`  |
| 2393   | Layout 1 | `f115b6d22c27`  |
| 2384   | Layout 1 | `f115b6d22c27`  |
| 2378   | Layout 1 | `f115b6d22c27`  |
| 2372   | Layout 1 | `f115b6d22c27`  |
| 2358   | Layout 1 | `f115b6d22c27`  |
| 2352   | Layout 1 | `f115b6d22c27`  |
| 2347   | Layout 1 | `f115b6d22c27`  |
| 2343   | Layout 1 | `f115b6d22c27`  |
| 2335   | Layout 1 | `f115b6d22c27`  |
| 2327   | Layout 1 | `f115b6d22c27`  |
| 2324   | Layout 1 | `f115b6d22c27`  |
| 2319   | Layout 1 | `f115b6d22c27`  |
| 2313   | Layout 1 | `f115b6d22c27`  |
| 2308   | Layout 1 | `f115b6d22c27`  |
| 2302   | Layout 1 | `f115b6d22c27`  |
| 2295   | Layout 1 | `f115b6d22c27`  |
| 2290   | Layout 1 | `f115b6d22c27`  |
| 2284   | Layout 1 | `f115b6d22c27`  |
| 2276   | Layout 1 | `f115b6d22c27`  |
| 2269   | Layout 1 | `f115b6d22c27`  |
| 2259   | Layout 1 | `f115b6d22c27`  |
| 2250   | Layout 1 | `f115b6d22c27`  |
| 2243   | Layout 1 | `f115b6d22c27`  |
| 2235   | Layout 1 | `f115b6d22c27`  |
| 2229   | Layout 1 | `f115b6d22c27`  |
| 2224   | Layout 1 | `f115b6d22c27`  |
| 2218   | Layout 1 | `f115b6d22c27`  |
| 2215   | Layout 1 | `f115b6d22c27`  |
| 2207   | Layout 1 | `f115b6d22c27`  |
| 2203   | Layout 1 | `f115b6d22c27`  |
| 2196   | Layout 1 | `f115b6d22c27`  |
| 2192   | Layout 1 | `f115b6d22c27`  |
| 2189   | Layout 1 | `f115b6d22c27`  |
| 2183   | Layout 1 | `f115b6d22c27`  |
| 2179   | Layout 1 | `f115b6d22c27`  |
| 2171   | Layout 1 | `f115b6d22c27`  |
| 2163   | Layout 1 | `f115b6d22c27`  |
| 2156   | Layout 1 | `f115b6d22c27`  |
| 2151   | Layout 1 | `f115b6d22c27`  |
| 2147   | Layout 1 | `f115b6d22c27`  |
| 2142   | Layout 1 | `f115b6d22c27`  |
| 2138   | Layout 1 | `f115b6d22c27`  |
| 2134   | Layout 1 | `f115b6d22c27`  |
| 2130   | Layout 1 | `f115b6d22c27`  |
| 2122   | Layout 1 | `f115b6d22c27`  |
| 2107   | Layout 1 | `f115b6d22c27`  |
| 2098   | Layout 1 | `f115b6d22c27`  |
| 2089   | Layout 1 | `f115b6d22c27`  |
| 2081   | Layout 1 | `f115b6d22c27`  |
| 2073   | Layout 1 | `f115b6d22c27`  |
| 2067   | Layout 1 | `f115b6d22c27`  |
| 2063   | Layout 1 | `f115b6d22c27`  |
| 2059   | Layout 1 | `f115b6d22c27`  |
| 2052   | Layout 1 | `f115b6d22c27`  |
| 2044   | Layout 1 | `f115b6d22c27`  |
| 2039   | Layout 1 | `f115b6d22c27`  |
| 2032   | Layout 1 | `f115b6d22c27`  |
| 2025   | Layout 1 | `f115b6d22c27`  |
| 2011   | Layout 1 | `f115b6d22c27`  |
| 2005   | Layout 1 | `f115b6d22c27`  |
| 2000   | Layout 1 | `f115b6d22c27`  |
| 1996   | Layout 1 | `f115b6d22c27`  |
| 1991   | Layout 1 | `f115b6d22c27`  |
| 1985   | Layout 1 | `f115b6d22c27`  |
| 1980   | Layout 1 | `f115b6d22c27`  |
| 1969   | Layout 1 | `f115b6d22c27`  |
| 1964   | Layout 1 | `f115b6d22c27`  |
| 1958   | Layout 1 | `f115b6d22c27`  |
| 1950   | Layout 1 | `f115b6d22c27`  |
| 1945   | Layout 1 | `f115b6d22c27`  |
| 1937   | Layout 1 | `f115b6d22c27`  |
| 1933   | Layout 1 | `f115b6d22c27`  |
| 1927   | Layout 1 | `f115b6d22c27`  |
| 1921   | Layout 1 | `f115b6d22c27`  |
| 1914   | Layout 1 | `f115b6d22c27`  |
| 1908   | Layout 1 | `f115b6d22c27`  |
| 1897   | Layout 1 | `f115b6d22c27`  |
| 1892   | Layout 1 | `f115b6d22c27`  |
| 1886   | Layout 1 | `f115b6d22c27`  |
| 1881   | Layout 1 | `f115b6d22c27`  |
| 1871   | Layout 1 | `f115b6d22c27`  |
| 1866   | Layout 1 | `f115b6d22c27`  |
| 1862   | Layout 1 | `f115b6d22c27`  |
| 1854   | Layout 1 | `f115b6d22c27`  |
| 1846   | Layout 1 | `f115b6d22c27`  |
| 1838   | Layout 1 | `f115b6d22c27`  |
| 1832   | Layout 1 | `f115b6d22c27`  |
| 1826   | Layout 1 | `f115b6d22c27`  |
| 1822   | Layout 1 | `f115b6d22c27`  |
| 1818   | Layout 1 | `f115b6d22c27`  |
| 1804   | Layout 1 | `f115b6d22c27`  |
| 1794   | Layout 1 | `f115b6d22c27`  |
| 1790   | Layout 1 | `f115b6d22c27`  |
| 1784   | Layout 1 | `f115b6d22c27`  |
| 1774   | Layout 1 | `f115b6d22c27`  |
| 1771   | Layout 1 | `f115b6d22c27`  |
| 1762   | Layout 1 | `f115b6d22c27`  |
| 1759   | Layout 1 | `f115b6d22c27`  |
| 1754   | Layout 1 | `f115b6d22c27`  |
| 1749   | Layout 1 | `f115b6d22c27`  |
| 1743   | Layout 1 | `f115b6d22c27`  |
| 1737   | Layout 1 | `f115b6d22c27`  |
| 1731   | Layout 1 | `f115b6d22c27`  |
| 1725   | Layout 1 | `f115b6d22c27`  |
| 1717   | Layout 1 | `f115b6d22c27`  |
| 1710   | Layout 1 | `f115b6d22c27`  |
| 1704   | Layout 1 | `f115b6d22c27`  |
| 1698   | Layout 1 | `f115b6d22c27`  |
| 1690   | Layout 1 | `f115b6d22c27`  |
| 1685   | Layout 1 | `f115b6d22c27`  |
| 1680   | Layout 1 | `f115b6d22c27`  |
| 1674   | Layout 1 | `f115b6d22c27`  |
| 1668   | Layout 1 | `f115b6d22c27`  |
| 1659   | Layout 1 | `f115b6d22c27`  |
| 1649   | Layout 1 | `f115b6d22c27`  |
| 1642   | Layout 1 | `f115b6d22c27`  |
| 1636   | Layout 1 | `f115b6d22c27`  |
| 1628   | Layout 1 | `f115b6d22c27`  |
| 1622   | Layout 1 | `f115b6d22c27`  |
| 1614   | Layout 1 | `f115b6d22c27`  |
| 1608   | Layout 1 | `f115b6d22c27`  |
| 1602   | Layout 1 | `f115b6d22c27`  |
| 1598   | Layout 1 | `f115b6d22c27`  |
| 1594   | Layout 1 | `f115b6d22c27`  |
| 1590   | Layout 1 | `f115b6d22c27`  |
| 1587   | Layout 1 | `f115b6d22c27`  |
| 1584   | Layout 1 | `f115b6d22c27`  |
| 1579   | Layout 1 | `f115b6d22c27`  |
| 1572   | Layout 1 | `f115b6d22c27`  |
| 1565   | Layout 1 | `f115b6d22c27`  |
| 1559   | Layout 1 | `f115b6d22c27`  |
| 1554   | Layout 1 | `f115b6d22c27`  |
| 1547   | Layout 1 | `f115b6d22c27`  |
| 1537   | Layout 1 | `f115b6d22c27`  |
| 1529   | Layout 1 | `f115b6d22c27`  |
| 1524   | Layout 1 | `f115b6d22c27`  |
| 1519   | Layout 1 | `f115b6d22c27`  |
| 1509   | Layout 1 | `f115b6d22c27`  |
| 1506   | Layout 1 | `f115b6d22c27`  |
| 1504   | Layout 1 | `f115b6d22c27`  |
| 1500   | Layout 1 | `f115b6d22c27`  |
| 1493   | Layout 1 | `f115b6d22c27`  |
| 1489   | Layout 1 | `f115b6d22c27`  |
| 1485   | Layout 1 | `f115b6d22c27`  |
| 1481   | Layout 1 | `f115b6d22c27`  |
| 1474   | Layout 1 | `f115b6d22c27`  |
| 1466   | Layout 1 | `f115b6d22c27`  |
| 1462   | Layout 1 | `f115b6d22c27`  |
| 1459   | Layout 1 | `f115b6d22c27`  |
| 1453   | Layout 1 | `f115b6d22c27`  |
| 1450   | Layout 1 | `f115b6d22c27`  |
| 1445   | Layout 1 | `f115b6d22c27`  |
| 1439   | Layout 1 | `f115b6d22c27`  |
| 1433   | Layout 1 | `f115b6d22c27`  |
| 1430   | Layout 1 | `f115b6d22c27`  |
| 1426   | Layout 1 | `f115b6d22c27`  |
| 1421   | Layout 1 | `f115b6d22c27`  |
| 1417   | Layout 1 | `f115b6d22c27`  |
| 1416   | Layout 1 | `f115b6d22c27`  |
| 1409   | Layout 1 | `f115b6d22c27`  |
| 1405   | Layout 1 | `f115b6d22c27`  |
| 1401   | Layout 1 | `f115b6d22c27`  |
| 1396   | Layout 1 | `f115b6d22c27`  |
| 1391   | No file  | `f115b6d22c27`  |
| 1390   | No file  | `f115b6d22c27`  |
| 1386   | No file  | `f115b6d22c27`  |
| 1381   | No file  | `f115b6d22c27`  |
| 1379   | No file  | `f115b6d22c27`  |
| 1372   | No file  | `f115b6d22c27`  |
| 1366   | No file  | `f115b6d22c27`  |
| 1364   | No file  | `f115b6d22c27`  |
| 1363   | No file  | `f115b6d22c27`  |
| 1360   | No file  | `f115b6d22c27`  |
| 1358   | No file  | `f115b6d22c27`  |
| 1355   | No file  | `f115b6d22c27`  |
| 1351   | No file  | `f115b6d22c27`  |
| 1348   | No file  | `f115b6d22c27`  |
| 1346   | No file  | `f115b6d22c27`  |
| 1341   | No file  | `f115b6d22c27`  |
| 1340   | No file  | `f115b6d22c27`  |
| 1338   | No file  | `f115b6d22c27`  |
| 1335   | No file  | `f115b6d22c27`  |
| 1333   | No file  | `f115b6d22c27`  |
| 1329   | No file  | `f115b6d22c27`  |
| 1327   | No file  | `f115b6d22c27`  |
| 1324   | No file  | `f115b6d22c27`  |
| 1321   | No file  | `f115b6d22c27`  |
| 1319   | No file  | `f115b6d22c27`  |
| 1318   | No file  | `f115b6d22c27`  |
| 1316   | No file  | `f115b6d22c27`  |
| 1313   | No file  | `f115b6d22c27`  |
| 1311   | No file  | `f115b6d22c27`  |
| 1309   | No file  | `f115b6d22c27`  |
| 1304   | No file  | `f115b6d22c27`  |
| 1292   | No file  | `f115b6d22c27`  |
| 1286   | No file  | `f115b6d22c27`  |
| 1280   | No file  | `f115b6d22c27`  |
| 1276   | No file  | `f115b6d22c27`  |
| 1267   | No file  | `f115b6d22c27`  |
| 1261   | No file  | `f115b6d22c27`  |
| 1256   | No file  | `f115b6d22c27`  |
| 1250   | No file  | `f115b6d22c27`  |
| 1246   | No file  | `f115b6d22c27`  |
| 1239   | No file  | `f115b6d22c27`  |
| 1230   | No file  | `f115b6d22c27`  |
| 1226   | No file  | `f115b6d22c27`  |
| 1220   | No file  | `f115b6d22c27`  |
| 1217   | No file  | `f115b6d22c27`  |
| 1211   | No file  | `f115b6d22c27`  |
| 1210   | No file  | `f115b6d22c27`  |
| 1208   | No file  | `f115b6d22c27`  |
| 1203   | No file  | `f115b6d22c27`  |
| 1197   | No file  | `f115b6d22c27`  |
| 1194   | No file  | `f115b6d22c27`  |
| 1192   | No file  | `f115b6d22c27`  |
| 1187   | No file  | `f115b6d22c27`  |
| 1183   | No file  | `f115b6d22c27`  |
| 1177   | No file  | `f115b6d22c27`  |
| 1173   | No file  | `f115b6d22c27`  |
| 1167   | No file  | `f115b6d22c27`  |
| 1164   | No file  | `f115b6d22c27`  |
| 1156   | No file  | `f115b6d22c27`  |
| 1149   | No file  | `f115b6d22c27`  |
| 1144   | No file  | `f115b6d22c27`  |
| 1137   | No file  | `f115b6d22c27`  |
| 1132   | No file  | `f115b6d22c27`  |
| 1127   | No file  | `f115b6d22c27`  |
| 1122   | No file  | `f115b6d22c27`  |
| 1118   | No file  | `f115b6d22c27`  |
| 1114   | No file  | `f115b6d22c27`  |
| 1109   | No file  | `f115b6d22c27`  |
| 1102   | No file  | `f115b6d22c27`  |
| 1096   | No file  | `f115b6d22c27`  |
| 1088   | No file  | `f115b6d22c27`  |
| 1081   | No file  | `f115b6d22c27`  |
| 1076   | No file  | `f115b6d22c27`  |
| 1069   | No file  | `f115b6d22c27`  |
| 1064   | No file  | `f115b6d22c27`  |
| 1058   | No file  | `f115b6d22c27`  |
| 1051   | No file  | `f115b6d22c27`  |
| 1044   | No file  | `f115b6d22c27`  |
| 1036   | No file  | `f115b6d22c27`  |
| 1026   | No file  | `f115b6d22c27`  |
| 1016   | No file  | `f115b6d22c27`  |
| 1009   | No file  | `f115b6d22c27`  |
| 1005   | No file  | `f115b6d22c27`  |
| 1000   | No file  | `f115b6d22c27`  |
| 998    | No file  | `f115b6d22c27`  |
| 990    | No file  | `f115b6d22c27`  |
| 979    | No file  | `f115b6d22c27`  |
| 972    | No file  | `f115b6d22c27`  |
| 963    | No file  | `f115b6d22c27`  |
| 955    | No file  | `f115b6d22c27`  |
| 946    | No file  | `f115b6d22c27`  |
| 938    | No file  | `f115b6d22c27`  |
| 927    | No file  | `f115b6d22c27`  |
| 911    | No file  | `f115b6d22c27`  |
| 904    | No file  | `f115b6d22c27`  |
| 899    | No file  | `f115b6d22c27`  |
| 894    | No file  | `f115b6d22c27`  |
| 885    | No file  | `f115b6d22c27`  |
| 879    | No file  | `f115b6d22c27`  |
| 872    | No file  | `f115b6d22c27`  |
| 864    | No file  | `f115b6d22c27`  |
| 855    | No file  | `f115b6d22c27`  |
| 853    | No file  | `f115b6d22c27`  |
| 845    | No file  | `f115b6d22c27`  |
| 837    | No file  | `f115b6d22c27`  |
| 829    | No file  | `f115b6d22c27`  |
| 822    | No file  | `f115b6d22c27`  |
| 814    | No file  | `f115b6d22c27`  |
| 805    | No file  | `f115b6d22c27`  |
| 794    | No file  | `f115b6d22c27`  |
| 787    | No file  | `f115b6d22c27`  |
| 780    | No file  | `f115b6d22c27`  |
| 771    | No file  | `f115b6d22c27`  |
| 760    | No file  | `f115b6d22c27`  |
| 748    | No file  | `f115b6d22c27`  |
| 741    | No file  | `f115b6d22c27`  |
| 736    | No file  | `f115b6d22c27`  |
| 731    | No file  | `f115b6d22c27`  |
| 723    | No file  | `f115b6d22c27`  |
| 711    | No file  | `f115b6d22c27`  |
| 707    | No file  | `f115b6d22c27`  |
| 697    | No file  | `f115b6d22c27`  |
| 689    | No file  | `f115b6d22c27`  |
| 683    | No file  | `f115b6d22c27`  |
| 678    | No file  | `f115b6d22c27`  |
| 670    | No file  | `f115b6d22c27`  |
| 661    | No file  | `f115b6d22c27`  |
| 656    | No file  | `f115b6d22c27`  |
| 652    | No file  | `f115b6d22c27`  |
| 643    | No file  | `f115b6d22c27`  |
| 637    | No file  | `f115b6d22c27`  |
| 630    | No file  | `f115b6d22c27`  |
| 627    | No file  | `f115b6d22c27`  |
| 621    | No file  | `f115b6d22c27`  |
| 617    | No file  | `f115b6d22c27`  |
| 615    | No file  | `f115b6d22c27`  |
| 606    | No file  | `f115b6d22c27`  |
| 599    | No file  | `f115b6d22c27`  |
| 592    | No file  | `f115b6d22c27`  |
| 586    | No file  | `f115b6d22c27`  |
| 577    | No file  | `f115b6d22c27`  |
| 569    | No file  | `f115b6d22c27`  |
| 561    | No file  | `f115b6d22c27`  |
| 554    | No file  | `f115b6d22c27`  |
| 542    | No file  | `f115b6d22c27`  |
| 532    | No file  | `f115b6d22c27`  |
| 531    | No file  | `f115b6d22c27`  |
| 526    | No file  | `f115b6d22c27`  |
| 521    | No file  | `f115b6d22c27`  |
| 517    | No file  | `f115b6d22c27`  |
| 510    | No file  | `f115b6d22c27`  |
| 508    | No file  | `f115b6d22c27`  |
| 504    | No file  | `f115b6d22c27`  |
| 497    | No file  | `f115b6d22c27`  |
| 491    | No file  | `f115b6d22c27`  |
| 485    | No file  | `f115b6d22c27`  |
| 478    | No file  | `f115b6d22c27`  |
| 472    | No file  | `f115b6d22c27`  |
| 466    | No file  | `f115b6d22c27`  |
| 457    | No file  | `f115b6d22c27`  |
| 452    | No file  | `f115b6d22c27`  |
| 449    | No file  | `f115b6d22c27`  |
| 435    | No file  | `f115b6d22c27`  |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                                          |
| ---------------------------------- | -------- | ----------------------------------------------------------------------------- |
| `marblegamediceitemkeyoffset.dbss` | Optional | `dice_item_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `marblegamediceitemgroup.dbss`     | Optional | The drop groups that list each key, for the Drop Groups and Items columns     |
| `itemenchant.dbss`                 | Optional | The items that grant those groups; the handler reads them from the `MARBLE_DICE_GROUP_ITEMS` lookup index, not as a companion |
| `languagedata_en.loc`              | Optional | Item names (type 0)                                                           |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of keys |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3482 the file is 4 + 45 x 4 = 184 bytes.

### Row (4 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | dice_item_key | Row key; each key once. See Keys                            |

### `marblegamediceitemkeyoffset.dbss`

Bare offset table into `marblegamediceitemkey.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                        |
| ------- | ----------------- | ----- | -------------------------------------------- |
| `+0x00` | u32               | count | Equals the `marblegamediceitemkey.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                               |

### Offset Row (12 bytes)

| Offset  | Type | Field         | Notes                                   |
| ------- | ---- | ------------- | --------------------------------------- |
| `+0x00` | u32  | dice_item_key | Key of the row it points at             |
| `+0x04` | u32  | data_offset   | Row start, at `dice_item_key`           |
| `+0x08` | u32  | data_size     | `4` on every row                        |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order; on clients 1784 and 3482 every index row
points at the row with its key.

## Keys

The keys fall in ranges. The Item column names the items whose contents
event `98` grants a drop group that holds the key alone (see
[`marblegamediceitemgroup.dbss`](marblegamediceitemgroup_dbss.md)), on
client 3482; the Sheet Note column translates the Korean `#Desc` note
column of the `DiceItem_Table` sheet of a private server on client 1784.

| Keys         | Item (client 3482)                                                  | Sheet Note (client 1784)                     |
| ------------ | ------------------------------------------------------------------- | -------------------------------------------- |
| `1`          | Black Spirit's Dice                                                 | A die that rolls 1 to 6                      |
| `2` to `7`   | Black Spirit's Special Dice (1, 1) to (6,6)                         | A die that rolls only 1, ..., only 6         |
| `8`          | Black Spirit's Dice                                                 | Golden die                                   |
| `11` to `14` | [Event] Black Spirit's Purple, Orange, Small Snowflake and Large Snowflake Die | Purple, orange, small and large snowflake die |
| `15` to `31` | [Event] dice, `24` to `29` Festival Die (1) to (6); `18` and `19` have none | Not in the sheet                    |
| `101` to `106` | Pace of Delight - 1 Square to 6 Squares                           | Pace of Delight, 1 to 6 squares              |
| `201`, `202` | None                                                                | Move back 1 or 2 squares                     |
| `301` to `303` | Lucky Day - 1 to 3 Additional Rolls                               | Lucky Day, 1 to 3 more rolls                 |
| `401`        | Fated Encounter                                                     | Fated Encounter                              |
| `501`        | None                                                                | Resets the free die delay                    |
| `601`, `701`, `801` | Nice Fluke!, Clattering Rattle, Cosmos Cataclysm             | The Korean names of the same three cards     |

## Field Names

The `DiceItem_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `DiceItemKey` and `ItemType`; its 28 keys are
the 28 keys of the client 1784 file, and all 28 are in the client 3482
file. The `.xlsm` copy of the sheet
(`datasheet_itemdatatable_marblegamedice.xlsm`) adds the note column
`#Desc`, which is not compiled. `ItemType` (`0` on `1` to `8`, `2` on `11`
to `14`, `1` on the board cards from `101`) is not in the client file: a
row is the key alone.

## Notes

- Black Spirit's Adventure runs in a web control: `panel_eventmarblegame.luac`
  on client 3482 opens `bAdventureWebUrl .. "/MarbleGame/EventStart"`, and
  no client Lua reads this table.
- The Yar! dice keys of [`yachtdice.dbss`](yachtdice_dbss.md) (`1` to `15`)
  overlap these keys by number only. The Yar! sheets (`DiceList`,
  `DicePreset`) are in `datasheet_minigame.xlsm`, this one in
  `datasheet_itemdatatable_marblegamedice.xlsm`, and a Yar! die is six
  `yachtbasecard.dbss` faces, so the view does not link the two.
- The view shows each key with the drop groups that list it (each a link to
  its `marblegamediceitemgroup.dbss` row) and the items that grant those
  groups. Keys `201`, `202` and `501` are in no group on clients 1784 and
  3482.

## Open Questions

### How Keys Outside Every Group Are Handed Out

No drop group lists `201`, `202` (move back) or `501` (free die delay
reset), and no item grants them, on clients 1784 and 3482. Whether the
board hands them out through its squares on the web side is open.
