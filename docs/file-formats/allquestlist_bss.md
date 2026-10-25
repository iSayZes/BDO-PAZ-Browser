# `allquestlist.bss` Format

## Purpose

Quest order list. The file is a compact `PABR` table of packed quest IDs, one per `quest.dbss` record and in the same physical order as the records in `quest.dbss`. The IDs line up with LOC quest title keys and use the packed ID scheme of `quest.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File               | Bytes  | Records      | Row bytes |
| ------ | -------------- | ------------------ | ------ | ------------ | --------- |
| 1      | 1109 and later | `allquestlist.bss` | 75,984 | 18,991 Entry | 4         |

| Layout | File               | Known             | Unknown    |
| ------ | ------------------ | ----------------- | ---------- |
| 1      | `allquestlist.bss` | 75,984 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `210c7b5c748a`  |
| 3482   | Layout 1 | `210c7b5c748a`  |
| 3474   | Layout 1 | `210c7b5c748a`  |
| 3473   | Layout 1 | `210c7b5c748a`  |
| 3464   | Layout 1 | `210c7b5c748a`  |
| 3458   | Layout 1 | `210c7b5c748a`  |
| 3454   | Layout 1 | `210c7b5c748a`  |
| 3444   | Layout 1 | `210c7b5c748a`  |
| 3435   | Layout 1 | `210c7b5c748a`  |
| 3426   | Layout 1 | `210c7b5c748a`  |
| 3418   | Layout 1 | `210c7b5c748a`  |
| 3412   | Layout 1 | `210c7b5c748a`  |
| 3402   | Layout 1 | `210c7b5c748a`  |
| 3396   | Layout 1 | `210c7b5c748a`  |
| 3387   | Layout 1 | `210c7b5c748a`  |
| 3381   | Layout 1 | `210c7b5c748a`  |
| 3373   | Layout 1 | `210c7b5c748a`  |
| 3364   | Layout 1 | `210c7b5c748a`  |
| 3356   | Layout 1 | `210c7b5c748a`  |
| 3349   | Layout 1 | `210c7b5c748a`  |
| 3342   | Layout 1 | `210c7b5c748a`  |
| 3335   | Layout 1 | `210c7b5c748a`  |
| 3326   | Layout 1 | `210c7b5c748a`  |
| 3321   | Layout 1 | `210c7b5c748a`  |
| 3314   | Layout 1 | `210c7b5c748a`  |
| 3303   | Layout 1 | `210c7b5c748a`  |
| 3302   | Layout 1 | `210c7b5c748a`  |
| 3293   | Layout 1 | `210c7b5c748a`  |
| 3283   | Layout 1 | `210c7b5c748a`  |
| 3275   | Layout 1 | `210c7b5c748a`  |
| 3267   | Layout 1 | `210c7b5c748a`  |
| 3258   | Layout 1 | `210c7b5c748a`  |
| 3251   | Layout 1 | `210c7b5c748a`  |
| 3242   | Layout 1 | `210c7b5c748a`  |
| 3235   | Layout 1 | `210c7b5c748a`  |
| 3229   | Layout 1 | `210c7b5c748a`  |
| 3212   | Layout 1 | `210c7b5c748a`  |
| 3203   | Layout 1 | `210c7b5c748a`  |
| 3193   | Layout 1 | `210c7b5c748a`  |
| 3186   | Layout 1 | `210c7b5c748a`  |
| 3177   | Layout 1 | `210c7b5c748a`  |
| 3169   | Layout 1 | `210c7b5c748a`  |
| 3158   | Layout 1 | `210c7b5c748a`  |
| 3151   | Layout 1 | `210c7b5c748a`  |
| 3144   | Layout 1 | `210c7b5c748a`  |
| 3133   | Layout 1 | `210c7b5c748a`  |
| 3125   | Layout 1 | `210c7b5c748a`  |
| 3118   | Layout 1 | `210c7b5c748a`  |
| 3111   | Layout 1 | `210c7b5c748a`  |
| 3103   | Layout 1 | `210c7b5c748a`  |
| 3095   | Layout 1 | `210c7b5c748a`  |
| 3086   | Layout 1 | `210c7b5c748a`  |
| 3072   | Layout 1 | `210c7b5c748a`  |
| 3062   | Layout 1 | `210c7b5c748a`  |
| 3052   | Layout 1 | `210c7b5c748a`  |
| 3045   | Layout 1 | `210c7b5c748a`  |
| 3037   | Layout 1 | `210c7b5c748a`  |
| 3030   | Layout 1 | `210c7b5c748a`  |
| 3021   | Layout 1 | `210c7b5c748a`  |
| 3012   | Layout 1 | `210c7b5c748a`  |
| 3002   | Layout 1 | `210c7b5c748a`  |
| 2995   | Layout 1 | `210c7b5c748a`  |
| 2987   | Layout 1 | `210c7b5c748a`  |
| 2978   | Layout 1 | `210c7b5c748a`  |
| 2970   | Layout 1 | `210c7b5c748a`  |
| 2959   | Layout 1 | `210c7b5c748a`  |
| 2951   | Layout 1 | `210c7b5c748a`  |
| 2942   | Layout 1 | `210c7b5c748a`  |
| 2935   | Layout 1 | `210c7b5c748a`  |
| 2932   | Layout 1 | `210c7b5c748a`  |
| 2923   | Layout 1 | `210c7b5c748a`  |
| 2919   | Layout 1 | `210c7b5c748a`  |
| 2907   | Layout 1 | `210c7b5c748a`  |
| 2900   | Layout 1 | `210c7b5c748a`  |
| 2891   | Layout 1 | `210c7b5c748a`  |
| 2882   | Layout 1 | `210c7b5c748a`  |
| 2872   | Layout 1 | `210c7b5c748a`  |
| 2863   | Layout 1 | `210c7b5c748a`  |
| 2855   | Layout 1 | `210c7b5c748a`  |
| 2849   | Layout 1 | `210c7b5c748a`  |
| 2844   | Layout 1 | `210c7b5c748a`  |
| 2834   | Layout 1 | `210c7b5c748a`  |
| 2825   | Layout 1 | `210c7b5c748a`  |
| 2819   | Layout 1 | `210c7b5c748a`  |
| 2811   | Layout 1 | `210c7b5c748a`  |
| 2803   | Layout 1 | `210c7b5c748a`  |
| 2794   | Layout 1 | `210c7b5c748a`  |
| 2783   | Layout 1 | `210c7b5c748a`  |
| 2774   | Layout 1 | `210c7b5c748a`  |
| 2765   | Layout 1 | `210c7b5c748a`  |
| 2756   | Layout 1 | `210c7b5c748a`  |
| 2750   | Layout 1 | `210c7b5c748a`  |
| 2743   | Layout 1 | `210c7b5c748a`  |
| 2736   | Layout 1 | `210c7b5c748a`  |
| 2726   | Layout 1 | `210c7b5c748a`  |
| 2717   | Layout 1 | `210c7b5c748a`  |
| 2709   | Layout 1 | `210c7b5c748a`  |
| 2703   | Layout 1 | `210c7b5c748a`  |
| 2695   | Layout 1 | `210c7b5c748a`  |
| 2684   | Layout 1 | `210c7b5c748a`  |
| 2672   | Layout 1 | `210c7b5c748a`  |
| 2665   | Layout 1 | `210c7b5c748a`  |
| 2657   | Layout 1 | `210c7b5c748a`  |
| 2649   | Layout 1 | `210c7b5c748a`  |
| 2644   | Layout 1 | `210c7b5c748a`  |
| 2637   | Layout 1 | `210c7b5c748a`  |
| 2629   | Layout 1 | `210c7b5c748a`  |
| 2619   | Layout 1 | `210c7b5c748a`  |
| 2612   | Layout 1 | `210c7b5c748a`  |
| 2606   | Layout 1 | `210c7b5c748a`  |
| 2602   | Layout 1 | `210c7b5c748a`  |
| 2601   | Layout 1 | `210c7b5c748a`  |
| 2592   | Layout 1 | `210c7b5c748a`  |
| 2583   | Layout 1 | `210c7b5c748a`  |
| 2575   | Layout 1 | `210c7b5c748a`  |
| 2567   | Layout 1 | `210c7b5c748a`  |
| 2560   | Layout 1 | `210c7b5c748a`  |
| 2553   | Layout 1 | `210c7b5c748a`  |
| 2545   | Layout 1 | `210c7b5c748a`  |
| 2538   | Layout 1 | `210c7b5c748a`  |
| 2529   | Layout 1 | `210c7b5c748a`  |
| 2519   | Layout 1 | `210c7b5c748a`  |
| 2513   | Layout 1 | `210c7b5c748a`  |
| 2510   | Layout 1 | `210c7b5c748a`  |
| 2507   | Layout 1 | `210c7b5c748a`  |
| 2503   | Layout 1 | `210c7b5c748a`  |
| 2498   | Layout 1 | `210c7b5c748a`  |
| 2492   | Layout 1 | `210c7b5c748a`  |
| 2487   | Layout 1 | `210c7b5c748a`  |
| 2480   | Layout 1 | `210c7b5c748a`  |
| 2474   | Layout 1 | `210c7b5c748a`  |
| 2468   | Layout 1 | `210c7b5c748a`  |
| 2460   | Layout 1 | `210c7b5c748a`  |
| 2453   | Layout 1 | `210c7b5c748a`  |
| 2444   | Layout 1 | `210c7b5c748a`  |
| 2438   | Layout 1 | `210c7b5c748a`  |
| 2434   | Layout 1 | `210c7b5c748a`  |
| 2429   | Layout 1 | `210c7b5c748a`  |
| 2421   | Layout 1 | `210c7b5c748a`  |
| 2414   | Layout 1 | `210c7b5c748a`  |
| 2407   | Layout 1 | `210c7b5c748a`  |
| 2401   | Layout 1 | `210c7b5c748a`  |
| 2397   | Layout 1 | `210c7b5c748a`  |
| 2393   | Layout 1 | `210c7b5c748a`  |
| 2384   | Layout 1 | `210c7b5c748a`  |
| 2378   | Layout 1 | `210c7b5c748a`  |
| 2372   | Layout 1 | `210c7b5c748a`  |
| 2358   | Layout 1 | `210c7b5c748a`  |
| 2352   | Layout 1 | `210c7b5c748a`  |
| 2347   | Layout 1 | `210c7b5c748a`  |
| 2343   | Layout 1 | `210c7b5c748a`  |
| 2335   | Layout 1 | `210c7b5c748a`  |
| 2327   | Layout 1 | `210c7b5c748a`  |
| 2324   | Layout 1 | `210c7b5c748a`  |
| 2319   | Layout 1 | `210c7b5c748a`  |
| 2313   | Layout 1 | `210c7b5c748a`  |
| 2308   | Layout 1 | `210c7b5c748a`  |
| 2302   | Layout 1 | `210c7b5c748a`  |
| 2295   | Layout 1 | `210c7b5c748a`  |
| 2290   | Layout 1 | `210c7b5c748a`  |
| 2284   | Layout 1 | `210c7b5c748a`  |
| 2276   | Layout 1 | `210c7b5c748a`  |
| 2269   | Layout 1 | `210c7b5c748a`  |
| 2259   | Layout 1 | `210c7b5c748a`  |
| 2250   | Layout 1 | `210c7b5c748a`  |
| 2243   | Layout 1 | `210c7b5c748a`  |
| 2235   | Layout 1 | `210c7b5c748a`  |
| 2229   | Layout 1 | `210c7b5c748a`  |
| 2224   | Layout 1 | `210c7b5c748a`  |
| 2218   | Layout 1 | `210c7b5c748a`  |
| 2215   | Layout 1 | `210c7b5c748a`  |
| 2207   | Layout 1 | `210c7b5c748a`  |
| 2203   | Layout 1 | `210c7b5c748a`  |
| 2196   | Layout 1 | `210c7b5c748a`  |
| 2192   | Layout 1 | `210c7b5c748a`  |
| 2189   | Layout 1 | `210c7b5c748a`  |
| 2183   | Layout 1 | `210c7b5c748a`  |
| 2179   | Layout 1 | `210c7b5c748a`  |
| 2171   | Layout 1 | `210c7b5c748a`  |
| 2163   | Layout 1 | `210c7b5c748a`  |
| 2156   | Layout 1 | `210c7b5c748a`  |
| 2151   | Layout 1 | `210c7b5c748a`  |
| 2147   | Layout 1 | `210c7b5c748a`  |
| 2142   | Layout 1 | `210c7b5c748a`  |
| 2138   | Layout 1 | `210c7b5c748a`  |
| 2134   | Layout 1 | `210c7b5c748a`  |
| 2130   | Layout 1 | `210c7b5c748a`  |
| 2122   | Layout 1 | `210c7b5c748a`  |
| 2107   | Layout 1 | `210c7b5c748a`  |
| 2098   | Layout 1 | `210c7b5c748a`  |
| 2089   | Layout 1 | `210c7b5c748a`  |
| 2081   | Layout 1 | `210c7b5c748a`  |
| 2073   | Layout 1 | `210c7b5c748a`  |
| 2067   | Layout 1 | `210c7b5c748a`  |
| 2063   | Layout 1 | `210c7b5c748a`  |
| 2059   | Layout 1 | `210c7b5c748a`  |
| 2052   | Layout 1 | `210c7b5c748a`  |
| 2044   | Layout 1 | `210c7b5c748a`  |
| 2039   | Layout 1 | `210c7b5c748a`  |
| 2032   | Layout 1 | `210c7b5c748a`  |
| 2025   | Layout 1 | `210c7b5c748a`  |
| 2011   | Layout 1 | `210c7b5c748a`  |
| 2005   | Layout 1 | `210c7b5c748a`  |
| 2000   | Layout 1 | `210c7b5c748a`  |
| 1996   | Layout 1 | `210c7b5c748a`  |
| 1991   | Layout 1 | `210c7b5c748a`  |
| 1985   | Layout 1 | `210c7b5c748a`  |
| 1980   | Layout 1 | `210c7b5c748a`  |
| 1969   | Layout 1 | `210c7b5c748a`  |
| 1964   | Layout 1 | `210c7b5c748a`  |
| 1958   | Layout 1 | `210c7b5c748a`  |
| 1950   | Layout 1 | `210c7b5c748a`  |
| 1945   | Layout 1 | `210c7b5c748a`  |
| 1937   | Layout 1 | `210c7b5c748a`  |
| 1933   | Layout 1 | `210c7b5c748a`  |
| 1927   | Layout 1 | `210c7b5c748a`  |
| 1921   | Layout 1 | `210c7b5c748a`  |
| 1914   | Layout 1 | `210c7b5c748a`  |
| 1908   | Layout 1 | `210c7b5c748a`  |
| 1897   | Layout 1 | `210c7b5c748a`  |
| 1892   | Layout 1 | `210c7b5c748a`  |
| 1886   | Layout 1 | `210c7b5c748a`  |
| 1881   | Layout 1 | `210c7b5c748a`  |
| 1871   | Layout 1 | `210c7b5c748a`  |
| 1866   | Layout 1 | `210c7b5c748a`  |
| 1862   | Layout 1 | `210c7b5c748a`  |
| 1854   | Layout 1 | `210c7b5c748a`  |
| 1846   | Layout 1 | `210c7b5c748a`  |
| 1838   | Layout 1 | `210c7b5c748a`  |
| 1832   | Layout 1 | `210c7b5c748a`  |
| 1826   | Layout 1 | `210c7b5c748a`  |
| 1822   | Layout 1 | `210c7b5c748a`  |
| 1818   | Layout 1 | `210c7b5c748a`  |
| 1804   | Layout 1 | `210c7b5c748a`  |
| 1794   | Layout 1 | `210c7b5c748a`  |
| 1790   | Layout 1 | `210c7b5c748a`  |
| 1784   | Layout 1 | `210c7b5c748a`  |
| 1774   | Layout 1 | `210c7b5c748a`  |
| 1771   | Layout 1 | `210c7b5c748a`  |
| 1762   | Layout 1 | `210c7b5c748a`  |
| 1759   | Layout 1 | `210c7b5c748a`  |
| 1754   | Layout 1 | `210c7b5c748a`  |
| 1749   | Layout 1 | `210c7b5c748a`  |
| 1743   | Layout 1 | `210c7b5c748a`  |
| 1737   | Layout 1 | `210c7b5c748a`  |
| 1731   | Layout 1 | `210c7b5c748a`  |
| 1725   | Layout 1 | `210c7b5c748a`  |
| 1717   | Layout 1 | `210c7b5c748a`  |
| 1710   | Layout 1 | `210c7b5c748a`  |
| 1704   | Layout 1 | `210c7b5c748a`  |
| 1698   | Layout 1 | `210c7b5c748a`  |
| 1690   | Layout 1 | `210c7b5c748a`  |
| 1685   | Layout 1 | `210c7b5c748a`  |
| 1680   | Layout 1 | `210c7b5c748a`  |
| 1674   | Layout 1 | `210c7b5c748a`  |
| 1668   | Layout 1 | `210c7b5c748a`  |
| 1659   | Layout 1 | `210c7b5c748a`  |
| 1649   | Layout 1 | `210c7b5c748a`  |
| 1642   | Layout 1 | `210c7b5c748a`  |
| 1636   | Layout 1 | `210c7b5c748a`  |
| 1628   | Layout 1 | `210c7b5c748a`  |
| 1622   | Layout 1 | `210c7b5c748a`  |
| 1614   | Layout 1 | `210c7b5c748a`  |
| 1608   | Layout 1 | `210c7b5c748a`  |
| 1602   | Layout 1 | `210c7b5c748a`  |
| 1598   | Layout 1 | `210c7b5c748a`  |
| 1594   | Layout 1 | `210c7b5c748a`  |
| 1590   | Layout 1 | `210c7b5c748a`  |
| 1587   | Layout 1 | `210c7b5c748a`  |
| 1584   | Layout 1 | `210c7b5c748a`  |
| 1579   | Layout 1 | `210c7b5c748a`  |
| 1572   | Layout 1 | `210c7b5c748a`  |
| 1565   | Layout 1 | `210c7b5c748a`  |
| 1559   | Layout 1 | `210c7b5c748a`  |
| 1554   | Layout 1 | `210c7b5c748a`  |
| 1547   | Layout 1 | `210c7b5c748a`  |
| 1537   | Layout 1 | `210c7b5c748a`  |
| 1529   | Layout 1 | `210c7b5c748a`  |
| 1524   | Layout 1 | `210c7b5c748a`  |
| 1519   | Layout 1 | `210c7b5c748a`  |
| 1509   | Layout 1 | `210c7b5c748a`  |
| 1506   | Layout 1 | `210c7b5c748a`  |
| 1504   | Layout 1 | `210c7b5c748a`  |
| 1500   | Layout 1 | `210c7b5c748a`  |
| 1493   | Layout 1 | `210c7b5c748a`  |
| 1489   | Layout 1 | `210c7b5c748a`  |
| 1485   | Layout 1 | `210c7b5c748a`  |
| 1481   | Layout 1 | `210c7b5c748a`  |
| 1474   | Layout 1 | `210c7b5c748a`  |
| 1466   | Layout 1 | `210c7b5c748a`  |
| 1462   | Layout 1 | `210c7b5c748a`  |
| 1459   | Layout 1 | `210c7b5c748a`  |
| 1453   | Layout 1 | `210c7b5c748a`  |
| 1450   | Layout 1 | `210c7b5c748a`  |
| 1445   | Layout 1 | `210c7b5c748a`  |
| 1439   | Layout 1 | `210c7b5c748a`  |
| 1433   | Layout 1 | `210c7b5c748a`  |
| 1430   | Layout 1 | `210c7b5c748a`  |
| 1426   | Layout 1 | `210c7b5c748a`  |
| 1421   | Layout 1 | `210c7b5c748a`  |
| 1417   | Layout 1 | `210c7b5c748a`  |
| 1416   | Layout 1 | `210c7b5c748a`  |
| 1409   | Layout 1 | `210c7b5c748a`  |
| 1405   | Layout 1 | `210c7b5c748a`  |
| 1401   | Layout 1 | `210c7b5c748a`  |
| 1396   | Layout 1 | `210c7b5c748a`  |
| 1391   | Layout 1 | `210c7b5c748a`  |
| 1390   | Layout 1 | `210c7b5c748a`  |
| 1386   | Layout 1 | `210c7b5c748a`  |
| 1381   | Layout 1 | `210c7b5c748a`  |
| 1379   | Layout 1 | `210c7b5c748a`  |
| 1372   | Layout 1 | `210c7b5c748a`  |
| 1366   | Layout 1 | `210c7b5c748a`  |
| 1364   | Layout 1 | `210c7b5c748a`  |
| 1363   | Layout 1 | `210c7b5c748a`  |
| 1360   | Layout 1 | `210c7b5c748a`  |
| 1358   | Layout 1 | `210c7b5c748a`  |
| 1355   | Layout 1 | `210c7b5c748a`  |
| 1351   | Layout 1 | `210c7b5c748a`  |
| 1348   | Layout 1 | `210c7b5c748a`  |
| 1346   | Layout 1 | `210c7b5c748a`  |
| 1341   | Layout 1 | `210c7b5c748a`  |
| 1340   | Layout 1 | `210c7b5c748a`  |
| 1338   | Layout 1 | `210c7b5c748a`  |
| 1335   | Layout 1 | `210c7b5c748a`  |
| 1333   | Layout 1 | `210c7b5c748a`  |
| 1329   | Layout 1 | `210c7b5c748a`  |
| 1327   | Layout 1 | `210c7b5c748a`  |
| 1324   | Layout 1 | `210c7b5c748a`  |
| 1321   | Layout 1 | `210c7b5c748a`  |
| 1319   | Layout 1 | `210c7b5c748a`  |
| 1318   | Layout 1 | `210c7b5c748a`  |
| 1316   | Layout 1 | `210c7b5c748a`  |
| 1313   | Layout 1 | `210c7b5c748a`  |
| 1311   | Layout 1 | `210c7b5c748a`  |
| 1309   | Layout 1 | `210c7b5c748a`  |
| 1304   | Layout 1 | `210c7b5c748a`  |
| 1292   | Layout 1 | `210c7b5c748a`  |
| 1286   | Layout 1 | `210c7b5c748a`  |
| 1280   | Layout 1 | `210c7b5c748a`  |
| 1276   | Layout 1 | `210c7b5c748a`  |
| 1267   | Layout 1 | `210c7b5c748a`  |
| 1261   | Layout 1 | `210c7b5c748a`  |
| 1256   | Layout 1 | `210c7b5c748a`  |
| 1250   | Layout 1 | `210c7b5c748a`  |
| 1246   | No file  | `210c7b5c748a`  |
| 1239   | No file  | `210c7b5c748a`  |
| 1230   | No file  | `210c7b5c748a`  |
| 1226   | No file  | `210c7b5c748a`  |
| 1220   | No file  | `210c7b5c748a`  |
| 1217   | No file  | `210c7b5c748a`  |
| 1211   | No file  | `210c7b5c748a`  |
| 1210   | No file  | `210c7b5c748a`  |
| 1208   | No file  | `210c7b5c748a`  |
| 1203   | No file  | `210c7b5c748a`  |
| 1197   | No file  | `210c7b5c748a`  |
| 1194   | No file  | `210c7b5c748a`  |
| 1192   | No file  | `210c7b5c748a`  |
| 1187   | No file  | `210c7b5c748a`  |
| 1183   | No file  | `210c7b5c748a`  |
| 1177   | No file  | `210c7b5c748a`  |
| 1173   | No file  | `210c7b5c748a`  |
| 1167   | No file  | `210c7b5c748a`  |
| 1164   | No file  | `210c7b5c748a`  |
| 1156   | No file  | `210c7b5c748a`  |
| 1149   | No file  | `210c7b5c748a`  |
| 1144   | Layout 1 | `210c7b5c748a`  |
| 1137   | Layout 1 | `210c7b5c748a`  |
| 1132   | Layout 1 | `210c7b5c748a`  |
| 1127   | Layout 1 | `210c7b5c748a`  |
| 1122   | Layout 1 | `210c7b5c748a`  |
| 1118   | Layout 1 | `210c7b5c748a`  |
| 1114   | Layout 1 | `210c7b5c748a`  |
| 1109   | Layout 1 | `210c7b5c748a`  |
| 1102   | No file  | `210c7b5c748a`  |
| 1096   | No file  | `210c7b5c748a`  |
| 1088   | No file  | `210c7b5c748a`  |
| 1081   | No file  | `210c7b5c748a`  |
| 1076   | No file  | `210c7b5c748a`  |
| 1069   | No file  | `210c7b5c748a`  |
| 1064   | No file  | `210c7b5c748a`  |
| 1058   | No file  | `210c7b5c748a`  |
| 1051   | No file  | `210c7b5c748a`  |
| 1044   | No file  | `210c7b5c748a`  |
| 1036   | No file  | `210c7b5c748a`  |
| 1026   | No file  | `210c7b5c748a`  |
| 1016   | No file  | `210c7b5c748a`  |
| 1009   | No file  | `210c7b5c748a`  |
| 1005   | No file  | `210c7b5c748a`  |
| 1000   | No file  | `210c7b5c748a`  |
| 998    | No file  | `210c7b5c748a`  |
| 990    | No file  | `210c7b5c748a`  |
| 979    | No file  | `210c7b5c748a`  |
| 972    | No file  | `210c7b5c748a`  |
| 963    | No file  | `210c7b5c748a`  |
| 955    | No file  | `210c7b5c748a`  |
| 946    | No file  | `210c7b5c748a`  |
| 938    | No file  | `210c7b5c748a`  |
| 927    | No file  | `210c7b5c748a`  |
| 911    | No file  | `210c7b5c748a`  |
| 904    | No file  | `210c7b5c748a`  |
| 899    | No file  | `210c7b5c748a`  |
| 894    | No file  | `210c7b5c748a`  |
| 885    | No file  | `210c7b5c748a`  |
| 879    | No file  | `210c7b5c748a`  |
| 872    | No file  | `210c7b5c748a`  |
| 864    | No file  | `210c7b5c748a`  |
| 855    | No file  | `210c7b5c748a`  |
| 853    | No file  | `210c7b5c748a`  |
| 845    | No file  | `210c7b5c748a`  |
| 837    | No file  | `210c7b5c748a`  |
| 829    | No file  | `210c7b5c748a`  |
| 822    | No file  | `210c7b5c748a`  |
| 814    | No file  | `210c7b5c748a`  |
| 805    | No file  | `210c7b5c748a`  |
| 794    | No file  | `210c7b5c748a`  |
| 787    | No file  | `210c7b5c748a`  |
| 780    | No file  | `210c7b5c748a`  |
| 771    | No file  | `210c7b5c748a`  |
| 760    | No file  | `210c7b5c748a`  |
| 748    | No file  | `210c7b5c748a`  |
| 741    | No file  | `210c7b5c748a`  |
| 736    | No file  | `210c7b5c748a`  |
| 731    | No file  | `210c7b5c748a`  |
| 723    | No file  | `210c7b5c748a`  |
| 711    | No file  | `210c7b5c748a`  |
| 707    | No file  | `210c7b5c748a`  |
| 697    | No file  | `210c7b5c748a`  |
| 689    | No file  | `210c7b5c748a`  |
| 683    | No file  | `210c7b5c748a`  |
| 678    | No file  | `210c7b5c748a`  |
| 670    | No file  | `210c7b5c748a`  |
| 661    | No file  | `210c7b5c748a`  |
| 656    | No file  | `210c7b5c748a`  |
| 652    | No file  | `210c7b5c748a`  |
| 643    | No file  | `210c7b5c748a`  |
| 637    | No file  | `210c7b5c748a`  |
| 630    | No file  | `210c7b5c748a`  |
| 627    | No file  | `210c7b5c748a`  |
| 621    | No file  | `210c7b5c748a`  |
| 617    | No file  | `210c7b5c748a`  |
| 615    | No file  | `210c7b5c748a`  |
| 606    | No file  | `210c7b5c748a`  |
| 599    | No file  | `210c7b5c748a`  |
| 592    | No file  | `210c7b5c748a`  |
| 586    | No file  | `210c7b5c748a`  |
| 577    | No file  | `210c7b5c748a`  |
| 569    | No file  | `210c7b5c748a`  |
| 561    | No file  | `210c7b5c748a`  |
| 554    | No file  | `210c7b5c748a`  |
| 542    | No file  | `210c7b5c748a`  |
| 532    | No file  | `210c7b5c748a`  |
| 531    | No file  | `210c7b5c748a`  |
| 526    | No file  | `210c7b5c748a`  |
| 521    | No file  | `210c7b5c748a`  |
| 517    | No file  | `210c7b5c748a`  |
| 510    | No file  | `210c7b5c748a`  |
| 508    | No file  | `210c7b5c748a`  |
| 504    | No file  | `210c7b5c748a`  |
| 497    | No file  | `210c7b5c748a`  |
| 491    | No file  | `210c7b5c748a`  |
| 485    | No file  | `210c7b5c748a`  |
| 478    | No file  | `210c7b5c748a`  |
| 472    | No file  | `210c7b5c748a`  |
| 466    | No file  | `210c7b5c748a`  |
| 457    | No file  | `210c7b5c748a`  |
| 452    | No file  | `210c7b5c748a`  |
| 449    | No file  | `210c7b5c748a`  |
| 435    | No file  | `210c7b5c748a`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `quest.dbss`          | Optional | Quest records, stored in the same order as this list                 |
| `acceptquest.bss`     | Optional | The NPC dialog that gives each quest of this list                     |
| `completequest.bss`   | Optional | The NPC dialog that takes each quest of this list                     |
| `mainquest.bss`       | Optional | Provides main-quest UI sequence groups for a subset of quest IDs      |
| `newquest.bss`        | Optional | Provides new-quest UI sequence groups for a subset of quest IDs       |
| `languagedata_en.loc` | Optional | Provides quest title/objective text for display via LOC type `18`    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field          | Notes                                           |
| ------------------- | -------------- | -------------- | ----------------------------------------------- |
| `+0x00`             | char[4]        | magic          | `PABR` (ASCII)                                  |
| `+0x04`             | u32            | count          | Number of entries; `19,327` after the 2026-09-27 client update, `18,988` before it, `19,599` fixture |
| `+0x08`             | Entry[count]   | entries        | See Entry                                       |
| `entries+0x00`      | String Table   | string_table   | The 12-byte trailer starts here; see String Table |
| `string_table+0x00` | u32            | end_of_entries | Byte offset immediately after entries, `8 + count × 4` |
| `string_table+0x04` | u32            | zero           | Observed `0`                                    |

### Entry (4 bytes)

| Offset  | Type | Field           | Notes                                                     |
| ------- | ---- | --------------- | --------------------------------------------------------- |
| `+0x00` | u32  | packed_quest_id | Packed as `(quest_id << 16) \| quest_chain_id`; split into `quest_chain_id` and `quest_id` |

Derived fields:

```text
quest_chain_id = packed_quest_id & 0xFFFF
quest_id       = packed_quest_id >> 16
```

### String Table (variable: 4 bytes + strings)

The PABR string table of `acceptquest.bss`, here with no strings.

| Offset  | Type               | Field        | Notes        |
| ------- | ------------------ | ------------ | ------------ |
| `+0x00` | u32                | string_count | Observed `0` |
| `+0x04` | pstr[string_count] | strings      | Empty        |

## Reference Rows

Current client data (`files/allquestlist.bss`):

| Slot  | Packed Quest ID | Chain ID | Quest ID | LOC Title (type 18, `id4=0`)                                     |
| ----- | --------------- | -------- | -------- | ---------------------------------------------------------------- |
| 0     | `795132`        | `8700`   | `12`     | `[Storybook] Tale of the Mudang Wraith`                          |
| 1     | `138172`        | `7100`   | `2`      | `[Processing] The Beauty of Planks`                              |
| 2     | `196891`        | `283`    | `3`      | `Exalted Character III`                                          |
| 18987 | `181218`        | `50146`  | `2`      | `A Whole New Experience Presented by Fughar! (Black Spirit Pass)` |

The older fixture starts with `1050655` (chain `2079`, quest `16`, `[Elvia Weekly] Gigagord`) and also ends with `181218`.

## Notes

- Current file: `75,972` bytes, `18,988` entries, `end_of_entries = 75,960`. After the 2026-09-27 update: `77,328` bytes, `19,327` entries, `end_of_entries = 77,316`. Fixture: `78,416` bytes, `19,599` entries, `end_of_entries = 78,404` (`0x13244`). All three match `8 + count × 4 + 12`.
- `count` equals the `quest.dbss` header count in all three versions, and all entries are distinct.
- Physical order: walking `quest.dbss` sequentially, record `i` carries packed quest ID `entry[i]` at the start of its fixed block (after its objective text) and again in its trailing echo. The walk succeeds for all `18,988` current, `19,327` updated and `19,599` fixture records, so this list is the record-order index for `quest.dbss` (as stated by [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)). See [quest_dbss.md](quest_dbss.md) for the record layout.
- The list is not a byte offset table; it stores IDs only, so record offsets still have to be found by walking `quest.dbss`.
- The entry encoding matches the packed quest ID relationship documented in `questgroup.dbss`.
- [`doguildquestlist.bss`](doguildquestlist_bss.md), [`growthpassquestlist.bss`](growthpassquestlist_bss.md), the three [Olvia Academy lists](olviaacademyquestlist_bss.md), [`regionmonsterkillquestlist.bss`](regionmonsterkillquestlist_bss.md), [`specialquestlist.bss`](specialquestlist_bss.md), [`supplyservantquestlist.bss`](supplyservantquestlist_bss.md) and the three [Black Spirit Pass lists](seasonpassquestlist_bss.md) use this layout and handler. [`questprogressgroup.bss`](questprogressgroup_bss.md) does not: it stores unpacked u16 chain and quest IDs in its own group layout.
- All 827 adventure-journal page quests from `journalquest.dbss` are in the current list.
- LOC coverage: `18,961` of `18,988` current entries (fixture: `19,455` of `19,599`) have a LOC type `18`, `str_id4=0` title row keyed by `(quest_chain_id, quest_id)`.
