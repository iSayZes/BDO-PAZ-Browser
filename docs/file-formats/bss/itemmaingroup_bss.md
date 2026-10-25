# `itemmaingroup.bss` Format

## Purpose

Item main groups: each group lists one or more [`itemsubgroup.dbss`](../dbss/itemsubgroup_dbss.md) subgroups, each with an optional condition script. [`characterfunction.dbss`](../dbss/characterfunction_dbss.md) points its shop, sell, guild shop and trade fields here, so a group is the item list an NPC window shows. The plain PABR file holds the groups, then a string table of the condition scripts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes   | Records                    | Row bytes |
| ------ | -------------- | ------------------- | ------- | -------------------------- | --------- |
| 2      | 2726 and later | `itemmaingroup.bss` | 684,909 | 19,069 Entry, 16,664 Group | 10        |
| 1      | 805 to 2717    | `itemmaingroup.bss` | 537,650 | 15,679 Entry, 13,671 Group | 10        |

| Layout | File                | Known             | Unknown           |
| ------ | ------------------- | ----------------- | ----------------- |
| 2      | `itemmaingroup.bss` | 342,009 B (49.9%) | 342,900 B (50.1%) |
| 1      | `itemmaingroup.bss` | 269,869 B (50.2%) | 267,781 B (49.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `563c608b0a75`  |
| 3482   | Layout 2             | `563c608b0a75`  |
| 3474   | Layout 2             | `563c608b0a75`  |
| 3473   | Layout 2             | `563c608b0a75`  |
| 3464   | Layout 2             | `563c608b0a75`  |
| 3458   | Layout 2             | `563c608b0a75`  |
| 3454   | Layout 2             | `563c608b0a75`  |
| 3444   | Layout 2             | `563c608b0a75`  |
| 3435   | Layout 2             | `563c608b0a75`  |
| 3426   | Layout 2             | `563c608b0a75`  |
| 3418   | Layout 2             | `563c608b0a75`  |
| 3412   | Layout 2             | `563c608b0a75`  |
| 3402   | Layout 2             | `563c608b0a75`  |
| 3396   | Layout 2             | `563c608b0a75`  |
| 3387   | Layout 2             | `563c608b0a75`  |
| 3381   | Layout 2             | `563c608b0a75`  |
| 3373   | Layout 2             | `563c608b0a75`  |
| 3364   | Layout 2             | `563c608b0a75`  |
| 3356   | Layout 2             | `563c608b0a75`  |
| 3349   | Layout 2             | `563c608b0a75`  |
| 3342   | Layout 2             | `563c608b0a75`  |
| 3335   | Layout 2             | `563c608b0a75`  |
| 3326   | Layout 2             | `563c608b0a75`  |
| 3321   | Layout 2             | `563c608b0a75`  |
| 3314   | Layout 2             | `563c608b0a75`  |
| 3303   | Layout 2             | `563c608b0a75`  |
| 3302   | Layout 2             | `563c608b0a75`  |
| 3293   | Layout 2             | `563c608b0a75`  |
| 3283   | Layout 2             | `563c608b0a75`  |
| 3275   | Layout 2             | `563c608b0a75`  |
| 3267   | Layout 2             | `563c608b0a75`  |
| 3258   | Layout 2             | `563c608b0a75`  |
| 3251   | Layout 2             | `563c608b0a75`  |
| 3242   | Layout 2             | `563c608b0a75`  |
| 3235   | Layout 2             | `563c608b0a75`  |
| 3229   | Layout 2             | `563c608b0a75`  |
| 3212   | Layout 2             | `563c608b0a75`  |
| 3203   | Layout 2             | `563c608b0a75`  |
| 3193   | Layout 2             | `563c608b0a75`  |
| 3186   | Layout 2             | `563c608b0a75`  |
| 3177   | Layout 2             | `563c608b0a75`  |
| 3169   | Layout 2             | `563c608b0a75`  |
| 3158   | Layout 2             | `563c608b0a75`  |
| 3151   | Layout 2             | `563c608b0a75`  |
| 3144   | Layout 2             | `563c608b0a75`  |
| 3133   | Layout 2             | `563c608b0a75`  |
| 3125   | Layout 2             | `563c608b0a75`  |
| 3118   | Layout 2             | `563c608b0a75`  |
| 3111   | Layout 2             | `563c608b0a75`  |
| 3103   | Layout 2             | `563c608b0a75`  |
| 3095   | Layout 2             | `563c608b0a75`  |
| 3086   | Layout 2             | `563c608b0a75`  |
| 3072   | Layout 2             | `563c608b0a75`  |
| 3062   | Layout 2             | `563c608b0a75`  |
| 3052   | Layout 2             | `563c608b0a75`  |
| 3045   | Layout 2             | `563c608b0a75`  |
| 3037   | Layout 2             | `563c608b0a75`  |
| 3030   | Layout 2             | `563c608b0a75`  |
| 3021   | Layout 2             | `563c608b0a75`  |
| 3012   | Layout 2             | `563c608b0a75`  |
| 3002   | Layout 2             | `563c608b0a75`  |
| 2995   | Layout 2             | `563c608b0a75`  |
| 2987   | Layout 2             | `563c608b0a75`  |
| 2978   | Layout 2             | `563c608b0a75`  |
| 2970   | Layout 2             | `563c608b0a75`  |
| 2959   | Layout 2             | `563c608b0a75`  |
| 2951   | Layout 2             | `563c608b0a75`  |
| 2942   | Layout 2             | `563c608b0a75`  |
| 2935   | Layout 2             | `563c608b0a75`  |
| 2932   | Layout 2             | `563c608b0a75`  |
| 2923   | Layout 2             | `563c608b0a75`  |
| 2919   | Layout 2             | `563c608b0a75`  |
| 2907   | Layout 2             | `563c608b0a75`  |
| 2900   | Layout 2             | `563c608b0a75`  |
| 2891   | Layout 2             | `563c608b0a75`  |
| 2882   | Layout 2             | `563c608b0a75`  |
| 2872   | Layout 2             | `563c608b0a75`  |
| 2863   | Layout 2             | `563c608b0a75`  |
| 2855   | Layout 2             | `563c608b0a75`  |
| 2849   | Layout 2             | `563c608b0a75`  |
| 2844   | Layout 2             | `563c608b0a75`  |
| 2834   | Layout 2             | `563c608b0a75`  |
| 2825   | Layout 2             | `563c608b0a75`  |
| 2819   | Layout 2             | `563c608b0a75`  |
| 2811   | Layout 2             | `563c608b0a75`  |
| 2803   | Layout 2             | `563c608b0a75`  |
| 2794   | Layout 2             | `563c608b0a75`  |
| 2783   | Layout 2             | `563c608b0a75`  |
| 2774   | Layout 2             | `563c608b0a75`  |
| 2765   | Layout 2             | `563c608b0a75`  |
| 2756   | Layout 2             | `563c608b0a75`  |
| 2750   | Layout 2             | `563c608b0a75`  |
| 2743   | Layout 2             | `563c608b0a75`  |
| 2736   | Layout 2             | `563c608b0a75`  |
| 2726   | Layout 2             | `563c608b0a75`  |
| 2717   | Layout 1             | `563c608b0a75`  |
| 2709   | Layout 1             | `563c608b0a75`  |
| 2703   | Layout 1             | `563c608b0a75`  |
| 2695   | Layout 1             | `563c608b0a75`  |
| 2684   | Layout 1             | `563c608b0a75`  |
| 2672   | Layout 1             | `563c608b0a75`  |
| 2665   | Layout 1             | `563c608b0a75`  |
| 2657   | Layout 1             | `563c608b0a75`  |
| 2649   | Layout 1             | `563c608b0a75`  |
| 2644   | Layout 1             | `563c608b0a75`  |
| 2637   | Layout 1             | `563c608b0a75`  |
| 2629   | Layout 1             | `563c608b0a75`  |
| 2619   | Layout 1             | `563c608b0a75`  |
| 2612   | Layout 1             | `563c608b0a75`  |
| 2606   | Layout 1             | `563c608b0a75`  |
| 2602   | Layout 1             | `563c608b0a75`  |
| 2601   | Layout 1             | `563c608b0a75`  |
| 2592   | Layout 1             | `563c608b0a75`  |
| 2583   | Layout 1             | `563c608b0a75`  |
| 2575   | Layout 1             | `563c608b0a75`  |
| 2567   | Layout 1             | `563c608b0a75`  |
| 2560   | Layout 1             | `563c608b0a75`  |
| 2553   | Layout 1             | `563c608b0a75`  |
| 2545   | Layout 1             | `563c608b0a75`  |
| 2538   | Layout 1             | `563c608b0a75`  |
| 2529   | Layout 1             | `563c608b0a75`  |
| 2519   | Layout 1             | `563c608b0a75`  |
| 2513   | Layout 1             | `563c608b0a75`  |
| 2510   | Layout 1             | `563c608b0a75`  |
| 2507   | Layout 1             | `563c608b0a75`  |
| 2503   | Layout 1             | `563c608b0a75`  |
| 2498   | Layout 1             | `563c608b0a75`  |
| 2492   | Layout 1             | `563c608b0a75`  |
| 2487   | Layout 1             | `563c608b0a75`  |
| 2480   | Layout 1             | `563c608b0a75`  |
| 2474   | Layout 1             | `563c608b0a75`  |
| 2468   | Layout 1             | `563c608b0a75`  |
| 2460   | Layout 1             | `563c608b0a75`  |
| 2453   | Layout 1             | `563c608b0a75`  |
| 2444   | Layout 1             | `563c608b0a75`  |
| 2438   | Layout 1             | `563c608b0a75`  |
| 2434   | Layout 1             | `563c608b0a75`  |
| 2429   | Layout 1             | `563c608b0a75`  |
| 2421   | Layout 1             | `563c608b0a75`  |
| 2414   | Layout 1             | `563c608b0a75`  |
| 2407   | Layout 1             | `563c608b0a75`  |
| 2401   | Layout 1             | `563c608b0a75`  |
| 2397   | Layout 1             | `563c608b0a75`  |
| 2393   | Layout 1             | `563c608b0a75`  |
| 2384   | Layout 1             | `563c608b0a75`  |
| 2378   | Layout 1             | `563c608b0a75`  |
| 2372   | Layout 1             | `563c608b0a75`  |
| 2358   | Layout 1             | `563c608b0a75`  |
| 2352   | Layout 1             | `563c608b0a75`  |
| 2347   | Layout 1             | `563c608b0a75`  |
| 2343   | Layout 1             | `563c608b0a75`  |
| 2335   | Layout 1             | `563c608b0a75`  |
| 2327   | Layout 1             | `563c608b0a75`  |
| 2324   | Layout 1             | `563c608b0a75`  |
| 2319   | Layout 1             | `563c608b0a75`  |
| 2313   | Layout 1             | `563c608b0a75`  |
| 2308   | Layout 1             | `563c608b0a75`  |
| 2302   | Layout 1             | `563c608b0a75`  |
| 2295   | Layout 1             | `563c608b0a75`  |
| 2290   | Layout 1             | `563c608b0a75`  |
| 2284   | Layout 1             | `563c608b0a75`  |
| 2276   | Layout 1             | `563c608b0a75`  |
| 2269   | Layout 1             | `563c608b0a75`  |
| 2259   | Layout 1             | `563c608b0a75`  |
| 2250   | Layout 1             | `563c608b0a75`  |
| 2243   | Layout 1             | `563c608b0a75`  |
| 2235   | Layout 1             | `563c608b0a75`  |
| 2229   | Layout 1             | `563c608b0a75`  |
| 2224   | Layout 1             | `563c608b0a75`  |
| 2218   | Layout 1             | `563c608b0a75`  |
| 2215   | Layout 1             | `563c608b0a75`  |
| 2207   | Layout 1             | `563c608b0a75`  |
| 2203   | Layout 1             | `563c608b0a75`  |
| 2196   | Layout 1             | `563c608b0a75`  |
| 2192   | Layout 1             | `563c608b0a75`  |
| 2189   | Layout 1             | `563c608b0a75`  |
| 2183   | Layout 1             | `563c608b0a75`  |
| 2179   | Layout 1             | `563c608b0a75`  |
| 2171   | Layout 1             | `563c608b0a75`  |
| 2163   | Layout 1             | `563c608b0a75`  |
| 2156   | Layout 1             | `563c608b0a75`  |
| 2151   | Layout 1             | `563c608b0a75`  |
| 2147   | Layout 1             | `563c608b0a75`  |
| 2142   | Layout 1             | `563c608b0a75`  |
| 2138   | Layout 1             | `563c608b0a75`  |
| 2134   | Layout 1             | `563c608b0a75`  |
| 2130   | Layout 1             | `563c608b0a75`  |
| 2122   | Layout 1             | `563c608b0a75`  |
| 2107   | Layout 1             | `563c608b0a75`  |
| 2098   | Layout 1             | `563c608b0a75`  |
| 2089   | Layout 1             | `563c608b0a75`  |
| 2081   | Layout 1             | `563c608b0a75`  |
| 2073   | Layout 1             | `563c608b0a75`  |
| 2067   | Layout 1             | `563c608b0a75`  |
| 2063   | Layout 1             | `563c608b0a75`  |
| 2059   | Layout 1             | `563c608b0a75`  |
| 2052   | Layout 1             | `563c608b0a75`  |
| 2044   | Layout 1             | `563c608b0a75`  |
| 2039   | Layout 1             | `563c608b0a75`  |
| 2032   | Layout 1             | `563c608b0a75`  |
| 2025   | Layout 1             | `563c608b0a75`  |
| 2011   | Layout 1             | `563c608b0a75`  |
| 2005   | Layout 1             | `563c608b0a75`  |
| 2000   | Layout 1             | `563c608b0a75`  |
| 1996   | Layout 1             | `563c608b0a75`  |
| 1991   | Layout 1             | `563c608b0a75`  |
| 1985   | Layout 1             | `563c608b0a75`  |
| 1980   | Layout 1             | `563c608b0a75`  |
| 1969   | Layout 1             | `563c608b0a75`  |
| 1964   | Layout 1             | `563c608b0a75`  |
| 1958   | Layout 1             | `563c608b0a75`  |
| 1950   | Layout 1             | `563c608b0a75`  |
| 1945   | Layout 1             | `563c608b0a75`  |
| 1937   | Layout 1             | `563c608b0a75`  |
| 1933   | Layout 1             | `563c608b0a75`  |
| 1927   | Layout 1             | `563c608b0a75`  |
| 1921   | Layout 1             | `563c608b0a75`  |
| 1914   | Layout 1             | `563c608b0a75`  |
| 1908   | Layout 1             | `563c608b0a75`  |
| 1897   | Layout 1             | `563c608b0a75`  |
| 1892   | Layout 1             | `563c608b0a75`  |
| 1886   | Layout 1             | `563c608b0a75`  |
| 1881   | Layout 1             | `563c608b0a75`  |
| 1871   | Layout 1             | `563c608b0a75`  |
| 1866   | Layout 1             | `563c608b0a75`  |
| 1862   | Layout 1             | `563c608b0a75`  |
| 1854   | Layout 1             | `563c608b0a75`  |
| 1846   | Layout 1             | `563c608b0a75`  |
| 1838   | Layout 1             | `563c608b0a75`  |
| 1832   | Layout 1             | `563c608b0a75`  |
| 1826   | Layout 1             | `563c608b0a75`  |
| 1822   | Layout 1             | `563c608b0a75`  |
| 1818   | Layout 1             | `563c608b0a75`  |
| 1804   | Layout 1             | `563c608b0a75`  |
| 1794   | Layout 1             | `563c608b0a75`  |
| 1790   | Layout 1             | `563c608b0a75`  |
| 1784   | Layout 1             | `563c608b0a75`  |
| 1774   | Layout 1             | `563c608b0a75`  |
| 1771   | Layout 1             | `563c608b0a75`  |
| 1762   | Layout 1             | `563c608b0a75`  |
| 1759   | Layout 1             | `563c608b0a75`  |
| 1754   | Layout 1             | `563c608b0a75`  |
| 1749   | Layout 1             | `563c608b0a75`  |
| 1743   | Layout 1             | `563c608b0a75`  |
| 1737   | Layout 1             | `563c608b0a75`  |
| 1731   | Layout 1             | `563c608b0a75`  |
| 1725   | Layout 1             | `563c608b0a75`  |
| 1717   | Layout 1             | `563c608b0a75`  |
| 1710   | Layout 1             | `563c608b0a75`  |
| 1704   | Layout 1             | `563c608b0a75`  |
| 1698   | Layout 1             | `563c608b0a75`  |
| 1690   | Layout 1             | `563c608b0a75`  |
| 1685   | Layout 1             | `563c608b0a75`  |
| 1680   | Layout 1             | `563c608b0a75`  |
| 1674   | Layout 1             | `563c608b0a75`  |
| 1668   | Layout 1             | `563c608b0a75`  |
| 1659   | Layout 1             | `563c608b0a75`  |
| 1649   | Layout 1             | `563c608b0a75`  |
| 1642   | Layout 1             | `563c608b0a75`  |
| 1636   | Layout 1             | `563c608b0a75`  |
| 1628   | Layout 1             | `563c608b0a75`  |
| 1622   | Layout 1             | `563c608b0a75`  |
| 1614   | Layout 1             | `563c608b0a75`  |
| 1608   | Layout 1             | `563c608b0a75`  |
| 1602   | Layout 1             | `563c608b0a75`  |
| 1598   | Layout 1             | `563c608b0a75`  |
| 1594   | Layout 1             | `563c608b0a75`  |
| 1590   | Layout 1             | `563c608b0a75`  |
| 1587   | Layout 1             | `563c608b0a75`  |
| 1584   | Layout 1             | `563c608b0a75`  |
| 1579   | Layout 1             | `563c608b0a75`  |
| 1572   | Layout 1             | `563c608b0a75`  |
| 1565   | Layout 1             | `563c608b0a75`  |
| 1559   | Layout 1             | `563c608b0a75`  |
| 1554   | Layout 1             | `563c608b0a75`  |
| 1547   | Layout 1             | `563c608b0a75`  |
| 1537   | Layout 1             | `563c608b0a75`  |
| 1529   | Layout 1             | `563c608b0a75`  |
| 1524   | Layout 1             | `563c608b0a75`  |
| 1519   | Layout 1             | `563c608b0a75`  |
| 1509   | Layout 1             | `563c608b0a75`  |
| 1506   | Layout 1             | `563c608b0a75`  |
| 1504   | Layout 1             | `563c608b0a75`  |
| 1500   | Layout 1             | `563c608b0a75`  |
| 1493   | Layout 1             | `563c608b0a75`  |
| 1489   | Layout 1             | `563c608b0a75`  |
| 1485   | Layout 1             | `563c608b0a75`  |
| 1481   | Layout 1             | `563c608b0a75`  |
| 1474   | Layout 1             | `563c608b0a75`  |
| 1466   | Layout 1             | `563c608b0a75`  |
| 1462   | Layout 1             | `563c608b0a75`  |
| 1459   | Layout 1             | `563c608b0a75`  |
| 1453   | Layout 1             | `563c608b0a75`  |
| 1450   | Layout 1             | `563c608b0a75`  |
| 1445   | Layout 1             | `563c608b0a75`  |
| 1439   | Layout 1             | `563c608b0a75`  |
| 1433   | Layout 1             | `563c608b0a75`  |
| 1430   | Layout 1             | `563c608b0a75`  |
| 1426   | Layout 1             | `563c608b0a75`  |
| 1421   | Layout 1             | `563c608b0a75`  |
| 1417   | Layout 1             | `563c608b0a75`  |
| 1416   | Layout 1             | `563c608b0a75`  |
| 1409   | Layout 1             | `563c608b0a75`  |
| 1405   | Layout 1             | `563c608b0a75`  |
| 1401   | Layout 1             | `563c608b0a75`  |
| 1396   | Layout 1             | `563c608b0a75`  |
| 1391   | Layout 1             | `563c608b0a75`  |
| 1390   | Layout 1             | `563c608b0a75`  |
| 1386   | Layout 1             | `563c608b0a75`  |
| 1381   | Layout 1             | `563c608b0a75`  |
| 1379   | Layout 1             | `563c608b0a75`  |
| 1372   | Layout 1             | `563c608b0a75`  |
| 1366   | Layout 1             | `563c608b0a75`  |
| 1364   | Layout 1             | `563c608b0a75`  |
| 1363   | Layout 1             | `563c608b0a75`  |
| 1360   | Layout 1             | `563c608b0a75`  |
| 1358   | Layout 1             | `563c608b0a75`  |
| 1355   | Layout 1             | `563c608b0a75`  |
| 1351   | Layout 1             | `563c608b0a75`  |
| 1348   | Layout 1             | `563c608b0a75`  |
| 1346   | Layout 1             | `563c608b0a75`  |
| 1341   | Layout 1             | `563c608b0a75`  |
| 1340   | Layout 1             | `563c608b0a75`  |
| 1338   | Layout 1             | `563c608b0a75`  |
| 1335   | Layout 1             | `563c608b0a75`  |
| 1333   | Layout 1             | `563c608b0a75`  |
| 1329   | Layout 1             | `563c608b0a75`  |
| 1327   | Layout 1             | `563c608b0a75`  |
| 1324   | Layout 1             | `563c608b0a75`  |
| 1321   | Layout 1             | `563c608b0a75`  |
| 1319   | Layout 1             | `563c608b0a75`  |
| 1318   | Layout 1             | `563c608b0a75`  |
| 1316   | Layout 1             | `563c608b0a75`  |
| 1313   | Layout 1             | `563c608b0a75`  |
| 1311   | Layout 1             | `563c608b0a75`  |
| 1309   | Layout 1             | `563c608b0a75`  |
| 1304   | Layout 1             | `563c608b0a75`  |
| 1292   | Layout 1             | `563c608b0a75`  |
| 1286   | Layout 1             | `563c608b0a75`  |
| 1280   | Layout 1             | `563c608b0a75`  |
| 1276   | Layout 1             | `563c608b0a75`  |
| 1267   | Layout 1             | `563c608b0a75`  |
| 1261   | Layout 1             | `563c608b0a75`  |
| 1256   | Layout 1             | `563c608b0a75`  |
| 1250   | Layout 1             | `563c608b0a75`  |
| 1246   | Layout 1             | `563c608b0a75`  |
| 1239   | Layout 1             | `563c608b0a75`  |
| 1230   | Layout 1             | `563c608b0a75`  |
| 1226   | Layout 1             | `563c608b0a75`  |
| 1220   | Layout 1             | `563c608b0a75`  |
| 1217   | Layout 1             | `563c608b0a75`  |
| 1211   | Layout 1             | `563c608b0a75`  |
| 1210   | Layout 1             | `563c608b0a75`  |
| 1208   | Layout 1             | `563c608b0a75`  |
| 1203   | Layout 1             | `563c608b0a75`  |
| 1197   | Layout 1             | `563c608b0a75`  |
| 1194   | Layout 1             | `563c608b0a75`  |
| 1192   | Layout 1             | `563c608b0a75`  |
| 1187   | Layout 1             | `563c608b0a75`  |
| 1183   | Layout 1             | `563c608b0a75`  |
| 1177   | Layout 1             | `563c608b0a75`  |
| 1173   | Layout 1             | `563c608b0a75`  |
| 1167   | Layout 1             | `563c608b0a75`  |
| 1164   | Layout 1             | `563c608b0a75`  |
| 1156   | Layout 1             | `563c608b0a75`  |
| 1149   | Layout 1             | `563c608b0a75`  |
| 1144   | Layout 1             | `563c608b0a75`  |
| 1137   | Layout 1             | `563c608b0a75`  |
| 1132   | Layout 1             | `563c608b0a75`  |
| 1127   | Layout 1             | `563c608b0a75`  |
| 1122   | Layout 1             | `563c608b0a75`  |
| 1118   | Layout 1             | `563c608b0a75`  |
| 1114   | Layout 1             | `563c608b0a75`  |
| 1109   | Layout 1             | `563c608b0a75`  |
| 1102   | No file              | `563c608b0a75`  |
| 1096   | No file              | `563c608b0a75`  |
| 1088   | No file              | `563c608b0a75`  |
| 1081   | No file              | `563c608b0a75`  |
| 1076   | No file              | `563c608b0a75`  |
| 1069   | No file              | `563c608b0a75`  |
| 1064   | No file              | `563c608b0a75`  |
| 1058   | No file              | `563c608b0a75`  |
| 1051   | No file              | `563c608b0a75`  |
| 1044   | No file              | `563c608b0a75`  |
| 1036   | No file              | `563c608b0a75`  |
| 1026   | No file              | `563c608b0a75`  |
| 1016   | No file              | `563c608b0a75`  |
| 1009   | No file              | `563c608b0a75`  |
| 1005   | No file              | `563c608b0a75`  |
| 1000   | No file              | `563c608b0a75`  |
| 998    | No file              | `563c608b0a75`  |
| 990    | No file              | `563c608b0a75`  |
| 979    | No file              | `563c608b0a75`  |
| 972    | No file              | `563c608b0a75`  |
| 963    | No file              | `563c608b0a75`  |
| 955    | No file              | `563c608b0a75`  |
| 946    | No file              | `563c608b0a75`  |
| 938    | No file              | `563c608b0a75`  |
| 927    | No file              | `563c608b0a75`  |
| 911    | No file              | `563c608b0a75`  |
| 904    | No file              | `563c608b0a75`  |
| 899    | No file              | `563c608b0a75`  |
| 894    | No file              | `563c608b0a75`  |
| 885    | No file              | `563c608b0a75`  |
| 879    | No file              | `563c608b0a75`  |
| 872    | No file              | `563c608b0a75`  |
| 864    | No file              | `563c608b0a75`  |
| 855    | No file              | `563c608b0a75`  |
| 853    | No file              | `563c608b0a75`  |
| 845    | No file              | `563c608b0a75`  |
| 837    | No file              | `563c608b0a75`  |
| 829    | Layout 1             | `563c608b0a75`  |
| 822    | Layout 1             | `563c608b0a75`  |
| 814    | Layout 1             | `563c608b0a75`  |
| 805    | Layout 1             | `563c608b0a75`  |
| 794    | No documented layout | `563c608b0a75`  |
| 787    | No documented layout | `563c608b0a75`  |
| 780    | No documented layout | `563c608b0a75`  |
| 771    | No documented layout | `563c608b0a75`  |
| 760    | No documented layout | `563c608b0a75`  |
| 748    | No documented layout | `563c608b0a75`  |
| 741    | No documented layout | `563c608b0a75`  |
| 736    | No documented layout | `563c608b0a75`  |
| 731    | No documented layout | `563c608b0a75`  |
| 723    | No documented layout | `563c608b0a75`  |
| 711    | No documented layout | `563c608b0a75`  |
| 707    | No documented layout | `563c608b0a75`  |
| 697    | No documented layout | `563c608b0a75`  |
| 689    | No documented layout | `563c608b0a75`  |
| 683    | No documented layout | `563c608b0a75`  |
| 678    | No documented layout | `563c608b0a75`  |
| 670    | No documented layout | `563c608b0a75`  |
| 661    | No documented layout | `563c608b0a75`  |
| 656    | No documented layout | `563c608b0a75`  |
| 652    | No documented layout | `563c608b0a75`  |
| 643    | No documented layout | `563c608b0a75`  |
| 637    | No documented layout | `563c608b0a75`  |
| 630    | No documented layout | `563c608b0a75`  |
| 627    | No documented layout | `563c608b0a75`  |
| 621    | No documented layout | `563c608b0a75`  |
| 617    | No documented layout | `563c608b0a75`  |
| 615    | No documented layout | `563c608b0a75`  |
| 606    | No documented layout | `563c608b0a75`  |
| 599    | No documented layout | `563c608b0a75`  |
| 592    | No documented layout | `563c608b0a75`  |
| 586    | No documented layout | `563c608b0a75`  |
| 577    | No documented layout | `563c608b0a75`  |
| 569    | No documented layout | `563c608b0a75`  |
| 561    | No documented layout | `563c608b0a75`  |
| 554    | No documented layout | `563c608b0a75`  |
| 542    | No documented layout | `563c608b0a75`  |
| 532    | No documented layout | `563c608b0a75`  |
| 531    | No documented layout | `563c608b0a75`  |
| 526    | No documented layout | `563c608b0a75`  |
| 521    | No documented layout | `563c608b0a75`  |
| 517    | No documented layout | `563c608b0a75`  |
| 510    | No documented layout | `563c608b0a75`  |
| 508    | No documented layout | `563c608b0a75`  |
| 504    | No documented layout | `563c608b0a75`  |
| 497    | No documented layout | `563c608b0a75`  |
| 491    | No documented layout | `563c608b0a75`  |
| 485    | No documented layout | `563c608b0a75`  |
| 478    | No documented layout | `563c608b0a75`  |
| 472    | No documented layout | `563c608b0a75`  |
| 466    | No documented layout | `563c608b0a75`  |
| 457    | No documented layout | `563c608b0a75`  |
| 452    | No documented layout | `563c608b0a75`  |
| 449    | No documented layout | `563c608b0a75`  |
| 435    | No documented layout | `563c608b0a75`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                      |
| ------------------------- | -------- | --------------------------------------------------------- |
| `itemsubgroup.dbss`       | Required | The items of each subgroup                                |
| `itemsubgroupoffset.dbss` | Required | Index into `itemsubgroup.dbss`                            |
| `languagedata_en.loc`     | Optional | Item names, LOC type 0 at `str_id1=item_id`               |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type          | Field              | Notes                                                        |
| ------------------- | ------------- | ------------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]       | magic              | ASCII `PABR`                                                 |
| `+0x04`             | u32           | count              | Number of groups; `16,501` on client 3464                    |
| `+0x08`             | Group[count]  | groups             | Variable-size groups, back to back; see Group                |
| `groups+0x00`       | String Table  | string_table       | See String Table                                             |
| `string_table+0x00` | u32           | string_table_start | Offset of `string_count`, where the groups end               |
| `string_table+0x04` | u32           | zero               | Always `0`                                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Every string here is wide (UTF-16LE). Walking `count` groups ends exactly at `string_table_start`, and the string table ends exactly at the trailer.

