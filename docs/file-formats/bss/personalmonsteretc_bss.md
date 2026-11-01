# `personalmonsteretc.bss` Format

## Purpose

The world map settings of the Dark Rift bosses of
[`personalmonster.dbss`](../dbss/personalmonster_dbss.md), one PABR value block:
the range within which the map shows a boss, the highest boss level, and
the icon sheet with the regions of its three difficulty frames and five
level marks. The file is the same 236 bytes on clients 1784 and 3474.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records        | Row bytes |
| ------ | -------------- | ------------------------ | ----- | -------------- | --------- |
| 1      | 1246 and later | `personalmonsteretc.bss` | 236   | 1 String Table | 72        |

| Layout | File                     | Known          | Unknown    |
| ------ | ------------------------ | -------------- | ---------- |
| 1      | `personalmonsteretc.bss` | 236 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a91f6761f19f`  |
| 3482   | Layout 1 | `a91f6761f19f`  |
| 3474   | Layout 1 | `a91f6761f19f`  |
| 3473   | Layout 1 | `a91f6761f19f`  |
| 3464   | Layout 1 | `a91f6761f19f`  |
| 3458   | Layout 1 | `a91f6761f19f`  |
| 3454   | Layout 1 | `a91f6761f19f`  |
| 3444   | Layout 1 | `a91f6761f19f`  |
| 3435   | Layout 1 | `a91f6761f19f`  |
| 3426   | Layout 1 | `a91f6761f19f`  |
| 3418   | Layout 1 | `a91f6761f19f`  |
| 3412   | Layout 1 | `a91f6761f19f`  |
| 3402   | Layout 1 | `a91f6761f19f`  |
| 3396   | Layout 1 | `a91f6761f19f`  |
| 3387   | Layout 1 | `a91f6761f19f`  |
| 3381   | Layout 1 | `a91f6761f19f`  |
| 3373   | Layout 1 | `a91f6761f19f`  |
| 3364   | Layout 1 | `a91f6761f19f`  |
| 3356   | Layout 1 | `a91f6761f19f`  |
| 3349   | Layout 1 | `a91f6761f19f`  |
| 3342   | Layout 1 | `a91f6761f19f`  |
| 3335   | Layout 1 | `a91f6761f19f`  |
| 3326   | Layout 1 | `a91f6761f19f`  |
| 3321   | Layout 1 | `a91f6761f19f`  |
| 3314   | Layout 1 | `a91f6761f19f`  |
| 3303   | Layout 1 | `a91f6761f19f`  |
| 3302   | Layout 1 | `a91f6761f19f`  |
| 3293   | Layout 1 | `a91f6761f19f`  |
| 3283   | Layout 1 | `a91f6761f19f`  |
| 3275   | Layout 1 | `a91f6761f19f`  |
| 3267   | Layout 1 | `a91f6761f19f`  |
| 3258   | Layout 1 | `a91f6761f19f`  |
| 3251   | Layout 1 | `a91f6761f19f`  |
| 3242   | Layout 1 | `a91f6761f19f`  |
| 3235   | Layout 1 | `a91f6761f19f`  |
| 3229   | Layout 1 | `a91f6761f19f`  |
| 3212   | Layout 1 | `a91f6761f19f`  |
| 3203   | Layout 1 | `a91f6761f19f`  |
| 3193   | Layout 1 | `a91f6761f19f`  |
| 3186   | Layout 1 | `a91f6761f19f`  |
| 3177   | Layout 1 | `a91f6761f19f`  |
| 3169   | Layout 1 | `a91f6761f19f`  |
| 3158   | Layout 1 | `a91f6761f19f`  |
| 3151   | Layout 1 | `a91f6761f19f`  |
| 3144   | Layout 1 | `a91f6761f19f`  |
| 3133   | Layout 1 | `a91f6761f19f`  |
| 3125   | Layout 1 | `a91f6761f19f`  |
| 3118   | Layout 1 | `a91f6761f19f`  |
| 3111   | Layout 1 | `a91f6761f19f`  |
| 3103   | Layout 1 | `a91f6761f19f`  |
| 3095   | Layout 1 | `a91f6761f19f`  |
| 3086   | Layout 1 | `a91f6761f19f`  |
| 3072   | Layout 1 | `a91f6761f19f`  |
| 3062   | Layout 1 | `a91f6761f19f`  |
| 3052   | Layout 1 | `a91f6761f19f`  |
| 3045   | Layout 1 | `a91f6761f19f`  |
| 3037   | Layout 1 | `a91f6761f19f`  |
| 3030   | Layout 1 | `a91f6761f19f`  |
| 3021   | Layout 1 | `a91f6761f19f`  |
| 3012   | Layout 1 | `a91f6761f19f`  |
| 3002   | Layout 1 | `a91f6761f19f`  |
| 2995   | Layout 1 | `a91f6761f19f`  |
| 2987   | Layout 1 | `a91f6761f19f`  |
| 2978   | Layout 1 | `a91f6761f19f`  |
| 2970   | Layout 1 | `a91f6761f19f`  |
| 2959   | Layout 1 | `a91f6761f19f`  |
| 2951   | Layout 1 | `a91f6761f19f`  |
| 2942   | Layout 1 | `a91f6761f19f`  |
| 2935   | Layout 1 | `a91f6761f19f`  |
| 2932   | Layout 1 | `a91f6761f19f`  |
| 2923   | Layout 1 | `a91f6761f19f`  |
| 2919   | Layout 1 | `a91f6761f19f`  |
| 2907   | Layout 1 | `a91f6761f19f`  |
| 2900   | Layout 1 | `a91f6761f19f`  |
| 2891   | Layout 1 | `a91f6761f19f`  |
| 2882   | Layout 1 | `a91f6761f19f`  |
| 2872   | Layout 1 | `a91f6761f19f`  |
| 2863   | Layout 1 | `a91f6761f19f`  |
| 2855   | Layout 1 | `a91f6761f19f`  |
| 2849   | Layout 1 | `a91f6761f19f`  |
| 2844   | Layout 1 | `a91f6761f19f`  |
| 2834   | Layout 1 | `a91f6761f19f`  |
| 2825   | Layout 1 | `a91f6761f19f`  |
| 2819   | Layout 1 | `a91f6761f19f`  |
| 2811   | Layout 1 | `a91f6761f19f`  |
| 2803   | Layout 1 | `a91f6761f19f`  |
| 2794   | Layout 1 | `a91f6761f19f`  |
| 2783   | Layout 1 | `a91f6761f19f`  |
| 2774   | Layout 1 | `a91f6761f19f`  |
| 2765   | Layout 1 | `a91f6761f19f`  |
| 2756   | Layout 1 | `a91f6761f19f`  |
| 2750   | Layout 1 | `a91f6761f19f`  |
| 2743   | Layout 1 | `a91f6761f19f`  |
| 2736   | Layout 1 | `a91f6761f19f`  |
| 2726   | Layout 1 | `a91f6761f19f`  |
| 2717   | Layout 1 | `a91f6761f19f`  |
| 2709   | Layout 1 | `a91f6761f19f`  |
| 2703   | Layout 1 | `a91f6761f19f`  |
| 2695   | Layout 1 | `a91f6761f19f`  |
| 2684   | Layout 1 | `a91f6761f19f`  |
| 2672   | Layout 1 | `a91f6761f19f`  |
| 2665   | Layout 1 | `a91f6761f19f`  |
| 2657   | Layout 1 | `a91f6761f19f`  |
| 2649   | Layout 1 | `a91f6761f19f`  |
| 2644   | Layout 1 | `a91f6761f19f`  |
| 2637   | Layout 1 | `a91f6761f19f`  |
| 2629   | Layout 1 | `a91f6761f19f`  |
| 2619   | Layout 1 | `a91f6761f19f`  |
| 2612   | Layout 1 | `a91f6761f19f`  |
| 2606   | Layout 1 | `a91f6761f19f`  |
| 2602   | Layout 1 | `a91f6761f19f`  |
| 2601   | Layout 1 | `a91f6761f19f`  |
| 2592   | Layout 1 | `a91f6761f19f`  |
| 2583   | Layout 1 | `a91f6761f19f`  |
| 2575   | Layout 1 | `a91f6761f19f`  |
| 2567   | Layout 1 | `a91f6761f19f`  |
| 2560   | Layout 1 | `a91f6761f19f`  |
| 2553   | Layout 1 | `a91f6761f19f`  |
| 2545   | Layout 1 | `a91f6761f19f`  |
| 2538   | Layout 1 | `a91f6761f19f`  |
| 2529   | Layout 1 | `a91f6761f19f`  |
| 2519   | Layout 1 | `a91f6761f19f`  |
| 2513   | Layout 1 | `a91f6761f19f`  |
| 2510   | Layout 1 | `a91f6761f19f`  |
| 2507   | Layout 1 | `a91f6761f19f`  |
| 2503   | Layout 1 | `a91f6761f19f`  |
| 2498   | Layout 1 | `a91f6761f19f`  |
| 2492   | Layout 1 | `a91f6761f19f`  |
| 2487   | Layout 1 | `a91f6761f19f`  |
| 2480   | Layout 1 | `a91f6761f19f`  |
| 2474   | Layout 1 | `a91f6761f19f`  |
| 2468   | Layout 1 | `a91f6761f19f`  |
| 2460   | Layout 1 | `a91f6761f19f`  |
| 2453   | Layout 1 | `a91f6761f19f`  |
| 2444   | Layout 1 | `a91f6761f19f`  |
| 2438   | Layout 1 | `a91f6761f19f`  |
| 2434   | Layout 1 | `a91f6761f19f`  |
| 2429   | Layout 1 | `a91f6761f19f`  |
| 2421   | Layout 1 | `a91f6761f19f`  |
| 2414   | Layout 1 | `a91f6761f19f`  |
| 2407   | Layout 1 | `a91f6761f19f`  |
| 2401   | Layout 1 | `a91f6761f19f`  |
| 2397   | Layout 1 | `a91f6761f19f`  |
| 2393   | Layout 1 | `a91f6761f19f`  |
| 2384   | Layout 1 | `a91f6761f19f`  |
| 2378   | Layout 1 | `a91f6761f19f`  |
| 2372   | Layout 1 | `a91f6761f19f`  |
| 2358   | Layout 1 | `a91f6761f19f`  |
| 2352   | Layout 1 | `a91f6761f19f`  |
| 2347   | Layout 1 | `a91f6761f19f`  |
| 2343   | Layout 1 | `a91f6761f19f`  |
| 2335   | Layout 1 | `a91f6761f19f`  |
| 2327   | Layout 1 | `a91f6761f19f`  |
| 2324   | Layout 1 | `a91f6761f19f`  |
| 2319   | Layout 1 | `a91f6761f19f`  |
| 2313   | Layout 1 | `a91f6761f19f`  |
| 2308   | Layout 1 | `a91f6761f19f`  |
| 2302   | Layout 1 | `a91f6761f19f`  |
| 2295   | Layout 1 | `a91f6761f19f`  |
| 2290   | Layout 1 | `a91f6761f19f`  |
| 2284   | Layout 1 | `a91f6761f19f`  |
| 2276   | Layout 1 | `a91f6761f19f`  |
| 2269   | Layout 1 | `a91f6761f19f`  |
| 2259   | Layout 1 | `a91f6761f19f`  |
| 2250   | Layout 1 | `a91f6761f19f`  |
| 2243   | Layout 1 | `a91f6761f19f`  |
| 2235   | Layout 1 | `a91f6761f19f`  |
| 2229   | Layout 1 | `a91f6761f19f`  |
| 2224   | Layout 1 | `a91f6761f19f`  |
| 2218   | Layout 1 | `a91f6761f19f`  |
| 2215   | Layout 1 | `a91f6761f19f`  |
| 2207   | Layout 1 | `a91f6761f19f`  |
| 2203   | Layout 1 | `a91f6761f19f`  |
| 2196   | Layout 1 | `a91f6761f19f`  |
| 2192   | Layout 1 | `a91f6761f19f`  |
| 2189   | Layout 1 | `a91f6761f19f`  |
| 2183   | Layout 1 | `a91f6761f19f`  |
| 2179   | Layout 1 | `a91f6761f19f`  |
| 2171   | Layout 1 | `a91f6761f19f`  |
| 2163   | Layout 1 | `a91f6761f19f`  |
| 2156   | Layout 1 | `a91f6761f19f`  |
| 2151   | Layout 1 | `a91f6761f19f`  |
| 2147   | Layout 1 | `a91f6761f19f`  |
| 2142   | Layout 1 | `a91f6761f19f`  |
| 2138   | Layout 1 | `a91f6761f19f`  |
| 2134   | Layout 1 | `a91f6761f19f`  |
| 2130   | Layout 1 | `a91f6761f19f`  |
| 2122   | Layout 1 | `a91f6761f19f`  |
| 2107   | Layout 1 | `a91f6761f19f`  |
| 2098   | Layout 1 | `a91f6761f19f`  |
| 2089   | Layout 1 | `a91f6761f19f`  |
| 2081   | Layout 1 | `a91f6761f19f`  |
| 2073   | Layout 1 | `a91f6761f19f`  |
| 2067   | Layout 1 | `a91f6761f19f`  |
| 2063   | Layout 1 | `a91f6761f19f`  |
| 2059   | Layout 1 | `a91f6761f19f`  |
| 2052   | Layout 1 | `a91f6761f19f`  |
| 2044   | Layout 1 | `a91f6761f19f`  |
| 2039   | Layout 1 | `a91f6761f19f`  |
| 2032   | Layout 1 | `a91f6761f19f`  |
| 2025   | Layout 1 | `a91f6761f19f`  |
| 2011   | Layout 1 | `a91f6761f19f`  |
| 2005   | Layout 1 | `a91f6761f19f`  |
| 2000   | Layout 1 | `a91f6761f19f`  |
| 1996   | Layout 1 | `a91f6761f19f`  |
| 1991   | Layout 1 | `a91f6761f19f`  |
| 1985   | Layout 1 | `a91f6761f19f`  |
| 1980   | Layout 1 | `a91f6761f19f`  |
| 1969   | Layout 1 | `a91f6761f19f`  |
| 1964   | Layout 1 | `a91f6761f19f`  |
| 1958   | Layout 1 | `a91f6761f19f`  |
| 1950   | Layout 1 | `a91f6761f19f`  |
| 1945   | Layout 1 | `a91f6761f19f`  |
| 1937   | Layout 1 | `a91f6761f19f`  |
| 1933   | Layout 1 | `a91f6761f19f`  |
| 1927   | Layout 1 | `a91f6761f19f`  |
| 1921   | Layout 1 | `a91f6761f19f`  |
| 1914   | Layout 1 | `a91f6761f19f`  |
| 1908   | Layout 1 | `a91f6761f19f`  |
| 1897   | Layout 1 | `a91f6761f19f`  |
| 1892   | Layout 1 | `a91f6761f19f`  |
| 1886   | Layout 1 | `a91f6761f19f`  |
| 1881   | Layout 1 | `a91f6761f19f`  |
| 1871   | Layout 1 | `a91f6761f19f`  |
| 1866   | Layout 1 | `a91f6761f19f`  |
| 1862   | Layout 1 | `a91f6761f19f`  |
| 1854   | Layout 1 | `a91f6761f19f`  |
| 1846   | Layout 1 | `a91f6761f19f`  |
| 1838   | Layout 1 | `a91f6761f19f`  |
| 1832   | Layout 1 | `a91f6761f19f`  |
| 1826   | Layout 1 | `a91f6761f19f`  |
| 1822   | Layout 1 | `a91f6761f19f`  |
| 1818   | Layout 1 | `a91f6761f19f`  |
| 1804   | Layout 1 | `a91f6761f19f`  |
| 1794   | Layout 1 | `a91f6761f19f`  |
| 1790   | Layout 1 | `a91f6761f19f`  |
| 1784   | Layout 1 | `a91f6761f19f`  |
| 1774   | Layout 1 | `a91f6761f19f`  |
| 1771   | Layout 1 | `a91f6761f19f`  |
| 1762   | Layout 1 | `a91f6761f19f`  |
| 1759   | Layout 1 | `a91f6761f19f`  |
| 1754   | Layout 1 | `a91f6761f19f`  |
| 1749   | Layout 1 | `a91f6761f19f`  |
| 1743   | Layout 1 | `a91f6761f19f`  |
| 1737   | Layout 1 | `a91f6761f19f`  |
| 1731   | Layout 1 | `a91f6761f19f`  |
| 1725   | Layout 1 | `a91f6761f19f`  |
| 1717   | Layout 1 | `a91f6761f19f`  |
| 1710   | Layout 1 | `a91f6761f19f`  |
| 1704   | Layout 1 | `a91f6761f19f`  |
| 1698   | Layout 1 | `a91f6761f19f`  |
| 1690   | Layout 1 | `a91f6761f19f`  |
| 1685   | Layout 1 | `a91f6761f19f`  |
| 1680   | Layout 1 | `a91f6761f19f`  |
| 1674   | Layout 1 | `a91f6761f19f`  |
| 1668   | Layout 1 | `a91f6761f19f`  |
| 1659   | Layout 1 | `a91f6761f19f`  |
| 1649   | Layout 1 | `a91f6761f19f`  |
| 1642   | Layout 1 | `a91f6761f19f`  |
| 1636   | Layout 1 | `a91f6761f19f`  |
| 1628   | Layout 1 | `a91f6761f19f`  |
| 1622   | Layout 1 | `a91f6761f19f`  |
| 1614   | Layout 1 | `a91f6761f19f`  |
| 1608   | Layout 1 | `a91f6761f19f`  |
| 1602   | Layout 1 | `a91f6761f19f`  |
| 1598   | Layout 1 | `a91f6761f19f`  |
| 1594   | Layout 1 | `a91f6761f19f`  |
| 1590   | Layout 1 | `a91f6761f19f`  |
| 1587   | Layout 1 | `a91f6761f19f`  |
| 1584   | Layout 1 | `a91f6761f19f`  |
| 1579   | Layout 1 | `a91f6761f19f`  |
| 1572   | Layout 1 | `a91f6761f19f`  |
| 1565   | Layout 1 | `a91f6761f19f`  |
| 1559   | Layout 1 | `a91f6761f19f`  |
| 1554   | Layout 1 | `a91f6761f19f`  |
| 1547   | Layout 1 | `a91f6761f19f`  |
| 1537   | Layout 1 | `a91f6761f19f`  |
| 1529   | Layout 1 | `a91f6761f19f`  |
| 1524   | Layout 1 | `a91f6761f19f`  |
| 1519   | Layout 1 | `a91f6761f19f`  |
| 1509   | Layout 1 | `a91f6761f19f`  |
| 1506   | Layout 1 | `a91f6761f19f`  |
| 1504   | Layout 1 | `a91f6761f19f`  |
| 1500   | Layout 1 | `a91f6761f19f`  |
| 1493   | Layout 1 | `a91f6761f19f`  |
| 1489   | Layout 1 | `a91f6761f19f`  |
| 1485   | Layout 1 | `a91f6761f19f`  |
| 1481   | Layout 1 | `a91f6761f19f`  |
| 1474   | Layout 1 | `a91f6761f19f`  |
| 1466   | Layout 1 | `a91f6761f19f`  |
| 1462   | Layout 1 | `a91f6761f19f`  |
| 1459   | Layout 1 | `a91f6761f19f`  |
| 1453   | Layout 1 | `a91f6761f19f`  |
| 1450   | Layout 1 | `a91f6761f19f`  |
| 1445   | Layout 1 | `a91f6761f19f`  |
| 1439   | Layout 1 | `a91f6761f19f`  |
| 1433   | Layout 1 | `a91f6761f19f`  |
| 1430   | Layout 1 | `a91f6761f19f`  |
| 1426   | Layout 1 | `a91f6761f19f`  |
| 1421   | Layout 1 | `a91f6761f19f`  |
| 1417   | Layout 1 | `a91f6761f19f`  |
| 1416   | Layout 1 | `a91f6761f19f`  |
| 1409   | Layout 1 | `a91f6761f19f`  |
| 1405   | Layout 1 | `a91f6761f19f`  |
| 1401   | Layout 1 | `a91f6761f19f`  |
| 1396   | Layout 1 | `a91f6761f19f`  |
| 1391   | Layout 1 | `a91f6761f19f`  |
| 1390   | Layout 1 | `a91f6761f19f`  |
| 1386   | Layout 1 | `a91f6761f19f`  |
| 1381   | Layout 1 | `a91f6761f19f`  |
| 1379   | Layout 1 | `a91f6761f19f`  |
| 1372   | Layout 1 | `a91f6761f19f`  |
| 1366   | Layout 1 | `a91f6761f19f`  |
| 1364   | Layout 1 | `a91f6761f19f`  |
| 1363   | Layout 1 | `a91f6761f19f`  |
| 1360   | Layout 1 | `a91f6761f19f`  |
| 1358   | Layout 1 | `a91f6761f19f`  |
| 1355   | Layout 1 | `a91f6761f19f`  |
| 1351   | Layout 1 | `a91f6761f19f`  |
| 1348   | Layout 1 | `a91f6761f19f`  |
| 1346   | Layout 1 | `a91f6761f19f`  |
| 1341   | Layout 1 | `a91f6761f19f`  |
| 1340   | Layout 1 | `a91f6761f19f`  |
| 1338   | Layout 1 | `a91f6761f19f`  |
| 1335   | Layout 1 | `a91f6761f19f`  |
| 1333   | Layout 1 | `a91f6761f19f`  |
| 1329   | Layout 1 | `a91f6761f19f`  |
| 1327   | Layout 1 | `a91f6761f19f`  |
| 1324   | Layout 1 | `a91f6761f19f`  |
| 1321   | Layout 1 | `a91f6761f19f`  |
| 1319   | Layout 1 | `a91f6761f19f`  |
| 1318   | Layout 1 | `a91f6761f19f`  |
| 1316   | Layout 1 | `a91f6761f19f`  |
| 1313   | Layout 1 | `a91f6761f19f`  |
| 1311   | Layout 1 | `a91f6761f19f`  |
| 1309   | Layout 1 | `a91f6761f19f`  |
| 1304   | Layout 1 | `a91f6761f19f`  |
| 1292   | Layout 1 | `a91f6761f19f`  |
| 1286   | Layout 1 | `a91f6761f19f`  |
| 1280   | Layout 1 | `a91f6761f19f`  |
| 1276   | Layout 1 | `a91f6761f19f`  |
| 1267   | Layout 1 | `a91f6761f19f`  |
| 1261   | Layout 1 | `a91f6761f19f`  |
| 1256   | Layout 1 | `a91f6761f19f`  |
| 1250   | Layout 1 | `a91f6761f19f`  |
| 1246   | Layout 1 | `a91f6761f19f`  |
| 1239   | No file  | `a91f6761f19f`  |
| 1230   | No file  | `a91f6761f19f`  |
| 1226   | No file  | `a91f6761f19f`  |
| 1220   | No file  | `a91f6761f19f`  |
| 1217   | No file  | `a91f6761f19f`  |
| 1211   | No file  | `a91f6761f19f`  |
| 1210   | No file  | `a91f6761f19f`  |
| 1208   | No file  | `a91f6761f19f`  |
| 1203   | No file  | `a91f6761f19f`  |
| 1197   | No file  | `a91f6761f19f`  |
| 1194   | No file  | `a91f6761f19f`  |
| 1192   | No file  | `a91f6761f19f`  |
| 1187   | No file  | `a91f6761f19f`  |
| 1183   | No file  | `a91f6761f19f`  |
| 1177   | No file  | `a91f6761f19f`  |
| 1173   | No file  | `a91f6761f19f`  |
| 1167   | No file  | `a91f6761f19f`  |
| 1164   | No file  | `a91f6761f19f`  |
| 1156   | No file  | `a91f6761f19f`  |
| 1149   | No file  | `a91f6761f19f`  |
| 1144   | No file  | `a91f6761f19f`  |
| 1137   | No file  | `a91f6761f19f`  |
| 1132   | No file  | `a91f6761f19f`  |
| 1127   | No file  | `a91f6761f19f`  |
| 1122   | No file  | `a91f6761f19f`  |
| 1118   | No file  | `a91f6761f19f`  |
| 1114   | No file  | `a91f6761f19f`  |
| 1109   | No file  | `a91f6761f19f`  |
| 1102   | No file  | `a91f6761f19f`  |
| 1096   | No file  | `a91f6761f19f`  |
| 1088   | No file  | `a91f6761f19f`  |
| 1081   | No file  | `a91f6761f19f`  |
| 1076   | No file  | `a91f6761f19f`  |
| 1069   | No file  | `a91f6761f19f`  |
| 1064   | No file  | `a91f6761f19f`  |
| 1058   | No file  | `a91f6761f19f`  |
| 1051   | No file  | `a91f6761f19f`  |
| 1044   | No file  | `a91f6761f19f`  |
| 1036   | No file  | `a91f6761f19f`  |
| 1026   | No file  | `a91f6761f19f`  |
| 1016   | No file  | `a91f6761f19f`  |
| 1009   | No file  | `a91f6761f19f`  |
| 1005   | No file  | `a91f6761f19f`  |
| 1000   | No file  | `a91f6761f19f`  |
| 998    | No file  | `a91f6761f19f`  |
| 990    | No file  | `a91f6761f19f`  |
| 979    | No file  | `a91f6761f19f`  |
| 972    | No file  | `a91f6761f19f`  |
| 963    | No file  | `a91f6761f19f`  |
| 955    | No file  | `a91f6761f19f`  |
| 946    | No file  | `a91f6761f19f`  |
| 938    | No file  | `a91f6761f19f`  |
| 927    | No file  | `a91f6761f19f`  |
| 911    | No file  | `a91f6761f19f`  |
| 904    | No file  | `a91f6761f19f`  |
| 899    | No file  | `a91f6761f19f`  |
| 894    | No file  | `a91f6761f19f`  |
| 885    | No file  | `a91f6761f19f`  |
| 879    | No file  | `a91f6761f19f`  |
| 872    | No file  | `a91f6761f19f`  |
| 864    | No file  | `a91f6761f19f`  |
| 855    | No file  | `a91f6761f19f`  |
| 853    | No file  | `a91f6761f19f`  |
| 845    | No file  | `a91f6761f19f`  |
| 837    | No file  | `a91f6761f19f`  |
| 829    | No file  | `a91f6761f19f`  |
| 822    | No file  | `a91f6761f19f`  |
| 814    | No file  | `a91f6761f19f`  |
| 805    | No file  | `a91f6761f19f`  |
| 794    | No file  | `a91f6761f19f`  |
| 787    | No file  | `a91f6761f19f`  |
| 780    | No file  | `a91f6761f19f`  |
| 771    | No file  | `a91f6761f19f`  |
| 760    | No file  | `a91f6761f19f`  |
| 748    | No file  | `a91f6761f19f`  |
| 741    | No file  | `a91f6761f19f`  |
| 736    | No file  | `a91f6761f19f`  |
| 731    | No file  | `a91f6761f19f`  |
| 723    | No file  | `a91f6761f19f`  |
| 711    | No file  | `a91f6761f19f`  |
| 707    | No file  | `a91f6761f19f`  |
| 697    | No file  | `a91f6761f19f`  |
| 689    | No file  | `a91f6761f19f`  |
| 683    | No file  | `a91f6761f19f`  |
| 678    | No file  | `a91f6761f19f`  |
| 670    | No file  | `a91f6761f19f`  |
| 661    | No file  | `a91f6761f19f`  |
| 656    | No file  | `a91f6761f19f`  |
| 652    | No file  | `a91f6761f19f`  |
| 643    | No file  | `a91f6761f19f`  |
| 637    | No file  | `a91f6761f19f`  |
| 630    | No file  | `a91f6761f19f`  |
| 627    | No file  | `a91f6761f19f`  |
| 621    | No file  | `a91f6761f19f`  |
| 617    | No file  | `a91f6761f19f`  |
| 615    | No file  | `a91f6761f19f`  |
| 606    | No file  | `a91f6761f19f`  |
| 599    | No file  | `a91f6761f19f`  |
| 592    | No file  | `a91f6761f19f`  |
| 586    | No file  | `a91f6761f19f`  |
| 577    | No file  | `a91f6761f19f`  |
| 569    | No file  | `a91f6761f19f`  |
| 561    | No file  | `a91f6761f19f`  |
| 554    | No file  | `a91f6761f19f`  |
| 542    | No file  | `a91f6761f19f`  |
| 532    | No file  | `a91f6761f19f`  |
| 531    | No file  | `a91f6761f19f`  |
| 526    | No file  | `a91f6761f19f`  |
| 521    | No file  | `a91f6761f19f`  |
| 517    | No file  | `a91f6761f19f`  |
| 510    | No file  | `a91f6761f19f`  |
| 508    | No file  | `a91f6761f19f`  |
| 504    | No file  | `a91f6761f19f`  |
| 497    | No file  | `a91f6761f19f`  |
| 491    | No file  | `a91f6761f19f`  |
| 485    | No file  | `a91f6761f19f`  |
| 478    | No file  | `a91f6761f19f`  |
| 472    | No file  | `a91f6761f19f`  |
| 466    | No file  | `a91f6761f19f`  |
| 457    | No file  | `a91f6761f19f`  |
| 452    | No file  | `a91f6761f19f`  |
| 449    | No file  | `a91f6761f19f`  |
| 435    | No file  | `a91f6761f19f`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field                      | Notes                                                                    |
| ------------------- | ------------ | -------------------------- | ------------------------------------------------------------------------ |
| `+0x00`             | char[4]      | magic                      | ASCII `PABR`                                                             |
| `+0x04`             | u32          | monster_icon_image_ref     | String table index of the icon sheet path; `0` on clients 1784 and 3474  |
| `+0x08`             | f32          | detect_range               | `2000000`; the world map shows a boss once an adventurer is this close   |
| `+0x0C`             | u32          | max_level                  | `5`; the highest boss level                                              |
| `+0x10`             | f32[2]       | icon_size                  | `119, 119`: width and height of the world map icon                       |
| `+0x18`             | f32[3][4]    | difficulty_icon_uvs        | Per difficulty `1` to `3` a region `x1, y1, x2, y2` of the icon sheet    |
| `+0x48`             | f32[5][4]    | level_icon_uvs             | Per level `1` to `5` a region `x1, y1, x2, y2` of the icon sheet         |
| `+0x98`             | u32          | total_accept_condition_ref | String table index of the accept condition; `1` (empty) on clients 1784 and 3474 |
| `+0x9C`             | String Table | string_table               | See String Table                                                         |
| `string_table+0x00` | u32          | table_start                | Offset of the string table; `0x9C` on clients 1784 and 3474              |
| `string_table+0x04` | u32          | zero                       | Always `0`                                                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `2` on clients 1784 and 3474 |
| `+0x04` | pstr[string_count] | strings      | See Strings                               |

## Strings

| Index | Wide | Field                      | Text (clients 1784 and 3474)                                 |
| ----- | ---- | -------------------------- | ------------------------------------------------------------ |
| 0     | `0`  | monster_icon_image_ref     | `renewal/PcRemaster/Remaster_Icon_Worldmap_AutoBoss_All.dds` |
| 1     | `1`  | total_accept_condition_ref | Empty                                                        |

String 0 is the sheet's `MonsterIconImage`, the icon sheet the regions
below cut from. String 1 is its `TotalAcceptCondition`, empty in the
sheet.

## Icon Regions

The regions on clients 1784 and 3474, in pixels of the icon sheet. The
sheet's notes call the three difficulty frames normal, hard and very hard;
the LOC labels of `personalmonster.dbss` difficulties `1` to `3` read
Normal, Difficult and Very Difficult.

| Field                 | Entry | x1  | y1  | x2  | y2  |
| --------------------- | ----- | --- | --- | --- | --- |
| `difficulty_icon_uvs` | 1     | 1   | 1   | 120 | 120 |
| `difficulty_icon_uvs` | 2     | 121 | 1   | 240 | 120 |
| `difficulty_icon_uvs` | 3     | 241 | 1   | 360 | 120 |
| `level_icon_uvs`      | 1     | 361 | 1   | 480 | 120 |
| `level_icon_uvs`      | 2     | 1   | 121 | 120 | 240 |
| `level_icon_uvs`      | 3     | 121 | 121 | 240 | 240 |
| `level_icon_uvs`      | 4     | 241 | 121 | 360 | 240 |
| `level_icon_uvs`      | 5     | 361 | 121 | 480 | 240 |

## Field Names

The `PersonalMonsterOption_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has one row. Its client columns are
`DetectRange`, `MonsterIcon`, `MonsterIconImage`, `IconSize`,
`UV Difficulty1` to `UV Difficulty3`, `UV Level1` to `UV Level5`,
`MaxLevel` and `TotalAcceptCondition`; `MaxSpawnMonster`,
`DailySpawnMonster`, `DailySpawnTime`, `DailySpawnVariableTime`,
`LevelUpCycle`, `APDecreaseRate` and `DPDecreaseRate` are server-only
(`%`) and not in the file. The file matches the row on every value it
holds: `DetectRange` `2000000`, `MaxLevel` `5`, `IconSize` `119,119`, the
32 numbers of the eight `UV` columns in column order, and
`MonsterIconImage` as string 0. The sheet's developer notes call
`DetectRange` the distance at which the world map shows the monster,
`MaxLevel` the highest number of Dark Rift level-ups, and the `UV` columns
the difficulty and level regions of the world map boss icon. The 2016
client's debug symbols have no personal monster type.

The server loader for the sheet in the client 1784 server dump reads
`MonsterIconImage` first, as a narrow string, then `DetectRange`,
`LevelUpCycle`, `MaxLevel`, `APDecreaseRate`, `DPDecreaseRate` and
`IconSize`, and `TotalAcceptCondition` last, as a wide string, into the
last member of its option struct. The file keeps that order without the
server-only columns: `monster_icon_image_ref` before `detect_range`, and
`total_accept_condition_ref` after the regions. Each index points at a
string of the matching kind: string 0 is narrow (`is_wide` `0`), string 1
wide (`is_wide` `1`).

## Notes

- `MonsterIcon` lists three `.dds` paths in the sheet; the file holds none
  of them.
- The Dark Rift window's Lua (`panel_window_personalmonster_all.luac`,
  client 3474) has its own copy of the regions (`x2 = 480`, `y2 = 240`)
  and names levels `I` to `VII` in `_difficultyRoma`, two more than
  `max_level`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/personalmonster_tables.py`:
  one row with the icon sheet path, the range, the highest level, the icon
  size as `width x height` and each icon region as `x1, y1, x2, y2` on its
  own line. The empty accept condition gets no column.
