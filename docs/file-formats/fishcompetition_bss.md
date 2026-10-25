# `fishcompetition.bss` Format

## Purpose

The fish of the fishing contest (the Fish Competition window opened from the
Fishing Encyclopedia): per fish item its grade, the reward box of each of
the six rank tiers and the title item for the biggest catch. After the rows
the file lists the last rank of each reward tier.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------- | ----- | ------- | --------- |
| 1      | 2863 and later | `fishcompetition.bss` | 5,765 | 173 Row | 33        |

| Layout | File                  | Known           | Unknown     |
| ------ | --------------------- | --------------- | ----------- |
| 1      | `fishcompetition.bss` | 5,753 B (99.8%) | 12 B (0.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `9952c1fb8ef1`  |
| 3482   | Layout 1 | `9952c1fb8ef1`  |
| 3474   | Layout 1 | `9952c1fb8ef1`  |
| 3473   | Layout 1 | `9952c1fb8ef1`  |
| 3464   | Layout 1 | `9952c1fb8ef1`  |
| 3458   | Layout 1 | `9952c1fb8ef1`  |
| 3454   | Layout 1 | `9952c1fb8ef1`  |
| 3444   | Layout 1 | `9952c1fb8ef1`  |
| 3435   | Layout 1 | `9952c1fb8ef1`  |
| 3426   | Layout 1 | `9952c1fb8ef1`  |
| 3418   | Layout 1 | `9952c1fb8ef1`  |
| 3412   | Layout 1 | `9952c1fb8ef1`  |
| 3402   | Layout 1 | `9952c1fb8ef1`  |
| 3396   | Layout 1 | `9952c1fb8ef1`  |
| 3387   | Layout 1 | `9952c1fb8ef1`  |
| 3381   | Layout 1 | `9952c1fb8ef1`  |
| 3373   | Layout 1 | `9952c1fb8ef1`  |
| 3364   | Layout 1 | `9952c1fb8ef1`  |
| 3356   | Layout 1 | `9952c1fb8ef1`  |
| 3349   | Layout 1 | `9952c1fb8ef1`  |
| 3342   | Layout 1 | `9952c1fb8ef1`  |
| 3335   | Layout 1 | `9952c1fb8ef1`  |
| 3326   | Layout 1 | `9952c1fb8ef1`  |
| 3321   | Layout 1 | `9952c1fb8ef1`  |
| 3314   | Layout 1 | `9952c1fb8ef1`  |
| 3303   | Layout 1 | `9952c1fb8ef1`  |
| 3302   | Layout 1 | `9952c1fb8ef1`  |
| 3293   | Layout 1 | `9952c1fb8ef1`  |
| 3283   | Layout 1 | `9952c1fb8ef1`  |
| 3275   | Layout 1 | `9952c1fb8ef1`  |
| 3267   | Layout 1 | `9952c1fb8ef1`  |
| 3258   | Layout 1 | `9952c1fb8ef1`  |
| 3251   | Layout 1 | `9952c1fb8ef1`  |
| 3242   | Layout 1 | `9952c1fb8ef1`  |
| 3235   | Layout 1 | `9952c1fb8ef1`  |
| 3229   | Layout 1 | `9952c1fb8ef1`  |
| 3212   | Layout 1 | `9952c1fb8ef1`  |
| 3203   | Layout 1 | `9952c1fb8ef1`  |
| 3193   | Layout 1 | `9952c1fb8ef1`  |
| 3186   | Layout 1 | `9952c1fb8ef1`  |
| 3177   | Layout 1 | `9952c1fb8ef1`  |
| 3169   | Layout 1 | `9952c1fb8ef1`  |
| 3158   | Layout 1 | `9952c1fb8ef1`  |
| 3151   | Layout 1 | `9952c1fb8ef1`  |
| 3144   | Layout 1 | `9952c1fb8ef1`  |
| 3133   | Layout 1 | `9952c1fb8ef1`  |
| 3125   | Layout 1 | `9952c1fb8ef1`  |
| 3118   | Layout 1 | `9952c1fb8ef1`  |
| 3111   | Layout 1 | `9952c1fb8ef1`  |
| 3103   | Layout 1 | `9952c1fb8ef1`  |
| 3095   | Layout 1 | `9952c1fb8ef1`  |
| 3086   | Layout 1 | `9952c1fb8ef1`  |
| 3072   | Layout 1 | `9952c1fb8ef1`  |
| 3062   | Layout 1 | `9952c1fb8ef1`  |
| 3052   | Layout 1 | `9952c1fb8ef1`  |
| 3045   | Layout 1 | `9952c1fb8ef1`  |
| 3037   | Layout 1 | `9952c1fb8ef1`  |
| 3030   | Layout 1 | `9952c1fb8ef1`  |
| 3021   | Layout 1 | `9952c1fb8ef1`  |
| 3012   | Layout 1 | `9952c1fb8ef1`  |
| 3002   | Layout 1 | `9952c1fb8ef1`  |
| 2995   | Layout 1 | `9952c1fb8ef1`  |
| 2987   | Layout 1 | `9952c1fb8ef1`  |
| 2978   | Layout 1 | `9952c1fb8ef1`  |
| 2970   | Layout 1 | `9952c1fb8ef1`  |
| 2959   | Layout 1 | `9952c1fb8ef1`  |
| 2951   | Layout 1 | `9952c1fb8ef1`  |
| 2942   | Layout 1 | `9952c1fb8ef1`  |
| 2935   | Layout 1 | `9952c1fb8ef1`  |
| 2932   | Layout 1 | `9952c1fb8ef1`  |
| 2923   | Layout 1 | `9952c1fb8ef1`  |
| 2919   | Layout 1 | `9952c1fb8ef1`  |
| 2907   | Layout 1 | `9952c1fb8ef1`  |
| 2900   | Layout 1 | `9952c1fb8ef1`  |
| 2891   | Layout 1 | `9952c1fb8ef1`  |
| 2882   | Layout 1 | `9952c1fb8ef1`  |
| 2872   | Layout 1 | `9952c1fb8ef1`  |
| 2863   | Layout 1 | `9952c1fb8ef1`  |
| 2855   | No file  | `9952c1fb8ef1`  |
| 2849   | No file  | `9952c1fb8ef1`  |
| 2844   | No file  | `9952c1fb8ef1`  |
| 2834   | No file  | `9952c1fb8ef1`  |
| 2825   | No file  | `9952c1fb8ef1`  |
| 2819   | No file  | `9952c1fb8ef1`  |
| 2811   | No file  | `9952c1fb8ef1`  |
| 2803   | No file  | `9952c1fb8ef1`  |
| 2794   | No file  | `9952c1fb8ef1`  |
| 2783   | No file  | `9952c1fb8ef1`  |
| 2774   | No file  | `9952c1fb8ef1`  |
| 2765   | No file  | `9952c1fb8ef1`  |
| 2756   | No file  | `9952c1fb8ef1`  |
| 2750   | No file  | `9952c1fb8ef1`  |
| 2743   | No file  | `9952c1fb8ef1`  |
| 2736   | No file  | `9952c1fb8ef1`  |
| 2726   | No file  | `9952c1fb8ef1`  |
| 2717   | No file  | `9952c1fb8ef1`  |
| 2709   | No file  | `9952c1fb8ef1`  |
| 2703   | No file  | `9952c1fb8ef1`  |
| 2695   | No file  | `9952c1fb8ef1`  |
| 2684   | No file  | `9952c1fb8ef1`  |
| 2672   | No file  | `9952c1fb8ef1`  |
| 2665   | No file  | `9952c1fb8ef1`  |
| 2657   | No file  | `9952c1fb8ef1`  |
| 2649   | No file  | `9952c1fb8ef1`  |
| 2644   | No file  | `9952c1fb8ef1`  |
| 2637   | No file  | `9952c1fb8ef1`  |
| 2629   | No file  | `9952c1fb8ef1`  |
| 2619   | No file  | `9952c1fb8ef1`  |
| 2612   | No file  | `9952c1fb8ef1`  |
| 2606   | No file  | `9952c1fb8ef1`  |
| 2602   | No file  | `9952c1fb8ef1`  |
| 2601   | No file  | `9952c1fb8ef1`  |
| 2592   | No file  | `9952c1fb8ef1`  |
| 2583   | No file  | `9952c1fb8ef1`  |
| 2575   | No file  | `9952c1fb8ef1`  |
| 2567   | No file  | `9952c1fb8ef1`  |
| 2560   | No file  | `9952c1fb8ef1`  |
| 2553   | No file  | `9952c1fb8ef1`  |
| 2545   | No file  | `9952c1fb8ef1`  |
| 2538   | No file  | `9952c1fb8ef1`  |
| 2529   | No file  | `9952c1fb8ef1`  |
| 2519   | No file  | `9952c1fb8ef1`  |
| 2513   | No file  | `9952c1fb8ef1`  |
| 2510   | No file  | `9952c1fb8ef1`  |
| 2507   | No file  | `9952c1fb8ef1`  |
| 2503   | No file  | `9952c1fb8ef1`  |
| 2498   | No file  | `9952c1fb8ef1`  |
| 2492   | No file  | `9952c1fb8ef1`  |
| 2487   | No file  | `9952c1fb8ef1`  |
| 2480   | No file  | `9952c1fb8ef1`  |
| 2474   | No file  | `9952c1fb8ef1`  |
| 2468   | No file  | `9952c1fb8ef1`  |
| 2460   | No file  | `9952c1fb8ef1`  |
| 2453   | No file  | `9952c1fb8ef1`  |
| 2444   | No file  | `9952c1fb8ef1`  |
| 2438   | No file  | `9952c1fb8ef1`  |
| 2434   | No file  | `9952c1fb8ef1`  |
| 2429   | No file  | `9952c1fb8ef1`  |
| 2421   | No file  | `9952c1fb8ef1`  |
| 2414   | No file  | `9952c1fb8ef1`  |
| 2407   | No file  | `9952c1fb8ef1`  |
| 2401   | No file  | `9952c1fb8ef1`  |
| 2397   | No file  | `9952c1fb8ef1`  |
| 2393   | No file  | `9952c1fb8ef1`  |
| 2384   | No file  | `9952c1fb8ef1`  |
| 2378   | No file  | `9952c1fb8ef1`  |
| 2372   | No file  | `9952c1fb8ef1`  |
| 2358   | No file  | `9952c1fb8ef1`  |
| 2352   | No file  | `9952c1fb8ef1`  |
| 2347   | No file  | `9952c1fb8ef1`  |
| 2343   | No file  | `9952c1fb8ef1`  |
| 2335   | No file  | `9952c1fb8ef1`  |
| 2327   | No file  | `9952c1fb8ef1`  |
| 2324   | No file  | `9952c1fb8ef1`  |
| 2319   | No file  | `9952c1fb8ef1`  |
| 2313   | No file  | `9952c1fb8ef1`  |
| 2308   | No file  | `9952c1fb8ef1`  |
| 2302   | No file  | `9952c1fb8ef1`  |
| 2295   | No file  | `9952c1fb8ef1`  |
| 2290   | No file  | `9952c1fb8ef1`  |
| 2284   | No file  | `9952c1fb8ef1`  |
| 2276   | No file  | `9952c1fb8ef1`  |
| 2269   | No file  | `9952c1fb8ef1`  |
| 2259   | No file  | `9952c1fb8ef1`  |
| 2250   | No file  | `9952c1fb8ef1`  |
| 2243   | No file  | `9952c1fb8ef1`  |
| 2235   | No file  | `9952c1fb8ef1`  |
| 2229   | No file  | `9952c1fb8ef1`  |
| 2224   | No file  | `9952c1fb8ef1`  |
| 2218   | No file  | `9952c1fb8ef1`  |
| 2215   | No file  | `9952c1fb8ef1`  |
| 2207   | No file  | `9952c1fb8ef1`  |
| 2203   | No file  | `9952c1fb8ef1`  |
| 2196   | No file  | `9952c1fb8ef1`  |
| 2192   | No file  | `9952c1fb8ef1`  |
| 2189   | No file  | `9952c1fb8ef1`  |
| 2183   | No file  | `9952c1fb8ef1`  |
| 2179   | No file  | `9952c1fb8ef1`  |
| 2171   | No file  | `9952c1fb8ef1`  |
| 2163   | No file  | `9952c1fb8ef1`  |
| 2156   | No file  | `9952c1fb8ef1`  |
| 2151   | No file  | `9952c1fb8ef1`  |
| 2147   | No file  | `9952c1fb8ef1`  |
| 2142   | No file  | `9952c1fb8ef1`  |
| 2138   | No file  | `9952c1fb8ef1`  |
| 2134   | No file  | `9952c1fb8ef1`  |
| 2130   | No file  | `9952c1fb8ef1`  |
| 2122   | No file  | `9952c1fb8ef1`  |
| 2107   | No file  | `9952c1fb8ef1`  |
| 2098   | No file  | `9952c1fb8ef1`  |
| 2089   | No file  | `9952c1fb8ef1`  |
| 2081   | No file  | `9952c1fb8ef1`  |
| 2073   | No file  | `9952c1fb8ef1`  |
| 2067   | No file  | `9952c1fb8ef1`  |
| 2063   | No file  | `9952c1fb8ef1`  |
| 2059   | No file  | `9952c1fb8ef1`  |
| 2052   | No file  | `9952c1fb8ef1`  |
| 2044   | No file  | `9952c1fb8ef1`  |
| 2039   | No file  | `9952c1fb8ef1`  |
| 2032   | No file  | `9952c1fb8ef1`  |
| 2025   | No file  | `9952c1fb8ef1`  |
| 2011   | No file  | `9952c1fb8ef1`  |
| 2005   | No file  | `9952c1fb8ef1`  |
| 2000   | No file  | `9952c1fb8ef1`  |
| 1996   | No file  | `9952c1fb8ef1`  |
| 1991   | No file  | `9952c1fb8ef1`  |
| 1985   | No file  | `9952c1fb8ef1`  |
| 1980   | No file  | `9952c1fb8ef1`  |
| 1969   | No file  | `9952c1fb8ef1`  |
| 1964   | No file  | `9952c1fb8ef1`  |
| 1958   | No file  | `9952c1fb8ef1`  |
| 1950   | No file  | `9952c1fb8ef1`  |
| 1945   | No file  | `9952c1fb8ef1`  |
| 1937   | No file  | `9952c1fb8ef1`  |
| 1933   | No file  | `9952c1fb8ef1`  |
| 1927   | No file  | `9952c1fb8ef1`  |
| 1921   | No file  | `9952c1fb8ef1`  |
| 1914   | No file  | `9952c1fb8ef1`  |
| 1908   | No file  | `9952c1fb8ef1`  |
| 1897   | No file  | `9952c1fb8ef1`  |
| 1892   | No file  | `9952c1fb8ef1`  |
| 1886   | No file  | `9952c1fb8ef1`  |
| 1881   | No file  | `9952c1fb8ef1`  |
| 1871   | No file  | `9952c1fb8ef1`  |
| 1866   | No file  | `9952c1fb8ef1`  |
| 1862   | No file  | `9952c1fb8ef1`  |
| 1854   | No file  | `9952c1fb8ef1`  |
| 1846   | No file  | `9952c1fb8ef1`  |
| 1838   | No file  | `9952c1fb8ef1`  |
| 1832   | No file  | `9952c1fb8ef1`  |
| 1826   | No file  | `9952c1fb8ef1`  |
| 1822   | No file  | `9952c1fb8ef1`  |
| 1818   | No file  | `9952c1fb8ef1`  |
| 1804   | No file  | `9952c1fb8ef1`  |
| 1794   | No file  | `9952c1fb8ef1`  |
| 1790   | No file  | `9952c1fb8ef1`  |
| 1784   | No file  | `9952c1fb8ef1`  |
| 1774   | No file  | `9952c1fb8ef1`  |
| 1771   | No file  | `9952c1fb8ef1`  |
| 1762   | No file  | `9952c1fb8ef1`  |
| 1759   | No file  | `9952c1fb8ef1`  |
| 1754   | No file  | `9952c1fb8ef1`  |
| 1749   | No file  | `9952c1fb8ef1`  |
| 1743   | No file  | `9952c1fb8ef1`  |
| 1737   | No file  | `9952c1fb8ef1`  |
| 1731   | No file  | `9952c1fb8ef1`  |
| 1725   | No file  | `9952c1fb8ef1`  |
| 1717   | No file  | `9952c1fb8ef1`  |
| 1710   | No file  | `9952c1fb8ef1`  |
| 1704   | No file  | `9952c1fb8ef1`  |
| 1698   | No file  | `9952c1fb8ef1`  |
| 1690   | No file  | `9952c1fb8ef1`  |
| 1685   | No file  | `9952c1fb8ef1`  |
| 1680   | No file  | `9952c1fb8ef1`  |
| 1674   | No file  | `9952c1fb8ef1`  |
| 1668   | No file  | `9952c1fb8ef1`  |
| 1659   | No file  | `9952c1fb8ef1`  |
| 1649   | No file  | `9952c1fb8ef1`  |
| 1642   | No file  | `9952c1fb8ef1`  |
| 1636   | No file  | `9952c1fb8ef1`  |
| 1628   | No file  | `9952c1fb8ef1`  |
| 1622   | No file  | `9952c1fb8ef1`  |
| 1614   | No file  | `9952c1fb8ef1`  |
| 1608   | No file  | `9952c1fb8ef1`  |
| 1602   | No file  | `9952c1fb8ef1`  |
| 1598   | No file  | `9952c1fb8ef1`  |
| 1594   | No file  | `9952c1fb8ef1`  |
| 1590   | No file  | `9952c1fb8ef1`  |
| 1587   | No file  | `9952c1fb8ef1`  |
| 1584   | No file  | `9952c1fb8ef1`  |
| 1579   | No file  | `9952c1fb8ef1`  |
| 1572   | No file  | `9952c1fb8ef1`  |
| 1565   | No file  | `9952c1fb8ef1`  |
| 1559   | No file  | `9952c1fb8ef1`  |
| 1554   | No file  | `9952c1fb8ef1`  |
| 1547   | No file  | `9952c1fb8ef1`  |
| 1537   | No file  | `9952c1fb8ef1`  |
| 1529   | No file  | `9952c1fb8ef1`  |
| 1524   | No file  | `9952c1fb8ef1`  |
| 1519   | No file  | `9952c1fb8ef1`  |
| 1509   | No file  | `9952c1fb8ef1`  |
| 1506   | No file  | `9952c1fb8ef1`  |
| 1504   | No file  | `9952c1fb8ef1`  |
| 1500   | No file  | `9952c1fb8ef1`  |
| 1493   | No file  | `9952c1fb8ef1`  |
| 1489   | No file  | `9952c1fb8ef1`  |
| 1485   | No file  | `9952c1fb8ef1`  |
| 1481   | No file  | `9952c1fb8ef1`  |
| 1474   | No file  | `9952c1fb8ef1`  |
| 1466   | No file  | `9952c1fb8ef1`  |
| 1462   | No file  | `9952c1fb8ef1`  |
| 1459   | No file  | `9952c1fb8ef1`  |
| 1453   | No file  | `9952c1fb8ef1`  |
| 1450   | No file  | `9952c1fb8ef1`  |
| 1445   | No file  | `9952c1fb8ef1`  |
| 1439   | No file  | `9952c1fb8ef1`  |
| 1433   | No file  | `9952c1fb8ef1`  |
| 1430   | No file  | `9952c1fb8ef1`  |
| 1426   | No file  | `9952c1fb8ef1`  |
| 1421   | No file  | `9952c1fb8ef1`  |
| 1417   | No file  | `9952c1fb8ef1`  |
| 1416   | No file  | `9952c1fb8ef1`  |
| 1409   | No file  | `9952c1fb8ef1`  |
| 1405   | No file  | `9952c1fb8ef1`  |
| 1401   | No file  | `9952c1fb8ef1`  |
| 1396   | No file  | `9952c1fb8ef1`  |
| 1391   | No file  | `9952c1fb8ef1`  |
| 1390   | No file  | `9952c1fb8ef1`  |
| 1386   | No file  | `9952c1fb8ef1`  |
| 1381   | No file  | `9952c1fb8ef1`  |
| 1379   | No file  | `9952c1fb8ef1`  |
| 1372   | No file  | `9952c1fb8ef1`  |
| 1366   | No file  | `9952c1fb8ef1`  |
| 1364   | No file  | `9952c1fb8ef1`  |
| 1363   | No file  | `9952c1fb8ef1`  |
| 1360   | No file  | `9952c1fb8ef1`  |
| 1358   | No file  | `9952c1fb8ef1`  |
| 1355   | No file  | `9952c1fb8ef1`  |
| 1351   | No file  | `9952c1fb8ef1`  |
| 1348   | No file  | `9952c1fb8ef1`  |
| 1346   | No file  | `9952c1fb8ef1`  |
| 1341   | No file  | `9952c1fb8ef1`  |
| 1340   | No file  | `9952c1fb8ef1`  |
| 1338   | No file  | `9952c1fb8ef1`  |
| 1335   | No file  | `9952c1fb8ef1`  |
| 1333   | No file  | `9952c1fb8ef1`  |
| 1329   | No file  | `9952c1fb8ef1`  |
| 1327   | No file  | `9952c1fb8ef1`  |
| 1324   | No file  | `9952c1fb8ef1`  |
| 1321   | No file  | `9952c1fb8ef1`  |
| 1319   | No file  | `9952c1fb8ef1`  |
| 1318   | No file  | `9952c1fb8ef1`  |
| 1316   | No file  | `9952c1fb8ef1`  |
| 1313   | No file  | `9952c1fb8ef1`  |
| 1311   | No file  | `9952c1fb8ef1`  |
| 1309   | No file  | `9952c1fb8ef1`  |
| 1304   | No file  | `9952c1fb8ef1`  |
| 1292   | No file  | `9952c1fb8ef1`  |
| 1286   | No file  | `9952c1fb8ef1`  |
| 1280   | No file  | `9952c1fb8ef1`  |
| 1276   | No file  | `9952c1fb8ef1`  |
| 1267   | No file  | `9952c1fb8ef1`  |
| 1261   | No file  | `9952c1fb8ef1`  |
| 1256   | No file  | `9952c1fb8ef1`  |
| 1250   | No file  | `9952c1fb8ef1`  |
| 1246   | No file  | `9952c1fb8ef1`  |
| 1239   | No file  | `9952c1fb8ef1`  |
| 1230   | No file  | `9952c1fb8ef1`  |
| 1226   | No file  | `9952c1fb8ef1`  |
| 1220   | No file  | `9952c1fb8ef1`  |
| 1217   | No file  | `9952c1fb8ef1`  |
| 1211   | No file  | `9952c1fb8ef1`  |
| 1210   | No file  | `9952c1fb8ef1`  |
| 1208   | No file  | `9952c1fb8ef1`  |
| 1203   | No file  | `9952c1fb8ef1`  |
| 1197   | No file  | `9952c1fb8ef1`  |
| 1194   | No file  | `9952c1fb8ef1`  |
| 1192   | No file  | `9952c1fb8ef1`  |
| 1187   | No file  | `9952c1fb8ef1`  |
| 1183   | No file  | `9952c1fb8ef1`  |
| 1177   | No file  | `9952c1fb8ef1`  |
| 1173   | No file  | `9952c1fb8ef1`  |
| 1167   | No file  | `9952c1fb8ef1`  |
| 1164   | No file  | `9952c1fb8ef1`  |
| 1156   | No file  | `9952c1fb8ef1`  |
| 1149   | No file  | `9952c1fb8ef1`  |
| 1144   | No file  | `9952c1fb8ef1`  |
| 1137   | No file  | `9952c1fb8ef1`  |
| 1132   | No file  | `9952c1fb8ef1`  |
| 1127   | No file  | `9952c1fb8ef1`  |
| 1122   | No file  | `9952c1fb8ef1`  |
| 1118   | No file  | `9952c1fb8ef1`  |
| 1114   | No file  | `9952c1fb8ef1`  |
| 1109   | No file  | `9952c1fb8ef1`  |
| 1102   | No file  | `9952c1fb8ef1`  |
| 1096   | No file  | `9952c1fb8ef1`  |
| 1088   | No file  | `9952c1fb8ef1`  |
| 1081   | No file  | `9952c1fb8ef1`  |
| 1076   | No file  | `9952c1fb8ef1`  |
| 1069   | No file  | `9952c1fb8ef1`  |
| 1064   | No file  | `9952c1fb8ef1`  |
| 1058   | No file  | `9952c1fb8ef1`  |
| 1051   | No file  | `9952c1fb8ef1`  |
| 1044   | No file  | `9952c1fb8ef1`  |
| 1036   | No file  | `9952c1fb8ef1`  |
| 1026   | No file  | `9952c1fb8ef1`  |
| 1016   | No file  | `9952c1fb8ef1`  |
| 1009   | No file  | `9952c1fb8ef1`  |
| 1005   | No file  | `9952c1fb8ef1`  |
| 1000   | No file  | `9952c1fb8ef1`  |
| 998    | No file  | `9952c1fb8ef1`  |
| 990    | No file  | `9952c1fb8ef1`  |
| 979    | No file  | `9952c1fb8ef1`  |
| 972    | No file  | `9952c1fb8ef1`  |
| 963    | No file  | `9952c1fb8ef1`  |
| 955    | No file  | `9952c1fb8ef1`  |
| 946    | No file  | `9952c1fb8ef1`  |
| 938    | No file  | `9952c1fb8ef1`  |
| 927    | No file  | `9952c1fb8ef1`  |
| 911    | No file  | `9952c1fb8ef1`  |
| 904    | No file  | `9952c1fb8ef1`  |
| 899    | No file  | `9952c1fb8ef1`  |
| 894    | No file  | `9952c1fb8ef1`  |
| 885    | No file  | `9952c1fb8ef1`  |
| 879    | No file  | `9952c1fb8ef1`  |
| 872    | No file  | `9952c1fb8ef1`  |
| 864    | No file  | `9952c1fb8ef1`  |
| 855    | No file  | `9952c1fb8ef1`  |
| 853    | No file  | `9952c1fb8ef1`  |
| 845    | No file  | `9952c1fb8ef1`  |
| 837    | No file  | `9952c1fb8ef1`  |
| 829    | No file  | `9952c1fb8ef1`  |
| 822    | No file  | `9952c1fb8ef1`  |
| 814    | No file  | `9952c1fb8ef1`  |
| 805    | No file  | `9952c1fb8ef1`  |
| 794    | No file  | `9952c1fb8ef1`  |
| 787    | No file  | `9952c1fb8ef1`  |
| 780    | No file  | `9952c1fb8ef1`  |
| 771    | No file  | `9952c1fb8ef1`  |
| 760    | No file  | `9952c1fb8ef1`  |
| 748    | No file  | `9952c1fb8ef1`  |
| 741    | No file  | `9952c1fb8ef1`  |
| 736    | No file  | `9952c1fb8ef1`  |
| 731    | No file  | `9952c1fb8ef1`  |
| 723    | No file  | `9952c1fb8ef1`  |
| 711    | No file  | `9952c1fb8ef1`  |
| 707    | No file  | `9952c1fb8ef1`  |
| 697    | No file  | `9952c1fb8ef1`  |
| 689    | No file  | `9952c1fb8ef1`  |
| 683    | No file  | `9952c1fb8ef1`  |
| 678    | No file  | `9952c1fb8ef1`  |
| 670    | No file  | `9952c1fb8ef1`  |
| 661    | No file  | `9952c1fb8ef1`  |
| 656    | No file  | `9952c1fb8ef1`  |
| 652    | No file  | `9952c1fb8ef1`  |
| 643    | No file  | `9952c1fb8ef1`  |
| 637    | No file  | `9952c1fb8ef1`  |
| 630    | No file  | `9952c1fb8ef1`  |
| 627    | No file  | `9952c1fb8ef1`  |
| 621    | No file  | `9952c1fb8ef1`  |
| 617    | No file  | `9952c1fb8ef1`  |
| 615    | No file  | `9952c1fb8ef1`  |
| 606    | No file  | `9952c1fb8ef1`  |
| 599    | No file  | `9952c1fb8ef1`  |
| 592    | No file  | `9952c1fb8ef1`  |
| 586    | No file  | `9952c1fb8ef1`  |
| 577    | No file  | `9952c1fb8ef1`  |
| 569    | No file  | `9952c1fb8ef1`  |
| 561    | No file  | `9952c1fb8ef1`  |
| 554    | No file  | `9952c1fb8ef1`  |
| 542    | No file  | `9952c1fb8ef1`  |
| 532    | No file  | `9952c1fb8ef1`  |
| 531    | No file  | `9952c1fb8ef1`  |
| 526    | No file  | `9952c1fb8ef1`  |
| 521    | No file  | `9952c1fb8ef1`  |
| 517    | No file  | `9952c1fb8ef1`  |
| 510    | No file  | `9952c1fb8ef1`  |
| 508    | No file  | `9952c1fb8ef1`  |
| 504    | No file  | `9952c1fb8ef1`  |
| 497    | No file  | `9952c1fb8ef1`  |
| 491    | No file  | `9952c1fb8ef1`  |
| 485    | No file  | `9952c1fb8ef1`  |
| 478    | No file  | `9952c1fb8ef1`  |
| 472    | No file  | `9952c1fb8ef1`  |
| 466    | No file  | `9952c1fb8ef1`  |
| 457    | No file  | `9952c1fb8ef1`  |
| 452    | No file  | `9952c1fb8ef1`  |
| 449    | No file  | `9952c1fb8ef1`  |
| 435    | No file  | `9952c1fb8ef1`  |

<!-- versions:end -->

## Companion Files

None. Item names come from LOC type `0`, else the `ITEM_NAME_KR` lookup
index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type              | Field           | Notes                                                       |
| ------------------- | ----------------- | --------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]           | magic           | ASCII `PABR`                                                |
| `+0x04`             | u32               | count           | Number of rows                                              |
| `+0x08`             | Row[count]        | rows            | See Row                                                     |
| `rows+0x00`         | u32               | unknown_rows_00 | `1` on clients 3002 and 3474                                |
| `rows+0x04`         | u32               | unknown_rows_04 | `1` on clients 3002 and 3474                                |
| `rows+0x08`         | u32               | unknown_rows_08 | `1` on clients 3002 and 3474                                |
| `rows+0x0C`         | u32[6]            | rank_tiers      | Last rank of each reward tier: `1`, `2`, `3`, `30`, `100`, `300` on clients 3002 and 3474 |
| `rows+0x24`         | String Table      | string_table    | See String Table                                            |
| `string_table+0x00` | u32               | table_start     | Offset of the string table                                  |
| `string_table+0x04` | u32               | zero            | Always `0`                                                  |

