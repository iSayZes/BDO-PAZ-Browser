# `skill.dbss` Format

## Purpose

The rule record of every skill rank: class skills, passives, item and event
skills, mount and guild skills. Each record carries the rank's cooldown, the
buffs it applies, an effect script, and the skills it leads to. This is the
middle link of the item effect chain: a consumable names a skill key, and
the skill names its buffs.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes     | Records                            | Row bytes                    |
| ------ | -------------- | ------- | ------------------ | --------- | ---------------------------------- | ---------------------------- |
| 3      | 3464 and later | 3483    | `skill.dbss`       | 9,781,356 | 30,547 Skill Record, 30,547 Record | 210 to 1,540, 316 on average |
| 3      | 3464 and later | 3483    | `skilloffset.dbss` | 366,584   | 30,547 Index Row                   | 12                           |
| 2      | 3242 to 3458   | 3458    | `skill.dbss`       | 9,128,941 | 30,424 Skill Record, 30,424 Record | 190 to 1,520, 296 on average |
| 2      | 3242 to 3458   | 3458    | `skilloffset.dbss` | 365,108   | 30,424 Index Row                   | 12                           |
| 1      | 1481 to 2243   | 2243    | `skill.dbss`       | 7,997,606 | 25,996 Skill Record, 25,996 Record | 190 to 1,320, 304 on average |
| 1      | 1481 to 2243   | 2243    | `skilloffset.dbss` | 311,972   | 25,996 Index Row                   | 12                           |

