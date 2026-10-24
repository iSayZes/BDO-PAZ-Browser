# `servantexperience.dbss` Format

## Purpose

Level table of the mounts and ships (servants): one record per servant
character and level, with the EXP to the next level, max HP, stamina and
weight, the four movement stats and the dice that add a random bonus on each
level-up. Each record holds
the stat body of [experience.bss](experience_bss.md) in its middle. On client
3464 the file has 20,885 records for 418 servants.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes     | Records                                 | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | --------- | --------------------------------------- | --------- |
| 2      | 3326 and later | 3483    | `servantexperience.dbss`       | 8,360,280 | 62,655 Body String, 20,885 Level Record | 18        |
| 2      | 3326 and later | 3483    | `servantexperienceoffset.dbss` | 250,624   | 20,885 Index Row                        | 12        |
| 1      | 1338 to 2907   | 2907    | `servantexperience.dbss`       | 7,631,446 | 55,359 Body String, 18,453 Level Record | 18        |
| 1      | 1338 to 2907   | 2907    | `servantexperienceoffset.dbss` | 221,440   | 18,453 Index Row                        | 12        |

| Layout | File                           | Known               | Unknown             |
| ------ | ------------------------------ | ------------------- | ------------------- |
| 2      | `servantexperience.dbss`       | 3,890,890 B (46.5%) | 4,469,390 B (53.5%) |
| 2      | `servantexperienceoffset.dbss` | 250,624 B (100.0%)  | 0 B (0.0%)          |
| 1      | `servantexperience.dbss`       | 3,424,162 B (44.9%) | 4,207,284 B (55.1%) |
| 1      | `servantexperienceoffset.dbss` | 221,440 B (100.0%)  | 0 B (0.0%)          |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `2cd0e3840987`  |
| 3482   | Layout 2             | `2cd0e3840987`  |
| 3474   | Layout 2             | `2cd0e3840987`  |
| 3473   | Layout 2             | `2cd0e3840987`  |
| 3464   | Layout 2             | `2cd0e3840987`  |
| 3458   | Layout 2             | `2cd0e3840987`  |
| 3454   | Layout 2             | `2cd0e3840987`  |
| 3444   | Layout 2             | `2cd0e3840987`  |
| 3435   | Layout 2             | `2cd0e3840987`  |
| 3426   | Layout 2             | `2cd0e3840987`  |
| 3418   | Layout 2             | `2cd0e3840987`  |
| 3412   | Layout 2             | `2cd0e3840987`  |
| 3402   | Layout 2             | `2cd0e3840987`  |
| 3396   | Layout 2             | `2cd0e3840987`  |
| 3387   | Layout 2             | `2cd0e3840987`  |
| 3381   | Layout 2             | `2cd0e3840987`  |
| 3373   | Layout 2             | `2cd0e3840987`  |
| 3364   | Layout 2             | `2cd0e3840987`  |
| 3356   | Layout 2             | `2cd0e3840987`  |
| 3349   | Layout 2             | `2cd0e3840987`  |
| 3342   | Layout 2             | `2cd0e3840987`  |
| 3335   | Layout 2             | `2cd0e3840987`  |
| 3326   | Layout 2             | `2cd0e3840987`  |
| 3321   | No documented layout | `2cd0e3840987`  |
| 3314   | No documented layout | `2cd0e3840987`  |
| 3303   | No documented layout | `2cd0e3840987`  |
| 3302   | No documented layout | `2cd0e3840987`  |
| 3293   | No documented layout | `2cd0e3840987`  |
| 3283   | No documented layout | `2cd0e3840987`  |
| 3275   | No documented layout | `2cd0e3840987`  |
| 3267   | No documented layout | `2cd0e3840987`  |
| 3258   | No documented layout | `2cd0e3840987`  |
| 3251   | No documented layout | `2cd0e3840987`  |
| 3242   | No documented layout | `2cd0e3840987`  |
| 3235   | No documented layout | `2cd0e3840987`  |
| 3229   | No documented layout | `2cd0e3840987`  |
| 3212   | No documented layout | `2cd0e3840987`  |
| 3203   | No documented layout | `2cd0e3840987`  |
| 3193   | No documented layout | `2cd0e3840987`  |
| 3186   | No documented layout | `2cd0e3840987`  |
| 3177   | No documented layout | `2cd0e3840987`  |
| 3169   | No documented layout | `2cd0e3840987`  |
| 3158   | No documented layout | `2cd0e3840987`  |
| 3151   | No documented layout | `2cd0e3840987`  |
| 3144   | No documented layout | `2cd0e3840987`  |
| 3133   | No documented layout | `2cd0e3840987`  |
| 3125   | No documented layout | `2cd0e3840987`  |
| 3118   | No documented layout | `2cd0e3840987`  |
| 3111   | No documented layout | `2cd0e3840987`  |
| 3103   | No documented layout | `2cd0e3840987`  |
| 3095   | No documented layout | `2cd0e3840987`  |
| 3086   | No documented layout | `2cd0e3840987`  |
| 3072   | No documented layout | `2cd0e3840987`  |
| 3062   | No documented layout | `2cd0e3840987`  |
| 3052   | No documented layout | `2cd0e3840987`  |
| 3045   | No documented layout | `2cd0e3840987`  |
| 3037   | No documented layout | `2cd0e3840987`  |
| 3030   | No documented layout | `2cd0e3840987`  |
| 3021   | No documented layout | `2cd0e3840987`  |
| 3012   | No documented layout | `2cd0e3840987`  |
| 3002   | No documented layout | `2cd0e3840987`  |
| 2995   | No documented layout | `2cd0e3840987`  |
| 2987   | No documented layout | `2cd0e3840987`  |
| 2978   | No documented layout | `2cd0e3840987`  |
| 2970   | No documented layout | `2cd0e3840987`  |
| 2959   | No documented layout | `2cd0e3840987`  |
| 2951   | No documented layout | `2cd0e3840987`  |
| 2942   | No documented layout | `2cd0e3840987`  |
| 2935   | No documented layout | `2cd0e3840987`  |
| 2932   | No documented layout | `2cd0e3840987`  |
| 2923   | No documented layout | `2cd0e3840987`  |
| 2919   | No documented layout | `2cd0e3840987`  |
| 2907   | Layout 1             | `2cd0e3840987`  |
| 2900   | Layout 1             | `2cd0e3840987`  |
| 2891   | Layout 1             | `2cd0e3840987`  |
| 2882   | Layout 1             | `2cd0e3840987`  |
| 2872   | Layout 1             | `2cd0e3840987`  |
| 2863   | Layout 1             | `2cd0e3840987`  |
| 2855   | Layout 1             | `2cd0e3840987`  |
| 2849   | Layout 1             | `2cd0e3840987`  |
| 2844   | Layout 1             | `2cd0e3840987`  |
| 2834   | Layout 1             | `2cd0e3840987`  |
| 2825   | Layout 1             | `2cd0e3840987`  |
| 2819   | Layout 1             | `2cd0e3840987`  |
| 2811   | Layout 1             | `2cd0e3840987`  |
| 2803   | Layout 1             | `2cd0e3840987`  |
| 2794   | Layout 1             | `2cd0e3840987`  |
| 2783   | Layout 1             | `2cd0e3840987`  |
| 2774   | Layout 1             | `2cd0e3840987`  |
| 2765   | Layout 1             | `2cd0e3840987`  |
| 2756   | Layout 1             | `2cd0e3840987`  |
| 2750   | Layout 1             | `2cd0e3840987`  |
| 2743   | Layout 1             | `2cd0e3840987`  |
| 2736   | Layout 1             | `2cd0e3840987`  |
| 2726   | Layout 1             | `2cd0e3840987`  |
| 2717   | Layout 1             | `2cd0e3840987`  |
| 2709   | Layout 1             | `2cd0e3840987`  |
| 2703   | Layout 1             | `2cd0e3840987`  |
| 2695   | Layout 1             | `2cd0e3840987`  |
| 2684   | Layout 1             | `2cd0e3840987`  |
| 2672   | Layout 1             | `2cd0e3840987`  |
| 2665   | Layout 1             | `2cd0e3840987`  |
| 2657   | Layout 1             | `2cd0e3840987`  |
| 2649   | Layout 1             | `2cd0e3840987`  |
| 2644   | Layout 1             | `2cd0e3840987`  |
| 2637   | Layout 1             | `2cd0e3840987`  |
| 2629   | Layout 1             | `2cd0e3840987`  |
| 2619   | Layout 1             | `2cd0e3840987`  |
| 2612   | Layout 1             | `2cd0e3840987`  |
| 2606   | Layout 1             | `2cd0e3840987`  |
| 2602   | Layout 1             | `2cd0e3840987`  |
| 2601   | Layout 1             | `2cd0e3840987`  |
| 2592   | Layout 1             | `2cd0e3840987`  |
| 2583   | Layout 1             | `2cd0e3840987`  |
| 2575   | Layout 1             | `2cd0e3840987`  |
| 2567   | Layout 1             | `2cd0e3840987`  |
| 2560   | Layout 1             | `2cd0e3840987`  |
| 2553   | Layout 1             | `2cd0e3840987`  |
| 2545   | Layout 1             | `2cd0e3840987`  |
| 2538   | Layout 1             | `2cd0e3840987`  |
| 2529   | Layout 1             | `2cd0e3840987`  |
| 2519   | Layout 1             | `2cd0e3840987`  |
| 2513   | Layout 1             | `2cd0e3840987`  |
| 2510   | Layout 1             | `2cd0e3840987`  |
| 2507   | Layout 1             | `2cd0e3840987`  |
| 2503   | Layout 1             | `2cd0e3840987`  |
| 2498   | Layout 1             | `2cd0e3840987`  |
| 2492   | Layout 1             | `2cd0e3840987`  |
| 2487   | Layout 1             | `2cd0e3840987`  |
| 2480   | Layout 1             | `2cd0e3840987`  |
| 2474   | Layout 1             | `2cd0e3840987`  |
| 2468   | Layout 1             | `2cd0e3840987`  |
| 2460   | Layout 1             | `2cd0e3840987`  |
| 2453   | Layout 1             | `2cd0e3840987`  |
| 2444   | Layout 1             | `2cd0e3840987`  |
| 2438   | Layout 1             | `2cd0e3840987`  |
| 2434   | Layout 1             | `2cd0e3840987`  |
| 2429   | Layout 1             | `2cd0e3840987`  |
| 2421   | Layout 1             | `2cd0e3840987`  |
| 2414   | Layout 1             | `2cd0e3840987`  |
| 2407   | Layout 1             | `2cd0e3840987`  |
| 2401   | Layout 1             | `2cd0e3840987`  |
| 2397   | Layout 1             | `2cd0e3840987`  |
| 2393   | Layout 1             | `2cd0e3840987`  |
| 2384   | Layout 1             | `2cd0e3840987`  |
| 2378   | Layout 1             | `2cd0e3840987`  |
| 2372   | Layout 1             | `2cd0e3840987`  |
| 2358   | Layout 1             | `2cd0e3840987`  |
| 2352   | Layout 1             | `2cd0e3840987`  |
| 2347   | Layout 1             | `2cd0e3840987`  |
| 2343   | Layout 1             | `2cd0e3840987`  |
| 2335   | Layout 1             | `2cd0e3840987`  |
| 2327   | Layout 1             | `2cd0e3840987`  |
| 2324   | Layout 1             | `2cd0e3840987`  |
| 2319   | Layout 1             | `2cd0e3840987`  |
| 2313   | Layout 1             | `2cd0e3840987`  |
| 2308   | Layout 1             | `2cd0e3840987`  |
| 2302   | Layout 1             | `2cd0e3840987`  |
| 2295   | Layout 1             | `2cd0e3840987`  |
| 2290   | Layout 1             | `2cd0e3840987`  |
| 2284   | Layout 1             | `2cd0e3840987`  |
| 2276   | Layout 1             | `2cd0e3840987`  |
| 2269   | Layout 1             | `2cd0e3840987`  |
| 2259   | Layout 1             | `2cd0e3840987`  |
| 2250   | Layout 1             | `2cd0e3840987`  |
| 2243   | Layout 1             | `2cd0e3840987`  |
| 2235   | Layout 1             | `2cd0e3840987`  |
| 2229   | Layout 1             | `2cd0e3840987`  |
| 2224   | Layout 1             | `2cd0e3840987`  |
| 2218   | Layout 1             | `2cd0e3840987`  |
| 2215   | Layout 1             | `2cd0e3840987`  |
| 2207   | Layout 1             | `2cd0e3840987`  |
| 2203   | Layout 1             | `2cd0e3840987`  |
| 2196   | Layout 1             | `2cd0e3840987`  |
| 2192   | Layout 1             | `2cd0e3840987`  |
| 2189   | Layout 1             | `2cd0e3840987`  |
| 2183   | Layout 1             | `2cd0e3840987`  |
| 2179   | Layout 1             | `2cd0e3840987`  |
| 2171   | Layout 1             | `2cd0e3840987`  |
| 2163   | Layout 1             | `2cd0e3840987`  |
| 2156   | Layout 1             | `2cd0e3840987`  |
| 2151   | Layout 1             | `2cd0e3840987`  |
| 2147   | Layout 1             | `2cd0e3840987`  |
| 2142   | Layout 1             | `2cd0e3840987`  |
| 2138   | Layout 1             | `2cd0e3840987`  |
| 2134   | Layout 1             | `2cd0e3840987`  |
| 2130   | Layout 1             | `2cd0e3840987`  |
| 2122   | Layout 1             | `2cd0e3840987`  |
| 2107   | Layout 1             | `2cd0e3840987`  |
| 2098   | Layout 1             | `2cd0e3840987`  |
| 2089   | Layout 1             | `2cd0e3840987`  |
| 2081   | Layout 1             | `2cd0e3840987`  |
| 2073   | Layout 1             | `2cd0e3840987`  |
| 2067   | Layout 1             | `2cd0e3840987`  |
| 2063   | Layout 1             | `2cd0e3840987`  |
| 2059   | Layout 1             | `2cd0e3840987`  |
| 2052   | Layout 1             | `2cd0e3840987`  |
| 2044   | Layout 1             | `2cd0e3840987`  |
| 2039   | Layout 1             | `2cd0e3840987`  |
| 2032   | Layout 1             | `2cd0e3840987`  |
| 2025   | Layout 1             | `2cd0e3840987`  |
| 2011   | Layout 1             | `2cd0e3840987`  |
| 2005   | Layout 1             | `2cd0e3840987`  |
| 2000   | Layout 1             | `2cd0e3840987`  |
| 1996   | Layout 1             | `2cd0e3840987`  |
| 1991   | Layout 1             | `2cd0e3840987`  |
| 1985   | Layout 1             | `2cd0e3840987`  |
| 1980   | Layout 1             | `2cd0e3840987`  |
| 1969   | Layout 1             | `2cd0e3840987`  |
| 1964   | Layout 1             | `2cd0e3840987`  |
| 1958   | Layout 1             | `2cd0e3840987`  |
| 1950   | Layout 1             | `2cd0e3840987`  |
| 1945   | Layout 1             | `2cd0e3840987`  |
| 1937   | Layout 1             | `2cd0e3840987`  |
| 1933   | Layout 1             | `2cd0e3840987`  |
| 1927   | Layout 1             | `2cd0e3840987`  |
| 1921   | Layout 1             | `2cd0e3840987`  |
| 1914   | Layout 1             | `2cd0e3840987`  |
| 1908   | Layout 1             | `2cd0e3840987`  |
| 1897   | Layout 1             | `2cd0e3840987`  |
| 1892   | Layout 1             | `2cd0e3840987`  |
| 1886   | Layout 1             | `2cd0e3840987`  |
| 1881   | Layout 1             | `2cd0e3840987`  |
| 1871   | Layout 1             | `2cd0e3840987`  |
| 1866   | Layout 1             | `2cd0e3840987`  |
| 1862   | Layout 1             | `2cd0e3840987`  |
| 1854   | Layout 1             | `2cd0e3840987`  |
| 1846   | Layout 1             | `2cd0e3840987`  |
| 1838   | Layout 1             | `2cd0e3840987`  |
| 1832   | Layout 1             | `2cd0e3840987`  |
| 1826   | Layout 1             | `2cd0e3840987`  |
| 1822   | Layout 1             | `2cd0e3840987`  |
| 1818   | Layout 1             | `2cd0e3840987`  |
| 1804   | Layout 1             | `2cd0e3840987`  |
| 1794   | Layout 1             | `2cd0e3840987`  |
| 1790   | Layout 1             | `2cd0e3840987`  |
| 1784   | Layout 1             | `2cd0e3840987`  |
| 1774   | Layout 1             | `2cd0e3840987`  |
| 1771   | Layout 1             | `2cd0e3840987`  |
| 1762   | Layout 1             | `2cd0e3840987`  |
| 1759   | Layout 1             | `2cd0e3840987`  |
| 1754   | Layout 1             | `2cd0e3840987`  |
| 1749   | Layout 1             | `2cd0e3840987`  |
| 1743   | Layout 1             | `2cd0e3840987`  |
| 1737   | Layout 1             | `2cd0e3840987`  |
| 1731   | Layout 1             | `2cd0e3840987`  |
| 1725   | Layout 1             | `2cd0e3840987`  |
| 1717   | Layout 1             | `2cd0e3840987`  |
| 1710   | Layout 1             | `2cd0e3840987`  |
| 1704   | Layout 1             | `2cd0e3840987`  |
| 1698   | Layout 1             | `2cd0e3840987`  |
| 1690   | Layout 1             | `2cd0e3840987`  |
| 1685   | Layout 1             | `2cd0e3840987`  |
| 1680   | Layout 1             | `2cd0e3840987`  |
| 1674   | Layout 1             | `2cd0e3840987`  |
| 1668   | Layout 1             | `2cd0e3840987`  |
| 1659   | Layout 1             | `2cd0e3840987`  |
| 1649   | Layout 1             | `2cd0e3840987`  |
| 1642   | Layout 1             | `2cd0e3840987`  |
| 1636   | Layout 1             | `2cd0e3840987`  |
| 1628   | Layout 1             | `2cd0e3840987`  |
| 1622   | Layout 1             | `2cd0e3840987`  |
| 1614   | Layout 1             | `2cd0e3840987`  |
| 1608   | Layout 1             | `2cd0e3840987`  |
| 1602   | Layout 1             | `2cd0e3840987`  |
| 1598   | Layout 1             | `2cd0e3840987`  |
| 1594   | Layout 1             | `2cd0e3840987`  |
| 1590   | Layout 1             | `2cd0e3840987`  |
| 1587   | Layout 1             | `2cd0e3840987`  |
| 1584   | Layout 1             | `2cd0e3840987`  |
| 1579   | Layout 1             | `2cd0e3840987`  |
| 1572   | Layout 1             | `2cd0e3840987`  |
| 1565   | Layout 1             | `2cd0e3840987`  |
| 1559   | Layout 1             | `2cd0e3840987`  |
| 1554   | Layout 1             | `2cd0e3840987`  |
| 1547   | Layout 1             | `2cd0e3840987`  |
| 1537   | Layout 1             | `2cd0e3840987`  |
| 1529   | Layout 1             | `2cd0e3840987`  |
| 1524   | Layout 1             | `2cd0e3840987`  |
| 1519   | Layout 1             | `2cd0e3840987`  |
| 1509   | Layout 1             | `2cd0e3840987`  |
| 1506   | Layout 1             | `2cd0e3840987`  |
| 1504   | Layout 1             | `2cd0e3840987`  |
| 1500   | Layout 1             | `2cd0e3840987`  |
| 1493   | Layout 1             | `2cd0e3840987`  |
| 1489   | Layout 1             | `2cd0e3840987`  |
| 1485   | Layout 1             | `2cd0e3840987`  |
| 1481   | Layout 1             | `2cd0e3840987`  |
| 1474   | Layout 1             | `2cd0e3840987`  |
| 1466   | Layout 1             | `2cd0e3840987`  |
| 1462   | Layout 1             | `2cd0e3840987`  |
| 1459   | Layout 1             | `2cd0e3840987`  |
| 1453   | Layout 1             | `2cd0e3840987`  |
| 1450   | Layout 1             | `2cd0e3840987`  |
| 1445   | Layout 1             | `2cd0e3840987`  |
| 1439   | Layout 1             | `2cd0e3840987`  |
| 1433   | Layout 1             | `2cd0e3840987`  |
| 1430   | Layout 1             | `2cd0e3840987`  |
| 1426   | Layout 1             | `2cd0e3840987`  |
| 1421   | Layout 1             | `2cd0e3840987`  |
| 1417   | Layout 1             | `2cd0e3840987`  |
| 1416   | Layout 1             | `2cd0e3840987`  |
| 1409   | Layout 1             | `2cd0e3840987`  |
| 1405   | Layout 1             | `2cd0e3840987`  |
| 1401   | Layout 1             | `2cd0e3840987`  |
| 1396   | Layout 1             | `2cd0e3840987`  |
| 1391   | Layout 1             | `2cd0e3840987`  |
| 1390   | Layout 1             | `2cd0e3840987`  |
| 1386   | Layout 1             | `2cd0e3840987`  |
| 1381   | Layout 1             | `2cd0e3840987`  |
| 1379   | Layout 1             | `2cd0e3840987`  |
| 1372   | Layout 1             | `2cd0e3840987`  |
| 1366   | Layout 1             | `2cd0e3840987`  |
| 1364   | Layout 1             | `2cd0e3840987`  |
| 1363   | Layout 1             | `2cd0e3840987`  |
| 1360   | Layout 1             | `2cd0e3840987`  |
| 1358   | Layout 1             | `2cd0e3840987`  |
| 1355   | Layout 1             | `2cd0e3840987`  |
| 1351   | Layout 1             | `2cd0e3840987`  |
| 1348   | Layout 1             | `2cd0e3840987`  |
| 1346   | Layout 1             | `2cd0e3840987`  |
| 1341   | Layout 1             | `2cd0e3840987`  |
| 1340   | Layout 1             | `2cd0e3840987`  |
| 1338   | Layout 1             | `2cd0e3840987`  |
| 1335   | No documented layout | `2cd0e3840987`  |
| 1333   | No documented layout | `2cd0e3840987`  |
| 1329   | No documented layout | `2cd0e3840987`  |
| 1327   | No documented layout | `2cd0e3840987`  |
| 1324   | No documented layout | `2cd0e3840987`  |
| 1321   | No documented layout | `2cd0e3840987`  |
| 1319   | No documented layout | `2cd0e3840987`  |
| 1318   | No documented layout | `2cd0e3840987`  |
| 1316   | No documented layout | `2cd0e3840987`  |
| 1313   | No documented layout | `2cd0e3840987`  |
| 1311   | No documented layout | `2cd0e3840987`  |
| 1309   | No documented layout | `2cd0e3840987`  |
| 1304   | No documented layout | `2cd0e3840987`  |
| 1292   | No documented layout | `2cd0e3840987`  |
| 1286   | No documented layout | `2cd0e3840987`  |
| 1280   | No documented layout | `2cd0e3840987`  |
| 1276   | No documented layout | `2cd0e3840987`  |
| 1267   | No file              | `2cd0e3840987`  |
| 1261   | No file              | `2cd0e3840987`  |
| 1256   | No documented layout | `2cd0e3840987`  |
| 1250   | No file              | `2cd0e3840987`  |
| 1246   | No file              | `2cd0e3840987`  |
| 1239   | No file              | `2cd0e3840987`  |
| 1230   | No file              | `2cd0e3840987`  |
| 1226   | No file              | `2cd0e3840987`  |
| 1220   | No file              | `2cd0e3840987`  |
| 1217   | No file              | `2cd0e3840987`  |
| 1211   | No file              | `2cd0e3840987`  |
| 1210   | No file              | `2cd0e3840987`  |
| 1208   | No file              | `2cd0e3840987`  |
| 1203   | No file              | `2cd0e3840987`  |
| 1197   | No file              | `2cd0e3840987`  |
| 1194   | No file              | `2cd0e3840987`  |
| 1192   | No file              | `2cd0e3840987`  |
| 1187   | No file              | `2cd0e3840987`  |
| 1183   | No file              | `2cd0e3840987`  |
| 1177   | No file              | `2cd0e3840987`  |
| 1173   | No file              | `2cd0e3840987`  |
| 1167   | No file              | `2cd0e3840987`  |
| 1164   | No file              | `2cd0e3840987`  |
| 1156   | No file              | `2cd0e3840987`  |
| 1149   | No file              | `2cd0e3840987`  |
| 1144   | No file              | `2cd0e3840987`  |
| 1137   | No file              | `2cd0e3840987`  |
| 1132   | No file              | `2cd0e3840987`  |
| 1127   | No file              | `2cd0e3840987`  |
| 1122   | No file              | `2cd0e3840987`  |
| 1118   | No file              | `2cd0e3840987`  |
| 1114   | No file              | `2cd0e3840987`  |
| 1109   | No file              | `2cd0e3840987`  |
| 1102   | No file              | `2cd0e3840987`  |
| 1096   | No file              | `2cd0e3840987`  |
| 1088   | No file              | `2cd0e3840987`  |
| 1081   | No file              | `2cd0e3840987`  |
| 1076   | No file              | `2cd0e3840987`  |
| 1069   | No file              | `2cd0e3840987`  |
| 1064   | No file              | `2cd0e3840987`  |
| 1058   | No file              | `2cd0e3840987`  |
| 1051   | No file              | `2cd0e3840987`  |
| 1044   | No file              | `2cd0e3840987`  |
| 1036   | No file              | `2cd0e3840987`  |
| 1026   | No file              | `2cd0e3840987`  |
| 1016   | No file              | `2cd0e3840987`  |
| 1009   | No file              | `2cd0e3840987`  |
| 1005   | No file              | `2cd0e3840987`  |
| 1000   | No file              | `2cd0e3840987`  |
| 998    | No file              | `2cd0e3840987`  |
| 990    | No file              | `2cd0e3840987`  |
| 979    | No file              | `2cd0e3840987`  |
| 972    | No file              | `2cd0e3840987`  |
| 963    | No file              | `2cd0e3840987`  |
| 955    | No file              | `2cd0e3840987`  |
| 946    | No file              | `2cd0e3840987`  |
| 938    | No file              | `2cd0e3840987`  |
| 927    | No file              | `2cd0e3840987`  |
| 911    | No file              | `2cd0e3840987`  |
| 904    | No file              | `2cd0e3840987`  |
| 899    | No file              | `2cd0e3840987`  |
| 894    | No file              | `2cd0e3840987`  |
| 885    | No file              | `2cd0e3840987`  |
| 879    | No file              | `2cd0e3840987`  |
| 872    | No file              | `2cd0e3840987`  |
| 864    | No file              | `2cd0e3840987`  |
| 855    | No file              | `2cd0e3840987`  |
| 853    | No file              | `2cd0e3840987`  |
| 845    | No file              | `2cd0e3840987`  |
| 837    | No file              | `2cd0e3840987`  |
| 829    | No file              | `2cd0e3840987`  |
| 822    | No file              | `2cd0e3840987`  |
| 814    | No file              | `2cd0e3840987`  |
| 805    | No file              | `2cd0e3840987`  |
| 794    | No file              | `2cd0e3840987`  |
| 787    | No file              | `2cd0e3840987`  |
| 780    | No file              | `2cd0e3840987`  |
| 771    | No file              | `2cd0e3840987`  |
| 760    | No file              | `2cd0e3840987`  |
| 748    | No file              | `2cd0e3840987`  |
| 741    | No file              | `2cd0e3840987`  |
| 736    | No file              | `2cd0e3840987`  |
| 731    | No file              | `2cd0e3840987`  |
| 723    | No file              | `2cd0e3840987`  |
| 711    | No file              | `2cd0e3840987`  |
| 707    | No file              | `2cd0e3840987`  |
| 697    | No file              | `2cd0e3840987`  |
| 689    | No file              | `2cd0e3840987`  |
| 683    | No file              | `2cd0e3840987`  |
| 678    | No file              | `2cd0e3840987`  |
| 670    | No file              | `2cd0e3840987`  |
| 661    | No file              | `2cd0e3840987`  |
| 656    | No file              | `2cd0e3840987`  |
| 652    | No file              | `2cd0e3840987`  |
| 643    | No file              | `2cd0e3840987`  |
| 637    | No file              | `2cd0e3840987`  |
| 630    | No file              | `2cd0e3840987`  |
| 627    | No file              | `2cd0e3840987`  |
| 621    | No file              | `2cd0e3840987`  |
| 617    | No file              | `2cd0e3840987`  |
| 615    | No file              | `2cd0e3840987`  |
| 606    | No file              | `2cd0e3840987`  |
| 599    | No file              | `2cd0e3840987`  |
| 592    | No file              | `2cd0e3840987`  |
| 586    | No file              | `2cd0e3840987`  |
| 577    | No file              | `2cd0e3840987`  |
| 569    | No file              | `2cd0e3840987`  |
| 561    | No file              | `2cd0e3840987`  |
| 554    | No file              | `2cd0e3840987`  |
| 542    | No file              | `2cd0e3840987`  |
| 532    | No file              | `2cd0e3840987`  |
| 531    | No file              | `2cd0e3840987`  |
| 526    | No file              | `2cd0e3840987`  |
| 521    | No file              | `2cd0e3840987`  |
| 517    | No file              | `2cd0e3840987`  |
| 510    | No file              | `2cd0e3840987`  |
| 508    | No file              | `2cd0e3840987`  |
| 504    | No file              | `2cd0e3840987`  |
| 497    | No file              | `2cd0e3840987`  |
| 491    | No file              | `2cd0e3840987`  |
| 485    | No file              | `2cd0e3840987`  |
| 478    | No file              | `2cd0e3840987`  |
| 472    | No file              | `2cd0e3840987`  |
| 466    | No file              | `2cd0e3840987`  |
| 457    | No file              | `2cd0e3840987`  |
| 452    | No file              | `2cd0e3840987`  |
| 449    | No file              | `2cd0e3840987`  |
| 435    | No file              | `2cd0e3840987`  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                                          |
| ------------------------------- | -------- | ----------------------------------------------------------------------------- |
| `servantexperienceoffset.dbss`  | Required | Key to `(offset, size)` index of the records                                  |
| `languagedata_en.loc`           | Optional | Servant names (LOC type 6, `str_id1` = `character_id`)                        |

