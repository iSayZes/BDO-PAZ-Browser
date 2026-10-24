# `employeespawninfo.dbss` Format

## Purpose

Hire data of the sailors that wait in Velia, Port Epheria and Iliya Island (the client calls sailors "employees"). One row per sailor character `59053` to `59072`: its sailor ID in `employeestaticstatus.bss`, the `employeespawnposition.dbss` spots it can appear on, the item a hire costs, and the line the sailor says when it agrees to be hired or turns the player down. Companion `employeespawninfooffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | ---------------------------- | --------- |
| 1      | 1280 and later | 3483    | `employeespawninfo.dbss`       | 3,702 | 20 Hire Block, 20 Sailor Row | 44        |
| 1      | 1280 and later | 3483    | `employeespawninfooffset.dbss` | 204   | 20 Offset Row                | 10        |

| Layout | File                           | Known           | Unknown       |
| ------ | ------------------------------ | --------------- | ------------- |
| 1      | `employeespawninfo.dbss`       | 3,062 B (82.7%) | 640 B (17.3%) |
| 1      | `employeespawninfooffset.dbss` | 204 B (100.0%)  | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `1b290b0108e7`  |
| 3482   | Layout 1             | `1b290b0108e7`  |
| 3474   | Layout 1             | `1b290b0108e7`  |
| 3473   | Layout 1             | `1b290b0108e7`  |
| 3464   | Layout 1             | `1b290b0108e7`  |
| 3458   | Layout 1             | `1b290b0108e7`  |
| 3454   | Layout 1             | `1b290b0108e7`  |
| 3444   | Layout 1             | `1b290b0108e7`  |
| 3435   | Layout 1             | `1b290b0108e7`  |
| 3426   | Layout 1             | `1b290b0108e7`  |
| 3418   | Layout 1             | `1b290b0108e7`  |
| 3412   | Layout 1             | `1b290b0108e7`  |
| 3402   | Layout 1             | `1b290b0108e7`  |
| 3396   | Layout 1             | `1b290b0108e7`  |
| 3387   | Layout 1             | `1b290b0108e7`  |
| 3381   | Layout 1             | `1b290b0108e7`  |
| 3373   | Layout 1             | `1b290b0108e7`  |
| 3364   | Layout 1             | `1b290b0108e7`  |
| 3356   | Layout 1             | `1b290b0108e7`  |
| 3349   | Layout 1             | `1b290b0108e7`  |
| 3342   | Layout 1             | `1b290b0108e7`  |
| 3335   | Layout 1             | `1b290b0108e7`  |
| 3326   | Layout 1             | `1b290b0108e7`  |
| 3321   | Layout 1             | `1b290b0108e7`  |
| 3314   | Layout 1             | `1b290b0108e7`  |
| 3303   | Layout 1             | `1b290b0108e7`  |
| 3302   | Layout 1             | `1b290b0108e7`  |
| 3293   | Layout 1             | `1b290b0108e7`  |
| 3283   | Layout 1             | `1b290b0108e7`  |
| 3275   | Layout 1             | `1b290b0108e7`  |
| 3267   | Layout 1             | `1b290b0108e7`  |
| 3258   | Layout 1             | `1b290b0108e7`  |
| 3251   | Layout 1             | `1b290b0108e7`  |
| 3242   | Layout 1             | `1b290b0108e7`  |
| 3235   | Layout 1             | `1b290b0108e7`  |
| 3229   | Layout 1             | `1b290b0108e7`  |
| 3212   | Layout 1             | `1b290b0108e7`  |
| 3203   | Layout 1             | `1b290b0108e7`  |
| 3193   | Layout 1             | `1b290b0108e7`  |
| 3186   | Layout 1             | `1b290b0108e7`  |
| 3177   | Layout 1             | `1b290b0108e7`  |
| 3169   | Layout 1             | `1b290b0108e7`  |
| 3158   | Layout 1             | `1b290b0108e7`  |
| 3151   | Layout 1             | `1b290b0108e7`  |
| 3144   | Layout 1             | `1b290b0108e7`  |
| 3133   | Layout 1             | `1b290b0108e7`  |
| 3125   | Layout 1             | `1b290b0108e7`  |
| 3118   | Layout 1             | `1b290b0108e7`  |
| 3111   | Layout 1             | `1b290b0108e7`  |
| 3103   | Layout 1             | `1b290b0108e7`  |
| 3095   | Layout 1             | `1b290b0108e7`  |
| 3086   | Layout 1             | `1b290b0108e7`  |
| 3072   | Layout 1             | `1b290b0108e7`  |
| 3062   | Layout 1             | `1b290b0108e7`  |
| 3052   | Layout 1             | `1b290b0108e7`  |
| 3045   | Layout 1             | `1b290b0108e7`  |
| 3037   | Layout 1             | `1b290b0108e7`  |
| 3030   | Layout 1             | `1b290b0108e7`  |
| 3021   | Layout 1             | `1b290b0108e7`  |
| 3012   | Layout 1             | `1b290b0108e7`  |
| 3002   | Layout 1             | `1b290b0108e7`  |
| 2995   | Layout 1             | `1b290b0108e7`  |
| 2987   | Layout 1             | `1b290b0108e7`  |
| 2978   | Layout 1             | `1b290b0108e7`  |
| 2970   | Layout 1             | `1b290b0108e7`  |
| 2959   | Layout 1             | `1b290b0108e7`  |
| 2951   | Layout 1             | `1b290b0108e7`  |
| 2942   | Layout 1             | `1b290b0108e7`  |
| 2935   | Layout 1             | `1b290b0108e7`  |
| 2932   | Layout 1             | `1b290b0108e7`  |
| 2923   | Layout 1             | `1b290b0108e7`  |
| 2919   | Layout 1             | `1b290b0108e7`  |
| 2907   | Layout 1             | `1b290b0108e7`  |
| 2900   | Layout 1             | `1b290b0108e7`  |
| 2891   | Layout 1             | `1b290b0108e7`  |
| 2882   | Layout 1             | `1b290b0108e7`  |
| 2872   | Layout 1             | `1b290b0108e7`  |
| 2863   | Layout 1             | `1b290b0108e7`  |
| 2855   | Layout 1             | `1b290b0108e7`  |
| 2849   | Layout 1             | `1b290b0108e7`  |
| 2844   | Layout 1             | `1b290b0108e7`  |
| 2834   | Layout 1             | `1b290b0108e7`  |
| 2825   | Layout 1             | `1b290b0108e7`  |
| 2819   | Layout 1             | `1b290b0108e7`  |
| 2811   | Layout 1             | `1b290b0108e7`  |
| 2803   | Layout 1             | `1b290b0108e7`  |
| 2794   | Layout 1             | `1b290b0108e7`  |
| 2783   | Layout 1             | `1b290b0108e7`  |
| 2774   | Layout 1             | `1b290b0108e7`  |
| 2765   | Layout 1             | `1b290b0108e7`  |
| 2756   | Layout 1             | `1b290b0108e7`  |
| 2750   | Layout 1             | `1b290b0108e7`  |
| 2743   | Layout 1             | `1b290b0108e7`  |
| 2736   | Layout 1             | `1b290b0108e7`  |
| 2726   | Layout 1             | `1b290b0108e7`  |
| 2717   | Layout 1             | `1b290b0108e7`  |
| 2709   | Layout 1             | `1b290b0108e7`  |
| 2703   | Layout 1             | `1b290b0108e7`  |
| 2695   | Layout 1             | `1b290b0108e7`  |
| 2684   | Layout 1             | `1b290b0108e7`  |
| 2672   | Layout 1             | `1b290b0108e7`  |
| 2665   | Layout 1             | `1b290b0108e7`  |
| 2657   | Layout 1             | `1b290b0108e7`  |
| 2649   | Layout 1             | `1b290b0108e7`  |
| 2644   | Layout 1             | `1b290b0108e7`  |
| 2637   | Layout 1             | `1b290b0108e7`  |
| 2629   | Layout 1             | `1b290b0108e7`  |
| 2619   | Layout 1             | `1b290b0108e7`  |
| 2612   | Layout 1             | `1b290b0108e7`  |
| 2606   | Layout 1             | `1b290b0108e7`  |
| 2602   | Layout 1             | `1b290b0108e7`  |
| 2601   | Layout 1             | `1b290b0108e7`  |
| 2592   | Layout 1             | `1b290b0108e7`  |
| 2583   | Layout 1             | `1b290b0108e7`  |
| 2575   | Layout 1             | `1b290b0108e7`  |
| 2567   | Layout 1             | `1b290b0108e7`  |
| 2560   | Layout 1             | `1b290b0108e7`  |
| 2553   | Layout 1             | `1b290b0108e7`  |
| 2545   | Layout 1             | `1b290b0108e7`  |
| 2538   | Layout 1             | `1b290b0108e7`  |
| 2529   | Layout 1             | `1b290b0108e7`  |
| 2519   | Layout 1             | `1b290b0108e7`  |
| 2513   | Layout 1             | `1b290b0108e7`  |
| 2510   | Layout 1             | `1b290b0108e7`  |
| 2507   | Layout 1             | `1b290b0108e7`  |
| 2503   | Layout 1             | `1b290b0108e7`  |
| 2498   | Layout 1             | `1b290b0108e7`  |
| 2492   | Layout 1             | `1b290b0108e7`  |
| 2487   | Layout 1             | `1b290b0108e7`  |
| 2480   | Layout 1             | `1b290b0108e7`  |
| 2474   | Layout 1             | `1b290b0108e7`  |
| 2468   | Layout 1             | `1b290b0108e7`  |
| 2460   | Layout 1             | `1b290b0108e7`  |
| 2453   | Layout 1             | `1b290b0108e7`  |
| 2444   | Layout 1             | `1b290b0108e7`  |
| 2438   | Layout 1             | `1b290b0108e7`  |
| 2434   | Layout 1             | `1b290b0108e7`  |
| 2429   | Layout 1             | `1b290b0108e7`  |
| 2421   | Layout 1             | `1b290b0108e7`  |
| 2414   | Layout 1             | `1b290b0108e7`  |
| 2407   | Layout 1             | `1b290b0108e7`  |
| 2401   | Layout 1             | `1b290b0108e7`  |
| 2397   | Layout 1             | `1b290b0108e7`  |
| 2393   | Layout 1             | `1b290b0108e7`  |
| 2384   | Layout 1             | `1b290b0108e7`  |
| 2378   | Layout 1             | `1b290b0108e7`  |
| 2372   | Layout 1             | `1b290b0108e7`  |
| 2358   | Layout 1             | `1b290b0108e7`  |
| 2352   | Layout 1             | `1b290b0108e7`  |
| 2347   | Layout 1             | `1b290b0108e7`  |
| 2343   | Layout 1             | `1b290b0108e7`  |
| 2335   | Layout 1             | `1b290b0108e7`  |
| 2327   | Layout 1             | `1b290b0108e7`  |
| 2324   | Layout 1             | `1b290b0108e7`  |
| 2319   | Layout 1             | `1b290b0108e7`  |
| 2313   | Layout 1             | `1b290b0108e7`  |
| 2308   | Layout 1             | `1b290b0108e7`  |
| 2302   | Layout 1             | `1b290b0108e7`  |
| 2295   | Layout 1             | `1b290b0108e7`  |
| 2290   | Layout 1             | `1b290b0108e7`  |
| 2284   | Layout 1             | `1b290b0108e7`  |
| 2276   | Layout 1             | `1b290b0108e7`  |
| 2269   | Layout 1             | `1b290b0108e7`  |
| 2259   | Layout 1             | `1b290b0108e7`  |
| 2250   | Layout 1             | `1b290b0108e7`  |
| 2243   | Layout 1             | `1b290b0108e7`  |
| 2235   | Layout 1             | `1b290b0108e7`  |
| 2229   | Layout 1             | `1b290b0108e7`  |
| 2224   | Layout 1             | `1b290b0108e7`  |
| 2218   | Layout 1             | `1b290b0108e7`  |
| 2215   | Layout 1             | `1b290b0108e7`  |
| 2207   | Layout 1             | `1b290b0108e7`  |
| 2203   | Layout 1             | `1b290b0108e7`  |
| 2196   | Layout 1             | `1b290b0108e7`  |
| 2192   | Layout 1             | `1b290b0108e7`  |
| 2189   | Layout 1             | `1b290b0108e7`  |
| 2183   | Layout 1             | `1b290b0108e7`  |
| 2179   | Layout 1             | `1b290b0108e7`  |
| 2171   | Layout 1             | `1b290b0108e7`  |
| 2163   | Layout 1             | `1b290b0108e7`  |
| 2156   | Layout 1             | `1b290b0108e7`  |
| 2151   | Layout 1             | `1b290b0108e7`  |
| 2147   | Layout 1             | `1b290b0108e7`  |
| 2142   | Layout 1             | `1b290b0108e7`  |
| 2138   | Layout 1             | `1b290b0108e7`  |
| 2134   | Layout 1             | `1b290b0108e7`  |
| 2130   | Layout 1             | `1b290b0108e7`  |
| 2122   | Layout 1             | `1b290b0108e7`  |
| 2107   | Layout 1             | `1b290b0108e7`  |
| 2098   | Layout 1             | `1b290b0108e7`  |
| 2089   | Layout 1             | `1b290b0108e7`  |
| 2081   | Layout 1             | `1b290b0108e7`  |
| 2073   | Layout 1             | `1b290b0108e7`  |
| 2067   | Layout 1             | `1b290b0108e7`  |
| 2063   | Layout 1             | `1b290b0108e7`  |
| 2059   | Layout 1             | `1b290b0108e7`  |
| 2052   | Layout 1             | `1b290b0108e7`  |
| 2044   | Layout 1             | `1b290b0108e7`  |
| 2039   | Layout 1             | `1b290b0108e7`  |
| 2032   | Layout 1             | `1b290b0108e7`  |
| 2025   | Layout 1             | `1b290b0108e7`  |
| 2011   | Layout 1             | `1b290b0108e7`  |
| 2005   | Layout 1             | `1b290b0108e7`  |
| 2000   | Layout 1             | `1b290b0108e7`  |
| 1996   | Layout 1             | `1b290b0108e7`  |
| 1991   | Layout 1             | `1b290b0108e7`  |
| 1985   | Layout 1             | `1b290b0108e7`  |
| 1980   | Layout 1             | `1b290b0108e7`  |
| 1969   | Layout 1             | `1b290b0108e7`  |
| 1964   | Layout 1             | `1b290b0108e7`  |
| 1958   | Layout 1             | `1b290b0108e7`  |
| 1950   | Layout 1             | `1b290b0108e7`  |
| 1945   | Layout 1             | `1b290b0108e7`  |
| 1937   | Layout 1             | `1b290b0108e7`  |
| 1933   | Layout 1             | `1b290b0108e7`  |
| 1927   | Layout 1             | `1b290b0108e7`  |
| 1921   | Layout 1             | `1b290b0108e7`  |
| 1914   | Layout 1             | `1b290b0108e7`  |
| 1908   | Layout 1             | `1b290b0108e7`  |
| 1897   | Layout 1             | `1b290b0108e7`  |
| 1892   | Layout 1             | `1b290b0108e7`  |
| 1886   | Layout 1             | `1b290b0108e7`  |
| 1881   | Layout 1             | `1b290b0108e7`  |
| 1871   | Layout 1             | `1b290b0108e7`  |
| 1866   | Layout 1             | `1b290b0108e7`  |
| 1862   | Layout 1             | `1b290b0108e7`  |
| 1854   | Layout 1             | `1b290b0108e7`  |
| 1846   | Layout 1             | `1b290b0108e7`  |
| 1838   | Layout 1             | `1b290b0108e7`  |
| 1832   | Layout 1             | `1b290b0108e7`  |
| 1826   | Layout 1             | `1b290b0108e7`  |
| 1822   | Layout 1             | `1b290b0108e7`  |
| 1818   | Layout 1             | `1b290b0108e7`  |
| 1804   | Layout 1             | `1b290b0108e7`  |
| 1794   | Layout 1             | `1b290b0108e7`  |
| 1790   | Layout 1             | `1b290b0108e7`  |
| 1784   | Layout 1             | `1b290b0108e7`  |
| 1774   | Layout 1             | `1b290b0108e7`  |
| 1771   | Layout 1             | `1b290b0108e7`  |
| 1762   | Layout 1             | `1b290b0108e7`  |
| 1759   | Layout 1             | `1b290b0108e7`  |
| 1754   | Layout 1             | `1b290b0108e7`  |
| 1749   | Layout 1             | `1b290b0108e7`  |
| 1743   | Layout 1             | `1b290b0108e7`  |
| 1737   | Layout 1             | `1b290b0108e7`  |
| 1731   | Layout 1             | `1b290b0108e7`  |
| 1725   | Layout 1             | `1b290b0108e7`  |
| 1717   | Layout 1             | `1b290b0108e7`  |
| 1710   | Layout 1             | `1b290b0108e7`  |
| 1704   | Layout 1             | `1b290b0108e7`  |
| 1698   | Layout 1             | `1b290b0108e7`  |
| 1690   | Layout 1             | `1b290b0108e7`  |
| 1685   | Layout 1             | `1b290b0108e7`  |
| 1680   | Layout 1             | `1b290b0108e7`  |
| 1674   | Layout 1             | `1b290b0108e7`  |
| 1668   | Layout 1             | `1b290b0108e7`  |
| 1659   | Layout 1             | `1b290b0108e7`  |
| 1649   | Layout 1             | `1b290b0108e7`  |
| 1642   | Layout 1             | `1b290b0108e7`  |
| 1636   | Layout 1             | `1b290b0108e7`  |
| 1628   | Layout 1             | `1b290b0108e7`  |
| 1622   | Layout 1             | `1b290b0108e7`  |
| 1614   | Layout 1             | `1b290b0108e7`  |
| 1608   | Layout 1             | `1b290b0108e7`  |
| 1602   | Layout 1             | `1b290b0108e7`  |
| 1598   | Layout 1             | `1b290b0108e7`  |
| 1594   | Layout 1             | `1b290b0108e7`  |
| 1590   | Layout 1             | `1b290b0108e7`  |
| 1587   | Layout 1             | `1b290b0108e7`  |
| 1584   | Layout 1             | `1b290b0108e7`  |
| 1579   | Layout 1             | `1b290b0108e7`  |
| 1572   | Layout 1             | `1b290b0108e7`  |
| 1565   | Layout 1             | `1b290b0108e7`  |
| 1559   | Layout 1             | `1b290b0108e7`  |
| 1554   | Layout 1             | `1b290b0108e7`  |
| 1547   | Layout 1             | `1b290b0108e7`  |
| 1537   | Layout 1             | `1b290b0108e7`  |
| 1529   | Layout 1             | `1b290b0108e7`  |
| 1524   | Layout 1             | `1b290b0108e7`  |
| 1519   | Layout 1             | `1b290b0108e7`  |
| 1509   | Layout 1             | `1b290b0108e7`  |
| 1506   | Layout 1             | `1b290b0108e7`  |
| 1504   | Layout 1             | `1b290b0108e7`  |
| 1500   | Layout 1             | `1b290b0108e7`  |
| 1493   | Layout 1             | `1b290b0108e7`  |
| 1489   | Layout 1             | `1b290b0108e7`  |
| 1485   | Layout 1             | `1b290b0108e7`  |
| 1481   | Layout 1             | `1b290b0108e7`  |
| 1474   | Layout 1             | `1b290b0108e7`  |
| 1466   | Layout 1             | `1b290b0108e7`  |
| 1462   | Layout 1             | `1b290b0108e7`  |
| 1459   | Layout 1             | `1b290b0108e7`  |
| 1453   | Layout 1             | `1b290b0108e7`  |
| 1450   | Layout 1             | `1b290b0108e7`  |
| 1445   | Layout 1             | `1b290b0108e7`  |
| 1439   | Layout 1             | `1b290b0108e7`  |
| 1433   | Layout 1             | `1b290b0108e7`  |
| 1430   | Layout 1             | `1b290b0108e7`  |
| 1426   | Layout 1             | `1b290b0108e7`  |
| 1421   | Layout 1             | `1b290b0108e7`  |
| 1417   | Layout 1             | `1b290b0108e7`  |
| 1416   | Layout 1             | `1b290b0108e7`  |
| 1409   | Layout 1             | `1b290b0108e7`  |
| 1405   | Layout 1             | `1b290b0108e7`  |
| 1401   | Layout 1             | `1b290b0108e7`  |
| 1396   | Layout 1             | `1b290b0108e7`  |
| 1391   | Layout 1             | `1b290b0108e7`  |
| 1390   | Layout 1             | `1b290b0108e7`  |
| 1386   | Layout 1             | `1b290b0108e7`  |
| 1381   | Layout 1             | `1b290b0108e7`  |
| 1379   | Layout 1             | `1b290b0108e7`  |
| 1372   | Layout 1             | `1b290b0108e7`  |
| 1366   | Layout 1             | `1b290b0108e7`  |
| 1364   | Layout 1             | `1b290b0108e7`  |
| 1363   | Layout 1             | `1b290b0108e7`  |
| 1360   | Layout 1             | `1b290b0108e7`  |
| 1358   | Layout 1             | `1b290b0108e7`  |
| 1355   | Layout 1             | `1b290b0108e7`  |
| 1351   | Layout 1             | `1b290b0108e7`  |
| 1348   | Layout 1             | `1b290b0108e7`  |
| 1346   | Layout 1             | `1b290b0108e7`  |
| 1341   | Layout 1             | `1b290b0108e7`  |
| 1340   | Layout 1             | `1b290b0108e7`  |
| 1338   | Layout 1             | `1b290b0108e7`  |
| 1335   | Layout 1             | `1b290b0108e7`  |
| 1333   | Layout 1             | `1b290b0108e7`  |
| 1329   | Layout 1             | `1b290b0108e7`  |
| 1327   | Layout 1             | `1b290b0108e7`  |
| 1324   | Layout 1             | `1b290b0108e7`  |
| 1321   | Layout 1             | `1b290b0108e7`  |
| 1319   | Layout 1             | `1b290b0108e7`  |
| 1318   | Layout 1             | `1b290b0108e7`  |
| 1316   | Layout 1             | `1b290b0108e7`  |
| 1313   | Layout 1             | `1b290b0108e7`  |
| 1311   | Layout 1             | `1b290b0108e7`  |
| 1309   | Layout 1             | `1b290b0108e7`  |
| 1304   | Layout 1             | `1b290b0108e7`  |
| 1292   | Layout 1             | `1b290b0108e7`  |
| 1286   | Layout 1             | `1b290b0108e7`  |
| 1280   | Layout 1             | `1b290b0108e7`  |
| 1276   | No documented layout | `1b290b0108e7`  |
| 1267   | No documented layout | `1b290b0108e7`  |
| 1261   | No file              | `1b290b0108e7`  |
| 1256   | No file              | `1b290b0108e7`  |
| 1250   | No file              | `1b290b0108e7`  |
| 1246   | No file              | `1b290b0108e7`  |
| 1239   | No file              | `1b290b0108e7`  |
| 1230   | No file              | `1b290b0108e7`  |
| 1226   | No file              | `1b290b0108e7`  |
| 1220   | No file              | `1b290b0108e7`  |
| 1217   | No file              | `1b290b0108e7`  |
| 1211   | No file              | `1b290b0108e7`  |
| 1210   | No file              | `1b290b0108e7`  |
| 1208   | No file              | `1b290b0108e7`  |
| 1203   | No file              | `1b290b0108e7`  |
| 1197   | No file              | `1b290b0108e7`  |
| 1194   | No file              | `1b290b0108e7`  |
| 1192   | No file              | `1b290b0108e7`  |
| 1187   | No file              | `1b290b0108e7`  |
| 1183   | No file              | `1b290b0108e7`  |
| 1177   | No file              | `1b290b0108e7`  |
| 1173   | No file              | `1b290b0108e7`  |
| 1167   | No file              | `1b290b0108e7`  |
| 1164   | No file              | `1b290b0108e7`  |
| 1156   | No file              | `1b290b0108e7`  |
| 1149   | No file              | `1b290b0108e7`  |
| 1144   | No file              | `1b290b0108e7`  |
| 1137   | No file              | `1b290b0108e7`  |
| 1132   | No file              | `1b290b0108e7`  |
| 1127   | No file              | `1b290b0108e7`  |
| 1122   | No file              | `1b290b0108e7`  |
| 1118   | No file              | `1b290b0108e7`  |
| 1114   | No file              | `1b290b0108e7`  |
| 1109   | No file              | `1b290b0108e7`  |
| 1102   | No file              | `1b290b0108e7`  |
| 1096   | No file              | `1b290b0108e7`  |
| 1088   | No file              | `1b290b0108e7`  |
| 1081   | No file              | `1b290b0108e7`  |
| 1076   | No file              | `1b290b0108e7`  |
| 1069   | No file              | `1b290b0108e7`  |
| 1064   | No file              | `1b290b0108e7`  |
| 1058   | No file              | `1b290b0108e7`  |
| 1051   | No file              | `1b290b0108e7`  |
| 1044   | No file              | `1b290b0108e7`  |
| 1036   | No file              | `1b290b0108e7`  |
| 1026   | No file              | `1b290b0108e7`  |
| 1016   | No file              | `1b290b0108e7`  |
| 1009   | No file              | `1b290b0108e7`  |
| 1005   | No file              | `1b290b0108e7`  |
| 1000   | No file              | `1b290b0108e7`  |
| 998    | No file              | `1b290b0108e7`  |
| 990    | No file              | `1b290b0108e7`  |
| 979    | No file              | `1b290b0108e7`  |
| 972    | No file              | `1b290b0108e7`  |
| 963    | No file              | `1b290b0108e7`  |
| 955    | No file              | `1b290b0108e7`  |
| 946    | No file              | `1b290b0108e7`  |
| 938    | No file              | `1b290b0108e7`  |
| 927    | No file              | `1b290b0108e7`  |
| 911    | No file              | `1b290b0108e7`  |
| 904    | No file              | `1b290b0108e7`  |
| 899    | No file              | `1b290b0108e7`  |
| 894    | No file              | `1b290b0108e7`  |
| 885    | No file              | `1b290b0108e7`  |
| 879    | No file              | `1b290b0108e7`  |
| 872    | No file              | `1b290b0108e7`  |
| 864    | No file              | `1b290b0108e7`  |
| 855    | No file              | `1b290b0108e7`  |
| 853    | No file              | `1b290b0108e7`  |
| 845    | No file              | `1b290b0108e7`  |
| 837    | No file              | `1b290b0108e7`  |
| 829    | No file              | `1b290b0108e7`  |
| 822    | No file              | `1b290b0108e7`  |
| 814    | No file              | `1b290b0108e7`  |
| 805    | No file              | `1b290b0108e7`  |
| 794    | No file              | `1b290b0108e7`  |
| 787    | No file              | `1b290b0108e7`  |
| 780    | No file              | `1b290b0108e7`  |
| 771    | No file              | `1b290b0108e7`  |
| 760    | No file              | `1b290b0108e7`  |
| 748    | No file              | `1b290b0108e7`  |
| 741    | No file              | `1b290b0108e7`  |
| 736    | No file              | `1b290b0108e7`  |
| 731    | No file              | `1b290b0108e7`  |
| 723    | No file              | `1b290b0108e7`  |
| 711    | No file              | `1b290b0108e7`  |
| 707    | No file              | `1b290b0108e7`  |
| 697    | No file              | `1b290b0108e7`  |
| 689    | No file              | `1b290b0108e7`  |
| 683    | No file              | `1b290b0108e7`  |
| 678    | No file              | `1b290b0108e7`  |
| 670    | No file              | `1b290b0108e7`  |
| 661    | No file              | `1b290b0108e7`  |
| 656    | No file              | `1b290b0108e7`  |
| 652    | No file              | `1b290b0108e7`  |
| 643    | No file              | `1b290b0108e7`  |
| 637    | No file              | `1b290b0108e7`  |
| 630    | No file              | `1b290b0108e7`  |
| 627    | No file              | `1b290b0108e7`  |
| 621    | No file              | `1b290b0108e7`  |
| 617    | No file              | `1b290b0108e7`  |
| 615    | No file              | `1b290b0108e7`  |
| 606    | No file              | `1b290b0108e7`  |
| 599    | No file              | `1b290b0108e7`  |
| 592    | No file              | `1b290b0108e7`  |
| 586    | No file              | `1b290b0108e7`  |
| 577    | No file              | `1b290b0108e7`  |
| 569    | No file              | `1b290b0108e7`  |
| 561    | No file              | `1b290b0108e7`  |
| 554    | No file              | `1b290b0108e7`  |
| 542    | No file              | `1b290b0108e7`  |
| 532    | No file              | `1b290b0108e7`  |
| 531    | No file              | `1b290b0108e7`  |
| 526    | No file              | `1b290b0108e7`  |
| 521    | No file              | `1b290b0108e7`  |
| 517    | No file              | `1b290b0108e7`  |
| 510    | No file              | `1b290b0108e7`  |
| 508    | No file              | `1b290b0108e7`  |
| 504    | No file              | `1b290b0108e7`  |
| 497    | No file              | `1b290b0108e7`  |
| 491    | No file              | `1b290b0108e7`  |
| 485    | No file              | `1b290b0108e7`  |
| 478    | No file              | `1b290b0108e7`  |
| 472    | No file              | `1b290b0108e7`  |
| 466    | No file              | `1b290b0108e7`  |
| 457    | No file              | `1b290b0108e7`  |
| 452    | No file              | `1b290b0108e7`  |
| 449    | No file              | `1b290b0108e7`  |
| 435    | No file              | `1b290b0108e7`  |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                                     |
| ---------------------------------- | -------- | ------------------------------------------------------------------------ |
| `employeespawninfooffset.dbss`     | Required | `character_key -> (offset, size)` of every row                           |
| `employeespawnposition.dbss`       | Optional | Region of each spawn position, for the Towns column                       |
| `employeespawnpositionoffset.dbss` | Optional | Offset table of `employeespawnposition.dbss`                              |
| `languagedata_en.loc`              | Optional | Sailor name and title (type 6), accept and refuse lines (type 70), item name (type 0), region names (type 17) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type              | Field | Notes                                                       |
| ------- | ----------------- | ----- | ----------------------------------------------------------- |
| `+0x00` | u32               | count | Number of rows (observed: 20)                               |
| `+0x04` | Sailor Row[count] | rows  | `count` variable-length rows, read through the offset table |

The rows follow each other with no gap and end at the end of the file (3,702 bytes on client 3458).

### Sailor Row (variable: 74 bytes + spawn keys and text)

| Offset                     | Type             | Field                        | Notes                                                                           |
| -------------------------- | ---------------- | ---------------------------- | ------------------------------------------------------------------------------- |
| `+0x00`                    | u16              | character_key                | Row key; the sailor character, `59053` to `59072`                               |
| `+0x02`                    | u32              | employee_key                 | Sailor ID in `employeestaticstatus.bss` (`1` to `20`, the same character there) |
| `+0x06`                    | u32              | spawn_count                  | Number of spawn positions, `1` or `2`                                           |
| `+0x0A`                    | u32[spawn_count] | spawn_position_keys          | Keys of `employeespawnposition.dbss` rows                                       |
| `spawn_position_keys+0x00` | Hire Block       | hire                         | See Hire Block                                                                  |
| `spawn_position_keys+0x2C` | str16            | accept_text_kr               | Korean line when the sailor agrees to be hired; u64 length in UTF-16 units      |
| `accept_text_kr+0x00`      | str16            | refuse_text_kr               | Korean line when the sailor turns the player down                               |
| `refuse_text_kr+0x00`      | u32              | unknown_after_refuse_text_kr | Always `0`; the row ends after it                                               |

The inline text holds real line breaks (`0x0A`), not the `\n` escape of `buff.dbss` and `skill.dbss`.

Earlier versions of this doc called `unknown_after_refuse_text_kr` `terminator`.

### Hire Block (44 bytes)

Offsets count from the end of `spawn_position_keys`. Every row of client 3458 holds the same 44 bytes.

| Offset  | Type | Field           | Notes                                                            |
| ------- | ---- | --------------- | ---------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00      | Always `0`                                                       |
| `+0x04` | u32  | unknown_04      | Always `0`                                                       |
| `+0x08` | u32  | unknown_08      | Always `0`                                                       |
| `+0x0C` | u32  | unknown_0c      | Always `0`                                                       |
| `+0x10` | u32  | respawn_time_s  | Always `3600`; seconds, the one-hour sailor respawn time in game |
| `+0x14` | u32  | unknown_14      | Always `0`                                                       |
| `+0x18` | u32  | unknown_18      | Always `1000000`; see Open Questions                             |
| `+0x1C` | u32  | hire_item_key   | Always `752030`, Sailor Contract Certificate (LOC type 0)        |
| `+0x20` | u64  | hire_item_count | Always `1`                                                       |
| `+0x28` | u32  | unknown_28      | Always `1000000`; see Open Questions                             |

The item text of `752030` reads "A certificate required for hiring a sailor", and the grumpygreen.cricket sailor guide states one certificate per hired sailor, which matches `hire_item_count` `1`. Item counts are 64-bit in the client (`getNeedItemCount_s64` in `panel_dialog_employee_hireitem_all_1.luac`); the upper half of `hire_item_count` is `0` on every row, so a u32 count and a zero u32 would read the same.

### `employeespawninfooffset.dbss`

Bare offset table into `employeespawninfo.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                             |
| ------- | ----------------- | ----- | ------------------------------------------------- |
| `+0x00` | u32               | count | Number of offset rows; equals the main file count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                    |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                            |
| ------- | ---- | ------------- | ------------------------------------------------ |
| `+0x00` | u16  | character_key | Key of the row it points at                      |
| `+0x02` | u32  | data_offset   | Absolute byte offset in `employeespawninfo.dbss` |
| `+0x06` | u32  | data_size     | Row size in bytes, `136` to `236`                |

