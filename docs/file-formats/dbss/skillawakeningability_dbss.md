# `skillawakeningability.dbss` Format

## Purpose

The Skill Add-on effects: one row per ability index, with the buff the
effect applies and its Korean description. The skill window lists the
add-ons of a skill by these indexes (`ToClient_GetAwakeningAbilityIndex`)
and shows their text, so the index is the key other files and the Lua use.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes  | Records      | Row bytes                  |
| ------ | -------------- | ---------------------------------- | ------ | ------------ | -------------------------- |
| 2      | 3464 and later | `skillawakeningability.dbss`       | 15,838 | 96 Row       | 110 to 270, 165 on average |
| 2      | 3464 and later | `skillawakeningabilityoffset.dbss` | 1,156  | 96 Index Row | 12                         |
| 1      | 1346 to 3458   | `skillawakeningability.dbss`       | 15,646 | 96 Row       | 108 to 268, 163 on average |
| 1      | 1346 to 3458   | `skillawakeningabilityoffset.dbss` | 1,156  | 96 Index Row | 12                         |

| Layout | File                               | Known            | Unknown      |
| ------ | ---------------------------------- | ---------------- | ------------ |
| 2      | `skillawakeningability.dbss`       | 15,454 B (97.6%) | 384 B (2.4%) |
| 2      | `skillawakeningabilityoffset.dbss` | 1,156 B (100.0%) | 0 B (0.0%)   |
| 1      | `skillawakeningability.dbss`       | 15,262 B (97.5%) | 384 B (2.5%) |
| 1      | `skillawakeningabilityoffset.dbss` | 1,156 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `e8617d28d233`  |
| 3482   | Layout 2             | `e8617d28d233`  |
| 3474   | Layout 2             | `e8617d28d233`  |
| 3473   | Layout 2             | `e8617d28d233`  |
| 3464   | Layout 2             | `e8617d28d233`  |
| 3458   | Layout 1             | `e8617d28d233`  |
| 3454   | Layout 1             | `e8617d28d233`  |
| 3444   | Layout 1             | `e8617d28d233`  |
| 3435   | Layout 1             | `e8617d28d233`  |
| 3426   | Layout 1             | `e8617d28d233`  |
| 3418   | Layout 1             | `e8617d28d233`  |
| 3412   | Layout 1             | `e8617d28d233`  |
| 3402   | Layout 1             | `e8617d28d233`  |
| 3396   | Layout 1             | `e8617d28d233`  |
| 3387   | Layout 1             | `e8617d28d233`  |
| 3381   | Layout 1             | `e8617d28d233`  |
| 3373   | Layout 1             | `e8617d28d233`  |
| 3364   | Layout 1             | `e8617d28d233`  |
| 3356   | Layout 1             | `e8617d28d233`  |
| 3349   | Layout 1             | `e8617d28d233`  |
| 3342   | Layout 1             | `e8617d28d233`  |
| 3335   | Layout 1             | `e8617d28d233`  |
| 3326   | Layout 1             | `e8617d28d233`  |
| 3321   | Layout 1             | `e8617d28d233`  |
| 3314   | Layout 1             | `e8617d28d233`  |
| 3303   | Layout 1             | `e8617d28d233`  |
| 3302   | Layout 1             | `e8617d28d233`  |
| 3293   | Layout 1             | `e8617d28d233`  |
| 3283   | Layout 1             | `e8617d28d233`  |
| 3275   | Layout 1             | `e8617d28d233`  |
| 3267   | Layout 1             | `e8617d28d233`  |
| 3258   | Layout 1             | `e8617d28d233`  |
| 3251   | Layout 1             | `e8617d28d233`  |
| 3242   | Layout 1             | `e8617d28d233`  |
| 3235   | Layout 1             | `e8617d28d233`  |
| 3229   | Layout 1             | `e8617d28d233`  |
| 3212   | Layout 1             | `e8617d28d233`  |
| 3203   | Layout 1             | `e8617d28d233`  |
| 3193   | Layout 1             | `e8617d28d233`  |
| 3186   | Layout 1             | `e8617d28d233`  |
| 3177   | Layout 1             | `e8617d28d233`  |
| 3169   | Layout 1             | `e8617d28d233`  |
| 3158   | Layout 1             | `e8617d28d233`  |
| 3151   | Layout 1             | `e8617d28d233`  |
| 3144   | Layout 1             | `e8617d28d233`  |
| 3133   | Layout 1             | `e8617d28d233`  |
| 3125   | Layout 1             | `e8617d28d233`  |
| 3118   | Layout 1             | `e8617d28d233`  |
| 3111   | Layout 1             | `e8617d28d233`  |
| 3103   | Layout 1             | `e8617d28d233`  |
| 3095   | Layout 1             | `e8617d28d233`  |
| 3086   | Layout 1             | `e8617d28d233`  |
| 3072   | Layout 1             | `e8617d28d233`  |
| 3062   | Layout 1             | `e8617d28d233`  |
| 3052   | Layout 1             | `e8617d28d233`  |
| 3045   | Layout 1             | `e8617d28d233`  |
| 3037   | Layout 1             | `e8617d28d233`  |
| 3030   | Layout 1             | `e8617d28d233`  |
| 3021   | Layout 1             | `e8617d28d233`  |
| 3012   | Layout 1             | `e8617d28d233`  |
| 3002   | Layout 1             | `e8617d28d233`  |
| 2995   | Layout 1             | `e8617d28d233`  |
| 2987   | Layout 1             | `e8617d28d233`  |
| 2978   | Layout 1             | `e8617d28d233`  |
| 2970   | Layout 1             | `e8617d28d233`  |
| 2959   | Layout 1             | `e8617d28d233`  |
| 2951   | Layout 1             | `e8617d28d233`  |
| 2942   | Layout 1             | `e8617d28d233`  |
| 2935   | Layout 1             | `e8617d28d233`  |
| 2932   | Layout 1             | `e8617d28d233`  |
| 2923   | Layout 1             | `e8617d28d233`  |
| 2919   | Layout 1             | `e8617d28d233`  |
| 2907   | Layout 1             | `e8617d28d233`  |
| 2900   | Layout 1             | `e8617d28d233`  |
| 2891   | Layout 1             | `e8617d28d233`  |
| 2882   | Layout 1             | `e8617d28d233`  |
| 2872   | Layout 1             | `e8617d28d233`  |
| 2863   | Layout 1             | `e8617d28d233`  |
| 2855   | Layout 1             | `e8617d28d233`  |
| 2849   | Layout 1             | `e8617d28d233`  |
| 2844   | Layout 1             | `e8617d28d233`  |
| 2834   | Layout 1             | `e8617d28d233`  |
| 2825   | Layout 1             | `e8617d28d233`  |
| 2819   | Layout 1             | `e8617d28d233`  |
| 2811   | Layout 1             | `e8617d28d233`  |
| 2803   | Layout 1             | `e8617d28d233`  |
| 2794   | Layout 1             | `e8617d28d233`  |
| 2783   | Layout 1             | `e8617d28d233`  |
| 2774   | Layout 1             | `e8617d28d233`  |
| 2765   | Layout 1             | `e8617d28d233`  |
| 2756   | Layout 1             | `e8617d28d233`  |
| 2750   | Layout 1             | `e8617d28d233`  |
| 2743   | Layout 1             | `e8617d28d233`  |
| 2736   | Layout 1             | `e8617d28d233`  |
| 2726   | Layout 1             | `e8617d28d233`  |
| 2717   | Layout 1             | `e8617d28d233`  |
| 2709   | Layout 1             | `e8617d28d233`  |
| 2703   | Layout 1             | `e8617d28d233`  |
| 2695   | Layout 1             | `e8617d28d233`  |
| 2684   | Layout 1             | `e8617d28d233`  |
| 2672   | Layout 1             | `e8617d28d233`  |
| 2665   | Layout 1             | `e8617d28d233`  |
| 2657   | Layout 1             | `e8617d28d233`  |
| 2649   | Layout 1             | `e8617d28d233`  |
| 2644   | Layout 1             | `e8617d28d233`  |
| 2637   | Layout 1             | `e8617d28d233`  |
| 2629   | Layout 1             | `e8617d28d233`  |
| 2619   | Layout 1             | `e8617d28d233`  |
| 2612   | Layout 1             | `e8617d28d233`  |
| 2606   | Layout 1             | `e8617d28d233`  |
| 2602   | Layout 1             | `e8617d28d233`  |
| 2601   | Layout 1             | `e8617d28d233`  |
| 2592   | Layout 1             | `e8617d28d233`  |
| 2583   | Layout 1             | `e8617d28d233`  |
| 2575   | Layout 1             | `e8617d28d233`  |
| 2567   | Layout 1             | `e8617d28d233`  |
| 2560   | Layout 1             | `e8617d28d233`  |
| 2553   | Layout 1             | `e8617d28d233`  |
| 2545   | Layout 1             | `e8617d28d233`  |
| 2538   | Layout 1             | `e8617d28d233`  |
| 2529   | Layout 1             | `e8617d28d233`  |
| 2519   | Layout 1             | `e8617d28d233`  |
| 2513   | Layout 1             | `e8617d28d233`  |
| 2510   | Layout 1             | `e8617d28d233`  |
| 2507   | Layout 1             | `e8617d28d233`  |
| 2503   | Layout 1             | `e8617d28d233`  |
| 2498   | Layout 1             | `e8617d28d233`  |
| 2492   | Layout 1             | `e8617d28d233`  |
| 2487   | Layout 1             | `e8617d28d233`  |
| 2480   | Layout 1             | `e8617d28d233`  |
| 2474   | Layout 1             | `e8617d28d233`  |
| 2468   | Layout 1             | `e8617d28d233`  |
| 2460   | Layout 1             | `e8617d28d233`  |
| 2453   | Layout 1             | `e8617d28d233`  |
| 2444   | Layout 1             | `e8617d28d233`  |
| 2438   | Layout 1             | `e8617d28d233`  |
| 2434   | Layout 1             | `e8617d28d233`  |
| 2429   | Layout 1             | `e8617d28d233`  |
| 2421   | Layout 1             | `e8617d28d233`  |
| 2414   | Layout 1             | `e8617d28d233`  |
| 2407   | Layout 1             | `e8617d28d233`  |
| 2401   | Layout 1             | `e8617d28d233`  |
| 2397   | Layout 1             | `e8617d28d233`  |
| 2393   | Layout 1             | `e8617d28d233`  |
| 2384   | Layout 1             | `e8617d28d233`  |
| 2378   | Layout 1             | `e8617d28d233`  |
| 2372   | Layout 1             | `e8617d28d233`  |
| 2358   | Layout 1             | `e8617d28d233`  |
| 2352   | Layout 1             | `e8617d28d233`  |
| 2347   | Layout 1             | `e8617d28d233`  |
| 2343   | Layout 1             | `e8617d28d233`  |
| 2335   | Layout 1             | `e8617d28d233`  |
| 2327   | Layout 1             | `e8617d28d233`  |
| 2324   | Layout 1             | `e8617d28d233`  |
| 2319   | Layout 1             | `e8617d28d233`  |
| 2313   | Layout 1             | `e8617d28d233`  |
| 2308   | Layout 1             | `e8617d28d233`  |
| 2302   | Layout 1             | `e8617d28d233`  |
| 2295   | Layout 1             | `e8617d28d233`  |
| 2290   | Layout 1             | `e8617d28d233`  |
| 2284   | Layout 1             | `e8617d28d233`  |
| 2276   | Layout 1             | `e8617d28d233`  |
| 2269   | Layout 1             | `e8617d28d233`  |
| 2259   | Layout 1             | `e8617d28d233`  |
| 2250   | Layout 1             | `e8617d28d233`  |
| 2243   | Layout 1             | `e8617d28d233`  |
| 2235   | Layout 1             | `e8617d28d233`  |
| 2229   | Layout 1             | `e8617d28d233`  |
| 2224   | Layout 1             | `e8617d28d233`  |
| 2218   | Layout 1             | `e8617d28d233`  |
| 2215   | Layout 1             | `e8617d28d233`  |
| 2207   | Layout 1             | `e8617d28d233`  |
| 2203   | Layout 1             | `e8617d28d233`  |
| 2196   | Layout 1             | `e8617d28d233`  |
| 2192   | Layout 1             | `e8617d28d233`  |
| 2189   | Layout 1             | `e8617d28d233`  |
| 2183   | Layout 1             | `e8617d28d233`  |
| 2179   | Layout 1             | `e8617d28d233`  |
| 2171   | Layout 1             | `e8617d28d233`  |
| 2163   | Layout 1             | `e8617d28d233`  |
| 2156   | Layout 1             | `e8617d28d233`  |
| 2151   | Layout 1             | `e8617d28d233`  |
| 2147   | Layout 1             | `e8617d28d233`  |
| 2142   | Layout 1             | `e8617d28d233`  |
| 2138   | Layout 1             | `e8617d28d233`  |
| 2134   | Layout 1             | `e8617d28d233`  |
| 2130   | Layout 1             | `e8617d28d233`  |
| 2122   | Layout 1             | `e8617d28d233`  |
| 2107   | Layout 1             | `e8617d28d233`  |
| 2098   | Layout 1             | `e8617d28d233`  |
| 2089   | Layout 1             | `e8617d28d233`  |
| 2081   | Layout 1             | `e8617d28d233`  |
| 2073   | Layout 1             | `e8617d28d233`  |
| 2067   | Layout 1             | `e8617d28d233`  |
| 2063   | Layout 1             | `e8617d28d233`  |
| 2059   | Layout 1             | `e8617d28d233`  |
| 2052   | Layout 1             | `e8617d28d233`  |
| 2044   | Layout 1             | `e8617d28d233`  |
| 2039   | Layout 1             | `e8617d28d233`  |
| 2032   | Layout 1             | `e8617d28d233`  |
| 2025   | Layout 1             | `e8617d28d233`  |
| 2011   | Layout 1             | `e8617d28d233`  |
| 2005   | Layout 1             | `e8617d28d233`  |
| 2000   | Layout 1             | `e8617d28d233`  |
| 1996   | Layout 1             | `e8617d28d233`  |
| 1991   | Layout 1             | `e8617d28d233`  |
| 1985   | Layout 1             | `e8617d28d233`  |
| 1980   | Layout 1             | `e8617d28d233`  |
| 1969   | Layout 1             | `e8617d28d233`  |
| 1964   | Layout 1             | `e8617d28d233`  |
| 1958   | Layout 1             | `e8617d28d233`  |
| 1950   | Layout 1             | `e8617d28d233`  |
| 1945   | Layout 1             | `e8617d28d233`  |
| 1937   | Layout 1             | `e8617d28d233`  |
| 1933   | Layout 1             | `e8617d28d233`  |
| 1927   | Layout 1             | `e8617d28d233`  |
| 1921   | Layout 1             | `e8617d28d233`  |
| 1914   | Layout 1             | `e8617d28d233`  |
| 1908   | Layout 1             | `e8617d28d233`  |
| 1897   | Layout 1             | `e8617d28d233`  |
| 1892   | Layout 1             | `e8617d28d233`  |
| 1886   | Layout 1             | `e8617d28d233`  |
| 1881   | Layout 1             | `e8617d28d233`  |
| 1871   | Layout 1             | `e8617d28d233`  |
| 1866   | Layout 1             | `e8617d28d233`  |
| 1862   | Layout 1             | `e8617d28d233`  |
| 1854   | Layout 1             | `e8617d28d233`  |
| 1846   | Layout 1             | `e8617d28d233`  |
| 1838   | Layout 1             | `e8617d28d233`  |
| 1832   | Layout 1             | `e8617d28d233`  |
| 1826   | Layout 1             | `e8617d28d233`  |
| 1822   | Layout 1             | `e8617d28d233`  |
| 1818   | Layout 1             | `e8617d28d233`  |
| 1804   | Layout 1             | `e8617d28d233`  |
| 1794   | Layout 1             | `e8617d28d233`  |
| 1790   | Layout 1             | `e8617d28d233`  |
| 1784   | Layout 1             | `e8617d28d233`  |
| 1774   | Layout 1             | `e8617d28d233`  |
| 1771   | Layout 1             | `e8617d28d233`  |
| 1762   | Layout 1             | `e8617d28d233`  |
| 1759   | Layout 1             | `e8617d28d233`  |
| 1754   | Layout 1             | `e8617d28d233`  |
| 1749   | Layout 1             | `e8617d28d233`  |
| 1743   | Layout 1             | `e8617d28d233`  |
| 1737   | Layout 1             | `e8617d28d233`  |
| 1731   | Layout 1             | `e8617d28d233`  |
| 1725   | Layout 1             | `e8617d28d233`  |
| 1717   | Layout 1             | `e8617d28d233`  |
| 1710   | Layout 1             | `e8617d28d233`  |
| 1704   | Layout 1             | `e8617d28d233`  |
| 1698   | Layout 1             | `e8617d28d233`  |
| 1690   | Layout 1             | `e8617d28d233`  |
| 1685   | Layout 1             | `e8617d28d233`  |
| 1680   | Layout 1             | `e8617d28d233`  |
| 1674   | Layout 1             | `e8617d28d233`  |
| 1668   | Layout 1             | `e8617d28d233`  |
| 1659   | Layout 1             | `e8617d28d233`  |
| 1649   | Layout 1             | `e8617d28d233`  |
| 1642   | Layout 1             | `e8617d28d233`  |
| 1636   | Layout 1             | `e8617d28d233`  |
| 1628   | Layout 1             | `e8617d28d233`  |
| 1622   | Layout 1             | `e8617d28d233`  |
| 1614   | Layout 1             | `e8617d28d233`  |
| 1608   | Layout 1             | `e8617d28d233`  |
| 1602   | Layout 1             | `e8617d28d233`  |
| 1598   | Layout 1             | `e8617d28d233`  |
| 1594   | Layout 1             | `e8617d28d233`  |
| 1590   | Layout 1             | `e8617d28d233`  |
| 1587   | Layout 1             | `e8617d28d233`  |
| 1584   | Layout 1             | `e8617d28d233`  |
| 1579   | Layout 1             | `e8617d28d233`  |
| 1572   | Layout 1             | `e8617d28d233`  |
| 1565   | Layout 1             | `e8617d28d233`  |
| 1559   | Layout 1             | `e8617d28d233`  |
| 1554   | Layout 1             | `e8617d28d233`  |
| 1547   | Layout 1             | `e8617d28d233`  |
| 1537   | Layout 1             | `e8617d28d233`  |
| 1529   | Layout 1             | `e8617d28d233`  |
| 1524   | Layout 1             | `e8617d28d233`  |
| 1519   | Layout 1             | `e8617d28d233`  |
| 1509   | Layout 1             | `e8617d28d233`  |
| 1506   | Layout 1             | `e8617d28d233`  |
| 1504   | Layout 1             | `e8617d28d233`  |
| 1500   | Layout 1             | `e8617d28d233`  |
| 1493   | Layout 1             | `e8617d28d233`  |
| 1489   | Layout 1             | `e8617d28d233`  |
| 1485   | Layout 1             | `e8617d28d233`  |
| 1481   | Layout 1             | `e8617d28d233`  |
| 1474   | Layout 1             | `e8617d28d233`  |
| 1466   | Layout 1             | `e8617d28d233`  |
| 1462   | Layout 1             | `e8617d28d233`  |
| 1459   | Layout 1             | `e8617d28d233`  |
| 1453   | Layout 1             | `e8617d28d233`  |
| 1450   | Layout 1             | `e8617d28d233`  |
| 1445   | Layout 1             | `e8617d28d233`  |
| 1439   | Layout 1             | `e8617d28d233`  |
| 1433   | Layout 1             | `e8617d28d233`  |
| 1430   | Layout 1             | `e8617d28d233`  |
| 1426   | Layout 1             | `e8617d28d233`  |
| 1421   | Layout 1             | `e8617d28d233`  |
| 1417   | Layout 1             | `e8617d28d233`  |
| 1416   | Layout 1             | `e8617d28d233`  |
| 1409   | Layout 1             | `e8617d28d233`  |
| 1405   | Layout 1             | `e8617d28d233`  |
| 1401   | Layout 1             | `e8617d28d233`  |
| 1396   | Layout 1             | `e8617d28d233`  |
| 1391   | Layout 1             | `e8617d28d233`  |
| 1390   | Layout 1             | `e8617d28d233`  |
| 1386   | Layout 1             | `e8617d28d233`  |
| 1381   | Layout 1             | `e8617d28d233`  |
| 1379   | Layout 1             | `e8617d28d233`  |
| 1372   | Layout 1             | `e8617d28d233`  |
| 1366   | Layout 1             | `e8617d28d233`  |
| 1364   | Layout 1             | `e8617d28d233`  |
| 1363   | Layout 1             | `e8617d28d233`  |
| 1360   | Layout 1             | `e8617d28d233`  |
| 1358   | Layout 1             | `e8617d28d233`  |
| 1355   | Layout 1             | `e8617d28d233`  |
| 1351   | Layout 1             | `e8617d28d233`  |
| 1348   | Layout 1             | `e8617d28d233`  |
| 1346   | Layout 1             | `e8617d28d233`  |
| 1341   | No documented layout | `e8617d28d233`  |
| 1340   | No documented layout | `e8617d28d233`  |
| 1338   | No documented layout | `e8617d28d233`  |
| 1335   | No documented layout | `e8617d28d233`  |
| 1333   | No documented layout | `e8617d28d233`  |
| 1329   | No documented layout | `e8617d28d233`  |
| 1327   | No documented layout | `e8617d28d233`  |
| 1324   | No documented layout | `e8617d28d233`  |
| 1321   | No documented layout | `e8617d28d233`  |
| 1319   | No documented layout | `e8617d28d233`  |
| 1318   | No documented layout | `e8617d28d233`  |
| 1316   | No documented layout | `e8617d28d233`  |
| 1313   | No documented layout | `e8617d28d233`  |
| 1311   | No documented layout | `e8617d28d233`  |
| 1309   | No documented layout | `e8617d28d233`  |
| 1304   | No documented layout | `e8617d28d233`  |
| 1292   | No documented layout | `e8617d28d233`  |
| 1286   | No file              | `e8617d28d233`  |
| 1280   | No file              | `e8617d28d233`  |
| 1276   | No file              | `e8617d28d233`  |
| 1267   | No file              | `e8617d28d233`  |
| 1261   | No file              | `e8617d28d233`  |
| 1256   | No file              | `e8617d28d233`  |
| 1250   | No file              | `e8617d28d233`  |
| 1246   | No file              | `e8617d28d233`  |
| 1239   | No file              | `e8617d28d233`  |
| 1230   | No file              | `e8617d28d233`  |
| 1226   | No file              | `e8617d28d233`  |
| 1220   | No file              | `e8617d28d233`  |
| 1217   | No file              | `e8617d28d233`  |
| 1211   | No file              | `e8617d28d233`  |
| 1210   | No file              | `e8617d28d233`  |
| 1208   | No file              | `e8617d28d233`  |
| 1203   | No file              | `e8617d28d233`  |
| 1197   | No file              | `e8617d28d233`  |
| 1194   | No file              | `e8617d28d233`  |
| 1192   | No file              | `e8617d28d233`  |
| 1187   | No file              | `e8617d28d233`  |
| 1183   | No file              | `e8617d28d233`  |
| 1177   | No file              | `e8617d28d233`  |
| 1173   | No file              | `e8617d28d233`  |
| 1167   | No file              | `e8617d28d233`  |
| 1164   | No file              | `e8617d28d233`  |
| 1156   | No file              | `e8617d28d233`  |
| 1149   | No file              | `e8617d28d233`  |
| 1144   | No file              | `e8617d28d233`  |
| 1137   | No file              | `e8617d28d233`  |
| 1132   | No file              | `e8617d28d233`  |
| 1127   | No file              | `e8617d28d233`  |
| 1122   | No file              | `e8617d28d233`  |
| 1118   | No file              | `e8617d28d233`  |
| 1114   | No file              | `e8617d28d233`  |
| 1109   | No file              | `e8617d28d233`  |
| 1102   | No file              | `e8617d28d233`  |
| 1096   | No file              | `e8617d28d233`  |
| 1088   | No file              | `e8617d28d233`  |
| 1081   | No file              | `e8617d28d233`  |
| 1076   | No file              | `e8617d28d233`  |
| 1069   | No file              | `e8617d28d233`  |
| 1064   | No file              | `e8617d28d233`  |
| 1058   | No file              | `e8617d28d233`  |
| 1051   | No file              | `e8617d28d233`  |
| 1044   | No file              | `e8617d28d233`  |
| 1036   | No file              | `e8617d28d233`  |
| 1026   | No file              | `e8617d28d233`  |
| 1016   | No file              | `e8617d28d233`  |
| 1009   | No file              | `e8617d28d233`  |
| 1005   | No file              | `e8617d28d233`  |
| 1000   | No file              | `e8617d28d233`  |
| 998    | No file              | `e8617d28d233`  |
| 990    | No file              | `e8617d28d233`  |
| 979    | No file              | `e8617d28d233`  |
| 972    | No file              | `e8617d28d233`  |
| 963    | No file              | `e8617d28d233`  |
| 955    | No file              | `e8617d28d233`  |
| 946    | No file              | `e8617d28d233`  |
| 938    | No file              | `e8617d28d233`  |
| 927    | No file              | `e8617d28d233`  |
| 911    | No file              | `e8617d28d233`  |
| 904    | No file              | `e8617d28d233`  |
| 899    | No file              | `e8617d28d233`  |
| 894    | No file              | `e8617d28d233`  |
| 885    | No file              | `e8617d28d233`  |
| 879    | No file              | `e8617d28d233`  |
| 872    | No file              | `e8617d28d233`  |
| 864    | No file              | `e8617d28d233`  |
| 855    | No file              | `e8617d28d233`  |
| 853    | No file              | `e8617d28d233`  |
| 845    | No file              | `e8617d28d233`  |
| 837    | No file              | `e8617d28d233`  |
| 829    | No file              | `e8617d28d233`  |
| 822    | No file              | `e8617d28d233`  |
| 814    | No file              | `e8617d28d233`  |
| 805    | No file              | `e8617d28d233`  |
| 794    | No file              | `e8617d28d233`  |
| 787    | No file              | `e8617d28d233`  |
| 780    | No file              | `e8617d28d233`  |
| 771    | No file              | `e8617d28d233`  |
| 760    | No file              | `e8617d28d233`  |
| 748    | No file              | `e8617d28d233`  |
| 741    | No file              | `e8617d28d233`  |
| 736    | No file              | `e8617d28d233`  |
| 731    | No file              | `e8617d28d233`  |
| 723    | No file              | `e8617d28d233`  |
| 711    | No file              | `e8617d28d233`  |
| 707    | No file              | `e8617d28d233`  |
| 697    | No file              | `e8617d28d233`  |
| 689    | No file              | `e8617d28d233`  |
| 683    | No file              | `e8617d28d233`  |
| 678    | No file              | `e8617d28d233`  |
| 670    | No file              | `e8617d28d233`  |
| 661    | No file              | `e8617d28d233`  |
| 656    | No file              | `e8617d28d233`  |
| 652    | No file              | `e8617d28d233`  |
| 643    | No file              | `e8617d28d233`  |
| 637    | No file              | `e8617d28d233`  |
| 630    | No file              | `e8617d28d233`  |
| 627    | No file              | `e8617d28d233`  |
| 621    | No file              | `e8617d28d233`  |
| 617    | No file              | `e8617d28d233`  |
| 615    | No file              | `e8617d28d233`  |
| 606    | No file              | `e8617d28d233`  |
| 599    | No file              | `e8617d28d233`  |
| 592    | No file              | `e8617d28d233`  |
| 586    | No file              | `e8617d28d233`  |
| 577    | No file              | `e8617d28d233`  |
| 569    | No file              | `e8617d28d233`  |
| 561    | No file              | `e8617d28d233`  |
| 554    | No file              | `e8617d28d233`  |
| 542    | No file              | `e8617d28d233`  |
| 532    | No file              | `e8617d28d233`  |
| 531    | No file              | `e8617d28d233`  |
| 526    | No file              | `e8617d28d233`  |
| 521    | No file              | `e8617d28d233`  |
| 517    | No file              | `e8617d28d233`  |
| 510    | No file              | `e8617d28d233`  |
| 508    | No file              | `e8617d28d233`  |
| 504    | No file              | `e8617d28d233`  |
| 497    | No file              | `e8617d28d233`  |
| 491    | No file              | `e8617d28d233`  |
| 485    | No file              | `e8617d28d233`  |
| 478    | No file              | `e8617d28d233`  |
| 472    | No file              | `e8617d28d233`  |
| 466    | No file              | `e8617d28d233`  |
| 457    | No file              | `e8617d28d233`  |
| 452    | No file              | `e8617d28d233`  |
| 449    | No file              | `e8617d28d233`  |
| 435    | No file              | `e8617d28d233`  |