[servantexperiencemaxlevel.bss](servantexperiencemaxlevel_bss.md) holds each
servant's top level; the handler does not need it, since the records give the
same number.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type                | Field   | Notes                                         |
| ------- | ------------------- | ------- | --------------------------------------------- |
| `+0x00` | u32                 | count   | 20,885 on client 3464; equals the index count |
| `+0x04` | Level Record[count] | records | Back to back, variable size                   |

The record sizes sum to the file size minus 4.

### Level Record (variable: 250 bytes + strings)

352 to 412 bytes on client 3464. The record size is 352 plus twice the
characters of the six dice strings. Offsets after `+0xAA` follow the strings.

| Offset              | Type            | Field        | Notes                                                                 |
| ------------------- | --------------- | ------------ | --------------------------------------------------------------------- |
| `+0x00`             | u16             | character_id | Servant character, as in `characterstatic.dbss`                       |
| `+0x02`             | i32             | level        | 0 to the servant's top level                                          |
| `+0x06`             | u64             | exp          | EXP from `level` to `level + 1` (Notes)                               |
| `+0x0E`             | f32             | max_hp       | Max HP, shown as is; `1.0` at level 0                                 |
| `+0x12`             | u32             | max_mp       | Max stamina (`getMaxMp()`), shown as is; 0 on ships; `1` at level 0   |
| `+0x16`             | bytes[20]       | unknown_16   | Always 0                                                              |
| `+0x2A`             | f32             | unknown_2a   | `1.0` at level 0, else 0                                              |
| `+0x2E`             | bytes[20]       | unknown_2e   | Always 0                                                              |
| `+0x42`             | u32             | max_critical_rate | Always `5`                                                       |
| `+0x46`             | u32             | max_drop_item_luck | Always `5`                                                      |
| `+0x4A`             | u32             | max_fishing_luck | Always `5`                                                        |
| `+0x4E`             | u32             | max_collection_luck | Always `5`                                                     |
| `+0x52`             | i64             | max_weight   | Max weight, LT x 10,000; 0 at level 0                                 |
| `+0x5A`             | f32             | unknown_5a   | Always `1.0`                                                          |
| `+0x5E`             | bytes[16]       | unknown_5e   | Always 0                                                              |
| `+0x6E`             | u32[3]          | max_varied_speed | Always `10, 10, 10`: attack, movement and casting speed limits (Field Names) |
| `+0x7A`             | f32             | unknown_7a   | `1.0` at level 0, else 0                                              |
| `+0x7E`             | bytes[12]       | unknown_7e   | Always 0                                                              |
| `+0x8A`             | u32[8]          | stats        | By `ServantStatType` (Enum Values), percent x 10,000                  |
| `+0xAA`             | Body String[3]  | unknown_aa   | Always `1D1` and 0; the parser keeps the strings as `unknown_aa` and the u32s as `unknown_aa_values` |
| `unknown_aa+0x00`   | bytes[48]       | unknown_e0   | Always 0                                                              |
| `unknown_aa+0x30`   | str16[6]        | growth_dice  | Level-up bonus dice: HP, stamina, acceleration, speed, cornering, brake (Notes) |
| `growth_dice+0x00`  | bytes[32]       | unknown_end  | Always 0                                                              |

