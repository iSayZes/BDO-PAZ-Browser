# `vehicletrainingskill.bss` Format

## Purpose

The mount training skills: the [`vehicleskill.dbss`](../dbss/vehicleskill_dbss.md)
keys that a mount raises with training items instead of riding. A u32 count
follows the PABR magic, then one u8 skill key per entry. On every client
checked (1784 to 3474) the list is `49` Skill, `50` Elegance and `51`
Strength.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes | Records        | Row bytes |
| ------ | -------------- | -------------------------- | ----- | -------------- | --------- |
| 1      | 1250 and later | `vehicletrainingskill.bss` | 23    | 1 String Table | 4         |

| Layout | File                       | Known         | Unknown    |
| ------ | -------------------------- | ------------- | ---------- |
| 1      | `vehicletrainingskill.bss` | 23 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `f2e70712ee5c`  |
| 3482   | Layout 1 | `f2e70712ee5c`  |
| 3474   | Layout 1 | `f2e70712ee5c`  |
| 3473   | Layout 1 | `f2e70712ee5c`  |
| 3464   | Layout 1 | `f2e70712ee5c`  |
| 3458   | Layout 1 | `f2e70712ee5c`  |
| 3454   | Layout 1 | `f2e70712ee5c`  |
| 3444   | Layout 1 | `f2e70712ee5c`  |
| 3435   | Layout 1 | `f2e70712ee5c`  |
| 3426   | Layout 1 | `f2e70712ee5c`  |
| 3418   | Layout 1 | `f2e70712ee5c`  |
| 3412   | Layout 1 | `f2e70712ee5c`  |
| 3402   | Layout 1 | `f2e70712ee5c`  |
| 3396   | Layout 1 | `f2e70712ee5c`  |
| 3387   | Layout 1 | `f2e70712ee5c`  |
| 3381   | Layout 1 | `f2e70712ee5c`  |
| 3373   | Layout 1 | `f2e70712ee5c`  |
| 3364   | Layout 1 | `f2e70712ee5c`  |
| 3356   | Layout 1 | `f2e70712ee5c`  |
| 3349   | Layout 1 | `f2e70712ee5c`  |
| 3342   | Layout 1 | `f2e70712ee5c`  |
| 3335   | Layout 1 | `f2e70712ee5c`  |
| 3326   | Layout 1 | `f2e70712ee5c`  |
| 3321   | Layout 1 | `f2e70712ee5c`  |
| 3314   | Layout 1 | `f2e70712ee5c`  |
| 3303   | Layout 1 | `f2e70712ee5c`  |
| 3302   | Layout 1 | `f2e70712ee5c`  |
| 3293   | Layout 1 | `f2e70712ee5c`  |
| 3283   | Layout 1 | `f2e70712ee5c`  |
| 3275   | Layout 1 | `f2e70712ee5c`  |
| 3267   | Layout 1 | `f2e70712ee5c`  |
| 3258   | Layout 1 | `f2e70712ee5c`  |
| 3251   | Layout 1 | `f2e70712ee5c`  |
| 3242   | Layout 1 | `f2e70712ee5c`  |
| 3235   | Layout 1 | `f2e70712ee5c`  |
| 3229   | Layout 1 | `f2e70712ee5c`  |
| 3212   | Layout 1 | `f2e70712ee5c`  |
| 3203   | Layout 1 | `f2e70712ee5c`  |
| 3193   | Layout 1 | `f2e70712ee5c`  |
| 3186   | Layout 1 | `f2e70712ee5c`  |
| 3177   | Layout 1 | `f2e70712ee5c`  |
| 3169   | Layout 1 | `f2e70712ee5c`  |
| 3158   | Layout 1 | `f2e70712ee5c`  |
| 3151   | Layout 1 | `f2e70712ee5c`  |
| 3144   | Layout 1 | `f2e70712ee5c`  |
| 3133   | Layout 1 | `f2e70712ee5c`  |
| 3125   | Layout 1 | `f2e70712ee5c`  |
| 3118   | Layout 1 | `f2e70712ee5c`  |
| 3111   | Layout 1 | `f2e70712ee5c`  |
| 3103   | Layout 1 | `f2e70712ee5c`  |
| 3095   | Layout 1 | `f2e70712ee5c`  |
| 3086   | Layout 1 | `f2e70712ee5c`  |
| 3072   | Layout 1 | `f2e70712ee5c`  |
| 3062   | Layout 1 | `f2e70712ee5c`  |
| 3052   | Layout 1 | `f2e70712ee5c`  |
| 3045   | Layout 1 | `f2e70712ee5c`  |
| 3037   | Layout 1 | `f2e70712ee5c`  |
| 3030   | Layout 1 | `f2e70712ee5c`  |
| 3021   | Layout 1 | `f2e70712ee5c`  |
| 3012   | Layout 1 | `f2e70712ee5c`  |
| 3002   | Layout 1 | `f2e70712ee5c`  |
| 2995   | Layout 1 | `f2e70712ee5c`  |
| 2987   | Layout 1 | `f2e70712ee5c`  |
| 2978   | Layout 1 | `f2e70712ee5c`  |
| 2970   | Layout 1 | `f2e70712ee5c`  |
| 2959   | Layout 1 | `f2e70712ee5c`  |
| 2951   | Layout 1 | `f2e70712ee5c`  |
| 2942   | Layout 1 | `f2e70712ee5c`  |
| 2935   | Layout 1 | `f2e70712ee5c`  |
| 2932   | Layout 1 | `f2e70712ee5c`  |
| 2923   | Layout 1 | `f2e70712ee5c`  |
| 2919   | Layout 1 | `f2e70712ee5c`  |
| 2907   | Layout 1 | `f2e70712ee5c`  |
| 2900   | Layout 1 | `f2e70712ee5c`  |
| 2891   | Layout 1 | `f2e70712ee5c`  |
| 2882   | Layout 1 | `f2e70712ee5c`  |
| 2872   | Layout 1 | `f2e70712ee5c`  |
| 2863   | Layout 1 | `f2e70712ee5c`  |
| 2855   | Layout 1 | `f2e70712ee5c`  |
| 2849   | Layout 1 | `f2e70712ee5c`  |
| 2844   | Layout 1 | `f2e70712ee5c`  |
| 2834   | Layout 1 | `f2e70712ee5c`  |
| 2825   | Layout 1 | `f2e70712ee5c`  |
| 2819   | Layout 1 | `f2e70712ee5c`  |
| 2811   | Layout 1 | `f2e70712ee5c`  |
| 2803   | Layout 1 | `f2e70712ee5c`  |
| 2794   | Layout 1 | `f2e70712ee5c`  |
| 2783   | Layout 1 | `f2e70712ee5c`  |
| 2774   | Layout 1 | `f2e70712ee5c`  |
| 2765   | Layout 1 | `f2e70712ee5c`  |
| 2756   | Layout 1 | `f2e70712ee5c`  |
| 2750   | Layout 1 | `f2e70712ee5c`  |
| 2743   | Layout 1 | `f2e70712ee5c`  |
| 2736   | Layout 1 | `f2e70712ee5c`  |
| 2726   | Layout 1 | `f2e70712ee5c`  |
| 2717   | Layout 1 | `f2e70712ee5c`  |
| 2709   | Layout 1 | `f2e70712ee5c`  |
| 2703   | Layout 1 | `f2e70712ee5c`  |
| 2695   | Layout 1 | `f2e70712ee5c`  |
| 2684   | Layout 1 | `f2e70712ee5c`  |
| 2672   | Layout 1 | `f2e70712ee5c`  |
| 2665   | Layout 1 | `f2e70712ee5c`  |
| 2657   | Layout 1 | `f2e70712ee5c`  |
| 2649   | Layout 1 | `f2e70712ee5c`  |
| 2644   | Layout 1 | `f2e70712ee5c`  |
| 2637   | Layout 1 | `f2e70712ee5c`  |
| 2629   | Layout 1 | `f2e70712ee5c`  |
| 2619   | Layout 1 | `f2e70712ee5c`  |
| 2612   | Layout 1 | `f2e70712ee5c`  |
| 2606   | Layout 1 | `f2e70712ee5c`  |
| 2602   | Layout 1 | `f2e70712ee5c`  |
| 2601   | Layout 1 | `f2e70712ee5c`  |
| 2592   | Layout 1 | `f2e70712ee5c`  |
| 2583   | Layout 1 | `f2e70712ee5c`  |
| 2575   | Layout 1 | `f2e70712ee5c`  |
| 2567   | Layout 1 | `f2e70712ee5c`  |
| 2560   | Layout 1 | `f2e70712ee5c`  |
| 2553   | Layout 1 | `f2e70712ee5c`  |
| 2545   | Layout 1 | `f2e70712ee5c`  |
| 2538   | Layout 1 | `f2e70712ee5c`  |
| 2529   | Layout 1 | `f2e70712ee5c`  |
| 2519   | Layout 1 | `f2e70712ee5c`  |
| 2513   | Layout 1 | `f2e70712ee5c`  |
| 2510   | Layout 1 | `f2e70712ee5c`  |
| 2507   | Layout 1 | `f2e70712ee5c`  |
| 2503   | Layout 1 | `f2e70712ee5c`  |
| 2498   | Layout 1 | `f2e70712ee5c`  |
| 2492   | Layout 1 | `f2e70712ee5c`  |
| 2487   | Layout 1 | `f2e70712ee5c`  |
| 2480   | Layout 1 | `f2e70712ee5c`  |
| 2474   | Layout 1 | `f2e70712ee5c`  |
| 2468   | Layout 1 | `f2e70712ee5c`  |
| 2460   | Layout 1 | `f2e70712ee5c`  |
| 2453   | Layout 1 | `f2e70712ee5c`  |
| 2444   | Layout 1 | `f2e70712ee5c`  |
| 2438   | Layout 1 | `f2e70712ee5c`  |
| 2434   | Layout 1 | `f2e70712ee5c`  |
| 2429   | Layout 1 | `f2e70712ee5c`  |
| 2421   | Layout 1 | `f2e70712ee5c`  |
| 2414   | Layout 1 | `f2e70712ee5c`  |
| 2407   | Layout 1 | `f2e70712ee5c`  |
| 2401   | Layout 1 | `f2e70712ee5c`  |
| 2397   | Layout 1 | `f2e70712ee5c`  |
| 2393   | Layout 1 | `f2e70712ee5c`  |
| 2384   | Layout 1 | `f2e70712ee5c`  |
| 2378   | Layout 1 | `f2e70712ee5c`  |
| 2372   | Layout 1 | `f2e70712ee5c`  |
| 2358   | Layout 1 | `f2e70712ee5c`  |
| 2352   | Layout 1 | `f2e70712ee5c`  |
| 2347   | Layout 1 | `f2e70712ee5c`  |
| 2343   | Layout 1 | `f2e70712ee5c`  |
| 2335   | Layout 1 | `f2e70712ee5c`  |
| 2327   | Layout 1 | `f2e70712ee5c`  |
| 2324   | Layout 1 | `f2e70712ee5c`  |
| 2319   | Layout 1 | `f2e70712ee5c`  |
| 2313   | Layout 1 | `f2e70712ee5c`  |
| 2308   | Layout 1 | `f2e70712ee5c`  |
| 2302   | Layout 1 | `f2e70712ee5c`  |
| 2295   | Layout 1 | `f2e70712ee5c`  |
| 2290   | Layout 1 | `f2e70712ee5c`  |
| 2284   | Layout 1 | `f2e70712ee5c`  |
| 2276   | Layout 1 | `f2e70712ee5c`  |
| 2269   | Layout 1 | `f2e70712ee5c`  |
| 2259   | Layout 1 | `f2e70712ee5c`  |
| 2250   | Layout 1 | `f2e70712ee5c`  |
| 2243   | Layout 1 | `f2e70712ee5c`  |
| 2235   | Layout 1 | `f2e70712ee5c`  |
| 2229   | Layout 1 | `f2e70712ee5c`  |
| 2224   | Layout 1 | `f2e70712ee5c`  |
| 2218   | Layout 1 | `f2e70712ee5c`  |
| 2215   | Layout 1 | `f2e70712ee5c`  |
| 2207   | Layout 1 | `f2e70712ee5c`  |
| 2203   | Layout 1 | `f2e70712ee5c`  |
| 2196   | Layout 1 | `f2e70712ee5c`  |
| 2192   | Layout 1 | `f2e70712ee5c`  |
| 2189   | Layout 1 | `f2e70712ee5c`  |
| 2183   | Layout 1 | `f2e70712ee5c`  |
| 2179   | Layout 1 | `f2e70712ee5c`  |
| 2171   | Layout 1 | `f2e70712ee5c`  |
| 2163   | Layout 1 | `f2e70712ee5c`  |
| 2156   | Layout 1 | `f2e70712ee5c`  |
| 2151   | Layout 1 | `f2e70712ee5c`  |
| 2147   | Layout 1 | `f2e70712ee5c`  |
| 2142   | Layout 1 | `f2e70712ee5c`  |
| 2138   | Layout 1 | `f2e70712ee5c`  |
| 2134   | Layout 1 | `f2e70712ee5c`  |
| 2130   | Layout 1 | `f2e70712ee5c`  |
| 2122   | Layout 1 | `f2e70712ee5c`  |
| 2107   | Layout 1 | `f2e70712ee5c`  |
| 2098   | Layout 1 | `f2e70712ee5c`  |
| 2089   | Layout 1 | `f2e70712ee5c`  |
| 2081   | Layout 1 | `f2e70712ee5c`  |
| 2073   | Layout 1 | `f2e70712ee5c`  |
| 2067   | Layout 1 | `f2e70712ee5c`  |
| 2063   | Layout 1 | `f2e70712ee5c`  |
| 2059   | Layout 1 | `f2e70712ee5c`  |
| 2052   | Layout 1 | `f2e70712ee5c`  |
| 2044   | Layout 1 | `f2e70712ee5c`  |
| 2039   | Layout 1 | `f2e70712ee5c`  |
| 2032   | Layout 1 | `f2e70712ee5c`  |
| 2025   | Layout 1 | `f2e70712ee5c`  |
| 2011   | Layout 1 | `f2e70712ee5c`  |
| 2005   | Layout 1 | `f2e70712ee5c`  |
| 2000   | Layout 1 | `f2e70712ee5c`  |
| 1996   | Layout 1 | `f2e70712ee5c`  |
| 1991   | Layout 1 | `f2e70712ee5c`  |
| 1985   | Layout 1 | `f2e70712ee5c`  |
| 1980   | Layout 1 | `f2e70712ee5c`  |
| 1969   | Layout 1 | `f2e70712ee5c`  |
| 1964   | Layout 1 | `f2e70712ee5c`  |
| 1958   | Layout 1 | `f2e70712ee5c`  |
| 1950   | Layout 1 | `f2e70712ee5c`  |
| 1945   | Layout 1 | `f2e70712ee5c`  |
| 1937   | Layout 1 | `f2e70712ee5c`  |
| 1933   | Layout 1 | `f2e70712ee5c`  |
| 1927   | Layout 1 | `f2e70712ee5c`  |
| 1921   | Layout 1 | `f2e70712ee5c`  |
| 1914   | Layout 1 | `f2e70712ee5c`  |
| 1908   | Layout 1 | `f2e70712ee5c`  |
| 1897   | Layout 1 | `f2e70712ee5c`  |
| 1892   | Layout 1 | `f2e70712ee5c`  |
| 1886   | Layout 1 | `f2e70712ee5c`  |
| 1881   | Layout 1 | `f2e70712ee5c`  |
| 1871   | Layout 1 | `f2e70712ee5c`  |
| 1866   | Layout 1 | `f2e70712ee5c`  |
| 1862   | Layout 1 | `f2e70712ee5c`  |
| 1854   | Layout 1 | `f2e70712ee5c`  |
| 1846   | Layout 1 | `f2e70712ee5c`  |
| 1838   | Layout 1 | `f2e70712ee5c`  |
| 1832   | Layout 1 | `f2e70712ee5c`  |
| 1826   | Layout 1 | `f2e70712ee5c`  |
| 1822   | Layout 1 | `f2e70712ee5c`  |
| 1818   | Layout 1 | `f2e70712ee5c`  |
| 1804   | Layout 1 | `f2e70712ee5c`  |
| 1794   | Layout 1 | `f2e70712ee5c`  |
| 1790   | Layout 1 | `f2e70712ee5c`  |
| 1784   | Layout 1 | `f2e70712ee5c`  |
| 1774   | Layout 1 | `f2e70712ee5c`  |
| 1771   | Layout 1 | `f2e70712ee5c`  |
| 1762   | Layout 1 | `f2e70712ee5c`  |
| 1759   | Layout 1 | `f2e70712ee5c`  |
| 1754   | Layout 1 | `f2e70712ee5c`  |
| 1749   | Layout 1 | `f2e70712ee5c`  |
| 1743   | Layout 1 | `f2e70712ee5c`  |
| 1737   | Layout 1 | `f2e70712ee5c`  |
| 1731   | Layout 1 | `f2e70712ee5c`  |
| 1725   | Layout 1 | `f2e70712ee5c`  |
| 1717   | Layout 1 | `f2e70712ee5c`  |
| 1710   | Layout 1 | `f2e70712ee5c`  |
| 1704   | Layout 1 | `f2e70712ee5c`  |
| 1698   | Layout 1 | `f2e70712ee5c`  |
| 1690   | Layout 1 | `f2e70712ee5c`  |
| 1685   | Layout 1 | `f2e70712ee5c`  |
| 1680   | Layout 1 | `f2e70712ee5c`  |
| 1674   | Layout 1 | `f2e70712ee5c`  |
| 1668   | Layout 1 | `f2e70712ee5c`  |
| 1659   | Layout 1 | `f2e70712ee5c`  |
| 1649   | Layout 1 | `f2e70712ee5c`  |
| 1642   | Layout 1 | `f2e70712ee5c`  |
| 1636   | Layout 1 | `f2e70712ee5c`  |
| 1628   | Layout 1 | `f2e70712ee5c`  |
| 1622   | Layout 1 | `f2e70712ee5c`  |
| 1614   | Layout 1 | `f2e70712ee5c`  |
| 1608   | Layout 1 | `f2e70712ee5c`  |
| 1602   | Layout 1 | `f2e70712ee5c`  |
| 1598   | Layout 1 | `f2e70712ee5c`  |
| 1594   | Layout 1 | `f2e70712ee5c`  |
| 1590   | Layout 1 | `f2e70712ee5c`  |
| 1587   | Layout 1 | `f2e70712ee5c`  |
| 1584   | Layout 1 | `f2e70712ee5c`  |
| 1579   | Layout 1 | `f2e70712ee5c`  |
| 1572   | Layout 1 | `f2e70712ee5c`  |
| 1565   | Layout 1 | `f2e70712ee5c`  |
| 1559   | Layout 1 | `f2e70712ee5c`  |
| 1554   | Layout 1 | `f2e70712ee5c`  |
| 1547   | Layout 1 | `f2e70712ee5c`  |
| 1537   | Layout 1 | `f2e70712ee5c`  |
| 1529   | Layout 1 | `f2e70712ee5c`  |
| 1524   | Layout 1 | `f2e70712ee5c`  |
| 1519   | Layout 1 | `f2e70712ee5c`  |
| 1509   | Layout 1 | `f2e70712ee5c`  |
| 1506   | Layout 1 | `f2e70712ee5c`  |
| 1504   | Layout 1 | `f2e70712ee5c`  |
| 1500   | Layout 1 | `f2e70712ee5c`  |
| 1493   | Layout 1 | `f2e70712ee5c`  |
| 1489   | Layout 1 | `f2e70712ee5c`  |
| 1485   | Layout 1 | `f2e70712ee5c`  |
| 1481   | Layout 1 | `f2e70712ee5c`  |
| 1474   | Layout 1 | `f2e70712ee5c`  |
| 1466   | Layout 1 | `f2e70712ee5c`  |
| 1462   | Layout 1 | `f2e70712ee5c`  |
| 1459   | Layout 1 | `f2e70712ee5c`  |
| 1453   | Layout 1 | `f2e70712ee5c`  |
| 1450   | Layout 1 | `f2e70712ee5c`  |
| 1445   | Layout 1 | `f2e70712ee5c`  |
| 1439   | Layout 1 | `f2e70712ee5c`  |
| 1433   | Layout 1 | `f2e70712ee5c`  |
| 1430   | Layout 1 | `f2e70712ee5c`  |
| 1426   | Layout 1 | `f2e70712ee5c`  |
| 1421   | Layout 1 | `f2e70712ee5c`  |
| 1417   | Layout 1 | `f2e70712ee5c`  |
| 1416   | Layout 1 | `f2e70712ee5c`  |
| 1409   | Layout 1 | `f2e70712ee5c`  |
| 1405   | Layout 1 | `f2e70712ee5c`  |
| 1401   | Layout 1 | `f2e70712ee5c`  |
| 1396   | Layout 1 | `f2e70712ee5c`  |
| 1391   | Layout 1 | `f2e70712ee5c`  |
| 1390   | Layout 1 | `f2e70712ee5c`  |
| 1386   | Layout 1 | `f2e70712ee5c`  |
| 1381   | Layout 1 | `f2e70712ee5c`  |
| 1379   | Layout 1 | `f2e70712ee5c`  |
| 1372   | Layout 1 | `f2e70712ee5c`  |
| 1366   | Layout 1 | `f2e70712ee5c`  |
| 1364   | Layout 1 | `f2e70712ee5c`  |
| 1363   | Layout 1 | `f2e70712ee5c`  |
| 1360   | Layout 1 | `f2e70712ee5c`  |
| 1358   | Layout 1 | `f2e70712ee5c`  |
| 1355   | Layout 1 | `f2e70712ee5c`  |
| 1351   | Layout 1 | `f2e70712ee5c`  |
| 1348   | Layout 1 | `f2e70712ee5c`  |
| 1346   | Layout 1 | `f2e70712ee5c`  |
| 1341   | Layout 1 | `f2e70712ee5c`  |
| 1340   | Layout 1 | `f2e70712ee5c`  |
| 1338   | Layout 1 | `f2e70712ee5c`  |
| 1335   | Layout 1 | `f2e70712ee5c`  |
| 1333   | Layout 1 | `f2e70712ee5c`  |
| 1329   | Layout 1 | `f2e70712ee5c`  |
| 1327   | Layout 1 | `f2e70712ee5c`  |
| 1324   | Layout 1 | `f2e70712ee5c`  |
| 1321   | Layout 1 | `f2e70712ee5c`  |
| 1319   | Layout 1 | `f2e70712ee5c`  |
| 1318   | Layout 1 | `f2e70712ee5c`  |
| 1316   | Layout 1 | `f2e70712ee5c`  |
| 1313   | Layout 1 | `f2e70712ee5c`  |
| 1311   | Layout 1 | `f2e70712ee5c`  |
| 1309   | Layout 1 | `f2e70712ee5c`  |
| 1304   | Layout 1 | `f2e70712ee5c`  |
| 1292   | Layout 1 | `f2e70712ee5c`  |
| 1286   | Layout 1 | `f2e70712ee5c`  |
| 1280   | Layout 1 | `f2e70712ee5c`  |
| 1276   | Layout 1 | `f2e70712ee5c`  |
| 1267   | Layout 1 | `f2e70712ee5c`  |
| 1261   | Layout 1 | `f2e70712ee5c`  |
| 1256   | Layout 1 | `f2e70712ee5c`  |
| 1250   | Layout 1 | `f2e70712ee5c`  |
| 1246   | No file  | `f2e70712ee5c`  |
| 1239   | No file  | `f2e70712ee5c`  |
| 1230   | No file  | `f2e70712ee5c`  |
| 1226   | No file  | `f2e70712ee5c`  |
| 1220   | No file  | `f2e70712ee5c`  |
| 1217   | No file  | `f2e70712ee5c`  |
| 1211   | No file  | `f2e70712ee5c`  |
| 1210   | No file  | `f2e70712ee5c`  |
| 1208   | No file  | `f2e70712ee5c`  |
| 1203   | No file  | `f2e70712ee5c`  |
| 1197   | No file  | `f2e70712ee5c`  |
| 1194   | No file  | `f2e70712ee5c`  |
| 1192   | No file  | `f2e70712ee5c`  |
| 1187   | No file  | `f2e70712ee5c`  |
| 1183   | No file  | `f2e70712ee5c`  |
| 1177   | No file  | `f2e70712ee5c`  |
| 1173   | No file  | `f2e70712ee5c`  |
| 1167   | No file  | `f2e70712ee5c`  |
| 1164   | No file  | `f2e70712ee5c`  |
| 1156   | No file  | `f2e70712ee5c`  |
| 1149   | No file  | `f2e70712ee5c`  |
| 1144   | No file  | `f2e70712ee5c`  |
| 1137   | No file  | `f2e70712ee5c`  |
| 1132   | No file  | `f2e70712ee5c`  |
| 1127   | No file  | `f2e70712ee5c`  |
| 1122   | No file  | `f2e70712ee5c`  |
| 1118   | No file  | `f2e70712ee5c`  |
| 1114   | No file  | `f2e70712ee5c`  |
| 1109   | No file  | `f2e70712ee5c`  |
| 1102   | No file  | `f2e70712ee5c`  |
| 1096   | No file  | `f2e70712ee5c`  |
| 1088   | No file  | `f2e70712ee5c`  |
| 1081   | No file  | `f2e70712ee5c`  |
| 1076   | No file  | `f2e70712ee5c`  |
| 1069   | No file  | `f2e70712ee5c`  |
| 1064   | No file  | `f2e70712ee5c`  |
| 1058   | No file  | `f2e70712ee5c`  |
| 1051   | No file  | `f2e70712ee5c`  |
| 1044   | No file  | `f2e70712ee5c`  |
| 1036   | No file  | `f2e70712ee5c`  |
| 1026   | No file  | `f2e70712ee5c`  |
| 1016   | No file  | `f2e70712ee5c`  |
| 1009   | No file  | `f2e70712ee5c`  |
| 1005   | No file  | `f2e70712ee5c`  |
| 1000   | No file  | `f2e70712ee5c`  |
| 998    | No file  | `f2e70712ee5c`  |
| 990    | No file  | `f2e70712ee5c`  |
| 979    | No file  | `f2e70712ee5c`  |
| 972    | No file  | `f2e70712ee5c`  |
| 963    | No file  | `f2e70712ee5c`  |
| 955    | No file  | `f2e70712ee5c`  |
| 946    | No file  | `f2e70712ee5c`  |
| 938    | No file  | `f2e70712ee5c`  |
| 927    | No file  | `f2e70712ee5c`  |
| 911    | No file  | `f2e70712ee5c`  |
| 904    | No file  | `f2e70712ee5c`  |
| 899    | No file  | `f2e70712ee5c`  |
| 894    | No file  | `f2e70712ee5c`  |
| 885    | No file  | `f2e70712ee5c`  |
| 879    | No file  | `f2e70712ee5c`  |
| 872    | No file  | `f2e70712ee5c`  |
| 864    | No file  | `f2e70712ee5c`  |
| 855    | No file  | `f2e70712ee5c`  |
| 853    | No file  | `f2e70712ee5c`  |
| 845    | No file  | `f2e70712ee5c`  |
| 837    | No file  | `f2e70712ee5c`  |
| 829    | No file  | `f2e70712ee5c`  |
| 822    | No file  | `f2e70712ee5c`  |
| 814    | No file  | `f2e70712ee5c`  |
| 805    | No file  | `f2e70712ee5c`  |
| 794    | No file  | `f2e70712ee5c`  |
| 787    | No file  | `f2e70712ee5c`  |
| 780    | No file  | `f2e70712ee5c`  |
| 771    | No file  | `f2e70712ee5c`  |
| 760    | No file  | `f2e70712ee5c`  |
| 748    | No file  | `f2e70712ee5c`  |
| 741    | No file  | `f2e70712ee5c`  |
| 736    | No file  | `f2e70712ee5c`  |
| 731    | No file  | `f2e70712ee5c`  |
| 723    | No file  | `f2e70712ee5c`  |
| 711    | No file  | `f2e70712ee5c`  |
| 707    | No file  | `f2e70712ee5c`  |
| 697    | No file  | `f2e70712ee5c`  |
| 689    | No file  | `f2e70712ee5c`  |
| 683    | No file  | `f2e70712ee5c`  |
| 678    | No file  | `f2e70712ee5c`  |
| 670    | No file  | `f2e70712ee5c`  |
| 661    | No file  | `f2e70712ee5c`  |
| 656    | No file  | `f2e70712ee5c`  |
| 652    | No file  | `f2e70712ee5c`  |
| 643    | No file  | `f2e70712ee5c`  |
| 637    | No file  | `f2e70712ee5c`  |
| 630    | No file  | `f2e70712ee5c`  |
| 627    | No file  | `f2e70712ee5c`  |
| 621    | No file  | `f2e70712ee5c`  |
| 617    | No file  | `f2e70712ee5c`  |
| 615    | No file  | `f2e70712ee5c`  |
| 606    | No file  | `f2e70712ee5c`  |
| 599    | No file  | `f2e70712ee5c`  |
| 592    | No file  | `f2e70712ee5c`  |
| 586    | No file  | `f2e70712ee5c`  |
| 577    | No file  | `f2e70712ee5c`  |
| 569    | No file  | `f2e70712ee5c`  |
| 561    | No file  | `f2e70712ee5c`  |
| 554    | No file  | `f2e70712ee5c`  |
| 542    | No file  | `f2e70712ee5c`  |
| 532    | No file  | `f2e70712ee5c`  |
| 531    | No file  | `f2e70712ee5c`  |
| 526    | No file  | `f2e70712ee5c`  |
| 521    | No file  | `f2e70712ee5c`  |
| 517    | No file  | `f2e70712ee5c`  |
| 510    | No file  | `f2e70712ee5c`  |
| 508    | No file  | `f2e70712ee5c`  |
| 504    | No file  | `f2e70712ee5c`  |
| 497    | No file  | `f2e70712ee5c`  |
| 491    | No file  | `f2e70712ee5c`  |
| 485    | No file  | `f2e70712ee5c`  |
| 478    | No file  | `f2e70712ee5c`  |
| 472    | No file  | `f2e70712ee5c`  |
| 466    | No file  | `f2e70712ee5c`  |
| 457    | No file  | `f2e70712ee5c`  |
| 452    | No file  | `f2e70712ee5c`  |
| 449    | No file  | `f2e70712ee5c`  |
| 435    | No file  | `f2e70712ee5c`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                             |
| --------------------- | -------- | -------------------------------- |
| `languagedata_en.loc` | Optional | Mount skill names, LOC type 8    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field        | Notes                                                      |
| ------------------- | --------------- | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32             | skill_count  | Number of skill keys                                       |
| `+0x08`             | u8[skill_count] | skill_key    | `vehicleskill.dbss` key; the handler shows its LOC type 8 name |
| `skill_key+0x00`    | String Table    | string_table | See String Table                                           |
| `string_table+0x00` | u32             | table_start  | Offset of the string table; `0x0B` on every client checked |
| `string_table+0x04` | u32             | zero         | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `VehicleTrainingSkill_Item_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_vehicleskill.xlsm`, has the columns `ItemKey`, `SkillKey`,
`Experience` and `Desc` and 13 rows. Its `SkillKey` values are `49`, `50`
and `51`, the three keys of the client 1784 file (3 of 3) and of the live
file (client 3474). The file keeps only the distinct skill keys; the item
rows are in [`vehicletraining.bss`](vehicletraining_bss.md). The `Desc`
texts name the three trainings
(`기술 훈련`, `기품 훈련`, `체력 훈련`), and a note column of the workbook
says one training skill can be raised with several items (dated
2016-12-12).

The keys are the mount skills `기술`, `기품` and `체력` in `vehicleskill.dbss`
on client 3474; LOC type 8 names them Skill, Elegance and Strength (`str_id4`
`0`), with Elegance Training and Strength Training under `str_id4` `1` and
`4`.

## Notes

- Raw bytes on clients 1784 and 3474:
  `50 41 42 52 03 00 00 00 31 32 33 00 00 00 00 0B 00 00 00 00 00 00 00`
  (23 bytes).
- The skill key is one byte here, as in the other tables that list mount
  skills (`_common/vehicle_skill.py`).
- The servant skill window (`panel_dialog_servantskillmanagement_all_1.luac`,
  client 3474) leaves skills with `skillWrapper:isTrainingSkill()` out of the
  learned skill list.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per skill key.
