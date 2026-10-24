# `collect.dbss` Format

## Purpose

Gathering rules per gathering character: one row per Collect character (a
tree, ore vein, plant or animal corpse) with its gathering kind, gathering
time, the tools that work on it and the drop group each tool gives. The row
key is the character key that `collectresourcename.dbss` maps the world
models to. `collectoffset.dbss` is the key-ordered index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------- | ------ | -------------- | --------- |
| 2      | 2726 and later | 3483    | `collect.dbss`       | 48,556 | 714 Row        | 68        |
| 2      | 2726 and later | 3483    | `collectoffset.dbss` | 7,144  | 714 Offset Row | 10        |
| 1      | 1346 to 2039   | 2039    | `collect.dbss`       | 29,716 | 619 Row        | 48        |
| 1      | 1346 to 2039   | 2039    | `collectoffset.dbss` | 6,194  | 619 Offset Row | 10        |

| Layout | File                 | Known             | Unknown         |
| ------ | -------------------- | ----------------- | --------------- |
| 2      | `collect.dbss`       | 39,988 B (82.4%)  | 8,568 B (17.6%) |
| 2      | `collectoffset.dbss` | 7,144 B (100.0%)  | 0 B (0.0%)      |
| 1      | `collect.dbss`       | 29,716 B (100.0%) | 0 B (0.0%)      |
| 1      | `collectoffset.dbss` | 6,194 B (100.0%)  | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `2614241a0fe6`  |
| 3482   | Layout 2             | `2614241a0fe6`  |
| 3474   | Layout 2             | `2614241a0fe6`  |
| 3473   | Layout 2             | `2614241a0fe6`  |
| 3464   | Layout 2             | `2614241a0fe6`  |
| 3458   | Layout 2             | `2614241a0fe6`  |
| 3454   | Layout 2             | `2614241a0fe6`  |
| 3444   | Layout 2             | `2614241a0fe6`  |
| 3435   | Layout 2             | `2614241a0fe6`  |
| 3426   | Layout 2             | `2614241a0fe6`  |
| 3418   | Layout 2             | `2614241a0fe6`  |
| 3412   | Layout 2             | `2614241a0fe6`  |
| 3402   | Layout 2             | `2614241a0fe6`  |
| 3396   | Layout 2             | `2614241a0fe6`  |
| 3387   | Layout 2             | `2614241a0fe6`  |
| 3381   | Layout 2             | `2614241a0fe6`  |
| 3373   | Layout 2             | `2614241a0fe6`  |
| 3364   | Layout 2             | `2614241a0fe6`  |
| 3356   | Layout 2             | `2614241a0fe6`  |
| 3349   | Layout 2             | `2614241a0fe6`  |
| 3342   | Layout 2             | `2614241a0fe6`  |
| 3335   | Layout 2             | `2614241a0fe6`  |
| 3326   | Layout 2             | `2614241a0fe6`  |
| 3321   | Layout 2             | `2614241a0fe6`  |
| 3314   | Layout 2             | `2614241a0fe6`  |
| 3303   | Layout 2             | `2614241a0fe6`  |
| 3302   | Layout 2             | `2614241a0fe6`  |
| 3293   | Layout 2             | `2614241a0fe6`  |
| 3283   | Layout 2             | `2614241a0fe6`  |
| 3275   | Layout 2             | `2614241a0fe6`  |
| 3267   | Layout 2             | `2614241a0fe6`  |
| 3258   | Layout 2             | `2614241a0fe6`  |
| 3251   | Layout 2             | `2614241a0fe6`  |
| 3242   | Layout 2             | `2614241a0fe6`  |
| 3235   | Layout 2             | `2614241a0fe6`  |
| 3229   | Layout 2             | `2614241a0fe6`  |
| 3212   | Layout 2             | `2614241a0fe6`  |
| 3203   | Layout 2             | `2614241a0fe6`  |
| 3193   | Layout 2             | `2614241a0fe6`  |
| 3186   | Layout 2             | `2614241a0fe6`  |
| 3177   | Layout 2             | `2614241a0fe6`  |
| 3169   | Layout 2             | `2614241a0fe6`  |
| 3158   | Layout 2             | `2614241a0fe6`  |
| 3151   | Layout 2             | `2614241a0fe6`  |
| 3144   | Layout 2             | `2614241a0fe6`  |
| 3133   | Layout 2             | `2614241a0fe6`  |
| 3125   | Layout 2             | `2614241a0fe6`  |
| 3118   | Layout 2             | `2614241a0fe6`  |
| 3111   | Layout 2             | `2614241a0fe6`  |
| 3103   | Layout 2             | `2614241a0fe6`  |
| 3095   | Layout 2             | `2614241a0fe6`  |
| 3086   | Layout 2             | `2614241a0fe6`  |
| 3072   | Layout 2             | `2614241a0fe6`  |
| 3062   | Layout 2             | `2614241a0fe6`  |
| 3052   | Layout 2             | `2614241a0fe6`  |
| 3045   | Layout 2             | `2614241a0fe6`  |
| 3037   | Layout 2             | `2614241a0fe6`  |
| 3030   | Layout 2             | `2614241a0fe6`  |
| 3021   | Layout 2             | `2614241a0fe6`  |
| 3012   | Layout 2             | `2614241a0fe6`  |
| 3002   | Layout 2             | `2614241a0fe6`  |
| 2995   | Layout 2             | `2614241a0fe6`  |
| 2987   | Layout 2             | `2614241a0fe6`  |
| 2978   | Layout 2             | `2614241a0fe6`  |
| 2970   | Layout 2             | `2614241a0fe6`  |
| 2959   | Layout 2             | `2614241a0fe6`  |
| 2951   | Layout 2             | `2614241a0fe6`  |
| 2942   | Layout 2             | `2614241a0fe6`  |
| 2935   | Layout 2             | `2614241a0fe6`  |
| 2932   | Layout 2             | `2614241a0fe6`  |
| 2923   | Layout 2             | `2614241a0fe6`  |
| 2919   | Layout 2             | `2614241a0fe6`  |
| 2907   | Layout 2             | `2614241a0fe6`  |
| 2900   | Layout 2             | `2614241a0fe6`  |
| 2891   | Layout 2             | `2614241a0fe6`  |
| 2882   | Layout 2             | `2614241a0fe6`  |
| 2872   | Layout 2             | `2614241a0fe6`  |
| 2863   | Layout 2             | `2614241a0fe6`  |
| 2855   | Layout 2             | `2614241a0fe6`  |
| 2849   | Layout 2             | `2614241a0fe6`  |
| 2844   | Layout 2             | `2614241a0fe6`  |
| 2834   | Layout 2             | `2614241a0fe6`  |
| 2825   | Layout 2             | `2614241a0fe6`  |
| 2819   | Layout 2             | `2614241a0fe6`  |
| 2811   | Layout 2             | `2614241a0fe6`  |
| 2803   | Layout 2             | `2614241a0fe6`  |
| 2794   | Layout 2             | `2614241a0fe6`  |
| 2783   | Layout 2             | `2614241a0fe6`  |
| 2774   | Layout 2             | `2614241a0fe6`  |
| 2765   | Layout 2             | `2614241a0fe6`  |
| 2756   | Layout 2             | `2614241a0fe6`  |
| 2750   | Layout 2             | `2614241a0fe6`  |
| 2743   | Layout 2             | `2614241a0fe6`  |
| 2736   | Layout 2             | `2614241a0fe6`  |
| 2726   | Layout 2             | `2614241a0fe6`  |
| 2717   | No documented layout | `2614241a0fe6`  |
| 2709   | No documented layout | `2614241a0fe6`  |
| 2703   | No documented layout | `2614241a0fe6`  |
| 2695   | No documented layout | `2614241a0fe6`  |
| 2684   | No documented layout | `2614241a0fe6`  |
| 2672   | No documented layout | `2614241a0fe6`  |
| 2665   | No documented layout | `2614241a0fe6`  |
| 2657   | No documented layout | `2614241a0fe6`  |
| 2649   | No documented layout | `2614241a0fe6`  |
| 2644   | No documented layout | `2614241a0fe6`  |
| 2637   | No documented layout | `2614241a0fe6`  |
| 2629   | No documented layout | `2614241a0fe6`  |
| 2619   | No documented layout | `2614241a0fe6`  |
| 2612   | No documented layout | `2614241a0fe6`  |
| 2606   | No documented layout | `2614241a0fe6`  |
| 2602   | No documented layout | `2614241a0fe6`  |
| 2601   | No documented layout | `2614241a0fe6`  |
| 2592   | No documented layout | `2614241a0fe6`  |
| 2583   | No documented layout | `2614241a0fe6`  |
| 2575   | No documented layout | `2614241a0fe6`  |
| 2567   | No documented layout | `2614241a0fe6`  |
| 2560   | No documented layout | `2614241a0fe6`  |
| 2553   | No documented layout | `2614241a0fe6`  |
| 2545   | No documented layout | `2614241a0fe6`  |
| 2538   | No documented layout | `2614241a0fe6`  |
| 2529   | No documented layout | `2614241a0fe6`  |
| 2519   | No documented layout | `2614241a0fe6`  |
| 2513   | No documented layout | `2614241a0fe6`  |
| 2510   | No documented layout | `2614241a0fe6`  |
| 2507   | No documented layout | `2614241a0fe6`  |
| 2503   | No documented layout | `2614241a0fe6`  |
| 2498   | No documented layout | `2614241a0fe6`  |
| 2492   | No documented layout | `2614241a0fe6`  |
| 2487   | No documented layout | `2614241a0fe6`  |
| 2480   | No documented layout | `2614241a0fe6`  |
| 2474   | No documented layout | `2614241a0fe6`  |
| 2468   | No documented layout | `2614241a0fe6`  |
| 2460   | No documented layout | `2614241a0fe6`  |
| 2453   | No documented layout | `2614241a0fe6`  |
| 2444   | No documented layout | `2614241a0fe6`  |
| 2438   | No documented layout | `2614241a0fe6`  |
| 2434   | No documented layout | `2614241a0fe6`  |
| 2429   | No documented layout | `2614241a0fe6`  |
| 2421   | No documented layout | `2614241a0fe6`  |
| 2414   | No documented layout | `2614241a0fe6`  |
| 2407   | No documented layout | `2614241a0fe6`  |
| 2401   | No documented layout | `2614241a0fe6`  |
| 2397   | No documented layout | `2614241a0fe6`  |
| 2393   | No documented layout | `2614241a0fe6`  |
| 2384   | No documented layout | `2614241a0fe6`  |
| 2378   | No documented layout | `2614241a0fe6`  |
| 2372   | No documented layout | `2614241a0fe6`  |
| 2358   | No documented layout | `2614241a0fe6`  |
| 2352   | No documented layout | `2614241a0fe6`  |
| 2347   | No documented layout | `2614241a0fe6`  |
| 2343   | No documented layout | `2614241a0fe6`  |
| 2335   | No documented layout | `2614241a0fe6`  |
| 2327   | No documented layout | `2614241a0fe6`  |
| 2324   | No documented layout | `2614241a0fe6`  |
| 2319   | No documented layout | `2614241a0fe6`  |
| 2313   | No documented layout | `2614241a0fe6`  |
| 2308   | No documented layout | `2614241a0fe6`  |
| 2302   | No documented layout | `2614241a0fe6`  |
| 2295   | No documented layout | `2614241a0fe6`  |
| 2290   | No documented layout | `2614241a0fe6`  |
| 2284   | No documented layout | `2614241a0fe6`  |
| 2276   | No documented layout | `2614241a0fe6`  |
| 2269   | No documented layout | `2614241a0fe6`  |
| 2259   | No documented layout | `2614241a0fe6`  |
| 2250   | No documented layout | `2614241a0fe6`  |
| 2243   | No documented layout | `2614241a0fe6`  |
| 2235   | No documented layout | `2614241a0fe6`  |
| 2229   | No documented layout | `2614241a0fe6`  |
| 2224   | No documented layout | `2614241a0fe6`  |
| 2218   | No documented layout | `2614241a0fe6`  |
| 2215   | No documented layout | `2614241a0fe6`  |
| 2207   | No documented layout | `2614241a0fe6`  |
| 2203   | No documented layout | `2614241a0fe6`  |
| 2196   | No documented layout | `2614241a0fe6`  |
| 2192   | No documented layout | `2614241a0fe6`  |
| 2189   | No documented layout | `2614241a0fe6`  |
| 2183   | No documented layout | `2614241a0fe6`  |
| 2179   | No documented layout | `2614241a0fe6`  |
| 2171   | No documented layout | `2614241a0fe6`  |
| 2163   | No documented layout | `2614241a0fe6`  |
| 2156   | No documented layout | `2614241a0fe6`  |
| 2151   | No documented layout | `2614241a0fe6`  |
| 2147   | No documented layout | `2614241a0fe6`  |
| 2142   | No documented layout | `2614241a0fe6`  |
| 2138   | No documented layout | `2614241a0fe6`  |
| 2134   | No documented layout | `2614241a0fe6`  |
| 2130   | No documented layout | `2614241a0fe6`  |
| 2122   | No documented layout | `2614241a0fe6`  |
| 2107   | No documented layout | `2614241a0fe6`  |
| 2098   | No documented layout | `2614241a0fe6`  |
| 2089   | No documented layout | `2614241a0fe6`  |
| 2081   | No documented layout | `2614241a0fe6`  |
| 2073   | No documented layout | `2614241a0fe6`  |
| 2067   | No documented layout | `2614241a0fe6`  |
| 2063   | No documented layout | `2614241a0fe6`  |
| 2059   | No documented layout | `2614241a0fe6`  |
| 2052   | No documented layout | `2614241a0fe6`  |
| 2044   | No documented layout | `2614241a0fe6`  |
| 2039   | Layout 1             | `2614241a0fe6`  |
| 2032   | Layout 1             | `2614241a0fe6`  |
| 2025   | Layout 1             | `2614241a0fe6`  |
| 2011   | Layout 1             | `2614241a0fe6`  |
| 2005   | Layout 1             | `2614241a0fe6`  |
| 2000   | Layout 1             | `2614241a0fe6`  |
| 1996   | Layout 1             | `2614241a0fe6`  |
| 1991   | Layout 1             | `2614241a0fe6`  |
| 1985   | Layout 1             | `2614241a0fe6`  |
| 1980   | Layout 1             | `2614241a0fe6`  |
| 1969   | Layout 1             | `2614241a0fe6`  |
| 1964   | Layout 1             | `2614241a0fe6`  |
| 1958   | Layout 1             | `2614241a0fe6`  |
| 1950   | Layout 1             | `2614241a0fe6`  |
| 1945   | Layout 1             | `2614241a0fe6`  |
| 1937   | Layout 1             | `2614241a0fe6`  |
| 1933   | Layout 1             | `2614241a0fe6`  |
| 1927   | Layout 1             | `2614241a0fe6`  |
| 1921   | Layout 1             | `2614241a0fe6`  |
| 1914   | Layout 1             | `2614241a0fe6`  |
| 1908   | Layout 1             | `2614241a0fe6`  |
| 1897   | Layout 1             | `2614241a0fe6`  |
| 1892   | Layout 1             | `2614241a0fe6`  |
| 1886   | Layout 1             | `2614241a0fe6`  |
| 1881   | Layout 1             | `2614241a0fe6`  |
| 1871   | Layout 1             | `2614241a0fe6`  |
| 1866   | Layout 1             | `2614241a0fe6`  |
| 1862   | Layout 1             | `2614241a0fe6`  |
| 1854   | Layout 1             | `2614241a0fe6`  |
| 1846   | Layout 1             | `2614241a0fe6`  |
| 1838   | Layout 1             | `2614241a0fe6`  |
| 1832   | Layout 1             | `2614241a0fe6`  |
| 1826   | Layout 1             | `2614241a0fe6`  |
| 1822   | Layout 1             | `2614241a0fe6`  |
| 1818   | Layout 1             | `2614241a0fe6`  |
| 1804   | Layout 1             | `2614241a0fe6`  |
| 1794   | Layout 1             | `2614241a0fe6`  |
| 1790   | Layout 1             | `2614241a0fe6`  |
| 1784   | Layout 1             | `2614241a0fe6`  |
| 1774   | Layout 1             | `2614241a0fe6`  |
| 1771   | Layout 1             | `2614241a0fe6`  |
| 1762   | Layout 1             | `2614241a0fe6`  |
| 1759   | Layout 1             | `2614241a0fe6`  |
| 1754   | Layout 1             | `2614241a0fe6`  |
| 1749   | Layout 1             | `2614241a0fe6`  |
| 1743   | Layout 1             | `2614241a0fe6`  |
| 1737   | Layout 1             | `2614241a0fe6`  |
| 1731   | Layout 1             | `2614241a0fe6`  |
| 1725   | Layout 1             | `2614241a0fe6`  |
| 1717   | Layout 1             | `2614241a0fe6`  |
| 1710   | Layout 1             | `2614241a0fe6`  |
| 1704   | Layout 1             | `2614241a0fe6`  |
| 1698   | Layout 1             | `2614241a0fe6`  |
| 1690   | Layout 1             | `2614241a0fe6`  |
| 1685   | Layout 1             | `2614241a0fe6`  |
| 1680   | Layout 1             | `2614241a0fe6`  |
| 1674   | Layout 1             | `2614241a0fe6`  |
| 1668   | Layout 1             | `2614241a0fe6`  |
| 1659   | Layout 1             | `2614241a0fe6`  |
| 1649   | Layout 1             | `2614241a0fe6`  |
| 1642   | Layout 1             | `2614241a0fe6`  |
| 1636   | Layout 1             | `2614241a0fe6`  |
| 1628   | Layout 1             | `2614241a0fe6`  |
| 1622   | Layout 1             | `2614241a0fe6`  |
| 1614   | Layout 1             | `2614241a0fe6`  |
| 1608   | Layout 1             | `2614241a0fe6`  |
| 1602   | Layout 1             | `2614241a0fe6`  |
| 1598   | Layout 1             | `2614241a0fe6`  |
| 1594   | Layout 1             | `2614241a0fe6`  |
| 1590   | Layout 1             | `2614241a0fe6`  |
| 1587   | Layout 1             | `2614241a0fe6`  |
| 1584   | Layout 1             | `2614241a0fe6`  |
| 1579   | Layout 1             | `2614241a0fe6`  |
| 1572   | Layout 1             | `2614241a0fe6`  |
| 1565   | Layout 1             | `2614241a0fe6`  |
| 1559   | Layout 1             | `2614241a0fe6`  |
| 1554   | Layout 1             | `2614241a0fe6`  |
| 1547   | Layout 1             | `2614241a0fe6`  |
| 1537   | Layout 1             | `2614241a0fe6`  |
| 1529   | Layout 1             | `2614241a0fe6`  |
| 1524   | Layout 1             | `2614241a0fe6`  |
| 1519   | Layout 1             | `2614241a0fe6`  |
| 1509   | Layout 1             | `2614241a0fe6`  |
| 1506   | Layout 1             | `2614241a0fe6`  |
| 1504   | Layout 1             | `2614241a0fe6`  |
| 1500   | Layout 1             | `2614241a0fe6`  |
| 1493   | Layout 1             | `2614241a0fe6`  |
| 1489   | Layout 1             | `2614241a0fe6`  |
| 1485   | Layout 1             | `2614241a0fe6`  |
| 1481   | Layout 1             | `2614241a0fe6`  |
| 1474   | Layout 1             | `2614241a0fe6`  |
| 1466   | Layout 1             | `2614241a0fe6`  |
| 1462   | Layout 1             | `2614241a0fe6`  |
| 1459   | Layout 1             | `2614241a0fe6`  |
| 1453   | Layout 1             | `2614241a0fe6`  |
| 1450   | Layout 1             | `2614241a0fe6`  |
| 1445   | Layout 1             | `2614241a0fe6`  |
| 1439   | Layout 1             | `2614241a0fe6`  |
| 1433   | Layout 1             | `2614241a0fe6`  |
| 1430   | Layout 1             | `2614241a0fe6`  |
| 1426   | Layout 1             | `2614241a0fe6`  |
| 1421   | Layout 1             | `2614241a0fe6`  |
| 1417   | Layout 1             | `2614241a0fe6`  |
| 1416   | Layout 1             | `2614241a0fe6`  |
| 1409   | Layout 1             | `2614241a0fe6`  |
| 1405   | Layout 1             | `2614241a0fe6`  |
| 1401   | Layout 1             | `2614241a0fe6`  |
| 1396   | Layout 1             | `2614241a0fe6`  |
| 1391   | Layout 1             | `2614241a0fe6`  |
| 1390   | Layout 1             | `2614241a0fe6`  |
| 1386   | Layout 1             | `2614241a0fe6`  |
| 1381   | Layout 1             | `2614241a0fe6`  |
| 1379   | Layout 1             | `2614241a0fe6`  |
| 1372   | Layout 1             | `2614241a0fe6`  |
| 1366   | Layout 1             | `2614241a0fe6`  |
| 1364   | Layout 1             | `2614241a0fe6`  |
| 1363   | Layout 1             | `2614241a0fe6`  |
| 1360   | Layout 1             | `2614241a0fe6`  |
| 1358   | Layout 1             | `2614241a0fe6`  |
| 1355   | Layout 1             | `2614241a0fe6`  |
| 1351   | Layout 1             | `2614241a0fe6`  |
| 1348   | Layout 1             | `2614241a0fe6`  |
| 1346   | Layout 1             | `2614241a0fe6`  |
| 1341   | No documented layout | `2614241a0fe6`  |
| 1340   | No documented layout | `2614241a0fe6`  |
| 1338   | No documented layout | `2614241a0fe6`  |
| 1335   | No documented layout | `2614241a0fe6`  |
| 1333   | No documented layout | `2614241a0fe6`  |
| 1329   | No documented layout | `2614241a0fe6`  |
| 1327   | No documented layout | `2614241a0fe6`  |
| 1324   | No documented layout | `2614241a0fe6`  |
| 1321   | No documented layout | `2614241a0fe6`  |
| 1319   | No documented layout | `2614241a0fe6`  |
| 1318   | No documented layout | `2614241a0fe6`  |
| 1316   | No documented layout | `2614241a0fe6`  |
| 1313   | No documented layout | `2614241a0fe6`  |
| 1311   | No documented layout | `2614241a0fe6`  |
| 1309   | No documented layout | `2614241a0fe6`  |
| 1304   | No documented layout | `2614241a0fe6`  |
| 1292   | No documented layout | `2614241a0fe6`  |
| 1286   | No documented layout | `2614241a0fe6`  |
| 1280   | No documented layout | `2614241a0fe6`  |
| 1276   | No documented layout | `2614241a0fe6`  |
| 1267   | No documented layout | `2614241a0fe6`  |
| 1261   | No documented layout | `2614241a0fe6`  |
| 1256   | No documented layout | `2614241a0fe6`  |
| 1250   | No file              | `2614241a0fe6`  |
| 1246   | No file              | `2614241a0fe6`  |
| 1239   | No file              | `2614241a0fe6`  |
| 1230   | No file              | `2614241a0fe6`  |
| 1226   | No file              | `2614241a0fe6`  |
| 1220   | No file              | `2614241a0fe6`  |
| 1217   | No file              | `2614241a0fe6`  |
| 1211   | No file              | `2614241a0fe6`  |
| 1210   | No file              | `2614241a0fe6`  |
| 1208   | No file              | `2614241a0fe6`  |
| 1203   | No file              | `2614241a0fe6`  |
| 1197   | No file              | `2614241a0fe6`  |
| 1194   | No file              | `2614241a0fe6`  |
| 1192   | No file              | `2614241a0fe6`  |
| 1187   | No file              | `2614241a0fe6`  |
| 1183   | No file              | `2614241a0fe6`  |
| 1177   | No file              | `2614241a0fe6`  |
| 1173   | No file              | `2614241a0fe6`  |
| 1167   | No file              | `2614241a0fe6`  |
| 1164   | No file              | `2614241a0fe6`  |
| 1156   | No file              | `2614241a0fe6`  |
| 1149   | No file              | `2614241a0fe6`  |
| 1144   | No file              | `2614241a0fe6`  |
| 1137   | No file              | `2614241a0fe6`  |
| 1132   | No file              | `2614241a0fe6`  |
| 1127   | No file              | `2614241a0fe6`  |
| 1122   | No file              | `2614241a0fe6`  |
| 1118   | No file              | `2614241a0fe6`  |
| 1114   | No file              | `2614241a0fe6`  |
| 1109   | No file              | `2614241a0fe6`  |
| 1102   | No file              | `2614241a0fe6`  |
| 1096   | No file              | `2614241a0fe6`  |
| 1088   | No file              | `2614241a0fe6`  |
| 1081   | No file              | `2614241a0fe6`  |
| 1076   | No file              | `2614241a0fe6`  |
| 1069   | No file              | `2614241a0fe6`  |
| 1064   | No file              | `2614241a0fe6`  |
| 1058   | No file              | `2614241a0fe6`  |
| 1051   | No file              | `2614241a0fe6`  |
| 1044   | No file              | `2614241a0fe6`  |
| 1036   | No file              | `2614241a0fe6`  |
| 1026   | No file              | `2614241a0fe6`  |
| 1016   | No file              | `2614241a0fe6`  |
| 1009   | No file              | `2614241a0fe6`  |
| 1005   | No file              | `2614241a0fe6`  |
| 1000   | No file              | `2614241a0fe6`  |
| 998    | No file              | `2614241a0fe6`  |
| 990    | No file              | `2614241a0fe6`  |
| 979    | No file              | `2614241a0fe6`  |
| 972    | No file              | `2614241a0fe6`  |
| 963    | No file              | `2614241a0fe6`  |
| 955    | No file              | `2614241a0fe6`  |
| 946    | No file              | `2614241a0fe6`  |
| 938    | No file              | `2614241a0fe6`  |
| 927    | No file              | `2614241a0fe6`  |
| 911    | No file              | `2614241a0fe6`  |
| 904    | No file              | `2614241a0fe6`  |
| 899    | No file              | `2614241a0fe6`  |
| 894    | No file              | `2614241a0fe6`  |
| 885    | No file              | `2614241a0fe6`  |
| 879    | No file              | `2614241a0fe6`  |
| 872    | No file              | `2614241a0fe6`  |
| 864    | No file              | `2614241a0fe6`  |
| 855    | No file              | `2614241a0fe6`  |
| 853    | No file              | `2614241a0fe6`  |
| 845    | No file              | `2614241a0fe6`  |
| 837    | No file              | `2614241a0fe6`  |
| 829    | No file              | `2614241a0fe6`  |
| 822    | No file              | `2614241a0fe6`  |
| 814    | No file              | `2614241a0fe6`  |
| 805    | No file              | `2614241a0fe6`  |
| 794    | No file              | `2614241a0fe6`  |
| 787    | No file              | `2614241a0fe6`  |
| 780    | No file              | `2614241a0fe6`  |
| 771    | No file              | `2614241a0fe6`  |
| 760    | No file              | `2614241a0fe6`  |
| 748    | No file              | `2614241a0fe6`  |
| 741    | No file              | `2614241a0fe6`  |
| 736    | No file              | `2614241a0fe6`  |
| 731    | No file              | `2614241a0fe6`  |
| 723    | No file              | `2614241a0fe6`  |
| 711    | No file              | `2614241a0fe6`  |
| 707    | No file              | `2614241a0fe6`  |
| 697    | No file              | `2614241a0fe6`  |
| 689    | No file              | `2614241a0fe6`  |
| 683    | No file              | `2614241a0fe6`  |
| 678    | No file              | `2614241a0fe6`  |
| 670    | No file              | `2614241a0fe6`  |
| 661    | No file              | `2614241a0fe6`  |
| 656    | No file              | `2614241a0fe6`  |
| 652    | No file              | `2614241a0fe6`  |
| 643    | No file              | `2614241a0fe6`  |
| 637    | No file              | `2614241a0fe6`  |
| 630    | No file              | `2614241a0fe6`  |
| 627    | No file              | `2614241a0fe6`  |
| 621    | No file              | `2614241a0fe6`  |
| 617    | No file              | `2614241a0fe6`  |
| 615    | No file              | `2614241a0fe6`  |
| 606    | No file              | `2614241a0fe6`  |
| 599    | No file              | `2614241a0fe6`  |
| 592    | No file              | `2614241a0fe6`  |
| 586    | No file              | `2614241a0fe6`  |
| 577    | No file              | `2614241a0fe6`  |
| 569    | No file              | `2614241a0fe6`  |
| 561    | No file              | `2614241a0fe6`  |
| 554    | No file              | `2614241a0fe6`  |
| 542    | No file              | `2614241a0fe6`  |
| 532    | No file              | `2614241a0fe6`  |
| 531    | No file              | `2614241a0fe6`  |
| 526    | No file              | `2614241a0fe6`  |
| 521    | No file              | `2614241a0fe6`  |
| 517    | No file              | `2614241a0fe6`  |
| 510    | No file              | `2614241a0fe6`  |
| 508    | No file              | `2614241a0fe6`  |
| 504    | No file              | `2614241a0fe6`  |
| 497    | No file              | `2614241a0fe6`  |
| 491    | No file              | `2614241a0fe6`  |
| 485    | No file              | `2614241a0fe6`  |
| 478    | No file              | `2614241a0fe6`  |
| 472    | No file              | `2614241a0fe6`  |
| 466    | No file              | `2614241a0fe6`  |
| 457    | No file              | `2614241a0fe6`  |
| 452    | No file              | `2614241a0fe6`  |
| 449    | No file              | `2614241a0fe6`  |
| 435    | No file              | `2614241a0fe6`  |

