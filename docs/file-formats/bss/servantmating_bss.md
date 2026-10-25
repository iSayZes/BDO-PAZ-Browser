# `servantmating.bss` Format

## Purpose

Horse breeding grade table: one row per band of the parents' average grade,
with the lowest and highest grade a foal of that band can get. Client 3474
adds the Imperial Steed and the band's chance to breed it (Breeding
Results). On client 3474 the file has 34 rows, keys 1 to 36 without 29 and
30.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes | Records       | Row bytes |
| ------ | -------------- | -------------------------- | ----- | ------------- | --------- |
| 2      | 2794 and later | `servantmating.bss`        | 684   | 34 Row        | 20        |
| 1      | 435 to 794     | `servantmating.bss`        | 298   | 21 Row        | 14        |
| 1      | 1346 to 2460   | `servantmating.dbss`       | 340   | 24 Row        | 14        |
| 1      | 1346 to 2460   | `servantmatingoffset.dbss` | 292   | 24 Offset Row | 12        |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 2      | `servantmating.bss`        | 684 B (100.0%) | 0 B (0.0%) |
| 1      | `servantmating.bss`        | 298 B (100.0%) | 0 B (0.0%) |
| 1      | `servantmating.dbss`       | 340 B (100.0%) | 0 B (0.0%) |
| 1      | `servantmatingoffset.dbss` | 292 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `3630e616686c`  |
| 3482   | Layout 2             | `3630e616686c`  |
| 3474   | Layout 2             | `3630e616686c`  |
| 3473   | Layout 2             | `3630e616686c`  |
| 3464   | Layout 2             | `3630e616686c`  |
| 3458   | Layout 2             | `3630e616686c`  |
| 3454   | Layout 2             | `3630e616686c`  |
| 3444   | Layout 2             | `3630e616686c`  |
| 3435   | Layout 2             | `3630e616686c`  |
| 3426   | Layout 2             | `3630e616686c`  |
| 3418   | Layout 2             | `3630e616686c`  |
| 3412   | Layout 2             | `3630e616686c`  |
| 3402   | Layout 2             | `3630e616686c`  |
| 3396   | Layout 2             | `3630e616686c`  |
| 3387   | Layout 2             | `3630e616686c`  |
| 3381   | Layout 2             | `3630e616686c`  |
| 3373   | Layout 2             | `3630e616686c`  |
| 3364   | Layout 2             | `3630e616686c`  |
| 3356   | Layout 2             | `3630e616686c`  |
| 3349   | Layout 2             | `3630e616686c`  |
| 3342   | Layout 2             | `3630e616686c`  |
| 3335   | Layout 2             | `3630e616686c`  |
| 3326   | Layout 2             | `3630e616686c`  |
| 3321   | Layout 2             | `3630e616686c`  |
| 3314   | Layout 2             | `3630e616686c`  |
| 3303   | Layout 2             | `3630e616686c`  |
| 3302   | Layout 2             | `3630e616686c`  |
| 3293   | Layout 2             | `3630e616686c`  |
| 3283   | Layout 2             | `3630e616686c`  |
| 3275   | Layout 2             | `3630e616686c`  |
| 3267   | Layout 2             | `3630e616686c`  |
| 3258   | Layout 2             | `3630e616686c`  |
| 3251   | Layout 2             | `3630e616686c`  |
| 3242   | Layout 2             | `3630e616686c`  |
| 3235   | Layout 2             | `3630e616686c`  |
| 3229   | Layout 2             | `3630e616686c`  |
| 3212   | Layout 2             | `3630e616686c`  |
| 3203   | Layout 2             | `3630e616686c`  |
| 3193   | Layout 2             | `3630e616686c`  |
| 3186   | Layout 2             | `3630e616686c`  |
| 3177   | Layout 2             | `3630e616686c`  |
| 3169   | Layout 2             | `3630e616686c`  |
| 3158   | Layout 2             | `3630e616686c`  |
| 3151   | Layout 2             | `3630e616686c`  |
| 3144   | Layout 2             | `3630e616686c`  |
| 3133   | Layout 2             | `3630e616686c`  |
| 3125   | Layout 2             | `3630e616686c`  |
| 3118   | Layout 2             | `3630e616686c`  |
| 3111   | Layout 2             | `3630e616686c`  |
| 3103   | Layout 2             | `3630e616686c`  |
| 3095   | Layout 2             | `3630e616686c`  |
| 3086   | Layout 2             | `3630e616686c`  |
| 3072   | Layout 2             | `3630e616686c`  |
| 3062   | Layout 2             | `3630e616686c`  |
| 3052   | Layout 2             | `3630e616686c`  |
| 3045   | Layout 2             | `3630e616686c`  |
| 3037   | Layout 2             | `3630e616686c`  |
| 3030   | Layout 2             | `3630e616686c`  |
| 3021   | Layout 2             | `3630e616686c`  |
| 3012   | Layout 2             | `3630e616686c`  |
| 3002   | Layout 2             | `3630e616686c`  |
| 2995   | Layout 2             | `3630e616686c`  |
| 2987   | Layout 2             | `3630e616686c`  |
| 2978   | Layout 2             | `3630e616686c`  |
| 2970   | Layout 2             | `3630e616686c`  |
| 2959   | Layout 2             | `3630e616686c`  |
| 2951   | Layout 2             | `3630e616686c`  |
| 2942   | Layout 2             | `3630e616686c`  |
| 2935   | Layout 2             | `3630e616686c`  |
| 2932   | Layout 2             | `3630e616686c`  |
| 2923   | Layout 2             | `3630e616686c`  |
| 2919   | Layout 2             | `3630e616686c`  |
| 2907   | Layout 2             | `3630e616686c`  |
| 2900   | Layout 2             | `3630e616686c`  |
| 2891   | Layout 2             | `3630e616686c`  |
| 2882   | Layout 2             | `3630e616686c`  |
| 2872   | Layout 2             | `3630e616686c`  |
| 2863   | Layout 2             | `3630e616686c`  |
| 2855   | Layout 2             | `3630e616686c`  |
| 2849   | Layout 2             | `3630e616686c`  |
| 2844   | Layout 2             | `3630e616686c`  |
| 2834   | Layout 2             | `3630e616686c`  |
| 2825   | Layout 2             | `3630e616686c`  |
| 2819   | Layout 2             | `3630e616686c`  |
| 2811   | Layout 2             | `3630e616686c`  |
| 2803   | Layout 2             | `3630e616686c`  |
| 2794   | Layout 2             | `3630e616686c`  |
| 2783   | No documented layout | `3630e616686c`  |
| 2774   | No documented layout | `3630e616686c`  |
| 2765   | No documented layout | `3630e616686c`  |
| 2756   | No documented layout | `3630e616686c`  |
| 2750   | No documented layout | `3630e616686c`  |
| 2743   | No documented layout | `3630e616686c`  |
| 2736   | No documented layout | `3630e616686c`  |
| 2726   | No documented layout | `3630e616686c`  |
| 2717   | No documented layout | `3630e616686c`  |
| 2709   | No documented layout | `3630e616686c`  |
| 2703   | No documented layout | `3630e616686c`  |
| 2695   | No documented layout | `3630e616686c`  |
| 2684   | No documented layout | `3630e616686c`  |
| 2672   | No documented layout | `3630e616686c`  |
| 2665   | No documented layout | `3630e616686c`  |
| 2657   | No documented layout | `3630e616686c`  |
| 2649   | No documented layout | `3630e616686c`  |
| 2644   | No documented layout | `3630e616686c`  |
| 2637   | No documented layout | `3630e616686c`  |
| 2629   | No documented layout | `3630e616686c`  |
| 2619   | No documented layout | `3630e616686c`  |
| 2612   | No documented layout | `3630e616686c`  |
| 2606   | No documented layout | `3630e616686c`  |
| 2602   | No documented layout | `3630e616686c`  |
| 2601   | No documented layout | `3630e616686c`  |
| 2592   | No documented layout | `3630e616686c`  |
| 2583   | No documented layout | `3630e616686c`  |
| 2575   | No documented layout | `3630e616686c`  |
| 2567   | No documented layout | `3630e616686c`  |
| 2560   | No documented layout | `3630e616686c`  |
| 2553   | No documented layout | `3630e616686c`  |
| 2545   | No documented layout | `3630e616686c`  |
| 2538   | No documented layout | `3630e616686c`  |
| 2529   | No documented layout | `3630e616686c`  |
| 2519   | No documented layout | `3630e616686c`  |
| 2513   | No documented layout | `3630e616686c`  |
| 2510   | No documented layout | `3630e616686c`  |
| 2507   | No documented layout | `3630e616686c`  |
| 2503   | No documented layout | `3630e616686c`  |
| 2498   | No documented layout | `3630e616686c`  |
| 2492   | No documented layout | `3630e616686c`  |
| 2487   | No documented layout | `3630e616686c`  |
| 2480   | No documented layout | `3630e616686c`  |
| 2474   | No documented layout | `3630e616686c`  |
| 2468   | No documented layout | `3630e616686c`  |
| 2460   | Layout 1             | `3630e616686c`  |
| 2453   | Layout 1             | `3630e616686c`  |
| 2444   | Layout 1             | `3630e616686c`  |
| 2438   | Layout 1             | `3630e616686c`  |
| 2434   | Layout 1             | `3630e616686c`  |
| 2429   | Layout 1             | `3630e616686c`  |
| 2421   | Layout 1             | `3630e616686c`  |
| 2414   | Layout 1             | `3630e616686c`  |
| 2407   | Layout 1             | `3630e616686c`  |
| 2401   | Layout 1             | `3630e616686c`  |
| 2397   | Layout 1             | `3630e616686c`  |
| 2393   | Layout 1             | `3630e616686c`  |
| 2384   | Layout 1             | `3630e616686c`  |
| 2378   | Layout 1             | `3630e616686c`  |
| 2372   | Layout 1             | `3630e616686c`  |
| 2358   | Layout 1             | `3630e616686c`  |
| 2352   | Layout 1             | `3630e616686c`  |
| 2347   | Layout 1             | `3630e616686c`  |
| 2343   | Layout 1             | `3630e616686c`  |
| 2335   | Layout 1             | `3630e616686c`  |
| 2327   | Layout 1             | `3630e616686c`  |
| 2324   | Layout 1             | `3630e616686c`  |
| 2319   | Layout 1             | `3630e616686c`  |
| 2313   | Layout 1             | `3630e616686c`  |
| 2308   | Layout 1             | `3630e616686c`  |
| 2302   | Layout 1             | `3630e616686c`  |
| 2295   | Layout 1             | `3630e616686c`  |
| 2290   | Layout 1             | `3630e616686c`  |
| 2284   | Layout 1             | `3630e616686c`  |
| 2276   | Layout 1             | `3630e616686c`  |
| 2269   | Layout 1             | `3630e616686c`  |
| 2259   | Layout 1             | `3630e616686c`  |
| 2250   | Layout 1             | `3630e616686c`  |
| 2243   | Layout 1             | `3630e616686c`  |
| 2235   | Layout 1             | `3630e616686c`  |
| 2229   | Layout 1             | `3630e616686c`  |
| 2224   | Layout 1             | `3630e616686c`  |
| 2218   | Layout 1             | `3630e616686c`  |
| 2215   | Layout 1             | `3630e616686c`  |
| 2207   | Layout 1             | `3630e616686c`  |
| 2203   | Layout 1             | `3630e616686c`  |
| 2196   | Layout 1             | `3630e616686c`  |
| 2192   | Layout 1             | `3630e616686c`  |
| 2189   | Layout 1             | `3630e616686c`  |
| 2183   | Layout 1             | `3630e616686c`  |
| 2179   | Layout 1             | `3630e616686c`  |
| 2171   | Layout 1             | `3630e616686c`  |
| 2163   | Layout 1             | `3630e616686c`  |
| 2156   | Layout 1             | `3630e616686c`  |
| 2151   | Layout 1             | `3630e616686c`  |
| 2147   | Layout 1             | `3630e616686c`  |
| 2142   | Layout 1             | `3630e616686c`  |
| 2138   | Layout 1             | `3630e616686c`  |
| 2134   | Layout 1             | `3630e616686c`  |
| 2130   | Layout 1             | `3630e616686c`  |
| 2122   | Layout 1             | `3630e616686c`  |
| 2107   | Layout 1             | `3630e616686c`  |
| 2098   | Layout 1             | `3630e616686c`  |
| 2089   | Layout 1             | `3630e616686c`  |
| 2081   | Layout 1             | `3630e616686c`  |
| 2073   | Layout 1             | `3630e616686c`  |
| 2067   | Layout 1             | `3630e616686c`  |
| 2063   | Layout 1             | `3630e616686c`  |
| 2059   | Layout 1             | `3630e616686c`  |
| 2052   | Layout 1             | `3630e616686c`  |
| 2044   | Layout 1             | `3630e616686c`  |
| 2039   | Layout 1             | `3630e616686c`  |
| 2032   | Layout 1             | `3630e616686c`  |
| 2025   | Layout 1             | `3630e616686c`  |
| 2011   | Layout 1             | `3630e616686c`  |
| 2005   | Layout 1             | `3630e616686c`  |
| 2000   | Layout 1             | `3630e616686c`  |
| 1996   | Layout 1             | `3630e616686c`  |
| 1991   | Layout 1             | `3630e616686c`  |
| 1985   | Layout 1             | `3630e616686c`  |
| 1980   | Layout 1             | `3630e616686c`  |
| 1969   | Layout 1             | `3630e616686c`  |
| 1964   | Layout 1             | `3630e616686c`  |
| 1958   | Layout 1             | `3630e616686c`  |
| 1950   | Layout 1             | `3630e616686c`  |
| 1945   | Layout 1             | `3630e616686c`  |
| 1937   | Layout 1             | `3630e616686c`  |
| 1933   | Layout 1             | `3630e616686c`  |
| 1927   | Layout 1             | `3630e616686c`  |
| 1921   | Layout 1             | `3630e616686c`  |
| 1914   | Layout 1             | `3630e616686c`  |
| 1908   | Layout 1             | `3630e616686c`  |
| 1897   | Layout 1             | `3630e616686c`  |
| 1892   | Layout 1             | `3630e616686c`  |
| 1886   | Layout 1             | `3630e616686c`  |
| 1881   | Layout 1             | `3630e616686c`  |
| 1871   | Layout 1             | `3630e616686c`  |
| 1866   | Layout 1             | `3630e616686c`  |
| 1862   | Layout 1             | `3630e616686c`  |
| 1854   | Layout 1             | `3630e616686c`  |
| 1846   | Layout 1             | `3630e616686c`  |
| 1838   | Layout 1             | `3630e616686c`  |
| 1832   | Layout 1             | `3630e616686c`  |
| 1826   | Layout 1             | `3630e616686c`  |
| 1822   | Layout 1             | `3630e616686c`  |
| 1818   | Layout 1             | `3630e616686c`  |
| 1804   | Layout 1             | `3630e616686c`  |
| 1794   | Layout 1             | `3630e616686c`  |
| 1790   | Layout 1             | `3630e616686c`  |
| 1784   | Layout 1             | `3630e616686c`  |
| 1774   | Layout 1             | `3630e616686c`  |
| 1771   | Layout 1             | `3630e616686c`  |
| 1762   | Layout 1             | `3630e616686c`  |
| 1759   | Layout 1             | `3630e616686c`  |
| 1754   | Layout 1             | `3630e616686c`  |
| 1749   | Layout 1             | `3630e616686c`  |
| 1743   | Layout 1             | `3630e616686c`  |
| 1737   | Layout 1             | `3630e616686c`  |
| 1731   | Layout 1             | `3630e616686c`  |
| 1725   | Layout 1             | `3630e616686c`  |
| 1717   | Layout 1             | `3630e616686c`  |
| 1710   | Layout 1             | `3630e616686c`  |
| 1704   | Layout 1             | `3630e616686c`  |
| 1698   | Layout 1             | `3630e616686c`  |
| 1690   | Layout 1             | `3630e616686c`  |
| 1685   | Layout 1             | `3630e616686c`  |
| 1680   | Layout 1             | `3630e616686c`  |
| 1674   | Layout 1             | `3630e616686c`  |
| 1668   | Layout 1             | `3630e616686c`  |
| 1659   | Layout 1             | `3630e616686c`  |
| 1649   | Layout 1             | `3630e616686c`  |
| 1642   | Layout 1             | `3630e616686c`  |
| 1636   | Layout 1             | `3630e616686c`  |
| 1628   | Layout 1             | `3630e616686c`  |
| 1622   | Layout 1             | `3630e616686c`  |
| 1614   | Layout 1             | `3630e616686c`  |
| 1608   | Layout 1             | `3630e616686c`  |
| 1602   | Layout 1             | `3630e616686c`  |
| 1598   | Layout 1             | `3630e616686c`  |
| 1594   | Layout 1             | `3630e616686c`  |
| 1590   | Layout 1             | `3630e616686c`  |
| 1587   | Layout 1             | `3630e616686c`  |
| 1584   | Layout 1             | `3630e616686c`  |
| 1579   | Layout 1             | `3630e616686c`  |
| 1572   | Layout 1             | `3630e616686c`  |
| 1565   | Layout 1             | `3630e616686c`  |
| 1559   | Layout 1             | `3630e616686c`  |
| 1554   | Layout 1             | `3630e616686c`  |
| 1547   | Layout 1             | `3630e616686c`  |
| 1537   | Layout 1             | `3630e616686c`  |
| 1529   | Layout 1             | `3630e616686c`  |
| 1524   | Layout 1             | `3630e616686c`  |
| 1519   | Layout 1             | `3630e616686c`  |
| 1509   | Layout 1             | `3630e616686c`  |
| 1506   | Layout 1             | `3630e616686c`  |
| 1504   | Layout 1             | `3630e616686c`  |
| 1500   | Layout 1             | `3630e616686c`  |
| 1493   | Layout 1             | `3630e616686c`  |
| 1489   | Layout 1             | `3630e616686c`  |
| 1485   | Layout 1             | `3630e616686c`  |
| 1481   | Layout 1             | `3630e616686c`  |
| 1474   | Layout 1             | `3630e616686c`  |
| 1466   | Layout 1             | `3630e616686c`  |
| 1462   | Layout 1             | `3630e616686c`  |
| 1459   | Layout 1             | `3630e616686c`  |
| 1453   | Layout 1             | `3630e616686c`  |
| 1450   | Layout 1             | `3630e616686c`  |
| 1445   | Layout 1             | `3630e616686c`  |
| 1439   | Layout 1             | `3630e616686c`  |
| 1433   | Layout 1             | `3630e616686c`  |
| 1430   | Layout 1             | `3630e616686c`  |
| 1426   | Layout 1             | `3630e616686c`  |
| 1421   | Layout 1             | `3630e616686c`  |
| 1417   | Layout 1             | `3630e616686c`  |
| 1416   | Layout 1             | `3630e616686c`  |
| 1409   | Layout 1             | `3630e616686c`  |
| 1405   | Layout 1             | `3630e616686c`  |
| 1401   | Layout 1             | `3630e616686c`  |
| 1396   | Layout 1             | `3630e616686c`  |
| 1391   | Layout 1             | `3630e616686c`  |
| 1390   | Layout 1             | `3630e616686c`  |
| 1386   | Layout 1             | `3630e616686c`  |
| 1381   | Layout 1             | `3630e616686c`  |
| 1379   | Layout 1             | `3630e616686c`  |
| 1372   | Layout 1             | `3630e616686c`  |
| 1366   | Layout 1             | `3630e616686c`  |
| 1364   | Layout 1             | `3630e616686c`  |
| 1363   | Layout 1             | `3630e616686c`  |
| 1360   | Layout 1             | `3630e616686c`  |
| 1358   | Layout 1             | `3630e616686c`  |
| 1355   | Layout 1             | `3630e616686c`  |
| 1351   | Layout 1             | `3630e616686c`  |
| 1348   | Layout 1             | `3630e616686c`  |
| 1346   | Layout 1             | `3630e616686c`  |
| 1341   | No documented layout | `3630e616686c`  |
| 1340   | No documented layout | `3630e616686c`  |
| 1338   | No documented layout | `3630e616686c`  |
| 1335   | No documented layout | `3630e616686c`  |
| 1333   | No documented layout | `3630e616686c`  |
| 1329   | No documented layout | `3630e616686c`  |
| 1327   | No documented layout | `3630e616686c`  |
| 1324   | No documented layout | `3630e616686c`  |
| 1321   | No documented layout | `3630e616686c`  |
| 1319   | No documented layout | `3630e616686c`  |
| 1318   | No documented layout | `3630e616686c`  |
| 1316   | No documented layout | `3630e616686c`  |
| 1313   | No documented layout | `3630e616686c`  |
| 1311   | No documented layout | `3630e616686c`  |
| 1309   | No documented layout | `3630e616686c`  |
| 1304   | No documented layout | `3630e616686c`  |
| 1292   | No documented layout | `3630e616686c`  |
| 1286   | No documented layout | `3630e616686c`  |
| 1280   | No documented layout | `3630e616686c`  |
| 1276   | No documented layout | `3630e616686c`  |
| 1267   | No documented layout | `3630e616686c`  |
| 1261   | No documented layout | `3630e616686c`  |
| 1256   | No documented layout | `3630e616686c`  |
| 1250   | No documented layout | `3630e616686c`  |
| 1246   | No documented layout | `3630e616686c`  |
| 1239   | No documented layout | `3630e616686c`  |
| 1230   | No documented layout | `3630e616686c`  |
| 1226   | No documented layout | `3630e616686c`  |
| 1220   | No documented layout | `3630e616686c`  |
| 1217   | No documented layout | `3630e616686c`  |
| 1211   | No documented layout | `3630e616686c`  |
| 1210   | No documented layout | `3630e616686c`  |
| 1208   | No documented layout | `3630e616686c`  |
| 1203   | No documented layout | `3630e616686c`  |
| 1197   | No documented layout | `3630e616686c`  |
| 1194   | No documented layout | `3630e616686c`  |
| 1192   | No documented layout | `3630e616686c`  |
| 1187   | No documented layout | `3630e616686c`  |
| 1183   | No documented layout | `3630e616686c`  |
| 1177   | No documented layout | `3630e616686c`  |
| 1173   | No documented layout | `3630e616686c`  |
| 1167   | No documented layout | `3630e616686c`  |
| 1164   | No documented layout | `3630e616686c`  |
| 1156   | No documented layout | `3630e616686c`  |
| 1149   | No documented layout | `3630e616686c`  |
| 1144   | No documented layout | `3630e616686c`  |
| 1137   | No documented layout | `3630e616686c`  |
| 1132   | No documented layout | `3630e616686c`  |
| 1127   | No documented layout | `3630e616686c`  |
| 1122   | No documented layout | `3630e616686c`  |
| 1118   | No documented layout | `3630e616686c`  |
| 1114   | No documented layout | `3630e616686c`  |
| 1109   | No documented layout | `3630e616686c`  |
| 1102   | No documented layout | `3630e616686c`  |
| 1096   | No documented layout | `3630e616686c`  |
| 1088   | No documented layout | `3630e616686c`  |
| 1081   | No documented layout | `3630e616686c`  |
| 1076   | No documented layout | `3630e616686c`  |
| 1069   | No documented layout | `3630e616686c`  |
| 1064   | No documented layout | `3630e616686c`  |
| 1058   | No documented layout | `3630e616686c`  |
| 1051   | No documented layout | `3630e616686c`  |
| 1044   | No documented layout | `3630e616686c`  |
| 1036   | No documented layout | `3630e616686c`  |
| 1026   | No documented layout | `3630e616686c`  |
| 1016   | No documented layout | `3630e616686c`  |
| 1009   | No documented layout | `3630e616686c`  |
| 1005   | No documented layout | `3630e616686c`  |
| 1000   | No documented layout | `3630e616686c`  |
| 998    | No documented layout | `3630e616686c`  |
| 990    | No documented layout | `3630e616686c`  |
| 979    | No documented layout | `3630e616686c`  |
| 972    | No documented layout | `3630e616686c`  |
| 963    | No documented layout | `3630e616686c`  |
| 955    | No documented layout | `3630e616686c`  |
| 946    | No documented layout | `3630e616686c`  |
| 938    | No documented layout | `3630e616686c`  |
| 927    | No documented layout | `3630e616686c`  |
| 911    | No documented layout | `3630e616686c`  |
| 904    | No documented layout | `3630e616686c`  |
| 899    | No documented layout | `3630e616686c`  |
| 894    | No documented layout | `3630e616686c`  |
| 885    | No documented layout | `3630e616686c`  |
| 879    | No documented layout | `3630e616686c`  |
| 872    | No documented layout | `3630e616686c`  |
| 864    | No documented layout | `3630e616686c`  |
| 855    | No documented layout | `3630e616686c`  |
| 853    | No documented layout | `3630e616686c`  |
| 845    | No documented layout | `3630e616686c`  |
| 837    | No documented layout | `3630e616686c`  |
| 829    | No documented layout | `3630e616686c`  |
| 822    | No documented layout | `3630e616686c`  |
| 814    | No documented layout | `3630e616686c`  |
| 805    | No documented layout | `3630e616686c`  |
| 794    | Layout 1             | `3630e616686c`  |
| 787    | Layout 1             | `3630e616686c`  |
| 780    | Layout 1             | `3630e616686c`  |
| 771    | Layout 1             | `3630e616686c`  |
| 760    | Layout 1             | `3630e616686c`  |
| 748    | Layout 1             | `3630e616686c`  |
| 741    | Layout 1             | `3630e616686c`  |
| 736    | Layout 1             | `3630e616686c`  |
| 731    | Layout 1             | `3630e616686c`  |
| 723    | Layout 1             | `3630e616686c`  |
| 711    | Layout 1             | `3630e616686c`  |
| 707    | Layout 1             | `3630e616686c`  |
| 697    | Layout 1             | `3630e616686c`  |
| 689    | Layout 1             | `3630e616686c`  |
| 683    | Layout 1             | `3630e616686c`  |
| 678    | Layout 1             | `3630e616686c`  |
| 670    | Layout 1             | `3630e616686c`  |
| 661    | Layout 1             | `3630e616686c`  |
| 656    | Layout 1             | `3630e616686c`  |
| 652    | Layout 1             | `3630e616686c`  |
| 643    | Layout 1             | `3630e616686c`  |
| 637    | Layout 1             | `3630e616686c`  |
| 630    | Layout 1             | `3630e616686c`  |
| 627    | Layout 1             | `3630e616686c`  |
| 621    | Layout 1             | `3630e616686c`  |
| 617    | Layout 1             | `3630e616686c`  |
| 615    | Layout 1             | `3630e616686c`  |
| 606    | Layout 1             | `3630e616686c`  |
| 599    | Layout 1             | `3630e616686c`  |
| 592    | Layout 1             | `3630e616686c`  |
| 586    | Layout 1             | `3630e616686c`  |
| 577    | Layout 1             | `3630e616686c`  |
| 569    | Layout 1             | `3630e616686c`  |
| 561    | Layout 1             | `3630e616686c`  |
| 554    | Layout 1             | `3630e616686c`  |
| 542    | Layout 1             | `3630e616686c`  |
| 532    | Layout 1             | `3630e616686c`  |
| 531    | Layout 1             | `3630e616686c`  |
| 526    | Layout 1             | `3630e616686c`  |
| 521    | Layout 1             | `3630e616686c`  |
| 517    | Layout 1             | `3630e616686c`  |
| 510    | Layout 1             | `3630e616686c`  |
| 508    | Layout 1             | `3630e616686c`  |
| 504    | Layout 1             | `3630e616686c`  |
| 497    | Layout 1             | `3630e616686c`  |
| 491    | Layout 1             | `3630e616686c`  |
| 485    | Layout 1             | `3630e616686c`  |
| 478    | Layout 1             | `3630e616686c`  |
| 472    | Layout 1             | `3630e616686c`  |
| 466    | Layout 1             | `3630e616686c`  |
| 457    | Layout 1             | `3630e616686c`  |
| 452    | Layout 1             | `3630e616686c`  |
| 449    | Layout 1             | `3630e616686c`  |
| 435    | Layout 1             | `3630e616686c`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | The Imperial Steed's name (LOC type 6, `str_id1` = `imperial_steed_character_id`) |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so an `imperial_steed_character_id` without a row shows as plain text instead of a link |

