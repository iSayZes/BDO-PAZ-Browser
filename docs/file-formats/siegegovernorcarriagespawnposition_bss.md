# `siegegovernorcarriagespawnposition.bss` Format

## Purpose

The spawn positions of the Conquest War supply wagon: rows of an index
and a world position. The `spawn_position_list` of
[`siegegovernorcarriagespawn.bss`](siegegovernorcarriagespawn_bss.md)
points at the indexes. Client 3482 has nine rows, three positions repeated
three times.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                     | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------------------------------- | ----- | ------- | --------- |
| 1      | 1743 and later | `siegegovernorcarriagespawnposition.bss` | 164   | 9 Row   | 16        |

| Layout | File                                     | Known          | Unknown    |
| ------ | ---------------------------------------- | -------------- | ---------- |
| 1      | `siegegovernorcarriagespawnposition.bss` | 164 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d2bb777a0ab0`  |
| 3482   | Layout 1 | `d2bb777a0ab0`  |
| 3474   | Layout 1 | `d2bb777a0ab0`  |
| 3473   | Layout 1 | `d2bb777a0ab0`  |
| 3464   | Layout 1 | `d2bb777a0ab0`  |
| 3458   | Layout 1 | `d2bb777a0ab0`  |
| 3454   | Layout 1 | `d2bb777a0ab0`  |
| 3444   | Layout 1 | `d2bb777a0ab0`  |
| 3435   | Layout 1 | `d2bb777a0ab0`  |
| 3426   | Layout 1 | `d2bb777a0ab0`  |
| 3418   | Layout 1 | `d2bb777a0ab0`  |
| 3412   | Layout 1 | `d2bb777a0ab0`  |
| 3402   | Layout 1 | `d2bb777a0ab0`  |
| 3396   | Layout 1 | `d2bb777a0ab0`  |
| 3387   | Layout 1 | `d2bb777a0ab0`  |
| 3381   | Layout 1 | `d2bb777a0ab0`  |
| 3373   | Layout 1 | `d2bb777a0ab0`  |
| 3364   | Layout 1 | `d2bb777a0ab0`  |
| 3356   | Layout 1 | `d2bb777a0ab0`  |
| 3349   | Layout 1 | `d2bb777a0ab0`  |
| 3342   | Layout 1 | `d2bb777a0ab0`  |
| 3335   | Layout 1 | `d2bb777a0ab0`  |
| 3326   | Layout 1 | `d2bb777a0ab0`  |
| 3321   | Layout 1 | `d2bb777a0ab0`  |
| 3314   | Layout 1 | `d2bb777a0ab0`  |
| 3303   | Layout 1 | `d2bb777a0ab0`  |
| 3302   | Layout 1 | `d2bb777a0ab0`  |
| 3293   | Layout 1 | `d2bb777a0ab0`  |
| 3283   | Layout 1 | `d2bb777a0ab0`  |
| 3275   | Layout 1 | `d2bb777a0ab0`  |
| 3267   | Layout 1 | `d2bb777a0ab0`  |
| 3258   | Layout 1 | `d2bb777a0ab0`  |
| 3251   | Layout 1 | `d2bb777a0ab0`  |
| 3242   | Layout 1 | `d2bb777a0ab0`  |
| 3235   | Layout 1 | `d2bb777a0ab0`  |
| 3229   | Layout 1 | `d2bb777a0ab0`  |
| 3212   | Layout 1 | `d2bb777a0ab0`  |
| 3203   | Layout 1 | `d2bb777a0ab0`  |
| 3193   | Layout 1 | `d2bb777a0ab0`  |
| 3186   | Layout 1 | `d2bb777a0ab0`  |
| 3177   | Layout 1 | `d2bb777a0ab0`  |
| 3169   | Layout 1 | `d2bb777a0ab0`  |
| 3158   | Layout 1 | `d2bb777a0ab0`  |
| 3151   | Layout 1 | `d2bb777a0ab0`  |
| 3144   | Layout 1 | `d2bb777a0ab0`  |
| 3133   | Layout 1 | `d2bb777a0ab0`  |
| 3125   | Layout 1 | `d2bb777a0ab0`  |
| 3118   | Layout 1 | `d2bb777a0ab0`  |
| 3111   | Layout 1 | `d2bb777a0ab0`  |
| 3103   | Layout 1 | `d2bb777a0ab0`  |
| 3095   | Layout 1 | `d2bb777a0ab0`  |
| 3086   | Layout 1 | `d2bb777a0ab0`  |
| 3072   | Layout 1 | `d2bb777a0ab0`  |
| 3062   | Layout 1 | `d2bb777a0ab0`  |
| 3052   | Layout 1 | `d2bb777a0ab0`  |
| 3045   | Layout 1 | `d2bb777a0ab0`  |
| 3037   | Layout 1 | `d2bb777a0ab0`  |
| 3030   | Layout 1 | `d2bb777a0ab0`  |
| 3021   | Layout 1 | `d2bb777a0ab0`  |
| 3012   | Layout 1 | `d2bb777a0ab0`  |
| 3002   | Layout 1 | `d2bb777a0ab0`  |
| 2995   | Layout 1 | `d2bb777a0ab0`  |
| 2987   | Layout 1 | `d2bb777a0ab0`  |
| 2978   | Layout 1 | `d2bb777a0ab0`  |
| 2970   | Layout 1 | `d2bb777a0ab0`  |
| 2959   | Layout 1 | `d2bb777a0ab0`  |
| 2951   | Layout 1 | `d2bb777a0ab0`  |
| 2942   | Layout 1 | `d2bb777a0ab0`  |
| 2935   | Layout 1 | `d2bb777a0ab0`  |
| 2932   | Layout 1 | `d2bb777a0ab0`  |
| 2923   | Layout 1 | `d2bb777a0ab0`  |
| 2919   | Layout 1 | `d2bb777a0ab0`  |
| 2907   | Layout 1 | `d2bb777a0ab0`  |
| 2900   | Layout 1 | `d2bb777a0ab0`  |
| 2891   | Layout 1 | `d2bb777a0ab0`  |
| 2882   | Layout 1 | `d2bb777a0ab0`  |
| 2872   | Layout 1 | `d2bb777a0ab0`  |
| 2863   | Layout 1 | `d2bb777a0ab0`  |
| 2855   | Layout 1 | `d2bb777a0ab0`  |
| 2849   | Layout 1 | `d2bb777a0ab0`  |
| 2844   | Layout 1 | `d2bb777a0ab0`  |
| 2834   | Layout 1 | `d2bb777a0ab0`  |
| 2825   | Layout 1 | `d2bb777a0ab0`  |
| 2819   | Layout 1 | `d2bb777a0ab0`  |
| 2811   | Layout 1 | `d2bb777a0ab0`  |
| 2803   | Layout 1 | `d2bb777a0ab0`  |
| 2794   | Layout 1 | `d2bb777a0ab0`  |
| 2783   | Layout 1 | `d2bb777a0ab0`  |
| 2774   | Layout 1 | `d2bb777a0ab0`  |
| 2765   | Layout 1 | `d2bb777a0ab0`  |
| 2756   | Layout 1 | `d2bb777a0ab0`  |
| 2750   | Layout 1 | `d2bb777a0ab0`  |
| 2743   | Layout 1 | `d2bb777a0ab0`  |
| 2736   | Layout 1 | `d2bb777a0ab0`  |
| 2726   | Layout 1 | `d2bb777a0ab0`  |
| 2717   | Layout 1 | `d2bb777a0ab0`  |
| 2709   | Layout 1 | `d2bb777a0ab0`  |
| 2703   | Layout 1 | `d2bb777a0ab0`  |
| 2695   | Layout 1 | `d2bb777a0ab0`  |
| 2684   | Layout 1 | `d2bb777a0ab0`  |
| 2672   | Layout 1 | `d2bb777a0ab0`  |
| 2665   | Layout 1 | `d2bb777a0ab0`  |
| 2657   | Layout 1 | `d2bb777a0ab0`  |
| 2649   | Layout 1 | `d2bb777a0ab0`  |
| 2644   | Layout 1 | `d2bb777a0ab0`  |
| 2637   | Layout 1 | `d2bb777a0ab0`  |
| 2629   | Layout 1 | `d2bb777a0ab0`  |
| 2619   | Layout 1 | `d2bb777a0ab0`  |
| 2612   | Layout 1 | `d2bb777a0ab0`  |
| 2606   | Layout 1 | `d2bb777a0ab0`  |
| 2602   | Layout 1 | `d2bb777a0ab0`  |
| 2601   | Layout 1 | `d2bb777a0ab0`  |
| 2592   | Layout 1 | `d2bb777a0ab0`  |
| 2583   | Layout 1 | `d2bb777a0ab0`  |
| 2575   | Layout 1 | `d2bb777a0ab0`  |
| 2567   | Layout 1 | `d2bb777a0ab0`  |
| 2560   | Layout 1 | `d2bb777a0ab0`  |
| 2553   | Layout 1 | `d2bb777a0ab0`  |
| 2545   | Layout 1 | `d2bb777a0ab0`  |
| 2538   | Layout 1 | `d2bb777a0ab0`  |
| 2529   | Layout 1 | `d2bb777a0ab0`  |
| 2519   | Layout 1 | `d2bb777a0ab0`  |
| 2513   | Layout 1 | `d2bb777a0ab0`  |
| 2510   | Layout 1 | `d2bb777a0ab0`  |
| 2507   | Layout 1 | `d2bb777a0ab0`  |
| 2503   | Layout 1 | `d2bb777a0ab0`  |
| 2498   | Layout 1 | `d2bb777a0ab0`  |
| 2492   | Layout 1 | `d2bb777a0ab0`  |
| 2487   | Layout 1 | `d2bb777a0ab0`  |
| 2480   | Layout 1 | `d2bb777a0ab0`  |
| 2474   | Layout 1 | `d2bb777a0ab0`  |
| 2468   | Layout 1 | `d2bb777a0ab0`  |
| 2460   | Layout 1 | `d2bb777a0ab0`  |
| 2453   | Layout 1 | `d2bb777a0ab0`  |
| 2444   | Layout 1 | `d2bb777a0ab0`  |
| 2438   | Layout 1 | `d2bb777a0ab0`  |
| 2434   | Layout 1 | `d2bb777a0ab0`  |
| 2429   | Layout 1 | `d2bb777a0ab0`  |
| 2421   | Layout 1 | `d2bb777a0ab0`  |
| 2414   | Layout 1 | `d2bb777a0ab0`  |
| 2407   | Layout 1 | `d2bb777a0ab0`  |
| 2401   | Layout 1 | `d2bb777a0ab0`  |
| 2397   | Layout 1 | `d2bb777a0ab0`  |
| 2393   | Layout 1 | `d2bb777a0ab0`  |
| 2384   | Layout 1 | `d2bb777a0ab0`  |
| 2378   | Layout 1 | `d2bb777a0ab0`  |
| 2372   | Layout 1 | `d2bb777a0ab0`  |
| 2358   | Layout 1 | `d2bb777a0ab0`  |
| 2352   | Layout 1 | `d2bb777a0ab0`  |
| 2347   | Layout 1 | `d2bb777a0ab0`  |
| 2343   | Layout 1 | `d2bb777a0ab0`  |
| 2335   | Layout 1 | `d2bb777a0ab0`  |
| 2327   | Layout 1 | `d2bb777a0ab0`  |
| 2324   | Layout 1 | `d2bb777a0ab0`  |
| 2319   | Layout 1 | `d2bb777a0ab0`  |
| 2313   | Layout 1 | `d2bb777a0ab0`  |
| 2308   | Layout 1 | `d2bb777a0ab0`  |
| 2302   | Layout 1 | `d2bb777a0ab0`  |
| 2295   | Layout 1 | `d2bb777a0ab0`  |
| 2290   | Layout 1 | `d2bb777a0ab0`  |
| 2284   | Layout 1 | `d2bb777a0ab0`  |
| 2276   | Layout 1 | `d2bb777a0ab0`  |
| 2269   | Layout 1 | `d2bb777a0ab0`  |
| 2259   | Layout 1 | `d2bb777a0ab0`  |
| 2250   | Layout 1 | `d2bb777a0ab0`  |
| 2243   | Layout 1 | `d2bb777a0ab0`  |
| 2235   | Layout 1 | `d2bb777a0ab0`  |
| 2229   | Layout 1 | `d2bb777a0ab0`  |
| 2224   | Layout 1 | `d2bb777a0ab0`  |
| 2218   | Layout 1 | `d2bb777a0ab0`  |
| 2215   | Layout 1 | `d2bb777a0ab0`  |
| 2207   | Layout 1 | `d2bb777a0ab0`  |
| 2203   | Layout 1 | `d2bb777a0ab0`  |
| 2196   | Layout 1 | `d2bb777a0ab0`  |
| 2192   | Layout 1 | `d2bb777a0ab0`  |
| 2189   | Layout 1 | `d2bb777a0ab0`  |
| 2183   | Layout 1 | `d2bb777a0ab0`  |
| 2179   | Layout 1 | `d2bb777a0ab0`  |
| 2171   | Layout 1 | `d2bb777a0ab0`  |
| 2163   | Layout 1 | `d2bb777a0ab0`  |
| 2156   | Layout 1 | `d2bb777a0ab0`  |
| 2151   | Layout 1 | `d2bb777a0ab0`  |
| 2147   | Layout 1 | `d2bb777a0ab0`  |
| 2142   | Layout 1 | `d2bb777a0ab0`  |
| 2138   | Layout 1 | `d2bb777a0ab0`  |
| 2134   | Layout 1 | `d2bb777a0ab0`  |
| 2130   | Layout 1 | `d2bb777a0ab0`  |
| 2122   | Layout 1 | `d2bb777a0ab0`  |
| 2107   | Layout 1 | `d2bb777a0ab0`  |
| 2098   | Layout 1 | `d2bb777a0ab0`  |
| 2089   | Layout 1 | `d2bb777a0ab0`  |
| 2081   | Layout 1 | `d2bb777a0ab0`  |
| 2073   | Layout 1 | `d2bb777a0ab0`  |
| 2067   | Layout 1 | `d2bb777a0ab0`  |
| 2063   | Layout 1 | `d2bb777a0ab0`  |
| 2059   | Layout 1 | `d2bb777a0ab0`  |
| 2052   | Layout 1 | `d2bb777a0ab0`  |
| 2044   | Layout 1 | `d2bb777a0ab0`  |
| 2039   | Layout 1 | `d2bb777a0ab0`  |
| 2032   | Layout 1 | `d2bb777a0ab0`  |
| 2025   | Layout 1 | `d2bb777a0ab0`  |
| 2011   | Layout 1 | `d2bb777a0ab0`  |
| 2005   | Layout 1 | `d2bb777a0ab0`  |
| 2000   | Layout 1 | `d2bb777a0ab0`  |
| 1996   | Layout 1 | `d2bb777a0ab0`  |
| 1991   | Layout 1 | `d2bb777a0ab0`  |
| 1985   | Layout 1 | `d2bb777a0ab0`  |
| 1980   | Layout 1 | `d2bb777a0ab0`  |
| 1969   | Layout 1 | `d2bb777a0ab0`  |
| 1964   | Layout 1 | `d2bb777a0ab0`  |
| 1958   | Layout 1 | `d2bb777a0ab0`  |
| 1950   | Layout 1 | `d2bb777a0ab0`  |
| 1945   | Layout 1 | `d2bb777a0ab0`  |
| 1937   | Layout 1 | `d2bb777a0ab0`  |
| 1933   | Layout 1 | `d2bb777a0ab0`  |
| 1927   | Layout 1 | `d2bb777a0ab0`  |
| 1921   | Layout 1 | `d2bb777a0ab0`  |
| 1914   | Layout 1 | `d2bb777a0ab0`  |
| 1908   | Layout 1 | `d2bb777a0ab0`  |
| 1897   | Layout 1 | `d2bb777a0ab0`  |
| 1892   | Layout 1 | `d2bb777a0ab0`  |
| 1886   | Layout 1 | `d2bb777a0ab0`  |
| 1881   | Layout 1 | `d2bb777a0ab0`  |
| 1871   | Layout 1 | `d2bb777a0ab0`  |
| 1866   | Layout 1 | `d2bb777a0ab0`  |
| 1862   | Layout 1 | `d2bb777a0ab0`  |
| 1854   | Layout 1 | `d2bb777a0ab0`  |
| 1846   | Layout 1 | `d2bb777a0ab0`  |
| 1838   | Layout 1 | `d2bb777a0ab0`  |
| 1832   | Layout 1 | `d2bb777a0ab0`  |
| 1826   | Layout 1 | `d2bb777a0ab0`  |
| 1822   | Layout 1 | `d2bb777a0ab0`  |
| 1818   | Layout 1 | `d2bb777a0ab0`  |
| 1804   | Layout 1 | `d2bb777a0ab0`  |
| 1794   | Layout 1 | `d2bb777a0ab0`  |
| 1790   | Layout 1 | `d2bb777a0ab0`  |
| 1784   | Layout 1 | `d2bb777a0ab0`  |
| 1774   | Layout 1 | `d2bb777a0ab0`  |
| 1771   | Layout 1 | `d2bb777a0ab0`  |
| 1762   | Layout 1 | `d2bb777a0ab0`  |
| 1759   | Layout 1 | `d2bb777a0ab0`  |
| 1754   | Layout 1 | `d2bb777a0ab0`  |
| 1749   | Layout 1 | `d2bb777a0ab0`  |
| 1743   | Layout 1 | `d2bb777a0ab0`  |
| 1737   | No file  | `d2bb777a0ab0`  |
| 1731   | No file  | `d2bb777a0ab0`  |
| 1725   | No file  | `d2bb777a0ab0`  |
| 1717   | No file  | `d2bb777a0ab0`  |
| 1710   | No file  | `d2bb777a0ab0`  |
| 1704   | No file  | `d2bb777a0ab0`  |
| 1698   | No file  | `d2bb777a0ab0`  |
| 1690   | No file  | `d2bb777a0ab0`  |
| 1685   | No file  | `d2bb777a0ab0`  |
| 1680   | No file  | `d2bb777a0ab0`  |
| 1674   | No file  | `d2bb777a0ab0`  |
| 1668   | No file  | `d2bb777a0ab0`  |
| 1659   | No file  | `d2bb777a0ab0`  |
| 1649   | No file  | `d2bb777a0ab0`  |
| 1642   | No file  | `d2bb777a0ab0`  |
| 1636   | No file  | `d2bb777a0ab0`  |
| 1628   | No file  | `d2bb777a0ab0`  |
| 1622   | No file  | `d2bb777a0ab0`  |
| 1614   | No file  | `d2bb777a0ab0`  |
| 1608   | No file  | `d2bb777a0ab0`  |
| 1602   | No file  | `d2bb777a0ab0`  |
| 1598   | No file  | `d2bb777a0ab0`  |
| 1594   | No file  | `d2bb777a0ab0`  |
| 1590   | No file  | `d2bb777a0ab0`  |
| 1587   | No file  | `d2bb777a0ab0`  |
| 1584   | No file  | `d2bb777a0ab0`  |
| 1579   | No file  | `d2bb777a0ab0`  |
| 1572   | No file  | `d2bb777a0ab0`  |
| 1565   | No file  | `d2bb777a0ab0`  |
| 1559   | No file  | `d2bb777a0ab0`  |
| 1554   | No file  | `d2bb777a0ab0`  |
| 1547   | No file  | `d2bb777a0ab0`  |
| 1537   | No file  | `d2bb777a0ab0`  |
| 1529   | No file  | `d2bb777a0ab0`  |
| 1524   | No file  | `d2bb777a0ab0`  |
| 1519   | No file  | `d2bb777a0ab0`  |
| 1509   | No file  | `d2bb777a0ab0`  |
| 1506   | No file  | `d2bb777a0ab0`  |
| 1504   | No file  | `d2bb777a0ab0`  |
| 1500   | No file  | `d2bb777a0ab0`  |
| 1493   | No file  | `d2bb777a0ab0`  |
| 1489   | No file  | `d2bb777a0ab0`  |
| 1485   | No file  | `d2bb777a0ab0`  |
| 1481   | No file  | `d2bb777a0ab0`  |
| 1474   | No file  | `d2bb777a0ab0`  |
| 1466   | No file  | `d2bb777a0ab0`  |
| 1462   | No file  | `d2bb777a0ab0`  |
| 1459   | No file  | `d2bb777a0ab0`  |
| 1453   | No file  | `d2bb777a0ab0`  |
| 1450   | No file  | `d2bb777a0ab0`  |
| 1445   | No file  | `d2bb777a0ab0`  |
| 1439   | No file  | `d2bb777a0ab0`  |
| 1433   | No file  | `d2bb777a0ab0`  |
| 1430   | No file  | `d2bb777a0ab0`  |
| 1426   | No file  | `d2bb777a0ab0`  |
| 1421   | No file  | `d2bb777a0ab0`  |
| 1417   | No file  | `d2bb777a0ab0`  |
| 1416   | No file  | `d2bb777a0ab0`  |
| 1409   | No file  | `d2bb777a0ab0`  |
| 1405   | No file  | `d2bb777a0ab0`  |
| 1401   | No file  | `d2bb777a0ab0`  |
| 1396   | No file  | `d2bb777a0ab0`  |
| 1391   | No file  | `d2bb777a0ab0`  |
| 1390   | No file  | `d2bb777a0ab0`  |
| 1386   | No file  | `d2bb777a0ab0`  |
| 1381   | No file  | `d2bb777a0ab0`  |
| 1379   | No file  | `d2bb777a0ab0`  |
| 1372   | No file  | `d2bb777a0ab0`  |
| 1366   | No file  | `d2bb777a0ab0`  |
| 1364   | No file  | `d2bb777a0ab0`  |
| 1363   | No file  | `d2bb777a0ab0`  |
| 1360   | No file  | `d2bb777a0ab0`  |
| 1358   | No file  | `d2bb777a0ab0`  |
| 1355   | No file  | `d2bb777a0ab0`  |
| 1351   | No file  | `d2bb777a0ab0`  |
| 1348   | No file  | `d2bb777a0ab0`  |
| 1346   | No file  | `d2bb777a0ab0`  |
| 1341   | No file  | `d2bb777a0ab0`  |
| 1340   | No file  | `d2bb777a0ab0`  |
| 1338   | No file  | `d2bb777a0ab0`  |
| 1335   | No file  | `d2bb777a0ab0`  |
| 1333   | No file  | `d2bb777a0ab0`  |
| 1329   | No file  | `d2bb777a0ab0`  |
| 1327   | No file  | `d2bb777a0ab0`  |
| 1324   | No file  | `d2bb777a0ab0`  |
| 1321   | No file  | `d2bb777a0ab0`  |
| 1319   | No file  | `d2bb777a0ab0`  |
| 1318   | No file  | `d2bb777a0ab0`  |
| 1316   | No file  | `d2bb777a0ab0`  |
| 1313   | No file  | `d2bb777a0ab0`  |
| 1311   | No file  | `d2bb777a0ab0`  |
| 1309   | No file  | `d2bb777a0ab0`  |
| 1304   | No file  | `d2bb777a0ab0`  |
| 1292   | No file  | `d2bb777a0ab0`  |
| 1286   | No file  | `d2bb777a0ab0`  |
| 1280   | No file  | `d2bb777a0ab0`  |
| 1276   | No file  | `d2bb777a0ab0`  |
| 1267   | No file  | `d2bb777a0ab0`  |
| 1261   | No file  | `d2bb777a0ab0`  |
| 1256   | No file  | `d2bb777a0ab0`  |
| 1250   | No file  | `d2bb777a0ab0`  |
| 1246   | No file  | `d2bb777a0ab0`  |
| 1239   | No file  | `d2bb777a0ab0`  |
| 1230   | No file  | `d2bb777a0ab0`  |
| 1226   | No file  | `d2bb777a0ab0`  |
| 1220   | No file  | `d2bb777a0ab0`  |
| 1217   | No file  | `d2bb777a0ab0`  |
| 1211   | No file  | `d2bb777a0ab0`  |
| 1210   | No file  | `d2bb777a0ab0`  |
| 1208   | No file  | `d2bb777a0ab0`  |
| 1203   | No file  | `d2bb777a0ab0`  |
| 1197   | No file  | `d2bb777a0ab0`  |
| 1194   | No file  | `d2bb777a0ab0`  |
| 1192   | No file  | `d2bb777a0ab0`  |
| 1187   | No file  | `d2bb777a0ab0`  |
| 1183   | No file  | `d2bb777a0ab0`  |
| 1177   | No file  | `d2bb777a0ab0`  |
| 1173   | No file  | `d2bb777a0ab0`  |
| 1167   | No file  | `d2bb777a0ab0`  |
| 1164   | No file  | `d2bb777a0ab0`  |
| 1156   | No file  | `d2bb777a0ab0`  |
| 1149   | No file  | `d2bb777a0ab0`  |
| 1144   | No file  | `d2bb777a0ab0`  |
| 1137   | No file  | `d2bb777a0ab0`  |
| 1132   | No file  | `d2bb777a0ab0`  |
| 1127   | No file  | `d2bb777a0ab0`  |
| 1122   | No file  | `d2bb777a0ab0`  |
| 1118   | No file  | `d2bb777a0ab0`  |
| 1114   | No file  | `d2bb777a0ab0`  |
| 1109   | No file  | `d2bb777a0ab0`  |
| 1102   | No file  | `d2bb777a0ab0`  |
| 1096   | No file  | `d2bb777a0ab0`  |
| 1088   | No file  | `d2bb777a0ab0`  |
| 1081   | No file  | `d2bb777a0ab0`  |
| 1076   | No file  | `d2bb777a0ab0`  |
| 1069   | No file  | `d2bb777a0ab0`  |
| 1064   | No file  | `d2bb777a0ab0`  |
| 1058   | No file  | `d2bb777a0ab0`  |
| 1051   | No file  | `d2bb777a0ab0`  |
| 1044   | No file  | `d2bb777a0ab0`  |
| 1036   | No file  | `d2bb777a0ab0`  |
| 1026   | No file  | `d2bb777a0ab0`  |
| 1016   | No file  | `d2bb777a0ab0`  |
| 1009   | No file  | `d2bb777a0ab0`  |
| 1005   | No file  | `d2bb777a0ab0`  |
| 1000   | No file  | `d2bb777a0ab0`  |
| 998    | No file  | `d2bb777a0ab0`  |
| 990    | No file  | `d2bb777a0ab0`  |
| 979    | No file  | `d2bb777a0ab0`  |
| 972    | No file  | `d2bb777a0ab0`  |
| 963    | No file  | `d2bb777a0ab0`  |
| 955    | No file  | `d2bb777a0ab0`  |
| 946    | No file  | `d2bb777a0ab0`  |
| 938    | No file  | `d2bb777a0ab0`  |
| 927    | No file  | `d2bb777a0ab0`  |
| 911    | No file  | `d2bb777a0ab0`  |
| 904    | No file  | `d2bb777a0ab0`  |
| 899    | No file  | `d2bb777a0ab0`  |
| 894    | No file  | `d2bb777a0ab0`  |
| 885    | No file  | `d2bb777a0ab0`  |
| 879    | No file  | `d2bb777a0ab0`  |
| 872    | No file  | `d2bb777a0ab0`  |
| 864    | No file  | `d2bb777a0ab0`  |
| 855    | No file  | `d2bb777a0ab0`  |
| 853    | No file  | `d2bb777a0ab0`  |
| 845    | No file  | `d2bb777a0ab0`  |
| 837    | No file  | `d2bb777a0ab0`  |
| 829    | No file  | `d2bb777a0ab0`  |
| 822    | No file  | `d2bb777a0ab0`  |
| 814    | No file  | `d2bb777a0ab0`  |
| 805    | No file  | `d2bb777a0ab0`  |
| 794    | No file  | `d2bb777a0ab0`  |
| 787    | No file  | `d2bb777a0ab0`  |
| 780    | No file  | `d2bb777a0ab0`  |
| 771    | No file  | `d2bb777a0ab0`  |
| 760    | No file  | `d2bb777a0ab0`  |
| 748    | No file  | `d2bb777a0ab0`  |
| 741    | No file  | `d2bb777a0ab0`  |
| 736    | No file  | `d2bb777a0ab0`  |
| 731    | No file  | `d2bb777a0ab0`  |
| 723    | No file  | `d2bb777a0ab0`  |
| 711    | No file  | `d2bb777a0ab0`  |
| 707    | No file  | `d2bb777a0ab0`  |
| 697    | No file  | `d2bb777a0ab0`  |
| 689    | No file  | `d2bb777a0ab0`  |
| 683    | No file  | `d2bb777a0ab0`  |
| 678    | No file  | `d2bb777a0ab0`  |
| 670    | No file  | `d2bb777a0ab0`  |
| 661    | No file  | `d2bb777a0ab0`  |
| 656    | No file  | `d2bb777a0ab0`  |
| 652    | No file  | `d2bb777a0ab0`  |
| 643    | No file  | `d2bb777a0ab0`  |
| 637    | No file  | `d2bb777a0ab0`  |
| 630    | No file  | `d2bb777a0ab0`  |
| 627    | No file  | `d2bb777a0ab0`  |
| 621    | No file  | `d2bb777a0ab0`  |
| 617    | No file  | `d2bb777a0ab0`  |
| 615    | No file  | `d2bb777a0ab0`  |
| 606    | No file  | `d2bb777a0ab0`  |
| 599    | No file  | `d2bb777a0ab0`  |
| 592    | No file  | `d2bb777a0ab0`  |
| 586    | No file  | `d2bb777a0ab0`  |
| 577    | No file  | `d2bb777a0ab0`  |
| 569    | No file  | `d2bb777a0ab0`  |
| 561    | No file  | `d2bb777a0ab0`  |
| 554    | No file  | `d2bb777a0ab0`  |
| 542    | No file  | `d2bb777a0ab0`  |
| 532    | No file  | `d2bb777a0ab0`  |
| 531    | No file  | `d2bb777a0ab0`  |
| 526    | No file  | `d2bb777a0ab0`  |
| 521    | No file  | `d2bb777a0ab0`  |
| 517    | No file  | `d2bb777a0ab0`  |
| 510    | No file  | `d2bb777a0ab0`  |
| 508    | No file  | `d2bb777a0ab0`  |
| 504    | No file  | `d2bb777a0ab0`  |
| 497    | No file  | `d2bb777a0ab0`  |
| 491    | No file  | `d2bb777a0ab0`  |
| 485    | No file  | `d2bb777a0ab0`  |
| 478    | No file  | `d2bb777a0ab0`  |
| 472    | No file  | `d2bb777a0ab0`  |
| 466    | No file  | `d2bb777a0ab0`  |
| 457    | No file  | `d2bb777a0ab0`  |
| 452    | No file  | `d2bb777a0ab0`  |
| 449    | No file  | `d2bb777a0ab0`  |
| 435    | No file  | `d2bb777a0ab0`  |

<!-- versions:end -->

## Companion Files

None. The handler reads only this file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `0` on clients that ship the file empty |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (16 bytes)

| Offset  | Type | Field      | Notes                                |
| ------- | ---- | ---------- | ------------------------------------ |
| `+0x00` | u32  | index      | `0` to `row_count - 1` in file order |
| `+0x04` | f32  | position_x | World X                              |
| `+0x08` | f32  | position_y | World Y (height)                     |
| `+0x0C` | f32  | position_z | World Z                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `TankSpawnPosition` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Index`, `PositionX`, `PositionY` and
`PositionZ`, and its nine rows match the nine rows of the client 3482 file
in order and value (9 of 9); client 1784 ships the file empty. That
server's dump (client 1784) names the member
`TankSpawnPositionStaticStatus _index`.

## Notes

- Clients 1784 to 2765 ship the file with `row_count` `0`; client 3002
  and later hold the nine rows.
- Indexes `0` to `2`, `3` to `5` and `6` to `8` hold the same three
  positions (`-347644, 1854, -53615`, `-347038, 1854, -54532` and
  `-346340, 1803, -55563`). Each lies within 3,000 units (X and Z) of
  Calpheon's first castle gate attack position in the
  `SiegeCastleTeleportPos` sheet (client 1784, `-348487, 2287, -56349`),
  so the Mediah and Valencia rows of `siegegovernorcarriagespawn.bss`
  point at positions at Calpheon too.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`.
