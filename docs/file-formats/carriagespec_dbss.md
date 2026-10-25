# `carriagespec.dbss` Format

## Purpose

One row per transport carriage type of the warehouse transport window
(`ToClient_NewDelivery*` in the client Lua): travel speed, loadage, weight
limits, base fee and fee per weight, and which kinds of trade goods it may
carry. On client 3474 the file has 2 rows, carriage keys `1` and `2`.
Companion `carriagespecoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes | Records      | Row bytes |
| ------ | -------------- | ------------------------- | ----- | ------------ | --------- |
| 1      | 1309 and later | `carriagespec.dbss`       | 84    | 2 Row        | 40        |
| 1      | 1309 and later | `carriagespecoffset.dbss` | 22    | 2 Offset Row | 9         |

| Layout | File                      | Known         | Unknown    |
| ------ | ------------------------- | ------------- | ---------- |
| 1      | `carriagespec.dbss`       | 84 B (100.0%) | 0 B (0.0%) |
| 1      | `carriagespecoffset.dbss` | 22 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `f50c59491b27`  |
| 3482   | Layout 1             | `f50c59491b27`  |
| 3474   | Layout 1             | `f50c59491b27`  |
| 3473   | Layout 1             | `f50c59491b27`  |
| 3464   | Layout 1             | `f50c59491b27`  |
| 3458   | Layout 1             | `f50c59491b27`  |
| 3454   | Layout 1             | `f50c59491b27`  |
| 3444   | Layout 1             | `f50c59491b27`  |
| 3435   | Layout 1             | `f50c59491b27`  |
| 3426   | Layout 1             | `f50c59491b27`  |
| 3418   | Layout 1             | `f50c59491b27`  |
| 3412   | Layout 1             | `f50c59491b27`  |
| 3402   | Layout 1             | `f50c59491b27`  |
| 3396   | Layout 1             | `f50c59491b27`  |
| 3387   | Layout 1             | `f50c59491b27`  |
| 3381   | Layout 1             | `f50c59491b27`  |
| 3373   | Layout 1             | `f50c59491b27`  |
| 3364   | Layout 1             | `f50c59491b27`  |
| 3356   | Layout 1             | `f50c59491b27`  |
| 3349   | Layout 1             | `f50c59491b27`  |
| 3342   | Layout 1             | `f50c59491b27`  |
| 3335   | Layout 1             | `f50c59491b27`  |
| 3326   | Layout 1             | `f50c59491b27`  |
| 3321   | Layout 1             | `f50c59491b27`  |
| 3314   | Layout 1             | `f50c59491b27`  |
| 3303   | Layout 1             | `f50c59491b27`  |
| 3302   | Layout 1             | `f50c59491b27`  |
| 3293   | Layout 1             | `f50c59491b27`  |
| 3283   | Layout 1             | `f50c59491b27`  |
| 3275   | Layout 1             | `f50c59491b27`  |
| 3267   | Layout 1             | `f50c59491b27`  |
| 3258   | Layout 1             | `f50c59491b27`  |
| 3251   | Layout 1             | `f50c59491b27`  |
| 3242   | Layout 1             | `f50c59491b27`  |
| 3235   | Layout 1             | `f50c59491b27`  |
| 3229   | Layout 1             | `f50c59491b27`  |
| 3212   | Layout 1             | `f50c59491b27`  |
| 3203   | Layout 1             | `f50c59491b27`  |
| 3193   | Layout 1             | `f50c59491b27`  |
| 3186   | Layout 1             | `f50c59491b27`  |
| 3177   | Layout 1             | `f50c59491b27`  |
| 3169   | Layout 1             | `f50c59491b27`  |
| 3158   | Layout 1             | `f50c59491b27`  |
| 3151   | Layout 1             | `f50c59491b27`  |
| 3144   | Layout 1             | `f50c59491b27`  |
| 3133   | Layout 1             | `f50c59491b27`  |
| 3125   | Layout 1             | `f50c59491b27`  |
| 3118   | Layout 1             | `f50c59491b27`  |
| 3111   | Layout 1             | `f50c59491b27`  |
| 3103   | Layout 1             | `f50c59491b27`  |
| 3095   | Layout 1             | `f50c59491b27`  |
| 3086   | Layout 1             | `f50c59491b27`  |
| 3072   | Layout 1             | `f50c59491b27`  |
| 3062   | Layout 1             | `f50c59491b27`  |
| 3052   | Layout 1             | `f50c59491b27`  |
| 3045   | Layout 1             | `f50c59491b27`  |
| 3037   | Layout 1             | `f50c59491b27`  |
| 3030   | Layout 1             | `f50c59491b27`  |
| 3021   | Layout 1             | `f50c59491b27`  |
| 3012   | Layout 1             | `f50c59491b27`  |
| 3002   | Layout 1             | `f50c59491b27`  |
| 2995   | Layout 1             | `f50c59491b27`  |
| 2987   | Layout 1             | `f50c59491b27`  |
| 2978   | Layout 1             | `f50c59491b27`  |
| 2970   | Layout 1             | `f50c59491b27`  |
| 2959   | Layout 1             | `f50c59491b27`  |
| 2951   | Layout 1             | `f50c59491b27`  |
| 2942   | Layout 1             | `f50c59491b27`  |
| 2935   | Layout 1             | `f50c59491b27`  |
| 2932   | Layout 1             | `f50c59491b27`  |
| 2923   | Layout 1             | `f50c59491b27`  |
| 2919   | Layout 1             | `f50c59491b27`  |
| 2907   | Layout 1             | `f50c59491b27`  |
| 2900   | Layout 1             | `f50c59491b27`  |
| 2891   | Layout 1             | `f50c59491b27`  |
| 2882   | Layout 1             | `f50c59491b27`  |
| 2872   | Layout 1             | `f50c59491b27`  |
| 2863   | Layout 1             | `f50c59491b27`  |
| 2855   | Layout 1             | `f50c59491b27`  |
| 2849   | Layout 1             | `f50c59491b27`  |
| 2844   | Layout 1             | `f50c59491b27`  |
| 2834   | Layout 1             | `f50c59491b27`  |
| 2825   | Layout 1             | `f50c59491b27`  |
| 2819   | Layout 1             | `f50c59491b27`  |
| 2811   | Layout 1             | `f50c59491b27`  |
| 2803   | Layout 1             | `f50c59491b27`  |
| 2794   | Layout 1             | `f50c59491b27`  |
| 2783   | Layout 1             | `f50c59491b27`  |
| 2774   | Layout 1             | `f50c59491b27`  |
| 2765   | Layout 1             | `f50c59491b27`  |
| 2756   | Layout 1             | `f50c59491b27`  |
| 2750   | Layout 1             | `f50c59491b27`  |
| 2743   | Layout 1             | `f50c59491b27`  |
| 2736   | Layout 1             | `f50c59491b27`  |
| 2726   | Layout 1             | `f50c59491b27`  |
| 2717   | Layout 1             | `f50c59491b27`  |
| 2709   | Layout 1             | `f50c59491b27`  |
| 2703   | Layout 1             | `f50c59491b27`  |
| 2695   | Layout 1             | `f50c59491b27`  |
| 2684   | Layout 1             | `f50c59491b27`  |
| 2672   | Layout 1             | `f50c59491b27`  |
| 2665   | Layout 1             | `f50c59491b27`  |
| 2657   | Layout 1             | `f50c59491b27`  |
| 2649   | Layout 1             | `f50c59491b27`  |
| 2644   | Layout 1             | `f50c59491b27`  |
| 2637   | Layout 1             | `f50c59491b27`  |
| 2629   | Layout 1             | `f50c59491b27`  |
| 2619   | Layout 1             | `f50c59491b27`  |
| 2612   | Layout 1             | `f50c59491b27`  |
| 2606   | Layout 1             | `f50c59491b27`  |
| 2602   | Layout 1             | `f50c59491b27`  |
| 2601   | Layout 1             | `f50c59491b27`  |
| 2592   | Layout 1             | `f50c59491b27`  |
| 2583   | Layout 1             | `f50c59491b27`  |
| 2575   | Layout 1             | `f50c59491b27`  |
| 2567   | Layout 1             | `f50c59491b27`  |
| 2560   | Layout 1             | `f50c59491b27`  |
| 2553   | Layout 1             | `f50c59491b27`  |
| 2545   | Layout 1             | `f50c59491b27`  |
| 2538   | Layout 1             | `f50c59491b27`  |
| 2529   | Layout 1             | `f50c59491b27`  |
| 2519   | Layout 1             | `f50c59491b27`  |
| 2513   | Layout 1             | `f50c59491b27`  |
| 2510   | Layout 1             | `f50c59491b27`  |
| 2507   | Layout 1             | `f50c59491b27`  |
| 2503   | Layout 1             | `f50c59491b27`  |
| 2498   | Layout 1             | `f50c59491b27`  |
| 2492   | Layout 1             | `f50c59491b27`  |
| 2487   | Layout 1             | `f50c59491b27`  |
| 2480   | Layout 1             | `f50c59491b27`  |
| 2474   | Layout 1             | `f50c59491b27`  |
| 2468   | Layout 1             | `f50c59491b27`  |
| 2460   | Layout 1             | `f50c59491b27`  |
| 2453   | Layout 1             | `f50c59491b27`  |
| 2444   | Layout 1             | `f50c59491b27`  |
| 2438   | Layout 1             | `f50c59491b27`  |
| 2434   | Layout 1             | `f50c59491b27`  |
| 2429   | Layout 1             | `f50c59491b27`  |
| 2421   | Layout 1             | `f50c59491b27`  |
| 2414   | Layout 1             | `f50c59491b27`  |
| 2407   | Layout 1             | `f50c59491b27`  |
| 2401   | Layout 1             | `f50c59491b27`  |
| 2397   | Layout 1             | `f50c59491b27`  |
| 2393   | Layout 1             | `f50c59491b27`  |
| 2384   | Layout 1             | `f50c59491b27`  |
| 2378   | Layout 1             | `f50c59491b27`  |
| 2372   | Layout 1             | `f50c59491b27`  |
| 2358   | Layout 1             | `f50c59491b27`  |
| 2352   | Layout 1             | `f50c59491b27`  |
| 2347   | Layout 1             | `f50c59491b27`  |
| 2343   | Layout 1             | `f50c59491b27`  |
| 2335   | Layout 1             | `f50c59491b27`  |
| 2327   | Layout 1             | `f50c59491b27`  |
| 2324   | Layout 1             | `f50c59491b27`  |
| 2319   | Layout 1             | `f50c59491b27`  |
| 2313   | Layout 1             | `f50c59491b27`  |
| 2308   | Layout 1             | `f50c59491b27`  |
| 2302   | Layout 1             | `f50c59491b27`  |
| 2295   | Layout 1             | `f50c59491b27`  |
| 2290   | Layout 1             | `f50c59491b27`  |
| 2284   | Layout 1             | `f50c59491b27`  |
| 2276   | Layout 1             | `f50c59491b27`  |
| 2269   | Layout 1             | `f50c59491b27`  |
| 2259   | Layout 1             | `f50c59491b27`  |
| 2250   | Layout 1             | `f50c59491b27`  |
| 2243   | Layout 1             | `f50c59491b27`  |
| 2235   | Layout 1             | `f50c59491b27`  |
| 2229   | Layout 1             | `f50c59491b27`  |
| 2224   | Layout 1             | `f50c59491b27`  |
| 2218   | Layout 1             | `f50c59491b27`  |
| 2215   | Layout 1             | `f50c59491b27`  |
| 2207   | Layout 1             | `f50c59491b27`  |
| 2203   | Layout 1             | `f50c59491b27`  |
| 2196   | Layout 1             | `f50c59491b27`  |
| 2192   | Layout 1             | `f50c59491b27`  |
| 2189   | Layout 1             | `f50c59491b27`  |
| 2183   | Layout 1             | `f50c59491b27`  |
| 2179   | Layout 1             | `f50c59491b27`  |
| 2171   | Layout 1             | `f50c59491b27`  |
| 2163   | Layout 1             | `f50c59491b27`  |
| 2156   | Layout 1             | `f50c59491b27`  |
| 2151   | Layout 1             | `f50c59491b27`  |
| 2147   | Layout 1             | `f50c59491b27`  |
| 2142   | Layout 1             | `f50c59491b27`  |
| 2138   | Layout 1             | `f50c59491b27`  |
| 2134   | Layout 1             | `f50c59491b27`  |
| 2130   | Layout 1             | `f50c59491b27`  |
| 2122   | Layout 1             | `f50c59491b27`  |
| 2107   | Layout 1             | `f50c59491b27`  |
| 2098   | Layout 1             | `f50c59491b27`  |
| 2089   | Layout 1             | `f50c59491b27`  |
| 2081   | Layout 1             | `f50c59491b27`  |
| 2073   | Layout 1             | `f50c59491b27`  |
| 2067   | Layout 1             | `f50c59491b27`  |
| 2063   | Layout 1             | `f50c59491b27`  |
| 2059   | Layout 1             | `f50c59491b27`  |
| 2052   | Layout 1             | `f50c59491b27`  |
| 2044   | Layout 1             | `f50c59491b27`  |
| 2039   | Layout 1             | `f50c59491b27`  |
| 2032   | Layout 1             | `f50c59491b27`  |
| 2025   | Layout 1             | `f50c59491b27`  |
| 2011   | Layout 1             | `f50c59491b27`  |
| 2005   | Layout 1             | `f50c59491b27`  |
| 2000   | Layout 1             | `f50c59491b27`  |
| 1996   | Layout 1             | `f50c59491b27`  |
| 1991   | Layout 1             | `f50c59491b27`  |
| 1985   | Layout 1             | `f50c59491b27`  |
| 1980   | Layout 1             | `f50c59491b27`  |
| 1969   | Layout 1             | `f50c59491b27`  |
| 1964   | Layout 1             | `f50c59491b27`  |
| 1958   | Layout 1             | `f50c59491b27`  |
| 1950   | Layout 1             | `f50c59491b27`  |
| 1945   | Layout 1             | `f50c59491b27`  |
| 1937   | Layout 1             | `f50c59491b27`  |
| 1933   | Layout 1             | `f50c59491b27`  |
| 1927   | Layout 1             | `f50c59491b27`  |
| 1921   | Layout 1             | `f50c59491b27`  |
| 1914   | Layout 1             | `f50c59491b27`  |
| 1908   | Layout 1             | `f50c59491b27`  |
| 1897   | Layout 1             | `f50c59491b27`  |
| 1892   | Layout 1             | `f50c59491b27`  |
| 1886   | Layout 1             | `f50c59491b27`  |
| 1881   | Layout 1             | `f50c59491b27`  |
| 1871   | Layout 1             | `f50c59491b27`  |
| 1866   | Layout 1             | `f50c59491b27`  |
| 1862   | Layout 1             | `f50c59491b27`  |
| 1854   | Layout 1             | `f50c59491b27`  |
| 1846   | Layout 1             | `f50c59491b27`  |
| 1838   | Layout 1             | `f50c59491b27`  |
| 1832   | Layout 1             | `f50c59491b27`  |
| 1826   | Layout 1             | `f50c59491b27`  |
| 1822   | Layout 1             | `f50c59491b27`  |
| 1818   | Layout 1             | `f50c59491b27`  |
| 1804   | Layout 1             | `f50c59491b27`  |
| 1794   | Layout 1             | `f50c59491b27`  |
| 1790   | Layout 1             | `f50c59491b27`  |
| 1784   | Layout 1             | `f50c59491b27`  |
| 1774   | Layout 1             | `f50c59491b27`  |
| 1771   | Layout 1             | `f50c59491b27`  |
| 1762   | Layout 1             | `f50c59491b27`  |
| 1759   | Layout 1             | `f50c59491b27`  |
| 1754   | Layout 1             | `f50c59491b27`  |
| 1749   | Layout 1             | `f50c59491b27`  |
| 1743   | Layout 1             | `f50c59491b27`  |
| 1737   | Layout 1             | `f50c59491b27`  |
| 1731   | Layout 1             | `f50c59491b27`  |
| 1725   | Layout 1             | `f50c59491b27`  |
| 1717   | Layout 1             | `f50c59491b27`  |
| 1710   | Layout 1             | `f50c59491b27`  |
| 1704   | Layout 1             | `f50c59491b27`  |
| 1698   | Layout 1             | `f50c59491b27`  |
| 1690   | Layout 1             | `f50c59491b27`  |
| 1685   | Layout 1             | `f50c59491b27`  |
| 1680   | Layout 1             | `f50c59491b27`  |
| 1674   | Layout 1             | `f50c59491b27`  |
| 1668   | Layout 1             | `f50c59491b27`  |
| 1659   | Layout 1             | `f50c59491b27`  |
| 1649   | Layout 1             | `f50c59491b27`  |
| 1642   | Layout 1             | `f50c59491b27`  |
| 1636   | Layout 1             | `f50c59491b27`  |
| 1628   | Layout 1             | `f50c59491b27`  |
| 1622   | Layout 1             | `f50c59491b27`  |
| 1614   | Layout 1             | `f50c59491b27`  |
| 1608   | Layout 1             | `f50c59491b27`  |
| 1602   | Layout 1             | `f50c59491b27`  |
| 1598   | Layout 1             | `f50c59491b27`  |
| 1594   | Layout 1             | `f50c59491b27`  |
| 1590   | Layout 1             | `f50c59491b27`  |
| 1587   | Layout 1             | `f50c59491b27`  |
| 1584   | Layout 1             | `f50c59491b27`  |
| 1579   | Layout 1             | `f50c59491b27`  |
| 1572   | Layout 1             | `f50c59491b27`  |
| 1565   | Layout 1             | `f50c59491b27`  |
| 1559   | Layout 1             | `f50c59491b27`  |
| 1554   | Layout 1             | `f50c59491b27`  |
| 1547   | Layout 1             | `f50c59491b27`  |
| 1537   | Layout 1             | `f50c59491b27`  |
| 1529   | Layout 1             | `f50c59491b27`  |
| 1524   | Layout 1             | `f50c59491b27`  |
| 1519   | Layout 1             | `f50c59491b27`  |
| 1509   | Layout 1             | `f50c59491b27`  |
| 1506   | Layout 1             | `f50c59491b27`  |
| 1504   | Layout 1             | `f50c59491b27`  |
| 1500   | Layout 1             | `f50c59491b27`  |
| 1493   | Layout 1             | `f50c59491b27`  |
| 1489   | Layout 1             | `f50c59491b27`  |
| 1485   | Layout 1             | `f50c59491b27`  |
| 1481   | Layout 1             | `f50c59491b27`  |
| 1474   | Layout 1             | `f50c59491b27`  |
| 1466   | Layout 1             | `f50c59491b27`  |
| 1462   | Layout 1             | `f50c59491b27`  |
| 1459   | Layout 1             | `f50c59491b27`  |
| 1453   | Layout 1             | `f50c59491b27`  |
| 1450   | Layout 1             | `f50c59491b27`  |
| 1445   | Layout 1             | `f50c59491b27`  |
| 1439   | Layout 1             | `f50c59491b27`  |
| 1433   | Layout 1             | `f50c59491b27`  |
| 1430   | Layout 1             | `f50c59491b27`  |
| 1426   | Layout 1             | `f50c59491b27`  |
| 1421   | Layout 1             | `f50c59491b27`  |
| 1417   | Layout 1             | `f50c59491b27`  |
| 1416   | Layout 1             | `f50c59491b27`  |
| 1409   | Layout 1             | `f50c59491b27`  |
| 1405   | Layout 1             | `f50c59491b27`  |
| 1401   | Layout 1             | `f50c59491b27`  |
| 1396   | Layout 1             | `f50c59491b27`  |
| 1391   | Layout 1             | `f50c59491b27`  |
| 1390   | Layout 1             | `f50c59491b27`  |
| 1386   | Layout 1             | `f50c59491b27`  |
| 1381   | Layout 1             | `f50c59491b27`  |
| 1379   | Layout 1             | `f50c59491b27`  |
| 1372   | Layout 1             | `f50c59491b27`  |
| 1366   | Layout 1             | `f50c59491b27`  |
| 1364   | Layout 1             | `f50c59491b27`  |
| 1363   | Layout 1             | `f50c59491b27`  |
| 1360   | Layout 1             | `f50c59491b27`  |
| 1358   | Layout 1             | `f50c59491b27`  |
| 1355   | Layout 1             | `f50c59491b27`  |
| 1351   | Layout 1             | `f50c59491b27`  |
| 1348   | Layout 1             | `f50c59491b27`  |
| 1346   | Layout 1             | `f50c59491b27`  |
| 1341   | Layout 1             | `f50c59491b27`  |
| 1340   | Layout 1             | `f50c59491b27`  |
| 1338   | Layout 1             | `f50c59491b27`  |
| 1335   | Layout 1             | `f50c59491b27`  |
| 1333   | Layout 1             | `f50c59491b27`  |
| 1329   | Layout 1             | `f50c59491b27`  |
| 1327   | Layout 1             | `f50c59491b27`  |
| 1324   | Layout 1             | `f50c59491b27`  |
| 1321   | Layout 1             | `f50c59491b27`  |
| 1319   | Layout 1             | `f50c59491b27`  |
| 1318   | Layout 1             | `f50c59491b27`  |
| 1316   | Layout 1             | `f50c59491b27`  |
| 1313   | Layout 1             | `f50c59491b27`  |
| 1311   | Layout 1             | `f50c59491b27`  |
| 1309   | Layout 1             | `f50c59491b27`  |
| 1304   | No documented layout | `f50c59491b27`  |
| 1292   | No documented layout | `f50c59491b27`  |
| 1286   | No documented layout | `f50c59491b27`  |
| 1280   | No documented layout | `f50c59491b27`  |
| 1276   | No documented layout | `f50c59491b27`  |
| 1267   | No file              | `f50c59491b27`  |
| 1261   | No file              | `f50c59491b27`  |
| 1256   | No file              | `f50c59491b27`  |
| 1250   | No file              | `f50c59491b27`  |
| 1246   | No file              | `f50c59491b27`  |
| 1239   | No file              | `f50c59491b27`  |
| 1230   | No file              | `f50c59491b27`  |
| 1226   | No file              | `f50c59491b27`  |
| 1220   | No file              | `f50c59491b27`  |
| 1217   | No file              | `f50c59491b27`  |
| 1211   | No file              | `f50c59491b27`  |
| 1210   | No file              | `f50c59491b27`  |
| 1208   | No file              | `f50c59491b27`  |
| 1203   | No file              | `f50c59491b27`  |
| 1197   | No file              | `f50c59491b27`  |
| 1194   | No file              | `f50c59491b27`  |
| 1192   | No file              | `f50c59491b27`  |
| 1187   | No file              | `f50c59491b27`  |
| 1183   | No file              | `f50c59491b27`  |
| 1177   | No file              | `f50c59491b27`  |
| 1173   | No file              | `f50c59491b27`  |
| 1167   | No file              | `f50c59491b27`  |
| 1164   | No file              | `f50c59491b27`  |
| 1156   | No file              | `f50c59491b27`  |
| 1149   | No file              | `f50c59491b27`  |
| 1144   | No file              | `f50c59491b27`  |
| 1137   | No file              | `f50c59491b27`  |
| 1132   | No file              | `f50c59491b27`  |
| 1127   | No file              | `f50c59491b27`  |
| 1122   | No file              | `f50c59491b27`  |
| 1118   | No file              | `f50c59491b27`  |
| 1114   | No file              | `f50c59491b27`  |
| 1109   | No file              | `f50c59491b27`  |
| 1102   | No file              | `f50c59491b27`  |
| 1096   | No file              | `f50c59491b27`  |
| 1088   | No file              | `f50c59491b27`  |
| 1081   | No file              | `f50c59491b27`  |
| 1076   | No file              | `f50c59491b27`  |
| 1069   | No file              | `f50c59491b27`  |
| 1064   | No file              | `f50c59491b27`  |
| 1058   | No file              | `f50c59491b27`  |
| 1051   | No file              | `f50c59491b27`  |
| 1044   | No file              | `f50c59491b27`  |
| 1036   | No file              | `f50c59491b27`  |
| 1026   | No file              | `f50c59491b27`  |
| 1016   | No file              | `f50c59491b27`  |
| 1009   | No file              | `f50c59491b27`  |
| 1005   | No file              | `f50c59491b27`  |
| 1000   | No file              | `f50c59491b27`  |
| 998    | No file              | `f50c59491b27`  |
| 990    | No file              | `f50c59491b27`  |
| 979    | No file              | `f50c59491b27`  |
| 972    | No file              | `f50c59491b27`  |
| 963    | No file              | `f50c59491b27`  |
| 955    | No file              | `f50c59491b27`  |
| 946    | No file              | `f50c59491b27`  |
| 938    | No file              | `f50c59491b27`  |
| 927    | No file              | `f50c59491b27`  |
| 911    | No file              | `f50c59491b27`  |
| 904    | No file              | `f50c59491b27`  |
| 899    | No file              | `f50c59491b27`  |
| 894    | No file              | `f50c59491b27`  |
| 885    | No file              | `f50c59491b27`  |
| 879    | No file              | `f50c59491b27`  |
| 872    | No file              | `f50c59491b27`  |
| 864    | No file              | `f50c59491b27`  |
| 855    | No file              | `f50c59491b27`  |
| 853    | No file              | `f50c59491b27`  |
| 845    | No file              | `f50c59491b27`  |
| 837    | No file              | `f50c59491b27`  |
| 829    | No file              | `f50c59491b27`  |
| 822    | No file              | `f50c59491b27`  |
| 814    | No file              | `f50c59491b27`  |
| 805    | No file              | `f50c59491b27`  |
| 794    | No file              | `f50c59491b27`  |
| 787    | No file              | `f50c59491b27`  |
| 780    | No file              | `f50c59491b27`  |
| 771    | No file              | `f50c59491b27`  |
| 760    | No file              | `f50c59491b27`  |
| 748    | No file              | `f50c59491b27`  |
| 741    | No file              | `f50c59491b27`  |
| 736    | No file              | `f50c59491b27`  |
| 731    | No file              | `f50c59491b27`  |
| 723    | No file              | `f50c59491b27`  |
| 711    | No file              | `f50c59491b27`  |
| 707    | No file              | `f50c59491b27`  |
| 697    | No file              | `f50c59491b27`  |
| 689    | No file              | `f50c59491b27`  |
| 683    | No file              | `f50c59491b27`  |
| 678    | No file              | `f50c59491b27`  |
| 670    | No file              | `f50c59491b27`  |
| 661    | No file              | `f50c59491b27`  |
| 656    | No file              | `f50c59491b27`  |
| 652    | No file              | `f50c59491b27`  |
| 643    | No file              | `f50c59491b27`  |
| 637    | No file              | `f50c59491b27`  |
| 630    | No file              | `f50c59491b27`  |
| 627    | No file              | `f50c59491b27`  |
| 621    | No file              | `f50c59491b27`  |
| 617    | No file              | `f50c59491b27`  |
| 615    | No file              | `f50c59491b27`  |
| 606    | No file              | `f50c59491b27`  |
| 599    | No file              | `f50c59491b27`  |
| 592    | No file              | `f50c59491b27`  |
| 586    | No file              | `f50c59491b27`  |
| 577    | No file              | `f50c59491b27`  |
| 569    | No file              | `f50c59491b27`  |
| 561    | No file              | `f50c59491b27`  |
| 554    | No file              | `f50c59491b27`  |
| 542    | No file              | `f50c59491b27`  |
| 532    | No file              | `f50c59491b27`  |
| 531    | No file              | `f50c59491b27`  |
| 526    | No file              | `f50c59491b27`  |
| 521    | No file              | `f50c59491b27`  |
| 517    | No file              | `f50c59491b27`  |
| 510    | No file              | `f50c59491b27`  |
| 508    | No file              | `f50c59491b27`  |
| 504    | No file              | `f50c59491b27`  |
| 497    | No file              | `f50c59491b27`  |
| 491    | No file              | `f50c59491b27`  |
| 485    | No file              | `f50c59491b27`  |
| 478    | No file              | `f50c59491b27`  |
| 472    | No file              | `f50c59491b27`  |
| 466    | No file              | `f50c59491b27`  |
| 457    | No file              | `f50c59491b27`  |
| 452    | No file              | `f50c59491b27`  |
| 449    | No file              | `f50c59491b27`  |
| 435    | No file              | `f50c59491b27`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                 |
| ------------------------- | -------- | -------------------------------------------------------------------- |
| `carriagespecoffset.dbss` | Optional | `carriage_key -> (offset, size)` of every row; the main file can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (40 bytes)

| Offset  | Type | Field                             | Notes                                                    |
| ------- | ---- | --------------------------------- | -------------------------------------------------------- |
| `+0x00` | u8   | carriage_key                      | Carriage type; the offset file points here               |
| `+0x01` | i32  | distance_per_minute               | `6500` on both rows (client 3474)                        |
| `+0x05` | i32  | loadage                           | `20` on both rows (client 3474)                          |
| `+0x09` | i32  | transport_max_weight              | See Values per Carriage                                  |
| `+0x0D` | i32  | camasilb_add_transport_max_weight | `15000000` on both rows (client 3474)                    |
| `+0x11` | i64  | base_fee                          | See Values per Carriage                                  |
| `+0x19` | i32  | overload_weight                   | Equal to `transport_max_weight` on both rows (client 3474) |
| `+0x1D` | i64  | fee_per_weight                    | `1` on both rows (client 3474)                           |
| `+0x25` | u8   | non_stack_trade                   | Bool                                                     |
| `+0x26` | u8   | stack_trade                       | Bool                                                     |
| `+0x27` | u8   | expiration_period_trade           | Bool; `0` on both rows (client 3474)                     |

### `carriagespecoffset.dbss`

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `carriagespec.dbss` count    |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row    |

### Offset Row (9 bytes)

| Offset  | Type | Field        | Notes                                         |
| ------- | ---- | ------------ | --------------------------------------------- |
| `+0x00` | u8   | carriage_key | Key of the row it points at                   |
| `+0x01` | u32  | offset       | Row start, at its `carriage_key`              |
| `+0x05` | u32  | size         | The whole row: always `40`                    |

Read by `parse_bare_u8_offset_rows()` in `_common/pabr_offset.py`.

## Values per Carriage

Every field that differs between the two rows or between clients. The
rest are the same on both rows and both clients (see the Row notes).

| `carriage_key` | Client | `transport_max_weight` | `overload_weight` | `base_fee` | `non_stack_trade` | `stack_trade` |
| -------------- | ------ | ---------------------- | ----------------- | ---------- | ----------------- | ------------- |
| 1              | 1784   | 15000000               | 15000000          | 10         | 0                 | 0             |
| 1              | 3474   | 15000000               | 15000000          | 10         | 0                 | 0             |
| 2              | 1784   | 300000000              | 300000000         | 30         | 1                 | 1             |
| 2              | 3474   | 600000000              | 600000000         | 3          | 1                 | 1             |

## Field Names

The names follow the `New_Carriage2_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (the same sheet sits in its
`datasheet_plantdatatable.xlsm`, with no developer comments). Its columns are
`CarriageKey`, `DistancePerMinute`, `Loadage`, `BaseFee`,
`TransportMaxWeight`, `OverLoadWeight`, `FeePerWeight`, `NonStackTrade`,
`StackTrade`, `ExpirationPeriodTrade` and `CamasilbAddTransportMaxWeight`.
Both of its rows match the file on client 1784 in all 11 columns (2 of 2
keys). On client 3474 key `1` still matches in all 11; key `2` differs in
`BaseFee`, `TransportMaxWeight` and `OverLoadWeight` (table above), a
rebalance after client 1784.

