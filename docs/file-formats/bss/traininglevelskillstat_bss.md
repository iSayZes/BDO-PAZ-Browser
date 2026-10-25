# `traininglevelskillstat.bss` Format

## Purpose

Two Training bonuses per Training level, from level 1 (Beginner 1) to 180
(Guru 100): the chance for a mount to learn a skill when it gains a level,
and the chance for a higher minimum movement speed gain on a mount level up.
The Training tooltip in the Character Info Basic tab shows both.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                         | Bytes | Records         | Row bytes |
| ------ | ------------- | ---------------------------- | ----- | --------------- | --------- |
| 1      | 946 and later | `traininglevelskillstat.bss` | 1,456 | 180 Level Entry | 8         |

| Layout | File                         | Known            | Unknown    |
| ------ | ---------------------------- | ---------------- | ---------- |
| 1      | `traininglevelskillstat.bss` | 1,456 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `8393d4bcd55a`  |
| 3482   | Layout 1 | `8393d4bcd55a`  |
| 3474   | Layout 1 | `8393d4bcd55a`  |
| 3473   | Layout 1 | `8393d4bcd55a`  |
| 3464   | Layout 1 | `8393d4bcd55a`  |
| 3458   | Layout 1 | `8393d4bcd55a`  |
| 3454   | Layout 1 | `8393d4bcd55a`  |
| 3444   | Layout 1 | `8393d4bcd55a`  |
| 3435   | Layout 1 | `8393d4bcd55a`  |
| 3426   | Layout 1 | `8393d4bcd55a`  |
| 3418   | Layout 1 | `8393d4bcd55a`  |
| 3412   | Layout 1 | `8393d4bcd55a`  |
| 3402   | Layout 1 | `8393d4bcd55a`  |
| 3396   | Layout 1 | `8393d4bcd55a`  |
| 3387   | Layout 1 | `8393d4bcd55a`  |
| 3381   | Layout 1 | `8393d4bcd55a`  |
| 3373   | Layout 1 | `8393d4bcd55a`  |
| 3364   | Layout 1 | `8393d4bcd55a`  |
| 3356   | Layout 1 | `8393d4bcd55a`  |
| 3349   | Layout 1 | `8393d4bcd55a`  |
| 3342   | Layout 1 | `8393d4bcd55a`  |
| 3335   | Layout 1 | `8393d4bcd55a`  |
| 3326   | Layout 1 | `8393d4bcd55a`  |
| 3321   | Layout 1 | `8393d4bcd55a`  |
| 3314   | Layout 1 | `8393d4bcd55a`  |
| 3303   | Layout 1 | `8393d4bcd55a`  |
| 3302   | Layout 1 | `8393d4bcd55a`  |
| 3293   | Layout 1 | `8393d4bcd55a`  |
| 3283   | Layout 1 | `8393d4bcd55a`  |
| 3275   | Layout 1 | `8393d4bcd55a`  |
| 3267   | Layout 1 | `8393d4bcd55a`  |
| 3258   | Layout 1 | `8393d4bcd55a`  |
| 3251   | Layout 1 | `8393d4bcd55a`  |
| 3242   | Layout 1 | `8393d4bcd55a`  |
| 3235   | Layout 1 | `8393d4bcd55a`  |
| 3229   | Layout 1 | `8393d4bcd55a`  |
| 3212   | Layout 1 | `8393d4bcd55a`  |
| 3203   | Layout 1 | `8393d4bcd55a`  |
| 3193   | Layout 1 | `8393d4bcd55a`  |
| 3186   | Layout 1 | `8393d4bcd55a`  |
| 3177   | Layout 1 | `8393d4bcd55a`  |
| 3169   | Layout 1 | `8393d4bcd55a`  |
| 3158   | Layout 1 | `8393d4bcd55a`  |
| 3151   | Layout 1 | `8393d4bcd55a`  |
| 3144   | Layout 1 | `8393d4bcd55a`  |
| 3133   | Layout 1 | `8393d4bcd55a`  |
| 3125   | Layout 1 | `8393d4bcd55a`  |
| 3118   | Layout 1 | `8393d4bcd55a`  |
| 3111   | Layout 1 | `8393d4bcd55a`  |
| 3103   | Layout 1 | `8393d4bcd55a`  |
| 3095   | Layout 1 | `8393d4bcd55a`  |
| 3086   | Layout 1 | `8393d4bcd55a`  |
| 3072   | Layout 1 | `8393d4bcd55a`  |
| 3062   | Layout 1 | `8393d4bcd55a`  |
| 3052   | Layout 1 | `8393d4bcd55a`  |
| 3045   | Layout 1 | `8393d4bcd55a`  |
| 3037   | Layout 1 | `8393d4bcd55a`  |
| 3030   | Layout 1 | `8393d4bcd55a`  |
| 3021   | Layout 1 | `8393d4bcd55a`  |
| 3012   | Layout 1 | `8393d4bcd55a`  |
| 3002   | Layout 1 | `8393d4bcd55a`  |
| 2995   | Layout 1 | `8393d4bcd55a`  |
| 2987   | Layout 1 | `8393d4bcd55a`  |
| 2978   | Layout 1 | `8393d4bcd55a`  |
| 2970   | Layout 1 | `8393d4bcd55a`  |
| 2959   | Layout 1 | `8393d4bcd55a`  |
| 2951   | Layout 1 | `8393d4bcd55a`  |
| 2942   | Layout 1 | `8393d4bcd55a`  |
| 2935   | Layout 1 | `8393d4bcd55a`  |
| 2932   | Layout 1 | `8393d4bcd55a`  |
| 2923   | Layout 1 | `8393d4bcd55a`  |
| 2919   | Layout 1 | `8393d4bcd55a`  |
| 2907   | Layout 1 | `8393d4bcd55a`  |
| 2900   | Layout 1 | `8393d4bcd55a`  |
| 2891   | Layout 1 | `8393d4bcd55a`  |
| 2882   | Layout 1 | `8393d4bcd55a`  |
| 2872   | Layout 1 | `8393d4bcd55a`  |
| 2863   | Layout 1 | `8393d4bcd55a`  |
| 2855   | Layout 1 | `8393d4bcd55a`  |
| 2849   | Layout 1 | `8393d4bcd55a`  |
| 2844   | Layout 1 | `8393d4bcd55a`  |
| 2834   | Layout 1 | `8393d4bcd55a`  |
| 2825   | Layout 1 | `8393d4bcd55a`  |
| 2819   | Layout 1 | `8393d4bcd55a`  |
| 2811   | Layout 1 | `8393d4bcd55a`  |
| 2803   | Layout 1 | `8393d4bcd55a`  |
| 2794   | Layout 1 | `8393d4bcd55a`  |
| 2783   | Layout 1 | `8393d4bcd55a`  |
| 2774   | Layout 1 | `8393d4bcd55a`  |
| 2765   | Layout 1 | `8393d4bcd55a`  |
| 2756   | Layout 1 | `8393d4bcd55a`  |
| 2750   | Layout 1 | `8393d4bcd55a`  |
| 2743   | Layout 1 | `8393d4bcd55a`  |
| 2736   | Layout 1 | `8393d4bcd55a`  |
| 2726   | Layout 1 | `8393d4bcd55a`  |
| 2717   | Layout 1 | `8393d4bcd55a`  |
| 2709   | Layout 1 | `8393d4bcd55a`  |
| 2703   | Layout 1 | `8393d4bcd55a`  |
| 2695   | Layout 1 | `8393d4bcd55a`  |
| 2684   | Layout 1 | `8393d4bcd55a`  |
| 2672   | Layout 1 | `8393d4bcd55a`  |
| 2665   | Layout 1 | `8393d4bcd55a`  |
| 2657   | Layout 1 | `8393d4bcd55a`  |
| 2649   | Layout 1 | `8393d4bcd55a`  |
| 2644   | Layout 1 | `8393d4bcd55a`  |
| 2637   | Layout 1 | `8393d4bcd55a`  |
| 2629   | Layout 1 | `8393d4bcd55a`  |
| 2619   | Layout 1 | `8393d4bcd55a`  |
| 2612   | Layout 1 | `8393d4bcd55a`  |
| 2606   | Layout 1 | `8393d4bcd55a`  |
| 2602   | Layout 1 | `8393d4bcd55a`  |
| 2601   | Layout 1 | `8393d4bcd55a`  |
| 2592   | Layout 1 | `8393d4bcd55a`  |
| 2583   | Layout 1 | `8393d4bcd55a`  |
| 2575   | Layout 1 | `8393d4bcd55a`  |
| 2567   | Layout 1 | `8393d4bcd55a`  |
| 2560   | Layout 1 | `8393d4bcd55a`  |
| 2553   | Layout 1 | `8393d4bcd55a`  |
| 2545   | Layout 1 | `8393d4bcd55a`  |
| 2538   | Layout 1 | `8393d4bcd55a`  |
| 2529   | Layout 1 | `8393d4bcd55a`  |
| 2519   | Layout 1 | `8393d4bcd55a`  |
| 2513   | Layout 1 | `8393d4bcd55a`  |
| 2510   | Layout 1 | `8393d4bcd55a`  |
| 2507   | Layout 1 | `8393d4bcd55a`  |
| 2503   | Layout 1 | `8393d4bcd55a`  |
| 2498   | Layout 1 | `8393d4bcd55a`  |
| 2492   | Layout 1 | `8393d4bcd55a`  |
| 2487   | Layout 1 | `8393d4bcd55a`  |
| 2480   | Layout 1 | `8393d4bcd55a`  |
| 2474   | Layout 1 | `8393d4bcd55a`  |
| 2468   | Layout 1 | `8393d4bcd55a`  |
| 2460   | Layout 1 | `8393d4bcd55a`  |
| 2453   | Layout 1 | `8393d4bcd55a`  |
| 2444   | Layout 1 | `8393d4bcd55a`  |
| 2438   | Layout 1 | `8393d4bcd55a`  |
| 2434   | Layout 1 | `8393d4bcd55a`  |
| 2429   | Layout 1 | `8393d4bcd55a`  |
| 2421   | Layout 1 | `8393d4bcd55a`  |
| 2414   | Layout 1 | `8393d4bcd55a`  |
| 2407   | Layout 1 | `8393d4bcd55a`  |
| 2401   | Layout 1 | `8393d4bcd55a`  |
| 2397   | Layout 1 | `8393d4bcd55a`  |
| 2393   | Layout 1 | `8393d4bcd55a`  |
| 2384   | Layout 1 | `8393d4bcd55a`  |
| 2378   | Layout 1 | `8393d4bcd55a`  |
| 2372   | Layout 1 | `8393d4bcd55a`  |
| 2358   | Layout 1 | `8393d4bcd55a`  |
| 2352   | Layout 1 | `8393d4bcd55a`  |
| 2347   | Layout 1 | `8393d4bcd55a`  |
| 2343   | Layout 1 | `8393d4bcd55a`  |
| 2335   | Layout 1 | `8393d4bcd55a`  |
| 2327   | Layout 1 | `8393d4bcd55a`  |
| 2324   | Layout 1 | `8393d4bcd55a`  |
| 2319   | Layout 1 | `8393d4bcd55a`  |
| 2313   | Layout 1 | `8393d4bcd55a`  |
| 2308   | Layout 1 | `8393d4bcd55a`  |
| 2302   | Layout 1 | `8393d4bcd55a`  |
| 2295   | Layout 1 | `8393d4bcd55a`  |
| 2290   | Layout 1 | `8393d4bcd55a`  |
| 2284   | Layout 1 | `8393d4bcd55a`  |
| 2276   | Layout 1 | `8393d4bcd55a`  |
| 2269   | Layout 1 | `8393d4bcd55a`  |
| 2259   | Layout 1 | `8393d4bcd55a`  |
| 2250   | Layout 1 | `8393d4bcd55a`  |
| 2243   | Layout 1 | `8393d4bcd55a`  |
| 2235   | Layout 1 | `8393d4bcd55a`  |
| 2229   | Layout 1 | `8393d4bcd55a`  |
| 2224   | Layout 1 | `8393d4bcd55a`  |
| 2218   | Layout 1 | `8393d4bcd55a`  |
| 2215   | Layout 1 | `8393d4bcd55a`  |
| 2207   | Layout 1 | `8393d4bcd55a`  |
| 2203   | Layout 1 | `8393d4bcd55a`  |
| 2196   | Layout 1 | `8393d4bcd55a`  |
| 2192   | Layout 1 | `8393d4bcd55a`  |
| 2189   | Layout 1 | `8393d4bcd55a`  |
| 2183   | Layout 1 | `8393d4bcd55a`  |
| 2179   | Layout 1 | `8393d4bcd55a`  |
| 2171   | Layout 1 | `8393d4bcd55a`  |
| 2163   | Layout 1 | `8393d4bcd55a`  |
| 2156   | Layout 1 | `8393d4bcd55a`  |
| 2151   | Layout 1 | `8393d4bcd55a`  |
| 2147   | Layout 1 | `8393d4bcd55a`  |
| 2142   | Layout 1 | `8393d4bcd55a`  |
| 2138   | Layout 1 | `8393d4bcd55a`  |
| 2134   | Layout 1 | `8393d4bcd55a`  |
| 2130   | Layout 1 | `8393d4bcd55a`  |
| 2122   | Layout 1 | `8393d4bcd55a`  |
| 2107   | Layout 1 | `8393d4bcd55a`  |
| 2098   | Layout 1 | `8393d4bcd55a`  |
| 2089   | Layout 1 | `8393d4bcd55a`  |
| 2081   | Layout 1 | `8393d4bcd55a`  |
| 2073   | Layout 1 | `8393d4bcd55a`  |
| 2067   | Layout 1 | `8393d4bcd55a`  |
| 2063   | Layout 1 | `8393d4bcd55a`  |
| 2059   | Layout 1 | `8393d4bcd55a`  |
| 2052   | Layout 1 | `8393d4bcd55a`  |
| 2044   | Layout 1 | `8393d4bcd55a`  |
| 2039   | Layout 1 | `8393d4bcd55a`  |
| 2032   | Layout 1 | `8393d4bcd55a`  |
| 2025   | Layout 1 | `8393d4bcd55a`  |
| 2011   | Layout 1 | `8393d4bcd55a`  |
| 2005   | Layout 1 | `8393d4bcd55a`  |
| 2000   | Layout 1 | `8393d4bcd55a`  |
| 1996   | Layout 1 | `8393d4bcd55a`  |
| 1991   | Layout 1 | `8393d4bcd55a`  |
| 1985   | Layout 1 | `8393d4bcd55a`  |
| 1980   | Layout 1 | `8393d4bcd55a`  |
| 1969   | Layout 1 | `8393d4bcd55a`  |
| 1964   | Layout 1 | `8393d4bcd55a`  |
| 1958   | Layout 1 | `8393d4bcd55a`  |
| 1950   | Layout 1 | `8393d4bcd55a`  |
| 1945   | Layout 1 | `8393d4bcd55a`  |
| 1937   | Layout 1 | `8393d4bcd55a`  |
| 1933   | Layout 1 | `8393d4bcd55a`  |
| 1927   | Layout 1 | `8393d4bcd55a`  |
| 1921   | Layout 1 | `8393d4bcd55a`  |
| 1914   | Layout 1 | `8393d4bcd55a`  |
| 1908   | Layout 1 | `8393d4bcd55a`  |
| 1897   | Layout 1 | `8393d4bcd55a`  |
| 1892   | Layout 1 | `8393d4bcd55a`  |
| 1886   | Layout 1 | `8393d4bcd55a`  |
| 1881   | Layout 1 | `8393d4bcd55a`  |
| 1871   | Layout 1 | `8393d4bcd55a`  |
| 1866   | Layout 1 | `8393d4bcd55a`  |
| 1862   | Layout 1 | `8393d4bcd55a`  |
| 1854   | Layout 1 | `8393d4bcd55a`  |
| 1846   | Layout 1 | `8393d4bcd55a`  |
| 1838   | Layout 1 | `8393d4bcd55a`  |
| 1832   | Layout 1 | `8393d4bcd55a`  |
| 1826   | Layout 1 | `8393d4bcd55a`  |
| 1822   | Layout 1 | `8393d4bcd55a`  |
| 1818   | Layout 1 | `8393d4bcd55a`  |
| 1804   | Layout 1 | `8393d4bcd55a`  |
| 1794   | Layout 1 | `8393d4bcd55a`  |
| 1790   | Layout 1 | `8393d4bcd55a`  |
| 1784   | Layout 1 | `8393d4bcd55a`  |
| 1774   | Layout 1 | `8393d4bcd55a`  |
| 1771   | Layout 1 | `8393d4bcd55a`  |
| 1762   | Layout 1 | `8393d4bcd55a`  |
| 1759   | Layout 1 | `8393d4bcd55a`  |
| 1754   | Layout 1 | `8393d4bcd55a`  |
| 1749   | Layout 1 | `8393d4bcd55a`  |
| 1743   | Layout 1 | `8393d4bcd55a`  |
| 1737   | Layout 1 | `8393d4bcd55a`  |
| 1731   | Layout 1 | `8393d4bcd55a`  |
| 1725   | Layout 1 | `8393d4bcd55a`  |
| 1717   | Layout 1 | `8393d4bcd55a`  |
| 1710   | Layout 1 | `8393d4bcd55a`  |
| 1704   | Layout 1 | `8393d4bcd55a`  |
| 1698   | Layout 1 | `8393d4bcd55a`  |
| 1690   | Layout 1 | `8393d4bcd55a`  |
| 1685   | Layout 1 | `8393d4bcd55a`  |
| 1680   | Layout 1 | `8393d4bcd55a`  |
| 1674   | Layout 1 | `8393d4bcd55a`  |
| 1668   | Layout 1 | `8393d4bcd55a`  |
| 1659   | Layout 1 | `8393d4bcd55a`  |
| 1649   | Layout 1 | `8393d4bcd55a`  |
| 1642   | Layout 1 | `8393d4bcd55a`  |
| 1636   | Layout 1 | `8393d4bcd55a`  |
| 1628   | Layout 1 | `8393d4bcd55a`  |
| 1622   | Layout 1 | `8393d4bcd55a`  |
| 1614   | Layout 1 | `8393d4bcd55a`  |
| 1608   | Layout 1 | `8393d4bcd55a`  |
| 1602   | Layout 1 | `8393d4bcd55a`  |
| 1598   | Layout 1 | `8393d4bcd55a`  |
| 1594   | Layout 1 | `8393d4bcd55a`  |
| 1590   | Layout 1 | `8393d4bcd55a`  |
| 1587   | Layout 1 | `8393d4bcd55a`  |
| 1584   | Layout 1 | `8393d4bcd55a`  |
| 1579   | Layout 1 | `8393d4bcd55a`  |
| 1572   | Layout 1 | `8393d4bcd55a`  |
| 1565   | Layout 1 | `8393d4bcd55a`  |
| 1559   | Layout 1 | `8393d4bcd55a`  |
| 1554   | Layout 1 | `8393d4bcd55a`  |
| 1547   | Layout 1 | `8393d4bcd55a`  |
| 1537   | Layout 1 | `8393d4bcd55a`  |
| 1529   | Layout 1 | `8393d4bcd55a`  |
| 1524   | Layout 1 | `8393d4bcd55a`  |
| 1519   | Layout 1 | `8393d4bcd55a`  |
| 1509   | Layout 1 | `8393d4bcd55a`  |
| 1506   | Layout 1 | `8393d4bcd55a`  |
| 1504   | Layout 1 | `8393d4bcd55a`  |
| 1500   | Layout 1 | `8393d4bcd55a`  |
| 1493   | Layout 1 | `8393d4bcd55a`  |
| 1489   | Layout 1 | `8393d4bcd55a`  |
| 1485   | Layout 1 | `8393d4bcd55a`  |
| 1481   | Layout 1 | `8393d4bcd55a`  |
| 1474   | Layout 1 | `8393d4bcd55a`  |
| 1466   | Layout 1 | `8393d4bcd55a`  |
| 1462   | Layout 1 | `8393d4bcd55a`  |
| 1459   | Layout 1 | `8393d4bcd55a`  |
| 1453   | Layout 1 | `8393d4bcd55a`  |
| 1450   | Layout 1 | `8393d4bcd55a`  |
| 1445   | Layout 1 | `8393d4bcd55a`  |
| 1439   | Layout 1 | `8393d4bcd55a`  |
| 1433   | Layout 1 | `8393d4bcd55a`  |
| 1430   | Layout 1 | `8393d4bcd55a`  |
| 1426   | Layout 1 | `8393d4bcd55a`  |
| 1421   | Layout 1 | `8393d4bcd55a`  |
| 1417   | Layout 1 | `8393d4bcd55a`  |
| 1416   | Layout 1 | `8393d4bcd55a`  |
| 1409   | Layout 1 | `8393d4bcd55a`  |
| 1405   | Layout 1 | `8393d4bcd55a`  |
| 1401   | Layout 1 | `8393d4bcd55a`  |
| 1396   | Layout 1 | `8393d4bcd55a`  |
| 1391   | Layout 1 | `8393d4bcd55a`  |
| 1390   | Layout 1 | `8393d4bcd55a`  |
| 1386   | Layout 1 | `8393d4bcd55a`  |
| 1381   | Layout 1 | `8393d4bcd55a`  |
| 1379   | Layout 1 | `8393d4bcd55a`  |
| 1372   | Layout 1 | `8393d4bcd55a`  |
| 1366   | Layout 1 | `8393d4bcd55a`  |
| 1364   | Layout 1 | `8393d4bcd55a`  |
| 1363   | Layout 1 | `8393d4bcd55a`  |
| 1360   | Layout 1 | `8393d4bcd55a`  |
| 1358   | Layout 1 | `8393d4bcd55a`  |
| 1355   | Layout 1 | `8393d4bcd55a`  |
| 1351   | Layout 1 | `8393d4bcd55a`  |
| 1348   | Layout 1 | `8393d4bcd55a`  |
| 1346   | Layout 1 | `8393d4bcd55a`  |
| 1341   | Layout 1 | `8393d4bcd55a`  |
| 1340   | Layout 1 | `8393d4bcd55a`  |
| 1338   | Layout 1 | `8393d4bcd55a`  |
| 1335   | Layout 1 | `8393d4bcd55a`  |
| 1333   | Layout 1 | `8393d4bcd55a`  |
| 1329   | Layout 1 | `8393d4bcd55a`  |
| 1327   | Layout 1 | `8393d4bcd55a`  |
| 1324   | Layout 1 | `8393d4bcd55a`  |
| 1321   | Layout 1 | `8393d4bcd55a`  |
| 1319   | Layout 1 | `8393d4bcd55a`  |
| 1318   | Layout 1 | `8393d4bcd55a`  |
| 1316   | Layout 1 | `8393d4bcd55a`  |
| 1313   | Layout 1 | `8393d4bcd55a`  |
| 1311   | Layout 1 | `8393d4bcd55a`  |
| 1309   | Layout 1 | `8393d4bcd55a`  |
| 1304   | Layout 1 | `8393d4bcd55a`  |
| 1292   | Layout 1 | `8393d4bcd55a`  |
| 1286   | Layout 1 | `8393d4bcd55a`  |
| 1280   | Layout 1 | `8393d4bcd55a`  |
| 1276   | Layout 1 | `8393d4bcd55a`  |
| 1267   | Layout 1 | `8393d4bcd55a`  |
| 1261   | Layout 1 | `8393d4bcd55a`  |
| 1256   | Layout 1 | `8393d4bcd55a`  |
| 1250   | Layout 1 | `8393d4bcd55a`  |
| 1246   | Layout 1 | `8393d4bcd55a`  |
| 1239   | Layout 1 | `8393d4bcd55a`  |
| 1230   | No file  | `8393d4bcd55a`  |
| 1226   | No file  | `8393d4bcd55a`  |
| 1220   | Layout 1 | `8393d4bcd55a`  |
| 1217   | Layout 1 | `8393d4bcd55a`  |
| 1211   | Layout 1 | `8393d4bcd55a`  |
| 1210   | Layout 1 | `8393d4bcd55a`  |
| 1208   | Layout 1 | `8393d4bcd55a`  |
| 1203   | Layout 1 | `8393d4bcd55a`  |
| 1197   | Layout 1 | `8393d4bcd55a`  |
| 1194   | Layout 1 | `8393d4bcd55a`  |
| 1192   | Layout 1 | `8393d4bcd55a`  |
| 1187   | Layout 1 | `8393d4bcd55a`  |
| 1183   | Layout 1 | `8393d4bcd55a`  |
| 1177   | Layout 1 | `8393d4bcd55a`  |
| 1173   | Layout 1 | `8393d4bcd55a`  |
| 1167   | Layout 1 | `8393d4bcd55a`  |
| 1164   | Layout 1 | `8393d4bcd55a`  |
| 1156   | Layout 1 | `8393d4bcd55a`  |
| 1149   | Layout 1 | `8393d4bcd55a`  |
| 1144   | Layout 1 | `8393d4bcd55a`  |
| 1137   | Layout 1 | `8393d4bcd55a`  |
| 1132   | Layout 1 | `8393d4bcd55a`  |
| 1127   | Layout 1 | `8393d4bcd55a`  |
| 1122   | Layout 1 | `8393d4bcd55a`  |
| 1118   | Layout 1 | `8393d4bcd55a`  |
| 1114   | Layout 1 | `8393d4bcd55a`  |
| 1109   | Layout 1 | `8393d4bcd55a`  |
| 1102   | Layout 1 | `8393d4bcd55a`  |
| 1096   | Layout 1 | `8393d4bcd55a`  |
| 1088   | Layout 1 | `8393d4bcd55a`  |
| 1081   | Layout 1 | `8393d4bcd55a`  |
| 1076   | Layout 1 | `8393d4bcd55a`  |
| 1069   | Layout 1 | `8393d4bcd55a`  |
| 1064   | Layout 1 | `8393d4bcd55a`  |
| 1058   | Layout 1 | `8393d4bcd55a`  |
| 1051   | Layout 1 | `8393d4bcd55a`  |
| 1044   | Layout 1 | `8393d4bcd55a`  |
| 1036   | Layout 1 | `8393d4bcd55a`  |
| 1026   | Layout 1 | `8393d4bcd55a`  |
| 1016   | Layout 1 | `8393d4bcd55a`  |
| 1009   | Layout 1 | `8393d4bcd55a`  |
| 1005   | Layout 1 | `8393d4bcd55a`  |
| 1000   | Layout 1 | `8393d4bcd55a`  |
| 998    | Layout 1 | `8393d4bcd55a`  |
| 990    | Layout 1 | `8393d4bcd55a`  |
| 979    | Layout 1 | `8393d4bcd55a`  |
| 972    | Layout 1 | `8393d4bcd55a`  |
| 963    | Layout 1 | `8393d4bcd55a`  |
| 955    | Layout 1 | `8393d4bcd55a`  |
| 946    | Layout 1 | `8393d4bcd55a`  |
| 938    | No file  | `8393d4bcd55a`  |
| 927    | No file  | `8393d4bcd55a`  |
| 911    | No file  | `8393d4bcd55a`  |
| 904    | No file  | `8393d4bcd55a`  |
| 899    | No file  | `8393d4bcd55a`  |
| 894    | No file  | `8393d4bcd55a`  |
| 885    | No file  | `8393d4bcd55a`  |
| 879    | No file  | `8393d4bcd55a`  |
| 872    | No file  | `8393d4bcd55a`  |
| 864    | No file  | `8393d4bcd55a`  |
| 855    | No file  | `8393d4bcd55a`  |
| 853    | No file  | `8393d4bcd55a`  |
| 845    | No file  | `8393d4bcd55a`  |
| 837    | No file  | `8393d4bcd55a`  |
| 829    | No file  | `8393d4bcd55a`  |
| 822    | No file  | `8393d4bcd55a`  |
| 814    | No file  | `8393d4bcd55a`  |
| 805    | No file  | `8393d4bcd55a`  |
| 794    | No file  | `8393d4bcd55a`  |
| 787    | No file  | `8393d4bcd55a`  |
| 780    | No file  | `8393d4bcd55a`  |
| 771    | No file  | `8393d4bcd55a`  |
| 760    | No file  | `8393d4bcd55a`  |
| 748    | No file  | `8393d4bcd55a`  |
| 741    | No file  | `8393d4bcd55a`  |
| 736    | No file  | `8393d4bcd55a`  |
| 731    | No file  | `8393d4bcd55a`  |
| 723    | No file  | `8393d4bcd55a`  |
| 711    | No file  | `8393d4bcd55a`  |
| 707    | No file  | `8393d4bcd55a`  |
| 697    | No file  | `8393d4bcd55a`  |
| 689    | No file  | `8393d4bcd55a`  |
| 683    | No file  | `8393d4bcd55a`  |
| 678    | No file  | `8393d4bcd55a`  |
| 670    | No file  | `8393d4bcd55a`  |
| 661    | No file  | `8393d4bcd55a`  |
| 656    | No file  | `8393d4bcd55a`  |
| 652    | No file  | `8393d4bcd55a`  |
| 643    | No file  | `8393d4bcd55a`  |
| 637    | No file  | `8393d4bcd55a`  |
| 630    | No file  | `8393d4bcd55a`  |
| 627    | No file  | `8393d4bcd55a`  |
| 621    | No file  | `8393d4bcd55a`  |
| 617    | No file  | `8393d4bcd55a`  |
| 615    | No file  | `8393d4bcd55a`  |
| 606    | No file  | `8393d4bcd55a`  |
| 599    | No file  | `8393d4bcd55a`  |
| 592    | No file  | `8393d4bcd55a`  |
| 586    | No file  | `8393d4bcd55a`  |
| 577    | No file  | `8393d4bcd55a`  |
| 569    | No file  | `8393d4bcd55a`  |
| 561    | No file  | `8393d4bcd55a`  |
| 554    | No file  | `8393d4bcd55a`  |
| 542    | No file  | `8393d4bcd55a`  |
| 532    | No file  | `8393d4bcd55a`  |
| 531    | No file  | `8393d4bcd55a`  |
| 526    | No file  | `8393d4bcd55a`  |
| 521    | No file  | `8393d4bcd55a`  |
| 517    | No file  | `8393d4bcd55a`  |
| 510    | No file  | `8393d4bcd55a`  |
| 508    | No file  | `8393d4bcd55a`  |
| 504    | No file  | `8393d4bcd55a`  |
| 497    | No file  | `8393d4bcd55a`  |
| 491    | No file  | `8393d4bcd55a`  |
| 485    | No file  | `8393d4bcd55a`  |
| 478    | No file  | `8393d4bcd55a`  |
| 472    | No file  | `8393d4bcd55a`  |
| 466    | No file  | `8393d4bcd55a`  |
| 457    | No file  | `8393d4bcd55a`  |
| 452    | No file  | `8393d4bcd55a`  |
| 449    | No file  | `8393d4bcd55a`  |
| 435    | No file  | `8393d4bcd55a`  |

