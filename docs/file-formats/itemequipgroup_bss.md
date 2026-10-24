# `itemequipgroup.bss` Format

## Purpose

Equipment groups: each group key lists the item IDs of one kind of gear across its variants (group 11 holds the Tuvala main weapons of every class, group 14 the Kzarka main weapons). Quest and dialog conditions test a group with `checkequipitemgroup(group, min_level, max_level)` and `checkinventoryitemgroup(group, min_level, max_level)`, so one condition covers every class's version of a weapon. The plain PABR file holds the groups, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records  | Row bytes               |
| ------ | -------------- | ------- | -------------------- | ----- | -------- | ----------------------- |
| 1      | 1500 and later | 3483    | `itemequipgroup.bss` | 5,784 | 61 Group | 8 to 176, 94 on average |

| Layout | File                 | Known            | Unknown    |
| ------ | -------------------- | ---------------- | ---------- |
| 1      | `itemequipgroup.bss` | 5,784 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `91ace5d82823`  |
| 3482   | Layout 1 | `91ace5d82823`  |
| 3474   | Layout 1 | `91ace5d82823`  |
| 3473   | Layout 1 | `91ace5d82823`  |
| 3464   | Layout 1 | `91ace5d82823`  |
| 3458   | Layout 1 | `91ace5d82823`  |
| 3454   | Layout 1 | `91ace5d82823`  |
| 3444   | Layout 1 | `91ace5d82823`  |
| 3435   | Layout 1 | `91ace5d82823`  |
| 3426   | Layout 1 | `91ace5d82823`  |
| 3418   | Layout 1 | `91ace5d82823`  |
| 3412   | Layout 1 | `91ace5d82823`  |
| 3402   | Layout 1 | `91ace5d82823`  |
| 3396   | Layout 1 | `91ace5d82823`  |
| 3387   | Layout 1 | `91ace5d82823`  |
| 3381   | Layout 1 | `91ace5d82823`  |
| 3373   | Layout 1 | `91ace5d82823`  |
| 3364   | Layout 1 | `91ace5d82823`  |
| 3356   | Layout 1 | `91ace5d82823`  |
| 3349   | Layout 1 | `91ace5d82823`  |
| 3342   | Layout 1 | `91ace5d82823`  |
| 3335   | Layout 1 | `91ace5d82823`  |
| 3326   | Layout 1 | `91ace5d82823`  |
| 3321   | Layout 1 | `91ace5d82823`  |
| 3314   | Layout 1 | `91ace5d82823`  |
| 3303   | Layout 1 | `91ace5d82823`  |
| 3302   | Layout 1 | `91ace5d82823`  |
| 3293   | Layout 1 | `91ace5d82823`  |
| 3283   | Layout 1 | `91ace5d82823`  |
| 3275   | Layout 1 | `91ace5d82823`  |
| 3267   | Layout 1 | `91ace5d82823`  |
| 3258   | Layout 1 | `91ace5d82823`  |
| 3251   | Layout 1 | `91ace5d82823`  |
| 3242   | Layout 1 | `91ace5d82823`  |
| 3235   | Layout 1 | `91ace5d82823`  |
| 3229   | Layout 1 | `91ace5d82823`  |
| 3212   | Layout 1 | `91ace5d82823`  |
| 3203   | Layout 1 | `91ace5d82823`  |
| 3193   | Layout 1 | `91ace5d82823`  |
| 3186   | Layout 1 | `91ace5d82823`  |
| 3177   | Layout 1 | `91ace5d82823`  |
| 3169   | Layout 1 | `91ace5d82823`  |
| 3158   | Layout 1 | `91ace5d82823`  |
| 3151   | Layout 1 | `91ace5d82823`  |
| 3144   | Layout 1 | `91ace5d82823`  |
| 3133   | Layout 1 | `91ace5d82823`  |
| 3125   | Layout 1 | `91ace5d82823`  |
| 3118   | Layout 1 | `91ace5d82823`  |
| 3111   | Layout 1 | `91ace5d82823`  |
| 3103   | Layout 1 | `91ace5d82823`  |
| 3095   | Layout 1 | `91ace5d82823`  |
| 3086   | Layout 1 | `91ace5d82823`  |
| 3072   | Layout 1 | `91ace5d82823`  |
| 3062   | Layout 1 | `91ace5d82823`  |
| 3052   | Layout 1 | `91ace5d82823`  |
| 3045   | Layout 1 | `91ace5d82823`  |
| 3037   | Layout 1 | `91ace5d82823`  |
| 3030   | Layout 1 | `91ace5d82823`  |
| 3021   | Layout 1 | `91ace5d82823`  |
| 3012   | Layout 1 | `91ace5d82823`  |
| 3002   | Layout 1 | `91ace5d82823`  |
| 2995   | Layout 1 | `91ace5d82823`  |
| 2987   | Layout 1 | `91ace5d82823`  |
| 2978   | Layout 1 | `91ace5d82823`  |
| 2970   | Layout 1 | `91ace5d82823`  |
| 2959   | Layout 1 | `91ace5d82823`  |
| 2951   | Layout 1 | `91ace5d82823`  |
| 2942   | Layout 1 | `91ace5d82823`  |
| 2935   | Layout 1 | `91ace5d82823`  |
| 2932   | Layout 1 | `91ace5d82823`  |
| 2923   | Layout 1 | `91ace5d82823`  |
| 2919   | Layout 1 | `91ace5d82823`  |
| 2907   | Layout 1 | `91ace5d82823`  |
| 2900   | Layout 1 | `91ace5d82823`  |
| 2891   | Layout 1 | `91ace5d82823`  |
| 2882   | Layout 1 | `91ace5d82823`  |
| 2872   | Layout 1 | `91ace5d82823`  |
| 2863   | Layout 1 | `91ace5d82823`  |
| 2855   | Layout 1 | `91ace5d82823`  |
| 2849   | Layout 1 | `91ace5d82823`  |
| 2844   | Layout 1 | `91ace5d82823`  |
| 2834   | Layout 1 | `91ace5d82823`  |
| 2825   | Layout 1 | `91ace5d82823`  |
| 2819   | Layout 1 | `91ace5d82823`  |
| 2811   | Layout 1 | `91ace5d82823`  |
| 2803   | Layout 1 | `91ace5d82823`  |
| 2794   | Layout 1 | `91ace5d82823`  |
| 2783   | Layout 1 | `91ace5d82823`  |
| 2774   | Layout 1 | `91ace5d82823`  |
| 2765   | Layout 1 | `91ace5d82823`  |
| 2756   | Layout 1 | `91ace5d82823`  |
| 2750   | Layout 1 | `91ace5d82823`  |
| 2743   | Layout 1 | `91ace5d82823`  |
| 2736   | Layout 1 | `91ace5d82823`  |
| 2726   | Layout 1 | `91ace5d82823`  |
| 2717   | Layout 1 | `91ace5d82823`  |
| 2709   | Layout 1 | `91ace5d82823`  |
| 2703   | Layout 1 | `91ace5d82823`  |
| 2695   | Layout 1 | `91ace5d82823`  |
| 2684   | Layout 1 | `91ace5d82823`  |
| 2672   | Layout 1 | `91ace5d82823`  |
| 2665   | Layout 1 | `91ace5d82823`  |
| 2657   | Layout 1 | `91ace5d82823`  |
| 2649   | Layout 1 | `91ace5d82823`  |
| 2644   | Layout 1 | `91ace5d82823`  |
| 2637   | Layout 1 | `91ace5d82823`  |
| 2629   | Layout 1 | `91ace5d82823`  |
| 2619   | Layout 1 | `91ace5d82823`  |
| 2612   | Layout 1 | `91ace5d82823`  |
| 2606   | Layout 1 | `91ace5d82823`  |
| 2602   | Layout 1 | `91ace5d82823`  |
| 2601   | Layout 1 | `91ace5d82823`  |
| 2592   | Layout 1 | `91ace5d82823`  |
| 2583   | Layout 1 | `91ace5d82823`  |
| 2575   | Layout 1 | `91ace5d82823`  |
| 2567   | Layout 1 | `91ace5d82823`  |
| 2560   | Layout 1 | `91ace5d82823`  |
| 2553   | Layout 1 | `91ace5d82823`  |
| 2545   | Layout 1 | `91ace5d82823`  |
| 2538   | Layout 1 | `91ace5d82823`  |
| 2529   | Layout 1 | `91ace5d82823`  |
| 2519   | Layout 1 | `91ace5d82823`  |
| 2513   | Layout 1 | `91ace5d82823`  |
| 2510   | Layout 1 | `91ace5d82823`  |
| 2507   | Layout 1 | `91ace5d82823`  |
| 2503   | Layout 1 | `91ace5d82823`  |
| 2498   | Layout 1 | `91ace5d82823`  |
| 2492   | Layout 1 | `91ace5d82823`  |
| 2487   | Layout 1 | `91ace5d82823`  |
| 2480   | Layout 1 | `91ace5d82823`  |
| 2474   | Layout 1 | `91ace5d82823`  |
| 2468   | Layout 1 | `91ace5d82823`  |
| 2460   | Layout 1 | `91ace5d82823`  |
| 2453   | Layout 1 | `91ace5d82823`  |
| 2444   | Layout 1 | `91ace5d82823`  |
| 2438   | Layout 1 | `91ace5d82823`  |
| 2434   | Layout 1 | `91ace5d82823`  |
| 2429   | Layout 1 | `91ace5d82823`  |
| 2421   | Layout 1 | `91ace5d82823`  |
| 2414   | Layout 1 | `91ace5d82823`  |
| 2407   | Layout 1 | `91ace5d82823`  |
| 2401   | Layout 1 | `91ace5d82823`  |
| 2397   | Layout 1 | `91ace5d82823`  |
| 2393   | Layout 1 | `91ace5d82823`  |
| 2384   | Layout 1 | `91ace5d82823`  |
| 2378   | Layout 1 | `91ace5d82823`  |
| 2372   | Layout 1 | `91ace5d82823`  |
| 2358   | Layout 1 | `91ace5d82823`  |
| 2352   | Layout 1 | `91ace5d82823`  |
| 2347   | Layout 1 | `91ace5d82823`  |
| 2343   | Layout 1 | `91ace5d82823`  |
| 2335   | Layout 1 | `91ace5d82823`  |
| 2327   | Layout 1 | `91ace5d82823`  |
| 2324   | Layout 1 | `91ace5d82823`  |
| 2319   | Layout 1 | `91ace5d82823`  |
| 2313   | Layout 1 | `91ace5d82823`  |
| 2308   | Layout 1 | `91ace5d82823`  |
| 2302   | Layout 1 | `91ace5d82823`  |
| 2295   | Layout 1 | `91ace5d82823`  |
| 2290   | Layout 1 | `91ace5d82823`  |
| 2284   | Layout 1 | `91ace5d82823`  |
| 2276   | Layout 1 | `91ace5d82823`  |
| 2269   | Layout 1 | `91ace5d82823`  |
| 2259   | Layout 1 | `91ace5d82823`  |
| 2250   | Layout 1 | `91ace5d82823`  |
| 2243   | Layout 1 | `91ace5d82823`  |
| 2235   | Layout 1 | `91ace5d82823`  |
| 2229   | Layout 1 | `91ace5d82823`  |
| 2224   | Layout 1 | `91ace5d82823`  |
| 2218   | Layout 1 | `91ace5d82823`  |
| 2215   | Layout 1 | `91ace5d82823`  |
| 2207   | Layout 1 | `91ace5d82823`  |
| 2203   | Layout 1 | `91ace5d82823`  |
| 2196   | Layout 1 | `91ace5d82823`  |
| 2192   | Layout 1 | `91ace5d82823`  |
| 2189   | Layout 1 | `91ace5d82823`  |
| 2183   | Layout 1 | `91ace5d82823`  |
| 2179   | Layout 1 | `91ace5d82823`  |
| 2171   | Layout 1 | `91ace5d82823`  |
| 2163   | Layout 1 | `91ace5d82823`  |
| 2156   | Layout 1 | `91ace5d82823`  |
| 2151   | Layout 1 | `91ace5d82823`  |
| 2147   | Layout 1 | `91ace5d82823`  |
| 2142   | Layout 1 | `91ace5d82823`  |
| 2138   | Layout 1 | `91ace5d82823`  |
| 2134   | Layout 1 | `91ace5d82823`  |
| 2130   | Layout 1 | `91ace5d82823`  |
| 2122   | Layout 1 | `91ace5d82823`  |
| 2107   | Layout 1 | `91ace5d82823`  |
| 2098   | Layout 1 | `91ace5d82823`  |
| 2089   | Layout 1 | `91ace5d82823`  |
| 2081   | Layout 1 | `91ace5d82823`  |
| 2073   | Layout 1 | `91ace5d82823`  |
| 2067   | Layout 1 | `91ace5d82823`  |
| 2063   | Layout 1 | `91ace5d82823`  |
| 2059   | Layout 1 | `91ace5d82823`  |
| 2052   | Layout 1 | `91ace5d82823`  |
| 2044   | Layout 1 | `91ace5d82823`  |
| 2039   | Layout 1 | `91ace5d82823`  |
| 2032   | Layout 1 | `91ace5d82823`  |
| 2025   | Layout 1 | `91ace5d82823`  |
| 2011   | Layout 1 | `91ace5d82823`  |
| 2005   | Layout 1 | `91ace5d82823`  |
| 2000   | Layout 1 | `91ace5d82823`  |
| 1996   | Layout 1 | `91ace5d82823`  |
| 1991   | Layout 1 | `91ace5d82823`  |
| 1985   | Layout 1 | `91ace5d82823`  |
| 1980   | Layout 1 | `91ace5d82823`  |
| 1969   | Layout 1 | `91ace5d82823`  |
| 1964   | Layout 1 | `91ace5d82823`  |
| 1958   | Layout 1 | `91ace5d82823`  |
| 1950   | Layout 1 | `91ace5d82823`  |
| 1945   | Layout 1 | `91ace5d82823`  |
| 1937   | Layout 1 | `91ace5d82823`  |
| 1933   | Layout 1 | `91ace5d82823`  |
| 1927   | Layout 1 | `91ace5d82823`  |
| 1921   | Layout 1 | `91ace5d82823`  |
| 1914   | Layout 1 | `91ace5d82823`  |
| 1908   | Layout 1 | `91ace5d82823`  |
| 1897   | Layout 1 | `91ace5d82823`  |
| 1892   | Layout 1 | `91ace5d82823`  |
| 1886   | Layout 1 | `91ace5d82823`  |
| 1881   | Layout 1 | `91ace5d82823`  |
| 1871   | Layout 1 | `91ace5d82823`  |
| 1866   | Layout 1 | `91ace5d82823`  |
| 1862   | Layout 1 | `91ace5d82823`  |
| 1854   | Layout 1 | `91ace5d82823`  |
| 1846   | Layout 1 | `91ace5d82823`  |
| 1838   | Layout 1 | `91ace5d82823`  |
| 1832   | Layout 1 | `91ace5d82823`  |
| 1826   | Layout 1 | `91ace5d82823`  |
| 1822   | Layout 1 | `91ace5d82823`  |
| 1818   | Layout 1 | `91ace5d82823`  |
| 1804   | Layout 1 | `91ace5d82823`  |
| 1794   | Layout 1 | `91ace5d82823`  |
| 1790   | Layout 1 | `91ace5d82823`  |
| 1784   | Layout 1 | `91ace5d82823`  |
| 1774   | Layout 1 | `91ace5d82823`  |
| 1771   | Layout 1 | `91ace5d82823`  |
| 1762   | Layout 1 | `91ace5d82823`  |
| 1759   | Layout 1 | `91ace5d82823`  |
| 1754   | Layout 1 | `91ace5d82823`  |
| 1749   | Layout 1 | `91ace5d82823`  |
| 1743   | Layout 1 | `91ace5d82823`  |
| 1737   | Layout 1 | `91ace5d82823`  |
| 1731   | Layout 1 | `91ace5d82823`  |
| 1725   | Layout 1 | `91ace5d82823`  |
| 1717   | Layout 1 | `91ace5d82823`  |
| 1710   | Layout 1 | `91ace5d82823`  |
| 1704   | Layout 1 | `91ace5d82823`  |
| 1698   | Layout 1 | `91ace5d82823`  |
| 1690   | Layout 1 | `91ace5d82823`  |
| 1685   | Layout 1 | `91ace5d82823`  |
| 1680   | Layout 1 | `91ace5d82823`  |
| 1674   | Layout 1 | `91ace5d82823`  |
| 1668   | Layout 1 | `91ace5d82823`  |
| 1659   | Layout 1 | `91ace5d82823`  |
| 1649   | Layout 1 | `91ace5d82823`  |
| 1642   | Layout 1 | `91ace5d82823`  |
| 1636   | Layout 1 | `91ace5d82823`  |
| 1628   | Layout 1 | `91ace5d82823`  |
| 1622   | Layout 1 | `91ace5d82823`  |
| 1614   | Layout 1 | `91ace5d82823`  |
| 1608   | Layout 1 | `91ace5d82823`  |
| 1602   | Layout 1 | `91ace5d82823`  |
| 1598   | Layout 1 | `91ace5d82823`  |
| 1594   | Layout 1 | `91ace5d82823`  |
| 1590   | Layout 1 | `91ace5d82823`  |
| 1587   | Layout 1 | `91ace5d82823`  |
| 1584   | Layout 1 | `91ace5d82823`  |
| 1579   | Layout 1 | `91ace5d82823`  |
| 1572   | Layout 1 | `91ace5d82823`  |
| 1565   | Layout 1 | `91ace5d82823`  |
| 1559   | Layout 1 | `91ace5d82823`  |
| 1554   | Layout 1 | `91ace5d82823`  |
| 1547   | Layout 1 | `91ace5d82823`  |
| 1537   | Layout 1 | `91ace5d82823`  |
| 1529   | Layout 1 | `91ace5d82823`  |
| 1524   | Layout 1 | `91ace5d82823`  |
| 1519   | Layout 1 | `91ace5d82823`  |
| 1509   | Layout 1 | `91ace5d82823`  |
| 1506   | Layout 1 | `91ace5d82823`  |
| 1504   | Layout 1 | `91ace5d82823`  |
| 1500   | Layout 1 | `91ace5d82823`  |
| 1493   | No file  | `91ace5d82823`  |
| 1489   | No file  | `91ace5d82823`  |
| 1485   | No file  | `91ace5d82823`  |
| 1481   | No file  | `91ace5d82823`  |
| 1474   | No file  | `91ace5d82823`  |
| 1466   | No file  | `91ace5d82823`  |
| 1462   | No file  | `91ace5d82823`  |
| 1459   | No file  | `91ace5d82823`  |
| 1453   | No file  | `91ace5d82823`  |
| 1450   | No file  | `91ace5d82823`  |
| 1445   | No file  | `91ace5d82823`  |
| 1439   | No file  | `91ace5d82823`  |
| 1433   | No file  | `91ace5d82823`  |
| 1430   | No file  | `91ace5d82823`  |
| 1426   | No file  | `91ace5d82823`  |
| 1421   | No file  | `91ace5d82823`  |
| 1417   | No file  | `91ace5d82823`  |
| 1416   | No file  | `91ace5d82823`  |
| 1409   | No file  | `91ace5d82823`  |
| 1405   | No file  | `91ace5d82823`  |
| 1401   | No file  | `91ace5d82823`  |
| 1396   | No file  | `91ace5d82823`  |
| 1391   | No file  | `91ace5d82823`  |
| 1390   | No file  | `91ace5d82823`  |
| 1386   | No file  | `91ace5d82823`  |
| 1381   | No file  | `91ace5d82823`  |
| 1379   | No file  | `91ace5d82823`  |
| 1372   | No file  | `91ace5d82823`  |
| 1366   | No file  | `91ace5d82823`  |
| 1364   | No file  | `91ace5d82823`  |
| 1363   | No file  | `91ace5d82823`  |
| 1360   | No file  | `91ace5d82823`  |
| 1358   | No file  | `91ace5d82823`  |
| 1355   | No file  | `91ace5d82823`  |
| 1351   | No file  | `91ace5d82823`  |
| 1348   | No file  | `91ace5d82823`  |
| 1346   | No file  | `91ace5d82823`  |
| 1341   | No file  | `91ace5d82823`  |
| 1340   | No file  | `91ace5d82823`  |
| 1338   | No file  | `91ace5d82823`  |
| 1335   | No file  | `91ace5d82823`  |
| 1333   | No file  | `91ace5d82823`  |
| 1329   | No file  | `91ace5d82823`  |
| 1327   | No file  | `91ace5d82823`  |
| 1324   | No file  | `91ace5d82823`  |
| 1321   | No file  | `91ace5d82823`  |
| 1319   | No file  | `91ace5d82823`  |
| 1318   | No file  | `91ace5d82823`  |
| 1316   | No file  | `91ace5d82823`  |
| 1313   | No file  | `91ace5d82823`  |
| 1311   | No file  | `91ace5d82823`  |
| 1309   | No file  | `91ace5d82823`  |
| 1304   | No file  | `91ace5d82823`  |
| 1292   | No file  | `91ace5d82823`  |
| 1286   | No file  | `91ace5d82823`  |
| 1280   | No file  | `91ace5d82823`  |
| 1276   | No file  | `91ace5d82823`  |
| 1267   | No file  | `91ace5d82823`  |
| 1261   | No file  | `91ace5d82823`  |
| 1256   | No file  | `91ace5d82823`  |
| 1250   | No file  | `91ace5d82823`  |
| 1246   | No file  | `91ace5d82823`  |
| 1239   | No file  | `91ace5d82823`  |
| 1230   | No file  | `91ace5d82823`  |
| 1226   | No file  | `91ace5d82823`  |
| 1220   | No file  | `91ace5d82823`  |
| 1217   | No file  | `91ace5d82823`  |
| 1211   | No file  | `91ace5d82823`  |
| 1210   | No file  | `91ace5d82823`  |
| 1208   | No file  | `91ace5d82823`  |
| 1203   | No file  | `91ace5d82823`  |
| 1197   | No file  | `91ace5d82823`  |
| 1194   | No file  | `91ace5d82823`  |
| 1192   | No file  | `91ace5d82823`  |
| 1187   | No file  | `91ace5d82823`  |
| 1183   | No file  | `91ace5d82823`  |
| 1177   | No file  | `91ace5d82823`  |
| 1173   | No file  | `91ace5d82823`  |
| 1167   | No file  | `91ace5d82823`  |
| 1164   | No file  | `91ace5d82823`  |
| 1156   | No file  | `91ace5d82823`  |
| 1149   | No file  | `91ace5d82823`  |
| 1144   | No file  | `91ace5d82823`  |
| 1137   | No file  | `91ace5d82823`  |
| 1132   | No file  | `91ace5d82823`  |
| 1127   | No file  | `91ace5d82823`  |
| 1122   | No file  | `91ace5d82823`  |
| 1118   | No file  | `91ace5d82823`  |
| 1114   | No file  | `91ace5d82823`  |
| 1109   | No file  | `91ace5d82823`  |
| 1102   | No file  | `91ace5d82823`  |
| 1096   | No file  | `91ace5d82823`  |
| 1088   | No file  | `91ace5d82823`  |
| 1081   | No file  | `91ace5d82823`  |
| 1076   | No file  | `91ace5d82823`  |
| 1069   | No file  | `91ace5d82823`  |
| 1064   | No file  | `91ace5d82823`  |
| 1058   | No file  | `91ace5d82823`  |
| 1051   | No file  | `91ace5d82823`  |
| 1044   | No file  | `91ace5d82823`  |
| 1036   | No file  | `91ace5d82823`  |
| 1026   | No file  | `91ace5d82823`  |
| 1016   | No file  | `91ace5d82823`  |
| 1009   | No file  | `91ace5d82823`  |
| 1005   | No file  | `91ace5d82823`  |
| 1000   | No file  | `91ace5d82823`  |
| 998    | No file  | `91ace5d82823`  |
| 990    | No file  | `91ace5d82823`  |
| 979    | No file  | `91ace5d82823`  |
| 972    | No file  | `91ace5d82823`  |
| 963    | No file  | `91ace5d82823`  |
| 955    | No file  | `91ace5d82823`  |
| 946    | No file  | `91ace5d82823`  |
| 938    | No file  | `91ace5d82823`  |
| 927    | No file  | `91ace5d82823`  |
| 911    | No file  | `91ace5d82823`  |
| 904    | No file  | `91ace5d82823`  |
| 899    | No file  | `91ace5d82823`  |
| 894    | No file  | `91ace5d82823`  |
| 885    | No file  | `91ace5d82823`  |
| 879    | No file  | `91ace5d82823`  |
| 872    | No file  | `91ace5d82823`  |
| 864    | No file  | `91ace5d82823`  |
| 855    | No file  | `91ace5d82823`  |
| 853    | No file  | `91ace5d82823`  |
| 845    | No file  | `91ace5d82823`  |
| 837    | No file  | `91ace5d82823`  |
| 829    | No file  | `91ace5d82823`  |
| 822    | No file  | `91ace5d82823`  |
| 814    | No file  | `91ace5d82823`  |
| 805    | No file  | `91ace5d82823`  |
| 794    | No file  | `91ace5d82823`  |
| 787    | No file  | `91ace5d82823`  |
| 780    | No file  | `91ace5d82823`  |
| 771    | No file  | `91ace5d82823`  |
| 760    | No file  | `91ace5d82823`  |
| 748    | No file  | `91ace5d82823`  |
| 741    | No file  | `91ace5d82823`  |
| 736    | No file  | `91ace5d82823`  |
| 731    | No file  | `91ace5d82823`  |
| 723    | No file  | `91ace5d82823`  |
| 711    | No file  | `91ace5d82823`  |
| 707    | No file  | `91ace5d82823`  |
| 697    | No file  | `91ace5d82823`  |
| 689    | No file  | `91ace5d82823`  |
| 683    | No file  | `91ace5d82823`  |
| 678    | No file  | `91ace5d82823`  |
| 670    | No file  | `91ace5d82823`  |
| 661    | No file  | `91ace5d82823`  |
| 656    | No file  | `91ace5d82823`  |
| 652    | No file  | `91ace5d82823`  |
| 643    | No file  | `91ace5d82823`  |
| 637    | No file  | `91ace5d82823`  |
| 630    | No file  | `91ace5d82823`  |
| 627    | No file  | `91ace5d82823`  |
| 621    | No file  | `91ace5d82823`  |
| 617    | No file  | `91ace5d82823`  |
| 615    | No file  | `91ace5d82823`  |
| 606    | No file  | `91ace5d82823`  |
| 599    | No file  | `91ace5d82823`  |
| 592    | No file  | `91ace5d82823`  |
| 586    | No file  | `91ace5d82823`  |
| 577    | No file  | `91ace5d82823`  |
| 569    | No file  | `91ace5d82823`  |
| 561    | No file  | `91ace5d82823`  |
| 554    | No file  | `91ace5d82823`  |
| 542    | No file  | `91ace5d82823`  |
| 532    | No file  | `91ace5d82823`  |
| 531    | No file  | `91ace5d82823`  |
| 526    | No file  | `91ace5d82823`  |
| 521    | No file  | `91ace5d82823`  |
| 517    | No file  | `91ace5d82823`  |
| 510    | No file  | `91ace5d82823`  |
| 508    | No file  | `91ace5d82823`  |
| 504    | No file  | `91ace5d82823`  |
| 497    | No file  | `91ace5d82823`  |
| 491    | No file  | `91ace5d82823`  |
| 485    | No file  | `91ace5d82823`  |
| 478    | No file  | `91ace5d82823`  |
| 472    | No file  | `91ace5d82823`  |
| 466    | No file  | `91ace5d82823`  |
| 457    | No file  | `91ace5d82823`  |
| 452    | No file  | `91ace5d82823`  |
| 449    | No file  | `91ace5d82823`  |
| 435    | No file  | `91ace5d82823`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                    |
| --------------------- | -------- | --------------------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0 at `str_id1=item_id` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                                    |
| ------------------- | ------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                             |
| `+0x04`             | u32          | count              | Number of groups                                         |
| `+0x08`             | Group[count] | groups             | Variable-size groups, back to back; see Group            |
| `groups+0x00`       | String Table | string_table       | See String Table                                         |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the groups end           |
| `string_table+0x04` | u32          | zero               | Always `0`                                               |

