# `*.bwp` Waypoint Graph Format

## Purpose

Waypoint graphs: named 3D points, the links between them, optional groups and optional routes. Every PABR `.bwp` under `gamecommondata/waypoint_binary/` shares this layout (1,287 files on client 3458). Each one is the binary form of the same-named Ocean tool export in `gamecommondata/waypoint/*.xml`. The worldmap node graph is `mapdata_realexplore2.bwp`: its waypoint keys are `exploration.bss` node keys, and a production sub-node's only link is its parent node. In it, waypoint 1 `town(velia)` links to 21, 22, 26, 43, 46, 102, 103, 1018 and 1898, and waypoint 1880 `hidden_field_goduvillage_2` links only to 1857, Godu Village.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes   | Records                    | Row bytes |
| ------ | -------------- | -------------------------- | ------- | -------------------------- | --------- |
| 1      | 2059 and later | `mapdata_realexplore2.bwp` | 100,531 | 1,101 Waypoint, 2,498 Link | 8         |

| Layout | File                       | Known              | Unknown    |
| ------ | -------------------------- | ------------------ | ---------- |
| 1      | `mapdata_realexplore2.bwp` | 100,531 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `56c043fd75d7`  |
| 3482   | Layout 1 | `56c043fd75d7`  |
| 3474   | Layout 1 | `56c043fd75d7`  |
| 3473   | Layout 1 | `56c043fd75d7`  |
| 3464   | Layout 1 | `56c043fd75d7`  |
| 3458   | Layout 1 | `56c043fd75d7`  |
| 3454   | Layout 1 | `56c043fd75d7`  |
| 3444   | Layout 1 | `56c043fd75d7`  |
| 3435   | Layout 1 | `56c043fd75d7`  |
| 3426   | Layout 1 | `56c043fd75d7`  |
| 3418   | Layout 1 | `56c043fd75d7`  |
| 3412   | Layout 1 | `56c043fd75d7`  |
| 3402   | Layout 1 | `56c043fd75d7`  |
| 3396   | Layout 1 | `56c043fd75d7`  |
| 3387   | Layout 1 | `56c043fd75d7`  |
| 3381   | Layout 1 | `56c043fd75d7`  |
| 3373   | Layout 1 | `56c043fd75d7`  |
| 3364   | Layout 1 | `56c043fd75d7`  |
| 3356   | Layout 1 | `56c043fd75d7`  |
| 3349   | Layout 1 | `56c043fd75d7`  |
| 3342   | Layout 1 | `56c043fd75d7`  |
| 3335   | Layout 1 | `56c043fd75d7`  |
| 3326   | Layout 1 | `56c043fd75d7`  |
| 3321   | Layout 1 | `56c043fd75d7`  |
| 3314   | Layout 1 | `56c043fd75d7`  |
| 3303   | Layout 1 | `56c043fd75d7`  |
| 3302   | Layout 1 | `56c043fd75d7`  |
| 3293   | Layout 1 | `56c043fd75d7`  |
| 3283   | Layout 1 | `56c043fd75d7`  |
| 3275   | Layout 1 | `56c043fd75d7`  |
| 3267   | Layout 1 | `56c043fd75d7`  |
| 3258   | Layout 1 | `56c043fd75d7`  |
| 3251   | Layout 1 | `56c043fd75d7`  |
| 3242   | Layout 1 | `56c043fd75d7`  |
| 3235   | Layout 1 | `56c043fd75d7`  |
| 3229   | Layout 1 | `56c043fd75d7`  |
| 3212   | Layout 1 | `56c043fd75d7`  |
| 3203   | Layout 1 | `56c043fd75d7`  |
| 3193   | Layout 1 | `56c043fd75d7`  |
| 3186   | Layout 1 | `56c043fd75d7`  |
| 3177   | Layout 1 | `56c043fd75d7`  |
| 3169   | Layout 1 | `56c043fd75d7`  |
| 3158   | Layout 1 | `56c043fd75d7`  |
| 3151   | Layout 1 | `56c043fd75d7`  |
| 3144   | Layout 1 | `56c043fd75d7`  |
| 3133   | Layout 1 | `56c043fd75d7`  |
| 3125   | Layout 1 | `56c043fd75d7`  |
| 3118   | Layout 1 | `56c043fd75d7`  |
| 3111   | Layout 1 | `56c043fd75d7`  |
| 3103   | Layout 1 | `56c043fd75d7`  |
| 3095   | Layout 1 | `56c043fd75d7`  |
| 3086   | Layout 1 | `56c043fd75d7`  |
| 3072   | Layout 1 | `56c043fd75d7`  |
| 3062   | Layout 1 | `56c043fd75d7`  |
| 3052   | Layout 1 | `56c043fd75d7`  |
| 3045   | Layout 1 | `56c043fd75d7`  |
| 3037   | Layout 1 | `56c043fd75d7`  |
| 3030   | Layout 1 | `56c043fd75d7`  |
| 3021   | Layout 1 | `56c043fd75d7`  |
| 3012   | Layout 1 | `56c043fd75d7`  |
| 3002   | Layout 1 | `56c043fd75d7`  |
| 2995   | Layout 1 | `56c043fd75d7`  |
| 2987   | Layout 1 | `56c043fd75d7`  |
| 2978   | Layout 1 | `56c043fd75d7`  |
| 2970   | Layout 1 | `56c043fd75d7`  |
| 2959   | Layout 1 | `56c043fd75d7`  |
| 2951   | Layout 1 | `56c043fd75d7`  |
| 2942   | Layout 1 | `56c043fd75d7`  |
| 2935   | Layout 1 | `56c043fd75d7`  |
| 2932   | Layout 1 | `56c043fd75d7`  |
| 2923   | Layout 1 | `56c043fd75d7`  |
| 2919   | Layout 1 | `56c043fd75d7`  |
| 2907   | Layout 1 | `56c043fd75d7`  |
| 2900   | Layout 1 | `56c043fd75d7`  |
| 2891   | Layout 1 | `56c043fd75d7`  |
| 2882   | Layout 1 | `56c043fd75d7`  |
| 2872   | Layout 1 | `56c043fd75d7`  |
| 2863   | Layout 1 | `56c043fd75d7`  |
| 2855   | Layout 1 | `56c043fd75d7`  |
| 2849   | Layout 1 | `56c043fd75d7`  |
| 2844   | Layout 1 | `56c043fd75d7`  |
| 2834   | Layout 1 | `56c043fd75d7`  |
| 2825   | Layout 1 | `56c043fd75d7`  |
| 2819   | Layout 1 | `56c043fd75d7`  |
| 2811   | Layout 1 | `56c043fd75d7`  |
| 2803   | Layout 1 | `56c043fd75d7`  |
| 2794   | Layout 1 | `56c043fd75d7`  |
| 2783   | Layout 1 | `56c043fd75d7`  |
| 2774   | Layout 1 | `56c043fd75d7`  |
| 2765   | Layout 1 | `56c043fd75d7`  |
| 2756   | Layout 1 | `56c043fd75d7`  |
| 2750   | Layout 1 | `56c043fd75d7`  |
| 2743   | Layout 1 | `56c043fd75d7`  |
| 2736   | Layout 1 | `56c043fd75d7`  |
| 2726   | Layout 1 | `56c043fd75d7`  |
| 2717   | Layout 1 | `56c043fd75d7`  |
| 2709   | Layout 1 | `56c043fd75d7`  |
| 2703   | Layout 1 | `56c043fd75d7`  |
| 2695   | Layout 1 | `56c043fd75d7`  |
| 2684   | Layout 1 | `56c043fd75d7`  |
| 2672   | Layout 1 | `56c043fd75d7`  |
| 2665   | Layout 1 | `56c043fd75d7`  |
| 2657   | Layout 1 | `56c043fd75d7`  |
| 2649   | Layout 1 | `56c043fd75d7`  |
| 2644   | Layout 1 | `56c043fd75d7`  |
| 2637   | Layout 1 | `56c043fd75d7`  |
| 2629   | Layout 1 | `56c043fd75d7`  |
| 2619   | Layout 1 | `56c043fd75d7`  |
| 2612   | Layout 1 | `56c043fd75d7`  |
| 2606   | Layout 1 | `56c043fd75d7`  |
| 2602   | Layout 1 | `56c043fd75d7`  |
| 2601   | Layout 1 | `56c043fd75d7`  |
| 2592   | Layout 1 | `56c043fd75d7`  |
| 2583   | Layout 1 | `56c043fd75d7`  |
| 2575   | Layout 1 | `56c043fd75d7`  |
| 2567   | Layout 1 | `56c043fd75d7`  |
| 2560   | Layout 1 | `56c043fd75d7`  |
| 2553   | Layout 1 | `56c043fd75d7`  |
| 2545   | Layout 1 | `56c043fd75d7`  |
| 2538   | Layout 1 | `56c043fd75d7`  |
| 2529   | Layout 1 | `56c043fd75d7`  |
| 2519   | Layout 1 | `56c043fd75d7`  |
| 2513   | Layout 1 | `56c043fd75d7`  |
| 2510   | Layout 1 | `56c043fd75d7`  |
| 2507   | Layout 1 | `56c043fd75d7`  |
| 2503   | Layout 1 | `56c043fd75d7`  |
| 2498   | Layout 1 | `56c043fd75d7`  |
| 2492   | Layout 1 | `56c043fd75d7`  |
| 2487   | Layout 1 | `56c043fd75d7`  |
| 2480   | Layout 1 | `56c043fd75d7`  |
| 2474   | Layout 1 | `56c043fd75d7`  |
| 2468   | Layout 1 | `56c043fd75d7`  |
| 2460   | Layout 1 | `56c043fd75d7`  |
| 2453   | Layout 1 | `56c043fd75d7`  |
| 2444   | Layout 1 | `56c043fd75d7`  |
| 2438   | Layout 1 | `56c043fd75d7`  |
| 2434   | Layout 1 | `56c043fd75d7`  |
| 2429   | Layout 1 | `56c043fd75d7`  |
| 2421   | Layout 1 | `56c043fd75d7`  |
| 2414   | Layout 1 | `56c043fd75d7`  |
| 2407   | Layout 1 | `56c043fd75d7`  |
| 2401   | Layout 1 | `56c043fd75d7`  |
| 2397   | Layout 1 | `56c043fd75d7`  |
| 2393   | Layout 1 | `56c043fd75d7`  |
| 2384   | Layout 1 | `56c043fd75d7`  |
| 2378   | Layout 1 | `56c043fd75d7`  |
| 2372   | Layout 1 | `56c043fd75d7`  |
| 2358   | Layout 1 | `56c043fd75d7`  |
| 2352   | Layout 1 | `56c043fd75d7`  |
| 2347   | Layout 1 | `56c043fd75d7`  |
| 2343   | Layout 1 | `56c043fd75d7`  |
| 2335   | Layout 1 | `56c043fd75d7`  |
| 2327   | Layout 1 | `56c043fd75d7`  |
| 2324   | Layout 1 | `56c043fd75d7`  |
| 2319   | Layout 1 | `56c043fd75d7`  |
| 2313   | Layout 1 | `56c043fd75d7`  |
| 2308   | Layout 1 | `56c043fd75d7`  |
| 2302   | Layout 1 | `56c043fd75d7`  |
| 2295   | Layout 1 | `56c043fd75d7`  |
| 2290   | Layout 1 | `56c043fd75d7`  |
| 2284   | Layout 1 | `56c043fd75d7`  |
| 2276   | Layout 1 | `56c043fd75d7`  |
| 2269   | Layout 1 | `56c043fd75d7`  |
| 2259   | Layout 1 | `56c043fd75d7`  |
| 2250   | Layout 1 | `56c043fd75d7`  |
| 2243   | Layout 1 | `56c043fd75d7`  |
| 2235   | Layout 1 | `56c043fd75d7`  |
| 2229   | Layout 1 | `56c043fd75d7`  |
| 2224   | Layout 1 | `56c043fd75d7`  |
| 2218   | Layout 1 | `56c043fd75d7`  |
| 2215   | Layout 1 | `56c043fd75d7`  |
| 2207   | Layout 1 | `56c043fd75d7`  |
| 2203   | Layout 1 | `56c043fd75d7`  |
| 2196   | Layout 1 | `56c043fd75d7`  |
| 2192   | Layout 1 | `56c043fd75d7`  |
| 2189   | Layout 1 | `56c043fd75d7`  |
| 2183   | Layout 1 | `56c043fd75d7`  |
| 2179   | Layout 1 | `56c043fd75d7`  |
| 2171   | Layout 1 | `56c043fd75d7`  |
| 2163   | Layout 1 | `56c043fd75d7`  |
| 2156   | Layout 1 | `56c043fd75d7`  |
| 2151   | Layout 1 | `56c043fd75d7`  |
| 2147   | Layout 1 | `56c043fd75d7`  |
| 2142   | Layout 1 | `56c043fd75d7`  |
| 2138   | Layout 1 | `56c043fd75d7`  |
| 2134   | Layout 1 | `56c043fd75d7`  |
| 2130   | Layout 1 | `56c043fd75d7`  |
| 2122   | Layout 1 | `56c043fd75d7`  |
| 2107   | Layout 1 | `56c043fd75d7`  |
| 2098   | Layout 1 | `56c043fd75d7`  |
| 2089   | Layout 1 | `56c043fd75d7`  |
| 2081   | Layout 1 | `56c043fd75d7`  |
| 2073   | Layout 1 | `56c043fd75d7`  |
| 2067   | Layout 1 | `56c043fd75d7`  |
| 2063   | Layout 1 | `56c043fd75d7`  |
| 2059   | Layout 1 | `56c043fd75d7`  |
| 2052   | No file  | `56c043fd75d7`  |
| 2044   | No file  | `56c043fd75d7`  |
| 2039   | No file  | `56c043fd75d7`  |
| 2032   | No file  | `56c043fd75d7`  |
| 2025   | No file  | `56c043fd75d7`  |
| 2011   | No file  | `56c043fd75d7`  |
| 2005   | No file  | `56c043fd75d7`  |
| 2000   | No file  | `56c043fd75d7`  |
| 1996   | No file  | `56c043fd75d7`  |
| 1991   | No file  | `56c043fd75d7`  |
| 1985   | No file  | `56c043fd75d7`  |
| 1980   | No file  | `56c043fd75d7`  |
| 1969   | No file  | `56c043fd75d7`  |
| 1964   | No file  | `56c043fd75d7`  |
| 1958   | No file  | `56c043fd75d7`  |
| 1950   | No file  | `56c043fd75d7`  |
| 1945   | No file  | `56c043fd75d7`  |
| 1937   | No file  | `56c043fd75d7`  |
| 1933   | No file  | `56c043fd75d7`  |
| 1927   | No file  | `56c043fd75d7`  |
| 1921   | No file  | `56c043fd75d7`  |
| 1914   | No file  | `56c043fd75d7`  |
| 1908   | No file  | `56c043fd75d7`  |
| 1897   | No file  | `56c043fd75d7`  |
| 1892   | No file  | `56c043fd75d7`  |
| 1886   | No file  | `56c043fd75d7`  |
| 1881   | No file  | `56c043fd75d7`  |
| 1871   | No file  | `56c043fd75d7`  |
| 1866   | No file  | `56c043fd75d7`  |
| 1862   | No file  | `56c043fd75d7`  |
| 1854   | No file  | `56c043fd75d7`  |
| 1846   | No file  | `56c043fd75d7`  |
| 1838   | No file  | `56c043fd75d7`  |
| 1832   | No file  | `56c043fd75d7`  |
| 1826   | No file  | `56c043fd75d7`  |
| 1822   | No file  | `56c043fd75d7`  |
| 1818   | No file  | `56c043fd75d7`  |
| 1804   | No file  | `56c043fd75d7`  |
| 1794   | No file  | `56c043fd75d7`  |
| 1790   | No file  | `56c043fd75d7`  |
| 1784   | No file  | `56c043fd75d7`  |
| 1774   | No file  | `56c043fd75d7`  |
| 1771   | No file  | `56c043fd75d7`  |
| 1762   | No file  | `56c043fd75d7`  |
| 1759   | No file  | `56c043fd75d7`  |
| 1754   | No file  | `56c043fd75d7`  |
| 1749   | No file  | `56c043fd75d7`  |
| 1743   | No file  | `56c043fd75d7`  |
| 1737   | No file  | `56c043fd75d7`  |
| 1731   | No file  | `56c043fd75d7`  |
| 1725   | No file  | `56c043fd75d7`  |
| 1717   | No file  | `56c043fd75d7`  |
| 1710   | No file  | `56c043fd75d7`  |
| 1704   | No file  | `56c043fd75d7`  |
| 1698   | No file  | `56c043fd75d7`  |
| 1690   | No file  | `56c043fd75d7`  |
| 1685   | No file  | `56c043fd75d7`  |
| 1680   | No file  | `56c043fd75d7`  |
| 1674   | No file  | `56c043fd75d7`  |
| 1668   | No file  | `56c043fd75d7`  |
| 1659   | No file  | `56c043fd75d7`  |
| 1649   | No file  | `56c043fd75d7`  |
| 1642   | No file  | `56c043fd75d7`  |
| 1636   | No file  | `56c043fd75d7`  |
| 1628   | No file  | `56c043fd75d7`  |
| 1622   | No file  | `56c043fd75d7`  |
| 1614   | No file  | `56c043fd75d7`  |
| 1608   | No file  | `56c043fd75d7`  |
| 1602   | No file  | `56c043fd75d7`  |
| 1598   | No file  | `56c043fd75d7`  |
| 1594   | No file  | `56c043fd75d7`  |
| 1590   | No file  | `56c043fd75d7`  |
| 1587   | No file  | `56c043fd75d7`  |
| 1584   | No file  | `56c043fd75d7`  |
| 1579   | No file  | `56c043fd75d7`  |
| 1572   | No file  | `56c043fd75d7`  |
| 1565   | No file  | `56c043fd75d7`  |
| 1559   | No file  | `56c043fd75d7`  |
| 1554   | No file  | `56c043fd75d7`  |
| 1547   | No file  | `56c043fd75d7`  |
| 1537   | No file  | `56c043fd75d7`  |
| 1529   | No file  | `56c043fd75d7`  |
| 1524   | No file  | `56c043fd75d7`  |
| 1519   | No file  | `56c043fd75d7`  |
| 1509   | No file  | `56c043fd75d7`  |
| 1506   | No file  | `56c043fd75d7`  |
| 1504   | No file  | `56c043fd75d7`  |
| 1500   | No file  | `56c043fd75d7`  |
| 1493   | No file  | `56c043fd75d7`  |
| 1489   | No file  | `56c043fd75d7`  |
| 1485   | No file  | `56c043fd75d7`  |
| 1481   | No file  | `56c043fd75d7`  |
| 1474   | No file  | `56c043fd75d7`  |
| 1466   | No file  | `56c043fd75d7`  |
| 1462   | No file  | `56c043fd75d7`  |
| 1459   | No file  | `56c043fd75d7`  |
| 1453   | No file  | `56c043fd75d7`  |
| 1450   | No file  | `56c043fd75d7`  |
| 1445   | No file  | `56c043fd75d7`  |
| 1439   | No file  | `56c043fd75d7`  |
| 1433   | No file  | `56c043fd75d7`  |
| 1430   | No file  | `56c043fd75d7`  |
| 1426   | No file  | `56c043fd75d7`  |
| 1421   | No file  | `56c043fd75d7`  |
| 1417   | No file  | `56c043fd75d7`  |
| 1416   | No file  | `56c043fd75d7`  |
| 1409   | No file  | `56c043fd75d7`  |
| 1405   | No file  | `56c043fd75d7`  |
| 1401   | No file  | `56c043fd75d7`  |
| 1396   | No file  | `56c043fd75d7`  |
| 1391   | No file  | `56c043fd75d7`  |
| 1390   | No file  | `56c043fd75d7`  |
| 1386   | No file  | `56c043fd75d7`  |
| 1381   | No file  | `56c043fd75d7`  |
| 1379   | No file  | `56c043fd75d7`  |
| 1372   | No file  | `56c043fd75d7`  |
| 1366   | No file  | `56c043fd75d7`  |
| 1364   | No file  | `56c043fd75d7`  |
| 1363   | No file  | `56c043fd75d7`  |
| 1360   | No file  | `56c043fd75d7`  |
| 1358   | No file  | `56c043fd75d7`  |
| 1355   | No file  | `56c043fd75d7`  |
| 1351   | No file  | `56c043fd75d7`  |
| 1348   | No file  | `56c043fd75d7`  |
| 1346   | No file  | `56c043fd75d7`  |
| 1341   | No file  | `56c043fd75d7`  |
| 1340   | No file  | `56c043fd75d7`  |
| 1338   | No file  | `56c043fd75d7`  |
| 1335   | No file  | `56c043fd75d7`  |
| 1333   | No file  | `56c043fd75d7`  |
| 1329   | No file  | `56c043fd75d7`  |
| 1327   | No file  | `56c043fd75d7`  |
| 1324   | No file  | `56c043fd75d7`  |
| 1321   | No file  | `56c043fd75d7`  |
| 1319   | No file  | `56c043fd75d7`  |
| 1318   | No file  | `56c043fd75d7`  |
| 1316   | No file  | `56c043fd75d7`  |
| 1313   | No file  | `56c043fd75d7`  |
| 1311   | No file  | `56c043fd75d7`  |
| 1309   | No file  | `56c043fd75d7`  |
| 1304   | No file  | `56c043fd75d7`  |
| 1292   | No file  | `56c043fd75d7`  |
| 1286   | No file  | `56c043fd75d7`  |
| 1280   | No file  | `56c043fd75d7`  |
| 1276   | No file  | `56c043fd75d7`  |
| 1267   | No file  | `56c043fd75d7`  |
| 1261   | No file  | `56c043fd75d7`  |
| 1256   | No file  | `56c043fd75d7`  |
| 1250   | No file  | `56c043fd75d7`  |
| 1246   | No file  | `56c043fd75d7`  |
| 1239   | No file  | `56c043fd75d7`  |
| 1230   | No file  | `56c043fd75d7`  |
| 1226   | No file  | `56c043fd75d7`  |
| 1220   | No file  | `56c043fd75d7`  |
| 1217   | No file  | `56c043fd75d7`  |
| 1211   | No file  | `56c043fd75d7`  |
| 1210   | No file  | `56c043fd75d7`  |
| 1208   | No file  | `56c043fd75d7`  |
| 1203   | No file  | `56c043fd75d7`  |
| 1197   | No file  | `56c043fd75d7`  |
| 1194   | No file  | `56c043fd75d7`  |
| 1192   | No file  | `56c043fd75d7`  |
| 1187   | No file  | `56c043fd75d7`  |
| 1183   | No file  | `56c043fd75d7`  |
| 1177   | No file  | `56c043fd75d7`  |
| 1173   | No file  | `56c043fd75d7`  |
| 1167   | No file  | `56c043fd75d7`  |
| 1164   | No file  | `56c043fd75d7`  |
| 1156   | No file  | `56c043fd75d7`  |
| 1149   | No file  | `56c043fd75d7`  |
| 1144   | No file  | `56c043fd75d7`  |
| 1137   | No file  | `56c043fd75d7`  |
| 1132   | No file  | `56c043fd75d7`  |
| 1127   | No file  | `56c043fd75d7`  |
| 1122   | No file  | `56c043fd75d7`  |
| 1118   | No file  | `56c043fd75d7`  |
| 1114   | No file  | `56c043fd75d7`  |
| 1109   | No file  | `56c043fd75d7`  |
| 1102   | No file  | `56c043fd75d7`  |
| 1096   | No file  | `56c043fd75d7`  |
| 1088   | No file  | `56c043fd75d7`  |
| 1081   | No file  | `56c043fd75d7`  |
| 1076   | No file  | `56c043fd75d7`  |
| 1069   | No file  | `56c043fd75d7`  |
| 1064   | No file  | `56c043fd75d7`  |
| 1058   | No file  | `56c043fd75d7`  |
| 1051   | No file  | `56c043fd75d7`  |
| 1044   | No file  | `56c043fd75d7`  |
| 1036   | No file  | `56c043fd75d7`  |
| 1026   | No file  | `56c043fd75d7`  |
| 1016   | No file  | `56c043fd75d7`  |
| 1009   | No file  | `56c043fd75d7`  |
| 1005   | No file  | `56c043fd75d7`  |
| 1000   | No file  | `56c043fd75d7`  |
| 998    | No file  | `56c043fd75d7`  |
| 990    | No file  | `56c043fd75d7`  |
| 979    | No file  | `56c043fd75d7`  |
| 972    | No file  | `56c043fd75d7`  |
| 963    | No file  | `56c043fd75d7`  |
| 955    | No file  | `56c043fd75d7`  |
| 946    | No file  | `56c043fd75d7`  |
| 938    | No file  | `56c043fd75d7`  |
| 927    | No file  | `56c043fd75d7`  |
| 911    | No file  | `56c043fd75d7`  |
| 904    | No file  | `56c043fd75d7`  |
| 899    | No file  | `56c043fd75d7`  |
| 894    | No file  | `56c043fd75d7`  |
| 885    | No file  | `56c043fd75d7`  |
| 879    | No file  | `56c043fd75d7`  |
| 872    | No file  | `56c043fd75d7`  |
| 864    | No file  | `56c043fd75d7`  |
| 855    | No file  | `56c043fd75d7`  |
| 853    | No file  | `56c043fd75d7`  |
| 845    | No file  | `56c043fd75d7`  |
| 837    | No file  | `56c043fd75d7`  |
| 829    | No file  | `56c043fd75d7`  |
| 822    | No file  | `56c043fd75d7`  |
| 814    | No file  | `56c043fd75d7`  |
| 805    | No file  | `56c043fd75d7`  |
| 794    | No file  | `56c043fd75d7`  |
| 787    | No file  | `56c043fd75d7`  |
| 780    | No file  | `56c043fd75d7`  |
| 771    | No file  | `56c043fd75d7`  |
| 760    | No file  | `56c043fd75d7`  |
| 748    | No file  | `56c043fd75d7`  |
| 741    | No file  | `56c043fd75d7`  |
| 736    | No file  | `56c043fd75d7`  |
| 731    | No file  | `56c043fd75d7`  |
| 723    | No file  | `56c043fd75d7`  |
| 711    | No file  | `56c043fd75d7`  |
| 707    | No file  | `56c043fd75d7`  |
| 697    | No file  | `56c043fd75d7`  |
| 689    | No file  | `56c043fd75d7`  |
| 683    | No file  | `56c043fd75d7`  |
| 678    | No file  | `56c043fd75d7`  |
| 670    | No file  | `56c043fd75d7`  |
| 661    | No file  | `56c043fd75d7`  |
| 656    | No file  | `56c043fd75d7`  |
| 652    | No file  | `56c043fd75d7`  |
| 643    | No file  | `56c043fd75d7`  |
| 637    | No file  | `56c043fd75d7`  |
| 630    | No file  | `56c043fd75d7`  |
| 627    | No file  | `56c043fd75d7`  |
| 621    | No file  | `56c043fd75d7`  |
| 617    | No file  | `56c043fd75d7`  |
| 615    | No file  | `56c043fd75d7`  |
| 606    | No file  | `56c043fd75d7`  |
| 599    | No file  | `56c043fd75d7`  |
| 592    | No file  | `56c043fd75d7`  |
| 586    | No file  | `56c043fd75d7`  |
| 577    | No file  | `56c043fd75d7`  |
| 569    | No file  | `56c043fd75d7`  |
| 561    | No file  | `56c043fd75d7`  |
| 554    | No file  | `56c043fd75d7`  |
| 542    | No file  | `56c043fd75d7`  |
| 532    | No file  | `56c043fd75d7`  |
| 531    | No file  | `56c043fd75d7`  |
| 526    | No file  | `56c043fd75d7`  |
| 521    | No file  | `56c043fd75d7`  |
| 517    | No file  | `56c043fd75d7`  |
| 510    | No file  | `56c043fd75d7`  |
| 508    | No file  | `56c043fd75d7`  |
| 504    | No file  | `56c043fd75d7`  |
| 497    | No file  | `56c043fd75d7`  |
| 491    | No file  | `56c043fd75d7`  |
| 485    | No file  | `56c043fd75d7`  |
| 478    | No file  | `56c043fd75d7`  |
| 472    | No file  | `56c043fd75d7`  |
| 466    | No file  | `56c043fd75d7`  |
| 457    | No file  | `56c043fd75d7`  |
| 452    | No file  | `56c043fd75d7`  |
| 449    | No file  | `56c043fd75d7`  |
| 435    | No file  | `56c043fd75d7`  |

