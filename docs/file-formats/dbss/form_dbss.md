# `form.dbss` Format

## Purpose

The forms (looks) of horses and other mounts that the look change windows
offer: one row per form with its type, the action chart index the model
uses, the horse tier, two UI icons and, on newer clients, the characters
that can take the form. On client 3482 the file holds 297 forms (272 on
client 1784): 115 with `type` `0`, all with a horse icon, and 182 with
`type` `1`: 119 more horses, ships and boats, carriages, donkeys, elephants
and a few others. Companion `formoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File              | Bytes  | Records        | Row bytes                 |
| ------ | -------------- | ----------------- | ------ | -------------- | ------------------------- |
| 2      | 1996 and later | `form.dbss`       | 76,275 | 297 Row        | 31 to 269, 257 on average |
| 2      | 1996 and later | `formoffset.dbss` | 2,974  | 297 Offset Row | 10                        |
| 1      | 1346 to 1991   | `form.dbss`       | 70,234 | 278 Row        | 27 to 265, 253 on average |
| 1      | 1346 to 1991   | `formoffset.dbss` | 2,784  | 278 Offset Row | 10                        |

| Layout | File              | Known             | Unknown    |
| ------ | ----------------- | ----------------- | ---------- |
| 2      | `form.dbss`       | 76,275 B (100.0%) | 0 B (0.0%) |
| 2      | `formoffset.dbss` | 2,974 B (100.0%)  | 0 B (0.0%) |
| 1      | `form.dbss`       | 70,234 B (100.0%) | 0 B (0.0%) |
| 1      | `formoffset.dbss` | 2,784 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `d72a257aaa0e`  |
| 3482   | Layout 2             | `d72a257aaa0e`  |
| 3474   | Layout 2             | `d72a257aaa0e`  |
| 3473   | Layout 2             | `d72a257aaa0e`  |
| 3464   | Layout 2             | `d72a257aaa0e`  |
| 3458   | Layout 2             | `d72a257aaa0e`  |
| 3454   | Layout 2             | `d72a257aaa0e`  |
| 3444   | Layout 2             | `d72a257aaa0e`  |
| 3435   | Layout 2             | `d72a257aaa0e`  |
| 3426   | Layout 2             | `d72a257aaa0e`  |
| 3418   | Layout 2             | `d72a257aaa0e`  |
| 3412   | Layout 2             | `d72a257aaa0e`  |
| 3402   | Layout 2             | `d72a257aaa0e`  |
| 3396   | Layout 2             | `d72a257aaa0e`  |
| 3387   | Layout 2             | `d72a257aaa0e`  |
| 3381   | Layout 2             | `d72a257aaa0e`  |
| 3373   | Layout 2             | `d72a257aaa0e`  |
| 3364   | Layout 2             | `d72a257aaa0e`  |
| 3356   | Layout 2             | `d72a257aaa0e`  |
| 3349   | Layout 2             | `d72a257aaa0e`  |
| 3342   | Layout 2             | `d72a257aaa0e`  |
| 3335   | Layout 2             | `d72a257aaa0e`  |
| 3326   | Layout 2             | `d72a257aaa0e`  |
| 3321   | Layout 2             | `d72a257aaa0e`  |
| 3314   | Layout 2             | `d72a257aaa0e`  |
| 3303   | Layout 2             | `d72a257aaa0e`  |
| 3302   | Layout 2             | `d72a257aaa0e`  |
| 3293   | Layout 2             | `d72a257aaa0e`  |
| 3283   | Layout 2             | `d72a257aaa0e`  |
| 3275   | Layout 2             | `d72a257aaa0e`  |
| 3267   | Layout 2             | `d72a257aaa0e`  |
| 3258   | Layout 2             | `d72a257aaa0e`  |
| 3251   | Layout 2             | `d72a257aaa0e`  |
| 3242   | Layout 2             | `d72a257aaa0e`  |
| 3235   | Layout 2             | `d72a257aaa0e`  |
| 3229   | Layout 2             | `d72a257aaa0e`  |
| 3212   | Layout 2             | `d72a257aaa0e`  |
| 3203   | Layout 2             | `d72a257aaa0e`  |
| 3193   | Layout 2             | `d72a257aaa0e`  |
| 3186   | Layout 2             | `d72a257aaa0e`  |
| 3177   | Layout 2             | `d72a257aaa0e`  |
| 3169   | Layout 2             | `d72a257aaa0e`  |
| 3158   | Layout 2             | `d72a257aaa0e`  |
| 3151   | Layout 2             | `d72a257aaa0e`  |
| 3144   | Layout 2             | `d72a257aaa0e`  |
| 3133   | Layout 2             | `d72a257aaa0e`  |
| 3125   | Layout 2             | `d72a257aaa0e`  |
| 3118   | Layout 2             | `d72a257aaa0e`  |
| 3111   | Layout 2             | `d72a257aaa0e`  |
| 3103   | Layout 2             | `d72a257aaa0e`  |
| 3095   | Layout 2             | `d72a257aaa0e`  |
| 3086   | Layout 2             | `d72a257aaa0e`  |
| 3072   | Layout 2             | `d72a257aaa0e`  |
| 3062   | Layout 2             | `d72a257aaa0e`  |
| 3052   | Layout 2             | `d72a257aaa0e`  |
| 3045   | Layout 2             | `d72a257aaa0e`  |
| 3037   | Layout 2             | `d72a257aaa0e`  |
| 3030   | Layout 2             | `d72a257aaa0e`  |
| 3021   | Layout 2             | `d72a257aaa0e`  |
| 3012   | Layout 2             | `d72a257aaa0e`  |
| 3002   | Layout 2             | `d72a257aaa0e`  |
| 2995   | Layout 2             | `d72a257aaa0e`  |
| 2987   | Layout 2             | `d72a257aaa0e`  |
| 2978   | Layout 2             | `d72a257aaa0e`  |
| 2970   | Layout 2             | `d72a257aaa0e`  |
| 2959   | Layout 2             | `d72a257aaa0e`  |
| 2951   | Layout 2             | `d72a257aaa0e`  |
| 2942   | Layout 2             | `d72a257aaa0e`  |
| 2935   | Layout 2             | `d72a257aaa0e`  |
| 2932   | Layout 2             | `d72a257aaa0e`  |
| 2923   | Layout 2             | `d72a257aaa0e`  |
| 2919   | Layout 2             | `d72a257aaa0e`  |
| 2907   | Layout 2             | `d72a257aaa0e`  |
| 2900   | Layout 2             | `d72a257aaa0e`  |
| 2891   | Layout 2             | `d72a257aaa0e`  |
| 2882   | Layout 2             | `d72a257aaa0e`  |
| 2872   | Layout 2             | `d72a257aaa0e`  |
| 2863   | Layout 2             | `d72a257aaa0e`  |
| 2855   | Layout 2             | `d72a257aaa0e`  |
| 2849   | Layout 2             | `d72a257aaa0e`  |
| 2844   | Layout 2             | `d72a257aaa0e`  |
| 2834   | Layout 2             | `d72a257aaa0e`  |
| 2825   | Layout 2             | `d72a257aaa0e`  |
| 2819   | Layout 2             | `d72a257aaa0e`  |
| 2811   | Layout 2             | `d72a257aaa0e`  |
| 2803   | Layout 2             | `d72a257aaa0e`  |
| 2794   | Layout 2             | `d72a257aaa0e`  |
| 2783   | Layout 2             | `d72a257aaa0e`  |
| 2774   | Layout 2             | `d72a257aaa0e`  |
| 2765   | Layout 2             | `d72a257aaa0e`  |
| 2756   | Layout 2             | `d72a257aaa0e`  |
| 2750   | Layout 2             | `d72a257aaa0e`  |
| 2743   | Layout 2             | `d72a257aaa0e`  |
| 2736   | Layout 2             | `d72a257aaa0e`  |
| 2726   | Layout 2             | `d72a257aaa0e`  |
| 2717   | Layout 2             | `d72a257aaa0e`  |
| 2709   | Layout 2             | `d72a257aaa0e`  |
| 2703   | Layout 2             | `d72a257aaa0e`  |
| 2695   | Layout 2             | `d72a257aaa0e`  |
| 2684   | Layout 2             | `d72a257aaa0e`  |
| 2672   | Layout 2             | `d72a257aaa0e`  |
| 2665   | Layout 2             | `d72a257aaa0e`  |
| 2657   | Layout 2             | `d72a257aaa0e`  |
| 2649   | Layout 2             | `d72a257aaa0e`  |
| 2644   | Layout 2             | `d72a257aaa0e`  |
| 2637   | Layout 2             | `d72a257aaa0e`  |
| 2629   | Layout 2             | `d72a257aaa0e`  |
| 2619   | Layout 2             | `d72a257aaa0e`  |
| 2612   | Layout 2             | `d72a257aaa0e`  |
| 2606   | Layout 2             | `d72a257aaa0e`  |
| 2602   | Layout 2             | `d72a257aaa0e`  |
| 2601   | Layout 2             | `d72a257aaa0e`  |
| 2592   | Layout 2             | `d72a257aaa0e`  |
| 2583   | Layout 2             | `d72a257aaa0e`  |
| 2575   | Layout 2             | `d72a257aaa0e`  |
| 2567   | Layout 2             | `d72a257aaa0e`  |
| 2560   | Layout 2             | `d72a257aaa0e`  |
| 2553   | Layout 2             | `d72a257aaa0e`  |
| 2545   | Layout 2             | `d72a257aaa0e`  |
| 2538   | Layout 2             | `d72a257aaa0e`  |
| 2529   | Layout 2             | `d72a257aaa0e`  |
| 2519   | Layout 2             | `d72a257aaa0e`  |
| 2513   | Layout 2             | `d72a257aaa0e`  |
| 2510   | Layout 2             | `d72a257aaa0e`  |
| 2507   | Layout 2             | `d72a257aaa0e`  |
| 2503   | Layout 2             | `d72a257aaa0e`  |
| 2498   | Layout 2             | `d72a257aaa0e`  |
| 2492   | Layout 2             | `d72a257aaa0e`  |
| 2487   | Layout 2             | `d72a257aaa0e`  |
| 2480   | Layout 2             | `d72a257aaa0e`  |
| 2474   | Layout 2             | `d72a257aaa0e`  |
| 2468   | Layout 2             | `d72a257aaa0e`  |
| 2460   | Layout 2             | `d72a257aaa0e`  |
| 2453   | Layout 2             | `d72a257aaa0e`  |
| 2444   | Layout 2             | `d72a257aaa0e`  |
| 2438   | Layout 2             | `d72a257aaa0e`  |
| 2434   | Layout 2             | `d72a257aaa0e`  |
| 2429   | Layout 2             | `d72a257aaa0e`  |
| 2421   | Layout 2             | `d72a257aaa0e`  |
| 2414   | Layout 2             | `d72a257aaa0e`  |
| 2407   | Layout 2             | `d72a257aaa0e`  |
| 2401   | Layout 2             | `d72a257aaa0e`  |
| 2397   | Layout 2             | `d72a257aaa0e`  |
| 2393   | Layout 2             | `d72a257aaa0e`  |
| 2384   | Layout 2             | `d72a257aaa0e`  |
| 2378   | Layout 2             | `d72a257aaa0e`  |
| 2372   | Layout 2             | `d72a257aaa0e`  |
| 2358   | Layout 2             | `d72a257aaa0e`  |
| 2352   | Layout 2             | `d72a257aaa0e`  |
| 2347   | Layout 2             | `d72a257aaa0e`  |
| 2343   | Layout 2             | `d72a257aaa0e`  |
| 2335   | Layout 2             | `d72a257aaa0e`  |
| 2327   | Layout 2             | `d72a257aaa0e`  |
| 2324   | Layout 2             | `d72a257aaa0e`  |
| 2319   | Layout 2             | `d72a257aaa0e`  |
| 2313   | Layout 2             | `d72a257aaa0e`  |
| 2308   | Layout 2             | `d72a257aaa0e`  |
| 2302   | Layout 2             | `d72a257aaa0e`  |
| 2295   | Layout 2             | `d72a257aaa0e`  |
| 2290   | Layout 2             | `d72a257aaa0e`  |
| 2284   | Layout 2             | `d72a257aaa0e`  |
| 2276   | Layout 2             | `d72a257aaa0e`  |
| 2269   | Layout 2             | `d72a257aaa0e`  |
| 2259   | Layout 2             | `d72a257aaa0e`  |
| 2250   | Layout 2             | `d72a257aaa0e`  |
| 2243   | Layout 2             | `d72a257aaa0e`  |
| 2235   | Layout 2             | `d72a257aaa0e`  |
| 2229   | Layout 2             | `d72a257aaa0e`  |
| 2224   | Layout 2             | `d72a257aaa0e`  |
| 2218   | Layout 2             | `d72a257aaa0e`  |
| 2215   | Layout 2             | `d72a257aaa0e`  |
| 2207   | Layout 2             | `d72a257aaa0e`  |
| 2203   | Layout 2             | `d72a257aaa0e`  |
| 2196   | Layout 2             | `d72a257aaa0e`  |
| 2192   | Layout 2             | `d72a257aaa0e`  |
| 2189   | Layout 2             | `d72a257aaa0e`  |
| 2183   | Layout 2             | `d72a257aaa0e`  |
| 2179   | Layout 2             | `d72a257aaa0e`  |
| 2171   | Layout 2             | `d72a257aaa0e`  |
| 2163   | Layout 2             | `d72a257aaa0e`  |
| 2156   | Layout 2             | `d72a257aaa0e`  |
| 2151   | Layout 2             | `d72a257aaa0e`  |
| 2147   | Layout 2             | `d72a257aaa0e`  |
| 2142   | Layout 2             | `d72a257aaa0e`  |
| 2138   | Layout 2             | `d72a257aaa0e`  |
| 2134   | Layout 2             | `d72a257aaa0e`  |
| 2130   | Layout 2             | `d72a257aaa0e`  |
| 2122   | Layout 2             | `d72a257aaa0e`  |
| 2107   | Layout 2             | `d72a257aaa0e`  |
| 2098   | Layout 2             | `d72a257aaa0e`  |
| 2089   | Layout 2             | `d72a257aaa0e`  |
| 2081   | Layout 2             | `d72a257aaa0e`  |
| 2073   | Layout 2             | `d72a257aaa0e`  |
| 2067   | Layout 2             | `d72a257aaa0e`  |
| 2063   | Layout 2             | `d72a257aaa0e`  |
| 2059   | Layout 2             | `d72a257aaa0e`  |
| 2052   | Layout 2             | `d72a257aaa0e`  |
| 2044   | Layout 2             | `d72a257aaa0e`  |
| 2039   | Layout 2             | `d72a257aaa0e`  |
| 2032   | Layout 2             | `d72a257aaa0e`  |
| 2025   | Layout 2             | `d72a257aaa0e`  |
| 2011   | Layout 2             | `d72a257aaa0e`  |
| 2005   | Layout 2             | `d72a257aaa0e`  |
| 2000   | Layout 2             | `d72a257aaa0e`  |
| 1996   | Layout 2             | `d72a257aaa0e`  |
| 1991   | Layout 1             | `d72a257aaa0e`  |
| 1985   | Layout 1             | `d72a257aaa0e`  |
| 1980   | Layout 1             | `d72a257aaa0e`  |
| 1969   | Layout 1             | `d72a257aaa0e`  |
| 1964   | Layout 1             | `d72a257aaa0e`  |
| 1958   | Layout 1             | `d72a257aaa0e`  |
| 1950   | Layout 1             | `d72a257aaa0e`  |
| 1945   | Layout 1             | `d72a257aaa0e`  |
| 1937   | Layout 1             | `d72a257aaa0e`  |
| 1933   | Layout 1             | `d72a257aaa0e`  |
| 1927   | Layout 1             | `d72a257aaa0e`  |
| 1921   | Layout 1             | `d72a257aaa0e`  |
| 1914   | Layout 1             | `d72a257aaa0e`  |
| 1908   | Layout 1             | `d72a257aaa0e`  |
| 1897   | Layout 1             | `d72a257aaa0e`  |
| 1892   | Layout 1             | `d72a257aaa0e`  |
| 1886   | Layout 1             | `d72a257aaa0e`  |
| 1881   | Layout 1             | `d72a257aaa0e`  |
| 1871   | Layout 1             | `d72a257aaa0e`  |
| 1866   | Layout 1             | `d72a257aaa0e`  |
| 1862   | Layout 1             | `d72a257aaa0e`  |
| 1854   | Layout 1             | `d72a257aaa0e`  |
| 1846   | Layout 1             | `d72a257aaa0e`  |
| 1838   | Layout 1             | `d72a257aaa0e`  |
| 1832   | Layout 1             | `d72a257aaa0e`  |
| 1826   | Layout 1             | `d72a257aaa0e`  |
| 1822   | Layout 1             | `d72a257aaa0e`  |
| 1818   | Layout 1             | `d72a257aaa0e`  |
| 1804   | Layout 1             | `d72a257aaa0e`  |
| 1794   | Layout 1             | `d72a257aaa0e`  |
| 1790   | Layout 1             | `d72a257aaa0e`  |
| 1784   | Layout 1             | `d72a257aaa0e`  |
| 1774   | Layout 1             | `d72a257aaa0e`  |
| 1771   | Layout 1             | `d72a257aaa0e`  |
| 1762   | Layout 1             | `d72a257aaa0e`  |
| 1759   | Layout 1             | `d72a257aaa0e`  |
| 1754   | Layout 1             | `d72a257aaa0e`  |
| 1749   | Layout 1             | `d72a257aaa0e`  |
| 1743   | Layout 1             | `d72a257aaa0e`  |
| 1737   | Layout 1             | `d72a257aaa0e`  |
| 1731   | Layout 1             | `d72a257aaa0e`  |
| 1725   | Layout 1             | `d72a257aaa0e`  |
| 1717   | Layout 1             | `d72a257aaa0e`  |
| 1710   | Layout 1             | `d72a257aaa0e`  |
| 1704   | Layout 1             | `d72a257aaa0e`  |
| 1698   | Layout 1             | `d72a257aaa0e`  |
| 1690   | Layout 1             | `d72a257aaa0e`  |
| 1685   | Layout 1             | `d72a257aaa0e`  |
| 1680   | Layout 1             | `d72a257aaa0e`  |
| 1674   | Layout 1             | `d72a257aaa0e`  |
| 1668   | Layout 1             | `d72a257aaa0e`  |
| 1659   | Layout 1             | `d72a257aaa0e`  |
| 1649   | Layout 1             | `d72a257aaa0e`  |
| 1642   | Layout 1             | `d72a257aaa0e`  |
| 1636   | Layout 1             | `d72a257aaa0e`  |
| 1628   | Layout 1             | `d72a257aaa0e`  |
| 1622   | Layout 1             | `d72a257aaa0e`  |
| 1614   | Layout 1             | `d72a257aaa0e`  |
| 1608   | Layout 1             | `d72a257aaa0e`  |
| 1602   | Layout 1             | `d72a257aaa0e`  |
| 1598   | Layout 1             | `d72a257aaa0e`  |
| 1594   | Layout 1             | `d72a257aaa0e`  |
| 1590   | Layout 1             | `d72a257aaa0e`  |
| 1587   | Layout 1             | `d72a257aaa0e`  |
| 1584   | Layout 1             | `d72a257aaa0e`  |
| 1579   | Layout 1             | `d72a257aaa0e`  |
| 1572   | Layout 1             | `d72a257aaa0e`  |
| 1565   | Layout 1             | `d72a257aaa0e`  |
| 1559   | Layout 1             | `d72a257aaa0e`  |
| 1554   | Layout 1             | `d72a257aaa0e`  |
| 1547   | Layout 1             | `d72a257aaa0e`  |
| 1537   | Layout 1             | `d72a257aaa0e`  |
| 1529   | Layout 1             | `d72a257aaa0e`  |
| 1524   | Layout 1             | `d72a257aaa0e`  |
| 1519   | Layout 1             | `d72a257aaa0e`  |
| 1509   | Layout 1             | `d72a257aaa0e`  |
| 1506   | Layout 1             | `d72a257aaa0e`  |
| 1504   | Layout 1             | `d72a257aaa0e`  |
| 1500   | Layout 1             | `d72a257aaa0e`  |
| 1493   | Layout 1             | `d72a257aaa0e`  |
| 1489   | Layout 1             | `d72a257aaa0e`  |
| 1485   | Layout 1             | `d72a257aaa0e`  |
| 1481   | Layout 1             | `d72a257aaa0e`  |
| 1474   | Layout 1             | `d72a257aaa0e`  |
| 1466   | Layout 1             | `d72a257aaa0e`  |
| 1462   | Layout 1             | `d72a257aaa0e`  |
| 1459   | Layout 1             | `d72a257aaa0e`  |
| 1453   | Layout 1             | `d72a257aaa0e`  |
| 1450   | Layout 1             | `d72a257aaa0e`  |
| 1445   | Layout 1             | `d72a257aaa0e`  |
| 1439   | Layout 1             | `d72a257aaa0e`  |
| 1433   | Layout 1             | `d72a257aaa0e`  |
| 1430   | Layout 1             | `d72a257aaa0e`  |
| 1426   | Layout 1             | `d72a257aaa0e`  |
| 1421   | Layout 1             | `d72a257aaa0e`  |
| 1417   | Layout 1             | `d72a257aaa0e`  |
| 1416   | Layout 1             | `d72a257aaa0e`  |
| 1409   | Layout 1             | `d72a257aaa0e`  |
| 1405   | Layout 1             | `d72a257aaa0e`  |
| 1401   | Layout 1             | `d72a257aaa0e`  |
| 1396   | Layout 1             | `d72a257aaa0e`  |
| 1391   | Layout 1             | `d72a257aaa0e`  |
| 1390   | Layout 1             | `d72a257aaa0e`  |
| 1386   | Layout 1             | `d72a257aaa0e`  |
| 1381   | Layout 1             | `d72a257aaa0e`  |
| 1379   | Layout 1             | `d72a257aaa0e`  |
| 1372   | Layout 1             | `d72a257aaa0e`  |
| 1366   | Layout 1             | `d72a257aaa0e`  |
| 1364   | Layout 1             | `d72a257aaa0e`  |
| 1363   | Layout 1             | `d72a257aaa0e`  |
| 1360   | Layout 1             | `d72a257aaa0e`  |
| 1358   | Layout 1             | `d72a257aaa0e`  |
| 1355   | Layout 1             | `d72a257aaa0e`  |
| 1351   | Layout 1             | `d72a257aaa0e`  |
| 1348   | Layout 1             | `d72a257aaa0e`  |
| 1346   | Layout 1             | `d72a257aaa0e`  |
| 1341   | No documented layout | `d72a257aaa0e`  |
| 1340   | No documented layout | `d72a257aaa0e`  |
| 1338   | No documented layout | `d72a257aaa0e`  |
| 1335   | No documented layout | `d72a257aaa0e`  |
| 1333   | No documented layout | `d72a257aaa0e`  |
| 1329   | No documented layout | `d72a257aaa0e`  |
| 1327   | No documented layout | `d72a257aaa0e`  |
| 1324   | No documented layout | `d72a257aaa0e`  |
| 1321   | No documented layout | `d72a257aaa0e`  |
| 1319   | No documented layout | `d72a257aaa0e`  |
| 1318   | No documented layout | `d72a257aaa0e`  |
| 1316   | No documented layout | `d72a257aaa0e`  |
| 1313   | No documented layout | `d72a257aaa0e`  |
| 1311   | No documented layout | `d72a257aaa0e`  |
| 1309   | No documented layout | `d72a257aaa0e`  |
| 1304   | No documented layout | `d72a257aaa0e`  |
| 1292   | No documented layout | `d72a257aaa0e`  |
| 1286   | No documented layout | `d72a257aaa0e`  |
| 1280   | No documented layout | `d72a257aaa0e`  |
| 1276   | No documented layout | `d72a257aaa0e`  |
| 1267   | No file              | `d72a257aaa0e`  |
| 1261   | No file              | `d72a257aaa0e`  |
| 1256   | No documented layout | `d72a257aaa0e`  |
| 1250   | No file              | `d72a257aaa0e`  |
| 1246   | No file              | `d72a257aaa0e`  |
| 1239   | No file              | `d72a257aaa0e`  |
| 1230   | No file              | `d72a257aaa0e`  |
| 1226   | No file              | `d72a257aaa0e`  |
| 1220   | No file              | `d72a257aaa0e`  |
| 1217   | No file              | `d72a257aaa0e`  |
| 1211   | No file              | `d72a257aaa0e`  |
| 1210   | No file              | `d72a257aaa0e`  |
| 1208   | No file              | `d72a257aaa0e`  |
| 1203   | No file              | `d72a257aaa0e`  |
| 1197   | No file              | `d72a257aaa0e`  |
| 1194   | No file              | `d72a257aaa0e`  |
| 1192   | No file              | `d72a257aaa0e`  |
| 1187   | No file              | `d72a257aaa0e`  |
| 1183   | No file              | `d72a257aaa0e`  |
| 1177   | No file              | `d72a257aaa0e`  |
| 1173   | No file              | `d72a257aaa0e`  |
| 1167   | No file              | `d72a257aaa0e`  |
| 1164   | No file              | `d72a257aaa0e`  |
| 1156   | No file              | `d72a257aaa0e`  |
| 1149   | No file              | `d72a257aaa0e`  |
| 1144   | No file              | `d72a257aaa0e`  |
| 1137   | No file              | `d72a257aaa0e`  |
| 1132   | No file              | `d72a257aaa0e`  |
| 1127   | No file              | `d72a257aaa0e`  |
| 1122   | No file              | `d72a257aaa0e`  |
| 1118   | No file              | `d72a257aaa0e`  |
| 1114   | No file              | `d72a257aaa0e`  |
| 1109   | No file              | `d72a257aaa0e`  |
| 1102   | No file              | `d72a257aaa0e`  |
| 1096   | No file              | `d72a257aaa0e`  |
| 1088   | No file              | `d72a257aaa0e`  |
| 1081   | No file              | `d72a257aaa0e`  |
| 1076   | No file              | `d72a257aaa0e`  |
| 1069   | No file              | `d72a257aaa0e`  |
| 1064   | No file              | `d72a257aaa0e`  |
| 1058   | No file              | `d72a257aaa0e`  |
| 1051   | No file              | `d72a257aaa0e`  |
| 1044   | No file              | `d72a257aaa0e`  |
| 1036   | No file              | `d72a257aaa0e`  |
| 1026   | No file              | `d72a257aaa0e`  |
| 1016   | No file              | `d72a257aaa0e`  |
| 1009   | No file              | `d72a257aaa0e`  |
| 1005   | No file              | `d72a257aaa0e`  |
| 1000   | No file              | `d72a257aaa0e`  |
| 998    | No file              | `d72a257aaa0e`  |
| 990    | No file              | `d72a257aaa0e`  |
| 979    | No file              | `d72a257aaa0e`  |
| 972    | No file              | `d72a257aaa0e`  |
| 963    | No file              | `d72a257aaa0e`  |
| 955    | No file              | `d72a257aaa0e`  |
| 946    | No file              | `d72a257aaa0e`  |
| 938    | No file              | `d72a257aaa0e`  |
| 927    | No file              | `d72a257aaa0e`  |
| 911    | No file              | `d72a257aaa0e`  |
| 904    | No file              | `d72a257aaa0e`  |
| 899    | No file              | `d72a257aaa0e`  |
| 894    | No file              | `d72a257aaa0e`  |
| 885    | No file              | `d72a257aaa0e`  |
| 879    | No file              | `d72a257aaa0e`  |
| 872    | No file              | `d72a257aaa0e`  |
| 864    | No file              | `d72a257aaa0e`  |
| 855    | No file              | `d72a257aaa0e`  |
| 853    | No file              | `d72a257aaa0e`  |
| 845    | No file              | `d72a257aaa0e`  |
| 837    | No file              | `d72a257aaa0e`  |
| 829    | No file              | `d72a257aaa0e`  |
| 822    | No file              | `d72a257aaa0e`  |
| 814    | No file              | `d72a257aaa0e`  |
| 805    | No file              | `d72a257aaa0e`  |
| 794    | No file              | `d72a257aaa0e`  |
| 787    | No file              | `d72a257aaa0e`  |
| 780    | No file              | `d72a257aaa0e`  |
| 771    | No file              | `d72a257aaa0e`  |
| 760    | No file              | `d72a257aaa0e`  |
| 748    | No file              | `d72a257aaa0e`  |
| 741    | No file              | `d72a257aaa0e`  |
| 736    | No file              | `d72a257aaa0e`  |
| 731    | No file              | `d72a257aaa0e`  |
| 723    | No file              | `d72a257aaa0e`  |
| 711    | No file              | `d72a257aaa0e`  |
| 707    | No file              | `d72a257aaa0e`  |
| 697    | No file              | `d72a257aaa0e`  |
| 689    | No file              | `d72a257aaa0e`  |
| 683    | No file              | `d72a257aaa0e`  |
| 678    | No file              | `d72a257aaa0e`  |
| 670    | No file              | `d72a257aaa0e`  |
| 661    | No file              | `d72a257aaa0e`  |
| 656    | No file              | `d72a257aaa0e`  |
| 652    | No file              | `d72a257aaa0e`  |
| 643    | No file              | `d72a257aaa0e`  |
| 637    | No file              | `d72a257aaa0e`  |
| 630    | No file              | `d72a257aaa0e`  |
| 627    | No file              | `d72a257aaa0e`  |
| 621    | No file              | `d72a257aaa0e`  |
| 617    | No file              | `d72a257aaa0e`  |
| 615    | No file              | `d72a257aaa0e`  |
| 606    | No file              | `d72a257aaa0e`  |
| 599    | No file              | `d72a257aaa0e`  |
| 592    | No file              | `d72a257aaa0e`  |
| 586    | No file              | `d72a257aaa0e`  |
| 577    | No file              | `d72a257aaa0e`  |
| 569    | No file              | `d72a257aaa0e`  |
| 561    | No file              | `d72a257aaa0e`  |
| 554    | No file              | `d72a257aaa0e`  |
| 542    | No file              | `d72a257aaa0e`  |
| 532    | No file              | `d72a257aaa0e`  |
| 531    | No file              | `d72a257aaa0e`  |
| 526    | No file              | `d72a257aaa0e`  |
| 521    | No file              | `d72a257aaa0e`  |
| 517    | No file              | `d72a257aaa0e`  |
| 510    | No file              | `d72a257aaa0e`  |
| 508    | No file              | `d72a257aaa0e`  |
| 504    | No file              | `d72a257aaa0e`  |
| 497    | No file              | `d72a257aaa0e`  |
| 491    | No file              | `d72a257aaa0e`  |
| 485    | No file              | `d72a257aaa0e`  |
| 478    | No file              | `d72a257aaa0e`  |
| 472    | No file              | `d72a257aaa0e`  |
| 466    | No file              | `d72a257aaa0e`  |
| 457    | No file              | `d72a257aaa0e`  |
| 452    | No file              | `d72a257aaa0e`  |
| 449    | No file              | `d72a257aaa0e`  |
| 435    | No file              | `d72a257aaa0e`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                      |
| ---------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `formoffset.dbss`            | Optional | `index -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a listed character without a row shows as plain text   |
| `languagedata_en.loc`        | Optional | Names of the listed characters, LOC type 6                                                |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 31 bytes + icon texts + character keys)

