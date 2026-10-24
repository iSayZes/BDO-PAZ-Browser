# `siegerevivevalue.bss` Format

## Purpose

One record of Node War and Conquest War revive and liberation options:
revival times, the Conquest War liberation points per fortress, kill and
death, the liberation reward time, the outfit item for entering the
Conquest War and two short-distance revival values. The record grew over
time: clients 1485 and 1636 hold four revival values, client 1784 the
twelve `SiegeOption` columns, and later clients add one or two unnamed
fields at the end.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | -------------- | --------- |
| 5      | 3203 and later | 3483    | `siegerevivevalue.bss` | 97    | 1 String Table | 4         |
| 4      | 2736 to 3193   | 3193    | `siegerevivevalue.bss` | 93    | 1 String Table | 4         |
| 3      | 2122 to 2726   | 2726    | `siegerevivevalue.bss` | 94    | 1 String Table | 4         |
| 2      | 1737 to 2107   | 2107    | `siegerevivevalue.bss` | 92    | 1 String Table | 4         |
| 1      | 1391 to 1659   | 1659    | `siegerevivevalue.bss` | 48    | 1 String Table | 4         |

| Layout | File                   | Known         | Unknown    |
| ------ | ---------------------- | ------------- | ---------- |
| 5      | `siegerevivevalue.bss` | 92 B (94.8%)  | 5 B (5.2%) |
| 4      | `siegerevivevalue.bss` | 92 B (98.9%)  | 1 B (1.1%) |
| 3      | `siegerevivevalue.bss` | 92 B (97.9%)  | 2 B (2.1%) |
| 2      | `siegerevivevalue.bss` | 92 B (100.0%) | 0 B (0.0%) |
| 1      | `siegerevivevalue.bss` | 48 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 5             | `02782f01cf71`  |
| 3482   | Layout 5             | `02782f01cf71`  |
| 3474   | Layout 5             | `02782f01cf71`  |
| 3473   | Layout 5             | `02782f01cf71`  |
| 3464   | Layout 5             | `02782f01cf71`  |
| 3458   | Layout 5             | `02782f01cf71`  |
| 3454   | Layout 5             | `02782f01cf71`  |
| 3444   | Layout 5             | `02782f01cf71`  |
| 3435   | Layout 5             | `02782f01cf71`  |
| 3426   | Layout 5             | `02782f01cf71`  |
| 3418   | Layout 5             | `02782f01cf71`  |
| 3412   | Layout 5             | `02782f01cf71`  |
| 3402   | Layout 5             | `02782f01cf71`  |
| 3396   | Layout 5             | `02782f01cf71`  |
| 3387   | Layout 5             | `02782f01cf71`  |
| 3381   | Layout 5             | `02782f01cf71`  |
| 3373   | Layout 5             | `02782f01cf71`  |
| 3364   | Layout 5             | `02782f01cf71`  |
| 3356   | Layout 5             | `02782f01cf71`  |
| 3349   | Layout 5             | `02782f01cf71`  |
| 3342   | Layout 5             | `02782f01cf71`  |
| 3335   | Layout 5             | `02782f01cf71`  |
| 3326   | Layout 5             | `02782f01cf71`  |
| 3321   | Layout 5             | `02782f01cf71`  |
| 3314   | Layout 5             | `02782f01cf71`  |
| 3303   | Layout 5             | `02782f01cf71`  |
| 3302   | Layout 5             | `02782f01cf71`  |
| 3293   | Layout 5             | `02782f01cf71`  |
| 3283   | Layout 5             | `02782f01cf71`  |
| 3275   | Layout 5             | `02782f01cf71`  |
| 3267   | Layout 5             | `02782f01cf71`  |
| 3258   | Layout 5             | `02782f01cf71`  |
| 3251   | Layout 5             | `02782f01cf71`  |
| 3242   | Layout 5             | `02782f01cf71`  |
| 3235   | Layout 5             | `02782f01cf71`  |
| 3229   | Layout 5             | `02782f01cf71`  |
| 3212   | Layout 5             | `02782f01cf71`  |
| 3203   | Layout 5             | `02782f01cf71`  |
| 3193   | Layout 4             | `02782f01cf71`  |
| 3186   | Layout 4             | `02782f01cf71`  |
| 3177   | Layout 4             | `02782f01cf71`  |
| 3169   | Layout 4             | `02782f01cf71`  |
| 3158   | Layout 4             | `02782f01cf71`  |
| 3151   | Layout 4             | `02782f01cf71`  |
| 3144   | Layout 4             | `02782f01cf71`  |
| 3133   | Layout 4             | `02782f01cf71`  |
| 3125   | Layout 4             | `02782f01cf71`  |
| 3118   | Layout 4             | `02782f01cf71`  |
| 3111   | Layout 4             | `02782f01cf71`  |
| 3103   | Layout 4             | `02782f01cf71`  |
| 3095   | Layout 4             | `02782f01cf71`  |
| 3086   | Layout 4             | `02782f01cf71`  |
| 3072   | Layout 4             | `02782f01cf71`  |
| 3062   | Layout 4             | `02782f01cf71`  |
| 3052   | Layout 4             | `02782f01cf71`  |
| 3045   | Layout 4             | `02782f01cf71`  |
| 3037   | Layout 4             | `02782f01cf71`  |
| 3030   | Layout 4             | `02782f01cf71`  |
| 3021   | Layout 4             | `02782f01cf71`  |
| 3012   | Layout 4             | `02782f01cf71`  |
| 3002   | Layout 4             | `02782f01cf71`  |
| 2995   | Layout 4             | `02782f01cf71`  |
| 2987   | Layout 4             | `02782f01cf71`  |
| 2978   | Layout 4             | `02782f01cf71`  |
| 2970   | Layout 4             | `02782f01cf71`  |
| 2959   | Layout 4             | `02782f01cf71`  |
| 2951   | Layout 4             | `02782f01cf71`  |
| 2942   | Layout 4             | `02782f01cf71`  |
| 2935   | Layout 4             | `02782f01cf71`  |
| 2932   | Layout 4             | `02782f01cf71`  |
| 2923   | Layout 4             | `02782f01cf71`  |
| 2919   | Layout 4             | `02782f01cf71`  |
| 2907   | Layout 4             | `02782f01cf71`  |
| 2900   | Layout 4             | `02782f01cf71`  |
| 2891   | Layout 4             | `02782f01cf71`  |
| 2882   | Layout 4             | `02782f01cf71`  |
| 2872   | Layout 4             | `02782f01cf71`  |
| 2863   | Layout 4             | `02782f01cf71`  |
| 2855   | Layout 4             | `02782f01cf71`  |
| 2849   | Layout 4             | `02782f01cf71`  |
| 2844   | Layout 4             | `02782f01cf71`  |
| 2834   | Layout 4             | `02782f01cf71`  |
| 2825   | Layout 4             | `02782f01cf71`  |
| 2819   | Layout 4             | `02782f01cf71`  |
| 2811   | Layout 4             | `02782f01cf71`  |
| 2803   | Layout 4             | `02782f01cf71`  |
| 2794   | Layout 4             | `02782f01cf71`  |
| 2783   | Layout 4             | `02782f01cf71`  |
| 2774   | Layout 4             | `02782f01cf71`  |
| 2765   | Layout 4             | `02782f01cf71`  |
| 2756   | Layout 4             | `02782f01cf71`  |
| 2750   | Layout 4             | `02782f01cf71`  |
| 2743   | Layout 4             | `02782f01cf71`  |
| 2736   | Layout 4             | `02782f01cf71`  |
| 2726   | Layout 3             | `02782f01cf71`  |
| 2717   | Layout 3             | `02782f01cf71`  |
| 2709   | Layout 3             | `02782f01cf71`  |
| 2703   | Layout 3             | `02782f01cf71`  |
| 2695   | Layout 3             | `02782f01cf71`  |
| 2684   | Layout 3             | `02782f01cf71`  |
| 2672   | Layout 3             | `02782f01cf71`  |
| 2665   | Layout 3             | `02782f01cf71`  |
| 2657   | Layout 3             | `02782f01cf71`  |
| 2649   | Layout 3             | `02782f01cf71`  |
| 2644   | Layout 3             | `02782f01cf71`  |
| 2637   | Layout 3             | `02782f01cf71`  |
| 2629   | Layout 3             | `02782f01cf71`  |
| 2619   | Layout 3             | `02782f01cf71`  |
| 2612   | Layout 3             | `02782f01cf71`  |
| 2606   | Layout 3             | `02782f01cf71`  |
| 2602   | Layout 3             | `02782f01cf71`  |
| 2601   | Layout 3             | `02782f01cf71`  |
| 2592   | Layout 3             | `02782f01cf71`  |
| 2583   | Layout 3             | `02782f01cf71`  |
| 2575   | Layout 3             | `02782f01cf71`  |
| 2567   | Layout 3             | `02782f01cf71`  |
| 2560   | Layout 3             | `02782f01cf71`  |
| 2553   | Layout 3             | `02782f01cf71`  |
| 2545   | Layout 3             | `02782f01cf71`  |
| 2538   | Layout 3             | `02782f01cf71`  |
| 2529   | Layout 3             | `02782f01cf71`  |
| 2519   | Layout 3             | `02782f01cf71`  |
| 2513   | Layout 3             | `02782f01cf71`  |
| 2510   | Layout 3             | `02782f01cf71`  |
| 2507   | Layout 3             | `02782f01cf71`  |
| 2503   | Layout 3             | `02782f01cf71`  |
| 2498   | Layout 3             | `02782f01cf71`  |
| 2492   | Layout 3             | `02782f01cf71`  |
| 2487   | Layout 3             | `02782f01cf71`  |
| 2480   | Layout 3             | `02782f01cf71`  |
| 2474   | Layout 3             | `02782f01cf71`  |
| 2468   | Layout 3             | `02782f01cf71`  |
| 2460   | Layout 3             | `02782f01cf71`  |
| 2453   | Layout 3             | `02782f01cf71`  |
| 2444   | Layout 3             | `02782f01cf71`  |
| 2438   | Layout 3             | `02782f01cf71`  |
| 2434   | Layout 3             | `02782f01cf71`  |
| 2429   | Layout 3             | `02782f01cf71`  |
| 2421   | Layout 3             | `02782f01cf71`  |
| 2414   | Layout 3             | `02782f01cf71`  |
| 2407   | Layout 3             | `02782f01cf71`  |
| 2401   | Layout 3             | `02782f01cf71`  |
| 2397   | Layout 3             | `02782f01cf71`  |
| 2393   | Layout 3             | `02782f01cf71`  |
| 2384   | Layout 3             | `02782f01cf71`  |
| 2378   | Layout 3             | `02782f01cf71`  |
| 2372   | Layout 3             | `02782f01cf71`  |
| 2358   | Layout 3             | `02782f01cf71`  |
| 2352   | Layout 3             | `02782f01cf71`  |
| 2347   | Layout 3             | `02782f01cf71`  |
| 2343   | Layout 3             | `02782f01cf71`  |
| 2335   | Layout 3             | `02782f01cf71`  |
| 2327   | Layout 3             | `02782f01cf71`  |
| 2324   | Layout 3             | `02782f01cf71`  |
| 2319   | Layout 3             | `02782f01cf71`  |
| 2313   | Layout 3             | `02782f01cf71`  |
| 2308   | Layout 3             | `02782f01cf71`  |
| 2302   | Layout 3             | `02782f01cf71`  |
| 2295   | Layout 3             | `02782f01cf71`  |
| 2290   | Layout 3             | `02782f01cf71`  |
| 2284   | Layout 3             | `02782f01cf71`  |
| 2276   | Layout 3             | `02782f01cf71`  |
| 2269   | Layout 3             | `02782f01cf71`  |
| 2259   | Layout 3             | `02782f01cf71`  |
| 2250   | Layout 3             | `02782f01cf71`  |
| 2243   | Layout 3             | `02782f01cf71`  |
| 2235   | Layout 3             | `02782f01cf71`  |
| 2229   | Layout 3             | `02782f01cf71`  |
| 2224   | Layout 3             | `02782f01cf71`  |
| 2218   | Layout 3             | `02782f01cf71`  |
| 2215   | Layout 3             | `02782f01cf71`  |
| 2207   | Layout 3             | `02782f01cf71`  |
| 2203   | Layout 3             | `02782f01cf71`  |
| 2196   | Layout 3             | `02782f01cf71`  |
| 2192   | Layout 3             | `02782f01cf71`  |
| 2189   | Layout 3             | `02782f01cf71`  |
| 2183   | Layout 3             | `02782f01cf71`  |
| 2179   | Layout 3             | `02782f01cf71`  |
| 2171   | Layout 3             | `02782f01cf71`  |
| 2163   | Layout 3             | `02782f01cf71`  |
| 2156   | Layout 3             | `02782f01cf71`  |
| 2151   | Layout 3             | `02782f01cf71`  |
| 2147   | Layout 3             | `02782f01cf71`  |
| 2142   | Layout 3             | `02782f01cf71`  |
| 2138   | Layout 3             | `02782f01cf71`  |
| 2134   | Layout 3             | `02782f01cf71`  |
| 2130   | Layout 3             | `02782f01cf71`  |
| 2122   | Layout 3             | `02782f01cf71`  |
| 2107   | Layout 2             | `02782f01cf71`  |
| 2098   | Layout 2             | `02782f01cf71`  |
| 2089   | Layout 2             | `02782f01cf71`  |
| 2081   | Layout 2             | `02782f01cf71`  |
| 2073   | Layout 2             | `02782f01cf71`  |
| 2067   | Layout 2             | `02782f01cf71`  |
| 2063   | Layout 2             | `02782f01cf71`  |
| 2059   | Layout 2             | `02782f01cf71`  |
| 2052   | Layout 2             | `02782f01cf71`  |
| 2044   | Layout 2             | `02782f01cf71`  |
| 2039   | Layout 2             | `02782f01cf71`  |
| 2032   | Layout 2             | `02782f01cf71`  |
| 2025   | Layout 2             | `02782f01cf71`  |
| 2011   | Layout 2             | `02782f01cf71`  |
| 2005   | Layout 2             | `02782f01cf71`  |
| 2000   | Layout 2             | `02782f01cf71`  |
| 1996   | Layout 2             | `02782f01cf71`  |
| 1991   | Layout 2             | `02782f01cf71`  |
| 1985   | Layout 2             | `02782f01cf71`  |
| 1980   | Layout 2             | `02782f01cf71`  |
| 1969   | Layout 2             | `02782f01cf71`  |
| 1964   | Layout 2             | `02782f01cf71`  |
| 1958   | Layout 2             | `02782f01cf71`  |
| 1950   | Layout 2             | `02782f01cf71`  |
| 1945   | Layout 2             | `02782f01cf71`  |
| 1937   | Layout 2             | `02782f01cf71`  |
| 1933   | Layout 2             | `02782f01cf71`  |
| 1927   | Layout 2             | `02782f01cf71`  |
| 1921   | Layout 2             | `02782f01cf71`  |
| 1914   | Layout 2             | `02782f01cf71`  |
| 1908   | Layout 2             | `02782f01cf71`  |
| 1897   | Layout 2             | `02782f01cf71`  |
| 1892   | Layout 2             | `02782f01cf71`  |
| 1886   | Layout 2             | `02782f01cf71`  |
| 1881   | Layout 2             | `02782f01cf71`  |
| 1871   | Layout 2             | `02782f01cf71`  |
| 1866   | Layout 2             | `02782f01cf71`  |
| 1862   | Layout 2             | `02782f01cf71`  |
| 1854   | Layout 2             | `02782f01cf71`  |
| 1846   | Layout 2             | `02782f01cf71`  |
| 1838   | Layout 2             | `02782f01cf71`  |
| 1832   | Layout 2             | `02782f01cf71`  |
| 1826   | Layout 2             | `02782f01cf71`  |
| 1822   | Layout 2             | `02782f01cf71`  |
| 1818   | Layout 2             | `02782f01cf71`  |
| 1804   | Layout 2             | `02782f01cf71`  |
| 1794   | Layout 2             | `02782f01cf71`  |
| 1790   | Layout 2             | `02782f01cf71`  |
| 1784   | Layout 2             | `02782f01cf71`  |
| 1774   | Layout 2             | `02782f01cf71`  |
| 1771   | Layout 2             | `02782f01cf71`  |
| 1762   | Layout 2             | `02782f01cf71`  |
| 1759   | Layout 2             | `02782f01cf71`  |
| 1754   | Layout 2             | `02782f01cf71`  |
| 1749   | Layout 2             | `02782f01cf71`  |
| 1743   | Layout 2             | `02782f01cf71`  |
| 1737   | Layout 2             | `02782f01cf71`  |
| 1731   | No documented layout | `02782f01cf71`  |
| 1725   | No documented layout | `02782f01cf71`  |
| 1717   | No documented layout | `02782f01cf71`  |
| 1710   | No documented layout | `02782f01cf71`  |
| 1704   | No documented layout | `02782f01cf71`  |
| 1698   | No documented layout | `02782f01cf71`  |
| 1690   | No documented layout | `02782f01cf71`  |
| 1685   | No documented layout | `02782f01cf71`  |
| 1680   | No documented layout | `02782f01cf71`  |
| 1674   | No documented layout | `02782f01cf71`  |
| 1668   | No documented layout | `02782f01cf71`  |
| 1659   | Layout 1             | `02782f01cf71`  |
| 1649   | Layout 1             | `02782f01cf71`  |
| 1642   | Layout 1             | `02782f01cf71`  |
| 1636   | Layout 1             | `02782f01cf71`  |
| 1628   | Layout 1             | `02782f01cf71`  |
| 1622   | Layout 1             | `02782f01cf71`  |
| 1614   | Layout 1             | `02782f01cf71`  |
| 1608   | Layout 1             | `02782f01cf71`  |
| 1602   | Layout 1             | `02782f01cf71`  |
| 1598   | Layout 1             | `02782f01cf71`  |
| 1594   | Layout 1             | `02782f01cf71`  |
| 1590   | Layout 1             | `02782f01cf71`  |
| 1587   | Layout 1             | `02782f01cf71`  |
| 1584   | Layout 1             | `02782f01cf71`  |
| 1579   | Layout 1             | `02782f01cf71`  |
| 1572   | Layout 1             | `02782f01cf71`  |
| 1565   | Layout 1             | `02782f01cf71`  |
| 1559   | Layout 1             | `02782f01cf71`  |
| 1554   | Layout 1             | `02782f01cf71`  |
| 1547   | Layout 1             | `02782f01cf71`  |
| 1537   | Layout 1             | `02782f01cf71`  |
| 1529   | Layout 1             | `02782f01cf71`  |
| 1524   | Layout 1             | `02782f01cf71`  |
| 1519   | Layout 1             | `02782f01cf71`  |
| 1509   | Layout 1             | `02782f01cf71`  |
| 1506   | Layout 1             | `02782f01cf71`  |
| 1504   | Layout 1             | `02782f01cf71`  |
| 1500   | Layout 1             | `02782f01cf71`  |
| 1493   | Layout 1             | `02782f01cf71`  |
| 1489   | Layout 1             | `02782f01cf71`  |
| 1485   | Layout 1             | `02782f01cf71`  |
| 1481   | Layout 1             | `02782f01cf71`  |
| 1474   | Layout 1             | `02782f01cf71`  |
| 1466   | Layout 1             | `02782f01cf71`  |
| 1462   | Layout 1             | `02782f01cf71`  |
| 1459   | Layout 1             | `02782f01cf71`  |
| 1453   | Layout 1             | `02782f01cf71`  |
| 1450   | Layout 1             | `02782f01cf71`  |
| 1445   | Layout 1             | `02782f01cf71`  |
| 1439   | Layout 1             | `02782f01cf71`  |
| 1433   | Layout 1             | `02782f01cf71`  |
| 1430   | Layout 1             | `02782f01cf71`  |
| 1426   | Layout 1             | `02782f01cf71`  |
| 1421   | Layout 1             | `02782f01cf71`  |
| 1417   | Layout 1             | `02782f01cf71`  |
| 1416   | Layout 1             | `02782f01cf71`  |
| 1409   | Layout 1             | `02782f01cf71`  |
| 1405   | Layout 1             | `02782f01cf71`  |
| 1401   | Layout 1             | `02782f01cf71`  |
| 1396   | Layout 1             | `02782f01cf71`  |
| 1391   | Layout 1             | `02782f01cf71`  |
| 1390   | No file              | `02782f01cf71`  |
| 1386   | No file              | `02782f01cf71`  |
| 1381   | No file              | `02782f01cf71`  |
| 1379   | No file              | `02782f01cf71`  |
| 1372   | No file              | `02782f01cf71`  |
| 1366   | No file              | `02782f01cf71`  |
| 1364   | No file              | `02782f01cf71`  |
| 1363   | No file              | `02782f01cf71`  |
| 1360   | No file              | `02782f01cf71`  |
| 1358   | No file              | `02782f01cf71`  |
| 1355   | No file              | `02782f01cf71`  |
| 1351   | No file              | `02782f01cf71`  |
| 1348   | No file              | `02782f01cf71`  |
| 1346   | No file              | `02782f01cf71`  |
| 1341   | No file              | `02782f01cf71`  |
| 1340   | No file              | `02782f01cf71`  |
| 1338   | No file              | `02782f01cf71`  |
| 1335   | No file              | `02782f01cf71`  |
| 1333   | No file              | `02782f01cf71`  |
| 1329   | No file              | `02782f01cf71`  |
| 1327   | No file              | `02782f01cf71`  |
| 1324   | No file              | `02782f01cf71`  |
| 1321   | No file              | `02782f01cf71`  |
| 1319   | No file              | `02782f01cf71`  |
| 1318   | No file              | `02782f01cf71`  |
| 1316   | No file              | `02782f01cf71`  |
| 1313   | No file              | `02782f01cf71`  |
| 1311   | No file              | `02782f01cf71`  |
| 1309   | No file              | `02782f01cf71`  |
| 1304   | No file              | `02782f01cf71`  |
| 1292   | No file              | `02782f01cf71`  |
| 1286   | No file              | `02782f01cf71`  |
| 1280   | No file              | `02782f01cf71`  |
| 1276   | No file              | `02782f01cf71`  |
| 1267   | No file              | `02782f01cf71`  |
| 1261   | No file              | `02782f01cf71`  |
| 1256   | No file              | `02782f01cf71`  |
| 1250   | No file              | `02782f01cf71`  |
| 1246   | No file              | `02782f01cf71`  |
| 1239   | No file              | `02782f01cf71`  |
| 1230   | No file              | `02782f01cf71`  |
| 1226   | No file              | `02782f01cf71`  |
| 1220   | No file              | `02782f01cf71`  |
| 1217   | No file              | `02782f01cf71`  |
| 1211   | No file              | `02782f01cf71`  |
| 1210   | No file              | `02782f01cf71`  |
| 1208   | No file              | `02782f01cf71`  |
| 1203   | No file              | `02782f01cf71`  |
| 1197   | No file              | `02782f01cf71`  |
| 1194   | No file              | `02782f01cf71`  |
| 1192   | No file              | `02782f01cf71`  |
| 1187   | No file              | `02782f01cf71`  |
| 1183   | No file              | `02782f01cf71`  |
| 1177   | No file              | `02782f01cf71`  |
| 1173   | No file              | `02782f01cf71`  |
| 1167   | No file              | `02782f01cf71`  |
| 1164   | No file              | `02782f01cf71`  |
| 1156   | No file              | `02782f01cf71`  |
| 1149   | No file              | `02782f01cf71`  |
| 1144   | No file              | `02782f01cf71`  |
| 1137   | No file              | `02782f01cf71`  |
| 1132   | No file              | `02782f01cf71`  |
| 1127   | No file              | `02782f01cf71`  |
| 1122   | No file              | `02782f01cf71`  |
| 1118   | No file              | `02782f01cf71`  |
| 1114   | No file              | `02782f01cf71`  |
| 1109   | No file              | `02782f01cf71`  |
| 1102   | No file              | `02782f01cf71`  |
| 1096   | No file              | `02782f01cf71`  |
| 1088   | No file              | `02782f01cf71`  |
| 1081   | No file              | `02782f01cf71`  |
| 1076   | No file              | `02782f01cf71`  |
| 1069   | No file              | `02782f01cf71`  |
| 1064   | No file              | `02782f01cf71`  |
| 1058   | No file              | `02782f01cf71`  |
| 1051   | No file              | `02782f01cf71`  |
| 1044   | No file              | `02782f01cf71`  |
| 1036   | No file              | `02782f01cf71`  |
| 1026   | No file              | `02782f01cf71`  |
| 1016   | No file              | `02782f01cf71`  |
| 1009   | No file              | `02782f01cf71`  |
| 1005   | No file              | `02782f01cf71`  |
| 1000   | No file              | `02782f01cf71`  |
| 998    | No file              | `02782f01cf71`  |
| 990    | No file              | `02782f01cf71`  |
| 979    | No file              | `02782f01cf71`  |
| 972    | No file              | `02782f01cf71`  |
| 963    | No file              | `02782f01cf71`  |
| 955    | No file              | `02782f01cf71`  |
| 946    | No file              | `02782f01cf71`  |
| 938    | No file              | `02782f01cf71`  |
| 927    | No file              | `02782f01cf71`  |
| 911    | No file              | `02782f01cf71`  |
| 904    | No file              | `02782f01cf71`  |
| 899    | No file              | `02782f01cf71`  |
| 894    | No file              | `02782f01cf71`  |
| 885    | No file              | `02782f01cf71`  |
| 879    | No file              | `02782f01cf71`  |
| 872    | No file              | `02782f01cf71`  |
| 864    | No file              | `02782f01cf71`  |
| 855    | No file              | `02782f01cf71`  |
| 853    | No file              | `02782f01cf71`  |
| 845    | No file              | `02782f01cf71`  |
| 837    | No file              | `02782f01cf71`  |
| 829    | No file              | `02782f01cf71`  |
| 822    | No file              | `02782f01cf71`  |
| 814    | No file              | `02782f01cf71`  |
| 805    | No file              | `02782f01cf71`  |
| 794    | No file              | `02782f01cf71`  |
| 787    | No file              | `02782f01cf71`  |
| 780    | No file              | `02782f01cf71`  |
| 771    | No file              | `02782f01cf71`  |
| 760    | No file              | `02782f01cf71`  |
| 748    | No file              | `02782f01cf71`  |
| 741    | No file              | `02782f01cf71`  |
| 736    | No file              | `02782f01cf71`  |
| 731    | No file              | `02782f01cf71`  |
| 723    | No file              | `02782f01cf71`  |
| 711    | No file              | `02782f01cf71`  |
| 707    | No file              | `02782f01cf71`  |
| 697    | No file              | `02782f01cf71`  |
| 689    | No file              | `02782f01cf71`  |
| 683    | No file              | `02782f01cf71`  |
| 678    | No file              | `02782f01cf71`  |
| 670    | No file              | `02782f01cf71`  |
| 661    | No file              | `02782f01cf71`  |
| 656    | No file              | `02782f01cf71`  |
| 652    | No file              | `02782f01cf71`  |
| 643    | No file              | `02782f01cf71`  |
| 637    | No file              | `02782f01cf71`  |
| 630    | No file              | `02782f01cf71`  |
| 627    | No file              | `02782f01cf71`  |
| 621    | No file              | `02782f01cf71`  |
| 617    | No file              | `02782f01cf71`  |
| 615    | No file              | `02782f01cf71`  |
| 606    | No file              | `02782f01cf71`  |
| 599    | No file              | `02782f01cf71`  |
| 592    | No file              | `02782f01cf71`  |
| 586    | No file              | `02782f01cf71`  |
| 577    | No file              | `02782f01cf71`  |
| 569    | No file              | `02782f01cf71`  |
| 561    | No file              | `02782f01cf71`  |
| 554    | No file              | `02782f01cf71`  |
| 542    | No file              | `02782f01cf71`  |
| 532    | No file              | `02782f01cf71`  |
| 531    | No file              | `02782f01cf71`  |
| 526    | No file              | `02782f01cf71`  |
| 521    | No file              | `02782f01cf71`  |
| 517    | No file              | `02782f01cf71`  |
| 510    | No file              | `02782f01cf71`  |
| 508    | No file              | `02782f01cf71`  |
| 504    | No file              | `02782f01cf71`  |
| 497    | No file              | `02782f01cf71`  |
| 491    | No file              | `02782f01cf71`  |
| 485    | No file              | `02782f01cf71`  |
| 478    | No file              | `02782f01cf71`  |
| 472    | No file              | `02782f01cf71`  |
| 466    | No file              | `02782f01cf71`  |
| 457    | No file              | `02782f01cf71`  |
| 452    | No file              | `02782f01cf71`  |
| 449    | No file              | `02782f01cf71`  |
| 435    | No file              | `02782f01cf71`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                      |
| --------------------- | -------- | ----------------------------------------- |
| `languagedata_en.loc` | Optional | Item name of the entry outfit, LOC type 0 |

