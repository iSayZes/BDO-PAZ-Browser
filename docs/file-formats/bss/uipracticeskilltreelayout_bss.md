# `uipracticeskilltreelayout.bss` Format

## Purpose

A skill tree grid per class for a "practice" skill window, in the cell
format of the 2016 client's skill trees. Every grid of clients 1784 and
3482 is blank: eight classes, 23 by 51 cells each, every cell of type
Blank and no skill placed. The file is the same on both clients.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                            | Bytes  | Records                  | Row bytes |
| ------ | ------------- | ------------------------------- | ------ | ------------------------ | --------- |
| 1      | 805 and later | `uipracticeskilltreelayout.bss` | 37,628 | 9,384 Cell, 8 Class Grid | 4         |

| Layout | File                            | Known             | Unknown    |
| ------ | ------------------------------- | ----------------- | ---------- |
| 1      | `uipracticeskilltreelayout.bss` | 37,628 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `a79d73a75aef`  |
| 3482   | Layout 1             | `a79d73a75aef`  |
| 3474   | Layout 1             | `a79d73a75aef`  |
| 3473   | Layout 1             | `a79d73a75aef`  |
| 3464   | Layout 1             | `a79d73a75aef`  |
| 3458   | Layout 1             | `a79d73a75aef`  |
| 3454   | Layout 1             | `a79d73a75aef`  |
| 3444   | Layout 1             | `a79d73a75aef`  |
| 3435   | Layout 1             | `a79d73a75aef`  |
| 3426   | Layout 1             | `a79d73a75aef`  |
| 3418   | Layout 1             | `a79d73a75aef`  |
| 3412   | Layout 1             | `a79d73a75aef`  |
| 3402   | Layout 1             | `a79d73a75aef`  |
| 3396   | Layout 1             | `a79d73a75aef`  |
| 3387   | Layout 1             | `a79d73a75aef`  |
| 3381   | Layout 1             | `a79d73a75aef`  |
| 3373   | Layout 1             | `a79d73a75aef`  |
| 3364   | Layout 1             | `a79d73a75aef`  |
| 3356   | Layout 1             | `a79d73a75aef`  |
| 3349   | Layout 1             | `a79d73a75aef`  |
| 3342   | Layout 1             | `a79d73a75aef`  |
| 3335   | Layout 1             | `a79d73a75aef`  |
| 3326   | Layout 1             | `a79d73a75aef`  |
| 3321   | Layout 1             | `a79d73a75aef`  |
| 3314   | Layout 1             | `a79d73a75aef`  |
| 3303   | Layout 1             | `a79d73a75aef`  |
| 3302   | Layout 1             | `a79d73a75aef`  |
| 3293   | Layout 1             | `a79d73a75aef`  |
| 3283   | Layout 1             | `a79d73a75aef`  |
| 3275   | Layout 1             | `a79d73a75aef`  |
| 3267   | Layout 1             | `a79d73a75aef`  |
| 3258   | Layout 1             | `a79d73a75aef`  |
| 3251   | Layout 1             | `a79d73a75aef`  |
| 3242   | Layout 1             | `a79d73a75aef`  |
| 3235   | Layout 1             | `a79d73a75aef`  |
| 3229   | Layout 1             | `a79d73a75aef`  |
| 3212   | Layout 1             | `a79d73a75aef`  |
| 3203   | Layout 1             | `a79d73a75aef`  |
| 3193   | Layout 1             | `a79d73a75aef`  |
| 3186   | Layout 1             | `a79d73a75aef`  |
| 3177   | Layout 1             | `a79d73a75aef`  |
| 3169   | Layout 1             | `a79d73a75aef`  |
| 3158   | Layout 1             | `a79d73a75aef`  |
| 3151   | Layout 1             | `a79d73a75aef`  |
| 3144   | Layout 1             | `a79d73a75aef`  |
| 3133   | Layout 1             | `a79d73a75aef`  |
| 3125   | Layout 1             | `a79d73a75aef`  |
| 3118   | Layout 1             | `a79d73a75aef`  |
| 3111   | Layout 1             | `a79d73a75aef`  |
| 3103   | Layout 1             | `a79d73a75aef`  |
| 3095   | Layout 1             | `a79d73a75aef`  |
| 3086   | Layout 1             | `a79d73a75aef`  |
| 3072   | Layout 1             | `a79d73a75aef`  |
| 3062   | Layout 1             | `a79d73a75aef`  |
| 3052   | Layout 1             | `a79d73a75aef`  |
| 3045   | Layout 1             | `a79d73a75aef`  |
| 3037   | Layout 1             | `a79d73a75aef`  |
| 3030   | Layout 1             | `a79d73a75aef`  |
| 3021   | Layout 1             | `a79d73a75aef`  |
| 3012   | Layout 1             | `a79d73a75aef`  |
| 3002   | Layout 1             | `a79d73a75aef`  |
| 2995   | Layout 1             | `a79d73a75aef`  |
| 2987   | Layout 1             | `a79d73a75aef`  |
| 2978   | Layout 1             | `a79d73a75aef`  |
| 2970   | Layout 1             | `a79d73a75aef`  |
| 2959   | Layout 1             | `a79d73a75aef`  |
| 2951   | Layout 1             | `a79d73a75aef`  |
| 2942   | Layout 1             | `a79d73a75aef`  |
| 2935   | Layout 1             | `a79d73a75aef`  |
| 2932   | Layout 1             | `a79d73a75aef`  |
| 2923   | Layout 1             | `a79d73a75aef`  |
| 2919   | Layout 1             | `a79d73a75aef`  |
| 2907   | Layout 1             | `a79d73a75aef`  |
| 2900   | Layout 1             | `a79d73a75aef`  |
| 2891   | Layout 1             | `a79d73a75aef`  |
| 2882   | Layout 1             | `a79d73a75aef`  |
| 2872   | Layout 1             | `a79d73a75aef`  |
| 2863   | Layout 1             | `a79d73a75aef`  |
| 2855   | Layout 1             | `a79d73a75aef`  |
| 2849   | Layout 1             | `a79d73a75aef`  |
| 2844   | Layout 1             | `a79d73a75aef`  |
| 2834   | Layout 1             | `a79d73a75aef`  |
| 2825   | Layout 1             | `a79d73a75aef`  |
| 2819   | Layout 1             | `a79d73a75aef`  |
| 2811   | Layout 1             | `a79d73a75aef`  |
| 2803   | Layout 1             | `a79d73a75aef`  |
| 2794   | Layout 1             | `a79d73a75aef`  |
| 2783   | Layout 1             | `a79d73a75aef`  |
| 2774   | Layout 1             | `a79d73a75aef`  |
| 2765   | Layout 1             | `a79d73a75aef`  |
| 2756   | Layout 1             | `a79d73a75aef`  |
| 2750   | Layout 1             | `a79d73a75aef`  |
| 2743   | Layout 1             | `a79d73a75aef`  |
| 2736   | Layout 1             | `a79d73a75aef`  |
| 2726   | Layout 1             | `a79d73a75aef`  |
| 2717   | Layout 1             | `a79d73a75aef`  |
| 2709   | Layout 1             | `a79d73a75aef`  |
| 2703   | Layout 1             | `a79d73a75aef`  |
| 2695   | Layout 1             | `a79d73a75aef`  |
| 2684   | Layout 1             | `a79d73a75aef`  |
| 2672   | Layout 1             | `a79d73a75aef`  |
| 2665   | Layout 1             | `a79d73a75aef`  |
| 2657   | Layout 1             | `a79d73a75aef`  |
| 2649   | Layout 1             | `a79d73a75aef`  |
| 2644   | Layout 1             | `a79d73a75aef`  |
| 2637   | Layout 1             | `a79d73a75aef`  |
| 2629   | Layout 1             | `a79d73a75aef`  |
| 2619   | Layout 1             | `a79d73a75aef`  |
| 2612   | Layout 1             | `a79d73a75aef`  |
| 2606   | Layout 1             | `a79d73a75aef`  |
| 2602   | Layout 1             | `a79d73a75aef`  |
| 2601   | Layout 1             | `a79d73a75aef`  |
| 2592   | Layout 1             | `a79d73a75aef`  |
| 2583   | Layout 1             | `a79d73a75aef`  |
| 2575   | Layout 1             | `a79d73a75aef`  |
| 2567   | Layout 1             | `a79d73a75aef`  |
| 2560   | Layout 1             | `a79d73a75aef`  |
| 2553   | Layout 1             | `a79d73a75aef`  |
| 2545   | Layout 1             | `a79d73a75aef`  |
| 2538   | Layout 1             | `a79d73a75aef`  |
| 2529   | Layout 1             | `a79d73a75aef`  |
| 2519   | Layout 1             | `a79d73a75aef`  |
| 2513   | Layout 1             | `a79d73a75aef`  |
| 2510   | Layout 1             | `a79d73a75aef`  |
| 2507   | Layout 1             | `a79d73a75aef`  |
| 2503   | Layout 1             | `a79d73a75aef`  |
| 2498   | Layout 1             | `a79d73a75aef`  |
| 2492   | Layout 1             | `a79d73a75aef`  |
| 2487   | Layout 1             | `a79d73a75aef`  |
| 2480   | Layout 1             | `a79d73a75aef`  |
| 2474   | Layout 1             | `a79d73a75aef`  |
| 2468   | Layout 1             | `a79d73a75aef`  |
| 2460   | Layout 1             | `a79d73a75aef`  |
| 2453   | Layout 1             | `a79d73a75aef`  |
| 2444   | Layout 1             | `a79d73a75aef`  |
| 2438   | Layout 1             | `a79d73a75aef`  |
| 2434   | Layout 1             | `a79d73a75aef`  |
| 2429   | Layout 1             | `a79d73a75aef`  |
| 2421   | Layout 1             | `a79d73a75aef`  |
| 2414   | Layout 1             | `a79d73a75aef`  |
| 2407   | Layout 1             | `a79d73a75aef`  |
| 2401   | Layout 1             | `a79d73a75aef`  |
| 2397   | Layout 1             | `a79d73a75aef`  |
| 2393   | Layout 1             | `a79d73a75aef`  |
| 2384   | Layout 1             | `a79d73a75aef`  |
| 2378   | Layout 1             | `a79d73a75aef`  |
| 2372   | Layout 1             | `a79d73a75aef`  |
| 2358   | Layout 1             | `a79d73a75aef`  |
| 2352   | Layout 1             | `a79d73a75aef`  |
| 2347   | Layout 1             | `a79d73a75aef`  |
| 2343   | Layout 1             | `a79d73a75aef`  |
| 2335   | Layout 1             | `a79d73a75aef`  |
| 2327   | Layout 1             | `a79d73a75aef`  |
| 2324   | Layout 1             | `a79d73a75aef`  |
| 2319   | Layout 1             | `a79d73a75aef`  |
| 2313   | Layout 1             | `a79d73a75aef`  |
| 2308   | Layout 1             | `a79d73a75aef`  |
| 2302   | Layout 1             | `a79d73a75aef`  |
| 2295   | Layout 1             | `a79d73a75aef`  |
| 2290   | Layout 1             | `a79d73a75aef`  |
| 2284   | Layout 1             | `a79d73a75aef`  |
| 2276   | Layout 1             | `a79d73a75aef`  |
| 2269   | Layout 1             | `a79d73a75aef`  |
| 2259   | Layout 1             | `a79d73a75aef`  |
| 2250   | Layout 1             | `a79d73a75aef`  |
| 2243   | Layout 1             | `a79d73a75aef`  |
| 2235   | Layout 1             | `a79d73a75aef`  |
| 2229   | Layout 1             | `a79d73a75aef`  |
| 2224   | Layout 1             | `a79d73a75aef`  |
| 2218   | Layout 1             | `a79d73a75aef`  |
| 2215   | Layout 1             | `a79d73a75aef`  |
| 2207   | Layout 1             | `a79d73a75aef`  |
| 2203   | Layout 1             | `a79d73a75aef`  |
| 2196   | Layout 1             | `a79d73a75aef`  |
| 2192   | Layout 1             | `a79d73a75aef`  |
| 2189   | Layout 1             | `a79d73a75aef`  |
| 2183   | Layout 1             | `a79d73a75aef`  |
| 2179   | Layout 1             | `a79d73a75aef`  |
| 2171   | Layout 1             | `a79d73a75aef`  |
| 2163   | Layout 1             | `a79d73a75aef`  |
| 2156   | Layout 1             | `a79d73a75aef`  |
| 2151   | Layout 1             | `a79d73a75aef`  |
| 2147   | Layout 1             | `a79d73a75aef`  |
| 2142   | Layout 1             | `a79d73a75aef`  |
| 2138   | Layout 1             | `a79d73a75aef`  |
| 2134   | Layout 1             | `a79d73a75aef`  |
| 2130   | Layout 1             | `a79d73a75aef`  |
| 2122   | Layout 1             | `a79d73a75aef`  |
| 2107   | Layout 1             | `a79d73a75aef`  |
| 2098   | Layout 1             | `a79d73a75aef`  |
| 2089   | Layout 1             | `a79d73a75aef`  |
| 2081   | Layout 1             | `a79d73a75aef`  |
| 2073   | Layout 1             | `a79d73a75aef`  |
| 2067   | Layout 1             | `a79d73a75aef`  |
| 2063   | Layout 1             | `a79d73a75aef`  |
| 2059   | Layout 1             | `a79d73a75aef`  |
| 2052   | Layout 1             | `a79d73a75aef`  |
| 2044   | Layout 1             | `a79d73a75aef`  |
| 2039   | Layout 1             | `a79d73a75aef`  |
| 2032   | Layout 1             | `a79d73a75aef`  |
| 2025   | Layout 1             | `a79d73a75aef`  |
| 2011   | Layout 1             | `a79d73a75aef`  |
| 2005   | Layout 1             | `a79d73a75aef`  |
| 2000   | Layout 1             | `a79d73a75aef`  |
| 1996   | Layout 1             | `a79d73a75aef`  |
| 1991   | Layout 1             | `a79d73a75aef`  |
| 1985   | Layout 1             | `a79d73a75aef`  |
| 1980   | Layout 1             | `a79d73a75aef`  |
| 1969   | Layout 1             | `a79d73a75aef`  |
| 1964   | Layout 1             | `a79d73a75aef`  |
| 1958   | Layout 1             | `a79d73a75aef`  |
| 1950   | Layout 1             | `a79d73a75aef`  |
| 1945   | Layout 1             | `a79d73a75aef`  |
| 1937   | Layout 1             | `a79d73a75aef`  |
| 1933   | Layout 1             | `a79d73a75aef`  |
| 1927   | Layout 1             | `a79d73a75aef`  |
| 1921   | Layout 1             | `a79d73a75aef`  |
| 1914   | Layout 1             | `a79d73a75aef`  |
| 1908   | Layout 1             | `a79d73a75aef`  |
| 1897   | Layout 1             | `a79d73a75aef`  |
| 1892   | Layout 1             | `a79d73a75aef`  |
| 1886   | Layout 1             | `a79d73a75aef`  |
| 1881   | Layout 1             | `a79d73a75aef`  |
| 1871   | Layout 1             | `a79d73a75aef`  |
| 1866   | Layout 1             | `a79d73a75aef`  |
| 1862   | Layout 1             | `a79d73a75aef`  |
| 1854   | Layout 1             | `a79d73a75aef`  |
| 1846   | Layout 1             | `a79d73a75aef`  |
| 1838   | Layout 1             | `a79d73a75aef`  |
| 1832   | Layout 1             | `a79d73a75aef`  |
| 1826   | Layout 1             | `a79d73a75aef`  |
| 1822   | Layout 1             | `a79d73a75aef`  |
| 1818   | Layout 1             | `a79d73a75aef`  |
| 1804   | Layout 1             | `a79d73a75aef`  |
| 1794   | Layout 1             | `a79d73a75aef`  |
| 1790   | Layout 1             | `a79d73a75aef`  |
| 1784   | Layout 1             | `a79d73a75aef`  |
| 1774   | Layout 1             | `a79d73a75aef`  |
| 1771   | Layout 1             | `a79d73a75aef`  |
| 1762   | Layout 1             | `a79d73a75aef`  |
| 1759   | Layout 1             | `a79d73a75aef`  |
| 1754   | Layout 1             | `a79d73a75aef`  |
| 1749   | Layout 1             | `a79d73a75aef`  |
| 1743   | Layout 1             | `a79d73a75aef`  |
| 1737   | Layout 1             | `a79d73a75aef`  |
| 1731   | Layout 1             | `a79d73a75aef`  |
| 1725   | Layout 1             | `a79d73a75aef`  |
| 1717   | Layout 1             | `a79d73a75aef`  |
| 1710   | Layout 1             | `a79d73a75aef`  |
| 1704   | Layout 1             | `a79d73a75aef`  |
| 1698   | Layout 1             | `a79d73a75aef`  |
| 1690   | Layout 1             | `a79d73a75aef`  |
| 1685   | Layout 1             | `a79d73a75aef`  |
| 1680   | Layout 1             | `a79d73a75aef`  |
| 1674   | Layout 1             | `a79d73a75aef`  |
| 1668   | Layout 1             | `a79d73a75aef`  |
| 1659   | Layout 1             | `a79d73a75aef`  |
| 1649   | Layout 1             | `a79d73a75aef`  |
| 1642   | Layout 1             | `a79d73a75aef`  |
| 1636   | Layout 1             | `a79d73a75aef`  |
| 1628   | Layout 1             | `a79d73a75aef`  |
| 1622   | Layout 1             | `a79d73a75aef`  |
| 1614   | Layout 1             | `a79d73a75aef`  |
| 1608   | Layout 1             | `a79d73a75aef`  |
| 1602   | Layout 1             | `a79d73a75aef`  |
| 1598   | Layout 1             | `a79d73a75aef`  |
| 1594   | Layout 1             | `a79d73a75aef`  |
| 1590   | Layout 1             | `a79d73a75aef`  |
| 1587   | Layout 1             | `a79d73a75aef`  |
| 1584   | Layout 1             | `a79d73a75aef`  |
| 1579   | Layout 1             | `a79d73a75aef`  |
| 1572   | Layout 1             | `a79d73a75aef`  |
| 1565   | Layout 1             | `a79d73a75aef`  |
| 1559   | Layout 1             | `a79d73a75aef`  |
| 1554   | Layout 1             | `a79d73a75aef`  |
| 1547   | Layout 1             | `a79d73a75aef`  |
| 1537   | Layout 1             | `a79d73a75aef`  |
| 1529   | Layout 1             | `a79d73a75aef`  |
| 1524   | Layout 1             | `a79d73a75aef`  |
| 1519   | Layout 1             | `a79d73a75aef`  |
| 1509   | Layout 1             | `a79d73a75aef`  |
| 1506   | Layout 1             | `a79d73a75aef`  |
| 1504   | Layout 1             | `a79d73a75aef`  |
| 1500   | Layout 1             | `a79d73a75aef`  |
| 1493   | Layout 1             | `a79d73a75aef`  |
| 1489   | Layout 1             | `a79d73a75aef`  |
| 1485   | Layout 1             | `a79d73a75aef`  |
| 1481   | Layout 1             | `a79d73a75aef`  |
| 1474   | Layout 1             | `a79d73a75aef`  |
| 1466   | Layout 1             | `a79d73a75aef`  |
| 1462   | Layout 1             | `a79d73a75aef`  |
| 1459   | Layout 1             | `a79d73a75aef`  |
| 1453   | Layout 1             | `a79d73a75aef`  |
| 1450   | Layout 1             | `a79d73a75aef`  |
| 1445   | Layout 1             | `a79d73a75aef`  |
| 1439   | Layout 1             | `a79d73a75aef`  |
| 1433   | Layout 1             | `a79d73a75aef`  |
| 1430   | Layout 1             | `a79d73a75aef`  |
| 1426   | Layout 1             | `a79d73a75aef`  |
| 1421   | Layout 1             | `a79d73a75aef`  |
| 1417   | Layout 1             | `a79d73a75aef`  |
| 1416   | Layout 1             | `a79d73a75aef`  |
| 1409   | Layout 1             | `a79d73a75aef`  |
| 1405   | Layout 1             | `a79d73a75aef`  |
| 1401   | Layout 1             | `a79d73a75aef`  |
| 1396   | Layout 1             | `a79d73a75aef`  |
| 1391   | Layout 1             | `a79d73a75aef`  |
| 1390   | Layout 1             | `a79d73a75aef`  |
| 1386   | Layout 1             | `a79d73a75aef`  |
| 1381   | Layout 1             | `a79d73a75aef`  |
| 1379   | Layout 1             | `a79d73a75aef`  |
| 1372   | Layout 1             | `a79d73a75aef`  |
| 1366   | Layout 1             | `a79d73a75aef`  |
| 1364   | Layout 1             | `a79d73a75aef`  |
| 1363   | Layout 1             | `a79d73a75aef`  |
| 1360   | Layout 1             | `a79d73a75aef`  |
| 1358   | Layout 1             | `a79d73a75aef`  |
| 1355   | Layout 1             | `a79d73a75aef`  |
| 1351   | Layout 1             | `a79d73a75aef`  |
| 1348   | Layout 1             | `a79d73a75aef`  |
| 1346   | Layout 1             | `a79d73a75aef`  |
| 1341   | Layout 1             | `a79d73a75aef`  |
| 1340   | Layout 1             | `a79d73a75aef`  |
| 1338   | Layout 1             | `a79d73a75aef`  |
| 1335   | Layout 1             | `a79d73a75aef`  |
| 1333   | Layout 1             | `a79d73a75aef`  |
| 1329   | Layout 1             | `a79d73a75aef`  |
| 1327   | Layout 1             | `a79d73a75aef`  |
| 1324   | Layout 1             | `a79d73a75aef`  |
| 1321   | Layout 1             | `a79d73a75aef`  |
| 1319   | Layout 1             | `a79d73a75aef`  |
| 1318   | Layout 1             | `a79d73a75aef`  |
| 1316   | Layout 1             | `a79d73a75aef`  |
| 1313   | Layout 1             | `a79d73a75aef`  |
| 1311   | Layout 1             | `a79d73a75aef`  |
| 1309   | Layout 1             | `a79d73a75aef`  |
| 1304   | Layout 1             | `a79d73a75aef`  |
| 1292   | Layout 1             | `a79d73a75aef`  |
| 1286   | Layout 1             | `a79d73a75aef`  |
| 1280   | Layout 1             | `a79d73a75aef`  |
| 1276   | Layout 1             | `a79d73a75aef`  |
| 1267   | Layout 1             | `a79d73a75aef`  |
| 1261   | Layout 1             | `a79d73a75aef`  |
| 1256   | Layout 1             | `a79d73a75aef`  |
| 1250   | Layout 1             | `a79d73a75aef`  |
| 1246   | Layout 1             | `a79d73a75aef`  |
| 1239   | Layout 1             | `a79d73a75aef`  |
| 1230   | Layout 1             | `a79d73a75aef`  |
| 1226   | Layout 1             | `a79d73a75aef`  |
| 1220   | Layout 1             | `a79d73a75aef`  |
| 1217   | Layout 1             | `a79d73a75aef`  |
| 1211   | Layout 1             | `a79d73a75aef`  |
| 1210   | Layout 1             | `a79d73a75aef`  |
| 1208   | Layout 1             | `a79d73a75aef`  |
| 1203   | Layout 1             | `a79d73a75aef`  |
| 1197   | Layout 1             | `a79d73a75aef`  |
| 1194   | Layout 1             | `a79d73a75aef`  |
| 1192   | Layout 1             | `a79d73a75aef`  |
| 1187   | Layout 1             | `a79d73a75aef`  |
| 1183   | Layout 1             | `a79d73a75aef`  |
| 1177   | Layout 1             | `a79d73a75aef`  |
| 1173   | Layout 1             | `a79d73a75aef`  |
| 1167   | Layout 1             | `a79d73a75aef`  |
| 1164   | Layout 1             | `a79d73a75aef`  |
| 1156   | Layout 1             | `a79d73a75aef`  |
| 1149   | Layout 1             | `a79d73a75aef`  |
| 1144   | Layout 1             | `a79d73a75aef`  |
| 1137   | Layout 1             | `a79d73a75aef`  |
| 1132   | Layout 1             | `a79d73a75aef`  |
| 1127   | Layout 1             | `a79d73a75aef`  |
| 1122   | Layout 1             | `a79d73a75aef`  |
| 1118   | Layout 1             | `a79d73a75aef`  |
| 1114   | Layout 1             | `a79d73a75aef`  |
| 1109   | Layout 1             | `a79d73a75aef`  |
| 1102   | Layout 1             | `a79d73a75aef`  |
| 1096   | Layout 1             | `a79d73a75aef`  |
| 1088   | Layout 1             | `a79d73a75aef`  |
| 1081   | Layout 1             | `a79d73a75aef`  |
| 1076   | Layout 1             | `a79d73a75aef`  |
| 1069   | Layout 1             | `a79d73a75aef`  |
| 1064   | Layout 1             | `a79d73a75aef`  |
| 1058   | Layout 1             | `a79d73a75aef`  |
| 1051   | Layout 1             | `a79d73a75aef`  |
| 1044   | Layout 1             | `a79d73a75aef`  |
| 1036   | Layout 1             | `a79d73a75aef`  |
| 1026   | Layout 1             | `a79d73a75aef`  |
| 1016   | Layout 1             | `a79d73a75aef`  |
| 1009   | Layout 1             | `a79d73a75aef`  |
| 1005   | Layout 1             | `a79d73a75aef`  |
| 1000   | Layout 1             | `a79d73a75aef`  |
| 998    | Layout 1             | `a79d73a75aef`  |
| 990    | Layout 1             | `a79d73a75aef`  |
| 979    | Layout 1             | `a79d73a75aef`  |
| 972    | Layout 1             | `a79d73a75aef`  |
| 963    | Layout 1             | `a79d73a75aef`  |
| 955    | Layout 1             | `a79d73a75aef`  |
| 946    | Layout 1             | `a79d73a75aef`  |
| 938    | Layout 1             | `a79d73a75aef`  |
| 927    | Layout 1             | `a79d73a75aef`  |
| 911    | Layout 1             | `a79d73a75aef`  |
| 904    | Layout 1             | `a79d73a75aef`  |
| 899    | Layout 1             | `a79d73a75aef`  |
| 894    | Layout 1             | `a79d73a75aef`  |
| 885    | Layout 1             | `a79d73a75aef`  |
| 879    | Layout 1             | `a79d73a75aef`  |
| 872    | Layout 1             | `a79d73a75aef`  |
| 864    | Layout 1             | `a79d73a75aef`  |
| 855    | Layout 1             | `a79d73a75aef`  |
| 853    | Layout 1             | `a79d73a75aef`  |
| 845    | Layout 1             | `a79d73a75aef`  |
| 837    | Layout 1             | `a79d73a75aef`  |
| 829    | Layout 1             | `a79d73a75aef`  |
| 822    | Layout 1             | `a79d73a75aef`  |
| 814    | Layout 1             | `a79d73a75aef`  |
| 805    | Layout 1             | `a79d73a75aef`  |
| 794    | No documented layout | `a79d73a75aef`  |
| 787    | No documented layout | `a79d73a75aef`  |
| 780    | No documented layout | `a79d73a75aef`  |
| 771    | No documented layout | `a79d73a75aef`  |
| 760    | No documented layout | `a79d73a75aef`  |
| 748    | No documented layout | `a79d73a75aef`  |
| 741    | No documented layout | `a79d73a75aef`  |
| 736    | No documented layout | `a79d73a75aef`  |
| 731    | No documented layout | `a79d73a75aef`  |
| 723    | No documented layout | `a79d73a75aef`  |
| 711    | No documented layout | `a79d73a75aef`  |
| 707    | No documented layout | `a79d73a75aef`  |
| 697    | No documented layout | `a79d73a75aef`  |
| 689    | No documented layout | `a79d73a75aef`  |
| 683    | No documented layout | `a79d73a75aef`  |
| 678    | No documented layout | `a79d73a75aef`  |
| 670    | No documented layout | `a79d73a75aef`  |
| 661    | No documented layout | `a79d73a75aef`  |
| 656    | No documented layout | `a79d73a75aef`  |
| 652    | No documented layout | `a79d73a75aef`  |
| 643    | No documented layout | `a79d73a75aef`  |
| 637    | No documented layout | `a79d73a75aef`  |
| 630    | No documented layout | `a79d73a75aef`  |
| 627    | No documented layout | `a79d73a75aef`  |
| 621    | No documented layout | `a79d73a75aef`  |
| 617    | No documented layout | `a79d73a75aef`  |
| 615    | No documented layout | `a79d73a75aef`  |
| 606    | No documented layout | `a79d73a75aef`  |
| 599    | No documented layout | `a79d73a75aef`  |
| 592    | No documented layout | `a79d73a75aef`  |
| 586    | No documented layout | `a79d73a75aef`  |
| 577    | No documented layout | `a79d73a75aef`  |
| 569    | No documented layout | `a79d73a75aef`  |
| 561    | No documented layout | `a79d73a75aef`  |
| 554    | No documented layout | `a79d73a75aef`  |
| 542    | No documented layout | `a79d73a75aef`  |
| 532    | No documented layout | `a79d73a75aef`  |
| 531    | No documented layout | `a79d73a75aef`  |
| 526    | No documented layout | `a79d73a75aef`  |
| 521    | No documented layout | `a79d73a75aef`  |
| 517    | No documented layout | `a79d73a75aef`  |
| 510    | No documented layout | `a79d73a75aef`  |
| 508    | No documented layout | `a79d73a75aef`  |
| 504    | No documented layout | `a79d73a75aef`  |
| 497    | No documented layout | `a79d73a75aef`  |
| 491    | No documented layout | `a79d73a75aef`  |
| 485    | No documented layout | `a79d73a75aef`  |
| 478    | No documented layout | `a79d73a75aef`  |
| 472    | No documented layout | `a79d73a75aef`  |
| 466    | No documented layout | `a79d73a75aef`  |
| 457    | No documented layout | `a79d73a75aef`  |
| 452    | No file              | `a79d73a75aef`  |
| 449    | No file              | `a79d73a75aef`  |
| 435    | No file              | `a79d73a75aef`  |

