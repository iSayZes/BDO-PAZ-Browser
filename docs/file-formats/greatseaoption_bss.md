# `greatseaoption.bss` Format

## Purpose

One record of Great Ocean and island barter options: food use, the
explore cooldown, the ship management and barter ranges, barter exchange
and reset counts, discount values and two EXP values. The fields are the
client side of the `IslandExplore_Option` sheet (see Field Names).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | -------------- | --------- |
| 5      | 2717 and later | 3483    | `greatseaoption.bss` | 88    | 1 String Table | 4         |
| 4      | 1313 to 2709   | 2709    | `greatseaoption.bss` | 86    | 1 String Table | 4         |
| 3      | 1304 to 1311   | 1311    | `greatseaoption.bss` | 82    | 1 String Table | 4         |
| 2      | 1267 to 1292   | 1292    | `greatseaoption.bss` | 54    | 1 String Table | 4         |
| 1      | 1239 to 1261   | 1261    | `greatseaoption.bss` | 42    | 1 String Table | 4         |

| Layout | File                 | Known        | Unknown      |
| ------ | -------------------- | ------------ | ------------ |
| 5      | `greatseaoption.bss` | 75 B (85.2%) | 13 B (14.8%) |
| 4      | `greatseaoption.bss` | 73 B (84.9%) | 13 B (15.1%) |
| 3      | `greatseaoption.bss` | 73 B (89.0%) | 9 B (11.0%)  |
| 2      | `greatseaoption.bss` | 53 B (98.1%) | 1 B (1.9%)   |
| 1      | `greatseaoption.bss` | 41 B (97.6%) | 1 B (2.4%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 5 | `f9c2854dd891`  |
| 3482   | Layout 5 | `f9c2854dd891`  |
| 3474   | Layout 5 | `f9c2854dd891`  |
| 3473   | Layout 5 | `f9c2854dd891`  |
| 3464   | Layout 5 | `f9c2854dd891`  |
| 3458   | Layout 5 | `f9c2854dd891`  |
| 3454   | Layout 5 | `f9c2854dd891`  |
| 3444   | Layout 5 | `f9c2854dd891`  |
| 3435   | Layout 5 | `f9c2854dd891`  |
| 3426   | Layout 5 | `f9c2854dd891`  |
| 3418   | Layout 5 | `f9c2854dd891`  |
| 3412   | Layout 5 | `f9c2854dd891`  |
| 3402   | Layout 5 | `f9c2854dd891`  |
| 3396   | Layout 5 | `f9c2854dd891`  |
| 3387   | Layout 5 | `f9c2854dd891`  |
| 3381   | Layout 5 | `f9c2854dd891`  |
| 3373   | Layout 5 | `f9c2854dd891`  |
| 3364   | Layout 5 | `f9c2854dd891`  |
| 3356   | Layout 5 | `f9c2854dd891`  |
| 3349   | Layout 5 | `f9c2854dd891`  |
| 3342   | Layout 5 | `f9c2854dd891`  |
| 3335   | Layout 5 | `f9c2854dd891`  |
| 3326   | Layout 5 | `f9c2854dd891`  |
| 3321   | Layout 5 | `f9c2854dd891`  |
| 3314   | Layout 5 | `f9c2854dd891`  |
| 3303   | Layout 5 | `f9c2854dd891`  |
| 3302   | Layout 5 | `f9c2854dd891`  |
| 3293   | Layout 5 | `f9c2854dd891`  |
| 3283   | Layout 5 | `f9c2854dd891`  |
| 3275   | Layout 5 | `f9c2854dd891`  |
| 3267   | Layout 5 | `f9c2854dd891`  |
| 3258   | Layout 5 | `f9c2854dd891`  |
| 3251   | Layout 5 | `f9c2854dd891`  |
| 3242   | Layout 5 | `f9c2854dd891`  |
| 3235   | Layout 5 | `f9c2854dd891`  |
| 3229   | Layout 5 | `f9c2854dd891`  |
| 3212   | Layout 5 | `f9c2854dd891`  |
| 3203   | Layout 5 | `f9c2854dd891`  |
| 3193   | Layout 5 | `f9c2854dd891`  |
| 3186   | Layout 5 | `f9c2854dd891`  |
| 3177   | Layout 5 | `f9c2854dd891`  |
| 3169   | Layout 5 | `f9c2854dd891`  |
| 3158   | Layout 5 | `f9c2854dd891`  |
| 3151   | Layout 5 | `f9c2854dd891`  |
| 3144   | Layout 5 | `f9c2854dd891`  |
| 3133   | Layout 5 | `f9c2854dd891`  |
| 3125   | Layout 5 | `f9c2854dd891`  |
| 3118   | Layout 5 | `f9c2854dd891`  |
| 3111   | Layout 5 | `f9c2854dd891`  |
| 3103   | Layout 5 | `f9c2854dd891`  |
| 3095   | Layout 5 | `f9c2854dd891`  |
| 3086   | Layout 5 | `f9c2854dd891`  |
| 3072   | Layout 5 | `f9c2854dd891`  |
| 3062   | Layout 5 | `f9c2854dd891`  |
| 3052   | Layout 5 | `f9c2854dd891`  |
| 3045   | Layout 5 | `f9c2854dd891`  |
| 3037   | Layout 5 | `f9c2854dd891`  |
| 3030   | Layout 5 | `f9c2854dd891`  |
| 3021   | Layout 5 | `f9c2854dd891`  |
| 3012   | Layout 5 | `f9c2854dd891`  |
| 3002   | Layout 5 | `f9c2854dd891`  |
| 2995   | Layout 5 | `f9c2854dd891`  |
| 2987   | Layout 5 | `f9c2854dd891`  |
| 2978   | Layout 5 | `f9c2854dd891`  |
| 2970   | Layout 5 | `f9c2854dd891`  |
| 2959   | Layout 5 | `f9c2854dd891`  |
| 2951   | Layout 5 | `f9c2854dd891`  |
| 2942   | Layout 5 | `f9c2854dd891`  |
| 2935   | Layout 5 | `f9c2854dd891`  |
| 2932   | Layout 5 | `f9c2854dd891`  |
| 2923   | Layout 5 | `f9c2854dd891`  |
| 2919   | Layout 5 | `f9c2854dd891`  |
| 2907   | Layout 5 | `f9c2854dd891`  |
| 2900   | Layout 5 | `f9c2854dd891`  |
| 2891   | Layout 5 | `f9c2854dd891`  |
| 2882   | Layout 5 | `f9c2854dd891`  |
| 2872   | Layout 5 | `f9c2854dd891`  |
| 2863   | Layout 5 | `f9c2854dd891`  |
| 2855   | Layout 5 | `f9c2854dd891`  |
| 2849   | Layout 5 | `f9c2854dd891`  |
| 2844   | Layout 5 | `f9c2854dd891`  |
| 2834   | Layout 5 | `f9c2854dd891`  |
| 2825   | Layout 5 | `f9c2854dd891`  |
| 2819   | Layout 5 | `f9c2854dd891`  |
| 2811   | Layout 5 | `f9c2854dd891`  |
| 2803   | Layout 5 | `f9c2854dd891`  |
| 2794   | Layout 5 | `f9c2854dd891`  |
| 2783   | Layout 5 | `f9c2854dd891`  |
| 2774   | Layout 5 | `f9c2854dd891`  |
| 2765   | Layout 5 | `f9c2854dd891`  |
| 2756   | Layout 5 | `f9c2854dd891`  |
| 2750   | Layout 5 | `f9c2854dd891`  |
| 2743   | Layout 5 | `f9c2854dd891`  |
| 2736   | Layout 5 | `f9c2854dd891`  |
| 2726   | Layout 5 | `f9c2854dd891`  |
| 2717   | Layout 5 | `f9c2854dd891`  |
| 2709   | Layout 4 | `f9c2854dd891`  |
| 2703   | Layout 4 | `f9c2854dd891`  |
| 2695   | Layout 4 | `f9c2854dd891`  |
| 2684   | Layout 4 | `f9c2854dd891`  |
| 2672   | Layout 4 | `f9c2854dd891`  |
| 2665   | Layout 4 | `f9c2854dd891`  |
| 2657   | Layout 4 | `f9c2854dd891`  |
| 2649   | Layout 4 | `f9c2854dd891`  |
| 2644   | Layout 4 | `f9c2854dd891`  |
| 2637   | Layout 4 | `f9c2854dd891`  |
| 2629   | Layout 4 | `f9c2854dd891`  |
| 2619   | Layout 4 | `f9c2854dd891`  |
| 2612   | Layout 4 | `f9c2854dd891`  |
| 2606   | Layout 4 | `f9c2854dd891`  |
| 2602   | Layout 4 | `f9c2854dd891`  |
| 2601   | Layout 4 | `f9c2854dd891`  |
| 2592   | Layout 4 | `f9c2854dd891`  |
| 2583   | Layout 4 | `f9c2854dd891`  |
| 2575   | Layout 4 | `f9c2854dd891`  |
| 2567   | Layout 4 | `f9c2854dd891`  |
| 2560   | Layout 4 | `f9c2854dd891`  |
| 2553   | Layout 4 | `f9c2854dd891`  |
| 2545   | Layout 4 | `f9c2854dd891`  |
| 2538   | Layout 4 | `f9c2854dd891`  |
| 2529   | Layout 4 | `f9c2854dd891`  |
| 2519   | Layout 4 | `f9c2854dd891`  |
| 2513   | Layout 4 | `f9c2854dd891`  |
| 2510   | Layout 4 | `f9c2854dd891`  |
| 2507   | Layout 4 | `f9c2854dd891`  |
| 2503   | Layout 4 | `f9c2854dd891`  |
| 2498   | Layout 4 | `f9c2854dd891`  |
| 2492   | Layout 4 | `f9c2854dd891`  |
| 2487   | Layout 4 | `f9c2854dd891`  |
| 2480   | Layout 4 | `f9c2854dd891`  |
| 2474   | Layout 4 | `f9c2854dd891`  |
| 2468   | Layout 4 | `f9c2854dd891`  |
| 2460   | Layout 4 | `f9c2854dd891`  |
| 2453   | Layout 4 | `f9c2854dd891`  |
| 2444   | Layout 4 | `f9c2854dd891`  |
| 2438   | Layout 4 | `f9c2854dd891`  |
| 2434   | Layout 4 | `f9c2854dd891`  |
| 2429   | Layout 4 | `f9c2854dd891`  |
| 2421   | Layout 4 | `f9c2854dd891`  |
| 2414   | Layout 4 | `f9c2854dd891`  |
| 2407   | Layout 4 | `f9c2854dd891`  |
| 2401   | Layout 4 | `f9c2854dd891`  |
| 2397   | Layout 4 | `f9c2854dd891`  |
| 2393   | Layout 4 | `f9c2854dd891`  |
| 2384   | Layout 4 | `f9c2854dd891`  |
| 2378   | Layout 4 | `f9c2854dd891`  |
| 2372   | Layout 4 | `f9c2854dd891`  |
| 2358   | Layout 4 | `f9c2854dd891`  |
| 2352   | Layout 4 | `f9c2854dd891`  |
| 2347   | Layout 4 | `f9c2854dd891`  |
| 2343   | Layout 4 | `f9c2854dd891`  |
| 2335   | Layout 4 | `f9c2854dd891`  |
| 2327   | Layout 4 | `f9c2854dd891`  |
| 2324   | Layout 4 | `f9c2854dd891`  |
| 2319   | Layout 4 | `f9c2854dd891`  |
| 2313   | Layout 4 | `f9c2854dd891`  |
| 2308   | Layout 4 | `f9c2854dd891`  |
| 2302   | Layout 4 | `f9c2854dd891`  |
| 2295   | Layout 4 | `f9c2854dd891`  |
| 2290   | Layout 4 | `f9c2854dd891`  |
| 2284   | Layout 4 | `f9c2854dd891`  |
| 2276   | Layout 4 | `f9c2854dd891`  |
| 2269   | Layout 4 | `f9c2854dd891`  |
| 2259   | Layout 4 | `f9c2854dd891`  |
| 2250   | Layout 4 | `f9c2854dd891`  |
| 2243   | Layout 4 | `f9c2854dd891`  |
| 2235   | Layout 4 | `f9c2854dd891`  |
| 2229   | Layout 4 | `f9c2854dd891`  |
| 2224   | Layout 4 | `f9c2854dd891`  |
| 2218   | Layout 4 | `f9c2854dd891`  |
| 2215   | Layout 4 | `f9c2854dd891`  |
| 2207   | Layout 4 | `f9c2854dd891`  |
| 2203   | Layout 4 | `f9c2854dd891`  |
| 2196   | Layout 4 | `f9c2854dd891`  |
| 2192   | Layout 4 | `f9c2854dd891`  |
| 2189   | Layout 4 | `f9c2854dd891`  |
| 2183   | Layout 4 | `f9c2854dd891`  |
| 2179   | Layout 4 | `f9c2854dd891`  |
| 2171   | Layout 4 | `f9c2854dd891`  |
| 2163   | Layout 4 | `f9c2854dd891`  |
| 2156   | Layout 4 | `f9c2854dd891`  |
| 2151   | Layout 4 | `f9c2854dd891`  |
| 2147   | Layout 4 | `f9c2854dd891`  |
| 2142   | Layout 4 | `f9c2854dd891`  |
| 2138   | Layout 4 | `f9c2854dd891`  |
| 2134   | Layout 4 | `f9c2854dd891`  |
| 2130   | Layout 4 | `f9c2854dd891`  |
| 2122   | Layout 4 | `f9c2854dd891`  |
| 2107   | Layout 4 | `f9c2854dd891`  |
| 2098   | Layout 4 | `f9c2854dd891`  |
| 2089   | Layout 4 | `f9c2854dd891`  |
| 2081   | Layout 4 | `f9c2854dd891`  |
| 2073   | Layout 4 | `f9c2854dd891`  |
| 2067   | Layout 4 | `f9c2854dd891`  |
| 2063   | Layout 4 | `f9c2854dd891`  |
| 2059   | Layout 4 | `f9c2854dd891`  |
| 2052   | Layout 4 | `f9c2854dd891`  |
| 2044   | Layout 4 | `f9c2854dd891`  |
| 2039   | Layout 4 | `f9c2854dd891`  |
| 2032   | Layout 4 | `f9c2854dd891`  |
| 2025   | Layout 4 | `f9c2854dd891`  |
| 2011   | Layout 4 | `f9c2854dd891`  |
| 2005   | Layout 4 | `f9c2854dd891`  |
| 2000   | Layout 4 | `f9c2854dd891`  |
| 1996   | Layout 4 | `f9c2854dd891`  |
| 1991   | Layout 4 | `f9c2854dd891`  |
| 1985   | Layout 4 | `f9c2854dd891`  |
| 1980   | Layout 4 | `f9c2854dd891`  |
| 1969   | Layout 4 | `f9c2854dd891`  |
| 1964   | Layout 4 | `f9c2854dd891`  |
| 1958   | Layout 4 | `f9c2854dd891`  |
| 1950   | Layout 4 | `f9c2854dd891`  |
| 1945   | Layout 4 | `f9c2854dd891`  |
| 1937   | Layout 4 | `f9c2854dd891`  |
| 1933   | Layout 4 | `f9c2854dd891`  |
| 1927   | Layout 4 | `f9c2854dd891`  |
| 1921   | Layout 4 | `f9c2854dd891`  |
| 1914   | Layout 4 | `f9c2854dd891`  |
| 1908   | Layout 4 | `f9c2854dd891`  |
| 1897   | Layout 4 | `f9c2854dd891`  |
| 1892   | Layout 4 | `f9c2854dd891`  |
| 1886   | Layout 4 | `f9c2854dd891`  |
| 1881   | Layout 4 | `f9c2854dd891`  |
| 1871   | Layout 4 | `f9c2854dd891`  |
| 1866   | Layout 4 | `f9c2854dd891`  |
| 1862   | Layout 4 | `f9c2854dd891`  |
| 1854   | Layout 4 | `f9c2854dd891`  |
| 1846   | Layout 4 | `f9c2854dd891`  |
| 1838   | Layout 4 | `f9c2854dd891`  |
| 1832   | Layout 4 | `f9c2854dd891`  |
| 1826   | Layout 4 | `f9c2854dd891`  |
| 1822   | Layout 4 | `f9c2854dd891`  |
| 1818   | Layout 4 | `f9c2854dd891`  |
| 1804   | Layout 4 | `f9c2854dd891`  |
| 1794   | Layout 4 | `f9c2854dd891`  |
| 1790   | Layout 4 | `f9c2854dd891`  |
| 1784   | Layout 4 | `f9c2854dd891`  |
| 1774   | Layout 4 | `f9c2854dd891`  |
| 1771   | Layout 4 | `f9c2854dd891`  |
| 1762   | Layout 4 | `f9c2854dd891`  |
| 1759   | Layout 4 | `f9c2854dd891`  |
| 1754   | Layout 4 | `f9c2854dd891`  |
| 1749   | Layout 4 | `f9c2854dd891`  |
| 1743   | Layout 4 | `f9c2854dd891`  |
| 1737   | Layout 4 | `f9c2854dd891`  |
| 1731   | Layout 4 | `f9c2854dd891`  |
| 1725   | Layout 4 | `f9c2854dd891`  |
| 1717   | Layout 4 | `f9c2854dd891`  |
| 1710   | Layout 4 | `f9c2854dd891`  |
| 1704   | Layout 4 | `f9c2854dd891`  |
| 1698   | Layout 4 | `f9c2854dd891`  |
| 1690   | Layout 4 | `f9c2854dd891`  |
| 1685   | Layout 4 | `f9c2854dd891`  |
| 1680   | Layout 4 | `f9c2854dd891`  |
| 1674   | Layout 4 | `f9c2854dd891`  |
| 1668   | Layout 4 | `f9c2854dd891`  |
| 1659   | Layout 4 | `f9c2854dd891`  |
| 1649   | Layout 4 | `f9c2854dd891`  |
| 1642   | Layout 4 | `f9c2854dd891`  |
| 1636   | Layout 4 | `f9c2854dd891`  |
| 1628   | Layout 4 | `f9c2854dd891`  |
| 1622   | Layout 4 | `f9c2854dd891`  |
| 1614   | Layout 4 | `f9c2854dd891`  |
| 1608   | Layout 4 | `f9c2854dd891`  |
| 1602   | Layout 4 | `f9c2854dd891`  |
| 1598   | Layout 4 | `f9c2854dd891`  |
| 1594   | Layout 4 | `f9c2854dd891`  |
| 1590   | Layout 4 | `f9c2854dd891`  |
| 1587   | Layout 4 | `f9c2854dd891`  |
| 1584   | Layout 4 | `f9c2854dd891`  |
| 1579   | Layout 4 | `f9c2854dd891`  |
| 1572   | Layout 4 | `f9c2854dd891`  |
| 1565   | Layout 4 | `f9c2854dd891`  |
| 1559   | Layout 4 | `f9c2854dd891`  |
| 1554   | Layout 4 | `f9c2854dd891`  |
| 1547   | Layout 4 | `f9c2854dd891`  |
| 1537   | Layout 4 | `f9c2854dd891`  |
| 1529   | Layout 4 | `f9c2854dd891`  |
| 1524   | Layout 4 | `f9c2854dd891`  |
| 1519   | Layout 4 | `f9c2854dd891`  |
| 1509   | Layout 4 | `f9c2854dd891`  |
| 1506   | Layout 4 | `f9c2854dd891`  |
| 1504   | Layout 4 | `f9c2854dd891`  |
| 1500   | Layout 4 | `f9c2854dd891`  |
| 1493   | Layout 4 | `f9c2854dd891`  |
| 1489   | Layout 4 | `f9c2854dd891`  |
| 1485   | Layout 4 | `f9c2854dd891`  |
| 1481   | Layout 4 | `f9c2854dd891`  |
| 1474   | Layout 4 | `f9c2854dd891`  |
| 1466   | Layout 4 | `f9c2854dd891`  |
| 1462   | Layout 4 | `f9c2854dd891`  |
| 1459   | Layout 4 | `f9c2854dd891`  |
| 1453   | Layout 4 | `f9c2854dd891`  |
| 1450   | Layout 4 | `f9c2854dd891`  |
| 1445   | Layout 4 | `f9c2854dd891`  |
| 1439   | Layout 4 | `f9c2854dd891`  |
| 1433   | Layout 4 | `f9c2854dd891`  |
| 1430   | Layout 4 | `f9c2854dd891`  |
| 1426   | Layout 4 | `f9c2854dd891`  |
| 1421   | Layout 4 | `f9c2854dd891`  |
| 1417   | Layout 4 | `f9c2854dd891`  |
| 1416   | Layout 4 | `f9c2854dd891`  |
| 1409   | Layout 4 | `f9c2854dd891`  |
| 1405   | Layout 4 | `f9c2854dd891`  |
| 1401   | Layout 4 | `f9c2854dd891`  |
| 1396   | Layout 4 | `f9c2854dd891`  |
| 1391   | Layout 4 | `f9c2854dd891`  |
| 1390   | Layout 4 | `f9c2854dd891`  |
| 1386   | Layout 4 | `f9c2854dd891`  |
| 1381   | Layout 4 | `f9c2854dd891`  |
| 1379   | Layout 4 | `f9c2854dd891`  |
| 1372   | Layout 4 | `f9c2854dd891`  |
| 1366   | Layout 4 | `f9c2854dd891`  |
| 1364   | Layout 4 | `f9c2854dd891`  |
| 1363   | Layout 4 | `f9c2854dd891`  |
| 1360   | Layout 4 | `f9c2854dd891`  |
| 1358   | Layout 4 | `f9c2854dd891`  |
| 1355   | Layout 4 | `f9c2854dd891`  |
| 1351   | Layout 4 | `f9c2854dd891`  |
| 1348   | Layout 4 | `f9c2854dd891`  |
| 1346   | Layout 4 | `f9c2854dd891`  |
| 1341   | Layout 4 | `f9c2854dd891`  |
| 1340   | Layout 4 | `f9c2854dd891`  |
| 1338   | Layout 4 | `f9c2854dd891`  |
| 1335   | Layout 4 | `f9c2854dd891`  |
| 1333   | Layout 4 | `f9c2854dd891`  |
| 1329   | Layout 4 | `f9c2854dd891`  |
| 1327   | Layout 4 | `f9c2854dd891`  |
| 1324   | Layout 4 | `f9c2854dd891`  |
| 1321   | Layout 4 | `f9c2854dd891`  |
| 1319   | Layout 4 | `f9c2854dd891`  |
| 1318   | Layout 4 | `f9c2854dd891`  |
| 1316   | Layout 4 | `f9c2854dd891`  |
| 1313   | Layout 4 | `f9c2854dd891`  |
| 1311   | Layout 3 | `f9c2854dd891`  |
| 1309   | Layout 3 | `f9c2854dd891`  |
| 1304   | Layout 3 | `f9c2854dd891`  |
| 1292   | Layout 2 | `f9c2854dd891`  |
| 1286   | Layout 2 | `f9c2854dd891`  |
| 1280   | Layout 2 | `f9c2854dd891`  |
| 1276   | Layout 2 | `f9c2854dd891`  |
| 1267   | Layout 2 | `f9c2854dd891`  |
| 1261   | Layout 1 | `f9c2854dd891`  |
| 1256   | Layout 1 | `f9c2854dd891`  |
| 1250   | Layout 1 | `f9c2854dd891`  |
| 1246   | Layout 1 | `f9c2854dd891`  |
| 1239   | Layout 1 | `f9c2854dd891`  |
| 1230   | No file  | `f9c2854dd891`  |
| 1226   | No file  | `f9c2854dd891`  |
| 1220   | No file  | `f9c2854dd891`  |
| 1217   | No file  | `f9c2854dd891`  |
| 1211   | No file  | `f9c2854dd891`  |
| 1210   | No file  | `f9c2854dd891`  |
| 1208   | No file  | `f9c2854dd891`  |
| 1203   | No file  | `f9c2854dd891`  |
| 1197   | No file  | `f9c2854dd891`  |
| 1194   | No file  | `f9c2854dd891`  |
| 1192   | No file  | `f9c2854dd891`  |
| 1187   | No file  | `f9c2854dd891`  |
| 1183   | No file  | `f9c2854dd891`  |
| 1177   | No file  | `f9c2854dd891`  |
| 1173   | No file  | `f9c2854dd891`  |
| 1167   | No file  | `f9c2854dd891`  |
| 1164   | No file  | `f9c2854dd891`  |
| 1156   | No file  | `f9c2854dd891`  |
| 1149   | No file  | `f9c2854dd891`  |
| 1144   | No file  | `f9c2854dd891`  |
| 1137   | No file  | `f9c2854dd891`  |
| 1132   | No file  | `f9c2854dd891`  |
| 1127   | No file  | `f9c2854dd891`  |
| 1122   | No file  | `f9c2854dd891`  |
| 1118   | No file  | `f9c2854dd891`  |
| 1114   | No file  | `f9c2854dd891`  |
| 1109   | No file  | `f9c2854dd891`  |
| 1102   | No file  | `f9c2854dd891`  |
| 1096   | No file  | `f9c2854dd891`  |
| 1088   | No file  | `f9c2854dd891`  |
| 1081   | No file  | `f9c2854dd891`  |
| 1076   | No file  | `f9c2854dd891`  |
| 1069   | No file  | `f9c2854dd891`  |
| 1064   | No file  | `f9c2854dd891`  |
| 1058   | No file  | `f9c2854dd891`  |
| 1051   | No file  | `f9c2854dd891`  |
| 1044   | No file  | `f9c2854dd891`  |
| 1036   | No file  | `f9c2854dd891`  |
| 1026   | No file  | `f9c2854dd891`  |
| 1016   | No file  | `f9c2854dd891`  |
| 1009   | No file  | `f9c2854dd891`  |
| 1005   | No file  | `f9c2854dd891`  |
| 1000   | No file  | `f9c2854dd891`  |
| 998    | No file  | `f9c2854dd891`  |
| 990    | No file  | `f9c2854dd891`  |
| 979    | No file  | `f9c2854dd891`  |
| 972    | No file  | `f9c2854dd891`  |
| 963    | No file  | `f9c2854dd891`  |
| 955    | No file  | `f9c2854dd891`  |
| 946    | No file  | `f9c2854dd891`  |
| 938    | No file  | `f9c2854dd891`  |
| 927    | No file  | `f9c2854dd891`  |
| 911    | No file  | `f9c2854dd891`  |
| 904    | No file  | `f9c2854dd891`  |
| 899    | No file  | `f9c2854dd891`  |
| 894    | No file  | `f9c2854dd891`  |
| 885    | No file  | `f9c2854dd891`  |
| 879    | No file  | `f9c2854dd891`  |
| 872    | No file  | `f9c2854dd891`  |
| 864    | No file  | `f9c2854dd891`  |
| 855    | No file  | `f9c2854dd891`  |
| 853    | No file  | `f9c2854dd891`  |
| 845    | No file  | `f9c2854dd891`  |
| 837    | No file  | `f9c2854dd891`  |
| 829    | No file  | `f9c2854dd891`  |
| 822    | No file  | `f9c2854dd891`  |
| 814    | No file  | `f9c2854dd891`  |
| 805    | No file  | `f9c2854dd891`  |
| 794    | No file  | `f9c2854dd891`  |
| 787    | No file  | `f9c2854dd891`  |
| 780    | No file  | `f9c2854dd891`  |
| 771    | No file  | `f9c2854dd891`  |
| 760    | No file  | `f9c2854dd891`  |
| 748    | No file  | `f9c2854dd891`  |
| 741    | No file  | `f9c2854dd891`  |
| 736    | No file  | `f9c2854dd891`  |
| 731    | No file  | `f9c2854dd891`  |
| 723    | No file  | `f9c2854dd891`  |
| 711    | No file  | `f9c2854dd891`  |
| 707    | No file  | `f9c2854dd891`  |
| 697    | No file  | `f9c2854dd891`  |
| 689    | No file  | `f9c2854dd891`  |
| 683    | No file  | `f9c2854dd891`  |
| 678    | No file  | `f9c2854dd891`  |
| 670    | No file  | `f9c2854dd891`  |
| 661    | No file  | `f9c2854dd891`  |
| 656    | No file  | `f9c2854dd891`  |
| 652    | No file  | `f9c2854dd891`  |
| 643    | No file  | `f9c2854dd891`  |
| 637    | No file  | `f9c2854dd891`  |
| 630    | No file  | `f9c2854dd891`  |
| 627    | No file  | `f9c2854dd891`  |
| 621    | No file  | `f9c2854dd891`  |
| 617    | No file  | `f9c2854dd891`  |
| 615    | No file  | `f9c2854dd891`  |
| 606    | No file  | `f9c2854dd891`  |
| 599    | No file  | `f9c2854dd891`  |
| 592    | No file  | `f9c2854dd891`  |
| 586    | No file  | `f9c2854dd891`  |
| 577    | No file  | `f9c2854dd891`  |
| 569    | No file  | `f9c2854dd891`  |
| 561    | No file  | `f9c2854dd891`  |
| 554    | No file  | `f9c2854dd891`  |
| 542    | No file  | `f9c2854dd891`  |
| 532    | No file  | `f9c2854dd891`  |
| 531    | No file  | `f9c2854dd891`  |
| 526    | No file  | `f9c2854dd891`  |
| 521    | No file  | `f9c2854dd891`  |
| 517    | No file  | `f9c2854dd891`  |
| 510    | No file  | `f9c2854dd891`  |
| 508    | No file  | `f9c2854dd891`  |
| 504    | No file  | `f9c2854dd891`  |
| 497    | No file  | `f9c2854dd891`  |
| 491    | No file  | `f9c2854dd891`  |
| 485    | No file  | `f9c2854dd891`  |
| 478    | No file  | `f9c2854dd891`  |
| 472    | No file  | `f9c2854dd891`  |
| 466    | No file  | `f9c2854dd891`  |
| 457    | No file  | `f9c2854dd891`  |
| 452    | No file  | `f9c2854dd891`  |
| 449    | No file  | `f9c2854dd891`  |
| 435    | No file  | `f9c2854dd891`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 5

### File Layout

| Offset              | Type         | Field                 | Notes                                                               |
| ------------------- | ------------ | --------------------- | ------------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                                                        |
| `+0x04`             | u32          | food_consume          | `100000` on clients 1784 and 3482                                   |
| `+0x08`             | u32          | explore_cool_time     | `1200` on clients 1784 and 3482                                     |
| `+0x0C`             | f32          | ship_management_range | `15000` on client 1784, `20000` on client 3482                      |
| `+0x10`             | f32          | barter_range          | `5000` on clients 1784 and 3482                                     |
| `+0x14`             | u8           | reset_cool_time       | `4` on client 1784, `2` on client 3482                              |
| `+0x15`             | u8           | unknown_15            | `0` on every client checked                                         |
| `+0x16`             | u32          | max_exchange_count    | `1000000` on clients 1784 and 3482                                  |
| `+0x1A`             | u32          | over_max_count        | `1000000` on clients 1784 and 3482                                  |
| `+0x1E`             | u32          | max_reset_count       | `100` on clients 1784 and 3482                                      |
| `+0x22`             | u16          | barter_reset_time     | `6` on client 3482                                                  |
| `+0x24`             | u32          | discount_rate         | `100000` on clients 1784 and 3482                                   |
| `+0x28`             | u32          | add_reset_count       | `50` on clients 1784 and 3482                                       |
| `+0x2C`             | u32          | reset_need_count      | `30` on clients 1784 and 3482                                       |
| `+0x30`             | u32          | time_discount         | `10000` on clients 1784 and 3482                                    |
| `+0x34`             | u32          | time_discount_limit   | `50000` on clients 1784 and 3482                                    |
| `+0x38`             | u32          | sub_employee_exp      | `20` on clients 1784 and 3482                                       |
| `+0x3C`             | u32          | unknown_3c            | `0` on every client checked                                         |
| `+0x40`             | u32          | sub_trade_exp         | `499` on clients 1784 and 3482                                      |
| `+0x44`             | u32          | unknown_44            | `0` on every client checked                                         |
| `+0x48`             | u32          | unknown_48            | `500000` on every client checked; see Open Questions                |
| `+0x4C`             | String Table | string_table          | See String Table                                                    |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x4C`                                  |
| `string_table+0x04` | u32          | zero                  | Always `0`                                                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 4

No `barter_reset_time`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          |                                    |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    |                                    |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | u32          | max_reset_count       |                                    |
| `+0x22`             | u32          | discount_rate         |                                    |
| `+0x26`             | u32          | add_reset_count       |                                    |
| `+0x2A`             | u32          | reset_need_count      |                                    |
| `+0x2E`             | u32          | time_discount         |                                    |
| `+0x32`             | u32          | time_discount_limit   |                                    |
| `+0x36`             | u32          | sub_employee_exp      |                                    |
| `+0x3A`             | u32          | unknown_3c            |                                    |
| `+0x3E`             | u32          | sub_trade_exp         |                                    |
| `+0x42`             | u32          | unknown_44            |                                    |
| `+0x46`             | u32          | unknown_48            |                                    |
| `+0x4A`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x4A` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Layout 3

No `unknown_48`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          |                                    |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    |                                    |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | u32          | max_reset_count       | `3` on client 1309                 |
| `+0x22`             | u32          | discount_rate         |                                    |
| `+0x26`             | u32          | add_reset_count       | `1` on client 1309                 |
| `+0x2A`             | u32          | reset_need_count      | `1` on client 1309                 |
| `+0x2E`             | u32          | time_discount         |                                    |
| `+0x32`             | u32          | time_discount_limit   |                                    |
| `+0x36`             | u32          | sub_employee_exp      |                                    |
| `+0x3A`             | u32          | unknown_3c            |                                    |
| `+0x3E`             | u32          | sub_trade_exp         |                                    |
| `+0x42`             | u32          | unknown_44            |                                    |
| `+0x46`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x46` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Layout 2

The values end after `add_reset_count`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          |                                    |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    |                                    |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | u32          | max_reset_count       |                                    |
| `+0x22`             | u32          | discount_rate         |                                    |
| `+0x26`             | u32          | add_reset_count       |                                    |
| `+0x2A`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x2A` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Layout 1

The values end after `over_max_count`. Client 1239 is the first client
with the file (client 1230 has none).

The two u32 after `unknown_15` are `max_exchange_count` and
`over_max_count`. Layout 2 appends `max_reset_count`, `discount_rate` and
`add_reset_count` after them, the same step at the end of the values as
Layouts 3 and 4 take, and the server loader in Field Names stores
`MaxExchangeCount` and `OverMaxCount` in that order before
`MaxResetCount`. The client Lua agrees: the client 1256 barter Lua shows
`ToClient_barterMaxExchangeCountForTime()` minus
`ToClient_barterCurrentExchangeCountForTime()` as the remaining count
(`LUA_TRADEITEM_REMAIN_COUNT`) and has no reset or discount getter.
`ToClient_getMaxChangeSeedCountForDay`, `ToClient_discountPointByBarterLevel`
and `ToClient_needExchangeCount` first appear in the client 1267 Lua,
where the same remainder becomes a ticket count
(`LUA_TRADEITEM_TICKET_COUNT`) and `max_exchange_count` rises from `100`
to `1000000`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          | `8000` on clients 1239 to 1261     |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    | `100` on clients 1239 to 1261      |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x1E` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Field Names

The `IslandExplore_Option` sheet of a private server's
`DataSheets.bexcel` on client 1784 has 24 columns and one row. The client
1784 file holds 19 values; 15 of them are sheet values, in close to sheet
order: `FoodConsume` (`100000`), `ExploreCoolTime` (`1200`),
`ShipManagementRange` (`15000`), `BarterRange` (`5000`), `ResetCoolTime`
(`4`), `MaxExchangeCount` and `OverMaxCount` (both `1000000`),
`MaxResetCount` (`100`), `DiscountRate` (`100000`), `AddResetCount`
(`50`), `ResetNeedCount` (`30`), `TimeDiscount` (`10000`),
`TimeDiscountLimit` (`50000`), `SubEmployeeExp` (`20`) and `SubTradeExp`
(`499`). `BarterResetTime` is `6` in that sheet and absent from the client
1784 file; Layout 5 adds a u16 `6` at `+0x22`, the only sheet column with
that value.

Three pairs share one value, so the sheet's column order decides:
`FoodConsume` and `DiscountRate` (`100000`), `MaxExchangeCount` and
`OverMaxCount` (`1000000`), and `BarterRange` and
`SpecialBarterInvokationCost` (`5000`), where the f32 type, the same as
`ShipManagementRange`, picks the range. That server's dump holds the
sheet's column names as UTF-16 strings in this order: `FoodConsume`, `ExploreCoolTime`,
`ShipManagementRange`, `VoyageExploreCoolTime`,
`SpecialBarterInvokationCost`, `BarterRange`, `MaxExchangeCount`,
`ResetCoolTime`, `MaxResetCount`, `OverMaxCount`, `AddResetCount`,
`BarterResetTime`, `TimeDiscount`, `ResetNeedCount`, `SubTradeExp`,
`TimeDiscountLimit`, then `KamasylveDiscount`, `SubEmployeeExp`,
`OceanPenaltyMin`, `OceanPenaltyRate` and `OceanPenaltyMax`.

The sheet's `VoyageExploreCoolTime` (`300`), `ResetBarter` (`45504`),
`SpecialBarterInvokationCost`, `ShipMoveEmployeeExp` (`1`) and the three
`OceanPenalty` columns (`1`, `1`, `500000`) have no other match in the
file.

That server's `IslandExplore_Option` loader stores the columns in this
order: `FoodConsume`, `ExploreCoolTime`, `VoyageExploreCoolTime`,
`ShipManagementRange`, `BarterRange`, `SpecialBarterInvokationCost`,
`ResetCoolTime` (i16), `MaxExchangeCount`, `OverMaxCount`,
`MaxResetCount`, `BarterResetTime` (u16), `DiscountRate`,
`AddResetCount`, `ResetNeedCount`, `TimeDiscount`, `TimeDiscountLimit`,
`SubEmployeeExp` and `SubTradeExp` (both i64), `KamasylveDiscount`,
`OceanPenaltyRate`, then `OceanPenaltyMin` and `OceanPenaltyMax` (both
i8). Without `VoyageExploreCoolTime` and `SpecialBarterInvokationCost`
this is the field order of Layout 5 up to `unknown_48`. Read with those
widths, `unknown_15` is the high byte of an i16 `ResetCoolTime`,
`unknown_3c` and `unknown_44` are the high halves of the i64
`SubEmployeeExp` and `SubTradeExp`, and `unknown_48` is
`KamasylveDiscount`. These names rest on the server read only, so the
fields keep their `unknown_` names (see Open Questions).

## Notes

- Clients 1239 to 1261 hold Layout 1 (42 bytes), client 1286 Layout 2
  (54 bytes), client 1309 Layout 3 (82 bytes), clients 1316 to 2703
  Layout 4 (86 bytes) and clients 2736 to 3482 Layout 5 (88 bytes).
  Between them `barter_range` drops from `8000` to `5000` (client 1267),
  `reset_cool_time` from `4` to `2` (client 2519) and
  `ship_management_range` rises from `15000` to `20000` (client 3474).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/greatsea_tables.py`: one
  row with every named field. It reads Layout 5 only.

## Open Questions

### The Value After `sub_trade_exp`

`unknown_48` is `500000`, the value of two sheet columns,
`KamasylveDiscount` and `OceanPenaltyRate`, so the value alone does not
name it. The column strings put `KamasylveDiscount` next to
`SubEmployeeExp`, but the file stores `sub_trade_exp` between them. The
server loader stores `KamasylveDiscount` right after `SubTradeExp` (Field
Names); no client getter or client value confirms it yet.

### The Zero Fields

`unknown_15`, `unknown_3c` and `unknown_44` are `0` on every client
checked. No column of the sheet is `0`; `ShipMoveEmployeeExp`,
`OceanPenaltyMin` and `OceanPenaltyMax` are `1` there and may read `0` in
the client build. The server loader's widths (Field Names) make them the
high parts of `reset_cool_time`, `sub_employee_exp` and `sub_trade_exp`;
a client value above `0xFF` or `0xFFFFFFFF` in one of those fields would
confirm it.
