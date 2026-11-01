# `worldmapdecostaticstatusmanager.bss` Format

## Purpose

The decoration models of the world map: per row a `.pam` model (town
houses, castles, farms, temples) with its world position, scale and
rotation. The world map draws these models over the terrain.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                  | Bytes  | Records | Row bytes               |
| ------ | -------------- | ------------------------------------- | ------ | ------- | ----------------------- |
| 1      | 2987 and later | `worldmapdecostaticstatusmanager.bss` | 41,058 | 657 Row | 49 to 78, 62 on average |

| Layout | File                                  | Known            | Unknown        |
| ------ | ------------------------------------- | ---------------- | -------------- |
| 1      | `worldmapdecostaticstatusmanager.bss` | 39,744 B (96.8%) | 1,314 B (3.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `3a1e19b292dc`  |
| 3482   | Layout 1 | `3a1e19b292dc`  |
| 3474   | Layout 1 | `3a1e19b292dc`  |
| 3473   | Layout 1 | `3a1e19b292dc`  |
| 3464   | Layout 1 | `3a1e19b292dc`  |
| 3458   | Layout 1 | `3a1e19b292dc`  |
| 3454   | Layout 1 | `3a1e19b292dc`  |
| 3444   | Layout 1 | `3a1e19b292dc`  |
| 3435   | Layout 1 | `3a1e19b292dc`  |
| 3426   | Layout 1 | `3a1e19b292dc`  |
| 3418   | Layout 1 | `3a1e19b292dc`  |
| 3412   | Layout 1 | `3a1e19b292dc`  |
| 3402   | Layout 1 | `3a1e19b292dc`  |
| 3396   | Layout 1 | `3a1e19b292dc`  |
| 3387   | Layout 1 | `3a1e19b292dc`  |
| 3381   | Layout 1 | `3a1e19b292dc`  |
| 3373   | Layout 1 | `3a1e19b292dc`  |
| 3364   | Layout 1 | `3a1e19b292dc`  |
| 3356   | Layout 1 | `3a1e19b292dc`  |
| 3349   | Layout 1 | `3a1e19b292dc`  |
| 3342   | Layout 1 | `3a1e19b292dc`  |
| 3335   | Layout 1 | `3a1e19b292dc`  |
| 3326   | Layout 1 | `3a1e19b292dc`  |
| 3321   | Layout 1 | `3a1e19b292dc`  |
| 3314   | Layout 1 | `3a1e19b292dc`  |
| 3303   | Layout 1 | `3a1e19b292dc`  |
| 3302   | Layout 1 | `3a1e19b292dc`  |
| 3293   | Layout 1 | `3a1e19b292dc`  |
| 3283   | Layout 1 | `3a1e19b292dc`  |
| 3275   | Layout 1 | `3a1e19b292dc`  |
| 3267   | Layout 1 | `3a1e19b292dc`  |
| 3258   | Layout 1 | `3a1e19b292dc`  |
| 3251   | Layout 1 | `3a1e19b292dc`  |
| 3242   | Layout 1 | `3a1e19b292dc`  |
| 3235   | Layout 1 | `3a1e19b292dc`  |
| 3229   | Layout 1 | `3a1e19b292dc`  |
| 3212   | Layout 1 | `3a1e19b292dc`  |
| 3203   | Layout 1 | `3a1e19b292dc`  |
| 3193   | Layout 1 | `3a1e19b292dc`  |
| 3186   | Layout 1 | `3a1e19b292dc`  |
| 3177   | Layout 1 | `3a1e19b292dc`  |
| 3169   | Layout 1 | `3a1e19b292dc`  |
| 3158   | Layout 1 | `3a1e19b292dc`  |
| 3151   | Layout 1 | `3a1e19b292dc`  |
| 3144   | Layout 1 | `3a1e19b292dc`  |
| 3133   | Layout 1 | `3a1e19b292dc`  |
| 3125   | Layout 1 | `3a1e19b292dc`  |
| 3118   | Layout 1 | `3a1e19b292dc`  |
| 3111   | Layout 1 | `3a1e19b292dc`  |
| 3103   | Layout 1 | `3a1e19b292dc`  |
| 3095   | Layout 1 | `3a1e19b292dc`  |
| 3086   | Layout 1 | `3a1e19b292dc`  |
| 3072   | Layout 1 | `3a1e19b292dc`  |
| 3062   | Layout 1 | `3a1e19b292dc`  |
| 3052   | Layout 1 | `3a1e19b292dc`  |
| 3045   | Layout 1 | `3a1e19b292dc`  |
| 3037   | Layout 1 | `3a1e19b292dc`  |
| 3030   | Layout 1 | `3a1e19b292dc`  |
| 3021   | Layout 1 | `3a1e19b292dc`  |
| 3012   | Layout 1 | `3a1e19b292dc`  |
| 3002   | Layout 1 | `3a1e19b292dc`  |
| 2995   | Layout 1 | `3a1e19b292dc`  |
| 2987   | Layout 1 | `3a1e19b292dc`  |
| 2978   | No file  | `3a1e19b292dc`  |
| 2970   | No file  | `3a1e19b292dc`  |
| 2959   | No file  | `3a1e19b292dc`  |
| 2951   | No file  | `3a1e19b292dc`  |
| 2942   | No file  | `3a1e19b292dc`  |
| 2935   | No file  | `3a1e19b292dc`  |
| 2932   | No file  | `3a1e19b292dc`  |
| 2923   | No file  | `3a1e19b292dc`  |
| 2919   | No file  | `3a1e19b292dc`  |
| 2907   | No file  | `3a1e19b292dc`  |
| 2900   | No file  | `3a1e19b292dc`  |
| 2891   | No file  | `3a1e19b292dc`  |
| 2882   | No file  | `3a1e19b292dc`  |
| 2872   | No file  | `3a1e19b292dc`  |
| 2863   | No file  | `3a1e19b292dc`  |
| 2855   | No file  | `3a1e19b292dc`  |
| 2849   | No file  | `3a1e19b292dc`  |
| 2844   | No file  | `3a1e19b292dc`  |
| 2834   | No file  | `3a1e19b292dc`  |
| 2825   | No file  | `3a1e19b292dc`  |
| 2819   | No file  | `3a1e19b292dc`  |
| 2811   | No file  | `3a1e19b292dc`  |
| 2803   | No file  | `3a1e19b292dc`  |
| 2794   | No file  | `3a1e19b292dc`  |
| 2783   | No file  | `3a1e19b292dc`  |
| 2774   | No file  | `3a1e19b292dc`  |
| 2765   | No file  | `3a1e19b292dc`  |
| 2756   | No file  | `3a1e19b292dc`  |
| 2750   | No file  | `3a1e19b292dc`  |
| 2743   | No file  | `3a1e19b292dc`  |
| 2736   | No file  | `3a1e19b292dc`  |
| 2726   | No file  | `3a1e19b292dc`  |
| 2717   | No file  | `3a1e19b292dc`  |
| 2709   | No file  | `3a1e19b292dc`  |
| 2703   | No file  | `3a1e19b292dc`  |
| 2695   | No file  | `3a1e19b292dc`  |
| 2684   | No file  | `3a1e19b292dc`  |
| 2672   | No file  | `3a1e19b292dc`  |
| 2665   | No file  | `3a1e19b292dc`  |
| 2657   | No file  | `3a1e19b292dc`  |
| 2649   | No file  | `3a1e19b292dc`  |
| 2644   | No file  | `3a1e19b292dc`  |
| 2637   | No file  | `3a1e19b292dc`  |
| 2629   | No file  | `3a1e19b292dc`  |
| 2619   | No file  | `3a1e19b292dc`  |
| 2612   | No file  | `3a1e19b292dc`  |
| 2606   | No file  | `3a1e19b292dc`  |
| 2602   | No file  | `3a1e19b292dc`  |
| 2601   | No file  | `3a1e19b292dc`  |
| 2592   | No file  | `3a1e19b292dc`  |
| 2583   | No file  | `3a1e19b292dc`  |
| 2575   | No file  | `3a1e19b292dc`  |
| 2567   | No file  | `3a1e19b292dc`  |
| 2560   | No file  | `3a1e19b292dc`  |
| 2553   | No file  | `3a1e19b292dc`  |
| 2545   | No file  | `3a1e19b292dc`  |
| 2538   | No file  | `3a1e19b292dc`  |
| 2529   | No file  | `3a1e19b292dc`  |
| 2519   | No file  | `3a1e19b292dc`  |
| 2513   | No file  | `3a1e19b292dc`  |
| 2510   | No file  | `3a1e19b292dc`  |
| 2507   | No file  | `3a1e19b292dc`  |
| 2503   | No file  | `3a1e19b292dc`  |
| 2498   | No file  | `3a1e19b292dc`  |
| 2492   | No file  | `3a1e19b292dc`  |
| 2487   | No file  | `3a1e19b292dc`  |
| 2480   | No file  | `3a1e19b292dc`  |
| 2474   | No file  | `3a1e19b292dc`  |
| 2468   | No file  | `3a1e19b292dc`  |
| 2460   | No file  | `3a1e19b292dc`  |
| 2453   | No file  | `3a1e19b292dc`  |
| 2444   | No file  | `3a1e19b292dc`  |
| 2438   | No file  | `3a1e19b292dc`  |
| 2434   | No file  | `3a1e19b292dc`  |
| 2429   | No file  | `3a1e19b292dc`  |
| 2421   | No file  | `3a1e19b292dc`  |
| 2414   | No file  | `3a1e19b292dc`  |
| 2407   | No file  | `3a1e19b292dc`  |
| 2401   | No file  | `3a1e19b292dc`  |
| 2397   | No file  | `3a1e19b292dc`  |
| 2393   | No file  | `3a1e19b292dc`  |
| 2384   | No file  | `3a1e19b292dc`  |
| 2378   | No file  | `3a1e19b292dc`  |
| 2372   | No file  | `3a1e19b292dc`  |
| 2358   | No file  | `3a1e19b292dc`  |
| 2352   | No file  | `3a1e19b292dc`  |
| 2347   | No file  | `3a1e19b292dc`  |
| 2343   | No file  | `3a1e19b292dc`  |
| 2335   | No file  | `3a1e19b292dc`  |
| 2327   | No file  | `3a1e19b292dc`  |
| 2324   | No file  | `3a1e19b292dc`  |
| 2319   | No file  | `3a1e19b292dc`  |
| 2313   | No file  | `3a1e19b292dc`  |
| 2308   | No file  | `3a1e19b292dc`  |
| 2302   | No file  | `3a1e19b292dc`  |
| 2295   | No file  | `3a1e19b292dc`  |
| 2290   | No file  | `3a1e19b292dc`  |
| 2284   | No file  | `3a1e19b292dc`  |
| 2276   | No file  | `3a1e19b292dc`  |
| 2269   | No file  | `3a1e19b292dc`  |
| 2259   | No file  | `3a1e19b292dc`  |
| 2250   | No file  | `3a1e19b292dc`  |
| 2243   | No file  | `3a1e19b292dc`  |
| 2235   | No file  | `3a1e19b292dc`  |
| 2229   | No file  | `3a1e19b292dc`  |
| 2224   | No file  | `3a1e19b292dc`  |
| 2218   | No file  | `3a1e19b292dc`  |
| 2215   | No file  | `3a1e19b292dc`  |
| 2207   | No file  | `3a1e19b292dc`  |
| 2203   | No file  | `3a1e19b292dc`  |
| 2196   | No file  | `3a1e19b292dc`  |
| 2192   | No file  | `3a1e19b292dc`  |
| 2189   | No file  | `3a1e19b292dc`  |
| 2183   | No file  | `3a1e19b292dc`  |
| 2179   | No file  | `3a1e19b292dc`  |
| 2171   | No file  | `3a1e19b292dc`  |
| 2163   | No file  | `3a1e19b292dc`  |
| 2156   | No file  | `3a1e19b292dc`  |
| 2151   | No file  | `3a1e19b292dc`  |
| 2147   | No file  | `3a1e19b292dc`  |
| 2142   | No file  | `3a1e19b292dc`  |
| 2138   | No file  | `3a1e19b292dc`  |
| 2134   | No file  | `3a1e19b292dc`  |
| 2130   | No file  | `3a1e19b292dc`  |
| 2122   | No file  | `3a1e19b292dc`  |
| 2107   | No file  | `3a1e19b292dc`  |
| 2098   | No file  | `3a1e19b292dc`  |
| 2089   | No file  | `3a1e19b292dc`  |
| 2081   | No file  | `3a1e19b292dc`  |
| 2073   | No file  | `3a1e19b292dc`  |
| 2067   | No file  | `3a1e19b292dc`  |
| 2063   | No file  | `3a1e19b292dc`  |
| 2059   | No file  | `3a1e19b292dc`  |
| 2052   | No file  | `3a1e19b292dc`  |
| 2044   | No file  | `3a1e19b292dc`  |
| 2039   | No file  | `3a1e19b292dc`  |
| 2032   | No file  | `3a1e19b292dc`  |
| 2025   | No file  | `3a1e19b292dc`  |
| 2011   | No file  | `3a1e19b292dc`  |
| 2005   | No file  | `3a1e19b292dc`  |
| 2000   | No file  | `3a1e19b292dc`  |
| 1996   | No file  | `3a1e19b292dc`  |
| 1991   | No file  | `3a1e19b292dc`  |
| 1985   | No file  | `3a1e19b292dc`  |
| 1980   | No file  | `3a1e19b292dc`  |
| 1969   | No file  | `3a1e19b292dc`  |
| 1964   | No file  | `3a1e19b292dc`  |
| 1958   | No file  | `3a1e19b292dc`  |
| 1950   | No file  | `3a1e19b292dc`  |
| 1945   | No file  | `3a1e19b292dc`  |
| 1937   | No file  | `3a1e19b292dc`  |
| 1933   | No file  | `3a1e19b292dc`  |
| 1927   | No file  | `3a1e19b292dc`  |
| 1921   | No file  | `3a1e19b292dc`  |
| 1914   | No file  | `3a1e19b292dc`  |
| 1908   | No file  | `3a1e19b292dc`  |
| 1897   | No file  | `3a1e19b292dc`  |
| 1892   | No file  | `3a1e19b292dc`  |
| 1886   | No file  | `3a1e19b292dc`  |
| 1881   | No file  | `3a1e19b292dc`  |
| 1871   | No file  | `3a1e19b292dc`  |
| 1866   | No file  | `3a1e19b292dc`  |
| 1862   | No file  | `3a1e19b292dc`  |
| 1854   | No file  | `3a1e19b292dc`  |
| 1846   | No file  | `3a1e19b292dc`  |
| 1838   | No file  | `3a1e19b292dc`  |
| 1832   | No file  | `3a1e19b292dc`  |
| 1826   | No file  | `3a1e19b292dc`  |
| 1822   | No file  | `3a1e19b292dc`  |
| 1818   | No file  | `3a1e19b292dc`  |
| 1804   | No file  | `3a1e19b292dc`  |
| 1794   | No file  | `3a1e19b292dc`  |
| 1790   | No file  | `3a1e19b292dc`  |
| 1784   | No file  | `3a1e19b292dc`  |
| 1774   | No file  | `3a1e19b292dc`  |
| 1771   | No file  | `3a1e19b292dc`  |
| 1762   | No file  | `3a1e19b292dc`  |
| 1759   | No file  | `3a1e19b292dc`  |
| 1754   | No file  | `3a1e19b292dc`  |
| 1749   | No file  | `3a1e19b292dc`  |
| 1743   | No file  | `3a1e19b292dc`  |
| 1737   | No file  | `3a1e19b292dc`  |
| 1731   | No file  | `3a1e19b292dc`  |
| 1725   | No file  | `3a1e19b292dc`  |
| 1717   | No file  | `3a1e19b292dc`  |
| 1710   | No file  | `3a1e19b292dc`  |
| 1704   | No file  | `3a1e19b292dc`  |
| 1698   | No file  | `3a1e19b292dc`  |
| 1690   | No file  | `3a1e19b292dc`  |
| 1685   | No file  | `3a1e19b292dc`  |
| 1680   | No file  | `3a1e19b292dc`  |
| 1674   | No file  | `3a1e19b292dc`  |
| 1668   | No file  | `3a1e19b292dc`  |
| 1659   | No file  | `3a1e19b292dc`  |
| 1649   | No file  | `3a1e19b292dc`  |
| 1642   | No file  | `3a1e19b292dc`  |
| 1636   | No file  | `3a1e19b292dc`  |
| 1628   | No file  | `3a1e19b292dc`  |
| 1622   | No file  | `3a1e19b292dc`  |
| 1614   | No file  | `3a1e19b292dc`  |
| 1608   | No file  | `3a1e19b292dc`  |
| 1602   | No file  | `3a1e19b292dc`  |
| 1598   | No file  | `3a1e19b292dc`  |
| 1594   | No file  | `3a1e19b292dc`  |
| 1590   | No file  | `3a1e19b292dc`  |
| 1587   | No file  | `3a1e19b292dc`  |
| 1584   | No file  | `3a1e19b292dc`  |
| 1579   | No file  | `3a1e19b292dc`  |
| 1572   | No file  | `3a1e19b292dc`  |
| 1565   | No file  | `3a1e19b292dc`  |
| 1559   | No file  | `3a1e19b292dc`  |
| 1554   | No file  | `3a1e19b292dc`  |
| 1547   | No file  | `3a1e19b292dc`  |
| 1537   | No file  | `3a1e19b292dc`  |
| 1529   | No file  | `3a1e19b292dc`  |
| 1524   | No file  | `3a1e19b292dc`  |
| 1519   | No file  | `3a1e19b292dc`  |
| 1509   | No file  | `3a1e19b292dc`  |
| 1506   | No file  | `3a1e19b292dc`  |
| 1504   | No file  | `3a1e19b292dc`  |
| 1500   | No file  | `3a1e19b292dc`  |
| 1493   | No file  | `3a1e19b292dc`  |
| 1489   | No file  | `3a1e19b292dc`  |
| 1485   | No file  | `3a1e19b292dc`  |
| 1481   | No file  | `3a1e19b292dc`  |
| 1474   | No file  | `3a1e19b292dc`  |
| 1466   | No file  | `3a1e19b292dc`  |
| 1462   | No file  | `3a1e19b292dc`  |
| 1459   | No file  | `3a1e19b292dc`  |
| 1453   | No file  | `3a1e19b292dc`  |
| 1450   | No file  | `3a1e19b292dc`  |
| 1445   | No file  | `3a1e19b292dc`  |
| 1439   | No file  | `3a1e19b292dc`  |
| 1433   | No file  | `3a1e19b292dc`  |
| 1430   | No file  | `3a1e19b292dc`  |
| 1426   | No file  | `3a1e19b292dc`  |
| 1421   | No file  | `3a1e19b292dc`  |
| 1417   | No file  | `3a1e19b292dc`  |
| 1416   | No file  | `3a1e19b292dc`  |
| 1409   | No file  | `3a1e19b292dc`  |
| 1405   | No file  | `3a1e19b292dc`  |
| 1401   | No file  | `3a1e19b292dc`  |
| 1396   | No file  | `3a1e19b292dc`  |
| 1391   | No file  | `3a1e19b292dc`  |
| 1390   | No file  | `3a1e19b292dc`  |
| 1386   | No file  | `3a1e19b292dc`  |
| 1381   | No file  | `3a1e19b292dc`  |
| 1379   | No file  | `3a1e19b292dc`  |
| 1372   | No file  | `3a1e19b292dc`  |
| 1366   | No file  | `3a1e19b292dc`  |
| 1364   | No file  | `3a1e19b292dc`  |
| 1363   | No file  | `3a1e19b292dc`  |
| 1360   | No file  | `3a1e19b292dc`  |
| 1358   | No file  | `3a1e19b292dc`  |
| 1355   | No file  | `3a1e19b292dc`  |
| 1351   | No file  | `3a1e19b292dc`  |
| 1348   | No file  | `3a1e19b292dc`  |
| 1346   | No file  | `3a1e19b292dc`  |
| 1341   | No file  | `3a1e19b292dc`  |
| 1340   | No file  | `3a1e19b292dc`  |
| 1338   | No file  | `3a1e19b292dc`  |
| 1335   | No file  | `3a1e19b292dc`  |
| 1333   | No file  | `3a1e19b292dc`  |
| 1329   | No file  | `3a1e19b292dc`  |
| 1327   | No file  | `3a1e19b292dc`  |
| 1324   | No file  | `3a1e19b292dc`  |
| 1321   | No file  | `3a1e19b292dc`  |
| 1319   | No file  | `3a1e19b292dc`  |
| 1318   | No file  | `3a1e19b292dc`  |
| 1316   | No file  | `3a1e19b292dc`  |
| 1313   | No file  | `3a1e19b292dc`  |
| 1311   | No file  | `3a1e19b292dc`  |
| 1309   | No file  | `3a1e19b292dc`  |
| 1304   | No file  | `3a1e19b292dc`  |
| 1292   | No file  | `3a1e19b292dc`  |
| 1286   | No file  | `3a1e19b292dc`  |
| 1280   | No file  | `3a1e19b292dc`  |
| 1276   | No file  | `3a1e19b292dc`  |
| 1267   | No file  | `3a1e19b292dc`  |
| 1261   | No file  | `3a1e19b292dc`  |
| 1256   | No file  | `3a1e19b292dc`  |
| 1250   | No file  | `3a1e19b292dc`  |
| 1246   | No file  | `3a1e19b292dc`  |
| 1239   | No file  | `3a1e19b292dc`  |
| 1230   | No file  | `3a1e19b292dc`  |
| 1226   | No file  | `3a1e19b292dc`  |
| 1220   | No file  | `3a1e19b292dc`  |
| 1217   | No file  | `3a1e19b292dc`  |
| 1211   | No file  | `3a1e19b292dc`  |
| 1210   | No file  | `3a1e19b292dc`  |
| 1208   | No file  | `3a1e19b292dc`  |
| 1203   | No file  | `3a1e19b292dc`  |
| 1197   | No file  | `3a1e19b292dc`  |
| 1194   | No file  | `3a1e19b292dc`  |
| 1192   | No file  | `3a1e19b292dc`  |
| 1187   | No file  | `3a1e19b292dc`  |
| 1183   | No file  | `3a1e19b292dc`  |
| 1177   | No file  | `3a1e19b292dc`  |
| 1173   | No file  | `3a1e19b292dc`  |
| 1167   | No file  | `3a1e19b292dc`  |
| 1164   | No file  | `3a1e19b292dc`  |
| 1156   | No file  | `3a1e19b292dc`  |
| 1149   | No file  | `3a1e19b292dc`  |
| 1144   | No file  | `3a1e19b292dc`  |
| 1137   | No file  | `3a1e19b292dc`  |
| 1132   | No file  | `3a1e19b292dc`  |
| 1127   | No file  | `3a1e19b292dc`  |
| 1122   | No file  | `3a1e19b292dc`  |
| 1118   | No file  | `3a1e19b292dc`  |
| 1114   | No file  | `3a1e19b292dc`  |
| 1109   | No file  | `3a1e19b292dc`  |
| 1102   | No file  | `3a1e19b292dc`  |
| 1096   | No file  | `3a1e19b292dc`  |
| 1088   | No file  | `3a1e19b292dc`  |
| 1081   | No file  | `3a1e19b292dc`  |
| 1076   | No file  | `3a1e19b292dc`  |
| 1069   | No file  | `3a1e19b292dc`  |
| 1064   | No file  | `3a1e19b292dc`  |
| 1058   | No file  | `3a1e19b292dc`  |
| 1051   | No file  | `3a1e19b292dc`  |
| 1044   | No file  | `3a1e19b292dc`  |
| 1036   | No file  | `3a1e19b292dc`  |
| 1026   | No file  | `3a1e19b292dc`  |
| 1016   | No file  | `3a1e19b292dc`  |
| 1009   | No file  | `3a1e19b292dc`  |
| 1005   | No file  | `3a1e19b292dc`  |
| 1000   | No file  | `3a1e19b292dc`  |
| 998    | No file  | `3a1e19b292dc`  |
| 990    | No file  | `3a1e19b292dc`  |
| 979    | No file  | `3a1e19b292dc`  |
| 972    | No file  | `3a1e19b292dc`  |
| 963    | No file  | `3a1e19b292dc`  |
| 955    | No file  | `3a1e19b292dc`  |
| 946    | No file  | `3a1e19b292dc`  |
| 938    | No file  | `3a1e19b292dc`  |
| 927    | No file  | `3a1e19b292dc`  |
| 911    | No file  | `3a1e19b292dc`  |
| 904    | No file  | `3a1e19b292dc`  |
| 899    | No file  | `3a1e19b292dc`  |
| 894    | No file  | `3a1e19b292dc`  |
| 885    | No file  | `3a1e19b292dc`  |
| 879    | No file  | `3a1e19b292dc`  |
| 872    | No file  | `3a1e19b292dc`  |
| 864    | No file  | `3a1e19b292dc`  |
| 855    | No file  | `3a1e19b292dc`  |
| 853    | No file  | `3a1e19b292dc`  |
| 845    | No file  | `3a1e19b292dc`  |
| 837    | No file  | `3a1e19b292dc`  |
| 829    | No file  | `3a1e19b292dc`  |
| 822    | No file  | `3a1e19b292dc`  |
| 814    | No file  | `3a1e19b292dc`  |
| 805    | No file  | `3a1e19b292dc`  |
| 794    | No file  | `3a1e19b292dc`  |
| 787    | No file  | `3a1e19b292dc`  |
| 780    | No file  | `3a1e19b292dc`  |
| 771    | No file  | `3a1e19b292dc`  |
| 760    | No file  | `3a1e19b292dc`  |
| 748    | No file  | `3a1e19b292dc`  |
| 741    | No file  | `3a1e19b292dc`  |
| 736    | No file  | `3a1e19b292dc`  |
| 731    | No file  | `3a1e19b292dc`  |
| 723    | No file  | `3a1e19b292dc`  |
| 711    | No file  | `3a1e19b292dc`  |
| 707    | No file  | `3a1e19b292dc`  |
| 697    | No file  | `3a1e19b292dc`  |
| 689    | No file  | `3a1e19b292dc`  |
| 683    | No file  | `3a1e19b292dc`  |
| 678    | No file  | `3a1e19b292dc`  |
| 670    | No file  | `3a1e19b292dc`  |
| 661    | No file  | `3a1e19b292dc`  |
| 656    | No file  | `3a1e19b292dc`  |
| 652    | No file  | `3a1e19b292dc`  |
| 643    | No file  | `3a1e19b292dc`  |
| 637    | No file  | `3a1e19b292dc`  |
| 630    | No file  | `3a1e19b292dc`  |
| 627    | No file  | `3a1e19b292dc`  |
| 621    | No file  | `3a1e19b292dc`  |
| 617    | No file  | `3a1e19b292dc`  |
| 615    | No file  | `3a1e19b292dc`  |
| 606    | No file  | `3a1e19b292dc`  |
| 599    | No file  | `3a1e19b292dc`  |
| 592    | No file  | `3a1e19b292dc`  |
| 586    | No file  | `3a1e19b292dc`  |
| 577    | No file  | `3a1e19b292dc`  |
| 569    | No file  | `3a1e19b292dc`  |
| 561    | No file  | `3a1e19b292dc`  |
| 554    | No file  | `3a1e19b292dc`  |
| 542    | No file  | `3a1e19b292dc`  |
| 532    | No file  | `3a1e19b292dc`  |
| 531    | No file  | `3a1e19b292dc`  |
| 526    | No file  | `3a1e19b292dc`  |
| 521    | No file  | `3a1e19b292dc`  |
| 517    | No file  | `3a1e19b292dc`  |
| 510    | No file  | `3a1e19b292dc`  |
| 508    | No file  | `3a1e19b292dc`  |
| 504    | No file  | `3a1e19b292dc`  |
| 497    | No file  | `3a1e19b292dc`  |
| 491    | No file  | `3a1e19b292dc`  |
| 485    | No file  | `3a1e19b292dc`  |
| 478    | No file  | `3a1e19b292dc`  |
| 472    | No file  | `3a1e19b292dc`  |
| 466    | No file  | `3a1e19b292dc`  |
| 457    | No file  | `3a1e19b292dc`  |
| 452    | No file  | `3a1e19b292dc`  |
| 449    | No file  | `3a1e19b292dc`  |
| 435    | No file  | `3a1e19b292dc`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table: a row count, then the rows back to
back to the end of the file.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 32 bytes + model name)