| Layout | File               | Known               | Unknown          |
| ------ | ------------------ | ------------------- | ---------------- |
| 3      | `skill.dbss`       | 9,506,433 B (97.2%) | 274,923 B (2.8%) |
| 3      | `skilloffset.dbss` | 366,584 B (100.0%)  | 0 B (0.0%)       |
| 2      | `skill.dbss`       | 8,855,125 B (97.0%) | 273,816 B (3.0%) |
| 2      | `skilloffset.dbss` | 365,108 B (100.0%)  | 0 B (0.0%)       |
| 1      | `skill.dbss`       | 7,867,626 B (98.4%) | 129,980 B (1.6%) |
| 1      | `skilloffset.dbss` | 311,972 B (100.0%)  | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 3             | `211a0e78bebb`  |
| 3482   | Layout 3             | `211a0e78bebb`  |
| 3474   | Layout 3             | `211a0e78bebb`  |
| 3473   | Layout 3             | `211a0e78bebb`  |
| 3464   | Layout 3             | `211a0e78bebb`  |
| 3458   | Layout 2             | `211a0e78bebb`  |
| 3454   | Layout 2             | `211a0e78bebb`  |
| 3444   | Layout 2             | `211a0e78bebb`  |
| 3435   | Layout 2             | `211a0e78bebb`  |
| 3426   | Layout 2             | `211a0e78bebb`  |
| 3418   | Layout 2             | `211a0e78bebb`  |
| 3412   | Layout 2             | `211a0e78bebb`  |
| 3402   | Layout 2             | `211a0e78bebb`  |
| 3396   | Layout 2             | `211a0e78bebb`  |
| 3387   | Layout 2             | `211a0e78bebb`  |
| 3381   | Layout 2             | `211a0e78bebb`  |
| 3373   | Layout 2             | `211a0e78bebb`  |
| 3364   | Layout 2             | `211a0e78bebb`  |
| 3356   | Layout 2             | `211a0e78bebb`  |
| 3349   | Layout 2             | `211a0e78bebb`  |
| 3342   | Layout 2             | `211a0e78bebb`  |
| 3335   | Layout 2             | `211a0e78bebb`  |
| 3326   | Layout 2             | `211a0e78bebb`  |
| 3321   | Layout 2             | `211a0e78bebb`  |
| 3314   | Layout 2             | `211a0e78bebb`  |
| 3303   | Layout 2             | `211a0e78bebb`  |
| 3302   | Layout 2             | `211a0e78bebb`  |
| 3293   | Layout 2             | `211a0e78bebb`  |
| 3283   | Layout 2             | `211a0e78bebb`  |
| 3275   | Layout 2             | `211a0e78bebb`  |
| 3267   | Layout 2             | `211a0e78bebb`  |
| 3258   | Layout 2             | `211a0e78bebb`  |
| 3251   | Layout 2             | `211a0e78bebb`  |
| 3242   | Layout 2             | `211a0e78bebb`  |
| 3235   | No documented layout | `211a0e78bebb`  |
| 3229   | No documented layout | `211a0e78bebb`  |
| 3212   | No documented layout | `211a0e78bebb`  |
| 3203   | No documented layout | `211a0e78bebb`  |
| 3193   | No documented layout | `211a0e78bebb`  |
| 3186   | No documented layout | `211a0e78bebb`  |
| 3177   | No documented layout | `211a0e78bebb`  |
| 3169   | No documented layout | `211a0e78bebb`  |
| 3158   | No documented layout | `211a0e78bebb`  |
| 3151   | No documented layout | `211a0e78bebb`  |
| 3144   | No documented layout | `211a0e78bebb`  |
| 3133   | No documented layout | `211a0e78bebb`  |
| 3125   | No documented layout | `211a0e78bebb`  |
| 3118   | No documented layout | `211a0e78bebb`  |
| 3111   | No documented layout | `211a0e78bebb`  |
| 3103   | No documented layout | `211a0e78bebb`  |
| 3095   | No documented layout | `211a0e78bebb`  |
| 3086   | No documented layout | `211a0e78bebb`  |
| 3072   | No documented layout | `211a0e78bebb`  |
| 3062   | No documented layout | `211a0e78bebb`  |
| 3052   | No documented layout | `211a0e78bebb`  |
| 3045   | No documented layout | `211a0e78bebb`  |
| 3037   | No documented layout | `211a0e78bebb`  |
| 3030   | No documented layout | `211a0e78bebb`  |
| 3021   | No documented layout | `211a0e78bebb`  |
| 3012   | No documented layout | `211a0e78bebb`  |
| 3002   | No documented layout | `211a0e78bebb`  |
| 2995   | No documented layout | `211a0e78bebb`  |
| 2987   | No documented layout | `211a0e78bebb`  |
| 2978   | No documented layout | `211a0e78bebb`  |
| 2970   | No documented layout | `211a0e78bebb`  |
| 2959   | No documented layout | `211a0e78bebb`  |
| 2951   | No documented layout | `211a0e78bebb`  |
| 2942   | No documented layout | `211a0e78bebb`  |
| 2935   | No documented layout | `211a0e78bebb`  |
| 2932   | No documented layout | `211a0e78bebb`  |
| 2923   | No documented layout | `211a0e78bebb`  |
| 2919   | No documented layout | `211a0e78bebb`  |
| 2907   | No documented layout | `211a0e78bebb`  |
| 2900   | No documented layout | `211a0e78bebb`  |
| 2891   | No documented layout | `211a0e78bebb`  |
| 2882   | No documented layout | `211a0e78bebb`  |
| 2872   | No documented layout | `211a0e78bebb`  |
| 2863   | No documented layout | `211a0e78bebb`  |
| 2855   | No documented layout | `211a0e78bebb`  |
| 2849   | No documented layout | `211a0e78bebb`  |
| 2844   | No documented layout | `211a0e78bebb`  |
| 2834   | No documented layout | `211a0e78bebb`  |
| 2825   | No documented layout | `211a0e78bebb`  |
| 2819   | No documented layout | `211a0e78bebb`  |
| 2811   | No documented layout | `211a0e78bebb`  |
| 2803   | No documented layout | `211a0e78bebb`  |
| 2794   | No documented layout | `211a0e78bebb`  |
| 2783   | No documented layout | `211a0e78bebb`  |
| 2774   | No documented layout | `211a0e78bebb`  |
| 2765   | No documented layout | `211a0e78bebb`  |
| 2756   | No documented layout | `211a0e78bebb`  |
| 2750   | No documented layout | `211a0e78bebb`  |
| 2743   | No documented layout | `211a0e78bebb`  |
| 2736   | No documented layout | `211a0e78bebb`  |
| 2726   | No documented layout | `211a0e78bebb`  |
| 2717   | No documented layout | `211a0e78bebb`  |
| 2709   | No documented layout | `211a0e78bebb`  |
| 2703   | No documented layout | `211a0e78bebb`  |
| 2695   | No documented layout | `211a0e78bebb`  |
| 2684   | No documented layout | `211a0e78bebb`  |
| 2672   | No documented layout | `211a0e78bebb`  |
| 2665   | No documented layout | `211a0e78bebb`  |
| 2657   | No documented layout | `211a0e78bebb`  |
| 2649   | No documented layout | `211a0e78bebb`  |
| 2644   | No documented layout | `211a0e78bebb`  |
| 2637   | No documented layout | `211a0e78bebb`  |
| 2629   | No documented layout | `211a0e78bebb`  |
| 2619   | No documented layout | `211a0e78bebb`  |
| 2612   | No documented layout | `211a0e78bebb`  |
| 2606   | No documented layout | `211a0e78bebb`  |
| 2602   | No documented layout | `211a0e78bebb`  |
| 2601   | No documented layout | `211a0e78bebb`  |
| 2592   | No documented layout | `211a0e78bebb`  |
| 2583   | No documented layout | `211a0e78bebb`  |
| 2575   | No documented layout | `211a0e78bebb`  |
| 2567   | No documented layout | `211a0e78bebb`  |
| 2560   | No documented layout | `211a0e78bebb`  |
| 2553   | No documented layout | `211a0e78bebb`  |
| 2545   | No documented layout | `211a0e78bebb`  |
| 2538   | No documented layout | `211a0e78bebb`  |
| 2529   | No documented layout | `211a0e78bebb`  |
| 2519   | No documented layout | `211a0e78bebb`  |
| 2513   | No documented layout | `211a0e78bebb`  |
| 2510   | No documented layout | `211a0e78bebb`  |
| 2507   | No documented layout | `211a0e78bebb`  |
| 2503   | No documented layout | `211a0e78bebb`  |
| 2498   | No documented layout | `211a0e78bebb`  |
| 2492   | No documented layout | `211a0e78bebb`  |
| 2487   | No documented layout | `211a0e78bebb`  |
| 2480   | No documented layout | `211a0e78bebb`  |
| 2474   | No documented layout | `211a0e78bebb`  |
| 2468   | No documented layout | `211a0e78bebb`  |
| 2460   | No documented layout | `211a0e78bebb`  |
| 2453   | No documented layout | `211a0e78bebb`  |
| 2444   | No documented layout | `211a0e78bebb`  |
| 2438   | No documented layout | `211a0e78bebb`  |
| 2434   | No documented layout | `211a0e78bebb`  |
| 2429   | No documented layout | `211a0e78bebb`  |
| 2421   | No documented layout | `211a0e78bebb`  |
| 2414   | No documented layout | `211a0e78bebb`  |
| 2407   | No documented layout | `211a0e78bebb`  |
| 2401   | No documented layout | `211a0e78bebb`  |
| 2397   | No documented layout | `211a0e78bebb`  |
| 2393   | No documented layout | `211a0e78bebb`  |
| 2384   | No documented layout | `211a0e78bebb`  |
| 2378   | No documented layout | `211a0e78bebb`  |
| 2372   | No documented layout | `211a0e78bebb`  |
| 2358   | No documented layout | `211a0e78bebb`  |
| 2352   | No documented layout | `211a0e78bebb`  |
| 2347   | No documented layout | `211a0e78bebb`  |
| 2343   | No documented layout | `211a0e78bebb`  |
| 2335   | No documented layout | `211a0e78bebb`  |
| 2327   | No documented layout | `211a0e78bebb`  |
| 2324   | No documented layout | `211a0e78bebb`  |
| 2319   | No documented layout | `211a0e78bebb`  |
| 2313   | No documented layout | `211a0e78bebb`  |
| 2308   | No documented layout | `211a0e78bebb`  |
| 2302   | No documented layout | `211a0e78bebb`  |
| 2295   | No documented layout | `211a0e78bebb`  |
| 2290   | No documented layout | `211a0e78bebb`  |
| 2284   | No documented layout | `211a0e78bebb`  |
| 2276   | No documented layout | `211a0e78bebb`  |
| 2269   | No documented layout | `211a0e78bebb`  |
| 2259   | No documented layout | `211a0e78bebb`  |
| 2250   | No documented layout | `211a0e78bebb`  |
| 2243   | Layout 1             | `211a0e78bebb`  |
| 2235   | Layout 1             | `211a0e78bebb`  |
| 2229   | Layout 1             | `211a0e78bebb`  |
| 2224   | Layout 1             | `211a0e78bebb`  |
| 2218   | Layout 1             | `211a0e78bebb`  |
| 2215   | Layout 1             | `211a0e78bebb`  |
| 2207   | Layout 1             | `211a0e78bebb`  |
| 2203   | Layout 1             | `211a0e78bebb`  |
| 2196   | Layout 1             | `211a0e78bebb`  |
| 2192   | Layout 1             | `211a0e78bebb`  |
| 2189   | Layout 1             | `211a0e78bebb`  |
| 2183   | Layout 1             | `211a0e78bebb`  |
| 2179   | Layout 1             | `211a0e78bebb`  |
| 2171   | Layout 1             | `211a0e78bebb`  |
| 2163   | Layout 1             | `211a0e78bebb`  |
| 2156   | Layout 1             | `211a0e78bebb`  |
| 2151   | Layout 1             | `211a0e78bebb`  |
| 2147   | Layout 1             | `211a0e78bebb`  |
| 2142   | Layout 1             | `211a0e78bebb`  |
| 2138   | Layout 1             | `211a0e78bebb`  |
| 2134   | Layout 1             | `211a0e78bebb`  |
| 2130   | Layout 1             | `211a0e78bebb`  |
| 2122   | Layout 1             | `211a0e78bebb`  |
| 2107   | Layout 1             | `211a0e78bebb`  |
| 2098   | Layout 1             | `211a0e78bebb`  |
| 2089   | Layout 1             | `211a0e78bebb`  |
| 2081   | Layout 1             | `211a0e78bebb`  |
| 2073   | Layout 1             | `211a0e78bebb`  |
| 2067   | Layout 1             | `211a0e78bebb`  |
| 2063   | Layout 1             | `211a0e78bebb`  |
| 2059   | Layout 1             | `211a0e78bebb`  |
| 2052   | Layout 1             | `211a0e78bebb`  |
| 2044   | Layout 1             | `211a0e78bebb`  |
| 2039   | Layout 1             | `211a0e78bebb`  |
| 2032   | Layout 1             | `211a0e78bebb`  |
| 2025   | Layout 1             | `211a0e78bebb`  |
| 2011   | Layout 1             | `211a0e78bebb`  |
| 2005   | Layout 1             | `211a0e78bebb`  |
| 2000   | Layout 1             | `211a0e78bebb`  |
| 1996   | Layout 1             | `211a0e78bebb`  |
| 1991   | Layout 1             | `211a0e78bebb`  |
| 1985   | Layout 1             | `211a0e78bebb`  |
| 1980   | Layout 1             | `211a0e78bebb`  |
| 1969   | Layout 1             | `211a0e78bebb`  |
| 1964   | Layout 1             | `211a0e78bebb`  |
| 1958   | Layout 1             | `211a0e78bebb`  |
| 1950   | Layout 1             | `211a0e78bebb`  |
| 1945   | Layout 1             | `211a0e78bebb`  |
| 1937   | Layout 1             | `211a0e78bebb`  |
| 1933   | Layout 1             | `211a0e78bebb`  |
| 1927   | Layout 1             | `211a0e78bebb`  |
| 1921   | Layout 1             | `211a0e78bebb`  |
| 1914   | Layout 1             | `211a0e78bebb`  |
| 1908   | Layout 1             | `211a0e78bebb`  |
| 1897   | Layout 1             | `211a0e78bebb`  |
| 1892   | Layout 1             | `211a0e78bebb`  |
| 1886   | Layout 1             | `211a0e78bebb`  |
| 1881   | Layout 1             | `211a0e78bebb`  |
| 1871   | Layout 1             | `211a0e78bebb`  |
| 1866   | Layout 1             | `211a0e78bebb`  |
| 1862   | Layout 1             | `211a0e78bebb`  |
| 1854   | Layout 1             | `211a0e78bebb`  |
| 1846   | Layout 1             | `211a0e78bebb`  |
| 1838   | Layout 1             | `211a0e78bebb`  |
| 1832   | Layout 1             | `211a0e78bebb`  |
| 1826   | Layout 1             | `211a0e78bebb`  |
| 1822   | Layout 1             | `211a0e78bebb`  |
| 1818   | Layout 1             | `211a0e78bebb`  |
| 1804   | Layout 1             | `211a0e78bebb`  |
| 1794   | Layout 1             | `211a0e78bebb`  |
| 1790   | Layout 1             | `211a0e78bebb`  |
| 1784   | Layout 1             | `211a0e78bebb`  |
| 1774   | Layout 1             | `211a0e78bebb`  |
| 1771   | Layout 1             | `211a0e78bebb`  |
| 1762   | Layout 1             | `211a0e78bebb`  |
| 1759   | Layout 1             | `211a0e78bebb`  |
| 1754   | Layout 1             | `211a0e78bebb`  |
| 1749   | Layout 1             | `211a0e78bebb`  |
| 1743   | Layout 1             | `211a0e78bebb`  |
| 1737   | Layout 1             | `211a0e78bebb`  |
| 1731   | Layout 1             | `211a0e78bebb`  |
| 1725   | Layout 1             | `211a0e78bebb`  |
| 1717   | Layout 1             | `211a0e78bebb`  |
| 1710   | Layout 1             | `211a0e78bebb`  |
| 1704   | Layout 1             | `211a0e78bebb`  |
| 1698   | Layout 1             | `211a0e78bebb`  |
| 1690   | Layout 1             | `211a0e78bebb`  |
| 1685   | Layout 1             | `211a0e78bebb`  |
| 1680   | Layout 1             | `211a0e78bebb`  |
| 1674   | Layout 1             | `211a0e78bebb`  |
| 1668   | Layout 1             | `211a0e78bebb`  |
| 1659   | Layout 1             | `211a0e78bebb`  |
| 1649   | Layout 1             | `211a0e78bebb`  |
| 1642   | Layout 1             | `211a0e78bebb`  |
| 1636   | Layout 1             | `211a0e78bebb`  |
| 1628   | Layout 1             | `211a0e78bebb`  |
| 1622   | Layout 1             | `211a0e78bebb`  |
| 1614   | Layout 1             | `211a0e78bebb`  |
| 1608   | Layout 1             | `211a0e78bebb`  |
| 1602   | Layout 1             | `211a0e78bebb`  |
| 1598   | Layout 1             | `211a0e78bebb`  |
| 1594   | Layout 1             | `211a0e78bebb`  |
| 1590   | Layout 1             | `211a0e78bebb`  |
| 1587   | Layout 1             | `211a0e78bebb`  |
| 1584   | Layout 1             | `211a0e78bebb`  |
| 1579   | Layout 1             | `211a0e78bebb`  |
| 1572   | Layout 1             | `211a0e78bebb`  |
| 1565   | Layout 1             | `211a0e78bebb`  |
| 1559   | Layout 1             | `211a0e78bebb`  |
| 1554   | Layout 1             | `211a0e78bebb`  |
| 1547   | Layout 1             | `211a0e78bebb`  |
| 1537   | Layout 1             | `211a0e78bebb`  |
| 1529   | Layout 1             | `211a0e78bebb`  |
| 1524   | Layout 1             | `211a0e78bebb`  |
| 1519   | Layout 1             | `211a0e78bebb`  |
| 1509   | Layout 1             | `211a0e78bebb`  |
| 1506   | Layout 1             | `211a0e78bebb`  |
| 1504   | Layout 1             | `211a0e78bebb`  |
| 1500   | Layout 1             | `211a0e78bebb`  |
| 1493   | Layout 1             | `211a0e78bebb`  |
| 1489   | Layout 1             | `211a0e78bebb`  |
| 1485   | Layout 1             | `211a0e78bebb`  |
| 1481   | Layout 1             | `211a0e78bebb`  |
| 1474   | No documented layout | `211a0e78bebb`  |
| 1466   | No documented layout | `211a0e78bebb`  |
| 1462   | No documented layout | `211a0e78bebb`  |
| 1459   | No documented layout | `211a0e78bebb`  |
| 1453   | No documented layout | `211a0e78bebb`  |
| 1450   | No documented layout | `211a0e78bebb`  |
| 1445   | No documented layout | `211a0e78bebb`  |
| 1439   | No documented layout | `211a0e78bebb`  |
| 1433   | No documented layout | `211a0e78bebb`  |
| 1430   | No documented layout | `211a0e78bebb`  |
| 1426   | No documented layout | `211a0e78bebb`  |
| 1421   | No documented layout | `211a0e78bebb`  |
| 1417   | No documented layout | `211a0e78bebb`  |
| 1416   | No documented layout | `211a0e78bebb`  |
| 1409   | No documented layout | `211a0e78bebb`  |
| 1405   | No documented layout | `211a0e78bebb`  |
| 1401   | No documented layout | `211a0e78bebb`  |
| 1396   | No documented layout | `211a0e78bebb`  |
| 1391   | No documented layout | `211a0e78bebb`  |
| 1390   | No documented layout | `211a0e78bebb`  |
| 1386   | No documented layout | `211a0e78bebb`  |
| 1381   | No documented layout | `211a0e78bebb`  |
| 1379   | No documented layout | `211a0e78bebb`  |
| 1372   | No documented layout | `211a0e78bebb`  |
| 1366   | No documented layout | `211a0e78bebb`  |
| 1364   | No documented layout | `211a0e78bebb`  |
| 1363   | No documented layout | `211a0e78bebb`  |
| 1360   | No documented layout | `211a0e78bebb`  |
| 1358   | No documented layout | `211a0e78bebb`  |
| 1355   | No documented layout | `211a0e78bebb`  |
| 1351   | No documented layout | `211a0e78bebb`  |
| 1348   | No documented layout | `211a0e78bebb`  |
| 1346   | No documented layout | `211a0e78bebb`  |
| 1341   | No documented layout | `211a0e78bebb`  |
| 1340   | No documented layout | `211a0e78bebb`  |
| 1338   | No documented layout | `211a0e78bebb`  |
| 1335   | No documented layout | `211a0e78bebb`  |
| 1333   | No documented layout | `211a0e78bebb`  |
| 1329   | No documented layout | `211a0e78bebb`  |
| 1327   | No documented layout | `211a0e78bebb`  |
| 1324   | No documented layout | `211a0e78bebb`  |
| 1321   | No documented layout | `211a0e78bebb`  |
| 1319   | No documented layout | `211a0e78bebb`  |
| 1318   | No documented layout | `211a0e78bebb`  |
| 1316   | No documented layout | `211a0e78bebb`  |
| 1313   | No documented layout | `211a0e78bebb`  |
| 1311   | No documented layout | `211a0e78bebb`  |
| 1309   | No documented layout | `211a0e78bebb`  |
| 1304   | No documented layout | `211a0e78bebb`  |
| 1292   | No documented layout | `211a0e78bebb`  |
| 1286   | No file              | `211a0e78bebb`  |
| 1280   | No file              | `211a0e78bebb`  |
| 1276   | No file              | `211a0e78bebb`  |
| 1267   | No file              | `211a0e78bebb`  |
| 1261   | No file              | `211a0e78bebb`  |
| 1256   | No file              | `211a0e78bebb`  |
| 1250   | No file              | `211a0e78bebb`  |
| 1246   | No file              | `211a0e78bebb`  |
| 1239   | No file              | `211a0e78bebb`  |
| 1230   | No file              | `211a0e78bebb`  |
| 1226   | No file              | `211a0e78bebb`  |
| 1220   | No file              | `211a0e78bebb`  |
| 1217   | No file              | `211a0e78bebb`  |
| 1211   | No file              | `211a0e78bebb`  |
| 1210   | No file              | `211a0e78bebb`  |
| 1208   | No file              | `211a0e78bebb`  |
| 1203   | No file              | `211a0e78bebb`  |
| 1197   | No file              | `211a0e78bebb`  |
| 1194   | No file              | `211a0e78bebb`  |
| 1192   | No file              | `211a0e78bebb`  |
| 1187   | No file              | `211a0e78bebb`  |
| 1183   | No file              | `211a0e78bebb`  |
| 1177   | No file              | `211a0e78bebb`  |
| 1173   | No file              | `211a0e78bebb`  |
| 1167   | No file              | `211a0e78bebb`  |
| 1164   | No file              | `211a0e78bebb`  |
| 1156   | No file              | `211a0e78bebb`  |
| 1149   | No file              | `211a0e78bebb`  |
| 1144   | No file              | `211a0e78bebb`  |
| 1137   | No file              | `211a0e78bebb`  |
| 1132   | No file              | `211a0e78bebb`  |
| 1127   | No file              | `211a0e78bebb`  |
| 1122   | No file              | `211a0e78bebb`  |
| 1118   | No file              | `211a0e78bebb`  |
| 1114   | No file              | `211a0e78bebb`  |
| 1109   | No file              | `211a0e78bebb`  |
| 1102   | No file              | `211a0e78bebb`  |
| 1096   | No file              | `211a0e78bebb`  |
| 1088   | No file              | `211a0e78bebb`  |
| 1081   | No file              | `211a0e78bebb`  |
| 1076   | No file              | `211a0e78bebb`  |
| 1069   | No file              | `211a0e78bebb`  |
| 1064   | No file              | `211a0e78bebb`  |
| 1058   | No file              | `211a0e78bebb`  |
| 1051   | No file              | `211a0e78bebb`  |
| 1044   | No file              | `211a0e78bebb`  |
| 1036   | No file              | `211a0e78bebb`  |
| 1026   | No file              | `211a0e78bebb`  |
| 1016   | No file              | `211a0e78bebb`  |
| 1009   | No file              | `211a0e78bebb`  |
| 1005   | No file              | `211a0e78bebb`  |
| 1000   | No file              | `211a0e78bebb`  |
| 998    | No file              | `211a0e78bebb`  |
| 990    | No file              | `211a0e78bebb`  |
| 979    | No file              | `211a0e78bebb`  |
| 972    | No file              | `211a0e78bebb`  |
| 963    | No file              | `211a0e78bebb`  |
| 955    | No file              | `211a0e78bebb`  |
| 946    | No file              | `211a0e78bebb`  |
| 938    | No file              | `211a0e78bebb`  |
| 927    | No file              | `211a0e78bebb`  |
| 911    | No file              | `211a0e78bebb`  |
| 904    | No file              | `211a0e78bebb`  |
| 899    | No file              | `211a0e78bebb`  |
| 894    | No file              | `211a0e78bebb`  |
| 885    | No file              | `211a0e78bebb`  |
| 879    | No file              | `211a0e78bebb`  |
| 872    | No file              | `211a0e78bebb`  |
| 864    | No file              | `211a0e78bebb`  |
| 855    | No file              | `211a0e78bebb`  |
| 853    | No file              | `211a0e78bebb`  |
| 845    | No file              | `211a0e78bebb`  |
| 837    | No file              | `211a0e78bebb`  |
| 829    | No file              | `211a0e78bebb`  |
| 822    | No file              | `211a0e78bebb`  |
| 814    | No file              | `211a0e78bebb`  |
| 805    | No file              | `211a0e78bebb`  |
| 794    | No file              | `211a0e78bebb`  |
| 787    | No file              | `211a0e78bebb`  |
| 780    | No file              | `211a0e78bebb`  |
| 771    | No file              | `211a0e78bebb`  |
| 760    | No file              | `211a0e78bebb`  |
| 748    | No file              | `211a0e78bebb`  |
| 741    | No file              | `211a0e78bebb`  |
| 736    | No file              | `211a0e78bebb`  |
| 731    | No file              | `211a0e78bebb`  |
| 723    | No file              | `211a0e78bebb`  |
| 711    | No file              | `211a0e78bebb`  |
| 707    | No file              | `211a0e78bebb`  |
| 697    | No file              | `211a0e78bebb`  |
| 689    | No file              | `211a0e78bebb`  |
| 683    | No file              | `211a0e78bebb`  |
| 678    | No file              | `211a0e78bebb`  |
| 670    | No file              | `211a0e78bebb`  |
| 661    | No file              | `211a0e78bebb`  |
| 656    | No file              | `211a0e78bebb`  |
| 652    | No file              | `211a0e78bebb`  |
| 643    | No file              | `211a0e78bebb`  |
| 637    | No file              | `211a0e78bebb`  |
| 630    | No file              | `211a0e78bebb`  |
| 627    | No file              | `211a0e78bebb`  |
| 621    | No file              | `211a0e78bebb`  |
| 617    | No file              | `211a0e78bebb`  |
| 615    | No file              | `211a0e78bebb`  |
| 606    | No file              | `211a0e78bebb`  |
| 599    | No file              | `211a0e78bebb`  |
| 592    | No file              | `211a0e78bebb`  |
| 586    | No file              | `211a0e78bebb`  |
| 577    | No file              | `211a0e78bebb`  |
| 569    | No file              | `211a0e78bebb`  |
| 561    | No file              | `211a0e78bebb`  |
| 554    | No file              | `211a0e78bebb`  |
| 542    | No file              | `211a0e78bebb`  |
| 532    | No file              | `211a0e78bebb`  |
| 531    | No file              | `211a0e78bebb`  |
| 526    | No file              | `211a0e78bebb`  |
| 521    | No file              | `211a0e78bebb`  |
| 517    | No file              | `211a0e78bebb`  |
| 510    | No file              | `211a0e78bebb`  |
| 508    | No file              | `211a0e78bebb`  |
| 504    | No file              | `211a0e78bebb`  |
| 497    | No file              | `211a0e78bebb`  |
| 491    | No file              | `211a0e78bebb`  |
| 485    | No file              | `211a0e78bebb`  |
| 478    | No file              | `211a0e78bebb`  |
| 472    | No file              | `211a0e78bebb`  |
| 466    | No file              | `211a0e78bebb`  |
| 457    | No file              | `211a0e78bebb`  |
| 452    | No file              | `211a0e78bebb`  |
| 449    | No file              | `211a0e78bebb`  |
| 435    | No file              | `211a0e78bebb`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                            |
| --------------------- | -------- | --------------------------------------------------------------- |
| `skilloffset.dbss`    | Required | `skill_key → (offset, size)` index into this file               |
| `buff.dbss`           | Optional | The buffs named by `buff_ids`                                   |
| `skilltype.dbss`      | Optional | Korean name, kind and icon of the same skill, see [`skilltype.dbss`](skilltype_dbss.md); the app reads name and icon through the `SKILL_NAME_KR` and `SKILL_ICON` lookup indexes |
| `languagedata_en.loc` | Optional | Skill names and descriptions, LOC type `10`, `str_id1 = skill_no`; each rank's own text, LOC type `13`, `str_id1 = skill_no`, `str_id2 = level` |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset  | Type          | Field   | Notes                                                    |
| ------- | ------------- | ------- | -------------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; matches the offset file               |
| `+0x04` | Record[count] | records | Each record is preceded by a repeated copy of its key   |

