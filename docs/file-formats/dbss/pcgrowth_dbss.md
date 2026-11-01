# `pcgrowth.dbss` Format

## Purpose

The class selection record of every class type: the player character key of the class, its gender, its combat type (melee, ranged or magic), the beginner weapons of the class, the main, sub and awakening weapon of the class, the Korean name and description, and the class selection video. Despite the name, the file holds no per-level stat growth; nothing in it is indexed by character level. `pcgrowthoffset.dbss` lists where each record sits, [pcgrowthsimply](../bss/pcgrowthsimply_bss.md) is a fixed-row list of the same class types with a playable flag, and [pcgrowthdefaultcharacterkey](../bss/pcgrowthdefaultcharacterkey_bss.md) stores one character key.

The class type is the number `getClassType()` returns and the bit of a class mask (`_common/class_type.py`); the character key is the player prototype in `characterstatic.dbss` and LOC type 6. They differ for most classes: Ranger is class type 4 and character 2, Sorceress class type 8 and character 3.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes  | Records                                                                                            | Row bytes               |
| ------ | -------------- | --------------------- | ------ | -------------------------------------------------------------------------------------------------- | ----------------------- |
| 2      | 3314 and later | `pcgrowth.dbss`       | 55,280 | 47 Setup Block, 47 Presentation Block, 250 Model Entry, 94 Model List, 47 Class Record, 47 Record  | 53 to 71, 58 on average |
| 2      | 3314 and later | `pcgrowthoffset.dbss` | 427    | 47 Offset Row                                                                                      | 9                       |
| 1      | 1759 to 1862   | `pcgrowth.dbss`       | 63,228 | 82 Setup Block, 82 Presentation Block, 164 Model List, 82 Class Record, 82 Record, 144 Model Entry | 4 to 196, 55 on average |
| 1      | 1759 to 1862   | `pcgrowthoffset.dbss` | 742    | 82 Offset Row                                                                                      | 9                       |