Client 1784 ships the table as `servantmating.dbss` with the index
`servantmatingoffset.dbss` (Layout 1).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | 34 on client 3474                       |
| `+0x04` | Row[count] | rows  | `count` rows of 20 bytes, ending at EOF |

### Row (20 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u32  | key              | Band index; not in key order (36 to 32, 15 to 1, 31 to 16 on client 3474) |
| `+0x04` | u32  | key_dup          | Equals `key` on every row |
| `+0x08` | u16  | average_grade    | Lower end of the band: 0 to 1,150 in steps of 50 for keys 1 to 24, then 1,160 to 1,250 in steps of 10 (client 3474) |
| `+0x0A` | u16  | result_max_grade | 520 to 660 on client 3474 |
| `+0x0C` | u16  | result_min_grade | 460 to 615 on client 3474 |
| `+0x0E` | u16  | imperial_steed_character_id | 31594 on every row (client 3474), the Imperial Steed in `servant.bss` |
| `+0x10` | u32  | imperial_steed_rate | Millionths: 1,600 (0.16%) to 70,000 (7%), rising with `average_grade` (client 3474) |

## Layout 1

### `servantmating.dbss`

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | 24 on client 1784                       |
| `+0x04` | Row[count] | rows  | `count` rows of 14 bytes, ending at EOF |

