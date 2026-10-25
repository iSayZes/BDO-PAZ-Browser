# `pcroommaid.bss` Format

## Purpose

The PC room maids and butlers: a u32 count and the u16 character key of
every [`maid.dbss`](../dbss/maid_dbss.md) row whose `pc_room_type` is set, in
`maid.dbss` row order.
On client 3474 these are the eight keys `18964` to `18967` and `18974` to
`18977`, each a Fairy Chiara or Ethan the Butler with the `[Oasis]` name
prefix (LOC type 6).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------- | ----- | ------- | --------- |
| 1      | 1230 and later | `pcroommaid.bss` | 20    | 8 Row   | 2         |

| Layout | File             | Known         | Unknown    |
| ------ | ---------------- | ------------- | ---------- |
| 1      | `pcroommaid.bss` | 20 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `57925a58e2a9`  |
| 3482   | Layout 1 | `57925a58e2a9`  |
| 3474   | Layout 1 | `57925a58e2a9`  |
| 3473   | Layout 1 | `57925a58e2a9`  |
| 3464   | Layout 1 | `57925a58e2a9`  |
| 3458   | Layout 1 | `57925a58e2a9`  |
| 3454   | Layout 1 | `57925a58e2a9`  |
| 3444   | Layout 1 | `57925a58e2a9`  |
| 3435   | Layout 1 | `57925a58e2a9`  |
| 3426   | Layout 1 | `57925a58e2a9`  |
| 3418   | Layout 1 | `57925a58e2a9`  |
| 3412   | Layout 1 | `57925a58e2a9`  |
| 3402   | Layout 1 | `57925a58e2a9`  |
| 3396   | Layout 1 | `57925a58e2a9`  |
| 3387   | Layout 1 | `57925a58e2a9`  |
| 3381   | Layout 1 | `57925a58e2a9`  |
| 3373   | Layout 1 | `57925a58e2a9`  |
| 3364   | Layout 1 | `57925a58e2a9`  |
| 3356   | Layout 1 | `57925a58e2a9`  |
| 3349   | Layout 1 | `57925a58e2a9`  |
| 3342   | Layout 1 | `57925a58e2a9`  |
| 3335   | Layout 1 | `57925a58e2a9`  |
| 3326   | Layout 1 | `57925a58e2a9`  |
| 3321   | Layout 1 | `57925a58e2a9`  |
| 3314   | Layout 1 | `57925a58e2a9`  |
| 3303   | Layout 1 | `57925a58e2a9`  |
| 3302   | Layout 1 | `57925a58e2a9`  |
| 3293   | Layout 1 | `57925a58e2a9`  |
| 3283   | Layout 1 | `57925a58e2a9`  |
| 3275   | Layout 1 | `57925a58e2a9`  |
| 3267   | Layout 1 | `57925a58e2a9`  |
| 3258   | Layout 1 | `57925a58e2a9`  |
| 3251   | Layout 1 | `57925a58e2a9`  |
| 3242   | Layout 1 | `57925a58e2a9`  |
| 3235   | Layout 1 | `57925a58e2a9`  |
| 3229   | Layout 1 | `57925a58e2a9`  |
| 3212   | Layout 1 | `57925a58e2a9`  |
| 3203   | Layout 1 | `57925a58e2a9`  |
| 3193   | Layout 1 | `57925a58e2a9`  |
| 3186   | Layout 1 | `57925a58e2a9`  |
| 3177   | Layout 1 | `57925a58e2a9`  |
| 3169   | Layout 1 | `57925a58e2a9`  |
| 3158   | Layout 1 | `57925a58e2a9`  |
| 3151   | Layout 1 | `57925a58e2a9`  |
| 3144   | Layout 1 | `57925a58e2a9`  |
| 3133   | Layout 1 | `57925a58e2a9`  |
| 3125   | Layout 1 | `57925a58e2a9`  |
| 3118   | Layout 1 | `57925a58e2a9`  |
| 3111   | Layout 1 | `57925a58e2a9`  |
| 3103   | Layout 1 | `57925a58e2a9`  |
| 3095   | Layout 1 | `57925a58e2a9`  |
| 3086   | Layout 1 | `57925a58e2a9`  |
| 3072   | Layout 1 | `57925a58e2a9`  |
| 3062   | Layout 1 | `57925a58e2a9`  |
| 3052   | Layout 1 | `57925a58e2a9`  |
| 3045   | Layout 1 | `57925a58e2a9`  |
| 3037   | Layout 1 | `57925a58e2a9`  |
| 3030   | Layout 1 | `57925a58e2a9`  |
| 3021   | Layout 1 | `57925a58e2a9`  |
| 3012   | Layout 1 | `57925a58e2a9`  |
| 3002   | Layout 1 | `57925a58e2a9`  |
| 2995   | Layout 1 | `57925a58e2a9`  |
| 2987   | Layout 1 | `57925a58e2a9`  |
| 2978   | Layout 1 | `57925a58e2a9`  |
| 2970   | Layout 1 | `57925a58e2a9`  |
| 2959   | Layout 1 | `57925a58e2a9`  |
| 2951   | Layout 1 | `57925a58e2a9`  |
| 2942   | Layout 1 | `57925a58e2a9`  |
| 2935   | Layout 1 | `57925a58e2a9`  |
| 2932   | Layout 1 | `57925a58e2a9`  |
| 2923   | Layout 1 | `57925a58e2a9`  |
| 2919   | Layout 1 | `57925a58e2a9`  |
| 2907   | Layout 1 | `57925a58e2a9`  |
| 2900   | Layout 1 | `57925a58e2a9`  |
| 2891   | Layout 1 | `57925a58e2a9`  |
| 2882   | Layout 1 | `57925a58e2a9`  |
| 2872   | Layout 1 | `57925a58e2a9`  |
| 2863   | Layout 1 | `57925a58e2a9`  |
| 2855   | Layout 1 | `57925a58e2a9`  |
| 2849   | Layout 1 | `57925a58e2a9`  |
| 2844   | Layout 1 | `57925a58e2a9`  |
| 2834   | Layout 1 | `57925a58e2a9`  |
| 2825   | Layout 1 | `57925a58e2a9`  |
| 2819   | Layout 1 | `57925a58e2a9`  |
| 2811   | Layout 1 | `57925a58e2a9`  |
| 2803   | Layout 1 | `57925a58e2a9`  |
| 2794   | Layout 1 | `57925a58e2a9`  |
| 2783   | Layout 1 | `57925a58e2a9`  |
| 2774   | Layout 1 | `57925a58e2a9`  |
| 2765   | Layout 1 | `57925a58e2a9`  |
| 2756   | Layout 1 | `57925a58e2a9`  |
| 2750   | Layout 1 | `57925a58e2a9`  |
| 2743   | Layout 1 | `57925a58e2a9`  |
| 2736   | Layout 1 | `57925a58e2a9`  |
| 2726   | Layout 1 | `57925a58e2a9`  |
| 2717   | Layout 1 | `57925a58e2a9`  |
| 2709   | Layout 1 | `57925a58e2a9`  |
| 2703   | Layout 1 | `57925a58e2a9`  |
| 2695   | Layout 1 | `57925a58e2a9`  |
| 2684   | Layout 1 | `57925a58e2a9`  |
| 2672   | Layout 1 | `57925a58e2a9`  |
| 2665   | Layout 1 | `57925a58e2a9`  |
| 2657   | Layout 1 | `57925a58e2a9`  |
| 2649   | Layout 1 | `57925a58e2a9`  |
| 2644   | Layout 1 | `57925a58e2a9`  |
| 2637   | Layout 1 | `57925a58e2a9`  |
| 2629   | Layout 1 | `57925a58e2a9`  |
| 2619   | Layout 1 | `57925a58e2a9`  |
| 2612   | Layout 1 | `57925a58e2a9`  |
| 2606   | Layout 1 | `57925a58e2a9`  |
| 2602   | Layout 1 | `57925a58e2a9`  |
| 2601   | Layout 1 | `57925a58e2a9`  |
| 2592   | Layout 1 | `57925a58e2a9`  |
| 2583   | Layout 1 | `57925a58e2a9`  |
| 2575   | Layout 1 | `57925a58e2a9`  |
| 2567   | Layout 1 | `57925a58e2a9`  |
| 2560   | Layout 1 | `57925a58e2a9`  |
| 2553   | Layout 1 | `57925a58e2a9`  |
| 2545   | Layout 1 | `57925a58e2a9`  |
| 2538   | Layout 1 | `57925a58e2a9`  |
| 2529   | Layout 1 | `57925a58e2a9`  |
| 2519   | Layout 1 | `57925a58e2a9`  |
| 2513   | Layout 1 | `57925a58e2a9`  |
| 2510   | Layout 1 | `57925a58e2a9`  |
| 2507   | Layout 1 | `57925a58e2a9`  |
| 2503   | Layout 1 | `57925a58e2a9`  |
| 2498   | Layout 1 | `57925a58e2a9`  |
| 2492   | Layout 1 | `57925a58e2a9`  |
| 2487   | Layout 1 | `57925a58e2a9`  |
| 2480   | Layout 1 | `57925a58e2a9`  |
| 2474   | Layout 1 | `57925a58e2a9`  |
| 2468   | Layout 1 | `57925a58e2a9`  |
| 2460   | Layout 1 | `57925a58e2a9`  |
| 2453   | Layout 1 | `57925a58e2a9`  |
| 2444   | Layout 1 | `57925a58e2a9`  |
| 2438   | Layout 1 | `57925a58e2a9`  |
| 2434   | Layout 1 | `57925a58e2a9`  |
| 2429   | Layout 1 | `57925a58e2a9`  |
| 2421   | Layout 1 | `57925a58e2a9`  |
| 2414   | Layout 1 | `57925a58e2a9`  |
| 2407   | Layout 1 | `57925a58e2a9`  |
| 2401   | Layout 1 | `57925a58e2a9`  |
| 2397   | Layout 1 | `57925a58e2a9`  |
| 2393   | Layout 1 | `57925a58e2a9`  |
| 2384   | Layout 1 | `57925a58e2a9`  |
| 2378   | Layout 1 | `57925a58e2a9`  |
| 2372   | Layout 1 | `57925a58e2a9`  |
| 2358   | Layout 1 | `57925a58e2a9`  |
| 2352   | Layout 1 | `57925a58e2a9`  |
| 2347   | Layout 1 | `57925a58e2a9`  |
| 2343   | Layout 1 | `57925a58e2a9`  |
| 2335   | Layout 1 | `57925a58e2a9`  |
| 2327   | Layout 1 | `57925a58e2a9`  |
| 2324   | Layout 1 | `57925a58e2a9`  |
| 2319   | Layout 1 | `57925a58e2a9`  |
| 2313   | Layout 1 | `57925a58e2a9`  |
| 2308   | Layout 1 | `57925a58e2a9`  |
| 2302   | Layout 1 | `57925a58e2a9`  |
| 2295   | Layout 1 | `57925a58e2a9`  |
| 2290   | Layout 1 | `57925a58e2a9`  |
| 2284   | Layout 1 | `57925a58e2a9`  |
| 2276   | Layout 1 | `57925a58e2a9`  |
| 2269   | Layout 1 | `57925a58e2a9`  |
| 2259   | Layout 1 | `57925a58e2a9`  |
| 2250   | Layout 1 | `57925a58e2a9`  |
| 2243   | Layout 1 | `57925a58e2a9`  |
| 2235   | Layout 1 | `57925a58e2a9`  |
| 2229   | Layout 1 | `57925a58e2a9`  |
| 2224   | Layout 1 | `57925a58e2a9`  |
| 2218   | Layout 1 | `57925a58e2a9`  |
| 2215   | Layout 1 | `57925a58e2a9`  |
| 2207   | Layout 1 | `57925a58e2a9`  |
| 2203   | Layout 1 | `57925a58e2a9`  |
| 2196   | Layout 1 | `57925a58e2a9`  |
| 2192   | Layout 1 | `57925a58e2a9`  |
| 2189   | Layout 1 | `57925a58e2a9`  |
| 2183   | Layout 1 | `57925a58e2a9`  |
| 2179   | Layout 1 | `57925a58e2a9`  |
| 2171   | Layout 1 | `57925a58e2a9`  |
| 2163   | Layout 1 | `57925a58e2a9`  |
| 2156   | Layout 1 | `57925a58e2a9`  |
| 2151   | Layout 1 | `57925a58e2a9`  |
| 2147   | Layout 1 | `57925a58e2a9`  |
| 2142   | Layout 1 | `57925a58e2a9`  |
| 2138   | Layout 1 | `57925a58e2a9`  |
| 2134   | Layout 1 | `57925a58e2a9`  |
| 2130   | Layout 1 | `57925a58e2a9`  |
| 2122   | Layout 1 | `57925a58e2a9`  |
| 2107   | Layout 1 | `57925a58e2a9`  |
| 2098   | Layout 1 | `57925a58e2a9`  |
| 2089   | Layout 1 | `57925a58e2a9`  |
| 2081   | Layout 1 | `57925a58e2a9`  |
| 2073   | Layout 1 | `57925a58e2a9`  |
| 2067   | Layout 1 | `57925a58e2a9`  |
| 2063   | Layout 1 | `57925a58e2a9`  |
| 2059   | Layout 1 | `57925a58e2a9`  |
| 2052   | Layout 1 | `57925a58e2a9`  |
| 2044   | Layout 1 | `57925a58e2a9`  |
| 2039   | Layout 1 | `57925a58e2a9`  |
| 2032   | Layout 1 | `57925a58e2a9`  |
| 2025   | Layout 1 | `57925a58e2a9`  |
| 2011   | Layout 1 | `57925a58e2a9`  |
| 2005   | Layout 1 | `57925a58e2a9`  |
| 2000   | Layout 1 | `57925a58e2a9`  |
| 1996   | Layout 1 | `57925a58e2a9`  |
| 1991   | Layout 1 | `57925a58e2a9`  |
| 1985   | Layout 1 | `57925a58e2a9`  |
| 1980   | Layout 1 | `57925a58e2a9`  |
| 1969   | Layout 1 | `57925a58e2a9`  |
| 1964   | Layout 1 | `57925a58e2a9`  |
| 1958   | Layout 1 | `57925a58e2a9`  |
| 1950   | Layout 1 | `57925a58e2a9`  |
| 1945   | Layout 1 | `57925a58e2a9`  |
| 1937   | Layout 1 | `57925a58e2a9`  |
| 1933   | Layout 1 | `57925a58e2a9`  |
| 1927   | Layout 1 | `57925a58e2a9`  |
| 1921   | Layout 1 | `57925a58e2a9`  |
| 1914   | Layout 1 | `57925a58e2a9`  |
| 1908   | Layout 1 | `57925a58e2a9`  |
| 1897   | Layout 1 | `57925a58e2a9`  |
| 1892   | Layout 1 | `57925a58e2a9`  |
| 1886   | Layout 1 | `57925a58e2a9`  |
| 1881   | Layout 1 | `57925a58e2a9`  |
| 1871   | Layout 1 | `57925a58e2a9`  |
| 1866   | Layout 1 | `57925a58e2a9`  |
| 1862   | Layout 1 | `57925a58e2a9`  |
| 1854   | Layout 1 | `57925a58e2a9`  |
| 1846   | Layout 1 | `57925a58e2a9`  |
| 1838   | Layout 1 | `57925a58e2a9`  |
| 1832   | Layout 1 | `57925a58e2a9`  |
| 1826   | Layout 1 | `57925a58e2a9`  |
| 1822   | Layout 1 | `57925a58e2a9`  |
| 1818   | Layout 1 | `57925a58e2a9`  |
| 1804   | Layout 1 | `57925a58e2a9`  |
| 1794   | Layout 1 | `57925a58e2a9`  |
| 1790   | Layout 1 | `57925a58e2a9`  |
| 1784   | Layout 1 | `57925a58e2a9`  |
| 1774   | Layout 1 | `57925a58e2a9`  |
| 1771   | Layout 1 | `57925a58e2a9`  |
| 1762   | Layout 1 | `57925a58e2a9`  |
| 1759   | Layout 1 | `57925a58e2a9`  |
| 1754   | Layout 1 | `57925a58e2a9`  |
| 1749   | Layout 1 | `57925a58e2a9`  |
| 1743   | Layout 1 | `57925a58e2a9`  |
| 1737   | Layout 1 | `57925a58e2a9`  |
| 1731   | Layout 1 | `57925a58e2a9`  |
| 1725   | Layout 1 | `57925a58e2a9`  |
| 1717   | Layout 1 | `57925a58e2a9`  |
| 1710   | Layout 1 | `57925a58e2a9`  |
| 1704   | Layout 1 | `57925a58e2a9`  |
| 1698   | Layout 1 | `57925a58e2a9`  |
| 1690   | Layout 1 | `57925a58e2a9`  |
| 1685   | Layout 1 | `57925a58e2a9`  |
| 1680   | Layout 1 | `57925a58e2a9`  |
| 1674   | Layout 1 | `57925a58e2a9`  |
| 1668   | Layout 1 | `57925a58e2a9`  |
| 1659   | Layout 1 | `57925a58e2a9`  |
| 1649   | Layout 1 | `57925a58e2a9`  |
| 1642   | Layout 1 | `57925a58e2a9`  |
| 1636   | Layout 1 | `57925a58e2a9`  |
| 1628   | Layout 1 | `57925a58e2a9`  |
| 1622   | Layout 1 | `57925a58e2a9`  |
| 1614   | Layout 1 | `57925a58e2a9`  |
| 1608   | Layout 1 | `57925a58e2a9`  |
| 1602   | Layout 1 | `57925a58e2a9`  |
| 1598   | Layout 1 | `57925a58e2a9`  |
| 1594   | Layout 1 | `57925a58e2a9`  |
| 1590   | Layout 1 | `57925a58e2a9`  |
| 1587   | Layout 1 | `57925a58e2a9`  |
| 1584   | Layout 1 | `57925a58e2a9`  |
| 1579   | Layout 1 | `57925a58e2a9`  |
| 1572   | Layout 1 | `57925a58e2a9`  |
| 1565   | Layout 1 | `57925a58e2a9`  |
| 1559   | Layout 1 | `57925a58e2a9`  |
| 1554   | Layout 1 | `57925a58e2a9`  |
| 1547   | Layout 1 | `57925a58e2a9`  |
| 1537   | Layout 1 | `57925a58e2a9`  |
| 1529   | Layout 1 | `57925a58e2a9`  |
| 1524   | Layout 1 | `57925a58e2a9`  |
| 1519   | Layout 1 | `57925a58e2a9`  |
| 1509   | Layout 1 | `57925a58e2a9`  |
| 1506   | Layout 1 | `57925a58e2a9`  |
| 1504   | Layout 1 | `57925a58e2a9`  |
| 1500   | Layout 1 | `57925a58e2a9`  |
| 1493   | Layout 1 | `57925a58e2a9`  |
| 1489   | Layout 1 | `57925a58e2a9`  |
| 1485   | Layout 1 | `57925a58e2a9`  |
| 1481   | Layout 1 | `57925a58e2a9`  |
| 1474   | Layout 1 | `57925a58e2a9`  |
| 1466   | Layout 1 | `57925a58e2a9`  |
| 1462   | Layout 1 | `57925a58e2a9`  |
| 1459   | Layout 1 | `57925a58e2a9`  |
| 1453   | Layout 1 | `57925a58e2a9`  |
| 1450   | Layout 1 | `57925a58e2a9`  |
| 1445   | Layout 1 | `57925a58e2a9`  |
| 1439   | Layout 1 | `57925a58e2a9`  |
| 1433   | Layout 1 | `57925a58e2a9`  |
| 1430   | Layout 1 | `57925a58e2a9`  |
| 1426   | Layout 1 | `57925a58e2a9`  |
| 1421   | Layout 1 | `57925a58e2a9`  |
| 1417   | Layout 1 | `57925a58e2a9`  |
| 1416   | Layout 1 | `57925a58e2a9`  |
| 1409   | Layout 1 | `57925a58e2a9`  |
| 1405   | Layout 1 | `57925a58e2a9`  |
| 1401   | Layout 1 | `57925a58e2a9`  |
| 1396   | Layout 1 | `57925a58e2a9`  |
| 1391   | Layout 1 | `57925a58e2a9`  |
| 1390   | Layout 1 | `57925a58e2a9`  |
| 1386   | Layout 1 | `57925a58e2a9`  |
| 1381   | Layout 1 | `57925a58e2a9`  |
| 1379   | Layout 1 | `57925a58e2a9`  |
| 1372   | Layout 1 | `57925a58e2a9`  |
| 1366   | Layout 1 | `57925a58e2a9`  |
| 1364   | Layout 1 | `57925a58e2a9`  |
| 1363   | Layout 1 | `57925a58e2a9`  |
| 1360   | Layout 1 | `57925a58e2a9`  |
| 1358   | Layout 1 | `57925a58e2a9`  |
| 1355   | Layout 1 | `57925a58e2a9`  |
| 1351   | Layout 1 | `57925a58e2a9`  |
| 1348   | Layout 1 | `57925a58e2a9`  |
| 1346   | Layout 1 | `57925a58e2a9`  |
| 1341   | Layout 1 | `57925a58e2a9`  |
| 1340   | Layout 1 | `57925a58e2a9`  |
| 1338   | Layout 1 | `57925a58e2a9`  |
| 1335   | Layout 1 | `57925a58e2a9`  |
| 1333   | Layout 1 | `57925a58e2a9`  |
| 1329   | Layout 1 | `57925a58e2a9`  |
| 1327   | Layout 1 | `57925a58e2a9`  |
| 1324   | Layout 1 | `57925a58e2a9`  |
| 1321   | Layout 1 | `57925a58e2a9`  |
| 1319   | Layout 1 | `57925a58e2a9`  |
| 1318   | Layout 1 | `57925a58e2a9`  |
| 1316   | Layout 1 | `57925a58e2a9`  |
| 1313   | Layout 1 | `57925a58e2a9`  |
| 1311   | Layout 1 | `57925a58e2a9`  |
| 1309   | Layout 1 | `57925a58e2a9`  |
| 1304   | Layout 1 | `57925a58e2a9`  |
| 1292   | Layout 1 | `57925a58e2a9`  |
| 1286   | Layout 1 | `57925a58e2a9`  |
| 1280   | Layout 1 | `57925a58e2a9`  |
| 1276   | Layout 1 | `57925a58e2a9`  |
| 1267   | Layout 1 | `57925a58e2a9`  |
| 1261   | Layout 1 | `57925a58e2a9`  |
| 1256   | Layout 1 | `57925a58e2a9`  |
| 1250   | Layout 1 | `57925a58e2a9`  |
| 1246   | Layout 1 | `57925a58e2a9`  |
| 1239   | Layout 1 | `57925a58e2a9`  |
| 1230   | Layout 1 | `57925a58e2a9`  |
| 1226   | No file  | `57925a58e2a9`  |
| 1220   | No file  | `57925a58e2a9`  |
| 1217   | No file  | `57925a58e2a9`  |
| 1211   | No file  | `57925a58e2a9`  |
| 1210   | No file  | `57925a58e2a9`  |
| 1208   | No file  | `57925a58e2a9`  |
| 1203   | No file  | `57925a58e2a9`  |
| 1197   | No file  | `57925a58e2a9`  |
| 1194   | No file  | `57925a58e2a9`  |
| 1192   | No file  | `57925a58e2a9`  |
| 1187   | No file  | `57925a58e2a9`  |
| 1183   | No file  | `57925a58e2a9`  |
| 1177   | No file  | `57925a58e2a9`  |
| 1173   | No file  | `57925a58e2a9`  |
| 1167   | No file  | `57925a58e2a9`  |
| 1164   | No file  | `57925a58e2a9`  |
| 1156   | No file  | `57925a58e2a9`  |
| 1149   | No file  | `57925a58e2a9`  |
| 1144   | No file  | `57925a58e2a9`  |
| 1137   | No file  | `57925a58e2a9`  |
| 1132   | No file  | `57925a58e2a9`  |
| 1127   | No file  | `57925a58e2a9`  |
| 1122   | No file  | `57925a58e2a9`  |
| 1118   | No file  | `57925a58e2a9`  |
| 1114   | No file  | `57925a58e2a9`  |
| 1109   | No file  | `57925a58e2a9`  |
| 1102   | No file  | `57925a58e2a9`  |
| 1096   | No file  | `57925a58e2a9`  |
| 1088   | No file  | `57925a58e2a9`  |
| 1081   | No file  | `57925a58e2a9`  |
| 1076   | No file  | `57925a58e2a9`  |
| 1069   | No file  | `57925a58e2a9`  |
| 1064   | No file  | `57925a58e2a9`  |
| 1058   | No file  | `57925a58e2a9`  |
| 1051   | No file  | `57925a58e2a9`  |
| 1044   | No file  | `57925a58e2a9`  |
| 1036   | No file  | `57925a58e2a9`  |
| 1026   | No file  | `57925a58e2a9`  |
| 1016   | No file  | `57925a58e2a9`  |
| 1009   | No file  | `57925a58e2a9`  |
| 1005   | No file  | `57925a58e2a9`  |
| 1000   | No file  | `57925a58e2a9`  |
| 998    | No file  | `57925a58e2a9`  |
| 990    | No file  | `57925a58e2a9`  |
| 979    | No file  | `57925a58e2a9`  |
| 972    | No file  | `57925a58e2a9`  |
| 963    | No file  | `57925a58e2a9`  |
| 955    | No file  | `57925a58e2a9`  |
| 946    | No file  | `57925a58e2a9`  |
| 938    | No file  | `57925a58e2a9`  |
| 927    | No file  | `57925a58e2a9`  |
| 911    | No file  | `57925a58e2a9`  |
| 904    | No file  | `57925a58e2a9`  |
| 899    | No file  | `57925a58e2a9`  |
| 894    | No file  | `57925a58e2a9`  |
| 885    | No file  | `57925a58e2a9`  |
| 879    | No file  | `57925a58e2a9`  |
| 872    | No file  | `57925a58e2a9`  |
| 864    | No file  | `57925a58e2a9`  |
| 855    | No file  | `57925a58e2a9`  |
| 853    | No file  | `57925a58e2a9`  |
| 845    | No file  | `57925a58e2a9`  |
| 837    | No file  | `57925a58e2a9`  |
| 829    | No file  | `57925a58e2a9`  |
| 822    | No file  | `57925a58e2a9`  |
| 814    | No file  | `57925a58e2a9`  |
| 805    | No file  | `57925a58e2a9`  |
| 794    | No file  | `57925a58e2a9`  |
| 787    | No file  | `57925a58e2a9`  |
| 780    | No file  | `57925a58e2a9`  |
| 771    | No file  | `57925a58e2a9`  |
| 760    | No file  | `57925a58e2a9`  |
| 748    | No file  | `57925a58e2a9`  |
| 741    | No file  | `57925a58e2a9`  |
| 736    | No file  | `57925a58e2a9`  |
| 731    | No file  | `57925a58e2a9`  |
| 723    | No file  | `57925a58e2a9`  |
| 711    | No file  | `57925a58e2a9`  |
| 707    | No file  | `57925a58e2a9`  |
| 697    | No file  | `57925a58e2a9`  |
| 689    | No file  | `57925a58e2a9`  |
| 683    | No file  | `57925a58e2a9`  |
| 678    | No file  | `57925a58e2a9`  |
| 670    | No file  | `57925a58e2a9`  |
| 661    | No file  | `57925a58e2a9`  |
| 656    | No file  | `57925a58e2a9`  |
| 652    | No file  | `57925a58e2a9`  |
| 643    | No file  | `57925a58e2a9`  |
| 637    | No file  | `57925a58e2a9`  |
| 630    | No file  | `57925a58e2a9`  |
| 627    | No file  | `57925a58e2a9`  |
| 621    | No file  | `57925a58e2a9`  |
| 617    | No file  | `57925a58e2a9`  |
| 615    | No file  | `57925a58e2a9`  |
| 606    | No file  | `57925a58e2a9`  |
| 599    | No file  | `57925a58e2a9`  |
| 592    | No file  | `57925a58e2a9`  |
| 586    | No file  | `57925a58e2a9`  |
| 577    | No file  | `57925a58e2a9`  |
| 569    | No file  | `57925a58e2a9`  |
| 561    | No file  | `57925a58e2a9`  |
| 554    | No file  | `57925a58e2a9`  |
| 542    | No file  | `57925a58e2a9`  |
| 532    | No file  | `57925a58e2a9`  |
| 531    | No file  | `57925a58e2a9`  |
| 526    | No file  | `57925a58e2a9`  |
| 521    | No file  | `57925a58e2a9`  |
| 517    | No file  | `57925a58e2a9`  |
| 510    | No file  | `57925a58e2a9`  |
| 508    | No file  | `57925a58e2a9`  |
| 504    | No file  | `57925a58e2a9`  |
| 497    | No file  | `57925a58e2a9`  |
| 491    | No file  | `57925a58e2a9`  |
| 485    | No file  | `57925a58e2a9`  |
| 478    | No file  | `57925a58e2a9`  |
| 472    | No file  | `57925a58e2a9`  |
| 466    | No file  | `57925a58e2a9`  |
| 457    | No file  | `57925a58e2a9`  |
| 452    | No file  | `57925a58e2a9`  |
| 449    | No file  | `57925a58e2a9`  |
| 435    | No file  | `57925a58e2a9`  |

