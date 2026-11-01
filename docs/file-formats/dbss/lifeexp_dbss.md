# `lifeexp.dbss` Format

## Purpose

EXP tables of the life skills (Gathering, Fishing, Hunting, Cooking, Alchemy, Processing, Training, Trading, Farming, Sailing, Barter and four spare slots). Each row gives the EXP one life skill needs to go from one level to the next, from level 0 to the max level. Companion `lifeexpoffset.dbss` lists where every row sits, and [lifeexpmaxlevel](../bss/lifeexpmaxlevel_bss.md) holds the max level per life skill. The client shows a level as a rank and a number (`Guru 12` is level 92), see Rank Groups.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes  | Records                           | Row bytes |
| ------ | -------------- | -------------------- | ------ | --------------------------------- | --------- |
| 1      | 1280 and later | `lifeexp.dbss`       | 35,359 | 2,715 Level Row, 15 Block         | 13        |
| 1      | 1280 and later | `lifeexpoffset.dbss` | 32,644 | 2,715 Offset Row, 15 Offset Block | 12        |

| Layout | File                 | Known             | Unknown    |
| ------ | -------------------- | ----------------- | ---------- |
| 1      | `lifeexp.dbss`       | 35,359 B (100.0%) | 0 B (0.0%) |
| 1      | `lifeexpoffset.dbss` | 32,644 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d4cf0365a3ab`  |
| 3482   | Layout 1 | `d4cf0365a3ab`  |
| 3474   | Layout 1 | `d4cf0365a3ab`  |
| 3473   | Layout 1 | `d4cf0365a3ab`  |
| 3464   | Layout 1 | `d4cf0365a3ab`  |
| 3458   | Layout 1 | `d4cf0365a3ab`  |
| 3454   | Layout 1 | `d4cf0365a3ab`  |
| 3444   | Layout 1 | `d4cf0365a3ab`  |
| 3435   | Layout 1 | `d4cf0365a3ab`  |
| 3426   | Layout 1 | `d4cf0365a3ab`  |
| 3418   | Layout 1 | `d4cf0365a3ab`  |
| 3412   | Layout 1 | `d4cf0365a3ab`  |
| 3402   | Layout 1 | `d4cf0365a3ab`  |
| 3396   | Layout 1 | `d4cf0365a3ab`  |
| 3387   | Layout 1 | `d4cf0365a3ab`  |
| 3381   | Layout 1 | `d4cf0365a3ab`  |
| 3373   | Layout 1 | `d4cf0365a3ab`  |
| 3364   | Layout 1 | `d4cf0365a3ab`  |
| 3356   | Layout 1 | `d4cf0365a3ab`  |
| 3349   | Layout 1 | `d4cf0365a3ab`  |
| 3342   | Layout 1 | `d4cf0365a3ab`  |
| 3335   | Layout 1 | `d4cf0365a3ab`  |
| 3326   | Layout 1 | `d4cf0365a3ab`  |
| 3321   | Layout 1 | `d4cf0365a3ab`  |
| 3314   | Layout 1 | `d4cf0365a3ab`  |
| 3303   | Layout 1 | `d4cf0365a3ab`  |
| 3302   | Layout 1 | `d4cf0365a3ab`  |
| 3293   | Layout 1 | `d4cf0365a3ab`  |
| 3283   | Layout 1 | `d4cf0365a3ab`  |
| 3275   | Layout 1 | `d4cf0365a3ab`  |
| 3267   | Layout 1 | `d4cf0365a3ab`  |
| 3258   | Layout 1 | `d4cf0365a3ab`  |
| 3251   | Layout 1 | `d4cf0365a3ab`  |
| 3242   | Layout 1 | `d4cf0365a3ab`  |
| 3235   | Layout 1 | `d4cf0365a3ab`  |
| 3229   | Layout 1 | `d4cf0365a3ab`  |
| 3212   | Layout 1 | `d4cf0365a3ab`  |
| 3203   | Layout 1 | `d4cf0365a3ab`  |
| 3193   | Layout 1 | `d4cf0365a3ab`  |
| 3186   | Layout 1 | `d4cf0365a3ab`  |
| 3177   | Layout 1 | `d4cf0365a3ab`  |
| 3169   | Layout 1 | `d4cf0365a3ab`  |
| 3158   | Layout 1 | `d4cf0365a3ab`  |
| 3151   | Layout 1 | `d4cf0365a3ab`  |
| 3144   | Layout 1 | `d4cf0365a3ab`  |
| 3133   | Layout 1 | `d4cf0365a3ab`  |
| 3125   | Layout 1 | `d4cf0365a3ab`  |
| 3118   | Layout 1 | `d4cf0365a3ab`  |
| 3111   | Layout 1 | `d4cf0365a3ab`  |
| 3103   | Layout 1 | `d4cf0365a3ab`  |
| 3095   | Layout 1 | `d4cf0365a3ab`  |
| 3086   | Layout 1 | `d4cf0365a3ab`  |
| 3072   | Layout 1 | `d4cf0365a3ab`  |
| 3062   | Layout 1 | `d4cf0365a3ab`  |
| 3052   | Layout 1 | `d4cf0365a3ab`  |
| 3045   | Layout 1 | `d4cf0365a3ab`  |
| 3037   | Layout 1 | `d4cf0365a3ab`  |
| 3030   | Layout 1 | `d4cf0365a3ab`  |
| 3021   | Layout 1 | `d4cf0365a3ab`  |
| 3012   | Layout 1 | `d4cf0365a3ab`  |
| 3002   | Layout 1 | `d4cf0365a3ab`  |
| 2995   | Layout 1 | `d4cf0365a3ab`  |
| 2987   | Layout 1 | `d4cf0365a3ab`  |
| 2978   | Layout 1 | `d4cf0365a3ab`  |
| 2970   | Layout 1 | `d4cf0365a3ab`  |
| 2959   | Layout 1 | `d4cf0365a3ab`  |
| 2951   | Layout 1 | `d4cf0365a3ab`  |
| 2942   | Layout 1 | `d4cf0365a3ab`  |
| 2935   | Layout 1 | `d4cf0365a3ab`  |
| 2932   | Layout 1 | `d4cf0365a3ab`  |
| 2923   | Layout 1 | `d4cf0365a3ab`  |
| 2919   | Layout 1 | `d4cf0365a3ab`  |
| 2907   | Layout 1 | `d4cf0365a3ab`  |
| 2900   | Layout 1 | `d4cf0365a3ab`  |
| 2891   | Layout 1 | `d4cf0365a3ab`  |
| 2882   | Layout 1 | `d4cf0365a3ab`  |
| 2872   | Layout 1 | `d4cf0365a3ab`  |
| 2863   | Layout 1 | `d4cf0365a3ab`  |
| 2855   | Layout 1 | `d4cf0365a3ab`  |
| 2849   | Layout 1 | `d4cf0365a3ab`  |
| 2844   | Layout 1 | `d4cf0365a3ab`  |
| 2834   | Layout 1 | `d4cf0365a3ab`  |
| 2825   | Layout 1 | `d4cf0365a3ab`  |
| 2819   | Layout 1 | `d4cf0365a3ab`  |
| 2811   | Layout 1 | `d4cf0365a3ab`  |
| 2803   | Layout 1 | `d4cf0365a3ab`  |
| 2794   | Layout 1 | `d4cf0365a3ab`  |
| 2783   | Layout 1 | `d4cf0365a3ab`  |
| 2774   | Layout 1 | `d4cf0365a3ab`  |
| 2765   | Layout 1 | `d4cf0365a3ab`  |
| 2756   | Layout 1 | `d4cf0365a3ab`  |
| 2750   | Layout 1 | `d4cf0365a3ab`  |
| 2743   | Layout 1 | `d4cf0365a3ab`  |
| 2736   | Layout 1 | `d4cf0365a3ab`  |
| 2726   | Layout 1 | `d4cf0365a3ab`  |
| 2717   | Layout 1 | `d4cf0365a3ab`  |
| 2709   | Layout 1 | `d4cf0365a3ab`  |
| 2703   | Layout 1 | `d4cf0365a3ab`  |
| 2695   | Layout 1 | `d4cf0365a3ab`  |
| 2684   | Layout 1 | `d4cf0365a3ab`  |
| 2672   | Layout 1 | `d4cf0365a3ab`  |
| 2665   | Layout 1 | `d4cf0365a3ab`  |
| 2657   | Layout 1 | `d4cf0365a3ab`  |
| 2649   | Layout 1 | `d4cf0365a3ab`  |
| 2644   | Layout 1 | `d4cf0365a3ab`  |
| 2637   | Layout 1 | `d4cf0365a3ab`  |
| 2629   | Layout 1 | `d4cf0365a3ab`  |
| 2619   | Layout 1 | `d4cf0365a3ab`  |
| 2612   | Layout 1 | `d4cf0365a3ab`  |
| 2606   | Layout 1 | `d4cf0365a3ab`  |
| 2602   | Layout 1 | `d4cf0365a3ab`  |
| 2601   | Layout 1 | `d4cf0365a3ab`  |
| 2592   | Layout 1 | `d4cf0365a3ab`  |
| 2583   | Layout 1 | `d4cf0365a3ab`  |
| 2575   | Layout 1 | `d4cf0365a3ab`  |
| 2567   | Layout 1 | `d4cf0365a3ab`  |
| 2560   | Layout 1 | `d4cf0365a3ab`  |
| 2553   | Layout 1 | `d4cf0365a3ab`  |
| 2545   | Layout 1 | `d4cf0365a3ab`  |
| 2538   | Layout 1 | `d4cf0365a3ab`  |
| 2529   | Layout 1 | `d4cf0365a3ab`  |
| 2519   | Layout 1 | `d4cf0365a3ab`  |
| 2513   | Layout 1 | `d4cf0365a3ab`  |
| 2510   | Layout 1 | `d4cf0365a3ab`  |
| 2507   | Layout 1 | `d4cf0365a3ab`  |
| 2503   | Layout 1 | `d4cf0365a3ab`  |
| 2498   | Layout 1 | `d4cf0365a3ab`  |
| 2492   | Layout 1 | `d4cf0365a3ab`  |
| 2487   | Layout 1 | `d4cf0365a3ab`  |
| 2480   | Layout 1 | `d4cf0365a3ab`  |
| 2474   | Layout 1 | `d4cf0365a3ab`  |
| 2468   | Layout 1 | `d4cf0365a3ab`  |
| 2460   | Layout 1 | `d4cf0365a3ab`  |
| 2453   | Layout 1 | `d4cf0365a3ab`  |
| 2444   | Layout 1 | `d4cf0365a3ab`  |
| 2438   | Layout 1 | `d4cf0365a3ab`  |
| 2434   | Layout 1 | `d4cf0365a3ab`  |
| 2429   | Layout 1 | `d4cf0365a3ab`  |
| 2421   | Layout 1 | `d4cf0365a3ab`  |
| 2414   | Layout 1 | `d4cf0365a3ab`  |
| 2407   | Layout 1 | `d4cf0365a3ab`  |
| 2401   | Layout 1 | `d4cf0365a3ab`  |
| 2397   | Layout 1 | `d4cf0365a3ab`  |
| 2393   | Layout 1 | `d4cf0365a3ab`  |
| 2384   | Layout 1 | `d4cf0365a3ab`  |
| 2378   | Layout 1 | `d4cf0365a3ab`  |
| 2372   | Layout 1 | `d4cf0365a3ab`  |
| 2358   | Layout 1 | `d4cf0365a3ab`  |
| 2352   | Layout 1 | `d4cf0365a3ab`  |
| 2347   | Layout 1 | `d4cf0365a3ab`  |
| 2343   | Layout 1 | `d4cf0365a3ab`  |
| 2335   | Layout 1 | `d4cf0365a3ab`  |
| 2327   | Layout 1 | `d4cf0365a3ab`  |
| 2324   | Layout 1 | `d4cf0365a3ab`  |
| 2319   | Layout 1 | `d4cf0365a3ab`  |
| 2313   | Layout 1 | `d4cf0365a3ab`  |
| 2308   | Layout 1 | `d4cf0365a3ab`  |
| 2302   | Layout 1 | `d4cf0365a3ab`  |
| 2295   | Layout 1 | `d4cf0365a3ab`  |
| 2290   | Layout 1 | `d4cf0365a3ab`  |
| 2284   | Layout 1 | `d4cf0365a3ab`  |
| 2276   | Layout 1 | `d4cf0365a3ab`  |
| 2269   | Layout 1 | `d4cf0365a3ab`  |
| 2259   | Layout 1 | `d4cf0365a3ab`  |
| 2250   | Layout 1 | `d4cf0365a3ab`  |
| 2243   | Layout 1 | `d4cf0365a3ab`  |
| 2235   | Layout 1 | `d4cf0365a3ab`  |
| 2229   | Layout 1 | `d4cf0365a3ab`  |
| 2224   | Layout 1 | `d4cf0365a3ab`  |
| 2218   | Layout 1 | `d4cf0365a3ab`  |
| 2215   | Layout 1 | `d4cf0365a3ab`  |
| 2207   | Layout 1 | `d4cf0365a3ab`  |
| 2203   | Layout 1 | `d4cf0365a3ab`  |
| 2196   | Layout 1 | `d4cf0365a3ab`  |
| 2192   | Layout 1 | `d4cf0365a3ab`  |
| 2189   | Layout 1 | `d4cf0365a3ab`  |
| 2183   | Layout 1 | `d4cf0365a3ab`  |
| 2179   | Layout 1 | `d4cf0365a3ab`  |
| 2171   | Layout 1 | `d4cf0365a3ab`  |
| 2163   | Layout 1 | `d4cf0365a3ab`  |
| 2156   | Layout 1 | `d4cf0365a3ab`  |
| 2151   | Layout 1 | `d4cf0365a3ab`  |
| 2147   | Layout 1 | `d4cf0365a3ab`  |
| 2142   | Layout 1 | `d4cf0365a3ab`  |
| 2138   | Layout 1 | `d4cf0365a3ab`  |
| 2134   | Layout 1 | `d4cf0365a3ab`  |
| 2130   | Layout 1 | `d4cf0365a3ab`  |
| 2122   | Layout 1 | `d4cf0365a3ab`  |
| 2107   | Layout 1 | `d4cf0365a3ab`  |
| 2098   | Layout 1 | `d4cf0365a3ab`  |
| 2089   | Layout 1 | `d4cf0365a3ab`  |
| 2081   | Layout 1 | `d4cf0365a3ab`  |
| 2073   | Layout 1 | `d4cf0365a3ab`  |
| 2067   | Layout 1 | `d4cf0365a3ab`  |
| 2063   | Layout 1 | `d4cf0365a3ab`  |
| 2059   | Layout 1 | `d4cf0365a3ab`  |
| 2052   | Layout 1 | `d4cf0365a3ab`  |
| 2044   | Layout 1 | `d4cf0365a3ab`  |
| 2039   | Layout 1 | `d4cf0365a3ab`  |
| 2032   | Layout 1 | `d4cf0365a3ab`  |
| 2025   | Layout 1 | `d4cf0365a3ab`  |
| 2011   | Layout 1 | `d4cf0365a3ab`  |
| 2005   | Layout 1 | `d4cf0365a3ab`  |
| 2000   | Layout 1 | `d4cf0365a3ab`  |
| 1996   | Layout 1 | `d4cf0365a3ab`  |
| 1991   | Layout 1 | `d4cf0365a3ab`  |
| 1985   | Layout 1 | `d4cf0365a3ab`  |
| 1980   | Layout 1 | `d4cf0365a3ab`  |
| 1969   | Layout 1 | `d4cf0365a3ab`  |
| 1964   | Layout 1 | `d4cf0365a3ab`  |
| 1958   | Layout 1 | `d4cf0365a3ab`  |
| 1950   | Layout 1 | `d4cf0365a3ab`  |
| 1945   | Layout 1 | `d4cf0365a3ab`  |
| 1937   | Layout 1 | `d4cf0365a3ab`  |
| 1933   | Layout 1 | `d4cf0365a3ab`  |
| 1927   | Layout 1 | `d4cf0365a3ab`  |
| 1921   | Layout 1 | `d4cf0365a3ab`  |
| 1914   | Layout 1 | `d4cf0365a3ab`  |
| 1908   | Layout 1 | `d4cf0365a3ab`  |
| 1897   | Layout 1 | `d4cf0365a3ab`  |
| 1892   | Layout 1 | `d4cf0365a3ab`  |
| 1886   | Layout 1 | `d4cf0365a3ab`  |
| 1881   | Layout 1 | `d4cf0365a3ab`  |
| 1871   | Layout 1 | `d4cf0365a3ab`  |
| 1866   | Layout 1 | `d4cf0365a3ab`  |
| 1862   | Layout 1 | `d4cf0365a3ab`  |
| 1854   | Layout 1 | `d4cf0365a3ab`  |
| 1846   | Layout 1 | `d4cf0365a3ab`  |
| 1838   | Layout 1 | `d4cf0365a3ab`  |
| 1832   | Layout 1 | `d4cf0365a3ab`  |
| 1826   | Layout 1 | `d4cf0365a3ab`  |
| 1822   | Layout 1 | `d4cf0365a3ab`  |
| 1818   | Layout 1 | `d4cf0365a3ab`  |
| 1804   | Layout 1 | `d4cf0365a3ab`  |
| 1794   | Layout 1 | `d4cf0365a3ab`  |
| 1790   | Layout 1 | `d4cf0365a3ab`  |
| 1784   | Layout 1 | `d4cf0365a3ab`  |
| 1774   | Layout 1 | `d4cf0365a3ab`  |
| 1771   | Layout 1 | `d4cf0365a3ab`  |
| 1762   | Layout 1 | `d4cf0365a3ab`  |
| 1759   | Layout 1 | `d4cf0365a3ab`  |
| 1754   | Layout 1 | `d4cf0365a3ab`  |
| 1749   | Layout 1 | `d4cf0365a3ab`  |
| 1743   | Layout 1 | `d4cf0365a3ab`  |
| 1737   | Layout 1 | `d4cf0365a3ab`  |
| 1731   | Layout 1 | `d4cf0365a3ab`  |
| 1725   | Layout 1 | `d4cf0365a3ab`  |
| 1717   | Layout 1 | `d4cf0365a3ab`  |
| 1710   | Layout 1 | `d4cf0365a3ab`  |
| 1704   | Layout 1 | `d4cf0365a3ab`  |
| 1698   | Layout 1 | `d4cf0365a3ab`  |
| 1690   | Layout 1 | `d4cf0365a3ab`  |
| 1685   | Layout 1 | `d4cf0365a3ab`  |
| 1680   | Layout 1 | `d4cf0365a3ab`  |
| 1674   | Layout 1 | `d4cf0365a3ab`  |
| 1668   | Layout 1 | `d4cf0365a3ab`  |
| 1659   | Layout 1 | `d4cf0365a3ab`  |
| 1649   | Layout 1 | `d4cf0365a3ab`  |
| 1642   | Layout 1 | `d4cf0365a3ab`  |
| 1636   | Layout 1 | `d4cf0365a3ab`  |
| 1628   | Layout 1 | `d4cf0365a3ab`  |
| 1622   | Layout 1 | `d4cf0365a3ab`  |
| 1614   | Layout 1 | `d4cf0365a3ab`  |
| 1608   | Layout 1 | `d4cf0365a3ab`  |
| 1602   | Layout 1 | `d4cf0365a3ab`  |
| 1598   | Layout 1 | `d4cf0365a3ab`  |
| 1594   | Layout 1 | `d4cf0365a3ab`  |
| 1590   | Layout 1 | `d4cf0365a3ab`  |
| 1587   | Layout 1 | `d4cf0365a3ab`  |
| 1584   | Layout 1 | `d4cf0365a3ab`  |
| 1579   | Layout 1 | `d4cf0365a3ab`  |
| 1572   | Layout 1 | `d4cf0365a3ab`  |
| 1565   | Layout 1 | `d4cf0365a3ab`  |
| 1559   | Layout 1 | `d4cf0365a3ab`  |
| 1554   | Layout 1 | `d4cf0365a3ab`  |
| 1547   | Layout 1 | `d4cf0365a3ab`  |
| 1537   | Layout 1 | `d4cf0365a3ab`  |
| 1529   | Layout 1 | `d4cf0365a3ab`  |
| 1524   | Layout 1 | `d4cf0365a3ab`  |
| 1519   | Layout 1 | `d4cf0365a3ab`  |
| 1509   | Layout 1 | `d4cf0365a3ab`  |
| 1506   | Layout 1 | `d4cf0365a3ab`  |
| 1504   | Layout 1 | `d4cf0365a3ab`  |
| 1500   | Layout 1 | `d4cf0365a3ab`  |
| 1493   | Layout 1 | `d4cf0365a3ab`  |
| 1489   | Layout 1 | `d4cf0365a3ab`  |
| 1485   | Layout 1 | `d4cf0365a3ab`  |
| 1481   | Layout 1 | `d4cf0365a3ab`  |
| 1474   | Layout 1 | `d4cf0365a3ab`  |
| 1466   | Layout 1 | `d4cf0365a3ab`  |
| 1462   | Layout 1 | `d4cf0365a3ab`  |
| 1459   | Layout 1 | `d4cf0365a3ab`  |
| 1453   | Layout 1 | `d4cf0365a3ab`  |
| 1450   | Layout 1 | `d4cf0365a3ab`  |
| 1445   | Layout 1 | `d4cf0365a3ab`  |
| 1439   | Layout 1 | `d4cf0365a3ab`  |
| 1433   | Layout 1 | `d4cf0365a3ab`  |
| 1430   | Layout 1 | `d4cf0365a3ab`  |
| 1426   | Layout 1 | `d4cf0365a3ab`  |
| 1421   | Layout 1 | `d4cf0365a3ab`  |
| 1417   | Layout 1 | `d4cf0365a3ab`  |
| 1416   | Layout 1 | `d4cf0365a3ab`  |
| 1409   | Layout 1 | `d4cf0365a3ab`  |
| 1405   | Layout 1 | `d4cf0365a3ab`  |
| 1401   | Layout 1 | `d4cf0365a3ab`  |
| 1396   | Layout 1 | `d4cf0365a3ab`  |
| 1391   | Layout 1 | `d4cf0365a3ab`  |
| 1390   | Layout 1 | `d4cf0365a3ab`  |
| 1386   | Layout 1 | `d4cf0365a3ab`  |
| 1381   | Layout 1 | `d4cf0365a3ab`  |
| 1379   | Layout 1 | `d4cf0365a3ab`  |
| 1372   | Layout 1 | `d4cf0365a3ab`  |
| 1366   | Layout 1 | `d4cf0365a3ab`  |
| 1364   | Layout 1 | `d4cf0365a3ab`  |
| 1363   | Layout 1 | `d4cf0365a3ab`  |
| 1360   | Layout 1 | `d4cf0365a3ab`  |
| 1358   | Layout 1 | `d4cf0365a3ab`  |
| 1355   | Layout 1 | `d4cf0365a3ab`  |
| 1351   | Layout 1 | `d4cf0365a3ab`  |
| 1348   | Layout 1 | `d4cf0365a3ab`  |
| 1346   | Layout 1 | `d4cf0365a3ab`  |
| 1341   | Layout 1 | `d4cf0365a3ab`  |
| 1340   | Layout 1 | `d4cf0365a3ab`  |
| 1338   | Layout 1 | `d4cf0365a3ab`  |
| 1335   | Layout 1 | `d4cf0365a3ab`  |
| 1333   | Layout 1 | `d4cf0365a3ab`  |
| 1329   | Layout 1 | `d4cf0365a3ab`  |
| 1327   | Layout 1 | `d4cf0365a3ab`  |
| 1324   | Layout 1 | `d4cf0365a3ab`  |
| 1321   | Layout 1 | `d4cf0365a3ab`  |
| 1319   | Layout 1 | `d4cf0365a3ab`  |
| 1318   | Layout 1 | `d4cf0365a3ab`  |
| 1316   | Layout 1 | `d4cf0365a3ab`  |
| 1313   | Layout 1 | `d4cf0365a3ab`  |
| 1311   | Layout 1 | `d4cf0365a3ab`  |
| 1309   | Layout 1 | `d4cf0365a3ab`  |
| 1304   | Layout 1 | `d4cf0365a3ab`  |
| 1292   | Layout 1 | `d4cf0365a3ab`  |
| 1286   | Layout 1 | `d4cf0365a3ab`  |
| 1280   | Layout 1 | `d4cf0365a3ab`  |
| 1276   | No file  | `d4cf0365a3ab`  |
| 1267   | No file  | `d4cf0365a3ab`  |
| 1261   | No file  | `d4cf0365a3ab`  |
| 1256   | No file  | `d4cf0365a3ab`  |
| 1250   | No file  | `d4cf0365a3ab`  |
| 1246   | No file  | `d4cf0365a3ab`  |
| 1239   | No file  | `d4cf0365a3ab`  |
| 1230   | No file  | `d4cf0365a3ab`  |
| 1226   | No file  | `d4cf0365a3ab`  |
| 1220   | No file  | `d4cf0365a3ab`  |
| 1217   | No file  | `d4cf0365a3ab`  |
| 1211   | No file  | `d4cf0365a3ab`  |
| 1210   | No file  | `d4cf0365a3ab`  |
| 1208   | No file  | `d4cf0365a3ab`  |
| 1203   | No file  | `d4cf0365a3ab`  |
| 1197   | No file  | `d4cf0365a3ab`  |
| 1194   | No file  | `d4cf0365a3ab`  |
| 1192   | No file  | `d4cf0365a3ab`  |
| 1187   | No file  | `d4cf0365a3ab`  |
| 1183   | No file  | `d4cf0365a3ab`  |
| 1177   | No file  | `d4cf0365a3ab`  |
| 1173   | No file  | `d4cf0365a3ab`  |
| 1167   | No file  | `d4cf0365a3ab`  |
| 1164   | No file  | `d4cf0365a3ab`  |
| 1156   | No file  | `d4cf0365a3ab`  |
| 1149   | No file  | `d4cf0365a3ab`  |
| 1144   | No file  | `d4cf0365a3ab`  |
| 1137   | No file  | `d4cf0365a3ab`  |
| 1132   | No file  | `d4cf0365a3ab`  |
| 1127   | No file  | `d4cf0365a3ab`  |
| 1122   | No file  | `d4cf0365a3ab`  |
| 1118   | No file  | `d4cf0365a3ab`  |
| 1114   | No file  | `d4cf0365a3ab`  |
| 1109   | No file  | `d4cf0365a3ab`  |
| 1102   | No file  | `d4cf0365a3ab`  |
| 1096   | No file  | `d4cf0365a3ab`  |
| 1088   | No file  | `d4cf0365a3ab`  |
| 1081   | No file  | `d4cf0365a3ab`  |
| 1076   | No file  | `d4cf0365a3ab`  |
| 1069   | No file  | `d4cf0365a3ab`  |
| 1064   | No file  | `d4cf0365a3ab`  |
| 1058   | No file  | `d4cf0365a3ab`  |
| 1051   | No file  | `d4cf0365a3ab`  |
| 1044   | No file  | `d4cf0365a3ab`  |
| 1036   | No file  | `d4cf0365a3ab`  |
| 1026   | No file  | `d4cf0365a3ab`  |
| 1016   | No file  | `d4cf0365a3ab`  |
| 1009   | No file  | `d4cf0365a3ab`  |
| 1005   | No file  | `d4cf0365a3ab`  |
| 1000   | No file  | `d4cf0365a3ab`  |
| 998    | No file  | `d4cf0365a3ab`  |
| 990    | No file  | `d4cf0365a3ab`  |
| 979    | No file  | `d4cf0365a3ab`  |
| 972    | No file  | `d4cf0365a3ab`  |
| 963    | No file  | `d4cf0365a3ab`  |
| 955    | No file  | `d4cf0365a3ab`  |
| 946    | No file  | `d4cf0365a3ab`  |
| 938    | No file  | `d4cf0365a3ab`  |
| 927    | No file  | `d4cf0365a3ab`  |
| 911    | No file  | `d4cf0365a3ab`  |
| 904    | No file  | `d4cf0365a3ab`  |
| 899    | No file  | `d4cf0365a3ab`  |
| 894    | No file  | `d4cf0365a3ab`  |
| 885    | No file  | `d4cf0365a3ab`  |
| 879    | No file  | `d4cf0365a3ab`  |
| 872    | No file  | `d4cf0365a3ab`  |
| 864    | No file  | `d4cf0365a3ab`  |
| 855    | No file  | `d4cf0365a3ab`  |
| 853    | No file  | `d4cf0365a3ab`  |
| 845    | No file  | `d4cf0365a3ab`  |
| 837    | No file  | `d4cf0365a3ab`  |
| 829    | No file  | `d4cf0365a3ab`  |
| 822    | No file  | `d4cf0365a3ab`  |
| 814    | No file  | `d4cf0365a3ab`  |
| 805    | No file  | `d4cf0365a3ab`  |
| 794    | No file  | `d4cf0365a3ab`  |
| 787    | No file  | `d4cf0365a3ab`  |
| 780    | No file  | `d4cf0365a3ab`  |
| 771    | No file  | `d4cf0365a3ab`  |
| 760    | No file  | `d4cf0365a3ab`  |
| 748    | No file  | `d4cf0365a3ab`  |
| 741    | No file  | `d4cf0365a3ab`  |
| 736    | No file  | `d4cf0365a3ab`  |
| 731    | No file  | `d4cf0365a3ab`  |
| 723    | No file  | `d4cf0365a3ab`  |
| 711    | No file  | `d4cf0365a3ab`  |
| 707    | No file  | `d4cf0365a3ab`  |
| 697    | No file  | `d4cf0365a3ab`  |
| 689    | No file  | `d4cf0365a3ab`  |
| 683    | No file  | `d4cf0365a3ab`  |
| 678    | No file  | `d4cf0365a3ab`  |
| 670    | No file  | `d4cf0365a3ab`  |
| 661    | No file  | `d4cf0365a3ab`  |
| 656    | No file  | `d4cf0365a3ab`  |
| 652    | No file  | `d4cf0365a3ab`  |
| 643    | No file  | `d4cf0365a3ab`  |
| 637    | No file  | `d4cf0365a3ab`  |
| 630    | No file  | `d4cf0365a3ab`  |
| 627    | No file  | `d4cf0365a3ab`  |
| 621    | No file  | `d4cf0365a3ab`  |
| 617    | No file  | `d4cf0365a3ab`  |
| 615    | No file  | `d4cf0365a3ab`  |
| 606    | No file  | `d4cf0365a3ab`  |
| 599    | No file  | `d4cf0365a3ab`  |
| 592    | No file  | `d4cf0365a3ab`  |
| 586    | No file  | `d4cf0365a3ab`  |
| 577    | No file  | `d4cf0365a3ab`  |
| 569    | No file  | `d4cf0365a3ab`  |
| 561    | No file  | `d4cf0365a3ab`  |
| 554    | No file  | `d4cf0365a3ab`  |
| 542    | No file  | `d4cf0365a3ab`  |
| 532    | No file  | `d4cf0365a3ab`  |
| 531    | No file  | `d4cf0365a3ab`  |
| 526    | No file  | `d4cf0365a3ab`  |
| 521    | No file  | `d4cf0365a3ab`  |
| 517    | No file  | `d4cf0365a3ab`  |
| 510    | No file  | `d4cf0365a3ab`  |
| 508    | No file  | `d4cf0365a3ab`  |
| 504    | No file  | `d4cf0365a3ab`  |
| 497    | No file  | `d4cf0365a3ab`  |
| 491    | No file  | `d4cf0365a3ab`  |
| 485    | No file  | `d4cf0365a3ab`  |
| 478    | No file  | `d4cf0365a3ab`  |
| 472    | No file  | `d4cf0365a3ab`  |
| 466    | No file  | `d4cf0365a3ab`  |
| 457    | No file  | `d4cf0365a3ab`  |
| 452    | No file  | `d4cf0365a3ab`  |
| 449    | No file  | `d4cf0365a3ab`  |
| 435    | No file  | `d4cf0365a3ab`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                    |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| `lifeexpoffset.dbss`  | Required | `(life skill, level) -> (offset, size)` of every row                    |
| `lifeexpmaxlevel.bss` | Optional | Max level per life skill, see [lifeexpmaxlevel](../bss/lifeexpmaxlevel_bss.md) |
| `stringtable.bss`     | Optional | Hashes of the `GAME` sheet keys that name the life skills and ranks     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field       | Notes                                                    |
| ------- | ------------------ | ----------- | -------------------------------------------------------- |
| `+0x00` | u32                | skill_count | Number of life skill blocks; 15 on client 3464, the client's `Type_Count` |
| `+0x04` | Block[skill_count] | blocks      | One per life skill in ID order; see Block                |

### Block (variable: 4 bytes + rows)

| Offset  | Type                   | Field       | Notes                                                        |
| ------- | ---------------------- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u32                    | level_count | Rows in this block; 181 (levels 0 to 180) on client 3464     |
| `+0x04` | Level Row[level_count] | rows        | See Level Row                                                |

The blocks fill the file exactly: 4 + 15 x (4 + 181 x 13) = 35,359 bytes on client 3464.

### Level Row (13 bytes)

| Offset  | Type | Field      | Notes                                                       |
| ------- | ---- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u8   | life_skill | Life skill ID, see Life Skills; equals the block index      |
| `+0x01` | u32  | level      | `0` to the max level, ascending inside a block               |
| `+0x05` | u64  | exp        | EXP to go from `level` to `level + 1`, the demand the client's EXP bar divides by (Notes) |

### `lifeexpoffset.dbss`

Index into `lifeexp.dbss`, with the same block shape as the main file, including the leading skill count.

| Offset  | Type                      | Field       | Notes                                 |
| ------- | ------------------------- | ----------- | ------------------------------------- |
| `+0x00` | u32                       | skill_count | Equals the `lifeexp.dbss` skill count |
| `+0x04` | Offset Block[skill_count] | blocks      | See Offset Block                      |

### Offset Block (variable: 4 bytes + rows)

| Offset  | Type                    | Field       | Notes                                   |
| ------- | ----------------------- | ----------- | --------------------------------------- |
| `+0x00` | u32                     | level_count | Rows in this block (181 on client 3464) |
| `+0x04` | Offset Row[level_count] | rows        | See Offset Row                          |

The block index is the life skill; the file stores no life skill field. 4 + 15 x (4 + 181 x 12) = 32,644 bytes on client 3464.

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                           |
| ------- | ---- | ----------- | --------------------------------------------------------------- |
| `+0x00` | u32  | level       | Level of the row it points at                                   |
| `+0x04` | u32  | data_offset | Absolute byte offset of the 13-byte row in `lifeexp.dbss`       |
| `+0x08` | u32  | data_size   | Always 13                                                       |

The first Gathering row sits at `0x08`, after the skill count and Gathering's level count; each later block starts 4 bytes past the previous block's last row. The parser reads the main file through these rows and checks that each row's `life_skill` and `level` match the offset row's block and key.

## Enum Values

### Life Skills

The IDs and names come from `global_define_cpp_enum.luac`: `CppEnums.LifeExperienceType` numbers the life skills and `CppEnums.LifeExperienceString` names each one with a `GAME` sheet key. The English column is the LOC type 37 text of that key. The order matches the life skill parameter of buff effect types 80 and 149 in [buff](buff_dbss.md).

| ID  | Enum          | Name key                            | English    |
| --- | ------------- | ----------------------------------- | ---------- |
| 0   | `gather`      | `LUA_SELFCHARACTERINFO_GATHER`      | Gathering  |
| 1   | `fishing`     | `LUA_SELFCHARACTERINFO_FISH`        | Fishing    |
| 2   | `hunting`     | `LUA_SELFCHARACTERINFO_HUNT`        | Hunting    |
| 3   | `cooking`     | `LUA_SELFCHARACTERINFO_COOK`        | Cooking    |
| 4   | `alchemy`     | `LUA_SELFCHARACTERINFO_ALCHEMY`     | Alchemy    |
| 5   | `manufacture` | `LUA_SELFCHARACTERINFO_MANUFACTURE` | Processing |
| 6   | `training`    | `LUA_SELFCHARACTERINFO_OBEDIENCE`   | Training   |
| 7   | `trade`       | `LUA_SELFCHARACTERINFO_TRADE`       | Trading    |
| 8   | `growth`      | `LUA_SELFCHARACTERINFO_GROWTH`      | Farming    |
| 9   | `sail`        | `LUA_SELFCHARACTERINFO_SAIL`        | Sailing    |
| 10  | `temp1`       | none, Korean `예비1` ("spare 1")    |            |
| 11  | `barter`      | `LUA_SELFCHARACTERINFO_BARTER`      | Barter     |
| 12  | `temp2`       | none, Korean `예비2`                |            |
| 13  | `temp3`       | none, Korean `예비3`                |            |
| 14  | `temp4`       | none, Korean `예비4`                |            |

The handlers show the spare slots by their enum name.

### Rank Groups

`PaGlobalFunc_Util_CraftLevelReplace` in `global_util.luac` turns a level into the rank text: the group key's LOC text, then the level minus the levels of the groups below it. `panel_transferlifeexperience_all.luac` shows life skill levels with the same keys.

| Levels    | Key                                    | English      | Shown as                    |
| --------- | -------------------------------------- | ------------ | --------------------------- |
| 1 to 10   | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_1` | Beginner     | Beginner 1 to Beginner 10   |
| 11 to 20  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_2` | Apprentice   | Apprentice 1 to 10          |
| 21 to 30  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_3` | Skilled      | Skilled 1 to 10             |
| 31 to 40  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_4` | Professional | Professional 1 to 10        |
| 41 to 50  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_5` | Artisan      | Artisan 1 to 10             |
| 51 to 80  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_6` | Master       | Master 1 to 30              |
| 81 to 180 | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_7` | Guru         | Guru 1 to 100               |

