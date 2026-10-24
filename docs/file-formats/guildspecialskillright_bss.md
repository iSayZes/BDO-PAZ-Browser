# `guildspecialskillright.bss` Format

## Purpose

Which guild member grades may use each special guild skill: one row per
guild skill number with one flag per member grade, the flags of
[guildright](guildright_bss.md). On client 3474 the file has 8 rows:
Command to Gather, Battle Command to Gather, Breath of Life, Blessing of
Battle and the four skills Admiral's Rally, BreezyVoyage, Seaforge
Blessing and Seawatch Pulse, each with grades `0`, `6`, `8` and `9` set.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ------- | --------- |
| 1      | 1421 and later | 3483    | `guildspecialskillright.bss` | 156   | 8 Row   | 17        |

| Layout | File                         | Known          | Unknown    |
| ------ | ---------------------------- | -------------- | ---------- |
| 1      | `guildspecialskillright.bss` | 156 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c9c230702f49`  |
| 3482   | Layout 1 | `c9c230702f49`  |
| 3474   | Layout 1 | `c9c230702f49`  |
| 3473   | Layout 1 | `c9c230702f49`  |
| 3464   | Layout 1 | `c9c230702f49`  |
| 3458   | Layout 1 | `c9c230702f49`  |
| 3454   | Layout 1 | `c9c230702f49`  |
| 3444   | Layout 1 | `c9c230702f49`  |
| 3435   | Layout 1 | `c9c230702f49`  |
| 3426   | Layout 1 | `c9c230702f49`  |
| 3418   | Layout 1 | `c9c230702f49`  |
| 3412   | Layout 1 | `c9c230702f49`  |
| 3402   | Layout 1 | `c9c230702f49`  |
| 3396   | Layout 1 | `c9c230702f49`  |
| 3387   | Layout 1 | `c9c230702f49`  |
| 3381   | Layout 1 | `c9c230702f49`  |
| 3373   | Layout 1 | `c9c230702f49`  |
| 3364   | Layout 1 | `c9c230702f49`  |
| 3356   | Layout 1 | `c9c230702f49`  |
| 3349   | Layout 1 | `c9c230702f49`  |
| 3342   | Layout 1 | `c9c230702f49`  |
| 3335   | Layout 1 | `c9c230702f49`  |
| 3326   | Layout 1 | `c9c230702f49`  |
| 3321   | Layout 1 | `c9c230702f49`  |
| 3314   | Layout 1 | `c9c230702f49`  |
| 3303   | Layout 1 | `c9c230702f49`  |
| 3302   | Layout 1 | `c9c230702f49`  |
| 3293   | Layout 1 | `c9c230702f49`  |
| 3283   | Layout 1 | `c9c230702f49`  |
| 3275   | Layout 1 | `c9c230702f49`  |
| 3267   | Layout 1 | `c9c230702f49`  |
| 3258   | Layout 1 | `c9c230702f49`  |
| 3251   | Layout 1 | `c9c230702f49`  |
| 3242   | Layout 1 | `c9c230702f49`  |
| 3235   | Layout 1 | `c9c230702f49`  |
| 3229   | Layout 1 | `c9c230702f49`  |
| 3212   | Layout 1 | `c9c230702f49`  |
| 3203   | Layout 1 | `c9c230702f49`  |
| 3193   | Layout 1 | `c9c230702f49`  |
| 3186   | Layout 1 | `c9c230702f49`  |
| 3177   | Layout 1 | `c9c230702f49`  |
| 3169   | Layout 1 | `c9c230702f49`  |
| 3158   | Layout 1 | `c9c230702f49`  |
| 3151   | Layout 1 | `c9c230702f49`  |
| 3144   | Layout 1 | `c9c230702f49`  |
| 3133   | Layout 1 | `c9c230702f49`  |
| 3125   | Layout 1 | `c9c230702f49`  |
| 3118   | Layout 1 | `c9c230702f49`  |
| 3111   | Layout 1 | `c9c230702f49`  |
| 3103   | Layout 1 | `c9c230702f49`  |
| 3095   | Layout 1 | `c9c230702f49`  |
| 3086   | Layout 1 | `c9c230702f49`  |
| 3072   | Layout 1 | `c9c230702f49`  |
| 3062   | Layout 1 | `c9c230702f49`  |
| 3052   | Layout 1 | `c9c230702f49`  |
| 3045   | Layout 1 | `c9c230702f49`  |
| 3037   | Layout 1 | `c9c230702f49`  |
| 3030   | Layout 1 | `c9c230702f49`  |
| 3021   | Layout 1 | `c9c230702f49`  |
| 3012   | Layout 1 | `c9c230702f49`  |
| 3002   | Layout 1 | `c9c230702f49`  |
| 2995   | Layout 1 | `c9c230702f49`  |
| 2987   | Layout 1 | `c9c230702f49`  |
| 2978   | Layout 1 | `c9c230702f49`  |
| 2970   | Layout 1 | `c9c230702f49`  |
| 2959   | Layout 1 | `c9c230702f49`  |
| 2951   | Layout 1 | `c9c230702f49`  |
| 2942   | Layout 1 | `c9c230702f49`  |
| 2935   | Layout 1 | `c9c230702f49`  |
| 2932   | Layout 1 | `c9c230702f49`  |
| 2923   | Layout 1 | `c9c230702f49`  |
| 2919   | Layout 1 | `c9c230702f49`  |
| 2907   | Layout 1 | `c9c230702f49`  |
| 2900   | Layout 1 | `c9c230702f49`  |
| 2891   | Layout 1 | `c9c230702f49`  |
| 2882   | Layout 1 | `c9c230702f49`  |
| 2872   | Layout 1 | `c9c230702f49`  |
| 2863   | Layout 1 | `c9c230702f49`  |
| 2855   | Layout 1 | `c9c230702f49`  |
| 2849   | Layout 1 | `c9c230702f49`  |
| 2844   | Layout 1 | `c9c230702f49`  |
| 2834   | Layout 1 | `c9c230702f49`  |
| 2825   | Layout 1 | `c9c230702f49`  |
| 2819   | Layout 1 | `c9c230702f49`  |
| 2811   | Layout 1 | `c9c230702f49`  |
| 2803   | Layout 1 | `c9c230702f49`  |
| 2794   | Layout 1 | `c9c230702f49`  |
| 2783   | Layout 1 | `c9c230702f49`  |
| 2774   | Layout 1 | `c9c230702f49`  |
| 2765   | Layout 1 | `c9c230702f49`  |
| 2756   | Layout 1 | `c9c230702f49`  |
| 2750   | Layout 1 | `c9c230702f49`  |
| 2743   | Layout 1 | `c9c230702f49`  |
| 2736   | Layout 1 | `c9c230702f49`  |
| 2726   | Layout 1 | `c9c230702f49`  |
| 2717   | Layout 1 | `c9c230702f49`  |
| 2709   | Layout 1 | `c9c230702f49`  |
| 2703   | Layout 1 | `c9c230702f49`  |
| 2695   | Layout 1 | `c9c230702f49`  |
| 2684   | Layout 1 | `c9c230702f49`  |
| 2672   | Layout 1 | `c9c230702f49`  |
| 2665   | Layout 1 | `c9c230702f49`  |
| 2657   | Layout 1 | `c9c230702f49`  |
| 2649   | Layout 1 | `c9c230702f49`  |
| 2644   | Layout 1 | `c9c230702f49`  |
| 2637   | Layout 1 | `c9c230702f49`  |
| 2629   | Layout 1 | `c9c230702f49`  |
| 2619   | Layout 1 | `c9c230702f49`  |
| 2612   | Layout 1 | `c9c230702f49`  |
| 2606   | Layout 1 | `c9c230702f49`  |
| 2602   | Layout 1 | `c9c230702f49`  |
| 2601   | Layout 1 | `c9c230702f49`  |
| 2592   | Layout 1 | `c9c230702f49`  |
| 2583   | Layout 1 | `c9c230702f49`  |
| 2575   | Layout 1 | `c9c230702f49`  |
| 2567   | Layout 1 | `c9c230702f49`  |
| 2560   | Layout 1 | `c9c230702f49`  |
| 2553   | Layout 1 | `c9c230702f49`  |
| 2545   | Layout 1 | `c9c230702f49`  |
| 2538   | Layout 1 | `c9c230702f49`  |
| 2529   | Layout 1 | `c9c230702f49`  |
| 2519   | Layout 1 | `c9c230702f49`  |
| 2513   | Layout 1 | `c9c230702f49`  |
| 2510   | Layout 1 | `c9c230702f49`  |
| 2507   | Layout 1 | `c9c230702f49`  |
| 2503   | Layout 1 | `c9c230702f49`  |
| 2498   | Layout 1 | `c9c230702f49`  |
| 2492   | Layout 1 | `c9c230702f49`  |
| 2487   | Layout 1 | `c9c230702f49`  |
| 2480   | Layout 1 | `c9c230702f49`  |
| 2474   | Layout 1 | `c9c230702f49`  |
| 2468   | Layout 1 | `c9c230702f49`  |
| 2460   | Layout 1 | `c9c230702f49`  |
| 2453   | Layout 1 | `c9c230702f49`  |
| 2444   | Layout 1 | `c9c230702f49`  |
| 2438   | Layout 1 | `c9c230702f49`  |
| 2434   | Layout 1 | `c9c230702f49`  |
| 2429   | Layout 1 | `c9c230702f49`  |
| 2421   | Layout 1 | `c9c230702f49`  |
| 2414   | Layout 1 | `c9c230702f49`  |
| 2407   | Layout 1 | `c9c230702f49`  |
| 2401   | Layout 1 | `c9c230702f49`  |
| 2397   | Layout 1 | `c9c230702f49`  |
| 2393   | Layout 1 | `c9c230702f49`  |
| 2384   | Layout 1 | `c9c230702f49`  |
| 2378   | Layout 1 | `c9c230702f49`  |
| 2372   | Layout 1 | `c9c230702f49`  |
| 2358   | Layout 1 | `c9c230702f49`  |
| 2352   | Layout 1 | `c9c230702f49`  |
| 2347   | Layout 1 | `c9c230702f49`  |
| 2343   | Layout 1 | `c9c230702f49`  |
| 2335   | Layout 1 | `c9c230702f49`  |
| 2327   | Layout 1 | `c9c230702f49`  |
| 2324   | Layout 1 | `c9c230702f49`  |
| 2319   | Layout 1 | `c9c230702f49`  |
| 2313   | Layout 1 | `c9c230702f49`  |
| 2308   | Layout 1 | `c9c230702f49`  |
| 2302   | Layout 1 | `c9c230702f49`  |
| 2295   | Layout 1 | `c9c230702f49`  |
| 2290   | Layout 1 | `c9c230702f49`  |
| 2284   | Layout 1 | `c9c230702f49`  |
| 2276   | Layout 1 | `c9c230702f49`  |
| 2269   | Layout 1 | `c9c230702f49`  |
| 2259   | Layout 1 | `c9c230702f49`  |
| 2250   | Layout 1 | `c9c230702f49`  |
| 2243   | Layout 1 | `c9c230702f49`  |
| 2235   | Layout 1 | `c9c230702f49`  |
| 2229   | Layout 1 | `c9c230702f49`  |
| 2224   | Layout 1 | `c9c230702f49`  |
| 2218   | Layout 1 | `c9c230702f49`  |
| 2215   | Layout 1 | `c9c230702f49`  |
| 2207   | Layout 1 | `c9c230702f49`  |
| 2203   | Layout 1 | `c9c230702f49`  |
| 2196   | Layout 1 | `c9c230702f49`  |
| 2192   | Layout 1 | `c9c230702f49`  |
| 2189   | Layout 1 | `c9c230702f49`  |
| 2183   | Layout 1 | `c9c230702f49`  |
| 2179   | Layout 1 | `c9c230702f49`  |
| 2171   | Layout 1 | `c9c230702f49`  |
| 2163   | Layout 1 | `c9c230702f49`  |
| 2156   | Layout 1 | `c9c230702f49`  |
| 2151   | Layout 1 | `c9c230702f49`  |
| 2147   | Layout 1 | `c9c230702f49`  |
| 2142   | Layout 1 | `c9c230702f49`  |
| 2138   | Layout 1 | `c9c230702f49`  |
| 2134   | Layout 1 | `c9c230702f49`  |
| 2130   | Layout 1 | `c9c230702f49`  |
| 2122   | Layout 1 | `c9c230702f49`  |
| 2107   | Layout 1 | `c9c230702f49`  |
| 2098   | Layout 1 | `c9c230702f49`  |
| 2089   | Layout 1 | `c9c230702f49`  |
| 2081   | Layout 1 | `c9c230702f49`  |
| 2073   | Layout 1 | `c9c230702f49`  |
| 2067   | Layout 1 | `c9c230702f49`  |
| 2063   | Layout 1 | `c9c230702f49`  |
| 2059   | Layout 1 | `c9c230702f49`  |
| 2052   | Layout 1 | `c9c230702f49`  |
| 2044   | Layout 1 | `c9c230702f49`  |
| 2039   | Layout 1 | `c9c230702f49`  |
| 2032   | Layout 1 | `c9c230702f49`  |
| 2025   | Layout 1 | `c9c230702f49`  |
| 2011   | Layout 1 | `c9c230702f49`  |
| 2005   | Layout 1 | `c9c230702f49`  |
| 2000   | Layout 1 | `c9c230702f49`  |
| 1996   | Layout 1 | `c9c230702f49`  |
| 1991   | Layout 1 | `c9c230702f49`  |
| 1985   | Layout 1 | `c9c230702f49`  |
| 1980   | Layout 1 | `c9c230702f49`  |
| 1969   | Layout 1 | `c9c230702f49`  |
| 1964   | Layout 1 | `c9c230702f49`  |
| 1958   | Layout 1 | `c9c230702f49`  |
| 1950   | Layout 1 | `c9c230702f49`  |
| 1945   | Layout 1 | `c9c230702f49`  |
| 1937   | Layout 1 | `c9c230702f49`  |
| 1933   | Layout 1 | `c9c230702f49`  |
| 1927   | Layout 1 | `c9c230702f49`  |
| 1921   | Layout 1 | `c9c230702f49`  |
| 1914   | Layout 1 | `c9c230702f49`  |
| 1908   | Layout 1 | `c9c230702f49`  |
| 1897   | Layout 1 | `c9c230702f49`  |
| 1892   | Layout 1 | `c9c230702f49`  |
| 1886   | Layout 1 | `c9c230702f49`  |
| 1881   | Layout 1 | `c9c230702f49`  |
| 1871   | Layout 1 | `c9c230702f49`  |
| 1866   | Layout 1 | `c9c230702f49`  |
| 1862   | Layout 1 | `c9c230702f49`  |
| 1854   | Layout 1 | `c9c230702f49`  |
| 1846   | Layout 1 | `c9c230702f49`  |
| 1838   | Layout 1 | `c9c230702f49`  |
| 1832   | Layout 1 | `c9c230702f49`  |
| 1826   | Layout 1 | `c9c230702f49`  |
| 1822   | Layout 1 | `c9c230702f49`  |
| 1818   | Layout 1 | `c9c230702f49`  |
| 1804   | Layout 1 | `c9c230702f49`  |
| 1794   | Layout 1 | `c9c230702f49`  |
| 1790   | Layout 1 | `c9c230702f49`  |
| 1784   | Layout 1 | `c9c230702f49`  |
| 1774   | Layout 1 | `c9c230702f49`  |
| 1771   | Layout 1 | `c9c230702f49`  |
| 1762   | Layout 1 | `c9c230702f49`  |
| 1759   | Layout 1 | `c9c230702f49`  |
| 1754   | Layout 1 | `c9c230702f49`  |
| 1749   | Layout 1 | `c9c230702f49`  |
| 1743   | Layout 1 | `c9c230702f49`  |
| 1737   | Layout 1 | `c9c230702f49`  |
| 1731   | Layout 1 | `c9c230702f49`  |
| 1725   | Layout 1 | `c9c230702f49`  |
| 1717   | Layout 1 | `c9c230702f49`  |
| 1710   | Layout 1 | `c9c230702f49`  |
| 1704   | Layout 1 | `c9c230702f49`  |
| 1698   | Layout 1 | `c9c230702f49`  |
| 1690   | Layout 1 | `c9c230702f49`  |
| 1685   | Layout 1 | `c9c230702f49`  |
| 1680   | Layout 1 | `c9c230702f49`  |
| 1674   | Layout 1 | `c9c230702f49`  |
| 1668   | Layout 1 | `c9c230702f49`  |
| 1659   | Layout 1 | `c9c230702f49`  |
| 1649   | Layout 1 | `c9c230702f49`  |
| 1642   | Layout 1 | `c9c230702f49`  |
| 1636   | Layout 1 | `c9c230702f49`  |
| 1628   | Layout 1 | `c9c230702f49`  |
| 1622   | Layout 1 | `c9c230702f49`  |
| 1614   | Layout 1 | `c9c230702f49`  |
| 1608   | Layout 1 | `c9c230702f49`  |
| 1602   | Layout 1 | `c9c230702f49`  |
| 1598   | Layout 1 | `c9c230702f49`  |
| 1594   | Layout 1 | `c9c230702f49`  |
| 1590   | Layout 1 | `c9c230702f49`  |
| 1587   | Layout 1 | `c9c230702f49`  |
| 1584   | Layout 1 | `c9c230702f49`  |
| 1579   | Layout 1 | `c9c230702f49`  |
| 1572   | Layout 1 | `c9c230702f49`  |
| 1565   | Layout 1 | `c9c230702f49`  |
| 1559   | Layout 1 | `c9c230702f49`  |
| 1554   | Layout 1 | `c9c230702f49`  |
| 1547   | Layout 1 | `c9c230702f49`  |
| 1537   | Layout 1 | `c9c230702f49`  |
| 1529   | Layout 1 | `c9c230702f49`  |
| 1524   | Layout 1 | `c9c230702f49`  |
| 1519   | Layout 1 | `c9c230702f49`  |
| 1509   | Layout 1 | `c9c230702f49`  |
| 1506   | Layout 1 | `c9c230702f49`  |
| 1504   | Layout 1 | `c9c230702f49`  |
| 1500   | Layout 1 | `c9c230702f49`  |
| 1493   | Layout 1 | `c9c230702f49`  |
| 1489   | Layout 1 | `c9c230702f49`  |
| 1485   | Layout 1 | `c9c230702f49`  |
| 1481   | Layout 1 | `c9c230702f49`  |
| 1474   | Layout 1 | `c9c230702f49`  |
| 1466   | Layout 1 | `c9c230702f49`  |
| 1462   | Layout 1 | `c9c230702f49`  |
| 1459   | Layout 1 | `c9c230702f49`  |
| 1453   | Layout 1 | `c9c230702f49`  |
| 1450   | Layout 1 | `c9c230702f49`  |
| 1445   | Layout 1 | `c9c230702f49`  |
| 1439   | Layout 1 | `c9c230702f49`  |
| 1433   | Layout 1 | `c9c230702f49`  |
| 1430   | Layout 1 | `c9c230702f49`  |
| 1426   | Layout 1 | `c9c230702f49`  |
| 1421   | Layout 1 | `c9c230702f49`  |
| 1417   | No file  | `c9c230702f49`  |
| 1416   | No file  | `c9c230702f49`  |
| 1409   | No file  | `c9c230702f49`  |
| 1405   | No file  | `c9c230702f49`  |
| 1401   | No file  | `c9c230702f49`  |
| 1396   | No file  | `c9c230702f49`  |
| 1391   | No file  | `c9c230702f49`  |
| 1390   | No file  | `c9c230702f49`  |
| 1386   | No file  | `c9c230702f49`  |
| 1381   | No file  | `c9c230702f49`  |
| 1379   | No file  | `c9c230702f49`  |
| 1372   | No file  | `c9c230702f49`  |
| 1366   | No file  | `c9c230702f49`  |
| 1364   | No file  | `c9c230702f49`  |
| 1363   | No file  | `c9c230702f49`  |
| 1360   | No file  | `c9c230702f49`  |
| 1358   | No file  | `c9c230702f49`  |
| 1355   | No file  | `c9c230702f49`  |
| 1351   | No file  | `c9c230702f49`  |
| 1348   | No file  | `c9c230702f49`  |
| 1346   | No file  | `c9c230702f49`  |
| 1341   | No file  | `c9c230702f49`  |
| 1340   | No file  | `c9c230702f49`  |
| 1338   | No file  | `c9c230702f49`  |
| 1335   | No file  | `c9c230702f49`  |
| 1333   | No file  | `c9c230702f49`  |
| 1329   | No file  | `c9c230702f49`  |
| 1327   | No file  | `c9c230702f49`  |
| 1324   | No file  | `c9c230702f49`  |
| 1321   | No file  | `c9c230702f49`  |
| 1319   | No file  | `c9c230702f49`  |
| 1318   | No file  | `c9c230702f49`  |
| 1316   | No file  | `c9c230702f49`  |
| 1313   | No file  | `c9c230702f49`  |
| 1311   | No file  | `c9c230702f49`  |
| 1309   | No file  | `c9c230702f49`  |
| 1304   | No file  | `c9c230702f49`  |
| 1292   | No file  | `c9c230702f49`  |
| 1286   | No file  | `c9c230702f49`  |
| 1280   | No file  | `c9c230702f49`  |
| 1276   | No file  | `c9c230702f49`  |
| 1267   | No file  | `c9c230702f49`  |
| 1261   | No file  | `c9c230702f49`  |
| 1256   | No file  | `c9c230702f49`  |
| 1250   | No file  | `c9c230702f49`  |
| 1246   | No file  | `c9c230702f49`  |
| 1239   | No file  | `c9c230702f49`  |
| 1230   | No file  | `c9c230702f49`  |
| 1226   | No file  | `c9c230702f49`  |
| 1220   | No file  | `c9c230702f49`  |
| 1217   | No file  | `c9c230702f49`  |
| 1211   | No file  | `c9c230702f49`  |
| 1210   | No file  | `c9c230702f49`  |
| 1208   | No file  | `c9c230702f49`  |
| 1203   | No file  | `c9c230702f49`  |
| 1197   | No file  | `c9c230702f49`  |
| 1194   | No file  | `c9c230702f49`  |
| 1192   | No file  | `c9c230702f49`  |
| 1187   | No file  | `c9c230702f49`  |
| 1183   | No file  | `c9c230702f49`  |
| 1177   | No file  | `c9c230702f49`  |
| 1173   | No file  | `c9c230702f49`  |
| 1167   | No file  | `c9c230702f49`  |
| 1164   | No file  | `c9c230702f49`  |
| 1156   | No file  | `c9c230702f49`  |
| 1149   | No file  | `c9c230702f49`  |
| 1144   | No file  | `c9c230702f49`  |
| 1137   | No file  | `c9c230702f49`  |
| 1132   | No file  | `c9c230702f49`  |
| 1127   | No file  | `c9c230702f49`  |
| 1122   | No file  | `c9c230702f49`  |
| 1118   | No file  | `c9c230702f49`  |
| 1114   | No file  | `c9c230702f49`  |
| 1109   | No file  | `c9c230702f49`  |
| 1102   | No file  | `c9c230702f49`  |
| 1096   | No file  | `c9c230702f49`  |
| 1088   | No file  | `c9c230702f49`  |
| 1081   | No file  | `c9c230702f49`  |
| 1076   | No file  | `c9c230702f49`  |
| 1069   | No file  | `c9c230702f49`  |
| 1064   | No file  | `c9c230702f49`  |
| 1058   | No file  | `c9c230702f49`  |
| 1051   | No file  | `c9c230702f49`  |
| 1044   | No file  | `c9c230702f49`  |
| 1036   | No file  | `c9c230702f49`  |
| 1026   | No file  | `c9c230702f49`  |
| 1016   | No file  | `c9c230702f49`  |
| 1009   | No file  | `c9c230702f49`  |
| 1005   | No file  | `c9c230702f49`  |
| 1000   | No file  | `c9c230702f49`  |
| 998    | No file  | `c9c230702f49`  |
| 990    | No file  | `c9c230702f49`  |
| 979    | No file  | `c9c230702f49`  |
| 972    | No file  | `c9c230702f49`  |
| 963    | No file  | `c9c230702f49`  |
| 955    | No file  | `c9c230702f49`  |
| 946    | No file  | `c9c230702f49`  |
| 938    | No file  | `c9c230702f49`  |
| 927    | No file  | `c9c230702f49`  |
| 911    | No file  | `c9c230702f49`  |
| 904    | No file  | `c9c230702f49`  |
| 899    | No file  | `c9c230702f49`  |
| 894    | No file  | `c9c230702f49`  |
| 885    | No file  | `c9c230702f49`  |
| 879    | No file  | `c9c230702f49`  |
| 872    | No file  | `c9c230702f49`  |
| 864    | No file  | `c9c230702f49`  |
| 855    | No file  | `c9c230702f49`  |
| 853    | No file  | `c9c230702f49`  |
| 845    | No file  | `c9c230702f49`  |
| 837    | No file  | `c9c230702f49`  |
| 829    | No file  | `c9c230702f49`  |
| 822    | No file  | `c9c230702f49`  |
| 814    | No file  | `c9c230702f49`  |
| 805    | No file  | `c9c230702f49`  |
| 794    | No file  | `c9c230702f49`  |
| 787    | No file  | `c9c230702f49`  |
| 780    | No file  | `c9c230702f49`  |
| 771    | No file  | `c9c230702f49`  |
| 760    | No file  | `c9c230702f49`  |
| 748    | No file  | `c9c230702f49`  |
| 741    | No file  | `c9c230702f49`  |
| 736    | No file  | `c9c230702f49`  |
| 731    | No file  | `c9c230702f49`  |
| 723    | No file  | `c9c230702f49`  |
| 711    | No file  | `c9c230702f49`  |
| 707    | No file  | `c9c230702f49`  |
| 697    | No file  | `c9c230702f49`  |
| 689    | No file  | `c9c230702f49`  |
| 683    | No file  | `c9c230702f49`  |
| 678    | No file  | `c9c230702f49`  |
| 670    | No file  | `c9c230702f49`  |
| 661    | No file  | `c9c230702f49`  |
| 656    | No file  | `c9c230702f49`  |
| 652    | No file  | `c9c230702f49`  |
| 643    | No file  | `c9c230702f49`  |
| 637    | No file  | `c9c230702f49`  |
| 630    | No file  | `c9c230702f49`  |
| 627    | No file  | `c9c230702f49`  |
| 621    | No file  | `c9c230702f49`  |
| 617    | No file  | `c9c230702f49`  |
| 615    | No file  | `c9c230702f49`  |
| 606    | No file  | `c9c230702f49`  |
| 599    | No file  | `c9c230702f49`  |
| 592    | No file  | `c9c230702f49`  |
| 586    | No file  | `c9c230702f49`  |
| 577    | No file  | `c9c230702f49`  |
| 569    | No file  | `c9c230702f49`  |
| 561    | No file  | `c9c230702f49`  |
| 554    | No file  | `c9c230702f49`  |
| 542    | No file  | `c9c230702f49`  |
| 532    | No file  | `c9c230702f49`  |
| 531    | No file  | `c9c230702f49`  |
| 526    | No file  | `c9c230702f49`  |
| 521    | No file  | `c9c230702f49`  |
| 517    | No file  | `c9c230702f49`  |
| 510    | No file  | `c9c230702f49`  |
| 508    | No file  | `c9c230702f49`  |
| 504    | No file  | `c9c230702f49`  |
| 497    | No file  | `c9c230702f49`  |
| 491    | No file  | `c9c230702f49`  |
| 485    | No file  | `c9c230702f49`  |
| 478    | No file  | `c9c230702f49`  |
| 472    | No file  | `c9c230702f49`  |
| 466    | No file  | `c9c230702f49`  |
| 457    | No file  | `c9c230702f49`  |
| 452    | No file  | `c9c230702f49`  |
| 449    | No file  | `c9c230702f49`  |
| 435    | No file  | `c9c230702f49`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                       |
| --------------------- | -------- | -------------------------- |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 6 bytes + flags)

| Offset  | Type            | Field          | Notes                                                                                  |
| ------- | --------------- | -------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u16             | guild_skill_no | Skill number of a [guildskill](guildskill_bss.md) row; the handler shows its LOC type 10 name |
| `+0x02` | u32             | grade_count    | Number of flags, one per member grade; `11` on client 3474, `8` on 1784                |
| `+0x06` | u8[grade_count] | grade          | `1` when member grade `N` (the flag's position) may use the skill; see [guildright](guildright_bss.md#grades) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names follow the `GuildSpecialSkillRight_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784: `GuildSkillNo` and `Grade`, the
grade numbers whose flag is set (4 of 4 rows match the client 1784 file).
The sheet's third column, `ContentsGroupKey` (`1503` and `1648`), is not in
the file. Every skill number is a guild skill: all 8 are rows of
[guildskill](guildskill_bss.md) on client 3474.

## Notes

- Client 1784 has the first four skills with grades `0` and `6` (8 flags).
  Client 3002 sets `0`, `6`, `8` and `9` of 11 flags on the same four, and
  client 3251 adds the other four (62845 to 62848).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`: the skill, its name and the set
  grade numbers.
