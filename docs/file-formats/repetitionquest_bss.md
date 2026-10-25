# `repetitionquest.bss` Format

## Purpose

Defines the repeatable-quest list: daily, weekly and contribution quests grouped under names such as `[Contribution] [Lv. 35] Calpheon City` or `[Throne of Edana] [Weekly] For the Throne`, each group named by LOC type 42, with a condition line per quest. 48 groups and 806 quest references on client 3458. All text sits in a string table at the end of the file (Korean group names, Korean condition lines, scripts).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes   | Records                           | Row bytes |
| ------ | -------------- | --------------------- | ------- | --------------------------------- | --------- |
| 1      | 1304 and later | `repetitionquest.bss` | 200,069 | 806 Quest Reference Row, 48 Group | 17        |

| Layout | File                  | Known             | Unknown      |
| ------ | --------------------- | ----------------- | ------------ |
| 1      | `repetitionquest.bss` | 199,877 B (99.9%) | 192 B (0.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `9b0493b43e56`  |
| 3482   | Layout 1             | `9b0493b43e56`  |
| 3474   | Layout 1             | `9b0493b43e56`  |
| 3473   | Layout 1             | `9b0493b43e56`  |
| 3464   | Layout 1             | `9b0493b43e56`  |
| 3458   | Layout 1             | `9b0493b43e56`  |
| 3454   | Layout 1             | `9b0493b43e56`  |
| 3444   | Layout 1             | `9b0493b43e56`  |
| 3435   | Layout 1             | `9b0493b43e56`  |
| 3426   | Layout 1             | `9b0493b43e56`  |
| 3418   | Layout 1             | `9b0493b43e56`  |
| 3412   | Layout 1             | `9b0493b43e56`  |
| 3402   | Layout 1             | `9b0493b43e56`  |
| 3396   | Layout 1             | `9b0493b43e56`  |
| 3387   | Layout 1             | `9b0493b43e56`  |
| 3381   | Layout 1             | `9b0493b43e56`  |
| 3373   | Layout 1             | `9b0493b43e56`  |
| 3364   | Layout 1             | `9b0493b43e56`  |
| 3356   | Layout 1             | `9b0493b43e56`  |
| 3349   | Layout 1             | `9b0493b43e56`  |
| 3342   | Layout 1             | `9b0493b43e56`  |
| 3335   | Layout 1             | `9b0493b43e56`  |
| 3326   | Layout 1             | `9b0493b43e56`  |
| 3321   | Layout 1             | `9b0493b43e56`  |
| 3314   | Layout 1             | `9b0493b43e56`  |
| 3303   | Layout 1             | `9b0493b43e56`  |
| 3302   | Layout 1             | `9b0493b43e56`  |
| 3293   | Layout 1             | `9b0493b43e56`  |
| 3283   | Layout 1             | `9b0493b43e56`  |
| 3275   | Layout 1             | `9b0493b43e56`  |
| 3267   | Layout 1             | `9b0493b43e56`  |
| 3258   | Layout 1             | `9b0493b43e56`  |
| 3251   | Layout 1             | `9b0493b43e56`  |
| 3242   | Layout 1             | `9b0493b43e56`  |
| 3235   | Layout 1             | `9b0493b43e56`  |
| 3229   | Layout 1             | `9b0493b43e56`  |
| 3212   | Layout 1             | `9b0493b43e56`  |
| 3203   | Layout 1             | `9b0493b43e56`  |
| 3193   | Layout 1             | `9b0493b43e56`  |
| 3186   | Layout 1             | `9b0493b43e56`  |
| 3177   | Layout 1             | `9b0493b43e56`  |
| 3169   | Layout 1             | `9b0493b43e56`  |
| 3158   | Layout 1             | `9b0493b43e56`  |
| 3151   | Layout 1             | `9b0493b43e56`  |
| 3144   | Layout 1             | `9b0493b43e56`  |
| 3133   | Layout 1             | `9b0493b43e56`  |
| 3125   | Layout 1             | `9b0493b43e56`  |
| 3118   | Layout 1             | `9b0493b43e56`  |
| 3111   | Layout 1             | `9b0493b43e56`  |
| 3103   | Layout 1             | `9b0493b43e56`  |
| 3095   | Layout 1             | `9b0493b43e56`  |
| 3086   | Layout 1             | `9b0493b43e56`  |
| 3072   | Layout 1             | `9b0493b43e56`  |
| 3062   | Layout 1             | `9b0493b43e56`  |
| 3052   | Layout 1             | `9b0493b43e56`  |
| 3045   | Layout 1             | `9b0493b43e56`  |
| 3037   | Layout 1             | `9b0493b43e56`  |
| 3030   | Layout 1             | `9b0493b43e56`  |
| 3021   | Layout 1             | `9b0493b43e56`  |
| 3012   | Layout 1             | `9b0493b43e56`  |
| 3002   | Layout 1             | `9b0493b43e56`  |
| 2995   | Layout 1             | `9b0493b43e56`  |
| 2987   | Layout 1             | `9b0493b43e56`  |
| 2978   | Layout 1             | `9b0493b43e56`  |
| 2970   | Layout 1             | `9b0493b43e56`  |
| 2959   | Layout 1             | `9b0493b43e56`  |
| 2951   | Layout 1             | `9b0493b43e56`  |
| 2942   | Layout 1             | `9b0493b43e56`  |
| 2935   | Layout 1             | `9b0493b43e56`  |
| 2932   | Layout 1             | `9b0493b43e56`  |
| 2923   | Layout 1             | `9b0493b43e56`  |
| 2919   | Layout 1             | `9b0493b43e56`  |
| 2907   | Layout 1             | `9b0493b43e56`  |
| 2900   | Layout 1             | `9b0493b43e56`  |
| 2891   | Layout 1             | `9b0493b43e56`  |
| 2882   | Layout 1             | `9b0493b43e56`  |
| 2872   | Layout 1             | `9b0493b43e56`  |
| 2863   | Layout 1             | `9b0493b43e56`  |
| 2855   | Layout 1             | `9b0493b43e56`  |
| 2849   | Layout 1             | `9b0493b43e56`  |
| 2844   | Layout 1             | `9b0493b43e56`  |
| 2834   | Layout 1             | `9b0493b43e56`  |
| 2825   | Layout 1             | `9b0493b43e56`  |
| 2819   | Layout 1             | `9b0493b43e56`  |
| 2811   | Layout 1             | `9b0493b43e56`  |
| 2803   | Layout 1             | `9b0493b43e56`  |
| 2794   | Layout 1             | `9b0493b43e56`  |
| 2783   | Layout 1             | `9b0493b43e56`  |
| 2774   | Layout 1             | `9b0493b43e56`  |
| 2765   | Layout 1             | `9b0493b43e56`  |
| 2756   | Layout 1             | `9b0493b43e56`  |
| 2750   | Layout 1             | `9b0493b43e56`  |
| 2743   | Layout 1             | `9b0493b43e56`  |
| 2736   | Layout 1             | `9b0493b43e56`  |
| 2726   | Layout 1             | `9b0493b43e56`  |
| 2717   | Layout 1             | `9b0493b43e56`  |
| 2709   | Layout 1             | `9b0493b43e56`  |
| 2703   | Layout 1             | `9b0493b43e56`  |
| 2695   | Layout 1             | `9b0493b43e56`  |
| 2684   | Layout 1             | `9b0493b43e56`  |
| 2672   | Layout 1             | `9b0493b43e56`  |
| 2665   | Layout 1             | `9b0493b43e56`  |
| 2657   | Layout 1             | `9b0493b43e56`  |
| 2649   | Layout 1             | `9b0493b43e56`  |
| 2644   | Layout 1             | `9b0493b43e56`  |
| 2637   | Layout 1             | `9b0493b43e56`  |
| 2629   | Layout 1             | `9b0493b43e56`  |
| 2619   | Layout 1             | `9b0493b43e56`  |
| 2612   | Layout 1             | `9b0493b43e56`  |
| 2606   | Layout 1             | `9b0493b43e56`  |
| 2602   | Layout 1             | `9b0493b43e56`  |
| 2601   | Layout 1             | `9b0493b43e56`  |
| 2592   | Layout 1             | `9b0493b43e56`  |
| 2583   | Layout 1             | `9b0493b43e56`  |
| 2575   | Layout 1             | `9b0493b43e56`  |
| 2567   | Layout 1             | `9b0493b43e56`  |
| 2560   | Layout 1             | `9b0493b43e56`  |
| 2553   | Layout 1             | `9b0493b43e56`  |
| 2545   | Layout 1             | `9b0493b43e56`  |
| 2538   | Layout 1             | `9b0493b43e56`  |
| 2529   | Layout 1             | `9b0493b43e56`  |
| 2519   | Layout 1             | `9b0493b43e56`  |
| 2513   | Layout 1             | `9b0493b43e56`  |
| 2510   | Layout 1             | `9b0493b43e56`  |
| 2507   | Layout 1             | `9b0493b43e56`  |
| 2503   | Layout 1             | `9b0493b43e56`  |
| 2498   | Layout 1             | `9b0493b43e56`  |
| 2492   | Layout 1             | `9b0493b43e56`  |
| 2487   | Layout 1             | `9b0493b43e56`  |
| 2480   | Layout 1             | `9b0493b43e56`  |
| 2474   | Layout 1             | `9b0493b43e56`  |
| 2468   | Layout 1             | `9b0493b43e56`  |
| 2460   | Layout 1             | `9b0493b43e56`  |
| 2453   | Layout 1             | `9b0493b43e56`  |
| 2444   | Layout 1             | `9b0493b43e56`  |
| 2438   | Layout 1             | `9b0493b43e56`  |
| 2434   | Layout 1             | `9b0493b43e56`  |
| 2429   | Layout 1             | `9b0493b43e56`  |
| 2421   | Layout 1             | `9b0493b43e56`  |
| 2414   | Layout 1             | `9b0493b43e56`  |
| 2407   | Layout 1             | `9b0493b43e56`  |
| 2401   | Layout 1             | `9b0493b43e56`  |
| 2397   | Layout 1             | `9b0493b43e56`  |
| 2393   | Layout 1             | `9b0493b43e56`  |
| 2384   | Layout 1             | `9b0493b43e56`  |
| 2378   | Layout 1             | `9b0493b43e56`  |
| 2372   | Layout 1             | `9b0493b43e56`  |
| 2358   | Layout 1             | `9b0493b43e56`  |
| 2352   | Layout 1             | `9b0493b43e56`  |
| 2347   | Layout 1             | `9b0493b43e56`  |
| 2343   | Layout 1             | `9b0493b43e56`  |
| 2335   | Layout 1             | `9b0493b43e56`  |
| 2327   | Layout 1             | `9b0493b43e56`  |
| 2324   | Layout 1             | `9b0493b43e56`  |
| 2319   | Layout 1             | `9b0493b43e56`  |
| 2313   | Layout 1             | `9b0493b43e56`  |
| 2308   | Layout 1             | `9b0493b43e56`  |
| 2302   | Layout 1             | `9b0493b43e56`  |
| 2295   | Layout 1             | `9b0493b43e56`  |
| 2290   | Layout 1             | `9b0493b43e56`  |
| 2284   | Layout 1             | `9b0493b43e56`  |
| 2276   | Layout 1             | `9b0493b43e56`  |
| 2269   | Layout 1             | `9b0493b43e56`  |
| 2259   | Layout 1             | `9b0493b43e56`  |
| 2250   | Layout 1             | `9b0493b43e56`  |
| 2243   | Layout 1             | `9b0493b43e56`  |
| 2235   | Layout 1             | `9b0493b43e56`  |
| 2229   | Layout 1             | `9b0493b43e56`  |
| 2224   | Layout 1             | `9b0493b43e56`  |
| 2218   | Layout 1             | `9b0493b43e56`  |
| 2215   | Layout 1             | `9b0493b43e56`  |
| 2207   | Layout 1             | `9b0493b43e56`  |
| 2203   | Layout 1             | `9b0493b43e56`  |
| 2196   | Layout 1             | `9b0493b43e56`  |
| 2192   | Layout 1             | `9b0493b43e56`  |
| 2189   | Layout 1             | `9b0493b43e56`  |
| 2183   | Layout 1             | `9b0493b43e56`  |
| 2179   | Layout 1             | `9b0493b43e56`  |
| 2171   | Layout 1             | `9b0493b43e56`  |
| 2163   | Layout 1             | `9b0493b43e56`  |
| 2156   | Layout 1             | `9b0493b43e56`  |
| 2151   | Layout 1             | `9b0493b43e56`  |
| 2147   | Layout 1             | `9b0493b43e56`  |
| 2142   | Layout 1             | `9b0493b43e56`  |
| 2138   | Layout 1             | `9b0493b43e56`  |
| 2134   | Layout 1             | `9b0493b43e56`  |
| 2130   | Layout 1             | `9b0493b43e56`  |
| 2122   | Layout 1             | `9b0493b43e56`  |
| 2107   | Layout 1             | `9b0493b43e56`  |
| 2098   | Layout 1             | `9b0493b43e56`  |
| 2089   | Layout 1             | `9b0493b43e56`  |
| 2081   | Layout 1             | `9b0493b43e56`  |
| 2073   | Layout 1             | `9b0493b43e56`  |
| 2067   | Layout 1             | `9b0493b43e56`  |
| 2063   | Layout 1             | `9b0493b43e56`  |
| 2059   | Layout 1             | `9b0493b43e56`  |
| 2052   | Layout 1             | `9b0493b43e56`  |
| 2044   | Layout 1             | `9b0493b43e56`  |
| 2039   | Layout 1             | `9b0493b43e56`  |
| 2032   | Layout 1             | `9b0493b43e56`  |
| 2025   | Layout 1             | `9b0493b43e56`  |
| 2011   | Layout 1             | `9b0493b43e56`  |
| 2005   | Layout 1             | `9b0493b43e56`  |
| 2000   | Layout 1             | `9b0493b43e56`  |
| 1996   | Layout 1             | `9b0493b43e56`  |
| 1991   | Layout 1             | `9b0493b43e56`  |
| 1985   | Layout 1             | `9b0493b43e56`  |
| 1980   | Layout 1             | `9b0493b43e56`  |
| 1969   | Layout 1             | `9b0493b43e56`  |
| 1964   | Layout 1             | `9b0493b43e56`  |
| 1958   | Layout 1             | `9b0493b43e56`  |
| 1950   | Layout 1             | `9b0493b43e56`  |
| 1945   | Layout 1             | `9b0493b43e56`  |
| 1937   | Layout 1             | `9b0493b43e56`  |
| 1933   | Layout 1             | `9b0493b43e56`  |
| 1927   | Layout 1             | `9b0493b43e56`  |
| 1921   | Layout 1             | `9b0493b43e56`  |
| 1914   | Layout 1             | `9b0493b43e56`  |
| 1908   | Layout 1             | `9b0493b43e56`  |
| 1897   | Layout 1             | `9b0493b43e56`  |
| 1892   | Layout 1             | `9b0493b43e56`  |
| 1886   | Layout 1             | `9b0493b43e56`  |
| 1881   | Layout 1             | `9b0493b43e56`  |
| 1871   | Layout 1             | `9b0493b43e56`  |
| 1866   | Layout 1             | `9b0493b43e56`  |
| 1862   | Layout 1             | `9b0493b43e56`  |
| 1854   | Layout 1             | `9b0493b43e56`  |
| 1846   | Layout 1             | `9b0493b43e56`  |
| 1838   | Layout 1             | `9b0493b43e56`  |
| 1832   | Layout 1             | `9b0493b43e56`  |
| 1826   | Layout 1             | `9b0493b43e56`  |
| 1822   | Layout 1             | `9b0493b43e56`  |
| 1818   | Layout 1             | `9b0493b43e56`  |
| 1804   | Layout 1             | `9b0493b43e56`  |
| 1794   | Layout 1             | `9b0493b43e56`  |
| 1790   | Layout 1             | `9b0493b43e56`  |
| 1784   | Layout 1             | `9b0493b43e56`  |
| 1774   | Layout 1             | `9b0493b43e56`  |
| 1771   | Layout 1             | `9b0493b43e56`  |
| 1762   | Layout 1             | `9b0493b43e56`  |
| 1759   | Layout 1             | `9b0493b43e56`  |
| 1754   | Layout 1             | `9b0493b43e56`  |
| 1749   | Layout 1             | `9b0493b43e56`  |
| 1743   | Layout 1             | `9b0493b43e56`  |
| 1737   | Layout 1             | `9b0493b43e56`  |
| 1731   | Layout 1             | `9b0493b43e56`  |
| 1725   | Layout 1             | `9b0493b43e56`  |
| 1717   | Layout 1             | `9b0493b43e56`  |
| 1710   | Layout 1             | `9b0493b43e56`  |
| 1704   | Layout 1             | `9b0493b43e56`  |
| 1698   | Layout 1             | `9b0493b43e56`  |
| 1690   | Layout 1             | `9b0493b43e56`  |
| 1685   | Layout 1             | `9b0493b43e56`  |
| 1680   | Layout 1             | `9b0493b43e56`  |
| 1674   | Layout 1             | `9b0493b43e56`  |
| 1668   | Layout 1             | `9b0493b43e56`  |
| 1659   | Layout 1             | `9b0493b43e56`  |
| 1649   | Layout 1             | `9b0493b43e56`  |
| 1642   | Layout 1             | `9b0493b43e56`  |
| 1636   | Layout 1             | `9b0493b43e56`  |
| 1628   | Layout 1             | `9b0493b43e56`  |
| 1622   | Layout 1             | `9b0493b43e56`  |
| 1614   | Layout 1             | `9b0493b43e56`  |
| 1608   | Layout 1             | `9b0493b43e56`  |
| 1602   | Layout 1             | `9b0493b43e56`  |
| 1598   | Layout 1             | `9b0493b43e56`  |
| 1594   | Layout 1             | `9b0493b43e56`  |
| 1590   | Layout 1             | `9b0493b43e56`  |
| 1587   | Layout 1             | `9b0493b43e56`  |
| 1584   | Layout 1             | `9b0493b43e56`  |
| 1579   | Layout 1             | `9b0493b43e56`  |
| 1572   | Layout 1             | `9b0493b43e56`  |
| 1565   | Layout 1             | `9b0493b43e56`  |
| 1559   | Layout 1             | `9b0493b43e56`  |
| 1554   | Layout 1             | `9b0493b43e56`  |
| 1547   | Layout 1             | `9b0493b43e56`  |
| 1537   | Layout 1             | `9b0493b43e56`  |
| 1529   | Layout 1             | `9b0493b43e56`  |
| 1524   | Layout 1             | `9b0493b43e56`  |
| 1519   | Layout 1             | `9b0493b43e56`  |
| 1509   | Layout 1             | `9b0493b43e56`  |
| 1506   | Layout 1             | `9b0493b43e56`  |
| 1504   | Layout 1             | `9b0493b43e56`  |
| 1500   | Layout 1             | `9b0493b43e56`  |
| 1493   | Layout 1             | `9b0493b43e56`  |
| 1489   | Layout 1             | `9b0493b43e56`  |
| 1485   | Layout 1             | `9b0493b43e56`  |
| 1481   | Layout 1             | `9b0493b43e56`  |
| 1474   | Layout 1             | `9b0493b43e56`  |
| 1466   | Layout 1             | `9b0493b43e56`  |
| 1462   | Layout 1             | `9b0493b43e56`  |
| 1459   | Layout 1             | `9b0493b43e56`  |
| 1453   | Layout 1             | `9b0493b43e56`  |
| 1450   | Layout 1             | `9b0493b43e56`  |
| 1445   | Layout 1             | `9b0493b43e56`  |
| 1439   | Layout 1             | `9b0493b43e56`  |
| 1433   | Layout 1             | `9b0493b43e56`  |
| 1430   | Layout 1             | `9b0493b43e56`  |
| 1426   | Layout 1             | `9b0493b43e56`  |
| 1421   | Layout 1             | `9b0493b43e56`  |
| 1417   | Layout 1             | `9b0493b43e56`  |
| 1416   | Layout 1             | `9b0493b43e56`  |
| 1409   | Layout 1             | `9b0493b43e56`  |
| 1405   | Layout 1             | `9b0493b43e56`  |
| 1401   | Layout 1             | `9b0493b43e56`  |
| 1396   | Layout 1             | `9b0493b43e56`  |
| 1391   | Layout 1             | `9b0493b43e56`  |
| 1390   | Layout 1             | `9b0493b43e56`  |
| 1386   | Layout 1             | `9b0493b43e56`  |
| 1381   | Layout 1             | `9b0493b43e56`  |
| 1379   | Layout 1             | `9b0493b43e56`  |
| 1372   | Layout 1             | `9b0493b43e56`  |
| 1366   | Layout 1             | `9b0493b43e56`  |
| 1364   | Layout 1             | `9b0493b43e56`  |
| 1363   | Layout 1             | `9b0493b43e56`  |
| 1360   | Layout 1             | `9b0493b43e56`  |
| 1358   | Layout 1             | `9b0493b43e56`  |
| 1355   | Layout 1             | `9b0493b43e56`  |
| 1351   | Layout 1             | `9b0493b43e56`  |
| 1348   | Layout 1             | `9b0493b43e56`  |
| 1346   | Layout 1             | `9b0493b43e56`  |
| 1341   | Layout 1             | `9b0493b43e56`  |
| 1340   | Layout 1             | `9b0493b43e56`  |
| 1338   | Layout 1             | `9b0493b43e56`  |
| 1335   | Layout 1             | `9b0493b43e56`  |
| 1333   | Layout 1             | `9b0493b43e56`  |
| 1329   | Layout 1             | `9b0493b43e56`  |
| 1327   | Layout 1             | `9b0493b43e56`  |
| 1324   | Layout 1             | `9b0493b43e56`  |
| 1321   | Layout 1             | `9b0493b43e56`  |
| 1319   | Layout 1             | `9b0493b43e56`  |
| 1318   | Layout 1             | `9b0493b43e56`  |
| 1316   | Layout 1             | `9b0493b43e56`  |
| 1313   | Layout 1             | `9b0493b43e56`  |
| 1311   | Layout 1             | `9b0493b43e56`  |
| 1309   | Layout 1             | `9b0493b43e56`  |
| 1304   | Layout 1             | `9b0493b43e56`  |
| 1292   | No documented layout | `9b0493b43e56`  |
| 1286   | No documented layout | `9b0493b43e56`  |
| 1280   | No documented layout | `9b0493b43e56`  |
| 1276   | No documented layout | `9b0493b43e56`  |
| 1267   | No documented layout | `9b0493b43e56`  |
| 1261   | No documented layout | `9b0493b43e56`  |
| 1256   | No documented layout | `9b0493b43e56`  |
| 1250   | No documented layout | `9b0493b43e56`  |
| 1246   | No file              | `9b0493b43e56`  |
| 1239   | No file              | `9b0493b43e56`  |
| 1230   | No file              | `9b0493b43e56`  |
| 1226   | No file              | `9b0493b43e56`  |
| 1220   | No file              | `9b0493b43e56`  |
| 1217   | No file              | `9b0493b43e56`  |
| 1211   | No file              | `9b0493b43e56`  |
| 1210   | No file              | `9b0493b43e56`  |
| 1208   | No file              | `9b0493b43e56`  |
| 1203   | No file              | `9b0493b43e56`  |
| 1197   | No file              | `9b0493b43e56`  |
| 1194   | No file              | `9b0493b43e56`  |
| 1192   | No file              | `9b0493b43e56`  |
| 1187   | No file              | `9b0493b43e56`  |
| 1183   | No file              | `9b0493b43e56`  |
| 1177   | No file              | `9b0493b43e56`  |
| 1173   | No file              | `9b0493b43e56`  |
| 1167   | No file              | `9b0493b43e56`  |
| 1164   | No file              | `9b0493b43e56`  |
| 1156   | No file              | `9b0493b43e56`  |
| 1149   | No file              | `9b0493b43e56`  |
| 1144   | No documented layout | `9b0493b43e56`  |
| 1137   | No documented layout | `9b0493b43e56`  |
| 1132   | No documented layout | `9b0493b43e56`  |
| 1127   | No documented layout | `9b0493b43e56`  |
| 1122   | No documented layout | `9b0493b43e56`  |
| 1118   | No documented layout | `9b0493b43e56`  |
| 1114   | No documented layout | `9b0493b43e56`  |
| 1109   | No documented layout | `9b0493b43e56`  |
| 1102   | No file              | `9b0493b43e56`  |
| 1096   | No file              | `9b0493b43e56`  |
| 1088   | No file              | `9b0493b43e56`  |
| 1081   | No file              | `9b0493b43e56`  |
| 1076   | No file              | `9b0493b43e56`  |
| 1069   | No file              | `9b0493b43e56`  |
| 1064   | No file              | `9b0493b43e56`  |
| 1058   | No file              | `9b0493b43e56`  |
| 1051   | No file              | `9b0493b43e56`  |
| 1044   | No file              | `9b0493b43e56`  |
| 1036   | No file              | `9b0493b43e56`  |
| 1026   | No file              | `9b0493b43e56`  |
| 1016   | No file              | `9b0493b43e56`  |
| 1009   | No file              | `9b0493b43e56`  |
| 1005   | No file              | `9b0493b43e56`  |
| 1000   | No file              | `9b0493b43e56`  |
| 998    | No file              | `9b0493b43e56`  |
| 990    | No file              | `9b0493b43e56`  |
| 979    | No file              | `9b0493b43e56`  |
| 972    | No file              | `9b0493b43e56`  |
| 963    | No file              | `9b0493b43e56`  |
| 955    | No file              | `9b0493b43e56`  |
| 946    | No file              | `9b0493b43e56`  |
| 938    | No file              | `9b0493b43e56`  |
| 927    | No file              | `9b0493b43e56`  |
| 911    | No file              | `9b0493b43e56`  |
| 904    | No file              | `9b0493b43e56`  |
| 899    | No file              | `9b0493b43e56`  |
| 894    | No file              | `9b0493b43e56`  |
| 885    | No file              | `9b0493b43e56`  |
| 879    | No file              | `9b0493b43e56`  |
| 872    | No file              | `9b0493b43e56`  |
| 864    | No file              | `9b0493b43e56`  |
| 855    | No file              | `9b0493b43e56`  |
| 853    | No file              | `9b0493b43e56`  |
| 845    | No file              | `9b0493b43e56`  |
| 837    | No file              | `9b0493b43e56`  |
| 829    | No documented layout | `9b0493b43e56`  |
| 822    | No documented layout | `9b0493b43e56`  |
| 814    | No documented layout | `9b0493b43e56`  |
| 805    | No documented layout | `9b0493b43e56`  |
| 794    | No documented layout | `9b0493b43e56`  |
| 787    | No documented layout | `9b0493b43e56`  |
| 780    | No documented layout | `9b0493b43e56`  |
| 771    | No documented layout | `9b0493b43e56`  |
| 760    | No documented layout | `9b0493b43e56`  |
| 748    | No documented layout | `9b0493b43e56`  |
| 741    | No documented layout | `9b0493b43e56`  |
| 736    | No documented layout | `9b0493b43e56`  |
| 731    | No documented layout | `9b0493b43e56`  |
| 723    | No documented layout | `9b0493b43e56`  |
| 711    | No documented layout | `9b0493b43e56`  |
| 707    | No documented layout | `9b0493b43e56`  |
| 697    | No documented layout | `9b0493b43e56`  |
| 689    | No documented layout | `9b0493b43e56`  |
| 683    | No documented layout | `9b0493b43e56`  |
| 678    | No documented layout | `9b0493b43e56`  |
| 670    | No documented layout | `9b0493b43e56`  |
| 661    | No documented layout | `9b0493b43e56`  |
| 656    | No documented layout | `9b0493b43e56`  |
| 652    | No documented layout | `9b0493b43e56`  |
| 643    | No documented layout | `9b0493b43e56`  |
| 637    | No documented layout | `9b0493b43e56`  |
| 630    | No documented layout | `9b0493b43e56`  |
| 627    | No documented layout | `9b0493b43e56`  |
| 621    | No documented layout | `9b0493b43e56`  |
| 617    | No documented layout | `9b0493b43e56`  |
| 615    | No documented layout | `9b0493b43e56`  |
| 606    | No documented layout | `9b0493b43e56`  |
| 599    | No documented layout | `9b0493b43e56`  |
| 592    | No documented layout | `9b0493b43e56`  |
| 586    | No documented layout | `9b0493b43e56`  |
| 577    | No documented layout | `9b0493b43e56`  |
| 569    | No documented layout | `9b0493b43e56`  |
| 561    | No documented layout | `9b0493b43e56`  |
| 554    | No documented layout | `9b0493b43e56`  |
| 542    | No documented layout | `9b0493b43e56`  |
| 532    | No documented layout | `9b0493b43e56`  |
| 531    | No documented layout | `9b0493b43e56`  |
| 526    | No documented layout | `9b0493b43e56`  |
| 521    | No documented layout | `9b0493b43e56`  |
| 517    | No documented layout | `9b0493b43e56`  |
| 510    | No documented layout | `9b0493b43e56`  |
| 508    | No documented layout | `9b0493b43e56`  |
| 504    | No documented layout | `9b0493b43e56`  |
| 497    | No documented layout | `9b0493b43e56`  |
| 491    | No documented layout | `9b0493b43e56`  |
| 485    | No documented layout | `9b0493b43e56`  |
| 478    | No documented layout | `9b0493b43e56`  |
| 472    | No documented layout | `9b0493b43e56`  |
| 466    | No documented layout | `9b0493b43e56`  |
| 457    | No documented layout | `9b0493b43e56`  |
| 452    | No documented layout | `9b0493b43e56`  |
| 449    | No documented layout | `9b0493b43e56`  |
| 435    | No documented layout | `9b0493b43e56`  |

<!-- versions:end -->

## Observed Values

Same layout as [`newquest.bss`](newquest_bss.md), the layout reference: an 8-byte `PABR` header with a group count; per group an 11-byte header, 17-byte quest reference rows and a 12-byte trailer; a string table; an 8-byte file trailer. One handler reads all four quest lists. Values seen on client 3458:

| Field                                  | Observed                                              |
| -------------------------------------- | ----------------------------------------------------- |
| `group_count`                          | `48`                                                  |
| First group                            | key `51`, `10` rows                                   |
| Group header `group_type`              | `0` on every group                                    |
| Group trailer start / end index        | Index `31`, the empty string: no event period         |
| Row `is_sub_quest`                       | `0` on every row                                      |
| Row `hide_conditions_index`                   | Empty string on 678 rows, a script on 128             |
| Row `visible_conditions_index`                   | Empty string on 517 rows, a script on 289             |
| String table                           | `633` strings; `string_count` at `0x000039DE`         |

The empty string sits at index `31` here, so the script fields read `31` on most rows. The scripts check other quests of a weekly set (`clearquest(9108,2);<or>clearquest(9108,3);...`), life skill levels (`getLifeLevel(6)>80;`), content groups and random rolls (`checkRandom`); see String Table in the `newquest.bss` doc for the two script roles.

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

## Localization

LOC type `42` holds the English text of this list, keyed by the group's `group_key`:

| Key                                                               | Text                                                 |
| ----------------------------------------------------------------- | ---------------------------------------------------- |
| `str_id1 = group_key`, `str_id4 = 0`                              | Group name, e.g. key 51 `[Throne of Edana] [Weekly] For the Throne` |
| `str_id1 = packed_quest_id`, `str_id2 = group_key`, `str_id4 = 1` | The quest's condition line, e.g. `<PAColor0xfff3d900>from 350 AP & 427 DP <PAOldColor>via the <PAColor0xfff3d900>Throne of Aetherion<PAOldColor> ...` |

On client 3458 all 48 groups have a name (type 42 has 54, keys 1 to 54, so some belong to groups no longer in the file) and all 806 rows have a condition line. Condition lines carry `<PAColor>` tags (all but 1); group names do not. The string table holds the Korean source of both, which the handler shows where LOC has no row.

## Notes

- Decompressed size is `200,069` bytes on client 3458.
- One quest sits in two groups, with a condition line under each key: quest 4500 / 131 is in key 3 (`[Contribution] [Lv. 52] Mediah`) and key 45 (`Monster Zone Info`).

## Open Questions

### Shared Fields

What `group_type` selects is open for all four lists; see the Open Questions of [`newquest.bss`](newquest_bss.md).