| Layout | File                  | Known            | Unknown        |
| ------ | --------------------- | ---------------- | -------------- |
| 2      | `pcgrowth.dbss`       | 52,178 B (94.4%) | 3,102 B (5.6%) |
| 2      | `pcgrowthoffset.dbss` | 427 B (100.0%)   | 0 B (0.0%)     |
| 1      | `pcgrowth.dbss`       | 61,424 B (97.1%) | 1,804 B (2.9%) |
| 1      | `pcgrowthoffset.dbss` | 742 B (100.0%)   | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `ed6888f41e4f`  |
| 3482   | Layout 2             | `ed6888f41e4f`  |
| 3474   | Layout 2             | `ed6888f41e4f`  |
| 3473   | Layout 2             | `ed6888f41e4f`  |
| 3464   | Layout 2             | `ed6888f41e4f`  |
| 3458   | Layout 2             | `ed6888f41e4f`  |
| 3454   | Layout 2             | `ed6888f41e4f`  |
| 3444   | Layout 2             | `ed6888f41e4f`  |
| 3435   | Layout 2             | `ed6888f41e4f`  |
| 3426   | Layout 2             | `ed6888f41e4f`  |
| 3418   | Layout 2             | `ed6888f41e4f`  |
| 3412   | Layout 2             | `ed6888f41e4f`  |
| 3402   | Layout 2             | `ed6888f41e4f`  |
| 3396   | Layout 2             | `ed6888f41e4f`  |
| 3387   | Layout 2             | `ed6888f41e4f`  |
| 3381   | Layout 2             | `ed6888f41e4f`  |
| 3373   | Layout 2             | `ed6888f41e4f`  |
| 3364   | Layout 2             | `ed6888f41e4f`  |
| 3356   | Layout 2             | `ed6888f41e4f`  |
| 3349   | Layout 2             | `ed6888f41e4f`  |
| 3342   | Layout 2             | `ed6888f41e4f`  |
| 3335   | Layout 2             | `ed6888f41e4f`  |
| 3326   | Layout 2             | `ed6888f41e4f`  |
| 3321   | Layout 2             | `ed6888f41e4f`  |
| 3314   | Layout 2             | `ed6888f41e4f`  |
| 3303   | No documented layout | `ed6888f41e4f`  |
| 3302   | No documented layout | `ed6888f41e4f`  |
| 3293   | No documented layout | `ed6888f41e4f`  |
| 3283   | No documented layout | `ed6888f41e4f`  |
| 3275   | No documented layout | `ed6888f41e4f`  |
| 3267   | No documented layout | `ed6888f41e4f`  |
| 3258   | No documented layout | `ed6888f41e4f`  |
| 3251   | No documented layout | `ed6888f41e4f`  |
| 3242   | No documented layout | `ed6888f41e4f`  |
| 3235   | No documented layout | `ed6888f41e4f`  |
| 3229   | No documented layout | `ed6888f41e4f`  |
| 3212   | No documented layout | `ed6888f41e4f`  |
| 3203   | No documented layout | `ed6888f41e4f`  |
| 3193   | No documented layout | `ed6888f41e4f`  |
| 3186   | No documented layout | `ed6888f41e4f`  |
| 3177   | No documented layout | `ed6888f41e4f`  |
| 3169   | No documented layout | `ed6888f41e4f`  |
| 3158   | No documented layout | `ed6888f41e4f`  |
| 3151   | No documented layout | `ed6888f41e4f`  |
| 3144   | No documented layout | `ed6888f41e4f`  |
| 3133   | No documented layout | `ed6888f41e4f`  |
| 3125   | No documented layout | `ed6888f41e4f`  |
| 3118   | No documented layout | `ed6888f41e4f`  |
| 3111   | No documented layout | `ed6888f41e4f`  |
| 3103   | No documented layout | `ed6888f41e4f`  |
| 3095   | No documented layout | `ed6888f41e4f`  |
| 3086   | No documented layout | `ed6888f41e4f`  |
| 3072   | No documented layout | `ed6888f41e4f`  |
| 3062   | No documented layout | `ed6888f41e4f`  |
| 3052   | No documented layout | `ed6888f41e4f`  |
| 3045   | No documented layout | `ed6888f41e4f`  |
| 3037   | No documented layout | `ed6888f41e4f`  |
| 3030   | No documented layout | `ed6888f41e4f`  |
| 3021   | No documented layout | `ed6888f41e4f`  |
| 3012   | No documented layout | `ed6888f41e4f`  |
| 3002   | No documented layout | `ed6888f41e4f`  |
| 2995   | No documented layout | `ed6888f41e4f`  |
| 2987   | No documented layout | `ed6888f41e4f`  |
| 2978   | No documented layout | `ed6888f41e4f`  |
| 2970   | No documented layout | `ed6888f41e4f`  |
| 2959   | No documented layout | `ed6888f41e4f`  |
| 2951   | No documented layout | `ed6888f41e4f`  |
| 2942   | No documented layout | `ed6888f41e4f`  |
| 2935   | No documented layout | `ed6888f41e4f`  |
| 2932   | No documented layout | `ed6888f41e4f`  |
| 2923   | No documented layout | `ed6888f41e4f`  |
| 2919   | No documented layout | `ed6888f41e4f`  |
| 2907   | No documented layout | `ed6888f41e4f`  |
| 2900   | No documented layout | `ed6888f41e4f`  |
| 2891   | No documented layout | `ed6888f41e4f`  |
| 2882   | No documented layout | `ed6888f41e4f`  |
| 2872   | No documented layout | `ed6888f41e4f`  |
| 2863   | No documented layout | `ed6888f41e4f`  |
| 2855   | No documented layout | `ed6888f41e4f`  |
| 2849   | No documented layout | `ed6888f41e4f`  |
| 2844   | No documented layout | `ed6888f41e4f`  |
| 2834   | No documented layout | `ed6888f41e4f`  |
| 2825   | No documented layout | `ed6888f41e4f`  |
| 2819   | No documented layout | `ed6888f41e4f`  |
| 2811   | No documented layout | `ed6888f41e4f`  |
| 2803   | No documented layout | `ed6888f41e4f`  |
| 2794   | No documented layout | `ed6888f41e4f`  |
| 2783   | No documented layout | `ed6888f41e4f`  |
| 2774   | No documented layout | `ed6888f41e4f`  |
| 2765   | No documented layout | `ed6888f41e4f`  |
| 2756   | No documented layout | `ed6888f41e4f`  |
| 2750   | No documented layout | `ed6888f41e4f`  |
| 2743   | No documented layout | `ed6888f41e4f`  |
| 2736   | No documented layout | `ed6888f41e4f`  |
| 2726   | No documented layout | `ed6888f41e4f`  |
| 2717   | No documented layout | `ed6888f41e4f`  |
| 2709   | No documented layout | `ed6888f41e4f`  |
| 2703   | No documented layout | `ed6888f41e4f`  |
| 2695   | No documented layout | `ed6888f41e4f`  |
| 2684   | No documented layout | `ed6888f41e4f`  |
| 2672   | No documented layout | `ed6888f41e4f`  |
| 2665   | No documented layout | `ed6888f41e4f`  |
| 2657   | No documented layout | `ed6888f41e4f`  |
| 2649   | No documented layout | `ed6888f41e4f`  |
| 2644   | No documented layout | `ed6888f41e4f`  |
| 2637   | No documented layout | `ed6888f41e4f`  |
| 2629   | No documented layout | `ed6888f41e4f`  |
| 2619   | No documented layout | `ed6888f41e4f`  |
| 2612   | No documented layout | `ed6888f41e4f`  |
| 2606   | No documented layout | `ed6888f41e4f`  |
| 2602   | No documented layout | `ed6888f41e4f`  |
| 2601   | No documented layout | `ed6888f41e4f`  |
| 2592   | No documented layout | `ed6888f41e4f`  |
| 2583   | No documented layout | `ed6888f41e4f`  |
| 2575   | No documented layout | `ed6888f41e4f`  |
| 2567   | No documented layout | `ed6888f41e4f`  |
| 2560   | No documented layout | `ed6888f41e4f`  |
| 2553   | No documented layout | `ed6888f41e4f`  |
| 2545   | No documented layout | `ed6888f41e4f`  |
| 2538   | No documented layout | `ed6888f41e4f`  |
| 2529   | No documented layout | `ed6888f41e4f`  |
| 2519   | No documented layout | `ed6888f41e4f`  |
| 2513   | No documented layout | `ed6888f41e4f`  |
| 2510   | No documented layout | `ed6888f41e4f`  |
| 2507   | No documented layout | `ed6888f41e4f`  |
| 2503   | No documented layout | `ed6888f41e4f`  |
| 2498   | No documented layout | `ed6888f41e4f`  |
| 2492   | No documented layout | `ed6888f41e4f`  |
| 2487   | No documented layout | `ed6888f41e4f`  |
| 2480   | No documented layout | `ed6888f41e4f`  |
| 2474   | No documented layout | `ed6888f41e4f`  |
| 2468   | No documented layout | `ed6888f41e4f`  |
| 2460   | No documented layout | `ed6888f41e4f`  |
| 2453   | No documented layout | `ed6888f41e4f`  |
| 2444   | No documented layout | `ed6888f41e4f`  |
| 2438   | No documented layout | `ed6888f41e4f`  |
| 2434   | No documented layout | `ed6888f41e4f`  |
| 2429   | No documented layout | `ed6888f41e4f`  |
| 2421   | No documented layout | `ed6888f41e4f`  |
| 2414   | No documented layout | `ed6888f41e4f`  |
| 2407   | No documented layout | `ed6888f41e4f`  |
| 2401   | No documented layout | `ed6888f41e4f`  |
| 2397   | No documented layout | `ed6888f41e4f`  |
| 2393   | No documented layout | `ed6888f41e4f`  |
| 2384   | No documented layout | `ed6888f41e4f`  |
| 2378   | No documented layout | `ed6888f41e4f`  |
| 2372   | No documented layout | `ed6888f41e4f`  |
| 2358   | No documented layout | `ed6888f41e4f`  |
| 2352   | No documented layout | `ed6888f41e4f`  |
| 2347   | No documented layout | `ed6888f41e4f`  |
| 2343   | No documented layout | `ed6888f41e4f`  |
| 2335   | No documented layout | `ed6888f41e4f`  |
| 2327   | No documented layout | `ed6888f41e4f`  |
| 2324   | No documented layout | `ed6888f41e4f`  |
| 2319   | No documented layout | `ed6888f41e4f`  |
| 2313   | No documented layout | `ed6888f41e4f`  |
| 2308   | No documented layout | `ed6888f41e4f`  |
| 2302   | No documented layout | `ed6888f41e4f`  |
| 2295   | No documented layout | `ed6888f41e4f`  |
| 2290   | No documented layout | `ed6888f41e4f`  |
| 2284   | No documented layout | `ed6888f41e4f`  |
| 2276   | No documented layout | `ed6888f41e4f`  |
| 2269   | No documented layout | `ed6888f41e4f`  |
| 2259   | No documented layout | `ed6888f41e4f`  |
| 2250   | No documented layout | `ed6888f41e4f`  |
| 2243   | No documented layout | `ed6888f41e4f`  |
| 2235   | No documented layout | `ed6888f41e4f`  |
| 2229   | No documented layout | `ed6888f41e4f`  |
| 2224   | No documented layout | `ed6888f41e4f`  |
| 2218   | No documented layout | `ed6888f41e4f`  |
| 2215   | No documented layout | `ed6888f41e4f`  |
| 2207   | No documented layout | `ed6888f41e4f`  |
| 2203   | No documented layout | `ed6888f41e4f`  |
| 2196   | No documented layout | `ed6888f41e4f`  |
| 2192   | No documented layout | `ed6888f41e4f`  |
| 2189   | No documented layout | `ed6888f41e4f`  |
| 2183   | No documented layout | `ed6888f41e4f`  |
| 2179   | No documented layout | `ed6888f41e4f`  |
| 2171   | No documented layout | `ed6888f41e4f`  |
| 2163   | No documented layout | `ed6888f41e4f`  |
| 2156   | No documented layout | `ed6888f41e4f`  |
| 2151   | No documented layout | `ed6888f41e4f`  |
| 2147   | No documented layout | `ed6888f41e4f`  |
| 2142   | No documented layout | `ed6888f41e4f`  |
| 2138   | No documented layout | `ed6888f41e4f`  |
| 2134   | No documented layout | `ed6888f41e4f`  |
| 2130   | No documented layout | `ed6888f41e4f`  |
| 2122   | No documented layout | `ed6888f41e4f`  |
| 2107   | No documented layout | `ed6888f41e4f`  |
| 2098   | No documented layout | `ed6888f41e4f`  |
| 2089   | No documented layout | `ed6888f41e4f`  |
| 2081   | No documented layout | `ed6888f41e4f`  |
| 2073   | No documented layout | `ed6888f41e4f`  |
| 2067   | No documented layout | `ed6888f41e4f`  |
| 2063   | No documented layout | `ed6888f41e4f`  |
| 2059   | No documented layout | `ed6888f41e4f`  |
| 2052   | No documented layout | `ed6888f41e4f`  |
| 2044   | No documented layout | `ed6888f41e4f`  |
| 2039   | No documented layout | `ed6888f41e4f`  |
| 2032   | No documented layout | `ed6888f41e4f`  |
| 2025   | No documented layout | `ed6888f41e4f`  |
| 2011   | No documented layout | `ed6888f41e4f`  |
| 2005   | No documented layout | `ed6888f41e4f`  |
| 2000   | No documented layout | `ed6888f41e4f`  |
| 1996   | No documented layout | `ed6888f41e4f`  |
| 1991   | No documented layout | `ed6888f41e4f`  |
| 1985   | No documented layout | `ed6888f41e4f`  |
| 1980   | No documented layout | `ed6888f41e4f`  |
| 1969   | No documented layout | `ed6888f41e4f`  |
| 1964   | No documented layout | `ed6888f41e4f`  |
| 1958   | No documented layout | `ed6888f41e4f`  |
| 1950   | No documented layout | `ed6888f41e4f`  |
| 1945   | No documented layout | `ed6888f41e4f`  |
| 1937   | No documented layout | `ed6888f41e4f`  |
| 1933   | No documented layout | `ed6888f41e4f`  |
| 1927   | No documented layout | `ed6888f41e4f`  |
| 1921   | No documented layout | `ed6888f41e4f`  |
| 1914   | No documented layout | `ed6888f41e4f`  |
| 1908   | No documented layout | `ed6888f41e4f`  |
| 1897   | No documented layout | `ed6888f41e4f`  |
| 1892   | No documented layout | `ed6888f41e4f`  |
| 1886   | No documented layout | `ed6888f41e4f`  |
| 1881   | No documented layout | `ed6888f41e4f`  |
| 1871   | No documented layout | `ed6888f41e4f`  |
| 1866   | No documented layout | `ed6888f41e4f`  |
| 1862   | Layout 1             | `ed6888f41e4f`  |
| 1854   | Layout 1             | `ed6888f41e4f`  |
| 1846   | Layout 1             | `ed6888f41e4f`  |
| 1838   | Layout 1             | `ed6888f41e4f`  |
| 1832   | Layout 1             | `ed6888f41e4f`  |
| 1826   | Layout 1             | `ed6888f41e4f`  |
| 1822   | Layout 1             | `ed6888f41e4f`  |
| 1818   | Layout 1             | `ed6888f41e4f`  |
| 1804   | Layout 1             | `ed6888f41e4f`  |
| 1794   | Layout 1             | `ed6888f41e4f`  |
| 1790   | Layout 1             | `ed6888f41e4f`  |
| 1784   | Layout 1             | `ed6888f41e4f`  |
| 1774   | Layout 1             | `ed6888f41e4f`  |
| 1771   | Layout 1             | `ed6888f41e4f`  |
| 1762   | Layout 1             | `ed6888f41e4f`  |
| 1759   | Layout 1             | `ed6888f41e4f`  |
| 1754   | No documented layout | `ed6888f41e4f`  |
| 1749   | No documented layout | `ed6888f41e4f`  |
| 1743   | No documented layout | `ed6888f41e4f`  |
| 1737   | No documented layout | `ed6888f41e4f`  |
| 1731   | No documented layout | `ed6888f41e4f`  |
| 1725   | No documented layout | `ed6888f41e4f`  |
| 1717   | No documented layout | `ed6888f41e4f`  |
| 1710   | No documented layout | `ed6888f41e4f`  |
| 1704   | No documented layout | `ed6888f41e4f`  |
| 1698   | No documented layout | `ed6888f41e4f`  |
| 1690   | No documented layout | `ed6888f41e4f`  |
| 1685   | No documented layout | `ed6888f41e4f`  |
| 1680   | No documented layout | `ed6888f41e4f`  |
| 1674   | No documented layout | `ed6888f41e4f`  |
| 1668   | No documented layout | `ed6888f41e4f`  |
| 1659   | No documented layout | `ed6888f41e4f`  |
| 1649   | No documented layout | `ed6888f41e4f`  |
| 1642   | No documented layout | `ed6888f41e4f`  |
| 1636   | No documented layout | `ed6888f41e4f`  |
| 1628   | No documented layout | `ed6888f41e4f`  |
| 1622   | No documented layout | `ed6888f41e4f`  |
| 1614   | No documented layout | `ed6888f41e4f`  |
| 1608   | No documented layout | `ed6888f41e4f`  |
| 1602   | No documented layout | `ed6888f41e4f`  |
| 1598   | No documented layout | `ed6888f41e4f`  |
| 1594   | No documented layout | `ed6888f41e4f`  |
| 1590   | No documented layout | `ed6888f41e4f`  |
| 1587   | No documented layout | `ed6888f41e4f`  |
| 1584   | No documented layout | `ed6888f41e4f`  |
| 1579   | No documented layout | `ed6888f41e4f`  |
| 1572   | No documented layout | `ed6888f41e4f`  |
| 1565   | No documented layout | `ed6888f41e4f`  |
| 1559   | No documented layout | `ed6888f41e4f`  |
| 1554   | No documented layout | `ed6888f41e4f`  |
| 1547   | No documented layout | `ed6888f41e4f`  |
| 1537   | No documented layout | `ed6888f41e4f`  |
| 1529   | No documented layout | `ed6888f41e4f`  |
| 1524   | No documented layout | `ed6888f41e4f`  |
| 1519   | No documented layout | `ed6888f41e4f`  |
| 1509   | No documented layout | `ed6888f41e4f`  |
| 1506   | No documented layout | `ed6888f41e4f`  |
| 1504   | No documented layout | `ed6888f41e4f`  |
| 1500   | No documented layout | `ed6888f41e4f`  |
| 1493   | No documented layout | `ed6888f41e4f`  |
| 1489   | No documented layout | `ed6888f41e4f`  |
| 1485   | No documented layout | `ed6888f41e4f`  |
| 1481   | No documented layout | `ed6888f41e4f`  |
| 1474   | No documented layout | `ed6888f41e4f`  |
| 1466   | No documented layout | `ed6888f41e4f`  |
| 1462   | No documented layout | `ed6888f41e4f`  |
| 1459   | No documented layout | `ed6888f41e4f`  |
| 1453   | No documented layout | `ed6888f41e4f`  |
| 1450   | No documented layout | `ed6888f41e4f`  |
| 1445   | No documented layout | `ed6888f41e4f`  |
| 1439   | No documented layout | `ed6888f41e4f`  |
| 1433   | No documented layout | `ed6888f41e4f`  |
| 1430   | No documented layout | `ed6888f41e4f`  |
| 1426   | No documented layout | `ed6888f41e4f`  |
| 1421   | No documented layout | `ed6888f41e4f`  |
| 1417   | No documented layout | `ed6888f41e4f`  |
| 1416   | No documented layout | `ed6888f41e4f`  |
| 1409   | No documented layout | `ed6888f41e4f`  |
| 1405   | No documented layout | `ed6888f41e4f`  |
| 1401   | No documented layout | `ed6888f41e4f`  |
| 1396   | No documented layout | `ed6888f41e4f`  |
| 1391   | No documented layout | `ed6888f41e4f`  |
| 1390   | No documented layout | `ed6888f41e4f`  |
| 1386   | No documented layout | `ed6888f41e4f`  |
| 1381   | No documented layout | `ed6888f41e4f`  |
| 1379   | No documented layout | `ed6888f41e4f`  |
| 1372   | No documented layout | `ed6888f41e4f`  |
| 1366   | No documented layout | `ed6888f41e4f`  |
| 1364   | No documented layout | `ed6888f41e4f`  |
| 1363   | No documented layout | `ed6888f41e4f`  |
| 1360   | No documented layout | `ed6888f41e4f`  |
| 1358   | No documented layout | `ed6888f41e4f`  |
| 1355   | No documented layout | `ed6888f41e4f`  |
| 1351   | No documented layout | `ed6888f41e4f`  |
| 1348   | No documented layout | `ed6888f41e4f`  |
| 1346   | No documented layout | `ed6888f41e4f`  |
| 1341   | No documented layout | `ed6888f41e4f`  |
| 1340   | No documented layout | `ed6888f41e4f`  |
| 1338   | No documented layout | `ed6888f41e4f`  |
| 1335   | No documented layout | `ed6888f41e4f`  |
| 1333   | No documented layout | `ed6888f41e4f`  |
| 1329   | No documented layout | `ed6888f41e4f`  |
| 1327   | No documented layout | `ed6888f41e4f`  |
| 1324   | No documented layout | `ed6888f41e4f`  |
| 1321   | No documented layout | `ed6888f41e4f`  |
| 1319   | No documented layout | `ed6888f41e4f`  |
| 1318   | No documented layout | `ed6888f41e4f`  |
| 1316   | No documented layout | `ed6888f41e4f`  |
| 1313   | No documented layout | `ed6888f41e4f`  |
| 1311   | No documented layout | `ed6888f41e4f`  |
| 1309   | No documented layout | `ed6888f41e4f`  |
| 1304   | No documented layout | `ed6888f41e4f`  |
| 1292   | No documented layout | `ed6888f41e4f`  |
| 1286   | No documented layout | `ed6888f41e4f`  |
| 1280   | No documented layout | `ed6888f41e4f`  |
| 1276   | No documented layout | `ed6888f41e4f`  |
| 1267   | No documented layout | `ed6888f41e4f`  |
| 1261   | No documented layout | `ed6888f41e4f`  |
| 1256   | No documented layout | `ed6888f41e4f`  |
| 1250   | No documented layout | `ed6888f41e4f`  |
| 1246   | No file              | `ed6888f41e4f`  |
| 1239   | No file              | `ed6888f41e4f`  |
| 1230   | No file              | `ed6888f41e4f`  |
| 1226   | No file              | `ed6888f41e4f`  |
| 1220   | No file              | `ed6888f41e4f`  |
| 1217   | No file              | `ed6888f41e4f`  |
| 1211   | No file              | `ed6888f41e4f`  |
| 1210   | No file              | `ed6888f41e4f`  |
| 1208   | No file              | `ed6888f41e4f`  |
| 1203   | No file              | `ed6888f41e4f`  |
| 1197   | No file              | `ed6888f41e4f`  |
| 1194   | No file              | `ed6888f41e4f`  |
| 1192   | No file              | `ed6888f41e4f`  |
| 1187   | No file              | `ed6888f41e4f`  |
| 1183   | No file              | `ed6888f41e4f`  |
| 1177   | No file              | `ed6888f41e4f`  |
| 1173   | No file              | `ed6888f41e4f`  |
| 1167   | No file              | `ed6888f41e4f`  |
| 1164   | No file              | `ed6888f41e4f`  |
| 1156   | No file              | `ed6888f41e4f`  |
| 1149   | No file              | `ed6888f41e4f`  |
| 1144   | No file              | `ed6888f41e4f`  |
| 1137   | No file              | `ed6888f41e4f`  |
| 1132   | No file              | `ed6888f41e4f`  |
| 1127   | No file              | `ed6888f41e4f`  |
| 1122   | No file              | `ed6888f41e4f`  |
| 1118   | No file              | `ed6888f41e4f`  |
| 1114   | No file              | `ed6888f41e4f`  |
| 1109   | No file              | `ed6888f41e4f`  |
| 1102   | No file              | `ed6888f41e4f`  |
| 1096   | No file              | `ed6888f41e4f`  |
| 1088   | No file              | `ed6888f41e4f`  |
| 1081   | No file              | `ed6888f41e4f`  |
| 1076   | No file              | `ed6888f41e4f`  |
| 1069   | No file              | `ed6888f41e4f`  |
| 1064   | No file              | `ed6888f41e4f`  |
| 1058   | No file              | `ed6888f41e4f`  |
| 1051   | No file              | `ed6888f41e4f`  |
| 1044   | No file              | `ed6888f41e4f`  |
| 1036   | No file              | `ed6888f41e4f`  |
| 1026   | No file              | `ed6888f41e4f`  |
| 1016   | No file              | `ed6888f41e4f`  |
| 1009   | No file              | `ed6888f41e4f`  |
| 1005   | No file              | `ed6888f41e4f`  |
| 1000   | No file              | `ed6888f41e4f`  |
| 998    | No file              | `ed6888f41e4f`  |
| 990    | No file              | `ed6888f41e4f`  |
| 979    | No file              | `ed6888f41e4f`  |
| 972    | No file              | `ed6888f41e4f`  |
| 963    | No file              | `ed6888f41e4f`  |
| 955    | No file              | `ed6888f41e4f`  |
| 946    | No file              | `ed6888f41e4f`  |
| 938    | No file              | `ed6888f41e4f`  |
| 927    | No file              | `ed6888f41e4f`  |
| 911    | No file              | `ed6888f41e4f`  |
| 904    | No file              | `ed6888f41e4f`  |
| 899    | No file              | `ed6888f41e4f`  |
| 894    | No file              | `ed6888f41e4f`  |
| 885    | No file              | `ed6888f41e4f`  |
| 879    | No file              | `ed6888f41e4f`  |
| 872    | No file              | `ed6888f41e4f`  |
| 864    | No file              | `ed6888f41e4f`  |
| 855    | No file              | `ed6888f41e4f`  |
| 853    | No file              | `ed6888f41e4f`  |
| 845    | No file              | `ed6888f41e4f`  |
| 837    | No file              | `ed6888f41e4f`  |
| 829    | No file              | `ed6888f41e4f`  |
| 822    | No file              | `ed6888f41e4f`  |
| 814    | No file              | `ed6888f41e4f`  |
| 805    | No file              | `ed6888f41e4f`  |
| 794    | No file              | `ed6888f41e4f`  |
| 787    | No file              | `ed6888f41e4f`  |
| 780    | No file              | `ed6888f41e4f`  |
| 771    | No file              | `ed6888f41e4f`  |
| 760    | No file              | `ed6888f41e4f`  |
| 748    | No file              | `ed6888f41e4f`  |
| 741    | No file              | `ed6888f41e4f`  |
| 736    | No file              | `ed6888f41e4f`  |
| 731    | No file              | `ed6888f41e4f`  |
| 723    | No file              | `ed6888f41e4f`  |
| 711    | No file              | `ed6888f41e4f`  |
| 707    | No file              | `ed6888f41e4f`  |
| 697    | No file              | `ed6888f41e4f`  |
| 689    | No file              | `ed6888f41e4f`  |
| 683    | No file              | `ed6888f41e4f`  |
| 678    | No file              | `ed6888f41e4f`  |
| 670    | No file              | `ed6888f41e4f`  |
| 661    | No file              | `ed6888f41e4f`  |
| 656    | No file              | `ed6888f41e4f`  |
| 652    | No file              | `ed6888f41e4f`  |
| 643    | No file              | `ed6888f41e4f`  |
| 637    | No file              | `ed6888f41e4f`  |
| 630    | No file              | `ed6888f41e4f`  |
| 627    | No file              | `ed6888f41e4f`  |
| 621    | No file              | `ed6888f41e4f`  |
| 617    | No file              | `ed6888f41e4f`  |
| 615    | No file              | `ed6888f41e4f`  |
| 606    | No file              | `ed6888f41e4f`  |
| 599    | No file              | `ed6888f41e4f`  |
| 592    | No file              | `ed6888f41e4f`  |
| 586    | No file              | `ed6888f41e4f`  |
| 577    | No file              | `ed6888f41e4f`  |
| 569    | No file              | `ed6888f41e4f`  |
| 561    | No file              | `ed6888f41e4f`  |
| 554    | No file              | `ed6888f41e4f`  |
| 542    | No file              | `ed6888f41e4f`  |
| 532    | No file              | `ed6888f41e4f`  |
| 531    | No file              | `ed6888f41e4f`  |
| 526    | No file              | `ed6888f41e4f`  |
| 521    | No file              | `ed6888f41e4f`  |
| 517    | No file              | `ed6888f41e4f`  |
| 510    | No file              | `ed6888f41e4f`  |
| 508    | No file              | `ed6888f41e4f`  |
| 504    | No file              | `ed6888f41e4f`  |
| 497    | No file              | `ed6888f41e4f`  |
| 491    | No file              | `ed6888f41e4f`  |
| 485    | No file              | `ed6888f41e4f`  |
| 478    | No file              | `ed6888f41e4f`  |
| 472    | No file              | `ed6888f41e4f`  |
| 466    | No file              | `ed6888f41e4f`  |
| 457    | No file              | `ed6888f41e4f`  |
| 452    | No file              | `ed6888f41e4f`  |
| 449    | No file              | `ed6888f41e4f`  |
| 435    | No file              | `ed6888f41e4f`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                        |
| --------------------------------- | -------- | ----------------------------------------------------------- |
| `pcgrowthoffset.dbss`             | Required | `class_type -> (offset, size)` of every record              |
| `languagedata_en.loc`             | Optional | Class name and description (type 21), combat type (type 37), item names (type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                                                       |
| ------- | ------------- | ------- | --------------------------------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `47` on client 3464, class types `0` to `46`             |
| `+0x04` | Record[count] | records | `count` variable-length records, each after a u8 copy of its class type     |

Each record is the u8 class type followed by the record body. The offset table points at the body, one byte past the copy, and its size covers the body only, so the next copy sits at `data_offset + data_size`. The last body ends at the end of the file (55,280 bytes on client 3464).

### Record (variable: 1 bytes + class record)

| Offset  | Type         | Field      | Notes                                                  |
| ------- | ------------ | ---------- | ------------------------------------------------------ |
| `+0x00` | u8           | key_prefix | Copy of the class type; the offset row points past it  |
| `+0x01` | Class Record | body       | `data_size` bytes; the offset row points at this field |

### Class Record (variable: 142 bytes + starter weapons and text)

Offsets count from `data_offset`.

| Offset                 | Type               | Field                    | Notes                                                                                   |
| ---------------------- | ------------------ | ------------------------ | --------------------------------------------------------------------------------------- |
| `+0x00`                | u8                 | class_type               | Same as the copy before it and the offset row key                                       |
| `+0x01`                | u16                | character_key            | Player prototype; LOC type 6 names it like the class (`1` Warrior, `2` Ranger)          |
| `+0x03`                | u16                | background_character_key | `101` to `149`; `100 + character_key` on 24 of 47 records. LOC type 6 names `101` Warrior, `102` Ranger |
| `+0x05`                | u16                | alterego_character_key   | `521` to `536`; LOC type 6 names them Combat Mercenary (`521` to `524`) and PC Mercenary (`536`) |
| `+0x07`                | u16                | worker_character_key     | `201` to `214`; LOC type 6 names `201` Warrior_TEST, `206` Musa, `214` Guardian         |
| `+0x09`                | u32                | unknown_09               | `0xED819B97` for character 1; the low byte is `0x96 + character_key` on class types 0 to 36 |
| `+0x0D`                | u8                 | unknown_0d               | Always `101`; see Field Names                                                           |
| `+0x0E`                | u32                | starter_count            | `0` to `3`                                                                              |
| `+0x12`                | u32[starter_count] | starter_weapons          | Item IDs of the class's beginner weapons (Rusty Longsword, Round Shield); Wukong, Scholar, Kunoichi, Ninja, Archer, Seraph and Deadeye list three |
| `starter_weapons+0x00` | Setup Block        | setup                    | See below                                                                               |
| `starter_weapons+0x63` | str16              | name_kr                  | Korean class name (`워리어`); LOC type 21 `str_id4` 0 holds the translation              |
| `name_kr+0x00`         | str16              | description_kr           | Korean class description; LOC type 21 `str_id4` 1 holds the translation                 |
| `description_kr+0x00`  | str16              | select_movie             | Class selection video, `UI_Customize/Movie/Movie_ClassSelect/<code>.webm`; empty on class types 13, 14 and 36 |
| `select_movie+0x00`    | u8                 | gender                   | `0` male, `1` female (Warrior, Musa and Striker `0`; Ranger, Sorceress and Valkyrie `1`) |
| `select_movie+0x01`    | str8[4]            | consume_actions          | Action names `v<code>_Consume_Lv1` to `Lv4` after a class code (`vPBW_*`, the Tamer code, on 16 records); empty on Guardian |
| `consume_actions+0x00` | Presentation Block | presentation             | See below; 71 bytes plus 8 per pair                                                     |
| `presentation+0x00`    | Model List         | weapon_models            | See below                                                                               |
| `weapon_models+0x00`   | Model List         | unknown_model_list       | Same paths as `weapon_models` on every record of client 3464                            |

The `str16` strings store a u64 length in UTF-16 units, then the text, with no terminator; the `str8` strings store a u64 byte length. No inline text holds a line break.

### Setup Block (99 bytes)

Offsets count from the start of the block. The 99 bytes are the same on all 47 records of client 3464 except `+0x5E`. The names come from the client 1784 `PC_Set_Table`, see Field Names.

| Offset  | Type    | Field                 | Notes                                                                    |
| ------- | ------- | --------------------- | ------------------------------------------------------------------------ |
| `+0x00` | f32[3]  | start_position        | `-154408.4`, `-335.9`, `135204.7`                                        |
| `+0x0C` | u32     | start_direction       | `270`                                                                    |
| `+0x10` | f32[3]  | new_start_position    | `-44361.7`, `1303.6`, `-1832.2`                                          |
| `+0x1C` | u32     | new_start_direction   | `180`                                                                    |
| `+0x20` | f32[3]  | new_start_position_2  | `-36121.8`, `27827.2`, `-420972.1`                                       |
| `+0x2C` | f32[9]  | unknown_2c            | Values from `-1315839.5` to `1143770.9`; not in Layout 1                 |
| `+0x50` | u32     | unknown_50            | `1`; see Field Names                                                     |
| `+0x54` | u32     | unknown_54            | `1`; see Field Names                                                     |
| `+0x58` | u32     | unknown_58            | `0`; see Field Names                                                     |
| `+0x5C` | i16     | field_no              | `1`                                                                      |
| `+0x5E` | u8      | combat_resource_type  | `CppEnums.CombatResourceType`, see Notes; the only byte that differs per class |
| `+0x5F` | u32     | start_waypoint_no     | `2`                                                                      |

### Presentation Block (variable: 71 bytes + lists)

Offsets count from the start of the block.

| Offset               | Type               | Field              | Notes                                                                                 |
| -------------------- | ------------------ | ------------------ | ------------------------------------------------------------------------------------- |
| `+0x00`              | f32[3]             | combo_color        | RGB, `0.0` to `1.0`; the parser returns `rrggbb` (Warrior `bc963f`)                   |
| `+0x0C`              | f32[3]             | awaken_combo_color | RGB of the awakening; equal to `combo_color` on 36 of 47 records                      |
| `+0x18`              | u8                 | combat_type        | `__eAttackType`: `0` Direct (melee), `1` Range, `2` Magical; see Notes                |
| `+0x19`              | u32[3]             | class_weapons      | Item IDs of the main, sub and awakening weapon (Warrior: Rusty Longsword, Round Shield, Mercenary's Steel Greatsword); `0` for none |
| `+0x25`              | u8                 | is_open            | `1` on the playable classes; equals `pcgrowthsimply.bss` `is_playable` on every class of clients 1784 and 3483, and the browser's Playable column reads it |
| `+0x26`              | u8                 | unknown_26         | `0`; see Field Names                                                                  |
| `+0x27`              | f32[3]             | start_character_angle | The sheet's `StartCharacterAngle` with its last two values swapped: `230.0` to `270.0`, then `0.3` to `0.8`, `-0.5` to `-0.3` |
| `+0x33`              | f32                | start_character_angle_y | `-38.0` to `50.0`                                                              |
| `+0x37`              | u32                | unknown_37         | `0`; not in Layout 1                                                                  |
| `+0x3B`              | u32                | unknown_list_count | `0` on every record                                                                   |
| `+0x3F`              | u32[unknown_list_count] | unknown_list  | Empty                                                                                 |
| `unknown_list+0x00`  | u32                | default_life_count | `0`, except `2` on Shai (class type 17)                                               |
| `unknown_list+0x04`  | u32[default_life_count][2] | default_life_skills | (life skill, level) pairs: the sheet's `DefaultLifeType` and `DefaultLifeLevel`. Shai: `0, 31` and `4, 31`, Gathering and Alchemy at level 31 in `CppEnums.LifeExperienceType` order |
| `default_life_skills+0x00` | u32          | unknown_end        | `0`; `pcgrowthsimply.bss` `unknown_06` copies it                                      |

### Model List (variable: 4 bytes + entries)

| Offset  | Type               | Field   | Notes                                                                     |
| ------- | ------------------ | ------- | ------------------------------------------------------------------------- |
| `+0x00` | u32                | count   | `3` on 41 records, `2` on Agent, `0` on class types 13, 14, 18, 22 and 36 |
| `+0x04` | Model Entry[count] | entries | `count` entries                                                           |

Each entry is a u8 slot (`1` main, `2` sub, `3` awakening) and a `str8` model path, such as `1_Pc/1_PHM/Weapon/1_OneHandSword/PHM_01_OHS_0004_R.pac` for the Warrior main weapon.

### Model Entry (variable: 9 bytes + path)

| Offset  | Type | Field | Notes                            |
| ------- | ---- | ----- | -------------------------------- |
| `+0x00` | u8   | slot  | `1` main, `2` sub, `3` awakening |
| `+0x01` | str8 | path  | Model path                       |

### `pcgrowthoffset.dbss`

Bare offset table into `pcgrowth.dbss` (no PABR magic, no trailer), read with `parse_bare_u8_offset_rows()` from `_common/pabr_offset.py`.

| Offset  | Type              | Field | Notes                                             |
| ------- | ----------------- | ----- | ------------------------------------------------- |
| `+0x00` | u32               | count | Number of offset rows; equals the main file count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                    |

### Offset Row (9 bytes)

| Offset  | Type | Field       | Notes                                                         |
| ------- | ---- | ----------- | ------------------------------------------------------------- |
| `+0x00` | u8   | class_type  | Key of the record it points at                                |
| `+0x01` | u32  | data_offset | Absolute byte offset of the record body, one past its u8 copy |
| `+0x05` | u32  | data_size   | Body size in bytes, `437` to `1485` on client 3464            |

The rows are in file order, which is not key order: 46 down to 32, 15 down to 0, then 31 down to 16. The parser checks the u8 copy before each body, that the body holds the same class type, and that it ends exactly at `data_offset + data_size`.

## Layout 1

On client 1784 the Class Record has no `unknown_09`, so `unknown_0d` follows
`worker_character_key` and every later field sits 4 bytes earlier, the Setup
Block has no `unknown_2c`, so it is 63 bytes, and the Presentation Block has
no `unknown_37`. The Class Record, the Setup Block and the Presentation Block
differ from Layout 2. Field names keep Layout 2's offsets, so `unknown_0d`
sits at `+0x09` here. The server dump of a private server on client 1784
reads the record in this order (`ReadRecord_pcGrowth`, VA `0x140bbb460`).

### Class Record (variable: 102 bytes + starter weapons and text)

| Offset                 | Type               | Field                    | Notes |
| ---------------------- | ------------------ | ------------------------ | ----- |
| `+0x00`                | u8                 | class_type               |       |
| `+0x01`                | u16                | character_key            |       |
| `+0x03`                | u16                | background_character_key |       |
| `+0x05`                | u16                | alterego_character_key   |       |
| `+0x07`                | u16                | worker_character_key     |       |
| `+0x09`                | u8                 | unknown_0d               |       |
| `+0x0A`                | u32                | starter_count            |       |
| `+0x0E`                | u32[starter_count] | starter_weapons          |       |
| `starter_weapons+0x00` | Setup Block        | setup                    |       |
| `starter_weapons+0x3F` | str16              | name_kr                  |       |
| `name_kr+0x00`         | str16              | description_kr           |       |
| `description_kr+0x00`  | str16              | select_movie             |       |
| `select_movie+0x00`    | u8                 | gender                   |       |
| `select_movie+0x01`    | str8[4]            | consume_actions          |       |
| `consume_actions+0x00` | Presentation Block | presentation             |       |
| `presentation+0x00`    | Model List         | weapon_models            |       |
| `weapon_models+0x00`   | Model List         | unknown_model_list       |       |

### Setup Block (63 bytes)

| Offset  | Type   | Field                | Notes |
| ------- | ------ | -------------------- | ----- |
| `+0x00` | f32[3] | start_position       |       |
| `+0x0C` | u32    | start_direction      |       |
| `+0x10` | f32[3] | new_start_position   |       |
| `+0x1C` | u32    | new_start_direction  |       |
| `+0x20` | f32[3] | new_start_position_2 |       |
| `+0x2C` | u32    | unknown_50           |       |
| `+0x30` | u32    | unknown_54           |       |
| `+0x34` | u32    | unknown_58           |       |
| `+0x38` | i16    | field_no             |       |
| `+0x3A` | u8     | combat_resource_type |       |
| `+0x3B` | u32    | start_waypoint_no    |       |

### Presentation Block (variable: 67 bytes + lists)

| Offset               | Type               | Field              | Notes                                          |
| -------------------- | ------------------ | ------------------ | ---------------------------------------------- |
| `+0x00`              | f32[3]             | combo_color        |                                                |
| `+0x0C`              | f32[3]             | awaken_combo_color |                                                |
| `+0x18`              | u8                 | combat_type        |                                                |
| `+0x19`              | u32[3]             | class_weapons      |                                                |
| `+0x25`              | u8                 | is_open            |                                                |
| `+0x26`              | u8                 | unknown_26         |                                                |
| `+0x27`              | f32[3]             | start_character_angle |                                             |
| `+0x33`              | f32                | start_character_angle_y |                                           |
| `+0x37`              | u32                | unknown_list_count |                                                |
| `+0x3B`              | u32[unknown_list_count] | unknown_list  |                                                |
| `unknown_list+0x00`  | u32                | default_life_count | `2` on Shai, else `0` on client 1784           |
| `unknown_list+0x04`  | u32[default_life_count][2] | default_life_skills |                                     |
| `default_life_skills+0x00` | u32          | unknown_end        |                                                |

## Localization

| Text        | LOC key                                               |
| ----------- | ----------------------------------------------------- |
| Class name  | type 21, `str_id1` = `class_type`, `str_id4` 0        |
| Description | type 21, `str_id1` = `class_type`, `str_id4` 1        |
| Weapons     | type 0, `str_id1` = item ID                           |
| Combat type | type 37, `GAME` sheet key per value (see Notes)       |

LOC type 21 has a name and a description for all 47 class types on client 3464, including the unused slots (`Ain (No Use)`, `PYFW5`). The English text matches the inline Korean (class type 0: `Warrior` for `워리어`). The handler shows the LOC name and falls back to the inline Korean, as does the [pcgrowthsimply](../bss/pcgrowthsimply_bss.md) handler.

## Notes

- iDevelopThings/bdo-data-extractor `FORMATS.md` lists this record layout. Checked against client 3464: the offset table and the record walk match, and all 47 records end at their recorded size. It reads the presentation block as seven f32 and a u32 at `+0x43`, with four extra u32 only on Shai; this doc reads `+0x3F` as a pair count, which gives the same byte total.
- `starter_weapons` start with the same main and sub weapon as `class_weapons` on every class with class weapons except Wukong and Ninja, which list them in another order (Ninja: Old Shuriken before Old Kunai).
- `combat_type` is the `__eAttackType` value that `global_newclass_data.luac` stores per class as `_attackType`. `panel_characterinfo_basic_all_1.luac` labels it on the character info panel with the `GAME` sheet keys `LUA_WARRIOR_AWAKEN_COMBAT_TYPE` (`Melee`), `LUA_RANGER_SUCCESSION_COMBAT_TYPE` (`Ranged`) and `LUA_ATKTYPE_MAGIC` (`Magic`); `combat_types.py` stores their `stringtable.bss` hashes. The Combat Type tooltip in game lists the same classes per value as the file:

  | Value | Label  | Playable class types |
  | ----- | ------ | -------------------- |
  | `0`   | Melee  | Warrior (0), Wukong (3), Guardian (5), Scholar (6), Drakania (7), Nova (9), Corsair (10), Lahn (11), Berserker (12), Shai (17), Striker (19), Musa (20), Maehwa (21), Mystic (23), Valkyrie (24), Kunoichi (25), Ninja (26), Seraph (32) |
  | `1`   | Ranged | Ranger (4), Archer (29), Deadeye (34), Agent (35) |
  | `2`   | Magic  | Hashashin (1), Sage (2), Sorceress (8), Maegu (15), Tamer (16), Dark Knight (27), Wizard (28), Woosa (30), Witch (31), Dosa (33) |

  Hashashin and Dark Knight fight at close range but count as magic classes. Of the unplayable slots, 13, 14, 22 and 36 hold `0`, and 18 and 37 to 46 hold `2`.
- `combat_resource_type` is the resource bar of the class. The character info panel (`panel_characterinfo_basic_all_1.luac`) labels each `CppEnums.CombatResourceType` value with a `GAME` sheet key; `combat_types.py` stores their hashes too. Counts are records on client 3464:

  | Value | Enum | Key                             | English | Records | Examples                         |
  | ----- | ---- | ------------------------------- | ------- | ------: | -------------------------------- |
  | `0`   | MP   | `LUA_CHARACTERINFO_TEXT_MP`     | MP      | 22      | Sorceress, Wizard, Witch, Tamer  |
  | `1`   | FP   | `LUA_CHARACTERINFO_TEXT_FP_NEW` | WP      | 16      | Warrior, Musa, Guardian, Striker |
  | `2`   | EP   | `LUA_CHARACTERINFO_TEXT_EP`     | MP      | 6       | Ranger, Shai, Archer, Deadeye    |
  | `3`   | BP   | `LUA_SELFCHARACTERINFO_BP`      | SP      | 3       | Valkyrie, Nova, Seraph           |

- The ten unplayable class types 37 to 46 (`PYFM`, `PYFW` to `PYFM5`, `PYFW5`) copy the Dosa (male) and Woosa (female) records: same gender, starter weapons, video, models and `unknown_09`, no class weapons.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols, and its `gc::PcGrowthStaticStatus` lists `_key`, `_characterKey`, `_backgroundCharacterKey`, `_alteregoCharacterKey`, `_workerCharacterKey`, `_parentKey`, `_defaultItemListKey`, `_startPosition`, three endurance decrease rates, `_fieldNo`, `_combatResourceType`, `_baseExploreNode`, `_name`, `_desc`, `_classMovie`, `_isWoman`, `_resourceSaveEffect[4]`, `_comboColor`, `_mainAttackType` and three default weapon keys in this order, the order this record stores them in. The server-side `PC_Set_Table` of a private server on client 519 has a column for each; I matched them over the 32 class types it shares with client 3464. Several classes have been reworked since, so the matches are partial but each one is the best column for its field:

| Field                    | `PC_Set_Table` column  | Matching (of 32) |
| ------------------------ | ---------------------- | ---------------: |
| character_key            | `CharacterKey`         | 32               |
| background_character_key | `BackgroundCharacterKey` | 24             |
| alterego_character_key   | `AlteregoKey`          | 27               |
| worker_character_key     | `WorkerCharacterKey`   | 26               |
| combat_resource_type     | `CombatResourceType`   | 25               |
| combo_color              | `ComboColor` (0 to 255 per channel) | 23  |
| awaken_combo_color       | `AwakenComboColor`     | 22               |
| combat_type              | `MainAttackType`       | 22               |
| class_weapons            | `DefaultVisibleWeapon`, `DefaultVisibleSubWeapon`, `DefaultVisibleAwakenWeapon` | 21 |

The `PC_Set_Table` sheet of a private server on client 1784 holds the
columns of the official client 1784 file in record order, and its server
dump reads the record field by field (`ReadRecord_pcGrowth`, VA
`0x140bbb460`; sheet loader `Load_PC_Set_Table`, VA `0x140894d40`). Matched
over all 82 class types of the official client 1784 file:

| Field                   | `PC_Set_Table` column              | Matching (of 82) | Client 3483 |
| ----------------------- | ---------------------------------- | ---------------: | ----------- |
| start_position          | `StartPosition`                    | 82 | Same values on all 47 |
| start_direction         | `StartDirection`                   | 82 | Same |
| new_start_position      | `NewStartPosition`                 | 82 | Same |
| new_start_direction     | `NewStartDirection`                | 82 | Same |
| new_start_position_2    | `NewStartPosition_2`               | 82 | Same; followed by the 9 floats of `unknown_2c` |
| field_no                | `FieldNo` (`ReadColumnInt16B`)     | 82 | Same |
| start_waypoint_no       | `StartWayPointNo`                  | 82 | Same |
| combat_resource_type    | `CombatResourceType`               | 82 | |
| is_open                 | `IsOpen`                           | 81; the sheet opens class 6, the file does not | Equals `pcgrowthsimply.bss` `is_playable` on all 47 |
| start_character_angle   | `StartCharacterAngle`, last two values swapped | 82 | |
| start_character_angle_y | `StartCharacterAngleY`             | 82 | |
| default_life_skills     | `DefaultLifeType`, `DefaultLifeLevel` zipped | 82 | The same Shai pairs |
| gender                  | `isWoman`                          | 81; the sheet makes class 3 female | |
| weapon_models           | `FakeVisibleWeapon`, `FakeVisibleSubWeapon`, `FakeVisibleAwakenWeapon` | 82 | |

The reads the sheet does not confirm keep their names:

- `unknown_0d` is read where the loader stores `ParentsClass`, empty on
  every sheet row, and the file stores `101` (no class, as `class_type`
  `101` elsewhere) on all of them. The 2016 `_parentKey` sits there too.
- `unknown_50`, `unknown_54` and `unknown_58` are read where the three
  endurance decrease rates go (`WeaponEnduranceDecreseRate`,
  `ArmorEnduranceDecreseRate`, `ArmorEnduranceArrowDecreseRate`). The sheet
  holds `0` for all three on every row, the file `1`, `1` and `0`.
- `unknown_26` is read into the member the loader fills from
  `IsDevelopingContents`, `0` on every row of the sheet and the file.
- `unknown_list` has no column and is empty on every client read; Layout 2
  adds `unknown_37`, also `0`, and either of its two u32 could be the count.
- The second model list repeats the first on every record; no column
  fills it.

## Open Questions

### Header Field unknown_09

`unknown_09` follows the character key in its low byte. It came after client 1862: the client 1784 record and sheet have nothing there. `unknown_0d` is the `ParentsClass` read, see Field Names.

### Setup Block

`unknown_2c` holds 9 floats that Layout 1 does not have, after `new_start_position_2`; they could be three more start positions. The endurance decrease rates in the `unknown_50` place read `1`, `1`, `0` where the sheet has `0`, see Field Names.

### Second Model List

Both model lists hold the same slots and paths on every record of client 3464. A record where they differ would show which one the class selection screen uses.
