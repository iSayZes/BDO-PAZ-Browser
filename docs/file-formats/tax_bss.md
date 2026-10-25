# `tax.bss` Format

## Purpose

The tax bounds of each territory: for each of eight tax types, a minimum
and a maximum rate or price and a system rate.
One 100-byte row per territory; client 3482 has 14 rows, territory keys
`13` down to `0`, all with the same values.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File      | Bytes | Records         | Row bytes |
| ------ | ------------- | --------- | ----- | --------------- | --------- |
| 1      | 805 and later | `tax.bss` | 1,420 | 112 Tax, 14 Row | 12        |

| Layout | File      | Known            | Unknown    |
| ------ | --------- | ---------------- | ---------- |
| 1      | `tax.bss` | 1,420 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `b4d58bd3b7dc`  |
| 3482   | Layout 1             | `b4d58bd3b7dc`  |
| 3474   | Layout 1             | `b4d58bd3b7dc`  |
| 3473   | Layout 1             | `b4d58bd3b7dc`  |
| 3464   | Layout 1             | `b4d58bd3b7dc`  |
| 3458   | Layout 1             | `b4d58bd3b7dc`  |
| 3454   | Layout 1             | `b4d58bd3b7dc`  |
| 3444   | Layout 1             | `b4d58bd3b7dc`  |
| 3435   | Layout 1             | `b4d58bd3b7dc`  |
| 3426   | Layout 1             | `b4d58bd3b7dc`  |
| 3418   | Layout 1             | `b4d58bd3b7dc`  |
| 3412   | Layout 1             | `b4d58bd3b7dc`  |
| 3402   | Layout 1             | `b4d58bd3b7dc`  |
| 3396   | Layout 1             | `b4d58bd3b7dc`  |
| 3387   | Layout 1             | `b4d58bd3b7dc`  |
| 3381   | Layout 1             | `b4d58bd3b7dc`  |
| 3373   | Layout 1             | `b4d58bd3b7dc`  |
| 3364   | Layout 1             | `b4d58bd3b7dc`  |
| 3356   | Layout 1             | `b4d58bd3b7dc`  |
| 3349   | Layout 1             | `b4d58bd3b7dc`  |
| 3342   | Layout 1             | `b4d58bd3b7dc`  |
| 3335   | Layout 1             | `b4d58bd3b7dc`  |
| 3326   | Layout 1             | `b4d58bd3b7dc`  |
| 3321   | Layout 1             | `b4d58bd3b7dc`  |
| 3314   | Layout 1             | `b4d58bd3b7dc`  |
| 3303   | Layout 1             | `b4d58bd3b7dc`  |
| 3302   | Layout 1             | `b4d58bd3b7dc`  |
| 3293   | Layout 1             | `b4d58bd3b7dc`  |
| 3283   | Layout 1             | `b4d58bd3b7dc`  |
| 3275   | Layout 1             | `b4d58bd3b7dc`  |
| 3267   | Layout 1             | `b4d58bd3b7dc`  |
| 3258   | Layout 1             | `b4d58bd3b7dc`  |
| 3251   | Layout 1             | `b4d58bd3b7dc`  |
| 3242   | Layout 1             | `b4d58bd3b7dc`  |
| 3235   | Layout 1             | `b4d58bd3b7dc`  |
| 3229   | Layout 1             | `b4d58bd3b7dc`  |
| 3212   | Layout 1             | `b4d58bd3b7dc`  |
| 3203   | Layout 1             | `b4d58bd3b7dc`  |
| 3193   | Layout 1             | `b4d58bd3b7dc`  |
| 3186   | Layout 1             | `b4d58bd3b7dc`  |
| 3177   | Layout 1             | `b4d58bd3b7dc`  |
| 3169   | Layout 1             | `b4d58bd3b7dc`  |
| 3158   | Layout 1             | `b4d58bd3b7dc`  |
| 3151   | Layout 1             | `b4d58bd3b7dc`  |
| 3144   | Layout 1             | `b4d58bd3b7dc`  |
| 3133   | Layout 1             | `b4d58bd3b7dc`  |
| 3125   | Layout 1             | `b4d58bd3b7dc`  |
| 3118   | Layout 1             | `b4d58bd3b7dc`  |
| 3111   | Layout 1             | `b4d58bd3b7dc`  |
| 3103   | Layout 1             | `b4d58bd3b7dc`  |
| 3095   | Layout 1             | `b4d58bd3b7dc`  |
| 3086   | Layout 1             | `b4d58bd3b7dc`  |
| 3072   | Layout 1             | `b4d58bd3b7dc`  |
| 3062   | Layout 1             | `b4d58bd3b7dc`  |
| 3052   | Layout 1             | `b4d58bd3b7dc`  |
| 3045   | Layout 1             | `b4d58bd3b7dc`  |
| 3037   | Layout 1             | `b4d58bd3b7dc`  |
| 3030   | Layout 1             | `b4d58bd3b7dc`  |
| 3021   | Layout 1             | `b4d58bd3b7dc`  |
| 3012   | Layout 1             | `b4d58bd3b7dc`  |
| 3002   | Layout 1             | `b4d58bd3b7dc`  |
| 2995   | Layout 1             | `b4d58bd3b7dc`  |
| 2987   | Layout 1             | `b4d58bd3b7dc`  |
| 2978   | Layout 1             | `b4d58bd3b7dc`  |
| 2970   | Layout 1             | `b4d58bd3b7dc`  |
| 2959   | Layout 1             | `b4d58bd3b7dc`  |
| 2951   | Layout 1             | `b4d58bd3b7dc`  |
| 2942   | Layout 1             | `b4d58bd3b7dc`  |
| 2935   | Layout 1             | `b4d58bd3b7dc`  |
| 2932   | Layout 1             | `b4d58bd3b7dc`  |
| 2923   | Layout 1             | `b4d58bd3b7dc`  |
| 2919   | Layout 1             | `b4d58bd3b7dc`  |
| 2907   | Layout 1             | `b4d58bd3b7dc`  |
| 2900   | Layout 1             | `b4d58bd3b7dc`  |
| 2891   | Layout 1             | `b4d58bd3b7dc`  |
| 2882   | Layout 1             | `b4d58bd3b7dc`  |
| 2872   | Layout 1             | `b4d58bd3b7dc`  |
| 2863   | Layout 1             | `b4d58bd3b7dc`  |
| 2855   | Layout 1             | `b4d58bd3b7dc`  |
| 2849   | Layout 1             | `b4d58bd3b7dc`  |
| 2844   | Layout 1             | `b4d58bd3b7dc`  |
| 2834   | Layout 1             | `b4d58bd3b7dc`  |
| 2825   | Layout 1             | `b4d58bd3b7dc`  |
| 2819   | Layout 1             | `b4d58bd3b7dc`  |
| 2811   | Layout 1             | `b4d58bd3b7dc`  |
| 2803   | Layout 1             | `b4d58bd3b7dc`  |
| 2794   | Layout 1             | `b4d58bd3b7dc`  |
| 2783   | Layout 1             | `b4d58bd3b7dc`  |
| 2774   | Layout 1             | `b4d58bd3b7dc`  |
| 2765   | Layout 1             | `b4d58bd3b7dc`  |
| 2756   | Layout 1             | `b4d58bd3b7dc`  |
| 2750   | Layout 1             | `b4d58bd3b7dc`  |
| 2743   | Layout 1             | `b4d58bd3b7dc`  |
| 2736   | Layout 1             | `b4d58bd3b7dc`  |
| 2726   | Layout 1             | `b4d58bd3b7dc`  |
| 2717   | Layout 1             | `b4d58bd3b7dc`  |
| 2709   | Layout 1             | `b4d58bd3b7dc`  |
| 2703   | Layout 1             | `b4d58bd3b7dc`  |
| 2695   | Layout 1             | `b4d58bd3b7dc`  |
| 2684   | Layout 1             | `b4d58bd3b7dc`  |
| 2672   | Layout 1             | `b4d58bd3b7dc`  |
| 2665   | Layout 1             | `b4d58bd3b7dc`  |
| 2657   | Layout 1             | `b4d58bd3b7dc`  |
| 2649   | Layout 1             | `b4d58bd3b7dc`  |
| 2644   | Layout 1             | `b4d58bd3b7dc`  |
| 2637   | Layout 1             | `b4d58bd3b7dc`  |
| 2629   | Layout 1             | `b4d58bd3b7dc`  |
| 2619   | Layout 1             | `b4d58bd3b7dc`  |
| 2612   | Layout 1             | `b4d58bd3b7dc`  |
| 2606   | Layout 1             | `b4d58bd3b7dc`  |
| 2602   | Layout 1             | `b4d58bd3b7dc`  |
| 2601   | Layout 1             | `b4d58bd3b7dc`  |
| 2592   | Layout 1             | `b4d58bd3b7dc`  |
| 2583   | Layout 1             | `b4d58bd3b7dc`  |
| 2575   | Layout 1             | `b4d58bd3b7dc`  |
| 2567   | Layout 1             | `b4d58bd3b7dc`  |
| 2560   | Layout 1             | `b4d58bd3b7dc`  |
| 2553   | Layout 1             | `b4d58bd3b7dc`  |
| 2545   | Layout 1             | `b4d58bd3b7dc`  |
| 2538   | Layout 1             | `b4d58bd3b7dc`  |
| 2529   | Layout 1             | `b4d58bd3b7dc`  |
| 2519   | Layout 1             | `b4d58bd3b7dc`  |
| 2513   | Layout 1             | `b4d58bd3b7dc`  |
| 2510   | Layout 1             | `b4d58bd3b7dc`  |
| 2507   | Layout 1             | `b4d58bd3b7dc`  |
| 2503   | Layout 1             | `b4d58bd3b7dc`  |
| 2498   | Layout 1             | `b4d58bd3b7dc`  |
| 2492   | Layout 1             | `b4d58bd3b7dc`  |
| 2487   | Layout 1             | `b4d58bd3b7dc`  |
| 2480   | Layout 1             | `b4d58bd3b7dc`  |
| 2474   | Layout 1             | `b4d58bd3b7dc`  |
| 2468   | Layout 1             | `b4d58bd3b7dc`  |
| 2460   | Layout 1             | `b4d58bd3b7dc`  |
| 2453   | Layout 1             | `b4d58bd3b7dc`  |
| 2444   | Layout 1             | `b4d58bd3b7dc`  |
| 2438   | Layout 1             | `b4d58bd3b7dc`  |
| 2434   | Layout 1             | `b4d58bd3b7dc`  |
| 2429   | Layout 1             | `b4d58bd3b7dc`  |
| 2421   | Layout 1             | `b4d58bd3b7dc`  |
| 2414   | Layout 1             | `b4d58bd3b7dc`  |
| 2407   | Layout 1             | `b4d58bd3b7dc`  |
| 2401   | Layout 1             | `b4d58bd3b7dc`  |
| 2397   | Layout 1             | `b4d58bd3b7dc`  |
| 2393   | Layout 1             | `b4d58bd3b7dc`  |
| 2384   | Layout 1             | `b4d58bd3b7dc`  |
| 2378   | Layout 1             | `b4d58bd3b7dc`  |
| 2372   | Layout 1             | `b4d58bd3b7dc`  |
| 2358   | Layout 1             | `b4d58bd3b7dc`  |
| 2352   | Layout 1             | `b4d58bd3b7dc`  |
| 2347   | Layout 1             | `b4d58bd3b7dc`  |
| 2343   | Layout 1             | `b4d58bd3b7dc`  |
| 2335   | Layout 1             | `b4d58bd3b7dc`  |
| 2327   | Layout 1             | `b4d58bd3b7dc`  |
| 2324   | Layout 1             | `b4d58bd3b7dc`  |
| 2319   | Layout 1             | `b4d58bd3b7dc`  |
| 2313   | Layout 1             | `b4d58bd3b7dc`  |
| 2308   | Layout 1             | `b4d58bd3b7dc`  |
| 2302   | Layout 1             | `b4d58bd3b7dc`  |
| 2295   | Layout 1             | `b4d58bd3b7dc`  |
| 2290   | Layout 1             | `b4d58bd3b7dc`  |
| 2284   | Layout 1             | `b4d58bd3b7dc`  |
| 2276   | Layout 1             | `b4d58bd3b7dc`  |
| 2269   | Layout 1             | `b4d58bd3b7dc`  |
| 2259   | Layout 1             | `b4d58bd3b7dc`  |
| 2250   | Layout 1             | `b4d58bd3b7dc`  |
| 2243   | Layout 1             | `b4d58bd3b7dc`  |
| 2235   | Layout 1             | `b4d58bd3b7dc`  |
| 2229   | Layout 1             | `b4d58bd3b7dc`  |
| 2224   | Layout 1             | `b4d58bd3b7dc`  |
| 2218   | Layout 1             | `b4d58bd3b7dc`  |
| 2215   | Layout 1             | `b4d58bd3b7dc`  |
| 2207   | Layout 1             | `b4d58bd3b7dc`  |
| 2203   | Layout 1             | `b4d58bd3b7dc`  |
| 2196   | Layout 1             | `b4d58bd3b7dc`  |
| 2192   | Layout 1             | `b4d58bd3b7dc`  |
| 2189   | Layout 1             | `b4d58bd3b7dc`  |
| 2183   | Layout 1             | `b4d58bd3b7dc`  |
| 2179   | Layout 1             | `b4d58bd3b7dc`  |
| 2171   | Layout 1             | `b4d58bd3b7dc`  |
| 2163   | Layout 1             | `b4d58bd3b7dc`  |
| 2156   | Layout 1             | `b4d58bd3b7dc`  |
| 2151   | Layout 1             | `b4d58bd3b7dc`  |
| 2147   | Layout 1             | `b4d58bd3b7dc`  |
| 2142   | Layout 1             | `b4d58bd3b7dc`  |
| 2138   | Layout 1             | `b4d58bd3b7dc`  |
| 2134   | Layout 1             | `b4d58bd3b7dc`  |
| 2130   | Layout 1             | `b4d58bd3b7dc`  |
| 2122   | Layout 1             | `b4d58bd3b7dc`  |
| 2107   | Layout 1             | `b4d58bd3b7dc`  |
| 2098   | Layout 1             | `b4d58bd3b7dc`  |
| 2089   | Layout 1             | `b4d58bd3b7dc`  |
| 2081   | Layout 1             | `b4d58bd3b7dc`  |
| 2073   | Layout 1             | `b4d58bd3b7dc`  |
| 2067   | Layout 1             | `b4d58bd3b7dc`  |
| 2063   | Layout 1             | `b4d58bd3b7dc`  |
| 2059   | Layout 1             | `b4d58bd3b7dc`  |
| 2052   | Layout 1             | `b4d58bd3b7dc`  |
| 2044   | Layout 1             | `b4d58bd3b7dc`  |
| 2039   | Layout 1             | `b4d58bd3b7dc`  |
| 2032   | Layout 1             | `b4d58bd3b7dc`  |
| 2025   | Layout 1             | `b4d58bd3b7dc`  |
| 2011   | Layout 1             | `b4d58bd3b7dc`  |
| 2005   | Layout 1             | `b4d58bd3b7dc`  |
| 2000   | Layout 1             | `b4d58bd3b7dc`  |
| 1996   | Layout 1             | `b4d58bd3b7dc`  |
| 1991   | Layout 1             | `b4d58bd3b7dc`  |
| 1985   | Layout 1             | `b4d58bd3b7dc`  |
| 1980   | Layout 1             | `b4d58bd3b7dc`  |
| 1969   | Layout 1             | `b4d58bd3b7dc`  |
| 1964   | Layout 1             | `b4d58bd3b7dc`  |
| 1958   | Layout 1             | `b4d58bd3b7dc`  |
| 1950   | Layout 1             | `b4d58bd3b7dc`  |
| 1945   | Layout 1             | `b4d58bd3b7dc`  |
| 1937   | Layout 1             | `b4d58bd3b7dc`  |
| 1933   | Layout 1             | `b4d58bd3b7dc`  |
| 1927   | Layout 1             | `b4d58bd3b7dc`  |
| 1921   | Layout 1             | `b4d58bd3b7dc`  |
| 1914   | Layout 1             | `b4d58bd3b7dc`  |
| 1908   | Layout 1             | `b4d58bd3b7dc`  |
| 1897   | Layout 1             | `b4d58bd3b7dc`  |
| 1892   | Layout 1             | `b4d58bd3b7dc`  |
| 1886   | Layout 1             | `b4d58bd3b7dc`  |
| 1881   | Layout 1             | `b4d58bd3b7dc`  |
| 1871   | Layout 1             | `b4d58bd3b7dc`  |
| 1866   | Layout 1             | `b4d58bd3b7dc`  |
| 1862   | Layout 1             | `b4d58bd3b7dc`  |
| 1854   | Layout 1             | `b4d58bd3b7dc`  |
| 1846   | Layout 1             | `b4d58bd3b7dc`  |
| 1838   | Layout 1             | `b4d58bd3b7dc`  |
| 1832   | Layout 1             | `b4d58bd3b7dc`  |
| 1826   | Layout 1             | `b4d58bd3b7dc`  |
| 1822   | Layout 1             | `b4d58bd3b7dc`  |
| 1818   | Layout 1             | `b4d58bd3b7dc`  |
| 1804   | Layout 1             | `b4d58bd3b7dc`  |
| 1794   | Layout 1             | `b4d58bd3b7dc`  |
| 1790   | Layout 1             | `b4d58bd3b7dc`  |
| 1784   | Layout 1             | `b4d58bd3b7dc`  |
| 1774   | Layout 1             | `b4d58bd3b7dc`  |
| 1771   | Layout 1             | `b4d58bd3b7dc`  |
| 1762   | Layout 1             | `b4d58bd3b7dc`  |
| 1759   | Layout 1             | `b4d58bd3b7dc`  |
| 1754   | Layout 1             | `b4d58bd3b7dc`  |
| 1749   | Layout 1             | `b4d58bd3b7dc`  |
| 1743   | Layout 1             | `b4d58bd3b7dc`  |
| 1737   | Layout 1             | `b4d58bd3b7dc`  |
| 1731   | Layout 1             | `b4d58bd3b7dc`  |
| 1725   | Layout 1             | `b4d58bd3b7dc`  |
| 1717   | Layout 1             | `b4d58bd3b7dc`  |
| 1710   | Layout 1             | `b4d58bd3b7dc`  |
| 1704   | Layout 1             | `b4d58bd3b7dc`  |
| 1698   | Layout 1             | `b4d58bd3b7dc`  |
| 1690   | Layout 1             | `b4d58bd3b7dc`  |
| 1685   | Layout 1             | `b4d58bd3b7dc`  |
| 1680   | Layout 1             | `b4d58bd3b7dc`  |
| 1674   | Layout 1             | `b4d58bd3b7dc`  |
| 1668   | Layout 1             | `b4d58bd3b7dc`  |
| 1659   | Layout 1             | `b4d58bd3b7dc`  |
| 1649   | Layout 1             | `b4d58bd3b7dc`  |
| 1642   | Layout 1             | `b4d58bd3b7dc`  |
| 1636   | Layout 1             | `b4d58bd3b7dc`  |
| 1628   | Layout 1             | `b4d58bd3b7dc`  |
| 1622   | Layout 1             | `b4d58bd3b7dc`  |
| 1614   | Layout 1             | `b4d58bd3b7dc`  |
| 1608   | Layout 1             | `b4d58bd3b7dc`  |
| 1602   | Layout 1             | `b4d58bd3b7dc`  |
| 1598   | Layout 1             | `b4d58bd3b7dc`  |
| 1594   | Layout 1             | `b4d58bd3b7dc`  |
| 1590   | Layout 1             | `b4d58bd3b7dc`  |
| 1587   | Layout 1             | `b4d58bd3b7dc`  |
| 1584   | Layout 1             | `b4d58bd3b7dc`  |
| 1579   | Layout 1             | `b4d58bd3b7dc`  |
| 1572   | Layout 1             | `b4d58bd3b7dc`  |
| 1565   | Layout 1             | `b4d58bd3b7dc`  |
| 1559   | Layout 1             | `b4d58bd3b7dc`  |
| 1554   | Layout 1             | `b4d58bd3b7dc`  |
| 1547   | Layout 1             | `b4d58bd3b7dc`  |
| 1537   | Layout 1             | `b4d58bd3b7dc`  |
| 1529   | Layout 1             | `b4d58bd3b7dc`  |
| 1524   | Layout 1             | `b4d58bd3b7dc`  |
| 1519   | Layout 1             | `b4d58bd3b7dc`  |
| 1509   | Layout 1             | `b4d58bd3b7dc`  |
| 1506   | Layout 1             | `b4d58bd3b7dc`  |
| 1504   | Layout 1             | `b4d58bd3b7dc`  |
| 1500   | Layout 1             | `b4d58bd3b7dc`  |
| 1493   | Layout 1             | `b4d58bd3b7dc`  |
| 1489   | Layout 1             | `b4d58bd3b7dc`  |
| 1485   | Layout 1             | `b4d58bd3b7dc`  |
| 1481   | Layout 1             | `b4d58bd3b7dc`  |
| 1474   | Layout 1             | `b4d58bd3b7dc`  |
| 1466   | Layout 1             | `b4d58bd3b7dc`  |
| 1462   | Layout 1             | `b4d58bd3b7dc`  |
| 1459   | Layout 1             | `b4d58bd3b7dc`  |
| 1453   | Layout 1             | `b4d58bd3b7dc`  |
| 1450   | Layout 1             | `b4d58bd3b7dc`  |
| 1445   | Layout 1             | `b4d58bd3b7dc`  |
| 1439   | Layout 1             | `b4d58bd3b7dc`  |
| 1433   | Layout 1             | `b4d58bd3b7dc`  |
| 1430   | Layout 1             | `b4d58bd3b7dc`  |
| 1426   | Layout 1             | `b4d58bd3b7dc`  |
| 1421   | Layout 1             | `b4d58bd3b7dc`  |
| 1417   | Layout 1             | `b4d58bd3b7dc`  |
| 1416   | Layout 1             | `b4d58bd3b7dc`  |
| 1409   | Layout 1             | `b4d58bd3b7dc`  |
| 1405   | Layout 1             | `b4d58bd3b7dc`  |
| 1401   | Layout 1             | `b4d58bd3b7dc`  |
| 1396   | Layout 1             | `b4d58bd3b7dc`  |
| 1391   | Layout 1             | `b4d58bd3b7dc`  |
| 1390   | Layout 1             | `b4d58bd3b7dc`  |
| 1386   | Layout 1             | `b4d58bd3b7dc`  |
| 1381   | Layout 1             | `b4d58bd3b7dc`  |
| 1379   | Layout 1             | `b4d58bd3b7dc`  |
| 1372   | Layout 1             | `b4d58bd3b7dc`  |
| 1366   | Layout 1             | `b4d58bd3b7dc`  |
| 1364   | Layout 1             | `b4d58bd3b7dc`  |
| 1363   | Layout 1             | `b4d58bd3b7dc`  |
| 1360   | Layout 1             | `b4d58bd3b7dc`  |
| 1358   | Layout 1             | `b4d58bd3b7dc`  |
| 1355   | Layout 1             | `b4d58bd3b7dc`  |
| 1351   | Layout 1             | `b4d58bd3b7dc`  |
| 1348   | Layout 1             | `b4d58bd3b7dc`  |
| 1346   | Layout 1             | `b4d58bd3b7dc`  |
| 1341   | Layout 1             | `b4d58bd3b7dc`  |
| 1340   | Layout 1             | `b4d58bd3b7dc`  |
| 1338   | Layout 1             | `b4d58bd3b7dc`  |
| 1335   | Layout 1             | `b4d58bd3b7dc`  |
| 1333   | Layout 1             | `b4d58bd3b7dc`  |
| 1329   | Layout 1             | `b4d58bd3b7dc`  |
| 1327   | Layout 1             | `b4d58bd3b7dc`  |
| 1324   | Layout 1             | `b4d58bd3b7dc`  |
| 1321   | Layout 1             | `b4d58bd3b7dc`  |
| 1319   | Layout 1             | `b4d58bd3b7dc`  |
| 1318   | Layout 1             | `b4d58bd3b7dc`  |
| 1316   | Layout 1             | `b4d58bd3b7dc`  |
| 1313   | Layout 1             | `b4d58bd3b7dc`  |
| 1311   | Layout 1             | `b4d58bd3b7dc`  |
| 1309   | Layout 1             | `b4d58bd3b7dc`  |
| 1304   | Layout 1             | `b4d58bd3b7dc`  |
| 1292   | Layout 1             | `b4d58bd3b7dc`  |
| 1286   | Layout 1             | `b4d58bd3b7dc`  |
| 1280   | Layout 1             | `b4d58bd3b7dc`  |
| 1276   | Layout 1             | `b4d58bd3b7dc`  |
| 1267   | Layout 1             | `b4d58bd3b7dc`  |
| 1261   | Layout 1             | `b4d58bd3b7dc`  |
| 1256   | Layout 1             | `b4d58bd3b7dc`  |
| 1250   | Layout 1             | `b4d58bd3b7dc`  |
| 1246   | Layout 1             | `b4d58bd3b7dc`  |
| 1239   | Layout 1             | `b4d58bd3b7dc`  |
| 1230   | Layout 1             | `b4d58bd3b7dc`  |
| 1226   | Layout 1             | `b4d58bd3b7dc`  |
| 1220   | Layout 1             | `b4d58bd3b7dc`  |
| 1217   | Layout 1             | `b4d58bd3b7dc`  |
| 1211   | Layout 1             | `b4d58bd3b7dc`  |
| 1210   | Layout 1             | `b4d58bd3b7dc`  |
| 1208   | Layout 1             | `b4d58bd3b7dc`  |
| 1203   | Layout 1             | `b4d58bd3b7dc`  |
| 1197   | Layout 1             | `b4d58bd3b7dc`  |
| 1194   | Layout 1             | `b4d58bd3b7dc`  |
| 1192   | Layout 1             | `b4d58bd3b7dc`  |
| 1187   | Layout 1             | `b4d58bd3b7dc`  |
| 1183   | Layout 1             | `b4d58bd3b7dc`  |
| 1177   | Layout 1             | `b4d58bd3b7dc`  |
| 1173   | Layout 1             | `b4d58bd3b7dc`  |
| 1167   | Layout 1             | `b4d58bd3b7dc`  |
| 1164   | Layout 1             | `b4d58bd3b7dc`  |
| 1156   | Layout 1             | `b4d58bd3b7dc`  |
| 1149   | Layout 1             | `b4d58bd3b7dc`  |
| 1144   | Layout 1             | `b4d58bd3b7dc`  |
| 1137   | Layout 1             | `b4d58bd3b7dc`  |
| 1132   | Layout 1             | `b4d58bd3b7dc`  |
| 1127   | Layout 1             | `b4d58bd3b7dc`  |
| 1122   | Layout 1             | `b4d58bd3b7dc`  |
| 1118   | Layout 1             | `b4d58bd3b7dc`  |
| 1114   | Layout 1             | `b4d58bd3b7dc`  |
| 1109   | Layout 1             | `b4d58bd3b7dc`  |
| 1102   | No file              | `b4d58bd3b7dc`  |
| 1096   | No file              | `b4d58bd3b7dc`  |
| 1088   | No file              | `b4d58bd3b7dc`  |
| 1081   | No file              | `b4d58bd3b7dc`  |
| 1076   | No file              | `b4d58bd3b7dc`  |
| 1069   | No file              | `b4d58bd3b7dc`  |
| 1064   | No file              | `b4d58bd3b7dc`  |
| 1058   | No file              | `b4d58bd3b7dc`  |
| 1051   | No file              | `b4d58bd3b7dc`  |
| 1044   | No file              | `b4d58bd3b7dc`  |
| 1036   | No file              | `b4d58bd3b7dc`  |
| 1026   | No file              | `b4d58bd3b7dc`  |
| 1016   | No file              | `b4d58bd3b7dc`  |
| 1009   | No file              | `b4d58bd3b7dc`  |
| 1005   | No file              | `b4d58bd3b7dc`  |
| 1000   | No file              | `b4d58bd3b7dc`  |
| 998    | No file              | `b4d58bd3b7dc`  |
| 990    | No file              | `b4d58bd3b7dc`  |
| 979    | No file              | `b4d58bd3b7dc`  |
| 972    | No file              | `b4d58bd3b7dc`  |
| 963    | No file              | `b4d58bd3b7dc`  |
| 955    | No file              | `b4d58bd3b7dc`  |
| 946    | No file              | `b4d58bd3b7dc`  |
| 938    | No file              | `b4d58bd3b7dc`  |
| 927    | No file              | `b4d58bd3b7dc`  |
| 911    | No file              | `b4d58bd3b7dc`  |
| 904    | No file              | `b4d58bd3b7dc`  |
| 899    | No file              | `b4d58bd3b7dc`  |
| 894    | No file              | `b4d58bd3b7dc`  |
| 885    | No file              | `b4d58bd3b7dc`  |
| 879    | No file              | `b4d58bd3b7dc`  |
| 872    | No file              | `b4d58bd3b7dc`  |
| 864    | No file              | `b4d58bd3b7dc`  |
| 855    | No file              | `b4d58bd3b7dc`  |
| 853    | No file              | `b4d58bd3b7dc`  |
| 845    | No file              | `b4d58bd3b7dc`  |
| 837    | No file              | `b4d58bd3b7dc`  |
| 829    | Layout 1             | `b4d58bd3b7dc`  |
| 822    | Layout 1             | `b4d58bd3b7dc`  |
| 814    | Layout 1             | `b4d58bd3b7dc`  |
| 805    | Layout 1             | `b4d58bd3b7dc`  |
| 794    | No documented layout | `b4d58bd3b7dc`  |
| 787    | No documented layout | `b4d58bd3b7dc`  |
| 780    | No documented layout | `b4d58bd3b7dc`  |
| 771    | No documented layout | `b4d58bd3b7dc`  |
| 760    | No documented layout | `b4d58bd3b7dc`  |
| 748    | No documented layout | `b4d58bd3b7dc`  |
| 741    | No documented layout | `b4d58bd3b7dc`  |
| 736    | No documented layout | `b4d58bd3b7dc`  |
| 731    | No documented layout | `b4d58bd3b7dc`  |
| 723    | No documented layout | `b4d58bd3b7dc`  |
| 711    | No documented layout | `b4d58bd3b7dc`  |
| 707    | No documented layout | `b4d58bd3b7dc`  |
| 697    | No documented layout | `b4d58bd3b7dc`  |
| 689    | No documented layout | `b4d58bd3b7dc`  |
| 683    | No documented layout | `b4d58bd3b7dc`  |
| 678    | No documented layout | `b4d58bd3b7dc`  |
| 670    | No documented layout | `b4d58bd3b7dc`  |
| 661    | No documented layout | `b4d58bd3b7dc`  |
| 656    | No documented layout | `b4d58bd3b7dc`  |
| 652    | No documented layout | `b4d58bd3b7dc`  |
| 643    | No documented layout | `b4d58bd3b7dc`  |
| 637    | No documented layout | `b4d58bd3b7dc`  |
| 630    | No documented layout | `b4d58bd3b7dc`  |
| 627    | No documented layout | `b4d58bd3b7dc`  |
| 621    | No documented layout | `b4d58bd3b7dc`  |
| 617    | No documented layout | `b4d58bd3b7dc`  |
| 615    | No documented layout | `b4d58bd3b7dc`  |
| 606    | No documented layout | `b4d58bd3b7dc`  |
| 599    | No documented layout | `b4d58bd3b7dc`  |
| 592    | No documented layout | `b4d58bd3b7dc`  |
| 586    | No documented layout | `b4d58bd3b7dc`  |
| 577    | No documented layout | `b4d58bd3b7dc`  |
| 569    | No documented layout | `b4d58bd3b7dc`  |
| 561    | No documented layout | `b4d58bd3b7dc`  |
| 554    | No documented layout | `b4d58bd3b7dc`  |
| 542    | No documented layout | `b4d58bd3b7dc`  |
| 532    | No documented layout | `b4d58bd3b7dc`  |
| 531    | No documented layout | `b4d58bd3b7dc`  |
| 526    | No documented layout | `b4d58bd3b7dc`  |
| 521    | No documented layout | `b4d58bd3b7dc`  |
| 517    | No documented layout | `b4d58bd3b7dc`  |
| 510    | No documented layout | `b4d58bd3b7dc`  |
| 508    | No documented layout | `b4d58bd3b7dc`  |
| 504    | No documented layout | `b4d58bd3b7dc`  |
| 497    | No documented layout | `b4d58bd3b7dc`  |
| 491    | No documented layout | `b4d58bd3b7dc`  |
| 485    | No documented layout | `b4d58bd3b7dc`  |
| 478    | No documented layout | `b4d58bd3b7dc`  |
| 472    | No documented layout | `b4d58bd3b7dc`  |
| 466    | No documented layout | `b4d58bd3b7dc`  |
| 457    | No documented layout | `b4d58bd3b7dc`  |
| 452    | No documented layout | `b4d58bd3b7dc`  |
| 449    | No documented layout | `b4d58bd3b7dc`  |
| 435    | No documented layout | `b4d58bd3b7dc`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows, one per territory             |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (100 bytes)

