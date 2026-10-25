# `elementalstat.bss` Format

## Purpose

One row per aura of the Black Shrine (검은 사당) boss blitz in the Land of
the Morning Light: Sun Aura, Moon Aura and Earth Aura. The player enhances an
aura with Light Orbs and spends the Additional Stats it gives on the aura's
AP and DP. Each row holds the aura's `element_type` and what one Light Orb
adds to it: 50 AP, 100 DP and 3 Additional Stats on every row (client
3474).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------- | ----- | ------- | --------- |
| 1      | 2224 and later | `elementalstat.bss` | 46    | 3 Row   | 14        |

| Layout | File                | Known         | Unknown    |
| ------ | ------------------- | ------------- | ---------- |
| 1      | `elementalstat.bss` | 46 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `5bacf6d5d5e8`  |
| 3482   | Layout 1 | `5bacf6d5d5e8`  |
| 3474   | Layout 1 | `5bacf6d5d5e8`  |
| 3473   | Layout 1 | `5bacf6d5d5e8`  |
| 3464   | Layout 1 | `5bacf6d5d5e8`  |
| 3458   | Layout 1 | `5bacf6d5d5e8`  |
| 3454   | Layout 1 | `5bacf6d5d5e8`  |
| 3444   | Layout 1 | `5bacf6d5d5e8`  |
| 3435   | Layout 1 | `5bacf6d5d5e8`  |
| 3426   | Layout 1 | `5bacf6d5d5e8`  |
| 3418   | Layout 1 | `5bacf6d5d5e8`  |
| 3412   | Layout 1 | `5bacf6d5d5e8`  |
| 3402   | Layout 1 | `5bacf6d5d5e8`  |
| 3396   | Layout 1 | `5bacf6d5d5e8`  |
| 3387   | Layout 1 | `5bacf6d5d5e8`  |
| 3381   | Layout 1 | `5bacf6d5d5e8`  |
| 3373   | Layout 1 | `5bacf6d5d5e8`  |
| 3364   | Layout 1 | `5bacf6d5d5e8`  |
| 3356   | Layout 1 | `5bacf6d5d5e8`  |
| 3349   | Layout 1 | `5bacf6d5d5e8`  |
| 3342   | Layout 1 | `5bacf6d5d5e8`  |
| 3335   | Layout 1 | `5bacf6d5d5e8`  |
| 3326   | Layout 1 | `5bacf6d5d5e8`  |
| 3321   | Layout 1 | `5bacf6d5d5e8`  |
| 3314   | Layout 1 | `5bacf6d5d5e8`  |
| 3303   | Layout 1 | `5bacf6d5d5e8`  |
| 3302   | Layout 1 | `5bacf6d5d5e8`  |
| 3293   | Layout 1 | `5bacf6d5d5e8`  |
| 3283   | Layout 1 | `5bacf6d5d5e8`  |
| 3275   | Layout 1 | `5bacf6d5d5e8`  |
| 3267   | Layout 1 | `5bacf6d5d5e8`  |
| 3258   | Layout 1 | `5bacf6d5d5e8`  |
| 3251   | Layout 1 | `5bacf6d5d5e8`  |
| 3242   | Layout 1 | `5bacf6d5d5e8`  |
| 3235   | Layout 1 | `5bacf6d5d5e8`  |
| 3229   | Layout 1 | `5bacf6d5d5e8`  |
| 3212   | Layout 1 | `5bacf6d5d5e8`  |
| 3203   | Layout 1 | `5bacf6d5d5e8`  |
| 3193   | Layout 1 | `5bacf6d5d5e8`  |
| 3186   | Layout 1 | `5bacf6d5d5e8`  |
| 3177   | Layout 1 | `5bacf6d5d5e8`  |
| 3169   | Layout 1 | `5bacf6d5d5e8`  |
| 3158   | Layout 1 | `5bacf6d5d5e8`  |
| 3151   | Layout 1 | `5bacf6d5d5e8`  |
| 3144   | Layout 1 | `5bacf6d5d5e8`  |
| 3133   | Layout 1 | `5bacf6d5d5e8`  |
| 3125   | Layout 1 | `5bacf6d5d5e8`  |
| 3118   | Layout 1 | `5bacf6d5d5e8`  |
| 3111   | Layout 1 | `5bacf6d5d5e8`  |
| 3103   | Layout 1 | `5bacf6d5d5e8`  |
| 3095   | Layout 1 | `5bacf6d5d5e8`  |
| 3086   | Layout 1 | `5bacf6d5d5e8`  |
| 3072   | Layout 1 | `5bacf6d5d5e8`  |
| 3062   | Layout 1 | `5bacf6d5d5e8`  |
| 3052   | Layout 1 | `5bacf6d5d5e8`  |
| 3045   | Layout 1 | `5bacf6d5d5e8`  |
| 3037   | Layout 1 | `5bacf6d5d5e8`  |
| 3030   | Layout 1 | `5bacf6d5d5e8`  |
| 3021   | Layout 1 | `5bacf6d5d5e8`  |
| 3012   | Layout 1 | `5bacf6d5d5e8`  |
| 3002   | Layout 1 | `5bacf6d5d5e8`  |
| 2995   | Layout 1 | `5bacf6d5d5e8`  |
| 2987   | Layout 1 | `5bacf6d5d5e8`  |
| 2978   | Layout 1 | `5bacf6d5d5e8`  |
| 2970   | Layout 1 | `5bacf6d5d5e8`  |
| 2959   | Layout 1 | `5bacf6d5d5e8`  |
| 2951   | Layout 1 | `5bacf6d5d5e8`  |
| 2942   | Layout 1 | `5bacf6d5d5e8`  |
| 2935   | Layout 1 | `5bacf6d5d5e8`  |
| 2932   | Layout 1 | `5bacf6d5d5e8`  |
| 2923   | Layout 1 | `5bacf6d5d5e8`  |
| 2919   | Layout 1 | `5bacf6d5d5e8`  |
| 2907   | Layout 1 | `5bacf6d5d5e8`  |
| 2900   | Layout 1 | `5bacf6d5d5e8`  |
| 2891   | Layout 1 | `5bacf6d5d5e8`  |
| 2882   | Layout 1 | `5bacf6d5d5e8`  |
| 2872   | Layout 1 | `5bacf6d5d5e8`  |
| 2863   | Layout 1 | `5bacf6d5d5e8`  |
| 2855   | Layout 1 | `5bacf6d5d5e8`  |
| 2849   | Layout 1 | `5bacf6d5d5e8`  |
| 2844   | Layout 1 | `5bacf6d5d5e8`  |
| 2834   | Layout 1 | `5bacf6d5d5e8`  |
| 2825   | Layout 1 | `5bacf6d5d5e8`  |
| 2819   | Layout 1 | `5bacf6d5d5e8`  |
| 2811   | Layout 1 | `5bacf6d5d5e8`  |
| 2803   | Layout 1 | `5bacf6d5d5e8`  |
| 2794   | Layout 1 | `5bacf6d5d5e8`  |
| 2783   | Layout 1 | `5bacf6d5d5e8`  |
| 2774   | Layout 1 | `5bacf6d5d5e8`  |
| 2765   | Layout 1 | `5bacf6d5d5e8`  |
| 2756   | Layout 1 | `5bacf6d5d5e8`  |
| 2750   | Layout 1 | `5bacf6d5d5e8`  |
| 2743   | Layout 1 | `5bacf6d5d5e8`  |
| 2736   | Layout 1 | `5bacf6d5d5e8`  |
| 2726   | Layout 1 | `5bacf6d5d5e8`  |
| 2717   | Layout 1 | `5bacf6d5d5e8`  |
| 2709   | Layout 1 | `5bacf6d5d5e8`  |
| 2703   | Layout 1 | `5bacf6d5d5e8`  |
| 2695   | Layout 1 | `5bacf6d5d5e8`  |
| 2684   | Layout 1 | `5bacf6d5d5e8`  |
| 2672   | Layout 1 | `5bacf6d5d5e8`  |
| 2665   | Layout 1 | `5bacf6d5d5e8`  |
| 2657   | Layout 1 | `5bacf6d5d5e8`  |
| 2649   | Layout 1 | `5bacf6d5d5e8`  |
| 2644   | Layout 1 | `5bacf6d5d5e8`  |
| 2637   | Layout 1 | `5bacf6d5d5e8`  |
| 2629   | Layout 1 | `5bacf6d5d5e8`  |
| 2619   | Layout 1 | `5bacf6d5d5e8`  |
| 2612   | Layout 1 | `5bacf6d5d5e8`  |
| 2606   | Layout 1 | `5bacf6d5d5e8`  |
| 2602   | Layout 1 | `5bacf6d5d5e8`  |
| 2601   | Layout 1 | `5bacf6d5d5e8`  |
| 2592   | Layout 1 | `5bacf6d5d5e8`  |
| 2583   | Layout 1 | `5bacf6d5d5e8`  |
| 2575   | Layout 1 | `5bacf6d5d5e8`  |
| 2567   | Layout 1 | `5bacf6d5d5e8`  |
| 2560   | Layout 1 | `5bacf6d5d5e8`  |
| 2553   | Layout 1 | `5bacf6d5d5e8`  |
| 2545   | Layout 1 | `5bacf6d5d5e8`  |
| 2538   | Layout 1 | `5bacf6d5d5e8`  |
| 2529   | Layout 1 | `5bacf6d5d5e8`  |
| 2519   | Layout 1 | `5bacf6d5d5e8`  |
| 2513   | Layout 1 | `5bacf6d5d5e8`  |
| 2510   | Layout 1 | `5bacf6d5d5e8`  |
| 2507   | Layout 1 | `5bacf6d5d5e8`  |
| 2503   | Layout 1 | `5bacf6d5d5e8`  |
| 2498   | Layout 1 | `5bacf6d5d5e8`  |
| 2492   | Layout 1 | `5bacf6d5d5e8`  |
| 2487   | Layout 1 | `5bacf6d5d5e8`  |
| 2480   | Layout 1 | `5bacf6d5d5e8`  |
| 2474   | Layout 1 | `5bacf6d5d5e8`  |
| 2468   | Layout 1 | `5bacf6d5d5e8`  |
| 2460   | Layout 1 | `5bacf6d5d5e8`  |
| 2453   | Layout 1 | `5bacf6d5d5e8`  |
| 2444   | Layout 1 | `5bacf6d5d5e8`  |
| 2438   | Layout 1 | `5bacf6d5d5e8`  |
| 2434   | Layout 1 | `5bacf6d5d5e8`  |
| 2429   | Layout 1 | `5bacf6d5d5e8`  |
| 2421   | Layout 1 | `5bacf6d5d5e8`  |
| 2414   | Layout 1 | `5bacf6d5d5e8`  |
| 2407   | Layout 1 | `5bacf6d5d5e8`  |
| 2401   | Layout 1 | `5bacf6d5d5e8`  |
| 2397   | Layout 1 | `5bacf6d5d5e8`  |
| 2393   | Layout 1 | `5bacf6d5d5e8`  |
| 2384   | Layout 1 | `5bacf6d5d5e8`  |
| 2378   | Layout 1 | `5bacf6d5d5e8`  |
| 2372   | Layout 1 | `5bacf6d5d5e8`  |
| 2358   | Layout 1 | `5bacf6d5d5e8`  |
| 2352   | Layout 1 | `5bacf6d5d5e8`  |
| 2347   | Layout 1 | `5bacf6d5d5e8`  |
| 2343   | Layout 1 | `5bacf6d5d5e8`  |
| 2335   | Layout 1 | `5bacf6d5d5e8`  |
| 2327   | Layout 1 | `5bacf6d5d5e8`  |
| 2324   | Layout 1 | `5bacf6d5d5e8`  |
| 2319   | Layout 1 | `5bacf6d5d5e8`  |
| 2313   | Layout 1 | `5bacf6d5d5e8`  |
| 2308   | Layout 1 | `5bacf6d5d5e8`  |
| 2302   | Layout 1 | `5bacf6d5d5e8`  |
| 2295   | Layout 1 | `5bacf6d5d5e8`  |
| 2290   | Layout 1 | `5bacf6d5d5e8`  |
| 2284   | Layout 1 | `5bacf6d5d5e8`  |
| 2276   | Layout 1 | `5bacf6d5d5e8`  |
| 2269   | Layout 1 | `5bacf6d5d5e8`  |
| 2259   | Layout 1 | `5bacf6d5d5e8`  |
| 2250   | Layout 1 | `5bacf6d5d5e8`  |
| 2243   | Layout 1 | `5bacf6d5d5e8`  |
| 2235   | Layout 1 | `5bacf6d5d5e8`  |
| 2229   | Layout 1 | `5bacf6d5d5e8`  |
| 2224   | Layout 1 | `5bacf6d5d5e8`  |
| 2218   | No file  | `5bacf6d5d5e8`  |
| 2215   | No file  | `5bacf6d5d5e8`  |
| 2207   | No file  | `5bacf6d5d5e8`  |
| 2203   | No file  | `5bacf6d5d5e8`  |
| 2196   | No file  | `5bacf6d5d5e8`  |
| 2192   | No file  | `5bacf6d5d5e8`  |
| 2189   | No file  | `5bacf6d5d5e8`  |
| 2183   | No file  | `5bacf6d5d5e8`  |
| 2179   | No file  | `5bacf6d5d5e8`  |
| 2171   | No file  | `5bacf6d5d5e8`  |
| 2163   | No file  | `5bacf6d5d5e8`  |
| 2156   | No file  | `5bacf6d5d5e8`  |
| 2151   | No file  | `5bacf6d5d5e8`  |
| 2147   | No file  | `5bacf6d5d5e8`  |
| 2142   | No file  | `5bacf6d5d5e8`  |
| 2138   | No file  | `5bacf6d5d5e8`  |
| 2134   | No file  | `5bacf6d5d5e8`  |
| 2130   | No file  | `5bacf6d5d5e8`  |
| 2122   | No file  | `5bacf6d5d5e8`  |
| 2107   | No file  | `5bacf6d5d5e8`  |
| 2098   | No file  | `5bacf6d5d5e8`  |
| 2089   | No file  | `5bacf6d5d5e8`  |
| 2081   | No file  | `5bacf6d5d5e8`  |
| 2073   | No file  | `5bacf6d5d5e8`  |
| 2067   | No file  | `5bacf6d5d5e8`  |
| 2063   | No file  | `5bacf6d5d5e8`  |
| 2059   | No file  | `5bacf6d5d5e8`  |
| 2052   | No file  | `5bacf6d5d5e8`  |
| 2044   | No file  | `5bacf6d5d5e8`  |
| 2039   | No file  | `5bacf6d5d5e8`  |
| 2032   | No file  | `5bacf6d5d5e8`  |
| 2025   | No file  | `5bacf6d5d5e8`  |
| 2011   | No file  | `5bacf6d5d5e8`  |
| 2005   | No file  | `5bacf6d5d5e8`  |
| 2000   | No file  | `5bacf6d5d5e8`  |
| 1996   | No file  | `5bacf6d5d5e8`  |
| 1991   | No file  | `5bacf6d5d5e8`  |
| 1985   | No file  | `5bacf6d5d5e8`  |
| 1980   | No file  | `5bacf6d5d5e8`  |
| 1969   | No file  | `5bacf6d5d5e8`  |
| 1964   | No file  | `5bacf6d5d5e8`  |
| 1958   | No file  | `5bacf6d5d5e8`  |
| 1950   | No file  | `5bacf6d5d5e8`  |
| 1945   | No file  | `5bacf6d5d5e8`  |
| 1937   | No file  | `5bacf6d5d5e8`  |
| 1933   | No file  | `5bacf6d5d5e8`  |
| 1927   | No file  | `5bacf6d5d5e8`  |
| 1921   | No file  | `5bacf6d5d5e8`  |
| 1914   | No file  | `5bacf6d5d5e8`  |
| 1908   | No file  | `5bacf6d5d5e8`  |
| 1897   | No file  | `5bacf6d5d5e8`  |
| 1892   | No file  | `5bacf6d5d5e8`  |
| 1886   | No file  | `5bacf6d5d5e8`  |
| 1881   | No file  | `5bacf6d5d5e8`  |
| 1871   | No file  | `5bacf6d5d5e8`  |
| 1866   | No file  | `5bacf6d5d5e8`  |
| 1862   | No file  | `5bacf6d5d5e8`  |
| 1854   | No file  | `5bacf6d5d5e8`  |
| 1846   | No file  | `5bacf6d5d5e8`  |
| 1838   | No file  | `5bacf6d5d5e8`  |
| 1832   | No file  | `5bacf6d5d5e8`  |
| 1826   | No file  | `5bacf6d5d5e8`  |
| 1822   | No file  | `5bacf6d5d5e8`  |
| 1818   | No file  | `5bacf6d5d5e8`  |
| 1804   | No file  | `5bacf6d5d5e8`  |
| 1794   | No file  | `5bacf6d5d5e8`  |
| 1790   | No file  | `5bacf6d5d5e8`  |
| 1784   | No file  | `5bacf6d5d5e8`  |
| 1774   | No file  | `5bacf6d5d5e8`  |
| 1771   | No file  | `5bacf6d5d5e8`  |
| 1762   | No file  | `5bacf6d5d5e8`  |
| 1759   | No file  | `5bacf6d5d5e8`  |
| 1754   | No file  | `5bacf6d5d5e8`  |
| 1749   | No file  | `5bacf6d5d5e8`  |
| 1743   | No file  | `5bacf6d5d5e8`  |
| 1737   | No file  | `5bacf6d5d5e8`  |
| 1731   | No file  | `5bacf6d5d5e8`  |
| 1725   | No file  | `5bacf6d5d5e8`  |
| 1717   | No file  | `5bacf6d5d5e8`  |
| 1710   | No file  | `5bacf6d5d5e8`  |
| 1704   | No file  | `5bacf6d5d5e8`  |
| 1698   | No file  | `5bacf6d5d5e8`  |
| 1690   | No file  | `5bacf6d5d5e8`  |
| 1685   | No file  | `5bacf6d5d5e8`  |
| 1680   | No file  | `5bacf6d5d5e8`  |
| 1674   | No file  | `5bacf6d5d5e8`  |
| 1668   | No file  | `5bacf6d5d5e8`  |
| 1659   | No file  | `5bacf6d5d5e8`  |
| 1649   | No file  | `5bacf6d5d5e8`  |
| 1642   | No file  | `5bacf6d5d5e8`  |
| 1636   | No file  | `5bacf6d5d5e8`  |
| 1628   | No file  | `5bacf6d5d5e8`  |
| 1622   | No file  | `5bacf6d5d5e8`  |
| 1614   | No file  | `5bacf6d5d5e8`  |
| 1608   | No file  | `5bacf6d5d5e8`  |
| 1602   | No file  | `5bacf6d5d5e8`  |
| 1598   | No file  | `5bacf6d5d5e8`  |
| 1594   | No file  | `5bacf6d5d5e8`  |
| 1590   | No file  | `5bacf6d5d5e8`  |
| 1587   | No file  | `5bacf6d5d5e8`  |
| 1584   | No file  | `5bacf6d5d5e8`  |
| 1579   | No file  | `5bacf6d5d5e8`  |
| 1572   | No file  | `5bacf6d5d5e8`  |
| 1565   | No file  | `5bacf6d5d5e8`  |
| 1559   | No file  | `5bacf6d5d5e8`  |
| 1554   | No file  | `5bacf6d5d5e8`  |
| 1547   | No file  | `5bacf6d5d5e8`  |
| 1537   | No file  | `5bacf6d5d5e8`  |
| 1529   | No file  | `5bacf6d5d5e8`  |
| 1524   | No file  | `5bacf6d5d5e8`  |
| 1519   | No file  | `5bacf6d5d5e8`  |
| 1509   | No file  | `5bacf6d5d5e8`  |
| 1506   | No file  | `5bacf6d5d5e8`  |
| 1504   | No file  | `5bacf6d5d5e8`  |
| 1500   | No file  | `5bacf6d5d5e8`  |
| 1493   | No file  | `5bacf6d5d5e8`  |
| 1489   | No file  | `5bacf6d5d5e8`  |
| 1485   | No file  | `5bacf6d5d5e8`  |
| 1481   | No file  | `5bacf6d5d5e8`  |
| 1474   | No file  | `5bacf6d5d5e8`  |
| 1466   | No file  | `5bacf6d5d5e8`  |
| 1462   | No file  | `5bacf6d5d5e8`  |
| 1459   | No file  | `5bacf6d5d5e8`  |
| 1453   | No file  | `5bacf6d5d5e8`  |
| 1450   | No file  | `5bacf6d5d5e8`  |
| 1445   | No file  | `5bacf6d5d5e8`  |
| 1439   | No file  | `5bacf6d5d5e8`  |
| 1433   | No file  | `5bacf6d5d5e8`  |
| 1430   | No file  | `5bacf6d5d5e8`  |
| 1426   | No file  | `5bacf6d5d5e8`  |
| 1421   | No file  | `5bacf6d5d5e8`  |
| 1417   | No file  | `5bacf6d5d5e8`  |
| 1416   | No file  | `5bacf6d5d5e8`  |
| 1409   | No file  | `5bacf6d5d5e8`  |
| 1405   | No file  | `5bacf6d5d5e8`  |
| 1401   | No file  | `5bacf6d5d5e8`  |
| 1396   | No file  | `5bacf6d5d5e8`  |
| 1391   | No file  | `5bacf6d5d5e8`  |
| 1390   | No file  | `5bacf6d5d5e8`  |
| 1386   | No file  | `5bacf6d5d5e8`  |
| 1381   | No file  | `5bacf6d5d5e8`  |
| 1379   | No file  | `5bacf6d5d5e8`  |
| 1372   | No file  | `5bacf6d5d5e8`  |
| 1366   | No file  | `5bacf6d5d5e8`  |
| 1364   | No file  | `5bacf6d5d5e8`  |
| 1363   | No file  | `5bacf6d5d5e8`  |
| 1360   | No file  | `5bacf6d5d5e8`  |
| 1358   | No file  | `5bacf6d5d5e8`  |
| 1355   | No file  | `5bacf6d5d5e8`  |
| 1351   | No file  | `5bacf6d5d5e8`  |
| 1348   | No file  | `5bacf6d5d5e8`  |
| 1346   | No file  | `5bacf6d5d5e8`  |
| 1341   | No file  | `5bacf6d5d5e8`  |
| 1340   | No file  | `5bacf6d5d5e8`  |
| 1338   | No file  | `5bacf6d5d5e8`  |
| 1335   | No file  | `5bacf6d5d5e8`  |
| 1333   | No file  | `5bacf6d5d5e8`  |
| 1329   | No file  | `5bacf6d5d5e8`  |
| 1327   | No file  | `5bacf6d5d5e8`  |
| 1324   | No file  | `5bacf6d5d5e8`  |
| 1321   | No file  | `5bacf6d5d5e8`  |
| 1319   | No file  | `5bacf6d5d5e8`  |
| 1318   | No file  | `5bacf6d5d5e8`  |
| 1316   | No file  | `5bacf6d5d5e8`  |
| 1313   | No file  | `5bacf6d5d5e8`  |
| 1311   | No file  | `5bacf6d5d5e8`  |
| 1309   | No file  | `5bacf6d5d5e8`  |
| 1304   | No file  | `5bacf6d5d5e8`  |
| 1292   | No file  | `5bacf6d5d5e8`  |
| 1286   | No file  | `5bacf6d5d5e8`  |
| 1280   | No file  | `5bacf6d5d5e8`  |
| 1276   | No file  | `5bacf6d5d5e8`  |
| 1267   | No file  | `5bacf6d5d5e8`  |
| 1261   | No file  | `5bacf6d5d5e8`  |
| 1256   | No file  | `5bacf6d5d5e8`  |
| 1250   | No file  | `5bacf6d5d5e8`  |
| 1246   | No file  | `5bacf6d5d5e8`  |
| 1239   | No file  | `5bacf6d5d5e8`  |
| 1230   | No file  | `5bacf6d5d5e8`  |
| 1226   | No file  | `5bacf6d5d5e8`  |
| 1220   | No file  | `5bacf6d5d5e8`  |
| 1217   | No file  | `5bacf6d5d5e8`  |
| 1211   | No file  | `5bacf6d5d5e8`  |
| 1210   | No file  | `5bacf6d5d5e8`  |
| 1208   | No file  | `5bacf6d5d5e8`  |
| 1203   | No file  | `5bacf6d5d5e8`  |
| 1197   | No file  | `5bacf6d5d5e8`  |
| 1194   | No file  | `5bacf6d5d5e8`  |
| 1192   | No file  | `5bacf6d5d5e8`  |
| 1187   | No file  | `5bacf6d5d5e8`  |
| 1183   | No file  | `5bacf6d5d5e8`  |
| 1177   | No file  | `5bacf6d5d5e8`  |
| 1173   | No file  | `5bacf6d5d5e8`  |
| 1167   | No file  | `5bacf6d5d5e8`  |
| 1164   | No file  | `5bacf6d5d5e8`  |
| 1156   | No file  | `5bacf6d5d5e8`  |
| 1149   | No file  | `5bacf6d5d5e8`  |
| 1144   | No file  | `5bacf6d5d5e8`  |
| 1137   | No file  | `5bacf6d5d5e8`  |
| 1132   | No file  | `5bacf6d5d5e8`  |
| 1127   | No file  | `5bacf6d5d5e8`  |
| 1122   | No file  | `5bacf6d5d5e8`  |
| 1118   | No file  | `5bacf6d5d5e8`  |
| 1114   | No file  | `5bacf6d5d5e8`  |
| 1109   | No file  | `5bacf6d5d5e8`  |
| 1102   | No file  | `5bacf6d5d5e8`  |
| 1096   | No file  | `5bacf6d5d5e8`  |
| 1088   | No file  | `5bacf6d5d5e8`  |
| 1081   | No file  | `5bacf6d5d5e8`  |
| 1076   | No file  | `5bacf6d5d5e8`  |
| 1069   | No file  | `5bacf6d5d5e8`  |
| 1064   | No file  | `5bacf6d5d5e8`  |
| 1058   | No file  | `5bacf6d5d5e8`  |
| 1051   | No file  | `5bacf6d5d5e8`  |
| 1044   | No file  | `5bacf6d5d5e8`  |
| 1036   | No file  | `5bacf6d5d5e8`  |
| 1026   | No file  | `5bacf6d5d5e8`  |
| 1016   | No file  | `5bacf6d5d5e8`  |
| 1009   | No file  | `5bacf6d5d5e8`  |
| 1005   | No file  | `5bacf6d5d5e8`  |
| 1000   | No file  | `5bacf6d5d5e8`  |
| 998    | No file  | `5bacf6d5d5e8`  |
| 990    | No file  | `5bacf6d5d5e8`  |
| 979    | No file  | `5bacf6d5d5e8`  |
| 972    | No file  | `5bacf6d5d5e8`  |
| 963    | No file  | `5bacf6d5d5e8`  |
| 955    | No file  | `5bacf6d5d5e8`  |
| 946    | No file  | `5bacf6d5d5e8`  |
| 938    | No file  | `5bacf6d5d5e8`  |
| 927    | No file  | `5bacf6d5d5e8`  |
| 911    | No file  | `5bacf6d5d5e8`  |
| 904    | No file  | `5bacf6d5d5e8`  |
| 899    | No file  | `5bacf6d5d5e8`  |
| 894    | No file  | `5bacf6d5d5e8`  |
| 885    | No file  | `5bacf6d5d5e8`  |
| 879    | No file  | `5bacf6d5d5e8`  |
| 872    | No file  | `5bacf6d5d5e8`  |
| 864    | No file  | `5bacf6d5d5e8`  |
| 855    | No file  | `5bacf6d5d5e8`  |
| 853    | No file  | `5bacf6d5d5e8`  |
| 845    | No file  | `5bacf6d5d5e8`  |
| 837    | No file  | `5bacf6d5d5e8`  |
| 829    | No file  | `5bacf6d5d5e8`  |
| 822    | No file  | `5bacf6d5d5e8`  |
| 814    | No file  | `5bacf6d5d5e8`  |
| 805    | No file  | `5bacf6d5d5e8`  |
| 794    | No file  | `5bacf6d5d5e8`  |
| 787    | No file  | `5bacf6d5d5e8`  |
| 780    | No file  | `5bacf6d5d5e8`  |
| 771    | No file  | `5bacf6d5d5e8`  |
| 760    | No file  | `5bacf6d5d5e8`  |
| 748    | No file  | `5bacf6d5d5e8`  |
| 741    | No file  | `5bacf6d5d5e8`  |
| 736    | No file  | `5bacf6d5d5e8`  |
| 731    | No file  | `5bacf6d5d5e8`  |
| 723    | No file  | `5bacf6d5d5e8`  |
| 711    | No file  | `5bacf6d5d5e8`  |
| 707    | No file  | `5bacf6d5d5e8`  |
| 697    | No file  | `5bacf6d5d5e8`  |
| 689    | No file  | `5bacf6d5d5e8`  |
| 683    | No file  | `5bacf6d5d5e8`  |
| 678    | No file  | `5bacf6d5d5e8`  |
| 670    | No file  | `5bacf6d5d5e8`  |
| 661    | No file  | `5bacf6d5d5e8`  |
| 656    | No file  | `5bacf6d5d5e8`  |
| 652    | No file  | `5bacf6d5d5e8`  |
| 643    | No file  | `5bacf6d5d5e8`  |
| 637    | No file  | `5bacf6d5d5e8`  |
| 630    | No file  | `5bacf6d5d5e8`  |
| 627    | No file  | `5bacf6d5d5e8`  |
| 621    | No file  | `5bacf6d5d5e8`  |
| 617    | No file  | `5bacf6d5d5e8`  |
| 615    | No file  | `5bacf6d5d5e8`  |
| 606    | No file  | `5bacf6d5d5e8`  |
| 599    | No file  | `5bacf6d5d5e8`  |
| 592    | No file  | `5bacf6d5d5e8`  |
| 586    | No file  | `5bacf6d5d5e8`  |
| 577    | No file  | `5bacf6d5d5e8`  |
| 569    | No file  | `5bacf6d5d5e8`  |
| 561    | No file  | `5bacf6d5d5e8`  |
| 554    | No file  | `5bacf6d5d5e8`  |
| 542    | No file  | `5bacf6d5d5e8`  |
| 532    | No file  | `5bacf6d5d5e8`  |
| 531    | No file  | `5bacf6d5d5e8`  |
| 526    | No file  | `5bacf6d5d5e8`  |
| 521    | No file  | `5bacf6d5d5e8`  |
| 517    | No file  | `5bacf6d5d5e8`  |
| 510    | No file  | `5bacf6d5d5e8`  |
| 508    | No file  | `5bacf6d5d5e8`  |
| 504    | No file  | `5bacf6d5d5e8`  |
| 497    | No file  | `5bacf6d5d5e8`  |
| 491    | No file  | `5bacf6d5d5e8`  |
| 485    | No file  | `5bacf6d5d5e8`  |
| 478    | No file  | `5bacf6d5d5e8`  |
| 472    | No file  | `5bacf6d5d5e8`  |
| 466    | No file  | `5bacf6d5d5e8`  |
| 457    | No file  | `5bacf6d5d5e8`  |
| 452    | No file  | `5bacf6d5d5e8`  |
| 449    | No file  | `5bacf6d5d5e8`  |
| 435    | No file  | `5bacf6d5d5e8`  |

