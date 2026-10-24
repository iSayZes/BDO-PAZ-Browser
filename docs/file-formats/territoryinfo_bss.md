# `territoryinfo.bss` Format

## Purpose

The world's territories (Balenos, Serendia, Calpheon, ...) in game order: one
row per territory with its Korean territory and nation names, world map mark
icons, the booty items its lord receives (a conquest crown and armor), its
siege positions and its territory supply keys. The row key is the LOC type 12
ID, so the English territory and nation names come from that type.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records          | Row bytes                  |
| ------ | -------------- | ------- | ------------------- | ----- | ---------------- | -------------------------- |
| 9      | 2726 and later | 3483    | `territoryinfo.bss` | 4,730 | 14 Territory Row | 88 to 92, 89 on average    |
| 8      | 2575 to 2717   | 2717    | `territoryinfo.bss` | 4,067 | 12 Territory Row | 88 to 90, 88 on average    |
| 7      | 2474 to 2567   | 2567    | `territoryinfo.bss` | 4,203 | 12 Territory Row | 96 to 108, 100 on average  |
| 6      | 1276 to 2468   | 2468    | `territoryinfo.bss` | 4,491 | 12 Territory Row | 120 to 132, 124 on average |
| 5      | 805 to 1267    | 1267    | `territoryinfo.bss` | 3,218 | 9 Territory Row  | 116 to 136, 129 on average |
| 4      | 723 to 794     | 794     | `territoryinfo.bss` | 4,168 | 8 Territory Row  | 480 to 542, 520 on average |
| 3      | 526 to 711     | 711     | `territoryinfo.bss` | 3,976 | 8 Territory Row  | 456 to 518, 496 on average |
| 2      | 472 to 521     | 521     | `territoryinfo.bss` | 3,138 | 7 Territory Row  | 434 to 456, 448 on average |
| 1      | 435 to 466     | 466     | `territoryinfo.bss` | 2,986 | 7 Territory Row  | 412 to 438, 426 on average |

