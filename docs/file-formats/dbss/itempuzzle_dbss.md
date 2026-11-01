# `itempuzzle.dbss` Format

## Purpose

The inventory puzzles: items that combine into another item when they lie
in the inventory in a given shape, such as three Ancient Pottery Fragments
in a row. Each row holds one puzzle as a 5 x 5 grid of item keys, row by
row, and the first piece and the grid bounds the client works out from it.
The item a puzzle makes is a server-only column and `0` in the client
file. Companion `itempuzzleoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                    | Bytes  | Records        | Row bytes |
| ------ | -------------- | ----------------------- | ------ | -------------- | --------- |
| 1      | 1280 and later | `itempuzzle.dbss`       | 46,324 | 386 Row        | 120       |
| 1      | 1280 and later | `itempuzzleoffset.dbss` | 3,864  | 386 Offset Row | 10        |

| Layout | File                    | Known             | Unknown    |
| ------ | ----------------------- | ----------------- | ---------- |
| 1      | `itempuzzle.dbss`       | 46,324 B (100.0%) | 0 B (0.0%) |
| 1      | `itempuzzleoffset.dbss` | 3,864 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c5a247e8a93f`  |
| 3482   | Layout 1 | `c5a247e8a93f`  |
| 3474   | Layout 1 | `c5a247e8a93f`  |
| 3473   | Layout 1 | `c5a247e8a93f`  |
| 3464   | Layout 1 | `c5a247e8a93f`  |
| 3458   | Layout 1 | `c5a247e8a93f`  |
| 3454   | Layout 1 | `c5a247e8a93f`  |
| 3444   | Layout 1 | `c5a247e8a93f`  |
| 3435   | Layout 1 | `c5a247e8a93f`  |
| 3426   | Layout 1 | `c5a247e8a93f`  |
| 3418   | Layout 1 | `c5a247e8a93f`  |
| 3412   | Layout 1 | `c5a247e8a93f`  |
| 3402   | Layout 1 | `c5a247e8a93f`  |
| 3396   | Layout 1 | `c5a247e8a93f`  |
| 3387   | Layout 1 | `c5a247e8a93f`  |
| 3381   | Layout 1 | `c5a247e8a93f`  |
| 3373   | Layout 1 | `c5a247e8a93f`  |
| 3364   | Layout 1 | `c5a247e8a93f`  |
| 3356   | Layout 1 | `c5a247e8a93f`  |
| 3349   | Layout 1 | `c5a247e8a93f`  |
| 3342   | Layout 1 | `c5a247e8a93f`  |
| 3335   | Layout 1 | `c5a247e8a93f`  |
| 3326   | Layout 1 | `c5a247e8a93f`  |
| 3321   | Layout 1 | `c5a247e8a93f`  |
| 3314   | Layout 1 | `c5a247e8a93f`  |
| 3303   | Layout 1 | `c5a247e8a93f`  |
| 3302   | Layout 1 | `c5a247e8a93f`  |
| 3293   | Layout 1 | `c5a247e8a93f`  |
| 3283   | Layout 1 | `c5a247e8a93f`  |
| 3275   | Layout 1 | `c5a247e8a93f`  |
| 3267   | Layout 1 | `c5a247e8a93f`  |
| 3258   | Layout 1 | `c5a247e8a93f`  |
| 3251   | Layout 1 | `c5a247e8a93f`  |
| 3242   | Layout 1 | `c5a247e8a93f`  |
| 3235   | Layout 1 | `c5a247e8a93f`  |
| 3229   | Layout 1 | `c5a247e8a93f`  |
| 3212   | Layout 1 | `c5a247e8a93f`  |
| 3203   | Layout 1 | `c5a247e8a93f`  |
| 3193   | Layout 1 | `c5a247e8a93f`  |
| 3186   | Layout 1 | `c5a247e8a93f`  |
| 3177   | Layout 1 | `c5a247e8a93f`  |
| 3169   | Layout 1 | `c5a247e8a93f`  |
| 3158   | Layout 1 | `c5a247e8a93f`  |
| 3151   | Layout 1 | `c5a247e8a93f`  |
| 3144   | Layout 1 | `c5a247e8a93f`  |
| 3133   | Layout 1 | `c5a247e8a93f`  |
| 3125   | Layout 1 | `c5a247e8a93f`  |
| 3118   | Layout 1 | `c5a247e8a93f`  |
| 3111   | Layout 1 | `c5a247e8a93f`  |
| 3103   | Layout 1 | `c5a247e8a93f`  |
| 3095   | Layout 1 | `c5a247e8a93f`  |
| 3086   | Layout 1 | `c5a247e8a93f`  |
| 3072   | Layout 1 | `c5a247e8a93f`  |
| 3062   | Layout 1 | `c5a247e8a93f`  |
| 3052   | Layout 1 | `c5a247e8a93f`  |
| 3045   | Layout 1 | `c5a247e8a93f`  |
| 3037   | Layout 1 | `c5a247e8a93f`  |
| 3030   | Layout 1 | `c5a247e8a93f`  |
| 3021   | Layout 1 | `c5a247e8a93f`  |
| 3012   | Layout 1 | `c5a247e8a93f`  |
| 3002   | Layout 1 | `c5a247e8a93f`  |
| 2995   | Layout 1 | `c5a247e8a93f`  |
| 2987   | Layout 1 | `c5a247e8a93f`  |
| 2978   | Layout 1 | `c5a247e8a93f`  |
| 2970   | Layout 1 | `c5a247e8a93f`  |
| 2959   | Layout 1 | `c5a247e8a93f`  |
| 2951   | Layout 1 | `c5a247e8a93f`  |
| 2942   | Layout 1 | `c5a247e8a93f`  |
| 2935   | Layout 1 | `c5a247e8a93f`  |
| 2932   | Layout 1 | `c5a247e8a93f`  |
| 2923   | Layout 1 | `c5a247e8a93f`  |
| 2919   | Layout 1 | `c5a247e8a93f`  |
| 2907   | Layout 1 | `c5a247e8a93f`  |
| 2900   | Layout 1 | `c5a247e8a93f`  |
| 2891   | Layout 1 | `c5a247e8a93f`  |
| 2882   | Layout 1 | `c5a247e8a93f`  |
| 2872   | Layout 1 | `c5a247e8a93f`  |
| 2863   | Layout 1 | `c5a247e8a93f`  |
| 2855   | Layout 1 | `c5a247e8a93f`  |
| 2849   | Layout 1 | `c5a247e8a93f`  |
| 2844   | Layout 1 | `c5a247e8a93f`  |
| 2834   | Layout 1 | `c5a247e8a93f`  |
| 2825   | Layout 1 | `c5a247e8a93f`  |
| 2819   | Layout 1 | `c5a247e8a93f`  |
| 2811   | Layout 1 | `c5a247e8a93f`  |
| 2803   | Layout 1 | `c5a247e8a93f`  |
| 2794   | Layout 1 | `c5a247e8a93f`  |
| 2783   | Layout 1 | `c5a247e8a93f`  |
| 2774   | Layout 1 | `c5a247e8a93f`  |
| 2765   | Layout 1 | `c5a247e8a93f`  |
| 2756   | Layout 1 | `c5a247e8a93f`  |
| 2750   | Layout 1 | `c5a247e8a93f`  |
| 2743   | Layout 1 | `c5a247e8a93f`  |
| 2736   | Layout 1 | `c5a247e8a93f`  |
| 2726   | Layout 1 | `c5a247e8a93f`  |
| 2717   | Layout 1 | `c5a247e8a93f`  |
| 2709   | Layout 1 | `c5a247e8a93f`  |
| 2703   | Layout 1 | `c5a247e8a93f`  |
| 2695   | Layout 1 | `c5a247e8a93f`  |
| 2684   | Layout 1 | `c5a247e8a93f`  |
| 2672   | Layout 1 | `c5a247e8a93f`  |
| 2665   | Layout 1 | `c5a247e8a93f`  |
| 2657   | Layout 1 | `c5a247e8a93f`  |
| 2649   | Layout 1 | `c5a247e8a93f`  |
| 2644   | Layout 1 | `c5a247e8a93f`  |
| 2637   | Layout 1 | `c5a247e8a93f`  |
| 2629   | Layout 1 | `c5a247e8a93f`  |
| 2619   | Layout 1 | `c5a247e8a93f`  |
| 2612   | Layout 1 | `c5a247e8a93f`  |
| 2606   | Layout 1 | `c5a247e8a93f`  |
| 2602   | Layout 1 | `c5a247e8a93f`  |
| 2601   | Layout 1 | `c5a247e8a93f`  |
| 2592   | Layout 1 | `c5a247e8a93f`  |
| 2583   | Layout 1 | `c5a247e8a93f`  |
| 2575   | Layout 1 | `c5a247e8a93f`  |
| 2567   | Layout 1 | `c5a247e8a93f`  |
| 2560   | Layout 1 | `c5a247e8a93f`  |
| 2553   | Layout 1 | `c5a247e8a93f`  |
| 2545   | Layout 1 | `c5a247e8a93f`  |
| 2538   | Layout 1 | `c5a247e8a93f`  |
| 2529   | Layout 1 | `c5a247e8a93f`  |
| 2519   | Layout 1 | `c5a247e8a93f`  |
| 2513   | Layout 1 | `c5a247e8a93f`  |
| 2510   | Layout 1 | `c5a247e8a93f`  |
| 2507   | Layout 1 | `c5a247e8a93f`  |
| 2503   | Layout 1 | `c5a247e8a93f`  |
| 2498   | Layout 1 | `c5a247e8a93f`  |
| 2492   | Layout 1 | `c5a247e8a93f`  |
| 2487   | Layout 1 | `c5a247e8a93f`  |
| 2480   | Layout 1 | `c5a247e8a93f`  |
| 2474   | Layout 1 | `c5a247e8a93f`  |
| 2468   | Layout 1 | `c5a247e8a93f`  |
| 2460   | Layout 1 | `c5a247e8a93f`  |
| 2453   | Layout 1 | `c5a247e8a93f`  |
| 2444   | Layout 1 | `c5a247e8a93f`  |
| 2438   | Layout 1 | `c5a247e8a93f`  |
| 2434   | Layout 1 | `c5a247e8a93f`  |
| 2429   | Layout 1 | `c5a247e8a93f`  |
| 2421   | Layout 1 | `c5a247e8a93f`  |
| 2414   | Layout 1 | `c5a247e8a93f`  |
| 2407   | Layout 1 | `c5a247e8a93f`  |
| 2401   | Layout 1 | `c5a247e8a93f`  |
| 2397   | Layout 1 | `c5a247e8a93f`  |
| 2393   | Layout 1 | `c5a247e8a93f`  |
| 2384   | Layout 1 | `c5a247e8a93f`  |
| 2378   | Layout 1 | `c5a247e8a93f`  |
| 2372   | Layout 1 | `c5a247e8a93f`  |
| 2358   | Layout 1 | `c5a247e8a93f`  |
| 2352   | Layout 1 | `c5a247e8a93f`  |
| 2347   | Layout 1 | `c5a247e8a93f`  |
| 2343   | Layout 1 | `c5a247e8a93f`  |
| 2335   | Layout 1 | `c5a247e8a93f`  |
| 2327   | Layout 1 | `c5a247e8a93f`  |
| 2324   | Layout 1 | `c5a247e8a93f`  |
| 2319   | Layout 1 | `c5a247e8a93f`  |
| 2313   | Layout 1 | `c5a247e8a93f`  |
| 2308   | Layout 1 | `c5a247e8a93f`  |
| 2302   | Layout 1 | `c5a247e8a93f`  |
| 2295   | Layout 1 | `c5a247e8a93f`  |
| 2290   | Layout 1 | `c5a247e8a93f`  |
| 2284   | Layout 1 | `c5a247e8a93f`  |
| 2276   | Layout 1 | `c5a247e8a93f`  |
| 2269   | Layout 1 | `c5a247e8a93f`  |
| 2259   | Layout 1 | `c5a247e8a93f`  |
| 2250   | Layout 1 | `c5a247e8a93f`  |
| 2243   | Layout 1 | `c5a247e8a93f`  |
| 2235   | Layout 1 | `c5a247e8a93f`  |
| 2229   | Layout 1 | `c5a247e8a93f`  |
| 2224   | Layout 1 | `c5a247e8a93f`  |
| 2218   | Layout 1 | `c5a247e8a93f`  |
| 2215   | Layout 1 | `c5a247e8a93f`  |
| 2207   | Layout 1 | `c5a247e8a93f`  |
| 2203   | Layout 1 | `c5a247e8a93f`  |
| 2196   | Layout 1 | `c5a247e8a93f`  |
| 2192   | Layout 1 | `c5a247e8a93f`  |
| 2189   | Layout 1 | `c5a247e8a93f`  |
| 2183   | Layout 1 | `c5a247e8a93f`  |
| 2179   | Layout 1 | `c5a247e8a93f`  |
| 2171   | Layout 1 | `c5a247e8a93f`  |
| 2163   | Layout 1 | `c5a247e8a93f`  |
| 2156   | Layout 1 | `c5a247e8a93f`  |
| 2151   | Layout 1 | `c5a247e8a93f`  |
| 2147   | Layout 1 | `c5a247e8a93f`  |
| 2142   | Layout 1 | `c5a247e8a93f`  |
| 2138   | Layout 1 | `c5a247e8a93f`  |
| 2134   | Layout 1 | `c5a247e8a93f`  |
| 2130   | Layout 1 | `c5a247e8a93f`  |
| 2122   | Layout 1 | `c5a247e8a93f`  |
| 2107   | Layout 1 | `c5a247e8a93f`  |
| 2098   | Layout 1 | `c5a247e8a93f`  |
| 2089   | Layout 1 | `c5a247e8a93f`  |
| 2081   | Layout 1 | `c5a247e8a93f`  |
| 2073   | Layout 1 | `c5a247e8a93f`  |
| 2067   | Layout 1 | `c5a247e8a93f`  |
| 2063   | Layout 1 | `c5a247e8a93f`  |
| 2059   | Layout 1 | `c5a247e8a93f`  |
| 2052   | Layout 1 | `c5a247e8a93f`  |
| 2044   | Layout 1 | `c5a247e8a93f`  |
| 2039   | Layout 1 | `c5a247e8a93f`  |
| 2032   | Layout 1 | `c5a247e8a93f`  |
| 2025   | Layout 1 | `c5a247e8a93f`  |
| 2011   | Layout 1 | `c5a247e8a93f`  |
| 2005   | Layout 1 | `c5a247e8a93f`  |
| 2000   | Layout 1 | `c5a247e8a93f`  |
| 1996   | Layout 1 | `c5a247e8a93f`  |
| 1991   | Layout 1 | `c5a247e8a93f`  |
| 1985   | Layout 1 | `c5a247e8a93f`  |
| 1980   | Layout 1 | `c5a247e8a93f`  |
| 1969   | Layout 1 | `c5a247e8a93f`  |
| 1964   | Layout 1 | `c5a247e8a93f`  |
| 1958   | Layout 1 | `c5a247e8a93f`  |
| 1950   | Layout 1 | `c5a247e8a93f`  |
| 1945   | Layout 1 | `c5a247e8a93f`  |
| 1937   | Layout 1 | `c5a247e8a93f`  |
| 1933   | Layout 1 | `c5a247e8a93f`  |
| 1927   | Layout 1 | `c5a247e8a93f`  |
| 1921   | Layout 1 | `c5a247e8a93f`  |
| 1914   | Layout 1 | `c5a247e8a93f`  |
| 1908   | Layout 1 | `c5a247e8a93f`  |
| 1897   | Layout 1 | `c5a247e8a93f`  |
| 1892   | Layout 1 | `c5a247e8a93f`  |
| 1886   | Layout 1 | `c5a247e8a93f`  |
| 1881   | Layout 1 | `c5a247e8a93f`  |
| 1871   | Layout 1 | `c5a247e8a93f`  |
| 1866   | Layout 1 | `c5a247e8a93f`  |
| 1862   | Layout 1 | `c5a247e8a93f`  |
| 1854   | Layout 1 | `c5a247e8a93f`  |
| 1846   | Layout 1 | `c5a247e8a93f`  |
| 1838   | Layout 1 | `c5a247e8a93f`  |
| 1832   | Layout 1 | `c5a247e8a93f`  |
| 1826   | Layout 1 | `c5a247e8a93f`  |
| 1822   | Layout 1 | `c5a247e8a93f`  |
| 1818   | Layout 1 | `c5a247e8a93f`  |
| 1804   | Layout 1 | `c5a247e8a93f`  |
| 1794   | Layout 1 | `c5a247e8a93f`  |
| 1790   | Layout 1 | `c5a247e8a93f`  |
| 1784   | Layout 1 | `c5a247e8a93f`  |
| 1774   | Layout 1 | `c5a247e8a93f`  |
| 1771   | Layout 1 | `c5a247e8a93f`  |
| 1762   | Layout 1 | `c5a247e8a93f`  |
| 1759   | Layout 1 | `c5a247e8a93f`  |
| 1754   | Layout 1 | `c5a247e8a93f`  |
| 1749   | Layout 1 | `c5a247e8a93f`  |
| 1743   | Layout 1 | `c5a247e8a93f`  |
| 1737   | Layout 1 | `c5a247e8a93f`  |
| 1731   | Layout 1 | `c5a247e8a93f`  |
| 1725   | Layout 1 | `c5a247e8a93f`  |
| 1717   | Layout 1 | `c5a247e8a93f`  |
| 1710   | Layout 1 | `c5a247e8a93f`  |
| 1704   | Layout 1 | `c5a247e8a93f`  |
| 1698   | Layout 1 | `c5a247e8a93f`  |
| 1690   | Layout 1 | `c5a247e8a93f`  |
| 1685   | Layout 1 | `c5a247e8a93f`  |
| 1680   | Layout 1 | `c5a247e8a93f`  |
| 1674   | Layout 1 | `c5a247e8a93f`  |
| 1668   | Layout 1 | `c5a247e8a93f`  |
| 1659   | Layout 1 | `c5a247e8a93f`  |
| 1649   | Layout 1 | `c5a247e8a93f`  |
| 1642   | Layout 1 | `c5a247e8a93f`  |
| 1636   | Layout 1 | `c5a247e8a93f`  |
| 1628   | Layout 1 | `c5a247e8a93f`  |
| 1622   | Layout 1 | `c5a247e8a93f`  |
| 1614   | Layout 1 | `c5a247e8a93f`  |
| 1608   | Layout 1 | `c5a247e8a93f`  |
| 1602   | Layout 1 | `c5a247e8a93f`  |
| 1598   | Layout 1 | `c5a247e8a93f`  |
| 1594   | Layout 1 | `c5a247e8a93f`  |
| 1590   | Layout 1 | `c5a247e8a93f`  |
| 1587   | Layout 1 | `c5a247e8a93f`  |
| 1584   | Layout 1 | `c5a247e8a93f`  |
| 1579   | Layout 1 | `c5a247e8a93f`  |
| 1572   | Layout 1 | `c5a247e8a93f`  |
| 1565   | Layout 1 | `c5a247e8a93f`  |
| 1559   | Layout 1 | `c5a247e8a93f`  |
| 1554   | Layout 1 | `c5a247e8a93f`  |
| 1547   | Layout 1 | `c5a247e8a93f`  |
| 1537   | Layout 1 | `c5a247e8a93f`  |
| 1529   | Layout 1 | `c5a247e8a93f`  |
| 1524   | Layout 1 | `c5a247e8a93f`  |
| 1519   | Layout 1 | `c5a247e8a93f`  |
| 1509   | Layout 1 | `c5a247e8a93f`  |
| 1506   | Layout 1 | `c5a247e8a93f`  |
| 1504   | Layout 1 | `c5a247e8a93f`  |
| 1500   | Layout 1 | `c5a247e8a93f`  |
| 1493   | Layout 1 | `c5a247e8a93f`  |
| 1489   | Layout 1 | `c5a247e8a93f`  |
| 1485   | Layout 1 | `c5a247e8a93f`  |
| 1481   | Layout 1 | `c5a247e8a93f`  |
| 1474   | Layout 1 | `c5a247e8a93f`  |
| 1466   | Layout 1 | `c5a247e8a93f`  |
| 1462   | Layout 1 | `c5a247e8a93f`  |
| 1459   | Layout 1 | `c5a247e8a93f`  |
| 1453   | Layout 1 | `c5a247e8a93f`  |
| 1450   | Layout 1 | `c5a247e8a93f`  |
| 1445   | Layout 1 | `c5a247e8a93f`  |
| 1439   | Layout 1 | `c5a247e8a93f`  |
| 1433   | Layout 1 | `c5a247e8a93f`  |
| 1430   | Layout 1 | `c5a247e8a93f`  |
| 1426   | Layout 1 | `c5a247e8a93f`  |
| 1421   | Layout 1 | `c5a247e8a93f`  |
| 1417   | Layout 1 | `c5a247e8a93f`  |
| 1416   | Layout 1 | `c5a247e8a93f`  |
| 1409   | Layout 1 | `c5a247e8a93f`  |
| 1405   | Layout 1 | `c5a247e8a93f`  |
| 1401   | Layout 1 | `c5a247e8a93f`  |
| 1396   | Layout 1 | `c5a247e8a93f`  |
| 1391   | Layout 1 | `c5a247e8a93f`  |
| 1390   | Layout 1 | `c5a247e8a93f`  |
| 1386   | Layout 1 | `c5a247e8a93f`  |
| 1381   | Layout 1 | `c5a247e8a93f`  |
| 1379   | Layout 1 | `c5a247e8a93f`  |
| 1372   | Layout 1 | `c5a247e8a93f`  |
| 1366   | Layout 1 | `c5a247e8a93f`  |
| 1364   | Layout 1 | `c5a247e8a93f`  |
| 1363   | Layout 1 | `c5a247e8a93f`  |
| 1360   | Layout 1 | `c5a247e8a93f`  |
| 1358   | Layout 1 | `c5a247e8a93f`  |
| 1355   | Layout 1 | `c5a247e8a93f`  |
| 1351   | Layout 1 | `c5a247e8a93f`  |
| 1348   | Layout 1 | `c5a247e8a93f`  |
| 1346   | Layout 1 | `c5a247e8a93f`  |
| 1341   | Layout 1 | `c5a247e8a93f`  |
| 1340   | Layout 1 | `c5a247e8a93f`  |
| 1338   | Layout 1 | `c5a247e8a93f`  |
| 1335   | Layout 1 | `c5a247e8a93f`  |
| 1333   | Layout 1 | `c5a247e8a93f`  |
| 1329   | Layout 1 | `c5a247e8a93f`  |
| 1327   | Layout 1 | `c5a247e8a93f`  |
| 1324   | Layout 1 | `c5a247e8a93f`  |
| 1321   | Layout 1 | `c5a247e8a93f`  |
| 1319   | Layout 1 | `c5a247e8a93f`  |
| 1318   | Layout 1 | `c5a247e8a93f`  |
| 1316   | Layout 1 | `c5a247e8a93f`  |
| 1313   | Layout 1 | `c5a247e8a93f`  |
| 1311   | Layout 1 | `c5a247e8a93f`  |
| 1309   | Layout 1 | `c5a247e8a93f`  |
| 1304   | Layout 1 | `c5a247e8a93f`  |
| 1292   | Layout 1 | `c5a247e8a93f`  |
| 1286   | Layout 1 | `c5a247e8a93f`  |
| 1280   | Layout 1 | `c5a247e8a93f`  |
| 1276   | No file  | `c5a247e8a93f`  |
| 1267   | No file  | `c5a247e8a93f`  |
| 1261   | No file  | `c5a247e8a93f`  |
| 1256   | No file  | `c5a247e8a93f`  |
| 1250   | No file  | `c5a247e8a93f`  |
| 1246   | No file  | `c5a247e8a93f`  |
| 1239   | No file  | `c5a247e8a93f`  |
| 1230   | No file  | `c5a247e8a93f`  |
| 1226   | No file  | `c5a247e8a93f`  |
| 1220   | No file  | `c5a247e8a93f`  |
| 1217   | No file  | `c5a247e8a93f`  |
| 1211   | No file  | `c5a247e8a93f`  |
| 1210   | No file  | `c5a247e8a93f`  |
| 1208   | No file  | `c5a247e8a93f`  |
| 1203   | No file  | `c5a247e8a93f`  |
| 1197   | No file  | `c5a247e8a93f`  |
| 1194   | No file  | `c5a247e8a93f`  |
| 1192   | No file  | `c5a247e8a93f`  |
| 1187   | No file  | `c5a247e8a93f`  |
| 1183   | No file  | `c5a247e8a93f`  |
| 1177   | No file  | `c5a247e8a93f`  |
| 1173   | No file  | `c5a247e8a93f`  |
| 1167   | No file  | `c5a247e8a93f`  |
| 1164   | No file  | `c5a247e8a93f`  |
| 1156   | No file  | `c5a247e8a93f`  |
| 1149   | No file  | `c5a247e8a93f`  |
| 1144   | No file  | `c5a247e8a93f`  |
| 1137   | No file  | `c5a247e8a93f`  |
| 1132   | No file  | `c5a247e8a93f`  |
| 1127   | No file  | `c5a247e8a93f`  |
| 1122   | No file  | `c5a247e8a93f`  |
| 1118   | No file  | `c5a247e8a93f`  |
| 1114   | No file  | `c5a247e8a93f`  |
| 1109   | No file  | `c5a247e8a93f`  |
| 1102   | No file  | `c5a247e8a93f`  |
| 1096   | No file  | `c5a247e8a93f`  |
| 1088   | No file  | `c5a247e8a93f`  |
| 1081   | No file  | `c5a247e8a93f`  |
| 1076   | No file  | `c5a247e8a93f`  |
| 1069   | No file  | `c5a247e8a93f`  |
| 1064   | No file  | `c5a247e8a93f`  |
| 1058   | No file  | `c5a247e8a93f`  |
| 1051   | No file  | `c5a247e8a93f`  |
| 1044   | No file  | `c5a247e8a93f`  |
| 1036   | No file  | `c5a247e8a93f`  |
| 1026   | No file  | `c5a247e8a93f`  |
| 1016   | No file  | `c5a247e8a93f`  |
| 1009   | No file  | `c5a247e8a93f`  |
| 1005   | No file  | `c5a247e8a93f`  |
| 1000   | No file  | `c5a247e8a93f`  |
| 998    | No file  | `c5a247e8a93f`  |
| 990    | No file  | `c5a247e8a93f`  |
| 979    | No file  | `c5a247e8a93f`  |
| 972    | No file  | `c5a247e8a93f`  |
| 963    | No file  | `c5a247e8a93f`  |
| 955    | No file  | `c5a247e8a93f`  |
| 946    | No file  | `c5a247e8a93f`  |
| 938    | No file  | `c5a247e8a93f`  |
| 927    | No file  | `c5a247e8a93f`  |
| 911    | No file  | `c5a247e8a93f`  |
| 904    | No file  | `c5a247e8a93f`  |
| 899    | No file  | `c5a247e8a93f`  |
| 894    | No file  | `c5a247e8a93f`  |
| 885    | No file  | `c5a247e8a93f`  |
| 879    | No file  | `c5a247e8a93f`  |
| 872    | No file  | `c5a247e8a93f`  |
| 864    | No file  | `c5a247e8a93f`  |
| 855    | No file  | `c5a247e8a93f`  |
| 853    | No file  | `c5a247e8a93f`  |
| 845    | No file  | `c5a247e8a93f`  |
| 837    | No file  | `c5a247e8a93f`  |
| 829    | No file  | `c5a247e8a93f`  |
| 822    | No file  | `c5a247e8a93f`  |
| 814    | No file  | `c5a247e8a93f`  |
| 805    | No file  | `c5a247e8a93f`  |
| 794    | No file  | `c5a247e8a93f`  |
| 787    | No file  | `c5a247e8a93f`  |
| 780    | No file  | `c5a247e8a93f`  |
| 771    | No file  | `c5a247e8a93f`  |
| 760    | No file  | `c5a247e8a93f`  |
| 748    | No file  | `c5a247e8a93f`  |
| 741    | No file  | `c5a247e8a93f`  |
| 736    | No file  | `c5a247e8a93f`  |
| 731    | No file  | `c5a247e8a93f`  |
| 723    | No file  | `c5a247e8a93f`  |
| 711    | No file  | `c5a247e8a93f`  |
| 707    | No file  | `c5a247e8a93f`  |
| 697    | No file  | `c5a247e8a93f`  |
| 689    | No file  | `c5a247e8a93f`  |
| 683    | No file  | `c5a247e8a93f`  |
| 678    | No file  | `c5a247e8a93f`  |
| 670    | No file  | `c5a247e8a93f`  |
| 661    | No file  | `c5a247e8a93f`  |
| 656    | No file  | `c5a247e8a93f`  |
| 652    | No file  | `c5a247e8a93f`  |
| 643    | No file  | `c5a247e8a93f`  |
| 637    | No file  | `c5a247e8a93f`  |
| 630    | No file  | `c5a247e8a93f`  |
| 627    | No file  | `c5a247e8a93f`  |
| 621    | No file  | `c5a247e8a93f`  |
| 617    | No file  | `c5a247e8a93f`  |
| 615    | No file  | `c5a247e8a93f`  |
| 606    | No file  | `c5a247e8a93f`  |
| 599    | No file  | `c5a247e8a93f`  |
| 592    | No file  | `c5a247e8a93f`  |
| 586    | No file  | `c5a247e8a93f`  |
| 577    | No file  | `c5a247e8a93f`  |
| 569    | No file  | `c5a247e8a93f`  |
| 561    | No file  | `c5a247e8a93f`  |
| 554    | No file  | `c5a247e8a93f`  |
| 542    | No file  | `c5a247e8a93f`  |
| 532    | No file  | `c5a247e8a93f`  |
| 531    | No file  | `c5a247e8a93f`  |
| 526    | No file  | `c5a247e8a93f`  |
| 521    | No file  | `c5a247e8a93f`  |
| 517    | No file  | `c5a247e8a93f`  |
| 510    | No file  | `c5a247e8a93f`  |
| 508    | No file  | `c5a247e8a93f`  |
| 504    | No file  | `c5a247e8a93f`  |
| 497    | No file  | `c5a247e8a93f`  |
| 491    | No file  | `c5a247e8a93f`  |
| 485    | No file  | `c5a247e8a93f`  |
| 478    | No file  | `c5a247e8a93f`  |
| 472    | No file  | `c5a247e8a93f`  |
| 466    | No file  | `c5a247e8a93f`  |
| 457    | No file  | `c5a247e8a93f`  |
| 452    | No file  | `c5a247e8a93f`  |
| 449    | No file  | `c5a247e8a93f`  |
| 435    | No file  | `c5a247e8a93f`  |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                                                          |
| ----------------------- | -------- | ----------------------------------------------------------------------------- |
| `itempuzzleoffset.dbss` | Optional | `puzzle_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`   | Optional | Item names (type `0`)                                                          |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 386 x 120 = 46,324 bytes.

