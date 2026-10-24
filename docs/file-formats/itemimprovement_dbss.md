# `itemimprovement.dbss` Format

## Purpose

Gear Reform (`LUA_IMPROVEMENT_TITLE` "Reform"): the Black Spirit window where
a piece of gear and a reform stone turn into the next grade of that gear. A
record names the result and the gear it is made from, and a reform group that
ties it to the stones of
[`itemimprovementsource.dbss`](itemimprovementsource_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes   | Records         | Row bytes               |
| ------ | -------------- | ------- | ---------------------------- | ------- | --------------- | ----------------------- |
| 2      | 3258 and later | 3483    | `itemimprovement.dbss`       | 174,276 | 3,904 Record    | 29 to 45, 45 on average |
| 2      | 3258 and later | 3483    | `itemimprovementoffset.dbss` | 46,852  | 3,904 Index Row | 12                      |
| 1      | 1346 to 2498   | 2498    | `itemimprovement.dbss`       | 121,142 | 3,274 Record    | 37                      |
| 1      | 1346 to 2498   | 2498    | `itemimprovementoffset.dbss` | 39,292  | 3,274 Index Row | 12                      |

| Layout | File                         | Known             | Unknown          |
| ------ | ---------------------------- | ----------------- | ---------------- |
| 2      | `itemimprovement.dbss`       | 127,428 B (73.1%) | 46,848 B (26.9%) |
| 2      | `itemimprovementoffset.dbss` | 46,852 B (100.0%) | 0 B (0.0%)       |
| 1      | `itemimprovement.dbss`       | 108,046 B (89.2%) | 13,096 B (10.8%) |
| 1      | `itemimprovementoffset.dbss` | 39,292 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `ad1aac07ca5b`  |
| 3482   | Layout 2             | `ad1aac07ca5b`  |
| 3474   | Layout 2             | `ad1aac07ca5b`  |
| 3473   | Layout 2             | `ad1aac07ca5b`  |
| 3464   | Layout 2             | `ad1aac07ca5b`  |
| 3458   | Layout 2             | `ad1aac07ca5b`  |
| 3454   | Layout 2             | `ad1aac07ca5b`  |
| 3444   | Layout 2             | `ad1aac07ca5b`  |
| 3435   | Layout 2             | `ad1aac07ca5b`  |
| 3426   | Layout 2             | `ad1aac07ca5b`  |
| 3418   | Layout 2             | `ad1aac07ca5b`  |
| 3412   | Layout 2             | `ad1aac07ca5b`  |
| 3402   | Layout 2             | `ad1aac07ca5b`  |
| 3396   | Layout 2             | `ad1aac07ca5b`  |
| 3387   | Layout 2             | `ad1aac07ca5b`  |
| 3381   | Layout 2             | `ad1aac07ca5b`  |
| 3373   | Layout 2             | `ad1aac07ca5b`  |
| 3364   | Layout 2             | `ad1aac07ca5b`  |
| 3356   | Layout 2             | `ad1aac07ca5b`  |
| 3349   | Layout 2             | `ad1aac07ca5b`  |
| 3342   | Layout 2             | `ad1aac07ca5b`  |
| 3335   | Layout 2             | `ad1aac07ca5b`  |
| 3326   | Layout 2             | `ad1aac07ca5b`  |
| 3321   | Layout 2             | `ad1aac07ca5b`  |
| 3314   | Layout 2             | `ad1aac07ca5b`  |
| 3303   | Layout 2             | `ad1aac07ca5b`  |
| 3302   | Layout 2             | `ad1aac07ca5b`  |
| 3293   | Layout 2             | `ad1aac07ca5b`  |
| 3283   | Layout 2             | `ad1aac07ca5b`  |
| 3275   | Layout 2             | `ad1aac07ca5b`  |
| 3267   | Layout 2             | `ad1aac07ca5b`  |
| 3258   | Layout 2             | `ad1aac07ca5b`  |
| 3251   | No documented layout | `ad1aac07ca5b`  |
| 3242   | No documented layout | `ad1aac07ca5b`  |
| 3235   | No documented layout | `ad1aac07ca5b`  |
| 3229   | No documented layout | `ad1aac07ca5b`  |
| 3212   | No documented layout | `ad1aac07ca5b`  |
| 3203   | No documented layout | `ad1aac07ca5b`  |
| 3193   | No documented layout | `ad1aac07ca5b`  |
| 3186   | No documented layout | `ad1aac07ca5b`  |
| 3177   | No documented layout | `ad1aac07ca5b`  |
| 3169   | No documented layout | `ad1aac07ca5b`  |
| 3158   | No documented layout | `ad1aac07ca5b`  |
| 3151   | No documented layout | `ad1aac07ca5b`  |
| 3144   | No documented layout | `ad1aac07ca5b`  |
| 3133   | No documented layout | `ad1aac07ca5b`  |
| 3125   | No documented layout | `ad1aac07ca5b`  |
| 3118   | No documented layout | `ad1aac07ca5b`  |
| 3111   | No documented layout | `ad1aac07ca5b`  |
| 3103   | No documented layout | `ad1aac07ca5b`  |
| 3095   | No documented layout | `ad1aac07ca5b`  |
| 3086   | No documented layout | `ad1aac07ca5b`  |
| 3072   | No documented layout | `ad1aac07ca5b`  |
| 3062   | No documented layout | `ad1aac07ca5b`  |
| 3052   | No documented layout | `ad1aac07ca5b`  |
| 3045   | No documented layout | `ad1aac07ca5b`  |
| 3037   | No documented layout | `ad1aac07ca5b`  |
| 3030   | No documented layout | `ad1aac07ca5b`  |
| 3021   | No documented layout | `ad1aac07ca5b`  |
| 3012   | No documented layout | `ad1aac07ca5b`  |
| 3002   | No documented layout | `ad1aac07ca5b`  |
| 2995   | No documented layout | `ad1aac07ca5b`  |
| 2987   | No documented layout | `ad1aac07ca5b`  |
| 2978   | No documented layout | `ad1aac07ca5b`  |
| 2970   | No documented layout | `ad1aac07ca5b`  |
| 2959   | No documented layout | `ad1aac07ca5b`  |
| 2951   | No documented layout | `ad1aac07ca5b`  |
| 2942   | No documented layout | `ad1aac07ca5b`  |
| 2935   | No documented layout | `ad1aac07ca5b`  |
| 2932   | No documented layout | `ad1aac07ca5b`  |
| 2923   | No documented layout | `ad1aac07ca5b`  |
| 2919   | No documented layout | `ad1aac07ca5b`  |
| 2907   | No documented layout | `ad1aac07ca5b`  |
| 2900   | No documented layout | `ad1aac07ca5b`  |
| 2891   | No documented layout | `ad1aac07ca5b`  |
| 2882   | No documented layout | `ad1aac07ca5b`  |
| 2872   | No documented layout | `ad1aac07ca5b`  |
| 2863   | No documented layout | `ad1aac07ca5b`  |
| 2855   | No documented layout | `ad1aac07ca5b`  |
| 2849   | No documented layout | `ad1aac07ca5b`  |
| 2844   | No documented layout | `ad1aac07ca5b`  |
| 2834   | No documented layout | `ad1aac07ca5b`  |
| 2825   | No documented layout | `ad1aac07ca5b`  |
| 2819   | No documented layout | `ad1aac07ca5b`  |
| 2811   | No documented layout | `ad1aac07ca5b`  |
| 2803   | No documented layout | `ad1aac07ca5b`  |
| 2794   | No documented layout | `ad1aac07ca5b`  |
| 2783   | No documented layout | `ad1aac07ca5b`  |
| 2774   | No documented layout | `ad1aac07ca5b`  |
| 2765   | No documented layout | `ad1aac07ca5b`  |
| 2756   | No documented layout | `ad1aac07ca5b`  |
| 2750   | No documented layout | `ad1aac07ca5b`  |
| 2743   | No documented layout | `ad1aac07ca5b`  |
| 2736   | No documented layout | `ad1aac07ca5b`  |
| 2726   | No documented layout | `ad1aac07ca5b`  |
| 2717   | No documented layout | `ad1aac07ca5b`  |
| 2709   | No documented layout | `ad1aac07ca5b`  |
| 2703   | No documented layout | `ad1aac07ca5b`  |
| 2695   | No documented layout | `ad1aac07ca5b`  |
| 2684   | No documented layout | `ad1aac07ca5b`  |
| 2672   | No documented layout | `ad1aac07ca5b`  |
| 2665   | No documented layout | `ad1aac07ca5b`  |
| 2657   | No documented layout | `ad1aac07ca5b`  |
| 2649   | No documented layout | `ad1aac07ca5b`  |
| 2644   | No documented layout | `ad1aac07ca5b`  |
| 2637   | No documented layout | `ad1aac07ca5b`  |
| 2629   | No documented layout | `ad1aac07ca5b`  |
| 2619   | No documented layout | `ad1aac07ca5b`  |
| 2612   | No documented layout | `ad1aac07ca5b`  |
| 2606   | No documented layout | `ad1aac07ca5b`  |
| 2602   | No documented layout | `ad1aac07ca5b`  |
| 2601   | No documented layout | `ad1aac07ca5b`  |
| 2592   | No documented layout | `ad1aac07ca5b`  |
| 2583   | No documented layout | `ad1aac07ca5b`  |
| 2575   | No documented layout | `ad1aac07ca5b`  |
| 2567   | No documented layout | `ad1aac07ca5b`  |
| 2560   | No documented layout | `ad1aac07ca5b`  |
| 2553   | No documented layout | `ad1aac07ca5b`  |
| 2545   | No documented layout | `ad1aac07ca5b`  |
| 2538   | No documented layout | `ad1aac07ca5b`  |
| 2529   | No documented layout | `ad1aac07ca5b`  |
| 2519   | No documented layout | `ad1aac07ca5b`  |
| 2513   | No documented layout | `ad1aac07ca5b`  |
| 2510   | No documented layout | `ad1aac07ca5b`  |
| 2507   | No documented layout | `ad1aac07ca5b`  |
| 2503   | No documented layout | `ad1aac07ca5b`  |
| 2498   | Layout 1             | `ad1aac07ca5b`  |
| 2492   | Layout 1             | `ad1aac07ca5b`  |
| 2487   | Layout 1             | `ad1aac07ca5b`  |
| 2480   | Layout 1             | `ad1aac07ca5b`  |
| 2474   | Layout 1             | `ad1aac07ca5b`  |
| 2468   | Layout 1             | `ad1aac07ca5b`  |
| 2460   | Layout 1             | `ad1aac07ca5b`  |
| 2453   | Layout 1             | `ad1aac07ca5b`  |
| 2444   | Layout 1             | `ad1aac07ca5b`  |
| 2438   | Layout 1             | `ad1aac07ca5b`  |
| 2434   | Layout 1             | `ad1aac07ca5b`  |
| 2429   | Layout 1             | `ad1aac07ca5b`  |
| 2421   | Layout 1             | `ad1aac07ca5b`  |
| 2414   | Layout 1             | `ad1aac07ca5b`  |
| 2407   | Layout 1             | `ad1aac07ca5b`  |
| 2401   | Layout 1             | `ad1aac07ca5b`  |
| 2397   | Layout 1             | `ad1aac07ca5b`  |
| 2393   | Layout 1             | `ad1aac07ca5b`  |
| 2384   | Layout 1             | `ad1aac07ca5b`  |
| 2378   | Layout 1             | `ad1aac07ca5b`  |
| 2372   | Layout 1             | `ad1aac07ca5b`  |
| 2358   | Layout 1             | `ad1aac07ca5b`  |
| 2352   | Layout 1             | `ad1aac07ca5b`  |
| 2347   | Layout 1             | `ad1aac07ca5b`  |
| 2343   | Layout 1             | `ad1aac07ca5b`  |
| 2335   | Layout 1             | `ad1aac07ca5b`  |
| 2327   | Layout 1             | `ad1aac07ca5b`  |
| 2324   | Layout 1             | `ad1aac07ca5b`  |
| 2319   | Layout 1             | `ad1aac07ca5b`  |
| 2313   | Layout 1             | `ad1aac07ca5b`  |
| 2308   | Layout 1             | `ad1aac07ca5b`  |
| 2302   | Layout 1             | `ad1aac07ca5b`  |
| 2295   | Layout 1             | `ad1aac07ca5b`  |
| 2290   | Layout 1             | `ad1aac07ca5b`  |
| 2284   | Layout 1             | `ad1aac07ca5b`  |
| 2276   | Layout 1             | `ad1aac07ca5b`  |
| 2269   | Layout 1             | `ad1aac07ca5b`  |
| 2259   | Layout 1             | `ad1aac07ca5b`  |
| 2250   | Layout 1             | `ad1aac07ca5b`  |
| 2243   | Layout 1             | `ad1aac07ca5b`  |
| 2235   | Layout 1             | `ad1aac07ca5b`  |
| 2229   | Layout 1             | `ad1aac07ca5b`  |
| 2224   | Layout 1             | `ad1aac07ca5b`  |
| 2218   | Layout 1             | `ad1aac07ca5b`  |
| 2215   | Layout 1             | `ad1aac07ca5b`  |
| 2207   | Layout 1             | `ad1aac07ca5b`  |
| 2203   | Layout 1             | `ad1aac07ca5b`  |
| 2196   | Layout 1             | `ad1aac07ca5b`  |
| 2192   | Layout 1             | `ad1aac07ca5b`  |
| 2189   | Layout 1             | `ad1aac07ca5b`  |
| 2183   | Layout 1             | `ad1aac07ca5b`  |
| 2179   | Layout 1             | `ad1aac07ca5b`  |
| 2171   | Layout 1             | `ad1aac07ca5b`  |
| 2163   | Layout 1             | `ad1aac07ca5b`  |
| 2156   | Layout 1             | `ad1aac07ca5b`  |
| 2151   | Layout 1             | `ad1aac07ca5b`  |
| 2147   | Layout 1             | `ad1aac07ca5b`  |
| 2142   | Layout 1             | `ad1aac07ca5b`  |
| 2138   | Layout 1             | `ad1aac07ca5b`  |
| 2134   | Layout 1             | `ad1aac07ca5b`  |
| 2130   | Layout 1             | `ad1aac07ca5b`  |
| 2122   | Layout 1             | `ad1aac07ca5b`  |
| 2107   | Layout 1             | `ad1aac07ca5b`  |
| 2098   | Layout 1             | `ad1aac07ca5b`  |
| 2089   | Layout 1             | `ad1aac07ca5b`  |
| 2081   | Layout 1             | `ad1aac07ca5b`  |
| 2073   | Layout 1             | `ad1aac07ca5b`  |
| 2067   | Layout 1             | `ad1aac07ca5b`  |
| 2063   | Layout 1             | `ad1aac07ca5b`  |
| 2059   | Layout 1             | `ad1aac07ca5b`  |
| 2052   | Layout 1             | `ad1aac07ca5b`  |
| 2044   | Layout 1             | `ad1aac07ca5b`  |
| 2039   | Layout 1             | `ad1aac07ca5b`  |
| 2032   | Layout 1             | `ad1aac07ca5b`  |
| 2025   | Layout 1             | `ad1aac07ca5b`  |
| 2011   | Layout 1             | `ad1aac07ca5b`  |
| 2005   | Layout 1             | `ad1aac07ca5b`  |
| 2000   | Layout 1             | `ad1aac07ca5b`  |
| 1996   | Layout 1             | `ad1aac07ca5b`  |
| 1991   | Layout 1             | `ad1aac07ca5b`  |
| 1985   | Layout 1             | `ad1aac07ca5b`  |
| 1980   | Layout 1             | `ad1aac07ca5b`  |
| 1969   | Layout 1             | `ad1aac07ca5b`  |
| 1964   | Layout 1             | `ad1aac07ca5b`  |
| 1958   | Layout 1             | `ad1aac07ca5b`  |
| 1950   | Layout 1             | `ad1aac07ca5b`  |
| 1945   | Layout 1             | `ad1aac07ca5b`  |
| 1937   | Layout 1             | `ad1aac07ca5b`  |
| 1933   | Layout 1             | `ad1aac07ca5b`  |
| 1927   | Layout 1             | `ad1aac07ca5b`  |
| 1921   | Layout 1             | `ad1aac07ca5b`  |
| 1914   | Layout 1             | `ad1aac07ca5b`  |
| 1908   | Layout 1             | `ad1aac07ca5b`  |
| 1897   | Layout 1             | `ad1aac07ca5b`  |
| 1892   | Layout 1             | `ad1aac07ca5b`  |
| 1886   | Layout 1             | `ad1aac07ca5b`  |
| 1881   | Layout 1             | `ad1aac07ca5b`  |
| 1871   | Layout 1             | `ad1aac07ca5b`  |
| 1866   | Layout 1             | `ad1aac07ca5b`  |
| 1862   | Layout 1             | `ad1aac07ca5b`  |
| 1854   | Layout 1             | `ad1aac07ca5b`  |
| 1846   | Layout 1             | `ad1aac07ca5b`  |
| 1838   | Layout 1             | `ad1aac07ca5b`  |
| 1832   | Layout 1             | `ad1aac07ca5b`  |
| 1826   | Layout 1             | `ad1aac07ca5b`  |
| 1822   | Layout 1             | `ad1aac07ca5b`  |
| 1818   | Layout 1             | `ad1aac07ca5b`  |
| 1804   | Layout 1             | `ad1aac07ca5b`  |
| 1794   | Layout 1             | `ad1aac07ca5b`  |
| 1790   | Layout 1             | `ad1aac07ca5b`  |
| 1784   | Layout 1             | `ad1aac07ca5b`  |
| 1774   | Layout 1             | `ad1aac07ca5b`  |
| 1771   | Layout 1             | `ad1aac07ca5b`  |
| 1762   | Layout 1             | `ad1aac07ca5b`  |
| 1759   | Layout 1             | `ad1aac07ca5b`  |
| 1754   | Layout 1             | `ad1aac07ca5b`  |
| 1749   | Layout 1             | `ad1aac07ca5b`  |
| 1743   | Layout 1             | `ad1aac07ca5b`  |
| 1737   | Layout 1             | `ad1aac07ca5b`  |
| 1731   | Layout 1             | `ad1aac07ca5b`  |
| 1725   | Layout 1             | `ad1aac07ca5b`  |
| 1717   | Layout 1             | `ad1aac07ca5b`  |
| 1710   | Layout 1             | `ad1aac07ca5b`  |
| 1704   | Layout 1             | `ad1aac07ca5b`  |
| 1698   | Layout 1             | `ad1aac07ca5b`  |
| 1690   | Layout 1             | `ad1aac07ca5b`  |
| 1685   | Layout 1             | `ad1aac07ca5b`  |
| 1680   | Layout 1             | `ad1aac07ca5b`  |
| 1674   | Layout 1             | `ad1aac07ca5b`  |
| 1668   | Layout 1             | `ad1aac07ca5b`  |
| 1659   | Layout 1             | `ad1aac07ca5b`  |
| 1649   | Layout 1             | `ad1aac07ca5b`  |
| 1642   | Layout 1             | `ad1aac07ca5b`  |
| 1636   | Layout 1             | `ad1aac07ca5b`  |
| 1628   | Layout 1             | `ad1aac07ca5b`  |
| 1622   | Layout 1             | `ad1aac07ca5b`  |
| 1614   | Layout 1             | `ad1aac07ca5b`  |
| 1608   | Layout 1             | `ad1aac07ca5b`  |
| 1602   | Layout 1             | `ad1aac07ca5b`  |
| 1598   | Layout 1             | `ad1aac07ca5b`  |
| 1594   | Layout 1             | `ad1aac07ca5b`  |
| 1590   | Layout 1             | `ad1aac07ca5b`  |
| 1587   | Layout 1             | `ad1aac07ca5b`  |
| 1584   | Layout 1             | `ad1aac07ca5b`  |
| 1579   | Layout 1             | `ad1aac07ca5b`  |
| 1572   | Layout 1             | `ad1aac07ca5b`  |
| 1565   | Layout 1             | `ad1aac07ca5b`  |
| 1559   | Layout 1             | `ad1aac07ca5b`  |
| 1554   | Layout 1             | `ad1aac07ca5b`  |
| 1547   | Layout 1             | `ad1aac07ca5b`  |
| 1537   | Layout 1             | `ad1aac07ca5b`  |
| 1529   | Layout 1             | `ad1aac07ca5b`  |
| 1524   | Layout 1             | `ad1aac07ca5b`  |
| 1519   | Layout 1             | `ad1aac07ca5b`  |
| 1509   | Layout 1             | `ad1aac07ca5b`  |
| 1506   | Layout 1             | `ad1aac07ca5b`  |
| 1504   | Layout 1             | `ad1aac07ca5b`  |
| 1500   | Layout 1             | `ad1aac07ca5b`  |
| 1493   | Layout 1             | `ad1aac07ca5b`  |
| 1489   | Layout 1             | `ad1aac07ca5b`  |
| 1485   | Layout 1             | `ad1aac07ca5b`  |
| 1481   | Layout 1             | `ad1aac07ca5b`  |
| 1474   | Layout 1             | `ad1aac07ca5b`  |
| 1466   | Layout 1             | `ad1aac07ca5b`  |
| 1462   | Layout 1             | `ad1aac07ca5b`  |
| 1459   | Layout 1             | `ad1aac07ca5b`  |
| 1453   | Layout 1             | `ad1aac07ca5b`  |
| 1450   | Layout 1             | `ad1aac07ca5b`  |
| 1445   | No documented layout | `ad1aac07ca5b`  |
| 1439   | No documented layout | `ad1aac07ca5b`  |
| 1433   | No documented layout | `ad1aac07ca5b`  |
| 1430   | No documented layout | `ad1aac07ca5b`  |
| 1426   | No documented layout | `ad1aac07ca5b`  |
| 1421   | No documented layout | `ad1aac07ca5b`  |
| 1417   | No documented layout | `ad1aac07ca5b`  |
| 1416   | No documented layout | `ad1aac07ca5b`  |
| 1409   | No documented layout | `ad1aac07ca5b`  |
| 1405   | No documented layout | `ad1aac07ca5b`  |
| 1401   | No documented layout | `ad1aac07ca5b`  |
| 1396   | No documented layout | `ad1aac07ca5b`  |
| 1391   | Layout 1             | `ad1aac07ca5b`  |
| 1390   | Layout 1             | `ad1aac07ca5b`  |
| 1386   | Layout 1             | `ad1aac07ca5b`  |
| 1381   | Layout 1             | `ad1aac07ca5b`  |
| 1379   | Layout 1             | `ad1aac07ca5b`  |
| 1372   | Layout 1             | `ad1aac07ca5b`  |
| 1366   | Layout 1             | `ad1aac07ca5b`  |
| 1364   | Layout 1             | `ad1aac07ca5b`  |
| 1363   | Layout 1             | `ad1aac07ca5b`  |
| 1360   | Layout 1             | `ad1aac07ca5b`  |
| 1358   | Layout 1             | `ad1aac07ca5b`  |
| 1355   | Layout 1             | `ad1aac07ca5b`  |
| 1351   | Layout 1             | `ad1aac07ca5b`  |
| 1348   | Layout 1             | `ad1aac07ca5b`  |
| 1346   | Layout 1             | `ad1aac07ca5b`  |
| 1341   | No documented layout | `ad1aac07ca5b`  |
| 1340   | No documented layout | `ad1aac07ca5b`  |
| 1338   | No documented layout | `ad1aac07ca5b`  |
| 1335   | No documented layout | `ad1aac07ca5b`  |
| 1333   | No documented layout | `ad1aac07ca5b`  |
| 1329   | No documented layout | `ad1aac07ca5b`  |
| 1327   | No documented layout | `ad1aac07ca5b`  |
| 1324   | No documented layout | `ad1aac07ca5b`  |
| 1321   | No documented layout | `ad1aac07ca5b`  |
| 1319   | No documented layout | `ad1aac07ca5b`  |
| 1318   | No documented layout | `ad1aac07ca5b`  |
| 1316   | No documented layout | `ad1aac07ca5b`  |
| 1313   | No documented layout | `ad1aac07ca5b`  |
| 1311   | No documented layout | `ad1aac07ca5b`  |
| 1309   | No documented layout | `ad1aac07ca5b`  |
| 1304   | No documented layout | `ad1aac07ca5b`  |
| 1292   | No documented layout | `ad1aac07ca5b`  |
| 1286   | No documented layout | `ad1aac07ca5b`  |
| 1280   | No documented layout | `ad1aac07ca5b`  |
| 1276   | No file              | `ad1aac07ca5b`  |
| 1267   | No file              | `ad1aac07ca5b`  |
| 1261   | No file              | `ad1aac07ca5b`  |
| 1256   | No file              | `ad1aac07ca5b`  |
| 1250   | No file              | `ad1aac07ca5b`  |
| 1246   | No file              | `ad1aac07ca5b`  |
| 1239   | No file              | `ad1aac07ca5b`  |
| 1230   | No file              | `ad1aac07ca5b`  |
| 1226   | No file              | `ad1aac07ca5b`  |
| 1220   | No file              | `ad1aac07ca5b`  |
| 1217   | No file              | `ad1aac07ca5b`  |
| 1211   | No file              | `ad1aac07ca5b`  |
| 1210   | No file              | `ad1aac07ca5b`  |
| 1208   | No file              | `ad1aac07ca5b`  |
| 1203   | No file              | `ad1aac07ca5b`  |
| 1197   | No file              | `ad1aac07ca5b`  |
| 1194   | No file              | `ad1aac07ca5b`  |
| 1192   | No file              | `ad1aac07ca5b`  |
| 1187   | No file              | `ad1aac07ca5b`  |
| 1183   | No file              | `ad1aac07ca5b`  |
| 1177   | No file              | `ad1aac07ca5b`  |
| 1173   | No file              | `ad1aac07ca5b`  |
| 1167   | No file              | `ad1aac07ca5b`  |
| 1164   | No file              | `ad1aac07ca5b`  |
| 1156   | No file              | `ad1aac07ca5b`  |
| 1149   | No file              | `ad1aac07ca5b`  |
| 1144   | No file              | `ad1aac07ca5b`  |
| 1137   | No file              | `ad1aac07ca5b`  |
| 1132   | No file              | `ad1aac07ca5b`  |
| 1127   | No file              | `ad1aac07ca5b`  |
| 1122   | No file              | `ad1aac07ca5b`  |
| 1118   | No file              | `ad1aac07ca5b`  |
| 1114   | No file              | `ad1aac07ca5b`  |
| 1109   | No file              | `ad1aac07ca5b`  |
| 1102   | No file              | `ad1aac07ca5b`  |
| 1096   | No file              | `ad1aac07ca5b`  |
| 1088   | No file              | `ad1aac07ca5b`  |
| 1081   | No file              | `ad1aac07ca5b`  |
| 1076   | No file              | `ad1aac07ca5b`  |
| 1069   | No file              | `ad1aac07ca5b`  |
| 1064   | No file              | `ad1aac07ca5b`  |
| 1058   | No file              | `ad1aac07ca5b`  |
| 1051   | No file              | `ad1aac07ca5b`  |
| 1044   | No file              | `ad1aac07ca5b`  |
| 1036   | No file              | `ad1aac07ca5b`  |
| 1026   | No file              | `ad1aac07ca5b`  |
| 1016   | No file              | `ad1aac07ca5b`  |
| 1009   | No file              | `ad1aac07ca5b`  |
| 1005   | No file              | `ad1aac07ca5b`  |
| 1000   | No file              | `ad1aac07ca5b`  |
| 998    | No file              | `ad1aac07ca5b`  |
| 990    | No file              | `ad1aac07ca5b`  |
| 979    | No file              | `ad1aac07ca5b`  |
| 972    | No file              | `ad1aac07ca5b`  |
| 963    | No file              | `ad1aac07ca5b`  |
| 955    | No file              | `ad1aac07ca5b`  |
| 946    | No file              | `ad1aac07ca5b`  |
| 938    | No file              | `ad1aac07ca5b`  |
| 927    | No file              | `ad1aac07ca5b`  |
| 911    | No file              | `ad1aac07ca5b`  |
| 904    | No file              | `ad1aac07ca5b`  |
| 899    | No file              | `ad1aac07ca5b`  |
| 894    | No file              | `ad1aac07ca5b`  |
| 885    | No file              | `ad1aac07ca5b`  |
| 879    | No file              | `ad1aac07ca5b`  |
| 872    | No file              | `ad1aac07ca5b`  |
| 864    | No file              | `ad1aac07ca5b`  |
| 855    | No file              | `ad1aac07ca5b`  |
| 853    | No file              | `ad1aac07ca5b`  |
| 845    | No file              | `ad1aac07ca5b`  |
| 837    | No file              | `ad1aac07ca5b`  |
| 829    | No file              | `ad1aac07ca5b`  |
| 822    | No file              | `ad1aac07ca5b`  |
| 814    | No file              | `ad1aac07ca5b`  |
| 805    | No file              | `ad1aac07ca5b`  |
| 794    | No file              | `ad1aac07ca5b`  |
| 787    | No file              | `ad1aac07ca5b`  |
| 780    | No file              | `ad1aac07ca5b`  |
| 771    | No file              | `ad1aac07ca5b`  |
| 760    | No file              | `ad1aac07ca5b`  |
| 748    | No file              | `ad1aac07ca5b`  |
| 741    | No file              | `ad1aac07ca5b`  |
| 736    | No file              | `ad1aac07ca5b`  |
| 731    | No file              | `ad1aac07ca5b`  |
| 723    | No file              | `ad1aac07ca5b`  |
| 711    | No file              | `ad1aac07ca5b`  |
| 707    | No file              | `ad1aac07ca5b`  |
| 697    | No file              | `ad1aac07ca5b`  |
| 689    | No file              | `ad1aac07ca5b`  |
| 683    | No file              | `ad1aac07ca5b`  |
| 678    | No file              | `ad1aac07ca5b`  |
| 670    | No file              | `ad1aac07ca5b`  |
| 661    | No file              | `ad1aac07ca5b`  |
| 656    | No file              | `ad1aac07ca5b`  |
| 652    | No file              | `ad1aac07ca5b`  |
| 643    | No file              | `ad1aac07ca5b`  |
| 637    | No file              | `ad1aac07ca5b`  |
| 630    | No file              | `ad1aac07ca5b`  |
| 627    | No file              | `ad1aac07ca5b`  |
| 621    | No file              | `ad1aac07ca5b`  |
| 617    | No file              | `ad1aac07ca5b`  |
| 615    | No file              | `ad1aac07ca5b`  |
| 606    | No file              | `ad1aac07ca5b`  |
| 599    | No file              | `ad1aac07ca5b`  |
| 592    | No file              | `ad1aac07ca5b`  |
| 586    | No file              | `ad1aac07ca5b`  |
| 577    | No file              | `ad1aac07ca5b`  |
| 569    | No file              | `ad1aac07ca5b`  |
| 561    | No file              | `ad1aac07ca5b`  |
| 554    | No file              | `ad1aac07ca5b`  |
| 542    | No file              | `ad1aac07ca5b`  |
| 532    | No file              | `ad1aac07ca5b`  |
| 531    | No file              | `ad1aac07ca5b`  |
| 526    | No file              | `ad1aac07ca5b`  |
| 521    | No file              | `ad1aac07ca5b`  |
| 517    | No file              | `ad1aac07ca5b`  |
| 510    | No file              | `ad1aac07ca5b`  |
| 508    | No file              | `ad1aac07ca5b`  |
| 504    | No file              | `ad1aac07ca5b`  |
| 497    | No file              | `ad1aac07ca5b`  |
| 491    | No file              | `ad1aac07ca5b`  |
| 485    | No file              | `ad1aac07ca5b`  |
| 478    | No file              | `ad1aac07ca5b`  |
| 472    | No file              | `ad1aac07ca5b`  |
| 466    | No file              | `ad1aac07ca5b`  |
| 457    | No file              | `ad1aac07ca5b`  |
| 452    | No file              | `ad1aac07ca5b`  |
| 449    | No file              | `ad1aac07ca5b`  |
| 435    | No file              | `ad1aac07ca5b`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                     |
| --------------------------------- | -------- | -------------------------------------------------------- |
| `itemimprovementoffset.dbss`      | Optional | `key -> (data_offset, data_size)` index, see below; the handler walks the records without it |
| `itemimprovementsource.dbss`      | Optional | The reform stones, see [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md) |

Item names come from LOC type 0 and icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type           | Field   | Notes                                                       |
| ------- | -------------- | ------- | ----------------------------------------------------------- |
| `+0x00` | u32            | count   | Number of records; `3,904` on client 3464                   |
| `+0x04` | Record[count]  | records | Back to back to the end of the file; see Record             |

### Record (variable: 25 bytes + item IDs)

| Offset           | Type             | Field          | Notes                                                    |
| ---------------- | ---------------- | -------------- | -------------------------------------------------------- |
| `+0x00`          | u32              | key            | Record key, `1` to `4,949` with gaps; the index's `data_offset` points past it |
| `+0x04`          | u64              | item_count     | `5` or `1`                                               |
| `+0x0C`          | u32[item_count]  | item_ids       | `item_count` item IDs, see below                         |
| `item_ids+0x00`  | u8               | unknown_tail_0 | `0` in every record                                      |
| `item_ids+0x01`  | u8               | group          | Reform group, `1` to `37`; matches `group` of the stones |
| `item_ids+0x02`  | bytes[11]        | unknown_tail_2 | All `0` in every record                                  |

With 5 items, `item_ids[0]` is the result and `item_ids[1]` to `[4]` the input
gear, the same ID four times in all 3,816 such records (client 3464).
Kharazad Necklace (`11697`) to Dawnbound Kharazad Necklace (`11698`) is
stored as `[11698, 11697, 11697, 11697, 11697]`, and Kutum Clavis (`743327`)
to Earthshaking Kutum Clavis (`737423`) as `[737423, 743327 x4]`. The 88
records with 1 item hold 87 Tuvala items, mostly in groups 3, 4 and 5 (Tuvala
Clavis `695190` in groups 4 and 5); see Open Questions.

An item can be the input of several records with different groups and
results; 1,528 items are a result in one record and an input in another.

### `itemimprovementoffset.dbss`

| Offset  | Type             | Field | Notes                                      |
| ------- | ---------------- | ----- | ------------------------------------------ |
| `+0x00` | u32              | count | Equals the `itemimprovement.dbss` count    |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row        |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | key         | Record key                              |
| `+0x04` | u32  | data_offset | Record start + 4, past `key`            |
| `+0x08` | u32  | data_size   | Record size - 4: `41` or `25`           |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The rows
are not in file order; on client 3464 every row matches the record walked
from the start of the file.

## Layout 1

Client 1784 records end in 3 bytes after `group`, where client 3473 has 11.
Only the Record differs from Layout 2.

### Record (variable: 17 bytes + item IDs)

| Offset          | Type            | Field          | Notes                                       |
| --------------- | --------------- | -------------- | ------------------------------------------- |
| `+0x00`         | u32             | key            |                                             |
| `+0x04`         | u64             | item_count     | `5` in all 2,081 records on client 1784     |
| `+0x0C`         | u32[item_count] | item_ids       |                                             |
| `item_ids+0x00` | u8              | unknown_tail_0 |                                             |
| `item_ids+0x01` | u8              | group          |                                             |
| `item_ids+0x02` | bytes[3]        | unknown_tail_2 | All `0` in every record (client 1784)       |

## Notes

- The window is `panel_improvement_all` (`Panel_Window_Improvement_All`). It
  lists gear whose item static status says `isImprovable()`, and stones that
  `getImproveInformation():checkIsValidSubItem(slot)` accepts; both checks run
  in the client, so the Lua does not show how a stone is matched to gear.
- The window text: "You can use Reform Stones to level up gear to the next
  grade. The higher the grade of the Reform stone, the higher the chances of
  acquiring higher grade gear." (`LUA_IMPROVEMENT_DESC_RENEW`).
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  (`internal/tables/itemimprovement.go`) reads the record body as `u32 disc`,
  `u32 0`, result, four bases, a `flag` that is "always N x 256" and 9 zero
  bytes, and drops the 25-byte records. Its `disc` and `0` are the u64
  `item_count` (`5` or `1`, the number of IDs that follow), and its `flag` is
  `group` read as a u32 from one byte early: `0x2100` is group `33`.

## Open Questions

### Which Stone a Record Takes

Several stones share a `group`; they differ in `category` (see
[`itemimprovementsource.dbss`](itemimprovementsource_dbss.md)). Mapping the
input gear's `itemenchant.dbss` `category` byte (`+0x05`) to a stone category,
`1` and `2` (weapons) to `1`, `3` (armor) to `2`, `4` (accessories) to `3` and
`0` (alchemy stones) to `4`, every one of the 3,904 records (client 3464) has
a stone with its group and that category, and the names agree: Behelit's
Heart (`761877`, group 3) meets Crimson Behelit Alchemy Stone Appearance
(category 4, group 3). Whether the client matches by this pair, and what
stone category `5` (Flawless Herald's Crystal) takes, is open.

### Records With One Item

The 88 records with one item ID name Tuvala gear and no result. Groups 3, 4
and 5 are also the groups of the `[Season] Tuvala ... Conversion Stone`
items, so these may be conversions whose result is not one fixed item. What
the client does with them is open.

### The 13-Byte Tail

Only byte `+1` (`group`) is ever non-zero.