<!-- versions:end -->

## Companion Files

| File                 | Required | Role                                                                  |
| -------------------- | -------- | --------------------------------------------------------------------- |
| `maidoffset.dbss`    | Optional | Which keys have a [`maid.dbss`](../dbss/maid_dbss.md) row to link to          |
| `languagedata_*.loc` | Optional | Character names, LOC type 6, keyed by `character_key`                 |

The key column links to the `maid.dbss` row, and that row's key links on to
`characterstatic.dbss`, so the view loads no `characterstatic.dbss`
companion. Without `maidoffset.dbss` every key stays a link.

All multi-byte values are little-endian.

## Layout 1

### File Layout

Plain binary: no `PABR` magic, no offset file and no trailer.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 8 x 2 = 20 bytes on client 3474.

### Row (2 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of a `maid.dbss` row and a LOC type 6 character name    |

## PC Room Maids

| character_key | Name (LOC type 6, client 3474) | Duty in the client 1784 `Maid_Table` |
| ------------- | ------------------------------ | ------------------------------------ |
| `18964`       | [Oasis] Fairy Chiara           | Warehouse                            |
| `18965`       | [Oasis] Fairy Chiara           | Marketplace                          |
| `18966`       | [Oasis] Ethan the Butler       | Warehouse                            |
| `18967`       | [Oasis] Ethan the Butler       | Marketplace                          |
| `18974`       | [Oasis] Fairy Chiara           | Not in the sheet                     |
| `18975`       | [Oasis] Fairy Chiara           | Not in the sheet                     |
| `18976`       | [Oasis] Ethan the Butler       | Not in the sheet                     |
| `18977`       | [Oasis] Ethan the Butler       | Not in the sheet                     |

