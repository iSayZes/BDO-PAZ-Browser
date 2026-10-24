# `newquest.bss` Format

## Purpose

Defines the new-quest (event) list: quest IDs grouped under events such as `[Event] Mastering Life Skills`, each group with an event period, and per quest a condition line, a visible condition and a hide condition. 232 groups and 1,281 quest references on client 3458. All text sits in a string table at the end of the file (Korean group names, Korean condition lines, scripts, dates); LOC type 58 holds the English names and condition lines.

[`mainquest.bss`](mainquest_bss.md), [`recommendationquest.bss`](recommendationquest_bss.md) and [`repetitionquest.bss`](repetitionquest_bss.md) share this layout, each with its own LOC type; one handler reads all four. This doc is the layout reference for all four.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File           | Bytes   | Records                              | Row bytes |
| ------ | -------------- | ------- | -------------- | ------- | ------------------------------------ | --------- |
| 1      | 1304 and later | 3483    | `newquest.bss` | 790,158 | 1,237 Quest Reference Row, 229 Group | 17        |

| Layout | File           | Known             | Unknown      |
| ------ | -------------- | ----------------- | ------------ |
| 1      | `newquest.bss` | 789,242 B (99.9%) | 916 B (0.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `d4d4b0abe240`  |
| 3482   | Layout 1             | `d4d4b0abe240`  |
| 3474   | Layout 1             | `d4d4b0abe240`  |
| 3473   | Layout 1             | `d4d4b0abe240`  |
| 3464   | Layout 1             | `d4d4b0abe240`  |
| 3458   | Layout 1             | `d4d4b0abe240`  |
| 3454   | Layout 1             | `d4d4b0abe240`  |
| 3444   | Layout 1             | `d4d4b0abe240`  |
| 3435   | Layout 1             | `d4d4b0abe240`  |
| 3426   | Layout 1             | `d4d4b0abe240`  |
| 3418   | Layout 1             | `d4d4b0abe240`  |
| 3412   | Layout 1             | `d4d4b0abe240`  |
| 3402   | Layout 1             | `d4d4b0abe240`  |
| 3396   | Layout 1             | `d4d4b0abe240`  |
| 3387   | Layout 1             | `d4d4b0abe240`  |
| 3381   | Layout 1             | `d4d4b0abe240`  |
| 3373   | Layout 1             | `d4d4b0abe240`  |
| 3364   | Layout 1             | `d4d4b0abe240`  |
| 3356   | Layout 1             | `d4d4b0abe240`  |
| 3349   | Layout 1             | `d4d4b0abe240`  |
| 3342   | Layout 1             | `d4d4b0abe240`  |
| 3335   | Layout 1             | `d4d4b0abe240`  |
| 3326   | Layout 1             | `d4d4b0abe240`  |
| 3321   | Layout 1             | `d4d4b0abe240`  |
| 3314   | Layout 1             | `d4d4b0abe240`  |
| 3303   | Layout 1             | `d4d4b0abe240`  |
| 3302   | Layout 1             | `d4d4b0abe240`  |
| 3293   | Layout 1             | `d4d4b0abe240`  |
| 3283   | Layout 1             | `d4d4b0abe240`  |
| 3275   | Layout 1             | `d4d4b0abe240`  |
| 3267   | Layout 1             | `d4d4b0abe240`  |
| 3258   | Layout 1             | `d4d4b0abe240`  |
| 3251   | Layout 1             | `d4d4b0abe240`  |
| 3242   | Layout 1             | `d4d4b0abe240`  |
| 3235   | Layout 1             | `d4d4b0abe240`  |
| 3229   | Layout 1             | `d4d4b0abe240`  |
| 3212   | Layout 1             | `d4d4b0abe240`  |
| 3203   | Layout 1             | `d4d4b0abe240`  |
| 3193   | Layout 1             | `d4d4b0abe240`  |
| 3186   | Layout 1             | `d4d4b0abe240`  |
| 3177   | Layout 1             | `d4d4b0abe240`  |
| 3169   | Layout 1             | `d4d4b0abe240`  |
| 3158   | Layout 1             | `d4d4b0abe240`  |
| 3151   | Layout 1             | `d4d4b0abe240`  |
| 3144   | Layout 1             | `d4d4b0abe240`  |
| 3133   | Layout 1             | `d4d4b0abe240`  |
| 3125   | Layout 1             | `d4d4b0abe240`  |
| 3118   | Layout 1             | `d4d4b0abe240`  |
| 3111   | Layout 1             | `d4d4b0abe240`  |
| 3103   | Layout 1             | `d4d4b0abe240`  |
| 3095   | Layout 1             | `d4d4b0abe240`  |
| 3086   | Layout 1             | `d4d4b0abe240`  |
| 3072   | Layout 1             | `d4d4b0abe240`  |
| 3062   | Layout 1             | `d4d4b0abe240`  |
| 3052   | Layout 1             | `d4d4b0abe240`  |
| 3045   | Layout 1             | `d4d4b0abe240`  |
| 3037   | Layout 1             | `d4d4b0abe240`  |
| 3030   | Layout 1             | `d4d4b0abe240`  |
| 3021   | Layout 1             | `d4d4b0abe240`  |
| 3012   | Layout 1             | `d4d4b0abe240`  |
| 3002   | Layout 1             | `d4d4b0abe240`  |
| 2995   | Layout 1             | `d4d4b0abe240`  |
| 2987   | Layout 1             | `d4d4b0abe240`  |
| 2978   | Layout 1             | `d4d4b0abe240`  |
| 2970   | Layout 1             | `d4d4b0abe240`  |
| 2959   | Layout 1             | `d4d4b0abe240`  |
| 2951   | Layout 1             | `d4d4b0abe240`  |
| 2942   | Layout 1             | `d4d4b0abe240`  |
| 2935   | Layout 1             | `d4d4b0abe240`  |
| 2932   | Layout 1             | `d4d4b0abe240`  |
| 2923   | Layout 1             | `d4d4b0abe240`  |
| 2919   | Layout 1             | `d4d4b0abe240`  |
| 2907   | Layout 1             | `d4d4b0abe240`  |
| 2900   | Layout 1             | `d4d4b0abe240`  |
| 2891   | Layout 1             | `d4d4b0abe240`  |
| 2882   | Layout 1             | `d4d4b0abe240`  |
| 2872   | Layout 1             | `d4d4b0abe240`  |
| 2863   | Layout 1             | `d4d4b0abe240`  |
| 2855   | Layout 1             | `d4d4b0abe240`  |
| 2849   | Layout 1             | `d4d4b0abe240`  |
| 2844   | Layout 1             | `d4d4b0abe240`  |
| 2834   | Layout 1             | `d4d4b0abe240`  |
| 2825   | Layout 1             | `d4d4b0abe240`  |
| 2819   | Layout 1             | `d4d4b0abe240`  |
| 2811   | Layout 1             | `d4d4b0abe240`  |
| 2803   | Layout 1             | `d4d4b0abe240`  |
| 2794   | Layout 1             | `d4d4b0abe240`  |
| 2783   | Layout 1             | `d4d4b0abe240`  |
| 2774   | Layout 1             | `d4d4b0abe240`  |
| 2765   | Layout 1             | `d4d4b0abe240`  |
| 2756   | Layout 1             | `d4d4b0abe240`  |
| 2750   | Layout 1             | `d4d4b0abe240`  |
| 2743   | Layout 1             | `d4d4b0abe240`  |
| 2736   | Layout 1             | `d4d4b0abe240`  |
| 2726   | Layout 1             | `d4d4b0abe240`  |
| 2717   | Layout 1             | `d4d4b0abe240`  |
| 2709   | Layout 1             | `d4d4b0abe240`  |
| 2703   | Layout 1             | `d4d4b0abe240`  |
| 2695   | Layout 1             | `d4d4b0abe240`  |
| 2684   | Layout 1             | `d4d4b0abe240`  |
| 2672   | Layout 1             | `d4d4b0abe240`  |
| 2665   | Layout 1             | `d4d4b0abe240`  |
| 2657   | Layout 1             | `d4d4b0abe240`  |
| 2649   | Layout 1             | `d4d4b0abe240`  |
| 2644   | Layout 1             | `d4d4b0abe240`  |
| 2637   | Layout 1             | `d4d4b0abe240`  |
| 2629   | Layout 1             | `d4d4b0abe240`  |
| 2619   | Layout 1             | `d4d4b0abe240`  |
| 2612   | Layout 1             | `d4d4b0abe240`  |
| 2606   | Layout 1             | `d4d4b0abe240`  |
| 2602   | Layout 1             | `d4d4b0abe240`  |
| 2601   | Layout 1             | `d4d4b0abe240`  |
| 2592   | Layout 1             | `d4d4b0abe240`  |
| 2583   | Layout 1             | `d4d4b0abe240`  |
| 2575   | Layout 1             | `d4d4b0abe240`  |
| 2567   | Layout 1             | `d4d4b0abe240`  |
| 2560   | Layout 1             | `d4d4b0abe240`  |
| 2553   | Layout 1             | `d4d4b0abe240`  |
| 2545   | Layout 1             | `d4d4b0abe240`  |
| 2538   | Layout 1             | `d4d4b0abe240`  |
| 2529   | Layout 1             | `d4d4b0abe240`  |
| 2519   | Layout 1             | `d4d4b0abe240`  |
| 2513   | Layout 1             | `d4d4b0abe240`  |
| 2510   | Layout 1             | `d4d4b0abe240`  |
| 2507   | Layout 1             | `d4d4b0abe240`  |
| 2503   | Layout 1             | `d4d4b0abe240`  |
| 2498   | Layout 1             | `d4d4b0abe240`  |
| 2492   | Layout 1             | `d4d4b0abe240`  |
| 2487   | Layout 1             | `d4d4b0abe240`  |
| 2480   | Layout 1             | `d4d4b0abe240`  |
| 2474   | Layout 1             | `d4d4b0abe240`  |
| 2468   | Layout 1             | `d4d4b0abe240`  |
| 2460   | Layout 1             | `d4d4b0abe240`  |
| 2453   | Layout 1             | `d4d4b0abe240`  |
| 2444   | Layout 1             | `d4d4b0abe240`  |
| 2438   | Layout 1             | `d4d4b0abe240`  |
| 2434   | Layout 1             | `d4d4b0abe240`  |
| 2429   | Layout 1             | `d4d4b0abe240`  |
| 2421   | Layout 1             | `d4d4b0abe240`  |
| 2414   | Layout 1             | `d4d4b0abe240`  |
| 2407   | Layout 1             | `d4d4b0abe240`  |
| 2401   | Layout 1             | `d4d4b0abe240`  |
| 2397   | Layout 1             | `d4d4b0abe240`  |
| 2393   | Layout 1             | `d4d4b0abe240`  |
| 2384   | Layout 1             | `d4d4b0abe240`  |
| 2378   | Layout 1             | `d4d4b0abe240`  |
| 2372   | Layout 1             | `d4d4b0abe240`  |
| 2358   | Layout 1             | `d4d4b0abe240`  |
| 2352   | Layout 1             | `d4d4b0abe240`  |
| 2347   | Layout 1             | `d4d4b0abe240`  |
| 2343   | Layout 1             | `d4d4b0abe240`  |
| 2335   | Layout 1             | `d4d4b0abe240`  |
| 2327   | Layout 1             | `d4d4b0abe240`  |
| 2324   | Layout 1             | `d4d4b0abe240`  |
| 2319   | Layout 1             | `d4d4b0abe240`  |
| 2313   | Layout 1             | `d4d4b0abe240`  |
| 2308   | Layout 1             | `d4d4b0abe240`  |
| 2302   | Layout 1             | `d4d4b0abe240`  |
| 2295   | Layout 1             | `d4d4b0abe240`  |
| 2290   | Layout 1             | `d4d4b0abe240`  |
| 2284   | Layout 1             | `d4d4b0abe240`  |
| 2276   | Layout 1             | `d4d4b0abe240`  |
| 2269   | Layout 1             | `d4d4b0abe240`  |
| 2259   | Layout 1             | `d4d4b0abe240`  |
| 2250   | Layout 1             | `d4d4b0abe240`  |
| 2243   | Layout 1             | `d4d4b0abe240`  |
| 2235   | Layout 1             | `d4d4b0abe240`  |
| 2229   | Layout 1             | `d4d4b0abe240`  |
| 2224   | Layout 1             | `d4d4b0abe240`  |
| 2218   | Layout 1             | `d4d4b0abe240`  |
| 2215   | Layout 1             | `d4d4b0abe240`  |
| 2207   | Layout 1             | `d4d4b0abe240`  |
| 2203   | Layout 1             | `d4d4b0abe240`  |
| 2196   | Layout 1             | `d4d4b0abe240`  |
| 2192   | Layout 1             | `d4d4b0abe240`  |
| 2189   | Layout 1             | `d4d4b0abe240`  |
| 2183   | Layout 1             | `d4d4b0abe240`  |
| 2179   | Layout 1             | `d4d4b0abe240`  |
| 2171   | Layout 1             | `d4d4b0abe240`  |
| 2163   | Layout 1             | `d4d4b0abe240`  |
| 2156   | Layout 1             | `d4d4b0abe240`  |
| 2151   | Layout 1             | `d4d4b0abe240`  |
| 2147   | Layout 1             | `d4d4b0abe240`  |
| 2142   | Layout 1             | `d4d4b0abe240`  |
| 2138   | Layout 1             | `d4d4b0abe240`  |
| 2134   | Layout 1             | `d4d4b0abe240`  |
| 2130   | Layout 1             | `d4d4b0abe240`  |
| 2122   | Layout 1             | `d4d4b0abe240`  |
| 2107   | Layout 1             | `d4d4b0abe240`  |
| 2098   | Layout 1             | `d4d4b0abe240`  |
| 2089   | Layout 1             | `d4d4b0abe240`  |
| 2081   | Layout 1             | `d4d4b0abe240`  |
| 2073   | Layout 1             | `d4d4b0abe240`  |
| 2067   | Layout 1             | `d4d4b0abe240`  |
| 2063   | Layout 1             | `d4d4b0abe240`  |
| 2059   | Layout 1             | `d4d4b0abe240`  |
| 2052   | Layout 1             | `d4d4b0abe240`  |
| 2044   | Layout 1             | `d4d4b0abe240`  |
| 2039   | Layout 1             | `d4d4b0abe240`  |
| 2032   | Layout 1             | `d4d4b0abe240`  |
| 2025   | Layout 1             | `d4d4b0abe240`  |
| 2011   | Layout 1             | `d4d4b0abe240`  |
| 2005   | Layout 1             | `d4d4b0abe240`  |
| 2000   | Layout 1             | `d4d4b0abe240`  |
| 1996   | Layout 1             | `d4d4b0abe240`  |
| 1991   | Layout 1             | `d4d4b0abe240`  |
| 1985   | Layout 1             | `d4d4b0abe240`  |
| 1980   | Layout 1             | `d4d4b0abe240`  |
| 1969   | Layout 1             | `d4d4b0abe240`  |
| 1964   | Layout 1             | `d4d4b0abe240`  |
| 1958   | Layout 1             | `d4d4b0abe240`  |
| 1950   | Layout 1             | `d4d4b0abe240`  |
| 1945   | Layout 1             | `d4d4b0abe240`  |
| 1937   | Layout 1             | `d4d4b0abe240`  |
| 1933   | Layout 1             | `d4d4b0abe240`  |
| 1927   | Layout 1             | `d4d4b0abe240`  |
| 1921   | Layout 1             | `d4d4b0abe240`  |
| 1914   | Layout 1             | `d4d4b0abe240`  |
| 1908   | Layout 1             | `d4d4b0abe240`  |
| 1897   | Layout 1             | `d4d4b0abe240`  |
| 1892   | Layout 1             | `d4d4b0abe240`  |
| 1886   | Layout 1             | `d4d4b0abe240`  |
| 1881   | Layout 1             | `d4d4b0abe240`  |
| 1871   | Layout 1             | `d4d4b0abe240`  |
| 1866   | Layout 1             | `d4d4b0abe240`  |
| 1862   | Layout 1             | `d4d4b0abe240`  |
| 1854   | Layout 1             | `d4d4b0abe240`  |
| 1846   | Layout 1             | `d4d4b0abe240`  |
| 1838   | Layout 1             | `d4d4b0abe240`  |
| 1832   | Layout 1             | `d4d4b0abe240`  |
| 1826   | Layout 1             | `d4d4b0abe240`  |
| 1822   | Layout 1             | `d4d4b0abe240`  |
| 1818   | Layout 1             | `d4d4b0abe240`  |
| 1804   | Layout 1             | `d4d4b0abe240`  |
| 1794   | Layout 1             | `d4d4b0abe240`  |
| 1790   | Layout 1             | `d4d4b0abe240`  |
| 1784   | Layout 1             | `d4d4b0abe240`  |
| 1774   | Layout 1             | `d4d4b0abe240`  |
| 1771   | Layout 1             | `d4d4b0abe240`  |
| 1762   | Layout 1             | `d4d4b0abe240`  |
| 1759   | Layout 1             | `d4d4b0abe240`  |
| 1754   | Layout 1             | `d4d4b0abe240`  |
| 1749   | Layout 1             | `d4d4b0abe240`  |
| 1743   | Layout 1             | `d4d4b0abe240`  |
| 1737   | Layout 1             | `d4d4b0abe240`  |
| 1731   | Layout 1             | `d4d4b0abe240`  |
| 1725   | Layout 1             | `d4d4b0abe240`  |
| 1717   | Layout 1             | `d4d4b0abe240`  |
| 1710   | Layout 1             | `d4d4b0abe240`  |
| 1704   | Layout 1             | `d4d4b0abe240`  |
| 1698   | Layout 1             | `d4d4b0abe240`  |
| 1690   | Layout 1             | `d4d4b0abe240`  |
| 1685   | Layout 1             | `d4d4b0abe240`  |
| 1680   | Layout 1             | `d4d4b0abe240`  |
| 1674   | Layout 1             | `d4d4b0abe240`  |
| 1668   | Layout 1             | `d4d4b0abe240`  |
| 1659   | Layout 1             | `d4d4b0abe240`  |
| 1649   | Layout 1             | `d4d4b0abe240`  |
| 1642   | Layout 1             | `d4d4b0abe240`  |
| 1636   | Layout 1             | `d4d4b0abe240`  |
| 1628   | Layout 1             | `d4d4b0abe240`  |
| 1622   | Layout 1             | `d4d4b0abe240`  |
| 1614   | Layout 1             | `d4d4b0abe240`  |
| 1608   | Layout 1             | `d4d4b0abe240`  |
| 1602   | Layout 1             | `d4d4b0abe240`  |
| 1598   | Layout 1             | `d4d4b0abe240`  |
| 1594   | Layout 1             | `d4d4b0abe240`  |
| 1590   | Layout 1             | `d4d4b0abe240`  |
| 1587   | Layout 1             | `d4d4b0abe240`  |
| 1584   | Layout 1             | `d4d4b0abe240`  |
| 1579   | Layout 1             | `d4d4b0abe240`  |
| 1572   | Layout 1             | `d4d4b0abe240`  |
| 1565   | Layout 1             | `d4d4b0abe240`  |
| 1559   | Layout 1             | `d4d4b0abe240`  |
| 1554   | Layout 1             | `d4d4b0abe240`  |
| 1547   | Layout 1             | `d4d4b0abe240`  |
| 1537   | Layout 1             | `d4d4b0abe240`  |
| 1529   | Layout 1             | `d4d4b0abe240`  |
| 1524   | Layout 1             | `d4d4b0abe240`  |
| 1519   | Layout 1             | `d4d4b0abe240`  |
| 1509   | Layout 1             | `d4d4b0abe240`  |
| 1506   | Layout 1             | `d4d4b0abe240`  |
| 1504   | Layout 1             | `d4d4b0abe240`  |
| 1500   | Layout 1             | `d4d4b0abe240`  |
| 1493   | Layout 1             | `d4d4b0abe240`  |
| 1489   | Layout 1             | `d4d4b0abe240`  |
| 1485   | Layout 1             | `d4d4b0abe240`  |
| 1481   | Layout 1             | `d4d4b0abe240`  |
| 1474   | Layout 1             | `d4d4b0abe240`  |
| 1466   | Layout 1             | `d4d4b0abe240`  |
| 1462   | Layout 1             | `d4d4b0abe240`  |
| 1459   | Layout 1             | `d4d4b0abe240`  |
| 1453   | Layout 1             | `d4d4b0abe240`  |
| 1450   | Layout 1             | `d4d4b0abe240`  |
| 1445   | Layout 1             | `d4d4b0abe240`  |
| 1439   | Layout 1             | `d4d4b0abe240`  |
| 1433   | Layout 1             | `d4d4b0abe240`  |
| 1430   | Layout 1             | `d4d4b0abe240`  |
| 1426   | Layout 1             | `d4d4b0abe240`  |
| 1421   | Layout 1             | `d4d4b0abe240`  |
| 1417   | Layout 1             | `d4d4b0abe240`  |
| 1416   | Layout 1             | `d4d4b0abe240`  |
| 1409   | Layout 1             | `d4d4b0abe240`  |
| 1405   | Layout 1             | `d4d4b0abe240`  |
| 1401   | Layout 1             | `d4d4b0abe240`  |
| 1396   | Layout 1             | `d4d4b0abe240`  |
| 1391   | Layout 1             | `d4d4b0abe240`  |
| 1390   | Layout 1             | `d4d4b0abe240`  |
| 1386   | Layout 1             | `d4d4b0abe240`  |
| 1381   | Layout 1             | `d4d4b0abe240`  |
| 1379   | Layout 1             | `d4d4b0abe240`  |
| 1372   | Layout 1             | `d4d4b0abe240`  |
| 1366   | Layout 1             | `d4d4b0abe240`  |
| 1364   | Layout 1             | `d4d4b0abe240`  |
| 1363   | Layout 1             | `d4d4b0abe240`  |
| 1360   | Layout 1             | `d4d4b0abe240`  |
| 1358   | Layout 1             | `d4d4b0abe240`  |
| 1355   | Layout 1             | `d4d4b0abe240`  |
| 1351   | Layout 1             | `d4d4b0abe240`  |
| 1348   | Layout 1             | `d4d4b0abe240`  |
| 1346   | Layout 1             | `d4d4b0abe240`  |
| 1341   | Layout 1             | `d4d4b0abe240`  |
| 1340   | Layout 1             | `d4d4b0abe240`  |
| 1338   | Layout 1             | `d4d4b0abe240`  |
| 1335   | Layout 1             | `d4d4b0abe240`  |
| 1333   | Layout 1             | `d4d4b0abe240`  |
| 1329   | Layout 1             | `d4d4b0abe240`  |
| 1327   | Layout 1             | `d4d4b0abe240`  |
| 1324   | Layout 1             | `d4d4b0abe240`  |
| 1321   | Layout 1             | `d4d4b0abe240`  |
| 1319   | Layout 1             | `d4d4b0abe240`  |
| 1318   | Layout 1             | `d4d4b0abe240`  |
| 1316   | Layout 1             | `d4d4b0abe240`  |
| 1313   | Layout 1             | `d4d4b0abe240`  |
| 1311   | Layout 1             | `d4d4b0abe240`  |
| 1309   | Layout 1             | `d4d4b0abe240`  |
| 1304   | Layout 1             | `d4d4b0abe240`  |
| 1292   | No documented layout | `d4d4b0abe240`  |
| 1286   | No documented layout | `d4d4b0abe240`  |
| 1280   | No documented layout | `d4d4b0abe240`  |
| 1276   | No documented layout | `d4d4b0abe240`  |
| 1267   | No documented layout | `d4d4b0abe240`  |
| 1261   | No documented layout | `d4d4b0abe240`  |
| 1256   | No documented layout | `d4d4b0abe240`  |
| 1250   | No documented layout | `d4d4b0abe240`  |
| 1246   | No file              | `d4d4b0abe240`  |
| 1239   | No file              | `d4d4b0abe240`  |
| 1230   | No file              | `d4d4b0abe240`  |
| 1226   | No file              | `d4d4b0abe240`  |
| 1220   | No file              | `d4d4b0abe240`  |
| 1217   | No file              | `d4d4b0abe240`  |
| 1211   | No file              | `d4d4b0abe240`  |
| 1210   | No file              | `d4d4b0abe240`  |
| 1208   | No file              | `d4d4b0abe240`  |
| 1203   | No file              | `d4d4b0abe240`  |
| 1197   | No file              | `d4d4b0abe240`  |
| 1194   | No file              | `d4d4b0abe240`  |
| 1192   | No file              | `d4d4b0abe240`  |
| 1187   | No file              | `d4d4b0abe240`  |
| 1183   | No file              | `d4d4b0abe240`  |
| 1177   | No file              | `d4d4b0abe240`  |
| 1173   | No file              | `d4d4b0abe240`  |
| 1167   | No file              | `d4d4b0abe240`  |
| 1164   | No file              | `d4d4b0abe240`  |
| 1156   | No file              | `d4d4b0abe240`  |
| 1149   | No file              | `d4d4b0abe240`  |
| 1144   | No documented layout | `d4d4b0abe240`  |
| 1137   | No documented layout | `d4d4b0abe240`  |
| 1132   | No documented layout | `d4d4b0abe240`  |
| 1127   | No documented layout | `d4d4b0abe240`  |
| 1122   | No documented layout | `d4d4b0abe240`  |
| 1118   | No documented layout | `d4d4b0abe240`  |
| 1114   | No documented layout | `d4d4b0abe240`  |
| 1109   | No documented layout | `d4d4b0abe240`  |
| 1102   | No file              | `d4d4b0abe240`  |
| 1096   | No file              | `d4d4b0abe240`  |
| 1088   | No file              | `d4d4b0abe240`  |
| 1081   | No file              | `d4d4b0abe240`  |
| 1076   | No file              | `d4d4b0abe240`  |
| 1069   | No file              | `d4d4b0abe240`  |
| 1064   | No file              | `d4d4b0abe240`  |
| 1058   | No file              | `d4d4b0abe240`  |
| 1051   | No file              | `d4d4b0abe240`  |
| 1044   | No file              | `d4d4b0abe240`  |
| 1036   | No file              | `d4d4b0abe240`  |
| 1026   | No file              | `d4d4b0abe240`  |
| 1016   | No file              | `d4d4b0abe240`  |
| 1009   | No file              | `d4d4b0abe240`  |
| 1005   | No file              | `d4d4b0abe240`  |
| 1000   | No file              | `d4d4b0abe240`  |
| 998    | No file              | `d4d4b0abe240`  |
| 990    | No file              | `d4d4b0abe240`  |
| 979    | No file              | `d4d4b0abe240`  |
| 972    | No file              | `d4d4b0abe240`  |
| 963    | No file              | `d4d4b0abe240`  |
| 955    | No file              | `d4d4b0abe240`  |
| 946    | No file              | `d4d4b0abe240`  |
| 938    | No file              | `d4d4b0abe240`  |
| 927    | No file              | `d4d4b0abe240`  |
| 911    | No file              | `d4d4b0abe240`  |
| 904    | No file              | `d4d4b0abe240`  |
| 899    | No file              | `d4d4b0abe240`  |
| 894    | No file              | `d4d4b0abe240`  |
| 885    | No file              | `d4d4b0abe240`  |
| 879    | No file              | `d4d4b0abe240`  |
| 872    | No file              | `d4d4b0abe240`  |
| 864    | No file              | `d4d4b0abe240`  |
| 855    | No file              | `d4d4b0abe240`  |
| 853    | No file              | `d4d4b0abe240`  |
| 845    | No file              | `d4d4b0abe240`  |
| 837    | No file              | `d4d4b0abe240`  |
| 829    | No file              | `d4d4b0abe240`  |
| 822    | No file              | `d4d4b0abe240`  |
| 814    | No file              | `d4d4b0abe240`  |
| 805    | No file              | `d4d4b0abe240`  |
| 794    | No file              | `d4d4b0abe240`  |
| 787    | No file              | `d4d4b0abe240`  |
| 780    | No file              | `d4d4b0abe240`  |
| 771    | No file              | `d4d4b0abe240`  |
| 760    | No file              | `d4d4b0abe240`  |
| 748    | No file              | `d4d4b0abe240`  |
| 741    | No file              | `d4d4b0abe240`  |
| 736    | No file              | `d4d4b0abe240`  |
| 731    | No file              | `d4d4b0abe240`  |
| 723    | No file              | `d4d4b0abe240`  |
| 711    | No file              | `d4d4b0abe240`  |
| 707    | No file              | `d4d4b0abe240`  |
| 697    | No file              | `d4d4b0abe240`  |
| 689    | No file              | `d4d4b0abe240`  |
| 683    | No file              | `d4d4b0abe240`  |
| 678    | No file              | `d4d4b0abe240`  |
| 670    | No file              | `d4d4b0abe240`  |
| 661    | No file              | `d4d4b0abe240`  |
| 656    | No file              | `d4d4b0abe240`  |
| 652    | No file              | `d4d4b0abe240`  |
| 643    | No file              | `d4d4b0abe240`  |
| 637    | No file              | `d4d4b0abe240`  |
| 630    | No file              | `d4d4b0abe240`  |
| 627    | No file              | `d4d4b0abe240`  |
| 621    | No file              | `d4d4b0abe240`  |
| 617    | No file              | `d4d4b0abe240`  |
| 615    | No file              | `d4d4b0abe240`  |
| 606    | No file              | `d4d4b0abe240`  |
| 599    | No file              | `d4d4b0abe240`  |
| 592    | No file              | `d4d4b0abe240`  |
| 586    | No file              | `d4d4b0abe240`  |
| 577    | No file              | `d4d4b0abe240`  |
| 569    | No file              | `d4d4b0abe240`  |
| 561    | No file              | `d4d4b0abe240`  |
| 554    | No file              | `d4d4b0abe240`  |
| 542    | No file              | `d4d4b0abe240`  |
| 532    | No file              | `d4d4b0abe240`  |
| 531    | No file              | `d4d4b0abe240`  |
| 526    | No file              | `d4d4b0abe240`  |
| 521    | No file              | `d4d4b0abe240`  |
| 517    | No file              | `d4d4b0abe240`  |
| 510    | No file              | `d4d4b0abe240`  |
| 508    | No file              | `d4d4b0abe240`  |
| 504    | No file              | `d4d4b0abe240`  |
| 497    | No file              | `d4d4b0abe240`  |
| 491    | No file              | `d4d4b0abe240`  |
| 485    | No file              | `d4d4b0abe240`  |
| 478    | No file              | `d4d4b0abe240`  |
| 472    | No file              | `d4d4b0abe240`  |
| 466    | No file              | `d4d4b0abe240`  |
| 457    | No file              | `d4d4b0abe240`  |
| 452    | No file              | `d4d4b0abe240`  |
| 449    | No file              | `d4d4b0abe240`  |
| 435    | No file              | `d4d4b0abe240`  |

<!-- versions:end -->

## Companion Files

None. LOC type 58 holds the English group names and condition lines (see Localization).

All multi-byte values are little-endian.

## Layout 1

### File Layout

A header, the groups back to back, the PABR string table and the file trailer.

| Offset              | Type                | Field        | Notes                                                    |
| ------------------- | ------------------- | ------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]             | magic        | `PABR` (ASCII)                                           |
| `+0x04`             | u32                 | group_count  | Number of quest groups; `232` on client 3458             |
| `+0x08`             | Group[group_count]  | groups       | See Group                                                |
| `groups+0x00`       | String Table        | string_table | See String Table                                         |
| `string_table+0x00` | u32                 | table_start  | File offset of the string table's `string_count` (`0x69F1` here) |
| `string_table+0x04` | u32                 | zero         | Observed `0`                                             |