The records tile the file: each starts 4 bytes after the previous one ends
(the repeated key), the first at `8`, and the last ends at end of file.

Strings are a `u64` count followed by that many units: UTF-16LE for text and
scripts, single-byte ASCII for `action_name`. There is no terminator.

### Record (variable: 4 bytes + record)

| Offset  | Type         | Field      | Notes                                                       |
| ------- | ------------ | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32          | key_prefix | Repeated copy of the record's `skill_key`                   |
| `+0x04` | Skill Record | record     | `size` bytes; the index row's `offset` points at this field |

### Skill Record (variable: 210 bytes + text and key lists)

Offsets `action_name+0xNN` count from the end of `action_name`, called `N`
in the notes below; with an empty name `N` is `17`. The sheet columns and
server members behind the names are in Field Names.

| Offset                 | Type                   | Field               | Notes                                                           |
| ---------------------- | ---------------------- | ------------------- | --------------------------------------------------------------- |
| `+0x00`                | u32                    | skill_key           | Equals the index key                                            |
| `+0x04`                | u32                    | level_1_key         | `skill_no << 16 \| 1`, the key of the skill's `skilltype.dbss` record; equals `skill_key` except on the 82 keys above level 1 |
| `+0x08`                | u8                     | is_attack_skill     | `1` on 8,738 records (client 3474); equals `skillsimply.dbss` `unknown_e08`, see Field Names |
| `+0x09`                | str8                   | action_name         | ASCII action such as `SUMMON_BOSS`, `SETUP_QUESTITEM`; empty on 24,794 records |
| `action_name+0x00`     | u32                    | action_hash         | Hash of `action_name`; `0` when it is empty; one value per name (4,461 names) |
| `action_name+0x04`     | u8                     | is_prompt_for_learning | See Field Names                                              |
| `action_name+0x05`     | u16                    | need_skill_point    | Skill points it costs to learn                                  |
| `action_name+0x07`     | u32                    | need_level          | Character level needed to learn it                              |
| `action_name+0x0B`     | u64                    | need_money_for_learning | Always `0` on client 3474                                   |
| `action_name+0x13`     | u32                    | need_item_key_for_learning | Always `0` on client 3474                                |
| `action_name+0x17`     | u64                    | need_item_count_for_learning | Always `0` on client 3474                              |
| `action_name+0x1F`     | u16                    | need_skill_level_1  | Level of `need_skill_no_1`                                      |
| `action_name+0x21`     | u16                    | need_skill_no_1     | Skill number that must be learned first                         |
| `action_name+0x23`     | u16                    | need_skill_level_2  | Level of `need_skill_no_2`                                      |
| `action_name+0x25`     | u16                    | need_skill_no_2     | A second required skill                                         |
| `action_name+0x27`     | u8                     | do_require_point_need | `1` exactly where `require_hp`, `resource_cost` or `require_sub_resource_point` is set |
| `action_name+0x28`     | f32                    | require_hp          | HP the skill costs; see Field Names                             |
| `action_name+0x2C`     | u32                    | resource_cost       | MP or WP the skill costs, by class; `0` on 26,837 records, up to `660`; see below |
| `action_name+0x30`     | u32                    | require_sub_resource_point | Cost in the resource `sub_resource_type` names; see Field Names |
| `action_name+0x34`     | u8                     | sub_resource_type   | See Field Names                                                 |
| `action_name+0x35`     | u32                    | stamina_cost        | Stamina the skill costs; `0` on 26,635 records, `1` on 2,825, up to `600`; see below |
| `action_name+0x39`     | u32                    | need_item_key       | Always `0` on client 3474                                       |
| `action_name+0x3D`     | u64                    | need_item_count     | Always `0` on client 3474                                       |
| `action_name+0x45`     | u8                     | is_usable_when_alive | `0` only on revival skills, see Field Names                    |
| `action_name+0x46`     | u32                    | global_reuse_cycle  | Always `0` on client 3474; see Field Names                      |
| `action_name+0x4A`     | u16                    | reuse_group         | Set on 1,254 records (client 3474), 178 values; see Field Names |
| `action_name+0x4C`     | u16                    | unknown_n4c         | Always `0` on client 3474; not in Layout 1                      |
| `action_name+0x4E`     | u32                    | cooldown_ms         | Cooldown in milliseconds; `0` on 22,798 records, see Notes      |
| `action_name+0x52`     | u32[10]                | buff_ids            | `buff.dbss` IDs, zero-padded; see below                          |
| `action_name+0x7A`     | str16                  | description         | Korean description, UTF-16; empty on 21,114 records, `UNKNOWN` on 1,284, `<null>` on 43. The Korean source of LOC type `13` for the same `(skill_no, level)`, and often the same text as LOC type `10` `str_id4 = 1`, see Notes. Line breaks are stored as the two characters `\n` (873 on client 3458) and decoded by the parser |
| `description+0x00`     | str16                  | script              | UTF-16 effect script such as `DAM_ATT_2(...)`, `AWAKEN();`, `BATH();`; empty on 21,594 records |
| `script+0x00`          | u8                     | is_usable_while_in_cool_time | `1` on 1,020 records (client 3474); the tooltip Lua reads it with `isUsableWhileInCoolTime` |
| `script+0x01`          | u8                     | unknown_s01         | No column; see Open Questions                                  |
| `script+0x02`          | u8                     | is_expired_in_offline | See Field Names                                               |
| `script+0x03`          | u16                    | balance_channel_skill_no | Always `0` on client 3474                                  |
| `script+0x05`          | u8                     | is_developing_contents | See Field Names                                              |
| `script+0x06`          | u8                     | is_fusion           | `1` on the fusion skills                                        |
| `script+0x07`          | u8                     | enable_in_water     | `1` on 15 HP potion skills (client 3474); see Field Names      |
| `script+0x08`          | u32                    | preview_action_hash | Hash of the preview action name, `0` when there is none         |
| `script+0x0C`          | f32[3]                 | dummy_monster_distance | Three floats; see Field Names                                |
| `script+0x18`          | u32                    | black_skill_key     | Level 1 key of the skill's Black Spirit version                 |
| `script+0x1C`          | u32                    | adrenalin_point     | See Field Names                                                 |
| `script+0x20`          | u32                    | link_tooltip_skill_key | Level 1 key of the skill whose tooltip this skill links     |
| `script+0x24`          | u32                    | next_skill_count    | `0` on 25,209 records, `1` on 4,560; up to `75`, see below       |
| `script+0x28`          | u32[next_skill_count]  | next_skill_keys     | Skill keys this rank leads to, see below                        |
| `next_skill_keys+0x00` | u32                    | unknown_after_next_skill_keys | Always `0`                                            |
| `next_skill_keys+0x04` | u32                    | related_cool_time_skill_count | `1` on 150 records (client 3474), else `0`            |
| `next_skill_keys+0x08` | u32[related_cool_time_skill_count] | related_cool_time_skill_keys | Set on the Core skills, see below    |
| `related_cool_time_skill_keys+0x00` | f32       | target_search_angle | `-1.0` (no value) on 29,788 records (client 3474), else `0.0`   |
| `related_cool_time_skill_keys+0x04` | u8        | is_except_cool_time | `1` on 255 "Black Spirit:" records (client 3474), see `skillsimply.dbss` |
| `related_cool_time_skill_keys+0x05` | bytes[2]  | unknown_end         | Not in Layout 1; see Open Questions                            |

