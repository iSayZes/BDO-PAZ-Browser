# `enchantfailcountexpstaticstatus.bss` Format

## Purpose

A table keyed by enhancement fail stack. On client 3474 each record holds one
`stack` and, for every feed key and enhancement level of
[fairyfeedenchantfailcount.bss](fairyfeedenchantfailcount_bss.md), a value
that falls as the stack rises and is non-zero only inside that entry's stack
range (see Stack Ranges). Client 1784 ships a different table under the same
stem: the EXP needed per fail stack, from the `FairyFeed_Range` developer
sheet (Layout 1).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                         | Bytes  | Records                              | Row bytes |
| ------ | -------------- | ------- | -------------------------------------------- | ------ | ------------------------------------ | --------- |
| 2      | 1109 and later | 3483    | `enchantfailcountexpstaticstatus.bss`        | 39,620 | 3,600 Entry, 2,800 Group, 400 Record | 5         |
| 1      | 1286 to 3212   | 3212    | `enchantfailcountexpstaticstatus.dbss`       | 5,140  | 321 Row                              | 16        |
| 1      | 1286 to 3212   | 3212    | `enchantfailcountexpstaticstatusoffset.dbss` | 5,140  | 321 Offset Row                       | 16        |

| Layout | File                                         | Known            | Unknown          |
| ------ | -------------------------------------------- | ---------------- | ---------------- |
| 2      | `enchantfailcountexpstaticstatus.bss`        | 25,220 B (63.7%) | 14,400 B (36.3%) |
| 1      | `enchantfailcountexpstaticstatus.dbss`       | 5,140 B (100.0%) | 0 B (0.0%)       |
| 1      | `enchantfailcountexpstaticstatusoffset.dbss` | 5,140 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `0837094b2ea7`  |
| 3482   | Layout 2             | `0837094b2ea7`  |
| 3474   | Layout 2             | `0837094b2ea7`  |
| 3473   | Layout 2             | `0837094b2ea7`  |
| 3464   | Layout 2             | `0837094b2ea7`  |
| 3458   | Layout 2             | `0837094b2ea7`  |
| 3454   | Layout 2             | `0837094b2ea7`  |
| 3444   | Layout 2             | `0837094b2ea7`  |
| 3435   | Layout 2             | `0837094b2ea7`  |
| 3426   | Layout 2             | `0837094b2ea7`  |
| 3418   | Layout 2             | `0837094b2ea7`  |
| 3412   | Layout 2             | `0837094b2ea7`  |
| 3402   | Layout 2             | `0837094b2ea7`  |
| 3396   | Layout 2             | `0837094b2ea7`  |
| 3387   | Layout 2             | `0837094b2ea7`  |
| 3381   | Layout 2             | `0837094b2ea7`  |
| 3373   | Layout 2             | `0837094b2ea7`  |
| 3364   | Layout 2             | `0837094b2ea7`  |
| 3356   | Layout 2             | `0837094b2ea7`  |
| 3349   | Layout 2             | `0837094b2ea7`  |
| 3342   | Layout 2             | `0837094b2ea7`  |
| 3335   | Layout 2             | `0837094b2ea7`  |
| 3326   | Layout 2             | `0837094b2ea7`  |
| 3321   | Layout 2             | `0837094b2ea7`  |
| 3314   | Layout 2             | `0837094b2ea7`  |
| 3303   | Layout 2             | `0837094b2ea7`  |
| 3302   | Layout 2             | `0837094b2ea7`  |
| 3293   | Layout 2             | `0837094b2ea7`  |
| 3283   | Layout 2             | `0837094b2ea7`  |
| 3275   | Layout 2             | `0837094b2ea7`  |
| 3267   | Layout 2             | `0837094b2ea7`  |
| 3258   | Layout 2             | `0837094b2ea7`  |
| 3251   | Layout 2             | `0837094b2ea7`  |
| 3242   | Layout 2             | `0837094b2ea7`  |
| 3235   | Layout 2             | `0837094b2ea7`  |
| 3229   | Layout 2             | `0837094b2ea7`  |
| 3212   | Layout 1             | `0837094b2ea7`  |
| 3203   | Layout 1             | `0837094b2ea7`  |
| 3193   | Layout 1             | `0837094b2ea7`  |
| 3186   | Layout 1             | `0837094b2ea7`  |
| 3177   | Layout 1             | `0837094b2ea7`  |
| 3169   | Layout 1             | `0837094b2ea7`  |
| 3158   | Layout 1             | `0837094b2ea7`  |
| 3151   | Layout 1             | `0837094b2ea7`  |
| 3144   | Layout 1             | `0837094b2ea7`  |
| 3133   | Layout 1             | `0837094b2ea7`  |
| 3125   | Layout 1             | `0837094b2ea7`  |
| 3118   | Layout 1             | `0837094b2ea7`  |
| 3111   | Layout 1             | `0837094b2ea7`  |
| 3103   | Layout 1             | `0837094b2ea7`  |
| 3095   | Layout 1             | `0837094b2ea7`  |
| 3086   | Layout 1             | `0837094b2ea7`  |
| 3072   | Layout 1             | `0837094b2ea7`  |
| 3062   | Layout 1             | `0837094b2ea7`  |
| 3052   | Layout 1             | `0837094b2ea7`  |
| 3045   | Layout 1             | `0837094b2ea7`  |
| 3037   | Layout 1             | `0837094b2ea7`  |
| 3030   | Layout 1             | `0837094b2ea7`  |
| 3021   | Layout 1             | `0837094b2ea7`  |
| 3012   | Layout 1             | `0837094b2ea7`  |
| 3002   | Layout 1             | `0837094b2ea7`  |
| 2995   | Layout 1             | `0837094b2ea7`  |
| 2987   | Layout 1             | `0837094b2ea7`  |
| 2978   | Layout 1             | `0837094b2ea7`  |
| 2970   | Layout 1             | `0837094b2ea7`  |
| 2959   | Layout 1             | `0837094b2ea7`  |
| 2951   | Layout 1             | `0837094b2ea7`  |
| 2942   | Layout 1             | `0837094b2ea7`  |
| 2935   | Layout 1             | `0837094b2ea7`  |
| 2932   | Layout 1             | `0837094b2ea7`  |
| 2923   | Layout 1             | `0837094b2ea7`  |
| 2919   | Layout 1             | `0837094b2ea7`  |
| 2907   | Layout 1             | `0837094b2ea7`  |
| 2900   | Layout 1             | `0837094b2ea7`  |
| 2891   | Layout 1             | `0837094b2ea7`  |
| 2882   | Layout 1             | `0837094b2ea7`  |
| 2872   | Layout 1             | `0837094b2ea7`  |
| 2863   | Layout 1             | `0837094b2ea7`  |
| 2855   | Layout 1             | `0837094b2ea7`  |
| 2849   | Layout 1             | `0837094b2ea7`  |
| 2844   | Layout 1             | `0837094b2ea7`  |
| 2834   | Layout 1             | `0837094b2ea7`  |
| 2825   | Layout 1             | `0837094b2ea7`  |
| 2819   | Layout 1             | `0837094b2ea7`  |
| 2811   | Layout 1             | `0837094b2ea7`  |
| 2803   | Layout 1             | `0837094b2ea7`  |
| 2794   | Layout 1             | `0837094b2ea7`  |
| 2783   | Layout 1             | `0837094b2ea7`  |
| 2774   | Layout 1             | `0837094b2ea7`  |
| 2765   | Layout 1             | `0837094b2ea7`  |
| 2756   | Layout 1             | `0837094b2ea7`  |
| 2750   | Layout 1             | `0837094b2ea7`  |
| 2743   | Layout 1             | `0837094b2ea7`  |
| 2736   | Layout 1             | `0837094b2ea7`  |
| 2726   | Layout 1             | `0837094b2ea7`  |
| 2717   | Layout 1             | `0837094b2ea7`  |
| 2709   | Layout 1             | `0837094b2ea7`  |
| 2703   | Layout 1             | `0837094b2ea7`  |
| 2695   | Layout 1             | `0837094b2ea7`  |
| 2684   | Layout 1             | `0837094b2ea7`  |
| 2672   | Layout 1             | `0837094b2ea7`  |
| 2665   | Layout 1             | `0837094b2ea7`  |
| 2657   | Layout 1             | `0837094b2ea7`  |
| 2649   | Layout 1             | `0837094b2ea7`  |
| 2644   | Layout 1             | `0837094b2ea7`  |
| 2637   | Layout 1             | `0837094b2ea7`  |
| 2629   | Layout 1             | `0837094b2ea7`  |
| 2619   | Layout 1             | `0837094b2ea7`  |
| 2612   | Layout 1             | `0837094b2ea7`  |
| 2606   | Layout 1             | `0837094b2ea7`  |
| 2602   | Layout 1             | `0837094b2ea7`  |
| 2601   | Layout 1             | `0837094b2ea7`  |
| 2592   | Layout 1             | `0837094b2ea7`  |
| 2583   | Layout 1             | `0837094b2ea7`  |
| 2575   | Layout 1             | `0837094b2ea7`  |
| 2567   | Layout 1             | `0837094b2ea7`  |
| 2560   | Layout 1             | `0837094b2ea7`  |
| 2553   | Layout 1             | `0837094b2ea7`  |
| 2545   | Layout 1             | `0837094b2ea7`  |
| 2538   | Layout 1             | `0837094b2ea7`  |
| 2529   | Layout 1             | `0837094b2ea7`  |
| 2519   | Layout 1             | `0837094b2ea7`  |
| 2513   | Layout 1             | `0837094b2ea7`  |
| 2510   | Layout 1             | `0837094b2ea7`  |
| 2507   | Layout 1             | `0837094b2ea7`  |
| 2503   | Layout 1             | `0837094b2ea7`  |
| 2498   | Layout 1             | `0837094b2ea7`  |
| 2492   | Layout 1             | `0837094b2ea7`  |
| 2487   | Layout 1             | `0837094b2ea7`  |
| 2480   | Layout 1             | `0837094b2ea7`  |
| 2474   | Layout 1             | `0837094b2ea7`  |
| 2468   | Layout 1             | `0837094b2ea7`  |
| 2460   | Layout 1             | `0837094b2ea7`  |
| 2453   | Layout 1             | `0837094b2ea7`  |
| 2444   | Layout 1             | `0837094b2ea7`  |
| 2438   | Layout 1             | `0837094b2ea7`  |
| 2434   | Layout 1             | `0837094b2ea7`  |
| 2429   | Layout 1             | `0837094b2ea7`  |
| 2421   | Layout 1             | `0837094b2ea7`  |
| 2414   | Layout 1             | `0837094b2ea7`  |
| 2407   | Layout 1             | `0837094b2ea7`  |
| 2401   | Layout 1             | `0837094b2ea7`  |
| 2397   | Layout 1             | `0837094b2ea7`  |
| 2393   | Layout 1             | `0837094b2ea7`  |
| 2384   | Layout 1             | `0837094b2ea7`  |
| 2378   | Layout 1             | `0837094b2ea7`  |
| 2372   | Layout 1             | `0837094b2ea7`  |
| 2358   | Layout 1             | `0837094b2ea7`  |
| 2352   | Layout 1             | `0837094b2ea7`  |
| 2347   | Layout 1             | `0837094b2ea7`  |
| 2343   | Layout 1             | `0837094b2ea7`  |
| 2335   | Layout 1             | `0837094b2ea7`  |
| 2327   | Layout 1             | `0837094b2ea7`  |
| 2324   | Layout 1             | `0837094b2ea7`  |
| 2319   | Layout 1             | `0837094b2ea7`  |
| 2313   | Layout 1             | `0837094b2ea7`  |
| 2308   | Layout 1             | `0837094b2ea7`  |
| 2302   | Layout 1             | `0837094b2ea7`  |
| 2295   | Layout 1             | `0837094b2ea7`  |
| 2290   | Layout 1             | `0837094b2ea7`  |
| 2284   | Layout 1             | `0837094b2ea7`  |
| 2276   | Layout 1             | `0837094b2ea7`  |
| 2269   | Layout 1             | `0837094b2ea7`  |
| 2259   | Layout 1             | `0837094b2ea7`  |
| 2250   | Layout 1             | `0837094b2ea7`  |
| 2243   | Layout 1             | `0837094b2ea7`  |
| 2235   | Layout 1             | `0837094b2ea7`  |
| 2229   | Layout 1             | `0837094b2ea7`  |
| 2224   | Layout 1             | `0837094b2ea7`  |
| 2218   | Layout 1             | `0837094b2ea7`  |
| 2215   | Layout 1             | `0837094b2ea7`  |
| 2207   | Layout 1             | `0837094b2ea7`  |
| 2203   | Layout 1             | `0837094b2ea7`  |
| 2196   | Layout 1             | `0837094b2ea7`  |
| 2192   | Layout 1             | `0837094b2ea7`  |
| 2189   | Layout 1             | `0837094b2ea7`  |
| 2183   | Layout 1             | `0837094b2ea7`  |
| 2179   | Layout 1             | `0837094b2ea7`  |
| 2171   | Layout 1             | `0837094b2ea7`  |
| 2163   | Layout 1             | `0837094b2ea7`  |
| 2156   | Layout 1             | `0837094b2ea7`  |
| 2151   | Layout 1             | `0837094b2ea7`  |
| 2147   | Layout 1             | `0837094b2ea7`  |
| 2142   | Layout 1             | `0837094b2ea7`  |
| 2138   | Layout 1             | `0837094b2ea7`  |
| 2134   | Layout 1             | `0837094b2ea7`  |
| 2130   | Layout 1             | `0837094b2ea7`  |
| 2122   | Layout 1             | `0837094b2ea7`  |
| 2107   | Layout 1             | `0837094b2ea7`  |
| 2098   | Layout 1             | `0837094b2ea7`  |
| 2089   | Layout 1             | `0837094b2ea7`  |
| 2081   | Layout 1             | `0837094b2ea7`  |
| 2073   | Layout 1             | `0837094b2ea7`  |
| 2067   | Layout 1             | `0837094b2ea7`  |
| 2063   | Layout 1             | `0837094b2ea7`  |
| 2059   | Layout 1             | `0837094b2ea7`  |
| 2052   | Layout 1             | `0837094b2ea7`  |
| 2044   | Layout 1             | `0837094b2ea7`  |
| 2039   | Layout 1             | `0837094b2ea7`  |
| 2032   | Layout 1             | `0837094b2ea7`  |
| 2025   | Layout 1             | `0837094b2ea7`  |
| 2011   | Layout 1             | `0837094b2ea7`  |
| 2005   | Layout 1             | `0837094b2ea7`  |
| 2000   | Layout 1             | `0837094b2ea7`  |
| 1996   | Layout 1             | `0837094b2ea7`  |
| 1991   | Layout 1             | `0837094b2ea7`  |
| 1985   | Layout 1             | `0837094b2ea7`  |
| 1980   | Layout 1             | `0837094b2ea7`  |
| 1969   | Layout 1             | `0837094b2ea7`  |
| 1964   | Layout 1             | `0837094b2ea7`  |
| 1958   | Layout 1             | `0837094b2ea7`  |
| 1950   | Layout 1             | `0837094b2ea7`  |
| 1945   | Layout 1             | `0837094b2ea7`  |
| 1937   | Layout 1             | `0837094b2ea7`  |
| 1933   | Layout 1             | `0837094b2ea7`  |
| 1927   | Layout 1             | `0837094b2ea7`  |
| 1921   | Layout 1             | `0837094b2ea7`  |
| 1914   | Layout 1             | `0837094b2ea7`  |
| 1908   | Layout 1             | `0837094b2ea7`  |
| 1897   | Layout 1             | `0837094b2ea7`  |
| 1892   | Layout 1             | `0837094b2ea7`  |
| 1886   | Layout 1             | `0837094b2ea7`  |
| 1881   | Layout 1             | `0837094b2ea7`  |
| 1871   | Layout 1             | `0837094b2ea7`  |
| 1866   | Layout 1             | `0837094b2ea7`  |
| 1862   | Layout 1             | `0837094b2ea7`  |
| 1854   | Layout 1             | `0837094b2ea7`  |
| 1846   | Layout 1             | `0837094b2ea7`  |
| 1838   | Layout 1             | `0837094b2ea7`  |
| 1832   | Layout 1             | `0837094b2ea7`  |
| 1826   | Layout 1             | `0837094b2ea7`  |
| 1822   | Layout 1             | `0837094b2ea7`  |
| 1818   | Layout 1             | `0837094b2ea7`  |
| 1804   | Layout 1             | `0837094b2ea7`  |
| 1794   | Layout 1             | `0837094b2ea7`  |
| 1790   | Layout 1             | `0837094b2ea7`  |
| 1784   | Layout 1             | `0837094b2ea7`  |
| 1774   | Layout 1             | `0837094b2ea7`  |
| 1771   | Layout 1             | `0837094b2ea7`  |
| 1762   | Layout 1             | `0837094b2ea7`  |
| 1759   | Layout 1             | `0837094b2ea7`  |
| 1754   | Layout 1             | `0837094b2ea7`  |
| 1749   | Layout 1             | `0837094b2ea7`  |
| 1743   | Layout 1             | `0837094b2ea7`  |
| 1737   | Layout 1             | `0837094b2ea7`  |
| 1731   | Layout 1             | `0837094b2ea7`  |
| 1725   | Layout 1             | `0837094b2ea7`  |
| 1717   | Layout 1             | `0837094b2ea7`  |
| 1710   | Layout 1             | `0837094b2ea7`  |
| 1704   | Layout 1             | `0837094b2ea7`  |
| 1698   | Layout 1             | `0837094b2ea7`  |
| 1690   | Layout 1             | `0837094b2ea7`  |
| 1685   | Layout 1             | `0837094b2ea7`  |
| 1680   | Layout 1             | `0837094b2ea7`  |
| 1674   | Layout 1             | `0837094b2ea7`  |
| 1668   | Layout 1             | `0837094b2ea7`  |
| 1659   | Layout 1             | `0837094b2ea7`  |
| 1649   | Layout 1             | `0837094b2ea7`  |
| 1642   | Layout 1             | `0837094b2ea7`  |
| 1636   | Layout 1             | `0837094b2ea7`  |
| 1628   | Layout 1             | `0837094b2ea7`  |
| 1622   | Layout 1             | `0837094b2ea7`  |
| 1614   | Layout 1             | `0837094b2ea7`  |
| 1608   | Layout 1             | `0837094b2ea7`  |
| 1602   | Layout 1             | `0837094b2ea7`  |
| 1598   | Layout 1             | `0837094b2ea7`  |
| 1594   | Layout 1             | `0837094b2ea7`  |
| 1590   | Layout 1             | `0837094b2ea7`  |
| 1587   | Layout 1             | `0837094b2ea7`  |
| 1584   | Layout 1             | `0837094b2ea7`  |
| 1579   | Layout 1             | `0837094b2ea7`  |
| 1572   | Layout 1             | `0837094b2ea7`  |
| 1565   | Layout 1             | `0837094b2ea7`  |
| 1559   | Layout 1             | `0837094b2ea7`  |
| 1554   | Layout 1             | `0837094b2ea7`  |
| 1547   | Layout 1             | `0837094b2ea7`  |
| 1537   | Layout 1             | `0837094b2ea7`  |
| 1529   | Layout 1             | `0837094b2ea7`  |
| 1524   | Layout 1             | `0837094b2ea7`  |
| 1519   | Layout 1             | `0837094b2ea7`  |
| 1509   | Layout 1             | `0837094b2ea7`  |
| 1506   | Layout 1             | `0837094b2ea7`  |
| 1504   | Layout 1             | `0837094b2ea7`  |
| 1500   | Layout 1             | `0837094b2ea7`  |
| 1493   | Layout 1             | `0837094b2ea7`  |
| 1489   | Layout 1             | `0837094b2ea7`  |
| 1485   | Layout 1             | `0837094b2ea7`  |
| 1481   | Layout 1             | `0837094b2ea7`  |
| 1474   | Layout 1             | `0837094b2ea7`  |
| 1466   | Layout 1             | `0837094b2ea7`  |
| 1462   | Layout 1             | `0837094b2ea7`  |
| 1459   | Layout 1             | `0837094b2ea7`  |
| 1453   | Layout 1             | `0837094b2ea7`  |
| 1450   | Layout 1             | `0837094b2ea7`  |
| 1445   | Layout 1             | `0837094b2ea7`  |
| 1439   | Layout 1             | `0837094b2ea7`  |
| 1433   | Layout 1             | `0837094b2ea7`  |
| 1430   | Layout 1             | `0837094b2ea7`  |
| 1426   | Layout 1             | `0837094b2ea7`  |
| 1421   | Layout 1             | `0837094b2ea7`  |
| 1417   | Layout 1             | `0837094b2ea7`  |
| 1416   | Layout 1             | `0837094b2ea7`  |
| 1409   | Layout 1             | `0837094b2ea7`  |
| 1405   | Layout 1             | `0837094b2ea7`  |
| 1401   | Layout 1             | `0837094b2ea7`  |
| 1396   | Layout 1             | `0837094b2ea7`  |
| 1391   | Layout 1             | `0837094b2ea7`  |
| 1390   | Layout 1             | `0837094b2ea7`  |
| 1386   | Layout 1             | `0837094b2ea7`  |
| 1381   | Layout 1             | `0837094b2ea7`  |
| 1379   | Layout 1             | `0837094b2ea7`  |
| 1372   | Layout 1             | `0837094b2ea7`  |
| 1366   | Layout 1             | `0837094b2ea7`  |
| 1364   | Layout 1             | `0837094b2ea7`  |
| 1363   | Layout 1             | `0837094b2ea7`  |
| 1360   | Layout 1             | `0837094b2ea7`  |
| 1358   | Layout 1             | `0837094b2ea7`  |
| 1355   | Layout 1             | `0837094b2ea7`  |
| 1351   | Layout 1             | `0837094b2ea7`  |
| 1348   | Layout 1             | `0837094b2ea7`  |
| 1346   | Layout 1             | `0837094b2ea7`  |
| 1341   | Layout 1             | `0837094b2ea7`  |
| 1340   | Layout 1             | `0837094b2ea7`  |
| 1338   | Layout 1             | `0837094b2ea7`  |
| 1335   | Layout 1             | `0837094b2ea7`  |
| 1333   | Layout 1             | `0837094b2ea7`  |
| 1329   | Layout 1             | `0837094b2ea7`  |
| 1327   | Layout 1             | `0837094b2ea7`  |
| 1324   | Layout 1             | `0837094b2ea7`  |
| 1321   | Layout 1             | `0837094b2ea7`  |
| 1319   | Layout 1             | `0837094b2ea7`  |
| 1318   | Layout 1             | `0837094b2ea7`  |
| 1316   | Layout 1             | `0837094b2ea7`  |
| 1313   | Layout 1             | `0837094b2ea7`  |
| 1311   | Layout 1             | `0837094b2ea7`  |
| 1309   | Layout 1             | `0837094b2ea7`  |
| 1304   | Layout 1             | `0837094b2ea7`  |
| 1292   | Layout 1             | `0837094b2ea7`  |
| 1286   | Layout 1             | `0837094b2ea7`  |
| 1280   | No documented layout | `0837094b2ea7`  |
| 1276   | No documented layout | `0837094b2ea7`  |
| 1267   | No documented layout | `0837094b2ea7`  |
| 1261   | No documented layout | `0837094b2ea7`  |
| 1256   | No documented layout | `0837094b2ea7`  |
| 1250   | No documented layout | `0837094b2ea7`  |
| 1246   | No documented layout | `0837094b2ea7`  |
| 1239   | No documented layout | `0837094b2ea7`  |
| 1230   | No documented layout | `0837094b2ea7`  |
| 1226   | No documented layout | `0837094b2ea7`  |
| 1220   | No documented layout | `0837094b2ea7`  |
| 1217   | No documented layout | `0837094b2ea7`  |
| 1211   | No documented layout | `0837094b2ea7`  |
| 1210   | No documented layout | `0837094b2ea7`  |
| 1208   | No documented layout | `0837094b2ea7`  |
| 1203   | No documented layout | `0837094b2ea7`  |
| 1197   | No documented layout | `0837094b2ea7`  |
| 1194   | No documented layout | `0837094b2ea7`  |
| 1192   | No documented layout | `0837094b2ea7`  |
| 1187   | No documented layout | `0837094b2ea7`  |
| 1183   | No documented layout | `0837094b2ea7`  |
| 1177   | Layout 2             | `0837094b2ea7`  |
| 1173   | Layout 2             | `0837094b2ea7`  |
| 1167   | Layout 2             | `0837094b2ea7`  |
| 1164   | Layout 2             | `0837094b2ea7`  |
| 1156   | Layout 2             | `0837094b2ea7`  |
| 1149   | Layout 2             | `0837094b2ea7`  |
| 1144   | Layout 2             | `0837094b2ea7`  |
| 1137   | Layout 2             | `0837094b2ea7`  |
| 1132   | Layout 2             | `0837094b2ea7`  |
| 1127   | Layout 2             | `0837094b2ea7`  |
| 1122   | Layout 2             | `0837094b2ea7`  |
| 1118   | Layout 2             | `0837094b2ea7`  |
| 1114   | Layout 2             | `0837094b2ea7`  |
| 1109   | Layout 2             | `0837094b2ea7`  |
| 1102   | No file              | `0837094b2ea7`  |
| 1096   | No file              | `0837094b2ea7`  |
| 1088   | No file              | `0837094b2ea7`  |
| 1081   | No file              | `0837094b2ea7`  |
| 1076   | No file              | `0837094b2ea7`  |
| 1069   | No file              | `0837094b2ea7`  |
| 1064   | No file              | `0837094b2ea7`  |
| 1058   | No file              | `0837094b2ea7`  |
| 1051   | No file              | `0837094b2ea7`  |
| 1044   | No file              | `0837094b2ea7`  |
| 1036   | No file              | `0837094b2ea7`  |
| 1026   | No file              | `0837094b2ea7`  |
| 1016   | No file              | `0837094b2ea7`  |
| 1009   | No file              | `0837094b2ea7`  |
| 1005   | No file              | `0837094b2ea7`  |
| 1000   | No file              | `0837094b2ea7`  |
| 998    | No file              | `0837094b2ea7`  |
| 990    | No file              | `0837094b2ea7`  |
| 979    | No file              | `0837094b2ea7`  |
| 972    | No file              | `0837094b2ea7`  |
| 963    | No file              | `0837094b2ea7`  |
| 955    | No file              | `0837094b2ea7`  |
| 946    | No file              | `0837094b2ea7`  |
| 938    | No file              | `0837094b2ea7`  |
| 927    | No file              | `0837094b2ea7`  |
| 911    | No file              | `0837094b2ea7`  |
| 904    | No file              | `0837094b2ea7`  |
| 899    | No file              | `0837094b2ea7`  |
| 894    | No file              | `0837094b2ea7`  |
| 885    | No file              | `0837094b2ea7`  |
| 879    | No file              | `0837094b2ea7`  |
| 872    | No file              | `0837094b2ea7`  |
| 864    | No file              | `0837094b2ea7`  |
| 855    | No file              | `0837094b2ea7`  |
| 853    | No file              | `0837094b2ea7`  |
| 845    | No file              | `0837094b2ea7`  |
| 837    | No file              | `0837094b2ea7`  |
| 829    | No file              | `0837094b2ea7`  |
| 822    | No file              | `0837094b2ea7`  |
| 814    | No file              | `0837094b2ea7`  |
| 805    | No file              | `0837094b2ea7`  |
| 794    | No file              | `0837094b2ea7`  |
| 787    | No file              | `0837094b2ea7`  |
| 780    | No file              | `0837094b2ea7`  |
| 771    | No file              | `0837094b2ea7`  |
| 760    | No file              | `0837094b2ea7`  |
| 748    | No file              | `0837094b2ea7`  |
| 741    | No file              | `0837094b2ea7`  |
| 736    | No file              | `0837094b2ea7`  |
| 731    | No file              | `0837094b2ea7`  |
| 723    | No file              | `0837094b2ea7`  |
| 711    | No file              | `0837094b2ea7`  |
| 707    | No file              | `0837094b2ea7`  |
| 697    | No file              | `0837094b2ea7`  |
| 689    | No file              | `0837094b2ea7`  |
| 683    | No file              | `0837094b2ea7`  |
| 678    | No file              | `0837094b2ea7`  |
| 670    | No file              | `0837094b2ea7`  |
| 661    | No file              | `0837094b2ea7`  |
| 656    | No file              | `0837094b2ea7`  |
| 652    | No file              | `0837094b2ea7`  |
| 643    | No file              | `0837094b2ea7`  |
| 637    | No file              | `0837094b2ea7`  |
| 630    | No file              | `0837094b2ea7`  |
| 627    | No file              | `0837094b2ea7`  |
| 621    | No file              | `0837094b2ea7`  |
| 617    | No file              | `0837094b2ea7`  |
| 615    | No file              | `0837094b2ea7`  |
| 606    | No file              | `0837094b2ea7`  |
| 599    | No file              | `0837094b2ea7`  |
| 592    | No file              | `0837094b2ea7`  |
| 586    | No file              | `0837094b2ea7`  |
| 577    | No file              | `0837094b2ea7`  |
| 569    | No file              | `0837094b2ea7`  |
| 561    | No file              | `0837094b2ea7`  |
| 554    | No file              | `0837094b2ea7`  |
| 542    | No file              | `0837094b2ea7`  |
| 532    | No file              | `0837094b2ea7`  |
| 531    | No file              | `0837094b2ea7`  |
| 526    | No file              | `0837094b2ea7`  |
| 521    | No file              | `0837094b2ea7`  |
| 517    | No file              | `0837094b2ea7`  |
| 510    | No file              | `0837094b2ea7`  |
| 508    | No file              | `0837094b2ea7`  |
| 504    | No file              | `0837094b2ea7`  |
| 497    | No file              | `0837094b2ea7`  |
| 491    | No file              | `0837094b2ea7`  |
| 485    | No file              | `0837094b2ea7`  |
| 478    | No file              | `0837094b2ea7`  |
| 472    | No file              | `0837094b2ea7`  |
| 466    | No file              | `0837094b2ea7`  |
| 457    | No file              | `0837094b2ea7`  |
| 452    | No file              | `0837094b2ea7`  |
| 449    | No file              | `0837094b2ea7`  |
| 435    | No file              | `0837094b2ea7`  |

