# `siegeoccupycolor.bss` Format

## Purpose

A numbered colour palette for sieges ("occupy colour"): rows of an index
counting up from `1` and a four-byte colour. Client 3482 has 90 rows, all
colours unique and fully opaque. What the client paints with them is
open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------- | --------- |
| 1      | 1519 and later | 3483    | `siegeoccupycolor.bss` | 740   | 90 Row  | 8         |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `siegeoccupycolor.bss` | 740 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `359edc2e5e19`  |
| 3482   | Layout 1 | `359edc2e5e19`  |
| 3474   | Layout 1 | `359edc2e5e19`  |
| 3473   | Layout 1 | `359edc2e5e19`  |
| 3464   | Layout 1 | `359edc2e5e19`  |
| 3458   | Layout 1 | `359edc2e5e19`  |
| 3454   | Layout 1 | `359edc2e5e19`  |
| 3444   | Layout 1 | `359edc2e5e19`  |
| 3435   | Layout 1 | `359edc2e5e19`  |
| 3426   | Layout 1 | `359edc2e5e19`  |
| 3418   | Layout 1 | `359edc2e5e19`  |
| 3412   | Layout 1 | `359edc2e5e19`  |
| 3402   | Layout 1 | `359edc2e5e19`  |
| 3396   | Layout 1 | `359edc2e5e19`  |
| 3387   | Layout 1 | `359edc2e5e19`  |
| 3381   | Layout 1 | `359edc2e5e19`  |
| 3373   | Layout 1 | `359edc2e5e19`  |
| 3364   | Layout 1 | `359edc2e5e19`  |
| 3356   | Layout 1 | `359edc2e5e19`  |
| 3349   | Layout 1 | `359edc2e5e19`  |
| 3342   | Layout 1 | `359edc2e5e19`  |
| 3335   | Layout 1 | `359edc2e5e19`  |
| 3326   | Layout 1 | `359edc2e5e19`  |
| 3321   | Layout 1 | `359edc2e5e19`  |
| 3314   | Layout 1 | `359edc2e5e19`  |
| 3303   | Layout 1 | `359edc2e5e19`  |
| 3302   | Layout 1 | `359edc2e5e19`  |
| 3293   | Layout 1 | `359edc2e5e19`  |
| 3283   | Layout 1 | `359edc2e5e19`  |
| 3275   | Layout 1 | `359edc2e5e19`  |
| 3267   | Layout 1 | `359edc2e5e19`  |
| 3258   | Layout 1 | `359edc2e5e19`  |
| 3251   | Layout 1 | `359edc2e5e19`  |
| 3242   | Layout 1 | `359edc2e5e19`  |
| 3235   | Layout 1 | `359edc2e5e19`  |
| 3229   | Layout 1 | `359edc2e5e19`  |
| 3212   | Layout 1 | `359edc2e5e19`  |
| 3203   | Layout 1 | `359edc2e5e19`  |
| 3193   | Layout 1 | `359edc2e5e19`  |
| 3186   | Layout 1 | `359edc2e5e19`  |
| 3177   | Layout 1 | `359edc2e5e19`  |
| 3169   | Layout 1 | `359edc2e5e19`  |
| 3158   | Layout 1 | `359edc2e5e19`  |
| 3151   | Layout 1 | `359edc2e5e19`  |
| 3144   | Layout 1 | `359edc2e5e19`  |
| 3133   | Layout 1 | `359edc2e5e19`  |
| 3125   | Layout 1 | `359edc2e5e19`  |
| 3118   | Layout 1 | `359edc2e5e19`  |
| 3111   | Layout 1 | `359edc2e5e19`  |
| 3103   | Layout 1 | `359edc2e5e19`  |
| 3095   | Layout 1 | `359edc2e5e19`  |
| 3086   | Layout 1 | `359edc2e5e19`  |
| 3072   | Layout 1 | `359edc2e5e19`  |
| 3062   | Layout 1 | `359edc2e5e19`  |
| 3052   | Layout 1 | `359edc2e5e19`  |
| 3045   | Layout 1 | `359edc2e5e19`  |
| 3037   | Layout 1 | `359edc2e5e19`  |
| 3030   | Layout 1 | `359edc2e5e19`  |
| 3021   | Layout 1 | `359edc2e5e19`  |
| 3012   | Layout 1 | `359edc2e5e19`  |
| 3002   | Layout 1 | `359edc2e5e19`  |
| 2995   | Layout 1 | `359edc2e5e19`  |
| 2987   | Layout 1 | `359edc2e5e19`  |
| 2978   | Layout 1 | `359edc2e5e19`  |
| 2970   | Layout 1 | `359edc2e5e19`  |
| 2959   | Layout 1 | `359edc2e5e19`  |
| 2951   | Layout 1 | `359edc2e5e19`  |
| 2942   | Layout 1 | `359edc2e5e19`  |
| 2935   | Layout 1 | `359edc2e5e19`  |
| 2932   | Layout 1 | `359edc2e5e19`  |
| 2923   | Layout 1 | `359edc2e5e19`  |
| 2919   | Layout 1 | `359edc2e5e19`  |
| 2907   | Layout 1 | `359edc2e5e19`  |
| 2900   | Layout 1 | `359edc2e5e19`  |
| 2891   | Layout 1 | `359edc2e5e19`  |
| 2882   | Layout 1 | `359edc2e5e19`  |
| 2872   | Layout 1 | `359edc2e5e19`  |
| 2863   | Layout 1 | `359edc2e5e19`  |
| 2855   | Layout 1 | `359edc2e5e19`  |
| 2849   | Layout 1 | `359edc2e5e19`  |
| 2844   | Layout 1 | `359edc2e5e19`  |
| 2834   | Layout 1 | `359edc2e5e19`  |
| 2825   | Layout 1 | `359edc2e5e19`  |
| 2819   | Layout 1 | `359edc2e5e19`  |
| 2811   | Layout 1 | `359edc2e5e19`  |
| 2803   | Layout 1 | `359edc2e5e19`  |
| 2794   | Layout 1 | `359edc2e5e19`  |
| 2783   | Layout 1 | `359edc2e5e19`  |
| 2774   | Layout 1 | `359edc2e5e19`  |
| 2765   | Layout 1 | `359edc2e5e19`  |
| 2756   | Layout 1 | `359edc2e5e19`  |
| 2750   | Layout 1 | `359edc2e5e19`  |
| 2743   | Layout 1 | `359edc2e5e19`  |
| 2736   | Layout 1 | `359edc2e5e19`  |
| 2726   | Layout 1 | `359edc2e5e19`  |
| 2717   | Layout 1 | `359edc2e5e19`  |
| 2709   | Layout 1 | `359edc2e5e19`  |
| 2703   | Layout 1 | `359edc2e5e19`  |
| 2695   | Layout 1 | `359edc2e5e19`  |
| 2684   | Layout 1 | `359edc2e5e19`  |
| 2672   | Layout 1 | `359edc2e5e19`  |
| 2665   | Layout 1 | `359edc2e5e19`  |
| 2657   | Layout 1 | `359edc2e5e19`  |
| 2649   | Layout 1 | `359edc2e5e19`  |
| 2644   | Layout 1 | `359edc2e5e19`  |
| 2637   | Layout 1 | `359edc2e5e19`  |
| 2629   | Layout 1 | `359edc2e5e19`  |
| 2619   | Layout 1 | `359edc2e5e19`  |
| 2612   | Layout 1 | `359edc2e5e19`  |
| 2606   | Layout 1 | `359edc2e5e19`  |
| 2602   | Layout 1 | `359edc2e5e19`  |
| 2601   | Layout 1 | `359edc2e5e19`  |
| 2592   | Layout 1 | `359edc2e5e19`  |
| 2583   | Layout 1 | `359edc2e5e19`  |
| 2575   | Layout 1 | `359edc2e5e19`  |
| 2567   | Layout 1 | `359edc2e5e19`  |
| 2560   | Layout 1 | `359edc2e5e19`  |
| 2553   | Layout 1 | `359edc2e5e19`  |
| 2545   | Layout 1 | `359edc2e5e19`  |
| 2538   | Layout 1 | `359edc2e5e19`  |
| 2529   | Layout 1 | `359edc2e5e19`  |
| 2519   | Layout 1 | `359edc2e5e19`  |
| 2513   | Layout 1 | `359edc2e5e19`  |
| 2510   | Layout 1 | `359edc2e5e19`  |
| 2507   | Layout 1 | `359edc2e5e19`  |
| 2503   | Layout 1 | `359edc2e5e19`  |
| 2498   | Layout 1 | `359edc2e5e19`  |
| 2492   | Layout 1 | `359edc2e5e19`  |
| 2487   | Layout 1 | `359edc2e5e19`  |
| 2480   | Layout 1 | `359edc2e5e19`  |
| 2474   | Layout 1 | `359edc2e5e19`  |
| 2468   | Layout 1 | `359edc2e5e19`  |
| 2460   | Layout 1 | `359edc2e5e19`  |
| 2453   | Layout 1 | `359edc2e5e19`  |
| 2444   | Layout 1 | `359edc2e5e19`  |
| 2438   | Layout 1 | `359edc2e5e19`  |
| 2434   | Layout 1 | `359edc2e5e19`  |
| 2429   | Layout 1 | `359edc2e5e19`  |
| 2421   | Layout 1 | `359edc2e5e19`  |
| 2414   | Layout 1 | `359edc2e5e19`  |
| 2407   | Layout 1 | `359edc2e5e19`  |
| 2401   | Layout 1 | `359edc2e5e19`  |
| 2397   | Layout 1 | `359edc2e5e19`  |
| 2393   | Layout 1 | `359edc2e5e19`  |
| 2384   | Layout 1 | `359edc2e5e19`  |
| 2378   | Layout 1 | `359edc2e5e19`  |
| 2372   | Layout 1 | `359edc2e5e19`  |
| 2358   | Layout 1 | `359edc2e5e19`  |
| 2352   | Layout 1 | `359edc2e5e19`  |
| 2347   | Layout 1 | `359edc2e5e19`  |
| 2343   | Layout 1 | `359edc2e5e19`  |
| 2335   | Layout 1 | `359edc2e5e19`  |
| 2327   | Layout 1 | `359edc2e5e19`  |
| 2324   | Layout 1 | `359edc2e5e19`  |
| 2319   | Layout 1 | `359edc2e5e19`  |
| 2313   | Layout 1 | `359edc2e5e19`  |
| 2308   | Layout 1 | `359edc2e5e19`  |
| 2302   | Layout 1 | `359edc2e5e19`  |
| 2295   | Layout 1 | `359edc2e5e19`  |
| 2290   | Layout 1 | `359edc2e5e19`  |
| 2284   | Layout 1 | `359edc2e5e19`  |
| 2276   | Layout 1 | `359edc2e5e19`  |
| 2269   | Layout 1 | `359edc2e5e19`  |
| 2259   | Layout 1 | `359edc2e5e19`  |
| 2250   | Layout 1 | `359edc2e5e19`  |
| 2243   | Layout 1 | `359edc2e5e19`  |
| 2235   | Layout 1 | `359edc2e5e19`  |
| 2229   | Layout 1 | `359edc2e5e19`  |
| 2224   | Layout 1 | `359edc2e5e19`  |
| 2218   | Layout 1 | `359edc2e5e19`  |
| 2215   | Layout 1 | `359edc2e5e19`  |
| 2207   | Layout 1 | `359edc2e5e19`  |
| 2203   | Layout 1 | `359edc2e5e19`  |
| 2196   | Layout 1 | `359edc2e5e19`  |
| 2192   | Layout 1 | `359edc2e5e19`  |
| 2189   | Layout 1 | `359edc2e5e19`  |
| 2183   | Layout 1 | `359edc2e5e19`  |
| 2179   | Layout 1 | `359edc2e5e19`  |
| 2171   | Layout 1 | `359edc2e5e19`  |
| 2163   | Layout 1 | `359edc2e5e19`  |
| 2156   | Layout 1 | `359edc2e5e19`  |
| 2151   | Layout 1 | `359edc2e5e19`  |
| 2147   | Layout 1 | `359edc2e5e19`  |
| 2142   | Layout 1 | `359edc2e5e19`  |
| 2138   | Layout 1 | `359edc2e5e19`  |
| 2134   | Layout 1 | `359edc2e5e19`  |
| 2130   | Layout 1 | `359edc2e5e19`  |
| 2122   | Layout 1 | `359edc2e5e19`  |
| 2107   | Layout 1 | `359edc2e5e19`  |
| 2098   | Layout 1 | `359edc2e5e19`  |
| 2089   | Layout 1 | `359edc2e5e19`  |
| 2081   | Layout 1 | `359edc2e5e19`  |
| 2073   | Layout 1 | `359edc2e5e19`  |
| 2067   | Layout 1 | `359edc2e5e19`  |
| 2063   | Layout 1 | `359edc2e5e19`  |
| 2059   | Layout 1 | `359edc2e5e19`  |
| 2052   | Layout 1 | `359edc2e5e19`  |
| 2044   | Layout 1 | `359edc2e5e19`  |
| 2039   | Layout 1 | `359edc2e5e19`  |
| 2032   | Layout 1 | `359edc2e5e19`  |
| 2025   | Layout 1 | `359edc2e5e19`  |
| 2011   | Layout 1 | `359edc2e5e19`  |
| 2005   | Layout 1 | `359edc2e5e19`  |
| 2000   | Layout 1 | `359edc2e5e19`  |
| 1996   | Layout 1 | `359edc2e5e19`  |
| 1991   | Layout 1 | `359edc2e5e19`  |
| 1985   | Layout 1 | `359edc2e5e19`  |
| 1980   | Layout 1 | `359edc2e5e19`  |
| 1969   | Layout 1 | `359edc2e5e19`  |
| 1964   | Layout 1 | `359edc2e5e19`  |
| 1958   | Layout 1 | `359edc2e5e19`  |
| 1950   | Layout 1 | `359edc2e5e19`  |
| 1945   | Layout 1 | `359edc2e5e19`  |
| 1937   | Layout 1 | `359edc2e5e19`  |
| 1933   | Layout 1 | `359edc2e5e19`  |
| 1927   | Layout 1 | `359edc2e5e19`  |
| 1921   | Layout 1 | `359edc2e5e19`  |
| 1914   | Layout 1 | `359edc2e5e19`  |
| 1908   | Layout 1 | `359edc2e5e19`  |
| 1897   | Layout 1 | `359edc2e5e19`  |
| 1892   | Layout 1 | `359edc2e5e19`  |
| 1886   | Layout 1 | `359edc2e5e19`  |
| 1881   | Layout 1 | `359edc2e5e19`  |
| 1871   | Layout 1 | `359edc2e5e19`  |
| 1866   | Layout 1 | `359edc2e5e19`  |
| 1862   | Layout 1 | `359edc2e5e19`  |
| 1854   | Layout 1 | `359edc2e5e19`  |
| 1846   | Layout 1 | `359edc2e5e19`  |
| 1838   | Layout 1 | `359edc2e5e19`  |
| 1832   | Layout 1 | `359edc2e5e19`  |
| 1826   | Layout 1 | `359edc2e5e19`  |
| 1822   | Layout 1 | `359edc2e5e19`  |
| 1818   | Layout 1 | `359edc2e5e19`  |
| 1804   | Layout 1 | `359edc2e5e19`  |
| 1794   | Layout 1 | `359edc2e5e19`  |
| 1790   | Layout 1 | `359edc2e5e19`  |
| 1784   | Layout 1 | `359edc2e5e19`  |
| 1774   | Layout 1 | `359edc2e5e19`  |
| 1771   | Layout 1 | `359edc2e5e19`  |
| 1762   | Layout 1 | `359edc2e5e19`  |
| 1759   | Layout 1 | `359edc2e5e19`  |
| 1754   | Layout 1 | `359edc2e5e19`  |
| 1749   | Layout 1 | `359edc2e5e19`  |
| 1743   | Layout 1 | `359edc2e5e19`  |
| 1737   | Layout 1 | `359edc2e5e19`  |
| 1731   | Layout 1 | `359edc2e5e19`  |
| 1725   | Layout 1 | `359edc2e5e19`  |
| 1717   | Layout 1 | `359edc2e5e19`  |
| 1710   | Layout 1 | `359edc2e5e19`  |
| 1704   | Layout 1 | `359edc2e5e19`  |
| 1698   | Layout 1 | `359edc2e5e19`  |
| 1690   | Layout 1 | `359edc2e5e19`  |
| 1685   | Layout 1 | `359edc2e5e19`  |
| 1680   | Layout 1 | `359edc2e5e19`  |
| 1674   | Layout 1 | `359edc2e5e19`  |
| 1668   | Layout 1 | `359edc2e5e19`  |
| 1659   | Layout 1 | `359edc2e5e19`  |
| 1649   | Layout 1 | `359edc2e5e19`  |
| 1642   | Layout 1 | `359edc2e5e19`  |
| 1636   | Layout 1 | `359edc2e5e19`  |
| 1628   | Layout 1 | `359edc2e5e19`  |
| 1622   | Layout 1 | `359edc2e5e19`  |
| 1614   | Layout 1 | `359edc2e5e19`  |
| 1608   | Layout 1 | `359edc2e5e19`  |
| 1602   | Layout 1 | `359edc2e5e19`  |
| 1598   | Layout 1 | `359edc2e5e19`  |
| 1594   | Layout 1 | `359edc2e5e19`  |
| 1590   | Layout 1 | `359edc2e5e19`  |
| 1587   | Layout 1 | `359edc2e5e19`  |
| 1584   | Layout 1 | `359edc2e5e19`  |
| 1579   | Layout 1 | `359edc2e5e19`  |
| 1572   | Layout 1 | `359edc2e5e19`  |
| 1565   | Layout 1 | `359edc2e5e19`  |
| 1559   | Layout 1 | `359edc2e5e19`  |
| 1554   | Layout 1 | `359edc2e5e19`  |
| 1547   | Layout 1 | `359edc2e5e19`  |
| 1537   | Layout 1 | `359edc2e5e19`  |
| 1529   | Layout 1 | `359edc2e5e19`  |
| 1524   | Layout 1 | `359edc2e5e19`  |
| 1519   | Layout 1 | `359edc2e5e19`  |
| 1509   | No file  | `359edc2e5e19`  |
| 1506   | No file  | `359edc2e5e19`  |
| 1504   | No file  | `359edc2e5e19`  |
| 1500   | No file  | `359edc2e5e19`  |
| 1493   | No file  | `359edc2e5e19`  |
| 1489   | No file  | `359edc2e5e19`  |
| 1485   | No file  | `359edc2e5e19`  |
| 1481   | No file  | `359edc2e5e19`  |
| 1474   | No file  | `359edc2e5e19`  |
| 1466   | No file  | `359edc2e5e19`  |
| 1462   | No file  | `359edc2e5e19`  |
| 1459   | No file  | `359edc2e5e19`  |
| 1453   | No file  | `359edc2e5e19`  |
| 1450   | No file  | `359edc2e5e19`  |
| 1445   | No file  | `359edc2e5e19`  |
| 1439   | No file  | `359edc2e5e19`  |
| 1433   | No file  | `359edc2e5e19`  |
| 1430   | No file  | `359edc2e5e19`  |
| 1426   | No file  | `359edc2e5e19`  |
| 1421   | No file  | `359edc2e5e19`  |
| 1417   | No file  | `359edc2e5e19`  |
| 1416   | No file  | `359edc2e5e19`  |
| 1409   | No file  | `359edc2e5e19`  |
| 1405   | No file  | `359edc2e5e19`  |
| 1401   | No file  | `359edc2e5e19`  |
| 1396   | No file  | `359edc2e5e19`  |
| 1391   | No file  | `359edc2e5e19`  |
| 1390   | No file  | `359edc2e5e19`  |
| 1386   | No file  | `359edc2e5e19`  |
| 1381   | No file  | `359edc2e5e19`  |
| 1379   | No file  | `359edc2e5e19`  |
| 1372   | No file  | `359edc2e5e19`  |
| 1366   | No file  | `359edc2e5e19`  |
| 1364   | No file  | `359edc2e5e19`  |
| 1363   | No file  | `359edc2e5e19`  |
| 1360   | No file  | `359edc2e5e19`  |
| 1358   | No file  | `359edc2e5e19`  |
| 1355   | No file  | `359edc2e5e19`  |
| 1351   | No file  | `359edc2e5e19`  |
| 1348   | No file  | `359edc2e5e19`  |
| 1346   | No file  | `359edc2e5e19`  |
| 1341   | No file  | `359edc2e5e19`  |
| 1340   | No file  | `359edc2e5e19`  |
| 1338   | No file  | `359edc2e5e19`  |
| 1335   | No file  | `359edc2e5e19`  |
| 1333   | No file  | `359edc2e5e19`  |
| 1329   | No file  | `359edc2e5e19`  |
| 1327   | No file  | `359edc2e5e19`  |
| 1324   | No file  | `359edc2e5e19`  |
| 1321   | No file  | `359edc2e5e19`  |
| 1319   | No file  | `359edc2e5e19`  |
| 1318   | No file  | `359edc2e5e19`  |
| 1316   | No file  | `359edc2e5e19`  |
| 1313   | No file  | `359edc2e5e19`  |
| 1311   | No file  | `359edc2e5e19`  |
| 1309   | No file  | `359edc2e5e19`  |
| 1304   | No file  | `359edc2e5e19`  |
| 1292   | No file  | `359edc2e5e19`  |
| 1286   | No file  | `359edc2e5e19`  |
| 1280   | No file  | `359edc2e5e19`  |
| 1276   | No file  | `359edc2e5e19`  |
| 1267   | No file  | `359edc2e5e19`  |
| 1261   | No file  | `359edc2e5e19`  |
| 1256   | No file  | `359edc2e5e19`  |
| 1250   | No file  | `359edc2e5e19`  |
| 1246   | No file  | `359edc2e5e19`  |
| 1239   | No file  | `359edc2e5e19`  |
| 1230   | No file  | `359edc2e5e19`  |
| 1226   | No file  | `359edc2e5e19`  |
| 1220   | No file  | `359edc2e5e19`  |
| 1217   | No file  | `359edc2e5e19`  |
| 1211   | No file  | `359edc2e5e19`  |
| 1210   | No file  | `359edc2e5e19`  |
| 1208   | No file  | `359edc2e5e19`  |
| 1203   | No file  | `359edc2e5e19`  |
| 1197   | No file  | `359edc2e5e19`  |
| 1194   | No file  | `359edc2e5e19`  |
| 1192   | No file  | `359edc2e5e19`  |
| 1187   | No file  | `359edc2e5e19`  |
| 1183   | No file  | `359edc2e5e19`  |
| 1177   | No file  | `359edc2e5e19`  |
| 1173   | No file  | `359edc2e5e19`  |
| 1167   | No file  | `359edc2e5e19`  |
| 1164   | No file  | `359edc2e5e19`  |
| 1156   | No file  | `359edc2e5e19`  |
| 1149   | No file  | `359edc2e5e19`  |
| 1144   | No file  | `359edc2e5e19`  |
| 1137   | No file  | `359edc2e5e19`  |
| 1132   | No file  | `359edc2e5e19`  |
| 1127   | No file  | `359edc2e5e19`  |
| 1122   | No file  | `359edc2e5e19`  |
| 1118   | No file  | `359edc2e5e19`  |
| 1114   | No file  | `359edc2e5e19`  |
| 1109   | No file  | `359edc2e5e19`  |
| 1102   | No file  | `359edc2e5e19`  |
| 1096   | No file  | `359edc2e5e19`  |
| 1088   | No file  | `359edc2e5e19`  |
| 1081   | No file  | `359edc2e5e19`  |
| 1076   | No file  | `359edc2e5e19`  |
| 1069   | No file  | `359edc2e5e19`  |
| 1064   | No file  | `359edc2e5e19`  |
| 1058   | No file  | `359edc2e5e19`  |
| 1051   | No file  | `359edc2e5e19`  |
| 1044   | No file  | `359edc2e5e19`  |
| 1036   | No file  | `359edc2e5e19`  |
| 1026   | No file  | `359edc2e5e19`  |
| 1016   | No file  | `359edc2e5e19`  |
| 1009   | No file  | `359edc2e5e19`  |
| 1005   | No file  | `359edc2e5e19`  |
| 1000   | No file  | `359edc2e5e19`  |
| 998    | No file  | `359edc2e5e19`  |
| 990    | No file  | `359edc2e5e19`  |
| 979    | No file  | `359edc2e5e19`  |
| 972    | No file  | `359edc2e5e19`  |
| 963    | No file  | `359edc2e5e19`  |
| 955    | No file  | `359edc2e5e19`  |
| 946    | No file  | `359edc2e5e19`  |
| 938    | No file  | `359edc2e5e19`  |
| 927    | No file  | `359edc2e5e19`  |
| 911    | No file  | `359edc2e5e19`  |
| 904    | No file  | `359edc2e5e19`  |
| 899    | No file  | `359edc2e5e19`  |
| 894    | No file  | `359edc2e5e19`  |
| 885    | No file  | `359edc2e5e19`  |
| 879    | No file  | `359edc2e5e19`  |
| 872    | No file  | `359edc2e5e19`  |
| 864    | No file  | `359edc2e5e19`  |
| 855    | No file  | `359edc2e5e19`  |
| 853    | No file  | `359edc2e5e19`  |
| 845    | No file  | `359edc2e5e19`  |
| 837    | No file  | `359edc2e5e19`  |
| 829    | No file  | `359edc2e5e19`  |
| 822    | No file  | `359edc2e5e19`  |
| 814    | No file  | `359edc2e5e19`  |
| 805    | No file  | `359edc2e5e19`  |
| 794    | No file  | `359edc2e5e19`  |
| 787    | No file  | `359edc2e5e19`  |
| 780    | No file  | `359edc2e5e19`  |
| 771    | No file  | `359edc2e5e19`  |
| 760    | No file  | `359edc2e5e19`  |
| 748    | No file  | `359edc2e5e19`  |
| 741    | No file  | `359edc2e5e19`  |
| 736    | No file  | `359edc2e5e19`  |
| 731    | No file  | `359edc2e5e19`  |
| 723    | No file  | `359edc2e5e19`  |
| 711    | No file  | `359edc2e5e19`  |
| 707    | No file  | `359edc2e5e19`  |
| 697    | No file  | `359edc2e5e19`  |
| 689    | No file  | `359edc2e5e19`  |
| 683    | No file  | `359edc2e5e19`  |
| 678    | No file  | `359edc2e5e19`  |
| 670    | No file  | `359edc2e5e19`  |
| 661    | No file  | `359edc2e5e19`  |
| 656    | No file  | `359edc2e5e19`  |
| 652    | No file  | `359edc2e5e19`  |
| 643    | No file  | `359edc2e5e19`  |
| 637    | No file  | `359edc2e5e19`  |
| 630    | No file  | `359edc2e5e19`  |
| 627    | No file  | `359edc2e5e19`  |
| 621    | No file  | `359edc2e5e19`  |
| 617    | No file  | `359edc2e5e19`  |
| 615    | No file  | `359edc2e5e19`  |
| 606    | No file  | `359edc2e5e19`  |
| 599    | No file  | `359edc2e5e19`  |
| 592    | No file  | `359edc2e5e19`  |
| 586    | No file  | `359edc2e5e19`  |
| 577    | No file  | `359edc2e5e19`  |
| 569    | No file  | `359edc2e5e19`  |
| 561    | No file  | `359edc2e5e19`  |
| 554    | No file  | `359edc2e5e19`  |
| 542    | No file  | `359edc2e5e19`  |
| 532    | No file  | `359edc2e5e19`  |
| 531    | No file  | `359edc2e5e19`  |
| 526    | No file  | `359edc2e5e19`  |
| 521    | No file  | `359edc2e5e19`  |
| 517    | No file  | `359edc2e5e19`  |
| 510    | No file  | `359edc2e5e19`  |
| 508    | No file  | `359edc2e5e19`  |
| 504    | No file  | `359edc2e5e19`  |
| 497    | No file  | `359edc2e5e19`  |
| 491    | No file  | `359edc2e5e19`  |
| 485    | No file  | `359edc2e5e19`  |
| 478    | No file  | `359edc2e5e19`  |
| 472    | No file  | `359edc2e5e19`  |
| 466    | No file  | `359edc2e5e19`  |
| 457    | No file  | `359edc2e5e19`  |
| 452    | No file  | `359edc2e5e19`  |
| 449    | No file  | `359edc2e5e19`  |
| 435    | No file  | `359edc2e5e19`  |

