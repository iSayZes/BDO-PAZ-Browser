# `questgroup.dbss` Format

## Purpose

Quest grouping table. Each record names a quest chain/group in Korean and lists the `quest.dbss` quest IDs that belong to that group.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File              | Bytes | Records                                | Row bytes |
| ------ | -------------- | ----------------- | ----- | -------------------------------------- | --------- |
| 1      | 1220 and later | `questgroup.dbss` | 5,918 | 110 Quest Group Record, 474 Quest Link | 4         |

| Layout | File              | Known           | Unknown      |
| ------ | ----------------- | --------------- | ------------ |
| 1      | `questgroup.dbss` | 5,478 B (92.6%) | 440 B (7.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `1fa2e8560512`  |
| 3482   | Layout 1 | `1fa2e8560512`  |
| 3474   | Layout 1 | `1fa2e8560512`  |
| 3473   | Layout 1 | `1fa2e8560512`  |
| 3464   | Layout 1 | `1fa2e8560512`  |
| 3458   | Layout 1 | `1fa2e8560512`  |
| 3454   | Layout 1 | `1fa2e8560512`  |
| 3444   | Layout 1 | `1fa2e8560512`  |
| 3435   | Layout 1 | `1fa2e8560512`  |
| 3426   | Layout 1 | `1fa2e8560512`  |
| 3418   | Layout 1 | `1fa2e8560512`  |
| 3412   | Layout 1 | `1fa2e8560512`  |
| 3402   | Layout 1 | `1fa2e8560512`  |
| 3396   | Layout 1 | `1fa2e8560512`  |
| 3387   | Layout 1 | `1fa2e8560512`  |
| 3381   | Layout 1 | `1fa2e8560512`  |
| 3373   | Layout 1 | `1fa2e8560512`  |
| 3364   | Layout 1 | `1fa2e8560512`  |
| 3356   | Layout 1 | `1fa2e8560512`  |
| 3349   | Layout 1 | `1fa2e8560512`  |
| 3342   | Layout 1 | `1fa2e8560512`  |
| 3335   | Layout 1 | `1fa2e8560512`  |
| 3326   | Layout 1 | `1fa2e8560512`  |
| 3321   | Layout 1 | `1fa2e8560512`  |
| 3314   | Layout 1 | `1fa2e8560512`  |
| 3303   | Layout 1 | `1fa2e8560512`  |
| 3302   | Layout 1 | `1fa2e8560512`  |
| 3293   | Layout 1 | `1fa2e8560512`  |
| 3283   | Layout 1 | `1fa2e8560512`  |
| 3275   | Layout 1 | `1fa2e8560512`  |
| 3267   | Layout 1 | `1fa2e8560512`  |
| 3258   | Layout 1 | `1fa2e8560512`  |
| 3251   | Layout 1 | `1fa2e8560512`  |
| 3242   | Layout 1 | `1fa2e8560512`  |
| 3235   | Layout 1 | `1fa2e8560512`  |
| 3229   | Layout 1 | `1fa2e8560512`  |
| 3212   | Layout 1 | `1fa2e8560512`  |
| 3203   | Layout 1 | `1fa2e8560512`  |
| 3193   | Layout 1 | `1fa2e8560512`  |
| 3186   | Layout 1 | `1fa2e8560512`  |
| 3177   | Layout 1 | `1fa2e8560512`  |
| 3169   | Layout 1 | `1fa2e8560512`  |
| 3158   | Layout 1 | `1fa2e8560512`  |
| 3151   | Layout 1 | `1fa2e8560512`  |
| 3144   | Layout 1 | `1fa2e8560512`  |
| 3133   | Layout 1 | `1fa2e8560512`  |
| 3125   | Layout 1 | `1fa2e8560512`  |
| 3118   | Layout 1 | `1fa2e8560512`  |
| 3111   | Layout 1 | `1fa2e8560512`  |
| 3103   | Layout 1 | `1fa2e8560512`  |
| 3095   | Layout 1 | `1fa2e8560512`  |
| 3086   | Layout 1 | `1fa2e8560512`  |
| 3072   | Layout 1 | `1fa2e8560512`  |
| 3062   | Layout 1 | `1fa2e8560512`  |
| 3052   | Layout 1 | `1fa2e8560512`  |
| 3045   | Layout 1 | `1fa2e8560512`  |
| 3037   | Layout 1 | `1fa2e8560512`  |
| 3030   | Layout 1 | `1fa2e8560512`  |
| 3021   | Layout 1 | `1fa2e8560512`  |
| 3012   | Layout 1 | `1fa2e8560512`  |
| 3002   | Layout 1 | `1fa2e8560512`  |
| 2995   | Layout 1 | `1fa2e8560512`  |
| 2987   | Layout 1 | `1fa2e8560512`  |
| 2978   | Layout 1 | `1fa2e8560512`  |
| 2970   | Layout 1 | `1fa2e8560512`  |
| 2959   | Layout 1 | `1fa2e8560512`  |
| 2951   | Layout 1 | `1fa2e8560512`  |
| 2942   | Layout 1 | `1fa2e8560512`  |
| 2935   | Layout 1 | `1fa2e8560512`  |
| 2932   | Layout 1 | `1fa2e8560512`  |
| 2923   | Layout 1 | `1fa2e8560512`  |
| 2919   | Layout 1 | `1fa2e8560512`  |
| 2907   | Layout 1 | `1fa2e8560512`  |
| 2900   | Layout 1 | `1fa2e8560512`  |
| 2891   | Layout 1 | `1fa2e8560512`  |
| 2882   | Layout 1 | `1fa2e8560512`  |
| 2872   | Layout 1 | `1fa2e8560512`  |
| 2863   | Layout 1 | `1fa2e8560512`  |
| 2855   | Layout 1 | `1fa2e8560512`  |
| 2849   | Layout 1 | `1fa2e8560512`  |
| 2844   | Layout 1 | `1fa2e8560512`  |
| 2834   | Layout 1 | `1fa2e8560512`  |
| 2825   | Layout 1 | `1fa2e8560512`  |
| 2819   | Layout 1 | `1fa2e8560512`  |
| 2811   | Layout 1 | `1fa2e8560512`  |
| 2803   | Layout 1 | `1fa2e8560512`  |
| 2794   | Layout 1 | `1fa2e8560512`  |
| 2783   | Layout 1 | `1fa2e8560512`  |
| 2774   | Layout 1 | `1fa2e8560512`  |
| 2765   | Layout 1 | `1fa2e8560512`  |
| 2756   | Layout 1 | `1fa2e8560512`  |
| 2750   | Layout 1 | `1fa2e8560512`  |
| 2743   | Layout 1 | `1fa2e8560512`  |
| 2736   | Layout 1 | `1fa2e8560512`  |
| 2726   | Layout 1 | `1fa2e8560512`  |
| 2717   | Layout 1 | `1fa2e8560512`  |
| 2709   | Layout 1 | `1fa2e8560512`  |
| 2703   | Layout 1 | `1fa2e8560512`  |
| 2695   | Layout 1 | `1fa2e8560512`  |
| 2684   | Layout 1 | `1fa2e8560512`  |
| 2672   | Layout 1 | `1fa2e8560512`  |
| 2665   | Layout 1 | `1fa2e8560512`  |
| 2657   | Layout 1 | `1fa2e8560512`  |
| 2649   | Layout 1 | `1fa2e8560512`  |
| 2644   | Layout 1 | `1fa2e8560512`  |
| 2637   | Layout 1 | `1fa2e8560512`  |
| 2629   | Layout 1 | `1fa2e8560512`  |
| 2619   | Layout 1 | `1fa2e8560512`  |
| 2612   | Layout 1 | `1fa2e8560512`  |
| 2606   | Layout 1 | `1fa2e8560512`  |
| 2602   | Layout 1 | `1fa2e8560512`  |
| 2601   | Layout 1 | `1fa2e8560512`  |
| 2592   | Layout 1 | `1fa2e8560512`  |
| 2583   | Layout 1 | `1fa2e8560512`  |
| 2575   | Layout 1 | `1fa2e8560512`  |
| 2567   | Layout 1 | `1fa2e8560512`  |
| 2560   | Layout 1 | `1fa2e8560512`  |
| 2553   | Layout 1 | `1fa2e8560512`  |
| 2545   | Layout 1 | `1fa2e8560512`  |
| 2538   | Layout 1 | `1fa2e8560512`  |
| 2529   | Layout 1 | `1fa2e8560512`  |
| 2519   | Layout 1 | `1fa2e8560512`  |
| 2513   | Layout 1 | `1fa2e8560512`  |
| 2510   | Layout 1 | `1fa2e8560512`  |
| 2507   | Layout 1 | `1fa2e8560512`  |
| 2503   | Layout 1 | `1fa2e8560512`  |
| 2498   | Layout 1 | `1fa2e8560512`  |
| 2492   | Layout 1 | `1fa2e8560512`  |
| 2487   | Layout 1 | `1fa2e8560512`  |
| 2480   | Layout 1 | `1fa2e8560512`  |
| 2474   | Layout 1 | `1fa2e8560512`  |
| 2468   | Layout 1 | `1fa2e8560512`  |
| 2460   | Layout 1 | `1fa2e8560512`  |
| 2453   | Layout 1 | `1fa2e8560512`  |
| 2444   | Layout 1 | `1fa2e8560512`  |
| 2438   | Layout 1 | `1fa2e8560512`  |
| 2434   | Layout 1 | `1fa2e8560512`  |
| 2429   | Layout 1 | `1fa2e8560512`  |
| 2421   | Layout 1 | `1fa2e8560512`  |
| 2414   | Layout 1 | `1fa2e8560512`  |
| 2407   | Layout 1 | `1fa2e8560512`  |
| 2401   | Layout 1 | `1fa2e8560512`  |
| 2397   | Layout 1 | `1fa2e8560512`  |
| 2393   | Layout 1 | `1fa2e8560512`  |
| 2384   | Layout 1 | `1fa2e8560512`  |
| 2378   | Layout 1 | `1fa2e8560512`  |
| 2372   | Layout 1 | `1fa2e8560512`  |
| 2358   | Layout 1 | `1fa2e8560512`  |
| 2352   | Layout 1 | `1fa2e8560512`  |
| 2347   | Layout 1 | `1fa2e8560512`  |
| 2343   | Layout 1 | `1fa2e8560512`  |
| 2335   | Layout 1 | `1fa2e8560512`  |
| 2327   | Layout 1 | `1fa2e8560512`  |
| 2324   | Layout 1 | `1fa2e8560512`  |
| 2319   | Layout 1 | `1fa2e8560512`  |
| 2313   | Layout 1 | `1fa2e8560512`  |
| 2308   | Layout 1 | `1fa2e8560512`  |
| 2302   | Layout 1 | `1fa2e8560512`  |
| 2295   | Layout 1 | `1fa2e8560512`  |
| 2290   | Layout 1 | `1fa2e8560512`  |
| 2284   | Layout 1 | `1fa2e8560512`  |
| 2276   | Layout 1 | `1fa2e8560512`  |
| 2269   | Layout 1 | `1fa2e8560512`  |
| 2259   | Layout 1 | `1fa2e8560512`  |
| 2250   | Layout 1 | `1fa2e8560512`  |
| 2243   | Layout 1 | `1fa2e8560512`  |
| 2235   | Layout 1 | `1fa2e8560512`  |
| 2229   | Layout 1 | `1fa2e8560512`  |
| 2224   | Layout 1 | `1fa2e8560512`  |
| 2218   | Layout 1 | `1fa2e8560512`  |
| 2215   | Layout 1 | `1fa2e8560512`  |
| 2207   | Layout 1 | `1fa2e8560512`  |
| 2203   | Layout 1 | `1fa2e8560512`  |
| 2196   | Layout 1 | `1fa2e8560512`  |
| 2192   | Layout 1 | `1fa2e8560512`  |
| 2189   | Layout 1 | `1fa2e8560512`  |
| 2183   | Layout 1 | `1fa2e8560512`  |
| 2179   | Layout 1 | `1fa2e8560512`  |
| 2171   | Layout 1 | `1fa2e8560512`  |
| 2163   | Layout 1 | `1fa2e8560512`  |
| 2156   | Layout 1 | `1fa2e8560512`  |
| 2151   | Layout 1 | `1fa2e8560512`  |
| 2147   | Layout 1 | `1fa2e8560512`  |
| 2142   | Layout 1 | `1fa2e8560512`  |
| 2138   | Layout 1 | `1fa2e8560512`  |
| 2134   | Layout 1 | `1fa2e8560512`  |
| 2130   | Layout 1 | `1fa2e8560512`  |
| 2122   | Layout 1 | `1fa2e8560512`  |
| 2107   | Layout 1 | `1fa2e8560512`  |
| 2098   | Layout 1 | `1fa2e8560512`  |
| 2089   | Layout 1 | `1fa2e8560512`  |
| 2081   | Layout 1 | `1fa2e8560512`  |
| 2073   | Layout 1 | `1fa2e8560512`  |
| 2067   | Layout 1 | `1fa2e8560512`  |
| 2063   | Layout 1 | `1fa2e8560512`  |
| 2059   | Layout 1 | `1fa2e8560512`  |
| 2052   | Layout 1 | `1fa2e8560512`  |
| 2044   | Layout 1 | `1fa2e8560512`  |
| 2039   | Layout 1 | `1fa2e8560512`  |
| 2032   | Layout 1 | `1fa2e8560512`  |
| 2025   | Layout 1 | `1fa2e8560512`  |
| 2011   | Layout 1 | `1fa2e8560512`  |
| 2005   | Layout 1 | `1fa2e8560512`  |
| 2000   | Layout 1 | `1fa2e8560512`  |
| 1996   | Layout 1 | `1fa2e8560512`  |
| 1991   | Layout 1 | `1fa2e8560512`  |
| 1985   | Layout 1 | `1fa2e8560512`  |
| 1980   | Layout 1 | `1fa2e8560512`  |
| 1969   | Layout 1 | `1fa2e8560512`  |
| 1964   | Layout 1 | `1fa2e8560512`  |
| 1958   | Layout 1 | `1fa2e8560512`  |
| 1950   | Layout 1 | `1fa2e8560512`  |
| 1945   | Layout 1 | `1fa2e8560512`  |
| 1937   | Layout 1 | `1fa2e8560512`  |
| 1933   | Layout 1 | `1fa2e8560512`  |
| 1927   | Layout 1 | `1fa2e8560512`  |
| 1921   | Layout 1 | `1fa2e8560512`  |
| 1914   | Layout 1 | `1fa2e8560512`  |
| 1908   | Layout 1 | `1fa2e8560512`  |
| 1897   | Layout 1 | `1fa2e8560512`  |
| 1892   | Layout 1 | `1fa2e8560512`  |
| 1886   | Layout 1 | `1fa2e8560512`  |
| 1881   | Layout 1 | `1fa2e8560512`  |
| 1871   | Layout 1 | `1fa2e8560512`  |
| 1866   | Layout 1 | `1fa2e8560512`  |
| 1862   | Layout 1 | `1fa2e8560512`  |
| 1854   | Layout 1 | `1fa2e8560512`  |
| 1846   | Layout 1 | `1fa2e8560512`  |
| 1838   | Layout 1 | `1fa2e8560512`  |
| 1832   | Layout 1 | `1fa2e8560512`  |
| 1826   | Layout 1 | `1fa2e8560512`  |
| 1822   | Layout 1 | `1fa2e8560512`  |
| 1818   | Layout 1 | `1fa2e8560512`  |
| 1804   | Layout 1 | `1fa2e8560512`  |
| 1794   | Layout 1 | `1fa2e8560512`  |
| 1790   | Layout 1 | `1fa2e8560512`  |
| 1784   | Layout 1 | `1fa2e8560512`  |
| 1774   | Layout 1 | `1fa2e8560512`  |
| 1771   | Layout 1 | `1fa2e8560512`  |
| 1762   | Layout 1 | `1fa2e8560512`  |
| 1759   | Layout 1 | `1fa2e8560512`  |
| 1754   | Layout 1 | `1fa2e8560512`  |
| 1749   | Layout 1 | `1fa2e8560512`  |
| 1743   | Layout 1 | `1fa2e8560512`  |
| 1737   | Layout 1 | `1fa2e8560512`  |
| 1731   | Layout 1 | `1fa2e8560512`  |
| 1725   | Layout 1 | `1fa2e8560512`  |
| 1717   | Layout 1 | `1fa2e8560512`  |
| 1710   | Layout 1 | `1fa2e8560512`  |
| 1704   | Layout 1 | `1fa2e8560512`  |
| 1698   | Layout 1 | `1fa2e8560512`  |
| 1690   | Layout 1 | `1fa2e8560512`  |
| 1685   | Layout 1 | `1fa2e8560512`  |
| 1680   | Layout 1 | `1fa2e8560512`  |
| 1674   | Layout 1 | `1fa2e8560512`  |
| 1668   | Layout 1 | `1fa2e8560512`  |
| 1659   | Layout 1 | `1fa2e8560512`  |
| 1649   | Layout 1 | `1fa2e8560512`  |
| 1642   | Layout 1 | `1fa2e8560512`  |
| 1636   | Layout 1 | `1fa2e8560512`  |
| 1628   | Layout 1 | `1fa2e8560512`  |
| 1622   | Layout 1 | `1fa2e8560512`  |
| 1614   | Layout 1 | `1fa2e8560512`  |
| 1608   | Layout 1 | `1fa2e8560512`  |
| 1602   | Layout 1 | `1fa2e8560512`  |
| 1598   | Layout 1 | `1fa2e8560512`  |
| 1594   | Layout 1 | `1fa2e8560512`  |
| 1590   | Layout 1 | `1fa2e8560512`  |
| 1587   | Layout 1 | `1fa2e8560512`  |
| 1584   | Layout 1 | `1fa2e8560512`  |
| 1579   | Layout 1 | `1fa2e8560512`  |
| 1572   | Layout 1 | `1fa2e8560512`  |
| 1565   | Layout 1 | `1fa2e8560512`  |
| 1559   | Layout 1 | `1fa2e8560512`  |
| 1554   | Layout 1 | `1fa2e8560512`  |
| 1547   | Layout 1 | `1fa2e8560512`  |
| 1537   | Layout 1 | `1fa2e8560512`  |
| 1529   | Layout 1 | `1fa2e8560512`  |
| 1524   | Layout 1 | `1fa2e8560512`  |
| 1519   | Layout 1 | `1fa2e8560512`  |
| 1509   | Layout 1 | `1fa2e8560512`  |
| 1506   | Layout 1 | `1fa2e8560512`  |
| 1504   | Layout 1 | `1fa2e8560512`  |
| 1500   | Layout 1 | `1fa2e8560512`  |
| 1493   | Layout 1 | `1fa2e8560512`  |
| 1489   | Layout 1 | `1fa2e8560512`  |
| 1485   | Layout 1 | `1fa2e8560512`  |
| 1481   | Layout 1 | `1fa2e8560512`  |
| 1474   | Layout 1 | `1fa2e8560512`  |
| 1466   | Layout 1 | `1fa2e8560512`  |
| 1462   | Layout 1 | `1fa2e8560512`  |
| 1459   | Layout 1 | `1fa2e8560512`  |
| 1453   | Layout 1 | `1fa2e8560512`  |
| 1450   | Layout 1 | `1fa2e8560512`  |
| 1445   | Layout 1 | `1fa2e8560512`  |
| 1439   | Layout 1 | `1fa2e8560512`  |
| 1433   | Layout 1 | `1fa2e8560512`  |
| 1430   | Layout 1 | `1fa2e8560512`  |
| 1426   | Layout 1 | `1fa2e8560512`  |
| 1421   | Layout 1 | `1fa2e8560512`  |
| 1417   | Layout 1 | `1fa2e8560512`  |
| 1416   | Layout 1 | `1fa2e8560512`  |
| 1409   | Layout 1 | `1fa2e8560512`  |
| 1405   | Layout 1 | `1fa2e8560512`  |
| 1401   | Layout 1 | `1fa2e8560512`  |
| 1396   | Layout 1 | `1fa2e8560512`  |
| 1391   | Layout 1 | `1fa2e8560512`  |
| 1390   | Layout 1 | `1fa2e8560512`  |
| 1386   | Layout 1 | `1fa2e8560512`  |
| 1381   | Layout 1 | `1fa2e8560512`  |
| 1379   | Layout 1 | `1fa2e8560512`  |
| 1372   | Layout 1 | `1fa2e8560512`  |
| 1366   | Layout 1 | `1fa2e8560512`  |
| 1364   | Layout 1 | `1fa2e8560512`  |
| 1363   | Layout 1 | `1fa2e8560512`  |
| 1360   | Layout 1 | `1fa2e8560512`  |
| 1358   | Layout 1 | `1fa2e8560512`  |
| 1355   | Layout 1 | `1fa2e8560512`  |
| 1351   | Layout 1 | `1fa2e8560512`  |
| 1348   | Layout 1 | `1fa2e8560512`  |
| 1346   | Layout 1 | `1fa2e8560512`  |
| 1341   | Layout 1 | `1fa2e8560512`  |
| 1340   | Layout 1 | `1fa2e8560512`  |
| 1338   | Layout 1 | `1fa2e8560512`  |
| 1335   | Layout 1 | `1fa2e8560512`  |
| 1333   | Layout 1 | `1fa2e8560512`  |
| 1329   | Layout 1 | `1fa2e8560512`  |
| 1327   | Layout 1 | `1fa2e8560512`  |
| 1324   | Layout 1 | `1fa2e8560512`  |
| 1321   | Layout 1 | `1fa2e8560512`  |
| 1319   | Layout 1 | `1fa2e8560512`  |
| 1318   | Layout 1 | `1fa2e8560512`  |
| 1316   | Layout 1 | `1fa2e8560512`  |
| 1313   | Layout 1 | `1fa2e8560512`  |
| 1311   | Layout 1 | `1fa2e8560512`  |
| 1309   | Layout 1 | `1fa2e8560512`  |
| 1304   | Layout 1 | `1fa2e8560512`  |
| 1292   | Layout 1 | `1fa2e8560512`  |
| 1286   | Layout 1 | `1fa2e8560512`  |
| 1280   | Layout 1 | `1fa2e8560512`  |
| 1276   | Layout 1 | `1fa2e8560512`  |
| 1267   | Layout 1 | `1fa2e8560512`  |
| 1261   | Layout 1 | `1fa2e8560512`  |
| 1256   | Layout 1 | `1fa2e8560512`  |
| 1250   | Layout 1 | `1fa2e8560512`  |
| 1246   | Layout 1 | `1fa2e8560512`  |
| 1239   | Layout 1 | `1fa2e8560512`  |
| 1230   | Layout 1 | `1fa2e8560512`  |
| 1226   | Layout 1 | `1fa2e8560512`  |
| 1220   | Layout 1 | `1fa2e8560512`  |
| 1217   | No file  | `1fa2e8560512`  |
| 1211   | No file  | `1fa2e8560512`  |
| 1210   | No file  | `1fa2e8560512`  |
| 1208   | No file  | `1fa2e8560512`  |
| 1203   | No file  | `1fa2e8560512`  |
| 1197   | No file  | `1fa2e8560512`  |
| 1194   | No file  | `1fa2e8560512`  |
| 1192   | No file  | `1fa2e8560512`  |
| 1187   | No file  | `1fa2e8560512`  |
| 1183   | No file  | `1fa2e8560512`  |
| 1177   | No file  | `1fa2e8560512`  |
| 1173   | No file  | `1fa2e8560512`  |
| 1167   | No file  | `1fa2e8560512`  |
| 1164   | No file  | `1fa2e8560512`  |
| 1156   | No file  | `1fa2e8560512`  |
| 1149   | No file  | `1fa2e8560512`  |
| 1144   | No file  | `1fa2e8560512`  |
| 1137   | No file  | `1fa2e8560512`  |
| 1132   | No file  | `1fa2e8560512`  |
| 1127   | No file  | `1fa2e8560512`  |
| 1122   | No file  | `1fa2e8560512`  |
| 1118   | No file  | `1fa2e8560512`  |
| 1114   | No file  | `1fa2e8560512`  |
| 1109   | No file  | `1fa2e8560512`  |
| 1102   | No file  | `1fa2e8560512`  |
| 1096   | No file  | `1fa2e8560512`  |
| 1088   | No file  | `1fa2e8560512`  |
| 1081   | No file  | `1fa2e8560512`  |
| 1076   | No file  | `1fa2e8560512`  |
| 1069   | No file  | `1fa2e8560512`  |
| 1064   | No file  | `1fa2e8560512`  |
| 1058   | No file  | `1fa2e8560512`  |
| 1051   | No file  | `1fa2e8560512`  |
| 1044   | No file  | `1fa2e8560512`  |
| 1036   | No file  | `1fa2e8560512`  |
| 1026   | No file  | `1fa2e8560512`  |
| 1016   | No file  | `1fa2e8560512`  |
| 1009   | No file  | `1fa2e8560512`  |
| 1005   | No file  | `1fa2e8560512`  |
| 1000   | No file  | `1fa2e8560512`  |
| 998    | No file  | `1fa2e8560512`  |
| 990    | No file  | `1fa2e8560512`  |
| 979    | No file  | `1fa2e8560512`  |
| 972    | No file  | `1fa2e8560512`  |
| 963    | No file  | `1fa2e8560512`  |
| 955    | No file  | `1fa2e8560512`  |
| 946    | No file  | `1fa2e8560512`  |
| 938    | No file  | `1fa2e8560512`  |
| 927    | No file  | `1fa2e8560512`  |
| 911    | No file  | `1fa2e8560512`  |
| 904    | No file  | `1fa2e8560512`  |
| 899    | No file  | `1fa2e8560512`  |
| 894    | No file  | `1fa2e8560512`  |
| 885    | No file  | `1fa2e8560512`  |
| 879    | No file  | `1fa2e8560512`  |
| 872    | No file  | `1fa2e8560512`  |
| 864    | No file  | `1fa2e8560512`  |
| 855    | No file  | `1fa2e8560512`  |
| 853    | No file  | `1fa2e8560512`  |
| 845    | No file  | `1fa2e8560512`  |
| 837    | No file  | `1fa2e8560512`  |
| 829    | No file  | `1fa2e8560512`  |
| 822    | No file  | `1fa2e8560512`  |
| 814    | No file  | `1fa2e8560512`  |
| 805    | No file  | `1fa2e8560512`  |
| 794    | No file  | `1fa2e8560512`  |
| 787    | No file  | `1fa2e8560512`  |
| 780    | No file  | `1fa2e8560512`  |
| 771    | No file  | `1fa2e8560512`  |
| 760    | No file  | `1fa2e8560512`  |
| 748    | No file  | `1fa2e8560512`  |
| 741    | No file  | `1fa2e8560512`  |
| 736    | No file  | `1fa2e8560512`  |
| 731    | No file  | `1fa2e8560512`  |
| 723    | No file  | `1fa2e8560512`  |
| 711    | No file  | `1fa2e8560512`  |
| 707    | No file  | `1fa2e8560512`  |
| 697    | No file  | `1fa2e8560512`  |
| 689    | No file  | `1fa2e8560512`  |
| 683    | No file  | `1fa2e8560512`  |
| 678    | No file  | `1fa2e8560512`  |
| 670    | No file  | `1fa2e8560512`  |
| 661    | No file  | `1fa2e8560512`  |
| 656    | No file  | `1fa2e8560512`  |
| 652    | No file  | `1fa2e8560512`  |
| 643    | No file  | `1fa2e8560512`  |
| 637    | No file  | `1fa2e8560512`  |
| 630    | No file  | `1fa2e8560512`  |
| 627    | No file  | `1fa2e8560512`  |
| 621    | No file  | `1fa2e8560512`  |
| 617    | No file  | `1fa2e8560512`  |
| 615    | No file  | `1fa2e8560512`  |
| 606    | No file  | `1fa2e8560512`  |
| 599    | No file  | `1fa2e8560512`  |
| 592    | No file  | `1fa2e8560512`  |
| 586    | No file  | `1fa2e8560512`  |
| 577    | No file  | `1fa2e8560512`  |
| 569    | No file  | `1fa2e8560512`  |
| 561    | No file  | `1fa2e8560512`  |
| 554    | No file  | `1fa2e8560512`  |
| 542    | No file  | `1fa2e8560512`  |
| 532    | No file  | `1fa2e8560512`  |
| 531    | No file  | `1fa2e8560512`  |
| 526    | No file  | `1fa2e8560512`  |
| 521    | No file  | `1fa2e8560512`  |
| 517    | No file  | `1fa2e8560512`  |
| 510    | No file  | `1fa2e8560512`  |
| 508    | No file  | `1fa2e8560512`  |
| 504    | No file  | `1fa2e8560512`  |
| 497    | No file  | `1fa2e8560512`  |
| 491    | No file  | `1fa2e8560512`  |
| 485    | No file  | `1fa2e8560512`  |
| 478    | No file  | `1fa2e8560512`  |
| 472    | No file  | `1fa2e8560512`  |
| 466    | No file  | `1fa2e8560512`  |
| 457    | No file  | `1fa2e8560512`  |
| 452    | No file  | `1fa2e8560512`  |
| 449    | No file  | `1fa2e8560512`  |
| 435    | No file  | `1fa2e8560512`  |

<!-- versions:end -->

## Companion Files

| File          | Required | Role                                             |
| ------------- | -------- | ------------------------------------------------ |
| `quest.dbss`  | Optional | Provides full quest records for listed quest IDs |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                      | Field   | Notes                                       |
| ------- | ------------------------- | ------- | ------------------------------------------- |
| `+0x00` | u32                       | count   | Number of quest group records; `110` in the pre-2026-09-27 fixture and in the 2026-09-27 client |
| `+0x04` | Quest Group Record[count] | records | See Quest Group Record                      |

Records start immediately after the header at `+0x04`. Records are variable length because each group name and child quest list can have different sizes.

### Quest Group Record (variable: 18 bytes + name and quest links)

| Offset         | Type                    | Field       | Notes                                                              |
| -------------- | ----------------------- | ----------- | ------------------------------------------------------------------ |
| `+0x00`        | u16                     | group_id    | Quest group identifier; also appears in child quest IDs            |
| `+0x02`        | str16                   | name_kr     | Korean quest group title, not NUL-terminated; see Field Names      |
| `name_kr+0x00` | u32                     | quest_count | Number of child quest IDs                                          |
| `name_kr+0x04` | Quest Link[quest_count] | quests      | `quest_count` child quest references                               |
| `quests+0x00`  | u32                     | unknown_end | Observed `0` in all 110 records; see Field Names                   |

### Quest Link (4 bytes)

| Offset  | Type | Field    | Notes                                             |
| ------- | ---- | -------- | ------------------------------------------------- |
| `+0x00` | u16  | group_id | Child quest group ID; normally matches parent     |
| `+0x02` | u16  | quest_no | 1-based quest number within the group             |

The corresponding `quest.dbss` `quest_id` is the same 4 bytes interpreted as a little-endian `u32`:

```text
quest_id = (quest_no << 16) | group_id
```

## Observed Records

Pre-2026-09-27 fixture:

| File Offset | Group ID | Name KR                  | Quest Count | Quest IDs                         |
| ----------- | -------- | ------------------------ | ----------- | --------------------------------- |
| `0x000004`  | `1022`   | `소서러, 여정의 시작`    | `3`         | `66558`, `132094`, `197630`       |
| `0x000038`  | `1014`   | `워리어, 여정의 시작`    | `3`         | `66550`, `132086`, `197622`       |
| `0x00006C`  | `1055`   | `해적이 숨겨 놓은 보물`  | `6`         | `66591` .. `394271`               |
| `0x0000AE`  | `503`    | `소서러의 기술`          | `4`         | `66039`, `131575`, `197111`, `262647` |
| `0x0000DE`  | `3100`   | `칼페온의 레이트 가문`   | `4`         | `68636`, `134172`, `199708`, `265244` |

## Field Names

The record is the `Group_Quest` sheet of a private server on client 1784
(`QuestGroup`, `GroupName`). That server's dump (`Instance_dumpFull.exe`)
reads the client record (row reader at VA `0x140c18560`) as a u16 group key,
a wide string, a u32 count with that many u32 quest links, and a closing u32,
and rejects a record whose bytes it does not consume exactly. Its string
reader takes a u64 code unit count (VA `0x140510d78`), so `+0x02` to `+0x09`
is one count and the text starts at `+0x0A`. Earlier versions of this doc
read those 8 bytes as a u16 `name_len`, a u32 `unknown_04` and a u16
`unknown_08`; the upper six bytes are `0` because no title has 65,536 code
units. The sheet loader builds each quest list as `(group, 1)`, `(group,
2)`, ... for as long as the quest exists.

`unknown_end` has no sheet column and no member in the 2016 PDB's
`gc::QuestGroupStaticStatus`. The loader sets it to `0`; the only code that
reads it passes it with LOC type 25 to a lookup that skips `0` and otherwise
reads an 8-byte entry at `value * 8` of a `Head_LanguageData_` file, the
same use as the `newquest.bss` group trailer ([`newquest_bss.md`](../bss/newquest_bss.md)
Open Questions). Nothing names it.

The sheet and the private server's own file hold the same 114 groups with
the same names; client 3474 shares 110 of them, all with the same name.

## Notes

- Observed decompressed size is `6,038` bytes in the pre-2026-09-27 fixture and `5,918` in the 2026-09-27 client.
- `(file_size - 4) / count` is not integral, confirming variable-length records.
- All 504 child quest IDs were found as little-endian `u32` values in the extracted `quest.dbss` sample. All are `allquestlist.bss` entries: 504 of 504 in the pre-2026-09-27 fixture, 474 of 474 in the 2026-09-27 client.
- Child links are stored as `(group_id, quest_no)` pairs, not as standalone `u32` fields, but the byte representation is identical to the derived `quest_id`.
- `quest_count` ranges from `0` to `21` in both files. Two groups are empty in the fixture and nine in the 2026-09-27 client, which emptied group `1022` (Sorceress, Beginning of the Journey) among others.
- The `name_kr` count ranges from `3` to `15` UTF-16 code units.

## Open Questions

### Localization

Group names are stored inline as Korean UTF-16 text. LOC type `18` rows keyed by `str_id1=group_id` provide child quest titles, not group names. The handler reads English group names from LOC type `25` keyed by `str_id1=group_id` (group `1022` `소서러, 여정의 시작` is "Sorceress, Beginning of the Journey"); all 110 groups have one in both the pre-2026-09-27 fixture and the 2026-09-27 client.