| Offset                       | Type                     | Field               | Notes                                                                                      |
| ---------------------------- | ------------------------ | ------------------- | ------------------------------------------------------------------------------------------ |
| `+0x00`                      | u16                      | index               | Row key: the form                                                                          |
| `+0x02`                      | u16                      | index_dup           | Equal to `index` on every row; the offset index points here                               |
| `+0x04`                      | u8                       | type                | `gc::FormType`: `0` horse, `1` the enum count, where the sheet leaves it blank; see Form Types |
| `+0x05`                      | u32                      | action_index        | Action chart index of the look; `0` on 48 rows (client 3482)                               |
| `+0x09`                      | u16                      | tier                | Horse tier `1` to `9`; `0` on 72 rows (client 3482)                                         |
| `+0x0B`                      | str16                    | icon_1              | Stable icon under `ui_texture/` (`New_UI_Common_forLua\Window\Stable\Horse_01.dds`); empty on form `9` |
| `icon_1+0x00`                | str16                    | icon_2              | Second icon: `UI_Main_Mercenary_Icon_Horse.dds` on 295 rows, the goat icon on form `33`, empty on form `9` (client 3482) |
| `icon_2+0x00`                | u32                      | character_key_count | Number of `character_keys`; `0` on 295 of 297 rows (client 3482)                           |
| `icon_2+0x04`                | u16[character_key_count] | character_keys      | `characterstatic.dbss` characters that can take this form                                 |

