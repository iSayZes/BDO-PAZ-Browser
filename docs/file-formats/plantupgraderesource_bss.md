# `plantupgraderesource.bss` Format

## Purpose

Upgrade costs of the worker system: one entry per level group and level with the time, contribution points, silver and up to three items the upgrade to that level takes. Towns in [planttown.bss](planttown_bss.md) use level group 1.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                       | Bytes | Records                 | Row bytes |
| ------ | ------------- | ------- | -------------------------- | ----- | ----------------------- | --------- |
| 1      | 805 and later | 3483    | `plantupgraderesource.bss` | 4,428 | 228 Need Item, 76 Entry | 12        |

| Layout | File                       | Known            | Unknown    |
| ------ | -------------------------- | ---------------- | ---------- |
| 1      | `plantupgraderesource.bss` | 4,428 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `6eb6a9b27cdf`  |
| 3482   | Layout 1             | `6eb6a9b27cdf`  |
| 3474   | Layout 1             | `6eb6a9b27cdf`  |
| 3473   | Layout 1             | `6eb6a9b27cdf`  |
| 3464   | Layout 1             | `6eb6a9b27cdf`  |
| 3458   | Layout 1             | `6eb6a9b27cdf`  |
| 3454   | Layout 1             | `6eb6a9b27cdf`  |
| 3444   | Layout 1             | `6eb6a9b27cdf`  |
| 3435   | Layout 1             | `6eb6a9b27cdf`  |
| 3426   | Layout 1             | `6eb6a9b27cdf`  |
| 3418   | Layout 1             | `6eb6a9b27cdf`  |
| 3412   | Layout 1             | `6eb6a9b27cdf`  |
| 3402   | Layout 1             | `6eb6a9b27cdf`  |
| 3396   | Layout 1             | `6eb6a9b27cdf`  |
| 3387   | Layout 1             | `6eb6a9b27cdf`  |
| 3381   | Layout 1             | `6eb6a9b27cdf`  |
| 3373   | Layout 1             | `6eb6a9b27cdf`  |
| 3364   | Layout 1             | `6eb6a9b27cdf`  |
| 3356   | Layout 1             | `6eb6a9b27cdf`  |
| 3349   | Layout 1             | `6eb6a9b27cdf`  |
| 3342   | Layout 1             | `6eb6a9b27cdf`  |
| 3335   | Layout 1             | `6eb6a9b27cdf`  |
| 3326   | Layout 1             | `6eb6a9b27cdf`  |
| 3321   | Layout 1             | `6eb6a9b27cdf`  |
| 3314   | Layout 1             | `6eb6a9b27cdf`  |
| 3303   | Layout 1             | `6eb6a9b27cdf`  |
| 3302   | Layout 1             | `6eb6a9b27cdf`  |
| 3293   | Layout 1             | `6eb6a9b27cdf`  |
| 3283   | Layout 1             | `6eb6a9b27cdf`  |
| 3275   | Layout 1             | `6eb6a9b27cdf`  |
| 3267   | Layout 1             | `6eb6a9b27cdf`  |
| 3258   | Layout 1             | `6eb6a9b27cdf`  |
| 3251   | Layout 1             | `6eb6a9b27cdf`  |
| 3242   | Layout 1             | `6eb6a9b27cdf`  |
| 3235   | Layout 1             | `6eb6a9b27cdf`  |
| 3229   | Layout 1             | `6eb6a9b27cdf`  |
| 3212   | Layout 1             | `6eb6a9b27cdf`  |
| 3203   | Layout 1             | `6eb6a9b27cdf`  |
| 3193   | Layout 1             | `6eb6a9b27cdf`  |
| 3186   | Layout 1             | `6eb6a9b27cdf`  |
| 3177   | Layout 1             | `6eb6a9b27cdf`  |
| 3169   | Layout 1             | `6eb6a9b27cdf`  |
| 3158   | Layout 1             | `6eb6a9b27cdf`  |
| 3151   | Layout 1             | `6eb6a9b27cdf`  |
| 3144   | Layout 1             | `6eb6a9b27cdf`  |
| 3133   | Layout 1             | `6eb6a9b27cdf`  |
| 3125   | Layout 1             | `6eb6a9b27cdf`  |
| 3118   | Layout 1             | `6eb6a9b27cdf`  |
| 3111   | Layout 1             | `6eb6a9b27cdf`  |
| 3103   | Layout 1             | `6eb6a9b27cdf`  |
| 3095   | Layout 1             | `6eb6a9b27cdf`  |
| 3086   | Layout 1             | `6eb6a9b27cdf`  |
| 3072   | Layout 1             | `6eb6a9b27cdf`  |
| 3062   | Layout 1             | `6eb6a9b27cdf`  |
| 3052   | Layout 1             | `6eb6a9b27cdf`  |
| 3045   | Layout 1             | `6eb6a9b27cdf`  |
| 3037   | Layout 1             | `6eb6a9b27cdf`  |
| 3030   | Layout 1             | `6eb6a9b27cdf`  |
| 3021   | Layout 1             | `6eb6a9b27cdf`  |
| 3012   | Layout 1             | `6eb6a9b27cdf`  |
| 3002   | Layout 1             | `6eb6a9b27cdf`  |
| 2995   | Layout 1             | `6eb6a9b27cdf`  |
| 2987   | Layout 1             | `6eb6a9b27cdf`  |
| 2978   | Layout 1             | `6eb6a9b27cdf`  |
| 2970   | Layout 1             | `6eb6a9b27cdf`  |
| 2959   | Layout 1             | `6eb6a9b27cdf`  |
| 2951   | Layout 1             | `6eb6a9b27cdf`  |
| 2942   | Layout 1             | `6eb6a9b27cdf`  |
| 2935   | Layout 1             | `6eb6a9b27cdf`  |
| 2932   | Layout 1             | `6eb6a9b27cdf`  |
| 2923   | Layout 1             | `6eb6a9b27cdf`  |
| 2919   | Layout 1             | `6eb6a9b27cdf`  |
| 2907   | Layout 1             | `6eb6a9b27cdf`  |
| 2900   | Layout 1             | `6eb6a9b27cdf`  |
| 2891   | Layout 1             | `6eb6a9b27cdf`  |
| 2882   | Layout 1             | `6eb6a9b27cdf`  |
| 2872   | Layout 1             | `6eb6a9b27cdf`  |
| 2863   | Layout 1             | `6eb6a9b27cdf`  |
| 2855   | Layout 1             | `6eb6a9b27cdf`  |
| 2849   | Layout 1             | `6eb6a9b27cdf`  |
| 2844   | Layout 1             | `6eb6a9b27cdf`  |
| 2834   | Layout 1             | `6eb6a9b27cdf`  |
| 2825   | Layout 1             | `6eb6a9b27cdf`  |
| 2819   | Layout 1             | `6eb6a9b27cdf`  |
| 2811   | Layout 1             | `6eb6a9b27cdf`  |
| 2803   | Layout 1             | `6eb6a9b27cdf`  |
| 2794   | Layout 1             | `6eb6a9b27cdf`  |
| 2783   | Layout 1             | `6eb6a9b27cdf`  |
| 2774   | Layout 1             | `6eb6a9b27cdf`  |
| 2765   | Layout 1             | `6eb6a9b27cdf`  |
| 2756   | Layout 1             | `6eb6a9b27cdf`  |
| 2750   | Layout 1             | `6eb6a9b27cdf`  |
| 2743   | Layout 1             | `6eb6a9b27cdf`  |
| 2736   | Layout 1             | `6eb6a9b27cdf`  |
| 2726   | Layout 1             | `6eb6a9b27cdf`  |
| 2717   | Layout 1             | `6eb6a9b27cdf`  |
| 2709   | Layout 1             | `6eb6a9b27cdf`  |
| 2703   | Layout 1             | `6eb6a9b27cdf`  |
| 2695   | Layout 1             | `6eb6a9b27cdf`  |
| 2684   | Layout 1             | `6eb6a9b27cdf`  |
| 2672   | Layout 1             | `6eb6a9b27cdf`  |
| 2665   | Layout 1             | `6eb6a9b27cdf`  |
| 2657   | Layout 1             | `6eb6a9b27cdf`  |
| 2649   | Layout 1             | `6eb6a9b27cdf`  |
| 2644   | Layout 1             | `6eb6a9b27cdf`  |
| 2637   | Layout 1             | `6eb6a9b27cdf`  |
| 2629   | Layout 1             | `6eb6a9b27cdf`  |
| 2619   | Layout 1             | `6eb6a9b27cdf`  |
| 2612   | Layout 1             | `6eb6a9b27cdf`  |
| 2606   | Layout 1             | `6eb6a9b27cdf`  |
| 2602   | Layout 1             | `6eb6a9b27cdf`  |
| 2601   | Layout 1             | `6eb6a9b27cdf`  |
| 2592   | Layout 1             | `6eb6a9b27cdf`  |
| 2583   | Layout 1             | `6eb6a9b27cdf`  |
| 2575   | Layout 1             | `6eb6a9b27cdf`  |
| 2567   | Layout 1             | `6eb6a9b27cdf`  |
| 2560   | Layout 1             | `6eb6a9b27cdf`  |
| 2553   | Layout 1             | `6eb6a9b27cdf`  |
| 2545   | Layout 1             | `6eb6a9b27cdf`  |
| 2538   | Layout 1             | `6eb6a9b27cdf`  |
| 2529   | Layout 1             | `6eb6a9b27cdf`  |
| 2519   | Layout 1             | `6eb6a9b27cdf`  |
| 2513   | Layout 1             | `6eb6a9b27cdf`  |
| 2510   | Layout 1             | `6eb6a9b27cdf`  |
| 2507   | Layout 1             | `6eb6a9b27cdf`  |
| 2503   | Layout 1             | `6eb6a9b27cdf`  |
| 2498   | Layout 1             | `6eb6a9b27cdf`  |
| 2492   | Layout 1             | `6eb6a9b27cdf`  |
| 2487   | Layout 1             | `6eb6a9b27cdf`  |
| 2480   | Layout 1             | `6eb6a9b27cdf`  |
| 2474   | Layout 1             | `6eb6a9b27cdf`  |
| 2468   | Layout 1             | `6eb6a9b27cdf`  |
| 2460   | Layout 1             | `6eb6a9b27cdf`  |
| 2453   | Layout 1             | `6eb6a9b27cdf`  |
| 2444   | Layout 1             | `6eb6a9b27cdf`  |
| 2438   | Layout 1             | `6eb6a9b27cdf`  |
| 2434   | Layout 1             | `6eb6a9b27cdf`  |
| 2429   | Layout 1             | `6eb6a9b27cdf`  |
| 2421   | Layout 1             | `6eb6a9b27cdf`  |
| 2414   | Layout 1             | `6eb6a9b27cdf`  |
| 2407   | Layout 1             | `6eb6a9b27cdf`  |
| 2401   | Layout 1             | `6eb6a9b27cdf`  |
| 2397   | Layout 1             | `6eb6a9b27cdf`  |
| 2393   | Layout 1             | `6eb6a9b27cdf`  |
| 2384   | Layout 1             | `6eb6a9b27cdf`  |
| 2378   | Layout 1             | `6eb6a9b27cdf`  |
| 2372   | Layout 1             | `6eb6a9b27cdf`  |
| 2358   | Layout 1             | `6eb6a9b27cdf`  |
| 2352   | Layout 1             | `6eb6a9b27cdf`  |
| 2347   | Layout 1             | `6eb6a9b27cdf`  |
| 2343   | Layout 1             | `6eb6a9b27cdf`  |
| 2335   | Layout 1             | `6eb6a9b27cdf`  |
| 2327   | Layout 1             | `6eb6a9b27cdf`  |
| 2324   | Layout 1             | `6eb6a9b27cdf`  |
| 2319   | Layout 1             | `6eb6a9b27cdf`  |
| 2313   | Layout 1             | `6eb6a9b27cdf`  |
| 2308   | Layout 1             | `6eb6a9b27cdf`  |
| 2302   | Layout 1             | `6eb6a9b27cdf`  |
| 2295   | Layout 1             | `6eb6a9b27cdf`  |
| 2290   | Layout 1             | `6eb6a9b27cdf`  |
| 2284   | Layout 1             | `6eb6a9b27cdf`  |
| 2276   | Layout 1             | `6eb6a9b27cdf`  |
| 2269   | Layout 1             | `6eb6a9b27cdf`  |
| 2259   | Layout 1             | `6eb6a9b27cdf`  |
| 2250   | Layout 1             | `6eb6a9b27cdf`  |
| 2243   | Layout 1             | `6eb6a9b27cdf`  |
| 2235   | Layout 1             | `6eb6a9b27cdf`  |
| 2229   | Layout 1             | `6eb6a9b27cdf`  |
| 2224   | Layout 1             | `6eb6a9b27cdf`  |
| 2218   | Layout 1             | `6eb6a9b27cdf`  |
| 2215   | Layout 1             | `6eb6a9b27cdf`  |
| 2207   | Layout 1             | `6eb6a9b27cdf`  |
| 2203   | Layout 1             | `6eb6a9b27cdf`  |
| 2196   | Layout 1             | `6eb6a9b27cdf`  |
| 2192   | Layout 1             | `6eb6a9b27cdf`  |
| 2189   | Layout 1             | `6eb6a9b27cdf`  |
| 2183   | Layout 1             | `6eb6a9b27cdf`  |
| 2179   | Layout 1             | `6eb6a9b27cdf`  |
| 2171   | Layout 1             | `6eb6a9b27cdf`  |
| 2163   | Layout 1             | `6eb6a9b27cdf`  |
| 2156   | Layout 1             | `6eb6a9b27cdf`  |
| 2151   | Layout 1             | `6eb6a9b27cdf`  |
| 2147   | Layout 1             | `6eb6a9b27cdf`  |
| 2142   | Layout 1             | `6eb6a9b27cdf`  |
| 2138   | Layout 1             | `6eb6a9b27cdf`  |
| 2134   | Layout 1             | `6eb6a9b27cdf`  |
| 2130   | Layout 1             | `6eb6a9b27cdf`  |
| 2122   | Layout 1             | `6eb6a9b27cdf`  |
| 2107   | Layout 1             | `6eb6a9b27cdf`  |
| 2098   | Layout 1             | `6eb6a9b27cdf`  |
| 2089   | Layout 1             | `6eb6a9b27cdf`  |
| 2081   | Layout 1             | `6eb6a9b27cdf`  |
| 2073   | Layout 1             | `6eb6a9b27cdf`  |
| 2067   | Layout 1             | `6eb6a9b27cdf`  |
| 2063   | Layout 1             | `6eb6a9b27cdf`  |
| 2059   | Layout 1             | `6eb6a9b27cdf`  |
| 2052   | Layout 1             | `6eb6a9b27cdf`  |
| 2044   | Layout 1             | `6eb6a9b27cdf`  |
| 2039   | Layout 1             | `6eb6a9b27cdf`  |
| 2032   | Layout 1             | `6eb6a9b27cdf`  |
| 2025   | Layout 1             | `6eb6a9b27cdf`  |
| 2011   | Layout 1             | `6eb6a9b27cdf`  |
| 2005   | Layout 1             | `6eb6a9b27cdf`  |
| 2000   | Layout 1             | `6eb6a9b27cdf`  |
| 1996   | Layout 1             | `6eb6a9b27cdf`  |
| 1991   | Layout 1             | `6eb6a9b27cdf`  |
| 1985   | Layout 1             | `6eb6a9b27cdf`  |
| 1980   | Layout 1             | `6eb6a9b27cdf`  |
| 1969   | Layout 1             | `6eb6a9b27cdf`  |
| 1964   | Layout 1             | `6eb6a9b27cdf`  |
| 1958   | Layout 1             | `6eb6a9b27cdf`  |
| 1950   | Layout 1             | `6eb6a9b27cdf`  |
| 1945   | Layout 1             | `6eb6a9b27cdf`  |
| 1937   | Layout 1             | `6eb6a9b27cdf`  |
| 1933   | Layout 1             | `6eb6a9b27cdf`  |
| 1927   | Layout 1             | `6eb6a9b27cdf`  |
| 1921   | Layout 1             | `6eb6a9b27cdf`  |
| 1914   | Layout 1             | `6eb6a9b27cdf`  |
| 1908   | Layout 1             | `6eb6a9b27cdf`  |
| 1897   | Layout 1             | `6eb6a9b27cdf`  |
| 1892   | Layout 1             | `6eb6a9b27cdf`  |
| 1886   | Layout 1             | `6eb6a9b27cdf`  |
| 1881   | Layout 1             | `6eb6a9b27cdf`  |
| 1871   | Layout 1             | `6eb6a9b27cdf`  |
| 1866   | Layout 1             | `6eb6a9b27cdf`  |
| 1862   | Layout 1             | `6eb6a9b27cdf`  |
| 1854   | Layout 1             | `6eb6a9b27cdf`  |
| 1846   | Layout 1             | `6eb6a9b27cdf`  |
| 1838   | Layout 1             | `6eb6a9b27cdf`  |
| 1832   | Layout 1             | `6eb6a9b27cdf`  |
| 1826   | Layout 1             | `6eb6a9b27cdf`  |
| 1822   | Layout 1             | `6eb6a9b27cdf`  |
| 1818   | Layout 1             | `6eb6a9b27cdf`  |
| 1804   | Layout 1             | `6eb6a9b27cdf`  |
| 1794   | Layout 1             | `6eb6a9b27cdf`  |
| 1790   | Layout 1             | `6eb6a9b27cdf`  |
| 1784   | Layout 1             | `6eb6a9b27cdf`  |
| 1774   | Layout 1             | `6eb6a9b27cdf`  |
| 1771   | Layout 1             | `6eb6a9b27cdf`  |
| 1762   | Layout 1             | `6eb6a9b27cdf`  |
| 1759   | Layout 1             | `6eb6a9b27cdf`  |
| 1754   | Layout 1             | `6eb6a9b27cdf`  |
| 1749   | Layout 1             | `6eb6a9b27cdf`  |
| 1743   | Layout 1             | `6eb6a9b27cdf`  |
| 1737   | Layout 1             | `6eb6a9b27cdf`  |
| 1731   | Layout 1             | `6eb6a9b27cdf`  |
| 1725   | Layout 1             | `6eb6a9b27cdf`  |
| 1717   | Layout 1             | `6eb6a9b27cdf`  |
| 1710   | Layout 1             | `6eb6a9b27cdf`  |
| 1704   | Layout 1             | `6eb6a9b27cdf`  |
| 1698   | Layout 1             | `6eb6a9b27cdf`  |
| 1690   | Layout 1             | `6eb6a9b27cdf`  |
| 1685   | Layout 1             | `6eb6a9b27cdf`  |
| 1680   | Layout 1             | `6eb6a9b27cdf`  |
| 1674   | Layout 1             | `6eb6a9b27cdf`  |
| 1668   | Layout 1             | `6eb6a9b27cdf`  |
| 1659   | Layout 1             | `6eb6a9b27cdf`  |
| 1649   | Layout 1             | `6eb6a9b27cdf`  |
| 1642   | Layout 1             | `6eb6a9b27cdf`  |
| 1636   | Layout 1             | `6eb6a9b27cdf`  |
| 1628   | Layout 1             | `6eb6a9b27cdf`  |
| 1622   | Layout 1             | `6eb6a9b27cdf`  |
| 1614   | Layout 1             | `6eb6a9b27cdf`  |
| 1608   | Layout 1             | `6eb6a9b27cdf`  |
| 1602   | Layout 1             | `6eb6a9b27cdf`  |
| 1598   | Layout 1             | `6eb6a9b27cdf`  |
| 1594   | Layout 1             | `6eb6a9b27cdf`  |
| 1590   | Layout 1             | `6eb6a9b27cdf`  |
| 1587   | Layout 1             | `6eb6a9b27cdf`  |
| 1584   | Layout 1             | `6eb6a9b27cdf`  |
| 1579   | Layout 1             | `6eb6a9b27cdf`  |
| 1572   | Layout 1             | `6eb6a9b27cdf`  |
| 1565   | Layout 1             | `6eb6a9b27cdf`  |
| 1559   | Layout 1             | `6eb6a9b27cdf`  |
| 1554   | Layout 1             | `6eb6a9b27cdf`  |
| 1547   | Layout 1             | `6eb6a9b27cdf`  |
| 1537   | Layout 1             | `6eb6a9b27cdf`  |
| 1529   | Layout 1             | `6eb6a9b27cdf`  |
| 1524   | Layout 1             | `6eb6a9b27cdf`  |
| 1519   | Layout 1             | `6eb6a9b27cdf`  |
| 1509   | Layout 1             | `6eb6a9b27cdf`  |
| 1506   | Layout 1             | `6eb6a9b27cdf`  |
| 1504   | Layout 1             | `6eb6a9b27cdf`  |
| 1500   | Layout 1             | `6eb6a9b27cdf`  |
| 1493   | Layout 1             | `6eb6a9b27cdf`  |
| 1489   | Layout 1             | `6eb6a9b27cdf`  |
| 1485   | Layout 1             | `6eb6a9b27cdf`  |
| 1481   | Layout 1             | `6eb6a9b27cdf`  |
| 1474   | Layout 1             | `6eb6a9b27cdf`  |
| 1466   | Layout 1             | `6eb6a9b27cdf`  |
| 1462   | Layout 1             | `6eb6a9b27cdf`  |
| 1459   | Layout 1             | `6eb6a9b27cdf`  |
| 1453   | Layout 1             | `6eb6a9b27cdf`  |
| 1450   | Layout 1             | `6eb6a9b27cdf`  |
| 1445   | Layout 1             | `6eb6a9b27cdf`  |
| 1439   | Layout 1             | `6eb6a9b27cdf`  |
| 1433   | Layout 1             | `6eb6a9b27cdf`  |
| 1430   | Layout 1             | `6eb6a9b27cdf`  |
| 1426   | Layout 1             | `6eb6a9b27cdf`  |
| 1421   | Layout 1             | `6eb6a9b27cdf`  |
| 1417   | Layout 1             | `6eb6a9b27cdf`  |
| 1416   | Layout 1             | `6eb6a9b27cdf`  |
| 1409   | Layout 1             | `6eb6a9b27cdf`  |
| 1405   | Layout 1             | `6eb6a9b27cdf`  |
| 1401   | Layout 1             | `6eb6a9b27cdf`  |
| 1396   | Layout 1             | `6eb6a9b27cdf`  |
| 1391   | Layout 1             | `6eb6a9b27cdf`  |
| 1390   | Layout 1             | `6eb6a9b27cdf`  |
| 1386   | Layout 1             | `6eb6a9b27cdf`  |
| 1381   | Layout 1             | `6eb6a9b27cdf`  |
| 1379   | Layout 1             | `6eb6a9b27cdf`  |
| 1372   | Layout 1             | `6eb6a9b27cdf`  |
| 1366   | Layout 1             | `6eb6a9b27cdf`  |
| 1364   | Layout 1             | `6eb6a9b27cdf`  |
| 1363   | Layout 1             | `6eb6a9b27cdf`  |
| 1360   | Layout 1             | `6eb6a9b27cdf`  |
| 1358   | Layout 1             | `6eb6a9b27cdf`  |
| 1355   | Layout 1             | `6eb6a9b27cdf`  |
| 1351   | Layout 1             | `6eb6a9b27cdf`  |
| 1348   | Layout 1             | `6eb6a9b27cdf`  |
| 1346   | Layout 1             | `6eb6a9b27cdf`  |
| 1341   | Layout 1             | `6eb6a9b27cdf`  |
| 1340   | Layout 1             | `6eb6a9b27cdf`  |
| 1338   | Layout 1             | `6eb6a9b27cdf`  |
| 1335   | Layout 1             | `6eb6a9b27cdf`  |
| 1333   | Layout 1             | `6eb6a9b27cdf`  |
| 1329   | Layout 1             | `6eb6a9b27cdf`  |
| 1327   | Layout 1             | `6eb6a9b27cdf`  |
| 1324   | Layout 1             | `6eb6a9b27cdf`  |
| 1321   | Layout 1             | `6eb6a9b27cdf`  |
| 1319   | Layout 1             | `6eb6a9b27cdf`  |
| 1318   | Layout 1             | `6eb6a9b27cdf`  |
| 1316   | Layout 1             | `6eb6a9b27cdf`  |
| 1313   | Layout 1             | `6eb6a9b27cdf`  |
| 1311   | Layout 1             | `6eb6a9b27cdf`  |
| 1309   | Layout 1             | `6eb6a9b27cdf`  |
| 1304   | Layout 1             | `6eb6a9b27cdf`  |
| 1292   | Layout 1             | `6eb6a9b27cdf`  |
| 1286   | Layout 1             | `6eb6a9b27cdf`  |
| 1280   | Layout 1             | `6eb6a9b27cdf`  |
| 1276   | Layout 1             | `6eb6a9b27cdf`  |
| 1267   | Layout 1             | `6eb6a9b27cdf`  |
| 1261   | Layout 1             | `6eb6a9b27cdf`  |
| 1256   | Layout 1             | `6eb6a9b27cdf`  |
| 1250   | Layout 1             | `6eb6a9b27cdf`  |
| 1246   | Layout 1             | `6eb6a9b27cdf`  |
| 1239   | Layout 1             | `6eb6a9b27cdf`  |
| 1230   | Layout 1             | `6eb6a9b27cdf`  |
| 1226   | Layout 1             | `6eb6a9b27cdf`  |
| 1220   | Layout 1             | `6eb6a9b27cdf`  |
| 1217   | Layout 1             | `6eb6a9b27cdf`  |
| 1211   | Layout 1             | `6eb6a9b27cdf`  |
| 1210   | Layout 1             | `6eb6a9b27cdf`  |
| 1208   | Layout 1             | `6eb6a9b27cdf`  |
| 1203   | Layout 1             | `6eb6a9b27cdf`  |
| 1197   | Layout 1             | `6eb6a9b27cdf`  |
| 1194   | Layout 1             | `6eb6a9b27cdf`  |
| 1192   | Layout 1             | `6eb6a9b27cdf`  |
| 1187   | Layout 1             | `6eb6a9b27cdf`  |
| 1183   | Layout 1             | `6eb6a9b27cdf`  |
| 1177   | Layout 1             | `6eb6a9b27cdf`  |
| 1173   | Layout 1             | `6eb6a9b27cdf`  |
| 1167   | Layout 1             | `6eb6a9b27cdf`  |
| 1164   | Layout 1             | `6eb6a9b27cdf`  |
| 1156   | Layout 1             | `6eb6a9b27cdf`  |
| 1149   | Layout 1             | `6eb6a9b27cdf`  |
| 1144   | Layout 1             | `6eb6a9b27cdf`  |
| 1137   | Layout 1             | `6eb6a9b27cdf`  |
| 1132   | Layout 1             | `6eb6a9b27cdf`  |
| 1127   | Layout 1             | `6eb6a9b27cdf`  |
| 1122   | Layout 1             | `6eb6a9b27cdf`  |
| 1118   | Layout 1             | `6eb6a9b27cdf`  |
| 1114   | Layout 1             | `6eb6a9b27cdf`  |
| 1109   | Layout 1             | `6eb6a9b27cdf`  |
| 1102   | No file              | `6eb6a9b27cdf`  |
| 1096   | No file              | `6eb6a9b27cdf`  |
| 1088   | No file              | `6eb6a9b27cdf`  |
| 1081   | No file              | `6eb6a9b27cdf`  |
| 1076   | No file              | `6eb6a9b27cdf`  |
| 1069   | No file              | `6eb6a9b27cdf`  |
| 1064   | No file              | `6eb6a9b27cdf`  |
| 1058   | No file              | `6eb6a9b27cdf`  |
| 1051   | No file              | `6eb6a9b27cdf`  |
| 1044   | No file              | `6eb6a9b27cdf`  |
| 1036   | No file              | `6eb6a9b27cdf`  |
| 1026   | No file              | `6eb6a9b27cdf`  |
| 1016   | No file              | `6eb6a9b27cdf`  |
| 1009   | No file              | `6eb6a9b27cdf`  |
| 1005   | No file              | `6eb6a9b27cdf`  |
| 1000   | No file              | `6eb6a9b27cdf`  |
| 998    | No file              | `6eb6a9b27cdf`  |
| 990    | No file              | `6eb6a9b27cdf`  |
| 979    | No file              | `6eb6a9b27cdf`  |
| 972    | No file              | `6eb6a9b27cdf`  |
| 963    | No file              | `6eb6a9b27cdf`  |
| 955    | No file              | `6eb6a9b27cdf`  |
| 946    | No file              | `6eb6a9b27cdf`  |
| 938    | No file              | `6eb6a9b27cdf`  |
| 927    | No file              | `6eb6a9b27cdf`  |
| 911    | No file              | `6eb6a9b27cdf`  |
| 904    | No file              | `6eb6a9b27cdf`  |
| 899    | No file              | `6eb6a9b27cdf`  |
| 894    | No file              | `6eb6a9b27cdf`  |
| 885    | No file              | `6eb6a9b27cdf`  |
| 879    | No file              | `6eb6a9b27cdf`  |
| 872    | No file              | `6eb6a9b27cdf`  |
| 864    | No file              | `6eb6a9b27cdf`  |
| 855    | No file              | `6eb6a9b27cdf`  |
| 853    | No file              | `6eb6a9b27cdf`  |
| 845    | No file              | `6eb6a9b27cdf`  |
| 837    | No file              | `6eb6a9b27cdf`  |
| 829    | Layout 1             | `6eb6a9b27cdf`  |
| 822    | Layout 1             | `6eb6a9b27cdf`  |
| 814    | Layout 1             | `6eb6a9b27cdf`  |
| 805    | Layout 1             | `6eb6a9b27cdf`  |
| 794    | No documented layout | `6eb6a9b27cdf`  |
| 787    | No documented layout | `6eb6a9b27cdf`  |
| 780    | No documented layout | `6eb6a9b27cdf`  |
| 771    | No documented layout | `6eb6a9b27cdf`  |
| 760    | No documented layout | `6eb6a9b27cdf`  |
| 748    | No documented layout | `6eb6a9b27cdf`  |
| 741    | No documented layout | `6eb6a9b27cdf`  |
| 736    | No documented layout | `6eb6a9b27cdf`  |
| 731    | No documented layout | `6eb6a9b27cdf`  |
| 723    | No documented layout | `6eb6a9b27cdf`  |
| 711    | No documented layout | `6eb6a9b27cdf`  |
| 707    | No documented layout | `6eb6a9b27cdf`  |
| 697    | No documented layout | `6eb6a9b27cdf`  |
| 689    | No documented layout | `6eb6a9b27cdf`  |
| 683    | No documented layout | `6eb6a9b27cdf`  |
| 678    | No documented layout | `6eb6a9b27cdf`  |
| 670    | No documented layout | `6eb6a9b27cdf`  |
| 661    | No documented layout | `6eb6a9b27cdf`  |
| 656    | No documented layout | `6eb6a9b27cdf`  |
| 652    | No documented layout | `6eb6a9b27cdf`  |
| 643    | No documented layout | `6eb6a9b27cdf`  |
| 637    | No documented layout | `6eb6a9b27cdf`  |
| 630    | No documented layout | `6eb6a9b27cdf`  |
| 627    | No documented layout | `6eb6a9b27cdf`  |
| 621    | No documented layout | `6eb6a9b27cdf`  |
| 617    | No documented layout | `6eb6a9b27cdf`  |
| 615    | No documented layout | `6eb6a9b27cdf`  |
| 606    | No documented layout | `6eb6a9b27cdf`  |
| 599    | No documented layout | `6eb6a9b27cdf`  |
| 592    | No documented layout | `6eb6a9b27cdf`  |
| 586    | No documented layout | `6eb6a9b27cdf`  |
| 577    | No documented layout | `6eb6a9b27cdf`  |
| 569    | No documented layout | `6eb6a9b27cdf`  |
| 561    | No documented layout | `6eb6a9b27cdf`  |
| 554    | No documented layout | `6eb6a9b27cdf`  |
| 542    | No documented layout | `6eb6a9b27cdf`  |
| 532    | No documented layout | `6eb6a9b27cdf`  |
| 531    | No documented layout | `6eb6a9b27cdf`  |
| 526    | No documented layout | `6eb6a9b27cdf`  |
| 521    | No documented layout | `6eb6a9b27cdf`  |
| 517    | No documented layout | `6eb6a9b27cdf`  |
| 510    | No documented layout | `6eb6a9b27cdf`  |
| 508    | No documented layout | `6eb6a9b27cdf`  |
| 504    | No documented layout | `6eb6a9b27cdf`  |
| 497    | No documented layout | `6eb6a9b27cdf`  |
| 491    | No documented layout | `6eb6a9b27cdf`  |
| 485    | No documented layout | `6eb6a9b27cdf`  |
| 478    | No documented layout | `6eb6a9b27cdf`  |
| 472    | No documented layout | `6eb6a9b27cdf`  |
| 466    | No documented layout | `6eb6a9b27cdf`  |
| 457    | No documented layout | `6eb6a9b27cdf`  |
| 452    | No documented layout | `6eb6a9b27cdf`  |
| 449    | No documented layout | `6eb6a9b27cdf`  |
| 435    | No documented layout | `6eb6a9b27cdf`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes |
| ------------------- | ------------ | ------------ | ----- |
| `+0x00`             | char[4]      | magic        | `PABR` |
| `+0x04`             | u32          | count        | Number of entries; `76` on client 3473 |
| `+0x08`             | Entry[count] | entries      | See Entry |
| `entries+0x00`      | String Table | string_table | See String Table |
| `string_table+0x00` | u32          | data_end     | `8 + count × 58`, the offset of the trailer |
| `string_table+0x04` | u32          | zero         | `0` |

