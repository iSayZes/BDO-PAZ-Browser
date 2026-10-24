# `marblegamediceitemgroup.dbss` Format

## Purpose

The Black Spirit's Adventure dice drop groups: per group key the
[`marblegamediceitemkey.dbss`](marblegamediceitemkey_dbss.md) dice items it
drops. An item whose contents event is `98` grants one group (see Granting
Items). The file holds 44 groups with 55 entries on client 3482, 27 groups
with 38 entries on client 1784. Companion
`marblegamediceitemgroupoffset.dbss` lists where every group sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                 | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | ------------------------------------ | ----- | ---------------- | --------- |
| 1      | 1396 and later | 3483    | `marblegamediceitemgroup.dbss`       | 796   | 55 Entry, 44 Row | 8         |
| 1      | 1396 and later | 3483    | `marblegamediceitemgroupoffset.dbss` | 532   | 44 Offset Row    | 12        |

| Layout | File                                 | Known          | Unknown    |
| ------ | ------------------------------------ | -------------- | ---------- |
| 1      | `marblegamediceitemgroup.dbss`       | 796 B (100.0%) | 0 B (0.0%) |
| 1      | `marblegamediceitemgroupoffset.dbss` | 532 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `31dfd8bacd8f`  |
| 3482   | Layout 1 | `31dfd8bacd8f`  |
| 3474   | Layout 1 | `31dfd8bacd8f`  |
| 3473   | Layout 1 | `31dfd8bacd8f`  |
| 3464   | Layout 1 | `31dfd8bacd8f`  |
| 3458   | Layout 1 | `31dfd8bacd8f`  |
| 3454   | Layout 1 | `31dfd8bacd8f`  |
| 3444   | Layout 1 | `31dfd8bacd8f`  |
| 3435   | Layout 1 | `31dfd8bacd8f`  |
| 3426   | Layout 1 | `31dfd8bacd8f`  |
| 3418   | Layout 1 | `31dfd8bacd8f`  |
| 3412   | Layout 1 | `31dfd8bacd8f`  |
| 3402   | Layout 1 | `31dfd8bacd8f`  |
| 3396   | Layout 1 | `31dfd8bacd8f`  |
| 3387   | Layout 1 | `31dfd8bacd8f`  |
| 3381   | Layout 1 | `31dfd8bacd8f`  |
| 3373   | Layout 1 | `31dfd8bacd8f`  |
| 3364   | Layout 1 | `31dfd8bacd8f`  |
| 3356   | Layout 1 | `31dfd8bacd8f`  |
| 3349   | Layout 1 | `31dfd8bacd8f`  |
| 3342   | Layout 1 | `31dfd8bacd8f`  |
| 3335   | Layout 1 | `31dfd8bacd8f`  |
| 3326   | Layout 1 | `31dfd8bacd8f`  |
| 3321   | Layout 1 | `31dfd8bacd8f`  |
| 3314   | Layout 1 | `31dfd8bacd8f`  |
| 3303   | Layout 1 | `31dfd8bacd8f`  |
| 3302   | Layout 1 | `31dfd8bacd8f`  |
| 3293   | Layout 1 | `31dfd8bacd8f`  |
| 3283   | Layout 1 | `31dfd8bacd8f`  |
| 3275   | Layout 1 | `31dfd8bacd8f`  |
| 3267   | Layout 1 | `31dfd8bacd8f`  |
| 3258   | Layout 1 | `31dfd8bacd8f`  |
| 3251   | Layout 1 | `31dfd8bacd8f`  |
| 3242   | Layout 1 | `31dfd8bacd8f`  |
| 3235   | Layout 1 | `31dfd8bacd8f`  |
| 3229   | Layout 1 | `31dfd8bacd8f`  |
| 3212   | Layout 1 | `31dfd8bacd8f`  |
| 3203   | Layout 1 | `31dfd8bacd8f`  |
| 3193   | Layout 1 | `31dfd8bacd8f`  |
| 3186   | Layout 1 | `31dfd8bacd8f`  |
| 3177   | Layout 1 | `31dfd8bacd8f`  |
| 3169   | Layout 1 | `31dfd8bacd8f`  |
| 3158   | Layout 1 | `31dfd8bacd8f`  |
| 3151   | Layout 1 | `31dfd8bacd8f`  |
| 3144   | Layout 1 | `31dfd8bacd8f`  |
| 3133   | Layout 1 | `31dfd8bacd8f`  |
| 3125   | Layout 1 | `31dfd8bacd8f`  |
| 3118   | Layout 1 | `31dfd8bacd8f`  |
| 3111   | Layout 1 | `31dfd8bacd8f`  |
| 3103   | Layout 1 | `31dfd8bacd8f`  |
| 3095   | Layout 1 | `31dfd8bacd8f`  |
| 3086   | Layout 1 | `31dfd8bacd8f`  |
| 3072   | Layout 1 | `31dfd8bacd8f`  |
| 3062   | Layout 1 | `31dfd8bacd8f`  |
| 3052   | Layout 1 | `31dfd8bacd8f`  |
| 3045   | Layout 1 | `31dfd8bacd8f`  |
| 3037   | Layout 1 | `31dfd8bacd8f`  |
| 3030   | Layout 1 | `31dfd8bacd8f`  |
| 3021   | Layout 1 | `31dfd8bacd8f`  |
| 3012   | Layout 1 | `31dfd8bacd8f`  |
| 3002   | Layout 1 | `31dfd8bacd8f`  |
| 2995   | Layout 1 | `31dfd8bacd8f`  |
| 2987   | Layout 1 | `31dfd8bacd8f`  |
| 2978   | Layout 1 | `31dfd8bacd8f`  |
| 2970   | Layout 1 | `31dfd8bacd8f`  |
| 2959   | Layout 1 | `31dfd8bacd8f`  |
| 2951   | Layout 1 | `31dfd8bacd8f`  |
| 2942   | Layout 1 | `31dfd8bacd8f`  |
| 2935   | Layout 1 | `31dfd8bacd8f`  |
| 2932   | Layout 1 | `31dfd8bacd8f`  |
| 2923   | Layout 1 | `31dfd8bacd8f`  |
| 2919   | Layout 1 | `31dfd8bacd8f`  |
| 2907   | Layout 1 | `31dfd8bacd8f`  |
| 2900   | Layout 1 | `31dfd8bacd8f`  |
| 2891   | Layout 1 | `31dfd8bacd8f`  |
| 2882   | Layout 1 | `31dfd8bacd8f`  |
| 2872   | Layout 1 | `31dfd8bacd8f`  |
| 2863   | Layout 1 | `31dfd8bacd8f`  |
| 2855   | Layout 1 | `31dfd8bacd8f`  |
| 2849   | Layout 1 | `31dfd8bacd8f`  |
| 2844   | Layout 1 | `31dfd8bacd8f`  |
| 2834   | Layout 1 | `31dfd8bacd8f`  |
| 2825   | Layout 1 | `31dfd8bacd8f`  |
| 2819   | Layout 1 | `31dfd8bacd8f`  |
| 2811   | Layout 1 | `31dfd8bacd8f`  |
| 2803   | Layout 1 | `31dfd8bacd8f`  |
| 2794   | Layout 1 | `31dfd8bacd8f`  |
| 2783   | Layout 1 | `31dfd8bacd8f`  |
| 2774   | Layout 1 | `31dfd8bacd8f`  |
| 2765   | Layout 1 | `31dfd8bacd8f`  |
| 2756   | Layout 1 | `31dfd8bacd8f`  |
| 2750   | Layout 1 | `31dfd8bacd8f`  |
| 2743   | Layout 1 | `31dfd8bacd8f`  |
| 2736   | Layout 1 | `31dfd8bacd8f`  |
| 2726   | Layout 1 | `31dfd8bacd8f`  |
| 2717   | Layout 1 | `31dfd8bacd8f`  |
| 2709   | Layout 1 | `31dfd8bacd8f`  |
| 2703   | Layout 1 | `31dfd8bacd8f`  |
| 2695   | Layout 1 | `31dfd8bacd8f`  |
| 2684   | Layout 1 | `31dfd8bacd8f`  |
| 2672   | Layout 1 | `31dfd8bacd8f`  |
| 2665   | Layout 1 | `31dfd8bacd8f`  |
| 2657   | Layout 1 | `31dfd8bacd8f`  |
| 2649   | Layout 1 | `31dfd8bacd8f`  |
| 2644   | Layout 1 | `31dfd8bacd8f`  |
| 2637   | Layout 1 | `31dfd8bacd8f`  |
| 2629   | Layout 1 | `31dfd8bacd8f`  |
| 2619   | Layout 1 | `31dfd8bacd8f`  |
| 2612   | Layout 1 | `31dfd8bacd8f`  |
| 2606   | Layout 1 | `31dfd8bacd8f`  |
| 2602   | Layout 1 | `31dfd8bacd8f`  |
| 2601   | Layout 1 | `31dfd8bacd8f`  |
| 2592   | Layout 1 | `31dfd8bacd8f`  |
| 2583   | Layout 1 | `31dfd8bacd8f`  |
| 2575   | Layout 1 | `31dfd8bacd8f`  |
| 2567   | Layout 1 | `31dfd8bacd8f`  |
| 2560   | Layout 1 | `31dfd8bacd8f`  |
| 2553   | Layout 1 | `31dfd8bacd8f`  |
| 2545   | Layout 1 | `31dfd8bacd8f`  |
| 2538   | Layout 1 | `31dfd8bacd8f`  |
| 2529   | Layout 1 | `31dfd8bacd8f`  |
| 2519   | Layout 1 | `31dfd8bacd8f`  |
| 2513   | Layout 1 | `31dfd8bacd8f`  |
| 2510   | Layout 1 | `31dfd8bacd8f`  |
| 2507   | Layout 1 | `31dfd8bacd8f`  |
| 2503   | Layout 1 | `31dfd8bacd8f`  |
| 2498   | Layout 1 | `31dfd8bacd8f`  |
| 2492   | Layout 1 | `31dfd8bacd8f`  |
| 2487   | Layout 1 | `31dfd8bacd8f`  |
| 2480   | Layout 1 | `31dfd8bacd8f`  |
| 2474   | Layout 1 | `31dfd8bacd8f`  |
| 2468   | Layout 1 | `31dfd8bacd8f`  |
| 2460   | Layout 1 | `31dfd8bacd8f`  |
| 2453   | Layout 1 | `31dfd8bacd8f`  |
| 2444   | Layout 1 | `31dfd8bacd8f`  |
| 2438   | Layout 1 | `31dfd8bacd8f`  |
| 2434   | Layout 1 | `31dfd8bacd8f`  |
| 2429   | Layout 1 | `31dfd8bacd8f`  |
| 2421   | Layout 1 | `31dfd8bacd8f`  |
| 2414   | Layout 1 | `31dfd8bacd8f`  |
| 2407   | Layout 1 | `31dfd8bacd8f`  |
| 2401   | Layout 1 | `31dfd8bacd8f`  |
| 2397   | Layout 1 | `31dfd8bacd8f`  |
| 2393   | Layout 1 | `31dfd8bacd8f`  |
| 2384   | Layout 1 | `31dfd8bacd8f`  |
| 2378   | Layout 1 | `31dfd8bacd8f`  |
| 2372   | Layout 1 | `31dfd8bacd8f`  |
| 2358   | Layout 1 | `31dfd8bacd8f`  |
| 2352   | Layout 1 | `31dfd8bacd8f`  |
| 2347   | Layout 1 | `31dfd8bacd8f`  |
| 2343   | Layout 1 | `31dfd8bacd8f`  |
| 2335   | Layout 1 | `31dfd8bacd8f`  |
| 2327   | Layout 1 | `31dfd8bacd8f`  |
| 2324   | Layout 1 | `31dfd8bacd8f`  |
| 2319   | Layout 1 | `31dfd8bacd8f`  |
| 2313   | Layout 1 | `31dfd8bacd8f`  |
| 2308   | Layout 1 | `31dfd8bacd8f`  |
| 2302   | Layout 1 | `31dfd8bacd8f`  |
| 2295   | Layout 1 | `31dfd8bacd8f`  |
| 2290   | Layout 1 | `31dfd8bacd8f`  |
| 2284   | Layout 1 | `31dfd8bacd8f`  |
| 2276   | Layout 1 | `31dfd8bacd8f`  |
| 2269   | Layout 1 | `31dfd8bacd8f`  |
| 2259   | Layout 1 | `31dfd8bacd8f`  |
| 2250   | Layout 1 | `31dfd8bacd8f`  |
| 2243   | Layout 1 | `31dfd8bacd8f`  |
| 2235   | Layout 1 | `31dfd8bacd8f`  |
| 2229   | Layout 1 | `31dfd8bacd8f`  |
| 2224   | Layout 1 | `31dfd8bacd8f`  |
| 2218   | Layout 1 | `31dfd8bacd8f`  |
| 2215   | Layout 1 | `31dfd8bacd8f`  |
| 2207   | Layout 1 | `31dfd8bacd8f`  |
| 2203   | Layout 1 | `31dfd8bacd8f`  |
| 2196   | Layout 1 | `31dfd8bacd8f`  |
| 2192   | Layout 1 | `31dfd8bacd8f`  |
| 2189   | Layout 1 | `31dfd8bacd8f`  |
| 2183   | Layout 1 | `31dfd8bacd8f`  |
| 2179   | Layout 1 | `31dfd8bacd8f`  |
| 2171   | Layout 1 | `31dfd8bacd8f`  |
| 2163   | Layout 1 | `31dfd8bacd8f`  |
| 2156   | Layout 1 | `31dfd8bacd8f`  |
| 2151   | Layout 1 | `31dfd8bacd8f`  |
| 2147   | Layout 1 | `31dfd8bacd8f`  |
| 2142   | Layout 1 | `31dfd8bacd8f`  |
| 2138   | Layout 1 | `31dfd8bacd8f`  |
| 2134   | Layout 1 | `31dfd8bacd8f`  |
| 2130   | Layout 1 | `31dfd8bacd8f`  |
| 2122   | Layout 1 | `31dfd8bacd8f`  |
| 2107   | Layout 1 | `31dfd8bacd8f`  |
| 2098   | Layout 1 | `31dfd8bacd8f`  |
| 2089   | Layout 1 | `31dfd8bacd8f`  |
| 2081   | Layout 1 | `31dfd8bacd8f`  |
| 2073   | Layout 1 | `31dfd8bacd8f`  |
| 2067   | Layout 1 | `31dfd8bacd8f`  |
| 2063   | Layout 1 | `31dfd8bacd8f`  |
| 2059   | Layout 1 | `31dfd8bacd8f`  |
| 2052   | Layout 1 | `31dfd8bacd8f`  |
| 2044   | Layout 1 | `31dfd8bacd8f`  |
| 2039   | Layout 1 | `31dfd8bacd8f`  |
| 2032   | Layout 1 | `31dfd8bacd8f`  |
| 2025   | Layout 1 | `31dfd8bacd8f`  |
| 2011   | Layout 1 | `31dfd8bacd8f`  |
| 2005   | Layout 1 | `31dfd8bacd8f`  |
| 2000   | Layout 1 | `31dfd8bacd8f`  |
| 1996   | Layout 1 | `31dfd8bacd8f`  |
| 1991   | Layout 1 | `31dfd8bacd8f`  |
| 1985   | Layout 1 | `31dfd8bacd8f`  |
| 1980   | Layout 1 | `31dfd8bacd8f`  |
| 1969   | Layout 1 | `31dfd8bacd8f`  |
| 1964   | Layout 1 | `31dfd8bacd8f`  |
| 1958   | Layout 1 | `31dfd8bacd8f`  |
| 1950   | Layout 1 | `31dfd8bacd8f`  |
| 1945   | Layout 1 | `31dfd8bacd8f`  |
| 1937   | Layout 1 | `31dfd8bacd8f`  |
| 1933   | Layout 1 | `31dfd8bacd8f`  |
| 1927   | Layout 1 | `31dfd8bacd8f`  |
| 1921   | Layout 1 | `31dfd8bacd8f`  |
| 1914   | Layout 1 | `31dfd8bacd8f`  |
| 1908   | Layout 1 | `31dfd8bacd8f`  |
| 1897   | Layout 1 | `31dfd8bacd8f`  |
| 1892   | Layout 1 | `31dfd8bacd8f`  |
| 1886   | Layout 1 | `31dfd8bacd8f`  |
| 1881   | Layout 1 | `31dfd8bacd8f`  |
| 1871   | Layout 1 | `31dfd8bacd8f`  |
| 1866   | Layout 1 | `31dfd8bacd8f`  |
| 1862   | Layout 1 | `31dfd8bacd8f`  |
| 1854   | Layout 1 | `31dfd8bacd8f`  |
| 1846   | Layout 1 | `31dfd8bacd8f`  |
| 1838   | Layout 1 | `31dfd8bacd8f`  |
| 1832   | Layout 1 | `31dfd8bacd8f`  |
| 1826   | Layout 1 | `31dfd8bacd8f`  |
| 1822   | Layout 1 | `31dfd8bacd8f`  |
| 1818   | Layout 1 | `31dfd8bacd8f`  |
| 1804   | Layout 1 | `31dfd8bacd8f`  |
| 1794   | Layout 1 | `31dfd8bacd8f`  |
| 1790   | Layout 1 | `31dfd8bacd8f`  |
| 1784   | Layout 1 | `31dfd8bacd8f`  |
| 1774   | Layout 1 | `31dfd8bacd8f`  |
| 1771   | Layout 1 | `31dfd8bacd8f`  |
| 1762   | Layout 1 | `31dfd8bacd8f`  |
| 1759   | Layout 1 | `31dfd8bacd8f`  |
| 1754   | Layout 1 | `31dfd8bacd8f`  |
| 1749   | Layout 1 | `31dfd8bacd8f`  |
| 1743   | Layout 1 | `31dfd8bacd8f`  |
| 1737   | Layout 1 | `31dfd8bacd8f`  |
| 1731   | Layout 1 | `31dfd8bacd8f`  |
| 1725   | Layout 1 | `31dfd8bacd8f`  |
| 1717   | Layout 1 | `31dfd8bacd8f`  |
| 1710   | Layout 1 | `31dfd8bacd8f`  |
| 1704   | Layout 1 | `31dfd8bacd8f`  |
| 1698   | Layout 1 | `31dfd8bacd8f`  |
| 1690   | Layout 1 | `31dfd8bacd8f`  |
| 1685   | Layout 1 | `31dfd8bacd8f`  |
| 1680   | Layout 1 | `31dfd8bacd8f`  |
| 1674   | Layout 1 | `31dfd8bacd8f`  |
| 1668   | Layout 1 | `31dfd8bacd8f`  |
| 1659   | Layout 1 | `31dfd8bacd8f`  |
| 1649   | Layout 1 | `31dfd8bacd8f`  |
| 1642   | Layout 1 | `31dfd8bacd8f`  |
| 1636   | Layout 1 | `31dfd8bacd8f`  |
| 1628   | Layout 1 | `31dfd8bacd8f`  |
| 1622   | Layout 1 | `31dfd8bacd8f`  |
| 1614   | Layout 1 | `31dfd8bacd8f`  |
| 1608   | Layout 1 | `31dfd8bacd8f`  |
| 1602   | Layout 1 | `31dfd8bacd8f`  |
| 1598   | Layout 1 | `31dfd8bacd8f`  |
| 1594   | Layout 1 | `31dfd8bacd8f`  |
| 1590   | Layout 1 | `31dfd8bacd8f`  |
| 1587   | Layout 1 | `31dfd8bacd8f`  |
| 1584   | Layout 1 | `31dfd8bacd8f`  |
| 1579   | Layout 1 | `31dfd8bacd8f`  |
| 1572   | Layout 1 | `31dfd8bacd8f`  |
| 1565   | Layout 1 | `31dfd8bacd8f`  |
| 1559   | Layout 1 | `31dfd8bacd8f`  |
| 1554   | Layout 1 | `31dfd8bacd8f`  |
| 1547   | Layout 1 | `31dfd8bacd8f`  |
| 1537   | Layout 1 | `31dfd8bacd8f`  |
| 1529   | Layout 1 | `31dfd8bacd8f`  |
| 1524   | Layout 1 | `31dfd8bacd8f`  |
| 1519   | Layout 1 | `31dfd8bacd8f`  |
| 1509   | Layout 1 | `31dfd8bacd8f`  |
| 1506   | Layout 1 | `31dfd8bacd8f`  |
| 1504   | Layout 1 | `31dfd8bacd8f`  |
| 1500   | Layout 1 | `31dfd8bacd8f`  |
| 1493   | Layout 1 | `31dfd8bacd8f`  |
| 1489   | Layout 1 | `31dfd8bacd8f`  |
| 1485   | Layout 1 | `31dfd8bacd8f`  |
| 1481   | Layout 1 | `31dfd8bacd8f`  |
| 1474   | Layout 1 | `31dfd8bacd8f`  |
| 1466   | Layout 1 | `31dfd8bacd8f`  |
| 1462   | Layout 1 | `31dfd8bacd8f`  |
| 1459   | Layout 1 | `31dfd8bacd8f`  |
| 1453   | Layout 1 | `31dfd8bacd8f`  |
| 1450   | Layout 1 | `31dfd8bacd8f`  |
| 1445   | Layout 1 | `31dfd8bacd8f`  |
| 1439   | Layout 1 | `31dfd8bacd8f`  |
| 1433   | Layout 1 | `31dfd8bacd8f`  |
| 1430   | Layout 1 | `31dfd8bacd8f`  |
| 1426   | Layout 1 | `31dfd8bacd8f`  |
| 1421   | Layout 1 | `31dfd8bacd8f`  |
| 1417   | Layout 1 | `31dfd8bacd8f`  |
| 1416   | Layout 1 | `31dfd8bacd8f`  |
| 1409   | Layout 1 | `31dfd8bacd8f`  |
| 1405   | Layout 1 | `31dfd8bacd8f`  |
| 1401   | Layout 1 | `31dfd8bacd8f`  |
| 1396   | Layout 1 | `31dfd8bacd8f`  |
| 1391   | No file  | `31dfd8bacd8f`  |
| 1390   | No file  | `31dfd8bacd8f`  |
| 1386   | No file  | `31dfd8bacd8f`  |
| 1381   | No file  | `31dfd8bacd8f`  |
| 1379   | No file  | `31dfd8bacd8f`  |
| 1372   | No file  | `31dfd8bacd8f`  |
| 1366   | No file  | `31dfd8bacd8f`  |
| 1364   | No file  | `31dfd8bacd8f`  |
| 1363   | No file  | `31dfd8bacd8f`  |
| 1360   | No file  | `31dfd8bacd8f`  |
| 1358   | No file  | `31dfd8bacd8f`  |
| 1355   | No file  | `31dfd8bacd8f`  |
| 1351   | No file  | `31dfd8bacd8f`  |
| 1348   | No file  | `31dfd8bacd8f`  |
| 1346   | No file  | `31dfd8bacd8f`  |
| 1341   | No file  | `31dfd8bacd8f`  |
| 1340   | No file  | `31dfd8bacd8f`  |
| 1338   | No file  | `31dfd8bacd8f`  |
| 1335   | No file  | `31dfd8bacd8f`  |
| 1333   | No file  | `31dfd8bacd8f`  |
| 1329   | No file  | `31dfd8bacd8f`  |
| 1327   | No file  | `31dfd8bacd8f`  |
| 1324   | No file  | `31dfd8bacd8f`  |
| 1321   | No file  | `31dfd8bacd8f`  |
| 1319   | No file  | `31dfd8bacd8f`  |
| 1318   | No file  | `31dfd8bacd8f`  |
| 1316   | No file  | `31dfd8bacd8f`  |
| 1313   | No file  | `31dfd8bacd8f`  |
| 1311   | No file  | `31dfd8bacd8f`  |
| 1309   | No file  | `31dfd8bacd8f`  |
| 1304   | No file  | `31dfd8bacd8f`  |
| 1292   | No file  | `31dfd8bacd8f`  |
| 1286   | No file  | `31dfd8bacd8f`  |
| 1280   | No file  | `31dfd8bacd8f`  |
| 1276   | No file  | `31dfd8bacd8f`  |
| 1267   | No file  | `31dfd8bacd8f`  |
| 1261   | No file  | `31dfd8bacd8f`  |
| 1256   | No file  | `31dfd8bacd8f`  |
| 1250   | No file  | `31dfd8bacd8f`  |
| 1246   | No file  | `31dfd8bacd8f`  |
| 1239   | No file  | `31dfd8bacd8f`  |
| 1230   | No file  | `31dfd8bacd8f`  |
| 1226   | No file  | `31dfd8bacd8f`  |
| 1220   | No file  | `31dfd8bacd8f`  |
| 1217   | No file  | `31dfd8bacd8f`  |
| 1211   | No file  | `31dfd8bacd8f`  |
| 1210   | No file  | `31dfd8bacd8f`  |
| 1208   | No file  | `31dfd8bacd8f`  |
| 1203   | No file  | `31dfd8bacd8f`  |
| 1197   | No file  | `31dfd8bacd8f`  |
| 1194   | No file  | `31dfd8bacd8f`  |
| 1192   | No file  | `31dfd8bacd8f`  |
| 1187   | No file  | `31dfd8bacd8f`  |
| 1183   | No file  | `31dfd8bacd8f`  |
| 1177   | No file  | `31dfd8bacd8f`  |
| 1173   | No file  | `31dfd8bacd8f`  |
| 1167   | No file  | `31dfd8bacd8f`  |
| 1164   | No file  | `31dfd8bacd8f`  |
| 1156   | No file  | `31dfd8bacd8f`  |
| 1149   | No file  | `31dfd8bacd8f`  |
| 1144   | No file  | `31dfd8bacd8f`  |
| 1137   | No file  | `31dfd8bacd8f`  |
| 1132   | No file  | `31dfd8bacd8f`  |
| 1127   | No file  | `31dfd8bacd8f`  |
| 1122   | No file  | `31dfd8bacd8f`  |
| 1118   | No file  | `31dfd8bacd8f`  |
| 1114   | No file  | `31dfd8bacd8f`  |
| 1109   | No file  | `31dfd8bacd8f`  |
| 1102   | No file  | `31dfd8bacd8f`  |
| 1096   | No file  | `31dfd8bacd8f`  |
| 1088   | No file  | `31dfd8bacd8f`  |
| 1081   | No file  | `31dfd8bacd8f`  |
| 1076   | No file  | `31dfd8bacd8f`  |
| 1069   | No file  | `31dfd8bacd8f`  |
| 1064   | No file  | `31dfd8bacd8f`  |
| 1058   | No file  | `31dfd8bacd8f`  |
| 1051   | No file  | `31dfd8bacd8f`  |
| 1044   | No file  | `31dfd8bacd8f`  |
| 1036   | No file  | `31dfd8bacd8f`  |
| 1026   | No file  | `31dfd8bacd8f`  |
| 1016   | No file  | `31dfd8bacd8f`  |
| 1009   | No file  | `31dfd8bacd8f`  |
| 1005   | No file  | `31dfd8bacd8f`  |
| 1000   | No file  | `31dfd8bacd8f`  |
| 998    | No file  | `31dfd8bacd8f`  |
| 990    | No file  | `31dfd8bacd8f`  |
| 979    | No file  | `31dfd8bacd8f`  |
| 972    | No file  | `31dfd8bacd8f`  |
| 963    | No file  | `31dfd8bacd8f`  |
| 955    | No file  | `31dfd8bacd8f`  |
| 946    | No file  | `31dfd8bacd8f`  |
| 938    | No file  | `31dfd8bacd8f`  |
| 927    | No file  | `31dfd8bacd8f`  |
| 911    | No file  | `31dfd8bacd8f`  |
| 904    | No file  | `31dfd8bacd8f`  |
| 899    | No file  | `31dfd8bacd8f`  |
| 894    | No file  | `31dfd8bacd8f`  |
| 885    | No file  | `31dfd8bacd8f`  |
| 879    | No file  | `31dfd8bacd8f`  |
| 872    | No file  | `31dfd8bacd8f`  |
| 864    | No file  | `31dfd8bacd8f`  |
| 855    | No file  | `31dfd8bacd8f`  |
| 853    | No file  | `31dfd8bacd8f`  |
| 845    | No file  | `31dfd8bacd8f`  |
| 837    | No file  | `31dfd8bacd8f`  |
| 829    | No file  | `31dfd8bacd8f`  |
| 822    | No file  | `31dfd8bacd8f`  |
| 814    | No file  | `31dfd8bacd8f`  |
| 805    | No file  | `31dfd8bacd8f`  |
| 794    | No file  | `31dfd8bacd8f`  |
| 787    | No file  | `31dfd8bacd8f`  |
| 780    | No file  | `31dfd8bacd8f`  |
| 771    | No file  | `31dfd8bacd8f`  |
| 760    | No file  | `31dfd8bacd8f`  |
| 748    | No file  | `31dfd8bacd8f`  |
| 741    | No file  | `31dfd8bacd8f`  |
| 736    | No file  | `31dfd8bacd8f`  |
| 731    | No file  | `31dfd8bacd8f`  |
| 723    | No file  | `31dfd8bacd8f`  |
| 711    | No file  | `31dfd8bacd8f`  |
| 707    | No file  | `31dfd8bacd8f`  |
| 697    | No file  | `31dfd8bacd8f`  |
| 689    | No file  | `31dfd8bacd8f`  |
| 683    | No file  | `31dfd8bacd8f`  |
| 678    | No file  | `31dfd8bacd8f`  |
| 670    | No file  | `31dfd8bacd8f`  |
| 661    | No file  | `31dfd8bacd8f`  |
| 656    | No file  | `31dfd8bacd8f`  |
| 652    | No file  | `31dfd8bacd8f`  |
| 643    | No file  | `31dfd8bacd8f`  |
| 637    | No file  | `31dfd8bacd8f`  |
| 630    | No file  | `31dfd8bacd8f`  |
| 627    | No file  | `31dfd8bacd8f`  |
| 621    | No file  | `31dfd8bacd8f`  |
| 617    | No file  | `31dfd8bacd8f`  |
| 615    | No file  | `31dfd8bacd8f`  |
| 606    | No file  | `31dfd8bacd8f`  |
| 599    | No file  | `31dfd8bacd8f`  |
| 592    | No file  | `31dfd8bacd8f`  |
| 586    | No file  | `31dfd8bacd8f`  |
| 577    | No file  | `31dfd8bacd8f`  |
| 569    | No file  | `31dfd8bacd8f`  |
| 561    | No file  | `31dfd8bacd8f`  |
| 554    | No file  | `31dfd8bacd8f`  |
| 542    | No file  | `31dfd8bacd8f`  |
| 532    | No file  | `31dfd8bacd8f`  |
| 531    | No file  | `31dfd8bacd8f`  |
| 526    | No file  | `31dfd8bacd8f`  |
| 521    | No file  | `31dfd8bacd8f`  |
| 517    | No file  | `31dfd8bacd8f`  |
| 510    | No file  | `31dfd8bacd8f`  |
| 508    | No file  | `31dfd8bacd8f`  |
| 504    | No file  | `31dfd8bacd8f`  |
| 497    | No file  | `31dfd8bacd8f`  |
| 491    | No file  | `31dfd8bacd8f`  |
| 485    | No file  | `31dfd8bacd8f`  |
| 478    | No file  | `31dfd8bacd8f`  |
| 472    | No file  | `31dfd8bacd8f`  |
| 466    | No file  | `31dfd8bacd8f`  |
| 457    | No file  | `31dfd8bacd8f`  |
| 452    | No file  | `31dfd8bacd8f`  |
| 449    | No file  | `31dfd8bacd8f`  |
| 435    | No file  | `31dfd8bacd8f`  |