The rows are in no key order; client 3482 opens with 239, 238, 237.

### `formoffset.dbss`

Bare offset table into `form.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                        |
| ------- | ----------------- | ----- | ---------------------------- |
| `+0x00` | u32               | count | Equals the `form.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row               |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u16  | index       | Key of the row it points at             |
| `+0x02` | u32  | data_offset | Row start + 2, at `index_dup`           |
| `+0x06` | u32  | data_size   | The row less its leading `index`        |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on clients 1784 and 3482 every index row points at
the row whose `index` is its key.

## Layout 1

The row has no character key list. Only the Row differs from Layout 2.

### Row (variable: 27 bytes + icon texts)

| Offset   | Type  | Field        | Notes                          |
| -------- | ----- | ------------ | ------------------------------ |
| `+0x00`  | u16   | index        | Row key: the form              |
| `+0x02`  | u16   | index_dup    | Equal to `index` on every row  |
| `+0x04`  | u8    | type         | `0` horse, `1` the enum count  |
| `+0x05`  | u32   | action_index | Action chart index of the look |
| `+0x09`  | u16   | tier         | Horse tier                     |
| `+0x0B`  | str16 | icon_1       | Stable icon                    |
| `icon_1+0x00` | str16 | icon_2  | Second icon                    |

## Form Types

