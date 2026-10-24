# `knowledgelearning.dbss` Format

## Purpose

Defines how knowledge entries are obtained from characters and items. The file holds two tables: table 0 maps a character ID (a monster, NPC, gathering node or other `characterstatic.dbss` entry) to the knowledge card it teaches, and table 1 maps an item ID to the card it teaches. Parsing is driven by `knowledgelearningoffset.dbss`, which gives each record's source ID, byte offset and size.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records                                                       | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ------ | ------------------------------------------------------------- | --------- |
| 1      | 1346 and later | 3483    | `knowledgelearning.dbss`       | 79,534 | 4,678 Learning Record, 4,678 Learning Entry, 2 Learning Table | 13        |
| 1      | 1346 and later | 3483    | `knowledgelearningoffset.dbss` | 56,148 | 4,678 Index Row, 2 Index Table                                | 12        |

| Layout | File                           | Known             | Unknown        |
| ------ | ------------------------------ | ----------------- | -------------- |
| 1      | `knowledgelearning.dbss`       | 74,856 B (94.1%)  | 4,678 B (5.9%) |
| 1      | `knowledgelearningoffset.dbss` | 56,148 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `1d3516d2562c`  |
| 3482   | Layout 1             | `1d3516d2562c`  |
| 3474   | Layout 1             | `1d3516d2562c`  |
| 3473   | Layout 1             | `1d3516d2562c`  |
| 3464   | Layout 1             | `1d3516d2562c`  |
| 3458   | Layout 1             | `1d3516d2562c`  |
| 3454   | Layout 1             | `1d3516d2562c`  |
| 3444   | Layout 1             | `1d3516d2562c`  |
| 3435   | Layout 1             | `1d3516d2562c`  |
| 3426   | Layout 1             | `1d3516d2562c`  |
| 3418   | Layout 1             | `1d3516d2562c`  |
| 3412   | Layout 1             | `1d3516d2562c`  |
| 3402   | Layout 1             | `1d3516d2562c`  |
| 3396   | Layout 1             | `1d3516d2562c`  |
| 3387   | Layout 1             | `1d3516d2562c`  |
| 3381   | Layout 1             | `1d3516d2562c`  |
| 3373   | Layout 1             | `1d3516d2562c`  |
| 3364   | Layout 1             | `1d3516d2562c`  |
| 3356   | Layout 1             | `1d3516d2562c`  |
| 3349   | Layout 1             | `1d3516d2562c`  |
| 3342   | Layout 1             | `1d3516d2562c`  |
| 3335   | Layout 1             | `1d3516d2562c`  |
| 3326   | Layout 1             | `1d3516d2562c`  |
| 3321   | Layout 1             | `1d3516d2562c`  |
| 3314   | Layout 1             | `1d3516d2562c`  |
| 3303   | Layout 1             | `1d3516d2562c`  |
| 3302   | Layout 1             | `1d3516d2562c`  |
| 3293   | Layout 1             | `1d3516d2562c`  |
| 3283   | Layout 1             | `1d3516d2562c`  |
| 3275   | Layout 1             | `1d3516d2562c`  |
| 3267   | Layout 1             | `1d3516d2562c`  |
| 3258   | Layout 1             | `1d3516d2562c`  |
| 3251   | Layout 1             | `1d3516d2562c`  |
| 3242   | Layout 1             | `1d3516d2562c`  |
| 3235   | Layout 1             | `1d3516d2562c`  |
| 3229   | Layout 1             | `1d3516d2562c`  |
| 3212   | Layout 1             | `1d3516d2562c`  |
| 3203   | Layout 1             | `1d3516d2562c`  |
| 3193   | Layout 1             | `1d3516d2562c`  |
| 3186   | Layout 1             | `1d3516d2562c`  |
| 3177   | Layout 1             | `1d3516d2562c`  |
| 3169   | Layout 1             | `1d3516d2562c`  |
| 3158   | Layout 1             | `1d3516d2562c`  |
| 3151   | Layout 1             | `1d3516d2562c`  |
| 3144   | Layout 1             | `1d3516d2562c`  |
| 3133   | Layout 1             | `1d3516d2562c`  |
| 3125   | Layout 1             | `1d3516d2562c`  |
| 3118   | Layout 1             | `1d3516d2562c`  |
| 3111   | Layout 1             | `1d3516d2562c`  |
| 3103   | Layout 1             | `1d3516d2562c`  |
| 3095   | Layout 1             | `1d3516d2562c`  |
| 3086   | Layout 1             | `1d3516d2562c`  |
| 3072   | Layout 1             | `1d3516d2562c`  |
| 3062   | Layout 1             | `1d3516d2562c`  |
| 3052   | Layout 1             | `1d3516d2562c`  |
| 3045   | Layout 1             | `1d3516d2562c`  |
| 3037   | Layout 1             | `1d3516d2562c`  |
| 3030   | Layout 1             | `1d3516d2562c`  |
| 3021   | Layout 1             | `1d3516d2562c`  |
| 3012   | Layout 1             | `1d3516d2562c`  |
| 3002   | Layout 1             | `1d3516d2562c`  |
| 2995   | Layout 1             | `1d3516d2562c`  |
| 2987   | Layout 1             | `1d3516d2562c`  |
| 2978   | Layout 1             | `1d3516d2562c`  |
| 2970   | Layout 1             | `1d3516d2562c`  |
| 2959   | Layout 1             | `1d3516d2562c`  |
| 2951   | Layout 1             | `1d3516d2562c`  |
| 2942   | Layout 1             | `1d3516d2562c`  |
| 2935   | Layout 1             | `1d3516d2562c`  |
| 2932   | Layout 1             | `1d3516d2562c`  |
| 2923   | Layout 1             | `1d3516d2562c`  |
| 2919   | Layout 1             | `1d3516d2562c`  |
| 2907   | Layout 1             | `1d3516d2562c`  |
| 2900   | Layout 1             | `1d3516d2562c`  |
| 2891   | Layout 1             | `1d3516d2562c`  |
| 2882   | Layout 1             | `1d3516d2562c`  |
| 2872   | Layout 1             | `1d3516d2562c`  |
| 2863   | Layout 1             | `1d3516d2562c`  |
| 2855   | Layout 1             | `1d3516d2562c`  |
| 2849   | Layout 1             | `1d3516d2562c`  |
| 2844   | Layout 1             | `1d3516d2562c`  |
| 2834   | Layout 1             | `1d3516d2562c`  |
| 2825   | Layout 1             | `1d3516d2562c`  |
| 2819   | Layout 1             | `1d3516d2562c`  |
| 2811   | Layout 1             | `1d3516d2562c`  |
| 2803   | Layout 1             | `1d3516d2562c`  |
| 2794   | Layout 1             | `1d3516d2562c`  |
| 2783   | Layout 1             | `1d3516d2562c`  |
| 2774   | Layout 1             | `1d3516d2562c`  |
| 2765   | Layout 1             | `1d3516d2562c`  |
| 2756   | Layout 1             | `1d3516d2562c`  |
| 2750   | Layout 1             | `1d3516d2562c`  |
| 2743   | Layout 1             | `1d3516d2562c`  |
| 2736   | Layout 1             | `1d3516d2562c`  |
| 2726   | Layout 1             | `1d3516d2562c`  |
| 2717   | Layout 1             | `1d3516d2562c`  |
| 2709   | Layout 1             | `1d3516d2562c`  |
| 2703   | Layout 1             | `1d3516d2562c`  |
| 2695   | Layout 1             | `1d3516d2562c`  |
| 2684   | Layout 1             | `1d3516d2562c`  |
| 2672   | Layout 1             | `1d3516d2562c`  |
| 2665   | Layout 1             | `1d3516d2562c`  |
| 2657   | Layout 1             | `1d3516d2562c`  |
| 2649   | Layout 1             | `1d3516d2562c`  |
| 2644   | Layout 1             | `1d3516d2562c`  |
| 2637   | Layout 1             | `1d3516d2562c`  |
| 2629   | Layout 1             | `1d3516d2562c`  |
| 2619   | Layout 1             | `1d3516d2562c`  |
| 2612   | Layout 1             | `1d3516d2562c`  |
| 2606   | Layout 1             | `1d3516d2562c`  |
| 2602   | Layout 1             | `1d3516d2562c`  |
| 2601   | Layout 1             | `1d3516d2562c`  |
| 2592   | Layout 1             | `1d3516d2562c`  |
| 2583   | Layout 1             | `1d3516d2562c`  |
| 2575   | Layout 1             | `1d3516d2562c`  |
| 2567   | Layout 1             | `1d3516d2562c`  |
| 2560   | Layout 1             | `1d3516d2562c`  |
| 2553   | Layout 1             | `1d3516d2562c`  |
| 2545   | Layout 1             | `1d3516d2562c`  |
| 2538   | Layout 1             | `1d3516d2562c`  |
| 2529   | Layout 1             | `1d3516d2562c`  |
| 2519   | Layout 1             | `1d3516d2562c`  |
| 2513   | Layout 1             | `1d3516d2562c`  |
| 2510   | Layout 1             | `1d3516d2562c`  |
| 2507   | Layout 1             | `1d3516d2562c`  |
| 2503   | Layout 1             | `1d3516d2562c`  |
| 2498   | Layout 1             | `1d3516d2562c`  |
| 2492   | Layout 1             | `1d3516d2562c`  |
| 2487   | Layout 1             | `1d3516d2562c`  |
| 2480   | Layout 1             | `1d3516d2562c`  |
| 2474   | Layout 1             | `1d3516d2562c`  |
| 2468   | Layout 1             | `1d3516d2562c`  |
| 2460   | Layout 1             | `1d3516d2562c`  |
| 2453   | Layout 1             | `1d3516d2562c`  |
| 2444   | Layout 1             | `1d3516d2562c`  |
| 2438   | Layout 1             | `1d3516d2562c`  |
| 2434   | Layout 1             | `1d3516d2562c`  |
| 2429   | Layout 1             | `1d3516d2562c`  |
| 2421   | Layout 1             | `1d3516d2562c`  |
| 2414   | Layout 1             | `1d3516d2562c`  |
| 2407   | Layout 1             | `1d3516d2562c`  |
| 2401   | Layout 1             | `1d3516d2562c`  |
| 2397   | Layout 1             | `1d3516d2562c`  |
| 2393   | Layout 1             | `1d3516d2562c`  |
| 2384   | Layout 1             | `1d3516d2562c`  |
| 2378   | Layout 1             | `1d3516d2562c`  |
| 2372   | Layout 1             | `1d3516d2562c`  |
| 2358   | Layout 1             | `1d3516d2562c`  |
| 2352   | Layout 1             | `1d3516d2562c`  |
| 2347   | Layout 1             | `1d3516d2562c`  |
| 2343   | Layout 1             | `1d3516d2562c`  |
| 2335   | Layout 1             | `1d3516d2562c`  |
| 2327   | Layout 1             | `1d3516d2562c`  |
| 2324   | Layout 1             | `1d3516d2562c`  |
| 2319   | Layout 1             | `1d3516d2562c`  |
| 2313   | Layout 1             | `1d3516d2562c`  |
| 2308   | Layout 1             | `1d3516d2562c`  |
| 2302   | Layout 1             | `1d3516d2562c`  |
| 2295   | Layout 1             | `1d3516d2562c`  |
| 2290   | Layout 1             | `1d3516d2562c`  |
| 2284   | Layout 1             | `1d3516d2562c`  |
| 2276   | Layout 1             | `1d3516d2562c`  |
| 2269   | Layout 1             | `1d3516d2562c`  |
| 2259   | Layout 1             | `1d3516d2562c`  |
| 2250   | Layout 1             | `1d3516d2562c`  |
| 2243   | Layout 1             | `1d3516d2562c`  |
| 2235   | Layout 1             | `1d3516d2562c`  |
| 2229   | Layout 1             | `1d3516d2562c`  |
| 2224   | Layout 1             | `1d3516d2562c`  |
| 2218   | Layout 1             | `1d3516d2562c`  |
| 2215   | Layout 1             | `1d3516d2562c`  |
| 2207   | Layout 1             | `1d3516d2562c`  |
| 2203   | Layout 1             | `1d3516d2562c`  |
| 2196   | Layout 1             | `1d3516d2562c`  |
| 2192   | Layout 1             | `1d3516d2562c`  |
| 2189   | Layout 1             | `1d3516d2562c`  |
| 2183   | Layout 1             | `1d3516d2562c`  |
| 2179   | Layout 1             | `1d3516d2562c`  |
| 2171   | Layout 1             | `1d3516d2562c`  |
| 2163   | Layout 1             | `1d3516d2562c`  |
| 2156   | Layout 1             | `1d3516d2562c`  |
| 2151   | Layout 1             | `1d3516d2562c`  |
| 2147   | Layout 1             | `1d3516d2562c`  |
| 2142   | Layout 1             | `1d3516d2562c`  |
| 2138   | Layout 1             | `1d3516d2562c`  |
| 2134   | Layout 1             | `1d3516d2562c`  |
| 2130   | Layout 1             | `1d3516d2562c`  |
| 2122   | Layout 1             | `1d3516d2562c`  |
| 2107   | Layout 1             | `1d3516d2562c`  |
| 2098   | Layout 1             | `1d3516d2562c`  |
| 2089   | Layout 1             | `1d3516d2562c`  |
| 2081   | Layout 1             | `1d3516d2562c`  |
| 2073   | Layout 1             | `1d3516d2562c`  |
| 2067   | Layout 1             | `1d3516d2562c`  |
| 2063   | Layout 1             | `1d3516d2562c`  |
| 2059   | Layout 1             | `1d3516d2562c`  |
| 2052   | Layout 1             | `1d3516d2562c`  |
| 2044   | Layout 1             | `1d3516d2562c`  |
| 2039   | Layout 1             | `1d3516d2562c`  |
| 2032   | Layout 1             | `1d3516d2562c`  |
| 2025   | Layout 1             | `1d3516d2562c`  |
| 2011   | Layout 1             | `1d3516d2562c`  |
| 2005   | Layout 1             | `1d3516d2562c`  |
| 2000   | Layout 1             | `1d3516d2562c`  |
| 1996   | Layout 1             | `1d3516d2562c`  |
| 1991   | Layout 1             | `1d3516d2562c`  |
| 1985   | Layout 1             | `1d3516d2562c`  |
| 1980   | Layout 1             | `1d3516d2562c`  |
| 1969   | Layout 1             | `1d3516d2562c`  |
| 1964   | Layout 1             | `1d3516d2562c`  |
| 1958   | Layout 1             | `1d3516d2562c`  |
| 1950   | Layout 1             | `1d3516d2562c`  |
| 1945   | Layout 1             | `1d3516d2562c`  |
| 1937   | Layout 1             | `1d3516d2562c`  |
| 1933   | Layout 1             | `1d3516d2562c`  |
| 1927   | Layout 1             | `1d3516d2562c`  |
| 1921   | Layout 1             | `1d3516d2562c`  |
| 1914   | Layout 1             | `1d3516d2562c`  |
| 1908   | Layout 1             | `1d3516d2562c`  |
| 1897   | Layout 1             | `1d3516d2562c`  |
| 1892   | Layout 1             | `1d3516d2562c`  |
| 1886   | Layout 1             | `1d3516d2562c`  |
| 1881   | Layout 1             | `1d3516d2562c`  |
| 1871   | Layout 1             | `1d3516d2562c`  |
| 1866   | Layout 1             | `1d3516d2562c`  |
| 1862   | Layout 1             | `1d3516d2562c`  |
| 1854   | Layout 1             | `1d3516d2562c`  |
| 1846   | Layout 1             | `1d3516d2562c`  |
| 1838   | Layout 1             | `1d3516d2562c`  |
| 1832   | Layout 1             | `1d3516d2562c`  |
| 1826   | Layout 1             | `1d3516d2562c`  |
| 1822   | Layout 1             | `1d3516d2562c`  |
| 1818   | Layout 1             | `1d3516d2562c`  |
| 1804   | Layout 1             | `1d3516d2562c`  |
| 1794   | Layout 1             | `1d3516d2562c`  |
| 1790   | Layout 1             | `1d3516d2562c`  |
| 1784   | Layout 1             | `1d3516d2562c`  |
| 1774   | Layout 1             | `1d3516d2562c`  |
| 1771   | Layout 1             | `1d3516d2562c`  |
| 1762   | Layout 1             | `1d3516d2562c`  |
| 1759   | Layout 1             | `1d3516d2562c`  |
| 1754   | Layout 1             | `1d3516d2562c`  |
| 1749   | Layout 1             | `1d3516d2562c`  |
| 1743   | Layout 1             | `1d3516d2562c`  |
| 1737   | Layout 1             | `1d3516d2562c`  |
| 1731   | Layout 1             | `1d3516d2562c`  |
| 1725   | Layout 1             | `1d3516d2562c`  |
| 1717   | Layout 1             | `1d3516d2562c`  |
| 1710   | Layout 1             | `1d3516d2562c`  |
| 1704   | Layout 1             | `1d3516d2562c`  |
| 1698   | Layout 1             | `1d3516d2562c`  |
| 1690   | Layout 1             | `1d3516d2562c`  |
| 1685   | Layout 1             | `1d3516d2562c`  |
| 1680   | Layout 1             | `1d3516d2562c`  |
| 1674   | Layout 1             | `1d3516d2562c`  |
| 1668   | Layout 1             | `1d3516d2562c`  |
| 1659   | Layout 1             | `1d3516d2562c`  |
| 1649   | Layout 1             | `1d3516d2562c`  |
| 1642   | Layout 1             | `1d3516d2562c`  |
| 1636   | Layout 1             | `1d3516d2562c`  |
| 1628   | Layout 1             | `1d3516d2562c`  |
| 1622   | Layout 1             | `1d3516d2562c`  |
| 1614   | Layout 1             | `1d3516d2562c`  |
| 1608   | Layout 1             | `1d3516d2562c`  |
| 1602   | Layout 1             | `1d3516d2562c`  |
| 1598   | Layout 1             | `1d3516d2562c`  |
| 1594   | Layout 1             | `1d3516d2562c`  |
| 1590   | Layout 1             | `1d3516d2562c`  |
| 1587   | Layout 1             | `1d3516d2562c`  |
| 1584   | Layout 1             | `1d3516d2562c`  |
| 1579   | Layout 1             | `1d3516d2562c`  |
| 1572   | Layout 1             | `1d3516d2562c`  |
| 1565   | Layout 1             | `1d3516d2562c`  |
| 1559   | Layout 1             | `1d3516d2562c`  |
| 1554   | Layout 1             | `1d3516d2562c`  |
| 1547   | Layout 1             | `1d3516d2562c`  |
| 1537   | Layout 1             | `1d3516d2562c`  |
| 1529   | Layout 1             | `1d3516d2562c`  |
| 1524   | Layout 1             | `1d3516d2562c`  |
| 1519   | Layout 1             | `1d3516d2562c`  |
| 1509   | Layout 1             | `1d3516d2562c`  |
| 1506   | Layout 1             | `1d3516d2562c`  |
| 1504   | Layout 1             | `1d3516d2562c`  |
| 1500   | Layout 1             | `1d3516d2562c`  |
| 1493   | Layout 1             | `1d3516d2562c`  |
| 1489   | Layout 1             | `1d3516d2562c`  |
| 1485   | Layout 1             | `1d3516d2562c`  |
| 1481   | Layout 1             | `1d3516d2562c`  |
| 1474   | Layout 1             | `1d3516d2562c`  |
| 1466   | Layout 1             | `1d3516d2562c`  |
| 1462   | Layout 1             | `1d3516d2562c`  |
| 1459   | Layout 1             | `1d3516d2562c`  |
| 1453   | Layout 1             | `1d3516d2562c`  |
| 1450   | Layout 1             | `1d3516d2562c`  |
| 1445   | Layout 1             | `1d3516d2562c`  |
| 1439   | Layout 1             | `1d3516d2562c`  |
| 1433   | Layout 1             | `1d3516d2562c`  |
| 1430   | Layout 1             | `1d3516d2562c`  |
| 1426   | Layout 1             | `1d3516d2562c`  |
| 1421   | Layout 1             | `1d3516d2562c`  |
| 1417   | Layout 1             | `1d3516d2562c`  |
| 1416   | Layout 1             | `1d3516d2562c`  |
| 1409   | Layout 1             | `1d3516d2562c`  |
| 1405   | Layout 1             | `1d3516d2562c`  |
| 1401   | Layout 1             | `1d3516d2562c`  |
| 1396   | Layout 1             | `1d3516d2562c`  |
| 1391   | Layout 1             | `1d3516d2562c`  |
| 1390   | Layout 1             | `1d3516d2562c`  |
| 1386   | Layout 1             | `1d3516d2562c`  |
| 1381   | Layout 1             | `1d3516d2562c`  |
| 1379   | Layout 1             | `1d3516d2562c`  |
| 1372   | Layout 1             | `1d3516d2562c`  |
| 1366   | Layout 1             | `1d3516d2562c`  |
| 1364   | Layout 1             | `1d3516d2562c`  |
| 1363   | Layout 1             | `1d3516d2562c`  |
| 1360   | Layout 1             | `1d3516d2562c`  |
| 1358   | Layout 1             | `1d3516d2562c`  |
| 1355   | Layout 1             | `1d3516d2562c`  |
| 1351   | Layout 1             | `1d3516d2562c`  |
| 1348   | Layout 1             | `1d3516d2562c`  |
| 1346   | Layout 1             | `1d3516d2562c`  |
| 1341   | No documented layout | `1d3516d2562c`  |
| 1340   | No documented layout | `1d3516d2562c`  |
| 1338   | No documented layout | `1d3516d2562c`  |
| 1335   | No documented layout | `1d3516d2562c`  |
| 1333   | No documented layout | `1d3516d2562c`  |
| 1329   | No documented layout | `1d3516d2562c`  |
| 1327   | No documented layout | `1d3516d2562c`  |
| 1324   | No documented layout | `1d3516d2562c`  |
| 1321   | No documented layout | `1d3516d2562c`  |
| 1319   | No documented layout | `1d3516d2562c`  |
| 1318   | No documented layout | `1d3516d2562c`  |
| 1316   | No documented layout | `1d3516d2562c`  |
| 1313   | No documented layout | `1d3516d2562c`  |
| 1311   | No documented layout | `1d3516d2562c`  |
| 1309   | No documented layout | `1d3516d2562c`  |
| 1304   | No documented layout | `1d3516d2562c`  |
| 1292   | No documented layout | `1d3516d2562c`  |
| 1286   | No documented layout | `1d3516d2562c`  |
| 1280   | No file              | `1d3516d2562c`  |
| 1276   | No file              | `1d3516d2562c`  |
| 1267   | No file              | `1d3516d2562c`  |
| 1261   | No file              | `1d3516d2562c`  |
| 1256   | No file              | `1d3516d2562c`  |
| 1250   | No file              | `1d3516d2562c`  |
| 1246   | No file              | `1d3516d2562c`  |
| 1239   | No file              | `1d3516d2562c`  |
| 1230   | No file              | `1d3516d2562c`  |
| 1226   | No file              | `1d3516d2562c`  |
| 1220   | No file              | `1d3516d2562c`  |
| 1217   | No file              | `1d3516d2562c`  |
| 1211   | No file              | `1d3516d2562c`  |
| 1210   | No file              | `1d3516d2562c`  |
| 1208   | No file              | `1d3516d2562c`  |
| 1203   | No file              | `1d3516d2562c`  |
| 1197   | No file              | `1d3516d2562c`  |
| 1194   | No file              | `1d3516d2562c`  |
| 1192   | No file              | `1d3516d2562c`  |
| 1187   | No file              | `1d3516d2562c`  |
| 1183   | No file              | `1d3516d2562c`  |
| 1177   | No file              | `1d3516d2562c`  |
| 1173   | No file              | `1d3516d2562c`  |
| 1167   | No file              | `1d3516d2562c`  |
| 1164   | No file              | `1d3516d2562c`  |
| 1156   | No file              | `1d3516d2562c`  |
| 1149   | No file              | `1d3516d2562c`  |
| 1144   | No file              | `1d3516d2562c`  |
| 1137   | No file              | `1d3516d2562c`  |
| 1132   | No file              | `1d3516d2562c`  |
| 1127   | No file              | `1d3516d2562c`  |
| 1122   | No file              | `1d3516d2562c`  |
| 1118   | No file              | `1d3516d2562c`  |
| 1114   | No file              | `1d3516d2562c`  |
| 1109   | No file              | `1d3516d2562c`  |
| 1102   | No file              | `1d3516d2562c`  |
| 1096   | No file              | `1d3516d2562c`  |
| 1088   | No file              | `1d3516d2562c`  |
| 1081   | No file              | `1d3516d2562c`  |
| 1076   | No file              | `1d3516d2562c`  |
| 1069   | No file              | `1d3516d2562c`  |
| 1064   | No file              | `1d3516d2562c`  |
| 1058   | No file              | `1d3516d2562c`  |
| 1051   | No file              | `1d3516d2562c`  |
| 1044   | No file              | `1d3516d2562c`  |
| 1036   | No file              | `1d3516d2562c`  |
| 1026   | No file              | `1d3516d2562c`  |
| 1016   | No file              | `1d3516d2562c`  |
| 1009   | No file              | `1d3516d2562c`  |
| 1005   | No file              | `1d3516d2562c`  |
| 1000   | No file              | `1d3516d2562c`  |
| 998    | No file              | `1d3516d2562c`  |
| 990    | No file              | `1d3516d2562c`  |
| 979    | No file              | `1d3516d2562c`  |
| 972    | No file              | `1d3516d2562c`  |
| 963    | No file              | `1d3516d2562c`  |
| 955    | No file              | `1d3516d2562c`  |
| 946    | No file              | `1d3516d2562c`  |
| 938    | No file              | `1d3516d2562c`  |
| 927    | No file              | `1d3516d2562c`  |
| 911    | No file              | `1d3516d2562c`  |
| 904    | No file              | `1d3516d2562c`  |
| 899    | No file              | `1d3516d2562c`  |
| 894    | No file              | `1d3516d2562c`  |
| 885    | No file              | `1d3516d2562c`  |
| 879    | No file              | `1d3516d2562c`  |
| 872    | No file              | `1d3516d2562c`  |
| 864    | No file              | `1d3516d2562c`  |
| 855    | No file              | `1d3516d2562c`  |
| 853    | No file              | `1d3516d2562c`  |
| 845    | No file              | `1d3516d2562c`  |
| 837    | No file              | `1d3516d2562c`  |
| 829    | No file              | `1d3516d2562c`  |
| 822    | No file              | `1d3516d2562c`  |
| 814    | No file              | `1d3516d2562c`  |
| 805    | No file              | `1d3516d2562c`  |
| 794    | No file              | `1d3516d2562c`  |
| 787    | No file              | `1d3516d2562c`  |
| 780    | No file              | `1d3516d2562c`  |
| 771    | No file              | `1d3516d2562c`  |
| 760    | No file              | `1d3516d2562c`  |
| 748    | No file              | `1d3516d2562c`  |
| 741    | No file              | `1d3516d2562c`  |
| 736    | No file              | `1d3516d2562c`  |
| 731    | No file              | `1d3516d2562c`  |
| 723    | No file              | `1d3516d2562c`  |
| 711    | No file              | `1d3516d2562c`  |
| 707    | No file              | `1d3516d2562c`  |
| 697    | No file              | `1d3516d2562c`  |
| 689    | No file              | `1d3516d2562c`  |
| 683    | No file              | `1d3516d2562c`  |
| 678    | No file              | `1d3516d2562c`  |
| 670    | No file              | `1d3516d2562c`  |
| 661    | No file              | `1d3516d2562c`  |
| 656    | No file              | `1d3516d2562c`  |
| 652    | No file              | `1d3516d2562c`  |
| 643    | No file              | `1d3516d2562c`  |
| 637    | No file              | `1d3516d2562c`  |
| 630    | No file              | `1d3516d2562c`  |
| 627    | No file              | `1d3516d2562c`  |
| 621    | No file              | `1d3516d2562c`  |
| 617    | No file              | `1d3516d2562c`  |
| 615    | No file              | `1d3516d2562c`  |
| 606    | No file              | `1d3516d2562c`  |
| 599    | No file              | `1d3516d2562c`  |
| 592    | No file              | `1d3516d2562c`  |
| 586    | No file              | `1d3516d2562c`  |
| 577    | No file              | `1d3516d2562c`  |
| 569    | No file              | `1d3516d2562c`  |
| 561    | No file              | `1d3516d2562c`  |
| 554    | No file              | `1d3516d2562c`  |
| 542    | No file              | `1d3516d2562c`  |
| 532    | No file              | `1d3516d2562c`  |
| 531    | No file              | `1d3516d2562c`  |
| 526    | No file              | `1d3516d2562c`  |
| 521    | No file              | `1d3516d2562c`  |
| 517    | No file              | `1d3516d2562c`  |
| 510    | No file              | `1d3516d2562c`  |
| 508    | No file              | `1d3516d2562c`  |
| 504    | No file              | `1d3516d2562c`  |
| 497    | No file              | `1d3516d2562c`  |
| 491    | No file              | `1d3516d2562c`  |
| 485    | No file              | `1d3516d2562c`  |
| 478    | No file              | `1d3516d2562c`  |
| 472    | No file              | `1d3516d2562c`  |
| 466    | No file              | `1d3516d2562c`  |
| 457    | No file              | `1d3516d2562c`  |
| 452    | No file              | `1d3516d2562c`  |
| 449    | No file              | `1d3516d2562c`  |
| 435    | No file              | `1d3516d2562c`  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                        |
| ------------------------------ | -------- | ----------------------------------------------------------- |
| `knowledgelearningoffset.dbss` | Required | Provides source ID, byte offset and size for each record    |
| `knowledgelearningcharacterkey.bss` | Optional | Table 0 grouped by card: each card with the characters that teach it ([doc](knowledgelearningcharacterkey_bss.md)) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The two tables follow each other; the file holds no table count of its own.