### Group (variable: 23 bytes + quest rows)

An 11-byte group header, `quest_ref_count` quest rows and a 12-byte group trailer.

| Offset      | Type                        | Field             | Notes                                                                   |
| ----------- | --------------------------- | ----------------- | ----------------------------------------------------------------------- |
| `+0x00`     | u16                         | group_key         | The group's key, see Localization; unique per group                     |
| `+0x02`     | u32                         | name_index        | String table index of the Korean group name (`group_name_kr`); `0` for the first group |
| `+0x06`     | u8                          | group_type        | `0` on most groups; the server's `NewQuestType`, see Field Names and Open Questions |
| `+0x07`     | u32                         | quest_ref_count   | Number of following rows                                                |
| `+0x0B`     | Quest Reference Row[quest_ref_count] | rows | See Quest Reference Row                                                      |
| `rows+0x00` | u32                         | event_start_index | String table index of the event start (`event_start`), e.g. `2019-10-16 04:00`; the empty string in the other three lists |
| `rows+0x04` | u32                         | event_end_index   | String table index of the event end (`event_end`), e.g. `2019-11-13 05:59`; always after the start |
| `rows+0x08` | u32                         | unknown_tail_08   | Observed `0` in every group of the four files                          |

The start of group 1 `[Event] Black Desert 2019 Halloween` is `2019-10-16 04:00`, and its English condition lines read `Oct 16 (after maintenance) - ...`.

