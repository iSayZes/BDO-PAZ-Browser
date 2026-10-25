# `majorseigereleaseobjectpoint.bss` Format

## Purpose

The Conquest War (major siege) liberation points per siege object: rows
of a `characterstatic.dbss` character key and its point value. On client
3482 the 71 rows cover the guild siege buildings: command posts, field
HQs and forts are worth `150`, the Barricade and the Defense Tower `1`.
The file name keeps the client's spelling `seige`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------------------------- | ----- | ------- | --------- |
| 1      | 1690 and later | `majorseigereleaseobjectpoint.bss` | 446   | 71 Row  | 6         |

| Layout | File                               | Known          | Unknown    |
| ------ | ---------------------------------- | -------------- | ---------- |
| 1      | `majorseigereleaseobjectpoint.bss` | 446 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c3516e6b7091`  |
| 3482   | Layout 1 | `c3516e6b7091`  |
| 3474   | Layout 1 | `c3516e6b7091`  |
| 3473   | Layout 1 | `c3516e6b7091`  |
| 3464   | Layout 1 | `c3516e6b7091`  |
| 3458   | Layout 1 | `c3516e6b7091`  |
| 3454   | Layout 1 | `c3516e6b7091`  |
| 3444   | Layout 1 | `c3516e6b7091`  |
| 3435   | Layout 1 | `c3516e6b7091`  |
| 3426   | Layout 1 | `c3516e6b7091`  |
| 3418   | Layout 1 | `c3516e6b7091`  |
| 3412   | Layout 1 | `c3516e6b7091`  |
| 3402   | Layout 1 | `c3516e6b7091`  |
| 3396   | Layout 1 | `c3516e6b7091`  |
| 3387   | Layout 1 | `c3516e6b7091`  |
| 3381   | Layout 1 | `c3516e6b7091`  |
| 3373   | Layout 1 | `c3516e6b7091`  |
| 3364   | Layout 1 | `c3516e6b7091`  |
| 3356   | Layout 1 | `c3516e6b7091`  |
| 3349   | Layout 1 | `c3516e6b7091`  |
| 3342   | Layout 1 | `c3516e6b7091`  |
| 3335   | Layout 1 | `c3516e6b7091`  |
| 3326   | Layout 1 | `c3516e6b7091`  |
| 3321   | Layout 1 | `c3516e6b7091`  |
| 3314   | Layout 1 | `c3516e6b7091`  |
| 3303   | Layout 1 | `c3516e6b7091`  |
| 3302   | Layout 1 | `c3516e6b7091`  |
| 3293   | Layout 1 | `c3516e6b7091`  |
| 3283   | Layout 1 | `c3516e6b7091`  |
| 3275   | Layout 1 | `c3516e6b7091`  |
| 3267   | Layout 1 | `c3516e6b7091`  |
| 3258   | Layout 1 | `c3516e6b7091`  |
| 3251   | Layout 1 | `c3516e6b7091`  |
| 3242   | Layout 1 | `c3516e6b7091`  |
| 3235   | Layout 1 | `c3516e6b7091`  |
| 3229   | Layout 1 | `c3516e6b7091`  |
| 3212   | Layout 1 | `c3516e6b7091`  |
| 3203   | Layout 1 | `c3516e6b7091`  |
| 3193   | Layout 1 | `c3516e6b7091`  |
| 3186   | Layout 1 | `c3516e6b7091`  |
| 3177   | Layout 1 | `c3516e6b7091`  |
| 3169   | Layout 1 | `c3516e6b7091`  |
| 3158   | Layout 1 | `c3516e6b7091`  |
| 3151   | Layout 1 | `c3516e6b7091`  |
| 3144   | Layout 1 | `c3516e6b7091`  |
| 3133   | Layout 1 | `c3516e6b7091`  |
| 3125   | Layout 1 | `c3516e6b7091`  |
| 3118   | Layout 1 | `c3516e6b7091`  |
| 3111   | Layout 1 | `c3516e6b7091`  |
| 3103   | Layout 1 | `c3516e6b7091`  |
| 3095   | Layout 1 | `c3516e6b7091`  |
| 3086   | Layout 1 | `c3516e6b7091`  |
| 3072   | Layout 1 | `c3516e6b7091`  |
| 3062   | Layout 1 | `c3516e6b7091`  |
| 3052   | Layout 1 | `c3516e6b7091`  |
| 3045   | Layout 1 | `c3516e6b7091`  |
| 3037   | Layout 1 | `c3516e6b7091`  |
| 3030   | Layout 1 | `c3516e6b7091`  |
| 3021   | Layout 1 | `c3516e6b7091`  |
| 3012   | Layout 1 | `c3516e6b7091`  |
| 3002   | Layout 1 | `c3516e6b7091`  |
| 2995   | Layout 1 | `c3516e6b7091`  |
| 2987   | Layout 1 | `c3516e6b7091`  |
| 2978   | Layout 1 | `c3516e6b7091`  |
| 2970   | Layout 1 | `c3516e6b7091`  |
| 2959   | Layout 1 | `c3516e6b7091`  |
| 2951   | Layout 1 | `c3516e6b7091`  |
| 2942   | Layout 1 | `c3516e6b7091`  |
| 2935   | Layout 1 | `c3516e6b7091`  |
| 2932   | Layout 1 | `c3516e6b7091`  |
| 2923   | Layout 1 | `c3516e6b7091`  |
| 2919   | Layout 1 | `c3516e6b7091`  |
| 2907   | Layout 1 | `c3516e6b7091`  |
| 2900   | Layout 1 | `c3516e6b7091`  |
| 2891   | Layout 1 | `c3516e6b7091`  |
| 2882   | Layout 1 | `c3516e6b7091`  |
| 2872   | Layout 1 | `c3516e6b7091`  |
| 2863   | Layout 1 | `c3516e6b7091`  |
| 2855   | Layout 1 | `c3516e6b7091`  |
| 2849   | Layout 1 | `c3516e6b7091`  |
| 2844   | Layout 1 | `c3516e6b7091`  |
| 2834   | Layout 1 | `c3516e6b7091`  |
| 2825   | Layout 1 | `c3516e6b7091`  |
| 2819   | Layout 1 | `c3516e6b7091`  |
| 2811   | Layout 1 | `c3516e6b7091`  |
| 2803   | Layout 1 | `c3516e6b7091`  |
| 2794   | Layout 1 | `c3516e6b7091`  |
| 2783   | Layout 1 | `c3516e6b7091`  |
| 2774   | Layout 1 | `c3516e6b7091`  |
| 2765   | Layout 1 | `c3516e6b7091`  |
| 2756   | Layout 1 | `c3516e6b7091`  |
| 2750   | Layout 1 | `c3516e6b7091`  |
| 2743   | Layout 1 | `c3516e6b7091`  |
| 2736   | Layout 1 | `c3516e6b7091`  |
| 2726   | Layout 1 | `c3516e6b7091`  |
| 2717   | Layout 1 | `c3516e6b7091`  |
| 2709   | Layout 1 | `c3516e6b7091`  |
| 2703   | Layout 1 | `c3516e6b7091`  |
| 2695   | Layout 1 | `c3516e6b7091`  |
| 2684   | Layout 1 | `c3516e6b7091`  |
| 2672   | Layout 1 | `c3516e6b7091`  |
| 2665   | Layout 1 | `c3516e6b7091`  |
| 2657   | Layout 1 | `c3516e6b7091`  |
| 2649   | Layout 1 | `c3516e6b7091`  |
| 2644   | Layout 1 | `c3516e6b7091`  |
| 2637   | Layout 1 | `c3516e6b7091`  |
| 2629   | Layout 1 | `c3516e6b7091`  |
| 2619   | Layout 1 | `c3516e6b7091`  |
| 2612   | Layout 1 | `c3516e6b7091`  |
| 2606   | Layout 1 | `c3516e6b7091`  |
| 2602   | Layout 1 | `c3516e6b7091`  |
| 2601   | Layout 1 | `c3516e6b7091`  |
| 2592   | Layout 1 | `c3516e6b7091`  |
| 2583   | Layout 1 | `c3516e6b7091`  |
| 2575   | Layout 1 | `c3516e6b7091`  |
| 2567   | Layout 1 | `c3516e6b7091`  |
| 2560   | Layout 1 | `c3516e6b7091`  |
| 2553   | Layout 1 | `c3516e6b7091`  |
| 2545   | Layout 1 | `c3516e6b7091`  |
| 2538   | Layout 1 | `c3516e6b7091`  |
| 2529   | Layout 1 | `c3516e6b7091`  |
| 2519   | Layout 1 | `c3516e6b7091`  |
| 2513   | Layout 1 | `c3516e6b7091`  |
| 2510   | Layout 1 | `c3516e6b7091`  |
| 2507   | Layout 1 | `c3516e6b7091`  |
| 2503   | Layout 1 | `c3516e6b7091`  |
| 2498   | Layout 1 | `c3516e6b7091`  |
| 2492   | Layout 1 | `c3516e6b7091`  |
| 2487   | Layout 1 | `c3516e6b7091`  |
| 2480   | Layout 1 | `c3516e6b7091`  |
| 2474   | Layout 1 | `c3516e6b7091`  |
| 2468   | Layout 1 | `c3516e6b7091`  |
| 2460   | Layout 1 | `c3516e6b7091`  |
| 2453   | Layout 1 | `c3516e6b7091`  |
| 2444   | Layout 1 | `c3516e6b7091`  |
| 2438   | Layout 1 | `c3516e6b7091`  |
| 2434   | Layout 1 | `c3516e6b7091`  |
| 2429   | Layout 1 | `c3516e6b7091`  |
| 2421   | Layout 1 | `c3516e6b7091`  |
| 2414   | Layout 1 | `c3516e6b7091`  |
| 2407   | Layout 1 | `c3516e6b7091`  |
| 2401   | Layout 1 | `c3516e6b7091`  |
| 2397   | Layout 1 | `c3516e6b7091`  |
| 2393   | Layout 1 | `c3516e6b7091`  |
| 2384   | Layout 1 | `c3516e6b7091`  |
| 2378   | Layout 1 | `c3516e6b7091`  |
| 2372   | Layout 1 | `c3516e6b7091`  |
| 2358   | Layout 1 | `c3516e6b7091`  |
| 2352   | Layout 1 | `c3516e6b7091`  |
| 2347   | Layout 1 | `c3516e6b7091`  |
| 2343   | Layout 1 | `c3516e6b7091`  |
| 2335   | Layout 1 | `c3516e6b7091`  |
| 2327   | Layout 1 | `c3516e6b7091`  |
| 2324   | Layout 1 | `c3516e6b7091`  |
| 2319   | Layout 1 | `c3516e6b7091`  |
| 2313   | Layout 1 | `c3516e6b7091`  |
| 2308   | Layout 1 | `c3516e6b7091`  |
| 2302   | Layout 1 | `c3516e6b7091`  |
| 2295   | Layout 1 | `c3516e6b7091`  |
| 2290   | Layout 1 | `c3516e6b7091`  |
| 2284   | Layout 1 | `c3516e6b7091`  |
| 2276   | Layout 1 | `c3516e6b7091`  |
| 2269   | Layout 1 | `c3516e6b7091`  |
| 2259   | Layout 1 | `c3516e6b7091`  |
| 2250   | Layout 1 | `c3516e6b7091`  |
| 2243   | Layout 1 | `c3516e6b7091`  |
| 2235   | Layout 1 | `c3516e6b7091`  |
| 2229   | Layout 1 | `c3516e6b7091`  |
| 2224   | Layout 1 | `c3516e6b7091`  |
| 2218   | Layout 1 | `c3516e6b7091`  |
| 2215   | Layout 1 | `c3516e6b7091`  |
| 2207   | Layout 1 | `c3516e6b7091`  |
| 2203   | Layout 1 | `c3516e6b7091`  |
| 2196   | Layout 1 | `c3516e6b7091`  |
| 2192   | Layout 1 | `c3516e6b7091`  |
| 2189   | Layout 1 | `c3516e6b7091`  |
| 2183   | Layout 1 | `c3516e6b7091`  |
| 2179   | Layout 1 | `c3516e6b7091`  |
| 2171   | Layout 1 | `c3516e6b7091`  |
| 2163   | Layout 1 | `c3516e6b7091`  |
| 2156   | Layout 1 | `c3516e6b7091`  |
| 2151   | Layout 1 | `c3516e6b7091`  |
| 2147   | Layout 1 | `c3516e6b7091`  |
| 2142   | Layout 1 | `c3516e6b7091`  |
| 2138   | Layout 1 | `c3516e6b7091`  |
| 2134   | Layout 1 | `c3516e6b7091`  |
| 2130   | Layout 1 | `c3516e6b7091`  |
| 2122   | Layout 1 | `c3516e6b7091`  |
| 2107   | Layout 1 | `c3516e6b7091`  |
| 2098   | Layout 1 | `c3516e6b7091`  |
| 2089   | Layout 1 | `c3516e6b7091`  |
| 2081   | Layout 1 | `c3516e6b7091`  |
| 2073   | Layout 1 | `c3516e6b7091`  |
| 2067   | Layout 1 | `c3516e6b7091`  |
| 2063   | Layout 1 | `c3516e6b7091`  |
| 2059   | Layout 1 | `c3516e6b7091`  |
| 2052   | Layout 1 | `c3516e6b7091`  |
| 2044   | Layout 1 | `c3516e6b7091`  |
| 2039   | Layout 1 | `c3516e6b7091`  |
| 2032   | Layout 1 | `c3516e6b7091`  |
| 2025   | Layout 1 | `c3516e6b7091`  |
| 2011   | Layout 1 | `c3516e6b7091`  |
| 2005   | Layout 1 | `c3516e6b7091`  |
| 2000   | Layout 1 | `c3516e6b7091`  |
| 1996   | Layout 1 | `c3516e6b7091`  |
| 1991   | Layout 1 | `c3516e6b7091`  |
| 1985   | Layout 1 | `c3516e6b7091`  |
| 1980   | Layout 1 | `c3516e6b7091`  |
| 1969   | Layout 1 | `c3516e6b7091`  |
| 1964   | Layout 1 | `c3516e6b7091`  |
| 1958   | Layout 1 | `c3516e6b7091`  |
| 1950   | Layout 1 | `c3516e6b7091`  |
| 1945   | Layout 1 | `c3516e6b7091`  |
| 1937   | Layout 1 | `c3516e6b7091`  |
| 1933   | Layout 1 | `c3516e6b7091`  |
| 1927   | Layout 1 | `c3516e6b7091`  |
| 1921   | Layout 1 | `c3516e6b7091`  |
| 1914   | Layout 1 | `c3516e6b7091`  |
| 1908   | Layout 1 | `c3516e6b7091`  |
| 1897   | Layout 1 | `c3516e6b7091`  |
| 1892   | Layout 1 | `c3516e6b7091`  |
| 1886   | Layout 1 | `c3516e6b7091`  |
| 1881   | Layout 1 | `c3516e6b7091`  |
| 1871   | Layout 1 | `c3516e6b7091`  |
| 1866   | Layout 1 | `c3516e6b7091`  |
| 1862   | Layout 1 | `c3516e6b7091`  |
| 1854   | Layout 1 | `c3516e6b7091`  |
| 1846   | Layout 1 | `c3516e6b7091`  |
| 1838   | Layout 1 | `c3516e6b7091`  |
| 1832   | Layout 1 | `c3516e6b7091`  |
| 1826   | Layout 1 | `c3516e6b7091`  |
| 1822   | Layout 1 | `c3516e6b7091`  |
| 1818   | Layout 1 | `c3516e6b7091`  |
| 1804   | Layout 1 | `c3516e6b7091`  |
| 1794   | Layout 1 | `c3516e6b7091`  |
| 1790   | Layout 1 | `c3516e6b7091`  |
| 1784   | Layout 1 | `c3516e6b7091`  |
| 1774   | Layout 1 | `c3516e6b7091`  |
| 1771   | Layout 1 | `c3516e6b7091`  |
| 1762   | Layout 1 | `c3516e6b7091`  |
| 1759   | Layout 1 | `c3516e6b7091`  |
| 1754   | Layout 1 | `c3516e6b7091`  |
| 1749   | Layout 1 | `c3516e6b7091`  |
| 1743   | Layout 1 | `c3516e6b7091`  |
| 1737   | Layout 1 | `c3516e6b7091`  |
| 1731   | Layout 1 | `c3516e6b7091`  |
| 1725   | Layout 1 | `c3516e6b7091`  |
| 1717   | Layout 1 | `c3516e6b7091`  |
| 1710   | Layout 1 | `c3516e6b7091`  |
| 1704   | Layout 1 | `c3516e6b7091`  |
| 1698   | Layout 1 | `c3516e6b7091`  |
| 1690   | Layout 1 | `c3516e6b7091`  |
| 1685   | No file  | `c3516e6b7091`  |
| 1680   | No file  | `c3516e6b7091`  |
| 1674   | No file  | `c3516e6b7091`  |
| 1668   | No file  | `c3516e6b7091`  |
| 1659   | No file  | `c3516e6b7091`  |
| 1649   | No file  | `c3516e6b7091`  |
| 1642   | No file  | `c3516e6b7091`  |
| 1636   | No file  | `c3516e6b7091`  |
| 1628   | No file  | `c3516e6b7091`  |
| 1622   | No file  | `c3516e6b7091`  |
| 1614   | No file  | `c3516e6b7091`  |
| 1608   | No file  | `c3516e6b7091`  |
| 1602   | No file  | `c3516e6b7091`  |
| 1598   | No file  | `c3516e6b7091`  |
| 1594   | No file  | `c3516e6b7091`  |
| 1590   | No file  | `c3516e6b7091`  |
| 1587   | No file  | `c3516e6b7091`  |
| 1584   | No file  | `c3516e6b7091`  |
| 1579   | No file  | `c3516e6b7091`  |
| 1572   | No file  | `c3516e6b7091`  |
| 1565   | No file  | `c3516e6b7091`  |
| 1559   | No file  | `c3516e6b7091`  |
| 1554   | No file  | `c3516e6b7091`  |
| 1547   | No file  | `c3516e6b7091`  |
| 1537   | No file  | `c3516e6b7091`  |
| 1529   | No file  | `c3516e6b7091`  |
| 1524   | No file  | `c3516e6b7091`  |
| 1519   | No file  | `c3516e6b7091`  |
| 1509   | No file  | `c3516e6b7091`  |
| 1506   | No file  | `c3516e6b7091`  |
| 1504   | No file  | `c3516e6b7091`  |
| 1500   | No file  | `c3516e6b7091`  |
| 1493   | No file  | `c3516e6b7091`  |
| 1489   | No file  | `c3516e6b7091`  |
| 1485   | No file  | `c3516e6b7091`  |
| 1481   | No file  | `c3516e6b7091`  |
| 1474   | No file  | `c3516e6b7091`  |
| 1466   | No file  | `c3516e6b7091`  |
| 1462   | No file  | `c3516e6b7091`  |
| 1459   | No file  | `c3516e6b7091`  |
| 1453   | No file  | `c3516e6b7091`  |
| 1450   | No file  | `c3516e6b7091`  |
| 1445   | No file  | `c3516e6b7091`  |
| 1439   | No file  | `c3516e6b7091`  |
| 1433   | No file  | `c3516e6b7091`  |
| 1430   | No file  | `c3516e6b7091`  |
| 1426   | No file  | `c3516e6b7091`  |
| 1421   | No file  | `c3516e6b7091`  |
| 1417   | No file  | `c3516e6b7091`  |
| 1416   | No file  | `c3516e6b7091`  |
| 1409   | No file  | `c3516e6b7091`  |
| 1405   | No file  | `c3516e6b7091`  |
| 1401   | No file  | `c3516e6b7091`  |
| 1396   | No file  | `c3516e6b7091`  |
| 1391   | No file  | `c3516e6b7091`  |
| 1390   | No file  | `c3516e6b7091`  |
| 1386   | No file  | `c3516e6b7091`  |
| 1381   | No file  | `c3516e6b7091`  |
| 1379   | No file  | `c3516e6b7091`  |
| 1372   | No file  | `c3516e6b7091`  |
| 1366   | No file  | `c3516e6b7091`  |
| 1364   | No file  | `c3516e6b7091`  |
| 1363   | No file  | `c3516e6b7091`  |
| 1360   | No file  | `c3516e6b7091`  |
| 1358   | No file  | `c3516e6b7091`  |
| 1355   | No file  | `c3516e6b7091`  |
| 1351   | No file  | `c3516e6b7091`  |
| 1348   | No file  | `c3516e6b7091`  |
| 1346   | No file  | `c3516e6b7091`  |
| 1341   | No file  | `c3516e6b7091`  |
| 1340   | No file  | `c3516e6b7091`  |
| 1338   | No file  | `c3516e6b7091`  |
| 1335   | No file  | `c3516e6b7091`  |
| 1333   | No file  | `c3516e6b7091`  |
| 1329   | No file  | `c3516e6b7091`  |
| 1327   | No file  | `c3516e6b7091`  |
| 1324   | No file  | `c3516e6b7091`  |
| 1321   | No file  | `c3516e6b7091`  |
| 1319   | No file  | `c3516e6b7091`  |
| 1318   | No file  | `c3516e6b7091`  |
| 1316   | No file  | `c3516e6b7091`  |
| 1313   | No file  | `c3516e6b7091`  |
| 1311   | No file  | `c3516e6b7091`  |
| 1309   | No file  | `c3516e6b7091`  |
| 1304   | No file  | `c3516e6b7091`  |
| 1292   | No file  | `c3516e6b7091`  |
| 1286   | No file  | `c3516e6b7091`  |
| 1280   | No file  | `c3516e6b7091`  |
| 1276   | No file  | `c3516e6b7091`  |
| 1267   | No file  | `c3516e6b7091`  |
| 1261   | No file  | `c3516e6b7091`  |
| 1256   | No file  | `c3516e6b7091`  |
| 1250   | No file  | `c3516e6b7091`  |
| 1246   | No file  | `c3516e6b7091`  |
| 1239   | No file  | `c3516e6b7091`  |
| 1230   | No file  | `c3516e6b7091`  |
| 1226   | No file  | `c3516e6b7091`  |
| 1220   | No file  | `c3516e6b7091`  |
| 1217   | No file  | `c3516e6b7091`  |
| 1211   | No file  | `c3516e6b7091`  |
| 1210   | No file  | `c3516e6b7091`  |
| 1208   | No file  | `c3516e6b7091`  |
| 1203   | No file  | `c3516e6b7091`  |
| 1197   | No file  | `c3516e6b7091`  |
| 1194   | No file  | `c3516e6b7091`  |
| 1192   | No file  | `c3516e6b7091`  |
| 1187   | No file  | `c3516e6b7091`  |
| 1183   | No file  | `c3516e6b7091`  |
| 1177   | No file  | `c3516e6b7091`  |
| 1173   | No file  | `c3516e6b7091`  |
| 1167   | No file  | `c3516e6b7091`  |
| 1164   | No file  | `c3516e6b7091`  |
| 1156   | No file  | `c3516e6b7091`  |
| 1149   | No file  | `c3516e6b7091`  |
| 1144   | No file  | `c3516e6b7091`  |
| 1137   | No file  | `c3516e6b7091`  |
| 1132   | No file  | `c3516e6b7091`  |
| 1127   | No file  | `c3516e6b7091`  |
| 1122   | No file  | `c3516e6b7091`  |
| 1118   | No file  | `c3516e6b7091`  |
| 1114   | No file  | `c3516e6b7091`  |
| 1109   | No file  | `c3516e6b7091`  |
| 1102   | No file  | `c3516e6b7091`  |
| 1096   | No file  | `c3516e6b7091`  |
| 1088   | No file  | `c3516e6b7091`  |
| 1081   | No file  | `c3516e6b7091`  |
| 1076   | No file  | `c3516e6b7091`  |
| 1069   | No file  | `c3516e6b7091`  |
| 1064   | No file  | `c3516e6b7091`  |
| 1058   | No file  | `c3516e6b7091`  |
| 1051   | No file  | `c3516e6b7091`  |
| 1044   | No file  | `c3516e6b7091`  |
| 1036   | No file  | `c3516e6b7091`  |
| 1026   | No file  | `c3516e6b7091`  |
| 1016   | No file  | `c3516e6b7091`  |
| 1009   | No file  | `c3516e6b7091`  |
| 1005   | No file  | `c3516e6b7091`  |
| 1000   | No file  | `c3516e6b7091`  |
| 998    | No file  | `c3516e6b7091`  |
| 990    | No file  | `c3516e6b7091`  |
| 979    | No file  | `c3516e6b7091`  |
| 972    | No file  | `c3516e6b7091`  |
| 963    | No file  | `c3516e6b7091`  |
| 955    | No file  | `c3516e6b7091`  |
| 946    | No file  | `c3516e6b7091`  |
| 938    | No file  | `c3516e6b7091`  |
| 927    | No file  | `c3516e6b7091`  |
| 911    | No file  | `c3516e6b7091`  |
| 904    | No file  | `c3516e6b7091`  |
| 899    | No file  | `c3516e6b7091`  |
| 894    | No file  | `c3516e6b7091`  |
| 885    | No file  | `c3516e6b7091`  |
| 879    | No file  | `c3516e6b7091`  |
| 872    | No file  | `c3516e6b7091`  |
| 864    | No file  | `c3516e6b7091`  |
| 855    | No file  | `c3516e6b7091`  |
| 853    | No file  | `c3516e6b7091`  |
| 845    | No file  | `c3516e6b7091`  |
| 837    | No file  | `c3516e6b7091`  |
| 829    | No file  | `c3516e6b7091`  |
| 822    | No file  | `c3516e6b7091`  |
| 814    | No file  | `c3516e6b7091`  |
| 805    | No file  | `c3516e6b7091`  |
| 794    | No file  | `c3516e6b7091`  |
| 787    | No file  | `c3516e6b7091`  |
| 780    | No file  | `c3516e6b7091`  |
| 771    | No file  | `c3516e6b7091`  |
| 760    | No file  | `c3516e6b7091`  |
| 748    | No file  | `c3516e6b7091`  |
| 741    | No file  | `c3516e6b7091`  |
| 736    | No file  | `c3516e6b7091`  |
| 731    | No file  | `c3516e6b7091`  |
| 723    | No file  | `c3516e6b7091`  |
| 711    | No file  | `c3516e6b7091`  |
| 707    | No file  | `c3516e6b7091`  |
| 697    | No file  | `c3516e6b7091`  |
| 689    | No file  | `c3516e6b7091`  |
| 683    | No file  | `c3516e6b7091`  |
| 678    | No file  | `c3516e6b7091`  |
| 670    | No file  | `c3516e6b7091`  |
| 661    | No file  | `c3516e6b7091`  |
| 656    | No file  | `c3516e6b7091`  |
| 652    | No file  | `c3516e6b7091`  |
| 643    | No file  | `c3516e6b7091`  |
| 637    | No file  | `c3516e6b7091`  |
| 630    | No file  | `c3516e6b7091`  |
| 627    | No file  | `c3516e6b7091`  |
| 621    | No file  | `c3516e6b7091`  |
| 617    | No file  | `c3516e6b7091`  |
| 615    | No file  | `c3516e6b7091`  |
| 606    | No file  | `c3516e6b7091`  |
| 599    | No file  | `c3516e6b7091`  |
| 592    | No file  | `c3516e6b7091`  |
| 586    | No file  | `c3516e6b7091`  |
| 577    | No file  | `c3516e6b7091`  |
| 569    | No file  | `c3516e6b7091`  |
| 561    | No file  | `c3516e6b7091`  |
| 554    | No file  | `c3516e6b7091`  |
| 542    | No file  | `c3516e6b7091`  |
| 532    | No file  | `c3516e6b7091`  |
| 531    | No file  | `c3516e6b7091`  |
| 526    | No file  | `c3516e6b7091`  |
| 521    | No file  | `c3516e6b7091`  |
| 517    | No file  | `c3516e6b7091`  |
| 510    | No file  | `c3516e6b7091`  |
| 508    | No file  | `c3516e6b7091`  |
| 504    | No file  | `c3516e6b7091`  |
| 497    | No file  | `c3516e6b7091`  |
| 491    | No file  | `c3516e6b7091`  |
| 485    | No file  | `c3516e6b7091`  |
| 478    | No file  | `c3516e6b7091`  |
| 472    | No file  | `c3516e6b7091`  |
| 466    | No file  | `c3516e6b7091`  |
| 457    | No file  | `c3516e6b7091`  |
| 452    | No file  | `c3516e6b7091`  |
| 449    | No file  | `c3516e6b7091`  |
| 435    | No file  | `c3516e6b7091`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                      |
| ------- | ---- | ------------- | ---------------------------------------------------------- |
| `+0x00` | u16  | character_key | `characterstatic.dbss` key of the siege object; one row each |
| `+0x02` | u32  | object_point  | Liberation points of the object; `1` to `150` on client 3482 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `MajorSiegeLiberationObjectPoint` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `CharacterKey` and
`MajorSiegeObjectPoint`, and its 25 rows match the 25 rows of the
client 1784 file by key and value (25 of 25). `object_point` is
`MajorSiegeObjectPoint`; the sheet's `#CharacterKeyName` note column
names the keys `[길드] 점령전 바리케이드` ([Guild] Conquest War
barricade) and the other Conquest War buildings.

## Notes

- The rows are not sorted by key.
- Clients 1784 to 2765 have 25 rows (170 bytes); client 3002 and later have 71,
  adding keys in the `12797` to `12841` and `62403` to `62418` ranges
  that repeat the building names of the first 25. Client 3482 rates many objects lower than
  client 1784: the Medium Siege Tower Factory `2049` is worth `15`
  there and `50` on client 1784, the Big Hwacha `31078` `40` and `100`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/majorsiege_tables.py`:
  the character key with its name, and the points.