<!-- versions:end -->

## Companion Files

None. Class names come from LOC type 21 and the names of placed skills
(none on clients 1784 and 3482) from LOC type 10.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                     | Field        | Notes                                              |
| ------------------- | ------------------------ | ------------ | -------------------------------------------------- |
| `+0x00`             | char[4]                  | magic        | `PABR`                                             |
| `+0x04`             | u32                      | class_count  | Number of class grids; `8`                         |
| `+0x08`             | Class Grid[class_count]  | grids        | See Class Grid                                     |
| `grids+0x00`        | String Table             | string_table | See String Table                                   |
| `string_table+0x00` | u32                      | table_start  | Offset of the string table, where `grids` ends     |
| `string_table+0x04` | u32                      | zero         | Always `0`                                         |

### Class Grid (variable: 9 bytes + cells)

| Offset  | Type                | Field      | Notes                                                       |
| ------- | ------------------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u8                  | class_type | Class, LOC type `21`: `0`, `4`, `8`, `12`, `13`, `16`, `20`, `24` |
| `+0x01` | u32                 | width      | Sheet columns; `23` on every grid                           |
| `+0x05` | u32                 | height     | Sheet rows; `51` on every grid                              |
| `+0x09` | Cell[width][height] | cells      | `width * height` cells; see Cell                            |

