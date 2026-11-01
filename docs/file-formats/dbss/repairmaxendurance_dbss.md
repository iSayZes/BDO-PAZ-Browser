# `repairmaxendurance.dbss` Format

## Purpose

The materials that restore an item's max durability: one row per item that
can be repaired this way, with a counted list of materials and the max
durability each one restores. Every row starts with the item itself (`10`)
and ends with Memory Fragment (`44195`, `1`). The Max Durability Recovery
window (`panel_window_endurance_recovery_all`) reads it through
`ToClient_getRepairMaxEnduranceCount`. Companion
`repairmaxenduranceoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                            | Bytes   | Records                   | Row bytes |
| ------ | -------------- | ------------------------------- | ------- | ------------------------- | --------- |
| 1      | 1346 and later | `repairmaxendurance.dbss`       | 108,380 | 5,450 Material, 1,458 Row | 14        |
| 1      | 1346 and later | `repairmaxenduranceoffset.dbss` | 17,500  | 1,458 Offset Row          | 12        |

| Layout | File                            | Known              | Unknown    |
| ------ | ------------------------------- | ------------------ | ---------- |
| 1      | `repairmaxendurance.dbss`       | 108,380 B (100.0%) | 0 B (0.0%) |
| 1      | `repairmaxenduranceoffset.dbss` | 17,500 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `1f6976d6f901`  |
| 3482   | Layout 1             | `1f6976d6f901`  |
| 3474   | Layout 1             | `1f6976d6f901`  |
| 3473   | Layout 1             | `1f6976d6f901`  |
| 3464   | Layout 1             | `1f6976d6f901`  |
| 3458   | Layout 1             | `1f6976d6f901`  |
| 3454   | Layout 1             | `1f6976d6f901`  |
| 3444   | Layout 1             | `1f6976d6f901`  |
| 3435   | Layout 1             | `1f6976d6f901`  |
| 3426   | Layout 1             | `1f6976d6f901`  |
| 3418   | Layout 1             | `1f6976d6f901`  |
| 3412   | Layout 1             | `1f6976d6f901`  |
| 3402   | Layout 1             | `1f6976d6f901`  |
| 3396   | Layout 1             | `1f6976d6f901`  |
| 3387   | Layout 1             | `1f6976d6f901`  |
| 3381   | Layout 1             | `1f6976d6f901`  |
| 3373   | Layout 1             | `1f6976d6f901`  |
| 3364   | Layout 1             | `1f6976d6f901`  |
| 3356   | Layout 1             | `1f6976d6f901`  |
| 3349   | Layout 1             | `1f6976d6f901`  |
| 3342   | Layout 1             | `1f6976d6f901`  |
| 3335   | Layout 1             | `1f6976d6f901`  |
| 3326   | Layout 1             | `1f6976d6f901`  |
| 3321   | Layout 1             | `1f6976d6f901`  |
| 3314   | Layout 1             | `1f6976d6f901`  |
| 3303   | Layout 1             | `1f6976d6f901`  |
| 3302   | Layout 1             | `1f6976d6f901`  |
| 3293   | Layout 1             | `1f6976d6f901`  |
| 3283   | Layout 1             | `1f6976d6f901`  |
| 3275   | Layout 1             | `1f6976d6f901`  |
| 3267   | Layout 1             | `1f6976d6f901`  |
| 3258   | Layout 1             | `1f6976d6f901`  |
| 3251   | Layout 1             | `1f6976d6f901`  |
| 3242   | Layout 1             | `1f6976d6f901`  |
| 3235   | Layout 1             | `1f6976d6f901`  |
| 3229   | Layout 1             | `1f6976d6f901`  |
| 3212   | Layout 1             | `1f6976d6f901`  |
| 3203   | Layout 1             | `1f6976d6f901`  |
| 3193   | Layout 1             | `1f6976d6f901`  |
| 3186   | Layout 1             | `1f6976d6f901`  |
| 3177   | Layout 1             | `1f6976d6f901`  |
| 3169   | Layout 1             | `1f6976d6f901`  |
| 3158   | Layout 1             | `1f6976d6f901`  |
| 3151   | Layout 1             | `1f6976d6f901`  |
| 3144   | Layout 1             | `1f6976d6f901`  |
| 3133   | Layout 1             | `1f6976d6f901`  |
| 3125   | Layout 1             | `1f6976d6f901`  |
| 3118   | Layout 1             | `1f6976d6f901`  |
| 3111   | Layout 1             | `1f6976d6f901`  |
| 3103   | Layout 1             | `1f6976d6f901`  |
| 3095   | Layout 1             | `1f6976d6f901`  |
| 3086   | Layout 1             | `1f6976d6f901`  |
| 3072   | Layout 1             | `1f6976d6f901`  |
| 3062   | Layout 1             | `1f6976d6f901`  |
| 3052   | Layout 1             | `1f6976d6f901`  |
| 3045   | Layout 1             | `1f6976d6f901`  |
| 3037   | Layout 1             | `1f6976d6f901`  |
| 3030   | Layout 1             | `1f6976d6f901`  |
| 3021   | Layout 1             | `1f6976d6f901`  |
| 3012   | Layout 1             | `1f6976d6f901`  |
| 3002   | Layout 1             | `1f6976d6f901`  |
| 2995   | Layout 1             | `1f6976d6f901`  |
| 2987   | Layout 1             | `1f6976d6f901`  |
| 2978   | Layout 1             | `1f6976d6f901`  |
| 2970   | Layout 1             | `1f6976d6f901`  |
| 2959   | Layout 1             | `1f6976d6f901`  |
| 2951   | Layout 1             | `1f6976d6f901`  |
| 2942   | Layout 1             | `1f6976d6f901`  |
| 2935   | Layout 1             | `1f6976d6f901`  |
| 2932   | Layout 1             | `1f6976d6f901`  |
| 2923   | Layout 1             | `1f6976d6f901`  |
| 2919   | Layout 1             | `1f6976d6f901`  |
| 2907   | Layout 1             | `1f6976d6f901`  |
| 2900   | Layout 1             | `1f6976d6f901`  |
| 2891   | Layout 1             | `1f6976d6f901`  |
| 2882   | Layout 1             | `1f6976d6f901`  |
| 2872   | Layout 1             | `1f6976d6f901`  |
| 2863   | Layout 1             | `1f6976d6f901`  |
| 2855   | Layout 1             | `1f6976d6f901`  |
| 2849   | Layout 1             | `1f6976d6f901`  |
| 2844   | Layout 1             | `1f6976d6f901`  |
| 2834   | Layout 1             | `1f6976d6f901`  |
| 2825   | Layout 1             | `1f6976d6f901`  |
| 2819   | Layout 1             | `1f6976d6f901`  |
| 2811   | Layout 1             | `1f6976d6f901`  |
| 2803   | Layout 1             | `1f6976d6f901`  |
| 2794   | Layout 1             | `1f6976d6f901`  |
| 2783   | Layout 1             | `1f6976d6f901`  |
| 2774   | Layout 1             | `1f6976d6f901`  |
| 2765   | Layout 1             | `1f6976d6f901`  |
| 2756   | Layout 1             | `1f6976d6f901`  |
| 2750   | Layout 1             | `1f6976d6f901`  |
| 2743   | Layout 1             | `1f6976d6f901`  |
| 2736   | Layout 1             | `1f6976d6f901`  |
| 2726   | Layout 1             | `1f6976d6f901`  |
| 2717   | Layout 1             | `1f6976d6f901`  |
| 2709   | Layout 1             | `1f6976d6f901`  |
| 2703   | Layout 1             | `1f6976d6f901`  |
| 2695   | Layout 1             | `1f6976d6f901`  |
| 2684   | Layout 1             | `1f6976d6f901`  |
| 2672   | Layout 1             | `1f6976d6f901`  |
| 2665   | Layout 1             | `1f6976d6f901`  |
| 2657   | Layout 1             | `1f6976d6f901`  |
| 2649   | Layout 1             | `1f6976d6f901`  |
| 2644   | Layout 1             | `1f6976d6f901`  |
| 2637   | Layout 1             | `1f6976d6f901`  |
| 2629   | Layout 1             | `1f6976d6f901`  |
| 2619   | Layout 1             | `1f6976d6f901`  |
| 2612   | Layout 1             | `1f6976d6f901`  |
| 2606   | Layout 1             | `1f6976d6f901`  |
| 2602   | Layout 1             | `1f6976d6f901`  |
| 2601   | Layout 1             | `1f6976d6f901`  |
| 2592   | Layout 1             | `1f6976d6f901`  |
| 2583   | Layout 1             | `1f6976d6f901`  |
| 2575   | Layout 1             | `1f6976d6f901`  |
| 2567   | Layout 1             | `1f6976d6f901`  |
| 2560   | Layout 1             | `1f6976d6f901`  |
| 2553   | Layout 1             | `1f6976d6f901`  |
| 2545   | Layout 1             | `1f6976d6f901`  |
| 2538   | Layout 1             | `1f6976d6f901`  |
| 2529   | Layout 1             | `1f6976d6f901`  |
| 2519   | Layout 1             | `1f6976d6f901`  |
| 2513   | Layout 1             | `1f6976d6f901`  |
| 2510   | Layout 1             | `1f6976d6f901`  |
| 2507   | Layout 1             | `1f6976d6f901`  |
| 2503   | Layout 1             | `1f6976d6f901`  |
| 2498   | Layout 1             | `1f6976d6f901`  |
| 2492   | Layout 1             | `1f6976d6f901`  |
| 2487   | Layout 1             | `1f6976d6f901`  |
| 2480   | Layout 1             | `1f6976d6f901`  |
| 2474   | Layout 1             | `1f6976d6f901`  |
| 2468   | Layout 1             | `1f6976d6f901`  |
| 2460   | Layout 1             | `1f6976d6f901`  |
| 2453   | Layout 1             | `1f6976d6f901`  |
| 2444   | Layout 1             | `1f6976d6f901`  |
| 2438   | Layout 1             | `1f6976d6f901`  |
| 2434   | Layout 1             | `1f6976d6f901`  |
| 2429   | Layout 1             | `1f6976d6f901`  |
| 2421   | Layout 1             | `1f6976d6f901`  |
| 2414   | Layout 1             | `1f6976d6f901`  |
| 2407   | Layout 1             | `1f6976d6f901`  |
| 2401   | Layout 1             | `1f6976d6f901`  |
| 2397   | Layout 1             | `1f6976d6f901`  |
| 2393   | Layout 1             | `1f6976d6f901`  |
| 2384   | Layout 1             | `1f6976d6f901`  |
| 2378   | Layout 1             | `1f6976d6f901`  |
| 2372   | Layout 1             | `1f6976d6f901`  |
| 2358   | Layout 1             | `1f6976d6f901`  |
| 2352   | Layout 1             | `1f6976d6f901`  |
| 2347   | Layout 1             | `1f6976d6f901`  |
| 2343   | Layout 1             | `1f6976d6f901`  |
| 2335   | Layout 1             | `1f6976d6f901`  |
| 2327   | Layout 1             | `1f6976d6f901`  |
| 2324   | Layout 1             | `1f6976d6f901`  |
| 2319   | Layout 1             | `1f6976d6f901`  |
| 2313   | Layout 1             | `1f6976d6f901`  |
| 2308   | Layout 1             | `1f6976d6f901`  |
| 2302   | Layout 1             | `1f6976d6f901`  |
| 2295   | Layout 1             | `1f6976d6f901`  |
| 2290   | Layout 1             | `1f6976d6f901`  |
| 2284   | Layout 1             | `1f6976d6f901`  |
| 2276   | Layout 1             | `1f6976d6f901`  |
| 2269   | Layout 1             | `1f6976d6f901`  |
| 2259   | Layout 1             | `1f6976d6f901`  |
| 2250   | Layout 1             | `1f6976d6f901`  |
| 2243   | Layout 1             | `1f6976d6f901`  |
| 2235   | Layout 1             | `1f6976d6f901`  |
| 2229   | Layout 1             | `1f6976d6f901`  |
| 2224   | Layout 1             | `1f6976d6f901`  |
| 2218   | Layout 1             | `1f6976d6f901`  |
| 2215   | Layout 1             | `1f6976d6f901`  |
| 2207   | Layout 1             | `1f6976d6f901`  |
| 2203   | Layout 1             | `1f6976d6f901`  |
| 2196   | Layout 1             | `1f6976d6f901`  |
| 2192   | Layout 1             | `1f6976d6f901`  |
| 2189   | Layout 1             | `1f6976d6f901`  |
| 2183   | Layout 1             | `1f6976d6f901`  |
| 2179   | Layout 1             | `1f6976d6f901`  |
| 2171   | Layout 1             | `1f6976d6f901`  |
| 2163   | Layout 1             | `1f6976d6f901`  |
| 2156   | Layout 1             | `1f6976d6f901`  |
| 2151   | Layout 1             | `1f6976d6f901`  |
| 2147   | Layout 1             | `1f6976d6f901`  |
| 2142   | Layout 1             | `1f6976d6f901`  |
| 2138   | Layout 1             | `1f6976d6f901`  |
| 2134   | Layout 1             | `1f6976d6f901`  |
| 2130   | Layout 1             | `1f6976d6f901`  |
| 2122   | Layout 1             | `1f6976d6f901`  |
| 2107   | Layout 1             | `1f6976d6f901`  |
| 2098   | Layout 1             | `1f6976d6f901`  |
| 2089   | Layout 1             | `1f6976d6f901`  |
| 2081   | Layout 1             | `1f6976d6f901`  |
| 2073   | Layout 1             | `1f6976d6f901`  |
| 2067   | Layout 1             | `1f6976d6f901`  |
| 2063   | Layout 1             | `1f6976d6f901`  |
| 2059   | Layout 1             | `1f6976d6f901`  |
| 2052   | Layout 1             | `1f6976d6f901`  |
| 2044   | Layout 1             | `1f6976d6f901`  |
| 2039   | Layout 1             | `1f6976d6f901`  |
| 2032   | Layout 1             | `1f6976d6f901`  |
| 2025   | Layout 1             | `1f6976d6f901`  |
| 2011   | Layout 1             | `1f6976d6f901`  |
| 2005   | Layout 1             | `1f6976d6f901`  |
| 2000   | Layout 1             | `1f6976d6f901`  |
| 1996   | Layout 1             | `1f6976d6f901`  |
| 1991   | Layout 1             | `1f6976d6f901`  |
| 1985   | Layout 1             | `1f6976d6f901`  |
| 1980   | Layout 1             | `1f6976d6f901`  |
| 1969   | Layout 1             | `1f6976d6f901`  |
| 1964   | Layout 1             | `1f6976d6f901`  |
| 1958   | Layout 1             | `1f6976d6f901`  |
| 1950   | Layout 1             | `1f6976d6f901`  |
| 1945   | Layout 1             | `1f6976d6f901`  |
| 1937   | Layout 1             | `1f6976d6f901`  |
| 1933   | Layout 1             | `1f6976d6f901`  |
| 1927   | Layout 1             | `1f6976d6f901`  |
| 1921   | Layout 1             | `1f6976d6f901`  |
| 1914   | Layout 1             | `1f6976d6f901`  |
| 1908   | Layout 1             | `1f6976d6f901`  |
| 1897   | Layout 1             | `1f6976d6f901`  |
| 1892   | Layout 1             | `1f6976d6f901`  |
| 1886   | Layout 1             | `1f6976d6f901`  |
| 1881   | Layout 1             | `1f6976d6f901`  |
| 1871   | Layout 1             | `1f6976d6f901`  |
| 1866   | Layout 1             | `1f6976d6f901`  |
| 1862   | Layout 1             | `1f6976d6f901`  |
| 1854   | Layout 1             | `1f6976d6f901`  |
| 1846   | Layout 1             | `1f6976d6f901`  |
| 1838   | Layout 1             | `1f6976d6f901`  |
| 1832   | Layout 1             | `1f6976d6f901`  |
| 1826   | Layout 1             | `1f6976d6f901`  |
| 1822   | Layout 1             | `1f6976d6f901`  |
| 1818   | Layout 1             | `1f6976d6f901`  |
| 1804   | Layout 1             | `1f6976d6f901`  |
| 1794   | Layout 1             | `1f6976d6f901`  |
| 1790   | Layout 1             | `1f6976d6f901`  |
| 1784   | Layout 1             | `1f6976d6f901`  |
| 1774   | Layout 1             | `1f6976d6f901`  |
| 1771   | Layout 1             | `1f6976d6f901`  |
| 1762   | Layout 1             | `1f6976d6f901`  |
| 1759   | Layout 1             | `1f6976d6f901`  |
| 1754   | Layout 1             | `1f6976d6f901`  |
| 1749   | Layout 1             | `1f6976d6f901`  |
| 1743   | Layout 1             | `1f6976d6f901`  |
| 1737   | Layout 1             | `1f6976d6f901`  |
| 1731   | Layout 1             | `1f6976d6f901`  |
| 1725   | Layout 1             | `1f6976d6f901`  |
| 1717   | Layout 1             | `1f6976d6f901`  |
| 1710   | Layout 1             | `1f6976d6f901`  |
| 1704   | Layout 1             | `1f6976d6f901`  |
| 1698   | Layout 1             | `1f6976d6f901`  |
| 1690   | Layout 1             | `1f6976d6f901`  |
| 1685   | Layout 1             | `1f6976d6f901`  |
| 1680   | Layout 1             | `1f6976d6f901`  |
| 1674   | Layout 1             | `1f6976d6f901`  |
| 1668   | Layout 1             | `1f6976d6f901`  |
| 1659   | Layout 1             | `1f6976d6f901`  |
| 1649   | Layout 1             | `1f6976d6f901`  |
| 1642   | Layout 1             | `1f6976d6f901`  |
| 1636   | Layout 1             | `1f6976d6f901`  |
| 1628   | Layout 1             | `1f6976d6f901`  |
| 1622   | Layout 1             | `1f6976d6f901`  |
| 1614   | Layout 1             | `1f6976d6f901`  |
| 1608   | Layout 1             | `1f6976d6f901`  |
| 1602   | Layout 1             | `1f6976d6f901`  |
| 1598   | Layout 1             | `1f6976d6f901`  |
| 1594   | Layout 1             | `1f6976d6f901`  |
| 1590   | Layout 1             | `1f6976d6f901`  |
| 1587   | Layout 1             | `1f6976d6f901`  |
| 1584   | Layout 1             | `1f6976d6f901`  |
| 1579   | Layout 1             | `1f6976d6f901`  |
| 1572   | Layout 1             | `1f6976d6f901`  |
| 1565   | Layout 1             | `1f6976d6f901`  |
| 1559   | Layout 1             | `1f6976d6f901`  |
| 1554   | Layout 1             | `1f6976d6f901`  |
| 1547   | Layout 1             | `1f6976d6f901`  |
| 1537   | Layout 1             | `1f6976d6f901`  |
| 1529   | Layout 1             | `1f6976d6f901`  |
| 1524   | Layout 1             | `1f6976d6f901`  |
| 1519   | Layout 1             | `1f6976d6f901`  |
| 1509   | Layout 1             | `1f6976d6f901`  |
| 1506   | Layout 1             | `1f6976d6f901`  |
| 1504   | Layout 1             | `1f6976d6f901`  |
| 1500   | Layout 1             | `1f6976d6f901`  |
| 1493   | Layout 1             | `1f6976d6f901`  |
| 1489   | Layout 1             | `1f6976d6f901`  |
| 1485   | Layout 1             | `1f6976d6f901`  |
| 1481   | Layout 1             | `1f6976d6f901`  |
| 1474   | Layout 1             | `1f6976d6f901`  |
| 1466   | Layout 1             | `1f6976d6f901`  |
| 1462   | Layout 1             | `1f6976d6f901`  |
| 1459   | Layout 1             | `1f6976d6f901`  |
| 1453   | Layout 1             | `1f6976d6f901`  |
| 1450   | Layout 1             | `1f6976d6f901`  |
| 1445   | Layout 1             | `1f6976d6f901`  |
| 1439   | Layout 1             | `1f6976d6f901`  |
| 1433   | Layout 1             | `1f6976d6f901`  |
| 1430   | Layout 1             | `1f6976d6f901`  |
| 1426   | Layout 1             | `1f6976d6f901`  |
| 1421   | Layout 1             | `1f6976d6f901`  |
| 1417   | Layout 1             | `1f6976d6f901`  |
| 1416   | Layout 1             | `1f6976d6f901`  |
| 1409   | Layout 1             | `1f6976d6f901`  |
| 1405   | Layout 1             | `1f6976d6f901`  |
| 1401   | Layout 1             | `1f6976d6f901`  |
| 1396   | Layout 1             | `1f6976d6f901`  |
| 1391   | Layout 1             | `1f6976d6f901`  |
| 1390   | Layout 1             | `1f6976d6f901`  |
| 1386   | Layout 1             | `1f6976d6f901`  |
| 1381   | Layout 1             | `1f6976d6f901`  |
| 1379   | Layout 1             | `1f6976d6f901`  |
| 1372   | Layout 1             | `1f6976d6f901`  |
| 1366   | Layout 1             | `1f6976d6f901`  |
| 1364   | Layout 1             | `1f6976d6f901`  |
| 1363   | Layout 1             | `1f6976d6f901`  |
| 1360   | Layout 1             | `1f6976d6f901`  |
| 1358   | Layout 1             | `1f6976d6f901`  |
| 1355   | Layout 1             | `1f6976d6f901`  |
| 1351   | Layout 1             | `1f6976d6f901`  |
| 1348   | Layout 1             | `1f6976d6f901`  |
| 1346   | Layout 1             | `1f6976d6f901`  |
| 1341   | No documented layout | `1f6976d6f901`  |
| 1340   | No documented layout | `1f6976d6f901`  |
| 1338   | No documented layout | `1f6976d6f901`  |
| 1335   | No documented layout | `1f6976d6f901`  |
| 1333   | No documented layout | `1f6976d6f901`  |
| 1329   | No documented layout | `1f6976d6f901`  |
| 1327   | No documented layout | `1f6976d6f901`  |
| 1324   | No documented layout | `1f6976d6f901`  |
| 1321   | No documented layout | `1f6976d6f901`  |
| 1319   | No documented layout | `1f6976d6f901`  |
| 1318   | No documented layout | `1f6976d6f901`  |
| 1316   | No documented layout | `1f6976d6f901`  |
| 1313   | No documented layout | `1f6976d6f901`  |
| 1311   | No documented layout | `1f6976d6f901`  |
| 1309   | No documented layout | `1f6976d6f901`  |
| 1304   | No documented layout | `1f6976d6f901`  |
| 1292   | No documented layout | `1f6976d6f901`  |
| 1286   | No documented layout | `1f6976d6f901`  |
| 1280   | No documented layout | `1f6976d6f901`  |
| 1276   | No file              | `1f6976d6f901`  |
| 1267   | No file              | `1f6976d6f901`  |
| 1261   | No file              | `1f6976d6f901`  |
| 1256   | No file              | `1f6976d6f901`  |
| 1250   | No file              | `1f6976d6f901`  |
| 1246   | No file              | `1f6976d6f901`  |
| 1239   | No file              | `1f6976d6f901`  |
| 1230   | No file              | `1f6976d6f901`  |
| 1226   | No file              | `1f6976d6f901`  |
| 1220   | No file              | `1f6976d6f901`  |
| 1217   | No file              | `1f6976d6f901`  |
| 1211   | No file              | `1f6976d6f901`  |
| 1210   | No file              | `1f6976d6f901`  |
| 1208   | No file              | `1f6976d6f901`  |
| 1203   | No file              | `1f6976d6f901`  |
| 1197   | No file              | `1f6976d6f901`  |
| 1194   | No file              | `1f6976d6f901`  |
| 1192   | No file              | `1f6976d6f901`  |
| 1187   | No file              | `1f6976d6f901`  |
| 1183   | No file              | `1f6976d6f901`  |
| 1177   | No file              | `1f6976d6f901`  |
| 1173   | No file              | `1f6976d6f901`  |
| 1167   | No file              | `1f6976d6f901`  |
| 1164   | No file              | `1f6976d6f901`  |
| 1156   | No file              | `1f6976d6f901`  |
| 1149   | No file              | `1f6976d6f901`  |
| 1144   | No file              | `1f6976d6f901`  |
| 1137   | No file              | `1f6976d6f901`  |
| 1132   | No file              | `1f6976d6f901`  |
| 1127   | No file              | `1f6976d6f901`  |
| 1122   | No file              | `1f6976d6f901`  |
| 1118   | No file              | `1f6976d6f901`  |
| 1114   | No file              | `1f6976d6f901`  |
| 1109   | No file              | `1f6976d6f901`  |
| 1102   | No file              | `1f6976d6f901`  |
| 1096   | No file              | `1f6976d6f901`  |
| 1088   | No file              | `1f6976d6f901`  |
| 1081   | No file              | `1f6976d6f901`  |
| 1076   | No file              | `1f6976d6f901`  |
| 1069   | No file              | `1f6976d6f901`  |
| 1064   | No file              | `1f6976d6f901`  |
| 1058   | No file              | `1f6976d6f901`  |
| 1051   | No file              | `1f6976d6f901`  |
| 1044   | No file              | `1f6976d6f901`  |
| 1036   | No file              | `1f6976d6f901`  |
| 1026   | No file              | `1f6976d6f901`  |
| 1016   | No file              | `1f6976d6f901`  |
| 1009   | No file              | `1f6976d6f901`  |
| 1005   | No file              | `1f6976d6f901`  |
| 1000   | No file              | `1f6976d6f901`  |
| 998    | No file              | `1f6976d6f901`  |
| 990    | No file              | `1f6976d6f901`  |
| 979    | No file              | `1f6976d6f901`  |
| 972    | No file              | `1f6976d6f901`  |
| 963    | No file              | `1f6976d6f901`  |
| 955    | No file              | `1f6976d6f901`  |
| 946    | No file              | `1f6976d6f901`  |
| 938    | No file              | `1f6976d6f901`  |
| 927    | No file              | `1f6976d6f901`  |
| 911    | No file              | `1f6976d6f901`  |
| 904    | No file              | `1f6976d6f901`  |
| 899    | No file              | `1f6976d6f901`  |
| 894    | No file              | `1f6976d6f901`  |
| 885    | No file              | `1f6976d6f901`  |
| 879    | No file              | `1f6976d6f901`  |
| 872    | No file              | `1f6976d6f901`  |
| 864    | No file              | `1f6976d6f901`  |
| 855    | No file              | `1f6976d6f901`  |
| 853    | No file              | `1f6976d6f901`  |
| 845    | No file              | `1f6976d6f901`  |
| 837    | No file              | `1f6976d6f901`  |
| 829    | No file              | `1f6976d6f901`  |
| 822    | No file              | `1f6976d6f901`  |
| 814    | No file              | `1f6976d6f901`  |
| 805    | No file              | `1f6976d6f901`  |
| 794    | No file              | `1f6976d6f901`  |
| 787    | No file              | `1f6976d6f901`  |
| 780    | No file              | `1f6976d6f901`  |
| 771    | No file              | `1f6976d6f901`  |
| 760    | No file              | `1f6976d6f901`  |
| 748    | No file              | `1f6976d6f901`  |
| 741    | No file              | `1f6976d6f901`  |
| 736    | No file              | `1f6976d6f901`  |
| 731    | No file              | `1f6976d6f901`  |
| 723    | No file              | `1f6976d6f901`  |
| 711    | No file              | `1f6976d6f901`  |
| 707    | No file              | `1f6976d6f901`  |
| 697    | No file              | `1f6976d6f901`  |
| 689    | No file              | `1f6976d6f901`  |
| 683    | No file              | `1f6976d6f901`  |
| 678    | No file              | `1f6976d6f901`  |
| 670    | No file              | `1f6976d6f901`  |
| 661    | No file              | `1f6976d6f901`  |
| 656    | No file              | `1f6976d6f901`  |
| 652    | No file              | `1f6976d6f901`  |
| 643    | No file              | `1f6976d6f901`  |
| 637    | No file              | `1f6976d6f901`  |
| 630    | No file              | `1f6976d6f901`  |
| 627    | No file              | `1f6976d6f901`  |
| 621    | No file              | `1f6976d6f901`  |
| 617    | No file              | `1f6976d6f901`  |
| 615    | No file              | `1f6976d6f901`  |
| 606    | No file              | `1f6976d6f901`  |
| 599    | No file              | `1f6976d6f901`  |
| 592    | No file              | `1f6976d6f901`  |
| 586    | No file              | `1f6976d6f901`  |
| 577    | No file              | `1f6976d6f901`  |
| 569    | No file              | `1f6976d6f901`  |
| 561    | No file              | `1f6976d6f901`  |
| 554    | No file              | `1f6976d6f901`  |
| 542    | No file              | `1f6976d6f901`  |
| 532    | No file              | `1f6976d6f901`  |
| 531    | No file              | `1f6976d6f901`  |
| 526    | No file              | `1f6976d6f901`  |
| 521    | No file              | `1f6976d6f901`  |
| 517    | No file              | `1f6976d6f901`  |
| 510    | No file              | `1f6976d6f901`  |
| 508    | No file              | `1f6976d6f901`  |
| 504    | No file              | `1f6976d6f901`  |
| 497    | No file              | `1f6976d6f901`  |
| 491    | No file              | `1f6976d6f901`  |
| 485    | No file              | `1f6976d6f901`  |
| 478    | No file              | `1f6976d6f901`  |
| 472    | No file              | `1f6976d6f901`  |
| 466    | No file              | `1f6976d6f901`  |
| 457    | No file              | `1f6976d6f901`  |
| 452    | No file              | `1f6976d6f901`  |
| 449    | No file              | `1f6976d6f901`  |
| 435    | No file              | `1f6976d6f901`  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                                 |
| ------------------------------- | -------- | -------------------------------------------------------------------- |
| `repairmaxenduranceoffset.dbss` | Optional | `item_key -> (data_offset, data_size)` of every row; the rows carry their own material count and can be walked without it |
| `languagedata_en.loc`           | Optional | Item names (type `0`, `str_id1` = item ID)                           |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `1458` on client 3474        |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 22 bytes + materials)

| Offset  | Type                     | Field                   | Notes                                                                 |
| ------- | ------------------------ | ----------------------- | --------------------------------------------------------------------- |
| `+0x00` | u32                      | item_key                | Item whose max durability the row restores, packed as `enchant_level << 24 \| item_id`; unique per row, the index key |
| `+0x04` | u32                      | item_key_dup            | Equal to `item_key` in every row; the offset file points here         |
| `+0x08` | i64                      | only_need_money         | Silver for a repair with no material; `0` in every row                |
| `+0x10` | i16                      | only_money_repair_count | Max durability that silver-only repair restores; `0` in every row     |
| `+0x12` | u32                      | material_count          | Number of materials; `2` to `12`                                      |
| `+0x16` | Material[material_count] | materials               | See Material                                                          |

The enchant level byte of `item_key` is `0` in every row on clients 1784
and 3474. The rows are not sorted by `item_key`.

### Material (14 bytes)

| Offset  | Type | Field        | Notes                                                              |
| ------- | ---- | ------------ | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_key     | Material item, packed as the row's `item_key`; enchant level `0` in every entry |
| `+0x04` | i16  | repair_count | Max durability one material restores; see Repair Counts            |
| `+0x06` | i64  | need_money   | Silver per use; `0` in every entry                                 |

### `repairmaxenduranceoffset.dbss`

| Offset  | Type              | Field | Notes                                      |
| ------- | ----------------- | ----- | ------------------------------------------ |
| `+0x00` | u32               | count | Equals the `repairmaxendurance.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row       |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                     |
| ------- | ---- | ----------- | --------------------------------------------------------- |
| `+0x00` | u32  | item_key    | Key of the row it points at                               |
| `+0x04` | u32  | data_offset | Row start + 4, at `item_key_dup`                          |
| `+0x08` | u32  | data_size   | The row without its leading `item_key`: `18 + 14 x material_count` |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Repair Counts