<!-- versions:end -->

## Companion Files

None. The string table at the end holds the names.

## Layout 1

### File Layout

866 of the files are empty: `waypoint_count`, `link_count`, `group_count` and `route_count` are all `0`.

| Offset               | Type                     | Field              | Notes                                                        |
| -------------------- | ------------------------ | ------------------ | ------------------------------------------------------------ |
| `+0x00`              | char[4]                  | magic              | ASCII `PABR`                                                 |
| `+0x04`              | u32                      | waypoint_count     | `1,101` in `mapdata_realexplore2.bwp`                        |
| `+0x08`              | Waypoint[waypoint_count] | waypoints          |                                                              |
| `waypoints+0x00`     | u32                      | link_count         | `2,498` in `mapdata_realexplore2.bwp`                        |
| `waypoints+0x04`     | Link[link_count]         | links              |                                                              |
| `links+0x00`         | u8                       | group_count        | `0` or `1` only, see Open Questions                          |
| `links+0x01`         | Group[group_count]       | groups             |                                                              |
| `groups+0x00`        | u32                      | route_count        | `0` in every file but `mapdata_realnpc_route.bwp` (899)      |
| `groups+0x04`        | Route[route_count]       | routes             |                                                              |
| `routes+0x00`        | String Table             | string_table       | Each string stored once                                      |
| `string_table+0x00`  | u32                      | string_table_start | Equals the offset where the routes end, on all 1,287 files   |
| `string_table+0x04`  | u32                      | zero               | Always `0`                                                   |

