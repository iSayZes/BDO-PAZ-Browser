# `actionverificationindex.dbss` Format

## Purpose

The class types that have an action verification list: one record per class
type, keyed by the class type. On clients 1784 and 3474 the file holds 12
records, class types `52`, `53`, `55`, `58`, `60`, `61`, `63`, `65`, `69`,
`71`, `81` and `87`, which LOC type 21 names Jordine, Peony, Ahon Kirus,
Povios, Syaki, Sanmyoung, Nelydormin, Elgriffin, Orwen, `[PH] 12`, `[PH] 22`
and `[PH] 28`. The source sheets (see Field Names) also give each class type
a list of action names with an index; every list is empty in the client 1784
sheets, and the client 1784 and 3474 files hold no list data past the class
type. Companion `actionverificationindexoffset.dbss` lists where every record
sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                 | Bytes | Records               | Row bytes |
| ------ | -------------- | ------------------------------------ | ----- | --------------------- | --------- |
| 1      | 1360 and later | `actionverificationindex.dbss`       | 112   | 12 Payload, 12 Record | 8         |
| 1      | 1360 and later | `actionverificationindexoffset.dbss` | 148   | 12 Offset Row         | 12        |

| Layout | File                                 | Known          | Unknown      |
| ------ | ------------------------------------ | -------------- | ------------ |
| 1      | `actionverificationindex.dbss`       | 28 B (25.0%)   | 84 B (75.0%) |
| 1      | `actionverificationindexoffset.dbss` | 148 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `f3a333a30a7f`  |
| 3482   | Layout 1             | `f3a333a30a7f`  |
| 3474   | Layout 1             | `f3a333a30a7f`  |
| 3473   | Layout 1             | `f3a333a30a7f`  |
| 3464   | Layout 1             | `f3a333a30a7f`  |
| 3458   | Layout 1             | `f3a333a30a7f`  |
| 3454   | Layout 1             | `f3a333a30a7f`  |
| 3444   | Layout 1             | `f3a333a30a7f`  |
| 3435   | Layout 1             | `f3a333a30a7f`  |
| 3426   | Layout 1             | `f3a333a30a7f`  |
| 3418   | Layout 1             | `f3a333a30a7f`  |
| 3412   | Layout 1             | `f3a333a30a7f`  |
| 3402   | Layout 1             | `f3a333a30a7f`  |
| 3396   | Layout 1             | `f3a333a30a7f`  |
| 3387   | Layout 1             | `f3a333a30a7f`  |
| 3381   | Layout 1             | `f3a333a30a7f`  |
| 3373   | Layout 1             | `f3a333a30a7f`  |
| 3364   | Layout 1             | `f3a333a30a7f`  |
| 3356   | Layout 1             | `f3a333a30a7f`  |
| 3349   | Layout 1             | `f3a333a30a7f`  |
| 3342   | Layout 1             | `f3a333a30a7f`  |
| 3335   | Layout 1             | `f3a333a30a7f`  |
| 3326   | Layout 1             | `f3a333a30a7f`  |
| 3321   | Layout 1             | `f3a333a30a7f`  |
| 3314   | Layout 1             | `f3a333a30a7f`  |
| 3303   | Layout 1             | `f3a333a30a7f`  |
| 3302   | Layout 1             | `f3a333a30a7f`  |
| 3293   | Layout 1             | `f3a333a30a7f`  |
| 3283   | Layout 1             | `f3a333a30a7f`  |
| 3275   | Layout 1             | `f3a333a30a7f`  |
| 3267   | Layout 1             | `f3a333a30a7f`  |
| 3258   | Layout 1             | `f3a333a30a7f`  |
| 3251   | Layout 1             | `f3a333a30a7f`  |
| 3242   | Layout 1             | `f3a333a30a7f`  |
| 3235   | Layout 1             | `f3a333a30a7f`  |
| 3229   | Layout 1             | `f3a333a30a7f`  |
| 3212   | Layout 1             | `f3a333a30a7f`  |
| 3203   | Layout 1             | `f3a333a30a7f`  |
| 3193   | Layout 1             | `f3a333a30a7f`  |
| 3186   | Layout 1             | `f3a333a30a7f`  |
| 3177   | Layout 1             | `f3a333a30a7f`  |
| 3169   | Layout 1             | `f3a333a30a7f`  |
| 3158   | Layout 1             | `f3a333a30a7f`  |
| 3151   | Layout 1             | `f3a333a30a7f`  |
| 3144   | Layout 1             | `f3a333a30a7f`  |
| 3133   | Layout 1             | `f3a333a30a7f`  |
| 3125   | Layout 1             | `f3a333a30a7f`  |
| 3118   | Layout 1             | `f3a333a30a7f`  |
| 3111   | Layout 1             | `f3a333a30a7f`  |
| 3103   | Layout 1             | `f3a333a30a7f`  |
| 3095   | Layout 1             | `f3a333a30a7f`  |
| 3086   | Layout 1             | `f3a333a30a7f`  |
| 3072   | Layout 1             | `f3a333a30a7f`  |
| 3062   | Layout 1             | `f3a333a30a7f`  |
| 3052   | Layout 1             | `f3a333a30a7f`  |
| 3045   | Layout 1             | `f3a333a30a7f`  |
| 3037   | Layout 1             | `f3a333a30a7f`  |
| 3030   | Layout 1             | `f3a333a30a7f`  |
| 3021   | Layout 1             | `f3a333a30a7f`  |
| 3012   | Layout 1             | `f3a333a30a7f`  |
| 3002   | Layout 1             | `f3a333a30a7f`  |
| 2995   | Layout 1             | `f3a333a30a7f`  |
| 2987   | Layout 1             | `f3a333a30a7f`  |
| 2978   | Layout 1             | `f3a333a30a7f`  |
| 2970   | Layout 1             | `f3a333a30a7f`  |
| 2959   | Layout 1             | `f3a333a30a7f`  |
| 2951   | Layout 1             | `f3a333a30a7f`  |
| 2942   | Layout 1             | `f3a333a30a7f`  |
| 2935   | Layout 1             | `f3a333a30a7f`  |
| 2932   | Layout 1             | `f3a333a30a7f`  |
| 2923   | Layout 1             | `f3a333a30a7f`  |
| 2919   | Layout 1             | `f3a333a30a7f`  |
| 2907   | Layout 1             | `f3a333a30a7f`  |
| 2900   | Layout 1             | `f3a333a30a7f`  |
| 2891   | Layout 1             | `f3a333a30a7f`  |
| 2882   | Layout 1             | `f3a333a30a7f`  |
| 2872   | Layout 1             | `f3a333a30a7f`  |
| 2863   | Layout 1             | `f3a333a30a7f`  |
| 2855   | Layout 1             | `f3a333a30a7f`  |
| 2849   | Layout 1             | `f3a333a30a7f`  |
| 2844   | Layout 1             | `f3a333a30a7f`  |
| 2834   | Layout 1             | `f3a333a30a7f`  |
| 2825   | Layout 1             | `f3a333a30a7f`  |
| 2819   | Layout 1             | `f3a333a30a7f`  |
| 2811   | Layout 1             | `f3a333a30a7f`  |
| 2803   | Layout 1             | `f3a333a30a7f`  |
| 2794   | Layout 1             | `f3a333a30a7f`  |
| 2783   | Layout 1             | `f3a333a30a7f`  |
| 2774   | Layout 1             | `f3a333a30a7f`  |
| 2765   | Layout 1             | `f3a333a30a7f`  |
| 2756   | Layout 1             | `f3a333a30a7f`  |
| 2750   | Layout 1             | `f3a333a30a7f`  |
| 2743   | Layout 1             | `f3a333a30a7f`  |
| 2736   | Layout 1             | `f3a333a30a7f`  |
| 2726   | Layout 1             | `f3a333a30a7f`  |
| 2717   | Layout 1             | `f3a333a30a7f`  |
| 2709   | Layout 1             | `f3a333a30a7f`  |
| 2703   | Layout 1             | `f3a333a30a7f`  |
| 2695   | Layout 1             | `f3a333a30a7f`  |
| 2684   | Layout 1             | `f3a333a30a7f`  |
| 2672   | Layout 1             | `f3a333a30a7f`  |
| 2665   | Layout 1             | `f3a333a30a7f`  |
| 2657   | Layout 1             | `f3a333a30a7f`  |
| 2649   | Layout 1             | `f3a333a30a7f`  |
| 2644   | Layout 1             | `f3a333a30a7f`  |
| 2637   | Layout 1             | `f3a333a30a7f`  |
| 2629   | Layout 1             | `f3a333a30a7f`  |
| 2619   | Layout 1             | `f3a333a30a7f`  |
| 2612   | Layout 1             | `f3a333a30a7f`  |
| 2606   | Layout 1             | `f3a333a30a7f`  |
| 2602   | Layout 1             | `f3a333a30a7f`  |
| 2601   | Layout 1             | `f3a333a30a7f`  |
| 2592   | Layout 1             | `f3a333a30a7f`  |
| 2583   | Layout 1             | `f3a333a30a7f`  |
| 2575   | Layout 1             | `f3a333a30a7f`  |
| 2567   | Layout 1             | `f3a333a30a7f`  |
| 2560   | Layout 1             | `f3a333a30a7f`  |
| 2553   | Layout 1             | `f3a333a30a7f`  |
| 2545   | Layout 1             | `f3a333a30a7f`  |
| 2538   | Layout 1             | `f3a333a30a7f`  |
| 2529   | Layout 1             | `f3a333a30a7f`  |
| 2519   | Layout 1             | `f3a333a30a7f`  |
| 2513   | Layout 1             | `f3a333a30a7f`  |
| 2510   | Layout 1             | `f3a333a30a7f`  |
| 2507   | Layout 1             | `f3a333a30a7f`  |
| 2503   | Layout 1             | `f3a333a30a7f`  |
| 2498   | Layout 1             | `f3a333a30a7f`  |
| 2492   | Layout 1             | `f3a333a30a7f`  |
| 2487   | Layout 1             | `f3a333a30a7f`  |
| 2480   | Layout 1             | `f3a333a30a7f`  |
| 2474   | Layout 1             | `f3a333a30a7f`  |
| 2468   | Layout 1             | `f3a333a30a7f`  |
| 2460   | Layout 1             | `f3a333a30a7f`  |
| 2453   | Layout 1             | `f3a333a30a7f`  |
| 2444   | Layout 1             | `f3a333a30a7f`  |
| 2438   | Layout 1             | `f3a333a30a7f`  |
| 2434   | Layout 1             | `f3a333a30a7f`  |
| 2429   | Layout 1             | `f3a333a30a7f`  |
| 2421   | Layout 1             | `f3a333a30a7f`  |
| 2414   | Layout 1             | `f3a333a30a7f`  |
| 2407   | Layout 1             | `f3a333a30a7f`  |
| 2401   | Layout 1             | `f3a333a30a7f`  |
| 2397   | Layout 1             | `f3a333a30a7f`  |
| 2393   | Layout 1             | `f3a333a30a7f`  |
| 2384   | Layout 1             | `f3a333a30a7f`  |
| 2378   | Layout 1             | `f3a333a30a7f`  |
| 2372   | Layout 1             | `f3a333a30a7f`  |
| 2358   | Layout 1             | `f3a333a30a7f`  |
| 2352   | Layout 1             | `f3a333a30a7f`  |
| 2347   | Layout 1             | `f3a333a30a7f`  |
| 2343   | Layout 1             | `f3a333a30a7f`  |
| 2335   | Layout 1             | `f3a333a30a7f`  |
| 2327   | Layout 1             | `f3a333a30a7f`  |
| 2324   | Layout 1             | `f3a333a30a7f`  |
| 2319   | Layout 1             | `f3a333a30a7f`  |
| 2313   | Layout 1             | `f3a333a30a7f`  |
| 2308   | Layout 1             | `f3a333a30a7f`  |
| 2302   | Layout 1             | `f3a333a30a7f`  |
| 2295   | Layout 1             | `f3a333a30a7f`  |
| 2290   | Layout 1             | `f3a333a30a7f`  |
| 2284   | Layout 1             | `f3a333a30a7f`  |
| 2276   | Layout 1             | `f3a333a30a7f`  |
| 2269   | Layout 1             | `f3a333a30a7f`  |
| 2259   | Layout 1             | `f3a333a30a7f`  |
| 2250   | Layout 1             | `f3a333a30a7f`  |
| 2243   | Layout 1             | `f3a333a30a7f`  |
| 2235   | Layout 1             | `f3a333a30a7f`  |
| 2229   | Layout 1             | `f3a333a30a7f`  |
| 2224   | Layout 1             | `f3a333a30a7f`  |
| 2218   | Layout 1             | `f3a333a30a7f`  |
| 2215   | Layout 1             | `f3a333a30a7f`  |
| 2207   | Layout 1             | `f3a333a30a7f`  |
| 2203   | Layout 1             | `f3a333a30a7f`  |
| 2196   | Layout 1             | `f3a333a30a7f`  |
| 2192   | Layout 1             | `f3a333a30a7f`  |
| 2189   | Layout 1             | `f3a333a30a7f`  |
| 2183   | Layout 1             | `f3a333a30a7f`  |
| 2179   | Layout 1             | `f3a333a30a7f`  |
| 2171   | Layout 1             | `f3a333a30a7f`  |
| 2163   | Layout 1             | `f3a333a30a7f`  |
| 2156   | Layout 1             | `f3a333a30a7f`  |
| 2151   | Layout 1             | `f3a333a30a7f`  |
| 2147   | Layout 1             | `f3a333a30a7f`  |
| 2142   | Layout 1             | `f3a333a30a7f`  |
| 2138   | Layout 1             | `f3a333a30a7f`  |
| 2134   | Layout 1             | `f3a333a30a7f`  |
| 2130   | Layout 1             | `f3a333a30a7f`  |
| 2122   | Layout 1             | `f3a333a30a7f`  |
| 2107   | Layout 1             | `f3a333a30a7f`  |
| 2098   | Layout 1             | `f3a333a30a7f`  |
| 2089   | Layout 1             | `f3a333a30a7f`  |
| 2081   | Layout 1             | `f3a333a30a7f`  |
| 2073   | Layout 1             | `f3a333a30a7f`  |
| 2067   | Layout 1             | `f3a333a30a7f`  |
| 2063   | Layout 1             | `f3a333a30a7f`  |
| 2059   | Layout 1             | `f3a333a30a7f`  |
| 2052   | Layout 1             | `f3a333a30a7f`  |
| 2044   | Layout 1             | `f3a333a30a7f`  |
| 2039   | Layout 1             | `f3a333a30a7f`  |
| 2032   | Layout 1             | `f3a333a30a7f`  |
| 2025   | Layout 1             | `f3a333a30a7f`  |
| 2011   | Layout 1             | `f3a333a30a7f`  |
| 2005   | Layout 1             | `f3a333a30a7f`  |
| 2000   | Layout 1             | `f3a333a30a7f`  |
| 1996   | Layout 1             | `f3a333a30a7f`  |
| 1991   | Layout 1             | `f3a333a30a7f`  |
| 1985   | Layout 1             | `f3a333a30a7f`  |
| 1980   | Layout 1             | `f3a333a30a7f`  |
| 1969   | Layout 1             | `f3a333a30a7f`  |
| 1964   | Layout 1             | `f3a333a30a7f`  |
| 1958   | Layout 1             | `f3a333a30a7f`  |
| 1950   | Layout 1             | `f3a333a30a7f`  |
| 1945   | Layout 1             | `f3a333a30a7f`  |
| 1937   | Layout 1             | `f3a333a30a7f`  |
| 1933   | Layout 1             | `f3a333a30a7f`  |
| 1927   | Layout 1             | `f3a333a30a7f`  |
| 1921   | Layout 1             | `f3a333a30a7f`  |
| 1914   | Layout 1             | `f3a333a30a7f`  |
| 1908   | Layout 1             | `f3a333a30a7f`  |
| 1897   | Layout 1             | `f3a333a30a7f`  |
| 1892   | Layout 1             | `f3a333a30a7f`  |
| 1886   | Layout 1             | `f3a333a30a7f`  |
| 1881   | Layout 1             | `f3a333a30a7f`  |
| 1871   | Layout 1             | `f3a333a30a7f`  |
| 1866   | Layout 1             | `f3a333a30a7f`  |
| 1862   | Layout 1             | `f3a333a30a7f`  |
| 1854   | Layout 1             | `f3a333a30a7f`  |
| 1846   | Layout 1             | `f3a333a30a7f`  |
| 1838   | Layout 1             | `f3a333a30a7f`  |
| 1832   | Layout 1             | `f3a333a30a7f`  |
| 1826   | Layout 1             | `f3a333a30a7f`  |
| 1822   | Layout 1             | `f3a333a30a7f`  |
| 1818   | Layout 1             | `f3a333a30a7f`  |
| 1804   | Layout 1             | `f3a333a30a7f`  |
| 1794   | Layout 1             | `f3a333a30a7f`  |
| 1790   | Layout 1             | `f3a333a30a7f`  |
| 1784   | Layout 1             | `f3a333a30a7f`  |
| 1774   | Layout 1             | `f3a333a30a7f`  |
| 1771   | Layout 1             | `f3a333a30a7f`  |
| 1762   | Layout 1             | `f3a333a30a7f`  |
| 1759   | Layout 1             | `f3a333a30a7f`  |
| 1754   | Layout 1             | `f3a333a30a7f`  |
| 1749   | Layout 1             | `f3a333a30a7f`  |
| 1743   | Layout 1             | `f3a333a30a7f`  |
| 1737   | Layout 1             | `f3a333a30a7f`  |
| 1731   | Layout 1             | `f3a333a30a7f`  |
| 1725   | Layout 1             | `f3a333a30a7f`  |
| 1717   | Layout 1             | `f3a333a30a7f`  |
| 1710   | Layout 1             | `f3a333a30a7f`  |
| 1704   | Layout 1             | `f3a333a30a7f`  |
| 1698   | Layout 1             | `f3a333a30a7f`  |
| 1690   | Layout 1             | `f3a333a30a7f`  |
| 1685   | Layout 1             | `f3a333a30a7f`  |
| 1680   | Layout 1             | `f3a333a30a7f`  |
| 1674   | Layout 1             | `f3a333a30a7f`  |
| 1668   | Layout 1             | `f3a333a30a7f`  |
| 1659   | Layout 1             | `f3a333a30a7f`  |
| 1649   | Layout 1             | `f3a333a30a7f`  |
| 1642   | Layout 1             | `f3a333a30a7f`  |
| 1636   | Layout 1             | `f3a333a30a7f`  |
| 1628   | Layout 1             | `f3a333a30a7f`  |
| 1622   | Layout 1             | `f3a333a30a7f`  |
| 1614   | Layout 1             | `f3a333a30a7f`  |
| 1608   | Layout 1             | `f3a333a30a7f`  |
| 1602   | Layout 1             | `f3a333a30a7f`  |
| 1598   | Layout 1             | `f3a333a30a7f`  |
| 1594   | Layout 1             | `f3a333a30a7f`  |
| 1590   | Layout 1             | `f3a333a30a7f`  |
| 1587   | Layout 1             | `f3a333a30a7f`  |
| 1584   | Layout 1             | `f3a333a30a7f`  |
| 1579   | Layout 1             | `f3a333a30a7f`  |
| 1572   | Layout 1             | `f3a333a30a7f`  |
| 1565   | Layout 1             | `f3a333a30a7f`  |
| 1559   | Layout 1             | `f3a333a30a7f`  |
| 1554   | Layout 1             | `f3a333a30a7f`  |
| 1547   | Layout 1             | `f3a333a30a7f`  |
| 1537   | Layout 1             | `f3a333a30a7f`  |
| 1529   | Layout 1             | `f3a333a30a7f`  |
| 1524   | Layout 1             | `f3a333a30a7f`  |
| 1519   | Layout 1             | `f3a333a30a7f`  |
| 1509   | Layout 1             | `f3a333a30a7f`  |
| 1506   | Layout 1             | `f3a333a30a7f`  |
| 1504   | Layout 1             | `f3a333a30a7f`  |
| 1500   | Layout 1             | `f3a333a30a7f`  |
| 1493   | Layout 1             | `f3a333a30a7f`  |
| 1489   | Layout 1             | `f3a333a30a7f`  |
| 1485   | Layout 1             | `f3a333a30a7f`  |
| 1481   | Layout 1             | `f3a333a30a7f`  |
| 1474   | Layout 1             | `f3a333a30a7f`  |
| 1466   | Layout 1             | `f3a333a30a7f`  |
| 1462   | Layout 1             | `f3a333a30a7f`  |
| 1459   | Layout 1             | `f3a333a30a7f`  |
| 1453   | Layout 1             | `f3a333a30a7f`  |
| 1450   | Layout 1             | `f3a333a30a7f`  |
| 1445   | Layout 1             | `f3a333a30a7f`  |
| 1439   | Layout 1             | `f3a333a30a7f`  |
| 1433   | Layout 1             | `f3a333a30a7f`  |
| 1430   | Layout 1             | `f3a333a30a7f`  |
| 1426   | Layout 1             | `f3a333a30a7f`  |
| 1421   | Layout 1             | `f3a333a30a7f`  |
| 1417   | Layout 1             | `f3a333a30a7f`  |
| 1416   | Layout 1             | `f3a333a30a7f`  |
| 1409   | Layout 1             | `f3a333a30a7f`  |
| 1405   | Layout 1             | `f3a333a30a7f`  |
| 1401   | Layout 1             | `f3a333a30a7f`  |
| 1396   | Layout 1             | `f3a333a30a7f`  |
| 1391   | Layout 1             | `f3a333a30a7f`  |
| 1390   | Layout 1             | `f3a333a30a7f`  |
| 1386   | Layout 1             | `f3a333a30a7f`  |
| 1381   | Layout 1             | `f3a333a30a7f`  |
| 1379   | Layout 1             | `f3a333a30a7f`  |
| 1372   | Layout 1             | `f3a333a30a7f`  |
| 1366   | Layout 1             | `f3a333a30a7f`  |
| 1364   | Layout 1             | `f3a333a30a7f`  |
| 1363   | Layout 1             | `f3a333a30a7f`  |
| 1360   | Layout 1             | `f3a333a30a7f`  |
| 1358   | No documented layout | `f3a333a30a7f`  |
| 1355   | No documented layout | `f3a333a30a7f`  |
| 1351   | No documented layout | `f3a333a30a7f`  |
| 1348   | No documented layout | `f3a333a30a7f`  |
| 1346   | No documented layout | `f3a333a30a7f`  |
| 1341   | No documented layout | `f3a333a30a7f`  |
| 1340   | No documented layout | `f3a333a30a7f`  |
| 1338   | No documented layout | `f3a333a30a7f`  |
| 1335   | No documented layout | `f3a333a30a7f`  |
| 1333   | No documented layout | `f3a333a30a7f`  |
| 1329   | No documented layout | `f3a333a30a7f`  |
| 1327   | No documented layout | `f3a333a30a7f`  |
| 1324   | No documented layout | `f3a333a30a7f`  |
| 1321   | No documented layout | `f3a333a30a7f`  |
| 1319   | No documented layout | `f3a333a30a7f`  |
| 1318   | No documented layout | `f3a333a30a7f`  |
| 1316   | No documented layout | `f3a333a30a7f`  |
| 1313   | No documented layout | `f3a333a30a7f`  |
| 1311   | No documented layout | `f3a333a30a7f`  |
| 1309   | No file              | `f3a333a30a7f`  |
| 1304   | No file              | `f3a333a30a7f`  |
| 1292   | No file              | `f3a333a30a7f`  |
| 1286   | No file              | `f3a333a30a7f`  |
| 1280   | No file              | `f3a333a30a7f`  |
| 1276   | No file              | `f3a333a30a7f`  |
| 1267   | No file              | `f3a333a30a7f`  |
| 1261   | No file              | `f3a333a30a7f`  |
| 1256   | No file              | `f3a333a30a7f`  |
| 1250   | No file              | `f3a333a30a7f`  |
| 1246   | No file              | `f3a333a30a7f`  |
| 1239   | No file              | `f3a333a30a7f`  |
| 1230   | No file              | `f3a333a30a7f`  |
| 1226   | No file              | `f3a333a30a7f`  |
| 1220   | No file              | `f3a333a30a7f`  |
| 1217   | No file              | `f3a333a30a7f`  |
| 1211   | No file              | `f3a333a30a7f`  |
| 1210   | No file              | `f3a333a30a7f`  |
| 1208   | No file              | `f3a333a30a7f`  |
| 1203   | No file              | `f3a333a30a7f`  |
| 1197   | No file              | `f3a333a30a7f`  |
| 1194   | No file              | `f3a333a30a7f`  |
| 1192   | No file              | `f3a333a30a7f`  |
| 1187   | No file              | `f3a333a30a7f`  |
| 1183   | No file              | `f3a333a30a7f`  |
| 1177   | No file              | `f3a333a30a7f`  |
| 1173   | No file              | `f3a333a30a7f`  |
| 1167   | No file              | `f3a333a30a7f`  |
| 1164   | No file              | `f3a333a30a7f`  |
| 1156   | No file              | `f3a333a30a7f`  |
| 1149   | No file              | `f3a333a30a7f`  |
| 1144   | No file              | `f3a333a30a7f`  |
| 1137   | No file              | `f3a333a30a7f`  |
| 1132   | No file              | `f3a333a30a7f`  |
| 1127   | No file              | `f3a333a30a7f`  |
| 1122   | No file              | `f3a333a30a7f`  |
| 1118   | No file              | `f3a333a30a7f`  |
| 1114   | No file              | `f3a333a30a7f`  |
| 1109   | No file              | `f3a333a30a7f`  |
| 1102   | No file              | `f3a333a30a7f`  |
| 1096   | No file              | `f3a333a30a7f`  |
| 1088   | No file              | `f3a333a30a7f`  |
| 1081   | No file              | `f3a333a30a7f`  |
| 1076   | No file              | `f3a333a30a7f`  |
| 1069   | No file              | `f3a333a30a7f`  |
| 1064   | No file              | `f3a333a30a7f`  |
| 1058   | No file              | `f3a333a30a7f`  |
| 1051   | No file              | `f3a333a30a7f`  |
| 1044   | No file              | `f3a333a30a7f`  |
| 1036   | No file              | `f3a333a30a7f`  |
| 1026   | No file              | `f3a333a30a7f`  |
| 1016   | No file              | `f3a333a30a7f`  |
| 1009   | No file              | `f3a333a30a7f`  |
| 1005   | No file              | `f3a333a30a7f`  |
| 1000   | No file              | `f3a333a30a7f`  |
| 998    | No file              | `f3a333a30a7f`  |
| 990    | No file              | `f3a333a30a7f`  |
| 979    | No file              | `f3a333a30a7f`  |
| 972    | No file              | `f3a333a30a7f`  |
| 963    | No file              | `f3a333a30a7f`  |
| 955    | No file              | `f3a333a30a7f`  |
| 946    | No file              | `f3a333a30a7f`  |
| 938    | No file              | `f3a333a30a7f`  |
| 927    | No file              | `f3a333a30a7f`  |
| 911    | No file              | `f3a333a30a7f`  |
| 904    | No file              | `f3a333a30a7f`  |
| 899    | No file              | `f3a333a30a7f`  |
| 894    | No file              | `f3a333a30a7f`  |
| 885    | No file              | `f3a333a30a7f`  |
| 879    | No file              | `f3a333a30a7f`  |
| 872    | No file              | `f3a333a30a7f`  |
| 864    | No file              | `f3a333a30a7f`  |
| 855    | No file              | `f3a333a30a7f`  |
| 853    | No file              | `f3a333a30a7f`  |
| 845    | No file              | `f3a333a30a7f`  |
| 837    | No file              | `f3a333a30a7f`  |
| 829    | No file              | `f3a333a30a7f`  |
| 822    | No file              | `f3a333a30a7f`  |
| 814    | No file              | `f3a333a30a7f`  |
| 805    | No file              | `f3a333a30a7f`  |
| 794    | No file              | `f3a333a30a7f`  |
| 787    | No file              | `f3a333a30a7f`  |
| 780    | No file              | `f3a333a30a7f`  |
| 771    | No file              | `f3a333a30a7f`  |
| 760    | No file              | `f3a333a30a7f`  |
| 748    | No file              | `f3a333a30a7f`  |
| 741    | No file              | `f3a333a30a7f`  |
| 736    | No file              | `f3a333a30a7f`  |
| 731    | No file              | `f3a333a30a7f`  |
| 723    | No file              | `f3a333a30a7f`  |
| 711    | No file              | `f3a333a30a7f`  |
| 707    | No file              | `f3a333a30a7f`  |
| 697    | No file              | `f3a333a30a7f`  |
| 689    | No file              | `f3a333a30a7f`  |
| 683    | No file              | `f3a333a30a7f`  |
| 678    | No file              | `f3a333a30a7f`  |
| 670    | No file              | `f3a333a30a7f`  |
| 661    | No file              | `f3a333a30a7f`  |
| 656    | No file              | `f3a333a30a7f`  |
| 652    | No file              | `f3a333a30a7f`  |
| 643    | No file              | `f3a333a30a7f`  |
| 637    | No file              | `f3a333a30a7f`  |
| 630    | No file              | `f3a333a30a7f`  |
| 627    | No file              | `f3a333a30a7f`  |
| 621    | No file              | `f3a333a30a7f`  |
| 617    | No file              | `f3a333a30a7f`  |
| 615    | No file              | `f3a333a30a7f`  |
| 606    | No file              | `f3a333a30a7f`  |
| 599    | No file              | `f3a333a30a7f`  |
| 592    | No file              | `f3a333a30a7f`  |
| 586    | No file              | `f3a333a30a7f`  |
| 577    | No file              | `f3a333a30a7f`  |
| 569    | No file              | `f3a333a30a7f`  |
| 561    | No file              | `f3a333a30a7f`  |
| 554    | No file              | `f3a333a30a7f`  |
| 542    | No file              | `f3a333a30a7f`  |
| 532    | No file              | `f3a333a30a7f`  |
| 531    | No file              | `f3a333a30a7f`  |
| 526    | No file              | `f3a333a30a7f`  |
| 521    | No file              | `f3a333a30a7f`  |
| 517    | No file              | `f3a333a30a7f`  |
| 510    | No file              | `f3a333a30a7f`  |
| 508    | No file              | `f3a333a30a7f`  |
| 504    | No file              | `f3a333a30a7f`  |
| 497    | No file              | `f3a333a30a7f`  |
| 491    | No file              | `f3a333a30a7f`  |
| 485    | No file              | `f3a333a30a7f`  |
| 478    | No file              | `f3a333a30a7f`  |
| 472    | No file              | `f3a333a30a7f`  |
| 466    | No file              | `f3a333a30a7f`  |
| 457    | No file              | `f3a333a30a7f`  |
| 452    | No file              | `f3a333a30a7f`  |
| 449    | No file              | `f3a333a30a7f`  |
| 435    | No file              | `f3a333a30a7f`  |

