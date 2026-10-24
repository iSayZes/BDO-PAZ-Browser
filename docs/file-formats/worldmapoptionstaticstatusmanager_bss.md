# `worldmapoptionstaticstatusmanager.bss` Format

## Purpose

A world map option table of one world position per territory: on client
3482 its 14 rows count `0` to `13`, the LOC type 12 territory keys from
Balenos to Inner Edania, and each position lies inside the territory of
its row. What the world map does with the positions is open.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ------- | --------- |
| 1      | 3435 and later | 3483    | `worldmapoptionstaticstatusmanager.bss` | 244   | 14 Row  | 16        |

| Layout | File                                    | Known       | Unknown       |
| ------ | --------------------------------------- | ----------- | ------------- |
| 1      | `worldmapoptionstaticstatusmanager.bss` | 20 B (8.2%) | 224 B (91.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d530b6418a5e`  |
| 3482   | Layout 1 | `d530b6418a5e`  |
| 3474   | Layout 1 | `d530b6418a5e`  |
| 3473   | Layout 1 | `d530b6418a5e`  |
| 3464   | Layout 1 | `d530b6418a5e`  |
| 3458   | Layout 1 | `d530b6418a5e`  |
| 3454   | Layout 1 | `d530b6418a5e`  |
| 3444   | Layout 1 | `d530b6418a5e`  |
| 3435   | Layout 1 | `d530b6418a5e`  |
| 3426   | No file  | `d530b6418a5e`  |
| 3418   | No file  | `d530b6418a5e`  |
| 3412   | No file  | `d530b6418a5e`  |
| 3402   | No file  | `d530b6418a5e`  |
| 3396   | No file  | `d530b6418a5e`  |
| 3387   | No file  | `d530b6418a5e`  |
| 3381   | No file  | `d530b6418a5e`  |
| 3373   | No file  | `d530b6418a5e`  |
| 3364   | No file  | `d530b6418a5e`  |
| 3356   | No file  | `d530b6418a5e`  |
| 3349   | No file  | `d530b6418a5e`  |
| 3342   | No file  | `d530b6418a5e`  |
| 3335   | No file  | `d530b6418a5e`  |
| 3326   | No file  | `d530b6418a5e`  |
| 3321   | No file  | `d530b6418a5e`  |
| 3314   | No file  | `d530b6418a5e`  |
| 3303   | No file  | `d530b6418a5e`  |
| 3302   | No file  | `d530b6418a5e`  |
| 3293   | No file  | `d530b6418a5e`  |
| 3283   | No file  | `d530b6418a5e`  |
| 3275   | No file  | `d530b6418a5e`  |
| 3267   | No file  | `d530b6418a5e`  |
| 3258   | No file  | `d530b6418a5e`  |
| 3251   | No file  | `d530b6418a5e`  |
| 3242   | No file  | `d530b6418a5e`  |
| 3235   | No file  | `d530b6418a5e`  |
| 3229   | No file  | `d530b6418a5e`  |
| 3212   | No file  | `d530b6418a5e`  |
| 3203   | No file  | `d530b6418a5e`  |
| 3193   | No file  | `d530b6418a5e`  |
| 3186   | No file  | `d530b6418a5e`  |
| 3177   | No file  | `d530b6418a5e`  |
| 3169   | No file  | `d530b6418a5e`  |
| 3158   | No file  | `d530b6418a5e`  |
| 3151   | No file  | `d530b6418a5e`  |
| 3144   | No file  | `d530b6418a5e`  |
| 3133   | No file  | `d530b6418a5e`  |
| 3125   | No file  | `d530b6418a5e`  |
| 3118   | No file  | `d530b6418a5e`  |
| 3111   | No file  | `d530b6418a5e`  |
| 3103   | No file  | `d530b6418a5e`  |
| 3095   | No file  | `d530b6418a5e`  |
| 3086   | No file  | `d530b6418a5e`  |
| 3072   | No file  | `d530b6418a5e`  |
| 3062   | No file  | `d530b6418a5e`  |
| 3052   | No file  | `d530b6418a5e`  |
| 3045   | No file  | `d530b6418a5e`  |
| 3037   | No file  | `d530b6418a5e`  |
| 3030   | No file  | `d530b6418a5e`  |
| 3021   | No file  | `d530b6418a5e`  |
| 3012   | No file  | `d530b6418a5e`  |
| 3002   | No file  | `d530b6418a5e`  |
| 2995   | No file  | `d530b6418a5e`  |
| 2987   | No file  | `d530b6418a5e`  |
| 2978   | No file  | `d530b6418a5e`  |
| 2970   | No file  | `d530b6418a5e`  |
| 2959   | No file  | `d530b6418a5e`  |
| 2951   | No file  | `d530b6418a5e`  |
| 2942   | No file  | `d530b6418a5e`  |
| 2935   | No file  | `d530b6418a5e`  |
| 2932   | No file  | `d530b6418a5e`  |
| 2923   | No file  | `d530b6418a5e`  |
| 2919   | No file  | `d530b6418a5e`  |
| 2907   | No file  | `d530b6418a5e`  |
| 2900   | No file  | `d530b6418a5e`  |
| 2891   | No file  | `d530b6418a5e`  |
| 2882   | No file  | `d530b6418a5e`  |
| 2872   | No file  | `d530b6418a5e`  |
| 2863   | No file  | `d530b6418a5e`  |
| 2855   | No file  | `d530b6418a5e`  |
| 2849   | No file  | `d530b6418a5e`  |
| 2844   | No file  | `d530b6418a5e`  |
| 2834   | No file  | `d530b6418a5e`  |
| 2825   | No file  | `d530b6418a5e`  |
| 2819   | No file  | `d530b6418a5e`  |
| 2811   | No file  | `d530b6418a5e`  |
| 2803   | No file  | `d530b6418a5e`  |
| 2794   | No file  | `d530b6418a5e`  |
| 2783   | No file  | `d530b6418a5e`  |
| 2774   | No file  | `d530b6418a5e`  |
| 2765   | No file  | `d530b6418a5e`  |
| 2756   | No file  | `d530b6418a5e`  |
| 2750   | No file  | `d530b6418a5e`  |
| 2743   | No file  | `d530b6418a5e`  |
| 2736   | No file  | `d530b6418a5e`  |
| 2726   | No file  | `d530b6418a5e`  |
| 2717   | No file  | `d530b6418a5e`  |
| 2709   | No file  | `d530b6418a5e`  |
| 2703   | No file  | `d530b6418a5e`  |
| 2695   | No file  | `d530b6418a5e`  |
| 2684   | No file  | `d530b6418a5e`  |
| 2672   | No file  | `d530b6418a5e`  |
| 2665   | No file  | `d530b6418a5e`  |
| 2657   | No file  | `d530b6418a5e`  |
| 2649   | No file  | `d530b6418a5e`  |
| 2644   | No file  | `d530b6418a5e`  |
| 2637   | No file  | `d530b6418a5e`  |
| 2629   | No file  | `d530b6418a5e`  |
| 2619   | No file  | `d530b6418a5e`  |
| 2612   | No file  | `d530b6418a5e`  |
| 2606   | No file  | `d530b6418a5e`  |
| 2602   | No file  | `d530b6418a5e`  |
| 2601   | No file  | `d530b6418a5e`  |
| 2592   | No file  | `d530b6418a5e`  |
| 2583   | No file  | `d530b6418a5e`  |
| 2575   | No file  | `d530b6418a5e`  |
| 2567   | No file  | `d530b6418a5e`  |
| 2560   | No file  | `d530b6418a5e`  |
| 2553   | No file  | `d530b6418a5e`  |
| 2545   | No file  | `d530b6418a5e`  |
| 2538   | No file  | `d530b6418a5e`  |
| 2529   | No file  | `d530b6418a5e`  |
| 2519   | No file  | `d530b6418a5e`  |
| 2513   | No file  | `d530b6418a5e`  |
| 2510   | No file  | `d530b6418a5e`  |
| 2507   | No file  | `d530b6418a5e`  |
| 2503   | No file  | `d530b6418a5e`  |
| 2498   | No file  | `d530b6418a5e`  |
| 2492   | No file  | `d530b6418a5e`  |
| 2487   | No file  | `d530b6418a5e`  |
| 2480   | No file  | `d530b6418a5e`  |
| 2474   | No file  | `d530b6418a5e`  |
| 2468   | No file  | `d530b6418a5e`  |
| 2460   | No file  | `d530b6418a5e`  |
| 2453   | No file  | `d530b6418a5e`  |
| 2444   | No file  | `d530b6418a5e`  |
| 2438   | No file  | `d530b6418a5e`  |
| 2434   | No file  | `d530b6418a5e`  |
| 2429   | No file  | `d530b6418a5e`  |
| 2421   | No file  | `d530b6418a5e`  |
| 2414   | No file  | `d530b6418a5e`  |
| 2407   | No file  | `d530b6418a5e`  |
| 2401   | No file  | `d530b6418a5e`  |
| 2397   | No file  | `d530b6418a5e`  |
| 2393   | No file  | `d530b6418a5e`  |
| 2384   | No file  | `d530b6418a5e`  |
| 2378   | No file  | `d530b6418a5e`  |
| 2372   | No file  | `d530b6418a5e`  |
| 2358   | No file  | `d530b6418a5e`  |
| 2352   | No file  | `d530b6418a5e`  |
| 2347   | No file  | `d530b6418a5e`  |
| 2343   | No file  | `d530b6418a5e`  |
| 2335   | No file  | `d530b6418a5e`  |
| 2327   | No file  | `d530b6418a5e`  |
| 2324   | No file  | `d530b6418a5e`  |
| 2319   | No file  | `d530b6418a5e`  |
| 2313   | No file  | `d530b6418a5e`  |
| 2308   | No file  | `d530b6418a5e`  |
| 2302   | No file  | `d530b6418a5e`  |
| 2295   | No file  | `d530b6418a5e`  |
| 2290   | No file  | `d530b6418a5e`  |
| 2284   | No file  | `d530b6418a5e`  |
| 2276   | No file  | `d530b6418a5e`  |
| 2269   | No file  | `d530b6418a5e`  |
| 2259   | No file  | `d530b6418a5e`  |
| 2250   | No file  | `d530b6418a5e`  |
| 2243   | No file  | `d530b6418a5e`  |
| 2235   | No file  | `d530b6418a5e`  |
| 2229   | No file  | `d530b6418a5e`  |
| 2224   | No file  | `d530b6418a5e`  |
| 2218   | No file  | `d530b6418a5e`  |
| 2215   | No file  | `d530b6418a5e`  |
| 2207   | No file  | `d530b6418a5e`  |
| 2203   | No file  | `d530b6418a5e`  |
| 2196   | No file  | `d530b6418a5e`  |
| 2192   | No file  | `d530b6418a5e`  |
| 2189   | No file  | `d530b6418a5e`  |
| 2183   | No file  | `d530b6418a5e`  |
| 2179   | No file  | `d530b6418a5e`  |
| 2171   | No file  | `d530b6418a5e`  |
| 2163   | No file  | `d530b6418a5e`  |
| 2156   | No file  | `d530b6418a5e`  |
| 2151   | No file  | `d530b6418a5e`  |
| 2147   | No file  | `d530b6418a5e`  |
| 2142   | No file  | `d530b6418a5e`  |
| 2138   | No file  | `d530b6418a5e`  |
| 2134   | No file  | `d530b6418a5e`  |
| 2130   | No file  | `d530b6418a5e`  |
| 2122   | No file  | `d530b6418a5e`  |
| 2107   | No file  | `d530b6418a5e`  |
| 2098   | No file  | `d530b6418a5e`  |
| 2089   | No file  | `d530b6418a5e`  |
| 2081   | No file  | `d530b6418a5e`  |
| 2073   | No file  | `d530b6418a5e`  |
| 2067   | No file  | `d530b6418a5e`  |
| 2063   | No file  | `d530b6418a5e`  |
| 2059   | No file  | `d530b6418a5e`  |
| 2052   | No file  | `d530b6418a5e`  |
| 2044   | No file  | `d530b6418a5e`  |
| 2039   | No file  | `d530b6418a5e`  |
| 2032   | No file  | `d530b6418a5e`  |
| 2025   | No file  | `d530b6418a5e`  |
| 2011   | No file  | `d530b6418a5e`  |
| 2005   | No file  | `d530b6418a5e`  |
| 2000   | No file  | `d530b6418a5e`  |
| 1996   | No file  | `d530b6418a5e`  |
| 1991   | No file  | `d530b6418a5e`  |
| 1985   | No file  | `d530b6418a5e`  |
| 1980   | No file  | `d530b6418a5e`  |
| 1969   | No file  | `d530b6418a5e`  |
| 1964   | No file  | `d530b6418a5e`  |
| 1958   | No file  | `d530b6418a5e`  |
| 1950   | No file  | `d530b6418a5e`  |
| 1945   | No file  | `d530b6418a5e`  |
| 1937   | No file  | `d530b6418a5e`  |
| 1933   | No file  | `d530b6418a5e`  |
| 1927   | No file  | `d530b6418a5e`  |
| 1921   | No file  | `d530b6418a5e`  |
| 1914   | No file  | `d530b6418a5e`  |
| 1908   | No file  | `d530b6418a5e`  |
| 1897   | No file  | `d530b6418a5e`  |
| 1892   | No file  | `d530b6418a5e`  |
| 1886   | No file  | `d530b6418a5e`  |
| 1881   | No file  | `d530b6418a5e`  |
| 1871   | No file  | `d530b6418a5e`  |
| 1866   | No file  | `d530b6418a5e`  |
| 1862   | No file  | `d530b6418a5e`  |
| 1854   | No file  | `d530b6418a5e`  |
| 1846   | No file  | `d530b6418a5e`  |
| 1838   | No file  | `d530b6418a5e`  |
| 1832   | No file  | `d530b6418a5e`  |
| 1826   | No file  | `d530b6418a5e`  |
| 1822   | No file  | `d530b6418a5e`  |
| 1818   | No file  | `d530b6418a5e`  |
| 1804   | No file  | `d530b6418a5e`  |
| 1794   | No file  | `d530b6418a5e`  |
| 1790   | No file  | `d530b6418a5e`  |
| 1784   | No file  | `d530b6418a5e`  |
| 1774   | No file  | `d530b6418a5e`  |
| 1771   | No file  | `d530b6418a5e`  |
| 1762   | No file  | `d530b6418a5e`  |
| 1759   | No file  | `d530b6418a5e`  |
| 1754   | No file  | `d530b6418a5e`  |
| 1749   | No file  | `d530b6418a5e`  |
| 1743   | No file  | `d530b6418a5e`  |
| 1737   | No file  | `d530b6418a5e`  |
| 1731   | No file  | `d530b6418a5e`  |
| 1725   | No file  | `d530b6418a5e`  |
| 1717   | No file  | `d530b6418a5e`  |
| 1710   | No file  | `d530b6418a5e`  |
| 1704   | No file  | `d530b6418a5e`  |
| 1698   | No file  | `d530b6418a5e`  |
| 1690   | No file  | `d530b6418a5e`  |
| 1685   | No file  | `d530b6418a5e`  |
| 1680   | No file  | `d530b6418a5e`  |
| 1674   | No file  | `d530b6418a5e`  |
| 1668   | No file  | `d530b6418a5e`  |
| 1659   | No file  | `d530b6418a5e`  |
| 1649   | No file  | `d530b6418a5e`  |
| 1642   | No file  | `d530b6418a5e`  |
| 1636   | No file  | `d530b6418a5e`  |
| 1628   | No file  | `d530b6418a5e`  |
| 1622   | No file  | `d530b6418a5e`  |
| 1614   | No file  | `d530b6418a5e`  |
| 1608   | No file  | `d530b6418a5e`  |
| 1602   | No file  | `d530b6418a5e`  |
| 1598   | No file  | `d530b6418a5e`  |
| 1594   | No file  | `d530b6418a5e`  |
| 1590   | No file  | `d530b6418a5e`  |
| 1587   | No file  | `d530b6418a5e`  |
| 1584   | No file  | `d530b6418a5e`  |
| 1579   | No file  | `d530b6418a5e`  |
| 1572   | No file  | `d530b6418a5e`  |
| 1565   | No file  | `d530b6418a5e`  |
| 1559   | No file  | `d530b6418a5e`  |
| 1554   | No file  | `d530b6418a5e`  |
| 1547   | No file  | `d530b6418a5e`  |
| 1537   | No file  | `d530b6418a5e`  |
| 1529   | No file  | `d530b6418a5e`  |
| 1524   | No file  | `d530b6418a5e`  |
| 1519   | No file  | `d530b6418a5e`  |
| 1509   | No file  | `d530b6418a5e`  |
| 1506   | No file  | `d530b6418a5e`  |
| 1504   | No file  | `d530b6418a5e`  |
| 1500   | No file  | `d530b6418a5e`  |
| 1493   | No file  | `d530b6418a5e`  |
| 1489   | No file  | `d530b6418a5e`  |
| 1485   | No file  | `d530b6418a5e`  |
| 1481   | No file  | `d530b6418a5e`  |
| 1474   | No file  | `d530b6418a5e`  |
| 1466   | No file  | `d530b6418a5e`  |
| 1462   | No file  | `d530b6418a5e`  |
| 1459   | No file  | `d530b6418a5e`  |
| 1453   | No file  | `d530b6418a5e`  |
| 1450   | No file  | `d530b6418a5e`  |
| 1445   | No file  | `d530b6418a5e`  |
| 1439   | No file  | `d530b6418a5e`  |
| 1433   | No file  | `d530b6418a5e`  |
| 1430   | No file  | `d530b6418a5e`  |
| 1426   | No file  | `d530b6418a5e`  |
| 1421   | No file  | `d530b6418a5e`  |
| 1417   | No file  | `d530b6418a5e`  |
| 1416   | No file  | `d530b6418a5e`  |
| 1409   | No file  | `d530b6418a5e`  |
| 1405   | No file  | `d530b6418a5e`  |
| 1401   | No file  | `d530b6418a5e`  |
| 1396   | No file  | `d530b6418a5e`  |
| 1391   | No file  | `d530b6418a5e`  |
| 1390   | No file  | `d530b6418a5e`  |
| 1386   | No file  | `d530b6418a5e`  |
| 1381   | No file  | `d530b6418a5e`  |
| 1379   | No file  | `d530b6418a5e`  |
| 1372   | No file  | `d530b6418a5e`  |
| 1366   | No file  | `d530b6418a5e`  |
| 1364   | No file  | `d530b6418a5e`  |
| 1363   | No file  | `d530b6418a5e`  |
| 1360   | No file  | `d530b6418a5e`  |
| 1358   | No file  | `d530b6418a5e`  |
| 1355   | No file  | `d530b6418a5e`  |
| 1351   | No file  | `d530b6418a5e`  |
| 1348   | No file  | `d530b6418a5e`  |
| 1346   | No file  | `d530b6418a5e`  |
| 1341   | No file  | `d530b6418a5e`  |
| 1340   | No file  | `d530b6418a5e`  |
| 1338   | No file  | `d530b6418a5e`  |
| 1335   | No file  | `d530b6418a5e`  |
| 1333   | No file  | `d530b6418a5e`  |
| 1329   | No file  | `d530b6418a5e`  |
| 1327   | No file  | `d530b6418a5e`  |
| 1324   | No file  | `d530b6418a5e`  |
| 1321   | No file  | `d530b6418a5e`  |
| 1319   | No file  | `d530b6418a5e`  |
| 1318   | No file  | `d530b6418a5e`  |
| 1316   | No file  | `d530b6418a5e`  |
| 1313   | No file  | `d530b6418a5e`  |
| 1311   | No file  | `d530b6418a5e`  |
| 1309   | No file  | `d530b6418a5e`  |
| 1304   | No file  | `d530b6418a5e`  |
| 1292   | No file  | `d530b6418a5e`  |
| 1286   | No file  | `d530b6418a5e`  |
| 1280   | No file  | `d530b6418a5e`  |
| 1276   | No file  | `d530b6418a5e`  |
| 1267   | No file  | `d530b6418a5e`  |
| 1261   | No file  | `d530b6418a5e`  |
| 1256   | No file  | `d530b6418a5e`  |
| 1250   | No file  | `d530b6418a5e`  |
| 1246   | No file  | `d530b6418a5e`  |
| 1239   | No file  | `d530b6418a5e`  |
| 1230   | No file  | `d530b6418a5e`  |
| 1226   | No file  | `d530b6418a5e`  |
| 1220   | No file  | `d530b6418a5e`  |
| 1217   | No file  | `d530b6418a5e`  |
| 1211   | No file  | `d530b6418a5e`  |
| 1210   | No file  | `d530b6418a5e`  |
| 1208   | No file  | `d530b6418a5e`  |
| 1203   | No file  | `d530b6418a5e`  |
| 1197   | No file  | `d530b6418a5e`  |
| 1194   | No file  | `d530b6418a5e`  |
| 1192   | No file  | `d530b6418a5e`  |
| 1187   | No file  | `d530b6418a5e`  |
| 1183   | No file  | `d530b6418a5e`  |
| 1177   | No file  | `d530b6418a5e`  |
| 1173   | No file  | `d530b6418a5e`  |
| 1167   | No file  | `d530b6418a5e`  |
| 1164   | No file  | `d530b6418a5e`  |
| 1156   | No file  | `d530b6418a5e`  |
| 1149   | No file  | `d530b6418a5e`  |
| 1144   | No file  | `d530b6418a5e`  |
| 1137   | No file  | `d530b6418a5e`  |
| 1132   | No file  | `d530b6418a5e`  |
| 1127   | No file  | `d530b6418a5e`  |
| 1122   | No file  | `d530b6418a5e`  |
| 1118   | No file  | `d530b6418a5e`  |
| 1114   | No file  | `d530b6418a5e`  |
| 1109   | No file  | `d530b6418a5e`  |
| 1102   | No file  | `d530b6418a5e`  |
| 1096   | No file  | `d530b6418a5e`  |
| 1088   | No file  | `d530b6418a5e`  |
| 1081   | No file  | `d530b6418a5e`  |
| 1076   | No file  | `d530b6418a5e`  |
| 1069   | No file  | `d530b6418a5e`  |
| 1064   | No file  | `d530b6418a5e`  |
| 1058   | No file  | `d530b6418a5e`  |
| 1051   | No file  | `d530b6418a5e`  |
| 1044   | No file  | `d530b6418a5e`  |
| 1036   | No file  | `d530b6418a5e`  |
| 1026   | No file  | `d530b6418a5e`  |
| 1016   | No file  | `d530b6418a5e`  |
| 1009   | No file  | `d530b6418a5e`  |
| 1005   | No file  | `d530b6418a5e`  |
| 1000   | No file  | `d530b6418a5e`  |
| 998    | No file  | `d530b6418a5e`  |
| 990    | No file  | `d530b6418a5e`  |
| 979    | No file  | `d530b6418a5e`  |
| 972    | No file  | `d530b6418a5e`  |
| 963    | No file  | `d530b6418a5e`  |
| 955    | No file  | `d530b6418a5e`  |
| 946    | No file  | `d530b6418a5e`  |
| 938    | No file  | `d530b6418a5e`  |
| 927    | No file  | `d530b6418a5e`  |
| 911    | No file  | `d530b6418a5e`  |
| 904    | No file  | `d530b6418a5e`  |
| 899    | No file  | `d530b6418a5e`  |
| 894    | No file  | `d530b6418a5e`  |
| 885    | No file  | `d530b6418a5e`  |
| 879    | No file  | `d530b6418a5e`  |
| 872    | No file  | `d530b6418a5e`  |
| 864    | No file  | `d530b6418a5e`  |
| 855    | No file  | `d530b6418a5e`  |
| 853    | No file  | `d530b6418a5e`  |
| 845    | No file  | `d530b6418a5e`  |
| 837    | No file  | `d530b6418a5e`  |
| 829    | No file  | `d530b6418a5e`  |
| 822    | No file  | `d530b6418a5e`  |
| 814    | No file  | `d530b6418a5e`  |
| 805    | No file  | `d530b6418a5e`  |
| 794    | No file  | `d530b6418a5e`  |
| 787    | No file  | `d530b6418a5e`  |
| 780    | No file  | `d530b6418a5e`  |
| 771    | No file  | `d530b6418a5e`  |
| 760    | No file  | `d530b6418a5e`  |
| 748    | No file  | `d530b6418a5e`  |
| 741    | No file  | `d530b6418a5e`  |
| 736    | No file  | `d530b6418a5e`  |
| 731    | No file  | `d530b6418a5e`  |
| 723    | No file  | `d530b6418a5e`  |
| 711    | No file  | `d530b6418a5e`  |
| 707    | No file  | `d530b6418a5e`  |
| 697    | No file  | `d530b6418a5e`  |
| 689    | No file  | `d530b6418a5e`  |
| 683    | No file  | `d530b6418a5e`  |
| 678    | No file  | `d530b6418a5e`  |
| 670    | No file  | `d530b6418a5e`  |
| 661    | No file  | `d530b6418a5e`  |
| 656    | No file  | `d530b6418a5e`  |
| 652    | No file  | `d530b6418a5e`  |
| 643    | No file  | `d530b6418a5e`  |
| 637    | No file  | `d530b6418a5e`  |
| 630    | No file  | `d530b6418a5e`  |
| 627    | No file  | `d530b6418a5e`  |
| 621    | No file  | `d530b6418a5e`  |
| 617    | No file  | `d530b6418a5e`  |
| 615    | No file  | `d530b6418a5e`  |
| 606    | No file  | `d530b6418a5e`  |
| 599    | No file  | `d530b6418a5e`  |
| 592    | No file  | `d530b6418a5e`  |
| 586    | No file  | `d530b6418a5e`  |
| 577    | No file  | `d530b6418a5e`  |
| 569    | No file  | `d530b6418a5e`  |
| 561    | No file  | `d530b6418a5e`  |
| 554    | No file  | `d530b6418a5e`  |
| 542    | No file  | `d530b6418a5e`  |
| 532    | No file  | `d530b6418a5e`  |
| 531    | No file  | `d530b6418a5e`  |
| 526    | No file  | `d530b6418a5e`  |
| 521    | No file  | `d530b6418a5e`  |
| 517    | No file  | `d530b6418a5e`  |
| 510    | No file  | `d530b6418a5e`  |
| 508    | No file  | `d530b6418a5e`  |
| 504    | No file  | `d530b6418a5e`  |
| 497    | No file  | `d530b6418a5e`  |
| 491    | No file  | `d530b6418a5e`  |
| 485    | No file  | `d530b6418a5e`  |
| 478    | No file  | `d530b6418a5e`  |
| 472    | No file  | `d530b6418a5e`  |
| 466    | No file  | `d530b6418a5e`  |
| 457    | No file  | `d530b6418a5e`  |
| 452    | No file  | `d530b6418a5e`  |
| 449    | No file  | `d530b6418a5e`  |
| 435    | No file  | `d530b6418a5e`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (16 bytes)

| Offset  | Type   | Field      | Notes                                                |
| ------- | ------ | ---------- | ---------------------------------------------------- |
| `+0x00` | u16    | unknown_00 | The row's position, `0` to `13` on client 3482       |
| `+0x02` | u16    | unknown_02 | Equal to `unknown_00` on every row (client 3482)     |
| `+0x04` | f32[3] | unknown_04 | World `x, y, z`; see Positions                       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Positions

Client 3482, rounded to whole units, with the LOC type 12 territory name
of the row's `unknown_00`:

| `unknown_00` | Territory (LOC type 12)    | x          | y      | z          |
| ------------ | -------------------------- | ---------- | ------ | ---------- |
| `0`          | Balenos                    | -27,413    | 31,792 | 180,549    |
| `1`          | Serendia                   | 4,329      | 39,165 | -76,638    |
| `2`          | Calpheon                   | -274,896   | 40,374 | -54,047    |
| `3`          | Mediah                     | 228,957    | 37,767 | 5,386      |
| `4`          | Valencia                   | 762,119    | 47,710 | 163,193    |
| `5`          | The Great Ocean            | -657,330   | 32,286 | 931,828    |
| `6`          | Kamasylvia                 | -466,849   | 49,392 | -369,512   |
| `7`          | Drieghan                   | -70,966    | 55,845 | -315,808   |
| `8`          | O'dyllita                  | -236,009   | 52,212 | -558,866   |
| `9`          | Mountain of Eternal Winter | 113,077    | 61,250 | -448,362   |
| `10`         | Land of the Morning Light  | -1,297,222 | 44,018 | 1,273,371  |
| `11`         | Ulukita                    | 371,205    | 44,703 | -300,007   |
| `12`         | Outer Edania               | 601,117    | 41,781 | 590,163    |
| `13`         | Inner Edania               | 1,000,000  | 46,300 | 751,000    |

## Field Names

No reference source names the fields. The file is not in client 1784, a
private server's `DataSheets.bexcel` on client 1784 has no sheet with
`WorldMapOption` in its name, and no client Lua file of client 3482
names the table or a getter that returns one of the positions. The
fields stay `unknown_<offset>`.

## Notes

- Row `13` (Inner Edania) holds the round `x` `1,000,000` and `z`
  `751,000`; the other rows hold no round numbers.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/ui_tables.py`. With no
  named field it shows each row's 16 bytes.

## Open Questions

### What the Positions Are

The two u16 fields count up as the LOC type 12 territory keys do, and
each position falls in the territory of that key (Valencia far east,
Kamasylvia and O'dyllita in the north-west, Edania in the south-east), so
the rows read as one point per territory: a camera target, a label
position or a centre. Which one, and why the key is stored twice, needs a
getter in a newer Lua or a sheet; until then the three fields keep their
offset names.