The 2016 client's `gc::FormType` (u8) has two values. The `Form_Table`
sheet leaves `Type` blank on 166 rows; the client file holds `1` there.

| Value | Name              | Rows (client 3482) |
| ----- | ----------------- | ------------------ |
| 0     | `eFormType_Horse` | 115                |
| 1     | `eFormType_Count` | 182                |

## Field Names

The 2016 `gc::FormStaticStatus` holds `_index` (u16), `_type`
(`gc::FormType`, u8), `_actionIndex` (u32), `_tier` (u16), `_icon1` and
`_icon2` in this order, the members of Layout 1 packed. The `Form_Table`
sheet of a private server's `DataSheets.bexcel` on client 1784 has the
columns `Index`, `Type`, `ActionIndex`, `Tier`, `IconImageFile1` and
`IconImageFile2`, 274 rows.

| Field        | Column           | Same value (client 1784) | Same value (client 3482) |
| ------------ | ---------------- | ------------------------ | ------------------------ |
| index        | `Index`          | 272 of 272               | 274 of 274               |
| type         | `Type`           | 272 of 272, blank as `1` | 274 of 274, blank as `1` |
| action_index | `ActionIndex`    | 272 of 272               | 274 of 274               |
| tier         | `Tier`           | 272 of 272               | 269 of 274               |
| icon_1       | `IconImageFile1` | 272 of 272               | 274 of 274               |
| icon_2       | `IconImageFile2` | 272 of 272               | 274 of 274               |