### Row (120 bytes)

The 2016 `gc::ItemPuzzleStaticStatus` packed: its members in order, with no
alignment padding and without the `_makeItemEnchantStaticStatus` pointer.

| Offset  | Type    | Field                   | Notes                                                                 |
| ------- | ------- | ----------------------- | --------------------------------------------------------------------- |
| `+0x00` | u16     | puzzle_key              | Row key; `1` to `531` on client 3474, not every number used            |
| `+0x02` | u32[25] | puzzle_item_keys        | The 5 x 5 grid, row by row (`row x 5 + column`); item enchant keys, `0` for an empty cell; level `0` on every cell of clients 1784 and 3474 |
| `+0x66` | u32     | start_puzzle_item_key   | The first non-zero cell of the grid                                    |
| `+0x6A` | i32     | start_puzzle_item_index | Grid index of that cell                                                |
| `+0x6E` | i16     | width_max_index         | The highest column (0 to 4) holding an item                            |
| `+0x70` | i16     | height_max_index        | The highest row (0 to 4) holding an item                               |
| `+0x72` | u32     | make_item_key           | The item the puzzle makes; `0` on every row (clients 1784 and 3474), see Field Names |
| `+0x76` | i16     | line_count              | `5` on every row: the grid side                                        |

The rows are not sorted by key.

