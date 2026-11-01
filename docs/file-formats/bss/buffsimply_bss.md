# `buffsimply.bss` Format

## Purpose

A compact copy of [`buff.dbss`](../dbss/buff_dbss.md): one fixed row per buff (32 bytes, 30 before client 3464)
with the buff ID, the icon path and `effect_name` as indices into a shared
string table, `is_shown`, `is_debuff`, `remove_on_dead` and the equipment the
buff needs. It holds no name, parameters,
duration or description, so it covers what the buff bar needs to draw a buff
and nothing about its effect.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes     | Records         | Row bytes |
| ------ | -------------- | ---------------- | --------- | --------------- | --------- |
| 2      | 3464 and later | `buffsimply.bss` | 1,490,698 | 44,724 Buff Row | 32        |
| 1      | 1311 to 3458   | `buffsimply.bss` | 1,398,407 | 44,645 Buff Row | 30        |

| Layout | File             | Known             | Unknown           |
| ------ | ---------------- | ----------------- | ----------------- |
| 2      | `buffsimply.bss` | 819,838 B (55.0%) | 670,860 B (45.0%) |
| 1      | `buffsimply.bss` | 728,732 B (52.1%) | 669,675 B (47.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `a359dd56a2d3`  |
| 3482   | Layout 2 | `a359dd56a2d3`  |
| 3474   | Layout 2 | `a359dd56a2d3`  |
| 3473   | Layout 2 | `a359dd56a2d3`  |
| 3464   | Layout 2 | `a359dd56a2d3`  |
| 3458   | Layout 1 | `a359dd56a2d3`  |
| 3454   | Layout 1 | `a359dd56a2d3`  |
| 3444   | Layout 1 | `a359dd56a2d3`  |
| 3435   | Layout 1 | `a359dd56a2d3`  |
| 3426   | Layout 1 | `a359dd56a2d3`  |
| 3418   | Layout 1 | `a359dd56a2d3`  |
| 3412   | Layout 1 | `a359dd56a2d3`  |
| 3402   | Layout 1 | `a359dd56a2d3`  |
| 3396   | Layout 1 | `a359dd56a2d3`  |
| 3387   | Layout 1 | `a359dd56a2d3`  |
| 3381   | Layout 1 | `a359dd56a2d3`  |
| 3373   | Layout 1 | `a359dd56a2d3`  |
| 3364   | Layout 1 | `a359dd56a2d3`  |
| 3356   | Layout 1 | `a359dd56a2d3`  |
| 3349   | Layout 1 | `a359dd56a2d3`  |
| 3342   | Layout 1 | `a359dd56a2d3`  |
| 3335   | Layout 1 | `a359dd56a2d3`  |
| 3326   | Layout 1 | `a359dd56a2d3`  |
| 3321   | Layout 1 | `a359dd56a2d3`  |
| 3314   | Layout 1 | `a359dd56a2d3`  |
| 3303   | Layout 1 | `a359dd56a2d3`  |
| 3302   | Layout 1 | `a359dd56a2d3`  |
| 3293   | Layout 1 | `a359dd56a2d3`  |
| 3283   | Layout 1 | `a359dd56a2d3`  |
| 3275   | Layout 1 | `a359dd56a2d3`  |
| 3267   | Layout 1 | `a359dd56a2d3`  |
| 3258   | Layout 1 | `a359dd56a2d3`  |
| 3251   | Layout 1 | `a359dd56a2d3`  |
| 3242   | Layout 1 | `a359dd56a2d3`  |
| 3235   | Layout 1 | `a359dd56a2d3`  |
| 3229   | Layout 1 | `a359dd56a2d3`  |
| 3212   | Layout 1 | `a359dd56a2d3`  |
| 3203   | Layout 1 | `a359dd56a2d3`  |
| 3193   | Layout 1 | `a359dd56a2d3`  |
| 3186   | Layout 1 | `a359dd56a2d3`  |
| 3177   | Layout 1 | `a359dd56a2d3`  |
| 3169   | Layout 1 | `a359dd56a2d3`  |
| 3158   | Layout 1 | `a359dd56a2d3`  |
| 3151   | Layout 1 | `a359dd56a2d3`  |
| 3144   | Layout 1 | `a359dd56a2d3`  |
| 3133   | Layout 1 | `a359dd56a2d3`  |
| 3125   | Layout 1 | `a359dd56a2d3`  |
| 3118   | Layout 1 | `a359dd56a2d3`  |
| 3111   | Layout 1 | `a359dd56a2d3`  |
| 3103   | Layout 1 | `a359dd56a2d3`  |
| 3095   | Layout 1 | `a359dd56a2d3`  |
| 3086   | Layout 1 | `a359dd56a2d3`  |
| 3072   | Layout 1 | `a359dd56a2d3`  |
| 3062   | Layout 1 | `a359dd56a2d3`  |
| 3052   | Layout 1 | `a359dd56a2d3`  |
| 3045   | Layout 1 | `a359dd56a2d3`  |
| 3037   | Layout 1 | `a359dd56a2d3`  |
| 3030   | Layout 1 | `a359dd56a2d3`  |
| 3021   | Layout 1 | `a359dd56a2d3`  |
| 3012   | Layout 1 | `a359dd56a2d3`  |
| 3002   | Layout 1 | `a359dd56a2d3`  |
| 2995   | Layout 1 | `a359dd56a2d3`  |
| 2987   | Layout 1 | `a359dd56a2d3`  |
| 2978   | Layout 1 | `a359dd56a2d3`  |
| 2970   | Layout 1 | `a359dd56a2d3`  |
| 2959   | Layout 1 | `a359dd56a2d3`  |
| 2951   | Layout 1 | `a359dd56a2d3`  |
| 2942   | Layout 1 | `a359dd56a2d3`  |
| 2935   | Layout 1 | `a359dd56a2d3`  |
| 2932   | Layout 1 | `a359dd56a2d3`  |
| 2923   | Layout 1 | `a359dd56a2d3`  |
| 2919   | Layout 1 | `a359dd56a2d3`  |
| 2907   | Layout 1 | `a359dd56a2d3`  |
| 2900   | Layout 1 | `a359dd56a2d3`  |
| 2891   | Layout 1 | `a359dd56a2d3`  |
| 2882   | Layout 1 | `a359dd56a2d3`  |
| 2872   | Layout 1 | `a359dd56a2d3`  |
| 2863   | Layout 1 | `a359dd56a2d3`  |
| 2855   | Layout 1 | `a359dd56a2d3`  |
| 2849   | Layout 1 | `a359dd56a2d3`  |
| 2844   | Layout 1 | `a359dd56a2d3`  |
| 2834   | Layout 1 | `a359dd56a2d3`  |
| 2825   | Layout 1 | `a359dd56a2d3`  |
| 2819   | Layout 1 | `a359dd56a2d3`  |
| 2811   | Layout 1 | `a359dd56a2d3`  |
| 2803   | Layout 1 | `a359dd56a2d3`  |
| 2794   | Layout 1 | `a359dd56a2d3`  |
| 2783   | Layout 1 | `a359dd56a2d3`  |
| 2774   | Layout 1 | `a359dd56a2d3`  |
| 2765   | Layout 1 | `a359dd56a2d3`  |
| 2756   | Layout 1 | `a359dd56a2d3`  |
| 2750   | Layout 1 | `a359dd56a2d3`  |
| 2743   | Layout 1 | `a359dd56a2d3`  |
| 2736   | Layout 1 | `a359dd56a2d3`  |
| 2726   | Layout 1 | `a359dd56a2d3`  |
| 2717   | Layout 1 | `a359dd56a2d3`  |
| 2709   | Layout 1 | `a359dd56a2d3`  |
| 2703   | Layout 1 | `a359dd56a2d3`  |
| 2695   | Layout 1 | `a359dd56a2d3`  |
| 2684   | Layout 1 | `a359dd56a2d3`  |
| 2672   | Layout 1 | `a359dd56a2d3`  |
| 2665   | Layout 1 | `a359dd56a2d3`  |
| 2657   | Layout 1 | `a359dd56a2d3`  |
| 2649   | Layout 1 | `a359dd56a2d3`  |
| 2644   | Layout 1 | `a359dd56a2d3`  |
| 2637   | Layout 1 | `a359dd56a2d3`  |
| 2629   | Layout 1 | `a359dd56a2d3`  |
| 2619   | Layout 1 | `a359dd56a2d3`  |
| 2612   | Layout 1 | `a359dd56a2d3`  |
| 2606   | Layout 1 | `a359dd56a2d3`  |
| 2602   | Layout 1 | `a359dd56a2d3`  |
| 2601   | Layout 1 | `a359dd56a2d3`  |
| 2592   | Layout 1 | `a359dd56a2d3`  |
| 2583   | Layout 1 | `a359dd56a2d3`  |
| 2575   | Layout 1 | `a359dd56a2d3`  |
| 2567   | Layout 1 | `a359dd56a2d3`  |
| 2560   | Layout 1 | `a359dd56a2d3`  |
| 2553   | Layout 1 | `a359dd56a2d3`  |
| 2545   | Layout 1 | `a359dd56a2d3`  |
| 2538   | Layout 1 | `a359dd56a2d3`  |
| 2529   | Layout 1 | `a359dd56a2d3`  |
| 2519   | Layout 1 | `a359dd56a2d3`  |
| 2513   | Layout 1 | `a359dd56a2d3`  |
| 2510   | Layout 1 | `a359dd56a2d3`  |
| 2507   | Layout 1 | `a359dd56a2d3`  |
| 2503   | Layout 1 | `a359dd56a2d3`  |
| 2498   | Layout 1 | `a359dd56a2d3`  |
| 2492   | Layout 1 | `a359dd56a2d3`  |
| 2487   | Layout 1 | `a359dd56a2d3`  |
| 2480   | Layout 1 | `a359dd56a2d3`  |
| 2474   | Layout 1 | `a359dd56a2d3`  |
| 2468   | Layout 1 | `a359dd56a2d3`  |
| 2460   | Layout 1 | `a359dd56a2d3`  |
| 2453   | Layout 1 | `a359dd56a2d3`  |
| 2444   | Layout 1 | `a359dd56a2d3`  |
| 2438   | Layout 1 | `a359dd56a2d3`  |
| 2434   | Layout 1 | `a359dd56a2d3`  |
| 2429   | Layout 1 | `a359dd56a2d3`  |
| 2421   | Layout 1 | `a359dd56a2d3`  |
| 2414   | Layout 1 | `a359dd56a2d3`  |
| 2407   | Layout 1 | `a359dd56a2d3`  |
| 2401   | Layout 1 | `a359dd56a2d3`  |
| 2397   | Layout 1 | `a359dd56a2d3`  |
| 2393   | Layout 1 | `a359dd56a2d3`  |
| 2384   | Layout 1 | `a359dd56a2d3`  |
| 2378   | Layout 1 | `a359dd56a2d3`  |
| 2372   | Layout 1 | `a359dd56a2d3`  |
| 2358   | Layout 1 | `a359dd56a2d3`  |
| 2352   | Layout 1 | `a359dd56a2d3`  |
| 2347   | Layout 1 | `a359dd56a2d3`  |
| 2343   | Layout 1 | `a359dd56a2d3`  |
| 2335   | Layout 1 | `a359dd56a2d3`  |
| 2327   | Layout 1 | `a359dd56a2d3`  |
| 2324   | Layout 1 | `a359dd56a2d3`  |
| 2319   | Layout 1 | `a359dd56a2d3`  |
| 2313   | Layout 1 | `a359dd56a2d3`  |
| 2308   | Layout 1 | `a359dd56a2d3`  |
| 2302   | Layout 1 | `a359dd56a2d3`  |
| 2295   | Layout 1 | `a359dd56a2d3`  |
| 2290   | Layout 1 | `a359dd56a2d3`  |
| 2284   | Layout 1 | `a359dd56a2d3`  |
| 2276   | Layout 1 | `a359dd56a2d3`  |
| 2269   | Layout 1 | `a359dd56a2d3`  |
| 2259   | Layout 1 | `a359dd56a2d3`  |
| 2250   | Layout 1 | `a359dd56a2d3`  |
| 2243   | Layout 1 | `a359dd56a2d3`  |
| 2235   | Layout 1 | `a359dd56a2d3`  |
| 2229   | Layout 1 | `a359dd56a2d3`  |
| 2224   | Layout 1 | `a359dd56a2d3`  |
| 2218   | Layout 1 | `a359dd56a2d3`  |
| 2215   | Layout 1 | `a359dd56a2d3`  |
| 2207   | Layout 1 | `a359dd56a2d3`  |
| 2203   | Layout 1 | `a359dd56a2d3`  |
| 2196   | Layout 1 | `a359dd56a2d3`  |
| 2192   | Layout 1 | `a359dd56a2d3`  |
| 2189   | Layout 1 | `a359dd56a2d3`  |
| 2183   | Layout 1 | `a359dd56a2d3`  |
| 2179   | Layout 1 | `a359dd56a2d3`  |
| 2171   | Layout 1 | `a359dd56a2d3`  |
| 2163   | Layout 1 | `a359dd56a2d3`  |
| 2156   | Layout 1 | `a359dd56a2d3`  |
| 2151   | Layout 1 | `a359dd56a2d3`  |
| 2147   | Layout 1 | `a359dd56a2d3`  |
| 2142   | Layout 1 | `a359dd56a2d3`  |
| 2138   | Layout 1 | `a359dd56a2d3`  |
| 2134   | Layout 1 | `a359dd56a2d3`  |
| 2130   | Layout 1 | `a359dd56a2d3`  |
| 2122   | Layout 1 | `a359dd56a2d3`  |
| 2107   | Layout 1 | `a359dd56a2d3`  |
| 2098   | Layout 1 | `a359dd56a2d3`  |
| 2089   | Layout 1 | `a359dd56a2d3`  |
| 2081   | Layout 1 | `a359dd56a2d3`  |
| 2073   | Layout 1 | `a359dd56a2d3`  |
| 2067   | Layout 1 | `a359dd56a2d3`  |
| 2063   | Layout 1 | `a359dd56a2d3`  |
| 2059   | Layout 1 | `a359dd56a2d3`  |
| 2052   | Layout 1 | `a359dd56a2d3`  |
| 2044   | Layout 1 | `a359dd56a2d3`  |
| 2039   | Layout 1 | `a359dd56a2d3`  |
| 2032   | Layout 1 | `a359dd56a2d3`  |
| 2025   | Layout 1 | `a359dd56a2d3`  |
| 2011   | Layout 1 | `a359dd56a2d3`  |
| 2005   | Layout 1 | `a359dd56a2d3`  |
| 2000   | Layout 1 | `a359dd56a2d3`  |
| 1996   | Layout 1 | `a359dd56a2d3`  |
| 1991   | Layout 1 | `a359dd56a2d3`  |
| 1985   | Layout 1 | `a359dd56a2d3`  |
| 1980   | Layout 1 | `a359dd56a2d3`  |
| 1969   | Layout 1 | `a359dd56a2d3`  |
| 1964   | Layout 1 | `a359dd56a2d3`  |
| 1958   | Layout 1 | `a359dd56a2d3`  |
| 1950   | Layout 1 | `a359dd56a2d3`  |
| 1945   | Layout 1 | `a359dd56a2d3`  |
| 1937   | Layout 1 | `a359dd56a2d3`  |
| 1933   | Layout 1 | `a359dd56a2d3`  |
| 1927   | Layout 1 | `a359dd56a2d3`  |
| 1921   | Layout 1 | `a359dd56a2d3`  |
| 1914   | Layout 1 | `a359dd56a2d3`  |
| 1908   | Layout 1 | `a359dd56a2d3`  |
| 1897   | Layout 1 | `a359dd56a2d3`  |
| 1892   | Layout 1 | `a359dd56a2d3`  |
| 1886   | Layout 1 | `a359dd56a2d3`  |
| 1881   | Layout 1 | `a359dd56a2d3`  |
| 1871   | Layout 1 | `a359dd56a2d3`  |
| 1866   | Layout 1 | `a359dd56a2d3`  |
| 1862   | Layout 1 | `a359dd56a2d3`  |
| 1854   | Layout 1 | `a359dd56a2d3`  |
| 1846   | Layout 1 | `a359dd56a2d3`  |
| 1838   | Layout 1 | `a359dd56a2d3`  |
| 1832   | Layout 1 | `a359dd56a2d3`  |
| 1826   | Layout 1 | `a359dd56a2d3`  |
| 1822   | Layout 1 | `a359dd56a2d3`  |
| 1818   | Layout 1 | `a359dd56a2d3`  |
| 1804   | Layout 1 | `a359dd56a2d3`  |
| 1794   | Layout 1 | `a359dd56a2d3`  |
| 1790   | Layout 1 | `a359dd56a2d3`  |
| 1784   | Layout 1 | `a359dd56a2d3`  |
| 1774   | Layout 1 | `a359dd56a2d3`  |
| 1771   | Layout 1 | `a359dd56a2d3`  |
| 1762   | Layout 1 | `a359dd56a2d3`  |
| 1759   | Layout 1 | `a359dd56a2d3`  |
| 1754   | Layout 1 | `a359dd56a2d3`  |
| 1749   | Layout 1 | `a359dd56a2d3`  |
| 1743   | Layout 1 | `a359dd56a2d3`  |
| 1737   | Layout 1 | `a359dd56a2d3`  |
| 1731   | Layout 1 | `a359dd56a2d3`  |
| 1725   | Layout 1 | `a359dd56a2d3`  |
| 1717   | Layout 1 | `a359dd56a2d3`  |
| 1710   | Layout 1 | `a359dd56a2d3`  |
| 1704   | Layout 1 | `a359dd56a2d3`  |
| 1698   | Layout 1 | `a359dd56a2d3`  |
| 1690   | Layout 1 | `a359dd56a2d3`  |
| 1685   | Layout 1 | `a359dd56a2d3`  |
| 1680   | Layout 1 | `a359dd56a2d3`  |
| 1674   | Layout 1 | `a359dd56a2d3`  |
| 1668   | Layout 1 | `a359dd56a2d3`  |
| 1659   | Layout 1 | `a359dd56a2d3`  |
| 1649   | Layout 1 | `a359dd56a2d3`  |
| 1642   | Layout 1 | `a359dd56a2d3`  |
| 1636   | Layout 1 | `a359dd56a2d3`  |
| 1628   | Layout 1 | `a359dd56a2d3`  |
| 1622   | Layout 1 | `a359dd56a2d3`  |
| 1614   | Layout 1 | `a359dd56a2d3`  |
| 1608   | Layout 1 | `a359dd56a2d3`  |
| 1602   | Layout 1 | `a359dd56a2d3`  |
| 1598   | Layout 1 | `a359dd56a2d3`  |
| 1594   | Layout 1 | `a359dd56a2d3`  |
| 1590   | Layout 1 | `a359dd56a2d3`  |
| 1587   | Layout 1 | `a359dd56a2d3`  |
| 1584   | Layout 1 | `a359dd56a2d3`  |
| 1579   | Layout 1 | `a359dd56a2d3`  |
| 1572   | Layout 1 | `a359dd56a2d3`  |
| 1565   | Layout 1 | `a359dd56a2d3`  |
| 1559   | Layout 1 | `a359dd56a2d3`  |
| 1554   | Layout 1 | `a359dd56a2d3`  |
| 1547   | Layout 1 | `a359dd56a2d3`  |
| 1537   | Layout 1 | `a359dd56a2d3`  |
| 1529   | Layout 1 | `a359dd56a2d3`  |
| 1524   | Layout 1 | `a359dd56a2d3`  |
| 1519   | Layout 1 | `a359dd56a2d3`  |
| 1509   | Layout 1 | `a359dd56a2d3`  |
| 1506   | Layout 1 | `a359dd56a2d3`  |
| 1504   | Layout 1 | `a359dd56a2d3`  |
| 1500   | Layout 1 | `a359dd56a2d3`  |
| 1493   | Layout 1 | `a359dd56a2d3`  |
| 1489   | Layout 1 | `a359dd56a2d3`  |
| 1485   | Layout 1 | `a359dd56a2d3`  |
| 1481   | Layout 1 | `a359dd56a2d3`  |
| 1474   | Layout 1 | `a359dd56a2d3`  |
| 1466   | Layout 1 | `a359dd56a2d3`  |
| 1462   | Layout 1 | `a359dd56a2d3`  |
| 1459   | Layout 1 | `a359dd56a2d3`  |
| 1453   | Layout 1 | `a359dd56a2d3`  |
| 1450   | Layout 1 | `a359dd56a2d3`  |
| 1445   | Layout 1 | `a359dd56a2d3`  |
| 1439   | Layout 1 | `a359dd56a2d3`  |
| 1433   | Layout 1 | `a359dd56a2d3`  |
| 1430   | Layout 1 | `a359dd56a2d3`  |
| 1426   | Layout 1 | `a359dd56a2d3`  |
| 1421   | Layout 1 | `a359dd56a2d3`  |
| 1417   | Layout 1 | `a359dd56a2d3`  |
| 1416   | Layout 1 | `a359dd56a2d3`  |
| 1409   | Layout 1 | `a359dd56a2d3`  |
| 1405   | Layout 1 | `a359dd56a2d3`  |
| 1401   | Layout 1 | `a359dd56a2d3`  |
| 1396   | Layout 1 | `a359dd56a2d3`  |
| 1391   | Layout 1 | `a359dd56a2d3`  |
| 1390   | Layout 1 | `a359dd56a2d3`  |
| 1386   | Layout 1 | `a359dd56a2d3`  |
| 1381   | Layout 1 | `a359dd56a2d3`  |
| 1379   | Layout 1 | `a359dd56a2d3`  |
| 1372   | Layout 1 | `a359dd56a2d3`  |
| 1366   | Layout 1 | `a359dd56a2d3`  |
| 1364   | Layout 1 | `a359dd56a2d3`  |
| 1363   | Layout 1 | `a359dd56a2d3`  |
| 1360   | Layout 1 | `a359dd56a2d3`  |
| 1358   | Layout 1 | `a359dd56a2d3`  |
| 1355   | Layout 1 | `a359dd56a2d3`  |
| 1351   | Layout 1 | `a359dd56a2d3`  |
| 1348   | Layout 1 | `a359dd56a2d3`  |
| 1346   | Layout 1 | `a359dd56a2d3`  |
| 1341   | Layout 1 | `a359dd56a2d3`  |
| 1340   | Layout 1 | `a359dd56a2d3`  |
| 1338   | Layout 1 | `a359dd56a2d3`  |
| 1335   | Layout 1 | `a359dd56a2d3`  |
| 1333   | Layout 1 | `a359dd56a2d3`  |
| 1329   | Layout 1 | `a359dd56a2d3`  |
| 1327   | Layout 1 | `a359dd56a2d3`  |
| 1324   | Layout 1 | `a359dd56a2d3`  |
| 1321   | Layout 1 | `a359dd56a2d3`  |
| 1319   | Layout 1 | `a359dd56a2d3`  |
| 1318   | Layout 1 | `a359dd56a2d3`  |
| 1316   | Layout 1 | `a359dd56a2d3`  |
| 1313   | Layout 1 | `a359dd56a2d3`  |
| 1311   | Layout 1 | `a359dd56a2d3`  |
| 1309   | No file  | `a359dd56a2d3`  |
| 1304   | No file  | `a359dd56a2d3`  |
| 1292   | No file  | `a359dd56a2d3`  |
| 1286   | No file  | `a359dd56a2d3`  |
| 1280   | No file  | `a359dd56a2d3`  |
| 1276   | No file  | `a359dd56a2d3`  |
| 1267   | No file  | `a359dd56a2d3`  |
| 1261   | No file  | `a359dd56a2d3`  |
| 1256   | No file  | `a359dd56a2d3`  |
| 1250   | No file  | `a359dd56a2d3`  |
| 1246   | No file  | `a359dd56a2d3`  |
| 1239   | No file  | `a359dd56a2d3`  |
| 1230   | No file  | `a359dd56a2d3`  |
| 1226   | No file  | `a359dd56a2d3`  |
| 1220   | No file  | `a359dd56a2d3`  |
| 1217   | No file  | `a359dd56a2d3`  |
| 1211   | No file  | `a359dd56a2d3`  |
| 1210   | No file  | `a359dd56a2d3`  |
| 1208   | No file  | `a359dd56a2d3`  |
| 1203   | No file  | `a359dd56a2d3`  |
| 1197   | No file  | `a359dd56a2d3`  |
| 1194   | No file  | `a359dd56a2d3`  |
| 1192   | No file  | `a359dd56a2d3`  |
| 1187   | No file  | `a359dd56a2d3`  |
| 1183   | No file  | `a359dd56a2d3`  |
| 1177   | No file  | `a359dd56a2d3`  |
| 1173   | No file  | `a359dd56a2d3`  |
| 1167   | No file  | `a359dd56a2d3`  |
| 1164   | No file  | `a359dd56a2d3`  |
| 1156   | No file  | `a359dd56a2d3`  |
| 1149   | No file  | `a359dd56a2d3`  |
| 1144   | No file  | `a359dd56a2d3`  |
| 1137   | No file  | `a359dd56a2d3`  |
| 1132   | No file  | `a359dd56a2d3`  |
| 1127   | No file  | `a359dd56a2d3`  |
| 1122   | No file  | `a359dd56a2d3`  |
| 1118   | No file  | `a359dd56a2d3`  |
| 1114   | No file  | `a359dd56a2d3`  |
| 1109   | No file  | `a359dd56a2d3`  |
| 1102   | No file  | `a359dd56a2d3`  |
| 1096   | No file  | `a359dd56a2d3`  |
| 1088   | No file  | `a359dd56a2d3`  |
| 1081   | No file  | `a359dd56a2d3`  |
| 1076   | No file  | `a359dd56a2d3`  |
| 1069   | No file  | `a359dd56a2d3`  |
| 1064   | No file  | `a359dd56a2d3`  |
| 1058   | No file  | `a359dd56a2d3`  |
| 1051   | No file  | `a359dd56a2d3`  |
| 1044   | No file  | `a359dd56a2d3`  |
| 1036   | No file  | `a359dd56a2d3`  |
| 1026   | No file  | `a359dd56a2d3`  |
| 1016   | No file  | `a359dd56a2d3`  |
| 1009   | No file  | `a359dd56a2d3`  |
| 1005   | No file  | `a359dd56a2d3`  |
| 1000   | No file  | `a359dd56a2d3`  |
| 998    | No file  | `a359dd56a2d3`  |
| 990    | No file  | `a359dd56a2d3`  |
| 979    | No file  | `a359dd56a2d3`  |
| 972    | No file  | `a359dd56a2d3`  |
| 963    | No file  | `a359dd56a2d3`  |
| 955    | No file  | `a359dd56a2d3`  |
| 946    | No file  | `a359dd56a2d3`  |
| 938    | No file  | `a359dd56a2d3`  |
| 927    | No file  | `a359dd56a2d3`  |
| 911    | No file  | `a359dd56a2d3`  |
| 904    | No file  | `a359dd56a2d3`  |
| 899    | No file  | `a359dd56a2d3`  |
| 894    | No file  | `a359dd56a2d3`  |
| 885    | No file  | `a359dd56a2d3`  |
| 879    | No file  | `a359dd56a2d3`  |
| 872    | No file  | `a359dd56a2d3`  |
| 864    | No file  | `a359dd56a2d3`  |
| 855    | No file  | `a359dd56a2d3`  |
| 853    | No file  | `a359dd56a2d3`  |
| 845    | No file  | `a359dd56a2d3`  |
| 837    | No file  | `a359dd56a2d3`  |
| 829    | No file  | `a359dd56a2d3`  |
| 822    | No file  | `a359dd56a2d3`  |
| 814    | No file  | `a359dd56a2d3`  |
| 805    | No file  | `a359dd56a2d3`  |
| 794    | No file  | `a359dd56a2d3`  |
| 787    | No file  | `a359dd56a2d3`  |
| 780    | No file  | `a359dd56a2d3`  |
| 771    | No file  | `a359dd56a2d3`  |
| 760    | No file  | `a359dd56a2d3`  |
| 748    | No file  | `a359dd56a2d3`  |
| 741    | No file  | `a359dd56a2d3`  |
| 736    | No file  | `a359dd56a2d3`  |
| 731    | No file  | `a359dd56a2d3`  |
| 723    | No file  | `a359dd56a2d3`  |
| 711    | No file  | `a359dd56a2d3`  |
| 707    | No file  | `a359dd56a2d3`  |
| 697    | No file  | `a359dd56a2d3`  |
| 689    | No file  | `a359dd56a2d3`  |
| 683    | No file  | `a359dd56a2d3`  |
| 678    | No file  | `a359dd56a2d3`  |
| 670    | No file  | `a359dd56a2d3`  |
| 661    | No file  | `a359dd56a2d3`  |
| 656    | No file  | `a359dd56a2d3`  |
| 652    | No file  | `a359dd56a2d3`  |
| 643    | No file  | `a359dd56a2d3`  |
| 637    | No file  | `a359dd56a2d3`  |
| 630    | No file  | `a359dd56a2d3`  |
| 627    | No file  | `a359dd56a2d3`  |
| 621    | No file  | `a359dd56a2d3`  |
| 617    | No file  | `a359dd56a2d3`  |
| 615    | No file  | `a359dd56a2d3`  |
| 606    | No file  | `a359dd56a2d3`  |
| 599    | No file  | `a359dd56a2d3`  |
| 592    | No file  | `a359dd56a2d3`  |
| 586    | No file  | `a359dd56a2d3`  |
| 577    | No file  | `a359dd56a2d3`  |
| 569    | No file  | `a359dd56a2d3`  |
| 561    | No file  | `a359dd56a2d3`  |
| 554    | No file  | `a359dd56a2d3`  |
| 542    | No file  | `a359dd56a2d3`  |
| 532    | No file  | `a359dd56a2d3`  |
| 531    | No file  | `a359dd56a2d3`  |
| 526    | No file  | `a359dd56a2d3`  |
| 521    | No file  | `a359dd56a2d3`  |
| 517    | No file  | `a359dd56a2d3`  |
| 510    | No file  | `a359dd56a2d3`  |
| 508    | No file  | `a359dd56a2d3`  |
| 504    | No file  | `a359dd56a2d3`  |
| 497    | No file  | `a359dd56a2d3`  |
| 491    | No file  | `a359dd56a2d3`  |
| 485    | No file  | `a359dd56a2d3`  |
| 478    | No file  | `a359dd56a2d3`  |
| 472    | No file  | `a359dd56a2d3`  |
| 466    | No file  | `a359dd56a2d3`  |
| 457    | No file  | `a359dd56a2d3`  |
| 452    | No file  | `a359dd56a2d3`  |
| 449    | No file  | `a359dd56a2d3`  |
| 435    | No file  | `a359dd56a2d3`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                        |
| --------------------- | -------- | ----------------------------------------------------------- |
| `buff.dbss`           | Optional | Full buff records; every row here has a record there        |
| `languagedata_en.loc` | Optional | English descriptions, LOC type 5 keyed by `buff_id`         |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout of `npcsimply.bss` and
`plantexchangegroup.bss` (`_common/pabr_strings.py`).

| Offset              | Type            | Field        | Notes                                                  |
| ------------------- | --------------- | ------------ | ------------------------------------------------------ |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                           |
| `+0x04`             | u32             | count        | Number of rows; 44,683 on client 3464, equal to the `buff.dbss` count |
| `+0x08`             | Buff Row[count] | rows         | See Buff Row                                           |
| `rows+0x00`         | String Table    | string_table | See String Table                                       |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where the rows end         |
| `string_table+0x04` | u32             | zero         | Always 0                                               |

The rows follow `buffoffset.dbss` order exactly, which is neither ascending nor
descending by ID (the first row is buff 4100000000 on client 3464, 48879 on
3458).

### Buff Row (32 bytes)

Fields are unaligned. The Source column names the `buff.dbss` field that holds
the same value in every row, when one does.

| Offset  | Type     | Field           | Source (`buff.dbss`)    | Notes                                                                          |
| ------- | -------- | --------------- | ----------------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u32      | buff_id         | `buff_id`               | Unique; 43 to 65,528 and five IDs from 700,000 to 4,100,000,000                |
| `+0x04` | u8       | need_equip_type | stats `need_equip_type` | `0` in every row but buff 2078 (`13`)                                          |
| `+0x05` | bytes[2] | unknown_05      |                         | Always `0`                                                                     |
| `+0x07` | u8       | unknown_07      | stats `+0x7D`           | `0` in every row but buff 2078 (`1`)                                           |
| `+0x08` | u8       | unknown_08      | stats `+0x7D`           | Same values as `unknown_07`; not stats `+0x7E`, see Notes                      |
| `+0x09` | u8       | unknown_09      | stats `unknown_7f`      | Always `2`                                                                     |
| `+0x0A` | u8       | unknown_0a      |                         | Always `0`                                                                     |
| `+0x0B` | u8       | need_equip_slot | stats `need_equip_slot` | `46` (no slot) in every row but buff 2078 (`6`)                                |
| `+0x0C` | u8       | unknown_0c      | stats `unknown_82`      | `2` in every row but buff 2078 (`1`)                                           |
| `+0x0D` | u32      | effect_name_ref | `effect_name`           | String table index; 187 distinct, `0` (`"0"`) in 39,527 rows, `1` (`""`) in 52 |
| `+0x11` | u8       | is_debuff       | stats `is_debuff`       | `1` in 14,432 rows                                                             |
| `+0x12` | u32      | unknown_12_ref  |                         | String table index; `1` (`""`) in every row, see Open Questions               |
| `+0x16` | u8       | remove_on_dead  | stats `remove_on_dead`  | `1` in 33,944 rows                                                             |
| `+0x17` | u8       | is_shown        | `is_shown`              | `1` in 12,766 rows                                                             |
| `+0x18` | u32      | unknown_18      | tail `unknown_02`       | `0` in 25,701 rows, `1` in 14,420, `2` in 4,562                                |
| `+0x1C` | u32      | icon_ref        | `icon_path`             | String table index; `1` (the empty string) in 29,357 rows                      |

### String Table (variable: 4 bytes + strings)

1,235 strings on client 3464, all distinct and all referenced. `effect_name_ref`,
`unknown_12_ref` and `icon_ref` index the same table and share only the empty
string: index 0 is `"0"`, index 1 is `""`, and every other entry is either an
`effect_name` value or an icon path.

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | 1,235 on client 3464 |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries  |

## Layout 1

Before client 3464 `buff_id` was a u16 and every later field sat 2 bytes
earlier. Only the Buff Row differs from Layout 2. Field names keep Layout
2's offsets, so `unknown_05` sits at `+0x03` here.

The file holds no layout number; the parser reads it with the layout whose
rows end where the string table starts, trying the one whose Versions clients
cover the loaded client first.

### Buff Row (30 bytes)

| Offset  | Type     | Field           | Notes |
| ------- | -------- | --------------- | ----- |
| `+0x00` | u16      | buff_id         |       |
| `+0x02` | u8       | need_equip_type |       |
| `+0x03` | bytes[2] | unknown_05      |       |
| `+0x05` | u8       | unknown_07      |       |
| `+0x06` | u8       | unknown_08      |       |
| `+0x07` | u8       | unknown_09      |       |
| `+0x08` | u8       | unknown_0a      |       |
| `+0x09` | u8       | need_equip_slot |       |
| `+0x0A` | u8       | unknown_0c      |       |
| `+0x0B` | u32      | effect_name_ref |       |
| `+0x0F` | u8       | is_debuff       |       |
| `+0x10` | u32      | unknown_12_ref  |       |
| `+0x14` | u8       | remove_on_dead  |       |
| `+0x15` | u8       | is_shown        |       |
| `+0x16` | u32      | unknown_18      |       |
| `+0x1A` | u32      | icon_ref        |       |

## Notes

- Checked against `buff.dbss` on client 3464: all 44,683 IDs have a record
  there, and `effect_name_ref`, `icon_ref`, `is_shown` and every field with a
  Source match the record in all 44,683 rows.
- The app builds its buff icon lookup index (`IndexKind.BUFF_ICON`, read
  through `IconKind.BUFF`) from this file: it gives the same paths as
  `buff.dbss` from a 1.4 MB fixed-row file, without walking the 12 MB of
  variable-length records.
- Icon paths follow the `buff.dbss` conventions: 15,282 rows set one, over
  1,043 stored strings that become 1,017 paths once lowercased with `\`
  turned into `/` (35 stored strings use backslashes). 206 rows store the
  placeholder `UNKNOWN`, and three double a separator
  (`04_PC_Skill//04_Debuff`); collapsing it finds their file. Resolve under
  `ui_texture/icon/`, as for `buff.dbss`. On client 3458, 14,884 of the
  15,076 real icons exist; the other 192 rows point at 22 paths the client
  does not ship.
- The icon is not unique to a headline buff: the hidden effects that follow
  one often store the same path (all of 48717 to 48734, the three Adventure's
  Boon runs, store `SilverBless.dds`), while only the headline has `is_shown`.
- Buff 2078 (`[장착용] 두건 효과 : 정체 감추기`, "equip: hood effect, hide
  identity") is the only row where `+0x04` to `+0x0C` differ from the
  constants, and its stats bytes `+0x7A` to `+0x82` read
  `0d 00 00 01 01 02 00 06 01`, the same nine bytes as this row: the
  `_needEquipType` copy of an `itemenchant.dbss` equip type (see the
  `buff.dbss` Field Names). On every other buff stats `+0x7E` (`unknown_7e`) is
  `1` in 44,588 rows while `+0x08` here stays `0`, so `+0x08` is not that
  byte. Only per-byte matches are claimed above.
- `buff.dbss` fields with no copy here: `name`, `buff_level`, `group`,
  `condition_type`, `effect_type`, the parameters, `duration_ms`,
  `apply_rate`, `description` and `stacking_category`.
- [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  mentions the file only as a 30-byte PABR projection over the buff keys (the
  pre-3464 row size) with
  an icon string-table reference; it gives no row layout.

## Field Names

The named fields take the names of the `buff.dbss` fields they copy, which come from the 2016 `gc::BuffStaticStatus` and the `Buff_Table` of a private server on client 519 ([buff.dbss Field Names](../dbss/buff_dbss.md#field-names)). The client 1784 exe reads a Layout 1 row in `BuffSimplyStaticStatusManager::readFromBinary` (VA `0x140fbad30`) into a 0x78-byte struct. It copies `+0x02` to `+0x0A` in one 9-byte read, the `gc::ItemEquipType` copy, so the 2016 member order applies byte for byte: `unknown_05` is `_isWeapon` and `_isSubWeapon`, and `unknown_07`, `unknown_08`, `unknown_09`, `unknown_0a` and `unknown_0c` sit in the `_isExtractable`, `_isUseAvatarMesh`, `_rangeType`, `_isTwoHanded` and `_enchantFailType` places. No server column holds them and the matching `itemenchant.dbss` header bytes have no name either. `unknown_18` copies `buff.dbss` tail `unknown_02`, the `DisplayOrder` column of the server and client `Buff_Table` loaders ([buff.dbss Field Names](../dbss/buff_dbss.md#field-names)); it keeps its name because the live client does not confirm it.

## Open Questions

### What does `unknown_12` hold?

A string table index: the client 1784 reader reads it with the same 8-bit
string reader as `icon_ref` (the one `buff.dbss` uses for `icon_path` and
`ui_effect`) into struct `+0x20`, between `effect_name` (`+0x00`) and the
icon (`+0x40`). It is `1`, the empty string, in every row of clients 1784
and 3482. The only other 8-bit string in a `buff.dbss` record is
`ui_effect`, which is empty on every record of those clients, so
`unknown_12_ref` is probably `ui_effect`. No client code that reads struct
`+0x20` has been traced, and no row stores a non-empty string to compare.
