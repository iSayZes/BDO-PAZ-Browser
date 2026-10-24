# `houseinfoneeditem.dbss` Format

## Purpose

What it costs to set a node house to a use and to raise that use a level.
A row is one need item group, the `need_item_key` that
[`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) rows point at, with six
level slots: slot 0 is level 0 and holds nothing, slots 1 to 5 hold the
transfer time and the items house levels 1 to 5 take. On client 3474 every
item is Silver.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records                        | Row bytes               |
| ------ | -------------- | ------- | ------------------------------ | ----- | ------------------------------ | ----------------------- |
| 1      | 1292 and later | 3483    | `houseinfoneeditem.dbss`       | 1,322 | 66 Level, 42 Need Item, 11 Row | 12 to 24, 20 on average |
| 1      | 1292 and later | 3483    | `houseinfoneeditemoffset.dbss` | 114   | 11 Index Row                   | 10                      |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 1      | `houseinfoneeditem.dbss`       | 1,322 B (100.0%) | 0 B (0.0%) |
| 1      | `houseinfoneeditemoffset.dbss` | 114 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d477e0f317fe`  |
| 3482   | Layout 1 | `d477e0f317fe`  |
| 3474   | Layout 1 | `d477e0f317fe`  |
| 3473   | Layout 1 | `d477e0f317fe`  |
| 3464   | Layout 1 | `d477e0f317fe`  |
| 3458   | Layout 1 | `d477e0f317fe`  |
| 3454   | Layout 1 | `d477e0f317fe`  |
| 3444   | Layout 1 | `d477e0f317fe`  |
| 3435   | Layout 1 | `d477e0f317fe`  |
| 3426   | Layout 1 | `d477e0f317fe`  |
| 3418   | Layout 1 | `d477e0f317fe`  |
| 3412   | Layout 1 | `d477e0f317fe`  |
| 3402   | Layout 1 | `d477e0f317fe`  |
| 3396   | Layout 1 | `d477e0f317fe`  |
| 3387   | Layout 1 | `d477e0f317fe`  |
| 3381   | Layout 1 | `d477e0f317fe`  |
| 3373   | Layout 1 | `d477e0f317fe`  |
| 3364   | Layout 1 | `d477e0f317fe`  |
| 3356   | Layout 1 | `d477e0f317fe`  |
| 3349   | Layout 1 | `d477e0f317fe`  |
| 3342   | Layout 1 | `d477e0f317fe`  |
| 3335   | Layout 1 | `d477e0f317fe`  |
| 3326   | Layout 1 | `d477e0f317fe`  |
| 3321   | Layout 1 | `d477e0f317fe`  |
| 3314   | Layout 1 | `d477e0f317fe`  |
| 3303   | Layout 1 | `d477e0f317fe`  |
| 3302   | Layout 1 | `d477e0f317fe`  |
| 3293   | Layout 1 | `d477e0f317fe`  |
| 3283   | Layout 1 | `d477e0f317fe`  |
| 3275   | Layout 1 | `d477e0f317fe`  |
| 3267   | Layout 1 | `d477e0f317fe`  |
| 3258   | Layout 1 | `d477e0f317fe`  |
| 3251   | Layout 1 | `d477e0f317fe`  |
| 3242   | Layout 1 | `d477e0f317fe`  |
| 3235   | Layout 1 | `d477e0f317fe`  |
| 3229   | Layout 1 | `d477e0f317fe`  |
| 3212   | Layout 1 | `d477e0f317fe`  |
| 3203   | Layout 1 | `d477e0f317fe`  |
| 3193   | Layout 1 | `d477e0f317fe`  |
| 3186   | Layout 1 | `d477e0f317fe`  |
| 3177   | Layout 1 | `d477e0f317fe`  |
| 3169   | Layout 1 | `d477e0f317fe`  |
| 3158   | Layout 1 | `d477e0f317fe`  |
| 3151   | Layout 1 | `d477e0f317fe`  |
| 3144   | Layout 1 | `d477e0f317fe`  |
| 3133   | Layout 1 | `d477e0f317fe`  |
| 3125   | Layout 1 | `d477e0f317fe`  |
| 3118   | Layout 1 | `d477e0f317fe`  |
| 3111   | Layout 1 | `d477e0f317fe`  |
| 3103   | Layout 1 | `d477e0f317fe`  |
| 3095   | Layout 1 | `d477e0f317fe`  |
| 3086   | Layout 1 | `d477e0f317fe`  |
| 3072   | Layout 1 | `d477e0f317fe`  |
| 3062   | Layout 1 | `d477e0f317fe`  |
| 3052   | Layout 1 | `d477e0f317fe`  |
| 3045   | Layout 1 | `d477e0f317fe`  |
| 3037   | Layout 1 | `d477e0f317fe`  |
| 3030   | Layout 1 | `d477e0f317fe`  |
| 3021   | Layout 1 | `d477e0f317fe`  |
| 3012   | Layout 1 | `d477e0f317fe`  |
| 3002   | Layout 1 | `d477e0f317fe`  |
| 2995   | Layout 1 | `d477e0f317fe`  |
| 2987   | Layout 1 | `d477e0f317fe`  |
| 2978   | Layout 1 | `d477e0f317fe`  |
| 2970   | Layout 1 | `d477e0f317fe`  |
| 2959   | Layout 1 | `d477e0f317fe`  |
| 2951   | Layout 1 | `d477e0f317fe`  |
| 2942   | Layout 1 | `d477e0f317fe`  |
| 2935   | Layout 1 | `d477e0f317fe`  |
| 2932   | Layout 1 | `d477e0f317fe`  |
| 2923   | Layout 1 | `d477e0f317fe`  |
| 2919   | Layout 1 | `d477e0f317fe`  |
| 2907   | Layout 1 | `d477e0f317fe`  |
| 2900   | Layout 1 | `d477e0f317fe`  |
| 2891   | Layout 1 | `d477e0f317fe`  |
| 2882   | Layout 1 | `d477e0f317fe`  |
| 2872   | Layout 1 | `d477e0f317fe`  |
| 2863   | Layout 1 | `d477e0f317fe`  |
| 2855   | Layout 1 | `d477e0f317fe`  |
| 2849   | Layout 1 | `d477e0f317fe`  |
| 2844   | Layout 1 | `d477e0f317fe`  |
| 2834   | Layout 1 | `d477e0f317fe`  |
| 2825   | Layout 1 | `d477e0f317fe`  |
| 2819   | Layout 1 | `d477e0f317fe`  |
| 2811   | Layout 1 | `d477e0f317fe`  |
| 2803   | Layout 1 | `d477e0f317fe`  |
| 2794   | Layout 1 | `d477e0f317fe`  |
| 2783   | Layout 1 | `d477e0f317fe`  |
| 2774   | Layout 1 | `d477e0f317fe`  |
| 2765   | Layout 1 | `d477e0f317fe`  |
| 2756   | Layout 1 | `d477e0f317fe`  |
| 2750   | Layout 1 | `d477e0f317fe`  |
| 2743   | Layout 1 | `d477e0f317fe`  |
| 2736   | Layout 1 | `d477e0f317fe`  |
| 2726   | Layout 1 | `d477e0f317fe`  |
| 2717   | Layout 1 | `d477e0f317fe`  |
| 2709   | Layout 1 | `d477e0f317fe`  |
| 2703   | Layout 1 | `d477e0f317fe`  |
| 2695   | Layout 1 | `d477e0f317fe`  |
| 2684   | Layout 1 | `d477e0f317fe`  |
| 2672   | Layout 1 | `d477e0f317fe`  |
| 2665   | Layout 1 | `d477e0f317fe`  |
| 2657   | Layout 1 | `d477e0f317fe`  |
| 2649   | Layout 1 | `d477e0f317fe`  |
| 2644   | Layout 1 | `d477e0f317fe`  |
| 2637   | Layout 1 | `d477e0f317fe`  |
| 2629   | Layout 1 | `d477e0f317fe`  |
| 2619   | Layout 1 | `d477e0f317fe`  |
| 2612   | Layout 1 | `d477e0f317fe`  |
| 2606   | Layout 1 | `d477e0f317fe`  |
| 2602   | Layout 1 | `d477e0f317fe`  |
| 2601   | Layout 1 | `d477e0f317fe`  |
| 2592   | Layout 1 | `d477e0f317fe`  |
| 2583   | Layout 1 | `d477e0f317fe`  |
| 2575   | Layout 1 | `d477e0f317fe`  |
| 2567   | Layout 1 | `d477e0f317fe`  |
| 2560   | Layout 1 | `d477e0f317fe`  |
| 2553   | Layout 1 | `d477e0f317fe`  |
| 2545   | Layout 1 | `d477e0f317fe`  |
| 2538   | Layout 1 | `d477e0f317fe`  |
| 2529   | Layout 1 | `d477e0f317fe`  |
| 2519   | Layout 1 | `d477e0f317fe`  |
| 2513   | Layout 1 | `d477e0f317fe`  |
| 2510   | Layout 1 | `d477e0f317fe`  |
| 2507   | Layout 1 | `d477e0f317fe`  |
| 2503   | Layout 1 | `d477e0f317fe`  |
| 2498   | Layout 1 | `d477e0f317fe`  |
| 2492   | Layout 1 | `d477e0f317fe`  |
| 2487   | Layout 1 | `d477e0f317fe`  |
| 2480   | Layout 1 | `d477e0f317fe`  |
| 2474   | Layout 1 | `d477e0f317fe`  |
| 2468   | Layout 1 | `d477e0f317fe`  |
| 2460   | Layout 1 | `d477e0f317fe`  |
| 2453   | Layout 1 | `d477e0f317fe`  |
| 2444   | Layout 1 | `d477e0f317fe`  |
| 2438   | Layout 1 | `d477e0f317fe`  |
| 2434   | Layout 1 | `d477e0f317fe`  |
| 2429   | Layout 1 | `d477e0f317fe`  |
| 2421   | Layout 1 | `d477e0f317fe`  |
| 2414   | Layout 1 | `d477e0f317fe`  |
| 2407   | Layout 1 | `d477e0f317fe`  |
| 2401   | Layout 1 | `d477e0f317fe`  |
| 2397   | Layout 1 | `d477e0f317fe`  |
| 2393   | Layout 1 | `d477e0f317fe`  |
| 2384   | Layout 1 | `d477e0f317fe`  |
| 2378   | Layout 1 | `d477e0f317fe`  |
| 2372   | Layout 1 | `d477e0f317fe`  |
| 2358   | Layout 1 | `d477e0f317fe`  |
| 2352   | Layout 1 | `d477e0f317fe`  |
| 2347   | Layout 1 | `d477e0f317fe`  |
| 2343   | Layout 1 | `d477e0f317fe`  |
| 2335   | Layout 1 | `d477e0f317fe`  |
| 2327   | Layout 1 | `d477e0f317fe`  |
| 2324   | Layout 1 | `d477e0f317fe`  |
| 2319   | Layout 1 | `d477e0f317fe`  |
| 2313   | Layout 1 | `d477e0f317fe`  |
| 2308   | Layout 1 | `d477e0f317fe`  |
| 2302   | Layout 1 | `d477e0f317fe`  |
| 2295   | Layout 1 | `d477e0f317fe`  |
| 2290   | Layout 1 | `d477e0f317fe`  |
| 2284   | Layout 1 | `d477e0f317fe`  |
| 2276   | Layout 1 | `d477e0f317fe`  |
| 2269   | Layout 1 | `d477e0f317fe`  |
| 2259   | Layout 1 | `d477e0f317fe`  |
| 2250   | Layout 1 | `d477e0f317fe`  |
| 2243   | Layout 1 | `d477e0f317fe`  |
| 2235   | Layout 1 | `d477e0f317fe`  |
| 2229   | Layout 1 | `d477e0f317fe`  |
| 2224   | Layout 1 | `d477e0f317fe`  |
| 2218   | Layout 1 | `d477e0f317fe`  |
| 2215   | Layout 1 | `d477e0f317fe`  |
| 2207   | Layout 1 | `d477e0f317fe`  |
| 2203   | Layout 1 | `d477e0f317fe`  |
| 2196   | Layout 1 | `d477e0f317fe`  |
| 2192   | Layout 1 | `d477e0f317fe`  |
| 2189   | Layout 1 | `d477e0f317fe`  |
| 2183   | Layout 1 | `d477e0f317fe`  |
| 2179   | Layout 1 | `d477e0f317fe`  |
| 2171   | Layout 1 | `d477e0f317fe`  |
| 2163   | Layout 1 | `d477e0f317fe`  |
| 2156   | Layout 1 | `d477e0f317fe`  |
| 2151   | Layout 1 | `d477e0f317fe`  |
| 2147   | Layout 1 | `d477e0f317fe`  |
| 2142   | Layout 1 | `d477e0f317fe`  |
| 2138   | Layout 1 | `d477e0f317fe`  |
| 2134   | Layout 1 | `d477e0f317fe`  |
| 2130   | Layout 1 | `d477e0f317fe`  |
| 2122   | Layout 1 | `d477e0f317fe`  |
| 2107   | Layout 1 | `d477e0f317fe`  |
| 2098   | Layout 1 | `d477e0f317fe`  |
| 2089   | Layout 1 | `d477e0f317fe`  |
| 2081   | Layout 1 | `d477e0f317fe`  |
| 2073   | Layout 1 | `d477e0f317fe`  |
| 2067   | Layout 1 | `d477e0f317fe`  |
| 2063   | Layout 1 | `d477e0f317fe`  |
| 2059   | Layout 1 | `d477e0f317fe`  |
| 2052   | Layout 1 | `d477e0f317fe`  |
| 2044   | Layout 1 | `d477e0f317fe`  |
| 2039   | Layout 1 | `d477e0f317fe`  |
| 2032   | Layout 1 | `d477e0f317fe`  |
| 2025   | Layout 1 | `d477e0f317fe`  |
| 2011   | Layout 1 | `d477e0f317fe`  |
| 2005   | Layout 1 | `d477e0f317fe`  |
| 2000   | Layout 1 | `d477e0f317fe`  |
| 1996   | Layout 1 | `d477e0f317fe`  |
| 1991   | Layout 1 | `d477e0f317fe`  |
| 1985   | Layout 1 | `d477e0f317fe`  |
| 1980   | Layout 1 | `d477e0f317fe`  |
| 1969   | Layout 1 | `d477e0f317fe`  |
| 1964   | Layout 1 | `d477e0f317fe`  |
| 1958   | Layout 1 | `d477e0f317fe`  |
| 1950   | Layout 1 | `d477e0f317fe`  |
| 1945   | Layout 1 | `d477e0f317fe`  |
| 1937   | Layout 1 | `d477e0f317fe`  |
| 1933   | Layout 1 | `d477e0f317fe`  |
| 1927   | Layout 1 | `d477e0f317fe`  |
| 1921   | Layout 1 | `d477e0f317fe`  |
| 1914   | Layout 1 | `d477e0f317fe`  |
| 1908   | Layout 1 | `d477e0f317fe`  |
| 1897   | Layout 1 | `d477e0f317fe`  |
| 1892   | Layout 1 | `d477e0f317fe`  |
| 1886   | Layout 1 | `d477e0f317fe`  |
| 1881   | Layout 1 | `d477e0f317fe`  |
| 1871   | Layout 1 | `d477e0f317fe`  |
| 1866   | Layout 1 | `d477e0f317fe`  |
| 1862   | Layout 1 | `d477e0f317fe`  |
| 1854   | Layout 1 | `d477e0f317fe`  |
| 1846   | Layout 1 | `d477e0f317fe`  |
| 1838   | Layout 1 | `d477e0f317fe`  |
| 1832   | Layout 1 | `d477e0f317fe`  |
| 1826   | Layout 1 | `d477e0f317fe`  |
| 1822   | Layout 1 | `d477e0f317fe`  |
| 1818   | Layout 1 | `d477e0f317fe`  |
| 1804   | Layout 1 | `d477e0f317fe`  |
| 1794   | Layout 1 | `d477e0f317fe`  |
| 1790   | Layout 1 | `d477e0f317fe`  |
| 1784   | Layout 1 | `d477e0f317fe`  |
| 1774   | Layout 1 | `d477e0f317fe`  |
| 1771   | Layout 1 | `d477e0f317fe`  |
| 1762   | Layout 1 | `d477e0f317fe`  |
| 1759   | Layout 1 | `d477e0f317fe`  |
| 1754   | Layout 1 | `d477e0f317fe`  |
| 1749   | Layout 1 | `d477e0f317fe`  |
| 1743   | Layout 1 | `d477e0f317fe`  |
| 1737   | Layout 1 | `d477e0f317fe`  |
| 1731   | Layout 1 | `d477e0f317fe`  |
| 1725   | Layout 1 | `d477e0f317fe`  |
| 1717   | Layout 1 | `d477e0f317fe`  |
| 1710   | Layout 1 | `d477e0f317fe`  |
| 1704   | Layout 1 | `d477e0f317fe`  |
| 1698   | Layout 1 | `d477e0f317fe`  |
| 1690   | Layout 1 | `d477e0f317fe`  |
| 1685   | Layout 1 | `d477e0f317fe`  |
| 1680   | Layout 1 | `d477e0f317fe`  |
| 1674   | Layout 1 | `d477e0f317fe`  |
| 1668   | Layout 1 | `d477e0f317fe`  |
| 1659   | Layout 1 | `d477e0f317fe`  |
| 1649   | Layout 1 | `d477e0f317fe`  |
| 1642   | Layout 1 | `d477e0f317fe`  |
| 1636   | Layout 1 | `d477e0f317fe`  |
| 1628   | Layout 1 | `d477e0f317fe`  |
| 1622   | Layout 1 | `d477e0f317fe`  |
| 1614   | Layout 1 | `d477e0f317fe`  |
| 1608   | Layout 1 | `d477e0f317fe`  |
| 1602   | Layout 1 | `d477e0f317fe`  |
| 1598   | Layout 1 | `d477e0f317fe`  |
| 1594   | Layout 1 | `d477e0f317fe`  |
| 1590   | Layout 1 | `d477e0f317fe`  |
| 1587   | Layout 1 | `d477e0f317fe`  |
| 1584   | Layout 1 | `d477e0f317fe`  |
| 1579   | Layout 1 | `d477e0f317fe`  |
| 1572   | Layout 1 | `d477e0f317fe`  |
| 1565   | Layout 1 | `d477e0f317fe`  |
| 1559   | Layout 1 | `d477e0f317fe`  |
| 1554   | Layout 1 | `d477e0f317fe`  |
| 1547   | Layout 1 | `d477e0f317fe`  |
| 1537   | Layout 1 | `d477e0f317fe`  |
| 1529   | Layout 1 | `d477e0f317fe`  |
| 1524   | Layout 1 | `d477e0f317fe`  |
| 1519   | Layout 1 | `d477e0f317fe`  |
| 1509   | Layout 1 | `d477e0f317fe`  |
| 1506   | Layout 1 | `d477e0f317fe`  |
| 1504   | Layout 1 | `d477e0f317fe`  |
| 1500   | Layout 1 | `d477e0f317fe`  |
| 1493   | Layout 1 | `d477e0f317fe`  |
| 1489   | Layout 1 | `d477e0f317fe`  |
| 1485   | Layout 1 | `d477e0f317fe`  |
| 1481   | Layout 1 | `d477e0f317fe`  |
| 1474   | Layout 1 | `d477e0f317fe`  |
| 1466   | Layout 1 | `d477e0f317fe`  |
| 1462   | Layout 1 | `d477e0f317fe`  |
| 1459   | Layout 1 | `d477e0f317fe`  |
| 1453   | Layout 1 | `d477e0f317fe`  |
| 1450   | Layout 1 | `d477e0f317fe`  |
| 1445   | Layout 1 | `d477e0f317fe`  |
| 1439   | Layout 1 | `d477e0f317fe`  |
| 1433   | Layout 1 | `d477e0f317fe`  |
| 1430   | Layout 1 | `d477e0f317fe`  |
| 1426   | Layout 1 | `d477e0f317fe`  |
| 1421   | Layout 1 | `d477e0f317fe`  |
| 1417   | Layout 1 | `d477e0f317fe`  |
| 1416   | Layout 1 | `d477e0f317fe`  |
| 1409   | Layout 1 | `d477e0f317fe`  |
| 1405   | Layout 1 | `d477e0f317fe`  |
| 1401   | Layout 1 | `d477e0f317fe`  |
| 1396   | Layout 1 | `d477e0f317fe`  |
| 1391   | Layout 1 | `d477e0f317fe`  |
| 1390   | Layout 1 | `d477e0f317fe`  |
| 1386   | Layout 1 | `d477e0f317fe`  |
| 1381   | Layout 1 | `d477e0f317fe`  |
| 1379   | Layout 1 | `d477e0f317fe`  |
| 1372   | Layout 1 | `d477e0f317fe`  |
| 1366   | Layout 1 | `d477e0f317fe`  |
| 1364   | Layout 1 | `d477e0f317fe`  |
| 1363   | Layout 1 | `d477e0f317fe`  |
| 1360   | Layout 1 | `d477e0f317fe`  |
| 1358   | Layout 1 | `d477e0f317fe`  |
| 1355   | Layout 1 | `d477e0f317fe`  |
| 1351   | Layout 1 | `d477e0f317fe`  |
| 1348   | Layout 1 | `d477e0f317fe`  |
| 1346   | Layout 1 | `d477e0f317fe`  |
| 1341   | Layout 1 | `d477e0f317fe`  |
| 1340   | Layout 1 | `d477e0f317fe`  |
| 1338   | Layout 1 | `d477e0f317fe`  |
| 1335   | Layout 1 | `d477e0f317fe`  |
| 1333   | Layout 1 | `d477e0f317fe`  |
| 1329   | Layout 1 | `d477e0f317fe`  |
| 1327   | Layout 1 | `d477e0f317fe`  |
| 1324   | Layout 1 | `d477e0f317fe`  |
| 1321   | Layout 1 | `d477e0f317fe`  |
| 1319   | Layout 1 | `d477e0f317fe`  |
| 1318   | Layout 1 | `d477e0f317fe`  |
| 1316   | Layout 1 | `d477e0f317fe`  |
| 1313   | Layout 1 | `d477e0f317fe`  |
| 1311   | Layout 1 | `d477e0f317fe`  |
| 1309   | Layout 1 | `d477e0f317fe`  |
| 1304   | Layout 1 | `d477e0f317fe`  |
| 1292   | Layout 1 | `d477e0f317fe`  |
| 1286   | No file  | `d477e0f317fe`  |
| 1280   | No file  | `d477e0f317fe`  |
| 1276   | No file  | `d477e0f317fe`  |
| 1267   | No file  | `d477e0f317fe`  |
| 1261   | No file  | `d477e0f317fe`  |
| 1256   | No file  | `d477e0f317fe`  |
| 1250   | No file  | `d477e0f317fe`  |
| 1246   | No file  | `d477e0f317fe`  |
| 1239   | No file  | `d477e0f317fe`  |
| 1230   | No file  | `d477e0f317fe`  |
| 1226   | No file  | `d477e0f317fe`  |
| 1220   | No file  | `d477e0f317fe`  |
| 1217   | No file  | `d477e0f317fe`  |
| 1211   | No file  | `d477e0f317fe`  |
| 1210   | No file  | `d477e0f317fe`  |
| 1208   | No file  | `d477e0f317fe`  |
| 1203   | No file  | `d477e0f317fe`  |
| 1197   | No file  | `d477e0f317fe`  |
| 1194   | No file  | `d477e0f317fe`  |
| 1192   | No file  | `d477e0f317fe`  |
| 1187   | No file  | `d477e0f317fe`  |
| 1183   | No file  | `d477e0f317fe`  |
| 1177   | No file  | `d477e0f317fe`  |
| 1173   | No file  | `d477e0f317fe`  |
| 1167   | No file  | `d477e0f317fe`  |
| 1164   | No file  | `d477e0f317fe`  |
| 1156   | No file  | `d477e0f317fe`  |
| 1149   | No file  | `d477e0f317fe`  |
| 1144   | No file  | `d477e0f317fe`  |
| 1137   | No file  | `d477e0f317fe`  |
| 1132   | No file  | `d477e0f317fe`  |
| 1127   | No file  | `d477e0f317fe`  |
| 1122   | No file  | `d477e0f317fe`  |
| 1118   | No file  | `d477e0f317fe`  |
| 1114   | No file  | `d477e0f317fe`  |
| 1109   | No file  | `d477e0f317fe`  |
| 1102   | No file  | `d477e0f317fe`  |
| 1096   | No file  | `d477e0f317fe`  |
| 1088   | No file  | `d477e0f317fe`  |
| 1081   | No file  | `d477e0f317fe`  |
| 1076   | No file  | `d477e0f317fe`  |
| 1069   | No file  | `d477e0f317fe`  |
| 1064   | No file  | `d477e0f317fe`  |
| 1058   | No file  | `d477e0f317fe`  |
| 1051   | No file  | `d477e0f317fe`  |
| 1044   | No file  | `d477e0f317fe`  |
| 1036   | No file  | `d477e0f317fe`  |
| 1026   | No file  | `d477e0f317fe`  |
| 1016   | No file  | `d477e0f317fe`  |
| 1009   | No file  | `d477e0f317fe`  |
| 1005   | No file  | `d477e0f317fe`  |
| 1000   | No file  | `d477e0f317fe`  |
| 998    | No file  | `d477e0f317fe`  |
| 990    | No file  | `d477e0f317fe`  |
| 979    | No file  | `d477e0f317fe`  |
| 972    | No file  | `d477e0f317fe`  |
| 963    | No file  | `d477e0f317fe`  |
| 955    | No file  | `d477e0f317fe`  |
| 946    | No file  | `d477e0f317fe`  |
| 938    | No file  | `d477e0f317fe`  |
| 927    | No file  | `d477e0f317fe`  |
| 911    | No file  | `d477e0f317fe`  |
| 904    | No file  | `d477e0f317fe`  |
| 899    | No file  | `d477e0f317fe`  |
| 894    | No file  | `d477e0f317fe`  |
| 885    | No file  | `d477e0f317fe`  |
| 879    | No file  | `d477e0f317fe`  |
| 872    | No file  | `d477e0f317fe`  |
| 864    | No file  | `d477e0f317fe`  |
| 855    | No file  | `d477e0f317fe`  |
| 853    | No file  | `d477e0f317fe`  |
| 845    | No file  | `d477e0f317fe`  |
| 837    | No file  | `d477e0f317fe`  |
| 829    | No file  | `d477e0f317fe`  |
| 822    | No file  | `d477e0f317fe`  |
| 814    | No file  | `d477e0f317fe`  |
| 805    | No file  | `d477e0f317fe`  |
| 794    | No file  | `d477e0f317fe`  |
| 787    | No file  | `d477e0f317fe`  |
| 780    | No file  | `d477e0f317fe`  |
| 771    | No file  | `d477e0f317fe`  |
| 760    | No file  | `d477e0f317fe`  |
| 748    | No file  | `d477e0f317fe`  |
| 741    | No file  | `d477e0f317fe`  |
| 736    | No file  | `d477e0f317fe`  |
| 731    | No file  | `d477e0f317fe`  |
| 723    | No file  | `d477e0f317fe`  |
| 711    | No file  | `d477e0f317fe`  |
| 707    | No file  | `d477e0f317fe`  |
| 697    | No file  | `d477e0f317fe`  |
| 689    | No file  | `d477e0f317fe`  |
| 683    | No file  | `d477e0f317fe`  |
| 678    | No file  | `d477e0f317fe`  |
| 670    | No file  | `d477e0f317fe`  |
| 661    | No file  | `d477e0f317fe`  |
| 656    | No file  | `d477e0f317fe`  |
| 652    | No file  | `d477e0f317fe`  |
| 643    | No file  | `d477e0f317fe`  |
| 637    | No file  | `d477e0f317fe`  |
| 630    | No file  | `d477e0f317fe`  |
| 627    | No file  | `d477e0f317fe`  |
| 621    | No file  | `d477e0f317fe`  |
| 617    | No file  | `d477e0f317fe`  |
| 615    | No file  | `d477e0f317fe`  |
| 606    | No file  | `d477e0f317fe`  |
| 599    | No file  | `d477e0f317fe`  |
| 592    | No file  | `d477e0f317fe`  |
| 586    | No file  | `d477e0f317fe`  |
| 577    | No file  | `d477e0f317fe`  |
| 569    | No file  | `d477e0f317fe`  |
| 561    | No file  | `d477e0f317fe`  |
| 554    | No file  | `d477e0f317fe`  |
| 542    | No file  | `d477e0f317fe`  |
| 532    | No file  | `d477e0f317fe`  |
| 531    | No file  | `d477e0f317fe`  |
| 526    | No file  | `d477e0f317fe`  |
| 521    | No file  | `d477e0f317fe`  |
| 517    | No file  | `d477e0f317fe`  |
| 510    | No file  | `d477e0f317fe`  |
| 508    | No file  | `d477e0f317fe`  |
| 504    | No file  | `d477e0f317fe`  |
| 497    | No file  | `d477e0f317fe`  |
| 491    | No file  | `d477e0f317fe`  |
| 485    | No file  | `d477e0f317fe`  |
| 478    | No file  | `d477e0f317fe`  |
| 472    | No file  | `d477e0f317fe`  |
| 466    | No file  | `d477e0f317fe`  |
| 457    | No file  | `d477e0f317fe`  |
| 452    | No file  | `d477e0f317fe`  |
| 449    | No file  | `d477e0f317fe`  |
| 435    | No file  | `d477e0f317fe`  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                                                   |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------- |
| `houseinfoneeditemoffset.dbss` | Optional | Index `need_item_key -> (offset, size)`, see below; the handler walks the rows in order and does not load it |
| `houseinforeceipe.dbss`        | Optional | The house uses whose `need_item_key` names each group                                  |
| `languagedata_en.loc`          | Optional | LOC type 16 house use names, LOC type 0 item names                                     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type           | Field     | Notes               |
| ------- | -------------- | --------- | ------------------- |
| `+0x00` | u32            | row_count | `11` on client 3474 |
| `+0x04` | Row[row_count] | rows      | See Row             |

The rows run from key 11 down to key 1 (client 3474).

### Row (variable: 2 bytes + levels)

| Offset  | Type     | Field         | Notes                                                    |
| ------- | -------- | ------------- | -------------------------------------------------------- |
| `+0x00` | u16      | need_item_key | Unique row key; `houseinforeceipe.dbss` `need_item_key` |
| `+0x02` | Level[6] | levels        | Slots 0 to 5, see Level                                  |

### Level (variable: 12 bytes + items)

| Offset  | Type                   | Field         | Notes                                                    |
| ------- | ---------------------- | ------------- | -------------------------------------------------------- |
| `+0x00` | i32                    | level         | The slot number, `0` to `5`                              |
| `+0x04` | i32                    | transfer_time | Seconds, see Transfer Time                               |
| `+0x08` | u32                    | item_count    | Number of need items                                     |
| `+0x0C` | Need Item[item_count]  | items         | See Need Item                                            |

Slot 0 holds level `0`, transfer time `0` and no items on every row of
clients 1784 and 3474, so every row is at least 74 bytes (`2 + 6 x 12`).

### Need Item (12 bytes)

| Offset  | Type | Field    | Notes                                                       |
| ------- | ---- | -------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_key | Item enchant key, see Notes; `1` (Silver, LOC type 0) on every item (client 3474) |
| `+0x04` | i64  | count    | Number of that item                                         |

No level holds more than one item on client 3474.

### `houseinfoneeditemoffset.dbss`

| Offset  | Type                 | Field     | Notes                                                    |
| ------- | -------------------- | --------- | -------------------------------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count`; `11` on client 3474 |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                                            |

Every index row points at the main row with the same key, in the main
file's order, and the rows tile the main file from `0x04` to the end with
no gap.

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | need_item_key | The main row's `need_item_key`                               |
| `+0x02` | u32  | offset        | Start of the row in `houseinfoneeditem.dbss`, at its `need_item_key` |
| `+0x06` | u32  | size          | Full row length, key included                                |

## Costs

The Silver each level takes (client 3474). A dash is a level with no items.
The [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md#need-item-join) Need
Item Join lists the house uses of each group.

| need_item_key | Lv 1  | Lv 2      | Lv 3   | Lv 4   | Lv 5    |
| ------------- | ----- | --------- | ------ | ------ | ------- |
| 1             | 500   | 1,000     | 2,500  | 5,000  | 10,000  |
| 2             | 2,000 | 3,500     | 7,000  | 10,000 | 15,000  |
| 3             | -     | -         | -      | -      | -       |
| 4             | -     | 1,000     | 3,000  | 7,000  | 15,000  |
| 5             | 2,000 | 1,000,000 | -      | -      | -       |
| 6             | 500   | 10,000    | 30,000 | -      | -       |
| 7             | 5,000 | 25,000    | 45,000 | 70,000 | 100,000 |
| 8             | 3,000 | 6,000     | 10,000 | 15,000 | 25,000  |
| 9             | 5,000 | 15,000    | 25,000 | 35,000 | -       |
| 10            | 1,000 | 3,000     | 7,000  | 18,000 | -       |
| 11            | 1,000 | 2,500     | 5,000  | 10,000 | 20,000  |

## Transfer Time

`transfer_time` is `5` on every priced level from 2 up and `0` on level 1
and on every level with no items (client 3474). On client 1784 it is `60`
times the level (`60` to `300`), `600` on group 5 level 2, `60` on the
empty level 1 of group 4, and `0` on group 3 and on the levels past the
last one groups 5, 6, 9 and 10 price. The house window reads it with
`getTransperTime(receipeKey, fromLevel, toLevel)`, names it `needTime_sec`
and passes it to `Util.Time.timeFormatting`; at `0` it shows `--`
(`panel_new_housecontrol.lua`). So the field is seconds, and a level change
on client 3474 takes 5 seconds. That matches the live game, where a level
change takes a few seconds; on older clients it took longer, as the 1784
values show.

## Field Names

The names follow the 2016 `gc::HouseInfoNeedItemStaticStatus`: `_key`
(u16), then `pa::Array<gc::HouseInfoNeedItemLevelGroup,6> _houseInfoList`.
A `HouseInfoNeedItemLevelGroup` is `int _level`, `int _transferTime` and a
vector of `gc::ItemStaticInformation`, whose `_key` is a
`gc::ItemEnchantKey` and `_count` an `__int64`. The six-slot array is why a
row holds slot 0.

The values match the `House_Transfer_New` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `TransferKey` and `Level`:

| Field         | Column                     | Same value (client 1784) | Same value (client 3474) |
| ------------- | -------------------------- | ------------------------ | ------------------------ |
| need_item_key | `TransferKey`              | 11 of 11 keys            | 11 of 11 keys            |
| level         | `Level`                    | 55 of 55 levels          | 55 of 55 levels          |
| transfer_time | `Time`                     | 55 of 55                 | 12 of 55                 |
| items         | `Itemkey1` to `ItemCount3` | 55 of 55                 | 55 of 55                 |

The sheet has no level 0 row; slot 0 is not compiled from it. Client 3474
sets the time to `0` or `5` (see Transfer Time); the 12 levels that still
match are the ones at `0` on both clients. The sheet holds three item
columns per level and fills only the first; the file counts its items.
The `ReceipeForTown_New` sheet of the same workbook names the
`houseinforeceipe.dbss` `need_item_key` column `TransferKey`: Residence
`3`, Lodging `1`, Storage `4` and Horse Ranch `1`, as on client 3474.

## Notes

- The house window asks for the items by receipe key and level
  (`getNeedItemListCount`, `getNeedItemListItemKey`,
  `getNeedItemListItemCount` in `panel_new_housecontrol.lua`), so the client
  goes from the receipe to its `need_item_key` row. It passes each item key
  to `getItemEnchantStaticStatus`, which takes an item enchant key
  (`enchant_level << 24 | item_id`, the packing `itemenchant.dbss` uses).
- `getNeedAllItemListCount(receipeKey, fromLevel, toLevel)` and the
  `fromLevel, toLevel` pair of `getTransperTime` read a range of levels, for
  a house raised several levels at once.
- Group 9 is the one no `houseinforeceipe.dbss` row names (client 3474).
- The level 2 price of group 5 (1,000,000 Silver) is the same on clients
  1784 and 3474.
- The offset file is the same 114 bytes on clients 1784 and 3474.
