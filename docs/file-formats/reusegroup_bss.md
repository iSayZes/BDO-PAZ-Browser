# `reusegroup.bss` Format

## Purpose

The skill cooldown groups: skills that share a `ReuseGroup` share one
cooldown. A PABR list with one row per group key and a flag that is set
when the group's cooldown runs out while the player is offline. On client
3482 it holds 178 groups, `1` to `180` without `30` and `31`, and the
flag is set on ten of them; client 1784 holds `1` to `144`. The rows are
not in key order: they run down in blocks of up to 16 keys (`175` to
`160`, `180` to `176`, `143` to `128`, ...).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------- | --------- |
| 2      | 3242 and later | 3483    | `reusegroup.bss` | 910   | 178 Row | 5         |
| 1      | 1187 to 3235   | 3235    | `reusegroup.bss` | 562   | 180 Row | 3         |

| Layout | File             | Known          | Unknown    |
| ------ | ---------------- | -------------- | ---------- |
| 2      | `reusegroup.bss` | 910 B (100.0%) | 0 B (0.0%) |
| 1      | `reusegroup.bss` | 560 B (99.6%)  | 2 B (0.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `2db35a81d57d`  |
| 3482   | Layout 2 | `2db35a81d57d`  |
| 3474   | Layout 2 | `2db35a81d57d`  |
| 3473   | Layout 2 | `2db35a81d57d`  |
| 3464   | Layout 2 | `2db35a81d57d`  |
| 3458   | Layout 2 | `2db35a81d57d`  |
| 3454   | Layout 2 | `2db35a81d57d`  |
| 3444   | Layout 2 | `2db35a81d57d`  |
| 3435   | Layout 2 | `2db35a81d57d`  |
| 3426   | Layout 2 | `2db35a81d57d`  |
| 3418   | Layout 2 | `2db35a81d57d`  |
| 3412   | Layout 2 | `2db35a81d57d`  |
| 3402   | Layout 2 | `2db35a81d57d`  |
| 3396   | Layout 2 | `2db35a81d57d`  |
| 3387   | Layout 2 | `2db35a81d57d`  |
| 3381   | Layout 2 | `2db35a81d57d`  |
| 3373   | Layout 2 | `2db35a81d57d`  |
| 3364   | Layout 2 | `2db35a81d57d`  |
| 3356   | Layout 2 | `2db35a81d57d`  |
| 3349   | Layout 2 | `2db35a81d57d`  |
| 3342   | Layout 2 | `2db35a81d57d`  |
| 3335   | Layout 2 | `2db35a81d57d`  |
| 3326   | Layout 2 | `2db35a81d57d`  |
| 3321   | Layout 2 | `2db35a81d57d`  |
| 3314   | Layout 2 | `2db35a81d57d`  |
| 3303   | Layout 2 | `2db35a81d57d`  |
| 3302   | Layout 2 | `2db35a81d57d`  |
| 3293   | Layout 2 | `2db35a81d57d`  |
| 3283   | Layout 2 | `2db35a81d57d`  |
| 3275   | Layout 2 | `2db35a81d57d`  |
| 3267   | Layout 2 | `2db35a81d57d`  |
| 3258   | Layout 2 | `2db35a81d57d`  |
| 3251   | Layout 2 | `2db35a81d57d`  |
| 3242   | Layout 2 | `2db35a81d57d`  |
| 3235   | Layout 1 | `2db35a81d57d`  |
| 3229   | Layout 1 | `2db35a81d57d`  |
| 3212   | Layout 1 | `2db35a81d57d`  |
| 3203   | Layout 1 | `2db35a81d57d`  |
| 3193   | Layout 1 | `2db35a81d57d`  |
| 3186   | Layout 1 | `2db35a81d57d`  |
| 3177   | Layout 1 | `2db35a81d57d`  |
| 3169   | Layout 1 | `2db35a81d57d`  |
| 3158   | Layout 1 | `2db35a81d57d`  |
| 3151   | Layout 1 | `2db35a81d57d`  |
| 3144   | Layout 1 | `2db35a81d57d`  |
| 3133   | Layout 1 | `2db35a81d57d`  |
| 3125   | Layout 1 | `2db35a81d57d`  |
| 3118   | Layout 1 | `2db35a81d57d`  |
| 3111   | Layout 1 | `2db35a81d57d`  |
| 3103   | Layout 1 | `2db35a81d57d`  |
| 3095   | Layout 1 | `2db35a81d57d`  |
| 3086   | Layout 1 | `2db35a81d57d`  |
| 3072   | Layout 1 | `2db35a81d57d`  |
| 3062   | Layout 1 | `2db35a81d57d`  |
| 3052   | Layout 1 | `2db35a81d57d`  |
| 3045   | Layout 1 | `2db35a81d57d`  |
| 3037   | Layout 1 | `2db35a81d57d`  |
| 3030   | Layout 1 | `2db35a81d57d`  |
| 3021   | Layout 1 | `2db35a81d57d`  |
| 3012   | Layout 1 | `2db35a81d57d`  |
| 3002   | Layout 1 | `2db35a81d57d`  |
| 2995   | Layout 1 | `2db35a81d57d`  |
| 2987   | Layout 1 | `2db35a81d57d`  |
| 2978   | Layout 1 | `2db35a81d57d`  |
| 2970   | Layout 1 | `2db35a81d57d`  |
| 2959   | Layout 1 | `2db35a81d57d`  |
| 2951   | Layout 1 | `2db35a81d57d`  |
| 2942   | Layout 1 | `2db35a81d57d`  |
| 2935   | Layout 1 | `2db35a81d57d`  |
| 2932   | Layout 1 | `2db35a81d57d`  |
| 2923   | Layout 1 | `2db35a81d57d`  |
| 2919   | Layout 1 | `2db35a81d57d`  |
| 2907   | Layout 1 | `2db35a81d57d`  |
| 2900   | Layout 1 | `2db35a81d57d`  |
| 2891   | Layout 1 | `2db35a81d57d`  |
| 2882   | Layout 1 | `2db35a81d57d`  |
| 2872   | Layout 1 | `2db35a81d57d`  |
| 2863   | Layout 1 | `2db35a81d57d`  |
| 2855   | Layout 1 | `2db35a81d57d`  |
| 2849   | Layout 1 | `2db35a81d57d`  |
| 2844   | Layout 1 | `2db35a81d57d`  |
| 2834   | Layout 1 | `2db35a81d57d`  |
| 2825   | Layout 1 | `2db35a81d57d`  |
| 2819   | Layout 1 | `2db35a81d57d`  |
| 2811   | Layout 1 | `2db35a81d57d`  |
| 2803   | Layout 1 | `2db35a81d57d`  |
| 2794   | Layout 1 | `2db35a81d57d`  |
| 2783   | Layout 1 | `2db35a81d57d`  |
| 2774   | Layout 1 | `2db35a81d57d`  |
| 2765   | Layout 1 | `2db35a81d57d`  |
| 2756   | Layout 1 | `2db35a81d57d`  |
| 2750   | Layout 1 | `2db35a81d57d`  |
| 2743   | Layout 1 | `2db35a81d57d`  |
| 2736   | Layout 1 | `2db35a81d57d`  |
| 2726   | Layout 1 | `2db35a81d57d`  |
| 2717   | Layout 1 | `2db35a81d57d`  |
| 2709   | Layout 1 | `2db35a81d57d`  |
| 2703   | Layout 1 | `2db35a81d57d`  |
| 2695   | Layout 1 | `2db35a81d57d`  |
| 2684   | Layout 1 | `2db35a81d57d`  |
| 2672   | Layout 1 | `2db35a81d57d`  |
| 2665   | Layout 1 | `2db35a81d57d`  |
| 2657   | Layout 1 | `2db35a81d57d`  |
| 2649   | Layout 1 | `2db35a81d57d`  |
| 2644   | Layout 1 | `2db35a81d57d`  |
| 2637   | Layout 1 | `2db35a81d57d`  |
| 2629   | Layout 1 | `2db35a81d57d`  |
| 2619   | Layout 1 | `2db35a81d57d`  |
| 2612   | Layout 1 | `2db35a81d57d`  |
| 2606   | Layout 1 | `2db35a81d57d`  |
| 2602   | Layout 1 | `2db35a81d57d`  |
| 2601   | Layout 1 | `2db35a81d57d`  |
| 2592   | Layout 1 | `2db35a81d57d`  |
| 2583   | Layout 1 | `2db35a81d57d`  |
| 2575   | Layout 1 | `2db35a81d57d`  |
| 2567   | Layout 1 | `2db35a81d57d`  |
| 2560   | Layout 1 | `2db35a81d57d`  |
| 2553   | Layout 1 | `2db35a81d57d`  |
| 2545   | Layout 1 | `2db35a81d57d`  |
| 2538   | Layout 1 | `2db35a81d57d`  |
| 2529   | Layout 1 | `2db35a81d57d`  |
| 2519   | Layout 1 | `2db35a81d57d`  |
| 2513   | Layout 1 | `2db35a81d57d`  |
| 2510   | Layout 1 | `2db35a81d57d`  |
| 2507   | Layout 1 | `2db35a81d57d`  |
| 2503   | Layout 1 | `2db35a81d57d`  |
| 2498   | Layout 1 | `2db35a81d57d`  |
| 2492   | Layout 1 | `2db35a81d57d`  |
| 2487   | Layout 1 | `2db35a81d57d`  |
| 2480   | Layout 1 | `2db35a81d57d`  |
| 2474   | Layout 1 | `2db35a81d57d`  |
| 2468   | Layout 1 | `2db35a81d57d`  |
| 2460   | Layout 1 | `2db35a81d57d`  |
| 2453   | Layout 1 | `2db35a81d57d`  |
| 2444   | Layout 1 | `2db35a81d57d`  |
| 2438   | Layout 1 | `2db35a81d57d`  |
| 2434   | Layout 1 | `2db35a81d57d`  |
| 2429   | Layout 1 | `2db35a81d57d`  |
| 2421   | Layout 1 | `2db35a81d57d`  |
| 2414   | Layout 1 | `2db35a81d57d`  |
| 2407   | Layout 1 | `2db35a81d57d`  |
| 2401   | Layout 1 | `2db35a81d57d`  |
| 2397   | Layout 1 | `2db35a81d57d`  |
| 2393   | Layout 1 | `2db35a81d57d`  |
| 2384   | Layout 1 | `2db35a81d57d`  |
| 2378   | Layout 1 | `2db35a81d57d`  |
| 2372   | Layout 1 | `2db35a81d57d`  |
| 2358   | Layout 1 | `2db35a81d57d`  |
| 2352   | Layout 1 | `2db35a81d57d`  |
| 2347   | Layout 1 | `2db35a81d57d`  |
| 2343   | Layout 1 | `2db35a81d57d`  |
| 2335   | Layout 1 | `2db35a81d57d`  |
| 2327   | Layout 1 | `2db35a81d57d`  |
| 2324   | Layout 1 | `2db35a81d57d`  |
| 2319   | Layout 1 | `2db35a81d57d`  |
| 2313   | Layout 1 | `2db35a81d57d`  |
| 2308   | Layout 1 | `2db35a81d57d`  |
| 2302   | Layout 1 | `2db35a81d57d`  |
| 2295   | Layout 1 | `2db35a81d57d`  |
| 2290   | Layout 1 | `2db35a81d57d`  |
| 2284   | Layout 1 | `2db35a81d57d`  |
| 2276   | Layout 1 | `2db35a81d57d`  |
| 2269   | Layout 1 | `2db35a81d57d`  |
| 2259   | Layout 1 | `2db35a81d57d`  |
| 2250   | Layout 1 | `2db35a81d57d`  |
| 2243   | Layout 1 | `2db35a81d57d`  |
| 2235   | Layout 1 | `2db35a81d57d`  |
| 2229   | Layout 1 | `2db35a81d57d`  |
| 2224   | Layout 1 | `2db35a81d57d`  |
| 2218   | Layout 1 | `2db35a81d57d`  |
| 2215   | Layout 1 | `2db35a81d57d`  |
| 2207   | Layout 1 | `2db35a81d57d`  |
| 2203   | Layout 1 | `2db35a81d57d`  |
| 2196   | Layout 1 | `2db35a81d57d`  |
| 2192   | Layout 1 | `2db35a81d57d`  |
| 2189   | Layout 1 | `2db35a81d57d`  |
| 2183   | Layout 1 | `2db35a81d57d`  |
| 2179   | Layout 1 | `2db35a81d57d`  |
| 2171   | Layout 1 | `2db35a81d57d`  |
| 2163   | Layout 1 | `2db35a81d57d`  |
| 2156   | Layout 1 | `2db35a81d57d`  |
| 2151   | Layout 1 | `2db35a81d57d`  |
| 2147   | Layout 1 | `2db35a81d57d`  |
| 2142   | Layout 1 | `2db35a81d57d`  |
| 2138   | Layout 1 | `2db35a81d57d`  |
| 2134   | Layout 1 | `2db35a81d57d`  |
| 2130   | Layout 1 | `2db35a81d57d`  |
| 2122   | Layout 1 | `2db35a81d57d`  |
| 2107   | Layout 1 | `2db35a81d57d`  |
| 2098   | Layout 1 | `2db35a81d57d`  |
| 2089   | Layout 1 | `2db35a81d57d`  |
| 2081   | Layout 1 | `2db35a81d57d`  |
| 2073   | Layout 1 | `2db35a81d57d`  |
| 2067   | Layout 1 | `2db35a81d57d`  |
| 2063   | Layout 1 | `2db35a81d57d`  |
| 2059   | Layout 1 | `2db35a81d57d`  |
| 2052   | Layout 1 | `2db35a81d57d`  |
| 2044   | Layout 1 | `2db35a81d57d`  |
| 2039   | Layout 1 | `2db35a81d57d`  |
| 2032   | Layout 1 | `2db35a81d57d`  |
| 2025   | Layout 1 | `2db35a81d57d`  |
| 2011   | Layout 1 | `2db35a81d57d`  |
| 2005   | Layout 1 | `2db35a81d57d`  |
| 2000   | Layout 1 | `2db35a81d57d`  |
| 1996   | Layout 1 | `2db35a81d57d`  |
| 1991   | Layout 1 | `2db35a81d57d`  |
| 1985   | Layout 1 | `2db35a81d57d`  |
| 1980   | Layout 1 | `2db35a81d57d`  |
| 1969   | Layout 1 | `2db35a81d57d`  |
| 1964   | Layout 1 | `2db35a81d57d`  |
| 1958   | Layout 1 | `2db35a81d57d`  |
| 1950   | Layout 1 | `2db35a81d57d`  |
| 1945   | Layout 1 | `2db35a81d57d`  |
| 1937   | Layout 1 | `2db35a81d57d`  |
| 1933   | Layout 1 | `2db35a81d57d`  |
| 1927   | Layout 1 | `2db35a81d57d`  |
| 1921   | Layout 1 | `2db35a81d57d`  |
| 1914   | Layout 1 | `2db35a81d57d`  |
| 1908   | Layout 1 | `2db35a81d57d`  |
| 1897   | Layout 1 | `2db35a81d57d`  |
| 1892   | Layout 1 | `2db35a81d57d`  |
| 1886   | Layout 1 | `2db35a81d57d`  |
| 1881   | Layout 1 | `2db35a81d57d`  |
| 1871   | Layout 1 | `2db35a81d57d`  |
| 1866   | Layout 1 | `2db35a81d57d`  |
| 1862   | Layout 1 | `2db35a81d57d`  |
| 1854   | Layout 1 | `2db35a81d57d`  |
| 1846   | Layout 1 | `2db35a81d57d`  |
| 1838   | Layout 1 | `2db35a81d57d`  |
| 1832   | Layout 1 | `2db35a81d57d`  |
| 1826   | Layout 1 | `2db35a81d57d`  |
| 1822   | Layout 1 | `2db35a81d57d`  |
| 1818   | Layout 1 | `2db35a81d57d`  |
| 1804   | Layout 1 | `2db35a81d57d`  |
| 1794   | Layout 1 | `2db35a81d57d`  |
| 1790   | Layout 1 | `2db35a81d57d`  |
| 1784   | Layout 1 | `2db35a81d57d`  |
| 1774   | Layout 1 | `2db35a81d57d`  |
| 1771   | Layout 1 | `2db35a81d57d`  |
| 1762   | Layout 1 | `2db35a81d57d`  |
| 1759   | Layout 1 | `2db35a81d57d`  |
| 1754   | Layout 1 | `2db35a81d57d`  |
| 1749   | Layout 1 | `2db35a81d57d`  |
| 1743   | Layout 1 | `2db35a81d57d`  |
| 1737   | Layout 1 | `2db35a81d57d`  |
| 1731   | Layout 1 | `2db35a81d57d`  |
| 1725   | Layout 1 | `2db35a81d57d`  |
| 1717   | Layout 1 | `2db35a81d57d`  |
| 1710   | Layout 1 | `2db35a81d57d`  |
| 1704   | Layout 1 | `2db35a81d57d`  |
| 1698   | Layout 1 | `2db35a81d57d`  |
| 1690   | Layout 1 | `2db35a81d57d`  |
| 1685   | Layout 1 | `2db35a81d57d`  |
| 1680   | Layout 1 | `2db35a81d57d`  |
| 1674   | Layout 1 | `2db35a81d57d`  |
| 1668   | Layout 1 | `2db35a81d57d`  |
| 1659   | Layout 1 | `2db35a81d57d`  |
| 1649   | Layout 1 | `2db35a81d57d`  |
| 1642   | Layout 1 | `2db35a81d57d`  |
| 1636   | Layout 1 | `2db35a81d57d`  |
| 1628   | Layout 1 | `2db35a81d57d`  |
| 1622   | Layout 1 | `2db35a81d57d`  |
| 1614   | Layout 1 | `2db35a81d57d`  |
| 1608   | Layout 1 | `2db35a81d57d`  |
| 1602   | Layout 1 | `2db35a81d57d`  |
| 1598   | Layout 1 | `2db35a81d57d`  |
| 1594   | Layout 1 | `2db35a81d57d`  |
| 1590   | Layout 1 | `2db35a81d57d`  |
| 1587   | Layout 1 | `2db35a81d57d`  |
| 1584   | Layout 1 | `2db35a81d57d`  |
| 1579   | Layout 1 | `2db35a81d57d`  |
| 1572   | Layout 1 | `2db35a81d57d`  |
| 1565   | Layout 1 | `2db35a81d57d`  |
| 1559   | Layout 1 | `2db35a81d57d`  |
| 1554   | Layout 1 | `2db35a81d57d`  |
| 1547   | Layout 1 | `2db35a81d57d`  |
| 1537   | Layout 1 | `2db35a81d57d`  |
| 1529   | Layout 1 | `2db35a81d57d`  |
| 1524   | Layout 1 | `2db35a81d57d`  |
| 1519   | Layout 1 | `2db35a81d57d`  |
| 1509   | Layout 1 | `2db35a81d57d`  |
| 1506   | Layout 1 | `2db35a81d57d`  |
| 1504   | Layout 1 | `2db35a81d57d`  |
| 1500   | Layout 1 | `2db35a81d57d`  |
| 1493   | Layout 1 | `2db35a81d57d`  |
| 1489   | Layout 1 | `2db35a81d57d`  |
| 1485   | Layout 1 | `2db35a81d57d`  |
| 1481   | Layout 1 | `2db35a81d57d`  |
| 1474   | Layout 1 | `2db35a81d57d`  |
| 1466   | Layout 1 | `2db35a81d57d`  |
| 1462   | Layout 1 | `2db35a81d57d`  |
| 1459   | Layout 1 | `2db35a81d57d`  |
| 1453   | Layout 1 | `2db35a81d57d`  |
| 1450   | Layout 1 | `2db35a81d57d`  |
| 1445   | Layout 1 | `2db35a81d57d`  |
| 1439   | Layout 1 | `2db35a81d57d`  |
| 1433   | Layout 1 | `2db35a81d57d`  |
| 1430   | Layout 1 | `2db35a81d57d`  |
| 1426   | Layout 1 | `2db35a81d57d`  |
| 1421   | Layout 1 | `2db35a81d57d`  |
| 1417   | Layout 1 | `2db35a81d57d`  |
| 1416   | Layout 1 | `2db35a81d57d`  |
| 1409   | Layout 1 | `2db35a81d57d`  |
| 1405   | Layout 1 | `2db35a81d57d`  |
| 1401   | Layout 1 | `2db35a81d57d`  |
| 1396   | Layout 1 | `2db35a81d57d`  |
| 1391   | Layout 1 | `2db35a81d57d`  |
| 1390   | Layout 1 | `2db35a81d57d`  |
| 1386   | Layout 1 | `2db35a81d57d`  |
| 1381   | Layout 1 | `2db35a81d57d`  |
| 1379   | Layout 1 | `2db35a81d57d`  |
| 1372   | Layout 1 | `2db35a81d57d`  |
| 1366   | Layout 1 | `2db35a81d57d`  |
| 1364   | Layout 1 | `2db35a81d57d`  |
| 1363   | Layout 1 | `2db35a81d57d`  |
| 1360   | Layout 1 | `2db35a81d57d`  |
| 1358   | Layout 1 | `2db35a81d57d`  |
| 1355   | Layout 1 | `2db35a81d57d`  |
| 1351   | Layout 1 | `2db35a81d57d`  |
| 1348   | Layout 1 | `2db35a81d57d`  |
| 1346   | Layout 1 | `2db35a81d57d`  |
| 1341   | Layout 1 | `2db35a81d57d`  |
| 1340   | Layout 1 | `2db35a81d57d`  |
| 1338   | Layout 1 | `2db35a81d57d`  |
| 1335   | Layout 1 | `2db35a81d57d`  |
| 1333   | Layout 1 | `2db35a81d57d`  |
| 1329   | Layout 1 | `2db35a81d57d`  |
| 1327   | Layout 1 | `2db35a81d57d`  |
| 1324   | Layout 1 | `2db35a81d57d`  |
| 1321   | Layout 1 | `2db35a81d57d`  |
| 1319   | Layout 1 | `2db35a81d57d`  |
| 1318   | Layout 1 | `2db35a81d57d`  |
| 1316   | Layout 1 | `2db35a81d57d`  |
| 1313   | Layout 1 | `2db35a81d57d`  |
| 1311   | Layout 1 | `2db35a81d57d`  |
| 1309   | Layout 1 | `2db35a81d57d`  |
| 1304   | Layout 1 | `2db35a81d57d`  |
| 1292   | Layout 1 | `2db35a81d57d`  |
| 1286   | Layout 1 | `2db35a81d57d`  |
| 1280   | Layout 1 | `2db35a81d57d`  |
| 1276   | Layout 1 | `2db35a81d57d`  |
| 1267   | Layout 1 | `2db35a81d57d`  |
| 1261   | Layout 1 | `2db35a81d57d`  |
| 1256   | Layout 1 | `2db35a81d57d`  |
| 1250   | Layout 1 | `2db35a81d57d`  |
| 1246   | Layout 1 | `2db35a81d57d`  |
| 1239   | Layout 1 | `2db35a81d57d`  |
| 1230   | Layout 1 | `2db35a81d57d`  |
| 1226   | Layout 1 | `2db35a81d57d`  |
| 1220   | Layout 1 | `2db35a81d57d`  |
| 1217   | Layout 1 | `2db35a81d57d`  |
| 1211   | Layout 1 | `2db35a81d57d`  |
| 1210   | Layout 1 | `2db35a81d57d`  |
| 1208   | Layout 1 | `2db35a81d57d`  |
| 1203   | Layout 1 | `2db35a81d57d`  |
| 1197   | Layout 1 | `2db35a81d57d`  |
| 1194   | Layout 1 | `2db35a81d57d`  |
| 1192   | Layout 1 | `2db35a81d57d`  |
| 1187   | Layout 1 | `2db35a81d57d`  |
| 1183   | No file  | `2db35a81d57d`  |
| 1177   | No file  | `2db35a81d57d`  |
| 1173   | No file  | `2db35a81d57d`  |
| 1167   | No file  | `2db35a81d57d`  |
| 1164   | No file  | `2db35a81d57d`  |
| 1156   | No file  | `2db35a81d57d`  |
| 1149   | No file  | `2db35a81d57d`  |
| 1144   | No file  | `2db35a81d57d`  |
| 1137   | No file  | `2db35a81d57d`  |
| 1132   | No file  | `2db35a81d57d`  |
| 1127   | No file  | `2db35a81d57d`  |
| 1122   | No file  | `2db35a81d57d`  |
| 1118   | No file  | `2db35a81d57d`  |
| 1114   | No file  | `2db35a81d57d`  |
| 1109   | No file  | `2db35a81d57d`  |
| 1102   | No file  | `2db35a81d57d`  |
| 1096   | No file  | `2db35a81d57d`  |
| 1088   | No file  | `2db35a81d57d`  |
| 1081   | No file  | `2db35a81d57d`  |
| 1076   | No file  | `2db35a81d57d`  |
| 1069   | No file  | `2db35a81d57d`  |
| 1064   | No file  | `2db35a81d57d`  |
| 1058   | No file  | `2db35a81d57d`  |
| 1051   | No file  | `2db35a81d57d`  |
| 1044   | No file  | `2db35a81d57d`  |
| 1036   | No file  | `2db35a81d57d`  |
| 1026   | No file  | `2db35a81d57d`  |
| 1016   | No file  | `2db35a81d57d`  |
| 1009   | No file  | `2db35a81d57d`  |
| 1005   | No file  | `2db35a81d57d`  |
| 1000   | No file  | `2db35a81d57d`  |
| 998    | No file  | `2db35a81d57d`  |
| 990    | No file  | `2db35a81d57d`  |
| 979    | No file  | `2db35a81d57d`  |
| 972    | No file  | `2db35a81d57d`  |
| 963    | No file  | `2db35a81d57d`  |
| 955    | No file  | `2db35a81d57d`  |
| 946    | No file  | `2db35a81d57d`  |
| 938    | No file  | `2db35a81d57d`  |
| 927    | No file  | `2db35a81d57d`  |
| 911    | No file  | `2db35a81d57d`  |
| 904    | No file  | `2db35a81d57d`  |
| 899    | No file  | `2db35a81d57d`  |
| 894    | No file  | `2db35a81d57d`  |
| 885    | No file  | `2db35a81d57d`  |
| 879    | No file  | `2db35a81d57d`  |
| 872    | No file  | `2db35a81d57d`  |
| 864    | No file  | `2db35a81d57d`  |
| 855    | No file  | `2db35a81d57d`  |
| 853    | No file  | `2db35a81d57d`  |
| 845    | No file  | `2db35a81d57d`  |
| 837    | No file  | `2db35a81d57d`  |
| 829    | No file  | `2db35a81d57d`  |
| 822    | No file  | `2db35a81d57d`  |
| 814    | No file  | `2db35a81d57d`  |
| 805    | No file  | `2db35a81d57d`  |
| 794    | No file  | `2db35a81d57d`  |
| 787    | No file  | `2db35a81d57d`  |
| 780    | No file  | `2db35a81d57d`  |
| 771    | No file  | `2db35a81d57d`  |
| 760    | No file  | `2db35a81d57d`  |
| 748    | No file  | `2db35a81d57d`  |
| 741    | No file  | `2db35a81d57d`  |
| 736    | No file  | `2db35a81d57d`  |
| 731    | No file  | `2db35a81d57d`  |
| 723    | No file  | `2db35a81d57d`  |
| 711    | No file  | `2db35a81d57d`  |
| 707    | No file  | `2db35a81d57d`  |
| 697    | No file  | `2db35a81d57d`  |
| 689    | No file  | `2db35a81d57d`  |
| 683    | No file  | `2db35a81d57d`  |
| 678    | No file  | `2db35a81d57d`  |
| 670    | No file  | `2db35a81d57d`  |
| 661    | No file  | `2db35a81d57d`  |
| 656    | No file  | `2db35a81d57d`  |
| 652    | No file  | `2db35a81d57d`  |
| 643    | No file  | `2db35a81d57d`  |
| 637    | No file  | `2db35a81d57d`  |
| 630    | No file  | `2db35a81d57d`  |
| 627    | No file  | `2db35a81d57d`  |
| 621    | No file  | `2db35a81d57d`  |
| 617    | No file  | `2db35a81d57d`  |
| 615    | No file  | `2db35a81d57d`  |
| 606    | No file  | `2db35a81d57d`  |
| 599    | No file  | `2db35a81d57d`  |
| 592    | No file  | `2db35a81d57d`  |
| 586    | No file  | `2db35a81d57d`  |
| 577    | No file  | `2db35a81d57d`  |
| 569    | No file  | `2db35a81d57d`  |
| 561    | No file  | `2db35a81d57d`  |
| 554    | No file  | `2db35a81d57d`  |
| 542    | No file  | `2db35a81d57d`  |
| 532    | No file  | `2db35a81d57d`  |
| 531    | No file  | `2db35a81d57d`  |
| 526    | No file  | `2db35a81d57d`  |
| 521    | No file  | `2db35a81d57d`  |
| 517    | No file  | `2db35a81d57d`  |
| 510    | No file  | `2db35a81d57d`  |
| 508    | No file  | `2db35a81d57d`  |
| 504    | No file  | `2db35a81d57d`  |
| 497    | No file  | `2db35a81d57d`  |
| 491    | No file  | `2db35a81d57d`  |
| 485    | No file  | `2db35a81d57d`  |
| 478    | No file  | `2db35a81d57d`  |
| 472    | No file  | `2db35a81d57d`  |
| 466    | No file  | `2db35a81d57d`  |
| 457    | No file  | `2db35a81d57d`  |
| 452    | No file  | `2db35a81d57d`  |
| 449    | No file  | `2db35a81d57d`  |
| 435    | No file  | `2db35a81d57d`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of groups                              |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (5 bytes)

| Offset  | Type | Field                 | Notes                                                          |
| ------- | ---- | --------------------- | -------------------------------------------------------------- |
| `+0x00` | u32  | reuse_group           | Group key, the `ReuseGroup` of the skills in the group; unique |
| `+0x04` | u8   | is_expired_in_offline | `1` when a skill of the group has `isExpiredInOffline` set     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### File Layout

| Offset              | Type           | Field              | Notes                                                       |
| ------------------- | -------------- | ------------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                                |
| `+0x04`             | u32            | row_count          | Number of groups                                            |
| `+0x08`             | Row[row_count] | rows               | See Row                                                     |
| `rows+0x00`         | u16            | unknown_after_rows | `144` on client 1784, equal to `row_count` and the top key  |
| `rows+0x02`         | String Table   | string_table       | See String Table                                            |
| `string_table+0x00` | u32            | table_start        | Offset of the string table, where `unknown_after_rows` ends |
| `string_table+0x04` | u32            | zero               | Always `0`                                                  |

### Row (3 bytes)

| Offset  | Type | Field                 | Notes                         |
| ------- | ---- | --------------------- | ----------------------------- |
| `+0x00` | u16  | reuse_group           | Group key                     |
| `+0x02` | u8   | is_expired_in_offline | Same as Layout 2              |

## Field Names

The `Skill_Table_New` sheet of a private server's `DataSheets.bexcel` on
client 1784 has a `ReuseGroup` column, and its server dump reads it next
to `ReuseCycle`, `IsGlobalCycle` and `isExpiredInOffline`. All 144 group
keys of the client 1784 file are `ReuseGroup` values of that sheet, so the
key is `reuse_group`. The flag matches `isExpiredInOffline` on 144 of 144
groups: it is `1` on the six groups where at least one skill of the group
sets `isExpiredInOffline` (`54`, `55`, `120`, `127`, `140`, `141`) and `0`
on every group where no skill does. `IsGlobalCycle` is `0` on every skill
of every group, so it does not place the flag.

## Notes

- On client 3482 the flag is set on groups `54`, `55`, `120`, `127`,
  `140`, `141`, `158`, `159`, `160` and `177`.
- Group `141` mixes skills with and without `isExpiredInOffline` on client
  1784 (3 of 9); the flag is `1`, so one set skill sets the group.
- The cooldown lengths (`ReuseCycle` on the sheet) stay in the skill
  tables; this file holds none.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`.

## Open Questions

### The u16 After the Rows of Layout 1

Layout 1 ends its rows with a u16 that is `144` on client 1784, both the
row count and the highest group key there, so the values cannot tell a
second count from a top key. Layout 2 no longer has it.