### Entry (58 bytes)

| Offset  | Type         | Field       | Notes |
| ------- | ------------ | ----------- | ----- |
| `+0x00` | u16          | group       | Map key: level group, see Level Groups |
| `+0x02` | i16          | level       | Map key: level, from 1 |
| `+0x04` | u16          | key_group   | Equals `group` in every entry |
| `+0x06` | i16          | key_level   | Equals `level` in every entry |
| `+0x08` | i32          | need_time   | `600` in every entry; the unit is not confirmed |
| `+0x0C` | Need Item[3] | need_items  | Three slots of a u32 item ID and an i64 count, see Need Item |
| `+0x30` | i16          | need_point  | Contribution points: `10` in group 1, `5` in group 2, `50` in groups 3 and 4 |
| `+0x32` | i64          | need_money  | `0` in every entry |

### Need Item (12 bytes)

Each `need_items` slot.

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | u32  | item_id | `0` in every slot on client 3473 |
| `+0x04` | i64  | count   | `0` in every slot on client 3473 |

### String Table (variable: 4 bytes + strings)

The PABR string table, here with no strings.

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Level Groups

The groups on client 3473. The names translate the developer comments of the private server's sheet (see Field Names).

| Group | Levels | Name | Referenced by |
| ----: | -----: | ---- | ------------- |
| 1 | 1 to 16 | Town, common | `planttown.bss` `upgrade_resource_key` |
| 2 | 1 to 10 | Farm, small | The `UpgradeResource` column of the `PlantZone_Table` sheet; `plantzone.dbss` has no field for it |
| 3 | 1 to 20 | Farm, medium | - |
| 4 | 1 to 30 | Farm, large | - |