The times are stored without zero padding (`2018-10-3 10:00`, `2019-7-24 9:00`). The parser pads month, day and hour (`2018-10-03 10:00`) so they sort as text, and keeps text in any other form as stored. All 464 times on client 3458 have the `YYYY-M-D H:MM` form.

### Quest Reference Row (17 bytes)

| Offset  | Type | Field          | Notes                                                                   |
| ------- | ---- | -------------- | ----------------------------------------------------------------------- |
| `+0x00` | u16  | quest_chain_id | LOC type 18 `str_id1`; combines with `quest_id` to form quest key       |
| `+0x02` | u16  | quest_id       | LOC type 18 `str_id2`; combines with `quest_chain_id` to form quest key |
| `+0x04` | u32  | condition_index | String table index of the Korean condition line (`condition_kr`), the source of the LOC condition line |
| `+0x08` | u32  | hide_conditions_index | String table index of the hide condition script (`hide_conditions`), often the empty string; see String Table |
| `+0x0C` | u32  | visible_conditions_index | String table index of the visible condition script (`visible_conditions`), often the empty string; see String Table |
| `+0x10` | u8   | is_sub_quest   | `0` on every row here; `1` on 7 `mainquest.bss` rows                    |

Derived packed quest ID:

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

### String Table (variable: 4 bytes + strings)

