# `employeeclientspawn.dbss` Format

## Purpose

Where the sailors stand on a ship: one row per boat character and position
index, with a position and a facing. The ships are the boat characters of
[`employeecharactership.dbss`](employeecharactership_dbss.md), and the
number of rows per ship matches its `employee_spawn_count` (see Notes).
Companion `employeeclientspawnoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ----- | ------------- | --------- |
| 1      | 1267 and later | 3483    | `employeeclientspawn.dbss`       | 724   | 36 Row        | 20        |
| 1      | 1267 and later | 3483    | `employeeclientspawnoffset.dbss` | 436   | 36 Offset Row | 12        |

| Layout | File                             | Known          | Unknown    |
| ------ | -------------------------------- | -------------- | ---------- |
| 1      | `employeeclientspawn.dbss`       | 724 B (100.0%) | 0 B (0.0%) |
| 1      | `employeeclientspawnoffset.dbss` | 436 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `298f23fe616f`  |
| 3482   | Layout 1 | `298f23fe616f`  |
| 3474   | Layout 1 | `298f23fe616f`  |
| 3473   | Layout 1 | `298f23fe616f`  |
| 3464   | Layout 1 | `298f23fe616f`  |
| 3458   | Layout 1 | `298f23fe616f`  |
| 3454   | Layout 1 | `298f23fe616f`  |
| 3444   | Layout 1 | `298f23fe616f`  |
| 3435   | Layout 1 | `298f23fe616f`  |
| 3426   | Layout 1 | `298f23fe616f`  |
| 3418   | Layout 1 | `298f23fe616f`  |
| 3412   | Layout 1 | `298f23fe616f`  |
| 3402   | Layout 1 | `298f23fe616f`  |
| 3396   | Layout 1 | `298f23fe616f`  |
| 3387   | Layout 1 | `298f23fe616f`  |
| 3381   | Layout 1 | `298f23fe616f`  |
| 3373   | Layout 1 | `298f23fe616f`  |
| 3364   | Layout 1 | `298f23fe616f`  |
| 3356   | Layout 1 | `298f23fe616f`  |
| 3349   | Layout 1 | `298f23fe616f`  |
| 3342   | Layout 1 | `298f23fe616f`  |
| 3335   | Layout 1 | `298f23fe616f`  |
| 3326   | Layout 1 | `298f23fe616f`  |
| 3321   | Layout 1 | `298f23fe616f`  |
| 3314   | Layout 1 | `298f23fe616f`  |
| 3303   | Layout 1 | `298f23fe616f`  |
| 3302   | Layout 1 | `298f23fe616f`  |
| 3293   | Layout 1 | `298f23fe616f`  |
| 3283   | Layout 1 | `298f23fe616f`  |
| 3275   | Layout 1 | `298f23fe616f`  |
| 3267   | Layout 1 | `298f23fe616f`  |
| 3258   | Layout 1 | `298f23fe616f`  |
| 3251   | Layout 1 | `298f23fe616f`  |
| 3242   | Layout 1 | `298f23fe616f`  |
| 3235   | Layout 1 | `298f23fe616f`  |
| 3229   | Layout 1 | `298f23fe616f`  |
| 3212   | Layout 1 | `298f23fe616f`  |
| 3203   | Layout 1 | `298f23fe616f`  |
| 3193   | Layout 1 | `298f23fe616f`  |
| 3186   | Layout 1 | `298f23fe616f`  |
| 3177   | Layout 1 | `298f23fe616f`  |
| 3169   | Layout 1 | `298f23fe616f`  |
| 3158   | Layout 1 | `298f23fe616f`  |
| 3151   | Layout 1 | `298f23fe616f`  |
| 3144   | Layout 1 | `298f23fe616f`  |
| 3133   | Layout 1 | `298f23fe616f`  |
| 3125   | Layout 1 | `298f23fe616f`  |
| 3118   | Layout 1 | `298f23fe616f`  |
| 3111   | Layout 1 | `298f23fe616f`  |
| 3103   | Layout 1 | `298f23fe616f`  |
| 3095   | Layout 1 | `298f23fe616f`  |
| 3086   | Layout 1 | `298f23fe616f`  |
| 3072   | Layout 1 | `298f23fe616f`  |
| 3062   | Layout 1 | `298f23fe616f`  |
| 3052   | Layout 1 | `298f23fe616f`  |
| 3045   | Layout 1 | `298f23fe616f`  |
| 3037   | Layout 1 | `298f23fe616f`  |
| 3030   | Layout 1 | `298f23fe616f`  |
| 3021   | Layout 1 | `298f23fe616f`  |
| 3012   | Layout 1 | `298f23fe616f`  |
| 3002   | Layout 1 | `298f23fe616f`  |
| 2995   | Layout 1 | `298f23fe616f`  |
| 2987   | Layout 1 | `298f23fe616f`  |
| 2978   | Layout 1 | `298f23fe616f`  |
| 2970   | Layout 1 | `298f23fe616f`  |
| 2959   | Layout 1 | `298f23fe616f`  |
| 2951   | Layout 1 | `298f23fe616f`  |
| 2942   | Layout 1 | `298f23fe616f`  |
| 2935   | Layout 1 | `298f23fe616f`  |
| 2932   | Layout 1 | `298f23fe616f`  |
| 2923   | Layout 1 | `298f23fe616f`  |
| 2919   | Layout 1 | `298f23fe616f`  |
| 2907   | Layout 1 | `298f23fe616f`  |
| 2900   | Layout 1 | `298f23fe616f`  |
| 2891   | Layout 1 | `298f23fe616f`  |
| 2882   | Layout 1 | `298f23fe616f`  |
| 2872   | Layout 1 | `298f23fe616f`  |
| 2863   | Layout 1 | `298f23fe616f`  |
| 2855   | Layout 1 | `298f23fe616f`  |
| 2849   | Layout 1 | `298f23fe616f`  |
| 2844   | Layout 1 | `298f23fe616f`  |
| 2834   | Layout 1 | `298f23fe616f`  |
| 2825   | Layout 1 | `298f23fe616f`  |
| 2819   | Layout 1 | `298f23fe616f`  |
| 2811   | Layout 1 | `298f23fe616f`  |
| 2803   | Layout 1 | `298f23fe616f`  |
| 2794   | Layout 1 | `298f23fe616f`  |
| 2783   | Layout 1 | `298f23fe616f`  |
| 2774   | Layout 1 | `298f23fe616f`  |
| 2765   | Layout 1 | `298f23fe616f`  |
| 2756   | Layout 1 | `298f23fe616f`  |
| 2750   | Layout 1 | `298f23fe616f`  |
| 2743   | Layout 1 | `298f23fe616f`  |
| 2736   | Layout 1 | `298f23fe616f`  |
| 2726   | Layout 1 | `298f23fe616f`  |
| 2717   | Layout 1 | `298f23fe616f`  |
| 2709   | Layout 1 | `298f23fe616f`  |
| 2703   | Layout 1 | `298f23fe616f`  |
| 2695   | Layout 1 | `298f23fe616f`  |
| 2684   | Layout 1 | `298f23fe616f`  |
| 2672   | Layout 1 | `298f23fe616f`  |
| 2665   | Layout 1 | `298f23fe616f`  |
| 2657   | Layout 1 | `298f23fe616f`  |
| 2649   | Layout 1 | `298f23fe616f`  |
| 2644   | Layout 1 | `298f23fe616f`  |
| 2637   | Layout 1 | `298f23fe616f`  |
| 2629   | Layout 1 | `298f23fe616f`  |
| 2619   | Layout 1 | `298f23fe616f`  |
| 2612   | Layout 1 | `298f23fe616f`  |
| 2606   | Layout 1 | `298f23fe616f`  |
| 2602   | Layout 1 | `298f23fe616f`  |
| 2601   | Layout 1 | `298f23fe616f`  |
| 2592   | Layout 1 | `298f23fe616f`  |
| 2583   | Layout 1 | `298f23fe616f`  |
| 2575   | Layout 1 | `298f23fe616f`  |
| 2567   | Layout 1 | `298f23fe616f`  |
| 2560   | Layout 1 | `298f23fe616f`  |
| 2553   | Layout 1 | `298f23fe616f`  |
| 2545   | Layout 1 | `298f23fe616f`  |
| 2538   | Layout 1 | `298f23fe616f`  |
| 2529   | Layout 1 | `298f23fe616f`  |
| 2519   | Layout 1 | `298f23fe616f`  |
| 2513   | Layout 1 | `298f23fe616f`  |
| 2510   | Layout 1 | `298f23fe616f`  |
| 2507   | Layout 1 | `298f23fe616f`  |
| 2503   | Layout 1 | `298f23fe616f`  |
| 2498   | Layout 1 | `298f23fe616f`  |
| 2492   | Layout 1 | `298f23fe616f`  |
| 2487   | Layout 1 | `298f23fe616f`  |
| 2480   | Layout 1 | `298f23fe616f`  |
| 2474   | Layout 1 | `298f23fe616f`  |
| 2468   | Layout 1 | `298f23fe616f`  |
| 2460   | Layout 1 | `298f23fe616f`  |
| 2453   | Layout 1 | `298f23fe616f`  |
| 2444   | Layout 1 | `298f23fe616f`  |
| 2438   | Layout 1 | `298f23fe616f`  |
| 2434   | Layout 1 | `298f23fe616f`  |
| 2429   | Layout 1 | `298f23fe616f`  |
| 2421   | Layout 1 | `298f23fe616f`  |
| 2414   | Layout 1 | `298f23fe616f`  |
| 2407   | Layout 1 | `298f23fe616f`  |
| 2401   | Layout 1 | `298f23fe616f`  |
| 2397   | Layout 1 | `298f23fe616f`  |
| 2393   | Layout 1 | `298f23fe616f`  |
| 2384   | Layout 1 | `298f23fe616f`  |
| 2378   | Layout 1 | `298f23fe616f`  |
| 2372   | Layout 1 | `298f23fe616f`  |
| 2358   | Layout 1 | `298f23fe616f`  |
| 2352   | Layout 1 | `298f23fe616f`  |
| 2347   | Layout 1 | `298f23fe616f`  |
| 2343   | Layout 1 | `298f23fe616f`  |
| 2335   | Layout 1 | `298f23fe616f`  |
| 2327   | Layout 1 | `298f23fe616f`  |
| 2324   | Layout 1 | `298f23fe616f`  |
| 2319   | Layout 1 | `298f23fe616f`  |
| 2313   | Layout 1 | `298f23fe616f`  |
| 2308   | Layout 1 | `298f23fe616f`  |
| 2302   | Layout 1 | `298f23fe616f`  |
| 2295   | Layout 1 | `298f23fe616f`  |
| 2290   | Layout 1 | `298f23fe616f`  |
| 2284   | Layout 1 | `298f23fe616f`  |
| 2276   | Layout 1 | `298f23fe616f`  |
| 2269   | Layout 1 | `298f23fe616f`  |
| 2259   | Layout 1 | `298f23fe616f`  |
| 2250   | Layout 1 | `298f23fe616f`  |
| 2243   | Layout 1 | `298f23fe616f`  |
| 2235   | Layout 1 | `298f23fe616f`  |
| 2229   | Layout 1 | `298f23fe616f`  |
| 2224   | Layout 1 | `298f23fe616f`  |
| 2218   | Layout 1 | `298f23fe616f`  |
| 2215   | Layout 1 | `298f23fe616f`  |
| 2207   | Layout 1 | `298f23fe616f`  |
| 2203   | Layout 1 | `298f23fe616f`  |
| 2196   | Layout 1 | `298f23fe616f`  |
| 2192   | Layout 1 | `298f23fe616f`  |
| 2189   | Layout 1 | `298f23fe616f`  |
| 2183   | Layout 1 | `298f23fe616f`  |
| 2179   | Layout 1 | `298f23fe616f`  |
| 2171   | Layout 1 | `298f23fe616f`  |
| 2163   | Layout 1 | `298f23fe616f`  |
| 2156   | Layout 1 | `298f23fe616f`  |
| 2151   | Layout 1 | `298f23fe616f`  |
| 2147   | Layout 1 | `298f23fe616f`  |
| 2142   | Layout 1 | `298f23fe616f`  |
| 2138   | Layout 1 | `298f23fe616f`  |
| 2134   | Layout 1 | `298f23fe616f`  |
| 2130   | Layout 1 | `298f23fe616f`  |
| 2122   | Layout 1 | `298f23fe616f`  |
| 2107   | Layout 1 | `298f23fe616f`  |
| 2098   | Layout 1 | `298f23fe616f`  |
| 2089   | Layout 1 | `298f23fe616f`  |
| 2081   | Layout 1 | `298f23fe616f`  |
| 2073   | Layout 1 | `298f23fe616f`  |
| 2067   | Layout 1 | `298f23fe616f`  |
| 2063   | Layout 1 | `298f23fe616f`  |
| 2059   | Layout 1 | `298f23fe616f`  |
| 2052   | Layout 1 | `298f23fe616f`  |
| 2044   | Layout 1 | `298f23fe616f`  |
| 2039   | Layout 1 | `298f23fe616f`  |
| 2032   | Layout 1 | `298f23fe616f`  |
| 2025   | Layout 1 | `298f23fe616f`  |
| 2011   | Layout 1 | `298f23fe616f`  |
| 2005   | Layout 1 | `298f23fe616f`  |
| 2000   | Layout 1 | `298f23fe616f`  |
| 1996   | Layout 1 | `298f23fe616f`  |
| 1991   | Layout 1 | `298f23fe616f`  |
| 1985   | Layout 1 | `298f23fe616f`  |
| 1980   | Layout 1 | `298f23fe616f`  |
| 1969   | Layout 1 | `298f23fe616f`  |
| 1964   | Layout 1 | `298f23fe616f`  |
| 1958   | Layout 1 | `298f23fe616f`  |
| 1950   | Layout 1 | `298f23fe616f`  |
| 1945   | Layout 1 | `298f23fe616f`  |
| 1937   | Layout 1 | `298f23fe616f`  |
| 1933   | Layout 1 | `298f23fe616f`  |
| 1927   | Layout 1 | `298f23fe616f`  |
| 1921   | Layout 1 | `298f23fe616f`  |
| 1914   | Layout 1 | `298f23fe616f`  |
| 1908   | Layout 1 | `298f23fe616f`  |
| 1897   | Layout 1 | `298f23fe616f`  |
| 1892   | Layout 1 | `298f23fe616f`  |
| 1886   | Layout 1 | `298f23fe616f`  |
| 1881   | Layout 1 | `298f23fe616f`  |
| 1871   | Layout 1 | `298f23fe616f`  |
| 1866   | Layout 1 | `298f23fe616f`  |
| 1862   | Layout 1 | `298f23fe616f`  |
| 1854   | Layout 1 | `298f23fe616f`  |
| 1846   | Layout 1 | `298f23fe616f`  |
| 1838   | Layout 1 | `298f23fe616f`  |
| 1832   | Layout 1 | `298f23fe616f`  |
| 1826   | Layout 1 | `298f23fe616f`  |
| 1822   | Layout 1 | `298f23fe616f`  |
| 1818   | Layout 1 | `298f23fe616f`  |
| 1804   | Layout 1 | `298f23fe616f`  |
| 1794   | Layout 1 | `298f23fe616f`  |
| 1790   | Layout 1 | `298f23fe616f`  |
| 1784   | Layout 1 | `298f23fe616f`  |
| 1774   | Layout 1 | `298f23fe616f`  |
| 1771   | Layout 1 | `298f23fe616f`  |
| 1762   | Layout 1 | `298f23fe616f`  |
| 1759   | Layout 1 | `298f23fe616f`  |
| 1754   | Layout 1 | `298f23fe616f`  |
| 1749   | Layout 1 | `298f23fe616f`  |
| 1743   | Layout 1 | `298f23fe616f`  |
| 1737   | Layout 1 | `298f23fe616f`  |
| 1731   | Layout 1 | `298f23fe616f`  |
| 1725   | Layout 1 | `298f23fe616f`  |
| 1717   | Layout 1 | `298f23fe616f`  |
| 1710   | Layout 1 | `298f23fe616f`  |
| 1704   | Layout 1 | `298f23fe616f`  |
| 1698   | Layout 1 | `298f23fe616f`  |
| 1690   | Layout 1 | `298f23fe616f`  |
| 1685   | Layout 1 | `298f23fe616f`  |
| 1680   | Layout 1 | `298f23fe616f`  |
| 1674   | Layout 1 | `298f23fe616f`  |
| 1668   | Layout 1 | `298f23fe616f`  |
| 1659   | Layout 1 | `298f23fe616f`  |
| 1649   | Layout 1 | `298f23fe616f`  |
| 1642   | Layout 1 | `298f23fe616f`  |
| 1636   | Layout 1 | `298f23fe616f`  |
| 1628   | Layout 1 | `298f23fe616f`  |
| 1622   | Layout 1 | `298f23fe616f`  |
| 1614   | Layout 1 | `298f23fe616f`  |
| 1608   | Layout 1 | `298f23fe616f`  |
| 1602   | Layout 1 | `298f23fe616f`  |
| 1598   | Layout 1 | `298f23fe616f`  |
| 1594   | Layout 1 | `298f23fe616f`  |
| 1590   | Layout 1 | `298f23fe616f`  |
| 1587   | Layout 1 | `298f23fe616f`  |
| 1584   | Layout 1 | `298f23fe616f`  |
| 1579   | Layout 1 | `298f23fe616f`  |
| 1572   | Layout 1 | `298f23fe616f`  |
| 1565   | Layout 1 | `298f23fe616f`  |
| 1559   | Layout 1 | `298f23fe616f`  |
| 1554   | Layout 1 | `298f23fe616f`  |
| 1547   | Layout 1 | `298f23fe616f`  |
| 1537   | Layout 1 | `298f23fe616f`  |
| 1529   | Layout 1 | `298f23fe616f`  |
| 1524   | Layout 1 | `298f23fe616f`  |
| 1519   | Layout 1 | `298f23fe616f`  |
| 1509   | Layout 1 | `298f23fe616f`  |
| 1506   | Layout 1 | `298f23fe616f`  |
| 1504   | Layout 1 | `298f23fe616f`  |
| 1500   | Layout 1 | `298f23fe616f`  |
| 1493   | Layout 1 | `298f23fe616f`  |
| 1489   | Layout 1 | `298f23fe616f`  |
| 1485   | Layout 1 | `298f23fe616f`  |
| 1481   | Layout 1 | `298f23fe616f`  |
| 1474   | Layout 1 | `298f23fe616f`  |
| 1466   | Layout 1 | `298f23fe616f`  |
| 1462   | Layout 1 | `298f23fe616f`  |
| 1459   | Layout 1 | `298f23fe616f`  |
| 1453   | Layout 1 | `298f23fe616f`  |
| 1450   | Layout 1 | `298f23fe616f`  |
| 1445   | Layout 1 | `298f23fe616f`  |
| 1439   | Layout 1 | `298f23fe616f`  |
| 1433   | Layout 1 | `298f23fe616f`  |
| 1430   | Layout 1 | `298f23fe616f`  |
| 1426   | Layout 1 | `298f23fe616f`  |
| 1421   | Layout 1 | `298f23fe616f`  |
| 1417   | Layout 1 | `298f23fe616f`  |
| 1416   | Layout 1 | `298f23fe616f`  |
| 1409   | Layout 1 | `298f23fe616f`  |
| 1405   | Layout 1 | `298f23fe616f`  |
| 1401   | Layout 1 | `298f23fe616f`  |
| 1396   | Layout 1 | `298f23fe616f`  |
| 1391   | Layout 1 | `298f23fe616f`  |
| 1390   | Layout 1 | `298f23fe616f`  |
| 1386   | Layout 1 | `298f23fe616f`  |
| 1381   | Layout 1 | `298f23fe616f`  |
| 1379   | Layout 1 | `298f23fe616f`  |
| 1372   | Layout 1 | `298f23fe616f`  |
| 1366   | Layout 1 | `298f23fe616f`  |
| 1364   | Layout 1 | `298f23fe616f`  |
| 1363   | Layout 1 | `298f23fe616f`  |
| 1360   | Layout 1 | `298f23fe616f`  |
| 1358   | Layout 1 | `298f23fe616f`  |
| 1355   | Layout 1 | `298f23fe616f`  |
| 1351   | Layout 1 | `298f23fe616f`  |
| 1348   | Layout 1 | `298f23fe616f`  |
| 1346   | Layout 1 | `298f23fe616f`  |
| 1341   | Layout 1 | `298f23fe616f`  |
| 1340   | Layout 1 | `298f23fe616f`  |
| 1338   | Layout 1 | `298f23fe616f`  |
| 1335   | Layout 1 | `298f23fe616f`  |
| 1333   | Layout 1 | `298f23fe616f`  |
| 1329   | Layout 1 | `298f23fe616f`  |
| 1327   | Layout 1 | `298f23fe616f`  |
| 1324   | Layout 1 | `298f23fe616f`  |
| 1321   | Layout 1 | `298f23fe616f`  |
| 1319   | Layout 1 | `298f23fe616f`  |
| 1318   | Layout 1 | `298f23fe616f`  |
| 1316   | Layout 1 | `298f23fe616f`  |
| 1313   | Layout 1 | `298f23fe616f`  |
| 1311   | Layout 1 | `298f23fe616f`  |
| 1309   | Layout 1 | `298f23fe616f`  |
| 1304   | Layout 1 | `298f23fe616f`  |
| 1292   | Layout 1 | `298f23fe616f`  |
| 1286   | Layout 1 | `298f23fe616f`  |
| 1280   | Layout 1 | `298f23fe616f`  |
| 1276   | Layout 1 | `298f23fe616f`  |
| 1267   | Layout 1 | `298f23fe616f`  |
| 1261   | No file  | `298f23fe616f`  |
| 1256   | No file  | `298f23fe616f`  |
| 1250   | No file  | `298f23fe616f`  |
| 1246   | No file  | `298f23fe616f`  |
| 1239   | No file  | `298f23fe616f`  |
| 1230   | No file  | `298f23fe616f`  |
| 1226   | No file  | `298f23fe616f`  |
| 1220   | No file  | `298f23fe616f`  |
| 1217   | No file  | `298f23fe616f`  |
| 1211   | No file  | `298f23fe616f`  |
| 1210   | No file  | `298f23fe616f`  |
| 1208   | No file  | `298f23fe616f`  |
| 1203   | No file  | `298f23fe616f`  |
| 1197   | No file  | `298f23fe616f`  |
| 1194   | No file  | `298f23fe616f`  |
| 1192   | No file  | `298f23fe616f`  |
| 1187   | No file  | `298f23fe616f`  |
| 1183   | No file  | `298f23fe616f`  |
| 1177   | No file  | `298f23fe616f`  |
| 1173   | No file  | `298f23fe616f`  |
| 1167   | No file  | `298f23fe616f`  |
| 1164   | No file  | `298f23fe616f`  |
| 1156   | No file  | `298f23fe616f`  |
| 1149   | No file  | `298f23fe616f`  |
| 1144   | No file  | `298f23fe616f`  |
| 1137   | No file  | `298f23fe616f`  |
| 1132   | No file  | `298f23fe616f`  |
| 1127   | No file  | `298f23fe616f`  |
| 1122   | No file  | `298f23fe616f`  |
| 1118   | No file  | `298f23fe616f`  |
| 1114   | No file  | `298f23fe616f`  |
| 1109   | No file  | `298f23fe616f`  |
| 1102   | No file  | `298f23fe616f`  |
| 1096   | No file  | `298f23fe616f`  |
| 1088   | No file  | `298f23fe616f`  |
| 1081   | No file  | `298f23fe616f`  |
| 1076   | No file  | `298f23fe616f`  |
| 1069   | No file  | `298f23fe616f`  |
| 1064   | No file  | `298f23fe616f`  |
| 1058   | No file  | `298f23fe616f`  |
| 1051   | No file  | `298f23fe616f`  |
| 1044   | No file  | `298f23fe616f`  |
| 1036   | No file  | `298f23fe616f`  |
| 1026   | No file  | `298f23fe616f`  |
| 1016   | No file  | `298f23fe616f`  |
| 1009   | No file  | `298f23fe616f`  |
| 1005   | No file  | `298f23fe616f`  |
| 1000   | No file  | `298f23fe616f`  |
| 998    | No file  | `298f23fe616f`  |
| 990    | No file  | `298f23fe616f`  |
| 979    | No file  | `298f23fe616f`  |
| 972    | No file  | `298f23fe616f`  |
| 963    | No file  | `298f23fe616f`  |
| 955    | No file  | `298f23fe616f`  |
| 946    | No file  | `298f23fe616f`  |
| 938    | No file  | `298f23fe616f`  |
| 927    | No file  | `298f23fe616f`  |
| 911    | No file  | `298f23fe616f`  |
| 904    | No file  | `298f23fe616f`  |
| 899    | No file  | `298f23fe616f`  |
| 894    | No file  | `298f23fe616f`  |
| 885    | No file  | `298f23fe616f`  |
| 879    | No file  | `298f23fe616f`  |
| 872    | No file  | `298f23fe616f`  |
| 864    | No file  | `298f23fe616f`  |
| 855    | No file  | `298f23fe616f`  |
| 853    | No file  | `298f23fe616f`  |
| 845    | No file  | `298f23fe616f`  |
| 837    | No file  | `298f23fe616f`  |
| 829    | No file  | `298f23fe616f`  |
| 822    | No file  | `298f23fe616f`  |
| 814    | No file  | `298f23fe616f`  |
| 805    | No file  | `298f23fe616f`  |
| 794    | No file  | `298f23fe616f`  |
| 787    | No file  | `298f23fe616f`  |
| 780    | No file  | `298f23fe616f`  |
| 771    | No file  | `298f23fe616f`  |
| 760    | No file  | `298f23fe616f`  |
| 748    | No file  | `298f23fe616f`  |
| 741    | No file  | `298f23fe616f`  |
| 736    | No file  | `298f23fe616f`  |
| 731    | No file  | `298f23fe616f`  |
| 723    | No file  | `298f23fe616f`  |
| 711    | No file  | `298f23fe616f`  |
| 707    | No file  | `298f23fe616f`  |
| 697    | No file  | `298f23fe616f`  |
| 689    | No file  | `298f23fe616f`  |
| 683    | No file  | `298f23fe616f`  |
| 678    | No file  | `298f23fe616f`  |
| 670    | No file  | `298f23fe616f`  |
| 661    | No file  | `298f23fe616f`  |
| 656    | No file  | `298f23fe616f`  |
| 652    | No file  | `298f23fe616f`  |
| 643    | No file  | `298f23fe616f`  |
| 637    | No file  | `298f23fe616f`  |
| 630    | No file  | `298f23fe616f`  |
| 627    | No file  | `298f23fe616f`  |
| 621    | No file  | `298f23fe616f`  |
| 617    | No file  | `298f23fe616f`  |
| 615    | No file  | `298f23fe616f`  |
| 606    | No file  | `298f23fe616f`  |
| 599    | No file  | `298f23fe616f`  |
| 592    | No file  | `298f23fe616f`  |
| 586    | No file  | `298f23fe616f`  |
| 577    | No file  | `298f23fe616f`  |
| 569    | No file  | `298f23fe616f`  |
| 561    | No file  | `298f23fe616f`  |
| 554    | No file  | `298f23fe616f`  |
| 542    | No file  | `298f23fe616f`  |
| 532    | No file  | `298f23fe616f`  |
| 531    | No file  | `298f23fe616f`  |
| 526    | No file  | `298f23fe616f`  |
| 521    | No file  | `298f23fe616f`  |
| 517    | No file  | `298f23fe616f`  |
| 510    | No file  | `298f23fe616f`  |
| 508    | No file  | `298f23fe616f`  |
| 504    | No file  | `298f23fe616f`  |
| 497    | No file  | `298f23fe616f`  |
| 491    | No file  | `298f23fe616f`  |
| 485    | No file  | `298f23fe616f`  |
| 478    | No file  | `298f23fe616f`  |
| 472    | No file  | `298f23fe616f`  |
| 466    | No file  | `298f23fe616f`  |
| 457    | No file  | `298f23fe616f`  |
| 452    | No file  | `298f23fe616f`  |
| 449    | No file  | `298f23fe616f`  |
| 435    | No file  | `298f23fe616f`  |

<!-- versions:end -->

## Companion Files

| File                                              | Required | Role                                                                          |
| ------------------------------------------------- | -------- | ----------------------------------------------------------------------------- |
| `employeeclientspawnoffset.dbss`                  | Optional | `(character_key, index) -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row  |