Every byte from `+0x0E` to `+0xA9` that has no name is 0 in every record on
client 3464.

### Body String (variable: 12 bytes + text)

| Offset            | Type  | Field           | Notes                     |
| ----------------- | ----- | --------------- | ------------------------- |
| `+0x00`           | str16 | unknown_00      | Always `1D1`              |
| `unknown_00+0x00` | u32   | unknown_tail_00 | Always 0                  |

### `servantexperienceoffset.dbss`

| Offset  | Type             | Field   | Notes                                |
| ------- | ---------------- | ------- | ------------------------------------ |
| `+0x00` | u32              | count   | Number of entries                    |
| `+0x04` | Index Row[count] | entries | `count` entries of 12 bytes          |

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                                      |
| ------- | ---- | ------ | ---------------------------------------------------------- |
| `+0x00` | u32  | key    | `level << 16 \| character_id`; the first 4 bytes of the record |
| `+0x04` | u32  | offset | Byte offset of the record in `servantexperience.dbss`      |
| `+0x08` | u32  | size   | Record size in bytes                                       |

The index is not in file order: the first entry is level 0 of character
31017, whose record sits after its level 1 record.

## Layout 1

On client 1784 a record holds the sheet's `StunGauge` as an i16 at `+0x16`
(Field Names), so every later field sits 2 bytes further on; `unknown_5e`
is 12 bytes longer and `unknown_7e` 4 bytes shorter, and a u32 follows
`unknown_e0`. A record is 14 bytes longer than in Layout 2.