### Group (variable: 29 bytes + entries)

| Offset  | Type               | Field              | Notes                                                                      |
| ------- | ------------------ | ------------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32                | group_id           | Unique; `1,309` to `65,535`, not in key order                              |
| `+0x04` | u8                 | do_select_only_one | `1` when the group hands out one of its subgroups; `0` on 11,926 groups, `1` on 4,575 (client 3464) |
| `+0x05` | bytes[8]           | unknown_05         | Always zero; the 2016 `_pickCount` (i64) slot, see Field Names             |
| `+0x0D` | i32                | refresh_start_hour | `-1`, or `0` on group 50452 only (client 3464)                             |
| `+0x11` | bytes[8]           | unknown_11         | Always zero; the 2016 `_refreshInterval` (u64) slot, see Field Names       |
| `+0x19` | u32                | entry_count        | `1` to `4`; never `0` on client 3464                                       |
| `+0x1D` | Entry[entry_count] | entries            | See Entry                                                                  |

### Entry (10 bytes)

| Offset  | Type | Field         | Notes                                                               |
| ------- | ---- | ------------- | ------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00    | Always `0`; the 2016 `_selectRate` slot, see Field Names            |
| `+0x04` | u32  | condition_ref | Index into the string table; string `0` is empty (no condition)     |
| `+0x08` | u16  | subgroup_key  | `itemsubgroup.dbss` subgroup key; every key is in its offset index  |

