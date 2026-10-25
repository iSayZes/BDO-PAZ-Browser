# `characterobject.dbss` Format

## Purpose

Per-character world-object records for placeable objects: house furniture and crafting tools, crops, houses and other buildings, tents, barricades and guild siege towers. Each record carries the object's kind, its model path and, for most records, an inline icon path. Names come from LOC type `6`, the same table `characterstatic.dbss` uses.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes     | Records                                                                                                                                                                                | Row bytes |
| ------ | -------------- | ---------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 2      | 3302 and later | `characterobject.dbss`       | 8,183,741 | 28,202 Face, 2,321 Hull, 1,079 Hull Layer, 295 Structure Suffix, 1,160 Structure Body, 5,131 Record, 3,971 Furniture Block, 3,971 Furniture Tail, 3,971 Furniture Body, 865 House Tail | 140       |
| 2      | 3302 and later | `characterobjectoffset.dbss` | 51,330    | 5,131 Index Row                                                                                                                                                                        | 10        |
| 1      | 1762 to 2243   | `characterobject.dbss`       | 6,959,048 | 26,090 Face, 2,147 Hull, 1,009 Hull Layer, 151 Structure Suffix, 981 Structure Body, 4,232 Record, 3,251 Furniture Block, 3,251 Furniture Tail, 3,251 Furniture Body, 830 House Tail   | 140       |
| 1      | 1762 to 2243   | `characterobjectoffset.dbss` | 42,340    | 4,232 Index Row                                                                                                                                                                        | 10        |

