# `profiling.dbss` Format

## Purpose

Information messages grouped by profiling key: on client 3482 27 keys
with 75 messages, each a Korean text that opens with `[<subject>]에 대한
정보를 획득하였습니다.` ("Obtained information on [<subject>]") and goes on
about an NPC, a monster, a place or a game system. Three
messages carry a reward script that hands out an item. No client Lua names
the file or a getter for it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes  | Records         | Row bytes                   |
| ------ | -------------- | ---------------------- | ------ | --------------- | --------------------------- |
| 2      | 1280 and later | `profiling.dbss`       | 23,948 | 75 Info, 27 Row | 66 to 1,766, 316 on average |
| 2      | 1280 and later | `profilingoffset.dbss` | 274    | 27 Offset Row   | 10                          |
| 1      | 1267 to 1276   | `profiling.dbss`       | 21,876 | 73 Info, 25 Row | 66 to 648, 298 on average   |
| 1      | 1267 to 1276   | `profilingoffset.dbss` | 254    | 25 Offset Row   | 10                          |

| Layout | File                   | Known             | Unknown      |
| ------ | ---------------------- | ----------------- | ------------ |
| 2      | `profiling.dbss`       | 23,840 B (99.5%)  | 108 B (0.5%) |
| 2      | `profilingoffset.dbss` | 274 B (100.0%)    | 0 B (0.0%)   |
| 1      | `profiling.dbss`       | 21,876 B (100.0%) | 0 B (0.0%)   |
| 1      | `profilingoffset.dbss` | 254 B (100.0%)    | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `8bf0896dcb7f`  |
| 3482   | Layout 2 | `8bf0896dcb7f`  |
| 3474   | Layout 2 | `8bf0896dcb7f`  |
| 3473   | Layout 2 | `8bf0896dcb7f`  |
| 3464   | Layout 2 | `8bf0896dcb7f`  |
| 3458   | Layout 2 | `8bf0896dcb7f`  |
| 3454   | Layout 2 | `8bf0896dcb7f`  |
| 3444   | Layout 2 | `8bf0896dcb7f`  |
| 3435   | Layout 2 | `8bf0896dcb7f`  |
| 3426   | Layout 2 | `8bf0896dcb7f`  |
| 3418   | Layout 2 | `8bf0896dcb7f`  |
| 3412   | Layout 2 | `8bf0896dcb7f`  |
| 3402   | Layout 2 | `8bf0896dcb7f`  |
| 3396   | Layout 2 | `8bf0896dcb7f`  |
| 3387   | Layout 2 | `8bf0896dcb7f`  |
| 3381   | Layout 2 | `8bf0896dcb7f`  |
| 3373   | Layout 2 | `8bf0896dcb7f`  |
| 3364   | Layout 2 | `8bf0896dcb7f`  |
| 3356   | Layout 2 | `8bf0896dcb7f`  |
| 3349   | Layout 2 | `8bf0896dcb7f`  |
| 3342   | Layout 2 | `8bf0896dcb7f`  |
| 3335   | Layout 2 | `8bf0896dcb7f`  |
| 3326   | Layout 2 | `8bf0896dcb7f`  |
| 3321   | Layout 2 | `8bf0896dcb7f`  |
| 3314   | Layout 2 | `8bf0896dcb7f`  |
| 3303   | Layout 2 | `8bf0896dcb7f`  |
| 3302   | Layout 2 | `8bf0896dcb7f`  |
| 3293   | Layout 2 | `8bf0896dcb7f`  |
| 3283   | Layout 2 | `8bf0896dcb7f`  |
| 3275   | Layout 2 | `8bf0896dcb7f`  |
| 3267   | Layout 2 | `8bf0896dcb7f`  |
| 3258   | Layout 2 | `8bf0896dcb7f`  |
| 3251   | Layout 2 | `8bf0896dcb7f`  |
| 3242   | Layout 2 | `8bf0896dcb7f`  |
| 3235   | Layout 2 | `8bf0896dcb7f`  |
| 3229   | Layout 2 | `8bf0896dcb7f`  |
| 3212   | Layout 2 | `8bf0896dcb7f`  |
| 3203   | Layout 2 | `8bf0896dcb7f`  |
| 3193   | Layout 2 | `8bf0896dcb7f`  |
| 3186   | Layout 2 | `8bf0896dcb7f`  |
| 3177   | Layout 2 | `8bf0896dcb7f`  |
| 3169   | Layout 2 | `8bf0896dcb7f`  |
| 3158   | Layout 2 | `8bf0896dcb7f`  |
| 3151   | Layout 2 | `8bf0896dcb7f`  |
| 3144   | Layout 2 | `8bf0896dcb7f`  |
| 3133   | Layout 2 | `8bf0896dcb7f`  |
| 3125   | Layout 2 | `8bf0896dcb7f`  |
| 3118   | Layout 2 | `8bf0896dcb7f`  |
| 3111   | Layout 2 | `8bf0896dcb7f`  |
| 3103   | Layout 2 | `8bf0896dcb7f`  |
| 3095   | Layout 2 | `8bf0896dcb7f`  |
| 3086   | Layout 2 | `8bf0896dcb7f`  |
| 3072   | Layout 2 | `8bf0896dcb7f`  |
| 3062   | Layout 2 | `8bf0896dcb7f`  |
| 3052   | Layout 2 | `8bf0896dcb7f`  |
| 3045   | Layout 2 | `8bf0896dcb7f`  |
| 3037   | Layout 2 | `8bf0896dcb7f`  |
| 3030   | Layout 2 | `8bf0896dcb7f`  |
| 3021   | Layout 2 | `8bf0896dcb7f`  |
| 3012   | Layout 2 | `8bf0896dcb7f`  |
| 3002   | Layout 2 | `8bf0896dcb7f`  |
| 2995   | Layout 2 | `8bf0896dcb7f`  |
| 2987   | Layout 2 | `8bf0896dcb7f`  |
| 2978   | Layout 2 | `8bf0896dcb7f`  |
| 2970   | Layout 2 | `8bf0896dcb7f`  |
| 2959   | Layout 2 | `8bf0896dcb7f`  |
| 2951   | Layout 2 | `8bf0896dcb7f`  |
| 2942   | Layout 2 | `8bf0896dcb7f`  |
| 2935   | Layout 2 | `8bf0896dcb7f`  |
| 2932   | Layout 2 | `8bf0896dcb7f`  |
| 2923   | Layout 2 | `8bf0896dcb7f`  |
| 2919   | Layout 2 | `8bf0896dcb7f`  |
| 2907   | Layout 2 | `8bf0896dcb7f`  |
| 2900   | Layout 2 | `8bf0896dcb7f`  |
| 2891   | Layout 2 | `8bf0896dcb7f`  |
| 2882   | Layout 2 | `8bf0896dcb7f`  |
| 2872   | Layout 2 | `8bf0896dcb7f`  |
| 2863   | Layout 2 | `8bf0896dcb7f`  |
| 2855   | Layout 2 | `8bf0896dcb7f`  |
| 2849   | Layout 2 | `8bf0896dcb7f`  |
| 2844   | Layout 2 | `8bf0896dcb7f`  |
| 2834   | Layout 2 | `8bf0896dcb7f`  |
| 2825   | Layout 2 | `8bf0896dcb7f`  |
| 2819   | Layout 2 | `8bf0896dcb7f`  |
| 2811   | Layout 2 | `8bf0896dcb7f`  |
| 2803   | Layout 2 | `8bf0896dcb7f`  |
| 2794   | Layout 2 | `8bf0896dcb7f`  |
| 2783   | Layout 2 | `8bf0896dcb7f`  |
| 2774   | Layout 2 | `8bf0896dcb7f`  |
| 2765   | Layout 2 | `8bf0896dcb7f`  |
| 2756   | Layout 2 | `8bf0896dcb7f`  |
| 2750   | Layout 2 | `8bf0896dcb7f`  |
| 2743   | Layout 2 | `8bf0896dcb7f`  |
| 2736   | Layout 2 | `8bf0896dcb7f`  |
| 2726   | Layout 2 | `8bf0896dcb7f`  |
| 2717   | Layout 2 | `8bf0896dcb7f`  |
| 2709   | Layout 2 | `8bf0896dcb7f`  |
| 2703   | Layout 2 | `8bf0896dcb7f`  |
| 2695   | Layout 2 | `8bf0896dcb7f`  |
| 2684   | Layout 2 | `8bf0896dcb7f`  |
| 2672   | Layout 2 | `8bf0896dcb7f`  |
| 2665   | Layout 2 | `8bf0896dcb7f`  |
| 2657   | Layout 2 | `8bf0896dcb7f`  |
| 2649   | Layout 2 | `8bf0896dcb7f`  |
| 2644   | Layout 2 | `8bf0896dcb7f`  |
| 2637   | Layout 2 | `8bf0896dcb7f`  |
| 2629   | Layout 2 | `8bf0896dcb7f`  |
| 2619   | Layout 2 | `8bf0896dcb7f`  |
| 2612   | Layout 2 | `8bf0896dcb7f`  |
| 2606   | Layout 2 | `8bf0896dcb7f`  |
| 2602   | Layout 2 | `8bf0896dcb7f`  |
| 2601   | Layout 2 | `8bf0896dcb7f`  |
| 2592   | Layout 2 | `8bf0896dcb7f`  |
| 2583   | Layout 2 | `8bf0896dcb7f`  |
| 2575   | Layout 2 | `8bf0896dcb7f`  |
| 2567   | Layout 2 | `8bf0896dcb7f`  |
| 2560   | Layout 2 | `8bf0896dcb7f`  |
| 2553   | Layout 2 | `8bf0896dcb7f`  |
| 2545   | Layout 2 | `8bf0896dcb7f`  |
| 2538   | Layout 2 | `8bf0896dcb7f`  |
| 2529   | Layout 2 | `8bf0896dcb7f`  |
| 2519   | Layout 2 | `8bf0896dcb7f`  |
| 2513   | Layout 2 | `8bf0896dcb7f`  |
| 2510   | Layout 2 | `8bf0896dcb7f`  |
| 2507   | Layout 2 | `8bf0896dcb7f`  |
| 2503   | Layout 2 | `8bf0896dcb7f`  |
| 2498   | Layout 2 | `8bf0896dcb7f`  |
| 2492   | Layout 2 | `8bf0896dcb7f`  |
| 2487   | Layout 2 | `8bf0896dcb7f`  |
| 2480   | Layout 2 | `8bf0896dcb7f`  |
| 2474   | Layout 2 | `8bf0896dcb7f`  |
| 2468   | Layout 2 | `8bf0896dcb7f`  |
| 2460   | Layout 2 | `8bf0896dcb7f`  |
| 2453   | Layout 2 | `8bf0896dcb7f`  |
| 2444   | Layout 2 | `8bf0896dcb7f`  |
| 2438   | Layout 2 | `8bf0896dcb7f`  |
| 2434   | Layout 2 | `8bf0896dcb7f`  |
| 2429   | Layout 2 | `8bf0896dcb7f`  |
| 2421   | Layout 2 | `8bf0896dcb7f`  |
| 2414   | Layout 2 | `8bf0896dcb7f`  |
| 2407   | Layout 2 | `8bf0896dcb7f`  |
| 2401   | Layout 2 | `8bf0896dcb7f`  |
| 2397   | Layout 2 | `8bf0896dcb7f`  |
| 2393   | Layout 2 | `8bf0896dcb7f`  |
| 2384   | Layout 2 | `8bf0896dcb7f`  |
| 2378   | Layout 2 | `8bf0896dcb7f`  |
| 2372   | Layout 2 | `8bf0896dcb7f`  |
| 2358   | Layout 2 | `8bf0896dcb7f`  |
| 2352   | Layout 2 | `8bf0896dcb7f`  |
| 2347   | Layout 2 | `8bf0896dcb7f`  |
| 2343   | Layout 2 | `8bf0896dcb7f`  |
| 2335   | Layout 2 | `8bf0896dcb7f`  |
| 2327   | Layout 2 | `8bf0896dcb7f`  |
| 2324   | Layout 2 | `8bf0896dcb7f`  |
| 2319   | Layout 2 | `8bf0896dcb7f`  |
| 2313   | Layout 2 | `8bf0896dcb7f`  |
| 2308   | Layout 2 | `8bf0896dcb7f`  |
| 2302   | Layout 2 | `8bf0896dcb7f`  |
| 2295   | Layout 2 | `8bf0896dcb7f`  |
| 2290   | Layout 2 | `8bf0896dcb7f`  |
| 2284   | Layout 2 | `8bf0896dcb7f`  |
| 2276   | Layout 2 | `8bf0896dcb7f`  |
| 2269   | Layout 2 | `8bf0896dcb7f`  |
| 2259   | Layout 2 | `8bf0896dcb7f`  |
| 2250   | Layout 2 | `8bf0896dcb7f`  |
| 2243   | Layout 2 | `8bf0896dcb7f`  |
| 2235   | Layout 2 | `8bf0896dcb7f`  |
| 2229   | Layout 2 | `8bf0896dcb7f`  |
| 2224   | Layout 2 | `8bf0896dcb7f`  |
| 2218   | Layout 2 | `8bf0896dcb7f`  |
| 2215   | Layout 2 | `8bf0896dcb7f`  |
| 2207   | Layout 2 | `8bf0896dcb7f`  |
| 2203   | Layout 2 | `8bf0896dcb7f`  |
| 2196   | Layout 2 | `8bf0896dcb7f`  |
| 2192   | Layout 2 | `8bf0896dcb7f`  |
| 2189   | Layout 2 | `8bf0896dcb7f`  |
| 2183   | Layout 2 | `8bf0896dcb7f`  |
| 2179   | Layout 2 | `8bf0896dcb7f`  |
| 2171   | Layout 2 | `8bf0896dcb7f`  |
| 2163   | Layout 2 | `8bf0896dcb7f`  |
| 2156   | Layout 2 | `8bf0896dcb7f`  |
| 2151   | Layout 2 | `8bf0896dcb7f`  |
| 2147   | Layout 2 | `8bf0896dcb7f`  |
| 2142   | Layout 2 | `8bf0896dcb7f`  |
| 2138   | Layout 2 | `8bf0896dcb7f`  |
| 2134   | Layout 2 | `8bf0896dcb7f`  |
| 2130   | Layout 2 | `8bf0896dcb7f`  |
| 2122   | Layout 2 | `8bf0896dcb7f`  |
| 2107   | Layout 2 | `8bf0896dcb7f`  |
| 2098   | Layout 2 | `8bf0896dcb7f`  |
| 2089   | Layout 2 | `8bf0896dcb7f`  |
| 2081   | Layout 2 | `8bf0896dcb7f`  |
| 2073   | Layout 2 | `8bf0896dcb7f`  |
| 2067   | Layout 2 | `8bf0896dcb7f`  |
| 2063   | Layout 2 | `8bf0896dcb7f`  |
| 2059   | Layout 2 | `8bf0896dcb7f`  |
| 2052   | Layout 2 | `8bf0896dcb7f`  |
| 2044   | Layout 2 | `8bf0896dcb7f`  |
| 2039   | Layout 2 | `8bf0896dcb7f`  |
| 2032   | Layout 2 | `8bf0896dcb7f`  |
| 2025   | Layout 2 | `8bf0896dcb7f`  |
| 2011   | Layout 2 | `8bf0896dcb7f`  |
| 2005   | Layout 2 | `8bf0896dcb7f`  |
| 2000   | Layout 2 | `8bf0896dcb7f`  |
| 1996   | Layout 2 | `8bf0896dcb7f`  |
| 1991   | Layout 2 | `8bf0896dcb7f`  |
| 1985   | Layout 2 | `8bf0896dcb7f`  |
| 1980   | Layout 2 | `8bf0896dcb7f`  |
| 1969   | Layout 2 | `8bf0896dcb7f`  |
| 1964   | Layout 2 | `8bf0896dcb7f`  |
| 1958   | Layout 2 | `8bf0896dcb7f`  |
| 1950   | Layout 2 | `8bf0896dcb7f`  |
| 1945   | Layout 2 | `8bf0896dcb7f`  |
| 1937   | Layout 2 | `8bf0896dcb7f`  |
| 1933   | Layout 2 | `8bf0896dcb7f`  |
| 1927   | Layout 2 | `8bf0896dcb7f`  |
| 1921   | Layout 2 | `8bf0896dcb7f`  |
| 1914   | Layout 2 | `8bf0896dcb7f`  |
| 1908   | Layout 2 | `8bf0896dcb7f`  |
| 1897   | Layout 2 | `8bf0896dcb7f`  |
| 1892   | Layout 2 | `8bf0896dcb7f`  |
| 1886   | Layout 2 | `8bf0896dcb7f`  |
| 1881   | Layout 2 | `8bf0896dcb7f`  |
| 1871   | Layout 2 | `8bf0896dcb7f`  |
| 1866   | Layout 2 | `8bf0896dcb7f`  |
| 1862   | Layout 2 | `8bf0896dcb7f`  |
| 1854   | Layout 2 | `8bf0896dcb7f`  |
| 1846   | Layout 2 | `8bf0896dcb7f`  |
| 1838   | Layout 2 | `8bf0896dcb7f`  |
| 1832   | Layout 2 | `8bf0896dcb7f`  |
| 1826   | Layout 2 | `8bf0896dcb7f`  |
| 1822   | Layout 2 | `8bf0896dcb7f`  |
| 1818   | Layout 2 | `8bf0896dcb7f`  |
| 1804   | Layout 2 | `8bf0896dcb7f`  |
| 1794   | Layout 2 | `8bf0896dcb7f`  |
| 1790   | Layout 2 | `8bf0896dcb7f`  |
| 1784   | Layout 2 | `8bf0896dcb7f`  |
| 1774   | Layout 2 | `8bf0896dcb7f`  |
| 1771   | Layout 2 | `8bf0896dcb7f`  |
| 1762   | Layout 2 | `8bf0896dcb7f`  |
| 1759   | Layout 2 | `8bf0896dcb7f`  |
| 1754   | Layout 2 | `8bf0896dcb7f`  |
| 1749   | Layout 2 | `8bf0896dcb7f`  |
| 1743   | Layout 2 | `8bf0896dcb7f`  |
| 1737   | Layout 2 | `8bf0896dcb7f`  |
| 1731   | Layout 2 | `8bf0896dcb7f`  |
| 1725   | Layout 2 | `8bf0896dcb7f`  |
| 1717   | Layout 2 | `8bf0896dcb7f`  |
| 1710   | Layout 2 | `8bf0896dcb7f`  |
| 1704   | Layout 2 | `8bf0896dcb7f`  |
| 1698   | Layout 2 | `8bf0896dcb7f`  |
| 1690   | Layout 2 | `8bf0896dcb7f`  |
| 1685   | Layout 2 | `8bf0896dcb7f`  |
| 1680   | Layout 2 | `8bf0896dcb7f`  |
| 1674   | Layout 2 | `8bf0896dcb7f`  |
| 1668   | Layout 2 | `8bf0896dcb7f`  |
| 1659   | Layout 2 | `8bf0896dcb7f`  |
| 1649   | Layout 2 | `8bf0896dcb7f`  |
| 1642   | Layout 2 | `8bf0896dcb7f`  |
| 1636   | Layout 2 | `8bf0896dcb7f`  |
| 1628   | Layout 2 | `8bf0896dcb7f`  |
| 1622   | Layout 2 | `8bf0896dcb7f`  |
| 1614   | Layout 2 | `8bf0896dcb7f`  |
| 1608   | Layout 2 | `8bf0896dcb7f`  |
| 1602   | Layout 2 | `8bf0896dcb7f`  |
| 1598   | Layout 2 | `8bf0896dcb7f`  |
| 1594   | Layout 2 | `8bf0896dcb7f`  |
| 1590   | Layout 2 | `8bf0896dcb7f`  |
| 1587   | Layout 2 | `8bf0896dcb7f`  |
| 1584   | Layout 2 | `8bf0896dcb7f`  |
| 1579   | Layout 2 | `8bf0896dcb7f`  |
| 1572   | Layout 2 | `8bf0896dcb7f`  |
| 1565   | Layout 2 | `8bf0896dcb7f`  |
| 1559   | Layout 2 | `8bf0896dcb7f`  |
| 1554   | Layout 2 | `8bf0896dcb7f`  |
| 1547   | Layout 2 | `8bf0896dcb7f`  |
| 1537   | Layout 2 | `8bf0896dcb7f`  |
| 1529   | Layout 2 | `8bf0896dcb7f`  |
| 1524   | Layout 2 | `8bf0896dcb7f`  |
| 1519   | Layout 2 | `8bf0896dcb7f`  |
| 1509   | Layout 2 | `8bf0896dcb7f`  |
| 1506   | Layout 2 | `8bf0896dcb7f`  |
| 1504   | Layout 2 | `8bf0896dcb7f`  |
| 1500   | Layout 2 | `8bf0896dcb7f`  |
| 1493   | Layout 2 | `8bf0896dcb7f`  |
| 1489   | Layout 2 | `8bf0896dcb7f`  |
| 1485   | Layout 2 | `8bf0896dcb7f`  |
| 1481   | Layout 2 | `8bf0896dcb7f`  |
| 1474   | Layout 2 | `8bf0896dcb7f`  |
| 1466   | Layout 2 | `8bf0896dcb7f`  |
| 1462   | Layout 2 | `8bf0896dcb7f`  |
| 1459   | Layout 2 | `8bf0896dcb7f`  |
| 1453   | Layout 2 | `8bf0896dcb7f`  |
| 1450   | Layout 2 | `8bf0896dcb7f`  |
| 1445   | Layout 2 | `8bf0896dcb7f`  |
| 1439   | Layout 2 | `8bf0896dcb7f`  |
| 1433   | Layout 2 | `8bf0896dcb7f`  |
| 1430   | Layout 2 | `8bf0896dcb7f`  |
| 1426   | Layout 2 | `8bf0896dcb7f`  |
| 1421   | Layout 2 | `8bf0896dcb7f`  |
| 1417   | Layout 2 | `8bf0896dcb7f`  |
| 1416   | Layout 2 | `8bf0896dcb7f`  |
| 1409   | Layout 2 | `8bf0896dcb7f`  |
| 1405   | Layout 2 | `8bf0896dcb7f`  |
| 1401   | Layout 2 | `8bf0896dcb7f`  |
| 1396   | Layout 2 | `8bf0896dcb7f`  |
| 1391   | Layout 2 | `8bf0896dcb7f`  |
| 1390   | Layout 2 | `8bf0896dcb7f`  |
| 1386   | Layout 2 | `8bf0896dcb7f`  |
| 1381   | Layout 2 | `8bf0896dcb7f`  |
| 1379   | Layout 2 | `8bf0896dcb7f`  |
| 1372   | Layout 2 | `8bf0896dcb7f`  |
| 1366   | Layout 2 | `8bf0896dcb7f`  |
| 1364   | Layout 2 | `8bf0896dcb7f`  |
| 1363   | Layout 2 | `8bf0896dcb7f`  |
| 1360   | Layout 2 | `8bf0896dcb7f`  |
| 1358   | Layout 2 | `8bf0896dcb7f`  |
| 1355   | Layout 2 | `8bf0896dcb7f`  |
| 1351   | Layout 2 | `8bf0896dcb7f`  |
| 1348   | Layout 2 | `8bf0896dcb7f`  |
| 1346   | Layout 2 | `8bf0896dcb7f`  |
| 1341   | Layout 2 | `8bf0896dcb7f`  |
| 1340   | Layout 2 | `8bf0896dcb7f`  |
| 1338   | Layout 2 | `8bf0896dcb7f`  |
| 1335   | Layout 2 | `8bf0896dcb7f`  |
| 1333   | Layout 2 | `8bf0896dcb7f`  |
| 1329   | Layout 2 | `8bf0896dcb7f`  |
| 1327   | Layout 2 | `8bf0896dcb7f`  |
| 1324   | Layout 2 | `8bf0896dcb7f`  |
| 1321   | Layout 2 | `8bf0896dcb7f`  |
| 1319   | Layout 2 | `8bf0896dcb7f`  |
| 1318   | Layout 2 | `8bf0896dcb7f`  |
| 1316   | Layout 2 | `8bf0896dcb7f`  |
| 1313   | Layout 2 | `8bf0896dcb7f`  |
| 1311   | Layout 2 | `8bf0896dcb7f`  |
| 1309   | Layout 2 | `8bf0896dcb7f`  |
| 1304   | Layout 2 | `8bf0896dcb7f`  |
| 1292   | Layout 2 | `8bf0896dcb7f`  |
| 1286   | Layout 2 | `8bf0896dcb7f`  |
| 1280   | Layout 2 | `8bf0896dcb7f`  |
| 1276   | Layout 1 | `8bf0896dcb7f`  |
| 1267   | Layout 1 | `8bf0896dcb7f`  |
| 1261   | No file  | `8bf0896dcb7f`  |
| 1256   | No file  | `8bf0896dcb7f`  |
| 1250   | No file  | `8bf0896dcb7f`  |
| 1246   | No file  | `8bf0896dcb7f`  |
| 1239   | No file  | `8bf0896dcb7f`  |
| 1230   | No file  | `8bf0896dcb7f`  |
| 1226   | No file  | `8bf0896dcb7f`  |
| 1220   | No file  | `8bf0896dcb7f`  |
| 1217   | No file  | `8bf0896dcb7f`  |
| 1211   | No file  | `8bf0896dcb7f`  |
| 1210   | No file  | `8bf0896dcb7f`  |
| 1208   | No file  | `8bf0896dcb7f`  |
| 1203   | No file  | `8bf0896dcb7f`  |
| 1197   | No file  | `8bf0896dcb7f`  |
| 1194   | No file  | `8bf0896dcb7f`  |
| 1192   | No file  | `8bf0896dcb7f`  |
| 1187   | No file  | `8bf0896dcb7f`  |
| 1183   | No file  | `8bf0896dcb7f`  |
| 1177   | No file  | `8bf0896dcb7f`  |
| 1173   | No file  | `8bf0896dcb7f`  |
| 1167   | No file  | `8bf0896dcb7f`  |
| 1164   | No file  | `8bf0896dcb7f`  |
| 1156   | No file  | `8bf0896dcb7f`  |
| 1149   | No file  | `8bf0896dcb7f`  |
| 1144   | No file  | `8bf0896dcb7f`  |
| 1137   | No file  | `8bf0896dcb7f`  |
| 1132   | No file  | `8bf0896dcb7f`  |
| 1127   | No file  | `8bf0896dcb7f`  |
| 1122   | No file  | `8bf0896dcb7f`  |
| 1118   | No file  | `8bf0896dcb7f`  |
| 1114   | No file  | `8bf0896dcb7f`  |
| 1109   | No file  | `8bf0896dcb7f`  |
| 1102   | No file  | `8bf0896dcb7f`  |
| 1096   | No file  | `8bf0896dcb7f`  |
| 1088   | No file  | `8bf0896dcb7f`  |
| 1081   | No file  | `8bf0896dcb7f`  |
| 1076   | No file  | `8bf0896dcb7f`  |
| 1069   | No file  | `8bf0896dcb7f`  |
| 1064   | No file  | `8bf0896dcb7f`  |
| 1058   | No file  | `8bf0896dcb7f`  |
| 1051   | No file  | `8bf0896dcb7f`  |
| 1044   | No file  | `8bf0896dcb7f`  |
| 1036   | No file  | `8bf0896dcb7f`  |
| 1026   | No file  | `8bf0896dcb7f`  |
| 1016   | No file  | `8bf0896dcb7f`  |
| 1009   | No file  | `8bf0896dcb7f`  |
| 1005   | No file  | `8bf0896dcb7f`  |
| 1000   | No file  | `8bf0896dcb7f`  |
| 998    | No file  | `8bf0896dcb7f`  |
| 990    | No file  | `8bf0896dcb7f`  |
| 979    | No file  | `8bf0896dcb7f`  |
| 972    | No file  | `8bf0896dcb7f`  |
| 963    | No file  | `8bf0896dcb7f`  |
| 955    | No file  | `8bf0896dcb7f`  |
| 946    | No file  | `8bf0896dcb7f`  |
| 938    | No file  | `8bf0896dcb7f`  |
| 927    | No file  | `8bf0896dcb7f`  |
| 911    | No file  | `8bf0896dcb7f`  |
| 904    | No file  | `8bf0896dcb7f`  |
| 899    | No file  | `8bf0896dcb7f`  |
| 894    | No file  | `8bf0896dcb7f`  |
| 885    | No file  | `8bf0896dcb7f`  |
| 879    | No file  | `8bf0896dcb7f`  |
| 872    | No file  | `8bf0896dcb7f`  |
| 864    | No file  | `8bf0896dcb7f`  |
| 855    | No file  | `8bf0896dcb7f`  |
| 853    | No file  | `8bf0896dcb7f`  |
| 845    | No file  | `8bf0896dcb7f`  |
| 837    | No file  | `8bf0896dcb7f`  |
| 829    | No file  | `8bf0896dcb7f`  |
| 822    | No file  | `8bf0896dcb7f`  |
| 814    | No file  | `8bf0896dcb7f`  |
| 805    | No file  | `8bf0896dcb7f`  |
| 794    | No file  | `8bf0896dcb7f`  |
| 787    | No file  | `8bf0896dcb7f`  |
| 780    | No file  | `8bf0896dcb7f`  |
| 771    | No file  | `8bf0896dcb7f`  |
| 760    | No file  | `8bf0896dcb7f`  |
| 748    | No file  | `8bf0896dcb7f`  |
| 741    | No file  | `8bf0896dcb7f`  |
| 736    | No file  | `8bf0896dcb7f`  |
| 731    | No file  | `8bf0896dcb7f`  |
| 723    | No file  | `8bf0896dcb7f`  |
| 711    | No file  | `8bf0896dcb7f`  |
| 707    | No file  | `8bf0896dcb7f`  |
| 697    | No file  | `8bf0896dcb7f`  |
| 689    | No file  | `8bf0896dcb7f`  |
| 683    | No file  | `8bf0896dcb7f`  |
| 678    | No file  | `8bf0896dcb7f`  |
| 670    | No file  | `8bf0896dcb7f`  |
| 661    | No file  | `8bf0896dcb7f`  |
| 656    | No file  | `8bf0896dcb7f`  |
| 652    | No file  | `8bf0896dcb7f`  |
| 643    | No file  | `8bf0896dcb7f`  |
| 637    | No file  | `8bf0896dcb7f`  |
| 630    | No file  | `8bf0896dcb7f`  |
| 627    | No file  | `8bf0896dcb7f`  |
| 621    | No file  | `8bf0896dcb7f`  |
| 617    | No file  | `8bf0896dcb7f`  |
| 615    | No file  | `8bf0896dcb7f`  |
| 606    | No file  | `8bf0896dcb7f`  |
| 599    | No file  | `8bf0896dcb7f`  |
| 592    | No file  | `8bf0896dcb7f`  |
| 586    | No file  | `8bf0896dcb7f`  |
| 577    | No file  | `8bf0896dcb7f`  |
| 569    | No file  | `8bf0896dcb7f`  |
| 561    | No file  | `8bf0896dcb7f`  |
| 554    | No file  | `8bf0896dcb7f`  |
| 542    | No file  | `8bf0896dcb7f`  |
| 532    | No file  | `8bf0896dcb7f`  |
| 531    | No file  | `8bf0896dcb7f`  |
| 526    | No file  | `8bf0896dcb7f`  |
| 521    | No file  | `8bf0896dcb7f`  |
| 517    | No file  | `8bf0896dcb7f`  |
| 510    | No file  | `8bf0896dcb7f`  |
| 508    | No file  | `8bf0896dcb7f`  |
| 504    | No file  | `8bf0896dcb7f`  |
| 497    | No file  | `8bf0896dcb7f`  |
| 491    | No file  | `8bf0896dcb7f`  |
| 485    | No file  | `8bf0896dcb7f`  |
| 478    | No file  | `8bf0896dcb7f`  |
| 472    | No file  | `8bf0896dcb7f`  |
| 466    | No file  | `8bf0896dcb7f`  |
| 457    | No file  | `8bf0896dcb7f`  |
| 452    | No file  | `8bf0896dcb7f`  |
| 449    | No file  | `8bf0896dcb7f`  |
| 435    | No file  | `8bf0896dcb7f`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role |
| ---------------------- | -------- | ---- |
| `profilingoffset.dbss` | Optional | `profiling_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type       | Field | Notes                                |
| ------- | ---------- | ----- | ------------------------------------ |
| `+0x00` | u32        | count | Number of keys; `27` on client 3482  |
| `+0x04` | Row[count] | rows  | See Row                              |

### Row (variable: 10 bytes + infos)

| Offset        | Type             | Field             | Notes |
| ------------- | ---------------- | ----------------- | ----- |
| `+0x00`       | u16              | profiling_key     | Row key: `1` to `23`, `51`, `52`, `101`, `102`, `151`, `152` and `300` on client 3482 |
| `+0x02`       | u32              | info_count        | `1` to `6`                                        |
| `+0x06`       | Info[info_count] | infos             | See Info                                          |
| `infos+0x00`  | u32              | unknown_infos_00  | `0` on every row of clients 1784 and 3482         |

### Info (variable: 16 bytes + texts)

| Offset                    | Type  | Field              | Notes |
| ------------------------- | ----- | ------------------ | ----- |
| `+0x00`                   | str16 | profile_message_kr | Korean message with `\n` line breaks |
| `profile_message_kr+0x00` | str16 | execute            | Reward script (`pushitem(34023,0,1);`, `PushItem(36014,0,1);`); empty on 72 of 75 infos |

### `profilingoffset.dbss`

Bare offset table into `profiling.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `profiling.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                           |
| ------- | ---- | ------------- | ----------------------------------------------- |
| `+0x00` | u16  | profiling_key | Key of the row it points at                     |
| `+0x02` | u32  | data_offset   | Absolute offset of the row in `profiling.dbss`  |
| `+0x06` | u32  | data_size     | Row size in bytes, `unknown_infos_00` included  |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3482 every one points at
the row with its key and the rows tile the file.

## Layout 1

A row ends after its last info: it has no `unknown_infos_00`, and the
`data_size` of `profilingoffset.dbss` is 4 bytes smaller per row. On
clients 1267 and 1276 the file holds 25 keys (`1` to `7`, `11` to `21`,
`23`, `51`, `52`, `101`, `102`, `151` and `152`) with 73 infos, and each
index row points at the row with its key. Only the Row differs from
Layout 2.

### Row (variable: 6 bytes + infos)

| Offset  | Type             | Field         | Notes |
| ------- | ---------------- | ------------- | ----- |
| `+0x00` | u16              | profiling_key |       |
| `+0x02` | u32              | info_count    |       |
| `+0x06` | Info[info_count] | infos         |       |

## Field Names

The 2016 `gc::ProfilingStaticStatus` is a `_key` (`u16`) and a list of
`gc::ProfilingInfo`, each a `_profileMessage`, a `_rewardsText` and the
compiled `_rewards`, the Row of Layout 1 without the compiled list;
`unknown_infos_00` came with Layout 2. The `Profiling` sheet of a private
server's `DataSheets.bexcel` on client 1784 has one row per info with the columns
`Key`, `DialogKey`, `ProfileMessage` and `Execute`: its 75 rows match the
75 infos of the client 1784 file in key, message and script, and 74 of
the 75 on client 3482 (one message was reworded). `DialogKey`
(`Profiling_Balenos_01`) is not in the file.