On client 3464 the 16,501 groups hold 18,906 entries: 15,608 groups have one entry, 121 two, 32 three and 740 four. 15,072 of the one-entry groups list the subgroup with their own key (group 50503 lists subgroup 50503).

The conditions use the script calls of `characterfunction.dbss` conditions (`getIntimacy`, `getLevel`, `clearQuest`, `checkexplore`, `isContentsGroupOpen`), joined with `;` and alternatives split by `<or>`. On client 3464, 16,422 entries have no condition, 2,140 have the text `0`, and 118 have `checkexplore(103, 1)`, node 103 being Bahar Investment Bank.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                   |
| ------- | ------------------ | ------------ | --------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `197` on client 3464 |
| `+0x04` | pstr[string_count] | strings      | Every string here is wide (UTF-16LE)    |

## Layout 1

Client 1784 groups have 7 bytes between `group_id` and `refresh_start_hour`,
where client 3473 has `do_select_only_one` and the 8-byte `unknown_05`. All 7
are zero in every group of client 1784, so which two bytes the newer layout
added is open. Only the Group differs from Layout 2.

### Group (variable: 27 bytes + entries)

| Offset  | Type               | Field              | Notes                                                     |
| ------- | ------------------ | ------------------ | --------------------------------------------------------- |
| `+0x00` | u32                | group_id           |                                                           |
| `+0x04` | bytes[7]           | unknown_04         | Zero in all 14,305 groups (client 1784)                   |
| `+0x0B` | i32                | refresh_start_hour |                                                           |
| `+0x0F` | bytes[8]           | unknown_11         | Always zero                                               |
| `+0x17` | u32                | entry_count        |                                                           |
| `+0x1B` | Entry[entry_count] | entries            |                                                           |