On client 3474 the file is 8 + 173 x 33 + 36 + 4 + 8 = 5,765 bytes.

### Row (33 bytes)

| Offset  | Type   | Field                 | Notes                                                                       |
| ------- | ------ | --------------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32    | fish_item_key         | The fish (`8330` Tilefish, `821017` Mantis Shrimp); unique                  |
| `+0x04` | u8     | grade                 | Grade of the fish: `2`, `3` or `4`; equals the fish item's grade on 173 of 173 rows (client 3474) |
| `+0x05` | u32[6] | rank_reward_item_keys | Reward item per rank tier, in `rank_tiers` order                            |
| `+0x1D` | u32    | title_item_key        | The `[Title] The Biggest <fish>` item; unique per row                       |

The rows are not sorted by key.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 3002 and 3474                   |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Rank Tiers

The reward info window (`panel_window_fishcompetitionrewardinfo.luac`) shows
`_rewardCount = 6` tiers. For tier `i` it calls
`ToClient_GetFishCompetitionRankByIndex(i - 1)`, prints the first
`_singleRankCount = 3` as single ranks (`PANEL_FISHEVENT_MYRANK`) and the
rest as ranges (`PANEL_FISHEVENT_RANKARRANGE`). The six `rank_tiers` values
are those ranks. Every row of clients 3002 and 3474 holds the same six
reward boxes:

