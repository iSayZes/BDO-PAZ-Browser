# `houseinforeceipe.dbss` Format

## Purpose

The house uses ("receipes" in the client) a node house can be set to:
Residence, Lodging, Storage, Horse Ranch, the workshops, the processing and
packing workshops, the Shipyard and the Guild Storage levels. A row is the
receipe key, its Korean name, the house use type and icon type the client
enums name, the `houseinfoneeditem.dbss` group that prices each level, and
the item exchange recipes the house unlocks at each level.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes  | Records                 | Row bytes               |
| ------ | -------------- | ----------------------------- | ------ | ----------------------- | ----------------------- |
| 2      | 2726 and later | `houseinforeceipe.dbss`       | 26,166 | 660 Level List, 132 Row | 4 to 376, 31 on average |
| 2      | 2726 and later | `houseinforeceipeoffset.dbss` | 1,588  | 132 Index Row           | 12                      |
| 1      | 1304 to 2138   | `houseinforeceipe.dbss`       | 12,533 | 515 Level List, 103 Row | 4 to 156, 18 on average |
| 1      | 1304 to 2138   | `houseinforeceipeoffset.dbss` | 1,240  | 103 Index Row           | 12                      |

| Layout | File                          | Known            | Unknown        |
| ------ | ----------------------------- | ---------------- | -------------- |
| 2      | `houseinforeceipe.dbss`       | 24,232 B (92.6%) | 1,934 B (7.4%) |
| 2      | `houseinforeceipeoffset.dbss` | 1,588 B (100.0%) | 0 B (0.0%)     |
| 1      | `houseinforeceipe.dbss`       | 12,121 B (96.7%) | 412 B (3.3%)   |
| 1      | `houseinforeceipeoffset.dbss` | 1,240 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `0081f71f5209`  |
| 3482   | Layout 2             | `0081f71f5209`  |
| 3474   | Layout 2             | `0081f71f5209`  |
| 3473   | Layout 2             | `0081f71f5209`  |
| 3464   | Layout 2             | `0081f71f5209`  |
| 3458   | Layout 2             | `0081f71f5209`  |
| 3454   | Layout 2             | `0081f71f5209`  |
| 3444   | Layout 2             | `0081f71f5209`  |
| 3435   | Layout 2             | `0081f71f5209`  |
| 3426   | Layout 2             | `0081f71f5209`  |
| 3418   | Layout 2             | `0081f71f5209`  |
| 3412   | Layout 2             | `0081f71f5209`  |
| 3402   | Layout 2             | `0081f71f5209`  |
| 3396   | Layout 2             | `0081f71f5209`  |
| 3387   | Layout 2             | `0081f71f5209`  |
| 3381   | Layout 2             | `0081f71f5209`  |
| 3373   | Layout 2             | `0081f71f5209`  |
| 3364   | Layout 2             | `0081f71f5209`  |
| 3356   | Layout 2             | `0081f71f5209`  |
| 3349   | Layout 2             | `0081f71f5209`  |
| 3342   | Layout 2             | `0081f71f5209`  |
| 3335   | Layout 2             | `0081f71f5209`  |
| 3326   | Layout 2             | `0081f71f5209`  |
| 3321   | Layout 2             | `0081f71f5209`  |
| 3314   | Layout 2             | `0081f71f5209`  |
| 3303   | Layout 2             | `0081f71f5209`  |
| 3302   | Layout 2             | `0081f71f5209`  |
| 3293   | Layout 2             | `0081f71f5209`  |
| 3283   | Layout 2             | `0081f71f5209`  |
| 3275   | Layout 2             | `0081f71f5209`  |
| 3267   | Layout 2             | `0081f71f5209`  |
| 3258   | Layout 2             | `0081f71f5209`  |
| 3251   | Layout 2             | `0081f71f5209`  |
| 3242   | Layout 2             | `0081f71f5209`  |
| 3235   | Layout 2             | `0081f71f5209`  |
| 3229   | Layout 2             | `0081f71f5209`  |
| 3212   | Layout 2             | `0081f71f5209`  |
| 3203   | Layout 2             | `0081f71f5209`  |
| 3193   | Layout 2             | `0081f71f5209`  |
| 3186   | Layout 2             | `0081f71f5209`  |
| 3177   | Layout 2             | `0081f71f5209`  |
| 3169   | Layout 2             | `0081f71f5209`  |
| 3158   | Layout 2             | `0081f71f5209`  |
| 3151   | Layout 2             | `0081f71f5209`  |
| 3144   | Layout 2             | `0081f71f5209`  |
| 3133   | Layout 2             | `0081f71f5209`  |
| 3125   | Layout 2             | `0081f71f5209`  |
| 3118   | Layout 2             | `0081f71f5209`  |
| 3111   | Layout 2             | `0081f71f5209`  |
| 3103   | Layout 2             | `0081f71f5209`  |
| 3095   | Layout 2             | `0081f71f5209`  |
| 3086   | Layout 2             | `0081f71f5209`  |
| 3072   | Layout 2             | `0081f71f5209`  |
| 3062   | Layout 2             | `0081f71f5209`  |
| 3052   | Layout 2             | `0081f71f5209`  |
| 3045   | Layout 2             | `0081f71f5209`  |
| 3037   | Layout 2             | `0081f71f5209`  |
| 3030   | Layout 2             | `0081f71f5209`  |
| 3021   | Layout 2             | `0081f71f5209`  |
| 3012   | Layout 2             | `0081f71f5209`  |
| 3002   | Layout 2             | `0081f71f5209`  |
| 2995   | Layout 2             | `0081f71f5209`  |
| 2987   | Layout 2             | `0081f71f5209`  |
| 2978   | Layout 2             | `0081f71f5209`  |
| 2970   | Layout 2             | `0081f71f5209`  |
| 2959   | Layout 2             | `0081f71f5209`  |
| 2951   | Layout 2             | `0081f71f5209`  |
| 2942   | Layout 2             | `0081f71f5209`  |
| 2935   | Layout 2             | `0081f71f5209`  |
| 2932   | Layout 2             | `0081f71f5209`  |
| 2923   | Layout 2             | `0081f71f5209`  |
| 2919   | Layout 2             | `0081f71f5209`  |
| 2907   | Layout 2             | `0081f71f5209`  |
| 2900   | Layout 2             | `0081f71f5209`  |
| 2891   | Layout 2             | `0081f71f5209`  |
| 2882   | Layout 2             | `0081f71f5209`  |
| 2872   | Layout 2             | `0081f71f5209`  |
| 2863   | Layout 2             | `0081f71f5209`  |
| 2855   | Layout 2             | `0081f71f5209`  |
| 2849   | Layout 2             | `0081f71f5209`  |
| 2844   | Layout 2             | `0081f71f5209`  |
| 2834   | Layout 2             | `0081f71f5209`  |
| 2825   | Layout 2             | `0081f71f5209`  |
| 2819   | Layout 2             | `0081f71f5209`  |
| 2811   | Layout 2             | `0081f71f5209`  |
| 2803   | Layout 2             | `0081f71f5209`  |
| 2794   | Layout 2             | `0081f71f5209`  |
| 2783   | Layout 2             | `0081f71f5209`  |
| 2774   | Layout 2             | `0081f71f5209`  |
| 2765   | Layout 2             | `0081f71f5209`  |
| 2756   | Layout 2             | `0081f71f5209`  |
| 2750   | Layout 2             | `0081f71f5209`  |
| 2743   | Layout 2             | `0081f71f5209`  |
| 2736   | Layout 2             | `0081f71f5209`  |
| 2726   | Layout 2             | `0081f71f5209`  |
| 2717   | No documented layout | `0081f71f5209`  |
| 2709   | No documented layout | `0081f71f5209`  |
| 2703   | No documented layout | `0081f71f5209`  |
| 2695   | No documented layout | `0081f71f5209`  |
| 2684   | No documented layout | `0081f71f5209`  |
| 2672   | No documented layout | `0081f71f5209`  |
| 2665   | No documented layout | `0081f71f5209`  |
| 2657   | No documented layout | `0081f71f5209`  |
| 2649   | No documented layout | `0081f71f5209`  |
| 2644   | No documented layout | `0081f71f5209`  |
| 2637   | No documented layout | `0081f71f5209`  |
| 2629   | No documented layout | `0081f71f5209`  |
| 2619   | No documented layout | `0081f71f5209`  |
| 2612   | No documented layout | `0081f71f5209`  |
| 2606   | No documented layout | `0081f71f5209`  |
| 2602   | No documented layout | `0081f71f5209`  |
| 2601   | No documented layout | `0081f71f5209`  |
| 2592   | No documented layout | `0081f71f5209`  |
| 2583   | No documented layout | `0081f71f5209`  |
| 2575   | No documented layout | `0081f71f5209`  |
| 2567   | No documented layout | `0081f71f5209`  |
| 2560   | No documented layout | `0081f71f5209`  |
| 2553   | No documented layout | `0081f71f5209`  |
| 2545   | No documented layout | `0081f71f5209`  |
| 2538   | No documented layout | `0081f71f5209`  |
| 2529   | No documented layout | `0081f71f5209`  |
| 2519   | No documented layout | `0081f71f5209`  |
| 2513   | No documented layout | `0081f71f5209`  |
| 2510   | No documented layout | `0081f71f5209`  |
| 2507   | No documented layout | `0081f71f5209`  |
| 2503   | No documented layout | `0081f71f5209`  |
| 2498   | No documented layout | `0081f71f5209`  |
| 2492   | No documented layout | `0081f71f5209`  |
| 2487   | No documented layout | `0081f71f5209`  |
| 2480   | No documented layout | `0081f71f5209`  |
| 2474   | No documented layout | `0081f71f5209`  |
| 2468   | No documented layout | `0081f71f5209`  |
| 2460   | No documented layout | `0081f71f5209`  |
| 2453   | No documented layout | `0081f71f5209`  |
| 2444   | No documented layout | `0081f71f5209`  |
| 2438   | No documented layout | `0081f71f5209`  |
| 2434   | No documented layout | `0081f71f5209`  |
| 2429   | No documented layout | `0081f71f5209`  |
| 2421   | No documented layout | `0081f71f5209`  |
| 2414   | No documented layout | `0081f71f5209`  |
| 2407   | No documented layout | `0081f71f5209`  |
| 2401   | No documented layout | `0081f71f5209`  |
| 2397   | No documented layout | `0081f71f5209`  |
| 2393   | No documented layout | `0081f71f5209`  |
| 2384   | No documented layout | `0081f71f5209`  |
| 2378   | No documented layout | `0081f71f5209`  |
| 2372   | No documented layout | `0081f71f5209`  |
| 2358   | No documented layout | `0081f71f5209`  |
| 2352   | No documented layout | `0081f71f5209`  |
| 2347   | No documented layout | `0081f71f5209`  |
| 2343   | No documented layout | `0081f71f5209`  |
| 2335   | No documented layout | `0081f71f5209`  |
| 2327   | No documented layout | `0081f71f5209`  |
| 2324   | No documented layout | `0081f71f5209`  |
| 2319   | No documented layout | `0081f71f5209`  |
| 2313   | No documented layout | `0081f71f5209`  |
| 2308   | No documented layout | `0081f71f5209`  |
| 2302   | No documented layout | `0081f71f5209`  |
| 2295   | No documented layout | `0081f71f5209`  |
| 2290   | No documented layout | `0081f71f5209`  |
| 2284   | No documented layout | `0081f71f5209`  |
| 2276   | No documented layout | `0081f71f5209`  |
| 2269   | No documented layout | `0081f71f5209`  |
| 2259   | No documented layout | `0081f71f5209`  |
| 2250   | No documented layout | `0081f71f5209`  |
| 2243   | No documented layout | `0081f71f5209`  |
| 2235   | No documented layout | `0081f71f5209`  |
| 2229   | No documented layout | `0081f71f5209`  |
| 2224   | No documented layout | `0081f71f5209`  |
| 2218   | No documented layout | `0081f71f5209`  |
| 2215   | No documented layout | `0081f71f5209`  |
| 2207   | No documented layout | `0081f71f5209`  |
| 2203   | No documented layout | `0081f71f5209`  |
| 2196   | No documented layout | `0081f71f5209`  |
| 2192   | No documented layout | `0081f71f5209`  |
| 2189   | No documented layout | `0081f71f5209`  |
| 2183   | No documented layout | `0081f71f5209`  |
| 2179   | No documented layout | `0081f71f5209`  |
| 2171   | No documented layout | `0081f71f5209`  |
| 2163   | No documented layout | `0081f71f5209`  |
| 2156   | No documented layout | `0081f71f5209`  |
| 2151   | No documented layout | `0081f71f5209`  |
| 2147   | No documented layout | `0081f71f5209`  |
| 2142   | No documented layout | `0081f71f5209`  |
| 2138   | Layout 1             | `0081f71f5209`  |
| 2134   | Layout 1             | `0081f71f5209`  |
| 2130   | Layout 1             | `0081f71f5209`  |
| 2122   | Layout 1             | `0081f71f5209`  |
| 2107   | Layout 1             | `0081f71f5209`  |
| 2098   | Layout 1             | `0081f71f5209`  |
| 2089   | Layout 1             | `0081f71f5209`  |
| 2081   | Layout 1             | `0081f71f5209`  |
| 2073   | Layout 1             | `0081f71f5209`  |
| 2067   | Layout 1             | `0081f71f5209`  |
| 2063   | Layout 1             | `0081f71f5209`  |
| 2059   | Layout 1             | `0081f71f5209`  |
| 2052   | Layout 1             | `0081f71f5209`  |
| 2044   | Layout 1             | `0081f71f5209`  |
| 2039   | Layout 1             | `0081f71f5209`  |
| 2032   | Layout 1             | `0081f71f5209`  |
| 2025   | Layout 1             | `0081f71f5209`  |
| 2011   | Layout 1             | `0081f71f5209`  |
| 2005   | Layout 1             | `0081f71f5209`  |
| 2000   | Layout 1             | `0081f71f5209`  |
| 1996   | Layout 1             | `0081f71f5209`  |
| 1991   | Layout 1             | `0081f71f5209`  |
| 1985   | Layout 1             | `0081f71f5209`  |
| 1980   | Layout 1             | `0081f71f5209`  |
| 1969   | Layout 1             | `0081f71f5209`  |
| 1964   | Layout 1             | `0081f71f5209`  |
| 1958   | Layout 1             | `0081f71f5209`  |
| 1950   | Layout 1             | `0081f71f5209`  |
| 1945   | Layout 1             | `0081f71f5209`  |
| 1937   | Layout 1             | `0081f71f5209`  |
| 1933   | Layout 1             | `0081f71f5209`  |
| 1927   | Layout 1             | `0081f71f5209`  |
| 1921   | Layout 1             | `0081f71f5209`  |
| 1914   | Layout 1             | `0081f71f5209`  |
| 1908   | Layout 1             | `0081f71f5209`  |
| 1897   | Layout 1             | `0081f71f5209`  |
| 1892   | Layout 1             | `0081f71f5209`  |
| 1886   | Layout 1             | `0081f71f5209`  |
| 1881   | Layout 1             | `0081f71f5209`  |
| 1871   | Layout 1             | `0081f71f5209`  |
| 1866   | Layout 1             | `0081f71f5209`  |
| 1862   | Layout 1             | `0081f71f5209`  |
| 1854   | Layout 1             | `0081f71f5209`  |
| 1846   | Layout 1             | `0081f71f5209`  |
| 1838   | Layout 1             | `0081f71f5209`  |
| 1832   | Layout 1             | `0081f71f5209`  |
| 1826   | Layout 1             | `0081f71f5209`  |
| 1822   | Layout 1             | `0081f71f5209`  |
| 1818   | Layout 1             | `0081f71f5209`  |
| 1804   | Layout 1             | `0081f71f5209`  |
| 1794   | Layout 1             | `0081f71f5209`  |
| 1790   | Layout 1             | `0081f71f5209`  |
| 1784   | Layout 1             | `0081f71f5209`  |
| 1774   | Layout 1             | `0081f71f5209`  |
| 1771   | Layout 1             | `0081f71f5209`  |
| 1762   | Layout 1             | `0081f71f5209`  |
| 1759   | Layout 1             | `0081f71f5209`  |
| 1754   | Layout 1             | `0081f71f5209`  |
| 1749   | Layout 1             | `0081f71f5209`  |
| 1743   | Layout 1             | `0081f71f5209`  |
| 1737   | Layout 1             | `0081f71f5209`  |
| 1731   | Layout 1             | `0081f71f5209`  |
| 1725   | Layout 1             | `0081f71f5209`  |
| 1717   | Layout 1             | `0081f71f5209`  |
| 1710   | Layout 1             | `0081f71f5209`  |
| 1704   | Layout 1             | `0081f71f5209`  |
| 1698   | Layout 1             | `0081f71f5209`  |
| 1690   | Layout 1             | `0081f71f5209`  |
| 1685   | Layout 1             | `0081f71f5209`  |
| 1680   | Layout 1             | `0081f71f5209`  |
| 1674   | Layout 1             | `0081f71f5209`  |
| 1668   | Layout 1             | `0081f71f5209`  |
| 1659   | Layout 1             | `0081f71f5209`  |
| 1649   | Layout 1             | `0081f71f5209`  |
| 1642   | Layout 1             | `0081f71f5209`  |
| 1636   | Layout 1             | `0081f71f5209`  |
| 1628   | Layout 1             | `0081f71f5209`  |
| 1622   | Layout 1             | `0081f71f5209`  |
| 1614   | Layout 1             | `0081f71f5209`  |
| 1608   | Layout 1             | `0081f71f5209`  |
| 1602   | Layout 1             | `0081f71f5209`  |
| 1598   | Layout 1             | `0081f71f5209`  |
| 1594   | Layout 1             | `0081f71f5209`  |
| 1590   | Layout 1             | `0081f71f5209`  |
| 1587   | Layout 1             | `0081f71f5209`  |
| 1584   | Layout 1             | `0081f71f5209`  |
| 1579   | Layout 1             | `0081f71f5209`  |
| 1572   | Layout 1             | `0081f71f5209`  |
| 1565   | Layout 1             | `0081f71f5209`  |
| 1559   | Layout 1             | `0081f71f5209`  |
| 1554   | Layout 1             | `0081f71f5209`  |
| 1547   | Layout 1             | `0081f71f5209`  |
| 1537   | Layout 1             | `0081f71f5209`  |
| 1529   | Layout 1             | `0081f71f5209`  |
| 1524   | Layout 1             | `0081f71f5209`  |
| 1519   | Layout 1             | `0081f71f5209`  |
| 1509   | Layout 1             | `0081f71f5209`  |
| 1506   | Layout 1             | `0081f71f5209`  |
| 1504   | Layout 1             | `0081f71f5209`  |
| 1500   | Layout 1             | `0081f71f5209`  |
| 1493   | Layout 1             | `0081f71f5209`  |
| 1489   | Layout 1             | `0081f71f5209`  |
| 1485   | Layout 1             | `0081f71f5209`  |
| 1481   | Layout 1             | `0081f71f5209`  |
| 1474   | Layout 1             | `0081f71f5209`  |
| 1466   | Layout 1             | `0081f71f5209`  |
| 1462   | Layout 1             | `0081f71f5209`  |
| 1459   | Layout 1             | `0081f71f5209`  |
| 1453   | Layout 1             | `0081f71f5209`  |
| 1450   | Layout 1             | `0081f71f5209`  |
| 1445   | Layout 1             | `0081f71f5209`  |
| 1439   | Layout 1             | `0081f71f5209`  |
| 1433   | Layout 1             | `0081f71f5209`  |
| 1430   | Layout 1             | `0081f71f5209`  |
| 1426   | Layout 1             | `0081f71f5209`  |
| 1421   | Layout 1             | `0081f71f5209`  |
| 1417   | Layout 1             | `0081f71f5209`  |
| 1416   | Layout 1             | `0081f71f5209`  |
| 1409   | Layout 1             | `0081f71f5209`  |
| 1405   | Layout 1             | `0081f71f5209`  |
| 1401   | Layout 1             | `0081f71f5209`  |
| 1396   | Layout 1             | `0081f71f5209`  |
| 1391   | Layout 1             | `0081f71f5209`  |
| 1390   | Layout 1             | `0081f71f5209`  |
| 1386   | Layout 1             | `0081f71f5209`  |
| 1381   | Layout 1             | `0081f71f5209`  |
| 1379   | Layout 1             | `0081f71f5209`  |
| 1372   | Layout 1             | `0081f71f5209`  |
| 1366   | Layout 1             | `0081f71f5209`  |
| 1364   | Layout 1             | `0081f71f5209`  |
| 1363   | Layout 1             | `0081f71f5209`  |
| 1360   | Layout 1             | `0081f71f5209`  |
| 1358   | Layout 1             | `0081f71f5209`  |
| 1355   | Layout 1             | `0081f71f5209`  |
| 1351   | Layout 1             | `0081f71f5209`  |
| 1348   | Layout 1             | `0081f71f5209`  |
| 1346   | Layout 1             | `0081f71f5209`  |
| 1341   | Layout 1             | `0081f71f5209`  |
| 1340   | Layout 1             | `0081f71f5209`  |
| 1338   | Layout 1             | `0081f71f5209`  |
| 1335   | Layout 1             | `0081f71f5209`  |
| 1333   | Layout 1             | `0081f71f5209`  |
| 1329   | Layout 1             | `0081f71f5209`  |
| 1327   | Layout 1             | `0081f71f5209`  |
| 1324   | Layout 1             | `0081f71f5209`  |
| 1321   | Layout 1             | `0081f71f5209`  |
| 1319   | Layout 1             | `0081f71f5209`  |
| 1318   | Layout 1             | `0081f71f5209`  |
| 1316   | Layout 1             | `0081f71f5209`  |
| 1313   | Layout 1             | `0081f71f5209`  |
| 1311   | Layout 1             | `0081f71f5209`  |
| 1309   | Layout 1             | `0081f71f5209`  |
| 1304   | Layout 1             | `0081f71f5209`  |
| 1292   | No file              | `0081f71f5209`  |
| 1286   | No file              | `0081f71f5209`  |
| 1280   | No file              | `0081f71f5209`  |
| 1276   | No file              | `0081f71f5209`  |
| 1267   | No file              | `0081f71f5209`  |
| 1261   | No file              | `0081f71f5209`  |
| 1256   | No file              | `0081f71f5209`  |
| 1250   | No file              | `0081f71f5209`  |
| 1246   | No file              | `0081f71f5209`  |
| 1239   | No file              | `0081f71f5209`  |
| 1230   | No file              | `0081f71f5209`  |
| 1226   | No file              | `0081f71f5209`  |
| 1220   | No file              | `0081f71f5209`  |
| 1217   | No file              | `0081f71f5209`  |
| 1211   | No file              | `0081f71f5209`  |
| 1210   | No file              | `0081f71f5209`  |
| 1208   | No file              | `0081f71f5209`  |
| 1203   | No file              | `0081f71f5209`  |
| 1197   | No file              | `0081f71f5209`  |
| 1194   | No file              | `0081f71f5209`  |
| 1192   | No file              | `0081f71f5209`  |
| 1187   | No file              | `0081f71f5209`  |
| 1183   | No file              | `0081f71f5209`  |
| 1177   | No file              | `0081f71f5209`  |
| 1173   | No file              | `0081f71f5209`  |
| 1167   | No file              | `0081f71f5209`  |
| 1164   | No file              | `0081f71f5209`  |
| 1156   | No file              | `0081f71f5209`  |
| 1149   | No file              | `0081f71f5209`  |
| 1144   | No file              | `0081f71f5209`  |
| 1137   | No file              | `0081f71f5209`  |
| 1132   | No file              | `0081f71f5209`  |
| 1127   | No file              | `0081f71f5209`  |
| 1122   | No file              | `0081f71f5209`  |
| 1118   | No file              | `0081f71f5209`  |
| 1114   | No file              | `0081f71f5209`  |
| 1109   | No file              | `0081f71f5209`  |
| 1102   | No file              | `0081f71f5209`  |
| 1096   | No file              | `0081f71f5209`  |
| 1088   | No file              | `0081f71f5209`  |
| 1081   | No file              | `0081f71f5209`  |
| 1076   | No file              | `0081f71f5209`  |
| 1069   | No file              | `0081f71f5209`  |
| 1064   | No file              | `0081f71f5209`  |
| 1058   | No file              | `0081f71f5209`  |
| 1051   | No file              | `0081f71f5209`  |
| 1044   | No file              | `0081f71f5209`  |
| 1036   | No file              | `0081f71f5209`  |
| 1026   | No file              | `0081f71f5209`  |
| 1016   | No file              | `0081f71f5209`  |
| 1009   | No file              | `0081f71f5209`  |
| 1005   | No file              | `0081f71f5209`  |
| 1000   | No file              | `0081f71f5209`  |
| 998    | No file              | `0081f71f5209`  |
| 990    | No file              | `0081f71f5209`  |
| 979    | No file              | `0081f71f5209`  |
| 972    | No file              | `0081f71f5209`  |
| 963    | No file              | `0081f71f5209`  |
| 955    | No file              | `0081f71f5209`  |
| 946    | No file              | `0081f71f5209`  |
| 938    | No file              | `0081f71f5209`  |
| 927    | No file              | `0081f71f5209`  |
| 911    | No file              | `0081f71f5209`  |
| 904    | No file              | `0081f71f5209`  |
| 899    | No file              | `0081f71f5209`  |
| 894    | No file              | `0081f71f5209`  |
| 885    | No file              | `0081f71f5209`  |
| 879    | No file              | `0081f71f5209`  |
| 872    | No file              | `0081f71f5209`  |
| 864    | No file              | `0081f71f5209`  |
| 855    | No file              | `0081f71f5209`  |
| 853    | No file              | `0081f71f5209`  |
| 845    | No file              | `0081f71f5209`  |
| 837    | No file              | `0081f71f5209`  |
| 829    | No file              | `0081f71f5209`  |
| 822    | No file              | `0081f71f5209`  |
| 814    | No file              | `0081f71f5209`  |
| 805    | No file              | `0081f71f5209`  |
| 794    | No file              | `0081f71f5209`  |
| 787    | No file              | `0081f71f5209`  |
| 780    | No file              | `0081f71f5209`  |
| 771    | No file              | `0081f71f5209`  |
| 760    | No file              | `0081f71f5209`  |
| 748    | No file              | `0081f71f5209`  |
| 741    | No file              | `0081f71f5209`  |
| 736    | No file              | `0081f71f5209`  |
| 731    | No file              | `0081f71f5209`  |
| 723    | No file              | `0081f71f5209`  |
| 711    | No file              | `0081f71f5209`  |
| 707    | No file              | `0081f71f5209`  |
| 697    | No file              | `0081f71f5209`  |
| 689    | No file              | `0081f71f5209`  |
| 683    | No file              | `0081f71f5209`  |
| 678    | No file              | `0081f71f5209`  |
| 670    | No file              | `0081f71f5209`  |
| 661    | No file              | `0081f71f5209`  |
| 656    | No file              | `0081f71f5209`  |
| 652    | No file              | `0081f71f5209`  |
| 643    | No file              | `0081f71f5209`  |
| 637    | No file              | `0081f71f5209`  |
| 630    | No file              | `0081f71f5209`  |
| 627    | No file              | `0081f71f5209`  |
| 621    | No file              | `0081f71f5209`  |
| 617    | No file              | `0081f71f5209`  |
| 615    | No file              | `0081f71f5209`  |
| 606    | No file              | `0081f71f5209`  |
| 599    | No file              | `0081f71f5209`  |
| 592    | No file              | `0081f71f5209`  |
| 586    | No file              | `0081f71f5209`  |
| 577    | No file              | `0081f71f5209`  |
| 569    | No file              | `0081f71f5209`  |
| 561    | No file              | `0081f71f5209`  |
| 554    | No file              | `0081f71f5209`  |
| 542    | No file              | `0081f71f5209`  |
| 532    | No file              | `0081f71f5209`  |
| 531    | No file              | `0081f71f5209`  |
| 526    | No file              | `0081f71f5209`  |
| 521    | No file              | `0081f71f5209`  |
| 517    | No file              | `0081f71f5209`  |
| 510    | No file              | `0081f71f5209`  |
| 508    | No file              | `0081f71f5209`  |
| 504    | No file              | `0081f71f5209`  |
| 497    | No file              | `0081f71f5209`  |
| 491    | No file              | `0081f71f5209`  |
| 485    | No file              | `0081f71f5209`  |
| 478    | No file              | `0081f71f5209`  |
| 472    | No file              | `0081f71f5209`  |
| 466    | No file              | `0081f71f5209`  |
| 457    | No file              | `0081f71f5209`  |
| 452    | No file              | `0081f71f5209`  |
| 449    | No file              | `0081f71f5209`  |
| 435    | No file              | `0081f71f5209`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                               |
| ----------------------------- | -------- | ---------------------------------------------------------------------------------- |
| `houseinforeceipeoffset.dbss` | Optional | Index `receipe_key -> (offset, size)`, see below; the handler walks the rows in order and does not load it |
| `languagedata_en.loc`         | Optional | LOC type 16, `str_id1` = `receipe_key`: the English receipe name                   |
| `houseinfoneeditem.dbss`      | Optional | Per-level need items, joined by `need_item_key`; see [`houseinfoneeditem.dbss`](houseinfoneeditem_dbss.md) |
| `itemexchangesource.bss`      | Optional | The item exchange recipes the level lists key into; see [`itemexchangesource.bss`](../bss/itemexchangesource_bss.md). The handler reads their names from the `EXCHANGE_NAME_KR` lookup index and LOC type 24 (see `docs/handler.md`) and does not open the file |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | `132` on client 3464 |
| `+0x04` | Row[row_count] | rows      | See Row              |

