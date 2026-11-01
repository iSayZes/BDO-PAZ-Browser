# `interiorrelationpoint.dbss` Format

## Purpose

Placement points of the house furniture: one 66-byte row per furniture
character with the chair that matches it and a point value for each piece
of furniture it can stand on (dresser, bedside cabinet, table, shelf and
more) and for each free side (front, back, left, right). The matching
character pairs a table with its chair: Melissande Table (`6252`) and
Melissande Dining Table (`6251`) both match Melissande Chair (`6751`).
On client 3482 the file holds 1,140 rows, 966 on client 1784. Companion
`interiorrelationpointoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes  | Records          | Row bytes |
| ------ | -------------- | ---------------------------------- | ------ | ---------------- | --------- |
| 1      | 1346 and later | `interiorrelationpoint.dbss`       | 75,260 | 1,140 Row        | 66        |
| 1      | 1346 and later | `interiorrelationpointoffset.dbss` | 11,420 | 1,140 Offset Row | 10        |

| Layout | File                               | Known             | Unknown    |
| ------ | ---------------------------------- | ----------------- | ---------- |
| 1      | `interiorrelationpoint.dbss`       | 75,260 B (100.0%) | 0 B (0.0%) |
| 1      | `interiorrelationpointoffset.dbss` | 11,420 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `f0e347ea9f51`  |
| 3482   | Layout 1             | `f0e347ea9f51`  |
| 3474   | Layout 1             | `f0e347ea9f51`  |
| 3473   | Layout 1             | `f0e347ea9f51`  |
| 3464   | Layout 1             | `f0e347ea9f51`  |
| 3458   | Layout 1             | `f0e347ea9f51`  |
| 3454   | Layout 1             | `f0e347ea9f51`  |
| 3444   | Layout 1             | `f0e347ea9f51`  |
| 3435   | Layout 1             | `f0e347ea9f51`  |
| 3426   | Layout 1             | `f0e347ea9f51`  |
| 3418   | Layout 1             | `f0e347ea9f51`  |
| 3412   | Layout 1             | `f0e347ea9f51`  |
| 3402   | Layout 1             | `f0e347ea9f51`  |
| 3396   | Layout 1             | `f0e347ea9f51`  |
| 3387   | Layout 1             | `f0e347ea9f51`  |
| 3381   | Layout 1             | `f0e347ea9f51`  |
| 3373   | Layout 1             | `f0e347ea9f51`  |
| 3364   | Layout 1             | `f0e347ea9f51`  |
| 3356   | Layout 1             | `f0e347ea9f51`  |
| 3349   | Layout 1             | `f0e347ea9f51`  |
| 3342   | Layout 1             | `f0e347ea9f51`  |
| 3335   | Layout 1             | `f0e347ea9f51`  |
| 3326   | Layout 1             | `f0e347ea9f51`  |
| 3321   | Layout 1             | `f0e347ea9f51`  |
| 3314   | Layout 1             | `f0e347ea9f51`  |
| 3303   | Layout 1             | `f0e347ea9f51`  |
| 3302   | Layout 1             | `f0e347ea9f51`  |
| 3293   | Layout 1             | `f0e347ea9f51`  |
| 3283   | Layout 1             | `f0e347ea9f51`  |
| 3275   | Layout 1             | `f0e347ea9f51`  |
| 3267   | Layout 1             | `f0e347ea9f51`  |
| 3258   | Layout 1             | `f0e347ea9f51`  |
| 3251   | Layout 1             | `f0e347ea9f51`  |
| 3242   | Layout 1             | `f0e347ea9f51`  |
| 3235   | Layout 1             | `f0e347ea9f51`  |
| 3229   | Layout 1             | `f0e347ea9f51`  |
| 3212   | Layout 1             | `f0e347ea9f51`  |
| 3203   | Layout 1             | `f0e347ea9f51`  |
| 3193   | Layout 1             | `f0e347ea9f51`  |
| 3186   | Layout 1             | `f0e347ea9f51`  |
| 3177   | Layout 1             | `f0e347ea9f51`  |
| 3169   | Layout 1             | `f0e347ea9f51`  |
| 3158   | Layout 1             | `f0e347ea9f51`  |
| 3151   | Layout 1             | `f0e347ea9f51`  |
| 3144   | Layout 1             | `f0e347ea9f51`  |
| 3133   | Layout 1             | `f0e347ea9f51`  |
| 3125   | Layout 1             | `f0e347ea9f51`  |
| 3118   | Layout 1             | `f0e347ea9f51`  |
| 3111   | Layout 1             | `f0e347ea9f51`  |
| 3103   | Layout 1             | `f0e347ea9f51`  |
| 3095   | Layout 1             | `f0e347ea9f51`  |
| 3086   | Layout 1             | `f0e347ea9f51`  |
| 3072   | Layout 1             | `f0e347ea9f51`  |
| 3062   | Layout 1             | `f0e347ea9f51`  |
| 3052   | Layout 1             | `f0e347ea9f51`  |
| 3045   | Layout 1             | `f0e347ea9f51`  |
| 3037   | Layout 1             | `f0e347ea9f51`  |
| 3030   | Layout 1             | `f0e347ea9f51`  |
| 3021   | Layout 1             | `f0e347ea9f51`  |
| 3012   | Layout 1             | `f0e347ea9f51`  |
| 3002   | Layout 1             | `f0e347ea9f51`  |
| 2995   | Layout 1             | `f0e347ea9f51`  |
| 2987   | Layout 1             | `f0e347ea9f51`  |
| 2978   | Layout 1             | `f0e347ea9f51`  |
| 2970   | Layout 1             | `f0e347ea9f51`  |
| 2959   | Layout 1             | `f0e347ea9f51`  |
| 2951   | Layout 1             | `f0e347ea9f51`  |
| 2942   | Layout 1             | `f0e347ea9f51`  |
| 2935   | Layout 1             | `f0e347ea9f51`  |
| 2932   | Layout 1             | `f0e347ea9f51`  |
| 2923   | Layout 1             | `f0e347ea9f51`  |
| 2919   | Layout 1             | `f0e347ea9f51`  |
| 2907   | Layout 1             | `f0e347ea9f51`  |
| 2900   | Layout 1             | `f0e347ea9f51`  |
| 2891   | Layout 1             | `f0e347ea9f51`  |
| 2882   | Layout 1             | `f0e347ea9f51`  |
| 2872   | Layout 1             | `f0e347ea9f51`  |
| 2863   | Layout 1             | `f0e347ea9f51`  |
| 2855   | Layout 1             | `f0e347ea9f51`  |
| 2849   | Layout 1             | `f0e347ea9f51`  |
| 2844   | Layout 1             | `f0e347ea9f51`  |
| 2834   | Layout 1             | `f0e347ea9f51`  |
| 2825   | Layout 1             | `f0e347ea9f51`  |
| 2819   | Layout 1             | `f0e347ea9f51`  |
| 2811   | Layout 1             | `f0e347ea9f51`  |
| 2803   | Layout 1             | `f0e347ea9f51`  |
| 2794   | Layout 1             | `f0e347ea9f51`  |
| 2783   | Layout 1             | `f0e347ea9f51`  |
| 2774   | Layout 1             | `f0e347ea9f51`  |
| 2765   | Layout 1             | `f0e347ea9f51`  |
| 2756   | Layout 1             | `f0e347ea9f51`  |
| 2750   | Layout 1             | `f0e347ea9f51`  |
| 2743   | Layout 1             | `f0e347ea9f51`  |
| 2736   | Layout 1             | `f0e347ea9f51`  |
| 2726   | Layout 1             | `f0e347ea9f51`  |
| 2717   | Layout 1             | `f0e347ea9f51`  |
| 2709   | Layout 1             | `f0e347ea9f51`  |
| 2703   | Layout 1             | `f0e347ea9f51`  |
| 2695   | Layout 1             | `f0e347ea9f51`  |
| 2684   | Layout 1             | `f0e347ea9f51`  |
| 2672   | Layout 1             | `f0e347ea9f51`  |
| 2665   | Layout 1             | `f0e347ea9f51`  |
| 2657   | Layout 1             | `f0e347ea9f51`  |
| 2649   | Layout 1             | `f0e347ea9f51`  |
| 2644   | Layout 1             | `f0e347ea9f51`  |
| 2637   | Layout 1             | `f0e347ea9f51`  |
| 2629   | Layout 1             | `f0e347ea9f51`  |
| 2619   | Layout 1             | `f0e347ea9f51`  |
| 2612   | Layout 1             | `f0e347ea9f51`  |
| 2606   | Layout 1             | `f0e347ea9f51`  |
| 2602   | Layout 1             | `f0e347ea9f51`  |
| 2601   | Layout 1             | `f0e347ea9f51`  |
| 2592   | Layout 1             | `f0e347ea9f51`  |
| 2583   | Layout 1             | `f0e347ea9f51`  |
| 2575   | Layout 1             | `f0e347ea9f51`  |
| 2567   | Layout 1             | `f0e347ea9f51`  |
| 2560   | Layout 1             | `f0e347ea9f51`  |
| 2553   | Layout 1             | `f0e347ea9f51`  |
| 2545   | Layout 1             | `f0e347ea9f51`  |
| 2538   | Layout 1             | `f0e347ea9f51`  |
| 2529   | Layout 1             | `f0e347ea9f51`  |
| 2519   | Layout 1             | `f0e347ea9f51`  |
| 2513   | Layout 1             | `f0e347ea9f51`  |
| 2510   | Layout 1             | `f0e347ea9f51`  |
| 2507   | Layout 1             | `f0e347ea9f51`  |
| 2503   | Layout 1             | `f0e347ea9f51`  |
| 2498   | Layout 1             | `f0e347ea9f51`  |
| 2492   | Layout 1             | `f0e347ea9f51`  |
| 2487   | Layout 1             | `f0e347ea9f51`  |
| 2480   | Layout 1             | `f0e347ea9f51`  |
| 2474   | Layout 1             | `f0e347ea9f51`  |
| 2468   | Layout 1             | `f0e347ea9f51`  |
| 2460   | Layout 1             | `f0e347ea9f51`  |
| 2453   | Layout 1             | `f0e347ea9f51`  |
| 2444   | Layout 1             | `f0e347ea9f51`  |
| 2438   | Layout 1             | `f0e347ea9f51`  |
| 2434   | Layout 1             | `f0e347ea9f51`  |
| 2429   | Layout 1             | `f0e347ea9f51`  |
| 2421   | Layout 1             | `f0e347ea9f51`  |
| 2414   | Layout 1             | `f0e347ea9f51`  |
| 2407   | Layout 1             | `f0e347ea9f51`  |
| 2401   | Layout 1             | `f0e347ea9f51`  |
| 2397   | Layout 1             | `f0e347ea9f51`  |
| 2393   | Layout 1             | `f0e347ea9f51`  |
| 2384   | Layout 1             | `f0e347ea9f51`  |
| 2378   | Layout 1             | `f0e347ea9f51`  |
| 2372   | Layout 1             | `f0e347ea9f51`  |
| 2358   | Layout 1             | `f0e347ea9f51`  |
| 2352   | Layout 1             | `f0e347ea9f51`  |
| 2347   | Layout 1             | `f0e347ea9f51`  |
| 2343   | Layout 1             | `f0e347ea9f51`  |
| 2335   | Layout 1             | `f0e347ea9f51`  |
| 2327   | Layout 1             | `f0e347ea9f51`  |
| 2324   | Layout 1             | `f0e347ea9f51`  |
| 2319   | Layout 1             | `f0e347ea9f51`  |
| 2313   | Layout 1             | `f0e347ea9f51`  |
| 2308   | Layout 1             | `f0e347ea9f51`  |
| 2302   | Layout 1             | `f0e347ea9f51`  |
| 2295   | Layout 1             | `f0e347ea9f51`  |
| 2290   | Layout 1             | `f0e347ea9f51`  |
| 2284   | Layout 1             | `f0e347ea9f51`  |
| 2276   | Layout 1             | `f0e347ea9f51`  |
| 2269   | Layout 1             | `f0e347ea9f51`  |
| 2259   | Layout 1             | `f0e347ea9f51`  |
| 2250   | Layout 1             | `f0e347ea9f51`  |
| 2243   | Layout 1             | `f0e347ea9f51`  |
| 2235   | Layout 1             | `f0e347ea9f51`  |
| 2229   | Layout 1             | `f0e347ea9f51`  |
| 2224   | Layout 1             | `f0e347ea9f51`  |
| 2218   | Layout 1             | `f0e347ea9f51`  |
| 2215   | Layout 1             | `f0e347ea9f51`  |
| 2207   | Layout 1             | `f0e347ea9f51`  |
| 2203   | Layout 1             | `f0e347ea9f51`  |
| 2196   | Layout 1             | `f0e347ea9f51`  |
| 2192   | Layout 1             | `f0e347ea9f51`  |
| 2189   | Layout 1             | `f0e347ea9f51`  |
| 2183   | Layout 1             | `f0e347ea9f51`  |
| 2179   | Layout 1             | `f0e347ea9f51`  |
| 2171   | Layout 1             | `f0e347ea9f51`  |
| 2163   | Layout 1             | `f0e347ea9f51`  |
| 2156   | Layout 1             | `f0e347ea9f51`  |
| 2151   | Layout 1             | `f0e347ea9f51`  |
| 2147   | Layout 1             | `f0e347ea9f51`  |
| 2142   | Layout 1             | `f0e347ea9f51`  |
| 2138   | Layout 1             | `f0e347ea9f51`  |
| 2134   | Layout 1             | `f0e347ea9f51`  |
| 2130   | Layout 1             | `f0e347ea9f51`  |
| 2122   | Layout 1             | `f0e347ea9f51`  |
| 2107   | Layout 1             | `f0e347ea9f51`  |
| 2098   | Layout 1             | `f0e347ea9f51`  |
| 2089   | Layout 1             | `f0e347ea9f51`  |
| 2081   | Layout 1             | `f0e347ea9f51`  |
| 2073   | Layout 1             | `f0e347ea9f51`  |
| 2067   | Layout 1             | `f0e347ea9f51`  |
| 2063   | Layout 1             | `f0e347ea9f51`  |
| 2059   | Layout 1             | `f0e347ea9f51`  |
| 2052   | Layout 1             | `f0e347ea9f51`  |
| 2044   | Layout 1             | `f0e347ea9f51`  |
| 2039   | Layout 1             | `f0e347ea9f51`  |
| 2032   | Layout 1             | `f0e347ea9f51`  |
| 2025   | Layout 1             | `f0e347ea9f51`  |
| 2011   | Layout 1             | `f0e347ea9f51`  |
| 2005   | Layout 1             | `f0e347ea9f51`  |
| 2000   | Layout 1             | `f0e347ea9f51`  |
| 1996   | Layout 1             | `f0e347ea9f51`  |
| 1991   | Layout 1             | `f0e347ea9f51`  |
| 1985   | Layout 1             | `f0e347ea9f51`  |
| 1980   | Layout 1             | `f0e347ea9f51`  |
| 1969   | Layout 1             | `f0e347ea9f51`  |
| 1964   | Layout 1             | `f0e347ea9f51`  |
| 1958   | Layout 1             | `f0e347ea9f51`  |
| 1950   | Layout 1             | `f0e347ea9f51`  |
| 1945   | Layout 1             | `f0e347ea9f51`  |
| 1937   | Layout 1             | `f0e347ea9f51`  |
| 1933   | Layout 1             | `f0e347ea9f51`  |
| 1927   | Layout 1             | `f0e347ea9f51`  |
| 1921   | Layout 1             | `f0e347ea9f51`  |
| 1914   | Layout 1             | `f0e347ea9f51`  |
| 1908   | Layout 1             | `f0e347ea9f51`  |
| 1897   | Layout 1             | `f0e347ea9f51`  |
| 1892   | Layout 1             | `f0e347ea9f51`  |
| 1886   | Layout 1             | `f0e347ea9f51`  |
| 1881   | Layout 1             | `f0e347ea9f51`  |
| 1871   | Layout 1             | `f0e347ea9f51`  |
| 1866   | Layout 1             | `f0e347ea9f51`  |
| 1862   | Layout 1             | `f0e347ea9f51`  |
| 1854   | Layout 1             | `f0e347ea9f51`  |
| 1846   | Layout 1             | `f0e347ea9f51`  |
| 1838   | Layout 1             | `f0e347ea9f51`  |
| 1832   | Layout 1             | `f0e347ea9f51`  |
| 1826   | Layout 1             | `f0e347ea9f51`  |
| 1822   | Layout 1             | `f0e347ea9f51`  |
| 1818   | Layout 1             | `f0e347ea9f51`  |
| 1804   | Layout 1             | `f0e347ea9f51`  |
| 1794   | Layout 1             | `f0e347ea9f51`  |
| 1790   | Layout 1             | `f0e347ea9f51`  |
| 1784   | Layout 1             | `f0e347ea9f51`  |
| 1774   | Layout 1             | `f0e347ea9f51`  |
| 1771   | Layout 1             | `f0e347ea9f51`  |
| 1762   | Layout 1             | `f0e347ea9f51`  |
| 1759   | Layout 1             | `f0e347ea9f51`  |
| 1754   | Layout 1             | `f0e347ea9f51`  |
| 1749   | Layout 1             | `f0e347ea9f51`  |
| 1743   | Layout 1             | `f0e347ea9f51`  |
| 1737   | Layout 1             | `f0e347ea9f51`  |
| 1731   | Layout 1             | `f0e347ea9f51`  |
| 1725   | Layout 1             | `f0e347ea9f51`  |
| 1717   | Layout 1             | `f0e347ea9f51`  |
| 1710   | Layout 1             | `f0e347ea9f51`  |
| 1704   | Layout 1             | `f0e347ea9f51`  |
| 1698   | Layout 1             | `f0e347ea9f51`  |
| 1690   | Layout 1             | `f0e347ea9f51`  |
| 1685   | Layout 1             | `f0e347ea9f51`  |
| 1680   | Layout 1             | `f0e347ea9f51`  |
| 1674   | Layout 1             | `f0e347ea9f51`  |
| 1668   | Layout 1             | `f0e347ea9f51`  |
| 1659   | Layout 1             | `f0e347ea9f51`  |
| 1649   | Layout 1             | `f0e347ea9f51`  |
| 1642   | Layout 1             | `f0e347ea9f51`  |
| 1636   | Layout 1             | `f0e347ea9f51`  |
| 1628   | Layout 1             | `f0e347ea9f51`  |
| 1622   | Layout 1             | `f0e347ea9f51`  |
| 1614   | Layout 1             | `f0e347ea9f51`  |
| 1608   | Layout 1             | `f0e347ea9f51`  |
| 1602   | Layout 1             | `f0e347ea9f51`  |
| 1598   | Layout 1             | `f0e347ea9f51`  |
| 1594   | Layout 1             | `f0e347ea9f51`  |
| 1590   | Layout 1             | `f0e347ea9f51`  |
| 1587   | Layout 1             | `f0e347ea9f51`  |
| 1584   | Layout 1             | `f0e347ea9f51`  |
| 1579   | Layout 1             | `f0e347ea9f51`  |
| 1572   | Layout 1             | `f0e347ea9f51`  |
| 1565   | Layout 1             | `f0e347ea9f51`  |
| 1559   | Layout 1             | `f0e347ea9f51`  |
| 1554   | Layout 1             | `f0e347ea9f51`  |
| 1547   | Layout 1             | `f0e347ea9f51`  |
| 1537   | Layout 1             | `f0e347ea9f51`  |
| 1529   | Layout 1             | `f0e347ea9f51`  |
| 1524   | Layout 1             | `f0e347ea9f51`  |
| 1519   | Layout 1             | `f0e347ea9f51`  |
| 1509   | Layout 1             | `f0e347ea9f51`  |
| 1506   | Layout 1             | `f0e347ea9f51`  |
| 1504   | Layout 1             | `f0e347ea9f51`  |
| 1500   | Layout 1             | `f0e347ea9f51`  |
| 1493   | Layout 1             | `f0e347ea9f51`  |
| 1489   | Layout 1             | `f0e347ea9f51`  |
| 1485   | Layout 1             | `f0e347ea9f51`  |
| 1481   | Layout 1             | `f0e347ea9f51`  |
| 1474   | Layout 1             | `f0e347ea9f51`  |
| 1466   | Layout 1             | `f0e347ea9f51`  |
| 1462   | Layout 1             | `f0e347ea9f51`  |
| 1459   | Layout 1             | `f0e347ea9f51`  |
| 1453   | Layout 1             | `f0e347ea9f51`  |
| 1450   | Layout 1             | `f0e347ea9f51`  |
| 1445   | Layout 1             | `f0e347ea9f51`  |
| 1439   | Layout 1             | `f0e347ea9f51`  |
| 1433   | Layout 1             | `f0e347ea9f51`  |
| 1430   | Layout 1             | `f0e347ea9f51`  |
| 1426   | Layout 1             | `f0e347ea9f51`  |
| 1421   | Layout 1             | `f0e347ea9f51`  |
| 1417   | Layout 1             | `f0e347ea9f51`  |
| 1416   | Layout 1             | `f0e347ea9f51`  |
| 1409   | Layout 1             | `f0e347ea9f51`  |
| 1405   | Layout 1             | `f0e347ea9f51`  |
| 1401   | Layout 1             | `f0e347ea9f51`  |
| 1396   | Layout 1             | `f0e347ea9f51`  |
| 1391   | Layout 1             | `f0e347ea9f51`  |
| 1390   | Layout 1             | `f0e347ea9f51`  |
| 1386   | Layout 1             | `f0e347ea9f51`  |
| 1381   | Layout 1             | `f0e347ea9f51`  |
| 1379   | Layout 1             | `f0e347ea9f51`  |
| 1372   | Layout 1             | `f0e347ea9f51`  |
| 1366   | Layout 1             | `f0e347ea9f51`  |
| 1364   | Layout 1             | `f0e347ea9f51`  |
| 1363   | Layout 1             | `f0e347ea9f51`  |
| 1360   | Layout 1             | `f0e347ea9f51`  |
| 1358   | Layout 1             | `f0e347ea9f51`  |
| 1355   | Layout 1             | `f0e347ea9f51`  |
| 1351   | Layout 1             | `f0e347ea9f51`  |
| 1348   | Layout 1             | `f0e347ea9f51`  |
| 1346   | Layout 1             | `f0e347ea9f51`  |
| 1341   | No documented layout | `f0e347ea9f51`  |
| 1340   | No documented layout | `f0e347ea9f51`  |
| 1338   | No documented layout | `f0e347ea9f51`  |
| 1335   | No documented layout | `f0e347ea9f51`  |
| 1333   | No documented layout | `f0e347ea9f51`  |
| 1329   | No documented layout | `f0e347ea9f51`  |
| 1327   | No documented layout | `f0e347ea9f51`  |
| 1324   | No documented layout | `f0e347ea9f51`  |
| 1321   | No documented layout | `f0e347ea9f51`  |
| 1319   | No documented layout | `f0e347ea9f51`  |
| 1318   | No documented layout | `f0e347ea9f51`  |
| 1316   | No documented layout | `f0e347ea9f51`  |
| 1313   | No documented layout | `f0e347ea9f51`  |
| 1311   | No documented layout | `f0e347ea9f51`  |
| 1309   | No documented layout | `f0e347ea9f51`  |
| 1304   | No documented layout | `f0e347ea9f51`  |
| 1292   | No documented layout | `f0e347ea9f51`  |
| 1286   | No documented layout | `f0e347ea9f51`  |
| 1280   | No documented layout | `f0e347ea9f51`  |
| 1276   | No documented layout | `f0e347ea9f51`  |
| 1267   | No documented layout | `f0e347ea9f51`  |
| 1261   | No documented layout | `f0e347ea9f51`  |
| 1256   | No documented layout | `f0e347ea9f51`  |
| 1250   | No file              | `f0e347ea9f51`  |
| 1246   | No file              | `f0e347ea9f51`  |
| 1239   | No file              | `f0e347ea9f51`  |
| 1230   | No file              | `f0e347ea9f51`  |
| 1226   | No file              | `f0e347ea9f51`  |
| 1220   | No file              | `f0e347ea9f51`  |
| 1217   | No file              | `f0e347ea9f51`  |
| 1211   | No file              | `f0e347ea9f51`  |
| 1210   | No file              | `f0e347ea9f51`  |
| 1208   | No file              | `f0e347ea9f51`  |
| 1203   | No file              | `f0e347ea9f51`  |
| 1197   | No file              | `f0e347ea9f51`  |
| 1194   | No file              | `f0e347ea9f51`  |
| 1192   | No file              | `f0e347ea9f51`  |
| 1187   | No file              | `f0e347ea9f51`  |
| 1183   | No file              | `f0e347ea9f51`  |
| 1177   | No file              | `f0e347ea9f51`  |
| 1173   | No file              | `f0e347ea9f51`  |
| 1167   | No file              | `f0e347ea9f51`  |
| 1164   | No file              | `f0e347ea9f51`  |
| 1156   | No file              | `f0e347ea9f51`  |
| 1149   | No file              | `f0e347ea9f51`  |
| 1144   | No file              | `f0e347ea9f51`  |
| 1137   | No file              | `f0e347ea9f51`  |
| 1132   | No file              | `f0e347ea9f51`  |
| 1127   | No file              | `f0e347ea9f51`  |
| 1122   | No file              | `f0e347ea9f51`  |
| 1118   | No file              | `f0e347ea9f51`  |
| 1114   | No file              | `f0e347ea9f51`  |
| 1109   | No file              | `f0e347ea9f51`  |
| 1102   | No file              | `f0e347ea9f51`  |
| 1096   | No file              | `f0e347ea9f51`  |
| 1088   | No file              | `f0e347ea9f51`  |
| 1081   | No file              | `f0e347ea9f51`  |
| 1076   | No file              | `f0e347ea9f51`  |
| 1069   | No file              | `f0e347ea9f51`  |
| 1064   | No file              | `f0e347ea9f51`  |
| 1058   | No file              | `f0e347ea9f51`  |
| 1051   | No file              | `f0e347ea9f51`  |
| 1044   | No file              | `f0e347ea9f51`  |
| 1036   | No file              | `f0e347ea9f51`  |
| 1026   | No file              | `f0e347ea9f51`  |
| 1016   | No file              | `f0e347ea9f51`  |
| 1009   | No file              | `f0e347ea9f51`  |
| 1005   | No file              | `f0e347ea9f51`  |
| 1000   | No file              | `f0e347ea9f51`  |
| 998    | No file              | `f0e347ea9f51`  |
| 990    | No file              | `f0e347ea9f51`  |
| 979    | No file              | `f0e347ea9f51`  |
| 972    | No file              | `f0e347ea9f51`  |
| 963    | No file              | `f0e347ea9f51`  |
| 955    | No file              | `f0e347ea9f51`  |
| 946    | No file              | `f0e347ea9f51`  |
| 938    | No file              | `f0e347ea9f51`  |
| 927    | No file              | `f0e347ea9f51`  |
| 911    | No file              | `f0e347ea9f51`  |
| 904    | No file              | `f0e347ea9f51`  |
| 899    | No file              | `f0e347ea9f51`  |
| 894    | No file              | `f0e347ea9f51`  |
| 885    | No file              | `f0e347ea9f51`  |
| 879    | No file              | `f0e347ea9f51`  |
| 872    | No file              | `f0e347ea9f51`  |
| 864    | No file              | `f0e347ea9f51`  |
| 855    | No file              | `f0e347ea9f51`  |
| 853    | No file              | `f0e347ea9f51`  |
| 845    | No file              | `f0e347ea9f51`  |
| 837    | No file              | `f0e347ea9f51`  |
| 829    | No file              | `f0e347ea9f51`  |
| 822    | No file              | `f0e347ea9f51`  |
| 814    | No file              | `f0e347ea9f51`  |
| 805    | No file              | `f0e347ea9f51`  |
| 794    | No file              | `f0e347ea9f51`  |
| 787    | No file              | `f0e347ea9f51`  |
| 780    | No file              | `f0e347ea9f51`  |
| 771    | No file              | `f0e347ea9f51`  |
| 760    | No file              | `f0e347ea9f51`  |
| 748    | No file              | `f0e347ea9f51`  |
| 741    | No file              | `f0e347ea9f51`  |
| 736    | No file              | `f0e347ea9f51`  |
| 731    | No file              | `f0e347ea9f51`  |
| 723    | No file              | `f0e347ea9f51`  |
| 711    | No file              | `f0e347ea9f51`  |
| 707    | No file              | `f0e347ea9f51`  |
| 697    | No file              | `f0e347ea9f51`  |
| 689    | No file              | `f0e347ea9f51`  |
| 683    | No file              | `f0e347ea9f51`  |
| 678    | No file              | `f0e347ea9f51`  |
| 670    | No file              | `f0e347ea9f51`  |
| 661    | No file              | `f0e347ea9f51`  |
| 656    | No file              | `f0e347ea9f51`  |
| 652    | No file              | `f0e347ea9f51`  |
| 643    | No file              | `f0e347ea9f51`  |
| 637    | No file              | `f0e347ea9f51`  |
| 630    | No file              | `f0e347ea9f51`  |
| 627    | No file              | `f0e347ea9f51`  |
| 621    | No file              | `f0e347ea9f51`  |
| 617    | No file              | `f0e347ea9f51`  |
| 615    | No file              | `f0e347ea9f51`  |
| 606    | No file              | `f0e347ea9f51`  |
| 599    | No file              | `f0e347ea9f51`  |
| 592    | No file              | `f0e347ea9f51`  |
| 586    | No file              | `f0e347ea9f51`  |
| 577    | No file              | `f0e347ea9f51`  |
| 569    | No file              | `f0e347ea9f51`  |
| 561    | No file              | `f0e347ea9f51`  |
| 554    | No file              | `f0e347ea9f51`  |
| 542    | No file              | `f0e347ea9f51`  |
| 532    | No file              | `f0e347ea9f51`  |
| 531    | No file              | `f0e347ea9f51`  |
| 526    | No file              | `f0e347ea9f51`  |
| 521    | No file              | `f0e347ea9f51`  |
| 517    | No file              | `f0e347ea9f51`  |
| 510    | No file              | `f0e347ea9f51`  |
| 508    | No file              | `f0e347ea9f51`  |
| 504    | No file              | `f0e347ea9f51`  |
| 497    | No file              | `f0e347ea9f51`  |
| 491    | No file              | `f0e347ea9f51`  |
| 485    | No file              | `f0e347ea9f51`  |
| 478    | No file              | `f0e347ea9f51`  |
| 472    | No file              | `f0e347ea9f51`  |
| 466    | No file              | `f0e347ea9f51`  |
| 457    | No file              | `f0e347ea9f51`  |
| 452    | No file              | `f0e347ea9f51`  |
| 449    | No file              | `f0e347ea9f51`  |
| 435    | No file              | `f0e347ea9f51`  |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                                                    |
| ---------------------------------- | -------- | --------------------------------------------------------------------------------------- |
| `interiorrelationpointoffset.dbss` | Optional | `character_key -> data_offset` of every row; the parser walks the main file without it   |
| `characterstaticoffset.dbss`       | Optional | The `characterstatic.dbss` keys, so a key without a row shows as plain text              |
| `languagedata_en.loc`              | Optional | Furniture names, LOC type 6                                                              |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of fixed rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset      | Type       | Field        | Notes                                    |
| ----------- | ---------- | ------------ | ---------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                   |
| `+0x04`     | u32        | count        | Number of rows; 1,140 on client 3482     |
| `+0x08`     | Row[count] | rows         | See Row                                  |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table         |
| `rows+0x04` | u32        | table_start  | End of the rows (`8 + 66 * count`)       |
| `rows+0x08` | u32        | zero         | Always `0`                               |

### Row (66 bytes)

Values on client 3482; a point is `0`, `1`, `2`, `3` or `5`.

| Offset  | Type | Field                    | Notes                                                                    |
| ------- | ---- | ------------------------ | ------------------------------------------------------------------------ |
| `+0x00` | u16  | character_key            | Row key: the furniture installation, a `characterstatic.dbss` character  |
| `+0x02` | u16  | character_key_dup        | Equal to `character_key` on every row; the offset index points here      |
| `+0x04` | u16  | matching_character_key   | The matching chair, a `characterstatic.dbss` key; `0` on 1,016 rows      |
| `+0x06` | i32  | matching_character_point | `0` on every row (clients 1784 and 3482)                                 |
| `+0x0A` | i32  | on_dresser               | Non-zero on 262 rows                                                      |
| `+0x0E` | i32  | on_bed_side_cabinet      | Equal to `on_dresser` on every row                                       |
| `+0x12` | i32  | on_wardrobe              | `0` on every row                                                          |
| `+0x16` | i32  | on_dining_table          | Non-zero on 261 rows                                                      |
| `+0x1A` | i32  | on_table                 | Non-zero on 262 rows                                                      |
| `+0x1E` | i32  | on_chair                 | `0` on every row                                                          |
| `+0x22` | i32  | on_sofa                  | `0` on every row                                                          |
| `+0x26` | i32  | on_bed                   | `0` on every row                                                          |
| `+0x2A` | i32  | on_book_case             | `3` on 17 rows, else `0`                                                 |
| `+0x2E` | i32  | on_shelf                 | Non-zero on 261 rows                                                      |
| `+0x32` | i32  | is_empty_in_front        | Non-zero on 531 rows                                                      |
| `+0x36` | i32  | is_empty_in_back         | `2` on 61 rows, else `0`                                                 |
| `+0x3A` | i32  | is_empty_in_left         | Equal to `is_empty_in_back` on every row                                 |
| `+0x3E` | i32  | is_empty_in_right        | Equal to `is_empty_in_back` on every row                                 |

The rows are in no key order; client 3482 opens with 16111, 16110, 16109.

### `interiorrelationpointoffset.dbss`

The `PABR` index layout of `characterstaticoffset.dbss`, read by
`parse_pabr_offset_rows()` in `_common/pabr_offset.py`.

| Offset      | Type              | Field        | Notes                                         |
| ----------- | ----------------- | ------------ | --------------------------------------------- |
| `+0x00`     | char[4]           | magic        | `PABR`                                        |
| `+0x04`     | u32               | count        | Equals the `interiorrelationpoint.dbss` count |
| `+0x08`     | Offset Row[count] | rows         | See Offset Row                                |
| `rows+0x00` | u32               | string_count | `0`: the empty PABR string table              |
| `rows+0x04` | u32               | table_start  | End of the rows (`8 + 10 * count`)            |
| `rows+0x08` | u32               | zero         | Always `0`                                    |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                     |
| ------- | ---- | ------------- | ----------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at               |
| `+0x02` | u32  | data_offset   | Row start + 2, at `character_key_dup`     |
| `+0x06` | u32  | data_size     | `0` on every row                          |

The index rows are in another order than the file; on clients 1784 and
3482 every index row points at the row with its key.

## Field Names

The `InteriorRelationPoint_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has 17 columns: `CharacterKey`, the ten
`On*` columns (`OnDresser` to `OnShelf`), the four `IsEmptyIn*` columns,
`MatchingCharacterKey` and `MatchingCharacterPoint`. The 2016
`gc::InteriorRelationPointStaticStatus` holds `_installationCharacterKey`,
`_relationPoint` (13 i32 then, 14 now) and `_matchingCharacterKey` and
`_matchingCharacterPoint` as a pair.

