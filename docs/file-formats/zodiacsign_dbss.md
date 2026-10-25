# `zodiacsign.dbss` Format

## Purpose

Defines the 12 BDO horoscope (zodiac) signs. Each record stores star-position coordinates, constellation-edge pairs, a Korean constellation name and personality-trait text, and two texture-asset paths.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                    | Bytes | Records       | Row bytes                  |
| ------ | -------------- | ----------------------- | ----- | ------------- | -------------------------- |
| 1      | 1346 and later | `zodiacsign.dbss`       | 4,810 | 12 Record     | 360 to 434, 400 on average |
| 1      | 1346 and later | `zodiacsignoffset.dbss` | 112   | 12 Offset Row | 9                          |

| Layout | File                    | Known           | Unknown      |
| ------ | ----------------------- | --------------- | ------------ |
| 1      | `zodiacsign.dbss`       | 4,702 B (97.8%) | 108 B (2.2%) |
| 1      | `zodiacsignoffset.dbss` | 112 B (100.0%)  | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `75c0007d032f`  |
| 3482   | Layout 1             | `75c0007d032f`  |
| 3474   | Layout 1             | `75c0007d032f`  |
| 3473   | Layout 1             | `75c0007d032f`  |
| 3464   | Layout 1             | `75c0007d032f`  |
| 3458   | Layout 1             | `75c0007d032f`  |
| 3454   | Layout 1             | `75c0007d032f`  |
| 3444   | Layout 1             | `75c0007d032f`  |
| 3435   | Layout 1             | `75c0007d032f`  |
| 3426   | Layout 1             | `75c0007d032f`  |
| 3418   | Layout 1             | `75c0007d032f`  |
| 3412   | Layout 1             | `75c0007d032f`  |
| 3402   | Layout 1             | `75c0007d032f`  |
| 3396   | Layout 1             | `75c0007d032f`  |
| 3387   | Layout 1             | `75c0007d032f`  |
| 3381   | Layout 1             | `75c0007d032f`  |
| 3373   | Layout 1             | `75c0007d032f`  |
| 3364   | Layout 1             | `75c0007d032f`  |
| 3356   | Layout 1             | `75c0007d032f`  |
| 3349   | Layout 1             | `75c0007d032f`  |
| 3342   | Layout 1             | `75c0007d032f`  |
| 3335   | Layout 1             | `75c0007d032f`  |
| 3326   | Layout 1             | `75c0007d032f`  |
| 3321   | Layout 1             | `75c0007d032f`  |
| 3314   | Layout 1             | `75c0007d032f`  |
| 3303   | Layout 1             | `75c0007d032f`  |
| 3302   | Layout 1             | `75c0007d032f`  |
| 3293   | Layout 1             | `75c0007d032f`  |
| 3283   | Layout 1             | `75c0007d032f`  |
| 3275   | Layout 1             | `75c0007d032f`  |
| 3267   | Layout 1             | `75c0007d032f`  |
| 3258   | Layout 1             | `75c0007d032f`  |
| 3251   | Layout 1             | `75c0007d032f`  |
| 3242   | Layout 1             | `75c0007d032f`  |
| 3235   | Layout 1             | `75c0007d032f`  |
| 3229   | Layout 1             | `75c0007d032f`  |
| 3212   | Layout 1             | `75c0007d032f`  |
| 3203   | Layout 1             | `75c0007d032f`  |
| 3193   | Layout 1             | `75c0007d032f`  |
| 3186   | Layout 1             | `75c0007d032f`  |
| 3177   | Layout 1             | `75c0007d032f`  |
| 3169   | Layout 1             | `75c0007d032f`  |
| 3158   | Layout 1             | `75c0007d032f`  |
| 3151   | Layout 1             | `75c0007d032f`  |
| 3144   | Layout 1             | `75c0007d032f`  |
| 3133   | Layout 1             | `75c0007d032f`  |
| 3125   | Layout 1             | `75c0007d032f`  |
| 3118   | Layout 1             | `75c0007d032f`  |
| 3111   | Layout 1             | `75c0007d032f`  |
| 3103   | Layout 1             | `75c0007d032f`  |
| 3095   | Layout 1             | `75c0007d032f`  |
| 3086   | Layout 1             | `75c0007d032f`  |
| 3072   | Layout 1             | `75c0007d032f`  |
| 3062   | Layout 1             | `75c0007d032f`  |
| 3052   | Layout 1             | `75c0007d032f`  |
| 3045   | Layout 1             | `75c0007d032f`  |
| 3037   | Layout 1             | `75c0007d032f`  |
| 3030   | Layout 1             | `75c0007d032f`  |
| 3021   | Layout 1             | `75c0007d032f`  |
| 3012   | Layout 1             | `75c0007d032f`  |
| 3002   | Layout 1             | `75c0007d032f`  |
| 2995   | Layout 1             | `75c0007d032f`  |
| 2987   | Layout 1             | `75c0007d032f`  |
| 2978   | Layout 1             | `75c0007d032f`  |
| 2970   | Layout 1             | `75c0007d032f`  |
| 2959   | Layout 1             | `75c0007d032f`  |
| 2951   | Layout 1             | `75c0007d032f`  |
| 2942   | Layout 1             | `75c0007d032f`  |
| 2935   | Layout 1             | `75c0007d032f`  |
| 2932   | Layout 1             | `75c0007d032f`  |
| 2923   | Layout 1             | `75c0007d032f`  |
| 2919   | Layout 1             | `75c0007d032f`  |
| 2907   | Layout 1             | `75c0007d032f`  |
| 2900   | Layout 1             | `75c0007d032f`  |
| 2891   | Layout 1             | `75c0007d032f`  |
| 2882   | Layout 1             | `75c0007d032f`  |
| 2872   | Layout 1             | `75c0007d032f`  |
| 2863   | Layout 1             | `75c0007d032f`  |
| 2855   | Layout 1             | `75c0007d032f`  |
| 2849   | Layout 1             | `75c0007d032f`  |
| 2844   | Layout 1             | `75c0007d032f`  |
| 2834   | Layout 1             | `75c0007d032f`  |
| 2825   | Layout 1             | `75c0007d032f`  |
| 2819   | Layout 1             | `75c0007d032f`  |
| 2811   | Layout 1             | `75c0007d032f`  |
| 2803   | Layout 1             | `75c0007d032f`  |
| 2794   | Layout 1             | `75c0007d032f`  |
| 2783   | Layout 1             | `75c0007d032f`  |
| 2774   | Layout 1             | `75c0007d032f`  |
| 2765   | Layout 1             | `75c0007d032f`  |
| 2756   | Layout 1             | `75c0007d032f`  |
| 2750   | Layout 1             | `75c0007d032f`  |
| 2743   | Layout 1             | `75c0007d032f`  |
| 2736   | Layout 1             | `75c0007d032f`  |
| 2726   | Layout 1             | `75c0007d032f`  |
| 2717   | Layout 1             | `75c0007d032f`  |
| 2709   | Layout 1             | `75c0007d032f`  |
| 2703   | Layout 1             | `75c0007d032f`  |
| 2695   | Layout 1             | `75c0007d032f`  |
| 2684   | Layout 1             | `75c0007d032f`  |
| 2672   | Layout 1             | `75c0007d032f`  |
| 2665   | Layout 1             | `75c0007d032f`  |
| 2657   | Layout 1             | `75c0007d032f`  |
| 2649   | Layout 1             | `75c0007d032f`  |
| 2644   | Layout 1             | `75c0007d032f`  |
| 2637   | Layout 1             | `75c0007d032f`  |
| 2629   | Layout 1             | `75c0007d032f`  |
| 2619   | Layout 1             | `75c0007d032f`  |
| 2612   | Layout 1             | `75c0007d032f`  |
| 2606   | Layout 1             | `75c0007d032f`  |
| 2602   | Layout 1             | `75c0007d032f`  |
| 2601   | Layout 1             | `75c0007d032f`  |
| 2592   | Layout 1             | `75c0007d032f`  |
| 2583   | Layout 1             | `75c0007d032f`  |
| 2575   | Layout 1             | `75c0007d032f`  |
| 2567   | Layout 1             | `75c0007d032f`  |
| 2560   | Layout 1             | `75c0007d032f`  |
| 2553   | Layout 1             | `75c0007d032f`  |
| 2545   | Layout 1             | `75c0007d032f`  |
| 2538   | Layout 1             | `75c0007d032f`  |
| 2529   | Layout 1             | `75c0007d032f`  |
| 2519   | Layout 1             | `75c0007d032f`  |
| 2513   | Layout 1             | `75c0007d032f`  |
| 2510   | Layout 1             | `75c0007d032f`  |
| 2507   | Layout 1             | `75c0007d032f`  |
| 2503   | Layout 1             | `75c0007d032f`  |
| 2498   | Layout 1             | `75c0007d032f`  |
| 2492   | Layout 1             | `75c0007d032f`  |
| 2487   | Layout 1             | `75c0007d032f`  |
| 2480   | Layout 1             | `75c0007d032f`  |
| 2474   | Layout 1             | `75c0007d032f`  |
| 2468   | Layout 1             | `75c0007d032f`  |
| 2460   | Layout 1             | `75c0007d032f`  |
| 2453   | Layout 1             | `75c0007d032f`  |
| 2444   | Layout 1             | `75c0007d032f`  |
| 2438   | Layout 1             | `75c0007d032f`  |
| 2434   | Layout 1             | `75c0007d032f`  |
| 2429   | Layout 1             | `75c0007d032f`  |
| 2421   | Layout 1             | `75c0007d032f`  |
| 2414   | Layout 1             | `75c0007d032f`  |
| 2407   | Layout 1             | `75c0007d032f`  |
| 2401   | Layout 1             | `75c0007d032f`  |
| 2397   | Layout 1             | `75c0007d032f`  |
| 2393   | Layout 1             | `75c0007d032f`  |
| 2384   | Layout 1             | `75c0007d032f`  |
| 2378   | Layout 1             | `75c0007d032f`  |
| 2372   | Layout 1             | `75c0007d032f`  |
| 2358   | Layout 1             | `75c0007d032f`  |
| 2352   | Layout 1             | `75c0007d032f`  |
| 2347   | Layout 1             | `75c0007d032f`  |
| 2343   | Layout 1             | `75c0007d032f`  |
| 2335   | Layout 1             | `75c0007d032f`  |
| 2327   | Layout 1             | `75c0007d032f`  |
| 2324   | Layout 1             | `75c0007d032f`  |
| 2319   | Layout 1             | `75c0007d032f`  |
| 2313   | Layout 1             | `75c0007d032f`  |
| 2308   | Layout 1             | `75c0007d032f`  |
| 2302   | Layout 1             | `75c0007d032f`  |
| 2295   | Layout 1             | `75c0007d032f`  |
| 2290   | Layout 1             | `75c0007d032f`  |
| 2284   | Layout 1             | `75c0007d032f`  |
| 2276   | Layout 1             | `75c0007d032f`  |
| 2269   | Layout 1             | `75c0007d032f`  |
| 2259   | Layout 1             | `75c0007d032f`  |
| 2250   | Layout 1             | `75c0007d032f`  |
| 2243   | Layout 1             | `75c0007d032f`  |
| 2235   | Layout 1             | `75c0007d032f`  |
| 2229   | Layout 1             | `75c0007d032f`  |
| 2224   | Layout 1             | `75c0007d032f`  |
| 2218   | Layout 1             | `75c0007d032f`  |
| 2215   | Layout 1             | `75c0007d032f`  |
| 2207   | Layout 1             | `75c0007d032f`  |
| 2203   | Layout 1             | `75c0007d032f`  |
| 2196   | Layout 1             | `75c0007d032f`  |
| 2192   | Layout 1             | `75c0007d032f`  |
| 2189   | Layout 1             | `75c0007d032f`  |
| 2183   | Layout 1             | `75c0007d032f`  |
| 2179   | Layout 1             | `75c0007d032f`  |
| 2171   | Layout 1             | `75c0007d032f`  |
| 2163   | Layout 1             | `75c0007d032f`  |
| 2156   | Layout 1             | `75c0007d032f`  |
| 2151   | Layout 1             | `75c0007d032f`  |
| 2147   | Layout 1             | `75c0007d032f`  |
| 2142   | Layout 1             | `75c0007d032f`  |
| 2138   | Layout 1             | `75c0007d032f`  |
| 2134   | Layout 1             | `75c0007d032f`  |
| 2130   | Layout 1             | `75c0007d032f`  |
| 2122   | Layout 1             | `75c0007d032f`  |
| 2107   | Layout 1             | `75c0007d032f`  |
| 2098   | Layout 1             | `75c0007d032f`  |
| 2089   | Layout 1             | `75c0007d032f`  |
| 2081   | Layout 1             | `75c0007d032f`  |
| 2073   | Layout 1             | `75c0007d032f`  |
| 2067   | Layout 1             | `75c0007d032f`  |
| 2063   | Layout 1             | `75c0007d032f`  |
| 2059   | Layout 1             | `75c0007d032f`  |
| 2052   | Layout 1             | `75c0007d032f`  |
| 2044   | Layout 1             | `75c0007d032f`  |
| 2039   | Layout 1             | `75c0007d032f`  |
| 2032   | Layout 1             | `75c0007d032f`  |
| 2025   | Layout 1             | `75c0007d032f`  |
| 2011   | Layout 1             | `75c0007d032f`  |
| 2005   | Layout 1             | `75c0007d032f`  |
| 2000   | Layout 1             | `75c0007d032f`  |
| 1996   | Layout 1             | `75c0007d032f`  |
| 1991   | Layout 1             | `75c0007d032f`  |
| 1985   | Layout 1             | `75c0007d032f`  |
| 1980   | Layout 1             | `75c0007d032f`  |
| 1969   | Layout 1             | `75c0007d032f`  |
| 1964   | Layout 1             | `75c0007d032f`  |
| 1958   | Layout 1             | `75c0007d032f`  |
| 1950   | Layout 1             | `75c0007d032f`  |
| 1945   | Layout 1             | `75c0007d032f`  |
| 1937   | Layout 1             | `75c0007d032f`  |
| 1933   | Layout 1             | `75c0007d032f`  |
| 1927   | Layout 1             | `75c0007d032f`  |
| 1921   | Layout 1             | `75c0007d032f`  |
| 1914   | Layout 1             | `75c0007d032f`  |
| 1908   | Layout 1             | `75c0007d032f`  |
| 1897   | Layout 1             | `75c0007d032f`  |
| 1892   | Layout 1             | `75c0007d032f`  |
| 1886   | Layout 1             | `75c0007d032f`  |
| 1881   | Layout 1             | `75c0007d032f`  |
| 1871   | Layout 1             | `75c0007d032f`  |
| 1866   | Layout 1             | `75c0007d032f`  |
| 1862   | Layout 1             | `75c0007d032f`  |
| 1854   | Layout 1             | `75c0007d032f`  |
| 1846   | Layout 1             | `75c0007d032f`  |
| 1838   | Layout 1             | `75c0007d032f`  |
| 1832   | Layout 1             | `75c0007d032f`  |
| 1826   | Layout 1             | `75c0007d032f`  |
| 1822   | Layout 1             | `75c0007d032f`  |
| 1818   | Layout 1             | `75c0007d032f`  |
| 1804   | Layout 1             | `75c0007d032f`  |
| 1794   | Layout 1             | `75c0007d032f`  |
| 1790   | Layout 1             | `75c0007d032f`  |
| 1784   | Layout 1             | `75c0007d032f`  |
| 1774   | Layout 1             | `75c0007d032f`  |
| 1771   | Layout 1             | `75c0007d032f`  |
| 1762   | Layout 1             | `75c0007d032f`  |
| 1759   | Layout 1             | `75c0007d032f`  |
| 1754   | Layout 1             | `75c0007d032f`  |
| 1749   | Layout 1             | `75c0007d032f`  |
| 1743   | Layout 1             | `75c0007d032f`  |
| 1737   | Layout 1             | `75c0007d032f`  |
| 1731   | Layout 1             | `75c0007d032f`  |
| 1725   | Layout 1             | `75c0007d032f`  |
| 1717   | Layout 1             | `75c0007d032f`  |
| 1710   | Layout 1             | `75c0007d032f`  |
| 1704   | Layout 1             | `75c0007d032f`  |
| 1698   | Layout 1             | `75c0007d032f`  |
| 1690   | Layout 1             | `75c0007d032f`  |
| 1685   | Layout 1             | `75c0007d032f`  |
| 1680   | Layout 1             | `75c0007d032f`  |
| 1674   | Layout 1             | `75c0007d032f`  |
| 1668   | Layout 1             | `75c0007d032f`  |
| 1659   | Layout 1             | `75c0007d032f`  |
| 1649   | Layout 1             | `75c0007d032f`  |
| 1642   | Layout 1             | `75c0007d032f`  |
| 1636   | Layout 1             | `75c0007d032f`  |
| 1628   | Layout 1             | `75c0007d032f`  |
| 1622   | Layout 1             | `75c0007d032f`  |
| 1614   | Layout 1             | `75c0007d032f`  |
| 1608   | Layout 1             | `75c0007d032f`  |
| 1602   | Layout 1             | `75c0007d032f`  |
| 1598   | Layout 1             | `75c0007d032f`  |
| 1594   | Layout 1             | `75c0007d032f`  |
| 1590   | Layout 1             | `75c0007d032f`  |
| 1587   | Layout 1             | `75c0007d032f`  |
| 1584   | Layout 1             | `75c0007d032f`  |
| 1579   | Layout 1             | `75c0007d032f`  |
| 1572   | Layout 1             | `75c0007d032f`  |
| 1565   | Layout 1             | `75c0007d032f`  |
| 1559   | Layout 1             | `75c0007d032f`  |
| 1554   | Layout 1             | `75c0007d032f`  |
| 1547   | Layout 1             | `75c0007d032f`  |
| 1537   | Layout 1             | `75c0007d032f`  |
| 1529   | Layout 1             | `75c0007d032f`  |
| 1524   | Layout 1             | `75c0007d032f`  |
| 1519   | Layout 1             | `75c0007d032f`  |
| 1509   | Layout 1             | `75c0007d032f`  |
| 1506   | Layout 1             | `75c0007d032f`  |
| 1504   | Layout 1             | `75c0007d032f`  |
| 1500   | Layout 1             | `75c0007d032f`  |
| 1493   | Layout 1             | `75c0007d032f`  |
| 1489   | Layout 1             | `75c0007d032f`  |
| 1485   | Layout 1             | `75c0007d032f`  |
| 1481   | Layout 1             | `75c0007d032f`  |
| 1474   | Layout 1             | `75c0007d032f`  |
| 1466   | Layout 1             | `75c0007d032f`  |
| 1462   | Layout 1             | `75c0007d032f`  |
| 1459   | Layout 1             | `75c0007d032f`  |
| 1453   | Layout 1             | `75c0007d032f`  |
| 1450   | Layout 1             | `75c0007d032f`  |
| 1445   | Layout 1             | `75c0007d032f`  |
| 1439   | Layout 1             | `75c0007d032f`  |
| 1433   | Layout 1             | `75c0007d032f`  |
| 1430   | Layout 1             | `75c0007d032f`  |
| 1426   | Layout 1             | `75c0007d032f`  |
| 1421   | Layout 1             | `75c0007d032f`  |
| 1417   | Layout 1             | `75c0007d032f`  |
| 1416   | Layout 1             | `75c0007d032f`  |
| 1409   | Layout 1             | `75c0007d032f`  |
| 1405   | Layout 1             | `75c0007d032f`  |
| 1401   | Layout 1             | `75c0007d032f`  |
| 1396   | Layout 1             | `75c0007d032f`  |
| 1391   | Layout 1             | `75c0007d032f`  |
| 1390   | Layout 1             | `75c0007d032f`  |
| 1386   | Layout 1             | `75c0007d032f`  |
| 1381   | Layout 1             | `75c0007d032f`  |
| 1379   | Layout 1             | `75c0007d032f`  |
| 1372   | Layout 1             | `75c0007d032f`  |
| 1366   | Layout 1             | `75c0007d032f`  |
| 1364   | Layout 1             | `75c0007d032f`  |
| 1363   | Layout 1             | `75c0007d032f`  |
| 1360   | Layout 1             | `75c0007d032f`  |
| 1358   | Layout 1             | `75c0007d032f`  |
| 1355   | Layout 1             | `75c0007d032f`  |
| 1351   | Layout 1             | `75c0007d032f`  |
| 1348   | Layout 1             | `75c0007d032f`  |
| 1346   | Layout 1             | `75c0007d032f`  |
| 1341   | No documented layout | `75c0007d032f`  |
| 1340   | No documented layout | `75c0007d032f`  |
| 1338   | No documented layout | `75c0007d032f`  |
| 1335   | No documented layout | `75c0007d032f`  |
| 1333   | No documented layout | `75c0007d032f`  |
| 1329   | No documented layout | `75c0007d032f`  |
| 1327   | No documented layout | `75c0007d032f`  |
| 1324   | No documented layout | `75c0007d032f`  |
| 1321   | No documented layout | `75c0007d032f`  |
| 1319   | No documented layout | `75c0007d032f`  |
| 1318   | No documented layout | `75c0007d032f`  |
| 1316   | No documented layout | `75c0007d032f`  |
| 1313   | No documented layout | `75c0007d032f`  |
| 1311   | No documented layout | `75c0007d032f`  |
| 1309   | No documented layout | `75c0007d032f`  |
| 1304   | No documented layout | `75c0007d032f`  |
| 1292   | No documented layout | `75c0007d032f`  |
| 1286   | No documented layout | `75c0007d032f`  |
| 1280   | No documented layout | `75c0007d032f`  |
| 1276   | No documented layout | `75c0007d032f`  |
| 1267   | No documented layout | `75c0007d032f`  |
| 1261   | No documented layout | `75c0007d032f`  |
| 1256   | No documented layout | `75c0007d032f`  |
| 1250   | No documented layout | `75c0007d032f`  |
| 1246   | No file              | `75c0007d032f`  |
| 1239   | No file              | `75c0007d032f`  |
| 1230   | No file              | `75c0007d032f`  |
| 1226   | No file              | `75c0007d032f`  |
| 1220   | No file              | `75c0007d032f`  |
| 1217   | No file              | `75c0007d032f`  |
| 1211   | No file              | `75c0007d032f`  |
| 1210   | No file              | `75c0007d032f`  |
| 1208   | No file              | `75c0007d032f`  |
| 1203   | No file              | `75c0007d032f`  |
| 1197   | No file              | `75c0007d032f`  |
| 1194   | No file              | `75c0007d032f`  |
| 1192   | No file              | `75c0007d032f`  |
| 1187   | No file              | `75c0007d032f`  |
| 1183   | No file              | `75c0007d032f`  |
| 1177   | No file              | `75c0007d032f`  |
| 1173   | No file              | `75c0007d032f`  |
| 1167   | No file              | `75c0007d032f`  |
| 1164   | No file              | `75c0007d032f`  |
| 1156   | No file              | `75c0007d032f`  |
| 1149   | No file              | `75c0007d032f`  |
| 1144   | No file              | `75c0007d032f`  |
| 1137   | No file              | `75c0007d032f`  |
| 1132   | No file              | `75c0007d032f`  |
| 1127   | No file              | `75c0007d032f`  |
| 1122   | No file              | `75c0007d032f`  |
| 1118   | No file              | `75c0007d032f`  |
| 1114   | No file              | `75c0007d032f`  |
| 1109   | No file              | `75c0007d032f`  |
| 1102   | No file              | `75c0007d032f`  |
| 1096   | No file              | `75c0007d032f`  |
| 1088   | No file              | `75c0007d032f`  |
| 1081   | No file              | `75c0007d032f`  |
| 1076   | No file              | `75c0007d032f`  |
| 1069   | No file              | `75c0007d032f`  |
| 1064   | No file              | `75c0007d032f`  |
| 1058   | No file              | `75c0007d032f`  |
| 1051   | No file              | `75c0007d032f`  |
| 1044   | No file              | `75c0007d032f`  |
| 1036   | No file              | `75c0007d032f`  |
| 1026   | No file              | `75c0007d032f`  |
| 1016   | No file              | `75c0007d032f`  |
| 1009   | No file              | `75c0007d032f`  |
| 1005   | No file              | `75c0007d032f`  |
| 1000   | No file              | `75c0007d032f`  |
| 998    | No file              | `75c0007d032f`  |
| 990    | No file              | `75c0007d032f`  |
| 979    | No file              | `75c0007d032f`  |
| 972    | No file              | `75c0007d032f`  |
| 963    | No file              | `75c0007d032f`  |
| 955    | No file              | `75c0007d032f`  |
| 946    | No file              | `75c0007d032f`  |
| 938    | No file              | `75c0007d032f`  |
| 927    | No file              | `75c0007d032f`  |
| 911    | No file              | `75c0007d032f`  |
| 904    | No file              | `75c0007d032f`  |
| 899    | No file              | `75c0007d032f`  |
| 894    | No file              | `75c0007d032f`  |
| 885    | No file              | `75c0007d032f`  |
| 879    | No file              | `75c0007d032f`  |
| 872    | No file              | `75c0007d032f`  |
| 864    | No file              | `75c0007d032f`  |
| 855    | No file              | `75c0007d032f`  |
| 853    | No file              | `75c0007d032f`  |
| 845    | No file              | `75c0007d032f`  |
| 837    | No file              | `75c0007d032f`  |
| 829    | No file              | `75c0007d032f`  |
| 822    | No file              | `75c0007d032f`  |
| 814    | No file              | `75c0007d032f`  |
| 805    | No file              | `75c0007d032f`  |
| 794    | No file              | `75c0007d032f`  |
| 787    | No file              | `75c0007d032f`  |
| 780    | No file              | `75c0007d032f`  |
| 771    | No file              | `75c0007d032f`  |
| 760    | No file              | `75c0007d032f`  |
| 748    | No file              | `75c0007d032f`  |
| 741    | No file              | `75c0007d032f`  |
| 736    | No file              | `75c0007d032f`  |
| 731    | No file              | `75c0007d032f`  |
| 723    | No file              | `75c0007d032f`  |
| 711    | No file              | `75c0007d032f`  |
| 707    | No file              | `75c0007d032f`  |
| 697    | No file              | `75c0007d032f`  |
| 689    | No file              | `75c0007d032f`  |
| 683    | No file              | `75c0007d032f`  |
| 678    | No file              | `75c0007d032f`  |
| 670    | No file              | `75c0007d032f`  |
| 661    | No file              | `75c0007d032f`  |
| 656    | No file              | `75c0007d032f`  |
| 652    | No file              | `75c0007d032f`  |
| 643    | No file              | `75c0007d032f`  |
| 637    | No file              | `75c0007d032f`  |
| 630    | No file              | `75c0007d032f`  |
| 627    | No file              | `75c0007d032f`  |
| 621    | No file              | `75c0007d032f`  |
| 617    | No file              | `75c0007d032f`  |
| 615    | No file              | `75c0007d032f`  |
| 606    | No file              | `75c0007d032f`  |
| 599    | No file              | `75c0007d032f`  |
| 592    | No file              | `75c0007d032f`  |
| 586    | No file              | `75c0007d032f`  |
| 577    | No file              | `75c0007d032f`  |
| 569    | No file              | `75c0007d032f`  |
| 561    | No file              | `75c0007d032f`  |
| 554    | No file              | `75c0007d032f`  |
| 542    | No file              | `75c0007d032f`  |
| 532    | No file              | `75c0007d032f`  |
| 531    | No file              | `75c0007d032f`  |
| 526    | No file              | `75c0007d032f`  |
| 521    | No file              | `75c0007d032f`  |
| 517    | No file              | `75c0007d032f`  |
| 510    | No file              | `75c0007d032f`  |
| 508    | No file              | `75c0007d032f`  |
| 504    | No file              | `75c0007d032f`  |
| 497    | No file              | `75c0007d032f`  |
| 491    | No file              | `75c0007d032f`  |
| 485    | No file              | `75c0007d032f`  |
| 478    | No file              | `75c0007d032f`  |
| 472    | No file              | `75c0007d032f`  |
| 466    | No file              | `75c0007d032f`  |
| 457    | No file              | `75c0007d032f`  |
| 452    | No file              | `75c0007d032f`  |
| 449    | No file              | `75c0007d032f`  |
| 435    | No file              | `75c0007d032f`  |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                       |
| ----------------------- | -------- | ------------------------------------------ |
| `zodiacsignoffset.dbss` | Required | ID-keyed index (same count, same order)    |
| `languagedata_en.loc`   | Optional | English names and trait text (str_type=7)  |