| Offset  | Type   | Field             | Notes                                                                 |
| ------- | ------ | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | i16    | territory_key     | `territoryinfo.bss` key, LOC type 12 name; the key the table is read by |
| `+0x02` | i16    | territory_key_dup | Equals `territory_key` on every row; the 2016 struct's `_key`         |
| `+0x04` | Tax[8] | taxes             | One per tax type, in `TaxType` order; see Tax Types                   |

### Tax (12 bytes)

| Offset  | Type | Field                | Notes                                                     |
| ------- | ---- | -------------------- | --------------------------------------------------------- |
| `+0x00` | i32  | min_percent_or_price | `0` on every row of client 3482                           |
| `+0x04` | i32  | max_percent_or_price | `100000`, or `500` for tax type 4                         |
| `+0x08` | i32  | system_percent       | `0`, `200`, `250000` or `300000` by tax type              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Tax Types

The index of a `Tax` in `taxes`. Names 0 to 5 are `CppEnums.TaxType` in
`global_define_cpp_enum.luac` (client 3482), which ends with
`eTaxType_Count = 6`; 6 and 7 come from the 2016 `gc::TaxType`, which has
eight types and calls 1 `eTaxTypeBuyItemFromConsignment`. The values are
those of every territory on client 3482.

| Index | Name                          | `min_percent_or_price` | `max_percent_or_price` | `system_percent` |
| ----- | ----------------------------- | ---------------------- | ---------------------- | ---------------- |
| 0     | `eTaxType_BuyItemFromSystem`  | 0                      | 100000                 | 0                |
| 1     | `eTaxType_ReserveTemp`        | 0                      | 100000                 | 0                |
| 2     | `eTaxType_BuyHorseFromServantMarket` | 0               | 100000                 | 300000           |
| 3     | `eTaxType_BuyHorseFromServantMating` | 0               | 100000                 | 300000           |
| 4     | `eTaxType_DeliverItemByPublicWagon`  | 0               | 500                    | 200              |
| 5     | `eTaxTypeSellItemToItemMarket`       | 0               | 100000                 | 0                |
| 6     | `eTaxTypeSellWorkerToMarket` (2016)  | 0               | 100000                 | 300000           |
| 7     | `eTaxTypeSellPetInAuction` (2016)    | 0               | 100000                 | 250000           |

## Field Names

The 2016 `gc::TaxStaticStatus` (100 bytes) holds `gc::KeyType<short, -1>
_key`, two bytes of padding and `pa::Array<gc::TaxStaticStatus::value, 8>
_tax`; each `value` is `int _minPercentOrPrice`, `int _maxPercentOrPrice`
and `int _systemPercent`. The file packs the key the table is read by,
then `_key` in place of the padding, then the eight values.

The `Tax` sheet of a private server's `DataSheets.bexcel` on client 1784
has the columns `TerritoryKey`, `TaxType`, `MinPercentOrPrice`,
`MaxPercentOrPrice` and `SystemPercent`, one row per territory and tax
type. Its 80 rows (territories `0` to `9`, types `0` to `7`) match the
80 values of the client 1784 file (10 rows) by territory, type and value.

## Notes

- Client 1784 holds 10 rows (territories `9` down to `0`) with the same
  values; client 3482 adds territories `10` to `13`.
- The scale of the rates is not confirmed; the Lua reads the lord's set
  rate with `getTaxRateForFortress` and does not read this file.
- The tax handler (`_bss/tax/`) shows one row per territory and tax type,
  with the territory name and the tax type name.
