# `pcgrowth.dbss` Format

## Purpose

The class selection record of every class type: the player character key of the class, its gender, its combat type (melee, ranged or magic), the beginner weapons of the class, the main, sub and awakening weapon of the class, the Korean name and description, and the class selection video. Despite the name, the file holds no per-level stat growth; nothing in it is indexed by character level. `pcgrowthoffset.dbss` lists where each record sits, [pcgrowthsimply](pcgrowthsimply_bss.md) is a fixed-row list of the same class types with a playable flag, and [pcgrowthdefaultcharacterkey](pcgrowthdefaultcharacterkey_bss.md) stores one character key.

The class type is the number `getClassType()` returns and the bit of a class mask (`_common/class_type.py`); the character key is the player prototype in `characterstatic.dbss` and LOC type 6. They differ for most classes: Ranger is class type 4 and character 2, Sorceress class type 8 and character 3.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes  | Records                                                                                            | Row bytes               |
| ------ | -------------- | ------- | --------------------- | ------ | -------------------------------------------------------------------------------------------------- | ----------------------- |
| 2      | 3314 and later | 3483    | `pcgrowth.dbss`       | 55,280 | 47 Setup Block, 47 Presentation Block, 250 Model Entry, 94 Model List, 47 Class Record, 47 Record  | 53 to 71, 58 on average |
| 2      | 3314 and later | 3483    | `pcgrowthoffset.dbss` | 427    | 47 Offset Row                                                                                      | 9                       |
| 1      | 1759 to 1862   | 1862    | `pcgrowth.dbss`       | 63,228 | 82 Setup Block, 82 Presentation Block, 164 Model List, 82 Class Record, 82 Record, 144 Model Entry | 4 to 196, 55 on average |
| 1      | 1759 to 1862   | 1862    | `pcgrowthoffset.dbss` | 742    | 82 Offset Row                                                                                      | 9                       |

