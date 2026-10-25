# `musicoption.bss` Format

## Purpose

Options of the instrument performance system: the distance at which other
players hear a performance, and since client 2519 eight more bytes. The
values start right after the PABR magic, in the slot where a table keeps
its record count, and end at the string table. On client 3474 the distance
is `1500`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File              | Bytes | Records        | Row bytes |
| ------ | -------------- | ----------------- | ----- | -------------- | --------- |
| 2      | 2378 and later | `musicoption.bss` | 28    | 1 String Table | 4         |
| 1      | 1348 to 2372   | `musicoption.bss` | 20    | 1 String Table | 4         |

| Layout | File              | Known         | Unknown     |
| ------ | ----------------- | ------------- | ----------- |
| 2      | `musicoption.bss` | 20 B (71.4%)  | 8 B (28.6%) |
| 1      | `musicoption.bss` | 20 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `ef329a9952ab`  |
| 3482   | Layout 2 | `ef329a9952ab`  |
| 3474   | Layout 2 | `ef329a9952ab`  |
| 3473   | Layout 2 | `ef329a9952ab`  |
| 3464   | Layout 2 | `ef329a9952ab`  |
| 3458   | Layout 2 | `ef329a9952ab`  |
| 3454   | Layout 2 | `ef329a9952ab`  |
| 3444   | Layout 2 | `ef329a9952ab`  |
| 3435   | Layout 2 | `ef329a9952ab`  |
| 3426   | Layout 2 | `ef329a9952ab`  |
| 3418   | Layout 2 | `ef329a9952ab`  |
| 3412   | Layout 2 | `ef329a9952ab`  |
| 3402   | Layout 2 | `ef329a9952ab`  |
| 3396   | Layout 2 | `ef329a9952ab`  |
| 3387   | Layout 2 | `ef329a9952ab`  |
| 3381   | Layout 2 | `ef329a9952ab`  |
| 3373   | Layout 2 | `ef329a9952ab`  |
| 3364   | Layout 2 | `ef329a9952ab`  |
| 3356   | Layout 2 | `ef329a9952ab`  |
| 3349   | Layout 2 | `ef329a9952ab`  |
| 3342   | Layout 2 | `ef329a9952ab`  |
| 3335   | Layout 2 | `ef329a9952ab`  |
| 3326   | Layout 2 | `ef329a9952ab`  |
| 3321   | Layout 2 | `ef329a9952ab`  |
| 3314   | Layout 2 | `ef329a9952ab`  |
| 3303   | Layout 2 | `ef329a9952ab`  |
| 3302   | Layout 2 | `ef329a9952ab`  |
| 3293   | Layout 2 | `ef329a9952ab`  |
| 3283   | Layout 2 | `ef329a9952ab`  |
| 3275   | Layout 2 | `ef329a9952ab`  |
| 3267   | Layout 2 | `ef329a9952ab`  |
| 3258   | Layout 2 | `ef329a9952ab`  |
| 3251   | Layout 2 | `ef329a9952ab`  |
| 3242   | Layout 2 | `ef329a9952ab`  |
| 3235   | Layout 2 | `ef329a9952ab`  |
| 3229   | Layout 2 | `ef329a9952ab`  |
| 3212   | Layout 2 | `ef329a9952ab`  |
| 3203   | Layout 2 | `ef329a9952ab`  |
| 3193   | Layout 2 | `ef329a9952ab`  |
| 3186   | Layout 2 | `ef329a9952ab`  |
| 3177   | Layout 2 | `ef329a9952ab`  |
| 3169   | Layout 2 | `ef329a9952ab`  |
| 3158   | Layout 2 | `ef329a9952ab`  |
| 3151   | Layout 2 | `ef329a9952ab`  |
| 3144   | Layout 2 | `ef329a9952ab`  |
| 3133   | Layout 2 | `ef329a9952ab`  |
| 3125   | Layout 2 | `ef329a9952ab`  |
| 3118   | Layout 2 | `ef329a9952ab`  |
| 3111   | Layout 2 | `ef329a9952ab`  |
| 3103   | Layout 2 | `ef329a9952ab`  |
| 3095   | Layout 2 | `ef329a9952ab`  |
| 3086   | Layout 2 | `ef329a9952ab`  |
| 3072   | Layout 2 | `ef329a9952ab`  |
| 3062   | Layout 2 | `ef329a9952ab`  |
| 3052   | Layout 2 | `ef329a9952ab`  |
| 3045   | Layout 2 | `ef329a9952ab`  |
| 3037   | Layout 2 | `ef329a9952ab`  |
| 3030   | Layout 2 | `ef329a9952ab`  |
| 3021   | Layout 2 | `ef329a9952ab`  |
| 3012   | Layout 2 | `ef329a9952ab`  |
| 3002   | Layout 2 | `ef329a9952ab`  |
| 2995   | Layout 2 | `ef329a9952ab`  |
| 2987   | Layout 2 | `ef329a9952ab`  |
| 2978   | Layout 2 | `ef329a9952ab`  |
| 2970   | Layout 2 | `ef329a9952ab`  |
| 2959   | Layout 2 | `ef329a9952ab`  |
| 2951   | Layout 2 | `ef329a9952ab`  |
| 2942   | Layout 2 | `ef329a9952ab`  |
| 2935   | Layout 2 | `ef329a9952ab`  |
| 2932   | Layout 2 | `ef329a9952ab`  |
| 2923   | Layout 2 | `ef329a9952ab`  |
| 2919   | Layout 2 | `ef329a9952ab`  |
| 2907   | Layout 2 | `ef329a9952ab`  |
| 2900   | Layout 2 | `ef329a9952ab`  |
| 2891   | Layout 2 | `ef329a9952ab`  |
| 2882   | Layout 2 | `ef329a9952ab`  |
| 2872   | Layout 2 | `ef329a9952ab`  |
| 2863   | Layout 2 | `ef329a9952ab`  |
| 2855   | Layout 2 | `ef329a9952ab`  |
| 2849   | Layout 2 | `ef329a9952ab`  |
| 2844   | Layout 2 | `ef329a9952ab`  |
| 2834   | Layout 2 | `ef329a9952ab`  |
| 2825   | Layout 2 | `ef329a9952ab`  |
| 2819   | Layout 2 | `ef329a9952ab`  |
| 2811   | Layout 2 | `ef329a9952ab`  |
| 2803   | Layout 2 | `ef329a9952ab`  |
| 2794   | Layout 2 | `ef329a9952ab`  |
| 2783   | Layout 2 | `ef329a9952ab`  |
| 2774   | Layout 2 | `ef329a9952ab`  |
| 2765   | Layout 2 | `ef329a9952ab`  |
| 2756   | Layout 2 | `ef329a9952ab`  |
| 2750   | Layout 2 | `ef329a9952ab`  |
| 2743   | Layout 2 | `ef329a9952ab`  |
| 2736   | Layout 2 | `ef329a9952ab`  |
| 2726   | Layout 2 | `ef329a9952ab`  |
| 2717   | Layout 2 | `ef329a9952ab`  |
| 2709   | Layout 2 | `ef329a9952ab`  |
| 2703   | Layout 2 | `ef329a9952ab`  |
| 2695   | Layout 2 | `ef329a9952ab`  |
| 2684   | Layout 2 | `ef329a9952ab`  |
| 2672   | Layout 2 | `ef329a9952ab`  |
| 2665   | Layout 2 | `ef329a9952ab`  |
| 2657   | Layout 2 | `ef329a9952ab`  |
| 2649   | Layout 2 | `ef329a9952ab`  |
| 2644   | Layout 2 | `ef329a9952ab`  |
| 2637   | Layout 2 | `ef329a9952ab`  |
| 2629   | Layout 2 | `ef329a9952ab`  |
| 2619   | Layout 2 | `ef329a9952ab`  |
| 2612   | Layout 2 | `ef329a9952ab`  |
| 2606   | Layout 2 | `ef329a9952ab`  |
| 2602   | Layout 2 | `ef329a9952ab`  |
| 2601   | Layout 2 | `ef329a9952ab`  |
| 2592   | Layout 2 | `ef329a9952ab`  |
| 2583   | Layout 2 | `ef329a9952ab`  |
| 2575   | Layout 2 | `ef329a9952ab`  |
| 2567   | Layout 2 | `ef329a9952ab`  |
| 2560   | Layout 2 | `ef329a9952ab`  |
| 2553   | Layout 2 | `ef329a9952ab`  |
| 2545   | Layout 2 | `ef329a9952ab`  |
| 2538   | Layout 2 | `ef329a9952ab`  |
| 2529   | Layout 2 | `ef329a9952ab`  |
| 2519   | Layout 2 | `ef329a9952ab`  |
| 2513   | Layout 2 | `ef329a9952ab`  |
| 2510   | Layout 2 | `ef329a9952ab`  |
| 2507   | Layout 2 | `ef329a9952ab`  |
| 2503   | Layout 2 | `ef329a9952ab`  |
| 2498   | Layout 2 | `ef329a9952ab`  |
| 2492   | Layout 2 | `ef329a9952ab`  |
| 2487   | Layout 2 | `ef329a9952ab`  |
| 2480   | Layout 2 | `ef329a9952ab`  |
| 2474   | Layout 2 | `ef329a9952ab`  |
| 2468   | Layout 2 | `ef329a9952ab`  |
| 2460   | Layout 2 | `ef329a9952ab`  |
| 2453   | Layout 2 | `ef329a9952ab`  |
| 2444   | Layout 2 | `ef329a9952ab`  |
| 2438   | Layout 2 | `ef329a9952ab`  |
| 2434   | Layout 2 | `ef329a9952ab`  |
| 2429   | Layout 2 | `ef329a9952ab`  |
| 2421   | Layout 2 | `ef329a9952ab`  |
| 2414   | Layout 2 | `ef329a9952ab`  |
| 2407   | Layout 2 | `ef329a9952ab`  |
| 2401   | Layout 2 | `ef329a9952ab`  |
| 2397   | Layout 2 | `ef329a9952ab`  |
| 2393   | Layout 2 | `ef329a9952ab`  |
| 2384   | Layout 2 | `ef329a9952ab`  |
| 2378   | Layout 2 | `ef329a9952ab`  |
| 2372   | Layout 1 | `ef329a9952ab`  |
| 2358   | Layout 1 | `ef329a9952ab`  |
| 2352   | Layout 1 | `ef329a9952ab`  |
| 2347   | Layout 1 | `ef329a9952ab`  |
| 2343   | Layout 1 | `ef329a9952ab`  |
| 2335   | Layout 1 | `ef329a9952ab`  |
| 2327   | Layout 1 | `ef329a9952ab`  |
| 2324   | Layout 1 | `ef329a9952ab`  |
| 2319   | Layout 1 | `ef329a9952ab`  |
| 2313   | Layout 1 | `ef329a9952ab`  |
| 2308   | Layout 1 | `ef329a9952ab`  |
| 2302   | Layout 1 | `ef329a9952ab`  |
| 2295   | Layout 1 | `ef329a9952ab`  |
| 2290   | Layout 1 | `ef329a9952ab`  |
| 2284   | Layout 1 | `ef329a9952ab`  |
| 2276   | Layout 1 | `ef329a9952ab`  |
| 2269   | Layout 1 | `ef329a9952ab`  |
| 2259   | Layout 1 | `ef329a9952ab`  |
| 2250   | Layout 1 | `ef329a9952ab`  |
| 2243   | Layout 1 | `ef329a9952ab`  |
| 2235   | Layout 1 | `ef329a9952ab`  |
| 2229   | Layout 1 | `ef329a9952ab`  |
| 2224   | Layout 1 | `ef329a9952ab`  |
| 2218   | Layout 1 | `ef329a9952ab`  |
| 2215   | Layout 1 | `ef329a9952ab`  |
| 2207   | Layout 1 | `ef329a9952ab`  |
| 2203   | Layout 1 | `ef329a9952ab`  |
| 2196   | Layout 1 | `ef329a9952ab`  |
| 2192   | Layout 1 | `ef329a9952ab`  |
| 2189   | Layout 1 | `ef329a9952ab`  |
| 2183   | Layout 1 | `ef329a9952ab`  |
| 2179   | Layout 1 | `ef329a9952ab`  |
| 2171   | Layout 1 | `ef329a9952ab`  |
| 2163   | Layout 1 | `ef329a9952ab`  |
| 2156   | Layout 1 | `ef329a9952ab`  |
| 2151   | Layout 1 | `ef329a9952ab`  |
| 2147   | Layout 1 | `ef329a9952ab`  |
| 2142   | Layout 1 | `ef329a9952ab`  |
| 2138   | Layout 1 | `ef329a9952ab`  |
| 2134   | Layout 1 | `ef329a9952ab`  |
| 2130   | Layout 1 | `ef329a9952ab`  |
| 2122   | Layout 1 | `ef329a9952ab`  |
| 2107   | Layout 1 | `ef329a9952ab`  |
| 2098   | Layout 1 | `ef329a9952ab`  |
| 2089   | Layout 1 | `ef329a9952ab`  |
| 2081   | Layout 1 | `ef329a9952ab`  |
| 2073   | Layout 1 | `ef329a9952ab`  |
| 2067   | Layout 1 | `ef329a9952ab`  |
| 2063   | Layout 1 | `ef329a9952ab`  |
| 2059   | Layout 1 | `ef329a9952ab`  |
| 2052   | Layout 1 | `ef329a9952ab`  |
| 2044   | Layout 1 | `ef329a9952ab`  |
| 2039   | Layout 1 | `ef329a9952ab`  |
| 2032   | Layout 1 | `ef329a9952ab`  |
| 2025   | Layout 1 | `ef329a9952ab`  |
| 2011   | Layout 1 | `ef329a9952ab`  |
| 2005   | Layout 1 | `ef329a9952ab`  |
| 2000   | Layout 1 | `ef329a9952ab`  |
| 1996   | Layout 1 | `ef329a9952ab`  |
| 1991   | Layout 1 | `ef329a9952ab`  |
| 1985   | Layout 1 | `ef329a9952ab`  |
| 1980   | Layout 1 | `ef329a9952ab`  |
| 1969   | Layout 1 | `ef329a9952ab`  |
| 1964   | Layout 1 | `ef329a9952ab`  |
| 1958   | Layout 1 | `ef329a9952ab`  |
| 1950   | Layout 1 | `ef329a9952ab`  |
| 1945   | Layout 1 | `ef329a9952ab`  |
| 1937   | Layout 1 | `ef329a9952ab`  |
| 1933   | Layout 1 | `ef329a9952ab`  |
| 1927   | Layout 1 | `ef329a9952ab`  |
| 1921   | Layout 1 | `ef329a9952ab`  |
| 1914   | Layout 1 | `ef329a9952ab`  |
| 1908   | Layout 1 | `ef329a9952ab`  |
| 1897   | Layout 1 | `ef329a9952ab`  |
| 1892   | Layout 1 | `ef329a9952ab`  |
| 1886   | Layout 1 | `ef329a9952ab`  |
| 1881   | Layout 1 | `ef329a9952ab`  |
| 1871   | Layout 1 | `ef329a9952ab`  |
| 1866   | Layout 1 | `ef329a9952ab`  |
| 1862   | Layout 1 | `ef329a9952ab`  |
| 1854   | Layout 1 | `ef329a9952ab`  |
| 1846   | Layout 1 | `ef329a9952ab`  |
| 1838   | Layout 1 | `ef329a9952ab`  |
| 1832   | Layout 1 | `ef329a9952ab`  |
| 1826   | Layout 1 | `ef329a9952ab`  |
| 1822   | Layout 1 | `ef329a9952ab`  |
| 1818   | Layout 1 | `ef329a9952ab`  |
| 1804   | Layout 1 | `ef329a9952ab`  |
| 1794   | Layout 1 | `ef329a9952ab`  |
| 1790   | Layout 1 | `ef329a9952ab`  |
| 1784   | Layout 1 | `ef329a9952ab`  |
| 1774   | Layout 1 | `ef329a9952ab`  |
| 1771   | Layout 1 | `ef329a9952ab`  |
| 1762   | Layout 1 | `ef329a9952ab`  |
| 1759   | Layout 1 | `ef329a9952ab`  |
| 1754   | Layout 1 | `ef329a9952ab`  |
| 1749   | Layout 1 | `ef329a9952ab`  |
| 1743   | Layout 1 | `ef329a9952ab`  |
| 1737   | Layout 1 | `ef329a9952ab`  |
| 1731   | Layout 1 | `ef329a9952ab`  |
| 1725   | Layout 1 | `ef329a9952ab`  |
| 1717   | Layout 1 | `ef329a9952ab`  |
| 1710   | Layout 1 | `ef329a9952ab`  |
| 1704   | Layout 1 | `ef329a9952ab`  |
| 1698   | Layout 1 | `ef329a9952ab`  |
| 1690   | Layout 1 | `ef329a9952ab`  |
| 1685   | Layout 1 | `ef329a9952ab`  |
| 1680   | Layout 1 | `ef329a9952ab`  |
| 1674   | Layout 1 | `ef329a9952ab`  |
| 1668   | Layout 1 | `ef329a9952ab`  |
| 1659   | Layout 1 | `ef329a9952ab`  |
| 1649   | Layout 1 | `ef329a9952ab`  |
| 1642   | Layout 1 | `ef329a9952ab`  |
| 1636   | Layout 1 | `ef329a9952ab`  |
| 1628   | Layout 1 | `ef329a9952ab`  |
| 1622   | Layout 1 | `ef329a9952ab`  |
| 1614   | Layout 1 | `ef329a9952ab`  |
| 1608   | Layout 1 | `ef329a9952ab`  |
| 1602   | Layout 1 | `ef329a9952ab`  |
| 1598   | Layout 1 | `ef329a9952ab`  |
| 1594   | Layout 1 | `ef329a9952ab`  |
| 1590   | Layout 1 | `ef329a9952ab`  |
| 1587   | Layout 1 | `ef329a9952ab`  |
| 1584   | Layout 1 | `ef329a9952ab`  |
| 1579   | Layout 1 | `ef329a9952ab`  |
| 1572   | Layout 1 | `ef329a9952ab`  |
| 1565   | Layout 1 | `ef329a9952ab`  |
| 1559   | Layout 1 | `ef329a9952ab`  |
| 1554   | Layout 1 | `ef329a9952ab`  |
| 1547   | Layout 1 | `ef329a9952ab`  |
| 1537   | Layout 1 | `ef329a9952ab`  |
| 1529   | Layout 1 | `ef329a9952ab`  |
| 1524   | Layout 1 | `ef329a9952ab`  |
| 1519   | Layout 1 | `ef329a9952ab`  |
| 1509   | Layout 1 | `ef329a9952ab`  |
| 1506   | Layout 1 | `ef329a9952ab`  |
| 1504   | Layout 1 | `ef329a9952ab`  |
| 1500   | Layout 1 | `ef329a9952ab`  |
| 1493   | Layout 1 | `ef329a9952ab`  |
| 1489   | Layout 1 | `ef329a9952ab`  |
| 1485   | Layout 1 | `ef329a9952ab`  |
| 1481   | Layout 1 | `ef329a9952ab`  |
| 1474   | Layout 1 | `ef329a9952ab`  |
| 1466   | Layout 1 | `ef329a9952ab`  |
| 1462   | Layout 1 | `ef329a9952ab`  |
| 1459   | Layout 1 | `ef329a9952ab`  |
| 1453   | Layout 1 | `ef329a9952ab`  |
| 1450   | Layout 1 | `ef329a9952ab`  |
| 1445   | Layout 1 | `ef329a9952ab`  |
| 1439   | Layout 1 | `ef329a9952ab`  |
| 1433   | Layout 1 | `ef329a9952ab`  |
| 1430   | Layout 1 | `ef329a9952ab`  |
| 1426   | Layout 1 | `ef329a9952ab`  |
| 1421   | Layout 1 | `ef329a9952ab`  |
| 1417   | Layout 1 | `ef329a9952ab`  |
| 1416   | Layout 1 | `ef329a9952ab`  |
| 1409   | Layout 1 | `ef329a9952ab`  |
| 1405   | Layout 1 | `ef329a9952ab`  |
| 1401   | Layout 1 | `ef329a9952ab`  |
| 1396   | Layout 1 | `ef329a9952ab`  |
| 1391   | Layout 1 | `ef329a9952ab`  |
| 1390   | Layout 1 | `ef329a9952ab`  |
| 1386   | Layout 1 | `ef329a9952ab`  |
| 1381   | Layout 1 | `ef329a9952ab`  |
| 1379   | Layout 1 | `ef329a9952ab`  |
| 1372   | Layout 1 | `ef329a9952ab`  |
| 1366   | Layout 1 | `ef329a9952ab`  |
| 1364   | Layout 1 | `ef329a9952ab`  |
| 1363   | Layout 1 | `ef329a9952ab`  |
| 1360   | Layout 1 | `ef329a9952ab`  |
| 1358   | Layout 1 | `ef329a9952ab`  |
| 1355   | Layout 1 | `ef329a9952ab`  |
| 1351   | Layout 1 | `ef329a9952ab`  |
| 1348   | Layout 1 | `ef329a9952ab`  |
| 1346   | No file  | `ef329a9952ab`  |
| 1341   | No file  | `ef329a9952ab`  |
| 1340   | No file  | `ef329a9952ab`  |
| 1338   | No file  | `ef329a9952ab`  |
| 1335   | No file  | `ef329a9952ab`  |
| 1333   | No file  | `ef329a9952ab`  |
| 1329   | No file  | `ef329a9952ab`  |
| 1327   | No file  | `ef329a9952ab`  |
| 1324   | No file  | `ef329a9952ab`  |
| 1321   | No file  | `ef329a9952ab`  |
| 1319   | No file  | `ef329a9952ab`  |
| 1318   | No file  | `ef329a9952ab`  |
| 1316   | No file  | `ef329a9952ab`  |
| 1313   | No file  | `ef329a9952ab`  |
| 1311   | No file  | `ef329a9952ab`  |
| 1309   | No file  | `ef329a9952ab`  |
| 1304   | No file  | `ef329a9952ab`  |
| 1292   | No file  | `ef329a9952ab`  |
| 1286   | No file  | `ef329a9952ab`  |
| 1280   | No file  | `ef329a9952ab`  |
| 1276   | No file  | `ef329a9952ab`  |
| 1267   | No file  | `ef329a9952ab`  |
| 1261   | No file  | `ef329a9952ab`  |
| 1256   | No file  | `ef329a9952ab`  |
| 1250   | No file  | `ef329a9952ab`  |
| 1246   | No file  | `ef329a9952ab`  |
| 1239   | No file  | `ef329a9952ab`  |
| 1230   | No file  | `ef329a9952ab`  |
| 1226   | No file  | `ef329a9952ab`  |
| 1220   | No file  | `ef329a9952ab`  |
| 1217   | No file  | `ef329a9952ab`  |
| 1211   | No file  | `ef329a9952ab`  |
| 1210   | No file  | `ef329a9952ab`  |
| 1208   | No file  | `ef329a9952ab`  |
| 1203   | No file  | `ef329a9952ab`  |
| 1197   | No file  | `ef329a9952ab`  |
| 1194   | No file  | `ef329a9952ab`  |
| 1192   | No file  | `ef329a9952ab`  |
| 1187   | No file  | `ef329a9952ab`  |
| 1183   | No file  | `ef329a9952ab`  |
| 1177   | No file  | `ef329a9952ab`  |
| 1173   | No file  | `ef329a9952ab`  |
| 1167   | No file  | `ef329a9952ab`  |
| 1164   | No file  | `ef329a9952ab`  |
| 1156   | No file  | `ef329a9952ab`  |
| 1149   | No file  | `ef329a9952ab`  |
| 1144   | No file  | `ef329a9952ab`  |
| 1137   | No file  | `ef329a9952ab`  |
| 1132   | No file  | `ef329a9952ab`  |
| 1127   | No file  | `ef329a9952ab`  |
| 1122   | No file  | `ef329a9952ab`  |
| 1118   | No file  | `ef329a9952ab`  |
| 1114   | No file  | `ef329a9952ab`  |
| 1109   | No file  | `ef329a9952ab`  |
| 1102   | No file  | `ef329a9952ab`  |
| 1096   | No file  | `ef329a9952ab`  |
| 1088   | No file  | `ef329a9952ab`  |
| 1081   | No file  | `ef329a9952ab`  |
| 1076   | No file  | `ef329a9952ab`  |
| 1069   | No file  | `ef329a9952ab`  |
| 1064   | No file  | `ef329a9952ab`  |
| 1058   | No file  | `ef329a9952ab`  |
| 1051   | No file  | `ef329a9952ab`  |
| 1044   | No file  | `ef329a9952ab`  |
| 1036   | No file  | `ef329a9952ab`  |
| 1026   | No file  | `ef329a9952ab`  |
| 1016   | No file  | `ef329a9952ab`  |
| 1009   | No file  | `ef329a9952ab`  |
| 1005   | No file  | `ef329a9952ab`  |
| 1000   | No file  | `ef329a9952ab`  |
| 998    | No file  | `ef329a9952ab`  |
| 990    | No file  | `ef329a9952ab`  |
| 979    | No file  | `ef329a9952ab`  |
| 972    | No file  | `ef329a9952ab`  |
| 963    | No file  | `ef329a9952ab`  |
| 955    | No file  | `ef329a9952ab`  |
| 946    | No file  | `ef329a9952ab`  |
| 938    | No file  | `ef329a9952ab`  |
| 927    | No file  | `ef329a9952ab`  |
| 911    | No file  | `ef329a9952ab`  |
| 904    | No file  | `ef329a9952ab`  |
| 899    | No file  | `ef329a9952ab`  |
| 894    | No file  | `ef329a9952ab`  |
| 885    | No file  | `ef329a9952ab`  |
| 879    | No file  | `ef329a9952ab`  |
| 872    | No file  | `ef329a9952ab`  |
| 864    | No file  | `ef329a9952ab`  |
| 855    | No file  | `ef329a9952ab`  |
| 853    | No file  | `ef329a9952ab`  |
| 845    | No file  | `ef329a9952ab`  |
| 837    | No file  | `ef329a9952ab`  |
| 829    | No file  | `ef329a9952ab`  |
| 822    | No file  | `ef329a9952ab`  |
| 814    | No file  | `ef329a9952ab`  |
| 805    | No file  | `ef329a9952ab`  |
| 794    | No file  | `ef329a9952ab`  |
| 787    | No file  | `ef329a9952ab`  |
| 780    | No file  | `ef329a9952ab`  |
| 771    | No file  | `ef329a9952ab`  |
| 760    | No file  | `ef329a9952ab`  |
| 748    | No file  | `ef329a9952ab`  |
| 741    | No file  | `ef329a9952ab`  |
| 736    | No file  | `ef329a9952ab`  |
| 731    | No file  | `ef329a9952ab`  |
| 723    | No file  | `ef329a9952ab`  |
| 711    | No file  | `ef329a9952ab`  |
| 707    | No file  | `ef329a9952ab`  |
| 697    | No file  | `ef329a9952ab`  |
| 689    | No file  | `ef329a9952ab`  |
| 683    | No file  | `ef329a9952ab`  |
| 678    | No file  | `ef329a9952ab`  |
| 670    | No file  | `ef329a9952ab`  |
| 661    | No file  | `ef329a9952ab`  |
| 656    | No file  | `ef329a9952ab`  |
| 652    | No file  | `ef329a9952ab`  |
| 643    | No file  | `ef329a9952ab`  |
| 637    | No file  | `ef329a9952ab`  |
| 630    | No file  | `ef329a9952ab`  |
| 627    | No file  | `ef329a9952ab`  |
| 621    | No file  | `ef329a9952ab`  |
| 617    | No file  | `ef329a9952ab`  |
| 615    | No file  | `ef329a9952ab`  |
| 606    | No file  | `ef329a9952ab`  |
| 599    | No file  | `ef329a9952ab`  |
| 592    | No file  | `ef329a9952ab`  |
| 586    | No file  | `ef329a9952ab`  |
| 577    | No file  | `ef329a9952ab`  |
| 569    | No file  | `ef329a9952ab`  |
| 561    | No file  | `ef329a9952ab`  |
| 554    | No file  | `ef329a9952ab`  |
| 542    | No file  | `ef329a9952ab`  |
| 532    | No file  | `ef329a9952ab`  |
| 531    | No file  | `ef329a9952ab`  |
| 526    | No file  | `ef329a9952ab`  |
| 521    | No file  | `ef329a9952ab`  |
| 517    | No file  | `ef329a9952ab`  |
| 510    | No file  | `ef329a9952ab`  |
| 508    | No file  | `ef329a9952ab`  |
| 504    | No file  | `ef329a9952ab`  |
| 497    | No file  | `ef329a9952ab`  |
| 491    | No file  | `ef329a9952ab`  |
| 485    | No file  | `ef329a9952ab`  |
| 478    | No file  | `ef329a9952ab`  |
| 472    | No file  | `ef329a9952ab`  |
| 466    | No file  | `ef329a9952ab`  |
| 457    | No file  | `ef329a9952ab`  |
| 452    | No file  | `ef329a9952ab`  |
| 449    | No file  | `ef329a9952ab`  |
| 435    | No file  | `ef329a9952ab`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type         | Field             | Notes                                                      |
| ------------------- | ------------ | ----------------- | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                               |
| `+0x04`             | f32          | playable_distance | `1500.0` on every client checked; see Field Names          |
| `+0x08`             | bytes[8]     | unknown_08        | `01 00 00 00 00 00 00 00` on clients 2519 to 3474          |
| `+0x10`             | String Table | string_table      | See String Table                                           |
| `string_table+0x00` | u32          | table_start       | Offset of the string table; `0x10`                         |
| `string_table+0x04` | u32          | zero              | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