`repair_count` values on client 3474, over all 5,450 materials of the 1,458
rows:

| Value | Materials | Items                                                                  |
| ----- | --------- | ---------------------------------------------------------------------- |
| `10`  | 3,749     | The row's own item (first in every row) and other versions of the same gear |
| `5`   | 179       | Refined Black Energy Residue (`9750`, 90 rows), Time-filled Fragment (`721048`, 89 rows) |
| `20`  | 54        | Sandstorm Crystal (`721031`)                                           |
| `1`   | 1,468     | Memory Fragment (`44195`, last in every row), Yona's Fragment (`44350`, 10 rows) |

Material counts per row on client 3474: `3` on 1,212 rows, `8` on 176,
`6` on 22, `4` on 20, `5` on 16, `12` on 8, `2` and `7` on 2 each.

## Field Names

The names follow the 2016 `gc::RepairMaxEnduranceStaticStatus`, keyed by a
`gc::ItemEnchantKey`, with the members `_keyItem` (`ItemEnchantKey`),
`_onlyMoney` (`__int64`), `_repairAmountOnlyMoney` (`short`) and
`_materialList`, a vector of `gc::RepairMaxEnduranceMaterial` (`_itemKey`
as an `ItemEnchantKey`, `_repairAmount` as a `short`, `_needMoney` as an
`__int64`). Their sizes give the 8 + 2 bytes after `item_key_dup` and the
4 + 2 + 8 bytes of a Material. The field names are the columns of the
`RepairMaxEndurance` sheet of a private server's `DataSheets.bexcel` on
client 1784: `BaseItem`, `OnlyNeedMoney`, `OnlyMoneyRepairCount`, then ten
slots of `ItemN`, `RepairCountN` and `NeedMoneyN`.

