# `lightuserbonus.bss` Format

## Purpose

The light user bonus: by its sheet's column names, bonus items by time
spent disconnected. A PABR list of bonus rows; each row has a key, ten
reward slots of an offline time and a bonus item, and the number of filled
slots. On client 3482 it holds one row, key `1`, with every slot empty and
a filled-slot count of `0`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                 | Bytes | Records   | Row bytes |
| ------ | ------------- | ------- | -------------------- | ----- | --------- | --------- |
| 3      | 805 and later | 3483    | `lightuserbonus.bss` | 146   | 10 Reward | 12        |
| 2      | 526 to 794    | 794     | `lightuserbonus.bss` | 130   | 10 Reward | 12        |
| 1      | 435 to 521    | 521     | `lightuserbonus.bss` | 132   | 10 Reward | 12        |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 3      | `lightuserbonus.bss` | 146 B (100.0%) | 0 B (0.0%) |
| 2      | `lightuserbonus.bss` | 130 B (100.0%) | 0 B (0.0%) |
| 1      | `lightuserbonus.bss` | 130 B (98.5%)  | 2 B (1.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `6e36b70ef34f`  |
| 3482   | Layout 3 | `6e36b70ef34f`  |
| 3474   | Layout 3 | `6e36b70ef34f`  |
| 3473   | Layout 3 | `6e36b70ef34f`  |
| 3464   | Layout 3 | `6e36b70ef34f`  |
| 3458   | Layout 3 | `6e36b70ef34f`  |
| 3454   | Layout 3 | `6e36b70ef34f`  |
| 3444   | Layout 3 | `6e36b70ef34f`  |
| 3435   | Layout 3 | `6e36b70ef34f`  |
| 3426   | Layout 3 | `6e36b70ef34f`  |
| 3418   | Layout 3 | `6e36b70ef34f`  |
| 3412   | Layout 3 | `6e36b70ef34f`  |
| 3402   | Layout 3 | `6e36b70ef34f`  |
| 3396   | Layout 3 | `6e36b70ef34f`  |
| 3387   | Layout 3 | `6e36b70ef34f`  |
| 3381   | Layout 3 | `6e36b70ef34f`  |
| 3373   | Layout 3 | `6e36b70ef34f`  |
| 3364   | Layout 3 | `6e36b70ef34f`  |
| 3356   | Layout 3 | `6e36b70ef34f`  |
| 3349   | Layout 3 | `6e36b70ef34f`  |
| 3342   | Layout 3 | `6e36b70ef34f`  |
| 3335   | Layout 3 | `6e36b70ef34f`  |
| 3326   | Layout 3 | `6e36b70ef34f`  |
| 3321   | Layout 3 | `6e36b70ef34f`  |
| 3314   | Layout 3 | `6e36b70ef34f`  |
| 3303   | Layout 3 | `6e36b70ef34f`  |
| 3302   | Layout 3 | `6e36b70ef34f`  |
| 3293   | Layout 3 | `6e36b70ef34f`  |
| 3283   | Layout 3 | `6e36b70ef34f`  |
| 3275   | Layout 3 | `6e36b70ef34f`  |
| 3267   | Layout 3 | `6e36b70ef34f`  |
| 3258   | Layout 3 | `6e36b70ef34f`  |
| 3251   | Layout 3 | `6e36b70ef34f`  |
| 3242   | Layout 3 | `6e36b70ef34f`  |
| 3235   | Layout 3 | `6e36b70ef34f`  |
| 3229   | Layout 3 | `6e36b70ef34f`  |
| 3212   | Layout 3 | `6e36b70ef34f`  |
| 3203   | Layout 3 | `6e36b70ef34f`  |
| 3193   | Layout 3 | `6e36b70ef34f`  |
| 3186   | Layout 3 | `6e36b70ef34f`  |
| 3177   | Layout 3 | `6e36b70ef34f`  |
| 3169   | Layout 3 | `6e36b70ef34f`  |
| 3158   | Layout 3 | `6e36b70ef34f`  |
| 3151   | Layout 3 | `6e36b70ef34f`  |
| 3144   | Layout 3 | `6e36b70ef34f`  |
| 3133   | Layout 3 | `6e36b70ef34f`  |
| 3125   | Layout 3 | `6e36b70ef34f`  |
| 3118   | Layout 3 | `6e36b70ef34f`  |
| 3111   | Layout 3 | `6e36b70ef34f`  |
| 3103   | Layout 3 | `6e36b70ef34f`  |
| 3095   | Layout 3 | `6e36b70ef34f`  |
| 3086   | Layout 3 | `6e36b70ef34f`  |
| 3072   | Layout 3 | `6e36b70ef34f`  |
| 3062   | Layout 3 | `6e36b70ef34f`  |
| 3052   | Layout 3 | `6e36b70ef34f`  |
| 3045   | Layout 3 | `6e36b70ef34f`  |
| 3037   | Layout 3 | `6e36b70ef34f`  |
| 3030   | Layout 3 | `6e36b70ef34f`  |
| 3021   | Layout 3 | `6e36b70ef34f`  |
| 3012   | Layout 3 | `6e36b70ef34f`  |
| 3002   | Layout 3 | `6e36b70ef34f`  |
| 2995   | Layout 3 | `6e36b70ef34f`  |
| 2987   | Layout 3 | `6e36b70ef34f`  |
| 2978   | Layout 3 | `6e36b70ef34f`  |
| 2970   | Layout 3 | `6e36b70ef34f`  |
| 2959   | Layout 3 | `6e36b70ef34f`  |
| 2951   | Layout 3 | `6e36b70ef34f`  |
| 2942   | Layout 3 | `6e36b70ef34f`  |
| 2935   | Layout 3 | `6e36b70ef34f`  |
| 2932   | Layout 3 | `6e36b70ef34f`  |
| 2923   | Layout 3 | `6e36b70ef34f`  |
| 2919   | Layout 3 | `6e36b70ef34f`  |
| 2907   | Layout 3 | `6e36b70ef34f`  |
| 2900   | Layout 3 | `6e36b70ef34f`  |
| 2891   | Layout 3 | `6e36b70ef34f`  |
| 2882   | Layout 3 | `6e36b70ef34f`  |
| 2872   | Layout 3 | `6e36b70ef34f`  |
| 2863   | Layout 3 | `6e36b70ef34f`  |
| 2855   | Layout 3 | `6e36b70ef34f`  |
| 2849   | Layout 3 | `6e36b70ef34f`  |
| 2844   | Layout 3 | `6e36b70ef34f`  |
| 2834   | Layout 3 | `6e36b70ef34f`  |
| 2825   | Layout 3 | `6e36b70ef34f`  |
| 2819   | Layout 3 | `6e36b70ef34f`  |
| 2811   | Layout 3 | `6e36b70ef34f`  |
| 2803   | Layout 3 | `6e36b70ef34f`  |
| 2794   | Layout 3 | `6e36b70ef34f`  |
| 2783   | Layout 3 | `6e36b70ef34f`  |
| 2774   | Layout 3 | `6e36b70ef34f`  |
| 2765   | Layout 3 | `6e36b70ef34f`  |
| 2756   | Layout 3 | `6e36b70ef34f`  |
| 2750   | Layout 3 | `6e36b70ef34f`  |
| 2743   | Layout 3 | `6e36b70ef34f`  |
| 2736   | Layout 3 | `6e36b70ef34f`  |
| 2726   | Layout 3 | `6e36b70ef34f`  |
| 2717   | Layout 3 | `6e36b70ef34f`  |
| 2709   | Layout 3 | `6e36b70ef34f`  |
| 2703   | Layout 3 | `6e36b70ef34f`  |
| 2695   | Layout 3 | `6e36b70ef34f`  |
| 2684   | Layout 3 | `6e36b70ef34f`  |
| 2672   | Layout 3 | `6e36b70ef34f`  |
| 2665   | Layout 3 | `6e36b70ef34f`  |
| 2657   | Layout 3 | `6e36b70ef34f`  |
| 2649   | Layout 3 | `6e36b70ef34f`  |
| 2644   | Layout 3 | `6e36b70ef34f`  |
| 2637   | Layout 3 | `6e36b70ef34f`  |
| 2629   | Layout 3 | `6e36b70ef34f`  |
| 2619   | Layout 3 | `6e36b70ef34f`  |
| 2612   | Layout 3 | `6e36b70ef34f`  |
| 2606   | Layout 3 | `6e36b70ef34f`  |
| 2602   | Layout 3 | `6e36b70ef34f`  |
| 2601   | Layout 3 | `6e36b70ef34f`  |
| 2592   | Layout 3 | `6e36b70ef34f`  |
| 2583   | Layout 3 | `6e36b70ef34f`  |
| 2575   | Layout 3 | `6e36b70ef34f`  |
| 2567   | Layout 3 | `6e36b70ef34f`  |
| 2560   | Layout 3 | `6e36b70ef34f`  |
| 2553   | Layout 3 | `6e36b70ef34f`  |
| 2545   | Layout 3 | `6e36b70ef34f`  |
| 2538   | Layout 3 | `6e36b70ef34f`  |
| 2529   | Layout 3 | `6e36b70ef34f`  |
| 2519   | Layout 3 | `6e36b70ef34f`  |
| 2513   | Layout 3 | `6e36b70ef34f`  |
| 2510   | Layout 3 | `6e36b70ef34f`  |
| 2507   | Layout 3 | `6e36b70ef34f`  |
| 2503   | Layout 3 | `6e36b70ef34f`  |
| 2498   | Layout 3 | `6e36b70ef34f`  |
| 2492   | Layout 3 | `6e36b70ef34f`  |
| 2487   | Layout 3 | `6e36b70ef34f`  |
| 2480   | Layout 3 | `6e36b70ef34f`  |
| 2474   | Layout 3 | `6e36b70ef34f`  |
| 2468   | Layout 3 | `6e36b70ef34f`  |
| 2460   | Layout 3 | `6e36b70ef34f`  |
| 2453   | Layout 3 | `6e36b70ef34f`  |
| 2444   | Layout 3 | `6e36b70ef34f`  |
| 2438   | Layout 3 | `6e36b70ef34f`  |
| 2434   | Layout 3 | `6e36b70ef34f`  |
| 2429   | Layout 3 | `6e36b70ef34f`  |
| 2421   | Layout 3 | `6e36b70ef34f`  |
| 2414   | Layout 3 | `6e36b70ef34f`  |
| 2407   | Layout 3 | `6e36b70ef34f`  |
| 2401   | Layout 3 | `6e36b70ef34f`  |
| 2397   | Layout 3 | `6e36b70ef34f`  |
| 2393   | Layout 3 | `6e36b70ef34f`  |
| 2384   | Layout 3 | `6e36b70ef34f`  |
| 2378   | Layout 3 | `6e36b70ef34f`  |
| 2372   | Layout 3 | `6e36b70ef34f`  |
| 2358   | Layout 3 | `6e36b70ef34f`  |
| 2352   | Layout 3 | `6e36b70ef34f`  |
| 2347   | Layout 3 | `6e36b70ef34f`  |
| 2343   | Layout 3 | `6e36b70ef34f`  |
| 2335   | Layout 3 | `6e36b70ef34f`  |
| 2327   | Layout 3 | `6e36b70ef34f`  |
| 2324   | Layout 3 | `6e36b70ef34f`  |
| 2319   | Layout 3 | `6e36b70ef34f`  |
| 2313   | Layout 3 | `6e36b70ef34f`  |
| 2308   | Layout 3 | `6e36b70ef34f`  |
| 2302   | Layout 3 | `6e36b70ef34f`  |
| 2295   | Layout 3 | `6e36b70ef34f`  |
| 2290   | Layout 3 | `6e36b70ef34f`  |
| 2284   | Layout 3 | `6e36b70ef34f`  |
| 2276   | Layout 3 | `6e36b70ef34f`  |
| 2269   | Layout 3 | `6e36b70ef34f`  |
| 2259   | Layout 3 | `6e36b70ef34f`  |
| 2250   | Layout 3 | `6e36b70ef34f`  |
| 2243   | Layout 3 | `6e36b70ef34f`  |
| 2235   | Layout 3 | `6e36b70ef34f`  |
| 2229   | Layout 3 | `6e36b70ef34f`  |
| 2224   | Layout 3 | `6e36b70ef34f`  |
| 2218   | Layout 3 | `6e36b70ef34f`  |
| 2215   | Layout 3 | `6e36b70ef34f`  |
| 2207   | Layout 3 | `6e36b70ef34f`  |
| 2203   | Layout 3 | `6e36b70ef34f`  |
| 2196   | Layout 3 | `6e36b70ef34f`  |
| 2192   | Layout 3 | `6e36b70ef34f`  |
| 2189   | Layout 3 | `6e36b70ef34f`  |
| 2183   | Layout 3 | `6e36b70ef34f`  |
| 2179   | Layout 3 | `6e36b70ef34f`  |
| 2171   | Layout 3 | `6e36b70ef34f`  |
| 2163   | Layout 3 | `6e36b70ef34f`  |
| 2156   | Layout 3 | `6e36b70ef34f`  |
| 2151   | Layout 3 | `6e36b70ef34f`  |
| 2147   | Layout 3 | `6e36b70ef34f`  |
| 2142   | Layout 3 | `6e36b70ef34f`  |
| 2138   | Layout 3 | `6e36b70ef34f`  |
| 2134   | Layout 3 | `6e36b70ef34f`  |
| 2130   | Layout 3 | `6e36b70ef34f`  |
| 2122   | Layout 3 | `6e36b70ef34f`  |
| 2107   | Layout 3 | `6e36b70ef34f`  |
| 2098   | Layout 3 | `6e36b70ef34f`  |
| 2089   | Layout 3 | `6e36b70ef34f`  |
| 2081   | Layout 3 | `6e36b70ef34f`  |
| 2073   | Layout 3 | `6e36b70ef34f`  |
| 2067   | Layout 3 | `6e36b70ef34f`  |
| 2063   | Layout 3 | `6e36b70ef34f`  |
| 2059   | Layout 3 | `6e36b70ef34f`  |
| 2052   | Layout 3 | `6e36b70ef34f`  |
| 2044   | Layout 3 | `6e36b70ef34f`  |
| 2039   | Layout 3 | `6e36b70ef34f`  |
| 2032   | Layout 3 | `6e36b70ef34f`  |
| 2025   | Layout 3 | `6e36b70ef34f`  |
| 2011   | Layout 3 | `6e36b70ef34f`  |
| 2005   | Layout 3 | `6e36b70ef34f`  |
| 2000   | Layout 3 | `6e36b70ef34f`  |
| 1996   | Layout 3 | `6e36b70ef34f`  |
| 1991   | Layout 3 | `6e36b70ef34f`  |
| 1985   | Layout 3 | `6e36b70ef34f`  |
| 1980   | Layout 3 | `6e36b70ef34f`  |
| 1969   | Layout 3 | `6e36b70ef34f`  |
| 1964   | Layout 3 | `6e36b70ef34f`  |
| 1958   | Layout 3 | `6e36b70ef34f`  |
| 1950   | Layout 3 | `6e36b70ef34f`  |
| 1945   | Layout 3 | `6e36b70ef34f`  |
| 1937   | Layout 3 | `6e36b70ef34f`  |
| 1933   | Layout 3 | `6e36b70ef34f`  |
| 1927   | Layout 3 | `6e36b70ef34f`  |
| 1921   | Layout 3 | `6e36b70ef34f`  |
| 1914   | Layout 3 | `6e36b70ef34f`  |
| 1908   | Layout 3 | `6e36b70ef34f`  |
| 1897   | Layout 3 | `6e36b70ef34f`  |
| 1892   | Layout 3 | `6e36b70ef34f`  |
| 1886   | Layout 3 | `6e36b70ef34f`  |
| 1881   | Layout 3 | `6e36b70ef34f`  |
| 1871   | Layout 3 | `6e36b70ef34f`  |
| 1866   | Layout 3 | `6e36b70ef34f`  |
| 1862   | Layout 3 | `6e36b70ef34f`  |
| 1854   | Layout 3 | `6e36b70ef34f`  |
| 1846   | Layout 3 | `6e36b70ef34f`  |
| 1838   | Layout 3 | `6e36b70ef34f`  |
| 1832   | Layout 3 | `6e36b70ef34f`  |
| 1826   | Layout 3 | `6e36b70ef34f`  |
| 1822   | Layout 3 | `6e36b70ef34f`  |
| 1818   | Layout 3 | `6e36b70ef34f`  |
| 1804   | Layout 3 | `6e36b70ef34f`  |
| 1794   | Layout 3 | `6e36b70ef34f`  |
| 1790   | Layout 3 | `6e36b70ef34f`  |
| 1784   | Layout 3 | `6e36b70ef34f`  |
| 1774   | Layout 3 | `6e36b70ef34f`  |
| 1771   | Layout 3 | `6e36b70ef34f`  |
| 1762   | Layout 3 | `6e36b70ef34f`  |
| 1759   | Layout 3 | `6e36b70ef34f`  |
| 1754   | Layout 3 | `6e36b70ef34f`  |
| 1749   | Layout 3 | `6e36b70ef34f`  |
| 1743   | Layout 3 | `6e36b70ef34f`  |
| 1737   | Layout 3 | `6e36b70ef34f`  |
| 1731   | Layout 3 | `6e36b70ef34f`  |
| 1725   | Layout 3 | `6e36b70ef34f`  |
| 1717   | Layout 3 | `6e36b70ef34f`  |
| 1710   | Layout 3 | `6e36b70ef34f`  |
| 1704   | Layout 3 | `6e36b70ef34f`  |
| 1698   | Layout 3 | `6e36b70ef34f`  |
| 1690   | Layout 3 | `6e36b70ef34f`  |
| 1685   | Layout 3 | `6e36b70ef34f`  |
| 1680   | Layout 3 | `6e36b70ef34f`  |
| 1674   | Layout 3 | `6e36b70ef34f`  |
| 1668   | Layout 3 | `6e36b70ef34f`  |
| 1659   | Layout 3 | `6e36b70ef34f`  |
| 1649   | Layout 3 | `6e36b70ef34f`  |
| 1642   | Layout 3 | `6e36b70ef34f`  |
| 1636   | Layout 3 | `6e36b70ef34f`  |
| 1628   | Layout 3 | `6e36b70ef34f`  |
| 1622   | Layout 3 | `6e36b70ef34f`  |
| 1614   | Layout 3 | `6e36b70ef34f`  |
| 1608   | Layout 3 | `6e36b70ef34f`  |
| 1602   | Layout 3 | `6e36b70ef34f`  |
| 1598   | Layout 3 | `6e36b70ef34f`  |
| 1594   | Layout 3 | `6e36b70ef34f`  |
| 1590   | Layout 3 | `6e36b70ef34f`  |
| 1587   | Layout 3 | `6e36b70ef34f`  |
| 1584   | Layout 3 | `6e36b70ef34f`  |
| 1579   | Layout 3 | `6e36b70ef34f`  |
| 1572   | Layout 3 | `6e36b70ef34f`  |
| 1565   | Layout 3 | `6e36b70ef34f`  |
| 1559   | Layout 3 | `6e36b70ef34f`  |
| 1554   | Layout 3 | `6e36b70ef34f`  |
| 1547   | Layout 3 | `6e36b70ef34f`  |
| 1537   | Layout 3 | `6e36b70ef34f`  |
| 1529   | Layout 3 | `6e36b70ef34f`  |
| 1524   | Layout 3 | `6e36b70ef34f`  |
| 1519   | Layout 3 | `6e36b70ef34f`  |
| 1509   | Layout 3 | `6e36b70ef34f`  |
| 1506   | Layout 3 | `6e36b70ef34f`  |
| 1504   | Layout 3 | `6e36b70ef34f`  |
| 1500   | Layout 3 | `6e36b70ef34f`  |
| 1493   | Layout 3 | `6e36b70ef34f`  |
| 1489   | Layout 3 | `6e36b70ef34f`  |
| 1485   | Layout 3 | `6e36b70ef34f`  |
| 1481   | Layout 3 | `6e36b70ef34f`  |
| 1474   | Layout 3 | `6e36b70ef34f`  |
| 1466   | Layout 3 | `6e36b70ef34f`  |
| 1462   | Layout 3 | `6e36b70ef34f`  |
| 1459   | Layout 3 | `6e36b70ef34f`  |
| 1453   | Layout 3 | `6e36b70ef34f`  |
| 1450   | Layout 3 | `6e36b70ef34f`  |
| 1445   | Layout 3 | `6e36b70ef34f`  |
| 1439   | Layout 3 | `6e36b70ef34f`  |
| 1433   | Layout 3 | `6e36b70ef34f`  |
| 1430   | Layout 3 | `6e36b70ef34f`  |
| 1426   | Layout 3 | `6e36b70ef34f`  |
| 1421   | Layout 3 | `6e36b70ef34f`  |
| 1417   | Layout 3 | `6e36b70ef34f`  |
| 1416   | Layout 3 | `6e36b70ef34f`  |
| 1409   | Layout 3 | `6e36b70ef34f`  |
| 1405   | Layout 3 | `6e36b70ef34f`  |
| 1401   | Layout 3 | `6e36b70ef34f`  |
| 1396   | Layout 3 | `6e36b70ef34f`  |
| 1391   | Layout 3 | `6e36b70ef34f`  |
| 1390   | Layout 3 | `6e36b70ef34f`  |
| 1386   | Layout 3 | `6e36b70ef34f`  |
| 1381   | Layout 3 | `6e36b70ef34f`  |
| 1379   | Layout 3 | `6e36b70ef34f`  |
| 1372   | Layout 3 | `6e36b70ef34f`  |
| 1366   | Layout 3 | `6e36b70ef34f`  |
| 1364   | Layout 3 | `6e36b70ef34f`  |
| 1363   | Layout 3 | `6e36b70ef34f`  |
| 1360   | Layout 3 | `6e36b70ef34f`  |
| 1358   | Layout 3 | `6e36b70ef34f`  |
| 1355   | Layout 3 | `6e36b70ef34f`  |
| 1351   | Layout 3 | `6e36b70ef34f`  |
| 1348   | Layout 3 | `6e36b70ef34f`  |
| 1346   | Layout 3 | `6e36b70ef34f`  |
| 1341   | Layout 3 | `6e36b70ef34f`  |
| 1340   | Layout 3 | `6e36b70ef34f`  |
| 1338   | Layout 3 | `6e36b70ef34f`  |
| 1335   | Layout 3 | `6e36b70ef34f`  |
| 1333   | Layout 3 | `6e36b70ef34f`  |
| 1329   | Layout 3 | `6e36b70ef34f`  |
| 1327   | Layout 3 | `6e36b70ef34f`  |
| 1324   | Layout 3 | `6e36b70ef34f`  |
| 1321   | Layout 3 | `6e36b70ef34f`  |
| 1319   | Layout 3 | `6e36b70ef34f`  |
| 1318   | Layout 3 | `6e36b70ef34f`  |
| 1316   | Layout 3 | `6e36b70ef34f`  |
| 1313   | Layout 3 | `6e36b70ef34f`  |
| 1311   | Layout 3 | `6e36b70ef34f`  |
| 1309   | Layout 3 | `6e36b70ef34f`  |
| 1304   | Layout 3 | `6e36b70ef34f`  |
| 1292   | Layout 3 | `6e36b70ef34f`  |
| 1286   | Layout 3 | `6e36b70ef34f`  |
| 1280   | Layout 3 | `6e36b70ef34f`  |
| 1276   | Layout 3 | `6e36b70ef34f`  |
| 1267   | Layout 3 | `6e36b70ef34f`  |
| 1261   | Layout 3 | `6e36b70ef34f`  |
| 1256   | Layout 3 | `6e36b70ef34f`  |
| 1250   | Layout 3 | `6e36b70ef34f`  |
| 1246   | No file  | `6e36b70ef34f`  |
| 1239   | No file  | `6e36b70ef34f`  |
| 1230   | No file  | `6e36b70ef34f`  |
| 1226   | No file  | `6e36b70ef34f`  |
| 1220   | No file  | `6e36b70ef34f`  |
| 1217   | No file  | `6e36b70ef34f`  |
| 1211   | No file  | `6e36b70ef34f`  |
| 1210   | No file  | `6e36b70ef34f`  |
| 1208   | No file  | `6e36b70ef34f`  |
| 1203   | No file  | `6e36b70ef34f`  |
| 1197   | No file  | `6e36b70ef34f`  |
| 1194   | No file  | `6e36b70ef34f`  |
| 1192   | No file  | `6e36b70ef34f`  |
| 1187   | No file  | `6e36b70ef34f`  |
| 1183   | No file  | `6e36b70ef34f`  |
| 1177   | No file  | `6e36b70ef34f`  |
| 1173   | No file  | `6e36b70ef34f`  |
| 1167   | No file  | `6e36b70ef34f`  |
| 1164   | No file  | `6e36b70ef34f`  |
| 1156   | No file  | `6e36b70ef34f`  |
| 1149   | No file  | `6e36b70ef34f`  |
| 1144   | No file  | `6e36b70ef34f`  |
| 1137   | No file  | `6e36b70ef34f`  |
| 1132   | No file  | `6e36b70ef34f`  |
| 1127   | No file  | `6e36b70ef34f`  |
| 1122   | No file  | `6e36b70ef34f`  |
| 1118   | No file  | `6e36b70ef34f`  |
| 1114   | No file  | `6e36b70ef34f`  |
| 1109   | No file  | `6e36b70ef34f`  |
| 1102   | No file  | `6e36b70ef34f`  |
| 1096   | No file  | `6e36b70ef34f`  |
| 1088   | No file  | `6e36b70ef34f`  |
| 1081   | No file  | `6e36b70ef34f`  |
| 1076   | No file  | `6e36b70ef34f`  |
| 1069   | No file  | `6e36b70ef34f`  |
| 1064   | No file  | `6e36b70ef34f`  |
| 1058   | No file  | `6e36b70ef34f`  |
| 1051   | No file  | `6e36b70ef34f`  |
| 1044   | No file  | `6e36b70ef34f`  |
| 1036   | No file  | `6e36b70ef34f`  |
| 1026   | No file  | `6e36b70ef34f`  |
| 1016   | No file  | `6e36b70ef34f`  |
| 1009   | No file  | `6e36b70ef34f`  |
| 1005   | No file  | `6e36b70ef34f`  |
| 1000   | No file  | `6e36b70ef34f`  |
| 998    | No file  | `6e36b70ef34f`  |
| 990    | No file  | `6e36b70ef34f`  |
| 979    | No file  | `6e36b70ef34f`  |
| 972    | No file  | `6e36b70ef34f`  |
| 963    | No file  | `6e36b70ef34f`  |
| 955    | No file  | `6e36b70ef34f`  |
| 946    | No file  | `6e36b70ef34f`  |
| 938    | No file  | `6e36b70ef34f`  |
| 927    | No file  | `6e36b70ef34f`  |
| 911    | No file  | `6e36b70ef34f`  |
| 904    | No file  | `6e36b70ef34f`  |
| 899    | No file  | `6e36b70ef34f`  |
| 894    | No file  | `6e36b70ef34f`  |
| 885    | No file  | `6e36b70ef34f`  |
| 879    | No file  | `6e36b70ef34f`  |
| 872    | No file  | `6e36b70ef34f`  |
| 864    | No file  | `6e36b70ef34f`  |
| 855    | No file  | `6e36b70ef34f`  |
| 853    | No file  | `6e36b70ef34f`  |
| 845    | No file  | `6e36b70ef34f`  |
| 837    | No file  | `6e36b70ef34f`  |
| 829    | Layout 3 | `6e36b70ef34f`  |
| 822    | Layout 3 | `6e36b70ef34f`  |
| 814    | Layout 3 | `6e36b70ef34f`  |
| 805    | Layout 3 | `6e36b70ef34f`  |
| 794    | Layout 2 | `6e36b70ef34f`  |
| 787    | Layout 2 | `6e36b70ef34f`  |
| 780    | Layout 2 | `6e36b70ef34f`  |
| 771    | Layout 2 | `6e36b70ef34f`  |
| 760    | Layout 2 | `6e36b70ef34f`  |
| 748    | Layout 2 | `6e36b70ef34f`  |
| 741    | Layout 2 | `6e36b70ef34f`  |
| 736    | Layout 2 | `6e36b70ef34f`  |
| 731    | Layout 2 | `6e36b70ef34f`  |
| 723    | Layout 2 | `6e36b70ef34f`  |
| 711    | Layout 2 | `6e36b70ef34f`  |
| 707    | Layout 2 | `6e36b70ef34f`  |
| 697    | Layout 2 | `6e36b70ef34f`  |
| 689    | Layout 2 | `6e36b70ef34f`  |
| 683    | Layout 2 | `6e36b70ef34f`  |
| 678    | Layout 2 | `6e36b70ef34f`  |
| 670    | Layout 2 | `6e36b70ef34f`  |
| 661    | Layout 2 | `6e36b70ef34f`  |
| 656    | Layout 2 | `6e36b70ef34f`  |
| 652    | Layout 2 | `6e36b70ef34f`  |
| 643    | Layout 2 | `6e36b70ef34f`  |
| 637    | Layout 2 | `6e36b70ef34f`  |
| 630    | Layout 2 | `6e36b70ef34f`  |
| 627    | Layout 2 | `6e36b70ef34f`  |
| 621    | Layout 2 | `6e36b70ef34f`  |
| 617    | Layout 2 | `6e36b70ef34f`  |
| 615    | Layout 2 | `6e36b70ef34f`  |
| 606    | Layout 2 | `6e36b70ef34f`  |
| 599    | Layout 2 | `6e36b70ef34f`  |
| 592    | Layout 2 | `6e36b70ef34f`  |
| 586    | Layout 2 | `6e36b70ef34f`  |
| 577    | Layout 2 | `6e36b70ef34f`  |
| 569    | Layout 2 | `6e36b70ef34f`  |
| 561    | Layout 2 | `6e36b70ef34f`  |
| 554    | Layout 2 | `6e36b70ef34f`  |
| 542    | Layout 2 | `6e36b70ef34f`  |
| 532    | Layout 2 | `6e36b70ef34f`  |
| 531    | Layout 2 | `6e36b70ef34f`  |
| 526    | Layout 2 | `6e36b70ef34f`  |
| 521    | Layout 1 | `6e36b70ef34f`  |
| 517    | Layout 1 | `6e36b70ef34f`  |
| 510    | Layout 1 | `6e36b70ef34f`  |
| 508    | Layout 1 | `6e36b70ef34f`  |
| 504    | Layout 1 | `6e36b70ef34f`  |
| 497    | Layout 1 | `6e36b70ef34f`  |
| 491    | Layout 1 | `6e36b70ef34f`  |
| 485    | Layout 1 | `6e36b70ef34f`  |
| 478    | Layout 1 | `6e36b70ef34f`  |
| 472    | Layout 1 | `6e36b70ef34f`  |
| 466    | Layout 1 | `6e36b70ef34f`  |
| 457    | Layout 1 | `6e36b70ef34f`  |
| 452    | Layout 1 | `6e36b70ef34f`  |
| 449    | Layout 1 | `6e36b70ef34f`  |
| 435    | Layout 1 | `6e36b70ef34f`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of bonus rows; `1` on clients 1784 and 3482 |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (126 bytes)

| Offset  | Type        | Field              | Notes                                         |
| ------- | ----------- | ------------------ | --------------------------------------------- |
| `+0x00` | u16         | key                | Row key; `1`                                  |
| `+0x02` | Reward[10]  | rewards            | See Reward; slot N is `DisConnectedTimeN` and `BonusN` |
| `+0x7A` | u32         | valid_reward_count | Number of filled slots; `0`                   |

### Reward (12 bytes)

| Offset  | Type | Field             | Notes                                          |
| ------- | ---- | ----------------- | ---------------------------------------------- |
| `+0x00` | i64  | disconnected_time | Time offline that earns the slot; `0` (empty)  |
| `+0x08` | u32  | bonus             | Item enchant key of the bonus item; `0` (empty) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 2

The file has no PABR magic, string table or trailer; the rows are the
Layout 3 rows.

### File Layout

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | Number of bonus rows |
| `+0x04` | Row[row_count] | rows      | See Row              |

## Layout 1

### Row (128 bytes)

| Offset  | Type       | Field              | Notes                                |
| ------- | ---------- | ------------------ | ------------------------------------ |
| `+0x00` | u16        | key                | Row key; `1`                         |
| `+0x02` | u16        | unknown_after_key  | `1` on client 521                    |
| `+0x04` | Reward[10] | rewards            | Same as Layout 3                     |
| `+0x7C` | u32        | valid_reward_count | `0`                                  |

## Field Names

The `LightUserBonus_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Key`, then `DisConnectedTime1` and
`Bonus1` to `DisConnectedTime10` and `Bonus10`, and one row: key `1`
with every other column `<null>`. The client 1784 file holds that row, key
`1` and 124 zero bytes. The 2016 `gc::LightUserBonusStaticStatus` gives the
split of those bytes: a `KeyType<unsigned short>` `_key`, a
`pa::Array<gc::LightUserBonusReward,10>` `_reward` and an int
`_validRewardCount`, and each `gc::LightUserBonusReward` is an `__int64`
`_disconnectedTime` and a `gc::ItemEnchantKey` `_itemKey`. A u16, ten
12-byte slots and a u32 add up to the 126-byte row exactly. The slot
fields take the sheet's names, `valid_reward_count` the 2016 member's.

## Notes

- Every value but the key is `0` on clients 1784 and 3482, so the names
  rest on the sheet's column order and the 2016 struct, not on values.
- Layout 1 holds a u16 `1` between the key and the slots; the 2016 struct
  has only alignment there, so `unknown_after_key` stays unnamed.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/server_tables.py`; its
  Rewards cell lists only filled slots as `disconnected_time: bonus`.

## Open Questions

### The Unit of `disconnected_time`

No slot is filled on clients 521, 794, 1784 and 3482, and the client Lua
does not name the table, so whether `disconnected_time` counts seconds,
minutes or hours is open.
