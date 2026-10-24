# `petskill.dbss` Format

## Purpose

Pet skill levels. Each record is keyed by `pet_skill_id`, has a skill type that names it in the pet window, and holds ten level entries with two effect parameters each. Companion `petskilloffset.dbss` provides keyed lookup into the variable-size record stream.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records                                | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | -------------------------------------- | --------- |
| 2      | 1881 and later | 3483    | `petskill.dbss`       | 9,380 | 490 Level Entry, 49 Payload, 49 Record | 17        |
| 2      | 1881 and later | 3483    | `petskilloffset.dbss` | 494   | 49 Offset Row                          | 10        |
| 1      | 1346 to 1871   | 1871    | `petskill.dbss`       | 8,606 | 460 Level Entry, 46 Payload, 46 Record | 17        |
| 1      | 1346 to 1871   | 1871    | `petskilloffset.dbss` | 464   | 46 Offset Row                          | 10        |

| Layout | File                  | Known           | Unknown      |
| ------ | --------------------- | --------------- | ------------ |
| 2      | `petskill.dbss`       | 8,775 B (93.6%) | 605 B (6.4%) |
| 2      | `petskilloffset.dbss` | 396 B (80.2%)   | 98 B (19.8%) |
| 1      | `petskill.dbss`       | 8,238 B (95.7%) | 368 B (4.3%) |
| 1      | `petskilloffset.dbss` | 372 B (80.2%)   | 92 B (19.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `95e62c57ec32`  |
| 3482   | Layout 2             | `95e62c57ec32`  |
| 3474   | Layout 2             | `95e62c57ec32`  |
| 3473   | Layout 2             | `95e62c57ec32`  |
| 3464   | Layout 2             | `95e62c57ec32`  |
| 3458   | Layout 2             | `95e62c57ec32`  |
| 3454   | Layout 2             | `95e62c57ec32`  |
| 3444   | Layout 2             | `95e62c57ec32`  |
| 3435   | Layout 2             | `95e62c57ec32`  |
| 3426   | Layout 2             | `95e62c57ec32`  |
| 3418   | Layout 2             | `95e62c57ec32`  |
| 3412   | Layout 2             | `95e62c57ec32`  |
| 3402   | Layout 2             | `95e62c57ec32`  |
| 3396   | Layout 2             | `95e62c57ec32`  |
| 3387   | Layout 2             | `95e62c57ec32`  |
| 3381   | Layout 2             | `95e62c57ec32`  |
| 3373   | Layout 2             | `95e62c57ec32`  |
| 3364   | Layout 2             | `95e62c57ec32`  |
| 3356   | Layout 2             | `95e62c57ec32`  |
| 3349   | Layout 2             | `95e62c57ec32`  |
| 3342   | Layout 2             | `95e62c57ec32`  |
| 3335   | Layout 2             | `95e62c57ec32`  |
| 3326   | Layout 2             | `95e62c57ec32`  |
| 3321   | Layout 2             | `95e62c57ec32`  |
| 3314   | Layout 2             | `95e62c57ec32`  |
| 3303   | Layout 2             | `95e62c57ec32`  |
| 3302   | Layout 2             | `95e62c57ec32`  |
| 3293   | Layout 2             | `95e62c57ec32`  |
| 3283   | Layout 2             | `95e62c57ec32`  |
| 3275   | Layout 2             | `95e62c57ec32`  |
| 3267   | Layout 2             | `95e62c57ec32`  |
| 3258   | Layout 2             | `95e62c57ec32`  |
| 3251   | Layout 2             | `95e62c57ec32`  |
| 3242   | Layout 2             | `95e62c57ec32`  |
| 3235   | Layout 2             | `95e62c57ec32`  |
| 3229   | Layout 2             | `95e62c57ec32`  |
| 3212   | Layout 2             | `95e62c57ec32`  |
| 3203   | Layout 2             | `95e62c57ec32`  |
| 3193   | Layout 2             | `95e62c57ec32`  |
| 3186   | Layout 2             | `95e62c57ec32`  |
| 3177   | Layout 2             | `95e62c57ec32`  |
| 3169   | Layout 2             | `95e62c57ec32`  |
| 3158   | Layout 2             | `95e62c57ec32`  |
| 3151   | Layout 2             | `95e62c57ec32`  |
| 3144   | Layout 2             | `95e62c57ec32`  |
| 3133   | Layout 2             | `95e62c57ec32`  |
| 3125   | Layout 2             | `95e62c57ec32`  |
| 3118   | Layout 2             | `95e62c57ec32`  |
| 3111   | Layout 2             | `95e62c57ec32`  |
| 3103   | Layout 2             | `95e62c57ec32`  |
| 3095   | Layout 2             | `95e62c57ec32`  |
| 3086   | Layout 2             | `95e62c57ec32`  |
| 3072   | Layout 2             | `95e62c57ec32`  |
| 3062   | Layout 2             | `95e62c57ec32`  |
| 3052   | Layout 2             | `95e62c57ec32`  |
| 3045   | Layout 2             | `95e62c57ec32`  |
| 3037   | Layout 2             | `95e62c57ec32`  |
| 3030   | Layout 2             | `95e62c57ec32`  |
| 3021   | Layout 2             | `95e62c57ec32`  |
| 3012   | Layout 2             | `95e62c57ec32`  |
| 3002   | Layout 2             | `95e62c57ec32`  |
| 2995   | Layout 2             | `95e62c57ec32`  |
| 2987   | Layout 2             | `95e62c57ec32`  |
| 2978   | Layout 2             | `95e62c57ec32`  |
| 2970   | Layout 2             | `95e62c57ec32`  |
| 2959   | Layout 2             | `95e62c57ec32`  |
| 2951   | Layout 2             | `95e62c57ec32`  |
| 2942   | Layout 2             | `95e62c57ec32`  |
| 2935   | Layout 2             | `95e62c57ec32`  |
| 2932   | Layout 2             | `95e62c57ec32`  |
| 2923   | Layout 2             | `95e62c57ec32`  |
| 2919   | Layout 2             | `95e62c57ec32`  |
| 2907   | Layout 2             | `95e62c57ec32`  |
| 2900   | Layout 2             | `95e62c57ec32`  |
| 2891   | Layout 2             | `95e62c57ec32`  |
| 2882   | Layout 2             | `95e62c57ec32`  |
| 2872   | Layout 2             | `95e62c57ec32`  |
| 2863   | Layout 2             | `95e62c57ec32`  |
| 2855   | Layout 2             | `95e62c57ec32`  |
| 2849   | Layout 2             | `95e62c57ec32`  |
| 2844   | Layout 2             | `95e62c57ec32`  |
| 2834   | Layout 2             | `95e62c57ec32`  |
| 2825   | Layout 2             | `95e62c57ec32`  |
| 2819   | Layout 2             | `95e62c57ec32`  |
| 2811   | Layout 2             | `95e62c57ec32`  |
| 2803   | Layout 2             | `95e62c57ec32`  |
| 2794   | Layout 2             | `95e62c57ec32`  |
| 2783   | Layout 2             | `95e62c57ec32`  |
| 2774   | Layout 2             | `95e62c57ec32`  |
| 2765   | Layout 2             | `95e62c57ec32`  |
| 2756   | Layout 2             | `95e62c57ec32`  |
| 2750   | Layout 2             | `95e62c57ec32`  |
| 2743   | Layout 2             | `95e62c57ec32`  |
| 2736   | Layout 2             | `95e62c57ec32`  |
| 2726   | Layout 2             | `95e62c57ec32`  |
| 2717   | Layout 2             | `95e62c57ec32`  |
| 2709   | Layout 2             | `95e62c57ec32`  |
| 2703   | Layout 2             | `95e62c57ec32`  |
| 2695   | Layout 2             | `95e62c57ec32`  |
| 2684   | Layout 2             | `95e62c57ec32`  |
| 2672   | Layout 2             | `95e62c57ec32`  |
| 2665   | Layout 2             | `95e62c57ec32`  |
| 2657   | Layout 2             | `95e62c57ec32`  |
| 2649   | Layout 2             | `95e62c57ec32`  |
| 2644   | Layout 2             | `95e62c57ec32`  |
| 2637   | Layout 2             | `95e62c57ec32`  |
| 2629   | Layout 2             | `95e62c57ec32`  |
| 2619   | Layout 2             | `95e62c57ec32`  |
| 2612   | Layout 2             | `95e62c57ec32`  |
| 2606   | Layout 2             | `95e62c57ec32`  |
| 2602   | Layout 2             | `95e62c57ec32`  |
| 2601   | Layout 2             | `95e62c57ec32`  |
| 2592   | Layout 2             | `95e62c57ec32`  |
| 2583   | Layout 2             | `95e62c57ec32`  |
| 2575   | Layout 2             | `95e62c57ec32`  |
| 2567   | Layout 2             | `95e62c57ec32`  |
| 2560   | Layout 2             | `95e62c57ec32`  |
| 2553   | Layout 2             | `95e62c57ec32`  |
| 2545   | Layout 2             | `95e62c57ec32`  |
| 2538   | Layout 2             | `95e62c57ec32`  |
| 2529   | Layout 2             | `95e62c57ec32`  |
| 2519   | Layout 2             | `95e62c57ec32`  |
| 2513   | Layout 2             | `95e62c57ec32`  |
| 2510   | Layout 2             | `95e62c57ec32`  |
| 2507   | Layout 2             | `95e62c57ec32`  |
| 2503   | Layout 2             | `95e62c57ec32`  |
| 2498   | Layout 2             | `95e62c57ec32`  |
| 2492   | Layout 2             | `95e62c57ec32`  |
| 2487   | Layout 2             | `95e62c57ec32`  |
| 2480   | Layout 2             | `95e62c57ec32`  |
| 2474   | Layout 2             | `95e62c57ec32`  |
| 2468   | Layout 2             | `95e62c57ec32`  |
| 2460   | Layout 2             | `95e62c57ec32`  |
| 2453   | Layout 2             | `95e62c57ec32`  |
| 2444   | Layout 2             | `95e62c57ec32`  |
| 2438   | Layout 2             | `95e62c57ec32`  |
| 2434   | Layout 2             | `95e62c57ec32`  |
| 2429   | Layout 2             | `95e62c57ec32`  |
| 2421   | Layout 2             | `95e62c57ec32`  |
| 2414   | Layout 2             | `95e62c57ec32`  |
| 2407   | Layout 2             | `95e62c57ec32`  |
| 2401   | Layout 2             | `95e62c57ec32`  |
| 2397   | Layout 2             | `95e62c57ec32`  |
| 2393   | Layout 2             | `95e62c57ec32`  |
| 2384   | Layout 2             | `95e62c57ec32`  |
| 2378   | Layout 2             | `95e62c57ec32`  |
| 2372   | Layout 2             | `95e62c57ec32`  |
| 2358   | Layout 2             | `95e62c57ec32`  |
| 2352   | Layout 2             | `95e62c57ec32`  |
| 2347   | Layout 2             | `95e62c57ec32`  |
| 2343   | Layout 2             | `95e62c57ec32`  |
| 2335   | Layout 2             | `95e62c57ec32`  |
| 2327   | Layout 2             | `95e62c57ec32`  |
| 2324   | Layout 2             | `95e62c57ec32`  |
| 2319   | Layout 2             | `95e62c57ec32`  |
| 2313   | Layout 2             | `95e62c57ec32`  |
| 2308   | Layout 2             | `95e62c57ec32`  |
| 2302   | Layout 2             | `95e62c57ec32`  |
| 2295   | Layout 2             | `95e62c57ec32`  |
| 2290   | Layout 2             | `95e62c57ec32`  |
| 2284   | Layout 2             | `95e62c57ec32`  |
| 2276   | Layout 2             | `95e62c57ec32`  |
| 2269   | Layout 2             | `95e62c57ec32`  |
| 2259   | Layout 2             | `95e62c57ec32`  |
| 2250   | Layout 2             | `95e62c57ec32`  |
| 2243   | Layout 2             | `95e62c57ec32`  |
| 2235   | Layout 2             | `95e62c57ec32`  |
| 2229   | Layout 2             | `95e62c57ec32`  |
| 2224   | Layout 2             | `95e62c57ec32`  |
| 2218   | Layout 2             | `95e62c57ec32`  |
| 2215   | Layout 2             | `95e62c57ec32`  |
| 2207   | Layout 2             | `95e62c57ec32`  |
| 2203   | Layout 2             | `95e62c57ec32`  |
| 2196   | Layout 2             | `95e62c57ec32`  |
| 2192   | Layout 2             | `95e62c57ec32`  |
| 2189   | Layout 2             | `95e62c57ec32`  |
| 2183   | Layout 2             | `95e62c57ec32`  |
| 2179   | Layout 2             | `95e62c57ec32`  |
| 2171   | Layout 2             | `95e62c57ec32`  |
| 2163   | Layout 2             | `95e62c57ec32`  |
| 2156   | Layout 2             | `95e62c57ec32`  |
| 2151   | Layout 2             | `95e62c57ec32`  |
| 2147   | Layout 2             | `95e62c57ec32`  |
| 2142   | Layout 2             | `95e62c57ec32`  |
| 2138   | Layout 2             | `95e62c57ec32`  |
| 2134   | Layout 2             | `95e62c57ec32`  |
| 2130   | Layout 2             | `95e62c57ec32`  |
| 2122   | Layout 2             | `95e62c57ec32`  |
| 2107   | Layout 2             | `95e62c57ec32`  |
| 2098   | Layout 2             | `95e62c57ec32`  |
| 2089   | Layout 2             | `95e62c57ec32`  |
| 2081   | Layout 2             | `95e62c57ec32`  |
| 2073   | Layout 2             | `95e62c57ec32`  |
| 2067   | Layout 2             | `95e62c57ec32`  |
| 2063   | Layout 2             | `95e62c57ec32`  |
| 2059   | Layout 2             | `95e62c57ec32`  |
| 2052   | Layout 2             | `95e62c57ec32`  |
| 2044   | Layout 2             | `95e62c57ec32`  |
| 2039   | Layout 2             | `95e62c57ec32`  |
| 2032   | Layout 2             | `95e62c57ec32`  |
| 2025   | Layout 2             | `95e62c57ec32`  |
| 2011   | Layout 2             | `95e62c57ec32`  |
| 2005   | Layout 2             | `95e62c57ec32`  |
| 2000   | Layout 2             | `95e62c57ec32`  |
| 1996   | Layout 2             | `95e62c57ec32`  |
| 1991   | Layout 2             | `95e62c57ec32`  |
| 1985   | Layout 2             | `95e62c57ec32`  |
| 1980   | Layout 2             | `95e62c57ec32`  |
| 1969   | Layout 2             | `95e62c57ec32`  |
| 1964   | Layout 2             | `95e62c57ec32`  |
| 1958   | Layout 2             | `95e62c57ec32`  |
| 1950   | Layout 2             | `95e62c57ec32`  |
| 1945   | Layout 2             | `95e62c57ec32`  |
| 1937   | Layout 2             | `95e62c57ec32`  |
| 1933   | Layout 2             | `95e62c57ec32`  |
| 1927   | Layout 2             | `95e62c57ec32`  |
| 1921   | Layout 2             | `95e62c57ec32`  |
| 1914   | Layout 2             | `95e62c57ec32`  |
| 1908   | Layout 2             | `95e62c57ec32`  |
| 1897   | Layout 2             | `95e62c57ec32`  |
| 1892   | Layout 2             | `95e62c57ec32`  |
| 1886   | Layout 2             | `95e62c57ec32`  |
| 1881   | Layout 2             | `95e62c57ec32`  |
| 1871   | Layout 1             | `95e62c57ec32`  |
| 1866   | Layout 1             | `95e62c57ec32`  |
| 1862   | Layout 1             | `95e62c57ec32`  |
| 1854   | Layout 1             | `95e62c57ec32`  |
| 1846   | Layout 1             | `95e62c57ec32`  |
| 1838   | Layout 1             | `95e62c57ec32`  |
| 1832   | Layout 1             | `95e62c57ec32`  |
| 1826   | Layout 1             | `95e62c57ec32`  |
| 1822   | Layout 1             | `95e62c57ec32`  |
| 1818   | Layout 1             | `95e62c57ec32`  |
| 1804   | Layout 1             | `95e62c57ec32`  |
| 1794   | Layout 1             | `95e62c57ec32`  |
| 1790   | Layout 1             | `95e62c57ec32`  |
| 1784   | Layout 1             | `95e62c57ec32`  |
| 1774   | Layout 1             | `95e62c57ec32`  |
| 1771   | Layout 1             | `95e62c57ec32`  |
| 1762   | Layout 1             | `95e62c57ec32`  |
| 1759   | Layout 1             | `95e62c57ec32`  |
| 1754   | Layout 1             | `95e62c57ec32`  |
| 1749   | Layout 1             | `95e62c57ec32`  |
| 1743   | Layout 1             | `95e62c57ec32`  |
| 1737   | Layout 1             | `95e62c57ec32`  |
| 1731   | Layout 1             | `95e62c57ec32`  |
| 1725   | Layout 1             | `95e62c57ec32`  |
| 1717   | Layout 1             | `95e62c57ec32`  |
| 1710   | Layout 1             | `95e62c57ec32`  |
| 1704   | Layout 1             | `95e62c57ec32`  |
| 1698   | Layout 1             | `95e62c57ec32`  |
| 1690   | Layout 1             | `95e62c57ec32`  |
| 1685   | Layout 1             | `95e62c57ec32`  |
| 1680   | Layout 1             | `95e62c57ec32`  |
| 1674   | Layout 1             | `95e62c57ec32`  |
| 1668   | Layout 1             | `95e62c57ec32`  |
| 1659   | Layout 1             | `95e62c57ec32`  |
| 1649   | Layout 1             | `95e62c57ec32`  |
| 1642   | Layout 1             | `95e62c57ec32`  |
| 1636   | Layout 1             | `95e62c57ec32`  |
| 1628   | Layout 1             | `95e62c57ec32`  |
| 1622   | Layout 1             | `95e62c57ec32`  |
| 1614   | Layout 1             | `95e62c57ec32`  |
| 1608   | Layout 1             | `95e62c57ec32`  |
| 1602   | Layout 1             | `95e62c57ec32`  |
| 1598   | Layout 1             | `95e62c57ec32`  |
| 1594   | Layout 1             | `95e62c57ec32`  |
| 1590   | Layout 1             | `95e62c57ec32`  |
| 1587   | Layout 1             | `95e62c57ec32`  |
| 1584   | Layout 1             | `95e62c57ec32`  |
| 1579   | Layout 1             | `95e62c57ec32`  |
| 1572   | Layout 1             | `95e62c57ec32`  |
| 1565   | Layout 1             | `95e62c57ec32`  |
| 1559   | Layout 1             | `95e62c57ec32`  |
| 1554   | Layout 1             | `95e62c57ec32`  |
| 1547   | Layout 1             | `95e62c57ec32`  |
| 1537   | Layout 1             | `95e62c57ec32`  |
| 1529   | Layout 1             | `95e62c57ec32`  |
| 1524   | Layout 1             | `95e62c57ec32`  |
| 1519   | Layout 1             | `95e62c57ec32`  |
| 1509   | Layout 1             | `95e62c57ec32`  |
| 1506   | Layout 1             | `95e62c57ec32`  |
| 1504   | Layout 1             | `95e62c57ec32`  |
| 1500   | Layout 1             | `95e62c57ec32`  |
| 1493   | Layout 1             | `95e62c57ec32`  |
| 1489   | Layout 1             | `95e62c57ec32`  |
| 1485   | Layout 1             | `95e62c57ec32`  |
| 1481   | Layout 1             | `95e62c57ec32`  |
| 1474   | Layout 1             | `95e62c57ec32`  |
| 1466   | Layout 1             | `95e62c57ec32`  |
| 1462   | Layout 1             | `95e62c57ec32`  |
| 1459   | Layout 1             | `95e62c57ec32`  |
| 1453   | Layout 1             | `95e62c57ec32`  |
| 1450   | Layout 1             | `95e62c57ec32`  |
| 1445   | Layout 1             | `95e62c57ec32`  |
| 1439   | Layout 1             | `95e62c57ec32`  |
| 1433   | Layout 1             | `95e62c57ec32`  |
| 1430   | Layout 1             | `95e62c57ec32`  |
| 1426   | Layout 1             | `95e62c57ec32`  |
| 1421   | Layout 1             | `95e62c57ec32`  |
| 1417   | Layout 1             | `95e62c57ec32`  |
| 1416   | Layout 1             | `95e62c57ec32`  |
| 1409   | Layout 1             | `95e62c57ec32`  |
| 1405   | Layout 1             | `95e62c57ec32`  |
| 1401   | Layout 1             | `95e62c57ec32`  |
| 1396   | Layout 1             | `95e62c57ec32`  |
| 1391   | Layout 1             | `95e62c57ec32`  |
| 1390   | Layout 1             | `95e62c57ec32`  |
| 1386   | Layout 1             | `95e62c57ec32`  |
| 1381   | Layout 1             | `95e62c57ec32`  |
| 1379   | Layout 1             | `95e62c57ec32`  |
| 1372   | Layout 1             | `95e62c57ec32`  |
| 1366   | Layout 1             | `95e62c57ec32`  |
| 1364   | Layout 1             | `95e62c57ec32`  |
| 1363   | Layout 1             | `95e62c57ec32`  |
| 1360   | Layout 1             | `95e62c57ec32`  |
| 1358   | Layout 1             | `95e62c57ec32`  |
| 1355   | Layout 1             | `95e62c57ec32`  |
| 1351   | Layout 1             | `95e62c57ec32`  |
| 1348   | Layout 1             | `95e62c57ec32`  |
| 1346   | Layout 1             | `95e62c57ec32`  |
| 1341   | No documented layout | `95e62c57ec32`  |
| 1340   | No documented layout | `95e62c57ec32`  |
| 1338   | No documented layout | `95e62c57ec32`  |
| 1335   | No documented layout | `95e62c57ec32`  |
| 1333   | No documented layout | `95e62c57ec32`  |
| 1329   | No documented layout | `95e62c57ec32`  |
| 1327   | No documented layout | `95e62c57ec32`  |
| 1324   | No documented layout | `95e62c57ec32`  |
| 1321   | No documented layout | `95e62c57ec32`  |
| 1319   | No documented layout | `95e62c57ec32`  |
| 1318   | No documented layout | `95e62c57ec32`  |
| 1316   | No documented layout | `95e62c57ec32`  |
| 1313   | No documented layout | `95e62c57ec32`  |
| 1311   | No documented layout | `95e62c57ec32`  |
| 1309   | No documented layout | `95e62c57ec32`  |
| 1304   | No documented layout | `95e62c57ec32`  |
| 1292   | No documented layout | `95e62c57ec32`  |
| 1286   | No documented layout | `95e62c57ec32`  |
| 1280   | No file              | `95e62c57ec32`  |
| 1276   | No file              | `95e62c57ec32`  |
| 1267   | No documented layout | `95e62c57ec32`  |
| 1261   | No documented layout | `95e62c57ec32`  |
| 1256   | No file              | `95e62c57ec32`  |
| 1250   | No file              | `95e62c57ec32`  |
| 1246   | No file              | `95e62c57ec32`  |
| 1239   | No file              | `95e62c57ec32`  |
| 1230   | No file              | `95e62c57ec32`  |
| 1226   | No file              | `95e62c57ec32`  |
| 1220   | No file              | `95e62c57ec32`  |
| 1217   | No file              | `95e62c57ec32`  |
| 1211   | No file              | `95e62c57ec32`  |
| 1210   | No file              | `95e62c57ec32`  |
| 1208   | No file              | `95e62c57ec32`  |
| 1203   | No file              | `95e62c57ec32`  |
| 1197   | No file              | `95e62c57ec32`  |
| 1194   | No file              | `95e62c57ec32`  |
| 1192   | No file              | `95e62c57ec32`  |
| 1187   | No file              | `95e62c57ec32`  |
| 1183   | No file              | `95e62c57ec32`  |
| 1177   | No file              | `95e62c57ec32`  |
| 1173   | No file              | `95e62c57ec32`  |
| 1167   | No file              | `95e62c57ec32`  |
| 1164   | No file              | `95e62c57ec32`  |
| 1156   | No file              | `95e62c57ec32`  |
| 1149   | No file              | `95e62c57ec32`  |
| 1144   | No file              | `95e62c57ec32`  |
| 1137   | No file              | `95e62c57ec32`  |
| 1132   | No file              | `95e62c57ec32`  |
| 1127   | No file              | `95e62c57ec32`  |
| 1122   | No file              | `95e62c57ec32`  |
| 1118   | No file              | `95e62c57ec32`  |
| 1114   | No file              | `95e62c57ec32`  |
| 1109   | No file              | `95e62c57ec32`  |
| 1102   | No file              | `95e62c57ec32`  |
| 1096   | No file              | `95e62c57ec32`  |
| 1088   | No file              | `95e62c57ec32`  |
| 1081   | No file              | `95e62c57ec32`  |
| 1076   | No file              | `95e62c57ec32`  |
| 1069   | No file              | `95e62c57ec32`  |
| 1064   | No file              | `95e62c57ec32`  |
| 1058   | No file              | `95e62c57ec32`  |
| 1051   | No file              | `95e62c57ec32`  |
| 1044   | No file              | `95e62c57ec32`  |
| 1036   | No file              | `95e62c57ec32`  |
| 1026   | No file              | `95e62c57ec32`  |
| 1016   | No file              | `95e62c57ec32`  |
| 1009   | No file              | `95e62c57ec32`  |
| 1005   | No file              | `95e62c57ec32`  |
| 1000   | No file              | `95e62c57ec32`  |
| 998    | No file              | `95e62c57ec32`  |
| 990    | No file              | `95e62c57ec32`  |
| 979    | No file              | `95e62c57ec32`  |
| 972    | No file              | `95e62c57ec32`  |
| 963    | No file              | `95e62c57ec32`  |
| 955    | No file              | `95e62c57ec32`  |
| 946    | No file              | `95e62c57ec32`  |
| 938    | No file              | `95e62c57ec32`  |
| 927    | No file              | `95e62c57ec32`  |
| 911    | No file              | `95e62c57ec32`  |
| 904    | No file              | `95e62c57ec32`  |
| 899    | No file              | `95e62c57ec32`  |
| 894    | No file              | `95e62c57ec32`  |
| 885    | No file              | `95e62c57ec32`  |
| 879    | No file              | `95e62c57ec32`  |
| 872    | No file              | `95e62c57ec32`  |
| 864    | No file              | `95e62c57ec32`  |
| 855    | No file              | `95e62c57ec32`  |
| 853    | No file              | `95e62c57ec32`  |
| 845    | No file              | `95e62c57ec32`  |
| 837    | No file              | `95e62c57ec32`  |
| 829    | No file              | `95e62c57ec32`  |
| 822    | No file              | `95e62c57ec32`  |
| 814    | No file              | `95e62c57ec32`  |
| 805    | No file              | `95e62c57ec32`  |
| 794    | No file              | `95e62c57ec32`  |
| 787    | No file              | `95e62c57ec32`  |
| 780    | No file              | `95e62c57ec32`  |
| 771    | No file              | `95e62c57ec32`  |
| 760    | No file              | `95e62c57ec32`  |
| 748    | No file              | `95e62c57ec32`  |
| 741    | No file              | `95e62c57ec32`  |
| 736    | No file              | `95e62c57ec32`  |
| 731    | No file              | `95e62c57ec32`  |
| 723    | No file              | `95e62c57ec32`  |
| 711    | No file              | `95e62c57ec32`  |
| 707    | No file              | `95e62c57ec32`  |
| 697    | No file              | `95e62c57ec32`  |
| 689    | No file              | `95e62c57ec32`  |
| 683    | No file              | `95e62c57ec32`  |
| 678    | No file              | `95e62c57ec32`  |
| 670    | No file              | `95e62c57ec32`  |
| 661    | No file              | `95e62c57ec32`  |
| 656    | No file              | `95e62c57ec32`  |
| 652    | No file              | `95e62c57ec32`  |
| 643    | No file              | `95e62c57ec32`  |
| 637    | No file              | `95e62c57ec32`  |
| 630    | No file              | `95e62c57ec32`  |
| 627    | No file              | `95e62c57ec32`  |
| 621    | No file              | `95e62c57ec32`  |
| 617    | No file              | `95e62c57ec32`  |
| 615    | No file              | `95e62c57ec32`  |
| 606    | No file              | `95e62c57ec32`  |
| 599    | No file              | `95e62c57ec32`  |
| 592    | No file              | `95e62c57ec32`  |
| 586    | No file              | `95e62c57ec32`  |
| 577    | No file              | `95e62c57ec32`  |
| 569    | No file              | `95e62c57ec32`  |
| 561    | No file              | `95e62c57ec32`  |
| 554    | No file              | `95e62c57ec32`  |
| 542    | No file              | `95e62c57ec32`  |
| 532    | No file              | `95e62c57ec32`  |
| 531    | No file              | `95e62c57ec32`  |
| 526    | No file              | `95e62c57ec32`  |
| 521    | No file              | `95e62c57ec32`  |
| 517    | No file              | `95e62c57ec32`  |
| 510    | No file              | `95e62c57ec32`  |
| 508    | No file              | `95e62c57ec32`  |
| 504    | No file              | `95e62c57ec32`  |
| 497    | No file              | `95e62c57ec32`  |
| 491    | No file              | `95e62c57ec32`  |
| 485    | No file              | `95e62c57ec32`  |
| 478    | No file              | `95e62c57ec32`  |
| 472    | No file              | `95e62c57ec32`  |
| 466    | No file              | `95e62c57ec32`  |
| 457    | No file              | `95e62c57ec32`  |
| 452    | No file              | `95e62c57ec32`  |
| 449    | No file              | `95e62c57ec32`  |
| 435    | No file              | `95e62c57ec32`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                |
| ---------------------- | -------- | --------------------------------------------------- |
| `petskilloffset.dbss`  | Required | `pet_skill_id -> (data_offset, data_size)` lookup   |
| `stringtable.bss`      | Optional | Key hashes of the skill type names, see Skill Types |

All multi-byte values are little-endian.

## Layout 2

### File Layout

A record count, then the records back to back. Each record is a 2-byte key
prefix and the payload that `petskilloffset.dbss` addresses.

| Offset  | Type          | Field   | Notes                                |
| ------- | ------------- | ------- | ------------------------------------ |
| `+0x00` | u32           | count   | Number of records; 49 on client 3473 |
| `+0x04` | Record[count] | records | See Record                           |

### Record (variable: 2 bytes + payload)

| Offset  | Type    | Field      | Notes                                                  |
| ------- | ------- | ---------- | ------------------------------------------------------ |
| `+0x00` | u16     | key_prefix | Equals `pet_skill_id`                                  |
| `+0x02` | Payload | payload    | `data_size` bytes; the offset row points at this field |

### Payload (variable: 19 bytes + levels and list, size from `petskilloffset.dbss`)

| Offset        | Type                     | Field              | Notes                                                        |
| ------------- | ------------------------ | ------------------ | ------------------------------------------------------------ |
| `+0x00`       | u16                      | pet_skill_id       | Equals the key prefix and the offset-table key               |
| `+0x02`       | u8                       | skill_type         | 1 to 11 on client 3473, see Skill Types                      |
| `+0x03`       | i32                      | unknown_03         | Always `1`; the place of the 2016 `_petRequireLevel` (Notes) |
| `+0x07`       | u32                      | unknown_07         | Always `10`; the place of the 2016 `_skillMaxCount` (Notes)  |
| `+0x0B`       | u32                      | level_count        | `10` on every record                                         |
| `+0x0F`       | Level Entry[level_count] | levels             | Level 1 first                                                |
| `levels+0x00` | u32                      | unknown_list_count | `0` or `1`                                                   |
| `levels+0x04` | u8[unknown_list_count]   | unknown_list       | `9` or `10` when present                                     |

On client 3473, 32 payloads have an empty list (189 bytes) and 17 hold one
byte (190 bytes): `10` on the three type 9 skills (41 to 43), `9` on 14
skills of types 1, 2, 6, 10 and 11 (44 to 57).

### Level Entry (17 bytes)

One `gc::PetSkillParam` of the 2016 client (`_type`, `_level`, `_param[2]`),
after its map key.

| Offset  | Type | Field      | Notes                                                                          |
| ------- | ---- | ---------- | ------------------------------------------------------------------------------ |
| `+0x00` | i32  | level_dup  | Equals `level`; the key of the 2016 `_skillList` map                           |
| `+0x04` | u8   | skill_type | Equals the payload's `skill_type`                                              |
| `+0x05` | i32  | level      | 1 to 10                                                                        |
| `+0x09` | i32  | param_0    | The sheet's `Param0` (Notes); 2,000 to 500,000 on client 3473                  |
| `+0x0D` | i32  | param_1    | The sheet's `Param1`; 0 to 300,000 on client 3473, 0 on 200 of the 490 entries |

Earlier versions of this doc read the payload one byte off, as eleven 17-byte
rows of u8 `skill_type`, u8 `row_level`, u16 and three u32 (`raw_value_a`,
`raw_value_b`, `unknown_0c`) and a trailing u8 `unknown_bd`. The "baseline
row" was the payload head (`skill_type`, `1`, `10`, `10`) and the level 1
key; `raw_value_a` and `raw_value_b` were `param_0` and `param_1` times 256,
`unknown_0c` the next entry's `level_dup` and `unknown_bd` the list byte.

### `petskilloffset.dbss`

| Offset  | Type              | Field | Notes                            |
| ------- | ----------------- | ----- | -------------------------------- |
| `+0x00` | u32               | count | Equals the `petskill.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                   |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                                        |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_skill_id | Matches `pet_skill_id` in the main record                                    |
| `+0x02` | u32  | data_offset  | Absolute byte offset in `petskill.dbss` to the payload, after the key prefix |
| `+0x06` | u16  | data_size    | 189 or 190 bytes on client 3473                                              |
| `+0x08` | u16  | unknown_08   | Always 0                                                                     |

`record_start = data_offset - 2` gives the position of the 2-byte key prefix.

## Layout 1

On client 1784 every payload is 185 bytes: it ends after the tenth level
entry, with no `unknown_list_count`. Only the Payload differs from Layout 2.

### Payload (variable: 15 bytes + levels, size from `petskilloffset.dbss`)

| Offset  | Type                     | Field        | Notes                                          |
| ------- | ------------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u16                      | pet_skill_id | Equals the key prefix and the offset-table key |
| `+0x02` | u8                       | skill_type   |                                                |
| `+0x03` | i32                      | unknown_03   | Always `1`                                     |
| `+0x07` | u32                      | unknown_07   | Always `10`                                    |
| `+0x0B` | u32                      | level_count  | `10` on every record                           |
| `+0x0F` | Level Entry[level_count] | levels       | Level 1 first                                  |

## Observed Values

Client 3473:

| Field          | Observed values / range                           |
| -------------- | ------------------------------------------------- |
| `pet_skill_id` | 1 to 6, 11 to 18, 21 to 23, 26 to 57 (49 records) |
| `skill_type`   | 1 to 11                                           |
| `param_0`      | 2,000 to 500,000                                  |
| `param_1`      | 0 to 300,000                                      |
| `unknown_list` | empty, `9` or `10`                                |

`skill_type` is not unique: multiple `pet_skill_id` records share one value while carrying different parameters.

## Skill Types

`skill_type` is the 2016 `gc::PetSkillParam::PetSkillType`, which Lua reads as `skillParam._type`. It equals the `PetSkillType` column of the `Pet_Skill_Table` sheet of a private server on client 1784 on all 46 shared skills. The pet info window (`setPetSkillType` in `panel_window_petinfo_all_1.luac`) shows one GAME sheet string per type, prefixed `LUA_PETINFO_PETSKILLTYPE_`. Types 11 to 14 are newer than the 2016 enum. English text from client 3473:

| Type | 2016 enum | Key suffix | English text |
| ---: | --------- | ---------- | ------------ |
| 1  | `ePetSkill_Looting` | `ITEMGETTIME` | Loot (every {itemGetTime} sec) |
| 2  | `ePetSkill_AlertCollect` | `FINDGATHER` | Finds Resources |
| 3  | `ePetSkill_AlertMurderer` | `FINDPK` | Hostility Detection |
| 4  | `ePetSkill_DetectPosition` | `FINDPLACE` | Location Find |
| 5  | `ePetSkill_Aggro` | `MOBAGGRO` | Taunt Monster |
| 6  | `ePetSkill_FindNamedMonster` | `FINDRAREMONSTER` | Finds Rare Monsters |
| 7  | `ePetSkill_ReduceAutoFishingTime` | `REDUCEAUTOFISHINGTIME` | Auto-fishing Time Reduction |
| 8  | `ePetSkill_RegistForRegionSkill` | `REGISTILL` | Resistance to Desert Illnesses |
| 9  | `ePetSkill_Collecting` | `AUTOGETHERING` | Auto Gathering |
| 10 | `ePetSkill_CollectingBoost` | `GETHERINGINCREASE` | Gathering Quantity Increase |
| 11 | - | `HPRECOVERY` | Restore HP |
| 12 | - | `MPRECOVERY` | Endurance/MP Recovery |
| 13 | - | `FINDLOSTNORMALITEM` | Find Normal Lost Item |
| 14 | - | `FINDLOSTSPECIALITEM` | Find Special Lost Item |

The client fills `{itemGetTime}` from `ToClient_getPetLootingCoolTime(param, lootingType)`, game code the browser cannot reproduce, so the handler shows `?` there. The window prints the first pet skill as "Basic: ..." and the second as "Special: ...".

The parser yields one record per level entry, ten per pet skill.

## Notes

- File size is 9,380 bytes on client 3473: 4-byte count plus 49 wrapper records.
- `petskilloffset.dbss` size is 494 bytes on client 3473: 4-byte count plus 49 x 10-byte offset rows.
- `unknown_08` of the offset table is 0 in every record.
- Offset rows are sorted descending for high IDs first, not ascending by key.
- The 2016 client's `gc::PetSkillStaticStatus` holds `_petSkillKey` (u16), `_type` (u8), `_petRequireLevel` (i32), `_skillMaxCount` (u32) and `_skillList`, a map from int to `gc::PetSkillParam`. The payload follows that order. `unknown_03` and `unknown_07` stay unnamed: they are `1` and `10` on every record of both clients, and `Pet_Skill_Table` has no column for them.
- `skill_type`, `level`, `param_0` and `param_1` follow the `Pet_Skill_Table` sheet (`PetSkillNo`, `PetSkillType`, `Level`, `Param0`, `Param1`) of a private server's `DataSheets.bexcel` on client 1784. The private server's own file matches it on all 460 level entries. Client 3473 matches `PetSkillType` on all 460 shared entries, `Param0` on 190 and `Param1` on 274; the other values changed since.
- This file is distinct from `petequipskill.bss`, which stores localized equip-skill catalog entries.
- [pet.dbss](pet_dbss.md) keys this file twice per pet: `loot_skill_id` and `race_skill_id`. Every value of both is a `pet_skill_id` here.

## Open Questions

### Parameter Units

`param_0` and `param_1` mean something different per skill type. Loot (type 1) holds 2,000 to 8,000 in `param_0`, and Restore HP (type 11) falls from 14,000 at level 1 to 5,000 at level 10, which reads as an interval in milliseconds. The loot text gets its time from `ToClient_getPetLootingCoolTime(param, lootingType)`, game code that does not show which field `param` is.

### The Trailing List

On client 3473, 17 payloads end with a one-byte list (`9` or `10`), the others with an empty one; client 1784 has no list. The value does not follow `skill_type` alone (type 1 skills hold both an empty list and `9`), so what it selects is open.