`need_level`, `need_skill_point`, `need_skill_no_1`, `need_skill_no_2`,
`is_fusion`, `is_except_cool_time` and `related_cool_time_skill_keys` (there
`base_skill_keys`) hold the same values as the `skillsimply.dbss` fields on
all 30,487 records of client 3474.

Every one of the 30,481 records on client 3464 walks to exactly its `size`
with this layout.

### `skilloffset.dbss`

| Offset              | Type             | Field        | Notes                                                 |
| ------------------- | ---------------- | ------------ | ----------------------------------------------------- |
| `+0x00`             | char[4]          | magic        | `PABR`                                                |
| `+0x04`             | u32              | count        | Number of index rows; `30424` on client 3458          |
| `+0x08`             | Index Row[count] | rows         | See Index Row                                         |
| `rows+0x00`         | String Table     | string_table | An empty PABR string table                            |
| `string_table+0x00` | u32              | rows_end     | End of the rows (`8 + 12 * count`)                    |
| `string_table+0x04` | u32              | zero         | Always `0`                                            |

Read it with `parse_pabr_u32_offset_rows()`.

### Index Row (12 bytes)

| Offset  | Type | Field     | Notes                                        |
| ------- | ---- | --------- | -------------------------------------------- |
| `+0x00` | u32  | skill_key | `skill_no << 16 \| level`                    |
| `+0x04` | u32  | offset    | Byte offset of the record in `skill.dbss`     |
| `+0x08` | u32  | size      | Record size in bytes                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 2

