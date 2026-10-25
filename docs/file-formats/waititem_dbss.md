# `waititem.dbss` Format

## Purpose

The item keys (item plus enhancement level) that the Central Market puts in
its Registration Queue before they appear for sale: PEN Blackstar and boss
gear, TRI to PEN Godr-Ayed weapons, TET and PEN accessories, and every level
of Fallen God's Armor.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records       | Row bytes |
| ------ | -------------- | --------------------- | ----- | ------------- | --------- |
| 1      | 1614 and later | `waititem.dbss`       | 5,580 | 328 Row       | 17        |
| 1      | 1614 and later | `waititemoffset.dbss` | 3,940 | 328 Index Row | 12        |

| Layout | File                  | Known            | Unknown    |
| ------ | --------------------- | ---------------- | ---------- |
| 1      | `waititem.dbss`       | 5,580 B (100.0%) | 0 B (0.0%) |
| 1      | `waititemoffset.dbss` | 3,940 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `3d512e6c884c`  |
| 3482   | Layout 1 | `3d512e6c884c`  |
| 3474   | Layout 1 | `3d512e6c884c`  |
| 3473   | Layout 1 | `3d512e6c884c`  |
| 3464   | Layout 1 | `3d512e6c884c`  |
| 3458   | Layout 1 | `3d512e6c884c`  |
| 3454   | Layout 1 | `3d512e6c884c`  |
| 3444   | Layout 1 | `3d512e6c884c`  |
| 3435   | Layout 1 | `3d512e6c884c`  |
| 3426   | Layout 1 | `3d512e6c884c`  |
| 3418   | Layout 1 | `3d512e6c884c`  |
| 3412   | Layout 1 | `3d512e6c884c`  |
| 3402   | Layout 1 | `3d512e6c884c`  |
| 3396   | Layout 1 | `3d512e6c884c`  |
| 3387   | Layout 1 | `3d512e6c884c`  |
| 3381   | Layout 1 | `3d512e6c884c`  |
| 3373   | Layout 1 | `3d512e6c884c`  |
| 3364   | Layout 1 | `3d512e6c884c`  |
| 3356   | Layout 1 | `3d512e6c884c`  |
| 3349   | Layout 1 | `3d512e6c884c`  |
| 3342   | Layout 1 | `3d512e6c884c`  |
| 3335   | Layout 1 | `3d512e6c884c`  |
| 3326   | Layout 1 | `3d512e6c884c`  |
| 3321   | Layout 1 | `3d512e6c884c`  |
| 3314   | Layout 1 | `3d512e6c884c`  |
| 3303   | Layout 1 | `3d512e6c884c`  |
| 3302   | Layout 1 | `3d512e6c884c`  |
| 3293   | Layout 1 | `3d512e6c884c`  |
| 3283   | Layout 1 | `3d512e6c884c`  |
| 3275   | Layout 1 | `3d512e6c884c`  |
| 3267   | Layout 1 | `3d512e6c884c`  |
| 3258   | Layout 1 | `3d512e6c884c`  |
| 3251   | Layout 1 | `3d512e6c884c`  |
| 3242   | Layout 1 | `3d512e6c884c`  |
| 3235   | Layout 1 | `3d512e6c884c`  |
| 3229   | Layout 1 | `3d512e6c884c`  |
| 3212   | Layout 1 | `3d512e6c884c`  |
| 3203   | Layout 1 | `3d512e6c884c`  |
| 3193   | Layout 1 | `3d512e6c884c`  |
| 3186   | Layout 1 | `3d512e6c884c`  |
| 3177   | Layout 1 | `3d512e6c884c`  |
| 3169   | Layout 1 | `3d512e6c884c`  |
| 3158   | Layout 1 | `3d512e6c884c`  |
| 3151   | Layout 1 | `3d512e6c884c`  |
| 3144   | Layout 1 | `3d512e6c884c`  |
| 3133   | Layout 1 | `3d512e6c884c`  |
| 3125   | Layout 1 | `3d512e6c884c`  |
| 3118   | Layout 1 | `3d512e6c884c`  |
| 3111   | Layout 1 | `3d512e6c884c`  |
| 3103   | Layout 1 | `3d512e6c884c`  |
| 3095   | Layout 1 | `3d512e6c884c`  |
| 3086   | Layout 1 | `3d512e6c884c`  |
| 3072   | Layout 1 | `3d512e6c884c`  |
| 3062   | Layout 1 | `3d512e6c884c`  |
| 3052   | Layout 1 | `3d512e6c884c`  |
| 3045   | Layout 1 | `3d512e6c884c`  |
| 3037   | Layout 1 | `3d512e6c884c`  |
| 3030   | Layout 1 | `3d512e6c884c`  |
| 3021   | Layout 1 | `3d512e6c884c`  |
| 3012   | Layout 1 | `3d512e6c884c`  |
| 3002   | Layout 1 | `3d512e6c884c`  |
| 2995   | Layout 1 | `3d512e6c884c`  |
| 2987   | Layout 1 | `3d512e6c884c`  |
| 2978   | Layout 1 | `3d512e6c884c`  |
| 2970   | Layout 1 | `3d512e6c884c`  |
| 2959   | Layout 1 | `3d512e6c884c`  |
| 2951   | Layout 1 | `3d512e6c884c`  |
| 2942   | Layout 1 | `3d512e6c884c`  |
| 2935   | Layout 1 | `3d512e6c884c`  |
| 2932   | Layout 1 | `3d512e6c884c`  |
| 2923   | Layout 1 | `3d512e6c884c`  |
| 2919   | Layout 1 | `3d512e6c884c`  |
| 2907   | Layout 1 | `3d512e6c884c`  |
| 2900   | Layout 1 | `3d512e6c884c`  |
| 2891   | Layout 1 | `3d512e6c884c`  |
| 2882   | Layout 1 | `3d512e6c884c`  |
| 2872   | Layout 1 | `3d512e6c884c`  |
| 2863   | Layout 1 | `3d512e6c884c`  |
| 2855   | Layout 1 | `3d512e6c884c`  |
| 2849   | Layout 1 | `3d512e6c884c`  |
| 2844   | Layout 1 | `3d512e6c884c`  |
| 2834   | Layout 1 | `3d512e6c884c`  |
| 2825   | Layout 1 | `3d512e6c884c`  |
| 2819   | Layout 1 | `3d512e6c884c`  |
| 2811   | Layout 1 | `3d512e6c884c`  |
| 2803   | Layout 1 | `3d512e6c884c`  |
| 2794   | Layout 1 | `3d512e6c884c`  |
| 2783   | Layout 1 | `3d512e6c884c`  |
| 2774   | Layout 1 | `3d512e6c884c`  |
| 2765   | Layout 1 | `3d512e6c884c`  |
| 2756   | Layout 1 | `3d512e6c884c`  |
| 2750   | Layout 1 | `3d512e6c884c`  |
| 2743   | Layout 1 | `3d512e6c884c`  |
| 2736   | Layout 1 | `3d512e6c884c`  |
| 2726   | Layout 1 | `3d512e6c884c`  |
| 2717   | Layout 1 | `3d512e6c884c`  |
| 2709   | Layout 1 | `3d512e6c884c`  |
| 2703   | Layout 1 | `3d512e6c884c`  |
| 2695   | Layout 1 | `3d512e6c884c`  |
| 2684   | Layout 1 | `3d512e6c884c`  |
| 2672   | Layout 1 | `3d512e6c884c`  |
| 2665   | Layout 1 | `3d512e6c884c`  |
| 2657   | Layout 1 | `3d512e6c884c`  |
| 2649   | Layout 1 | `3d512e6c884c`  |
| 2644   | Layout 1 | `3d512e6c884c`  |
| 2637   | Layout 1 | `3d512e6c884c`  |
| 2629   | Layout 1 | `3d512e6c884c`  |
| 2619   | Layout 1 | `3d512e6c884c`  |
| 2612   | Layout 1 | `3d512e6c884c`  |
| 2606   | Layout 1 | `3d512e6c884c`  |
| 2602   | Layout 1 | `3d512e6c884c`  |
| 2601   | Layout 1 | `3d512e6c884c`  |
| 2592   | Layout 1 | `3d512e6c884c`  |
| 2583   | Layout 1 | `3d512e6c884c`  |
| 2575   | Layout 1 | `3d512e6c884c`  |
| 2567   | Layout 1 | `3d512e6c884c`  |
| 2560   | Layout 1 | `3d512e6c884c`  |
| 2553   | Layout 1 | `3d512e6c884c`  |
| 2545   | Layout 1 | `3d512e6c884c`  |
| 2538   | Layout 1 | `3d512e6c884c`  |
| 2529   | Layout 1 | `3d512e6c884c`  |
| 2519   | Layout 1 | `3d512e6c884c`  |
| 2513   | Layout 1 | `3d512e6c884c`  |
| 2510   | Layout 1 | `3d512e6c884c`  |
| 2507   | Layout 1 | `3d512e6c884c`  |
| 2503   | Layout 1 | `3d512e6c884c`  |
| 2498   | Layout 1 | `3d512e6c884c`  |
| 2492   | Layout 1 | `3d512e6c884c`  |
| 2487   | Layout 1 | `3d512e6c884c`  |
| 2480   | Layout 1 | `3d512e6c884c`  |
| 2474   | Layout 1 | `3d512e6c884c`  |
| 2468   | Layout 1 | `3d512e6c884c`  |
| 2460   | Layout 1 | `3d512e6c884c`  |
| 2453   | Layout 1 | `3d512e6c884c`  |
| 2444   | Layout 1 | `3d512e6c884c`  |
| 2438   | Layout 1 | `3d512e6c884c`  |
| 2434   | Layout 1 | `3d512e6c884c`  |
| 2429   | Layout 1 | `3d512e6c884c`  |
| 2421   | Layout 1 | `3d512e6c884c`  |
| 2414   | Layout 1 | `3d512e6c884c`  |
| 2407   | Layout 1 | `3d512e6c884c`  |
| 2401   | Layout 1 | `3d512e6c884c`  |
| 2397   | Layout 1 | `3d512e6c884c`  |
| 2393   | Layout 1 | `3d512e6c884c`  |
| 2384   | Layout 1 | `3d512e6c884c`  |
| 2378   | Layout 1 | `3d512e6c884c`  |
| 2372   | Layout 1 | `3d512e6c884c`  |
| 2358   | Layout 1 | `3d512e6c884c`  |
| 2352   | Layout 1 | `3d512e6c884c`  |
| 2347   | Layout 1 | `3d512e6c884c`  |
| 2343   | Layout 1 | `3d512e6c884c`  |
| 2335   | Layout 1 | `3d512e6c884c`  |
| 2327   | Layout 1 | `3d512e6c884c`  |
| 2324   | Layout 1 | `3d512e6c884c`  |
| 2319   | Layout 1 | `3d512e6c884c`  |
| 2313   | Layout 1 | `3d512e6c884c`  |
| 2308   | Layout 1 | `3d512e6c884c`  |
| 2302   | Layout 1 | `3d512e6c884c`  |
| 2295   | Layout 1 | `3d512e6c884c`  |
| 2290   | Layout 1 | `3d512e6c884c`  |
| 2284   | Layout 1 | `3d512e6c884c`  |
| 2276   | Layout 1 | `3d512e6c884c`  |
| 2269   | Layout 1 | `3d512e6c884c`  |
| 2259   | Layout 1 | `3d512e6c884c`  |
| 2250   | Layout 1 | `3d512e6c884c`  |
| 2243   | Layout 1 | `3d512e6c884c`  |
| 2235   | Layout 1 | `3d512e6c884c`  |
| 2229   | Layout 1 | `3d512e6c884c`  |
| 2224   | Layout 1 | `3d512e6c884c`  |
| 2218   | Layout 1 | `3d512e6c884c`  |
| 2215   | Layout 1 | `3d512e6c884c`  |
| 2207   | Layout 1 | `3d512e6c884c`  |
| 2203   | Layout 1 | `3d512e6c884c`  |
| 2196   | Layout 1 | `3d512e6c884c`  |
| 2192   | Layout 1 | `3d512e6c884c`  |
| 2189   | Layout 1 | `3d512e6c884c`  |
| 2183   | Layout 1 | `3d512e6c884c`  |
| 2179   | Layout 1 | `3d512e6c884c`  |
| 2171   | Layout 1 | `3d512e6c884c`  |
| 2163   | Layout 1 | `3d512e6c884c`  |
| 2156   | Layout 1 | `3d512e6c884c`  |
| 2151   | Layout 1 | `3d512e6c884c`  |
| 2147   | Layout 1 | `3d512e6c884c`  |
| 2142   | Layout 1 | `3d512e6c884c`  |
| 2138   | Layout 1 | `3d512e6c884c`  |
| 2134   | Layout 1 | `3d512e6c884c`  |
| 2130   | Layout 1 | `3d512e6c884c`  |
| 2122   | Layout 1 | `3d512e6c884c`  |
| 2107   | Layout 1 | `3d512e6c884c`  |
| 2098   | Layout 1 | `3d512e6c884c`  |
| 2089   | Layout 1 | `3d512e6c884c`  |
| 2081   | Layout 1 | `3d512e6c884c`  |
| 2073   | Layout 1 | `3d512e6c884c`  |
| 2067   | Layout 1 | `3d512e6c884c`  |
| 2063   | Layout 1 | `3d512e6c884c`  |
| 2059   | Layout 1 | `3d512e6c884c`  |
| 2052   | Layout 1 | `3d512e6c884c`  |
| 2044   | Layout 1 | `3d512e6c884c`  |
| 2039   | Layout 1 | `3d512e6c884c`  |
| 2032   | Layout 1 | `3d512e6c884c`  |
| 2025   | Layout 1 | `3d512e6c884c`  |
| 2011   | Layout 1 | `3d512e6c884c`  |
| 2005   | Layout 1 | `3d512e6c884c`  |
| 2000   | Layout 1 | `3d512e6c884c`  |
| 1996   | Layout 1 | `3d512e6c884c`  |
| 1991   | Layout 1 | `3d512e6c884c`  |
| 1985   | Layout 1 | `3d512e6c884c`  |
| 1980   | Layout 1 | `3d512e6c884c`  |
| 1969   | Layout 1 | `3d512e6c884c`  |
| 1964   | Layout 1 | `3d512e6c884c`  |
| 1958   | Layout 1 | `3d512e6c884c`  |
| 1950   | Layout 1 | `3d512e6c884c`  |
| 1945   | Layout 1 | `3d512e6c884c`  |
| 1937   | Layout 1 | `3d512e6c884c`  |
| 1933   | Layout 1 | `3d512e6c884c`  |
| 1927   | Layout 1 | `3d512e6c884c`  |
| 1921   | Layout 1 | `3d512e6c884c`  |
| 1914   | Layout 1 | `3d512e6c884c`  |
| 1908   | Layout 1 | `3d512e6c884c`  |
| 1897   | Layout 1 | `3d512e6c884c`  |
| 1892   | Layout 1 | `3d512e6c884c`  |
| 1886   | Layout 1 | `3d512e6c884c`  |
| 1881   | Layout 1 | `3d512e6c884c`  |
| 1871   | Layout 1 | `3d512e6c884c`  |
| 1866   | Layout 1 | `3d512e6c884c`  |
| 1862   | Layout 1 | `3d512e6c884c`  |
| 1854   | Layout 1 | `3d512e6c884c`  |
| 1846   | Layout 1 | `3d512e6c884c`  |
| 1838   | Layout 1 | `3d512e6c884c`  |
| 1832   | Layout 1 | `3d512e6c884c`  |
| 1826   | Layout 1 | `3d512e6c884c`  |
| 1822   | Layout 1 | `3d512e6c884c`  |
| 1818   | Layout 1 | `3d512e6c884c`  |
| 1804   | Layout 1 | `3d512e6c884c`  |
| 1794   | Layout 1 | `3d512e6c884c`  |
| 1790   | Layout 1 | `3d512e6c884c`  |
| 1784   | Layout 1 | `3d512e6c884c`  |
| 1774   | Layout 1 | `3d512e6c884c`  |
| 1771   | Layout 1 | `3d512e6c884c`  |
| 1762   | Layout 1 | `3d512e6c884c`  |
| 1759   | Layout 1 | `3d512e6c884c`  |
| 1754   | Layout 1 | `3d512e6c884c`  |
| 1749   | Layout 1 | `3d512e6c884c`  |
| 1743   | Layout 1 | `3d512e6c884c`  |
| 1737   | Layout 1 | `3d512e6c884c`  |
| 1731   | Layout 1 | `3d512e6c884c`  |
| 1725   | Layout 1 | `3d512e6c884c`  |
| 1717   | Layout 1 | `3d512e6c884c`  |
| 1710   | Layout 1 | `3d512e6c884c`  |
| 1704   | Layout 1 | `3d512e6c884c`  |
| 1698   | Layout 1 | `3d512e6c884c`  |
| 1690   | Layout 1 | `3d512e6c884c`  |
| 1685   | Layout 1 | `3d512e6c884c`  |
| 1680   | Layout 1 | `3d512e6c884c`  |
| 1674   | Layout 1 | `3d512e6c884c`  |
| 1668   | Layout 1 | `3d512e6c884c`  |
| 1659   | Layout 1 | `3d512e6c884c`  |
| 1649   | Layout 1 | `3d512e6c884c`  |
| 1642   | Layout 1 | `3d512e6c884c`  |
| 1636   | Layout 1 | `3d512e6c884c`  |
| 1628   | Layout 1 | `3d512e6c884c`  |
| 1622   | Layout 1 | `3d512e6c884c`  |
| 1614   | Layout 1 | `3d512e6c884c`  |
| 1608   | No file  | `3d512e6c884c`  |
| 1602   | No file  | `3d512e6c884c`  |
| 1598   | No file  | `3d512e6c884c`  |
| 1594   | No file  | `3d512e6c884c`  |
| 1590   | No file  | `3d512e6c884c`  |
| 1587   | No file  | `3d512e6c884c`  |
| 1584   | No file  | `3d512e6c884c`  |
| 1579   | No file  | `3d512e6c884c`  |
| 1572   | No file  | `3d512e6c884c`  |
| 1565   | No file  | `3d512e6c884c`  |
| 1559   | No file  | `3d512e6c884c`  |
| 1554   | No file  | `3d512e6c884c`  |
| 1547   | No file  | `3d512e6c884c`  |
| 1537   | No file  | `3d512e6c884c`  |
| 1529   | No file  | `3d512e6c884c`  |
| 1524   | No file  | `3d512e6c884c`  |
| 1519   | No file  | `3d512e6c884c`  |
| 1509   | No file  | `3d512e6c884c`  |
| 1506   | No file  | `3d512e6c884c`  |
| 1504   | No file  | `3d512e6c884c`  |
| 1500   | No file  | `3d512e6c884c`  |
| 1493   | No file  | `3d512e6c884c`  |
| 1489   | No file  | `3d512e6c884c`  |
| 1485   | No file  | `3d512e6c884c`  |
| 1481   | No file  | `3d512e6c884c`  |
| 1474   | No file  | `3d512e6c884c`  |
| 1466   | No file  | `3d512e6c884c`  |
| 1462   | No file  | `3d512e6c884c`  |
| 1459   | No file  | `3d512e6c884c`  |
| 1453   | No file  | `3d512e6c884c`  |
| 1450   | No file  | `3d512e6c884c`  |
| 1445   | No file  | `3d512e6c884c`  |
| 1439   | No file  | `3d512e6c884c`  |
| 1433   | No file  | `3d512e6c884c`  |
| 1430   | No file  | `3d512e6c884c`  |
| 1426   | No file  | `3d512e6c884c`  |
| 1421   | No file  | `3d512e6c884c`  |
| 1417   | No file  | `3d512e6c884c`  |
| 1416   | No file  | `3d512e6c884c`  |
| 1409   | No file  | `3d512e6c884c`  |
| 1405   | No file  | `3d512e6c884c`  |
| 1401   | No file  | `3d512e6c884c`  |
| 1396   | No file  | `3d512e6c884c`  |
| 1391   | No file  | `3d512e6c884c`  |
| 1390   | No file  | `3d512e6c884c`  |
| 1386   | No file  | `3d512e6c884c`  |
| 1381   | No file  | `3d512e6c884c`  |
| 1379   | No file  | `3d512e6c884c`  |
| 1372   | No file  | `3d512e6c884c`  |
| 1366   | No file  | `3d512e6c884c`  |
| 1364   | No file  | `3d512e6c884c`  |
| 1363   | No file  | `3d512e6c884c`  |
| 1360   | No file  | `3d512e6c884c`  |
| 1358   | No file  | `3d512e6c884c`  |
| 1355   | No file  | `3d512e6c884c`  |
| 1351   | No file  | `3d512e6c884c`  |
| 1348   | No file  | `3d512e6c884c`  |
| 1346   | No file  | `3d512e6c884c`  |
| 1341   | No file  | `3d512e6c884c`  |
| 1340   | No file  | `3d512e6c884c`  |
| 1338   | No file  | `3d512e6c884c`  |
| 1335   | No file  | `3d512e6c884c`  |
| 1333   | No file  | `3d512e6c884c`  |
| 1329   | No file  | `3d512e6c884c`  |
| 1327   | No file  | `3d512e6c884c`  |
| 1324   | No file  | `3d512e6c884c`  |
| 1321   | No file  | `3d512e6c884c`  |
| 1319   | No file  | `3d512e6c884c`  |
| 1318   | No file  | `3d512e6c884c`  |
| 1316   | No file  | `3d512e6c884c`  |
| 1313   | No file  | `3d512e6c884c`  |
| 1311   | No file  | `3d512e6c884c`  |
| 1309   | No file  | `3d512e6c884c`  |
| 1304   | No file  | `3d512e6c884c`  |
| 1292   | No file  | `3d512e6c884c`  |
| 1286   | No file  | `3d512e6c884c`  |
| 1280   | No file  | `3d512e6c884c`  |
| 1276   | No file  | `3d512e6c884c`  |
| 1267   | No file  | `3d512e6c884c`  |
| 1261   | No file  | `3d512e6c884c`  |
| 1256   | No file  | `3d512e6c884c`  |
| 1250   | No file  | `3d512e6c884c`  |
| 1246   | No file  | `3d512e6c884c`  |
| 1239   | No file  | `3d512e6c884c`  |
| 1230   | No file  | `3d512e6c884c`  |
| 1226   | No file  | `3d512e6c884c`  |
| 1220   | No file  | `3d512e6c884c`  |
| 1217   | No file  | `3d512e6c884c`  |
| 1211   | No file  | `3d512e6c884c`  |
| 1210   | No file  | `3d512e6c884c`  |
| 1208   | No file  | `3d512e6c884c`  |
| 1203   | No file  | `3d512e6c884c`  |
| 1197   | No file  | `3d512e6c884c`  |
| 1194   | No file  | `3d512e6c884c`  |
| 1192   | No file  | `3d512e6c884c`  |
| 1187   | No file  | `3d512e6c884c`  |
| 1183   | No file  | `3d512e6c884c`  |
| 1177   | No file  | `3d512e6c884c`  |
| 1173   | No file  | `3d512e6c884c`  |
| 1167   | No file  | `3d512e6c884c`  |
| 1164   | No file  | `3d512e6c884c`  |
| 1156   | No file  | `3d512e6c884c`  |
| 1149   | No file  | `3d512e6c884c`  |
| 1144   | No file  | `3d512e6c884c`  |
| 1137   | No file  | `3d512e6c884c`  |
| 1132   | No file  | `3d512e6c884c`  |
| 1127   | No file  | `3d512e6c884c`  |
| 1122   | No file  | `3d512e6c884c`  |
| 1118   | No file  | `3d512e6c884c`  |
| 1114   | No file  | `3d512e6c884c`  |
| 1109   | No file  | `3d512e6c884c`  |
| 1102   | No file  | `3d512e6c884c`  |
| 1096   | No file  | `3d512e6c884c`  |
| 1088   | No file  | `3d512e6c884c`  |
| 1081   | No file  | `3d512e6c884c`  |
| 1076   | No file  | `3d512e6c884c`  |
| 1069   | No file  | `3d512e6c884c`  |
| 1064   | No file  | `3d512e6c884c`  |
| 1058   | No file  | `3d512e6c884c`  |
| 1051   | No file  | `3d512e6c884c`  |
| 1044   | No file  | `3d512e6c884c`  |
| 1036   | No file  | `3d512e6c884c`  |
| 1026   | No file  | `3d512e6c884c`  |
| 1016   | No file  | `3d512e6c884c`  |
| 1009   | No file  | `3d512e6c884c`  |
| 1005   | No file  | `3d512e6c884c`  |
| 1000   | No file  | `3d512e6c884c`  |
| 998    | No file  | `3d512e6c884c`  |
| 990    | No file  | `3d512e6c884c`  |
| 979    | No file  | `3d512e6c884c`  |
| 972    | No file  | `3d512e6c884c`  |
| 963    | No file  | `3d512e6c884c`  |
| 955    | No file  | `3d512e6c884c`  |
| 946    | No file  | `3d512e6c884c`  |
| 938    | No file  | `3d512e6c884c`  |
| 927    | No file  | `3d512e6c884c`  |
| 911    | No file  | `3d512e6c884c`  |
| 904    | No file  | `3d512e6c884c`  |
| 899    | No file  | `3d512e6c884c`  |
| 894    | No file  | `3d512e6c884c`  |
| 885    | No file  | `3d512e6c884c`  |
| 879    | No file  | `3d512e6c884c`  |
| 872    | No file  | `3d512e6c884c`  |
| 864    | No file  | `3d512e6c884c`  |
| 855    | No file  | `3d512e6c884c`  |
| 853    | No file  | `3d512e6c884c`  |
| 845    | No file  | `3d512e6c884c`  |
| 837    | No file  | `3d512e6c884c`  |
| 829    | No file  | `3d512e6c884c`  |
| 822    | No file  | `3d512e6c884c`  |
| 814    | No file  | `3d512e6c884c`  |
| 805    | No file  | `3d512e6c884c`  |
| 794    | No file  | `3d512e6c884c`  |
| 787    | No file  | `3d512e6c884c`  |
| 780    | No file  | `3d512e6c884c`  |
| 771    | No file  | `3d512e6c884c`  |
| 760    | No file  | `3d512e6c884c`  |
| 748    | No file  | `3d512e6c884c`  |
| 741    | No file  | `3d512e6c884c`  |
| 736    | No file  | `3d512e6c884c`  |
| 731    | No file  | `3d512e6c884c`  |
| 723    | No file  | `3d512e6c884c`  |
| 711    | No file  | `3d512e6c884c`  |
| 707    | No file  | `3d512e6c884c`  |
| 697    | No file  | `3d512e6c884c`  |
| 689    | No file  | `3d512e6c884c`  |
| 683    | No file  | `3d512e6c884c`  |
| 678    | No file  | `3d512e6c884c`  |
| 670    | No file  | `3d512e6c884c`  |
| 661    | No file  | `3d512e6c884c`  |
| 656    | No file  | `3d512e6c884c`  |
| 652    | No file  | `3d512e6c884c`  |
| 643    | No file  | `3d512e6c884c`  |
| 637    | No file  | `3d512e6c884c`  |
| 630    | No file  | `3d512e6c884c`  |
| 627    | No file  | `3d512e6c884c`  |
| 621    | No file  | `3d512e6c884c`  |
| 617    | No file  | `3d512e6c884c`  |
| 615    | No file  | `3d512e6c884c`  |
| 606    | No file  | `3d512e6c884c`  |
| 599    | No file  | `3d512e6c884c`  |
| 592    | No file  | `3d512e6c884c`  |
| 586    | No file  | `3d512e6c884c`  |
| 577    | No file  | `3d512e6c884c`  |
| 569    | No file  | `3d512e6c884c`  |
| 561    | No file  | `3d512e6c884c`  |
| 554    | No file  | `3d512e6c884c`  |
| 542    | No file  | `3d512e6c884c`  |
| 532    | No file  | `3d512e6c884c`  |
| 531    | No file  | `3d512e6c884c`  |
| 526    | No file  | `3d512e6c884c`  |
| 521    | No file  | `3d512e6c884c`  |
| 517    | No file  | `3d512e6c884c`  |
| 510    | No file  | `3d512e6c884c`  |
| 508    | No file  | `3d512e6c884c`  |
| 504    | No file  | `3d512e6c884c`  |
| 497    | No file  | `3d512e6c884c`  |
| 491    | No file  | `3d512e6c884c`  |
| 485    | No file  | `3d512e6c884c`  |
| 478    | No file  | `3d512e6c884c`  |
| 472    | No file  | `3d512e6c884c`  |
| 466    | No file  | `3d512e6c884c`  |
| 457    | No file  | `3d512e6c884c`  |
| 452    | No file  | `3d512e6c884c`  |
| 449    | No file  | `3d512e6c884c`  |
| 435    | No file  | `3d512e6c884c`  |

