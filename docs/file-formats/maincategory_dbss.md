# `maincategory.dbss` Format

## Purpose

`maincategory.dbss` is the list of Pearl Shop main categories, the tabs of the in-game shop. Each record holds the category ID, its tab order and tab image, the category type, an ASCII DDS icon path, an event cart key and whether the tab is shown. Companion `maincategoryoffset.dbss` holds the keyed record offsets.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------------ | --------- |
| 2      | 2151 and later | 3483    | `maincategory.dbss`       | 1,534 | 15 Category Record | 102       |
| 2      | 2151 and later | 3483    | `maincategoryoffset.dbss` | 154   | 15 Offset Record   | 10        |
| 1      | 1286 to 2147   | 2147    | `maincategory.dbss`       | 1,216 | 12 Category Record | 101       |
| 1      | 1286 to 2147   | 2147    | `maincategoryoffset.dbss` | 124   | 12 Offset Record   | 10        |

| Layout | File                      | Known            | Unknown      |
| ------ | ------------------------- | ---------------- | ------------ |
| 2      | `maincategory.dbss`       | 1,534 B (100.0%) | 0 B (0.0%)   |
| 2      | `maincategoryoffset.dbss` | 124 B (80.5%)    | 30 B (19.5%) |
| 1      | `maincategory.dbss`       | 1,216 B (100.0%) | 0 B (0.0%)   |
| 1      | `maincategoryoffset.dbss` | 100 B (80.6%)    | 24 B (19.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `4d0ea5c0305f`  |
| 3482   | Layout 2 | `4d0ea5c0305f`  |
| 3474   | Layout 2 | `4d0ea5c0305f`  |
| 3473   | Layout 2 | `4d0ea5c0305f`  |
| 3464   | Layout 2 | `4d0ea5c0305f`  |
| 3458   | Layout 2 | `4d0ea5c0305f`  |
| 3454   | Layout 2 | `4d0ea5c0305f`  |
| 3444   | Layout 2 | `4d0ea5c0305f`  |
| 3435   | Layout 2 | `4d0ea5c0305f`  |
| 3426   | Layout 2 | `4d0ea5c0305f`  |
| 3418   | Layout 2 | `4d0ea5c0305f`  |
| 3412   | Layout 2 | `4d0ea5c0305f`  |
| 3402   | Layout 2 | `4d0ea5c0305f`  |
| 3396   | Layout 2 | `4d0ea5c0305f`  |
| 3387   | Layout 2 | `4d0ea5c0305f`  |
| 3381   | Layout 2 | `4d0ea5c0305f`  |
| 3373   | Layout 2 | `4d0ea5c0305f`  |
| 3364   | Layout 2 | `4d0ea5c0305f`  |
| 3356   | Layout 2 | `4d0ea5c0305f`  |
| 3349   | Layout 2 | `4d0ea5c0305f`  |
| 3342   | Layout 2 | `4d0ea5c0305f`  |
| 3335   | Layout 2 | `4d0ea5c0305f`  |
| 3326   | Layout 2 | `4d0ea5c0305f`  |
| 3321   | Layout 2 | `4d0ea5c0305f`  |
| 3314   | Layout 2 | `4d0ea5c0305f`  |
| 3303   | Layout 2 | `4d0ea5c0305f`  |
| 3302   | Layout 2 | `4d0ea5c0305f`  |
| 3293   | Layout 2 | `4d0ea5c0305f`  |
| 3283   | Layout 2 | `4d0ea5c0305f`  |
| 3275   | Layout 2 | `4d0ea5c0305f`  |
| 3267   | Layout 2 | `4d0ea5c0305f`  |
| 3258   | Layout 2 | `4d0ea5c0305f`  |
| 3251   | Layout 2 | `4d0ea5c0305f`  |
| 3242   | Layout 2 | `4d0ea5c0305f`  |
| 3235   | Layout 2 | `4d0ea5c0305f`  |
| 3229   | Layout 2 | `4d0ea5c0305f`  |
| 3212   | Layout 2 | `4d0ea5c0305f`  |
| 3203   | Layout 2 | `4d0ea5c0305f`  |
| 3193   | Layout 2 | `4d0ea5c0305f`  |
| 3186   | Layout 2 | `4d0ea5c0305f`  |
| 3177   | Layout 2 | `4d0ea5c0305f`  |
| 3169   | Layout 2 | `4d0ea5c0305f`  |
| 3158   | Layout 2 | `4d0ea5c0305f`  |
| 3151   | Layout 2 | `4d0ea5c0305f`  |
| 3144   | Layout 2 | `4d0ea5c0305f`  |
| 3133   | Layout 2 | `4d0ea5c0305f`  |
| 3125   | Layout 2 | `4d0ea5c0305f`  |
| 3118   | Layout 2 | `4d0ea5c0305f`  |
| 3111   | Layout 2 | `4d0ea5c0305f`  |
| 3103   | Layout 2 | `4d0ea5c0305f`  |
| 3095   | Layout 2 | `4d0ea5c0305f`  |
| 3086   | Layout 2 | `4d0ea5c0305f`  |
| 3072   | Layout 2 | `4d0ea5c0305f`  |
| 3062   | Layout 2 | `4d0ea5c0305f`  |
| 3052   | Layout 2 | `4d0ea5c0305f`  |
| 3045   | Layout 2 | `4d0ea5c0305f`  |
| 3037   | Layout 2 | `4d0ea5c0305f`  |
| 3030   | Layout 2 | `4d0ea5c0305f`  |
| 3021   | Layout 2 | `4d0ea5c0305f`  |
| 3012   | Layout 2 | `4d0ea5c0305f`  |
| 3002   | Layout 2 | `4d0ea5c0305f`  |
| 2995   | Layout 2 | `4d0ea5c0305f`  |
| 2987   | Layout 2 | `4d0ea5c0305f`  |
| 2978   | Layout 2 | `4d0ea5c0305f`  |
| 2970   | Layout 2 | `4d0ea5c0305f`  |
| 2959   | Layout 2 | `4d0ea5c0305f`  |
| 2951   | Layout 2 | `4d0ea5c0305f`  |
| 2942   | Layout 2 | `4d0ea5c0305f`  |
| 2935   | Layout 2 | `4d0ea5c0305f`  |
| 2932   | Layout 2 | `4d0ea5c0305f`  |
| 2923   | Layout 2 | `4d0ea5c0305f`  |
| 2919   | Layout 2 | `4d0ea5c0305f`  |
| 2907   | Layout 2 | `4d0ea5c0305f`  |
| 2900   | Layout 2 | `4d0ea5c0305f`  |
| 2891   | Layout 2 | `4d0ea5c0305f`  |
| 2882   | Layout 2 | `4d0ea5c0305f`  |
| 2872   | Layout 2 | `4d0ea5c0305f`  |
| 2863   | Layout 2 | `4d0ea5c0305f`  |
| 2855   | Layout 2 | `4d0ea5c0305f`  |
| 2849   | Layout 2 | `4d0ea5c0305f`  |
| 2844   | Layout 2 | `4d0ea5c0305f`  |
| 2834   | Layout 2 | `4d0ea5c0305f`  |
| 2825   | Layout 2 | `4d0ea5c0305f`  |
| 2819   | Layout 2 | `4d0ea5c0305f`  |
| 2811   | Layout 2 | `4d0ea5c0305f`  |
| 2803   | Layout 2 | `4d0ea5c0305f`  |
| 2794   | Layout 2 | `4d0ea5c0305f`  |
| 2783   | Layout 2 | `4d0ea5c0305f`  |
| 2774   | Layout 2 | `4d0ea5c0305f`  |
| 2765   | Layout 2 | `4d0ea5c0305f`  |
| 2756   | Layout 2 | `4d0ea5c0305f`  |
| 2750   | Layout 2 | `4d0ea5c0305f`  |
| 2743   | Layout 2 | `4d0ea5c0305f`  |
| 2736   | Layout 2 | `4d0ea5c0305f`  |
| 2726   | Layout 2 | `4d0ea5c0305f`  |
| 2717   | Layout 2 | `4d0ea5c0305f`  |
| 2709   | Layout 2 | `4d0ea5c0305f`  |
| 2703   | Layout 2 | `4d0ea5c0305f`  |
| 2695   | Layout 2 | `4d0ea5c0305f`  |
| 2684   | Layout 2 | `4d0ea5c0305f`  |
| 2672   | Layout 2 | `4d0ea5c0305f`  |
| 2665   | Layout 2 | `4d0ea5c0305f`  |
| 2657   | Layout 2 | `4d0ea5c0305f`  |
| 2649   | Layout 2 | `4d0ea5c0305f`  |
| 2644   | Layout 2 | `4d0ea5c0305f`  |
| 2637   | Layout 2 | `4d0ea5c0305f`  |
| 2629   | Layout 2 | `4d0ea5c0305f`  |
| 2619   | Layout 2 | `4d0ea5c0305f`  |
| 2612   | Layout 2 | `4d0ea5c0305f`  |
| 2606   | Layout 2 | `4d0ea5c0305f`  |
| 2602   | Layout 2 | `4d0ea5c0305f`  |
| 2601   | Layout 2 | `4d0ea5c0305f`  |
| 2592   | Layout 2 | `4d0ea5c0305f`  |
| 2583   | Layout 2 | `4d0ea5c0305f`  |
| 2575   | Layout 2 | `4d0ea5c0305f`  |
| 2567   | Layout 2 | `4d0ea5c0305f`  |
| 2560   | Layout 2 | `4d0ea5c0305f`  |
| 2553   | Layout 2 | `4d0ea5c0305f`  |
| 2545   | Layout 2 | `4d0ea5c0305f`  |
| 2538   | Layout 2 | `4d0ea5c0305f`  |
| 2529   | Layout 2 | `4d0ea5c0305f`  |
| 2519   | Layout 2 | `4d0ea5c0305f`  |
| 2513   | Layout 2 | `4d0ea5c0305f`  |
| 2510   | Layout 2 | `4d0ea5c0305f`  |
| 2507   | Layout 2 | `4d0ea5c0305f`  |
| 2503   | Layout 2 | `4d0ea5c0305f`  |
| 2498   | Layout 2 | `4d0ea5c0305f`  |
| 2492   | Layout 2 | `4d0ea5c0305f`  |
| 2487   | Layout 2 | `4d0ea5c0305f`  |
| 2480   | Layout 2 | `4d0ea5c0305f`  |
| 2474   | Layout 2 | `4d0ea5c0305f`  |
| 2468   | Layout 2 | `4d0ea5c0305f`  |
| 2460   | Layout 2 | `4d0ea5c0305f`  |
| 2453   | Layout 2 | `4d0ea5c0305f`  |
| 2444   | Layout 2 | `4d0ea5c0305f`  |
| 2438   | Layout 2 | `4d0ea5c0305f`  |
| 2434   | Layout 2 | `4d0ea5c0305f`  |
| 2429   | Layout 2 | `4d0ea5c0305f`  |
| 2421   | Layout 2 | `4d0ea5c0305f`  |
| 2414   | Layout 2 | `4d0ea5c0305f`  |
| 2407   | Layout 2 | `4d0ea5c0305f`  |
| 2401   | Layout 2 | `4d0ea5c0305f`  |
| 2397   | Layout 2 | `4d0ea5c0305f`  |
| 2393   | Layout 2 | `4d0ea5c0305f`  |
| 2384   | Layout 2 | `4d0ea5c0305f`  |
| 2378   | Layout 2 | `4d0ea5c0305f`  |
| 2372   | Layout 2 | `4d0ea5c0305f`  |
| 2358   | Layout 2 | `4d0ea5c0305f`  |
| 2352   | Layout 2 | `4d0ea5c0305f`  |
| 2347   | Layout 2 | `4d0ea5c0305f`  |
| 2343   | Layout 2 | `4d0ea5c0305f`  |
| 2335   | Layout 2 | `4d0ea5c0305f`  |
| 2327   | Layout 2 | `4d0ea5c0305f`  |
| 2324   | Layout 2 | `4d0ea5c0305f`  |
| 2319   | Layout 2 | `4d0ea5c0305f`  |
| 2313   | Layout 2 | `4d0ea5c0305f`  |
| 2308   | Layout 2 | `4d0ea5c0305f`  |
| 2302   | Layout 2 | `4d0ea5c0305f`  |
| 2295   | Layout 2 | `4d0ea5c0305f`  |
| 2290   | Layout 2 | `4d0ea5c0305f`  |
| 2284   | Layout 2 | `4d0ea5c0305f`  |
| 2276   | Layout 2 | `4d0ea5c0305f`  |
| 2269   | Layout 2 | `4d0ea5c0305f`  |
| 2259   | Layout 2 | `4d0ea5c0305f`  |
| 2250   | Layout 2 | `4d0ea5c0305f`  |
| 2243   | Layout 2 | `4d0ea5c0305f`  |
| 2235   | Layout 2 | `4d0ea5c0305f`  |
| 2229   | Layout 2 | `4d0ea5c0305f`  |
| 2224   | Layout 2 | `4d0ea5c0305f`  |
| 2218   | Layout 2 | `4d0ea5c0305f`  |
| 2215   | Layout 2 | `4d0ea5c0305f`  |
| 2207   | Layout 2 | `4d0ea5c0305f`  |
| 2203   | Layout 2 | `4d0ea5c0305f`  |
| 2196   | Layout 2 | `4d0ea5c0305f`  |
| 2192   | Layout 2 | `4d0ea5c0305f`  |
| 2189   | Layout 2 | `4d0ea5c0305f`  |
| 2183   | Layout 2 | `4d0ea5c0305f`  |
| 2179   | Layout 2 | `4d0ea5c0305f`  |
| 2171   | Layout 2 | `4d0ea5c0305f`  |
| 2163   | Layout 2 | `4d0ea5c0305f`  |
| 2156   | Layout 2 | `4d0ea5c0305f`  |
| 2151   | Layout 2 | `4d0ea5c0305f`  |
| 2147   | Layout 1 | `4d0ea5c0305f`  |
| 2142   | Layout 1 | `4d0ea5c0305f`  |
| 2138   | Layout 1 | `4d0ea5c0305f`  |
| 2134   | Layout 1 | `4d0ea5c0305f`  |
| 2130   | Layout 1 | `4d0ea5c0305f`  |
| 2122   | Layout 1 | `4d0ea5c0305f`  |
| 2107   | Layout 1 | `4d0ea5c0305f`  |
| 2098   | Layout 1 | `4d0ea5c0305f`  |
| 2089   | Layout 1 | `4d0ea5c0305f`  |
| 2081   | Layout 1 | `4d0ea5c0305f`  |
| 2073   | Layout 1 | `4d0ea5c0305f`  |
| 2067   | Layout 1 | `4d0ea5c0305f`  |
| 2063   | Layout 1 | `4d0ea5c0305f`  |
| 2059   | Layout 1 | `4d0ea5c0305f`  |
| 2052   | Layout 1 | `4d0ea5c0305f`  |
| 2044   | Layout 1 | `4d0ea5c0305f`  |
| 2039   | Layout 1 | `4d0ea5c0305f`  |
| 2032   | Layout 1 | `4d0ea5c0305f`  |
| 2025   | Layout 1 | `4d0ea5c0305f`  |
| 2011   | Layout 1 | `4d0ea5c0305f`  |
| 2005   | Layout 1 | `4d0ea5c0305f`  |
| 2000   | Layout 1 | `4d0ea5c0305f`  |
| 1996   | Layout 1 | `4d0ea5c0305f`  |
| 1991   | Layout 1 | `4d0ea5c0305f`  |
| 1985   | Layout 1 | `4d0ea5c0305f`  |
| 1980   | Layout 1 | `4d0ea5c0305f`  |
| 1969   | Layout 1 | `4d0ea5c0305f`  |
| 1964   | Layout 1 | `4d0ea5c0305f`  |
| 1958   | Layout 1 | `4d0ea5c0305f`  |
| 1950   | Layout 1 | `4d0ea5c0305f`  |
| 1945   | Layout 1 | `4d0ea5c0305f`  |
| 1937   | Layout 1 | `4d0ea5c0305f`  |
| 1933   | Layout 1 | `4d0ea5c0305f`  |
| 1927   | Layout 1 | `4d0ea5c0305f`  |
| 1921   | Layout 1 | `4d0ea5c0305f`  |
| 1914   | Layout 1 | `4d0ea5c0305f`  |
| 1908   | Layout 1 | `4d0ea5c0305f`  |
| 1897   | Layout 1 | `4d0ea5c0305f`  |
| 1892   | Layout 1 | `4d0ea5c0305f`  |
| 1886   | Layout 1 | `4d0ea5c0305f`  |
| 1881   | Layout 1 | `4d0ea5c0305f`  |
| 1871   | Layout 1 | `4d0ea5c0305f`  |
| 1866   | Layout 1 | `4d0ea5c0305f`  |
| 1862   | Layout 1 | `4d0ea5c0305f`  |
| 1854   | Layout 1 | `4d0ea5c0305f`  |
| 1846   | Layout 1 | `4d0ea5c0305f`  |
| 1838   | Layout 1 | `4d0ea5c0305f`  |
| 1832   | Layout 1 | `4d0ea5c0305f`  |
| 1826   | Layout 1 | `4d0ea5c0305f`  |
| 1822   | Layout 1 | `4d0ea5c0305f`  |
| 1818   | Layout 1 | `4d0ea5c0305f`  |
| 1804   | Layout 1 | `4d0ea5c0305f`  |
| 1794   | Layout 1 | `4d0ea5c0305f`  |
| 1790   | Layout 1 | `4d0ea5c0305f`  |
| 1784   | Layout 1 | `4d0ea5c0305f`  |
| 1774   | Layout 1 | `4d0ea5c0305f`  |
| 1771   | Layout 1 | `4d0ea5c0305f`  |
| 1762   | Layout 1 | `4d0ea5c0305f`  |
| 1759   | Layout 1 | `4d0ea5c0305f`  |
| 1754   | Layout 1 | `4d0ea5c0305f`  |
| 1749   | Layout 1 | `4d0ea5c0305f`  |
| 1743   | Layout 1 | `4d0ea5c0305f`  |
| 1737   | Layout 1 | `4d0ea5c0305f`  |
| 1731   | Layout 1 | `4d0ea5c0305f`  |
| 1725   | Layout 1 | `4d0ea5c0305f`  |
| 1717   | Layout 1 | `4d0ea5c0305f`  |
| 1710   | Layout 1 | `4d0ea5c0305f`  |
| 1704   | Layout 1 | `4d0ea5c0305f`  |
| 1698   | Layout 1 | `4d0ea5c0305f`  |
| 1690   | Layout 1 | `4d0ea5c0305f`  |
| 1685   | Layout 1 | `4d0ea5c0305f`  |
| 1680   | Layout 1 | `4d0ea5c0305f`  |
| 1674   | Layout 1 | `4d0ea5c0305f`  |
| 1668   | Layout 1 | `4d0ea5c0305f`  |
| 1659   | Layout 1 | `4d0ea5c0305f`  |
| 1649   | Layout 1 | `4d0ea5c0305f`  |
| 1642   | Layout 1 | `4d0ea5c0305f`  |
| 1636   | Layout 1 | `4d0ea5c0305f`  |
| 1628   | Layout 1 | `4d0ea5c0305f`  |
| 1622   | Layout 1 | `4d0ea5c0305f`  |
| 1614   | Layout 1 | `4d0ea5c0305f`  |
| 1608   | Layout 1 | `4d0ea5c0305f`  |
| 1602   | Layout 1 | `4d0ea5c0305f`  |
| 1598   | Layout 1 | `4d0ea5c0305f`  |
| 1594   | Layout 1 | `4d0ea5c0305f`  |
| 1590   | Layout 1 | `4d0ea5c0305f`  |
| 1587   | Layout 1 | `4d0ea5c0305f`  |
| 1584   | Layout 1 | `4d0ea5c0305f`  |
| 1579   | Layout 1 | `4d0ea5c0305f`  |
| 1572   | Layout 1 | `4d0ea5c0305f`  |
| 1565   | Layout 1 | `4d0ea5c0305f`  |
| 1559   | Layout 1 | `4d0ea5c0305f`  |
| 1554   | Layout 1 | `4d0ea5c0305f`  |
| 1547   | Layout 1 | `4d0ea5c0305f`  |
| 1537   | Layout 1 | `4d0ea5c0305f`  |
| 1529   | Layout 1 | `4d0ea5c0305f`  |
| 1524   | Layout 1 | `4d0ea5c0305f`  |
| 1519   | Layout 1 | `4d0ea5c0305f`  |
| 1509   | Layout 1 | `4d0ea5c0305f`  |
| 1506   | Layout 1 | `4d0ea5c0305f`  |
| 1504   | Layout 1 | `4d0ea5c0305f`  |
| 1500   | Layout 1 | `4d0ea5c0305f`  |
| 1493   | Layout 1 | `4d0ea5c0305f`  |
| 1489   | Layout 1 | `4d0ea5c0305f`  |
| 1485   | Layout 1 | `4d0ea5c0305f`  |
| 1481   | Layout 1 | `4d0ea5c0305f`  |
| 1474   | Layout 1 | `4d0ea5c0305f`  |
| 1466   | Layout 1 | `4d0ea5c0305f`  |
| 1462   | Layout 1 | `4d0ea5c0305f`  |
| 1459   | Layout 1 | `4d0ea5c0305f`  |
| 1453   | Layout 1 | `4d0ea5c0305f`  |
| 1450   | Layout 1 | `4d0ea5c0305f`  |
| 1445   | Layout 1 | `4d0ea5c0305f`  |
| 1439   | Layout 1 | `4d0ea5c0305f`  |
| 1433   | Layout 1 | `4d0ea5c0305f`  |
| 1430   | Layout 1 | `4d0ea5c0305f`  |
| 1426   | Layout 1 | `4d0ea5c0305f`  |
| 1421   | Layout 1 | `4d0ea5c0305f`  |
| 1417   | Layout 1 | `4d0ea5c0305f`  |
| 1416   | Layout 1 | `4d0ea5c0305f`  |
| 1409   | Layout 1 | `4d0ea5c0305f`  |
| 1405   | Layout 1 | `4d0ea5c0305f`  |
| 1401   | Layout 1 | `4d0ea5c0305f`  |
| 1396   | Layout 1 | `4d0ea5c0305f`  |
| 1391   | Layout 1 | `4d0ea5c0305f`  |
| 1390   | Layout 1 | `4d0ea5c0305f`  |
| 1386   | Layout 1 | `4d0ea5c0305f`  |
| 1381   | Layout 1 | `4d0ea5c0305f`  |
| 1379   | Layout 1 | `4d0ea5c0305f`  |
| 1372   | Layout 1 | `4d0ea5c0305f`  |
| 1366   | Layout 1 | `4d0ea5c0305f`  |
| 1364   | Layout 1 | `4d0ea5c0305f`  |
| 1363   | Layout 1 | `4d0ea5c0305f`  |
| 1360   | Layout 1 | `4d0ea5c0305f`  |
| 1358   | Layout 1 | `4d0ea5c0305f`  |
| 1355   | Layout 1 | `4d0ea5c0305f`  |
| 1351   | Layout 1 | `4d0ea5c0305f`  |
| 1348   | Layout 1 | `4d0ea5c0305f`  |
| 1346   | Layout 1 | `4d0ea5c0305f`  |
| 1341   | Layout 1 | `4d0ea5c0305f`  |
| 1340   | Layout 1 | `4d0ea5c0305f`  |
| 1338   | Layout 1 | `4d0ea5c0305f`  |
| 1335   | Layout 1 | `4d0ea5c0305f`  |
| 1333   | Layout 1 | `4d0ea5c0305f`  |
| 1329   | Layout 1 | `4d0ea5c0305f`  |
| 1327   | Layout 1 | `4d0ea5c0305f`  |
| 1324   | Layout 1 | `4d0ea5c0305f`  |
| 1321   | Layout 1 | `4d0ea5c0305f`  |
| 1319   | Layout 1 | `4d0ea5c0305f`  |
| 1318   | Layout 1 | `4d0ea5c0305f`  |
| 1316   | Layout 1 | `4d0ea5c0305f`  |
| 1313   | Layout 1 | `4d0ea5c0305f`  |
| 1311   | Layout 1 | `4d0ea5c0305f`  |
| 1309   | Layout 1 | `4d0ea5c0305f`  |
| 1304   | Layout 1 | `4d0ea5c0305f`  |
| 1292   | Layout 1 | `4d0ea5c0305f`  |
| 1286   | Layout 1 | `4d0ea5c0305f`  |
| 1280   | No file  | `4d0ea5c0305f`  |
| 1276   | No file  | `4d0ea5c0305f`  |
| 1267   | No file  | `4d0ea5c0305f`  |
| 1261   | No file  | `4d0ea5c0305f`  |
| 1256   | No file  | `4d0ea5c0305f`  |
| 1250   | No file  | `4d0ea5c0305f`  |
| 1246   | No file  | `4d0ea5c0305f`  |
| 1239   | No file  | `4d0ea5c0305f`  |
| 1230   | No file  | `4d0ea5c0305f`  |
| 1226   | No file  | `4d0ea5c0305f`  |
| 1220   | No file  | `4d0ea5c0305f`  |
| 1217   | No file  | `4d0ea5c0305f`  |
| 1211   | No file  | `4d0ea5c0305f`  |
| 1210   | No file  | `4d0ea5c0305f`  |
| 1208   | No file  | `4d0ea5c0305f`  |
| 1203   | No file  | `4d0ea5c0305f`  |
| 1197   | No file  | `4d0ea5c0305f`  |
| 1194   | No file  | `4d0ea5c0305f`  |
| 1192   | No file  | `4d0ea5c0305f`  |
| 1187   | No file  | `4d0ea5c0305f`  |
| 1183   | No file  | `4d0ea5c0305f`  |
| 1177   | No file  | `4d0ea5c0305f`  |
| 1173   | No file  | `4d0ea5c0305f`  |
| 1167   | No file  | `4d0ea5c0305f`  |
| 1164   | No file  | `4d0ea5c0305f`  |
| 1156   | No file  | `4d0ea5c0305f`  |
| 1149   | No file  | `4d0ea5c0305f`  |
| 1144   | No file  | `4d0ea5c0305f`  |
| 1137   | No file  | `4d0ea5c0305f`  |
| 1132   | No file  | `4d0ea5c0305f`  |
| 1127   | No file  | `4d0ea5c0305f`  |
| 1122   | No file  | `4d0ea5c0305f`  |
| 1118   | No file  | `4d0ea5c0305f`  |
| 1114   | No file  | `4d0ea5c0305f`  |
| 1109   | No file  | `4d0ea5c0305f`  |
| 1102   | No file  | `4d0ea5c0305f`  |
| 1096   | No file  | `4d0ea5c0305f`  |
| 1088   | No file  | `4d0ea5c0305f`  |
| 1081   | No file  | `4d0ea5c0305f`  |
| 1076   | No file  | `4d0ea5c0305f`  |
| 1069   | No file  | `4d0ea5c0305f`  |
| 1064   | No file  | `4d0ea5c0305f`  |
| 1058   | No file  | `4d0ea5c0305f`  |
| 1051   | No file  | `4d0ea5c0305f`  |
| 1044   | No file  | `4d0ea5c0305f`  |
| 1036   | No file  | `4d0ea5c0305f`  |
| 1026   | No file  | `4d0ea5c0305f`  |
| 1016   | No file  | `4d0ea5c0305f`  |
| 1009   | No file  | `4d0ea5c0305f`  |
| 1005   | No file  | `4d0ea5c0305f`  |
| 1000   | No file  | `4d0ea5c0305f`  |
| 998    | No file  | `4d0ea5c0305f`  |
| 990    | No file  | `4d0ea5c0305f`  |
| 979    | No file  | `4d0ea5c0305f`  |
| 972    | No file  | `4d0ea5c0305f`  |
| 963    | No file  | `4d0ea5c0305f`  |
| 955    | No file  | `4d0ea5c0305f`  |
| 946    | No file  | `4d0ea5c0305f`  |
| 938    | No file  | `4d0ea5c0305f`  |
| 927    | No file  | `4d0ea5c0305f`  |
| 911    | No file  | `4d0ea5c0305f`  |
| 904    | No file  | `4d0ea5c0305f`  |
| 899    | No file  | `4d0ea5c0305f`  |
| 894    | No file  | `4d0ea5c0305f`  |
| 885    | No file  | `4d0ea5c0305f`  |
| 879    | No file  | `4d0ea5c0305f`  |
| 872    | No file  | `4d0ea5c0305f`  |
| 864    | No file  | `4d0ea5c0305f`  |
| 855    | No file  | `4d0ea5c0305f`  |
| 853    | No file  | `4d0ea5c0305f`  |
| 845    | No file  | `4d0ea5c0305f`  |
| 837    | No file  | `4d0ea5c0305f`  |
| 829    | No file  | `4d0ea5c0305f`  |
| 822    | No file  | `4d0ea5c0305f`  |
| 814    | No file  | `4d0ea5c0305f`  |
| 805    | No file  | `4d0ea5c0305f`  |
| 794    | No file  | `4d0ea5c0305f`  |
| 787    | No file  | `4d0ea5c0305f`  |
| 780    | No file  | `4d0ea5c0305f`  |
| 771    | No file  | `4d0ea5c0305f`  |
| 760    | No file  | `4d0ea5c0305f`  |
| 748    | No file  | `4d0ea5c0305f`  |
| 741    | No file  | `4d0ea5c0305f`  |
| 736    | No file  | `4d0ea5c0305f`  |
| 731    | No file  | `4d0ea5c0305f`  |
| 723    | No file  | `4d0ea5c0305f`  |
| 711    | No file  | `4d0ea5c0305f`  |
| 707    | No file  | `4d0ea5c0305f`  |
| 697    | No file  | `4d0ea5c0305f`  |
| 689    | No file  | `4d0ea5c0305f`  |
| 683    | No file  | `4d0ea5c0305f`  |
| 678    | No file  | `4d0ea5c0305f`  |
| 670    | No file  | `4d0ea5c0305f`  |
| 661    | No file  | `4d0ea5c0305f`  |
| 656    | No file  | `4d0ea5c0305f`  |
| 652    | No file  | `4d0ea5c0305f`  |
| 643    | No file  | `4d0ea5c0305f`  |
| 637    | No file  | `4d0ea5c0305f`  |
| 630    | No file  | `4d0ea5c0305f`  |
| 627    | No file  | `4d0ea5c0305f`  |
| 621    | No file  | `4d0ea5c0305f`  |
| 617    | No file  | `4d0ea5c0305f`  |
| 615    | No file  | `4d0ea5c0305f`  |
| 606    | No file  | `4d0ea5c0305f`  |
| 599    | No file  | `4d0ea5c0305f`  |
| 592    | No file  | `4d0ea5c0305f`  |
| 586    | No file  | `4d0ea5c0305f`  |
| 577    | No file  | `4d0ea5c0305f`  |
| 569    | No file  | `4d0ea5c0305f`  |
| 561    | No file  | `4d0ea5c0305f`  |
| 554    | No file  | `4d0ea5c0305f`  |
| 542    | No file  | `4d0ea5c0305f`  |
| 532    | No file  | `4d0ea5c0305f`  |
| 531    | No file  | `4d0ea5c0305f`  |
| 526    | No file  | `4d0ea5c0305f`  |
| 521    | No file  | `4d0ea5c0305f`  |
| 517    | No file  | `4d0ea5c0305f`  |
| 510    | No file  | `4d0ea5c0305f`  |
| 508    | No file  | `4d0ea5c0305f`  |
| 504    | No file  | `4d0ea5c0305f`  |
| 497    | No file  | `4d0ea5c0305f`  |
| 491    | No file  | `4d0ea5c0305f`  |
| 485    | No file  | `4d0ea5c0305f`  |
| 478    | No file  | `4d0ea5c0305f`  |
| 472    | No file  | `4d0ea5c0305f`  |
| 466    | No file  | `4d0ea5c0305f`  |
| 457    | No file  | `4d0ea5c0305f`  |
| 452    | No file  | `4d0ea5c0305f`  |
| 449    | No file  | `4d0ea5c0305f`  |
| 435    | No file  | `4d0ea5c0305f`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                 |
| ------------------------- | -------- | ---------------------------------------------------- |
| `maincategoryoffset.dbss` | Required | `category_id -> (record_offset, record_size)` lookup |

All multi-byte values are little-endian.

## Layout 2

### File Layout

`maincategory.dbss` begins with a count and then stores the category records. The count matches `maincategoryoffset.dbss`, and the offset table points to the first record at `0x0004`.

| Offset  | Type                   | Field   | Notes                      |
| ------- | ---------------------- | ------- | -------------------------- |
| `+0x00` | u32                    | count   | Number of category records |
| `+0x04` | Category Record[count] | records | See Category Record        |

### Category Record (variable: 27 bytes + icon path)

Offsets are relative to `record_offset` from `maincategoryoffset.dbss`. Field Names gives the source of each name.

| Offset           | Type | Field          | Notes                                                                                        |
| ---------------- | ---- | -------------- | -------------------------------------------------------------------------------------------- |
| `+0x00`          | u16  | category_id    | Primary key; matches offset-table key                                                        |
| `+0x02`          | u32  | display_order  | Tab position; the shop sorts the tabs by it, ascending                                       |
| `+0x06`          | u32  | tab_image_no   | Tab button style: the shop copies the `RadioButton_CategoryTab_<tab_image_no>` control       |
| `+0x0A`          | u32  | category_type  | `CppEnums.CashProductCategory` value, see Category Type; `0` for a category without a type   |
| `+0x0E`          | str8 | icon_path      | ASCII DDS path under `ui_texture/`; u64 byte length, no null terminator                      |
| `icon_path+0x00` | u32  | event_category | Event cart key the shop checks with `IngameCashShop_CheckOpenEventCart`; `0` for none        |
| `icon_path+0x04` | u8   | is_display     | `0` hides the category's tab; the name rests on width and the Lua getter, see Field Names    |

Earlier versions of this doc called `display_order`, `tab_image_no`, `category_type` and `event_category` `unknown_02`, `unknown_06`, `unknown_0a` and `unknown_after_icon_path`, and `is_display` `enabled_flag`, then `unknown_icon_path_04`.

The record size is `0x16 + icon_path length + 5`. Every icon path on client 3474 is 75 bytes, so every record is 102 bytes, but the path is length-prefixed and is read as variable-length.

### `maincategoryoffset.dbss`

Provides keyed lookup into `maincategory.dbss` and supplies the record count.

| Offset  | Type                 | Field | Notes                         |
| ------- | -------------------- | ----- | ----------------------------- |
| `+0x00` | u32                  | count | Number of category records    |
| `+0x04` | Offset Record[count] | rows  | See Offset Record; no trailer |

### Offset Record (10 bytes)

| Offset  | Type | Field         | Notes                                       |
| ------- | ---- | ------------- | ------------------------------------------- |
| `+0x00` | u16  | category_id   | Key for the category record                 |
| `+0x02` | u32  | record_offset | Absolute byte offset in `maincategory.dbss` |
| `+0x06` | u16  | record_size   | Size of the record in bytes                 |
| `+0x08` | u16  | unknown_08    | Always 0                                    |

Rows are stored in descending category ID order, the highest ID first.

## Layout 1

On client 1784 a category record ends after `event_category`: it has no `is_display` byte, so `record_size` is 101. Only the Category Record differs from Layout 2.

### Category Record (variable: 26 bytes + icon path)

| Offset           | Type | Field          | Notes                                 |
| ---------------- | ---- | -------------- | ------------------------------------- |
| `+0x00`          | u16  | category_id    | Primary key; matches offset-table key |
| `+0x02`          | u32  | display_order  |                                       |
| `+0x06`          | u32  | tab_image_no   |                                       |
| `+0x0A`          | u32  | category_type  |                                       |
| `+0x0E`          | str8 | icon_path      | ASCII DDS path                        |
| `icon_path+0x00` | u32  | event_category | 0, 3 or 4 on client 1784              |

## Category Type

The in-game shop (`panel_ingamecashshop.luac`) compares `getCategoryType()` with `CppEnums.CashProductCategory` from `global_define_cpp_enum.luac`, for example `eCashProductCategory_Pearl` to find the tab that sells pearls. The enum on client 3474:

| Value | Member                           |
| ----- | -------------------------------- |
| 1     | `eCashProductCategory_Pearl`     |
| 2     | `eCashProductCategory_Mileage`   |
| 3     | `eCashProductCategory_Normal`    |
| 4     | `eCashProductCategory_Costumes`  |
| 5     | `eCashProductCategory_Furniture` |
| 6     | `eCashProductCategory_Servant`   |
| 7     | `eCashProductCategory_Pet`       |
| 8     | `eCashProductCategory_Beauty`    |
| 9     | `eCashProductCategory_HotNew`    |
| 15    | `eCashProductCategory_StepUp`    |

The 2016 client's `enum gc::CashProductCategory : unsigned char` numbers the same first seven members from `0` and ends with `eCashProductCategory_Customize = 7` and `eCashProductCategory_Dye = 8`, so its values do not apply to this file.

## Field Names

The record is one row of the `MainCategory_Table` sheet of a private server on client 1784, in its `DataSheets.bexcel`. The sheet's columns are `Index`, `Display_Order`, `Tab_ImageNo`, `EventCategory`, `EventSlotCategory`, `CategoryType` and `IconPath`; no `.xlsm` in its `DataSheet` folder holds the sheet. The official client 1784 file is byte-identical to that server's compiled `maincategory.dbss`. I matched every record field against every column by value over the shared category IDs:

| Field            | Column          | Lua getter          | Equal, client 1784 | Equal, client 3474 |
| ---------------- | --------------- | ------------------- | ------------------ | ------------------ |
| `category_id`    | `Index`         | `getNoRaw()`        | 12 of 12           | 12 of 12           |
| `display_order`  | `Display_Order` | `getDisplayOrder()` | 12 of 12           | 10 of 12           |
| `tab_image_no`   | `Tab_ImageNo`   | `getTabImageNo()`   | 12 of 12           | 12 of 12           |
| `category_type`  | `CategoryType`  | `getCategoryType()` | 12 of 12           | 12 of 12           |
| `icon_path`      | `IconPath`      | `getIconPath()`     | 12 of 12           | 12 of 12           |
| `event_category` | `EventCategory` | `getEventKey()`     | 12 of 12           | 10 of 12           |
| `is_display`     |                 | `isDisplay()`       |                    |                    |

On client 3474, categories 1 and 10 swap display orders 3 and 4 against the sheet, and `event_category` is `0` on every record. A private server on client 519 has the same `MainCategory_Table` columns in its `bdo.sqlite3`, with all 12 rows equal to the 1784 sheet except `EventCategory`, which is empty there. The 2016 client's debug symbols have no main category static status, and the 1784 server dump (`Instance_dumpFull.exe`) names the manager `MainCategoryStaticStatusManager`; I did not trace its row reader, since every Layout 1 field matches a column by value.

The Lua getters come from `panel_ingamecashshop.luac`, which reads, per category from `ToClient_GetMainCategoryStaticStatusWrapperByKeyRaw`, `getDisplayOrder()`, `getNoRaw()`, `getTabImageNo()`, `getIconPath()`, `getCategoryType()`, `getEventKey()`, `getEventSlotKey()` and `isDisplay()`. It passes both event keys to `IngameCashShop_CheckOpenEventCart`.

`is_display` has no sheet column, so its name rests on width and the Lua, not on values. The client 1784 Lua already calls `isDisplay()` and `getEventSlotKey()` on each category although the 1784 file stores neither, and Layout 2 adds exactly one byte, which holds only `0` and `1` on client 3474. `inGameShop:initTabPos` hides the tab of a category whose `isDisplay()` is false, and the shop counts it in `_hideTabCount`. On client 3474 the two categories with the byte at `0`, 13 and 14, have the two highest display orders, 13 and 14. `EventSlotCategory` (`getEventSlotKey()`) is empty in the 1784 sheet and has no field in either layout; an event key like `EventCategory` is a u32 in the file, not a byte.

## Observed Records

The records on client 3474:

| Category ID | display_order | tab_image_no | category_type | event_category | is_display | Icon Path                                                                     |
| ----------- | ------------- | ------------ | ------------- | -------------- | ---------- | ----------------------------------------------------------------------------- |
| 1           | 3             | 2            | 1             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_02.dds` |
| 2           | 5             | 0            | 2             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_03.dds` |
| 3           | 6             | 0            | 3             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_04.dds` |
| 4           | 8             | 0            | 4             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_05.dds` |
| 5           | 9             | 0            | 5             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_08.dds` |
| 6           | 10            | 0            | 6             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_07.dds` |
| 7           | 11            | 0            | 7             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_06.dds` |
| 8           | 12            | 0            | 8             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_09.dds` |
| 9           | 1             | 1            | 9             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_14.dds` |
| 10          | 4             | 3            | 0             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_12.dds` |
| 11          | 7             | 0            | 0             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_01.dds` |
| 12          | 2             | 5            | 0             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_01.dds` |
| 13          | 13            | 6            | 0             | 0              | 0          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_17.dds` |
| 14          | 14            | 0            | 0             | 0              | 0          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_18.dds` |
| 15          | 5             | 6            | 15            | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_19.dds` |

## Notes

- `maincategoryoffset.dbss` is required because it gives the authoritative category IDs and record sizes.
- The shop takes a tab's name from `getCashCategoryName(getNoRaw(), CppEnums.CashProductCategoryNo_Undefined)`, not from this file.

## Open Questions

### Category Type 0

Categories 10 to 14 have `category_type` `0` on client 3474, a value no `CppEnums.CashProductCategory` member uses. What the shop does differently for them is not known.

### Category Names

`getCashCategoryName` is a client function; which file it reads the category names from is not known.

## In-Game Checks

### Hidden Tabs

This settles whether `is_display` `0` hides a main category tab. The name rests on the field width and the Lua getter `isDisplay()`, not on a sheet column.

1. Open the Pearl Shop.
2. Compare the main category tab icons with the Observed Records.

On client 3474 no tab shows the `CashShopMenu_17.dds` or `CashShopMenu_18.dds` icon (categories 13 and 14) when `0` hides a tab. A tab with one of those icons means the byte is something else.