The duty is the sheet's `IsAbleInWareHouse` (warehouse) or
`IsAbleSubmitMarket` (marketplace) column. On client 3474 the `maid.dbss`
rows of `18974` to `18977` are the bytes of `18964` to `18967` with only
the key changed.

## Field Names

The `Maid_Table` sheet of a private server's `DataSheets.bexcel` on client
1784 has a `PcRoomType` column, `1` on `18964` to `18967` and `0` on its
other 17 rows; the file on client 1784 lists exactly those four keys. The
sheet names the key column `CharacterKey`, hence `character_key`. No sheet
of that workbook is named after the file; its only PC room maid data is
the `PcRoomType` column.

## Notes

- The keys match `maid.dbss` by value on both clients checked: the u8 at
  `+0x13` of each `maid.dbss` row (counted from its u16 key, where
  `maidoffset.dbss` points) is `1` on exactly the listed keys and `0` on
  the rest (4 of 21 rows on client 1784, 8 of 27 on client 3474), and the
  file lists them in the order `maidoffset.dbss` lists the rows.
- Clients 1230, 1485, 1784 and 2107 hold the 12-byte file with `18967` to
  `18964`; clients 2519, 3002, 3251 and 3474 hold the 20-byte file with
  `18977` to `18974` added in front. Client 794 has no file. The private
  server's own compiled `pcroommaid.bss` (client 1784) is the same 12 bytes
  as the client file.
- The client Lua of the maid list (`panel_window_maidlist_all`) shows a PC
  room button when `_ContentsGroup_KR_Transfer` is on and
  `ToClient_isShowRegistPcRoomMaidButton()` returns true, and the button
  calls `ToClient_RegistPcRoomMaid()`. With the same content group the maid
  list opens in a premium PC room (`isPremiumPcRoom()`) even when the
  player has no maids. The client 1784 server dump has the request
  `eTrRegistPcRoomMaidReq` and `gm::PlayerActor::registPcRoomMaid`. No
  client Lua reads the keys directly.

## Open Questions

### Why Two Sets of PC Room Maids

Client 2519 added `18974` to `18977`, copies of `18964` to `18967` with new
keys and the same names. Whether the server registers one set or both in a
PC room cannot be read from the client data, and neither the LOC nor the
client Lua says what the second set is for.