| Offset                       | Type | Field                            | Notes                                                                    |
| ---------------------------- | ---- | -------------------------------- | ------------------------------------------------------------------------ |
| `+0x00`                      | u16  | deco_index                       | Row key; each key once                                                   |
| `+0x02`                      | str8 | world_map_object_file            | Model file name (`WofldMap_Velia_House_01.pam`, sic)                     |
| `world_map_object_file+0x00` | f32  | location_x                       | World position                                                           |
| `world_map_object_file+0x04` | f32  | location_y                       | World position, height                                                   |
| `world_map_object_file+0x08` | f32  | location_z                       | World position                                                           |
| `world_map_object_file+0x0C` | f32  | scale                            | Percent: `100` on 600 of 657 rows (client 3482), also `50`, `70`, `80`, `150` |
| `world_map_object_file+0x10` | f32  | rotation                         | Degrees (`96.27`, `-93`, `180`); `0` on 419 of 657 rows (client 3482)    |
| `world_map_object_file+0x14` | u16  | unknown_world_map_object_file_14 | `1` on every row of clients 3002 and 3482                                |

The rows are in no key order: client 3482 opens with keys 2049, 1, 1025,
513 and 2050. Keys run from 1 to 2187 with gaps.

## Field Names

The `WorlmapDeco_Table` sheet (sic) of a private server's
`DataSheets.bexcel` on client 1784 has the columns `Index`,
`WorldMapObjectFile`, `LocationX`, `LocationY`, `LocationZ`, `Rotation`
and `Scale`. Joined on `Index` = `deco_index`, every column matches on 488
of 488 shared keys (client 3482); the file stores `Scale` before
`Rotation`. The table of the same name of a private server on client 519
matches on 453 of 455 keys for the position and on 455 of 455 for scale
and rotation; its keys `1975` and `1976` hold other models or positions.
No column of either source holds the trailing u16.

## Notes

- Client 3002 is the first test client with the file, 605 rows; client
  2959 and older have none.

## Open Questions

### Trailing U16

`unknown_world_map_object_file_14` is `1` on every row and neither source
has a column for it. A visibility flag or a layer number would both fit; a
row with another value would tell them apart.
