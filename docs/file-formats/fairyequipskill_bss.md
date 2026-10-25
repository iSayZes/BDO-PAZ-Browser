# `fairyequipskill.bss` Format

## Purpose

Defines the fairy skill catalog, the 35 skills a fairy can hold, grouped into 8 skill types with tier progressions (e.g. `Tingling Breath I`–`V`). Each record stores its skill type group and a `gc::SkillKey` (skill level and skill number); the skill number resolves to both the skill name and its effect description, and doubles as the icon filename number.

The remainder of the file is a 200-slot reserved block of null placeholders, so the catalog can grow without changing the layout.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records                   | Row bytes |
| ------ | -------------- | --------------------- | ----- | ------------------------- | --------- |
| 2      | 1921 and later | `fairyequipskill.bss` | 3,636 | 35 Skill Record, 200 Slot | 16        |
| 1      | 805 to 1871    | `fairyequipskill.bss` | 1,576 | 30 Skill Record, 100 Slot | 12        |

| Layout | File                  | Known            | Unknown       |
| ------ | --------------------- | ---------------- | ------------- |
| 2      | `fairyequipskill.bss` | 2,836 B (78.0%)  | 800 B (22.0%) |
| 1      | `fairyequipskill.bss` | 1,576 B (100.0%) | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `ccdd6ac3b7cb`  |
| 3482   | Layout 2             | `ccdd6ac3b7cb`  |
| 3474   | Layout 2             | `ccdd6ac3b7cb`  |
| 3473   | Layout 2             | `ccdd6ac3b7cb`  |
| 3464   | Layout 2             | `ccdd6ac3b7cb`  |
| 3458   | Layout 2             | `ccdd6ac3b7cb`  |
| 3454   | Layout 2             | `ccdd6ac3b7cb`  |
| 3444   | Layout 2             | `ccdd6ac3b7cb`  |
| 3435   | Layout 2             | `ccdd6ac3b7cb`  |
| 3426   | Layout 2             | `ccdd6ac3b7cb`  |
| 3418   | Layout 2             | `ccdd6ac3b7cb`  |
| 3412   | Layout 2             | `ccdd6ac3b7cb`  |
| 3402   | Layout 2             | `ccdd6ac3b7cb`  |
| 3396   | Layout 2             | `ccdd6ac3b7cb`  |
| 3387   | Layout 2             | `ccdd6ac3b7cb`  |
| 3381   | Layout 2             | `ccdd6ac3b7cb`  |
| 3373   | Layout 2             | `ccdd6ac3b7cb`  |
| 3364   | Layout 2             | `ccdd6ac3b7cb`  |
| 3356   | Layout 2             | `ccdd6ac3b7cb`  |
| 3349   | Layout 2             | `ccdd6ac3b7cb`  |
| 3342   | Layout 2             | `ccdd6ac3b7cb`  |
| 3335   | Layout 2             | `ccdd6ac3b7cb`  |
| 3326   | Layout 2             | `ccdd6ac3b7cb`  |
| 3321   | Layout 2             | `ccdd6ac3b7cb`  |
| 3314   | Layout 2             | `ccdd6ac3b7cb`  |
| 3303   | Layout 2             | `ccdd6ac3b7cb`  |
| 3302   | Layout 2             | `ccdd6ac3b7cb`  |
| 3293   | Layout 2             | `ccdd6ac3b7cb`  |
| 3283   | Layout 2             | `ccdd6ac3b7cb`  |
| 3275   | Layout 2             | `ccdd6ac3b7cb`  |
| 3267   | Layout 2             | `ccdd6ac3b7cb`  |
| 3258   | Layout 2             | `ccdd6ac3b7cb`  |
| 3251   | Layout 2             | `ccdd6ac3b7cb`  |
| 3242   | Layout 2             | `ccdd6ac3b7cb`  |
| 3235   | Layout 2             | `ccdd6ac3b7cb`  |
| 3229   | Layout 2             | `ccdd6ac3b7cb`  |
| 3212   | Layout 2             | `ccdd6ac3b7cb`  |
| 3203   | Layout 2             | `ccdd6ac3b7cb`  |
| 3193   | Layout 2             | `ccdd6ac3b7cb`  |
| 3186   | Layout 2             | `ccdd6ac3b7cb`  |
| 3177   | Layout 2             | `ccdd6ac3b7cb`  |
| 3169   | Layout 2             | `ccdd6ac3b7cb`  |
| 3158   | Layout 2             | `ccdd6ac3b7cb`  |
| 3151   | Layout 2             | `ccdd6ac3b7cb`  |
| 3144   | Layout 2             | `ccdd6ac3b7cb`  |
| 3133   | Layout 2             | `ccdd6ac3b7cb`  |
| 3125   | Layout 2             | `ccdd6ac3b7cb`  |
| 3118   | Layout 2             | `ccdd6ac3b7cb`  |
| 3111   | Layout 2             | `ccdd6ac3b7cb`  |
| 3103   | Layout 2             | `ccdd6ac3b7cb`  |
| 3095   | Layout 2             | `ccdd6ac3b7cb`  |
| 3086   | Layout 2             | `ccdd6ac3b7cb`  |
| 3072   | Layout 2             | `ccdd6ac3b7cb`  |
| 3062   | Layout 2             | `ccdd6ac3b7cb`  |
| 3052   | Layout 2             | `ccdd6ac3b7cb`  |
| 3045   | Layout 2             | `ccdd6ac3b7cb`  |
| 3037   | Layout 2             | `ccdd6ac3b7cb`  |
| 3030   | Layout 2             | `ccdd6ac3b7cb`  |
| 3021   | Layout 2             | `ccdd6ac3b7cb`  |
| 3012   | Layout 2             | `ccdd6ac3b7cb`  |
| 3002   | Layout 2             | `ccdd6ac3b7cb`  |
| 2995   | Layout 2             | `ccdd6ac3b7cb`  |
| 2987   | Layout 2             | `ccdd6ac3b7cb`  |
| 2978   | Layout 2             | `ccdd6ac3b7cb`  |
| 2970   | Layout 2             | `ccdd6ac3b7cb`  |
| 2959   | Layout 2             | `ccdd6ac3b7cb`  |
| 2951   | Layout 2             | `ccdd6ac3b7cb`  |
| 2942   | Layout 2             | `ccdd6ac3b7cb`  |
| 2935   | Layout 2             | `ccdd6ac3b7cb`  |
| 2932   | Layout 2             | `ccdd6ac3b7cb`  |
| 2923   | Layout 2             | `ccdd6ac3b7cb`  |
| 2919   | Layout 2             | `ccdd6ac3b7cb`  |
| 2907   | Layout 2             | `ccdd6ac3b7cb`  |
| 2900   | Layout 2             | `ccdd6ac3b7cb`  |
| 2891   | Layout 2             | `ccdd6ac3b7cb`  |
| 2882   | Layout 2             | `ccdd6ac3b7cb`  |
| 2872   | Layout 2             | `ccdd6ac3b7cb`  |
| 2863   | Layout 2             | `ccdd6ac3b7cb`  |
| 2855   | Layout 2             | `ccdd6ac3b7cb`  |
| 2849   | Layout 2             | `ccdd6ac3b7cb`  |
| 2844   | Layout 2             | `ccdd6ac3b7cb`  |
| 2834   | Layout 2             | `ccdd6ac3b7cb`  |
| 2825   | Layout 2             | `ccdd6ac3b7cb`  |
| 2819   | Layout 2             | `ccdd6ac3b7cb`  |
| 2811   | Layout 2             | `ccdd6ac3b7cb`  |
| 2803   | Layout 2             | `ccdd6ac3b7cb`  |
| 2794   | Layout 2             | `ccdd6ac3b7cb`  |
| 2783   | Layout 2             | `ccdd6ac3b7cb`  |
| 2774   | Layout 2             | `ccdd6ac3b7cb`  |
| 2765   | Layout 2             | `ccdd6ac3b7cb`  |
| 2756   | Layout 2             | `ccdd6ac3b7cb`  |
| 2750   | Layout 2             | `ccdd6ac3b7cb`  |
| 2743   | Layout 2             | `ccdd6ac3b7cb`  |
| 2736   | Layout 2             | `ccdd6ac3b7cb`  |
| 2726   | Layout 2             | `ccdd6ac3b7cb`  |
| 2717   | Layout 2             | `ccdd6ac3b7cb`  |
| 2709   | Layout 2             | `ccdd6ac3b7cb`  |
| 2703   | Layout 2             | `ccdd6ac3b7cb`  |
| 2695   | Layout 2             | `ccdd6ac3b7cb`  |
| 2684   | Layout 2             | `ccdd6ac3b7cb`  |
| 2672   | Layout 2             | `ccdd6ac3b7cb`  |
| 2665   | Layout 2             | `ccdd6ac3b7cb`  |
| 2657   | Layout 2             | `ccdd6ac3b7cb`  |
| 2649   | Layout 2             | `ccdd6ac3b7cb`  |
| 2644   | Layout 2             | `ccdd6ac3b7cb`  |
| 2637   | Layout 2             | `ccdd6ac3b7cb`  |
| 2629   | Layout 2             | `ccdd6ac3b7cb`  |
| 2619   | Layout 2             | `ccdd6ac3b7cb`  |
| 2612   | Layout 2             | `ccdd6ac3b7cb`  |
| 2606   | Layout 2             | `ccdd6ac3b7cb`  |
| 2602   | Layout 2             | `ccdd6ac3b7cb`  |
| 2601   | Layout 2             | `ccdd6ac3b7cb`  |
| 2592   | Layout 2             | `ccdd6ac3b7cb`  |
| 2583   | Layout 2             | `ccdd6ac3b7cb`  |
| 2575   | Layout 2             | `ccdd6ac3b7cb`  |
| 2567   | Layout 2             | `ccdd6ac3b7cb`  |
| 2560   | Layout 2             | `ccdd6ac3b7cb`  |
| 2553   | Layout 2             | `ccdd6ac3b7cb`  |
| 2545   | Layout 2             | `ccdd6ac3b7cb`  |
| 2538   | Layout 2             | `ccdd6ac3b7cb`  |
| 2529   | Layout 2             | `ccdd6ac3b7cb`  |
| 2519   | Layout 2             | `ccdd6ac3b7cb`  |
| 2513   | Layout 2             | `ccdd6ac3b7cb`  |
| 2510   | Layout 2             | `ccdd6ac3b7cb`  |
| 2507   | Layout 2             | `ccdd6ac3b7cb`  |
| 2503   | Layout 2             | `ccdd6ac3b7cb`  |
| 2498   | Layout 2             | `ccdd6ac3b7cb`  |
| 2492   | Layout 2             | `ccdd6ac3b7cb`  |
| 2487   | Layout 2             | `ccdd6ac3b7cb`  |
| 2480   | Layout 2             | `ccdd6ac3b7cb`  |
| 2474   | Layout 2             | `ccdd6ac3b7cb`  |
| 2468   | Layout 2             | `ccdd6ac3b7cb`  |
| 2460   | Layout 2             | `ccdd6ac3b7cb`  |
| 2453   | Layout 2             | `ccdd6ac3b7cb`  |
| 2444   | Layout 2             | `ccdd6ac3b7cb`  |
| 2438   | Layout 2             | `ccdd6ac3b7cb`  |
| 2434   | Layout 2             | `ccdd6ac3b7cb`  |
| 2429   | Layout 2             | `ccdd6ac3b7cb`  |
| 2421   | Layout 2             | `ccdd6ac3b7cb`  |
| 2414   | Layout 2             | `ccdd6ac3b7cb`  |
| 2407   | Layout 2             | `ccdd6ac3b7cb`  |
| 2401   | Layout 2             | `ccdd6ac3b7cb`  |
| 2397   | Layout 2             | `ccdd6ac3b7cb`  |
| 2393   | Layout 2             | `ccdd6ac3b7cb`  |
| 2384   | Layout 2             | `ccdd6ac3b7cb`  |
| 2378   | Layout 2             | `ccdd6ac3b7cb`  |
| 2372   | Layout 2             | `ccdd6ac3b7cb`  |
| 2358   | Layout 2             | `ccdd6ac3b7cb`  |
| 2352   | Layout 2             | `ccdd6ac3b7cb`  |
| 2347   | Layout 2             | `ccdd6ac3b7cb`  |
| 2343   | Layout 2             | `ccdd6ac3b7cb`  |
| 2335   | Layout 2             | `ccdd6ac3b7cb`  |
| 2327   | Layout 2             | `ccdd6ac3b7cb`  |
| 2324   | Layout 2             | `ccdd6ac3b7cb`  |
| 2319   | Layout 2             | `ccdd6ac3b7cb`  |
| 2313   | Layout 2             | `ccdd6ac3b7cb`  |
| 2308   | Layout 2             | `ccdd6ac3b7cb`  |
| 2302   | Layout 2             | `ccdd6ac3b7cb`  |
| 2295   | Layout 2             | `ccdd6ac3b7cb`  |
| 2290   | Layout 2             | `ccdd6ac3b7cb`  |
| 2284   | Layout 2             | `ccdd6ac3b7cb`  |
| 2276   | Layout 2             | `ccdd6ac3b7cb`  |
| 2269   | Layout 2             | `ccdd6ac3b7cb`  |
| 2259   | Layout 2             | `ccdd6ac3b7cb`  |
| 2250   | Layout 2             | `ccdd6ac3b7cb`  |
| 2243   | Layout 2             | `ccdd6ac3b7cb`  |
| 2235   | Layout 2             | `ccdd6ac3b7cb`  |
| 2229   | Layout 2             | `ccdd6ac3b7cb`  |
| 2224   | Layout 2             | `ccdd6ac3b7cb`  |
| 2218   | Layout 2             | `ccdd6ac3b7cb`  |
| 2215   | Layout 2             | `ccdd6ac3b7cb`  |
| 2207   | Layout 2             | `ccdd6ac3b7cb`  |
| 2203   | Layout 2             | `ccdd6ac3b7cb`  |
| 2196   | Layout 2             | `ccdd6ac3b7cb`  |
| 2192   | Layout 2             | `ccdd6ac3b7cb`  |
| 2189   | Layout 2             | `ccdd6ac3b7cb`  |
| 2183   | Layout 2             | `ccdd6ac3b7cb`  |
| 2179   | Layout 2             | `ccdd6ac3b7cb`  |
| 2171   | Layout 2             | `ccdd6ac3b7cb`  |
| 2163   | Layout 2             | `ccdd6ac3b7cb`  |
| 2156   | Layout 2             | `ccdd6ac3b7cb`  |
| 2151   | Layout 2             | `ccdd6ac3b7cb`  |
| 2147   | Layout 2             | `ccdd6ac3b7cb`  |
| 2142   | Layout 2             | `ccdd6ac3b7cb`  |
| 2138   | Layout 2             | `ccdd6ac3b7cb`  |
| 2134   | Layout 2             | `ccdd6ac3b7cb`  |
| 2130   | Layout 2             | `ccdd6ac3b7cb`  |
| 2122   | Layout 2             | `ccdd6ac3b7cb`  |
| 2107   | Layout 2             | `ccdd6ac3b7cb`  |
| 2098   | Layout 2             | `ccdd6ac3b7cb`  |
| 2089   | Layout 2             | `ccdd6ac3b7cb`  |
| 2081   | Layout 2             | `ccdd6ac3b7cb`  |
| 2073   | Layout 2             | `ccdd6ac3b7cb`  |
| 2067   | Layout 2             | `ccdd6ac3b7cb`  |
| 2063   | Layout 2             | `ccdd6ac3b7cb`  |
| 2059   | Layout 2             | `ccdd6ac3b7cb`  |
| 2052   | Layout 2             | `ccdd6ac3b7cb`  |
| 2044   | Layout 2             | `ccdd6ac3b7cb`  |
| 2039   | Layout 2             | `ccdd6ac3b7cb`  |
| 2032   | Layout 2             | `ccdd6ac3b7cb`  |
| 2025   | Layout 2             | `ccdd6ac3b7cb`  |
| 2011   | Layout 2             | `ccdd6ac3b7cb`  |
| 2005   | Layout 2             | `ccdd6ac3b7cb`  |
| 2000   | Layout 2             | `ccdd6ac3b7cb`  |
| 1996   | Layout 2             | `ccdd6ac3b7cb`  |
| 1991   | Layout 2             | `ccdd6ac3b7cb`  |
| 1985   | Layout 2             | `ccdd6ac3b7cb`  |
| 1980   | Layout 2             | `ccdd6ac3b7cb`  |
| 1969   | Layout 2             | `ccdd6ac3b7cb`  |
| 1964   | Layout 2             | `ccdd6ac3b7cb`  |
| 1958   | Layout 2             | `ccdd6ac3b7cb`  |
| 1950   | Layout 2             | `ccdd6ac3b7cb`  |
| 1945   | Layout 2             | `ccdd6ac3b7cb`  |
| 1937   | Layout 2             | `ccdd6ac3b7cb`  |
| 1933   | Layout 2             | `ccdd6ac3b7cb`  |
| 1927   | Layout 2             | `ccdd6ac3b7cb`  |
| 1921   | Layout 2             | `ccdd6ac3b7cb`  |
| 1914   | No documented layout | `ccdd6ac3b7cb`  |
| 1908   | No documented layout | `ccdd6ac3b7cb`  |
| 1897   | No documented layout | `ccdd6ac3b7cb`  |
| 1892   | No documented layout | `ccdd6ac3b7cb`  |
| 1886   | No documented layout | `ccdd6ac3b7cb`  |
| 1881   | No documented layout | `ccdd6ac3b7cb`  |
| 1871   | Layout 1             | `ccdd6ac3b7cb`  |
| 1866   | Layout 1             | `ccdd6ac3b7cb`  |
| 1862   | Layout 1             | `ccdd6ac3b7cb`  |
| 1854   | Layout 1             | `ccdd6ac3b7cb`  |
| 1846   | Layout 1             | `ccdd6ac3b7cb`  |
| 1838   | Layout 1             | `ccdd6ac3b7cb`  |
| 1832   | Layout 1             | `ccdd6ac3b7cb`  |
| 1826   | Layout 1             | `ccdd6ac3b7cb`  |
| 1822   | Layout 1             | `ccdd6ac3b7cb`  |
| 1818   | Layout 1             | `ccdd6ac3b7cb`  |
| 1804   | Layout 1             | `ccdd6ac3b7cb`  |
| 1794   | Layout 1             | `ccdd6ac3b7cb`  |
| 1790   | Layout 1             | `ccdd6ac3b7cb`  |
| 1784   | Layout 1             | `ccdd6ac3b7cb`  |
| 1774   | Layout 1             | `ccdd6ac3b7cb`  |
| 1771   | Layout 1             | `ccdd6ac3b7cb`  |
| 1762   | Layout 1             | `ccdd6ac3b7cb`  |
| 1759   | Layout 1             | `ccdd6ac3b7cb`  |
| 1754   | Layout 1             | `ccdd6ac3b7cb`  |
| 1749   | Layout 1             | `ccdd6ac3b7cb`  |
| 1743   | Layout 1             | `ccdd6ac3b7cb`  |
| 1737   | Layout 1             | `ccdd6ac3b7cb`  |
| 1731   | Layout 1             | `ccdd6ac3b7cb`  |
| 1725   | Layout 1             | `ccdd6ac3b7cb`  |
| 1717   | Layout 1             | `ccdd6ac3b7cb`  |
| 1710   | Layout 1             | `ccdd6ac3b7cb`  |
| 1704   | Layout 1             | `ccdd6ac3b7cb`  |
| 1698   | Layout 1             | `ccdd6ac3b7cb`  |
| 1690   | Layout 1             | `ccdd6ac3b7cb`  |
| 1685   | Layout 1             | `ccdd6ac3b7cb`  |
| 1680   | Layout 1             | `ccdd6ac3b7cb`  |
| 1674   | Layout 1             | `ccdd6ac3b7cb`  |
| 1668   | Layout 1             | `ccdd6ac3b7cb`  |
| 1659   | Layout 1             | `ccdd6ac3b7cb`  |
| 1649   | Layout 1             | `ccdd6ac3b7cb`  |
| 1642   | Layout 1             | `ccdd6ac3b7cb`  |
| 1636   | Layout 1             | `ccdd6ac3b7cb`  |
| 1628   | Layout 1             | `ccdd6ac3b7cb`  |
| 1622   | Layout 1             | `ccdd6ac3b7cb`  |
| 1614   | Layout 1             | `ccdd6ac3b7cb`  |
| 1608   | Layout 1             | `ccdd6ac3b7cb`  |
| 1602   | Layout 1             | `ccdd6ac3b7cb`  |
| 1598   | Layout 1             | `ccdd6ac3b7cb`  |
| 1594   | Layout 1             | `ccdd6ac3b7cb`  |
| 1590   | Layout 1             | `ccdd6ac3b7cb`  |
| 1587   | Layout 1             | `ccdd6ac3b7cb`  |
| 1584   | Layout 1             | `ccdd6ac3b7cb`  |
| 1579   | Layout 1             | `ccdd6ac3b7cb`  |
| 1572   | Layout 1             | `ccdd6ac3b7cb`  |
| 1565   | Layout 1             | `ccdd6ac3b7cb`  |
| 1559   | Layout 1             | `ccdd6ac3b7cb`  |
| 1554   | Layout 1             | `ccdd6ac3b7cb`  |
| 1547   | Layout 1             | `ccdd6ac3b7cb`  |
| 1537   | Layout 1             | `ccdd6ac3b7cb`  |
| 1529   | Layout 1             | `ccdd6ac3b7cb`  |
| 1524   | Layout 1             | `ccdd6ac3b7cb`  |
| 1519   | Layout 1             | `ccdd6ac3b7cb`  |
| 1509   | Layout 1             | `ccdd6ac3b7cb`  |
| 1506   | Layout 1             | `ccdd6ac3b7cb`  |
| 1504   | Layout 1             | `ccdd6ac3b7cb`  |
| 1500   | Layout 1             | `ccdd6ac3b7cb`  |
| 1493   | Layout 1             | `ccdd6ac3b7cb`  |
| 1489   | Layout 1             | `ccdd6ac3b7cb`  |
| 1485   | Layout 1             | `ccdd6ac3b7cb`  |
| 1481   | Layout 1             | `ccdd6ac3b7cb`  |
| 1474   | Layout 1             | `ccdd6ac3b7cb`  |
| 1466   | Layout 1             | `ccdd6ac3b7cb`  |
| 1462   | Layout 1             | `ccdd6ac3b7cb`  |
| 1459   | Layout 1             | `ccdd6ac3b7cb`  |
| 1453   | Layout 1             | `ccdd6ac3b7cb`  |
| 1450   | Layout 1             | `ccdd6ac3b7cb`  |
| 1445   | Layout 1             | `ccdd6ac3b7cb`  |
| 1439   | Layout 1             | `ccdd6ac3b7cb`  |
| 1433   | Layout 1             | `ccdd6ac3b7cb`  |
| 1430   | Layout 1             | `ccdd6ac3b7cb`  |
| 1426   | Layout 1             | `ccdd6ac3b7cb`  |
| 1421   | Layout 1             | `ccdd6ac3b7cb`  |
| 1417   | Layout 1             | `ccdd6ac3b7cb`  |
| 1416   | Layout 1             | `ccdd6ac3b7cb`  |
| 1409   | Layout 1             | `ccdd6ac3b7cb`  |
| 1405   | Layout 1             | `ccdd6ac3b7cb`  |
| 1401   | Layout 1             | `ccdd6ac3b7cb`  |
| 1396   | Layout 1             | `ccdd6ac3b7cb`  |
| 1391   | Layout 1             | `ccdd6ac3b7cb`  |
| 1390   | Layout 1             | `ccdd6ac3b7cb`  |
| 1386   | Layout 1             | `ccdd6ac3b7cb`  |
| 1381   | Layout 1             | `ccdd6ac3b7cb`  |
| 1379   | Layout 1             | `ccdd6ac3b7cb`  |
| 1372   | Layout 1             | `ccdd6ac3b7cb`  |
| 1366   | Layout 1             | `ccdd6ac3b7cb`  |
| 1364   | Layout 1             | `ccdd6ac3b7cb`  |
| 1363   | Layout 1             | `ccdd6ac3b7cb`  |
| 1360   | Layout 1             | `ccdd6ac3b7cb`  |
| 1358   | Layout 1             | `ccdd6ac3b7cb`  |
| 1355   | Layout 1             | `ccdd6ac3b7cb`  |
| 1351   | Layout 1             | `ccdd6ac3b7cb`  |
| 1348   | Layout 1             | `ccdd6ac3b7cb`  |
| 1346   | Layout 1             | `ccdd6ac3b7cb`  |
| 1341   | Layout 1             | `ccdd6ac3b7cb`  |
| 1340   | Layout 1             | `ccdd6ac3b7cb`  |
| 1338   | Layout 1             | `ccdd6ac3b7cb`  |
| 1335   | Layout 1             | `ccdd6ac3b7cb`  |
| 1333   | Layout 1             | `ccdd6ac3b7cb`  |
| 1329   | Layout 1             | `ccdd6ac3b7cb`  |
| 1327   | Layout 1             | `ccdd6ac3b7cb`  |
| 1324   | Layout 1             | `ccdd6ac3b7cb`  |
| 1321   | Layout 1             | `ccdd6ac3b7cb`  |
| 1319   | Layout 1             | `ccdd6ac3b7cb`  |
| 1318   | Layout 1             | `ccdd6ac3b7cb`  |
| 1316   | Layout 1             | `ccdd6ac3b7cb`  |
| 1313   | Layout 1             | `ccdd6ac3b7cb`  |
| 1311   | Layout 1             | `ccdd6ac3b7cb`  |
| 1309   | Layout 1             | `ccdd6ac3b7cb`  |
| 1304   | Layout 1             | `ccdd6ac3b7cb`  |
| 1292   | Layout 1             | `ccdd6ac3b7cb`  |
| 1286   | Layout 1             | `ccdd6ac3b7cb`  |
| 1280   | Layout 1             | `ccdd6ac3b7cb`  |
| 1276   | Layout 1             | `ccdd6ac3b7cb`  |
| 1267   | Layout 1             | `ccdd6ac3b7cb`  |
| 1261   | Layout 1             | `ccdd6ac3b7cb`  |
| 1256   | Layout 1             | `ccdd6ac3b7cb`  |
| 1250   | Layout 1             | `ccdd6ac3b7cb`  |
| 1246   | Layout 1             | `ccdd6ac3b7cb`  |
| 1239   | Layout 1             | `ccdd6ac3b7cb`  |
| 1230   | Layout 1             | `ccdd6ac3b7cb`  |
| 1226   | Layout 1             | `ccdd6ac3b7cb`  |
| 1220   | Layout 1             | `ccdd6ac3b7cb`  |
| 1217   | Layout 1             | `ccdd6ac3b7cb`  |
| 1211   | Layout 1             | `ccdd6ac3b7cb`  |
| 1210   | Layout 1             | `ccdd6ac3b7cb`  |
| 1208   | Layout 1             | `ccdd6ac3b7cb`  |
| 1203   | Layout 1             | `ccdd6ac3b7cb`  |
| 1197   | Layout 1             | `ccdd6ac3b7cb`  |
| 1194   | Layout 1             | `ccdd6ac3b7cb`  |
| 1192   | Layout 1             | `ccdd6ac3b7cb`  |
| 1187   | Layout 1             | `ccdd6ac3b7cb`  |
| 1183   | Layout 1             | `ccdd6ac3b7cb`  |
| 1177   | Layout 1             | `ccdd6ac3b7cb`  |
| 1173   | Layout 1             | `ccdd6ac3b7cb`  |
| 1167   | Layout 1             | `ccdd6ac3b7cb`  |
| 1164   | Layout 1             | `ccdd6ac3b7cb`  |
| 1156   | Layout 1             | `ccdd6ac3b7cb`  |
| 1149   | Layout 1             | `ccdd6ac3b7cb`  |
| 1144   | Layout 1             | `ccdd6ac3b7cb`  |
| 1137   | Layout 1             | `ccdd6ac3b7cb`  |
| 1132   | Layout 1             | `ccdd6ac3b7cb`  |
| 1127   | Layout 1             | `ccdd6ac3b7cb`  |
| 1122   | Layout 1             | `ccdd6ac3b7cb`  |
| 1118   | Layout 1             | `ccdd6ac3b7cb`  |
| 1114   | Layout 1             | `ccdd6ac3b7cb`  |
| 1109   | Layout 1             | `ccdd6ac3b7cb`  |
| 1102   | No file              | `ccdd6ac3b7cb`  |
| 1096   | No file              | `ccdd6ac3b7cb`  |
| 1088   | No file              | `ccdd6ac3b7cb`  |
| 1081   | No file              | `ccdd6ac3b7cb`  |
| 1076   | No file              | `ccdd6ac3b7cb`  |
| 1069   | No file              | `ccdd6ac3b7cb`  |
| 1064   | No file              | `ccdd6ac3b7cb`  |
| 1058   | No file              | `ccdd6ac3b7cb`  |
| 1051   | No file              | `ccdd6ac3b7cb`  |
| 1044   | No file              | `ccdd6ac3b7cb`  |
| 1036   | No file              | `ccdd6ac3b7cb`  |
| 1026   | No file              | `ccdd6ac3b7cb`  |
| 1016   | No file              | `ccdd6ac3b7cb`  |
| 1009   | No file              | `ccdd6ac3b7cb`  |
| 1005   | No file              | `ccdd6ac3b7cb`  |
| 1000   | No file              | `ccdd6ac3b7cb`  |
| 998    | No file              | `ccdd6ac3b7cb`  |
| 990    | No file              | `ccdd6ac3b7cb`  |
| 979    | No file              | `ccdd6ac3b7cb`  |
| 972    | No file              | `ccdd6ac3b7cb`  |
| 963    | No file              | `ccdd6ac3b7cb`  |
| 955    | No file              | `ccdd6ac3b7cb`  |
| 946    | No file              | `ccdd6ac3b7cb`  |
| 938    | No file              | `ccdd6ac3b7cb`  |
| 927    | No file              | `ccdd6ac3b7cb`  |
| 911    | No file              | `ccdd6ac3b7cb`  |
| 904    | No file              | `ccdd6ac3b7cb`  |
| 899    | No file              | `ccdd6ac3b7cb`  |
| 894    | No file              | `ccdd6ac3b7cb`  |
| 885    | No file              | `ccdd6ac3b7cb`  |
| 879    | No file              | `ccdd6ac3b7cb`  |
| 872    | No file              | `ccdd6ac3b7cb`  |
| 864    | No file              | `ccdd6ac3b7cb`  |
| 855    | No file              | `ccdd6ac3b7cb`  |
| 853    | No file              | `ccdd6ac3b7cb`  |
| 845    | No file              | `ccdd6ac3b7cb`  |
| 837    | No file              | `ccdd6ac3b7cb`  |
| 829    | Layout 1             | `ccdd6ac3b7cb`  |
| 822    | Layout 1             | `ccdd6ac3b7cb`  |
| 814    | Layout 1             | `ccdd6ac3b7cb`  |
| 805    | Layout 1             | `ccdd6ac3b7cb`  |
| 794    | No documented layout | `ccdd6ac3b7cb`  |
| 787    | No documented layout | `ccdd6ac3b7cb`  |
| 780    | No documented layout | `ccdd6ac3b7cb`  |
| 771    | No documented layout | `ccdd6ac3b7cb`  |
| 760    | No documented layout | `ccdd6ac3b7cb`  |
| 748    | No documented layout | `ccdd6ac3b7cb`  |
| 741    | No documented layout | `ccdd6ac3b7cb`  |
| 736    | No documented layout | `ccdd6ac3b7cb`  |
| 731    | No documented layout | `ccdd6ac3b7cb`  |
| 723    | No documented layout | `ccdd6ac3b7cb`  |
| 711    | No documented layout | `ccdd6ac3b7cb`  |
| 707    | No documented layout | `ccdd6ac3b7cb`  |
| 697    | No documented layout | `ccdd6ac3b7cb`  |
| 689    | No documented layout | `ccdd6ac3b7cb`  |
| 683    | No documented layout | `ccdd6ac3b7cb`  |
| 678    | No documented layout | `ccdd6ac3b7cb`  |
| 670    | No documented layout | `ccdd6ac3b7cb`  |
| 661    | No documented layout | `ccdd6ac3b7cb`  |
| 656    | No documented layout | `ccdd6ac3b7cb`  |
| 652    | No file              | `ccdd6ac3b7cb`  |
| 643    | No file              | `ccdd6ac3b7cb`  |
| 637    | No file              | `ccdd6ac3b7cb`  |
| 630    | No file              | `ccdd6ac3b7cb`  |
| 627    | No file              | `ccdd6ac3b7cb`  |
| 621    | No file              | `ccdd6ac3b7cb`  |
| 617    | No file              | `ccdd6ac3b7cb`  |
| 615    | No file              | `ccdd6ac3b7cb`  |
| 606    | No file              | `ccdd6ac3b7cb`  |
| 599    | No file              | `ccdd6ac3b7cb`  |
| 592    | No file              | `ccdd6ac3b7cb`  |
| 586    | No file              | `ccdd6ac3b7cb`  |
| 577    | No file              | `ccdd6ac3b7cb`  |
| 569    | No file              | `ccdd6ac3b7cb`  |
| 561    | No file              | `ccdd6ac3b7cb`  |
| 554    | No file              | `ccdd6ac3b7cb`  |
| 542    | No file              | `ccdd6ac3b7cb`  |
| 532    | No file              | `ccdd6ac3b7cb`  |
| 531    | No file              | `ccdd6ac3b7cb`  |
| 526    | No file              | `ccdd6ac3b7cb`  |
| 521    | No file              | `ccdd6ac3b7cb`  |
| 517    | No file              | `ccdd6ac3b7cb`  |
| 510    | No file              | `ccdd6ac3b7cb`  |
| 508    | No file              | `ccdd6ac3b7cb`  |
| 504    | No file              | `ccdd6ac3b7cb`  |
| 497    | No file              | `ccdd6ac3b7cb`  |
| 491    | No file              | `ccdd6ac3b7cb`  |
| 485    | No file              | `ccdd6ac3b7cb`  |
| 478    | No file              | `ccdd6ac3b7cb`  |
| 472    | No file              | `ccdd6ac3b7cb`  |
| 466    | No file              | `ccdd6ac3b7cb`  |
| 457    | No file              | `ccdd6ac3b7cb`  |
| 452    | No file              | `ccdd6ac3b7cb`  |
| 449    | No file              | `ccdd6ac3b7cb`  |
| 435    | No file              | `ccdd6ac3b7cb`  |