No `unknown_08`: the string table follows the distance.

### File Layout

| Offset              | Type         | Field             | Notes                              |
| ------------------- | ------------ | ----------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                       |
| `+0x04`             | f32          | playable_distance | `1500.0`                           |
| `+0x08`             | String Table | string_table      | See String Table                   |
| `string_table+0x00` | u32          | table_start       | Offset of the string table; `0x08` |
| `string_table+0x04` | u32          | zero              | Always `0`                         |

## Field Names

The name follows the `MusicOption` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`DataSheet_MusicNoteTable.xlsm`. The sheet has one column,
`PlayableDistance`, and one row, `1500`. The server's loader reads it as a
float, and the client 1784 file is the Layout 1 file above with f32
`1500.0` (1 of 1 values). The value is the same on every client checked,
1784 to 3474.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 00 80 BB 44 01 00 00 00 00 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00`
  (28 bytes); on clients 1784 and 2107 the 20 bytes
  `50 41 42 52 00 80 BB 44 00 00 00 00 08 00 00 00 00 00 00 00`.
- The same workbook holds `MusicLevel` (`MusicLevel`, `MusicLevelEXPTable`,
  `IncreasingBarNumber`, `IncreasingNoteNumber`, `MusicRank`).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. It reads
  the newest layout and rejects the 20-byte Layout 1 file.

## Open Questions

### Bytes Added on Client 2519

`unknown_08` appeared between clients 2107 and 2519, after the sheet of
client 1784 was built, so no sheet names it. The first byte is `1`, the
other seven `0`: one flag and padding, a u32 and a `0` u32, or a u64 all fit.
The client Lua's music functions (`ToClient_GetMusicInfoByIndex`,
`ToClient_IsPlayMusicAble`, `ToClient_PlayPartyMusicReq` and others on
client 3474) return no option value that would show which.