<!-- versions:end -->

## Companion Files

None on client 3474: the file has no offset index, and no companion is
needed to parse it. Client 1784 ships the table as
`enchantfailcountexpstaticstatus.dbss` with the index
`enchantfailcountexpstaticstatusoffset.dbss` (Layout 1).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type          | Field          | Notes                                       |
| ------------------- | ------------- | -------------- | ------------------------------------------- |
| `+0x00`             | char[4]       | magic          | `PABR` (ASCII)                              |
| `+0x04`             | u32           | count          | Number of records; 400 on client 3474       |
| `+0x08`             | Record[count] | records        | Variable-length records, back to back       |
| `records+0x00`      | String Table  | string_table   | The PABR string table, here with no strings |
| `string_table+0x00` | u32           | end_of_records | Byte offset just past the last record       |
| `string_table+0x04` | u32           | zero           | Always `0`                                  |

### Record (variable: 12 bytes + groups)

| Offset        | Type               | Field       | Notes                                              |
| ------------- | ------------------ | ----------- | -------------------------------------------------- |
| `+0x00`       | u32                | group_count | 7 on every record (client 3474)                    |
| `+0x04`       | Group[group_count] | groups      | One per `fairy_feed_key`                           |
| `groups+0x00` | u64                | stack       | `Stack`; the record key, after the groups; 0 to 399 on client 3474 |