| Offset  | Type              | Field  | Notes                                                   |
| ------- | ----------------- | ------ | ------------------------------------------------------- |
| `+0x00` | Learning Table[2] | tables | Table 0 (characters), then table 1 (items); the offset file's `table_count` is `2` |

The index `data_offset` points past the lead, at the record itself. Table 0 starts at `0` and its records end at `44136` (`43065` in the pre-2026-09-27 fixture); table 1 starts there with its own count.

### Learning Table (variable: 4 bytes + entries)

| Offset  | Type                  | Field   | Notes                             |
| ------- | --------------------- | ------- | --------------------------------- |
| `+0x00` | u32                   | count   | Matches the index table's `count` |
| `+0x04` | Learning Entry[count] | entries | See Learning Entry                |

### Learning Entry (17 bytes)

| Offset  | Type            | Field      | Notes                                                          |
| ------- | --------------- | ---------- | -------------------------------------------------------------- |
| `+0x00` | u32             | key_prefix | Lead `source_id`, equal to the record's `source_id`            |
| `+0x04` | Learning Record | record     | See Learning Record; the index `data_offset` points here       |

### Learning Record (13 bytes)

| Offset  | Type | Field       | Notes                                                                  |
| ------- | ---- | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | source_id   | Character ID (table 0, LOC `str_type=6`) or item ID (table 1, LOC `str_type=0`) |
| `+0x04` | u32  | source_type | `0` in table 0, `1` in table 1                                         |
| `+0x08` | u8   | unknown_08  | Always `0`                                                             |
| `+0x09` | u32  | card_id     | Knowledge card taught; LOC `str_type=34`, key of `mentalcard.dbss`     |

