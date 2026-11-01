# `classskilllist.bss` Format

## Purpose

The skill list of each playable class for the Skill Guide widget: one
row per class type with the skill numbers whose key commands it can show.
The server of client 1784 loads the same data in
`GameCommonParameterLoaderFromExcel::loadMain(LoadClassSkillCommandList)`,
which logs `ClassType(%#):ClassSkillCommandList`, right before
`LoadSkillCommandList`. Every skill number in the file is a key of
`skillcommand.dbss` (517 of 517 distinct numbers, client 3473), the table of
skill command records.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                 | Bytes | Records      | Row bytes               |
| ------ | ------------- | -------------------- | ----- | ------------ | ----------------------- |
| 1      | 805 and later | `classskilllist.bss` | 1,372 | 32 Class Row | 25 to 53, 42 on average |

| Layout | File                 | Known            | Unknown    |
| ------ | -------------------- | ---------------- | ---------- |
| 1      | `classskilllist.bss` | 1,372 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `0478a63d3b1b`  |
| 3482   | Layout 1             | `0478a63d3b1b`  |
| 3474   | Layout 1             | `0478a63d3b1b`  |
| 3473   | Layout 1             | `0478a63d3b1b`  |
| 3464   | Layout 1             | `0478a63d3b1b`  |
| 3458   | Layout 1             | `0478a63d3b1b`  |
| 3454   | Layout 1             | `0478a63d3b1b`  |
| 3444   | Layout 1             | `0478a63d3b1b`  |
| 3435   | Layout 1             | `0478a63d3b1b`  |
| 3426   | Layout 1             | `0478a63d3b1b`  |
| 3418   | Layout 1             | `0478a63d3b1b`  |
| 3412   | Layout 1             | `0478a63d3b1b`  |
| 3402   | Layout 1             | `0478a63d3b1b`  |
| 3396   | Layout 1             | `0478a63d3b1b`  |
| 3387   | Layout 1             | `0478a63d3b1b`  |
| 3381   | Layout 1             | `0478a63d3b1b`  |
| 3373   | Layout 1             | `0478a63d3b1b`  |
| 3364   | Layout 1             | `0478a63d3b1b`  |
| 3356   | Layout 1             | `0478a63d3b1b`  |
| 3349   | Layout 1             | `0478a63d3b1b`  |
| 3342   | Layout 1             | `0478a63d3b1b`  |
| 3335   | Layout 1             | `0478a63d3b1b`  |
| 3326   | Layout 1             | `0478a63d3b1b`  |
| 3321   | Layout 1             | `0478a63d3b1b`  |
| 3314   | Layout 1             | `0478a63d3b1b`  |
| 3303   | Layout 1             | `0478a63d3b1b`  |
| 3302   | Layout 1             | `0478a63d3b1b`  |
| 3293   | Layout 1             | `0478a63d3b1b`  |
| 3283   | Layout 1             | `0478a63d3b1b`  |
| 3275   | Layout 1             | `0478a63d3b1b`  |
| 3267   | Layout 1             | `0478a63d3b1b`  |
| 3258   | Layout 1             | `0478a63d3b1b`  |
| 3251   | Layout 1             | `0478a63d3b1b`  |
| 3242   | Layout 1             | `0478a63d3b1b`  |
| 3235   | Layout 1             | `0478a63d3b1b`  |
| 3229   | Layout 1             | `0478a63d3b1b`  |
| 3212   | Layout 1             | `0478a63d3b1b`  |
| 3203   | Layout 1             | `0478a63d3b1b`  |
| 3193   | Layout 1             | `0478a63d3b1b`  |
| 3186   | Layout 1             | `0478a63d3b1b`  |
| 3177   | Layout 1             | `0478a63d3b1b`  |
| 3169   | Layout 1             | `0478a63d3b1b`  |
| 3158   | Layout 1             | `0478a63d3b1b`  |
| 3151   | Layout 1             | `0478a63d3b1b`  |
| 3144   | Layout 1             | `0478a63d3b1b`  |
| 3133   | Layout 1             | `0478a63d3b1b`  |
| 3125   | Layout 1             | `0478a63d3b1b`  |
| 3118   | Layout 1             | `0478a63d3b1b`  |
| 3111   | Layout 1             | `0478a63d3b1b`  |
| 3103   | Layout 1             | `0478a63d3b1b`  |
| 3095   | Layout 1             | `0478a63d3b1b`  |
| 3086   | Layout 1             | `0478a63d3b1b`  |
| 3072   | Layout 1             | `0478a63d3b1b`  |
| 3062   | Layout 1             | `0478a63d3b1b`  |
| 3052   | Layout 1             | `0478a63d3b1b`  |
| 3045   | Layout 1             | `0478a63d3b1b`  |
| 3037   | Layout 1             | `0478a63d3b1b`  |
| 3030   | Layout 1             | `0478a63d3b1b`  |
| 3021   | Layout 1             | `0478a63d3b1b`  |
| 3012   | Layout 1             | `0478a63d3b1b`  |
| 3002   | Layout 1             | `0478a63d3b1b`  |
| 2995   | Layout 1             | `0478a63d3b1b`  |
| 2987   | Layout 1             | `0478a63d3b1b`  |
| 2978   | Layout 1             | `0478a63d3b1b`  |
| 2970   | Layout 1             | `0478a63d3b1b`  |
| 2959   | Layout 1             | `0478a63d3b1b`  |
| 2951   | Layout 1             | `0478a63d3b1b`  |
| 2942   | Layout 1             | `0478a63d3b1b`  |
| 2935   | Layout 1             | `0478a63d3b1b`  |
| 2932   | Layout 1             | `0478a63d3b1b`  |
| 2923   | Layout 1             | `0478a63d3b1b`  |
| 2919   | Layout 1             | `0478a63d3b1b`  |
| 2907   | Layout 1             | `0478a63d3b1b`  |
| 2900   | Layout 1             | `0478a63d3b1b`  |
| 2891   | Layout 1             | `0478a63d3b1b`  |
| 2882   | Layout 1             | `0478a63d3b1b`  |
| 2872   | Layout 1             | `0478a63d3b1b`  |
| 2863   | Layout 1             | `0478a63d3b1b`  |
| 2855   | Layout 1             | `0478a63d3b1b`  |
| 2849   | Layout 1             | `0478a63d3b1b`  |
| 2844   | Layout 1             | `0478a63d3b1b`  |
| 2834   | Layout 1             | `0478a63d3b1b`  |
| 2825   | Layout 1             | `0478a63d3b1b`  |
| 2819   | Layout 1             | `0478a63d3b1b`  |
| 2811   | Layout 1             | `0478a63d3b1b`  |
| 2803   | Layout 1             | `0478a63d3b1b`  |
| 2794   | Layout 1             | `0478a63d3b1b`  |
| 2783   | Layout 1             | `0478a63d3b1b`  |
| 2774   | Layout 1             | `0478a63d3b1b`  |
| 2765   | Layout 1             | `0478a63d3b1b`  |
| 2756   | Layout 1             | `0478a63d3b1b`  |
| 2750   | Layout 1             | `0478a63d3b1b`  |
| 2743   | Layout 1             | `0478a63d3b1b`  |
| 2736   | Layout 1             | `0478a63d3b1b`  |
| 2726   | Layout 1             | `0478a63d3b1b`  |
| 2717   | Layout 1             | `0478a63d3b1b`  |
| 2709   | Layout 1             | `0478a63d3b1b`  |
| 2703   | Layout 1             | `0478a63d3b1b`  |
| 2695   | Layout 1             | `0478a63d3b1b`  |
| 2684   | Layout 1             | `0478a63d3b1b`  |
| 2672   | Layout 1             | `0478a63d3b1b`  |
| 2665   | Layout 1             | `0478a63d3b1b`  |
| 2657   | Layout 1             | `0478a63d3b1b`  |
| 2649   | Layout 1             | `0478a63d3b1b`  |
| 2644   | Layout 1             | `0478a63d3b1b`  |
| 2637   | Layout 1             | `0478a63d3b1b`  |
| 2629   | Layout 1             | `0478a63d3b1b`  |
| 2619   | Layout 1             | `0478a63d3b1b`  |
| 2612   | Layout 1             | `0478a63d3b1b`  |
| 2606   | Layout 1             | `0478a63d3b1b`  |
| 2602   | Layout 1             | `0478a63d3b1b`  |
| 2601   | Layout 1             | `0478a63d3b1b`  |
| 2592   | Layout 1             | `0478a63d3b1b`  |
| 2583   | Layout 1             | `0478a63d3b1b`  |
| 2575   | Layout 1             | `0478a63d3b1b`  |
| 2567   | Layout 1             | `0478a63d3b1b`  |
| 2560   | Layout 1             | `0478a63d3b1b`  |
| 2553   | Layout 1             | `0478a63d3b1b`  |
| 2545   | Layout 1             | `0478a63d3b1b`  |
| 2538   | Layout 1             | `0478a63d3b1b`  |
| 2529   | Layout 1             | `0478a63d3b1b`  |
| 2519   | Layout 1             | `0478a63d3b1b`  |
| 2513   | Layout 1             | `0478a63d3b1b`  |
| 2510   | Layout 1             | `0478a63d3b1b`  |
| 2507   | Layout 1             | `0478a63d3b1b`  |
| 2503   | Layout 1             | `0478a63d3b1b`  |
| 2498   | Layout 1             | `0478a63d3b1b`  |
| 2492   | Layout 1             | `0478a63d3b1b`  |
| 2487   | Layout 1             | `0478a63d3b1b`  |
| 2480   | Layout 1             | `0478a63d3b1b`  |
| 2474   | Layout 1             | `0478a63d3b1b`  |
| 2468   | Layout 1             | `0478a63d3b1b`  |
| 2460   | Layout 1             | `0478a63d3b1b`  |
| 2453   | Layout 1             | `0478a63d3b1b`  |
| 2444   | Layout 1             | `0478a63d3b1b`  |
| 2438   | Layout 1             | `0478a63d3b1b`  |
| 2434   | Layout 1             | `0478a63d3b1b`  |
| 2429   | Layout 1             | `0478a63d3b1b`  |
| 2421   | Layout 1             | `0478a63d3b1b`  |
| 2414   | Layout 1             | `0478a63d3b1b`  |
| 2407   | Layout 1             | `0478a63d3b1b`  |
| 2401   | Layout 1             | `0478a63d3b1b`  |
| 2397   | Layout 1             | `0478a63d3b1b`  |
| 2393   | Layout 1             | `0478a63d3b1b`  |
| 2384   | Layout 1             | `0478a63d3b1b`  |
| 2378   | Layout 1             | `0478a63d3b1b`  |
| 2372   | Layout 1             | `0478a63d3b1b`  |
| 2358   | Layout 1             | `0478a63d3b1b`  |
| 2352   | Layout 1             | `0478a63d3b1b`  |
| 2347   | Layout 1             | `0478a63d3b1b`  |
| 2343   | Layout 1             | `0478a63d3b1b`  |
| 2335   | Layout 1             | `0478a63d3b1b`  |
| 2327   | Layout 1             | `0478a63d3b1b`  |
| 2324   | Layout 1             | `0478a63d3b1b`  |
| 2319   | Layout 1             | `0478a63d3b1b`  |
| 2313   | Layout 1             | `0478a63d3b1b`  |
| 2308   | Layout 1             | `0478a63d3b1b`  |
| 2302   | Layout 1             | `0478a63d3b1b`  |
| 2295   | Layout 1             | `0478a63d3b1b`  |
| 2290   | Layout 1             | `0478a63d3b1b`  |
| 2284   | Layout 1             | `0478a63d3b1b`  |
| 2276   | Layout 1             | `0478a63d3b1b`  |
| 2269   | Layout 1             | `0478a63d3b1b`  |
| 2259   | Layout 1             | `0478a63d3b1b`  |
| 2250   | Layout 1             | `0478a63d3b1b`  |
| 2243   | Layout 1             | `0478a63d3b1b`  |
| 2235   | Layout 1             | `0478a63d3b1b`  |
| 2229   | Layout 1             | `0478a63d3b1b`  |
| 2224   | Layout 1             | `0478a63d3b1b`  |
| 2218   | Layout 1             | `0478a63d3b1b`  |
| 2215   | Layout 1             | `0478a63d3b1b`  |
| 2207   | Layout 1             | `0478a63d3b1b`  |
| 2203   | Layout 1             | `0478a63d3b1b`  |
| 2196   | Layout 1             | `0478a63d3b1b`  |
| 2192   | Layout 1             | `0478a63d3b1b`  |
| 2189   | Layout 1             | `0478a63d3b1b`  |
| 2183   | Layout 1             | `0478a63d3b1b`  |
| 2179   | Layout 1             | `0478a63d3b1b`  |
| 2171   | Layout 1             | `0478a63d3b1b`  |
| 2163   | Layout 1             | `0478a63d3b1b`  |
| 2156   | Layout 1             | `0478a63d3b1b`  |
| 2151   | Layout 1             | `0478a63d3b1b`  |
| 2147   | Layout 1             | `0478a63d3b1b`  |
| 2142   | Layout 1             | `0478a63d3b1b`  |
| 2138   | Layout 1             | `0478a63d3b1b`  |
| 2134   | Layout 1             | `0478a63d3b1b`  |
| 2130   | Layout 1             | `0478a63d3b1b`  |
| 2122   | Layout 1             | `0478a63d3b1b`  |
| 2107   | Layout 1             | `0478a63d3b1b`  |
| 2098   | Layout 1             | `0478a63d3b1b`  |
| 2089   | Layout 1             | `0478a63d3b1b`  |
| 2081   | Layout 1             | `0478a63d3b1b`  |
| 2073   | Layout 1             | `0478a63d3b1b`  |
| 2067   | Layout 1             | `0478a63d3b1b`  |
| 2063   | Layout 1             | `0478a63d3b1b`  |
| 2059   | Layout 1             | `0478a63d3b1b`  |
| 2052   | Layout 1             | `0478a63d3b1b`  |
| 2044   | Layout 1             | `0478a63d3b1b`  |
| 2039   | Layout 1             | `0478a63d3b1b`  |
| 2032   | Layout 1             | `0478a63d3b1b`  |
| 2025   | Layout 1             | `0478a63d3b1b`  |
| 2011   | Layout 1             | `0478a63d3b1b`  |
| 2005   | Layout 1             | `0478a63d3b1b`  |
| 2000   | Layout 1             | `0478a63d3b1b`  |
| 1996   | Layout 1             | `0478a63d3b1b`  |
| 1991   | Layout 1             | `0478a63d3b1b`  |
| 1985   | Layout 1             | `0478a63d3b1b`  |
| 1980   | Layout 1             | `0478a63d3b1b`  |
| 1969   | Layout 1             | `0478a63d3b1b`  |
| 1964   | Layout 1             | `0478a63d3b1b`  |
| 1958   | Layout 1             | `0478a63d3b1b`  |
| 1950   | Layout 1             | `0478a63d3b1b`  |
| 1945   | Layout 1             | `0478a63d3b1b`  |
| 1937   | Layout 1             | `0478a63d3b1b`  |
| 1933   | Layout 1             | `0478a63d3b1b`  |
| 1927   | Layout 1             | `0478a63d3b1b`  |
| 1921   | Layout 1             | `0478a63d3b1b`  |
| 1914   | Layout 1             | `0478a63d3b1b`  |
| 1908   | Layout 1             | `0478a63d3b1b`  |
| 1897   | Layout 1             | `0478a63d3b1b`  |
| 1892   | Layout 1             | `0478a63d3b1b`  |
| 1886   | Layout 1             | `0478a63d3b1b`  |
| 1881   | Layout 1             | `0478a63d3b1b`  |
| 1871   | Layout 1             | `0478a63d3b1b`  |
| 1866   | Layout 1             | `0478a63d3b1b`  |
| 1862   | Layout 1             | `0478a63d3b1b`  |
| 1854   | Layout 1             | `0478a63d3b1b`  |
| 1846   | Layout 1             | `0478a63d3b1b`  |
| 1838   | Layout 1             | `0478a63d3b1b`  |
| 1832   | Layout 1             | `0478a63d3b1b`  |
| 1826   | Layout 1             | `0478a63d3b1b`  |
| 1822   | Layout 1             | `0478a63d3b1b`  |
| 1818   | Layout 1             | `0478a63d3b1b`  |
| 1804   | Layout 1             | `0478a63d3b1b`  |
| 1794   | Layout 1             | `0478a63d3b1b`  |
| 1790   | Layout 1             | `0478a63d3b1b`  |
| 1784   | Layout 1             | `0478a63d3b1b`  |
| 1774   | Layout 1             | `0478a63d3b1b`  |
| 1771   | Layout 1             | `0478a63d3b1b`  |
| 1762   | Layout 1             | `0478a63d3b1b`  |
| 1759   | Layout 1             | `0478a63d3b1b`  |
| 1754   | Layout 1             | `0478a63d3b1b`  |
| 1749   | Layout 1             | `0478a63d3b1b`  |
| 1743   | Layout 1             | `0478a63d3b1b`  |
| 1737   | Layout 1             | `0478a63d3b1b`  |
| 1731   | Layout 1             | `0478a63d3b1b`  |
| 1725   | Layout 1             | `0478a63d3b1b`  |
| 1717   | Layout 1             | `0478a63d3b1b`  |
| 1710   | Layout 1             | `0478a63d3b1b`  |
| 1704   | Layout 1             | `0478a63d3b1b`  |
| 1698   | Layout 1             | `0478a63d3b1b`  |
| 1690   | Layout 1             | `0478a63d3b1b`  |
| 1685   | Layout 1             | `0478a63d3b1b`  |
| 1680   | Layout 1             | `0478a63d3b1b`  |
| 1674   | Layout 1             | `0478a63d3b1b`  |
| 1668   | Layout 1             | `0478a63d3b1b`  |
| 1659   | Layout 1             | `0478a63d3b1b`  |
| 1649   | Layout 1             | `0478a63d3b1b`  |
| 1642   | Layout 1             | `0478a63d3b1b`  |
| 1636   | Layout 1             | `0478a63d3b1b`  |
| 1628   | Layout 1             | `0478a63d3b1b`  |
| 1622   | Layout 1             | `0478a63d3b1b`  |
| 1614   | Layout 1             | `0478a63d3b1b`  |
| 1608   | Layout 1             | `0478a63d3b1b`  |
| 1602   | Layout 1             | `0478a63d3b1b`  |
| 1598   | Layout 1             | `0478a63d3b1b`  |
| 1594   | Layout 1             | `0478a63d3b1b`  |
| 1590   | Layout 1             | `0478a63d3b1b`  |
| 1587   | Layout 1             | `0478a63d3b1b`  |
| 1584   | Layout 1             | `0478a63d3b1b`  |
| 1579   | Layout 1             | `0478a63d3b1b`  |
| 1572   | Layout 1             | `0478a63d3b1b`  |
| 1565   | Layout 1             | `0478a63d3b1b`  |
| 1559   | Layout 1             | `0478a63d3b1b`  |
| 1554   | Layout 1             | `0478a63d3b1b`  |
| 1547   | Layout 1             | `0478a63d3b1b`  |
| 1537   | Layout 1             | `0478a63d3b1b`  |
| 1529   | Layout 1             | `0478a63d3b1b`  |
| 1524   | Layout 1             | `0478a63d3b1b`  |
| 1519   | Layout 1             | `0478a63d3b1b`  |
| 1509   | Layout 1             | `0478a63d3b1b`  |
| 1506   | Layout 1             | `0478a63d3b1b`  |
| 1504   | Layout 1             | `0478a63d3b1b`  |
| 1500   | Layout 1             | `0478a63d3b1b`  |
| 1493   | Layout 1             | `0478a63d3b1b`  |
| 1489   | Layout 1             | `0478a63d3b1b`  |
| 1485   | Layout 1             | `0478a63d3b1b`  |
| 1481   | Layout 1             | `0478a63d3b1b`  |
| 1474   | Layout 1             | `0478a63d3b1b`  |
| 1466   | Layout 1             | `0478a63d3b1b`  |
| 1462   | Layout 1             | `0478a63d3b1b`  |
| 1459   | Layout 1             | `0478a63d3b1b`  |
| 1453   | Layout 1             | `0478a63d3b1b`  |
| 1450   | Layout 1             | `0478a63d3b1b`  |
| 1445   | Layout 1             | `0478a63d3b1b`  |
| 1439   | Layout 1             | `0478a63d3b1b`  |
| 1433   | Layout 1             | `0478a63d3b1b`  |
| 1430   | Layout 1             | `0478a63d3b1b`  |
| 1426   | Layout 1             | `0478a63d3b1b`  |
| 1421   | Layout 1             | `0478a63d3b1b`  |
| 1417   | Layout 1             | `0478a63d3b1b`  |
| 1416   | Layout 1             | `0478a63d3b1b`  |
| 1409   | Layout 1             | `0478a63d3b1b`  |
| 1405   | Layout 1             | `0478a63d3b1b`  |
| 1401   | Layout 1             | `0478a63d3b1b`  |
| 1396   | Layout 1             | `0478a63d3b1b`  |
| 1391   | Layout 1             | `0478a63d3b1b`  |
| 1390   | Layout 1             | `0478a63d3b1b`  |
| 1386   | Layout 1             | `0478a63d3b1b`  |
| 1381   | Layout 1             | `0478a63d3b1b`  |
| 1379   | Layout 1             | `0478a63d3b1b`  |
| 1372   | Layout 1             | `0478a63d3b1b`  |
| 1366   | Layout 1             | `0478a63d3b1b`  |
| 1364   | Layout 1             | `0478a63d3b1b`  |
| 1363   | Layout 1             | `0478a63d3b1b`  |
| 1360   | Layout 1             | `0478a63d3b1b`  |
| 1358   | Layout 1             | `0478a63d3b1b`  |
| 1355   | Layout 1             | `0478a63d3b1b`  |
| 1351   | Layout 1             | `0478a63d3b1b`  |
| 1348   | Layout 1             | `0478a63d3b1b`  |
| 1346   | Layout 1             | `0478a63d3b1b`  |
| 1341   | Layout 1             | `0478a63d3b1b`  |
| 1340   | Layout 1             | `0478a63d3b1b`  |
| 1338   | Layout 1             | `0478a63d3b1b`  |
| 1335   | Layout 1             | `0478a63d3b1b`  |
| 1333   | Layout 1             | `0478a63d3b1b`  |
| 1329   | Layout 1             | `0478a63d3b1b`  |
| 1327   | Layout 1             | `0478a63d3b1b`  |
| 1324   | Layout 1             | `0478a63d3b1b`  |
| 1321   | Layout 1             | `0478a63d3b1b`  |
| 1319   | Layout 1             | `0478a63d3b1b`  |
| 1318   | Layout 1             | `0478a63d3b1b`  |
| 1316   | Layout 1             | `0478a63d3b1b`  |
| 1313   | Layout 1             | `0478a63d3b1b`  |
| 1311   | Layout 1             | `0478a63d3b1b`  |
| 1309   | Layout 1             | `0478a63d3b1b`  |
| 1304   | Layout 1             | `0478a63d3b1b`  |
| 1292   | Layout 1             | `0478a63d3b1b`  |
| 1286   | Layout 1             | `0478a63d3b1b`  |
| 1280   | Layout 1             | `0478a63d3b1b`  |
| 1276   | Layout 1             | `0478a63d3b1b`  |
| 1267   | Layout 1             | `0478a63d3b1b`  |
| 1261   | Layout 1             | `0478a63d3b1b`  |
| 1256   | Layout 1             | `0478a63d3b1b`  |
| 1250   | Layout 1             | `0478a63d3b1b`  |
| 1246   | Layout 1             | `0478a63d3b1b`  |
| 1239   | Layout 1             | `0478a63d3b1b`  |
| 1230   | Layout 1             | `0478a63d3b1b`  |
| 1226   | Layout 1             | `0478a63d3b1b`  |
| 1220   | Layout 1             | `0478a63d3b1b`  |
| 1217   | Layout 1             | `0478a63d3b1b`  |
| 1211   | Layout 1             | `0478a63d3b1b`  |
| 1210   | Layout 1             | `0478a63d3b1b`  |
| 1208   | Layout 1             | `0478a63d3b1b`  |
| 1203   | Layout 1             | `0478a63d3b1b`  |
| 1197   | Layout 1             | `0478a63d3b1b`  |
| 1194   | Layout 1             | `0478a63d3b1b`  |
| 1192   | Layout 1             | `0478a63d3b1b`  |
| 1187   | Layout 1             | `0478a63d3b1b`  |
| 1183   | Layout 1             | `0478a63d3b1b`  |
| 1177   | Layout 1             | `0478a63d3b1b`  |
| 1173   | Layout 1             | `0478a63d3b1b`  |
| 1167   | Layout 1             | `0478a63d3b1b`  |
| 1164   | Layout 1             | `0478a63d3b1b`  |
| 1156   | Layout 1             | `0478a63d3b1b`  |
| 1149   | Layout 1             | `0478a63d3b1b`  |
| 1144   | Layout 1             | `0478a63d3b1b`  |
| 1137   | Layout 1             | `0478a63d3b1b`  |
| 1132   | Layout 1             | `0478a63d3b1b`  |
| 1127   | Layout 1             | `0478a63d3b1b`  |
| 1122   | Layout 1             | `0478a63d3b1b`  |
| 1118   | Layout 1             | `0478a63d3b1b`  |
| 1114   | Layout 1             | `0478a63d3b1b`  |
| 1109   | Layout 1             | `0478a63d3b1b`  |
| 1102   | Layout 1             | `0478a63d3b1b`  |
| 1096   | Layout 1             | `0478a63d3b1b`  |
| 1088   | Layout 1             | `0478a63d3b1b`  |
| 1081   | Layout 1             | `0478a63d3b1b`  |
| 1076   | Layout 1             | `0478a63d3b1b`  |
| 1069   | Layout 1             | `0478a63d3b1b`  |
| 1064   | Layout 1             | `0478a63d3b1b`  |
| 1058   | Layout 1             | `0478a63d3b1b`  |
| 1051   | Layout 1             | `0478a63d3b1b`  |
| 1044   | Layout 1             | `0478a63d3b1b`  |
| 1036   | Layout 1             | `0478a63d3b1b`  |
| 1026   | Layout 1             | `0478a63d3b1b`  |
| 1016   | Layout 1             | `0478a63d3b1b`  |
| 1009   | Layout 1             | `0478a63d3b1b`  |
| 1005   | Layout 1             | `0478a63d3b1b`  |
| 1000   | Layout 1             | `0478a63d3b1b`  |
| 998    | Layout 1             | `0478a63d3b1b`  |
| 990    | Layout 1             | `0478a63d3b1b`  |
| 979    | Layout 1             | `0478a63d3b1b`  |
| 972    | Layout 1             | `0478a63d3b1b`  |
| 963    | Layout 1             | `0478a63d3b1b`  |
| 955    | Layout 1             | `0478a63d3b1b`  |
| 946    | Layout 1             | `0478a63d3b1b`  |
| 938    | Layout 1             | `0478a63d3b1b`  |
| 927    | Layout 1             | `0478a63d3b1b`  |
| 911    | Layout 1             | `0478a63d3b1b`  |
| 904    | Layout 1             | `0478a63d3b1b`  |
| 899    | Layout 1             | `0478a63d3b1b`  |
| 894    | Layout 1             | `0478a63d3b1b`  |
| 885    | Layout 1             | `0478a63d3b1b`  |
| 879    | Layout 1             | `0478a63d3b1b`  |
| 872    | Layout 1             | `0478a63d3b1b`  |
| 864    | Layout 1             | `0478a63d3b1b`  |
| 855    | Layout 1             | `0478a63d3b1b`  |
| 853    | Layout 1             | `0478a63d3b1b`  |
| 845    | Layout 1             | `0478a63d3b1b`  |
| 837    | Layout 1             | `0478a63d3b1b`  |
| 829    | Layout 1             | `0478a63d3b1b`  |
| 822    | Layout 1             | `0478a63d3b1b`  |
| 814    | Layout 1             | `0478a63d3b1b`  |
| 805    | Layout 1             | `0478a63d3b1b`  |
| 794    | No documented layout | `0478a63d3b1b`  |
| 787    | No documented layout | `0478a63d3b1b`  |
| 780    | No documented layout | `0478a63d3b1b`  |
| 771    | No documented layout | `0478a63d3b1b`  |
| 760    | No documented layout | `0478a63d3b1b`  |
| 748    | No documented layout | `0478a63d3b1b`  |
| 741    | No documented layout | `0478a63d3b1b`  |
| 736    | No documented layout | `0478a63d3b1b`  |
| 731    | No documented layout | `0478a63d3b1b`  |
| 723    | No documented layout | `0478a63d3b1b`  |
| 711    | No documented layout | `0478a63d3b1b`  |
| 707    | No documented layout | `0478a63d3b1b`  |
| 697    | No documented layout | `0478a63d3b1b`  |
| 689    | No documented layout | `0478a63d3b1b`  |
| 683    | No documented layout | `0478a63d3b1b`  |
| 678    | No documented layout | `0478a63d3b1b`  |
| 670    | No documented layout | `0478a63d3b1b`  |
| 661    | No documented layout | `0478a63d3b1b`  |
| 656    | No documented layout | `0478a63d3b1b`  |
| 652    | No documented layout | `0478a63d3b1b`  |
| 643    | No documented layout | `0478a63d3b1b`  |
| 637    | No documented layout | `0478a63d3b1b`  |
| 630    | No documented layout | `0478a63d3b1b`  |
| 627    | No documented layout | `0478a63d3b1b`  |
| 621    | No documented layout | `0478a63d3b1b`  |
| 617    | No documented layout | `0478a63d3b1b`  |
| 615    | No documented layout | `0478a63d3b1b`  |
| 606    | No documented layout | `0478a63d3b1b`  |
| 599    | No documented layout | `0478a63d3b1b`  |
| 592    | No documented layout | `0478a63d3b1b`  |
| 586    | No documented layout | `0478a63d3b1b`  |
| 577    | No documented layout | `0478a63d3b1b`  |
| 569    | No documented layout | `0478a63d3b1b`  |
| 561    | No documented layout | `0478a63d3b1b`  |
| 554    | No documented layout | `0478a63d3b1b`  |
| 542    | No documented layout | `0478a63d3b1b`  |
| 532    | No documented layout | `0478a63d3b1b`  |
| 531    | No documented layout | `0478a63d3b1b`  |
| 526    | No documented layout | `0478a63d3b1b`  |
| 521    | No documented layout | `0478a63d3b1b`  |
| 517    | No documented layout | `0478a63d3b1b`  |
| 510    | No documented layout | `0478a63d3b1b`  |
| 508    | No documented layout | `0478a63d3b1b`  |
| 504    | No documented layout | `0478a63d3b1b`  |
| 497    | No documented layout | `0478a63d3b1b`  |
| 491    | No documented layout | `0478a63d3b1b`  |
| 485    | No documented layout | `0478a63d3b1b`  |
| 478    | No documented layout | `0478a63d3b1b`  |
| 472    | No documented layout | `0478a63d3b1b`  |
| 466    | No documented layout | `0478a63d3b1b`  |
| 457    | No documented layout | `0478a63d3b1b`  |
| 452    | No documented layout | `0478a63d3b1b`  |
| 449    | No documented layout | `0478a63d3b1b`  |
| 435    | No documented layout | `0478a63d3b1b`  |