### Group (variable: 6 bytes + entries)

| Offset  | Type               | Field          | Notes                                         |
| ------- | ------------------ | -------------- | --------------------------------------------- |
| `+0x00` | u16                | fairy_feed_key | `FairyFeedKey`; 1 to 7 in that order (client 3474) |
| `+0x02` | u32                | entry_count    | 2 under keys 1 and 2, 1 under keys 3 to 7 (client 3474) |
| `+0x06` | Entry[entry_count] | entries        |                                               |

### Entry (5 bytes)

| Offset  | Type | Field         | Notes                                                    |
| ------- | ---- | ------------- | -------------------------------------------------------- |
| `+0x00` | u8   | enchant_level | `EnchantValue`; 19 (TET) and 20 (PEN) under keys 1 and 2, 0 under keys 3 to 7 |
| `+0x01` | u32  | unknown_01    | 0 to 75 on client 3474; non-zero only inside the entry's stack range |

The entry is unaligned: `unknown_01` starts at an odd offset.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Observed | Notes        |
| ------- | ------------------ | ------------ | -------- | ------------ |
| `+0x00` | u32                | string_count | 0        | Always zero  |
| `+0x04` | pstr[string_count] | strings      |          | Empty        |

## Layout 1

### `enchantfailcountexpstaticstatus.dbss`

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | 251 on client 1784                      |
| `+0x04` | Row[count] | rows  | `count` rows of 16 bytes, ending at EOF |