<!-- versions:end -->

## Companion Files

None. The handler reads the rows in file order and does not need
`waititemoffset.dbss` (see below). Item names come from LOC type 0 and 79,
icons from the `ITEM_KEY` and `ITEM_ICON` lookup indexes.

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then 17-byte rows; the
file ends after the last row.

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | `328` on client 3464 |
| `+0x04` | Row[row_count] | rows      | See Row              |

### Row (17 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | key           | Row key; equals `item_key` on every row                      |
| `+0x04` | u32  | item_key      | `enchant_level << 24 \| item_id`, the packed key of `_common/item_key.py` |
| `+0x08` | u32  | item_id       | The low 24 bits of `item_key`                                |
| `+0x0C` | u8   | enchant_level | The top byte of `item_key`                                   |
| `+0x0D` | u32  | wait_second   | `900` on every row (client 3474); see Field Names            |

On client 3464 the 328 rows hold 184 items:

| Levels        | Items | Examples                                                                   |
| ------------- | ----- | -------------------------------------------------------------------------- |
| `20`          | 89    | Blackstar weapons and armor, boss armor, Manos tools and clothes (735001 Blackstar Shield, 11013 Giath's Helmet, 16479 Manos Hoe, 705517 Manos Gatherer's Clothes) |
| `3`, `4`, `5` | 66    | Godr-Ayed weapons (736015 Godr-Ayed Longsword, 738201 Godr-Ayed Shield)    |
| `4`, `5`      | 7     | Accessories (11653 Deboreka Necklace, 12276 Deboreka Belt, 11663 Revived Lunar Necklace) |
| `5`           | 21    | Accessories (11629 Tungrad Necklace, 12061 Tungrad Ring, 705509 Manos Necklace) |
| `0` to `5`    | 1     | 719898 Fallen God's Armor                                                  |