| Layout | File                | Known            | Unknown     |
| ------ | ------------------- | ---------------- | ----------- |
| 9      | `territoryinfo.bss` | 4,674 B (98.8%)  | 56 B (1.2%) |
| 8      | `territoryinfo.bss` | 4,019 B (98.8%)  | 48 B (1.2%) |
| 7      | `territoryinfo.bss` | 4,155 B (98.9%)  | 48 B (1.1%) |
| 6      | `territoryinfo.bss` | 4,443 B (98.9%)  | 48 B (1.1%) |
| 5      | `territoryinfo.bss` | 3,218 B (100.0%) | 0 B (0.0%)  |
| 4      | `territoryinfo.bss` | 4,168 B (100.0%) | 0 B (0.0%)  |
| 3      | `territoryinfo.bss` | 3,976 B (100.0%) | 0 B (0.0%)  |
| 2      | `territoryinfo.bss` | 3,138 B (100.0%) | 0 B (0.0%)  |
| 1      | `territoryinfo.bss` | 2,986 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 9 | `ac532975a82d`  |
| 3482   | Layout 9 | `ac532975a82d`  |
| 3474   | Layout 9 | `ac532975a82d`  |
| 3473   | Layout 9 | `ac532975a82d`  |
| 3464   | Layout 9 | `ac532975a82d`  |
| 3458   | Layout 9 | `ac532975a82d`  |
| 3454   | Layout 9 | `ac532975a82d`  |
| 3444   | Layout 9 | `ac532975a82d`  |
| 3435   | Layout 9 | `ac532975a82d`  |
| 3426   | Layout 9 | `ac532975a82d`  |
| 3418   | Layout 9 | `ac532975a82d`  |
| 3412   | Layout 9 | `ac532975a82d`  |
| 3402   | Layout 9 | `ac532975a82d`  |
| 3396   | Layout 9 | `ac532975a82d`  |
| 3387   | Layout 9 | `ac532975a82d`  |
| 3381   | Layout 9 | `ac532975a82d`  |
| 3373   | Layout 9 | `ac532975a82d`  |
| 3364   | Layout 9 | `ac532975a82d`  |
| 3356   | Layout 9 | `ac532975a82d`  |
| 3349   | Layout 9 | `ac532975a82d`  |
| 3342   | Layout 9 | `ac532975a82d`  |
| 3335   | Layout 9 | `ac532975a82d`  |
| 3326   | Layout 9 | `ac532975a82d`  |
| 3321   | Layout 9 | `ac532975a82d`  |
| 3314   | Layout 9 | `ac532975a82d`  |
| 3303   | Layout 9 | `ac532975a82d`  |
| 3302   | Layout 9 | `ac532975a82d`  |
| 3293   | Layout 9 | `ac532975a82d`  |
| 3283   | Layout 9 | `ac532975a82d`  |
| 3275   | Layout 9 | `ac532975a82d`  |
| 3267   | Layout 9 | `ac532975a82d`  |
| 3258   | Layout 9 | `ac532975a82d`  |
| 3251   | Layout 9 | `ac532975a82d`  |
| 3242   | Layout 9 | `ac532975a82d`  |
| 3235   | Layout 9 | `ac532975a82d`  |
| 3229   | Layout 9 | `ac532975a82d`  |
| 3212   | Layout 9 | `ac532975a82d`  |
| 3203   | Layout 9 | `ac532975a82d`  |
| 3193   | Layout 9 | `ac532975a82d`  |
| 3186   | Layout 9 | `ac532975a82d`  |
| 3177   | Layout 9 | `ac532975a82d`  |
| 3169   | Layout 9 | `ac532975a82d`  |
| 3158   | Layout 9 | `ac532975a82d`  |
| 3151   | Layout 9 | `ac532975a82d`  |
| 3144   | Layout 9 | `ac532975a82d`  |
| 3133   | Layout 9 | `ac532975a82d`  |
| 3125   | Layout 9 | `ac532975a82d`  |
| 3118   | Layout 9 | `ac532975a82d`  |
| 3111   | Layout 9 | `ac532975a82d`  |
| 3103   | Layout 9 | `ac532975a82d`  |
| 3095   | Layout 9 | `ac532975a82d`  |
| 3086   | Layout 9 | `ac532975a82d`  |
| 3072   | Layout 9 | `ac532975a82d`  |
| 3062   | Layout 9 | `ac532975a82d`  |
| 3052   | Layout 9 | `ac532975a82d`  |
| 3045   | Layout 9 | `ac532975a82d`  |
| 3037   | Layout 9 | `ac532975a82d`  |
| 3030   | Layout 9 | `ac532975a82d`  |
| 3021   | Layout 9 | `ac532975a82d`  |
| 3012   | Layout 9 | `ac532975a82d`  |
| 3002   | Layout 9 | `ac532975a82d`  |
| 2995   | Layout 9 | `ac532975a82d`  |
| 2987   | Layout 9 | `ac532975a82d`  |
| 2978   | Layout 9 | `ac532975a82d`  |
| 2970   | Layout 9 | `ac532975a82d`  |
| 2959   | Layout 9 | `ac532975a82d`  |
| 2951   | Layout 9 | `ac532975a82d`  |
| 2942   | Layout 9 | `ac532975a82d`  |
| 2935   | Layout 9 | `ac532975a82d`  |
| 2932   | Layout 9 | `ac532975a82d`  |
| 2923   | Layout 9 | `ac532975a82d`  |
| 2919   | Layout 9 | `ac532975a82d`  |
| 2907   | Layout 9 | `ac532975a82d`  |
| 2900   | Layout 9 | `ac532975a82d`  |
| 2891   | Layout 9 | `ac532975a82d`  |
| 2882   | Layout 9 | `ac532975a82d`  |
| 2872   | Layout 9 | `ac532975a82d`  |
| 2863   | Layout 9 | `ac532975a82d`  |
| 2855   | Layout 9 | `ac532975a82d`  |
| 2849   | Layout 9 | `ac532975a82d`  |
| 2844   | Layout 9 | `ac532975a82d`  |
| 2834   | Layout 9 | `ac532975a82d`  |
| 2825   | Layout 9 | `ac532975a82d`  |
| 2819   | Layout 9 | `ac532975a82d`  |
| 2811   | Layout 9 | `ac532975a82d`  |
| 2803   | Layout 9 | `ac532975a82d`  |
| 2794   | Layout 9 | `ac532975a82d`  |
| 2783   | Layout 9 | `ac532975a82d`  |
| 2774   | Layout 9 | `ac532975a82d`  |
| 2765   | Layout 9 | `ac532975a82d`  |
| 2756   | Layout 9 | `ac532975a82d`  |
| 2750   | Layout 9 | `ac532975a82d`  |
| 2743   | Layout 9 | `ac532975a82d`  |
| 2736   | Layout 9 | `ac532975a82d`  |
| 2726   | Layout 9 | `ac532975a82d`  |
| 2717   | Layout 8 | `ac532975a82d`  |
| 2709   | Layout 8 | `ac532975a82d`  |
| 2703   | Layout 8 | `ac532975a82d`  |
| 2695   | Layout 8 | `ac532975a82d`  |
| 2684   | Layout 8 | `ac532975a82d`  |
| 2672   | Layout 8 | `ac532975a82d`  |
| 2665   | Layout 8 | `ac532975a82d`  |
| 2657   | Layout 8 | `ac532975a82d`  |
| 2649   | Layout 8 | `ac532975a82d`  |
| 2644   | Layout 8 | `ac532975a82d`  |
| 2637   | Layout 8 | `ac532975a82d`  |
| 2629   | Layout 8 | `ac532975a82d`  |
| 2619   | Layout 8 | `ac532975a82d`  |
| 2612   | Layout 8 | `ac532975a82d`  |
| 2606   | Layout 8 | `ac532975a82d`  |
| 2602   | Layout 8 | `ac532975a82d`  |
| 2601   | Layout 8 | `ac532975a82d`  |
| 2592   | Layout 8 | `ac532975a82d`  |
| 2583   | Layout 8 | `ac532975a82d`  |
| 2575   | Layout 8 | `ac532975a82d`  |
| 2567   | Layout 7 | `ac532975a82d`  |
| 2560   | Layout 7 | `ac532975a82d`  |
| 2553   | Layout 7 | `ac532975a82d`  |
| 2545   | Layout 7 | `ac532975a82d`  |
| 2538   | Layout 7 | `ac532975a82d`  |
| 2529   | Layout 7 | `ac532975a82d`  |
| 2519   | Layout 7 | `ac532975a82d`  |
| 2513   | Layout 7 | `ac532975a82d`  |
| 2510   | Layout 7 | `ac532975a82d`  |
| 2507   | Layout 7 | `ac532975a82d`  |
| 2503   | Layout 7 | `ac532975a82d`  |
| 2498   | Layout 7 | `ac532975a82d`  |
| 2492   | Layout 7 | `ac532975a82d`  |
| 2487   | Layout 7 | `ac532975a82d`  |
| 2480   | Layout 7 | `ac532975a82d`  |
| 2474   | Layout 7 | `ac532975a82d`  |
| 2468   | Layout 6 | `ac532975a82d`  |
| 2460   | Layout 6 | `ac532975a82d`  |
| 2453   | Layout 6 | `ac532975a82d`  |
| 2444   | Layout 6 | `ac532975a82d`  |
| 2438   | Layout 6 | `ac532975a82d`  |
| 2434   | Layout 6 | `ac532975a82d`  |
| 2429   | Layout 6 | `ac532975a82d`  |
| 2421   | Layout 6 | `ac532975a82d`  |
| 2414   | Layout 6 | `ac532975a82d`  |
| 2407   | Layout 6 | `ac532975a82d`  |
| 2401   | Layout 6 | `ac532975a82d`  |
| 2397   | Layout 6 | `ac532975a82d`  |
| 2393   | Layout 6 | `ac532975a82d`  |
| 2384   | Layout 6 | `ac532975a82d`  |
| 2378   | Layout 6 | `ac532975a82d`  |
| 2372   | Layout 6 | `ac532975a82d`  |
| 2358   | Layout 6 | `ac532975a82d`  |
| 2352   | Layout 6 | `ac532975a82d`  |
| 2347   | Layout 6 | `ac532975a82d`  |
| 2343   | Layout 6 | `ac532975a82d`  |
| 2335   | Layout 6 | `ac532975a82d`  |
| 2327   | Layout 6 | `ac532975a82d`  |
| 2324   | Layout 6 | `ac532975a82d`  |
| 2319   | Layout 6 | `ac532975a82d`  |
| 2313   | Layout 6 | `ac532975a82d`  |
| 2308   | Layout 6 | `ac532975a82d`  |
| 2302   | Layout 6 | `ac532975a82d`  |
| 2295   | Layout 6 | `ac532975a82d`  |
| 2290   | Layout 6 | `ac532975a82d`  |
| 2284   | Layout 6 | `ac532975a82d`  |
| 2276   | Layout 6 | `ac532975a82d`  |
| 2269   | Layout 6 | `ac532975a82d`  |
| 2259   | Layout 6 | `ac532975a82d`  |
| 2250   | Layout 6 | `ac532975a82d`  |
| 2243   | Layout 6 | `ac532975a82d`  |
| 2235   | Layout 6 | `ac532975a82d`  |
| 2229   | Layout 6 | `ac532975a82d`  |
| 2224   | Layout 6 | `ac532975a82d`  |
| 2218   | Layout 6 | `ac532975a82d`  |
| 2215   | Layout 6 | `ac532975a82d`  |
| 2207   | Layout 6 | `ac532975a82d`  |
| 2203   | Layout 6 | `ac532975a82d`  |
| 2196   | Layout 6 | `ac532975a82d`  |
| 2192   | Layout 6 | `ac532975a82d`  |
| 2189   | Layout 6 | `ac532975a82d`  |
| 2183   | Layout 6 | `ac532975a82d`  |
| 2179   | Layout 6 | `ac532975a82d`  |
| 2171   | Layout 6 | `ac532975a82d`  |
| 2163   | Layout 6 | `ac532975a82d`  |
| 2156   | Layout 6 | `ac532975a82d`  |
| 2151   | Layout 6 | `ac532975a82d`  |
| 2147   | Layout 6 | `ac532975a82d`  |
| 2142   | Layout 6 | `ac532975a82d`  |
| 2138   | Layout 6 | `ac532975a82d`  |
| 2134   | Layout 6 | `ac532975a82d`  |
| 2130   | Layout 6 | `ac532975a82d`  |
| 2122   | Layout 6 | `ac532975a82d`  |
| 2107   | Layout 6 | `ac532975a82d`  |
| 2098   | Layout 6 | `ac532975a82d`  |
| 2089   | Layout 6 | `ac532975a82d`  |
| 2081   | Layout 6 | `ac532975a82d`  |
| 2073   | Layout 6 | `ac532975a82d`  |
| 2067   | Layout 6 | `ac532975a82d`  |
| 2063   | Layout 6 | `ac532975a82d`  |
| 2059   | Layout 6 | `ac532975a82d`  |
| 2052   | Layout 6 | `ac532975a82d`  |
| 2044   | Layout 6 | `ac532975a82d`  |
| 2039   | Layout 6 | `ac532975a82d`  |
| 2032   | Layout 6 | `ac532975a82d`  |
| 2025   | Layout 6 | `ac532975a82d`  |
| 2011   | Layout 6 | `ac532975a82d`  |
| 2005   | Layout 6 | `ac532975a82d`  |
| 2000   | Layout 6 | `ac532975a82d`  |
| 1996   | Layout 6 | `ac532975a82d`  |
| 1991   | Layout 6 | `ac532975a82d`  |
| 1985   | Layout 6 | `ac532975a82d`  |
| 1980   | Layout 6 | `ac532975a82d`  |
| 1969   | Layout 6 | `ac532975a82d`  |
| 1964   | Layout 6 | `ac532975a82d`  |
| 1958   | Layout 6 | `ac532975a82d`  |
| 1950   | Layout 6 | `ac532975a82d`  |
| 1945   | Layout 6 | `ac532975a82d`  |
| 1937   | Layout 6 | `ac532975a82d`  |
| 1933   | Layout 6 | `ac532975a82d`  |
| 1927   | Layout 6 | `ac532975a82d`  |
| 1921   | Layout 6 | `ac532975a82d`  |
| 1914   | Layout 6 | `ac532975a82d`  |
| 1908   | Layout 6 | `ac532975a82d`  |
| 1897   | Layout 6 | `ac532975a82d`  |
| 1892   | Layout 6 | `ac532975a82d`  |
| 1886   | Layout 6 | `ac532975a82d`  |
| 1881   | Layout 6 | `ac532975a82d`  |
| 1871   | Layout 6 | `ac532975a82d`  |
| 1866   | Layout 6 | `ac532975a82d`  |
| 1862   | Layout 6 | `ac532975a82d`  |
| 1854   | Layout 6 | `ac532975a82d`  |
| 1846   | Layout 6 | `ac532975a82d`  |
| 1838   | Layout 6 | `ac532975a82d`  |
| 1832   | Layout 6 | `ac532975a82d`  |
| 1826   | Layout 6 | `ac532975a82d`  |
| 1822   | Layout 6 | `ac532975a82d`  |
| 1818   | Layout 6 | `ac532975a82d`  |
| 1804   | Layout 6 | `ac532975a82d`  |
| 1794   | Layout 6 | `ac532975a82d`  |
| 1790   | Layout 6 | `ac532975a82d`  |
| 1784   | Layout 6 | `ac532975a82d`  |
| 1774   | Layout 6 | `ac532975a82d`  |
| 1771   | Layout 6 | `ac532975a82d`  |
| 1762   | Layout 6 | `ac532975a82d`  |
| 1759   | Layout 6 | `ac532975a82d`  |
| 1754   | Layout 6 | `ac532975a82d`  |
| 1749   | Layout 6 | `ac532975a82d`  |
| 1743   | Layout 6 | `ac532975a82d`  |
| 1737   | Layout 6 | `ac532975a82d`  |
| 1731   | Layout 6 | `ac532975a82d`  |
| 1725   | Layout 6 | `ac532975a82d`  |
| 1717   | Layout 6 | `ac532975a82d`  |
| 1710   | Layout 6 | `ac532975a82d`  |
| 1704   | Layout 6 | `ac532975a82d`  |
| 1698   | Layout 6 | `ac532975a82d`  |
| 1690   | Layout 6 | `ac532975a82d`  |
| 1685   | Layout 6 | `ac532975a82d`  |
| 1680   | Layout 6 | `ac532975a82d`  |
| 1674   | Layout 6 | `ac532975a82d`  |
| 1668   | Layout 6 | `ac532975a82d`  |
| 1659   | Layout 6 | `ac532975a82d`  |
| 1649   | Layout 6 | `ac532975a82d`  |
| 1642   | Layout 6 | `ac532975a82d`  |
| 1636   | Layout 6 | `ac532975a82d`  |
| 1628   | Layout 6 | `ac532975a82d`  |
| 1622   | Layout 6 | `ac532975a82d`  |
| 1614   | Layout 6 | `ac532975a82d`  |
| 1608   | Layout 6 | `ac532975a82d`  |
| 1602   | Layout 6 | `ac532975a82d`  |
| 1598   | Layout 6 | `ac532975a82d`  |
| 1594   | Layout 6 | `ac532975a82d`  |
| 1590   | Layout 6 | `ac532975a82d`  |
| 1587   | Layout 6 | `ac532975a82d`  |
| 1584   | Layout 6 | `ac532975a82d`  |
| 1579   | Layout 6 | `ac532975a82d`  |
| 1572   | Layout 6 | `ac532975a82d`  |
| 1565   | Layout 6 | `ac532975a82d`  |
| 1559   | Layout 6 | `ac532975a82d`  |
| 1554   | Layout 6 | `ac532975a82d`  |
| 1547   | Layout 6 | `ac532975a82d`  |
| 1537   | Layout 6 | `ac532975a82d`  |
| 1529   | Layout 6 | `ac532975a82d`  |
| 1524   | Layout 6 | `ac532975a82d`  |
| 1519   | Layout 6 | `ac532975a82d`  |
| 1509   | Layout 6 | `ac532975a82d`  |
| 1506   | Layout 6 | `ac532975a82d`  |
| 1504   | Layout 6 | `ac532975a82d`  |
| 1500   | Layout 6 | `ac532975a82d`  |
| 1493   | Layout 6 | `ac532975a82d`  |
| 1489   | Layout 6 | `ac532975a82d`  |
| 1485   | Layout 6 | `ac532975a82d`  |
| 1481   | Layout 6 | `ac532975a82d`  |
| 1474   | Layout 6 | `ac532975a82d`  |
| 1466   | Layout 6 | `ac532975a82d`  |
| 1462   | Layout 6 | `ac532975a82d`  |
| 1459   | Layout 6 | `ac532975a82d`  |
| 1453   | Layout 6 | `ac532975a82d`  |
| 1450   | Layout 6 | `ac532975a82d`  |
| 1445   | Layout 6 | `ac532975a82d`  |
| 1439   | Layout 6 | `ac532975a82d`  |
| 1433   | Layout 6 | `ac532975a82d`  |
| 1430   | Layout 6 | `ac532975a82d`  |
| 1426   | Layout 6 | `ac532975a82d`  |
| 1421   | Layout 6 | `ac532975a82d`  |
| 1417   | Layout 6 | `ac532975a82d`  |
| 1416   | Layout 6 | `ac532975a82d`  |
| 1409   | Layout 6 | `ac532975a82d`  |
| 1405   | Layout 6 | `ac532975a82d`  |
| 1401   | Layout 6 | `ac532975a82d`  |
| 1396   | Layout 6 | `ac532975a82d`  |
| 1391   | Layout 6 | `ac532975a82d`  |
| 1390   | Layout 6 | `ac532975a82d`  |
| 1386   | Layout 6 | `ac532975a82d`  |
| 1381   | Layout 6 | `ac532975a82d`  |
| 1379   | Layout 6 | `ac532975a82d`  |
| 1372   | Layout 6 | `ac532975a82d`  |
| 1366   | Layout 6 | `ac532975a82d`  |
| 1364   | Layout 6 | `ac532975a82d`  |
| 1363   | Layout 6 | `ac532975a82d`  |
| 1360   | Layout 6 | `ac532975a82d`  |
| 1358   | Layout 6 | `ac532975a82d`  |
| 1355   | Layout 6 | `ac532975a82d`  |
| 1351   | Layout 6 | `ac532975a82d`  |
| 1348   | Layout 6 | `ac532975a82d`  |
| 1346   | Layout 6 | `ac532975a82d`  |
| 1341   | Layout 6 | `ac532975a82d`  |
| 1340   | Layout 6 | `ac532975a82d`  |
| 1338   | Layout 6 | `ac532975a82d`  |
| 1335   | Layout 6 | `ac532975a82d`  |
| 1333   | Layout 6 | `ac532975a82d`  |
| 1329   | Layout 6 | `ac532975a82d`  |
| 1327   | Layout 6 | `ac532975a82d`  |
| 1324   | Layout 6 | `ac532975a82d`  |
| 1321   | Layout 6 | `ac532975a82d`  |
| 1319   | Layout 6 | `ac532975a82d`  |
| 1318   | Layout 6 | `ac532975a82d`  |
| 1316   | Layout 6 | `ac532975a82d`  |
| 1313   | Layout 6 | `ac532975a82d`  |
| 1311   | Layout 6 | `ac532975a82d`  |
| 1309   | Layout 6 | `ac532975a82d`  |
| 1304   | Layout 6 | `ac532975a82d`  |
| 1292   | Layout 6 | `ac532975a82d`  |
| 1286   | Layout 6 | `ac532975a82d`  |
| 1280   | Layout 6 | `ac532975a82d`  |
| 1276   | Layout 6 | `ac532975a82d`  |
| 1267   | Layout 5 | `ac532975a82d`  |
| 1261   | Layout 5 | `ac532975a82d`  |
| 1256   | Layout 5 | `ac532975a82d`  |
| 1250   | Layout 5 | `ac532975a82d`  |
| 1246   | Layout 5 | `ac532975a82d`  |
| 1239   | Layout 5 | `ac532975a82d`  |
| 1230   | Layout 5 | `ac532975a82d`  |
| 1226   | Layout 5 | `ac532975a82d`  |
| 1220   | Layout 5 | `ac532975a82d`  |
| 1217   | Layout 5 | `ac532975a82d`  |
| 1211   | Layout 5 | `ac532975a82d`  |
| 1210   | Layout 5 | `ac532975a82d`  |
| 1208   | Layout 5 | `ac532975a82d`  |
| 1203   | Layout 5 | `ac532975a82d`  |
| 1197   | Layout 5 | `ac532975a82d`  |
| 1194   | Layout 5 | `ac532975a82d`  |
| 1192   | Layout 5 | `ac532975a82d`  |
| 1187   | Layout 5 | `ac532975a82d`  |
| 1183   | Layout 5 | `ac532975a82d`  |
| 1177   | Layout 5 | `ac532975a82d`  |
| 1173   | Layout 5 | `ac532975a82d`  |
| 1167   | Layout 5 | `ac532975a82d`  |
| 1164   | Layout 5 | `ac532975a82d`  |
| 1156   | Layout 5 | `ac532975a82d`  |
| 1149   | Layout 5 | `ac532975a82d`  |
| 1144   | Layout 5 | `ac532975a82d`  |
| 1137   | Layout 5 | `ac532975a82d`  |
| 1132   | Layout 5 | `ac532975a82d`  |
| 1127   | Layout 5 | `ac532975a82d`  |
| 1122   | Layout 5 | `ac532975a82d`  |
| 1118   | Layout 5 | `ac532975a82d`  |
| 1114   | Layout 5 | `ac532975a82d`  |
| 1109   | Layout 5 | `ac532975a82d`  |
| 1102   | No file  | `ac532975a82d`  |
| 1096   | No file  | `ac532975a82d`  |
| 1088   | No file  | `ac532975a82d`  |
| 1081   | No file  | `ac532975a82d`  |
| 1076   | No file  | `ac532975a82d`  |
| 1069   | No file  | `ac532975a82d`  |
| 1064   | No file  | `ac532975a82d`  |
| 1058   | No file  | `ac532975a82d`  |
| 1051   | No file  | `ac532975a82d`  |
| 1044   | No file  | `ac532975a82d`  |
| 1036   | No file  | `ac532975a82d`  |
| 1026   | No file  | `ac532975a82d`  |
| 1016   | No file  | `ac532975a82d`  |
| 1009   | No file  | `ac532975a82d`  |
| 1005   | No file  | `ac532975a82d`  |
| 1000   | No file  | `ac532975a82d`  |
| 998    | No file  | `ac532975a82d`  |
| 990    | No file  | `ac532975a82d`  |
| 979    | No file  | `ac532975a82d`  |
| 972    | No file  | `ac532975a82d`  |
| 963    | No file  | `ac532975a82d`  |
| 955    | No file  | `ac532975a82d`  |
| 946    | No file  | `ac532975a82d`  |
| 938    | No file  | `ac532975a82d`  |
| 927    | No file  | `ac532975a82d`  |
| 911    | No file  | `ac532975a82d`  |
| 904    | No file  | `ac532975a82d`  |
| 899    | No file  | `ac532975a82d`  |
| 894    | No file  | `ac532975a82d`  |
| 885    | No file  | `ac532975a82d`  |
| 879    | No file  | `ac532975a82d`  |
| 872    | No file  | `ac532975a82d`  |
| 864    | No file  | `ac532975a82d`  |
| 855    | No file  | `ac532975a82d`  |
| 853    | No file  | `ac532975a82d`  |
| 845    | No file  | `ac532975a82d`  |
| 837    | No file  | `ac532975a82d`  |
| 829    | Layout 5 | `ac532975a82d`  |
| 822    | Layout 5 | `ac532975a82d`  |
| 814    | Layout 5 | `ac532975a82d`  |
| 805    | Layout 5 | `ac532975a82d`  |
| 794    | Layout 4 | `ac532975a82d`  |
| 787    | Layout 4 | `ac532975a82d`  |
| 780    | Layout 4 | `ac532975a82d`  |
| 771    | Layout 4 | `ac532975a82d`  |
| 760    | Layout 4 | `ac532975a82d`  |
| 748    | Layout 4 | `ac532975a82d`  |
| 741    | Layout 4 | `ac532975a82d`  |
| 736    | Layout 4 | `ac532975a82d`  |
| 731    | Layout 4 | `ac532975a82d`  |
| 723    | Layout 4 | `ac532975a82d`  |
| 711    | Layout 3 | `ac532975a82d`  |
| 707    | Layout 3 | `ac532975a82d`  |
| 697    | Layout 3 | `ac532975a82d`  |
| 689    | Layout 3 | `ac532975a82d`  |
| 683    | Layout 3 | `ac532975a82d`  |
| 678    | Layout 3 | `ac532975a82d`  |
| 670    | Layout 3 | `ac532975a82d`  |
| 661    | Layout 3 | `ac532975a82d`  |
| 656    | Layout 3 | `ac532975a82d`  |
| 652    | Layout 3 | `ac532975a82d`  |
| 643    | Layout 3 | `ac532975a82d`  |
| 637    | Layout 3 | `ac532975a82d`  |
| 630    | Layout 3 | `ac532975a82d`  |
| 627    | Layout 3 | `ac532975a82d`  |
| 621    | Layout 3 | `ac532975a82d`  |
| 617    | Layout 3 | `ac532975a82d`  |
| 615    | Layout 3 | `ac532975a82d`  |
| 606    | Layout 3 | `ac532975a82d`  |
| 599    | Layout 3 | `ac532975a82d`  |
| 592    | Layout 3 | `ac532975a82d`  |
| 586    | Layout 3 | `ac532975a82d`  |
| 577    | Layout 3 | `ac532975a82d`  |
| 569    | Layout 3 | `ac532975a82d`  |
| 561    | Layout 3 | `ac532975a82d`  |
| 554    | Layout 3 | `ac532975a82d`  |
| 542    | Layout 3 | `ac532975a82d`  |
| 532    | Layout 3 | `ac532975a82d`  |
| 531    | Layout 3 | `ac532975a82d`  |
| 526    | Layout 3 | `ac532975a82d`  |
| 521    | Layout 2 | `ac532975a82d`  |
| 517    | Layout 2 | `ac532975a82d`  |
| 510    | Layout 2 | `ac532975a82d`  |
| 508    | Layout 2 | `ac532975a82d`  |
| 504    | Layout 2 | `ac532975a82d`  |
| 497    | Layout 2 | `ac532975a82d`  |
| 491    | Layout 2 | `ac532975a82d`  |
| 485    | Layout 2 | `ac532975a82d`  |
| 478    | Layout 2 | `ac532975a82d`  |
| 472    | Layout 2 | `ac532975a82d`  |
| 466    | Layout 1 | `ac532975a82d`  |
| 457    | Layout 1 | `ac532975a82d`  |
| 452    | Layout 1 | `ac532975a82d`  |
| 449    | Layout 1 | `ac532975a82d`  |
| 435    | Layout 1 | `ac532975a82d`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                     |
| --------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | LOC type 12, `str_id1` = `territory_key`, `str_id4` 0 / 1 = nation or realm / territory name |
| `languagedata_en.loc` | Optional | LOC type 0 names of the booty items                                                      |