### Row (16 bytes)

| Offset  | Type | Field     | Notes                                       |
| ------- | ---- | --------- | ------------------------------------------- |
| `+0x00` | u64  | stack     | `Stack`; 0 to 250 in order (client 1784)    |
| `+0x08` | u64  | stack_exp | `StackExp`; 1 at stack 0, 99 at stack 1, 691,830 from stack 240 (client 1784) |

### `enchantfailcountexpstaticstatusoffset.dbss`

| Offset  | Type              | Field   | Notes                                                   |
| ------- | ----------------- | ------- | ------------------------------------------------------- |
| `+0x00` | u32               | count   | Equals the `enchantfailcountexpstaticstatus.dbss` count |
| `+0x04` | Offset Row[count] | entries | `count` entries of 16 bytes                             |

### Offset Row (16 bytes)

| Offset  | Type | Field  | Notes                            |
| ------- | ---- | ------ | -------------------------------- |
| `+0x00` | u64  | stack  | The row's `stack`                |
| `+0x08` | u32  | offset | Where the row starts: `4 + 16 × index` |
| `+0x0C` | u32  | size   | 16 on every entry                |

## Stack Ranges

On client 3474 every record holds the same nine (`fairy_feed_key`,
`enchant_level`) pairs, in the order of the nine entries of
`fairyfeedenchantfailcount.bss`. For each pair, `unknown_01` is non-zero
exactly when `stack` is at least that entry's `feed_value` and below its
`equip_exp`: 0 misses over the 3,600 values. Within a range the value never
rises as `stack` rises. Keys 1 and 2 hold the same values at every stack.

