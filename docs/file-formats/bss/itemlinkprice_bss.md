# `itemlinkprice.bss` Format

## Purpose

Items whose price follows another item's price: pairs of item keys, the
item first, then the item whose price it takes. Fiery Kutum Shield
(`694290`) follows Kutum Shield (`10140`). The pairs on client 3474 tie a
gear variant (`Fiery`, `Earthshaking`, `Ultimate`, `of Agony`) or a second
item of the same name to the base item.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes  | Records    | Row bytes |
| ------ | -------------- | ------------------- | ------ | ---------- | --------- |
| 1      | 1450 and later | `itemlinkprice.bss` | 29,660 | 3,705 Link | 8         |

| Layout | File                | Known             | Unknown    |
| ------ | ------------------- | ----------------- | ---------- |
| 1      | `itemlinkprice.bss` | 29,660 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `3957e1e44d8c`  |
| 3482   | Layout 1 | `3957e1e44d8c`  |
| 3474   | Layout 1 | `3957e1e44d8c`  |
| 3473   | Layout 1 | `3957e1e44d8c`  |
| 3464   | Layout 1 | `3957e1e44d8c`  |
| 3458   | Layout 1 | `3957e1e44d8c`  |
| 3454   | Layout 1 | `3957e1e44d8c`  |
| 3444   | Layout 1 | `3957e1e44d8c`  |
| 3435   | Layout 1 | `3957e1e44d8c`  |
| 3426   | Layout 1 | `3957e1e44d8c`  |
| 3418   | Layout 1 | `3957e1e44d8c`  |
| 3412   | Layout 1 | `3957e1e44d8c`  |
| 3402   | Layout 1 | `3957e1e44d8c`  |
| 3396   | Layout 1 | `3957e1e44d8c`  |
| 3387   | Layout 1 | `3957e1e44d8c`  |
| 3381   | Layout 1 | `3957e1e44d8c`  |
| 3373   | Layout 1 | `3957e1e44d8c`  |
| 3364   | Layout 1 | `3957e1e44d8c`  |
| 3356   | Layout 1 | `3957e1e44d8c`  |
| 3349   | Layout 1 | `3957e1e44d8c`  |
| 3342   | Layout 1 | `3957e1e44d8c`  |
| 3335   | Layout 1 | `3957e1e44d8c`  |
| 3326   | Layout 1 | `3957e1e44d8c`  |
| 3321   | Layout 1 | `3957e1e44d8c`  |
| 3314   | Layout 1 | `3957e1e44d8c`  |
| 3303   | Layout 1 | `3957e1e44d8c`  |
| 3302   | Layout 1 | `3957e1e44d8c`  |
| 3293   | Layout 1 | `3957e1e44d8c`  |
| 3283   | Layout 1 | `3957e1e44d8c`  |
| 3275   | Layout 1 | `3957e1e44d8c`  |
| 3267   | Layout 1 | `3957e1e44d8c`  |
| 3258   | Layout 1 | `3957e1e44d8c`  |
| 3251   | Layout 1 | `3957e1e44d8c`  |
| 3242   | Layout 1 | `3957e1e44d8c`  |
| 3235   | Layout 1 | `3957e1e44d8c`  |
| 3229   | Layout 1 | `3957e1e44d8c`  |
| 3212   | Layout 1 | `3957e1e44d8c`  |
| 3203   | Layout 1 | `3957e1e44d8c`  |
| 3193   | Layout 1 | `3957e1e44d8c`  |
| 3186   | Layout 1 | `3957e1e44d8c`  |
| 3177   | Layout 1 | `3957e1e44d8c`  |
| 3169   | Layout 1 | `3957e1e44d8c`  |
| 3158   | Layout 1 | `3957e1e44d8c`  |
| 3151   | Layout 1 | `3957e1e44d8c`  |
| 3144   | Layout 1 | `3957e1e44d8c`  |
| 3133   | Layout 1 | `3957e1e44d8c`  |
| 3125   | Layout 1 | `3957e1e44d8c`  |
| 3118   | Layout 1 | `3957e1e44d8c`  |
| 3111   | Layout 1 | `3957e1e44d8c`  |
| 3103   | Layout 1 | `3957e1e44d8c`  |
| 3095   | Layout 1 | `3957e1e44d8c`  |
| 3086   | Layout 1 | `3957e1e44d8c`  |
| 3072   | Layout 1 | `3957e1e44d8c`  |
| 3062   | Layout 1 | `3957e1e44d8c`  |
| 3052   | Layout 1 | `3957e1e44d8c`  |
| 3045   | Layout 1 | `3957e1e44d8c`  |
| 3037   | Layout 1 | `3957e1e44d8c`  |
| 3030   | Layout 1 | `3957e1e44d8c`  |
| 3021   | Layout 1 | `3957e1e44d8c`  |
| 3012   | Layout 1 | `3957e1e44d8c`  |
| 3002   | Layout 1 | `3957e1e44d8c`  |
| 2995   | Layout 1 | `3957e1e44d8c`  |
| 2987   | Layout 1 | `3957e1e44d8c`  |
| 2978   | Layout 1 | `3957e1e44d8c`  |
| 2970   | Layout 1 | `3957e1e44d8c`  |
| 2959   | Layout 1 | `3957e1e44d8c`  |
| 2951   | Layout 1 | `3957e1e44d8c`  |
| 2942   | Layout 1 | `3957e1e44d8c`  |
| 2935   | Layout 1 | `3957e1e44d8c`  |
| 2932   | Layout 1 | `3957e1e44d8c`  |
| 2923   | Layout 1 | `3957e1e44d8c`  |
| 2919   | Layout 1 | `3957e1e44d8c`  |
| 2907   | Layout 1 | `3957e1e44d8c`  |
| 2900   | Layout 1 | `3957e1e44d8c`  |
| 2891   | Layout 1 | `3957e1e44d8c`  |
| 2882   | Layout 1 | `3957e1e44d8c`  |
| 2872   | Layout 1 | `3957e1e44d8c`  |
| 2863   | Layout 1 | `3957e1e44d8c`  |
| 2855   | Layout 1 | `3957e1e44d8c`  |
| 2849   | Layout 1 | `3957e1e44d8c`  |
| 2844   | Layout 1 | `3957e1e44d8c`  |
| 2834   | Layout 1 | `3957e1e44d8c`  |
| 2825   | Layout 1 | `3957e1e44d8c`  |
| 2819   | Layout 1 | `3957e1e44d8c`  |
| 2811   | Layout 1 | `3957e1e44d8c`  |
| 2803   | Layout 1 | `3957e1e44d8c`  |
| 2794   | Layout 1 | `3957e1e44d8c`  |
| 2783   | Layout 1 | `3957e1e44d8c`  |
| 2774   | Layout 1 | `3957e1e44d8c`  |
| 2765   | Layout 1 | `3957e1e44d8c`  |
| 2756   | Layout 1 | `3957e1e44d8c`  |
| 2750   | Layout 1 | `3957e1e44d8c`  |
| 2743   | Layout 1 | `3957e1e44d8c`  |
| 2736   | Layout 1 | `3957e1e44d8c`  |
| 2726   | Layout 1 | `3957e1e44d8c`  |
| 2717   | Layout 1 | `3957e1e44d8c`  |
| 2709   | Layout 1 | `3957e1e44d8c`  |
| 2703   | Layout 1 | `3957e1e44d8c`  |
| 2695   | Layout 1 | `3957e1e44d8c`  |
| 2684   | Layout 1 | `3957e1e44d8c`  |
| 2672   | Layout 1 | `3957e1e44d8c`  |
| 2665   | Layout 1 | `3957e1e44d8c`  |
| 2657   | Layout 1 | `3957e1e44d8c`  |
| 2649   | Layout 1 | `3957e1e44d8c`  |
| 2644   | Layout 1 | `3957e1e44d8c`  |
| 2637   | Layout 1 | `3957e1e44d8c`  |
| 2629   | Layout 1 | `3957e1e44d8c`  |
| 2619   | Layout 1 | `3957e1e44d8c`  |
| 2612   | Layout 1 | `3957e1e44d8c`  |
| 2606   | Layout 1 | `3957e1e44d8c`  |
| 2602   | Layout 1 | `3957e1e44d8c`  |
| 2601   | Layout 1 | `3957e1e44d8c`  |
| 2592   | Layout 1 | `3957e1e44d8c`  |
| 2583   | Layout 1 | `3957e1e44d8c`  |
| 2575   | Layout 1 | `3957e1e44d8c`  |
| 2567   | Layout 1 | `3957e1e44d8c`  |
| 2560   | Layout 1 | `3957e1e44d8c`  |
| 2553   | Layout 1 | `3957e1e44d8c`  |
| 2545   | Layout 1 | `3957e1e44d8c`  |
| 2538   | Layout 1 | `3957e1e44d8c`  |
| 2529   | Layout 1 | `3957e1e44d8c`  |
| 2519   | Layout 1 | `3957e1e44d8c`  |
| 2513   | Layout 1 | `3957e1e44d8c`  |
| 2510   | Layout 1 | `3957e1e44d8c`  |
| 2507   | Layout 1 | `3957e1e44d8c`  |
| 2503   | Layout 1 | `3957e1e44d8c`  |
| 2498   | Layout 1 | `3957e1e44d8c`  |
| 2492   | Layout 1 | `3957e1e44d8c`  |
| 2487   | Layout 1 | `3957e1e44d8c`  |
| 2480   | Layout 1 | `3957e1e44d8c`  |
| 2474   | Layout 1 | `3957e1e44d8c`  |
| 2468   | Layout 1 | `3957e1e44d8c`  |
| 2460   | Layout 1 | `3957e1e44d8c`  |
| 2453   | Layout 1 | `3957e1e44d8c`  |
| 2444   | Layout 1 | `3957e1e44d8c`  |
| 2438   | Layout 1 | `3957e1e44d8c`  |
| 2434   | Layout 1 | `3957e1e44d8c`  |
| 2429   | Layout 1 | `3957e1e44d8c`  |
| 2421   | Layout 1 | `3957e1e44d8c`  |
| 2414   | Layout 1 | `3957e1e44d8c`  |
| 2407   | Layout 1 | `3957e1e44d8c`  |
| 2401   | Layout 1 | `3957e1e44d8c`  |
| 2397   | Layout 1 | `3957e1e44d8c`  |
| 2393   | Layout 1 | `3957e1e44d8c`  |
| 2384   | Layout 1 | `3957e1e44d8c`  |
| 2378   | Layout 1 | `3957e1e44d8c`  |
| 2372   | Layout 1 | `3957e1e44d8c`  |
| 2358   | Layout 1 | `3957e1e44d8c`  |
| 2352   | Layout 1 | `3957e1e44d8c`  |
| 2347   | Layout 1 | `3957e1e44d8c`  |
| 2343   | Layout 1 | `3957e1e44d8c`  |
| 2335   | Layout 1 | `3957e1e44d8c`  |
| 2327   | Layout 1 | `3957e1e44d8c`  |
| 2324   | Layout 1 | `3957e1e44d8c`  |
| 2319   | Layout 1 | `3957e1e44d8c`  |
| 2313   | Layout 1 | `3957e1e44d8c`  |
| 2308   | Layout 1 | `3957e1e44d8c`  |
| 2302   | Layout 1 | `3957e1e44d8c`  |
| 2295   | Layout 1 | `3957e1e44d8c`  |
| 2290   | Layout 1 | `3957e1e44d8c`  |
| 2284   | Layout 1 | `3957e1e44d8c`  |
| 2276   | Layout 1 | `3957e1e44d8c`  |
| 2269   | Layout 1 | `3957e1e44d8c`  |
| 2259   | Layout 1 | `3957e1e44d8c`  |
| 2250   | Layout 1 | `3957e1e44d8c`  |
| 2243   | Layout 1 | `3957e1e44d8c`  |
| 2235   | Layout 1 | `3957e1e44d8c`  |
| 2229   | Layout 1 | `3957e1e44d8c`  |
| 2224   | Layout 1 | `3957e1e44d8c`  |
| 2218   | Layout 1 | `3957e1e44d8c`  |
| 2215   | Layout 1 | `3957e1e44d8c`  |
| 2207   | Layout 1 | `3957e1e44d8c`  |
| 2203   | Layout 1 | `3957e1e44d8c`  |
| 2196   | Layout 1 | `3957e1e44d8c`  |
| 2192   | Layout 1 | `3957e1e44d8c`  |
| 2189   | Layout 1 | `3957e1e44d8c`  |
| 2183   | Layout 1 | `3957e1e44d8c`  |
| 2179   | Layout 1 | `3957e1e44d8c`  |
| 2171   | Layout 1 | `3957e1e44d8c`  |
| 2163   | Layout 1 | `3957e1e44d8c`  |
| 2156   | Layout 1 | `3957e1e44d8c`  |
| 2151   | Layout 1 | `3957e1e44d8c`  |
| 2147   | Layout 1 | `3957e1e44d8c`  |
| 2142   | Layout 1 | `3957e1e44d8c`  |
| 2138   | Layout 1 | `3957e1e44d8c`  |
| 2134   | Layout 1 | `3957e1e44d8c`  |
| 2130   | Layout 1 | `3957e1e44d8c`  |
| 2122   | Layout 1 | `3957e1e44d8c`  |
| 2107   | Layout 1 | `3957e1e44d8c`  |
| 2098   | Layout 1 | `3957e1e44d8c`  |
| 2089   | Layout 1 | `3957e1e44d8c`  |
| 2081   | Layout 1 | `3957e1e44d8c`  |
| 2073   | Layout 1 | `3957e1e44d8c`  |
| 2067   | Layout 1 | `3957e1e44d8c`  |
| 2063   | Layout 1 | `3957e1e44d8c`  |
| 2059   | Layout 1 | `3957e1e44d8c`  |
| 2052   | Layout 1 | `3957e1e44d8c`  |
| 2044   | Layout 1 | `3957e1e44d8c`  |
| 2039   | Layout 1 | `3957e1e44d8c`  |
| 2032   | Layout 1 | `3957e1e44d8c`  |
| 2025   | Layout 1 | `3957e1e44d8c`  |
| 2011   | Layout 1 | `3957e1e44d8c`  |
| 2005   | Layout 1 | `3957e1e44d8c`  |
| 2000   | Layout 1 | `3957e1e44d8c`  |
| 1996   | Layout 1 | `3957e1e44d8c`  |
| 1991   | Layout 1 | `3957e1e44d8c`  |
| 1985   | Layout 1 | `3957e1e44d8c`  |
| 1980   | Layout 1 | `3957e1e44d8c`  |
| 1969   | Layout 1 | `3957e1e44d8c`  |
| 1964   | Layout 1 | `3957e1e44d8c`  |
| 1958   | Layout 1 | `3957e1e44d8c`  |
| 1950   | Layout 1 | `3957e1e44d8c`  |
| 1945   | Layout 1 | `3957e1e44d8c`  |
| 1937   | Layout 1 | `3957e1e44d8c`  |
| 1933   | Layout 1 | `3957e1e44d8c`  |
| 1927   | Layout 1 | `3957e1e44d8c`  |
| 1921   | Layout 1 | `3957e1e44d8c`  |
| 1914   | Layout 1 | `3957e1e44d8c`  |
| 1908   | Layout 1 | `3957e1e44d8c`  |
| 1897   | Layout 1 | `3957e1e44d8c`  |
| 1892   | Layout 1 | `3957e1e44d8c`  |
| 1886   | Layout 1 | `3957e1e44d8c`  |
| 1881   | Layout 1 | `3957e1e44d8c`  |
| 1871   | Layout 1 | `3957e1e44d8c`  |
| 1866   | Layout 1 | `3957e1e44d8c`  |
| 1862   | Layout 1 | `3957e1e44d8c`  |
| 1854   | Layout 1 | `3957e1e44d8c`  |
| 1846   | Layout 1 | `3957e1e44d8c`  |
| 1838   | Layout 1 | `3957e1e44d8c`  |
| 1832   | Layout 1 | `3957e1e44d8c`  |
| 1826   | Layout 1 | `3957e1e44d8c`  |
| 1822   | Layout 1 | `3957e1e44d8c`  |
| 1818   | Layout 1 | `3957e1e44d8c`  |
| 1804   | Layout 1 | `3957e1e44d8c`  |
| 1794   | Layout 1 | `3957e1e44d8c`  |
| 1790   | Layout 1 | `3957e1e44d8c`  |
| 1784   | Layout 1 | `3957e1e44d8c`  |
| 1774   | Layout 1 | `3957e1e44d8c`  |
| 1771   | Layout 1 | `3957e1e44d8c`  |
| 1762   | Layout 1 | `3957e1e44d8c`  |
| 1759   | Layout 1 | `3957e1e44d8c`  |
| 1754   | Layout 1 | `3957e1e44d8c`  |
| 1749   | Layout 1 | `3957e1e44d8c`  |
| 1743   | Layout 1 | `3957e1e44d8c`  |
| 1737   | Layout 1 | `3957e1e44d8c`  |
| 1731   | Layout 1 | `3957e1e44d8c`  |
| 1725   | Layout 1 | `3957e1e44d8c`  |
| 1717   | Layout 1 | `3957e1e44d8c`  |
| 1710   | Layout 1 | `3957e1e44d8c`  |
| 1704   | Layout 1 | `3957e1e44d8c`  |
| 1698   | Layout 1 | `3957e1e44d8c`  |
| 1690   | Layout 1 | `3957e1e44d8c`  |
| 1685   | Layout 1 | `3957e1e44d8c`  |
| 1680   | Layout 1 | `3957e1e44d8c`  |
| 1674   | Layout 1 | `3957e1e44d8c`  |
| 1668   | Layout 1 | `3957e1e44d8c`  |
| 1659   | Layout 1 | `3957e1e44d8c`  |
| 1649   | Layout 1 | `3957e1e44d8c`  |
| 1642   | Layout 1 | `3957e1e44d8c`  |
| 1636   | Layout 1 | `3957e1e44d8c`  |
| 1628   | Layout 1 | `3957e1e44d8c`  |
| 1622   | Layout 1 | `3957e1e44d8c`  |
| 1614   | Layout 1 | `3957e1e44d8c`  |
| 1608   | Layout 1 | `3957e1e44d8c`  |
| 1602   | Layout 1 | `3957e1e44d8c`  |
| 1598   | Layout 1 | `3957e1e44d8c`  |
| 1594   | Layout 1 | `3957e1e44d8c`  |
| 1590   | Layout 1 | `3957e1e44d8c`  |
| 1587   | Layout 1 | `3957e1e44d8c`  |
| 1584   | Layout 1 | `3957e1e44d8c`  |
| 1579   | Layout 1 | `3957e1e44d8c`  |
| 1572   | Layout 1 | `3957e1e44d8c`  |
| 1565   | Layout 1 | `3957e1e44d8c`  |
| 1559   | Layout 1 | `3957e1e44d8c`  |
| 1554   | Layout 1 | `3957e1e44d8c`  |
| 1547   | Layout 1 | `3957e1e44d8c`  |
| 1537   | Layout 1 | `3957e1e44d8c`  |
| 1529   | Layout 1 | `3957e1e44d8c`  |
| 1524   | Layout 1 | `3957e1e44d8c`  |
| 1519   | Layout 1 | `3957e1e44d8c`  |
| 1509   | Layout 1 | `3957e1e44d8c`  |
| 1506   | Layout 1 | `3957e1e44d8c`  |
| 1504   | Layout 1 | `3957e1e44d8c`  |
| 1500   | Layout 1 | `3957e1e44d8c`  |
| 1493   | Layout 1 | `3957e1e44d8c`  |
| 1489   | Layout 1 | `3957e1e44d8c`  |
| 1485   | Layout 1 | `3957e1e44d8c`  |
| 1481   | Layout 1 | `3957e1e44d8c`  |
| 1474   | Layout 1 | `3957e1e44d8c`  |
| 1466   | Layout 1 | `3957e1e44d8c`  |
| 1462   | Layout 1 | `3957e1e44d8c`  |
| 1459   | Layout 1 | `3957e1e44d8c`  |
| 1453   | Layout 1 | `3957e1e44d8c`  |
| 1450   | Layout 1 | `3957e1e44d8c`  |
| 1445   | No file  | `3957e1e44d8c`  |
| 1439   | No file  | `3957e1e44d8c`  |
| 1433   | No file  | `3957e1e44d8c`  |
| 1430   | No file  | `3957e1e44d8c`  |
| 1426   | No file  | `3957e1e44d8c`  |
| 1421   | No file  | `3957e1e44d8c`  |
| 1417   | No file  | `3957e1e44d8c`  |
| 1416   | No file  | `3957e1e44d8c`  |
| 1409   | No file  | `3957e1e44d8c`  |
| 1405   | No file  | `3957e1e44d8c`  |
| 1401   | No file  | `3957e1e44d8c`  |
| 1396   | No file  | `3957e1e44d8c`  |
| 1391   | No file  | `3957e1e44d8c`  |
| 1390   | No file  | `3957e1e44d8c`  |
| 1386   | No file  | `3957e1e44d8c`  |
| 1381   | No file  | `3957e1e44d8c`  |
| 1379   | No file  | `3957e1e44d8c`  |
| 1372   | No file  | `3957e1e44d8c`  |
| 1366   | No file  | `3957e1e44d8c`  |
| 1364   | No file  | `3957e1e44d8c`  |
| 1363   | No file  | `3957e1e44d8c`  |
| 1360   | No file  | `3957e1e44d8c`  |
| 1358   | No file  | `3957e1e44d8c`  |
| 1355   | No file  | `3957e1e44d8c`  |
| 1351   | No file  | `3957e1e44d8c`  |
| 1348   | No file  | `3957e1e44d8c`  |
| 1346   | No file  | `3957e1e44d8c`  |
| 1341   | No file  | `3957e1e44d8c`  |
| 1340   | No file  | `3957e1e44d8c`  |
| 1338   | No file  | `3957e1e44d8c`  |
| 1335   | No file  | `3957e1e44d8c`  |
| 1333   | No file  | `3957e1e44d8c`  |
| 1329   | No file  | `3957e1e44d8c`  |
| 1327   | No file  | `3957e1e44d8c`  |
| 1324   | No file  | `3957e1e44d8c`  |
| 1321   | No file  | `3957e1e44d8c`  |
| 1319   | No file  | `3957e1e44d8c`  |
| 1318   | No file  | `3957e1e44d8c`  |
| 1316   | No file  | `3957e1e44d8c`  |
| 1313   | No file  | `3957e1e44d8c`  |
| 1311   | No file  | `3957e1e44d8c`  |
| 1309   | No file  | `3957e1e44d8c`  |
| 1304   | No file  | `3957e1e44d8c`  |
| 1292   | No file  | `3957e1e44d8c`  |
| 1286   | No file  | `3957e1e44d8c`  |
| 1280   | No file  | `3957e1e44d8c`  |
| 1276   | No file  | `3957e1e44d8c`  |
| 1267   | No file  | `3957e1e44d8c`  |
| 1261   | No file  | `3957e1e44d8c`  |
| 1256   | No file  | `3957e1e44d8c`  |
| 1250   | No file  | `3957e1e44d8c`  |
| 1246   | No file  | `3957e1e44d8c`  |
| 1239   | No file  | `3957e1e44d8c`  |
| 1230   | No file  | `3957e1e44d8c`  |
| 1226   | No file  | `3957e1e44d8c`  |
| 1220   | No file  | `3957e1e44d8c`  |
| 1217   | No file  | `3957e1e44d8c`  |
| 1211   | No file  | `3957e1e44d8c`  |
| 1210   | No file  | `3957e1e44d8c`  |
| 1208   | No file  | `3957e1e44d8c`  |
| 1203   | No file  | `3957e1e44d8c`  |
| 1197   | No file  | `3957e1e44d8c`  |
| 1194   | No file  | `3957e1e44d8c`  |
| 1192   | No file  | `3957e1e44d8c`  |
| 1187   | No file  | `3957e1e44d8c`  |
| 1183   | No file  | `3957e1e44d8c`  |
| 1177   | No file  | `3957e1e44d8c`  |
| 1173   | No file  | `3957e1e44d8c`  |
| 1167   | No file  | `3957e1e44d8c`  |
| 1164   | No file  | `3957e1e44d8c`  |
| 1156   | No file  | `3957e1e44d8c`  |
| 1149   | No file  | `3957e1e44d8c`  |
| 1144   | No file  | `3957e1e44d8c`  |
| 1137   | No file  | `3957e1e44d8c`  |
| 1132   | No file  | `3957e1e44d8c`  |
| 1127   | No file  | `3957e1e44d8c`  |
| 1122   | No file  | `3957e1e44d8c`  |
| 1118   | No file  | `3957e1e44d8c`  |
| 1114   | No file  | `3957e1e44d8c`  |
| 1109   | No file  | `3957e1e44d8c`  |
| 1102   | No file  | `3957e1e44d8c`  |
| 1096   | No file  | `3957e1e44d8c`  |
| 1088   | No file  | `3957e1e44d8c`  |
| 1081   | No file  | `3957e1e44d8c`  |
| 1076   | No file  | `3957e1e44d8c`  |
| 1069   | No file  | `3957e1e44d8c`  |
| 1064   | No file  | `3957e1e44d8c`  |
| 1058   | No file  | `3957e1e44d8c`  |
| 1051   | No file  | `3957e1e44d8c`  |
| 1044   | No file  | `3957e1e44d8c`  |
| 1036   | No file  | `3957e1e44d8c`  |
| 1026   | No file  | `3957e1e44d8c`  |
| 1016   | No file  | `3957e1e44d8c`  |
| 1009   | No file  | `3957e1e44d8c`  |
| 1005   | No file  | `3957e1e44d8c`  |
| 1000   | No file  | `3957e1e44d8c`  |
| 998    | No file  | `3957e1e44d8c`  |
| 990    | No file  | `3957e1e44d8c`  |
| 979    | No file  | `3957e1e44d8c`  |
| 972    | No file  | `3957e1e44d8c`  |
| 963    | No file  | `3957e1e44d8c`  |
| 955    | No file  | `3957e1e44d8c`  |
| 946    | No file  | `3957e1e44d8c`  |
| 938    | No file  | `3957e1e44d8c`  |
| 927    | No file  | `3957e1e44d8c`  |
| 911    | No file  | `3957e1e44d8c`  |
| 904    | No file  | `3957e1e44d8c`  |
| 899    | No file  | `3957e1e44d8c`  |
| 894    | No file  | `3957e1e44d8c`  |
| 885    | No file  | `3957e1e44d8c`  |
| 879    | No file  | `3957e1e44d8c`  |
| 872    | No file  | `3957e1e44d8c`  |
| 864    | No file  | `3957e1e44d8c`  |
| 855    | No file  | `3957e1e44d8c`  |
| 853    | No file  | `3957e1e44d8c`  |
| 845    | No file  | `3957e1e44d8c`  |
| 837    | No file  | `3957e1e44d8c`  |
| 829    | No file  | `3957e1e44d8c`  |
| 822    | No file  | `3957e1e44d8c`  |
| 814    | No file  | `3957e1e44d8c`  |
| 805    | No file  | `3957e1e44d8c`  |
| 794    | No file  | `3957e1e44d8c`  |
| 787    | No file  | `3957e1e44d8c`  |
| 780    | No file  | `3957e1e44d8c`  |
| 771    | No file  | `3957e1e44d8c`  |
| 760    | No file  | `3957e1e44d8c`  |
| 748    | No file  | `3957e1e44d8c`  |
| 741    | No file  | `3957e1e44d8c`  |
| 736    | No file  | `3957e1e44d8c`  |
| 731    | No file  | `3957e1e44d8c`  |
| 723    | No file  | `3957e1e44d8c`  |
| 711    | No file  | `3957e1e44d8c`  |
| 707    | No file  | `3957e1e44d8c`  |
| 697    | No file  | `3957e1e44d8c`  |
| 689    | No file  | `3957e1e44d8c`  |
| 683    | No file  | `3957e1e44d8c`  |
| 678    | No file  | `3957e1e44d8c`  |
| 670    | No file  | `3957e1e44d8c`  |
| 661    | No file  | `3957e1e44d8c`  |
| 656    | No file  | `3957e1e44d8c`  |
| 652    | No file  | `3957e1e44d8c`  |
| 643    | No file  | `3957e1e44d8c`  |
| 637    | No file  | `3957e1e44d8c`  |
| 630    | No file  | `3957e1e44d8c`  |
| 627    | No file  | `3957e1e44d8c`  |
| 621    | No file  | `3957e1e44d8c`  |
| 617    | No file  | `3957e1e44d8c`  |
| 615    | No file  | `3957e1e44d8c`  |
| 606    | No file  | `3957e1e44d8c`  |
| 599    | No file  | `3957e1e44d8c`  |
| 592    | No file  | `3957e1e44d8c`  |
| 586    | No file  | `3957e1e44d8c`  |
| 577    | No file  | `3957e1e44d8c`  |
| 569    | No file  | `3957e1e44d8c`  |
| 561    | No file  | `3957e1e44d8c`  |
| 554    | No file  | `3957e1e44d8c`  |
| 542    | No file  | `3957e1e44d8c`  |
| 532    | No file  | `3957e1e44d8c`  |
| 531    | No file  | `3957e1e44d8c`  |
| 526    | No file  | `3957e1e44d8c`  |
| 521    | No file  | `3957e1e44d8c`  |
| 517    | No file  | `3957e1e44d8c`  |
| 510    | No file  | `3957e1e44d8c`  |
| 508    | No file  | `3957e1e44d8c`  |
| 504    | No file  | `3957e1e44d8c`  |
| 497    | No file  | `3957e1e44d8c`  |
| 491    | No file  | `3957e1e44d8c`  |
| 485    | No file  | `3957e1e44d8c`  |
| 478    | No file  | `3957e1e44d8c`  |
| 472    | No file  | `3957e1e44d8c`  |
| 466    | No file  | `3957e1e44d8c`  |
| 457    | No file  | `3957e1e44d8c`  |
| 452    | No file  | `3957e1e44d8c`  |
| 449    | No file  | `3957e1e44d8c`  |
| 435    | No file  | `3957e1e44d8c`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Item names (type `0`)       |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type             | Field              | Notes                                                   |
| ------------------- | ---------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]          | magic              | ASCII `PABR`                                            |
| `+0x04`             | u32              | link_count         | Number of rows; `3705` on client 3474                   |
| `+0x08`             | Link[link_count] | links              | See Link                                                |
| `links+0x00`        | String Table     | string_table       | The PABR string table, present but empty                |
| `string_table+0x00` | u32              | string_table_start | Absolute offset of `string_count`; equals `8 + 8 x link_count` |
| `string_table+0x04` | u32              | zero               | Always `0`                                              |

