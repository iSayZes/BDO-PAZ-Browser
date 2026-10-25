# `treasureinfostaicstatusmanager.bss` Format

## Purpose

The treasures of the treasure guidebook window
(`panel_window_treasure_guidebook_all_1.luac`). A PABR file with one row
per treasure item: its puzzle, a GAME sheet key of its description, the
core material items, the quest that leads to it, the texture of its
picture and a hunting flag. On client 3482 it holds six treasures:
Archaeologist's Map, Rich Merchant's Ring, Lafi Bedmountain's Upgraded
Compass, Lafi Bedmountain's Upgraded Telescope, Ebenruth's Nol and
Krogdalo's Sanctuary.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                 | Bytes | Records | Row bytes               |
| ------ | -------------- | ------------------------------------ | ----- | ------- | ----------------------- |
| 1      | 3458 and later | `treasureinfostaicstatusmanager.bss` | 1,232 | 6 Row   | 23 to 43, 34 on average |

| Layout | File                                 | Known            | Unknown    |
| ------ | ------------------------------------ | ---------------- | ---------- |
| 1      | `treasureinfostaicstatusmanager.bss` | 1,232 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e9726f7c2e87`  |
| 3482   | Layout 1 | `e9726f7c2e87`  |
| 3474   | Layout 1 | `e9726f7c2e87`  |
| 3473   | Layout 1 | `e9726f7c2e87`  |
| 3464   | Layout 1 | `e9726f7c2e87`  |
| 3458   | Layout 1 | `e9726f7c2e87`  |
| 3454   | No file  | `e9726f7c2e87`  |
| 3444   | No file  | `e9726f7c2e87`  |
| 3435   | No file  | `e9726f7c2e87`  |
| 3426   | No file  | `e9726f7c2e87`  |
| 3418   | No file  | `e9726f7c2e87`  |
| 3412   | No file  | `e9726f7c2e87`  |
| 3402   | No file  | `e9726f7c2e87`  |
| 3396   | No file  | `e9726f7c2e87`  |
| 3387   | No file  | `e9726f7c2e87`  |
| 3381   | No file  | `e9726f7c2e87`  |
| 3373   | No file  | `e9726f7c2e87`  |
| 3364   | No file  | `e9726f7c2e87`  |
| 3356   | No file  | `e9726f7c2e87`  |
| 3349   | No file  | `e9726f7c2e87`  |
| 3342   | No file  | `e9726f7c2e87`  |
| 3335   | No file  | `e9726f7c2e87`  |
| 3326   | No file  | `e9726f7c2e87`  |
| 3321   | No file  | `e9726f7c2e87`  |
| 3314   | No file  | `e9726f7c2e87`  |
| 3303   | No file  | `e9726f7c2e87`  |
| 3302   | No file  | `e9726f7c2e87`  |
| 3293   | No file  | `e9726f7c2e87`  |
| 3283   | No file  | `e9726f7c2e87`  |
| 3275   | No file  | `e9726f7c2e87`  |
| 3267   | No file  | `e9726f7c2e87`  |
| 3258   | No file  | `e9726f7c2e87`  |
| 3251   | No file  | `e9726f7c2e87`  |
| 3242   | No file  | `e9726f7c2e87`  |
| 3235   | No file  | `e9726f7c2e87`  |
| 3229   | No file  | `e9726f7c2e87`  |
| 3212   | No file  | `e9726f7c2e87`  |
| 3203   | No file  | `e9726f7c2e87`  |
| 3193   | No file  | `e9726f7c2e87`  |
| 3186   | No file  | `e9726f7c2e87`  |
| 3177   | No file  | `e9726f7c2e87`  |
| 3169   | No file  | `e9726f7c2e87`  |
| 3158   | No file  | `e9726f7c2e87`  |
| 3151   | No file  | `e9726f7c2e87`  |
| 3144   | No file  | `e9726f7c2e87`  |
| 3133   | No file  | `e9726f7c2e87`  |
| 3125   | No file  | `e9726f7c2e87`  |
| 3118   | No file  | `e9726f7c2e87`  |
| 3111   | No file  | `e9726f7c2e87`  |
| 3103   | No file  | `e9726f7c2e87`  |
| 3095   | No file  | `e9726f7c2e87`  |
| 3086   | No file  | `e9726f7c2e87`  |
| 3072   | No file  | `e9726f7c2e87`  |
| 3062   | No file  | `e9726f7c2e87`  |
| 3052   | No file  | `e9726f7c2e87`  |
| 3045   | No file  | `e9726f7c2e87`  |
| 3037   | No file  | `e9726f7c2e87`  |
| 3030   | No file  | `e9726f7c2e87`  |
| 3021   | No file  | `e9726f7c2e87`  |
| 3012   | No file  | `e9726f7c2e87`  |
| 3002   | No file  | `e9726f7c2e87`  |
| 2995   | No file  | `e9726f7c2e87`  |
| 2987   | No file  | `e9726f7c2e87`  |
| 2978   | No file  | `e9726f7c2e87`  |
| 2970   | No file  | `e9726f7c2e87`  |
| 2959   | No file  | `e9726f7c2e87`  |
| 2951   | No file  | `e9726f7c2e87`  |
| 2942   | No file  | `e9726f7c2e87`  |
| 2935   | No file  | `e9726f7c2e87`  |
| 2932   | No file  | `e9726f7c2e87`  |
| 2923   | No file  | `e9726f7c2e87`  |
| 2919   | No file  | `e9726f7c2e87`  |
| 2907   | No file  | `e9726f7c2e87`  |
| 2900   | No file  | `e9726f7c2e87`  |
| 2891   | No file  | `e9726f7c2e87`  |
| 2882   | No file  | `e9726f7c2e87`  |
| 2872   | No file  | `e9726f7c2e87`  |
| 2863   | No file  | `e9726f7c2e87`  |
| 2855   | No file  | `e9726f7c2e87`  |
| 2849   | No file  | `e9726f7c2e87`  |
| 2844   | No file  | `e9726f7c2e87`  |
| 2834   | No file  | `e9726f7c2e87`  |
| 2825   | No file  | `e9726f7c2e87`  |
| 2819   | No file  | `e9726f7c2e87`  |
| 2811   | No file  | `e9726f7c2e87`  |
| 2803   | No file  | `e9726f7c2e87`  |
| 2794   | No file  | `e9726f7c2e87`  |
| 2783   | No file  | `e9726f7c2e87`  |
| 2774   | No file  | `e9726f7c2e87`  |
| 2765   | No file  | `e9726f7c2e87`  |
| 2756   | No file  | `e9726f7c2e87`  |
| 2750   | No file  | `e9726f7c2e87`  |
| 2743   | No file  | `e9726f7c2e87`  |
| 2736   | No file  | `e9726f7c2e87`  |
| 2726   | No file  | `e9726f7c2e87`  |
| 2717   | No file  | `e9726f7c2e87`  |
| 2709   | No file  | `e9726f7c2e87`  |
| 2703   | No file  | `e9726f7c2e87`  |
| 2695   | No file  | `e9726f7c2e87`  |
| 2684   | No file  | `e9726f7c2e87`  |
| 2672   | No file  | `e9726f7c2e87`  |
| 2665   | No file  | `e9726f7c2e87`  |
| 2657   | No file  | `e9726f7c2e87`  |
| 2649   | No file  | `e9726f7c2e87`  |
| 2644   | No file  | `e9726f7c2e87`  |
| 2637   | No file  | `e9726f7c2e87`  |
| 2629   | No file  | `e9726f7c2e87`  |
| 2619   | No file  | `e9726f7c2e87`  |
| 2612   | No file  | `e9726f7c2e87`  |
| 2606   | No file  | `e9726f7c2e87`  |
| 2602   | No file  | `e9726f7c2e87`  |
| 2601   | No file  | `e9726f7c2e87`  |
| 2592   | No file  | `e9726f7c2e87`  |
| 2583   | No file  | `e9726f7c2e87`  |
| 2575   | No file  | `e9726f7c2e87`  |
| 2567   | No file  | `e9726f7c2e87`  |
| 2560   | No file  | `e9726f7c2e87`  |
| 2553   | No file  | `e9726f7c2e87`  |
| 2545   | No file  | `e9726f7c2e87`  |
| 2538   | No file  | `e9726f7c2e87`  |
| 2529   | No file  | `e9726f7c2e87`  |
| 2519   | No file  | `e9726f7c2e87`  |
| 2513   | No file  | `e9726f7c2e87`  |
| 2510   | No file  | `e9726f7c2e87`  |
| 2507   | No file  | `e9726f7c2e87`  |
| 2503   | No file  | `e9726f7c2e87`  |
| 2498   | No file  | `e9726f7c2e87`  |
| 2492   | No file  | `e9726f7c2e87`  |
| 2487   | No file  | `e9726f7c2e87`  |
| 2480   | No file  | `e9726f7c2e87`  |
| 2474   | No file  | `e9726f7c2e87`  |
| 2468   | No file  | `e9726f7c2e87`  |
| 2460   | No file  | `e9726f7c2e87`  |
| 2453   | No file  | `e9726f7c2e87`  |
| 2444   | No file  | `e9726f7c2e87`  |
| 2438   | No file  | `e9726f7c2e87`  |
| 2434   | No file  | `e9726f7c2e87`  |
| 2429   | No file  | `e9726f7c2e87`  |
| 2421   | No file  | `e9726f7c2e87`  |
| 2414   | No file  | `e9726f7c2e87`  |
| 2407   | No file  | `e9726f7c2e87`  |
| 2401   | No file  | `e9726f7c2e87`  |
| 2397   | No file  | `e9726f7c2e87`  |
| 2393   | No file  | `e9726f7c2e87`  |
| 2384   | No file  | `e9726f7c2e87`  |
| 2378   | No file  | `e9726f7c2e87`  |
| 2372   | No file  | `e9726f7c2e87`  |
| 2358   | No file  | `e9726f7c2e87`  |
| 2352   | No file  | `e9726f7c2e87`  |
| 2347   | No file  | `e9726f7c2e87`  |
| 2343   | No file  | `e9726f7c2e87`  |
| 2335   | No file  | `e9726f7c2e87`  |
| 2327   | No file  | `e9726f7c2e87`  |
| 2324   | No file  | `e9726f7c2e87`  |
| 2319   | No file  | `e9726f7c2e87`  |
| 2313   | No file  | `e9726f7c2e87`  |
| 2308   | No file  | `e9726f7c2e87`  |
| 2302   | No file  | `e9726f7c2e87`  |
| 2295   | No file  | `e9726f7c2e87`  |
| 2290   | No file  | `e9726f7c2e87`  |
| 2284   | No file  | `e9726f7c2e87`  |
| 2276   | No file  | `e9726f7c2e87`  |
| 2269   | No file  | `e9726f7c2e87`  |
| 2259   | No file  | `e9726f7c2e87`  |
| 2250   | No file  | `e9726f7c2e87`  |
| 2243   | No file  | `e9726f7c2e87`  |
| 2235   | No file  | `e9726f7c2e87`  |
| 2229   | No file  | `e9726f7c2e87`  |
| 2224   | No file  | `e9726f7c2e87`  |
| 2218   | No file  | `e9726f7c2e87`  |
| 2215   | No file  | `e9726f7c2e87`  |
| 2207   | No file  | `e9726f7c2e87`  |
| 2203   | No file  | `e9726f7c2e87`  |
| 2196   | No file  | `e9726f7c2e87`  |
| 2192   | No file  | `e9726f7c2e87`  |
| 2189   | No file  | `e9726f7c2e87`  |
| 2183   | No file  | `e9726f7c2e87`  |
| 2179   | No file  | `e9726f7c2e87`  |
| 2171   | No file  | `e9726f7c2e87`  |
| 2163   | No file  | `e9726f7c2e87`  |
| 2156   | No file  | `e9726f7c2e87`  |
| 2151   | No file  | `e9726f7c2e87`  |
| 2147   | No file  | `e9726f7c2e87`  |
| 2142   | No file  | `e9726f7c2e87`  |
| 2138   | No file  | `e9726f7c2e87`  |
| 2134   | No file  | `e9726f7c2e87`  |
| 2130   | No file  | `e9726f7c2e87`  |
| 2122   | No file  | `e9726f7c2e87`  |
| 2107   | No file  | `e9726f7c2e87`  |
| 2098   | No file  | `e9726f7c2e87`  |
| 2089   | No file  | `e9726f7c2e87`  |
| 2081   | No file  | `e9726f7c2e87`  |
| 2073   | No file  | `e9726f7c2e87`  |
| 2067   | No file  | `e9726f7c2e87`  |
| 2063   | No file  | `e9726f7c2e87`  |
| 2059   | No file  | `e9726f7c2e87`  |
| 2052   | No file  | `e9726f7c2e87`  |
| 2044   | No file  | `e9726f7c2e87`  |
| 2039   | No file  | `e9726f7c2e87`  |
| 2032   | No file  | `e9726f7c2e87`  |
| 2025   | No file  | `e9726f7c2e87`  |
| 2011   | No file  | `e9726f7c2e87`  |
| 2005   | No file  | `e9726f7c2e87`  |
| 2000   | No file  | `e9726f7c2e87`  |
| 1996   | No file  | `e9726f7c2e87`  |
| 1991   | No file  | `e9726f7c2e87`  |
| 1985   | No file  | `e9726f7c2e87`  |
| 1980   | No file  | `e9726f7c2e87`  |
| 1969   | No file  | `e9726f7c2e87`  |
| 1964   | No file  | `e9726f7c2e87`  |
| 1958   | No file  | `e9726f7c2e87`  |
| 1950   | No file  | `e9726f7c2e87`  |
| 1945   | No file  | `e9726f7c2e87`  |
| 1937   | No file  | `e9726f7c2e87`  |
| 1933   | No file  | `e9726f7c2e87`  |
| 1927   | No file  | `e9726f7c2e87`  |
| 1921   | No file  | `e9726f7c2e87`  |
| 1914   | No file  | `e9726f7c2e87`  |
| 1908   | No file  | `e9726f7c2e87`  |
| 1897   | No file  | `e9726f7c2e87`  |
| 1892   | No file  | `e9726f7c2e87`  |
| 1886   | No file  | `e9726f7c2e87`  |
| 1881   | No file  | `e9726f7c2e87`  |
| 1871   | No file  | `e9726f7c2e87`  |
| 1866   | No file  | `e9726f7c2e87`  |
| 1862   | No file  | `e9726f7c2e87`  |
| 1854   | No file  | `e9726f7c2e87`  |
| 1846   | No file  | `e9726f7c2e87`  |
| 1838   | No file  | `e9726f7c2e87`  |
| 1832   | No file  | `e9726f7c2e87`  |
| 1826   | No file  | `e9726f7c2e87`  |
| 1822   | No file  | `e9726f7c2e87`  |
| 1818   | No file  | `e9726f7c2e87`  |
| 1804   | No file  | `e9726f7c2e87`  |
| 1794   | No file  | `e9726f7c2e87`  |
| 1790   | No file  | `e9726f7c2e87`  |
| 1784   | No file  | `e9726f7c2e87`  |
| 1774   | No file  | `e9726f7c2e87`  |
| 1771   | No file  | `e9726f7c2e87`  |
| 1762   | No file  | `e9726f7c2e87`  |
| 1759   | No file  | `e9726f7c2e87`  |
| 1754   | No file  | `e9726f7c2e87`  |
| 1749   | No file  | `e9726f7c2e87`  |
| 1743   | No file  | `e9726f7c2e87`  |
| 1737   | No file  | `e9726f7c2e87`  |
| 1731   | No file  | `e9726f7c2e87`  |
| 1725   | No file  | `e9726f7c2e87`  |
| 1717   | No file  | `e9726f7c2e87`  |
| 1710   | No file  | `e9726f7c2e87`  |
| 1704   | No file  | `e9726f7c2e87`  |
| 1698   | No file  | `e9726f7c2e87`  |
| 1690   | No file  | `e9726f7c2e87`  |
| 1685   | No file  | `e9726f7c2e87`  |
| 1680   | No file  | `e9726f7c2e87`  |
| 1674   | No file  | `e9726f7c2e87`  |
| 1668   | No file  | `e9726f7c2e87`  |
| 1659   | No file  | `e9726f7c2e87`  |
| 1649   | No file  | `e9726f7c2e87`  |
| 1642   | No file  | `e9726f7c2e87`  |
| 1636   | No file  | `e9726f7c2e87`  |
| 1628   | No file  | `e9726f7c2e87`  |
| 1622   | No file  | `e9726f7c2e87`  |
| 1614   | No file  | `e9726f7c2e87`  |
| 1608   | No file  | `e9726f7c2e87`  |
| 1602   | No file  | `e9726f7c2e87`  |
| 1598   | No file  | `e9726f7c2e87`  |
| 1594   | No file  | `e9726f7c2e87`  |
| 1590   | No file  | `e9726f7c2e87`  |
| 1587   | No file  | `e9726f7c2e87`  |
| 1584   | No file  | `e9726f7c2e87`  |
| 1579   | No file  | `e9726f7c2e87`  |
| 1572   | No file  | `e9726f7c2e87`  |
| 1565   | No file  | `e9726f7c2e87`  |
| 1559   | No file  | `e9726f7c2e87`  |
| 1554   | No file  | `e9726f7c2e87`  |
| 1547   | No file  | `e9726f7c2e87`  |
| 1537   | No file  | `e9726f7c2e87`  |
| 1529   | No file  | `e9726f7c2e87`  |
| 1524   | No file  | `e9726f7c2e87`  |
| 1519   | No file  | `e9726f7c2e87`  |
| 1509   | No file  | `e9726f7c2e87`  |
| 1506   | No file  | `e9726f7c2e87`  |
| 1504   | No file  | `e9726f7c2e87`  |
| 1500   | No file  | `e9726f7c2e87`  |
| 1493   | No file  | `e9726f7c2e87`  |
| 1489   | No file  | `e9726f7c2e87`  |
| 1485   | No file  | `e9726f7c2e87`  |
| 1481   | No file  | `e9726f7c2e87`  |
| 1474   | No file  | `e9726f7c2e87`  |
| 1466   | No file  | `e9726f7c2e87`  |
| 1462   | No file  | `e9726f7c2e87`  |
| 1459   | No file  | `e9726f7c2e87`  |
| 1453   | No file  | `e9726f7c2e87`  |
| 1450   | No file  | `e9726f7c2e87`  |
| 1445   | No file  | `e9726f7c2e87`  |
| 1439   | No file  | `e9726f7c2e87`  |
| 1433   | No file  | `e9726f7c2e87`  |
| 1430   | No file  | `e9726f7c2e87`  |
| 1426   | No file  | `e9726f7c2e87`  |
| 1421   | No file  | `e9726f7c2e87`  |
| 1417   | No file  | `e9726f7c2e87`  |
| 1416   | No file  | `e9726f7c2e87`  |
| 1409   | No file  | `e9726f7c2e87`  |
| 1405   | No file  | `e9726f7c2e87`  |
| 1401   | No file  | `e9726f7c2e87`  |
| 1396   | No file  | `e9726f7c2e87`  |
| 1391   | No file  | `e9726f7c2e87`  |
| 1390   | No file  | `e9726f7c2e87`  |
| 1386   | No file  | `e9726f7c2e87`  |
| 1381   | No file  | `e9726f7c2e87`  |
| 1379   | No file  | `e9726f7c2e87`  |
| 1372   | No file  | `e9726f7c2e87`  |
| 1366   | No file  | `e9726f7c2e87`  |
| 1364   | No file  | `e9726f7c2e87`  |
| 1363   | No file  | `e9726f7c2e87`  |
| 1360   | No file  | `e9726f7c2e87`  |
| 1358   | No file  | `e9726f7c2e87`  |
| 1355   | No file  | `e9726f7c2e87`  |
| 1351   | No file  | `e9726f7c2e87`  |
| 1348   | No file  | `e9726f7c2e87`  |
| 1346   | No file  | `e9726f7c2e87`  |
| 1341   | No file  | `e9726f7c2e87`  |
| 1340   | No file  | `e9726f7c2e87`  |
| 1338   | No file  | `e9726f7c2e87`  |
| 1335   | No file  | `e9726f7c2e87`  |
| 1333   | No file  | `e9726f7c2e87`  |
| 1329   | No file  | `e9726f7c2e87`  |
| 1327   | No file  | `e9726f7c2e87`  |
| 1324   | No file  | `e9726f7c2e87`  |
| 1321   | No file  | `e9726f7c2e87`  |
| 1319   | No file  | `e9726f7c2e87`  |
| 1318   | No file  | `e9726f7c2e87`  |
| 1316   | No file  | `e9726f7c2e87`  |
| 1313   | No file  | `e9726f7c2e87`  |
| 1311   | No file  | `e9726f7c2e87`  |
| 1309   | No file  | `e9726f7c2e87`  |
| 1304   | No file  | `e9726f7c2e87`  |
| 1292   | No file  | `e9726f7c2e87`  |
| 1286   | No file  | `e9726f7c2e87`  |
| 1280   | No file  | `e9726f7c2e87`  |
| 1276   | No file  | `e9726f7c2e87`  |
| 1267   | No file  | `e9726f7c2e87`  |
| 1261   | No file  | `e9726f7c2e87`  |
| 1256   | No file  | `e9726f7c2e87`  |
| 1250   | No file  | `e9726f7c2e87`  |
| 1246   | No file  | `e9726f7c2e87`  |
| 1239   | No file  | `e9726f7c2e87`  |
| 1230   | No file  | `e9726f7c2e87`  |
| 1226   | No file  | `e9726f7c2e87`  |
| 1220   | No file  | `e9726f7c2e87`  |
| 1217   | No file  | `e9726f7c2e87`  |
| 1211   | No file  | `e9726f7c2e87`  |
| 1210   | No file  | `e9726f7c2e87`  |
| 1208   | No file  | `e9726f7c2e87`  |
| 1203   | No file  | `e9726f7c2e87`  |
| 1197   | No file  | `e9726f7c2e87`  |
| 1194   | No file  | `e9726f7c2e87`  |
| 1192   | No file  | `e9726f7c2e87`  |
| 1187   | No file  | `e9726f7c2e87`  |
| 1183   | No file  | `e9726f7c2e87`  |
| 1177   | No file  | `e9726f7c2e87`  |
| 1173   | No file  | `e9726f7c2e87`  |
| 1167   | No file  | `e9726f7c2e87`  |
| 1164   | No file  | `e9726f7c2e87`  |
| 1156   | No file  | `e9726f7c2e87`  |
| 1149   | No file  | `e9726f7c2e87`  |
| 1144   | No file  | `e9726f7c2e87`  |
| 1137   | No file  | `e9726f7c2e87`  |
| 1132   | No file  | `e9726f7c2e87`  |
| 1127   | No file  | `e9726f7c2e87`  |
| 1122   | No file  | `e9726f7c2e87`  |
| 1118   | No file  | `e9726f7c2e87`  |
| 1114   | No file  | `e9726f7c2e87`  |
| 1109   | No file  | `e9726f7c2e87`  |
| 1102   | No file  | `e9726f7c2e87`  |
| 1096   | No file  | `e9726f7c2e87`  |
| 1088   | No file  | `e9726f7c2e87`  |
| 1081   | No file  | `e9726f7c2e87`  |
| 1076   | No file  | `e9726f7c2e87`  |
| 1069   | No file  | `e9726f7c2e87`  |
| 1064   | No file  | `e9726f7c2e87`  |
| 1058   | No file  | `e9726f7c2e87`  |
| 1051   | No file  | `e9726f7c2e87`  |
| 1044   | No file  | `e9726f7c2e87`  |
| 1036   | No file  | `e9726f7c2e87`  |
| 1026   | No file  | `e9726f7c2e87`  |
| 1016   | No file  | `e9726f7c2e87`  |
| 1009   | No file  | `e9726f7c2e87`  |
| 1005   | No file  | `e9726f7c2e87`  |
| 1000   | No file  | `e9726f7c2e87`  |
| 998    | No file  | `e9726f7c2e87`  |
| 990    | No file  | `e9726f7c2e87`  |
| 979    | No file  | `e9726f7c2e87`  |
| 972    | No file  | `e9726f7c2e87`  |
| 963    | No file  | `e9726f7c2e87`  |
| 955    | No file  | `e9726f7c2e87`  |
| 946    | No file  | `e9726f7c2e87`  |
| 938    | No file  | `e9726f7c2e87`  |
| 927    | No file  | `e9726f7c2e87`  |
| 911    | No file  | `e9726f7c2e87`  |
| 904    | No file  | `e9726f7c2e87`  |
| 899    | No file  | `e9726f7c2e87`  |
| 894    | No file  | `e9726f7c2e87`  |
| 885    | No file  | `e9726f7c2e87`  |
| 879    | No file  | `e9726f7c2e87`  |
| 872    | No file  | `e9726f7c2e87`  |
| 864    | No file  | `e9726f7c2e87`  |
| 855    | No file  | `e9726f7c2e87`  |
| 853    | No file  | `e9726f7c2e87`  |
| 845    | No file  | `e9726f7c2e87`  |
| 837    | No file  | `e9726f7c2e87`  |
| 829    | No file  | `e9726f7c2e87`  |
| 822    | No file  | `e9726f7c2e87`  |
| 814    | No file  | `e9726f7c2e87`  |
| 805    | No file  | `e9726f7c2e87`  |
| 794    | No file  | `e9726f7c2e87`  |
| 787    | No file  | `e9726f7c2e87`  |
| 780    | No file  | `e9726f7c2e87`  |
| 771    | No file  | `e9726f7c2e87`  |
| 760    | No file  | `e9726f7c2e87`  |
| 748    | No file  | `e9726f7c2e87`  |
| 741    | No file  | `e9726f7c2e87`  |
| 736    | No file  | `e9726f7c2e87`  |
| 731    | No file  | `e9726f7c2e87`  |
| 723    | No file  | `e9726f7c2e87`  |
| 711    | No file  | `e9726f7c2e87`  |
| 707    | No file  | `e9726f7c2e87`  |
| 697    | No file  | `e9726f7c2e87`  |
| 689    | No file  | `e9726f7c2e87`  |
| 683    | No file  | `e9726f7c2e87`  |
| 678    | No file  | `e9726f7c2e87`  |
| 670    | No file  | `e9726f7c2e87`  |
| 661    | No file  | `e9726f7c2e87`  |
| 656    | No file  | `e9726f7c2e87`  |
| 652    | No file  | `e9726f7c2e87`  |
| 643    | No file  | `e9726f7c2e87`  |
| 637    | No file  | `e9726f7c2e87`  |
| 630    | No file  | `e9726f7c2e87`  |
| 627    | No file  | `e9726f7c2e87`  |
| 621    | No file  | `e9726f7c2e87`  |
| 617    | No file  | `e9726f7c2e87`  |
| 615    | No file  | `e9726f7c2e87`  |
| 606    | No file  | `e9726f7c2e87`  |
| 599    | No file  | `e9726f7c2e87`  |
| 592    | No file  | `e9726f7c2e87`  |
| 586    | No file  | `e9726f7c2e87`  |
| 577    | No file  | `e9726f7c2e87`  |
| 569    | No file  | `e9726f7c2e87`  |
| 561    | No file  | `e9726f7c2e87`  |
| 554    | No file  | `e9726f7c2e87`  |
| 542    | No file  | `e9726f7c2e87`  |
| 532    | No file  | `e9726f7c2e87`  |
| 531    | No file  | `e9726f7c2e87`  |
| 526    | No file  | `e9726f7c2e87`  |
| 521    | No file  | `e9726f7c2e87`  |
| 517    | No file  | `e9726f7c2e87`  |
| 510    | No file  | `e9726f7c2e87`  |
| 508    | No file  | `e9726f7c2e87`  |
| 504    | No file  | `e9726f7c2e87`  |
| 497    | No file  | `e9726f7c2e87`  |
| 491    | No file  | `e9726f7c2e87`  |
| 485    | No file  | `e9726f7c2e87`  |
| 478    | No file  | `e9726f7c2e87`  |
| 472    | No file  | `e9726f7c2e87`  |
| 466    | No file  | `e9726f7c2e87`  |
| 457    | No file  | `e9726f7c2e87`  |
| 452    | No file  | `e9726f7c2e87`  |
| 449    | No file  | `e9726f7c2e87`  |
| 435    | No file  | `e9726f7c2e87`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                      |
| --------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0), quest titles (LOC type 18), description text (LOC type 37 under the GAME sheet key hash) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of treasures                           |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 23 bytes + core materials)

| Offset                                 | Type                       | Field                           | Notes                                                                                   |
| -------------------------------------- | -------------------------- | ------------------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`                                | u32                        | item_enchant_key                | The treasure item, `enchant_level << 24 \| item_id`; `getItemEnchantKey`                |
| `+0x04`                                | u16                        | puzzle_key                      | `getPuzzleKeyRaw()`, the key of `ToClient_GetPuzzleStaticStatusByPuzzleKey`; `0` on Krogdalo's Sanctuary |
| `+0x06`                                | u32                        | desc_ref                        | String-table index of the GAME sheet key of the description; `getDesc()`               |
| `+0x0A`                                | u32                        | core_material_count             | `getCoreMaterialCount()`; `0` on Krogdalo's Sanctuary                                   |
| `+0x0E`                                | u32[core_material_count]   | core_material_item_enchant_keys | `getCoreMaterialItemEnchantKey(index)`, the pieces the guidebook counts                |
| `core_material_item_enchant_keys+0x00` | u32                        | quest_no                        | `getQuestNo()`, `quest << 16 \| group`; the quest the guidebook links                   |
| `core_material_item_enchant_keys+0x04` | u32                        | texture_id_ref                  | String-table index of the picture's UI texture ID; `getTextureID()`                     |
| `core_material_item_enchant_keys+0x08` | u8                         | is_hunting                      | `isHunting()`; `1` on the first four treasures of client 3482, see Field Names        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                  |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; two per row                                         |
| `+0x04` | pstr[string_count] | strings      | UTF-16 description keys and texture IDs, in row order                  |