Rows are not sorted by key. On client 3464 the file opens with the Guild
Storage keys 50009 down to 50001 and ends with 28 down to 16.

### Row (variable: 25 bytes + name text and lists)

A fixed head, the inline UTF-16LE name, three bytes, five counted level
lists, a u32 and a counted byte list. Rows differ in length; a reader takes
every length from its count.

| Offset                  | Type                   | Field               | Notes                                                                 |
| ----------------------- | ---------------------- | ------------------- | --------------------------------------------------------------------- |
| `+0x00`                 | u32                    | receipe_key         | Unique row key; LOC type 16 `str_id1`                                 |
| `+0x04`                 | u16                    | need_item_key       | `houseinfoneeditem.dbss` key, see Need Item Join                     |
| `+0x06`                 | str16                  | name                | Korean receipe name, such as `무기 단조 공방`                          |
| `name+0x00`             | u8                     | house_use_type      | `CppEnums.eHouseUseType`, see House Use Type                          |
| `name+0x01`             | u8                     | icon_type           | `CppEnums.eHouseIconType`, see Icon Type                              |
| `name+0x02`             | u8                     | unknown_tail_02     | `0` on every row (client 3464)                                        |
| `name+0x03`             | Level List[5]          | level_exchanges     | Levels 1 to 5, see Level List                                         |
| `level_exchanges+0x00`  | u32                    | unknown_after_level_exchanges | `0` on every row (client 3464)                                        |
| `level_exchanges+0x04`  | u32                    | unknown_end_count   | Bytes in `unknown_end`                                                |
| `level_exchanges+0x08`  | u8[unknown_end_count]  | unknown_end         | See Open Questions                                                    |