The sheet lists only the extra materials. A row of the file holds the item
itself with `10`, the sheet's slots in sheet order, then Memory Fragment
with `1`:

| Client | Rows | Shared with the sheet | Rows that match | Misses                                                                    |
| ------ | ---- | --------------------- | --------------- | ------------------------------------------------------------------------- |
| 1784   | 1425 | 1425                  | 1301            | 122 Tuvala gear rows list other Tuvala gear (`10`) where the sheet lists Tuvala Ore (`721051`, `10`); 2 rows (`718600`, `719069`) have no extra material where the sheet lists `721008` with `100` |
| 3474   | 1458 | 1232                  | 1167            | 63 Tuvala gear rows list Time-filled Fragment (`721048`, `5`) where the sheet lists Tuvala Ore (`721051`, `10`); the same 2 rows as on client 1784 |

The sheet has 1,547 rows, 122 of them with no row on client 1784.
`OnlyNeedMoney`, `OnlyMoneyRepairCount` and
every `NeedMoneyN` are `0` in the sheet, as in the file on both clients.

## Notes

- `panel_window_endurance_recovery_all_2.luac` builds the confirmation
  text of a repair: `10` when the material is the item itself, the repaired
  item's `_repairEnduranceCount` (item static status) when the material is
  Memory Fragment (`ItemEnchantKey(44195)` in
  `panel_window_endurance_recovery_all.luac`), and
  `ToClient_getRepairMaxEnduranceCount(repairItemKey, materialItemKey)` for
  any other material. With a cash item the count is multiplied by 5.
  `repair_MaxEndurance()` sends the repair.

## Open Questions

### Whether the Same-Item and Memory Fragment Entries Are Read

Every row holds the item itself with `10` and Memory Fragment with `1`, but
the recovery window Lua hard-codes `10` for the item itself and takes the
Memory Fragment count from the repaired item's `_repairEnduranceCount`. No
client Lua reads the two entries' `repair_count`, so whether the server
uses them, or only checks that the material is allowed, is open.