<!-- versions:end -->

## Companion Files

| File                                              | Required | Role                                                        |
| ------------------------------------------------- | -------- | ----------------------------------------------------------- |
| `collectoffset.dbss`                              | Optional | `character_key -> (data_offset, data_size)` index; the rows are fixed size and can be walked without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row |

Character names come from LOC type 6.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                      |
| ------- | ---------- | ----- | ------------------------------------------ |
| `+0x00` | u32        | count | Number of rows; `713` on client 3474       |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 68 bytes + name text)

| Offset        | Type    | Field                  | Notes                                                              |
| ------------- | ------- | ---------------------- | ------------------------------------------------------------------ |
| `+0x00`       | u16     | character_key          | Gathering character, a `characterstatic.dbss` `character_id`; unique per row, the index key |
| `+0x02`       | str16   | name                   | Empty on every row; the index's `data_offset` points here          |
| `name+0x00`   | u16     | character_key_dup      | Equal to `character_key` in every row                              |
| `name+0x02`   | u8      | product_data_type      | Gathering kind, see Product Data Types                             |
| `name+0x03`   | u32     | product_time           | `60000` on every row (client 3474)                                 |
| `name+0x07`   | f32     | product_hp             | `1.0` on every row (client 3474)                                   |
| `name+0x0B`   | f32     | product_decrease_hp    | `1.0` on every row (client 3474)                                   |
| `name+0x0F`   | u32     | product_item_drop_key  | `10002` on every row (client 3474); an item main group key, see Notes |
| `name+0x13`   | u8[3]   | collect_tool_types     | Tool per slot, see Collect Tool Types; `19` is an empty slot       |
| `name+0x16`   | u32[3]  | collect_item_drop_keys | Item main group key per slot; `0` exactly where the slot's tool is `19` |
| `name+0x22`   | bytes[12] | unknown_name_22      | `0` on every row (client 3474); not in Layout 1                    |
| `name+0x2E`   | u32     | action_point           | `1` on every row (client 3474)                                     |
| `name+0x32`   | u32     | spawn_delay_time       | `0` on every row (client 3474)                                     |
| `name+0x36`   | u32     | spawn_variable_time    | `0` on every row (client 3474)                                     |