### `itempuzzleoffset.dbss`

Bare offset table into `itempuzzle.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `itempuzzle.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u16  | puzzle_key  | Key of the row it points at                              |
| `+0x02` | u32  | data_offset | Absolute offset of the row in `itempuzzle.dbss`, at its `puzzle_key` |
| `+0x06` | u32  | data_size   | `120` on every row: the whole row                        |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3474 every
index row points at the row with its key.

## Field Names

The 2016 client's debug symbols have `gc::ItemPuzzleStaticStatus` as
`_key` (u16), `_puzzle` (25 `gc::ItemEnchantKey`), `_startPuzzleItem`,
`_startPuzzleItemIndex`, `_widthMaxIndex`, `_heightMaxIndex`,
`_makeItemKey`, a pointer to the made item's `gc::ItemEnchantStaticStatus`
and `_lineCount`; the file holds every member but the pointer, in that
order. The `ItemPuzzle_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `PuzzleKey`, `Puzzle0`
to `Puzzle4`, `MakeItemKey` and `MakeItemEnchantLevel`, five sheet rows per
key (one per grid row). It matches the file:

| Field            | Column                           | Same value (client 1784) | Same value (client 3474) |
| ---------------- | -------------------------------- | ------------------------ | ------------------------ |
| puzzle_key       | `PuzzleKey`                      | 311 of 311               | 283 of 386               |
| puzzle_item_keys | `Puzzle0` to `Puzzle4`, 5 rows   | 311 of 311               | 282 of 283               |
| make_item_key    | `MakeItemKey`, `MakeItemEnchantLevel` | 311 of 311          | 283 of 283               |

The sheet has 337 keys, 26 more than client 1784 ships; client 3474 adds
103 keys and lays one shared puzzle out differently. The developer
workbook (`datasheet_itemdatatable_quest.xlsm`) marks `MakeItemKey` and
`MakeItemEnchantLevel` with `%`, server only: the compiled sheet and both
clients hold `0`. The client 519 server table `ItemPuzzle_Table` has the
same columns with the made items filled in (key `94` makes item `12034`).
`start_puzzle_item_key`, `start_puzzle_item_index`, `width_max_index`,
`height_max_index` and `line_count` have no sheet column; the 2016 names
fit what every row of clients 1784 and 3474 holds (Notes).

## Notes

- On every row of clients 1784 and 3474, `start_puzzle_item_index` is the
  first non-zero cell of `puzzle_item_keys`, `start_puzzle_item_key` the
  item in it, and `width_max_index` and `height_max_index` the highest
  column and row holding an item, counted from the grid's left and top
  edge.
- The treasure guide (`panel_window_treasure_guidebook_all_1.luac`) draws
  a treasure item's puzzle with `ToClient_GetPuzzleStaticStatusByPuzzleKey`
  and `getPuzzleItemKey(row, column)`, the grid order of
  `puzzle_item_keys`. The inventory (`panel_window_inventory_all_2.luac`
  and `_4.luac`) finds a laid-out puzzle with `findPuzzleAndReadyMake` and
  makes it with `requestMakePuzzle`; the combine bag
  (`panel_window_combine_1.luac` and `_2.luac`) has its own
  `findPuzzleAndReadyMakeCombineBag` and `requestMakePuzzleFromCombine`.