## Notes

- Total size is `8 + count × 58 + 12`: 4,428 bytes on client 3473.
- The entries are in neither key nor level order (`(4, 13)`, `(3, 13)`, `(1, 13)`, `(4, 12)` ...). The 2016 client loads the table into a `pa::BinaryUnorderedMap` keyed by (group, level).
- No client Lua names this table; the only plant upgrade names in Lua are the `CppEnums.PlantLevelType` values (`ePlantLevelType_PlantTown`, `ePlantLevelType_PlantZoneEfficiency` and three more) in `global_define_cpp_enum.luac`.

## Field Names

The names follow the 2016 `gc::PlantUpgradeResourceStaticStatus` (`_key` as `PlantUpgradeResourceLevelKey` of a u16 key and a short level, `_needTime`, `_needItems` as three `NeedItem` of an `ItemEnchantKey` and an `__int64` count, `_needPoint` as a short, `_needMoney` as an `__int64`) and the `PlantUpgradeLevel_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (columns `LevelGoup`, `Level`, `NeedTime`, `NeedExplorePoint`, `NeedMoney`, `NeedItem1` to `NeedItemCount3`). Matched by (group, level) over the 76 entries both hold: every column equals its field on 76 of 76 (client 3473), `NeedExplorePoint` included, the one column whose values vary. The 2016 `_isBlockedNpcWork` bool has no byte in the record.

## Open Questions

### `need_time` Unit

`need_time` is `600` in every entry and in the sheet. Seconds would make every town and farm upgrade take 10 minutes, and no client Lua reads it. The 2016 loader (`GameCommonParameterLoaderFromExcel::LoadPlantUpgradeResourceInformation`) reads the `NeedTime` column with `pa::setValueFromExcel<int>` straight into `_needTime`, with no scaling, so the file holds the sheet's number. No other 2016 function names the table: its `StaticStatusManager::get` is one shared body with the `planttown.bss` manager's, so its callers cannot be told apart, and the code that turns `_needTime` into a duration is not found.