With the empty `name`, every row is 68 bytes. The rows are not sorted by key.

### `collectoffset.dbss`

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `collect.dbss` count        |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row   |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                  |
| ------- | ---- | ------------- | -------------------------------------- |
| `+0x00` | u16  | character_key | Row key                                |
| `+0x02` | u32  | data_offset   | Row start + 2, at `name`               |
| `+0x06` | u32  | data_size     | Row size - 2: `66` on client 3474      |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Layout 1

### Row (variable: 48 bytes + name text)

| Offset      | Type   | Field                  | Notes                                                   |
| ----------- | ------ | ---------------------- | ------------------------------------------------------- |
| `+0x00`     | u16    | character_key          | Gathering character                                     |
| `+0x02`     | str16  | name                   | Empty on every row                                      |
| `name+0x00` | u16    | character_key_dup      | Equal to `character_key` in every row                   |
| `name+0x02` | u8     | product_data_type      | Gathering kind, see Product Data Types                  |
| `name+0x03` | u32    | product_time           | `60000` on every row (client 1784)                      |
| `name+0x07` | f32    | product_hp             | `1.0` on every row (client 1784)                        |
| `name+0x0B` | f32    | product_decrease_hp    | `1.0` on every row (client 1784)                        |
| `name+0x0F` | u16    | product_item_drop_key  | `10002` on every row (client 1784)                      |
| `name+0x11` | u8[3]  | collect_tool_types     | Tool per slot; `15` is an empty slot                    |
| `name+0x14` | u16[3] | collect_item_drop_keys | `0` exactly where the slot's tool is `15`               |
| `name+0x1A` | u32    | action_point           | `1` on every row (client 1784)                          |
| `name+0x1E` | u32    | spawn_delay_time       | `0` on every row (client 1784)                          |
| `name+0x22` | u32    | spawn_variable_time    | `0` on every row (client 1784)                          |