| Tier | `rank_tiers` | `rank_reward_item_keys` | Item (LOC type 0)     |
| ---- | ------------ | ----------------------- | --------------------- |
| 1    | 1            | 767697                  | Waveswept Gold Box    |
| 2    | 2            | 767698                  | Waveswept Silver Box  |
| 3    | 3            | 767699                  | Waveswept Bronze Box  |
| 4    | 30           | 767700                  | Waveswept Blue Box    |
| 5    | 100          | 767701                  | Waveswept Green Box   |
| 6    | 300          | 767702                  | Waveswept Gray Box    |

## Field Names

No reference source has this table: the file is not in clients 1784, 2107
and 2519, and neither the 2016 symbols nor the client 1784 sheets name it.
The names follow the client Lua of client 3474:

- `grade`: the contest window colours each fish by
  `ToClient_GetFishCompetitionRareness(index)` and shows that many plus one
  rarity icons; the reward window has grades `_startGrade = 2` to
  `_endGrade = 4` (blue, yellow and red slots). The byte is `2` to `4` and
  matches the item grade of the fish on every row.
- `title_item_key`: the my-reward window asks a reward for
  `getRewardItemKey()` and `getRewardTitleKey()`; the row's last u32 is the
  title item of its fish.

## Notes

- Client 3474 has 173 rows (46 of grade `2`, 65 of grade `3`, 62 of grade
  `4`); client 3002 has 171.
- The reward window reads its items with
  `ToClient_GetCompetitionRewardByGradeAndIndex(grade, index)`; since every
  row holds the same boxes, the file does not show whether the client picks
  them per grade or per fish.

## Open Questions

### unknown_rows_00 to unknown_rows_08

Three u32 between the rows and `rank_tiers`, `1` each on clients 3002 and
3474. One of them may be a count of rank tier sets (with `rank_tiers` its
only entry), but nothing in the Lua reads more than one set.
