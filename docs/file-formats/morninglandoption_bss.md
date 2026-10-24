# `morninglandoption.bss` Format

## Purpose

Three option values for the Land of the Morning Light, with no PABR magic
and no string table: two u64 numbers and one byte. On client 3474 they are
`500000`, `2000000` and `5`. The two u64 values are the silver costs of the
two resets in the Black Shrine aura window, and the byte is the number of
Black Shrine clears a family gets per week (see Field Names).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 1      | 2224 and later | 3483    | `morninglandoption.bss` | 17    | -       | -         |

| Layout | File                    | Known         | Unknown    |
| ------ | ----------------------- | ------------- | ---------- |
| 1      | `morninglandoption.bss` | 17 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `9e6c034ca530`  |
| 3482   | Layout 1 | `9e6c034ca530`  |
| 3474   | Layout 1 | `9e6c034ca530`  |
| 3473   | Layout 1 | `9e6c034ca530`  |
| 3464   | Layout 1 | `9e6c034ca530`  |
| 3458   | Layout 1 | `9e6c034ca530`  |
| 3454   | Layout 1 | `9e6c034ca530`  |
| 3444   | Layout 1 | `9e6c034ca530`  |
| 3435   | Layout 1 | `9e6c034ca530`  |
| 3426   | Layout 1 | `9e6c034ca530`  |
| 3418   | Layout 1 | `9e6c034ca530`  |
| 3412   | Layout 1 | `9e6c034ca530`  |
| 3402   | Layout 1 | `9e6c034ca530`  |
| 3396   | Layout 1 | `9e6c034ca530`  |
| 3387   | Layout 1 | `9e6c034ca530`  |
| 3381   | Layout 1 | `9e6c034ca530`  |
| 3373   | Layout 1 | `9e6c034ca530`  |
| 3364   | Layout 1 | `9e6c034ca530`  |
| 3356   | Layout 1 | `9e6c034ca530`  |
| 3349   | Layout 1 | `9e6c034ca530`  |
| 3342   | Layout 1 | `9e6c034ca530`  |
| 3335   | Layout 1 | `9e6c034ca530`  |
| 3326   | Layout 1 | `9e6c034ca530`  |
| 3321   | Layout 1 | `9e6c034ca530`  |
| 3314   | Layout 1 | `9e6c034ca530`  |
| 3303   | Layout 1 | `9e6c034ca530`  |
| 3302   | Layout 1 | `9e6c034ca530`  |
| 3293   | Layout 1 | `9e6c034ca530`  |
| 3283   | Layout 1 | `9e6c034ca530`  |
| 3275   | Layout 1 | `9e6c034ca530`  |
| 3267   | Layout 1 | `9e6c034ca530`  |
| 3258   | Layout 1 | `9e6c034ca530`  |
| 3251   | Layout 1 | `9e6c034ca530`  |
| 3242   | Layout 1 | `9e6c034ca530`  |
| 3235   | Layout 1 | `9e6c034ca530`  |
| 3229   | Layout 1 | `9e6c034ca530`  |
| 3212   | Layout 1 | `9e6c034ca530`  |
| 3203   | Layout 1 | `9e6c034ca530`  |
| 3193   | Layout 1 | `9e6c034ca530`  |
| 3186   | Layout 1 | `9e6c034ca530`  |
| 3177   | Layout 1 | `9e6c034ca530`  |
| 3169   | Layout 1 | `9e6c034ca530`  |
| 3158   | Layout 1 | `9e6c034ca530`  |
| 3151   | Layout 1 | `9e6c034ca530`  |
| 3144   | Layout 1 | `9e6c034ca530`  |
| 3133   | Layout 1 | `9e6c034ca530`  |
| 3125   | Layout 1 | `9e6c034ca530`  |
| 3118   | Layout 1 | `9e6c034ca530`  |
| 3111   | Layout 1 | `9e6c034ca530`  |
| 3103   | Layout 1 | `9e6c034ca530`  |
| 3095   | Layout 1 | `9e6c034ca530`  |
| 3086   | Layout 1 | `9e6c034ca530`  |
| 3072   | Layout 1 | `9e6c034ca530`  |
| 3062   | Layout 1 | `9e6c034ca530`  |
| 3052   | Layout 1 | `9e6c034ca530`  |
| 3045   | Layout 1 | `9e6c034ca530`  |
| 3037   | Layout 1 | `9e6c034ca530`  |
| 3030   | Layout 1 | `9e6c034ca530`  |
| 3021   | Layout 1 | `9e6c034ca530`  |
| 3012   | Layout 1 | `9e6c034ca530`  |
| 3002   | Layout 1 | `9e6c034ca530`  |
| 2995   | Layout 1 | `9e6c034ca530`  |
| 2987   | Layout 1 | `9e6c034ca530`  |
| 2978   | Layout 1 | `9e6c034ca530`  |
| 2970   | Layout 1 | `9e6c034ca530`  |
| 2959   | Layout 1 | `9e6c034ca530`  |
| 2951   | Layout 1 | `9e6c034ca530`  |
| 2942   | Layout 1 | `9e6c034ca530`  |
| 2935   | Layout 1 | `9e6c034ca530`  |
| 2932   | Layout 1 | `9e6c034ca530`  |
| 2923   | Layout 1 | `9e6c034ca530`  |
| 2919   | Layout 1 | `9e6c034ca530`  |
| 2907   | Layout 1 | `9e6c034ca530`  |
| 2900   | Layout 1 | `9e6c034ca530`  |
| 2891   | Layout 1 | `9e6c034ca530`  |
| 2882   | Layout 1 | `9e6c034ca530`  |
| 2872   | Layout 1 | `9e6c034ca530`  |
| 2863   | Layout 1 | `9e6c034ca530`  |
| 2855   | Layout 1 | `9e6c034ca530`  |
| 2849   | Layout 1 | `9e6c034ca530`  |
| 2844   | Layout 1 | `9e6c034ca530`  |
| 2834   | Layout 1 | `9e6c034ca530`  |
| 2825   | Layout 1 | `9e6c034ca530`  |
| 2819   | Layout 1 | `9e6c034ca530`  |
| 2811   | Layout 1 | `9e6c034ca530`  |
| 2803   | Layout 1 | `9e6c034ca530`  |
| 2794   | Layout 1 | `9e6c034ca530`  |
| 2783   | Layout 1 | `9e6c034ca530`  |
| 2774   | Layout 1 | `9e6c034ca530`  |
| 2765   | Layout 1 | `9e6c034ca530`  |
| 2756   | Layout 1 | `9e6c034ca530`  |
| 2750   | Layout 1 | `9e6c034ca530`  |
| 2743   | Layout 1 | `9e6c034ca530`  |
| 2736   | Layout 1 | `9e6c034ca530`  |
| 2726   | Layout 1 | `9e6c034ca530`  |
| 2717   | Layout 1 | `9e6c034ca530`  |
| 2709   | Layout 1 | `9e6c034ca530`  |
| 2703   | Layout 1 | `9e6c034ca530`  |
| 2695   | Layout 1 | `9e6c034ca530`  |
| 2684   | Layout 1 | `9e6c034ca530`  |
| 2672   | Layout 1 | `9e6c034ca530`  |
| 2665   | Layout 1 | `9e6c034ca530`  |
| 2657   | Layout 1 | `9e6c034ca530`  |
| 2649   | Layout 1 | `9e6c034ca530`  |
| 2644   | Layout 1 | `9e6c034ca530`  |
| 2637   | Layout 1 | `9e6c034ca530`  |
| 2629   | Layout 1 | `9e6c034ca530`  |
| 2619   | Layout 1 | `9e6c034ca530`  |
| 2612   | Layout 1 | `9e6c034ca530`  |
| 2606   | Layout 1 | `9e6c034ca530`  |
| 2602   | Layout 1 | `9e6c034ca530`  |
| 2601   | Layout 1 | `9e6c034ca530`  |
| 2592   | Layout 1 | `9e6c034ca530`  |
| 2583   | Layout 1 | `9e6c034ca530`  |
| 2575   | Layout 1 | `9e6c034ca530`  |
| 2567   | Layout 1 | `9e6c034ca530`  |
| 2560   | Layout 1 | `9e6c034ca530`  |
| 2553   | Layout 1 | `9e6c034ca530`  |
| 2545   | Layout 1 | `9e6c034ca530`  |
| 2538   | Layout 1 | `9e6c034ca530`  |
| 2529   | Layout 1 | `9e6c034ca530`  |
| 2519   | Layout 1 | `9e6c034ca530`  |
| 2513   | Layout 1 | `9e6c034ca530`  |
| 2510   | Layout 1 | `9e6c034ca530`  |
| 2507   | Layout 1 | `9e6c034ca530`  |
| 2503   | Layout 1 | `9e6c034ca530`  |
| 2498   | Layout 1 | `9e6c034ca530`  |
| 2492   | Layout 1 | `9e6c034ca530`  |
| 2487   | Layout 1 | `9e6c034ca530`  |
| 2480   | Layout 1 | `9e6c034ca530`  |
| 2474   | Layout 1 | `9e6c034ca530`  |
| 2468   | Layout 1 | `9e6c034ca530`  |
| 2460   | Layout 1 | `9e6c034ca530`  |
| 2453   | Layout 1 | `9e6c034ca530`  |
| 2444   | Layout 1 | `9e6c034ca530`  |
| 2438   | Layout 1 | `9e6c034ca530`  |
| 2434   | Layout 1 | `9e6c034ca530`  |
| 2429   | Layout 1 | `9e6c034ca530`  |
| 2421   | Layout 1 | `9e6c034ca530`  |
| 2414   | Layout 1 | `9e6c034ca530`  |
| 2407   | Layout 1 | `9e6c034ca530`  |
| 2401   | Layout 1 | `9e6c034ca530`  |
| 2397   | Layout 1 | `9e6c034ca530`  |
| 2393   | Layout 1 | `9e6c034ca530`  |
| 2384   | Layout 1 | `9e6c034ca530`  |
| 2378   | Layout 1 | `9e6c034ca530`  |
| 2372   | Layout 1 | `9e6c034ca530`  |
| 2358   | Layout 1 | `9e6c034ca530`  |
| 2352   | Layout 1 | `9e6c034ca530`  |
| 2347   | Layout 1 | `9e6c034ca530`  |
| 2343   | Layout 1 | `9e6c034ca530`  |
| 2335   | Layout 1 | `9e6c034ca530`  |
| 2327   | Layout 1 | `9e6c034ca530`  |
| 2324   | Layout 1 | `9e6c034ca530`  |
| 2319   | Layout 1 | `9e6c034ca530`  |
| 2313   | Layout 1 | `9e6c034ca530`  |
| 2308   | Layout 1 | `9e6c034ca530`  |
| 2302   | Layout 1 | `9e6c034ca530`  |
| 2295   | Layout 1 | `9e6c034ca530`  |
| 2290   | Layout 1 | `9e6c034ca530`  |
| 2284   | Layout 1 | `9e6c034ca530`  |
| 2276   | Layout 1 | `9e6c034ca530`  |
| 2269   | Layout 1 | `9e6c034ca530`  |
| 2259   | Layout 1 | `9e6c034ca530`  |
| 2250   | Layout 1 | `9e6c034ca530`  |
| 2243   | Layout 1 | `9e6c034ca530`  |
| 2235   | Layout 1 | `9e6c034ca530`  |
| 2229   | Layout 1 | `9e6c034ca530`  |
| 2224   | Layout 1 | `9e6c034ca530`  |
| 2218   | No file  | `9e6c034ca530`  |
| 2215   | No file  | `9e6c034ca530`  |
| 2207   | No file  | `9e6c034ca530`  |
| 2203   | No file  | `9e6c034ca530`  |
| 2196   | No file  | `9e6c034ca530`  |
| 2192   | No file  | `9e6c034ca530`  |
| 2189   | No file  | `9e6c034ca530`  |
| 2183   | No file  | `9e6c034ca530`  |
| 2179   | No file  | `9e6c034ca530`  |
| 2171   | No file  | `9e6c034ca530`  |
| 2163   | No file  | `9e6c034ca530`  |
| 2156   | No file  | `9e6c034ca530`  |
| 2151   | No file  | `9e6c034ca530`  |
| 2147   | No file  | `9e6c034ca530`  |
| 2142   | No file  | `9e6c034ca530`  |
| 2138   | No file  | `9e6c034ca530`  |
| 2134   | No file  | `9e6c034ca530`  |
| 2130   | No file  | `9e6c034ca530`  |
| 2122   | No file  | `9e6c034ca530`  |
| 2107   | No file  | `9e6c034ca530`  |
| 2098   | No file  | `9e6c034ca530`  |
| 2089   | No file  | `9e6c034ca530`  |
| 2081   | No file  | `9e6c034ca530`  |
| 2073   | No file  | `9e6c034ca530`  |
| 2067   | No file  | `9e6c034ca530`  |
| 2063   | No file  | `9e6c034ca530`  |
| 2059   | No file  | `9e6c034ca530`  |
| 2052   | No file  | `9e6c034ca530`  |
| 2044   | No file  | `9e6c034ca530`  |
| 2039   | No file  | `9e6c034ca530`  |
| 2032   | No file  | `9e6c034ca530`  |
| 2025   | No file  | `9e6c034ca530`  |
| 2011   | No file  | `9e6c034ca530`  |
| 2005   | No file  | `9e6c034ca530`  |
| 2000   | No file  | `9e6c034ca530`  |
| 1996   | No file  | `9e6c034ca530`  |
| 1991   | No file  | `9e6c034ca530`  |
| 1985   | No file  | `9e6c034ca530`  |
| 1980   | No file  | `9e6c034ca530`  |
| 1969   | No file  | `9e6c034ca530`  |
| 1964   | No file  | `9e6c034ca530`  |
| 1958   | No file  | `9e6c034ca530`  |
| 1950   | No file  | `9e6c034ca530`  |
| 1945   | No file  | `9e6c034ca530`  |
| 1937   | No file  | `9e6c034ca530`  |
| 1933   | No file  | `9e6c034ca530`  |
| 1927   | No file  | `9e6c034ca530`  |
| 1921   | No file  | `9e6c034ca530`  |
| 1914   | No file  | `9e6c034ca530`  |
| 1908   | No file  | `9e6c034ca530`  |
| 1897   | No file  | `9e6c034ca530`  |
| 1892   | No file  | `9e6c034ca530`  |
| 1886   | No file  | `9e6c034ca530`  |
| 1881   | No file  | `9e6c034ca530`  |
| 1871   | No file  | `9e6c034ca530`  |
| 1866   | No file  | `9e6c034ca530`  |
| 1862   | No file  | `9e6c034ca530`  |
| 1854   | No file  | `9e6c034ca530`  |
| 1846   | No file  | `9e6c034ca530`  |
| 1838   | No file  | `9e6c034ca530`  |
| 1832   | No file  | `9e6c034ca530`  |
| 1826   | No file  | `9e6c034ca530`  |
| 1822   | No file  | `9e6c034ca530`  |
| 1818   | No file  | `9e6c034ca530`  |
| 1804   | No file  | `9e6c034ca530`  |
| 1794   | No file  | `9e6c034ca530`  |
| 1790   | No file  | `9e6c034ca530`  |
| 1784   | No file  | `9e6c034ca530`  |
| 1774   | No file  | `9e6c034ca530`  |
| 1771   | No file  | `9e6c034ca530`  |
| 1762   | No file  | `9e6c034ca530`  |
| 1759   | No file  | `9e6c034ca530`  |
| 1754   | No file  | `9e6c034ca530`  |
| 1749   | No file  | `9e6c034ca530`  |
| 1743   | No file  | `9e6c034ca530`  |
| 1737   | No file  | `9e6c034ca530`  |
| 1731   | No file  | `9e6c034ca530`  |
| 1725   | No file  | `9e6c034ca530`  |
| 1717   | No file  | `9e6c034ca530`  |
| 1710   | No file  | `9e6c034ca530`  |
| 1704   | No file  | `9e6c034ca530`  |
| 1698   | No file  | `9e6c034ca530`  |
| 1690   | No file  | `9e6c034ca530`  |
| 1685   | No file  | `9e6c034ca530`  |
| 1680   | No file  | `9e6c034ca530`  |
| 1674   | No file  | `9e6c034ca530`  |
| 1668   | No file  | `9e6c034ca530`  |
| 1659   | No file  | `9e6c034ca530`  |
| 1649   | No file  | `9e6c034ca530`  |
| 1642   | No file  | `9e6c034ca530`  |
| 1636   | No file  | `9e6c034ca530`  |
| 1628   | No file  | `9e6c034ca530`  |
| 1622   | No file  | `9e6c034ca530`  |
| 1614   | No file  | `9e6c034ca530`  |
| 1608   | No file  | `9e6c034ca530`  |
| 1602   | No file  | `9e6c034ca530`  |
| 1598   | No file  | `9e6c034ca530`  |
| 1594   | No file  | `9e6c034ca530`  |
| 1590   | No file  | `9e6c034ca530`  |
| 1587   | No file  | `9e6c034ca530`  |
| 1584   | No file  | `9e6c034ca530`  |
| 1579   | No file  | `9e6c034ca530`  |
| 1572   | No file  | `9e6c034ca530`  |
| 1565   | No file  | `9e6c034ca530`  |
| 1559   | No file  | `9e6c034ca530`  |
| 1554   | No file  | `9e6c034ca530`  |
| 1547   | No file  | `9e6c034ca530`  |
| 1537   | No file  | `9e6c034ca530`  |
| 1529   | No file  | `9e6c034ca530`  |
| 1524   | No file  | `9e6c034ca530`  |
| 1519   | No file  | `9e6c034ca530`  |
| 1509   | No file  | `9e6c034ca530`  |
| 1506   | No file  | `9e6c034ca530`  |
| 1504   | No file  | `9e6c034ca530`  |
| 1500   | No file  | `9e6c034ca530`  |
| 1493   | No file  | `9e6c034ca530`  |
| 1489   | No file  | `9e6c034ca530`  |
| 1485   | No file  | `9e6c034ca530`  |
| 1481   | No file  | `9e6c034ca530`  |
| 1474   | No file  | `9e6c034ca530`  |
| 1466   | No file  | `9e6c034ca530`  |
| 1462   | No file  | `9e6c034ca530`  |
| 1459   | No file  | `9e6c034ca530`  |
| 1453   | No file  | `9e6c034ca530`  |
| 1450   | No file  | `9e6c034ca530`  |
| 1445   | No file  | `9e6c034ca530`  |
| 1439   | No file  | `9e6c034ca530`  |
| 1433   | No file  | `9e6c034ca530`  |
| 1430   | No file  | `9e6c034ca530`  |
| 1426   | No file  | `9e6c034ca530`  |
| 1421   | No file  | `9e6c034ca530`  |
| 1417   | No file  | `9e6c034ca530`  |
| 1416   | No file  | `9e6c034ca530`  |
| 1409   | No file  | `9e6c034ca530`  |
| 1405   | No file  | `9e6c034ca530`  |
| 1401   | No file  | `9e6c034ca530`  |
| 1396   | No file  | `9e6c034ca530`  |
| 1391   | No file  | `9e6c034ca530`  |
| 1390   | No file  | `9e6c034ca530`  |
| 1386   | No file  | `9e6c034ca530`  |
| 1381   | No file  | `9e6c034ca530`  |
| 1379   | No file  | `9e6c034ca530`  |
| 1372   | No file  | `9e6c034ca530`  |
| 1366   | No file  | `9e6c034ca530`  |
| 1364   | No file  | `9e6c034ca530`  |
| 1363   | No file  | `9e6c034ca530`  |
| 1360   | No file  | `9e6c034ca530`  |
| 1358   | No file  | `9e6c034ca530`  |
| 1355   | No file  | `9e6c034ca530`  |
| 1351   | No file  | `9e6c034ca530`  |
| 1348   | No file  | `9e6c034ca530`  |
| 1346   | No file  | `9e6c034ca530`  |
| 1341   | No file  | `9e6c034ca530`  |
| 1340   | No file  | `9e6c034ca530`  |
| 1338   | No file  | `9e6c034ca530`  |
| 1335   | No file  | `9e6c034ca530`  |
| 1333   | No file  | `9e6c034ca530`  |
| 1329   | No file  | `9e6c034ca530`  |
| 1327   | No file  | `9e6c034ca530`  |
| 1324   | No file  | `9e6c034ca530`  |
| 1321   | No file  | `9e6c034ca530`  |
| 1319   | No file  | `9e6c034ca530`  |
| 1318   | No file  | `9e6c034ca530`  |
| 1316   | No file  | `9e6c034ca530`  |
| 1313   | No file  | `9e6c034ca530`  |
| 1311   | No file  | `9e6c034ca530`  |
| 1309   | No file  | `9e6c034ca530`  |
| 1304   | No file  | `9e6c034ca530`  |
| 1292   | No file  | `9e6c034ca530`  |
| 1286   | No file  | `9e6c034ca530`  |
| 1280   | No file  | `9e6c034ca530`  |
| 1276   | No file  | `9e6c034ca530`  |
| 1267   | No file  | `9e6c034ca530`  |
| 1261   | No file  | `9e6c034ca530`  |
| 1256   | No file  | `9e6c034ca530`  |
| 1250   | No file  | `9e6c034ca530`  |
| 1246   | No file  | `9e6c034ca530`  |
| 1239   | No file  | `9e6c034ca530`  |
| 1230   | No file  | `9e6c034ca530`  |
| 1226   | No file  | `9e6c034ca530`  |
| 1220   | No file  | `9e6c034ca530`  |
| 1217   | No file  | `9e6c034ca530`  |
| 1211   | No file  | `9e6c034ca530`  |
| 1210   | No file  | `9e6c034ca530`  |
| 1208   | No file  | `9e6c034ca530`  |
| 1203   | No file  | `9e6c034ca530`  |
| 1197   | No file  | `9e6c034ca530`  |
| 1194   | No file  | `9e6c034ca530`  |
| 1192   | No file  | `9e6c034ca530`  |
| 1187   | No file  | `9e6c034ca530`  |
| 1183   | No file  | `9e6c034ca530`  |
| 1177   | No file  | `9e6c034ca530`  |
| 1173   | No file  | `9e6c034ca530`  |
| 1167   | No file  | `9e6c034ca530`  |
| 1164   | No file  | `9e6c034ca530`  |
| 1156   | No file  | `9e6c034ca530`  |
| 1149   | No file  | `9e6c034ca530`  |
| 1144   | No file  | `9e6c034ca530`  |
| 1137   | No file  | `9e6c034ca530`  |
| 1132   | No file  | `9e6c034ca530`  |
| 1127   | No file  | `9e6c034ca530`  |
| 1122   | No file  | `9e6c034ca530`  |
| 1118   | No file  | `9e6c034ca530`  |
| 1114   | No file  | `9e6c034ca530`  |
| 1109   | No file  | `9e6c034ca530`  |
| 1102   | No file  | `9e6c034ca530`  |
| 1096   | No file  | `9e6c034ca530`  |
| 1088   | No file  | `9e6c034ca530`  |
| 1081   | No file  | `9e6c034ca530`  |
| 1076   | No file  | `9e6c034ca530`  |
| 1069   | No file  | `9e6c034ca530`  |
| 1064   | No file  | `9e6c034ca530`  |
| 1058   | No file  | `9e6c034ca530`  |
| 1051   | No file  | `9e6c034ca530`  |
| 1044   | No file  | `9e6c034ca530`  |
| 1036   | No file  | `9e6c034ca530`  |
| 1026   | No file  | `9e6c034ca530`  |
| 1016   | No file  | `9e6c034ca530`  |
| 1009   | No file  | `9e6c034ca530`  |
| 1005   | No file  | `9e6c034ca530`  |
| 1000   | No file  | `9e6c034ca530`  |
| 998    | No file  | `9e6c034ca530`  |
| 990    | No file  | `9e6c034ca530`  |
| 979    | No file  | `9e6c034ca530`  |
| 972    | No file  | `9e6c034ca530`  |
| 963    | No file  | `9e6c034ca530`  |
| 955    | No file  | `9e6c034ca530`  |
| 946    | No file  | `9e6c034ca530`  |
| 938    | No file  | `9e6c034ca530`  |
| 927    | No file  | `9e6c034ca530`  |
| 911    | No file  | `9e6c034ca530`  |
| 904    | No file  | `9e6c034ca530`  |
| 899    | No file  | `9e6c034ca530`  |
| 894    | No file  | `9e6c034ca530`  |
| 885    | No file  | `9e6c034ca530`  |
| 879    | No file  | `9e6c034ca530`  |
| 872    | No file  | `9e6c034ca530`  |
| 864    | No file  | `9e6c034ca530`  |
| 855    | No file  | `9e6c034ca530`  |
| 853    | No file  | `9e6c034ca530`  |
| 845    | No file  | `9e6c034ca530`  |
| 837    | No file  | `9e6c034ca530`  |
| 829    | No file  | `9e6c034ca530`  |
| 822    | No file  | `9e6c034ca530`  |
| 814    | No file  | `9e6c034ca530`  |
| 805    | No file  | `9e6c034ca530`  |
| 794    | No file  | `9e6c034ca530`  |
| 787    | No file  | `9e6c034ca530`  |
| 780    | No file  | `9e6c034ca530`  |
| 771    | No file  | `9e6c034ca530`  |
| 760    | No file  | `9e6c034ca530`  |
| 748    | No file  | `9e6c034ca530`  |
| 741    | No file  | `9e6c034ca530`  |
| 736    | No file  | `9e6c034ca530`  |
| 731    | No file  | `9e6c034ca530`  |
| 723    | No file  | `9e6c034ca530`  |
| 711    | No file  | `9e6c034ca530`  |
| 707    | No file  | `9e6c034ca530`  |
| 697    | No file  | `9e6c034ca530`  |
| 689    | No file  | `9e6c034ca530`  |
| 683    | No file  | `9e6c034ca530`  |
| 678    | No file  | `9e6c034ca530`  |
| 670    | No file  | `9e6c034ca530`  |
| 661    | No file  | `9e6c034ca530`  |
| 656    | No file  | `9e6c034ca530`  |
| 652    | No file  | `9e6c034ca530`  |
| 643    | No file  | `9e6c034ca530`  |
| 637    | No file  | `9e6c034ca530`  |
| 630    | No file  | `9e6c034ca530`  |
| 627    | No file  | `9e6c034ca530`  |
| 621    | No file  | `9e6c034ca530`  |
| 617    | No file  | `9e6c034ca530`  |
| 615    | No file  | `9e6c034ca530`  |
| 606    | No file  | `9e6c034ca530`  |
| 599    | No file  | `9e6c034ca530`  |
| 592    | No file  | `9e6c034ca530`  |
| 586    | No file  | `9e6c034ca530`  |
| 577    | No file  | `9e6c034ca530`  |
| 569    | No file  | `9e6c034ca530`  |
| 561    | No file  | `9e6c034ca530`  |
| 554    | No file  | `9e6c034ca530`  |
| 542    | No file  | `9e6c034ca530`  |
| 532    | No file  | `9e6c034ca530`  |
| 531    | No file  | `9e6c034ca530`  |
| 526    | No file  | `9e6c034ca530`  |
| 521    | No file  | `9e6c034ca530`  |
| 517    | No file  | `9e6c034ca530`  |
| 510    | No file  | `9e6c034ca530`  |
| 508    | No file  | `9e6c034ca530`  |
| 504    | No file  | `9e6c034ca530`  |
| 497    | No file  | `9e6c034ca530`  |
| 491    | No file  | `9e6c034ca530`  |
| 485    | No file  | `9e6c034ca530`  |
| 478    | No file  | `9e6c034ca530`  |
| 472    | No file  | `9e6c034ca530`  |
| 466    | No file  | `9e6c034ca530`  |
| 457    | No file  | `9e6c034ca530`  |
| 452    | No file  | `9e6c034ca530`  |
| 449    | No file  | `9e6c034ca530`  |
| 435    | No file  | `9e6c034ca530`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type | Field                | Notes                                                              |
| ------- | ---- | -------------------- | ------------------------------------------------------------------ |
| `+0x00` | u64  | stat_reset_cost      | Silver to reset one aura's Additional Stats; `500000` on clients 2519 to 3474 |
| `+0x08` | u64  | light_orb_reset_cost | Silver to reset the Light Orbs; `2000000` on clients 2519 to 3474  |
| `+0x10` | u8   | weekly_clear_limit   | Black Shrine clears per family per week; `5` on clients 2519 to 3474 |

