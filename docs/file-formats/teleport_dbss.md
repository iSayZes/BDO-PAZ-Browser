# `teleport.dbss` Format

## Purpose

The destinations of teleport buffs: world positions grouped into sections and
keyed within each section. A `buff.dbss` effect type 23 buff stores the
section in `param_1` and the key in `param_2`; using the item moves the player
to that point. The file holds positions only, no names.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes  | Records                          | Row bytes |
| ------ | -------------- | --------------------- | ------ | -------------------------------- | --------- |
| 1      | 1280 and later | `teleport.dbss`       | 11,278 | 625 Record, 6 Section            | 18        |
| 1      | 1280 and later | `teleportoffset.dbss` | 7,524  | 625 Offset Row, 6 Offset Section | 12        |

| Layout | File                  | Known             | Unknown    |
| ------ | --------------------- | ----------------- | ---------- |
| 1      | `teleport.dbss`       | 11,278 B (100.0%) | 0 B (0.0%) |
| 1      | `teleportoffset.dbss` | 7,524 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `8b0dc75fd560`  |
| 3482   | Layout 1 | `8b0dc75fd560`  |
| 3474   | Layout 1 | `8b0dc75fd560`  |
| 3473   | Layout 1 | `8b0dc75fd560`  |
| 3464   | Layout 1 | `8b0dc75fd560`  |
| 3458   | Layout 1 | `8b0dc75fd560`  |
| 3454   | Layout 1 | `8b0dc75fd560`  |
| 3444   | Layout 1 | `8b0dc75fd560`  |
| 3435   | Layout 1 | `8b0dc75fd560`  |
| 3426   | Layout 1 | `8b0dc75fd560`  |
| 3418   | Layout 1 | `8b0dc75fd560`  |
| 3412   | Layout 1 | `8b0dc75fd560`  |
| 3402   | Layout 1 | `8b0dc75fd560`  |
| 3396   | Layout 1 | `8b0dc75fd560`  |
| 3387   | Layout 1 | `8b0dc75fd560`  |
| 3381   | Layout 1 | `8b0dc75fd560`  |
| 3373   | Layout 1 | `8b0dc75fd560`  |
| 3364   | Layout 1 | `8b0dc75fd560`  |
| 3356   | Layout 1 | `8b0dc75fd560`  |
| 3349   | Layout 1 | `8b0dc75fd560`  |
| 3342   | Layout 1 | `8b0dc75fd560`  |
| 3335   | Layout 1 | `8b0dc75fd560`  |
| 3326   | Layout 1 | `8b0dc75fd560`  |
| 3321   | Layout 1 | `8b0dc75fd560`  |
| 3314   | Layout 1 | `8b0dc75fd560`  |
| 3303   | Layout 1 | `8b0dc75fd560`  |
| 3302   | Layout 1 | `8b0dc75fd560`  |
| 3293   | Layout 1 | `8b0dc75fd560`  |
| 3283   | Layout 1 | `8b0dc75fd560`  |
| 3275   | Layout 1 | `8b0dc75fd560`  |
| 3267   | Layout 1 | `8b0dc75fd560`  |
| 3258   | Layout 1 | `8b0dc75fd560`  |
| 3251   | Layout 1 | `8b0dc75fd560`  |
| 3242   | Layout 1 | `8b0dc75fd560`  |
| 3235   | Layout 1 | `8b0dc75fd560`  |
| 3229   | Layout 1 | `8b0dc75fd560`  |
| 3212   | Layout 1 | `8b0dc75fd560`  |
| 3203   | Layout 1 | `8b0dc75fd560`  |
| 3193   | Layout 1 | `8b0dc75fd560`  |
| 3186   | Layout 1 | `8b0dc75fd560`  |
| 3177   | Layout 1 | `8b0dc75fd560`  |
| 3169   | Layout 1 | `8b0dc75fd560`  |
| 3158   | Layout 1 | `8b0dc75fd560`  |
| 3151   | Layout 1 | `8b0dc75fd560`  |
| 3144   | Layout 1 | `8b0dc75fd560`  |
| 3133   | Layout 1 | `8b0dc75fd560`  |
| 3125   | Layout 1 | `8b0dc75fd560`  |
| 3118   | Layout 1 | `8b0dc75fd560`  |
| 3111   | Layout 1 | `8b0dc75fd560`  |
| 3103   | Layout 1 | `8b0dc75fd560`  |
| 3095   | Layout 1 | `8b0dc75fd560`  |
| 3086   | Layout 1 | `8b0dc75fd560`  |
| 3072   | Layout 1 | `8b0dc75fd560`  |
| 3062   | Layout 1 | `8b0dc75fd560`  |
| 3052   | Layout 1 | `8b0dc75fd560`  |
| 3045   | Layout 1 | `8b0dc75fd560`  |
| 3037   | Layout 1 | `8b0dc75fd560`  |
| 3030   | Layout 1 | `8b0dc75fd560`  |
| 3021   | Layout 1 | `8b0dc75fd560`  |
| 3012   | Layout 1 | `8b0dc75fd560`  |
| 3002   | Layout 1 | `8b0dc75fd560`  |
| 2995   | Layout 1 | `8b0dc75fd560`  |
| 2987   | Layout 1 | `8b0dc75fd560`  |
| 2978   | Layout 1 | `8b0dc75fd560`  |
| 2970   | Layout 1 | `8b0dc75fd560`  |
| 2959   | Layout 1 | `8b0dc75fd560`  |
| 2951   | Layout 1 | `8b0dc75fd560`  |
| 2942   | Layout 1 | `8b0dc75fd560`  |
| 2935   | Layout 1 | `8b0dc75fd560`  |
| 2932   | Layout 1 | `8b0dc75fd560`  |
| 2923   | Layout 1 | `8b0dc75fd560`  |
| 2919   | Layout 1 | `8b0dc75fd560`  |
| 2907   | Layout 1 | `8b0dc75fd560`  |
| 2900   | Layout 1 | `8b0dc75fd560`  |
| 2891   | Layout 1 | `8b0dc75fd560`  |
| 2882   | Layout 1 | `8b0dc75fd560`  |
| 2872   | Layout 1 | `8b0dc75fd560`  |
| 2863   | Layout 1 | `8b0dc75fd560`  |
| 2855   | Layout 1 | `8b0dc75fd560`  |
| 2849   | Layout 1 | `8b0dc75fd560`  |
| 2844   | Layout 1 | `8b0dc75fd560`  |
| 2834   | Layout 1 | `8b0dc75fd560`  |
| 2825   | Layout 1 | `8b0dc75fd560`  |
| 2819   | Layout 1 | `8b0dc75fd560`  |
| 2811   | Layout 1 | `8b0dc75fd560`  |
| 2803   | Layout 1 | `8b0dc75fd560`  |
| 2794   | Layout 1 | `8b0dc75fd560`  |
| 2783   | Layout 1 | `8b0dc75fd560`  |
| 2774   | Layout 1 | `8b0dc75fd560`  |
| 2765   | Layout 1 | `8b0dc75fd560`  |
| 2756   | Layout 1 | `8b0dc75fd560`  |
| 2750   | Layout 1 | `8b0dc75fd560`  |
| 2743   | Layout 1 | `8b0dc75fd560`  |
| 2736   | Layout 1 | `8b0dc75fd560`  |
| 2726   | Layout 1 | `8b0dc75fd560`  |
| 2717   | Layout 1 | `8b0dc75fd560`  |
| 2709   | Layout 1 | `8b0dc75fd560`  |
| 2703   | Layout 1 | `8b0dc75fd560`  |
| 2695   | Layout 1 | `8b0dc75fd560`  |
| 2684   | Layout 1 | `8b0dc75fd560`  |
| 2672   | Layout 1 | `8b0dc75fd560`  |
| 2665   | Layout 1 | `8b0dc75fd560`  |
| 2657   | Layout 1 | `8b0dc75fd560`  |
| 2649   | Layout 1 | `8b0dc75fd560`  |
| 2644   | Layout 1 | `8b0dc75fd560`  |
| 2637   | Layout 1 | `8b0dc75fd560`  |
| 2629   | Layout 1 | `8b0dc75fd560`  |
| 2619   | Layout 1 | `8b0dc75fd560`  |
| 2612   | Layout 1 | `8b0dc75fd560`  |
| 2606   | Layout 1 | `8b0dc75fd560`  |
| 2602   | Layout 1 | `8b0dc75fd560`  |
| 2601   | Layout 1 | `8b0dc75fd560`  |
| 2592   | Layout 1 | `8b0dc75fd560`  |
| 2583   | Layout 1 | `8b0dc75fd560`  |
| 2575   | Layout 1 | `8b0dc75fd560`  |
| 2567   | Layout 1 | `8b0dc75fd560`  |
| 2560   | Layout 1 | `8b0dc75fd560`  |
| 2553   | Layout 1 | `8b0dc75fd560`  |
| 2545   | Layout 1 | `8b0dc75fd560`  |
| 2538   | Layout 1 | `8b0dc75fd560`  |
| 2529   | Layout 1 | `8b0dc75fd560`  |
| 2519   | Layout 1 | `8b0dc75fd560`  |
| 2513   | Layout 1 | `8b0dc75fd560`  |
| 2510   | Layout 1 | `8b0dc75fd560`  |
| 2507   | Layout 1 | `8b0dc75fd560`  |
| 2503   | Layout 1 | `8b0dc75fd560`  |
| 2498   | Layout 1 | `8b0dc75fd560`  |
| 2492   | Layout 1 | `8b0dc75fd560`  |
| 2487   | Layout 1 | `8b0dc75fd560`  |
| 2480   | Layout 1 | `8b0dc75fd560`  |
| 2474   | Layout 1 | `8b0dc75fd560`  |
| 2468   | Layout 1 | `8b0dc75fd560`  |
| 2460   | Layout 1 | `8b0dc75fd560`  |
| 2453   | Layout 1 | `8b0dc75fd560`  |
| 2444   | Layout 1 | `8b0dc75fd560`  |
| 2438   | Layout 1 | `8b0dc75fd560`  |
| 2434   | Layout 1 | `8b0dc75fd560`  |
| 2429   | Layout 1 | `8b0dc75fd560`  |
| 2421   | Layout 1 | `8b0dc75fd560`  |
| 2414   | Layout 1 | `8b0dc75fd560`  |
| 2407   | Layout 1 | `8b0dc75fd560`  |
| 2401   | Layout 1 | `8b0dc75fd560`  |
| 2397   | Layout 1 | `8b0dc75fd560`  |
| 2393   | Layout 1 | `8b0dc75fd560`  |
| 2384   | Layout 1 | `8b0dc75fd560`  |
| 2378   | Layout 1 | `8b0dc75fd560`  |
| 2372   | Layout 1 | `8b0dc75fd560`  |
| 2358   | Layout 1 | `8b0dc75fd560`  |
| 2352   | Layout 1 | `8b0dc75fd560`  |
| 2347   | Layout 1 | `8b0dc75fd560`  |
| 2343   | Layout 1 | `8b0dc75fd560`  |
| 2335   | Layout 1 | `8b0dc75fd560`  |
| 2327   | Layout 1 | `8b0dc75fd560`  |
| 2324   | Layout 1 | `8b0dc75fd560`  |
| 2319   | Layout 1 | `8b0dc75fd560`  |
| 2313   | Layout 1 | `8b0dc75fd560`  |
| 2308   | Layout 1 | `8b0dc75fd560`  |
| 2302   | Layout 1 | `8b0dc75fd560`  |
| 2295   | Layout 1 | `8b0dc75fd560`  |
| 2290   | Layout 1 | `8b0dc75fd560`  |
| 2284   | Layout 1 | `8b0dc75fd560`  |
| 2276   | Layout 1 | `8b0dc75fd560`  |
| 2269   | Layout 1 | `8b0dc75fd560`  |
| 2259   | Layout 1 | `8b0dc75fd560`  |
| 2250   | Layout 1 | `8b0dc75fd560`  |
| 2243   | Layout 1 | `8b0dc75fd560`  |
| 2235   | Layout 1 | `8b0dc75fd560`  |
| 2229   | Layout 1 | `8b0dc75fd560`  |
| 2224   | Layout 1 | `8b0dc75fd560`  |
| 2218   | Layout 1 | `8b0dc75fd560`  |
| 2215   | Layout 1 | `8b0dc75fd560`  |
| 2207   | Layout 1 | `8b0dc75fd560`  |
| 2203   | Layout 1 | `8b0dc75fd560`  |
| 2196   | Layout 1 | `8b0dc75fd560`  |
| 2192   | Layout 1 | `8b0dc75fd560`  |
| 2189   | Layout 1 | `8b0dc75fd560`  |
| 2183   | Layout 1 | `8b0dc75fd560`  |
| 2179   | Layout 1 | `8b0dc75fd560`  |
| 2171   | Layout 1 | `8b0dc75fd560`  |
| 2163   | Layout 1 | `8b0dc75fd560`  |
| 2156   | Layout 1 | `8b0dc75fd560`  |
| 2151   | Layout 1 | `8b0dc75fd560`  |
| 2147   | Layout 1 | `8b0dc75fd560`  |
| 2142   | Layout 1 | `8b0dc75fd560`  |
| 2138   | Layout 1 | `8b0dc75fd560`  |
| 2134   | Layout 1 | `8b0dc75fd560`  |
| 2130   | Layout 1 | `8b0dc75fd560`  |
| 2122   | Layout 1 | `8b0dc75fd560`  |
| 2107   | Layout 1 | `8b0dc75fd560`  |
| 2098   | Layout 1 | `8b0dc75fd560`  |
| 2089   | Layout 1 | `8b0dc75fd560`  |
| 2081   | Layout 1 | `8b0dc75fd560`  |
| 2073   | Layout 1 | `8b0dc75fd560`  |
| 2067   | Layout 1 | `8b0dc75fd560`  |
| 2063   | Layout 1 | `8b0dc75fd560`  |
| 2059   | Layout 1 | `8b0dc75fd560`  |
| 2052   | Layout 1 | `8b0dc75fd560`  |
| 2044   | Layout 1 | `8b0dc75fd560`  |
| 2039   | Layout 1 | `8b0dc75fd560`  |
| 2032   | Layout 1 | `8b0dc75fd560`  |
| 2025   | Layout 1 | `8b0dc75fd560`  |
| 2011   | Layout 1 | `8b0dc75fd560`  |
| 2005   | Layout 1 | `8b0dc75fd560`  |
| 2000   | Layout 1 | `8b0dc75fd560`  |
| 1996   | Layout 1 | `8b0dc75fd560`  |
| 1991   | Layout 1 | `8b0dc75fd560`  |
| 1985   | Layout 1 | `8b0dc75fd560`  |
| 1980   | Layout 1 | `8b0dc75fd560`  |
| 1969   | Layout 1 | `8b0dc75fd560`  |
| 1964   | Layout 1 | `8b0dc75fd560`  |
| 1958   | Layout 1 | `8b0dc75fd560`  |
| 1950   | Layout 1 | `8b0dc75fd560`  |
| 1945   | Layout 1 | `8b0dc75fd560`  |
| 1937   | Layout 1 | `8b0dc75fd560`  |
| 1933   | Layout 1 | `8b0dc75fd560`  |
| 1927   | Layout 1 | `8b0dc75fd560`  |
| 1921   | Layout 1 | `8b0dc75fd560`  |
| 1914   | Layout 1 | `8b0dc75fd560`  |
| 1908   | Layout 1 | `8b0dc75fd560`  |
| 1897   | Layout 1 | `8b0dc75fd560`  |
| 1892   | Layout 1 | `8b0dc75fd560`  |
| 1886   | Layout 1 | `8b0dc75fd560`  |
| 1881   | Layout 1 | `8b0dc75fd560`  |
| 1871   | Layout 1 | `8b0dc75fd560`  |
| 1866   | Layout 1 | `8b0dc75fd560`  |
| 1862   | Layout 1 | `8b0dc75fd560`  |
| 1854   | Layout 1 | `8b0dc75fd560`  |
| 1846   | Layout 1 | `8b0dc75fd560`  |
| 1838   | Layout 1 | `8b0dc75fd560`  |
| 1832   | Layout 1 | `8b0dc75fd560`  |
| 1826   | Layout 1 | `8b0dc75fd560`  |
| 1822   | Layout 1 | `8b0dc75fd560`  |
| 1818   | Layout 1 | `8b0dc75fd560`  |
| 1804   | Layout 1 | `8b0dc75fd560`  |
| 1794   | Layout 1 | `8b0dc75fd560`  |
| 1790   | Layout 1 | `8b0dc75fd560`  |
| 1784   | Layout 1 | `8b0dc75fd560`  |
| 1774   | Layout 1 | `8b0dc75fd560`  |
| 1771   | Layout 1 | `8b0dc75fd560`  |
| 1762   | Layout 1 | `8b0dc75fd560`  |
| 1759   | Layout 1 | `8b0dc75fd560`  |
| 1754   | Layout 1 | `8b0dc75fd560`  |
| 1749   | Layout 1 | `8b0dc75fd560`  |
| 1743   | Layout 1 | `8b0dc75fd560`  |
| 1737   | Layout 1 | `8b0dc75fd560`  |
| 1731   | Layout 1 | `8b0dc75fd560`  |
| 1725   | Layout 1 | `8b0dc75fd560`  |
| 1717   | Layout 1 | `8b0dc75fd560`  |
| 1710   | Layout 1 | `8b0dc75fd560`  |
| 1704   | Layout 1 | `8b0dc75fd560`  |
| 1698   | Layout 1 | `8b0dc75fd560`  |
| 1690   | Layout 1 | `8b0dc75fd560`  |
| 1685   | Layout 1 | `8b0dc75fd560`  |
| 1680   | Layout 1 | `8b0dc75fd560`  |
| 1674   | Layout 1 | `8b0dc75fd560`  |
| 1668   | Layout 1 | `8b0dc75fd560`  |
| 1659   | Layout 1 | `8b0dc75fd560`  |
| 1649   | Layout 1 | `8b0dc75fd560`  |
| 1642   | Layout 1 | `8b0dc75fd560`  |
| 1636   | Layout 1 | `8b0dc75fd560`  |
| 1628   | Layout 1 | `8b0dc75fd560`  |
| 1622   | Layout 1 | `8b0dc75fd560`  |
| 1614   | Layout 1 | `8b0dc75fd560`  |
| 1608   | Layout 1 | `8b0dc75fd560`  |
| 1602   | Layout 1 | `8b0dc75fd560`  |
| 1598   | Layout 1 | `8b0dc75fd560`  |
| 1594   | Layout 1 | `8b0dc75fd560`  |
| 1590   | Layout 1 | `8b0dc75fd560`  |
| 1587   | Layout 1 | `8b0dc75fd560`  |
| 1584   | Layout 1 | `8b0dc75fd560`  |
| 1579   | Layout 1 | `8b0dc75fd560`  |
| 1572   | Layout 1 | `8b0dc75fd560`  |
| 1565   | Layout 1 | `8b0dc75fd560`  |
| 1559   | Layout 1 | `8b0dc75fd560`  |
| 1554   | Layout 1 | `8b0dc75fd560`  |
| 1547   | Layout 1 | `8b0dc75fd560`  |
| 1537   | Layout 1 | `8b0dc75fd560`  |
| 1529   | Layout 1 | `8b0dc75fd560`  |
| 1524   | Layout 1 | `8b0dc75fd560`  |
| 1519   | Layout 1 | `8b0dc75fd560`  |
| 1509   | Layout 1 | `8b0dc75fd560`  |
| 1506   | Layout 1 | `8b0dc75fd560`  |
| 1504   | Layout 1 | `8b0dc75fd560`  |
| 1500   | Layout 1 | `8b0dc75fd560`  |
| 1493   | Layout 1 | `8b0dc75fd560`  |
| 1489   | Layout 1 | `8b0dc75fd560`  |
| 1485   | Layout 1 | `8b0dc75fd560`  |
| 1481   | Layout 1 | `8b0dc75fd560`  |
| 1474   | Layout 1 | `8b0dc75fd560`  |
| 1466   | Layout 1 | `8b0dc75fd560`  |
| 1462   | Layout 1 | `8b0dc75fd560`  |
| 1459   | Layout 1 | `8b0dc75fd560`  |
| 1453   | Layout 1 | `8b0dc75fd560`  |
| 1450   | Layout 1 | `8b0dc75fd560`  |
| 1445   | Layout 1 | `8b0dc75fd560`  |
| 1439   | Layout 1 | `8b0dc75fd560`  |
| 1433   | Layout 1 | `8b0dc75fd560`  |
| 1430   | Layout 1 | `8b0dc75fd560`  |
| 1426   | Layout 1 | `8b0dc75fd560`  |
| 1421   | Layout 1 | `8b0dc75fd560`  |
| 1417   | Layout 1 | `8b0dc75fd560`  |
| 1416   | Layout 1 | `8b0dc75fd560`  |
| 1409   | Layout 1 | `8b0dc75fd560`  |
| 1405   | Layout 1 | `8b0dc75fd560`  |
| 1401   | Layout 1 | `8b0dc75fd560`  |
| 1396   | Layout 1 | `8b0dc75fd560`  |
| 1391   | Layout 1 | `8b0dc75fd560`  |
| 1390   | Layout 1 | `8b0dc75fd560`  |
| 1386   | Layout 1 | `8b0dc75fd560`  |
| 1381   | Layout 1 | `8b0dc75fd560`  |
| 1379   | Layout 1 | `8b0dc75fd560`  |
| 1372   | Layout 1 | `8b0dc75fd560`  |
| 1366   | Layout 1 | `8b0dc75fd560`  |
| 1364   | Layout 1 | `8b0dc75fd560`  |
| 1363   | Layout 1 | `8b0dc75fd560`  |
| 1360   | Layout 1 | `8b0dc75fd560`  |
| 1358   | Layout 1 | `8b0dc75fd560`  |
| 1355   | Layout 1 | `8b0dc75fd560`  |
| 1351   | Layout 1 | `8b0dc75fd560`  |
| 1348   | Layout 1 | `8b0dc75fd560`  |
| 1346   | Layout 1 | `8b0dc75fd560`  |
| 1341   | Layout 1 | `8b0dc75fd560`  |
| 1340   | Layout 1 | `8b0dc75fd560`  |
| 1338   | Layout 1 | `8b0dc75fd560`  |
| 1335   | Layout 1 | `8b0dc75fd560`  |
| 1333   | Layout 1 | `8b0dc75fd560`  |
| 1329   | Layout 1 | `8b0dc75fd560`  |
| 1327   | Layout 1 | `8b0dc75fd560`  |
| 1324   | Layout 1 | `8b0dc75fd560`  |
| 1321   | Layout 1 | `8b0dc75fd560`  |
| 1319   | Layout 1 | `8b0dc75fd560`  |
| 1318   | Layout 1 | `8b0dc75fd560`  |
| 1316   | Layout 1 | `8b0dc75fd560`  |
| 1313   | Layout 1 | `8b0dc75fd560`  |
| 1311   | Layout 1 | `8b0dc75fd560`  |
| 1309   | Layout 1 | `8b0dc75fd560`  |
| 1304   | Layout 1 | `8b0dc75fd560`  |
| 1292   | Layout 1 | `8b0dc75fd560`  |
| 1286   | Layout 1 | `8b0dc75fd560`  |
| 1280   | Layout 1 | `8b0dc75fd560`  |
| 1276   | No file  | `8b0dc75fd560`  |
| 1267   | No file  | `8b0dc75fd560`  |
| 1261   | No file  | `8b0dc75fd560`  |
| 1256   | No file  | `8b0dc75fd560`  |
| 1250   | No file  | `8b0dc75fd560`  |
| 1246   | No file  | `8b0dc75fd560`  |
| 1239   | No file  | `8b0dc75fd560`  |
| 1230   | No file  | `8b0dc75fd560`  |
| 1226   | No file  | `8b0dc75fd560`  |
| 1220   | No file  | `8b0dc75fd560`  |
| 1217   | No file  | `8b0dc75fd560`  |
| 1211   | No file  | `8b0dc75fd560`  |
| 1210   | No file  | `8b0dc75fd560`  |
| 1208   | No file  | `8b0dc75fd560`  |
| 1203   | No file  | `8b0dc75fd560`  |
| 1197   | No file  | `8b0dc75fd560`  |
| 1194   | No file  | `8b0dc75fd560`  |
| 1192   | No file  | `8b0dc75fd560`  |
| 1187   | No file  | `8b0dc75fd560`  |
| 1183   | No file  | `8b0dc75fd560`  |
| 1177   | No file  | `8b0dc75fd560`  |
| 1173   | No file  | `8b0dc75fd560`  |
| 1167   | No file  | `8b0dc75fd560`  |
| 1164   | No file  | `8b0dc75fd560`  |
| 1156   | No file  | `8b0dc75fd560`  |
| 1149   | No file  | `8b0dc75fd560`  |
| 1144   | No file  | `8b0dc75fd560`  |
| 1137   | No file  | `8b0dc75fd560`  |
| 1132   | No file  | `8b0dc75fd560`  |
| 1127   | No file  | `8b0dc75fd560`  |
| 1122   | No file  | `8b0dc75fd560`  |
| 1118   | No file  | `8b0dc75fd560`  |
| 1114   | No file  | `8b0dc75fd560`  |
| 1109   | No file  | `8b0dc75fd560`  |
| 1102   | No file  | `8b0dc75fd560`  |
| 1096   | No file  | `8b0dc75fd560`  |
| 1088   | No file  | `8b0dc75fd560`  |
| 1081   | No file  | `8b0dc75fd560`  |
| 1076   | No file  | `8b0dc75fd560`  |
| 1069   | No file  | `8b0dc75fd560`  |
| 1064   | No file  | `8b0dc75fd560`  |
| 1058   | No file  | `8b0dc75fd560`  |
| 1051   | No file  | `8b0dc75fd560`  |
| 1044   | No file  | `8b0dc75fd560`  |
| 1036   | No file  | `8b0dc75fd560`  |
| 1026   | No file  | `8b0dc75fd560`  |
| 1016   | No file  | `8b0dc75fd560`  |
| 1009   | No file  | `8b0dc75fd560`  |
| 1005   | No file  | `8b0dc75fd560`  |
| 1000   | No file  | `8b0dc75fd560`  |
| 998    | No file  | `8b0dc75fd560`  |
| 990    | No file  | `8b0dc75fd560`  |
| 979    | No file  | `8b0dc75fd560`  |
| 972    | No file  | `8b0dc75fd560`  |
| 963    | No file  | `8b0dc75fd560`  |
| 955    | No file  | `8b0dc75fd560`  |
| 946    | No file  | `8b0dc75fd560`  |
| 938    | No file  | `8b0dc75fd560`  |
| 927    | No file  | `8b0dc75fd560`  |
| 911    | No file  | `8b0dc75fd560`  |
| 904    | No file  | `8b0dc75fd560`  |
| 899    | No file  | `8b0dc75fd560`  |
| 894    | No file  | `8b0dc75fd560`  |
| 885    | No file  | `8b0dc75fd560`  |
| 879    | No file  | `8b0dc75fd560`  |
| 872    | No file  | `8b0dc75fd560`  |
| 864    | No file  | `8b0dc75fd560`  |
| 855    | No file  | `8b0dc75fd560`  |
| 853    | No file  | `8b0dc75fd560`  |
| 845    | No file  | `8b0dc75fd560`  |
| 837    | No file  | `8b0dc75fd560`  |
| 829    | No file  | `8b0dc75fd560`  |
| 822    | No file  | `8b0dc75fd560`  |
| 814    | No file  | `8b0dc75fd560`  |
| 805    | No file  | `8b0dc75fd560`  |
| 794    | No file  | `8b0dc75fd560`  |
| 787    | No file  | `8b0dc75fd560`  |
| 780    | No file  | `8b0dc75fd560`  |
| 771    | No file  | `8b0dc75fd560`  |
| 760    | No file  | `8b0dc75fd560`  |
| 748    | No file  | `8b0dc75fd560`  |
| 741    | No file  | `8b0dc75fd560`  |
| 736    | No file  | `8b0dc75fd560`  |
| 731    | No file  | `8b0dc75fd560`  |
| 723    | No file  | `8b0dc75fd560`  |
| 711    | No file  | `8b0dc75fd560`  |
| 707    | No file  | `8b0dc75fd560`  |
| 697    | No file  | `8b0dc75fd560`  |
| 689    | No file  | `8b0dc75fd560`  |
| 683    | No file  | `8b0dc75fd560`  |
| 678    | No file  | `8b0dc75fd560`  |
| 670    | No file  | `8b0dc75fd560`  |
| 661    | No file  | `8b0dc75fd560`  |
| 656    | No file  | `8b0dc75fd560`  |
| 652    | No file  | `8b0dc75fd560`  |
| 643    | No file  | `8b0dc75fd560`  |
| 637    | No file  | `8b0dc75fd560`  |
| 630    | No file  | `8b0dc75fd560`  |
| 627    | No file  | `8b0dc75fd560`  |
| 621    | No file  | `8b0dc75fd560`  |
| 617    | No file  | `8b0dc75fd560`  |
| 615    | No file  | `8b0dc75fd560`  |
| 606    | No file  | `8b0dc75fd560`  |
| 599    | No file  | `8b0dc75fd560`  |
| 592    | No file  | `8b0dc75fd560`  |
| 586    | No file  | `8b0dc75fd560`  |
| 577    | No file  | `8b0dc75fd560`  |
| 569    | No file  | `8b0dc75fd560`  |
| 561    | No file  | `8b0dc75fd560`  |
| 554    | No file  | `8b0dc75fd560`  |
| 542    | No file  | `8b0dc75fd560`  |
| 532    | No file  | `8b0dc75fd560`  |
| 531    | No file  | `8b0dc75fd560`  |
| 526    | No file  | `8b0dc75fd560`  |
| 521    | No file  | `8b0dc75fd560`  |
| 517    | No file  | `8b0dc75fd560`  |
| 510    | No file  | `8b0dc75fd560`  |
| 508    | No file  | `8b0dc75fd560`  |
| 504    | No file  | `8b0dc75fd560`  |
| 497    | No file  | `8b0dc75fd560`  |
| 491    | No file  | `8b0dc75fd560`  |
| 485    | No file  | `8b0dc75fd560`  |
| 478    | No file  | `8b0dc75fd560`  |
| 472    | No file  | `8b0dc75fd560`  |
| 466    | No file  | `8b0dc75fd560`  |
| 457    | No file  | `8b0dc75fd560`  |
| 452    | No file  | `8b0dc75fd560`  |
| 449    | No file  | `8b0dc75fd560`  |
| 435    | No file  | `8b0dc75fd560`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                        |
| ---------------------- | -------- | ----------------------------------------------------------- |
| `teleportoffset.dbss`  | Optional | Positional index of the records, see below; not needed to read this file |
| `mapdata_realexplore2.bwp` | Optional | Worldmap nodes in the same coordinate frame, to place a point |
| `buff.dbss`            | Optional | The type 23 buffs that teleport to each point, through the `TELEPORT_BUFFS` lookup index |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The file is a list of sections, each a counted run of fixed 18-byte records.
It walks exactly to its last byte on client 3458 (11,206 bytes).

