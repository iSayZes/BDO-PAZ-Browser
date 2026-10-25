# `petaction.dbss` Format

## Purpose

Defines pet action records keyed by action ID. Each record stores the Korean action name and a UTF-16 icon path for a pet command/reaction such as Like, Feed, Angry, Sleepy, Jump, Sit, Play, Bark, or Dislike. Companion `petactionoffset.dbss` provides the record count and keyed offsets.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records          | Row bytes                  |
| ------ | -------------- | ---------------------- | ----- | ---------------- | -------------------------- |
| 1      | 1346 and later | `petaction.dbss`       | 1,498 | 10 Record        | 146 to 154, 150 on average |
| 1      | 1346 and later | `petactionoffset.dbss` | 124   | 10 Offset Record | 12                         |

| Layout | File                   | Known           | Unknown       |
| ------ | ---------------------- | --------------- | ------------- |
| 1      | `petaction.dbss`       | 1,298 B (86.6%) | 200 B (13.4%) |
| 1      | `petactionoffset.dbss` | 124 B (100.0%)  | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `2881c58c3fdf`  |
| 3482   | Layout 1             | `2881c58c3fdf`  |
| 3474   | Layout 1             | `2881c58c3fdf`  |
| 3473   | Layout 1             | `2881c58c3fdf`  |
| 3464   | Layout 1             | `2881c58c3fdf`  |
| 3458   | Layout 1             | `2881c58c3fdf`  |
| 3454   | Layout 1             | `2881c58c3fdf`  |
| 3444   | Layout 1             | `2881c58c3fdf`  |
| 3435   | Layout 1             | `2881c58c3fdf`  |
| 3426   | Layout 1             | `2881c58c3fdf`  |
| 3418   | Layout 1             | `2881c58c3fdf`  |
| 3412   | Layout 1             | `2881c58c3fdf`  |
| 3402   | Layout 1             | `2881c58c3fdf`  |
| 3396   | Layout 1             | `2881c58c3fdf`  |
| 3387   | Layout 1             | `2881c58c3fdf`  |
| 3381   | Layout 1             | `2881c58c3fdf`  |
| 3373   | Layout 1             | `2881c58c3fdf`  |
| 3364   | Layout 1             | `2881c58c3fdf`  |
| 3356   | Layout 1             | `2881c58c3fdf`  |
| 3349   | Layout 1             | `2881c58c3fdf`  |
| 3342   | Layout 1             | `2881c58c3fdf`  |
| 3335   | Layout 1             | `2881c58c3fdf`  |
| 3326   | Layout 1             | `2881c58c3fdf`  |
| 3321   | Layout 1             | `2881c58c3fdf`  |
| 3314   | Layout 1             | `2881c58c3fdf`  |
| 3303   | Layout 1             | `2881c58c3fdf`  |
| 3302   | Layout 1             | `2881c58c3fdf`  |
| 3293   | Layout 1             | `2881c58c3fdf`  |
| 3283   | Layout 1             | `2881c58c3fdf`  |
| 3275   | Layout 1             | `2881c58c3fdf`  |
| 3267   | Layout 1             | `2881c58c3fdf`  |
| 3258   | Layout 1             | `2881c58c3fdf`  |
| 3251   | Layout 1             | `2881c58c3fdf`  |
| 3242   | Layout 1             | `2881c58c3fdf`  |
| 3235   | Layout 1             | `2881c58c3fdf`  |
| 3229   | Layout 1             | `2881c58c3fdf`  |
| 3212   | Layout 1             | `2881c58c3fdf`  |
| 3203   | Layout 1             | `2881c58c3fdf`  |
| 3193   | Layout 1             | `2881c58c3fdf`  |
| 3186   | Layout 1             | `2881c58c3fdf`  |
| 3177   | Layout 1             | `2881c58c3fdf`  |
| 3169   | Layout 1             | `2881c58c3fdf`  |
| 3158   | Layout 1             | `2881c58c3fdf`  |
| 3151   | Layout 1             | `2881c58c3fdf`  |
| 3144   | Layout 1             | `2881c58c3fdf`  |
| 3133   | Layout 1             | `2881c58c3fdf`  |
| 3125   | Layout 1             | `2881c58c3fdf`  |
| 3118   | Layout 1             | `2881c58c3fdf`  |
| 3111   | Layout 1             | `2881c58c3fdf`  |
| 3103   | Layout 1             | `2881c58c3fdf`  |
| 3095   | Layout 1             | `2881c58c3fdf`  |
| 3086   | Layout 1             | `2881c58c3fdf`  |
| 3072   | Layout 1             | `2881c58c3fdf`  |
| 3062   | Layout 1             | `2881c58c3fdf`  |
| 3052   | Layout 1             | `2881c58c3fdf`  |
| 3045   | Layout 1             | `2881c58c3fdf`  |
| 3037   | Layout 1             | `2881c58c3fdf`  |
| 3030   | Layout 1             | `2881c58c3fdf`  |
| 3021   | Layout 1             | `2881c58c3fdf`  |
| 3012   | Layout 1             | `2881c58c3fdf`  |
| 3002   | Layout 1             | `2881c58c3fdf`  |
| 2995   | Layout 1             | `2881c58c3fdf`  |
| 2987   | Layout 1             | `2881c58c3fdf`  |
| 2978   | Layout 1             | `2881c58c3fdf`  |
| 2970   | Layout 1             | `2881c58c3fdf`  |
| 2959   | Layout 1             | `2881c58c3fdf`  |
| 2951   | Layout 1             | `2881c58c3fdf`  |
| 2942   | Layout 1             | `2881c58c3fdf`  |
| 2935   | Layout 1             | `2881c58c3fdf`  |
| 2932   | Layout 1             | `2881c58c3fdf`  |
| 2923   | Layout 1             | `2881c58c3fdf`  |
| 2919   | Layout 1             | `2881c58c3fdf`  |
| 2907   | Layout 1             | `2881c58c3fdf`  |
| 2900   | Layout 1             | `2881c58c3fdf`  |
| 2891   | Layout 1             | `2881c58c3fdf`  |
| 2882   | Layout 1             | `2881c58c3fdf`  |
| 2872   | Layout 1             | `2881c58c3fdf`  |
| 2863   | Layout 1             | `2881c58c3fdf`  |
| 2855   | Layout 1             | `2881c58c3fdf`  |
| 2849   | Layout 1             | `2881c58c3fdf`  |
| 2844   | Layout 1             | `2881c58c3fdf`  |
| 2834   | Layout 1             | `2881c58c3fdf`  |
| 2825   | Layout 1             | `2881c58c3fdf`  |
| 2819   | Layout 1             | `2881c58c3fdf`  |
| 2811   | Layout 1             | `2881c58c3fdf`  |
| 2803   | Layout 1             | `2881c58c3fdf`  |
| 2794   | Layout 1             | `2881c58c3fdf`  |
| 2783   | Layout 1             | `2881c58c3fdf`  |
| 2774   | Layout 1             | `2881c58c3fdf`  |
| 2765   | Layout 1             | `2881c58c3fdf`  |
| 2756   | Layout 1             | `2881c58c3fdf`  |
| 2750   | Layout 1             | `2881c58c3fdf`  |
| 2743   | Layout 1             | `2881c58c3fdf`  |
| 2736   | Layout 1             | `2881c58c3fdf`  |
| 2726   | Layout 1             | `2881c58c3fdf`  |
| 2717   | Layout 1             | `2881c58c3fdf`  |
| 2709   | Layout 1             | `2881c58c3fdf`  |
| 2703   | Layout 1             | `2881c58c3fdf`  |
| 2695   | Layout 1             | `2881c58c3fdf`  |
| 2684   | Layout 1             | `2881c58c3fdf`  |
| 2672   | Layout 1             | `2881c58c3fdf`  |
| 2665   | Layout 1             | `2881c58c3fdf`  |
| 2657   | Layout 1             | `2881c58c3fdf`  |
| 2649   | Layout 1             | `2881c58c3fdf`  |
| 2644   | Layout 1             | `2881c58c3fdf`  |
| 2637   | Layout 1             | `2881c58c3fdf`  |
| 2629   | Layout 1             | `2881c58c3fdf`  |
| 2619   | Layout 1             | `2881c58c3fdf`  |
| 2612   | Layout 1             | `2881c58c3fdf`  |
| 2606   | Layout 1             | `2881c58c3fdf`  |
| 2602   | Layout 1             | `2881c58c3fdf`  |
| 2601   | Layout 1             | `2881c58c3fdf`  |
| 2592   | Layout 1             | `2881c58c3fdf`  |
| 2583   | Layout 1             | `2881c58c3fdf`  |
| 2575   | Layout 1             | `2881c58c3fdf`  |
| 2567   | Layout 1             | `2881c58c3fdf`  |
| 2560   | Layout 1             | `2881c58c3fdf`  |
| 2553   | Layout 1             | `2881c58c3fdf`  |
| 2545   | Layout 1             | `2881c58c3fdf`  |
| 2538   | Layout 1             | `2881c58c3fdf`  |
| 2529   | Layout 1             | `2881c58c3fdf`  |
| 2519   | Layout 1             | `2881c58c3fdf`  |
| 2513   | Layout 1             | `2881c58c3fdf`  |
| 2510   | Layout 1             | `2881c58c3fdf`  |
| 2507   | Layout 1             | `2881c58c3fdf`  |
| 2503   | Layout 1             | `2881c58c3fdf`  |
| 2498   | Layout 1             | `2881c58c3fdf`  |
| 2492   | Layout 1             | `2881c58c3fdf`  |
| 2487   | Layout 1             | `2881c58c3fdf`  |
| 2480   | Layout 1             | `2881c58c3fdf`  |
| 2474   | Layout 1             | `2881c58c3fdf`  |
| 2468   | Layout 1             | `2881c58c3fdf`  |
| 2460   | Layout 1             | `2881c58c3fdf`  |
| 2453   | Layout 1             | `2881c58c3fdf`  |
| 2444   | Layout 1             | `2881c58c3fdf`  |
| 2438   | Layout 1             | `2881c58c3fdf`  |
| 2434   | Layout 1             | `2881c58c3fdf`  |
| 2429   | Layout 1             | `2881c58c3fdf`  |
| 2421   | Layout 1             | `2881c58c3fdf`  |
| 2414   | Layout 1             | `2881c58c3fdf`  |
| 2407   | Layout 1             | `2881c58c3fdf`  |
| 2401   | Layout 1             | `2881c58c3fdf`  |
| 2397   | Layout 1             | `2881c58c3fdf`  |
| 2393   | Layout 1             | `2881c58c3fdf`  |
| 2384   | Layout 1             | `2881c58c3fdf`  |
| 2378   | Layout 1             | `2881c58c3fdf`  |
| 2372   | Layout 1             | `2881c58c3fdf`  |
| 2358   | Layout 1             | `2881c58c3fdf`  |
| 2352   | Layout 1             | `2881c58c3fdf`  |
| 2347   | Layout 1             | `2881c58c3fdf`  |
| 2343   | Layout 1             | `2881c58c3fdf`  |
| 2335   | Layout 1             | `2881c58c3fdf`  |
| 2327   | Layout 1             | `2881c58c3fdf`  |
| 2324   | Layout 1             | `2881c58c3fdf`  |
| 2319   | Layout 1             | `2881c58c3fdf`  |
| 2313   | Layout 1             | `2881c58c3fdf`  |
| 2308   | Layout 1             | `2881c58c3fdf`  |
| 2302   | Layout 1             | `2881c58c3fdf`  |
| 2295   | Layout 1             | `2881c58c3fdf`  |
| 2290   | Layout 1             | `2881c58c3fdf`  |
| 2284   | Layout 1             | `2881c58c3fdf`  |
| 2276   | Layout 1             | `2881c58c3fdf`  |
| 2269   | Layout 1             | `2881c58c3fdf`  |
| 2259   | Layout 1             | `2881c58c3fdf`  |
| 2250   | Layout 1             | `2881c58c3fdf`  |
| 2243   | Layout 1             | `2881c58c3fdf`  |
| 2235   | Layout 1             | `2881c58c3fdf`  |
| 2229   | Layout 1             | `2881c58c3fdf`  |
| 2224   | Layout 1             | `2881c58c3fdf`  |
| 2218   | Layout 1             | `2881c58c3fdf`  |
| 2215   | Layout 1             | `2881c58c3fdf`  |
| 2207   | Layout 1             | `2881c58c3fdf`  |
| 2203   | Layout 1             | `2881c58c3fdf`  |
| 2196   | Layout 1             | `2881c58c3fdf`  |
| 2192   | Layout 1             | `2881c58c3fdf`  |
| 2189   | Layout 1             | `2881c58c3fdf`  |
| 2183   | Layout 1             | `2881c58c3fdf`  |
| 2179   | Layout 1             | `2881c58c3fdf`  |
| 2171   | Layout 1             | `2881c58c3fdf`  |
| 2163   | Layout 1             | `2881c58c3fdf`  |
| 2156   | Layout 1             | `2881c58c3fdf`  |
| 2151   | Layout 1             | `2881c58c3fdf`  |
| 2147   | Layout 1             | `2881c58c3fdf`  |
| 2142   | Layout 1             | `2881c58c3fdf`  |
| 2138   | Layout 1             | `2881c58c3fdf`  |
| 2134   | Layout 1             | `2881c58c3fdf`  |
| 2130   | Layout 1             | `2881c58c3fdf`  |
| 2122   | Layout 1             | `2881c58c3fdf`  |
| 2107   | Layout 1             | `2881c58c3fdf`  |
| 2098   | Layout 1             | `2881c58c3fdf`  |
| 2089   | Layout 1             | `2881c58c3fdf`  |
| 2081   | Layout 1             | `2881c58c3fdf`  |
| 2073   | Layout 1             | `2881c58c3fdf`  |
| 2067   | Layout 1             | `2881c58c3fdf`  |
| 2063   | Layout 1             | `2881c58c3fdf`  |
| 2059   | Layout 1             | `2881c58c3fdf`  |
| 2052   | Layout 1             | `2881c58c3fdf`  |
| 2044   | Layout 1             | `2881c58c3fdf`  |
| 2039   | Layout 1             | `2881c58c3fdf`  |
| 2032   | Layout 1             | `2881c58c3fdf`  |
| 2025   | Layout 1             | `2881c58c3fdf`  |
| 2011   | Layout 1             | `2881c58c3fdf`  |
| 2005   | Layout 1             | `2881c58c3fdf`  |
| 2000   | Layout 1             | `2881c58c3fdf`  |
| 1996   | Layout 1             | `2881c58c3fdf`  |
| 1991   | Layout 1             | `2881c58c3fdf`  |
| 1985   | Layout 1             | `2881c58c3fdf`  |
| 1980   | Layout 1             | `2881c58c3fdf`  |
| 1969   | Layout 1             | `2881c58c3fdf`  |
| 1964   | Layout 1             | `2881c58c3fdf`  |
| 1958   | Layout 1             | `2881c58c3fdf`  |
| 1950   | Layout 1             | `2881c58c3fdf`  |
| 1945   | Layout 1             | `2881c58c3fdf`  |
| 1937   | Layout 1             | `2881c58c3fdf`  |
| 1933   | Layout 1             | `2881c58c3fdf`  |
| 1927   | Layout 1             | `2881c58c3fdf`  |
| 1921   | Layout 1             | `2881c58c3fdf`  |
| 1914   | Layout 1             | `2881c58c3fdf`  |
| 1908   | Layout 1             | `2881c58c3fdf`  |
| 1897   | Layout 1             | `2881c58c3fdf`  |
| 1892   | Layout 1             | `2881c58c3fdf`  |
| 1886   | Layout 1             | `2881c58c3fdf`  |
| 1881   | Layout 1             | `2881c58c3fdf`  |
| 1871   | Layout 1             | `2881c58c3fdf`  |
| 1866   | Layout 1             | `2881c58c3fdf`  |
| 1862   | Layout 1             | `2881c58c3fdf`  |
| 1854   | Layout 1             | `2881c58c3fdf`  |
| 1846   | Layout 1             | `2881c58c3fdf`  |
| 1838   | Layout 1             | `2881c58c3fdf`  |
| 1832   | Layout 1             | `2881c58c3fdf`  |
| 1826   | Layout 1             | `2881c58c3fdf`  |
| 1822   | Layout 1             | `2881c58c3fdf`  |
| 1818   | Layout 1             | `2881c58c3fdf`  |
| 1804   | Layout 1             | `2881c58c3fdf`  |
| 1794   | Layout 1             | `2881c58c3fdf`  |
| 1790   | Layout 1             | `2881c58c3fdf`  |
| 1784   | Layout 1             | `2881c58c3fdf`  |
| 1774   | Layout 1             | `2881c58c3fdf`  |
| 1771   | Layout 1             | `2881c58c3fdf`  |
| 1762   | Layout 1             | `2881c58c3fdf`  |
| 1759   | Layout 1             | `2881c58c3fdf`  |
| 1754   | Layout 1             | `2881c58c3fdf`  |
| 1749   | Layout 1             | `2881c58c3fdf`  |
| 1743   | Layout 1             | `2881c58c3fdf`  |
| 1737   | Layout 1             | `2881c58c3fdf`  |
| 1731   | Layout 1             | `2881c58c3fdf`  |
| 1725   | Layout 1             | `2881c58c3fdf`  |
| 1717   | Layout 1             | `2881c58c3fdf`  |
| 1710   | Layout 1             | `2881c58c3fdf`  |
| 1704   | Layout 1             | `2881c58c3fdf`  |
| 1698   | Layout 1             | `2881c58c3fdf`  |
| 1690   | Layout 1             | `2881c58c3fdf`  |
| 1685   | Layout 1             | `2881c58c3fdf`  |
| 1680   | Layout 1             | `2881c58c3fdf`  |
| 1674   | Layout 1             | `2881c58c3fdf`  |
| 1668   | Layout 1             | `2881c58c3fdf`  |
| 1659   | Layout 1             | `2881c58c3fdf`  |
| 1649   | Layout 1             | `2881c58c3fdf`  |
| 1642   | Layout 1             | `2881c58c3fdf`  |
| 1636   | Layout 1             | `2881c58c3fdf`  |
| 1628   | Layout 1             | `2881c58c3fdf`  |
| 1622   | Layout 1             | `2881c58c3fdf`  |
| 1614   | Layout 1             | `2881c58c3fdf`  |
| 1608   | Layout 1             | `2881c58c3fdf`  |
| 1602   | Layout 1             | `2881c58c3fdf`  |
| 1598   | Layout 1             | `2881c58c3fdf`  |
| 1594   | Layout 1             | `2881c58c3fdf`  |
| 1590   | Layout 1             | `2881c58c3fdf`  |
| 1587   | Layout 1             | `2881c58c3fdf`  |
| 1584   | Layout 1             | `2881c58c3fdf`  |
| 1579   | Layout 1             | `2881c58c3fdf`  |
| 1572   | Layout 1             | `2881c58c3fdf`  |
| 1565   | Layout 1             | `2881c58c3fdf`  |
| 1559   | Layout 1             | `2881c58c3fdf`  |
| 1554   | Layout 1             | `2881c58c3fdf`  |
| 1547   | Layout 1             | `2881c58c3fdf`  |
| 1537   | Layout 1             | `2881c58c3fdf`  |
| 1529   | Layout 1             | `2881c58c3fdf`  |
| 1524   | Layout 1             | `2881c58c3fdf`  |
| 1519   | Layout 1             | `2881c58c3fdf`  |
| 1509   | Layout 1             | `2881c58c3fdf`  |
| 1506   | Layout 1             | `2881c58c3fdf`  |
| 1504   | Layout 1             | `2881c58c3fdf`  |
| 1500   | Layout 1             | `2881c58c3fdf`  |
| 1493   | Layout 1             | `2881c58c3fdf`  |
| 1489   | Layout 1             | `2881c58c3fdf`  |
| 1485   | Layout 1             | `2881c58c3fdf`  |
| 1481   | Layout 1             | `2881c58c3fdf`  |
| 1474   | Layout 1             | `2881c58c3fdf`  |
| 1466   | Layout 1             | `2881c58c3fdf`  |
| 1462   | Layout 1             | `2881c58c3fdf`  |
| 1459   | Layout 1             | `2881c58c3fdf`  |
| 1453   | Layout 1             | `2881c58c3fdf`  |
| 1450   | Layout 1             | `2881c58c3fdf`  |
| 1445   | Layout 1             | `2881c58c3fdf`  |
| 1439   | Layout 1             | `2881c58c3fdf`  |
| 1433   | Layout 1             | `2881c58c3fdf`  |
| 1430   | Layout 1             | `2881c58c3fdf`  |
| 1426   | Layout 1             | `2881c58c3fdf`  |
| 1421   | Layout 1             | `2881c58c3fdf`  |
| 1417   | Layout 1             | `2881c58c3fdf`  |
| 1416   | Layout 1             | `2881c58c3fdf`  |
| 1409   | Layout 1             | `2881c58c3fdf`  |
| 1405   | Layout 1             | `2881c58c3fdf`  |
| 1401   | Layout 1             | `2881c58c3fdf`  |
| 1396   | Layout 1             | `2881c58c3fdf`  |
| 1391   | Layout 1             | `2881c58c3fdf`  |
| 1390   | Layout 1             | `2881c58c3fdf`  |
| 1386   | Layout 1             | `2881c58c3fdf`  |
| 1381   | Layout 1             | `2881c58c3fdf`  |
| 1379   | Layout 1             | `2881c58c3fdf`  |
| 1372   | Layout 1             | `2881c58c3fdf`  |
| 1366   | Layout 1             | `2881c58c3fdf`  |
| 1364   | Layout 1             | `2881c58c3fdf`  |
| 1363   | Layout 1             | `2881c58c3fdf`  |
| 1360   | Layout 1             | `2881c58c3fdf`  |
| 1358   | Layout 1             | `2881c58c3fdf`  |
| 1355   | Layout 1             | `2881c58c3fdf`  |
| 1351   | Layout 1             | `2881c58c3fdf`  |
| 1348   | Layout 1             | `2881c58c3fdf`  |
| 1346   | Layout 1             | `2881c58c3fdf`  |
| 1341   | No documented layout | `2881c58c3fdf`  |
| 1340   | No documented layout | `2881c58c3fdf`  |
| 1338   | No documented layout | `2881c58c3fdf`  |
| 1335   | No documented layout | `2881c58c3fdf`  |
| 1333   | No documented layout | `2881c58c3fdf`  |
| 1329   | No documented layout | `2881c58c3fdf`  |
| 1327   | No documented layout | `2881c58c3fdf`  |
| 1324   | No documented layout | `2881c58c3fdf`  |
| 1321   | No documented layout | `2881c58c3fdf`  |
| 1319   | No documented layout | `2881c58c3fdf`  |
| 1318   | No documented layout | `2881c58c3fdf`  |
| 1316   | No documented layout | `2881c58c3fdf`  |
| 1313   | No documented layout | `2881c58c3fdf`  |
| 1311   | No documented layout | `2881c58c3fdf`  |
| 1309   | No documented layout | `2881c58c3fdf`  |
| 1304   | No documented layout | `2881c58c3fdf`  |
| 1292   | No documented layout | `2881c58c3fdf`  |
| 1286   | No documented layout | `2881c58c3fdf`  |
| 1280   | No file              | `2881c58c3fdf`  |
| 1276   | No file              | `2881c58c3fdf`  |
| 1267   | No documented layout | `2881c58c3fdf`  |
| 1261   | No documented layout | `2881c58c3fdf`  |
| 1256   | No file              | `2881c58c3fdf`  |
| 1250   | No file              | `2881c58c3fdf`  |
| 1246   | No file              | `2881c58c3fdf`  |
| 1239   | No file              | `2881c58c3fdf`  |
| 1230   | No file              | `2881c58c3fdf`  |
| 1226   | No file              | `2881c58c3fdf`  |
| 1220   | No file              | `2881c58c3fdf`  |
| 1217   | No file              | `2881c58c3fdf`  |
| 1211   | No file              | `2881c58c3fdf`  |
| 1210   | No file              | `2881c58c3fdf`  |
| 1208   | No file              | `2881c58c3fdf`  |
| 1203   | No file              | `2881c58c3fdf`  |
| 1197   | No file              | `2881c58c3fdf`  |
| 1194   | No file              | `2881c58c3fdf`  |
| 1192   | No file              | `2881c58c3fdf`  |
| 1187   | No file              | `2881c58c3fdf`  |
| 1183   | No file              | `2881c58c3fdf`  |
| 1177   | No file              | `2881c58c3fdf`  |
| 1173   | No file              | `2881c58c3fdf`  |
| 1167   | No file              | `2881c58c3fdf`  |
| 1164   | No file              | `2881c58c3fdf`  |
| 1156   | No file              | `2881c58c3fdf`  |
| 1149   | No file              | `2881c58c3fdf`  |
| 1144   | No file              | `2881c58c3fdf`  |
| 1137   | No file              | `2881c58c3fdf`  |
| 1132   | No file              | `2881c58c3fdf`  |
| 1127   | No file              | `2881c58c3fdf`  |
| 1122   | No file              | `2881c58c3fdf`  |
| 1118   | No file              | `2881c58c3fdf`  |
| 1114   | No file              | `2881c58c3fdf`  |
| 1109   | No file              | `2881c58c3fdf`  |
| 1102   | No file              | `2881c58c3fdf`  |
| 1096   | No file              | `2881c58c3fdf`  |
| 1088   | No file              | `2881c58c3fdf`  |
| 1081   | No file              | `2881c58c3fdf`  |
| 1076   | No file              | `2881c58c3fdf`  |
| 1069   | No file              | `2881c58c3fdf`  |
| 1064   | No file              | `2881c58c3fdf`  |
| 1058   | No file              | `2881c58c3fdf`  |
| 1051   | No file              | `2881c58c3fdf`  |
| 1044   | No file              | `2881c58c3fdf`  |
| 1036   | No file              | `2881c58c3fdf`  |
| 1026   | No file              | `2881c58c3fdf`  |
| 1016   | No file              | `2881c58c3fdf`  |
| 1009   | No file              | `2881c58c3fdf`  |
| 1005   | No file              | `2881c58c3fdf`  |
| 1000   | No file              | `2881c58c3fdf`  |
| 998    | No file              | `2881c58c3fdf`  |
| 990    | No file              | `2881c58c3fdf`  |
| 979    | No file              | `2881c58c3fdf`  |
| 972    | No file              | `2881c58c3fdf`  |
| 963    | No file              | `2881c58c3fdf`  |
| 955    | No file              | `2881c58c3fdf`  |
| 946    | No file              | `2881c58c3fdf`  |
| 938    | No file              | `2881c58c3fdf`  |
| 927    | No file              | `2881c58c3fdf`  |
| 911    | No file              | `2881c58c3fdf`  |
| 904    | No file              | `2881c58c3fdf`  |
| 899    | No file              | `2881c58c3fdf`  |
| 894    | No file              | `2881c58c3fdf`  |
| 885    | No file              | `2881c58c3fdf`  |
| 879    | No file              | `2881c58c3fdf`  |
| 872    | No file              | `2881c58c3fdf`  |
| 864    | No file              | `2881c58c3fdf`  |
| 855    | No file              | `2881c58c3fdf`  |
| 853    | No file              | `2881c58c3fdf`  |
| 845    | No file              | `2881c58c3fdf`  |
| 837    | No file              | `2881c58c3fdf`  |
| 829    | No file              | `2881c58c3fdf`  |
| 822    | No file              | `2881c58c3fdf`  |
| 814    | No file              | `2881c58c3fdf`  |
| 805    | No file              | `2881c58c3fdf`  |
| 794    | No file              | `2881c58c3fdf`  |
| 787    | No file              | `2881c58c3fdf`  |
| 780    | No file              | `2881c58c3fdf`  |
| 771    | No file              | `2881c58c3fdf`  |
| 760    | No file              | `2881c58c3fdf`  |
| 748    | No file              | `2881c58c3fdf`  |
| 741    | No file              | `2881c58c3fdf`  |
| 736    | No file              | `2881c58c3fdf`  |
| 731    | No file              | `2881c58c3fdf`  |
| 723    | No file              | `2881c58c3fdf`  |
| 711    | No file              | `2881c58c3fdf`  |
| 707    | No file              | `2881c58c3fdf`  |
| 697    | No file              | `2881c58c3fdf`  |
| 689    | No file              | `2881c58c3fdf`  |
| 683    | No file              | `2881c58c3fdf`  |
| 678    | No file              | `2881c58c3fdf`  |
| 670    | No file              | `2881c58c3fdf`  |
| 661    | No file              | `2881c58c3fdf`  |
| 656    | No file              | `2881c58c3fdf`  |
| 652    | No file              | `2881c58c3fdf`  |
| 643    | No file              | `2881c58c3fdf`  |
| 637    | No file              | `2881c58c3fdf`  |
| 630    | No file              | `2881c58c3fdf`  |
| 627    | No file              | `2881c58c3fdf`  |
| 621    | No file              | `2881c58c3fdf`  |
| 617    | No file              | `2881c58c3fdf`  |
| 615    | No file              | `2881c58c3fdf`  |
| 606    | No file              | `2881c58c3fdf`  |
| 599    | No file              | `2881c58c3fdf`  |
| 592    | No file              | `2881c58c3fdf`  |
| 586    | No file              | `2881c58c3fdf`  |
| 577    | No file              | `2881c58c3fdf`  |
| 569    | No file              | `2881c58c3fdf`  |
| 561    | No file              | `2881c58c3fdf`  |
| 554    | No file              | `2881c58c3fdf`  |
| 542    | No file              | `2881c58c3fdf`  |
| 532    | No file              | `2881c58c3fdf`  |
| 531    | No file              | `2881c58c3fdf`  |
| 526    | No file              | `2881c58c3fdf`  |
| 521    | No file              | `2881c58c3fdf`  |
| 517    | No file              | `2881c58c3fdf`  |
| 510    | No file              | `2881c58c3fdf`  |
| 508    | No file              | `2881c58c3fdf`  |
| 504    | No file              | `2881c58c3fdf`  |
| 497    | No file              | `2881c58c3fdf`  |
| 491    | No file              | `2881c58c3fdf`  |
| 485    | No file              | `2881c58c3fdf`  |
| 478    | No file              | `2881c58c3fdf`  |
| 472    | No file              | `2881c58c3fdf`  |
| 466    | No file              | `2881c58c3fdf`  |
| 457    | No file              | `2881c58c3fdf`  |
| 452    | No file              | `2881c58c3fdf`  |
| 449    | No file              | `2881c58c3fdf`  |
| 435    | No file              | `2881c58c3fdf`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                               |
| ---------------------- | -------- | -------------------------------------------------- |
| `petactionoffset.dbss` | Required | `action_id -> (record_offset, record_size)` lookup |
| `languagedata_en.loc`  | Optional | English action names via LOC type 19               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