The file order is not the sheet order. The client 1784 server dump
(`Instance_dumpFull.exe`) reads the sheet in the function at VA
`0x140a05260`: `CarriageKey` with `ReadCellInt8` into a byte at `+0x00`,
then `DistancePerMinute`, `Loadage`, `TransportMaxWeight` and
`CamasilbAddTransportMaxWeight` with `ReadColumnInt` at `+0x04` to `+0x10`,
`BaseFee` with `ReadColumnInt` widened to 8 bytes at `+0x18`,
`OverLoadWeight` with `ReadColumnInt` at `+0x20`, `FeePerWeight` with
`ReadColumnInt64` at `+0x28` and the three trade columns with
`ReadColumnBool` at `+0x30` to `+0x32`. Packed with no padding, that order
and those widths give the 40-byte row of the file, and the values of both
clients land in the matching fields. `CamasilbAddTransportMaxWeight` keeps
the sheet's spelling as `camasilb_add_transport_max_weight`.

The 2016 client's debug symbols have no carriage spec struct; their
`ge::wrapper::DeliveryCarriageInfo` (character key and name) belongs to the
older delivery system. The `Carriage_Table` of a private server on client
519 is that older table (per-route waypoints and prices) and has none of
these columns.

## Notes

- Clients 1485 and 1784 have the same 84-byte main file and 22-byte offset
  file layout; only the key `2` values in the table above differ.