Before client 3464 the `buff_ids` slots were u16, so the Skill Record was 20
bytes shorter and `description` started at `N+102`; see `buff_ids`. Only the
Skill Record differs from Layout 3. The parser reads only Layout 3.

### Skill Record (variable: 190 bytes + text and key lists)

| Offset                 | Type                   | Field               | Notes |
| ---------------------- | ---------------------- | ------------------- | ----- |
| `+0x00`                | u32                    | skill_key           |       |
| `+0x04`                | u32                    | level_1_key         |       |
| `+0x08`                | u8                     | is_attack_skill     |       |
| `+0x09`                | str8                   | action_name         |       |
| `action_name+0x00`     | u32                    | action_hash         |       |
| `action_name+0x04`     | u8                     | is_prompt_for_learning |    |
| `action_name+0x05`     | u16                    | need_skill_point    |       |
| `action_name+0x07`     | u32                    | need_level          |       |
| `action_name+0x0B`     | u64                    | need_money_for_learning |   |
| `action_name+0x13`     | u32                    | need_item_key_for_learning | |
| `action_name+0x17`     | u64                    | need_item_count_for_learning | |
| `action_name+0x1F`     | u16                    | need_skill_level_1  |       |
| `action_name+0x21`     | u16                    | need_skill_no_1     |       |
| `action_name+0x23`     | u16                    | need_skill_level_2  |       |
| `action_name+0x25`     | u16                    | need_skill_no_2     |       |
| `action_name+0x27`     | u8                     | do_require_point_need |     |
| `action_name+0x28`     | f32                    | require_hp          |       |
| `action_name+0x2C`     | u32                    | resource_cost       |       |
| `action_name+0x30`     | u32                    | require_sub_resource_point | |
| `action_name+0x34`     | u8                     | sub_resource_type   |       |
| `action_name+0x35`     | u32                    | stamina_cost        |       |
| `action_name+0x39`     | u32                    | need_item_key       |       |
| `action_name+0x3D`     | u64                    | need_item_count     |       |
| `action_name+0x45`     | u8                     | is_usable_when_alive |      |
| `action_name+0x46`     | u32                    | global_reuse_cycle  |       |
| `action_name+0x4A`     | u16                    | reuse_group         |       |
| `action_name+0x4C`     | u16                    | unknown_n4c         |       |
| `action_name+0x4E`     | u32                    | cooldown_ms         |       |
| `action_name+0x52`     | u16[10]                | buff_ids            |       |
| `action_name+0x66`     | str16                  | description         |       |
| `description+0x00`     | str16                  | script              |       |
| `script+0x00`          | u8                     | is_usable_while_in_cool_time | |
| `script+0x01`          | u8                     | unknown_s01         |       |
| `script+0x02`          | u8                     | is_expired_in_offline |     |
| `script+0x03`          | u16                    | balance_channel_skill_no | |
| `script+0x05`          | u8                     | is_developing_contents |    |
| `script+0x06`          | u8                     | is_fusion           |       |
| `script+0x07`          | u8                     | enable_in_water     |       |
| `script+0x08`          | u32                    | preview_action_hash |       |
| `script+0x0C`          | f32[3]                 | dummy_monster_distance |    |
| `script+0x18`          | u32                    | black_skill_key     |       |
| `script+0x1C`          | u32                    | adrenalin_point     |       |
| `script+0x20`          | u32                    | link_tooltip_skill_key |    |
| `script+0x24`          | u32                    | next_skill_count    |       |
| `script+0x28`          | u32[next_skill_count]  | next_skill_keys     |       |
| `next_skill_keys+0x00` | u32                    | unknown_after_next_skill_keys |  |
| `next_skill_keys+0x04` | u32                    | related_cool_time_skill_count | |
| `next_skill_keys+0x08` | u32[related_cool_time_skill_count] | related_cool_time_skill_keys | |
| `related_cool_time_skill_keys+0x00` | f32       | target_search_angle |       |
| `related_cool_time_skill_keys+0x04` | u8        | is_except_cool_time |       |
| `related_cool_time_skill_keys+0x05` | bytes[2]  | unknown_end         |       |