<!-- versions:end -->

## Companion Files

None. `fairyequipskill.bss` is a standalone catalog with no offset index.

| File                  | Required | Role                                             |
| --------------------- | -------- | ------------------------------------------------ |
| `languagedata_en.loc` | Optional | Skill names (`id4=0`) and descriptions (`id4=1`) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

Total file size: 3636 bytes = 4 (magic) + 420 (catalog) + 3200 (reserved block) + 12 (trailer).

Records begin immediately at `+0x04`. There is **no** record count field; the catalog is terminated by the first record whose `equip_skill_id` is `200`.

| Offset              | Type                                      | Field         | Notes                                                       |
| ------------------- | ----------------------------------------- | ------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]                                   | magic         | `PABR` (ASCII)                                              |
| `+0x04`             | Skill Record[while equip_skill_id != 200] | skill_records | 35 x 12-byte skill records, `+0x004` to `+0x1A8`            |
| `skill_records+0x00` | Slot[..data_end]                         | slots         | Reserved block: 200 x 16-byte null placeholders, `+0x1A8` to `+0xE28` |
| `EOF-0x0C` | u32 | string_count | `0`: the PABR string table, here with no strings; `data_end` points at it |
| `EOF-0x08` | u32 | data_end | `0x0E28` (3624) = `file_size - 12`, the offset of `string_count` |
| `EOF-0x04` | u32 | zero | Always `0` |