## Field Names

The client Lua (`panel_window_morningland_boss_all_1.luac`, client 3474)
calls `ToClient_getMorningLandOptionManager()` and reads two silver costs
from it, and no other Lua reads that manager: `getStateResetCost` for the
"Reset Aura stats?" message (`Button_MyStat_Reset`) and
`getAllStatsResetCost` for the "Reset Light Orb?" message
(`Button_Attribute_Reset`). Garmoth's Black Shrine guide (section "Black
Shrine Auras") says "Resetting only your additional stats will be 500k, so
even less than resetting your Light Orbs", which is the `500000` at `+0x00`.
The other cost, `2000000` at `+0x08`, is then the Light Orb reset.

The boss window Lua also counts against `__eElementalMonsterWeekLimit`
(weekly boss conquests), a global no Lua file defines, so the client sets
it. The official update history page "[Update History] Black Shrine (Boss
Blitz)"
([groupMasterNo 8498](https://www.naeu.playblackdesert.com/en-us/Adventure/History?_groupMasterNo=8498))
says "You have 5 weekly successful attempts per Family to defeat bosses of
the Black Shrine" (resetting at midnight on Sunday), which is the `5` at
`+0x10`, the only other value of this option file.

## Notes

- Raw bytes on clients 2519, 3002, 3251 and 3474:
  `20 A1 07 00 00 00 00 00 80 84 1E 00 00 00 00 00 05` (17 bytes).
- The file is not in the client 1784 archive. A private server's
  `DataSheets.bexcel` on client 1784 has no sheet with `MorningLand` in its
  name, so no column names carry over.
- The high four bytes of both u64 fields are `0`, so two u32 values with a
  u32 `0` after each fit the bytes too.
- The installed `BlackDesert64.exe` (client 3474) holds neither the file
  name nor `MorningLandOption` as ASCII or UTF-16 text, so it does not show
  the loader or its struct.
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`: the values alone, with no magic, string table or trailer.
  A file of any other size raises.