### `waititemoffset.dbss`

A row count equal to the main file's, then one index row per main row.

| Offset  | Type                 | Field     | Notes                              |
| ------- | -------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                      |

### Index Row (12 bytes)

| Offset  | Type | Field    | Notes                                                        |
| ------- | ---- | -------- | ------------------------------------------------------------ |
| `+0x00` | u32  | item_key | Row key, the main row's `key`                                |
| `+0x04` | u32  | offset   | Start of the row in `waititem.dbss` plus 4, at its `item_key` |
| `+0x08` | u32  | size     | Always `13`, the row size minus the 4-byte `key`             |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first one points at main row 4).

## Field Names

The row is the `WorldMarketWaitItem` sheet of a private server on client
1784, with the columns `ItemKey`, `EnchantLevel` and `WaitSecond`. That
server's dump (`Instance_dumpFull.exe`) loads the sheet into
`WorldTradeMarketWaitItemStaticStatus` (loader at VA `0x140a70270`) and
fills the struct in file order (VA `0x140cf600f` to `0x140cf6020`): the
packed key `EnchantLevel << 24 | ItemKey` at `+0`, `ItemKey` at `+4`,
`EnchantLevel` as a byte at `+8` and `WaitSecond` as a u32 at `+0x0C`. After
the row's 4-byte `key`, the 13 bytes the index points at are that struct,
so `+0x0D` is `WaitSecond`.