The rows are in file order, which is not key order (59061, 59053, 59055, 59064, ...). The parser reads the main file through these rows, checks that every row holds the key of the offset row that points at it, and checks that the row ends exactly at `data_offset + data_size`.

## Localization

| Text            | LOC key                                                  |
| --------------- | -------------------------------------------------------- |
| Name            | type 6, `str_id1` = `character_key`, `str_id4` 0 (`Sailor`) |
| Title           | type 6, `str_id1` = `character_key`, `str_id4` 1 (`<Ambitious>`) |
| Accept line     | type 70, `str_id1` = `character_key`, `str_id4` 0         |
| Refuse line     | type 70, `str_id1` = `character_key`, `str_id4` 1         |
| Hire item       | type 0, `str_id1` = `hire_item_key`                       |
| Town            | type 17, `str_id1` = `region_key` of the spawn position   |

LOC type 70 holds exactly these 40 lines on client 3458, `str_id4` 0 and 1 for each of the 20 characters. The English line matches the inline Korean one (59053: "I will get rid of all the prejudice you have on Goblins." for "고블린에 대한 편견을 다 없애드리지요."). The handler shows the LOC text and falls back to the inline Korean. Without LOC the Name and Title columns show the Korean `characterstatic.dbss` name and title (`59053` `선원 <욕심 있는>`).

## Notes

- `employee_key` is the sailor ID of `employeestaticstatus.bss`: all 20 rows match its level 1 row for the same character (`1` = `59053` to `20` = `59072`). Sailors `21` to `23` of that table (`59101`, `59227`, `59228`) and the First Mates have no row here; they are not hired in a port town.
- The spawn positions of each sailor agree with the location chart of the grumpygreen.cricket sailor guide for 19 of 20 sailors (Ambitious: Velia and Port Epheria; Born in the Sea: Iliya Island; Quick-Witted: Velia and Iliya Island). The guide lists Tenacious (`59062`, positions `2` and `42`) in Velia only.
- Every row has one or two spawn positions, and every two-position row names two different towns.
- The `employeespawnposition.dbss` handler reads this file as an optional companion for its Sailors column (see [employeespawnposition](employeespawnposition_dbss.md)).

## Open Questions

### unknown_18 and unknown_28

Both store `1000000`, which is the client's 100% for rates stored out of 1,000,000. Either could be a hire success chance or a spawn chance. A row with another value after a patch would tell them apart.

### unknown_00 to unknown_0c and unknown_14

These five u32 values are `0` on every row. The first could be the count of an empty list rather than a fixed field; a row with a non-zero value would show which.