- Client 1230 has no `carriagespec.dbss`. Its `carriagespec.bss` is a PABR
  file of the same 2 rows in 36-byte rows with a 12-byte trailer: the order
  above without `camasilb_add_transport_max_weight`. Client 794 has neither
  file.
- [`carriagechar.bss`](carriagechar_bss.md) comes from the
  `New_Carriage_Table` sheet of the same workbook (`CharacterKey`,
  `ObjectName`: world map models `WorldMap_Cart.pam`,
  `WorldMap_WoodenBoat_small.pam`, `WorldMap_SailingShip.pam`) and has no
  carriage key column, so it does not join this file.
- The transport window (`panel_window_delivery_all`) labels deliverers at
  or above the client constant `__eDeliveryTradeCarriageIndex` with
  `LUA_DELIVERYNEW_FIVENUMBER_CARRIAGE` and the rest with
  `LUA_DELIVERYNEW_NUMBEROF_CARRIAGE`, and shows the remaining and maximum
  weight from `ToClient_NewDeliveryGetRemainWeight()` and
  `ToClient_NewDeliveryGetMaxWeightPerCarriage()` times `1.0E-4` as LT. No
  Lua names `carriagespec` or its columns.

## Open Questions

### Which Carriage Key Is Which

Key `2` has a 40 times larger `transport_max_weight` on client 3474 and is
the only row with `non_stack_trade` and `stack_trade` set, so it may be the
trade carriage that the transport window numbers from
`__eDeliveryTradeCarriageIndex`. The client Lua passes deliverer indexes,
not carriage keys, so the data does not tie the two together.

### Units of distance_per_minute, loadage and the Fees

The transport window divides weights by 10,000 for its LT label, so
`transport_max_weight` `15000000` would read as 1,500 LT, but the Lua reads
the limit through `ToClient_NewDeliveryGetMaxWeightPerCarriage()`, not from
this file. What `distance_per_minute` (`6500`) and `loadage` (`20`) count,
and how `base_fee` and `fee_per_weight` add up to
`Toclient_NewDeliveryGetPackItemTotalPrice()`, is open.

### camasilb_add_transport_max_weight

`15000000` on both rows and both clients. The column name reads as extra
transport weight tied to Kamasylvia or Kamasylve (`카마실브`); what grants it
is open.