### Waypoint (23 bytes)

| Offset  | Type | Field           | Notes                                                                 |
| ------- | ---- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | key             | Waypoint key, unique per file; `exploration.bss` node key in `mapdata_realexplore2.bwp` |
| `+0x04` | u32  | index           | Always the row number (`0`-based); also the string table index of the waypoint's name |
| `+0x08` | f32  | x               | World position                                                        |
| `+0x0C` | f32  | y               | Height                                                                |
| `+0x10` | f32  | z               | World position                                                        |
| `+0x14` | u8   | property        | Movement flags, see Property Values                                   |
| `+0x15` | u8   | is_sub_waypoint | `0` or `1` (`IsSubWaypoint`); `1` on 43 of 1,101 worldmap waypoints, not the same set as the `exploration.bss` sub-nodes |
| `+0x16` | u8   | is_escape       | `0` or `1` (`IsEscape`); `1` on 122 waypoints in all files, none in the worldmap |

### Link (8 bytes)

Links are directed. `mapdata_realexplore2.bwp` stores each one both ways (1,249 pairs, no duplicates); patrol and NPC graphs also hold one-way links (83,638 over all files).

| Offset  | Type | Field      | Notes                        |
| ------- | ---- | ---------- | ---------------------------- |
| `+0x00` | u32  | source_key | A waypoint key of this file  |
| `+0x04` | u32  | target_key | A waypoint key of this file  |

