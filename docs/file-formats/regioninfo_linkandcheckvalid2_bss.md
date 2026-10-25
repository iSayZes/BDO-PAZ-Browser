# `regioninfo_linkandcheckvalid2.bss` Format

## Purpose

Lists, per world region, the town regions a character can be sent to from it by PC delivery (Field Names). It has one record for every [`regioninfo.bss`](regioninfo_bss.md) region, and each list is the same list that `regioninfo.bss` stores as `pc_delivery_region_keys`, so this file is a stand-alone copy of those link lists. 58 regions (all of them `MainTown` or `MinorTown`) have a list; the other 1536 have none.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                                | Bytes  | Records                  | Row bytes               |
| ------ | ------------- | ----------------------------------- | ------ | ------------------------ | ----------------------- |
| 1      | 805 and later | `regioninfo_linkandcheckvalid2.bss` | 19,574 | 1,595 Region Link Record | 10 to 98, 12 on average |

| Layout | File                                | Known            | Unknown         |
| ------ | ----------------------------------- | ---------------- | --------------- |
| 1      | `regioninfo_linkandcheckvalid2.bss` | 13,194 B (67.4%) | 6,380 B (32.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `d1856b6d346d`  |
| 3482   | Layout 1             | `d1856b6d346d`  |
| 3474   | Layout 1             | `d1856b6d346d`  |
| 3473   | Layout 1             | `d1856b6d346d`  |
| 3464   | Layout 1             | `d1856b6d346d`  |
| 3458   | Layout 1             | `d1856b6d346d`  |
| 3454   | Layout 1             | `d1856b6d346d`  |
| 3444   | Layout 1             | `d1856b6d346d`  |
| 3435   | Layout 1             | `d1856b6d346d`  |
| 3426   | Layout 1             | `d1856b6d346d`  |
| 3418   | Layout 1             | `d1856b6d346d`  |
| 3412   | Layout 1             | `d1856b6d346d`  |
| 3402   | Layout 1             | `d1856b6d346d`  |
| 3396   | Layout 1             | `d1856b6d346d`  |
| 3387   | Layout 1             | `d1856b6d346d`  |
| 3381   | Layout 1             | `d1856b6d346d`  |
| 3373   | Layout 1             | `d1856b6d346d`  |
| 3364   | No file              | `d1856b6d346d`  |
| 3356   | Layout 1             | `d1856b6d346d`  |
| 3349   | Layout 1             | `d1856b6d346d`  |
| 3342   | Layout 1             | `d1856b6d346d`  |
| 3335   | Layout 1             | `d1856b6d346d`  |
| 3326   | Layout 1             | `d1856b6d346d`  |
| 3321   | Layout 1             | `d1856b6d346d`  |
| 3314   | Layout 1             | `d1856b6d346d`  |
| 3303   | Layout 1             | `d1856b6d346d`  |
| 3302   | Layout 1             | `d1856b6d346d`  |
| 3293   | Layout 1             | `d1856b6d346d`  |
| 3283   | Layout 1             | `d1856b6d346d`  |
| 3275   | Layout 1             | `d1856b6d346d`  |
| 3267   | Layout 1             | `d1856b6d346d`  |
| 3258   | Layout 1             | `d1856b6d346d`  |
| 3251   | Layout 1             | `d1856b6d346d`  |
| 3242   | Layout 1             | `d1856b6d346d`  |
| 3235   | Layout 1             | `d1856b6d346d`  |
| 3229   | Layout 1             | `d1856b6d346d`  |
| 3212   | Layout 1             | `d1856b6d346d`  |
| 3203   | Layout 1             | `d1856b6d346d`  |
| 3193   | Layout 1             | `d1856b6d346d`  |
| 3186   | Layout 1             | `d1856b6d346d`  |
| 3177   | Layout 1             | `d1856b6d346d`  |
| 3169   | Layout 1             | `d1856b6d346d`  |
| 3158   | Layout 1             | `d1856b6d346d`  |
| 3151   | Layout 1             | `d1856b6d346d`  |
| 3144   | Layout 1             | `d1856b6d346d`  |
| 3133   | Layout 1             | `d1856b6d346d`  |
| 3125   | Layout 1             | `d1856b6d346d`  |
| 3118   | Layout 1             | `d1856b6d346d`  |
| 3111   | Layout 1             | `d1856b6d346d`  |
| 3103   | Layout 1             | `d1856b6d346d`  |
| 3095   | Layout 1             | `d1856b6d346d`  |
| 3086   | Layout 1             | `d1856b6d346d`  |
| 3072   | Layout 1             | `d1856b6d346d`  |
| 3062   | Layout 1             | `d1856b6d346d`  |
| 3052   | Layout 1             | `d1856b6d346d`  |
| 3045   | Layout 1             | `d1856b6d346d`  |
| 3037   | Layout 1             | `d1856b6d346d`  |
| 3030   | Layout 1             | `d1856b6d346d`  |
| 3021   | Layout 1             | `d1856b6d346d`  |
| 3012   | Layout 1             | `d1856b6d346d`  |
| 3002   | Layout 1             | `d1856b6d346d`  |
| 2995   | Layout 1             | `d1856b6d346d`  |
| 2987   | Layout 1             | `d1856b6d346d`  |
| 2978   | Layout 1             | `d1856b6d346d`  |
| 2970   | Layout 1             | `d1856b6d346d`  |
| 2959   | Layout 1             | `d1856b6d346d`  |
| 2951   | Layout 1             | `d1856b6d346d`  |
| 2942   | Layout 1             | `d1856b6d346d`  |
| 2935   | Layout 1             | `d1856b6d346d`  |
| 2932   | Layout 1             | `d1856b6d346d`  |
| 2923   | Layout 1             | `d1856b6d346d`  |
| 2919   | Layout 1             | `d1856b6d346d`  |
| 2907   | Layout 1             | `d1856b6d346d`  |
| 2900   | Layout 1             | `d1856b6d346d`  |
| 2891   | Layout 1             | `d1856b6d346d`  |
| 2882   | Layout 1             | `d1856b6d346d`  |
| 2872   | Layout 1             | `d1856b6d346d`  |
| 2863   | Layout 1             | `d1856b6d346d`  |
| 2855   | Layout 1             | `d1856b6d346d`  |
| 2849   | Layout 1             | `d1856b6d346d`  |
| 2844   | Layout 1             | `d1856b6d346d`  |
| 2834   | Layout 1             | `d1856b6d346d`  |
| 2825   | Layout 1             | `d1856b6d346d`  |
| 2819   | Layout 1             | `d1856b6d346d`  |
| 2811   | Layout 1             | `d1856b6d346d`  |
| 2803   | Layout 1             | `d1856b6d346d`  |
| 2794   | Layout 1             | `d1856b6d346d`  |
| 2783   | Layout 1             | `d1856b6d346d`  |
| 2774   | Layout 1             | `d1856b6d346d`  |
| 2765   | Layout 1             | `d1856b6d346d`  |
| 2756   | Layout 1             | `d1856b6d346d`  |
| 2750   | Layout 1             | `d1856b6d346d`  |
| 2743   | Layout 1             | `d1856b6d346d`  |
| 2736   | Layout 1             | `d1856b6d346d`  |
| 2726   | Layout 1             | `d1856b6d346d`  |
| 2717   | Layout 1             | `d1856b6d346d`  |
| 2709   | Layout 1             | `d1856b6d346d`  |
| 2703   | Layout 1             | `d1856b6d346d`  |
| 2695   | Layout 1             | `d1856b6d346d`  |
| 2684   | Layout 1             | `d1856b6d346d`  |
| 2672   | Layout 1             | `d1856b6d346d`  |
| 2665   | Layout 1             | `d1856b6d346d`  |
| 2657   | Layout 1             | `d1856b6d346d`  |
| 2649   | Layout 1             | `d1856b6d346d`  |
| 2644   | Layout 1             | `d1856b6d346d`  |
| 2637   | Layout 1             | `d1856b6d346d`  |
| 2629   | Layout 1             | `d1856b6d346d`  |
| 2619   | Layout 1             | `d1856b6d346d`  |
| 2612   | Layout 1             | `d1856b6d346d`  |
| 2606   | Layout 1             | `d1856b6d346d`  |
| 2602   | Layout 1             | `d1856b6d346d`  |
| 2601   | Layout 1             | `d1856b6d346d`  |
| 2592   | Layout 1             | `d1856b6d346d`  |
| 2583   | Layout 1             | `d1856b6d346d`  |
| 2575   | Layout 1             | `d1856b6d346d`  |
| 2567   | Layout 1             | `d1856b6d346d`  |
| 2560   | Layout 1             | `d1856b6d346d`  |
| 2553   | Layout 1             | `d1856b6d346d`  |
| 2545   | Layout 1             | `d1856b6d346d`  |
| 2538   | Layout 1             | `d1856b6d346d`  |
| 2529   | Layout 1             | `d1856b6d346d`  |
| 2519   | Layout 1             | `d1856b6d346d`  |
| 2513   | Layout 1             | `d1856b6d346d`  |
| 2510   | Layout 1             | `d1856b6d346d`  |
| 2507   | Layout 1             | `d1856b6d346d`  |
| 2503   | Layout 1             | `d1856b6d346d`  |
| 2498   | Layout 1             | `d1856b6d346d`  |
| 2492   | Layout 1             | `d1856b6d346d`  |
| 2487   | Layout 1             | `d1856b6d346d`  |
| 2480   | Layout 1             | `d1856b6d346d`  |
| 2474   | Layout 1             | `d1856b6d346d`  |
| 2468   | Layout 1             | `d1856b6d346d`  |
| 2460   | Layout 1             | `d1856b6d346d`  |
| 2453   | Layout 1             | `d1856b6d346d`  |
| 2444   | Layout 1             | `d1856b6d346d`  |
| 2438   | Layout 1             | `d1856b6d346d`  |
| 2434   | Layout 1             | `d1856b6d346d`  |
| 2429   | Layout 1             | `d1856b6d346d`  |
| 2421   | Layout 1             | `d1856b6d346d`  |
| 2414   | Layout 1             | `d1856b6d346d`  |
| 2407   | Layout 1             | `d1856b6d346d`  |
| 2401   | Layout 1             | `d1856b6d346d`  |
| 2397   | Layout 1             | `d1856b6d346d`  |
| 2393   | Layout 1             | `d1856b6d346d`  |
| 2384   | Layout 1             | `d1856b6d346d`  |
| 2378   | Layout 1             | `d1856b6d346d`  |
| 2372   | Layout 1             | `d1856b6d346d`  |
| 2358   | Layout 1             | `d1856b6d346d`  |
| 2352   | Layout 1             | `d1856b6d346d`  |
| 2347   | Layout 1             | `d1856b6d346d`  |
| 2343   | Layout 1             | `d1856b6d346d`  |
| 2335   | Layout 1             | `d1856b6d346d`  |
| 2327   | Layout 1             | `d1856b6d346d`  |
| 2324   | Layout 1             | `d1856b6d346d`  |
| 2319   | Layout 1             | `d1856b6d346d`  |
| 2313   | Layout 1             | `d1856b6d346d`  |
| 2308   | Layout 1             | `d1856b6d346d`  |
| 2302   | Layout 1             | `d1856b6d346d`  |
| 2295   | Layout 1             | `d1856b6d346d`  |
| 2290   | Layout 1             | `d1856b6d346d`  |
| 2284   | Layout 1             | `d1856b6d346d`  |
| 2276   | Layout 1             | `d1856b6d346d`  |
| 2269   | Layout 1             | `d1856b6d346d`  |
| 2259   | Layout 1             | `d1856b6d346d`  |
| 2250   | Layout 1             | `d1856b6d346d`  |
| 2243   | Layout 1             | `d1856b6d346d`  |
| 2235   | Layout 1             | `d1856b6d346d`  |
| 2229   | Layout 1             | `d1856b6d346d`  |
| 2224   | Layout 1             | `d1856b6d346d`  |
| 2218   | Layout 1             | `d1856b6d346d`  |
| 2215   | Layout 1             | `d1856b6d346d`  |
| 2207   | Layout 1             | `d1856b6d346d`  |
| 2203   | Layout 1             | `d1856b6d346d`  |
| 2196   | Layout 1             | `d1856b6d346d`  |
| 2192   | Layout 1             | `d1856b6d346d`  |
| 2189   | Layout 1             | `d1856b6d346d`  |
| 2183   | Layout 1             | `d1856b6d346d`  |
| 2179   | Layout 1             | `d1856b6d346d`  |
| 2171   | Layout 1             | `d1856b6d346d`  |
| 2163   | Layout 1             | `d1856b6d346d`  |
| 2156   | Layout 1             | `d1856b6d346d`  |
| 2151   | Layout 1             | `d1856b6d346d`  |
| 2147   | Layout 1             | `d1856b6d346d`  |
| 2142   | Layout 1             | `d1856b6d346d`  |
| 2138   | Layout 1             | `d1856b6d346d`  |
| 2134   | Layout 1             | `d1856b6d346d`  |
| 2130   | Layout 1             | `d1856b6d346d`  |
| 2122   | Layout 1             | `d1856b6d346d`  |
| 2107   | Layout 1             | `d1856b6d346d`  |
| 2098   | Layout 1             | `d1856b6d346d`  |
| 2089   | Layout 1             | `d1856b6d346d`  |
| 2081   | Layout 1             | `d1856b6d346d`  |
| 2073   | Layout 1             | `d1856b6d346d`  |
| 2067   | Layout 1             | `d1856b6d346d`  |
| 2063   | Layout 1             | `d1856b6d346d`  |
| 2059   | Layout 1             | `d1856b6d346d`  |
| 2052   | Layout 1             | `d1856b6d346d`  |
| 2044   | Layout 1             | `d1856b6d346d`  |
| 2039   | Layout 1             | `d1856b6d346d`  |
| 2032   | Layout 1             | `d1856b6d346d`  |
| 2025   | Layout 1             | `d1856b6d346d`  |
| 2011   | Layout 1             | `d1856b6d346d`  |
| 2005   | Layout 1             | `d1856b6d346d`  |
| 2000   | Layout 1             | `d1856b6d346d`  |
| 1996   | Layout 1             | `d1856b6d346d`  |
| 1991   | Layout 1             | `d1856b6d346d`  |
| 1985   | Layout 1             | `d1856b6d346d`  |
| 1980   | Layout 1             | `d1856b6d346d`  |
| 1969   | Layout 1             | `d1856b6d346d`  |
| 1964   | Layout 1             | `d1856b6d346d`  |
| 1958   | Layout 1             | `d1856b6d346d`  |
| 1950   | Layout 1             | `d1856b6d346d`  |
| 1945   | Layout 1             | `d1856b6d346d`  |
| 1937   | Layout 1             | `d1856b6d346d`  |
| 1933   | Layout 1             | `d1856b6d346d`  |
| 1927   | Layout 1             | `d1856b6d346d`  |
| 1921   | Layout 1             | `d1856b6d346d`  |
| 1914   | Layout 1             | `d1856b6d346d`  |
| 1908   | Layout 1             | `d1856b6d346d`  |
| 1897   | Layout 1             | `d1856b6d346d`  |
| 1892   | Layout 1             | `d1856b6d346d`  |
| 1886   | Layout 1             | `d1856b6d346d`  |
| 1881   | Layout 1             | `d1856b6d346d`  |
| 1871   | Layout 1             | `d1856b6d346d`  |
| 1866   | Layout 1             | `d1856b6d346d`  |
| 1862   | Layout 1             | `d1856b6d346d`  |
| 1854   | Layout 1             | `d1856b6d346d`  |
| 1846   | Layout 1             | `d1856b6d346d`  |
| 1838   | Layout 1             | `d1856b6d346d`  |
| 1832   | Layout 1             | `d1856b6d346d`  |
| 1826   | Layout 1             | `d1856b6d346d`  |
| 1822   | Layout 1             | `d1856b6d346d`  |
| 1818   | Layout 1             | `d1856b6d346d`  |
| 1804   | Layout 1             | `d1856b6d346d`  |
| 1794   | Layout 1             | `d1856b6d346d`  |
| 1790   | Layout 1             | `d1856b6d346d`  |
| 1784   | Layout 1             | `d1856b6d346d`  |
| 1774   | Layout 1             | `d1856b6d346d`  |
| 1771   | Layout 1             | `d1856b6d346d`  |
| 1762   | Layout 1             | `d1856b6d346d`  |
| 1759   | Layout 1             | `d1856b6d346d`  |
| 1754   | Layout 1             | `d1856b6d346d`  |
| 1749   | Layout 1             | `d1856b6d346d`  |
| 1743   | Layout 1             | `d1856b6d346d`  |
| 1737   | Layout 1             | `d1856b6d346d`  |
| 1731   | Layout 1             | `d1856b6d346d`  |
| 1725   | Layout 1             | `d1856b6d346d`  |
| 1717   | Layout 1             | `d1856b6d346d`  |
| 1710   | Layout 1             | `d1856b6d346d`  |
| 1704   | Layout 1             | `d1856b6d346d`  |
| 1698   | Layout 1             | `d1856b6d346d`  |
| 1690   | Layout 1             | `d1856b6d346d`  |
| 1685   | Layout 1             | `d1856b6d346d`  |
| 1680   | Layout 1             | `d1856b6d346d`  |
| 1674   | Layout 1             | `d1856b6d346d`  |
| 1668   | Layout 1             | `d1856b6d346d`  |
| 1659   | Layout 1             | `d1856b6d346d`  |
| 1649   | Layout 1             | `d1856b6d346d`  |
| 1642   | Layout 1             | `d1856b6d346d`  |
| 1636   | Layout 1             | `d1856b6d346d`  |
| 1628   | Layout 1             | `d1856b6d346d`  |
| 1622   | Layout 1             | `d1856b6d346d`  |
| 1614   | Layout 1             | `d1856b6d346d`  |
| 1608   | Layout 1             | `d1856b6d346d`  |
| 1602   | Layout 1             | `d1856b6d346d`  |
| 1598   | Layout 1             | `d1856b6d346d`  |
| 1594   | Layout 1             | `d1856b6d346d`  |
| 1590   | Layout 1             | `d1856b6d346d`  |
| 1587   | Layout 1             | `d1856b6d346d`  |
| 1584   | Layout 1             | `d1856b6d346d`  |
| 1579   | Layout 1             | `d1856b6d346d`  |
| 1572   | Layout 1             | `d1856b6d346d`  |
| 1565   | Layout 1             | `d1856b6d346d`  |
| 1559   | Layout 1             | `d1856b6d346d`  |
| 1554   | Layout 1             | `d1856b6d346d`  |
| 1547   | Layout 1             | `d1856b6d346d`  |
| 1537   | Layout 1             | `d1856b6d346d`  |
| 1529   | Layout 1             | `d1856b6d346d`  |
| 1524   | Layout 1             | `d1856b6d346d`  |
| 1519   | Layout 1             | `d1856b6d346d`  |
| 1509   | Layout 1             | `d1856b6d346d`  |
| 1506   | Layout 1             | `d1856b6d346d`  |
| 1504   | Layout 1             | `d1856b6d346d`  |
| 1500   | Layout 1             | `d1856b6d346d`  |
| 1493   | Layout 1             | `d1856b6d346d`  |
| 1489   | Layout 1             | `d1856b6d346d`  |
| 1485   | Layout 1             | `d1856b6d346d`  |
| 1481   | Layout 1             | `d1856b6d346d`  |
| 1474   | Layout 1             | `d1856b6d346d`  |
| 1466   | Layout 1             | `d1856b6d346d`  |
| 1462   | Layout 1             | `d1856b6d346d`  |
| 1459   | Layout 1             | `d1856b6d346d`  |
| 1453   | Layout 1             | `d1856b6d346d`  |
| 1450   | Layout 1             | `d1856b6d346d`  |
| 1445   | Layout 1             | `d1856b6d346d`  |
| 1439   | Layout 1             | `d1856b6d346d`  |
| 1433   | Layout 1             | `d1856b6d346d`  |
| 1430   | Layout 1             | `d1856b6d346d`  |
| 1426   | Layout 1             | `d1856b6d346d`  |
| 1421   | Layout 1             | `d1856b6d346d`  |
| 1417   | Layout 1             | `d1856b6d346d`  |
| 1416   | Layout 1             | `d1856b6d346d`  |
| 1409   | Layout 1             | `d1856b6d346d`  |
| 1405   | Layout 1             | `d1856b6d346d`  |
| 1401   | Layout 1             | `d1856b6d346d`  |
| 1396   | Layout 1             | `d1856b6d346d`  |
| 1391   | Layout 1             | `d1856b6d346d`  |
| 1390   | Layout 1             | `d1856b6d346d`  |
| 1386   | Layout 1             | `d1856b6d346d`  |
| 1381   | Layout 1             | `d1856b6d346d`  |
| 1379   | Layout 1             | `d1856b6d346d`  |
| 1372   | Layout 1             | `d1856b6d346d`  |
| 1366   | Layout 1             | `d1856b6d346d`  |
| 1364   | Layout 1             | `d1856b6d346d`  |
| 1363   | Layout 1             | `d1856b6d346d`  |
| 1360   | Layout 1             | `d1856b6d346d`  |
| 1358   | Layout 1             | `d1856b6d346d`  |
| 1355   | Layout 1             | `d1856b6d346d`  |
| 1351   | Layout 1             | `d1856b6d346d`  |
| 1348   | Layout 1             | `d1856b6d346d`  |
| 1346   | Layout 1             | `d1856b6d346d`  |
| 1341   | Layout 1             | `d1856b6d346d`  |
| 1340   | Layout 1             | `d1856b6d346d`  |
| 1338   | Layout 1             | `d1856b6d346d`  |
| 1335   | Layout 1             | `d1856b6d346d`  |
| 1333   | Layout 1             | `d1856b6d346d`  |
| 1329   | Layout 1             | `d1856b6d346d`  |
| 1327   | Layout 1             | `d1856b6d346d`  |
| 1324   | Layout 1             | `d1856b6d346d`  |
| 1321   | Layout 1             | `d1856b6d346d`  |
| 1319   | Layout 1             | `d1856b6d346d`  |
| 1318   | Layout 1             | `d1856b6d346d`  |
| 1316   | Layout 1             | `d1856b6d346d`  |
| 1313   | Layout 1             | `d1856b6d346d`  |
| 1311   | Layout 1             | `d1856b6d346d`  |
| 1309   | Layout 1             | `d1856b6d346d`  |
| 1304   | Layout 1             | `d1856b6d346d`  |
| 1292   | Layout 1             | `d1856b6d346d`  |
| 1286   | Layout 1             | `d1856b6d346d`  |
| 1280   | Layout 1             | `d1856b6d346d`  |
| 1276   | Layout 1             | `d1856b6d346d`  |
| 1267   | Layout 1             | `d1856b6d346d`  |
| 1261   | Layout 1             | `d1856b6d346d`  |
| 1256   | Layout 1             | `d1856b6d346d`  |
| 1250   | Layout 1             | `d1856b6d346d`  |
| 1246   | Layout 1             | `d1856b6d346d`  |
| 1239   | Layout 1             | `d1856b6d346d`  |
| 1230   | Layout 1             | `d1856b6d346d`  |
| 1226   | Layout 1             | `d1856b6d346d`  |
| 1220   | Layout 1             | `d1856b6d346d`  |
| 1217   | Layout 1             | `d1856b6d346d`  |
| 1211   | Layout 1             | `d1856b6d346d`  |
| 1210   | Layout 1             | `d1856b6d346d`  |
| 1208   | Layout 1             | `d1856b6d346d`  |
| 1203   | Layout 1             | `d1856b6d346d`  |
| 1197   | Layout 1             | `d1856b6d346d`  |
| 1194   | Layout 1             | `d1856b6d346d`  |
| 1192   | Layout 1             | `d1856b6d346d`  |
| 1187   | Layout 1             | `d1856b6d346d`  |
| 1183   | Layout 1             | `d1856b6d346d`  |
| 1177   | Layout 1             | `d1856b6d346d`  |
| 1173   | Layout 1             | `d1856b6d346d`  |
| 1167   | Layout 1             | `d1856b6d346d`  |
| 1164   | Layout 1             | `d1856b6d346d`  |
| 1156   | Layout 1             | `d1856b6d346d`  |
| 1149   | Layout 1             | `d1856b6d346d`  |
| 1144   | Layout 1             | `d1856b6d346d`  |
| 1137   | Layout 1             | `d1856b6d346d`  |
| 1132   | Layout 1             | `d1856b6d346d`  |
| 1127   | Layout 1             | `d1856b6d346d`  |
| 1122   | Layout 1             | `d1856b6d346d`  |
| 1118   | Layout 1             | `d1856b6d346d`  |
| 1114   | Layout 1             | `d1856b6d346d`  |
| 1109   | Layout 1             | `d1856b6d346d`  |
| 1102   | No file              | `d1856b6d346d`  |
| 1096   | No file              | `d1856b6d346d`  |
| 1088   | No file              | `d1856b6d346d`  |
| 1081   | No file              | `d1856b6d346d`  |
| 1076   | No file              | `d1856b6d346d`  |
| 1069   | No file              | `d1856b6d346d`  |
| 1064   | No file              | `d1856b6d346d`  |
| 1058   | No file              | `d1856b6d346d`  |
| 1051   | No file              | `d1856b6d346d`  |
| 1044   | No file              | `d1856b6d346d`  |
| 1036   | No file              | `d1856b6d346d`  |
| 1026   | No file              | `d1856b6d346d`  |
| 1016   | No file              | `d1856b6d346d`  |
| 1009   | No file              | `d1856b6d346d`  |
| 1005   | No file              | `d1856b6d346d`  |
| 1000   | No file              | `d1856b6d346d`  |
| 998    | No file              | `d1856b6d346d`  |
| 990    | No file              | `d1856b6d346d`  |
| 979    | No file              | `d1856b6d346d`  |
| 972    | No file              | `d1856b6d346d`  |
| 963    | No file              | `d1856b6d346d`  |
| 955    | No file              | `d1856b6d346d`  |
| 946    | No file              | `d1856b6d346d`  |
| 938    | No file              | `d1856b6d346d`  |
| 927    | No file              | `d1856b6d346d`  |
| 911    | No file              | `d1856b6d346d`  |
| 904    | No file              | `d1856b6d346d`  |
| 899    | No file              | `d1856b6d346d`  |
| 894    | No file              | `d1856b6d346d`  |
| 885    | No file              | `d1856b6d346d`  |
| 879    | No file              | `d1856b6d346d`  |
| 872    | No file              | `d1856b6d346d`  |
| 864    | No file              | `d1856b6d346d`  |
| 855    | No file              | `d1856b6d346d`  |
| 853    | No file              | `d1856b6d346d`  |
| 845    | No file              | `d1856b6d346d`  |
| 837    | No file              | `d1856b6d346d`  |
| 829    | Layout 1             | `d1856b6d346d`  |
| 822    | Layout 1             | `d1856b6d346d`  |
| 814    | Layout 1             | `d1856b6d346d`  |
| 805    | Layout 1             | `d1856b6d346d`  |
| 794    | No documented layout | `d1856b6d346d`  |
| 787    | No documented layout | `d1856b6d346d`  |
| 780    | No documented layout | `d1856b6d346d`  |
| 771    | No documented layout | `d1856b6d346d`  |
| 760    | No documented layout | `d1856b6d346d`  |
| 748    | No documented layout | `d1856b6d346d`  |
| 741    | No documented layout | `d1856b6d346d`  |
| 736    | No documented layout | `d1856b6d346d`  |
| 731    | No documented layout | `d1856b6d346d`  |
| 723    | No documented layout | `d1856b6d346d`  |
| 711    | No documented layout | `d1856b6d346d`  |
| 707    | No documented layout | `d1856b6d346d`  |
| 697    | No documented layout | `d1856b6d346d`  |
| 689    | No documented layout | `d1856b6d346d`  |
| 683    | No documented layout | `d1856b6d346d`  |
| 678    | No documented layout | `d1856b6d346d`  |
| 670    | No documented layout | `d1856b6d346d`  |
| 661    | No documented layout | `d1856b6d346d`  |
| 656    | No documented layout | `d1856b6d346d`  |
| 652    | No documented layout | `d1856b6d346d`  |
| 643    | No documented layout | `d1856b6d346d`  |
| 637    | No documented layout | `d1856b6d346d`  |
| 630    | No documented layout | `d1856b6d346d`  |
| 627    | No documented layout | `d1856b6d346d`  |
| 621    | No documented layout | `d1856b6d346d`  |
| 617    | No documented layout | `d1856b6d346d`  |
| 615    | No documented layout | `d1856b6d346d`  |
| 606    | No documented layout | `d1856b6d346d`  |
| 599    | No documented layout | `d1856b6d346d`  |
| 592    | No documented layout | `d1856b6d346d`  |
| 586    | No documented layout | `d1856b6d346d`  |
| 577    | No documented layout | `d1856b6d346d`  |
| 569    | No documented layout | `d1856b6d346d`  |
| 561    | No documented layout | `d1856b6d346d`  |
| 554    | No documented layout | `d1856b6d346d`  |
| 542    | No documented layout | `d1856b6d346d`  |
| 532    | No documented layout | `d1856b6d346d`  |
| 531    | No documented layout | `d1856b6d346d`  |
| 526    | No documented layout | `d1856b6d346d`  |
| 521    | No documented layout | `d1856b6d346d`  |
| 517    | No documented layout | `d1856b6d346d`  |
| 510    | No documented layout | `d1856b6d346d`  |
| 508    | No documented layout | `d1856b6d346d`  |
| 504    | No documented layout | `d1856b6d346d`  |
| 497    | No documented layout | `d1856b6d346d`  |
| 491    | No documented layout | `d1856b6d346d`  |
| 485    | No documented layout | `d1856b6d346d`  |
| 478    | No documented layout | `d1856b6d346d`  |
| 472    | No documented layout | `d1856b6d346d`  |
| 466    | No documented layout | `d1856b6d346d`  |
| 457    | No file              | `d1856b6d346d`  |
| 452    | No file              | `d1856b6d346d`  |
| 449    | No file              | `d1856b6d346d`  |
| 435    | No file              | `d1856b6d346d`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names (LOC type 17, `str_id1 = region_key`)    |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type                             | Field              | Notes |
| ------------------- | -------------------------------- | ------------------ | ----- |
| `+0x00`             | char[4]                          | magic              | `PABR` (ASCII) |
| `+0x04`             | u32                              | record_count       | Observed `1594`, the same as `regioninfo.bss` |
| `+0x08`             | Region Link Record[record_count] | records            | Variable records packed back-to-back with no alignment |
| `records+0x00`      | String Table                     | string_table       | Shared `pabr_strings` layout; always empty here (`u32 count = 0`) |
| `string_table+0x00` | u32                              | string_table_start | Absolute file offset of `string_table.count`; the record walk ends exactly there |
| `string_table+0x04` | u32                              | zero               | Observed `0` |

### Region Link Record (variable: 10 bytes + links)

A record is `10 + 2 * link_count` bytes.

| Offset  | Type                | Field              | Notes |
| ------- | ------------------- | ------------------ | ----- |
| `+0x00` | u16                 | region_key         | `regioninfo.bss` region key; unique, and the key set equals that file's |
| `+0x02` | u32                 | link_count         | Number of keys that follow; `0` on 1536 records |
| `+0x06` | u32                 | unknown_06         | `0` in every record |
| `+0x0A` | u16[link_count]     | pc_delivery_region_keys | Region keys, in the same order as `regioninfo.bss` `pc_delivery_region_keys` for this region |

The records are not sorted by key. The file starts with regions 513, 1025, 1 (all `1 mod 512`), then 514, 1026, 2 and so on, which looks like a hash map written out in iteration order. The handler keeps file order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                       |
| ------- | ------------------ | ------------ | --------------------------- |
| `+0x00` | u32                | string_count | `0`; the table is always empty |
| `+0x04` | pstr[string_count] | strings      | None                        |

## Field Names

The 2016 client with debug symbols holds the list in `gc::RegionInfo` at
`+0x278` as `pa_vector<KeyType<u16>> _pcDeliveryRegionKeyList`. A private
server on client 1784 builds the same member in its `RegionInfo`
link-and-check step (VA `0x140c3a530`), which opens
`regionInfo_linkAndCheckValid2`: for every pair of regions with a flag set
(region byte `+0x2d`, not yet tied to a sheet column) it searches a path
over the waypoints, rejects a path through flagged waypoints, and pushes the
other region's key into this region's list, the region itself included. The
only reader of the list in that dump is the PC delivery request
(`gm::TrReservePcDeliveryReqTroc`, VA `0x141a27af9`), which looks up the
destination region in the current region's list and refuses a request whose
destination is missing; on success it calls the function that holds
`gm::PlayerActor::reservePcDelivery`. So the list is the set of regions a
character can be sent to from this region. No sheet column feeds it.

On client 1784 the 42 lists all hold their own region but are not all
mutual, since the path search runs once per ordered pair; on client 3474
the 58 lists are mutual. 5 of the 42 regions with a list on 1784 have the
same list on 3474; most grew (35 to 41 keys).

## Notes

- **The lists form groups.** Every list holds its own region, and the links are mutual: when A lists B, B lists A. There are 12 distinct lists in client 3458. 27 regions share Velia's 41-key list (the mainland towns from Velia to Muzgar and Velandir, plus town sub-regions such as Ossuary, Velia Beach and the three Calpheon trade zones); the seven Land of the Morning Light towns share one list; Valencia City and Ancado Inner Harbor list each other; Lema Island, Iliya Island, Arehaza and Oquilla's Eye list only themselves.
- **The groups overlap rather than partition.** Shakatu lists 18 towns (Glish, Eilton, Altinova ... Angavu Outpost) but not Velia, while Glish and Eilton list both Velia and Shakatu. Hakinza Sanctuary and Aal's Revelation list nine towns from Altinova to Angavu Outpost, and Angavu Outpost lists only Shakatu, Hakinza Sanctuary, Aal's Revelation and itself.
- The record walk was checked against client 3458: all 1594 records end exactly at `string_table_start`, and every list equals `regioninfo.bss` `pc_delivery_region_keys`, which [`regioninfo_bss.md`](regioninfo_bss.md) describes. The handler tests assert that equality, the mutual links and the self entry, so a patch that breaks any of them shows up.
- The file name says "link and check valid" and ends in `2`; no `regioninfo_linkandcheckvalid.bss` without the suffix exists in client 3458.

- **The lists form rings around Edania.** Grouping the 58 regions by their list gives the 12 lists (client 3458), in nine rows here since the four one-region lists only hold their own region; each list is shared by every region that owns it:

  | Size | Owned by | Compared with Velia's list |
  | ---- | -------- | -------------------------- |
  | 44   | Altinova, Asparkan, Sand Grain Bazaar, Muzgar, Velandir | adds Shakatu, Hakinza Sanctuary, Aal's Revelation |
  | 42   | Glish, Eilton, Tarif, Duvencrune, Ahib Conflict Zone, Marcha Outpost, O'draxxia, Salanar Pond, Delmira Plantation | adds Shakatu |
  | 41   | Velia, Heidel, Calpheon City, Olvia, Keplan, Port Epheria, Grána, Old Wisdom Tree and 19 more | the mainland from Velia to Muzgar, without Shakatu, Valencia City or the Edania towns |
  | 18   | Shakatu | the Mediah, Drieghan and Ulukita towns plus Hakinza Sanctuary, Aal's Revelation, Angavu Outpost |
  | 9    | Hakinza Sanctuary, Aal's Revelation | Altinova, Asparkan, Shakatu, Sand Grain Bazaar, Muzgar, Velandir and the three Edania towns |
  | 7    | the Land of the Morning Light towns | each other |
  | 4    | Angavu Outpost | Shakatu, Hakinza Sanctuary, Aal's Revelation, itself |
  | 2    | Valencia City, Ancado Inner Harbor | each other |
  | 1    | Lema Island, Iliya Island, Arehaza, Oquilla's Eye | itself |

  The deeper a town sits toward Edania, the smaller its list: Angavu Outpost reaches only Shakatu and the Edania towns, the Mediah and Ulukita towns reach both the mainland and Edania, and Velia's group reaches the mainland only. Valencia City, the islands and the Land of the Morning Light stand apart.

## Open Questions

### What `unknown_06` holds

The u32 between `link_count` and the keys is `0` in every record (1,066 on client 1784, 1,595 on 3474). It may be the upper half of a u64 `link_count`: the PABR reader of the client 1784 server reads string lengths as u64, and other PABR tables store u64 list counts. The server opens this file but reads no record from it in that build, so no code shows the width.
