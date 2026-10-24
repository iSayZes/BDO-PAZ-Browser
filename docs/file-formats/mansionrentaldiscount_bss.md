# `mansionrentaldiscount.bss` Format

## Purpose

The rental length steps of a mansion contract: a list of (days, discount
percent) and a list of (days, return percent), each with five steps from
1 to 365 days. The mansion contract window
(`panel_window_mansioncontract_all`) takes a contract period of 1 to 365
days, multiplies it by `ToClient_GetMansionPricePerDay()` and shows the
discounted price from `ToClient_GetMansionContractDiscountPrice(days,
price)` when it differs. The file is the same 84 bytes on clients 1784 and
3483.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records                            | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | ---------------------------------- | --------- |
| 1      | 1659 and later | 3483    | `mansionrentaldiscount.bss` | 84    | 5 Rental Percent, 5 Return Percent | 6         |

| Layout | File                        | Known         | Unknown    |
| ------ | --------------------------- | ------------- | ---------- |
| 1      | `mansionrentaldiscount.bss` | 84 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `4c64f2b5e81e`  |
| 3482   | Layout 1 | `4c64f2b5e81e`  |
| 3474   | Layout 1 | `4c64f2b5e81e`  |
| 3473   | Layout 1 | `4c64f2b5e81e`  |
| 3464   | Layout 1 | `4c64f2b5e81e`  |
| 3458   | Layout 1 | `4c64f2b5e81e`  |
| 3454   | Layout 1 | `4c64f2b5e81e`  |
| 3444   | Layout 1 | `4c64f2b5e81e`  |
| 3435   | Layout 1 | `4c64f2b5e81e`  |
| 3426   | Layout 1 | `4c64f2b5e81e`  |
| 3418   | Layout 1 | `4c64f2b5e81e`  |
| 3412   | Layout 1 | `4c64f2b5e81e`  |
| 3402   | Layout 1 | `4c64f2b5e81e`  |
| 3396   | Layout 1 | `4c64f2b5e81e`  |
| 3387   | Layout 1 | `4c64f2b5e81e`  |
| 3381   | Layout 1 | `4c64f2b5e81e`  |
| 3373   | Layout 1 | `4c64f2b5e81e`  |
| 3364   | Layout 1 | `4c64f2b5e81e`  |
| 3356   | Layout 1 | `4c64f2b5e81e`  |
| 3349   | Layout 1 | `4c64f2b5e81e`  |
| 3342   | Layout 1 | `4c64f2b5e81e`  |
| 3335   | Layout 1 | `4c64f2b5e81e`  |
| 3326   | Layout 1 | `4c64f2b5e81e`  |
| 3321   | Layout 1 | `4c64f2b5e81e`  |
| 3314   | Layout 1 | `4c64f2b5e81e`  |
| 3303   | Layout 1 | `4c64f2b5e81e`  |
| 3302   | Layout 1 | `4c64f2b5e81e`  |
| 3293   | Layout 1 | `4c64f2b5e81e`  |
| 3283   | Layout 1 | `4c64f2b5e81e`  |
| 3275   | Layout 1 | `4c64f2b5e81e`  |
| 3267   | Layout 1 | `4c64f2b5e81e`  |
| 3258   | Layout 1 | `4c64f2b5e81e`  |
| 3251   | Layout 1 | `4c64f2b5e81e`  |
| 3242   | Layout 1 | `4c64f2b5e81e`  |
| 3235   | Layout 1 | `4c64f2b5e81e`  |
| 3229   | Layout 1 | `4c64f2b5e81e`  |
| 3212   | Layout 1 | `4c64f2b5e81e`  |
| 3203   | Layout 1 | `4c64f2b5e81e`  |
| 3193   | Layout 1 | `4c64f2b5e81e`  |
| 3186   | Layout 1 | `4c64f2b5e81e`  |
| 3177   | Layout 1 | `4c64f2b5e81e`  |
| 3169   | Layout 1 | `4c64f2b5e81e`  |
| 3158   | Layout 1 | `4c64f2b5e81e`  |
| 3151   | Layout 1 | `4c64f2b5e81e`  |
| 3144   | Layout 1 | `4c64f2b5e81e`  |
| 3133   | Layout 1 | `4c64f2b5e81e`  |
| 3125   | Layout 1 | `4c64f2b5e81e`  |
| 3118   | Layout 1 | `4c64f2b5e81e`  |
| 3111   | Layout 1 | `4c64f2b5e81e`  |
| 3103   | Layout 1 | `4c64f2b5e81e`  |
| 3095   | Layout 1 | `4c64f2b5e81e`  |
| 3086   | Layout 1 | `4c64f2b5e81e`  |
| 3072   | Layout 1 | `4c64f2b5e81e`  |
| 3062   | Layout 1 | `4c64f2b5e81e`  |
| 3052   | Layout 1 | `4c64f2b5e81e`  |
| 3045   | Layout 1 | `4c64f2b5e81e`  |
| 3037   | Layout 1 | `4c64f2b5e81e`  |
| 3030   | Layout 1 | `4c64f2b5e81e`  |
| 3021   | Layout 1 | `4c64f2b5e81e`  |
| 3012   | Layout 1 | `4c64f2b5e81e`  |
| 3002   | Layout 1 | `4c64f2b5e81e`  |
| 2995   | Layout 1 | `4c64f2b5e81e`  |
| 2987   | Layout 1 | `4c64f2b5e81e`  |
| 2978   | Layout 1 | `4c64f2b5e81e`  |
| 2970   | Layout 1 | `4c64f2b5e81e`  |
| 2959   | Layout 1 | `4c64f2b5e81e`  |
| 2951   | Layout 1 | `4c64f2b5e81e`  |
| 2942   | Layout 1 | `4c64f2b5e81e`  |
| 2935   | Layout 1 | `4c64f2b5e81e`  |
| 2932   | Layout 1 | `4c64f2b5e81e`  |
| 2923   | Layout 1 | `4c64f2b5e81e`  |
| 2919   | Layout 1 | `4c64f2b5e81e`  |
| 2907   | Layout 1 | `4c64f2b5e81e`  |
| 2900   | Layout 1 | `4c64f2b5e81e`  |
| 2891   | Layout 1 | `4c64f2b5e81e`  |
| 2882   | Layout 1 | `4c64f2b5e81e`  |
| 2872   | Layout 1 | `4c64f2b5e81e`  |
| 2863   | Layout 1 | `4c64f2b5e81e`  |
| 2855   | Layout 1 | `4c64f2b5e81e`  |
| 2849   | Layout 1 | `4c64f2b5e81e`  |
| 2844   | Layout 1 | `4c64f2b5e81e`  |
| 2834   | Layout 1 | `4c64f2b5e81e`  |
| 2825   | Layout 1 | `4c64f2b5e81e`  |
| 2819   | Layout 1 | `4c64f2b5e81e`  |
| 2811   | Layout 1 | `4c64f2b5e81e`  |
| 2803   | Layout 1 | `4c64f2b5e81e`  |
| 2794   | Layout 1 | `4c64f2b5e81e`  |
| 2783   | Layout 1 | `4c64f2b5e81e`  |
| 2774   | Layout 1 | `4c64f2b5e81e`  |
| 2765   | Layout 1 | `4c64f2b5e81e`  |
| 2756   | Layout 1 | `4c64f2b5e81e`  |
| 2750   | Layout 1 | `4c64f2b5e81e`  |
| 2743   | Layout 1 | `4c64f2b5e81e`  |
| 2736   | Layout 1 | `4c64f2b5e81e`  |
| 2726   | Layout 1 | `4c64f2b5e81e`  |
| 2717   | Layout 1 | `4c64f2b5e81e`  |
| 2709   | Layout 1 | `4c64f2b5e81e`  |
| 2703   | Layout 1 | `4c64f2b5e81e`  |
| 2695   | Layout 1 | `4c64f2b5e81e`  |
| 2684   | Layout 1 | `4c64f2b5e81e`  |
| 2672   | Layout 1 | `4c64f2b5e81e`  |
| 2665   | Layout 1 | `4c64f2b5e81e`  |
| 2657   | Layout 1 | `4c64f2b5e81e`  |
| 2649   | Layout 1 | `4c64f2b5e81e`  |
| 2644   | Layout 1 | `4c64f2b5e81e`  |
| 2637   | Layout 1 | `4c64f2b5e81e`  |
| 2629   | Layout 1 | `4c64f2b5e81e`  |
| 2619   | Layout 1 | `4c64f2b5e81e`  |
| 2612   | Layout 1 | `4c64f2b5e81e`  |
| 2606   | Layout 1 | `4c64f2b5e81e`  |
| 2602   | Layout 1 | `4c64f2b5e81e`  |
| 2601   | Layout 1 | `4c64f2b5e81e`  |
| 2592   | Layout 1 | `4c64f2b5e81e`  |
| 2583   | Layout 1 | `4c64f2b5e81e`  |
| 2575   | Layout 1 | `4c64f2b5e81e`  |
| 2567   | Layout 1 | `4c64f2b5e81e`  |
| 2560   | Layout 1 | `4c64f2b5e81e`  |
| 2553   | Layout 1 | `4c64f2b5e81e`  |
| 2545   | Layout 1 | `4c64f2b5e81e`  |
| 2538   | Layout 1 | `4c64f2b5e81e`  |
| 2529   | Layout 1 | `4c64f2b5e81e`  |
| 2519   | Layout 1 | `4c64f2b5e81e`  |
| 2513   | Layout 1 | `4c64f2b5e81e`  |
| 2510   | Layout 1 | `4c64f2b5e81e`  |
| 2507   | Layout 1 | `4c64f2b5e81e`  |
| 2503   | Layout 1 | `4c64f2b5e81e`  |
| 2498   | Layout 1 | `4c64f2b5e81e`  |
| 2492   | Layout 1 | `4c64f2b5e81e`  |
| 2487   | Layout 1 | `4c64f2b5e81e`  |
| 2480   | Layout 1 | `4c64f2b5e81e`  |
| 2474   | Layout 1 | `4c64f2b5e81e`  |
| 2468   | Layout 1 | `4c64f2b5e81e`  |
| 2460   | Layout 1 | `4c64f2b5e81e`  |
| 2453   | Layout 1 | `4c64f2b5e81e`  |
| 2444   | Layout 1 | `4c64f2b5e81e`  |
| 2438   | Layout 1 | `4c64f2b5e81e`  |
| 2434   | Layout 1 | `4c64f2b5e81e`  |
| 2429   | Layout 1 | `4c64f2b5e81e`  |
| 2421   | Layout 1 | `4c64f2b5e81e`  |
| 2414   | Layout 1 | `4c64f2b5e81e`  |
| 2407   | Layout 1 | `4c64f2b5e81e`  |
| 2401   | Layout 1 | `4c64f2b5e81e`  |
| 2397   | Layout 1 | `4c64f2b5e81e`  |
| 2393   | Layout 1 | `4c64f2b5e81e`  |
| 2384   | Layout 1 | `4c64f2b5e81e`  |
| 2378   | Layout 1 | `4c64f2b5e81e`  |
| 2372   | Layout 1 | `4c64f2b5e81e`  |
| 2358   | Layout 1 | `4c64f2b5e81e`  |
| 2352   | Layout 1 | `4c64f2b5e81e`  |
| 2347   | Layout 1 | `4c64f2b5e81e`  |
| 2343   | Layout 1 | `4c64f2b5e81e`  |
| 2335   | Layout 1 | `4c64f2b5e81e`  |
| 2327   | Layout 1 | `4c64f2b5e81e`  |
| 2324   | Layout 1 | `4c64f2b5e81e`  |
| 2319   | Layout 1 | `4c64f2b5e81e`  |
| 2313   | Layout 1 | `4c64f2b5e81e`  |
| 2308   | Layout 1 | `4c64f2b5e81e`  |
| 2302   | Layout 1 | `4c64f2b5e81e`  |
| 2295   | Layout 1 | `4c64f2b5e81e`  |
| 2290   | Layout 1 | `4c64f2b5e81e`  |
| 2284   | Layout 1 | `4c64f2b5e81e`  |
| 2276   | Layout 1 | `4c64f2b5e81e`  |
| 2269   | Layout 1 | `4c64f2b5e81e`  |
| 2259   | Layout 1 | `4c64f2b5e81e`  |
| 2250   | Layout 1 | `4c64f2b5e81e`  |
| 2243   | Layout 1 | `4c64f2b5e81e`  |
| 2235   | Layout 1 | `4c64f2b5e81e`  |
| 2229   | Layout 1 | `4c64f2b5e81e`  |
| 2224   | Layout 1 | `4c64f2b5e81e`  |
| 2218   | Layout 1 | `4c64f2b5e81e`  |
| 2215   | Layout 1 | `4c64f2b5e81e`  |
| 2207   | Layout 1 | `4c64f2b5e81e`  |
| 2203   | Layout 1 | `4c64f2b5e81e`  |
| 2196   | Layout 1 | `4c64f2b5e81e`  |
| 2192   | Layout 1 | `4c64f2b5e81e`  |
| 2189   | Layout 1 | `4c64f2b5e81e`  |
| 2183   | Layout 1 | `4c64f2b5e81e`  |
| 2179   | Layout 1 | `4c64f2b5e81e`  |
| 2171   | Layout 1 | `4c64f2b5e81e`  |
| 2163   | Layout 1 | `4c64f2b5e81e`  |
| 2156   | Layout 1 | `4c64f2b5e81e`  |
| 2151   | Layout 1 | `4c64f2b5e81e`  |
| 2147   | Layout 1 | `4c64f2b5e81e`  |
| 2142   | Layout 1 | `4c64f2b5e81e`  |
| 2138   | Layout 1 | `4c64f2b5e81e`  |
| 2134   | Layout 1 | `4c64f2b5e81e`  |
| 2130   | Layout 1 | `4c64f2b5e81e`  |
| 2122   | Layout 1 | `4c64f2b5e81e`  |
| 2107   | Layout 1 | `4c64f2b5e81e`  |
| 2098   | Layout 1 | `4c64f2b5e81e`  |
| 2089   | Layout 1 | `4c64f2b5e81e`  |
| 2081   | Layout 1 | `4c64f2b5e81e`  |
| 2073   | Layout 1 | `4c64f2b5e81e`  |
| 2067   | Layout 1 | `4c64f2b5e81e`  |
| 2063   | Layout 1 | `4c64f2b5e81e`  |
| 2059   | Layout 1 | `4c64f2b5e81e`  |
| 2052   | Layout 1 | `4c64f2b5e81e`  |
| 2044   | Layout 1 | `4c64f2b5e81e`  |
| 2039   | Layout 1 | `4c64f2b5e81e`  |
| 2032   | Layout 1 | `4c64f2b5e81e`  |
| 2025   | Layout 1 | `4c64f2b5e81e`  |
| 2011   | Layout 1 | `4c64f2b5e81e`  |
| 2005   | Layout 1 | `4c64f2b5e81e`  |
| 2000   | Layout 1 | `4c64f2b5e81e`  |
| 1996   | Layout 1 | `4c64f2b5e81e`  |
| 1991   | Layout 1 | `4c64f2b5e81e`  |
| 1985   | Layout 1 | `4c64f2b5e81e`  |
| 1980   | Layout 1 | `4c64f2b5e81e`  |
| 1969   | Layout 1 | `4c64f2b5e81e`  |
| 1964   | Layout 1 | `4c64f2b5e81e`  |
| 1958   | Layout 1 | `4c64f2b5e81e`  |
| 1950   | Layout 1 | `4c64f2b5e81e`  |
| 1945   | Layout 1 | `4c64f2b5e81e`  |
| 1937   | Layout 1 | `4c64f2b5e81e`  |
| 1933   | Layout 1 | `4c64f2b5e81e`  |
| 1927   | Layout 1 | `4c64f2b5e81e`  |
| 1921   | Layout 1 | `4c64f2b5e81e`  |
| 1914   | Layout 1 | `4c64f2b5e81e`  |
| 1908   | Layout 1 | `4c64f2b5e81e`  |
| 1897   | Layout 1 | `4c64f2b5e81e`  |
| 1892   | Layout 1 | `4c64f2b5e81e`  |
| 1886   | Layout 1 | `4c64f2b5e81e`  |
| 1881   | Layout 1 | `4c64f2b5e81e`  |
| 1871   | Layout 1 | `4c64f2b5e81e`  |
| 1866   | Layout 1 | `4c64f2b5e81e`  |
| 1862   | Layout 1 | `4c64f2b5e81e`  |
| 1854   | Layout 1 | `4c64f2b5e81e`  |
| 1846   | Layout 1 | `4c64f2b5e81e`  |
| 1838   | Layout 1 | `4c64f2b5e81e`  |
| 1832   | Layout 1 | `4c64f2b5e81e`  |
| 1826   | Layout 1 | `4c64f2b5e81e`  |
| 1822   | Layout 1 | `4c64f2b5e81e`  |
| 1818   | Layout 1 | `4c64f2b5e81e`  |
| 1804   | Layout 1 | `4c64f2b5e81e`  |
| 1794   | Layout 1 | `4c64f2b5e81e`  |
| 1790   | Layout 1 | `4c64f2b5e81e`  |
| 1784   | Layout 1 | `4c64f2b5e81e`  |
| 1774   | Layout 1 | `4c64f2b5e81e`  |
| 1771   | Layout 1 | `4c64f2b5e81e`  |
| 1762   | Layout 1 | `4c64f2b5e81e`  |
| 1759   | Layout 1 | `4c64f2b5e81e`  |
| 1754   | Layout 1 | `4c64f2b5e81e`  |
| 1749   | Layout 1 | `4c64f2b5e81e`  |
| 1743   | Layout 1 | `4c64f2b5e81e`  |
| 1737   | Layout 1 | `4c64f2b5e81e`  |
| 1731   | Layout 1 | `4c64f2b5e81e`  |
| 1725   | Layout 1 | `4c64f2b5e81e`  |
| 1717   | Layout 1 | `4c64f2b5e81e`  |
| 1710   | Layout 1 | `4c64f2b5e81e`  |
| 1704   | Layout 1 | `4c64f2b5e81e`  |
| 1698   | Layout 1 | `4c64f2b5e81e`  |
| 1690   | Layout 1 | `4c64f2b5e81e`  |
| 1685   | Layout 1 | `4c64f2b5e81e`  |
| 1680   | Layout 1 | `4c64f2b5e81e`  |
| 1674   | Layout 1 | `4c64f2b5e81e`  |
| 1668   | Layout 1 | `4c64f2b5e81e`  |
| 1659   | Layout 1 | `4c64f2b5e81e`  |
| 1649   | No file  | `4c64f2b5e81e`  |
| 1642   | No file  | `4c64f2b5e81e`  |
| 1636   | No file  | `4c64f2b5e81e`  |
| 1628   | No file  | `4c64f2b5e81e`  |
| 1622   | No file  | `4c64f2b5e81e`  |
| 1614   | No file  | `4c64f2b5e81e`  |
| 1608   | No file  | `4c64f2b5e81e`  |
| 1602   | No file  | `4c64f2b5e81e`  |
| 1598   | No file  | `4c64f2b5e81e`  |
| 1594   | No file  | `4c64f2b5e81e`  |
| 1590   | No file  | `4c64f2b5e81e`  |
| 1587   | No file  | `4c64f2b5e81e`  |
| 1584   | No file  | `4c64f2b5e81e`  |
| 1579   | No file  | `4c64f2b5e81e`  |
| 1572   | No file  | `4c64f2b5e81e`  |
| 1565   | No file  | `4c64f2b5e81e`  |
| 1559   | No file  | `4c64f2b5e81e`  |
| 1554   | No file  | `4c64f2b5e81e`  |
| 1547   | No file  | `4c64f2b5e81e`  |
| 1537   | No file  | `4c64f2b5e81e`  |
| 1529   | No file  | `4c64f2b5e81e`  |
| 1524   | No file  | `4c64f2b5e81e`  |
| 1519   | No file  | `4c64f2b5e81e`  |
| 1509   | No file  | `4c64f2b5e81e`  |
| 1506   | No file  | `4c64f2b5e81e`  |
| 1504   | No file  | `4c64f2b5e81e`  |
| 1500   | No file  | `4c64f2b5e81e`  |
| 1493   | No file  | `4c64f2b5e81e`  |
| 1489   | No file  | `4c64f2b5e81e`  |
| 1485   | No file  | `4c64f2b5e81e`  |
| 1481   | No file  | `4c64f2b5e81e`  |
| 1474   | No file  | `4c64f2b5e81e`  |
| 1466   | No file  | `4c64f2b5e81e`  |
| 1462   | No file  | `4c64f2b5e81e`  |
| 1459   | No file  | `4c64f2b5e81e`  |
| 1453   | No file  | `4c64f2b5e81e`  |
| 1450   | No file  | `4c64f2b5e81e`  |
| 1445   | No file  | `4c64f2b5e81e`  |
| 1439   | No file  | `4c64f2b5e81e`  |
| 1433   | No file  | `4c64f2b5e81e`  |
| 1430   | No file  | `4c64f2b5e81e`  |
| 1426   | No file  | `4c64f2b5e81e`  |
| 1421   | No file  | `4c64f2b5e81e`  |
| 1417   | No file  | `4c64f2b5e81e`  |
| 1416   | No file  | `4c64f2b5e81e`  |
| 1409   | No file  | `4c64f2b5e81e`  |
| 1405   | No file  | `4c64f2b5e81e`  |
| 1401   | No file  | `4c64f2b5e81e`  |
| 1396   | No file  | `4c64f2b5e81e`  |
| 1391   | No file  | `4c64f2b5e81e`  |
| 1390   | No file  | `4c64f2b5e81e`  |
| 1386   | No file  | `4c64f2b5e81e`  |
| 1381   | No file  | `4c64f2b5e81e`  |
| 1379   | No file  | `4c64f2b5e81e`  |
| 1372   | No file  | `4c64f2b5e81e`  |
| 1366   | No file  | `4c64f2b5e81e`  |
| 1364   | No file  | `4c64f2b5e81e`  |
| 1363   | No file  | `4c64f2b5e81e`  |
| 1360   | No file  | `4c64f2b5e81e`  |
| 1358   | No file  | `4c64f2b5e81e`  |
| 1355   | No file  | `4c64f2b5e81e`  |
| 1351   | No file  | `4c64f2b5e81e`  |
| 1348   | No file  | `4c64f2b5e81e`  |
| 1346   | No file  | `4c64f2b5e81e`  |
| 1341   | No file  | `4c64f2b5e81e`  |
| 1340   | No file  | `4c64f2b5e81e`  |
| 1338   | No file  | `4c64f2b5e81e`  |
| 1335   | No file  | `4c64f2b5e81e`  |
| 1333   | No file  | `4c64f2b5e81e`  |
| 1329   | No file  | `4c64f2b5e81e`  |
| 1327   | No file  | `4c64f2b5e81e`  |
| 1324   | No file  | `4c64f2b5e81e`  |
| 1321   | No file  | `4c64f2b5e81e`  |
| 1319   | No file  | `4c64f2b5e81e`  |
| 1318   | No file  | `4c64f2b5e81e`  |
| 1316   | No file  | `4c64f2b5e81e`  |
| 1313   | No file  | `4c64f2b5e81e`  |
| 1311   | No file  | `4c64f2b5e81e`  |
| 1309   | No file  | `4c64f2b5e81e`  |
| 1304   | No file  | `4c64f2b5e81e`  |
| 1292   | No file  | `4c64f2b5e81e`  |
| 1286   | No file  | `4c64f2b5e81e`  |
| 1280   | No file  | `4c64f2b5e81e`  |
| 1276   | No file  | `4c64f2b5e81e`  |
| 1267   | No file  | `4c64f2b5e81e`  |
| 1261   | No file  | `4c64f2b5e81e`  |
| 1256   | No file  | `4c64f2b5e81e`  |
| 1250   | No file  | `4c64f2b5e81e`  |
| 1246   | No file  | `4c64f2b5e81e`  |
| 1239   | No file  | `4c64f2b5e81e`  |
| 1230   | No file  | `4c64f2b5e81e`  |
| 1226   | No file  | `4c64f2b5e81e`  |
| 1220   | No file  | `4c64f2b5e81e`  |
| 1217   | No file  | `4c64f2b5e81e`  |
| 1211   | No file  | `4c64f2b5e81e`  |
| 1210   | No file  | `4c64f2b5e81e`  |
| 1208   | No file  | `4c64f2b5e81e`  |
| 1203   | No file  | `4c64f2b5e81e`  |
| 1197   | No file  | `4c64f2b5e81e`  |
| 1194   | No file  | `4c64f2b5e81e`  |
| 1192   | No file  | `4c64f2b5e81e`  |
| 1187   | No file  | `4c64f2b5e81e`  |
| 1183   | No file  | `4c64f2b5e81e`  |
| 1177   | No file  | `4c64f2b5e81e`  |
| 1173   | No file  | `4c64f2b5e81e`  |
| 1167   | No file  | `4c64f2b5e81e`  |
| 1164   | No file  | `4c64f2b5e81e`  |
| 1156   | No file  | `4c64f2b5e81e`  |
| 1149   | No file  | `4c64f2b5e81e`  |
| 1144   | No file  | `4c64f2b5e81e`  |
| 1137   | No file  | `4c64f2b5e81e`  |
| 1132   | No file  | `4c64f2b5e81e`  |
| 1127   | No file  | `4c64f2b5e81e`  |
| 1122   | No file  | `4c64f2b5e81e`  |
| 1118   | No file  | `4c64f2b5e81e`  |
| 1114   | No file  | `4c64f2b5e81e`  |
| 1109   | No file  | `4c64f2b5e81e`  |
| 1102   | No file  | `4c64f2b5e81e`  |
| 1096   | No file  | `4c64f2b5e81e`  |
| 1088   | No file  | `4c64f2b5e81e`  |
| 1081   | No file  | `4c64f2b5e81e`  |
| 1076   | No file  | `4c64f2b5e81e`  |
| 1069   | No file  | `4c64f2b5e81e`  |
| 1064   | No file  | `4c64f2b5e81e`  |
| 1058   | No file  | `4c64f2b5e81e`  |
| 1051   | No file  | `4c64f2b5e81e`  |
| 1044   | No file  | `4c64f2b5e81e`  |
| 1036   | No file  | `4c64f2b5e81e`  |
| 1026   | No file  | `4c64f2b5e81e`  |
| 1016   | No file  | `4c64f2b5e81e`  |
| 1009   | No file  | `4c64f2b5e81e`  |
| 1005   | No file  | `4c64f2b5e81e`  |
| 1000   | No file  | `4c64f2b5e81e`  |
| 998    | No file  | `4c64f2b5e81e`  |
| 990    | No file  | `4c64f2b5e81e`  |
| 979    | No file  | `4c64f2b5e81e`  |
| 972    | No file  | `4c64f2b5e81e`  |
| 963    | No file  | `4c64f2b5e81e`  |
| 955    | No file  | `4c64f2b5e81e`  |
| 946    | No file  | `4c64f2b5e81e`  |
| 938    | No file  | `4c64f2b5e81e`  |
| 927    | No file  | `4c64f2b5e81e`  |
| 911    | No file  | `4c64f2b5e81e`  |
| 904    | No file  | `4c64f2b5e81e`  |
| 899    | No file  | `4c64f2b5e81e`  |
| 894    | No file  | `4c64f2b5e81e`  |
| 885    | No file  | `4c64f2b5e81e`  |
| 879    | No file  | `4c64f2b5e81e`  |
| 872    | No file  | `4c64f2b5e81e`  |
| 864    | No file  | `4c64f2b5e81e`  |
| 855    | No file  | `4c64f2b5e81e`  |
| 853    | No file  | `4c64f2b5e81e`  |
| 845    | No file  | `4c64f2b5e81e`  |
| 837    | No file  | `4c64f2b5e81e`  |
| 829    | No file  | `4c64f2b5e81e`  |
| 822    | No file  | `4c64f2b5e81e`  |
| 814    | No file  | `4c64f2b5e81e`  |
| 805    | No file  | `4c64f2b5e81e`  |
| 794    | No file  | `4c64f2b5e81e`  |
| 787    | No file  | `4c64f2b5e81e`  |
| 780    | No file  | `4c64f2b5e81e`  |
| 771    | No file  | `4c64f2b5e81e`  |
| 760    | No file  | `4c64f2b5e81e`  |
| 748    | No file  | `4c64f2b5e81e`  |
| 741    | No file  | `4c64f2b5e81e`  |
| 736    | No file  | `4c64f2b5e81e`  |
| 731    | No file  | `4c64f2b5e81e`  |
| 723    | No file  | `4c64f2b5e81e`  |
| 711    | No file  | `4c64f2b5e81e`  |
| 707    | No file  | `4c64f2b5e81e`  |
| 697    | No file  | `4c64f2b5e81e`  |
| 689    | No file  | `4c64f2b5e81e`  |
| 683    | No file  | `4c64f2b5e81e`  |
| 678    | No file  | `4c64f2b5e81e`  |
| 670    | No file  | `4c64f2b5e81e`  |
| 661    | No file  | `4c64f2b5e81e`  |
| 656    | No file  | `4c64f2b5e81e`  |
| 652    | No file  | `4c64f2b5e81e`  |
| 643    | No file  | `4c64f2b5e81e`  |
| 637    | No file  | `4c64f2b5e81e`  |
| 630    | No file  | `4c64f2b5e81e`  |
| 627    | No file  | `4c64f2b5e81e`  |
| 621    | No file  | `4c64f2b5e81e`  |
| 617    | No file  | `4c64f2b5e81e`  |
| 615    | No file  | `4c64f2b5e81e`  |
| 606    | No file  | `4c64f2b5e81e`  |
| 599    | No file  | `4c64f2b5e81e`  |
| 592    | No file  | `4c64f2b5e81e`  |
| 586    | No file  | `4c64f2b5e81e`  |
| 577    | No file  | `4c64f2b5e81e`  |
| 569    | No file  | `4c64f2b5e81e`  |
| 561    | No file  | `4c64f2b5e81e`  |
| 554    | No file  | `4c64f2b5e81e`  |
| 542    | No file  | `4c64f2b5e81e`  |
| 532    | No file  | `4c64f2b5e81e`  |
| 531    | No file  | `4c64f2b5e81e`  |
| 526    | No file  | `4c64f2b5e81e`  |
| 521    | No file  | `4c64f2b5e81e`  |
| 517    | No file  | `4c64f2b5e81e`  |
| 510    | No file  | `4c64f2b5e81e`  |
| 508    | No file  | `4c64f2b5e81e`  |
| 504    | No file  | `4c64f2b5e81e`  |
| 497    | No file  | `4c64f2b5e81e`  |
| 491    | No file  | `4c64f2b5e81e`  |
| 485    | No file  | `4c64f2b5e81e`  |
| 478    | No file  | `4c64f2b5e81e`  |
| 472    | No file  | `4c64f2b5e81e`  |
| 466    | No file  | `4c64f2b5e81e`  |
| 457    | No file  | `4c64f2b5e81e`  |
| 452    | No file  | `4c64f2b5e81e`  |
| 449    | No file  | `4c64f2b5e81e`  |
| 435    | No file  | `4c64f2b5e81e`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                     | Type                                 | Field                | Notes                                         |
| -------------------------- | ------------------------------------ | -------------------- | --------------------------------------------- |
| `+0x00`                    | char[4]                              | magic                | ASCII `PABR`                                  |
| `+0x04`                    | u32                                  | rental_percent_count | Number of `rental_percents`                   |
| `+0x08`                    | Rental Percent[rental_percent_count] | rental_percents      | See Rental Percent; rising `day` order        |
| `rental_percents+0x00`     | u32                                  | return_percent_count | Number of `return_percents`                   |
| `rental_percents+0x04`     | Return Percent[return_percent_count] | return_percents      | See Return Percent; rising `day` order        |
| `return_percents+0x00`     | String Table                         | string_table         | See String Table                              |
| `string_table+0x00`        | u32                                  | table_start          | Offset of the string table, where the lists end |
| `string_table+0x04`        | u32                                  | zero                 | Always `0`                                    |