All multi-byte values are little-endian.

## Layout 9

### File Layout

The shared PABR string table layout (`_common/pabr_strings.py`).

| Offset              | Type                 | Field        | Notes                                          |
| ------------------- | -------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                  | count        | Number of rows; 14 on client 3458              |
| `+0x08`             | Territory Row[count] | rows         | Byte-packed; see Territory Row                 |
| `rows+0x00`         | String Table         | string_table | See String Table                               |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                  | zero         | Always 0                                       |

A row is `80 + 4 * (booty_item_count + territory_supply_key_count)` bytes.
The rows tile `[0x08, table_start)` exactly (12 rows of 88 bytes and 2 of 92
on client 3458), so a parser walks them in order and fails when they do not
end at `table_start`.

### Territory Row (variable: 80 bytes + lists)

| Offset                       | Type                              | Field                      | Notes                                                                                  |
| ---------------------------- | --------------------------------- | -------------------------- | -------------------------------------------------------------------------------------- |
| `+0x00`                      | u16                               | territory_key              | 0 to 13, equal to the row index; LOC type 12 `str_id1`                                 |
| `+0x02`                      | u8                                | is_king_territory_only     | `1` on Calpheon to Outer Edania, `0` on Balenos, Serendia and Inner Edania             |
| `+0x03`                      | u8                                | is_lord_territory_only     | `1` on Balenos and Serendia only, the two names ending in 자치령 (autonomous territory) |
| `+0x04`                      | f32[3]                            | occupying_tent_position    | World `x, y, z` of the occupying tent; all zero when unused |
| `+0x10`                      | f32[3]                            | volunteer_attack_position  | World `x, y, z` of the militia attack respawn point; all zero when unused |
| `+0x1C`                      | f32[3]                            | volunteer_defense_position | World `x, y, z` of the militia defense respawn point; all zero when unused |
| `+0x28`                      | u32                               | national_key               | Same value on every territory of one nation, different between nations |
| `+0x2C`                      | u32                               | nation_ref                 | String table index of the Korean nation or realm name                                  |
| `+0x30`                      | u32                               | name_ref                   | String table index of the Korean territory name                                        |
| `+0x34`                      | u32                               | icon_large_ref             | String table index of the large world map mark, relative to `ui_texture/`              |
| `+0x38`                      | u32                               | icon_small_ref             | String table index of the small world map mark, relative to `ui_texture/`              |
| `+0x3C`                      | u64                               | booty_item_count           | Entries in `booty_item_ids`; `2` on every row on client 3473                           |
| `+0x44`                      | u32[booty_item_count]             | booty_item_ids             | Items the territory's lord receives (LOC type 0): the conquest crown, then its armor   |
| `booty_item_ids+0x00`        | u64                               | territory_supply_key_count | Entries in `territory_supply_keys`; `1` on Serendia and Mediah, `0` elsewhere on client 3473 |
| `booty_item_ids+0x08`        | u32[territory_supply_key_count]   | territory_supply_keys      | Territory supply group keys: `114` on Serendia, `312` on Mediah on client 3473         |
| `territory_supply_keys+0x00` | u32                               | unknown_tail               | `0` on every row                                                                       |