## Treasures

Client 3482, in file order. The quest is `group/quest`.

| `item_enchant_key` | Item                                  | `puzzle_key` | `desc_ref` key                            | Core materials                     | Quest     | `is_hunting` |
| ------------------ | ------------------------------------- | ------------ | ----------------------------------------- | ---------------------------------- | --------- | ------------ |
| `16019`            | Archaeologist's Map                   | `95`         | `LUA_TREASURE_GUIDEBOOK_ITEMDESC_MAP`       | `44273` to `44276`                 | `3730/7`  | `1`          |
| `12034`            | Rich Merchant's Ring                  | `94`         | `LUA_TREASURE_GUIDEBOOK_ITEMDESC_RING`      | `44268` to `44272`                 | `3730/5`  | `1`          |
| `16016`            | Lafi Bedmountain's Upgraded Compass   | `96`         | `LUA_TREASURE_GUIDEBOOK_ITEMDESC_COMPASS`   | `44277` to `44279`                 | `3730/3`  | `1`          |
| `65299`            | Lafi Bedmountain's Upgraded Telescope | `513`        | `LUA_TREASURE_GUIDEBOOK_ITEMDESC_TELESCOPE` | `65327`, `65331`, `65332`          | `3730/9`  | `1`          |
| `59321`            | Ebenruth's Nol                        | `240`        | `LUA_TREASURE_GUIDEBOOK_ITEMDESC_STONE`     | `59324` Ebenruth, `59320` Symbol-Engraved Nol | `3730/1`  | `0` |
| `59418`            | Krogdalo's Sanctuary                  | `0`          | `LUA_TREASURE_GUIDEBOOK_ITEMDESC_NEST`      | none                               | `3730/11` | `0`          |