### Rental Percent (6 bytes)

| Offset  | Type | Field            | Notes                                              |
| ------- | ---- | ---------------- | -------------------------------------------------- |
| `+0x00` | u16  | day              | Rental length in days the step starts at           |
| `+0x02` | u32  | discount_percent | Discount, 1,000,000 = 100%                         |

### Return Percent (6 bytes)

| Offset  | Type | Field          | Notes                                    |
| ------- | ---- | -------------- | ---------------------------------------- |
| `+0x00` | u16  | day            | Rental length in days the step starts at |
| `+0x02` | u32  | return_percent | Return rate, 1,000,000 = 100%            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Steps

The steps of clients 1784 and 3483, the same on both.

| `day` | `discount_percent` | `return_percent` |
| ----- | ------------------ | ---------------- |
| 1     | 0 (0%)             | 150000 (15%)     |
| 30    | 50000 (5%)         | 200000 (20%)     |
| 90    | 80000 (8%)         | 230000 (23%)     |
| 180   | 120000 (12%)       | 270000 (27%)     |
| 365   | 200000 (20%)       | 350000 (35%)     |

## Field Names

The names follow two sheets of a private server's `DataSheets.bexcel` on
client 1784: `MantionRental_Percent` (columns `Day` and
`Discount_Percent`) and `MantionReturn_Percent` (columns `Day` and
`Return_Percent`), 5 rows each. All 5 steps of each list in the client
1784 file match their sheet row on both columns (5 of 5 and 5 of 5), in
sheet order. The list names follow the sheet names.

## Notes

- The percents read on the client's 1,000,000 = 100% scale as 5% to 20%
  off for 30 to 365 days. The scale is the one the rate fields of other
  tables use; no Lua of client 3482 shows the percent itself.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/enchantshop_tables.py`:
  one row with both lists, each step as days and percent.

## Open Questions

### What the Return Percent Returns

`return_percent` rises from 15% at 1 day to 35% at 365 days. The Lua of
client 3482 has an `InteractionType_ReturnRentedMansion` interaction but
no getter for a return amount, so whether the percent is the share of the
rent paid back on an early return, or something else, is not known.