Positions on client 3458: Calpheon, Mediah and Valencia fill all three,
Kamasylvia and O'dyllita only the first, the rest none. The occupying tent
and the militia defense position lie within about 20,000 units of a castle
node in `mapdata_realexplore2.bwp`: `calpheon_castle` (702), `mediacastle`
(1152), `valencia_castle` (1342) and `othilita_castle` (1692). Valencia's
militia attack position sits next to `ruins of castle valencia` (1374).

Booty items: Balenos to Mediah each have their own crown and armor (Silver
Mane, Blue Lion, Golden Eagle, Asula); Valencia and every later territory
store the Crown of Aal (23385) and Armor of Aal (23390).

### String Table (variable: 4 bytes + strings)

46 strings on client 3458, all referenced. The territories of one nation
share its nation entry (Republic of Calpheon, Alyaelli), and where nation and
territory names match (The Great Ocean, Kamasylvia and the other single
territory realms) both refs point at one entry. The Great Ocean (territory 5) stores Valencia's marks under
`New_UI_Common_forLua/Widget/WorldMap/territory/`; every other icon is under
`Renewal/ETC/WordMap/`. Paths keep mixed case, so the handler lowercases them.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 46 on client 3458   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Layout 8

The territory supply keys are u16 values. Only the Territory Row differs
from Layout 9.

