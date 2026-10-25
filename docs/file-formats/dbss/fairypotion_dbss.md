# `fairypotion.dbss` Format

## Purpose

The potions a fairy can be set to use. The file holds one item list per
potion type: list `0` is the HP potions for the fairy's HP slot, lists `1`,
`2` and `3` the potions for the MP slot of classes that use MP, WP and SP.
`fairypotionoffset.dbss` is the type-keyed index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records       | Row bytes                  |
| ------ | -------------- | ------------------------ | ----- | ------------- | -------------------------- |
| 1      | 1261 and later | `fairypotion.dbss`       | 1,200 | 4 Potion List | 257 to 313, 299 on average |
| 1      | 1261 and later | `fairypotionoffset.dbss` | 44    | 4 Offset Row  | 10                         |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `fairypotion.dbss`       | 1,200 B (100.0%) | 0 B (0.0%) |
| 1      | `fairypotionoffset.dbss` | 44 B (100.0%)    | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `0f7df7ece813`  |
| 3482   | Layout 1 | `0f7df7ece813`  |
| 3474   | Layout 1 | `0f7df7ece813`  |
| 3473   | Layout 1 | `0f7df7ece813`  |
| 3464   | Layout 1 | `0f7df7ece813`  |
| 3458   | Layout 1 | `0f7df7ece813`  |
| 3454   | Layout 1 | `0f7df7ece813`  |
| 3444   | Layout 1 | `0f7df7ece813`  |
| 3435   | Layout 1 | `0f7df7ece813`  |
| 3426   | Layout 1 | `0f7df7ece813`  |
| 3418   | Layout 1 | `0f7df7ece813`  |
| 3412   | Layout 1 | `0f7df7ece813`  |
| 3402   | Layout 1 | `0f7df7ece813`  |
| 3396   | Layout 1 | `0f7df7ece813`  |
| 3387   | Layout 1 | `0f7df7ece813`  |
| 3381   | Layout 1 | `0f7df7ece813`  |
| 3373   | Layout 1 | `0f7df7ece813`  |
| 3364   | Layout 1 | `0f7df7ece813`  |
| 3356   | Layout 1 | `0f7df7ece813`  |
| 3349   | Layout 1 | `0f7df7ece813`  |
| 3342   | Layout 1 | `0f7df7ece813`  |
| 3335   | Layout 1 | `0f7df7ece813`  |
| 3326   | Layout 1 | `0f7df7ece813`  |
| 3321   | Layout 1 | `0f7df7ece813`  |
| 3314   | Layout 1 | `0f7df7ece813`  |
| 3303   | Layout 1 | `0f7df7ece813`  |
| 3302   | Layout 1 | `0f7df7ece813`  |
| 3293   | Layout 1 | `0f7df7ece813`  |
| 3283   | Layout 1 | `0f7df7ece813`  |
| 3275   | Layout 1 | `0f7df7ece813`  |
| 3267   | Layout 1 | `0f7df7ece813`  |
| 3258   | Layout 1 | `0f7df7ece813`  |
| 3251   | Layout 1 | `0f7df7ece813`  |
| 3242   | Layout 1 | `0f7df7ece813`  |
| 3235   | Layout 1 | `0f7df7ece813`  |
| 3229   | Layout 1 | `0f7df7ece813`  |
| 3212   | Layout 1 | `0f7df7ece813`  |
| 3203   | Layout 1 | `0f7df7ece813`  |
| 3193   | Layout 1 | `0f7df7ece813`  |
| 3186   | Layout 1 | `0f7df7ece813`  |
| 3177   | Layout 1 | `0f7df7ece813`  |
| 3169   | Layout 1 | `0f7df7ece813`  |
| 3158   | Layout 1 | `0f7df7ece813`  |
| 3151   | Layout 1 | `0f7df7ece813`  |
| 3144   | Layout 1 | `0f7df7ece813`  |
| 3133   | Layout 1 | `0f7df7ece813`  |
| 3125   | Layout 1 | `0f7df7ece813`  |
| 3118   | Layout 1 | `0f7df7ece813`  |
| 3111   | Layout 1 | `0f7df7ece813`  |
| 3103   | Layout 1 | `0f7df7ece813`  |
| 3095   | Layout 1 | `0f7df7ece813`  |
| 3086   | Layout 1 | `0f7df7ece813`  |
| 3072   | Layout 1 | `0f7df7ece813`  |
| 3062   | Layout 1 | `0f7df7ece813`  |
| 3052   | Layout 1 | `0f7df7ece813`  |
| 3045   | Layout 1 | `0f7df7ece813`  |
| 3037   | Layout 1 | `0f7df7ece813`  |
| 3030   | Layout 1 | `0f7df7ece813`  |
| 3021   | Layout 1 | `0f7df7ece813`  |
| 3012   | Layout 1 | `0f7df7ece813`  |
| 3002   | Layout 1 | `0f7df7ece813`  |
| 2995   | Layout 1 | `0f7df7ece813`  |
| 2987   | Layout 1 | `0f7df7ece813`  |
| 2978   | Layout 1 | `0f7df7ece813`  |
| 2970   | Layout 1 | `0f7df7ece813`  |
| 2959   | Layout 1 | `0f7df7ece813`  |
| 2951   | Layout 1 | `0f7df7ece813`  |
| 2942   | Layout 1 | `0f7df7ece813`  |
| 2935   | Layout 1 | `0f7df7ece813`  |
| 2932   | Layout 1 | `0f7df7ece813`  |
| 2923   | Layout 1 | `0f7df7ece813`  |
| 2919   | Layout 1 | `0f7df7ece813`  |
| 2907   | Layout 1 | `0f7df7ece813`  |
| 2900   | Layout 1 | `0f7df7ece813`  |
| 2891   | Layout 1 | `0f7df7ece813`  |
| 2882   | Layout 1 | `0f7df7ece813`  |
| 2872   | Layout 1 | `0f7df7ece813`  |
| 2863   | Layout 1 | `0f7df7ece813`  |
| 2855   | Layout 1 | `0f7df7ece813`  |
| 2849   | Layout 1 | `0f7df7ece813`  |
| 2844   | Layout 1 | `0f7df7ece813`  |
| 2834   | Layout 1 | `0f7df7ece813`  |
| 2825   | Layout 1 | `0f7df7ece813`  |
| 2819   | Layout 1 | `0f7df7ece813`  |
| 2811   | Layout 1 | `0f7df7ece813`  |
| 2803   | Layout 1 | `0f7df7ece813`  |
| 2794   | Layout 1 | `0f7df7ece813`  |
| 2783   | Layout 1 | `0f7df7ece813`  |
| 2774   | Layout 1 | `0f7df7ece813`  |
| 2765   | Layout 1 | `0f7df7ece813`  |
| 2756   | Layout 1 | `0f7df7ece813`  |
| 2750   | Layout 1 | `0f7df7ece813`  |
| 2743   | Layout 1 | `0f7df7ece813`  |
| 2736   | Layout 1 | `0f7df7ece813`  |
| 2726   | Layout 1 | `0f7df7ece813`  |
| 2717   | Layout 1 | `0f7df7ece813`  |
| 2709   | Layout 1 | `0f7df7ece813`  |
| 2703   | Layout 1 | `0f7df7ece813`  |
| 2695   | Layout 1 | `0f7df7ece813`  |
| 2684   | Layout 1 | `0f7df7ece813`  |
| 2672   | Layout 1 | `0f7df7ece813`  |
| 2665   | Layout 1 | `0f7df7ece813`  |
| 2657   | Layout 1 | `0f7df7ece813`  |
| 2649   | Layout 1 | `0f7df7ece813`  |
| 2644   | Layout 1 | `0f7df7ece813`  |
| 2637   | Layout 1 | `0f7df7ece813`  |
| 2629   | Layout 1 | `0f7df7ece813`  |
| 2619   | Layout 1 | `0f7df7ece813`  |
| 2612   | Layout 1 | `0f7df7ece813`  |
| 2606   | Layout 1 | `0f7df7ece813`  |
| 2602   | Layout 1 | `0f7df7ece813`  |
| 2601   | Layout 1 | `0f7df7ece813`  |
| 2592   | Layout 1 | `0f7df7ece813`  |
| 2583   | Layout 1 | `0f7df7ece813`  |
| 2575   | Layout 1 | `0f7df7ece813`  |
| 2567   | Layout 1 | `0f7df7ece813`  |
| 2560   | Layout 1 | `0f7df7ece813`  |
| 2553   | Layout 1 | `0f7df7ece813`  |
| 2545   | Layout 1 | `0f7df7ece813`  |
| 2538   | Layout 1 | `0f7df7ece813`  |
| 2529   | Layout 1 | `0f7df7ece813`  |
| 2519   | Layout 1 | `0f7df7ece813`  |
| 2513   | Layout 1 | `0f7df7ece813`  |
| 2510   | Layout 1 | `0f7df7ece813`  |
| 2507   | Layout 1 | `0f7df7ece813`  |
| 2503   | Layout 1 | `0f7df7ece813`  |
| 2498   | Layout 1 | `0f7df7ece813`  |
| 2492   | Layout 1 | `0f7df7ece813`  |
| 2487   | Layout 1 | `0f7df7ece813`  |
| 2480   | Layout 1 | `0f7df7ece813`  |
| 2474   | Layout 1 | `0f7df7ece813`  |
| 2468   | Layout 1 | `0f7df7ece813`  |
| 2460   | Layout 1 | `0f7df7ece813`  |
| 2453   | Layout 1 | `0f7df7ece813`  |
| 2444   | Layout 1 | `0f7df7ece813`  |
| 2438   | Layout 1 | `0f7df7ece813`  |
| 2434   | Layout 1 | `0f7df7ece813`  |
| 2429   | Layout 1 | `0f7df7ece813`  |
| 2421   | Layout 1 | `0f7df7ece813`  |
| 2414   | Layout 1 | `0f7df7ece813`  |
| 2407   | Layout 1 | `0f7df7ece813`  |
| 2401   | Layout 1 | `0f7df7ece813`  |
| 2397   | Layout 1 | `0f7df7ece813`  |
| 2393   | Layout 1 | `0f7df7ece813`  |
| 2384   | Layout 1 | `0f7df7ece813`  |
| 2378   | Layout 1 | `0f7df7ece813`  |
| 2372   | Layout 1 | `0f7df7ece813`  |
| 2358   | Layout 1 | `0f7df7ece813`  |
| 2352   | Layout 1 | `0f7df7ece813`  |
| 2347   | Layout 1 | `0f7df7ece813`  |
| 2343   | Layout 1 | `0f7df7ece813`  |
| 2335   | Layout 1 | `0f7df7ece813`  |
| 2327   | Layout 1 | `0f7df7ece813`  |
| 2324   | Layout 1 | `0f7df7ece813`  |
| 2319   | Layout 1 | `0f7df7ece813`  |
| 2313   | Layout 1 | `0f7df7ece813`  |
| 2308   | Layout 1 | `0f7df7ece813`  |
| 2302   | Layout 1 | `0f7df7ece813`  |
| 2295   | Layout 1 | `0f7df7ece813`  |
| 2290   | Layout 1 | `0f7df7ece813`  |
| 2284   | Layout 1 | `0f7df7ece813`  |
| 2276   | Layout 1 | `0f7df7ece813`  |
| 2269   | Layout 1 | `0f7df7ece813`  |
| 2259   | Layout 1 | `0f7df7ece813`  |
| 2250   | Layout 1 | `0f7df7ece813`  |
| 2243   | Layout 1 | `0f7df7ece813`  |
| 2235   | Layout 1 | `0f7df7ece813`  |
| 2229   | Layout 1 | `0f7df7ece813`  |
| 2224   | Layout 1 | `0f7df7ece813`  |
| 2218   | Layout 1 | `0f7df7ece813`  |
| 2215   | Layout 1 | `0f7df7ece813`  |
| 2207   | Layout 1 | `0f7df7ece813`  |
| 2203   | Layout 1 | `0f7df7ece813`  |
| 2196   | Layout 1 | `0f7df7ece813`  |
| 2192   | Layout 1 | `0f7df7ece813`  |
| 2189   | Layout 1 | `0f7df7ece813`  |
| 2183   | Layout 1 | `0f7df7ece813`  |
| 2179   | Layout 1 | `0f7df7ece813`  |
| 2171   | Layout 1 | `0f7df7ece813`  |
| 2163   | Layout 1 | `0f7df7ece813`  |
| 2156   | Layout 1 | `0f7df7ece813`  |
| 2151   | Layout 1 | `0f7df7ece813`  |
| 2147   | Layout 1 | `0f7df7ece813`  |
| 2142   | Layout 1 | `0f7df7ece813`  |
| 2138   | Layout 1 | `0f7df7ece813`  |
| 2134   | Layout 1 | `0f7df7ece813`  |
| 2130   | Layout 1 | `0f7df7ece813`  |
| 2122   | Layout 1 | `0f7df7ece813`  |
| 2107   | Layout 1 | `0f7df7ece813`  |
| 2098   | Layout 1 | `0f7df7ece813`  |
| 2089   | Layout 1 | `0f7df7ece813`  |
| 2081   | Layout 1 | `0f7df7ece813`  |
| 2073   | Layout 1 | `0f7df7ece813`  |
| 2067   | Layout 1 | `0f7df7ece813`  |
| 2063   | Layout 1 | `0f7df7ece813`  |
| 2059   | Layout 1 | `0f7df7ece813`  |
| 2052   | Layout 1 | `0f7df7ece813`  |
| 2044   | Layout 1 | `0f7df7ece813`  |
| 2039   | Layout 1 | `0f7df7ece813`  |
| 2032   | Layout 1 | `0f7df7ece813`  |
| 2025   | Layout 1 | `0f7df7ece813`  |
| 2011   | Layout 1 | `0f7df7ece813`  |
| 2005   | Layout 1 | `0f7df7ece813`  |
| 2000   | Layout 1 | `0f7df7ece813`  |
| 1996   | Layout 1 | `0f7df7ece813`  |
| 1991   | Layout 1 | `0f7df7ece813`  |
| 1985   | Layout 1 | `0f7df7ece813`  |
| 1980   | Layout 1 | `0f7df7ece813`  |
| 1969   | Layout 1 | `0f7df7ece813`  |
| 1964   | Layout 1 | `0f7df7ece813`  |
| 1958   | Layout 1 | `0f7df7ece813`  |
| 1950   | Layout 1 | `0f7df7ece813`  |
| 1945   | Layout 1 | `0f7df7ece813`  |
| 1937   | Layout 1 | `0f7df7ece813`  |
| 1933   | Layout 1 | `0f7df7ece813`  |
| 1927   | Layout 1 | `0f7df7ece813`  |
| 1921   | Layout 1 | `0f7df7ece813`  |
| 1914   | Layout 1 | `0f7df7ece813`  |
| 1908   | Layout 1 | `0f7df7ece813`  |
| 1897   | Layout 1 | `0f7df7ece813`  |
| 1892   | Layout 1 | `0f7df7ece813`  |
| 1886   | Layout 1 | `0f7df7ece813`  |
| 1881   | Layout 1 | `0f7df7ece813`  |
| 1871   | Layout 1 | `0f7df7ece813`  |
| 1866   | Layout 1 | `0f7df7ece813`  |
| 1862   | Layout 1 | `0f7df7ece813`  |
| 1854   | Layout 1 | `0f7df7ece813`  |
| 1846   | Layout 1 | `0f7df7ece813`  |
| 1838   | Layout 1 | `0f7df7ece813`  |
| 1832   | Layout 1 | `0f7df7ece813`  |
| 1826   | Layout 1 | `0f7df7ece813`  |
| 1822   | Layout 1 | `0f7df7ece813`  |
| 1818   | Layout 1 | `0f7df7ece813`  |
| 1804   | Layout 1 | `0f7df7ece813`  |
| 1794   | Layout 1 | `0f7df7ece813`  |
| 1790   | Layout 1 | `0f7df7ece813`  |
| 1784   | Layout 1 | `0f7df7ece813`  |
| 1774   | Layout 1 | `0f7df7ece813`  |
| 1771   | Layout 1 | `0f7df7ece813`  |
| 1762   | Layout 1 | `0f7df7ece813`  |
| 1759   | Layout 1 | `0f7df7ece813`  |
| 1754   | Layout 1 | `0f7df7ece813`  |
| 1749   | Layout 1 | `0f7df7ece813`  |
| 1743   | Layout 1 | `0f7df7ece813`  |
| 1737   | Layout 1 | `0f7df7ece813`  |
| 1731   | Layout 1 | `0f7df7ece813`  |
| 1725   | Layout 1 | `0f7df7ece813`  |
| 1717   | Layout 1 | `0f7df7ece813`  |
| 1710   | Layout 1 | `0f7df7ece813`  |
| 1704   | Layout 1 | `0f7df7ece813`  |
| 1698   | Layout 1 | `0f7df7ece813`  |
| 1690   | Layout 1 | `0f7df7ece813`  |
| 1685   | Layout 1 | `0f7df7ece813`  |
| 1680   | Layout 1 | `0f7df7ece813`  |
| 1674   | Layout 1 | `0f7df7ece813`  |
| 1668   | Layout 1 | `0f7df7ece813`  |
| 1659   | Layout 1 | `0f7df7ece813`  |
| 1649   | Layout 1 | `0f7df7ece813`  |
| 1642   | Layout 1 | `0f7df7ece813`  |
| 1636   | Layout 1 | `0f7df7ece813`  |
| 1628   | Layout 1 | `0f7df7ece813`  |
| 1622   | Layout 1 | `0f7df7ece813`  |
| 1614   | Layout 1 | `0f7df7ece813`  |
| 1608   | Layout 1 | `0f7df7ece813`  |
| 1602   | Layout 1 | `0f7df7ece813`  |
| 1598   | Layout 1 | `0f7df7ece813`  |
| 1594   | Layout 1 | `0f7df7ece813`  |
| 1590   | Layout 1 | `0f7df7ece813`  |
| 1587   | Layout 1 | `0f7df7ece813`  |
| 1584   | Layout 1 | `0f7df7ece813`  |
| 1579   | Layout 1 | `0f7df7ece813`  |
| 1572   | Layout 1 | `0f7df7ece813`  |
| 1565   | Layout 1 | `0f7df7ece813`  |
| 1559   | Layout 1 | `0f7df7ece813`  |
| 1554   | Layout 1 | `0f7df7ece813`  |
| 1547   | Layout 1 | `0f7df7ece813`  |
| 1537   | Layout 1 | `0f7df7ece813`  |
| 1529   | Layout 1 | `0f7df7ece813`  |
| 1524   | Layout 1 | `0f7df7ece813`  |
| 1519   | Layout 1 | `0f7df7ece813`  |
| 1509   | Layout 1 | `0f7df7ece813`  |
| 1506   | Layout 1 | `0f7df7ece813`  |
| 1504   | Layout 1 | `0f7df7ece813`  |
| 1500   | Layout 1 | `0f7df7ece813`  |
| 1493   | Layout 1 | `0f7df7ece813`  |
| 1489   | Layout 1 | `0f7df7ece813`  |
| 1485   | Layout 1 | `0f7df7ece813`  |
| 1481   | Layout 1 | `0f7df7ece813`  |
| 1474   | Layout 1 | `0f7df7ece813`  |
| 1466   | Layout 1 | `0f7df7ece813`  |
| 1462   | Layout 1 | `0f7df7ece813`  |
| 1459   | Layout 1 | `0f7df7ece813`  |
| 1453   | Layout 1 | `0f7df7ece813`  |
| 1450   | Layout 1 | `0f7df7ece813`  |
| 1445   | Layout 1 | `0f7df7ece813`  |
| 1439   | Layout 1 | `0f7df7ece813`  |
| 1433   | Layout 1 | `0f7df7ece813`  |
| 1430   | Layout 1 | `0f7df7ece813`  |
| 1426   | Layout 1 | `0f7df7ece813`  |
| 1421   | Layout 1 | `0f7df7ece813`  |
| 1417   | Layout 1 | `0f7df7ece813`  |
| 1416   | Layout 1 | `0f7df7ece813`  |
| 1409   | Layout 1 | `0f7df7ece813`  |
| 1405   | Layout 1 | `0f7df7ece813`  |
| 1401   | Layout 1 | `0f7df7ece813`  |
| 1396   | Layout 1 | `0f7df7ece813`  |
| 1391   | Layout 1 | `0f7df7ece813`  |
| 1390   | Layout 1 | `0f7df7ece813`  |
| 1386   | Layout 1 | `0f7df7ece813`  |
| 1381   | Layout 1 | `0f7df7ece813`  |
| 1379   | Layout 1 | `0f7df7ece813`  |
| 1372   | Layout 1 | `0f7df7ece813`  |
| 1366   | Layout 1 | `0f7df7ece813`  |
| 1364   | Layout 1 | `0f7df7ece813`  |
| 1363   | Layout 1 | `0f7df7ece813`  |
| 1360   | Layout 1 | `0f7df7ece813`  |
| 1358   | Layout 1 | `0f7df7ece813`  |
| 1355   | Layout 1 | `0f7df7ece813`  |
| 1351   | Layout 1 | `0f7df7ece813`  |
| 1348   | Layout 1 | `0f7df7ece813`  |
| 1346   | Layout 1 | `0f7df7ece813`  |
| 1341   | Layout 1 | `0f7df7ece813`  |
| 1340   | Layout 1 | `0f7df7ece813`  |
| 1338   | Layout 1 | `0f7df7ece813`  |
| 1335   | Layout 1 | `0f7df7ece813`  |
| 1333   | Layout 1 | `0f7df7ece813`  |
| 1329   | Layout 1 | `0f7df7ece813`  |
| 1327   | Layout 1 | `0f7df7ece813`  |
| 1324   | Layout 1 | `0f7df7ece813`  |
| 1321   | Layout 1 | `0f7df7ece813`  |
| 1319   | Layout 1 | `0f7df7ece813`  |
| 1318   | Layout 1 | `0f7df7ece813`  |
| 1316   | Layout 1 | `0f7df7ece813`  |
| 1313   | Layout 1 | `0f7df7ece813`  |
| 1311   | Layout 1 | `0f7df7ece813`  |
| 1309   | Layout 1 | `0f7df7ece813`  |
| 1304   | Layout 1 | `0f7df7ece813`  |
| 1292   | Layout 1 | `0f7df7ece813`  |
| 1286   | Layout 1 | `0f7df7ece813`  |
| 1280   | No file  | `0f7df7ece813`  |
| 1276   | No file  | `0f7df7ece813`  |
| 1267   | Layout 1 | `0f7df7ece813`  |
| 1261   | Layout 1 | `0f7df7ece813`  |
| 1256   | No file  | `0f7df7ece813`  |
| 1250   | No file  | `0f7df7ece813`  |
| 1246   | No file  | `0f7df7ece813`  |
| 1239   | No file  | `0f7df7ece813`  |
| 1230   | No file  | `0f7df7ece813`  |
| 1226   | No file  | `0f7df7ece813`  |
| 1220   | No file  | `0f7df7ece813`  |
| 1217   | No file  | `0f7df7ece813`  |
| 1211   | No file  | `0f7df7ece813`  |
| 1210   | No file  | `0f7df7ece813`  |
| 1208   | No file  | `0f7df7ece813`  |
| 1203   | No file  | `0f7df7ece813`  |
| 1197   | No file  | `0f7df7ece813`  |
| 1194   | No file  | `0f7df7ece813`  |
| 1192   | No file  | `0f7df7ece813`  |
| 1187   | No file  | `0f7df7ece813`  |
| 1183   | No file  | `0f7df7ece813`  |
| 1177   | No file  | `0f7df7ece813`  |
| 1173   | No file  | `0f7df7ece813`  |
| 1167   | No file  | `0f7df7ece813`  |
| 1164   | No file  | `0f7df7ece813`  |
| 1156   | No file  | `0f7df7ece813`  |
| 1149   | No file  | `0f7df7ece813`  |
| 1144   | No file  | `0f7df7ece813`  |
| 1137   | No file  | `0f7df7ece813`  |
| 1132   | No file  | `0f7df7ece813`  |
| 1127   | No file  | `0f7df7ece813`  |
| 1122   | No file  | `0f7df7ece813`  |
| 1118   | No file  | `0f7df7ece813`  |
| 1114   | No file  | `0f7df7ece813`  |
| 1109   | No file  | `0f7df7ece813`  |
| 1102   | No file  | `0f7df7ece813`  |
| 1096   | No file  | `0f7df7ece813`  |
| 1088   | No file  | `0f7df7ece813`  |
| 1081   | No file  | `0f7df7ece813`  |
| 1076   | No file  | `0f7df7ece813`  |
| 1069   | No file  | `0f7df7ece813`  |
| 1064   | No file  | `0f7df7ece813`  |
| 1058   | No file  | `0f7df7ece813`  |
| 1051   | No file  | `0f7df7ece813`  |
| 1044   | No file  | `0f7df7ece813`  |
| 1036   | No file  | `0f7df7ece813`  |
| 1026   | No file  | `0f7df7ece813`  |
| 1016   | No file  | `0f7df7ece813`  |
| 1009   | No file  | `0f7df7ece813`  |
| 1005   | No file  | `0f7df7ece813`  |
| 1000   | No file  | `0f7df7ece813`  |
| 998    | No file  | `0f7df7ece813`  |
| 990    | No file  | `0f7df7ece813`  |
| 979    | No file  | `0f7df7ece813`  |
| 972    | No file  | `0f7df7ece813`  |
| 963    | No file  | `0f7df7ece813`  |
| 955    | No file  | `0f7df7ece813`  |
| 946    | No file  | `0f7df7ece813`  |
| 938    | No file  | `0f7df7ece813`  |
| 927    | No file  | `0f7df7ece813`  |
| 911    | No file  | `0f7df7ece813`  |
| 904    | No file  | `0f7df7ece813`  |
| 899    | No file  | `0f7df7ece813`  |
| 894    | No file  | `0f7df7ece813`  |
| 885    | No file  | `0f7df7ece813`  |
| 879    | No file  | `0f7df7ece813`  |
| 872    | No file  | `0f7df7ece813`  |
| 864    | No file  | `0f7df7ece813`  |
| 855    | No file  | `0f7df7ece813`  |
| 853    | No file  | `0f7df7ece813`  |
| 845    | No file  | `0f7df7ece813`  |
| 837    | No file  | `0f7df7ece813`  |
| 829    | No file  | `0f7df7ece813`  |
| 822    | No file  | `0f7df7ece813`  |
| 814    | No file  | `0f7df7ece813`  |
| 805    | No file  | `0f7df7ece813`  |
| 794    | No file  | `0f7df7ece813`  |
| 787    | No file  | `0f7df7ece813`  |
| 780    | No file  | `0f7df7ece813`  |
| 771    | No file  | `0f7df7ece813`  |
| 760    | No file  | `0f7df7ece813`  |
| 748    | No file  | `0f7df7ece813`  |
| 741    | No file  | `0f7df7ece813`  |
| 736    | No file  | `0f7df7ece813`  |
| 731    | No file  | `0f7df7ece813`  |
| 723    | No file  | `0f7df7ece813`  |
| 711    | No file  | `0f7df7ece813`  |
| 707    | No file  | `0f7df7ece813`  |
| 697    | No file  | `0f7df7ece813`  |
| 689    | No file  | `0f7df7ece813`  |
| 683    | No file  | `0f7df7ece813`  |
| 678    | No file  | `0f7df7ece813`  |
| 670    | No file  | `0f7df7ece813`  |
| 661    | No file  | `0f7df7ece813`  |
| 656    | No file  | `0f7df7ece813`  |
| 652    | No file  | `0f7df7ece813`  |
| 643    | No file  | `0f7df7ece813`  |
| 637    | No file  | `0f7df7ece813`  |
| 630    | No file  | `0f7df7ece813`  |
| 627    | No file  | `0f7df7ece813`  |
| 621    | No file  | `0f7df7ece813`  |
| 617    | No file  | `0f7df7ece813`  |
| 615    | No file  | `0f7df7ece813`  |
| 606    | No file  | `0f7df7ece813`  |
| 599    | No file  | `0f7df7ece813`  |
| 592    | No file  | `0f7df7ece813`  |
| 586    | No file  | `0f7df7ece813`  |
| 577    | No file  | `0f7df7ece813`  |
| 569    | No file  | `0f7df7ece813`  |
| 561    | No file  | `0f7df7ece813`  |
| 554    | No file  | `0f7df7ece813`  |
| 542    | No file  | `0f7df7ece813`  |
| 532    | No file  | `0f7df7ece813`  |
| 531    | No file  | `0f7df7ece813`  |
| 526    | No file  | `0f7df7ece813`  |
| 521    | No file  | `0f7df7ece813`  |
| 517    | No file  | `0f7df7ece813`  |
| 510    | No file  | `0f7df7ece813`  |
| 508    | No file  | `0f7df7ece813`  |
| 504    | No file  | `0f7df7ece813`  |
| 497    | No file  | `0f7df7ece813`  |
| 491    | No file  | `0f7df7ece813`  |
| 485    | No file  | `0f7df7ece813`  |
| 478    | No file  | `0f7df7ece813`  |
| 472    | No file  | `0f7df7ece813`  |
| 466    | No file  | `0f7df7ece813`  |
| 457    | No file  | `0f7df7ece813`  |
| 452    | No file  | `0f7df7ece813`  |
| 449    | No file  | `0f7df7ece813`  |
| 435    | No file  | `0f7df7ece813`  |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                      |
| ------------------------ | -------- | --------------------------------------------------------- |
| `fairypotionoffset.dbss` | Optional | `potion_type -> (data_offset, data_size)` index           |
| `languagedata_en.loc`    | Optional | Item name for `item_id` (`str_type=0`, `str_id1=item_id`) |

