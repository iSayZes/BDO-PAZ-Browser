# `itemsortprioritytype.bss` Format

## Purpose

A PABR table of 2-byte rows. On client 3483 it has 21 rows: the first byte
counts `0` to `20` in row order and the second byte holds each of `0` to
`20` once, a reordering of the first. No source sheet or client Lua names
the file or its fields, so both bytes stay `unknown_*`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes | Records | Row bytes |
| ------ | -------------- | -------------------------- | ----- | ------- | --------- |
| 1      | 1832 and later | `itemsortprioritytype.bss` | 62    | 21 Row  | 2         |

| Layout | File                       | Known        | Unknown      |
| ------ | -------------------------- | ------------ | ------------ |
| 1      | `itemsortprioritytype.bss` | 20 B (32.3%) | 42 B (67.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `87cd59d08222`  |
| 3482   | Layout 1 | `87cd59d08222`  |
| 3474   | Layout 1 | `87cd59d08222`  |
| 3473   | Layout 1 | `87cd59d08222`  |
| 3464   | Layout 1 | `87cd59d08222`  |
| 3458   | Layout 1 | `87cd59d08222`  |
| 3454   | Layout 1 | `87cd59d08222`  |
| 3444   | Layout 1 | `87cd59d08222`  |
| 3435   | Layout 1 | `87cd59d08222`  |
| 3426   | Layout 1 | `87cd59d08222`  |
| 3418   | Layout 1 | `87cd59d08222`  |
| 3412   | Layout 1 | `87cd59d08222`  |
| 3402   | Layout 1 | `87cd59d08222`  |
| 3396   | Layout 1 | `87cd59d08222`  |
| 3387   | Layout 1 | `87cd59d08222`  |
| 3381   | Layout 1 | `87cd59d08222`  |
| 3373   | Layout 1 | `87cd59d08222`  |
| 3364   | Layout 1 | `87cd59d08222`  |
| 3356   | Layout 1 | `87cd59d08222`  |
| 3349   | Layout 1 | `87cd59d08222`  |
| 3342   | Layout 1 | `87cd59d08222`  |
| 3335   | Layout 1 | `87cd59d08222`  |
| 3326   | Layout 1 | `87cd59d08222`  |
| 3321   | Layout 1 | `87cd59d08222`  |
| 3314   | Layout 1 | `87cd59d08222`  |
| 3303   | Layout 1 | `87cd59d08222`  |
| 3302   | Layout 1 | `87cd59d08222`  |
| 3293   | Layout 1 | `87cd59d08222`  |
| 3283   | Layout 1 | `87cd59d08222`  |
| 3275   | Layout 1 | `87cd59d08222`  |
| 3267   | Layout 1 | `87cd59d08222`  |
| 3258   | Layout 1 | `87cd59d08222`  |
| 3251   | Layout 1 | `87cd59d08222`  |
| 3242   | Layout 1 | `87cd59d08222`  |
| 3235   | Layout 1 | `87cd59d08222`  |
| 3229   | Layout 1 | `87cd59d08222`  |
| 3212   | Layout 1 | `87cd59d08222`  |
| 3203   | Layout 1 | `87cd59d08222`  |
| 3193   | Layout 1 | `87cd59d08222`  |
| 3186   | Layout 1 | `87cd59d08222`  |
| 3177   | Layout 1 | `87cd59d08222`  |
| 3169   | Layout 1 | `87cd59d08222`  |
| 3158   | Layout 1 | `87cd59d08222`  |
| 3151   | Layout 1 | `87cd59d08222`  |
| 3144   | Layout 1 | `87cd59d08222`  |
| 3133   | Layout 1 | `87cd59d08222`  |
| 3125   | Layout 1 | `87cd59d08222`  |
| 3118   | Layout 1 | `87cd59d08222`  |
| 3111   | Layout 1 | `87cd59d08222`  |
| 3103   | Layout 1 | `87cd59d08222`  |
| 3095   | Layout 1 | `87cd59d08222`  |
| 3086   | Layout 1 | `87cd59d08222`  |
| 3072   | Layout 1 | `87cd59d08222`  |
| 3062   | Layout 1 | `87cd59d08222`  |
| 3052   | Layout 1 | `87cd59d08222`  |
| 3045   | Layout 1 | `87cd59d08222`  |
| 3037   | Layout 1 | `87cd59d08222`  |
| 3030   | Layout 1 | `87cd59d08222`  |
| 3021   | Layout 1 | `87cd59d08222`  |
| 3012   | Layout 1 | `87cd59d08222`  |
| 3002   | Layout 1 | `87cd59d08222`  |
| 2995   | Layout 1 | `87cd59d08222`  |
| 2987   | Layout 1 | `87cd59d08222`  |
| 2978   | Layout 1 | `87cd59d08222`  |
| 2970   | Layout 1 | `87cd59d08222`  |
| 2959   | Layout 1 | `87cd59d08222`  |
| 2951   | Layout 1 | `87cd59d08222`  |
| 2942   | Layout 1 | `87cd59d08222`  |
| 2935   | Layout 1 | `87cd59d08222`  |
| 2932   | Layout 1 | `87cd59d08222`  |
| 2923   | Layout 1 | `87cd59d08222`  |
| 2919   | Layout 1 | `87cd59d08222`  |
| 2907   | Layout 1 | `87cd59d08222`  |
| 2900   | Layout 1 | `87cd59d08222`  |
| 2891   | Layout 1 | `87cd59d08222`  |
| 2882   | Layout 1 | `87cd59d08222`  |
| 2872   | Layout 1 | `87cd59d08222`  |
| 2863   | Layout 1 | `87cd59d08222`  |
| 2855   | Layout 1 | `87cd59d08222`  |
| 2849   | Layout 1 | `87cd59d08222`  |
| 2844   | Layout 1 | `87cd59d08222`  |
| 2834   | Layout 1 | `87cd59d08222`  |
| 2825   | Layout 1 | `87cd59d08222`  |
| 2819   | Layout 1 | `87cd59d08222`  |
| 2811   | Layout 1 | `87cd59d08222`  |
| 2803   | Layout 1 | `87cd59d08222`  |
| 2794   | Layout 1 | `87cd59d08222`  |
| 2783   | Layout 1 | `87cd59d08222`  |
| 2774   | Layout 1 | `87cd59d08222`  |
| 2765   | Layout 1 | `87cd59d08222`  |
| 2756   | Layout 1 | `87cd59d08222`  |
| 2750   | Layout 1 | `87cd59d08222`  |
| 2743   | Layout 1 | `87cd59d08222`  |
| 2736   | Layout 1 | `87cd59d08222`  |
| 2726   | Layout 1 | `87cd59d08222`  |
| 2717   | Layout 1 | `87cd59d08222`  |
| 2709   | Layout 1 | `87cd59d08222`  |
| 2703   | Layout 1 | `87cd59d08222`  |
| 2695   | Layout 1 | `87cd59d08222`  |
| 2684   | Layout 1 | `87cd59d08222`  |
| 2672   | Layout 1 | `87cd59d08222`  |
| 2665   | Layout 1 | `87cd59d08222`  |
| 2657   | Layout 1 | `87cd59d08222`  |
| 2649   | Layout 1 | `87cd59d08222`  |
| 2644   | Layout 1 | `87cd59d08222`  |
| 2637   | Layout 1 | `87cd59d08222`  |
| 2629   | Layout 1 | `87cd59d08222`  |
| 2619   | Layout 1 | `87cd59d08222`  |
| 2612   | Layout 1 | `87cd59d08222`  |
| 2606   | Layout 1 | `87cd59d08222`  |
| 2602   | Layout 1 | `87cd59d08222`  |
| 2601   | Layout 1 | `87cd59d08222`  |
| 2592   | Layout 1 | `87cd59d08222`  |
| 2583   | Layout 1 | `87cd59d08222`  |
| 2575   | Layout 1 | `87cd59d08222`  |
| 2567   | Layout 1 | `87cd59d08222`  |
| 2560   | Layout 1 | `87cd59d08222`  |
| 2553   | Layout 1 | `87cd59d08222`  |
| 2545   | Layout 1 | `87cd59d08222`  |
| 2538   | Layout 1 | `87cd59d08222`  |
| 2529   | Layout 1 | `87cd59d08222`  |
| 2519   | Layout 1 | `87cd59d08222`  |
| 2513   | Layout 1 | `87cd59d08222`  |
| 2510   | Layout 1 | `87cd59d08222`  |
| 2507   | Layout 1 | `87cd59d08222`  |
| 2503   | Layout 1 | `87cd59d08222`  |
| 2498   | Layout 1 | `87cd59d08222`  |
| 2492   | Layout 1 | `87cd59d08222`  |
| 2487   | Layout 1 | `87cd59d08222`  |
| 2480   | Layout 1 | `87cd59d08222`  |
| 2474   | Layout 1 | `87cd59d08222`  |
| 2468   | Layout 1 | `87cd59d08222`  |
| 2460   | Layout 1 | `87cd59d08222`  |
| 2453   | Layout 1 | `87cd59d08222`  |
| 2444   | Layout 1 | `87cd59d08222`  |
| 2438   | Layout 1 | `87cd59d08222`  |
| 2434   | Layout 1 | `87cd59d08222`  |
| 2429   | Layout 1 | `87cd59d08222`  |
| 2421   | Layout 1 | `87cd59d08222`  |
| 2414   | Layout 1 | `87cd59d08222`  |
| 2407   | Layout 1 | `87cd59d08222`  |
| 2401   | Layout 1 | `87cd59d08222`  |
| 2397   | Layout 1 | `87cd59d08222`  |
| 2393   | Layout 1 | `87cd59d08222`  |
| 2384   | Layout 1 | `87cd59d08222`  |
| 2378   | Layout 1 | `87cd59d08222`  |
| 2372   | Layout 1 | `87cd59d08222`  |
| 2358   | Layout 1 | `87cd59d08222`  |
| 2352   | Layout 1 | `87cd59d08222`  |
| 2347   | Layout 1 | `87cd59d08222`  |
| 2343   | Layout 1 | `87cd59d08222`  |
| 2335   | Layout 1 | `87cd59d08222`  |
| 2327   | Layout 1 | `87cd59d08222`  |
| 2324   | Layout 1 | `87cd59d08222`  |
| 2319   | Layout 1 | `87cd59d08222`  |
| 2313   | Layout 1 | `87cd59d08222`  |
| 2308   | Layout 1 | `87cd59d08222`  |
| 2302   | Layout 1 | `87cd59d08222`  |
| 2295   | Layout 1 | `87cd59d08222`  |
| 2290   | Layout 1 | `87cd59d08222`  |
| 2284   | Layout 1 | `87cd59d08222`  |
| 2276   | Layout 1 | `87cd59d08222`  |
| 2269   | Layout 1 | `87cd59d08222`  |
| 2259   | Layout 1 | `87cd59d08222`  |
| 2250   | Layout 1 | `87cd59d08222`  |
| 2243   | Layout 1 | `87cd59d08222`  |
| 2235   | Layout 1 | `87cd59d08222`  |
| 2229   | Layout 1 | `87cd59d08222`  |
| 2224   | Layout 1 | `87cd59d08222`  |
| 2218   | Layout 1 | `87cd59d08222`  |
| 2215   | Layout 1 | `87cd59d08222`  |
| 2207   | Layout 1 | `87cd59d08222`  |
| 2203   | Layout 1 | `87cd59d08222`  |
| 2196   | Layout 1 | `87cd59d08222`  |
| 2192   | Layout 1 | `87cd59d08222`  |
| 2189   | Layout 1 | `87cd59d08222`  |
| 2183   | Layout 1 | `87cd59d08222`  |
| 2179   | Layout 1 | `87cd59d08222`  |
| 2171   | Layout 1 | `87cd59d08222`  |
| 2163   | Layout 1 | `87cd59d08222`  |
| 2156   | Layout 1 | `87cd59d08222`  |
| 2151   | Layout 1 | `87cd59d08222`  |
| 2147   | Layout 1 | `87cd59d08222`  |
| 2142   | Layout 1 | `87cd59d08222`  |
| 2138   | Layout 1 | `87cd59d08222`  |
| 2134   | Layout 1 | `87cd59d08222`  |
| 2130   | Layout 1 | `87cd59d08222`  |
| 2122   | Layout 1 | `87cd59d08222`  |
| 2107   | Layout 1 | `87cd59d08222`  |
| 2098   | Layout 1 | `87cd59d08222`  |
| 2089   | Layout 1 | `87cd59d08222`  |
| 2081   | Layout 1 | `87cd59d08222`  |
| 2073   | Layout 1 | `87cd59d08222`  |
| 2067   | Layout 1 | `87cd59d08222`  |
| 2063   | Layout 1 | `87cd59d08222`  |
| 2059   | Layout 1 | `87cd59d08222`  |
| 2052   | Layout 1 | `87cd59d08222`  |
| 2044   | Layout 1 | `87cd59d08222`  |
| 2039   | Layout 1 | `87cd59d08222`  |
| 2032   | Layout 1 | `87cd59d08222`  |
| 2025   | Layout 1 | `87cd59d08222`  |
| 2011   | Layout 1 | `87cd59d08222`  |
| 2005   | Layout 1 | `87cd59d08222`  |
| 2000   | Layout 1 | `87cd59d08222`  |
| 1996   | Layout 1 | `87cd59d08222`  |
| 1991   | Layout 1 | `87cd59d08222`  |
| 1985   | Layout 1 | `87cd59d08222`  |
| 1980   | Layout 1 | `87cd59d08222`  |
| 1969   | Layout 1 | `87cd59d08222`  |
| 1964   | Layout 1 | `87cd59d08222`  |
| 1958   | Layout 1 | `87cd59d08222`  |
| 1950   | Layout 1 | `87cd59d08222`  |
| 1945   | Layout 1 | `87cd59d08222`  |
| 1937   | Layout 1 | `87cd59d08222`  |
| 1933   | Layout 1 | `87cd59d08222`  |
| 1927   | Layout 1 | `87cd59d08222`  |
| 1921   | Layout 1 | `87cd59d08222`  |
| 1914   | Layout 1 | `87cd59d08222`  |
| 1908   | Layout 1 | `87cd59d08222`  |
| 1897   | Layout 1 | `87cd59d08222`  |
| 1892   | Layout 1 | `87cd59d08222`  |
| 1886   | Layout 1 | `87cd59d08222`  |
| 1881   | Layout 1 | `87cd59d08222`  |
| 1871   | Layout 1 | `87cd59d08222`  |
| 1866   | Layout 1 | `87cd59d08222`  |
| 1862   | Layout 1 | `87cd59d08222`  |
| 1854   | Layout 1 | `87cd59d08222`  |
| 1846   | Layout 1 | `87cd59d08222`  |
| 1838   | Layout 1 | `87cd59d08222`  |
| 1832   | Layout 1 | `87cd59d08222`  |
| 1826   | No file  | `87cd59d08222`  |
| 1822   | No file  | `87cd59d08222`  |
| 1818   | No file  | `87cd59d08222`  |
| 1804   | No file  | `87cd59d08222`  |
| 1794   | No file  | `87cd59d08222`  |
| 1790   | No file  | `87cd59d08222`  |
| 1784   | No file  | `87cd59d08222`  |
| 1774   | No file  | `87cd59d08222`  |
| 1771   | No file  | `87cd59d08222`  |
| 1762   | No file  | `87cd59d08222`  |
| 1759   | No file  | `87cd59d08222`  |
| 1754   | No file  | `87cd59d08222`  |
| 1749   | No file  | `87cd59d08222`  |
| 1743   | No file  | `87cd59d08222`  |
| 1737   | No file  | `87cd59d08222`  |
| 1731   | No file  | `87cd59d08222`  |
| 1725   | No file  | `87cd59d08222`  |
| 1717   | No file  | `87cd59d08222`  |
| 1710   | No file  | `87cd59d08222`  |
| 1704   | No file  | `87cd59d08222`  |
| 1698   | No file  | `87cd59d08222`  |
| 1690   | No file  | `87cd59d08222`  |
| 1685   | No file  | `87cd59d08222`  |
| 1680   | No file  | `87cd59d08222`  |
| 1674   | No file  | `87cd59d08222`  |
| 1668   | No file  | `87cd59d08222`  |
| 1659   | No file  | `87cd59d08222`  |
| 1649   | No file  | `87cd59d08222`  |
| 1642   | No file  | `87cd59d08222`  |
| 1636   | No file  | `87cd59d08222`  |
| 1628   | No file  | `87cd59d08222`  |
| 1622   | No file  | `87cd59d08222`  |
| 1614   | No file  | `87cd59d08222`  |
| 1608   | No file  | `87cd59d08222`  |
| 1602   | No file  | `87cd59d08222`  |
| 1598   | No file  | `87cd59d08222`  |
| 1594   | No file  | `87cd59d08222`  |
| 1590   | No file  | `87cd59d08222`  |
| 1587   | No file  | `87cd59d08222`  |
| 1584   | No file  | `87cd59d08222`  |
| 1579   | No file  | `87cd59d08222`  |
| 1572   | No file  | `87cd59d08222`  |
| 1565   | No file  | `87cd59d08222`  |
| 1559   | No file  | `87cd59d08222`  |
| 1554   | No file  | `87cd59d08222`  |
| 1547   | No file  | `87cd59d08222`  |
| 1537   | No file  | `87cd59d08222`  |
| 1529   | No file  | `87cd59d08222`  |
| 1524   | No file  | `87cd59d08222`  |
| 1519   | No file  | `87cd59d08222`  |
| 1509   | No file  | `87cd59d08222`  |
| 1506   | No file  | `87cd59d08222`  |
| 1504   | No file  | `87cd59d08222`  |
| 1500   | No file  | `87cd59d08222`  |
| 1493   | No file  | `87cd59d08222`  |
| 1489   | No file  | `87cd59d08222`  |
| 1485   | No file  | `87cd59d08222`  |
| 1481   | No file  | `87cd59d08222`  |
| 1474   | No file  | `87cd59d08222`  |
| 1466   | No file  | `87cd59d08222`  |
| 1462   | No file  | `87cd59d08222`  |
| 1459   | No file  | `87cd59d08222`  |
| 1453   | No file  | `87cd59d08222`  |
| 1450   | No file  | `87cd59d08222`  |
| 1445   | No file  | `87cd59d08222`  |
| 1439   | No file  | `87cd59d08222`  |
| 1433   | No file  | `87cd59d08222`  |
| 1430   | No file  | `87cd59d08222`  |
| 1426   | No file  | `87cd59d08222`  |
| 1421   | No file  | `87cd59d08222`  |
| 1417   | No file  | `87cd59d08222`  |
| 1416   | No file  | `87cd59d08222`  |
| 1409   | No file  | `87cd59d08222`  |
| 1405   | No file  | `87cd59d08222`  |
| 1401   | No file  | `87cd59d08222`  |
| 1396   | No file  | `87cd59d08222`  |
| 1391   | No file  | `87cd59d08222`  |
| 1390   | No file  | `87cd59d08222`  |
| 1386   | No file  | `87cd59d08222`  |
| 1381   | No file  | `87cd59d08222`  |
| 1379   | No file  | `87cd59d08222`  |
| 1372   | No file  | `87cd59d08222`  |
| 1366   | No file  | `87cd59d08222`  |
| 1364   | No file  | `87cd59d08222`  |
| 1363   | No file  | `87cd59d08222`  |
| 1360   | No file  | `87cd59d08222`  |
| 1358   | No file  | `87cd59d08222`  |
| 1355   | No file  | `87cd59d08222`  |
| 1351   | No file  | `87cd59d08222`  |
| 1348   | No file  | `87cd59d08222`  |
| 1346   | No file  | `87cd59d08222`  |
| 1341   | No file  | `87cd59d08222`  |
| 1340   | No file  | `87cd59d08222`  |
| 1338   | No file  | `87cd59d08222`  |
| 1335   | No file  | `87cd59d08222`  |
| 1333   | No file  | `87cd59d08222`  |
| 1329   | No file  | `87cd59d08222`  |
| 1327   | No file  | `87cd59d08222`  |
| 1324   | No file  | `87cd59d08222`  |
| 1321   | No file  | `87cd59d08222`  |
| 1319   | No file  | `87cd59d08222`  |
| 1318   | No file  | `87cd59d08222`  |
| 1316   | No file  | `87cd59d08222`  |
| 1313   | No file  | `87cd59d08222`  |
| 1311   | No file  | `87cd59d08222`  |
| 1309   | No file  | `87cd59d08222`  |
| 1304   | No file  | `87cd59d08222`  |
| 1292   | No file  | `87cd59d08222`  |
| 1286   | No file  | `87cd59d08222`  |
| 1280   | No file  | `87cd59d08222`  |
| 1276   | No file  | `87cd59d08222`  |
| 1267   | No file  | `87cd59d08222`  |
| 1261   | No file  | `87cd59d08222`  |
| 1256   | No file  | `87cd59d08222`  |
| 1250   | No file  | `87cd59d08222`  |
| 1246   | No file  | `87cd59d08222`  |
| 1239   | No file  | `87cd59d08222`  |
| 1230   | No file  | `87cd59d08222`  |
| 1226   | No file  | `87cd59d08222`  |
| 1220   | No file  | `87cd59d08222`  |
| 1217   | No file  | `87cd59d08222`  |
| 1211   | No file  | `87cd59d08222`  |
| 1210   | No file  | `87cd59d08222`  |
| 1208   | No file  | `87cd59d08222`  |
| 1203   | No file  | `87cd59d08222`  |
| 1197   | No file  | `87cd59d08222`  |
| 1194   | No file  | `87cd59d08222`  |
| 1192   | No file  | `87cd59d08222`  |
| 1187   | No file  | `87cd59d08222`  |
| 1183   | No file  | `87cd59d08222`  |
| 1177   | No file  | `87cd59d08222`  |
| 1173   | No file  | `87cd59d08222`  |
| 1167   | No file  | `87cd59d08222`  |
| 1164   | No file  | `87cd59d08222`  |
| 1156   | No file  | `87cd59d08222`  |
| 1149   | No file  | `87cd59d08222`  |
| 1144   | No file  | `87cd59d08222`  |
| 1137   | No file  | `87cd59d08222`  |
| 1132   | No file  | `87cd59d08222`  |
| 1127   | No file  | `87cd59d08222`  |
| 1122   | No file  | `87cd59d08222`  |
| 1118   | No file  | `87cd59d08222`  |
| 1114   | No file  | `87cd59d08222`  |
| 1109   | No file  | `87cd59d08222`  |
| 1102   | No file  | `87cd59d08222`  |
| 1096   | No file  | `87cd59d08222`  |
| 1088   | No file  | `87cd59d08222`  |
| 1081   | No file  | `87cd59d08222`  |
| 1076   | No file  | `87cd59d08222`  |
| 1069   | No file  | `87cd59d08222`  |
| 1064   | No file  | `87cd59d08222`  |
| 1058   | No file  | `87cd59d08222`  |
| 1051   | No file  | `87cd59d08222`  |
| 1044   | No file  | `87cd59d08222`  |
| 1036   | No file  | `87cd59d08222`  |
| 1026   | No file  | `87cd59d08222`  |
| 1016   | No file  | `87cd59d08222`  |
| 1009   | No file  | `87cd59d08222`  |
| 1005   | No file  | `87cd59d08222`  |
| 1000   | No file  | `87cd59d08222`  |
| 998    | No file  | `87cd59d08222`  |
| 990    | No file  | `87cd59d08222`  |
| 979    | No file  | `87cd59d08222`  |
| 972    | No file  | `87cd59d08222`  |
| 963    | No file  | `87cd59d08222`  |
| 955    | No file  | `87cd59d08222`  |
| 946    | No file  | `87cd59d08222`  |
| 938    | No file  | `87cd59d08222`  |
| 927    | No file  | `87cd59d08222`  |
| 911    | No file  | `87cd59d08222`  |
| 904    | No file  | `87cd59d08222`  |
| 899    | No file  | `87cd59d08222`  |
| 894    | No file  | `87cd59d08222`  |
| 885    | No file  | `87cd59d08222`  |
| 879    | No file  | `87cd59d08222`  |
| 872    | No file  | `87cd59d08222`  |
| 864    | No file  | `87cd59d08222`  |
| 855    | No file  | `87cd59d08222`  |
| 853    | No file  | `87cd59d08222`  |
| 845    | No file  | `87cd59d08222`  |
| 837    | No file  | `87cd59d08222`  |
| 829    | No file  | `87cd59d08222`  |
| 822    | No file  | `87cd59d08222`  |
| 814    | No file  | `87cd59d08222`  |
| 805    | No file  | `87cd59d08222`  |
| 794    | No file  | `87cd59d08222`  |
| 787    | No file  | `87cd59d08222`  |
| 780    | No file  | `87cd59d08222`  |
| 771    | No file  | `87cd59d08222`  |
| 760    | No file  | `87cd59d08222`  |
| 748    | No file  | `87cd59d08222`  |
| 741    | No file  | `87cd59d08222`  |
| 736    | No file  | `87cd59d08222`  |
| 731    | No file  | `87cd59d08222`  |
| 723    | No file  | `87cd59d08222`  |
| 711    | No file  | `87cd59d08222`  |
| 707    | No file  | `87cd59d08222`  |
| 697    | No file  | `87cd59d08222`  |
| 689    | No file  | `87cd59d08222`  |
| 683    | No file  | `87cd59d08222`  |
| 678    | No file  | `87cd59d08222`  |
| 670    | No file  | `87cd59d08222`  |
| 661    | No file  | `87cd59d08222`  |
| 656    | No file  | `87cd59d08222`  |
| 652    | No file  | `87cd59d08222`  |
| 643    | No file  | `87cd59d08222`  |
| 637    | No file  | `87cd59d08222`  |
| 630    | No file  | `87cd59d08222`  |
| 627    | No file  | `87cd59d08222`  |
| 621    | No file  | `87cd59d08222`  |
| 617    | No file  | `87cd59d08222`  |
| 615    | No file  | `87cd59d08222`  |
| 606    | No file  | `87cd59d08222`  |
| 599    | No file  | `87cd59d08222`  |
| 592    | No file  | `87cd59d08222`  |
| 586    | No file  | `87cd59d08222`  |
| 577    | No file  | `87cd59d08222`  |
| 569    | No file  | `87cd59d08222`  |
| 561    | No file  | `87cd59d08222`  |
| 554    | No file  | `87cd59d08222`  |
| 542    | No file  | `87cd59d08222`  |
| 532    | No file  | `87cd59d08222`  |
| 531    | No file  | `87cd59d08222`  |
| 526    | No file  | `87cd59d08222`  |
| 521    | No file  | `87cd59d08222`  |
| 517    | No file  | `87cd59d08222`  |
| 510    | No file  | `87cd59d08222`  |
| 508    | No file  | `87cd59d08222`  |
| 504    | No file  | `87cd59d08222`  |
| 497    | No file  | `87cd59d08222`  |
| 491    | No file  | `87cd59d08222`  |
| 485    | No file  | `87cd59d08222`  |
| 478    | No file  | `87cd59d08222`  |
| 472    | No file  | `87cd59d08222`  |
| 466    | No file  | `87cd59d08222`  |
| 457    | No file  | `87cd59d08222`  |
| 452    | No file  | `87cd59d08222`  |
| 449    | No file  | `87cd59d08222`  |
| 435    | No file  | `87cd59d08222`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (2 bytes)

| Offset  | Type | Field      | Notes                                                     |
| ------- | ---- | ---------- | --------------------------------------------------------- |
| `+0x00` | u8   | unknown_00 | The row's position, `0` to `20` (client 3483)             |
| `+0x01` | u8   | unknown_01 | Each of `0` to `20` once over the file (client 3483)      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Values

The 21 rows of client 3483:

| `unknown_00` | `unknown_01` | `unknown_00` | `unknown_01` | `unknown_00` | `unknown_01` |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| 0            | 4            | 7            | 7            | 14           | 12           |
| 1            | 0            | 8            | 14           | 15           | 17           |
| 2            | 2            | 9            | 16           | 16           | 5            |
| 3            | 9            | 10           | 3            | 17           | 15           |
| 4            | 6            | 11           | 8            | 18           | 18           |
| 5            | 1            | 12           | 10           | 19           | 19           |
| 6            | 11           | 13           | 13           | 20           | 20           |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
these rows, and client 1784 has no `itemsortprioritytype.bss`. The client
3482 Lua has no string with `sortpriority` or `itemsort` in it; the
inventory sort window (`panel_window_inventory_autosortfunction_1.luac`)
reads only the `__eInventorySortPropertyType_*` and
`__eInventorySortByType_*` settings through `ToClient_GetSortPropertyType`
and `ToClient_GetSortByType`.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/item_tables.py`. With no
  named field, each row shows as its two bytes in hex.

## Open Questions

### What the Two Bytes Hold

The file name reads as a sort priority per item type, which would make
`unknown_00` a type and `unknown_01` its place in the sort order. The 21
values fit neither `CppEnums.ItemType` (12 members, `Normal` to
`ToVehicle`) nor `CppEnums.ItemClassifyType` (18 members, `Etc` to
`DyeAmpule`) of the client 3482 `global_define_cpp_enum.luac`.