<!-- versions:end -->

## Companion Files

| File                                  | Required | Role                                            |
| ------------------------------------- | -------- | ----------------------------------------------- |
| `actionverificationindexoffset.dbss`  | Required | `class_type -> (offset, size)` of every record  |
| `languagedata_en.loc`                 | Optional | Class names (LOC type 21, `str_id1` = class type, `str_id4` = `0`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no trailer.

| Offset  | Type          | Field   | Notes                                                    |
| ------- | ------------- | ------- | -------------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `12` on clients 1784 and 3474         |
| `+0x04` | Record[count] | records | See Record                                               |

The records fill the file exactly: 4 + 12 x 9 = 112 bytes on client 3474.
They are in ascending order of `class_type XOR 0xDEADBEEF` (`71`, `69`,
`65`, `87`, `81`, `63`, `61`, `60`, `58`, `55`, `53`, `52`), the order of
the server's sorted class type map (see Field Names).

### Record (9 bytes)

| Offset  | Type    | Field      | Notes                                                        |
| ------- | ------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8      | key_prefix | Copy of the class type; the offset row points past it        |
| `+0x01` | Payload | payload    | See Payload; the offset row points here                      |

### Payload (8 bytes)

| Offset  | Type     | Field      | Notes                                                                   |
| ------- | -------- | ---------- | ----------------------------------------------------------------------- |
| `+0x00` | u8       | class_type | Class type, the number `getClassType()` returns; the record key          |
| `+0x01` | bytes[7] | unknown_01 | Every byte `0` on clients 1784 and 3474; see Open Questions             |

### `actionverificationindexoffset.dbss`

Bare offset table into `actionverificationindex.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                              |
| ------- | ----------------- | ----- | -------------------------------------------------- |
| `+0x00` | u32               | count | Number of offset rows; equals the main file count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                     |

The rows fill the file exactly: 4 + 12 x 12 = 148 bytes on client 3474.
Their order differs from the main file's (`63`, `87`, `71`, `61`, `69`,
`81`, `65`, `60`, `58`, `55`, `53`, `52` on client 3474).

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                       |
| ------- | ---- | ----------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | class_type  | Key of the record it points at                                              |
| `+0x04` | u32  | data_offset | Absolute byte offset of the Payload in `actionverificationindex.dbss`, past its `key_prefix` |
| `+0x08` | u32  | data_size   | `8`, the Payload size                                                       |

The first record's Payload sits at `5`, after the count and its
`key_prefix`. The parser reads the main file through these rows and checks
that each record's `key_prefix` and `class_type` equal the offset row's key.

## Field Names

The names follow the `VerificationClassType` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`DataSheet_VerificationDataTable_Shadow.xlsm`. The sheet has the columns
`Index` (`1` to `12`, in ascending class type order) and `ClassType`. Its
12 class types are the 12 keys of the client 1784 file and of the live
file (12 of 12, client 3474). The file stores no `Index`.

The same workbook has one sheet per class type, named after it (`52` to
`87`), each with the columns `ClassType`, `Index` and `ActionName` and no
rows, and the `ActionVerification_Table` sheet (`CharacterKey`,
`ActionName`, `AbleCallTime`) that
[`actionverification.bss`](../bss/actionverification_bss.md) is compiled from.
Its character keys `65002` and up are the same heroes in LOC type 6
(`65002` Jordine, `65003` Peony).

The client 1784 server dump of the same private server names the type
`gc::ActionVerificationIndexStaticStatus` and keeps the records in a
`StaticStatusManager` keyed by `gc::ClassType` (RTTI). Its loader reads
the `ClassType` column of `VerificationClassType` as text, opens the sheet
of that name, and takes the class type from the sheet name. From each row
of that sheet it reads `ClassType` and `Index` as ints and hashes
`ActionName` to a u32, and adds `ActionName` hash -> `Index` to a map in
the record. A check after each row logs an error for an `Index` of `0` or
less or a class type of `101` or more. The record is 80 bytes in memory: an
8-byte field the loader sets to `0`, the action map and the class type as
one byte. A second check walks the class type list, binary-searching each
class type in the manager's map sorted by `class_type XOR 0xDEADBEEF`, and
logs an error for a missing one.

The 2016 PDB has no action verification type, the client 519 tables have no
such table, and no client Lua file (client 3474) names it.

## Notes

- The client 1784 and 3474 files are byte for byte the same, in both the
  main file and the offset file.
- LOC type 21 gives every one of the 12 class types a name with `str_id4`
  `0`; `[PH] 12`, `[PH] 22` and `[PH] 28` are placeholders.
- Nine of the 12 class types plus `64950` are the hero character keys of
  [`actionverification.bss`](../bss/actionverification_bss.md) (`52` and
  `65002` Jordine); `61`, `65` and `71` have no character there.

## Open Questions

### What `unknown_01` Holds

The 7 bytes after `class_type` are `0` in every record of clients 1784 and
3474. The server loader gives each record a map of `ActionName` hash ->
`Index` from the class type's own sheet, and every such sheet is empty on
client 1784, so a u32 entry count of `0` would fit, as in
[`actionverification.bss`](../bss/actionverification_bss.md), which stores each
action map as a u32 count and (hash, value) pairs. With no record that has actions, the split of the 7
bytes (a count, its width, padding) and the shape of a list entry stay
unknown.