Follows the last group: a u32 `string_count`, then `string_count` entries, indexed from `0`. It is the counted string table other PABR `.bss` files end with (`exploration.bss`, `npcsimply.bss`, `menu.bss`), read by `_common/pabr_strings.py`.

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of entries                         |
| `+0x04` | pstr[string_count] | strings      | `is_wide` is `1` on every entry here: UTF-16-LE (`0` would be UTF-8); `length` is the text length in bytes, no terminator |


The table holds each distinct string once, in first-use order: the group name, then each row's condition line, hide condition and visible condition, then the trailer's dates. On client 3458 every entry is used (1,840 here). Index `0` is the first group's name, and the empty string sits where it is first used: index `2` here and in `mainquest.bss` and `recommendationquest.bss`, `31` in `repetitionquest.bss`. That is why the condition indexes repeat one value on so many rows.

The condition lines are the Korean source of the LOC lines and carry the same `<PAColor>` tags. The scripts are client condition calls separated by `;`, with `<or>` between alternatives and `!` for negation: `checkperiodbyGmt(0, 2019/9/4-00:00, 2019/9/25-09:00);`, `clearquest(40022,1);`, `progressquest(...)`, `getLevel()>59;`, `isContentsGroupOpen(0,2177);`, `checkClass(...)`, `getLifeLevel(6)>80;`. Across the four files:

- `visible_conditions` must hold for the quest to be listed: event periods, content groups, level and class checks, prerequisite quests (`mainquest.bss` quest 40022 / 2 needs `clearquest(40022,1);`), and `!clearquest` / `!progressquest` of the quest itself.
- `hide_conditions` takes the quest off the list when it holds: the other branches of a crossroad (7500 / 81 lists 7500 / 82), `do not accept Techthon and Quality Iron` (2001 / 138 lists 2001 / 137), and the other quests of a "once a week per Family" set. No level check ever appears in it.

The quest window (`panel_window_quest_all`) lists a quest of these groups only when `checkHideCondition()` is false and `checkVisibleCondition()` is true.

Calls across the four files on client 3458: `hide_conditions` holds `clearquest` 2,846 times and `progressquest` 1,990 times against 336 negated calls, and never `getLevel` or `checkperiodbyGmt`. `visible_conditions` holds `isContentsGroupOpen` 6,833 times, `checkperiodbyGmt` 5,494, `getLevel` 1,410 and a negated `clearquest` / `progressquest` 4,577 times.

Neither condition holds every check its LOC line names: of 496 `repetitionquest.bss` lines that start `from Lv. N`, 75 have the level check in a script. The rest is likely checked by the quest itself.

## Localization

LOC type `58` holds the English text of this list, keyed by the group's
`group_key`:

| Key                                              | Text                                         |
| ------------------------------------------------ | -------------------------------------------- |
| `str_id1 = group_key`, `str_id4 = 0`             | Group name, e.g. key 1 `[Event] Mastering Life Skills` |
| `str_id1 = packed_quest_id`, `str_id2 = group_key`, `str_id4 = 1` | The quest's condition line, e.g. `From <PAColor0xfff3d900>Lara <PAOldColor>during the event, once per Family` |

On client 3458 all 232 groups have a name (type 58 has 265, so some
belong to groups no longer in the file) and all 1,281 rows have a
condition line. A quest in two groups has a line under each key: quest
11060 / 1 sits in the groups with keys 2 (`[Event] Black Desert 2019
Halloween`) and 62 (`[Event] Black Desert 2020 Halloween`). Condition lines carry `<PAColor>`
tags; group names do not. The Korean names and condition lines in the
string table are the source of both, and the handler shows them where LOC has no row.

## Reference Rows

Client 3458:

| Group | Row | Group Key | Quest Chain ID | Quest ID | condition_index | hide_conditions_index | visible_conditions_index | Example LOC Title |
| ----: | --: | --------: | -------------: | -------: | --------------: | -------------: | -------------: | ----------------- |
| 0     | 0   | `1`       | `11059`        | `9`      | `1`        | `2`        | `2`        | `[Event] Love for Pets` |
| 0     | 1   | `1`       | `11059`        | `10`     | `1`        | `2`        | `2`        | `[Event] Savory Good Feed` |