### Link (8 bytes)

| Offset  | Type | Field                 | Notes                                                              |
| ------- | ---- | --------------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | price_follow_item_key | The item whose price follows; unique per row on clients 1784 and 3474 |
| `+0x04` | u32  | price_target_item_key | The item whose price it follows                                    |

Both are item keys below `2^24`, so read as item enchant keys
(`enchant_level << 24 | item_id`) they are level `0` on every row of
clients 1784 and 3474.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Field Names

The `LinkPrice` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `PriceFollowItem` and `PriceTargetItem`. All 2,366
pairs of client 1784 are sheet rows (the sheet has 2,381; 15 more), and
all 2,381 sheet pairs are pairs of client 3474, in the same column order.
The developer workbook (`datasheet_itemdatatable_equip.xlsm`) adds the note
columns `#가격을따라가는아이템명` ("name of the item that follows the
price") and `#가격대상이되는아이템명` ("name of the item that is the
price target"): `Fiery Kutum Shield` and `Kutum Shield` in the first row.

## Notes

- No client Lua names the table; the market and the NPC shops read item
  prices through C++ calls.

## Open Questions

### Which Price Follows

The sheet names say one item's price follows the other's, but not which
price: the Central Market base price, the NPC sell price, or the price a
repair or a cron stone cost is worked out from. Comparing the
`itemenchant.dbss` prices of a few pairs, or the market prices of a
variant and its base item, could tell which.
