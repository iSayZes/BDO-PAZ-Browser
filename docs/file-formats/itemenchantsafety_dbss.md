# `itemenchantsafety.dbss` Format

## Purpose

The enhancement safety limits per gear type: for the enhancement levels
`min_level` to `max_level`, the failstack at which enhancing stops
(`stack`) and the failstack and success chance above which the game shows a
caution (`caution_stack`, `caution_rate`). Companion
`itemenchantsafetyoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                           | Bytes | Records      | Row bytes |
| ------ | -------------- | ------------------------------ | ----- | ------------ | --------- |
| 1      | 1286 and later | `itemenchantsafety.dbss`       | 94    | 6 Row        | 15        |
| 1      | 1286 and later | `itemenchantsafetyoffset.dbss` | 76    | 6 Offset Row | 12        |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `itemenchantsafety.dbss`       | 94 B (100.0%) | 0 B (0.0%) |
| 1      | `itemenchantsafetyoffset.dbss` | 76 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `3416903331bf`  |
| 3482   | Layout 1 | `3416903331bf`  |
| 3474   | Layout 1 | `3416903331bf`  |
| 3473   | Layout 1 | `3416903331bf`  |
| 3464   | Layout 1 | `3416903331bf`  |
| 3458   | Layout 1 | `3416903331bf`  |
| 3454   | Layout 1 | `3416903331bf`  |
| 3444   | Layout 1 | `3416903331bf`  |
| 3435   | Layout 1 | `3416903331bf`  |
| 3426   | Layout 1 | `3416903331bf`  |
| 3418   | Layout 1 | `3416903331bf`  |
| 3412   | Layout 1 | `3416903331bf`  |
| 3402   | Layout 1 | `3416903331bf`  |
| 3396   | Layout 1 | `3416903331bf`  |
| 3387   | Layout 1 | `3416903331bf`  |
| 3381   | Layout 1 | `3416903331bf`  |
| 3373   | Layout 1 | `3416903331bf`  |
| 3364   | Layout 1 | `3416903331bf`  |
| 3356   | Layout 1 | `3416903331bf`  |
| 3349   | Layout 1 | `3416903331bf`  |
| 3342   | Layout 1 | `3416903331bf`  |
| 3335   | Layout 1 | `3416903331bf`  |
| 3326   | Layout 1 | `3416903331bf`  |
| 3321   | Layout 1 | `3416903331bf`  |
| 3314   | Layout 1 | `3416903331bf`  |
| 3303   | Layout 1 | `3416903331bf`  |
| 3302   | Layout 1 | `3416903331bf`  |
| 3293   | Layout 1 | `3416903331bf`  |
| 3283   | Layout 1 | `3416903331bf`  |
| 3275   | Layout 1 | `3416903331bf`  |
| 3267   | Layout 1 | `3416903331bf`  |
| 3258   | Layout 1 | `3416903331bf`  |
| 3251   | Layout 1 | `3416903331bf`  |
| 3242   | Layout 1 | `3416903331bf`  |
| 3235   | Layout 1 | `3416903331bf`  |
| 3229   | Layout 1 | `3416903331bf`  |
| 3212   | Layout 1 | `3416903331bf`  |
| 3203   | Layout 1 | `3416903331bf`  |
| 3193   | Layout 1 | `3416903331bf`  |
| 3186   | Layout 1 | `3416903331bf`  |
| 3177   | Layout 1 | `3416903331bf`  |
| 3169   | Layout 1 | `3416903331bf`  |
| 3158   | Layout 1 | `3416903331bf`  |
| 3151   | Layout 1 | `3416903331bf`  |
| 3144   | Layout 1 | `3416903331bf`  |
| 3133   | Layout 1 | `3416903331bf`  |
| 3125   | Layout 1 | `3416903331bf`  |
| 3118   | Layout 1 | `3416903331bf`  |
| 3111   | Layout 1 | `3416903331bf`  |
| 3103   | Layout 1 | `3416903331bf`  |
| 3095   | Layout 1 | `3416903331bf`  |
| 3086   | Layout 1 | `3416903331bf`  |
| 3072   | Layout 1 | `3416903331bf`  |
| 3062   | Layout 1 | `3416903331bf`  |
| 3052   | Layout 1 | `3416903331bf`  |
| 3045   | Layout 1 | `3416903331bf`  |
| 3037   | Layout 1 | `3416903331bf`  |
| 3030   | Layout 1 | `3416903331bf`  |
| 3021   | Layout 1 | `3416903331bf`  |
| 3012   | Layout 1 | `3416903331bf`  |
| 3002   | Layout 1 | `3416903331bf`  |
| 2995   | Layout 1 | `3416903331bf`  |
| 2987   | Layout 1 | `3416903331bf`  |
| 2978   | Layout 1 | `3416903331bf`  |
| 2970   | Layout 1 | `3416903331bf`  |
| 2959   | Layout 1 | `3416903331bf`  |
| 2951   | Layout 1 | `3416903331bf`  |
| 2942   | Layout 1 | `3416903331bf`  |
| 2935   | Layout 1 | `3416903331bf`  |
| 2932   | Layout 1 | `3416903331bf`  |
| 2923   | Layout 1 | `3416903331bf`  |
| 2919   | Layout 1 | `3416903331bf`  |
| 2907   | Layout 1 | `3416903331bf`  |
| 2900   | Layout 1 | `3416903331bf`  |
| 2891   | Layout 1 | `3416903331bf`  |
| 2882   | Layout 1 | `3416903331bf`  |
| 2872   | Layout 1 | `3416903331bf`  |
| 2863   | Layout 1 | `3416903331bf`  |
| 2855   | Layout 1 | `3416903331bf`  |
| 2849   | Layout 1 | `3416903331bf`  |
| 2844   | Layout 1 | `3416903331bf`  |
| 2834   | Layout 1 | `3416903331bf`  |
| 2825   | Layout 1 | `3416903331bf`  |
| 2819   | Layout 1 | `3416903331bf`  |
| 2811   | Layout 1 | `3416903331bf`  |
| 2803   | Layout 1 | `3416903331bf`  |
| 2794   | Layout 1 | `3416903331bf`  |
| 2783   | Layout 1 | `3416903331bf`  |
| 2774   | Layout 1 | `3416903331bf`  |
| 2765   | Layout 1 | `3416903331bf`  |
| 2756   | Layout 1 | `3416903331bf`  |
| 2750   | Layout 1 | `3416903331bf`  |
| 2743   | Layout 1 | `3416903331bf`  |
| 2736   | Layout 1 | `3416903331bf`  |
| 2726   | Layout 1 | `3416903331bf`  |
| 2717   | Layout 1 | `3416903331bf`  |
| 2709   | Layout 1 | `3416903331bf`  |
| 2703   | Layout 1 | `3416903331bf`  |
| 2695   | Layout 1 | `3416903331bf`  |
| 2684   | Layout 1 | `3416903331bf`  |
| 2672   | Layout 1 | `3416903331bf`  |
| 2665   | Layout 1 | `3416903331bf`  |
| 2657   | Layout 1 | `3416903331bf`  |
| 2649   | Layout 1 | `3416903331bf`  |
| 2644   | Layout 1 | `3416903331bf`  |
| 2637   | Layout 1 | `3416903331bf`  |
| 2629   | Layout 1 | `3416903331bf`  |
| 2619   | Layout 1 | `3416903331bf`  |
| 2612   | Layout 1 | `3416903331bf`  |
| 2606   | Layout 1 | `3416903331bf`  |
| 2602   | Layout 1 | `3416903331bf`  |
| 2601   | Layout 1 | `3416903331bf`  |
| 2592   | Layout 1 | `3416903331bf`  |
| 2583   | Layout 1 | `3416903331bf`  |
| 2575   | Layout 1 | `3416903331bf`  |
| 2567   | Layout 1 | `3416903331bf`  |
| 2560   | Layout 1 | `3416903331bf`  |
| 2553   | Layout 1 | `3416903331bf`  |
| 2545   | Layout 1 | `3416903331bf`  |
| 2538   | Layout 1 | `3416903331bf`  |
| 2529   | Layout 1 | `3416903331bf`  |
| 2519   | Layout 1 | `3416903331bf`  |
| 2513   | Layout 1 | `3416903331bf`  |
| 2510   | Layout 1 | `3416903331bf`  |
| 2507   | Layout 1 | `3416903331bf`  |
| 2503   | Layout 1 | `3416903331bf`  |
| 2498   | Layout 1 | `3416903331bf`  |
| 2492   | Layout 1 | `3416903331bf`  |
| 2487   | Layout 1 | `3416903331bf`  |
| 2480   | Layout 1 | `3416903331bf`  |
| 2474   | Layout 1 | `3416903331bf`  |
| 2468   | Layout 1 | `3416903331bf`  |
| 2460   | Layout 1 | `3416903331bf`  |
| 2453   | Layout 1 | `3416903331bf`  |
| 2444   | Layout 1 | `3416903331bf`  |
| 2438   | Layout 1 | `3416903331bf`  |
| 2434   | Layout 1 | `3416903331bf`  |
| 2429   | Layout 1 | `3416903331bf`  |
| 2421   | Layout 1 | `3416903331bf`  |
| 2414   | Layout 1 | `3416903331bf`  |
| 2407   | Layout 1 | `3416903331bf`  |
| 2401   | Layout 1 | `3416903331bf`  |
| 2397   | Layout 1 | `3416903331bf`  |
| 2393   | Layout 1 | `3416903331bf`  |
| 2384   | Layout 1 | `3416903331bf`  |
| 2378   | Layout 1 | `3416903331bf`  |
| 2372   | Layout 1 | `3416903331bf`  |
| 2358   | Layout 1 | `3416903331bf`  |
| 2352   | Layout 1 | `3416903331bf`  |
| 2347   | Layout 1 | `3416903331bf`  |
| 2343   | Layout 1 | `3416903331bf`  |
| 2335   | Layout 1 | `3416903331bf`  |
| 2327   | Layout 1 | `3416903331bf`  |
| 2324   | Layout 1 | `3416903331bf`  |
| 2319   | Layout 1 | `3416903331bf`  |
| 2313   | Layout 1 | `3416903331bf`  |
| 2308   | Layout 1 | `3416903331bf`  |
| 2302   | Layout 1 | `3416903331bf`  |
| 2295   | Layout 1 | `3416903331bf`  |
| 2290   | Layout 1 | `3416903331bf`  |
| 2284   | Layout 1 | `3416903331bf`  |
| 2276   | Layout 1 | `3416903331bf`  |
| 2269   | Layout 1 | `3416903331bf`  |
| 2259   | Layout 1 | `3416903331bf`  |
| 2250   | Layout 1 | `3416903331bf`  |
| 2243   | Layout 1 | `3416903331bf`  |
| 2235   | Layout 1 | `3416903331bf`  |
| 2229   | Layout 1 | `3416903331bf`  |
| 2224   | Layout 1 | `3416903331bf`  |
| 2218   | Layout 1 | `3416903331bf`  |
| 2215   | Layout 1 | `3416903331bf`  |
| 2207   | Layout 1 | `3416903331bf`  |
| 2203   | Layout 1 | `3416903331bf`  |
| 2196   | Layout 1 | `3416903331bf`  |
| 2192   | Layout 1 | `3416903331bf`  |
| 2189   | Layout 1 | `3416903331bf`  |
| 2183   | Layout 1 | `3416903331bf`  |
| 2179   | Layout 1 | `3416903331bf`  |
| 2171   | Layout 1 | `3416903331bf`  |
| 2163   | Layout 1 | `3416903331bf`  |
| 2156   | Layout 1 | `3416903331bf`  |
| 2151   | Layout 1 | `3416903331bf`  |
| 2147   | Layout 1 | `3416903331bf`  |
| 2142   | Layout 1 | `3416903331bf`  |
| 2138   | Layout 1 | `3416903331bf`  |
| 2134   | Layout 1 | `3416903331bf`  |
| 2130   | Layout 1 | `3416903331bf`  |
| 2122   | Layout 1 | `3416903331bf`  |
| 2107   | Layout 1 | `3416903331bf`  |
| 2098   | Layout 1 | `3416903331bf`  |
| 2089   | Layout 1 | `3416903331bf`  |
| 2081   | Layout 1 | `3416903331bf`  |
| 2073   | Layout 1 | `3416903331bf`  |
| 2067   | Layout 1 | `3416903331bf`  |
| 2063   | Layout 1 | `3416903331bf`  |
| 2059   | Layout 1 | `3416903331bf`  |
| 2052   | Layout 1 | `3416903331bf`  |
| 2044   | Layout 1 | `3416903331bf`  |
| 2039   | Layout 1 | `3416903331bf`  |
| 2032   | Layout 1 | `3416903331bf`  |
| 2025   | Layout 1 | `3416903331bf`  |
| 2011   | Layout 1 | `3416903331bf`  |
| 2005   | Layout 1 | `3416903331bf`  |
| 2000   | Layout 1 | `3416903331bf`  |
| 1996   | Layout 1 | `3416903331bf`  |
| 1991   | Layout 1 | `3416903331bf`  |
| 1985   | Layout 1 | `3416903331bf`  |
| 1980   | Layout 1 | `3416903331bf`  |
| 1969   | Layout 1 | `3416903331bf`  |
| 1964   | Layout 1 | `3416903331bf`  |
| 1958   | Layout 1 | `3416903331bf`  |
| 1950   | Layout 1 | `3416903331bf`  |
| 1945   | Layout 1 | `3416903331bf`  |
| 1937   | Layout 1 | `3416903331bf`  |
| 1933   | Layout 1 | `3416903331bf`  |
| 1927   | Layout 1 | `3416903331bf`  |
| 1921   | Layout 1 | `3416903331bf`  |
| 1914   | Layout 1 | `3416903331bf`  |
| 1908   | Layout 1 | `3416903331bf`  |
| 1897   | Layout 1 | `3416903331bf`  |
| 1892   | Layout 1 | `3416903331bf`  |
| 1886   | Layout 1 | `3416903331bf`  |
| 1881   | Layout 1 | `3416903331bf`  |
| 1871   | Layout 1 | `3416903331bf`  |
| 1866   | Layout 1 | `3416903331bf`  |
| 1862   | Layout 1 | `3416903331bf`  |
| 1854   | Layout 1 | `3416903331bf`  |
| 1846   | Layout 1 | `3416903331bf`  |
| 1838   | Layout 1 | `3416903331bf`  |
| 1832   | Layout 1 | `3416903331bf`  |
| 1826   | Layout 1 | `3416903331bf`  |
| 1822   | Layout 1 | `3416903331bf`  |
| 1818   | Layout 1 | `3416903331bf`  |
| 1804   | Layout 1 | `3416903331bf`  |
| 1794   | Layout 1 | `3416903331bf`  |
| 1790   | Layout 1 | `3416903331bf`  |
| 1784   | Layout 1 | `3416903331bf`  |
| 1774   | Layout 1 | `3416903331bf`  |
| 1771   | Layout 1 | `3416903331bf`  |
| 1762   | Layout 1 | `3416903331bf`  |
| 1759   | Layout 1 | `3416903331bf`  |
| 1754   | Layout 1 | `3416903331bf`  |
| 1749   | Layout 1 | `3416903331bf`  |
| 1743   | Layout 1 | `3416903331bf`  |
| 1737   | Layout 1 | `3416903331bf`  |
| 1731   | Layout 1 | `3416903331bf`  |
| 1725   | Layout 1 | `3416903331bf`  |
| 1717   | Layout 1 | `3416903331bf`  |
| 1710   | Layout 1 | `3416903331bf`  |
| 1704   | Layout 1 | `3416903331bf`  |
| 1698   | Layout 1 | `3416903331bf`  |
| 1690   | Layout 1 | `3416903331bf`  |
| 1685   | Layout 1 | `3416903331bf`  |
| 1680   | Layout 1 | `3416903331bf`  |
| 1674   | Layout 1 | `3416903331bf`  |
| 1668   | Layout 1 | `3416903331bf`  |
| 1659   | Layout 1 | `3416903331bf`  |
| 1649   | Layout 1 | `3416903331bf`  |
| 1642   | Layout 1 | `3416903331bf`  |
| 1636   | Layout 1 | `3416903331bf`  |
| 1628   | Layout 1 | `3416903331bf`  |
| 1622   | Layout 1 | `3416903331bf`  |
| 1614   | Layout 1 | `3416903331bf`  |
| 1608   | Layout 1 | `3416903331bf`  |
| 1602   | Layout 1 | `3416903331bf`  |
| 1598   | Layout 1 | `3416903331bf`  |
| 1594   | Layout 1 | `3416903331bf`  |
| 1590   | Layout 1 | `3416903331bf`  |
| 1587   | Layout 1 | `3416903331bf`  |
| 1584   | Layout 1 | `3416903331bf`  |
| 1579   | Layout 1 | `3416903331bf`  |
| 1572   | Layout 1 | `3416903331bf`  |
| 1565   | Layout 1 | `3416903331bf`  |
| 1559   | Layout 1 | `3416903331bf`  |
| 1554   | Layout 1 | `3416903331bf`  |
| 1547   | Layout 1 | `3416903331bf`  |
| 1537   | Layout 1 | `3416903331bf`  |
| 1529   | Layout 1 | `3416903331bf`  |
| 1524   | Layout 1 | `3416903331bf`  |
| 1519   | Layout 1 | `3416903331bf`  |
| 1509   | Layout 1 | `3416903331bf`  |
| 1506   | Layout 1 | `3416903331bf`  |
| 1504   | Layout 1 | `3416903331bf`  |
| 1500   | Layout 1 | `3416903331bf`  |
| 1493   | Layout 1 | `3416903331bf`  |
| 1489   | Layout 1 | `3416903331bf`  |
| 1485   | Layout 1 | `3416903331bf`  |
| 1481   | Layout 1 | `3416903331bf`  |
| 1474   | Layout 1 | `3416903331bf`  |
| 1466   | Layout 1 | `3416903331bf`  |
| 1462   | Layout 1 | `3416903331bf`  |
| 1459   | Layout 1 | `3416903331bf`  |
| 1453   | Layout 1 | `3416903331bf`  |
| 1450   | Layout 1 | `3416903331bf`  |
| 1445   | Layout 1 | `3416903331bf`  |
| 1439   | Layout 1 | `3416903331bf`  |
| 1433   | Layout 1 | `3416903331bf`  |
| 1430   | Layout 1 | `3416903331bf`  |
| 1426   | Layout 1 | `3416903331bf`  |
| 1421   | Layout 1 | `3416903331bf`  |
| 1417   | Layout 1 | `3416903331bf`  |
| 1416   | Layout 1 | `3416903331bf`  |
| 1409   | Layout 1 | `3416903331bf`  |
| 1405   | Layout 1 | `3416903331bf`  |
| 1401   | Layout 1 | `3416903331bf`  |
| 1396   | Layout 1 | `3416903331bf`  |
| 1391   | Layout 1 | `3416903331bf`  |
| 1390   | Layout 1 | `3416903331bf`  |
| 1386   | Layout 1 | `3416903331bf`  |
| 1381   | Layout 1 | `3416903331bf`  |
| 1379   | Layout 1 | `3416903331bf`  |
| 1372   | Layout 1 | `3416903331bf`  |
| 1366   | Layout 1 | `3416903331bf`  |
| 1364   | Layout 1 | `3416903331bf`  |
| 1363   | Layout 1 | `3416903331bf`  |
| 1360   | Layout 1 | `3416903331bf`  |
| 1358   | Layout 1 | `3416903331bf`  |
| 1355   | Layout 1 | `3416903331bf`  |
| 1351   | Layout 1 | `3416903331bf`  |
| 1348   | Layout 1 | `3416903331bf`  |
| 1346   | Layout 1 | `3416903331bf`  |
| 1341   | Layout 1 | `3416903331bf`  |
| 1340   | Layout 1 | `3416903331bf`  |
| 1338   | Layout 1 | `3416903331bf`  |
| 1335   | Layout 1 | `3416903331bf`  |
| 1333   | Layout 1 | `3416903331bf`  |
| 1329   | Layout 1 | `3416903331bf`  |
| 1327   | Layout 1 | `3416903331bf`  |
| 1324   | Layout 1 | `3416903331bf`  |
| 1321   | Layout 1 | `3416903331bf`  |
| 1319   | Layout 1 | `3416903331bf`  |
| 1318   | Layout 1 | `3416903331bf`  |
| 1316   | Layout 1 | `3416903331bf`  |
| 1313   | Layout 1 | `3416903331bf`  |
| 1311   | Layout 1 | `3416903331bf`  |
| 1309   | Layout 1 | `3416903331bf`  |
| 1304   | Layout 1 | `3416903331bf`  |
| 1292   | Layout 1 | `3416903331bf`  |
| 1286   | Layout 1 | `3416903331bf`  |
| 1280   | No file  | `3416903331bf`  |
| 1276   | No file  | `3416903331bf`  |
| 1267   | No file  | `3416903331bf`  |
| 1261   | No file  | `3416903331bf`  |
| 1256   | No file  | `3416903331bf`  |
| 1250   | No file  | `3416903331bf`  |
| 1246   | No file  | `3416903331bf`  |
| 1239   | No file  | `3416903331bf`  |
| 1230   | No file  | `3416903331bf`  |
| 1226   | No file  | `3416903331bf`  |
| 1220   | No file  | `3416903331bf`  |
| 1217   | No file  | `3416903331bf`  |
| 1211   | No file  | `3416903331bf`  |
| 1210   | No file  | `3416903331bf`  |
| 1208   | No file  | `3416903331bf`  |
| 1203   | No file  | `3416903331bf`  |
| 1197   | No file  | `3416903331bf`  |
| 1194   | No file  | `3416903331bf`  |
| 1192   | No file  | `3416903331bf`  |
| 1187   | No file  | `3416903331bf`  |
| 1183   | No file  | `3416903331bf`  |
| 1177   | No file  | `3416903331bf`  |
| 1173   | No file  | `3416903331bf`  |
| 1167   | No file  | `3416903331bf`  |
| 1164   | No file  | `3416903331bf`  |
| 1156   | No file  | `3416903331bf`  |
| 1149   | No file  | `3416903331bf`  |
| 1144   | No file  | `3416903331bf`  |
| 1137   | No file  | `3416903331bf`  |
| 1132   | No file  | `3416903331bf`  |
| 1127   | No file  | `3416903331bf`  |
| 1122   | No file  | `3416903331bf`  |
| 1118   | No file  | `3416903331bf`  |
| 1114   | No file  | `3416903331bf`  |
| 1109   | No file  | `3416903331bf`  |
| 1102   | No file  | `3416903331bf`  |
| 1096   | No file  | `3416903331bf`  |
| 1088   | No file  | `3416903331bf`  |
| 1081   | No file  | `3416903331bf`  |
| 1076   | No file  | `3416903331bf`  |
| 1069   | No file  | `3416903331bf`  |
| 1064   | No file  | `3416903331bf`  |
| 1058   | No file  | `3416903331bf`  |
| 1051   | No file  | `3416903331bf`  |
| 1044   | No file  | `3416903331bf`  |
| 1036   | No file  | `3416903331bf`  |
| 1026   | No file  | `3416903331bf`  |
| 1016   | No file  | `3416903331bf`  |
| 1009   | No file  | `3416903331bf`  |
| 1005   | No file  | `3416903331bf`  |
| 1000   | No file  | `3416903331bf`  |
| 998    | No file  | `3416903331bf`  |
| 990    | No file  | `3416903331bf`  |
| 979    | No file  | `3416903331bf`  |
| 972    | No file  | `3416903331bf`  |
| 963    | No file  | `3416903331bf`  |
| 955    | No file  | `3416903331bf`  |
| 946    | No file  | `3416903331bf`  |
| 938    | No file  | `3416903331bf`  |
| 927    | No file  | `3416903331bf`  |
| 911    | No file  | `3416903331bf`  |
| 904    | No file  | `3416903331bf`  |
| 899    | No file  | `3416903331bf`  |
| 894    | No file  | `3416903331bf`  |
| 885    | No file  | `3416903331bf`  |
| 879    | No file  | `3416903331bf`  |
| 872    | No file  | `3416903331bf`  |
| 864    | No file  | `3416903331bf`  |
| 855    | No file  | `3416903331bf`  |
| 853    | No file  | `3416903331bf`  |
| 845    | No file  | `3416903331bf`  |
| 837    | No file  | `3416903331bf`  |
| 829    | No file  | `3416903331bf`  |
| 822    | No file  | `3416903331bf`  |
| 814    | No file  | `3416903331bf`  |
| 805    | No file  | `3416903331bf`  |
| 794    | No file  | `3416903331bf`  |
| 787    | No file  | `3416903331bf`  |
| 780    | No file  | `3416903331bf`  |
| 771    | No file  | `3416903331bf`  |
| 760    | No file  | `3416903331bf`  |
| 748    | No file  | `3416903331bf`  |
| 741    | No file  | `3416903331bf`  |
| 736    | No file  | `3416903331bf`  |
| 731    | No file  | `3416903331bf`  |
| 723    | No file  | `3416903331bf`  |
| 711    | No file  | `3416903331bf`  |
| 707    | No file  | `3416903331bf`  |
| 697    | No file  | `3416903331bf`  |
| 689    | No file  | `3416903331bf`  |
| 683    | No file  | `3416903331bf`  |
| 678    | No file  | `3416903331bf`  |
| 670    | No file  | `3416903331bf`  |
| 661    | No file  | `3416903331bf`  |
| 656    | No file  | `3416903331bf`  |
| 652    | No file  | `3416903331bf`  |
| 643    | No file  | `3416903331bf`  |
| 637    | No file  | `3416903331bf`  |
| 630    | No file  | `3416903331bf`  |
| 627    | No file  | `3416903331bf`  |
| 621    | No file  | `3416903331bf`  |
| 617    | No file  | `3416903331bf`  |
| 615    | No file  | `3416903331bf`  |
| 606    | No file  | `3416903331bf`  |
| 599    | No file  | `3416903331bf`  |
| 592    | No file  | `3416903331bf`  |
| 586    | No file  | `3416903331bf`  |
| 577    | No file  | `3416903331bf`  |
| 569    | No file  | `3416903331bf`  |
| 561    | No file  | `3416903331bf`  |
| 554    | No file  | `3416903331bf`  |
| 542    | No file  | `3416903331bf`  |
| 532    | No file  | `3416903331bf`  |
| 531    | No file  | `3416903331bf`  |
| 526    | No file  | `3416903331bf`  |
| 521    | No file  | `3416903331bf`  |
| 517    | No file  | `3416903331bf`  |
| 510    | No file  | `3416903331bf`  |
| 508    | No file  | `3416903331bf`  |
| 504    | No file  | `3416903331bf`  |
| 497    | No file  | `3416903331bf`  |
| 491    | No file  | `3416903331bf`  |
| 485    | No file  | `3416903331bf`  |
| 478    | No file  | `3416903331bf`  |
| 472    | No file  | `3416903331bf`  |
| 466    | No file  | `3416903331bf`  |
| 457    | No file  | `3416903331bf`  |
| 452    | No file  | `3416903331bf`  |
| 449    | No file  | `3416903331bf`  |
| 435    | No file  | `3416903331bf`  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                                     |
| ------------------------------ | -------- | ------------------------------------------------------------------------ |
| `itemenchantsafetyoffset.dbss` | Optional | `type -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 6 x 15 = 94 bytes.