## Notes

- Decompressed size is `820,905` bytes on client 3458 (`816,761` with 224 groups and 1,255 rows before 2026-09-27).
- 27 quests sit in two groups (29 before 2026-09-27); each copy has its own condition line in LOC.
- The string table indexes shift whenever a string is added earlier in the file, so `condition_index` / `hide_conditions_index` / `visible_conditions_index` are not stable across patches: quest `77129` had `condition_index = 899` before 2026-09-27 and `896` after.
- Earlier versions of this doc and the handler read a 10-byte first group header and a 23-byte later one: the previous group's trailer followed by the next group's header. The rows were the same. They called the row flag `flags`, called `condition_index` / `hide_conditions_index` / `visible_conditions_index` `sequence_a` / `sequence_b` / `sequence_c` and later `unknown_05` / `unknown_09` / `unknown_0d`, and named the header fields `header_flag`, `unknown_a` to `unknown_d`, `group_key_a` and `group_key_b`.
- Until 2026-10-15 the conditions were `script_1` (hide) and `script_2` (visible), shown as Ruled Out When* and Offered When* with the role marked as a guess, and `group_type` and `is_sub_quest` were `unknown_06` and `unknown_10`.
- Until client 3464 this doc and the handler read a u16 `quest_ref_count` plus a padding byte, a row that opened with a u8 `unknown_00`, and a trailer that opened with a zero byte. Group sizes were the same, but each row took the flag byte of the row before it. `mainquest.bss` decides it: the 7 rows with the flag set are 6603 / 2 to 8, the whole run that shares the `hide_conditions` `getknowledge(6392);<or>clearquest(21601,1);<or>!clearquest(351,1);`. The old reading flagged 6603 / 3 to 8 and 6002 / 13, which has another `hide_conditions`. The [calpheonlabs](https://github.com/marceloclp/calpheonlabs) `newquest.bss` page reads the layout the same way.

## Field Names

The 2016 client has no struct or loader for these lists. The server-side tables of a private server on client 519 name every field: `<List>Quest_Table` (`<List>QuestGroupKey`, `QuestGroup`, `QuestID`, `AcceptConditionText`, `HideConditions`, `VisibleConditions`, `IsSubQuest`) and `Group_<List>Quest` (`<List>QuestGroupKey`, `<List>QuestType`, `<List>QuestGroupName`, `Desc`, and `StartDate` and `EndDate` for the event list), where `<List>` is `New`, `Main`, `Recommendation` or `Repetition`. Rows join on the group key and quest ID with client 3464:

| Field | Column | `newquest` | `mainquest` | `recommendationquest` | `repetitionquest` |
| ----- | ------ | ---------: | ----------: | --------------------: | ----------------: |
| shared rows | | 385 | 536 | 272 | 295 |
| condition_kr | `AcceptConditionText` | 160 | 171 | 156 | 55 |
| hide_conditions | `HideConditions` | 65 of 65 | 137 of 267 | 9 of 11 | 17 of 17 |
| visible_conditions | `VisibleConditions` | 144 of 175 | 131 of 131 | 4 of 211 | none set |
| is_sub_quest | `IsSubQuest` | none set | 7 of 7 | none set | none set |
| shared groups | | 43 | 12 | 24 | 20 |
| group_type | `<List>QuestType` | 3 of 3 | none set | 17 of 19 | none set |
| group_name_kr | `<List>QuestGroupName` | 43 | 8 | 4 | 0 |
| event_start, event_end | `StartDate`, `EndDate` | 38, 37 | - | - | - |

Counts with "of" are the rows where the server column is not empty or `0`. The low counts are text the client changed since: the server's `VisibleConditions` on 207 `recommendationquest` rows still checks levels the client dropped (`getLifeLevel(0)>9;getlevel()>19;` on 2100 / 115 to 118, where the client stores none), its `HideConditions` on 130 `mainquest` rows are longer versions of the client's (`clearquest(21401,1);<or>isContentsGroupOpen(0,110);!clearquest(4001,1);...` where 4001 / 1 to 4 store `!clearquest(4001,1);`), and Korean condition lines and group names were reworded.

The client Lua confirms the two condition roles: the quest window (`panel_window_quest_all`) lists a quest when `checkHideCondition()` is false and `checkVisibleCondition()` is true. `group_type` and `is_sub_quest` rest on the server columns alone; the Lua never calls a getter for either on these lists.

## Open Questions

### What Does `group_type` Select?

`0` on 227 of 232 groups here, and `1`, `2`, `6` or `8` on the rest (`[Hunting] Sniping, ...` 2, `Krogdalo's Three Seeds` 1, `[Season] Stronger Tuvala Gear` 8). In `recommendationquest.bss` it runs `0` to `8` and groups by theme ([Life] [Leap] gurus at 4 to 7, mounts and outfits at 2), so it may be a category or tab. The server calls it `NewQuestType`, but no Lua getter reads it, so which UI uses it is not confirmed.

### Duplicate Quest References

A quest in two groups has a condition line under both group keys, so a quest can be listed by two events (11060 / 1 in the 2019 and 2020 Halloween groups). Whether the game shows both copies at once is not confirmed.

### What Does `unknown_tail_08` Index?

`0` in every group of the four lists (clients 1784 and 3474). No sheet
column of `Group_MainQuest` or `Group_NewQuest` fills it. The client 1784
server dump has a u32 that its group loader sets to `0` as the last member
of the group struct (`+0x98`), and the only code that reads that member is
the language-data writer (VA `0x140c1faf0`): it passes the value with the
list's LOC type (28, 42, 43 or 58) to a lookup that skips `0` and otherwise
reads an 8-byte entry at `value * 8` of a `Head_LanguageData_` file. The
server has no reader for these files, so tying the file's trailer to that
member rests on position only, and nothing names it.