The loader rejects a row whose `ItemKey` is `0`, whose `EnchantLevel` is
21 or more, or whose `WaitSecond` is above 18,000 (5 hours), with
"판매 대기 waitSecond 비정상 입니다" ("sale wait: waitSecond is invalid") for
the last. The server has no reader for the client file; it loads only the
sheet.

The sheet and the private server's own `waititem.dbss` hold the same 101
rows: matched on item and level, `wait_second` equals `WaitSecond` on all
101. Every value is `900` there and on the 328 rows of client 3474, so the
values alone do not place the column; the struct order above does.

## Notes

- The Central Market sell window asks
  `ToClient_GetWorldMarketIsWaitItemPopUp(enchantKey, price)` before it
  lists an item and, when it returns true, warns that the Value Pack may
  expire before the sale (`LUA_MARKETPLACE_VALUEPACKAGE_WARNING_MSG`,
  `panel_window_marketplace_sell_renew`). The function takes the item key
  that this file lists. The Central Market lists the queued items under
  `PANEL_MARKETPLACE_WAITLISTTITME` "In Registration Queue", each with its
  `getWaitEndTime()` (`panel_window_marketplace_itemmarket_renew`).
- The registration warning `LUA_ITEMMARKET_REGISTITEM_CANCELITEM_MSGBOX2`
  says "The waiting time until being posted may vary depending on the
  situation", so the client text gives no fixed queue time.
- Accessory and Godr-Ayed levels `3` to `5` are TRI to PEN in game; the
  Item column shows the raw level in brackets, as `item_key_text()` does for
  every table.

## Open Questions

### Whether the List Is the Whole Rule

`ToClient_GetWorldMarketIsWaitItemPopUp` also takes the price, so the queue
may depend on the price as well as on this list. The client code that reads
the file is not in Lua.

## In-Game Checks

### wait_second as the Queue Time

Needs zone: any Central Market

`wait_second` is `900` on every row, 15 minutes. This checks that it is the
time an item waits in the Registration Queue.

1. Open the Central Market and list an item from this table.
2. Pick "In Registration Queue" and note the end time of the item, which
   appears at the top of the list.

Expected: the end time is 15 minutes after the item entered the queue.
