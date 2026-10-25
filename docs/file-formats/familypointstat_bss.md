# `familypointstat.bss` Format

## Purpose

Family point stat steps. A PABR list of steps; each row has an index, a
point value and the stats the step gives: AP, DP, max HP, MP, stamina,
weight, inventory, accuracy and evasion. On client 3482 it holds ten steps,
index `10` down to `1`, and every stat of step N is N or 100 times N.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------- | ----- | ------- | --------- |
| 1      | 1109 and later | `familypointstat.bss` | 450   | 10 Row  | 43        |

| Layout | File                  | Known         | Unknown     |
| ------ | --------------------- | ------------- | ----------- |
| 1      | `familypointstat.bss` | 410 B (91.1%) | 40 B (8.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `9f7afde34166`  |
| 3482   | Layout 1 | `9f7afde34166`  |
| 3474   | Layout 1 | `9f7afde34166`  |
| 3473   | Layout 1 | `9f7afde34166`  |
| 3464   | Layout 1 | `9f7afde34166`  |
| 3458   | Layout 1 | `9f7afde34166`  |
| 3454   | Layout 1 | `9f7afde34166`  |
| 3444   | Layout 1 | `9f7afde34166`  |
| 3435   | Layout 1 | `9f7afde34166`  |
| 3426   | Layout 1 | `9f7afde34166`  |
| 3418   | Layout 1 | `9f7afde34166`  |
| 3412   | Layout 1 | `9f7afde34166`  |
| 3402   | Layout 1 | `9f7afde34166`  |
| 3396   | Layout 1 | `9f7afde34166`  |
| 3387   | Layout 1 | `9f7afde34166`  |
| 3381   | Layout 1 | `9f7afde34166`  |
| 3373   | Layout 1 | `9f7afde34166`  |
| 3364   | Layout 1 | `9f7afde34166`  |
| 3356   | Layout 1 | `9f7afde34166`  |
| 3349   | Layout 1 | `9f7afde34166`  |
| 3342   | Layout 1 | `9f7afde34166`  |
| 3335   | Layout 1 | `9f7afde34166`  |
| 3326   | Layout 1 | `9f7afde34166`  |
| 3321   | Layout 1 | `9f7afde34166`  |
| 3314   | Layout 1 | `9f7afde34166`  |
| 3303   | Layout 1 | `9f7afde34166`  |
| 3302   | Layout 1 | `9f7afde34166`  |
| 3293   | Layout 1 | `9f7afde34166`  |
| 3283   | Layout 1 | `9f7afde34166`  |
| 3275   | Layout 1 | `9f7afde34166`  |
| 3267   | Layout 1 | `9f7afde34166`  |
| 3258   | Layout 1 | `9f7afde34166`  |
| 3251   | Layout 1 | `9f7afde34166`  |
| 3242   | Layout 1 | `9f7afde34166`  |
| 3235   | Layout 1 | `9f7afde34166`  |
| 3229   | Layout 1 | `9f7afde34166`  |
| 3212   | Layout 1 | `9f7afde34166`  |
| 3203   | Layout 1 | `9f7afde34166`  |
| 3193   | Layout 1 | `9f7afde34166`  |
| 3186   | Layout 1 | `9f7afde34166`  |
| 3177   | Layout 1 | `9f7afde34166`  |
| 3169   | Layout 1 | `9f7afde34166`  |
| 3158   | Layout 1 | `9f7afde34166`  |
| 3151   | Layout 1 | `9f7afde34166`  |
| 3144   | Layout 1 | `9f7afde34166`  |
| 3133   | Layout 1 | `9f7afde34166`  |
| 3125   | Layout 1 | `9f7afde34166`  |
| 3118   | Layout 1 | `9f7afde34166`  |
| 3111   | Layout 1 | `9f7afde34166`  |
| 3103   | Layout 1 | `9f7afde34166`  |
| 3095   | Layout 1 | `9f7afde34166`  |
| 3086   | Layout 1 | `9f7afde34166`  |
| 3072   | Layout 1 | `9f7afde34166`  |
| 3062   | Layout 1 | `9f7afde34166`  |
| 3052   | Layout 1 | `9f7afde34166`  |
| 3045   | Layout 1 | `9f7afde34166`  |
| 3037   | Layout 1 | `9f7afde34166`  |
| 3030   | Layout 1 | `9f7afde34166`  |
| 3021   | Layout 1 | `9f7afde34166`  |
| 3012   | Layout 1 | `9f7afde34166`  |
| 3002   | Layout 1 | `9f7afde34166`  |
| 2995   | Layout 1 | `9f7afde34166`  |
| 2987   | Layout 1 | `9f7afde34166`  |
| 2978   | Layout 1 | `9f7afde34166`  |
| 2970   | Layout 1 | `9f7afde34166`  |
| 2959   | Layout 1 | `9f7afde34166`  |
| 2951   | Layout 1 | `9f7afde34166`  |
| 2942   | Layout 1 | `9f7afde34166`  |
| 2935   | Layout 1 | `9f7afde34166`  |
| 2932   | Layout 1 | `9f7afde34166`  |
| 2923   | Layout 1 | `9f7afde34166`  |
| 2919   | Layout 1 | `9f7afde34166`  |
| 2907   | Layout 1 | `9f7afde34166`  |
| 2900   | Layout 1 | `9f7afde34166`  |
| 2891   | Layout 1 | `9f7afde34166`  |
| 2882   | Layout 1 | `9f7afde34166`  |
| 2872   | Layout 1 | `9f7afde34166`  |
| 2863   | Layout 1 | `9f7afde34166`  |
| 2855   | Layout 1 | `9f7afde34166`  |
| 2849   | Layout 1 | `9f7afde34166`  |
| 2844   | Layout 1 | `9f7afde34166`  |
| 2834   | Layout 1 | `9f7afde34166`  |
| 2825   | Layout 1 | `9f7afde34166`  |
| 2819   | Layout 1 | `9f7afde34166`  |
| 2811   | Layout 1 | `9f7afde34166`  |
| 2803   | Layout 1 | `9f7afde34166`  |
| 2794   | Layout 1 | `9f7afde34166`  |
| 2783   | Layout 1 | `9f7afde34166`  |
| 2774   | Layout 1 | `9f7afde34166`  |
| 2765   | Layout 1 | `9f7afde34166`  |
| 2756   | Layout 1 | `9f7afde34166`  |
| 2750   | Layout 1 | `9f7afde34166`  |
| 2743   | Layout 1 | `9f7afde34166`  |
| 2736   | Layout 1 | `9f7afde34166`  |
| 2726   | Layout 1 | `9f7afde34166`  |
| 2717   | Layout 1 | `9f7afde34166`  |
| 2709   | Layout 1 | `9f7afde34166`  |
| 2703   | Layout 1 | `9f7afde34166`  |
| 2695   | Layout 1 | `9f7afde34166`  |
| 2684   | Layout 1 | `9f7afde34166`  |
| 2672   | Layout 1 | `9f7afde34166`  |
| 2665   | Layout 1 | `9f7afde34166`  |
| 2657   | Layout 1 | `9f7afde34166`  |
| 2649   | Layout 1 | `9f7afde34166`  |
| 2644   | Layout 1 | `9f7afde34166`  |
| 2637   | Layout 1 | `9f7afde34166`  |
| 2629   | Layout 1 | `9f7afde34166`  |
| 2619   | Layout 1 | `9f7afde34166`  |
| 2612   | Layout 1 | `9f7afde34166`  |
| 2606   | Layout 1 | `9f7afde34166`  |
| 2602   | Layout 1 | `9f7afde34166`  |
| 2601   | Layout 1 | `9f7afde34166`  |
| 2592   | Layout 1 | `9f7afde34166`  |
| 2583   | Layout 1 | `9f7afde34166`  |
| 2575   | Layout 1 | `9f7afde34166`  |
| 2567   | Layout 1 | `9f7afde34166`  |
| 2560   | Layout 1 | `9f7afde34166`  |
| 2553   | Layout 1 | `9f7afde34166`  |
| 2545   | Layout 1 | `9f7afde34166`  |
| 2538   | Layout 1 | `9f7afde34166`  |
| 2529   | Layout 1 | `9f7afde34166`  |
| 2519   | Layout 1 | `9f7afde34166`  |
| 2513   | Layout 1 | `9f7afde34166`  |
| 2510   | Layout 1 | `9f7afde34166`  |
| 2507   | Layout 1 | `9f7afde34166`  |
| 2503   | Layout 1 | `9f7afde34166`  |
| 2498   | Layout 1 | `9f7afde34166`  |
| 2492   | Layout 1 | `9f7afde34166`  |
| 2487   | Layout 1 | `9f7afde34166`  |
| 2480   | Layout 1 | `9f7afde34166`  |
| 2474   | Layout 1 | `9f7afde34166`  |
| 2468   | Layout 1 | `9f7afde34166`  |
| 2460   | Layout 1 | `9f7afde34166`  |
| 2453   | Layout 1 | `9f7afde34166`  |
| 2444   | Layout 1 | `9f7afde34166`  |
| 2438   | Layout 1 | `9f7afde34166`  |
| 2434   | Layout 1 | `9f7afde34166`  |
| 2429   | Layout 1 | `9f7afde34166`  |
| 2421   | Layout 1 | `9f7afde34166`  |
| 2414   | Layout 1 | `9f7afde34166`  |
| 2407   | Layout 1 | `9f7afde34166`  |
| 2401   | Layout 1 | `9f7afde34166`  |
| 2397   | Layout 1 | `9f7afde34166`  |
| 2393   | Layout 1 | `9f7afde34166`  |
| 2384   | Layout 1 | `9f7afde34166`  |
| 2378   | Layout 1 | `9f7afde34166`  |
| 2372   | Layout 1 | `9f7afde34166`  |
| 2358   | Layout 1 | `9f7afde34166`  |
| 2352   | Layout 1 | `9f7afde34166`  |
| 2347   | Layout 1 | `9f7afde34166`  |
| 2343   | Layout 1 | `9f7afde34166`  |
| 2335   | Layout 1 | `9f7afde34166`  |
| 2327   | Layout 1 | `9f7afde34166`  |
| 2324   | Layout 1 | `9f7afde34166`  |
| 2319   | Layout 1 | `9f7afde34166`  |
| 2313   | Layout 1 | `9f7afde34166`  |
| 2308   | Layout 1 | `9f7afde34166`  |
| 2302   | Layout 1 | `9f7afde34166`  |
| 2295   | Layout 1 | `9f7afde34166`  |
| 2290   | Layout 1 | `9f7afde34166`  |
| 2284   | Layout 1 | `9f7afde34166`  |
| 2276   | Layout 1 | `9f7afde34166`  |
| 2269   | Layout 1 | `9f7afde34166`  |
| 2259   | Layout 1 | `9f7afde34166`  |
| 2250   | Layout 1 | `9f7afde34166`  |
| 2243   | Layout 1 | `9f7afde34166`  |
| 2235   | Layout 1 | `9f7afde34166`  |
| 2229   | Layout 1 | `9f7afde34166`  |
| 2224   | Layout 1 | `9f7afde34166`  |
| 2218   | Layout 1 | `9f7afde34166`  |
| 2215   | Layout 1 | `9f7afde34166`  |
| 2207   | Layout 1 | `9f7afde34166`  |
| 2203   | Layout 1 | `9f7afde34166`  |
| 2196   | Layout 1 | `9f7afde34166`  |
| 2192   | Layout 1 | `9f7afde34166`  |
| 2189   | Layout 1 | `9f7afde34166`  |
| 2183   | Layout 1 | `9f7afde34166`  |
| 2179   | Layout 1 | `9f7afde34166`  |
| 2171   | Layout 1 | `9f7afde34166`  |
| 2163   | Layout 1 | `9f7afde34166`  |
| 2156   | Layout 1 | `9f7afde34166`  |
| 2151   | Layout 1 | `9f7afde34166`  |
| 2147   | Layout 1 | `9f7afde34166`  |
| 2142   | Layout 1 | `9f7afde34166`  |
| 2138   | Layout 1 | `9f7afde34166`  |
| 2134   | Layout 1 | `9f7afde34166`  |
| 2130   | Layout 1 | `9f7afde34166`  |
| 2122   | Layout 1 | `9f7afde34166`  |
| 2107   | Layout 1 | `9f7afde34166`  |
| 2098   | Layout 1 | `9f7afde34166`  |
| 2089   | Layout 1 | `9f7afde34166`  |
| 2081   | Layout 1 | `9f7afde34166`  |
| 2073   | Layout 1 | `9f7afde34166`  |
| 2067   | Layout 1 | `9f7afde34166`  |
| 2063   | Layout 1 | `9f7afde34166`  |
| 2059   | Layout 1 | `9f7afde34166`  |
| 2052   | Layout 1 | `9f7afde34166`  |
| 2044   | Layout 1 | `9f7afde34166`  |
| 2039   | Layout 1 | `9f7afde34166`  |
| 2032   | Layout 1 | `9f7afde34166`  |
| 2025   | Layout 1 | `9f7afde34166`  |
| 2011   | Layout 1 | `9f7afde34166`  |
| 2005   | Layout 1 | `9f7afde34166`  |
| 2000   | Layout 1 | `9f7afde34166`  |
| 1996   | Layout 1 | `9f7afde34166`  |
| 1991   | Layout 1 | `9f7afde34166`  |
| 1985   | Layout 1 | `9f7afde34166`  |
| 1980   | Layout 1 | `9f7afde34166`  |
| 1969   | Layout 1 | `9f7afde34166`  |
| 1964   | Layout 1 | `9f7afde34166`  |
| 1958   | Layout 1 | `9f7afde34166`  |
| 1950   | Layout 1 | `9f7afde34166`  |
| 1945   | Layout 1 | `9f7afde34166`  |
| 1937   | Layout 1 | `9f7afde34166`  |
| 1933   | Layout 1 | `9f7afde34166`  |
| 1927   | Layout 1 | `9f7afde34166`  |
| 1921   | Layout 1 | `9f7afde34166`  |
| 1914   | Layout 1 | `9f7afde34166`  |
| 1908   | Layout 1 | `9f7afde34166`  |
| 1897   | Layout 1 | `9f7afde34166`  |
| 1892   | Layout 1 | `9f7afde34166`  |
| 1886   | Layout 1 | `9f7afde34166`  |
| 1881   | Layout 1 | `9f7afde34166`  |
| 1871   | Layout 1 | `9f7afde34166`  |
| 1866   | Layout 1 | `9f7afde34166`  |
| 1862   | Layout 1 | `9f7afde34166`  |
| 1854   | Layout 1 | `9f7afde34166`  |
| 1846   | Layout 1 | `9f7afde34166`  |
| 1838   | Layout 1 | `9f7afde34166`  |
| 1832   | Layout 1 | `9f7afde34166`  |
| 1826   | Layout 1 | `9f7afde34166`  |
| 1822   | Layout 1 | `9f7afde34166`  |
| 1818   | Layout 1 | `9f7afde34166`  |
| 1804   | Layout 1 | `9f7afde34166`  |
| 1794   | Layout 1 | `9f7afde34166`  |
| 1790   | Layout 1 | `9f7afde34166`  |
| 1784   | Layout 1 | `9f7afde34166`  |
| 1774   | Layout 1 | `9f7afde34166`  |
| 1771   | Layout 1 | `9f7afde34166`  |
| 1762   | Layout 1 | `9f7afde34166`  |
| 1759   | Layout 1 | `9f7afde34166`  |
| 1754   | Layout 1 | `9f7afde34166`  |
| 1749   | Layout 1 | `9f7afde34166`  |
| 1743   | Layout 1 | `9f7afde34166`  |
| 1737   | Layout 1 | `9f7afde34166`  |
| 1731   | Layout 1 | `9f7afde34166`  |
| 1725   | Layout 1 | `9f7afde34166`  |
| 1717   | Layout 1 | `9f7afde34166`  |
| 1710   | Layout 1 | `9f7afde34166`  |
| 1704   | Layout 1 | `9f7afde34166`  |
| 1698   | Layout 1 | `9f7afde34166`  |
| 1690   | Layout 1 | `9f7afde34166`  |
| 1685   | Layout 1 | `9f7afde34166`  |
| 1680   | Layout 1 | `9f7afde34166`  |
| 1674   | Layout 1 | `9f7afde34166`  |
| 1668   | Layout 1 | `9f7afde34166`  |
| 1659   | Layout 1 | `9f7afde34166`  |
| 1649   | Layout 1 | `9f7afde34166`  |
| 1642   | Layout 1 | `9f7afde34166`  |
| 1636   | Layout 1 | `9f7afde34166`  |
| 1628   | Layout 1 | `9f7afde34166`  |
| 1622   | Layout 1 | `9f7afde34166`  |
| 1614   | Layout 1 | `9f7afde34166`  |
| 1608   | Layout 1 | `9f7afde34166`  |
| 1602   | Layout 1 | `9f7afde34166`  |
| 1598   | Layout 1 | `9f7afde34166`  |
| 1594   | Layout 1 | `9f7afde34166`  |
| 1590   | Layout 1 | `9f7afde34166`  |
| 1587   | Layout 1 | `9f7afde34166`  |
| 1584   | Layout 1 | `9f7afde34166`  |
| 1579   | Layout 1 | `9f7afde34166`  |
| 1572   | Layout 1 | `9f7afde34166`  |
| 1565   | Layout 1 | `9f7afde34166`  |
| 1559   | Layout 1 | `9f7afde34166`  |
| 1554   | Layout 1 | `9f7afde34166`  |
| 1547   | Layout 1 | `9f7afde34166`  |
| 1537   | Layout 1 | `9f7afde34166`  |
| 1529   | Layout 1 | `9f7afde34166`  |
| 1524   | Layout 1 | `9f7afde34166`  |
| 1519   | Layout 1 | `9f7afde34166`  |
| 1509   | Layout 1 | `9f7afde34166`  |
| 1506   | Layout 1 | `9f7afde34166`  |
| 1504   | Layout 1 | `9f7afde34166`  |
| 1500   | Layout 1 | `9f7afde34166`  |
| 1493   | Layout 1 | `9f7afde34166`  |
| 1489   | Layout 1 | `9f7afde34166`  |
| 1485   | Layout 1 | `9f7afde34166`  |
| 1481   | Layout 1 | `9f7afde34166`  |
| 1474   | Layout 1 | `9f7afde34166`  |
| 1466   | Layout 1 | `9f7afde34166`  |
| 1462   | Layout 1 | `9f7afde34166`  |
| 1459   | Layout 1 | `9f7afde34166`  |
| 1453   | Layout 1 | `9f7afde34166`  |
| 1450   | Layout 1 | `9f7afde34166`  |
| 1445   | Layout 1 | `9f7afde34166`  |
| 1439   | Layout 1 | `9f7afde34166`  |
| 1433   | Layout 1 | `9f7afde34166`  |
| 1430   | Layout 1 | `9f7afde34166`  |
| 1426   | Layout 1 | `9f7afde34166`  |
| 1421   | Layout 1 | `9f7afde34166`  |
| 1417   | Layout 1 | `9f7afde34166`  |
| 1416   | Layout 1 | `9f7afde34166`  |
| 1409   | Layout 1 | `9f7afde34166`  |
| 1405   | Layout 1 | `9f7afde34166`  |
| 1401   | Layout 1 | `9f7afde34166`  |
| 1396   | Layout 1 | `9f7afde34166`  |
| 1391   | Layout 1 | `9f7afde34166`  |
| 1390   | Layout 1 | `9f7afde34166`  |
| 1386   | Layout 1 | `9f7afde34166`  |
| 1381   | Layout 1 | `9f7afde34166`  |
| 1379   | Layout 1 | `9f7afde34166`  |
| 1372   | Layout 1 | `9f7afde34166`  |
| 1366   | Layout 1 | `9f7afde34166`  |
| 1364   | Layout 1 | `9f7afde34166`  |
| 1363   | Layout 1 | `9f7afde34166`  |
| 1360   | Layout 1 | `9f7afde34166`  |
| 1358   | Layout 1 | `9f7afde34166`  |
| 1355   | Layout 1 | `9f7afde34166`  |
| 1351   | Layout 1 | `9f7afde34166`  |
| 1348   | Layout 1 | `9f7afde34166`  |
| 1346   | Layout 1 | `9f7afde34166`  |
| 1341   | Layout 1 | `9f7afde34166`  |
| 1340   | Layout 1 | `9f7afde34166`  |
| 1338   | Layout 1 | `9f7afde34166`  |
| 1335   | Layout 1 | `9f7afde34166`  |
| 1333   | Layout 1 | `9f7afde34166`  |
| 1329   | Layout 1 | `9f7afde34166`  |
| 1327   | Layout 1 | `9f7afde34166`  |
| 1324   | Layout 1 | `9f7afde34166`  |
| 1321   | Layout 1 | `9f7afde34166`  |
| 1319   | Layout 1 | `9f7afde34166`  |
| 1318   | Layout 1 | `9f7afde34166`  |
| 1316   | Layout 1 | `9f7afde34166`  |
| 1313   | Layout 1 | `9f7afde34166`  |
| 1311   | Layout 1 | `9f7afde34166`  |
| 1309   | Layout 1 | `9f7afde34166`  |
| 1304   | Layout 1 | `9f7afde34166`  |
| 1292   | Layout 1 | `9f7afde34166`  |
| 1286   | Layout 1 | `9f7afde34166`  |
| 1280   | Layout 1 | `9f7afde34166`  |
| 1276   | Layout 1 | `9f7afde34166`  |
| 1267   | Layout 1 | `9f7afde34166`  |
| 1261   | Layout 1 | `9f7afde34166`  |
| 1256   | Layout 1 | `9f7afde34166`  |
| 1250   | Layout 1 | `9f7afde34166`  |
| 1246   | Layout 1 | `9f7afde34166`  |
| 1239   | Layout 1 | `9f7afde34166`  |
| 1230   | Layout 1 | `9f7afde34166`  |
| 1226   | Layout 1 | `9f7afde34166`  |
| 1220   | Layout 1 | `9f7afde34166`  |
| 1217   | Layout 1 | `9f7afde34166`  |
| 1211   | Layout 1 | `9f7afde34166`  |
| 1210   | Layout 1 | `9f7afde34166`  |
| 1208   | Layout 1 | `9f7afde34166`  |
| 1203   | Layout 1 | `9f7afde34166`  |
| 1197   | Layout 1 | `9f7afde34166`  |
| 1194   | Layout 1 | `9f7afde34166`  |
| 1192   | Layout 1 | `9f7afde34166`  |
| 1187   | Layout 1 | `9f7afde34166`  |
| 1183   | Layout 1 | `9f7afde34166`  |
| 1177   | Layout 1 | `9f7afde34166`  |
| 1173   | Layout 1 | `9f7afde34166`  |
| 1167   | Layout 1 | `9f7afde34166`  |
| 1164   | Layout 1 | `9f7afde34166`  |
| 1156   | Layout 1 | `9f7afde34166`  |
| 1149   | Layout 1 | `9f7afde34166`  |
| 1144   | Layout 1 | `9f7afde34166`  |
| 1137   | Layout 1 | `9f7afde34166`  |
| 1132   | Layout 1 | `9f7afde34166`  |
| 1127   | Layout 1 | `9f7afde34166`  |
| 1122   | Layout 1 | `9f7afde34166`  |
| 1118   | Layout 1 | `9f7afde34166`  |
| 1114   | Layout 1 | `9f7afde34166`  |
| 1109   | Layout 1 | `9f7afde34166`  |
| 1102   | No file  | `9f7afde34166`  |
| 1096   | No file  | `9f7afde34166`  |
| 1088   | No file  | `9f7afde34166`  |
| 1081   | No file  | `9f7afde34166`  |
| 1076   | No file  | `9f7afde34166`  |
| 1069   | No file  | `9f7afde34166`  |
| 1064   | No file  | `9f7afde34166`  |
| 1058   | No file  | `9f7afde34166`  |
| 1051   | No file  | `9f7afde34166`  |
| 1044   | No file  | `9f7afde34166`  |
| 1036   | No file  | `9f7afde34166`  |
| 1026   | No file  | `9f7afde34166`  |
| 1016   | No file  | `9f7afde34166`  |
| 1009   | No file  | `9f7afde34166`  |
| 1005   | No file  | `9f7afde34166`  |
| 1000   | No file  | `9f7afde34166`  |
| 998    | No file  | `9f7afde34166`  |
| 990    | No file  | `9f7afde34166`  |
| 979    | No file  | `9f7afde34166`  |
| 972    | No file  | `9f7afde34166`  |
| 963    | No file  | `9f7afde34166`  |
| 955    | No file  | `9f7afde34166`  |
| 946    | No file  | `9f7afde34166`  |
| 938    | No file  | `9f7afde34166`  |
| 927    | No file  | `9f7afde34166`  |
| 911    | No file  | `9f7afde34166`  |
| 904    | No file  | `9f7afde34166`  |
| 899    | No file  | `9f7afde34166`  |
| 894    | No file  | `9f7afde34166`  |
| 885    | No file  | `9f7afde34166`  |
| 879    | No file  | `9f7afde34166`  |
| 872    | No file  | `9f7afde34166`  |
| 864    | No file  | `9f7afde34166`  |
| 855    | No file  | `9f7afde34166`  |
| 853    | No file  | `9f7afde34166`  |
| 845    | No file  | `9f7afde34166`  |
| 837    | No file  | `9f7afde34166`  |
| 829    | No file  | `9f7afde34166`  |
| 822    | No file  | `9f7afde34166`  |
| 814    | No file  | `9f7afde34166`  |
| 805    | No file  | `9f7afde34166`  |
| 794    | No file  | `9f7afde34166`  |
| 787    | No file  | `9f7afde34166`  |
| 780    | No file  | `9f7afde34166`  |
| 771    | No file  | `9f7afde34166`  |
| 760    | No file  | `9f7afde34166`  |
| 748    | No file  | `9f7afde34166`  |
| 741    | No file  | `9f7afde34166`  |
| 736    | No file  | `9f7afde34166`  |
| 731    | No file  | `9f7afde34166`  |
| 723    | No file  | `9f7afde34166`  |
| 711    | No file  | `9f7afde34166`  |
| 707    | No file  | `9f7afde34166`  |
| 697    | No file  | `9f7afde34166`  |
| 689    | No file  | `9f7afde34166`  |
| 683    | No file  | `9f7afde34166`  |
| 678    | No file  | `9f7afde34166`  |
| 670    | No file  | `9f7afde34166`  |
| 661    | No file  | `9f7afde34166`  |
| 656    | No file  | `9f7afde34166`  |
| 652    | No file  | `9f7afde34166`  |
| 643    | No file  | `9f7afde34166`  |
| 637    | No file  | `9f7afde34166`  |
| 630    | No file  | `9f7afde34166`  |
| 627    | No file  | `9f7afde34166`  |
| 621    | No file  | `9f7afde34166`  |
| 617    | No file  | `9f7afde34166`  |
| 615    | No file  | `9f7afde34166`  |
| 606    | No file  | `9f7afde34166`  |
| 599    | No file  | `9f7afde34166`  |
| 592    | No file  | `9f7afde34166`  |
| 586    | No file  | `9f7afde34166`  |
| 577    | No file  | `9f7afde34166`  |
| 569    | No file  | `9f7afde34166`  |
| 561    | No file  | `9f7afde34166`  |
| 554    | No file  | `9f7afde34166`  |
| 542    | No file  | `9f7afde34166`  |
| 532    | No file  | `9f7afde34166`  |
| 531    | No file  | `9f7afde34166`  |
| 526    | No file  | `9f7afde34166`  |
| 521    | No file  | `9f7afde34166`  |
| 517    | No file  | `9f7afde34166`  |
| 510    | No file  | `9f7afde34166`  |
| 508    | No file  | `9f7afde34166`  |
| 504    | No file  | `9f7afde34166`  |
| 497    | No file  | `9f7afde34166`  |
| 491    | No file  | `9f7afde34166`  |
| 485    | No file  | `9f7afde34166`  |
| 478    | No file  | `9f7afde34166`  |
| 472    | No file  | `9f7afde34166`  |
| 466    | No file  | `9f7afde34166`  |
| 457    | No file  | `9f7afde34166`  |
| 452    | No file  | `9f7afde34166`  |
| 449    | No file  | `9f7afde34166`  |
| 435    | No file  | `9f7afde34166`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of steps                               |
| `+0x08`             | Row[row_count] | rows         | See Row; in falling `index` order             |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (43 bytes)

| Offset  | Type | Field         | Notes                                        |
| ------- | ---- | ------------- | -------------------------------------------- |
| `+0x00` | u16  | index         | Step key; unique                             |
| `+0x02` | u32  | point         | Equal to `index` on every row (client 3482)  |
| `+0x06` | f32  | offence_point | AP; equal to `index`                         |
| `+0x0A` | f32  | defence_point | DP; equal to `index`                         |
| `+0x0E` | f32  | hp            | Max HP; 100 times `index`                    |
| `+0x12` | u32  | mp            | 100 times `index`                            |
| `+0x16` | u32  | sp            | Stamina; 100 times `index`                   |
| `+0x1A` | u32  | weight        | 100 times `index`                            |
| `+0x1E` | u8   | inventory     | Equal to `index`                             |
| `+0x1F` | f32  | hit           | Accuracy; equal to `index`                   |
| `+0x23` | f32  | dv            | Evasion; equal to `index`                    |
| `+0x27` | u32  | unknown_27    | `0` on every row; no sheet column            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names are the `Index`, `Point`, `OffencePoint`, `DefencePoint`, `Hp`,
`Mp`, `Sp`, `Weight`, `Inventory`, `Hit` and `Dv` columns of the
`FamilyPointStat` sheet of a private server's `DataSheets.bexcel` on
client 1784, in that order. The client 1784 file and the client 3482 file
hold the same ten rows, and all 10 of 10 match the sheet on all eleven
columns. The values cannot order the fields by themselves: within a row
`index`, `point`, AP, DP, `inventory`, `hit` and `dv` are all N and the
four others all 100 times N, so the order of the names rests on the
sheet's column order. The sheet has no column for `unknown_27`. The
`FamilyPointStat` table of a private server on client 519 has the same
columns and values.

## Notes

- The Java server code of the private server on client 519 keys the steps
  by `Point` and adds the step under the family's points to the
  character's HP, MP, stamina, weight, inventory and accuracy.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/server_tables.py`.

## Open Questions

### The u32 at the End of the Row

`unknown_27` is `0` on every row of clients 1784 and 3482, and every
column of the sheet already has a field, so what it holds is open.
