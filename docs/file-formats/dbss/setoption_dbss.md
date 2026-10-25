# `setoption.dbss` Format

## Purpose

The set effects of gear and furniture sets: on client 3482 75 sets, 29
gear sets (such as the Lar Arcien and Blitzen horse gear) and 46 furniture sets
(town interior sets, the Whale and Coral Reef furniture). Per set key the
file holds the set type, the set effect for each number of equipped pieces
and the item IDs of the pieces. A gear set's effect is a skill per piece
count, a furniture set's effect is interior points per piece count.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes  | Records       | Row bytes                  |
| ------ | -------------- | ---------------------- | ------ | ------------- | -------------------------- |
| 1      | 1267 and later | `setoption.dbss`       | 12,114 | 75 Row        | 146 to 198, 161 on average |
| 1      | 1267 and later | `setoptionoffset.dbss` | 754    | 75 Offset Row | 10                         |

| Layout | File                   | Known             | Unknown    |
| ------ | ---------------------- | ----------------- | ---------- |
| 1      | `setoption.dbss`       | 12,114 B (100.0%) | 0 B (0.0%) |
| 1      | `setoptionoffset.dbss` | 754 B (100.0%)    | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `89d6d8167d11`  |
| 3482   | Layout 1 | `89d6d8167d11`  |
| 3474   | Layout 1 | `89d6d8167d11`  |
| 3473   | Layout 1 | `89d6d8167d11`  |
| 3464   | Layout 1 | `89d6d8167d11`  |
| 3458   | Layout 1 | `89d6d8167d11`  |
| 3454   | Layout 1 | `89d6d8167d11`  |
| 3444   | Layout 1 | `89d6d8167d11`  |
| 3435   | Layout 1 | `89d6d8167d11`  |
| 3426   | Layout 1 | `89d6d8167d11`  |
| 3418   | Layout 1 | `89d6d8167d11`  |
| 3412   | Layout 1 | `89d6d8167d11`  |
| 3402   | Layout 1 | `89d6d8167d11`  |
| 3396   | Layout 1 | `89d6d8167d11`  |
| 3387   | Layout 1 | `89d6d8167d11`  |
| 3381   | Layout 1 | `89d6d8167d11`  |
| 3373   | Layout 1 | `89d6d8167d11`  |
| 3364   | Layout 1 | `89d6d8167d11`  |
| 3356   | Layout 1 | `89d6d8167d11`  |
| 3349   | Layout 1 | `89d6d8167d11`  |
| 3342   | Layout 1 | `89d6d8167d11`  |
| 3335   | Layout 1 | `89d6d8167d11`  |
| 3326   | Layout 1 | `89d6d8167d11`  |
| 3321   | Layout 1 | `89d6d8167d11`  |
| 3314   | Layout 1 | `89d6d8167d11`  |
| 3303   | Layout 1 | `89d6d8167d11`  |
| 3302   | Layout 1 | `89d6d8167d11`  |
| 3293   | Layout 1 | `89d6d8167d11`  |
| 3283   | Layout 1 | `89d6d8167d11`  |
| 3275   | Layout 1 | `89d6d8167d11`  |
| 3267   | Layout 1 | `89d6d8167d11`  |
| 3258   | Layout 1 | `89d6d8167d11`  |
| 3251   | Layout 1 | `89d6d8167d11`  |
| 3242   | Layout 1 | `89d6d8167d11`  |
| 3235   | Layout 1 | `89d6d8167d11`  |
| 3229   | Layout 1 | `89d6d8167d11`  |
| 3212   | Layout 1 | `89d6d8167d11`  |
| 3203   | Layout 1 | `89d6d8167d11`  |
| 3193   | Layout 1 | `89d6d8167d11`  |
| 3186   | Layout 1 | `89d6d8167d11`  |
| 3177   | Layout 1 | `89d6d8167d11`  |
| 3169   | Layout 1 | `89d6d8167d11`  |
| 3158   | Layout 1 | `89d6d8167d11`  |
| 3151   | Layout 1 | `89d6d8167d11`  |
| 3144   | Layout 1 | `89d6d8167d11`  |
| 3133   | Layout 1 | `89d6d8167d11`  |
| 3125   | Layout 1 | `89d6d8167d11`  |
| 3118   | Layout 1 | `89d6d8167d11`  |
| 3111   | Layout 1 | `89d6d8167d11`  |
| 3103   | Layout 1 | `89d6d8167d11`  |
| 3095   | Layout 1 | `89d6d8167d11`  |
| 3086   | Layout 1 | `89d6d8167d11`  |
| 3072   | Layout 1 | `89d6d8167d11`  |
| 3062   | Layout 1 | `89d6d8167d11`  |
| 3052   | Layout 1 | `89d6d8167d11`  |
| 3045   | Layout 1 | `89d6d8167d11`  |
| 3037   | Layout 1 | `89d6d8167d11`  |
| 3030   | Layout 1 | `89d6d8167d11`  |
| 3021   | Layout 1 | `89d6d8167d11`  |
| 3012   | Layout 1 | `89d6d8167d11`  |
| 3002   | Layout 1 | `89d6d8167d11`  |
| 2995   | Layout 1 | `89d6d8167d11`  |
| 2987   | Layout 1 | `89d6d8167d11`  |
| 2978   | Layout 1 | `89d6d8167d11`  |
| 2970   | Layout 1 | `89d6d8167d11`  |
| 2959   | Layout 1 | `89d6d8167d11`  |
| 2951   | Layout 1 | `89d6d8167d11`  |
| 2942   | Layout 1 | `89d6d8167d11`  |
| 2935   | Layout 1 | `89d6d8167d11`  |
| 2932   | Layout 1 | `89d6d8167d11`  |
| 2923   | Layout 1 | `89d6d8167d11`  |
| 2919   | Layout 1 | `89d6d8167d11`  |
| 2907   | Layout 1 | `89d6d8167d11`  |
| 2900   | Layout 1 | `89d6d8167d11`  |
| 2891   | Layout 1 | `89d6d8167d11`  |
| 2882   | Layout 1 | `89d6d8167d11`  |
| 2872   | Layout 1 | `89d6d8167d11`  |
| 2863   | Layout 1 | `89d6d8167d11`  |
| 2855   | Layout 1 | `89d6d8167d11`  |
| 2849   | Layout 1 | `89d6d8167d11`  |
| 2844   | Layout 1 | `89d6d8167d11`  |
| 2834   | Layout 1 | `89d6d8167d11`  |
| 2825   | Layout 1 | `89d6d8167d11`  |
| 2819   | Layout 1 | `89d6d8167d11`  |
| 2811   | Layout 1 | `89d6d8167d11`  |
| 2803   | Layout 1 | `89d6d8167d11`  |
| 2794   | Layout 1 | `89d6d8167d11`  |
| 2783   | Layout 1 | `89d6d8167d11`  |
| 2774   | Layout 1 | `89d6d8167d11`  |
| 2765   | Layout 1 | `89d6d8167d11`  |
| 2756   | Layout 1 | `89d6d8167d11`  |
| 2750   | Layout 1 | `89d6d8167d11`  |
| 2743   | Layout 1 | `89d6d8167d11`  |
| 2736   | Layout 1 | `89d6d8167d11`  |
| 2726   | Layout 1 | `89d6d8167d11`  |
| 2717   | Layout 1 | `89d6d8167d11`  |
| 2709   | Layout 1 | `89d6d8167d11`  |
| 2703   | Layout 1 | `89d6d8167d11`  |
| 2695   | Layout 1 | `89d6d8167d11`  |
| 2684   | Layout 1 | `89d6d8167d11`  |
| 2672   | Layout 1 | `89d6d8167d11`  |
| 2665   | Layout 1 | `89d6d8167d11`  |
| 2657   | Layout 1 | `89d6d8167d11`  |
| 2649   | Layout 1 | `89d6d8167d11`  |
| 2644   | Layout 1 | `89d6d8167d11`  |
| 2637   | Layout 1 | `89d6d8167d11`  |
| 2629   | Layout 1 | `89d6d8167d11`  |
| 2619   | Layout 1 | `89d6d8167d11`  |
| 2612   | Layout 1 | `89d6d8167d11`  |
| 2606   | Layout 1 | `89d6d8167d11`  |
| 2602   | Layout 1 | `89d6d8167d11`  |
| 2601   | Layout 1 | `89d6d8167d11`  |
| 2592   | Layout 1 | `89d6d8167d11`  |
| 2583   | Layout 1 | `89d6d8167d11`  |
| 2575   | Layout 1 | `89d6d8167d11`  |
| 2567   | Layout 1 | `89d6d8167d11`  |
| 2560   | Layout 1 | `89d6d8167d11`  |
| 2553   | Layout 1 | `89d6d8167d11`  |
| 2545   | Layout 1 | `89d6d8167d11`  |
| 2538   | Layout 1 | `89d6d8167d11`  |
| 2529   | Layout 1 | `89d6d8167d11`  |
| 2519   | Layout 1 | `89d6d8167d11`  |
| 2513   | Layout 1 | `89d6d8167d11`  |
| 2510   | Layout 1 | `89d6d8167d11`  |
| 2507   | Layout 1 | `89d6d8167d11`  |
| 2503   | Layout 1 | `89d6d8167d11`  |
| 2498   | Layout 1 | `89d6d8167d11`  |
| 2492   | Layout 1 | `89d6d8167d11`  |
| 2487   | Layout 1 | `89d6d8167d11`  |
| 2480   | Layout 1 | `89d6d8167d11`  |
| 2474   | Layout 1 | `89d6d8167d11`  |
| 2468   | Layout 1 | `89d6d8167d11`  |
| 2460   | Layout 1 | `89d6d8167d11`  |
| 2453   | Layout 1 | `89d6d8167d11`  |
| 2444   | Layout 1 | `89d6d8167d11`  |
| 2438   | Layout 1 | `89d6d8167d11`  |
| 2434   | Layout 1 | `89d6d8167d11`  |
| 2429   | Layout 1 | `89d6d8167d11`  |
| 2421   | Layout 1 | `89d6d8167d11`  |
| 2414   | Layout 1 | `89d6d8167d11`  |
| 2407   | Layout 1 | `89d6d8167d11`  |
| 2401   | Layout 1 | `89d6d8167d11`  |
| 2397   | Layout 1 | `89d6d8167d11`  |
| 2393   | Layout 1 | `89d6d8167d11`  |
| 2384   | Layout 1 | `89d6d8167d11`  |
| 2378   | Layout 1 | `89d6d8167d11`  |
| 2372   | Layout 1 | `89d6d8167d11`  |
| 2358   | Layout 1 | `89d6d8167d11`  |
| 2352   | Layout 1 | `89d6d8167d11`  |
| 2347   | Layout 1 | `89d6d8167d11`  |
| 2343   | Layout 1 | `89d6d8167d11`  |
| 2335   | Layout 1 | `89d6d8167d11`  |
| 2327   | Layout 1 | `89d6d8167d11`  |
| 2324   | Layout 1 | `89d6d8167d11`  |
| 2319   | Layout 1 | `89d6d8167d11`  |
| 2313   | Layout 1 | `89d6d8167d11`  |
| 2308   | Layout 1 | `89d6d8167d11`  |
| 2302   | Layout 1 | `89d6d8167d11`  |
| 2295   | Layout 1 | `89d6d8167d11`  |
| 2290   | Layout 1 | `89d6d8167d11`  |
| 2284   | Layout 1 | `89d6d8167d11`  |
| 2276   | Layout 1 | `89d6d8167d11`  |
| 2269   | Layout 1 | `89d6d8167d11`  |
| 2259   | Layout 1 | `89d6d8167d11`  |
| 2250   | Layout 1 | `89d6d8167d11`  |
| 2243   | Layout 1 | `89d6d8167d11`  |
| 2235   | Layout 1 | `89d6d8167d11`  |
| 2229   | Layout 1 | `89d6d8167d11`  |
| 2224   | Layout 1 | `89d6d8167d11`  |
| 2218   | Layout 1 | `89d6d8167d11`  |
| 2215   | Layout 1 | `89d6d8167d11`  |
| 2207   | Layout 1 | `89d6d8167d11`  |
| 2203   | Layout 1 | `89d6d8167d11`  |
| 2196   | Layout 1 | `89d6d8167d11`  |
| 2192   | Layout 1 | `89d6d8167d11`  |
| 2189   | Layout 1 | `89d6d8167d11`  |
| 2183   | Layout 1 | `89d6d8167d11`  |
| 2179   | Layout 1 | `89d6d8167d11`  |
| 2171   | Layout 1 | `89d6d8167d11`  |
| 2163   | Layout 1 | `89d6d8167d11`  |
| 2156   | Layout 1 | `89d6d8167d11`  |
| 2151   | Layout 1 | `89d6d8167d11`  |
| 2147   | Layout 1 | `89d6d8167d11`  |
| 2142   | Layout 1 | `89d6d8167d11`  |
| 2138   | Layout 1 | `89d6d8167d11`  |
| 2134   | Layout 1 | `89d6d8167d11`  |
| 2130   | Layout 1 | `89d6d8167d11`  |
| 2122   | Layout 1 | `89d6d8167d11`  |
| 2107   | Layout 1 | `89d6d8167d11`  |
| 2098   | Layout 1 | `89d6d8167d11`  |
| 2089   | Layout 1 | `89d6d8167d11`  |
| 2081   | Layout 1 | `89d6d8167d11`  |
| 2073   | Layout 1 | `89d6d8167d11`  |
| 2067   | Layout 1 | `89d6d8167d11`  |
| 2063   | Layout 1 | `89d6d8167d11`  |
| 2059   | Layout 1 | `89d6d8167d11`  |
| 2052   | Layout 1 | `89d6d8167d11`  |
| 2044   | Layout 1 | `89d6d8167d11`  |
| 2039   | Layout 1 | `89d6d8167d11`  |
| 2032   | Layout 1 | `89d6d8167d11`  |
| 2025   | Layout 1 | `89d6d8167d11`  |
| 2011   | Layout 1 | `89d6d8167d11`  |
| 2005   | Layout 1 | `89d6d8167d11`  |
| 2000   | Layout 1 | `89d6d8167d11`  |
| 1996   | Layout 1 | `89d6d8167d11`  |
| 1991   | Layout 1 | `89d6d8167d11`  |
| 1985   | Layout 1 | `89d6d8167d11`  |
| 1980   | Layout 1 | `89d6d8167d11`  |
| 1969   | Layout 1 | `89d6d8167d11`  |
| 1964   | Layout 1 | `89d6d8167d11`  |
| 1958   | Layout 1 | `89d6d8167d11`  |
| 1950   | Layout 1 | `89d6d8167d11`  |
| 1945   | Layout 1 | `89d6d8167d11`  |
| 1937   | Layout 1 | `89d6d8167d11`  |
| 1933   | Layout 1 | `89d6d8167d11`  |
| 1927   | Layout 1 | `89d6d8167d11`  |
| 1921   | Layout 1 | `89d6d8167d11`  |
| 1914   | Layout 1 | `89d6d8167d11`  |
| 1908   | Layout 1 | `89d6d8167d11`  |
| 1897   | Layout 1 | `89d6d8167d11`  |
| 1892   | Layout 1 | `89d6d8167d11`  |
| 1886   | Layout 1 | `89d6d8167d11`  |
| 1881   | Layout 1 | `89d6d8167d11`  |
| 1871   | Layout 1 | `89d6d8167d11`  |
| 1866   | Layout 1 | `89d6d8167d11`  |
| 1862   | Layout 1 | `89d6d8167d11`  |
| 1854   | Layout 1 | `89d6d8167d11`  |
| 1846   | Layout 1 | `89d6d8167d11`  |
| 1838   | Layout 1 | `89d6d8167d11`  |
| 1832   | Layout 1 | `89d6d8167d11`  |
| 1826   | Layout 1 | `89d6d8167d11`  |
| 1822   | Layout 1 | `89d6d8167d11`  |
| 1818   | Layout 1 | `89d6d8167d11`  |
| 1804   | Layout 1 | `89d6d8167d11`  |
| 1794   | Layout 1 | `89d6d8167d11`  |
| 1790   | Layout 1 | `89d6d8167d11`  |
| 1784   | Layout 1 | `89d6d8167d11`  |
| 1774   | Layout 1 | `89d6d8167d11`  |
| 1771   | Layout 1 | `89d6d8167d11`  |
| 1762   | Layout 1 | `89d6d8167d11`  |
| 1759   | Layout 1 | `89d6d8167d11`  |
| 1754   | Layout 1 | `89d6d8167d11`  |
| 1749   | Layout 1 | `89d6d8167d11`  |
| 1743   | Layout 1 | `89d6d8167d11`  |
| 1737   | Layout 1 | `89d6d8167d11`  |
| 1731   | Layout 1 | `89d6d8167d11`  |
| 1725   | Layout 1 | `89d6d8167d11`  |
| 1717   | Layout 1 | `89d6d8167d11`  |
| 1710   | Layout 1 | `89d6d8167d11`  |
| 1704   | Layout 1 | `89d6d8167d11`  |
| 1698   | Layout 1 | `89d6d8167d11`  |
| 1690   | Layout 1 | `89d6d8167d11`  |
| 1685   | Layout 1 | `89d6d8167d11`  |
| 1680   | Layout 1 | `89d6d8167d11`  |
| 1674   | Layout 1 | `89d6d8167d11`  |
| 1668   | Layout 1 | `89d6d8167d11`  |
| 1659   | Layout 1 | `89d6d8167d11`  |
| 1649   | Layout 1 | `89d6d8167d11`  |
| 1642   | Layout 1 | `89d6d8167d11`  |
| 1636   | Layout 1 | `89d6d8167d11`  |
| 1628   | Layout 1 | `89d6d8167d11`  |
| 1622   | Layout 1 | `89d6d8167d11`  |
| 1614   | Layout 1 | `89d6d8167d11`  |
| 1608   | Layout 1 | `89d6d8167d11`  |
| 1602   | Layout 1 | `89d6d8167d11`  |
| 1598   | Layout 1 | `89d6d8167d11`  |
| 1594   | Layout 1 | `89d6d8167d11`  |
| 1590   | Layout 1 | `89d6d8167d11`  |
| 1587   | Layout 1 | `89d6d8167d11`  |
| 1584   | Layout 1 | `89d6d8167d11`  |
| 1579   | Layout 1 | `89d6d8167d11`  |
| 1572   | Layout 1 | `89d6d8167d11`  |
| 1565   | Layout 1 | `89d6d8167d11`  |
| 1559   | Layout 1 | `89d6d8167d11`  |
| 1554   | Layout 1 | `89d6d8167d11`  |
| 1547   | Layout 1 | `89d6d8167d11`  |
| 1537   | Layout 1 | `89d6d8167d11`  |
| 1529   | Layout 1 | `89d6d8167d11`  |
| 1524   | Layout 1 | `89d6d8167d11`  |
| 1519   | Layout 1 | `89d6d8167d11`  |
| 1509   | Layout 1 | `89d6d8167d11`  |
| 1506   | Layout 1 | `89d6d8167d11`  |
| 1504   | Layout 1 | `89d6d8167d11`  |
| 1500   | Layout 1 | `89d6d8167d11`  |
| 1493   | Layout 1 | `89d6d8167d11`  |
| 1489   | Layout 1 | `89d6d8167d11`  |
| 1485   | Layout 1 | `89d6d8167d11`  |
| 1481   | Layout 1 | `89d6d8167d11`  |
| 1474   | Layout 1 | `89d6d8167d11`  |
| 1466   | Layout 1 | `89d6d8167d11`  |
| 1462   | Layout 1 | `89d6d8167d11`  |
| 1459   | Layout 1 | `89d6d8167d11`  |
| 1453   | Layout 1 | `89d6d8167d11`  |
| 1450   | Layout 1 | `89d6d8167d11`  |
| 1445   | Layout 1 | `89d6d8167d11`  |
| 1439   | Layout 1 | `89d6d8167d11`  |
| 1433   | Layout 1 | `89d6d8167d11`  |
| 1430   | Layout 1 | `89d6d8167d11`  |
| 1426   | Layout 1 | `89d6d8167d11`  |
| 1421   | Layout 1 | `89d6d8167d11`  |
| 1417   | Layout 1 | `89d6d8167d11`  |
| 1416   | Layout 1 | `89d6d8167d11`  |
| 1409   | Layout 1 | `89d6d8167d11`  |
| 1405   | Layout 1 | `89d6d8167d11`  |
| 1401   | Layout 1 | `89d6d8167d11`  |
| 1396   | Layout 1 | `89d6d8167d11`  |
| 1391   | Layout 1 | `89d6d8167d11`  |
| 1390   | Layout 1 | `89d6d8167d11`  |
| 1386   | Layout 1 | `89d6d8167d11`  |
| 1381   | Layout 1 | `89d6d8167d11`  |
| 1379   | Layout 1 | `89d6d8167d11`  |
| 1372   | Layout 1 | `89d6d8167d11`  |
| 1366   | Layout 1 | `89d6d8167d11`  |
| 1364   | Layout 1 | `89d6d8167d11`  |
| 1363   | Layout 1 | `89d6d8167d11`  |
| 1360   | Layout 1 | `89d6d8167d11`  |
| 1358   | Layout 1 | `89d6d8167d11`  |
| 1355   | Layout 1 | `89d6d8167d11`  |
| 1351   | Layout 1 | `89d6d8167d11`  |
| 1348   | Layout 1 | `89d6d8167d11`  |
| 1346   | Layout 1 | `89d6d8167d11`  |
| 1341   | Layout 1 | `89d6d8167d11`  |
| 1340   | Layout 1 | `89d6d8167d11`  |
| 1338   | Layout 1 | `89d6d8167d11`  |
| 1335   | Layout 1 | `89d6d8167d11`  |
| 1333   | Layout 1 | `89d6d8167d11`  |
| 1329   | Layout 1 | `89d6d8167d11`  |
| 1327   | Layout 1 | `89d6d8167d11`  |
| 1324   | Layout 1 | `89d6d8167d11`  |
| 1321   | Layout 1 | `89d6d8167d11`  |
| 1319   | Layout 1 | `89d6d8167d11`  |
| 1318   | Layout 1 | `89d6d8167d11`  |
| 1316   | Layout 1 | `89d6d8167d11`  |
| 1313   | Layout 1 | `89d6d8167d11`  |
| 1311   | Layout 1 | `89d6d8167d11`  |
| 1309   | Layout 1 | `89d6d8167d11`  |
| 1304   | Layout 1 | `89d6d8167d11`  |
| 1292   | Layout 1 | `89d6d8167d11`  |
| 1286   | Layout 1 | `89d6d8167d11`  |
| 1280   | Layout 1 | `89d6d8167d11`  |
| 1276   | Layout 1 | `89d6d8167d11`  |
| 1267   | Layout 1 | `89d6d8167d11`  |
| 1261   | No file  | `89d6d8167d11`  |
| 1256   | No file  | `89d6d8167d11`  |
| 1250   | No file  | `89d6d8167d11`  |
| 1246   | No file  | `89d6d8167d11`  |
| 1239   | No file  | `89d6d8167d11`  |
| 1230   | No file  | `89d6d8167d11`  |
| 1226   | No file  | `89d6d8167d11`  |
| 1220   | No file  | `89d6d8167d11`  |
| 1217   | No file  | `89d6d8167d11`  |
| 1211   | No file  | `89d6d8167d11`  |
| 1210   | No file  | `89d6d8167d11`  |
| 1208   | No file  | `89d6d8167d11`  |
| 1203   | No file  | `89d6d8167d11`  |
| 1197   | No file  | `89d6d8167d11`  |
| 1194   | No file  | `89d6d8167d11`  |
| 1192   | No file  | `89d6d8167d11`  |
| 1187   | No file  | `89d6d8167d11`  |
| 1183   | No file  | `89d6d8167d11`  |
| 1177   | No file  | `89d6d8167d11`  |
| 1173   | No file  | `89d6d8167d11`  |
| 1167   | No file  | `89d6d8167d11`  |
| 1164   | No file  | `89d6d8167d11`  |
| 1156   | No file  | `89d6d8167d11`  |
| 1149   | No file  | `89d6d8167d11`  |
| 1144   | No file  | `89d6d8167d11`  |
| 1137   | No file  | `89d6d8167d11`  |
| 1132   | No file  | `89d6d8167d11`  |
| 1127   | No file  | `89d6d8167d11`  |
| 1122   | No file  | `89d6d8167d11`  |
| 1118   | No file  | `89d6d8167d11`  |
| 1114   | No file  | `89d6d8167d11`  |
| 1109   | No file  | `89d6d8167d11`  |
| 1102   | No file  | `89d6d8167d11`  |
| 1096   | No file  | `89d6d8167d11`  |
| 1088   | No file  | `89d6d8167d11`  |
| 1081   | No file  | `89d6d8167d11`  |
| 1076   | No file  | `89d6d8167d11`  |
| 1069   | No file  | `89d6d8167d11`  |
| 1064   | No file  | `89d6d8167d11`  |
| 1058   | No file  | `89d6d8167d11`  |
| 1051   | No file  | `89d6d8167d11`  |
| 1044   | No file  | `89d6d8167d11`  |
| 1036   | No file  | `89d6d8167d11`  |
| 1026   | No file  | `89d6d8167d11`  |
| 1016   | No file  | `89d6d8167d11`  |
| 1009   | No file  | `89d6d8167d11`  |
| 1005   | No file  | `89d6d8167d11`  |
| 1000   | No file  | `89d6d8167d11`  |
| 998    | No file  | `89d6d8167d11`  |
| 990    | No file  | `89d6d8167d11`  |
| 979    | No file  | `89d6d8167d11`  |
| 972    | No file  | `89d6d8167d11`  |
| 963    | No file  | `89d6d8167d11`  |
| 955    | No file  | `89d6d8167d11`  |
| 946    | No file  | `89d6d8167d11`  |
| 938    | No file  | `89d6d8167d11`  |
| 927    | No file  | `89d6d8167d11`  |
| 911    | No file  | `89d6d8167d11`  |
| 904    | No file  | `89d6d8167d11`  |
| 899    | No file  | `89d6d8167d11`  |
| 894    | No file  | `89d6d8167d11`  |
| 885    | No file  | `89d6d8167d11`  |
| 879    | No file  | `89d6d8167d11`  |
| 872    | No file  | `89d6d8167d11`  |
| 864    | No file  | `89d6d8167d11`  |
| 855    | No file  | `89d6d8167d11`  |
| 853    | No file  | `89d6d8167d11`  |
| 845    | No file  | `89d6d8167d11`  |
| 837    | No file  | `89d6d8167d11`  |
| 829    | No file  | `89d6d8167d11`  |
| 822    | No file  | `89d6d8167d11`  |
| 814    | No file  | `89d6d8167d11`  |
| 805    | No file  | `89d6d8167d11`  |
| 794    | No file  | `89d6d8167d11`  |
| 787    | No file  | `89d6d8167d11`  |
| 780    | No file  | `89d6d8167d11`  |
| 771    | No file  | `89d6d8167d11`  |
| 760    | No file  | `89d6d8167d11`  |
| 748    | No file  | `89d6d8167d11`  |
| 741    | No file  | `89d6d8167d11`  |
| 736    | No file  | `89d6d8167d11`  |
| 731    | No file  | `89d6d8167d11`  |
| 723    | No file  | `89d6d8167d11`  |
| 711    | No file  | `89d6d8167d11`  |
| 707    | No file  | `89d6d8167d11`  |
| 697    | No file  | `89d6d8167d11`  |
| 689    | No file  | `89d6d8167d11`  |
| 683    | No file  | `89d6d8167d11`  |
| 678    | No file  | `89d6d8167d11`  |
| 670    | No file  | `89d6d8167d11`  |
| 661    | No file  | `89d6d8167d11`  |
| 656    | No file  | `89d6d8167d11`  |
| 652    | No file  | `89d6d8167d11`  |
| 643    | No file  | `89d6d8167d11`  |
| 637    | No file  | `89d6d8167d11`  |
| 630    | No file  | `89d6d8167d11`  |
| 627    | No file  | `89d6d8167d11`  |
| 621    | No file  | `89d6d8167d11`  |
| 617    | No file  | `89d6d8167d11`  |
| 615    | No file  | `89d6d8167d11`  |
| 606    | No file  | `89d6d8167d11`  |
| 599    | No file  | `89d6d8167d11`  |
| 592    | No file  | `89d6d8167d11`  |
| 586    | No file  | `89d6d8167d11`  |
| 577    | No file  | `89d6d8167d11`  |
| 569    | No file  | `89d6d8167d11`  |
| 561    | No file  | `89d6d8167d11`  |
| 554    | No file  | `89d6d8167d11`  |
| 542    | No file  | `89d6d8167d11`  |
| 532    | No file  | `89d6d8167d11`  |
| 531    | No file  | `89d6d8167d11`  |
| 526    | No file  | `89d6d8167d11`  |
| 521    | No file  | `89d6d8167d11`  |
| 517    | No file  | `89d6d8167d11`  |
| 510    | No file  | `89d6d8167d11`  |
| 508    | No file  | `89d6d8167d11`  |
| 504    | No file  | `89d6d8167d11`  |
| 497    | No file  | `89d6d8167d11`  |
| 491    | No file  | `89d6d8167d11`  |
| 485    | No file  | `89d6d8167d11`  |
| 478    | No file  | `89d6d8167d11`  |
| 472    | No file  | `89d6d8167d11`  |
| 466    | No file  | `89d6d8167d11`  |
| 457    | No file  | `89d6d8167d11`  |
| 452    | No file  | `89d6d8167d11`  |
| 449    | No file  | `89d6d8167d11`  |
| 435    | No file  | `89d6d8167d11`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role |
| ---------------------- | -------- | ---- |
| `setoptionoffset.dbss` | Optional | `set_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type       | Field | Notes                                |
| ------- | ---------- | ----- | ------------------------------------ |
| `+0x00` | u32        | count | Number of sets; `75` on client 3482  |
| `+0x04` | Row[count] | rows  | See Row                              |

### Row (variable: 134 bytes + item lists)

Slot `n` (from `1`) of `skill_keys` and `points` is the effect of `n`
equipped pieces.

| Offset                    | Type                        | Field              | Notes |
| ------------------------- | --------------------------- | ------------------ | ----- |
| `+0x00`                   | u16                         | set_key            | Set key, `1` to `75` on client 3482 |
| `+0x02`                   | u32                         | set_option_type    | `0` gear set (29 rows), `1` furniture set (46 rows) |
| `+0x06`                   | u32[14]                     | skill_keys         | Skill key per piece count, `skill_no << 16 \| level`; level `1` on every filled slot, all zero on furniture sets |
| `+0x3E`                   | u64                         | equip_count        | Number of gear pieces; `0` on furniture sets |
| `+0x46`                   | u32[equip_count]            | equip_items        | Item IDs of the gear pieces |
| `equip_items+0x00`        | u64                         | installation_count | Number of furniture pieces; `0` on gear sets |
| `equip_items+0x08`        | u32[installation_count]     | installation_items | Item IDs of the furniture pieces |
| `installation_items+0x00` | i32[14]                     | points             | Interior points per piece count (`100` to `500`); all zero on gear sets |

### `setoptionoffset.dbss`

Bare offset table into `setoption.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `setoption.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                |
| ------- | ---- | ----------- | ---------------------------------------------------- |
| `+0x00` | u16  | set_key     | Key of the row it points at                          |
| `+0x02` | u32  | data_offset | Absolute offset of the row in `setoption.dbss`       |
| `+0x06` | u32  | data_size   | Row size in bytes                                    |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in key order; on clients 1784 and 3482 every one points at the
row with its key and the rows tile the file.

## Field Names

The 2016 `gc::SetOptionStaticStatus` has the members `_setOptionType`,
`_key`, `_skillKeyList` (14 `gc::SkillKey`), `_equipList`,
`_InstallationList` and `_pointList` (14 `int`), in that order; the file
stores them in the order key, type, then the rest. The `EquipSetOption`
sheet of a private server's `DataSheets.bexcel` on client 1784 matches 74
of 74 rows of the client 1784 file and the 74 shared keys of client 3482
(key `75` is newer): `SetType` is `set_option_type`, `Set_N_Option` is the
skill number in slot `N` of a gear set and the points in slot `N` of a
furniture set, and `Equip_1` to `Equip_40` are `equip_items` of a gear set
and `installation_items` of a furniture set.

## Notes

- Every set fills one slot, except one furniture set with `500` points at
  nine pieces and `300` at fourteen. On client 3482, 21 gear sets give
  skill `53265` at four pieces and 8 another skill at three; 32 furniture
  sets give `500` points at nine pieces.
- The sheet's `EquipSetOptionName` is not in the file.