<!-- versions:end -->

## Companion Files

| File                                 | Required | Role                                                                          |
| ------------------------------------ | -------- | ----------------------------------------------------------------------------- |
| `marblegamediceitemgroupoffset.dbss` | Optional | `dice_drop_group_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `itemenchant.dbss`                   | Optional | The items that grant each group; the handler reads them from the `MARBLE_DICE_GROUP_ITEMS` lookup index, not as a companion |
| `languagedata_en.loc`                | Optional | Item names (type 0)                                                           |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes            |
| ------- | ---------- | ----- | ---------------- |
| `+0x00` | u32        | count | Number of groups |
| `+0x04` | Row[count] | rows  | See Row          |

On client 3482 the file is 4 + 44 x 8 + 55 x 8 = 796 bytes.

### Row (variable: 8 bytes + entries)

| Offset  | Type               | Field               | Notes                                                    |
| ------- | ------------------ | ------------------- | -------------------------------------------------------- |
| `+0x00` | u32                | dice_drop_group_key | Row key; each key once                                   |
| `+0x04` | u32                | entry_count         | Number of `entries`; `1` on every group but `8` (7) and `9` (6), clients 1784 and 3482 |
| `+0x08` | Entry[entry_count] | entries             | See Entry                                                |

### Entry (8 bytes)

| Offset  | Type | Field         | Notes                                                              |
| ------- | ---- | ------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | dice_item_key | A `marblegamediceitemkey.dbss` key                                 |
| `+0x04` | u32  | rate          | `0` on every entry of clients 1784 and 3482, see Field Names       |

### `marblegamediceitemgroupoffset.dbss`

Bare offset table into `marblegamediceitemgroup.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                          |
| ------- | ----------------- | ----- | ---------------------------------------------- |
| `+0x00` | u32               | count | Equals the `marblegamediceitemgroup.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                 |

### Offset Row (12 bytes)

| Offset  | Type | Field               | Notes                                   |
| ------- | ---- | ------------------- | --------------------------------------- |
| `+0x00` | u32  | dice_drop_group_key | Key of the row it points at             |
| `+0x04` | u32  | data_offset         | Row start, at `dice_drop_group_key`     |
| `+0x08` | u32  | data_size           | The whole row: `8 + 8 * entry_count`    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order; on clients 1784 and 3482 every index row
points at the row with its key.

## Groups

On client 3482 the groups hold:

| Groups           | Dice item keys                   |
| ---------------- | -------------------------------- |
| `1` to `7`       | The key of the same number       |
| `8`              | `1` to `7`                       |
| `9`              | `2` to `7`                       |
| `10`             | `8`                              |
| `11` to `31`     | The key of the same number       |
| `1001` to `1006` | `101` to `106`                   |
| `1007` to `1009` | `301` to `303`                   |
| `1010` to `1013` | `401`, `601`, `701`, `801`       |

Groups `1` to `14` and `1001` to `1013` are the 27 groups of client 1784;
`15` to `31` are new on client 3482.

## Granting Items

An item with contents event `98` in
[`itemenchant.dbss`](itemenchant_dbss.md) names a group in
`contents_event_param1`. On client 3482, 42 base items have the event and
each names a group key of this file. Groups `9`, `10` and `1001` to `1013`
are not dice item keys, so the parameter is the group key and not the dice
item key: Black Spirit's Dice `756438` grants group `9`, `756437` group
`10`, and Pace of Delight - 1 Square `756440` group `1001`. Groups `8`,
`18` and `19` have no item on client 3482. The `MARBLE_DICE_GROUP_ITEMS`
lookup index (`build_marble_dice_group_item_index()` in
`_dbss/itemenchant/parser.py`) maps each group to its items, and the view
shows them in the Items column.

## Field Names

The `DiceItemGroup_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `DiceDropGroupKey`, `DiceItemKey` and `Rate`,
one sheet row per entry. Its 38 rows are the 38 entries of the client 1784
file (27 groups), and all 38 are in the client 3482 file. In the `.xlsm`
copy of the sheet (`datasheet_itemdatatable_marblegamedice.xlsm`) the
column is `%Rate`, server-only, which the client build writes as `0`; the
sheet's rates are parts of 1,000,000 (group `8`: `940000` on die `1`,
`10000` on each of `2` to `7`). Its note column `#Desc` is not compiled.
The count in front of the entries has no sheet column; the file groups the
sheet rows by key, so it is `entry_count`.

## Notes

- No client Lua reads the table; Black Spirit's Adventure runs in a web
  control (see [`marblegamediceitemkey.dbss`](marblegamediceitemkey_dbss.md)).
- The view shows one row per group: its key, the items that grant it and its
  dice item keys, each a link to its `marblegamediceitemkey.dbss` row.

## Open Questions

### Groups Without an Item

Groups `8` (die `1` at 94% and the one-face dice `2` to `7` at 1% each, by
the client 1784 sheet), `18` and `19` are granted by no item on client
3482. Whether the web side draws them for the board's free rolls is open.