### Cell (4 bytes)

| Offset  | Type | Field      | Notes                                                           |
| ------- | ---- | ---------- | --------------------------------------------------------------- |
| `+0x00` | u8   | cell_type  | See Cell Types; `1` (Blank) on every cell                       |
| `+0x01` | u8   | arrow_type | See Arrow Types; `0` on every cell                              |
| `+0x02` | u16  | skill_no   | Skill number when `cell_type` is `2`; `0` on every cell         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482          |
| `+0x04` | pstr[string_count] | strings      | No field reads a string               |

## Cell Types

`ge::UISkillTreeLayout_CellValueType` of the 2016 PDB, the same values as
the [`ui_skillgroup_*.bss` Cell Types](ui_skillgroup_bss.md#cell-types):
`0` Undefined, `1` Blank, `2` Skill, `3` to `11` the corner and junction
pieces `LT` to `RB`, `12` Hori, `13` Vert.

## Arrow Types

`ge::UISkillTreeLayout_CellValueArrowType` of the 2016 PDB: `0` None, `1`
Left, `2` Right, `3` Top, `4` Bottom.

## Field Names

The cell is the 2016 `ge::UISkillTreeLayout_CellValue`, 4 bytes: u8
`_cellType`, u8 `_arrowType`, u16 `_skillNo`, in that order. The current
`ui_skillgroup_*.bss` files use a longer cell (a counted type list, a
group number and a tab band); this file keeps the 2016 one, and so do the
eight one-grid files of
[`uiguildskilltreelayout.bss`](uiguildskilltreelayout_bss.md).

The developer workbook `UIPracticeSkillTreeLayout.xlsm` of a private
server on client 1784 has one sheet per grid, named `0_SKill`, `4_Skill`,
`8_Skill`, `12_Skill`, `13_Skill`, `16_Skill`, `20_Skill` and `24_Skill`:
the eight `class_type` values in file order. Each sheet marks its right
edge with `END` in the first row of column X, which leaves 23 columns, the
`width`. Every sheet holds no cell value, only the line templates beside
the grid, which is why every cell is Blank.

## Notes

- The eight class types are Warrior, Ranger, Sorceress, Berserker, `13`,
  Tamer, Musa and Valkyrie; type `13` has the LOC type 21 name `PBM` on
  client 3482.
- With every cell Blank, the walk cannot tell whether cells run column by
  column, as in `ui_skillgroup_*.bss`, or row by row.
- No compiled Lua file of client 3482 contains the text `PracticeSkill`.

## Open Questions

### What Window the Practice Tree Belongs To

The grids are empty and no Lua names them. The name and the 2016 cell
format suggest a skill tree window of the 2016 client that the game no
longer fills.