All multi-byte values are little-endian.

## Layout 5

### File Layout

| Offset              | Type         | Field                                 | Notes                                                       |
| ------------------- | ------------ | ------------------------------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]      | magic                                 | ASCII `PABR`                                                |
| `+0x04`             | u64          | siege_revival_time                    | `1000` on clients 1784 and 3482                             |
| `+0x0C`             | u64          | siege_death_revival_time              | `1000` on clients 1784 and 3482                             |
| `+0x14`             | u64          | siege_recovery_revival_time           | `6000` on clients 1784 and 3482                             |
| `+0x1C`             | u64          | major_siege_recovery_revival_time     | `3000` on client 1784, `6000` on client 3482                |
| `+0x24`             | u64          | siege_resource_revival_time           | `5` on clients 1784 and 3482                                |
| `+0x2C`             | u32          | major_siege_liberation_fortress_point | `50` on clients 1784 and 3482                               |
| `+0x30`             | u32          | major_siege_liberation_kill_point     | `1` on client 1784, `3` on client 3482                      |
| `+0x34`             | u32          | major_siege_liberation_death_point    | `1` on clients 1784 and 3482                                |
| `+0x38`             | u64          | major_siege_liberation_reward_time    | `3600` on clients 1784 and 3482                             |
| `+0x40`             | u32          | major_siege_enter_clothes_item_key    | Item key; `607028` (Sun's Resolve) on clients 1784 and 3482 |
| `+0x44`             | f32          | siege_fortress_short_distance_revival | `6500` on clients 1784 and 3482                             |
| `+0x48`             | u64          | siege_short_distance_revival_avoid    | `12000` on client 1784, `9000` on client 3482               |
| `+0x50`             | u8           | unknown_50                            | `1` on clients 2313 to 3482                                 |
| `+0x51`             | u32          | unknown_51                            | `15` on client 3482                                         |
| `+0x55`             | String Table | string_table                          | See String Table                                            |
| `string_table+0x00` | u32          | table_start                           | Offset of the string table; `0x55`                          |
| `string_table+0x04` | u32          | zero                                  | Always `0`                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 4

No `unknown_51`.

### File Layout

| Offset              | Type         | Field                                 | Notes                              |
| ------------------- | ------------ | ------------------------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                                 | ASCII `PABR`                       |
| `+0x04`             | u64          | siege_revival_time                    |                                    |
| `+0x0C`             | u64          | siege_death_revival_time              |                                    |
| `+0x14`             | u64          | siege_recovery_revival_time           |                                    |
| `+0x1C`             | u64          | major_siege_recovery_revival_time     |                                    |
| `+0x24`             | u64          | siege_resource_revival_time           |                                    |
| `+0x2C`             | u32          | major_siege_liberation_fortress_point |                                    |
| `+0x30`             | u32          | major_siege_liberation_kill_point     |                                    |
| `+0x34`             | u32          | major_siege_liberation_death_point    |                                    |
| `+0x38`             | u64          | major_siege_liberation_reward_time    |                                    |
| `+0x40`             | u32          | major_siege_enter_clothes_item_key    |                                    |
| `+0x44`             | f32          | siege_fortress_short_distance_revival |                                    |
| `+0x48`             | u64          | siege_short_distance_revival_avoid    |                                    |
| `+0x50`             | u8           | unknown_50                            |                                    |
| `+0x51`             | String Table | string_table                          | See String Table                   |
| `string_table+0x00` | u32          | table_start                           | Offset of the string table; `0x51` |
| `string_table+0x04` | u32          | zero                                  | Always `0`                         |

## Layout 3

`unknown_51` is a u8 (`2` on client 2313, `6` on client 2519).

### File Layout

| Offset              | Type         | Field                                 | Notes                              |
| ------------------- | ------------ | ------------------------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                                 | ASCII `PABR`                       |
| `+0x04`             | u64          | siege_revival_time                    |                                    |
| `+0x0C`             | u64          | siege_death_revival_time              |                                    |
| `+0x14`             | u64          | siege_recovery_revival_time           |                                    |
| `+0x1C`             | u64          | major_siege_recovery_revival_time     |                                    |
| `+0x24`             | u64          | siege_resource_revival_time           |                                    |
| `+0x2C`             | u32          | major_siege_liberation_fortress_point |                                    |
| `+0x30`             | u32          | major_siege_liberation_kill_point     |                                    |
| `+0x34`             | u32          | major_siege_liberation_death_point    |                                    |
| `+0x38`             | u64          | major_siege_liberation_reward_time    |                                    |
| `+0x40`             | u32          | major_siege_enter_clothes_item_key    |                                    |
| `+0x44`             | f32          | siege_fortress_short_distance_revival |                                    |
| `+0x48`             | u64          | siege_short_distance_revival_avoid    |                                    |
| `+0x50`             | u8           | unknown_50                            |                                    |
| `+0x51`             | u8           | unknown_51                            |                                    |
| `+0x52`             | String Table | string_table                          | See String Table                   |
| `string_table+0x00` | u32          | table_start                           | Offset of the string table; `0x52` |
| `string_table+0x04` | u32          | zero                                  | Always `0`                         |

## Layout 2

The twelve `SiegeOption` fields only.

### File Layout

| Offset              | Type         | Field                                 | Notes                              |
| ------------------- | ------------ | ------------------------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                                 | ASCII `PABR`                       |
| `+0x04`             | u64          | siege_revival_time                    |                                    |
| `+0x0C`             | u64          | siege_death_revival_time              |                                    |
| `+0x14`             | u64          | siege_recovery_revival_time           |                                    |
| `+0x1C`             | u64          | major_siege_recovery_revival_time     |                                    |
| `+0x24`             | u64          | siege_resource_revival_time           |                                    |
| `+0x2C`             | u32          | major_siege_liberation_fortress_point |                                    |
| `+0x30`             | u32          | major_siege_liberation_kill_point     |                                    |
| `+0x34`             | u32          | major_siege_liberation_death_point    |                                    |
| `+0x38`             | u64          | major_siege_liberation_reward_time    |                                    |
| `+0x40`             | u32          | major_siege_enter_clothes_item_key    |                                    |
| `+0x44`             | f32          | siege_fortress_short_distance_revival |                                    |
| `+0x48`             | u64          | siege_short_distance_revival_avoid    |                                    |
| `+0x50`             | String Table | string_table                          | See String Table                   |
| `string_table+0x00` | u32          | table_start                           | Offset of the string table; `0x50` |
| `string_table+0x04` | u32          | zero                                  | Always `0`                         |

## Layout 1

Four revival values, before the Conquest War fields.

### File Layout

| Offset              | Type         | Field                       | Notes                              |
| ------------------- | ------------ | --------------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                       | ASCII `PABR`                       |
| `+0x04`             | u64          | siege_revival_time          | `1000` on clients 1485 and 1636    |
| `+0x0C`             | u64          | siege_death_revival_time    | `1000`                             |
| `+0x14`             | u64          | siege_recovery_revival_time | `6000`                             |
| `+0x1C`             | u64          | siege_resource_revival_time | `5`                                |
| `+0x24`             | String Table | string_table                | See String Table                   |
| `string_table+0x00` | u32          | table_start                 | Offset of the string table; `0x24` |
| `string_table+0x04` | u32          | zero                        | Always `0`                         |

## Field Names

The `SiegeOption` sheet of a private server's `DataSheets.bexcel` on
client 1784 has 24 columns and one row. Twelve of them are the twelve
fields of the client 1784 file, in sheet order and with the sheet's
values (12 of 12): `SiegeRevivalTime`, `SiegeDeathRevivalTime`,
`SiegeRecoveryRevivalTime`, `MajorSiegeRecoveryRevivalTime`,
`SiegeResourceRevivalTime`, `MajorSiegeLiberationFortressPoint`,
`MajorSiegeLiberationKillPoint`, `MajorSiegeLiberationDeathPoint`,
`MajorSiegeLiberationRewardTime`, `MajorSiegeEnterClothesItemKey`,
`SiegeFortressShortDistanceRevival` and `SiegeShortDistanceRevivalAvoid`.
The other twelve (`SiegeStartDistanceTeleport`, the
`majorSiegeAttackGuildReward*` columns, `SiegeMaxResource`,
`SiegeKeepCount1` to `5` and `CastellanImpossibleMinorSiege`) are not in
this file.

That server's dump (client 1784) has check messages for the struct
members `SiegeOptionStaticStatus _respawnTimePerMinute`,
`_respawnTimePerDeathCount`, `_respawnTimePerHealingTower`,
`_respawnTimePerHealingTowerMajor`, `_respawnResourcePerCost`,
`_castellanImpossibleTerritoryList`, `_majorSiegeLiberationFortressPoint`
and `_majorSiegeLiberationKillPoint`, stored in the reverse of the sheet's
column order from `SiegeRevivalTime` to `MajorSiegeLiberationKillPoint`.
That order pairs `SiegeRevivalTime` with `_respawnTimePerMinute` through
`SiegeResourceRevivalTime` with `_respawnResourcePerCost`. The field names
follow the sheet columns.

Layout 1 holds the values `1000, 1000, 6000, 5`: the client 1784 record
without `MajorSiegeRecoveryRevivalTime` (`3000`), so its four fields take
the names of the other four. `unknown_50` and `unknown_51` are newer than
client 1784 and have no source; `unknown_51` is a u8 on clients 2313 to
2637, missing on clients 2765 and 3002 and a u32 from client 3251.

## Notes

- `major_siege_enter_clothes_item_key` `607028` is Sun's Resolve
  (LOC type 0).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  one row with every named field and the outfit item with its icon and
  name. It reads Layout 5 only.

## Open Questions

### Units of the Revival Times

By the dump's member order, `siege_revival_time` and
`siege_death_revival_time` are `_respawnTimePerMinute` and
`_respawnTimePerDeathCount`: revive time added per minute of war and per
death. Neither the unit of their `1000` nor how the client combines them
is confirmed. `siege_resource_revival_time` (`_respawnResourcePerCost`,
`5`) reads as a resource cost, not a time.

### The Fields After the Short-Distance Revival

`unknown_50` is `1` from client 2313 on. `unknown_51` is a u8 (`2`, then
`6`) on clients 2313 to 2637, gone on clients 2765 and 3002, and a u32
`15` from client 3251; whether these are one field is open.