| Offset  | Type                   | Field         | Notes                                       |
| ------- | ---------------------- | ------------- | ------------------------------------------- |
| `+0x00` | u32                    | section_count | `6` on client 3458                          |
| `+0x04` | Section[section_count] | sections      | Sections in order 0, 1, 2, ...; see Section |

### Section (variable: 4 bytes + records)

| Offset  | Type          | Field   | Notes                             |
| ------- | ------------- | ------- | --------------------------------- |
| `+0x00` | u32           | count   | Number of records; `0` is allowed |
| `+0x04` | Record[count] | records | See Record                        |

### Record (18 bytes)

| Offset  | Type | Field       | Notes |
| ------- | ---- | ----------- | ----- |
| `+0x00` | u32  | key         | Unique within its section, not across sections; not sorted in section 0 and 5 (section 0 runs 0 to 1034 over 426 records) |
| `+0x04` | u8   | section     | Always the index of the section the record sits in |
| `+0x05` | f32  | x           | World position, the frame of `exploration.bss` and `mapdata_realexplore2.bwp` (centimetres) |
| `+0x09` | f32  | y           | Height |
| `+0x0D` | f32  | z           | |
| `+0x11` | u8   | destination | `0` on 612 of 621 records (client 3474); see Field Names |

### `teleportoffset.dbss`