### Row (15 bytes)

| Offset  | Type | Field         | Notes                                                                       |
| ------- | ---- | ------------- | --------------------------------------------------------------------------- |
| `+0x00` | u8   | type          | Gear type, see Gear Types; unique                                           |
| `+0x01` | u8   | min_level     | Lowest enhancement level of the range; `0` on every row of clients 1784 and 3474 |
| `+0x02` | u8   | max_level     | Highest enhancement level of the range                                      |
| `+0x03` | u32  | stack         | Failstack from which enhancing in the range is blocked                      |
| `+0x07` | u32  | caution_stack | Failstack from which a caution can show                                     |
| `+0x0B` | u32  | caution_rate  | Success chance above which the caution shows, 1,000,000 = 100%              |

The rows are sorted by `type`.

### `itemenchantsafetyoffset.dbss`

Bare offset table into `itemenchantsafety.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `itemenchantsafety.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | type        | `type` of the row it points at                                     |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `itemenchantsafety.dbss`, at its `type` |
| `+0x08` | u32  | data_size   | `15` on every row: the whole row                                   |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. On
clients 1784 and 3474 every index row points at the row with its type, in
file order.

## Gear Types

The developer comment on the `Type` column of the `Enchant_Safetymode`
sheet (a private server's `datasheet_enchantdatatable_new.xlsm`, client
1784) names types `0` to `4`. Type `5` came between clients 3002 and 3251:
clients 3251 and 3474 have it, 3002 and older do not.

