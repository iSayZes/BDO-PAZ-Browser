# `buffsimply.bss` Format

## Purpose

A compact copy of [`buff.dbss`](buff_dbss.md): one fixed 32-byte row per buff
with the buff ID, the icon path and `effect_name` as indices into a shared
string table, `is_shown`, `is_debuff`, `remove_on_dead` and the equipment the
buff needs. It holds no name, parameters,
duration or description, so it covers what the buff bar needs to draw a buff
and nothing about its effect.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes     | Records         | Row bytes |
| ------ | -------------- | ------- | ---------------- | --------- | --------------- | --------- |
| 2      | 3464 and later | 3483    | `buffsimply.bss` | 1,490,698 | 44,724 Buff Row | 32        |
| 1      | 1311 to 3458   | 3458    | `buffsimply.bss` | 1,398,407 | 44,645 Buff Row | 30        |

| Layout | File             | Known             | Unknown           |
| ------ | ---------------- | ----------------- | ----------------- |
| 2      | `buffsimply.bss` | 819,838 B (55.0%) | 670,860 B (45.0%) |
| 1      | `buffsimply.bss` | 728,732 B (52.1%) | 669,675 B (47.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `f7628403c4d7`  |
| 3482   | Layout 2 | `f7628403c4d7`  |
| 3474   | Layout 2 | `f7628403c4d7`  |
| 3473   | Layout 2 | `f7628403c4d7`  |
| 3464   | Layout 2 | `f7628403c4d7`  |
| 3458   | Layout 1 | `f7628403c4d7`  |
| 3454   | Layout 1 | `f7628403c4d7`  |
| 3444   | Layout 1 | `f7628403c4d7`  |
| 3435   | Layout 1 | `f7628403c4d7`  |
| 3426   | Layout 1 | `f7628403c4d7`  |
| 3418   | Layout 1 | `f7628403c4d7`  |
| 3412   | Layout 1 | `f7628403c4d7`  |
| 3402   | Layout 1 | `f7628403c4d7`  |
| 3396   | Layout 1 | `f7628403c4d7`  |
| 3387   | Layout 1 | `f7628403c4d7`  |
| 3381   | Layout 1 | `f7628403c4d7`  |
| 3373   | Layout 1 | `f7628403c4d7`  |
| 3364   | Layout 1 | `f7628403c4d7`  |
| 3356   | Layout 1 | `f7628403c4d7`  |
| 3349   | Layout 1 | `f7628403c4d7`  |
| 3342   | Layout 1 | `f7628403c4d7`  |
| 3335   | Layout 1 | `f7628403c4d7`  |
| 3326   | Layout 1 | `f7628403c4d7`  |
| 3321   | Layout 1 | `f7628403c4d7`  |
| 3314   | Layout 1 | `f7628403c4d7`  |
| 3303   | Layout 1 | `f7628403c4d7`  |
| 3302   | Layout 1 | `f7628403c4d7`  |
| 3293   | Layout 1 | `f7628403c4d7`  |
| 3283   | Layout 1 | `f7628403c4d7`  |
| 3275   | Layout 1 | `f7628403c4d7`  |
| 3267   | Layout 1 | `f7628403c4d7`  |
| 3258   | Layout 1 | `f7628403c4d7`  |
| 3251   | Layout 1 | `f7628403c4d7`  |
| 3242   | Layout 1 | `f7628403c4d7`  |
| 3235   | Layout 1 | `f7628403c4d7`  |
| 3229   | Layout 1 | `f7628403c4d7`  |
| 3212   | Layout 1 | `f7628403c4d7`  |
| 3203   | Layout 1 | `f7628403c4d7`  |
| 3193   | Layout 1 | `f7628403c4d7`  |
| 3186   | Layout 1 | `f7628403c4d7`  |
| 3177   | Layout 1 | `f7628403c4d7`  |
| 3169   | Layout 1 | `f7628403c4d7`  |
| 3158   | Layout 1 | `f7628403c4d7`  |
| 3151   | Layout 1 | `f7628403c4d7`  |
| 3144   | Layout 1 | `f7628403c4d7`  |
| 3133   | Layout 1 | `f7628403c4d7`  |
| 3125   | Layout 1 | `f7628403c4d7`  |
| 3118   | Layout 1 | `f7628403c4d7`  |
| 3111   | Layout 1 | `f7628403c4d7`  |
| 3103   | Layout 1 | `f7628403c4d7`  |
| 3095   | Layout 1 | `f7628403c4d7`  |
| 3086   | Layout 1 | `f7628403c4d7`  |
| 3072   | Layout 1 | `f7628403c4d7`  |
| 3062   | Layout 1 | `f7628403c4d7`  |
| 3052   | Layout 1 | `f7628403c4d7`  |
| 3045   | Layout 1 | `f7628403c4d7`  |
| 3037   | Layout 1 | `f7628403c4d7`  |
| 3030   | Layout 1 | `f7628403c4d7`  |
| 3021   | Layout 1 | `f7628403c4d7`  |
| 3012   | Layout 1 | `f7628403c4d7`  |
| 3002   | Layout 1 | `f7628403c4d7`  |
| 2995   | Layout 1 | `f7628403c4d7`  |
| 2987   | Layout 1 | `f7628403c4d7`  |
| 2978   | Layout 1 | `f7628403c4d7`  |
| 2970   | Layout 1 | `f7628403c4d7`  |
| 2959   | Layout 1 | `f7628403c4d7`  |
| 2951   | Layout 1 | `f7628403c4d7`  |
| 2942   | Layout 1 | `f7628403c4d7`  |
| 2935   | Layout 1 | `f7628403c4d7`  |
| 2932   | Layout 1 | `f7628403c4d7`  |
| 2923   | Layout 1 | `f7628403c4d7`  |
| 2919   | Layout 1 | `f7628403c4d7`  |
| 2907   | Layout 1 | `f7628403c4d7`  |
| 2900   | Layout 1 | `f7628403c4d7`  |
| 2891   | Layout 1 | `f7628403c4d7`  |
| 2882   | Layout 1 | `f7628403c4d7`  |
| 2872   | Layout 1 | `f7628403c4d7`  |
| 2863   | Layout 1 | `f7628403c4d7`  |
| 2855   | Layout 1 | `f7628403c4d7`  |
| 2849   | Layout 1 | `f7628403c4d7`  |
| 2844   | Layout 1 | `f7628403c4d7`  |
| 2834   | Layout 1 | `f7628403c4d7`  |
| 2825   | Layout 1 | `f7628403c4d7`  |
| 2819   | Layout 1 | `f7628403c4d7`  |
| 2811   | Layout 1 | `f7628403c4d7`  |
| 2803   | Layout 1 | `f7628403c4d7`  |
| 2794   | Layout 1 | `f7628403c4d7`  |
| 2783   | Layout 1 | `f7628403c4d7`  |
| 2774   | Layout 1 | `f7628403c4d7`  |
| 2765   | Layout 1 | `f7628403c4d7`  |
| 2756   | Layout 1 | `f7628403c4d7`  |
| 2750   | Layout 1 | `f7628403c4d7`  |
| 2743   | Layout 1 | `f7628403c4d7`  |
| 2736   | Layout 1 | `f7628403c4d7`  |
| 2726   | Layout 1 | `f7628403c4d7`  |
| 2717   | Layout 1 | `f7628403c4d7`  |
| 2709   | Layout 1 | `f7628403c4d7`  |
| 2703   | Layout 1 | `f7628403c4d7`  |
| 2695   | Layout 1 | `f7628403c4d7`  |
| 2684   | Layout 1 | `f7628403c4d7`  |
| 2672   | Layout 1 | `f7628403c4d7`  |
| 2665   | Layout 1 | `f7628403c4d7`  |
| 2657   | Layout 1 | `f7628403c4d7`  |
| 2649   | Layout 1 | `f7628403c4d7`  |
| 2644   | Layout 1 | `f7628403c4d7`  |
| 2637   | Layout 1 | `f7628403c4d7`  |
| 2629   | Layout 1 | `f7628403c4d7`  |
| 2619   | Layout 1 | `f7628403c4d7`  |
| 2612   | Layout 1 | `f7628403c4d7`  |
| 2606   | Layout 1 | `f7628403c4d7`  |
| 2602   | Layout 1 | `f7628403c4d7`  |
| 2601   | Layout 1 | `f7628403c4d7`  |
| 2592   | Layout 1 | `f7628403c4d7`  |
| 2583   | Layout 1 | `f7628403c4d7`  |
| 2575   | Layout 1 | `f7628403c4d7`  |
| 2567   | Layout 1 | `f7628403c4d7`  |
| 2560   | Layout 1 | `f7628403c4d7`  |
| 2553   | Layout 1 | `f7628403c4d7`  |
| 2545   | Layout 1 | `f7628403c4d7`  |
| 2538   | Layout 1 | `f7628403c4d7`  |
| 2529   | Layout 1 | `f7628403c4d7`  |
| 2519   | Layout 1 | `f7628403c4d7`  |
| 2513   | Layout 1 | `f7628403c4d7`  |
| 2510   | Layout 1 | `f7628403c4d7`  |
| 2507   | Layout 1 | `f7628403c4d7`  |
| 2503   | Layout 1 | `f7628403c4d7`  |
| 2498   | Layout 1 | `f7628403c4d7`  |
| 2492   | Layout 1 | `f7628403c4d7`  |
| 2487   | Layout 1 | `f7628403c4d7`  |
| 2480   | Layout 1 | `f7628403c4d7`  |
| 2474   | Layout 1 | `f7628403c4d7`  |
| 2468   | Layout 1 | `f7628403c4d7`  |
| 2460   | Layout 1 | `f7628403c4d7`  |
| 2453   | Layout 1 | `f7628403c4d7`  |
| 2444   | Layout 1 | `f7628403c4d7`  |
| 2438   | Layout 1 | `f7628403c4d7`  |
| 2434   | Layout 1 | `f7628403c4d7`  |
| 2429   | Layout 1 | `f7628403c4d7`  |
| 2421   | Layout 1 | `f7628403c4d7`  |
| 2414   | Layout 1 | `f7628403c4d7`  |
| 2407   | Layout 1 | `f7628403c4d7`  |
| 2401   | Layout 1 | `f7628403c4d7`  |
| 2397   | Layout 1 | `f7628403c4d7`  |
| 2393   | Layout 1 | `f7628403c4d7`  |
| 2384   | Layout 1 | `f7628403c4d7`  |
| 2378   | Layout 1 | `f7628403c4d7`  |
| 2372   | Layout 1 | `f7628403c4d7`  |
| 2358   | Layout 1 | `f7628403c4d7`  |
| 2352   | Layout 1 | `f7628403c4d7`  |
| 2347   | Layout 1 | `f7628403c4d7`  |
| 2343   | Layout 1 | `f7628403c4d7`  |
| 2335   | Layout 1 | `f7628403c4d7`  |
| 2327   | Layout 1 | `f7628403c4d7`  |
| 2324   | Layout 1 | `f7628403c4d7`  |
| 2319   | Layout 1 | `f7628403c4d7`  |
| 2313   | Layout 1 | `f7628403c4d7`  |
| 2308   | Layout 1 | `f7628403c4d7`  |
| 2302   | Layout 1 | `f7628403c4d7`  |
| 2295   | Layout 1 | `f7628403c4d7`  |
| 2290   | Layout 1 | `f7628403c4d7`  |
| 2284   | Layout 1 | `f7628403c4d7`  |
| 2276   | Layout 1 | `f7628403c4d7`  |
| 2269   | Layout 1 | `f7628403c4d7`  |
| 2259   | Layout 1 | `f7628403c4d7`  |
| 2250   | Layout 1 | `f7628403c4d7`  |
| 2243   | Layout 1 | `f7628403c4d7`  |
| 2235   | Layout 1 | `f7628403c4d7`  |
| 2229   | Layout 1 | `f7628403c4d7`  |
| 2224   | Layout 1 | `f7628403c4d7`  |
| 2218   | Layout 1 | `f7628403c4d7`  |
| 2215   | Layout 1 | `f7628403c4d7`  |
| 2207   | Layout 1 | `f7628403c4d7`  |
| 2203   | Layout 1 | `f7628403c4d7`  |
| 2196   | Layout 1 | `f7628403c4d7`  |
| 2192   | Layout 1 | `f7628403c4d7`  |
| 2189   | Layout 1 | `f7628403c4d7`  |
| 2183   | Layout 1 | `f7628403c4d7`  |
| 2179   | Layout 1 | `f7628403c4d7`  |
| 2171   | Layout 1 | `f7628403c4d7`  |
| 2163   | Layout 1 | `f7628403c4d7`  |
| 2156   | Layout 1 | `f7628403c4d7`  |
| 2151   | Layout 1 | `f7628403c4d7`  |
| 2147   | Layout 1 | `f7628403c4d7`  |
| 2142   | Layout 1 | `f7628403c4d7`  |
| 2138   | Layout 1 | `f7628403c4d7`  |
| 2134   | Layout 1 | `f7628403c4d7`  |
| 2130   | Layout 1 | `f7628403c4d7`  |
| 2122   | Layout 1 | `f7628403c4d7`  |
| 2107   | Layout 1 | `f7628403c4d7`  |
| 2098   | Layout 1 | `f7628403c4d7`  |
| 2089   | Layout 1 | `f7628403c4d7`  |
| 2081   | Layout 1 | `f7628403c4d7`  |
| 2073   | Layout 1 | `f7628403c4d7`  |
| 2067   | Layout 1 | `f7628403c4d7`  |
| 2063   | Layout 1 | `f7628403c4d7`  |
| 2059   | Layout 1 | `f7628403c4d7`  |
| 2052   | Layout 1 | `f7628403c4d7`  |
| 2044   | Layout 1 | `f7628403c4d7`  |
| 2039   | Layout 1 | `f7628403c4d7`  |
| 2032   | Layout 1 | `f7628403c4d7`  |
| 2025   | Layout 1 | `f7628403c4d7`  |
| 2011   | Layout 1 | `f7628403c4d7`  |
| 2005   | Layout 1 | `f7628403c4d7`  |
| 2000   | Layout 1 | `f7628403c4d7`  |
| 1996   | Layout 1 | `f7628403c4d7`  |
| 1991   | Layout 1 | `f7628403c4d7`  |
| 1985   | Layout 1 | `f7628403c4d7`  |
| 1980   | Layout 1 | `f7628403c4d7`  |
| 1969   | Layout 1 | `f7628403c4d7`  |
| 1964   | Layout 1 | `f7628403c4d7`  |
| 1958   | Layout 1 | `f7628403c4d7`  |
| 1950   | Layout 1 | `f7628403c4d7`  |
| 1945   | Layout 1 | `f7628403c4d7`  |
| 1937   | Layout 1 | `f7628403c4d7`  |
| 1933   | Layout 1 | `f7628403c4d7`  |
| 1927   | Layout 1 | `f7628403c4d7`  |
| 1921   | Layout 1 | `f7628403c4d7`  |
| 1914   | Layout 1 | `f7628403c4d7`  |
| 1908   | Layout 1 | `f7628403c4d7`  |
| 1897   | Layout 1 | `f7628403c4d7`  |
| 1892   | Layout 1 | `f7628403c4d7`  |
| 1886   | Layout 1 | `f7628403c4d7`  |
| 1881   | Layout 1 | `f7628403c4d7`  |
| 1871   | Layout 1 | `f7628403c4d7`  |
| 1866   | Layout 1 | `f7628403c4d7`  |
| 1862   | Layout 1 | `f7628403c4d7`  |
| 1854   | Layout 1 | `f7628403c4d7`  |
| 1846   | Layout 1 | `f7628403c4d7`  |
| 1838   | Layout 1 | `f7628403c4d7`  |
| 1832   | Layout 1 | `f7628403c4d7`  |
| 1826   | Layout 1 | `f7628403c4d7`  |
| 1822   | Layout 1 | `f7628403c4d7`  |
| 1818   | Layout 1 | `f7628403c4d7`  |
| 1804   | Layout 1 | `f7628403c4d7`  |
| 1794   | Layout 1 | `f7628403c4d7`  |
| 1790   | Layout 1 | `f7628403c4d7`  |
| 1784   | Layout 1 | `f7628403c4d7`  |
| 1774   | Layout 1 | `f7628403c4d7`  |
| 1771   | Layout 1 | `f7628403c4d7`  |
| 1762   | Layout 1 | `f7628403c4d7`  |
| 1759   | Layout 1 | `f7628403c4d7`  |
| 1754   | Layout 1 | `f7628403c4d7`  |
| 1749   | Layout 1 | `f7628403c4d7`  |
| 1743   | Layout 1 | `f7628403c4d7`  |
| 1737   | Layout 1 | `f7628403c4d7`  |
| 1731   | Layout 1 | `f7628403c4d7`  |
| 1725   | Layout 1 | `f7628403c4d7`  |
| 1717   | Layout 1 | `f7628403c4d7`  |
| 1710   | Layout 1 | `f7628403c4d7`  |
| 1704   | Layout 1 | `f7628403c4d7`  |
| 1698   | Layout 1 | `f7628403c4d7`  |
| 1690   | Layout 1 | `f7628403c4d7`  |
| 1685   | Layout 1 | `f7628403c4d7`  |
| 1680   | Layout 1 | `f7628403c4d7`  |
| 1674   | Layout 1 | `f7628403c4d7`  |
| 1668   | Layout 1 | `f7628403c4d7`  |
| 1659   | Layout 1 | `f7628403c4d7`  |
| 1649   | Layout 1 | `f7628403c4d7`  |
| 1642   | Layout 1 | `f7628403c4d7`  |
| 1636   | Layout 1 | `f7628403c4d7`  |
| 1628   | Layout 1 | `f7628403c4d7`  |
| 1622   | Layout 1 | `f7628403c4d7`  |
| 1614   | Layout 1 | `f7628403c4d7`  |
| 1608   | Layout 1 | `f7628403c4d7`  |
| 1602   | Layout 1 | `f7628403c4d7`  |
| 1598   | Layout 1 | `f7628403c4d7`  |
| 1594   | Layout 1 | `f7628403c4d7`  |
| 1590   | Layout 1 | `f7628403c4d7`  |
| 1587   | Layout 1 | `f7628403c4d7`  |
| 1584   | Layout 1 | `f7628403c4d7`  |
| 1579   | Layout 1 | `f7628403c4d7`  |
| 1572   | Layout 1 | `f7628403c4d7`  |
| 1565   | Layout 1 | `f7628403c4d7`  |
| 1559   | Layout 1 | `f7628403c4d7`  |
| 1554   | Layout 1 | `f7628403c4d7`  |
| 1547   | Layout 1 | `f7628403c4d7`  |
| 1537   | Layout 1 | `f7628403c4d7`  |
| 1529   | Layout 1 | `f7628403c4d7`  |
| 1524   | Layout 1 | `f7628403c4d7`  |
| 1519   | Layout 1 | `f7628403c4d7`  |
| 1509   | Layout 1 | `f7628403c4d7`  |
| 1506   | Layout 1 | `f7628403c4d7`  |
| 1504   | Layout 1 | `f7628403c4d7`  |
| 1500   | Layout 1 | `f7628403c4d7`  |
| 1493   | Layout 1 | `f7628403c4d7`  |
| 1489   | Layout 1 | `f7628403c4d7`  |
| 1485   | Layout 1 | `f7628403c4d7`  |
| 1481   | Layout 1 | `f7628403c4d7`  |
| 1474   | Layout 1 | `f7628403c4d7`  |
| 1466   | Layout 1 | `f7628403c4d7`  |
| 1462   | Layout 1 | `f7628403c4d7`  |
| 1459   | Layout 1 | `f7628403c4d7`  |
| 1453   | Layout 1 | `f7628403c4d7`  |
| 1450   | Layout 1 | `f7628403c4d7`  |
| 1445   | Layout 1 | `f7628403c4d7`  |
| 1439   | Layout 1 | `f7628403c4d7`  |
| 1433   | Layout 1 | `f7628403c4d7`  |
| 1430   | Layout 1 | `f7628403c4d7`  |
| 1426   | Layout 1 | `f7628403c4d7`  |
| 1421   | Layout 1 | `f7628403c4d7`  |
| 1417   | Layout 1 | `f7628403c4d7`  |
| 1416   | Layout 1 | `f7628403c4d7`  |
| 1409   | Layout 1 | `f7628403c4d7`  |
| 1405   | Layout 1 | `f7628403c4d7`  |
| 1401   | Layout 1 | `f7628403c4d7`  |
| 1396   | Layout 1 | `f7628403c4d7`  |
| 1391   | Layout 1 | `f7628403c4d7`  |
| 1390   | Layout 1 | `f7628403c4d7`  |
| 1386   | Layout 1 | `f7628403c4d7`  |
| 1381   | Layout 1 | `f7628403c4d7`  |
| 1379   | Layout 1 | `f7628403c4d7`  |
| 1372   | Layout 1 | `f7628403c4d7`  |
| 1366   | Layout 1 | `f7628403c4d7`  |
| 1364   | Layout 1 | `f7628403c4d7`  |
| 1363   | Layout 1 | `f7628403c4d7`  |
| 1360   | Layout 1 | `f7628403c4d7`  |
| 1358   | Layout 1 | `f7628403c4d7`  |
| 1355   | Layout 1 | `f7628403c4d7`  |
| 1351   | Layout 1 | `f7628403c4d7`  |
| 1348   | Layout 1 | `f7628403c4d7`  |
| 1346   | Layout 1 | `f7628403c4d7`  |
| 1341   | Layout 1 | `f7628403c4d7`  |
| 1340   | Layout 1 | `f7628403c4d7`  |
| 1338   | Layout 1 | `f7628403c4d7`  |
| 1335   | Layout 1 | `f7628403c4d7`  |
| 1333   | Layout 1 | `f7628403c4d7`  |
| 1329   | Layout 1 | `f7628403c4d7`  |
| 1327   | Layout 1 | `f7628403c4d7`  |
| 1324   | Layout 1 | `f7628403c4d7`  |
| 1321   | Layout 1 | `f7628403c4d7`  |
| 1319   | Layout 1 | `f7628403c4d7`  |
| 1318   | Layout 1 | `f7628403c4d7`  |
| 1316   | Layout 1 | `f7628403c4d7`  |
| 1313   | Layout 1 | `f7628403c4d7`  |
| 1311   | Layout 1 | `f7628403c4d7`  |
| 1309   | No file  | `f7628403c4d7`  |
| 1304   | No file  | `f7628403c4d7`  |
| 1292   | No file  | `f7628403c4d7`  |
| 1286   | No file  | `f7628403c4d7`  |
| 1280   | No file  | `f7628403c4d7`  |
| 1276   | No file  | `f7628403c4d7`  |
| 1267   | No file  | `f7628403c4d7`  |
| 1261   | No file  | `f7628403c4d7`  |
| 1256   | No file  | `f7628403c4d7`  |
| 1250   | No file  | `f7628403c4d7`  |
| 1246   | No file  | `f7628403c4d7`  |
| 1239   | No file  | `f7628403c4d7`  |
| 1230   | No file  | `f7628403c4d7`  |
| 1226   | No file  | `f7628403c4d7`  |
| 1220   | No file  | `f7628403c4d7`  |
| 1217   | No file  | `f7628403c4d7`  |
| 1211   | No file  | `f7628403c4d7`  |
| 1210   | No file  | `f7628403c4d7`  |
| 1208   | No file  | `f7628403c4d7`  |
| 1203   | No file  | `f7628403c4d7`  |
| 1197   | No file  | `f7628403c4d7`  |
| 1194   | No file  | `f7628403c4d7`  |
| 1192   | No file  | `f7628403c4d7`  |
| 1187   | No file  | `f7628403c4d7`  |
| 1183   | No file  | `f7628403c4d7`  |
| 1177   | No file  | `f7628403c4d7`  |
| 1173   | No file  | `f7628403c4d7`  |
| 1167   | No file  | `f7628403c4d7`  |
| 1164   | No file  | `f7628403c4d7`  |
| 1156   | No file  | `f7628403c4d7`  |
| 1149   | No file  | `f7628403c4d7`  |
| 1144   | No file  | `f7628403c4d7`  |
| 1137   | No file  | `f7628403c4d7`  |
| 1132   | No file  | `f7628403c4d7`  |
| 1127   | No file  | `f7628403c4d7`  |
| 1122   | No file  | `f7628403c4d7`  |
| 1118   | No file  | `f7628403c4d7`  |
| 1114   | No file  | `f7628403c4d7`  |
| 1109   | No file  | `f7628403c4d7`  |
| 1102   | No file  | `f7628403c4d7`  |
| 1096   | No file  | `f7628403c4d7`  |
| 1088   | No file  | `f7628403c4d7`  |
| 1081   | No file  | `f7628403c4d7`  |
| 1076   | No file  | `f7628403c4d7`  |
| 1069   | No file  | `f7628403c4d7`  |
| 1064   | No file  | `f7628403c4d7`  |
| 1058   | No file  | `f7628403c4d7`  |
| 1051   | No file  | `f7628403c4d7`  |
| 1044   | No file  | `f7628403c4d7`  |
| 1036   | No file  | `f7628403c4d7`  |
| 1026   | No file  | `f7628403c4d7`  |
| 1016   | No file  | `f7628403c4d7`  |
| 1009   | No file  | `f7628403c4d7`  |
| 1005   | No file  | `f7628403c4d7`  |
| 1000   | No file  | `f7628403c4d7`  |
| 998    | No file  | `f7628403c4d7`  |
| 990    | No file  | `f7628403c4d7`  |
| 979    | No file  | `f7628403c4d7`  |
| 972    | No file  | `f7628403c4d7`  |
| 963    | No file  | `f7628403c4d7`  |
| 955    | No file  | `f7628403c4d7`  |
| 946    | No file  | `f7628403c4d7`  |
| 938    | No file  | `f7628403c4d7`  |
| 927    | No file  | `f7628403c4d7`  |
| 911    | No file  | `f7628403c4d7`  |
| 904    | No file  | `f7628403c4d7`  |
| 899    | No file  | `f7628403c4d7`  |
| 894    | No file  | `f7628403c4d7`  |
| 885    | No file  | `f7628403c4d7`  |
| 879    | No file  | `f7628403c4d7`  |
| 872    | No file  | `f7628403c4d7`  |
| 864    | No file  | `f7628403c4d7`  |
| 855    | No file  | `f7628403c4d7`  |
| 853    | No file  | `f7628403c4d7`  |
| 845    | No file  | `f7628403c4d7`  |
| 837    | No file  | `f7628403c4d7`  |
| 829    | No file  | `f7628403c4d7`  |
| 822    | No file  | `f7628403c4d7`  |
| 814    | No file  | `f7628403c4d7`  |
| 805    | No file  | `f7628403c4d7`  |
| 794    | No file  | `f7628403c4d7`  |
| 787    | No file  | `f7628403c4d7`  |
| 780    | No file  | `f7628403c4d7`  |
| 771    | No file  | `f7628403c4d7`  |
| 760    | No file  | `f7628403c4d7`  |
| 748    | No file  | `f7628403c4d7`  |
| 741    | No file  | `f7628403c4d7`  |
| 736    | No file  | `f7628403c4d7`  |
| 731    | No file  | `f7628403c4d7`  |
| 723    | No file  | `f7628403c4d7`  |
| 711    | No file  | `f7628403c4d7`  |
| 707    | No file  | `f7628403c4d7`  |
| 697    | No file  | `f7628403c4d7`  |
| 689    | No file  | `f7628403c4d7`  |
| 683    | No file  | `f7628403c4d7`  |
| 678    | No file  | `f7628403c4d7`  |
| 670    | No file  | `f7628403c4d7`  |
| 661    | No file  | `f7628403c4d7`  |
| 656    | No file  | `f7628403c4d7`  |
| 652    | No file  | `f7628403c4d7`  |
| 643    | No file  | `f7628403c4d7`  |
| 637    | No file  | `f7628403c4d7`  |
| 630    | No file  | `f7628403c4d7`  |
| 627    | No file  | `f7628403c4d7`  |
| 621    | No file  | `f7628403c4d7`  |
| 617    | No file  | `f7628403c4d7`  |
| 615    | No file  | `f7628403c4d7`  |
| 606    | No file  | `f7628403c4d7`  |
| 599    | No file  | `f7628403c4d7`  |
| 592    | No file  | `f7628403c4d7`  |
| 586    | No file  | `f7628403c4d7`  |
| 577    | No file  | `f7628403c4d7`  |
| 569    | No file  | `f7628403c4d7`  |
| 561    | No file  | `f7628403c4d7`  |
| 554    | No file  | `f7628403c4d7`  |
| 542    | No file  | `f7628403c4d7`  |
| 532    | No file  | `f7628403c4d7`  |
| 531    | No file  | `f7628403c4d7`  |
| 526    | No file  | `f7628403c4d7`  |
| 521    | No file  | `f7628403c4d7`  |
| 517    | No file  | `f7628403c4d7`  |
| 510    | No file  | `f7628403c4d7`  |
| 508    | No file  | `f7628403c4d7`  |
| 504    | No file  | `f7628403c4d7`  |
| 497    | No file  | `f7628403c4d7`  |
| 491    | No file  | `f7628403c4d7`  |
| 485    | No file  | `f7628403c4d7`  |
| 478    | No file  | `f7628403c4d7`  |
| 472    | No file  | `f7628403c4d7`  |
| 466    | No file  | `f7628403c4d7`  |
| 457    | No file  | `f7628403c4d7`  |
| 452    | No file  | `f7628403c4d7`  |
| 449    | No file  | `f7628403c4d7`  |
| 435    | No file  | `f7628403c4d7`  |

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
| `+0x12` | u8       | unknown_12      |                         | Always `1`; no `buff.dbss` byte matches, see Open Questions                    |
| `+0x13` | bytes[3] | unknown_13      |                         | Always `0`                                                                     |
| `+0x16` | u8       | remove_on_dead  | stats `remove_on_dead`  | `1` in 33,944 rows                                                             |
| `+0x17` | u8       | is_shown        | `is_shown`              | `1` in 12,766 rows                                                             |
| `+0x18` | u32      | unknown_18      | tail `unknown_02`       | `0` in 25,701 rows, `1` in 14,420, `2` in 4,562                                |
| `+0x1C` | u32      | icon_ref        | `icon_path`             | String table index; `1` (the empty string) in 29,357 rows                      |

### String Table (variable: 4 bytes + strings)

1,235 strings on client 3464, all distinct and all referenced. `effect_name_ref`
and `icon_ref` index the same table and share only the empty string: index 0
is `"0"`, index 1 is `""`, and every other entry is either an `effect_name`
value or an icon path.

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | 1,235 on client 3464 |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries  |

## Layout 1

Before client 3464 `buff_id` was a u16 and every later field sat 2 bytes
earlier. Only the Buff Row differs from Layout 2. Field names keep Layout
2's offsets, so `unknown_05` sits at `+0x03` here. The parser reads only
Layout 2.

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
| `+0x10` | u8       | unknown_12      |       |
| `+0x11` | bytes[3] | unknown_13      |       |
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

The named fields take the names of the `buff.dbss` fields they copy, which come from the 2016 `gc::BuffStaticStatus` and the `Buff_Table` of a private server on client 519 ([buff.dbss Field Names](buff_dbss.md#field-names)). `unknown_07`, `unknown_08`, `unknown_09` and `unknown_0c` sit in the `_isExtractable`, `_isUseAvatarMesh`, `_rangeType` and `_enchantFailType` places of the `_needEquipType` copy; no server column holds them and the matching `itemenchant.dbss` header bytes have no name either. `unknown_18` copies `buff.dbss` tail `unknown_02`, which matches no server column.

## Open Questions

### What does `unknown_12` hold?

It is `1` in every row and matches no `buff.dbss` byte in all rows. The
closest are stats `param_1_set` (`1` in 44,525 rows) and `unknown_7e` (`1` in 44,550),
so it may be one of those with the exceptions dropped, or a constant of the
compact format.