### Level Record (variable: 264 bytes + strings)

| Offset              | Type            | Field             | Notes                                          |
| ------------------- | --------------- | ----------------- | ---------------------------------------------- |
| `+0x00`             | u16             | character_id      |                                                |
| `+0x02`             | i32             | level             |                                                |
| `+0x06`             | u64             | exp               |                                                |
| `+0x0E`             | f32             | max_hp            |                                                |
| `+0x12`             | u32             | max_mp            |                                                |
| `+0x16`             | i16             | unknown_old_16    | `100` on every record on client 1784; the sheet's `StunGauge` |
| `+0x18`             | bytes[20]       | unknown_16        | Always 0                                       |
| `+0x2C`             | f32             | unknown_2a        | `1.0` at level 0, else 0                       |
| `+0x30`             | bytes[20]       | unknown_2e        | Always 0                                       |
| `+0x44`             | u32             | max_critical_rate | Always `5`                                     |
| `+0x48`             | u32             | max_drop_item_luck | Always `5`                                    |
| `+0x4C`             | u32             | max_fishing_luck  | Always `5`                                     |
| `+0x50`             | u32             | max_collection_luck | Always `5`                                   |
| `+0x54`             | i64             | max_weight        |                                                |
| `+0x5C`             | f32             | unknown_5a        | Always `1.0`                                   |
| `+0x60`             | bytes[28]       | unknown_5e        | Always 0                                       |
| `+0x7C`             | u32[3]          | max_varied_speed  | Always `10, 10, 10`                            |
| `+0x88`             | f32             | unknown_7a        | `1.0` at level 0, else 0                       |
| `+0x8C`             | bytes[8]        | unknown_7e        | Always 0                                       |
| `+0x94`             | u32[8]          | stats             |                                                |
| `+0xB4`             | Body String[3]  | unknown_aa        | Always `1D1` and 0                             |
| `unknown_aa+0x00`   | bytes[48]       | unknown_e0        | Always 0                                       |
| `unknown_aa+0x30`   | u32             | unknown_after_unknown_e0 | `1000000` on every record on client 1784      |
| `unknown_aa+0x34`   | str16[6]        | growth_dice       | `1D1` x 6 on client 1784, empty on 281 records |
| `growth_dice+0x00`  | bytes[32]       | unknown_end       | Always 0                                       |