## Layout 1

On client 1784 the record had no `unknown_n4c`, so `cooldown_ms`,
`buff_ids` and everything after them sat 2 bytes earlier than in Layout 2.
An empty `special_weapon_hit_effects` list followed
`related_cool_time_skill_keys`, and `unknown_end` did not exist yet. Only the
Skill Record differs from Layout 2. Field names keep Layout 3's offsets.

### Skill Record (variable: 190 bytes + text and key lists)

| Offset                 | Type                   | Field               | Notes |
| ---------------------- | ---------------------- | ------------------- | ----- |
| `+0x00`                | u32                    | skill_key           |       |
| `+0x04`                | u32                    | level_1_key         |       |
| `+0x08`                | u8                     | is_attack_skill     |       |
| `+0x09`                | str8                   | action_name         |       |
| `action_name+0x00`     | u32                    | action_hash         |       |
| `action_name+0x04`     | u8                     | is_prompt_for_learning |    |
| `action_name+0x05`     | u16                    | need_skill_point    |       |
| `action_name+0x07`     | u32                    | need_level          |       |
| `action_name+0x0B`     | u64                    | need_money_for_learning |   |
| `action_name+0x13`     | u32                    | need_item_key_for_learning | |
| `action_name+0x17`     | u64                    | need_item_count_for_learning | |
| `action_name+0x1F`     | u16                    | need_skill_level_1  |       |
| `action_name+0x21`     | u16                    | need_skill_no_1     |       |
| `action_name+0x23`     | u16                    | need_skill_level_2  |       |
| `action_name+0x25`     | u16                    | need_skill_no_2     |       |
| `action_name+0x27`     | u8                     | do_require_point_need |     |
| `action_name+0x28`     | f32                    | require_hp          |       |
| `action_name+0x2C`     | u32                    | resource_cost       |       |
| `action_name+0x30`     | u32                    | require_sub_resource_point | |
| `action_name+0x34`     | u8                     | sub_resource_type   |       |
| `action_name+0x35`     | u32                    | stamina_cost        |       |
| `action_name+0x39`     | u32                    | need_item_key       |       |
| `action_name+0x3D`     | u64                    | need_item_count     |       |
| `action_name+0x45`     | u8                     | is_usable_when_alive |      |
| `action_name+0x46`     | u32                    | global_reuse_cycle  |       |
| `action_name+0x4A`     | u16                    | reuse_group         |       |
| `action_name+0x4C`     | u32                    | cooldown_ms         | Equals Layout 3's value in 22,275 of the 23,635 records both clients share |
| `action_name+0x50`     | u16[10]                | buff_ids            |       |
| `action_name+0x64`     | str16                  | description         |       |
| `description+0x00`     | str16                  | script              |       |
| `script+0x00`          | u8                     | is_usable_while_in_cool_time | |
| `script+0x01`          | u8                     | unknown_s01         |       |
| `script+0x02`          | u8                     | is_expired_in_offline |     |
| `script+0x03`          | u16                    | balance_channel_skill_no | |
| `script+0x05`          | u8                     | is_developing_contents |    |
| `script+0x06`          | u8                     | is_fusion           |       |
| `script+0x07`          | u8                     | enable_in_water     |       |
| `script+0x08`          | u32                    | preview_action_hash |       |
| `script+0x0C`          | f32[3]                 | dummy_monster_distance |    |
| `script+0x18`          | u32                    | black_skill_key     |       |
| `script+0x1C`          | u32                    | adrenalin_point     |       |
| `script+0x20`          | u32                    | link_tooltip_skill_key |    |
| `script+0x24`          | u32                    | next_skill_count    |       |
| `script+0x28`          | u32[next_skill_count]  | next_skill_keys     |       |
| `next_skill_keys+0x00` | u32                    | unknown_after_next_skill_keys |  |
| `next_skill_keys+0x04` | u32                    | related_cool_time_skill_count | |
| `next_skill_keys+0x08` | u32[related_cool_time_skill_count] | related_cool_time_skill_keys | |
| `related_cool_time_skill_keys+0x00` | u32       | special_weapon_hit_effect_count | `0` on every record of client 1784 |
| `related_cool_time_skill_keys+0x04` | u32[special_weapon_hit_effect_count] | special_weapon_hit_effects | The `SpecialWeaponHitEffect` column, empty on every sheet row |
| `special_weapon_hit_effects+0x00` | f32         | target_search_angle |       |
| `special_weapon_hit_effects+0x04` | u8          | is_except_cool_time | Equals Layout 3's value in 23,634 of the 23,635 shared records |

## Skill Keys

Every table in the skill cluster keys a skill rank by a u32:

```text
skill_key = skill_no << 16 | level
```

30,424 keys on client 3458, over 30,342 skill numbers. Almost every key is
level `1` (30,342); 54 are level `2`, 18 level `3`, and a handful go up to
`13`. Rank chains such as "Grave Digging I" to "IV" use separate skill numbers,
not levels, and [`skillgroup.bss`](skillgroup_bss.md) lists them.

The first key in the index, `0xDEAD0001`, is skill `57005` level 1,
"[Event] Energy of Happiness". It looks like a sentinel but is an ordinary
skill; `0xDEAC0001` next to it is skill `57004`, "Grim Reaper's Fury".

## `buff_ids`

Ten u32 slots. The IDs fill the front and the rest are `0`; no record has a
non-zero ID after a zero. On client 3464, 20,418 records name one buff, 507
fill all ten, and 96 name none. Every ID is a `buff.dbss` key.

Before client 3464 the slots were u16, so the block was 20 bytes shorter and
`description` started at `N+102`. The widening came with the first buff IDs
above 65,535 (see the `buff.dbss` Notes); skills 44974 to 44978 (level 1)
apply those five buffs. The parser reads only the u32 layout.

This is the item to buff link: `itemenchant.dbss` `skill_key_1` and
`skill_key_2` are keys of this table, and the buffs of both skills are the
item's effects. Item 761880 casts skill 47683, which applies the six buffs
48723 to 48728. The browser builds the `SKILL_BUFFS` and `BUFF_ITEMS` lookup
indexes from it (see "Lookup Indexes" in docs/handler.md): the
`itemenchant.dbss` Buffs column and the `buff.dbss` Applied By column read
them.

## `resource_cost` and `stamina_cost`

`resource_cost` is the class's own resource, so the tooltip names it by
class: MP on Wizard, WP on Mystic. Checked in game (2026-10-01): "Fireball IV"
shows "Required MP : 30" and "Lightning V" 60, the Mystic's "Thunder Pound
IV" costs 50 WP, and "Teleport III" shows "Required Stamina : 200", each as
stored. bdocodex lists 100 MP for "Grave Digging III" (stored `100`) and no
cost for "Imminent Doom" (`0`). The skill tooltip Lua reads them as
`_requireMp` and `_requireSp`. 18 records set both.