### Territory Row (variable: 80 bytes + lists)

| Offset                       | Type                            | Field                      | Notes |
| ---------------------------- | ------------------------------- | -------------------------- | ----- |
| `+0x00`                      | u16                             | territory_key              |       |
| `+0x02`                      | u8                              | is_king_territory_only     |       |
| `+0x03`                      | u8                              | is_lord_territory_only     |       |
| `+0x04`                      | f32[3]                          | occupying_tent_position    |       |
| `+0x10`                      | f32[3]                          | volunteer_attack_position  |       |
| `+0x1C`                      | f32[3]                          | volunteer_defense_position |       |
| `+0x28`                      | u32                             | national_key               |       |
| `+0x2C`                      | u32                             | nation_ref                 |       |
| `+0x30`                      | u32                             | name_ref                   |       |
| `+0x34`                      | u32                             | icon_large_ref             |       |
| `+0x38`                      | u32                             | icon_small_ref             |       |
| `+0x3C`                      | u64                             | booty_item_count           |       |
| `+0x44`                      | u32[booty_item_count]           | booty_item_ids             |       |
| `booty_item_ids+0x00`        | u64                             | territory_supply_key_count |       |
| `booty_item_ids+0x08`        | u16[territory_supply_key_count] | territory_supply_keys      | `114` on Serendia, `312` on Mediah on client 2717 |
| `territory_supply_keys+0x00` | u32                             | unknown_tail               | `0` on every row on client 2717 |