A level list is empty when the house does nothing at that level (Residence,
Lodging, Storage, Horse Ranch and the Guild Storage rows have five empty
lists). The lists fill from level 1 up with no gap: on client 3464, 13 rows
fill no list, and the others fill 1 to 5 levels. The longest list holds 93
keys.

### Level List (variable: 4 bytes + keys)

| Offset  | Type         | Field          | Notes                       |
| ------- | ------------ | -------------- | --------------------------- |
| `+0x00` | u32          | count          | Number of keys              |
| `+0x04` | u32[count]   | exchange_keys  | Item exchange keys          |

### `houseinforeceipeoffset.dbss`

| Offset  | Type                 | Field     | Notes                                               |
| ------- | -------------------- | --------- | --------------------------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count`; `132` on client 3464 |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                                       |

Every index row points at the main row with the same key, and the rows tile
the main file from `0x04` to the end with no gap. The index order is neither
the main file's order nor sorted by key: it opens 50009, 50008, 50007,
50006, 50005, 50004, 50003, 1106, 50002, 1105.

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                              |
| ------- | ---- | ----------- | -------------------------------------------------- |
| `+0x00` | u32  | receipe_key | The main row's `receipe_key`                       |
| `+0x04` | u32  | offset      | Start of the row in `houseinforeceipe.dbss`, at its `receipe_key` |
| `+0x08` | u32  | size        | Full row length, key included                      |

## Layout 1

Client 1784 rows hold `house_use_type` only, without `icon_type` and
`unknown_tail_02`, list their exchange keys as u16, and end after
`unknown_after_level_exchanges`, with no `unknown_end`. Only the Row and the
Level List differ from Layout 2.

### Row (variable: 19 bytes + name text and lists)

| Offset                 | Type          | Field                         | Notes                         |
| ---------------------- | ------------- | ----------------------------- | ----------------------------- |
| `+0x00`                | u32           | receipe_key                   |                               |
| `+0x04`                | u16           | need_item_key                 |                               |
| `+0x06`                | str16         | name                          |                               |
| `name+0x00`            | u8            | house_use_type                |                               |
| `name+0x01`            | Level List[5] | level_exchanges               |                               |
| `level_exchanges+0x00` | u32           | unknown_after_level_exchanges | `0` on every row (client 1784) |

### Level List (variable: 4 bytes + keys)

| Offset  | Type       | Field         | Notes                                    |
| ------- | ---------- | ------------- | ---------------------------------------- |
| `+0x00` | u32        | count         |                                          |
| `+0x04` | u16[count] | exchange_keys | Item exchange keys, 35013 at most on client 1784 |

## House Use Type

`house_use_type` takes the values of `CppEnums.eHouseUseType` in
`global_define_cpp_enum.lua`. The English names in the table are the LOC
type 16 names of the rows that hold each value (client 3464).

| Value | eHouseUseType            | Rows | Receipes                                                                 |
| ----- | ------------------------ | ---- | ------------------------------------------------------------------------ |
| 0     | Empty                    | 1    | Residence                                                                |
| 1     | Lodging                  | 1    | Lodging                                                                  |
| 2     | Depot                    | 10   | Storage, Guild Storage level 2 to 9                                      |
| 3     | Ranch                    | 1    | Horse Ranch                                                              |
| 4     | WeaponForgingWorkshop    | 2    | Weapon Workshop, Duvencrune Weapon Workshop                              |
| 5     | ArmorForgingWorkshop     | 1    | Armor Workshop                                                           |
| 6     | HandMadeWorkshop         | 1    | Handcraft Workshop                                                       |
| 7     | WoodCraftWorkshop        | 2    | Carpentry Workshop, Jangdok Platform                                     |
| 8     | JewelryWorkshop          | 5    | Jeweler, Manos Jeweler, Dokkebi Crystal Workshop, Safe and Risk Asset Management Bank |
| 9     | ToolWorkshop             | 5    | Tool Workshop, Old Moon Workshop, Dokkebi Tool Workshop                  |
| 10    | Refinery                 | 1    | Refinery                                                                 |
| 13    | Shipyard                 | 15   | Shipyard, Guild Shipyard, Mount Part Workshop, the five Specialties Packing rows, Imperial Trade Packing |
| 14    | CarriageWorkshop         | 9    | Wagon Workshop, Elephant Nursery                                         |
| 15    | HorseArmorWorkshop       | 2    | Horse Gear Workshop                                                      |
| 16    | FurnitureWorkshop        | 28   | Furniture Workshop, Old Moon Furniture Workshop, the six town workshops (Florin to O'draxxia) |
| 17    | LocalSpecailtiesWorkshop | 33   | Fish, Mushroom, Crop, Wood and Mineral Workshop                          |
| 18    | Wardrobe                 | 8    | Costume Mill, Old Moon Costume Mill                                      |
| 19    | SiegeWeapons             | 1    | Siege Weapon Workshop                                                    |
| 20    | ShipParts                | 4    | Ship Part Workshop, Iliya, Nampo and Cheongsa Ship Part Workshop         |
| 21    | WagonParts               | 1    | Wagon Part Workshop                                                      |
| 23    | PotteryWorkshop          | 1    | Ceramics Workshop                                                        |

No row holds 11 (ImproveWorkshop), 12 (CannonWorkshop) or 22
(AssetManagementshop); the two Asset Management Bank rows hold 8.

## Icon Type

`icon_type` takes the values of `CppEnums.eHouseIconType`. Values 0 to 23
name the same uses as `eHouseUseType`, and on those rows `icon_type` equals
`house_use_type`. The 40 rows where the two differ all hold an icon past 23
(client 3464):

| icon_type | eHouseIconType       | house_use_type | Receipes                  |
| --------- | -------------------- | -------------- | ------------------------- |
| 24        | Workshop_Florin      | 16             | Florin Workshop           |
| 25        | Workshop_Tarif       | 16             | Tarif Workshop            |
| 26        | Workshop_Arehaza     | 16             | Arehaza Workshop          |
| 27        | Workshop_Duvencrune  | 16             | Duvencrune Workshop       |
| 28        | Workshop_Grana       | 16             | Grána Workshop            |
| 29        | Workshop_Odraxxia    | 16             | O'draxxia Workshop        |
| 30        | Workshop_Fish        | 17             | Fish Workshop (7 rows)    |
| 31        | Workshop_Mushroom    | 17             | Mushroom Workshop (8)     |
| 32        | Workshop_Crop        | 17             | Crop Workshop (7)         |
| 33        | Workshop_Wood        | 17             | Wood Workshop (6)         |
| 34        | Workshop_Mineral     | 17             | Mineral Workshop (5)      |
| 35        | Jangdokdae           | 7              | Jangdok Platform          |

## Need Item Join

`need_item_key` is a key of [`houseinfoneeditem.dbss`](houseinfoneeditem_dbss.md),
whose index holds the u16 keys 1 to 11. Each of its rows holds level slots 0
to 5, and each level a transfer time and a list of (item key, count) pairs;
every item key there is 1 (Silver, LOC type 0).
On client 3464 the receipes use every key except 9, and no row's filled
level lists reach past the last level its group prices:

| need_item_key | Levels priced | Rows | Receipes                                                    |
| ------------- | ------------- | ---- | ----------------------------------------------------------- |
| 1             | 1 to 5        | 2    | Lodging, Horse Ranch                                        |
| 2             | 1 to 5        | 18   | Weapon, Duvencrune Weapon, Armor, Handcraft, Carpentry and Ceramics Workshop, Jeweler, Manos Jeweler, Dokkebi Crystal Workshop, Costume Mill, Old Moon Costume Mill, Jangdok Platform |
| 3             | none          | 1    | Residence                                                   |
| 4             | 2 to 5        | 10   | Storage, Guild Storage level 2 to 9                         |
| 5             | 1 to 2        | 42   | Processing workshops, Specialties Packing, Mount Part Workshop, Asset Management Banks |
| 6             | 1 to 3        | 1    | Refinery                                                    |
| 7             | 1 to 5        | 18   | Shipyard, Guild Shipyard, Wagon Workshop, Siege Weapon Workshop, Elephant Nursery |
| 8             | 1 to 5        | 7    | Ship Part, Wagon Part and Horse Gear Workshops              |
| 10            | 1 to 4        | 5    | Tool Workshop, Old Moon Workshop, Dokkebi Tool Workshop     |
| 11            | 1 to 5        | 28   | Furniture Workshops and the six town workshops              |

The Refinery fills three level lists and its group prices three levels; the
Tool Workshops fill up to four and their group prices four; the processing
workshops fill up to two and group 5 prices two. The house window asks for
the need items by receipe key and level
(`getNeedItemListItemKey(receipeKey, level, index)` and
`getNeedItemListItemCount` in `panel_new_housecontrol.lua`), so the client
needs a receipe-to-group link, and `need_item_key` is the field whose
groups line up with the level lists.

## Notes

- The house window builds its work list per level: it calls
  `ToClient_getHouseWorkableListByDataOnlySize(receipeKey, 1, level)` once
  per level and starts a new level row when the count is reached, and each
  entry is an item exchange
  (`ToClient_getHouseDataWorkableItemExchangeByIndex` returns a wrapper with
  `getFirstDropGroup`) in `panel_new_housecontrol.lua`. The window draws five
  grade buttons per receipe (`for level = 1, 5`).
- For Lodging, Depot and Ranch the window shows a guide line per level
  (`getWorkerCount`, `getExtendWarehouseCount`, `getExtendStableCount`)
  instead of a work list, which fits their empty level lists.
- `getGroupTypeByIndex` and `rentHouse:getHouseUseType()` return
  `eHouseUseType` values: the tutorial compares the group type with
  `CppEnums.eHouseUseType.Empty` (`tutorial_phase11_worldmapbuyhouse.lua`).
  `getIconType()` feeds `CppEnums.HouseIconType_*Texture[iconType]`.
- On client 3474 all 2,405 distinct exchange keys (5002 to 35015) are
  `itemexchangesource.bss` rows: 2,364 NonRecipeCraft, 19 LargeCraft and 22
  GuildHouseLargeCraft. 5026 (Weapon Workshop level 1) is Azwell Longsword:
  Steel x5, Pure Copper Crystal x1, Fine Tough Hide x1 and Black Stone
  Powder x5. 8801 (Shipyard level 1) is Ship License: Rowboat, starting with
  Usable Scantling x10 and Ash Plywood x20.
- The Exchanges column shows one line per filled level, each exchange as its
  name and key (`Azwell Longsword (5026)`) linked to its
  `itemexchangesource.bss` row; past four per level the rest sit behind a
  hoverable count. The `exchanges` record field holds the same texts for
  search and export.
- LOC type 16 also names 1603 "Chariot Workshop", which has no row on
  client 3464.
- Rows 50006 and 50007 both carry the Korean name `길드 창고 7단계` and the
  English "Guild Storage level 7".

## Open Questions

### unknown_end

The trailing byte list holds `0, 1, 2, 3, 4, 5` on 118 rows, `6, 7, 8` on
12 rows (2003 to 2013 and 1416 Old Moon Furniture Workshop) and `6` on 2001
Dokkebi Crystal Workshop and 2002 Dokkebi Tool Workshop (client 3464).
Read as `eHouseUseType` the values would be Empty to ArmorForgingWorkshop and
HandMade, WoodCraft and Jewelry, which does not fit a Fish Workshop. Read as
territory keys (LOC type 12) `6, 7, 8` are Kamasylvia, Drieghan and
O'dyllita, yet 27 Grána Workshop holds `0` to `5`. calpheonlabs reads the
list as accepted `eHouseUseGroupType` codes and cites `getGroupTypeByIndex`;
that call returns one value per receipe, which `house_use_type` already
holds, so it is only a lead.

### unknown_after_level_exchanges

The u32 after the five level lists is `0` on every row. It reads the same as
the count of a sixth, empty level list; `houseinfoneeditem.dbss` prices five
levels and the window draws five grade buttons, so the layout here keeps
five lists and a separate u32. calpheonlabs names it a content group key,
which no client file confirms yet.

### unknown_tail_02

The byte after `icon_type` is `0` on every row (client 3464).