Ship names come from LOC type 6, `str_id1` = `character_key`, `str_id4` 0
("Epheria Sailboat" for `31001`).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 36 x 20 = 724 bytes.

### Row (20 bytes)

| Offset  | Type | Field            | Notes                                                                  |
| ------- | ---- | ---------------- | ---------------------------------------------------------------------- |
| `+0x00` | u16  | character_key    | Boat character, a `character_key` of `employeecharactership.dbss`      |
| `+0x02` | u16  | index            | Position number on that ship, from `0`                                 |
| `+0x04` | f32  | spawn_position_x | Whole numbers from `-450` to `430` (client 3474)                        |
| `+0x08` | f32  | spawn_position_y | `300` or `700` (client 3474)                                           |
| `+0x0C` | f32  | spawn_position_z | Whole numbers from `-1000` to `200` (client 3474)                       |
| `+0x10` | f32  | spawn_direction  | Whole numbers from `45` to `330` (client 3474)                          |

The rows are grouped by `index` in the order 4, 1, 0, 3, 2 on clients 1784
and 3474, and the ships within a group are in no key order (`31055` index
4 first).

### `employeeclientspawnoffset.dbss`

Bare offset table into `employeeclientspawn.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `employeeclientspawn.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key | Ship of the row it points at                                |
| `+0x02` | u16  | index         | Position number of that row                                 |
| `+0x04` | u32  | data_offset   | Absolute offset of the row in `employeeclientspawn.dbss`, at `character_key` |
| `+0x08` | u32  | data_size     | `20` on every row: the whole row                            |