| Type | Gear (sheet comment)                                                                      | Levels (client 3474) | `stack` | `caution_stack` | `caution_rate` |
| ---- | ----------------------------------------------------------------------------------------- | -------------------- | ------- | --------------- | -------------- |
| 0    | Main weapons, sub-weapons, awakening weapons                                              | 0 to 18              | 100     | 150             | 30%            |
| 1    | Armor                                                                                     | 0 to 18              | 100     | 150             | 30%            |
| 2    | Accessories                                                                               | 0 to 2               | 100     | 50              | 70%            |
| 3    | Fishing rods, matchlocks, Trina battle axes, mount gear (ships, boats, wagons, horse gear, elephants) | 0 to 5 | 100     | 50              | 70%            |
| 4    | Silver Embroidered clothes (armor that takes more than one equipment slot)                 | 0 to 2               | 100     | 50              | 70%            |
| 5    | Not in the sheet                                                                          | 0 to 18              | 100     | 150             | 30%            |

On client 1784 types `0` and `1` read `0` to `17`, `caution_stack` `50` and
`caution_rate` 70%, like the other three.

## Field Names

The `Enchant_Safetymode` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Type`, `Min`, `Max`, `Stack`, `CautionStack`
and `CautionRate`, and its 5 rows match the client 1784 file on all 5 types
and every column. The developer comments on the sheet's header cells
(`datasheet_enchantdatatable_new.xlsm`, dated 2019-08-22 for the two
caution columns) say:

| Column         | Comment (translated)                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------- |
| `Min`, `Max`   | The group of levels where enhancing is blocked: Min `0` and Max `7` make +0 to +7 one group                   |
| `Stack`        | Enhancing is blocked when the character's failstack, without Valks' Cry, is at or above the value            |
| `CautionStack` | With a failstack at or above the value, a caution message shows when the success chance is above `CautionRate` |
| `CautionRate`  | `10000` = 1%                                                                                                  |

## Notes

- No client Lua script names a getter for the file: none of the 3,073
  scripts of client 3473 holds `Safety`, `SafeMode` or `Caution` next to
  enhancing, so the block and the caution run in the exe or on the server.
- The file exists on every checked client from 1485 to 3474 (1485, 1784,
  2107, 2519, 3002, 3251, 3474); clients 1485 and 1784 hold the same five
  rows. Client 1230 has an `itemenchantsafety.bss` in its place.

## Open Questions

### Gear Type 5

Type `5` (levels 0 to 18, `stack` 100, `caution_stack` 150, `caution_rate`
30%) has the values of types `0` and `1` but no name in the 1784 sheet, which
ends at type `4`. Which gear it covers is unknown.

### Current or Target Level

The sheet comment says Min `0` and Max `7` make "+0 to +7" one group, which
does not say whether the range holds the gear's level before the attempt or
the level it enhances to. With `max_level` 18 the two readings differ on the
TRI to TET attempt.
