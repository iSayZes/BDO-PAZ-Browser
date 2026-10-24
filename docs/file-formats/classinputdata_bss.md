# `classinputdata.bss` Format

## Purpose

Key commands by index: for each index and each `ClassNo` the list of
action inputs (`CppEnums.ActionInputType`) that make up one command, such
as TAB to draw the weapon or Shift + S. The client 1784 sheet writes the
commands as key names (`TAB`, `Shift,S`, `LC`, `S,LC,RC`); the file stores
the action input values.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records                     | Row bytes               |
| ------ | -------------- | ------- | -------------------- | ----- | --------------------------- | ----------------------- |
| 1      | 1759 and later | 3483    | `classinputdata.bss` | 214   | 10 Class Entry, 5 Index Row | 13 to 21, 15 on average |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 1      | `classinputdata.bss` | 214 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `0bcd388fd94f`  |
| 3482   | Layout 1 | `0bcd388fd94f`  |
| 3474   | Layout 1 | `0bcd388fd94f`  |
| 3473   | Layout 1 | `0bcd388fd94f`  |
| 3464   | Layout 1 | `0bcd388fd94f`  |
| 3458   | Layout 1 | `0bcd388fd94f`  |
| 3454   | Layout 1 | `0bcd388fd94f`  |
| 3444   | Layout 1 | `0bcd388fd94f`  |
| 3435   | Layout 1 | `0bcd388fd94f`  |
| 3426   | Layout 1 | `0bcd388fd94f`  |
| 3418   | Layout 1 | `0bcd388fd94f`  |
| 3412   | Layout 1 | `0bcd388fd94f`  |
| 3402   | Layout 1 | `0bcd388fd94f`  |
| 3396   | Layout 1 | `0bcd388fd94f`  |
| 3387   | Layout 1 | `0bcd388fd94f`  |
| 3381   | Layout 1 | `0bcd388fd94f`  |
| 3373   | Layout 1 | `0bcd388fd94f`  |
| 3364   | Layout 1 | `0bcd388fd94f`  |
| 3356   | Layout 1 | `0bcd388fd94f`  |
| 3349   | Layout 1 | `0bcd388fd94f`  |
| 3342   | Layout 1 | `0bcd388fd94f`  |
| 3335   | Layout 1 | `0bcd388fd94f`  |
| 3326   | Layout 1 | `0bcd388fd94f`  |
| 3321   | Layout 1 | `0bcd388fd94f`  |
| 3314   | Layout 1 | `0bcd388fd94f`  |
| 3303   | Layout 1 | `0bcd388fd94f`  |
| 3302   | Layout 1 | `0bcd388fd94f`  |
| 3293   | Layout 1 | `0bcd388fd94f`  |
| 3283   | Layout 1 | `0bcd388fd94f`  |
| 3275   | Layout 1 | `0bcd388fd94f`  |
| 3267   | Layout 1 | `0bcd388fd94f`  |
| 3258   | Layout 1 | `0bcd388fd94f`  |
| 3251   | Layout 1 | `0bcd388fd94f`  |
| 3242   | Layout 1 | `0bcd388fd94f`  |
| 3235   | Layout 1 | `0bcd388fd94f`  |
| 3229   | Layout 1 | `0bcd388fd94f`  |
| 3212   | Layout 1 | `0bcd388fd94f`  |
| 3203   | Layout 1 | `0bcd388fd94f`  |
| 3193   | Layout 1 | `0bcd388fd94f`  |
| 3186   | Layout 1 | `0bcd388fd94f`  |
| 3177   | Layout 1 | `0bcd388fd94f`  |
| 3169   | Layout 1 | `0bcd388fd94f`  |
| 3158   | Layout 1 | `0bcd388fd94f`  |
| 3151   | Layout 1 | `0bcd388fd94f`  |
| 3144   | Layout 1 | `0bcd388fd94f`  |
| 3133   | Layout 1 | `0bcd388fd94f`  |
| 3125   | Layout 1 | `0bcd388fd94f`  |
| 3118   | Layout 1 | `0bcd388fd94f`  |
| 3111   | Layout 1 | `0bcd388fd94f`  |
| 3103   | Layout 1 | `0bcd388fd94f`  |
| 3095   | Layout 1 | `0bcd388fd94f`  |
| 3086   | Layout 1 | `0bcd388fd94f`  |
| 3072   | Layout 1 | `0bcd388fd94f`  |
| 3062   | Layout 1 | `0bcd388fd94f`  |
| 3052   | Layout 1 | `0bcd388fd94f`  |
| 3045   | Layout 1 | `0bcd388fd94f`  |
| 3037   | Layout 1 | `0bcd388fd94f`  |
| 3030   | Layout 1 | `0bcd388fd94f`  |
| 3021   | Layout 1 | `0bcd388fd94f`  |
| 3012   | Layout 1 | `0bcd388fd94f`  |
| 3002   | Layout 1 | `0bcd388fd94f`  |
| 2995   | Layout 1 | `0bcd388fd94f`  |
| 2987   | Layout 1 | `0bcd388fd94f`  |
| 2978   | Layout 1 | `0bcd388fd94f`  |
| 2970   | Layout 1 | `0bcd388fd94f`  |
| 2959   | Layout 1 | `0bcd388fd94f`  |
| 2951   | Layout 1 | `0bcd388fd94f`  |
| 2942   | Layout 1 | `0bcd388fd94f`  |
| 2935   | Layout 1 | `0bcd388fd94f`  |
| 2932   | Layout 1 | `0bcd388fd94f`  |
| 2923   | Layout 1 | `0bcd388fd94f`  |
| 2919   | Layout 1 | `0bcd388fd94f`  |
| 2907   | Layout 1 | `0bcd388fd94f`  |
| 2900   | Layout 1 | `0bcd388fd94f`  |
| 2891   | Layout 1 | `0bcd388fd94f`  |
| 2882   | Layout 1 | `0bcd388fd94f`  |
| 2872   | Layout 1 | `0bcd388fd94f`  |
| 2863   | Layout 1 | `0bcd388fd94f`  |
| 2855   | Layout 1 | `0bcd388fd94f`  |
| 2849   | Layout 1 | `0bcd388fd94f`  |
| 2844   | Layout 1 | `0bcd388fd94f`  |
| 2834   | Layout 1 | `0bcd388fd94f`  |
| 2825   | Layout 1 | `0bcd388fd94f`  |
| 2819   | Layout 1 | `0bcd388fd94f`  |
| 2811   | Layout 1 | `0bcd388fd94f`  |
| 2803   | Layout 1 | `0bcd388fd94f`  |
| 2794   | Layout 1 | `0bcd388fd94f`  |
| 2783   | Layout 1 | `0bcd388fd94f`  |
| 2774   | Layout 1 | `0bcd388fd94f`  |
| 2765   | Layout 1 | `0bcd388fd94f`  |
| 2756   | Layout 1 | `0bcd388fd94f`  |
| 2750   | Layout 1 | `0bcd388fd94f`  |
| 2743   | Layout 1 | `0bcd388fd94f`  |
| 2736   | Layout 1 | `0bcd388fd94f`  |
| 2726   | Layout 1 | `0bcd388fd94f`  |
| 2717   | Layout 1 | `0bcd388fd94f`  |
| 2709   | Layout 1 | `0bcd388fd94f`  |
| 2703   | Layout 1 | `0bcd388fd94f`  |
| 2695   | Layout 1 | `0bcd388fd94f`  |
| 2684   | Layout 1 | `0bcd388fd94f`  |
| 2672   | Layout 1 | `0bcd388fd94f`  |
| 2665   | Layout 1 | `0bcd388fd94f`  |
| 2657   | Layout 1 | `0bcd388fd94f`  |
| 2649   | Layout 1 | `0bcd388fd94f`  |
| 2644   | Layout 1 | `0bcd388fd94f`  |
| 2637   | Layout 1 | `0bcd388fd94f`  |
| 2629   | Layout 1 | `0bcd388fd94f`  |
| 2619   | Layout 1 | `0bcd388fd94f`  |
| 2612   | Layout 1 | `0bcd388fd94f`  |
| 2606   | Layout 1 | `0bcd388fd94f`  |
| 2602   | Layout 1 | `0bcd388fd94f`  |
| 2601   | Layout 1 | `0bcd388fd94f`  |
| 2592   | Layout 1 | `0bcd388fd94f`  |
| 2583   | Layout 1 | `0bcd388fd94f`  |
| 2575   | Layout 1 | `0bcd388fd94f`  |
| 2567   | Layout 1 | `0bcd388fd94f`  |
| 2560   | Layout 1 | `0bcd388fd94f`  |
| 2553   | Layout 1 | `0bcd388fd94f`  |
| 2545   | Layout 1 | `0bcd388fd94f`  |
| 2538   | Layout 1 | `0bcd388fd94f`  |
| 2529   | Layout 1 | `0bcd388fd94f`  |
| 2519   | Layout 1 | `0bcd388fd94f`  |
| 2513   | Layout 1 | `0bcd388fd94f`  |
| 2510   | Layout 1 | `0bcd388fd94f`  |
| 2507   | Layout 1 | `0bcd388fd94f`  |
| 2503   | Layout 1 | `0bcd388fd94f`  |
| 2498   | Layout 1 | `0bcd388fd94f`  |
| 2492   | Layout 1 | `0bcd388fd94f`  |
| 2487   | Layout 1 | `0bcd388fd94f`  |
| 2480   | Layout 1 | `0bcd388fd94f`  |
| 2474   | Layout 1 | `0bcd388fd94f`  |
| 2468   | Layout 1 | `0bcd388fd94f`  |
| 2460   | Layout 1 | `0bcd388fd94f`  |
| 2453   | Layout 1 | `0bcd388fd94f`  |
| 2444   | Layout 1 | `0bcd388fd94f`  |
| 2438   | Layout 1 | `0bcd388fd94f`  |
| 2434   | Layout 1 | `0bcd388fd94f`  |
| 2429   | Layout 1 | `0bcd388fd94f`  |
| 2421   | Layout 1 | `0bcd388fd94f`  |
| 2414   | Layout 1 | `0bcd388fd94f`  |
| 2407   | Layout 1 | `0bcd388fd94f`  |
| 2401   | Layout 1 | `0bcd388fd94f`  |
| 2397   | Layout 1 | `0bcd388fd94f`  |
| 2393   | Layout 1 | `0bcd388fd94f`  |
| 2384   | Layout 1 | `0bcd388fd94f`  |
| 2378   | Layout 1 | `0bcd388fd94f`  |
| 2372   | Layout 1 | `0bcd388fd94f`  |
| 2358   | Layout 1 | `0bcd388fd94f`  |
| 2352   | Layout 1 | `0bcd388fd94f`  |
| 2347   | Layout 1 | `0bcd388fd94f`  |
| 2343   | Layout 1 | `0bcd388fd94f`  |
| 2335   | Layout 1 | `0bcd388fd94f`  |
| 2327   | Layout 1 | `0bcd388fd94f`  |
| 2324   | Layout 1 | `0bcd388fd94f`  |
| 2319   | Layout 1 | `0bcd388fd94f`  |
| 2313   | Layout 1 | `0bcd388fd94f`  |
| 2308   | Layout 1 | `0bcd388fd94f`  |
| 2302   | Layout 1 | `0bcd388fd94f`  |
| 2295   | Layout 1 | `0bcd388fd94f`  |
| 2290   | Layout 1 | `0bcd388fd94f`  |
| 2284   | Layout 1 | `0bcd388fd94f`  |
| 2276   | Layout 1 | `0bcd388fd94f`  |
| 2269   | Layout 1 | `0bcd388fd94f`  |
| 2259   | Layout 1 | `0bcd388fd94f`  |
| 2250   | Layout 1 | `0bcd388fd94f`  |
| 2243   | Layout 1 | `0bcd388fd94f`  |
| 2235   | Layout 1 | `0bcd388fd94f`  |
| 2229   | Layout 1 | `0bcd388fd94f`  |
| 2224   | Layout 1 | `0bcd388fd94f`  |
| 2218   | Layout 1 | `0bcd388fd94f`  |
| 2215   | Layout 1 | `0bcd388fd94f`  |
| 2207   | Layout 1 | `0bcd388fd94f`  |
| 2203   | Layout 1 | `0bcd388fd94f`  |
| 2196   | Layout 1 | `0bcd388fd94f`  |
| 2192   | Layout 1 | `0bcd388fd94f`  |
| 2189   | Layout 1 | `0bcd388fd94f`  |
| 2183   | Layout 1 | `0bcd388fd94f`  |
| 2179   | Layout 1 | `0bcd388fd94f`  |
| 2171   | Layout 1 | `0bcd388fd94f`  |
| 2163   | Layout 1 | `0bcd388fd94f`  |
| 2156   | Layout 1 | `0bcd388fd94f`  |
| 2151   | Layout 1 | `0bcd388fd94f`  |
| 2147   | Layout 1 | `0bcd388fd94f`  |
| 2142   | Layout 1 | `0bcd388fd94f`  |
| 2138   | Layout 1 | `0bcd388fd94f`  |
| 2134   | Layout 1 | `0bcd388fd94f`  |
| 2130   | Layout 1 | `0bcd388fd94f`  |
| 2122   | Layout 1 | `0bcd388fd94f`  |
| 2107   | Layout 1 | `0bcd388fd94f`  |
| 2098   | Layout 1 | `0bcd388fd94f`  |
| 2089   | Layout 1 | `0bcd388fd94f`  |
| 2081   | Layout 1 | `0bcd388fd94f`  |
| 2073   | Layout 1 | `0bcd388fd94f`  |
| 2067   | Layout 1 | `0bcd388fd94f`  |
| 2063   | Layout 1 | `0bcd388fd94f`  |
| 2059   | Layout 1 | `0bcd388fd94f`  |
| 2052   | Layout 1 | `0bcd388fd94f`  |
| 2044   | Layout 1 | `0bcd388fd94f`  |
| 2039   | Layout 1 | `0bcd388fd94f`  |
| 2032   | Layout 1 | `0bcd388fd94f`  |
| 2025   | Layout 1 | `0bcd388fd94f`  |
| 2011   | Layout 1 | `0bcd388fd94f`  |
| 2005   | Layout 1 | `0bcd388fd94f`  |
| 2000   | Layout 1 | `0bcd388fd94f`  |
| 1996   | Layout 1 | `0bcd388fd94f`  |
| 1991   | Layout 1 | `0bcd388fd94f`  |
| 1985   | Layout 1 | `0bcd388fd94f`  |
| 1980   | Layout 1 | `0bcd388fd94f`  |
| 1969   | Layout 1 | `0bcd388fd94f`  |
| 1964   | Layout 1 | `0bcd388fd94f`  |
| 1958   | Layout 1 | `0bcd388fd94f`  |
| 1950   | Layout 1 | `0bcd388fd94f`  |
| 1945   | Layout 1 | `0bcd388fd94f`  |
| 1937   | Layout 1 | `0bcd388fd94f`  |
| 1933   | Layout 1 | `0bcd388fd94f`  |
| 1927   | Layout 1 | `0bcd388fd94f`  |
| 1921   | Layout 1 | `0bcd388fd94f`  |
| 1914   | Layout 1 | `0bcd388fd94f`  |
| 1908   | Layout 1 | `0bcd388fd94f`  |
| 1897   | Layout 1 | `0bcd388fd94f`  |
| 1892   | Layout 1 | `0bcd388fd94f`  |
| 1886   | Layout 1 | `0bcd388fd94f`  |
| 1881   | Layout 1 | `0bcd388fd94f`  |
| 1871   | Layout 1 | `0bcd388fd94f`  |
| 1866   | Layout 1 | `0bcd388fd94f`  |
| 1862   | Layout 1 | `0bcd388fd94f`  |
| 1854   | Layout 1 | `0bcd388fd94f`  |
| 1846   | Layout 1 | `0bcd388fd94f`  |
| 1838   | Layout 1 | `0bcd388fd94f`  |
| 1832   | Layout 1 | `0bcd388fd94f`  |
| 1826   | Layout 1 | `0bcd388fd94f`  |
| 1822   | Layout 1 | `0bcd388fd94f`  |
| 1818   | Layout 1 | `0bcd388fd94f`  |
| 1804   | Layout 1 | `0bcd388fd94f`  |
| 1794   | Layout 1 | `0bcd388fd94f`  |
| 1790   | Layout 1 | `0bcd388fd94f`  |
| 1784   | Layout 1 | `0bcd388fd94f`  |
| 1774   | Layout 1 | `0bcd388fd94f`  |
| 1771   | Layout 1 | `0bcd388fd94f`  |
| 1762   | Layout 1 | `0bcd388fd94f`  |
| 1759   | Layout 1 | `0bcd388fd94f`  |
| 1754   | No file  | `0bcd388fd94f`  |
| 1749   | No file  | `0bcd388fd94f`  |
| 1743   | No file  | `0bcd388fd94f`  |
| 1737   | No file  | `0bcd388fd94f`  |
| 1731   | No file  | `0bcd388fd94f`  |
| 1725   | No file  | `0bcd388fd94f`  |
| 1717   | No file  | `0bcd388fd94f`  |
| 1710   | No file  | `0bcd388fd94f`  |
| 1704   | No file  | `0bcd388fd94f`  |
| 1698   | No file  | `0bcd388fd94f`  |
| 1690   | No file  | `0bcd388fd94f`  |
| 1685   | No file  | `0bcd388fd94f`  |
| 1680   | No file  | `0bcd388fd94f`  |
| 1674   | No file  | `0bcd388fd94f`  |
| 1668   | No file  | `0bcd388fd94f`  |
| 1659   | No file  | `0bcd388fd94f`  |
| 1649   | No file  | `0bcd388fd94f`  |
| 1642   | No file  | `0bcd388fd94f`  |
| 1636   | No file  | `0bcd388fd94f`  |
| 1628   | No file  | `0bcd388fd94f`  |
| 1622   | No file  | `0bcd388fd94f`  |
| 1614   | No file  | `0bcd388fd94f`  |
| 1608   | No file  | `0bcd388fd94f`  |
| 1602   | No file  | `0bcd388fd94f`  |
| 1598   | No file  | `0bcd388fd94f`  |
| 1594   | No file  | `0bcd388fd94f`  |
| 1590   | No file  | `0bcd388fd94f`  |
| 1587   | No file  | `0bcd388fd94f`  |
| 1584   | No file  | `0bcd388fd94f`  |
| 1579   | No file  | `0bcd388fd94f`  |
| 1572   | No file  | `0bcd388fd94f`  |
| 1565   | No file  | `0bcd388fd94f`  |
| 1559   | No file  | `0bcd388fd94f`  |
| 1554   | No file  | `0bcd388fd94f`  |
| 1547   | No file  | `0bcd388fd94f`  |
| 1537   | No file  | `0bcd388fd94f`  |
| 1529   | No file  | `0bcd388fd94f`  |
| 1524   | No file  | `0bcd388fd94f`  |
| 1519   | No file  | `0bcd388fd94f`  |
| 1509   | No file  | `0bcd388fd94f`  |
| 1506   | No file  | `0bcd388fd94f`  |
| 1504   | No file  | `0bcd388fd94f`  |
| 1500   | No file  | `0bcd388fd94f`  |
| 1493   | No file  | `0bcd388fd94f`  |
| 1489   | No file  | `0bcd388fd94f`  |
| 1485   | No file  | `0bcd388fd94f`  |
| 1481   | No file  | `0bcd388fd94f`  |
| 1474   | No file  | `0bcd388fd94f`  |
| 1466   | No file  | `0bcd388fd94f`  |
| 1462   | No file  | `0bcd388fd94f`  |
| 1459   | No file  | `0bcd388fd94f`  |
| 1453   | No file  | `0bcd388fd94f`  |
| 1450   | No file  | `0bcd388fd94f`  |
| 1445   | No file  | `0bcd388fd94f`  |
| 1439   | No file  | `0bcd388fd94f`  |
| 1433   | No file  | `0bcd388fd94f`  |
| 1430   | No file  | `0bcd388fd94f`  |
| 1426   | No file  | `0bcd388fd94f`  |
| 1421   | No file  | `0bcd388fd94f`  |
| 1417   | No file  | `0bcd388fd94f`  |
| 1416   | No file  | `0bcd388fd94f`  |
| 1409   | No file  | `0bcd388fd94f`  |
| 1405   | No file  | `0bcd388fd94f`  |
| 1401   | No file  | `0bcd388fd94f`  |
| 1396   | No file  | `0bcd388fd94f`  |
| 1391   | No file  | `0bcd388fd94f`  |
| 1390   | No file  | `0bcd388fd94f`  |
| 1386   | No file  | `0bcd388fd94f`  |
| 1381   | No file  | `0bcd388fd94f`  |
| 1379   | No file  | `0bcd388fd94f`  |
| 1372   | No file  | `0bcd388fd94f`  |
| 1366   | No file  | `0bcd388fd94f`  |
| 1364   | No file  | `0bcd388fd94f`  |
| 1363   | No file  | `0bcd388fd94f`  |
| 1360   | No file  | `0bcd388fd94f`  |
| 1358   | No file  | `0bcd388fd94f`  |
| 1355   | No file  | `0bcd388fd94f`  |
| 1351   | No file  | `0bcd388fd94f`  |
| 1348   | No file  | `0bcd388fd94f`  |
| 1346   | No file  | `0bcd388fd94f`  |
| 1341   | No file  | `0bcd388fd94f`  |
| 1340   | No file  | `0bcd388fd94f`  |
| 1338   | No file  | `0bcd388fd94f`  |
| 1335   | No file  | `0bcd388fd94f`  |
| 1333   | No file  | `0bcd388fd94f`  |
| 1329   | No file  | `0bcd388fd94f`  |
| 1327   | No file  | `0bcd388fd94f`  |
| 1324   | No file  | `0bcd388fd94f`  |
| 1321   | No file  | `0bcd388fd94f`  |
| 1319   | No file  | `0bcd388fd94f`  |
| 1318   | No file  | `0bcd388fd94f`  |
| 1316   | No file  | `0bcd388fd94f`  |
| 1313   | No file  | `0bcd388fd94f`  |
| 1311   | No file  | `0bcd388fd94f`  |
| 1309   | No file  | `0bcd388fd94f`  |
| 1304   | No file  | `0bcd388fd94f`  |
| 1292   | No file  | `0bcd388fd94f`  |
| 1286   | No file  | `0bcd388fd94f`  |
| 1280   | No file  | `0bcd388fd94f`  |
| 1276   | No file  | `0bcd388fd94f`  |
| 1267   | No file  | `0bcd388fd94f`  |
| 1261   | No file  | `0bcd388fd94f`  |
| 1256   | No file  | `0bcd388fd94f`  |
| 1250   | No file  | `0bcd388fd94f`  |
| 1246   | No file  | `0bcd388fd94f`  |
| 1239   | No file  | `0bcd388fd94f`  |
| 1230   | No file  | `0bcd388fd94f`  |
| 1226   | No file  | `0bcd388fd94f`  |
| 1220   | No file  | `0bcd388fd94f`  |
| 1217   | No file  | `0bcd388fd94f`  |
| 1211   | No file  | `0bcd388fd94f`  |
| 1210   | No file  | `0bcd388fd94f`  |
| 1208   | No file  | `0bcd388fd94f`  |
| 1203   | No file  | `0bcd388fd94f`  |
| 1197   | No file  | `0bcd388fd94f`  |
| 1194   | No file  | `0bcd388fd94f`  |
| 1192   | No file  | `0bcd388fd94f`  |
| 1187   | No file  | `0bcd388fd94f`  |
| 1183   | No file  | `0bcd388fd94f`  |
| 1177   | No file  | `0bcd388fd94f`  |
| 1173   | No file  | `0bcd388fd94f`  |
| 1167   | No file  | `0bcd388fd94f`  |
| 1164   | No file  | `0bcd388fd94f`  |
| 1156   | No file  | `0bcd388fd94f`  |
| 1149   | No file  | `0bcd388fd94f`  |
| 1144   | No file  | `0bcd388fd94f`  |
| 1137   | No file  | `0bcd388fd94f`  |
| 1132   | No file  | `0bcd388fd94f`  |
| 1127   | No file  | `0bcd388fd94f`  |
| 1122   | No file  | `0bcd388fd94f`  |
| 1118   | No file  | `0bcd388fd94f`  |
| 1114   | No file  | `0bcd388fd94f`  |
| 1109   | No file  | `0bcd388fd94f`  |
| 1102   | No file  | `0bcd388fd94f`  |
| 1096   | No file  | `0bcd388fd94f`  |
| 1088   | No file  | `0bcd388fd94f`  |
| 1081   | No file  | `0bcd388fd94f`  |
| 1076   | No file  | `0bcd388fd94f`  |
| 1069   | No file  | `0bcd388fd94f`  |
| 1064   | No file  | `0bcd388fd94f`  |
| 1058   | No file  | `0bcd388fd94f`  |
| 1051   | No file  | `0bcd388fd94f`  |
| 1044   | No file  | `0bcd388fd94f`  |
| 1036   | No file  | `0bcd388fd94f`  |
| 1026   | No file  | `0bcd388fd94f`  |
| 1016   | No file  | `0bcd388fd94f`  |
| 1009   | No file  | `0bcd388fd94f`  |
| 1005   | No file  | `0bcd388fd94f`  |
| 1000   | No file  | `0bcd388fd94f`  |
| 998    | No file  | `0bcd388fd94f`  |
| 990    | No file  | `0bcd388fd94f`  |
| 979    | No file  | `0bcd388fd94f`  |
| 972    | No file  | `0bcd388fd94f`  |
| 963    | No file  | `0bcd388fd94f`  |
| 955    | No file  | `0bcd388fd94f`  |
| 946    | No file  | `0bcd388fd94f`  |
| 938    | No file  | `0bcd388fd94f`  |
| 927    | No file  | `0bcd388fd94f`  |
| 911    | No file  | `0bcd388fd94f`  |
| 904    | No file  | `0bcd388fd94f`  |
| 899    | No file  | `0bcd388fd94f`  |
| 894    | No file  | `0bcd388fd94f`  |
| 885    | No file  | `0bcd388fd94f`  |
| 879    | No file  | `0bcd388fd94f`  |
| 872    | No file  | `0bcd388fd94f`  |
| 864    | No file  | `0bcd388fd94f`  |
| 855    | No file  | `0bcd388fd94f`  |
| 853    | No file  | `0bcd388fd94f`  |
| 845    | No file  | `0bcd388fd94f`  |
| 837    | No file  | `0bcd388fd94f`  |
| 829    | No file  | `0bcd388fd94f`  |
| 822    | No file  | `0bcd388fd94f`  |
| 814    | No file  | `0bcd388fd94f`  |
| 805    | No file  | `0bcd388fd94f`  |
| 794    | No file  | `0bcd388fd94f`  |
| 787    | No file  | `0bcd388fd94f`  |
| 780    | No file  | `0bcd388fd94f`  |
| 771    | No file  | `0bcd388fd94f`  |
| 760    | No file  | `0bcd388fd94f`  |
| 748    | No file  | `0bcd388fd94f`  |
| 741    | No file  | `0bcd388fd94f`  |
| 736    | No file  | `0bcd388fd94f`  |
| 731    | No file  | `0bcd388fd94f`  |
| 723    | No file  | `0bcd388fd94f`  |
| 711    | No file  | `0bcd388fd94f`  |
| 707    | No file  | `0bcd388fd94f`  |
| 697    | No file  | `0bcd388fd94f`  |
| 689    | No file  | `0bcd388fd94f`  |
| 683    | No file  | `0bcd388fd94f`  |
| 678    | No file  | `0bcd388fd94f`  |
| 670    | No file  | `0bcd388fd94f`  |
| 661    | No file  | `0bcd388fd94f`  |
| 656    | No file  | `0bcd388fd94f`  |
| 652    | No file  | `0bcd388fd94f`  |
| 643    | No file  | `0bcd388fd94f`  |
| 637    | No file  | `0bcd388fd94f`  |
| 630    | No file  | `0bcd388fd94f`  |
| 627    | No file  | `0bcd388fd94f`  |
| 621    | No file  | `0bcd388fd94f`  |
| 617    | No file  | `0bcd388fd94f`  |
| 615    | No file  | `0bcd388fd94f`  |
| 606    | No file  | `0bcd388fd94f`  |
| 599    | No file  | `0bcd388fd94f`  |
| 592    | No file  | `0bcd388fd94f`  |
| 586    | No file  | `0bcd388fd94f`  |
| 577    | No file  | `0bcd388fd94f`  |
| 569    | No file  | `0bcd388fd94f`  |
| 561    | No file  | `0bcd388fd94f`  |
| 554    | No file  | `0bcd388fd94f`  |
| 542    | No file  | `0bcd388fd94f`  |
| 532    | No file  | `0bcd388fd94f`  |
| 531    | No file  | `0bcd388fd94f`  |
| 526    | No file  | `0bcd388fd94f`  |
| 521    | No file  | `0bcd388fd94f`  |
| 517    | No file  | `0bcd388fd94f`  |
| 510    | No file  | `0bcd388fd94f`  |
| 508    | No file  | `0bcd388fd94f`  |
| 504    | No file  | `0bcd388fd94f`  |
| 497    | No file  | `0bcd388fd94f`  |
| 491    | No file  | `0bcd388fd94f`  |
| 485    | No file  | `0bcd388fd94f`  |
| 478    | No file  | `0bcd388fd94f`  |
| 472    | No file  | `0bcd388fd94f`  |
| 466    | No file  | `0bcd388fd94f`  |
| 457    | No file  | `0bcd388fd94f`  |
| 452    | No file  | `0bcd388fd94f`  |
| 449    | No file  | `0bcd388fd94f`  |
| 435    | No file  | `0bcd388fd94f`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                  | Field        | Notes                                         |
| ------------------- | --------------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]               | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32                   | index_count  | Number of indexes                             |
| `+0x08`             | Index Row[index_count] | rows        | See Index Row                                 |
| `rows+0x00`         | String Table          | string_table | See String Table                              |
| `string_table+0x00` | u32                   | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32                   | zero         | Always `0`                                    |

