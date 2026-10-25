# `itemviewstackenchantgroupss.bss` Format

## Purpose

Groups of [`enchantstaticstatus.dbss`](../dbss/enchantstaticstatus_dbss.md) enchant
keys. Each row is one enchant key with the full list of keys in its group,
itself included, so every key of a group has its own row with the same list.
A group is one item family across equipment types: the Liverto Longsword,
Longbow, Amulet and Axe keys (57, 257, 457, 657) form one group, the Kzarka
ones (62, 262, 462, 662) another. Every key of a group enhances with the same
success chance, material and failure result at each level (see Groups).

The Another Adventurer's Choice window beside the enhancement window counts
the failstacks other players used per group: every key of a group shows the
same ranges, and keys of different groups show different ones. Its button
shows only for keys in this file (both checked in game on client 3474, see
Another Adventurer's Choice).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                              | Bytes   | Records   | Row bytes                 |
| ------ | -------------- | --------------------------------- | ------- | --------- | ------------------------- |
| 1      | 2218 and later | `itemviewstackenchantgroupss.bss` | 192,732 | 1,146 Row | 20 to 628, 168 on average |

| Layout | File                              | Known             | Unknown        |
| ------ | --------------------------------- | ----------------- | -------------- |
| 1      | `itemviewstackenchantgroupss.bss` | 188,148 B (97.6%) | 4,584 B (2.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `52d5767bf248`  |
| 3482   | Layout 1 | `52d5767bf248`  |
| 3474   | Layout 1 | `52d5767bf248`  |
| 3473   | Layout 1 | `52d5767bf248`  |
| 3464   | Layout 1 | `52d5767bf248`  |
| 3458   | Layout 1 | `52d5767bf248`  |
| 3454   | Layout 1 | `52d5767bf248`  |
| 3444   | Layout 1 | `52d5767bf248`  |
| 3435   | Layout 1 | `52d5767bf248`  |
| 3426   | Layout 1 | `52d5767bf248`  |
| 3418   | Layout 1 | `52d5767bf248`  |
| 3412   | Layout 1 | `52d5767bf248`  |
| 3402   | Layout 1 | `52d5767bf248`  |
| 3396   | Layout 1 | `52d5767bf248`  |
| 3387   | Layout 1 | `52d5767bf248`  |
| 3381   | Layout 1 | `52d5767bf248`  |
| 3373   | Layout 1 | `52d5767bf248`  |
| 3364   | Layout 1 | `52d5767bf248`  |
| 3356   | Layout 1 | `52d5767bf248`  |
| 3349   | Layout 1 | `52d5767bf248`  |
| 3342   | Layout 1 | `52d5767bf248`  |
| 3335   | Layout 1 | `52d5767bf248`  |
| 3326   | Layout 1 | `52d5767bf248`  |
| 3321   | Layout 1 | `52d5767bf248`  |
| 3314   | Layout 1 | `52d5767bf248`  |
| 3303   | Layout 1 | `52d5767bf248`  |
| 3302   | Layout 1 | `52d5767bf248`  |
| 3293   | Layout 1 | `52d5767bf248`  |
| 3283   | Layout 1 | `52d5767bf248`  |
| 3275   | Layout 1 | `52d5767bf248`  |
| 3267   | Layout 1 | `52d5767bf248`  |
| 3258   | Layout 1 | `52d5767bf248`  |
| 3251   | Layout 1 | `52d5767bf248`  |
| 3242   | Layout 1 | `52d5767bf248`  |
| 3235   | Layout 1 | `52d5767bf248`  |
| 3229   | Layout 1 | `52d5767bf248`  |
| 3212   | Layout 1 | `52d5767bf248`  |
| 3203   | Layout 1 | `52d5767bf248`  |
| 3193   | Layout 1 | `52d5767bf248`  |
| 3186   | Layout 1 | `52d5767bf248`  |
| 3177   | Layout 1 | `52d5767bf248`  |
| 3169   | Layout 1 | `52d5767bf248`  |
| 3158   | Layout 1 | `52d5767bf248`  |
| 3151   | Layout 1 | `52d5767bf248`  |
| 3144   | Layout 1 | `52d5767bf248`  |
| 3133   | Layout 1 | `52d5767bf248`  |
| 3125   | Layout 1 | `52d5767bf248`  |
| 3118   | Layout 1 | `52d5767bf248`  |
| 3111   | Layout 1 | `52d5767bf248`  |
| 3103   | Layout 1 | `52d5767bf248`  |
| 3095   | Layout 1 | `52d5767bf248`  |
| 3086   | Layout 1 | `52d5767bf248`  |
| 3072   | Layout 1 | `52d5767bf248`  |
| 3062   | Layout 1 | `52d5767bf248`  |
| 3052   | Layout 1 | `52d5767bf248`  |
| 3045   | Layout 1 | `52d5767bf248`  |
| 3037   | Layout 1 | `52d5767bf248`  |
| 3030   | Layout 1 | `52d5767bf248`  |
| 3021   | Layout 1 | `52d5767bf248`  |
| 3012   | Layout 1 | `52d5767bf248`  |
| 3002   | Layout 1 | `52d5767bf248`  |
| 2995   | Layout 1 | `52d5767bf248`  |
| 2987   | Layout 1 | `52d5767bf248`  |
| 2978   | Layout 1 | `52d5767bf248`  |
| 2970   | Layout 1 | `52d5767bf248`  |
| 2959   | Layout 1 | `52d5767bf248`  |
| 2951   | Layout 1 | `52d5767bf248`  |
| 2942   | Layout 1 | `52d5767bf248`  |
| 2935   | Layout 1 | `52d5767bf248`  |
| 2932   | Layout 1 | `52d5767bf248`  |
| 2923   | Layout 1 | `52d5767bf248`  |
| 2919   | Layout 1 | `52d5767bf248`  |
| 2907   | Layout 1 | `52d5767bf248`  |
| 2900   | Layout 1 | `52d5767bf248`  |
| 2891   | Layout 1 | `52d5767bf248`  |
| 2882   | Layout 1 | `52d5767bf248`  |
| 2872   | Layout 1 | `52d5767bf248`  |
| 2863   | Layout 1 | `52d5767bf248`  |
| 2855   | Layout 1 | `52d5767bf248`  |
| 2849   | Layout 1 | `52d5767bf248`  |
| 2844   | Layout 1 | `52d5767bf248`  |
| 2834   | Layout 1 | `52d5767bf248`  |
| 2825   | Layout 1 | `52d5767bf248`  |
| 2819   | Layout 1 | `52d5767bf248`  |
| 2811   | Layout 1 | `52d5767bf248`  |
| 2803   | Layout 1 | `52d5767bf248`  |
| 2794   | Layout 1 | `52d5767bf248`  |
| 2783   | Layout 1 | `52d5767bf248`  |
| 2774   | Layout 1 | `52d5767bf248`  |
| 2765   | Layout 1 | `52d5767bf248`  |
| 2756   | Layout 1 | `52d5767bf248`  |
| 2750   | Layout 1 | `52d5767bf248`  |
| 2743   | Layout 1 | `52d5767bf248`  |
| 2736   | Layout 1 | `52d5767bf248`  |
| 2726   | Layout 1 | `52d5767bf248`  |
| 2717   | Layout 1 | `52d5767bf248`  |
| 2709   | Layout 1 | `52d5767bf248`  |
| 2703   | Layout 1 | `52d5767bf248`  |
| 2695   | Layout 1 | `52d5767bf248`  |
| 2684   | Layout 1 | `52d5767bf248`  |
| 2672   | Layout 1 | `52d5767bf248`  |
| 2665   | Layout 1 | `52d5767bf248`  |
| 2657   | Layout 1 | `52d5767bf248`  |
| 2649   | Layout 1 | `52d5767bf248`  |
| 2644   | Layout 1 | `52d5767bf248`  |
| 2637   | Layout 1 | `52d5767bf248`  |
| 2629   | Layout 1 | `52d5767bf248`  |
| 2619   | Layout 1 | `52d5767bf248`  |
| 2612   | Layout 1 | `52d5767bf248`  |
| 2606   | Layout 1 | `52d5767bf248`  |
| 2602   | Layout 1 | `52d5767bf248`  |
| 2601   | Layout 1 | `52d5767bf248`  |
| 2592   | Layout 1 | `52d5767bf248`  |
| 2583   | Layout 1 | `52d5767bf248`  |
| 2575   | Layout 1 | `52d5767bf248`  |
| 2567   | Layout 1 | `52d5767bf248`  |
| 2560   | Layout 1 | `52d5767bf248`  |
| 2553   | Layout 1 | `52d5767bf248`  |
| 2545   | Layout 1 | `52d5767bf248`  |
| 2538   | Layout 1 | `52d5767bf248`  |
| 2529   | Layout 1 | `52d5767bf248`  |
| 2519   | Layout 1 | `52d5767bf248`  |
| 2513   | Layout 1 | `52d5767bf248`  |
| 2510   | Layout 1 | `52d5767bf248`  |
| 2507   | Layout 1 | `52d5767bf248`  |
| 2503   | Layout 1 | `52d5767bf248`  |
| 2498   | Layout 1 | `52d5767bf248`  |
| 2492   | Layout 1 | `52d5767bf248`  |
| 2487   | Layout 1 | `52d5767bf248`  |
| 2480   | Layout 1 | `52d5767bf248`  |
| 2474   | Layout 1 | `52d5767bf248`  |
| 2468   | Layout 1 | `52d5767bf248`  |
| 2460   | Layout 1 | `52d5767bf248`  |
| 2453   | Layout 1 | `52d5767bf248`  |
| 2444   | Layout 1 | `52d5767bf248`  |
| 2438   | Layout 1 | `52d5767bf248`  |
| 2434   | Layout 1 | `52d5767bf248`  |
| 2429   | Layout 1 | `52d5767bf248`  |
| 2421   | Layout 1 | `52d5767bf248`  |
| 2414   | Layout 1 | `52d5767bf248`  |
| 2407   | Layout 1 | `52d5767bf248`  |
| 2401   | Layout 1 | `52d5767bf248`  |
| 2397   | Layout 1 | `52d5767bf248`  |
| 2393   | Layout 1 | `52d5767bf248`  |
| 2384   | Layout 1 | `52d5767bf248`  |
| 2378   | Layout 1 | `52d5767bf248`  |
| 2372   | Layout 1 | `52d5767bf248`  |
| 2358   | Layout 1 | `52d5767bf248`  |
| 2352   | Layout 1 | `52d5767bf248`  |
| 2347   | Layout 1 | `52d5767bf248`  |
| 2343   | Layout 1 | `52d5767bf248`  |
| 2335   | Layout 1 | `52d5767bf248`  |
| 2327   | Layout 1 | `52d5767bf248`  |
| 2324   | Layout 1 | `52d5767bf248`  |
| 2319   | Layout 1 | `52d5767bf248`  |
| 2313   | Layout 1 | `52d5767bf248`  |
| 2308   | Layout 1 | `52d5767bf248`  |
| 2302   | Layout 1 | `52d5767bf248`  |
| 2295   | Layout 1 | `52d5767bf248`  |
| 2290   | Layout 1 | `52d5767bf248`  |
| 2284   | Layout 1 | `52d5767bf248`  |
| 2276   | Layout 1 | `52d5767bf248`  |
| 2269   | Layout 1 | `52d5767bf248`  |
| 2259   | Layout 1 | `52d5767bf248`  |
| 2250   | Layout 1 | `52d5767bf248`  |
| 2243   | Layout 1 | `52d5767bf248`  |
| 2235   | Layout 1 | `52d5767bf248`  |
| 2229   | Layout 1 | `52d5767bf248`  |
| 2224   | Layout 1 | `52d5767bf248`  |
| 2218   | Layout 1 | `52d5767bf248`  |
| 2215   | No file  | `52d5767bf248`  |
| 2207   | No file  | `52d5767bf248`  |
| 2203   | No file  | `52d5767bf248`  |
| 2196   | No file  | `52d5767bf248`  |
| 2192   | No file  | `52d5767bf248`  |
| 2189   | No file  | `52d5767bf248`  |
| 2183   | No file  | `52d5767bf248`  |
| 2179   | No file  | `52d5767bf248`  |
| 2171   | No file  | `52d5767bf248`  |
| 2163   | No file  | `52d5767bf248`  |
| 2156   | No file  | `52d5767bf248`  |
| 2151   | No file  | `52d5767bf248`  |
| 2147   | No file  | `52d5767bf248`  |
| 2142   | No file  | `52d5767bf248`  |
| 2138   | No file  | `52d5767bf248`  |
| 2134   | No file  | `52d5767bf248`  |
| 2130   | No file  | `52d5767bf248`  |
| 2122   | No file  | `52d5767bf248`  |
| 2107   | No file  | `52d5767bf248`  |
| 2098   | No file  | `52d5767bf248`  |
| 2089   | No file  | `52d5767bf248`  |
| 2081   | No file  | `52d5767bf248`  |
| 2073   | No file  | `52d5767bf248`  |
| 2067   | No file  | `52d5767bf248`  |
| 2063   | No file  | `52d5767bf248`  |
| 2059   | No file  | `52d5767bf248`  |
| 2052   | No file  | `52d5767bf248`  |
| 2044   | No file  | `52d5767bf248`  |
| 2039   | No file  | `52d5767bf248`  |
| 2032   | No file  | `52d5767bf248`  |
| 2025   | No file  | `52d5767bf248`  |
| 2011   | No file  | `52d5767bf248`  |
| 2005   | No file  | `52d5767bf248`  |
| 2000   | No file  | `52d5767bf248`  |
| 1996   | No file  | `52d5767bf248`  |
| 1991   | No file  | `52d5767bf248`  |
| 1985   | No file  | `52d5767bf248`  |
| 1980   | No file  | `52d5767bf248`  |
| 1969   | No file  | `52d5767bf248`  |
| 1964   | No file  | `52d5767bf248`  |
| 1958   | No file  | `52d5767bf248`  |
| 1950   | No file  | `52d5767bf248`  |
| 1945   | No file  | `52d5767bf248`  |
| 1937   | No file  | `52d5767bf248`  |
| 1933   | No file  | `52d5767bf248`  |
| 1927   | No file  | `52d5767bf248`  |
| 1921   | No file  | `52d5767bf248`  |
| 1914   | No file  | `52d5767bf248`  |
| 1908   | No file  | `52d5767bf248`  |
| 1897   | No file  | `52d5767bf248`  |
| 1892   | No file  | `52d5767bf248`  |
| 1886   | No file  | `52d5767bf248`  |
| 1881   | No file  | `52d5767bf248`  |
| 1871   | No file  | `52d5767bf248`  |
| 1866   | No file  | `52d5767bf248`  |
| 1862   | No file  | `52d5767bf248`  |
| 1854   | No file  | `52d5767bf248`  |
| 1846   | No file  | `52d5767bf248`  |
| 1838   | No file  | `52d5767bf248`  |
| 1832   | No file  | `52d5767bf248`  |
| 1826   | No file  | `52d5767bf248`  |
| 1822   | No file  | `52d5767bf248`  |
| 1818   | No file  | `52d5767bf248`  |
| 1804   | No file  | `52d5767bf248`  |
| 1794   | No file  | `52d5767bf248`  |
| 1790   | No file  | `52d5767bf248`  |
| 1784   | No file  | `52d5767bf248`  |
| 1774   | No file  | `52d5767bf248`  |
| 1771   | No file  | `52d5767bf248`  |
| 1762   | No file  | `52d5767bf248`  |
| 1759   | No file  | `52d5767bf248`  |
| 1754   | No file  | `52d5767bf248`  |
| 1749   | No file  | `52d5767bf248`  |
| 1743   | No file  | `52d5767bf248`  |
| 1737   | No file  | `52d5767bf248`  |
| 1731   | No file  | `52d5767bf248`  |
| 1725   | No file  | `52d5767bf248`  |
| 1717   | No file  | `52d5767bf248`  |
| 1710   | No file  | `52d5767bf248`  |
| 1704   | No file  | `52d5767bf248`  |
| 1698   | No file  | `52d5767bf248`  |
| 1690   | No file  | `52d5767bf248`  |
| 1685   | No file  | `52d5767bf248`  |
| 1680   | No file  | `52d5767bf248`  |
| 1674   | No file  | `52d5767bf248`  |
| 1668   | No file  | `52d5767bf248`  |
| 1659   | No file  | `52d5767bf248`  |
| 1649   | No file  | `52d5767bf248`  |
| 1642   | No file  | `52d5767bf248`  |
| 1636   | No file  | `52d5767bf248`  |
| 1628   | No file  | `52d5767bf248`  |
| 1622   | No file  | `52d5767bf248`  |
| 1614   | No file  | `52d5767bf248`  |
| 1608   | No file  | `52d5767bf248`  |
| 1602   | No file  | `52d5767bf248`  |
| 1598   | No file  | `52d5767bf248`  |
| 1594   | No file  | `52d5767bf248`  |
| 1590   | No file  | `52d5767bf248`  |
| 1587   | No file  | `52d5767bf248`  |
| 1584   | No file  | `52d5767bf248`  |
| 1579   | No file  | `52d5767bf248`  |
| 1572   | No file  | `52d5767bf248`  |
| 1565   | No file  | `52d5767bf248`  |
| 1559   | No file  | `52d5767bf248`  |
| 1554   | No file  | `52d5767bf248`  |
| 1547   | No file  | `52d5767bf248`  |
| 1537   | No file  | `52d5767bf248`  |
| 1529   | No file  | `52d5767bf248`  |
| 1524   | No file  | `52d5767bf248`  |
| 1519   | No file  | `52d5767bf248`  |
| 1509   | No file  | `52d5767bf248`  |
| 1506   | No file  | `52d5767bf248`  |
| 1504   | No file  | `52d5767bf248`  |
| 1500   | No file  | `52d5767bf248`  |
| 1493   | No file  | `52d5767bf248`  |
| 1489   | No file  | `52d5767bf248`  |
| 1485   | No file  | `52d5767bf248`  |
| 1481   | No file  | `52d5767bf248`  |
| 1474   | No file  | `52d5767bf248`  |
| 1466   | No file  | `52d5767bf248`  |
| 1462   | No file  | `52d5767bf248`  |
| 1459   | No file  | `52d5767bf248`  |
| 1453   | No file  | `52d5767bf248`  |
| 1450   | No file  | `52d5767bf248`  |
| 1445   | No file  | `52d5767bf248`  |
| 1439   | No file  | `52d5767bf248`  |
| 1433   | No file  | `52d5767bf248`  |
| 1430   | No file  | `52d5767bf248`  |
| 1426   | No file  | `52d5767bf248`  |
| 1421   | No file  | `52d5767bf248`  |
| 1417   | No file  | `52d5767bf248`  |
| 1416   | No file  | `52d5767bf248`  |
| 1409   | No file  | `52d5767bf248`  |
| 1405   | No file  | `52d5767bf248`  |
| 1401   | No file  | `52d5767bf248`  |
| 1396   | No file  | `52d5767bf248`  |
| 1391   | No file  | `52d5767bf248`  |
| 1390   | No file  | `52d5767bf248`  |
| 1386   | No file  | `52d5767bf248`  |
| 1381   | No file  | `52d5767bf248`  |
| 1379   | No file  | `52d5767bf248`  |
| 1372   | No file  | `52d5767bf248`  |
| 1366   | No file  | `52d5767bf248`  |
| 1364   | No file  | `52d5767bf248`  |
| 1363   | No file  | `52d5767bf248`  |
| 1360   | No file  | `52d5767bf248`  |
| 1358   | No file  | `52d5767bf248`  |
| 1355   | No file  | `52d5767bf248`  |
| 1351   | No file  | `52d5767bf248`  |
| 1348   | No file  | `52d5767bf248`  |
| 1346   | No file  | `52d5767bf248`  |
| 1341   | No file  | `52d5767bf248`  |
| 1340   | No file  | `52d5767bf248`  |
| 1338   | No file  | `52d5767bf248`  |
| 1335   | No file  | `52d5767bf248`  |
| 1333   | No file  | `52d5767bf248`  |
| 1329   | No file  | `52d5767bf248`  |
| 1327   | No file  | `52d5767bf248`  |
| 1324   | No file  | `52d5767bf248`  |
| 1321   | No file  | `52d5767bf248`  |
| 1319   | No file  | `52d5767bf248`  |
| 1318   | No file  | `52d5767bf248`  |
| 1316   | No file  | `52d5767bf248`  |
| 1313   | No file  | `52d5767bf248`  |
| 1311   | No file  | `52d5767bf248`  |
| 1309   | No file  | `52d5767bf248`  |
| 1304   | No file  | `52d5767bf248`  |
| 1292   | No file  | `52d5767bf248`  |
| 1286   | No file  | `52d5767bf248`  |
| 1280   | No file  | `52d5767bf248`  |
| 1276   | No file  | `52d5767bf248`  |
| 1267   | No file  | `52d5767bf248`  |
| 1261   | No file  | `52d5767bf248`  |
| 1256   | No file  | `52d5767bf248`  |
| 1250   | No file  | `52d5767bf248`  |
| 1246   | No file  | `52d5767bf248`  |
| 1239   | No file  | `52d5767bf248`  |
| 1230   | No file  | `52d5767bf248`  |
| 1226   | No file  | `52d5767bf248`  |
| 1220   | No file  | `52d5767bf248`  |
| 1217   | No file  | `52d5767bf248`  |
| 1211   | No file  | `52d5767bf248`  |
| 1210   | No file  | `52d5767bf248`  |
| 1208   | No file  | `52d5767bf248`  |
| 1203   | No file  | `52d5767bf248`  |
| 1197   | No file  | `52d5767bf248`  |
| 1194   | No file  | `52d5767bf248`  |
| 1192   | No file  | `52d5767bf248`  |
| 1187   | No file  | `52d5767bf248`  |
| 1183   | No file  | `52d5767bf248`  |
| 1177   | No file  | `52d5767bf248`  |
| 1173   | No file  | `52d5767bf248`  |
| 1167   | No file  | `52d5767bf248`  |
| 1164   | No file  | `52d5767bf248`  |
| 1156   | No file  | `52d5767bf248`  |
| 1149   | No file  | `52d5767bf248`  |
| 1144   | No file  | `52d5767bf248`  |
| 1137   | No file  | `52d5767bf248`  |
| 1132   | No file  | `52d5767bf248`  |
| 1127   | No file  | `52d5767bf248`  |
| 1122   | No file  | `52d5767bf248`  |
| 1118   | No file  | `52d5767bf248`  |
| 1114   | No file  | `52d5767bf248`  |
| 1109   | No file  | `52d5767bf248`  |
| 1102   | No file  | `52d5767bf248`  |
| 1096   | No file  | `52d5767bf248`  |
| 1088   | No file  | `52d5767bf248`  |
| 1081   | No file  | `52d5767bf248`  |
| 1076   | No file  | `52d5767bf248`  |
| 1069   | No file  | `52d5767bf248`  |
| 1064   | No file  | `52d5767bf248`  |
| 1058   | No file  | `52d5767bf248`  |
| 1051   | No file  | `52d5767bf248`  |
| 1044   | No file  | `52d5767bf248`  |
| 1036   | No file  | `52d5767bf248`  |
| 1026   | No file  | `52d5767bf248`  |
| 1016   | No file  | `52d5767bf248`  |
| 1009   | No file  | `52d5767bf248`  |
| 1005   | No file  | `52d5767bf248`  |
| 1000   | No file  | `52d5767bf248`  |
| 998    | No file  | `52d5767bf248`  |
| 990    | No file  | `52d5767bf248`  |
| 979    | No file  | `52d5767bf248`  |
| 972    | No file  | `52d5767bf248`  |
| 963    | No file  | `52d5767bf248`  |
| 955    | No file  | `52d5767bf248`  |
| 946    | No file  | `52d5767bf248`  |
| 938    | No file  | `52d5767bf248`  |
| 927    | No file  | `52d5767bf248`  |
| 911    | No file  | `52d5767bf248`  |
| 904    | No file  | `52d5767bf248`  |
| 899    | No file  | `52d5767bf248`  |
| 894    | No file  | `52d5767bf248`  |
| 885    | No file  | `52d5767bf248`  |
| 879    | No file  | `52d5767bf248`  |
| 872    | No file  | `52d5767bf248`  |
| 864    | No file  | `52d5767bf248`  |
| 855    | No file  | `52d5767bf248`  |
| 853    | No file  | `52d5767bf248`  |
| 845    | No file  | `52d5767bf248`  |
| 837    | No file  | `52d5767bf248`  |
| 829    | No file  | `52d5767bf248`  |
| 822    | No file  | `52d5767bf248`  |
| 814    | No file  | `52d5767bf248`  |
| 805    | No file  | `52d5767bf248`  |
| 794    | No file  | `52d5767bf248`  |
| 787    | No file  | `52d5767bf248`  |
| 780    | No file  | `52d5767bf248`  |
| 771    | No file  | `52d5767bf248`  |
| 760    | No file  | `52d5767bf248`  |
| 748    | No file  | `52d5767bf248`  |
| 741    | No file  | `52d5767bf248`  |
| 736    | No file  | `52d5767bf248`  |
| 731    | No file  | `52d5767bf248`  |
| 723    | No file  | `52d5767bf248`  |
| 711    | No file  | `52d5767bf248`  |
| 707    | No file  | `52d5767bf248`  |
| 697    | No file  | `52d5767bf248`  |
| 689    | No file  | `52d5767bf248`  |
| 683    | No file  | `52d5767bf248`  |
| 678    | No file  | `52d5767bf248`  |
| 670    | No file  | `52d5767bf248`  |
| 661    | No file  | `52d5767bf248`  |
| 656    | No file  | `52d5767bf248`  |
| 652    | No file  | `52d5767bf248`  |
| 643    | No file  | `52d5767bf248`  |
| 637    | No file  | `52d5767bf248`  |
| 630    | No file  | `52d5767bf248`  |
| 627    | No file  | `52d5767bf248`  |
| 621    | No file  | `52d5767bf248`  |
| 617    | No file  | `52d5767bf248`  |
| 615    | No file  | `52d5767bf248`  |
| 606    | No file  | `52d5767bf248`  |
| 599    | No file  | `52d5767bf248`  |
| 592    | No file  | `52d5767bf248`  |
| 586    | No file  | `52d5767bf248`  |
| 577    | No file  | `52d5767bf248`  |
| 569    | No file  | `52d5767bf248`  |
| 561    | No file  | `52d5767bf248`  |
| 554    | No file  | `52d5767bf248`  |
| 542    | No file  | `52d5767bf248`  |
| 532    | No file  | `52d5767bf248`  |
| 531    | No file  | `52d5767bf248`  |
| 526    | No file  | `52d5767bf248`  |
| 521    | No file  | `52d5767bf248`  |
| 517    | No file  | `52d5767bf248`  |
| 510    | No file  | `52d5767bf248`  |
| 508    | No file  | `52d5767bf248`  |
| 504    | No file  | `52d5767bf248`  |
| 497    | No file  | `52d5767bf248`  |
| 491    | No file  | `52d5767bf248`  |
| 485    | No file  | `52d5767bf248`  |
| 478    | No file  | `52d5767bf248`  |
| 472    | No file  | `52d5767bf248`  |
| 466    | No file  | `52d5767bf248`  |
| 457    | No file  | `52d5767bf248`  |
| 452    | No file  | `52d5767bf248`  |
| 449    | No file  | `52d5767bf248`  |
| 435    | No file  | `52d5767bf248`  |

<!-- versions:end -->

## Companion Files

None. The handler names the items of each enchant key through the
`ENCHANT_KEY_ITEMS` lookup index (see `docs/handler.md`), built from
[`itemenchant.dbss`](../dbss/itemenchant_dbss.md), and LOC type 0 for the item names.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                 |
| ------- | ---------- | ----- | ------------------------------------- |
| `+0x00` | u32        | count | Number of rows; 1,146 on client 3473  |
| `+0x04` | Row[count] | rows  | See Row                               |

The rows are not sorted by key: client 3473 opens with keys 1143, 3046 and
25815.

### Row (variable: 16 bytes + group keys)

| Offset  | Type             | Field              | Notes                                                                              |
| ------- | ---------------- | ------------------ | ---------------------------------------------------------------------------------- |
| `+0x00` | u32              | enchant_key        | `enchantstaticstatus.dbss` enchant key; unique                                     |
| `+0x04` | u32              | unknown_04         | Equals `group_count` on all 1,146 rows (client 3473)                               |
| `+0x08` | u64              | group_count        | Number of `group_enchant_keys`; 1 to 153 on client 3473                            |
| `+0x10` | u32[group_count] | group_enchant_keys | Every enchant key of the group, `enchant_key` included                             |

`group_enchant_keys` is in ascending order on 1,084 of the 1,146 rows (client
3473); the others keep an order of their own, the same on every row of the
group (29787, 29784, 29781, 29778, ... and 684, 484, 284, 84).

## Groups

Counted on client 3473:

| Check                                                                 | Result                 |
| --------------------------------------------------------------------- | ---------------------- |
| `enchant_key` found as an `enchantstaticstatus.dbss` enchant key       | 1,146 of 1,146 rows    |
| `enchant_key` stored by an `itemenchant.dbss` base item               | 1,036 of 1,146 rows    |
| Group keys without a row of their own                                 | 0                      |
| Rows whose list differs from the lists of its group keys             | 0                      |
| Groups (distinct lists)                                               | 280, 166 of one key    |
| Groups of two or more keys with the same success chance, material, material count, failure result and downgrade chance at each level | 114 of 114 |
| Of those, with the same max durability at each level                  | 103 of 114             |

Equal enhancement data does not make two keys one group: 18 groups share
their data with another group (the four Blackstar armor groups, each a piece
with its Obsidian version; the Fiery Sovereign two-handed weapons and the
Fiery Sovereign main weapons), and 166 enhanceable keys outside the file
have the same data as a group. Of the 602 enhanceable keys outside the file
that an item stores, 410 hold an item with the name of an item in the file,
such as the `Kzarka Longsword` of key 3222 (items 734408 and 734422) next to
the Kzarka group of key 62.

## Another Adventurer's Choice

The window is `panel_otheruser_additionalrate_all.luac` with
`panel_window_otheruser_additionalrate_all.xml`. It lists the failstack
ranges other players used, five stacks wide
(`ToClient_GetOthersChoiceStackByIndex(i) * 5`), with a percentage each
(`ToClient_GetOthersChoicePercentByIndex(i)`), under "The most frequently
attempted Enhancement Chance for this gear by other Adventurers". The ranges
come from the server (`ToClient_RequestOthersChoice()`); no Lua names this
file, so the link rests on the in-game readings below.

The enhancement window shows the window's button when the exe check
`ToClient_CanShowOthersChoice()` is true (`panel_widget_enchant_main_all_1.luac`),
and hides it for gear that can change to Tuvala or a guaranteed enhancement.
On client 3474 the button showed for every key of this file opened below and
not for a PRI: Tati Godr Sphera (item 14813, key `2103`), a marketable
awakening weapon that enhances to +20 and whose key is not in the file.

On client 3474 the window showed these ranges, each pair read a few minutes
apart at the same enhancement level.

All five at +14:

| Range     | Rosar Longsword (`52`) | Bares Staff (`437`) | Grunil Helmet (`5164`) | Agerian Gloves (`5066`) | Akum Helmet (`5281`) |
| --------- | ---------------------- | ------------------- | ---------------------- | ----------------------- | -------------------- |
| +0 ~ +4   | 22%                    | 22%                 | 24%                    | 24%                     | 17%                  |
| +5 ~ +9   | 20%                    | 20%                 | 28%                    | 28%                     | 19%                  |
| +10 ~ +14 | 16%                    | 16%                 | 16%                    | 16%                     | 15%                  |
| +15 ~ +19 | 15%                    | 15%                 | 10%                    | 10%                     | 13%                  |
| +20 ~ +24 | 6%                     | 6%                  | 6%                     | 6%                      | 9%                   |

Both at PEN:

| Range       | PEN: Sovereign Staff (`3677`) | PEN: Fiery Sovereign Godr Sphera (`3683`) |
| ----------- | ----------------------------- | ----------------------------------------- |
| +265 ~ +269 | 9%                            | 9%                                        |
| +260 ~ +264 | 8%                            | 8%                                        |
| +270 ~ +274 | 6%                            | 7%                                        |
| +225 ~ +229 | 5%                            | 5%                                        |
| +220 ~ +224 | 5%                            | 5%                                        |

At PRI:

| Range     | PRI: Red Coral Ring (`9018`) | PRI: Blue Coral Ring (`9017`) |
| --------- | ---------------------------- | ----------------------------- |
| +30 ~ +34 | 59%                          | 61%                           |
| +35 ~ +39 | 14%                          | 13%                           |
| +40 ~ +44 | 12%                          | 13%                           |
| +25 ~ +29 | 3%                           | 2%                            |
| +20 ~ +24 | 2%                           | 2%                            |

| Items                                        | Same group | Same slot | Same grade | Ranges    |
| -------------------------------------------- | ---------- | --------- | ---------- | --------- |
| Rosar Longsword, Bares Staff                 | yes        | no        | yes        | same      |
| Grunil Helmet, Agerian Gloves                | yes        | no        | yes        | same      |
| Rosar Longsword, Grunil Helmet               | no         | no        | yes        | different |
| Grunil Helmet, Akum Helmet                   | no         | yes       | no         | different |
| Red Coral Ring, Blue Coral Ring              | no         | yes       | yes        | different |
| Sovereign Staff, Fiery Sovereign Godr Sphera | no         | no        | yes        | different |

Rosar, Bares, Grunil and Agerian are grade `1`, Akum and both coral rings
grade `2` (`itemenchant.dbss`). Items of one group give the same ranges
across weapon types and armor slots, and the two coral rings differ although
slot and grade match, so neither slot nor grade decides the count.

## Notes

- Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
  1784 has this table, and the client 1784 PAZ has no
  `itemviewstackenchantgroupss.bss`. No client Lua script names the file or
  its rows. The field names come from the join with
  `enchantstaticstatus.dbss` and the counts in the table above.
- Read as item IDs, the group keys name unrelated items (key 10 is Crow
  Coin, 12 and 16 Pure Black Stone, 21 Bartali Gold Bar in one group); as
  enchant keys the same group is the Rusty, Elsh and Azwell longswords.

## Open Questions

### Second Group Count at +0x04

`unknown_04` equals `group_count` on all 1,146 rows (client 3473). Why the
row stores the count twice, once as u32 and once as u64, is unknown.