| Layout | File                         | Known               | Unknown             |
| ------ | ---------------------------- | ------------------- | ------------------- |
| 2      | `characterobject.dbss`       | 5,222,514 B (63.8%) | 2,961,227 B (36.2%) |
| 2      | `characterobjectoffset.dbss` | 51,330 B (100.0%)   | 0 B (0.0%)          |
| 1      | `characterobject.dbss`       | 4,706,425 B (67.6%) | 2,252,623 B (32.4%) |
| 1      | `characterobjectoffset.dbss` | 42,340 B (100.0%)   | 0 B (0.0%)          |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `805c0b75d5e7`  |
| 3482   | Layout 2             | `805c0b75d5e7`  |
| 3474   | Layout 2             | `805c0b75d5e7`  |
| 3473   | Layout 2             | `805c0b75d5e7`  |
| 3464   | Layout 2             | `805c0b75d5e7`  |
| 3458   | Layout 2             | `805c0b75d5e7`  |
| 3454   | Layout 2             | `805c0b75d5e7`  |
| 3444   | Layout 2             | `805c0b75d5e7`  |
| 3435   | Layout 2             | `805c0b75d5e7`  |
| 3426   | Layout 2             | `805c0b75d5e7`  |
| 3418   | Layout 2             | `805c0b75d5e7`  |
| 3412   | Layout 2             | `805c0b75d5e7`  |
| 3402   | Layout 2             | `805c0b75d5e7`  |
| 3396   | Layout 2             | `805c0b75d5e7`  |
| 3387   | Layout 2             | `805c0b75d5e7`  |
| 3381   | Layout 2             | `805c0b75d5e7`  |
| 3373   | Layout 2             | `805c0b75d5e7`  |
| 3364   | Layout 2             | `805c0b75d5e7`  |
| 3356   | Layout 2             | `805c0b75d5e7`  |
| 3349   | Layout 2             | `805c0b75d5e7`  |
| 3342   | Layout 2             | `805c0b75d5e7`  |
| 3335   | Layout 2             | `805c0b75d5e7`  |
| 3326   | Layout 2             | `805c0b75d5e7`  |
| 3321   | Layout 2             | `805c0b75d5e7`  |
| 3314   | Layout 2             | `805c0b75d5e7`  |
| 3303   | Layout 2             | `805c0b75d5e7`  |
| 3302   | Layout 2             | `805c0b75d5e7`  |
| 3293   | No documented layout | `805c0b75d5e7`  |
| 3283   | No documented layout | `805c0b75d5e7`  |
| 3275   | No documented layout | `805c0b75d5e7`  |
| 3267   | No documented layout | `805c0b75d5e7`  |
| 3258   | No documented layout | `805c0b75d5e7`  |
| 3251   | No documented layout | `805c0b75d5e7`  |
| 3242   | No documented layout | `805c0b75d5e7`  |
| 3235   | No documented layout | `805c0b75d5e7`  |
| 3229   | No documented layout | `805c0b75d5e7`  |
| 3212   | No documented layout | `805c0b75d5e7`  |
| 3203   | No documented layout | `805c0b75d5e7`  |
| 3193   | No documented layout | `805c0b75d5e7`  |
| 3186   | No documented layout | `805c0b75d5e7`  |
| 3177   | No documented layout | `805c0b75d5e7`  |
| 3169   | No documented layout | `805c0b75d5e7`  |
| 3158   | No documented layout | `805c0b75d5e7`  |
| 3151   | No documented layout | `805c0b75d5e7`  |
| 3144   | No documented layout | `805c0b75d5e7`  |
| 3133   | No documented layout | `805c0b75d5e7`  |
| 3125   | No documented layout | `805c0b75d5e7`  |
| 3118   | No documented layout | `805c0b75d5e7`  |
| 3111   | No documented layout | `805c0b75d5e7`  |
| 3103   | No documented layout | `805c0b75d5e7`  |
| 3095   | No documented layout | `805c0b75d5e7`  |
| 3086   | No documented layout | `805c0b75d5e7`  |
| 3072   | No documented layout | `805c0b75d5e7`  |
| 3062   | No documented layout | `805c0b75d5e7`  |
| 3052   | No documented layout | `805c0b75d5e7`  |
| 3045   | No documented layout | `805c0b75d5e7`  |
| 3037   | No documented layout | `805c0b75d5e7`  |
| 3030   | No documented layout | `805c0b75d5e7`  |
| 3021   | No documented layout | `805c0b75d5e7`  |
| 3012   | No documented layout | `805c0b75d5e7`  |
| 3002   | No documented layout | `805c0b75d5e7`  |
| 2995   | No documented layout | `805c0b75d5e7`  |
| 2987   | No documented layout | `805c0b75d5e7`  |
| 2978   | No documented layout | `805c0b75d5e7`  |
| 2970   | No documented layout | `805c0b75d5e7`  |
| 2959   | No documented layout | `805c0b75d5e7`  |
| 2951   | No documented layout | `805c0b75d5e7`  |
| 2942   | No documented layout | `805c0b75d5e7`  |
| 2935   | No documented layout | `805c0b75d5e7`  |
| 2932   | No documented layout | `805c0b75d5e7`  |
| 2923   | No documented layout | `805c0b75d5e7`  |
| 2919   | No documented layout | `805c0b75d5e7`  |
| 2907   | No documented layout | `805c0b75d5e7`  |
| 2900   | No documented layout | `805c0b75d5e7`  |
| 2891   | No documented layout | `805c0b75d5e7`  |
| 2882   | No documented layout | `805c0b75d5e7`  |
| 2872   | No documented layout | `805c0b75d5e7`  |
| 2863   | No documented layout | `805c0b75d5e7`  |
| 2855   | No documented layout | `805c0b75d5e7`  |
| 2849   | No documented layout | `805c0b75d5e7`  |
| 2844   | No documented layout | `805c0b75d5e7`  |
| 2834   | No documented layout | `805c0b75d5e7`  |
| 2825   | No documented layout | `805c0b75d5e7`  |
| 2819   | No documented layout | `805c0b75d5e7`  |
| 2811   | No documented layout | `805c0b75d5e7`  |
| 2803   | No documented layout | `805c0b75d5e7`  |
| 2794   | No documented layout | `805c0b75d5e7`  |
| 2783   | No documented layout | `805c0b75d5e7`  |
| 2774   | No documented layout | `805c0b75d5e7`  |
| 2765   | No documented layout | `805c0b75d5e7`  |
| 2756   | No documented layout | `805c0b75d5e7`  |
| 2750   | No documented layout | `805c0b75d5e7`  |
| 2743   | No documented layout | `805c0b75d5e7`  |
| 2736   | No documented layout | `805c0b75d5e7`  |
| 2726   | No documented layout | `805c0b75d5e7`  |
| 2717   | No documented layout | `805c0b75d5e7`  |
| 2709   | No documented layout | `805c0b75d5e7`  |
| 2703   | No documented layout | `805c0b75d5e7`  |
| 2695   | No documented layout | `805c0b75d5e7`  |
| 2684   | No documented layout | `805c0b75d5e7`  |
| 2672   | No documented layout | `805c0b75d5e7`  |
| 2665   | No documented layout | `805c0b75d5e7`  |
| 2657   | No documented layout | `805c0b75d5e7`  |
| 2649   | No documented layout | `805c0b75d5e7`  |
| 2644   | No documented layout | `805c0b75d5e7`  |
| 2637   | No documented layout | `805c0b75d5e7`  |
| 2629   | No documented layout | `805c0b75d5e7`  |
| 2619   | No documented layout | `805c0b75d5e7`  |
| 2612   | No documented layout | `805c0b75d5e7`  |
| 2606   | No documented layout | `805c0b75d5e7`  |
| 2602   | No documented layout | `805c0b75d5e7`  |
| 2601   | No documented layout | `805c0b75d5e7`  |
| 2592   | No documented layout | `805c0b75d5e7`  |
| 2583   | No documented layout | `805c0b75d5e7`  |
| 2575   | No documented layout | `805c0b75d5e7`  |
| 2567   | No documented layout | `805c0b75d5e7`  |
| 2560   | No documented layout | `805c0b75d5e7`  |
| 2553   | No documented layout | `805c0b75d5e7`  |
| 2545   | No documented layout | `805c0b75d5e7`  |
| 2538   | No documented layout | `805c0b75d5e7`  |
| 2529   | No documented layout | `805c0b75d5e7`  |
| 2519   | No documented layout | `805c0b75d5e7`  |
| 2513   | No documented layout | `805c0b75d5e7`  |
| 2510   | No documented layout | `805c0b75d5e7`  |
| 2507   | No documented layout | `805c0b75d5e7`  |
| 2503   | No documented layout | `805c0b75d5e7`  |
| 2498   | No documented layout | `805c0b75d5e7`  |
| 2492   | No documented layout | `805c0b75d5e7`  |
| 2487   | No documented layout | `805c0b75d5e7`  |
| 2480   | No documented layout | `805c0b75d5e7`  |
| 2474   | No documented layout | `805c0b75d5e7`  |
| 2468   | No documented layout | `805c0b75d5e7`  |
| 2460   | No documented layout | `805c0b75d5e7`  |
| 2453   | No documented layout | `805c0b75d5e7`  |
| 2444   | No documented layout | `805c0b75d5e7`  |
| 2438   | No documented layout | `805c0b75d5e7`  |
| 2434   | No documented layout | `805c0b75d5e7`  |
| 2429   | No documented layout | `805c0b75d5e7`  |
| 2421   | No documented layout | `805c0b75d5e7`  |
| 2414   | No documented layout | `805c0b75d5e7`  |
| 2407   | No documented layout | `805c0b75d5e7`  |
| 2401   | No documented layout | `805c0b75d5e7`  |
| 2397   | No documented layout | `805c0b75d5e7`  |
| 2393   | No documented layout | `805c0b75d5e7`  |
| 2384   | No documented layout | `805c0b75d5e7`  |
| 2378   | No documented layout | `805c0b75d5e7`  |
| 2372   | No documented layout | `805c0b75d5e7`  |
| 2358   | No documented layout | `805c0b75d5e7`  |
| 2352   | No documented layout | `805c0b75d5e7`  |
| 2347   | No documented layout | `805c0b75d5e7`  |
| 2343   | No documented layout | `805c0b75d5e7`  |
| 2335   | No documented layout | `805c0b75d5e7`  |
| 2327   | No documented layout | `805c0b75d5e7`  |
| 2324   | No documented layout | `805c0b75d5e7`  |
| 2319   | No documented layout | `805c0b75d5e7`  |
| 2313   | No documented layout | `805c0b75d5e7`  |
| 2308   | No documented layout | `805c0b75d5e7`  |
| 2302   | No documented layout | `805c0b75d5e7`  |
| 2295   | No documented layout | `805c0b75d5e7`  |
| 2290   | No documented layout | `805c0b75d5e7`  |
| 2284   | No documented layout | `805c0b75d5e7`  |
| 2276   | No documented layout | `805c0b75d5e7`  |
| 2269   | No documented layout | `805c0b75d5e7`  |
| 2259   | No documented layout | `805c0b75d5e7`  |
| 2250   | No documented layout | `805c0b75d5e7`  |
| 2243   | Layout 1             | `805c0b75d5e7`  |
| 2235   | Layout 1             | `805c0b75d5e7`  |
| 2229   | Layout 1             | `805c0b75d5e7`  |
| 2224   | Layout 1             | `805c0b75d5e7`  |
| 2218   | Layout 1             | `805c0b75d5e7`  |
| 2215   | Layout 1             | `805c0b75d5e7`  |
| 2207   | Layout 1             | `805c0b75d5e7`  |
| 2203   | Layout 1             | `805c0b75d5e7`  |
| 2196   | Layout 1             | `805c0b75d5e7`  |
| 2192   | Layout 1             | `805c0b75d5e7`  |
| 2189   | Layout 1             | `805c0b75d5e7`  |
| 2183   | Layout 1             | `805c0b75d5e7`  |
| 2179   | Layout 1             | `805c0b75d5e7`  |
| 2171   | Layout 1             | `805c0b75d5e7`  |
| 2163   | Layout 1             | `805c0b75d5e7`  |
| 2156   | Layout 1             | `805c0b75d5e7`  |
| 2151   | Layout 1             | `805c0b75d5e7`  |
| 2147   | Layout 1             | `805c0b75d5e7`  |
| 2142   | Layout 1             | `805c0b75d5e7`  |
| 2138   | Layout 1             | `805c0b75d5e7`  |
| 2134   | Layout 1             | `805c0b75d5e7`  |
| 2130   | Layout 1             | `805c0b75d5e7`  |
| 2122   | Layout 1             | `805c0b75d5e7`  |
| 2107   | Layout 1             | `805c0b75d5e7`  |
| 2098   | Layout 1             | `805c0b75d5e7`  |
| 2089   | Layout 1             | `805c0b75d5e7`  |
| 2081   | Layout 1             | `805c0b75d5e7`  |
| 2073   | Layout 1             | `805c0b75d5e7`  |
| 2067   | Layout 1             | `805c0b75d5e7`  |
| 2063   | Layout 1             | `805c0b75d5e7`  |
| 2059   | Layout 1             | `805c0b75d5e7`  |
| 2052   | Layout 1             | `805c0b75d5e7`  |
| 2044   | Layout 1             | `805c0b75d5e7`  |
| 2039   | Layout 1             | `805c0b75d5e7`  |
| 2032   | Layout 1             | `805c0b75d5e7`  |
| 2025   | Layout 1             | `805c0b75d5e7`  |
| 2011   | Layout 1             | `805c0b75d5e7`  |
| 2005   | Layout 1             | `805c0b75d5e7`  |
| 2000   | Layout 1             | `805c0b75d5e7`  |
| 1996   | Layout 1             | `805c0b75d5e7`  |
| 1991   | Layout 1             | `805c0b75d5e7`  |
| 1985   | Layout 1             | `805c0b75d5e7`  |
| 1980   | Layout 1             | `805c0b75d5e7`  |
| 1969   | Layout 1             | `805c0b75d5e7`  |
| 1964   | Layout 1             | `805c0b75d5e7`  |
| 1958   | Layout 1             | `805c0b75d5e7`  |
| 1950   | Layout 1             | `805c0b75d5e7`  |
| 1945   | Layout 1             | `805c0b75d5e7`  |
| 1937   | Layout 1             | `805c0b75d5e7`  |
| 1933   | Layout 1             | `805c0b75d5e7`  |
| 1927   | Layout 1             | `805c0b75d5e7`  |
| 1921   | Layout 1             | `805c0b75d5e7`  |
| 1914   | Layout 1             | `805c0b75d5e7`  |
| 1908   | Layout 1             | `805c0b75d5e7`  |
| 1897   | Layout 1             | `805c0b75d5e7`  |
| 1892   | Layout 1             | `805c0b75d5e7`  |
| 1886   | Layout 1             | `805c0b75d5e7`  |
| 1881   | Layout 1             | `805c0b75d5e7`  |
| 1871   | Layout 1             | `805c0b75d5e7`  |
| 1866   | Layout 1             | `805c0b75d5e7`  |
| 1862   | Layout 1             | `805c0b75d5e7`  |
| 1854   | Layout 1             | `805c0b75d5e7`  |
| 1846   | Layout 1             | `805c0b75d5e7`  |
| 1838   | Layout 1             | `805c0b75d5e7`  |
| 1832   | Layout 1             | `805c0b75d5e7`  |
| 1826   | Layout 1             | `805c0b75d5e7`  |
| 1822   | Layout 1             | `805c0b75d5e7`  |
| 1818   | Layout 1             | `805c0b75d5e7`  |
| 1804   | Layout 1             | `805c0b75d5e7`  |
| 1794   | Layout 1             | `805c0b75d5e7`  |
| 1790   | Layout 1             | `805c0b75d5e7`  |
| 1784   | Layout 1             | `805c0b75d5e7`  |
| 1774   | Layout 1             | `805c0b75d5e7`  |
| 1771   | Layout 1             | `805c0b75d5e7`  |
| 1762   | Layout 1             | `805c0b75d5e7`  |
| 1759   | No documented layout | `805c0b75d5e7`  |
| 1754   | No documented layout | `805c0b75d5e7`  |
| 1749   | No documented layout | `805c0b75d5e7`  |
| 1743   | No documented layout | `805c0b75d5e7`  |
| 1737   | No documented layout | `805c0b75d5e7`  |
| 1731   | No documented layout | `805c0b75d5e7`  |
| 1725   | No documented layout | `805c0b75d5e7`  |
| 1717   | No documented layout | `805c0b75d5e7`  |
| 1710   | No documented layout | `805c0b75d5e7`  |
| 1704   | No documented layout | `805c0b75d5e7`  |
| 1698   | No documented layout | `805c0b75d5e7`  |
| 1690   | No documented layout | `805c0b75d5e7`  |
| 1685   | No documented layout | `805c0b75d5e7`  |
| 1680   | No documented layout | `805c0b75d5e7`  |
| 1674   | No documented layout | `805c0b75d5e7`  |
| 1668   | No documented layout | `805c0b75d5e7`  |
| 1659   | No documented layout | `805c0b75d5e7`  |
| 1649   | No documented layout | `805c0b75d5e7`  |
| 1642   | No documented layout | `805c0b75d5e7`  |
| 1636   | No documented layout | `805c0b75d5e7`  |
| 1628   | No documented layout | `805c0b75d5e7`  |
| 1622   | No documented layout | `805c0b75d5e7`  |
| 1614   | No documented layout | `805c0b75d5e7`  |
| 1608   | No documented layout | `805c0b75d5e7`  |
| 1602   | No documented layout | `805c0b75d5e7`  |
| 1598   | No documented layout | `805c0b75d5e7`  |
| 1594   | No documented layout | `805c0b75d5e7`  |
| 1590   | No documented layout | `805c0b75d5e7`  |
| 1587   | No documented layout | `805c0b75d5e7`  |
| 1584   | No documented layout | `805c0b75d5e7`  |
| 1579   | No documented layout | `805c0b75d5e7`  |
| 1572   | No documented layout | `805c0b75d5e7`  |
| 1565   | No documented layout | `805c0b75d5e7`  |
| 1559   | No documented layout | `805c0b75d5e7`  |
| 1554   | No documented layout | `805c0b75d5e7`  |
| 1547   | No documented layout | `805c0b75d5e7`  |
| 1537   | No documented layout | `805c0b75d5e7`  |
| 1529   | No documented layout | `805c0b75d5e7`  |
| 1524   | No documented layout | `805c0b75d5e7`  |
| 1519   | No documented layout | `805c0b75d5e7`  |
| 1509   | No documented layout | `805c0b75d5e7`  |
| 1506   | No documented layout | `805c0b75d5e7`  |
| 1504   | No documented layout | `805c0b75d5e7`  |
| 1500   | No documented layout | `805c0b75d5e7`  |
| 1493   | No documented layout | `805c0b75d5e7`  |
| 1489   | No documented layout | `805c0b75d5e7`  |
| 1485   | No documented layout | `805c0b75d5e7`  |
| 1481   | No documented layout | `805c0b75d5e7`  |
| 1474   | No documented layout | `805c0b75d5e7`  |
| 1466   | No documented layout | `805c0b75d5e7`  |
| 1462   | No documented layout | `805c0b75d5e7`  |
| 1459   | No documented layout | `805c0b75d5e7`  |
| 1453   | No documented layout | `805c0b75d5e7`  |
| 1450   | No documented layout | `805c0b75d5e7`  |
| 1445   | No documented layout | `805c0b75d5e7`  |
| 1439   | No documented layout | `805c0b75d5e7`  |
| 1433   | No documented layout | `805c0b75d5e7`  |
| 1430   | No documented layout | `805c0b75d5e7`  |
| 1426   | No documented layout | `805c0b75d5e7`  |
| 1421   | No documented layout | `805c0b75d5e7`  |
| 1417   | No documented layout | `805c0b75d5e7`  |
| 1416   | No documented layout | `805c0b75d5e7`  |
| 1409   | No documented layout | `805c0b75d5e7`  |
| 1405   | No documented layout | `805c0b75d5e7`  |
| 1401   | No documented layout | `805c0b75d5e7`  |
| 1396   | No documented layout | `805c0b75d5e7`  |
| 1391   | No documented layout | `805c0b75d5e7`  |
| 1390   | No documented layout | `805c0b75d5e7`  |
| 1386   | No documented layout | `805c0b75d5e7`  |
| 1381   | No documented layout | `805c0b75d5e7`  |
| 1379   | No documented layout | `805c0b75d5e7`  |
| 1372   | No documented layout | `805c0b75d5e7`  |
| 1366   | No documented layout | `805c0b75d5e7`  |
| 1364   | No documented layout | `805c0b75d5e7`  |
| 1363   | No documented layout | `805c0b75d5e7`  |
| 1360   | No documented layout | `805c0b75d5e7`  |
| 1358   | No documented layout | `805c0b75d5e7`  |
| 1355   | No documented layout | `805c0b75d5e7`  |
| 1351   | No documented layout | `805c0b75d5e7`  |
| 1348   | No documented layout | `805c0b75d5e7`  |
| 1346   | No documented layout | `805c0b75d5e7`  |
| 1341   | No documented layout | `805c0b75d5e7`  |
| 1340   | No documented layout | `805c0b75d5e7`  |
| 1338   | No documented layout | `805c0b75d5e7`  |
| 1335   | No documented layout | `805c0b75d5e7`  |
| 1333   | No documented layout | `805c0b75d5e7`  |
| 1329   | No documented layout | `805c0b75d5e7`  |
| 1327   | No documented layout | `805c0b75d5e7`  |
| 1324   | No documented layout | `805c0b75d5e7`  |
| 1321   | No documented layout | `805c0b75d5e7`  |
| 1319   | No documented layout | `805c0b75d5e7`  |
| 1318   | No documented layout | `805c0b75d5e7`  |
| 1316   | No documented layout | `805c0b75d5e7`  |
| 1313   | No documented layout | `805c0b75d5e7`  |
| 1311   | No documented layout | `805c0b75d5e7`  |
| 1309   | No documented layout | `805c0b75d5e7`  |
| 1304   | No documented layout | `805c0b75d5e7`  |
| 1292   | No documented layout | `805c0b75d5e7`  |
| 1286   | No documented layout | `805c0b75d5e7`  |
| 1280   | No documented layout | `805c0b75d5e7`  |
| 1276   | No documented layout | `805c0b75d5e7`  |
| 1267   | No documented layout | `805c0b75d5e7`  |
| 1261   | No documented layout | `805c0b75d5e7`  |
| 1256   | No documented layout | `805c0b75d5e7`  |
| 1250   | No documented layout | `805c0b75d5e7`  |
| 1246   | No file              | `805c0b75d5e7`  |
| 1239   | No file              | `805c0b75d5e7`  |
| 1230   | No file              | `805c0b75d5e7`  |
| 1226   | No file              | `805c0b75d5e7`  |
| 1220   | No file              | `805c0b75d5e7`  |
| 1217   | No file              | `805c0b75d5e7`  |
| 1211   | No file              | `805c0b75d5e7`  |
| 1210   | No file              | `805c0b75d5e7`  |
| 1208   | No file              | `805c0b75d5e7`  |
| 1203   | No file              | `805c0b75d5e7`  |
| 1197   | No file              | `805c0b75d5e7`  |
| 1194   | No file              | `805c0b75d5e7`  |
| 1192   | No file              | `805c0b75d5e7`  |
| 1187   | No file              | `805c0b75d5e7`  |
| 1183   | No file              | `805c0b75d5e7`  |
| 1177   | No file              | `805c0b75d5e7`  |
| 1173   | No file              | `805c0b75d5e7`  |
| 1167   | No file              | `805c0b75d5e7`  |
| 1164   | No file              | `805c0b75d5e7`  |
| 1156   | No file              | `805c0b75d5e7`  |
| 1149   | No file              | `805c0b75d5e7`  |
| 1144   | No file              | `805c0b75d5e7`  |
| 1137   | No file              | `805c0b75d5e7`  |
| 1132   | No file              | `805c0b75d5e7`  |
| 1127   | No file              | `805c0b75d5e7`  |
| 1122   | No file              | `805c0b75d5e7`  |
| 1118   | No file              | `805c0b75d5e7`  |
| 1114   | No file              | `805c0b75d5e7`  |
| 1109   | No file              | `805c0b75d5e7`  |
| 1102   | No file              | `805c0b75d5e7`  |
| 1096   | No file              | `805c0b75d5e7`  |
| 1088   | No file              | `805c0b75d5e7`  |
| 1081   | No file              | `805c0b75d5e7`  |
| 1076   | No file              | `805c0b75d5e7`  |
| 1069   | No file              | `805c0b75d5e7`  |
| 1064   | No file              | `805c0b75d5e7`  |
| 1058   | No file              | `805c0b75d5e7`  |
| 1051   | No file              | `805c0b75d5e7`  |
| 1044   | No file              | `805c0b75d5e7`  |
| 1036   | No file              | `805c0b75d5e7`  |
| 1026   | No file              | `805c0b75d5e7`  |
| 1016   | No file              | `805c0b75d5e7`  |
| 1009   | No file              | `805c0b75d5e7`  |
| 1005   | No file              | `805c0b75d5e7`  |
| 1000   | No file              | `805c0b75d5e7`  |
| 998    | No file              | `805c0b75d5e7`  |
| 990    | No file              | `805c0b75d5e7`  |
| 979    | No file              | `805c0b75d5e7`  |
| 972    | No file              | `805c0b75d5e7`  |
| 963    | No file              | `805c0b75d5e7`  |
| 955    | No file              | `805c0b75d5e7`  |
| 946    | No file              | `805c0b75d5e7`  |
| 938    | No file              | `805c0b75d5e7`  |
| 927    | No file              | `805c0b75d5e7`  |
| 911    | No file              | `805c0b75d5e7`  |
| 904    | No file              | `805c0b75d5e7`  |
| 899    | No file              | `805c0b75d5e7`  |
| 894    | No file              | `805c0b75d5e7`  |
| 885    | No file              | `805c0b75d5e7`  |
| 879    | No file              | `805c0b75d5e7`  |
| 872    | No file              | `805c0b75d5e7`  |
| 864    | No file              | `805c0b75d5e7`  |
| 855    | No file              | `805c0b75d5e7`  |
| 853    | No file              | `805c0b75d5e7`  |
| 845    | No file              | `805c0b75d5e7`  |
| 837    | No file              | `805c0b75d5e7`  |
| 829    | No file              | `805c0b75d5e7`  |
| 822    | No file              | `805c0b75d5e7`  |
| 814    | No file              | `805c0b75d5e7`  |
| 805    | No file              | `805c0b75d5e7`  |
| 794    | No file              | `805c0b75d5e7`  |
| 787    | No file              | `805c0b75d5e7`  |
| 780    | No file              | `805c0b75d5e7`  |
| 771    | No file              | `805c0b75d5e7`  |
| 760    | No file              | `805c0b75d5e7`  |
| 748    | No file              | `805c0b75d5e7`  |
| 741    | No file              | `805c0b75d5e7`  |
| 736    | No file              | `805c0b75d5e7`  |
| 731    | No file              | `805c0b75d5e7`  |
| 723    | No file              | `805c0b75d5e7`  |
| 711    | No file              | `805c0b75d5e7`  |
| 707    | No file              | `805c0b75d5e7`  |
| 697    | No file              | `805c0b75d5e7`  |
| 689    | No file              | `805c0b75d5e7`  |
| 683    | No file              | `805c0b75d5e7`  |
| 678    | No file              | `805c0b75d5e7`  |
| 670    | No file              | `805c0b75d5e7`  |
| 661    | No file              | `805c0b75d5e7`  |
| 656    | No file              | `805c0b75d5e7`  |
| 652    | No file              | `805c0b75d5e7`  |
| 643    | No file              | `805c0b75d5e7`  |
| 637    | No file              | `805c0b75d5e7`  |
| 630    | No file              | `805c0b75d5e7`  |
| 627    | No file              | `805c0b75d5e7`  |
| 621    | No file              | `805c0b75d5e7`  |
| 617    | No file              | `805c0b75d5e7`  |
| 615    | No file              | `805c0b75d5e7`  |
| 606    | No file              | `805c0b75d5e7`  |
| 599    | No file              | `805c0b75d5e7`  |
| 592    | No file              | `805c0b75d5e7`  |
| 586    | No file              | `805c0b75d5e7`  |
| 577    | No file              | `805c0b75d5e7`  |
| 569    | No file              | `805c0b75d5e7`  |
| 561    | No file              | `805c0b75d5e7`  |
| 554    | No file              | `805c0b75d5e7`  |
| 542    | No file              | `805c0b75d5e7`  |
| 532    | No file              | `805c0b75d5e7`  |
| 531    | No file              | `805c0b75d5e7`  |
| 526    | No file              | `805c0b75d5e7`  |
| 521    | No file              | `805c0b75d5e7`  |
| 517    | No file              | `805c0b75d5e7`  |
| 510    | No file              | `805c0b75d5e7`  |
| 508    | No file              | `805c0b75d5e7`  |
| 504    | No file              | `805c0b75d5e7`  |
| 497    | No file              | `805c0b75d5e7`  |
| 491    | No file              | `805c0b75d5e7`  |
| 485    | No file              | `805c0b75d5e7`  |
| 478    | No file              | `805c0b75d5e7`  |
| 472    | No file              | `805c0b75d5e7`  |
| 466    | No file              | `805c0b75d5e7`  |
| 457    | No file              | `805c0b75d5e7`  |
| 452    | No file              | `805c0b75d5e7`  |
| 449    | No file              | `805c0b75d5e7`  |
| 435    | No file              | `805c0b75d5e7`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                  |
| ---------------------------- | -------- | ----------------------------------------------------- |
| `characterobjectoffset.dbss` | Required | Maps `character_id` to byte offset and size of record |
| `languagedata_en.loc`        | Optional | Object names via type `6`                             |

