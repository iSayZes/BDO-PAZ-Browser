# `instancedungeoninfo.dbss` Format

## Purpose

The entry point of each instance dungeon: the field the dungeon runs in
(`field_no`, a `Field_Table` key), the world position a character enters
at and the direction it faces. The table holds 4 records on client 3474,
byte for byte the same as on client 1784. Companion
`instancedungeoninfooffset.dbss` lists where every record sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes | Records             | Row bytes |
| ------ | -------------- | -------------------------------- | ----- | ------------------- | --------- |
| 1      | 1276 and later | `instancedungeoninfo.dbss`       | 92    | 4 Dungeon Entry Row | 22        |
| 1      | 1276 and later | `instancedungeoninfooffset.dbss` | 52    | 4 Index Row         | 12        |

| Layout | File                             | Known         | Unknown    |
| ------ | -------------------------------- | ------------- | ---------- |
| 1      | `instancedungeoninfo.dbss`       | 92 B (100.0%) | 0 B (0.0%) |
| 1      | `instancedungeoninfooffset.dbss` | 52 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `59f27e42fd50`  |
| 3482   | Layout 1 | `59f27e42fd50`  |
| 3474   | Layout 1 | `59f27e42fd50`  |
| 3473   | Layout 1 | `59f27e42fd50`  |
| 3464   | Layout 1 | `59f27e42fd50`  |
| 3458   | Layout 1 | `59f27e42fd50`  |
| 3454   | Layout 1 | `59f27e42fd50`  |
| 3444   | Layout 1 | `59f27e42fd50`  |
| 3435   | Layout 1 | `59f27e42fd50`  |
| 3426   | Layout 1 | `59f27e42fd50`  |
| 3418   | Layout 1 | `59f27e42fd50`  |
| 3412   | Layout 1 | `59f27e42fd50`  |
| 3402   | Layout 1 | `59f27e42fd50`  |
| 3396   | Layout 1 | `59f27e42fd50`  |
| 3387   | Layout 1 | `59f27e42fd50`  |
| 3381   | Layout 1 | `59f27e42fd50`  |
| 3373   | Layout 1 | `59f27e42fd50`  |
| 3364   | Layout 1 | `59f27e42fd50`  |
| 3356   | Layout 1 | `59f27e42fd50`  |
| 3349   | Layout 1 | `59f27e42fd50`  |
| 3342   | Layout 1 | `59f27e42fd50`  |
| 3335   | Layout 1 | `59f27e42fd50`  |
| 3326   | Layout 1 | `59f27e42fd50`  |
| 3321   | Layout 1 | `59f27e42fd50`  |
| 3314   | Layout 1 | `59f27e42fd50`  |
| 3303   | Layout 1 | `59f27e42fd50`  |
| 3302   | Layout 1 | `59f27e42fd50`  |
| 3293   | Layout 1 | `59f27e42fd50`  |
| 3283   | Layout 1 | `59f27e42fd50`  |
| 3275   | Layout 1 | `59f27e42fd50`  |
| 3267   | Layout 1 | `59f27e42fd50`  |
| 3258   | Layout 1 | `59f27e42fd50`  |
| 3251   | Layout 1 | `59f27e42fd50`  |
| 3242   | Layout 1 | `59f27e42fd50`  |
| 3235   | Layout 1 | `59f27e42fd50`  |
| 3229   | Layout 1 | `59f27e42fd50`  |
| 3212   | Layout 1 | `59f27e42fd50`  |
| 3203   | Layout 1 | `59f27e42fd50`  |
| 3193   | Layout 1 | `59f27e42fd50`  |
| 3186   | Layout 1 | `59f27e42fd50`  |
| 3177   | Layout 1 | `59f27e42fd50`  |
| 3169   | Layout 1 | `59f27e42fd50`  |
| 3158   | Layout 1 | `59f27e42fd50`  |
| 3151   | Layout 1 | `59f27e42fd50`  |
| 3144   | Layout 1 | `59f27e42fd50`  |
| 3133   | Layout 1 | `59f27e42fd50`  |
| 3125   | Layout 1 | `59f27e42fd50`  |
| 3118   | Layout 1 | `59f27e42fd50`  |
| 3111   | Layout 1 | `59f27e42fd50`  |
| 3103   | Layout 1 | `59f27e42fd50`  |
| 3095   | Layout 1 | `59f27e42fd50`  |
| 3086   | Layout 1 | `59f27e42fd50`  |
| 3072   | Layout 1 | `59f27e42fd50`  |
| 3062   | Layout 1 | `59f27e42fd50`  |
| 3052   | Layout 1 | `59f27e42fd50`  |
| 3045   | Layout 1 | `59f27e42fd50`  |
| 3037   | Layout 1 | `59f27e42fd50`  |
| 3030   | Layout 1 | `59f27e42fd50`  |
| 3021   | Layout 1 | `59f27e42fd50`  |
| 3012   | Layout 1 | `59f27e42fd50`  |
| 3002   | Layout 1 | `59f27e42fd50`  |
| 2995   | Layout 1 | `59f27e42fd50`  |
| 2987   | Layout 1 | `59f27e42fd50`  |
| 2978   | Layout 1 | `59f27e42fd50`  |
| 2970   | Layout 1 | `59f27e42fd50`  |
| 2959   | Layout 1 | `59f27e42fd50`  |
| 2951   | Layout 1 | `59f27e42fd50`  |
| 2942   | Layout 1 | `59f27e42fd50`  |
| 2935   | Layout 1 | `59f27e42fd50`  |
| 2932   | Layout 1 | `59f27e42fd50`  |
| 2923   | Layout 1 | `59f27e42fd50`  |
| 2919   | Layout 1 | `59f27e42fd50`  |
| 2907   | Layout 1 | `59f27e42fd50`  |
| 2900   | Layout 1 | `59f27e42fd50`  |
| 2891   | Layout 1 | `59f27e42fd50`  |
| 2882   | Layout 1 | `59f27e42fd50`  |
| 2872   | Layout 1 | `59f27e42fd50`  |
| 2863   | Layout 1 | `59f27e42fd50`  |
| 2855   | Layout 1 | `59f27e42fd50`  |
| 2849   | Layout 1 | `59f27e42fd50`  |
| 2844   | Layout 1 | `59f27e42fd50`  |
| 2834   | Layout 1 | `59f27e42fd50`  |
| 2825   | Layout 1 | `59f27e42fd50`  |
| 2819   | Layout 1 | `59f27e42fd50`  |
| 2811   | Layout 1 | `59f27e42fd50`  |
| 2803   | Layout 1 | `59f27e42fd50`  |
| 2794   | Layout 1 | `59f27e42fd50`  |
| 2783   | Layout 1 | `59f27e42fd50`  |
| 2774   | Layout 1 | `59f27e42fd50`  |
| 2765   | Layout 1 | `59f27e42fd50`  |
| 2756   | Layout 1 | `59f27e42fd50`  |
| 2750   | Layout 1 | `59f27e42fd50`  |
| 2743   | Layout 1 | `59f27e42fd50`  |
| 2736   | Layout 1 | `59f27e42fd50`  |
| 2726   | Layout 1 | `59f27e42fd50`  |
| 2717   | Layout 1 | `59f27e42fd50`  |
| 2709   | Layout 1 | `59f27e42fd50`  |
| 2703   | Layout 1 | `59f27e42fd50`  |
| 2695   | Layout 1 | `59f27e42fd50`  |
| 2684   | Layout 1 | `59f27e42fd50`  |
| 2672   | Layout 1 | `59f27e42fd50`  |
| 2665   | Layout 1 | `59f27e42fd50`  |
| 2657   | Layout 1 | `59f27e42fd50`  |
| 2649   | Layout 1 | `59f27e42fd50`  |
| 2644   | Layout 1 | `59f27e42fd50`  |
| 2637   | Layout 1 | `59f27e42fd50`  |
| 2629   | Layout 1 | `59f27e42fd50`  |
| 2619   | Layout 1 | `59f27e42fd50`  |
| 2612   | Layout 1 | `59f27e42fd50`  |
| 2606   | Layout 1 | `59f27e42fd50`  |
| 2602   | Layout 1 | `59f27e42fd50`  |
| 2601   | Layout 1 | `59f27e42fd50`  |
| 2592   | Layout 1 | `59f27e42fd50`  |
| 2583   | Layout 1 | `59f27e42fd50`  |
| 2575   | Layout 1 | `59f27e42fd50`  |
| 2567   | Layout 1 | `59f27e42fd50`  |
| 2560   | Layout 1 | `59f27e42fd50`  |
| 2553   | Layout 1 | `59f27e42fd50`  |
| 2545   | Layout 1 | `59f27e42fd50`  |
| 2538   | Layout 1 | `59f27e42fd50`  |
| 2529   | Layout 1 | `59f27e42fd50`  |
| 2519   | Layout 1 | `59f27e42fd50`  |
| 2513   | Layout 1 | `59f27e42fd50`  |
| 2510   | Layout 1 | `59f27e42fd50`  |
| 2507   | Layout 1 | `59f27e42fd50`  |
| 2503   | Layout 1 | `59f27e42fd50`  |
| 2498   | Layout 1 | `59f27e42fd50`  |
| 2492   | Layout 1 | `59f27e42fd50`  |
| 2487   | Layout 1 | `59f27e42fd50`  |
| 2480   | Layout 1 | `59f27e42fd50`  |
| 2474   | Layout 1 | `59f27e42fd50`  |
| 2468   | Layout 1 | `59f27e42fd50`  |
| 2460   | Layout 1 | `59f27e42fd50`  |
| 2453   | Layout 1 | `59f27e42fd50`  |
| 2444   | Layout 1 | `59f27e42fd50`  |
| 2438   | Layout 1 | `59f27e42fd50`  |
| 2434   | Layout 1 | `59f27e42fd50`  |
| 2429   | Layout 1 | `59f27e42fd50`  |
| 2421   | Layout 1 | `59f27e42fd50`  |
| 2414   | Layout 1 | `59f27e42fd50`  |
| 2407   | Layout 1 | `59f27e42fd50`  |
| 2401   | Layout 1 | `59f27e42fd50`  |
| 2397   | Layout 1 | `59f27e42fd50`  |
| 2393   | Layout 1 | `59f27e42fd50`  |
| 2384   | Layout 1 | `59f27e42fd50`  |
| 2378   | Layout 1 | `59f27e42fd50`  |
| 2372   | Layout 1 | `59f27e42fd50`  |
| 2358   | Layout 1 | `59f27e42fd50`  |
| 2352   | Layout 1 | `59f27e42fd50`  |
| 2347   | Layout 1 | `59f27e42fd50`  |
| 2343   | Layout 1 | `59f27e42fd50`  |
| 2335   | Layout 1 | `59f27e42fd50`  |
| 2327   | Layout 1 | `59f27e42fd50`  |
| 2324   | Layout 1 | `59f27e42fd50`  |
| 2319   | Layout 1 | `59f27e42fd50`  |
| 2313   | Layout 1 | `59f27e42fd50`  |
| 2308   | Layout 1 | `59f27e42fd50`  |
| 2302   | Layout 1 | `59f27e42fd50`  |
| 2295   | Layout 1 | `59f27e42fd50`  |
| 2290   | Layout 1 | `59f27e42fd50`  |
| 2284   | Layout 1 | `59f27e42fd50`  |
| 2276   | Layout 1 | `59f27e42fd50`  |
| 2269   | Layout 1 | `59f27e42fd50`  |
| 2259   | Layout 1 | `59f27e42fd50`  |
| 2250   | Layout 1 | `59f27e42fd50`  |
| 2243   | Layout 1 | `59f27e42fd50`  |
| 2235   | Layout 1 | `59f27e42fd50`  |
| 2229   | Layout 1 | `59f27e42fd50`  |
| 2224   | Layout 1 | `59f27e42fd50`  |
| 2218   | Layout 1 | `59f27e42fd50`  |
| 2215   | Layout 1 | `59f27e42fd50`  |
| 2207   | Layout 1 | `59f27e42fd50`  |
| 2203   | Layout 1 | `59f27e42fd50`  |
| 2196   | Layout 1 | `59f27e42fd50`  |
| 2192   | Layout 1 | `59f27e42fd50`  |
| 2189   | Layout 1 | `59f27e42fd50`  |
| 2183   | Layout 1 | `59f27e42fd50`  |
| 2179   | Layout 1 | `59f27e42fd50`  |
| 2171   | Layout 1 | `59f27e42fd50`  |
| 2163   | Layout 1 | `59f27e42fd50`  |
| 2156   | Layout 1 | `59f27e42fd50`  |
| 2151   | Layout 1 | `59f27e42fd50`  |
| 2147   | Layout 1 | `59f27e42fd50`  |
| 2142   | Layout 1 | `59f27e42fd50`  |
| 2138   | Layout 1 | `59f27e42fd50`  |
| 2134   | Layout 1 | `59f27e42fd50`  |
| 2130   | Layout 1 | `59f27e42fd50`  |
| 2122   | Layout 1 | `59f27e42fd50`  |
| 2107   | Layout 1 | `59f27e42fd50`  |
| 2098   | Layout 1 | `59f27e42fd50`  |
| 2089   | Layout 1 | `59f27e42fd50`  |
| 2081   | Layout 1 | `59f27e42fd50`  |
| 2073   | Layout 1 | `59f27e42fd50`  |
| 2067   | Layout 1 | `59f27e42fd50`  |
| 2063   | Layout 1 | `59f27e42fd50`  |
| 2059   | Layout 1 | `59f27e42fd50`  |
| 2052   | Layout 1 | `59f27e42fd50`  |
| 2044   | Layout 1 | `59f27e42fd50`  |
| 2039   | Layout 1 | `59f27e42fd50`  |
| 2032   | Layout 1 | `59f27e42fd50`  |
| 2025   | Layout 1 | `59f27e42fd50`  |
| 2011   | Layout 1 | `59f27e42fd50`  |
| 2005   | Layout 1 | `59f27e42fd50`  |
| 2000   | Layout 1 | `59f27e42fd50`  |
| 1996   | Layout 1 | `59f27e42fd50`  |
| 1991   | Layout 1 | `59f27e42fd50`  |
| 1985   | Layout 1 | `59f27e42fd50`  |
| 1980   | Layout 1 | `59f27e42fd50`  |
| 1969   | Layout 1 | `59f27e42fd50`  |
| 1964   | Layout 1 | `59f27e42fd50`  |
| 1958   | Layout 1 | `59f27e42fd50`  |
| 1950   | Layout 1 | `59f27e42fd50`  |
| 1945   | Layout 1 | `59f27e42fd50`  |
| 1937   | Layout 1 | `59f27e42fd50`  |
| 1933   | Layout 1 | `59f27e42fd50`  |
| 1927   | Layout 1 | `59f27e42fd50`  |
| 1921   | Layout 1 | `59f27e42fd50`  |
| 1914   | Layout 1 | `59f27e42fd50`  |
| 1908   | Layout 1 | `59f27e42fd50`  |
| 1897   | Layout 1 | `59f27e42fd50`  |
| 1892   | Layout 1 | `59f27e42fd50`  |
| 1886   | Layout 1 | `59f27e42fd50`  |
| 1881   | Layout 1 | `59f27e42fd50`  |
| 1871   | Layout 1 | `59f27e42fd50`  |
| 1866   | Layout 1 | `59f27e42fd50`  |
| 1862   | Layout 1 | `59f27e42fd50`  |
| 1854   | Layout 1 | `59f27e42fd50`  |
| 1846   | Layout 1 | `59f27e42fd50`  |
| 1838   | Layout 1 | `59f27e42fd50`  |
| 1832   | Layout 1 | `59f27e42fd50`  |
| 1826   | Layout 1 | `59f27e42fd50`  |
| 1822   | Layout 1 | `59f27e42fd50`  |
| 1818   | Layout 1 | `59f27e42fd50`  |
| 1804   | Layout 1 | `59f27e42fd50`  |
| 1794   | Layout 1 | `59f27e42fd50`  |
| 1790   | Layout 1 | `59f27e42fd50`  |
| 1784   | Layout 1 | `59f27e42fd50`  |
| 1774   | Layout 1 | `59f27e42fd50`  |
| 1771   | Layout 1 | `59f27e42fd50`  |
| 1762   | Layout 1 | `59f27e42fd50`  |
| 1759   | Layout 1 | `59f27e42fd50`  |
| 1754   | Layout 1 | `59f27e42fd50`  |
| 1749   | Layout 1 | `59f27e42fd50`  |
| 1743   | Layout 1 | `59f27e42fd50`  |
| 1737   | Layout 1 | `59f27e42fd50`  |
| 1731   | Layout 1 | `59f27e42fd50`  |
| 1725   | Layout 1 | `59f27e42fd50`  |
| 1717   | Layout 1 | `59f27e42fd50`  |
| 1710   | Layout 1 | `59f27e42fd50`  |
| 1704   | Layout 1 | `59f27e42fd50`  |
| 1698   | Layout 1 | `59f27e42fd50`  |
| 1690   | Layout 1 | `59f27e42fd50`  |
| 1685   | Layout 1 | `59f27e42fd50`  |
| 1680   | Layout 1 | `59f27e42fd50`  |
| 1674   | Layout 1 | `59f27e42fd50`  |
| 1668   | Layout 1 | `59f27e42fd50`  |
| 1659   | Layout 1 | `59f27e42fd50`  |
| 1649   | Layout 1 | `59f27e42fd50`  |
| 1642   | Layout 1 | `59f27e42fd50`  |
| 1636   | Layout 1 | `59f27e42fd50`  |
| 1628   | Layout 1 | `59f27e42fd50`  |
| 1622   | Layout 1 | `59f27e42fd50`  |
| 1614   | Layout 1 | `59f27e42fd50`  |
| 1608   | Layout 1 | `59f27e42fd50`  |
| 1602   | Layout 1 | `59f27e42fd50`  |
| 1598   | Layout 1 | `59f27e42fd50`  |
| 1594   | Layout 1 | `59f27e42fd50`  |
| 1590   | Layout 1 | `59f27e42fd50`  |
| 1587   | Layout 1 | `59f27e42fd50`  |
| 1584   | Layout 1 | `59f27e42fd50`  |
| 1579   | Layout 1 | `59f27e42fd50`  |
| 1572   | Layout 1 | `59f27e42fd50`  |
| 1565   | Layout 1 | `59f27e42fd50`  |
| 1559   | Layout 1 | `59f27e42fd50`  |
| 1554   | Layout 1 | `59f27e42fd50`  |
| 1547   | Layout 1 | `59f27e42fd50`  |
| 1537   | Layout 1 | `59f27e42fd50`  |
| 1529   | Layout 1 | `59f27e42fd50`  |
| 1524   | Layout 1 | `59f27e42fd50`  |
| 1519   | Layout 1 | `59f27e42fd50`  |
| 1509   | Layout 1 | `59f27e42fd50`  |
| 1506   | Layout 1 | `59f27e42fd50`  |
| 1504   | Layout 1 | `59f27e42fd50`  |
| 1500   | Layout 1 | `59f27e42fd50`  |
| 1493   | Layout 1 | `59f27e42fd50`  |
| 1489   | Layout 1 | `59f27e42fd50`  |
| 1485   | Layout 1 | `59f27e42fd50`  |
| 1481   | Layout 1 | `59f27e42fd50`  |
| 1474   | Layout 1 | `59f27e42fd50`  |
| 1466   | Layout 1 | `59f27e42fd50`  |
| 1462   | Layout 1 | `59f27e42fd50`  |
| 1459   | Layout 1 | `59f27e42fd50`  |
| 1453   | Layout 1 | `59f27e42fd50`  |
| 1450   | Layout 1 | `59f27e42fd50`  |
| 1445   | Layout 1 | `59f27e42fd50`  |
| 1439   | Layout 1 | `59f27e42fd50`  |
| 1433   | Layout 1 | `59f27e42fd50`  |
| 1430   | Layout 1 | `59f27e42fd50`  |
| 1426   | Layout 1 | `59f27e42fd50`  |
| 1421   | Layout 1 | `59f27e42fd50`  |
| 1417   | Layout 1 | `59f27e42fd50`  |
| 1416   | Layout 1 | `59f27e42fd50`  |
| 1409   | Layout 1 | `59f27e42fd50`  |
| 1405   | Layout 1 | `59f27e42fd50`  |
| 1401   | Layout 1 | `59f27e42fd50`  |
| 1396   | Layout 1 | `59f27e42fd50`  |
| 1391   | Layout 1 | `59f27e42fd50`  |
| 1390   | Layout 1 | `59f27e42fd50`  |
| 1386   | Layout 1 | `59f27e42fd50`  |
| 1381   | Layout 1 | `59f27e42fd50`  |
| 1379   | Layout 1 | `59f27e42fd50`  |
| 1372   | Layout 1 | `59f27e42fd50`  |
| 1366   | Layout 1 | `59f27e42fd50`  |
| 1364   | Layout 1 | `59f27e42fd50`  |
| 1363   | Layout 1 | `59f27e42fd50`  |
| 1360   | Layout 1 | `59f27e42fd50`  |
| 1358   | Layout 1 | `59f27e42fd50`  |
| 1355   | Layout 1 | `59f27e42fd50`  |
| 1351   | Layout 1 | `59f27e42fd50`  |
| 1348   | Layout 1 | `59f27e42fd50`  |
| 1346   | Layout 1 | `59f27e42fd50`  |
| 1341   | Layout 1 | `59f27e42fd50`  |
| 1340   | Layout 1 | `59f27e42fd50`  |
| 1338   | Layout 1 | `59f27e42fd50`  |
| 1335   | Layout 1 | `59f27e42fd50`  |
| 1333   | Layout 1 | `59f27e42fd50`  |
| 1329   | Layout 1 | `59f27e42fd50`  |
| 1327   | Layout 1 | `59f27e42fd50`  |
| 1324   | Layout 1 | `59f27e42fd50`  |
| 1321   | Layout 1 | `59f27e42fd50`  |
| 1319   | Layout 1 | `59f27e42fd50`  |
| 1318   | Layout 1 | `59f27e42fd50`  |
| 1316   | Layout 1 | `59f27e42fd50`  |
| 1313   | Layout 1 | `59f27e42fd50`  |
| 1311   | Layout 1 | `59f27e42fd50`  |
| 1309   | Layout 1 | `59f27e42fd50`  |
| 1304   | Layout 1 | `59f27e42fd50`  |
| 1292   | Layout 1 | `59f27e42fd50`  |
| 1286   | Layout 1 | `59f27e42fd50`  |
| 1280   | Layout 1 | `59f27e42fd50`  |
| 1276   | Layout 1 | `59f27e42fd50`  |
| 1267   | No file  | `59f27e42fd50`  |
| 1261   | No file  | `59f27e42fd50`  |
| 1256   | No file  | `59f27e42fd50`  |
| 1250   | No file  | `59f27e42fd50`  |
| 1246   | No file  | `59f27e42fd50`  |
| 1239   | No file  | `59f27e42fd50`  |
| 1230   | No file  | `59f27e42fd50`  |
| 1226   | No file  | `59f27e42fd50`  |
| 1220   | No file  | `59f27e42fd50`  |
| 1217   | No file  | `59f27e42fd50`  |
| 1211   | No file  | `59f27e42fd50`  |
| 1210   | No file  | `59f27e42fd50`  |
| 1208   | No file  | `59f27e42fd50`  |
| 1203   | No file  | `59f27e42fd50`  |
| 1197   | No file  | `59f27e42fd50`  |
| 1194   | No file  | `59f27e42fd50`  |
| 1192   | No file  | `59f27e42fd50`  |
| 1187   | No file  | `59f27e42fd50`  |
| 1183   | No file  | `59f27e42fd50`  |
| 1177   | No file  | `59f27e42fd50`  |
| 1173   | No file  | `59f27e42fd50`  |
| 1167   | No file  | `59f27e42fd50`  |
| 1164   | No file  | `59f27e42fd50`  |
| 1156   | No file  | `59f27e42fd50`  |
| 1149   | No file  | `59f27e42fd50`  |
| 1144   | No file  | `59f27e42fd50`  |
| 1137   | No file  | `59f27e42fd50`  |
| 1132   | No file  | `59f27e42fd50`  |
| 1127   | No file  | `59f27e42fd50`  |
| 1122   | No file  | `59f27e42fd50`  |
| 1118   | No file  | `59f27e42fd50`  |
| 1114   | No file  | `59f27e42fd50`  |
| 1109   | No file  | `59f27e42fd50`  |
| 1102   | No file  | `59f27e42fd50`  |
| 1096   | No file  | `59f27e42fd50`  |
| 1088   | No file  | `59f27e42fd50`  |
| 1081   | No file  | `59f27e42fd50`  |
| 1076   | No file  | `59f27e42fd50`  |
| 1069   | No file  | `59f27e42fd50`  |
| 1064   | No file  | `59f27e42fd50`  |
| 1058   | No file  | `59f27e42fd50`  |
| 1051   | No file  | `59f27e42fd50`  |
| 1044   | No file  | `59f27e42fd50`  |
| 1036   | No file  | `59f27e42fd50`  |
| 1026   | No file  | `59f27e42fd50`  |
| 1016   | No file  | `59f27e42fd50`  |
| 1009   | No file  | `59f27e42fd50`  |
| 1005   | No file  | `59f27e42fd50`  |
| 1000   | No file  | `59f27e42fd50`  |
| 998    | No file  | `59f27e42fd50`  |
| 990    | No file  | `59f27e42fd50`  |
| 979    | No file  | `59f27e42fd50`  |
| 972    | No file  | `59f27e42fd50`  |
| 963    | No file  | `59f27e42fd50`  |
| 955    | No file  | `59f27e42fd50`  |
| 946    | No file  | `59f27e42fd50`  |
| 938    | No file  | `59f27e42fd50`  |
| 927    | No file  | `59f27e42fd50`  |
| 911    | No file  | `59f27e42fd50`  |
| 904    | No file  | `59f27e42fd50`  |
| 899    | No file  | `59f27e42fd50`  |
| 894    | No file  | `59f27e42fd50`  |
| 885    | No file  | `59f27e42fd50`  |
| 879    | No file  | `59f27e42fd50`  |
| 872    | No file  | `59f27e42fd50`  |
| 864    | No file  | `59f27e42fd50`  |
| 855    | No file  | `59f27e42fd50`  |
| 853    | No file  | `59f27e42fd50`  |
| 845    | No file  | `59f27e42fd50`  |
| 837    | No file  | `59f27e42fd50`  |
| 829    | No file  | `59f27e42fd50`  |
| 822    | No file  | `59f27e42fd50`  |
| 814    | No file  | `59f27e42fd50`  |
| 805    | No file  | `59f27e42fd50`  |
| 794    | No file  | `59f27e42fd50`  |
| 787    | No file  | `59f27e42fd50`  |
| 780    | No file  | `59f27e42fd50`  |
| 771    | No file  | `59f27e42fd50`  |
| 760    | No file  | `59f27e42fd50`  |
| 748    | No file  | `59f27e42fd50`  |
| 741    | No file  | `59f27e42fd50`  |
| 736    | No file  | `59f27e42fd50`  |
| 731    | No file  | `59f27e42fd50`  |
| 723    | No file  | `59f27e42fd50`  |
| 711    | No file  | `59f27e42fd50`  |
| 707    | No file  | `59f27e42fd50`  |
| 697    | No file  | `59f27e42fd50`  |
| 689    | No file  | `59f27e42fd50`  |
| 683    | No file  | `59f27e42fd50`  |
| 678    | No file  | `59f27e42fd50`  |
| 670    | No file  | `59f27e42fd50`  |
| 661    | No file  | `59f27e42fd50`  |
| 656    | No file  | `59f27e42fd50`  |
| 652    | No file  | `59f27e42fd50`  |
| 643    | No file  | `59f27e42fd50`  |
| 637    | No file  | `59f27e42fd50`  |
| 630    | No file  | `59f27e42fd50`  |
| 627    | No file  | `59f27e42fd50`  |
| 621    | No file  | `59f27e42fd50`  |
| 617    | No file  | `59f27e42fd50`  |
| 615    | No file  | `59f27e42fd50`  |
| 606    | No file  | `59f27e42fd50`  |
| 599    | No file  | `59f27e42fd50`  |
| 592    | No file  | `59f27e42fd50`  |
| 586    | No file  | `59f27e42fd50`  |
| 577    | No file  | `59f27e42fd50`  |
| 569    | No file  | `59f27e42fd50`  |
| 561    | No file  | `59f27e42fd50`  |
| 554    | No file  | `59f27e42fd50`  |
| 542    | No file  | `59f27e42fd50`  |
| 532    | No file  | `59f27e42fd50`  |
| 531    | No file  | `59f27e42fd50`  |
| 526    | No file  | `59f27e42fd50`  |
| 521    | No file  | `59f27e42fd50`  |
| 517    | No file  | `59f27e42fd50`  |
| 510    | No file  | `59f27e42fd50`  |
| 508    | No file  | `59f27e42fd50`  |
| 504    | No file  | `59f27e42fd50`  |
| 497    | No file  | `59f27e42fd50`  |
| 491    | No file  | `59f27e42fd50`  |
| 485    | No file  | `59f27e42fd50`  |
| 478    | No file  | `59f27e42fd50`  |
| 472    | No file  | `59f27e42fd50`  |
| 466    | No file  | `59f27e42fd50`  |
| 457    | No file  | `59f27e42fd50`  |
| 452    | No file  | `59f27e42fd50`  |
| 449    | No file  | `59f27e42fd50`  |
| 435    | No file  | `59f27e42fd50`  |

