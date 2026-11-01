# `fitnesslevel.dbss` Format

## Purpose

Level tables of the three fitness stats in the character window: Breath, Strength and Health. Each row gives the EXP to the next level and the total bonus the fitness stat grants at that level (max Stamina for Breath, weight limit for Strength, max HP and max MP/WP/SP for Health). Companion `fitnessleveloffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes | Records                        | Row bytes |
| ------ | -------------- | ------------------------- | ----- | ------------------------------ | --------- |
| 1      | 1276 and later | `fitnesslevel.dbss`       | 4,453 | 153 Level Row, 3 Block         | 29        |
| 1      | 1276 and later | `fitnessleveloffset.dbss` | 1,848 | 153 Offset Row, 3 Offset Block | 12        |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `fitnesslevel.dbss`       | 4,453 B (100.0%) | 0 B (0.0%) |
| 1      | `fitnessleveloffset.dbss` | 1,848 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `cae0025a4383`  |
| 3482   | Layout 1 | `cae0025a4383`  |
| 3474   | Layout 1 | `cae0025a4383`  |
| 3473   | Layout 1 | `cae0025a4383`  |
| 3464   | Layout 1 | `cae0025a4383`  |
| 3458   | Layout 1 | `cae0025a4383`  |
| 3454   | Layout 1 | `cae0025a4383`  |
| 3444   | Layout 1 | `cae0025a4383`  |
| 3435   | Layout 1 | `cae0025a4383`  |
| 3426   | Layout 1 | `cae0025a4383`  |
| 3418   | Layout 1 | `cae0025a4383`  |
| 3412   | Layout 1 | `cae0025a4383`  |
| 3402   | Layout 1 | `cae0025a4383`  |
| 3396   | Layout 1 | `cae0025a4383`  |
| 3387   | Layout 1 | `cae0025a4383`  |
| 3381   | Layout 1 | `cae0025a4383`  |
| 3373   | Layout 1 | `cae0025a4383`  |
| 3364   | Layout 1 | `cae0025a4383`  |
| 3356   | Layout 1 | `cae0025a4383`  |
| 3349   | Layout 1 | `cae0025a4383`  |
| 3342   | Layout 1 | `cae0025a4383`  |
| 3335   | Layout 1 | `cae0025a4383`  |
| 3326   | Layout 1 | `cae0025a4383`  |
| 3321   | Layout 1 | `cae0025a4383`  |
| 3314   | Layout 1 | `cae0025a4383`  |
| 3303   | Layout 1 | `cae0025a4383`  |
| 3302   | Layout 1 | `cae0025a4383`  |
| 3293   | Layout 1 | `cae0025a4383`  |
| 3283   | Layout 1 | `cae0025a4383`  |
| 3275   | Layout 1 | `cae0025a4383`  |
| 3267   | Layout 1 | `cae0025a4383`  |
| 3258   | Layout 1 | `cae0025a4383`  |
| 3251   | Layout 1 | `cae0025a4383`  |
| 3242   | Layout 1 | `cae0025a4383`  |
| 3235   | Layout 1 | `cae0025a4383`  |
| 3229   | Layout 1 | `cae0025a4383`  |
| 3212   | Layout 1 | `cae0025a4383`  |
| 3203   | Layout 1 | `cae0025a4383`  |
| 3193   | Layout 1 | `cae0025a4383`  |
| 3186   | Layout 1 | `cae0025a4383`  |
| 3177   | Layout 1 | `cae0025a4383`  |
| 3169   | Layout 1 | `cae0025a4383`  |
| 3158   | Layout 1 | `cae0025a4383`  |
| 3151   | Layout 1 | `cae0025a4383`  |
| 3144   | Layout 1 | `cae0025a4383`  |
| 3133   | Layout 1 | `cae0025a4383`  |
| 3125   | Layout 1 | `cae0025a4383`  |
| 3118   | Layout 1 | `cae0025a4383`  |
| 3111   | Layout 1 | `cae0025a4383`  |
| 3103   | Layout 1 | `cae0025a4383`  |
| 3095   | Layout 1 | `cae0025a4383`  |
| 3086   | Layout 1 | `cae0025a4383`  |
| 3072   | Layout 1 | `cae0025a4383`  |
| 3062   | Layout 1 | `cae0025a4383`  |
| 3052   | Layout 1 | `cae0025a4383`  |
| 3045   | Layout 1 | `cae0025a4383`  |
| 3037   | Layout 1 | `cae0025a4383`  |
| 3030   | Layout 1 | `cae0025a4383`  |
| 3021   | Layout 1 | `cae0025a4383`  |
| 3012   | Layout 1 | `cae0025a4383`  |
| 3002   | Layout 1 | `cae0025a4383`  |
| 2995   | Layout 1 | `cae0025a4383`  |
| 2987   | Layout 1 | `cae0025a4383`  |
| 2978   | Layout 1 | `cae0025a4383`  |
| 2970   | Layout 1 | `cae0025a4383`  |
| 2959   | Layout 1 | `cae0025a4383`  |
| 2951   | Layout 1 | `cae0025a4383`  |
| 2942   | Layout 1 | `cae0025a4383`  |
| 2935   | Layout 1 | `cae0025a4383`  |
| 2932   | Layout 1 | `cae0025a4383`  |
| 2923   | Layout 1 | `cae0025a4383`  |
| 2919   | Layout 1 | `cae0025a4383`  |
| 2907   | Layout 1 | `cae0025a4383`  |
| 2900   | Layout 1 | `cae0025a4383`  |
| 2891   | Layout 1 | `cae0025a4383`  |
| 2882   | Layout 1 | `cae0025a4383`  |
| 2872   | Layout 1 | `cae0025a4383`  |
| 2863   | Layout 1 | `cae0025a4383`  |
| 2855   | Layout 1 | `cae0025a4383`  |
| 2849   | Layout 1 | `cae0025a4383`  |
| 2844   | Layout 1 | `cae0025a4383`  |
| 2834   | Layout 1 | `cae0025a4383`  |
| 2825   | Layout 1 | `cae0025a4383`  |
| 2819   | Layout 1 | `cae0025a4383`  |
| 2811   | Layout 1 | `cae0025a4383`  |
| 2803   | Layout 1 | `cae0025a4383`  |
| 2794   | Layout 1 | `cae0025a4383`  |
| 2783   | Layout 1 | `cae0025a4383`  |
| 2774   | Layout 1 | `cae0025a4383`  |
| 2765   | Layout 1 | `cae0025a4383`  |
| 2756   | Layout 1 | `cae0025a4383`  |
| 2750   | Layout 1 | `cae0025a4383`  |
| 2743   | Layout 1 | `cae0025a4383`  |
| 2736   | Layout 1 | `cae0025a4383`  |
| 2726   | Layout 1 | `cae0025a4383`  |
| 2717   | Layout 1 | `cae0025a4383`  |
| 2709   | Layout 1 | `cae0025a4383`  |
| 2703   | Layout 1 | `cae0025a4383`  |
| 2695   | Layout 1 | `cae0025a4383`  |
| 2684   | Layout 1 | `cae0025a4383`  |
| 2672   | Layout 1 | `cae0025a4383`  |
| 2665   | Layout 1 | `cae0025a4383`  |
| 2657   | Layout 1 | `cae0025a4383`  |
| 2649   | Layout 1 | `cae0025a4383`  |
| 2644   | Layout 1 | `cae0025a4383`  |
| 2637   | Layout 1 | `cae0025a4383`  |
| 2629   | Layout 1 | `cae0025a4383`  |
| 2619   | Layout 1 | `cae0025a4383`  |
| 2612   | Layout 1 | `cae0025a4383`  |
| 2606   | Layout 1 | `cae0025a4383`  |
| 2602   | Layout 1 | `cae0025a4383`  |
| 2601   | Layout 1 | `cae0025a4383`  |
| 2592   | Layout 1 | `cae0025a4383`  |
| 2583   | Layout 1 | `cae0025a4383`  |
| 2575   | Layout 1 | `cae0025a4383`  |
| 2567   | Layout 1 | `cae0025a4383`  |
| 2560   | Layout 1 | `cae0025a4383`  |
| 2553   | Layout 1 | `cae0025a4383`  |
| 2545   | Layout 1 | `cae0025a4383`  |
| 2538   | Layout 1 | `cae0025a4383`  |
| 2529   | Layout 1 | `cae0025a4383`  |
| 2519   | Layout 1 | `cae0025a4383`  |
| 2513   | Layout 1 | `cae0025a4383`  |
| 2510   | Layout 1 | `cae0025a4383`  |
| 2507   | Layout 1 | `cae0025a4383`  |
| 2503   | Layout 1 | `cae0025a4383`  |
| 2498   | Layout 1 | `cae0025a4383`  |
| 2492   | Layout 1 | `cae0025a4383`  |
| 2487   | Layout 1 | `cae0025a4383`  |
| 2480   | Layout 1 | `cae0025a4383`  |
| 2474   | Layout 1 | `cae0025a4383`  |
| 2468   | Layout 1 | `cae0025a4383`  |
| 2460   | Layout 1 | `cae0025a4383`  |
| 2453   | Layout 1 | `cae0025a4383`  |
| 2444   | Layout 1 | `cae0025a4383`  |
| 2438   | Layout 1 | `cae0025a4383`  |
| 2434   | Layout 1 | `cae0025a4383`  |
| 2429   | Layout 1 | `cae0025a4383`  |
| 2421   | Layout 1 | `cae0025a4383`  |
| 2414   | Layout 1 | `cae0025a4383`  |
| 2407   | Layout 1 | `cae0025a4383`  |
| 2401   | Layout 1 | `cae0025a4383`  |
| 2397   | Layout 1 | `cae0025a4383`  |
| 2393   | Layout 1 | `cae0025a4383`  |
| 2384   | Layout 1 | `cae0025a4383`  |
| 2378   | Layout 1 | `cae0025a4383`  |
| 2372   | Layout 1 | `cae0025a4383`  |
| 2358   | Layout 1 | `cae0025a4383`  |
| 2352   | Layout 1 | `cae0025a4383`  |
| 2347   | Layout 1 | `cae0025a4383`  |
| 2343   | Layout 1 | `cae0025a4383`  |
| 2335   | Layout 1 | `cae0025a4383`  |
| 2327   | Layout 1 | `cae0025a4383`  |
| 2324   | Layout 1 | `cae0025a4383`  |
| 2319   | Layout 1 | `cae0025a4383`  |
| 2313   | Layout 1 | `cae0025a4383`  |
| 2308   | Layout 1 | `cae0025a4383`  |
| 2302   | Layout 1 | `cae0025a4383`  |
| 2295   | Layout 1 | `cae0025a4383`  |
| 2290   | Layout 1 | `cae0025a4383`  |
| 2284   | Layout 1 | `cae0025a4383`  |
| 2276   | Layout 1 | `cae0025a4383`  |
| 2269   | Layout 1 | `cae0025a4383`  |
| 2259   | Layout 1 | `cae0025a4383`  |
| 2250   | Layout 1 | `cae0025a4383`  |
| 2243   | Layout 1 | `cae0025a4383`  |
| 2235   | Layout 1 | `cae0025a4383`  |
| 2229   | Layout 1 | `cae0025a4383`  |
| 2224   | Layout 1 | `cae0025a4383`  |
| 2218   | Layout 1 | `cae0025a4383`  |
| 2215   | Layout 1 | `cae0025a4383`  |
| 2207   | Layout 1 | `cae0025a4383`  |
| 2203   | Layout 1 | `cae0025a4383`  |
| 2196   | Layout 1 | `cae0025a4383`  |
| 2192   | Layout 1 | `cae0025a4383`  |
| 2189   | Layout 1 | `cae0025a4383`  |
| 2183   | Layout 1 | `cae0025a4383`  |
| 2179   | Layout 1 | `cae0025a4383`  |
| 2171   | Layout 1 | `cae0025a4383`  |
| 2163   | Layout 1 | `cae0025a4383`  |
| 2156   | Layout 1 | `cae0025a4383`  |
| 2151   | Layout 1 | `cae0025a4383`  |
| 2147   | Layout 1 | `cae0025a4383`  |
| 2142   | Layout 1 | `cae0025a4383`  |
| 2138   | Layout 1 | `cae0025a4383`  |
| 2134   | Layout 1 | `cae0025a4383`  |
| 2130   | Layout 1 | `cae0025a4383`  |
| 2122   | Layout 1 | `cae0025a4383`  |
| 2107   | Layout 1 | `cae0025a4383`  |
| 2098   | Layout 1 | `cae0025a4383`  |
| 2089   | Layout 1 | `cae0025a4383`  |
| 2081   | Layout 1 | `cae0025a4383`  |
| 2073   | Layout 1 | `cae0025a4383`  |
| 2067   | Layout 1 | `cae0025a4383`  |
| 2063   | Layout 1 | `cae0025a4383`  |
| 2059   | Layout 1 | `cae0025a4383`  |
| 2052   | Layout 1 | `cae0025a4383`  |
| 2044   | Layout 1 | `cae0025a4383`  |
| 2039   | Layout 1 | `cae0025a4383`  |
| 2032   | Layout 1 | `cae0025a4383`  |
| 2025   | Layout 1 | `cae0025a4383`  |
| 2011   | Layout 1 | `cae0025a4383`  |
| 2005   | Layout 1 | `cae0025a4383`  |
| 2000   | Layout 1 | `cae0025a4383`  |
| 1996   | Layout 1 | `cae0025a4383`  |
| 1991   | Layout 1 | `cae0025a4383`  |
| 1985   | Layout 1 | `cae0025a4383`  |
| 1980   | Layout 1 | `cae0025a4383`  |
| 1969   | Layout 1 | `cae0025a4383`  |
| 1964   | Layout 1 | `cae0025a4383`  |
| 1958   | Layout 1 | `cae0025a4383`  |
| 1950   | Layout 1 | `cae0025a4383`  |
| 1945   | Layout 1 | `cae0025a4383`  |
| 1937   | Layout 1 | `cae0025a4383`  |
| 1933   | Layout 1 | `cae0025a4383`  |
| 1927   | Layout 1 | `cae0025a4383`  |
| 1921   | Layout 1 | `cae0025a4383`  |
| 1914   | Layout 1 | `cae0025a4383`  |
| 1908   | Layout 1 | `cae0025a4383`  |
| 1897   | Layout 1 | `cae0025a4383`  |
| 1892   | Layout 1 | `cae0025a4383`  |
| 1886   | Layout 1 | `cae0025a4383`  |
| 1881   | Layout 1 | `cae0025a4383`  |
| 1871   | Layout 1 | `cae0025a4383`  |
| 1866   | Layout 1 | `cae0025a4383`  |
| 1862   | Layout 1 | `cae0025a4383`  |
| 1854   | Layout 1 | `cae0025a4383`  |
| 1846   | Layout 1 | `cae0025a4383`  |
| 1838   | Layout 1 | `cae0025a4383`  |
| 1832   | Layout 1 | `cae0025a4383`  |
| 1826   | Layout 1 | `cae0025a4383`  |
| 1822   | Layout 1 | `cae0025a4383`  |
| 1818   | Layout 1 | `cae0025a4383`  |
| 1804   | Layout 1 | `cae0025a4383`  |
| 1794   | Layout 1 | `cae0025a4383`  |
| 1790   | Layout 1 | `cae0025a4383`  |
| 1784   | Layout 1 | `cae0025a4383`  |
| 1774   | Layout 1 | `cae0025a4383`  |
| 1771   | Layout 1 | `cae0025a4383`  |
| 1762   | Layout 1 | `cae0025a4383`  |
| 1759   | Layout 1 | `cae0025a4383`  |
| 1754   | Layout 1 | `cae0025a4383`  |
| 1749   | Layout 1 | `cae0025a4383`  |
| 1743   | Layout 1 | `cae0025a4383`  |
| 1737   | Layout 1 | `cae0025a4383`  |
| 1731   | Layout 1 | `cae0025a4383`  |
| 1725   | Layout 1 | `cae0025a4383`  |
| 1717   | Layout 1 | `cae0025a4383`  |
| 1710   | Layout 1 | `cae0025a4383`  |
| 1704   | Layout 1 | `cae0025a4383`  |
| 1698   | Layout 1 | `cae0025a4383`  |
| 1690   | Layout 1 | `cae0025a4383`  |
| 1685   | Layout 1 | `cae0025a4383`  |
| 1680   | Layout 1 | `cae0025a4383`  |
| 1674   | Layout 1 | `cae0025a4383`  |
| 1668   | Layout 1 | `cae0025a4383`  |
| 1659   | Layout 1 | `cae0025a4383`  |
| 1649   | Layout 1 | `cae0025a4383`  |
| 1642   | Layout 1 | `cae0025a4383`  |
| 1636   | Layout 1 | `cae0025a4383`  |
| 1628   | Layout 1 | `cae0025a4383`  |
| 1622   | Layout 1 | `cae0025a4383`  |
| 1614   | Layout 1 | `cae0025a4383`  |
| 1608   | Layout 1 | `cae0025a4383`  |
| 1602   | Layout 1 | `cae0025a4383`  |
| 1598   | Layout 1 | `cae0025a4383`  |
| 1594   | Layout 1 | `cae0025a4383`  |
| 1590   | Layout 1 | `cae0025a4383`  |
| 1587   | Layout 1 | `cae0025a4383`  |
| 1584   | Layout 1 | `cae0025a4383`  |
| 1579   | Layout 1 | `cae0025a4383`  |
| 1572   | Layout 1 | `cae0025a4383`  |
| 1565   | Layout 1 | `cae0025a4383`  |
| 1559   | Layout 1 | `cae0025a4383`  |
| 1554   | Layout 1 | `cae0025a4383`  |
| 1547   | Layout 1 | `cae0025a4383`  |
| 1537   | Layout 1 | `cae0025a4383`  |
| 1529   | Layout 1 | `cae0025a4383`  |
| 1524   | Layout 1 | `cae0025a4383`  |
| 1519   | Layout 1 | `cae0025a4383`  |
| 1509   | Layout 1 | `cae0025a4383`  |
| 1506   | Layout 1 | `cae0025a4383`  |
| 1504   | Layout 1 | `cae0025a4383`  |
| 1500   | Layout 1 | `cae0025a4383`  |
| 1493   | Layout 1 | `cae0025a4383`  |
| 1489   | Layout 1 | `cae0025a4383`  |
| 1485   | Layout 1 | `cae0025a4383`  |
| 1481   | Layout 1 | `cae0025a4383`  |
| 1474   | Layout 1 | `cae0025a4383`  |
| 1466   | Layout 1 | `cae0025a4383`  |
| 1462   | Layout 1 | `cae0025a4383`  |
| 1459   | Layout 1 | `cae0025a4383`  |
| 1453   | Layout 1 | `cae0025a4383`  |
| 1450   | Layout 1 | `cae0025a4383`  |
| 1445   | Layout 1 | `cae0025a4383`  |
| 1439   | Layout 1 | `cae0025a4383`  |
| 1433   | Layout 1 | `cae0025a4383`  |
| 1430   | Layout 1 | `cae0025a4383`  |
| 1426   | Layout 1 | `cae0025a4383`  |
| 1421   | Layout 1 | `cae0025a4383`  |
| 1417   | Layout 1 | `cae0025a4383`  |
| 1416   | Layout 1 | `cae0025a4383`  |
| 1409   | Layout 1 | `cae0025a4383`  |
| 1405   | Layout 1 | `cae0025a4383`  |
| 1401   | Layout 1 | `cae0025a4383`  |
| 1396   | Layout 1 | `cae0025a4383`  |
| 1391   | Layout 1 | `cae0025a4383`  |
| 1390   | Layout 1 | `cae0025a4383`  |
| 1386   | Layout 1 | `cae0025a4383`  |
| 1381   | Layout 1 | `cae0025a4383`  |
| 1379   | Layout 1 | `cae0025a4383`  |
| 1372   | Layout 1 | `cae0025a4383`  |
| 1366   | Layout 1 | `cae0025a4383`  |
| 1364   | Layout 1 | `cae0025a4383`  |
| 1363   | Layout 1 | `cae0025a4383`  |
| 1360   | Layout 1 | `cae0025a4383`  |
| 1358   | Layout 1 | `cae0025a4383`  |
| 1355   | Layout 1 | `cae0025a4383`  |
| 1351   | Layout 1 | `cae0025a4383`  |
| 1348   | Layout 1 | `cae0025a4383`  |
| 1346   | Layout 1 | `cae0025a4383`  |
| 1341   | Layout 1 | `cae0025a4383`  |
| 1340   | Layout 1 | `cae0025a4383`  |
| 1338   | Layout 1 | `cae0025a4383`  |
| 1335   | Layout 1 | `cae0025a4383`  |
| 1333   | Layout 1 | `cae0025a4383`  |
| 1329   | Layout 1 | `cae0025a4383`  |
| 1327   | Layout 1 | `cae0025a4383`  |
| 1324   | Layout 1 | `cae0025a4383`  |
| 1321   | Layout 1 | `cae0025a4383`  |
| 1319   | Layout 1 | `cae0025a4383`  |
| 1318   | Layout 1 | `cae0025a4383`  |
| 1316   | Layout 1 | `cae0025a4383`  |
| 1313   | Layout 1 | `cae0025a4383`  |
| 1311   | Layout 1 | `cae0025a4383`  |
| 1309   | Layout 1 | `cae0025a4383`  |
| 1304   | Layout 1 | `cae0025a4383`  |
| 1292   | Layout 1 | `cae0025a4383`  |
| 1286   | Layout 1 | `cae0025a4383`  |
| 1280   | Layout 1 | `cae0025a4383`  |
| 1276   | Layout 1 | `cae0025a4383`  |
| 1267   | No file  | `cae0025a4383`  |
| 1261   | No file  | `cae0025a4383`  |
| 1256   | No file  | `cae0025a4383`  |
| 1250   | No file  | `cae0025a4383`  |
| 1246   | No file  | `cae0025a4383`  |
| 1239   | No file  | `cae0025a4383`  |
| 1230   | No file  | `cae0025a4383`  |
| 1226   | No file  | `cae0025a4383`  |
| 1220   | No file  | `cae0025a4383`  |
| 1217   | No file  | `cae0025a4383`  |
| 1211   | No file  | `cae0025a4383`  |
| 1210   | No file  | `cae0025a4383`  |
| 1208   | No file  | `cae0025a4383`  |
| 1203   | No file  | `cae0025a4383`  |
| 1197   | No file  | `cae0025a4383`  |
| 1194   | No file  | `cae0025a4383`  |
| 1192   | No file  | `cae0025a4383`  |
| 1187   | No file  | `cae0025a4383`  |
| 1183   | No file  | `cae0025a4383`  |
| 1177   | No file  | `cae0025a4383`  |
| 1173   | No file  | `cae0025a4383`  |
| 1167   | No file  | `cae0025a4383`  |
| 1164   | No file  | `cae0025a4383`  |
| 1156   | No file  | `cae0025a4383`  |
| 1149   | No file  | `cae0025a4383`  |
| 1144   | No file  | `cae0025a4383`  |
| 1137   | No file  | `cae0025a4383`  |
| 1132   | No file  | `cae0025a4383`  |
| 1127   | No file  | `cae0025a4383`  |
| 1122   | No file  | `cae0025a4383`  |
| 1118   | No file  | `cae0025a4383`  |
| 1114   | No file  | `cae0025a4383`  |
| 1109   | No file  | `cae0025a4383`  |
| 1102   | No file  | `cae0025a4383`  |
| 1096   | No file  | `cae0025a4383`  |
| 1088   | No file  | `cae0025a4383`  |
| 1081   | No file  | `cae0025a4383`  |
| 1076   | No file  | `cae0025a4383`  |
| 1069   | No file  | `cae0025a4383`  |
| 1064   | No file  | `cae0025a4383`  |
| 1058   | No file  | `cae0025a4383`  |
| 1051   | No file  | `cae0025a4383`  |
| 1044   | No file  | `cae0025a4383`  |
| 1036   | No file  | `cae0025a4383`  |
| 1026   | No file  | `cae0025a4383`  |
| 1016   | No file  | `cae0025a4383`  |
| 1009   | No file  | `cae0025a4383`  |
| 1005   | No file  | `cae0025a4383`  |
| 1000   | No file  | `cae0025a4383`  |
| 998    | No file  | `cae0025a4383`  |
| 990    | No file  | `cae0025a4383`  |
| 979    | No file  | `cae0025a4383`  |
| 972    | No file  | `cae0025a4383`  |
| 963    | No file  | `cae0025a4383`  |
| 955    | No file  | `cae0025a4383`  |
| 946    | No file  | `cae0025a4383`  |
| 938    | No file  | `cae0025a4383`  |
| 927    | No file  | `cae0025a4383`  |
| 911    | No file  | `cae0025a4383`  |
| 904    | No file  | `cae0025a4383`  |
| 899    | No file  | `cae0025a4383`  |
| 894    | No file  | `cae0025a4383`  |
| 885    | No file  | `cae0025a4383`  |
| 879    | No file  | `cae0025a4383`  |
| 872    | No file  | `cae0025a4383`  |
| 864    | No file  | `cae0025a4383`  |
| 855    | No file  | `cae0025a4383`  |
| 853    | No file  | `cae0025a4383`  |
| 845    | No file  | `cae0025a4383`  |
| 837    | No file  | `cae0025a4383`  |
| 829    | No file  | `cae0025a4383`  |
| 822    | No file  | `cae0025a4383`  |
| 814    | No file  | `cae0025a4383`  |
| 805    | No file  | `cae0025a4383`  |
| 794    | No file  | `cae0025a4383`  |
| 787    | No file  | `cae0025a4383`  |
| 780    | No file  | `cae0025a4383`  |
| 771    | No file  | `cae0025a4383`  |
| 760    | No file  | `cae0025a4383`  |
| 748    | No file  | `cae0025a4383`  |
| 741    | No file  | `cae0025a4383`  |
| 736    | No file  | `cae0025a4383`  |
| 731    | No file  | `cae0025a4383`  |
| 723    | No file  | `cae0025a4383`  |
| 711    | No file  | `cae0025a4383`  |
| 707    | No file  | `cae0025a4383`  |
| 697    | No file  | `cae0025a4383`  |
| 689    | No file  | `cae0025a4383`  |
| 683    | No file  | `cae0025a4383`  |
| 678    | No file  | `cae0025a4383`  |
| 670    | No file  | `cae0025a4383`  |
| 661    | No file  | `cae0025a4383`  |
| 656    | No file  | `cae0025a4383`  |
| 652    | No file  | `cae0025a4383`  |
| 643    | No file  | `cae0025a4383`  |
| 637    | No file  | `cae0025a4383`  |
| 630    | No file  | `cae0025a4383`  |
| 627    | No file  | `cae0025a4383`  |
| 621    | No file  | `cae0025a4383`  |
| 617    | No file  | `cae0025a4383`  |
| 615    | No file  | `cae0025a4383`  |
| 606    | No file  | `cae0025a4383`  |
| 599    | No file  | `cae0025a4383`  |
| 592    | No file  | `cae0025a4383`  |
| 586    | No file  | `cae0025a4383`  |
| 577    | No file  | `cae0025a4383`  |
| 569    | No file  | `cae0025a4383`  |
| 561    | No file  | `cae0025a4383`  |
| 554    | No file  | `cae0025a4383`  |
| 542    | No file  | `cae0025a4383`  |
| 532    | No file  | `cae0025a4383`  |
| 531    | No file  | `cae0025a4383`  |
| 526    | No file  | `cae0025a4383`  |
| 521    | No file  | `cae0025a4383`  |
| 517    | No file  | `cae0025a4383`  |
| 510    | No file  | `cae0025a4383`  |
| 508    | No file  | `cae0025a4383`  |
| 504    | No file  | `cae0025a4383`  |
| 497    | No file  | `cae0025a4383`  |
| 491    | No file  | `cae0025a4383`  |
| 485    | No file  | `cae0025a4383`  |
| 478    | No file  | `cae0025a4383`  |
| 472    | No file  | `cae0025a4383`  |
| 466    | No file  | `cae0025a4383`  |
| 457    | No file  | `cae0025a4383`  |
| 452    | No file  | `cae0025a4383`  |
| 449    | No file  | `cae0025a4383`  |
| 435    | No file  | `cae0025a4383`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                   |
| ------------------------- | -------- | ------------------------------------------------------ |
| `fitnessleveloffset.dbss` | Required | `(fitness type, level) -> (offset, size)` of every row |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type              | Field      | Notes                                       |
| ------- | ----------------- | ---------- | ------------------------------------------- |
| `+0x00` | u32               | type_count | Number of fitness blocks (observed: 3)      |
| `+0x04` | Block[type_count] | blocks     | One block per fitness type                  |

The blocks fill the file exactly: 4 + 3 x (4 + 51 x 29) = 4,453 bytes on client 3458.

### Block (variable: 4 bytes + rows)

| Offset  | Type                   | Field       | Notes                                |
| ------- | ---------------------- | ----------- | ------------------------------------ |
| `+0x00` | u32                    | level_count | Rows in this block (observed: 51)    |
| `+0x04` | Level Row[level_count] | rows        | See Level Row                        |

### Level Row (29 bytes)

| Offset  | Type | Field        | Notes                                                                                          |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------------------------- |
| `+0x00` | u8   | fitness_type | `0` Breath, `1` Strength, `2` Health; equals the block index                                   |
| `+0x01` | u32  | level        | `0` to `50`, ascending inside a block                                                          |
| `+0x05` | u64  | exp          | EXP needed to go from this level to the next, read like `lifeexp.dbss` (Notes); `0` on level 0, rising to 5,500,000 (Breath, Strength) and 2,750,000 (Health) on level 50 |
| `+0x0D` | f32  | max_stamina  | Breath total: max Stamina bonus; `0` in Strength and Health rows                               |
| `+0x11` | f32  | weight_limit | Strength total: weight limit bonus in 1/10,000 LT (`400000` is 40 LT); `0` elsewhere          |
| `+0x15` | f32  | max_hp       | Health total: max HP bonus; `0` elsewhere                                                      |
| `+0x19` | f32  | max_mp       | Health total: max MP/WP/SP bonus (the class's combat resource); `0` elsewhere                  |

Every row carries all four stat floats; only the ones of its own fitness type are non-zero. All stored floats are whole numbers except `weight_limit`, whose LT value can end in `.5` (Strength level 29 is 385,000, 38.5 LT). Levels 0 and 1 hold no bonus; level 2 is the first that grants one.

A row's totals are the bonus at that row's own level, confirmed in game on 2026-10-06: the tooltips at Breath Lv.37, Strength Lv.31 and Health Lv.33 read `Max Stamina +570`, `Weight Limit +42 LT` and `Max HP +320`, the values of rows 37, 31 and 33.

### `fitnessleveloffset.dbss`

Index into `fitnesslevel.dbss`, with the same block shape as the main file but no leading type count.

| Offset  | Type                | Field  | Notes                                     |
| ------- | ------------------- | ------ | ----------------------------------------- |
| `+0x00` | Offset Block[..end] | blocks | Blocks repeated until the end of the file |

The block index is the fitness type; the file stores no type field. 3 x (4 + 51 x 12) = 1,848 bytes on client 3458.

### Offset Block (variable: 4 bytes + rows)

| Offset  | Type                    | Field       | Notes                                 |
| ------- | ----------------------- | ----------- | ------------------------------------- |
| `+0x00` | u32                     | level_count | Rows in this block (observed: 51)     |
| `+0x04` | Offset Row[level_count] | rows        | See Offset Row                        |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                    |
| ------- | ---- | ----------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | level       | Level of the row it points at                                            |
| `+0x04` | u32  | data_offset | Absolute byte offset of the 29-byte row in `fitnesslevel.dbss`           |
| `+0x08` | u32  | data_size   | Always 29                                                                |

The first Breath row sits at `0x08`, after the type count and Breath's level count; each later block starts 4 bytes past the previous block's last row, skipping that block's level count. The parser reads the main file through these rows and checks that each row's `fitness_type` and `level` match the offset row's block and key.

## Enum Values

### Fitness Type

| ID  | Name     | Stat in the row                     |
| --- | -------- | ----------------------------------- |
| 0   | Breath   | `max_stamina`                       |
| 1   | Strength | `weight_limit`                      |
| 2   | Health   | `max_hp`, `max_mp`                  |

The order matches the client's `_ENUM_FITNESS` in `panel_characterinfo_basic_all.luac` (`BREATH`, `POWER`, then Health), whose hover handlers pass `0`, `1` and `2` for the Breath, Strength and Health texts. The stat per type matches the client's tooltip strings `Breath: Max Stamina +`, `Strength: Weight Limit +` and `Health: Max HP +{hpIncrease}, Max {mpTypeName} +{mpIncrease}`.

## Notes

- `fitnessmaxlevel.bss` stores the max level of each fitness type, `50` for all three on client 3464, the top row of every block here; see [fitnessmaxlevel](../bss/fitnessmaxlevel_bss.md).
- Level 30 is the soft cap. No file stores it, but on client 3464 the EXP to the next level jumps between rows 30 and 31 in every block: Breath 20,000 to 50,000, Strength 10,000 to 30,000, Health 5,000 to 20,000. Up to row 30 the step between rows is at most 3,500.
- The client reads a fitness level and its EXP through `getFitnessLevel`, `getCurrFitnessExperiencePoint` and `getDemandFItnessExperiencePoint` (`panel_characterinfo_basic_all_3.luac`); the bonus shown in the tooltip comes from `ToClient_GetFitnessLevelStatus(type)`.
- The four stat floats are cumulative totals, not per-level increments: every column only rises with the level (Breath 25, 50, 75 up to 800; Strength 2 LT up to 80 LT; Health HP 10 up to 490 and MP/WP/SP 10 up to 300).
- Breath and Strength have the same EXP from level 41 up and Strength needs less than Breath on levels 1 to 40.
- Row direction: read like [lifeexp](lifeexp_dbss.md), where a packet capture confirmed that the row of level N is the EXP to go from N to N + 1. Both tables use the same block shape and the client draws both bars as current / demand (`getCurrFitnessExperiencePoint` / `getDemandFItnessExperiencePoint` here, the life skill pair there). Row 0 (`0` EXP, no bonus) is then an unused placeholder, as characters start every fitness stat at Lv.1. No fitness capture yet; a fitness EXP message whose bar matches row N + 1, or a fresh character at Breath Lv.0, would flip it.
