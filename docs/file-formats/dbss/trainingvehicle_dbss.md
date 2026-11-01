# `trainingvehicle.dbss` Format

## Purpose

The training dummies of Black Spirit's Training: one row per character of
vehicle type `51` (`Training` in [`characterstatic.dbss`](characterstatic_dbss.md)),
with its grade. On client 3474 the file has 3 rows: Scarecrow (`31506`) and
Advanced Scarecrow (`31508`), both with AI script `TrainingMonster`, and
Sandbag (`31511`) with `TrainingMonsterHouse`. These three are every
character of vehicle type `51` on that client. Companion
`trainingvehicleoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records      | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | ------------ | --------- |
| 1      | 1346 and later | `trainingvehicle.dbss`       | 28    | 3 Row        | 8         |
| 1      | 1346 and later | `trainingvehicleoffset.dbss` | 34    | 3 Offset Row | 10        |

| Layout | File                         | Known         | Unknown    |
| ------ | ---------------------------- | ------------- | ---------- |
| 1      | `trainingvehicle.dbss`       | 28 B (100.0%) | 0 B (0.0%) |
| 1      | `trainingvehicleoffset.dbss` | 34 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `a694bec65470`  |
| 3482   | Layout 1             | `a694bec65470`  |
| 3474   | Layout 1             | `a694bec65470`  |
| 3473   | Layout 1             | `a694bec65470`  |
| 3464   | Layout 1             | `a694bec65470`  |
| 3458   | Layout 1             | `a694bec65470`  |
| 3454   | Layout 1             | `a694bec65470`  |
| 3444   | Layout 1             | `a694bec65470`  |
| 3435   | Layout 1             | `a694bec65470`  |
| 3426   | Layout 1             | `a694bec65470`  |
| 3418   | Layout 1             | `a694bec65470`  |
| 3412   | Layout 1             | `a694bec65470`  |
| 3402   | Layout 1             | `a694bec65470`  |
| 3396   | Layout 1             | `a694bec65470`  |
| 3387   | Layout 1             | `a694bec65470`  |
| 3381   | Layout 1             | `a694bec65470`  |
| 3373   | Layout 1             | `a694bec65470`  |
| 3364   | Layout 1             | `a694bec65470`  |
| 3356   | Layout 1             | `a694bec65470`  |
| 3349   | Layout 1             | `a694bec65470`  |
| 3342   | Layout 1             | `a694bec65470`  |
| 3335   | Layout 1             | `a694bec65470`  |
| 3326   | Layout 1             | `a694bec65470`  |
| 3321   | Layout 1             | `a694bec65470`  |
| 3314   | Layout 1             | `a694bec65470`  |
| 3303   | Layout 1             | `a694bec65470`  |
| 3302   | Layout 1             | `a694bec65470`  |
| 3293   | Layout 1             | `a694bec65470`  |
| 3283   | Layout 1             | `a694bec65470`  |
| 3275   | Layout 1             | `a694bec65470`  |
| 3267   | Layout 1             | `a694bec65470`  |
| 3258   | Layout 1             | `a694bec65470`  |
| 3251   | Layout 1             | `a694bec65470`  |
| 3242   | Layout 1             | `a694bec65470`  |
| 3235   | Layout 1             | `a694bec65470`  |
| 3229   | Layout 1             | `a694bec65470`  |
| 3212   | Layout 1             | `a694bec65470`  |
| 3203   | Layout 1             | `a694bec65470`  |
| 3193   | Layout 1             | `a694bec65470`  |
| 3186   | Layout 1             | `a694bec65470`  |
| 3177   | Layout 1             | `a694bec65470`  |
| 3169   | Layout 1             | `a694bec65470`  |
| 3158   | Layout 1             | `a694bec65470`  |
| 3151   | Layout 1             | `a694bec65470`  |
| 3144   | Layout 1             | `a694bec65470`  |
| 3133   | Layout 1             | `a694bec65470`  |
| 3125   | Layout 1             | `a694bec65470`  |
| 3118   | Layout 1             | `a694bec65470`  |
| 3111   | Layout 1             | `a694bec65470`  |
| 3103   | Layout 1             | `a694bec65470`  |
| 3095   | Layout 1             | `a694bec65470`  |
| 3086   | Layout 1             | `a694bec65470`  |
| 3072   | Layout 1             | `a694bec65470`  |
| 3062   | Layout 1             | `a694bec65470`  |
| 3052   | Layout 1             | `a694bec65470`  |
| 3045   | Layout 1             | `a694bec65470`  |
| 3037   | Layout 1             | `a694bec65470`  |
| 3030   | Layout 1             | `a694bec65470`  |
| 3021   | Layout 1             | `a694bec65470`  |
| 3012   | Layout 1             | `a694bec65470`  |
| 3002   | Layout 1             | `a694bec65470`  |
| 2995   | Layout 1             | `a694bec65470`  |
| 2987   | Layout 1             | `a694bec65470`  |
| 2978   | Layout 1             | `a694bec65470`  |
| 2970   | Layout 1             | `a694bec65470`  |
| 2959   | Layout 1             | `a694bec65470`  |
| 2951   | Layout 1             | `a694bec65470`  |
| 2942   | Layout 1             | `a694bec65470`  |
| 2935   | Layout 1             | `a694bec65470`  |
| 2932   | Layout 1             | `a694bec65470`  |
| 2923   | Layout 1             | `a694bec65470`  |
| 2919   | Layout 1             | `a694bec65470`  |
| 2907   | Layout 1             | `a694bec65470`  |
| 2900   | Layout 1             | `a694bec65470`  |
| 2891   | Layout 1             | `a694bec65470`  |
| 2882   | Layout 1             | `a694bec65470`  |
| 2872   | Layout 1             | `a694bec65470`  |
| 2863   | Layout 1             | `a694bec65470`  |
| 2855   | Layout 1             | `a694bec65470`  |
| 2849   | Layout 1             | `a694bec65470`  |
| 2844   | Layout 1             | `a694bec65470`  |
| 2834   | Layout 1             | `a694bec65470`  |
| 2825   | Layout 1             | `a694bec65470`  |
| 2819   | Layout 1             | `a694bec65470`  |
| 2811   | Layout 1             | `a694bec65470`  |
| 2803   | Layout 1             | `a694bec65470`  |
| 2794   | Layout 1             | `a694bec65470`  |
| 2783   | Layout 1             | `a694bec65470`  |
| 2774   | Layout 1             | `a694bec65470`  |
| 2765   | Layout 1             | `a694bec65470`  |
| 2756   | Layout 1             | `a694bec65470`  |
| 2750   | Layout 1             | `a694bec65470`  |
| 2743   | Layout 1             | `a694bec65470`  |
| 2736   | Layout 1             | `a694bec65470`  |
| 2726   | Layout 1             | `a694bec65470`  |
| 2717   | Layout 1             | `a694bec65470`  |
| 2709   | Layout 1             | `a694bec65470`  |
| 2703   | Layout 1             | `a694bec65470`  |
| 2695   | Layout 1             | `a694bec65470`  |
| 2684   | Layout 1             | `a694bec65470`  |
| 2672   | Layout 1             | `a694bec65470`  |
| 2665   | Layout 1             | `a694bec65470`  |
| 2657   | Layout 1             | `a694bec65470`  |
| 2649   | Layout 1             | `a694bec65470`  |
| 2644   | Layout 1             | `a694bec65470`  |
| 2637   | Layout 1             | `a694bec65470`  |
| 2629   | Layout 1             | `a694bec65470`  |
| 2619   | Layout 1             | `a694bec65470`  |
| 2612   | Layout 1             | `a694bec65470`  |
| 2606   | Layout 1             | `a694bec65470`  |
| 2602   | Layout 1             | `a694bec65470`  |
| 2601   | Layout 1             | `a694bec65470`  |
| 2592   | Layout 1             | `a694bec65470`  |
| 2583   | Layout 1             | `a694bec65470`  |
| 2575   | Layout 1             | `a694bec65470`  |
| 2567   | Layout 1             | `a694bec65470`  |
| 2560   | Layout 1             | `a694bec65470`  |
| 2553   | Layout 1             | `a694bec65470`  |
| 2545   | Layout 1             | `a694bec65470`  |
| 2538   | Layout 1             | `a694bec65470`  |
| 2529   | Layout 1             | `a694bec65470`  |
| 2519   | Layout 1             | `a694bec65470`  |
| 2513   | Layout 1             | `a694bec65470`  |
| 2510   | Layout 1             | `a694bec65470`  |
| 2507   | Layout 1             | `a694bec65470`  |
| 2503   | Layout 1             | `a694bec65470`  |
| 2498   | Layout 1             | `a694bec65470`  |
| 2492   | Layout 1             | `a694bec65470`  |
| 2487   | Layout 1             | `a694bec65470`  |
| 2480   | Layout 1             | `a694bec65470`  |
| 2474   | Layout 1             | `a694bec65470`  |
| 2468   | Layout 1             | `a694bec65470`  |
| 2460   | Layout 1             | `a694bec65470`  |
| 2453   | Layout 1             | `a694bec65470`  |
| 2444   | Layout 1             | `a694bec65470`  |
| 2438   | Layout 1             | `a694bec65470`  |
| 2434   | Layout 1             | `a694bec65470`  |
| 2429   | Layout 1             | `a694bec65470`  |
| 2421   | Layout 1             | `a694bec65470`  |
| 2414   | Layout 1             | `a694bec65470`  |
| 2407   | Layout 1             | `a694bec65470`  |
| 2401   | Layout 1             | `a694bec65470`  |
| 2397   | Layout 1             | `a694bec65470`  |
| 2393   | Layout 1             | `a694bec65470`  |
| 2384   | Layout 1             | `a694bec65470`  |
| 2378   | Layout 1             | `a694bec65470`  |
| 2372   | Layout 1             | `a694bec65470`  |
| 2358   | Layout 1             | `a694bec65470`  |
| 2352   | Layout 1             | `a694bec65470`  |
| 2347   | Layout 1             | `a694bec65470`  |
| 2343   | Layout 1             | `a694bec65470`  |
| 2335   | Layout 1             | `a694bec65470`  |
| 2327   | Layout 1             | `a694bec65470`  |
| 2324   | Layout 1             | `a694bec65470`  |
| 2319   | Layout 1             | `a694bec65470`  |
| 2313   | Layout 1             | `a694bec65470`  |
| 2308   | Layout 1             | `a694bec65470`  |
| 2302   | Layout 1             | `a694bec65470`  |
| 2295   | Layout 1             | `a694bec65470`  |
| 2290   | Layout 1             | `a694bec65470`  |
| 2284   | Layout 1             | `a694bec65470`  |
| 2276   | Layout 1             | `a694bec65470`  |
| 2269   | Layout 1             | `a694bec65470`  |
| 2259   | Layout 1             | `a694bec65470`  |
| 2250   | Layout 1             | `a694bec65470`  |
| 2243   | Layout 1             | `a694bec65470`  |
| 2235   | Layout 1             | `a694bec65470`  |
| 2229   | Layout 1             | `a694bec65470`  |
| 2224   | Layout 1             | `a694bec65470`  |
| 2218   | Layout 1             | `a694bec65470`  |
| 2215   | Layout 1             | `a694bec65470`  |
| 2207   | Layout 1             | `a694bec65470`  |
| 2203   | Layout 1             | `a694bec65470`  |
| 2196   | Layout 1             | `a694bec65470`  |
| 2192   | Layout 1             | `a694bec65470`  |
| 2189   | Layout 1             | `a694bec65470`  |
| 2183   | Layout 1             | `a694bec65470`  |
| 2179   | Layout 1             | `a694bec65470`  |
| 2171   | Layout 1             | `a694bec65470`  |
| 2163   | Layout 1             | `a694bec65470`  |
| 2156   | Layout 1             | `a694bec65470`  |
| 2151   | Layout 1             | `a694bec65470`  |
| 2147   | Layout 1             | `a694bec65470`  |
| 2142   | Layout 1             | `a694bec65470`  |
| 2138   | Layout 1             | `a694bec65470`  |
| 2134   | Layout 1             | `a694bec65470`  |
| 2130   | Layout 1             | `a694bec65470`  |
| 2122   | Layout 1             | `a694bec65470`  |
| 2107   | Layout 1             | `a694bec65470`  |
| 2098   | Layout 1             | `a694bec65470`  |
| 2089   | Layout 1             | `a694bec65470`  |
| 2081   | Layout 1             | `a694bec65470`  |
| 2073   | Layout 1             | `a694bec65470`  |
| 2067   | Layout 1             | `a694bec65470`  |
| 2063   | Layout 1             | `a694bec65470`  |
| 2059   | Layout 1             | `a694bec65470`  |
| 2052   | Layout 1             | `a694bec65470`  |
| 2044   | Layout 1             | `a694bec65470`  |
| 2039   | Layout 1             | `a694bec65470`  |
| 2032   | Layout 1             | `a694bec65470`  |
| 2025   | Layout 1             | `a694bec65470`  |
| 2011   | Layout 1             | `a694bec65470`  |
| 2005   | Layout 1             | `a694bec65470`  |
| 2000   | Layout 1             | `a694bec65470`  |
| 1996   | Layout 1             | `a694bec65470`  |
| 1991   | Layout 1             | `a694bec65470`  |
| 1985   | Layout 1             | `a694bec65470`  |
| 1980   | Layout 1             | `a694bec65470`  |
| 1969   | Layout 1             | `a694bec65470`  |
| 1964   | Layout 1             | `a694bec65470`  |
| 1958   | Layout 1             | `a694bec65470`  |
| 1950   | Layout 1             | `a694bec65470`  |
| 1945   | Layout 1             | `a694bec65470`  |
| 1937   | Layout 1             | `a694bec65470`  |
| 1933   | Layout 1             | `a694bec65470`  |
| 1927   | Layout 1             | `a694bec65470`  |
| 1921   | Layout 1             | `a694bec65470`  |
| 1914   | Layout 1             | `a694bec65470`  |
| 1908   | Layout 1             | `a694bec65470`  |
| 1897   | Layout 1             | `a694bec65470`  |
| 1892   | Layout 1             | `a694bec65470`  |
| 1886   | Layout 1             | `a694bec65470`  |
| 1881   | Layout 1             | `a694bec65470`  |
| 1871   | Layout 1             | `a694bec65470`  |
| 1866   | Layout 1             | `a694bec65470`  |
| 1862   | Layout 1             | `a694bec65470`  |
| 1854   | Layout 1             | `a694bec65470`  |
| 1846   | Layout 1             | `a694bec65470`  |
| 1838   | Layout 1             | `a694bec65470`  |
| 1832   | Layout 1             | `a694bec65470`  |
| 1826   | Layout 1             | `a694bec65470`  |
| 1822   | Layout 1             | `a694bec65470`  |
| 1818   | Layout 1             | `a694bec65470`  |
| 1804   | Layout 1             | `a694bec65470`  |
| 1794   | Layout 1             | `a694bec65470`  |
| 1790   | Layout 1             | `a694bec65470`  |
| 1784   | Layout 1             | `a694bec65470`  |
| 1774   | Layout 1             | `a694bec65470`  |
| 1771   | Layout 1             | `a694bec65470`  |
| 1762   | Layout 1             | `a694bec65470`  |
| 1759   | Layout 1             | `a694bec65470`  |
| 1754   | Layout 1             | `a694bec65470`  |
| 1749   | Layout 1             | `a694bec65470`  |
| 1743   | Layout 1             | `a694bec65470`  |
| 1737   | Layout 1             | `a694bec65470`  |
| 1731   | Layout 1             | `a694bec65470`  |
| 1725   | Layout 1             | `a694bec65470`  |
| 1717   | Layout 1             | `a694bec65470`  |
| 1710   | Layout 1             | `a694bec65470`  |
| 1704   | Layout 1             | `a694bec65470`  |
| 1698   | Layout 1             | `a694bec65470`  |
| 1690   | Layout 1             | `a694bec65470`  |
| 1685   | Layout 1             | `a694bec65470`  |
| 1680   | Layout 1             | `a694bec65470`  |
| 1674   | Layout 1             | `a694bec65470`  |
| 1668   | Layout 1             | `a694bec65470`  |
| 1659   | Layout 1             | `a694bec65470`  |
| 1649   | Layout 1             | `a694bec65470`  |
| 1642   | Layout 1             | `a694bec65470`  |
| 1636   | Layout 1             | `a694bec65470`  |
| 1628   | Layout 1             | `a694bec65470`  |
| 1622   | Layout 1             | `a694bec65470`  |
| 1614   | Layout 1             | `a694bec65470`  |
| 1608   | Layout 1             | `a694bec65470`  |
| 1602   | Layout 1             | `a694bec65470`  |
| 1598   | Layout 1             | `a694bec65470`  |
| 1594   | Layout 1             | `a694bec65470`  |
| 1590   | Layout 1             | `a694bec65470`  |
| 1587   | Layout 1             | `a694bec65470`  |
| 1584   | Layout 1             | `a694bec65470`  |
| 1579   | Layout 1             | `a694bec65470`  |
| 1572   | Layout 1             | `a694bec65470`  |
| 1565   | Layout 1             | `a694bec65470`  |
| 1559   | Layout 1             | `a694bec65470`  |
| 1554   | Layout 1             | `a694bec65470`  |
| 1547   | Layout 1             | `a694bec65470`  |
| 1537   | Layout 1             | `a694bec65470`  |
| 1529   | Layout 1             | `a694bec65470`  |
| 1524   | Layout 1             | `a694bec65470`  |
| 1519   | Layout 1             | `a694bec65470`  |
| 1509   | Layout 1             | `a694bec65470`  |
| 1506   | Layout 1             | `a694bec65470`  |
| 1504   | Layout 1             | `a694bec65470`  |
| 1500   | Layout 1             | `a694bec65470`  |
| 1493   | Layout 1             | `a694bec65470`  |
| 1489   | Layout 1             | `a694bec65470`  |
| 1485   | Layout 1             | `a694bec65470`  |
| 1481   | Layout 1             | `a694bec65470`  |
| 1474   | Layout 1             | `a694bec65470`  |
| 1466   | Layout 1             | `a694bec65470`  |
| 1462   | Layout 1             | `a694bec65470`  |
| 1459   | Layout 1             | `a694bec65470`  |
| 1453   | Layout 1             | `a694bec65470`  |
| 1450   | Layout 1             | `a694bec65470`  |
| 1445   | Layout 1             | `a694bec65470`  |
| 1439   | Layout 1             | `a694bec65470`  |
| 1433   | Layout 1             | `a694bec65470`  |
| 1430   | Layout 1             | `a694bec65470`  |
| 1426   | Layout 1             | `a694bec65470`  |
| 1421   | Layout 1             | `a694bec65470`  |
| 1417   | Layout 1             | `a694bec65470`  |
| 1416   | Layout 1             | `a694bec65470`  |
| 1409   | Layout 1             | `a694bec65470`  |
| 1405   | Layout 1             | `a694bec65470`  |
| 1401   | Layout 1             | `a694bec65470`  |
| 1396   | Layout 1             | `a694bec65470`  |
| 1391   | Layout 1             | `a694bec65470`  |
| 1390   | Layout 1             | `a694bec65470`  |
| 1386   | Layout 1             | `a694bec65470`  |
| 1381   | Layout 1             | `a694bec65470`  |
| 1379   | Layout 1             | `a694bec65470`  |
| 1372   | Layout 1             | `a694bec65470`  |
| 1366   | Layout 1             | `a694bec65470`  |
| 1364   | Layout 1             | `a694bec65470`  |
| 1363   | Layout 1             | `a694bec65470`  |
| 1360   | Layout 1             | `a694bec65470`  |
| 1358   | Layout 1             | `a694bec65470`  |
| 1355   | Layout 1             | `a694bec65470`  |
| 1351   | Layout 1             | `a694bec65470`  |
| 1348   | Layout 1             | `a694bec65470`  |
| 1346   | Layout 1             | `a694bec65470`  |
| 1341   | No documented layout | `a694bec65470`  |
| 1340   | No documented layout | `a694bec65470`  |
| 1338   | No documented layout | `a694bec65470`  |
| 1335   | No documented layout | `a694bec65470`  |
| 1333   | No documented layout | `a694bec65470`  |
| 1329   | No documented layout | `a694bec65470`  |
| 1327   | No documented layout | `a694bec65470`  |
| 1324   | No documented layout | `a694bec65470`  |
| 1321   | No documented layout | `a694bec65470`  |
| 1319   | No documented layout | `a694bec65470`  |
| 1318   | No documented layout | `a694bec65470`  |
| 1316   | No documented layout | `a694bec65470`  |
| 1313   | No documented layout | `a694bec65470`  |
| 1311   | No documented layout | `a694bec65470`  |
| 1309   | No documented layout | `a694bec65470`  |
| 1304   | No documented layout | `a694bec65470`  |
| 1292   | No documented layout | `a694bec65470`  |
| 1286   | No documented layout | `a694bec65470`  |
| 1280   | No documented layout | `a694bec65470`  |
| 1276   | No file              | `a694bec65470`  |
| 1267   | No file              | `a694bec65470`  |
| 1261   | No file              | `a694bec65470`  |
| 1256   | No file              | `a694bec65470`  |
| 1250   | No file              | `a694bec65470`  |
| 1246   | No file              | `a694bec65470`  |
| 1239   | No file              | `a694bec65470`  |
| 1230   | No file              | `a694bec65470`  |
| 1226   | No file              | `a694bec65470`  |
| 1220   | No file              | `a694bec65470`  |
| 1217   | No file              | `a694bec65470`  |
| 1211   | No file              | `a694bec65470`  |
| 1210   | No file              | `a694bec65470`  |
| 1208   | No file              | `a694bec65470`  |
| 1203   | No file              | `a694bec65470`  |
| 1197   | No file              | `a694bec65470`  |
| 1194   | No file              | `a694bec65470`  |
| 1192   | No file              | `a694bec65470`  |
| 1187   | No file              | `a694bec65470`  |
| 1183   | No file              | `a694bec65470`  |
| 1177   | No file              | `a694bec65470`  |
| 1173   | No file              | `a694bec65470`  |
| 1167   | No file              | `a694bec65470`  |
| 1164   | No file              | `a694bec65470`  |
| 1156   | No file              | `a694bec65470`  |
| 1149   | No file              | `a694bec65470`  |
| 1144   | No file              | `a694bec65470`  |
| 1137   | No file              | `a694bec65470`  |
| 1132   | No file              | `a694bec65470`  |
| 1127   | No file              | `a694bec65470`  |
| 1122   | No file              | `a694bec65470`  |
| 1118   | No file              | `a694bec65470`  |
| 1114   | No file              | `a694bec65470`  |
| 1109   | No file              | `a694bec65470`  |
| 1102   | No file              | `a694bec65470`  |
| 1096   | No file              | `a694bec65470`  |
| 1088   | No file              | `a694bec65470`  |
| 1081   | No file              | `a694bec65470`  |
| 1076   | No file              | `a694bec65470`  |
| 1069   | No file              | `a694bec65470`  |
| 1064   | No file              | `a694bec65470`  |
| 1058   | No file              | `a694bec65470`  |
| 1051   | No file              | `a694bec65470`  |
| 1044   | No file              | `a694bec65470`  |
| 1036   | No file              | `a694bec65470`  |
| 1026   | No file              | `a694bec65470`  |
| 1016   | No file              | `a694bec65470`  |
| 1009   | No file              | `a694bec65470`  |
| 1005   | No file              | `a694bec65470`  |
| 1000   | No file              | `a694bec65470`  |
| 998    | No file              | `a694bec65470`  |
| 990    | No file              | `a694bec65470`  |
| 979    | No file              | `a694bec65470`  |
| 972    | No file              | `a694bec65470`  |
| 963    | No file              | `a694bec65470`  |
| 955    | No file              | `a694bec65470`  |
| 946    | No file              | `a694bec65470`  |
| 938    | No file              | `a694bec65470`  |
| 927    | No file              | `a694bec65470`  |
| 911    | No file              | `a694bec65470`  |
| 904    | No file              | `a694bec65470`  |
| 899    | No file              | `a694bec65470`  |
| 894    | No file              | `a694bec65470`  |
| 885    | No file              | `a694bec65470`  |
| 879    | No file              | `a694bec65470`  |
| 872    | No file              | `a694bec65470`  |
| 864    | No file              | `a694bec65470`  |
| 855    | No file              | `a694bec65470`  |
| 853    | No file              | `a694bec65470`  |
| 845    | No file              | `a694bec65470`  |
| 837    | No file              | `a694bec65470`  |
| 829    | No file              | `a694bec65470`  |
| 822    | No file              | `a694bec65470`  |
| 814    | No file              | `a694bec65470`  |
| 805    | No file              | `a694bec65470`  |
| 794    | No file              | `a694bec65470`  |
| 787    | No file              | `a694bec65470`  |
| 780    | No file              | `a694bec65470`  |
| 771    | No file              | `a694bec65470`  |
| 760    | No file              | `a694bec65470`  |
| 748    | No file              | `a694bec65470`  |
| 741    | No file              | `a694bec65470`  |
| 736    | No file              | `a694bec65470`  |
| 731    | No file              | `a694bec65470`  |
| 723    | No file              | `a694bec65470`  |
| 711    | No file              | `a694bec65470`  |
| 707    | No file              | `a694bec65470`  |
| 697    | No file              | `a694bec65470`  |
| 689    | No file              | `a694bec65470`  |
| 683    | No file              | `a694bec65470`  |
| 678    | No file              | `a694bec65470`  |
| 670    | No file              | `a694bec65470`  |
| 661    | No file              | `a694bec65470`  |
| 656    | No file              | `a694bec65470`  |
| 652    | No file              | `a694bec65470`  |
| 643    | No file              | `a694bec65470`  |
| 637    | No file              | `a694bec65470`  |
| 630    | No file              | `a694bec65470`  |
| 627    | No file              | `a694bec65470`  |
| 621    | No file              | `a694bec65470`  |
| 617    | No file              | `a694bec65470`  |
| 615    | No file              | `a694bec65470`  |
| 606    | No file              | `a694bec65470`  |
| 599    | No file              | `a694bec65470`  |
| 592    | No file              | `a694bec65470`  |
| 586    | No file              | `a694bec65470`  |
| 577    | No file              | `a694bec65470`  |
| 569    | No file              | `a694bec65470`  |
| 561    | No file              | `a694bec65470`  |
| 554    | No file              | `a694bec65470`  |
| 542    | No file              | `a694bec65470`  |
| 532    | No file              | `a694bec65470`  |
| 531    | No file              | `a694bec65470`  |
| 526    | No file              | `a694bec65470`  |
| 521    | No file              | `a694bec65470`  |
| 517    | No file              | `a694bec65470`  |
| 510    | No file              | `a694bec65470`  |
| 508    | No file              | `a694bec65470`  |
| 504    | No file              | `a694bec65470`  |
| 497    | No file              | `a694bec65470`  |
| 491    | No file              | `a694bec65470`  |
| 485    | No file              | `a694bec65470`  |
| 478    | No file              | `a694bec65470`  |
| 472    | No file              | `a694bec65470`  |
| 466    | No file              | `a694bec65470`  |
| 457    | No file              | `a694bec65470`  |
| 452    | No file              | `a694bec65470`  |
| 449    | No file              | `a694bec65470`  |
| 435    | No file              | `a694bec65470`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                 |
| ---------------------------- | -------- | -------------------------------------------------------------------- |
| `trainingvehicleoffset.dbss` | Optional | `character_key -> (offset, size)` of every row; the main file can be walked without it |
| `characterstaticoffset.dbss` | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key link |
| `languagedata_en.loc`        | Optional | Character names (LOC type 6)                                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (8 bytes)

| Offset  | Type | Field             | Notes                                                                 |
| ------- | ---- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key     | Training dummy character; unique, and every key has a `characterstatic.dbss` row (client 3474) |
| `+0x02` | u16  | character_key_dup | Equal to `character_key` in every row; the offset file points here    |
| `+0x04` | i32  | grade             | `1` for Scarecrow and Sandbag, `2` for Advanced Scarecrow (clients 1784 and 3474) |

### `trainingvehicleoffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `trainingvehicle.dbss` count     |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                    |
| ------- | ---- | ------------- | -------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                              |
| `+0x02` | u32  | offset        | Row start + 2, at `character_key_dup`                    |
| `+0x06` | u32  | size          | The row without its leading `character_key`: always `6`  |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in main file order.