`petequipskill.bss` carries the identical trailer (`data_end = 0x0EB0 = file_size - 12`), so this is a shared PABR convention rather than a fairy-specific field.

### Skill Record (12 bytes)

| Offset  | Type | Field          | Notes                                                  |
| ------- | ---- | -------------- | ------------------------------------------------------ |
| `+0x00` | u32  | equip_skill_id | Sequential record key, `0` to `34`; `200` marks the end |
| `+0x04` | u32  | skill_type     | Skill group, `1` to `8` (see Skill Types)              |
| `+0x08` | u16  | skill_level    | Skill level of the `gc::SkillKey`; always `1`          |
| `+0x0A` | u16  | skill_no       | Skill number (`SkillNo`); keys the name, description and icon |

Earlier versions of this doc called `skill_level` `tier`.

### Slot (16 bytes)

Two hundred unused catalog slots. Every record is `[u32 200][u32 0][u32 0][u32 0]`, where `200` is the null-entry sentinel. Skip these when parsing.

The stride here is 16 bytes, not the 12 used by live records; it matches the wider Section 2 record shape in `petequipskill.bss`, whose extended catalog is fully populated. In `fairyequipskill.bss` that extended section is entirely null.

| Offset  | Type      | Field          | Notes                                                                                                   |
| ------- | --------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | u32       | equip_skill_id | Always `200`, the null-entry sentinel                                                                   |
| `+0x04` | u32       | skill_type     | Always `0`                                                                                              |
| `+0x08` | u16       | skill_level    | Always `0`                                                                                              |
| `+0x0A` | u16       | skill_no       | Always `0`                                                                                              |
| `+0x0C` | u32       | unknown_0c     | Always `0`; the `petequipskill.bss` Slot's `unknown_0c`, and no extra u32 follows                       |