## Layout 7

A u16 list of territory trade keys sits before the territory supply keys.
Only the Territory Row differs from Layout 8. On client 2474 Balenos to
Mediah hold 5 trade keys each and the rest none.

### Territory Row (variable: 88 bytes + lists)

| Offset                       | Type                            | Field                      | Notes |
| ---------------------------- | ------------------------------- | -------------------------- | ----- |
| `+0x00`                      | u16                             | territory_key              |       |
| `+0x02`                      | u8                              | is_king_territory_only     |       |
| `+0x03`                      | u8                              | is_lord_territory_only     |       |
| `+0x04`                      | f32[3]                          | occupying_tent_position    |       |
| `+0x10`                      | f32[3]                          | volunteer_attack_position  |       |
| `+0x1C`                      | f32[3]                          | volunteer_defense_position |       |
| `+0x28`                      | u32                             | national_key               |       |
| `+0x2C`                      | u32                             | nation_ref                 |       |
| `+0x30`                      | u32                             | name_ref                   |       |
| `+0x34`                      | u32                             | icon_large_ref             |       |
| `+0x38`                      | u32                             | icon_small_ref             |       |
| `+0x3C`                      | u64                             | booty_item_count           |       |
| `+0x44`                      | u32[booty_item_count]           | booty_item_ids             |       |
| `booty_item_ids+0x00`        | u64                             | territory_trade_key_count  | Entries in `territory_trade_keys` |
| `booty_item_ids+0x08`        | u16[territory_trade_key_count]  | territory_trade_keys       | Territory trade group keys: Balenos holds `5` to `1`, Serendia `105` to `101` |
| `territory_trade_keys+0x00`  | u64                             | territory_supply_key_count |       |
| `territory_trade_keys+0x08`  | u16[territory_supply_key_count] | territory_supply_keys      |       |
| `territory_supply_keys+0x00` | u32                             | unknown_tail               |       |

## Layout 6

A Territory Row holds five positions instead of three, which moves
`national_key` to `+0x40`. Only the Territory Row differs from Layout 7. On
client 1784 the file holds 10 rows; Balenos to Mediah have 5 trade keys and
the rest none, and every territory has 0 to 5 supply keys.

### Territory Row (variable: 112 bytes + lists)

| Offset                       | Type                            | Field                      | Notes                                                          |
| ---------------------------- | ------------------------------- | -------------------------- | -------------------------------------------------------------- |
| `+0x00`                      | u16                             | territory_key              | Client 1276 opens with territory 8, then 0 to 7               |
| `+0x02`                      | u8                              | is_king_territory_only     |                                                                |
| `+0x03`                      | u8                              | is_lord_territory_only     |                                                                |
| `+0x04`                      | f32[3]                          | occupying_tent_position    |                                                                |
| `+0x10`                      | f32[3]                          | volunteer_attack_position  |                                                                |
| `+0x1C`                      | f32[3]                          | volunteer_defense_position |                                                                |
| `+0x28`                      | f32[3]                          | plunder_attack_position    | World `x, y, z` of the plunder war attack respawn point        |
| `+0x34`                      | f32[3]                          | plunder_defense_position   | World `x, y, z` of the plunder war defense respawn point       |
| `+0x40`                      | u32                             | national_key               |                                                                |
| `+0x44`                      | u32                             | nation_ref                 |                                                                |
| `+0x48`                      | u32                             | name_ref                   |                                                                |
| `+0x4C`                      | u32                             | icon_large_ref             |                                                                |
| `+0x50`                      | u32                             | icon_small_ref             |                                                                |
| `+0x54`                      | u64                             | booty_item_count           |                                                                |
| `+0x5C`                      | u32[booty_item_count]           | booty_item_ids             |                                                                |
| `booty_item_ids+0x00`        | u64                             | territory_trade_key_count  |                                                                |
| `booty_item_ids+0x08`        | u16[territory_trade_key_count]  | territory_trade_keys       |                                                                |
| `territory_trade_keys+0x00`  | u64                             | territory_supply_key_count |                                                                |
| `territory_trade_keys+0x08`  | u16[territory_supply_key_count] | territory_supply_keys      | Balenos holds `11` to `15`, Serendia `113`, `112`, `111`, `114`, `115` |
| `territory_supply_keys+0x00` | u32                             | unknown_tail               | `0` on every row on client 1784                                |

## Layout 5

A Territory Row ends with its territory supply keys: there is no
`unknown_tail`. Only the Territory Row differs from Layout 6.

### Territory Row (variable: 108 bytes + lists)

