# `servantexperiencemaxlevel.bss` Format

## Purpose

Top level of each servant (mount or ship): one row per servant character with
the highest level of its [servantexperience.dbss](../dbss/servantexperience_dbss.md)
records. On client 3464 the file has 418 rows, the same servants as
`servantexperience.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                            | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------------- | ----- | ------- | --------- |
| 1      | 1230 and later | `servantexperiencemaxlevel.bss` | 1,676 | 418 Row | 4         |

| Layout | File                            | Known            | Unknown    |
| ------ | ------------------------------- | ---------------- | ---------- |
| 1      | `servantexperiencemaxlevel.bss` | 1,676 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d768594c2272`  |
| 3482   | Layout 1 | `d768594c2272`  |
| 3474   | Layout 1 | `d768594c2272`  |
| 3473   | Layout 1 | `d768594c2272`  |
| 3464   | Layout 1 | `d768594c2272`  |
| 3458   | Layout 1 | `d768594c2272`  |
| 3454   | Layout 1 | `d768594c2272`  |
| 3444   | Layout 1 | `d768594c2272`  |
| 3435   | Layout 1 | `d768594c2272`  |
| 3426   | Layout 1 | `d768594c2272`  |
| 3418   | Layout 1 | `d768594c2272`  |
| 3412   | Layout 1 | `d768594c2272`  |
| 3402   | Layout 1 | `d768594c2272`  |
| 3396   | Layout 1 | `d768594c2272`  |
| 3387   | Layout 1 | `d768594c2272`  |
| 3381   | Layout 1 | `d768594c2272`  |
| 3373   | Layout 1 | `d768594c2272`  |
| 3364   | Layout 1 | `d768594c2272`  |
| 3356   | Layout 1 | `d768594c2272`  |
| 3349   | Layout 1 | `d768594c2272`  |
| 3342   | Layout 1 | `d768594c2272`  |
| 3335   | Layout 1 | `d768594c2272`  |
| 3326   | Layout 1 | `d768594c2272`  |
| 3321   | Layout 1 | `d768594c2272`  |
| 3314   | Layout 1 | `d768594c2272`  |
| 3303   | Layout 1 | `d768594c2272`  |
| 3302   | Layout 1 | `d768594c2272`  |
| 3293   | Layout 1 | `d768594c2272`  |
| 3283   | Layout 1 | `d768594c2272`  |
| 3275   | Layout 1 | `d768594c2272`  |
| 3267   | Layout 1 | `d768594c2272`  |
| 3258   | Layout 1 | `d768594c2272`  |
| 3251   | Layout 1 | `d768594c2272`  |
| 3242   | Layout 1 | `d768594c2272`  |
| 3235   | Layout 1 | `d768594c2272`  |
| 3229   | Layout 1 | `d768594c2272`  |
| 3212   | Layout 1 | `d768594c2272`  |
| 3203   | Layout 1 | `d768594c2272`  |
| 3193   | Layout 1 | `d768594c2272`  |
| 3186   | Layout 1 | `d768594c2272`  |
| 3177   | Layout 1 | `d768594c2272`  |
| 3169   | Layout 1 | `d768594c2272`  |
| 3158   | Layout 1 | `d768594c2272`  |
| 3151   | Layout 1 | `d768594c2272`  |
| 3144   | Layout 1 | `d768594c2272`  |
| 3133   | Layout 1 | `d768594c2272`  |
| 3125   | Layout 1 | `d768594c2272`  |
| 3118   | Layout 1 | `d768594c2272`  |
| 3111   | Layout 1 | `d768594c2272`  |
| 3103   | Layout 1 | `d768594c2272`  |
| 3095   | Layout 1 | `d768594c2272`  |
| 3086   | Layout 1 | `d768594c2272`  |
| 3072   | Layout 1 | `d768594c2272`  |
| 3062   | Layout 1 | `d768594c2272`  |
| 3052   | Layout 1 | `d768594c2272`  |
| 3045   | Layout 1 | `d768594c2272`  |
| 3037   | Layout 1 | `d768594c2272`  |
| 3030   | Layout 1 | `d768594c2272`  |
| 3021   | Layout 1 | `d768594c2272`  |
| 3012   | Layout 1 | `d768594c2272`  |
| 3002   | Layout 1 | `d768594c2272`  |
| 2995   | Layout 1 | `d768594c2272`  |
| 2987   | Layout 1 | `d768594c2272`  |
| 2978   | Layout 1 | `d768594c2272`  |
| 2970   | Layout 1 | `d768594c2272`  |
| 2959   | Layout 1 | `d768594c2272`  |
| 2951   | Layout 1 | `d768594c2272`  |
| 2942   | Layout 1 | `d768594c2272`  |
| 2935   | Layout 1 | `d768594c2272`  |
| 2932   | Layout 1 | `d768594c2272`  |
| 2923   | Layout 1 | `d768594c2272`  |
| 2919   | Layout 1 | `d768594c2272`  |
| 2907   | Layout 1 | `d768594c2272`  |
| 2900   | Layout 1 | `d768594c2272`  |
| 2891   | Layout 1 | `d768594c2272`  |
| 2882   | Layout 1 | `d768594c2272`  |
| 2872   | Layout 1 | `d768594c2272`  |
| 2863   | Layout 1 | `d768594c2272`  |
| 2855   | Layout 1 | `d768594c2272`  |
| 2849   | Layout 1 | `d768594c2272`  |
| 2844   | Layout 1 | `d768594c2272`  |
| 2834   | Layout 1 | `d768594c2272`  |
| 2825   | Layout 1 | `d768594c2272`  |
| 2819   | Layout 1 | `d768594c2272`  |
| 2811   | Layout 1 | `d768594c2272`  |
| 2803   | Layout 1 | `d768594c2272`  |
| 2794   | Layout 1 | `d768594c2272`  |
| 2783   | Layout 1 | `d768594c2272`  |
| 2774   | Layout 1 | `d768594c2272`  |
| 2765   | Layout 1 | `d768594c2272`  |
| 2756   | Layout 1 | `d768594c2272`  |
| 2750   | Layout 1 | `d768594c2272`  |
| 2743   | Layout 1 | `d768594c2272`  |
| 2736   | Layout 1 | `d768594c2272`  |
| 2726   | Layout 1 | `d768594c2272`  |
| 2717   | Layout 1 | `d768594c2272`  |
| 2709   | Layout 1 | `d768594c2272`  |
| 2703   | Layout 1 | `d768594c2272`  |
| 2695   | Layout 1 | `d768594c2272`  |
| 2684   | Layout 1 | `d768594c2272`  |
| 2672   | Layout 1 | `d768594c2272`  |
| 2665   | Layout 1 | `d768594c2272`  |
| 2657   | Layout 1 | `d768594c2272`  |
| 2649   | Layout 1 | `d768594c2272`  |
| 2644   | Layout 1 | `d768594c2272`  |
| 2637   | Layout 1 | `d768594c2272`  |
| 2629   | Layout 1 | `d768594c2272`  |
| 2619   | Layout 1 | `d768594c2272`  |
| 2612   | Layout 1 | `d768594c2272`  |
| 2606   | Layout 1 | `d768594c2272`  |
| 2602   | Layout 1 | `d768594c2272`  |
| 2601   | Layout 1 | `d768594c2272`  |
| 2592   | Layout 1 | `d768594c2272`  |
| 2583   | Layout 1 | `d768594c2272`  |
| 2575   | Layout 1 | `d768594c2272`  |
| 2567   | Layout 1 | `d768594c2272`  |
| 2560   | Layout 1 | `d768594c2272`  |
| 2553   | Layout 1 | `d768594c2272`  |
| 2545   | Layout 1 | `d768594c2272`  |
| 2538   | Layout 1 | `d768594c2272`  |
| 2529   | Layout 1 | `d768594c2272`  |
| 2519   | Layout 1 | `d768594c2272`  |
| 2513   | Layout 1 | `d768594c2272`  |
| 2510   | Layout 1 | `d768594c2272`  |
| 2507   | Layout 1 | `d768594c2272`  |
| 2503   | Layout 1 | `d768594c2272`  |
| 2498   | Layout 1 | `d768594c2272`  |
| 2492   | Layout 1 | `d768594c2272`  |
| 2487   | Layout 1 | `d768594c2272`  |
| 2480   | Layout 1 | `d768594c2272`  |
| 2474   | Layout 1 | `d768594c2272`  |
| 2468   | Layout 1 | `d768594c2272`  |
| 2460   | Layout 1 | `d768594c2272`  |
| 2453   | Layout 1 | `d768594c2272`  |
| 2444   | Layout 1 | `d768594c2272`  |
| 2438   | Layout 1 | `d768594c2272`  |
| 2434   | Layout 1 | `d768594c2272`  |
| 2429   | Layout 1 | `d768594c2272`  |
| 2421   | Layout 1 | `d768594c2272`  |
| 2414   | Layout 1 | `d768594c2272`  |
| 2407   | Layout 1 | `d768594c2272`  |
| 2401   | Layout 1 | `d768594c2272`  |
| 2397   | Layout 1 | `d768594c2272`  |
| 2393   | Layout 1 | `d768594c2272`  |
| 2384   | Layout 1 | `d768594c2272`  |
| 2378   | Layout 1 | `d768594c2272`  |
| 2372   | Layout 1 | `d768594c2272`  |
| 2358   | Layout 1 | `d768594c2272`  |
| 2352   | Layout 1 | `d768594c2272`  |
| 2347   | Layout 1 | `d768594c2272`  |
| 2343   | Layout 1 | `d768594c2272`  |
| 2335   | Layout 1 | `d768594c2272`  |
| 2327   | Layout 1 | `d768594c2272`  |
| 2324   | Layout 1 | `d768594c2272`  |
| 2319   | Layout 1 | `d768594c2272`  |
| 2313   | Layout 1 | `d768594c2272`  |
| 2308   | Layout 1 | `d768594c2272`  |
| 2302   | Layout 1 | `d768594c2272`  |
| 2295   | Layout 1 | `d768594c2272`  |
| 2290   | Layout 1 | `d768594c2272`  |
| 2284   | Layout 1 | `d768594c2272`  |
| 2276   | Layout 1 | `d768594c2272`  |
| 2269   | Layout 1 | `d768594c2272`  |
| 2259   | Layout 1 | `d768594c2272`  |
| 2250   | Layout 1 | `d768594c2272`  |
| 2243   | Layout 1 | `d768594c2272`  |
| 2235   | Layout 1 | `d768594c2272`  |
| 2229   | Layout 1 | `d768594c2272`  |
| 2224   | Layout 1 | `d768594c2272`  |
| 2218   | Layout 1 | `d768594c2272`  |
| 2215   | Layout 1 | `d768594c2272`  |
| 2207   | Layout 1 | `d768594c2272`  |
| 2203   | Layout 1 | `d768594c2272`  |
| 2196   | Layout 1 | `d768594c2272`  |
| 2192   | Layout 1 | `d768594c2272`  |
| 2189   | Layout 1 | `d768594c2272`  |
| 2183   | Layout 1 | `d768594c2272`  |
| 2179   | Layout 1 | `d768594c2272`  |
| 2171   | Layout 1 | `d768594c2272`  |
| 2163   | Layout 1 | `d768594c2272`  |
| 2156   | Layout 1 | `d768594c2272`  |
| 2151   | Layout 1 | `d768594c2272`  |
| 2147   | Layout 1 | `d768594c2272`  |
| 2142   | Layout 1 | `d768594c2272`  |
| 2138   | Layout 1 | `d768594c2272`  |
| 2134   | Layout 1 | `d768594c2272`  |
| 2130   | Layout 1 | `d768594c2272`  |
| 2122   | Layout 1 | `d768594c2272`  |
| 2107   | Layout 1 | `d768594c2272`  |
| 2098   | Layout 1 | `d768594c2272`  |
| 2089   | Layout 1 | `d768594c2272`  |
| 2081   | Layout 1 | `d768594c2272`  |
| 2073   | Layout 1 | `d768594c2272`  |
| 2067   | Layout 1 | `d768594c2272`  |
| 2063   | Layout 1 | `d768594c2272`  |
| 2059   | Layout 1 | `d768594c2272`  |
| 2052   | Layout 1 | `d768594c2272`  |
| 2044   | Layout 1 | `d768594c2272`  |
| 2039   | Layout 1 | `d768594c2272`  |
| 2032   | Layout 1 | `d768594c2272`  |
| 2025   | Layout 1 | `d768594c2272`  |
| 2011   | Layout 1 | `d768594c2272`  |
| 2005   | Layout 1 | `d768594c2272`  |
| 2000   | Layout 1 | `d768594c2272`  |
| 1996   | Layout 1 | `d768594c2272`  |
| 1991   | Layout 1 | `d768594c2272`  |
| 1985   | Layout 1 | `d768594c2272`  |
| 1980   | Layout 1 | `d768594c2272`  |
| 1969   | Layout 1 | `d768594c2272`  |
| 1964   | Layout 1 | `d768594c2272`  |
| 1958   | Layout 1 | `d768594c2272`  |
| 1950   | Layout 1 | `d768594c2272`  |
| 1945   | Layout 1 | `d768594c2272`  |
| 1937   | Layout 1 | `d768594c2272`  |
| 1933   | Layout 1 | `d768594c2272`  |
| 1927   | Layout 1 | `d768594c2272`  |
| 1921   | Layout 1 | `d768594c2272`  |
| 1914   | Layout 1 | `d768594c2272`  |
| 1908   | Layout 1 | `d768594c2272`  |
| 1897   | Layout 1 | `d768594c2272`  |
| 1892   | Layout 1 | `d768594c2272`  |
| 1886   | Layout 1 | `d768594c2272`  |
| 1881   | Layout 1 | `d768594c2272`  |
| 1871   | Layout 1 | `d768594c2272`  |
| 1866   | Layout 1 | `d768594c2272`  |
| 1862   | Layout 1 | `d768594c2272`  |
| 1854   | Layout 1 | `d768594c2272`  |
| 1846   | Layout 1 | `d768594c2272`  |
| 1838   | Layout 1 | `d768594c2272`  |
| 1832   | Layout 1 | `d768594c2272`  |
| 1826   | Layout 1 | `d768594c2272`  |
| 1822   | Layout 1 | `d768594c2272`  |
| 1818   | Layout 1 | `d768594c2272`  |
| 1804   | Layout 1 | `d768594c2272`  |
| 1794   | Layout 1 | `d768594c2272`  |
| 1790   | Layout 1 | `d768594c2272`  |
| 1784   | Layout 1 | `d768594c2272`  |
| 1774   | Layout 1 | `d768594c2272`  |
| 1771   | Layout 1 | `d768594c2272`  |
| 1762   | Layout 1 | `d768594c2272`  |
| 1759   | Layout 1 | `d768594c2272`  |
| 1754   | Layout 1 | `d768594c2272`  |
| 1749   | Layout 1 | `d768594c2272`  |
| 1743   | Layout 1 | `d768594c2272`  |
| 1737   | Layout 1 | `d768594c2272`  |
| 1731   | Layout 1 | `d768594c2272`  |
| 1725   | Layout 1 | `d768594c2272`  |
| 1717   | Layout 1 | `d768594c2272`  |
| 1710   | Layout 1 | `d768594c2272`  |
| 1704   | Layout 1 | `d768594c2272`  |
| 1698   | Layout 1 | `d768594c2272`  |
| 1690   | Layout 1 | `d768594c2272`  |
| 1685   | Layout 1 | `d768594c2272`  |
| 1680   | Layout 1 | `d768594c2272`  |
| 1674   | Layout 1 | `d768594c2272`  |
| 1668   | Layout 1 | `d768594c2272`  |
| 1659   | Layout 1 | `d768594c2272`  |
| 1649   | Layout 1 | `d768594c2272`  |
| 1642   | Layout 1 | `d768594c2272`  |
| 1636   | Layout 1 | `d768594c2272`  |
| 1628   | Layout 1 | `d768594c2272`  |
| 1622   | Layout 1 | `d768594c2272`  |
| 1614   | Layout 1 | `d768594c2272`  |
| 1608   | Layout 1 | `d768594c2272`  |
| 1602   | Layout 1 | `d768594c2272`  |
| 1598   | Layout 1 | `d768594c2272`  |
| 1594   | Layout 1 | `d768594c2272`  |
| 1590   | Layout 1 | `d768594c2272`  |
| 1587   | Layout 1 | `d768594c2272`  |
| 1584   | Layout 1 | `d768594c2272`  |
| 1579   | Layout 1 | `d768594c2272`  |
| 1572   | Layout 1 | `d768594c2272`  |
| 1565   | Layout 1 | `d768594c2272`  |
| 1559   | Layout 1 | `d768594c2272`  |
| 1554   | Layout 1 | `d768594c2272`  |
| 1547   | Layout 1 | `d768594c2272`  |
| 1537   | Layout 1 | `d768594c2272`  |
| 1529   | Layout 1 | `d768594c2272`  |
| 1524   | Layout 1 | `d768594c2272`  |
| 1519   | Layout 1 | `d768594c2272`  |
| 1509   | Layout 1 | `d768594c2272`  |
| 1506   | Layout 1 | `d768594c2272`  |
| 1504   | Layout 1 | `d768594c2272`  |
| 1500   | Layout 1 | `d768594c2272`  |
| 1493   | Layout 1 | `d768594c2272`  |
| 1489   | Layout 1 | `d768594c2272`  |
| 1485   | Layout 1 | `d768594c2272`  |
| 1481   | Layout 1 | `d768594c2272`  |
| 1474   | Layout 1 | `d768594c2272`  |
| 1466   | Layout 1 | `d768594c2272`  |
| 1462   | Layout 1 | `d768594c2272`  |
| 1459   | Layout 1 | `d768594c2272`  |
| 1453   | Layout 1 | `d768594c2272`  |
| 1450   | Layout 1 | `d768594c2272`  |
| 1445   | Layout 1 | `d768594c2272`  |
| 1439   | Layout 1 | `d768594c2272`  |
| 1433   | Layout 1 | `d768594c2272`  |
| 1430   | Layout 1 | `d768594c2272`  |
| 1426   | Layout 1 | `d768594c2272`  |
| 1421   | Layout 1 | `d768594c2272`  |
| 1417   | Layout 1 | `d768594c2272`  |
| 1416   | Layout 1 | `d768594c2272`  |
| 1409   | Layout 1 | `d768594c2272`  |
| 1405   | Layout 1 | `d768594c2272`  |
| 1401   | Layout 1 | `d768594c2272`  |
| 1396   | Layout 1 | `d768594c2272`  |
| 1391   | Layout 1 | `d768594c2272`  |
| 1390   | Layout 1 | `d768594c2272`  |
| 1386   | Layout 1 | `d768594c2272`  |
| 1381   | Layout 1 | `d768594c2272`  |
| 1379   | Layout 1 | `d768594c2272`  |
| 1372   | Layout 1 | `d768594c2272`  |
| 1366   | Layout 1 | `d768594c2272`  |
| 1364   | Layout 1 | `d768594c2272`  |
| 1363   | Layout 1 | `d768594c2272`  |
| 1360   | Layout 1 | `d768594c2272`  |
| 1358   | Layout 1 | `d768594c2272`  |
| 1355   | Layout 1 | `d768594c2272`  |
| 1351   | Layout 1 | `d768594c2272`  |
| 1348   | Layout 1 | `d768594c2272`  |
| 1346   | Layout 1 | `d768594c2272`  |
| 1341   | Layout 1 | `d768594c2272`  |
| 1340   | Layout 1 | `d768594c2272`  |
| 1338   | Layout 1 | `d768594c2272`  |
| 1335   | Layout 1 | `d768594c2272`  |
| 1333   | Layout 1 | `d768594c2272`  |
| 1329   | Layout 1 | `d768594c2272`  |
| 1327   | Layout 1 | `d768594c2272`  |
| 1324   | Layout 1 | `d768594c2272`  |
| 1321   | Layout 1 | `d768594c2272`  |
| 1319   | Layout 1 | `d768594c2272`  |
| 1318   | Layout 1 | `d768594c2272`  |
| 1316   | Layout 1 | `d768594c2272`  |
| 1313   | Layout 1 | `d768594c2272`  |
| 1311   | Layout 1 | `d768594c2272`  |
| 1309   | Layout 1 | `d768594c2272`  |
| 1304   | Layout 1 | `d768594c2272`  |
| 1292   | Layout 1 | `d768594c2272`  |
| 1286   | Layout 1 | `d768594c2272`  |
| 1280   | Layout 1 | `d768594c2272`  |
| 1276   | Layout 1 | `d768594c2272`  |
| 1267   | Layout 1 | `d768594c2272`  |
| 1261   | Layout 1 | `d768594c2272`  |
| 1256   | Layout 1 | `d768594c2272`  |
| 1250   | Layout 1 | `d768594c2272`  |
| 1246   | Layout 1 | `d768594c2272`  |
| 1239   | Layout 1 | `d768594c2272`  |
| 1230   | Layout 1 | `d768594c2272`  |
| 1226   | No file  | `d768594c2272`  |
| 1220   | No file  | `d768594c2272`  |
| 1217   | No file  | `d768594c2272`  |
| 1211   | No file  | `d768594c2272`  |
| 1210   | No file  | `d768594c2272`  |
| 1208   | No file  | `d768594c2272`  |
| 1203   | No file  | `d768594c2272`  |
| 1197   | No file  | `d768594c2272`  |
| 1194   | No file  | `d768594c2272`  |
| 1192   | No file  | `d768594c2272`  |
| 1187   | No file  | `d768594c2272`  |
| 1183   | No file  | `d768594c2272`  |
| 1177   | No file  | `d768594c2272`  |
| 1173   | No file  | `d768594c2272`  |
| 1167   | No file  | `d768594c2272`  |
| 1164   | No file  | `d768594c2272`  |
| 1156   | No file  | `d768594c2272`  |
| 1149   | No file  | `d768594c2272`  |
| 1144   | No file  | `d768594c2272`  |
| 1137   | No file  | `d768594c2272`  |
| 1132   | No file  | `d768594c2272`  |
| 1127   | No file  | `d768594c2272`  |
| 1122   | No file  | `d768594c2272`  |
| 1118   | No file  | `d768594c2272`  |
| 1114   | No file  | `d768594c2272`  |
| 1109   | No file  | `d768594c2272`  |
| 1102   | No file  | `d768594c2272`  |
| 1096   | No file  | `d768594c2272`  |
| 1088   | No file  | `d768594c2272`  |
| 1081   | No file  | `d768594c2272`  |
| 1076   | No file  | `d768594c2272`  |
| 1069   | No file  | `d768594c2272`  |
| 1064   | No file  | `d768594c2272`  |
| 1058   | No file  | `d768594c2272`  |
| 1051   | No file  | `d768594c2272`  |
| 1044   | No file  | `d768594c2272`  |
| 1036   | No file  | `d768594c2272`  |
| 1026   | No file  | `d768594c2272`  |
| 1016   | No file  | `d768594c2272`  |
| 1009   | No file  | `d768594c2272`  |
| 1005   | No file  | `d768594c2272`  |
| 1000   | No file  | `d768594c2272`  |
| 998    | No file  | `d768594c2272`  |
| 990    | No file  | `d768594c2272`  |
| 979    | No file  | `d768594c2272`  |
| 972    | No file  | `d768594c2272`  |
| 963    | No file  | `d768594c2272`  |
| 955    | No file  | `d768594c2272`  |
| 946    | No file  | `d768594c2272`  |
| 938    | No file  | `d768594c2272`  |
| 927    | No file  | `d768594c2272`  |
| 911    | No file  | `d768594c2272`  |
| 904    | No file  | `d768594c2272`  |
| 899    | No file  | `d768594c2272`  |
| 894    | No file  | `d768594c2272`  |
| 885    | No file  | `d768594c2272`  |
| 879    | No file  | `d768594c2272`  |
| 872    | No file  | `d768594c2272`  |
| 864    | No file  | `d768594c2272`  |
| 855    | No file  | `d768594c2272`  |
| 853    | No file  | `d768594c2272`  |
| 845    | No file  | `d768594c2272`  |
| 837    | No file  | `d768594c2272`  |
| 829    | No file  | `d768594c2272`  |
| 822    | No file  | `d768594c2272`  |
| 814    | No file  | `d768594c2272`  |
| 805    | No file  | `d768594c2272`  |
| 794    | No file  | `d768594c2272`  |
| 787    | No file  | `d768594c2272`  |
| 780    | No file  | `d768594c2272`  |
| 771    | No file  | `d768594c2272`  |
| 760    | No file  | `d768594c2272`  |
| 748    | No file  | `d768594c2272`  |
| 741    | No file  | `d768594c2272`  |
| 736    | No file  | `d768594c2272`  |
| 731    | No file  | `d768594c2272`  |
| 723    | No file  | `d768594c2272`  |
| 711    | No file  | `d768594c2272`  |
| 707    | No file  | `d768594c2272`  |
| 697    | No file  | `d768594c2272`  |
| 689    | No file  | `d768594c2272`  |
| 683    | No file  | `d768594c2272`  |
| 678    | No file  | `d768594c2272`  |
| 670    | No file  | `d768594c2272`  |
| 661    | No file  | `d768594c2272`  |
| 656    | No file  | `d768594c2272`  |
| 652    | No file  | `d768594c2272`  |
| 643    | No file  | `d768594c2272`  |
| 637    | No file  | `d768594c2272`  |
| 630    | No file  | `d768594c2272`  |
| 627    | No file  | `d768594c2272`  |
| 621    | No file  | `d768594c2272`  |
| 617    | No file  | `d768594c2272`  |
| 615    | No file  | `d768594c2272`  |
| 606    | No file  | `d768594c2272`  |
| 599    | No file  | `d768594c2272`  |
| 592    | No file  | `d768594c2272`  |
| 586    | No file  | `d768594c2272`  |
| 577    | No file  | `d768594c2272`  |
| 569    | No file  | `d768594c2272`  |
| 561    | No file  | `d768594c2272`  |
| 554    | No file  | `d768594c2272`  |
| 542    | No file  | `d768594c2272`  |
| 532    | No file  | `d768594c2272`  |
| 531    | No file  | `d768594c2272`  |
| 526    | No file  | `d768594c2272`  |
| 521    | No file  | `d768594c2272`  |
| 517    | No file  | `d768594c2272`  |
| 510    | No file  | `d768594c2272`  |
| 508    | No file  | `d768594c2272`  |
| 504    | No file  | `d768594c2272`  |
| 497    | No file  | `d768594c2272`  |
| 491    | No file  | `d768594c2272`  |
| 485    | No file  | `d768594c2272`  |
| 478    | No file  | `d768594c2272`  |
| 472    | No file  | `d768594c2272`  |
| 466    | No file  | `d768594c2272`  |
| 457    | No file  | `d768594c2272`  |
| 452    | No file  | `d768594c2272`  |
| 449    | No file  | `d768594c2272`  |
| 435    | No file  | `d768594c2272`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                   |
| --------------------- | -------- | ------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Servant names (LOC type 6, `str_id1` = `character_id`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No magic and no trailer: a count, then the rows to the end of the file.

| Offset  | Type       | Field | Notes                                  |
| ------- | ---------- | ----- | -------------------------------------- |
| `+0x00` | u32        | count | 418 on client 3464                     |
| `+0x04` | Row[count] | rows  | `count` rows of 4 bytes, ending at EOF |

### Row (4 bytes)

| Offset  | Type | Field        | Notes                                           |
| ------- | ---- | ------------ | ----------------------------------------------- |
| `+0x00` | u16  | character_id | Servant character, as in `characterstatic.dbss` |
| `+0x02` | u16  | max_level    | Highest level                                   |

## Notes

- On client 3464 every `max_level` equals the highest `level` that
  `servantexperience.dbss` holds for the same `character_id`, and both files
  list the same 418 servants: 161 at 100, 132 at 30, 95 at 1, 20 at 15,
  3 at 10, 2 at 20 and 5 at 0.
- The parser is `_bss/servantexperiencemaxlevel/parser.py`; the
  `servantexperience.dbss` tests check that both files agree.