Each list stores its own item count, so the handler walks the main file
without the offset companion.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field | Notes                |
| ------- | ------------------ | ----- | -------------------- |
| `+0x00` | u32                | count | Number of lists      |
| `+0x04` | Potion List[count] | lists | See Potion List      |

### Potion List (variable: 5 bytes + items)

| Offset          | Type             | Field       | Notes                                   |
| --------------- | ---------------- | ----------- | --------------------------------------- |
| `+0x00`         | u32              | item_count  | Number of item IDs that follow          |
| `+0x04`         | u32[item_count]  | item_ids    | Items the fairy may use for this type   |
| `item_ids+0x00` | u8               | potion_type | List key, see Potion Types              |

A list is `4 + 4 * item_count + 1` bytes. The key is the last byte of the
list, not the first, and the last list ends at the end of the file.

On client 3464 the file is 1,200 bytes: 4 lists stored in key order `3`, `2`,
`1`, `0` with 77, 77, 77 and 63 items (294 rows in the handler).

Every `item_id` has a zero top byte, so it reads the same as an item key with
enhancement level 0 (`_common/item_key.py`).

### `fairypotionoffset.dbss`

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `fairypotion.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                              |
| ------- | ---- | ----------- | -------------------------------------------------- |
| `+0x00` | u16  | potion_type | List key                                           |
| `+0x02` | u32  | data_offset | Absolute offset of the list's `item_count`         |
| `+0x06` | u32  | data_size   | Whole list, trailing `potion_type` byte included   |

There is no `PABR` magic and no trailer (`parse_bare_offset_rows`). Rows are
in the same order as the lists. Unlike most offset tables, `data_offset`
points at the start of the list, since the key sits at its end.

## Potion Types

| Type | Resource | Items on client 3464                                                       |
| ---- | -------- | -------------------------------------------------------------------------- |
| 0    | HP       | HP potions, Grain Juice, HP Spirit Essence items, Odore's Spirits         |
| 1    | MP       | MP, WP and SP potions, Herbal Juice, MP Spirit Essence items, Ornette's Spirits |
| 2    | WP       | The type `1` items with Odore's Spirits in place of Ornette's Spirits      |
| 3    | SP       | The type `2` items in the same order                                       |

Type `0` is HP: on client 3464 every named item in it is an HP item by its
English LOC name or description. The names of types `1` to `3` come from the
client Lua (see Notes); the lists themselves no longer tell them apart.

## Notes

- The Fairy Settings window (`panel_window_fairy_all_4.luac`,
  `PaGlobal_FairySetting_All`) has one HP slot and one MP slot. Its inventory
  list shows the items for which `ToClient_checkUsableFairyPotion(itemKey,
  classType)` is true. On a click, `ToClient_getFairyPotionType(itemKey,
  classType)` returns `-1` (message `LUA_FAIRYSETTING_NOT_ITEM`), `0` (HP
  slot) or another value (MP slot). Both calls take the player's class type,
  which fits one list per class resource.
- The same Lua file still holds hard-coded lists: `fairyMainPotionData[0]`
  (HP potions) and `fairySubPotionData[1]`, `[2]` and `[3]`. Index `1` holds
  MP potions and is the default; index `2` holds WP potions and is picked for
  the class types in its `spiritClass` table (0 Warrior, 11 Lahn, 12
  Berserker, 19 Striker, 20 Musa, 21 Maehwa, 23 Mystic, 25 Kunoichi, 26
  Ninja, 30 Woosa); index `3` holds SP potions and is picked for class type
  24 (Valkyrie). Indexes `2` and `3` also hold the Herbal Juice items. Only
  `isMP()` and `isHP()` read these tables, and they are passed `mpKeyStr`
  and `hpKeyStr`, which no fairy Lua file sets. The Resource names in this
  doc follow these indexes.
- On client 3464 every item of the Lua lists is in the matching list of this
  file except `[Savage] HP Potion (Extra Large)` (56093), which the Lua HP
  list has and list `0` lacks. Its MP counterpart (56094) is in lists `1` to
  `3`. The file lists add the Spirit Essence items, the Gourd Bottles (1041,
  1042) and others the Lua lists lack.
- Lists `1` to `3` each hold the MP, WP and SP potions together on client
  3464, while the Lua lists keep them apart (index `1` MP only, `2` WP only,
  `3` SP only).
- The two "Spirits" items are named the other way round from the two
  "Spirit Essence" items: Odore's Spirits (40734) and Ornette's Spirit
  Essence (40747) restore 550 HP, Ornette's Spirits (40733) and Odore's Spirit
  Essence (40713) restore 375 MP/WP/SP (English LOC item descriptions).
  List `0` and list `1` follow the descriptions; lists `2` and `3` hold
  Odore's Spirits (HP) and lack Ornette's Spirits.
- On client 3464, 26 rows have no English LOC item name: items 46901 and
  46907 in list `0`, and 46902 to 46904, 46908 to 46910, 720752 and 720753
  in each of lists `1` to `3`. The handler shows their item ID.

## Open Questions

### Potion Types 1 to 3

Type `0` is HP by its content. The MP, WP and SP names of types `1`, `2` and
`3` rest on the indexes of the Lua's `fairySubPotionData` table; the file
lists are near copies of each other, and the class-to-list choice happens in
`ToClient_getFairyPotionType`, which the Lua cannot show.

## In-Game Checks

### Ornette's Spirits for a WP Class

Needs item: [Ornette's Spirits](https://bdocodex.com/us/item/40733/)

Needs class: Warrior, or another class in the Lua's `spiritClass` list

Lists `2` and `3` lack Ornette's Spirits (MP/WP/SP) and hold Odore's Spirits
(HP) instead. Open the fairy's potion settings with Ornette's Spirits in the
inventory. If it is missing from the list on a Warrior but shows on an MP
class such as Sorceress, the client reads list `2` for WP classes, which
confirms type `2` as WP. If it shows on both, the client does not pick the
list by these types the way the Lua does.