<!-- versions:end -->

## Companion Files

None. The rows are read in file order from the count;
`skillawakeningabilityoffset.dbss` (below) only says where each row sits.
LOC type 33 holds the English description of each ability index (see
Field Names), and LOC type 5 the buff text.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 24 bytes + description text)

| Offset                | Type  | Field                     | Notes                                                                 |
| --------------------- | ----- | ------------------------- | --------------------------------------------------------------------- |
| `+0x00`               | u32   | ability_index             | The row key, from `1`; LOC type 33 `str_id1`                          |
| `+0x04`               | u32   | ability_index_dup         | Equal to `ability_index` on every row; the offset index points here   |
| `+0x08`               | u32   | buff_id                   | The `buff.dbss` buff the effect applies                               |
| `+0x0C`               | str16 | description_kr            | Korean effect text with `<PAColor>` tags                              |
| `description_kr+0x00` | u32   | unknown_description_kr_00 | `0` on every row of clients 1784 and 3482; see Open Questions         |

### `skillawakeningabilityoffset.dbss`

A bare index: no `PABR` magic and no trailer. Read by
`parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type             | Field | Notes                          |
| ------- | ---------------- | ----- | ------------------------------ |
| `+0x00` | u32              | count | Equals the main file's `count` |
| `+0x04` | Index Row[count] | rows  | See Index Row                  |

### Index Row (12 bytes)

| Offset  | Type | Field         | Notes                                       |
| ------- | ---- | ------------- | ------------------------------------------- |
| `+0x00` | u32  | ability_index | Key of the row it points at                 |
| `+0x04` | u32  | data_offset   | Row start + 4, at `ability_index_dup`       |
| `+0x08` | u32  | data_size     | The row less its leading `ability_index`    |

On clients 1784 and 3482 every index row points at the row with its key,
and the rows tile the file. Index and rows share one order, which is no
key order (96, 79 to 64, 95 to 80, 47 to 32, ... on client 3482).

## Layout 1

`buff_id` is a u16, as `_buffkey` in the 2016 `gc::SkillAwakeningAbilityStaticStatus`.

### Row (variable: 22 bytes + description text)

| Offset                | Type  | Field                     | Notes                                       |
| --------------------- | ----- | ------------------------- | ------------------------------------------- |
| `+0x00`               | u32   | ability_index             | The row key                                 |
| `+0x04`               | u32   | ability_index_dup         | Equal to `ability_index` on every row       |
| `+0x08`               | u16   | buff_id                   | The `buff.dbss` buff the effect applies     |
| `+0x0A`               | str16 | description_kr            | Korean effect text                          |
| `description_kr+0x00` | u32   | unknown_description_kr_00 | `0` on every row of client 1784             |

## Field Names

The `Awakening_Ability_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `Index`, `Buff`,
`BuffTarget`, `Description`, `VariedDirectDamage`, `VariedRangeDamage`,
`VariedMagicalDamage`, `VariedDirectHit`, `VariedRangeHit` and
`VariedMagicalHit`. Its 93 rows match the 93 rows of the official client
1784 file on `Index`, `Buff` and `Description` (93 of 93 each).