<!-- versions:end -->

## Companion Files

The file is self-contained. All multi-byte values are little-endian.

## Layout 1

### File Layout

The layout of [`commonlifestatdata.bss`](commonlifestatdata_bss.md): PABR,
then one entry per level with no row count, the empty string table and the
8-byte trailer.

| Offset     | Type               | Field        | Notes                                                                    |
| ---------- | ------------------ | ------------ | ------------------------------------------------------------------------ |
| `+0x00`    | char[4]            | magic        | ASCII `PABR`                                                             |
| `+0x04`    | Level Entry[..table_start] | entries      | One entry per level from level 1, up to `table_start`; 180 on client 3464 |
| `EOF-0x0C` | u32                | string_count | Always `0`                                                               |
| `EOF-0x08` | u32                | table_start  | Offset of `string_count`, where the entries end                          |
| `EOF-0x04` | u32                | zero         | Always `0`                                                               |

### Level Entry (8 bytes)

| Offset  | Type | Field                        | Notes                                                    |
| ------- | ---- | ---------------------------- | -------------------------------------------------------- |
| `+0x00` | u32  | add_vehicle_skill_owner_rate | Mount skill learn chance, `1,000,000` = 100%; `1,000,000` from Guru 20 on client 3464 |
| `+0x04` | u32  | add_servant_stat_rate        | Higher minimum movement speed chance, `1,000,000` = 100%; `470,000` from Guru 50 on client 3464 |