All 966 keys of the sheet have a row on client 1784. The ten relation
columns with non-zero values match a field on 966 of 966 keys each, in
sheet order: `OnDresser` and `OnBedSideCabinet` (equal columns, `+0x0A`
and `+0x0E`), `OnDiningTable`, `OnTable`, `OnBookCase`, `OnShelf`,
`IsEmptyInFront`, and the equal `IsEmptyInBack`, `IsEmptyInLeft` and
`IsEmptyInRight` (`+0x36` to `+0x3E`). The four columns that are `0` on
every sheet row (`OnWardrobe`, `OnChair`, `OnSofa`, `OnBed`) take the four
all-zero fields between them in the same order. `MatchingCharacterKey`
matches `matching_character_key` on 966 of 966 keys (`<null>` as `0`), and
`MatchingCharacterPoint` (`0` on every sheet row) is the one field left,
next to the key as in the 2016 struct.

## Notes

- 124 of the 1,140 rows name a matching character on client 3482: tables
  and dining tables name the chair of their set. All 45 chairs named that
  way have a row of their own.
- No Lua file of client 3482 reads this table. The house window shows the
  interior points of the visited house through
  `toClient_GetVisitingTotalInteriorPoint()`, `...BaseInteriorPoint()`,
  `...SetOptionInteriorPoint()` and `...BonusInteriorPoint()`
  (`panel_window_installationmode_housepoint_renew.luac`).

## Open Questions

### How the Relation Points Count

The points read as a bonus for placing the furniture on another piece or
with a free side, but what the game adds them to (the interior points of
the house window, or a placement check) and what the values `1` to `5`
weigh is open.