On the 9,850 records client 1784 shares with client 3473 the fields from
`max_critical_rate` to `max_weight`, `max_varied_speed` and `stats` hold
the same bytes in both on all but 15 records.

## Enum Values

`stats` follows `CppEnums.ServantStatType`, the order
[sailstatdata.bss](masterystatdata_bss.md) uses for its eight values:

| Index | Offset  | Name                  | Values on client 3464                  |
| ----- | ------- | --------------------- | -------------------------------------- |
| 0     | `+0x8A` | `Type_Acceleration`   | 200,000 to 2,000,000                   |
| 1     | `+0x8E` | `Type_MaxMoveSpeed`   | 200,000 to 2,000,000                   |
| 2     | `+0x92` | `Type_CorneringSpeed` | 200,000 to 2,000,000                   |
| 3     | `+0x96` | `Type_BrakeSpeed`     | 200,000 to 2,000,000                   |
| 4     | `+0x9A` | `Type_CannonCoolTime` | Always 0                               |
| 5     | `+0x9E` | `Type_CannonAccuracy` | Always 0                               |
| 6     | `+0xA2` | `Type_MaxLength`      | Always 0                               |
| 7     | `+0xA6` | `Type_MaxAngle`       | Always 0                               |

## Notes

- A servant's base HP and stamina in game are its level row plus the
  `max_hp` and `max_mp` of its own character record in
  [characterstatic.dbss](characterstatic_dbss.md): 500.0 and 1 on 309 of
  the horses in `servant.bss` (client 3474). Checked in game on client 3474
  (2026-10-20) in Horse Growth Info, each horse picked out by its Base
  Coat breed ([bdoservanttitless.bss](bdoservanttitless_bss.md)):

  | Horse | Level 1 row HP, stamina | Shown HP, stamina |
  | ----- | ----------------------- | ----------------- |
  | 9953 and 9915 (tier 6) | 1,630, 3,400 | 2,130, 3,401 |
  | 9890 (tier 8) | 1,792, 3,408 | 2,292, 3,409 |
  | 31619 (Mythical Arduanatt) | 2,140, 3,540 | 2,640, 3,541 |
  | 9909, 31529 or 31624 (tier 6 Breed 1) | 1,594, 3,240 | 2,094, 3,241 |

  The movement stats match the row without an offset, and the shown base
  does not change with mount level, Training level, Mount Brand or the
  Horse Gear Set. The maximums carry the same +500 and +1.
