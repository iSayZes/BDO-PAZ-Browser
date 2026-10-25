# `innstaticstatus.dbss` Format

## Purpose

The inns and their rooms: one row per inn with a list of room characters.
On clients 1784 and 3482 the file holds one inn, key `1`, whose rooms are
every house character of [`householdlist.bss`](../bss/householdlist_bss.md) in
another order: 865 on client 3482, 801 on client 1784. Companion
`innstaticstatusoffset.dbss` lists where the row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records      | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | ------------ | --------- |
| 1      | 1346 and later | `innstaticstatus.dbss`       | 1,740 | 1 Row        | 1,736     |
| 1      | 1346 and later | `innstaticstatusoffset.dbss` | 14    | 1 Offset Row | 10        |

| Layout | File                         | Known            | Unknown    |
| ------ | ---------------------------- | ---------------- | ---------- |
| 1      | `innstaticstatus.dbss`       | 1,740 B (100.0%) | 0 B (0.0%) |
| 1      | `innstaticstatusoffset.dbss` | 14 B (100.0%)    | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `c7a4776c4611`  |
| 3482   | Layout 1             | `c7a4776c4611`  |
| 3474   | Layout 1             | `c7a4776c4611`  |
| 3473   | Layout 1             | `c7a4776c4611`  |
| 3464   | Layout 1             | `c7a4776c4611`  |
| 3458   | Layout 1             | `c7a4776c4611`  |
| 3454   | Layout 1             | `c7a4776c4611`  |
| 3444   | Layout 1             | `c7a4776c4611`  |
| 3435   | Layout 1             | `c7a4776c4611`  |
| 3426   | Layout 1             | `c7a4776c4611`  |
| 3418   | Layout 1             | `c7a4776c4611`  |
| 3412   | Layout 1             | `c7a4776c4611`  |
| 3402   | Layout 1             | `c7a4776c4611`  |
| 3396   | Layout 1             | `c7a4776c4611`  |
| 3387   | Layout 1             | `c7a4776c4611`  |
| 3381   | Layout 1             | `c7a4776c4611`  |
| 3373   | Layout 1             | `c7a4776c4611`  |
| 3364   | Layout 1             | `c7a4776c4611`  |
| 3356   | Layout 1             | `c7a4776c4611`  |
| 3349   | Layout 1             | `c7a4776c4611`  |
| 3342   | Layout 1             | `c7a4776c4611`  |
| 3335   | Layout 1             | `c7a4776c4611`  |
| 3326   | Layout 1             | `c7a4776c4611`  |
| 3321   | Layout 1             | `c7a4776c4611`  |
| 3314   | Layout 1             | `c7a4776c4611`  |
| 3303   | Layout 1             | `c7a4776c4611`  |
| 3302   | Layout 1             | `c7a4776c4611`  |
| 3293   | Layout 1             | `c7a4776c4611`  |
| 3283   | Layout 1             | `c7a4776c4611`  |
| 3275   | Layout 1             | `c7a4776c4611`  |
| 3267   | Layout 1             | `c7a4776c4611`  |
| 3258   | Layout 1             | `c7a4776c4611`  |
| 3251   | Layout 1             | `c7a4776c4611`  |
| 3242   | Layout 1             | `c7a4776c4611`  |
| 3235   | Layout 1             | `c7a4776c4611`  |
| 3229   | Layout 1             | `c7a4776c4611`  |
| 3212   | Layout 1             | `c7a4776c4611`  |
| 3203   | Layout 1             | `c7a4776c4611`  |
| 3193   | Layout 1             | `c7a4776c4611`  |
| 3186   | Layout 1             | `c7a4776c4611`  |
| 3177   | Layout 1             | `c7a4776c4611`  |
| 3169   | Layout 1             | `c7a4776c4611`  |
| 3158   | Layout 1             | `c7a4776c4611`  |
| 3151   | Layout 1             | `c7a4776c4611`  |
| 3144   | Layout 1             | `c7a4776c4611`  |
| 3133   | Layout 1             | `c7a4776c4611`  |
| 3125   | Layout 1             | `c7a4776c4611`  |
| 3118   | Layout 1             | `c7a4776c4611`  |
| 3111   | Layout 1             | `c7a4776c4611`  |
| 3103   | Layout 1             | `c7a4776c4611`  |
| 3095   | Layout 1             | `c7a4776c4611`  |
| 3086   | Layout 1             | `c7a4776c4611`  |
| 3072   | Layout 1             | `c7a4776c4611`  |
| 3062   | Layout 1             | `c7a4776c4611`  |
| 3052   | Layout 1             | `c7a4776c4611`  |
| 3045   | Layout 1             | `c7a4776c4611`  |
| 3037   | Layout 1             | `c7a4776c4611`  |
| 3030   | Layout 1             | `c7a4776c4611`  |
| 3021   | Layout 1             | `c7a4776c4611`  |
| 3012   | Layout 1             | `c7a4776c4611`  |
| 3002   | Layout 1             | `c7a4776c4611`  |
| 2995   | Layout 1             | `c7a4776c4611`  |
| 2987   | Layout 1             | `c7a4776c4611`  |
| 2978   | Layout 1             | `c7a4776c4611`  |
| 2970   | Layout 1             | `c7a4776c4611`  |
| 2959   | Layout 1             | `c7a4776c4611`  |
| 2951   | Layout 1             | `c7a4776c4611`  |
| 2942   | Layout 1             | `c7a4776c4611`  |
| 2935   | Layout 1             | `c7a4776c4611`  |
| 2932   | Layout 1             | `c7a4776c4611`  |
| 2923   | Layout 1             | `c7a4776c4611`  |
| 2919   | Layout 1             | `c7a4776c4611`  |
| 2907   | Layout 1             | `c7a4776c4611`  |
| 2900   | Layout 1             | `c7a4776c4611`  |
| 2891   | Layout 1             | `c7a4776c4611`  |
| 2882   | Layout 1             | `c7a4776c4611`  |
| 2872   | Layout 1             | `c7a4776c4611`  |
| 2863   | Layout 1             | `c7a4776c4611`  |
| 2855   | Layout 1             | `c7a4776c4611`  |
| 2849   | Layout 1             | `c7a4776c4611`  |
| 2844   | Layout 1             | `c7a4776c4611`  |
| 2834   | Layout 1             | `c7a4776c4611`  |
| 2825   | Layout 1             | `c7a4776c4611`  |
| 2819   | Layout 1             | `c7a4776c4611`  |
| 2811   | Layout 1             | `c7a4776c4611`  |
| 2803   | Layout 1             | `c7a4776c4611`  |
| 2794   | Layout 1             | `c7a4776c4611`  |
| 2783   | Layout 1             | `c7a4776c4611`  |
| 2774   | Layout 1             | `c7a4776c4611`  |
| 2765   | Layout 1             | `c7a4776c4611`  |
| 2756   | Layout 1             | `c7a4776c4611`  |
| 2750   | Layout 1             | `c7a4776c4611`  |
| 2743   | Layout 1             | `c7a4776c4611`  |
| 2736   | Layout 1             | `c7a4776c4611`  |
| 2726   | Layout 1             | `c7a4776c4611`  |
| 2717   | Layout 1             | `c7a4776c4611`  |
| 2709   | Layout 1             | `c7a4776c4611`  |
| 2703   | Layout 1             | `c7a4776c4611`  |
| 2695   | Layout 1             | `c7a4776c4611`  |
| 2684   | Layout 1             | `c7a4776c4611`  |
| 2672   | Layout 1             | `c7a4776c4611`  |
| 2665   | Layout 1             | `c7a4776c4611`  |
| 2657   | Layout 1             | `c7a4776c4611`  |
| 2649   | Layout 1             | `c7a4776c4611`  |
| 2644   | Layout 1             | `c7a4776c4611`  |
| 2637   | Layout 1             | `c7a4776c4611`  |
| 2629   | Layout 1             | `c7a4776c4611`  |
| 2619   | Layout 1             | `c7a4776c4611`  |
| 2612   | Layout 1             | `c7a4776c4611`  |
| 2606   | Layout 1             | `c7a4776c4611`  |
| 2602   | Layout 1             | `c7a4776c4611`  |
| 2601   | Layout 1             | `c7a4776c4611`  |
| 2592   | Layout 1             | `c7a4776c4611`  |
| 2583   | Layout 1             | `c7a4776c4611`  |
| 2575   | Layout 1             | `c7a4776c4611`  |
| 2567   | Layout 1             | `c7a4776c4611`  |
| 2560   | Layout 1             | `c7a4776c4611`  |
| 2553   | Layout 1             | `c7a4776c4611`  |
| 2545   | Layout 1             | `c7a4776c4611`  |
| 2538   | Layout 1             | `c7a4776c4611`  |
| 2529   | Layout 1             | `c7a4776c4611`  |
| 2519   | Layout 1             | `c7a4776c4611`  |
| 2513   | Layout 1             | `c7a4776c4611`  |
| 2510   | Layout 1             | `c7a4776c4611`  |
| 2507   | Layout 1             | `c7a4776c4611`  |
| 2503   | Layout 1             | `c7a4776c4611`  |
| 2498   | Layout 1             | `c7a4776c4611`  |
| 2492   | Layout 1             | `c7a4776c4611`  |
| 2487   | Layout 1             | `c7a4776c4611`  |
| 2480   | Layout 1             | `c7a4776c4611`  |
| 2474   | Layout 1             | `c7a4776c4611`  |
| 2468   | Layout 1             | `c7a4776c4611`  |
| 2460   | Layout 1             | `c7a4776c4611`  |
| 2453   | Layout 1             | `c7a4776c4611`  |
| 2444   | Layout 1             | `c7a4776c4611`  |
| 2438   | Layout 1             | `c7a4776c4611`  |
| 2434   | Layout 1             | `c7a4776c4611`  |
| 2429   | Layout 1             | `c7a4776c4611`  |
| 2421   | Layout 1             | `c7a4776c4611`  |
| 2414   | Layout 1             | `c7a4776c4611`  |
| 2407   | Layout 1             | `c7a4776c4611`  |
| 2401   | Layout 1             | `c7a4776c4611`  |
| 2397   | Layout 1             | `c7a4776c4611`  |
| 2393   | Layout 1             | `c7a4776c4611`  |
| 2384   | Layout 1             | `c7a4776c4611`  |
| 2378   | Layout 1             | `c7a4776c4611`  |
| 2372   | Layout 1             | `c7a4776c4611`  |
| 2358   | Layout 1             | `c7a4776c4611`  |
| 2352   | Layout 1             | `c7a4776c4611`  |
| 2347   | Layout 1             | `c7a4776c4611`  |
| 2343   | Layout 1             | `c7a4776c4611`  |
| 2335   | Layout 1             | `c7a4776c4611`  |
| 2327   | Layout 1             | `c7a4776c4611`  |
| 2324   | Layout 1             | `c7a4776c4611`  |
| 2319   | Layout 1             | `c7a4776c4611`  |
| 2313   | Layout 1             | `c7a4776c4611`  |
| 2308   | Layout 1             | `c7a4776c4611`  |
| 2302   | Layout 1             | `c7a4776c4611`  |
| 2295   | Layout 1             | `c7a4776c4611`  |
| 2290   | Layout 1             | `c7a4776c4611`  |
| 2284   | Layout 1             | `c7a4776c4611`  |
| 2276   | Layout 1             | `c7a4776c4611`  |
| 2269   | Layout 1             | `c7a4776c4611`  |
| 2259   | Layout 1             | `c7a4776c4611`  |
| 2250   | Layout 1             | `c7a4776c4611`  |
| 2243   | Layout 1             | `c7a4776c4611`  |
| 2235   | Layout 1             | `c7a4776c4611`  |
| 2229   | Layout 1             | `c7a4776c4611`  |
| 2224   | Layout 1             | `c7a4776c4611`  |
| 2218   | Layout 1             | `c7a4776c4611`  |
| 2215   | Layout 1             | `c7a4776c4611`  |
| 2207   | Layout 1             | `c7a4776c4611`  |
| 2203   | Layout 1             | `c7a4776c4611`  |
| 2196   | Layout 1             | `c7a4776c4611`  |
| 2192   | Layout 1             | `c7a4776c4611`  |
| 2189   | Layout 1             | `c7a4776c4611`  |
| 2183   | Layout 1             | `c7a4776c4611`  |
| 2179   | Layout 1             | `c7a4776c4611`  |
| 2171   | Layout 1             | `c7a4776c4611`  |
| 2163   | Layout 1             | `c7a4776c4611`  |
| 2156   | Layout 1             | `c7a4776c4611`  |
| 2151   | Layout 1             | `c7a4776c4611`  |
| 2147   | Layout 1             | `c7a4776c4611`  |
| 2142   | Layout 1             | `c7a4776c4611`  |
| 2138   | Layout 1             | `c7a4776c4611`  |
| 2134   | Layout 1             | `c7a4776c4611`  |
| 2130   | Layout 1             | `c7a4776c4611`  |
| 2122   | Layout 1             | `c7a4776c4611`  |
| 2107   | Layout 1             | `c7a4776c4611`  |
| 2098   | Layout 1             | `c7a4776c4611`  |
| 2089   | Layout 1             | `c7a4776c4611`  |
| 2081   | Layout 1             | `c7a4776c4611`  |
| 2073   | Layout 1             | `c7a4776c4611`  |
| 2067   | Layout 1             | `c7a4776c4611`  |
| 2063   | Layout 1             | `c7a4776c4611`  |
| 2059   | Layout 1             | `c7a4776c4611`  |
| 2052   | Layout 1             | `c7a4776c4611`  |
| 2044   | Layout 1             | `c7a4776c4611`  |
| 2039   | Layout 1             | `c7a4776c4611`  |
| 2032   | Layout 1             | `c7a4776c4611`  |
| 2025   | Layout 1             | `c7a4776c4611`  |
| 2011   | Layout 1             | `c7a4776c4611`  |
| 2005   | Layout 1             | `c7a4776c4611`  |
| 2000   | Layout 1             | `c7a4776c4611`  |
| 1996   | Layout 1             | `c7a4776c4611`  |
| 1991   | Layout 1             | `c7a4776c4611`  |
| 1985   | Layout 1             | `c7a4776c4611`  |
| 1980   | Layout 1             | `c7a4776c4611`  |
| 1969   | Layout 1             | `c7a4776c4611`  |
| 1964   | Layout 1             | `c7a4776c4611`  |
| 1958   | Layout 1             | `c7a4776c4611`  |
| 1950   | Layout 1             | `c7a4776c4611`  |
| 1945   | Layout 1             | `c7a4776c4611`  |
| 1937   | Layout 1             | `c7a4776c4611`  |
| 1933   | Layout 1             | `c7a4776c4611`  |
| 1927   | Layout 1             | `c7a4776c4611`  |
| 1921   | Layout 1             | `c7a4776c4611`  |
| 1914   | Layout 1             | `c7a4776c4611`  |
| 1908   | Layout 1             | `c7a4776c4611`  |
| 1897   | Layout 1             | `c7a4776c4611`  |
| 1892   | Layout 1             | `c7a4776c4611`  |
| 1886   | Layout 1             | `c7a4776c4611`  |
| 1881   | Layout 1             | `c7a4776c4611`  |
| 1871   | Layout 1             | `c7a4776c4611`  |
| 1866   | Layout 1             | `c7a4776c4611`  |
| 1862   | Layout 1             | `c7a4776c4611`  |
| 1854   | Layout 1             | `c7a4776c4611`  |
| 1846   | Layout 1             | `c7a4776c4611`  |
| 1838   | Layout 1             | `c7a4776c4611`  |
| 1832   | Layout 1             | `c7a4776c4611`  |
| 1826   | Layout 1             | `c7a4776c4611`  |
| 1822   | Layout 1             | `c7a4776c4611`  |
| 1818   | Layout 1             | `c7a4776c4611`  |
| 1804   | Layout 1             | `c7a4776c4611`  |
| 1794   | Layout 1             | `c7a4776c4611`  |
| 1790   | Layout 1             | `c7a4776c4611`  |
| 1784   | Layout 1             | `c7a4776c4611`  |
| 1774   | Layout 1             | `c7a4776c4611`  |
| 1771   | Layout 1             | `c7a4776c4611`  |
| 1762   | Layout 1             | `c7a4776c4611`  |
| 1759   | Layout 1             | `c7a4776c4611`  |
| 1754   | Layout 1             | `c7a4776c4611`  |
| 1749   | Layout 1             | `c7a4776c4611`  |
| 1743   | Layout 1             | `c7a4776c4611`  |
| 1737   | Layout 1             | `c7a4776c4611`  |
| 1731   | Layout 1             | `c7a4776c4611`  |
| 1725   | Layout 1             | `c7a4776c4611`  |
| 1717   | Layout 1             | `c7a4776c4611`  |
| 1710   | Layout 1             | `c7a4776c4611`  |
| 1704   | Layout 1             | `c7a4776c4611`  |
| 1698   | Layout 1             | `c7a4776c4611`  |
| 1690   | Layout 1             | `c7a4776c4611`  |
| 1685   | Layout 1             | `c7a4776c4611`  |
| 1680   | Layout 1             | `c7a4776c4611`  |
| 1674   | Layout 1             | `c7a4776c4611`  |
| 1668   | Layout 1             | `c7a4776c4611`  |
| 1659   | Layout 1             | `c7a4776c4611`  |
| 1649   | Layout 1             | `c7a4776c4611`  |
| 1642   | Layout 1             | `c7a4776c4611`  |
| 1636   | Layout 1             | `c7a4776c4611`  |
| 1628   | Layout 1             | `c7a4776c4611`  |
| 1622   | Layout 1             | `c7a4776c4611`  |
| 1614   | Layout 1             | `c7a4776c4611`  |
| 1608   | Layout 1             | `c7a4776c4611`  |
| 1602   | Layout 1             | `c7a4776c4611`  |
| 1598   | Layout 1             | `c7a4776c4611`  |
| 1594   | Layout 1             | `c7a4776c4611`  |
| 1590   | Layout 1             | `c7a4776c4611`  |
| 1587   | Layout 1             | `c7a4776c4611`  |
| 1584   | Layout 1             | `c7a4776c4611`  |
| 1579   | Layout 1             | `c7a4776c4611`  |
| 1572   | Layout 1             | `c7a4776c4611`  |
| 1565   | Layout 1             | `c7a4776c4611`  |
| 1559   | Layout 1             | `c7a4776c4611`  |
| 1554   | Layout 1             | `c7a4776c4611`  |
| 1547   | Layout 1             | `c7a4776c4611`  |
| 1537   | Layout 1             | `c7a4776c4611`  |
| 1529   | Layout 1             | `c7a4776c4611`  |
| 1524   | Layout 1             | `c7a4776c4611`  |
| 1519   | Layout 1             | `c7a4776c4611`  |
| 1509   | Layout 1             | `c7a4776c4611`  |
| 1506   | Layout 1             | `c7a4776c4611`  |
| 1504   | Layout 1             | `c7a4776c4611`  |
| 1500   | Layout 1             | `c7a4776c4611`  |
| 1493   | Layout 1             | `c7a4776c4611`  |
| 1489   | Layout 1             | `c7a4776c4611`  |
| 1485   | Layout 1             | `c7a4776c4611`  |
| 1481   | Layout 1             | `c7a4776c4611`  |
| 1474   | Layout 1             | `c7a4776c4611`  |
| 1466   | Layout 1             | `c7a4776c4611`  |
| 1462   | Layout 1             | `c7a4776c4611`  |
| 1459   | Layout 1             | `c7a4776c4611`  |
| 1453   | Layout 1             | `c7a4776c4611`  |
| 1450   | Layout 1             | `c7a4776c4611`  |
| 1445   | Layout 1             | `c7a4776c4611`  |
| 1439   | Layout 1             | `c7a4776c4611`  |
| 1433   | Layout 1             | `c7a4776c4611`  |
| 1430   | Layout 1             | `c7a4776c4611`  |
| 1426   | Layout 1             | `c7a4776c4611`  |
| 1421   | Layout 1             | `c7a4776c4611`  |
| 1417   | Layout 1             | `c7a4776c4611`  |
| 1416   | Layout 1             | `c7a4776c4611`  |
| 1409   | Layout 1             | `c7a4776c4611`  |
| 1405   | Layout 1             | `c7a4776c4611`  |
| 1401   | Layout 1             | `c7a4776c4611`  |
| 1396   | Layout 1             | `c7a4776c4611`  |
| 1391   | Layout 1             | `c7a4776c4611`  |
| 1390   | Layout 1             | `c7a4776c4611`  |
| 1386   | Layout 1             | `c7a4776c4611`  |
| 1381   | Layout 1             | `c7a4776c4611`  |
| 1379   | Layout 1             | `c7a4776c4611`  |
| 1372   | Layout 1             | `c7a4776c4611`  |
| 1366   | Layout 1             | `c7a4776c4611`  |
| 1364   | Layout 1             | `c7a4776c4611`  |
| 1363   | Layout 1             | `c7a4776c4611`  |
| 1360   | Layout 1             | `c7a4776c4611`  |
| 1358   | Layout 1             | `c7a4776c4611`  |
| 1355   | Layout 1             | `c7a4776c4611`  |
| 1351   | Layout 1             | `c7a4776c4611`  |
| 1348   | Layout 1             | `c7a4776c4611`  |
| 1346   | Layout 1             | `c7a4776c4611`  |
| 1341   | No documented layout | `c7a4776c4611`  |
| 1340   | No documented layout | `c7a4776c4611`  |
| 1338   | No documented layout | `c7a4776c4611`  |
| 1335   | No documented layout | `c7a4776c4611`  |
| 1333   | No documented layout | `c7a4776c4611`  |
| 1329   | No documented layout | `c7a4776c4611`  |
| 1327   | No documented layout | `c7a4776c4611`  |
| 1324   | No documented layout | `c7a4776c4611`  |
| 1321   | No documented layout | `c7a4776c4611`  |
| 1319   | No documented layout | `c7a4776c4611`  |
| 1318   | No documented layout | `c7a4776c4611`  |
| 1316   | No documented layout | `c7a4776c4611`  |
| 1313   | No documented layout | `c7a4776c4611`  |
| 1311   | No documented layout | `c7a4776c4611`  |
| 1309   | No documented layout | `c7a4776c4611`  |
| 1304   | No documented layout | `c7a4776c4611`  |
| 1292   | No documented layout | `c7a4776c4611`  |
| 1286   | No documented layout | `c7a4776c4611`  |
| 1280   | No documented layout | `c7a4776c4611`  |
| 1276   | No file              | `c7a4776c4611`  |
| 1267   | No file              | `c7a4776c4611`  |
| 1261   | No file              | `c7a4776c4611`  |
| 1256   | No file              | `c7a4776c4611`  |
| 1250   | No file              | `c7a4776c4611`  |
| 1246   | No file              | `c7a4776c4611`  |
| 1239   | No file              | `c7a4776c4611`  |
| 1230   | No file              | `c7a4776c4611`  |
| 1226   | No file              | `c7a4776c4611`  |
| 1220   | No file              | `c7a4776c4611`  |
| 1217   | No file              | `c7a4776c4611`  |
| 1211   | No file              | `c7a4776c4611`  |
| 1210   | No file              | `c7a4776c4611`  |
| 1208   | No file              | `c7a4776c4611`  |
| 1203   | No file              | `c7a4776c4611`  |
| 1197   | No file              | `c7a4776c4611`  |
| 1194   | No file              | `c7a4776c4611`  |
| 1192   | No file              | `c7a4776c4611`  |
| 1187   | No file              | `c7a4776c4611`  |
| 1183   | No file              | `c7a4776c4611`  |
| 1177   | No file              | `c7a4776c4611`  |
| 1173   | No file              | `c7a4776c4611`  |
| 1167   | No file              | `c7a4776c4611`  |
| 1164   | No file              | `c7a4776c4611`  |
| 1156   | No file              | `c7a4776c4611`  |
| 1149   | No file              | `c7a4776c4611`  |
| 1144   | No file              | `c7a4776c4611`  |
| 1137   | No file              | `c7a4776c4611`  |
| 1132   | No file              | `c7a4776c4611`  |
| 1127   | No file              | `c7a4776c4611`  |
| 1122   | No file              | `c7a4776c4611`  |
| 1118   | No file              | `c7a4776c4611`  |
| 1114   | No file              | `c7a4776c4611`  |
| 1109   | No file              | `c7a4776c4611`  |
| 1102   | No file              | `c7a4776c4611`  |
| 1096   | No file              | `c7a4776c4611`  |
| 1088   | No file              | `c7a4776c4611`  |
| 1081   | No file              | `c7a4776c4611`  |
| 1076   | No file              | `c7a4776c4611`  |
| 1069   | No file              | `c7a4776c4611`  |
| 1064   | No file              | `c7a4776c4611`  |
| 1058   | No file              | `c7a4776c4611`  |
| 1051   | No file              | `c7a4776c4611`  |
| 1044   | No file              | `c7a4776c4611`  |
| 1036   | No file              | `c7a4776c4611`  |
| 1026   | No file              | `c7a4776c4611`  |
| 1016   | No file              | `c7a4776c4611`  |
| 1009   | No file              | `c7a4776c4611`  |
| 1005   | No file              | `c7a4776c4611`  |
| 1000   | No file              | `c7a4776c4611`  |
| 998    | No file              | `c7a4776c4611`  |
| 990    | No file              | `c7a4776c4611`  |
| 979    | No file              | `c7a4776c4611`  |
| 972    | No file              | `c7a4776c4611`  |
| 963    | No file              | `c7a4776c4611`  |
| 955    | No file              | `c7a4776c4611`  |
| 946    | No file              | `c7a4776c4611`  |
| 938    | No file              | `c7a4776c4611`  |
| 927    | No file              | `c7a4776c4611`  |
| 911    | No file              | `c7a4776c4611`  |
| 904    | No file              | `c7a4776c4611`  |
| 899    | No file              | `c7a4776c4611`  |
| 894    | No file              | `c7a4776c4611`  |
| 885    | No file              | `c7a4776c4611`  |
| 879    | No file              | `c7a4776c4611`  |
| 872    | No file              | `c7a4776c4611`  |
| 864    | No file              | `c7a4776c4611`  |
| 855    | No file              | `c7a4776c4611`  |
| 853    | No file              | `c7a4776c4611`  |
| 845    | No file              | `c7a4776c4611`  |
| 837    | No file              | `c7a4776c4611`  |
| 829    | No file              | `c7a4776c4611`  |
| 822    | No file              | `c7a4776c4611`  |
| 814    | No file              | `c7a4776c4611`  |
| 805    | No file              | `c7a4776c4611`  |
| 794    | No file              | `c7a4776c4611`  |
| 787    | No file              | `c7a4776c4611`  |
| 780    | No file              | `c7a4776c4611`  |
| 771    | No file              | `c7a4776c4611`  |
| 760    | No file              | `c7a4776c4611`  |
| 748    | No file              | `c7a4776c4611`  |
| 741    | No file              | `c7a4776c4611`  |
| 736    | No file              | `c7a4776c4611`  |
| 731    | No file              | `c7a4776c4611`  |
| 723    | No file              | `c7a4776c4611`  |
| 711    | No file              | `c7a4776c4611`  |
| 707    | No file              | `c7a4776c4611`  |
| 697    | No file              | `c7a4776c4611`  |
| 689    | No file              | `c7a4776c4611`  |
| 683    | No file              | `c7a4776c4611`  |
| 678    | No file              | `c7a4776c4611`  |
| 670    | No file              | `c7a4776c4611`  |
| 661    | No file              | `c7a4776c4611`  |
| 656    | No file              | `c7a4776c4611`  |
| 652    | No file              | `c7a4776c4611`  |
| 643    | No file              | `c7a4776c4611`  |
| 637    | No file              | `c7a4776c4611`  |
| 630    | No file              | `c7a4776c4611`  |
| 627    | No file              | `c7a4776c4611`  |
| 621    | No file              | `c7a4776c4611`  |
| 617    | No file              | `c7a4776c4611`  |
| 615    | No file              | `c7a4776c4611`  |
| 606    | No file              | `c7a4776c4611`  |
| 599    | No file              | `c7a4776c4611`  |
| 592    | No file              | `c7a4776c4611`  |
| 586    | No file              | `c7a4776c4611`  |
| 577    | No file              | `c7a4776c4611`  |
| 569    | No file              | `c7a4776c4611`  |
| 561    | No file              | `c7a4776c4611`  |
| 554    | No file              | `c7a4776c4611`  |
| 542    | No file              | `c7a4776c4611`  |
| 532    | No file              | `c7a4776c4611`  |
| 531    | No file              | `c7a4776c4611`  |
| 526    | No file              | `c7a4776c4611`  |
| 521    | No file              | `c7a4776c4611`  |
| 517    | No file              | `c7a4776c4611`  |
| 510    | No file              | `c7a4776c4611`  |
| 508    | No file              | `c7a4776c4611`  |
| 504    | No file              | `c7a4776c4611`  |
| 497    | No file              | `c7a4776c4611`  |
| 491    | No file              | `c7a4776c4611`  |
| 485    | No file              | `c7a4776c4611`  |
| 478    | No file              | `c7a4776c4611`  |
| 472    | No file              | `c7a4776c4611`  |
| 466    | No file              | `c7a4776c4611`  |
| 457    | No file              | `c7a4776c4611`  |
| 452    | No file              | `c7a4776c4611`  |
| 449    | No file              | `c7a4776c4611`  |
| 435    | No file              | `c7a4776c4611`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                          |
| ---------------------------- | -------- | ----------------------------------------------------------------------------- |
| `innstaticstatusoffset.dbss` | Optional | `inn_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `houseinfo.bss`              | Optional | The node house rows, for the House link and the Town column                    |
| `guildhouseinfo.dbss`        | Optional | The guild house rows, for the House link and the Town column                   |
| `languagedata_en.loc`        | Optional | House names (type 6) and town names (type 17)                                  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                  |
| ------- | ---------- | ----- | -------------------------------------- |
| `+0x00` | u32        | count | Number of inns; `1` on clients 1784 and 3482 |
| `+0x04` | Row[count] | rows  | See Row                                |

On client 3482 the file is 4 + 2 + 4 + 865 x 2 = 1,740 bytes.

### Row (variable: 6 bytes + room keys)

| Offset  | Type            | Field      | Notes                                                                    |
| ------- | --------------- | ---------- | ------------------------------------------------------------------------ |
| `+0x00` | u16             | inn_key    | Row key; `1`                                                              |
| `+0x02` | u32             | room_count | Number of `room_keys`                                                     |
| `+0x06` | u16[room_count] | room_keys  | House characters, `characterstatic.dbss` keys; each key once             |

### `innstaticstatusoffset.dbss`

Bare offset table into `innstaticstatus.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `innstaticstatus.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                          |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u16  | inn_key     | Key of the row it points at                              |
| `+0x02` | u32  | data_offset | Row start + 2, at `room_count`                           |
| `+0x06` | u32  | data_size   | The row less its key: `4 + 2 * room_count` (1,734 on client 3482) |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`.

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 is named
after the file. The 2016 `gc::InnStaticStatus` holds one member,
`_innRoomList`, a list of `CharacterStaticStatus` pointers, and
`gc::InnStaticStatusManager` keys the inns by a u16; so the list is
`room_keys` and the key `inn_key`. Every key of the list resolves to a
house name (LOC type 6).