### Index Row (variable: 8 bytes + class entries)

| Offset  | Type                      | Field       | Notes                                        |
| ------- | ------------------------- | ----------- | -------------------------------------------- |
| `+0x00` | u32                       | index       | Row key, `1` up                              |
| `+0x04` | u32                       | class_count | Number of class entries; `2` on every row (clients 1784 and 3482) |
| `+0x08` | Class Entry[class_count]  | classes     | See Class Entry                              |

### Class Entry (variable: 9 bytes + commands)

| Offset  | Type                 | Field         | Notes                                                       |
| ------- | -------------------- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u8                   | class_no      | `0` or `1` on clients 1784 and 3482                         |
| `+0x01` | u64                  | command_count | Number of action inputs                                     |
| `+0x09` | u32[command_count]   | commands      | `CppEnums.ActionInputType` values in sheet order; see Commands |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Commands

`global_define_cpp_enum.luac` (client 3482) numbers
`CppEnums.ActionInputType` from `ActionInputType_MoveFront = 0` to
`ActionInputType_Undefined = 64`. Both class entries of an index hold the
same commands on clients 1784 and 3482:

| `index` | `commands` | Action inputs            | Sheet `Command` (client 1784) |
| ------- | ---------- | ------------------------ | ----------------------------- |
| `1`     | `10`       | WeaponInOut              | `TAB`                         |
| `2`     | `6, 1`     | Dash, MoveBack           | `Shift,S`                     |
| `3`     | `4`        | Attack1                  | `LC`                          |
| `4`     | `1, 4, 5`  | MoveBack, Attack1, Attack2 | `S,LC,RC`                   |
| `5`     | `0`        | MoveFront                | Not in the sheet; client 3482 |

## Field Names

`index`, `class_no` and `commands` are the `Index`, `ClassNo` and
`Command` columns of the `ClassInputData` sheet of a private server's
`DataSheets.bexcel` on client 1784. The sheet has 8 rows, one per index
and `ClassNo`, and the client 1784 file holds all 8: each `Command` key
list is the `commands` list once the key names are read as action inputs
(`TAB` WeaponInOut, `Shift` Dash, `S` MoveBack, `LC` Attack1, `RC`
Attack2, the default bindings). The sheet rows sharing an `Index` become
the class entries of one index row. Client 3482 adds index `5`.

## Notes

- `command_count` is a u32 count followed by a u32 `0` on every entry,
  written as one u64 as `docs/format-docs.md` asks.
- No client Lua file of client 3482 names the table or a getter for it.
- The handler (`_bss/classinputdata/`) shows one row per index and class
  entry with the action input names joined by `+`.

## Open Questions

### What ClassNo Is

`class_no` is `0` or `1` and both entries of an index hold the same
commands. Class types `0` and `1` are Warrior and Hashashin, but nothing
in the file or the Lua ties the column to class types; it may as well be
an input device or a control mode. A client whose entries differ would
tell.