| Layout | File                  | Known            | Unknown         |
| ------ | --------------------- | ---------------- | --------------- |
| 2      | `pcgrowth.dbss`       | 49,013 B (88.7%) | 6,267 B (11.3%) |
| 2      | `pcgrowthoffset.dbss` | 427 B (100.0%)   | 0 B (0.0%)      |
| 1      | `pcgrowth.dbss`       | 55,914 B (88.4%) | 7,314 B (11.6%) |
| 1      | `pcgrowthoffset.dbss` | 742 B (100.0%)   | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `cbcdea2aeeed`  |
| 3482   | Layout 2             | `cbcdea2aeeed`  |
| 3474   | Layout 2             | `cbcdea2aeeed`  |
| 3473   | Layout 2             | `cbcdea2aeeed`  |
| 3464   | Layout 2             | `cbcdea2aeeed`  |
| 3458   | Layout 2             | `cbcdea2aeeed`  |
| 3454   | Layout 2             | `cbcdea2aeeed`  |
| 3444   | Layout 2             | `cbcdea2aeeed`  |
| 3435   | Layout 2             | `cbcdea2aeeed`  |
| 3426   | Layout 2             | `cbcdea2aeeed`  |
| 3418   | Layout 2             | `cbcdea2aeeed`  |
| 3412   | Layout 2             | `cbcdea2aeeed`  |
| 3402   | Layout 2             | `cbcdea2aeeed`  |
| 3396   | Layout 2             | `cbcdea2aeeed`  |
| 3387   | Layout 2             | `cbcdea2aeeed`  |
| 3381   | Layout 2             | `cbcdea2aeeed`  |
| 3373   | Layout 2             | `cbcdea2aeeed`  |
| 3364   | Layout 2             | `cbcdea2aeeed`  |
| 3356   | Layout 2             | `cbcdea2aeeed`  |
| 3349   | Layout 2             | `cbcdea2aeeed`  |
| 3342   | Layout 2             | `cbcdea2aeeed`  |
| 3335   | Layout 2             | `cbcdea2aeeed`  |
| 3326   | Layout 2             | `cbcdea2aeeed`  |
| 3321   | Layout 2             | `cbcdea2aeeed`  |
| 3314   | Layout 2             | `cbcdea2aeeed`  |
| 3303   | No documented layout | `cbcdea2aeeed`  |
| 3302   | No documented layout | `cbcdea2aeeed`  |
| 3293   | No documented layout | `cbcdea2aeeed`  |
| 3283   | No documented layout | `cbcdea2aeeed`  |
| 3275   | No documented layout | `cbcdea2aeeed`  |
| 3267   | No documented layout | `cbcdea2aeeed`  |
| 3258   | No documented layout | `cbcdea2aeeed`  |
| 3251   | No documented layout | `cbcdea2aeeed`  |
| 3242   | No documented layout | `cbcdea2aeeed`  |
| 3235   | No documented layout | `cbcdea2aeeed`  |
| 3229   | No documented layout | `cbcdea2aeeed`  |
| 3212   | No documented layout | `cbcdea2aeeed`  |
| 3203   | No documented layout | `cbcdea2aeeed`  |
| 3193   | No documented layout | `cbcdea2aeeed`  |
| 3186   | No documented layout | `cbcdea2aeeed`  |
| 3177   | No documented layout | `cbcdea2aeeed`  |
| 3169   | No documented layout | `cbcdea2aeeed`  |
| 3158   | No documented layout | `cbcdea2aeeed`  |
| 3151   | No documented layout | `cbcdea2aeeed`  |
| 3144   | No documented layout | `cbcdea2aeeed`  |
| 3133   | No documented layout | `cbcdea2aeeed`  |
| 3125   | No documented layout | `cbcdea2aeeed`  |
| 3118   | No documented layout | `cbcdea2aeeed`  |
| 3111   | No documented layout | `cbcdea2aeeed`  |
| 3103   | No documented layout | `cbcdea2aeeed`  |
| 3095   | No documented layout | `cbcdea2aeeed`  |
| 3086   | No documented layout | `cbcdea2aeeed`  |
| 3072   | No documented layout | `cbcdea2aeeed`  |
| 3062   | No documented layout | `cbcdea2aeeed`  |
| 3052   | No documented layout | `cbcdea2aeeed`  |
| 3045   | No documented layout | `cbcdea2aeeed`  |
| 3037   | No documented layout | `cbcdea2aeeed`  |
| 3030   | No documented layout | `cbcdea2aeeed`  |
| 3021   | No documented layout | `cbcdea2aeeed`  |
| 3012   | No documented layout | `cbcdea2aeeed`  |
| 3002   | No documented layout | `cbcdea2aeeed`  |
| 2995   | No documented layout | `cbcdea2aeeed`  |
| 2987   | No documented layout | `cbcdea2aeeed`  |
| 2978   | No documented layout | `cbcdea2aeeed`  |
| 2970   | No documented layout | `cbcdea2aeeed`  |
| 2959   | No documented layout | `cbcdea2aeeed`  |
| 2951   | No documented layout | `cbcdea2aeeed`  |
| 2942   | No documented layout | `cbcdea2aeeed`  |
| 2935   | No documented layout | `cbcdea2aeeed`  |
| 2932   | No documented layout | `cbcdea2aeeed`  |
| 2923   | No documented layout | `cbcdea2aeeed`  |
| 2919   | No documented layout | `cbcdea2aeeed`  |
| 2907   | No documented layout | `cbcdea2aeeed`  |
| 2900   | No documented layout | `cbcdea2aeeed`  |
| 2891   | No documented layout | `cbcdea2aeeed`  |
| 2882   | No documented layout | `cbcdea2aeeed`  |
| 2872   | No documented layout | `cbcdea2aeeed`  |
| 2863   | No documented layout | `cbcdea2aeeed`  |
| 2855   | No documented layout | `cbcdea2aeeed`  |
| 2849   | No documented layout | `cbcdea2aeeed`  |
| 2844   | No documented layout | `cbcdea2aeeed`  |
| 2834   | No documented layout | `cbcdea2aeeed`  |
| 2825   | No documented layout | `cbcdea2aeeed`  |
| 2819   | No documented layout | `cbcdea2aeeed`  |
| 2811   | No documented layout | `cbcdea2aeeed`  |
| 2803   | No documented layout | `cbcdea2aeeed`  |
| 2794   | No documented layout | `cbcdea2aeeed`  |
| 2783   | No documented layout | `cbcdea2aeeed`  |
| 2774   | No documented layout | `cbcdea2aeeed`  |
| 2765   | No documented layout | `cbcdea2aeeed`  |
| 2756   | No documented layout | `cbcdea2aeeed`  |
| 2750   | No documented layout | `cbcdea2aeeed`  |
| 2743   | No documented layout | `cbcdea2aeeed`  |
| 2736   | No documented layout | `cbcdea2aeeed`  |
| 2726   | No documented layout | `cbcdea2aeeed`  |
| 2717   | No documented layout | `cbcdea2aeeed`  |
| 2709   | No documented layout | `cbcdea2aeeed`  |
| 2703   | No documented layout | `cbcdea2aeeed`  |
| 2695   | No documented layout | `cbcdea2aeeed`  |
| 2684   | No documented layout | `cbcdea2aeeed`  |
| 2672   | No documented layout | `cbcdea2aeeed`  |
| 2665   | No documented layout | `cbcdea2aeeed`  |
| 2657   | No documented layout | `cbcdea2aeeed`  |
| 2649   | No documented layout | `cbcdea2aeeed`  |
| 2644   | No documented layout | `cbcdea2aeeed`  |
| 2637   | No documented layout | `cbcdea2aeeed`  |
| 2629   | No documented layout | `cbcdea2aeeed`  |
| 2619   | No documented layout | `cbcdea2aeeed`  |
| 2612   | No documented layout | `cbcdea2aeeed`  |
| 2606   | No documented layout | `cbcdea2aeeed`  |
| 2602   | No documented layout | `cbcdea2aeeed`  |
| 2601   | No documented layout | `cbcdea2aeeed`  |
| 2592   | No documented layout | `cbcdea2aeeed`  |
| 2583   | No documented layout | `cbcdea2aeeed`  |
| 2575   | No documented layout | `cbcdea2aeeed`  |
| 2567   | No documented layout | `cbcdea2aeeed`  |
| 2560   | No documented layout | `cbcdea2aeeed`  |
| 2553   | No documented layout | `cbcdea2aeeed`  |
| 2545   | No documented layout | `cbcdea2aeeed`  |
| 2538   | No documented layout | `cbcdea2aeeed`  |
| 2529   | No documented layout | `cbcdea2aeeed`  |
| 2519   | No documented layout | `cbcdea2aeeed`  |
| 2513   | No documented layout | `cbcdea2aeeed`  |
| 2510   | No documented layout | `cbcdea2aeeed`  |
| 2507   | No documented layout | `cbcdea2aeeed`  |
| 2503   | No documented layout | `cbcdea2aeeed`  |
| 2498   | No documented layout | `cbcdea2aeeed`  |
| 2492   | No documented layout | `cbcdea2aeeed`  |
| 2487   | No documented layout | `cbcdea2aeeed`  |
| 2480   | No documented layout | `cbcdea2aeeed`  |
| 2474   | No documented layout | `cbcdea2aeeed`  |
| 2468   | No documented layout | `cbcdea2aeeed`  |
| 2460   | No documented layout | `cbcdea2aeeed`  |
| 2453   | No documented layout | `cbcdea2aeeed`  |
| 2444   | No documented layout | `cbcdea2aeeed`  |
| 2438   | No documented layout | `cbcdea2aeeed`  |
| 2434   | No documented layout | `cbcdea2aeeed`  |
| 2429   | No documented layout | `cbcdea2aeeed`  |
| 2421   | No documented layout | `cbcdea2aeeed`  |
| 2414   | No documented layout | `cbcdea2aeeed`  |
| 2407   | No documented layout | `cbcdea2aeeed`  |
| 2401   | No documented layout | `cbcdea2aeeed`  |
| 2397   | No documented layout | `cbcdea2aeeed`  |
| 2393   | No documented layout | `cbcdea2aeeed`  |
| 2384   | No documented layout | `cbcdea2aeeed`  |
| 2378   | No documented layout | `cbcdea2aeeed`  |
| 2372   | No documented layout | `cbcdea2aeeed`  |
| 2358   | No documented layout | `cbcdea2aeeed`  |
| 2352   | No documented layout | `cbcdea2aeeed`  |
| 2347   | No documented layout | `cbcdea2aeeed`  |
| 2343   | No documented layout | `cbcdea2aeeed`  |
| 2335   | No documented layout | `cbcdea2aeeed`  |
| 2327   | No documented layout | `cbcdea2aeeed`  |
| 2324   | No documented layout | `cbcdea2aeeed`  |
| 2319   | No documented layout | `cbcdea2aeeed`  |
| 2313   | No documented layout | `cbcdea2aeeed`  |
| 2308   | No documented layout | `cbcdea2aeeed`  |
| 2302   | No documented layout | `cbcdea2aeeed`  |
| 2295   | No documented layout | `cbcdea2aeeed`  |
| 2290   | No documented layout | `cbcdea2aeeed`  |
| 2284   | No documented layout | `cbcdea2aeeed`  |
| 2276   | No documented layout | `cbcdea2aeeed`  |
| 2269   | No documented layout | `cbcdea2aeeed`  |
| 2259   | No documented layout | `cbcdea2aeeed`  |
| 2250   | No documented layout | `cbcdea2aeeed`  |
| 2243   | No documented layout | `cbcdea2aeeed`  |
| 2235   | No documented layout | `cbcdea2aeeed`  |
| 2229   | No documented layout | `cbcdea2aeeed`  |
| 2224   | No documented layout | `cbcdea2aeeed`  |
| 2218   | No documented layout | `cbcdea2aeeed`  |
| 2215   | No documented layout | `cbcdea2aeeed`  |
| 2207   | No documented layout | `cbcdea2aeeed`  |
| 2203   | No documented layout | `cbcdea2aeeed`  |
| 2196   | No documented layout | `cbcdea2aeeed`  |
| 2192   | No documented layout | `cbcdea2aeeed`  |
| 2189   | No documented layout | `cbcdea2aeeed`  |
| 2183   | No documented layout | `cbcdea2aeeed`  |
| 2179   | No documented layout | `cbcdea2aeeed`  |
| 2171   | No documented layout | `cbcdea2aeeed`  |
| 2163   | No documented layout | `cbcdea2aeeed`  |
| 2156   | No documented layout | `cbcdea2aeeed`  |
| 2151   | No documented layout | `cbcdea2aeeed`  |
| 2147   | No documented layout | `cbcdea2aeeed`  |
| 2142   | No documented layout | `cbcdea2aeeed`  |
| 2138   | No documented layout | `cbcdea2aeeed`  |
| 2134   | No documented layout | `cbcdea2aeeed`  |
| 2130   | No documented layout | `cbcdea2aeeed`  |
| 2122   | No documented layout | `cbcdea2aeeed`  |
| 2107   | No documented layout | `cbcdea2aeeed`  |
| 2098   | No documented layout | `cbcdea2aeeed`  |
| 2089   | No documented layout | `cbcdea2aeeed`  |
| 2081   | No documented layout | `cbcdea2aeeed`  |
| 2073   | No documented layout | `cbcdea2aeeed`  |
| 2067   | No documented layout | `cbcdea2aeeed`  |
| 2063   | No documented layout | `cbcdea2aeeed`  |
| 2059   | No documented layout | `cbcdea2aeeed`  |
| 2052   | No documented layout | `cbcdea2aeeed`  |
| 2044   | No documented layout | `cbcdea2aeeed`  |
| 2039   | No documented layout | `cbcdea2aeeed`  |
| 2032   | No documented layout | `cbcdea2aeeed`  |
| 2025   | No documented layout | `cbcdea2aeeed`  |
| 2011   | No documented layout | `cbcdea2aeeed`  |
| 2005   | No documented layout | `cbcdea2aeeed`  |
| 2000   | No documented layout | `cbcdea2aeeed`  |
| 1996   | No documented layout | `cbcdea2aeeed`  |
| 1991   | No documented layout | `cbcdea2aeeed`  |
| 1985   | No documented layout | `cbcdea2aeeed`  |
| 1980   | No documented layout | `cbcdea2aeeed`  |
| 1969   | No documented layout | `cbcdea2aeeed`  |
| 1964   | No documented layout | `cbcdea2aeeed`  |
| 1958   | No documented layout | `cbcdea2aeeed`  |
| 1950   | No documented layout | `cbcdea2aeeed`  |
| 1945   | No documented layout | `cbcdea2aeeed`  |
| 1937   | No documented layout | `cbcdea2aeeed`  |
| 1933   | No documented layout | `cbcdea2aeeed`  |
| 1927   | No documented layout | `cbcdea2aeeed`  |
| 1921   | No documented layout | `cbcdea2aeeed`  |
| 1914   | No documented layout | `cbcdea2aeeed`  |
| 1908   | No documented layout | `cbcdea2aeeed`  |
| 1897   | No documented layout | `cbcdea2aeeed`  |
| 1892   | No documented layout | `cbcdea2aeeed`  |
| 1886   | No documented layout | `cbcdea2aeeed`  |
| 1881   | No documented layout | `cbcdea2aeeed`  |
| 1871   | No documented layout | `cbcdea2aeeed`  |
| 1866   | No documented layout | `cbcdea2aeeed`  |
| 1862   | Layout 1             | `cbcdea2aeeed`  |
| 1854   | Layout 1             | `cbcdea2aeeed`  |
| 1846   | Layout 1             | `cbcdea2aeeed`  |
| 1838   | Layout 1             | `cbcdea2aeeed`  |
| 1832   | Layout 1             | `cbcdea2aeeed`  |
| 1826   | Layout 1             | `cbcdea2aeeed`  |
| 1822   | Layout 1             | `cbcdea2aeeed`  |
| 1818   | Layout 1             | `cbcdea2aeeed`  |
| 1804   | Layout 1             | `cbcdea2aeeed`  |
| 1794   | Layout 1             | `cbcdea2aeeed`  |
| 1790   | Layout 1             | `cbcdea2aeeed`  |
| 1784   | Layout 1             | `cbcdea2aeeed`  |
| 1774   | Layout 1             | `cbcdea2aeeed`  |
| 1771   | Layout 1             | `cbcdea2aeeed`  |
| 1762   | Layout 1             | `cbcdea2aeeed`  |
| 1759   | Layout 1             | `cbcdea2aeeed`  |
| 1754   | No documented layout | `cbcdea2aeeed`  |
| 1749   | No documented layout | `cbcdea2aeeed`  |
| 1743   | No documented layout | `cbcdea2aeeed`  |
| 1737   | No documented layout | `cbcdea2aeeed`  |
| 1731   | No documented layout | `cbcdea2aeeed`  |
| 1725   | No documented layout | `cbcdea2aeeed`  |
| 1717   | No documented layout | `cbcdea2aeeed`  |
| 1710   | No documented layout | `cbcdea2aeeed`  |
| 1704   | No documented layout | `cbcdea2aeeed`  |
| 1698   | No documented layout | `cbcdea2aeeed`  |
| 1690   | No documented layout | `cbcdea2aeeed`  |
| 1685   | No documented layout | `cbcdea2aeeed`  |
| 1680   | No documented layout | `cbcdea2aeeed`  |
| 1674   | No documented layout | `cbcdea2aeeed`  |
| 1668   | No documented layout | `cbcdea2aeeed`  |
| 1659   | No documented layout | `cbcdea2aeeed`  |
| 1649   | No documented layout | `cbcdea2aeeed`  |
| 1642   | No documented layout | `cbcdea2aeeed`  |
| 1636   | No documented layout | `cbcdea2aeeed`  |
| 1628   | No documented layout | `cbcdea2aeeed`  |
| 1622   | No documented layout | `cbcdea2aeeed`  |
| 1614   | No documented layout | `cbcdea2aeeed`  |
| 1608   | No documented layout | `cbcdea2aeeed`  |
| 1602   | No documented layout | `cbcdea2aeeed`  |
| 1598   | No documented layout | `cbcdea2aeeed`  |
| 1594   | No documented layout | `cbcdea2aeeed`  |
| 1590   | No documented layout | `cbcdea2aeeed`  |
| 1587   | No documented layout | `cbcdea2aeeed`  |
| 1584   | No documented layout | `cbcdea2aeeed`  |
| 1579   | No documented layout | `cbcdea2aeeed`  |
| 1572   | No documented layout | `cbcdea2aeeed`  |
| 1565   | No documented layout | `cbcdea2aeeed`  |
| 1559   | No documented layout | `cbcdea2aeeed`  |
| 1554   | No documented layout | `cbcdea2aeeed`  |
| 1547   | No documented layout | `cbcdea2aeeed`  |
| 1537   | No documented layout | `cbcdea2aeeed`  |
| 1529   | No documented layout | `cbcdea2aeeed`  |
| 1524   | No documented layout | `cbcdea2aeeed`  |
| 1519   | No documented layout | `cbcdea2aeeed`  |
| 1509   | No documented layout | `cbcdea2aeeed`  |
| 1506   | No documented layout | `cbcdea2aeeed`  |
| 1504   | No documented layout | `cbcdea2aeeed`  |
| 1500   | No documented layout | `cbcdea2aeeed`  |
| 1493   | No documented layout | `cbcdea2aeeed`  |
| 1489   | No documented layout | `cbcdea2aeeed`  |
| 1485   | No documented layout | `cbcdea2aeeed`  |
| 1481   | No documented layout | `cbcdea2aeeed`  |
| 1474   | No documented layout | `cbcdea2aeeed`  |
| 1466   | No documented layout | `cbcdea2aeeed`  |
| 1462   | No documented layout | `cbcdea2aeeed`  |
| 1459   | No documented layout | `cbcdea2aeeed`  |
| 1453   | No documented layout | `cbcdea2aeeed`  |
| 1450   | No documented layout | `cbcdea2aeeed`  |
| 1445   | No documented layout | `cbcdea2aeeed`  |
| 1439   | No documented layout | `cbcdea2aeeed`  |
| 1433   | No documented layout | `cbcdea2aeeed`  |
| 1430   | No documented layout | `cbcdea2aeeed`  |
| 1426   | No documented layout | `cbcdea2aeeed`  |
| 1421   | No documented layout | `cbcdea2aeeed`  |
| 1417   | No documented layout | `cbcdea2aeeed`  |
| 1416   | No documented layout | `cbcdea2aeeed`  |
| 1409   | No documented layout | `cbcdea2aeeed`  |
| 1405   | No documented layout | `cbcdea2aeeed`  |
| 1401   | No documented layout | `cbcdea2aeeed`  |
| 1396   | No documented layout | `cbcdea2aeeed`  |
| 1391   | No documented layout | `cbcdea2aeeed`  |
| 1390   | No documented layout | `cbcdea2aeeed`  |
| 1386   | No documented layout | `cbcdea2aeeed`  |
| 1381   | No documented layout | `cbcdea2aeeed`  |
| 1379   | No documented layout | `cbcdea2aeeed`  |
| 1372   | No documented layout | `cbcdea2aeeed`  |
| 1366   | No documented layout | `cbcdea2aeeed`  |
| 1364   | No documented layout | `cbcdea2aeeed`  |
| 1363   | No documented layout | `cbcdea2aeeed`  |
| 1360   | No documented layout | `cbcdea2aeeed`  |
| 1358   | No documented layout | `cbcdea2aeeed`  |
| 1355   | No documented layout | `cbcdea2aeeed`  |
| 1351   | No documented layout | `cbcdea2aeeed`  |
| 1348   | No documented layout | `cbcdea2aeeed`  |
| 1346   | No documented layout | `cbcdea2aeeed`  |
| 1341   | No documented layout | `cbcdea2aeeed`  |
| 1340   | No documented layout | `cbcdea2aeeed`  |
| 1338   | No documented layout | `cbcdea2aeeed`  |
| 1335   | No documented layout | `cbcdea2aeeed`  |
| 1333   | No documented layout | `cbcdea2aeeed`  |
| 1329   | No documented layout | `cbcdea2aeeed`  |
| 1327   | No documented layout | `cbcdea2aeeed`  |
| 1324   | No documented layout | `cbcdea2aeeed`  |
| 1321   | No documented layout | `cbcdea2aeeed`  |
| 1319   | No documented layout | `cbcdea2aeeed`  |
| 1318   | No documented layout | `cbcdea2aeeed`  |
| 1316   | No documented layout | `cbcdea2aeeed`  |
| 1313   | No documented layout | `cbcdea2aeeed`  |
| 1311   | No documented layout | `cbcdea2aeeed`  |
| 1309   | No documented layout | `cbcdea2aeeed`  |
| 1304   | No documented layout | `cbcdea2aeeed`  |
| 1292   | No documented layout | `cbcdea2aeeed`  |
| 1286   | No documented layout | `cbcdea2aeeed`  |
| 1280   | No documented layout | `cbcdea2aeeed`  |
| 1276   | No documented layout | `cbcdea2aeeed`  |
| 1267   | No documented layout | `cbcdea2aeeed`  |
| 1261   | No documented layout | `cbcdea2aeeed`  |
| 1256   | No documented layout | `cbcdea2aeeed`  |
| 1250   | No documented layout | `cbcdea2aeeed`  |
| 1246   | No file              | `cbcdea2aeeed`  |
| 1239   | No file              | `cbcdea2aeeed`  |
| 1230   | No file              | `cbcdea2aeeed`  |
| 1226   | No file              | `cbcdea2aeeed`  |
| 1220   | No file              | `cbcdea2aeeed`  |
| 1217   | No file              | `cbcdea2aeeed`  |
| 1211   | No file              | `cbcdea2aeeed`  |
| 1210   | No file              | `cbcdea2aeeed`  |
| 1208   | No file              | `cbcdea2aeeed`  |
| 1203   | No file              | `cbcdea2aeeed`  |
| 1197   | No file              | `cbcdea2aeeed`  |
| 1194   | No file              | `cbcdea2aeeed`  |
| 1192   | No file              | `cbcdea2aeeed`  |
| 1187   | No file              | `cbcdea2aeeed`  |
| 1183   | No file              | `cbcdea2aeeed`  |
| 1177   | No file              | `cbcdea2aeeed`  |
| 1173   | No file              | `cbcdea2aeeed`  |
| 1167   | No file              | `cbcdea2aeeed`  |
| 1164   | No file              | `cbcdea2aeeed`  |
| 1156   | No file              | `cbcdea2aeeed`  |
| 1149   | No file              | `cbcdea2aeeed`  |
| 1144   | No file              | `cbcdea2aeeed`  |
| 1137   | No file              | `cbcdea2aeeed`  |
| 1132   | No file              | `cbcdea2aeeed`  |
| 1127   | No file              | `cbcdea2aeeed`  |
| 1122   | No file              | `cbcdea2aeeed`  |
| 1118   | No file              | `cbcdea2aeeed`  |
| 1114   | No file              | `cbcdea2aeeed`  |
| 1109   | No file              | `cbcdea2aeeed`  |
| 1102   | No file              | `cbcdea2aeeed`  |
| 1096   | No file              | `cbcdea2aeeed`  |
| 1088   | No file              | `cbcdea2aeeed`  |
| 1081   | No file              | `cbcdea2aeeed`  |
| 1076   | No file              | `cbcdea2aeeed`  |
| 1069   | No file              | `cbcdea2aeeed`  |
| 1064   | No file              | `cbcdea2aeeed`  |
| 1058   | No file              | `cbcdea2aeeed`  |
| 1051   | No file              | `cbcdea2aeeed`  |
| 1044   | No file              | `cbcdea2aeeed`  |
| 1036   | No file              | `cbcdea2aeeed`  |
| 1026   | No file              | `cbcdea2aeeed`  |
| 1016   | No file              | `cbcdea2aeeed`  |
| 1009   | No file              | `cbcdea2aeeed`  |
| 1005   | No file              | `cbcdea2aeeed`  |
| 1000   | No file              | `cbcdea2aeeed`  |
| 998    | No file              | `cbcdea2aeeed`  |
| 990    | No file              | `cbcdea2aeeed`  |
| 979    | No file              | `cbcdea2aeeed`  |
| 972    | No file              | `cbcdea2aeeed`  |
| 963    | No file              | `cbcdea2aeeed`  |
| 955    | No file              | `cbcdea2aeeed`  |
| 946    | No file              | `cbcdea2aeeed`  |
| 938    | No file              | `cbcdea2aeeed`  |
| 927    | No file              | `cbcdea2aeeed`  |
| 911    | No file              | `cbcdea2aeeed`  |
| 904    | No file              | `cbcdea2aeeed`  |
| 899    | No file              | `cbcdea2aeeed`  |
| 894    | No file              | `cbcdea2aeeed`  |
| 885    | No file              | `cbcdea2aeeed`  |
| 879    | No file              | `cbcdea2aeeed`  |
| 872    | No file              | `cbcdea2aeeed`  |
| 864    | No file              | `cbcdea2aeeed`  |
| 855    | No file              | `cbcdea2aeeed`  |
| 853    | No file              | `cbcdea2aeeed`  |
| 845    | No file              | `cbcdea2aeeed`  |
| 837    | No file              | `cbcdea2aeeed`  |
| 829    | No file              | `cbcdea2aeeed`  |
| 822    | No file              | `cbcdea2aeeed`  |
| 814    | No file              | `cbcdea2aeeed`  |
| 805    | No file              | `cbcdea2aeeed`  |
| 794    | No file              | `cbcdea2aeeed`  |
| 787    | No file              | `cbcdea2aeeed`  |
| 780    | No file              | `cbcdea2aeeed`  |
| 771    | No file              | `cbcdea2aeeed`  |
| 760    | No file              | `cbcdea2aeeed`  |
| 748    | No file              | `cbcdea2aeeed`  |
| 741    | No file              | `cbcdea2aeeed`  |
| 736    | No file              | `cbcdea2aeeed`  |
| 731    | No file              | `cbcdea2aeeed`  |
| 723    | No file              | `cbcdea2aeeed`  |
| 711    | No file              | `cbcdea2aeeed`  |
| 707    | No file              | `cbcdea2aeeed`  |
| 697    | No file              | `cbcdea2aeeed`  |
| 689    | No file              | `cbcdea2aeeed`  |
| 683    | No file              | `cbcdea2aeeed`  |
| 678    | No file              | `cbcdea2aeeed`  |
| 670    | No file              | `cbcdea2aeeed`  |
| 661    | No file              | `cbcdea2aeeed`  |
| 656    | No file              | `cbcdea2aeeed`  |
| 652    | No file              | `cbcdea2aeeed`  |
| 643    | No file              | `cbcdea2aeeed`  |
| 637    | No file              | `cbcdea2aeeed`  |
| 630    | No file              | `cbcdea2aeeed`  |
| 627    | No file              | `cbcdea2aeeed`  |
| 621    | No file              | `cbcdea2aeeed`  |
| 617    | No file              | `cbcdea2aeeed`  |
| 615    | No file              | `cbcdea2aeeed`  |
| 606    | No file              | `cbcdea2aeeed`  |
| 599    | No file              | `cbcdea2aeeed`  |
| 592    | No file              | `cbcdea2aeeed`  |
| 586    | No file              | `cbcdea2aeeed`  |
| 577    | No file              | `cbcdea2aeeed`  |
| 569    | No file              | `cbcdea2aeeed`  |
| 561    | No file              | `cbcdea2aeeed`  |
| 554    | No file              | `cbcdea2aeeed`  |
| 542    | No file              | `cbcdea2aeeed`  |
| 532    | No file              | `cbcdea2aeeed`  |
| 531    | No file              | `cbcdea2aeeed`  |
| 526    | No file              | `cbcdea2aeeed`  |
| 521    | No file              | `cbcdea2aeeed`  |
| 517    | No file              | `cbcdea2aeeed`  |
| 510    | No file              | `cbcdea2aeeed`  |
| 508    | No file              | `cbcdea2aeeed`  |
| 504    | No file              | `cbcdea2aeeed`  |
| 497    | No file              | `cbcdea2aeeed`  |
| 491    | No file              | `cbcdea2aeeed`  |
| 485    | No file              | `cbcdea2aeeed`  |
| 478    | No file              | `cbcdea2aeeed`  |
| 472    | No file              | `cbcdea2aeeed`  |
| 466    | No file              | `cbcdea2aeeed`  |
| 457    | No file              | `cbcdea2aeeed`  |
| 452    | No file              | `cbcdea2aeeed`  |
| 449    | No file              | `cbcdea2aeeed`  |
| 435    | No file              | `cbcdea2aeeed`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                        |
| --------------------------------- | -------- | ----------------------------------------------------------- |
| `pcgrowthoffset.dbss`             | Required | `class_type -> (offset, size)` of every record              |
| `pcgrowthsimply.bss`              | Optional | Playable flag per class type, see [pcgrowthsimply](pcgrowthsimply_bss.md) |
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
| `+0x0D`                | u8                 | unknown_0d               | Always `101`                                                                            |
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