| Offset                      | Type                            | Field                      | Notes |
| --------------------------- | ------------------------------- | -------------------------- | ----- |
| `+0x00`                     | u16                             | territory_key              | Clients 1109 to 1267 open with territory 8, then 0 to 7 |
| `+0x02`                     | u8                              | is_king_territory_only     |       |
| `+0x03`                     | u8                              | is_lord_territory_only     |       |
| `+0x04`                     | f32[3]                          | occupying_tent_position    |       |
| `+0x10`                     | f32[3]                          | volunteer_attack_position  |       |
| `+0x1C`                     | f32[3]                          | volunteer_defense_position |       |
| `+0x28`                     | f32[3]                          | plunder_attack_position    |       |
| `+0x34`                     | f32[3]                          | plunder_defense_position   |       |
| `+0x40`                     | u32                             | national_key               |       |
| `+0x44`                     | u32                             | nation_ref                 |       |
| `+0x48`                     | u32                             | name_ref                   |       |
| `+0x4C`                     | u32                             | icon_large_ref             |       |
| `+0x50`                     | u32                             | icon_small_ref             |       |
| `+0x54`                     | u64                             | booty_item_count           |       |
| `+0x5C`                     | u32[booty_item_count]           | booty_item_ids             |       |
| `booty_item_ids+0x00`       | u64                             | territory_trade_key_count  |       |
| `booty_item_ids+0x08`       | u16[territory_trade_key_count]  | territory_trade_keys       |       |
| `territory_trade_keys+0x00` | u64                             | territory_supply_key_count |       |
| `territory_trade_keys+0x08` | u16[territory_supply_key_count] | territory_supply_keys      |       |

## Layout 4

No PABR header and no string table: the file opens with the row count, and
each row holds its names and icon paths inline as `str16`. The rows run to
the end of the file. In Layouts 1 to 4 the strings are Korean in the
`gamecommondata/binary/` copy (client 472) and English in the
`gamecommondata/binary/en/` copy (client 794), and every icon path is
under `New_UI_Common_forLua/Widget/WorldMap/territory/`.

### File Layout

| Offset  | Type                 | Field | Notes                          |
| ------- | -------------------- | ----- | ------------------------------ |
| `+0x00` | u32                  | count | Number of rows                 |
| `+0x04` | Territory Row[count] | rows  | Byte-packed; see Territory Row |

### Territory Row (variable: 124 bytes + strings and lists)

| Offset                      | Type                            | Field                      | Notes |
| --------------------------- | ------------------------------- | -------------------------- | ----- |
| `+0x00`                     | u16                             | territory_key              |       |
| `+0x02`                     | u8                              | is_king_territory_only     |       |
| `+0x03`                     | u8                              | is_lord_territory_only     |       |
| `+0x04`                     | f32[3]                          | occupying_tent_position    |       |
| `+0x10`                     | f32[3]                          | volunteer_attack_position  |       |
| `+0x1C`                     | f32[3]                          | volunteer_defense_position |       |
| `+0x28`                     | f32[3]                          | plunder_attack_position    |       |
| `+0x34`                     | f32[3]                          | plunder_defense_position   |       |
| `+0x40`                     | u32                             | national_key               |       |
| `+0x44`                     | str16                           | nation_name                | Nation or realm name |
| `nation_name+0x00`          | str16                           | territory_name             | Territory name |
| `territory_name+0x00`       | str16                           | icon_large_path            | Large world map mark, relative to `ui_texture/` |
| `icon_large_path+0x00`      | str16                           | icon_small_path            | Small world map mark, relative to `ui_texture/` |
| `icon_small_path+0x00`      | u64                             | booty_item_count           |       |
| `icon_small_path+0x08`      | u32[booty_item_count]           | booty_item_ids             |       |
| `booty_item_ids+0x00`       | u64                             | territory_trade_key_count  |       |
| `booty_item_ids+0x08`       | u16[territory_trade_key_count]  | territory_trade_keys       |       |
| `territory_trade_keys+0x00` | u64                             | territory_supply_key_count |       |
| `territory_trade_keys+0x08` | u16[territory_supply_key_count] | territory_supply_keys      |       |

## Layout 3

A Territory Row holds three positions, the first three of Layout 4. Only
the Territory Row differs from Layout 4.

### Territory Row (variable: 100 bytes + strings and lists)

| Offset                      | Type                            | Field                      | Notes |
| --------------------------- | ------------------------------- | -------------------------- | ----- |
| `+0x00`                     | u16                             | territory_key              |       |
| `+0x02`                     | u8                              | is_king_territory_only     |       |
| `+0x03`                     | u8                              | is_lord_territory_only     |       |
| `+0x04`                     | f32[3]                          | occupying_tent_position    |       |
| `+0x10`                     | f32[3]                          | volunteer_attack_position  |       |
| `+0x1C`                     | f32[3]                          | volunteer_defense_position |       |
| `+0x28`                     | u32                             | national_key               |       |
| `+0x2C`                     | str16                           | nation_name                |       |
| `nation_name+0x00`          | str16                           | territory_name             |       |
| `territory_name+0x00`       | str16                           | icon_large_path            |       |
| `icon_large_path+0x00`      | str16                           | icon_small_path            |       |
| `icon_small_path+0x00`      | u64                             | booty_item_count           |       |
| `icon_small_path+0x08`      | u32[booty_item_count]           | booty_item_ids             |       |
| `booty_item_ids+0x00`       | u64                             | territory_trade_key_count  |       |
| `booty_item_ids+0x08`       | u16[territory_trade_key_count]  | territory_trade_keys       |       |
| `territory_trade_keys+0x00` | u64                             | territory_supply_key_count |       |
| `territory_trade_keys+0x08` | u16[territory_supply_key_count] | territory_supply_keys      |       |

## Layout 2

The three list counts are u32. Only the Territory Row differs from Layout 3.

### Territory Row (variable: 88 bytes + strings and lists)

| Offset                      | Type                            | Field                      | Notes |
| --------------------------- | ------------------------------- | -------------------------- | ----- |
| `+0x00`                     | u16                             | territory_key              |       |
| `+0x02`                     | u8                              | is_king_territory_only     |       |
| `+0x03`                     | u8                              | is_lord_territory_only     |       |
| `+0x04`                     | f32[3]                          | occupying_tent_position    |       |
| `+0x10`                     | f32[3]                          | volunteer_attack_position  |       |
| `+0x1C`                     | f32[3]                          | volunteer_defense_position |       |
| `+0x28`                     | u32                             | national_key               |       |
| `+0x2C`                     | str16                           | nation_name                |       |
| `nation_name+0x00`          | str16                           | territory_name             |       |
| `territory_name+0x00`       | str16                           | icon_large_path            |       |
| `icon_large_path+0x00`      | str16                           | icon_small_path            |       |
| `icon_small_path+0x00`      | u32                             | booty_item_count           |       |
| `icon_small_path+0x04`      | u32[booty_item_count]           | booty_item_ids             |       |
| `booty_item_ids+0x00`       | u32                             | territory_trade_key_count  |       |
| `booty_item_ids+0x04`       | u16[territory_trade_key_count]  | territory_trade_keys       |       |
| `territory_trade_keys+0x00` | u32                             | territory_supply_key_count |       |
| `territory_trade_keys+0x04` | u16[territory_supply_key_count] | territory_supply_keys      |       |

## Layout 1

A Territory Row holds one position, the occupying tent, which moves
`national_key` to `+0x10`. Only the Territory Row differs from Layout 2. On
client 435 the file holds 7 rows (Balenos to Kamasylvia) and only Calpheon,
Mediah and Valencia fill the position.

### Territory Row (variable: 64 bytes + strings and lists)