<!-- versions:end -->

## Companion Files

None. The handler names each aura with its LOC type 37 text (GAME sheet
keys `LUA_MORNING_ATTRBOSS_SUN`, `_MOON` and `_SOIL`, the keys the Black
Shrine window uses) from `languagedata_*.loc` when it is loaded, and with the
enum name otherwise.

All multi-byte values are little-endian.

## Layout 1

### File Layout

Plain binary: no `PABR` magic, no offset file and no trailer.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 3 x 14 = 46 bytes on client 3474, in
the order `2`, `1`, `0`.

### Row (14 bytes)

| Offset  | Type | Field               | Notes                                                       |
| ------- | ---- | ------------------- | ----------------------------------------------------------- |
| `+0x00` | u8   | element_type        | Row key, see [Element Types](#element-types)                |
| `+0x01` | u32  | ap_per_orb          | AP per activated Light Orb; `50` on every row (client 3474) |
| `+0x05` | u32  | dp_per_orb          | DP per activated Light Orb; `100` on every row (client 3474) |
| `+0x09` | u32  | stat_points_per_orb | Additional Stats per activated Light Orb; `3` on every row (client 3474) |
| `+0x0d` | u8   | element_type_dup    | Equals `element_type` on every row                          |

## Element Types

| Value | Lua enum                 | Name (LOC, client 3474) |
| ----- | ------------------------ | ----------------------- |
| `0`   | `__eElementalStat_Sun`   | Sun Aura                |
| `1`   | `__eElementalStat_Moon`  | Moon Aura               |
| `2`   | `__eElementalStat_Land`  | Earth Aura              |

## Field Names

No reference source has the file. It first appears on client 2519 (absent
on client 2107), so a private server's `DataSheets.bexcel`, `.xlsm` sheets
and server dump on client 1784 have no `Elemental` sheet or column, the 2016
client and the client 519 server tables predate it, and the live client exe
holds no readable strings.

`element_type` follows the client Lua of the Black Shrine window
(`panel_window_morningland_boss_all.luac` and `_all_1.luac`). It passes
`__eElementalStat_Sun`, `_Moon` and `_Land` to `initSelectedElementalType`
from the buttons `Radiobutton_Attribute_Tap0` to `Tap2`, finds the button of
a type at list position `type + 1`, and indexes `_effectChar` (`[0]`, `[1]`,
`[2]`) by the type, so the three values are `0`, `1` and `2` in that order.
`panel_personalicon_left_remaster.luac` uses the same order for the aura
buffs (`_elementalMonsterBuffSun = 0`, `Moon = 1`, `Land = 2`). A boss's
weak aura comes from `getElementalStatType()` on the same scale.

The three u32 values follow Garmoth's Black Shrine guide (section "Black
Shrine Auras"): "Investing a light orb increases attack power (AP) by 50 and
defense power (DP) by 100 for that attribute/aura each time you invest one,
and it grants you 3 additional stat points." The three numbers are distinct
and sit in that order in every row, so `ap_per_orb`, `dp_per_orb` and
`stat_points_per_orb` take them in file order.

## Notes

- The file is the same 46 bytes on clients 2519, 3002, 3251 and 3474.
- The Black Shrine window reads per aura `ToClient_GetElementVaryPontCount(type)`,
  `ToClient_GetElementPointStat(type)` (`_fixedPoint`, `_addedPoint`,
  `_offencePoint`, `_defencePoint`) and `ToClient_GetCaculateOffenceStat(type)`
  / `ToClient_GetCaculateDffenceStat(type)`, and the global
  `ToClient_GetMaxElementPoint()` and `ToClient_GetRemainElementPoint()`. It
  shows `(fixedPoint + addedPoint) * ToClient_GetElementVaryPontCount(type)`
  as the aura's Additional Stats, and caps the Light Orb row of one aura at
  10 (`_elementStatMax`, a Lua constant). None of these reads a field of
  this file by name.
- The Light Orb is item `66667`. The tooltip `LUA_MORNING_ATTRBOSS_TOOLTIP_9`
  says "Gain additional AP and DP stats depending on the number of activated
  auras".
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`, one row per aura.
- The server Blessings of the Sun, Moon and Earth that a defeated boss
  gives are in [`elementalserverbuff.bss`](elementalserverbuff_bss.md).
- The weak aura of each boss is the `element_type` of
  [`elementalmonsterstat.bss`](elementalmonsterstat_bss.md), on the same
  scale; its ranking rewards are in
  [`elementalmonsterreward.bss`](elementalmonsterreward_bss.md).
