# `arshasetlostregion.bss` Format

## Purpose

The stages of the Arena of Arsha shrinking zone, the game rule the host
turns on with `ToClient_RequestArshaLostRegionMode(true)`
(`panel_window_arsha_func_all`). One row per stage: the stage index, an
unnamed count, a point and two distances that read as the zone's centre and
its start and end radius, and the skill the zone applies,
`41292` 아르샤의 창: 자기장 디버프(초당 -500) ("Arena of Arsha: magnetic
field debuff, -500 per second"). On client 3474 the file has 3 stages.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------ | ----- | ------- | --------- |
| 1      | 1554 and later | `arshasetlostregion.bss` | 110   | 3 Row   | 30        |

| Layout | File                     | Known        | Unknown      |
| ------ | ------------------------ | ------------ | ------------ |
| 1      | `arshasetlostregion.bss` | 38 B (34.5%) | 72 B (65.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `affb52d874df`  |
| 3482   | Layout 1 | `affb52d874df`  |
| 3474   | Layout 1 | `affb52d874df`  |
| 3473   | Layout 1 | `affb52d874df`  |
| 3464   | Layout 1 | `affb52d874df`  |
| 3458   | Layout 1 | `affb52d874df`  |
| 3454   | Layout 1 | `affb52d874df`  |
| 3444   | Layout 1 | `affb52d874df`  |
| 3435   | Layout 1 | `affb52d874df`  |
| 3426   | Layout 1 | `affb52d874df`  |
| 3418   | Layout 1 | `affb52d874df`  |
| 3412   | Layout 1 | `affb52d874df`  |
| 3402   | Layout 1 | `affb52d874df`  |
| 3396   | Layout 1 | `affb52d874df`  |
| 3387   | Layout 1 | `affb52d874df`  |
| 3381   | Layout 1 | `affb52d874df`  |
| 3373   | Layout 1 | `affb52d874df`  |
| 3364   | Layout 1 | `affb52d874df`  |
| 3356   | Layout 1 | `affb52d874df`  |
| 3349   | Layout 1 | `affb52d874df`  |
| 3342   | Layout 1 | `affb52d874df`  |
| 3335   | Layout 1 | `affb52d874df`  |
| 3326   | Layout 1 | `affb52d874df`  |
| 3321   | Layout 1 | `affb52d874df`  |
| 3314   | Layout 1 | `affb52d874df`  |
| 3303   | Layout 1 | `affb52d874df`  |
| 3302   | Layout 1 | `affb52d874df`  |
| 3293   | Layout 1 | `affb52d874df`  |
| 3283   | Layout 1 | `affb52d874df`  |
| 3275   | Layout 1 | `affb52d874df`  |
| 3267   | Layout 1 | `affb52d874df`  |
| 3258   | Layout 1 | `affb52d874df`  |
| 3251   | Layout 1 | `affb52d874df`  |
| 3242   | Layout 1 | `affb52d874df`  |
| 3235   | Layout 1 | `affb52d874df`  |
| 3229   | Layout 1 | `affb52d874df`  |
| 3212   | Layout 1 | `affb52d874df`  |
| 3203   | Layout 1 | `affb52d874df`  |
| 3193   | Layout 1 | `affb52d874df`  |
| 3186   | Layout 1 | `affb52d874df`  |
| 3177   | Layout 1 | `affb52d874df`  |
| 3169   | Layout 1 | `affb52d874df`  |
| 3158   | Layout 1 | `affb52d874df`  |
| 3151   | Layout 1 | `affb52d874df`  |
| 3144   | Layout 1 | `affb52d874df`  |
| 3133   | Layout 1 | `affb52d874df`  |
| 3125   | Layout 1 | `affb52d874df`  |
| 3118   | Layout 1 | `affb52d874df`  |
| 3111   | Layout 1 | `affb52d874df`  |
| 3103   | Layout 1 | `affb52d874df`  |
| 3095   | Layout 1 | `affb52d874df`  |
| 3086   | Layout 1 | `affb52d874df`  |
| 3072   | Layout 1 | `affb52d874df`  |
| 3062   | Layout 1 | `affb52d874df`  |
| 3052   | Layout 1 | `affb52d874df`  |
| 3045   | Layout 1 | `affb52d874df`  |
| 3037   | Layout 1 | `affb52d874df`  |
| 3030   | Layout 1 | `affb52d874df`  |
| 3021   | Layout 1 | `affb52d874df`  |
| 3012   | Layout 1 | `affb52d874df`  |
| 3002   | Layout 1 | `affb52d874df`  |
| 2995   | Layout 1 | `affb52d874df`  |
| 2987   | Layout 1 | `affb52d874df`  |
| 2978   | Layout 1 | `affb52d874df`  |
| 2970   | Layout 1 | `affb52d874df`  |
| 2959   | Layout 1 | `affb52d874df`  |
| 2951   | Layout 1 | `affb52d874df`  |
| 2942   | Layout 1 | `affb52d874df`  |
| 2935   | Layout 1 | `affb52d874df`  |
| 2932   | Layout 1 | `affb52d874df`  |
| 2923   | Layout 1 | `affb52d874df`  |
| 2919   | Layout 1 | `affb52d874df`  |
| 2907   | Layout 1 | `affb52d874df`  |
| 2900   | Layout 1 | `affb52d874df`  |
| 2891   | Layout 1 | `affb52d874df`  |
| 2882   | Layout 1 | `affb52d874df`  |
| 2872   | Layout 1 | `affb52d874df`  |
| 2863   | Layout 1 | `affb52d874df`  |
| 2855   | Layout 1 | `affb52d874df`  |
| 2849   | Layout 1 | `affb52d874df`  |
| 2844   | Layout 1 | `affb52d874df`  |
| 2834   | Layout 1 | `affb52d874df`  |
| 2825   | Layout 1 | `affb52d874df`  |
| 2819   | Layout 1 | `affb52d874df`  |
| 2811   | Layout 1 | `affb52d874df`  |
| 2803   | Layout 1 | `affb52d874df`  |
| 2794   | Layout 1 | `affb52d874df`  |
| 2783   | Layout 1 | `affb52d874df`  |
| 2774   | Layout 1 | `affb52d874df`  |
| 2765   | Layout 1 | `affb52d874df`  |
| 2756   | Layout 1 | `affb52d874df`  |
| 2750   | Layout 1 | `affb52d874df`  |
| 2743   | Layout 1 | `affb52d874df`  |
| 2736   | Layout 1 | `affb52d874df`  |
| 2726   | Layout 1 | `affb52d874df`  |
| 2717   | Layout 1 | `affb52d874df`  |
| 2709   | Layout 1 | `affb52d874df`  |
| 2703   | Layout 1 | `affb52d874df`  |
| 2695   | Layout 1 | `affb52d874df`  |
| 2684   | Layout 1 | `affb52d874df`  |
| 2672   | Layout 1 | `affb52d874df`  |
| 2665   | Layout 1 | `affb52d874df`  |
| 2657   | Layout 1 | `affb52d874df`  |
| 2649   | Layout 1 | `affb52d874df`  |
| 2644   | Layout 1 | `affb52d874df`  |
| 2637   | Layout 1 | `affb52d874df`  |
| 2629   | Layout 1 | `affb52d874df`  |
| 2619   | Layout 1 | `affb52d874df`  |
| 2612   | Layout 1 | `affb52d874df`  |
| 2606   | Layout 1 | `affb52d874df`  |
| 2602   | Layout 1 | `affb52d874df`  |
| 2601   | Layout 1 | `affb52d874df`  |
| 2592   | Layout 1 | `affb52d874df`  |
| 2583   | Layout 1 | `affb52d874df`  |
| 2575   | Layout 1 | `affb52d874df`  |
| 2567   | Layout 1 | `affb52d874df`  |
| 2560   | Layout 1 | `affb52d874df`  |
| 2553   | Layout 1 | `affb52d874df`  |
| 2545   | Layout 1 | `affb52d874df`  |
| 2538   | Layout 1 | `affb52d874df`  |
| 2529   | Layout 1 | `affb52d874df`  |
| 2519   | Layout 1 | `affb52d874df`  |
| 2513   | Layout 1 | `affb52d874df`  |
| 2510   | Layout 1 | `affb52d874df`  |
| 2507   | Layout 1 | `affb52d874df`  |
| 2503   | Layout 1 | `affb52d874df`  |
| 2498   | Layout 1 | `affb52d874df`  |
| 2492   | Layout 1 | `affb52d874df`  |
| 2487   | Layout 1 | `affb52d874df`  |
| 2480   | Layout 1 | `affb52d874df`  |
| 2474   | Layout 1 | `affb52d874df`  |
| 2468   | Layout 1 | `affb52d874df`  |
| 2460   | Layout 1 | `affb52d874df`  |
| 2453   | Layout 1 | `affb52d874df`  |
| 2444   | Layout 1 | `affb52d874df`  |
| 2438   | Layout 1 | `affb52d874df`  |
| 2434   | Layout 1 | `affb52d874df`  |
| 2429   | Layout 1 | `affb52d874df`  |
| 2421   | Layout 1 | `affb52d874df`  |
| 2414   | Layout 1 | `affb52d874df`  |
| 2407   | Layout 1 | `affb52d874df`  |
| 2401   | Layout 1 | `affb52d874df`  |
| 2397   | Layout 1 | `affb52d874df`  |
| 2393   | Layout 1 | `affb52d874df`  |
| 2384   | Layout 1 | `affb52d874df`  |
| 2378   | Layout 1 | `affb52d874df`  |
| 2372   | Layout 1 | `affb52d874df`  |
| 2358   | Layout 1 | `affb52d874df`  |
| 2352   | Layout 1 | `affb52d874df`  |
| 2347   | Layout 1 | `affb52d874df`  |
| 2343   | Layout 1 | `affb52d874df`  |
| 2335   | Layout 1 | `affb52d874df`  |
| 2327   | Layout 1 | `affb52d874df`  |
| 2324   | Layout 1 | `affb52d874df`  |
| 2319   | Layout 1 | `affb52d874df`  |
| 2313   | Layout 1 | `affb52d874df`  |
| 2308   | Layout 1 | `affb52d874df`  |
| 2302   | Layout 1 | `affb52d874df`  |
| 2295   | Layout 1 | `affb52d874df`  |
| 2290   | Layout 1 | `affb52d874df`  |
| 2284   | Layout 1 | `affb52d874df`  |
| 2276   | Layout 1 | `affb52d874df`  |
| 2269   | Layout 1 | `affb52d874df`  |
| 2259   | Layout 1 | `affb52d874df`  |
| 2250   | Layout 1 | `affb52d874df`  |
| 2243   | Layout 1 | `affb52d874df`  |
| 2235   | Layout 1 | `affb52d874df`  |
| 2229   | Layout 1 | `affb52d874df`  |
| 2224   | Layout 1 | `affb52d874df`  |
| 2218   | Layout 1 | `affb52d874df`  |
| 2215   | Layout 1 | `affb52d874df`  |
| 2207   | Layout 1 | `affb52d874df`  |
| 2203   | Layout 1 | `affb52d874df`  |
| 2196   | Layout 1 | `affb52d874df`  |
| 2192   | Layout 1 | `affb52d874df`  |
| 2189   | Layout 1 | `affb52d874df`  |
| 2183   | Layout 1 | `affb52d874df`  |
| 2179   | Layout 1 | `affb52d874df`  |
| 2171   | Layout 1 | `affb52d874df`  |
| 2163   | Layout 1 | `affb52d874df`  |
| 2156   | Layout 1 | `affb52d874df`  |
| 2151   | Layout 1 | `affb52d874df`  |
| 2147   | Layout 1 | `affb52d874df`  |
| 2142   | Layout 1 | `affb52d874df`  |
| 2138   | Layout 1 | `affb52d874df`  |
| 2134   | Layout 1 | `affb52d874df`  |
| 2130   | Layout 1 | `affb52d874df`  |
| 2122   | Layout 1 | `affb52d874df`  |
| 2107   | Layout 1 | `affb52d874df`  |
| 2098   | Layout 1 | `affb52d874df`  |
| 2089   | Layout 1 | `affb52d874df`  |
| 2081   | Layout 1 | `affb52d874df`  |
| 2073   | Layout 1 | `affb52d874df`  |
| 2067   | Layout 1 | `affb52d874df`  |
| 2063   | Layout 1 | `affb52d874df`  |
| 2059   | Layout 1 | `affb52d874df`  |
| 2052   | Layout 1 | `affb52d874df`  |
| 2044   | Layout 1 | `affb52d874df`  |
| 2039   | Layout 1 | `affb52d874df`  |
| 2032   | Layout 1 | `affb52d874df`  |
| 2025   | Layout 1 | `affb52d874df`  |
| 2011   | Layout 1 | `affb52d874df`  |
| 2005   | Layout 1 | `affb52d874df`  |
| 2000   | Layout 1 | `affb52d874df`  |
| 1996   | Layout 1 | `affb52d874df`  |
| 1991   | Layout 1 | `affb52d874df`  |
| 1985   | Layout 1 | `affb52d874df`  |
| 1980   | Layout 1 | `affb52d874df`  |
| 1969   | Layout 1 | `affb52d874df`  |
| 1964   | Layout 1 | `affb52d874df`  |
| 1958   | Layout 1 | `affb52d874df`  |
| 1950   | Layout 1 | `affb52d874df`  |
| 1945   | Layout 1 | `affb52d874df`  |
| 1937   | Layout 1 | `affb52d874df`  |
| 1933   | Layout 1 | `affb52d874df`  |
| 1927   | Layout 1 | `affb52d874df`  |
| 1921   | Layout 1 | `affb52d874df`  |
| 1914   | Layout 1 | `affb52d874df`  |
| 1908   | Layout 1 | `affb52d874df`  |
| 1897   | Layout 1 | `affb52d874df`  |
| 1892   | Layout 1 | `affb52d874df`  |
| 1886   | Layout 1 | `affb52d874df`  |
| 1881   | Layout 1 | `affb52d874df`  |
| 1871   | Layout 1 | `affb52d874df`  |
| 1866   | Layout 1 | `affb52d874df`  |
| 1862   | Layout 1 | `affb52d874df`  |
| 1854   | Layout 1 | `affb52d874df`  |
| 1846   | Layout 1 | `affb52d874df`  |
| 1838   | Layout 1 | `affb52d874df`  |
| 1832   | Layout 1 | `affb52d874df`  |
| 1826   | Layout 1 | `affb52d874df`  |
| 1822   | Layout 1 | `affb52d874df`  |
| 1818   | Layout 1 | `affb52d874df`  |
| 1804   | Layout 1 | `affb52d874df`  |
| 1794   | Layout 1 | `affb52d874df`  |
| 1790   | Layout 1 | `affb52d874df`  |
| 1784   | Layout 1 | `affb52d874df`  |
| 1774   | Layout 1 | `affb52d874df`  |
| 1771   | Layout 1 | `affb52d874df`  |
| 1762   | Layout 1 | `affb52d874df`  |
| 1759   | Layout 1 | `affb52d874df`  |
| 1754   | Layout 1 | `affb52d874df`  |
| 1749   | Layout 1 | `affb52d874df`  |
| 1743   | Layout 1 | `affb52d874df`  |
| 1737   | Layout 1 | `affb52d874df`  |
| 1731   | Layout 1 | `affb52d874df`  |
| 1725   | Layout 1 | `affb52d874df`  |
| 1717   | Layout 1 | `affb52d874df`  |
| 1710   | Layout 1 | `affb52d874df`  |
| 1704   | Layout 1 | `affb52d874df`  |
| 1698   | Layout 1 | `affb52d874df`  |
| 1690   | Layout 1 | `affb52d874df`  |
| 1685   | Layout 1 | `affb52d874df`  |
| 1680   | Layout 1 | `affb52d874df`  |
| 1674   | Layout 1 | `affb52d874df`  |
| 1668   | Layout 1 | `affb52d874df`  |
| 1659   | Layout 1 | `affb52d874df`  |
| 1649   | Layout 1 | `affb52d874df`  |
| 1642   | Layout 1 | `affb52d874df`  |
| 1636   | Layout 1 | `affb52d874df`  |
| 1628   | Layout 1 | `affb52d874df`  |
| 1622   | Layout 1 | `affb52d874df`  |
| 1614   | Layout 1 | `affb52d874df`  |
| 1608   | Layout 1 | `affb52d874df`  |
| 1602   | Layout 1 | `affb52d874df`  |
| 1598   | Layout 1 | `affb52d874df`  |
| 1594   | Layout 1 | `affb52d874df`  |
| 1590   | Layout 1 | `affb52d874df`  |
| 1587   | Layout 1 | `affb52d874df`  |
| 1584   | Layout 1 | `affb52d874df`  |
| 1579   | Layout 1 | `affb52d874df`  |
| 1572   | Layout 1 | `affb52d874df`  |
| 1565   | Layout 1 | `affb52d874df`  |
| 1559   | Layout 1 | `affb52d874df`  |
| 1554   | Layout 1 | `affb52d874df`  |
| 1547   | No file  | `affb52d874df`  |
| 1537   | No file  | `affb52d874df`  |
| 1529   | No file  | `affb52d874df`  |
| 1524   | No file  | `affb52d874df`  |
| 1519   | No file  | `affb52d874df`  |
| 1509   | No file  | `affb52d874df`  |
| 1506   | No file  | `affb52d874df`  |
| 1504   | No file  | `affb52d874df`  |
| 1500   | No file  | `affb52d874df`  |
| 1493   | No file  | `affb52d874df`  |
| 1489   | No file  | `affb52d874df`  |
| 1485   | No file  | `affb52d874df`  |
| 1481   | No file  | `affb52d874df`  |
| 1474   | No file  | `affb52d874df`  |
| 1466   | No file  | `affb52d874df`  |
| 1462   | No file  | `affb52d874df`  |
| 1459   | No file  | `affb52d874df`  |
| 1453   | No file  | `affb52d874df`  |
| 1450   | No file  | `affb52d874df`  |
| 1445   | No file  | `affb52d874df`  |
| 1439   | No file  | `affb52d874df`  |
| 1433   | No file  | `affb52d874df`  |
| 1430   | No file  | `affb52d874df`  |
| 1426   | No file  | `affb52d874df`  |
| 1421   | No file  | `affb52d874df`  |
| 1417   | No file  | `affb52d874df`  |
| 1416   | No file  | `affb52d874df`  |
| 1409   | No file  | `affb52d874df`  |
| 1405   | No file  | `affb52d874df`  |
| 1401   | No file  | `affb52d874df`  |
| 1396   | No file  | `affb52d874df`  |
| 1391   | No file  | `affb52d874df`  |
| 1390   | No file  | `affb52d874df`  |
| 1386   | No file  | `affb52d874df`  |
| 1381   | No file  | `affb52d874df`  |
| 1379   | No file  | `affb52d874df`  |
| 1372   | No file  | `affb52d874df`  |
| 1366   | No file  | `affb52d874df`  |
| 1364   | No file  | `affb52d874df`  |
| 1363   | No file  | `affb52d874df`  |
| 1360   | No file  | `affb52d874df`  |
| 1358   | No file  | `affb52d874df`  |
| 1355   | No file  | `affb52d874df`  |
| 1351   | No file  | `affb52d874df`  |
| 1348   | No file  | `affb52d874df`  |
| 1346   | No file  | `affb52d874df`  |
| 1341   | No file  | `affb52d874df`  |
| 1340   | No file  | `affb52d874df`  |
| 1338   | No file  | `affb52d874df`  |
| 1335   | No file  | `affb52d874df`  |
| 1333   | No file  | `affb52d874df`  |
| 1329   | No file  | `affb52d874df`  |
| 1327   | No file  | `affb52d874df`  |
| 1324   | No file  | `affb52d874df`  |
| 1321   | No file  | `affb52d874df`  |
| 1319   | No file  | `affb52d874df`  |
| 1318   | No file  | `affb52d874df`  |
| 1316   | No file  | `affb52d874df`  |
| 1313   | No file  | `affb52d874df`  |
| 1311   | No file  | `affb52d874df`  |
| 1309   | No file  | `affb52d874df`  |
| 1304   | No file  | `affb52d874df`  |
| 1292   | No file  | `affb52d874df`  |
| 1286   | No file  | `affb52d874df`  |
| 1280   | No file  | `affb52d874df`  |
| 1276   | No file  | `affb52d874df`  |
| 1267   | No file  | `affb52d874df`  |
| 1261   | No file  | `affb52d874df`  |
| 1256   | No file  | `affb52d874df`  |
| 1250   | No file  | `affb52d874df`  |
| 1246   | No file  | `affb52d874df`  |
| 1239   | No file  | `affb52d874df`  |
| 1230   | No file  | `affb52d874df`  |
| 1226   | No file  | `affb52d874df`  |
| 1220   | No file  | `affb52d874df`  |
| 1217   | No file  | `affb52d874df`  |
| 1211   | No file  | `affb52d874df`  |
| 1210   | No file  | `affb52d874df`  |
| 1208   | No file  | `affb52d874df`  |
| 1203   | No file  | `affb52d874df`  |
| 1197   | No file  | `affb52d874df`  |
| 1194   | No file  | `affb52d874df`  |
| 1192   | No file  | `affb52d874df`  |
| 1187   | No file  | `affb52d874df`  |
| 1183   | No file  | `affb52d874df`  |
| 1177   | No file  | `affb52d874df`  |
| 1173   | No file  | `affb52d874df`  |
| 1167   | No file  | `affb52d874df`  |
| 1164   | No file  | `affb52d874df`  |
| 1156   | No file  | `affb52d874df`  |
| 1149   | No file  | `affb52d874df`  |
| 1144   | No file  | `affb52d874df`  |
| 1137   | No file  | `affb52d874df`  |
| 1132   | No file  | `affb52d874df`  |
| 1127   | No file  | `affb52d874df`  |
| 1122   | No file  | `affb52d874df`  |
| 1118   | No file  | `affb52d874df`  |
| 1114   | No file  | `affb52d874df`  |
| 1109   | No file  | `affb52d874df`  |
| 1102   | No file  | `affb52d874df`  |
| 1096   | No file  | `affb52d874df`  |
| 1088   | No file  | `affb52d874df`  |
| 1081   | No file  | `affb52d874df`  |
| 1076   | No file  | `affb52d874df`  |
| 1069   | No file  | `affb52d874df`  |
| 1064   | No file  | `affb52d874df`  |
| 1058   | No file  | `affb52d874df`  |
| 1051   | No file  | `affb52d874df`  |
| 1044   | No file  | `affb52d874df`  |
| 1036   | No file  | `affb52d874df`  |
| 1026   | No file  | `affb52d874df`  |
| 1016   | No file  | `affb52d874df`  |
| 1009   | No file  | `affb52d874df`  |
| 1005   | No file  | `affb52d874df`  |
| 1000   | No file  | `affb52d874df`  |
| 998    | No file  | `affb52d874df`  |
| 990    | No file  | `affb52d874df`  |
| 979    | No file  | `affb52d874df`  |
| 972    | No file  | `affb52d874df`  |
| 963    | No file  | `affb52d874df`  |
| 955    | No file  | `affb52d874df`  |
| 946    | No file  | `affb52d874df`  |
| 938    | No file  | `affb52d874df`  |
| 927    | No file  | `affb52d874df`  |
| 911    | No file  | `affb52d874df`  |
| 904    | No file  | `affb52d874df`  |
| 899    | No file  | `affb52d874df`  |
| 894    | No file  | `affb52d874df`  |
| 885    | No file  | `affb52d874df`  |
| 879    | No file  | `affb52d874df`  |
| 872    | No file  | `affb52d874df`  |
| 864    | No file  | `affb52d874df`  |
| 855    | No file  | `affb52d874df`  |
| 853    | No file  | `affb52d874df`  |
| 845    | No file  | `affb52d874df`  |
| 837    | No file  | `affb52d874df`  |
| 829    | No file  | `affb52d874df`  |
| 822    | No file  | `affb52d874df`  |
| 814    | No file  | `affb52d874df`  |
| 805    | No file  | `affb52d874df`  |
| 794    | No file  | `affb52d874df`  |
| 787    | No file  | `affb52d874df`  |
| 780    | No file  | `affb52d874df`  |
| 771    | No file  | `affb52d874df`  |
| 760    | No file  | `affb52d874df`  |
| 748    | No file  | `affb52d874df`  |
| 741    | No file  | `affb52d874df`  |
| 736    | No file  | `affb52d874df`  |
| 731    | No file  | `affb52d874df`  |
| 723    | No file  | `affb52d874df`  |
| 711    | No file  | `affb52d874df`  |
| 707    | No file  | `affb52d874df`  |
| 697    | No file  | `affb52d874df`  |
| 689    | No file  | `affb52d874df`  |
| 683    | No file  | `affb52d874df`  |
| 678    | No file  | `affb52d874df`  |
| 670    | No file  | `affb52d874df`  |
| 661    | No file  | `affb52d874df`  |
| 656    | No file  | `affb52d874df`  |
| 652    | No file  | `affb52d874df`  |
| 643    | No file  | `affb52d874df`  |
| 637    | No file  | `affb52d874df`  |
| 630    | No file  | `affb52d874df`  |
| 627    | No file  | `affb52d874df`  |
| 621    | No file  | `affb52d874df`  |
| 617    | No file  | `affb52d874df`  |
| 615    | No file  | `affb52d874df`  |
| 606    | No file  | `affb52d874df`  |
| 599    | No file  | `affb52d874df`  |
| 592    | No file  | `affb52d874df`  |
| 586    | No file  | `affb52d874df`  |
| 577    | No file  | `affb52d874df`  |
| 569    | No file  | `affb52d874df`  |
| 561    | No file  | `affb52d874df`  |
| 554    | No file  | `affb52d874df`  |
| 542    | No file  | `affb52d874df`  |
| 532    | No file  | `affb52d874df`  |
| 531    | No file  | `affb52d874df`  |
| 526    | No file  | `affb52d874df`  |
| 521    | No file  | `affb52d874df`  |
| 517    | No file  | `affb52d874df`  |
| 510    | No file  | `affb52d874df`  |
| 508    | No file  | `affb52d874df`  |
| 504    | No file  | `affb52d874df`  |
| 497    | No file  | `affb52d874df`  |
| 491    | No file  | `affb52d874df`  |
| 485    | No file  | `affb52d874df`  |
| 478    | No file  | `affb52d874df`  |
| 472    | No file  | `affb52d874df`  |
| 466    | No file  | `affb52d874df`  |
| 457    | No file  | `affb52d874df`  |
| 452    | No file  | `affb52d874df`  |
| 449    | No file  | `affb52d874df`  |
| 435    | No file  | `affb52d874df`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone; the skill's Korean name comes from
the `skilltype.dbss` lookup index the app loads at start.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of stages                              |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (30 bytes)

| Offset  | Type | Field      | Notes                                                                                  |
| ------- | ---- | ---------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u32  | index      | Stage, `1` to `3`; see Field Names                                                     |
| `+0x04` | u32  | unknown_04 | `170`, `120`, `60` by stage; see Open Questions                                        |
| `+0x08` | f32  | unknown_08 | `183634` on every row                                                                  |
| `+0x0C` | f32  | unknown_0c | `-5063` on every row                                                                   |
| `+0x10` | f32  | unknown_10 | `404400` on every row                                                                  |
| `+0x14` | f32  | unknown_14 | `4600`, `2100`, `1100` by stage; the next stage's `unknown_18`                         |
| `+0x18` | f32  | unknown_18 | `9000`, `4600`, `2100` by stage                                                        |
| `+0x1C` | u16  | skill_no   | `skilltype.dbss` skill number, `41292` on every row; the handler shows its Korean name |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The server executable of a private server on client 1784 loads the file
with `GameCommonParameterLoaderFromExcel::loadArshaSetLostRegion` into the
`ArshaSetLostRegionStaticStatusManager`, whose insert error names the row
key `[index]`; the stages count from `1`. The `LostRegion_Table` sheet of
that private server's `DataSheets.bexcel` belongs to the Shadow Arena and
has the columns `Index` and `Order` and one row, so no sheet column matches
the other fields. `skill_no` is a `skilltype.dbss` skill number whose
Korean name is the Arena of Arsha zone debuff. `41292` is also a
`buff.dbss` key (Morning Sun: AP -200), which does not fit the zone.

## Notes

- The file is 110 bytes and the same on clients 1784, 2107, 2519, 3002,
  3251 and 3474.
- `unknown_08`, `unknown_0c` and `unknown_10` are the same on every row and
  read as one x, y, z point in world units, `unknown_14` and `unknown_18` as
  the radius a stage ends at and starts from: each stage starts at the
  radius the previous one ended at (9000 to 4600, 4600 to 2100, 2100 to
  1100). `test_pvp_tables.py` checks that chain.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`.

## Open Questions

### Stage Time

What `unknown_04` counts. `170`, `120` and `60` fall by stage, which fits
the seconds a stage lasts or the time before the zone shrinks, but no Lua
reads the value.

### Zone Point and Radii

Whether `unknown_08` to `unknown_10` are the centre of the zone in the
Arena of Arsha and `unknown_14` and `unknown_18` its end and start radius.
The values fit that reading; no Lua or sheet names them.