## Field Names

The names follow the `TrainingVehicle_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 and the same sheet in its
`datasheet_characterdatatable.xlsm`, columns `^Index`, `Grade`, `%ExpRate`
and `ContentsGroupKey`. The sheet has 5 rows; the 3 with `ContentsGroupKey`
`0` match the file by key and `grade` on clients 1784 and 3474 (3 of 3). The
other 2, Cart (`31551`) and Rowboat (`31552`) with contents group `1520`, are
missing from the file on both clients and have no `characterstatic.dbss` row
on client 3474. `%ExpRate` is a server-only column and `ContentsGroupKey` is
not in the file either.

The client 1784 server dump names the static status
`gc::TrainingVehicleStaticStatus`, keyed by a `KeyType<unsigned short>`, with
the members `_key`, `_grade` and `_expRate` (from its check messages). Its
sheet loader reads `Grade` with `ReadCellInt` into a 4-byte member at `+0x04`,
after the u16 key, and `ExpRate` as a float at `+0x08`. The file holds the key
and the 4-byte grade, so `grade` is an `i32`. The `TrainingVehicle_Table` of a
private server on client 519 has the same 3 rows with the same grades.

## Notes

- Client 1784 has the same 28-byte file, byte for byte.
- The file is not sorted by key: Sandbag (`31511`) comes first, Scarecrow
  (`31506`) last.
- The description of Book of Training - Skill (3 Days) (item `17999`, client
  3474) says it lets a player train "with the training scarecrows which can be
  found in any town" for Skill EXP, "when using Black Spirit's Training". Item
  `18815` on client 3474 is Black Spirit's Training Sandbag Installment.

## Open Questions

### What Grade Changes

Advanced Scarecrow has `grade` `2`, the other two `1`. No client Lua reads the
table: none of the 3,073 `.luac` files of client 3474 holds the text
`TrainingVehicle`. The AI scripts `TrainingMonster` and `TrainingMonsterHouse` do not
use a grade. Whether the grade scales the training EXP on the server, picks
which Books of Training work, or something else, is open. In the client 1784
sheet the server-only `%ExpRate` is `1.5` on the grade `2` row and `1` on the
others, but those values come from a private server and are not evidence.