### Group (8 bytes)

| Offset  | Type | Field    | Notes                                                              |
| ------- | ---- | -------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | key      | Group key (`Group Key`)                                            |
| `+0x04` | u32  | name_ref | String table index of the group name; may reuse a waypoint name (`mapdata_realmonster_patrol___trollaporter_01.bwp`) |

### Route (variable: 16 bytes + waypoint keys)

| Offset               | Type             | Field                    | Notes                                    |
| -------------------- | ---------------- | ------------------------ | ---------------------------------------- |
| `+0x00`              | u32              | key                      | Route key (`Route Key`)                  |
| `+0x04`              | u32              | name_ref                 | String table index of the route name     |
| `+0x08`              | u32              | point_count              | Number of points                         |
| `+0x0C`              | u32[point_count] | waypoint_keys            | Waypoint keys in route order             |
| `waypoint_keys+0x00` | u32              | unknown_waypoint_keys_00 | `0` on all 899 routes, see Notes         |

### String Table (variable: 4 bytes + strings)

The same counted table as [`npcsimply.bss`](../bss/npcsimply_bss.md#string-table-variable-4-bytes--strings).

| Offset  | Type               | Field        | Notes                           |
| ------- | ------------------ | ------------ | ------------------------------- |
| `+0x00` | u32                | string_count |                                 |
| `+0x04` | pstr[string_count] | strings      | Counted entries, indexed from 0 |

## Enum Values

### Property Values

Named after the XML `Property` attribute; they read as bit flags, with `all` setting every bit.

| Value  | Name   | Waypoints (all files) |
| ------ | ------ | --------------------- |
| `0x00` | none   | 14,284                |
| `0x01` | air    | 13,717                |
| `0x02` | wall   | 379                   |
| `0x10` | ground | 287,278               |
| `0x40` | water  | 7,023                 |
| `0xFF` | all    | 9,327                 |

## Notes

- Checked against the XML exports: in `mapdata_realexplore2`, every waypoint (key, name, position, property, both flags) and all 2,498 links match in file order; all 899 routes of `mapdata_realnpc_route` match (key, name, waypoint keys). The two one-waypoint graphs `mapdata_realexplore2___town(hausher)` and `mapdata_realexplore2___blazing_battlefield` each hold one group and match too.
- The `exploration.bss` Connections columns list each node's worldmap links from this graph, through `worldmap_links()` in `_bwp/waypoint/worldmap.py`.
- Every one of the 439 `plantzone.dbss` zones has exactly one link in `mapdata_realexplore2.bwp`, to a main node. `plantexchangegroup.bss` takes that node as the parent for its English names; it names zones the `exploration.bss` manager family misses (Godu Village 1879-1882, whose family has no main node) and corrects one it gets wrong (Specialties 1563 links to Arehaza 1380, as the Korean label says, not to Areha Palm Forest 1379 of its family).
- Checked in game 2026-09-29, all as the links say: the Specialties node that makes Box of Flesh-rich Coconuts (1563) hangs off Arehaza, the four Godu Village farms (1879-1882) off Godu Village, and four investment banks off Altinova (Zigmund 1189, Gulabi 1190, Quina 1191, Neruda Shen 1192).
- Every route ends in a u32 that is `0` on all 899 routes. The XML `Route` element has nothing besides `Key`, `Name` and `RouteWaypointList` that could map to it, so it stays `unknown_waypoint_keys_00`.
- The largest graphs are `mapdata_realexplore.bwp` (196,367 waypoints), `mapdata_realnpc.bwp` (18,550), `mapdata_realnpc_route.bwp` (9,383) and `mapdata_realmonster_patrol.bwp` (7,607).
- 12 `mapdata_instancedungeon*.bwp` templates (13, 46, 281 or 728 bytes) start with a small count (`00`, `01`, `04` or `0B 00 00 00`) instead of `PABR`. Their XML is empty too, so they are left unread: the preview shows an empty table that says so. A test records each one's size and fails when one grows or turns into a PABR graph, the signal to look at its layout again.

## Open Questions

### Width of `group_count`

The byte after the links is read as a u8 group count because a u32 would not fit the files with one group (`01 02 00 00 00 ...` for group key 2). No file has more than one group, so a u8 count and a one-byte "has group" flag cannot be told apart. A graph with two groups would settle it.
