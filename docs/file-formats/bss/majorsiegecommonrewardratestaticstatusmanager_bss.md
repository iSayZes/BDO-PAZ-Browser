# `majorsiegecommonrewardratestaticstatusmanager.bss` Format

## Purpose

A Conquest War (major siege) reward rate table: rows of a u32 and a rate
on the 1,000,000 = 100% scale. On client 3482 the 10 rows step the u32
from `30` to `120` in tens and the rate from 10% to 100% in tens. What
the u32 counts is open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                                | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------------------------------------- | ----- | ------- | --------- |
| 1      | 3302 and later | `majorsiegecommonrewardratestaticstatusmanager.bss` | 100   | 10 Row  | 8         |

| Layout | File                                                | Known        | Unknown      |
| ------ | --------------------------------------------------- | ------------ | ------------ |
| 1      | `majorsiegecommonrewardratestaticstatusmanager.bss` | 60 B (60.0%) | 40 B (40.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `4b11d7e7adef`  |
| 3482   | Layout 1 | `4b11d7e7adef`  |
| 3474   | Layout 1 | `4b11d7e7adef`  |
| 3473   | Layout 1 | `4b11d7e7adef`  |
| 3464   | Layout 1 | `4b11d7e7adef`  |
| 3458   | Layout 1 | `4b11d7e7adef`  |
| 3454   | Layout 1 | `4b11d7e7adef`  |
| 3444   | Layout 1 | `4b11d7e7adef`  |
| 3435   | Layout 1 | `4b11d7e7adef`  |
| 3426   | Layout 1 | `4b11d7e7adef`  |
| 3418   | Layout 1 | `4b11d7e7adef`  |
| 3412   | Layout 1 | `4b11d7e7adef`  |
| 3402   | Layout 1 | `4b11d7e7adef`  |
| 3396   | Layout 1 | `4b11d7e7adef`  |
| 3387   | Layout 1 | `4b11d7e7adef`  |
| 3381   | Layout 1 | `4b11d7e7adef`  |
| 3373   | Layout 1 | `4b11d7e7adef`  |
| 3364   | Layout 1 | `4b11d7e7adef`  |
| 3356   | Layout 1 | `4b11d7e7adef`  |
| 3349   | Layout 1 | `4b11d7e7adef`  |
| 3342   | Layout 1 | `4b11d7e7adef`  |
| 3335   | Layout 1 | `4b11d7e7adef`  |
| 3326   | Layout 1 | `4b11d7e7adef`  |
| 3321   | Layout 1 | `4b11d7e7adef`  |
| 3314   | Layout 1 | `4b11d7e7adef`  |
| 3303   | Layout 1 | `4b11d7e7adef`  |
| 3302   | Layout 1 | `4b11d7e7adef`  |
| 3293   | No file  | `4b11d7e7adef`  |
| 3283   | No file  | `4b11d7e7adef`  |
| 3275   | No file  | `4b11d7e7adef`  |
| 3267   | No file  | `4b11d7e7adef`  |
| 3258   | No file  | `4b11d7e7adef`  |
| 3251   | No file  | `4b11d7e7adef`  |
| 3242   | No file  | `4b11d7e7adef`  |
| 3235   | No file  | `4b11d7e7adef`  |
| 3229   | No file  | `4b11d7e7adef`  |
| 3212   | No file  | `4b11d7e7adef`  |
| 3203   | No file  | `4b11d7e7adef`  |
| 3193   | No file  | `4b11d7e7adef`  |
| 3186   | No file  | `4b11d7e7adef`  |
| 3177   | No file  | `4b11d7e7adef`  |
| 3169   | No file  | `4b11d7e7adef`  |
| 3158   | No file  | `4b11d7e7adef`  |
| 3151   | No file  | `4b11d7e7adef`  |
| 3144   | No file  | `4b11d7e7adef`  |
| 3133   | No file  | `4b11d7e7adef`  |
| 3125   | No file  | `4b11d7e7adef`  |
| 3118   | No file  | `4b11d7e7adef`  |
| 3111   | No file  | `4b11d7e7adef`  |
| 3103   | No file  | `4b11d7e7adef`  |
| 3095   | No file  | `4b11d7e7adef`  |
| 3086   | No file  | `4b11d7e7adef`  |
| 3072   | No file  | `4b11d7e7adef`  |
| 3062   | No file  | `4b11d7e7adef`  |
| 3052   | No file  | `4b11d7e7adef`  |
| 3045   | No file  | `4b11d7e7adef`  |
| 3037   | No file  | `4b11d7e7adef`  |
| 3030   | No file  | `4b11d7e7adef`  |
| 3021   | No file  | `4b11d7e7adef`  |
| 3012   | No file  | `4b11d7e7adef`  |
| 3002   | No file  | `4b11d7e7adef`  |
| 2995   | No file  | `4b11d7e7adef`  |
| 2987   | No file  | `4b11d7e7adef`  |
| 2978   | No file  | `4b11d7e7adef`  |
| 2970   | No file  | `4b11d7e7adef`  |
| 2959   | No file  | `4b11d7e7adef`  |
| 2951   | No file  | `4b11d7e7adef`  |
| 2942   | No file  | `4b11d7e7adef`  |
| 2935   | No file  | `4b11d7e7adef`  |
| 2932   | No file  | `4b11d7e7adef`  |
| 2923   | No file  | `4b11d7e7adef`  |
| 2919   | No file  | `4b11d7e7adef`  |
| 2907   | No file  | `4b11d7e7adef`  |
| 2900   | No file  | `4b11d7e7adef`  |
| 2891   | No file  | `4b11d7e7adef`  |
| 2882   | No file  | `4b11d7e7adef`  |
| 2872   | No file  | `4b11d7e7adef`  |
| 2863   | No file  | `4b11d7e7adef`  |
| 2855   | No file  | `4b11d7e7adef`  |
| 2849   | No file  | `4b11d7e7adef`  |
| 2844   | No file  | `4b11d7e7adef`  |
| 2834   | No file  | `4b11d7e7adef`  |
| 2825   | No file  | `4b11d7e7adef`  |
| 2819   | No file  | `4b11d7e7adef`  |
| 2811   | No file  | `4b11d7e7adef`  |
| 2803   | No file  | `4b11d7e7adef`  |
| 2794   | No file  | `4b11d7e7adef`  |
| 2783   | No file  | `4b11d7e7adef`  |
| 2774   | No file  | `4b11d7e7adef`  |
| 2765   | No file  | `4b11d7e7adef`  |
| 2756   | No file  | `4b11d7e7adef`  |
| 2750   | No file  | `4b11d7e7adef`  |
| 2743   | No file  | `4b11d7e7adef`  |
| 2736   | No file  | `4b11d7e7adef`  |
| 2726   | No file  | `4b11d7e7adef`  |
| 2717   | No file  | `4b11d7e7adef`  |
| 2709   | No file  | `4b11d7e7adef`  |
| 2703   | No file  | `4b11d7e7adef`  |
| 2695   | No file  | `4b11d7e7adef`  |
| 2684   | No file  | `4b11d7e7adef`  |
| 2672   | No file  | `4b11d7e7adef`  |
| 2665   | No file  | `4b11d7e7adef`  |
| 2657   | No file  | `4b11d7e7adef`  |
| 2649   | No file  | `4b11d7e7adef`  |
| 2644   | No file  | `4b11d7e7adef`  |
| 2637   | No file  | `4b11d7e7adef`  |
| 2629   | No file  | `4b11d7e7adef`  |
| 2619   | No file  | `4b11d7e7adef`  |
| 2612   | No file  | `4b11d7e7adef`  |
| 2606   | No file  | `4b11d7e7adef`  |
| 2602   | No file  | `4b11d7e7adef`  |
| 2601   | No file  | `4b11d7e7adef`  |
| 2592   | No file  | `4b11d7e7adef`  |
| 2583   | No file  | `4b11d7e7adef`  |
| 2575   | No file  | `4b11d7e7adef`  |
| 2567   | No file  | `4b11d7e7adef`  |
| 2560   | No file  | `4b11d7e7adef`  |
| 2553   | No file  | `4b11d7e7adef`  |
| 2545   | No file  | `4b11d7e7adef`  |
| 2538   | No file  | `4b11d7e7adef`  |
| 2529   | No file  | `4b11d7e7adef`  |
| 2519   | No file  | `4b11d7e7adef`  |
| 2513   | No file  | `4b11d7e7adef`  |
| 2510   | No file  | `4b11d7e7adef`  |
| 2507   | No file  | `4b11d7e7adef`  |
| 2503   | No file  | `4b11d7e7adef`  |
| 2498   | No file  | `4b11d7e7adef`  |
| 2492   | No file  | `4b11d7e7adef`  |
| 2487   | No file  | `4b11d7e7adef`  |
| 2480   | No file  | `4b11d7e7adef`  |
| 2474   | No file  | `4b11d7e7adef`  |
| 2468   | No file  | `4b11d7e7adef`  |
| 2460   | No file  | `4b11d7e7adef`  |
| 2453   | No file  | `4b11d7e7adef`  |
| 2444   | No file  | `4b11d7e7adef`  |
| 2438   | No file  | `4b11d7e7adef`  |
| 2434   | No file  | `4b11d7e7adef`  |
| 2429   | No file  | `4b11d7e7adef`  |
| 2421   | No file  | `4b11d7e7adef`  |
| 2414   | No file  | `4b11d7e7adef`  |
| 2407   | No file  | `4b11d7e7adef`  |
| 2401   | No file  | `4b11d7e7adef`  |
| 2397   | No file  | `4b11d7e7adef`  |
| 2393   | No file  | `4b11d7e7adef`  |
| 2384   | No file  | `4b11d7e7adef`  |
| 2378   | No file  | `4b11d7e7adef`  |
| 2372   | No file  | `4b11d7e7adef`  |
| 2358   | No file  | `4b11d7e7adef`  |
| 2352   | No file  | `4b11d7e7adef`  |
| 2347   | No file  | `4b11d7e7adef`  |
| 2343   | No file  | `4b11d7e7adef`  |
| 2335   | No file  | `4b11d7e7adef`  |
| 2327   | No file  | `4b11d7e7adef`  |
| 2324   | No file  | `4b11d7e7adef`  |
| 2319   | No file  | `4b11d7e7adef`  |
| 2313   | No file  | `4b11d7e7adef`  |
| 2308   | No file  | `4b11d7e7adef`  |
| 2302   | No file  | `4b11d7e7adef`  |
| 2295   | No file  | `4b11d7e7adef`  |
| 2290   | No file  | `4b11d7e7adef`  |
| 2284   | No file  | `4b11d7e7adef`  |
| 2276   | No file  | `4b11d7e7adef`  |
| 2269   | No file  | `4b11d7e7adef`  |
| 2259   | No file  | `4b11d7e7adef`  |
| 2250   | No file  | `4b11d7e7adef`  |
| 2243   | No file  | `4b11d7e7adef`  |
| 2235   | No file  | `4b11d7e7adef`  |
| 2229   | No file  | `4b11d7e7adef`  |
| 2224   | No file  | `4b11d7e7adef`  |
| 2218   | No file  | `4b11d7e7adef`  |
| 2215   | No file  | `4b11d7e7adef`  |
| 2207   | No file  | `4b11d7e7adef`  |
| 2203   | No file  | `4b11d7e7adef`  |
| 2196   | No file  | `4b11d7e7adef`  |
| 2192   | No file  | `4b11d7e7adef`  |
| 2189   | No file  | `4b11d7e7adef`  |
| 2183   | No file  | `4b11d7e7adef`  |
| 2179   | No file  | `4b11d7e7adef`  |
| 2171   | No file  | `4b11d7e7adef`  |
| 2163   | No file  | `4b11d7e7adef`  |
| 2156   | No file  | `4b11d7e7adef`  |
| 2151   | No file  | `4b11d7e7adef`  |
| 2147   | No file  | `4b11d7e7adef`  |
| 2142   | No file  | `4b11d7e7adef`  |
| 2138   | No file  | `4b11d7e7adef`  |
| 2134   | No file  | `4b11d7e7adef`  |
| 2130   | No file  | `4b11d7e7adef`  |
| 2122   | No file  | `4b11d7e7adef`  |
| 2107   | No file  | `4b11d7e7adef`  |
| 2098   | No file  | `4b11d7e7adef`  |
| 2089   | No file  | `4b11d7e7adef`  |
| 2081   | No file  | `4b11d7e7adef`  |
| 2073   | No file  | `4b11d7e7adef`  |
| 2067   | No file  | `4b11d7e7adef`  |
| 2063   | No file  | `4b11d7e7adef`  |
| 2059   | No file  | `4b11d7e7adef`  |
| 2052   | No file  | `4b11d7e7adef`  |
| 2044   | No file  | `4b11d7e7adef`  |
| 2039   | No file  | `4b11d7e7adef`  |
| 2032   | No file  | `4b11d7e7adef`  |
| 2025   | No file  | `4b11d7e7adef`  |
| 2011   | No file  | `4b11d7e7adef`  |
| 2005   | No file  | `4b11d7e7adef`  |
| 2000   | No file  | `4b11d7e7adef`  |
| 1996   | No file  | `4b11d7e7adef`  |
| 1991   | No file  | `4b11d7e7adef`  |
| 1985   | No file  | `4b11d7e7adef`  |
| 1980   | No file  | `4b11d7e7adef`  |
| 1969   | No file  | `4b11d7e7adef`  |
| 1964   | No file  | `4b11d7e7adef`  |
| 1958   | No file  | `4b11d7e7adef`  |
| 1950   | No file  | `4b11d7e7adef`  |
| 1945   | No file  | `4b11d7e7adef`  |
| 1937   | No file  | `4b11d7e7adef`  |
| 1933   | No file  | `4b11d7e7adef`  |
| 1927   | No file  | `4b11d7e7adef`  |
| 1921   | No file  | `4b11d7e7adef`  |
| 1914   | No file  | `4b11d7e7adef`  |
| 1908   | No file  | `4b11d7e7adef`  |
| 1897   | No file  | `4b11d7e7adef`  |
| 1892   | No file  | `4b11d7e7adef`  |
| 1886   | No file  | `4b11d7e7adef`  |
| 1881   | No file  | `4b11d7e7adef`  |
| 1871   | No file  | `4b11d7e7adef`  |
| 1866   | No file  | `4b11d7e7adef`  |
| 1862   | No file  | `4b11d7e7adef`  |
| 1854   | No file  | `4b11d7e7adef`  |
| 1846   | No file  | `4b11d7e7adef`  |
| 1838   | No file  | `4b11d7e7adef`  |
| 1832   | No file  | `4b11d7e7adef`  |
| 1826   | No file  | `4b11d7e7adef`  |
| 1822   | No file  | `4b11d7e7adef`  |
| 1818   | No file  | `4b11d7e7adef`  |
| 1804   | No file  | `4b11d7e7adef`  |
| 1794   | No file  | `4b11d7e7adef`  |
| 1790   | No file  | `4b11d7e7adef`  |
| 1784   | No file  | `4b11d7e7adef`  |
| 1774   | No file  | `4b11d7e7adef`  |
| 1771   | No file  | `4b11d7e7adef`  |
| 1762   | No file  | `4b11d7e7adef`  |
| 1759   | No file  | `4b11d7e7adef`  |
| 1754   | No file  | `4b11d7e7adef`  |
| 1749   | No file  | `4b11d7e7adef`  |
| 1743   | No file  | `4b11d7e7adef`  |
| 1737   | No file  | `4b11d7e7adef`  |
| 1731   | No file  | `4b11d7e7adef`  |
| 1725   | No file  | `4b11d7e7adef`  |
| 1717   | No file  | `4b11d7e7adef`  |
| 1710   | No file  | `4b11d7e7adef`  |
| 1704   | No file  | `4b11d7e7adef`  |
| 1698   | No file  | `4b11d7e7adef`  |
| 1690   | No file  | `4b11d7e7adef`  |
| 1685   | No file  | `4b11d7e7adef`  |
| 1680   | No file  | `4b11d7e7adef`  |
| 1674   | No file  | `4b11d7e7adef`  |
| 1668   | No file  | `4b11d7e7adef`  |
| 1659   | No file  | `4b11d7e7adef`  |
| 1649   | No file  | `4b11d7e7adef`  |
| 1642   | No file  | `4b11d7e7adef`  |
| 1636   | No file  | `4b11d7e7adef`  |
| 1628   | No file  | `4b11d7e7adef`  |
| 1622   | No file  | `4b11d7e7adef`  |
| 1614   | No file  | `4b11d7e7adef`  |
| 1608   | No file  | `4b11d7e7adef`  |
| 1602   | No file  | `4b11d7e7adef`  |
| 1598   | No file  | `4b11d7e7adef`  |
| 1594   | No file  | `4b11d7e7adef`  |
| 1590   | No file  | `4b11d7e7adef`  |
| 1587   | No file  | `4b11d7e7adef`  |
| 1584   | No file  | `4b11d7e7adef`  |
| 1579   | No file  | `4b11d7e7adef`  |
| 1572   | No file  | `4b11d7e7adef`  |
| 1565   | No file  | `4b11d7e7adef`  |
| 1559   | No file  | `4b11d7e7adef`  |
| 1554   | No file  | `4b11d7e7adef`  |
| 1547   | No file  | `4b11d7e7adef`  |
| 1537   | No file  | `4b11d7e7adef`  |
| 1529   | No file  | `4b11d7e7adef`  |
| 1524   | No file  | `4b11d7e7adef`  |
| 1519   | No file  | `4b11d7e7adef`  |
| 1509   | No file  | `4b11d7e7adef`  |
| 1506   | No file  | `4b11d7e7adef`  |
| 1504   | No file  | `4b11d7e7adef`  |
| 1500   | No file  | `4b11d7e7adef`  |
| 1493   | No file  | `4b11d7e7adef`  |
| 1489   | No file  | `4b11d7e7adef`  |
| 1485   | No file  | `4b11d7e7adef`  |
| 1481   | No file  | `4b11d7e7adef`  |
| 1474   | No file  | `4b11d7e7adef`  |
| 1466   | No file  | `4b11d7e7adef`  |
| 1462   | No file  | `4b11d7e7adef`  |
| 1459   | No file  | `4b11d7e7adef`  |
| 1453   | No file  | `4b11d7e7adef`  |
| 1450   | No file  | `4b11d7e7adef`  |
| 1445   | No file  | `4b11d7e7adef`  |
| 1439   | No file  | `4b11d7e7adef`  |
| 1433   | No file  | `4b11d7e7adef`  |
| 1430   | No file  | `4b11d7e7adef`  |
| 1426   | No file  | `4b11d7e7adef`  |
| 1421   | No file  | `4b11d7e7adef`  |
| 1417   | No file  | `4b11d7e7adef`  |
| 1416   | No file  | `4b11d7e7adef`  |
| 1409   | No file  | `4b11d7e7adef`  |
| 1405   | No file  | `4b11d7e7adef`  |
| 1401   | No file  | `4b11d7e7adef`  |
| 1396   | No file  | `4b11d7e7adef`  |
| 1391   | No file  | `4b11d7e7adef`  |
| 1390   | No file  | `4b11d7e7adef`  |
| 1386   | No file  | `4b11d7e7adef`  |
| 1381   | No file  | `4b11d7e7adef`  |
| 1379   | No file  | `4b11d7e7adef`  |
| 1372   | No file  | `4b11d7e7adef`  |
| 1366   | No file  | `4b11d7e7adef`  |
| 1364   | No file  | `4b11d7e7adef`  |
| 1363   | No file  | `4b11d7e7adef`  |
| 1360   | No file  | `4b11d7e7adef`  |
| 1358   | No file  | `4b11d7e7adef`  |
| 1355   | No file  | `4b11d7e7adef`  |
| 1351   | No file  | `4b11d7e7adef`  |
| 1348   | No file  | `4b11d7e7adef`  |
| 1346   | No file  | `4b11d7e7adef`  |
| 1341   | No file  | `4b11d7e7adef`  |
| 1340   | No file  | `4b11d7e7adef`  |
| 1338   | No file  | `4b11d7e7adef`  |
| 1335   | No file  | `4b11d7e7adef`  |
| 1333   | No file  | `4b11d7e7adef`  |
| 1329   | No file  | `4b11d7e7adef`  |
| 1327   | No file  | `4b11d7e7adef`  |
| 1324   | No file  | `4b11d7e7adef`  |
| 1321   | No file  | `4b11d7e7adef`  |
| 1319   | No file  | `4b11d7e7adef`  |
| 1318   | No file  | `4b11d7e7adef`  |
| 1316   | No file  | `4b11d7e7adef`  |
| 1313   | No file  | `4b11d7e7adef`  |
| 1311   | No file  | `4b11d7e7adef`  |
| 1309   | No file  | `4b11d7e7adef`  |
| 1304   | No file  | `4b11d7e7adef`  |
| 1292   | No file  | `4b11d7e7adef`  |
| 1286   | No file  | `4b11d7e7adef`  |
| 1280   | No file  | `4b11d7e7adef`  |
| 1276   | No file  | `4b11d7e7adef`  |
| 1267   | No file  | `4b11d7e7adef`  |
| 1261   | No file  | `4b11d7e7adef`  |
| 1256   | No file  | `4b11d7e7adef`  |
| 1250   | No file  | `4b11d7e7adef`  |
| 1246   | No file  | `4b11d7e7adef`  |
| 1239   | No file  | `4b11d7e7adef`  |
| 1230   | No file  | `4b11d7e7adef`  |
| 1226   | No file  | `4b11d7e7adef`  |
| 1220   | No file  | `4b11d7e7adef`  |
| 1217   | No file  | `4b11d7e7adef`  |
| 1211   | No file  | `4b11d7e7adef`  |
| 1210   | No file  | `4b11d7e7adef`  |
| 1208   | No file  | `4b11d7e7adef`  |
| 1203   | No file  | `4b11d7e7adef`  |
| 1197   | No file  | `4b11d7e7adef`  |
| 1194   | No file  | `4b11d7e7adef`  |
| 1192   | No file  | `4b11d7e7adef`  |
| 1187   | No file  | `4b11d7e7adef`  |
| 1183   | No file  | `4b11d7e7adef`  |
| 1177   | No file  | `4b11d7e7adef`  |
| 1173   | No file  | `4b11d7e7adef`  |
| 1167   | No file  | `4b11d7e7adef`  |
| 1164   | No file  | `4b11d7e7adef`  |
| 1156   | No file  | `4b11d7e7adef`  |
| 1149   | No file  | `4b11d7e7adef`  |
| 1144   | No file  | `4b11d7e7adef`  |
| 1137   | No file  | `4b11d7e7adef`  |
| 1132   | No file  | `4b11d7e7adef`  |
| 1127   | No file  | `4b11d7e7adef`  |
| 1122   | No file  | `4b11d7e7adef`  |
| 1118   | No file  | `4b11d7e7adef`  |
| 1114   | No file  | `4b11d7e7adef`  |
| 1109   | No file  | `4b11d7e7adef`  |
| 1102   | No file  | `4b11d7e7adef`  |
| 1096   | No file  | `4b11d7e7adef`  |
| 1088   | No file  | `4b11d7e7adef`  |
| 1081   | No file  | `4b11d7e7adef`  |
| 1076   | No file  | `4b11d7e7adef`  |
| 1069   | No file  | `4b11d7e7adef`  |
| 1064   | No file  | `4b11d7e7adef`  |
| 1058   | No file  | `4b11d7e7adef`  |
| 1051   | No file  | `4b11d7e7adef`  |
| 1044   | No file  | `4b11d7e7adef`  |
| 1036   | No file  | `4b11d7e7adef`  |
| 1026   | No file  | `4b11d7e7adef`  |
| 1016   | No file  | `4b11d7e7adef`  |
| 1009   | No file  | `4b11d7e7adef`  |
| 1005   | No file  | `4b11d7e7adef`  |
| 1000   | No file  | `4b11d7e7adef`  |
| 998    | No file  | `4b11d7e7adef`  |
| 990    | No file  | `4b11d7e7adef`  |
| 979    | No file  | `4b11d7e7adef`  |
| 972    | No file  | `4b11d7e7adef`  |
| 963    | No file  | `4b11d7e7adef`  |
| 955    | No file  | `4b11d7e7adef`  |
| 946    | No file  | `4b11d7e7adef`  |
| 938    | No file  | `4b11d7e7adef`  |
| 927    | No file  | `4b11d7e7adef`  |
| 911    | No file  | `4b11d7e7adef`  |
| 904    | No file  | `4b11d7e7adef`  |
| 899    | No file  | `4b11d7e7adef`  |
| 894    | No file  | `4b11d7e7adef`  |
| 885    | No file  | `4b11d7e7adef`  |
| 879    | No file  | `4b11d7e7adef`  |
| 872    | No file  | `4b11d7e7adef`  |
| 864    | No file  | `4b11d7e7adef`  |
| 855    | No file  | `4b11d7e7adef`  |
| 853    | No file  | `4b11d7e7adef`  |
| 845    | No file  | `4b11d7e7adef`  |
| 837    | No file  | `4b11d7e7adef`  |
| 829    | No file  | `4b11d7e7adef`  |
| 822    | No file  | `4b11d7e7adef`  |
| 814    | No file  | `4b11d7e7adef`  |
| 805    | No file  | `4b11d7e7adef`  |
| 794    | No file  | `4b11d7e7adef`  |
| 787    | No file  | `4b11d7e7adef`  |
| 780    | No file  | `4b11d7e7adef`  |
| 771    | No file  | `4b11d7e7adef`  |
| 760    | No file  | `4b11d7e7adef`  |
| 748    | No file  | `4b11d7e7adef`  |
| 741    | No file  | `4b11d7e7adef`  |
| 736    | No file  | `4b11d7e7adef`  |
| 731    | No file  | `4b11d7e7adef`  |
| 723    | No file  | `4b11d7e7adef`  |
| 711    | No file  | `4b11d7e7adef`  |
| 707    | No file  | `4b11d7e7adef`  |
| 697    | No file  | `4b11d7e7adef`  |
| 689    | No file  | `4b11d7e7adef`  |
| 683    | No file  | `4b11d7e7adef`  |
| 678    | No file  | `4b11d7e7adef`  |
| 670    | No file  | `4b11d7e7adef`  |
| 661    | No file  | `4b11d7e7adef`  |
| 656    | No file  | `4b11d7e7adef`  |
| 652    | No file  | `4b11d7e7adef`  |
| 643    | No file  | `4b11d7e7adef`  |
| 637    | No file  | `4b11d7e7adef`  |
| 630    | No file  | `4b11d7e7adef`  |
| 627    | No file  | `4b11d7e7adef`  |
| 621    | No file  | `4b11d7e7adef`  |
| 617    | No file  | `4b11d7e7adef`  |
| 615    | No file  | `4b11d7e7adef`  |
| 606    | No file  | `4b11d7e7adef`  |
| 599    | No file  | `4b11d7e7adef`  |
| 592    | No file  | `4b11d7e7adef`  |
| 586    | No file  | `4b11d7e7adef`  |
| 577    | No file  | `4b11d7e7adef`  |
| 569    | No file  | `4b11d7e7adef`  |
| 561    | No file  | `4b11d7e7adef`  |
| 554    | No file  | `4b11d7e7adef`  |
| 542    | No file  | `4b11d7e7adef`  |
| 532    | No file  | `4b11d7e7adef`  |
| 531    | No file  | `4b11d7e7adef`  |
| 526    | No file  | `4b11d7e7adef`  |
| 521    | No file  | `4b11d7e7adef`  |
| 517    | No file  | `4b11d7e7adef`  |
| 510    | No file  | `4b11d7e7adef`  |
| 508    | No file  | `4b11d7e7adef`  |
| 504    | No file  | `4b11d7e7adef`  |
| 497    | No file  | `4b11d7e7adef`  |
| 491    | No file  | `4b11d7e7adef`  |
| 485    | No file  | `4b11d7e7adef`  |
| 478    | No file  | `4b11d7e7adef`  |
| 472    | No file  | `4b11d7e7adef`  |
| 466    | No file  | `4b11d7e7adef`  |
| 457    | No file  | `4b11d7e7adef`  |
| 452    | No file  | `4b11d7e7adef`  |
| 449    | No file  | `4b11d7e7adef`  |
| 435    | No file  | `4b11d7e7adef`  |

<!-- versions:end -->

## Companion Files

None. The handler reads only this file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (8 bytes)

| Offset  | Type | Field       | Notes                                                                   |
| ------- | ---- | ----------- | ----------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00  | `30` to `120` in steps of `10`, rising in file order (client 3482)      |
| `+0x04` | u32  | reward_rate | On the 1,000,000 = 100% scale; `100000` (10%) to `1000000` (100%)       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The file is newer than client 1784: it is not in that client's archives
and no sheet of a private server's `DataSheets.bexcel` on that client
holds a column of these values. No client Lua of client 3482 reads it.
`reward_rate` takes its name from the file name, `CommonRewardRate`: it
is the one field on the 1,000,000 = 100% scale the handlers read rates
on (`_common/rate.py`).

## Notes

- On client 3482 every row's `reward_rate` is `(unknown_00 - 20) x
  10000`: `30` gives 10%, `120` gives 100%. The file is on clients 3474
  and 3482 of the test clients and not on 3251.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/majorsiege_tables.py`:
  `reward_rate` as a percentage, `unknown_00` on the record only.

## Open Questions

### What the u32 Counts

`unknown_00` runs `30` to `120` and sets a reward share from 10% to
100%. Minutes of participation, a score or a kill count all fit; no Lua
of client 3482 names the table, and no LOC text gives the steps.
