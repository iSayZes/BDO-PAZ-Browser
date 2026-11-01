# `horsemap.bss` Format

## Purpose

The speed zones of the horse race course: per colour of the course map
`ui_texture/minimap/area/horseracecoursemap.bmp` the share of the horse's
speed that applies where the map has that colour. The server dump of a
private server on client 1784 names the row `HorseRaceMapStaticStatus` and
logs it as `RGB(%#,%#,%#) _horseSpeedApplyRate(%#)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File           | Bytes | Records | Row bytes |
| ------ | -------------- | -------------- | ----- | ------- | --------- |
| 1      | 1489 and later | `horsemap.bss` | 80    | 5 Row   | 12        |

| Layout | File           | Known        | Unknown      |
| ------ | -------------- | ------------ | ------------ |
| 1      | `horsemap.bss` | 70 B (87.5%) | 10 B (12.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `86cba8f43143`  |
| 3482   | Layout 1 | `86cba8f43143`  |
| 3474   | Layout 1 | `86cba8f43143`  |
| 3473   | Layout 1 | `86cba8f43143`  |
| 3464   | Layout 1 | `86cba8f43143`  |
| 3458   | Layout 1 | `86cba8f43143`  |
| 3454   | Layout 1 | `86cba8f43143`  |
| 3444   | Layout 1 | `86cba8f43143`  |
| 3435   | Layout 1 | `86cba8f43143`  |
| 3426   | Layout 1 | `86cba8f43143`  |
| 3418   | Layout 1 | `86cba8f43143`  |
| 3412   | Layout 1 | `86cba8f43143`  |
| 3402   | Layout 1 | `86cba8f43143`  |
| 3396   | Layout 1 | `86cba8f43143`  |
| 3387   | Layout 1 | `86cba8f43143`  |
| 3381   | Layout 1 | `86cba8f43143`  |
| 3373   | Layout 1 | `86cba8f43143`  |
| 3364   | Layout 1 | `86cba8f43143`  |
| 3356   | Layout 1 | `86cba8f43143`  |
| 3349   | Layout 1 | `86cba8f43143`  |
| 3342   | Layout 1 | `86cba8f43143`  |
| 3335   | Layout 1 | `86cba8f43143`  |
| 3326   | Layout 1 | `86cba8f43143`  |
| 3321   | Layout 1 | `86cba8f43143`  |
| 3314   | Layout 1 | `86cba8f43143`  |
| 3303   | Layout 1 | `86cba8f43143`  |
| 3302   | Layout 1 | `86cba8f43143`  |
| 3293   | Layout 1 | `86cba8f43143`  |
| 3283   | Layout 1 | `86cba8f43143`  |
| 3275   | Layout 1 | `86cba8f43143`  |
| 3267   | Layout 1 | `86cba8f43143`  |
| 3258   | Layout 1 | `86cba8f43143`  |
| 3251   | Layout 1 | `86cba8f43143`  |
| 3242   | Layout 1 | `86cba8f43143`  |
| 3235   | Layout 1 | `86cba8f43143`  |
| 3229   | Layout 1 | `86cba8f43143`  |
| 3212   | Layout 1 | `86cba8f43143`  |
| 3203   | Layout 1 | `86cba8f43143`  |
| 3193   | Layout 1 | `86cba8f43143`  |
| 3186   | Layout 1 | `86cba8f43143`  |
| 3177   | Layout 1 | `86cba8f43143`  |
| 3169   | Layout 1 | `86cba8f43143`  |
| 3158   | Layout 1 | `86cba8f43143`  |
| 3151   | Layout 1 | `86cba8f43143`  |
| 3144   | Layout 1 | `86cba8f43143`  |
| 3133   | Layout 1 | `86cba8f43143`  |
| 3125   | Layout 1 | `86cba8f43143`  |
| 3118   | Layout 1 | `86cba8f43143`  |
| 3111   | Layout 1 | `86cba8f43143`  |
| 3103   | Layout 1 | `86cba8f43143`  |
| 3095   | Layout 1 | `86cba8f43143`  |
| 3086   | Layout 1 | `86cba8f43143`  |
| 3072   | Layout 1 | `86cba8f43143`  |
| 3062   | Layout 1 | `86cba8f43143`  |
| 3052   | Layout 1 | `86cba8f43143`  |
| 3045   | Layout 1 | `86cba8f43143`  |
| 3037   | Layout 1 | `86cba8f43143`  |
| 3030   | Layout 1 | `86cba8f43143`  |
| 3021   | Layout 1 | `86cba8f43143`  |
| 3012   | Layout 1 | `86cba8f43143`  |
| 3002   | Layout 1 | `86cba8f43143`  |
| 2995   | Layout 1 | `86cba8f43143`  |
| 2987   | Layout 1 | `86cba8f43143`  |
| 2978   | Layout 1 | `86cba8f43143`  |
| 2970   | Layout 1 | `86cba8f43143`  |
| 2959   | Layout 1 | `86cba8f43143`  |
| 2951   | Layout 1 | `86cba8f43143`  |
| 2942   | Layout 1 | `86cba8f43143`  |
| 2935   | Layout 1 | `86cba8f43143`  |
| 2932   | Layout 1 | `86cba8f43143`  |
| 2923   | Layout 1 | `86cba8f43143`  |
| 2919   | Layout 1 | `86cba8f43143`  |
| 2907   | Layout 1 | `86cba8f43143`  |
| 2900   | Layout 1 | `86cba8f43143`  |
| 2891   | Layout 1 | `86cba8f43143`  |
| 2882   | Layout 1 | `86cba8f43143`  |
| 2872   | Layout 1 | `86cba8f43143`  |
| 2863   | Layout 1 | `86cba8f43143`  |
| 2855   | Layout 1 | `86cba8f43143`  |
| 2849   | Layout 1 | `86cba8f43143`  |
| 2844   | Layout 1 | `86cba8f43143`  |
| 2834   | Layout 1 | `86cba8f43143`  |
| 2825   | Layout 1 | `86cba8f43143`  |
| 2819   | Layout 1 | `86cba8f43143`  |
| 2811   | Layout 1 | `86cba8f43143`  |
| 2803   | Layout 1 | `86cba8f43143`  |
| 2794   | Layout 1 | `86cba8f43143`  |
| 2783   | Layout 1 | `86cba8f43143`  |
| 2774   | Layout 1 | `86cba8f43143`  |
| 2765   | Layout 1 | `86cba8f43143`  |
| 2756   | Layout 1 | `86cba8f43143`  |
| 2750   | Layout 1 | `86cba8f43143`  |
| 2743   | Layout 1 | `86cba8f43143`  |
| 2736   | Layout 1 | `86cba8f43143`  |
| 2726   | Layout 1 | `86cba8f43143`  |
| 2717   | Layout 1 | `86cba8f43143`  |
| 2709   | Layout 1 | `86cba8f43143`  |
| 2703   | Layout 1 | `86cba8f43143`  |
| 2695   | Layout 1 | `86cba8f43143`  |
| 2684   | Layout 1 | `86cba8f43143`  |
| 2672   | Layout 1 | `86cba8f43143`  |
| 2665   | Layout 1 | `86cba8f43143`  |
| 2657   | Layout 1 | `86cba8f43143`  |
| 2649   | Layout 1 | `86cba8f43143`  |
| 2644   | Layout 1 | `86cba8f43143`  |
| 2637   | Layout 1 | `86cba8f43143`  |
| 2629   | Layout 1 | `86cba8f43143`  |
| 2619   | Layout 1 | `86cba8f43143`  |
| 2612   | Layout 1 | `86cba8f43143`  |
| 2606   | Layout 1 | `86cba8f43143`  |
| 2602   | Layout 1 | `86cba8f43143`  |
| 2601   | Layout 1 | `86cba8f43143`  |
| 2592   | Layout 1 | `86cba8f43143`  |
| 2583   | Layout 1 | `86cba8f43143`  |
| 2575   | Layout 1 | `86cba8f43143`  |
| 2567   | Layout 1 | `86cba8f43143`  |
| 2560   | Layout 1 | `86cba8f43143`  |
| 2553   | Layout 1 | `86cba8f43143`  |
| 2545   | Layout 1 | `86cba8f43143`  |
| 2538   | Layout 1 | `86cba8f43143`  |
| 2529   | Layout 1 | `86cba8f43143`  |
| 2519   | Layout 1 | `86cba8f43143`  |
| 2513   | Layout 1 | `86cba8f43143`  |
| 2510   | Layout 1 | `86cba8f43143`  |
| 2507   | Layout 1 | `86cba8f43143`  |
| 2503   | Layout 1 | `86cba8f43143`  |
| 2498   | Layout 1 | `86cba8f43143`  |
| 2492   | Layout 1 | `86cba8f43143`  |
| 2487   | Layout 1 | `86cba8f43143`  |
| 2480   | Layout 1 | `86cba8f43143`  |
| 2474   | Layout 1 | `86cba8f43143`  |
| 2468   | Layout 1 | `86cba8f43143`  |
| 2460   | Layout 1 | `86cba8f43143`  |
| 2453   | Layout 1 | `86cba8f43143`  |
| 2444   | Layout 1 | `86cba8f43143`  |
| 2438   | Layout 1 | `86cba8f43143`  |
| 2434   | Layout 1 | `86cba8f43143`  |
| 2429   | Layout 1 | `86cba8f43143`  |
| 2421   | Layout 1 | `86cba8f43143`  |
| 2414   | Layout 1 | `86cba8f43143`  |
| 2407   | Layout 1 | `86cba8f43143`  |
| 2401   | Layout 1 | `86cba8f43143`  |
| 2397   | Layout 1 | `86cba8f43143`  |
| 2393   | Layout 1 | `86cba8f43143`  |
| 2384   | Layout 1 | `86cba8f43143`  |
| 2378   | Layout 1 | `86cba8f43143`  |
| 2372   | Layout 1 | `86cba8f43143`  |
| 2358   | Layout 1 | `86cba8f43143`  |
| 2352   | Layout 1 | `86cba8f43143`  |
| 2347   | Layout 1 | `86cba8f43143`  |
| 2343   | Layout 1 | `86cba8f43143`  |
| 2335   | Layout 1 | `86cba8f43143`  |
| 2327   | Layout 1 | `86cba8f43143`  |
| 2324   | Layout 1 | `86cba8f43143`  |
| 2319   | Layout 1 | `86cba8f43143`  |
| 2313   | Layout 1 | `86cba8f43143`  |
| 2308   | Layout 1 | `86cba8f43143`  |
| 2302   | Layout 1 | `86cba8f43143`  |
| 2295   | Layout 1 | `86cba8f43143`  |
| 2290   | Layout 1 | `86cba8f43143`  |
| 2284   | Layout 1 | `86cba8f43143`  |
| 2276   | Layout 1 | `86cba8f43143`  |
| 2269   | Layout 1 | `86cba8f43143`  |
| 2259   | Layout 1 | `86cba8f43143`  |
| 2250   | Layout 1 | `86cba8f43143`  |
| 2243   | Layout 1 | `86cba8f43143`  |
| 2235   | Layout 1 | `86cba8f43143`  |
| 2229   | Layout 1 | `86cba8f43143`  |
| 2224   | Layout 1 | `86cba8f43143`  |
| 2218   | Layout 1 | `86cba8f43143`  |
| 2215   | Layout 1 | `86cba8f43143`  |
| 2207   | Layout 1 | `86cba8f43143`  |
| 2203   | Layout 1 | `86cba8f43143`  |
| 2196   | Layout 1 | `86cba8f43143`  |
| 2192   | Layout 1 | `86cba8f43143`  |
| 2189   | Layout 1 | `86cba8f43143`  |
| 2183   | Layout 1 | `86cba8f43143`  |
| 2179   | Layout 1 | `86cba8f43143`  |
| 2171   | Layout 1 | `86cba8f43143`  |
| 2163   | Layout 1 | `86cba8f43143`  |
| 2156   | Layout 1 | `86cba8f43143`  |
| 2151   | Layout 1 | `86cba8f43143`  |
| 2147   | Layout 1 | `86cba8f43143`  |
| 2142   | Layout 1 | `86cba8f43143`  |
| 2138   | Layout 1 | `86cba8f43143`  |
| 2134   | Layout 1 | `86cba8f43143`  |
| 2130   | Layout 1 | `86cba8f43143`  |
| 2122   | Layout 1 | `86cba8f43143`  |
| 2107   | Layout 1 | `86cba8f43143`  |
| 2098   | Layout 1 | `86cba8f43143`  |
| 2089   | Layout 1 | `86cba8f43143`  |
| 2081   | Layout 1 | `86cba8f43143`  |
| 2073   | Layout 1 | `86cba8f43143`  |
| 2067   | Layout 1 | `86cba8f43143`  |
| 2063   | Layout 1 | `86cba8f43143`  |
| 2059   | Layout 1 | `86cba8f43143`  |
| 2052   | Layout 1 | `86cba8f43143`  |
| 2044   | Layout 1 | `86cba8f43143`  |
| 2039   | Layout 1 | `86cba8f43143`  |
| 2032   | Layout 1 | `86cba8f43143`  |
| 2025   | Layout 1 | `86cba8f43143`  |
| 2011   | Layout 1 | `86cba8f43143`  |
| 2005   | Layout 1 | `86cba8f43143`  |
| 2000   | Layout 1 | `86cba8f43143`  |
| 1996   | Layout 1 | `86cba8f43143`  |
| 1991   | Layout 1 | `86cba8f43143`  |
| 1985   | Layout 1 | `86cba8f43143`  |
| 1980   | Layout 1 | `86cba8f43143`  |
| 1969   | Layout 1 | `86cba8f43143`  |
| 1964   | Layout 1 | `86cba8f43143`  |
| 1958   | Layout 1 | `86cba8f43143`  |
| 1950   | Layout 1 | `86cba8f43143`  |
| 1945   | Layout 1 | `86cba8f43143`  |
| 1937   | Layout 1 | `86cba8f43143`  |
| 1933   | Layout 1 | `86cba8f43143`  |
| 1927   | Layout 1 | `86cba8f43143`  |
| 1921   | Layout 1 | `86cba8f43143`  |
| 1914   | Layout 1 | `86cba8f43143`  |
| 1908   | Layout 1 | `86cba8f43143`  |
| 1897   | Layout 1 | `86cba8f43143`  |
| 1892   | Layout 1 | `86cba8f43143`  |
| 1886   | Layout 1 | `86cba8f43143`  |
| 1881   | Layout 1 | `86cba8f43143`  |
| 1871   | Layout 1 | `86cba8f43143`  |
| 1866   | Layout 1 | `86cba8f43143`  |
| 1862   | Layout 1 | `86cba8f43143`  |
| 1854   | Layout 1 | `86cba8f43143`  |
| 1846   | Layout 1 | `86cba8f43143`  |
| 1838   | Layout 1 | `86cba8f43143`  |
| 1832   | Layout 1 | `86cba8f43143`  |
| 1826   | Layout 1 | `86cba8f43143`  |
| 1822   | Layout 1 | `86cba8f43143`  |
| 1818   | Layout 1 | `86cba8f43143`  |
| 1804   | Layout 1 | `86cba8f43143`  |
| 1794   | Layout 1 | `86cba8f43143`  |
| 1790   | Layout 1 | `86cba8f43143`  |
| 1784   | Layout 1 | `86cba8f43143`  |
| 1774   | Layout 1 | `86cba8f43143`  |
| 1771   | Layout 1 | `86cba8f43143`  |
| 1762   | Layout 1 | `86cba8f43143`  |
| 1759   | Layout 1 | `86cba8f43143`  |
| 1754   | Layout 1 | `86cba8f43143`  |
| 1749   | Layout 1 | `86cba8f43143`  |
| 1743   | Layout 1 | `86cba8f43143`  |
| 1737   | Layout 1 | `86cba8f43143`  |
| 1731   | Layout 1 | `86cba8f43143`  |
| 1725   | Layout 1 | `86cba8f43143`  |
| 1717   | Layout 1 | `86cba8f43143`  |
| 1710   | Layout 1 | `86cba8f43143`  |
| 1704   | Layout 1 | `86cba8f43143`  |
| 1698   | Layout 1 | `86cba8f43143`  |
| 1690   | Layout 1 | `86cba8f43143`  |
| 1685   | Layout 1 | `86cba8f43143`  |
| 1680   | Layout 1 | `86cba8f43143`  |
| 1674   | Layout 1 | `86cba8f43143`  |
| 1668   | Layout 1 | `86cba8f43143`  |
| 1659   | Layout 1 | `86cba8f43143`  |
| 1649   | Layout 1 | `86cba8f43143`  |
| 1642   | Layout 1 | `86cba8f43143`  |
| 1636   | Layout 1 | `86cba8f43143`  |
| 1628   | Layout 1 | `86cba8f43143`  |
| 1622   | Layout 1 | `86cba8f43143`  |
| 1614   | Layout 1 | `86cba8f43143`  |
| 1608   | Layout 1 | `86cba8f43143`  |
| 1602   | Layout 1 | `86cba8f43143`  |
| 1598   | Layout 1 | `86cba8f43143`  |
| 1594   | Layout 1 | `86cba8f43143`  |
| 1590   | Layout 1 | `86cba8f43143`  |
| 1587   | Layout 1 | `86cba8f43143`  |
| 1584   | Layout 1 | `86cba8f43143`  |
| 1579   | Layout 1 | `86cba8f43143`  |
| 1572   | Layout 1 | `86cba8f43143`  |
| 1565   | Layout 1 | `86cba8f43143`  |
| 1559   | Layout 1 | `86cba8f43143`  |
| 1554   | Layout 1 | `86cba8f43143`  |
| 1547   | Layout 1 | `86cba8f43143`  |
| 1537   | Layout 1 | `86cba8f43143`  |
| 1529   | Layout 1 | `86cba8f43143`  |
| 1524   | Layout 1 | `86cba8f43143`  |
| 1519   | Layout 1 | `86cba8f43143`  |
| 1509   | Layout 1 | `86cba8f43143`  |
| 1506   | Layout 1 | `86cba8f43143`  |
| 1504   | Layout 1 | `86cba8f43143`  |
| 1500   | Layout 1 | `86cba8f43143`  |
| 1493   | Layout 1 | `86cba8f43143`  |
| 1489   | Layout 1 | `86cba8f43143`  |
| 1485   | No file  | `86cba8f43143`  |
| 1481   | No file  | `86cba8f43143`  |
| 1474   | No file  | `86cba8f43143`  |
| 1466   | No file  | `86cba8f43143`  |
| 1462   | No file  | `86cba8f43143`  |
| 1459   | No file  | `86cba8f43143`  |
| 1453   | No file  | `86cba8f43143`  |
| 1450   | No file  | `86cba8f43143`  |
| 1445   | No file  | `86cba8f43143`  |
| 1439   | No file  | `86cba8f43143`  |
| 1433   | No file  | `86cba8f43143`  |
| 1430   | No file  | `86cba8f43143`  |
| 1426   | No file  | `86cba8f43143`  |
| 1421   | No file  | `86cba8f43143`  |
| 1417   | No file  | `86cba8f43143`  |
| 1416   | No file  | `86cba8f43143`  |
| 1409   | No file  | `86cba8f43143`  |
| 1405   | No file  | `86cba8f43143`  |
| 1401   | No file  | `86cba8f43143`  |
| 1396   | No file  | `86cba8f43143`  |
| 1391   | No file  | `86cba8f43143`  |
| 1390   | No file  | `86cba8f43143`  |
| 1386   | No file  | `86cba8f43143`  |
| 1381   | No file  | `86cba8f43143`  |
| 1379   | No file  | `86cba8f43143`  |
| 1372   | No file  | `86cba8f43143`  |
| 1366   | No file  | `86cba8f43143`  |
| 1364   | No file  | `86cba8f43143`  |
| 1363   | No file  | `86cba8f43143`  |
| 1360   | No file  | `86cba8f43143`  |
| 1358   | No file  | `86cba8f43143`  |
| 1355   | No file  | `86cba8f43143`  |
| 1351   | No file  | `86cba8f43143`  |
| 1348   | No file  | `86cba8f43143`  |
| 1346   | No file  | `86cba8f43143`  |
| 1341   | No file  | `86cba8f43143`  |
| 1340   | No file  | `86cba8f43143`  |
| 1338   | No file  | `86cba8f43143`  |
| 1335   | No file  | `86cba8f43143`  |
| 1333   | No file  | `86cba8f43143`  |
| 1329   | No file  | `86cba8f43143`  |
| 1327   | No file  | `86cba8f43143`  |
| 1324   | No file  | `86cba8f43143`  |
| 1321   | No file  | `86cba8f43143`  |
| 1319   | No file  | `86cba8f43143`  |
| 1318   | No file  | `86cba8f43143`  |
| 1316   | No file  | `86cba8f43143`  |
| 1313   | No file  | `86cba8f43143`  |
| 1311   | No file  | `86cba8f43143`  |
| 1309   | No file  | `86cba8f43143`  |
| 1304   | No file  | `86cba8f43143`  |
| 1292   | No file  | `86cba8f43143`  |
| 1286   | No file  | `86cba8f43143`  |
| 1280   | No file  | `86cba8f43143`  |
| 1276   | No file  | `86cba8f43143`  |
| 1267   | No file  | `86cba8f43143`  |
| 1261   | No file  | `86cba8f43143`  |
| 1256   | No file  | `86cba8f43143`  |
| 1250   | No file  | `86cba8f43143`  |
| 1246   | No file  | `86cba8f43143`  |
| 1239   | No file  | `86cba8f43143`  |
| 1230   | No file  | `86cba8f43143`  |
| 1226   | No file  | `86cba8f43143`  |
| 1220   | No file  | `86cba8f43143`  |
| 1217   | No file  | `86cba8f43143`  |
| 1211   | No file  | `86cba8f43143`  |
| 1210   | No file  | `86cba8f43143`  |
| 1208   | No file  | `86cba8f43143`  |
| 1203   | No file  | `86cba8f43143`  |
| 1197   | No file  | `86cba8f43143`  |
| 1194   | No file  | `86cba8f43143`  |
| 1192   | No file  | `86cba8f43143`  |
| 1187   | No file  | `86cba8f43143`  |
| 1183   | No file  | `86cba8f43143`  |
| 1177   | No file  | `86cba8f43143`  |
| 1173   | No file  | `86cba8f43143`  |
| 1167   | No file  | `86cba8f43143`  |
| 1164   | No file  | `86cba8f43143`  |
| 1156   | No file  | `86cba8f43143`  |
| 1149   | No file  | `86cba8f43143`  |
| 1144   | No file  | `86cba8f43143`  |
| 1137   | No file  | `86cba8f43143`  |
| 1132   | No file  | `86cba8f43143`  |
| 1127   | No file  | `86cba8f43143`  |
| 1122   | No file  | `86cba8f43143`  |
| 1118   | No file  | `86cba8f43143`  |
| 1114   | No file  | `86cba8f43143`  |
| 1109   | No file  | `86cba8f43143`  |
| 1102   | No file  | `86cba8f43143`  |
| 1096   | No file  | `86cba8f43143`  |
| 1088   | No file  | `86cba8f43143`  |
| 1081   | No file  | `86cba8f43143`  |
| 1076   | No file  | `86cba8f43143`  |
| 1069   | No file  | `86cba8f43143`  |
| 1064   | No file  | `86cba8f43143`  |
| 1058   | No file  | `86cba8f43143`  |
| 1051   | No file  | `86cba8f43143`  |
| 1044   | No file  | `86cba8f43143`  |
| 1036   | No file  | `86cba8f43143`  |
| 1026   | No file  | `86cba8f43143`  |
| 1016   | No file  | `86cba8f43143`  |
| 1009   | No file  | `86cba8f43143`  |
| 1005   | No file  | `86cba8f43143`  |
| 1000   | No file  | `86cba8f43143`  |
| 998    | No file  | `86cba8f43143`  |
| 990    | No file  | `86cba8f43143`  |
| 979    | No file  | `86cba8f43143`  |
| 972    | No file  | `86cba8f43143`  |
| 963    | No file  | `86cba8f43143`  |
| 955    | No file  | `86cba8f43143`  |
| 946    | No file  | `86cba8f43143`  |
| 938    | No file  | `86cba8f43143`  |
| 927    | No file  | `86cba8f43143`  |
| 911    | No file  | `86cba8f43143`  |
| 904    | No file  | `86cba8f43143`  |
| 899    | No file  | `86cba8f43143`  |
| 894    | No file  | `86cba8f43143`  |
| 885    | No file  | `86cba8f43143`  |
| 879    | No file  | `86cba8f43143`  |
| 872    | No file  | `86cba8f43143`  |
| 864    | No file  | `86cba8f43143`  |
| 855    | No file  | `86cba8f43143`  |
| 853    | No file  | `86cba8f43143`  |
| 845    | No file  | `86cba8f43143`  |
| 837    | No file  | `86cba8f43143`  |
| 829    | No file  | `86cba8f43143`  |
| 822    | No file  | `86cba8f43143`  |
| 814    | No file  | `86cba8f43143`  |
| 805    | No file  | `86cba8f43143`  |
| 794    | No file  | `86cba8f43143`  |
| 787    | No file  | `86cba8f43143`  |
| 780    | No file  | `86cba8f43143`  |
| 771    | No file  | `86cba8f43143`  |
| 760    | No file  | `86cba8f43143`  |
| 748    | No file  | `86cba8f43143`  |
| 741    | No file  | `86cba8f43143`  |
| 736    | No file  | `86cba8f43143`  |
| 731    | No file  | `86cba8f43143`  |
| 723    | No file  | `86cba8f43143`  |
| 711    | No file  | `86cba8f43143`  |
| 707    | No file  | `86cba8f43143`  |
| 697    | No file  | `86cba8f43143`  |
| 689    | No file  | `86cba8f43143`  |
| 683    | No file  | `86cba8f43143`  |
| 678    | No file  | `86cba8f43143`  |
| 670    | No file  | `86cba8f43143`  |
| 661    | No file  | `86cba8f43143`  |
| 656    | No file  | `86cba8f43143`  |
| 652    | No file  | `86cba8f43143`  |
| 643    | No file  | `86cba8f43143`  |
| 637    | No file  | `86cba8f43143`  |
| 630    | No file  | `86cba8f43143`  |
| 627    | No file  | `86cba8f43143`  |
| 621    | No file  | `86cba8f43143`  |
| 617    | No file  | `86cba8f43143`  |
| 615    | No file  | `86cba8f43143`  |
| 606    | No file  | `86cba8f43143`  |
| 599    | No file  | `86cba8f43143`  |
| 592    | No file  | `86cba8f43143`  |
| 586    | No file  | `86cba8f43143`  |
| 577    | No file  | `86cba8f43143`  |
| 569    | No file  | `86cba8f43143`  |
| 561    | No file  | `86cba8f43143`  |
| 554    | No file  | `86cba8f43143`  |
| 542    | No file  | `86cba8f43143`  |
| 532    | No file  | `86cba8f43143`  |
| 531    | No file  | `86cba8f43143`  |
| 526    | No file  | `86cba8f43143`  |
| 521    | No file  | `86cba8f43143`  |
| 517    | No file  | `86cba8f43143`  |
| 510    | No file  | `86cba8f43143`  |
| 508    | No file  | `86cba8f43143`  |
| 504    | No file  | `86cba8f43143`  |
| 497    | No file  | `86cba8f43143`  |
| 491    | No file  | `86cba8f43143`  |
| 485    | No file  | `86cba8f43143`  |
| 478    | No file  | `86cba8f43143`  |
| 472    | No file  | `86cba8f43143`  |
| 466    | No file  | `86cba8f43143`  |
| 457    | No file  | `86cba8f43143`  |
| 452    | No file  | `86cba8f43143`  |
| 449    | No file  | `86cba8f43143`  |
| 435    | No file  | `86cba8f43143`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of colours                             |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (12 bytes)

| Offset  | Type     | Field                  | Notes                                                          |
| ------- | -------- | ---------------------- | -------------------------------------------------------------- |
| `+0x00` | bytes[3] | map_color              | Course map colour, stored blue, green, red; see Speed Zones    |
| `+0x03` | u8       | unknown_03             | Always `0`                                                     |
| `+0x04` | bytes[3] | map_color_dup          | Equals `map_color` on every row                                |
| `+0x07` | u8       | unknown_07             | Always `0`                                                     |
| `+0x08` | u32      | horse_speed_apply_rate | Share of the horse's speed, per million (`1000000` = 100%)     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Speed Zones

The rows on clients 1784 and 3482 (the files are the same 80 bytes), with
`map_color` as `rrggbb`:

| `map_color` | `horse_speed_apply_rate` |
| ----------- | ------------------------ |
| `1e1e1e`    | `0`                      |
| `ff9696`    | `200000` (20%)           |
| `ff6464`    | `500000` (50%)           |
| `ff3232`    | `800000` (80%)           |
| `ff0000`    | `1000000` (100%)         |

`ui_texture/minimap/area/horseracecoursemap.bmp.rid` (client 3482), the
palette of the course map, lists these 5 colours and no other.

## Field Names

The names follow the `HorseRace_CourseSpeed` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_horseracedatatable.xlsm`. The sheet has the columns `R`, `G`,
`B`, `HorseSpeedApplyRate` and `HorseSpeedRate` and 5 rows; each file row
holds one sheet row's `R`, `G` and `B` in both colour fields and its
`HorseSpeedApplyRate` (5 of 5 rows, clients 1784 and 3482). The file
stores no `HorseSpeedRate` (`500000` on the `1e1e1e` row, `1000000` on
the others), so that column is server-only.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/servant_tables.py`:
  `map_color` as `rrggbb` and the rate as a percentage.
- [`snowboardcourseinfo.bss`](snowboardcourseinfo_bss.md) and
  [`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md) also store a
  region map colour twice in each row.
