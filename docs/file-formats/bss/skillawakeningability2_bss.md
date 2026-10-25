# `skillawakeningability2.bss` Format

## Purpose

The Skill Add-on options of each skill: one row per skill number with the
list of [`skillawakeningability.dbss`](../dbss/skillawakeningability_dbss.md)
ability indexes the skill offers. The Skill Add-on window lists these
options for the chosen skill, and the player picks two of them.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                         | Bytes  | Records | Row bytes |
| ------ | ------------- | ---------------------------- | ------ | ------- | --------- |
| 2      | 805 and later | `skillawakeningability2.bss` | 83,648 | 909 Row | 92        |
| 1      | 435 to 794    | `skillawakeningability2.bss` | 14,044 | 390 Row | 36        |

| Layout | File                         | Known             | Unknown    |
| ------ | ---------------------------- | ----------------- | ---------- |
| 2      | `skillawakeningability2.bss` | 83,648 B (100.0%) | 0 B (0.0%) |
| 1      | `skillawakeningability2.bss` | 14,044 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `9a88bb022ecd`  |
| 3482   | Layout 2 | `9a88bb022ecd`  |
| 3474   | Layout 2 | `9a88bb022ecd`  |
| 3473   | Layout 2 | `9a88bb022ecd`  |
| 3464   | Layout 2 | `9a88bb022ecd`  |
| 3458   | Layout 2 | `9a88bb022ecd`  |
| 3454   | Layout 2 | `9a88bb022ecd`  |
| 3444   | Layout 2 | `9a88bb022ecd`  |
| 3435   | Layout 2 | `9a88bb022ecd`  |
| 3426   | Layout 2 | `9a88bb022ecd`  |
| 3418   | Layout 2 | `9a88bb022ecd`  |
| 3412   | Layout 2 | `9a88bb022ecd`  |
| 3402   | Layout 2 | `9a88bb022ecd`  |
| 3396   | Layout 2 | `9a88bb022ecd`  |
| 3387   | Layout 2 | `9a88bb022ecd`  |
| 3381   | Layout 2 | `9a88bb022ecd`  |
| 3373   | Layout 2 | `9a88bb022ecd`  |
| 3364   | Layout 2 | `9a88bb022ecd`  |
| 3356   | Layout 2 | `9a88bb022ecd`  |
| 3349   | Layout 2 | `9a88bb022ecd`  |
| 3342   | Layout 2 | `9a88bb022ecd`  |
| 3335   | Layout 2 | `9a88bb022ecd`  |
| 3326   | Layout 2 | `9a88bb022ecd`  |
| 3321   | Layout 2 | `9a88bb022ecd`  |
| 3314   | Layout 2 | `9a88bb022ecd`  |
| 3303   | Layout 2 | `9a88bb022ecd`  |
| 3302   | Layout 2 | `9a88bb022ecd`  |
| 3293   | Layout 2 | `9a88bb022ecd`  |
| 3283   | Layout 2 | `9a88bb022ecd`  |
| 3275   | Layout 2 | `9a88bb022ecd`  |
| 3267   | Layout 2 | `9a88bb022ecd`  |
| 3258   | Layout 2 | `9a88bb022ecd`  |
| 3251   | Layout 2 | `9a88bb022ecd`  |
| 3242   | Layout 2 | `9a88bb022ecd`  |
| 3235   | Layout 2 | `9a88bb022ecd`  |
| 3229   | Layout 2 | `9a88bb022ecd`  |
| 3212   | Layout 2 | `9a88bb022ecd`  |
| 3203   | Layout 2 | `9a88bb022ecd`  |
| 3193   | Layout 2 | `9a88bb022ecd`  |
| 3186   | Layout 2 | `9a88bb022ecd`  |
| 3177   | Layout 2 | `9a88bb022ecd`  |
| 3169   | Layout 2 | `9a88bb022ecd`  |
| 3158   | Layout 2 | `9a88bb022ecd`  |
| 3151   | Layout 2 | `9a88bb022ecd`  |
| 3144   | Layout 2 | `9a88bb022ecd`  |
| 3133   | Layout 2 | `9a88bb022ecd`  |
| 3125   | Layout 2 | `9a88bb022ecd`  |
| 3118   | Layout 2 | `9a88bb022ecd`  |
| 3111   | Layout 2 | `9a88bb022ecd`  |
| 3103   | Layout 2 | `9a88bb022ecd`  |
| 3095   | Layout 2 | `9a88bb022ecd`  |
| 3086   | Layout 2 | `9a88bb022ecd`  |
| 3072   | Layout 2 | `9a88bb022ecd`  |
| 3062   | Layout 2 | `9a88bb022ecd`  |
| 3052   | Layout 2 | `9a88bb022ecd`  |
| 3045   | Layout 2 | `9a88bb022ecd`  |
| 3037   | Layout 2 | `9a88bb022ecd`  |
| 3030   | Layout 2 | `9a88bb022ecd`  |
| 3021   | Layout 2 | `9a88bb022ecd`  |
| 3012   | Layout 2 | `9a88bb022ecd`  |
| 3002   | Layout 2 | `9a88bb022ecd`  |
| 2995   | Layout 2 | `9a88bb022ecd`  |
| 2987   | Layout 2 | `9a88bb022ecd`  |
| 2978   | Layout 2 | `9a88bb022ecd`  |
| 2970   | Layout 2 | `9a88bb022ecd`  |
| 2959   | Layout 2 | `9a88bb022ecd`  |
| 2951   | Layout 2 | `9a88bb022ecd`  |
| 2942   | Layout 2 | `9a88bb022ecd`  |
| 2935   | Layout 2 | `9a88bb022ecd`  |
| 2932   | Layout 2 | `9a88bb022ecd`  |
| 2923   | Layout 2 | `9a88bb022ecd`  |
| 2919   | Layout 2 | `9a88bb022ecd`  |
| 2907   | Layout 2 | `9a88bb022ecd`  |
| 2900   | Layout 2 | `9a88bb022ecd`  |
| 2891   | Layout 2 | `9a88bb022ecd`  |
| 2882   | Layout 2 | `9a88bb022ecd`  |
| 2872   | Layout 2 | `9a88bb022ecd`  |
| 2863   | Layout 2 | `9a88bb022ecd`  |
| 2855   | Layout 2 | `9a88bb022ecd`  |
| 2849   | Layout 2 | `9a88bb022ecd`  |
| 2844   | Layout 2 | `9a88bb022ecd`  |
| 2834   | Layout 2 | `9a88bb022ecd`  |
| 2825   | Layout 2 | `9a88bb022ecd`  |
| 2819   | Layout 2 | `9a88bb022ecd`  |
| 2811   | Layout 2 | `9a88bb022ecd`  |
| 2803   | Layout 2 | `9a88bb022ecd`  |
| 2794   | Layout 2 | `9a88bb022ecd`  |
| 2783   | Layout 2 | `9a88bb022ecd`  |
| 2774   | Layout 2 | `9a88bb022ecd`  |
| 2765   | Layout 2 | `9a88bb022ecd`  |
| 2756   | Layout 2 | `9a88bb022ecd`  |
| 2750   | Layout 2 | `9a88bb022ecd`  |
| 2743   | Layout 2 | `9a88bb022ecd`  |
| 2736   | Layout 2 | `9a88bb022ecd`  |
| 2726   | Layout 2 | `9a88bb022ecd`  |
| 2717   | Layout 2 | `9a88bb022ecd`  |
| 2709   | Layout 2 | `9a88bb022ecd`  |
| 2703   | Layout 2 | `9a88bb022ecd`  |
| 2695   | Layout 2 | `9a88bb022ecd`  |
| 2684   | Layout 2 | `9a88bb022ecd`  |
| 2672   | Layout 2 | `9a88bb022ecd`  |
| 2665   | Layout 2 | `9a88bb022ecd`  |
| 2657   | Layout 2 | `9a88bb022ecd`  |
| 2649   | Layout 2 | `9a88bb022ecd`  |
| 2644   | Layout 2 | `9a88bb022ecd`  |
| 2637   | Layout 2 | `9a88bb022ecd`  |
| 2629   | Layout 2 | `9a88bb022ecd`  |
| 2619   | Layout 2 | `9a88bb022ecd`  |
| 2612   | Layout 2 | `9a88bb022ecd`  |
| 2606   | Layout 2 | `9a88bb022ecd`  |
| 2602   | Layout 2 | `9a88bb022ecd`  |
| 2601   | Layout 2 | `9a88bb022ecd`  |
| 2592   | Layout 2 | `9a88bb022ecd`  |
| 2583   | Layout 2 | `9a88bb022ecd`  |
| 2575   | Layout 2 | `9a88bb022ecd`  |
| 2567   | Layout 2 | `9a88bb022ecd`  |
| 2560   | Layout 2 | `9a88bb022ecd`  |
| 2553   | Layout 2 | `9a88bb022ecd`  |
| 2545   | Layout 2 | `9a88bb022ecd`  |
| 2538   | Layout 2 | `9a88bb022ecd`  |
| 2529   | Layout 2 | `9a88bb022ecd`  |
| 2519   | Layout 2 | `9a88bb022ecd`  |
| 2513   | Layout 2 | `9a88bb022ecd`  |
| 2510   | Layout 2 | `9a88bb022ecd`  |
| 2507   | Layout 2 | `9a88bb022ecd`  |
| 2503   | Layout 2 | `9a88bb022ecd`  |
| 2498   | Layout 2 | `9a88bb022ecd`  |
| 2492   | Layout 2 | `9a88bb022ecd`  |
| 2487   | Layout 2 | `9a88bb022ecd`  |
| 2480   | Layout 2 | `9a88bb022ecd`  |
| 2474   | Layout 2 | `9a88bb022ecd`  |
| 2468   | Layout 2 | `9a88bb022ecd`  |
| 2460   | Layout 2 | `9a88bb022ecd`  |
| 2453   | Layout 2 | `9a88bb022ecd`  |
| 2444   | Layout 2 | `9a88bb022ecd`  |
| 2438   | Layout 2 | `9a88bb022ecd`  |
| 2434   | Layout 2 | `9a88bb022ecd`  |
| 2429   | Layout 2 | `9a88bb022ecd`  |
| 2421   | Layout 2 | `9a88bb022ecd`  |
| 2414   | Layout 2 | `9a88bb022ecd`  |
| 2407   | Layout 2 | `9a88bb022ecd`  |
| 2401   | Layout 2 | `9a88bb022ecd`  |
| 2397   | Layout 2 | `9a88bb022ecd`  |
| 2393   | Layout 2 | `9a88bb022ecd`  |
| 2384   | Layout 2 | `9a88bb022ecd`  |
| 2378   | Layout 2 | `9a88bb022ecd`  |
| 2372   | Layout 2 | `9a88bb022ecd`  |
| 2358   | Layout 2 | `9a88bb022ecd`  |
| 2352   | Layout 2 | `9a88bb022ecd`  |
| 2347   | Layout 2 | `9a88bb022ecd`  |
| 2343   | Layout 2 | `9a88bb022ecd`  |
| 2335   | Layout 2 | `9a88bb022ecd`  |
| 2327   | Layout 2 | `9a88bb022ecd`  |
| 2324   | Layout 2 | `9a88bb022ecd`  |
| 2319   | Layout 2 | `9a88bb022ecd`  |
| 2313   | Layout 2 | `9a88bb022ecd`  |
| 2308   | Layout 2 | `9a88bb022ecd`  |
| 2302   | Layout 2 | `9a88bb022ecd`  |
| 2295   | Layout 2 | `9a88bb022ecd`  |
| 2290   | Layout 2 | `9a88bb022ecd`  |
| 2284   | Layout 2 | `9a88bb022ecd`  |
| 2276   | Layout 2 | `9a88bb022ecd`  |
| 2269   | Layout 2 | `9a88bb022ecd`  |
| 2259   | Layout 2 | `9a88bb022ecd`  |
| 2250   | Layout 2 | `9a88bb022ecd`  |
| 2243   | Layout 2 | `9a88bb022ecd`  |
| 2235   | Layout 2 | `9a88bb022ecd`  |
| 2229   | Layout 2 | `9a88bb022ecd`  |
| 2224   | Layout 2 | `9a88bb022ecd`  |
| 2218   | Layout 2 | `9a88bb022ecd`  |
| 2215   | Layout 2 | `9a88bb022ecd`  |
| 2207   | Layout 2 | `9a88bb022ecd`  |
| 2203   | Layout 2 | `9a88bb022ecd`  |
| 2196   | Layout 2 | `9a88bb022ecd`  |
| 2192   | Layout 2 | `9a88bb022ecd`  |
| 2189   | Layout 2 | `9a88bb022ecd`  |
| 2183   | Layout 2 | `9a88bb022ecd`  |
| 2179   | Layout 2 | `9a88bb022ecd`  |
| 2171   | Layout 2 | `9a88bb022ecd`  |
| 2163   | Layout 2 | `9a88bb022ecd`  |
| 2156   | Layout 2 | `9a88bb022ecd`  |
| 2151   | Layout 2 | `9a88bb022ecd`  |
| 2147   | Layout 2 | `9a88bb022ecd`  |
| 2142   | Layout 2 | `9a88bb022ecd`  |
| 2138   | Layout 2 | `9a88bb022ecd`  |
| 2134   | Layout 2 | `9a88bb022ecd`  |
| 2130   | Layout 2 | `9a88bb022ecd`  |
| 2122   | Layout 2 | `9a88bb022ecd`  |
| 2107   | Layout 2 | `9a88bb022ecd`  |
| 2098   | Layout 2 | `9a88bb022ecd`  |
| 2089   | Layout 2 | `9a88bb022ecd`  |
| 2081   | Layout 2 | `9a88bb022ecd`  |
| 2073   | Layout 2 | `9a88bb022ecd`  |
| 2067   | Layout 2 | `9a88bb022ecd`  |
| 2063   | Layout 2 | `9a88bb022ecd`  |
| 2059   | Layout 2 | `9a88bb022ecd`  |
| 2052   | Layout 2 | `9a88bb022ecd`  |
| 2044   | Layout 2 | `9a88bb022ecd`  |
| 2039   | Layout 2 | `9a88bb022ecd`  |
| 2032   | Layout 2 | `9a88bb022ecd`  |
| 2025   | Layout 2 | `9a88bb022ecd`  |
| 2011   | Layout 2 | `9a88bb022ecd`  |
| 2005   | Layout 2 | `9a88bb022ecd`  |
| 2000   | Layout 2 | `9a88bb022ecd`  |
| 1996   | Layout 2 | `9a88bb022ecd`  |
| 1991   | Layout 2 | `9a88bb022ecd`  |
| 1985   | Layout 2 | `9a88bb022ecd`  |
| 1980   | Layout 2 | `9a88bb022ecd`  |
| 1969   | Layout 2 | `9a88bb022ecd`  |
| 1964   | Layout 2 | `9a88bb022ecd`  |
| 1958   | Layout 2 | `9a88bb022ecd`  |
| 1950   | Layout 2 | `9a88bb022ecd`  |
| 1945   | Layout 2 | `9a88bb022ecd`  |
| 1937   | Layout 2 | `9a88bb022ecd`  |
| 1933   | Layout 2 | `9a88bb022ecd`  |
| 1927   | Layout 2 | `9a88bb022ecd`  |
| 1921   | Layout 2 | `9a88bb022ecd`  |
| 1914   | Layout 2 | `9a88bb022ecd`  |
| 1908   | Layout 2 | `9a88bb022ecd`  |
| 1897   | Layout 2 | `9a88bb022ecd`  |
| 1892   | Layout 2 | `9a88bb022ecd`  |
| 1886   | Layout 2 | `9a88bb022ecd`  |
| 1881   | Layout 2 | `9a88bb022ecd`  |
| 1871   | Layout 2 | `9a88bb022ecd`  |
| 1866   | Layout 2 | `9a88bb022ecd`  |
| 1862   | Layout 2 | `9a88bb022ecd`  |
| 1854   | Layout 2 | `9a88bb022ecd`  |
| 1846   | Layout 2 | `9a88bb022ecd`  |
| 1838   | Layout 2 | `9a88bb022ecd`  |
| 1832   | Layout 2 | `9a88bb022ecd`  |
| 1826   | Layout 2 | `9a88bb022ecd`  |
| 1822   | Layout 2 | `9a88bb022ecd`  |
| 1818   | Layout 2 | `9a88bb022ecd`  |
| 1804   | Layout 2 | `9a88bb022ecd`  |
| 1794   | Layout 2 | `9a88bb022ecd`  |
| 1790   | Layout 2 | `9a88bb022ecd`  |
| 1784   | Layout 2 | `9a88bb022ecd`  |
| 1774   | Layout 2 | `9a88bb022ecd`  |
| 1771   | Layout 2 | `9a88bb022ecd`  |
| 1762   | Layout 2 | `9a88bb022ecd`  |
| 1759   | Layout 2 | `9a88bb022ecd`  |
| 1754   | Layout 2 | `9a88bb022ecd`  |
| 1749   | Layout 2 | `9a88bb022ecd`  |
| 1743   | Layout 2 | `9a88bb022ecd`  |
| 1737   | Layout 2 | `9a88bb022ecd`  |
| 1731   | Layout 2 | `9a88bb022ecd`  |
| 1725   | Layout 2 | `9a88bb022ecd`  |
| 1717   | Layout 2 | `9a88bb022ecd`  |
| 1710   | Layout 2 | `9a88bb022ecd`  |
| 1704   | Layout 2 | `9a88bb022ecd`  |
| 1698   | Layout 2 | `9a88bb022ecd`  |
| 1690   | Layout 2 | `9a88bb022ecd`  |
| 1685   | Layout 2 | `9a88bb022ecd`  |
| 1680   | Layout 2 | `9a88bb022ecd`  |
| 1674   | Layout 2 | `9a88bb022ecd`  |
| 1668   | Layout 2 | `9a88bb022ecd`  |
| 1659   | Layout 2 | `9a88bb022ecd`  |
| 1649   | Layout 2 | `9a88bb022ecd`  |
| 1642   | Layout 2 | `9a88bb022ecd`  |
| 1636   | Layout 2 | `9a88bb022ecd`  |
| 1628   | Layout 2 | `9a88bb022ecd`  |
| 1622   | Layout 2 | `9a88bb022ecd`  |
| 1614   | Layout 2 | `9a88bb022ecd`  |
| 1608   | Layout 2 | `9a88bb022ecd`  |
| 1602   | Layout 2 | `9a88bb022ecd`  |
| 1598   | Layout 2 | `9a88bb022ecd`  |
| 1594   | Layout 2 | `9a88bb022ecd`  |
| 1590   | Layout 2 | `9a88bb022ecd`  |
| 1587   | Layout 2 | `9a88bb022ecd`  |
| 1584   | Layout 2 | `9a88bb022ecd`  |
| 1579   | Layout 2 | `9a88bb022ecd`  |
| 1572   | Layout 2 | `9a88bb022ecd`  |
| 1565   | Layout 2 | `9a88bb022ecd`  |
| 1559   | Layout 2 | `9a88bb022ecd`  |
| 1554   | Layout 2 | `9a88bb022ecd`  |
| 1547   | Layout 2 | `9a88bb022ecd`  |
| 1537   | Layout 2 | `9a88bb022ecd`  |
| 1529   | Layout 2 | `9a88bb022ecd`  |
| 1524   | Layout 2 | `9a88bb022ecd`  |
| 1519   | Layout 2 | `9a88bb022ecd`  |
| 1509   | Layout 2 | `9a88bb022ecd`  |
| 1506   | Layout 2 | `9a88bb022ecd`  |
| 1504   | Layout 2 | `9a88bb022ecd`  |
| 1500   | Layout 2 | `9a88bb022ecd`  |
| 1493   | Layout 2 | `9a88bb022ecd`  |
| 1489   | Layout 2 | `9a88bb022ecd`  |
| 1485   | Layout 2 | `9a88bb022ecd`  |
| 1481   | Layout 2 | `9a88bb022ecd`  |
| 1474   | Layout 2 | `9a88bb022ecd`  |
| 1466   | Layout 2 | `9a88bb022ecd`  |
| 1462   | Layout 2 | `9a88bb022ecd`  |
| 1459   | Layout 2 | `9a88bb022ecd`  |
| 1453   | Layout 2 | `9a88bb022ecd`  |
| 1450   | Layout 2 | `9a88bb022ecd`  |
| 1445   | Layout 2 | `9a88bb022ecd`  |
| 1439   | Layout 2 | `9a88bb022ecd`  |
| 1433   | Layout 2 | `9a88bb022ecd`  |
| 1430   | Layout 2 | `9a88bb022ecd`  |
| 1426   | Layout 2 | `9a88bb022ecd`  |
| 1421   | Layout 2 | `9a88bb022ecd`  |
| 1417   | Layout 2 | `9a88bb022ecd`  |
| 1416   | Layout 2 | `9a88bb022ecd`  |
| 1409   | Layout 2 | `9a88bb022ecd`  |
| 1405   | Layout 2 | `9a88bb022ecd`  |
| 1401   | Layout 2 | `9a88bb022ecd`  |
| 1396   | Layout 2 | `9a88bb022ecd`  |
| 1391   | Layout 2 | `9a88bb022ecd`  |
| 1390   | Layout 2 | `9a88bb022ecd`  |
| 1386   | Layout 2 | `9a88bb022ecd`  |
| 1381   | Layout 2 | `9a88bb022ecd`  |
| 1379   | Layout 2 | `9a88bb022ecd`  |
| 1372   | Layout 2 | `9a88bb022ecd`  |
| 1366   | Layout 2 | `9a88bb022ecd`  |
| 1364   | Layout 2 | `9a88bb022ecd`  |
| 1363   | Layout 2 | `9a88bb022ecd`  |
| 1360   | Layout 2 | `9a88bb022ecd`  |
| 1358   | Layout 2 | `9a88bb022ecd`  |
| 1355   | Layout 2 | `9a88bb022ecd`  |
| 1351   | Layout 2 | `9a88bb022ecd`  |
| 1348   | Layout 2 | `9a88bb022ecd`  |
| 1346   | Layout 2 | `9a88bb022ecd`  |
| 1341   | Layout 2 | `9a88bb022ecd`  |
| 1340   | Layout 2 | `9a88bb022ecd`  |
| 1338   | Layout 2 | `9a88bb022ecd`  |
| 1335   | Layout 2 | `9a88bb022ecd`  |
| 1333   | Layout 2 | `9a88bb022ecd`  |
| 1329   | Layout 2 | `9a88bb022ecd`  |
| 1327   | Layout 2 | `9a88bb022ecd`  |
| 1324   | Layout 2 | `9a88bb022ecd`  |
| 1321   | Layout 2 | `9a88bb022ecd`  |
| 1319   | Layout 2 | `9a88bb022ecd`  |
| 1318   | Layout 2 | `9a88bb022ecd`  |
| 1316   | Layout 2 | `9a88bb022ecd`  |
| 1313   | Layout 2 | `9a88bb022ecd`  |
| 1311   | Layout 2 | `9a88bb022ecd`  |
| 1309   | Layout 2 | `9a88bb022ecd`  |
| 1304   | Layout 2 | `9a88bb022ecd`  |
| 1292   | Layout 2 | `9a88bb022ecd`  |
| 1286   | Layout 2 | `9a88bb022ecd`  |
| 1280   | Layout 2 | `9a88bb022ecd`  |
| 1276   | Layout 2 | `9a88bb022ecd`  |
| 1267   | Layout 2 | `9a88bb022ecd`  |
| 1261   | Layout 2 | `9a88bb022ecd`  |
| 1256   | Layout 2 | `9a88bb022ecd`  |
| 1250   | Layout 2 | `9a88bb022ecd`  |
| 1246   | Layout 2 | `9a88bb022ecd`  |
| 1239   | Layout 2 | `9a88bb022ecd`  |
| 1230   | Layout 2 | `9a88bb022ecd`  |
| 1226   | Layout 2 | `9a88bb022ecd`  |
| 1220   | Layout 2 | `9a88bb022ecd`  |
| 1217   | Layout 2 | `9a88bb022ecd`  |
| 1211   | Layout 2 | `9a88bb022ecd`  |
| 1210   | Layout 2 | `9a88bb022ecd`  |
| 1208   | Layout 2 | `9a88bb022ecd`  |
| 1203   | Layout 2 | `9a88bb022ecd`  |
| 1197   | Layout 2 | `9a88bb022ecd`  |
| 1194   | Layout 2 | `9a88bb022ecd`  |
| 1192   | Layout 2 | `9a88bb022ecd`  |
| 1187   | Layout 2 | `9a88bb022ecd`  |
| 1183   | Layout 2 | `9a88bb022ecd`  |
| 1177   | Layout 2 | `9a88bb022ecd`  |
| 1173   | Layout 2 | `9a88bb022ecd`  |
| 1167   | Layout 2 | `9a88bb022ecd`  |
| 1164   | Layout 2 | `9a88bb022ecd`  |
| 1156   | Layout 2 | `9a88bb022ecd`  |
| 1149   | Layout 2 | `9a88bb022ecd`  |
| 1144   | Layout 2 | `9a88bb022ecd`  |
| 1137   | Layout 2 | `9a88bb022ecd`  |
| 1132   | Layout 2 | `9a88bb022ecd`  |
| 1127   | Layout 2 | `9a88bb022ecd`  |
| 1122   | Layout 2 | `9a88bb022ecd`  |
| 1118   | Layout 2 | `9a88bb022ecd`  |
| 1114   | Layout 2 | `9a88bb022ecd`  |
| 1109   | Layout 2 | `9a88bb022ecd`  |
| 1102   | No file  | `9a88bb022ecd`  |
| 1096   | No file  | `9a88bb022ecd`  |
| 1088   | No file  | `9a88bb022ecd`  |
| 1081   | No file  | `9a88bb022ecd`  |
| 1076   | No file  | `9a88bb022ecd`  |
| 1069   | No file  | `9a88bb022ecd`  |
| 1064   | No file  | `9a88bb022ecd`  |
| 1058   | No file  | `9a88bb022ecd`  |
| 1051   | No file  | `9a88bb022ecd`  |
| 1044   | No file  | `9a88bb022ecd`  |
| 1036   | No file  | `9a88bb022ecd`  |
| 1026   | No file  | `9a88bb022ecd`  |
| 1016   | No file  | `9a88bb022ecd`  |
| 1009   | No file  | `9a88bb022ecd`  |
| 1005   | No file  | `9a88bb022ecd`  |
| 1000   | No file  | `9a88bb022ecd`  |
| 998    | No file  | `9a88bb022ecd`  |
| 990    | No file  | `9a88bb022ecd`  |
| 979    | No file  | `9a88bb022ecd`  |
| 972    | No file  | `9a88bb022ecd`  |
| 963    | No file  | `9a88bb022ecd`  |
| 955    | No file  | `9a88bb022ecd`  |
| 946    | No file  | `9a88bb022ecd`  |
| 938    | No file  | `9a88bb022ecd`  |
| 927    | No file  | `9a88bb022ecd`  |
| 911    | No file  | `9a88bb022ecd`  |
| 904    | No file  | `9a88bb022ecd`  |
| 899    | No file  | `9a88bb022ecd`  |
| 894    | No file  | `9a88bb022ecd`  |
| 885    | No file  | `9a88bb022ecd`  |
| 879    | No file  | `9a88bb022ecd`  |
| 872    | No file  | `9a88bb022ecd`  |
| 864    | No file  | `9a88bb022ecd`  |
| 855    | No file  | `9a88bb022ecd`  |
| 853    | No file  | `9a88bb022ecd`  |
| 845    | No file  | `9a88bb022ecd`  |
| 837    | No file  | `9a88bb022ecd`  |
| 829    | Layout 2 | `9a88bb022ecd`  |
| 822    | Layout 2 | `9a88bb022ecd`  |
| 814    | Layout 2 | `9a88bb022ecd`  |
| 805    | Layout 2 | `9a88bb022ecd`  |
| 794    | Layout 1 | `9a88bb022ecd`  |
| 787    | Layout 1 | `9a88bb022ecd`  |
| 780    | Layout 1 | `9a88bb022ecd`  |
| 771    | Layout 1 | `9a88bb022ecd`  |
| 760    | Layout 1 | `9a88bb022ecd`  |
| 748    | Layout 1 | `9a88bb022ecd`  |
| 741    | Layout 1 | `9a88bb022ecd`  |
| 736    | Layout 1 | `9a88bb022ecd`  |
| 731    | Layout 1 | `9a88bb022ecd`  |
| 723    | Layout 1 | `9a88bb022ecd`  |
| 711    | Layout 1 | `9a88bb022ecd`  |
| 707    | Layout 1 | `9a88bb022ecd`  |
| 697    | Layout 1 | `9a88bb022ecd`  |
| 689    | Layout 1 | `9a88bb022ecd`  |
| 683    | Layout 1 | `9a88bb022ecd`  |
| 678    | Layout 1 | `9a88bb022ecd`  |
| 670    | Layout 1 | `9a88bb022ecd`  |
| 661    | Layout 1 | `9a88bb022ecd`  |
| 656    | Layout 1 | `9a88bb022ecd`  |
| 652    | Layout 1 | `9a88bb022ecd`  |
| 643    | Layout 1 | `9a88bb022ecd`  |
| 637    | Layout 1 | `9a88bb022ecd`  |
| 630    | Layout 1 | `9a88bb022ecd`  |
| 627    | Layout 1 | `9a88bb022ecd`  |
| 621    | Layout 1 | `9a88bb022ecd`  |
| 617    | Layout 1 | `9a88bb022ecd`  |
| 615    | Layout 1 | `9a88bb022ecd`  |
| 606    | Layout 1 | `9a88bb022ecd`  |
| 599    | Layout 1 | `9a88bb022ecd`  |
| 592    | Layout 1 | `9a88bb022ecd`  |
| 586    | Layout 1 | `9a88bb022ecd`  |
| 577    | Layout 1 | `9a88bb022ecd`  |
| 569    | Layout 1 | `9a88bb022ecd`  |
| 561    | Layout 1 | `9a88bb022ecd`  |
| 554    | Layout 1 | `9a88bb022ecd`  |
| 542    | Layout 1 | `9a88bb022ecd`  |
| 532    | Layout 1 | `9a88bb022ecd`  |
| 531    | Layout 1 | `9a88bb022ecd`  |
| 526    | Layout 1 | `9a88bb022ecd`  |
| 521    | Layout 1 | `9a88bb022ecd`  |
| 517    | Layout 1 | `9a88bb022ecd`  |
| 510    | Layout 1 | `9a88bb022ecd`  |
| 508    | Layout 1 | `9a88bb022ecd`  |
| 504    | Layout 1 | `9a88bb022ecd`  |
| 497    | Layout 1 | `9a88bb022ecd`  |
| 491    | Layout 1 | `9a88bb022ecd`  |
| 485    | Layout 1 | `9a88bb022ecd`  |
| 478    | Layout 1 | `9a88bb022ecd`  |
| 472    | Layout 1 | `9a88bb022ecd`  |
| 466    | Layout 1 | `9a88bb022ecd`  |
| 457    | Layout 1 | `9a88bb022ecd`  |
| 452    | Layout 1 | `9a88bb022ecd`  |
| 449    | Layout 1 | `9a88bb022ecd`  |
| 435    | Layout 1 | `9a88bb022ecd`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                            |
| ---------------------------- | -------- | --------------------------------------------------------------- |
| `skillawakeningability.dbss` | Optional | The Korean effect text of each ability index, when LOC type 33 has no text |
| `languagedata_*.loc`         | Optional | LOC type 33 effect text of each ability index, the skill names  |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of skills, `909` on client 3482        |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 12 bytes + ability indexes)