`petaction.dbss` has no standalone header or record count. Records start at byte `0x0000`; use `petactionoffset.dbss` to enumerate them.

| Offset  | Type          | Field   | Notes                                         |
| ------- | ------------- | ------- | --------------------------------------------- |
| `+0x00` | Record[..end] | records | Variable-size record stream; observed 10 rows |

### Record (variable: 44 bytes + name and icon text)

Records are variable size because both strings are. Observed records are 146-154 bytes. Offsets are relative to `record_offset` from `petactionoffset.dbss`.

| Offset           | Type      | Field           | Notes                                                               |
| ---------------- | --------- | --------------- | ------------------------------------------------------------------- |
| `+0x00`          | u32       | action_id       | Primary key; matches offset-table key                               |
| `+0x04`          | u32       | unknown_04      | Always 0                                                            |
| `+0x08`          | u32       | unknown_08      | Always 0                                                            |
| `+0x0C`          | u32       | magic           | Always `0xDEBA1DCD`                                                 |
| `+0x10`          | str16     | name_kr         | Korean action name; the u64 counts UTF-16 code units                |
| `name_kr+0x00`   | str16     | icon_path       | Icon path; no null terminator                                       |
| `icon_path+0x00` | bytes[12] | unknown_tail_00 | Always 12 zero bytes; the record ends exactly after them            |