Level 0 has no rank; the Lua function falls through and returns the bare level.

## Notes

- Observed on client 3464: twelve of the fifteen blocks hold the same EXP on every level (IDs 0, 2 to 6, 8 to 10 and 12 to 14). Fishing (1) needs less on levels 1 to 128 (level 1: 200 against 400) and matches them from level 129 up. Barter (11) has its own curve on every level but 0.
- Trading (7) holds finite EXP up to level 60, then `999,999,999,999` on levels 61 to 130 and `9,999,999,999,999` on levels 131 to 180, so Trading stops at Master 11 (level 61), while [lifeexpmaxlevel](../bss/lifeexpmaxlevel_bss.md) still gives it 180. Client 3473 replaced the finite part of the curve: Beginner 1 needs 5 EXP instead of 20, and level 60 (Master 10 to Master 11) 630,643,672,350 instead of 212,980,644 (client 3464). The same client added [tradeexperiencess](../bss/tradeexperiencess_bss.md), whose rows divide the new curve into whole numbers of equal parts.
- The shared curve and Barter both change pace at level 131: Barter rises by about 8,150 EXP per level on levels 125 to 130, then 13% per level from 131 (4,104,606 on 130, 4,638,200 on 131). Trading's second sentinel starts on the same level.
- Every block starts with level 0 at `100` EXP, `20` for Trading.
- The client reads a life skill's level and EXP through `getLifeExperienceLevel`, `getCurrLifeExperiencePoint` and `getDemandLifeExperiencePoint` (`panel_transferlifeexperience_all.luac`) and draws the bar as current / demand, so EXP restarts at 0 on every level.
- The level-up notice (`nakmessage_life.luac`) names the rank groups `__eLifeGrade_Master` and `__eLifeGrade_GURU` in its constants.
- `fitnesslevel.dbss` uses the same block shape with 29-byte rows and is read with the same row direction; see [fitnesslevel](fitnesslevel_dbss.md).
- Row direction, checked 2026-10-09 with a packet capture while gathering at Gathering Master 8 (level 58): the server sends the current EXP in message `0x1C91` (u64 current EXP, u8 life skill, u32 level). It went from 6,601,966 to 6,608,284 while the in-game bar went from 44.41% to 44.45%, which is current EXP divided by the level 58 row (14,865,500: 44.41% to 44.45%), not the level 59 row (15,935,300: 41.43%). So the row of level N is the EXP to go from N to N + 1.