2,825 records store a stamina cost of `1`, mostly basic attacks and weapon
training ranks ("Staff Attack I" to "X", "Magic Arrow I" to "V"); whether the
tooltip shows that is not checked.

## `next_skill_keys` and `related_cool_time_skill_keys`

Every key in both lists is a `skill.dbss` key (7,877 and 155 entries on
client 3458).

`next_skill_keys` points forward along a skill line: "Ample Storage Lv. 26"
lists Lv. 27, "Soul Shower III" lists its next rank and "Core: Soul Shower".
Awakening, Succession and a few other hub skills list every skill they
unlock: most "Succession:" skills list 34 Prime skills, and "Succession:
Elemental Revelation" (4933) lists 75.
Of the 3,858 consecutive rank pairs in `skillgroup.bss`, 3,422 appear here as
rank `i` listing rank `i + 1`.

`related_cool_time_skill_keys` is set only on the 155 "Core:" skills
(client 3458) and names the skill the Core enhances ("Core: Soul Shower" ->
"Soul Shower III"). In 154 of the 155 cases that base skill lists the Core in
its `next_skill_keys`. The handler's Base Skill column shows it. The sheet
column it comes from, `RelatedCoolTimeSkillNo`, links the cooldowns of two
skills; what that does for a Core in game is not checked.

## Notes

- `cooldown_ms` is checked on the wiki (2026-09-28) on three skill lines:
  Warrior's Grave Digging I to IV show 8 s (8,000 stored), Imminent Doom (1209)
  18 s (18,000) and Succession: Imminent Doom (4859) 14 s (14,000), and in
  game (2026-10-01) on Wizard: Fireball IV 3 s, Lightning V 5 s and Teleport
  III 7 s. 7,547 of the 7,626 non-zero values are whole
  seconds; the other 79 are mostly Black Spirit variants at 90% of a round
  value (13,500, 8,100). The field name and its position `@95` come from
  bdo-data-extractor, which reads it at a fixed offset. That only holds when
  `action_name` is empty: skill 17569 has the 22-character name
  `SHADOW_SKILL_SLOT4_2LV`, and its cooldown (9,000) sits 22 bytes later.
- `description` holds real text on 7,983 records (client 3458); 43 more
  store the literal `<null>`. Class skills leave it empty, so their LOC
  type `10` `str_id4 = 1` text has no Korean copy here.
- It is the Korean source of LOC type `13`, keyed `str_id1 = skill_no`,
  `str_id2 = level`: 28,537 of the 28,869 type 13 keys are `skill.dbss`
  ranks, and the numbers in the two texts agree on 7,955 of 7,959 pairs.
  Type 13 stores `0` where `description` is `UNKNOWN` (set effect skills).
- On 7,324 records it is also the source of LOC type `10` `str_id4 = 1`,
  the same text: utility skills whose buffs have no description, such as
  knowledge entries ("Adds acquired knowledge to the book.", 5,651),
  exploration nodes (1,028), workers (540), trade stock refreshes (66) and
  contribution points (39).
- 657 are guild skills (skill numbers 62000 to 65999). Their type 10
  `str_id4 = 1` is missing (614) or a usage hint such as
  `{TextBind:CASTING_CLICK_RMB} after learning the skill` (Healing Touch,
  65209; the browser fills it as `Cast with [Attack2] after learning the
  skill`), while type 13 holds the effect (`- Effect: Recover 200 HP every
  3 sec (only during Node/Conquest War)`). The Description column shows
  both, the hint first; which order the game tooltip uses is not checked.
  The effect text is close to the Korean `buff.dbss` description of the
  skill's buffs but never equal to it: 375 contain every buff text and add
  a line ("does not stack with the previous rank"), the rest add the
  war-only condition, the duration and the caster, or reword it. So the
  buff text cannot stand in for it; the Buffs column shows the buffs.
- Five guild skill ranks (Monster Extra AP, 65077 to 65081) have Korean
  text only, so their Description stays Korean.
- The skill tooltip Lua (`panel_tooltip_skill.luac`) calls `getDescription`
  on both the skill type and the rank's static data, matching the two
  texts.
- `action_hash` is not the `stringtable.bss` key hash; the hash function
  is unknown. The server computes it from `ActionName` when it loads the
  sheet (see Field Names).
- `skillsimply.dbss` has exactly the same 30,424 keys and holds the learning
  rules (class, level, skill points, prerequisites), see
  [`skillsimply.dbss`](skillsimply_dbss.md).

## Field Names

The record is one row of the `Skill_Table_New` sheet of a private server on
client 1784. I matched every record field against every column by value,
twice: that server's own `skill.dbss` against the sheet in the
`datasheet_skilldatatable_*.xlsm` workbooks it was compiled from (27,563
sheet rows of ranks the file has), and client 3474's file against the sheet
in the server's `DataSheets.bexcel` (22,876 shared ranks).

The server dump (`Instance_dumpFull.exe`) names the fields whose values do
not vary. It holds both readers of the row, and both write the same static
status (0x2C0 bytes):

- The sheet loader (VA `0x14085dd80`) reads each column into one member.
- The file reader (VA `0x140c8ed50`) reads the record fields in file order
  into the members. Layout 1 is exactly the order it reads.
- `SkillStaticStatus::set()` (VA `0x140c8a6b0`, named by its own error
  messages) and the reset before each row (VA `0x140c8a2c0`) fill the
  members no column sets.

The 2016 member is the one of the 2016 client's `gc::SkillStaticStatus` at
the same place in the member order.