The same sections as `teleport.dbss`, in the same order, each a counted list
of 12-byte rows. Unlike `teleport.dbss` it has no section count: the first
section starts at `+0x00` and the sections run to the end of the file, which
they fill exactly (7,476 bytes).

| Offset  | Type                  | Field    | Notes                                         |
| ------- | --------------------- | -------- | --------------------------------------------- |
| `+0x00` | Offset Section[..end] | sections | Up to the end of the file; see Offset Section |

### Offset Section (variable: 4 bytes + rows)

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the record count of the same section |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field  | Notes |
| ------- | ---- | ------ | ----- |
| `+0x00` | u32  | index  | Position of the record within its section, `0` to `count - 1` |
| `+0x04` | u32  | offset | `teleport.dbss` offset of that record: section start + `18 * index` on every row |
| `+0x08` | u32  | size   | Always `18` |

The rows are in a hash order (section 0 starts `399, 0, 1, 393, 2, 3, 387,
4`), and `index` is a position, not the record's `key`. The two agree only
where a section's keys run `0` to `count - 1` in order (sections 1 and 2).
Read as a key, the section 0 rows point 14.5 km (median) away from the places
the buff texts name, against 73 m through the inline keys, so readers look
records up by the inline `key` and do not need this file.

## Sections on Client 3458