| `stack` (client 3474) | Key 1, 2 TET | Key 1, 2 PEN | Key 3 | Key 4 | Key 5 | Key 6 | Key 7 |
| --------------------- | ------------ | ------------ | ----- | ----- | ----- | ----- | ----- |
| Range                 | 0 to 199     | 0 to 299     | 100 to 299 | 100 to 299 | 100 to 299 | 100 to 299 | 300 to 349 |
| 0                     | 55           | 75           | 0     | 0     | 0     | 0     | 0     |
| 50                    | 13           | 30           | 0     | 0     | 0     | 0     | 0     |
| 100                   | 4            | 10           | 6     | 26    | 13    | 52    | 0     |
| 150                   | 2            | 5            | 3     | 15    | 7     | 30    | 0     |
| 199                   | 1            | 3            | 2     | 10    | 5     | 20    | 0     |
| 250                   | 0            | 2            | 1     | 7     | 3     | 14    | 0     |
| 299                   | 0            | 1            | 1     | 1     | 1     | 1     | 0     |
| 300 to 349            | 0            | 0            | 0     | 0     | 0     | 0     | 1     |
| 350 to 399            | 0            | 0            | 0     | 0     | 0     | 0     | 0     |

The client Lua has the same ranges. `panel_window_enchantstack_all_1.lua`
groups the items of the enchant stack list by `getStartEndStackIndex()` and
titles each group with `PANEL_ENCHANT_RENEWAL_STACK_RANGE`, filled from
`ToClient_GetStartStackByIndex` and `ToClient_GetEndStackByIndex`. An item
with `isPredation()` opens a number pad whose maximum is
`ToClient_GetAvailablePredationStack(index)`. No Lua call reads this table's
values directly.