- The stable window (`panel_dialog_servantinfo_all_1.luac`, decompiled with
  unluac) shows the four speed stats as
  `servantInfo:getStat(CppEnums.ServantStatType.Type_*) / 10000` with one
  decimal and `%`, so `1375000` reads 137.5%. On every horse the first two
  values are equal and so are the last two; only eleven ships differ
  (Epheria Galleon, Improved Galley, Panokseon, the four Epheria Carracks and
  four rowboats). The bexcel `Servant_Table` settles the acceleration and
  speed order: on the 8 ships where its `AccelerationRate` and
  `MaxMoveSpeedRate` differ, `+0x8A` holds the first and `+0x8E` the second
  (see Field Names).
- On client 3464, 401 of the 418 servants keep the same `stats` on every
  level from 1, and `max_hp`, `max_mp` and `max_weight` grow from level 1 to
  level 30 (312 servants grow all three, 4 keep `max_mp`). On 159 of the 161
  servants with levels 0 to 100, levels 31 to 100 repeat the level 30 values
  of the three.
- I checked the HP, stamina, weight and dice readings on a level 30 Mythical
  Arduanatt (every Arduanatt and Mythical Arduanatt row holds the same values
  and `1D13` x 6, client 3464). The Detailed Stats window shows inherent
  weight 180 LT and current and max 209 LT, the level 1 and level 30
  `max_weight`. The last level-up added HP 1,145, stamina 547 and weight
  1 LT; the table steps from level 29 to 30 are 1,140, 540 and 1 LT, so HP
  and stamina got a roll of 5 and 7 on top and weight none. Speed, Accel.,
  Turn and Brake grew 1.0%, 1.3%, 1.0% and 1.2%, rolls of 10, 13, 10 and 12
  in 0.1% steps, while `stats` stays the same. The max column is the table
  plus 13 on each of the 29 level-ups: HP 36,077 is 35,200 + 500 + 377 and
  stamina 19,578 is 19,200 + 1 + 377, where 500 and 1 are this horse's
  inherent HP 2,640 and stamina 3,541 above the level 1 row; speed and accel
  175.2% and turn and brake 160.2% are 137.5% and 122.5% + 37.7%.