Entry `n` (from 0) belongs to level `n + 1`, as in
[`commonlifestatdata.bss`](commonlifestatdata_bss.md).
`add_vehicle_skill_owner_rate` changes its step per level at every rank
start under that reading (client 3464):

| Levels                       | `add_vehicle_skill_owner_rate` step per level |
| ---------------------------- | --------------------------------------------- |
| Beginner 2 to 10             | 3,000 (from 10,000)                           |
| Apprentice 1 to 10           | 3,300                                         |
| Skilled 1 to 10              | 3,600                                         |
| Professional 1 to 10         | 6,500                                         |
| Artisan 1 to 10              | 7,000                                         |
| Master 1 to 10               | 7,500                                         |
| Master 11 to 20              | 12,800                                        |
| Master 21 to 30              | 13,600                                        |
| Guru 1 to 10                 | 14,400                                        |
| Guru 11 to 19                | 18,000                                        |
| Guru 20 to 100               | `1,000,000` flat                              |

`add_servant_stat_rate` rises in uneven steps from `10,000` at Beginner 2 to
`470,000` at Guru 50 and stays there. Both are 0 at Beginner 1.

`ToClient_getTrainingLevelSkillStatStaticStatus()` returns a wrapper with two
members, read in `panel_characterinfo_basic_all_2.luac` (behind
`_ContentsGroup_EnhanceTraining`):