<!-- versions:end -->

## Companion Files

None. The handler reads only this file.

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

### Row (8 bytes)

| Offset  | Type     | Field | Notes                                                                    |
| ------- | -------- | ----- | ------------------------------------------------------------------------ |
| `+0x00` | u32      | index | `1` to `row_count` in file order                                         |
| `+0x04` | bytes[4] | color | Stored blue, green, red, alpha; alpha `ff` on every row of client 3482   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
these rows. That server's dump (client 1784) names the loader
`GameCommonParameterLoaderFromExcel::loadMain(loadSiegeOccupyColor)`, the
table `SiegeOccupyColorStaticStatusManager` and the two members
`SiegeOccupyColorStaticStatus _index` and `SiegeOccupyColorStaticStatus
_color`, one per field of the 8-byte row.

## Notes

- Client 1784 holds the first 65 rows of client 3482 (540 bytes), each
  with the same colour; client 3482 adds indexes `66` to `90`.
- The colours are pale and mid tones (`3c3c3c` first, then `d5ffea`,
  `f3fed6`, ...), none of them in the `siegemap.bmp.rid` or
  `villagesiegemap_2024.bmp.rid` palettes.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: `color` as `aarrggbb`.

## Open Questions

### What the Colours Paint

No client Lua of client 3482 names `OccupyColor`. The name and the 90
distinct colours fit one colour per occupying guild on the node war or
conquest war map, but nothing ties an index to a guild yet.