On client 3482 forms `265` to `269` hold tier `9` where the sheet has `4`.
The sheet's `#Grade` note column is not compiled.

`character_keys` has no sheet column. The client Lua (3482) looks forms up
by character: `panel_dialog_servant_fantasyskin_all_1.luac` asks
`formManager:getFormCountByCharacterKey(key)` and
`formManager:getFormByCharacterKey(key, 0)` for the horse in the fantasy
skin window, and the three keys the file lists (`31539`, `31558`, `31562`)
are all Mythical Arduanatt (LOC type 6).

## Notes

- The look change window (`panel_dialog_servantlookchange_all_2.luac`)
  reads forms per tier with `formManager:getFormTierSize(tier)` and
  `formManager:getFormTierStaticWrapper(tier, i)`, and compares
  `formInfo:getActionIndex()` with the horse's own action index. The horse
  upgrade window (`panel_window_servantupgrade_1.luac`) shows
  `ToClient_FormStaticStatusWrapper(characterKey):getIcon1()`.
- On client 3482 forms `260` (`31562`) and `275` (`31539`, `31558`) list
  characters; the other 295 rows have an empty list.
- Form `9` has empty icons on clients 1784 and 3482.

## Open Questions

### What Type 0 Changes

All 115 forms with `type` `0` (`eFormType_Horse`) use a `Horse_*.dds`
stable icon, but so do 119 of the 182 forms with `type` `1`, the value the
sheet's blank compiles to. No client Lua (3482) reads the type, so which
window or rule tells the two horse groups apart is open.