[`zodiacsignorder.dbss`](zodiacsignorder_dbss.md) holds the order the stars
light up per personality type, and
[`zodiacsignindex.bss`](zodiacsignindex_bss.md) the display order of the 12
signs.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                    |
| ------- | ------------- | ------- | ------------------------ |
| `+0x00` | u32           | count   | Number of records (= 12) |
| `+0x04` | Record[count] | records | See Record               |

### Record (variable: 54 bytes + stars and text)

All four strings are `str16`: a u64 count of UTF-16 code units (a u32 count
and a u32 `0`), then UTF-16LE text with no terminator.

| Offset                  | Type                     | Field              | Notes                                                          |
| ----------------------- | ------------------------ | ------------------ | -------------------------------------------------------------- |
| `+0x00`                 | u8                       | zodiac_id          | 1–12; always equal to the record's sequential index            |
| `+0x01`                 | u32                      | float_count        | Number of constellation star positions (slots); range 4–8      |
| `+0x05`                 | f32[float_count][3]      | star_positions     | `float_count` triples (x, y, 1.0); third element is always 1.0 |
| `star_positions+0x00`   | u32                      | pairs_count        | Number of star-connection pairs; usually equals `float_count`  |
| `star_positions+0x04`   | u16[pairs_count][2]      | star_pairs         | `pairs_count` pairs of (u16 a, u16 b); star connectivity data. Both are zero-based indices into `star_positions`; the first pair is `(0, 1)` on every sign |
| `star_pairs+0x00`       | str16                    | name_kr            | Korean constellation name ending in 자리, e.g. `망치자리`      |
| `name_kr+0x00` | str16                  | trait_text         | Korean personality traits                                      |
| `trait_text+0x00`       | str16                    | icon_small         | Path to small icon DDS                                         |
| `icon_small+0x00`       | str16                    | icon_large         | Path to large icon DDS                                         |
| `icon_large+0x00`       | u8                       | zodiac_id_dup      | Duplicate of `zodiac_id`                                       |
| `icon_large+0x01`       | u8                       | zodiac_id_dup2     | Duplicate of `zodiac_id` again                                 |
| `icon_large+0x02`       | u8                       | unknown_tail_02    | Always 0                                                       |
| `icon_large+0x03`       | u16                      | next_zodiac_id     | ID of the next zodiac in cycle (12 → 1)                        |
| `icon_large+0x05`       | u8                       | unknown_tail_05    | Always 1                                                       |
| `icon_large+0x06`       | u8                       | unknown_tail_06    | Always 0                                                       |
| `icon_large+0x07`       | u8                       | unknown_tail_07    | Always 1                                                       |
| `icon_large+0x08`       | u8                       | unknown_tail_08    | Always 0                                                       |
| `icon_large+0x09`       | u32                      | unknown_end        | Always 0                                                       |