### `knowledgelearningoffset.dbss`

No `PABR` magic and no trailer; the file ends exactly after the last table.

| Offset  | Type                     | Field       | Notes                                    |
| ------- | ------------------------ | ----------- | ---------------------------------------- |
| `+0x00` | u32                      | table_count | Observed `2`                             |
| `+0x04` | Index Table[table_count] | tables      | See Index Table                          |

### Index Table (variable: 4 bytes + rows)

| Offset  | Type             | Field | Notes                                         |
| ------- | ---------------- | ----- | --------------------------------------------- |
| `+0x00` | u32              | count | Rows in this table: `2596` and `2088` in the 2026-09-27 client, `2533` and `2070` in the pre-2026-09-27 fixture |
| `+0x04` | Index Row[count] | rows  | See Index Row                                 |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | source_id   | Equals `source_id` at the start of the record            |
| `+0x04` | u32  | data_offset | Absolute offset of the record in `knowledgelearning.dbss` |
| `+0x08` | u32  | size        | Record size in bytes; always `13`                        |

## Enum Values

### `source_type`

| Value | Meaning   | Rows  | Evidence                                                        |
| ----- | --------- | ----- | --------------------------------------------------------------- |
| 0     | Character | 2,596 | All 2,596 `source_id` values have an LOC `str_type=6` name      |
| 1     | Item      | 2,088 | All 2,088 `source_id` values have an LOC `str_type=0` name      |