| Field          | Column        | Same value (client 1784) | Same value (client 3482) |
| -------------- | ------------- | ------------------------ | ------------------------ |
| ability_index  | `Index`       | 93 of 93                 | 93 of 93 (the file adds 94 to 96) |
| buff_id        | `Buff`        | 93 of 93                 | 21 of 93                 |
| description_kr | `Description` | 93 of 93                 | 0 of 93                  |

Client 3482 moved most rows to other buffs and rewrote every text, so
only the index carries over. `BuffTarget` (`0` self, `1` enemy, as
`gc::BuffTargetType`) is `1` on 51 sheet rows and `0` on 42, but
`unknown_description_kr_00` is `0` on all of them, so the column is not in
the file. The six `Varied*` columns are `<null>` on every sheet row.

The 2016 `gc::SkillAwakeningAbilityStaticStatus` has the members `_key`
(u32), `_buffkey` (u16, the width of Layout 1), `_buffTarget`,
`_description`, `_variedDamage` (3 f32) and `_variedHit` (3 f32).

LOC type 33 is the English `description_kr`: `str_id1` is the ability
index, the other ids `0`. Client 3482 has one string for each of the 96
indexes (index 96: "Target's recovery -40% for 7 sec").

## Notes

- `panel_window_reinforceskill_all_1.luac` and
  `panel_window_skillgroup_all_1.luac` (client 3482) read up to two
  add-ons per skill: `ToClient_GetAwakeningAbilityCount(skillNo)`, then
  `ToClient_GetAwakeningAbilityIndex(skillNo, i)` for each, and show
  `getSkillAwakenDescription(index)`. `index` is a position in the skill's
  option list: which ability indexes a skill offers, and in which order, is
  in [`skillawakeningability2.bss`](../bss/skillawakeningability2_bss.md).
- The Korean texts open with `자신` (self, 36 rows on client 3482), `상대`
  (target, 54 rows) or `타격` (on hit, 6 rows), which follows the sheet's
  `BuffTarget` on client 1784; the client gets the target from the buff.

## Open Questions

### What `unknown_description_kr_00` Holds

The u32 after the description is `0` on all 93 rows of client 1784 and all
96 rows of client 3482. The 2016 struct ends with the six `Varied*` floats,
which the sheet leaves empty; a u32 count of an empty list would read as
`0` too, but no row has a non-zero value to tell the two apart.