## Notes

- On client 3482 the 865 rooms are the 823 node houses of
  [`houseinfo.bss`](../bss/houseinfo_bss.md), the 23 guild houses of
  [`guildhouseinfo.dbss`](guildhouseinfo_dbss.md), Grána (`3520`) and
  O'draxxia (`3806`) Guild Houses and the 17 villas `3371` to `3387`
  (Kunid's Villa to Oberin's Villa).
- The list opens with `3121` (Valencia 15-1, 1F) and the Calpheon slum
  houses `2410`, `2415`, `2420`. [`householdlist.bss`](../bss/householdlist_bss.md)
  holds the same keys in another order.
- The house Lua asks `isInnRoom()` of a house's object static status
  (`panel_housing.luac`, `panel_window_installationmode_house_renew.luac`
  and 12 more), next to `isFixedHouse()` and `isMansionLand()`. The server
  dump of client 1784 has the transactions `TrRentInnRoomReq`
  and `TrUpdateExpiredInnRoomReq`. The view shows one row per room, with
  a link to the room's `houseinfo.bss` or `guildhouseinfo.dbss` row.

## Open Questions

### What Makes a House an Inn Room

`isInnRoom()` reads as a flag that sets a house apart, yet the one inn
lists every house character. Whether `isInnRoom()` reads this list, and
what a rentable inn room is in game, is open.
