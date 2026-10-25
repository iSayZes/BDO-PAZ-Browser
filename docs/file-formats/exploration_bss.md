# `exploration.bss` Format

## Purpose

Stores the worldmap node network: one record per node (towns, connection nodes, danger zones and worker production sub-nodes). The primary key is a node key that resolves through LOC `str_type=29` (`str_id4=0` name, `str_id4=1` description) and matches the waypoint keys in `mapdata_realexplore2.bwp`. Each record also carries its node kind, contribution cost, manager and representative NPCs, and the knowledge entries tied to the node.

Field names for several head fields and the `ExplorationNodeType` mapping follow [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, section 12), checked against the bytes of the current client file below.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File              | Bytes   | Records                                                        | Row bytes              |
| ------ | -------------- | ----------------- | ------- | -------------------------------------------------------------- | ---------------------- |
| 2      | 2130 and later | `exploration.bss` | 181,700 | 1,080 Node Head, 7,560 List, 1,080 Node Record, 118 Footer Row | 4 to 200, 6 on average |
| 1      | 1351 to 2122   | `exploration.bss` | 137,562 | 831 Node Head, 5,817 List, 831 Node Record                     | 4 to 196, 6 on average |

| Layout | File              | Known             | Unknown          |
| ------ | ----------------- | ----------------- | ---------------- |
| 2      | `exploration.bss` | 120,984 B (66.6%) | 60,716 B (33.4%) |
| 1      | `exploration.bss` | 87,702 B (63.8%)  | 49,860 B (36.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `de7fd3d83856`  |
| 3482   | Layout 2             | `de7fd3d83856`  |
| 3474   | Layout 2             | `de7fd3d83856`  |
| 3473   | Layout 2             | `de7fd3d83856`  |
| 3464   | Layout 2             | `de7fd3d83856`  |
| 3458   | Layout 2             | `de7fd3d83856`  |
| 3454   | Layout 2             | `de7fd3d83856`  |
| 3444   | Layout 2             | `de7fd3d83856`  |
| 3435   | Layout 2             | `de7fd3d83856`  |
| 3426   | Layout 2             | `de7fd3d83856`  |
| 3418   | Layout 2             | `de7fd3d83856`  |
| 3412   | Layout 2             | `de7fd3d83856`  |
| 3402   | Layout 2             | `de7fd3d83856`  |
| 3396   | Layout 2             | `de7fd3d83856`  |
| 3387   | Layout 2             | `de7fd3d83856`  |
| 3381   | Layout 2             | `de7fd3d83856`  |
| 3373   | Layout 2             | `de7fd3d83856`  |
| 3364   | Layout 2             | `de7fd3d83856`  |
| 3356   | Layout 2             | `de7fd3d83856`  |
| 3349   | Layout 2             | `de7fd3d83856`  |
| 3342   | Layout 2             | `de7fd3d83856`  |
| 3335   | Layout 2             | `de7fd3d83856`  |
| 3326   | Layout 2             | `de7fd3d83856`  |
| 3321   | Layout 2             | `de7fd3d83856`  |
| 3314   | Layout 2             | `de7fd3d83856`  |
| 3303   | Layout 2             | `de7fd3d83856`  |
| 3302   | Layout 2             | `de7fd3d83856`  |
| 3293   | Layout 2             | `de7fd3d83856`  |
| 3283   | Layout 2             | `de7fd3d83856`  |
| 3275   | Layout 2             | `de7fd3d83856`  |
| 3267   | Layout 2             | `de7fd3d83856`  |
| 3258   | Layout 2             | `de7fd3d83856`  |
| 3251   | Layout 2             | `de7fd3d83856`  |
| 3242   | Layout 2             | `de7fd3d83856`  |
| 3235   | Layout 2             | `de7fd3d83856`  |
| 3229   | Layout 2             | `de7fd3d83856`  |
| 3212   | Layout 2             | `de7fd3d83856`  |
| 3203   | Layout 2             | `de7fd3d83856`  |
| 3193   | Layout 2             | `de7fd3d83856`  |
| 3186   | Layout 2             | `de7fd3d83856`  |
| 3177   | Layout 2             | `de7fd3d83856`  |
| 3169   | Layout 2             | `de7fd3d83856`  |
| 3158   | Layout 2             | `de7fd3d83856`  |
| 3151   | Layout 2             | `de7fd3d83856`  |
| 3144   | Layout 2             | `de7fd3d83856`  |
| 3133   | Layout 2             | `de7fd3d83856`  |
| 3125   | Layout 2             | `de7fd3d83856`  |
| 3118   | Layout 2             | `de7fd3d83856`  |
| 3111   | Layout 2             | `de7fd3d83856`  |
| 3103   | Layout 2             | `de7fd3d83856`  |
| 3095   | Layout 2             | `de7fd3d83856`  |
| 3086   | Layout 2             | `de7fd3d83856`  |
| 3072   | Layout 2             | `de7fd3d83856`  |
| 3062   | Layout 2             | `de7fd3d83856`  |
| 3052   | Layout 2             | `de7fd3d83856`  |
| 3045   | Layout 2             | `de7fd3d83856`  |
| 3037   | Layout 2             | `de7fd3d83856`  |
| 3030   | Layout 2             | `de7fd3d83856`  |
| 3021   | Layout 2             | `de7fd3d83856`  |
| 3012   | Layout 2             | `de7fd3d83856`  |
| 3002   | Layout 2             | `de7fd3d83856`  |
| 2995   | Layout 2             | `de7fd3d83856`  |
| 2987   | Layout 2             | `de7fd3d83856`  |
| 2978   | Layout 2             | `de7fd3d83856`  |
| 2970   | Layout 2             | `de7fd3d83856`  |
| 2959   | Layout 2             | `de7fd3d83856`  |
| 2951   | Layout 2             | `de7fd3d83856`  |
| 2942   | Layout 2             | `de7fd3d83856`  |
| 2935   | Layout 2             | `de7fd3d83856`  |
| 2932   | Layout 2             | `de7fd3d83856`  |
| 2923   | Layout 2             | `de7fd3d83856`  |
| 2919   | Layout 2             | `de7fd3d83856`  |
| 2907   | Layout 2             | `de7fd3d83856`  |
| 2900   | Layout 2             | `de7fd3d83856`  |
| 2891   | Layout 2             | `de7fd3d83856`  |
| 2882   | Layout 2             | `de7fd3d83856`  |
| 2872   | Layout 2             | `de7fd3d83856`  |
| 2863   | Layout 2             | `de7fd3d83856`  |
| 2855   | Layout 2             | `de7fd3d83856`  |
| 2849   | Layout 2             | `de7fd3d83856`  |
| 2844   | Layout 2             | `de7fd3d83856`  |
| 2834   | Layout 2             | `de7fd3d83856`  |
| 2825   | Layout 2             | `de7fd3d83856`  |
| 2819   | Layout 2             | `de7fd3d83856`  |
| 2811   | Layout 2             | `de7fd3d83856`  |
| 2803   | Layout 2             | `de7fd3d83856`  |
| 2794   | Layout 2             | `de7fd3d83856`  |
| 2783   | Layout 2             | `de7fd3d83856`  |
| 2774   | Layout 2             | `de7fd3d83856`  |
| 2765   | Layout 2             | `de7fd3d83856`  |
| 2756   | Layout 2             | `de7fd3d83856`  |
| 2750   | Layout 2             | `de7fd3d83856`  |
| 2743   | Layout 2             | `de7fd3d83856`  |
| 2736   | Layout 2             | `de7fd3d83856`  |
| 2726   | Layout 2             | `de7fd3d83856`  |
| 2717   | No documented layout | `de7fd3d83856`  |
| 2709   | No documented layout | `de7fd3d83856`  |
| 2703   | No documented layout | `de7fd3d83856`  |
| 2695   | No documented layout | `de7fd3d83856`  |
| 2684   | No documented layout | `de7fd3d83856`  |
| 2672   | No documented layout | `de7fd3d83856`  |
| 2665   | No documented layout | `de7fd3d83856`  |
| 2657   | No documented layout | `de7fd3d83856`  |
| 2649   | No documented layout | `de7fd3d83856`  |
| 2644   | No documented layout | `de7fd3d83856`  |
| 2637   | No documented layout | `de7fd3d83856`  |
| 2629   | No documented layout | `de7fd3d83856`  |
| 2619   | No documented layout | `de7fd3d83856`  |
| 2612   | No documented layout | `de7fd3d83856`  |
| 2606   | No documented layout | `de7fd3d83856`  |
| 2602   | No documented layout | `de7fd3d83856`  |
| 2601   | No documented layout | `de7fd3d83856`  |
| 2592   | No documented layout | `de7fd3d83856`  |
| 2583   | No documented layout | `de7fd3d83856`  |
| 2575   | No documented layout | `de7fd3d83856`  |
| 2567   | No documented layout | `de7fd3d83856`  |
| 2560   | No documented layout | `de7fd3d83856`  |
| 2553   | No documented layout | `de7fd3d83856`  |
| 2545   | Layout 2             | `de7fd3d83856`  |
| 2538   | Layout 2             | `de7fd3d83856`  |
| 2529   | Layout 2             | `de7fd3d83856`  |
| 2519   | Layout 2             | `de7fd3d83856`  |
| 2513   | Layout 2             | `de7fd3d83856`  |
| 2510   | Layout 2             | `de7fd3d83856`  |
| 2507   | Layout 2             | `de7fd3d83856`  |
| 2503   | Layout 2             | `de7fd3d83856`  |
| 2498   | Layout 2             | `de7fd3d83856`  |
| 2492   | Layout 2             | `de7fd3d83856`  |
| 2487   | Layout 2             | `de7fd3d83856`  |
| 2480   | Layout 2             | `de7fd3d83856`  |
| 2474   | Layout 2             | `de7fd3d83856`  |
| 2468   | Layout 2             | `de7fd3d83856`  |
| 2460   | Layout 2             | `de7fd3d83856`  |
| 2453   | Layout 2             | `de7fd3d83856`  |
| 2444   | Layout 2             | `de7fd3d83856`  |
| 2438   | Layout 2             | `de7fd3d83856`  |
| 2434   | Layout 2             | `de7fd3d83856`  |
| 2429   | Layout 2             | `de7fd3d83856`  |
| 2421   | Layout 2             | `de7fd3d83856`  |
| 2414   | Layout 2             | `de7fd3d83856`  |
| 2407   | Layout 2             | `de7fd3d83856`  |
| 2401   | Layout 2             | `de7fd3d83856`  |
| 2397   | Layout 2             | `de7fd3d83856`  |
| 2393   | Layout 2             | `de7fd3d83856`  |
| 2384   | Layout 2             | `de7fd3d83856`  |
| 2378   | Layout 2             | `de7fd3d83856`  |
| 2372   | Layout 2             | `de7fd3d83856`  |
| 2358   | Layout 2             | `de7fd3d83856`  |
| 2352   | Layout 2             | `de7fd3d83856`  |
| 2347   | Layout 2             | `de7fd3d83856`  |
| 2343   | Layout 2             | `de7fd3d83856`  |
| 2335   | Layout 2             | `de7fd3d83856`  |
| 2327   | Layout 2             | `de7fd3d83856`  |
| 2324   | Layout 2             | `de7fd3d83856`  |
| 2319   | Layout 2             | `de7fd3d83856`  |
| 2313   | Layout 2             | `de7fd3d83856`  |
| 2308   | Layout 2             | `de7fd3d83856`  |
| 2302   | Layout 2             | `de7fd3d83856`  |
| 2295   | Layout 2             | `de7fd3d83856`  |
| 2290   | Layout 2             | `de7fd3d83856`  |
| 2284   | Layout 2             | `de7fd3d83856`  |
| 2276   | Layout 2             | `de7fd3d83856`  |
| 2269   | Layout 2             | `de7fd3d83856`  |
| 2259   | Layout 2             | `de7fd3d83856`  |
| 2250   | Layout 2             | `de7fd3d83856`  |
| 2243   | Layout 2             | `de7fd3d83856`  |
| 2235   | Layout 2             | `de7fd3d83856`  |
| 2229   | Layout 2             | `de7fd3d83856`  |
| 2224   | Layout 2             | `de7fd3d83856`  |
| 2218   | Layout 2             | `de7fd3d83856`  |
| 2215   | Layout 2             | `de7fd3d83856`  |
| 2207   | Layout 2             | `de7fd3d83856`  |
| 2203   | Layout 2             | `de7fd3d83856`  |
| 2196   | Layout 2             | `de7fd3d83856`  |
| 2192   | Layout 2             | `de7fd3d83856`  |
| 2189   | Layout 2             | `de7fd3d83856`  |
| 2183   | Layout 2             | `de7fd3d83856`  |
| 2179   | Layout 2             | `de7fd3d83856`  |
| 2171   | Layout 2             | `de7fd3d83856`  |
| 2163   | Layout 2             | `de7fd3d83856`  |
| 2156   | Layout 2             | `de7fd3d83856`  |
| 2151   | Layout 2             | `de7fd3d83856`  |
| 2147   | Layout 2             | `de7fd3d83856`  |
| 2142   | Layout 2             | `de7fd3d83856`  |
| 2138   | Layout 2             | `de7fd3d83856`  |
| 2134   | Layout 2             | `de7fd3d83856`  |
| 2130   | Layout 2             | `de7fd3d83856`  |
| 2122   | Layout 1             | `de7fd3d83856`  |
| 2107   | Layout 1             | `de7fd3d83856`  |
| 2098   | Layout 1             | `de7fd3d83856`  |
| 2089   | Layout 1             | `de7fd3d83856`  |
| 2081   | Layout 1             | `de7fd3d83856`  |
| 2073   | Layout 1             | `de7fd3d83856`  |
| 2067   | Layout 1             | `de7fd3d83856`  |
| 2063   | Layout 1             | `de7fd3d83856`  |
| 2059   | Layout 1             | `de7fd3d83856`  |
| 2052   | Layout 1             | `de7fd3d83856`  |
| 2044   | Layout 1             | `de7fd3d83856`  |
| 2039   | Layout 1             | `de7fd3d83856`  |
| 2032   | Layout 1             | `de7fd3d83856`  |
| 2025   | Layout 1             | `de7fd3d83856`  |
| 2011   | Layout 1             | `de7fd3d83856`  |
| 2005   | Layout 1             | `de7fd3d83856`  |
| 2000   | Layout 1             | `de7fd3d83856`  |
| 1996   | Layout 1             | `de7fd3d83856`  |
| 1991   | Layout 1             | `de7fd3d83856`  |
| 1985   | Layout 1             | `de7fd3d83856`  |
| 1980   | Layout 1             | `de7fd3d83856`  |
| 1969   | Layout 1             | `de7fd3d83856`  |
| 1964   | Layout 1             | `de7fd3d83856`  |
| 1958   | Layout 1             | `de7fd3d83856`  |
| 1950   | Layout 1             | `de7fd3d83856`  |
| 1945   | Layout 1             | `de7fd3d83856`  |
| 1937   | Layout 1             | `de7fd3d83856`  |
| 1933   | Layout 1             | `de7fd3d83856`  |
| 1927   | Layout 1             | `de7fd3d83856`  |
| 1921   | Layout 1             | `de7fd3d83856`  |
| 1914   | Layout 1             | `de7fd3d83856`  |
| 1908   | Layout 1             | `de7fd3d83856`  |
| 1897   | Layout 1             | `de7fd3d83856`  |
| 1892   | Layout 1             | `de7fd3d83856`  |
| 1886   | Layout 1             | `de7fd3d83856`  |
| 1881   | Layout 1             | `de7fd3d83856`  |
| 1871   | Layout 1             | `de7fd3d83856`  |
| 1866   | Layout 1             | `de7fd3d83856`  |
| 1862   | Layout 1             | `de7fd3d83856`  |
| 1854   | Layout 1             | `de7fd3d83856`  |
| 1846   | Layout 1             | `de7fd3d83856`  |
| 1838   | Layout 1             | `de7fd3d83856`  |
| 1832   | Layout 1             | `de7fd3d83856`  |
| 1826   | Layout 1             | `de7fd3d83856`  |
| 1822   | Layout 1             | `de7fd3d83856`  |
| 1818   | Layout 1             | `de7fd3d83856`  |
| 1804   | Layout 1             | `de7fd3d83856`  |
| 1794   | Layout 1             | `de7fd3d83856`  |
| 1790   | Layout 1             | `de7fd3d83856`  |
| 1784   | Layout 1             | `de7fd3d83856`  |
| 1774   | Layout 1             | `de7fd3d83856`  |
| 1771   | Layout 1             | `de7fd3d83856`  |
| 1762   | Layout 1             | `de7fd3d83856`  |
| 1759   | Layout 1             | `de7fd3d83856`  |
| 1754   | Layout 1             | `de7fd3d83856`  |
| 1749   | Layout 1             | `de7fd3d83856`  |
| 1743   | Layout 1             | `de7fd3d83856`  |
| 1737   | Layout 1             | `de7fd3d83856`  |
| 1731   | Layout 1             | `de7fd3d83856`  |
| 1725   | Layout 1             | `de7fd3d83856`  |
| 1717   | Layout 1             | `de7fd3d83856`  |
| 1710   | Layout 1             | `de7fd3d83856`  |
| 1704   | Layout 1             | `de7fd3d83856`  |
| 1698   | Layout 1             | `de7fd3d83856`  |
| 1690   | Layout 1             | `de7fd3d83856`  |
| 1685   | Layout 1             | `de7fd3d83856`  |
| 1680   | Layout 1             | `de7fd3d83856`  |
| 1674   | Layout 1             | `de7fd3d83856`  |
| 1668   | Layout 1             | `de7fd3d83856`  |
| 1659   | Layout 1             | `de7fd3d83856`  |
| 1649   | Layout 1             | `de7fd3d83856`  |
| 1642   | Layout 1             | `de7fd3d83856`  |
| 1636   | Layout 1             | `de7fd3d83856`  |
| 1628   | Layout 1             | `de7fd3d83856`  |
| 1622   | Layout 1             | `de7fd3d83856`  |
| 1614   | Layout 1             | `de7fd3d83856`  |
| 1608   | Layout 1             | `de7fd3d83856`  |
| 1602   | Layout 1             | `de7fd3d83856`  |
| 1598   | Layout 1             | `de7fd3d83856`  |
| 1594   | Layout 1             | `de7fd3d83856`  |
| 1590   | Layout 1             | `de7fd3d83856`  |
| 1587   | Layout 1             | `de7fd3d83856`  |
| 1584   | Layout 1             | `de7fd3d83856`  |
| 1579   | Layout 1             | `de7fd3d83856`  |
| 1572   | Layout 1             | `de7fd3d83856`  |
| 1565   | Layout 1             | `de7fd3d83856`  |
| 1559   | Layout 1             | `de7fd3d83856`  |
| 1554   | Layout 1             | `de7fd3d83856`  |
| 1547   | Layout 1             | `de7fd3d83856`  |
| 1537   | Layout 1             | `de7fd3d83856`  |
| 1529   | Layout 1             | `de7fd3d83856`  |
| 1524   | Layout 1             | `de7fd3d83856`  |
| 1519   | Layout 1             | `de7fd3d83856`  |
| 1509   | Layout 1             | `de7fd3d83856`  |
| 1506   | Layout 1             | `de7fd3d83856`  |
| 1504   | Layout 1             | `de7fd3d83856`  |
| 1500   | Layout 1             | `de7fd3d83856`  |
| 1493   | Layout 1             | `de7fd3d83856`  |
| 1489   | Layout 1             | `de7fd3d83856`  |
| 1485   | Layout 1             | `de7fd3d83856`  |
| 1481   | Layout 1             | `de7fd3d83856`  |
| 1474   | Layout 1             | `de7fd3d83856`  |
| 1466   | Layout 1             | `de7fd3d83856`  |
| 1462   | Layout 1             | `de7fd3d83856`  |
| 1459   | Layout 1             | `de7fd3d83856`  |
| 1453   | Layout 1             | `de7fd3d83856`  |
| 1450   | Layout 1             | `de7fd3d83856`  |
| 1445   | Layout 1             | `de7fd3d83856`  |
| 1439   | Layout 1             | `de7fd3d83856`  |
| 1433   | Layout 1             | `de7fd3d83856`  |
| 1430   | Layout 1             | `de7fd3d83856`  |
| 1426   | Layout 1             | `de7fd3d83856`  |
| 1421   | Layout 1             | `de7fd3d83856`  |
| 1417   | Layout 1             | `de7fd3d83856`  |
| 1416   | Layout 1             | `de7fd3d83856`  |
| 1409   | Layout 1             | `de7fd3d83856`  |
| 1405   | Layout 1             | `de7fd3d83856`  |
| 1401   | Layout 1             | `de7fd3d83856`  |
| 1396   | Layout 1             | `de7fd3d83856`  |
| 1391   | Layout 1             | `de7fd3d83856`  |
| 1390   | Layout 1             | `de7fd3d83856`  |
| 1386   | Layout 1             | `de7fd3d83856`  |
| 1381   | Layout 1             | `de7fd3d83856`  |
| 1379   | Layout 1             | `de7fd3d83856`  |
| 1372   | Layout 1             | `de7fd3d83856`  |
| 1366   | Layout 1             | `de7fd3d83856`  |
| 1364   | Layout 1             | `de7fd3d83856`  |
| 1363   | Layout 1             | `de7fd3d83856`  |
| 1360   | Layout 1             | `de7fd3d83856`  |
| 1358   | Layout 1             | `de7fd3d83856`  |
| 1355   | Layout 1             | `de7fd3d83856`  |
| 1351   | Layout 1             | `de7fd3d83856`  |
| 1348   | No documented layout | `de7fd3d83856`  |
| 1346   | No documented layout | `de7fd3d83856`  |
| 1341   | No documented layout | `de7fd3d83856`  |
| 1340   | No documented layout | `de7fd3d83856`  |
| 1338   | No documented layout | `de7fd3d83856`  |
| 1335   | No documented layout | `de7fd3d83856`  |
| 1333   | No documented layout | `de7fd3d83856`  |
| 1329   | No documented layout | `de7fd3d83856`  |
| 1327   | No documented layout | `de7fd3d83856`  |
| 1324   | No documented layout | `de7fd3d83856`  |
| 1321   | No documented layout | `de7fd3d83856`  |
| 1319   | No documented layout | `de7fd3d83856`  |
| 1318   | No documented layout | `de7fd3d83856`  |
| 1316   | No documented layout | `de7fd3d83856`  |
| 1313   | No documented layout | `de7fd3d83856`  |
| 1311   | No documented layout | `de7fd3d83856`  |
| 1309   | No documented layout | `de7fd3d83856`  |
| 1304   | No documented layout | `de7fd3d83856`  |
| 1292   | No documented layout | `de7fd3d83856`  |
| 1286   | No documented layout | `de7fd3d83856`  |
| 1280   | No documented layout | `de7fd3d83856`  |
| 1276   | No documented layout | `de7fd3d83856`  |
| 1267   | No documented layout | `de7fd3d83856`  |
| 1261   | No documented layout | `de7fd3d83856`  |
| 1256   | No documented layout | `de7fd3d83856`  |
| 1250   | No documented layout | `de7fd3d83856`  |
| 1246   | No documented layout | `de7fd3d83856`  |
| 1239   | No documented layout | `de7fd3d83856`  |
| 1230   | No documented layout | `de7fd3d83856`  |
| 1226   | No documented layout | `de7fd3d83856`  |
| 1220   | No documented layout | `de7fd3d83856`  |
| 1217   | No documented layout | `de7fd3d83856`  |
| 1211   | No documented layout | `de7fd3d83856`  |
| 1210   | No documented layout | `de7fd3d83856`  |
| 1208   | No documented layout | `de7fd3d83856`  |
| 1203   | No documented layout | `de7fd3d83856`  |
| 1197   | No documented layout | `de7fd3d83856`  |
| 1194   | No documented layout | `de7fd3d83856`  |
| 1192   | No documented layout | `de7fd3d83856`  |
| 1187   | No documented layout | `de7fd3d83856`  |
| 1183   | No documented layout | `de7fd3d83856`  |
| 1177   | No documented layout | `de7fd3d83856`  |
| 1173   | No documented layout | `de7fd3d83856`  |
| 1167   | No documented layout | `de7fd3d83856`  |
| 1164   | No documented layout | `de7fd3d83856`  |
| 1156   | No documented layout | `de7fd3d83856`  |
| 1149   | No documented layout | `de7fd3d83856`  |
| 1144   | No documented layout | `de7fd3d83856`  |
| 1137   | No documented layout | `de7fd3d83856`  |
| 1132   | No documented layout | `de7fd3d83856`  |
| 1127   | No documented layout | `de7fd3d83856`  |
| 1122   | No documented layout | `de7fd3d83856`  |
| 1118   | No documented layout | `de7fd3d83856`  |
| 1114   | No documented layout | `de7fd3d83856`  |
| 1109   | No documented layout | `de7fd3d83856`  |
| 1102   | No file              | `de7fd3d83856`  |
| 1096   | No file              | `de7fd3d83856`  |
| 1088   | No file              | `de7fd3d83856`  |
| 1081   | No file              | `de7fd3d83856`  |
| 1076   | No file              | `de7fd3d83856`  |
| 1069   | No file              | `de7fd3d83856`  |
| 1064   | No file              | `de7fd3d83856`  |
| 1058   | No file              | `de7fd3d83856`  |
| 1051   | No file              | `de7fd3d83856`  |
| 1044   | No file              | `de7fd3d83856`  |
| 1036   | No file              | `de7fd3d83856`  |
| 1026   | No file              | `de7fd3d83856`  |
| 1016   | No file              | `de7fd3d83856`  |
| 1009   | No file              | `de7fd3d83856`  |
| 1005   | No file              | `de7fd3d83856`  |
| 1000   | No file              | `de7fd3d83856`  |
| 998    | No file              | `de7fd3d83856`  |
| 990    | No file              | `de7fd3d83856`  |
| 979    | No file              | `de7fd3d83856`  |
| 972    | No file              | `de7fd3d83856`  |
| 963    | No file              | `de7fd3d83856`  |
| 955    | No file              | `de7fd3d83856`  |
| 946    | No file              | `de7fd3d83856`  |
| 938    | No file              | `de7fd3d83856`  |
| 927    | No file              | `de7fd3d83856`  |
| 911    | No file              | `de7fd3d83856`  |
| 904    | No file              | `de7fd3d83856`  |
| 899    | No file              | `de7fd3d83856`  |
| 894    | No file              | `de7fd3d83856`  |
| 885    | No file              | `de7fd3d83856`  |
| 879    | No file              | `de7fd3d83856`  |
| 872    | No file              | `de7fd3d83856`  |
| 864    | No file              | `de7fd3d83856`  |
| 855    | No file              | `de7fd3d83856`  |
| 853    | No file              | `de7fd3d83856`  |
| 845    | No file              | `de7fd3d83856`  |
| 837    | No file              | `de7fd3d83856`  |
| 829    | No documented layout | `de7fd3d83856`  |
| 822    | No documented layout | `de7fd3d83856`  |
| 814    | No documented layout | `de7fd3d83856`  |
| 805    | No documented layout | `de7fd3d83856`  |
| 794    | No documented layout | `de7fd3d83856`  |
| 787    | No documented layout | `de7fd3d83856`  |
| 780    | No documented layout | `de7fd3d83856`  |
| 771    | No documented layout | `de7fd3d83856`  |
| 760    | No documented layout | `de7fd3d83856`  |
| 748    | No documented layout | `de7fd3d83856`  |
| 741    | No documented layout | `de7fd3d83856`  |
| 736    | No documented layout | `de7fd3d83856`  |
| 731    | No documented layout | `de7fd3d83856`  |
| 723    | No documented layout | `de7fd3d83856`  |
| 711    | No documented layout | `de7fd3d83856`  |
| 707    | No documented layout | `de7fd3d83856`  |
| 697    | No documented layout | `de7fd3d83856`  |
| 689    | No documented layout | `de7fd3d83856`  |
| 683    | No documented layout | `de7fd3d83856`  |
| 678    | No documented layout | `de7fd3d83856`  |
| 670    | No documented layout | `de7fd3d83856`  |
| 661    | No documented layout | `de7fd3d83856`  |
| 656    | No documented layout | `de7fd3d83856`  |
| 652    | No documented layout | `de7fd3d83856`  |
| 643    | No documented layout | `de7fd3d83856`  |
| 637    | No documented layout | `de7fd3d83856`  |
| 630    | No documented layout | `de7fd3d83856`  |
| 627    | No documented layout | `de7fd3d83856`  |
| 621    | No documented layout | `de7fd3d83856`  |
| 617    | No documented layout | `de7fd3d83856`  |
| 615    | No documented layout | `de7fd3d83856`  |
| 606    | No documented layout | `de7fd3d83856`  |
| 599    | No documented layout | `de7fd3d83856`  |
| 592    | No documented layout | `de7fd3d83856`  |
| 586    | No documented layout | `de7fd3d83856`  |
| 577    | No documented layout | `de7fd3d83856`  |
| 569    | No documented layout | `de7fd3d83856`  |
| 561    | No documented layout | `de7fd3d83856`  |
| 554    | No documented layout | `de7fd3d83856`  |
| 542    | No documented layout | `de7fd3d83856`  |
| 532    | No documented layout | `de7fd3d83856`  |
| 531    | No documented layout | `de7fd3d83856`  |
| 526    | No documented layout | `de7fd3d83856`  |
| 521    | No documented layout | `de7fd3d83856`  |
| 517    | No documented layout | `de7fd3d83856`  |
| 510    | No documented layout | `de7fd3d83856`  |
| 508    | No documented layout | `de7fd3d83856`  |
| 504    | No documented layout | `de7fd3d83856`  |
| 497    | No documented layout | `de7fd3d83856`  |
| 491    | No documented layout | `de7fd3d83856`  |
| 485    | No documented layout | `de7fd3d83856`  |
| 478    | No documented layout | `de7fd3d83856`  |
| 472    | No documented layout | `de7fd3d83856`  |
| 466    | No documented layout | `de7fd3d83856`  |
| 457    | No documented layout | `de7fd3d83856`  |
| 452    | No documented layout | `de7fd3d83856`  |
| 449    | No documented layout | `de7fd3d83856`  |
| 435    | No documented layout | `de7fd3d83856`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                  |
| --------------------- | -------- | --------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Resolves node names/descriptions (type 29) and NPC names (type 6)     |

All multi-byte values are little-endian unless noted otherwise.

## Layout 2

### File Layout

| Offset              | Type                      | Field              | Notes                                                           |
| ------------------- | ------------------------- | ------------------ | --------------------------------------------------------------- |
| `+0x00`             | char[4]                   | magic              | `PABR` (ASCII)                                                  |
| `+0x04`             | u32                       | record_count       | Observed `1003` (2026-09-27 client: `1080`)                     |
| `+0x08`             | Node Record[record_count] | records            | 117-byte head plus seven counted lists, packed back-to-back     |
| `records+0x00`      | Footer                    | footer             | `u32 count` plus `count` 6-byte rows; observed `111` rows       |
| `footer+0x00`       | String Table              | string_table       | `u32 count` plus Korean strings; observed `622` entries         |
| `string_table+0x00` | u32                       | string_table_start | Absolute file offset of `string_table.count`; observed `157953` |
| `string_table+0x04` | u32                       | zero               | Observed `0`                                                    |

Walking the records with this layout ends at `157283`, the footer ends at `157953` (equal to `string_table_start`) and the string table ends exactly at `EOF-8`, so the file tiles with no gaps.

### Node Record (variable: 117 bytes + lists)

| Offset  | Type      | Field | Notes                         |
| ------- | --------- | ----- | ----------------------------- |
| `+0x00` | Node Head | head  | See Node Head                 |
| `+0x75` | List[7]   | lists | Seven counted lists, see List |

### Node Head (117 bytes)

| Offset  | Type      | Field                 | Notes                                                                                                                                                 |
| ------- | --------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+0x00` | u16       | node_key              | LOC `str_type=29`, `str_id1=node_key`; unique; all 1003 resolve                                                                                       |
| `+0x02` | u16       | unknown_02            | Always `0`                                                                                                                                            |
| `+0x04` | u8        | enabled               | `1` on 999 records; `0` on 4 records whose name is `UnKnown` (1503, 1706, 1831, 1839)                                                                 |
| `+0x05` | u8        | node_kind             | Client `ExplorationNodeType`; see table below                                                                                                         |
| `+0x06` | u16       | node_key_copy         | Equals `node_key` in all 1003 records                                                                                                                 |
| `+0x08` | u16       | unknown_08            | Always `0`                                                                                                                                            |
| `+0x0A` | u16       | name_index            | Index into `string_table`; Korean node name (608 distinct)                                                                                            |
| `+0x0C` | u16       | unknown_0c            | Always `0`                                                                                                                                            |
| `+0x0E` | u8        | unknown_0e            | Always `1`                                                                                                                                            |
| `+0x0F` | u8        | unknown_0f            | Always `0`                                                                                                                                            |
| `+0x10` | u8        | has_contribution_cost | `1` exactly when `contribution > 0` (1003/1003); `0` on cities, towns, banks and some sea nodes                                                       |
| `+0x11` | u8        | is_main_alt           | Equals `is_main` except on Ossuary 133, Ossuary 134 and Velia Beach 1898                                                                              |
| `+0x12` | u8        | is_main               | Exact inverse of `is_sub_node` (1003/1003)                                                                                                            |
| `+0x13` | u8        | zone_index            | Sparse (51 nonzero, 48 distinct); meaning unconfirmed                                                                                                 |
| `+0x14` | u8        | zone_category         | Sparse; `1` islands, `2` Valencia nodes, `5` and `6` newer regions; see Open Questions                                                                |
| `+0x15` | u8        | grind_zone            | Sparse (25 nonzero); meaning unconfirmed                                                                                                              |
| `+0x16` | u8        | grind_tier            | `2` on 11 records, `3` on Star's End 1704; meaning unconfirmed                                                                                        |
| `+0x17` | u32       | sub_key               | Unique when nonzero (522 records, all main nodes); `0` on every sub-node                                                                              |
| `+0x1B` | u32       | sub_key_copy          | Equals `sub_key` or is `0` (40 main nodes, e.g. Velia, Heidel, Glish)                                                                                 |
| `+0x1F` | f32       | radius                | Examples `2700.0`, `9700.0`, `12700.0`; `0.0` only on Duvencrune 1651 (client 3464), a second Duvencrune far off the map that the Map view leaves out |
| `+0x23` | f32       | radius_squared        | `radius²` in all records                                                                                                                              |
| `+0x27` | u32       | description_index     | Index into `string_table`; 13 shared Korean descriptions, each maps 1:1 to LOC type 29 `str_id4=1`                                                    |
| `+0x2B` | u16       | manager_family_id     | Character ID (LOC type 6) shared by a main node and its production nodes; `0` on 120 records                                                          |
| `+0x2D` | u16       | representative_id     | Town ruler/representative character ID (LOC type 6); set on 20 town/city records only                                                                 |
| `+0x2F` | u32       | packed_index          | Bit 17 (`0x20000`) set in all records; low 17 bits `0` on 768 records, otherwise mostly unique                                                        |
| `+0x33` | u32       | packed_area           | Low 16 bits always `0`; high 16 bits take 44 distinct values                                                                                          |
| `+0x37` | bytes[39] | unknown_37            | Always `0`                                                                                                                                            |
| `+0x5E` | u8        | contribution          | Contribution-point cost, `0`-`3`                                                                                                                      |
| `+0x5F` | bytes[9]  | unknown_5f            | Always `0`                                                                                                                                            |
| `+0x68` | f32[3]    | position              | Label/exploration anchor; sub-nodes repeat their parent's position                                                                                    |
| `+0x74` | u8        | is_sub_node           | `0` main node (583), `1` sub-node (420)                                                                                                               |

### List (variable: 4 bytes + values)

Seven lists follow the head, each `[u32 count][count × u32]`.

| Offset  | Type       | Field  | Notes               |
| ------- | ---------- | ------ | ------------------- |
| `+0x00` | u32        | count  | Number of values    |
| `+0x04` | u32[count] | values | See the table below |

| List | Observed lengths | Content                                                                         |
| ---- | ---------------- | ------------------------------------------------------------------------------- |
| 0    | 1-3              | Regional grouping hash; 31 distinct values; 1 entry on 997 records               |
| 1-5  | 0-49             | Knowledge entry IDs (LOC `str_type=34`); all 1947 values are `mentalcard.dbss` entries |
| 6    | 0                | Always empty                                                                    |

Lists 2-5 are populated on only 41 records, mostly towns, cities, gates and hubs (for example Velia, Arehaza, Tarif, Heidel, Calpheon).

### Footer (variable: 4 bytes + rows)

| Offset  | Type              | Field | Notes          |
| ------- | ----------------- | ----- | -------------- |
| `+0x00` | u32               | count | Number of rows |
| `+0x04` | Footer Row[count] | rows  | See Footer Row |

### Footer Row (6 bytes)

| Offset  | Type | Field      | Notes                                                               |
| ------- | ---- | ---------- | ------------------------------------------------------------------- |
| `+0x00` | u16  | index      | 111 distinct values in `0`-`1454`; not sorted                       |
| `+0x02` | u16  | node_key   | Always a valid main node key; mostly Dangerous (53) and Normal (49) |
| `+0x04` | u16  | unknown_04 | Always `0`                                                          |

Some nodes appear twice (Castle Ruins 324 with index 21 and 153, Bloody Monastery 325 with 19 and 150).

### String Table (variable: 4 bytes + strings)

Each entry is a `pstr`: the u8 `is_wide` is `1` (UTF-16LE) on every entry but
the empty one (`0`, UTF-8), the u32 is the payload length in bytes with no
terminator, and the payload is Korean text.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Observed `622`      |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Layout 1

On client 1784 the file had no Footer: the String Table followed the last
Node Record. The Node Head was 115 bytes: it held one zone byte pair
(`zone_index`, `zone_category`) without `grind_zone` and `grind_tier`,
`sub_key` and `sub_key_copy` were u16, a u16 `unknown_29` followed
`representative_id`, and `unknown_5f` was 11 bytes. The File Layout, the
Node Record and the Node Head differ from Layout 2. Field names keep Layout
2's offsets, so `radius` sits at `+0x19` here. On client 1784 the file holds
816 records and 520 strings.

### File Layout

| Offset              | Type                      | Field              | Notes                                           |
| ------------------- | ------------------------- | ------------------ | ----------------------------------------------- |
| `+0x00`             | char[4]                   | magic              | `PABR` (ASCII)                                  |
| `+0x04`             | u32                       | record_count       |                                                 |
| `+0x08`             | Node Record[record_count] | records            | 115-byte head plus seven counted lists          |
| `records+0x00`      | String Table              | string_table       | Directly after the records; there is no Footer  |
| `string_table+0x00` | u32                       | string_table_start | Absolute file offset of `string_table.count`    |
| `string_table+0x04` | u32                       | zero               |                                                 |

### Node Record (variable: 115 bytes + lists)

| Offset  | Type      | Field | Notes |
| ------- | --------- | ----- | ----- |
| `+0x00` | Node Head | head  |       |
| `+0x73` | List[7]   | lists |       |

### Node Head (115 bytes)

| Offset  | Type      | Field                 | Notes                                                                     |
| ------- | --------- | --------------------- | ------------------------------------------------------------------------- |
| `+0x00` | u16       | node_key              |                                                                           |
| `+0x02` | u16       | unknown_02            |                                                                           |
| `+0x04` | u8        | enabled               |                                                                           |
| `+0x05` | u8        | node_kind             |                                                                           |
| `+0x06` | u16       | node_key_copy         |                                                                           |
| `+0x08` | u16       | unknown_08            |                                                                           |
| `+0x0A` | u16       | name_index            |                                                                           |
| `+0x0C` | u16       | unknown_0c            |                                                                           |
| `+0x0E` | u8        | unknown_0e            |                                                                           |
| `+0x0F` | u8        | unknown_0f            |                                                                           |
| `+0x10` | u8        | has_contribution_cost |                                                                           |
| `+0x11` | u8        | is_main_alt           |                                                                           |
| `+0x12` | u8        | is_main               |                                                                           |
| `+0x13` | u8        | zone_index            | Same value range as Layout 2; a value here reappears in Layout 2 as `zone_index` or as `grind_zone` |
| `+0x14` | u8        | zone_category         | `0` to `3`, paired with `zone_index` as in Layout 2                       |
| `+0x15` | u16       | sub_key               |                                                                           |
| `+0x17` | u16       | sub_key_copy          |                                                                           |
| `+0x19` | f32       | radius                |                                                                           |
| `+0x1D` | f32       | radius_squared        |                                                                           |
| `+0x21` | u32       | description_index     |                                                                           |
| `+0x25` | u16       | manager_family_id     |                                                                           |
| `+0x27` | u16       | representative_id     |                                                                           |
| `+0x29` | u16       | unknown_29            | A character ID on 21 records (`40001` on Velia 1, `41010` on Heidel 301), else `0` |
| `+0x2B` | u32       | packed_index          |                                                                           |
| `+0x2F` | u32       | packed_area           |                                                                           |
| `+0x33` | bytes[39] | unknown_37            |                                                                           |
| `+0x5A` | u8        | contribution          |                                                                           |
| `+0x5B` | bytes[11] | unknown_5f            | Always `0` on client 1784                                                 |
| `+0x66` | f32[3]    | position              |                                                                           |
| `+0x72` | u8        | is_sub_node           |                                                                           |

## `node_kind` Values

Names come from the client's `CppEnums.ExplorationNodeType` in `global_define_cpp_enum.luac` (member order `eExplorationNodeType_Normal` ... `eExplorationNodeType_Excavation`, then `_Count`=16; the client spells member 1 `Viliage`).

| Value | Enum         | Count | Examples                                           |
| ----- | ------------ | ----- | -------------------------------------------------- |
| 0     | Normal       | 436   | Wale Farm 65, Wolf Hills 66, Racid Island 1008      |
| 1     | Viliage      | 33    | Western Guard Camp 2, Shakatu 1314, Tarif 1141      |
| 2     | City         | 13    | Velia 1, Heidel 301, Calpheon 601, Altinova 1101    |
| 3     | Gate         | 51    | Western Gateway 4, Heidel Pass 6, Mediah Castle 1152 |
| 4     | Farm         | 50    | Potato Farming 131, Cinnamon Farming 1207           |
| 5     | Trade        | 5     | Bartali Farm 21, Alejandro Farm 321, Grándiha 1738  |
| 6     | Collect      | 61    | Gathering sub-nodes                                 |
| 7     | Quarry       | 68    | Mining sub-nodes                                    |
| 8     | Logging      | 64    | Lumbering sub-nodes                                 |
| 9     | Dangerous    | 68    | Cron Castle 3, Goblin Cave 23                       |
| 10    | Finance      | 24    | Investment Bank sub-nodes                           |
| 11    | FishTrap     | 41    | Fish Drying Yard sub-nodes                          |
| 12    | MinorFinance | 2     | Norma Leight 611 and Valentine 612 Investment Banks |
| 13    | MonopolyFarm | 44    | Specialties sub-nodes                               |
| 14    | Craft        | 7     | Chicken Meat Production 132, Honey Production 432   |
| 15    | Excavation   | 36    | Excavation sub-nodes, Chiro's Figurehead Workshop 1736 |

## Manager Families

`manager_family_id` groups 883 records into 494 families. Each family normally has exactly one main node plus its production sub-nodes (Wale 40605: Wale Farm 65, Specialties 109, Olives 204). Exceptions:

| Family                 | Shape                                                                 |
| ---------------------- | --------------------------------------------------------------------- |
| 47608 Jinwan           | Four Farm sub-nodes (1879-1882), no main node                         |
| 47278 Borabae          | Farm/Gathering sub-nodes (1826-1829), no main node                    |
| 40001 Islin Bartali    | Four Normal pseudo nodes (858, 961, 962, 963), all flagged sub-node   |
| 40025 Emma Bartali     | Bartali Farm 21 plus Ossuary 133 and 134 as extra main nodes          |
| 40026 Severo Loggia    | Loggia Farm 26 plus Velia Beach 1898 as an extra main node            |

Two main nodes have `contribution > 0` but no family: Duvencrune 1651 (1 CP, the live city is 1649) and `UnKnown` 1706 (3 CP).

## Notes

- Cross-checked against an independent node dataset (849 nodes, keyed by the same `node_key`): `contribution` matches the node's CP cost on all 849, `is_sub_node` matches on 847, and every node that dataset marks as a city has `node_kind` `1` or `2`. The exceptions are Mining site 156 and Fish Drying Yard 2 (1044), which the file flags as sub-nodes, and Oquilla's Eye 1727, which is kind `City` there but not a city in the dataset.
- The file has no same-stem companion in the current PAZ listing. The handler loads `waypoint_binary/mapdata_realexplore2.bwp` for the Connections columns.
- Counts in this doc are from the pre-2026-09-27 fixture. The 2026-09-27 client has 1080 records: 615 main nodes and 465 sub-nodes (was 583 and 420). Velia (`1`) lists 46 knowledge IDs in both.
- The reference project reports 1037 records, 494 families with 914 nodes and a third CP-without-manager record (2055); the current client file has 1003 records, 494 families with 883 nodes, and no node 2055.
- LOC type 34 also has entries for 987 of the 1003 keys, but they are unrelated knowledge entries (key 65 is `Cron Castle Altar` in type 34, while the inline Korean name `웨일 농장` matches type 29 `Wale Farm`).
- All 45 `planttown.bss` node IDs and all 394 `plantzone.dbss` record IDs are keys in this file; every plant zone is a sub-node.
- The node links are not in this file; they are in [`mapdata_realexplore2.bwp`](waypoint_bwp.md), keyed by the same node keys. There each plant zone has exactly one link, its parent node, which is not always the `manager_family_id` main node: Specialties 1563 links to Arehaza (1380), its family's main node is Areha Palm Forest (1379).
- On client 3458, 1,076 of the 1,080 nodes have links. The four without are Tiamat Sea (2114), Oceanus Sea (2113), Red Battlefield (1378) and Pit of the Undying (1745). Five links go to waypoints with no record here, for example Runn Gateway Intersection (1313) to 1320 and 1323 (`field(shakatu_area)`, `field(atumach)`); they have no LOC type 29 name either. The links match the in-game worldmap for the nodes I checked: Velia links to Bartali, Finto and Loggia Farms, Forest of Plunder, Coastal Cave, the two investment banks, Luivano Island and Velia Beach; Western Guard Camp to Western Gateway, Bandit's Den Byway, Imp Cave and Toscani Farm.
- The record anchor used by older tooling (`node_key` repeated at `+0x06`) still finds the correct 1003 offsets, but the exact layout above makes the scan unnecessary.

## Open Questions

### Sub Key Target

`sub_key` (`+0x17`) is unique per main node and absent on sub-nodes. The reference project calls it a waypoint-space key, but only 80 of the 522 values appear as keys in `mapdata_realexplore2.bwp`, whose keys are node keys. No LOC type covers the values either. Why `sub_key_copy` is zero on 40 main nodes (mostly newer regions plus Velia, Heidel and Glish) is also open.

### Zone Category Labels

The reference project labels `zone_category` as `1` island, `2` coastal, `5` inland/desert and `6` battlefield/ocean. In this file `1` covers 15 islands plus Wolf Hills and Longleaf Tree Sentry Post, `2` covers only Valencia nodes (Ancado Coast, Rakshan Observatory, Valencia Castle), and `5`/`6` cover newer regions (Tungrad Ruins, Atessahra, Great Red Spot). The values look like a content or region class rather than terrain.

### Grind Zone Fields

`zone_index`, `grind_zone` and `grind_tier` are sparse. The reference project describes `grind_zone` as a Marni/Elvia grind-zone index and `grind_tier` as a recommended-AP tier; neither is confirmed by another file. The tier looks doubtful: the 11 nodes with `2` include non-grind places such as Polly's Forest (1624) and Tooth Fairy Forest (1619) next to Gyfin Rhasia Temple (1626) and Desert Naga Temple (1322), and only Star's End (1704) has `3`. `grind_zone` equals `zone_index` on only 6 of its 25 nonzero records.

Open: what the 11 nodes with `grind_tier` `2` share. They are Roud Sulfur
Mine, Ash Forest, Gyfin Rhasia Temple, Polly's Forest, Tooth Fairy Forest,
Mirumok Ruins, Manshaum Forest, Navarn Steppe, Ancado Coast, Pilgrim's
Sanctum: Obedience and Desert Naga Temple; Star's End is the only `3`.

### Packed Index and Area

The `0x20000` flag in `packed_index` is constant, but the low 17 bits are zero on 768 records and non-unique elsewhere, so the reference project's "node enumeration" reading does not hold as stated. Cities carry round values (Velia 1, Heidel 101, Calpheon 301, Valencia City 1201). The target of `packed_area`'s high word (44 values) is not confirmed.

### Footer Index

The footer `index` values and why some nodes appear twice are not mapped to any other table.

### Knowledge List Roles

Lists 1-5 all hold knowledge entry IDs, but what separates list 1 from lists 2-5 (populated on 41 mostly town and hub records) is not confirmed. List 0's hash is not linked to another table.
