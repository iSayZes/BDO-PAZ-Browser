# `rosewarfiercebattlemonsterstaticstatus.bss` Format

## Purpose

The Rose War sanctums (fierce battles): one row per fierce battle key with
the guardian character of each team, the neutral character, the sanctum's
buff skill and its Korean name. On client 3474 the file has 22 rows: keys
`1` to `10` are the Kamasylvia side sanctums, `11` to `20` the O'dyllita
side ones, and `21` and `22` the two gimmick sanctums, 정령의 제단 and
해양 성소, guarded by Mysterious Statue alone.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                         | Bytes | Records | Row bytes |
| ------ | -------------- | -------------------------------------------- | ----- | ------- | --------- |
| 1      | 2545 and later | `rosewarfiercebattlemonsterstaticstatus.bss` | 828   | 22 Row  | 16        |

| Layout | File                                         | Known         | Unknown     |
| ------ | -------------------------------------------- | ------------- | ----------- |
| 1      | `rosewarfiercebattlemonsterstaticstatus.bss` | 784 B (94.7%) | 44 B (5.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e6155da07ecb`  |
| 3482   | Layout 1 | `e6155da07ecb`  |
| 3474   | Layout 1 | `e6155da07ecb`  |
| 3473   | Layout 1 | `e6155da07ecb`  |
| 3464   | Layout 1 | `e6155da07ecb`  |
| 3458   | Layout 1 | `e6155da07ecb`  |
| 3454   | Layout 1 | `e6155da07ecb`  |
| 3444   | Layout 1 | `e6155da07ecb`  |
| 3435   | Layout 1 | `e6155da07ecb`  |
| 3426   | Layout 1 | `e6155da07ecb`  |
| 3418   | Layout 1 | `e6155da07ecb`  |
| 3412   | Layout 1 | `e6155da07ecb`  |
| 3402   | Layout 1 | `e6155da07ecb`  |
| 3396   | Layout 1 | `e6155da07ecb`  |
| 3387   | Layout 1 | `e6155da07ecb`  |
| 3381   | Layout 1 | `e6155da07ecb`  |
| 3373   | Layout 1 | `e6155da07ecb`  |
| 3364   | Layout 1 | `e6155da07ecb`  |
| 3356   | Layout 1 | `e6155da07ecb`  |
| 3349   | Layout 1 | `e6155da07ecb`  |
| 3342   | Layout 1 | `e6155da07ecb`  |
| 3335   | Layout 1 | `e6155da07ecb`  |
| 3326   | Layout 1 | `e6155da07ecb`  |
| 3321   | Layout 1 | `e6155da07ecb`  |
| 3314   | Layout 1 | `e6155da07ecb`  |
| 3303   | Layout 1 | `e6155da07ecb`  |
| 3302   | Layout 1 | `e6155da07ecb`  |
| 3293   | Layout 1 | `e6155da07ecb`  |
| 3283   | Layout 1 | `e6155da07ecb`  |
| 3275   | Layout 1 | `e6155da07ecb`  |
| 3267   | Layout 1 | `e6155da07ecb`  |
| 3258   | Layout 1 | `e6155da07ecb`  |
| 3251   | Layout 1 | `e6155da07ecb`  |
| 3242   | Layout 1 | `e6155da07ecb`  |
| 3235   | Layout 1 | `e6155da07ecb`  |
| 3229   | Layout 1 | `e6155da07ecb`  |
| 3212   | Layout 1 | `e6155da07ecb`  |
| 3203   | Layout 1 | `e6155da07ecb`  |
| 3193   | Layout 1 | `e6155da07ecb`  |
| 3186   | Layout 1 | `e6155da07ecb`  |
| 3177   | Layout 1 | `e6155da07ecb`  |
| 3169   | Layout 1 | `e6155da07ecb`  |
| 3158   | Layout 1 | `e6155da07ecb`  |
| 3151   | Layout 1 | `e6155da07ecb`  |
| 3144   | Layout 1 | `e6155da07ecb`  |
| 3133   | Layout 1 | `e6155da07ecb`  |
| 3125   | Layout 1 | `e6155da07ecb`  |
| 3118   | Layout 1 | `e6155da07ecb`  |
| 3111   | Layout 1 | `e6155da07ecb`  |
| 3103   | Layout 1 | `e6155da07ecb`  |
| 3095   | Layout 1 | `e6155da07ecb`  |
| 3086   | Layout 1 | `e6155da07ecb`  |
| 3072   | Layout 1 | `e6155da07ecb`  |
| 3062   | Layout 1 | `e6155da07ecb`  |
| 3052   | Layout 1 | `e6155da07ecb`  |
| 3045   | Layout 1 | `e6155da07ecb`  |
| 3037   | Layout 1 | `e6155da07ecb`  |
| 3030   | Layout 1 | `e6155da07ecb`  |
| 3021   | Layout 1 | `e6155da07ecb`  |
| 3012   | Layout 1 | `e6155da07ecb`  |
| 3002   | Layout 1 | `e6155da07ecb`  |
| 2995   | Layout 1 | `e6155da07ecb`  |
| 2987   | Layout 1 | `e6155da07ecb`  |
| 2978   | Layout 1 | `e6155da07ecb`  |
| 2970   | Layout 1 | `e6155da07ecb`  |
| 2959   | Layout 1 | `e6155da07ecb`  |
| 2951   | Layout 1 | `e6155da07ecb`  |
| 2942   | Layout 1 | `e6155da07ecb`  |
| 2935   | Layout 1 | `e6155da07ecb`  |
| 2932   | Layout 1 | `e6155da07ecb`  |
| 2923   | Layout 1 | `e6155da07ecb`  |
| 2919   | Layout 1 | `e6155da07ecb`  |
| 2907   | Layout 1 | `e6155da07ecb`  |
| 2900   | Layout 1 | `e6155da07ecb`  |
| 2891   | Layout 1 | `e6155da07ecb`  |
| 2882   | Layout 1 | `e6155da07ecb`  |
| 2872   | Layout 1 | `e6155da07ecb`  |
| 2863   | Layout 1 | `e6155da07ecb`  |
| 2855   | Layout 1 | `e6155da07ecb`  |
| 2849   | Layout 1 | `e6155da07ecb`  |
| 2844   | Layout 1 | `e6155da07ecb`  |
| 2834   | Layout 1 | `e6155da07ecb`  |
| 2825   | Layout 1 | `e6155da07ecb`  |
| 2819   | Layout 1 | `e6155da07ecb`  |
| 2811   | Layout 1 | `e6155da07ecb`  |
| 2803   | Layout 1 | `e6155da07ecb`  |
| 2794   | Layout 1 | `e6155da07ecb`  |
| 2783   | Layout 1 | `e6155da07ecb`  |
| 2774   | Layout 1 | `e6155da07ecb`  |
| 2765   | Layout 1 | `e6155da07ecb`  |
| 2756   | Layout 1 | `e6155da07ecb`  |
| 2750   | Layout 1 | `e6155da07ecb`  |
| 2743   | Layout 1 | `e6155da07ecb`  |
| 2736   | Layout 1 | `e6155da07ecb`  |
| 2726   | Layout 1 | `e6155da07ecb`  |
| 2717   | Layout 1 | `e6155da07ecb`  |
| 2709   | Layout 1 | `e6155da07ecb`  |
| 2703   | Layout 1 | `e6155da07ecb`  |
| 2695   | Layout 1 | `e6155da07ecb`  |
| 2684   | Layout 1 | `e6155da07ecb`  |
| 2672   | Layout 1 | `e6155da07ecb`  |
| 2665   | Layout 1 | `e6155da07ecb`  |
| 2657   | Layout 1 | `e6155da07ecb`  |
| 2649   | Layout 1 | `e6155da07ecb`  |
| 2644   | Layout 1 | `e6155da07ecb`  |
| 2637   | Layout 1 | `e6155da07ecb`  |
| 2629   | Layout 1 | `e6155da07ecb`  |
| 2619   | Layout 1 | `e6155da07ecb`  |
| 2612   | Layout 1 | `e6155da07ecb`  |
| 2606   | Layout 1 | `e6155da07ecb`  |
| 2602   | Layout 1 | `e6155da07ecb`  |
| 2601   | Layout 1 | `e6155da07ecb`  |
| 2592   | Layout 1 | `e6155da07ecb`  |
| 2583   | Layout 1 | `e6155da07ecb`  |
| 2575   | Layout 1 | `e6155da07ecb`  |
| 2567   | Layout 1 | `e6155da07ecb`  |
| 2560   | Layout 1 | `e6155da07ecb`  |
| 2553   | Layout 1 | `e6155da07ecb`  |
| 2545   | Layout 1 | `e6155da07ecb`  |
| 2538   | No file  | `e6155da07ecb`  |
| 2529   | No file  | `e6155da07ecb`  |
| 2519   | No file  | `e6155da07ecb`  |
| 2513   | No file  | `e6155da07ecb`  |
| 2510   | No file  | `e6155da07ecb`  |
| 2507   | No file  | `e6155da07ecb`  |
| 2503   | No file  | `e6155da07ecb`  |
| 2498   | No file  | `e6155da07ecb`  |
| 2492   | No file  | `e6155da07ecb`  |
| 2487   | No file  | `e6155da07ecb`  |
| 2480   | No file  | `e6155da07ecb`  |
| 2474   | No file  | `e6155da07ecb`  |
| 2468   | No file  | `e6155da07ecb`  |
| 2460   | No file  | `e6155da07ecb`  |
| 2453   | No file  | `e6155da07ecb`  |
| 2444   | No file  | `e6155da07ecb`  |
| 2438   | No file  | `e6155da07ecb`  |
| 2434   | No file  | `e6155da07ecb`  |
| 2429   | No file  | `e6155da07ecb`  |
| 2421   | No file  | `e6155da07ecb`  |
| 2414   | No file  | `e6155da07ecb`  |
| 2407   | No file  | `e6155da07ecb`  |
| 2401   | No file  | `e6155da07ecb`  |
| 2397   | No file  | `e6155da07ecb`  |
| 2393   | No file  | `e6155da07ecb`  |
| 2384   | No file  | `e6155da07ecb`  |
| 2378   | No file  | `e6155da07ecb`  |
| 2372   | No file  | `e6155da07ecb`  |
| 2358   | No file  | `e6155da07ecb`  |
| 2352   | No file  | `e6155da07ecb`  |
| 2347   | No file  | `e6155da07ecb`  |
| 2343   | No file  | `e6155da07ecb`  |
| 2335   | No file  | `e6155da07ecb`  |
| 2327   | No file  | `e6155da07ecb`  |
| 2324   | No file  | `e6155da07ecb`  |
| 2319   | No file  | `e6155da07ecb`  |
| 2313   | No file  | `e6155da07ecb`  |
| 2308   | No file  | `e6155da07ecb`  |
| 2302   | No file  | `e6155da07ecb`  |
| 2295   | No file  | `e6155da07ecb`  |
| 2290   | No file  | `e6155da07ecb`  |
| 2284   | No file  | `e6155da07ecb`  |
| 2276   | No file  | `e6155da07ecb`  |
| 2269   | No file  | `e6155da07ecb`  |
| 2259   | No file  | `e6155da07ecb`  |
| 2250   | No file  | `e6155da07ecb`  |
| 2243   | No file  | `e6155da07ecb`  |
| 2235   | No file  | `e6155da07ecb`  |
| 2229   | No file  | `e6155da07ecb`  |
| 2224   | No file  | `e6155da07ecb`  |
| 2218   | No file  | `e6155da07ecb`  |
| 2215   | No file  | `e6155da07ecb`  |
| 2207   | No file  | `e6155da07ecb`  |
| 2203   | No file  | `e6155da07ecb`  |
| 2196   | No file  | `e6155da07ecb`  |
| 2192   | No file  | `e6155da07ecb`  |
| 2189   | No file  | `e6155da07ecb`  |
| 2183   | No file  | `e6155da07ecb`  |
| 2179   | No file  | `e6155da07ecb`  |
| 2171   | No file  | `e6155da07ecb`  |
| 2163   | No file  | `e6155da07ecb`  |
| 2156   | No file  | `e6155da07ecb`  |
| 2151   | No file  | `e6155da07ecb`  |
| 2147   | No file  | `e6155da07ecb`  |
| 2142   | No file  | `e6155da07ecb`  |
| 2138   | No file  | `e6155da07ecb`  |
| 2134   | No file  | `e6155da07ecb`  |
| 2130   | No file  | `e6155da07ecb`  |
| 2122   | No file  | `e6155da07ecb`  |
| 2107   | No file  | `e6155da07ecb`  |
| 2098   | No file  | `e6155da07ecb`  |
| 2089   | No file  | `e6155da07ecb`  |
| 2081   | No file  | `e6155da07ecb`  |
| 2073   | No file  | `e6155da07ecb`  |
| 2067   | No file  | `e6155da07ecb`  |
| 2063   | No file  | `e6155da07ecb`  |
| 2059   | No file  | `e6155da07ecb`  |
| 2052   | No file  | `e6155da07ecb`  |
| 2044   | No file  | `e6155da07ecb`  |
| 2039   | No file  | `e6155da07ecb`  |
| 2032   | No file  | `e6155da07ecb`  |
| 2025   | No file  | `e6155da07ecb`  |
| 2011   | No file  | `e6155da07ecb`  |
| 2005   | No file  | `e6155da07ecb`  |
| 2000   | No file  | `e6155da07ecb`  |
| 1996   | No file  | `e6155da07ecb`  |
| 1991   | No file  | `e6155da07ecb`  |
| 1985   | No file  | `e6155da07ecb`  |
| 1980   | No file  | `e6155da07ecb`  |
| 1969   | No file  | `e6155da07ecb`  |
| 1964   | No file  | `e6155da07ecb`  |
| 1958   | No file  | `e6155da07ecb`  |
| 1950   | No file  | `e6155da07ecb`  |
| 1945   | No file  | `e6155da07ecb`  |
| 1937   | No file  | `e6155da07ecb`  |
| 1933   | No file  | `e6155da07ecb`  |
| 1927   | No file  | `e6155da07ecb`  |
| 1921   | No file  | `e6155da07ecb`  |
| 1914   | No file  | `e6155da07ecb`  |
| 1908   | No file  | `e6155da07ecb`  |
| 1897   | No file  | `e6155da07ecb`  |
| 1892   | No file  | `e6155da07ecb`  |
| 1886   | No file  | `e6155da07ecb`  |
| 1881   | No file  | `e6155da07ecb`  |
| 1871   | No file  | `e6155da07ecb`  |
| 1866   | No file  | `e6155da07ecb`  |
| 1862   | No file  | `e6155da07ecb`  |
| 1854   | No file  | `e6155da07ecb`  |
| 1846   | No file  | `e6155da07ecb`  |
| 1838   | No file  | `e6155da07ecb`  |
| 1832   | No file  | `e6155da07ecb`  |
| 1826   | No file  | `e6155da07ecb`  |
| 1822   | No file  | `e6155da07ecb`  |
| 1818   | No file  | `e6155da07ecb`  |
| 1804   | No file  | `e6155da07ecb`  |
| 1794   | No file  | `e6155da07ecb`  |
| 1790   | No file  | `e6155da07ecb`  |
| 1784   | No file  | `e6155da07ecb`  |
| 1774   | No file  | `e6155da07ecb`  |
| 1771   | No file  | `e6155da07ecb`  |
| 1762   | No file  | `e6155da07ecb`  |
| 1759   | No file  | `e6155da07ecb`  |
| 1754   | No file  | `e6155da07ecb`  |
| 1749   | No file  | `e6155da07ecb`  |
| 1743   | No file  | `e6155da07ecb`  |
| 1737   | No file  | `e6155da07ecb`  |
| 1731   | No file  | `e6155da07ecb`  |
| 1725   | No file  | `e6155da07ecb`  |
| 1717   | No file  | `e6155da07ecb`  |
| 1710   | No file  | `e6155da07ecb`  |
| 1704   | No file  | `e6155da07ecb`  |
| 1698   | No file  | `e6155da07ecb`  |
| 1690   | No file  | `e6155da07ecb`  |
| 1685   | No file  | `e6155da07ecb`  |
| 1680   | No file  | `e6155da07ecb`  |
| 1674   | No file  | `e6155da07ecb`  |
| 1668   | No file  | `e6155da07ecb`  |
| 1659   | No file  | `e6155da07ecb`  |
| 1649   | No file  | `e6155da07ecb`  |
| 1642   | No file  | `e6155da07ecb`  |
| 1636   | No file  | `e6155da07ecb`  |
| 1628   | No file  | `e6155da07ecb`  |
| 1622   | No file  | `e6155da07ecb`  |
| 1614   | No file  | `e6155da07ecb`  |
| 1608   | No file  | `e6155da07ecb`  |
| 1602   | No file  | `e6155da07ecb`  |
| 1598   | No file  | `e6155da07ecb`  |
| 1594   | No file  | `e6155da07ecb`  |
| 1590   | No file  | `e6155da07ecb`  |
| 1587   | No file  | `e6155da07ecb`  |
| 1584   | No file  | `e6155da07ecb`  |
| 1579   | No file  | `e6155da07ecb`  |
| 1572   | No file  | `e6155da07ecb`  |
| 1565   | No file  | `e6155da07ecb`  |
| 1559   | No file  | `e6155da07ecb`  |
| 1554   | No file  | `e6155da07ecb`  |
| 1547   | No file  | `e6155da07ecb`  |
| 1537   | No file  | `e6155da07ecb`  |
| 1529   | No file  | `e6155da07ecb`  |
| 1524   | No file  | `e6155da07ecb`  |
| 1519   | No file  | `e6155da07ecb`  |
| 1509   | No file  | `e6155da07ecb`  |
| 1506   | No file  | `e6155da07ecb`  |
| 1504   | No file  | `e6155da07ecb`  |
| 1500   | No file  | `e6155da07ecb`  |
| 1493   | No file  | `e6155da07ecb`  |
| 1489   | No file  | `e6155da07ecb`  |
| 1485   | No file  | `e6155da07ecb`  |
| 1481   | No file  | `e6155da07ecb`  |
| 1474   | No file  | `e6155da07ecb`  |
| 1466   | No file  | `e6155da07ecb`  |
| 1462   | No file  | `e6155da07ecb`  |
| 1459   | No file  | `e6155da07ecb`  |
| 1453   | No file  | `e6155da07ecb`  |
| 1450   | No file  | `e6155da07ecb`  |
| 1445   | No file  | `e6155da07ecb`  |
| 1439   | No file  | `e6155da07ecb`  |
| 1433   | No file  | `e6155da07ecb`  |
| 1430   | No file  | `e6155da07ecb`  |
| 1426   | No file  | `e6155da07ecb`  |
| 1421   | No file  | `e6155da07ecb`  |
| 1417   | No file  | `e6155da07ecb`  |
| 1416   | No file  | `e6155da07ecb`  |
| 1409   | No file  | `e6155da07ecb`  |
| 1405   | No file  | `e6155da07ecb`  |
| 1401   | No file  | `e6155da07ecb`  |
| 1396   | No file  | `e6155da07ecb`  |
| 1391   | No file  | `e6155da07ecb`  |
| 1390   | No file  | `e6155da07ecb`  |
| 1386   | No file  | `e6155da07ecb`  |
| 1381   | No file  | `e6155da07ecb`  |
| 1379   | No file  | `e6155da07ecb`  |
| 1372   | No file  | `e6155da07ecb`  |
| 1366   | No file  | `e6155da07ecb`  |
| 1364   | No file  | `e6155da07ecb`  |
| 1363   | No file  | `e6155da07ecb`  |
| 1360   | No file  | `e6155da07ecb`  |
| 1358   | No file  | `e6155da07ecb`  |
| 1355   | No file  | `e6155da07ecb`  |
| 1351   | No file  | `e6155da07ecb`  |
| 1348   | No file  | `e6155da07ecb`  |
| 1346   | No file  | `e6155da07ecb`  |
| 1341   | No file  | `e6155da07ecb`  |
| 1340   | No file  | `e6155da07ecb`  |
| 1338   | No file  | `e6155da07ecb`  |
| 1335   | No file  | `e6155da07ecb`  |
| 1333   | No file  | `e6155da07ecb`  |
| 1329   | No file  | `e6155da07ecb`  |
| 1327   | No file  | `e6155da07ecb`  |
| 1324   | No file  | `e6155da07ecb`  |
| 1321   | No file  | `e6155da07ecb`  |
| 1319   | No file  | `e6155da07ecb`  |
| 1318   | No file  | `e6155da07ecb`  |
| 1316   | No file  | `e6155da07ecb`  |
| 1313   | No file  | `e6155da07ecb`  |
| 1311   | No file  | `e6155da07ecb`  |
| 1309   | No file  | `e6155da07ecb`  |
| 1304   | No file  | `e6155da07ecb`  |
| 1292   | No file  | `e6155da07ecb`  |
| 1286   | No file  | `e6155da07ecb`  |
| 1280   | No file  | `e6155da07ecb`  |
| 1276   | No file  | `e6155da07ecb`  |
| 1267   | No file  | `e6155da07ecb`  |
| 1261   | No file  | `e6155da07ecb`  |
| 1256   | No file  | `e6155da07ecb`  |
| 1250   | No file  | `e6155da07ecb`  |
| 1246   | No file  | `e6155da07ecb`  |
| 1239   | No file  | `e6155da07ecb`  |
| 1230   | No file  | `e6155da07ecb`  |
| 1226   | No file  | `e6155da07ecb`  |
| 1220   | No file  | `e6155da07ecb`  |
| 1217   | No file  | `e6155da07ecb`  |
| 1211   | No file  | `e6155da07ecb`  |
| 1210   | No file  | `e6155da07ecb`  |
| 1208   | No file  | `e6155da07ecb`  |
| 1203   | No file  | `e6155da07ecb`  |
| 1197   | No file  | `e6155da07ecb`  |
| 1194   | No file  | `e6155da07ecb`  |
| 1192   | No file  | `e6155da07ecb`  |
| 1187   | No file  | `e6155da07ecb`  |
| 1183   | No file  | `e6155da07ecb`  |
| 1177   | No file  | `e6155da07ecb`  |
| 1173   | No file  | `e6155da07ecb`  |
| 1167   | No file  | `e6155da07ecb`  |
| 1164   | No file  | `e6155da07ecb`  |
| 1156   | No file  | `e6155da07ecb`  |
| 1149   | No file  | `e6155da07ecb`  |
| 1144   | No file  | `e6155da07ecb`  |
| 1137   | No file  | `e6155da07ecb`  |
| 1132   | No file  | `e6155da07ecb`  |
| 1127   | No file  | `e6155da07ecb`  |
| 1122   | No file  | `e6155da07ecb`  |
| 1118   | No file  | `e6155da07ecb`  |
| 1114   | No file  | `e6155da07ecb`  |
| 1109   | No file  | `e6155da07ecb`  |
| 1102   | No file  | `e6155da07ecb`  |
| 1096   | No file  | `e6155da07ecb`  |
| 1088   | No file  | `e6155da07ecb`  |
| 1081   | No file  | `e6155da07ecb`  |
| 1076   | No file  | `e6155da07ecb`  |
| 1069   | No file  | `e6155da07ecb`  |
| 1064   | No file  | `e6155da07ecb`  |
| 1058   | No file  | `e6155da07ecb`  |
| 1051   | No file  | `e6155da07ecb`  |
| 1044   | No file  | `e6155da07ecb`  |
| 1036   | No file  | `e6155da07ecb`  |
| 1026   | No file  | `e6155da07ecb`  |
| 1016   | No file  | `e6155da07ecb`  |
| 1009   | No file  | `e6155da07ecb`  |
| 1005   | No file  | `e6155da07ecb`  |
| 1000   | No file  | `e6155da07ecb`  |
| 998    | No file  | `e6155da07ecb`  |
| 990    | No file  | `e6155da07ecb`  |
| 979    | No file  | `e6155da07ecb`  |
| 972    | No file  | `e6155da07ecb`  |
| 963    | No file  | `e6155da07ecb`  |
| 955    | No file  | `e6155da07ecb`  |
| 946    | No file  | `e6155da07ecb`  |
| 938    | No file  | `e6155da07ecb`  |
| 927    | No file  | `e6155da07ecb`  |
| 911    | No file  | `e6155da07ecb`  |
| 904    | No file  | `e6155da07ecb`  |
| 899    | No file  | `e6155da07ecb`  |
| 894    | No file  | `e6155da07ecb`  |
| 885    | No file  | `e6155da07ecb`  |
| 879    | No file  | `e6155da07ecb`  |
| 872    | No file  | `e6155da07ecb`  |
| 864    | No file  | `e6155da07ecb`  |
| 855    | No file  | `e6155da07ecb`  |
| 853    | No file  | `e6155da07ecb`  |
| 845    | No file  | `e6155da07ecb`  |
| 837    | No file  | `e6155da07ecb`  |
| 829    | No file  | `e6155da07ecb`  |
| 822    | No file  | `e6155da07ecb`  |
| 814    | No file  | `e6155da07ecb`  |
| 805    | No file  | `e6155da07ecb`  |
| 794    | No file  | `e6155da07ecb`  |
| 787    | No file  | `e6155da07ecb`  |
| 780    | No file  | `e6155da07ecb`  |
| 771    | No file  | `e6155da07ecb`  |
| 760    | No file  | `e6155da07ecb`  |
| 748    | No file  | `e6155da07ecb`  |
| 741    | No file  | `e6155da07ecb`  |
| 736    | No file  | `e6155da07ecb`  |
| 731    | No file  | `e6155da07ecb`  |
| 723    | No file  | `e6155da07ecb`  |
| 711    | No file  | `e6155da07ecb`  |
| 707    | No file  | `e6155da07ecb`  |
| 697    | No file  | `e6155da07ecb`  |
| 689    | No file  | `e6155da07ecb`  |
| 683    | No file  | `e6155da07ecb`  |
| 678    | No file  | `e6155da07ecb`  |
| 670    | No file  | `e6155da07ecb`  |
| 661    | No file  | `e6155da07ecb`  |
| 656    | No file  | `e6155da07ecb`  |
| 652    | No file  | `e6155da07ecb`  |
| 643    | No file  | `e6155da07ecb`  |
| 637    | No file  | `e6155da07ecb`  |
| 630    | No file  | `e6155da07ecb`  |
| 627    | No file  | `e6155da07ecb`  |
| 621    | No file  | `e6155da07ecb`  |
| 617    | No file  | `e6155da07ecb`  |
| 615    | No file  | `e6155da07ecb`  |
| 606    | No file  | `e6155da07ecb`  |
| 599    | No file  | `e6155da07ecb`  |
| 592    | No file  | `e6155da07ecb`  |
| 586    | No file  | `e6155da07ecb`  |
| 577    | No file  | `e6155da07ecb`  |
| 569    | No file  | `e6155da07ecb`  |
| 561    | No file  | `e6155da07ecb`  |
| 554    | No file  | `e6155da07ecb`  |
| 542    | No file  | `e6155da07ecb`  |
| 532    | No file  | `e6155da07ecb`  |
| 531    | No file  | `e6155da07ecb`  |
| 526    | No file  | `e6155da07ecb`  |
| 521    | No file  | `e6155da07ecb`  |
| 517    | No file  | `e6155da07ecb`  |
| 510    | No file  | `e6155da07ecb`  |
| 508    | No file  | `e6155da07ecb`  |
| 504    | No file  | `e6155da07ecb`  |
| 497    | No file  | `e6155da07ecb`  |
| 491    | No file  | `e6155da07ecb`  |
| 485    | No file  | `e6155da07ecb`  |
| 478    | No file  | `e6155da07ecb`  |
| 472    | No file  | `e6155da07ecb`  |
| 466    | No file  | `e6155da07ecb`  |
| 457    | No file  | `e6155da07ecb`  |
| 452    | No file  | `e6155da07ecb`  |
| 449    | No file  | `e6155da07ecb`  |
| 435    | No file  | `e6155da07ecb`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Character names (LOC type 6), skill names (type 10) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (16 bytes)

| Offset  | Type | Field                    | Notes                                                                                   |
| ------- | ---- | ------------------------ | --------------------------------------------------------------------------------------- |
| `+0x00` | u16  | fierce_battle_key        | Sanctum key, `1` to `22` on client 3474                                                 |
| `+0x02` | u16  | kamasylvia_character_key | Kamasylvia's guardian character (Urugon, Old Mirumok, Fadus Archer); `0` on the gimmick rows |
| `+0x04` | u16  | odyllita_character_key   | O'dyllita's guardian character (Ahib Dark Champion, Turo Berserker, Khalk); `0` on the gimmick rows |
| `+0x06` | u16  | neutral_character_key    | Neutral character: Faded Relic on the 20 sanctums, Mysterious Statue on the gimmick rows |
| `+0x08` | u8   | unknown_08               | `0` on keys `1` to `20`, `1` on the gimmick rows                                        |
| `+0x09` | u16  | skill_no                 | `skill.dbss` skill number of the sanctum buff, `62814` to `62828`                        |
| `+0x0B` | u32  | name_ref                 | String table index of the Korean sanctum name                                           |
| `+0x0F` | u8   | unknown_0f               | `0` on keys `1` to `20`, `1` on key `21`, `2` on key `22`                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                  |
| ------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `22` on client 3474, one per row    |
| `+0x04` | pstr[string_count] | strings      | Wide Korean names in row order (`오네트 제1성소`)      |

## Sanctums

Client 3474. The skill names are LOC type 10, which names these buffs by
their effect.

| Keys        | Korean names                          | Guardians (Kamasylvia, O'dyllita)                    | Skills            |
| ----------- | ------------------------------------- | ---------------------------------------------------- | ----------------- |
| `1` to `10` | `오네트 제1성소` to `오네트 제10성소` | Urugon, Ronin, Narc Brishka, Griffon, Old Mirumok, Fadus Archer, Shaman and Warrior; Ahib Salun Wolf Spearmaiden, Ahib Salun Bear Spearmaiden, Ahib Dark Champion | `62814` to `62820` |
| `11` to `20`| `오도어 제1성소` to `오도어 제10성소` | Fadus Archer, Shaman and Warrior; Olun's Golem, Ulutuka, Dark Knight, Khalk, Turo Berserker and the three Ahib | `62821` to `62827` |
| `21`        | `정령의 제단`                         | none; Mysterious Statue `21699`                       | `62828` Spirit's Blessing |
| `22`        | `해양 성소`                           | none; Mysterious Statue `21700`                       | `62828` Spirit's Blessing |

Keys `8` to `10` repeat the skills of `5` to `7`, and `18` to `20` those of
`15` to `17`.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it; the names come from the
client Lua and the companion tables:

- `fierce_battle_key`: the Lua reads a sanctum with
  `ToClient_GetRoseWarFierceBattleObjectInfoWrapper(fierceBattleKey)` and
  loops keys `1` to `20` in the revive window (`panel_rosewar_deadmessage.luac`).
- The three character keys: [`rosewarnodemonsterinfostaicstatus.bss`](rosewarnodemonsterinfostaicstatus_bss.md)
  gives every character a tooltip image. The `+0x02` characters have
  `ElfWar_Kama_*` tooltips, the `+0x04` characters `ElfWar_Odyl_*` ones and
  the `+0x06` characters `ElfWar_Kama_Neutral_Tooltip` or
  `ElfWar_Odyl_Neutral_Tooltip` (`__eRoseWarTeam_Neutral` in the Lua).
- `skill_no`: `ToClient_GetRoseWarFierceBattleObjectSkillNo(fierceBattleKeyRaw)`
  feeds `getSkillStaticStatus(skillNo, 1)` for the sanctum tooltip's buff
  lines (`panel_rosewar_minimap_5.luac`).
- `name_ref`: the Lua shows `fierceBattleStaticStatusWrapper:getName()`;
  the strings are one Korean sanctum name per row.

## Notes

- The file is the same on clients 3002, 3251 and 3474, 828 bytes. It is
  not in the archives of client 1784.
- [`rosewarfiercebattlenodestaticstatus.bss`](rosewarfiercebattlenodestaticstatus_bss.md)
  links the sanctums, and the sanctum revive points of
  [`rosewarrevivepositionstaticstatus.bss`](rosewarrevivepositionstaticstatus_bss.md)
  use the same keys.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  the key and the Korean name first.

## Open Questions

### The Two Gimmick Flags

`unknown_08` is `1` and `unknown_0f` `1` or `2` on the two gimmick rows
only. The radar Lua (`radar.luac`, client 3474) has two gimmick sanctum
icons, `radarType_RoseWarGimicAdrenalinFierceBattle` and
`radarType_RoseWarGimicConquestFierceBattle`, and the war log has
`_Occupy_GimicAdrenalinFierceBattle` and `_Occupy_GimicConquestFierceBattle`,
which reads as `unknown_0f` holding the gimmick kind, but no Lua ties a
value to either name.
