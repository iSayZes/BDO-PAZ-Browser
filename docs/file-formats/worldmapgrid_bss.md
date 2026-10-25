# `worldmap*typedata.bss` and `worldmap*forconquest.bss` Format

## Purpose

Seven world map grids, one byte per 1,600 x 1,600 world-unit cell over
the whole map: each file is a 2,176 x 1,984 image whose cell value names
the territory, region group or siege area under that cell. The 2016
client already held a field type and a territory byte grid for its world
map textures (see [Field Names](#field-names)). All seven files have the same
layout and size (4,317,200 bytes); they differ only in what a cell value
joins to:

| File                                       | Grid                              | Cell value                                                          |
| ------------------------------------------ | --------------------------------- | ------------------------------------------------------------------- |
| `worldmapterritorytypedata.bss`            | Territories                       | `territoryinfo.bss` territory key                                   |
| `worldmapfieldtypedata.bss`                | Region groups                     | Low byte of a `regiongroupinfo.bss` region group key                |
| `worldmapmajorsiegeregiontypedata.bss`     | Conquest War areas                | Territory key; `255` outside the areas                              |
| `worldmapmajorsiegeterritorytypedata.bss`  | Conquest War areas                | Same bytes as `worldmapmajorsiegeregiontypedata.bss`                |
| `worldmapterritorytypedataforconquest.bss` | Node War territories              | Territory key + 1; `255` outside the territories                    |
| `worldmapsiegeregionforconquest.bss`       | Node War areas                    | Area number of a [`villagesiegeinfo.bss`](villagesiegeinfo_bss.md) row; `0` outside |
| `worldmapoceansiegeregionforconquest.bss`  | Blue Battlefield areas            | Area number of an [`oceansiegeinfo.bss`](oceansiegeinfo_bss.md) row; `255` outside |

[Cell Values](#cell-values) gives the evidence for each join. A
`worldmapfieldtypedata.bss` value that two region groups share is split
by territory, see [Shared Region Group Values](#shared-region-group-values).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                       | Bytes     | Records        | Row bytes |
| ------ | -------------- | ------------------------------------------ | --------- | -------------- | --------- |
| 1      | 805 and later  | `worldmapfieldtypedata.bss`                | 4,317,200 | 1 String Table | 4         |
| 1      | 1749 and later | `worldmapmajorsiegeregiontypedata.bss`     | 4,317,200 | 1 String Table | 4         |
| 1      | 1749 and later | `worldmapmajorsiegeterritorytypedata.bss`  | 4,317,200 | 1 String Table | 4         |
| 1      | 3111 and later | `worldmapoceansiegeregionforconquest.bss`  | 4,317,200 | 1 String Table | 4         |
| 1      | 1524 and later | `worldmapsiegeregionforconquest.bss`       | 4,317,200 | 1 String Table | 4         |
| 1      | 805 and later  | `worldmapterritorytypedata.bss`            | 4,317,200 | 1 String Table | 4         |
| 1      | 1524 and later | `worldmapterritorytypedataforconquest.bss` | 4,317,200 | 1 String Table | 4         |

| Layout | File                                       | Known                | Unknown    |
| ------ | ------------------------------------------ | -------------------- | ---------- |
| 1      | `worldmapfieldtypedata.bss`                | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapmajorsiegeregiontypedata.bss`     | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapmajorsiegeterritorytypedata.bss`  | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapoceansiegeregionforconquest.bss`  | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapsiegeregionforconquest.bss`       | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapterritorytypedata.bss`            | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapterritorytypedataforconquest.bss` | 4,317,200 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `fab918504475`  |
| 3482   | Layout 1             | `fab918504475`  |
| 3474   | Layout 1             | `fab918504475`  |
| 3473   | Layout 1             | `fab918504475`  |
| 3464   | Layout 1             | `fab918504475`  |
| 3458   | Layout 1             | `fab918504475`  |
| 3454   | Layout 1             | `fab918504475`  |
| 3444   | Layout 1             | `fab918504475`  |
| 3435   | Layout 1             | `fab918504475`  |
| 3426   | Layout 1             | `fab918504475`  |
| 3418   | Layout 1             | `fab918504475`  |
| 3412   | Layout 1             | `fab918504475`  |
| 3402   | Layout 1             | `fab918504475`  |
| 3396   | Layout 1             | `fab918504475`  |
| 3387   | Layout 1             | `fab918504475`  |
| 3381   | Layout 1             | `fab918504475`  |
| 3373   | Layout 1             | `fab918504475`  |
| 3364   | Layout 1             | `fab918504475`  |
| 3356   | Layout 1             | `fab918504475`  |
| 3349   | Layout 1             | `fab918504475`  |
| 3342   | Layout 1             | `fab918504475`  |
| 3335   | Layout 1             | `fab918504475`  |
| 3326   | Layout 1             | `fab918504475`  |
| 3321   | Layout 1             | `fab918504475`  |
| 3314   | Layout 1             | `fab918504475`  |
| 3303   | Layout 1             | `fab918504475`  |
| 3302   | Layout 1             | `fab918504475`  |
| 3293   | Layout 1             | `fab918504475`  |
| 3283   | Layout 1             | `fab918504475`  |
| 3275   | Layout 1             | `fab918504475`  |
| 3267   | Layout 1             | `fab918504475`  |
| 3258   | Layout 1             | `fab918504475`  |
| 3251   | Layout 1             | `fab918504475`  |
| 3242   | Layout 1             | `fab918504475`  |
| 3235   | Layout 1             | `fab918504475`  |
| 3229   | Layout 1             | `fab918504475`  |
| 3212   | Layout 1             | `fab918504475`  |
| 3203   | Layout 1             | `fab918504475`  |
| 3193   | Layout 1             | `fab918504475`  |
| 3186   | Layout 1             | `fab918504475`  |
| 3177   | Layout 1             | `fab918504475`  |
| 3169   | Layout 1             | `fab918504475`  |
| 3158   | Layout 1             | `fab918504475`  |
| 3151   | Layout 1             | `fab918504475`  |
| 3144   | Layout 1             | `fab918504475`  |
| 3133   | Layout 1             | `fab918504475`  |
| 3125   | Layout 1             | `fab918504475`  |
| 3118   | Layout 1             | `fab918504475`  |
| 3111   | Layout 1             | `fab918504475`  |
| 3103   | Layout 1             | `fab918504475`  |
| 3095   | Layout 1             | `fab918504475`  |
| 3086   | Layout 1             | `fab918504475`  |
| 3072   | Layout 1             | `fab918504475`  |
| 3062   | Layout 1             | `fab918504475`  |
| 3052   | Layout 1             | `fab918504475`  |
| 3045   | Layout 1             | `fab918504475`  |
| 3037   | Layout 1             | `fab918504475`  |
| 3030   | Layout 1             | `fab918504475`  |
| 3021   | Layout 1             | `fab918504475`  |
| 3012   | Layout 1             | `fab918504475`  |
| 3002   | Layout 1             | `fab918504475`  |
| 2995   | Layout 1             | `fab918504475`  |
| 2987   | Layout 1             | `fab918504475`  |
| 2978   | Layout 1             | `fab918504475`  |
| 2970   | Layout 1             | `fab918504475`  |
| 2959   | Layout 1             | `fab918504475`  |
| 2951   | Layout 1             | `fab918504475`  |
| 2942   | Layout 1             | `fab918504475`  |
| 2935   | Layout 1             | `fab918504475`  |
| 2932   | Layout 1             | `fab918504475`  |
| 2923   | Layout 1             | `fab918504475`  |
| 2919   | Layout 1             | `fab918504475`  |
| 2907   | Layout 1             | `fab918504475`  |
| 2900   | Layout 1             | `fab918504475`  |
| 2891   | Layout 1             | `fab918504475`  |
| 2882   | Layout 1             | `fab918504475`  |
| 2872   | Layout 1             | `fab918504475`  |
| 2863   | Layout 1             | `fab918504475`  |
| 2855   | Layout 1             | `fab918504475`  |
| 2849   | Layout 1             | `fab918504475`  |
| 2844   | Layout 1             | `fab918504475`  |
| 2834   | Layout 1             | `fab918504475`  |
| 2825   | Layout 1             | `fab918504475`  |
| 2819   | Layout 1             | `fab918504475`  |
| 2811   | Layout 1             | `fab918504475`  |
| 2803   | Layout 1             | `fab918504475`  |
| 2794   | Layout 1             | `fab918504475`  |
| 2783   | Layout 1             | `fab918504475`  |
| 2774   | Layout 1             | `fab918504475`  |
| 2765   | Layout 1             | `fab918504475`  |
| 2756   | Layout 1             | `fab918504475`  |
| 2750   | Layout 1             | `fab918504475`  |
| 2743   | Layout 1             | `fab918504475`  |
| 2736   | Layout 1             | `fab918504475`  |
| 2726   | Layout 1             | `fab918504475`  |
| 2717   | Layout 1             | `fab918504475`  |
| 2709   | Layout 1             | `fab918504475`  |
| 2703   | Layout 1             | `fab918504475`  |
| 2695   | Layout 1             | `fab918504475`  |
| 2684   | Layout 1             | `fab918504475`  |
| 2672   | Layout 1             | `fab918504475`  |
| 2665   | Layout 1             | `fab918504475`  |
| 2657   | Layout 1             | `fab918504475`  |
| 2649   | Layout 1             | `fab918504475`  |
| 2644   | Layout 1             | `fab918504475`  |
| 2637   | Layout 1             | `fab918504475`  |
| 2629   | Layout 1             | `fab918504475`  |
| 2619   | Layout 1             | `fab918504475`  |
| 2612   | Layout 1             | `fab918504475`  |
| 2606   | Layout 1             | `fab918504475`  |
| 2602   | Layout 1             | `fab918504475`  |
| 2601   | Layout 1             | `fab918504475`  |
| 2592   | Layout 1             | `fab918504475`  |
| 2583   | Layout 1             | `fab918504475`  |
| 2575   | Layout 1             | `fab918504475`  |
| 2567   | Layout 1             | `fab918504475`  |
| 2560   | Layout 1             | `fab918504475`  |
| 2553   | Layout 1             | `fab918504475`  |
| 2545   | Layout 1             | `fab918504475`  |
| 2538   | Layout 1             | `fab918504475`  |
| 2529   | Layout 1             | `fab918504475`  |
| 2519   | Layout 1             | `fab918504475`  |
| 2513   | Layout 1             | `fab918504475`  |
| 2510   | Layout 1             | `fab918504475`  |
| 2507   | Layout 1             | `fab918504475`  |
| 2503   | Layout 1             | `fab918504475`  |
| 2498   | Layout 1             | `fab918504475`  |
| 2492   | Layout 1             | `fab918504475`  |
| 2487   | Layout 1             | `fab918504475`  |
| 2480   | Layout 1             | `fab918504475`  |
| 2474   | Layout 1             | `fab918504475`  |
| 2468   | Layout 1             | `fab918504475`  |
| 2460   | Layout 1             | `fab918504475`  |
| 2453   | Layout 1             | `fab918504475`  |
| 2444   | Layout 1             | `fab918504475`  |
| 2438   | Layout 1             | `fab918504475`  |
| 2434   | Layout 1             | `fab918504475`  |
| 2429   | Layout 1             | `fab918504475`  |
| 2421   | Layout 1             | `fab918504475`  |
| 2414   | Layout 1             | `fab918504475`  |
| 2407   | Layout 1             | `fab918504475`  |
| 2401   | Layout 1             | `fab918504475`  |
| 2397   | Layout 1             | `fab918504475`  |
| 2393   | Layout 1             | `fab918504475`  |
| 2384   | Layout 1             | `fab918504475`  |
| 2378   | Layout 1             | `fab918504475`  |
| 2372   | Layout 1             | `fab918504475`  |
| 2358   | Layout 1             | `fab918504475`  |
| 2352   | Layout 1             | `fab918504475`  |
| 2347   | Layout 1             | `fab918504475`  |
| 2343   | Layout 1             | `fab918504475`  |
| 2335   | Layout 1             | `fab918504475`  |
| 2327   | Layout 1             | `fab918504475`  |
| 2324   | Layout 1             | `fab918504475`  |
| 2319   | Layout 1             | `fab918504475`  |
| 2313   | Layout 1             | `fab918504475`  |
| 2308   | Layout 1             | `fab918504475`  |
| 2302   | Layout 1             | `fab918504475`  |
| 2295   | Layout 1             | `fab918504475`  |
| 2290   | Layout 1             | `fab918504475`  |
| 2284   | Layout 1             | `fab918504475`  |
| 2276   | Layout 1             | `fab918504475`  |
| 2269   | Layout 1             | `fab918504475`  |
| 2259   | Layout 1             | `fab918504475`  |
| 2250   | Layout 1             | `fab918504475`  |
| 2243   | Layout 1             | `fab918504475`  |
| 2235   | Layout 1             | `fab918504475`  |
| 2229   | Layout 1             | `fab918504475`  |
| 2224   | Layout 1             | `fab918504475`  |
| 2218   | Layout 1             | `fab918504475`  |
| 2215   | Layout 1             | `fab918504475`  |
| 2207   | Layout 1             | `fab918504475`  |
| 2203   | Layout 1             | `fab918504475`  |
| 2196   | Layout 1             | `fab918504475`  |
| 2192   | Layout 1             | `fab918504475`  |
| 2189   | Layout 1             | `fab918504475`  |
| 2183   | Layout 1             | `fab918504475`  |
| 2179   | Layout 1             | `fab918504475`  |
| 2171   | Layout 1             | `fab918504475`  |
| 2163   | Layout 1             | `fab918504475`  |
| 2156   | Layout 1             | `fab918504475`  |
| 2151   | Layout 1             | `fab918504475`  |
| 2147   | Layout 1             | `fab918504475`  |
| 2142   | Layout 1             | `fab918504475`  |
| 2138   | Layout 1             | `fab918504475`  |
| 2134   | Layout 1             | `fab918504475`  |
| 2130   | Layout 1             | `fab918504475`  |
| 2122   | Layout 1             | `fab918504475`  |
| 2107   | Layout 1             | `fab918504475`  |
| 2098   | Layout 1             | `fab918504475`  |
| 2089   | Layout 1             | `fab918504475`  |
| 2081   | Layout 1             | `fab918504475`  |
| 2073   | Layout 1             | `fab918504475`  |
| 2067   | Layout 1             | `fab918504475`  |
| 2063   | Layout 1             | `fab918504475`  |
| 2059   | Layout 1             | `fab918504475`  |
| 2052   | Layout 1             | `fab918504475`  |
| 2044   | Layout 1             | `fab918504475`  |
| 2039   | Layout 1             | `fab918504475`  |
| 2032   | Layout 1             | `fab918504475`  |
| 2025   | Layout 1             | `fab918504475`  |
| 2011   | Layout 1             | `fab918504475`  |
| 2005   | Layout 1             | `fab918504475`  |
| 2000   | Layout 1             | `fab918504475`  |
| 1996   | Layout 1             | `fab918504475`  |
| 1991   | Layout 1             | `fab918504475`  |
| 1985   | Layout 1             | `fab918504475`  |
| 1980   | Layout 1             | `fab918504475`  |
| 1969   | Layout 1             | `fab918504475`  |
| 1964   | Layout 1             | `fab918504475`  |
| 1958   | Layout 1             | `fab918504475`  |
| 1950   | Layout 1             | `fab918504475`  |
| 1945   | Layout 1             | `fab918504475`  |
| 1937   | Layout 1             | `fab918504475`  |
| 1933   | Layout 1             | `fab918504475`  |
| 1927   | Layout 1             | `fab918504475`  |
| 1921   | Layout 1             | `fab918504475`  |
| 1914   | Layout 1             | `fab918504475`  |
| 1908   | Layout 1             | `fab918504475`  |
| 1897   | Layout 1             | `fab918504475`  |
| 1892   | Layout 1             | `fab918504475`  |
| 1886   | Layout 1             | `fab918504475`  |
| 1881   | Layout 1             | `fab918504475`  |
| 1871   | Layout 1             | `fab918504475`  |
| 1866   | Layout 1             | `fab918504475`  |
| 1862   | Layout 1             | `fab918504475`  |
| 1854   | Layout 1             | `fab918504475`  |
| 1846   | Layout 1             | `fab918504475`  |
| 1838   | Layout 1             | `fab918504475`  |
| 1832   | Layout 1             | `fab918504475`  |
| 1826   | Layout 1             | `fab918504475`  |
| 1822   | Layout 1             | `fab918504475`  |
| 1818   | Layout 1             | `fab918504475`  |
| 1804   | Layout 1             | `fab918504475`  |
| 1794   | Layout 1             | `fab918504475`  |
| 1790   | Layout 1             | `fab918504475`  |
| 1784   | Layout 1             | `fab918504475`  |
| 1774   | Layout 1             | `fab918504475`  |
| 1771   | Layout 1             | `fab918504475`  |
| 1762   | Layout 1             | `fab918504475`  |
| 1759   | Layout 1             | `fab918504475`  |
| 1754   | Layout 1             | `fab918504475`  |
| 1749   | Layout 1             | `fab918504475`  |
| 1743   | Layout 1             | `fab918504475`  |
| 1737   | Layout 1             | `fab918504475`  |
| 1731   | Layout 1             | `fab918504475`  |
| 1725   | Layout 1             | `fab918504475`  |
| 1717   | Layout 1             | `fab918504475`  |
| 1710   | Layout 1             | `fab918504475`  |
| 1704   | Layout 1             | `fab918504475`  |
| 1698   | Layout 1             | `fab918504475`  |
| 1690   | Layout 1             | `fab918504475`  |
| 1685   | Layout 1             | `fab918504475`  |
| 1680   | Layout 1             | `fab918504475`  |
| 1674   | Layout 1             | `fab918504475`  |
| 1668   | Layout 1             | `fab918504475`  |
| 1659   | Layout 1             | `fab918504475`  |
| 1649   | Layout 1             | `fab918504475`  |
| 1642   | Layout 1             | `fab918504475`  |
| 1636   | Layout 1             | `fab918504475`  |
| 1628   | Layout 1             | `fab918504475`  |
| 1622   | Layout 1             | `fab918504475`  |
| 1614   | Layout 1             | `fab918504475`  |
| 1608   | Layout 1             | `fab918504475`  |
| 1602   | Layout 1             | `fab918504475`  |
| 1598   | Layout 1             | `fab918504475`  |
| 1594   | Layout 1             | `fab918504475`  |
| 1590   | Layout 1             | `fab918504475`  |
| 1587   | Layout 1             | `fab918504475`  |
| 1584   | Layout 1             | `fab918504475`  |
| 1579   | Layout 1             | `fab918504475`  |
| 1572   | Layout 1             | `fab918504475`  |
| 1565   | Layout 1             | `fab918504475`  |
| 1559   | Layout 1             | `fab918504475`  |
| 1554   | Layout 1             | `fab918504475`  |
| 1547   | Layout 1             | `fab918504475`  |
| 1537   | Layout 1             | `fab918504475`  |
| 1529   | Layout 1             | `fab918504475`  |
| 1524   | Layout 1             | `fab918504475`  |
| 1519   | Layout 1             | `fab918504475`  |
| 1509   | Layout 1             | `fab918504475`  |
| 1506   | Layout 1             | `fab918504475`  |
| 1504   | Layout 1             | `fab918504475`  |
| 1500   | Layout 1             | `fab918504475`  |
| 1493   | Layout 1             | `fab918504475`  |
| 1489   | Layout 1             | `fab918504475`  |
| 1485   | Layout 1             | `fab918504475`  |
| 1481   | Layout 1             | `fab918504475`  |
| 1474   | Layout 1             | `fab918504475`  |
| 1466   | Layout 1             | `fab918504475`  |
| 1462   | Layout 1             | `fab918504475`  |
| 1459   | Layout 1             | `fab918504475`  |
| 1453   | Layout 1             | `fab918504475`  |
| 1450   | Layout 1             | `fab918504475`  |
| 1445   | Layout 1             | `fab918504475`  |
| 1439   | Layout 1             | `fab918504475`  |
| 1433   | Layout 1             | `fab918504475`  |
| 1430   | Layout 1             | `fab918504475`  |
| 1426   | Layout 1             | `fab918504475`  |
| 1421   | Layout 1             | `fab918504475`  |
| 1417   | Layout 1             | `fab918504475`  |
| 1416   | Layout 1             | `fab918504475`  |
| 1409   | Layout 1             | `fab918504475`  |
| 1405   | Layout 1             | `fab918504475`  |
| 1401   | Layout 1             | `fab918504475`  |
| 1396   | Layout 1             | `fab918504475`  |
| 1391   | Layout 1             | `fab918504475`  |
| 1390   | Layout 1             | `fab918504475`  |
| 1386   | Layout 1             | `fab918504475`  |
| 1381   | Layout 1             | `fab918504475`  |
| 1379   | Layout 1             | `fab918504475`  |
| 1372   | Layout 1             | `fab918504475`  |
| 1366   | Layout 1             | `fab918504475`  |
| 1364   | Layout 1             | `fab918504475`  |
| 1363   | Layout 1             | `fab918504475`  |
| 1360   | Layout 1             | `fab918504475`  |
| 1358   | Layout 1             | `fab918504475`  |
| 1355   | Layout 1             | `fab918504475`  |
| 1351   | Layout 1             | `fab918504475`  |
| 1348   | Layout 1             | `fab918504475`  |
| 1346   | Layout 1             | `fab918504475`  |
| 1341   | Layout 1             | `fab918504475`  |
| 1340   | Layout 1             | `fab918504475`  |
| 1338   | Layout 1             | `fab918504475`  |
| 1335   | Layout 1             | `fab918504475`  |
| 1333   | Layout 1             | `fab918504475`  |
| 1329   | Layout 1             | `fab918504475`  |
| 1327   | Layout 1             | `fab918504475`  |
| 1324   | Layout 1             | `fab918504475`  |
| 1321   | Layout 1             | `fab918504475`  |
| 1319   | Layout 1             | `fab918504475`  |
| 1318   | Layout 1             | `fab918504475`  |
| 1316   | Layout 1             | `fab918504475`  |
| 1313   | Layout 1             | `fab918504475`  |
| 1311   | Layout 1             | `fab918504475`  |
| 1309   | Layout 1             | `fab918504475`  |
| 1304   | Layout 1             | `fab918504475`  |
| 1292   | Layout 1             | `fab918504475`  |
| 1286   | Layout 1             | `fab918504475`  |
| 1280   | Layout 1             | `fab918504475`  |
| 1276   | Layout 1             | `fab918504475`  |
| 1267   | Layout 1             | `fab918504475`  |
| 1261   | Layout 1             | `fab918504475`  |
| 1256   | Layout 1             | `fab918504475`  |
| 1250   | Layout 1             | `fab918504475`  |
| 1246   | Layout 1             | `fab918504475`  |
| 1239   | Layout 1             | `fab918504475`  |
| 1230   | Layout 1             | `fab918504475`  |
| 1226   | Layout 1             | `fab918504475`  |
| 1220   | Layout 1             | `fab918504475`  |
| 1217   | Layout 1             | `fab918504475`  |
| 1211   | Layout 1             | `fab918504475`  |
| 1210   | Layout 1             | `fab918504475`  |
| 1208   | Layout 1             | `fab918504475`  |
| 1203   | Layout 1             | `fab918504475`  |
| 1197   | Layout 1             | `fab918504475`  |
| 1194   | Layout 1             | `fab918504475`  |
| 1192   | Layout 1             | `fab918504475`  |
| 1187   | Layout 1             | `fab918504475`  |
| 1183   | Layout 1             | `fab918504475`  |
| 1177   | Layout 1             | `fab918504475`  |
| 1173   | Layout 1             | `fab918504475`  |
| 1167   | Layout 1             | `fab918504475`  |
| 1164   | Layout 1             | `fab918504475`  |
| 1156   | Layout 1             | `fab918504475`  |
| 1149   | Layout 1             | `fab918504475`  |
| 1144   | Layout 1             | `fab918504475`  |
| 1137   | Layout 1             | `fab918504475`  |
| 1132   | Layout 1             | `fab918504475`  |
| 1127   | Layout 1             | `fab918504475`  |
| 1122   | Layout 1             | `fab918504475`  |
| 1118   | Layout 1             | `fab918504475`  |
| 1114   | Layout 1             | `fab918504475`  |
| 1109   | Layout 1             | `fab918504475`  |
| 1102   | No file              | `fab918504475`  |
| 1096   | No file              | `fab918504475`  |
| 1088   | No file              | `fab918504475`  |
| 1081   | No file              | `fab918504475`  |
| 1076   | No file              | `fab918504475`  |
| 1069   | No file              | `fab918504475`  |
| 1064   | No file              | `fab918504475`  |
| 1058   | No file              | `fab918504475`  |
| 1051   | No file              | `fab918504475`  |
| 1044   | No file              | `fab918504475`  |
| 1036   | No file              | `fab918504475`  |
| 1026   | No file              | `fab918504475`  |
| 1016   | No file              | `fab918504475`  |
| 1009   | No file              | `fab918504475`  |
| 1005   | No file              | `fab918504475`  |
| 1000   | No file              | `fab918504475`  |
| 998    | No file              | `fab918504475`  |
| 990    | No file              | `fab918504475`  |
| 979    | No file              | `fab918504475`  |
| 972    | No file              | `fab918504475`  |
| 963    | No file              | `fab918504475`  |
| 955    | No file              | `fab918504475`  |
| 946    | No file              | `fab918504475`  |
| 938    | No file              | `fab918504475`  |
| 927    | No file              | `fab918504475`  |
| 911    | No file              | `fab918504475`  |
| 904    | No file              | `fab918504475`  |
| 899    | No file              | `fab918504475`  |
| 894    | No file              | `fab918504475`  |
| 885    | No file              | `fab918504475`  |
| 879    | No file              | `fab918504475`  |
| 872    | No file              | `fab918504475`  |
| 864    | No file              | `fab918504475`  |
| 855    | No file              | `fab918504475`  |
| 853    | No file              | `fab918504475`  |
| 845    | No file              | `fab918504475`  |
| 837    | No file              | `fab918504475`  |
| 829    | Layout 1             | `fab918504475`  |
| 822    | Layout 1             | `fab918504475`  |
| 814    | Layout 1             | `fab918504475`  |
| 805    | Layout 1             | `fab918504475`  |
| 794    | No documented layout | `fab918504475`  |
| 787    | No documented layout | `fab918504475`  |
| 780    | No documented layout | `fab918504475`  |
| 771    | No documented layout | `fab918504475`  |
| 760    | No documented layout | `fab918504475`  |
| 748    | No documented layout | `fab918504475`  |
| 741    | No documented layout | `fab918504475`  |
| 736    | No documented layout | `fab918504475`  |
| 731    | No file              | `fab918504475`  |
| 723    | No file              | `fab918504475`  |
| 711    | No file              | `fab918504475`  |
| 707    | No file              | `fab918504475`  |
| 697    | No file              | `fab918504475`  |
| 689    | No file              | `fab918504475`  |
| 683    | No file              | `fab918504475`  |
| 678    | No file              | `fab918504475`  |
| 670    | No file              | `fab918504475`  |
| 661    | No file              | `fab918504475`  |
| 656    | No file              | `fab918504475`  |
| 652    | No file              | `fab918504475`  |
| 643    | No file              | `fab918504475`  |
| 637    | No file              | `fab918504475`  |
| 630    | No file              | `fab918504475`  |
| 627    | No file              | `fab918504475`  |
| 621    | No file              | `fab918504475`  |
| 617    | No file              | `fab918504475`  |
| 615    | No file              | `fab918504475`  |
| 606    | No file              | `fab918504475`  |
| 599    | No file              | `fab918504475`  |
| 592    | No file              | `fab918504475`  |
| 586    | No file              | `fab918504475`  |
| 577    | No file              | `fab918504475`  |
| 569    | No file              | `fab918504475`  |
| 561    | No file              | `fab918504475`  |
| 554    | No file              | `fab918504475`  |
| 542    | No file              | `fab918504475`  |
| 532    | No file              | `fab918504475`  |
| 531    | No file              | `fab918504475`  |
| 526    | No file              | `fab918504475`  |
| 521    | No file              | `fab918504475`  |
| 517    | No file              | `fab918504475`  |
| 510    | No file              | `fab918504475`  |
| 508    | No file              | `fab918504475`  |
| 504    | No file              | `fab918504475`  |
| 497    | No file              | `fab918504475`  |
| 491    | No file              | `fab918504475`  |
| 485    | No file              | `fab918504475`  |
| 478    | No file              | `fab918504475`  |
| 472    | No file              | `fab918504475`  |
| 466    | No file              | `fab918504475`  |
| 457    | No file              | `fab918504475`  |
| 452    | No file              | `fab918504475`  |
| 449    | No file              | `fab918504475`  |
| 435    | No file              | `fab918504475`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                                                     |
| ---------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `regiongroupinfo.bss`  | Optional | Region groups of `worldmapfieldtypedata.bss`, named by their worldmap node (LOC type 29) |
| `regioninfo.bss`       | Optional | Territory of each region group's regions, to split a shared `worldmapfieldtypedata.bss` value |
| `worldmapterritorytypedata.bss` | Optional | Territory of each cell, to split a shared `worldmapfieldtypedata.bss` value |
| `villagesiegeinfo.bss` | Optional | Region keys of each Node War area number, for `worldmapsiegeregionforconquest.bss`       |
| `oceansiegeinfo.bss`   | Optional | Island region keys of each Blue Battlefield area number, for `worldmapoceansiegeregionforconquest.bss` |
| `languagedata_en.loc`  | Optional | Territory names (type 12), region names (type 17), node names (type 29)                  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with the shared empty string table and 8-byte trailer (see
[`npcsimply.bss` String Table](npcsimply_bss.md#string-table-variable-4-bytes--strings)).
The grid has no row count: the cells start right after the magic, so a
reader that takes `+0x04` as a PABR count reads the first four cells (`0`
in every file).

| Offset              | Type           | Field        | Notes                                                                       |
| ------------------- | -------------- | ------------ | --------------------------------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                                                |
| `+0x04`             | u8[1984][2176] | cells        | 1,984 rows of 2,176 cells, row 0 at the south edge; see Grid                |
| `+0x41E004`         | String Table   | string_table | See String Table                                                            |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where the cells end: `0x41E004`                 |
| `string_table+0x04` | u32            | zero         | Always `0`                                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | `0` in every file on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | Empty                                     |

## Grid

Cell `(column, row)` sits at byte `0x04 + row * 2176 + column` and
covers world x `-2,048,000 + 1,600 * column` to 1,600 units east of it,
and world z `-1,126,400 + 1,600 * row` to 1,600 units north of it. A
12,800-unit world sector is 8 x 8 cells, so the grid spans sectors x
`-160` to `111` and z `-88` to `159`.

I found the transform by fitting the territory grid to the waypoints of
`mapdata_realexplore2.bwp`: on client 3482, 556 of the 557 regions of
`regioninfo.bss` outside Balenos whose `waypoint_key` has a waypoint lie
on a cell with their own `territory_key` under this transform, with the
cell size tried at 1,600 and 3,200 units and the origin in 6,400-unit
steps. The next best origin, one sector west, reaches 552.

The outermost 8 cells on each side (one sector) are `0` in every file on
clients 1784 and 3482, also in the files that fill the rest of the map
with `255`: 66,304 cells.

## Cell Values

Evidence on client 3482: each region of `regioninfo.bss` with a waypoint
in `mapdata_realexplore2.bwp` was looked up at its waypoint's cell (628
regions).

| File                                       | Check                                                       | Result |
| ------------------------------------------ | ----------------------------------------------------------- | ------ |
| `worldmapterritorytypedata.bss`            | Cell value equals the region's `territory_key`              | 627 of 628; Duvencrune (territory 7) reads `5` |
| `worldmapfieldtypedata.bss`                | Cell value equals `region_group_key & 0xFF`                 | 604 of 628; 20 of the misses read `0`, 3 a neighbouring group, and Duvencrune (group `0`) reads `220` |
| `worldmapmajorsiegeregiontypedata.bss`     | Cell value equals `territory_key`, cells other than `255`   | 13 of 13 |
| `worldmapterritorytypedataforconquest.bss` | Cell value equals `territory_key + 1`, cells other than `255` | 147 of 148; Serendia Western Gateway (Calpheon) reads `2` (Serendia) |
| `worldmapsiegeregionforconquest.bss`       | Each `villagesiegeinfo.bss` row's region reads the row's `area_number` | 30 of 40; the 4 capitals (`25` to `28`) are not in the grid, the other 6 waypoints read `0` |
| `worldmapoceansiegeregionforconquest.bss`  | Each `oceansiegeinfo.bss` island reads its row's `area_number` | 15 of the 15 islands whose number the grid holds |

Values present on client 3482:

| File                                       | Values                                                                 |
| ------------------------------------------ | ---------------------------------------------------------------------- |
| `worldmapterritorytypedata.bss`            | `0` to `13`, all 14 territories; `0` is also every cell off the map    |
| `worldmapfieldtypedata.bss`                | 208 values; `0` off the map                                            |
| `worldmapmajorsiegeregiontypedata.bss`     | `0` (Balenos, and the frame), `1` Serendia, `3` Mediah, `4` Valencia, `255` |
| `worldmapterritorytypedataforconquest.bss` | `0` (the frame), `1` Balenos, `2` Serendia, `3` Calpheon, `5` Valencia, `12` Ulukita, `13` Outer Edania, `255`: the six territories of the `villagesiegeinfo.bss` node war nodes |
| `worldmapsiegeregionforconquest.bss`       | `0`, `1` to `24` and `29` to `40`: the 36 node war nodes of `villagesiegeinfo.bss` |
| `worldmapoceansiegeregionforconquest.bss`  | `0` (the frame), `2` to `16` (the Balenos islands), `255`              |

A region group key above 255 shares its byte with the key 256 lower: on
client 3482, 39 of the values `0` to `46` stand for two groups each, `2`
for the Altar of Agris group (`2`) and the Unjongga Street group (`258`)
in the Land of the Morning Light.

## Shared Region Group Values

The territory grid tells the two groups of a shared
`worldmapfieldtypedata.bss` value apart, and the preview gives each group
its own row:

1. A group's territory is the `territory_key` of its `regioninfo.bss`
   regions. On client 3483, 249 of the 250 groups have all their regions
   in one territory; group `0` (no worldmap node, no position, the Test
   Zone, ocean and undiscovered-area regions among its 32) spans eight.
2. A group with one territory owns the value's cells whose
   `worldmapterritorytypedata.bss` cell is that territory. When two groups
   of a value have the same territory, neither owns it.
3. The value's other cells go to the groups that own no territory (group
   `0` for value `0`), or, when every group owns one, to one row with all
   the groups' keys.

On client 3483 the shared values pair a group in Balenos or Serendia with
one in the Land of the Morning Light (values `1` to `25` except `10`),
Calpheon with Ulukita (`31`, `33`, `34` and `36` to `38`), Calpheon with
Outer Edania (`40` to `46`) and Calpheon with Balenos (`39`, groups `39`
and `295`). Value `0` pairs group `0` with group `256` in the Land of the
Morning Light. Values `3`, `22` and `23` keep a row with both keys
for their cells in a territory neither group lies in: 3 cells in Serendia
and 95 in territory 7.

Evidence on client 3483: of the `regioninfo.bss` regions in a group of a
shared value whose `mapdata_realexplore2.bwp` waypoint lies on a cell of
that value, all 208 (121 in the lower group, 87 in the upper) land on
their own group's row. Another 15 waypoints lie on a cell of another
value.

Without `regioninfo.bss` or the territory grid, a shared value keeps one
row with both keys.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its
`PAWorldMapManager` holds `_fieldTypeData` and `_territoryTypeData`, both
`unsigned char*`, with `createFieldTypeData`, `getFieldTypeDataSize` and
`updateFieldTypeDataToTexture` (and the same three for the territory
data), and its shaders read the textures `WorldMapFieldTypeTexture` and
`WorldMapTerritoryTypeTexture`, with `fSelectedFieldType` and
`fFieldDataResolution` in `WorldmapTerrainShaderConst`. I name the cell
array `cells`; the 2016 names cover two of the seven files only.

## Notes

- `worldmapmajorsiegeregiontypedata.bss` and
  `worldmapmajorsiegeterritorytypedata.bss` are byte for byte equal on
  clients 1784 and 3482.
- Client 1784 has six of the files; `worldmapoceansiegeregionforconquest.bss`
  is missing there. Between client 1784 and 3482 the territory grid
  differs in 352,681 cells and the region group grid in 366,269.

## Open Questions

### Why the Node War Territory Grid Adds One

`worldmapterritorytypedataforconquest.bss` stores the territory key plus
one, while `worldmapmajorsiegeregiontypedata.bss` stores the key itself
and so cannot tell Balenos (`0`) from its frame. The shift is read from
the data only (147 of 148 waypoints); no Lua or symbol names it.

### Region and Territory Major Siege Grids

`worldmapmajorsiegeregiontypedata.bss` and
`worldmapmajorsiegeterritorytypedata.bss` hold the same bytes on both
clients checked. In the client 3482 Lua (`grand_worldmap_mainpanel_new.luac`,
`GuildWar_SetTerritoryKey`) the world map's siege filter passes a
territory key to `ToClient_setVisibleMajorSiegeTerritoryKey` when
`ToClient_SetMajorSiegeViewMode` is on, else to
`ToClient_setVisibleVillageTerritoryKey`. Which grid each call draws,
and why both major siege files exist, is open.

### Region Groups Above 255

The field type grid keeps only the low byte of a region group key, so
groups `256` to `302` share values with groups `0` to `46`. The preview
splits them by territory (see
[Shared Region Group Values](#shared-region-group-values)), which fits
every waypoint checked. Whether the client does the same when it
highlights a group on the world map, or highlights both groups, is open.