| Offset  | Type                 | Field           | Notes                                                                      |
| ------- | -------------------- | --------------- | -------------------------------------------------------------------------- |
| `+0x00` | u16                  | skill_no        | Map key: the skill number, LOC type `10`; all 909 have a `skill.dbss` row (client 3482) |
| `+0x02` | u16                  | skill_no_dup    | Equal to `skill_no` on every row                                           |
| `+0x04` | u64                  | ability_count   | Number of `ability_indexes`; `20` on every row of client 3482, `24` on client 1784 |
| `+0x0c` | u32[ability_count]   | ability_indexes | `skillawakeningability.dbss` ability indexes, in the order the window lists them |

The skill numbers are unique and in no key order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                        |
| ------- | ------------------ | ------------ | ---------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | No field reads a string      |

## Layout 1

No PABR magic and no string table: the file is the row count and the
rows, which have the Row of Layout 2.

### File Layout

| Offset  | Type           | Field     | Notes                                  |
| ------- | -------------- | --------- | -------------------------------------- |
| `+0x00` | u32            | row_count | Number of skills, `390` on client 794  |
| `+0x04` | Row[row_count] | rows      | See Row                                |

## Field Names

The `Awakening_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `SkillNo`, `Ability_Index1` to
`Ability_Index32` and `IsDevelopingContents`. Its 631 rows match the 631
rows of the official client 1784 file:

| Field           | Column                                      | Same value (client 1784) | Same value (client 3482) |
| --------------- | ------------------------------------------- | ------------------------ | ------------------------ |
| skill_no        | `SkillNo`                                   | 631 of 631               | 624 of 631 (the file adds 285) |
| ability_indexes | `Ability_Index1` to `Ability_Index32`, the filled ones in column order | 631 of 631 | 408 of 624 equal the first 20 sheet columns |

Every sheet row fills `Ability_Index1` to `Ability_Index24` and leaves the
other eight `<null>`. `IsDevelopingContents` is `1` on 45 sheet rows, and
those 45 skills are in the client 1784 file too, so the column is not
compiled into it.

The 2016 `gc::SkillAwakeningStaticStatusVer2` has the members `_skillNo`
(u16), `_rootSkillStatic` (a pointer the client fills), `_rate` (`int[1]`),
`_ability` (a vector of u32 keys) and `_abilityStaticStatus` (the pointers
to the ability rows), and `gc::SkillAwakeningStaticStatusVer2Manager` keeps
them in a `pa_unordered_map<unsigned short, ...>`. The file stores the map
key, `_skillNo` and `_ability`; `_rate` has no sheet column and no bytes.

## Ability Lists

`skillawakeningability.dbss` holds the effects in threes, ability indexes
`3n + 1` to `3n + 3`, most with a shorter to a longer duration (index 1
"All Damage Reduction +20 for 10 sec", 2 the same for 15 sec, 3 for 25
sec). Every row lists one index of each of the first 20 threes (24 on
client 1784), all from the same position in the three, so the rows hold
three lists:

| List                    | Rows (client 3482) | Rows (client 1784) |
| ----------------------- | ------------------ | ------------------ |
| `1, 4, 7, ..., 58`      | 293                | 98 (up to `70`)    |
| `2, 5, 8, ..., 59`      | 565                | 479 (up to `71`)   |
| `3, 6, 9, ..., 60`      | 51                 | 54 (up to `72`)    |

Client 3482 dropped indexes 61 to 72 (the MP/WP/SP reduction, the Extra AP
Against Monsters and Humans and the Extra Damage to Humans effects) from
every list; the `.dbss` still has them.

## Notes

- `panel_window_skill_reinforce_all_1.luac` (client 3482, the Skill Add-on
  window) gets the skill with `getSkillStaticStatus(skillNo, 1)`, lists the
  options from `0` to `getSkillAwakenInfoCount() - 1` of its
  `getActiveSkillStatus()` with `getSkillAwakenDescription(index)`, and
  sends the two picked positions with
  `ToClient_RequestSkillAwakening(type, skillIndex, option1, option2)`.
  `ability_count` is the option count and `index` a position in
  `ability_indexes`.
- `panel_window_reinforceskill_all_1.luac` shows the two add-ons a skill
  has with `getSkillAwakenDescription(ToClient_GetAwakeningAbilityIndex(skillNo, i))`,
  the same getter, so `ToClient_GetAwakeningAbilityIndex` returns a position
  in this list as well.
- The handler names each skill from LOC type 10 (`skill_name_tagged()`),
  links it to its `skill.dbss` row, and shows each option's effect text as
  the `skillawakeningability.dbss` handler does: LOC type 33, else the
  Korean `description_kr`.

## Open Questions

### Which of the Three Lists a Skill Gets

The list a skill gets follows its cooldown in part (client 3482, level 1
`cooldown_ms` of `skill.dbss`): the `1, 4, ...` skills have cooldowns of 0
to 11 seconds, the `3, 6, ...` skills 13 to 130 seconds, and the
`2, 5, ...` skills 0 to 120 seconds. No rule separates the middle list from
the other two, and the file holds no field for it, so the sheet sets the
list per skill.