Offsets count from the start of the block. The 99 bytes are the same on all 47 records of client 3464 except `+0x5E`.

| Offset  | Type    | Field                | Notes                                                                    |
| ------- | ------- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | f32[3]  | unknown_00           | `-154408.4`, `-335.9`, `135204.7`                                        |
| `+0x0C` | u32     | unknown_0c           | `270`                                                                    |
| `+0x10` | f32[3]  | unknown_10           | `-44361.7`, `1303.6`, `-1832.2`                                          |
| `+0x1C` | u32     | unknown_1c           | `180`                                                                    |
| `+0x20` | f32[12] | unknown_20           | Values from `-1315839.5` to `1143770.9`                                  |
| `+0x50` | u32     | unknown_50           | `1`                                                                      |
| `+0x54` | u32     | unknown_54           | `1`                                                                      |
| `+0x58` | u32     | unknown_58           | `0`                                                                      |
| `+0x5C` | u8      | unknown_5c           | `1`                                                                      |
| `+0x5D` | u8      | unknown_5d           | `0`                                                                      |
| `+0x5E` | u8      | combat_resource_type | `CppEnums.CombatResourceType`, see Notes; the only byte that differs per class |
| `+0x5F` | u8      | unknown_5f           | `2`                                                                      |
| `+0x60` | u8[3]   | unknown_60           | `0`                                                                      |