The parser reads the first u32 as one key, `index << 16 | character_key`,
with `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py` and splits
it. The index rows are in another order than the file; on clients 1784 and
3474 every index row points at the row with its key.

## Field Names

The `EmployeeShipSpawnPosition_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `CharacterKey`, `Index`,
`SpawnPosition` (three numbers, `100, 300, -450`) and `SpawnDirection`; its
36 rows match the file on all 36 keys and all four values, on client 1784
and on client 3474. The `.xlsx` copy of the sheet names each ship in a note
column (`#DisplayName`, `에페리아 범선` for `31001`). The client Lua has no
getter for the table.

| Field            | Column                     |
| ---------------- | -------------------------- |
| character_key    | `CharacterKey`             |
| index            | `Index`                    |
| spawn_position_x | `SpawnPosition`, first     |
| spawn_position_y | `SpawnPosition`, second    |
| spawn_position_z | `SpawnPosition`, third     |
| spawn_direction  | `SpawnDirection`           |

## Notes

- Ships share their positions and differ in `spawn_direction`: the five
  Epheria Carracks (`31045`, `31054` to `31057`) have the same five
  positions, the Epheria Caravel (`31048`) and Galleass (`31049`) the same
  three, and the five ships with one sailor (Epheria Sailboat, Frigate,
  their Improved versions and the Bartali Sailboat) all stand it at
  `100, 300, -450`. The positions are therefore relative to the ship, not
  world coordinates.
- On client 3474, 12 of the 13 ships with an `employee_spawn_count` above
  `0` in `employeecharactership.dbss` have that many rows here (1, 3 or 5).
  The Panokseon (`31025`, `employee_spawn_count` 5) has no rows.

## Open Questions

### Panokseon Without Positions

The Panokseon (`31025`) has `employee_spawn_count` 5 in
`employeecharactership.dbss` but no row in this file on client 3474. The
client may fall back to a default position for its sailors, or the ship
does not show them.
