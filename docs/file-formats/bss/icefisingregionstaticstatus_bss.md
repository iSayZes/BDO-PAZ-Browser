# `icefisingregionstaticstatus.bss` Format

## Purpose

The regions where the ice fishing mini-game runs and which mini-game group
each one uses. Each 4-byte row holds a [`regioninfo.bss`](regioninfo_bss.md)
region key and a mini-game group. The rows start right after the PABR magic
and run up to the string table; no count is stored. On client 3474 the two
rows are Snowfall Crasher: Alpine Glide (`1176`, group `1`) and Gyeonghoeru
Pavilion (`1484`, group `2`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                              | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | `icefisingregionstaticstatus.bss` | 24    | 2 Row   | 4         |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `icefisingregionstaticstatus.bss` | 24 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `ce9a21ac36f1`  |
| 3482   | Layout 1 | `ce9a21ac36f1`  |
| 3474   | Layout 1 | `ce9a21ac36f1`  |
| 3473   | Layout 1 | `ce9a21ac36f1`  |
| 3464   | Layout 1 | `ce9a21ac36f1`  |
| 3458   | Layout 1 | `ce9a21ac36f1`  |
| 3454   | Layout 1 | `ce9a21ac36f1`  |
| 3444   | Layout 1 | `ce9a21ac36f1`  |
| 3435   | Layout 1 | `ce9a21ac36f1`  |
| 3426   | Layout 1 | `ce9a21ac36f1`  |
| 3418   | Layout 1 | `ce9a21ac36f1`  |
| 3412   | Layout 1 | `ce9a21ac36f1`  |
| 3402   | Layout 1 | `ce9a21ac36f1`  |
| 3396   | Layout 1 | `ce9a21ac36f1`  |
| 3387   | Layout 1 | `ce9a21ac36f1`  |
| 3381   | Layout 1 | `ce9a21ac36f1`  |
| 3373   | Layout 1 | `ce9a21ac36f1`  |
| 3364   | Layout 1 | `ce9a21ac36f1`  |
| 3356   | Layout 1 | `ce9a21ac36f1`  |
| 3349   | Layout 1 | `ce9a21ac36f1`  |
| 3342   | Layout 1 | `ce9a21ac36f1`  |
| 3335   | Layout 1 | `ce9a21ac36f1`  |
| 3326   | Layout 1 | `ce9a21ac36f1`  |
| 3321   | Layout 1 | `ce9a21ac36f1`  |
| 3314   | Layout 1 | `ce9a21ac36f1`  |
| 3303   | Layout 1 | `ce9a21ac36f1`  |
| 3302   | Layout 1 | `ce9a21ac36f1`  |
| 3293   | Layout 1 | `ce9a21ac36f1`  |
| 3283   | Layout 1 | `ce9a21ac36f1`  |
| 3275   | Layout 1 | `ce9a21ac36f1`  |
| 3267   | Layout 1 | `ce9a21ac36f1`  |
| 3258   | Layout 1 | `ce9a21ac36f1`  |
| 3251   | Layout 1 | `ce9a21ac36f1`  |
| 3242   | Layout 1 | `ce9a21ac36f1`  |
| 3235   | Layout 1 | `ce9a21ac36f1`  |
| 3229   | Layout 1 | `ce9a21ac36f1`  |
| 3212   | Layout 1 | `ce9a21ac36f1`  |
| 3203   | Layout 1 | `ce9a21ac36f1`  |
| 3193   | Layout 1 | `ce9a21ac36f1`  |
| 3186   | Layout 1 | `ce9a21ac36f1`  |
| 3177   | Layout 1 | `ce9a21ac36f1`  |
| 3169   | Layout 1 | `ce9a21ac36f1`  |
| 3158   | Layout 1 | `ce9a21ac36f1`  |
| 3151   | Layout 1 | `ce9a21ac36f1`  |
| 3144   | Layout 1 | `ce9a21ac36f1`  |
| 3133   | Layout 1 | `ce9a21ac36f1`  |
| 3125   | Layout 1 | `ce9a21ac36f1`  |
| 3118   | Layout 1 | `ce9a21ac36f1`  |
| 3111   | Layout 1 | `ce9a21ac36f1`  |
| 3103   | Layout 1 | `ce9a21ac36f1`  |
| 3095   | Layout 1 | `ce9a21ac36f1`  |
| 3086   | Layout 1 | `ce9a21ac36f1`  |
| 3072   | Layout 1 | `ce9a21ac36f1`  |
| 3062   | Layout 1 | `ce9a21ac36f1`  |
| 3052   | Layout 1 | `ce9a21ac36f1`  |
| 3045   | Layout 1 | `ce9a21ac36f1`  |
| 3037   | Layout 1 | `ce9a21ac36f1`  |
| 3030   | Layout 1 | `ce9a21ac36f1`  |
| 3021   | Layout 1 | `ce9a21ac36f1`  |
| 3012   | Layout 1 | `ce9a21ac36f1`  |
| 3002   | Layout 1 | `ce9a21ac36f1`  |
| 2995   | Layout 1 | `ce9a21ac36f1`  |
| 2987   | Layout 1 | `ce9a21ac36f1`  |
| 2978   | Layout 1 | `ce9a21ac36f1`  |
| 2970   | Layout 1 | `ce9a21ac36f1`  |
| 2959   | Layout 1 | `ce9a21ac36f1`  |
| 2951   | Layout 1 | `ce9a21ac36f1`  |
| 2942   | Layout 1 | `ce9a21ac36f1`  |
| 2935   | Layout 1 | `ce9a21ac36f1`  |
| 2932   | Layout 1 | `ce9a21ac36f1`  |
| 2923   | Layout 1 | `ce9a21ac36f1`  |
| 2919   | Layout 1 | `ce9a21ac36f1`  |
| 2907   | Layout 1 | `ce9a21ac36f1`  |
| 2900   | Layout 1 | `ce9a21ac36f1`  |
| 2891   | Layout 1 | `ce9a21ac36f1`  |
| 2882   | Layout 1 | `ce9a21ac36f1`  |
| 2872   | Layout 1 | `ce9a21ac36f1`  |
| 2863   | Layout 1 | `ce9a21ac36f1`  |
| 2855   | Layout 1 | `ce9a21ac36f1`  |
| 2849   | Layout 1 | `ce9a21ac36f1`  |
| 2844   | Layout 1 | `ce9a21ac36f1`  |
| 2834   | Layout 1 | `ce9a21ac36f1`  |
| 2825   | Layout 1 | `ce9a21ac36f1`  |
| 2819   | Layout 1 | `ce9a21ac36f1`  |
| 2811   | Layout 1 | `ce9a21ac36f1`  |
| 2803   | Layout 1 | `ce9a21ac36f1`  |
| 2794   | Layout 1 | `ce9a21ac36f1`  |
| 2783   | Layout 1 | `ce9a21ac36f1`  |
| 2774   | Layout 1 | `ce9a21ac36f1`  |
| 2765   | Layout 1 | `ce9a21ac36f1`  |
| 2756   | Layout 1 | `ce9a21ac36f1`  |
| 2750   | Layout 1 | `ce9a21ac36f1`  |
| 2743   | Layout 1 | `ce9a21ac36f1`  |
| 2736   | Layout 1 | `ce9a21ac36f1`  |
| 2726   | Layout 1 | `ce9a21ac36f1`  |
| 2717   | Layout 1 | `ce9a21ac36f1`  |
| 2709   | Layout 1 | `ce9a21ac36f1`  |
| 2703   | Layout 1 | `ce9a21ac36f1`  |
| 2695   | Layout 1 | `ce9a21ac36f1`  |
| 2684   | Layout 1 | `ce9a21ac36f1`  |
| 2672   | Layout 1 | `ce9a21ac36f1`  |
| 2665   | Layout 1 | `ce9a21ac36f1`  |
| 2657   | Layout 1 | `ce9a21ac36f1`  |
| 2649   | Layout 1 | `ce9a21ac36f1`  |
| 2644   | Layout 1 | `ce9a21ac36f1`  |
| 2637   | Layout 1 | `ce9a21ac36f1`  |
| 2629   | Layout 1 | `ce9a21ac36f1`  |
| 2619   | Layout 1 | `ce9a21ac36f1`  |
| 2612   | Layout 1 | `ce9a21ac36f1`  |
| 2606   | Layout 1 | `ce9a21ac36f1`  |
| 2602   | Layout 1 | `ce9a21ac36f1`  |
| 2601   | Layout 1 | `ce9a21ac36f1`  |
| 2592   | Layout 1 | `ce9a21ac36f1`  |
| 2583   | Layout 1 | `ce9a21ac36f1`  |
| 2575   | Layout 1 | `ce9a21ac36f1`  |
| 2567   | Layout 1 | `ce9a21ac36f1`  |
| 2560   | Layout 1 | `ce9a21ac36f1`  |
| 2553   | Layout 1 | `ce9a21ac36f1`  |
| 2545   | Layout 1 | `ce9a21ac36f1`  |
| 2538   | Layout 1 | `ce9a21ac36f1`  |
| 2529   | Layout 1 | `ce9a21ac36f1`  |
| 2519   | Layout 1 | `ce9a21ac36f1`  |
| 2513   | Layout 1 | `ce9a21ac36f1`  |
| 2510   | Layout 1 | `ce9a21ac36f1`  |
| 2507   | Layout 1 | `ce9a21ac36f1`  |
| 2503   | Layout 1 | `ce9a21ac36f1`  |
| 2498   | Layout 1 | `ce9a21ac36f1`  |
| 2492   | Layout 1 | `ce9a21ac36f1`  |
| 2487   | Layout 1 | `ce9a21ac36f1`  |
| 2480   | Layout 1 | `ce9a21ac36f1`  |
| 2474   | Layout 1 | `ce9a21ac36f1`  |
| 2468   | Layout 1 | `ce9a21ac36f1`  |
| 2460   | Layout 1 | `ce9a21ac36f1`  |
| 2453   | Layout 1 | `ce9a21ac36f1`  |
| 2444   | Layout 1 | `ce9a21ac36f1`  |
| 2438   | Layout 1 | `ce9a21ac36f1`  |
| 2434   | Layout 1 | `ce9a21ac36f1`  |
| 2429   | Layout 1 | `ce9a21ac36f1`  |
| 2421   | Layout 1 | `ce9a21ac36f1`  |
| 2414   | Layout 1 | `ce9a21ac36f1`  |
| 2407   | Layout 1 | `ce9a21ac36f1`  |
| 2401   | Layout 1 | `ce9a21ac36f1`  |
| 2397   | Layout 1 | `ce9a21ac36f1`  |
| 2393   | Layout 1 | `ce9a21ac36f1`  |
| 2384   | Layout 1 | `ce9a21ac36f1`  |
| 2378   | Layout 1 | `ce9a21ac36f1`  |
| 2372   | Layout 1 | `ce9a21ac36f1`  |
| 2358   | Layout 1 | `ce9a21ac36f1`  |
| 2352   | Layout 1 | `ce9a21ac36f1`  |
| 2347   | Layout 1 | `ce9a21ac36f1`  |
| 2343   | Layout 1 | `ce9a21ac36f1`  |
| 2335   | Layout 1 | `ce9a21ac36f1`  |
| 2327   | Layout 1 | `ce9a21ac36f1`  |
| 2324   | Layout 1 | `ce9a21ac36f1`  |
| 2319   | Layout 1 | `ce9a21ac36f1`  |
| 2313   | Layout 1 | `ce9a21ac36f1`  |
| 2308   | Layout 1 | `ce9a21ac36f1`  |
| 2302   | Layout 1 | `ce9a21ac36f1`  |
| 2295   | Layout 1 | `ce9a21ac36f1`  |
| 2290   | Layout 1 | `ce9a21ac36f1`  |
| 2284   | Layout 1 | `ce9a21ac36f1`  |
| 2276   | Layout 1 | `ce9a21ac36f1`  |
| 2269   | Layout 1 | `ce9a21ac36f1`  |
| 2259   | Layout 1 | `ce9a21ac36f1`  |
| 2250   | Layout 1 | `ce9a21ac36f1`  |
| 2243   | Layout 1 | `ce9a21ac36f1`  |
| 2235   | Layout 1 | `ce9a21ac36f1`  |
| 2229   | Layout 1 | `ce9a21ac36f1`  |
| 2224   | Layout 1 | `ce9a21ac36f1`  |
| 2218   | Layout 1 | `ce9a21ac36f1`  |
| 2215   | Layout 1 | `ce9a21ac36f1`  |
| 2207   | Layout 1 | `ce9a21ac36f1`  |
| 2203   | Layout 1 | `ce9a21ac36f1`  |
| 2196   | Layout 1 | `ce9a21ac36f1`  |
| 2192   | Layout 1 | `ce9a21ac36f1`  |
| 2189   | Layout 1 | `ce9a21ac36f1`  |
| 2183   | Layout 1 | `ce9a21ac36f1`  |
| 2179   | Layout 1 | `ce9a21ac36f1`  |
| 2171   | Layout 1 | `ce9a21ac36f1`  |
| 2163   | Layout 1 | `ce9a21ac36f1`  |
| 2156   | Layout 1 | `ce9a21ac36f1`  |
| 2151   | Layout 1 | `ce9a21ac36f1`  |
| 2147   | Layout 1 | `ce9a21ac36f1`  |
| 2142   | Layout 1 | `ce9a21ac36f1`  |
| 2138   | Layout 1 | `ce9a21ac36f1`  |
| 2134   | Layout 1 | `ce9a21ac36f1`  |
| 2130   | Layout 1 | `ce9a21ac36f1`  |
| 2122   | Layout 1 | `ce9a21ac36f1`  |
| 2107   | Layout 1 | `ce9a21ac36f1`  |
| 2098   | Layout 1 | `ce9a21ac36f1`  |
| 2089   | Layout 1 | `ce9a21ac36f1`  |
| 2081   | Layout 1 | `ce9a21ac36f1`  |
| 2073   | Layout 1 | `ce9a21ac36f1`  |
| 2067   | Layout 1 | `ce9a21ac36f1`  |
| 2063   | Layout 1 | `ce9a21ac36f1`  |
| 2059   | Layout 1 | `ce9a21ac36f1`  |
| 2052   | Layout 1 | `ce9a21ac36f1`  |
| 2044   | Layout 1 | `ce9a21ac36f1`  |
| 2039   | Layout 1 | `ce9a21ac36f1`  |
| 2032   | Layout 1 | `ce9a21ac36f1`  |
| 2025   | Layout 1 | `ce9a21ac36f1`  |
| 2011   | Layout 1 | `ce9a21ac36f1`  |
| 2005   | Layout 1 | `ce9a21ac36f1`  |
| 2000   | Layout 1 | `ce9a21ac36f1`  |
| 1996   | Layout 1 | `ce9a21ac36f1`  |
| 1991   | Layout 1 | `ce9a21ac36f1`  |
| 1985   | Layout 1 | `ce9a21ac36f1`  |
| 1980   | Layout 1 | `ce9a21ac36f1`  |
| 1969   | Layout 1 | `ce9a21ac36f1`  |
| 1964   | Layout 1 | `ce9a21ac36f1`  |
| 1958   | Layout 1 | `ce9a21ac36f1`  |
| 1950   | Layout 1 | `ce9a21ac36f1`  |
| 1945   | Layout 1 | `ce9a21ac36f1`  |
| 1937   | Layout 1 | `ce9a21ac36f1`  |
| 1933   | Layout 1 | `ce9a21ac36f1`  |
| 1927   | Layout 1 | `ce9a21ac36f1`  |
| 1921   | Layout 1 | `ce9a21ac36f1`  |
| 1914   | Layout 1 | `ce9a21ac36f1`  |
| 1908   | Layout 1 | `ce9a21ac36f1`  |
| 1897   | Layout 1 | `ce9a21ac36f1`  |
| 1892   | Layout 1 | `ce9a21ac36f1`  |
| 1886   | Layout 1 | `ce9a21ac36f1`  |
| 1881   | Layout 1 | `ce9a21ac36f1`  |
| 1871   | Layout 1 | `ce9a21ac36f1`  |
| 1866   | Layout 1 | `ce9a21ac36f1`  |
| 1862   | Layout 1 | `ce9a21ac36f1`  |
| 1854   | Layout 1 | `ce9a21ac36f1`  |
| 1846   | Layout 1 | `ce9a21ac36f1`  |
| 1838   | Layout 1 | `ce9a21ac36f1`  |
| 1832   | Layout 1 | `ce9a21ac36f1`  |
| 1826   | Layout 1 | `ce9a21ac36f1`  |
| 1822   | Layout 1 | `ce9a21ac36f1`  |
| 1818   | Layout 1 | `ce9a21ac36f1`  |
| 1804   | Layout 1 | `ce9a21ac36f1`  |
| 1794   | Layout 1 | `ce9a21ac36f1`  |
| 1790   | Layout 1 | `ce9a21ac36f1`  |
| 1784   | Layout 1 | `ce9a21ac36f1`  |
| 1774   | No file  | `ce9a21ac36f1`  |
| 1771   | No file  | `ce9a21ac36f1`  |
| 1762   | No file  | `ce9a21ac36f1`  |
| 1759   | No file  | `ce9a21ac36f1`  |
| 1754   | No file  | `ce9a21ac36f1`  |
| 1749   | No file  | `ce9a21ac36f1`  |
| 1743   | No file  | `ce9a21ac36f1`  |
| 1737   | No file  | `ce9a21ac36f1`  |
| 1731   | No file  | `ce9a21ac36f1`  |
| 1725   | No file  | `ce9a21ac36f1`  |
| 1717   | No file  | `ce9a21ac36f1`  |
| 1710   | No file  | `ce9a21ac36f1`  |
| 1704   | No file  | `ce9a21ac36f1`  |
| 1698   | No file  | `ce9a21ac36f1`  |
| 1690   | No file  | `ce9a21ac36f1`  |
| 1685   | No file  | `ce9a21ac36f1`  |
| 1680   | No file  | `ce9a21ac36f1`  |
| 1674   | No file  | `ce9a21ac36f1`  |
| 1668   | No file  | `ce9a21ac36f1`  |
| 1659   | No file  | `ce9a21ac36f1`  |
| 1649   | No file  | `ce9a21ac36f1`  |
| 1642   | No file  | `ce9a21ac36f1`  |
| 1636   | No file  | `ce9a21ac36f1`  |
| 1628   | No file  | `ce9a21ac36f1`  |
| 1622   | No file  | `ce9a21ac36f1`  |
| 1614   | No file  | `ce9a21ac36f1`  |
| 1608   | No file  | `ce9a21ac36f1`  |
| 1602   | No file  | `ce9a21ac36f1`  |
| 1598   | No file  | `ce9a21ac36f1`  |
| 1594   | No file  | `ce9a21ac36f1`  |
| 1590   | No file  | `ce9a21ac36f1`  |
| 1587   | No file  | `ce9a21ac36f1`  |
| 1584   | No file  | `ce9a21ac36f1`  |
| 1579   | No file  | `ce9a21ac36f1`  |
| 1572   | No file  | `ce9a21ac36f1`  |
| 1565   | No file  | `ce9a21ac36f1`  |
| 1559   | No file  | `ce9a21ac36f1`  |
| 1554   | No file  | `ce9a21ac36f1`  |
| 1547   | No file  | `ce9a21ac36f1`  |
| 1537   | No file  | `ce9a21ac36f1`  |
| 1529   | No file  | `ce9a21ac36f1`  |
| 1524   | No file  | `ce9a21ac36f1`  |
| 1519   | No file  | `ce9a21ac36f1`  |
| 1509   | No file  | `ce9a21ac36f1`  |
| 1506   | No file  | `ce9a21ac36f1`  |
| 1504   | No file  | `ce9a21ac36f1`  |
| 1500   | No file  | `ce9a21ac36f1`  |
| 1493   | No file  | `ce9a21ac36f1`  |
| 1489   | No file  | `ce9a21ac36f1`  |
| 1485   | No file  | `ce9a21ac36f1`  |
| 1481   | No file  | `ce9a21ac36f1`  |
| 1474   | No file  | `ce9a21ac36f1`  |
| 1466   | No file  | `ce9a21ac36f1`  |
| 1462   | No file  | `ce9a21ac36f1`  |
| 1459   | No file  | `ce9a21ac36f1`  |
| 1453   | No file  | `ce9a21ac36f1`  |
| 1450   | No file  | `ce9a21ac36f1`  |
| 1445   | No file  | `ce9a21ac36f1`  |
| 1439   | No file  | `ce9a21ac36f1`  |
| 1433   | No file  | `ce9a21ac36f1`  |
| 1430   | No file  | `ce9a21ac36f1`  |
| 1426   | No file  | `ce9a21ac36f1`  |
| 1421   | No file  | `ce9a21ac36f1`  |
| 1417   | No file  | `ce9a21ac36f1`  |
| 1416   | No file  | `ce9a21ac36f1`  |
| 1409   | No file  | `ce9a21ac36f1`  |
| 1405   | No file  | `ce9a21ac36f1`  |
| 1401   | No file  | `ce9a21ac36f1`  |
| 1396   | No file  | `ce9a21ac36f1`  |
| 1391   | No file  | `ce9a21ac36f1`  |
| 1390   | No file  | `ce9a21ac36f1`  |
| 1386   | No file  | `ce9a21ac36f1`  |
| 1381   | No file  | `ce9a21ac36f1`  |
| 1379   | No file  | `ce9a21ac36f1`  |
| 1372   | No file  | `ce9a21ac36f1`  |
| 1366   | No file  | `ce9a21ac36f1`  |
| 1364   | No file  | `ce9a21ac36f1`  |
| 1363   | No file  | `ce9a21ac36f1`  |
| 1360   | No file  | `ce9a21ac36f1`  |
| 1358   | No file  | `ce9a21ac36f1`  |
| 1355   | No file  | `ce9a21ac36f1`  |
| 1351   | No file  | `ce9a21ac36f1`  |
| 1348   | No file  | `ce9a21ac36f1`  |
| 1346   | No file  | `ce9a21ac36f1`  |
| 1341   | No file  | `ce9a21ac36f1`  |
| 1340   | No file  | `ce9a21ac36f1`  |
| 1338   | No file  | `ce9a21ac36f1`  |
| 1335   | No file  | `ce9a21ac36f1`  |
| 1333   | No file  | `ce9a21ac36f1`  |
| 1329   | No file  | `ce9a21ac36f1`  |
| 1327   | No file  | `ce9a21ac36f1`  |
| 1324   | No file  | `ce9a21ac36f1`  |
| 1321   | No file  | `ce9a21ac36f1`  |
| 1319   | No file  | `ce9a21ac36f1`  |
| 1318   | No file  | `ce9a21ac36f1`  |
| 1316   | No file  | `ce9a21ac36f1`  |
| 1313   | No file  | `ce9a21ac36f1`  |
| 1311   | No file  | `ce9a21ac36f1`  |
| 1309   | No file  | `ce9a21ac36f1`  |
| 1304   | No file  | `ce9a21ac36f1`  |
| 1292   | No file  | `ce9a21ac36f1`  |
| 1286   | No file  | `ce9a21ac36f1`  |
| 1280   | No file  | `ce9a21ac36f1`  |
| 1276   | No file  | `ce9a21ac36f1`  |
| 1267   | No file  | `ce9a21ac36f1`  |
| 1261   | No file  | `ce9a21ac36f1`  |
| 1256   | No file  | `ce9a21ac36f1`  |
| 1250   | No file  | `ce9a21ac36f1`  |
| 1246   | No file  | `ce9a21ac36f1`  |
| 1239   | No file  | `ce9a21ac36f1`  |
| 1230   | No file  | `ce9a21ac36f1`  |
| 1226   | No file  | `ce9a21ac36f1`  |
| 1220   | No file  | `ce9a21ac36f1`  |
| 1217   | No file  | `ce9a21ac36f1`  |
| 1211   | No file  | `ce9a21ac36f1`  |
| 1210   | No file  | `ce9a21ac36f1`  |
| 1208   | No file  | `ce9a21ac36f1`  |
| 1203   | No file  | `ce9a21ac36f1`  |
| 1197   | No file  | `ce9a21ac36f1`  |
| 1194   | No file  | `ce9a21ac36f1`  |
| 1192   | No file  | `ce9a21ac36f1`  |
| 1187   | No file  | `ce9a21ac36f1`  |
| 1183   | No file  | `ce9a21ac36f1`  |
| 1177   | No file  | `ce9a21ac36f1`  |
| 1173   | No file  | `ce9a21ac36f1`  |
| 1167   | No file  | `ce9a21ac36f1`  |
| 1164   | No file  | `ce9a21ac36f1`  |
| 1156   | No file  | `ce9a21ac36f1`  |
| 1149   | No file  | `ce9a21ac36f1`  |
| 1144   | No file  | `ce9a21ac36f1`  |
| 1137   | No file  | `ce9a21ac36f1`  |
| 1132   | No file  | `ce9a21ac36f1`  |
| 1127   | No file  | `ce9a21ac36f1`  |
| 1122   | No file  | `ce9a21ac36f1`  |
| 1118   | No file  | `ce9a21ac36f1`  |
| 1114   | No file  | `ce9a21ac36f1`  |
| 1109   | No file  | `ce9a21ac36f1`  |
| 1102   | No file  | `ce9a21ac36f1`  |
| 1096   | No file  | `ce9a21ac36f1`  |
| 1088   | No file  | `ce9a21ac36f1`  |
| 1081   | No file  | `ce9a21ac36f1`  |
| 1076   | No file  | `ce9a21ac36f1`  |
| 1069   | No file  | `ce9a21ac36f1`  |
| 1064   | No file  | `ce9a21ac36f1`  |
| 1058   | No file  | `ce9a21ac36f1`  |
| 1051   | No file  | `ce9a21ac36f1`  |
| 1044   | No file  | `ce9a21ac36f1`  |
| 1036   | No file  | `ce9a21ac36f1`  |
| 1026   | No file  | `ce9a21ac36f1`  |
| 1016   | No file  | `ce9a21ac36f1`  |
| 1009   | No file  | `ce9a21ac36f1`  |
| 1005   | No file  | `ce9a21ac36f1`  |
| 1000   | No file  | `ce9a21ac36f1`  |
| 998    | No file  | `ce9a21ac36f1`  |
| 990    | No file  | `ce9a21ac36f1`  |
| 979    | No file  | `ce9a21ac36f1`  |
| 972    | No file  | `ce9a21ac36f1`  |
| 963    | No file  | `ce9a21ac36f1`  |
| 955    | No file  | `ce9a21ac36f1`  |
| 946    | No file  | `ce9a21ac36f1`  |
| 938    | No file  | `ce9a21ac36f1`  |
| 927    | No file  | `ce9a21ac36f1`  |
| 911    | No file  | `ce9a21ac36f1`  |
| 904    | No file  | `ce9a21ac36f1`  |
| 899    | No file  | `ce9a21ac36f1`  |
| 894    | No file  | `ce9a21ac36f1`  |
| 885    | No file  | `ce9a21ac36f1`  |
| 879    | No file  | `ce9a21ac36f1`  |
| 872    | No file  | `ce9a21ac36f1`  |
| 864    | No file  | `ce9a21ac36f1`  |
| 855    | No file  | `ce9a21ac36f1`  |
| 853    | No file  | `ce9a21ac36f1`  |
| 845    | No file  | `ce9a21ac36f1`  |
| 837    | No file  | `ce9a21ac36f1`  |
| 829    | No file  | `ce9a21ac36f1`  |
| 822    | No file  | `ce9a21ac36f1`  |
| 814    | No file  | `ce9a21ac36f1`  |
| 805    | No file  | `ce9a21ac36f1`  |
| 794    | No file  | `ce9a21ac36f1`  |
| 787    | No file  | `ce9a21ac36f1`  |
| 780    | No file  | `ce9a21ac36f1`  |
| 771    | No file  | `ce9a21ac36f1`  |
| 760    | No file  | `ce9a21ac36f1`  |
| 748    | No file  | `ce9a21ac36f1`  |
| 741    | No file  | `ce9a21ac36f1`  |
| 736    | No file  | `ce9a21ac36f1`  |
| 731    | No file  | `ce9a21ac36f1`  |
| 723    | No file  | `ce9a21ac36f1`  |
| 711    | No file  | `ce9a21ac36f1`  |
| 707    | No file  | `ce9a21ac36f1`  |
| 697    | No file  | `ce9a21ac36f1`  |
| 689    | No file  | `ce9a21ac36f1`  |
| 683    | No file  | `ce9a21ac36f1`  |
| 678    | No file  | `ce9a21ac36f1`  |
| 670    | No file  | `ce9a21ac36f1`  |
| 661    | No file  | `ce9a21ac36f1`  |
| 656    | No file  | `ce9a21ac36f1`  |
| 652    | No file  | `ce9a21ac36f1`  |
| 643    | No file  | `ce9a21ac36f1`  |
| 637    | No file  | `ce9a21ac36f1`  |
| 630    | No file  | `ce9a21ac36f1`  |
| 627    | No file  | `ce9a21ac36f1`  |
| 621    | No file  | `ce9a21ac36f1`  |
| 617    | No file  | `ce9a21ac36f1`  |
| 615    | No file  | `ce9a21ac36f1`  |
| 606    | No file  | `ce9a21ac36f1`  |
| 599    | No file  | `ce9a21ac36f1`  |
| 592    | No file  | `ce9a21ac36f1`  |
| 586    | No file  | `ce9a21ac36f1`  |
| 577    | No file  | `ce9a21ac36f1`  |
| 569    | No file  | `ce9a21ac36f1`  |
| 561    | No file  | `ce9a21ac36f1`  |
| 554    | No file  | `ce9a21ac36f1`  |
| 542    | No file  | `ce9a21ac36f1`  |
| 532    | No file  | `ce9a21ac36f1`  |
| 531    | No file  | `ce9a21ac36f1`  |
| 526    | No file  | `ce9a21ac36f1`  |
| 521    | No file  | `ce9a21ac36f1`  |
| 517    | No file  | `ce9a21ac36f1`  |
| 510    | No file  | `ce9a21ac36f1`  |
| 508    | No file  | `ce9a21ac36f1`  |
| 504    | No file  | `ce9a21ac36f1`  |
| 497    | No file  | `ce9a21ac36f1`  |
| 491    | No file  | `ce9a21ac36f1`  |
| 485    | No file  | `ce9a21ac36f1`  |
| 478    | No file  | `ce9a21ac36f1`  |
| 472    | No file  | `ce9a21ac36f1`  |
| 466    | No file  | `ce9a21ac36f1`  |
| 457    | No file  | `ce9a21ac36f1`  |
| 452    | No file  | `ce9a21ac36f1`  |
| 449    | No file  | `ce9a21ac36f1`  |
| 435    | No file  | `ce9a21ac36f1`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                              |
| --------------------- | -------- | --------------------------------- |
| `languagedata_en.loc` | Optional | Region names, LOC type 17         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset          | Type               | Field        | Notes                                                |
| --------------- | ------------------ | ------------ | ---------------------------------------------------- |
| `+0x00`         | char[4]            | magic        | ASCII `PABR`                                         |
| `+0x04`         | Row[..table_start] | rows         | See Row                                              |
| `rows+0x00`     | String Table       | string_table | See String Table                                     |
| `EOF-0x08`      | u32                | table_start  | Offset of the string table, where `rows` ends        |
| `EOF-0x04`      | u32                | zero         | Always `0`                                           |

The parser takes the row count from the trailer: `(table_start - 4) / 4`.

### Row (4 bytes)

| Offset  | Type | Field                 | Notes                                                                 |
| ------- | ---- | --------------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | region_key            | `regioninfo.bss` region key; the handler shows its LOC type 17 name    |
| `+0x02` | u16  | mini_game_group_index | Mini-game group the region uses                                        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names follow the `IceFishing_Region` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_minigame_2.xlsm`. The sheet has the columns `MiniGameRegionGroup`
and `MiniGameGroupIndex` and one row, `326` and `1`, with the note
`2021년 크리스마스 고요한 샘` (2021 Christmas, Serene Spring). The client 1784
archive's file holds that row: `46 01 01 00`, u16 `326` and u16 `1` (1 of 1
rows). Region `326` is Serene Spring in `regioninfo.bss` and in LOC type 17,
so `MiniGameRegionGroup` holds a region key and the field is `region_key`.

Rows on the clients checked, `region_key` / `mini_game_group_index`, with
the LOC type 17 names of client 3474:

| Client | Rows                              |
| ------ | --------------------------------- |
| 1784   | `326` / `1`                       |
| 2107   | `1191` / `1`                      |
| 2519   | `1191` / `1`                      |
| 3002   | `1176` / `1`                      |
| 3251   | `1176` / `1`, `1484` / `2`        |
| 3474   | `1176` / `1`, `1484` / `2`        |

`326` and `1191` are both Serene Spring, `1176` Snowfall Crasher: Alpine
Glide and `1484` Gyeonghoeru Pavilion.

The same sheet file holds the `IceFishing` sheet, whose first column is
`MiniGameGroup` (`1` on client 1784) followed by the mini-game timings, HP
and rewards. Its compiled file is
[`icefisingstaticstatus.bss`](icefisingstaticstatus_bss.md), whose header
count is `1` on client 1784 and `2` on client 3474, one per group above.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 98 04 01 00 CC 05 02 00 00 00 00 00 0C 00 00 00 00 00 00 00`.
- The server dump of the private server on client 1784 has a loader for
  `IceFishing_Region` that reads `MiniGameRegionGroup` as a number and
  `MiniGameGroupIndex` through the text reader, and an
  `IceFishingStaticStatusManager` that names `MinigameGroup` in its error
  messages.
- The client Lua opens the mini-game through `Panel_MiniGame_IceFishing_All`
  behind `_ContentsGroup_IceFishingGame`; it reads no region list.
- `icefising` is the client's spelling.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`.