The `unknown_tail_<hex>` offsets count from `zodiac_id_dup`.

Earlier versions of this doc called `zodiac_id_dup` `zodiac_id_tail`, and
read a u16 `unknown_after_pairs_count` after `pairs_count`, a `text_block` opening with a u32 `unknown_00` and a u16
`unknown_04`, and a `constellation_name` (now `name_kr`) with no length that
a reader found by scanning for the UTF-16LE bytes `90 C7 AC B9` ("자리").
Those 8 bytes are the first star index of `star_pairs` (always `0`) and the
top 6 bytes of the name's u64 count; the old reading shifted `star_pairs` by
2 bytes, so its last pair ended in the low half of that count. `star_pairs`
starts right after `pairs_count`, and the name is a `str16` like the other
three strings. Read this way the 12 records end exactly at end of file.

### `zodiacsignoffset.dbss`

Index file, one entry per zodiac record, stored in the same order as the main file.

| Offset  | Type              | Field   | Notes                              |
| ------- | ----------------- | ------- | ---------------------------------- |
| `+0x00` | u32               | count   | Must equal `zodiacsign.dbss` count |
| `+0x04` | Offset Row[count] | rows    | See Offset Row                     |

### Offset Row (9 bytes)

| Offset  | Type | Field       | Notes                                                            |
| ------- | ---- | ----------- | ---------------------------------------------------------------- |
| `+0x00` | u8   | zodiac_id   | Matches `zodiac_id` in main record                               |
| `+0x01` | u32  | data_offset | Byte offset into main file; 1 byte past the record start         |
| `+0x05` | u32  | data_size   | Byte count of record data (excluding the leading `zodiac_id` u8) |