All multi-byte values are little-endian. Strings are a u64 length followed by ASCII (`str8`, length in bytes) or UTF-16-LE (`str16`, length in code units) text with no terminator; the high u32 of the length is always `0`.

## Layout 2

### File Layout

Records are contiguous: sorted by offset, each one ends exactly where the next begins, the first starts at `+0x04` and the last ends at end of file. They are **not** stored in key order, so walking the offset table row by row jumps around the file.

| Offset  | Type          | Field   | Notes                                                     |
| ------- | ------------- | ------- | --------------------------------------------------------- |
| `+0x00` | u32           | count   | Record count; observed `5,123` (2026-09-27 client: `5,127`), equal to the offset count |
| `+0x04` | Record[count] | records | Variable-length records, back to back until end of file   |

### Record (variable: 14 bytes + model path and body, size from `characterobjectoffset.dbss`)

`data_offset` points at the record's own ID, unlike `characterstatic.dbss`, where it points just past it.

| Offset                | Type                               | Field          | Notes                                             |
| --------------------- | ---------------------------------- | -------------- | ------------------------------------------------- |
| `+0x00`               | u16                                | character_id   | Matches the offset-table key in all 5,123 records |
| `+0x02`               | u8                                 | object_kind    | Selects the record body; see [Object Kinds](#object-kinds) |
| `+0x03`               | u8                                 | is_siege_tent  | `1` on 45 records, all of kinds 4, 6 and 8 (forts, field HQs, command posts), else `0` |
| `+0x04`               | u8                                 | unknown_04     | `1` on 193 siege buildings (barricades, flame towers, hwachas, factories), else `0` |
| `+0x05`               | u8                                 | unknown_05     | Always `0`                                        |
| `+0x06`               | str8                               | model_path     | ASCII; see below                                  |
| `model_path+0x00`     | Furniture Body if object_kind = 2  | furniture_body | See Furniture Body                                |
| `furniture_body+0x00` | Structure Body if object_kind != 2 | structure_body | See Structure Body                                |

`model_path` extensions: `.pam` (4,479), `.srt` (622), `.r3m` (8), `.pcm` (5). A few paths carry a stray trailing character (`"srt "`, `"pam?"`).

### Furniture Body (variable: 624 bytes + action name and icon path)

The body of the `object_kind = 2` records (3,963 records). Follows `model_path`. Verified for every kind-2 record: walking these fields ends exactly at `data_size`.

| Offset             | Type            | Field       | Notes                                                                  |
| ------------------ | --------------- | ----------- | ---------------------------------------------------------------------- |
| `+0x000`           | Furniture Block | block       | Fixed block; mostly constant, see Furniture Block                      |
| `+0x22C`           | str8            | action_name | Empty in 3,887 records; else `OBJECT_BED_GoingToBed` (73) or `USE_BATHTUB_PREFARE` (3) |
| `action_name+0x00` | u32             | action_hash | `0` exactly when `action_name` is empty                                |
| `action_name+0x04` | str8            | icon_path   | Empty in 9 records                                                     |
| `icon_path+0x00`   | Furniture Tail  | tail        | See Furniture Tail                                                     |

### Furniture Block (556 bytes)

The 556-byte block is constant across all kind-2 records except for the bytes with values in Notes. The rows with "Constant" are zero or a fixed pattern of `1` flags and identity-like `1.0f` rows.

| Offset   | Type       | Field                        | Notes                                                                |
| -------- | ---------- | ---------------------------- | -------------------------------------------------------------------- |
| `+0x000` | bytes[16]  | unknown_000                  | Constant                                                             |
| `+0x010` | u8         | unknown_010                  | `1` (3,566), `0` (397)                                               |
| `+0x011` | bytes[128] | unknown_011                  | Constant                                                             |
| `+0x091` | u8         | unknown_091                  | `0` (3,936), `1` (27)                                                |
| `+0x092` | bytes[43]  | unknown_092                  | Constant                                                             |
| `+0x0BD` | u8         | unknown_0bd                  | 7 values; `0` (3,576), `1` (174), `5` (150), `2`, `10`, `4`, `3`     |
| `+0x0BE` | bytes[119] | unknown_0be                  | Constant                                                             |
| `+0x135` | u8         | installation_type            | `CppEnums.InstallationType`: `0` Default (1,486), `17` Buff (632), `10` Havest (374), `38` MansionTree (243) ... |
| `+0x136` | u8         | unknown_136                  | Constant                                                             |
| `+0x137` | u8         | reference_action_object_type | 11 values; `0` (3,797), `9` (145)                                    |
| `+0x138` | u8         | is_inside                    | Place flag: where it can be placed, `0` or `1`                       |
| `+0x139` | u8         | is_outside                   | Place flag                                                           |
| `+0x13A` | u8         | is_floor                     | Place flag                                                           |
| `+0x13B` | u8         | is_wall                      | Place flag                                                           |
| `+0x13C` | u8         | is_on_the_table              | Place flag                                                           |
| `+0x13D` | u8         | is_carpet                    | Place flag                                                           |
| `+0x13E` | bytes[3]   | unknown_13e                  | Constant                                                             |
| `+0x141` | f32        | installation_effect_radius   | Set on 9 records the server shares (client 3464)                     |
| `+0x145` | u8         | installation_effect_type     | Set on the same 9 records                                            |
| `+0x146` | bytes[16]  | unknown_146                  | Constant                                                             |
| `+0x156` | u32        | product_recipe_key           | `0`, or `57000 + n` on the 385 crop records                          |
| `+0x15A` | u32        | seed_recipe_key              | `0`, or `57100 + n` on the same records                              |
| `+0x15E` | u8         | explore_exp                  | `10` on the crop records, else `0`                                   |
| `+0x15F` | bytes[19]  | unknown_15f                  | Constant                                                             |
| `+0x172` | u64        | using_time                   | Set on 105 records the server shares (client 3464)                   |
| `+0x17A` | u16        | interior_point               | Interior points of the furniture; 136 values; `0` (809), `10` (498), `25`, `125`, `200`, `100`, `50` |
| `+0x17C` | bytes[154] | unknown_17c                  | Constant                                                             |
| `+0x216` | u32        | audio_bank_no                | Set on 30 records the server shares (client 3464)                    |
| `+0x21A` | u8         | unknown_21a                  | Constant                                                             |
| `+0x21B` | u8         | armor_material               | `100`, or `0` in 13 records (client 3483); see Field Names           |
| `+0x21C` | u16        | summon_character             | Character the object spawns; `0` when it spawns none                 |
| `+0x21E` | u16        | material_index               | Set on 103 records the server shares (client 3464)                   |
| `+0x220` | f32[3]     | relocate_position            | Where the character stands to use the object; set on 44 of them      |

On client 3464, `summon_character` names a character in 39 records:
Chicken Feed (1248) spawns Chicken (9099), Haystack (1245) spawns Dairy Cow
(9078), and the `[Oasis]` objects 18951 to 18977 spawn their characters 39801
to 39830 (`[Oasis] Ethan the Butler` 18977 -> `Oasis Ethan` 39830). An earlier
version of this doc read `+0x21B` as a u32, which merged this ID into it.

### Furniture Tail (48 bytes)

Observed values are from client 3464, 3,969 kind-2 records.

| Offset  | Type      | Field       | Notes                                                      |
| ------- | --------- | ----------- | ---------------------------------------------------------- |
| `+0x00` | bytes[40] | unknown_00  | Always zero                                                |
| `+0x28` | u32       | unknown_28  | Always `0xFFFFFFFF`                                        |
| `+0x2C` | u32       | repair_item | Item ID of the tool's repair item; `0` except in 6 records |

The 6 `repair_item` records are the crafting tools: Advanced Cooking Utensil
(1033) takes item 757406 Baermalo Hona's Advanced Cooking Repair Tool, and
Morning Light Traditional Alchemy Tool (1535) takes 757574 Morning Light
Traditional Alchemy Repair Tool.

### Structure Body (variable: 390 bytes + paths and hulls)

The body of the `object_kind != 2` records (1,160 records): houses, buildings, farms, tents, barricades and siege towers. Follows `model_path`. Verified for every structure record of client 3464: walking these fields ends exactly at `data_size` (`test_record_walk.py` walks all records of the installed client).

The tail is a House Tail when `hull_name` starts with `HH_`, else a Structure Suffix.

| Offset                 | Type                                  | Field                  | Notes                                                              |
| ---------------------- | ------------------------------------- | ---------------------- | ------------------------------------------------------------------ |
| `+0x00`                | str8                                  | hull_model_path        | The model path with a `_HH` or `_HH_NR` suffix                     |
| `hull_model_path+0x00` | str8                                  | hull_name              | Empty when `layer_count` is `0`; houses use `HH_<a>_<b>_<c>_<d>_<e>`, other structures a model name such as `Tower_AdBase_01_HH_NR` |
| `hull_name+0x00`       | u8                                    | unknown_flag           | `1` (1,085) or `0` (75)                                            |
| `hull_name+0x01`       | u32                                   | layer_count            | Hull layers that follow; `0` to `4`                                |
| `hull_name+0x05`       | u32                                   | unknown_b              | Always equal to `layer_count`                                      |
| `hull_name+0x09`       | Hull Layer[layer_count]               | layers                 | `layer_count` times, see Hull Layer                                |
| `layers+0x00`          | bytes[333]                            | unknown_block          | Fixed block, not decoded                                           |
| `layers+0x14D`         | str8                                  | material_path          | e.g. `Real_ETC/Material/Icon_Real_ETC_Material_Tent_N_00000000.dds`; never empty |
| `material_path+0x00`   | bytes[16]                             | unknown_after_material_path | Not decoded                                                        |
| `material_path+0x10`   | str8                                  | unknown_digits         | ASCII digits; see below                                            |
| `unknown_digits+0x00`  | House Tail if hull_name ^= HH_        | house              | When `hull_name` starts with `HH_`; see House Tail                 |
| `house+0x00`           | Structure Suffix if hull_name !^= HH_ | suffix                 | When `hull_name` does not start with `HH_`; see Structure Suffix   |

On client 3464, `layer_count` is `0` in 220 records (barricades, siege towers and
other guild structures, all with an empty `hull_name`), `1` in 820, `2` in 102,
`3` in 17 and `4` in 1. The records with two or more layers are houses (kinds
`1`, `5` and `9`). `unknown_digits` is `10` in every record except the 25 kind
`1` records, which hold 21 other values from `60` to `900`.

### Hull Layer (variable: 4 bytes + hulls)

| Offset  | Type             | Field      | Notes                            |
| ------- | ---------------- | ---------- | -------------------------------- |
| `+0x00` | u32              | hull_count | Hulls in this layer; `1` to `17` |
| `+0x04` | Hull[hull_count] | hulls      | See Hull                         |

On client 3464, 2,267 of the 2,321 hulls have 12 faces. Earlier versions of
this doc read `a`, `b` and `hull_count` as one header; the hull count repeats
per layer, so a walk that read it once ended short on every multi-layer house.

### Hull (variable: 4 bytes + faces)

| Offset  | Type             | Field      | Notes              |
| ------- | ---------------- | ---------- | ------------------ |
| `+0x00` | u32              | face_count | Faces in this hull |
| `+0x04` | Face[face_count] | faces      | See Face           |

### Face (140 bytes)

One bounding plane of a convex hull, the same 140-byte face as in
[`baseobject.bss`](../bss/baseobject_bss.md#face-140-bytes).

| Offset  | Type      | Field      | Notes                                                     |
| ------- | --------- | ---------- | --------------------------------------------------------- |
| `+0x00` | f32       | distance   | Plane distance: `-(normal . origin)` on every face        |
| `+0x04` | f32[3]    | normal     | Unit normal (x, y, z) of the plane                        |
| `+0x10` | f32[3]    | origin     | A point on the plane                                      |
| `+0x1C` | f32[9][3] | points     | Nine points (x, y, z), all on the plane; the first equals `origin` |
| `+0x88` | i32       | unknown_88 | `0` on every face                                         |

On client 3483 all 28,202 faces have a unit `normal`, a `distance` equal to
`-(normal . origin)` and nine `points` that satisfy the plane equation. The
hull layers of all 1,160 structure records are byte for byte the hull
layers of the `baseobject.bss` row with the same `character_id`.

### House Tail (variable: 234 bytes + text and paths)

The 865 records whose `hull_name` starts with `HH_` (client 3464: kinds `5`
(815), `1` (25), `9` (17) and `36` (8)).

| Offset                | Type       | Field                     | Notes                                                             |
| --------------------- | ---------- | ------------------------- | ----------------------------------------------------------------- |
| `+0x00`               | str16      | name_kr                   | UTF-16-LE Korean text; see below                                  |
| `name_kr+0x00`        | str16      | description_kr            | UTF-16-LE Korean text; see below                                  |
| `description_kr+0x00` | bytes[162] | unknown_description_kr_00 | Fixed block, not decoded                                          |
| `description_kr+0xA2` | str8       | icon_path                 | Set in all 865; e.g. `Icon/New_Icon/03_ETC/06_Housing/2101-1.dds` |
| `icon_path+0x00`      | str8       | icon_path_2               | Set in 17 records, as `<id>-2.dds` or `<id>_2.dds` next to slot 1 |
| `icon_path_2+0x00`    | str8       | unknown_path_3            | Empty in all 865                                                  |
| `unknown_path_3+0x00` | str8       | unknown_path_4            | Empty in all 865                                                  |
| `unknown_path_4+0x00` | bytes[24]  | unknown_unknown_path_4_00 | Not decoded                                                       |

`name_kr` is not the house name. On client 3464, 817 of the 865 records store
the same placeholder pair: `풋내기 대장장이의 집` ("Novice Blacksmith's House")
and a description of that house. Only these records carry their own text:

| Records | `name_kr`                                            | `description_kr`             |
| ------: | ---------------------------------------------------- | ---------------------------- |
| 25      | Guild house names, e.g. `벨리아 길드 하우스`           | `{TextBind:GUILDHOUSE_01}` to `_25` |
| 17      | Annex lines, e.g. `<PAColor0xFFf3d900>알사비의 별채<PAOldColor>\n주문서 : 신체 강화법\n일일 의뢰 : 토벌` | The placeholder story |
| 6       | `대저택`                                              | `대저택`                      |

`icon_path` names the record's own ID (`2101-1.dds`, `3823.dds`) in 686
records; the rest share one, such as the five Radiant Lands, Angavu and
Cheongsa Island houses 3874 to 3878 on `3873.dds`.

Earlier versions of this doc called `unknown_description_kr_00` `house_block` and `unknown_unknown_path_4_00` `house_tail`.

### Structure Suffix (234 bytes)

The 295 records whose `hull_name` does not start with `HH_` end in a fixed
234-byte block. Bytes `+0` to `+15` are zero, `+152` is a u16 `0xFFFF` and
`+226` a u32 `0xFFFFFFFF` in all of them; the u8 at `+148` is `0` in the 220
records with an empty `hull_name` and `1` in the other 75. The rest is not
decoded.

| Offset  | Type       | Field      | Notes                                                    |
| ------- | ---------- | ---------- | -------------------------------------------------------- |
| `+0x00` | bytes[16]  | unknown_00 | Always `0`                                               |
| `+0x10` | bytes[132] | unknown_10 | Not decoded                                              |
| `+0x94` | u8         | unknown_94 | `0` with an empty `hull_name` (220), `1` in the other 75 |
| `+0x95` | bytes[3]   | unknown_95 | Not decoded                                              |
| `+0x98` | u16        | unknown_98 | Always `0xFFFF`                                          |
| `+0x9A` | bytes[72]  | unknown_9a | Not decoded                                              |
| `+0xE2` | u32        | unknown_e2 | Always `0xFFFFFFFF`                                      |
| `+0xE6` | bytes[4]   | unknown_e6 | Not decoded                                              |

### `characterobjectoffset.dbss`

PABR index with a 10-byte row, because the key is a u16.

| Offset              | Type             | Field        | Notes                                                           |
| ------------------- | ---------------- | ------------ | --------------------------------------------------------------- |
| `+0x00`             | char[4]          | magic        | `PABR` (ASCII)                                                  |
| `+0x04`             | u32              | count        | Number of rows; observed `5,123` (2026-09-27 client: `5,127`)   |
| `+0x08`             | Index Row[count] | rows         | See Index Row                                                   |
| `rows+0x00`         | String Table     | string_table | Empty; observed zero                                            |
| `string_table+0x00` | u32              | end_of_rows  | Byte offset after rows; `8 + count * 10`; observed `51,238`     |
| `string_table+0x04` | u32              | zero         | Observed zero                                                   |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                                 |
| ------- | ---- | ------------ | ----------------------------------------------------- |
| `+0x00` | u16  | character_id | Unique; observed range `1001` to `19617`, unsorted    |
| `+0x02` | u32  | data_offset  | Absolute offset of the record in the main file        |
| `+0x06` | u32  | data_size    | Record size; observed `678` to `56,750`, median `786` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                          |
| ------- | ------------------ | ------------ | ------------------------------ |
| `+0x00` | u32                | string_count | `0`                            |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none here |

## Layout 1

On client 1784 the Furniture Block was 50 bytes shorter: `unknown_092` 4
bytes, `unknown_0be` 40 and `unknown_15f` 2, and the two recipe keys were
u16. In the Structure Body `unknown_block` was 285 bytes and
`unknown_after_material_path` 14. Two kind-5 records (3821 and 3822) have an
empty `hull_model_path` and `hull_name` and still end in a House Tail. Field names keep
Layout 2's offsets, so `installation_type` sits at `+0x109` here. The parser
reads only Layout 2.

### Furniture Body (variable: 574 bytes + action name and icon path)

| Offset             | Type            | Field       | Notes |
| ------------------ | --------------- | ----------- | ----- |
| `+0x000`           | Furniture Block | block       |       |
| `+0x1FA`           | str8            | action_name |       |
| `action_name+0x00` | u32             | action_hash |       |
| `action_name+0x04` | str8            | icon_path   |       |
| `icon_path+0x00`   | Furniture Tail  | tail        |       |

### Furniture Block (506 bytes)

| Offset   | Type       | Field                        | Notes |
| -------- | ---------- | ---------------------------- | ----- |
| `+0x000` | bytes[16]  | unknown_000                  |       |
| `+0x010` | u8         | unknown_010                  |       |
| `+0x011` | bytes[128] | unknown_011                  |       |
| `+0x091` | u8         | unknown_091                  |       |
| `+0x092` | bytes[39]  | unknown_092                  |       |
| `+0x0B9` | u8         | unknown_0bd                  |       |
| `+0x0BA` | bytes[79]  | unknown_0be                  |       |
| `+0x109` | u8         | installation_type            |       |
| `+0x10A` | u8         | unknown_136                  |       |
| `+0x10B` | u8         | reference_action_object_type |       |
| `+0x10C` | u8         | is_inside                    |       |
| `+0x10D` | u8         | is_outside                   |       |
| `+0x10E` | u8         | is_floor                     |       |
| `+0x10F` | u8         | is_wall                      |       |
| `+0x110` | u8         | is_on_the_table              |       |
| `+0x111` | u8         | is_carpet                    |       |
| `+0x112` | bytes[3]   | unknown_13e                  |       |
| `+0x115` | f32        | installation_effect_radius   |       |
| `+0x119` | u8         | installation_effect_type     |       |
| `+0x11A` | bytes[16]  | unknown_146                  |       |
| `+0x12A` | u16        | product_recipe_key           | Equals Layout 2's u32 in all 2,542 kind-2 records both clients share |
| `+0x12C` | u16        | seed_recipe_key              |       |
| `+0x12E` | u8         | explore_exp                  |       |
| `+0x12F` | bytes[17]  | unknown_15f                  |       |
| `+0x140` | u64        | using_time                   |       |
| `+0x148` | u16        | interior_point               |       |
| `+0x14A` | bytes[154] | unknown_17c                  |       |
| `+0x1E4` | u32        | audio_bank_no                |       |
| `+0x1E8` | u8         | unknown_21a                  |       |
| `+0x1E9` | u8         | armor_material               |       |
| `+0x1EA` | u16        | summon_character             |       |
| `+0x1EC` | u16        | material_index               |       |
| `+0x1EE` | f32[3]     | relocate_position            |       |

Which of the constant bytes inside `unknown_092` and `unknown_0be` the
newer client added cannot be told from the data; the varying fields on both
sides of each run line up in all 2,542 shared kind-2 records.

### Structure Body (variable: 340 bytes + paths, hulls and tail)

The tail is a House Tail when `hull_name` starts with `HH_` or
`hull_model_path` is empty (records 3821 and 3822 on client 1784), else a
Structure Suffix.

| Offset                 | Type                                                         | Field                       | Notes |
| ---------------------- | ------------------------------------------------------------ | --------------------------- | ----- |
| `+0x00`                | str8                                                         | hull_model_path             |       |
| `hull_model_path+0x00` | str8                                                         | hull_name                   |       |
| `hull_name+0x00`       | u8                                                           | unknown_flag                |       |
| `hull_name+0x01`       | u32                                                          | layer_count                 |       |
| `hull_name+0x05`       | u32                                                          | unknown_b                   |       |
| `hull_name+0x09`       | Hull Layer[layer_count]                                      | layers                      |       |
| `layers+0x00`          | bytes[285]                                                   | unknown_block               |       |
| `layers+0x11D`         | str8                                                         | material_path               |       |
| `material_path+0x00`   | bytes[14]                                                    | unknown_after_material_path |       |
| `material_path+0x0E`   | str8                                                         | unknown_digits              |       |
| `unknown_digits+0x00`  | House Tail if hull_name ^= HH_ or hull_model_path = ""        | house                       |       |
| `house+0x00`           | Structure Suffix if hull_name !^= HH_ and hull_model_path != "" | suffix                    |       |

## Icon Path

The icon index does not walk the record body; it scans each record for the first `icon/...(dds|png)` match. 4,817 of 5,123 records contain one, and 17 contain more than one; the index keeps the first. Material paths (`Real_ETC/Material/Icon_...`) have no `icon/` folder, so the scan skips them. On client 3464, the 17 records with two matches are the houses with an `icon_path_2`, and the first match is their `icon_path`.

The walked `icon_path` (furniture body, or slot 1 of the house tail) gives the same PAZ path as the scan for 5,124 of the 5,129 records of client 3464. On the other five the walked path names no file the client ships, so the index keeps the scan:

| Character | Stored `icon_path`                                       | Scan                                    |
| --------- | -------------------------------------------------------- | --------------------------------------- |
| 15267 to 15269 | `Icon/New_Icon/03_ETC/06_Housing/Rot_Island_OBJ_Deco_20.dds?` (`_21`, `_22`) | Drops the stray `?`; the `.dds` file exists |
| 15031     | `Icon/New_Icon/03_ETC/06_Housing/InHouse_Ber_DPFO_Jukebox_01.pam` | No match, so no own icon |
| 4758      | `Icon/New_Icon/03_ETC/06_Housing/Inhouse_Cash_View_035_SetBdds` | No match, so no own icon |

Two stored forms, which resolve to the same PAZ folder:

| Stored prefix | Records | PAZ path                         |
| ------------- | ------: | -------------------------------- |
| `Icon/`       |   4,622 | `ui_texture/` + stored path      |
| `New_Icon/`   |     195 | `ui_texture/icon/` + stored path |

Paths are lowercased to match PAZ entries. 87% of icons live under `icon/new_icon/03_etc/06_housing`, and most of the rest under `07_productmaterial`.

## Borrowed Item Icons

Many objects store no icon (fences, gardens and tents keep only a material path) or one the client does not ship. The item that places the object usually has a working one, and `itemenchant.dbss` names the placed character at `+0xAA`. When the character icon index is built, a character without a working icon takes its item's icon, if that file exists; a working own icon always wins.

```text
character 2053 [Event] Fence  -> no icon stored
item 58011 [Event] Fence      -> places 2053, icon 06_housing/00058003.dds
character 2053 icon           -> ui_texture/icon/new_icon/03_etc/06_housing/00058003.dds
```

## Object Kinds

Grouped by model folder. Kinds `0` to `9` are the members of `gc::ObjectKind` in the 2016 client; the later kinds have no name. The handler shows the name next to the number.

| Kind | Records | Observed objects                                        |
| ---- | ------: | ------------------------------------------------------- |
| `2` Installation |   3,963 | Furniture, crafting tools and crops (`Interior_House`, `Crafting`) |
| `5` InnRoom |     815 | Town buildings and farms (`*_STR_House_*`, `Products/Farm`) |
| `3` Barricade |      36 | Barricades                                              |
| `8` VillageTent |      28 | Guild citadel small sets                                |
| `1` FixedHouse |      25 | Houses                                                  |
| `0` PersonalTent |      17 | Farming fences and gardens (14, e.g. `[Event] Fence`), plus two tents and a drilling facility; models reuse `Tent/Minifarm_Housing_*` |
| `9` Villa |      17 | Valencia extra houses                                   |
| `10` to `15`, `17` to `19`, `22` to `26`, `29`, `35` | 1 to 23 each | One guild tower or siege structure type each |
| `4` KingTent, `6` LordTent, `7` Trap, `20`, `21`, `27`, `28`, `34`, `36`, `37` | 4 to 16 each | Citadel sets, mines, barricade doors, mixed siege objects, mansion bases |

## Notes

- This file stores icon paths for 4,817 of the 24,418 character IDs in `characterstaticoffset.dbss`; 4,608 of them exist in the PAZ. The rest of the IDs are NPCs, monsters and similar entries with no world-object record.
- Borrowing item icons raises the character index to 6,157 entries, 6,068 of them working (24.9% of all character IDs, up from 18.9%); pets gain icons this way too. 89 paths still point at icons the client does not ship; fix those with `icon_overrides.json`.
- Before the `New_Icon/` form was handled, those 195 records resolved to `ui_texture/icon/03_etc/...`, dropping the `new_icon/` level, and all of them pointed at files that do not exist.
- The `CHARACTER_ITEM` index (the item that places or summons the character, from `itemenchant.dbss` `+0xAA`) links 3,964 of the 5,127 records on client 3458.
- LOC type `6` names 5,020 of the 5,123 records; most of the rest are mansion props (`DecoPropMansion`).
- `product_recipe_key`/`seed_recipe_key` are not item IDs: item `57001` is a Striker costume, while character `1201` with `product_recipe_key = 57001` is Pepper Crop. The 2016 client points both at `gc::ItemExchangeSourceStaticStatus`, the item exchange recipes.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::ObjectStaticStatus` starts with `_objectKind`, `_isSiegeTent` and `_isSiegeOrFortressTent`, and further on holds `_installationType`, `_subInstallationType`, `_installationActionNumber`, `_installablePlaceFlag[6]`, `_productionFacilityFlag[3]`, `_installationEffectRadius`, `_installationEffectType`, the recipe keys, `_exploreExp`, `_usingTime`, `_interiorSensePoint`, `_audioBankNo`, `_armorMaterial`, `_summonCharacterKey`, `_materialIndexForInstallation`, `_relocatePosForUsing` and `_usingAction`. The furniture block stores its named fields in that order and ends right before `action_name`. The server-side `Object_Table` of a private server on client 519 shares 2,041 furniture records with client 3464:

| Field                        | `Object_Table` column        | Matching non-zero rows |
| ---------------------------- | ---------------------------- | ---------------------: |
| installation_type            | `InstallationType`           | 1,198 of 1,198         |
| reference_action_object_type | `ReferenceActionObjectType`  | 134 of 134             |
| place flags                  | `IsInside`, `IsOutside`, `IsFloor`, `IsWall`, `IsOnTheTable`, `IsCarpet` | 2,035 to 2,041 of 2,041 rows |
| installation_effect_radius, installation_effect_type | `Effect_Radius`, `Effect_Type` | 9 of 9 |
| product_recipe_key, seed_recipe_key | `ProductRecipe`, `SeedRecipe` | 263 of 263, 244 of 244 |
| explore_exp                  | `ExploreExp`                 | 263 of 263             |
| using_time                   | `UsingTime`                  | 105 of 105             |
| interior_point               | `InteriorPoint`              | 1,659 of 1,664         |
| audio_bank_no                | `AudioBankNo`                | 30 of 30               |
| summon_character             | `SummonCharacterKey`         | 27 of 27               |
| material_index               | `MaterialIndex`              | 103 of 103             |
| relocate_position            | `RelocatePosX`, `Y`, `Z`     | 2,041 of 2,041 rows    |

`armor_material` sits where the 2016 order has `_armorMaterial` and holds the same value as `baseobject.bss` `armor_material` on all 3,971 furniture records of client 3483 (`100` on 3,958, `0` on 13). That file takes the name from the client 1784 `Object_Table` column `ArmorMaterial`, which is empty on most rows and compiles to `100`; the client 519 table above holds `0` in that column on every row.

`installation_type` follows `CppEnums.InstallationType` in `global_define_cpp_enum.luac` (`0` Default to `39` EventPersonalTent). `is_siege_tent` has no server column; it is named from the 2016 order and is set only on the King, Lord and Village tent kinds.

## Open Questions

### Furniture Block Fields

Most varying bytes now have names (see Field Names). `unknown_010`, `unknown_091` and `unknown_0bd` match no server column.

### Structure Body Blocks

The walk crosses `unknown_block` (333 bytes), `unknown_after_material_path` (16), `unknown_description_kr_00` (162), `unknown_unknown_path_4_00` (24) and the 234-byte structure suffix without decoding them. Also open: whether a hull layer is a house floor (only houses have two or more), what `unknown_flag` and `unknown_b` select, and what the 21 `unknown_digits` values of the kind `1` records (`60` to `900`) measure. `unknown_88` of every face is `0`, where the 2016 `pa::PlaneExtended` has `_negNormBitMask`.

### Later Kind Names

Kinds `10` to `37` came after the 2016 `gc::ObjectKind` and have no name in any client table found so far. `unknown_04` (set on siege buildings, not on the forts) does not fit the 2016 `_isSiegeOrFortressTent` that sits at its place, and the house `hull_name` parts are also unexplained.