## Field Names

The client 1784 private server loads `Fairy_EquipSkill_Table` into one 24-byte entry per
record: `Index` (`equip_skill_id`) at `+0x00`, `GroupNo` (`skill_type`) at
`+0x04`, a runtime skill pointer at `+0x08` and a `gc::SkillKey` at `+0x10`.
The loader (VA `0x1409c8f13` to `0x1409c8f19`) writes the key as `(SkillNo << 16) | 1`, so its low u16
is the skill level (always `1`) and its high u16 the sheet's `SkillNo`. The
2016 client's `gc::SkillKey` is one `unsigned int _value` whose `getLevel()`
reads the low u16 and `getSkillNo()` the high u16, which places
`skill_level` at `+0x08` and `skill_no` at `+0x0A`. The server has no reader
for this file; the record is that entry in loader order without the pointer
and the padding. After loading, it looks up every key in the skill table and
logs "펫 착용 스킬에 알수 없는 스킬(%#)의 데이터가 있습니다!" ("pet equip
skill has data for an unknown skill (%#)!") for a missing one.
`petequipskill.bss` and `fairyequipskill.bss` share the entry, the loader
shape and the per-entry checks, which is why the fairy check logs the pet message.

The client 1784 build's own file matches `Fairy_EquipSkill_Table` on all
30 records (Index, GroupNo, level `1`, SkillNo); client 3474 has level `1`
on all 35. The null slots are the same struct with every field `0`.

LOC type 10 keys the skill name by `skill_no`
([`languagedata_loc.md`](languagedata_loc.md)). Earlier versions of this doc
read `+0x08` as two u8 fields (`unknown_08`, `unknown_09`) and named `+0x0A`
`loc_id`.

## Layout 1

On client 1784 the null-entry sentinel was `100`, not `200`, and every
Slot was 12 bytes, the size of a Skill Record. The File Layout and the Slot
differ from Layout 2; the Skill Record is the same. On client 1784 the file
holds 30 Skill Records and 100 Slots.

### File Layout

| Offset               | Type                                      | Field         | Notes                                                          |
| -------------------- | ----------------------------------------- | ------------- | -------------------------------------------------------------- |
| `+0x00`              | char[4]                                   | magic         | `PABR` (ASCII)                                                 |
| `+0x04`              | Skill Record[while equip_skill_id != 100] | skill_records | Ends at the first record whose `equip_skill_id` is `100`       |
| `skill_records+0x00` | Slot[..data_end]                          | slots         | 12-byte null placeholders up to `data_end`                     |
| `EOF-0x0C`           | u32                                       | string_count  | `0`: the PABR string table, here with no strings               |
| `EOF-0x08`           | u32                                       | data_end      | `file_size - 12`, the offset of `string_count`                 |
| `EOF-0x04`           | u32                                       | zero          | Always `0`                                                     |

### Slot (12 bytes)

| Offset  | Type     | Field          | Notes                                 |
| ------- | -------- | -------------- | ------------------------------------- |
| `+0x00` | u32      | equip_skill_id | Always `100`, the null-entry sentinel |
| `+0x04` | u32      | skill_type     | Always `0`                            |
| `+0x08` | u16      | skill_level    | Always `0`                            |
| `+0x0A` | u16      | skill_no       | Always `0`                            |