- The Growth Calculator (`panel_dialog_servantsimulator_2.luac`) gives the
  same horse at levels 1, 5 and 10 an HP increase of 1,141 to 1,153 and a
  stamina increase of 541 to 553, 13 values at 7.6923% (1/13) each: the table
  step (1,140 and 540 on every Arduanatt level from 1 to 30) plus a uniform
  `1D13`. The four movement stats show 0.4% to 1.3% in ten steps of 10% with
  Training Artisan 7 selected. The top is the `1D13` maximum; the floor is a
  Training level bonus, since the Lua reads each movement minimum twice
  through `getVariedStat_MinMax(type, isMin, level + 1, applyBonus,
  lifeLevel)`, with and without the bonus, and the HP and stamina minimums
  stay at step + 1. The bonus is `add_servant_stat_rate` of
  [traininglevelskillstat.bss](traininglevelskillstat_bss.md) (Notes
  below).
- The movement floor rises with Training level and every value from the
  floor to the die maximum stays equally likely. The floor die value is
  `1 + round(die max x add_servant_stat_rate / 1,000,000)`. I checked it in
  the calculator on a `1D13` Mythical Arduanatt and a `1D10` tier 6 horse
  (`add_servant_stat_rate` from client 3464):

  | Horse         | Training  | Rate    | Die max x rate | Range shown           |
  | ------------- | --------- | ------- | -------------- | --------------------- |
  | `1D13`        | Artisan 2 | 192,000 | 2.496          | 0.3 to 1.3, 9.0909%   |
  | `1D13`        | Artisan 7 | 214,000 | 2.782          | 0.4 to 1.3, 10%       |
  | `1D13`        | Master 10 | 273,500 | 3.556          | 0.5 to 1.3, 11.1111%  |
  | `1D10`        | Artisan 7 | 214,000 | 2.14           | 0.3 to 1.0, 12.5%     |
  | `1D10`        | Master 10 | 273,500 | 2.735          | 0.4 to 1.0, 14.2857%  |

  Artisan 2 on the `1D13` horse sits just under a rounding boundary, which
  rules out rounding up; the `1D10` horse rules out a fixed 13.
- The tier 6 horse matches the tier 6 rows with 121% in all four movement
  stats (for example character 9815): HP steps of 630 and stamina steps of
  400, so the calculator's 631 to 640 and 401 to 410 are step + `1D10`.