## Confirmed Examples

| Table | source_id | Source name (LOC)       | card_id | Card name (LOC)          |
| ----- | --------- | ----------------------- | ------- | ------------------------ |
| 0     | `10004`   | Feldspar (str_type=6)   | `7302`  | Feldspar                 |
| 0     | `21207`   | Valencian Lion          | `4893`  | Valencian Lion           |
| 0     | `10480`   | Pistachio Tree          | `7836`  | Pistachio                |
| 1     | `8279`    | Gurnard (str_type=0)    | `8579`  | Gurnard                  |
| 1     | `9728`    | Blue Whale Molar        | `7765`  | Blue Whale Tooth         |

## Notes

- Every `card_id` in both tables is a `mentalcard.dbss` card.
- The app groups table 0 by card into the `KNOWLEDGE_LEARNING_CHARACTERS` lookup index and table 1 into `KNOWLEDGE_LEARNING_ITEMS`. The `mentalcard.dbss` Learned From and Learned From Items columns read them.
- The Source Name column shows the name in the user's LOC language, else the Korean `characterstatic.dbss` name (table 0, `character_name()`) or `itemenchant.dbss` name (table 1, `item_name()`): `4070` shows `가공석탄` without LOC.
- The source name equals the card name on 2,504 of 2,596 character rows and 2,003 of 2,088 item rows. The rest are close variants (`Pistachio Tree` teaches `Pistachio`, several Magic Crystals teach `Low Grade Crystal Fusion`).
- Table 0 teaches 1,458 distinct cards, so several characters can teach one card (for example boss variants). Table 1 teaches 2,045 distinct cards.
- `source_id` is unique within each table. Read it with the right LOC type: in table 0, `10004` is the character Feldspar, while item `10004` is `Raell Longsword`.
- The earlier reading of this file skipped a 12-byte header and read rows as `offset, kind, idx_id`. That shifts every row by one field: `kind` was the record size (`13`) and `idx_id` was the next row's `source_id`. It also misreads table 1, whose rows start 4 bytes after table 0's last row.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) describes `knowledgelearning` as card-to-card learning prerequisites. Our files do not support that: `source_id` resolves as a character or item on every row, and only 272 of 2,596 character IDs are also card IDs.
- `knowledgelearningcharacterkey.bss` holds the same pairs as table 0, grouped by card in table 0 row order; see [its doc](knowledgelearningcharacterkey_bss.md). Table 1 has no such file.

## Open Questions

### Other Source Types

Only `source_type` 0 and 1 occur, one per table. It is not known whether the client supports other sources (quests, regions) through a third table.