The string table has the shape `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Walking `count` groups ends exactly at `string_table_start`.

### Group (variable: 8 bytes + items)

| Offset  | Type             | Field         | Notes                                                                 |
| ------- | ---------------- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16              | group_key     | Unique; the first argument of `checkequipitemgroup` and `checkinventoryitemgroup` |
| `+0x02` | u16              | group_key_dup | Equal to `group_key` in every group                                   |
| `+0x04` | u32              | item_count    | Number of items; `0` on three groups (client 3474)                     |
| `+0x08` | u32[item_count]  | item_ids      | Item IDs, LOC type 0 `str_id1`; no enhancement level packed in        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No group reads a string              |

## Conditions

`quest.dbss` (`condition_script`) and `detail_dialog.dbss` call two script functions with a group key here, the lowest enhancement level and the highest:

| Call                                       | Example                                   |
| ------------------------------------------ | ----------------------------------------- |
| `checkequipitemgroup(group, min, max)`     | `checkequipitemgroup(11,20,20)`           |
| `checkinventoryitemgroup(group, min, max)` | `checkinventoryitemgroup(11,20,20)`       |

On client 3474, `quest.dbss` holds 34 `checkequipitemgroup` and 21 `checkinventoryitemgroup` calls, and `detail_dialog.dbss` 25 and 21. Every group key they name is in the file. The Old Moon's Resplendent weapon quests (chains 41009 to 41011) test both calls with one group: quest 41009 / 1 `Old Moon's Resplendent Main Weapon: Tuvala` checks group 11 at level 20, quest 41009 / 4 `Old Moon's Resplendent Main Weapon: Kzarka` group 14 at level 19. Quest 9110 / 20 `[Edana's Defense Gear] Godslayer of Legend` checks groups 56 to 59 (one Edana armor piece each) at levels 0 to 10, and the dialogs check groups 41 to 43 (Tuvala main weapons, sub-weapons and armor) at levels 16 to 20.

## Field Names

The `Item_Group` sheet of a private server's `DataSheets.bexcel` on client 1784 has two columns: `Group_Index` (`group_key`) and `Item_Index` (`item_ids`, as one comma-separated list). The same server's compiled `itemequipgroup.bss` matches the sheet in all 43 groups, item for item. Against the client 1784 file, 42 of 43 groups match; group 47 is empty in the client and lists 15 items in the sheet. The server executable of that private server names the loader `loadEquipGroupInformation`, the record type `ItemEquipGroupStaticStatus` (keyed by a u16 `KeyType`) with its list `_itemList`, and the script arguments `EquipGroupKey`, `minEnchantLevel` and `maxEnchantLevel`.

On client 3474, 2 of the 43 shared groups (4 and 5) still match the sheet item for item. 24 start with the sheet's list in its order and append newer gear (groups 1 to 3 gained 731628 and 731631, 731728 and 731731, 731828 and 731831). The other 17 were refilled with other items (groups 41 and 42 moved from the 694xxx to the 695xxx Tuvala weapons) or emptied (6 and 8). Groups 53 to 70 are newer than the sheet.

## Notes

- On client 3474 the file is `5,784` bytes: 61 groups with keys 1 to 23 and 33 to 70, 1,319 items, 1,189 distinct. Groups 6, 8 and 53 are empty.
- The groups are not in key order (70, 69, 68, ..., 64, 47, 46, ...).
- An item can sit in more than one group (81 items on client 3474), and groups 21, 44 and 67 list one item twice.
- No client 3474 Lua file (`luacscript/`) calls either function or names the file. The only Lua text with `EquipItemGroup` in it is the drop window control `Static_EquipableDropItemGroup` (`panel_window_renewdropitem_all_1.luac`), which lists a monster's equipment drops.
- Client 1784 has the same layout: `3,400` bytes, 43 groups with keys 1 to 23 and 33 to 52.