<!-- versions:end -->

## Companion Files

None. `instancedungeoninfooffset.dbss` is the offset file of this table;
the handler reads the records straight from the main file, since every
record has the same size.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                     | Field | Notes                                 |
| ------- | ------------------------ | ----- | ------------------------------------- |
| `+0x00` | u32                      | count | Number of records; `4` on client 3474 |
| `+0x04` | Dungeon Entry Row[count] | rows  | See Dungeon Entry Row                 |

The rows fill the file exactly: 4 + 4 x 22 = 92 bytes on client 3474.

### Dungeon Entry Row (22 bytes)

| Offset  | Type | Field          | Notes                                                                       |
| ------- | ---- | -------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | key            | Record key, `0` to `3` on client 3474; equals the index row key             |
| `+0x04` | u16  | field_no       | Field the dungeon runs in, a `Field_Table` key: `1238`, `1239`, `700`, `701` on client 3474 |
| `+0x06` | f32  | enter_x        | Entry position, world X                                                     |
| `+0x0A` | f32  | enter_y        | Entry position, world Y (height)                                            |
| `+0x0E` | f32  | enter_z        | Entry position, world Z                                                     |
| `+0x12` | f32  | enter_rotation | Facing direction at entry in radians; the sheet column holds degrees        |

### `instancedungeoninfooffset.dbss`