| Offset                      | Type                            | Field                      | Notes |
| --------------------------- | ------------------------------- | -------------------------- | ----- |
| `+0x00`                     | u16                             | territory_key              |       |
| `+0x02`                     | u8                              | is_king_territory_only     |       |
| `+0x03`                     | u8                              | is_lord_territory_only     |       |
| `+0x04`                     | f32[3]                          | occupying_tent_position    |       |
| `+0x10`                     | u32                             | national_key               |       |
| `+0x14`                     | str16                           | nation_name                |       |
| `nation_name+0x00`          | str16                           | territory_name             |       |
| `territory_name+0x00`       | str16                           | icon_large_path            |       |
| `icon_large_path+0x00`      | str16                           | icon_small_path            |       |
| `icon_small_path+0x00`      | u32                             | booty_item_count           |       |
| `icon_small_path+0x04`      | u32[booty_item_count]           | booty_item_ids             |       |
| `booty_item_ids+0x00`       | u32                             | territory_trade_key_count  |       |
| `booty_item_ids+0x04`       | u16[territory_trade_key_count]  | territory_trade_keys       |       |
| `territory_trade_keys+0x00` | u32                             | territory_supply_key_count |       |
| `territory_trade_keys+0x04` | u16[territory_supply_key_count] | territory_supply_keys      |       |

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its
`gc::TerritoryInfo` holds `_territoryKey` (i16), `_isKingTerritoryOnly`,
`_isLordTerritoryOnly`, `_occupyingTentPosition`, three members filled at
load time (`_mainTownRegion`, `_capitalTownRegion`, `_affliatedRegionGroups`),
`_nationalKey` (u32), `_nationalName`, `_territoryName`, `_territoryImage`,
`_territorySmallImage`, `_bootyItemKeyList` (a vector of i32),
`_bootyItemList` (a vector of `gc::Item`), and four vectors of u16 keys:
`_territoryTradeList`, `_territorySupplyList`, `_territoryTradeKeyList` and
`_territorySupplyKeyList`. Layout 1 (client 435, 2017-05) stores
`_territoryKey` to `_occupyingTentPosition`, `_nationalKey` to
`_territorySmallImage` (inline), `_bootyItemKeyList`, `_territoryTradeKeyList`
and `_territorySupplyKeyList` in this order, with one position as the 2016
struct. Layouts 4 to 6 hold five positions, and Layout 6 adds `unknown_tail`
after the last list.

`Territory_Table` in a private server's `DataSheets.bexcel` on client 1784
(and the same sheet in its `.xlsm`, and in a second private server's database
on client 519) has the columns `TerritoryKey`, `NationalName`,
`TerritoryName`, `TerritoryImage`, `TerritorySmallImage`,
`OccupyingTentPositionX` to `Z`, `BootyItem`, `WorldMapColor`,
`VolunteerAttackX` to `Z`, `VolunteerDefenseX` to `Z`, `PlunderAttackX` to
`Z` and `PlunderDefenseX` to `Z`. The sheet shares territory keys 0 to 9 with
both clients:

| Column | Field | Equal (client 1784, 10 keys) | Equal (client 3473, 10 keys) |
| ------ | ----- | ---------------------------- | ---------------------------- |
| `OccupyingTentPositionX` to `Z` | `occupying_tent_position` | 10 | 8 |
| `VolunteerAttackX` to `Z` | `volunteer_attack_position` | 10 | 10 |
| `VolunteerDefenseX` to `Z` | `volunteer_defense_position` | 10 | 10 |
| `PlunderAttackX` to `Z` | `plunder_attack_position` | 10 | |
| `PlunderDefenseX` to `Z` | `plunder_defense_position` | 10 | |
| `BootyItem` | `booty_item_ids` | 10 | 10 |

Calpheon, Mediah and Valencia fill every position column; the other rows
are zero in both. The two client 3473 tent mismatches are Kamasylvia and
O'dyllita, which the sheet leaves at zero. The
sheet comments call the volunteer columns the militia (민병대) siege attack
and defense respawn points, the plunder columns the plunder war (약탈전)
respawn points, and `BootyItem` the items given to the occupying lord, at
enchant level 0 and count 1. `WorldMapColor` has no bytes in any layout.

The two lists come from `TerritoryTradeItemList_Table` (columns
`TerritoryKey`, `ItemGroupKeyType`, `ItemMainGruopKey`, `TerritoryGroupKey`).
Its comment gives `ItemGroupKeyType` `0` as territory trade (영지 무역) and
`1` as territory supply (영지 납품). On client 1784 each list holds the
`TerritoryGroupKey` values of the territory's rows of one type, in sheet
order: the first list type `0` on 4 of the 4 territories that have such
rows, the second type `1` on 6 of the 9. Valencia and The Great Ocean keep
their first 4 of 5 and 6 rows, and O'dyllita stores none of its one row
(`415`, `515`, `516` and `811` are missing). Neither list holds `ItemMainGruopKey` values, so the names follow the 2016
`_territoryTradeKeyList` and `_territorySupplyKeyList`. Client 3473 has one
list, and its keys `114` (Serendia) and `312` (Mediah) are type `1` rows of
those territories. `TerritorySupply` is the NPC role the client labels
Imperial Delivery (see [characterspawntype](characterspawntype_dbss.md)).

`is_king_territory_only` has no sheet column and is named from its place in
the 2016 member order, between the matched `territory_key` and the occupying
tent position. The client Lua calls `siegeWrapper:isKingTerritoryOnly()` in
`panel_window_lordmenu_all_1.luac`, where `isKing()` and
`isKingTerritoryOnly()` together decide whether the lord menu shows its
first two local tax sliders. The next 2016 bool, `_isLordTerritoryOnly`, is
`is_lord_territory_only`, set on the two autonomous territories. `national_key` is the 2016
`_nationalKey`; the sheet has no column for it. The position fields take the
sheet's column names; the 2016 struct has only `_occupyingTentPosition`.

## Notes

- iDevelopThings' [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  documents the same layout (FORMATS.md, section 10), with
  `is_king_territory_only` as a primary-territory flag and the positions as
  world map marks.
- bdo-data-extractor reads a territory index in each `regioninfo.bss` region
  that joins this file and LOC type 12.
- The `territory_key` of `dropuimaincategoryinfo.bss` (see
  [dropuihuntinggroundinfo](dropuihuntinggroundinfo_bss.md)) is the same LOC
  type 12 key.
- A territory supply key is the territory key times 100 plus 11 to 16 in the
  sheet; the trade keys are the territory key times 100 plus 1 to 5.
- The handler's Lord Territory and King Territory column labels are my own
  translations of the 2016 `_isLordTerritoryOnly` and `_isKingTerritoryOnly`,
  in every language. The client LOC has no term for either flag: the English
  territory names are plain ("Balenos", "Serendia"), and the only English LOC
  string with "autonomous" is "Drieghan Autonomous Region". The Korean names
  of the two lord territories end in 자치령 (autonomous territory), which the
  English client does not show, so the column does not use that word.

## Open Questions

### What `unknown_tail` Holds

Layouts 6 to 9 end a row with a u32 that is `0` on every row of clients
1276, 1784 and 2468, of every client from 2474 to 2726, and of client 3473.
Layouts 1 to 5 end with the supply keys, as the 2016
`gc::TerritoryInfo` ends with `_territorySupplyKeyList`, and no
`Territory_Table` column is left over except `WorldMapColor`, whose RGBA
values are not zero.