## Notes

- `characterfunction.dbss` stores five group IDs per NPC: `shop_buy_group`, `shop_sell_group`, `guild_shop_buy_group`, `guild_shop_sell_group` and `trade_group`. All 884, 743, 63, 61 and 125 non-zero values on client 3464 are group IDs here; that doc names the fields.
- The trade groups are the 62 IDs from 54002 to 54146 (client 3464). Each has one entry: subgroup 54001 (item 55151, the only subgroup besides 55000 that sets the trade price fields in `itemsubgroup.dbss`) under `checkexplore(103, 1)`. Subgroup 55000 (the trade crates) is in no group.
- A group can list one subgroup more than once: group 57996 lists 57771, then 57357 three times with the condition `0`.
- Worker production reaches groups through item exchanges: in the 2016 client a `plantexchangegroup.bss` row lists item exchange keys, and each `gc::ItemExchangeSourceStaticStatus` points at two groups here, `_productItemDropKey` (the product) and `_npcWorkerDropKeyForLuck` (the luck drop). `plantexchangegroup.bss` keeps the exchange key where earlier docs read a subgroup key; see [its Field Names](plantexchangegroup_bss.md#field-names). Group IDs 44059 and 44060 (Tungrad Ruins excavation) point at subgroups 42339 and 42340 (Trace of Nature with a Rough Translucent or Rough Blue Crystal), which is why those two zones resolve here and not in `itemsubgroup.dbss`.
- On client 3464, 4 of the 893 groups with more than one entry set `do_select_only_one`; the other 4,571 are one-entry groups.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::ItemMainGroupStaticStatus` holds `_key`, the entry list, `_doSelectOnlyOne` (bool), `_pickCount` (i64), `_refreshStartHour` (i32) and `_refreshInterval` (u64); each entry (`value_type`) holds `_selectRate` (i32), `_conditionString`, a parsed condition list and `_itemSubGroupKey` (u16). The file stores the scalars in that order between `group_id` and `entry_count`, with the list moved to the end, and the entry stores `_selectRate`, the condition string index and `_itemSubGroupKey` in that order. The server-side `ItemMainGroup_Table` of a private server on client 519 shares 6,168 group IDs with client 3464:

| Field              | `ItemMainGroup_Table` column | Matching groups                                    |
| ------------------ | ---------------------------- | -------------------------------------------------- |
| do_select_only_one | `DoSelectOnlyOne`            | 5,703 of 6,168; see below                          |
| refresh_start_hour | `RefreshStartHour`           | `-1` on both sides for every shared group but 50452, the one group set on both (server `12`, client `0`) |
| subgroup_key       | `ItemSubGroupKey0` to `3`    | 6,296 of 7,802 entries                             |

The 465 `do_select_only_one` mismatches sit in key bands: 357 groups the server has at `0` and the client at `1` (1347 to 64037), and 108 the other way, all from 46001 up (46001 to 46015 and on, 65021, 65213 to 65219). 455 of them list the same subgroups on both sides; I read them as flags changed by patches since the server data.

`unknown_05`, `unknown_11` and the entry `unknown_00` sit where the 2016 struct has `_pickCount`, `_refreshInterval` and `_selectRate`, but they keep their offsets: the client stores `0` on every group and entry, while the server sets `SelectRate0` to `1,000,000` on 10,745 of its 11,098 groups and `RefreshInterval` to `-1` on 9,274. The selection weights of a `do_select_only_one` group are not in the client file.

## Open Questions

### Condition `0`

2,140 entries carry the condition text `0` (client 3464), often on the second to fourth entry of a group that repeats one subgroup. It may be a script that never passes, which would turn the entry off, but no client code that evaluates these conditions has been found.

### `refresh_start_hour` on Group 50452

`refresh_start_hour` is `-1` on every group but 50452, a furniture list (Four-legged Dining Table and five more) where it is `0`. The server sets `RefreshStartHour` and `RefreshInterval` to `12` on the same group, so it is a list that refreshes on a timer, but the client keeps no interval (`unknown_11` is zero). What the client does with the start hour alone is open.