<!-- versions:end -->

## Companion Files

The file is self-contained. The handler reads names through the shared LOC
lookup:

| File                  | Required | Role                                                              |
| --------------------- | -------- | ----------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Class names (LOC type `21`, `str_id1` = class type) and skill names (LOC type `10`, `str_id1` = skill number) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                  | Field              | Notes                                                        |
| ------------------- | --------------------- | ------------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]               | magic              | `PABR` (ASCII)                                               |
| `+0x04`             | u32                   | class_count        | Number of rows; `32` on client 3473                          |
| `+0x08`             | Class Row[class_count] | rows              | See Class Row                                                |
| `rows+0x00`         | String Table          | string_table       | The PABR string table, present but empty                     |
| `string_table+0x00` | u32                   | string_table_start | Absolute offset of `string_count`, where the rows end        |
| `string_table+0x04` | u32                   | zero               | Always `0`                                                   |

On client 3473 the 32 rows end at `0x550`, the stored `string_table_start`,
and the file is 1,372 bytes. The parser rejects a file whose rows do not end
there.

### Class Row (variable: 9 bytes + skill numbers)

| Offset  | Type             | Field       | Notes                                                                   |
| ------- | ---------------- | ----------- | ----------------------------------------------------------------------- |
| `+0x00` | u8               | class_type  | The class type `getClassType()` returns, LOC type `21` names it; unique |
| `+0x01` | u64              | skill_count | Number of skill numbers that follow; `8` to `22` on client 3473          |
| `+0x09` | u16[skill_count] | skill_nos   | Skill numbers (`skill_key >> 16`), LOC type `10` names them             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Notes

