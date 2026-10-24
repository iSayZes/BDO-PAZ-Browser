# `elementalserverbuff.bss` Format

## Purpose

The server-wide Blessings of the Black Shrine (Land of the Morning Light):
after a Black Shrine boss is defeated, its server gets the Blessing of the
Sun (AP), the Blessing of the Moon (DP) or the Blessing of the Earth (Item
Drop Rate) for 180 minutes. Each of the four rows holds the three blessing
values and their duration, `1` AP, `1` DP, `200000` (+20%) and `10800`
seconds on every row (client 3474), one row per Calamity 7 to 10. The file has no
PABR magic and no trailer. The aura stats of the same content are in
[`elementalstat.bss`](elementalstat_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 2308 and later | 3483    | `elementalserverbuff.bss` | 136   | 6 Row   | 22        |

| Layout | File                      | Known         | Unknown      |
| ------ | ------------------------- | ------------- | ------------ |
| 1      | `elementalserverbuff.bss` | 112 B (82.4%) | 24 B (17.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6b8354d6a9b1`  |
| 3482   | Layout 1 | `6b8354d6a9b1`  |
| 3474   | Layout 1 | `6b8354d6a9b1`  |
| 3473   | Layout 1 | `6b8354d6a9b1`  |
| 3464   | Layout 1 | `6b8354d6a9b1`  |
| 3458   | Layout 1 | `6b8354d6a9b1`  |
| 3454   | Layout 1 | `6b8354d6a9b1`  |
| 3444   | Layout 1 | `6b8354d6a9b1`  |
| 3435   | Layout 1 | `6b8354d6a9b1`  |
| 3426   | Layout 1 | `6b8354d6a9b1`  |
| 3418   | Layout 1 | `6b8354d6a9b1`  |
| 3412   | Layout 1 | `6b8354d6a9b1`  |
| 3402   | Layout 1 | `6b8354d6a9b1`  |
| 3396   | Layout 1 | `6b8354d6a9b1`  |
| 3387   | Layout 1 | `6b8354d6a9b1`  |
| 3381   | Layout 1 | `6b8354d6a9b1`  |
| 3373   | Layout 1 | `6b8354d6a9b1`  |
| 3364   | Layout 1 | `6b8354d6a9b1`  |
| 3356   | Layout 1 | `6b8354d6a9b1`  |
| 3349   | Layout 1 | `6b8354d6a9b1`  |
| 3342   | Layout 1 | `6b8354d6a9b1`  |
| 3335   | Layout 1 | `6b8354d6a9b1`  |
| 3326   | Layout 1 | `6b8354d6a9b1`  |
| 3321   | Layout 1 | `6b8354d6a9b1`  |
| 3314   | Layout 1 | `6b8354d6a9b1`  |
| 3303   | Layout 1 | `6b8354d6a9b1`  |
| 3302   | Layout 1 | `6b8354d6a9b1`  |
| 3293   | Layout 1 | `6b8354d6a9b1`  |
| 3283   | Layout 1 | `6b8354d6a9b1`  |
| 3275   | Layout 1 | `6b8354d6a9b1`  |
| 3267   | Layout 1 | `6b8354d6a9b1`  |
| 3258   | Layout 1 | `6b8354d6a9b1`  |
| 3251   | Layout 1 | `6b8354d6a9b1`  |
| 3242   | Layout 1 | `6b8354d6a9b1`  |
| 3235   | Layout 1 | `6b8354d6a9b1`  |
| 3229   | Layout 1 | `6b8354d6a9b1`  |
| 3212   | Layout 1 | `6b8354d6a9b1`  |
| 3203   | Layout 1 | `6b8354d6a9b1`  |
| 3193   | Layout 1 | `6b8354d6a9b1`  |
| 3186   | Layout 1 | `6b8354d6a9b1`  |
| 3177   | Layout 1 | `6b8354d6a9b1`  |
| 3169   | Layout 1 | `6b8354d6a9b1`  |
| 3158   | Layout 1 | `6b8354d6a9b1`  |
| 3151   | Layout 1 | `6b8354d6a9b1`  |
| 3144   | Layout 1 | `6b8354d6a9b1`  |
| 3133   | Layout 1 | `6b8354d6a9b1`  |
| 3125   | Layout 1 | `6b8354d6a9b1`  |
| 3118   | Layout 1 | `6b8354d6a9b1`  |
| 3111   | Layout 1 | `6b8354d6a9b1`  |
| 3103   | Layout 1 | `6b8354d6a9b1`  |
| 3095   | Layout 1 | `6b8354d6a9b1`  |
| 3086   | Layout 1 | `6b8354d6a9b1`  |
| 3072   | Layout 1 | `6b8354d6a9b1`  |
| 3062   | Layout 1 | `6b8354d6a9b1`  |
| 3052   | Layout 1 | `6b8354d6a9b1`  |
| 3045   | Layout 1 | `6b8354d6a9b1`  |
| 3037   | Layout 1 | `6b8354d6a9b1`  |
| 3030   | Layout 1 | `6b8354d6a9b1`  |
| 3021   | Layout 1 | `6b8354d6a9b1`  |
| 3012   | Layout 1 | `6b8354d6a9b1`  |
| 3002   | Layout 1 | `6b8354d6a9b1`  |
| 2995   | Layout 1 | `6b8354d6a9b1`  |
| 2987   | Layout 1 | `6b8354d6a9b1`  |
| 2978   | Layout 1 | `6b8354d6a9b1`  |
| 2970   | Layout 1 | `6b8354d6a9b1`  |
| 2959   | Layout 1 | `6b8354d6a9b1`  |
| 2951   | Layout 1 | `6b8354d6a9b1`  |
| 2942   | Layout 1 | `6b8354d6a9b1`  |
| 2935   | Layout 1 | `6b8354d6a9b1`  |
| 2932   | Layout 1 | `6b8354d6a9b1`  |
| 2923   | Layout 1 | `6b8354d6a9b1`  |
| 2919   | Layout 1 | `6b8354d6a9b1`  |
| 2907   | Layout 1 | `6b8354d6a9b1`  |
| 2900   | Layout 1 | `6b8354d6a9b1`  |
| 2891   | Layout 1 | `6b8354d6a9b1`  |
| 2882   | Layout 1 | `6b8354d6a9b1`  |
| 2872   | Layout 1 | `6b8354d6a9b1`  |
| 2863   | Layout 1 | `6b8354d6a9b1`  |
| 2855   | Layout 1 | `6b8354d6a9b1`  |
| 2849   | Layout 1 | `6b8354d6a9b1`  |
| 2844   | Layout 1 | `6b8354d6a9b1`  |
| 2834   | Layout 1 | `6b8354d6a9b1`  |
| 2825   | Layout 1 | `6b8354d6a9b1`  |
| 2819   | Layout 1 | `6b8354d6a9b1`  |
| 2811   | Layout 1 | `6b8354d6a9b1`  |
| 2803   | Layout 1 | `6b8354d6a9b1`  |
| 2794   | Layout 1 | `6b8354d6a9b1`  |
| 2783   | Layout 1 | `6b8354d6a9b1`  |
| 2774   | Layout 1 | `6b8354d6a9b1`  |
| 2765   | Layout 1 | `6b8354d6a9b1`  |
| 2756   | Layout 1 | `6b8354d6a9b1`  |
| 2750   | Layout 1 | `6b8354d6a9b1`  |
| 2743   | Layout 1 | `6b8354d6a9b1`  |
| 2736   | Layout 1 | `6b8354d6a9b1`  |
| 2726   | Layout 1 | `6b8354d6a9b1`  |
| 2717   | Layout 1 | `6b8354d6a9b1`  |
| 2709   | Layout 1 | `6b8354d6a9b1`  |
| 2703   | Layout 1 | `6b8354d6a9b1`  |
| 2695   | Layout 1 | `6b8354d6a9b1`  |
| 2684   | Layout 1 | `6b8354d6a9b1`  |
| 2672   | Layout 1 | `6b8354d6a9b1`  |
| 2665   | Layout 1 | `6b8354d6a9b1`  |
| 2657   | Layout 1 | `6b8354d6a9b1`  |
| 2649   | Layout 1 | `6b8354d6a9b1`  |
| 2644   | Layout 1 | `6b8354d6a9b1`  |
| 2637   | Layout 1 | `6b8354d6a9b1`  |
| 2629   | Layout 1 | `6b8354d6a9b1`  |
| 2619   | Layout 1 | `6b8354d6a9b1`  |
| 2612   | Layout 1 | `6b8354d6a9b1`  |
| 2606   | Layout 1 | `6b8354d6a9b1`  |
| 2602   | Layout 1 | `6b8354d6a9b1`  |
| 2601   | Layout 1 | `6b8354d6a9b1`  |
| 2592   | Layout 1 | `6b8354d6a9b1`  |
| 2583   | Layout 1 | `6b8354d6a9b1`  |
| 2575   | Layout 1 | `6b8354d6a9b1`  |
| 2567   | Layout 1 | `6b8354d6a9b1`  |
| 2560   | Layout 1 | `6b8354d6a9b1`  |
| 2553   | Layout 1 | `6b8354d6a9b1`  |
| 2545   | Layout 1 | `6b8354d6a9b1`  |
| 2538   | Layout 1 | `6b8354d6a9b1`  |
| 2529   | Layout 1 | `6b8354d6a9b1`  |
| 2519   | Layout 1 | `6b8354d6a9b1`  |
| 2513   | Layout 1 | `6b8354d6a9b1`  |
| 2510   | Layout 1 | `6b8354d6a9b1`  |
| 2507   | Layout 1 | `6b8354d6a9b1`  |
| 2503   | Layout 1 | `6b8354d6a9b1`  |
| 2498   | Layout 1 | `6b8354d6a9b1`  |
| 2492   | Layout 1 | `6b8354d6a9b1`  |
| 2487   | Layout 1 | `6b8354d6a9b1`  |
| 2480   | Layout 1 | `6b8354d6a9b1`  |
| 2474   | Layout 1 | `6b8354d6a9b1`  |
| 2468   | Layout 1 | `6b8354d6a9b1`  |
| 2460   | Layout 1 | `6b8354d6a9b1`  |
| 2453   | Layout 1 | `6b8354d6a9b1`  |
| 2444   | Layout 1 | `6b8354d6a9b1`  |
| 2438   | Layout 1 | `6b8354d6a9b1`  |
| 2434   | Layout 1 | `6b8354d6a9b1`  |
| 2429   | Layout 1 | `6b8354d6a9b1`  |
| 2421   | Layout 1 | `6b8354d6a9b1`  |
| 2414   | Layout 1 | `6b8354d6a9b1`  |
| 2407   | Layout 1 | `6b8354d6a9b1`  |
| 2401   | Layout 1 | `6b8354d6a9b1`  |
| 2397   | Layout 1 | `6b8354d6a9b1`  |
| 2393   | Layout 1 | `6b8354d6a9b1`  |
| 2384   | Layout 1 | `6b8354d6a9b1`  |
| 2378   | Layout 1 | `6b8354d6a9b1`  |
| 2372   | Layout 1 | `6b8354d6a9b1`  |
| 2358   | Layout 1 | `6b8354d6a9b1`  |
| 2352   | Layout 1 | `6b8354d6a9b1`  |
| 2347   | Layout 1 | `6b8354d6a9b1`  |
| 2343   | Layout 1 | `6b8354d6a9b1`  |
| 2335   | Layout 1 | `6b8354d6a9b1`  |
| 2327   | Layout 1 | `6b8354d6a9b1`  |
| 2324   | Layout 1 | `6b8354d6a9b1`  |
| 2319   | Layout 1 | `6b8354d6a9b1`  |
| 2313   | Layout 1 | `6b8354d6a9b1`  |
| 2308   | Layout 1 | `6b8354d6a9b1`  |
| 2302   | No file  | `6b8354d6a9b1`  |
| 2295   | No file  | `6b8354d6a9b1`  |
| 2290   | No file  | `6b8354d6a9b1`  |
| 2284   | No file  | `6b8354d6a9b1`  |
| 2276   | No file  | `6b8354d6a9b1`  |
| 2269   | No file  | `6b8354d6a9b1`  |
| 2259   | No file  | `6b8354d6a9b1`  |
| 2250   | No file  | `6b8354d6a9b1`  |
| 2243   | No file  | `6b8354d6a9b1`  |
| 2235   | No file  | `6b8354d6a9b1`  |
| 2229   | No file  | `6b8354d6a9b1`  |
| 2224   | No file  | `6b8354d6a9b1`  |
| 2218   | No file  | `6b8354d6a9b1`  |
| 2215   | No file  | `6b8354d6a9b1`  |
| 2207   | No file  | `6b8354d6a9b1`  |
| 2203   | No file  | `6b8354d6a9b1`  |
| 2196   | No file  | `6b8354d6a9b1`  |
| 2192   | No file  | `6b8354d6a9b1`  |
| 2189   | No file  | `6b8354d6a9b1`  |
| 2183   | No file  | `6b8354d6a9b1`  |
| 2179   | No file  | `6b8354d6a9b1`  |
| 2171   | No file  | `6b8354d6a9b1`  |
| 2163   | No file  | `6b8354d6a9b1`  |
| 2156   | No file  | `6b8354d6a9b1`  |
| 2151   | No file  | `6b8354d6a9b1`  |
| 2147   | No file  | `6b8354d6a9b1`  |
| 2142   | No file  | `6b8354d6a9b1`  |
| 2138   | No file  | `6b8354d6a9b1`  |
| 2134   | No file  | `6b8354d6a9b1`  |
| 2130   | No file  | `6b8354d6a9b1`  |
| 2122   | No file  | `6b8354d6a9b1`  |
| 2107   | No file  | `6b8354d6a9b1`  |
| 2098   | No file  | `6b8354d6a9b1`  |
| 2089   | No file  | `6b8354d6a9b1`  |
| 2081   | No file  | `6b8354d6a9b1`  |
| 2073   | No file  | `6b8354d6a9b1`  |
| 2067   | No file  | `6b8354d6a9b1`  |
| 2063   | No file  | `6b8354d6a9b1`  |
| 2059   | No file  | `6b8354d6a9b1`  |
| 2052   | No file  | `6b8354d6a9b1`  |
| 2044   | No file  | `6b8354d6a9b1`  |
| 2039   | No file  | `6b8354d6a9b1`  |
| 2032   | No file  | `6b8354d6a9b1`  |
| 2025   | No file  | `6b8354d6a9b1`  |
| 2011   | No file  | `6b8354d6a9b1`  |
| 2005   | No file  | `6b8354d6a9b1`  |
| 2000   | No file  | `6b8354d6a9b1`  |
| 1996   | No file  | `6b8354d6a9b1`  |
| 1991   | No file  | `6b8354d6a9b1`  |
| 1985   | No file  | `6b8354d6a9b1`  |
| 1980   | No file  | `6b8354d6a9b1`  |
| 1969   | No file  | `6b8354d6a9b1`  |
| 1964   | No file  | `6b8354d6a9b1`  |
| 1958   | No file  | `6b8354d6a9b1`  |
| 1950   | No file  | `6b8354d6a9b1`  |
| 1945   | No file  | `6b8354d6a9b1`  |
| 1937   | No file  | `6b8354d6a9b1`  |
| 1933   | No file  | `6b8354d6a9b1`  |
| 1927   | No file  | `6b8354d6a9b1`  |
| 1921   | No file  | `6b8354d6a9b1`  |
| 1914   | No file  | `6b8354d6a9b1`  |
| 1908   | No file  | `6b8354d6a9b1`  |
| 1897   | No file  | `6b8354d6a9b1`  |
| 1892   | No file  | `6b8354d6a9b1`  |
| 1886   | No file  | `6b8354d6a9b1`  |
| 1881   | No file  | `6b8354d6a9b1`  |
| 1871   | No file  | `6b8354d6a9b1`  |
| 1866   | No file  | `6b8354d6a9b1`  |
| 1862   | No file  | `6b8354d6a9b1`  |
| 1854   | No file  | `6b8354d6a9b1`  |
| 1846   | No file  | `6b8354d6a9b1`  |
| 1838   | No file  | `6b8354d6a9b1`  |
| 1832   | No file  | `6b8354d6a9b1`  |
| 1826   | No file  | `6b8354d6a9b1`  |
| 1822   | No file  | `6b8354d6a9b1`  |
| 1818   | No file  | `6b8354d6a9b1`  |
| 1804   | No file  | `6b8354d6a9b1`  |
| 1794   | No file  | `6b8354d6a9b1`  |
| 1790   | No file  | `6b8354d6a9b1`  |
| 1784   | No file  | `6b8354d6a9b1`  |
| 1774   | No file  | `6b8354d6a9b1`  |
| 1771   | No file  | `6b8354d6a9b1`  |
| 1762   | No file  | `6b8354d6a9b1`  |
| 1759   | No file  | `6b8354d6a9b1`  |
| 1754   | No file  | `6b8354d6a9b1`  |
| 1749   | No file  | `6b8354d6a9b1`  |
| 1743   | No file  | `6b8354d6a9b1`  |
| 1737   | No file  | `6b8354d6a9b1`  |
| 1731   | No file  | `6b8354d6a9b1`  |
| 1725   | No file  | `6b8354d6a9b1`  |
| 1717   | No file  | `6b8354d6a9b1`  |
| 1710   | No file  | `6b8354d6a9b1`  |
| 1704   | No file  | `6b8354d6a9b1`  |
| 1698   | No file  | `6b8354d6a9b1`  |
| 1690   | No file  | `6b8354d6a9b1`  |
| 1685   | No file  | `6b8354d6a9b1`  |
| 1680   | No file  | `6b8354d6a9b1`  |
| 1674   | No file  | `6b8354d6a9b1`  |
| 1668   | No file  | `6b8354d6a9b1`  |
| 1659   | No file  | `6b8354d6a9b1`  |
| 1649   | No file  | `6b8354d6a9b1`  |
| 1642   | No file  | `6b8354d6a9b1`  |
| 1636   | No file  | `6b8354d6a9b1`  |
| 1628   | No file  | `6b8354d6a9b1`  |
| 1622   | No file  | `6b8354d6a9b1`  |
| 1614   | No file  | `6b8354d6a9b1`  |
| 1608   | No file  | `6b8354d6a9b1`  |
| 1602   | No file  | `6b8354d6a9b1`  |
| 1598   | No file  | `6b8354d6a9b1`  |
| 1594   | No file  | `6b8354d6a9b1`  |
| 1590   | No file  | `6b8354d6a9b1`  |
| 1587   | No file  | `6b8354d6a9b1`  |
| 1584   | No file  | `6b8354d6a9b1`  |
| 1579   | No file  | `6b8354d6a9b1`  |
| 1572   | No file  | `6b8354d6a9b1`  |
| 1565   | No file  | `6b8354d6a9b1`  |
| 1559   | No file  | `6b8354d6a9b1`  |
| 1554   | No file  | `6b8354d6a9b1`  |
| 1547   | No file  | `6b8354d6a9b1`  |
| 1537   | No file  | `6b8354d6a9b1`  |
| 1529   | No file  | `6b8354d6a9b1`  |
| 1524   | No file  | `6b8354d6a9b1`  |
| 1519   | No file  | `6b8354d6a9b1`  |
| 1509   | No file  | `6b8354d6a9b1`  |
| 1506   | No file  | `6b8354d6a9b1`  |
| 1504   | No file  | `6b8354d6a9b1`  |
| 1500   | No file  | `6b8354d6a9b1`  |
| 1493   | No file  | `6b8354d6a9b1`  |
| 1489   | No file  | `6b8354d6a9b1`  |
| 1485   | No file  | `6b8354d6a9b1`  |
| 1481   | No file  | `6b8354d6a9b1`  |
| 1474   | No file  | `6b8354d6a9b1`  |
| 1466   | No file  | `6b8354d6a9b1`  |
| 1462   | No file  | `6b8354d6a9b1`  |
| 1459   | No file  | `6b8354d6a9b1`  |
| 1453   | No file  | `6b8354d6a9b1`  |
| 1450   | No file  | `6b8354d6a9b1`  |
| 1445   | No file  | `6b8354d6a9b1`  |
| 1439   | No file  | `6b8354d6a9b1`  |
| 1433   | No file  | `6b8354d6a9b1`  |
| 1430   | No file  | `6b8354d6a9b1`  |
| 1426   | No file  | `6b8354d6a9b1`  |
| 1421   | No file  | `6b8354d6a9b1`  |
| 1417   | No file  | `6b8354d6a9b1`  |
| 1416   | No file  | `6b8354d6a9b1`  |
| 1409   | No file  | `6b8354d6a9b1`  |
| 1405   | No file  | `6b8354d6a9b1`  |
| 1401   | No file  | `6b8354d6a9b1`  |
| 1396   | No file  | `6b8354d6a9b1`  |
| 1391   | No file  | `6b8354d6a9b1`  |
| 1390   | No file  | `6b8354d6a9b1`  |
| 1386   | No file  | `6b8354d6a9b1`  |
| 1381   | No file  | `6b8354d6a9b1`  |
| 1379   | No file  | `6b8354d6a9b1`  |
| 1372   | No file  | `6b8354d6a9b1`  |
| 1366   | No file  | `6b8354d6a9b1`  |
| 1364   | No file  | `6b8354d6a9b1`  |
| 1363   | No file  | `6b8354d6a9b1`  |
| 1360   | No file  | `6b8354d6a9b1`  |
| 1358   | No file  | `6b8354d6a9b1`  |
| 1355   | No file  | `6b8354d6a9b1`  |
| 1351   | No file  | `6b8354d6a9b1`  |
| 1348   | No file  | `6b8354d6a9b1`  |
| 1346   | No file  | `6b8354d6a9b1`  |
| 1341   | No file  | `6b8354d6a9b1`  |
| 1340   | No file  | `6b8354d6a9b1`  |
| 1338   | No file  | `6b8354d6a9b1`  |
| 1335   | No file  | `6b8354d6a9b1`  |
| 1333   | No file  | `6b8354d6a9b1`  |
| 1329   | No file  | `6b8354d6a9b1`  |
| 1327   | No file  | `6b8354d6a9b1`  |
| 1324   | No file  | `6b8354d6a9b1`  |
| 1321   | No file  | `6b8354d6a9b1`  |
| 1319   | No file  | `6b8354d6a9b1`  |
| 1318   | No file  | `6b8354d6a9b1`  |
| 1316   | No file  | `6b8354d6a9b1`  |
| 1313   | No file  | `6b8354d6a9b1`  |
| 1311   | No file  | `6b8354d6a9b1`  |
| 1309   | No file  | `6b8354d6a9b1`  |
| 1304   | No file  | `6b8354d6a9b1`  |
| 1292   | No file  | `6b8354d6a9b1`  |
| 1286   | No file  | `6b8354d6a9b1`  |
| 1280   | No file  | `6b8354d6a9b1`  |
| 1276   | No file  | `6b8354d6a9b1`  |
| 1267   | No file  | `6b8354d6a9b1`  |
| 1261   | No file  | `6b8354d6a9b1`  |
| 1256   | No file  | `6b8354d6a9b1`  |
| 1250   | No file  | `6b8354d6a9b1`  |
| 1246   | No file  | `6b8354d6a9b1`  |
| 1239   | No file  | `6b8354d6a9b1`  |
| 1230   | No file  | `6b8354d6a9b1`  |
| 1226   | No file  | `6b8354d6a9b1`  |
| 1220   | No file  | `6b8354d6a9b1`  |
| 1217   | No file  | `6b8354d6a9b1`  |
| 1211   | No file  | `6b8354d6a9b1`  |
| 1210   | No file  | `6b8354d6a9b1`  |
| 1208   | No file  | `6b8354d6a9b1`  |
| 1203   | No file  | `6b8354d6a9b1`  |
| 1197   | No file  | `6b8354d6a9b1`  |
| 1194   | No file  | `6b8354d6a9b1`  |
| 1192   | No file  | `6b8354d6a9b1`  |
| 1187   | No file  | `6b8354d6a9b1`  |
| 1183   | No file  | `6b8354d6a9b1`  |
| 1177   | No file  | `6b8354d6a9b1`  |
| 1173   | No file  | `6b8354d6a9b1`  |
| 1167   | No file  | `6b8354d6a9b1`  |
| 1164   | No file  | `6b8354d6a9b1`  |
| 1156   | No file  | `6b8354d6a9b1`  |
| 1149   | No file  | `6b8354d6a9b1`  |
| 1144   | No file  | `6b8354d6a9b1`  |
| 1137   | No file  | `6b8354d6a9b1`  |
| 1132   | No file  | `6b8354d6a9b1`  |
| 1127   | No file  | `6b8354d6a9b1`  |
| 1122   | No file  | `6b8354d6a9b1`  |
| 1118   | No file  | `6b8354d6a9b1`  |
| 1114   | No file  | `6b8354d6a9b1`  |
| 1109   | No file  | `6b8354d6a9b1`  |
| 1102   | No file  | `6b8354d6a9b1`  |
| 1096   | No file  | `6b8354d6a9b1`  |
| 1088   | No file  | `6b8354d6a9b1`  |
| 1081   | No file  | `6b8354d6a9b1`  |
| 1076   | No file  | `6b8354d6a9b1`  |
| 1069   | No file  | `6b8354d6a9b1`  |
| 1064   | No file  | `6b8354d6a9b1`  |
| 1058   | No file  | `6b8354d6a9b1`  |
| 1051   | No file  | `6b8354d6a9b1`  |
| 1044   | No file  | `6b8354d6a9b1`  |
| 1036   | No file  | `6b8354d6a9b1`  |
| 1026   | No file  | `6b8354d6a9b1`  |
| 1016   | No file  | `6b8354d6a9b1`  |
| 1009   | No file  | `6b8354d6a9b1`  |
| 1005   | No file  | `6b8354d6a9b1`  |
| 1000   | No file  | `6b8354d6a9b1`  |
| 998    | No file  | `6b8354d6a9b1`  |
| 990    | No file  | `6b8354d6a9b1`  |
| 979    | No file  | `6b8354d6a9b1`  |
| 972    | No file  | `6b8354d6a9b1`  |
| 963    | No file  | `6b8354d6a9b1`  |
| 955    | No file  | `6b8354d6a9b1`  |
| 946    | No file  | `6b8354d6a9b1`  |
| 938    | No file  | `6b8354d6a9b1`  |
| 927    | No file  | `6b8354d6a9b1`  |
| 911    | No file  | `6b8354d6a9b1`  |
| 904    | No file  | `6b8354d6a9b1`  |
| 899    | No file  | `6b8354d6a9b1`  |
| 894    | No file  | `6b8354d6a9b1`  |
| 885    | No file  | `6b8354d6a9b1`  |
| 879    | No file  | `6b8354d6a9b1`  |
| 872    | No file  | `6b8354d6a9b1`  |
| 864    | No file  | `6b8354d6a9b1`  |
| 855    | No file  | `6b8354d6a9b1`  |
| 853    | No file  | `6b8354d6a9b1`  |
| 845    | No file  | `6b8354d6a9b1`  |
| 837    | No file  | `6b8354d6a9b1`  |
| 829    | No file  | `6b8354d6a9b1`  |
| 822    | No file  | `6b8354d6a9b1`  |
| 814    | No file  | `6b8354d6a9b1`  |
| 805    | No file  | `6b8354d6a9b1`  |
| 794    | No file  | `6b8354d6a9b1`  |
| 787    | No file  | `6b8354d6a9b1`  |
| 780    | No file  | `6b8354d6a9b1`  |
| 771    | No file  | `6b8354d6a9b1`  |
| 760    | No file  | `6b8354d6a9b1`  |
| 748    | No file  | `6b8354d6a9b1`  |
| 741    | No file  | `6b8354d6a9b1`  |
| 736    | No file  | `6b8354d6a9b1`  |
| 731    | No file  | `6b8354d6a9b1`  |
| 723    | No file  | `6b8354d6a9b1`  |
| 711    | No file  | `6b8354d6a9b1`  |
| 707    | No file  | `6b8354d6a9b1`  |
| 697    | No file  | `6b8354d6a9b1`  |
| 689    | No file  | `6b8354d6a9b1`  |
| 683    | No file  | `6b8354d6a9b1`  |
| 678    | No file  | `6b8354d6a9b1`  |
| 670    | No file  | `6b8354d6a9b1`  |
| 661    | No file  | `6b8354d6a9b1`  |
| 656    | No file  | `6b8354d6a9b1`  |
| 652    | No file  | `6b8354d6a9b1`  |
| 643    | No file  | `6b8354d6a9b1`  |
| 637    | No file  | `6b8354d6a9b1`  |
| 630    | No file  | `6b8354d6a9b1`  |
| 627    | No file  | `6b8354d6a9b1`  |
| 621    | No file  | `6b8354d6a9b1`  |
| 617    | No file  | `6b8354d6a9b1`  |
| 615    | No file  | `6b8354d6a9b1`  |
| 606    | No file  | `6b8354d6a9b1`  |
| 599    | No file  | `6b8354d6a9b1`  |
| 592    | No file  | `6b8354d6a9b1`  |
| 586    | No file  | `6b8354d6a9b1`  |
| 577    | No file  | `6b8354d6a9b1`  |
| 569    | No file  | `6b8354d6a9b1`  |
| 561    | No file  | `6b8354d6a9b1`  |
| 554    | No file  | `6b8354d6a9b1`  |
| 542    | No file  | `6b8354d6a9b1`  |
| 532    | No file  | `6b8354d6a9b1`  |
| 531    | No file  | `6b8354d6a9b1`  |
| 526    | No file  | `6b8354d6a9b1`  |
| 521    | No file  | `6b8354d6a9b1`  |
| 517    | No file  | `6b8354d6a9b1`  |
| 510    | No file  | `6b8354d6a9b1`  |
| 508    | No file  | `6b8354d6a9b1`  |
| 504    | No file  | `6b8354d6a9b1`  |
| 497    | No file  | `6b8354d6a9b1`  |
| 491    | No file  | `6b8354d6a9b1`  |
| 485    | No file  | `6b8354d6a9b1`  |
| 478    | No file  | `6b8354d6a9b1`  |
| 472    | No file  | `6b8354d6a9b1`  |
| 466    | No file  | `6b8354d6a9b1`  |
| 457    | No file  | `6b8354d6a9b1`  |
| 452    | No file  | `6b8354d6a9b1`  |
| 449    | No file  | `6b8354d6a9b1`  |
| 435    | No file  | `6b8354d6a9b1`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 4 x 22 = 92 bytes on client 3474, in
the order `9`, `8`, `7`, `6`.

### Row (22 bytes)

| Offset  | Type | Field                    | Notes                                                                  |
| ------- | ---- | ------------------------ | ---------------------------------------------------------------------- |
| `+0x00` | u8   | calamity_level           | Row key, the stored Black Shrine level; `6` to `9` (Calamity 7 to 10) |
| `+0x01` | u8   | calamity_level_dup       | Equals `calamity_level` on every row                                   |
| `+0x02` | f32  | sun_blessing_ap          | AP of the Blessing of the Sun; `1.0` on every row (client 3474)        |
| `+0x06` | f32  | moon_blessing_dp         | DP of the Blessing of the Moon; `1.0` on every row (client 3474)       |
| `+0x0a` | u32  | earth_blessing_drop_rate | Item Drop Rate of the Blessing of the Earth; 1,000,000 = 100%, `200000` (+20%) on every row (client 3474) |
| `+0x0e` | u32  | buff_duration            | Seconds the blessing lasts; `10800` (180 minutes) on every row (client 3474) |
| `+0x12` | u32  | unknown_12               | `0` on every row (client 3474)                                         |

## Field Names

No reference source has the file. It first appears on client 2519 (absent
on client 2107), so a private server's `DataSheets.bexcel` on client 1784
has no sheet with `Elemental` in its name, and the 2016 client and the
client 519 server tables predate it.

The three blessing fields follow the client Lua and LOC of client 3474.
`panel_personalicon_left_remaster.luac` shows one icon for the three
blessings (`ElementalMonsterBuff`), asks `ToClient_isAppliedElementalMonsterBuff(type)`
and `ToClient_getElementalMonsterBuffRemainTime(type)` for the Sun (`0`),
Moon (`1`) and Land (`2`) types, the order of
[Element Types](elementalstat_bss.md#element-types), and fills the tooltip
from three resource strings:

| Lua type | Tooltip (LOC, client 3474)                                                     | Field                    |
| -------- | ------------------------------------------------------------------------------ | ------------------------ |
| `0` Sun  | "Great Adventurer {familyName} bestows the Blessing of the Sun. AP +1"          | sun_blessing_ap          |
| `1` Moon | "Great Adventurer {familyName} bestows the Blessing of the Moon. DP +1"         | moon_blessing_dp         |
| `2` Land | "Great Adventurer {familyName} bestows the Blessing of the Earth. Item Drop Rate +20%" | earth_blessing_drop_rate |

The values `1`, `1` and `200000` (+20% on the 1,000,000 = 100% scale) sit
in that order in every row. The Item Drop Rate tooltip adds: "Blessing of
the Earth is applied for a certain period on a server where a Black Shrine
boss vulnerable to earth is defeated."

`buff_duration` follows the official Black Desert wiki page "Black Shrine:
Donghae (Solo)" (section "Blessing of Morning Light"): "This buff lasts for
180 minutes", which is `10800` seconds. The same page lists the blessings
as Blessing of the Warm Sun (AP +1), Blessing of the Soft Moon (DP +1) and
Blessing of the Thriving Earth (Item Drop Rate +20%), each from its own
bosses.

## Notes

- The file is the same 92 bytes on clients 3002, 3251 and 3474. On client
  2519, row `6` held `2.0`, `2.0` and `400000` (+40%), twice the values of
  the other rows; the three blessing fields doubled together, and
  `buff_duration` stayed `10800`.
- The official event notice "[Black Shrine] Enhanced Blessing and
  Unpurified Energy"
  ([groupContentNo 8743](https://www.naeu.playblackdesert.com/en-us/News/Detail?groupContentNo=8743),
  July 2 to 17, 2025) doubles the Blessing of the Morning on the server:
  AP +1 to +2 (Sun Aura bosses Golden Pig King, Oduksini, Apex Changui),
  DP +1 to +2 (Moon Aura: Bari, Songakshi, Bamboo Legion Lieutenant) and
  Item Drop Rate +20% to +40% (Earth Aura: Sangoon, Gumiho, Duoksini,
  Imoogi), and says the buffs "last for 3 hours, same as before". That is
  the doubled set of row `6` on client 2519 (2024-05, before this event),
  so an event of the same kind was likely live in that build.
- The stat values are `f32` while the tooltip text writes whole numbers;
  `1.0` is the only value seen, so the file does not show whether the
  client rounds them.
- The tooltip text holds the numbers itself (`AP +1`, `Item Drop Rate
  +20%`); the Lua fills only `{familyName}` and the remaining time, so a
  changed value in this file would not change the text.
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`, one row per key. The Item Drop Rate cell shows the bonus
  (`+20%`) and the Duration cell the time (`3h`); the record keeps the
  stored values.
- `calamity_level` is the stored difficulty of the Black Shrine window
  (`panel_window_morningland_boss_all_1.luac`, `getLevel()` `0` to `9`,
  shown as Calamity 1 to 10), so rows `6` to `9` are Calamity 7 to 10. In
  game on client 3474 clearing Calamity 7 to 10 gives me the blessing, and
  the official wiki page "Black Shrine: Donghae (Solo)" ties it to the
  highest Calamity cleared. On client 2519 only row `6` (Calamity 7) held
  the doubled event set, which fits Calamity 7 being the top level then.