| Section | Records | Used by (buff type 23, Korean names) |
| ------- | ------: | ------------------------------------ |
| 0       | 426     | 470 buffs: travel items and quest moves, `발자국 : 잔해의 해안` ("footprints: Shore of Ruins", `Move to Shore of Ruins`), `출입 통과 : 오르의 요람` ("entry pass: Orze's Cradle") |
| 1       | 9       | 1 buff, `발렌시아 파트2 던전 무작위 순간이동` ("Valencia part 2 dungeon random teleport") |
| 2       | 3       | No buff                              |
| 3       | 0       | 1 buff, `단방향(마을) 귀환석` ("one-way (town) return stone"), key 0 |
| 4       | 0       | 1 buff, `벨리아 마을 귀환석` ("Velia town return stone"), key 5 |
| 5       | 183     | 181 buffs: boss rooms, event gimmicks and unstuck moves, `하둠 보스용 블랙홀 1번` ("Hadum boss black hole 1"), `이벤트 선물상자 끼이는 현상 방지 텔레포트` ("teleport against getting stuck in the event gift box") |

652 of the 654 type 23 buffs name a record that exists; the other two are the
return stones on the empty sections 3 and 4, whose destination is resolved
elsewhere. 22 of the 621 records are used by no buff.

## Field Names

