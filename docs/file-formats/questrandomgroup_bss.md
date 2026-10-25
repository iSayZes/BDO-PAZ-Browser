# `questrandomgroup.bss` Format

## Purpose

The random quest groups that the quest condition `checkRandomGroup(group, index)` in [`quest.dbss`](quest_dbss.md) reads. Each 32-byte row names a group key, the number of quest slots in the group and the quest chain they belong to. On client 3474 the file holds one group: key `1`, 37 slots, chain 2322, the `[Academy] [Weekly ...]` quests of the Olvia Academy. The plain PABR file holds the rows, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records               | Row bytes |
| ------ | -------------- | ---------------------- | ----- | --------------------- | --------- |
| 1      | 3125 and later | `questrandomgroup.bss` | 52    | 1 Row, 1 String Table | 32        |

| Layout | File                   | Known        | Unknown      |
| ------ | ---------------------- | ------------ | ------------ |
| 1      | `questrandomgroup.bss` | 30 B (57.7%) | 22 B (42.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `c5b2ad30717f`  |
| 3482   | Layout 1             | `c5b2ad30717f`  |
| 3474   | Layout 1             | `c5b2ad30717f`  |
| 3473   | Layout 1             | `c5b2ad30717f`  |
| 3464   | Layout 1             | `c5b2ad30717f`  |
| 3458   | Layout 1             | `c5b2ad30717f`  |
| 3454   | Layout 1             | `c5b2ad30717f`  |
| 3444   | Layout 1             | `c5b2ad30717f`  |
| 3435   | Layout 1             | `c5b2ad30717f`  |
| 3426   | Layout 1             | `c5b2ad30717f`  |
| 3418   | Layout 1             | `c5b2ad30717f`  |
| 3412   | Layout 1             | `c5b2ad30717f`  |
| 3402   | Layout 1             | `c5b2ad30717f`  |
| 3396   | Layout 1             | `c5b2ad30717f`  |
| 3387   | Layout 1             | `c5b2ad30717f`  |
| 3381   | Layout 1             | `c5b2ad30717f`  |
| 3373   | Layout 1             | `c5b2ad30717f`  |
| 3364   | Layout 1             | `c5b2ad30717f`  |
| 3356   | Layout 1             | `c5b2ad30717f`  |
| 3349   | Layout 1             | `c5b2ad30717f`  |
| 3342   | Layout 1             | `c5b2ad30717f`  |
| 3335   | Layout 1             | `c5b2ad30717f`  |
| 3326   | Layout 1             | `c5b2ad30717f`  |
| 3321   | Layout 1             | `c5b2ad30717f`  |
| 3314   | Layout 1             | `c5b2ad30717f`  |
| 3303   | Layout 1             | `c5b2ad30717f`  |
| 3302   | Layout 1             | `c5b2ad30717f`  |
| 3293   | Layout 1             | `c5b2ad30717f`  |
| 3283   | Layout 1             | `c5b2ad30717f`  |
| 3275   | Layout 1             | `c5b2ad30717f`  |
| 3267   | Layout 1             | `c5b2ad30717f`  |
| 3258   | Layout 1             | `c5b2ad30717f`  |
| 3251   | Layout 1             | `c5b2ad30717f`  |
| 3242   | Layout 1             | `c5b2ad30717f`  |
| 3235   | Layout 1             | `c5b2ad30717f`  |
| 3229   | Layout 1             | `c5b2ad30717f`  |
| 3212   | Layout 1             | `c5b2ad30717f`  |
| 3203   | Layout 1             | `c5b2ad30717f`  |
| 3193   | Layout 1             | `c5b2ad30717f`  |
| 3186   | Layout 1             | `c5b2ad30717f`  |
| 3177   | No documented layout | `c5b2ad30717f`  |
| 3169   | No documented layout | `c5b2ad30717f`  |
| 3158   | Layout 1             | `c5b2ad30717f`  |
| 3151   | Layout 1             | `c5b2ad30717f`  |
| 3144   | Layout 1             | `c5b2ad30717f`  |
| 3133   | Layout 1             | `c5b2ad30717f`  |
| 3125   | Layout 1             | `c5b2ad30717f`  |
| 3118   | No file              | `c5b2ad30717f`  |
| 3111   | No file              | `c5b2ad30717f`  |
| 3103   | No file              | `c5b2ad30717f`  |
| 3095   | No file              | `c5b2ad30717f`  |
| 3086   | No file              | `c5b2ad30717f`  |
| 3072   | No file              | `c5b2ad30717f`  |
| 3062   | No file              | `c5b2ad30717f`  |
| 3052   | No file              | `c5b2ad30717f`  |
| 3045   | No file              | `c5b2ad30717f`  |
| 3037   | No file              | `c5b2ad30717f`  |
| 3030   | No file              | `c5b2ad30717f`  |
| 3021   | No file              | `c5b2ad30717f`  |
| 3012   | No file              | `c5b2ad30717f`  |
| 3002   | No file              | `c5b2ad30717f`  |
| 2995   | No file              | `c5b2ad30717f`  |
| 2987   | No file              | `c5b2ad30717f`  |
| 2978   | No file              | `c5b2ad30717f`  |
| 2970   | No file              | `c5b2ad30717f`  |
| 2959   | No file              | `c5b2ad30717f`  |
| 2951   | No file              | `c5b2ad30717f`  |
| 2942   | No file              | `c5b2ad30717f`  |
| 2935   | No file              | `c5b2ad30717f`  |
| 2932   | No file              | `c5b2ad30717f`  |
| 2923   | No file              | `c5b2ad30717f`  |
| 2919   | No file              | `c5b2ad30717f`  |
| 2907   | No file              | `c5b2ad30717f`  |
| 2900   | No file              | `c5b2ad30717f`  |
| 2891   | No file              | `c5b2ad30717f`  |
| 2882   | No file              | `c5b2ad30717f`  |
| 2872   | No file              | `c5b2ad30717f`  |
| 2863   | No file              | `c5b2ad30717f`  |
| 2855   | No file              | `c5b2ad30717f`  |
| 2849   | No file              | `c5b2ad30717f`  |
| 2844   | No file              | `c5b2ad30717f`  |
| 2834   | No file              | `c5b2ad30717f`  |
| 2825   | No file              | `c5b2ad30717f`  |
| 2819   | No file              | `c5b2ad30717f`  |
| 2811   | No file              | `c5b2ad30717f`  |
| 2803   | No file              | `c5b2ad30717f`  |
| 2794   | No file              | `c5b2ad30717f`  |
| 2783   | No file              | `c5b2ad30717f`  |
| 2774   | No file              | `c5b2ad30717f`  |
| 2765   | No file              | `c5b2ad30717f`  |
| 2756   | No file              | `c5b2ad30717f`  |
| 2750   | No file              | `c5b2ad30717f`  |
| 2743   | No file              | `c5b2ad30717f`  |
| 2736   | No file              | `c5b2ad30717f`  |
| 2726   | No file              | `c5b2ad30717f`  |
| 2717   | No file              | `c5b2ad30717f`  |
| 2709   | No file              | `c5b2ad30717f`  |
| 2703   | No file              | `c5b2ad30717f`  |
| 2695   | No file              | `c5b2ad30717f`  |
| 2684   | No file              | `c5b2ad30717f`  |
| 2672   | No file              | `c5b2ad30717f`  |
| 2665   | No file              | `c5b2ad30717f`  |
| 2657   | No file              | `c5b2ad30717f`  |
| 2649   | No file              | `c5b2ad30717f`  |
| 2644   | No file              | `c5b2ad30717f`  |
| 2637   | No file              | `c5b2ad30717f`  |
| 2629   | No file              | `c5b2ad30717f`  |
| 2619   | No file              | `c5b2ad30717f`  |
| 2612   | No file              | `c5b2ad30717f`  |
| 2606   | No file              | `c5b2ad30717f`  |
| 2602   | No file              | `c5b2ad30717f`  |
| 2601   | No file              | `c5b2ad30717f`  |
| 2592   | No file              | `c5b2ad30717f`  |
| 2583   | No file              | `c5b2ad30717f`  |
| 2575   | No file              | `c5b2ad30717f`  |
| 2567   | No file              | `c5b2ad30717f`  |
| 2560   | No file              | `c5b2ad30717f`  |
| 2553   | No file              | `c5b2ad30717f`  |
| 2545   | No file              | `c5b2ad30717f`  |
| 2538   | No file              | `c5b2ad30717f`  |
| 2529   | No file              | `c5b2ad30717f`  |
| 2519   | No file              | `c5b2ad30717f`  |
| 2513   | No file              | `c5b2ad30717f`  |
| 2510   | No file              | `c5b2ad30717f`  |
| 2507   | No file              | `c5b2ad30717f`  |
| 2503   | No file              | `c5b2ad30717f`  |
| 2498   | No file              | `c5b2ad30717f`  |
| 2492   | No file              | `c5b2ad30717f`  |
| 2487   | No file              | `c5b2ad30717f`  |
| 2480   | No file              | `c5b2ad30717f`  |
| 2474   | No file              | `c5b2ad30717f`  |
| 2468   | No file              | `c5b2ad30717f`  |
| 2460   | No file              | `c5b2ad30717f`  |
| 2453   | No file              | `c5b2ad30717f`  |
| 2444   | No file              | `c5b2ad30717f`  |
| 2438   | No file              | `c5b2ad30717f`  |
| 2434   | No file              | `c5b2ad30717f`  |
| 2429   | No file              | `c5b2ad30717f`  |
| 2421   | No file              | `c5b2ad30717f`  |
| 2414   | No file              | `c5b2ad30717f`  |
| 2407   | No file              | `c5b2ad30717f`  |
| 2401   | No file              | `c5b2ad30717f`  |
| 2397   | No file              | `c5b2ad30717f`  |
| 2393   | No file              | `c5b2ad30717f`  |
| 2384   | No file              | `c5b2ad30717f`  |
| 2378   | No file              | `c5b2ad30717f`  |
| 2372   | No file              | `c5b2ad30717f`  |
| 2358   | No file              | `c5b2ad30717f`  |
| 2352   | No file              | `c5b2ad30717f`  |
| 2347   | No file              | `c5b2ad30717f`  |
| 2343   | No file              | `c5b2ad30717f`  |
| 2335   | No file              | `c5b2ad30717f`  |
| 2327   | No file              | `c5b2ad30717f`  |
| 2324   | No file              | `c5b2ad30717f`  |
| 2319   | No file              | `c5b2ad30717f`  |
| 2313   | No file              | `c5b2ad30717f`  |
| 2308   | No file              | `c5b2ad30717f`  |
| 2302   | No file              | `c5b2ad30717f`  |
| 2295   | No file              | `c5b2ad30717f`  |
| 2290   | No file              | `c5b2ad30717f`  |
| 2284   | No file              | `c5b2ad30717f`  |
| 2276   | No file              | `c5b2ad30717f`  |
| 2269   | No file              | `c5b2ad30717f`  |
| 2259   | No file              | `c5b2ad30717f`  |
| 2250   | No file              | `c5b2ad30717f`  |
| 2243   | No file              | `c5b2ad30717f`  |
| 2235   | No file              | `c5b2ad30717f`  |
| 2229   | No file              | `c5b2ad30717f`  |
| 2224   | No file              | `c5b2ad30717f`  |
| 2218   | No file              | `c5b2ad30717f`  |
| 2215   | No file              | `c5b2ad30717f`  |
| 2207   | No file              | `c5b2ad30717f`  |
| 2203   | No file              | `c5b2ad30717f`  |
| 2196   | No file              | `c5b2ad30717f`  |
| 2192   | No file              | `c5b2ad30717f`  |
| 2189   | No file              | `c5b2ad30717f`  |
| 2183   | No file              | `c5b2ad30717f`  |
| 2179   | No file              | `c5b2ad30717f`  |
| 2171   | No file              | `c5b2ad30717f`  |
| 2163   | No file              | `c5b2ad30717f`  |
| 2156   | No file              | `c5b2ad30717f`  |
| 2151   | No file              | `c5b2ad30717f`  |
| 2147   | No file              | `c5b2ad30717f`  |
| 2142   | No file              | `c5b2ad30717f`  |
| 2138   | No file              | `c5b2ad30717f`  |
| 2134   | No file              | `c5b2ad30717f`  |
| 2130   | No file              | `c5b2ad30717f`  |
| 2122   | No file              | `c5b2ad30717f`  |
| 2107   | No file              | `c5b2ad30717f`  |
| 2098   | No file              | `c5b2ad30717f`  |
| 2089   | No file              | `c5b2ad30717f`  |
| 2081   | No file              | `c5b2ad30717f`  |
| 2073   | No file              | `c5b2ad30717f`  |
| 2067   | No file              | `c5b2ad30717f`  |
| 2063   | No file              | `c5b2ad30717f`  |
| 2059   | No file              | `c5b2ad30717f`  |
| 2052   | No file              | `c5b2ad30717f`  |
| 2044   | No file              | `c5b2ad30717f`  |
| 2039   | No file              | `c5b2ad30717f`  |
| 2032   | No file              | `c5b2ad30717f`  |
| 2025   | No file              | `c5b2ad30717f`  |
| 2011   | No file              | `c5b2ad30717f`  |
| 2005   | No file              | `c5b2ad30717f`  |
| 2000   | No file              | `c5b2ad30717f`  |
| 1996   | No file              | `c5b2ad30717f`  |
| 1991   | No file              | `c5b2ad30717f`  |
| 1985   | No file              | `c5b2ad30717f`  |
| 1980   | No file              | `c5b2ad30717f`  |
| 1969   | No file              | `c5b2ad30717f`  |
| 1964   | No file              | `c5b2ad30717f`  |
| 1958   | No file              | `c5b2ad30717f`  |
| 1950   | No file              | `c5b2ad30717f`  |
| 1945   | No file              | `c5b2ad30717f`  |
| 1937   | No file              | `c5b2ad30717f`  |
| 1933   | No file              | `c5b2ad30717f`  |
| 1927   | No file              | `c5b2ad30717f`  |
| 1921   | No file              | `c5b2ad30717f`  |
| 1914   | No file              | `c5b2ad30717f`  |
| 1908   | No file              | `c5b2ad30717f`  |
| 1897   | No file              | `c5b2ad30717f`  |
| 1892   | No file              | `c5b2ad30717f`  |
| 1886   | No file              | `c5b2ad30717f`  |
| 1881   | No file              | `c5b2ad30717f`  |
| 1871   | No file              | `c5b2ad30717f`  |
| 1866   | No file              | `c5b2ad30717f`  |
| 1862   | No file              | `c5b2ad30717f`  |
| 1854   | No file              | `c5b2ad30717f`  |
| 1846   | No file              | `c5b2ad30717f`  |
| 1838   | No file              | `c5b2ad30717f`  |
| 1832   | No file              | `c5b2ad30717f`  |
| 1826   | No file              | `c5b2ad30717f`  |
| 1822   | No file              | `c5b2ad30717f`  |
| 1818   | No file              | `c5b2ad30717f`  |
| 1804   | No file              | `c5b2ad30717f`  |
| 1794   | No file              | `c5b2ad30717f`  |
| 1790   | No file              | `c5b2ad30717f`  |
| 1784   | No file              | `c5b2ad30717f`  |
| 1774   | No file              | `c5b2ad30717f`  |
| 1771   | No file              | `c5b2ad30717f`  |
| 1762   | No file              | `c5b2ad30717f`  |
| 1759   | No file              | `c5b2ad30717f`  |
| 1754   | No file              | `c5b2ad30717f`  |
| 1749   | No file              | `c5b2ad30717f`  |
| 1743   | No file              | `c5b2ad30717f`  |
| 1737   | No file              | `c5b2ad30717f`  |
| 1731   | No file              | `c5b2ad30717f`  |
| 1725   | No file              | `c5b2ad30717f`  |
| 1717   | No file              | `c5b2ad30717f`  |
| 1710   | No file              | `c5b2ad30717f`  |
| 1704   | No file              | `c5b2ad30717f`  |
| 1698   | No file              | `c5b2ad30717f`  |
| 1690   | No file              | `c5b2ad30717f`  |
| 1685   | No file              | `c5b2ad30717f`  |
| 1680   | No file              | `c5b2ad30717f`  |
| 1674   | No file              | `c5b2ad30717f`  |
| 1668   | No file              | `c5b2ad30717f`  |
| 1659   | No file              | `c5b2ad30717f`  |
| 1649   | No file              | `c5b2ad30717f`  |
| 1642   | No file              | `c5b2ad30717f`  |
| 1636   | No file              | `c5b2ad30717f`  |
| 1628   | No file              | `c5b2ad30717f`  |
| 1622   | No file              | `c5b2ad30717f`  |
| 1614   | No file              | `c5b2ad30717f`  |
| 1608   | No file              | `c5b2ad30717f`  |
| 1602   | No file              | `c5b2ad30717f`  |
| 1598   | No file              | `c5b2ad30717f`  |
| 1594   | No file              | `c5b2ad30717f`  |
| 1590   | No file              | `c5b2ad30717f`  |
| 1587   | No file              | `c5b2ad30717f`  |
| 1584   | No file              | `c5b2ad30717f`  |
| 1579   | No file              | `c5b2ad30717f`  |
| 1572   | No file              | `c5b2ad30717f`  |
| 1565   | No file              | `c5b2ad30717f`  |
| 1559   | No file              | `c5b2ad30717f`  |
| 1554   | No file              | `c5b2ad30717f`  |
| 1547   | No file              | `c5b2ad30717f`  |
| 1537   | No file              | `c5b2ad30717f`  |
| 1529   | No file              | `c5b2ad30717f`  |
| 1524   | No file              | `c5b2ad30717f`  |
| 1519   | No file              | `c5b2ad30717f`  |
| 1509   | No file              | `c5b2ad30717f`  |
| 1506   | No file              | `c5b2ad30717f`  |
| 1504   | No file              | `c5b2ad30717f`  |
| 1500   | No file              | `c5b2ad30717f`  |
| 1493   | No file              | `c5b2ad30717f`  |
| 1489   | No file              | `c5b2ad30717f`  |
| 1485   | No file              | `c5b2ad30717f`  |
| 1481   | No file              | `c5b2ad30717f`  |
| 1474   | No file              | `c5b2ad30717f`  |
| 1466   | No file              | `c5b2ad30717f`  |
| 1462   | No file              | `c5b2ad30717f`  |
| 1459   | No file              | `c5b2ad30717f`  |
| 1453   | No file              | `c5b2ad30717f`  |
| 1450   | No file              | `c5b2ad30717f`  |
| 1445   | No file              | `c5b2ad30717f`  |
| 1439   | No file              | `c5b2ad30717f`  |
| 1433   | No file              | `c5b2ad30717f`  |
| 1430   | No file              | `c5b2ad30717f`  |
| 1426   | No file              | `c5b2ad30717f`  |
| 1421   | No file              | `c5b2ad30717f`  |
| 1417   | No file              | `c5b2ad30717f`  |
| 1416   | No file              | `c5b2ad30717f`  |
| 1409   | No file              | `c5b2ad30717f`  |
| 1405   | No file              | `c5b2ad30717f`  |
| 1401   | No file              | `c5b2ad30717f`  |
| 1396   | No file              | `c5b2ad30717f`  |
| 1391   | No file              | `c5b2ad30717f`  |
| 1390   | No file              | `c5b2ad30717f`  |
| 1386   | No file              | `c5b2ad30717f`  |
| 1381   | No file              | `c5b2ad30717f`  |
| 1379   | No file              | `c5b2ad30717f`  |
| 1372   | No file              | `c5b2ad30717f`  |
| 1366   | No file              | `c5b2ad30717f`  |
| 1364   | No file              | `c5b2ad30717f`  |
| 1363   | No file              | `c5b2ad30717f`  |
| 1360   | No file              | `c5b2ad30717f`  |
| 1358   | No file              | `c5b2ad30717f`  |
| 1355   | No file              | `c5b2ad30717f`  |
| 1351   | No file              | `c5b2ad30717f`  |
| 1348   | No file              | `c5b2ad30717f`  |
| 1346   | No file              | `c5b2ad30717f`  |
| 1341   | No file              | `c5b2ad30717f`  |
| 1340   | No file              | `c5b2ad30717f`  |
| 1338   | No file              | `c5b2ad30717f`  |
| 1335   | No file              | `c5b2ad30717f`  |
| 1333   | No file              | `c5b2ad30717f`  |
| 1329   | No file              | `c5b2ad30717f`  |
| 1327   | No file              | `c5b2ad30717f`  |
| 1324   | No file              | `c5b2ad30717f`  |
| 1321   | No file              | `c5b2ad30717f`  |
| 1319   | No file              | `c5b2ad30717f`  |
| 1318   | No file              | `c5b2ad30717f`  |
| 1316   | No file              | `c5b2ad30717f`  |
| 1313   | No file              | `c5b2ad30717f`  |
| 1311   | No file              | `c5b2ad30717f`  |
| 1309   | No file              | `c5b2ad30717f`  |
| 1304   | No file              | `c5b2ad30717f`  |
| 1292   | No file              | `c5b2ad30717f`  |
| 1286   | No file              | `c5b2ad30717f`  |
| 1280   | No file              | `c5b2ad30717f`  |
| 1276   | No file              | `c5b2ad30717f`  |
| 1267   | No file              | `c5b2ad30717f`  |
| 1261   | No file              | `c5b2ad30717f`  |
| 1256   | No file              | `c5b2ad30717f`  |
| 1250   | No file              | `c5b2ad30717f`  |
| 1246   | No file              | `c5b2ad30717f`  |
| 1239   | No file              | `c5b2ad30717f`  |
| 1230   | No file              | `c5b2ad30717f`  |
| 1226   | No file              | `c5b2ad30717f`  |
| 1220   | No file              | `c5b2ad30717f`  |
| 1217   | No file              | `c5b2ad30717f`  |
| 1211   | No file              | `c5b2ad30717f`  |
| 1210   | No file              | `c5b2ad30717f`  |
| 1208   | No file              | `c5b2ad30717f`  |
| 1203   | No file              | `c5b2ad30717f`  |
| 1197   | No file              | `c5b2ad30717f`  |
| 1194   | No file              | `c5b2ad30717f`  |
| 1192   | No file              | `c5b2ad30717f`  |
| 1187   | No file              | `c5b2ad30717f`  |
| 1183   | No file              | `c5b2ad30717f`  |
| 1177   | No file              | `c5b2ad30717f`  |
| 1173   | No file              | `c5b2ad30717f`  |
| 1167   | No file              | `c5b2ad30717f`  |
| 1164   | No file              | `c5b2ad30717f`  |
| 1156   | No file              | `c5b2ad30717f`  |
| 1149   | No file              | `c5b2ad30717f`  |
| 1144   | No file              | `c5b2ad30717f`  |
| 1137   | No file              | `c5b2ad30717f`  |
| 1132   | No file              | `c5b2ad30717f`  |
| 1127   | No file              | `c5b2ad30717f`  |
| 1122   | No file              | `c5b2ad30717f`  |
| 1118   | No file              | `c5b2ad30717f`  |
| 1114   | No file              | `c5b2ad30717f`  |
| 1109   | No file              | `c5b2ad30717f`  |
| 1102   | No file              | `c5b2ad30717f`  |
| 1096   | No file              | `c5b2ad30717f`  |
| 1088   | No file              | `c5b2ad30717f`  |
| 1081   | No file              | `c5b2ad30717f`  |
| 1076   | No file              | `c5b2ad30717f`  |
| 1069   | No file              | `c5b2ad30717f`  |
| 1064   | No file              | `c5b2ad30717f`  |
| 1058   | No file              | `c5b2ad30717f`  |
| 1051   | No file              | `c5b2ad30717f`  |
| 1044   | No file              | `c5b2ad30717f`  |
| 1036   | No file              | `c5b2ad30717f`  |
| 1026   | No file              | `c5b2ad30717f`  |
| 1016   | No file              | `c5b2ad30717f`  |
| 1009   | No file              | `c5b2ad30717f`  |
| 1005   | No file              | `c5b2ad30717f`  |
| 1000   | No file              | `c5b2ad30717f`  |
| 998    | No file              | `c5b2ad30717f`  |
| 990    | No file              | `c5b2ad30717f`  |
| 979    | No file              | `c5b2ad30717f`  |
| 972    | No file              | `c5b2ad30717f`  |
| 963    | No file              | `c5b2ad30717f`  |
| 955    | No file              | `c5b2ad30717f`  |
| 946    | No file              | `c5b2ad30717f`  |
| 938    | No file              | `c5b2ad30717f`  |
| 927    | No file              | `c5b2ad30717f`  |
| 911    | No file              | `c5b2ad30717f`  |
| 904    | No file              | `c5b2ad30717f`  |
| 899    | No file              | `c5b2ad30717f`  |
| 894    | No file              | `c5b2ad30717f`  |
| 885    | No file              | `c5b2ad30717f`  |
| 879    | No file              | `c5b2ad30717f`  |
| 872    | No file              | `c5b2ad30717f`  |
| 864    | No file              | `c5b2ad30717f`  |
| 855    | No file              | `c5b2ad30717f`  |
| 853    | No file              | `c5b2ad30717f`  |
| 845    | No file              | `c5b2ad30717f`  |
| 837    | No file              | `c5b2ad30717f`  |
| 829    | No file              | `c5b2ad30717f`  |
| 822    | No file              | `c5b2ad30717f`  |
| 814    | No file              | `c5b2ad30717f`  |
| 805    | No file              | `c5b2ad30717f`  |
| 794    | No file              | `c5b2ad30717f`  |
| 787    | No file              | `c5b2ad30717f`  |
| 780    | No file              | `c5b2ad30717f`  |
| 771    | No file              | `c5b2ad30717f`  |
| 760    | No file              | `c5b2ad30717f`  |
| 748    | No file              | `c5b2ad30717f`  |
| 741    | No file              | `c5b2ad30717f`  |
| 736    | No file              | `c5b2ad30717f`  |
| 731    | No file              | `c5b2ad30717f`  |
| 723    | No file              | `c5b2ad30717f`  |
| 711    | No file              | `c5b2ad30717f`  |
| 707    | No file              | `c5b2ad30717f`  |
| 697    | No file              | `c5b2ad30717f`  |
| 689    | No file              | `c5b2ad30717f`  |
| 683    | No file              | `c5b2ad30717f`  |
| 678    | No file              | `c5b2ad30717f`  |
| 670    | No file              | `c5b2ad30717f`  |
| 661    | No file              | `c5b2ad30717f`  |
| 656    | No file              | `c5b2ad30717f`  |
| 652    | No file              | `c5b2ad30717f`  |
| 643    | No file              | `c5b2ad30717f`  |
| 637    | No file              | `c5b2ad30717f`  |
| 630    | No file              | `c5b2ad30717f`  |
| 627    | No file              | `c5b2ad30717f`  |
| 621    | No file              | `c5b2ad30717f`  |
| 617    | No file              | `c5b2ad30717f`  |
| 615    | No file              | `c5b2ad30717f`  |
| 606    | No file              | `c5b2ad30717f`  |
| 599    | No file              | `c5b2ad30717f`  |
| 592    | No file              | `c5b2ad30717f`  |
| 586    | No file              | `c5b2ad30717f`  |
| 577    | No file              | `c5b2ad30717f`  |
| 569    | No file              | `c5b2ad30717f`  |
| 561    | No file              | `c5b2ad30717f`  |
| 554    | No file              | `c5b2ad30717f`  |
| 542    | No file              | `c5b2ad30717f`  |
| 532    | No file              | `c5b2ad30717f`  |
| 531    | No file              | `c5b2ad30717f`  |
| 526    | No file              | `c5b2ad30717f`  |
| 521    | No file              | `c5b2ad30717f`  |
| 517    | No file              | `c5b2ad30717f`  |
| 510    | No file              | `c5b2ad30717f`  |
| 508    | No file              | `c5b2ad30717f`  |
| 504    | No file              | `c5b2ad30717f`  |
| 497    | No file              | `c5b2ad30717f`  |
| 491    | No file              | `c5b2ad30717f`  |
| 485    | No file              | `c5b2ad30717f`  |
| 478    | No file              | `c5b2ad30717f`  |
| 472    | No file              | `c5b2ad30717f`  |
| 466    | No file              | `c5b2ad30717f`  |
| 457    | No file              | `c5b2ad30717f`  |
| 452    | No file              | `c5b2ad30717f`  |
| 449    | No file              | `c5b2ad30717f`  |
| 435    | No file              | `c5b2ad30717f`  |

<!-- versions:end -->

## Companion Files

The handler reads no other file, and no field is a LOC key. The quests that call `checkRandomGroup` are in [`quest.dbss`](quest_dbss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                          |
| ------------------- | ------------ | ------------------ | ---------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                   |
| `+0x04`             | u32          | count              | Number of rows; `1` on client 3474             |
| `+0x08`             | Row[count]   | rows               | See Row                                        |
| `rows+0x00`         | String Table | string_table       | See String Table                               |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end (`8 + 32 * count`) |
| `string_table+0x04` | u32          | zero               | Always `0`                                     |

The string table has the shape [`itemexchangetoclassmapkey.bss`](itemexchangetoclassmapkey_bss.md) and [`questprogressgroup.bss`](questprogressgroup_bss.md) use (`_common/pabr_strings.py`).

### Row (32 bytes)

| Offset  | Type    | Field          | Notes |
| ------- | ------- | -------------- | ----- |
| `+0x00` | u64     | unknown_00     | `0x00007FF79B368530` on client 3474, an address in the range a 64-bit Windows program image loads at; see Notes |
| `+0x08` | u32     | group_key      | The first argument of `checkRandomGroup(group_key, index)` in `quest.dbss`; `1` |
| `+0x0C` | u16     | quest_count    | Number of quest slots, the `index` values `0` to `quest_count - 1`; `37` |
| `+0x0E` | u16     | quest_chain_id | Quest chain of the slots, LOC type 18 `str_id1`; `2322` |
| `+0x10` | u16     | draw_count     | Quests of the group a student is offered per week; `3` |
| `+0x12` | u16     | unknown_12     | `115` |
| `+0x14` | u32     | unknown_14     | `168`; see Open Questions |
| `+0x18` | bytes[8] | unknown_18    | `04 00 50 00 41 00 43 00` |

The split of `+0x10` to `+0x17` into u16, u16 and u32 follows the zero bytes of the one row; nothing else confirms it.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3474          |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Group 1

On client 3474, 37 records of `quest.dbss` call `checkRandomGroup`, all with group `1`: quests 1 to 37 of chain 2322, each with `checkRandomGroup(1, quest_id - 1);checkOlviaAcademyStudent();` as its `condition_script`. No other quest condition or action script calls it.

| Quest IDs (chain 2322) | Title tag                   | Quests |
| ---------------------- | --------------------------- | -----: |
| 1 to 13, 37            | `[Academy] [Weekly Combat]` | 14     |
| 14 to 26               | `[Academy] [Weekly Life]`   | 13     |
| 27 to 36               | `[Academy] [Weekly Visit]`  | 10     |

Every one of the 37 is accepted at `Bulletin Board` (`accept_dialog_key`) and handed in to an NPC (`complete_dialog_key`): Cliff for Combat quests 1 to 13, Justin Bartali for quest 37, and 18 different NPCs for the Life and Visit quests.

Chain 2321 (`[Academy] [Weekly] Bumblin' Buccaneers Brawl`, one quest) has no `checkRandomGroup` call and is not in the group.

## Field Names

The names come from the data. `group_key` is the group argument of `checkRandomGroup` (the only key the scripts use is `1`, the row's key). `quest_count` is `37`, the number of quests that call `checkRandomGroup(1, ...)` and one more than their highest index `36`. `quest_chain_id` is `2322`, the chain all 37 belong to. `draw_count` is `3`, and I checked in game that the Academy bulletin board offers 3 weekly quests per week with mixed tags (not one per Combat, Life and Visit tag). The file is not in the client 1784 archive. A private server's `DataSheets.bexcel` and `binary/` folder on client 1784 have no sheet or file for it, no `.xlsm` file there has `random` and `quest` in its name, and neither the 2016 PDB nor the server dump of client 1784 has a type or text with `RandomGroup` in it outside an instance-field loader message.

calpheonlabs (`questrandomgroup.bss.mdx`) reads the same 32-byte row and keeps it as raw bytes, since it found no count, join or consumer to split it by. The `quest.dbss` conditions above are that join for `+0x08` to `+0x0F`.

## Notes

- Decompressed size on client 3474: `52` bytes, `8 + 1 * 32 + 12`.
- `unknown_00` is not a game value. On client 3474 only two `gamecommondata/binary/` files hold a u64 between `0x00007FF79A000000` and `0x00007FF79BFFFFFF`: this row at `+0x00` (`0x00007FF79B368530`) and `guildhonorsystem.bss` (not documented yet) at file offset `0` (`0x00007FF79B062F88`). Both look like a pointer of the program that wrote the file, stored with the row.
- `unknown_18` (`04 00 50 00 41 00 43 00`) decodes as UTF-16 `4`, `P`, `A`, `C`. With the pointer at `+0x00`, this fits leftover memory written out with the row, so the two fields may hold no data.
- None of the 3,073 client Lua files (`luacscript/x64/`, client 3474) names the file or `checkRandomGroup`. `panel_widget_randomquestinfo_all.luac` is the Agris fever quest tooltip (`getQuestFeverPoint()`) and reads no random group.
- `checkRandom(n, ...)` in the conditions of 240 other quests (client 3474) is a different function with no group key.

## Open Questions

### What `unknown_12`, `unknown_14` and `unknown_18` Hold

`unknown_14` is `168`, the hours of a week (7 x 24), and the group holds the weekly Academy quests, so it may be the draw period in hours. `unknown_12` (`115`) and `unknown_18` match nothing found in `quest.dbss`, LOC or the Lua. calpheonlabs reports that the row bytes at `+12` and `+16` differ between two builds it read. Quest 37 (`[Weekly Combat] Resplendently-lit Gemstone`) comes after the Visit quests, which fits a `quest_count` that grew, but I have only the client 3474 file.
