# `simplesequence.bss` Format

## Purpose

A keyed table of 13-byte rows. Each u32 key is two u16 halves: the high
half groups the rows (238 groups, `1` to `424`, on client 3474) and the
low half numbers the rows of a group from `1` with no gap. Both halves
repeat in the row, and a last byte is `0` or `1` per group. No client Lua,
sheet or server text names the table, so what a group and its rows stand
for is open. The file is a u32 count and fixed rows, with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 2358 and later | 3483    | `simplesequence.bss` | 6,946 | 534 Row | 13        |

| Layout | File                 | Known           | Unknown         |
| ------ | -------------------- | --------------- | --------------- |
| 1      | `simplesequence.bss` | 2,140 B (30.8%) | 4,806 B (69.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `ef382e1a0c3b`  |
| 3482   | Layout 1             | `ef382e1a0c3b`  |
| 3474   | Layout 1             | `ef382e1a0c3b`  |
| 3473   | Layout 1             | `ef382e1a0c3b`  |
| 3464   | Layout 1             | `ef382e1a0c3b`  |
| 3458   | Layout 1             | `ef382e1a0c3b`  |
| 3454   | Layout 1             | `ef382e1a0c3b`  |
| 3444   | Layout 1             | `ef382e1a0c3b`  |
| 3435   | Layout 1             | `ef382e1a0c3b`  |
| 3426   | Layout 1             | `ef382e1a0c3b`  |
| 3418   | Layout 1             | `ef382e1a0c3b`  |
| 3412   | Layout 1             | `ef382e1a0c3b`  |
| 3402   | Layout 1             | `ef382e1a0c3b`  |
| 3396   | Layout 1             | `ef382e1a0c3b`  |
| 3387   | Layout 1             | `ef382e1a0c3b`  |
| 3381   | Layout 1             | `ef382e1a0c3b`  |
| 3373   | Layout 1             | `ef382e1a0c3b`  |
| 3364   | Layout 1             | `ef382e1a0c3b`  |
| 3356   | Layout 1             | `ef382e1a0c3b`  |
| 3349   | Layout 1             | `ef382e1a0c3b`  |
| 3342   | Layout 1             | `ef382e1a0c3b`  |
| 3335   | Layout 1             | `ef382e1a0c3b`  |
| 3326   | Layout 1             | `ef382e1a0c3b`  |
| 3321   | Layout 1             | `ef382e1a0c3b`  |
| 3314   | Layout 1             | `ef382e1a0c3b`  |
| 3303   | Layout 1             | `ef382e1a0c3b`  |
| 3302   | Layout 1             | `ef382e1a0c3b`  |
| 3293   | Layout 1             | `ef382e1a0c3b`  |
| 3283   | Layout 1             | `ef382e1a0c3b`  |
| 3275   | Layout 1             | `ef382e1a0c3b`  |
| 3267   | Layout 1             | `ef382e1a0c3b`  |
| 3258   | Layout 1             | `ef382e1a0c3b`  |
| 3251   | Layout 1             | `ef382e1a0c3b`  |
| 3242   | Layout 1             | `ef382e1a0c3b`  |
| 3235   | Layout 1             | `ef382e1a0c3b`  |
| 3229   | Layout 1             | `ef382e1a0c3b`  |
| 3212   | Layout 1             | `ef382e1a0c3b`  |
| 3203   | Layout 1             | `ef382e1a0c3b`  |
| 3193   | Layout 1             | `ef382e1a0c3b`  |
| 3186   | Layout 1             | `ef382e1a0c3b`  |
| 3177   | Layout 1             | `ef382e1a0c3b`  |
| 3169   | Layout 1             | `ef382e1a0c3b`  |
| 3158   | Layout 1             | `ef382e1a0c3b`  |
| 3151   | Layout 1             | `ef382e1a0c3b`  |
| 3144   | Layout 1             | `ef382e1a0c3b`  |
| 3133   | Layout 1             | `ef382e1a0c3b`  |
| 3125   | Layout 1             | `ef382e1a0c3b`  |
| 3118   | Layout 1             | `ef382e1a0c3b`  |
| 3111   | Layout 1             | `ef382e1a0c3b`  |
| 3103   | Layout 1             | `ef382e1a0c3b`  |
| 3095   | Layout 1             | `ef382e1a0c3b`  |
| 3086   | Layout 1             | `ef382e1a0c3b`  |
| 3072   | Layout 1             | `ef382e1a0c3b`  |
| 3062   | Layout 1             | `ef382e1a0c3b`  |
| 3052   | Layout 1             | `ef382e1a0c3b`  |
| 3045   | Layout 1             | `ef382e1a0c3b`  |
| 3037   | Layout 1             | `ef382e1a0c3b`  |
| 3030   | Layout 1             | `ef382e1a0c3b`  |
| 3021   | Layout 1             | `ef382e1a0c3b`  |
| 3012   | Layout 1             | `ef382e1a0c3b`  |
| 3002   | Layout 1             | `ef382e1a0c3b`  |
| 2995   | Layout 1             | `ef382e1a0c3b`  |
| 2987   | Layout 1             | `ef382e1a0c3b`  |
| 2978   | Layout 1             | `ef382e1a0c3b`  |
| 2970   | Layout 1             | `ef382e1a0c3b`  |
| 2959   | Layout 1             | `ef382e1a0c3b`  |
| 2951   | Layout 1             | `ef382e1a0c3b`  |
| 2942   | Layout 1             | `ef382e1a0c3b`  |
| 2935   | Layout 1             | `ef382e1a0c3b`  |
| 2932   | Layout 1             | `ef382e1a0c3b`  |
| 2923   | Layout 1             | `ef382e1a0c3b`  |
| 2919   | Layout 1             | `ef382e1a0c3b`  |
| 2907   | Layout 1             | `ef382e1a0c3b`  |
| 2900   | Layout 1             | `ef382e1a0c3b`  |
| 2891   | Layout 1             | `ef382e1a0c3b`  |
| 2882   | Layout 1             | `ef382e1a0c3b`  |
| 2872   | Layout 1             | `ef382e1a0c3b`  |
| 2863   | Layout 1             | `ef382e1a0c3b`  |
| 2855   | Layout 1             | `ef382e1a0c3b`  |
| 2849   | Layout 1             | `ef382e1a0c3b`  |
| 2844   | Layout 1             | `ef382e1a0c3b`  |
| 2834   | Layout 1             | `ef382e1a0c3b`  |
| 2825   | Layout 1             | `ef382e1a0c3b`  |
| 2819   | Layout 1             | `ef382e1a0c3b`  |
| 2811   | Layout 1             | `ef382e1a0c3b`  |
| 2803   | Layout 1             | `ef382e1a0c3b`  |
| 2794   | Layout 1             | `ef382e1a0c3b`  |
| 2783   | Layout 1             | `ef382e1a0c3b`  |
| 2774   | Layout 1             | `ef382e1a0c3b`  |
| 2765   | Layout 1             | `ef382e1a0c3b`  |
| 2756   | Layout 1             | `ef382e1a0c3b`  |
| 2750   | Layout 1             | `ef382e1a0c3b`  |
| 2743   | Layout 1             | `ef382e1a0c3b`  |
| 2736   | Layout 1             | `ef382e1a0c3b`  |
| 2726   | Layout 1             | `ef382e1a0c3b`  |
| 2717   | Layout 1             | `ef382e1a0c3b`  |
| 2709   | Layout 1             | `ef382e1a0c3b`  |
| 2703   | Layout 1             | `ef382e1a0c3b`  |
| 2695   | Layout 1             | `ef382e1a0c3b`  |
| 2684   | Layout 1             | `ef382e1a0c3b`  |
| 2672   | Layout 1             | `ef382e1a0c3b`  |
| 2665   | Layout 1             | `ef382e1a0c3b`  |
| 2657   | Layout 1             | `ef382e1a0c3b`  |
| 2649   | Layout 1             | `ef382e1a0c3b`  |
| 2644   | Layout 1             | `ef382e1a0c3b`  |
| 2637   | Layout 1             | `ef382e1a0c3b`  |
| 2629   | Layout 1             | `ef382e1a0c3b`  |
| 2619   | Layout 1             | `ef382e1a0c3b`  |
| 2612   | Layout 1             | `ef382e1a0c3b`  |
| 2606   | Layout 1             | `ef382e1a0c3b`  |
| 2602   | Layout 1             | `ef382e1a0c3b`  |
| 2601   | Layout 1             | `ef382e1a0c3b`  |
| 2592   | Layout 1             | `ef382e1a0c3b`  |
| 2583   | Layout 1             | `ef382e1a0c3b`  |
| 2575   | Layout 1             | `ef382e1a0c3b`  |
| 2567   | Layout 1             | `ef382e1a0c3b`  |
| 2560   | Layout 1             | `ef382e1a0c3b`  |
| 2553   | Layout 1             | `ef382e1a0c3b`  |
| 2545   | Layout 1             | `ef382e1a0c3b`  |
| 2538   | Layout 1             | `ef382e1a0c3b`  |
| 2529   | Layout 1             | `ef382e1a0c3b`  |
| 2519   | Layout 1             | `ef382e1a0c3b`  |
| 2513   | Layout 1             | `ef382e1a0c3b`  |
| 2510   | Layout 1             | `ef382e1a0c3b`  |
| 2507   | Layout 1             | `ef382e1a0c3b`  |
| 2503   | Layout 1             | `ef382e1a0c3b`  |
| 2498   | Layout 1             | `ef382e1a0c3b`  |
| 2492   | Layout 1             | `ef382e1a0c3b`  |
| 2487   | Layout 1             | `ef382e1a0c3b`  |
| 2480   | Layout 1             | `ef382e1a0c3b`  |
| 2474   | Layout 1             | `ef382e1a0c3b`  |
| 2468   | Layout 1             | `ef382e1a0c3b`  |
| 2460   | Layout 1             | `ef382e1a0c3b`  |
| 2453   | Layout 1             | `ef382e1a0c3b`  |
| 2444   | Layout 1             | `ef382e1a0c3b`  |
| 2438   | Layout 1             | `ef382e1a0c3b`  |
| 2434   | Layout 1             | `ef382e1a0c3b`  |
| 2429   | Layout 1             | `ef382e1a0c3b`  |
| 2421   | Layout 1             | `ef382e1a0c3b`  |
| 2414   | Layout 1             | `ef382e1a0c3b`  |
| 2407   | Layout 1             | `ef382e1a0c3b`  |
| 2401   | Layout 1             | `ef382e1a0c3b`  |
| 2397   | Layout 1             | `ef382e1a0c3b`  |
| 2393   | Layout 1             | `ef382e1a0c3b`  |
| 2384   | Layout 1             | `ef382e1a0c3b`  |
| 2378   | Layout 1             | `ef382e1a0c3b`  |
| 2372   | Layout 1             | `ef382e1a0c3b`  |
| 2358   | Layout 1             | `ef382e1a0c3b`  |
| 2352   | No documented layout | `ef382e1a0c3b`  |
| 2347   | No documented layout | `ef382e1a0c3b`  |
| 2343   | No documented layout | `ef382e1a0c3b`  |
| 2335   | No documented layout | `ef382e1a0c3b`  |
| 2327   | No documented layout | `ef382e1a0c3b`  |
| 2324   | No documented layout | `ef382e1a0c3b`  |
| 2319   | No documented layout | `ef382e1a0c3b`  |
| 2313   | No documented layout | `ef382e1a0c3b`  |
| 2308   | No documented layout | `ef382e1a0c3b`  |
| 2302   | No documented layout | `ef382e1a0c3b`  |
| 2295   | No documented layout | `ef382e1a0c3b`  |
| 2290   | No documented layout | `ef382e1a0c3b`  |
| 2284   | No documented layout | `ef382e1a0c3b`  |
| 2276   | No documented layout | `ef382e1a0c3b`  |
| 2269   | No documented layout | `ef382e1a0c3b`  |
| 2259   | No documented layout | `ef382e1a0c3b`  |
| 2250   | No documented layout | `ef382e1a0c3b`  |
| 2243   | No documented layout | `ef382e1a0c3b`  |
| 2235   | No documented layout | `ef382e1a0c3b`  |
| 2229   | No file              | `ef382e1a0c3b`  |
| 2224   | No file              | `ef382e1a0c3b`  |
| 2218   | No file              | `ef382e1a0c3b`  |
| 2215   | No file              | `ef382e1a0c3b`  |
| 2207   | No file              | `ef382e1a0c3b`  |
| 2203   | No file              | `ef382e1a0c3b`  |
| 2196   | No file              | `ef382e1a0c3b`  |
| 2192   | No file              | `ef382e1a0c3b`  |
| 2189   | No file              | `ef382e1a0c3b`  |
| 2183   | No file              | `ef382e1a0c3b`  |
| 2179   | No file              | `ef382e1a0c3b`  |
| 2171   | No file              | `ef382e1a0c3b`  |
| 2163   | No file              | `ef382e1a0c3b`  |
| 2156   | No file              | `ef382e1a0c3b`  |
| 2151   | No file              | `ef382e1a0c3b`  |
| 2147   | No file              | `ef382e1a0c3b`  |
| 2142   | No file              | `ef382e1a0c3b`  |
| 2138   | No file              | `ef382e1a0c3b`  |
| 2134   | No file              | `ef382e1a0c3b`  |
| 2130   | No file              | `ef382e1a0c3b`  |
| 2122   | No file              | `ef382e1a0c3b`  |
| 2107   | No file              | `ef382e1a0c3b`  |
| 2098   | No file              | `ef382e1a0c3b`  |
| 2089   | No file              | `ef382e1a0c3b`  |
| 2081   | No file              | `ef382e1a0c3b`  |
| 2073   | No file              | `ef382e1a0c3b`  |
| 2067   | No file              | `ef382e1a0c3b`  |
| 2063   | No file              | `ef382e1a0c3b`  |
| 2059   | No file              | `ef382e1a0c3b`  |
| 2052   | No file              | `ef382e1a0c3b`  |
| 2044   | No file              | `ef382e1a0c3b`  |
| 2039   | No file              | `ef382e1a0c3b`  |
| 2032   | No file              | `ef382e1a0c3b`  |
| 2025   | No file              | `ef382e1a0c3b`  |
| 2011   | No file              | `ef382e1a0c3b`  |
| 2005   | No file              | `ef382e1a0c3b`  |
| 2000   | No file              | `ef382e1a0c3b`  |
| 1996   | No file              | `ef382e1a0c3b`  |
| 1991   | No file              | `ef382e1a0c3b`  |
| 1985   | No file              | `ef382e1a0c3b`  |
| 1980   | No file              | `ef382e1a0c3b`  |
| 1969   | No file              | `ef382e1a0c3b`  |
| 1964   | No file              | `ef382e1a0c3b`  |
| 1958   | No file              | `ef382e1a0c3b`  |
| 1950   | No file              | `ef382e1a0c3b`  |
| 1945   | No file              | `ef382e1a0c3b`  |
| 1937   | No file              | `ef382e1a0c3b`  |
| 1933   | No file              | `ef382e1a0c3b`  |
| 1927   | No file              | `ef382e1a0c3b`  |
| 1921   | No file              | `ef382e1a0c3b`  |
| 1914   | No file              | `ef382e1a0c3b`  |
| 1908   | No file              | `ef382e1a0c3b`  |
| 1897   | No file              | `ef382e1a0c3b`  |
| 1892   | No file              | `ef382e1a0c3b`  |
| 1886   | No file              | `ef382e1a0c3b`  |
| 1881   | No file              | `ef382e1a0c3b`  |
| 1871   | No file              | `ef382e1a0c3b`  |
| 1866   | No file              | `ef382e1a0c3b`  |
| 1862   | No file              | `ef382e1a0c3b`  |
| 1854   | No file              | `ef382e1a0c3b`  |
| 1846   | No file              | `ef382e1a0c3b`  |
| 1838   | No file              | `ef382e1a0c3b`  |
| 1832   | No file              | `ef382e1a0c3b`  |
| 1826   | No file              | `ef382e1a0c3b`  |
| 1822   | No file              | `ef382e1a0c3b`  |
| 1818   | No file              | `ef382e1a0c3b`  |
| 1804   | No file              | `ef382e1a0c3b`  |
| 1794   | No file              | `ef382e1a0c3b`  |
| 1790   | No file              | `ef382e1a0c3b`  |
| 1784   | No file              | `ef382e1a0c3b`  |
| 1774   | No file              | `ef382e1a0c3b`  |
| 1771   | No file              | `ef382e1a0c3b`  |
| 1762   | No file              | `ef382e1a0c3b`  |
| 1759   | No file              | `ef382e1a0c3b`  |
| 1754   | No file              | `ef382e1a0c3b`  |
| 1749   | No file              | `ef382e1a0c3b`  |
| 1743   | No file              | `ef382e1a0c3b`  |
| 1737   | No file              | `ef382e1a0c3b`  |
| 1731   | No file              | `ef382e1a0c3b`  |
| 1725   | No file              | `ef382e1a0c3b`  |
| 1717   | No file              | `ef382e1a0c3b`  |
| 1710   | No file              | `ef382e1a0c3b`  |
| 1704   | No file              | `ef382e1a0c3b`  |
| 1698   | No file              | `ef382e1a0c3b`  |
| 1690   | No file              | `ef382e1a0c3b`  |
| 1685   | No file              | `ef382e1a0c3b`  |
| 1680   | No file              | `ef382e1a0c3b`  |
| 1674   | No file              | `ef382e1a0c3b`  |
| 1668   | No file              | `ef382e1a0c3b`  |
| 1659   | No file              | `ef382e1a0c3b`  |
| 1649   | No file              | `ef382e1a0c3b`  |
| 1642   | No file              | `ef382e1a0c3b`  |
| 1636   | No file              | `ef382e1a0c3b`  |
| 1628   | No file              | `ef382e1a0c3b`  |
| 1622   | No file              | `ef382e1a0c3b`  |
| 1614   | No file              | `ef382e1a0c3b`  |
| 1608   | No file              | `ef382e1a0c3b`  |
| 1602   | No file              | `ef382e1a0c3b`  |
| 1598   | No file              | `ef382e1a0c3b`  |
| 1594   | No file              | `ef382e1a0c3b`  |
| 1590   | No file              | `ef382e1a0c3b`  |
| 1587   | No file              | `ef382e1a0c3b`  |
| 1584   | No file              | `ef382e1a0c3b`  |
| 1579   | No file              | `ef382e1a0c3b`  |
| 1572   | No file              | `ef382e1a0c3b`  |
| 1565   | No file              | `ef382e1a0c3b`  |
| 1559   | No file              | `ef382e1a0c3b`  |
| 1554   | No file              | `ef382e1a0c3b`  |
| 1547   | No file              | `ef382e1a0c3b`  |
| 1537   | No file              | `ef382e1a0c3b`  |
| 1529   | No file              | `ef382e1a0c3b`  |
| 1524   | No file              | `ef382e1a0c3b`  |
| 1519   | No file              | `ef382e1a0c3b`  |
| 1509   | No file              | `ef382e1a0c3b`  |
| 1506   | No file              | `ef382e1a0c3b`  |
| 1504   | No file              | `ef382e1a0c3b`  |
| 1500   | No file              | `ef382e1a0c3b`  |
| 1493   | No file              | `ef382e1a0c3b`  |
| 1489   | No file              | `ef382e1a0c3b`  |
| 1485   | No file              | `ef382e1a0c3b`  |
| 1481   | No file              | `ef382e1a0c3b`  |
| 1474   | No file              | `ef382e1a0c3b`  |
| 1466   | No file              | `ef382e1a0c3b`  |
| 1462   | No file              | `ef382e1a0c3b`  |
| 1459   | No file              | `ef382e1a0c3b`  |
| 1453   | No file              | `ef382e1a0c3b`  |
| 1450   | No file              | `ef382e1a0c3b`  |
| 1445   | No file              | `ef382e1a0c3b`  |
| 1439   | No file              | `ef382e1a0c3b`  |
| 1433   | No file              | `ef382e1a0c3b`  |
| 1430   | No file              | `ef382e1a0c3b`  |
| 1426   | No file              | `ef382e1a0c3b`  |
| 1421   | No file              | `ef382e1a0c3b`  |
| 1417   | No file              | `ef382e1a0c3b`  |
| 1416   | No file              | `ef382e1a0c3b`  |
| 1409   | No file              | `ef382e1a0c3b`  |
| 1405   | No file              | `ef382e1a0c3b`  |
| 1401   | No file              | `ef382e1a0c3b`  |
| 1396   | No file              | `ef382e1a0c3b`  |
| 1391   | No file              | `ef382e1a0c3b`  |
| 1390   | No file              | `ef382e1a0c3b`  |
| 1386   | No file              | `ef382e1a0c3b`  |
| 1381   | No file              | `ef382e1a0c3b`  |
| 1379   | No file              | `ef382e1a0c3b`  |
| 1372   | No file              | `ef382e1a0c3b`  |
| 1366   | No file              | `ef382e1a0c3b`  |
| 1364   | No file              | `ef382e1a0c3b`  |
| 1363   | No file              | `ef382e1a0c3b`  |
| 1360   | No file              | `ef382e1a0c3b`  |
| 1358   | No file              | `ef382e1a0c3b`  |
| 1355   | No file              | `ef382e1a0c3b`  |
| 1351   | No file              | `ef382e1a0c3b`  |
| 1348   | No file              | `ef382e1a0c3b`  |
| 1346   | No file              | `ef382e1a0c3b`  |
| 1341   | No file              | `ef382e1a0c3b`  |
| 1340   | No file              | `ef382e1a0c3b`  |
| 1338   | No file              | `ef382e1a0c3b`  |
| 1335   | No file              | `ef382e1a0c3b`  |
| 1333   | No file              | `ef382e1a0c3b`  |
| 1329   | No file              | `ef382e1a0c3b`  |
| 1327   | No file              | `ef382e1a0c3b`  |
| 1324   | No file              | `ef382e1a0c3b`  |
| 1321   | No file              | `ef382e1a0c3b`  |
| 1319   | No file              | `ef382e1a0c3b`  |
| 1318   | No file              | `ef382e1a0c3b`  |
| 1316   | No file              | `ef382e1a0c3b`  |
| 1313   | No file              | `ef382e1a0c3b`  |
| 1311   | No file              | `ef382e1a0c3b`  |
| 1309   | No file              | `ef382e1a0c3b`  |
| 1304   | No file              | `ef382e1a0c3b`  |
| 1292   | No file              | `ef382e1a0c3b`  |
| 1286   | No file              | `ef382e1a0c3b`  |
| 1280   | No file              | `ef382e1a0c3b`  |
| 1276   | No file              | `ef382e1a0c3b`  |
| 1267   | No file              | `ef382e1a0c3b`  |
| 1261   | No file              | `ef382e1a0c3b`  |
| 1256   | No file              | `ef382e1a0c3b`  |
| 1250   | No file              | `ef382e1a0c3b`  |
| 1246   | No file              | `ef382e1a0c3b`  |
| 1239   | No file              | `ef382e1a0c3b`  |
| 1230   | No file              | `ef382e1a0c3b`  |
| 1226   | No file              | `ef382e1a0c3b`  |
| 1220   | No file              | `ef382e1a0c3b`  |
| 1217   | No file              | `ef382e1a0c3b`  |
| 1211   | No file              | `ef382e1a0c3b`  |
| 1210   | No file              | `ef382e1a0c3b`  |
| 1208   | No file              | `ef382e1a0c3b`  |
| 1203   | No file              | `ef382e1a0c3b`  |
| 1197   | No file              | `ef382e1a0c3b`  |
| 1194   | No file              | `ef382e1a0c3b`  |
| 1192   | No file              | `ef382e1a0c3b`  |
| 1187   | No file              | `ef382e1a0c3b`  |
| 1183   | No file              | `ef382e1a0c3b`  |
| 1177   | No file              | `ef382e1a0c3b`  |
| 1173   | No file              | `ef382e1a0c3b`  |
| 1167   | No file              | `ef382e1a0c3b`  |
| 1164   | No file              | `ef382e1a0c3b`  |
| 1156   | No file              | `ef382e1a0c3b`  |
| 1149   | No file              | `ef382e1a0c3b`  |
| 1144   | No file              | `ef382e1a0c3b`  |
| 1137   | No file              | `ef382e1a0c3b`  |
| 1132   | No file              | `ef382e1a0c3b`  |
| 1127   | No file              | `ef382e1a0c3b`  |
| 1122   | No file              | `ef382e1a0c3b`  |
| 1118   | No file              | `ef382e1a0c3b`  |
| 1114   | No file              | `ef382e1a0c3b`  |
| 1109   | No file              | `ef382e1a0c3b`  |
| 1102   | No file              | `ef382e1a0c3b`  |
| 1096   | No file              | `ef382e1a0c3b`  |
| 1088   | No file              | `ef382e1a0c3b`  |
| 1081   | No file              | `ef382e1a0c3b`  |
| 1076   | No file              | `ef382e1a0c3b`  |
| 1069   | No file              | `ef382e1a0c3b`  |
| 1064   | No file              | `ef382e1a0c3b`  |
| 1058   | No file              | `ef382e1a0c3b`  |
| 1051   | No file              | `ef382e1a0c3b`  |
| 1044   | No file              | `ef382e1a0c3b`  |
| 1036   | No file              | `ef382e1a0c3b`  |
| 1026   | No file              | `ef382e1a0c3b`  |
| 1016   | No file              | `ef382e1a0c3b`  |
| 1009   | No file              | `ef382e1a0c3b`  |
| 1005   | No file              | `ef382e1a0c3b`  |
| 1000   | No file              | `ef382e1a0c3b`  |
| 998    | No file              | `ef382e1a0c3b`  |
| 990    | No file              | `ef382e1a0c3b`  |
| 979    | No file              | `ef382e1a0c3b`  |
| 972    | No file              | `ef382e1a0c3b`  |
| 963    | No file              | `ef382e1a0c3b`  |
| 955    | No file              | `ef382e1a0c3b`  |
| 946    | No file              | `ef382e1a0c3b`  |
| 938    | No file              | `ef382e1a0c3b`  |
| 927    | No file              | `ef382e1a0c3b`  |
| 911    | No file              | `ef382e1a0c3b`  |
| 904    | No file              | `ef382e1a0c3b`  |
| 899    | No file              | `ef382e1a0c3b`  |
| 894    | No file              | `ef382e1a0c3b`  |
| 885    | No file              | `ef382e1a0c3b`  |
| 879    | No file              | `ef382e1a0c3b`  |
| 872    | No file              | `ef382e1a0c3b`  |
| 864    | No file              | `ef382e1a0c3b`  |
| 855    | No file              | `ef382e1a0c3b`  |
| 853    | No file              | `ef382e1a0c3b`  |
| 845    | No file              | `ef382e1a0c3b`  |
| 837    | No file              | `ef382e1a0c3b`  |
| 829    | No file              | `ef382e1a0c3b`  |
| 822    | No file              | `ef382e1a0c3b`  |
| 814    | No file              | `ef382e1a0c3b`  |
| 805    | No file              | `ef382e1a0c3b`  |
| 794    | No file              | `ef382e1a0c3b`  |
| 787    | No file              | `ef382e1a0c3b`  |
| 780    | No file              | `ef382e1a0c3b`  |
| 771    | No file              | `ef382e1a0c3b`  |
| 760    | No file              | `ef382e1a0c3b`  |
| 748    | No file              | `ef382e1a0c3b`  |
| 741    | No file              | `ef382e1a0c3b`  |
| 736    | No file              | `ef382e1a0c3b`  |
| 731    | No file              | `ef382e1a0c3b`  |
| 723    | No file              | `ef382e1a0c3b`  |
| 711    | No file              | `ef382e1a0c3b`  |
| 707    | No file              | `ef382e1a0c3b`  |
| 697    | No file              | `ef382e1a0c3b`  |
| 689    | No file              | `ef382e1a0c3b`  |
| 683    | No file              | `ef382e1a0c3b`  |
| 678    | No file              | `ef382e1a0c3b`  |
| 670    | No file              | `ef382e1a0c3b`  |
| 661    | No file              | `ef382e1a0c3b`  |
| 656    | No file              | `ef382e1a0c3b`  |
| 652    | No file              | `ef382e1a0c3b`  |
| 643    | No file              | `ef382e1a0c3b`  |
| 637    | No file              | `ef382e1a0c3b`  |
| 630    | No file              | `ef382e1a0c3b`  |
| 627    | No file              | `ef382e1a0c3b`  |
| 621    | No file              | `ef382e1a0c3b`  |
| 617    | No file              | `ef382e1a0c3b`  |
| 615    | No file              | `ef382e1a0c3b`  |
| 606    | No file              | `ef382e1a0c3b`  |
| 599    | No file              | `ef382e1a0c3b`  |
| 592    | No file              | `ef382e1a0c3b`  |
| 586    | No file              | `ef382e1a0c3b`  |
| 577    | No file              | `ef382e1a0c3b`  |
| 569    | No file              | `ef382e1a0c3b`  |
| 561    | No file              | `ef382e1a0c3b`  |
| 554    | No file              | `ef382e1a0c3b`  |
| 542    | No file              | `ef382e1a0c3b`  |
| 532    | No file              | `ef382e1a0c3b`  |
| 531    | No file              | `ef382e1a0c3b`  |
| 526    | No file              | `ef382e1a0c3b`  |
| 521    | No file              | `ef382e1a0c3b`  |
| 517    | No file              | `ef382e1a0c3b`  |
| 510    | No file              | `ef382e1a0c3b`  |
| 508    | No file              | `ef382e1a0c3b`  |
| 504    | No file              | `ef382e1a0c3b`  |
| 497    | No file              | `ef382e1a0c3b`  |
| 491    | No file              | `ef382e1a0c3b`  |
| 485    | No file              | `ef382e1a0c3b`  |
| 478    | No file              | `ef382e1a0c3b`  |
| 472    | No file              | `ef382e1a0c3b`  |
| 466    | No file              | `ef382e1a0c3b`  |
| 457    | No file              | `ef382e1a0c3b`  |
| 452    | No file              | `ef382e1a0c3b`  |
| 449    | No file              | `ef382e1a0c3b`  |
| 435    | No file              | `ef382e1a0c3b`  |

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

### Row (13 bytes)

| Offset  | Type | Field      | Notes                                                       |
| ------- | ---- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32  | key        | Unique; high u16 the group, low u16 the row in the group     |
| `+0x04` | u16  | unknown_04 | The key's low half                                          |
| `+0x06` | u16  | unknown_06 | The key's high half                                         |
| `+0x08` | u16  | unknown_08 | The key's high half                                         |
| `+0x0A` | u16  | unknown_0a | The key's low half                                          |
| `+0x0C` | u8   | unknown_0c | `0` or `1`; the same on every row of a group (client 3474)   |

The rows of a group sit together; neither the groups nor the rows within
a group are sorted by key (the file opens `0x00AD0002`, `0x00AD0001`,
`0x00AC0004`).

## Groups

On client 3474 the 534 rows form 238 groups: 86 of one row, 83 of two, 35
of three, 22 of four and 12 larger ones up to 22 rows (group `11` has 14,
the largest 22). `unknown_0c` is `0` on all rows of 53 groups (`1` to `40`,
`400` to `407` and `420` to `424`) and `1` on all rows of the other 185.

## Notes

- The file is not in client 1784. The 2016 client's debug symbols, the
  sheets of a private server's `DataSheets.bexcel` on client 1784 and its
  server dump hold no `SimpleSequence` name; the only `sequence` sheet
  column there is `sequenceFilePath` of `Emoticon_Table`.
- The client Lua plays cutscenes ("sequences") through `ToClient_*Sequence*`
  calls such as `ToClient_isPlayingSequence`, none with a key.

## Open Questions

### What a Group Stands For

The key's high half (`1` to `424`, 238 values) and low half (`1` to N)
match no table read so far, and `unknown_0c` splits the groups into 53
and 185 by key ranges. Whether a group is a cutscene, a quest step chain or
something else is open.