- `growth_dice` slot 1 is stamina: Giorga Viento (9894) has `1D1-1` (0)
  there and a `max_mp` of 999 on every level. `1D1-1` x 6 is also the level 0
  value, and 93 level 0 rows hold six empty strings.
- The EXP bar is `getExp_s64() / getNeedExp_s64()`, so the EXP restarts on
  every level, as in [nodeexperience](nodeexperience_bss.md); `exp` reads as
  that need. It never falls with level on the 416 servants with all levels.
  Level 0 holds 100 or 1 and is a placeholder like `experience.bss` level 0.
- Level counts on client 3464: 161 servants with levels 0 to 100, 132 with
  0 to 30, 95 with 0 to 1, 20 with 0 to 15, 3 with 0 to 10, 2 with 0 to 20
  and 5 with level 0 only. Traveler's Horse (31560) and Doom's Shadow (31577)
  have only levels 0 and 30.
- The six dice are equal on most rows (`1D10` x 6 on 4,943 rows on client
  3464, Doom `1D13` x 6). Beginner's Brown Horse (9001) has
  `1D5, 1D5, 1D3, 1D3, 1D3, 1D3` and Giorga Viento (9894)
  `1D5, 1D1-1, 1D1, 1D1, 1D1, 1D1`. On 331 of the 413 servants with levels
  from 1 every level holds one dice set.
- The parser is `_dbss/servantexperience/parser.py`. The handler splits
  `stats` into `acceleration`, `speed`, `turn`, `brake` and the four
  `cannon_stats`, keeps the three `1D1` strings as `unknown_aa` and their
  u32s as `unknown_aa_values`, and the offset table splits each key into
  `character_id` and `level`.
- Record `+0x0A` is the start of the `experience.bss` stat body: `+0x0E` is
  body `+0x04`, `+0x42` body `+0x38`, `+0x6E` body `+0x64` and `+0xAA` body
  `+0xA0`. The `5` at `+0x42` has no counterpart in `experience.bss`, whose
  body `+0x38` is 0. `max_hp`, `max_mp` and `max_weight` are body `+0x04`,
  `+0x08` and `+0x48`; `characterstatic.dbss` sets body `+0x48` to values
  such as `100000` and `10000000`.
- The three `1D1` strings at `+0xAA` sit where the `experience.bss` body has
  three always-0 u32 pairs, and string index 0 of that file is `1D1`.

## Field Names

The names follow the `Servant_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (9,893 (character, level) rows shared with client 3473) and the `Servant_Table` of a second private server on client 519 (7,241 rows), matched value by value at every offset of the fixed part:

| Column | Field | Equal (client 1784) | Equal (client 519) |
| ------ | ----- | -------------- | -------------- |
| `RequireEXP` | `exp` | 9,887 | 7,235 |
| `HP` | `max_hp` | 9,549 | 6,914 |
| `MP` | `max_mp` | 9,181 | |
| `possessableWeight` | `max_weight` (i64) | 9,879 | 7,225 |
| `AccelerationRate` | `stats[0]` | 9,891 | 7,148 |
| `MaxMoveSpeedRate` | `stats[1]` | 9,891 | 7,148 |
| `CorneringSpeedRate`, `BrakeSpeedRate` | `stats[2]`, `stats[3]` | 9,891 | 7,148 |

`AccelerationRate` equals `stats[1]` on 8 fewer rows than `stats[0]`, and `MaxMoveSpeedRate` the other way round: the 8 ships 9032, 9049, 9050 and 9075 (the four rowboats) and 31054 to 31057 (the four Epheria Carracks) have a lower acceleration than speed in both. `CorneringSpeedRate` and `BrakeSpeedRate` are equal on every row and keep the enum order.

The constants are placed by value: the sheet's only columns that hold `5` on every row are `MaxCriticalRate`, `MaxDropItemLuck`, `MaxFishingLuck` and `MaxCollectionLuck`, the four u32 at `+0x42`, and its only `10` columns are `MaxAttackSpeed`, `MaxMoveSpeed` and `MaxCastingSpeed`, the three at `+0x6E`. The 2016 client (build of 2016-01-11) ships with debug symbols; its `gc::CharacterStatStaticStatus` holds `_maxCriticalHitPoint`, `_maxDropItemPoint`, `_maxFishingPoint` and `_maxCollectionPoint` in that order, which splits the four `5`s, and `_maxVariedSpeedPoint` as one array of three. Which index of `max_varied_speed` is attack, movement or casting is not settled by the data; the [experience.bss](experience_bss.md#the-max_varied_speed-order) Open Questions hold the character window Lua lead.

`growth_dice` follows the sheet columns `VariedMaxHP`, `VariedMaxMP`, `VariedAccelerationRate`, `VariedMaxMoveSpeedRate`, `VariedCorneringSpeedRate` and `VariedBrakeSpeedRate`, and the 2016 `_variedMaxHp`, `_variedMaxMp` and `_variedStat[4]`, which the 2016 `LoadServantExperienceStaticInformation` reads from those columns in that order. The bexcel holds `0` in all six columns and the private server's own file `1D1`, so only the order ties the four movement slots to their stats; client 3473 rolls the same die in all four on every servant.

The private server's own `servantexperience.dbss` (client 1784, 10,869 records) stores the sheet's `StunGauge` (`100`) as an i16 at `+0x16`, after `max_mp` as in the 2016 `_stunGauge`. The fields from there to `unknown_5a` sit 2 bytes further on; the longer `unknown_5e` and shorter `unknown_7e` (Layout 1) put `max_varied_speed` to `unknown_7e` 0xE bytes and `stats` and `unknown_aa` 0xA bytes further on. Client 3473 has no such field: `+0x16` starts the zero bytes before `unknown_2a`.

`level` is an i32, the 2016 `_level`; its high half (`+0x04`, earlier `unknown_04`) is 0 on every record.

## Open Questions

### The Constant Fields

`unknown_2a`, `unknown_5a` and `unknown_7a` are `experience.bss` constant fields with no sheet match. `unknown_5a` (`1.0` on every record) sits where the 2016 member order has `_productionHit`, but the `ProductionHit` columns of both private servers hold `0` on every row, and client 1784 stores `1.0` there too, so the value does not come from that column. `unknown_2a` and `unknown_7a` are `1.0` on level 0 and `0` otherwise; no sheet column has that pattern.
