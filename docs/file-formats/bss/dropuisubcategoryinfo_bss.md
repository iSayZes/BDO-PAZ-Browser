# `dropuisubcategoryinfo.bss` Format

## Purpose

The filter categories of the drop item window (Monster Zone Info): one fixed
row per filter button with its Korean name and button icon.
[`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) lists the
categories of each hunting ground in `sub_category_keys`. LOC type 115 names
the categories by key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                        | Bytes | Records        | Row bytes |
| ------ | -------------- | --------------------------- | ----- | -------------- | --------- |
| 1      | 1914 and later | `dropuisubcategoryinfo.bss` | 609   | 8 Category Row | 12        |

| Layout | File                        | Known          | Unknown    |
| ------ | --------------------------- | -------------- | ---------- |
| 1      | `dropuisubcategoryinfo.bss` | 609 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `8a0e5e03e7d8`  |
| 3482   | Layout 1 | `8a0e5e03e7d8`  |
| 3474   | Layout 1 | `8a0e5e03e7d8`  |
| 3473   | Layout 1 | `8a0e5e03e7d8`  |
| 3464   | Layout 1 | `8a0e5e03e7d8`  |
| 3458   | Layout 1 | `8a0e5e03e7d8`  |
| 3454   | Layout 1 | `8a0e5e03e7d8`  |
| 3444   | Layout 1 | `8a0e5e03e7d8`  |
| 3435   | Layout 1 | `8a0e5e03e7d8`  |
| 3426   | Layout 1 | `8a0e5e03e7d8`  |
| 3418   | Layout 1 | `8a0e5e03e7d8`  |
| 3412   | Layout 1 | `8a0e5e03e7d8`  |
| 3402   | Layout 1 | `8a0e5e03e7d8`  |
| 3396   | Layout 1 | `8a0e5e03e7d8`  |
| 3387   | Layout 1 | `8a0e5e03e7d8`  |
| 3381   | Layout 1 | `8a0e5e03e7d8`  |
| 3373   | Layout 1 | `8a0e5e03e7d8`  |
| 3364   | Layout 1 | `8a0e5e03e7d8`  |
| 3356   | Layout 1 | `8a0e5e03e7d8`  |
| 3349   | Layout 1 | `8a0e5e03e7d8`  |
| 3342   | Layout 1 | `8a0e5e03e7d8`  |
| 3335   | Layout 1 | `8a0e5e03e7d8`  |
| 3326   | Layout 1 | `8a0e5e03e7d8`  |
| 3321   | Layout 1 | `8a0e5e03e7d8`  |
| 3314   | Layout 1 | `8a0e5e03e7d8`  |
| 3303   | Layout 1 | `8a0e5e03e7d8`  |
| 3302   | Layout 1 | `8a0e5e03e7d8`  |
| 3293   | Layout 1 | `8a0e5e03e7d8`  |
| 3283   | Layout 1 | `8a0e5e03e7d8`  |
| 3275   | Layout 1 | `8a0e5e03e7d8`  |
| 3267   | Layout 1 | `8a0e5e03e7d8`  |
| 3258   | Layout 1 | `8a0e5e03e7d8`  |
| 3251   | Layout 1 | `8a0e5e03e7d8`  |
| 3242   | Layout 1 | `8a0e5e03e7d8`  |
| 3235   | Layout 1 | `8a0e5e03e7d8`  |
| 3229   | Layout 1 | `8a0e5e03e7d8`  |
| 3212   | Layout 1 | `8a0e5e03e7d8`  |
| 3203   | Layout 1 | `8a0e5e03e7d8`  |
| 3193   | Layout 1 | `8a0e5e03e7d8`  |
| 3186   | Layout 1 | `8a0e5e03e7d8`  |
| 3177   | Layout 1 | `8a0e5e03e7d8`  |
| 3169   | Layout 1 | `8a0e5e03e7d8`  |
| 3158   | Layout 1 | `8a0e5e03e7d8`  |
| 3151   | Layout 1 | `8a0e5e03e7d8`  |
| 3144   | Layout 1 | `8a0e5e03e7d8`  |
| 3133   | Layout 1 | `8a0e5e03e7d8`  |
| 3125   | Layout 1 | `8a0e5e03e7d8`  |
| 3118   | Layout 1 | `8a0e5e03e7d8`  |
| 3111   | Layout 1 | `8a0e5e03e7d8`  |
| 3103   | Layout 1 | `8a0e5e03e7d8`  |
| 3095   | Layout 1 | `8a0e5e03e7d8`  |
| 3086   | Layout 1 | `8a0e5e03e7d8`  |
| 3072   | Layout 1 | `8a0e5e03e7d8`  |
| 3062   | Layout 1 | `8a0e5e03e7d8`  |
| 3052   | Layout 1 | `8a0e5e03e7d8`  |
| 3045   | Layout 1 | `8a0e5e03e7d8`  |
| 3037   | Layout 1 | `8a0e5e03e7d8`  |
| 3030   | Layout 1 | `8a0e5e03e7d8`  |
| 3021   | Layout 1 | `8a0e5e03e7d8`  |
| 3012   | Layout 1 | `8a0e5e03e7d8`  |
| 3002   | Layout 1 | `8a0e5e03e7d8`  |
| 2995   | Layout 1 | `8a0e5e03e7d8`  |
| 2987   | Layout 1 | `8a0e5e03e7d8`  |
| 2978   | Layout 1 | `8a0e5e03e7d8`  |
| 2970   | Layout 1 | `8a0e5e03e7d8`  |
| 2959   | Layout 1 | `8a0e5e03e7d8`  |
| 2951   | Layout 1 | `8a0e5e03e7d8`  |
| 2942   | Layout 1 | `8a0e5e03e7d8`  |
| 2935   | Layout 1 | `8a0e5e03e7d8`  |
| 2932   | Layout 1 | `8a0e5e03e7d8`  |
| 2923   | Layout 1 | `8a0e5e03e7d8`  |
| 2919   | Layout 1 | `8a0e5e03e7d8`  |
| 2907   | Layout 1 | `8a0e5e03e7d8`  |
| 2900   | Layout 1 | `8a0e5e03e7d8`  |
| 2891   | Layout 1 | `8a0e5e03e7d8`  |
| 2882   | Layout 1 | `8a0e5e03e7d8`  |
| 2872   | Layout 1 | `8a0e5e03e7d8`  |
| 2863   | Layout 1 | `8a0e5e03e7d8`  |
| 2855   | Layout 1 | `8a0e5e03e7d8`  |
| 2849   | Layout 1 | `8a0e5e03e7d8`  |
| 2844   | Layout 1 | `8a0e5e03e7d8`  |
| 2834   | Layout 1 | `8a0e5e03e7d8`  |
| 2825   | Layout 1 | `8a0e5e03e7d8`  |
| 2819   | Layout 1 | `8a0e5e03e7d8`  |
| 2811   | Layout 1 | `8a0e5e03e7d8`  |
| 2803   | Layout 1 | `8a0e5e03e7d8`  |
| 2794   | Layout 1 | `8a0e5e03e7d8`  |
| 2783   | Layout 1 | `8a0e5e03e7d8`  |
| 2774   | Layout 1 | `8a0e5e03e7d8`  |
| 2765   | Layout 1 | `8a0e5e03e7d8`  |
| 2756   | Layout 1 | `8a0e5e03e7d8`  |
| 2750   | Layout 1 | `8a0e5e03e7d8`  |
| 2743   | Layout 1 | `8a0e5e03e7d8`  |
| 2736   | Layout 1 | `8a0e5e03e7d8`  |
| 2726   | Layout 1 | `8a0e5e03e7d8`  |
| 2717   | Layout 1 | `8a0e5e03e7d8`  |
| 2709   | Layout 1 | `8a0e5e03e7d8`  |
| 2703   | Layout 1 | `8a0e5e03e7d8`  |
| 2695   | Layout 1 | `8a0e5e03e7d8`  |
| 2684   | Layout 1 | `8a0e5e03e7d8`  |
| 2672   | Layout 1 | `8a0e5e03e7d8`  |
| 2665   | Layout 1 | `8a0e5e03e7d8`  |
| 2657   | Layout 1 | `8a0e5e03e7d8`  |
| 2649   | Layout 1 | `8a0e5e03e7d8`  |
| 2644   | Layout 1 | `8a0e5e03e7d8`  |
| 2637   | Layout 1 | `8a0e5e03e7d8`  |
| 2629   | Layout 1 | `8a0e5e03e7d8`  |
| 2619   | Layout 1 | `8a0e5e03e7d8`  |
| 2612   | Layout 1 | `8a0e5e03e7d8`  |
| 2606   | Layout 1 | `8a0e5e03e7d8`  |
| 2602   | Layout 1 | `8a0e5e03e7d8`  |
| 2601   | Layout 1 | `8a0e5e03e7d8`  |
| 2592   | Layout 1 | `8a0e5e03e7d8`  |
| 2583   | Layout 1 | `8a0e5e03e7d8`  |
| 2575   | Layout 1 | `8a0e5e03e7d8`  |
| 2567   | Layout 1 | `8a0e5e03e7d8`  |
| 2560   | Layout 1 | `8a0e5e03e7d8`  |
| 2553   | Layout 1 | `8a0e5e03e7d8`  |
| 2545   | Layout 1 | `8a0e5e03e7d8`  |
| 2538   | Layout 1 | `8a0e5e03e7d8`  |
| 2529   | Layout 1 | `8a0e5e03e7d8`  |
| 2519   | Layout 1 | `8a0e5e03e7d8`  |
| 2513   | Layout 1 | `8a0e5e03e7d8`  |
| 2510   | Layout 1 | `8a0e5e03e7d8`  |
| 2507   | Layout 1 | `8a0e5e03e7d8`  |
| 2503   | Layout 1 | `8a0e5e03e7d8`  |
| 2498   | Layout 1 | `8a0e5e03e7d8`  |
| 2492   | Layout 1 | `8a0e5e03e7d8`  |
| 2487   | Layout 1 | `8a0e5e03e7d8`  |
| 2480   | Layout 1 | `8a0e5e03e7d8`  |
| 2474   | Layout 1 | `8a0e5e03e7d8`  |
| 2468   | Layout 1 | `8a0e5e03e7d8`  |
| 2460   | Layout 1 | `8a0e5e03e7d8`  |
| 2453   | Layout 1 | `8a0e5e03e7d8`  |
| 2444   | Layout 1 | `8a0e5e03e7d8`  |
| 2438   | Layout 1 | `8a0e5e03e7d8`  |
| 2434   | Layout 1 | `8a0e5e03e7d8`  |
| 2429   | Layout 1 | `8a0e5e03e7d8`  |
| 2421   | Layout 1 | `8a0e5e03e7d8`  |
| 2414   | Layout 1 | `8a0e5e03e7d8`  |
| 2407   | Layout 1 | `8a0e5e03e7d8`  |
| 2401   | Layout 1 | `8a0e5e03e7d8`  |
| 2397   | Layout 1 | `8a0e5e03e7d8`  |
| 2393   | Layout 1 | `8a0e5e03e7d8`  |
| 2384   | Layout 1 | `8a0e5e03e7d8`  |
| 2378   | Layout 1 | `8a0e5e03e7d8`  |
| 2372   | Layout 1 | `8a0e5e03e7d8`  |
| 2358   | Layout 1 | `8a0e5e03e7d8`  |
| 2352   | Layout 1 | `8a0e5e03e7d8`  |
| 2347   | Layout 1 | `8a0e5e03e7d8`  |
| 2343   | Layout 1 | `8a0e5e03e7d8`  |
| 2335   | Layout 1 | `8a0e5e03e7d8`  |
| 2327   | Layout 1 | `8a0e5e03e7d8`  |
| 2324   | Layout 1 | `8a0e5e03e7d8`  |
| 2319   | Layout 1 | `8a0e5e03e7d8`  |
| 2313   | Layout 1 | `8a0e5e03e7d8`  |
| 2308   | Layout 1 | `8a0e5e03e7d8`  |
| 2302   | Layout 1 | `8a0e5e03e7d8`  |
| 2295   | Layout 1 | `8a0e5e03e7d8`  |
| 2290   | Layout 1 | `8a0e5e03e7d8`  |
| 2284   | Layout 1 | `8a0e5e03e7d8`  |
| 2276   | Layout 1 | `8a0e5e03e7d8`  |
| 2269   | Layout 1 | `8a0e5e03e7d8`  |
| 2259   | Layout 1 | `8a0e5e03e7d8`  |
| 2250   | Layout 1 | `8a0e5e03e7d8`  |
| 2243   | Layout 1 | `8a0e5e03e7d8`  |
| 2235   | Layout 1 | `8a0e5e03e7d8`  |
| 2229   | Layout 1 | `8a0e5e03e7d8`  |
| 2224   | Layout 1 | `8a0e5e03e7d8`  |
| 2218   | Layout 1 | `8a0e5e03e7d8`  |
| 2215   | Layout 1 | `8a0e5e03e7d8`  |
| 2207   | Layout 1 | `8a0e5e03e7d8`  |
| 2203   | Layout 1 | `8a0e5e03e7d8`  |
| 2196   | Layout 1 | `8a0e5e03e7d8`  |
| 2192   | Layout 1 | `8a0e5e03e7d8`  |
| 2189   | Layout 1 | `8a0e5e03e7d8`  |
| 2183   | Layout 1 | `8a0e5e03e7d8`  |
| 2179   | Layout 1 | `8a0e5e03e7d8`  |
| 2171   | Layout 1 | `8a0e5e03e7d8`  |
| 2163   | Layout 1 | `8a0e5e03e7d8`  |
| 2156   | Layout 1 | `8a0e5e03e7d8`  |
| 2151   | Layout 1 | `8a0e5e03e7d8`  |
| 2147   | Layout 1 | `8a0e5e03e7d8`  |
| 2142   | Layout 1 | `8a0e5e03e7d8`  |
| 2138   | Layout 1 | `8a0e5e03e7d8`  |
| 2134   | Layout 1 | `8a0e5e03e7d8`  |
| 2130   | Layout 1 | `8a0e5e03e7d8`  |
| 2122   | Layout 1 | `8a0e5e03e7d8`  |
| 2107   | Layout 1 | `8a0e5e03e7d8`  |
| 2098   | Layout 1 | `8a0e5e03e7d8`  |
| 2089   | Layout 1 | `8a0e5e03e7d8`  |
| 2081   | Layout 1 | `8a0e5e03e7d8`  |
| 2073   | Layout 1 | `8a0e5e03e7d8`  |
| 2067   | Layout 1 | `8a0e5e03e7d8`  |
| 2063   | Layout 1 | `8a0e5e03e7d8`  |
| 2059   | Layout 1 | `8a0e5e03e7d8`  |
| 2052   | Layout 1 | `8a0e5e03e7d8`  |
| 2044   | Layout 1 | `8a0e5e03e7d8`  |
| 2039   | Layout 1 | `8a0e5e03e7d8`  |
| 2032   | Layout 1 | `8a0e5e03e7d8`  |
| 2025   | Layout 1 | `8a0e5e03e7d8`  |
| 2011   | Layout 1 | `8a0e5e03e7d8`  |
| 2005   | Layout 1 | `8a0e5e03e7d8`  |
| 2000   | Layout 1 | `8a0e5e03e7d8`  |
| 1996   | Layout 1 | `8a0e5e03e7d8`  |
| 1991   | Layout 1 | `8a0e5e03e7d8`  |
| 1985   | Layout 1 | `8a0e5e03e7d8`  |
| 1980   | Layout 1 | `8a0e5e03e7d8`  |
| 1969   | Layout 1 | `8a0e5e03e7d8`  |
| 1964   | Layout 1 | `8a0e5e03e7d8`  |
| 1958   | Layout 1 | `8a0e5e03e7d8`  |
| 1950   | Layout 1 | `8a0e5e03e7d8`  |
| 1945   | Layout 1 | `8a0e5e03e7d8`  |
| 1937   | Layout 1 | `8a0e5e03e7d8`  |
| 1933   | Layout 1 | `8a0e5e03e7d8`  |
| 1927   | Layout 1 | `8a0e5e03e7d8`  |
| 1921   | Layout 1 | `8a0e5e03e7d8`  |
| 1914   | Layout 1 | `8a0e5e03e7d8`  |
| 1908   | No file  | `8a0e5e03e7d8`  |
| 1897   | No file  | `8a0e5e03e7d8`  |
| 1892   | No file  | `8a0e5e03e7d8`  |
| 1886   | No file  | `8a0e5e03e7d8`  |
| 1881   | No file  | `8a0e5e03e7d8`  |
| 1871   | No file  | `8a0e5e03e7d8`  |
| 1866   | No file  | `8a0e5e03e7d8`  |
| 1862   | No file  | `8a0e5e03e7d8`  |
| 1854   | No file  | `8a0e5e03e7d8`  |
| 1846   | No file  | `8a0e5e03e7d8`  |
| 1838   | No file  | `8a0e5e03e7d8`  |
| 1832   | No file  | `8a0e5e03e7d8`  |
| 1826   | No file  | `8a0e5e03e7d8`  |
| 1822   | No file  | `8a0e5e03e7d8`  |
| 1818   | No file  | `8a0e5e03e7d8`  |
| 1804   | No file  | `8a0e5e03e7d8`  |
| 1794   | No file  | `8a0e5e03e7d8`  |
| 1790   | No file  | `8a0e5e03e7d8`  |
| 1784   | No file  | `8a0e5e03e7d8`  |
| 1774   | No file  | `8a0e5e03e7d8`  |
| 1771   | No file  | `8a0e5e03e7d8`  |
| 1762   | No file  | `8a0e5e03e7d8`  |
| 1759   | No file  | `8a0e5e03e7d8`  |
| 1754   | No file  | `8a0e5e03e7d8`  |
| 1749   | No file  | `8a0e5e03e7d8`  |
| 1743   | No file  | `8a0e5e03e7d8`  |
| 1737   | No file  | `8a0e5e03e7d8`  |
| 1731   | No file  | `8a0e5e03e7d8`  |
| 1725   | No file  | `8a0e5e03e7d8`  |
| 1717   | No file  | `8a0e5e03e7d8`  |
| 1710   | No file  | `8a0e5e03e7d8`  |
| 1704   | No file  | `8a0e5e03e7d8`  |
| 1698   | No file  | `8a0e5e03e7d8`  |
| 1690   | No file  | `8a0e5e03e7d8`  |
| 1685   | No file  | `8a0e5e03e7d8`  |
| 1680   | No file  | `8a0e5e03e7d8`  |
| 1674   | No file  | `8a0e5e03e7d8`  |
| 1668   | No file  | `8a0e5e03e7d8`  |
| 1659   | No file  | `8a0e5e03e7d8`  |
| 1649   | No file  | `8a0e5e03e7d8`  |
| 1642   | No file  | `8a0e5e03e7d8`  |
| 1636   | No file  | `8a0e5e03e7d8`  |
| 1628   | No file  | `8a0e5e03e7d8`  |
| 1622   | No file  | `8a0e5e03e7d8`  |
| 1614   | No file  | `8a0e5e03e7d8`  |
| 1608   | No file  | `8a0e5e03e7d8`  |
| 1602   | No file  | `8a0e5e03e7d8`  |
| 1598   | No file  | `8a0e5e03e7d8`  |
| 1594   | No file  | `8a0e5e03e7d8`  |
| 1590   | No file  | `8a0e5e03e7d8`  |
| 1587   | No file  | `8a0e5e03e7d8`  |
| 1584   | No file  | `8a0e5e03e7d8`  |
| 1579   | No file  | `8a0e5e03e7d8`  |
| 1572   | No file  | `8a0e5e03e7d8`  |
| 1565   | No file  | `8a0e5e03e7d8`  |
| 1559   | No file  | `8a0e5e03e7d8`  |
| 1554   | No file  | `8a0e5e03e7d8`  |
| 1547   | No file  | `8a0e5e03e7d8`  |
| 1537   | No file  | `8a0e5e03e7d8`  |
| 1529   | No file  | `8a0e5e03e7d8`  |
| 1524   | No file  | `8a0e5e03e7d8`  |
| 1519   | No file  | `8a0e5e03e7d8`  |
| 1509   | No file  | `8a0e5e03e7d8`  |
| 1506   | No file  | `8a0e5e03e7d8`  |
| 1504   | No file  | `8a0e5e03e7d8`  |
| 1500   | No file  | `8a0e5e03e7d8`  |
| 1493   | No file  | `8a0e5e03e7d8`  |
| 1489   | No file  | `8a0e5e03e7d8`  |
| 1485   | No file  | `8a0e5e03e7d8`  |
| 1481   | No file  | `8a0e5e03e7d8`  |
| 1474   | No file  | `8a0e5e03e7d8`  |
| 1466   | No file  | `8a0e5e03e7d8`  |
| 1462   | No file  | `8a0e5e03e7d8`  |
| 1459   | No file  | `8a0e5e03e7d8`  |
| 1453   | No file  | `8a0e5e03e7d8`  |
| 1450   | No file  | `8a0e5e03e7d8`  |
| 1445   | No file  | `8a0e5e03e7d8`  |
| 1439   | No file  | `8a0e5e03e7d8`  |
| 1433   | No file  | `8a0e5e03e7d8`  |
| 1430   | No file  | `8a0e5e03e7d8`  |
| 1426   | No file  | `8a0e5e03e7d8`  |
| 1421   | No file  | `8a0e5e03e7d8`  |
| 1417   | No file  | `8a0e5e03e7d8`  |
| 1416   | No file  | `8a0e5e03e7d8`  |
| 1409   | No file  | `8a0e5e03e7d8`  |
| 1405   | No file  | `8a0e5e03e7d8`  |
| 1401   | No file  | `8a0e5e03e7d8`  |
| 1396   | No file  | `8a0e5e03e7d8`  |
| 1391   | No file  | `8a0e5e03e7d8`  |
| 1390   | No file  | `8a0e5e03e7d8`  |
| 1386   | No file  | `8a0e5e03e7d8`  |
| 1381   | No file  | `8a0e5e03e7d8`  |
| 1379   | No file  | `8a0e5e03e7d8`  |
| 1372   | No file  | `8a0e5e03e7d8`  |
| 1366   | No file  | `8a0e5e03e7d8`  |
| 1364   | No file  | `8a0e5e03e7d8`  |
| 1363   | No file  | `8a0e5e03e7d8`  |
| 1360   | No file  | `8a0e5e03e7d8`  |
| 1358   | No file  | `8a0e5e03e7d8`  |
| 1355   | No file  | `8a0e5e03e7d8`  |
| 1351   | No file  | `8a0e5e03e7d8`  |
| 1348   | No file  | `8a0e5e03e7d8`  |
| 1346   | No file  | `8a0e5e03e7d8`  |
| 1341   | No file  | `8a0e5e03e7d8`  |
| 1340   | No file  | `8a0e5e03e7d8`  |
| 1338   | No file  | `8a0e5e03e7d8`  |
| 1335   | No file  | `8a0e5e03e7d8`  |
| 1333   | No file  | `8a0e5e03e7d8`  |
| 1329   | No file  | `8a0e5e03e7d8`  |
| 1327   | No file  | `8a0e5e03e7d8`  |
| 1324   | No file  | `8a0e5e03e7d8`  |
| 1321   | No file  | `8a0e5e03e7d8`  |
| 1319   | No file  | `8a0e5e03e7d8`  |
| 1318   | No file  | `8a0e5e03e7d8`  |
| 1316   | No file  | `8a0e5e03e7d8`  |
| 1313   | No file  | `8a0e5e03e7d8`  |
| 1311   | No file  | `8a0e5e03e7d8`  |
| 1309   | No file  | `8a0e5e03e7d8`  |
| 1304   | No file  | `8a0e5e03e7d8`  |
| 1292   | No file  | `8a0e5e03e7d8`  |
| 1286   | No file  | `8a0e5e03e7d8`  |
| 1280   | No file  | `8a0e5e03e7d8`  |
| 1276   | No file  | `8a0e5e03e7d8`  |
| 1267   | No file  | `8a0e5e03e7d8`  |
| 1261   | No file  | `8a0e5e03e7d8`  |
| 1256   | No file  | `8a0e5e03e7d8`  |
| 1250   | No file  | `8a0e5e03e7d8`  |
| 1246   | No file  | `8a0e5e03e7d8`  |
| 1239   | No file  | `8a0e5e03e7d8`  |
| 1230   | No file  | `8a0e5e03e7d8`  |
| 1226   | No file  | `8a0e5e03e7d8`  |
| 1220   | No file  | `8a0e5e03e7d8`  |
| 1217   | No file  | `8a0e5e03e7d8`  |
| 1211   | No file  | `8a0e5e03e7d8`  |
| 1210   | No file  | `8a0e5e03e7d8`  |
| 1208   | No file  | `8a0e5e03e7d8`  |
| 1203   | No file  | `8a0e5e03e7d8`  |
| 1197   | No file  | `8a0e5e03e7d8`  |
| 1194   | No file  | `8a0e5e03e7d8`  |
| 1192   | No file  | `8a0e5e03e7d8`  |
| 1187   | No file  | `8a0e5e03e7d8`  |
| 1183   | No file  | `8a0e5e03e7d8`  |
| 1177   | No file  | `8a0e5e03e7d8`  |
| 1173   | No file  | `8a0e5e03e7d8`  |
| 1167   | No file  | `8a0e5e03e7d8`  |
| 1164   | No file  | `8a0e5e03e7d8`  |
| 1156   | No file  | `8a0e5e03e7d8`  |
| 1149   | No file  | `8a0e5e03e7d8`  |
| 1144   | No file  | `8a0e5e03e7d8`  |
| 1137   | No file  | `8a0e5e03e7d8`  |
| 1132   | No file  | `8a0e5e03e7d8`  |
| 1127   | No file  | `8a0e5e03e7d8`  |
| 1122   | No file  | `8a0e5e03e7d8`  |
| 1118   | No file  | `8a0e5e03e7d8`  |
| 1114   | No file  | `8a0e5e03e7d8`  |
| 1109   | No file  | `8a0e5e03e7d8`  |
| 1102   | No file  | `8a0e5e03e7d8`  |
| 1096   | No file  | `8a0e5e03e7d8`  |
| 1088   | No file  | `8a0e5e03e7d8`  |
| 1081   | No file  | `8a0e5e03e7d8`  |
| 1076   | No file  | `8a0e5e03e7d8`  |
| 1069   | No file  | `8a0e5e03e7d8`  |
| 1064   | No file  | `8a0e5e03e7d8`  |
| 1058   | No file  | `8a0e5e03e7d8`  |
| 1051   | No file  | `8a0e5e03e7d8`  |
| 1044   | No file  | `8a0e5e03e7d8`  |
| 1036   | No file  | `8a0e5e03e7d8`  |
| 1026   | No file  | `8a0e5e03e7d8`  |
| 1016   | No file  | `8a0e5e03e7d8`  |
| 1009   | No file  | `8a0e5e03e7d8`  |
| 1005   | No file  | `8a0e5e03e7d8`  |
| 1000   | No file  | `8a0e5e03e7d8`  |
| 998    | No file  | `8a0e5e03e7d8`  |
| 990    | No file  | `8a0e5e03e7d8`  |
| 979    | No file  | `8a0e5e03e7d8`  |
| 972    | No file  | `8a0e5e03e7d8`  |
| 963    | No file  | `8a0e5e03e7d8`  |
| 955    | No file  | `8a0e5e03e7d8`  |
| 946    | No file  | `8a0e5e03e7d8`  |
| 938    | No file  | `8a0e5e03e7d8`  |
| 927    | No file  | `8a0e5e03e7d8`  |
| 911    | No file  | `8a0e5e03e7d8`  |
| 904    | No file  | `8a0e5e03e7d8`  |
| 899    | No file  | `8a0e5e03e7d8`  |
| 894    | No file  | `8a0e5e03e7d8`  |
| 885    | No file  | `8a0e5e03e7d8`  |
| 879    | No file  | `8a0e5e03e7d8`  |
| 872    | No file  | `8a0e5e03e7d8`  |
| 864    | No file  | `8a0e5e03e7d8`  |
| 855    | No file  | `8a0e5e03e7d8`  |
| 853    | No file  | `8a0e5e03e7d8`  |
| 845    | No file  | `8a0e5e03e7d8`  |
| 837    | No file  | `8a0e5e03e7d8`  |
| 829    | No file  | `8a0e5e03e7d8`  |
| 822    | No file  | `8a0e5e03e7d8`  |
| 814    | No file  | `8a0e5e03e7d8`  |
| 805    | No file  | `8a0e5e03e7d8`  |
| 794    | No file  | `8a0e5e03e7d8`  |
| 787    | No file  | `8a0e5e03e7d8`  |
| 780    | No file  | `8a0e5e03e7d8`  |
| 771    | No file  | `8a0e5e03e7d8`  |
| 760    | No file  | `8a0e5e03e7d8`  |
| 748    | No file  | `8a0e5e03e7d8`  |
| 741    | No file  | `8a0e5e03e7d8`  |
| 736    | No file  | `8a0e5e03e7d8`  |
| 731    | No file  | `8a0e5e03e7d8`  |
| 723    | No file  | `8a0e5e03e7d8`  |
| 711    | No file  | `8a0e5e03e7d8`  |
| 707    | No file  | `8a0e5e03e7d8`  |
| 697    | No file  | `8a0e5e03e7d8`  |
| 689    | No file  | `8a0e5e03e7d8`  |
| 683    | No file  | `8a0e5e03e7d8`  |
| 678    | No file  | `8a0e5e03e7d8`  |
| 670    | No file  | `8a0e5e03e7d8`  |
| 661    | No file  | `8a0e5e03e7d8`  |
| 656    | No file  | `8a0e5e03e7d8`  |
| 652    | No file  | `8a0e5e03e7d8`  |
| 643    | No file  | `8a0e5e03e7d8`  |
| 637    | No file  | `8a0e5e03e7d8`  |
| 630    | No file  | `8a0e5e03e7d8`  |
| 627    | No file  | `8a0e5e03e7d8`  |
| 621    | No file  | `8a0e5e03e7d8`  |
| 617    | No file  | `8a0e5e03e7d8`  |
| 615    | No file  | `8a0e5e03e7d8`  |
| 606    | No file  | `8a0e5e03e7d8`  |
| 599    | No file  | `8a0e5e03e7d8`  |
| 592    | No file  | `8a0e5e03e7d8`  |
| 586    | No file  | `8a0e5e03e7d8`  |
| 577    | No file  | `8a0e5e03e7d8`  |
| 569    | No file  | `8a0e5e03e7d8`  |
| 561    | No file  | `8a0e5e03e7d8`  |
| 554    | No file  | `8a0e5e03e7d8`  |
| 542    | No file  | `8a0e5e03e7d8`  |
| 532    | No file  | `8a0e5e03e7d8`  |
| 531    | No file  | `8a0e5e03e7d8`  |
| 526    | No file  | `8a0e5e03e7d8`  |
| 521    | No file  | `8a0e5e03e7d8`  |
| 517    | No file  | `8a0e5e03e7d8`  |
| 510    | No file  | `8a0e5e03e7d8`  |
| 508    | No file  | `8a0e5e03e7d8`  |
| 504    | No file  | `8a0e5e03e7d8`  |
| 497    | No file  | `8a0e5e03e7d8`  |
| 491    | No file  | `8a0e5e03e7d8`  |
| 485    | No file  | `8a0e5e03e7d8`  |
| 478    | No file  | `8a0e5e03e7d8`  |
| 472    | No file  | `8a0e5e03e7d8`  |
| 466    | No file  | `8a0e5e03e7d8`  |
| 457    | No file  | `8a0e5e03e7d8`  |
| 452    | No file  | `8a0e5e03e7d8`  |
| 449    | No file  | `8a0e5e03e7d8`  |
| 435    | No file  | `8a0e5e03e7d8`  |

<!-- versions:end -->

## Companion Files

| File                        | Required | Role                                          |
| --------------------------- | -------- | --------------------------------------------- |
| `languagedata_en.loc`       | Optional | Category names (115)                          |
| `texturestring_combine.xml` | Optional | Sprite sheet and rectangle of the button icon |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block of fixed 12-byte rows, followed by the same counted string table
and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table holds 15 strings: the Korean
names and the button icon names.

| Offset              | Type                | Field              | Notes                            |
| ------------------- | ------------------- | ------------------ | -------------------------------- |
| `+0x00`             | char[4]             | magic              | ASCII `PABR`                     |
| `+0x04`             | u32                 | count              | Number of rows; 8 on client 3464 |
| `+0x08`             | Category Row[count] | rows               | See Category Row                 |
| `rows+0x00`         | String Table        | string_table       | 15 wide strings                  |
| `string_table+0x00` | u32                 | string_table_start | Where the rows end               |
| `string_table+0x04` | u32                 | zero               | Always `0`                       |

### Category Row (12 bytes)

| Offset  | Type | Field    | Notes                                                    |
| ------- | ---- | -------- | -------------------------------------------------------- |
| `+0x00` | u32  | key      | Category, 1 to 8; LOC type 115 `str_id1`                 |
| `+0x04` | u32  | name_ref | String table index of the Korean name                    |
| `+0x08` | u32  | icon_ref | String table index of the button icon; 6 and 7 share one |

| Key | Korean               | LOC type 115              | Icon                                           |
| --- | -------------------- | ------------------------- | ---------------------------------------------- |
| 1   | 파티 사냥터          | Party Zones               | `Combine_Etc_DropItem_Icon_Filter_Btn_02_Over` |
| 2   | 엘비아의 영역        | Elvia Realm               | `Combine_Etc_DropItem_Icon_Filter_Btn_03_Over` |
| 3   | 마르니의 밀실        | Marni's Realm             | `Combine_Etc_DropItem_Icon_Filter_Btn_08_Over` |
| 4   | 지역 의뢰            | Region Quests             | `Combine_Etc_DropItem_Icon_Filter_Btn_05_Over` |
| 5   | 추천                 | Suggested                 | `Combine_Etc_DropItem_Icon_Filter_Btn_06_Over` |
| 6   | 데키아의 등불        | Dehkia's Lantern          | `Combine_Etc_DropItem_Icon_Filter_Btn_04_Over` |
| 7   | 데키아의 등불 II     | Dehkia's Lantern II       | `Combine_Etc_DropItem_Icon_Filter_Btn_04_Over` |
| 8   | 엘라 세르빈의 풍경화 | Allan Serbin's Landscape  | `Combine_Etc_DropItem_Icon_Filter_Btn_07_Over` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Notes

- No hunting ground stores 5 or 7 on client 3464.
- The [`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md)
  handler names the categories from LOC type 115 alone and does not read
  this file.
- The icon key is the texture key as stored; the drop window uses it without
  a state suffix (`panel_window_renewdropitem_all_1.luac`).
