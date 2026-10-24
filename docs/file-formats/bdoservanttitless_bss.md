# `bdoservanttitless.bss` Format

## Purpose

Breed titles of the horses: one row per servant character with the index of
its title in the file's string table, Korean dev text `품종 1번` ("breed 1")
to `품종 24번`, and a contents group that gates the row. On client 3474 the
file has 254 rows and 24 titles.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 2      | 2468 and later | 3483    | `bdoservanttitless.bss` | 2,950 | 254 Row | 10        |
| 1      | 1762 to 2460   | 2460    | `bdoservanttitless.bss` | 2,334 | 166 Row | 12        |

| Layout | File                    | Known            | Unknown    |
| ------ | ----------------------- | ---------------- | ---------- |
| 2      | `bdoservanttitless.bss` | 2,950 B (100.0%) | 0 B (0.0%) |
| 1      | `bdoservanttitless.bss` | 2,334 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `ec0944a505b7`  |
| 3482   | Layout 2 | `ec0944a505b7`  |
| 3474   | Layout 2 | `ec0944a505b7`  |
| 3473   | Layout 2 | `ec0944a505b7`  |
| 3464   | Layout 2 | `ec0944a505b7`  |
| 3458   | Layout 2 | `ec0944a505b7`  |
| 3454   | Layout 2 | `ec0944a505b7`  |
| 3444   | Layout 2 | `ec0944a505b7`  |
| 3435   | Layout 2 | `ec0944a505b7`  |
| 3426   | Layout 2 | `ec0944a505b7`  |
| 3418   | Layout 2 | `ec0944a505b7`  |
| 3412   | Layout 2 | `ec0944a505b7`  |
| 3402   | Layout 2 | `ec0944a505b7`  |
| 3396   | Layout 2 | `ec0944a505b7`  |
| 3387   | Layout 2 | `ec0944a505b7`  |
| 3381   | Layout 2 | `ec0944a505b7`  |
| 3373   | Layout 2 | `ec0944a505b7`  |
| 3364   | Layout 2 | `ec0944a505b7`  |
| 3356   | Layout 2 | `ec0944a505b7`  |
| 3349   | Layout 2 | `ec0944a505b7`  |
| 3342   | Layout 2 | `ec0944a505b7`  |
| 3335   | Layout 2 | `ec0944a505b7`  |
| 3326   | Layout 2 | `ec0944a505b7`  |
| 3321   | Layout 2 | `ec0944a505b7`  |
| 3314   | Layout 2 | `ec0944a505b7`  |
| 3303   | Layout 2 | `ec0944a505b7`  |
| 3302   | Layout 2 | `ec0944a505b7`  |
| 3293   | Layout 2 | `ec0944a505b7`  |
| 3283   | Layout 2 | `ec0944a505b7`  |
| 3275   | Layout 2 | `ec0944a505b7`  |
| 3267   | Layout 2 | `ec0944a505b7`  |
| 3258   | Layout 2 | `ec0944a505b7`  |
| 3251   | Layout 2 | `ec0944a505b7`  |
| 3242   | Layout 2 | `ec0944a505b7`  |
| 3235   | Layout 2 | `ec0944a505b7`  |
| 3229   | Layout 2 | `ec0944a505b7`  |
| 3212   | Layout 2 | `ec0944a505b7`  |
| 3203   | Layout 2 | `ec0944a505b7`  |
| 3193   | Layout 2 | `ec0944a505b7`  |
| 3186   | Layout 2 | `ec0944a505b7`  |
| 3177   | Layout 2 | `ec0944a505b7`  |
| 3169   | Layout 2 | `ec0944a505b7`  |
| 3158   | Layout 2 | `ec0944a505b7`  |
| 3151   | Layout 2 | `ec0944a505b7`  |
| 3144   | Layout 2 | `ec0944a505b7`  |
| 3133   | Layout 2 | `ec0944a505b7`  |
| 3125   | Layout 2 | `ec0944a505b7`  |
| 3118   | Layout 2 | `ec0944a505b7`  |
| 3111   | Layout 2 | `ec0944a505b7`  |
| 3103   | Layout 2 | `ec0944a505b7`  |
| 3095   | Layout 2 | `ec0944a505b7`  |
| 3086   | Layout 2 | `ec0944a505b7`  |
| 3072   | Layout 2 | `ec0944a505b7`  |
| 3062   | Layout 2 | `ec0944a505b7`  |
| 3052   | Layout 2 | `ec0944a505b7`  |
| 3045   | Layout 2 | `ec0944a505b7`  |
| 3037   | Layout 2 | `ec0944a505b7`  |
| 3030   | Layout 2 | `ec0944a505b7`  |
| 3021   | Layout 2 | `ec0944a505b7`  |
| 3012   | Layout 2 | `ec0944a505b7`  |
| 3002   | Layout 2 | `ec0944a505b7`  |
| 2995   | Layout 2 | `ec0944a505b7`  |
| 2987   | Layout 2 | `ec0944a505b7`  |
| 2978   | Layout 2 | `ec0944a505b7`  |
| 2970   | Layout 2 | `ec0944a505b7`  |
| 2959   | Layout 2 | `ec0944a505b7`  |
| 2951   | Layout 2 | `ec0944a505b7`  |
| 2942   | Layout 2 | `ec0944a505b7`  |
| 2935   | Layout 2 | `ec0944a505b7`  |
| 2932   | Layout 2 | `ec0944a505b7`  |
| 2923   | Layout 2 | `ec0944a505b7`  |
| 2919   | Layout 2 | `ec0944a505b7`  |
| 2907   | Layout 2 | `ec0944a505b7`  |
| 2900   | Layout 2 | `ec0944a505b7`  |
| 2891   | Layout 2 | `ec0944a505b7`  |
| 2882   | Layout 2 | `ec0944a505b7`  |
| 2872   | Layout 2 | `ec0944a505b7`  |
| 2863   | Layout 2 | `ec0944a505b7`  |
| 2855   | Layout 2 | `ec0944a505b7`  |
| 2849   | Layout 2 | `ec0944a505b7`  |
| 2844   | Layout 2 | `ec0944a505b7`  |
| 2834   | Layout 2 | `ec0944a505b7`  |
| 2825   | Layout 2 | `ec0944a505b7`  |
| 2819   | Layout 2 | `ec0944a505b7`  |
| 2811   | Layout 2 | `ec0944a505b7`  |
| 2803   | Layout 2 | `ec0944a505b7`  |
| 2794   | Layout 2 | `ec0944a505b7`  |
| 2783   | Layout 2 | `ec0944a505b7`  |
| 2774   | Layout 2 | `ec0944a505b7`  |
| 2765   | Layout 2 | `ec0944a505b7`  |
| 2756   | Layout 2 | `ec0944a505b7`  |
| 2750   | Layout 2 | `ec0944a505b7`  |
| 2743   | Layout 2 | `ec0944a505b7`  |
| 2736   | Layout 2 | `ec0944a505b7`  |
| 2726   | Layout 2 | `ec0944a505b7`  |
| 2717   | Layout 2 | `ec0944a505b7`  |
| 2709   | Layout 2 | `ec0944a505b7`  |
| 2703   | Layout 2 | `ec0944a505b7`  |
| 2695   | Layout 2 | `ec0944a505b7`  |
| 2684   | Layout 2 | `ec0944a505b7`  |
| 2672   | Layout 2 | `ec0944a505b7`  |
| 2665   | Layout 2 | `ec0944a505b7`  |
| 2657   | Layout 2 | `ec0944a505b7`  |
| 2649   | Layout 2 | `ec0944a505b7`  |
| 2644   | Layout 2 | `ec0944a505b7`  |
| 2637   | Layout 2 | `ec0944a505b7`  |
| 2629   | Layout 2 | `ec0944a505b7`  |
| 2619   | Layout 2 | `ec0944a505b7`  |
| 2612   | Layout 2 | `ec0944a505b7`  |
| 2606   | Layout 2 | `ec0944a505b7`  |
| 2602   | Layout 2 | `ec0944a505b7`  |
| 2601   | Layout 2 | `ec0944a505b7`  |
| 2592   | Layout 2 | `ec0944a505b7`  |
| 2583   | Layout 2 | `ec0944a505b7`  |
| 2575   | Layout 2 | `ec0944a505b7`  |
| 2567   | Layout 2 | `ec0944a505b7`  |
| 2560   | Layout 2 | `ec0944a505b7`  |
| 2553   | Layout 2 | `ec0944a505b7`  |
| 2545   | Layout 2 | `ec0944a505b7`  |
| 2538   | Layout 2 | `ec0944a505b7`  |
| 2529   | Layout 2 | `ec0944a505b7`  |
| 2519   | Layout 2 | `ec0944a505b7`  |
| 2513   | Layout 2 | `ec0944a505b7`  |
| 2510   | Layout 2 | `ec0944a505b7`  |
| 2507   | Layout 2 | `ec0944a505b7`  |
| 2503   | Layout 2 | `ec0944a505b7`  |
| 2498   | Layout 2 | `ec0944a505b7`  |
| 2492   | Layout 2 | `ec0944a505b7`  |
| 2487   | Layout 2 | `ec0944a505b7`  |
| 2480   | Layout 2 | `ec0944a505b7`  |
| 2474   | Layout 2 | `ec0944a505b7`  |
| 2468   | Layout 2 | `ec0944a505b7`  |
| 2460   | Layout 1 | `ec0944a505b7`  |
| 2453   | Layout 1 | `ec0944a505b7`  |
| 2444   | Layout 1 | `ec0944a505b7`  |
| 2438   | Layout 1 | `ec0944a505b7`  |
| 2434   | Layout 1 | `ec0944a505b7`  |
| 2429   | Layout 1 | `ec0944a505b7`  |
| 2421   | Layout 1 | `ec0944a505b7`  |
| 2414   | Layout 1 | `ec0944a505b7`  |
| 2407   | Layout 1 | `ec0944a505b7`  |
| 2401   | Layout 1 | `ec0944a505b7`  |
| 2397   | Layout 1 | `ec0944a505b7`  |
| 2393   | Layout 1 | `ec0944a505b7`  |
| 2384   | Layout 1 | `ec0944a505b7`  |
| 2378   | Layout 1 | `ec0944a505b7`  |
| 2372   | Layout 1 | `ec0944a505b7`  |
| 2358   | Layout 1 | `ec0944a505b7`  |
| 2352   | Layout 1 | `ec0944a505b7`  |
| 2347   | Layout 1 | `ec0944a505b7`  |
| 2343   | Layout 1 | `ec0944a505b7`  |
| 2335   | Layout 1 | `ec0944a505b7`  |
| 2327   | Layout 1 | `ec0944a505b7`  |
| 2324   | Layout 1 | `ec0944a505b7`  |
| 2319   | Layout 1 | `ec0944a505b7`  |
| 2313   | Layout 1 | `ec0944a505b7`  |
| 2308   | Layout 1 | `ec0944a505b7`  |
| 2302   | Layout 1 | `ec0944a505b7`  |
| 2295   | Layout 1 | `ec0944a505b7`  |
| 2290   | Layout 1 | `ec0944a505b7`  |
| 2284   | Layout 1 | `ec0944a505b7`  |
| 2276   | Layout 1 | `ec0944a505b7`  |
| 2269   | Layout 1 | `ec0944a505b7`  |
| 2259   | Layout 1 | `ec0944a505b7`  |
| 2250   | Layout 1 | `ec0944a505b7`  |
| 2243   | Layout 1 | `ec0944a505b7`  |
| 2235   | Layout 1 | `ec0944a505b7`  |
| 2229   | Layout 1 | `ec0944a505b7`  |
| 2224   | Layout 1 | `ec0944a505b7`  |
| 2218   | Layout 1 | `ec0944a505b7`  |
| 2215   | Layout 1 | `ec0944a505b7`  |
| 2207   | Layout 1 | `ec0944a505b7`  |
| 2203   | Layout 1 | `ec0944a505b7`  |
| 2196   | Layout 1 | `ec0944a505b7`  |
| 2192   | Layout 1 | `ec0944a505b7`  |
| 2189   | Layout 1 | `ec0944a505b7`  |
| 2183   | Layout 1 | `ec0944a505b7`  |
| 2179   | Layout 1 | `ec0944a505b7`  |
| 2171   | Layout 1 | `ec0944a505b7`  |
| 2163   | Layout 1 | `ec0944a505b7`  |
| 2156   | Layout 1 | `ec0944a505b7`  |
| 2151   | Layout 1 | `ec0944a505b7`  |
| 2147   | Layout 1 | `ec0944a505b7`  |
| 2142   | Layout 1 | `ec0944a505b7`  |
| 2138   | Layout 1 | `ec0944a505b7`  |
| 2134   | Layout 1 | `ec0944a505b7`  |
| 2130   | Layout 1 | `ec0944a505b7`  |
| 2122   | Layout 1 | `ec0944a505b7`  |
| 2107   | Layout 1 | `ec0944a505b7`  |
| 2098   | Layout 1 | `ec0944a505b7`  |
| 2089   | Layout 1 | `ec0944a505b7`  |
| 2081   | Layout 1 | `ec0944a505b7`  |
| 2073   | Layout 1 | `ec0944a505b7`  |
| 2067   | Layout 1 | `ec0944a505b7`  |
| 2063   | Layout 1 | `ec0944a505b7`  |
| 2059   | Layout 1 | `ec0944a505b7`  |
| 2052   | Layout 1 | `ec0944a505b7`  |
| 2044   | Layout 1 | `ec0944a505b7`  |
| 2039   | Layout 1 | `ec0944a505b7`  |
| 2032   | Layout 1 | `ec0944a505b7`  |
| 2025   | Layout 1 | `ec0944a505b7`  |
| 2011   | Layout 1 | `ec0944a505b7`  |
| 2005   | Layout 1 | `ec0944a505b7`  |
| 2000   | Layout 1 | `ec0944a505b7`  |
| 1996   | Layout 1 | `ec0944a505b7`  |
| 1991   | Layout 1 | `ec0944a505b7`  |
| 1985   | Layout 1 | `ec0944a505b7`  |
| 1980   | Layout 1 | `ec0944a505b7`  |
| 1969   | Layout 1 | `ec0944a505b7`  |
| 1964   | Layout 1 | `ec0944a505b7`  |
| 1958   | Layout 1 | `ec0944a505b7`  |
| 1950   | Layout 1 | `ec0944a505b7`  |
| 1945   | Layout 1 | `ec0944a505b7`  |
| 1937   | Layout 1 | `ec0944a505b7`  |
| 1933   | Layout 1 | `ec0944a505b7`  |
| 1927   | Layout 1 | `ec0944a505b7`  |
| 1921   | Layout 1 | `ec0944a505b7`  |
| 1914   | Layout 1 | `ec0944a505b7`  |
| 1908   | Layout 1 | `ec0944a505b7`  |
| 1897   | Layout 1 | `ec0944a505b7`  |
| 1892   | Layout 1 | `ec0944a505b7`  |
| 1886   | Layout 1 | `ec0944a505b7`  |
| 1881   | Layout 1 | `ec0944a505b7`  |
| 1871   | Layout 1 | `ec0944a505b7`  |
| 1866   | Layout 1 | `ec0944a505b7`  |
| 1862   | Layout 1 | `ec0944a505b7`  |
| 1854   | Layout 1 | `ec0944a505b7`  |
| 1846   | Layout 1 | `ec0944a505b7`  |
| 1838   | Layout 1 | `ec0944a505b7`  |
| 1832   | Layout 1 | `ec0944a505b7`  |
| 1826   | Layout 1 | `ec0944a505b7`  |
| 1822   | Layout 1 | `ec0944a505b7`  |
| 1818   | Layout 1 | `ec0944a505b7`  |
| 1804   | Layout 1 | `ec0944a505b7`  |
| 1794   | Layout 1 | `ec0944a505b7`  |
| 1790   | Layout 1 | `ec0944a505b7`  |
| 1784   | Layout 1 | `ec0944a505b7`  |
| 1774   | Layout 1 | `ec0944a505b7`  |
| 1771   | Layout 1 | `ec0944a505b7`  |
| 1762   | Layout 1 | `ec0944a505b7`  |
| 1759   | No file  | `ec0944a505b7`  |
| 1754   | No file  | `ec0944a505b7`  |
| 1749   | No file  | `ec0944a505b7`  |
| 1743   | No file  | `ec0944a505b7`  |
| 1737   | No file  | `ec0944a505b7`  |
| 1731   | No file  | `ec0944a505b7`  |
| 1725   | No file  | `ec0944a505b7`  |
| 1717   | No file  | `ec0944a505b7`  |
| 1710   | No file  | `ec0944a505b7`  |
| 1704   | No file  | `ec0944a505b7`  |
| 1698   | No file  | `ec0944a505b7`  |
| 1690   | No file  | `ec0944a505b7`  |
| 1685   | No file  | `ec0944a505b7`  |
| 1680   | No file  | `ec0944a505b7`  |
| 1674   | No file  | `ec0944a505b7`  |
| 1668   | No file  | `ec0944a505b7`  |
| 1659   | No file  | `ec0944a505b7`  |
| 1649   | No file  | `ec0944a505b7`  |
| 1642   | No file  | `ec0944a505b7`  |
| 1636   | No file  | `ec0944a505b7`  |
| 1628   | No file  | `ec0944a505b7`  |
| 1622   | No file  | `ec0944a505b7`  |
| 1614   | No file  | `ec0944a505b7`  |
| 1608   | No file  | `ec0944a505b7`  |
| 1602   | No file  | `ec0944a505b7`  |
| 1598   | No file  | `ec0944a505b7`  |
| 1594   | No file  | `ec0944a505b7`  |
| 1590   | No file  | `ec0944a505b7`  |
| 1587   | No file  | `ec0944a505b7`  |
| 1584   | No file  | `ec0944a505b7`  |
| 1579   | No file  | `ec0944a505b7`  |
| 1572   | No file  | `ec0944a505b7`  |
| 1565   | No file  | `ec0944a505b7`  |
| 1559   | No file  | `ec0944a505b7`  |
| 1554   | No file  | `ec0944a505b7`  |
| 1547   | No file  | `ec0944a505b7`  |
| 1537   | No file  | `ec0944a505b7`  |
| 1529   | No file  | `ec0944a505b7`  |
| 1524   | No file  | `ec0944a505b7`  |
| 1519   | No file  | `ec0944a505b7`  |
| 1509   | No file  | `ec0944a505b7`  |
| 1506   | No file  | `ec0944a505b7`  |
| 1504   | No file  | `ec0944a505b7`  |
| 1500   | No file  | `ec0944a505b7`  |
| 1493   | No file  | `ec0944a505b7`  |
| 1489   | No file  | `ec0944a505b7`  |
| 1485   | No file  | `ec0944a505b7`  |
| 1481   | No file  | `ec0944a505b7`  |
| 1474   | No file  | `ec0944a505b7`  |
| 1466   | No file  | `ec0944a505b7`  |
| 1462   | No file  | `ec0944a505b7`  |
| 1459   | No file  | `ec0944a505b7`  |
| 1453   | No file  | `ec0944a505b7`  |
| 1450   | No file  | `ec0944a505b7`  |
| 1445   | No file  | `ec0944a505b7`  |
| 1439   | No file  | `ec0944a505b7`  |
| 1433   | No file  | `ec0944a505b7`  |
| 1430   | No file  | `ec0944a505b7`  |
| 1426   | No file  | `ec0944a505b7`  |
| 1421   | No file  | `ec0944a505b7`  |
| 1417   | No file  | `ec0944a505b7`  |
| 1416   | No file  | `ec0944a505b7`  |
| 1409   | No file  | `ec0944a505b7`  |
| 1405   | No file  | `ec0944a505b7`  |
| 1401   | No file  | `ec0944a505b7`  |
| 1396   | No file  | `ec0944a505b7`  |
| 1391   | No file  | `ec0944a505b7`  |
| 1390   | No file  | `ec0944a505b7`  |
| 1386   | No file  | `ec0944a505b7`  |
| 1381   | No file  | `ec0944a505b7`  |
| 1379   | No file  | `ec0944a505b7`  |
| 1372   | No file  | `ec0944a505b7`  |
| 1366   | No file  | `ec0944a505b7`  |
| 1364   | No file  | `ec0944a505b7`  |
| 1363   | No file  | `ec0944a505b7`  |
| 1360   | No file  | `ec0944a505b7`  |
| 1358   | No file  | `ec0944a505b7`  |
| 1355   | No file  | `ec0944a505b7`  |
| 1351   | No file  | `ec0944a505b7`  |
| 1348   | No file  | `ec0944a505b7`  |
| 1346   | No file  | `ec0944a505b7`  |
| 1341   | No file  | `ec0944a505b7`  |
| 1340   | No file  | `ec0944a505b7`  |
| 1338   | No file  | `ec0944a505b7`  |
| 1335   | No file  | `ec0944a505b7`  |
| 1333   | No file  | `ec0944a505b7`  |
| 1329   | No file  | `ec0944a505b7`  |
| 1327   | No file  | `ec0944a505b7`  |
| 1324   | No file  | `ec0944a505b7`  |
| 1321   | No file  | `ec0944a505b7`  |
| 1319   | No file  | `ec0944a505b7`  |
| 1318   | No file  | `ec0944a505b7`  |
| 1316   | No file  | `ec0944a505b7`  |
| 1313   | No file  | `ec0944a505b7`  |
| 1311   | No file  | `ec0944a505b7`  |
| 1309   | No file  | `ec0944a505b7`  |
| 1304   | No file  | `ec0944a505b7`  |
| 1292   | No file  | `ec0944a505b7`  |
| 1286   | No file  | `ec0944a505b7`  |
| 1280   | No file  | `ec0944a505b7`  |
| 1276   | No file  | `ec0944a505b7`  |
| 1267   | No file  | `ec0944a505b7`  |
| 1261   | No file  | `ec0944a505b7`  |
| 1256   | No file  | `ec0944a505b7`  |
| 1250   | No file  | `ec0944a505b7`  |
| 1246   | No file  | `ec0944a505b7`  |
| 1239   | No file  | `ec0944a505b7`  |
| 1230   | No file  | `ec0944a505b7`  |
| 1226   | No file  | `ec0944a505b7`  |
| 1220   | No file  | `ec0944a505b7`  |
| 1217   | No file  | `ec0944a505b7`  |
| 1211   | No file  | `ec0944a505b7`  |
| 1210   | No file  | `ec0944a505b7`  |
| 1208   | No file  | `ec0944a505b7`  |
| 1203   | No file  | `ec0944a505b7`  |
| 1197   | No file  | `ec0944a505b7`  |
| 1194   | No file  | `ec0944a505b7`  |
| 1192   | No file  | `ec0944a505b7`  |
| 1187   | No file  | `ec0944a505b7`  |
| 1183   | No file  | `ec0944a505b7`  |
| 1177   | No file  | `ec0944a505b7`  |
| 1173   | No file  | `ec0944a505b7`  |
| 1167   | No file  | `ec0944a505b7`  |
| 1164   | No file  | `ec0944a505b7`  |
| 1156   | No file  | `ec0944a505b7`  |
| 1149   | No file  | `ec0944a505b7`  |
| 1144   | No file  | `ec0944a505b7`  |
| 1137   | No file  | `ec0944a505b7`  |
| 1132   | No file  | `ec0944a505b7`  |
| 1127   | No file  | `ec0944a505b7`  |
| 1122   | No file  | `ec0944a505b7`  |
| 1118   | No file  | `ec0944a505b7`  |
| 1114   | No file  | `ec0944a505b7`  |
| 1109   | No file  | `ec0944a505b7`  |
| 1102   | No file  | `ec0944a505b7`  |
| 1096   | No file  | `ec0944a505b7`  |
| 1088   | No file  | `ec0944a505b7`  |
| 1081   | No file  | `ec0944a505b7`  |
| 1076   | No file  | `ec0944a505b7`  |
| 1069   | No file  | `ec0944a505b7`  |
| 1064   | No file  | `ec0944a505b7`  |
| 1058   | No file  | `ec0944a505b7`  |
| 1051   | No file  | `ec0944a505b7`  |
| 1044   | No file  | `ec0944a505b7`  |
| 1036   | No file  | `ec0944a505b7`  |
| 1026   | No file  | `ec0944a505b7`  |
| 1016   | No file  | `ec0944a505b7`  |
| 1009   | No file  | `ec0944a505b7`  |
| 1005   | No file  | `ec0944a505b7`  |
| 1000   | No file  | `ec0944a505b7`  |
| 998    | No file  | `ec0944a505b7`  |
| 990    | No file  | `ec0944a505b7`  |
| 979    | No file  | `ec0944a505b7`  |
| 972    | No file  | `ec0944a505b7`  |
| 963    | No file  | `ec0944a505b7`  |
| 955    | No file  | `ec0944a505b7`  |
| 946    | No file  | `ec0944a505b7`  |
| 938    | No file  | `ec0944a505b7`  |
| 927    | No file  | `ec0944a505b7`  |
| 911    | No file  | `ec0944a505b7`  |
| 904    | No file  | `ec0944a505b7`  |
| 899    | No file  | `ec0944a505b7`  |
| 894    | No file  | `ec0944a505b7`  |
| 885    | No file  | `ec0944a505b7`  |
| 879    | No file  | `ec0944a505b7`  |
| 872    | No file  | `ec0944a505b7`  |
| 864    | No file  | `ec0944a505b7`  |
| 855    | No file  | `ec0944a505b7`  |
| 853    | No file  | `ec0944a505b7`  |
| 845    | No file  | `ec0944a505b7`  |
| 837    | No file  | `ec0944a505b7`  |
| 829    | No file  | `ec0944a505b7`  |
| 822    | No file  | `ec0944a505b7`  |
| 814    | No file  | `ec0944a505b7`  |
| 805    | No file  | `ec0944a505b7`  |
| 794    | No file  | `ec0944a505b7`  |
| 787    | No file  | `ec0944a505b7`  |
| 780    | No file  | `ec0944a505b7`  |
| 771    | No file  | `ec0944a505b7`  |
| 760    | No file  | `ec0944a505b7`  |
| 748    | No file  | `ec0944a505b7`  |
| 741    | No file  | `ec0944a505b7`  |
| 736    | No file  | `ec0944a505b7`  |
| 731    | No file  | `ec0944a505b7`  |
| 723    | No file  | `ec0944a505b7`  |
| 711    | No file  | `ec0944a505b7`  |
| 707    | No file  | `ec0944a505b7`  |
| 697    | No file  | `ec0944a505b7`  |
| 689    | No file  | `ec0944a505b7`  |
| 683    | No file  | `ec0944a505b7`  |
| 678    | No file  | `ec0944a505b7`  |
| 670    | No file  | `ec0944a505b7`  |
| 661    | No file  | `ec0944a505b7`  |
| 656    | No file  | `ec0944a505b7`  |
| 652    | No file  | `ec0944a505b7`  |
| 643    | No file  | `ec0944a505b7`  |
| 637    | No file  | `ec0944a505b7`  |
| 630    | No file  | `ec0944a505b7`  |
| 627    | No file  | `ec0944a505b7`  |
| 621    | No file  | `ec0944a505b7`  |
| 617    | No file  | `ec0944a505b7`  |
| 615    | No file  | `ec0944a505b7`  |
| 606    | No file  | `ec0944a505b7`  |
| 599    | No file  | `ec0944a505b7`  |
| 592    | No file  | `ec0944a505b7`  |
| 586    | No file  | `ec0944a505b7`  |
| 577    | No file  | `ec0944a505b7`  |
| 569    | No file  | `ec0944a505b7`  |
| 561    | No file  | `ec0944a505b7`  |
| 554    | No file  | `ec0944a505b7`  |
| 542    | No file  | `ec0944a505b7`  |
| 532    | No file  | `ec0944a505b7`  |
| 531    | No file  | `ec0944a505b7`  |
| 526    | No file  | `ec0944a505b7`  |
| 521    | No file  | `ec0944a505b7`  |
| 517    | No file  | `ec0944a505b7`  |
| 510    | No file  | `ec0944a505b7`  |
| 508    | No file  | `ec0944a505b7`  |
| 504    | No file  | `ec0944a505b7`  |
| 497    | No file  | `ec0944a505b7`  |
| 491    | No file  | `ec0944a505b7`  |
| 485    | No file  | `ec0944a505b7`  |
| 478    | No file  | `ec0944a505b7`  |
| 472    | No file  | `ec0944a505b7`  |
| 466    | No file  | `ec0944a505b7`  |
| 457    | No file  | `ec0944a505b7`  |
| 452    | No file  | `ec0944a505b7`  |
| 449    | No file  | `ec0944a505b7`  |
| 435    | No file  | `ec0944a505b7`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | Servant names (LOC type 6) and the shown breed title (LOC type 111, `str_id1` = `character_id`) |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                         |
| ------------------- | ----------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                                        |
| `+0x04`             | u32               | record_count       | 254 on client 3474                            |
| `+0x08`             | Row[record_count] | records            | See Row                                       |
| `records+0x00`      | String Table      | string_table       | The titles                                    |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`             |
| `string_table+0x04` | u32               | zero               | `0`                                           |

### Row (10 bytes)

| Offset  | Type | Field           | Notes |
| ------- | ---- | --------------- | ----- |
| `+0x00` | u16  | character_id    | Servant character, as in `servant.bss`; unique |
| `+0x02` | u32  | title_name      | Index into `strings` |
| `+0x06` | u32  | contents_option | `0`, or a contents group key: 258, 590, 751, 828, 2168 on 6 rows (client 3474) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | 24 on client 3474 |
| `+0x04` | pstr[string_count] | strings      | `품종 1번` to `품종 24번`, wide (`is_wide` 1) |

## Layout 1

Client 1784 repeats `character_id` and has 166 rows and 20 titles; its
`contents_option` is `0` on every row.

### Row (12 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u16  | character_id     | |
| `+0x02` | u16  | character_id_dup | Equals `character_id` on every row |
| `+0x04` | u32  | title_name       | |
| `+0x08` | u32  | contents_option  | |

## Field Names

The names follow the `ServantTitleName_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (`CharacterKey`, `TitleName`,
`ContentsOption`), matched value by value:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `CharacterKey` | `character_id` | 166 of 166 | 166 of 254 |
| `TitleName` | the string `title_name` points at | 166 | 165 |
| `ContentsOption` | `contents_option` | 166 | 166 |

