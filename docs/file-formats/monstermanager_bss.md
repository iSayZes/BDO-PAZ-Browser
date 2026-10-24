# `monstermanager.bss` Format

## Purpose

A PABR list of monster characters, each with two u32 values. On client
3482 it holds six rows: three `Black Spirit's Energy` characters
(`21246`, `20900`, `20899`) and three characters named `Test` (`20885`
to `20883`). The second value is the first plus `1000` to `3000` on every
row. What the two values set is open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 1937 and later | 3483    | `monstermanager.bss` | 80    | 6 Row   | 10        |

| Layout | File                 | Known        | Unknown      |
| ------ | -------------------- | ------------ | ------------ |
| 1      | `monstermanager.bss` | 32 B (40.0%) | 48 B (60.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `b827e9107678`  |
| 3482   | Layout 1 | `b827e9107678`  |
| 3474   | Layout 1 | `b827e9107678`  |
| 3473   | Layout 1 | `b827e9107678`  |
| 3464   | Layout 1 | `b827e9107678`  |
| 3458   | Layout 1 | `b827e9107678`  |
| 3454   | Layout 1 | `b827e9107678`  |
| 3444   | Layout 1 | `b827e9107678`  |
| 3435   | Layout 1 | `b827e9107678`  |
| 3426   | Layout 1 | `b827e9107678`  |
| 3418   | Layout 1 | `b827e9107678`  |
| 3412   | Layout 1 | `b827e9107678`  |
| 3402   | Layout 1 | `b827e9107678`  |
| 3396   | Layout 1 | `b827e9107678`  |
| 3387   | Layout 1 | `b827e9107678`  |
| 3381   | Layout 1 | `b827e9107678`  |
| 3373   | Layout 1 | `b827e9107678`  |
| 3364   | Layout 1 | `b827e9107678`  |
| 3356   | Layout 1 | `b827e9107678`  |
| 3349   | Layout 1 | `b827e9107678`  |
| 3342   | Layout 1 | `b827e9107678`  |
| 3335   | Layout 1 | `b827e9107678`  |
| 3326   | Layout 1 | `b827e9107678`  |
| 3321   | Layout 1 | `b827e9107678`  |
| 3314   | Layout 1 | `b827e9107678`  |
| 3303   | Layout 1 | `b827e9107678`  |
| 3302   | Layout 1 | `b827e9107678`  |
| 3293   | Layout 1 | `b827e9107678`  |
| 3283   | Layout 1 | `b827e9107678`  |
| 3275   | Layout 1 | `b827e9107678`  |
| 3267   | Layout 1 | `b827e9107678`  |
| 3258   | Layout 1 | `b827e9107678`  |
| 3251   | Layout 1 | `b827e9107678`  |
| 3242   | Layout 1 | `b827e9107678`  |
| 3235   | Layout 1 | `b827e9107678`  |
| 3229   | Layout 1 | `b827e9107678`  |
| 3212   | Layout 1 | `b827e9107678`  |
| 3203   | Layout 1 | `b827e9107678`  |
| 3193   | Layout 1 | `b827e9107678`  |
| 3186   | Layout 1 | `b827e9107678`  |
| 3177   | Layout 1 | `b827e9107678`  |
| 3169   | Layout 1 | `b827e9107678`  |
| 3158   | Layout 1 | `b827e9107678`  |
| 3151   | Layout 1 | `b827e9107678`  |
| 3144   | Layout 1 | `b827e9107678`  |
| 3133   | Layout 1 | `b827e9107678`  |
| 3125   | Layout 1 | `b827e9107678`  |
| 3118   | Layout 1 | `b827e9107678`  |
| 3111   | Layout 1 | `b827e9107678`  |
| 3103   | Layout 1 | `b827e9107678`  |
| 3095   | Layout 1 | `b827e9107678`  |
| 3086   | Layout 1 | `b827e9107678`  |
| 3072   | Layout 1 | `b827e9107678`  |
| 3062   | Layout 1 | `b827e9107678`  |
| 3052   | Layout 1 | `b827e9107678`  |
| 3045   | Layout 1 | `b827e9107678`  |
| 3037   | Layout 1 | `b827e9107678`  |
| 3030   | Layout 1 | `b827e9107678`  |
| 3021   | Layout 1 | `b827e9107678`  |
| 3012   | Layout 1 | `b827e9107678`  |
| 3002   | Layout 1 | `b827e9107678`  |
| 2995   | Layout 1 | `b827e9107678`  |
| 2987   | Layout 1 | `b827e9107678`  |
| 2978   | Layout 1 | `b827e9107678`  |
| 2970   | Layout 1 | `b827e9107678`  |
| 2959   | Layout 1 | `b827e9107678`  |
| 2951   | Layout 1 | `b827e9107678`  |
| 2942   | Layout 1 | `b827e9107678`  |
| 2935   | Layout 1 | `b827e9107678`  |
| 2932   | Layout 1 | `b827e9107678`  |
| 2923   | Layout 1 | `b827e9107678`  |
| 2919   | Layout 1 | `b827e9107678`  |
| 2907   | Layout 1 | `b827e9107678`  |
| 2900   | Layout 1 | `b827e9107678`  |
| 2891   | Layout 1 | `b827e9107678`  |
| 2882   | Layout 1 | `b827e9107678`  |
| 2872   | Layout 1 | `b827e9107678`  |
| 2863   | Layout 1 | `b827e9107678`  |
| 2855   | Layout 1 | `b827e9107678`  |
| 2849   | Layout 1 | `b827e9107678`  |
| 2844   | Layout 1 | `b827e9107678`  |
| 2834   | Layout 1 | `b827e9107678`  |
| 2825   | Layout 1 | `b827e9107678`  |
| 2819   | Layout 1 | `b827e9107678`  |
| 2811   | Layout 1 | `b827e9107678`  |
| 2803   | Layout 1 | `b827e9107678`  |
| 2794   | Layout 1 | `b827e9107678`  |
| 2783   | Layout 1 | `b827e9107678`  |
| 2774   | Layout 1 | `b827e9107678`  |
| 2765   | Layout 1 | `b827e9107678`  |
| 2756   | Layout 1 | `b827e9107678`  |
| 2750   | Layout 1 | `b827e9107678`  |
| 2743   | Layout 1 | `b827e9107678`  |
| 2736   | Layout 1 | `b827e9107678`  |
| 2726   | Layout 1 | `b827e9107678`  |
| 2717   | Layout 1 | `b827e9107678`  |
| 2709   | Layout 1 | `b827e9107678`  |
| 2703   | Layout 1 | `b827e9107678`  |
| 2695   | Layout 1 | `b827e9107678`  |
| 2684   | Layout 1 | `b827e9107678`  |
| 2672   | Layout 1 | `b827e9107678`  |
| 2665   | Layout 1 | `b827e9107678`  |
| 2657   | Layout 1 | `b827e9107678`  |
| 2649   | Layout 1 | `b827e9107678`  |
| 2644   | Layout 1 | `b827e9107678`  |
| 2637   | Layout 1 | `b827e9107678`  |
| 2629   | Layout 1 | `b827e9107678`  |
| 2619   | Layout 1 | `b827e9107678`  |
| 2612   | Layout 1 | `b827e9107678`  |
| 2606   | Layout 1 | `b827e9107678`  |
| 2602   | Layout 1 | `b827e9107678`  |
| 2601   | Layout 1 | `b827e9107678`  |
| 2592   | Layout 1 | `b827e9107678`  |
| 2583   | Layout 1 | `b827e9107678`  |
| 2575   | Layout 1 | `b827e9107678`  |
| 2567   | Layout 1 | `b827e9107678`  |
| 2560   | Layout 1 | `b827e9107678`  |
| 2553   | Layout 1 | `b827e9107678`  |
| 2545   | Layout 1 | `b827e9107678`  |
| 2538   | Layout 1 | `b827e9107678`  |
| 2529   | Layout 1 | `b827e9107678`  |
| 2519   | Layout 1 | `b827e9107678`  |
| 2513   | Layout 1 | `b827e9107678`  |
| 2510   | Layout 1 | `b827e9107678`  |
| 2507   | Layout 1 | `b827e9107678`  |
| 2503   | Layout 1 | `b827e9107678`  |
| 2498   | Layout 1 | `b827e9107678`  |
| 2492   | Layout 1 | `b827e9107678`  |
| 2487   | Layout 1 | `b827e9107678`  |
| 2480   | Layout 1 | `b827e9107678`  |
| 2474   | Layout 1 | `b827e9107678`  |
| 2468   | Layout 1 | `b827e9107678`  |
| 2460   | Layout 1 | `b827e9107678`  |
| 2453   | Layout 1 | `b827e9107678`  |
| 2444   | Layout 1 | `b827e9107678`  |
| 2438   | Layout 1 | `b827e9107678`  |
| 2434   | Layout 1 | `b827e9107678`  |
| 2429   | Layout 1 | `b827e9107678`  |
| 2421   | Layout 1 | `b827e9107678`  |
| 2414   | Layout 1 | `b827e9107678`  |
| 2407   | Layout 1 | `b827e9107678`  |
| 2401   | Layout 1 | `b827e9107678`  |
| 2397   | Layout 1 | `b827e9107678`  |
| 2393   | Layout 1 | `b827e9107678`  |
| 2384   | Layout 1 | `b827e9107678`  |
| 2378   | Layout 1 | `b827e9107678`  |
| 2372   | Layout 1 | `b827e9107678`  |
| 2358   | Layout 1 | `b827e9107678`  |
| 2352   | Layout 1 | `b827e9107678`  |
| 2347   | Layout 1 | `b827e9107678`  |
| 2343   | Layout 1 | `b827e9107678`  |
| 2335   | Layout 1 | `b827e9107678`  |
| 2327   | Layout 1 | `b827e9107678`  |
| 2324   | Layout 1 | `b827e9107678`  |
| 2319   | Layout 1 | `b827e9107678`  |
| 2313   | Layout 1 | `b827e9107678`  |
| 2308   | Layout 1 | `b827e9107678`  |
| 2302   | Layout 1 | `b827e9107678`  |
| 2295   | Layout 1 | `b827e9107678`  |
| 2290   | Layout 1 | `b827e9107678`  |
| 2284   | Layout 1 | `b827e9107678`  |
| 2276   | Layout 1 | `b827e9107678`  |
| 2269   | Layout 1 | `b827e9107678`  |
| 2259   | Layout 1 | `b827e9107678`  |
| 2250   | Layout 1 | `b827e9107678`  |
| 2243   | Layout 1 | `b827e9107678`  |
| 2235   | Layout 1 | `b827e9107678`  |
| 2229   | Layout 1 | `b827e9107678`  |
| 2224   | Layout 1 | `b827e9107678`  |
| 2218   | Layout 1 | `b827e9107678`  |
| 2215   | Layout 1 | `b827e9107678`  |
| 2207   | Layout 1 | `b827e9107678`  |
| 2203   | Layout 1 | `b827e9107678`  |
| 2196   | Layout 1 | `b827e9107678`  |
| 2192   | Layout 1 | `b827e9107678`  |
| 2189   | Layout 1 | `b827e9107678`  |
| 2183   | Layout 1 | `b827e9107678`  |
| 2179   | Layout 1 | `b827e9107678`  |
| 2171   | Layout 1 | `b827e9107678`  |
| 2163   | Layout 1 | `b827e9107678`  |
| 2156   | Layout 1 | `b827e9107678`  |
| 2151   | Layout 1 | `b827e9107678`  |
| 2147   | Layout 1 | `b827e9107678`  |
| 2142   | Layout 1 | `b827e9107678`  |
| 2138   | Layout 1 | `b827e9107678`  |
| 2134   | Layout 1 | `b827e9107678`  |
| 2130   | Layout 1 | `b827e9107678`  |
| 2122   | Layout 1 | `b827e9107678`  |
| 2107   | Layout 1 | `b827e9107678`  |
| 2098   | Layout 1 | `b827e9107678`  |
| 2089   | Layout 1 | `b827e9107678`  |
| 2081   | Layout 1 | `b827e9107678`  |
| 2073   | Layout 1 | `b827e9107678`  |
| 2067   | Layout 1 | `b827e9107678`  |
| 2063   | Layout 1 | `b827e9107678`  |
| 2059   | Layout 1 | `b827e9107678`  |
| 2052   | Layout 1 | `b827e9107678`  |
| 2044   | Layout 1 | `b827e9107678`  |
| 2039   | Layout 1 | `b827e9107678`  |
| 2032   | Layout 1 | `b827e9107678`  |
| 2025   | Layout 1 | `b827e9107678`  |
| 2011   | Layout 1 | `b827e9107678`  |
| 2005   | Layout 1 | `b827e9107678`  |
| 2000   | Layout 1 | `b827e9107678`  |
| 1996   | Layout 1 | `b827e9107678`  |
| 1991   | Layout 1 | `b827e9107678`  |
| 1985   | Layout 1 | `b827e9107678`  |
| 1980   | Layout 1 | `b827e9107678`  |
| 1969   | Layout 1 | `b827e9107678`  |
| 1964   | Layout 1 | `b827e9107678`  |
| 1958   | Layout 1 | `b827e9107678`  |
| 1950   | Layout 1 | `b827e9107678`  |
| 1945   | Layout 1 | `b827e9107678`  |
| 1937   | Layout 1 | `b827e9107678`  |
| 1933   | No file  | `b827e9107678`  |
| 1927   | No file  | `b827e9107678`  |
| 1921   | No file  | `b827e9107678`  |
| 1914   | No file  | `b827e9107678`  |
| 1908   | No file  | `b827e9107678`  |
| 1897   | No file  | `b827e9107678`  |
| 1892   | No file  | `b827e9107678`  |
| 1886   | No file  | `b827e9107678`  |
| 1881   | No file  | `b827e9107678`  |
| 1871   | No file  | `b827e9107678`  |
| 1866   | No file  | `b827e9107678`  |
| 1862   | No file  | `b827e9107678`  |
| 1854   | No file  | `b827e9107678`  |
| 1846   | No file  | `b827e9107678`  |
| 1838   | No file  | `b827e9107678`  |
| 1832   | No file  | `b827e9107678`  |
| 1826   | No file  | `b827e9107678`  |
| 1822   | No file  | `b827e9107678`  |
| 1818   | No file  | `b827e9107678`  |
| 1804   | No file  | `b827e9107678`  |
| 1794   | No file  | `b827e9107678`  |
| 1790   | No file  | `b827e9107678`  |
| 1784   | No file  | `b827e9107678`  |
| 1774   | No file  | `b827e9107678`  |
| 1771   | No file  | `b827e9107678`  |
| 1762   | No file  | `b827e9107678`  |
| 1759   | No file  | `b827e9107678`  |
| 1754   | No file  | `b827e9107678`  |
| 1749   | No file  | `b827e9107678`  |
| 1743   | No file  | `b827e9107678`  |
| 1737   | No file  | `b827e9107678`  |
| 1731   | No file  | `b827e9107678`  |
| 1725   | No file  | `b827e9107678`  |
| 1717   | No file  | `b827e9107678`  |
| 1710   | No file  | `b827e9107678`  |
| 1704   | No file  | `b827e9107678`  |
| 1698   | No file  | `b827e9107678`  |
| 1690   | No file  | `b827e9107678`  |
| 1685   | No file  | `b827e9107678`  |
| 1680   | No file  | `b827e9107678`  |
| 1674   | No file  | `b827e9107678`  |
| 1668   | No file  | `b827e9107678`  |
| 1659   | No file  | `b827e9107678`  |
| 1649   | No file  | `b827e9107678`  |
| 1642   | No file  | `b827e9107678`  |
| 1636   | No file  | `b827e9107678`  |
| 1628   | No file  | `b827e9107678`  |
| 1622   | No file  | `b827e9107678`  |
| 1614   | No file  | `b827e9107678`  |
| 1608   | No file  | `b827e9107678`  |
| 1602   | No file  | `b827e9107678`  |
| 1598   | No file  | `b827e9107678`  |
| 1594   | No file  | `b827e9107678`  |
| 1590   | No file  | `b827e9107678`  |
| 1587   | No file  | `b827e9107678`  |
| 1584   | No file  | `b827e9107678`  |
| 1579   | No file  | `b827e9107678`  |
| 1572   | No file  | `b827e9107678`  |
| 1565   | No file  | `b827e9107678`  |
| 1559   | No file  | `b827e9107678`  |
| 1554   | No file  | `b827e9107678`  |
| 1547   | No file  | `b827e9107678`  |
| 1537   | No file  | `b827e9107678`  |
| 1529   | No file  | `b827e9107678`  |
| 1524   | No file  | `b827e9107678`  |
| 1519   | No file  | `b827e9107678`  |
| 1509   | No file  | `b827e9107678`  |
| 1506   | No file  | `b827e9107678`  |
| 1504   | No file  | `b827e9107678`  |
| 1500   | No file  | `b827e9107678`  |
| 1493   | No file  | `b827e9107678`  |
| 1489   | No file  | `b827e9107678`  |
| 1485   | No file  | `b827e9107678`  |
| 1481   | No file  | `b827e9107678`  |
| 1474   | No file  | `b827e9107678`  |
| 1466   | No file  | `b827e9107678`  |
| 1462   | No file  | `b827e9107678`  |
| 1459   | No file  | `b827e9107678`  |
| 1453   | No file  | `b827e9107678`  |
| 1450   | No file  | `b827e9107678`  |
| 1445   | No file  | `b827e9107678`  |
| 1439   | No file  | `b827e9107678`  |
| 1433   | No file  | `b827e9107678`  |
| 1430   | No file  | `b827e9107678`  |
| 1426   | No file  | `b827e9107678`  |
| 1421   | No file  | `b827e9107678`  |
| 1417   | No file  | `b827e9107678`  |
| 1416   | No file  | `b827e9107678`  |
| 1409   | No file  | `b827e9107678`  |
| 1405   | No file  | `b827e9107678`  |
| 1401   | No file  | `b827e9107678`  |
| 1396   | No file  | `b827e9107678`  |
| 1391   | No file  | `b827e9107678`  |
| 1390   | No file  | `b827e9107678`  |
| 1386   | No file  | `b827e9107678`  |
| 1381   | No file  | `b827e9107678`  |
| 1379   | No file  | `b827e9107678`  |
| 1372   | No file  | `b827e9107678`  |
| 1366   | No file  | `b827e9107678`  |
| 1364   | No file  | `b827e9107678`  |
| 1363   | No file  | `b827e9107678`  |
| 1360   | No file  | `b827e9107678`  |
| 1358   | No file  | `b827e9107678`  |
| 1355   | No file  | `b827e9107678`  |
| 1351   | No file  | `b827e9107678`  |
| 1348   | No file  | `b827e9107678`  |
| 1346   | No file  | `b827e9107678`  |
| 1341   | No file  | `b827e9107678`  |
| 1340   | No file  | `b827e9107678`  |
| 1338   | No file  | `b827e9107678`  |
| 1335   | No file  | `b827e9107678`  |
| 1333   | No file  | `b827e9107678`  |
| 1329   | No file  | `b827e9107678`  |
| 1327   | No file  | `b827e9107678`  |
| 1324   | No file  | `b827e9107678`  |
| 1321   | No file  | `b827e9107678`  |
| 1319   | No file  | `b827e9107678`  |
| 1318   | No file  | `b827e9107678`  |
| 1316   | No file  | `b827e9107678`  |
| 1313   | No file  | `b827e9107678`  |
| 1311   | No file  | `b827e9107678`  |
| 1309   | No file  | `b827e9107678`  |
| 1304   | No file  | `b827e9107678`  |
| 1292   | No file  | `b827e9107678`  |
| 1286   | No file  | `b827e9107678`  |
| 1280   | No file  | `b827e9107678`  |
| 1276   | No file  | `b827e9107678`  |
| 1267   | No file  | `b827e9107678`  |
| 1261   | No file  | `b827e9107678`  |
| 1256   | No file  | `b827e9107678`  |
| 1250   | No file  | `b827e9107678`  |
| 1246   | No file  | `b827e9107678`  |
| 1239   | No file  | `b827e9107678`  |
| 1230   | No file  | `b827e9107678`  |
| 1226   | No file  | `b827e9107678`  |
| 1220   | No file  | `b827e9107678`  |
| 1217   | No file  | `b827e9107678`  |
| 1211   | No file  | `b827e9107678`  |
| 1210   | No file  | `b827e9107678`  |
| 1208   | No file  | `b827e9107678`  |
| 1203   | No file  | `b827e9107678`  |
| 1197   | No file  | `b827e9107678`  |
| 1194   | No file  | `b827e9107678`  |
| 1192   | No file  | `b827e9107678`  |
| 1187   | No file  | `b827e9107678`  |
| 1183   | No file  | `b827e9107678`  |
| 1177   | No file  | `b827e9107678`  |
| 1173   | No file  | `b827e9107678`  |
| 1167   | No file  | `b827e9107678`  |
| 1164   | No file  | `b827e9107678`  |
| 1156   | No file  | `b827e9107678`  |
| 1149   | No file  | `b827e9107678`  |
| 1144   | No file  | `b827e9107678`  |
| 1137   | No file  | `b827e9107678`  |
| 1132   | No file  | `b827e9107678`  |
| 1127   | No file  | `b827e9107678`  |
| 1122   | No file  | `b827e9107678`  |
| 1118   | No file  | `b827e9107678`  |
| 1114   | No file  | `b827e9107678`  |
| 1109   | No file  | `b827e9107678`  |
| 1102   | No file  | `b827e9107678`  |
| 1096   | No file  | `b827e9107678`  |
| 1088   | No file  | `b827e9107678`  |
| 1081   | No file  | `b827e9107678`  |
| 1076   | No file  | `b827e9107678`  |
| 1069   | No file  | `b827e9107678`  |
| 1064   | No file  | `b827e9107678`  |
| 1058   | No file  | `b827e9107678`  |
| 1051   | No file  | `b827e9107678`  |
| 1044   | No file  | `b827e9107678`  |
| 1036   | No file  | `b827e9107678`  |
| 1026   | No file  | `b827e9107678`  |
| 1016   | No file  | `b827e9107678`  |
| 1009   | No file  | `b827e9107678`  |
| 1005   | No file  | `b827e9107678`  |
| 1000   | No file  | `b827e9107678`  |
| 998    | No file  | `b827e9107678`  |
| 990    | No file  | `b827e9107678`  |
| 979    | No file  | `b827e9107678`  |
| 972    | No file  | `b827e9107678`  |
| 963    | No file  | `b827e9107678`  |
| 955    | No file  | `b827e9107678`  |
| 946    | No file  | `b827e9107678`  |
| 938    | No file  | `b827e9107678`  |
| 927    | No file  | `b827e9107678`  |
| 911    | No file  | `b827e9107678`  |
| 904    | No file  | `b827e9107678`  |
| 899    | No file  | `b827e9107678`  |
| 894    | No file  | `b827e9107678`  |
| 885    | No file  | `b827e9107678`  |
| 879    | No file  | `b827e9107678`  |
| 872    | No file  | `b827e9107678`  |
| 864    | No file  | `b827e9107678`  |
| 855    | No file  | `b827e9107678`  |
| 853    | No file  | `b827e9107678`  |
| 845    | No file  | `b827e9107678`  |
| 837    | No file  | `b827e9107678`  |
| 829    | No file  | `b827e9107678`  |
| 822    | No file  | `b827e9107678`  |
| 814    | No file  | `b827e9107678`  |
| 805    | No file  | `b827e9107678`  |
| 794    | No file  | `b827e9107678`  |
| 787    | No file  | `b827e9107678`  |
| 780    | No file  | `b827e9107678`  |
| 771    | No file  | `b827e9107678`  |
| 760    | No file  | `b827e9107678`  |
| 748    | No file  | `b827e9107678`  |
| 741    | No file  | `b827e9107678`  |
| 736    | No file  | `b827e9107678`  |
| 731    | No file  | `b827e9107678`  |
| 723    | No file  | `b827e9107678`  |
| 711    | No file  | `b827e9107678`  |
| 707    | No file  | `b827e9107678`  |
| 697    | No file  | `b827e9107678`  |
| 689    | No file  | `b827e9107678`  |
| 683    | No file  | `b827e9107678`  |
| 678    | No file  | `b827e9107678`  |
| 670    | No file  | `b827e9107678`  |
| 661    | No file  | `b827e9107678`  |
| 656    | No file  | `b827e9107678`  |
| 652    | No file  | `b827e9107678`  |
| 643    | No file  | `b827e9107678`  |
| 637    | No file  | `b827e9107678`  |
| 630    | No file  | `b827e9107678`  |
| 627    | No file  | `b827e9107678`  |
| 621    | No file  | `b827e9107678`  |
| 617    | No file  | `b827e9107678`  |
| 615    | No file  | `b827e9107678`  |
| 606    | No file  | `b827e9107678`  |
| 599    | No file  | `b827e9107678`  |
| 592    | No file  | `b827e9107678`  |
| 586    | No file  | `b827e9107678`  |
| 577    | No file  | `b827e9107678`  |
| 569    | No file  | `b827e9107678`  |
| 561    | No file  | `b827e9107678`  |
| 554    | No file  | `b827e9107678`  |
| 542    | No file  | `b827e9107678`  |
| 532    | No file  | `b827e9107678`  |
| 531    | No file  | `b827e9107678`  |
| 526    | No file  | `b827e9107678`  |
| 521    | No file  | `b827e9107678`  |
| 517    | No file  | `b827e9107678`  |
| 510    | No file  | `b827e9107678`  |
| 508    | No file  | `b827e9107678`  |
| 504    | No file  | `b827e9107678`  |
| 497    | No file  | `b827e9107678`  |
| 491    | No file  | `b827e9107678`  |
| 485    | No file  | `b827e9107678`  |
| 478    | No file  | `b827e9107678`  |
| 472    | No file  | `b827e9107678`  |
| 466    | No file  | `b827e9107678`  |
| 457    | No file  | `b827e9107678`  |
| 452    | No file  | `b827e9107678`  |
| 449    | No file  | `b827e9107678`  |
| 435    | No file  | `b827e9107678`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                     |
| ------------------- | -------------- | ------------ | ----------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                              |
| `+0x04`             | u32            | row_count    | Number of rows                            |
| `+0x08`             | Row[row_count] | rows         | See Row                                   |
| `rows+0x00`         | String Table   | string_table | See String Table                          |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                |

### Row (10 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | `characterstatic.dbss` key; the handler shows its LOC type 6 name     |
| `+0x02` | u32  | unknown_02    | `3000`, `5000` or `7000` on client 3482                               |
| `+0x06` | u32  | unknown_06    | `4000` to `10000` on client 3482; greater than `unknown_02` on every row |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Rows

Client 3482, in file order.

| `character_key` | Name (LOC type 6)     | `unknown_02` | `unknown_06` |
| --------------- | --------------------- | ------------ | ------------ |
| `21246`         | Black Spirit's Energy | `7000`       | `10000`      |
| `20900`         | Black Spirit's Energy | `5000`       | `8000`       |
| `20899`         | Black Spirit's Energy | `3000`       | `6000`       |
| `20885`         | Test                  | `7000`       | `8000`       |
| `20884`         | Test                  | `5000`       | `6000`       |
| `20883`         | Test                  | `3000`       | `4000`       |

## Field Names

Every key resolves to a LOC type 6 character name, so `character_key`
names the meaning. The file is not in the archives of client 1784, no
sheet or column of a private server's `DataSheets.bexcel` on that client
has `MonsterManager` in its name, and no client Lua on client 3482 names
the file or calls a getter for it. Both values stay unknown.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`: the
  character key and name per row.

## Open Questions

### What the Two Values Set

Both values are multiples of `1000` and the second is always the larger,
so a range (minimum and maximum) on a `10000` scale would fit, as would two
durations in milliseconds. The three `Black Spirit's Energy` characters and
the three `Test` characters step through the same `unknown_02` values
(`7000`, `5000`, `3000`). Nothing in the client Lua or UI XML reads either
value.