- On client 3473 the 32 rows cover every playable class type from `0` to
  `35` except the unused `13`, `14`, `18` and `22`. They are not sorted:
  `34` (Deadeye) comes before `32` (Seraph) and `35` (Agent).
- Each row lists skills of its own class by LOC name: row `0` (Warrior)
  starts with `216` Ground Roar, `1021` Spinning Slash and `1022` Charging
  Thrust. Wizard (`28`) and Witch (`31`) share their first 8 numbers
  (Fireball, Lightning, Meteor Shower and others), Kunoichi (`25`) and Ninja
  (`26`) share 5.
- A row can list a number twice: on client 3473 the Guardian row (`5`)
  holds `5011` Fierce Disdain and `5082` Mutilation twice each. No other
  row repeats a number.
- The client Lua of the Skill Guide (`ui_widget_skillcommand.luac`)
  calls `ToClient_RequestCommandList()` and receives one
  `FromClient_SkillCommandList(skillNo, isAwaken)` call per skill. The
  `isAwaken` flag is not stored in this file.
- The `binary/classskilllist.bss` of a private server on client 1784 has the
  same layout with 24 rows.
- Checked in game on client 3474 with a Wizard: the Skill Guide (Edit UI,
  hidden in safe zones) lists the Wizard row in file order. The main
  weapon shows the eight main weapon numbers and the awakening weapon the
  five awakening ones (`2212` Lava Field to `2232` Cataclysm). Each line
  shows the highest learned rank (`ToClient_GetTopLevelLearnActiveSkillNo`
  in the Lua), so `818` Fireball I and `819` Fireball II share the one
  "Absolute: Fireball" line.
