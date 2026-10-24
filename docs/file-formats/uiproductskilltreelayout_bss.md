# `uiproductskilltreelayout.bss` Format

## Purpose

A skill tree grid for production skills, 21 columns by 15 rows, with every
cell Blank and no skill placed. The file is the same on clients 1784 and
3482, and no client Lua of 3482 reads it (see Notes).

Same layout as [`uiguildskilltreelayout.bss`](uiguildskilltreelayout_bss.md), read by the same handler: a `PABR` header with the grid's width and height, `width * height` 4-byte cells column by column, an empty string table and the 8-byte trailer.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                           | Bytes | Records  | Row bytes |
| ------ | ------------- | ------- | ------------------------------ | ----- | -------- | --------- |
| 2      | 805 and later | 3483    | `uiproductskilltreelayout.bss` | 1,284 | 315 Cell | 4         |
| 1      | 457 to 794    | 794     | `uiproductskilltreelayout.bss` | 1,268 | 315 Cell | 4         |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 2      | `uiproductskilltreelayout.bss` | 1,284 B (100.0%) | 0 B (0.0%) |
| 1      | `uiproductskilltreelayout.bss` | 1,268 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `3c4ee3ff016a`  |
| 3482   | Layout 2 | `3c4ee3ff016a`  |
| 3474   | Layout 2 | `3c4ee3ff016a`  |
| 3473   | Layout 2 | `3c4ee3ff016a`  |
| 3464   | Layout 2 | `3c4ee3ff016a`  |
| 3458   | Layout 2 | `3c4ee3ff016a`  |
| 3454   | Layout 2 | `3c4ee3ff016a`  |
| 3444   | Layout 2 | `3c4ee3ff016a`  |
| 3435   | Layout 2 | `3c4ee3ff016a`  |
| 3426   | Layout 2 | `3c4ee3ff016a`  |
| 3418   | Layout 2 | `3c4ee3ff016a`  |
| 3412   | Layout 2 | `3c4ee3ff016a`  |
| 3402   | Layout 2 | `3c4ee3ff016a`  |
| 3396   | Layout 2 | `3c4ee3ff016a`  |
| 3387   | Layout 2 | `3c4ee3ff016a`  |
| 3381   | Layout 2 | `3c4ee3ff016a`  |
| 3373   | Layout 2 | `3c4ee3ff016a`  |
| 3364   | Layout 2 | `3c4ee3ff016a`  |
| 3356   | Layout 2 | `3c4ee3ff016a`  |
| 3349   | Layout 2 | `3c4ee3ff016a`  |
| 3342   | Layout 2 | `3c4ee3ff016a`  |
| 3335   | Layout 2 | `3c4ee3ff016a`  |
| 3326   | Layout 2 | `3c4ee3ff016a`  |
| 3321   | Layout 2 | `3c4ee3ff016a`  |
| 3314   | Layout 2 | `3c4ee3ff016a`  |
| 3303   | Layout 2 | `3c4ee3ff016a`  |
| 3302   | Layout 2 | `3c4ee3ff016a`  |
| 3293   | Layout 2 | `3c4ee3ff016a`  |
| 3283   | Layout 2 | `3c4ee3ff016a`  |
| 3275   | Layout 2 | `3c4ee3ff016a`  |
| 3267   | Layout 2 | `3c4ee3ff016a`  |
| 3258   | Layout 2 | `3c4ee3ff016a`  |
| 3251   | Layout 2 | `3c4ee3ff016a`  |
| 3242   | Layout 2 | `3c4ee3ff016a`  |
| 3235   | Layout 2 | `3c4ee3ff016a`  |
| 3229   | Layout 2 | `3c4ee3ff016a`  |
| 3212   | Layout 2 | `3c4ee3ff016a`  |
| 3203   | Layout 2 | `3c4ee3ff016a`  |
| 3193   | Layout 2 | `3c4ee3ff016a`  |
| 3186   | Layout 2 | `3c4ee3ff016a`  |
| 3177   | Layout 2 | `3c4ee3ff016a`  |
| 3169   | Layout 2 | `3c4ee3ff016a`  |
| 3158   | Layout 2 | `3c4ee3ff016a`  |
| 3151   | Layout 2 | `3c4ee3ff016a`  |
| 3144   | Layout 2 | `3c4ee3ff016a`  |
| 3133   | Layout 2 | `3c4ee3ff016a`  |
| 3125   | Layout 2 | `3c4ee3ff016a`  |
| 3118   | Layout 2 | `3c4ee3ff016a`  |
| 3111   | Layout 2 | `3c4ee3ff016a`  |
| 3103   | Layout 2 | `3c4ee3ff016a`  |
| 3095   | Layout 2 | `3c4ee3ff016a`  |
| 3086   | Layout 2 | `3c4ee3ff016a`  |
| 3072   | Layout 2 | `3c4ee3ff016a`  |
| 3062   | Layout 2 | `3c4ee3ff016a`  |
| 3052   | Layout 2 | `3c4ee3ff016a`  |
| 3045   | Layout 2 | `3c4ee3ff016a`  |
| 3037   | Layout 2 | `3c4ee3ff016a`  |
| 3030   | Layout 2 | `3c4ee3ff016a`  |
| 3021   | Layout 2 | `3c4ee3ff016a`  |
| 3012   | Layout 2 | `3c4ee3ff016a`  |
| 3002   | Layout 2 | `3c4ee3ff016a`  |
| 2995   | Layout 2 | `3c4ee3ff016a`  |
| 2987   | Layout 2 | `3c4ee3ff016a`  |
| 2978   | Layout 2 | `3c4ee3ff016a`  |
| 2970   | Layout 2 | `3c4ee3ff016a`  |
| 2959   | Layout 2 | `3c4ee3ff016a`  |
| 2951   | Layout 2 | `3c4ee3ff016a`  |
| 2942   | Layout 2 | `3c4ee3ff016a`  |
| 2935   | Layout 2 | `3c4ee3ff016a`  |
| 2932   | Layout 2 | `3c4ee3ff016a`  |
| 2923   | Layout 2 | `3c4ee3ff016a`  |
| 2919   | Layout 2 | `3c4ee3ff016a`  |
| 2907   | Layout 2 | `3c4ee3ff016a`  |
| 2900   | Layout 2 | `3c4ee3ff016a`  |
| 2891   | Layout 2 | `3c4ee3ff016a`  |
| 2882   | Layout 2 | `3c4ee3ff016a`  |
| 2872   | Layout 2 | `3c4ee3ff016a`  |
| 2863   | Layout 2 | `3c4ee3ff016a`  |
| 2855   | Layout 2 | `3c4ee3ff016a`  |
| 2849   | Layout 2 | `3c4ee3ff016a`  |
| 2844   | Layout 2 | `3c4ee3ff016a`  |
| 2834   | Layout 2 | `3c4ee3ff016a`  |
| 2825   | Layout 2 | `3c4ee3ff016a`  |
| 2819   | Layout 2 | `3c4ee3ff016a`  |
| 2811   | Layout 2 | `3c4ee3ff016a`  |
| 2803   | Layout 2 | `3c4ee3ff016a`  |
| 2794   | Layout 2 | `3c4ee3ff016a`  |
| 2783   | Layout 2 | `3c4ee3ff016a`  |
| 2774   | Layout 2 | `3c4ee3ff016a`  |
| 2765   | Layout 2 | `3c4ee3ff016a`  |
| 2756   | Layout 2 | `3c4ee3ff016a`  |
| 2750   | Layout 2 | `3c4ee3ff016a`  |
| 2743   | Layout 2 | `3c4ee3ff016a`  |
| 2736   | Layout 2 | `3c4ee3ff016a`  |
| 2726   | Layout 2 | `3c4ee3ff016a`  |
| 2717   | Layout 2 | `3c4ee3ff016a`  |
| 2709   | Layout 2 | `3c4ee3ff016a`  |
| 2703   | Layout 2 | `3c4ee3ff016a`  |
| 2695   | Layout 2 | `3c4ee3ff016a`  |
| 2684   | Layout 2 | `3c4ee3ff016a`  |
| 2672   | Layout 2 | `3c4ee3ff016a`  |
| 2665   | Layout 2 | `3c4ee3ff016a`  |
| 2657   | Layout 2 | `3c4ee3ff016a`  |
| 2649   | Layout 2 | `3c4ee3ff016a`  |
| 2644   | Layout 2 | `3c4ee3ff016a`  |
| 2637   | Layout 2 | `3c4ee3ff016a`  |
| 2629   | Layout 2 | `3c4ee3ff016a`  |
| 2619   | Layout 2 | `3c4ee3ff016a`  |
| 2612   | Layout 2 | `3c4ee3ff016a`  |
| 2606   | Layout 2 | `3c4ee3ff016a`  |
| 2602   | Layout 2 | `3c4ee3ff016a`  |
| 2601   | Layout 2 | `3c4ee3ff016a`  |
| 2592   | Layout 2 | `3c4ee3ff016a`  |
| 2583   | Layout 2 | `3c4ee3ff016a`  |
| 2575   | Layout 2 | `3c4ee3ff016a`  |
| 2567   | Layout 2 | `3c4ee3ff016a`  |
| 2560   | Layout 2 | `3c4ee3ff016a`  |
| 2553   | Layout 2 | `3c4ee3ff016a`  |
| 2545   | Layout 2 | `3c4ee3ff016a`  |
| 2538   | Layout 2 | `3c4ee3ff016a`  |
| 2529   | Layout 2 | `3c4ee3ff016a`  |
| 2519   | Layout 2 | `3c4ee3ff016a`  |
| 2513   | Layout 2 | `3c4ee3ff016a`  |
| 2510   | Layout 2 | `3c4ee3ff016a`  |
| 2507   | Layout 2 | `3c4ee3ff016a`  |
| 2503   | Layout 2 | `3c4ee3ff016a`  |
| 2498   | Layout 2 | `3c4ee3ff016a`  |
| 2492   | Layout 2 | `3c4ee3ff016a`  |
| 2487   | Layout 2 | `3c4ee3ff016a`  |
| 2480   | Layout 2 | `3c4ee3ff016a`  |
| 2474   | Layout 2 | `3c4ee3ff016a`  |
| 2468   | Layout 2 | `3c4ee3ff016a`  |
| 2460   | Layout 2 | `3c4ee3ff016a`  |
| 2453   | Layout 2 | `3c4ee3ff016a`  |
| 2444   | Layout 2 | `3c4ee3ff016a`  |
| 2438   | Layout 2 | `3c4ee3ff016a`  |
| 2434   | Layout 2 | `3c4ee3ff016a`  |
| 2429   | Layout 2 | `3c4ee3ff016a`  |
| 2421   | Layout 2 | `3c4ee3ff016a`  |
| 2414   | Layout 2 | `3c4ee3ff016a`  |
| 2407   | Layout 2 | `3c4ee3ff016a`  |
| 2401   | Layout 2 | `3c4ee3ff016a`  |
| 2397   | Layout 2 | `3c4ee3ff016a`  |
| 2393   | Layout 2 | `3c4ee3ff016a`  |
| 2384   | Layout 2 | `3c4ee3ff016a`  |
| 2378   | Layout 2 | `3c4ee3ff016a`  |
| 2372   | Layout 2 | `3c4ee3ff016a`  |
| 2358   | Layout 2 | `3c4ee3ff016a`  |
| 2352   | Layout 2 | `3c4ee3ff016a`  |
| 2347   | Layout 2 | `3c4ee3ff016a`  |
| 2343   | Layout 2 | `3c4ee3ff016a`  |
| 2335   | Layout 2 | `3c4ee3ff016a`  |
| 2327   | Layout 2 | `3c4ee3ff016a`  |
| 2324   | Layout 2 | `3c4ee3ff016a`  |
| 2319   | Layout 2 | `3c4ee3ff016a`  |
| 2313   | Layout 2 | `3c4ee3ff016a`  |
| 2308   | Layout 2 | `3c4ee3ff016a`  |
| 2302   | Layout 2 | `3c4ee3ff016a`  |
| 2295   | Layout 2 | `3c4ee3ff016a`  |
| 2290   | Layout 2 | `3c4ee3ff016a`  |
| 2284   | Layout 2 | `3c4ee3ff016a`  |
| 2276   | Layout 2 | `3c4ee3ff016a`  |
| 2269   | Layout 2 | `3c4ee3ff016a`  |
| 2259   | Layout 2 | `3c4ee3ff016a`  |
| 2250   | Layout 2 | `3c4ee3ff016a`  |
| 2243   | Layout 2 | `3c4ee3ff016a`  |
| 2235   | Layout 2 | `3c4ee3ff016a`  |
| 2229   | Layout 2 | `3c4ee3ff016a`  |
| 2224   | Layout 2 | `3c4ee3ff016a`  |
| 2218   | Layout 2 | `3c4ee3ff016a`  |
| 2215   | Layout 2 | `3c4ee3ff016a`  |
| 2207   | Layout 2 | `3c4ee3ff016a`  |
| 2203   | Layout 2 | `3c4ee3ff016a`  |
| 2196   | Layout 2 | `3c4ee3ff016a`  |
| 2192   | Layout 2 | `3c4ee3ff016a`  |
| 2189   | Layout 2 | `3c4ee3ff016a`  |
| 2183   | Layout 2 | `3c4ee3ff016a`  |
| 2179   | Layout 2 | `3c4ee3ff016a`  |
| 2171   | Layout 2 | `3c4ee3ff016a`  |
| 2163   | Layout 2 | `3c4ee3ff016a`  |
| 2156   | Layout 2 | `3c4ee3ff016a`  |
| 2151   | Layout 2 | `3c4ee3ff016a`  |
| 2147   | Layout 2 | `3c4ee3ff016a`  |
| 2142   | Layout 2 | `3c4ee3ff016a`  |
| 2138   | Layout 2 | `3c4ee3ff016a`  |
| 2134   | Layout 2 | `3c4ee3ff016a`  |
| 2130   | Layout 2 | `3c4ee3ff016a`  |
| 2122   | Layout 2 | `3c4ee3ff016a`  |
| 2107   | Layout 2 | `3c4ee3ff016a`  |
| 2098   | Layout 2 | `3c4ee3ff016a`  |
| 2089   | Layout 2 | `3c4ee3ff016a`  |
| 2081   | Layout 2 | `3c4ee3ff016a`  |
| 2073   | Layout 2 | `3c4ee3ff016a`  |
| 2067   | Layout 2 | `3c4ee3ff016a`  |
| 2063   | Layout 2 | `3c4ee3ff016a`  |
| 2059   | Layout 2 | `3c4ee3ff016a`  |
| 2052   | Layout 2 | `3c4ee3ff016a`  |
| 2044   | Layout 2 | `3c4ee3ff016a`  |
| 2039   | Layout 2 | `3c4ee3ff016a`  |
| 2032   | Layout 2 | `3c4ee3ff016a`  |
| 2025   | Layout 2 | `3c4ee3ff016a`  |
| 2011   | Layout 2 | `3c4ee3ff016a`  |
| 2005   | Layout 2 | `3c4ee3ff016a`  |
| 2000   | Layout 2 | `3c4ee3ff016a`  |
| 1996   | Layout 2 | `3c4ee3ff016a`  |
| 1991   | Layout 2 | `3c4ee3ff016a`  |
| 1985   | Layout 2 | `3c4ee3ff016a`  |
| 1980   | Layout 2 | `3c4ee3ff016a`  |
| 1969   | Layout 2 | `3c4ee3ff016a`  |
| 1964   | Layout 2 | `3c4ee3ff016a`  |
| 1958   | Layout 2 | `3c4ee3ff016a`  |
| 1950   | Layout 2 | `3c4ee3ff016a`  |
| 1945   | Layout 2 | `3c4ee3ff016a`  |
| 1937   | Layout 2 | `3c4ee3ff016a`  |
| 1933   | Layout 2 | `3c4ee3ff016a`  |
| 1927   | Layout 2 | `3c4ee3ff016a`  |
| 1921   | Layout 2 | `3c4ee3ff016a`  |
| 1914   | Layout 2 | `3c4ee3ff016a`  |
| 1908   | Layout 2 | `3c4ee3ff016a`  |
| 1897   | Layout 2 | `3c4ee3ff016a`  |
| 1892   | Layout 2 | `3c4ee3ff016a`  |
| 1886   | Layout 2 | `3c4ee3ff016a`  |
| 1881   | Layout 2 | `3c4ee3ff016a`  |
| 1871   | Layout 2 | `3c4ee3ff016a`  |
| 1866   | Layout 2 | `3c4ee3ff016a`  |
| 1862   | Layout 2 | `3c4ee3ff016a`  |
| 1854   | Layout 2 | `3c4ee3ff016a`  |
| 1846   | Layout 2 | `3c4ee3ff016a`  |
| 1838   | Layout 2 | `3c4ee3ff016a`  |
| 1832   | Layout 2 | `3c4ee3ff016a`  |
| 1826   | Layout 2 | `3c4ee3ff016a`  |
| 1822   | Layout 2 | `3c4ee3ff016a`  |
| 1818   | Layout 2 | `3c4ee3ff016a`  |
| 1804   | Layout 2 | `3c4ee3ff016a`  |
| 1794   | Layout 2 | `3c4ee3ff016a`  |
| 1790   | Layout 2 | `3c4ee3ff016a`  |
| 1784   | Layout 2 | `3c4ee3ff016a`  |
| 1774   | Layout 2 | `3c4ee3ff016a`  |
| 1771   | Layout 2 | `3c4ee3ff016a`  |
| 1762   | Layout 2 | `3c4ee3ff016a`  |
| 1759   | Layout 2 | `3c4ee3ff016a`  |
| 1754   | Layout 2 | `3c4ee3ff016a`  |
| 1749   | Layout 2 | `3c4ee3ff016a`  |
| 1743   | Layout 2 | `3c4ee3ff016a`  |
| 1737   | Layout 2 | `3c4ee3ff016a`  |
| 1731   | Layout 2 | `3c4ee3ff016a`  |
| 1725   | Layout 2 | `3c4ee3ff016a`  |
| 1717   | Layout 2 | `3c4ee3ff016a`  |
| 1710   | Layout 2 | `3c4ee3ff016a`  |
| 1704   | Layout 2 | `3c4ee3ff016a`  |
| 1698   | Layout 2 | `3c4ee3ff016a`  |
| 1690   | Layout 2 | `3c4ee3ff016a`  |
| 1685   | Layout 2 | `3c4ee3ff016a`  |
| 1680   | Layout 2 | `3c4ee3ff016a`  |
| 1674   | Layout 2 | `3c4ee3ff016a`  |
| 1668   | Layout 2 | `3c4ee3ff016a`  |
| 1659   | Layout 2 | `3c4ee3ff016a`  |
| 1649   | Layout 2 | `3c4ee3ff016a`  |
| 1642   | Layout 2 | `3c4ee3ff016a`  |
| 1636   | Layout 2 | `3c4ee3ff016a`  |
| 1628   | Layout 2 | `3c4ee3ff016a`  |
| 1622   | Layout 2 | `3c4ee3ff016a`  |
| 1614   | Layout 2 | `3c4ee3ff016a`  |
| 1608   | Layout 2 | `3c4ee3ff016a`  |
| 1602   | Layout 2 | `3c4ee3ff016a`  |
| 1598   | Layout 2 | `3c4ee3ff016a`  |
| 1594   | Layout 2 | `3c4ee3ff016a`  |
| 1590   | Layout 2 | `3c4ee3ff016a`  |
| 1587   | Layout 2 | `3c4ee3ff016a`  |
| 1584   | Layout 2 | `3c4ee3ff016a`  |
| 1579   | Layout 2 | `3c4ee3ff016a`  |
| 1572   | Layout 2 | `3c4ee3ff016a`  |
| 1565   | Layout 2 | `3c4ee3ff016a`  |
| 1559   | Layout 2 | `3c4ee3ff016a`  |
| 1554   | Layout 2 | `3c4ee3ff016a`  |
| 1547   | Layout 2 | `3c4ee3ff016a`  |
| 1537   | Layout 2 | `3c4ee3ff016a`  |
| 1529   | Layout 2 | `3c4ee3ff016a`  |
| 1524   | Layout 2 | `3c4ee3ff016a`  |
| 1519   | Layout 2 | `3c4ee3ff016a`  |
| 1509   | Layout 2 | `3c4ee3ff016a`  |
| 1506   | Layout 2 | `3c4ee3ff016a`  |
| 1504   | Layout 2 | `3c4ee3ff016a`  |
| 1500   | Layout 2 | `3c4ee3ff016a`  |
| 1493   | Layout 2 | `3c4ee3ff016a`  |
| 1489   | Layout 2 | `3c4ee3ff016a`  |
| 1485   | Layout 2 | `3c4ee3ff016a`  |
| 1481   | Layout 2 | `3c4ee3ff016a`  |
| 1474   | Layout 2 | `3c4ee3ff016a`  |
| 1466   | Layout 2 | `3c4ee3ff016a`  |
| 1462   | Layout 2 | `3c4ee3ff016a`  |
| 1459   | Layout 2 | `3c4ee3ff016a`  |
| 1453   | Layout 2 | `3c4ee3ff016a`  |
| 1450   | Layout 2 | `3c4ee3ff016a`  |
| 1445   | Layout 2 | `3c4ee3ff016a`  |
| 1439   | Layout 2 | `3c4ee3ff016a`  |
| 1433   | Layout 2 | `3c4ee3ff016a`  |
| 1430   | Layout 2 | `3c4ee3ff016a`  |
| 1426   | Layout 2 | `3c4ee3ff016a`  |
| 1421   | Layout 2 | `3c4ee3ff016a`  |
| 1417   | Layout 2 | `3c4ee3ff016a`  |
| 1416   | Layout 2 | `3c4ee3ff016a`  |
| 1409   | Layout 2 | `3c4ee3ff016a`  |
| 1405   | Layout 2 | `3c4ee3ff016a`  |
| 1401   | Layout 2 | `3c4ee3ff016a`  |
| 1396   | Layout 2 | `3c4ee3ff016a`  |
| 1391   | Layout 2 | `3c4ee3ff016a`  |
| 1390   | Layout 2 | `3c4ee3ff016a`  |
| 1386   | Layout 2 | `3c4ee3ff016a`  |
| 1381   | Layout 2 | `3c4ee3ff016a`  |
| 1379   | Layout 2 | `3c4ee3ff016a`  |
| 1372   | Layout 2 | `3c4ee3ff016a`  |
| 1366   | Layout 2 | `3c4ee3ff016a`  |
| 1364   | Layout 2 | `3c4ee3ff016a`  |
| 1363   | Layout 2 | `3c4ee3ff016a`  |
| 1360   | Layout 2 | `3c4ee3ff016a`  |
| 1358   | Layout 2 | `3c4ee3ff016a`  |
| 1355   | Layout 2 | `3c4ee3ff016a`  |
| 1351   | Layout 2 | `3c4ee3ff016a`  |
| 1348   | Layout 2 | `3c4ee3ff016a`  |
| 1346   | Layout 2 | `3c4ee3ff016a`  |
| 1341   | Layout 2 | `3c4ee3ff016a`  |
| 1340   | Layout 2 | `3c4ee3ff016a`  |
| 1338   | Layout 2 | `3c4ee3ff016a`  |
| 1335   | Layout 2 | `3c4ee3ff016a`  |
| 1333   | Layout 2 | `3c4ee3ff016a`  |
| 1329   | Layout 2 | `3c4ee3ff016a`  |
| 1327   | Layout 2 | `3c4ee3ff016a`  |
| 1324   | Layout 2 | `3c4ee3ff016a`  |
| 1321   | Layout 2 | `3c4ee3ff016a`  |
| 1319   | Layout 2 | `3c4ee3ff016a`  |
| 1318   | Layout 2 | `3c4ee3ff016a`  |
| 1316   | Layout 2 | `3c4ee3ff016a`  |
| 1313   | Layout 2 | `3c4ee3ff016a`  |
| 1311   | Layout 2 | `3c4ee3ff016a`  |
| 1309   | Layout 2 | `3c4ee3ff016a`  |
| 1304   | Layout 2 | `3c4ee3ff016a`  |
| 1292   | Layout 2 | `3c4ee3ff016a`  |
| 1286   | Layout 2 | `3c4ee3ff016a`  |
| 1280   | Layout 2 | `3c4ee3ff016a`  |
| 1276   | Layout 2 | `3c4ee3ff016a`  |
| 1267   | Layout 2 | `3c4ee3ff016a`  |
| 1261   | Layout 2 | `3c4ee3ff016a`  |
| 1256   | Layout 2 | `3c4ee3ff016a`  |
| 1250   | Layout 2 | `3c4ee3ff016a`  |
| 1246   | Layout 2 | `3c4ee3ff016a`  |
| 1239   | Layout 2 | `3c4ee3ff016a`  |
| 1230   | Layout 2 | `3c4ee3ff016a`  |
| 1226   | Layout 2 | `3c4ee3ff016a`  |
| 1220   | Layout 2 | `3c4ee3ff016a`  |
| 1217   | Layout 2 | `3c4ee3ff016a`  |
| 1211   | Layout 2 | `3c4ee3ff016a`  |
| 1210   | Layout 2 | `3c4ee3ff016a`  |
| 1208   | Layout 2 | `3c4ee3ff016a`  |
| 1203   | Layout 2 | `3c4ee3ff016a`  |
| 1197   | Layout 2 | `3c4ee3ff016a`  |
| 1194   | Layout 2 | `3c4ee3ff016a`  |
| 1192   | Layout 2 | `3c4ee3ff016a`  |
| 1187   | Layout 2 | `3c4ee3ff016a`  |
| 1183   | Layout 2 | `3c4ee3ff016a`  |
| 1177   | Layout 2 | `3c4ee3ff016a`  |
| 1173   | Layout 2 | `3c4ee3ff016a`  |
| 1167   | Layout 2 | `3c4ee3ff016a`  |
| 1164   | Layout 2 | `3c4ee3ff016a`  |
| 1156   | Layout 2 | `3c4ee3ff016a`  |
| 1149   | Layout 2 | `3c4ee3ff016a`  |
| 1144   | Layout 2 | `3c4ee3ff016a`  |
| 1137   | Layout 2 | `3c4ee3ff016a`  |
| 1132   | Layout 2 | `3c4ee3ff016a`  |
| 1127   | Layout 2 | `3c4ee3ff016a`  |
| 1122   | Layout 2 | `3c4ee3ff016a`  |
| 1118   | Layout 2 | `3c4ee3ff016a`  |
| 1114   | Layout 2 | `3c4ee3ff016a`  |
| 1109   | Layout 2 | `3c4ee3ff016a`  |
| 1102   | No file  | `3c4ee3ff016a`  |
| 1096   | No file  | `3c4ee3ff016a`  |
| 1088   | No file  | `3c4ee3ff016a`  |
| 1081   | No file  | `3c4ee3ff016a`  |
| 1076   | No file  | `3c4ee3ff016a`  |
| 1069   | No file  | `3c4ee3ff016a`  |
| 1064   | No file  | `3c4ee3ff016a`  |
| 1058   | No file  | `3c4ee3ff016a`  |
| 1051   | No file  | `3c4ee3ff016a`  |
| 1044   | No file  | `3c4ee3ff016a`  |
| 1036   | No file  | `3c4ee3ff016a`  |
| 1026   | No file  | `3c4ee3ff016a`  |
| 1016   | No file  | `3c4ee3ff016a`  |
| 1009   | No file  | `3c4ee3ff016a`  |
| 1005   | No file  | `3c4ee3ff016a`  |
| 1000   | No file  | `3c4ee3ff016a`  |
| 998    | No file  | `3c4ee3ff016a`  |
| 990    | No file  | `3c4ee3ff016a`  |
| 979    | No file  | `3c4ee3ff016a`  |
| 972    | No file  | `3c4ee3ff016a`  |
| 963    | No file  | `3c4ee3ff016a`  |
| 955    | No file  | `3c4ee3ff016a`  |
| 946    | No file  | `3c4ee3ff016a`  |
| 938    | No file  | `3c4ee3ff016a`  |
| 927    | No file  | `3c4ee3ff016a`  |
| 911    | No file  | `3c4ee3ff016a`  |
| 904    | No file  | `3c4ee3ff016a`  |
| 899    | No file  | `3c4ee3ff016a`  |
| 894    | No file  | `3c4ee3ff016a`  |
| 885    | No file  | `3c4ee3ff016a`  |
| 879    | No file  | `3c4ee3ff016a`  |
| 872    | No file  | `3c4ee3ff016a`  |
| 864    | No file  | `3c4ee3ff016a`  |
| 855    | No file  | `3c4ee3ff016a`  |
| 853    | No file  | `3c4ee3ff016a`  |
| 845    | No file  | `3c4ee3ff016a`  |
| 837    | No file  | `3c4ee3ff016a`  |
| 829    | Layout 2 | `3c4ee3ff016a`  |
| 822    | Layout 2 | `3c4ee3ff016a`  |
| 814    | Layout 2 | `3c4ee3ff016a`  |
| 805    | Layout 2 | `3c4ee3ff016a`  |
| 794    | Layout 1 | `3c4ee3ff016a`  |
| 787    | Layout 1 | `3c4ee3ff016a`  |
| 780    | Layout 1 | `3c4ee3ff016a`  |
| 771    | Layout 1 | `3c4ee3ff016a`  |
| 760    | Layout 1 | `3c4ee3ff016a`  |
| 748    | Layout 1 | `3c4ee3ff016a`  |
| 741    | Layout 1 | `3c4ee3ff016a`  |
| 736    | Layout 1 | `3c4ee3ff016a`  |
| 731    | Layout 1 | `3c4ee3ff016a`  |
| 723    | Layout 1 | `3c4ee3ff016a`  |
| 711    | Layout 1 | `3c4ee3ff016a`  |
| 707    | Layout 1 | `3c4ee3ff016a`  |
| 697    | Layout 1 | `3c4ee3ff016a`  |
| 689    | Layout 1 | `3c4ee3ff016a`  |
| 683    | Layout 1 | `3c4ee3ff016a`  |
| 678    | Layout 1 | `3c4ee3ff016a`  |
| 670    | Layout 1 | `3c4ee3ff016a`  |
| 661    | Layout 1 | `3c4ee3ff016a`  |
| 656    | Layout 1 | `3c4ee3ff016a`  |
| 652    | Layout 1 | `3c4ee3ff016a`  |
| 643    | Layout 1 | `3c4ee3ff016a`  |
| 637    | Layout 1 | `3c4ee3ff016a`  |
| 630    | Layout 1 | `3c4ee3ff016a`  |
| 627    | Layout 1 | `3c4ee3ff016a`  |
| 621    | Layout 1 | `3c4ee3ff016a`  |
| 617    | Layout 1 | `3c4ee3ff016a`  |
| 615    | Layout 1 | `3c4ee3ff016a`  |
| 606    | Layout 1 | `3c4ee3ff016a`  |
| 599    | Layout 1 | `3c4ee3ff016a`  |
| 592    | Layout 1 | `3c4ee3ff016a`  |
| 586    | Layout 1 | `3c4ee3ff016a`  |
| 577    | Layout 1 | `3c4ee3ff016a`  |
| 569    | Layout 1 | `3c4ee3ff016a`  |
| 561    | Layout 1 | `3c4ee3ff016a`  |
| 554    | Layout 1 | `3c4ee3ff016a`  |
| 542    | Layout 1 | `3c4ee3ff016a`  |
| 532    | Layout 1 | `3c4ee3ff016a`  |
| 531    | Layout 1 | `3c4ee3ff016a`  |
| 526    | Layout 1 | `3c4ee3ff016a`  |
| 521    | Layout 1 | `3c4ee3ff016a`  |
| 517    | Layout 1 | `3c4ee3ff016a`  |
| 510    | Layout 1 | `3c4ee3ff016a`  |
| 508    | Layout 1 | `3c4ee3ff016a`  |
| 504    | Layout 1 | `3c4ee3ff016a`  |
| 497    | Layout 1 | `3c4ee3ff016a`  |
| 491    | Layout 1 | `3c4ee3ff016a`  |
| 485    | Layout 1 | `3c4ee3ff016a`  |
| 478    | Layout 1 | `3c4ee3ff016a`  |
| 472    | Layout 1 | `3c4ee3ff016a`  |
| 466    | Layout 1 | `3c4ee3ff016a`  |
| 457    | Layout 1 | `3c4ee3ff016a`  |
| 452    | No file  | `3c4ee3ff016a`  |
| 449    | No file  | `3c4ee3ff016a`  |
| 435    | No file  | `3c4ee3ff016a`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Notes

- The source sheet `ProductSkill` of a private server's
  `uiproductskilltreelayout.xlsm` on client 1784 has `END` in V1 and A16,
  the 21 by 15 grid, and no value inside it (see
  [`uiguildskilltreelayout.bss` Field Names](uiguildskilltreelayout_bss.md#field-names)).
  Its template column lists four cell colours: 선행 스킬 (prerequisite
  skill), 단독 스킬 (standalone skill), 선택 스킬 (choice skill) and 선행
  조건 만족 스킬 (skill whose prerequisite is met).
- The client Lua of 3482 calls `getCombatSkillTree`,
  `getAwakeningWeaponSkillTree`, `getSuccessionSkillTree`,
  `getFusionSkillTree` and `getGuildSkillTree`; none reads a product or life
  skill tree.

## Open Questions

### What Window the Production Tree Belongs To

The grid is empty and no Lua reads it. The name points to a production
(life skill) skill tree that the game never filled; which window would
have shown it is open.