The record is the `Teleport_Table` sheet of a private server on client
1784, with the columns `Type`, `Index`, `PositionX`, `PositionY`,
`PositionZ` and `Destination`. That server's dump (`Instance_dumpFull.exe`)
loads the sheet into an 18-byte struct in record order (VA `0x1409b8f83` to
`0x1409b912e`): `Type` as a u8 at `+4` (the `section` byte), the three
positions as f32 at `+8` to `+0x10` and `Destination` as a u8 at `+0x14`,
which packs to `+0x11` in the file. On the 167 sheet rows, matched on
section and position in the section, the private server's own
`teleport.dbss` has the same position and the same `destination` on all 167;
the four non-zero values (keys 1, 2, 23 and 24 store `1`, `2`, `1`, `2`)
match client 3474 too.

The teleport buff effect of that server (VA `0x140dbcf20`) reads
`destination` only for section 0. On `1` it stores the point's position as
the player's saved position and sets a flag; on `2` it clears the flag and
the position. Any other value is a plain move. The keys that set `1` are
buffs to the Ancient Stone Chamber, the ones that set `2` lead back to
Valencia and the Gyfin Rhasia Temple.

On client 1784 the server writes `0xFFFFFFFF` for `key` and drops the
sheet's `Index`: all 170 records of that build store `0xFFFFFFFF`, so a
1784 record is found by its position in the section. On client 3474 `key`
equals the sheet's `Index` on the 148 shared rows whose position did not
move.