## Field Names

The server dump of a private server on client 1784
(`Instance_dumpFull.exe`) inserts this table's rows into
`EnchantFailCountExpStaticStatusManager` at VA `0x140b70a20`, which logs
"Insert Fail Stack(%#) , NeedExp(%#)". The `FairyFeed_Range` sheet of the
same server's `DataSheets.bexcel` has the columns `Stack` and `StackExp`:
the client 1784 `.dbss` matches it on 251 of 251 rows, both columns.

On client 3474 the record key is again a u64 stack, 0 to 399, so it keeps
the name `stack`. The client 3474 file has no `StackExp` column.
`fairy_feed_key` and `enchant_level` hold the nine (key, level) pairs of
`fairyfeedenchantfailcount.bss` on the same client, in the same order and
widths, so they take that doc's names. `unknown_01` matches no sheet column.

## Notes

- The record stream ends at `end_of_records`: 400 records of
  `4 + 7 × 6 + 9 × 5 + 8 = 99` bytes are 39,600 bytes after the 8-byte header
  (client 3474), and the 12-byte trailer closes the file.
- `stack` sits after the groups, at the end of each record. The first record
  starts with `group_count` right after the header, and the last `stack`
  (398) sits right before the string table.
- Records are not in `stack` order: 399, 0, 1, 393, 2, 3 at the start of the
  file (client 3474).
- The `.bss` keeps the stem of the client 1784 `.dbss`, but none of its
  values: there is no EXP column and the record count went from 251 to 400.

## Open Questions

### What `unknown_01` Counts

`unknown_01` is the only value per (stack, key, level). It is largest at the
bottom of each range (75 for PEN at stack 0, 52 for key 6 at stack 100) and
falls to 1 before the range ends, which fits the number of fail stacks that
feeding one item adds at the current stack. The client Lua shows a
per-item stack maximum (`ToClient_GetAvailablePredationStack`) but not where
it comes from, so the reading is not confirmed.

### Items Under Keys 3 to 7

Same open point as in
[fairyfeedenchantfailcount.bss](fairyfeedenchantfailcount_bss.md): which
items carry `FairyFeedKey` 3 to 7 is not known, so the item behind each
column of Stack Ranges is open for those keys.