`record_start = data_offset - 1`

## Reference Tables

### Zodiac ID → Name

| ID  | English Name  | Korean Constellation |
| --- | ------------- | -------------------- |
| 1   | Hammer        | 망치자리             |
| 2   | Boat          | 배자리               |
| 3   | Shield        | 방패자리             |
| 4   | Giant         | 거인자리             |
| 5   | Camel         | 낙타자리             |
| 6   | Black Dragon  | 검은용자리           |
| 7   | Treant Owl    | 엔트부엉이자리       |
| 8   | Elephant      | 코끼리자리           |
| 9   | Key           | 열쇠자리             |
| 10  | Wagon         | 마차자리             |
| 11  | Sealing Stone | 봉인석자리           |
| 12  | Goblin        | 고블린자리           |

### Personality Traits by Zodiac

| ID  | Traits (Korean)                                    |
| --- | -------------------------------------------------- |
| 1   | 용맹한, 보수적인, 의리 있는, 협동하는. 다혈질인.   |
| 2   | 풍류를 즐기는, 낙천적인, 자유로운. 방랑자.         |
| 3   | 이성적, 자신에게 엄격한, 계획적인.                 |
| 4   | 몽상가, 큰 뜻을 지닌, 재빠른. 관찰자.              |
| 5   | 끈기와 인내, 온순한, 또는 재주꾼.                  |
| 6   | 재물과 명성, 고매한, 세심한, 예민한, 사교적인.     |
| 7   | 우직한, 진부한, 뛰어난 지식, 천재 또는 멍청이      |
| 8   | 명예, 믿음이 강한, 우둔한, 헌신하는, 신뢰 받는.    |
| 9   | 탁월한 집중력, 지식의 탐구, 느긋한, 결정력이 좋은. |
| 10  | 행동하는, 재물을 타고난, 귀한, 이해타산적인        |
| 11  | 신중한, 기이한, 비밀을 가진, 단명할.               |
| 12  | 언어 술사, 신념, 지적인, 물질적인, 뛰어난 처세술   |

### Localisation

Names and trait descriptions in the user's language are in the LOC file under `str_type=7`, keyed by `str_id1=zodiac_id`:

| str_id4 | Field             |
| ------- | ----------------- |
| 0       | Sign name         |
| 1       | Trait description |

## Notes

- `star_positions` (x, y) pairs are 2D coordinates on the zodiac constellation display (range roughly ±250). The third float of each triple is always 1.0 and can be ignored.
- `personality_type` in `npcpersonality.dbss` cross-references `zodiac_id` via `major = personality_type // 100`.