### Row (14 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u32  | key              | 15 down to 1, then 24 down to 16 |
| `+0x04` | u32  | key_dup          | Equals `key` on every row |
| `+0x08` | u16  | average_grade    | |
| `+0x0A` | u16  | result_max_grade | |
| `+0x0C` | u16  | result_min_grade | |

### `servantmatingoffset.dbss`

| Offset  | Type              | Field   | Notes                           |
| ------- | ----------------- | ------- | ------------------------------- |
| `+0x00` | u32               | count   | Equals the `servantmating.dbss` count |
| `+0x04` | Offset Row[count] | entries | `count` entries of 12 bytes     |

### Offset Row (12 bytes)

| Offset  | Type | Field  | Notes                                               |
| ------- | ---- | ------ | --------------------------------------------------- |
| `+0x00` | u32  | key    | The row's `key`                                     |
| `+0x04` | u32  | offset | Where the row's `key_dup` starts, 4 bytes into the row |
| `+0x08` | u32  | size   | 10 on every entry: the row from `key_dup` on        |

## Breeding Results

Checked in game on client 3474 (2026-10-20) in the Horse Growth Info
Breed/Exchange Calculator with a tier 8 mare of grade 650 (9890) and a
stallion that puts the pair in band key 12 (`average_grade` 550,
`result_min_grade` 462, `result_max_grade` 535, `imperial_steed_rate`
3,200, the only band with that rate):