| Field | Column | Member | 2016 member | Equal, client 1784 | Equal, client 3474 |
| ----- | ------ | ------ | ----------- | ------------------ | ------------------ |
| `level_1_key` | | `+0x48` | | | |
| `is_attack_skill` | | `+0x58` | `_isAttackSkill` | | |
| `action_name` | `ActionName` | `+0x60` | `_actionName` | 27,543 | 22,624 |
| `action_hash` | `ActionName`, hashed | `+0x90` | `_actionHashKey` | | |
| `is_prompt_for_learning` | `IsPrompt_ForLearning` | `+0x184` | `_isPromptForLearning` | 27,563 | 22,857 |
| `need_skill_point` | `SkillPoint_ForLearning` | `+0xA0` | `_needSkillPointForLearning` | 27,278 | 19,409 |
| `need_level` | `PcLevel_ForLearning` | `+0xA4` | `_needCharacterLevelForLearning` | 27,527 | 22,049 |
| `need_money_for_learning` | `NeedMoney_ForLearning` | `+0xA8` | `_needMoneyForLearning` | 27,563 | 22,876 |
| `need_item_key_for_learning` | `NeedItemID_ForLearning` | `+0xB0` | `_needItemKeyForLearning` | 27,555 | 22,868 |
| `need_item_count_for_learning` | `NeedItemCount_ForLearning` | `+0xB8` | `_needItemCountForLearning` | 27,557 | 22,870 |
| `need_skill_level_1`, `need_skill_no_1` | `NeedSkillLevelNo0_ForLearning`, `NeedSkillNo0_ForLearning` | `+0xC0` | `_needPreSkillKeyForLearning` | 27,559, 27,557 | 22,399, 22,695 |
| `need_skill_level_2`, `need_skill_no_2` | `NeedSkillLevelNo1_ForLearning`, `NeedSkillNo1_ForLearning` | `+0xC4` | `_needPreSkillKeyForLearning` | 27,529, 27,558 | 22,646, 22,795 |
| `do_require_point_need` | | `+0xE0` | `_doRequirePointNeed` | | |
| `require_hp` | `RequireHP` | `+0xE4` | `_requireHp` | 27,563 | 22,876 |
| `resource_cost` | `RequireMP` | `+0xE8` | `_requireMp` | 27,550 | 22,697 |
| `require_sub_resource_point` | `RequireSubResourcePoint` | `+0xEC` | `_requireSubResourcePoint` | 27,563 | 22,875 |
| `sub_resource_type` | `SubResourceType` | `+0xF0` | | 27,563 | 22,876 |
| `stamina_cost` | `RequireSP` | `+0xF4` | `_requireSp` | 27,543 | 22,374 |
| `need_item_key` | `NeedItemID` | `+0xF8` | `_needItemKey` | 27,563 | 22,843 |
| `need_item_count` | `NeedItemCount` | `+0x100` | `_needItemCount` | 27,563 | 22,843 |
| `is_usable_when_alive` | | `+0x108` | `_isUsableWhenAlive` | | |
| `global_reuse_cycle` | `IsGlobalCycle` | `+0x10C` | `_globalReuseCycle` | 27,563 | 22,876 |
| `reuse_group` | `ReuseGroup` | `+0x110` | `_reuseCycleGroup` | 27,563 | 22,516 |
| `cooldown_ms` | `ReuseCycle` | `+0x114` | `_reuseCycle` | 27,547 | 21,520 |
| `buff_ids` | `Buff0` to `Buff9` | `+0x118` | `_buffKey` | 27,468 | 17,756 |
| `description` | `Desc` | `+0x138` | `_description` | 26,693 | 20,737 |
| `script` | `PatternDesc` | `+0x158` | | 26,811 | 16,693 |
| `is_usable_while_in_cool_time` | `UsableInCoolTime` | `+0x183` | `_isUsableWhileInCoolTime` | 27,563 | 22,796 |
| `unknown_s01` | | `+0x17E` | | | |
| `is_expired_in_offline` | `isExpiredInOffline` | `+0x17F` | | 27,563 | 22,875 |
| `balance_channel_skill_no` | `BalanceChannelSkillNo` | `+0x17C` | | 27,559 | 22,876 |
| `is_developing_contents` | `IsDevelopingContents` | `+0x180` | | 27,563 | 22,508 |
| `is_fusion` | `IsFusion` | `+0x181` | | 27,551 | 22,876 |
| `enable_in_water` | `EnableInWater` | `+0x182` | | 27,563 | 22,876 |
| `preview_action_hash` | `PreviewActionName`, hashed | `+0x80` | | | |
| `dummy_monster_distance` | `DummyMonsterDistance` | `+0x84` | | 27,558 | 22,763 |
| `black_skill_key` | `BlackSkillNo`, as a level 1 key | `+0x94` | | 27,563 | 22,774 |
| `adrenalin_point` | `AdrenalinPoint` | `+0x98` | | 27,563 | 22,769 |
| `link_tooltip_skill_key` | `LinkToolTipSkillNo`, as a level 1 key | `+0x9C` | | 27,563 | 22,837 |
| `next_skill_keys` | | `+0xC8` | `_postSkillsAfterLearning` | | |
| `unknown_after_next_skill_keys` | | `+0x2B0` | | | |
| `related_cool_time_skill_keys` | `RelatedCoolTimeSkillNo`, as level 1 keys | `+0x188` | | 27,551 | 22,871 |
| `special_weapon_hit_effects` (Layout 1) | `SpecialWeaponHitEffect` | `+0x1A0` | | 27,563 | |
| `target_search_angle` | `TargetSearchAngle` | `+0x1B8` | | 27,563 | 22,862 |
| `is_except_cool_time` | `ExceptCoolTime` | `+0x185` | | 27,563 | 22,875 |

Most columns are `0` or empty on nearly every row, so the equal counts
alone say little for them; the member chain names them. The client 3474
counts are lower where the private server edited balance values (skill
points, costs, cooldowns, buffs) or the live client added text. The fields
that were `name`, `name_hash` and `base_skill_keys` in earlier versions of
this doc take the column names `action_name`, `action_hash` and
`related_cool_time_skill_keys`, and `unknown_f32` is `target_search_angle`.
`resource_cost` and `stamina_cost` are u32, as the server reads them; their
values fit the u16 the doc gave them before.

- `level_1_key` is no column: `set()` looks up the skill type of
  `skill_no << 16 | 1` and stores its key and a pointer to it (the 2016
  `_skillType`).
- `is_attack_skill` has no column either, and neither the loader nor
  `set()` writes it. Its name rests on the member order: in both structs it
  is the bool after the skill type and Awakening pointers and right before
  the action name. The 2016 `_dontUse` sits right after `_key` instead. On
  client 3474 it is `1` on 8,738 records, and on Wizard it follows the
  damage line of the tooltip on 7 of 8 skills checked in game, see the
  `skillsimply.dbss` Notes.
- `do_require_point_need` is set by `set()` when `require_hp`,
  `resource_cost` or `require_sub_resource_point` is not `0`, and holds
  exactly that on all 30,487 records of client 3474 (`1` on 3,582).
- `is_usable_when_alive` is `1` after the reset and no column changes it.
  On client 3474 it is `0` on 13 records: the item skills "Necklace of
  Resurrection" (Lv. 1 and 2), "Mount Consumable: Revive Mount", "[Savage]
  Medical Kit Resurrection", "Special Revival Potion", and the eight skills
  15280 to 15287 (such as "Strategic Revival" and "Summon Ogre").
- `require_hp` is set on one record of client 3474, "Beast Form" (1031),
  at `250.0`. The skill tooltip Lua reads it as `_requireHp` next to
  `_requireMp` and `_requireSp`.
- `sub_resource_type` is `2` on 19 guild skills (65201 to 65227) and `1` on
  five Matchlock skills (15339 to 15472) on client 3474;
  `require_sub_resource_point` is `1` on five class skills, such as
  "Augmentation" and "Dragon's Calling". What the two resources are is not
  named in the sources.
- `global_reuse_cycle`: the loader stores `1000` when `IsGlobalCycle` is
  set, else `0`. No row sets it.
- `is_expired_in_offline` is `1` on 24 records of client 3474, such as
  "Returnstone", "Compass", "Telescope" and "Reset Barter".
- `enable_in_water` is `1` on 15 records of client 3474, all HP potions
  ("HP Recovery Potion (Small)" to "(Huge)", "[Hardcore] HP Potion").
- `is_developing_contents` is `1` on 1,233 records of client 3474. The
  loader reads it before every other column of the row.
- `preview_action_hash` is set on 6,948 records of client 3474, with 1,611
  values. The loader hashes `PreviewActionName` with a different routine
  from `ActionName` (VA `0x1405aebd0`, the action name uses `0x1405ae640`),
  and no preview name is also an action name, so I could not check the two
  hashes against each other.
- `dummy_monster_distance` is the column's three comma-separated numbers
  as floats. On client 3474 the third is set on 8,326 records, most often
  `200.0` (3,337; `900.0` on "Soul Shower III"), the first on 39 and the
  second on none.
- `black_skill_key` and `link_tooltip_skill_key` are the level 1 keys of the
  `BlackSkillNo` and `LinkToolTipSkillNo` skill numbers. All 677 and 107 on
  client 3474 are `skill.dbss` keys: "Sahee's Descent III" names "Black
  Spirit: Sahee's Descent III", and "Flow: Brimbolt Wave" names
  "Succession: Flow: Brimbolt Wave". The skill tooltip Lua reads them with
  `getlinkBlackSkillNo` and `getLinkTooltipSkillNo`.
- `adrenalin_point` is set on 682 records of client 3474, mostly `10000`
  and `20000`.
- `related_cool_time_skill_keys`: the loader splits the column at commas
  and stores each skill number as a level 1 key. Of the 132 shared ranks
  where the bexcel or client 3474 has a list, 127 hold the same keys. The
  1784 file has no Core skills and stores no list; the 12 `.xlsm` rows with
  a value are in `datasheet_skilldatatable_pc_ninja22.xlsm`, a workbook the
  server's sheet load list (`loaddatafilelist.txt`) does not name.
- `target_search_angle`: the loader reads the column as an integer and
  stores it as a float when the cell is set; the reset sets `-1.0`. On the
  1784 file it is `0.0` on exactly the 605 rows whose cell is `0` and
  `-1.0` on the rest.
- The file does not hold `ContentsGroupKey` (see `skillsimply.dbss`),
  `DoCheckHit`, `VariedHit`, `ApplyNumber`, `BuffApplyRate`, `StunValue`,
  the attack dice columns (`DDD` to `HMPV`) or `DoNotTranslate`: the loader
  writes their members and the file reader does not.

## Open Questions

### What do `unknown_s01` and `unknown_end` hold?

`unknown_s01` sits in server member `+0x17E`, which only the reset writes
(`0`). On client 3474 it is `1` on 178 records, the "[Party]" elixirs and
event buffs such as "[Event] Energy of Happiness"; on the 1784 file it is
`0` everywhere. `unknown_end` came after client 1784: its first byte is `1`
on 18 records of client 3474, the "Blessing of Taebaek" and "Asadal" ranks
(10189 to 10217), and its second byte is always `0`. `unknown_n4c` (always
`0`) and `unknown_after_next_skill_keys` (member `+0x2B0`, always `0`) have
no column either.