Both strings use the u64 length prefix read by `read_prefixed_at` in `_common/prefixed_string.py`.

Earlier versions of this doc read the `name_kr` length as a u32 `action_group` (2, or 4 for action 7) and the name's UTF-16 code units as one or two `icon_hash` values (`0xC068AE30` is `기쁨` read as a u32). That is why action 7, whose name `웅크리기` has four characters, looked like an "extended hash record". An earlier version of this doc also called `unknown_tail_00` `trailing_zeroes`.

### `petactionoffset.dbss`

Provides keyed lookup into `petaction.dbss` and supplies the record count.

| Offset  | Type                 | Field   | Notes                         |
| ------- | -------------------- | ------- | ----------------------------- |
| `+0x00` | u32                  | count   | Number of action records (10) |
| `+0x04` | Offset Record[count] | records | See Offset Record             |

### Offset Record (12 bytes)

| Offset  | Type | Field         | Notes                                    |
| ------- | ---- | ------------- | ---------------------------------------- |
| `+0x00` | u32  | action_id     | Key for the action/icon record           |
| `+0x04` | u32  | record_offset | Absolute byte offset in `petaction.dbss` |
| `+0x08` | u32  | record_size   | Size of the record in bytes              |

## Observed Records

| Action ID | LOC Name | Korean Name | Icon Name | Icon Path                                               |
| --------- | -------- | ----------- | --------- | ------------------------------------------------------- |
| 0         | Joy      | 기쁨        | Like      | `New_Icon/08_Servant_Skill/02_Pet/Action_0_Like.dds`    |
| 1         | Feed     | 먹이        | Feed      | `New_Icon/08_Servant_Skill/02_Pet/Action_9_Feed.dds`    |
| 2         | Angry    | 화남        | Angry     | `New_Icon/08_Servant_Skill/02_Pet/Action_2_Angry.dds`   |
| 3         | Sleepy   | 졸림        | Sleepy    | `New_Icon/08_Servant_Skill/02_Pet/Action_3_Sleepy.dds`  |
| 4         | Jump     | 점프        | Jump      | `New_Icon/08_Servant_Skill/02_Pet/Action_4_Jump.dds`    |
| 5         | Sit      | 앉기        | Sit       | `New_Icon/08_Servant_Skill/02_Pet/Action_5_Sit.dds`     |
| 6         | Play     | 장난        | Play1     | `New_Icon/08_Servant_Skill/02_Pet/Action_6_Play1.dds`   |
| 7         | Crouch   | 웅크리기    | Play2     | `New_Icon/08_Servant_Skill/02_Pet/Action_7_Play2.dds`   |
| 8         | Weep     | 울음        | Bark      | `New_Icon/08_Servant_Skill/02_Pet/Action_8_Bark.dds`    |
| 9         | Sulky    | 삐짐        | Dislike   | `New_Icon/08_Servant_Skill/02_Pet/Action_1_Dislike.dds` |

> Action ID 1 points to `Action_9_Feed.dds`, and action ID 9 points to `Action_1_Dislike.dds`. The record key order and filename number are not the same for those two actions.

The file is byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.

## Notes

- `petaction.dbss` itself starts with action ID 0, not a count. Always use `petactionoffset.dbss` to enumerate records.
- Both strings are UTF-16-LE and are not null-terminated. A fixed 12-byte zero trailer follows the icon path.
- The `magic` value `0xDEBA1DCD` appears in every record.
- Action names resolve through `languagedata_en.loc` with `str_type=19` and `str_id1=action_id`. The icon filename suffix is an asset name and does not always match the UI label.

## Open Questions

### Action ID Consumers

The action IDs are confirmed in-game to match LOC type 19 labels. The consuming pet UI or behavior table should join by `action_id`, but the exact source file is not confirmed.