```lua
skillRate = string.format("%.1f", trainingSKillStatStaticStatus._addVehicleSkillOwnerRate / 10000)
statRate = string.format("%.1f", trainingSKillStatStaticStatus._addServantStatRate / 10000)
```

They fill `rate1` and `rate2` of `LUA_CHARACTERINFO_LIFE_TRAINING_DESC_2`:
"+{rate1}% chance for your mount to learn a skill when your mount gains a
level" and "+{rate2}% chance to gain higher minimal movement speed when your
mount gains a level"; `rate3` is `ToClient_GetServantMarketTaxPercent()`.
The stable's skill tooltip in `panel_dialog_servantsimulator_5.luac` shows
`_addVehicleSkillOwnerRate` alone as
`LUA_SERVANTSIMULATOR_LEARNSKILLRATEFROMTRAININGLEVEL` ("- Based on Training
Level: {percent}%").

The Lua reads both members by name, so the in-game tooltip fixes the order:
at Training Artisan 7 (level 47) it shows +21.7% skill learn chance and
+21.4% higher minimum speed chance, entry 46's `+0x00` and `+0x04` (client
3464). Level 46 holds 21.0% for both, so the same tooltip also confirms the
entry `n` = level `n + 1` reading.

## Notes

- The handler is `_bss/traininglevelskillstat/`. It reads the entries with
  `parse_level_entries` from `_bss/commonlifestatdata/parser.py` and the
  rank text with `rank_text` from `_dbss/lifeexp/labels.py`.
- The column labels follow `LUA_CHARACTERINFO_LIFE_TRAINING_DESC_2` in each
  language's LOC.
- In the mount Growth Calculator, `add_servant_stat_rate` raises the
  lowest movement gain a level-up can roll to `1 + round(die max x rate /
  1,000,000)` tenths of a percent, where the die is the horse's movement
  dice in [servantexperience.dbss](../dbss/servantexperience_dbss.md); every value
  from that floor to the die maximum stays equally likely. I checked it on a
  `1D13` and a `1D10` horse at three Training levels (the table is in that
  doc's Notes).