The drop keys are u16 here and u32 in Layout 2, and `unknown_name_22` does
not exist yet. Every row is 48 bytes; the index's `data_size` is `46`.

## Field Names

The row is the 2016 `gc::CollectStaticStatus` in member order: `_name`,
`_key`, `_productDataType`, `_productTime`, `_productHp`,
`_productDecreaseHp`, `_productItemDropKey`, `_collectToolType[3]`,
`_collectItemDropKey[3]`, `_actionPoint`, `_spawnDelayTime`,
`_spawnVariableTime`. The 2016 drop keys are u16, as in Layout 1.

The values match the `Collect_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `Index`, the `character_key`: all 606
sheet keys are rows on both clients. An empty sheet cell in a tool slot is
tool `15` with drop key `0` on client 1784, and tool `19` with drop key `0`
on client 3474.

| Field                  | Column                           | Same value (client 1784) | Same value (client 3474) |
| ---------------------- | -------------------------------- | ------------------------ | ------------------------ |
| product_data_type      | `ProductDataType`                | 606 of 606               | 606 of 606               |
| product_time           | `ProductTime`                    | 606 of 606               | 606 of 606               |
| product_hp             | `ProductAllHP`                   | 606 of 606               | 606 of 606               |
| product_decrease_hp    | `ProductDeceraseHP`              | 606 of 606               | 606 of 606               |
| product_item_drop_key  | `ItemDropID`                     | 606 of 606               | 606 of 606               |
| collect_tool_types     | `ToolType_0` to `ToolType_2`     | 606 of 606               | 598 of 606               |
| collect_item_drop_keys | `ItemDropID_0` to `ItemDropID_2` | 606 of 606               | 598 of 606               |
| action_point           | `ActionPoint`                    | 606 of 606               | 606 of 606               |
| spawn_delay_time       | `SpawnDelayTime`                 | 606 of 606               | 606 of 606               |
| spawn_variable_time    | `SpawnVariableTime`              | 606 of 606               | 606 of 606               |

`product_time`, `product_hp`, `product_decrease_hp`, `product_item_drop_key`,
`action_point` and both spawn times hold one value on every row and in the
sheet, so their names rest on the 2016 member order and the Layout 1
positions, not on the values. The eight rows that differ on client 3474 are
`11985` to `11992` (Chanterelle, Red-spotted Amanita, Mesima, Dictyophora,
three Citron Trees, Jadeite): their tool slots or drop groups changed after
client 1784. The client 3474 file adds 107 keys the sheet lacks.

The sheet columns `NeedObjectSkillNo`, `ProductSkillLevel`, `Exp`,
`ProductSkillPointExp` and `IsNotReduce` have no place in the row. `Exp`
and `IsNotReduce` vary in the sheet, and no row byte follows them.

## Product Data Types

The names are the 2016 `gc::ProductDataType::Type` values.

| Value | Name                           | Rows (client 3474) | Tools in the rows                    |
| ----- | ------------------------------ | ------------------ | ------------------------------------ |
| 0     | `eProductData_Default`         | 0                  |                                      |
| 1     | `eProductData_Collect_Base`    | 0                  |                                      |
| 2     | `eProductData_Collect_Collect` | 229                | BareHands, Hoe, Syringe, Pray        |
| 3     | `eProductData_Collect_Farm`    | 0                  |                                      |
| 4     | `eProductData_Collect_Mining`  | 97                 | Pickax, BareHands, ButcheryKnife     |
| 5     | `eProductData_Collect_Purify`  | 0                  |                                      |
| 6     | `eProductData_Collect_Logging` | 246                | Axe, Syringe, Hoe, BareHands, Pickax |
| 7     | `eProductData_Collect_Tanning` | 141                | ButcheryKnife, SkinKnife, Syringe, Hoe, Axe |

## Collect Tool Types

Values `0` to `10` are the 2016 `gc::CollectToolType::Type` values, which end
at `TypeCount = 11`. The client Lua's `CppEnums.CollectToolTypeName`
(`global_define_cpp_enum.luac`) lists the same names in the same order and
adds MassStone, FishingChair, Whip, Oar and, on client 3474, Reserve; it
keys them by engine globals, so their numbers do not show in the Lua.

| Value | Name           | Slots (client 3474) |
| ----- | -------------- | ------------------- |
| 0     | BareHands      | 281                 |
| 2     | Axe            | 151                 |
| 3     | Syringe        | 175                 |
| 4     | Hoe            | 217                 |
| 5     | ButcheryKnife  | 122                 |
| 6     | SkinKnife      | 38                  |
| 7     | Pickax         | 110                 |
| 9     | Pray           | 2                   |
| 19    | Empty slot     | 1,043               |

The empty slot is `15` on client 1784, where the Lua lists 15 names (`0`
BareHands to `14` Oar) followed by `__eCollectToolType_Count`, which puts
`__eCollectToolType_Count` if the values run on from `0`. On client 3474 it
is `19` while the Lua lists 16 names.

## Notes

- On client 3474, 564 of the 713 keys are `characterstatic.dbss`
  characters: 563 with `npc_kind` Collect and `18561` Pine Mushroom with
  `npc_kind` 2. The one Collect character without a row is `501` Test
  Object. The other 149 keys (`10003`, `10146`, `10701` and more) have no
  `characterstatic.dbss` row and no LOC type 6 name.
- 561 keys are the `character_key` of a `collectresourcename.dbss` model;
  152 keys have no model there.
- None of the 564 distinct drop keys on client 3474 is a group of
  `itemmaingroup.bss` or a subgroup of `itemsubgroup.dbss`, so the drops
  cannot be resolved from the client. 481 of them are keys of the
  `ItemMainGroup_Table` sheet of a private server on client 1784, where
  main group `10002` holds subgroup `10002` and three subgroups many
  gathering groups share.
- The tool slot fill follows the gathering kind: logging rows hold Axe and
  Syringe (`11983` Snowfield Cedar Tree), mining rows Pickax, tanning rows
  ButcheryKnife and SkinKnife.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  lists this file with `collectresourcename.dbss` as "gatherable identity
  and internal mesh names; no yields or rates". The row has no rate, but it
  holds the drop group per tool.

## Open Questions

### The 12 Bytes After The Drop Keys

`unknown_name_22` is 12 bytes that Layout 1 does not have, `0` on every row
of client 3474. The 2016 struct has nothing between `_collectItemDropKey`
and `_actionPoint`, and the client 1784 sheet has no column for it.