## Field Names

The file is not in the archives of client 1784. Each field is read by one
getter of the treasure object that `ToClient_GetTreasureInfo(index)`
returns in `panel_window_treasure_guidebook_all_1.luac` (client 3482), and
the row holds one field per getter:

- `item_enchant_key`: `treasureInfo.getItemEnchantKey` goes to
  `getItemEnchantStaticStatus` and the item slot; the six keys are the
  six treasure items.
- `core_material_count` and `core_material_item_enchant_keys`: the
  guidebook draws `getCoreMaterialCount()` slots, each with
  `getCoreMaterialItemEnchantKey(i - 1)`; on the first four rows the keys
  are the treasure's pieces (Archaeologist's Map Piece, Al Yurad's Ring
  Piece, Lafi Bedmountain's Upgraded Compass Parts and Telescope Parts).
- `puzzle_key`: `getPuzzleKeyRaw()` goes to
  `ToClient_GetPuzzleStaticStatusByPuzzleKey`, whose puzzle grid the
  window draws.
- `quest_no`: `getQuestNo()` returns a quest with `_group` and `_quest`;
  the u32 is `3730` in the low half and the quest in the high half, the
  packed quest ID of [`olviaacademyseasonss.bss`](olviaacademyseasonss_bss.md).
- `desc_ref`: `PAGetString(Defines.StringSheet_GAME, treasureInfo:getDesc())`;
  every string it points at is a `LUA_TREASURE_GUIDEBOOK_ITEMDESC_*` key.
- `texture_id_ref`: `getTextureID()` goes to
  `ChangeTextureInfoTextureIDAsync`; the strings are
  `Combine_Etc_Treasure_Book_object_*` texture IDs.
- `is_hunting`: `isHunting()` is the only bool getter and the u8 the only
  one-byte field. When it is true the list button opens the drop search
  for the first core material (`PaGlobalFunc_RenewDropItem_OpenAndSearch`),
  else the treasure guide. The Map, Ring, Compass and Telescope hold `1`,
  Ebenruth's Nol and Krogdalo's Sanctuary `0`.

## Notes

- Krogdalo's Sanctuary (`59418`) has no core materials; the Lua counts
  its progress from quests `6815/2` to `6815/4` instead, by item key.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`: the
  item, puzzle key, description, core materials, quest, texture and the
  hunting flag.