## Notes

- Positions were checked against the type 23 buffs whose English text names
  a worldmap node: `Footprints: Flower-sunken Swamp`, `Mongryong's Exile` and
  `Martial God Tournament` lie within 1 m of their node, `Holbon Entrance`
  3 m, and 8 of 14 such points lie within 100 m. Points inside instanced
  areas (Orzekea, `Instantly teleport to Orze's Garden`) lie kilometres from
  any node.
- `mapdata_realteleport.xml` / `.bwp` in `gamecommondata/waypoint/` is a
  different set: its 293 waypoints have numeric names, and only 3 lie within
  5 m of a teleport point.
- `magnuseasyteleport.bss` (1.1 KB, PABR) holds the Abyss One Magnus teleport
  map; not read here.

## Open Questions

### What do `destination` values above 2 do?

Five section 0 records of client 3474 store `85`, `90`, `99`, `32` and `96`
(keys 260, 231, 253, 257 and 259: an indoor point after a street battle,
Muzgar Village, a watchtower, the Northern Wheat Plantation and a troll
defence base). None of these keys exists on client 1784, whose server reads
only `1` and `2` (Field Names) and moves the player normally for any other
value. What the newer server does with them is open.

### What do sections 1 and 2 serve?

Section 1 has one buff, a random teleport in the second Valencia dungeon,
whose `param_2` `0` picks one of nine points; section 2 has no buff. Some
other system (a dungeon script, an action chart) may pick points from them.