### Presentation Block (variable: 71 bytes + 8 per pair)

Offsets count from the start of the block.

| Offset               | Type               | Field              | Notes                                                                                 |
| -------------------- | ------------------ | ------------------ | ------------------------------------------------------------------------------------- |
| `+0x00`              | f32[3]             | combo_color        | RGB, `0.0` to `1.0`; the parser returns `rrggbb` (Warrior `bc963f`)                   |
| `+0x0C`              | f32[3]             | awaken_combo_color | RGB of the awakening; equal to `combo_color` on 36 of 47 records                      |
| `+0x18`              | u8                 | combat_type        | `__eAttackType`: `0` Direct (melee), `1` Range, `2` Magical; see Notes                |
| `+0x19`              | u32[3]             | class_weapons      | Item IDs of the main, sub and awakening weapon (Warrior: Rusty Longsword, Round Shield, Mercenary's Steel Greatsword); `0` for none |
| `+0x25`              | u16                | unknown_25         | `1` when the main weapon is set, else `0`                                             |
| `+0x27`              | f32[6]             | unknown_27         | First value `230.0` to `270.0`, then `0.3` to `0.8`, `-0.5` to `-0.3`, `-38.0` to `50.0`, `0.0`, `0.0` |
| `+0x3F`              | u32                | pair_count         | `0`, except `2` on Shai (class type 17)                                               |
| `+0x43`              | u32[pair_count][2] | unknown_pairs      | 8 bytes per pair. Shai: u32 values `0, 31, 4, 31`                                     |
| `unknown_pairs+0x00` | u32                | unknown_end        | `0`                                                                                   |

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
`worker_character_key` and every later field sits 4 bytes earlier, and
`unknown_20` of the Setup Block holds 3 floats instead of 12, so the block is
63 bytes, and `unknown_27` of the Presentation Block holds 5 floats instead
of 6. The Class Record, the Setup Block and the Presentation Block differ
from Layout 2. Field
names keep Layout 2's offsets, so `unknown_0d` sits at `+0x09` here.

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
| `+0x00` | f32[3] | unknown_00           |       |
| `+0x0C` | u32    | unknown_0c           |       |
| `+0x10` | f32[3] | unknown_10           |       |
| `+0x1C` | u32    | unknown_1c           |       |
| `+0x20` | f32[3] | unknown_20           |       |
| `+0x2C` | u32    | unknown_50           |       |
| `+0x30` | u32    | unknown_54           |       |
| `+0x34` | u32    | unknown_58           |       |
| `+0x38` | u8     | unknown_5c           |       |
| `+0x39` | u8     | unknown_5d           |       |
| `+0x3A` | u8     | combat_resource_type |       |
| `+0x3B` | u8     | unknown_5f           |       |
| `+0x3C` | u8[3]  | unknown_60           |       |

### Presentation Block (variable: 67 bytes + 8 per pair)

| Offset               | Type               | Field              | Notes                                          |
| -------------------- | ------------------ | ------------------ | ---------------------------------------------- |
| `+0x00`              | f32[3]             | combo_color        |                                                |
| `+0x0C`              | f32[3]             | awaken_combo_color |                                                |
| `+0x18`              | u8                 | combat_type        |                                                |
| `+0x19`              | u32[3]             | class_weapons      |                                                |
| `+0x25`              | u16                | unknown_25         |                                                |
| `+0x27`              | f32[5]             | unknown_27         | Shai (class type 17): `100.0`, `0.7`, `-0.3`, `-38.0`, `0.0` on client 1784 |
| `+0x3B`              | u32                | pair_count         | `2` on Shai, else `0` on client 1784           |
| `+0x3F`              | u32[pair_count][2] | unknown_pairs      |                                                |
| `unknown_pairs+0x00` | u32                | unknown_end        |                                                |

## Localization

| Text        | LOC key                                               |
| ----------- | ----------------------------------------------------- |
| Class name  | type 21, `str_id1` = `class_type`, `str_id4` 0        |
| Description | type 21, `str_id1` = `class_type`, `str_id4` 1        |
| Weapons     | type 0, `str_id1` = item ID                           |
| Combat type | type 37, `GAME` sheet key per value (see Notes)       |

LOC type 21 has a name and a description for all 47 class types on client 3464, including the unused slots (`Ain (No Use)`, `PYFW5`). The English text matches the inline Korean (class type 0: `Warrior` for `워리어`). The handler shows the LOC name and falls back to the inline Korean, as does the [pcgrowthsimply](pcgrowthsimply_bss.md) handler.

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

## Open Questions

### Header Fields unknown_09 and unknown_0d

`unknown_09` follows the character key in its low byte, and `unknown_0d` is always `101`. The 2016 struct has only `_parentKey` (a class type) between the worker key and the starter item list, so both are later additions or a reworked `_parentKey`.

### Setup Block

The 99 bytes are the same on every class except `combat_resource_type`. In the 2016 order the start position, three endurance decrease rates and `_fieldNo` come here. `unknown_10` (`-44361.7`, `1303.6`, `-1832.2`) is close to the server's `StartPosition` (`-44361, 1350, -1832`), and `unknown_00` and `unknown_0c` could be the newer `NewStartPosition` and its direction, but the server values (`-59881, -3758.18, 48109`) do not match, so neither is named yet.

### Presentation Block

`unknown_25` is `1` on exactly the playable classes, like the server's `IsOpen`, but it matches only 22 of 32 server rows. The f32[6] at `+0x27` do not match the server's `StartCharacterAngle` (`160, -0.6, 2.3`). The Shai pairs (`0, 31, 4, 31`) could also read as a zero u32 followed by `31, 4, 31, 0`.

### Second Model List

Both model lists hold the same slots and paths on every record of client 3464. A record where they differ would show which one the class selection screen uses.