The sheet's `ContentsOption` is empty on every row, so the column match
rests on the zeros. The 6 non-zero client 3474 values are all keys of
[contentsgroupoptionstaticstatusmanager.bss](contentsgroupoptionstaticstatusmanager_bss.md),
open on that client, and sit on servants newer than the sheet: Krogdalo
(31595), Voltarion (31611, 31612) and Mythical Arduanatt, Diné and Doom
(31619 to 31621).

## Notes

- Rows are in neither key nor title order. The string table holds each title
  once; client 1784 lists them in first-use order (`품종 1번`, `품종 10번`,
  `품종 4번`, ...), client 3474 in number order.
- The title shows in the horse windows as Base Coat (LOC type 37 `Base
  Coat`), for example "Base Coat: Breed 11" on a tier 6 stallion that the
  `vehicleskillowner.dbss` learn chances identify as 9953 (`품종 11번`), and
  "Breed 2" on 9915 (`품종 2번`), and "Breed 13" on a Mythical horse, which
  only 31619 (`품종 13번`, tier 9) can be; checked in game on client 3474. The
  displayed text is "Breed N", not the Korean string: LOC type 111 holds it
  per character (`str_id1` = `character_id`, `str_id4` 0), "Breed 11" for
  9953. On client 3474 all 254 rows have that text, and its number is the
  one in the row's `품종 N번`.