- The result grid holds 40 horses in pairs of 2.037% (mare) and 2.963%
  (stallion). `servant.bss` has exactly 40 breeding-result horses
  (`is_mating_result` 1) with a `grade` from 462 to 535: 20 tier 6 mares
  and 20 tier 6 stallions, at grades 490 and 520.
- Under the heading Imperial Steed it shows one mare at 0.32%: 3,200
  millionths, `imperial_steed_rate` of the band. 31594 is a mare
  (`is_male` 0); the calculators' horse list shows it with 31565 under the
  same heading.

The 40 pair chances add up to 100% without the Imperial Steed's 0.32%. How
the client splits mare and stallion chances (40.74% to 59.26% of each
pair here) is not in this file.

## Field Names

The names follow the `ServantMating_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (24 rows, `Index`, `AverageGrade`,
`ResultMinGrade`, `ResultMaxGrade`), matched value by value:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `Index` | `key` | 24 of 24 | 24 of 24 |
| `AverageGrade` | `average_grade` | 24 | 24 |
| `ResultMaxGrade` | `result_max_grade` | 24 | 10 |
| `ResultMinGrade` | `result_min_grade` | 24 | 8 |

The client 3474 misses are rebalances: band 15 (average 700) gives 468 to
600 against 435 to 600 on client 1784, and keys 1 to 11 all give 460 to 520
where client 1784 starts at 155 to 166. The 2016 `gc::ServantMatingStaticStatus`
holds `_key`, `_grade`, `_gradeByMin` and `_gradeByMax`; the file stores the
maximum before the minimum. The sheet has no column for
`imperial_steed_character_id` and `imperial_steed_rate`; their names come
from the in-game check in Breeding Results.