Bare offset table into `instancedungeoninfo.dbss` (no PABR magic, no
trailer).

| Offset  | Type             | Field | Notes                                           |
| ------- | ---------------- | ----- | ----------------------------------------------- |
| `+0x00` | u32              | count | Number of index rows; equals the main file count |
| `+0x04` | Index Row[count] | rows  | See Index Row                                   |

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                                  |
| ------- | ---- | ------ | ------------------------------------------------------ |
| `+0x00` | u32  | key    | The record's `key`                                     |
| `+0x04` | u32  | offset | Absolute byte offset of the record in the main file    |
| `+0x08` | u32  | size   | Record length including `key`; `22` on every row       |

## Field Names

The record is the `InstanceDungeonInfo_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784. Every column matches on all 4 keys of
client 3474:

| Field                           | Sheet column       | Match                                                        |
| ------------------------------- | ------------------ | ------------------------------------------------------------ |
| `key`                           | `Index`            | 4 of 4                                                       |
| `field_no`                      | `FieldNo`          | 4 of 4                                                       |
| `enter_x`, `enter_y`, `enter_z` | `EnterPosition`    | 4 of 4; the sheet writes the three as `768000,11542,102400`   |
| `enter_rotation`                | `EnterRotationDeg` | 4 of 4 once converted: the sheet's `90` is `1.5707964` (pi / 2) here, its `0` is `0` |

The `InstanceDungeonInfo_Table` of a private server on client 519 has the
same columns and rows, except that it gives `EnterRotationDeg` `0` for key
`1`. The server's loader for the sheet (`loadInstanceDungeonInformation`
in its log strings) reads `EnterPosition` as a string and
`EnterRotationDeg` as a float, and logs "인던필드의 EnterPosition의 Y값이
비정상입니다" ("the instance field's EnterPosition Y value is invalid"), and
the same for Z, when a coordinate is bad. The 2016 PDB has no instance
dungeon struct.

`FieldNo` is the key column of the `Field_Table` sheet of the same 1784
source, whose client copy is [fieldinfo.bss](fieldinfo_bss.md). The sheet
and the client 3474 file give the four fields the same names:

| `field_no` | `FieldName` in the sheet | Translation                       |
| ---------- | ------------------------ | --------------------------------- |
| `700`      | 칼페온 크자카 인던       | Calpheon Kzarka instance dungeon  |
| `701`      | 아쳐 튜토리얼 인던       | Archer tutorial instance dungeon  |
| `1238`     | 트리거 테스트 인던1      | Trigger test instance dungeon 1   |
| `1239`     | 트리거 테스트 인던2      | Trigger test instance dungeon 2   |

## Notes

- Keys `0` and `1` share the entry position `(768000, 11542, 102400)` and
  differ in `field_no` and `enter_rotation` (`0` and pi / 2).
- The client Lua enters an instance dungeon with
  `ToClient_EnterIntanceDungeon(indunKey, true)`
  (`panel_window_storyinstancedungeon.luac`), where `indunKey` comes from the
  server event `FromClient_ShowIndunMessage`.

## Open Questions

### Whether the Lua Instance Dungeon Key Is This Key

`panel_window_storyinstancedungeon.luac` passes an `indunKey` from the
server to `ToClient_EnterIntanceDungeon`. Whether that key is this table's
`key` (`0` to `3`), a `field_no` or another key space is open; the Lua
shows no literal key.
