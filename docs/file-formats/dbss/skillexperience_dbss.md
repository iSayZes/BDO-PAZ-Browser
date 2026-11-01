# `skillexperience.dbss` Format

## Purpose

EXP table of the combat skill points: the Skill EXP a character needs to go from one skill point level to the next, from level 0 to the max level in [skillexperiencemaxlevel](../bss/skillexperiencemaxlevel_bss.md). Companion `skillexperienceoffset.dbss` lists where every row sits. [guildskillexperience](guildskillexperience_dbss.md) (guild points) and [productexperience](productexperience_dbss.md) (life skill points) use the same container with other rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes  | Records          | Row bytes |
| ------ | -------------- | ---------------------------- | ------ | ---------------- | --------- |
| 1      | 1276 and later | `skillexperience.dbss`       | 32,020 | 2,001 Level Row  | 16        |
| 1      | 1276 and later | `skillexperienceoffset.dbss` | 20,014 | 2,001 Offset Row | 10        |

| Layout | File                         | Known             | Unknown    |
| ------ | ---------------------------- | ----------------- | ---------- |
| 1      | `skillexperience.dbss`       | 32,020 B (100.0%) | 0 B (0.0%) |
| 1      | `skillexperienceoffset.dbss` | 20,014 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a9a5f55e6b40`  |
| 3482   | Layout 1 | `a9a5f55e6b40`  |
| 3474   | Layout 1 | `a9a5f55e6b40`  |
| 3473   | Layout 1 | `a9a5f55e6b40`  |
| 3464   | Layout 1 | `a9a5f55e6b40`  |
| 3458   | Layout 1 | `a9a5f55e6b40`  |
| 3454   | Layout 1 | `a9a5f55e6b40`  |
| 3444   | Layout 1 | `a9a5f55e6b40`  |
| 3435   | Layout 1 | `a9a5f55e6b40`  |
| 3426   | Layout 1 | `a9a5f55e6b40`  |
| 3418   | Layout 1 | `a9a5f55e6b40`  |
| 3412   | Layout 1 | `a9a5f55e6b40`  |
| 3402   | Layout 1 | `a9a5f55e6b40`  |
| 3396   | Layout 1 | `a9a5f55e6b40`  |
| 3387   | Layout 1 | `a9a5f55e6b40`  |
| 3381   | Layout 1 | `a9a5f55e6b40`  |
| 3373   | Layout 1 | `a9a5f55e6b40`  |
| 3364   | Layout 1 | `a9a5f55e6b40`  |
| 3356   | Layout 1 | `a9a5f55e6b40`  |
| 3349   | Layout 1 | `a9a5f55e6b40`  |
| 3342   | Layout 1 | `a9a5f55e6b40`  |
| 3335   | Layout 1 | `a9a5f55e6b40`  |
| 3326   | Layout 1 | `a9a5f55e6b40`  |
| 3321   | Layout 1 | `a9a5f55e6b40`  |
| 3314   | Layout 1 | `a9a5f55e6b40`  |
| 3303   | Layout 1 | `a9a5f55e6b40`  |
| 3302   | Layout 1 | `a9a5f55e6b40`  |
| 3293   | Layout 1 | `a9a5f55e6b40`  |
| 3283   | Layout 1 | `a9a5f55e6b40`  |
| 3275   | Layout 1 | `a9a5f55e6b40`  |
| 3267   | Layout 1 | `a9a5f55e6b40`  |
| 3258   | Layout 1 | `a9a5f55e6b40`  |
| 3251   | Layout 1 | `a9a5f55e6b40`  |
| 3242   | Layout 1 | `a9a5f55e6b40`  |
| 3235   | Layout 1 | `a9a5f55e6b40`  |
| 3229   | Layout 1 | `a9a5f55e6b40`  |
| 3212   | Layout 1 | `a9a5f55e6b40`  |
| 3203   | Layout 1 | `a9a5f55e6b40`  |
| 3193   | Layout 1 | `a9a5f55e6b40`  |
| 3186   | Layout 1 | `a9a5f55e6b40`  |
| 3177   | Layout 1 | `a9a5f55e6b40`  |
| 3169   | Layout 1 | `a9a5f55e6b40`  |
| 3158   | Layout 1 | `a9a5f55e6b40`  |
| 3151   | Layout 1 | `a9a5f55e6b40`  |
| 3144   | Layout 1 | `a9a5f55e6b40`  |
| 3133   | Layout 1 | `a9a5f55e6b40`  |
| 3125   | Layout 1 | `a9a5f55e6b40`  |
| 3118   | Layout 1 | `a9a5f55e6b40`  |
| 3111   | Layout 1 | `a9a5f55e6b40`  |
| 3103   | Layout 1 | `a9a5f55e6b40`  |
| 3095   | Layout 1 | `a9a5f55e6b40`  |
| 3086   | Layout 1 | `a9a5f55e6b40`  |
| 3072   | Layout 1 | `a9a5f55e6b40`  |
| 3062   | Layout 1 | `a9a5f55e6b40`  |
| 3052   | Layout 1 | `a9a5f55e6b40`  |
| 3045   | Layout 1 | `a9a5f55e6b40`  |
| 3037   | Layout 1 | `a9a5f55e6b40`  |
| 3030   | Layout 1 | `a9a5f55e6b40`  |
| 3021   | Layout 1 | `a9a5f55e6b40`  |
| 3012   | Layout 1 | `a9a5f55e6b40`  |
| 3002   | Layout 1 | `a9a5f55e6b40`  |
| 2995   | Layout 1 | `a9a5f55e6b40`  |
| 2987   | Layout 1 | `a9a5f55e6b40`  |
| 2978   | Layout 1 | `a9a5f55e6b40`  |
| 2970   | Layout 1 | `a9a5f55e6b40`  |
| 2959   | Layout 1 | `a9a5f55e6b40`  |
| 2951   | Layout 1 | `a9a5f55e6b40`  |
| 2942   | Layout 1 | `a9a5f55e6b40`  |
| 2935   | Layout 1 | `a9a5f55e6b40`  |
| 2932   | Layout 1 | `a9a5f55e6b40`  |
| 2923   | Layout 1 | `a9a5f55e6b40`  |
| 2919   | Layout 1 | `a9a5f55e6b40`  |
| 2907   | Layout 1 | `a9a5f55e6b40`  |
| 2900   | Layout 1 | `a9a5f55e6b40`  |
| 2891   | Layout 1 | `a9a5f55e6b40`  |
| 2882   | Layout 1 | `a9a5f55e6b40`  |
| 2872   | Layout 1 | `a9a5f55e6b40`  |
| 2863   | Layout 1 | `a9a5f55e6b40`  |
| 2855   | Layout 1 | `a9a5f55e6b40`  |
| 2849   | Layout 1 | `a9a5f55e6b40`  |
| 2844   | Layout 1 | `a9a5f55e6b40`  |
| 2834   | Layout 1 | `a9a5f55e6b40`  |
| 2825   | Layout 1 | `a9a5f55e6b40`  |
| 2819   | Layout 1 | `a9a5f55e6b40`  |
| 2811   | Layout 1 | `a9a5f55e6b40`  |
| 2803   | Layout 1 | `a9a5f55e6b40`  |
| 2794   | Layout 1 | `a9a5f55e6b40`  |
| 2783   | Layout 1 | `a9a5f55e6b40`  |
| 2774   | Layout 1 | `a9a5f55e6b40`  |
| 2765   | Layout 1 | `a9a5f55e6b40`  |
| 2756   | Layout 1 | `a9a5f55e6b40`  |
| 2750   | Layout 1 | `a9a5f55e6b40`  |
| 2743   | Layout 1 | `a9a5f55e6b40`  |
| 2736   | Layout 1 | `a9a5f55e6b40`  |
| 2726   | Layout 1 | `a9a5f55e6b40`  |
| 2717   | Layout 1 | `a9a5f55e6b40`  |
| 2709   | Layout 1 | `a9a5f55e6b40`  |
| 2703   | Layout 1 | `a9a5f55e6b40`  |
| 2695   | Layout 1 | `a9a5f55e6b40`  |
| 2684   | Layout 1 | `a9a5f55e6b40`  |
| 2672   | Layout 1 | `a9a5f55e6b40`  |
| 2665   | Layout 1 | `a9a5f55e6b40`  |
| 2657   | Layout 1 | `a9a5f55e6b40`  |
| 2649   | Layout 1 | `a9a5f55e6b40`  |
| 2644   | Layout 1 | `a9a5f55e6b40`  |
| 2637   | Layout 1 | `a9a5f55e6b40`  |
| 2629   | Layout 1 | `a9a5f55e6b40`  |
| 2619   | Layout 1 | `a9a5f55e6b40`  |
| 2612   | Layout 1 | `a9a5f55e6b40`  |
| 2606   | Layout 1 | `a9a5f55e6b40`  |
| 2602   | Layout 1 | `a9a5f55e6b40`  |
| 2601   | Layout 1 | `a9a5f55e6b40`  |
| 2592   | Layout 1 | `a9a5f55e6b40`  |
| 2583   | Layout 1 | `a9a5f55e6b40`  |
| 2575   | Layout 1 | `a9a5f55e6b40`  |
| 2567   | Layout 1 | `a9a5f55e6b40`  |
| 2560   | Layout 1 | `a9a5f55e6b40`  |
| 2553   | Layout 1 | `a9a5f55e6b40`  |
| 2545   | Layout 1 | `a9a5f55e6b40`  |
| 2538   | Layout 1 | `a9a5f55e6b40`  |
| 2529   | Layout 1 | `a9a5f55e6b40`  |
| 2519   | Layout 1 | `a9a5f55e6b40`  |
| 2513   | Layout 1 | `a9a5f55e6b40`  |
| 2510   | Layout 1 | `a9a5f55e6b40`  |
| 2507   | Layout 1 | `a9a5f55e6b40`  |
| 2503   | Layout 1 | `a9a5f55e6b40`  |
| 2498   | Layout 1 | `a9a5f55e6b40`  |
| 2492   | Layout 1 | `a9a5f55e6b40`  |
| 2487   | Layout 1 | `a9a5f55e6b40`  |
| 2480   | Layout 1 | `a9a5f55e6b40`  |
| 2474   | Layout 1 | `a9a5f55e6b40`  |
| 2468   | Layout 1 | `a9a5f55e6b40`  |
| 2460   | Layout 1 | `a9a5f55e6b40`  |
| 2453   | Layout 1 | `a9a5f55e6b40`  |
| 2444   | Layout 1 | `a9a5f55e6b40`  |
| 2438   | Layout 1 | `a9a5f55e6b40`  |
| 2434   | Layout 1 | `a9a5f55e6b40`  |
| 2429   | Layout 1 | `a9a5f55e6b40`  |
| 2421   | Layout 1 | `a9a5f55e6b40`  |
| 2414   | Layout 1 | `a9a5f55e6b40`  |
| 2407   | Layout 1 | `a9a5f55e6b40`  |
| 2401   | Layout 1 | `a9a5f55e6b40`  |
| 2397   | Layout 1 | `a9a5f55e6b40`  |
| 2393   | Layout 1 | `a9a5f55e6b40`  |
| 2384   | Layout 1 | `a9a5f55e6b40`  |
| 2378   | Layout 1 | `a9a5f55e6b40`  |
| 2372   | Layout 1 | `a9a5f55e6b40`  |
| 2358   | Layout 1 | `a9a5f55e6b40`  |
| 2352   | Layout 1 | `a9a5f55e6b40`  |
| 2347   | Layout 1 | `a9a5f55e6b40`  |
| 2343   | Layout 1 | `a9a5f55e6b40`  |
| 2335   | Layout 1 | `a9a5f55e6b40`  |
| 2327   | Layout 1 | `a9a5f55e6b40`  |
| 2324   | Layout 1 | `a9a5f55e6b40`  |
| 2319   | Layout 1 | `a9a5f55e6b40`  |
| 2313   | Layout 1 | `a9a5f55e6b40`  |
| 2308   | Layout 1 | `a9a5f55e6b40`  |
| 2302   | Layout 1 | `a9a5f55e6b40`  |
| 2295   | Layout 1 | `a9a5f55e6b40`  |
| 2290   | Layout 1 | `a9a5f55e6b40`  |
| 2284   | Layout 1 | `a9a5f55e6b40`  |
| 2276   | Layout 1 | `a9a5f55e6b40`  |
| 2269   | Layout 1 | `a9a5f55e6b40`  |
| 2259   | Layout 1 | `a9a5f55e6b40`  |
| 2250   | Layout 1 | `a9a5f55e6b40`  |
| 2243   | Layout 1 | `a9a5f55e6b40`  |
| 2235   | Layout 1 | `a9a5f55e6b40`  |
| 2229   | Layout 1 | `a9a5f55e6b40`  |
| 2224   | Layout 1 | `a9a5f55e6b40`  |
| 2218   | Layout 1 | `a9a5f55e6b40`  |
| 2215   | Layout 1 | `a9a5f55e6b40`  |
| 2207   | Layout 1 | `a9a5f55e6b40`  |
| 2203   | Layout 1 | `a9a5f55e6b40`  |
| 2196   | Layout 1 | `a9a5f55e6b40`  |
| 2192   | Layout 1 | `a9a5f55e6b40`  |
| 2189   | Layout 1 | `a9a5f55e6b40`  |
| 2183   | Layout 1 | `a9a5f55e6b40`  |
| 2179   | Layout 1 | `a9a5f55e6b40`  |
| 2171   | Layout 1 | `a9a5f55e6b40`  |
| 2163   | Layout 1 | `a9a5f55e6b40`  |
| 2156   | Layout 1 | `a9a5f55e6b40`  |
| 2151   | Layout 1 | `a9a5f55e6b40`  |
| 2147   | Layout 1 | `a9a5f55e6b40`  |
| 2142   | Layout 1 | `a9a5f55e6b40`  |
| 2138   | Layout 1 | `a9a5f55e6b40`  |
| 2134   | Layout 1 | `a9a5f55e6b40`  |
| 2130   | Layout 1 | `a9a5f55e6b40`  |
| 2122   | Layout 1 | `a9a5f55e6b40`  |
| 2107   | Layout 1 | `a9a5f55e6b40`  |
| 2098   | Layout 1 | `a9a5f55e6b40`  |
| 2089   | Layout 1 | `a9a5f55e6b40`  |
| 2081   | Layout 1 | `a9a5f55e6b40`  |
| 2073   | Layout 1 | `a9a5f55e6b40`  |
| 2067   | Layout 1 | `a9a5f55e6b40`  |
| 2063   | Layout 1 | `a9a5f55e6b40`  |
| 2059   | Layout 1 | `a9a5f55e6b40`  |
| 2052   | Layout 1 | `a9a5f55e6b40`  |
| 2044   | Layout 1 | `a9a5f55e6b40`  |
| 2039   | Layout 1 | `a9a5f55e6b40`  |
| 2032   | Layout 1 | `a9a5f55e6b40`  |
| 2025   | Layout 1 | `a9a5f55e6b40`  |
| 2011   | Layout 1 | `a9a5f55e6b40`  |
| 2005   | Layout 1 | `a9a5f55e6b40`  |
| 2000   | Layout 1 | `a9a5f55e6b40`  |
| 1996   | Layout 1 | `a9a5f55e6b40`  |
| 1991   | Layout 1 | `a9a5f55e6b40`  |
| 1985   | Layout 1 | `a9a5f55e6b40`  |
| 1980   | Layout 1 | `a9a5f55e6b40`  |
| 1969   | Layout 1 | `a9a5f55e6b40`  |
| 1964   | Layout 1 | `a9a5f55e6b40`  |
| 1958   | Layout 1 | `a9a5f55e6b40`  |
| 1950   | Layout 1 | `a9a5f55e6b40`  |
| 1945   | Layout 1 | `a9a5f55e6b40`  |
| 1937   | Layout 1 | `a9a5f55e6b40`  |
| 1933   | Layout 1 | `a9a5f55e6b40`  |
| 1927   | Layout 1 | `a9a5f55e6b40`  |
| 1921   | Layout 1 | `a9a5f55e6b40`  |
| 1914   | Layout 1 | `a9a5f55e6b40`  |
| 1908   | Layout 1 | `a9a5f55e6b40`  |
| 1897   | Layout 1 | `a9a5f55e6b40`  |
| 1892   | Layout 1 | `a9a5f55e6b40`  |
| 1886   | Layout 1 | `a9a5f55e6b40`  |
| 1881   | Layout 1 | `a9a5f55e6b40`  |
| 1871   | Layout 1 | `a9a5f55e6b40`  |
| 1866   | Layout 1 | `a9a5f55e6b40`  |
| 1862   | Layout 1 | `a9a5f55e6b40`  |
| 1854   | Layout 1 | `a9a5f55e6b40`  |
| 1846   | Layout 1 | `a9a5f55e6b40`  |
| 1838   | Layout 1 | `a9a5f55e6b40`  |
| 1832   | Layout 1 | `a9a5f55e6b40`  |
| 1826   | Layout 1 | `a9a5f55e6b40`  |
| 1822   | Layout 1 | `a9a5f55e6b40`  |
| 1818   | Layout 1 | `a9a5f55e6b40`  |
| 1804   | Layout 1 | `a9a5f55e6b40`  |
| 1794   | Layout 1 | `a9a5f55e6b40`  |
| 1790   | Layout 1 | `a9a5f55e6b40`  |
| 1784   | Layout 1 | `a9a5f55e6b40`  |
| 1774   | Layout 1 | `a9a5f55e6b40`  |
| 1771   | Layout 1 | `a9a5f55e6b40`  |
| 1762   | Layout 1 | `a9a5f55e6b40`  |
| 1759   | Layout 1 | `a9a5f55e6b40`  |
| 1754   | Layout 1 | `a9a5f55e6b40`  |
| 1749   | Layout 1 | `a9a5f55e6b40`  |
| 1743   | Layout 1 | `a9a5f55e6b40`  |
| 1737   | Layout 1 | `a9a5f55e6b40`  |
| 1731   | Layout 1 | `a9a5f55e6b40`  |
| 1725   | Layout 1 | `a9a5f55e6b40`  |
| 1717   | Layout 1 | `a9a5f55e6b40`  |
| 1710   | Layout 1 | `a9a5f55e6b40`  |
| 1704   | Layout 1 | `a9a5f55e6b40`  |
| 1698   | Layout 1 | `a9a5f55e6b40`  |
| 1690   | Layout 1 | `a9a5f55e6b40`  |
| 1685   | Layout 1 | `a9a5f55e6b40`  |
| 1680   | Layout 1 | `a9a5f55e6b40`  |
| 1674   | Layout 1 | `a9a5f55e6b40`  |
| 1668   | Layout 1 | `a9a5f55e6b40`  |
| 1659   | Layout 1 | `a9a5f55e6b40`  |
| 1649   | Layout 1 | `a9a5f55e6b40`  |
| 1642   | Layout 1 | `a9a5f55e6b40`  |
| 1636   | Layout 1 | `a9a5f55e6b40`  |
| 1628   | Layout 1 | `a9a5f55e6b40`  |
| 1622   | Layout 1 | `a9a5f55e6b40`  |
| 1614   | Layout 1 | `a9a5f55e6b40`  |
| 1608   | Layout 1 | `a9a5f55e6b40`  |
| 1602   | Layout 1 | `a9a5f55e6b40`  |
| 1598   | Layout 1 | `a9a5f55e6b40`  |
| 1594   | Layout 1 | `a9a5f55e6b40`  |
| 1590   | Layout 1 | `a9a5f55e6b40`  |
| 1587   | Layout 1 | `a9a5f55e6b40`  |
| 1584   | Layout 1 | `a9a5f55e6b40`  |
| 1579   | Layout 1 | `a9a5f55e6b40`  |
| 1572   | Layout 1 | `a9a5f55e6b40`  |
| 1565   | Layout 1 | `a9a5f55e6b40`  |
| 1559   | Layout 1 | `a9a5f55e6b40`  |
| 1554   | Layout 1 | `a9a5f55e6b40`  |
| 1547   | Layout 1 | `a9a5f55e6b40`  |
| 1537   | Layout 1 | `a9a5f55e6b40`  |
| 1529   | Layout 1 | `a9a5f55e6b40`  |
| 1524   | Layout 1 | `a9a5f55e6b40`  |
| 1519   | Layout 1 | `a9a5f55e6b40`  |
| 1509   | Layout 1 | `a9a5f55e6b40`  |
| 1506   | Layout 1 | `a9a5f55e6b40`  |
| 1504   | Layout 1 | `a9a5f55e6b40`  |
| 1500   | Layout 1 | `a9a5f55e6b40`  |
| 1493   | Layout 1 | `a9a5f55e6b40`  |
| 1489   | Layout 1 | `a9a5f55e6b40`  |
| 1485   | Layout 1 | `a9a5f55e6b40`  |
| 1481   | Layout 1 | `a9a5f55e6b40`  |
| 1474   | Layout 1 | `a9a5f55e6b40`  |
| 1466   | Layout 1 | `a9a5f55e6b40`  |
| 1462   | Layout 1 | `a9a5f55e6b40`  |
| 1459   | Layout 1 | `a9a5f55e6b40`  |
| 1453   | Layout 1 | `a9a5f55e6b40`  |
| 1450   | Layout 1 | `a9a5f55e6b40`  |
| 1445   | Layout 1 | `a9a5f55e6b40`  |
| 1439   | Layout 1 | `a9a5f55e6b40`  |
| 1433   | Layout 1 | `a9a5f55e6b40`  |
| 1430   | Layout 1 | `a9a5f55e6b40`  |
| 1426   | Layout 1 | `a9a5f55e6b40`  |
| 1421   | Layout 1 | `a9a5f55e6b40`  |
| 1417   | Layout 1 | `a9a5f55e6b40`  |
| 1416   | Layout 1 | `a9a5f55e6b40`  |
| 1409   | Layout 1 | `a9a5f55e6b40`  |
| 1405   | Layout 1 | `a9a5f55e6b40`  |
| 1401   | Layout 1 | `a9a5f55e6b40`  |
| 1396   | Layout 1 | `a9a5f55e6b40`  |
| 1391   | Layout 1 | `a9a5f55e6b40`  |
| 1390   | Layout 1 | `a9a5f55e6b40`  |
| 1386   | Layout 1 | `a9a5f55e6b40`  |
| 1381   | Layout 1 | `a9a5f55e6b40`  |
| 1379   | Layout 1 | `a9a5f55e6b40`  |
| 1372   | Layout 1 | `a9a5f55e6b40`  |
| 1366   | Layout 1 | `a9a5f55e6b40`  |
| 1364   | Layout 1 | `a9a5f55e6b40`  |
| 1363   | Layout 1 | `a9a5f55e6b40`  |
| 1360   | Layout 1 | `a9a5f55e6b40`  |
| 1358   | Layout 1 | `a9a5f55e6b40`  |
| 1355   | Layout 1 | `a9a5f55e6b40`  |
| 1351   | Layout 1 | `a9a5f55e6b40`  |
| 1348   | Layout 1 | `a9a5f55e6b40`  |
| 1346   | Layout 1 | `a9a5f55e6b40`  |
| 1341   | Layout 1 | `a9a5f55e6b40`  |
| 1340   | Layout 1 | `a9a5f55e6b40`  |
| 1338   | Layout 1 | `a9a5f55e6b40`  |
| 1335   | Layout 1 | `a9a5f55e6b40`  |
| 1333   | Layout 1 | `a9a5f55e6b40`  |
| 1329   | Layout 1 | `a9a5f55e6b40`  |
| 1327   | Layout 1 | `a9a5f55e6b40`  |
| 1324   | Layout 1 | `a9a5f55e6b40`  |
| 1321   | Layout 1 | `a9a5f55e6b40`  |
| 1319   | Layout 1 | `a9a5f55e6b40`  |
| 1318   | Layout 1 | `a9a5f55e6b40`  |
| 1316   | Layout 1 | `a9a5f55e6b40`  |
| 1313   | Layout 1 | `a9a5f55e6b40`  |
| 1311   | Layout 1 | `a9a5f55e6b40`  |
| 1309   | Layout 1 | `a9a5f55e6b40`  |
| 1304   | Layout 1 | `a9a5f55e6b40`  |
| 1292   | Layout 1 | `a9a5f55e6b40`  |
| 1286   | Layout 1 | `a9a5f55e6b40`  |
| 1280   | Layout 1 | `a9a5f55e6b40`  |
| 1276   | Layout 1 | `a9a5f55e6b40`  |
| 1267   | No file  | `a9a5f55e6b40`  |
| 1261   | No file  | `a9a5f55e6b40`  |
| 1256   | No file  | `a9a5f55e6b40`  |
| 1250   | No file  | `a9a5f55e6b40`  |
| 1246   | No file  | `a9a5f55e6b40`  |
| 1239   | No file  | `a9a5f55e6b40`  |
| 1230   | No file  | `a9a5f55e6b40`  |
| 1226   | No file  | `a9a5f55e6b40`  |
| 1220   | No file  | `a9a5f55e6b40`  |
| 1217   | No file  | `a9a5f55e6b40`  |
| 1211   | No file  | `a9a5f55e6b40`  |
| 1210   | No file  | `a9a5f55e6b40`  |
| 1208   | No file  | `a9a5f55e6b40`  |
| 1203   | No file  | `a9a5f55e6b40`  |
| 1197   | No file  | `a9a5f55e6b40`  |
| 1194   | No file  | `a9a5f55e6b40`  |
| 1192   | No file  | `a9a5f55e6b40`  |
| 1187   | No file  | `a9a5f55e6b40`  |
| 1183   | No file  | `a9a5f55e6b40`  |
| 1177   | No file  | `a9a5f55e6b40`  |
| 1173   | No file  | `a9a5f55e6b40`  |
| 1167   | No file  | `a9a5f55e6b40`  |
| 1164   | No file  | `a9a5f55e6b40`  |
| 1156   | No file  | `a9a5f55e6b40`  |
| 1149   | No file  | `a9a5f55e6b40`  |
| 1144   | No file  | `a9a5f55e6b40`  |
| 1137   | No file  | `a9a5f55e6b40`  |
| 1132   | No file  | `a9a5f55e6b40`  |
| 1127   | No file  | `a9a5f55e6b40`  |
| 1122   | No file  | `a9a5f55e6b40`  |
| 1118   | No file  | `a9a5f55e6b40`  |
| 1114   | No file  | `a9a5f55e6b40`  |
| 1109   | No file  | `a9a5f55e6b40`  |
| 1102   | No file  | `a9a5f55e6b40`  |
| 1096   | No file  | `a9a5f55e6b40`  |
| 1088   | No file  | `a9a5f55e6b40`  |
| 1081   | No file  | `a9a5f55e6b40`  |
| 1076   | No file  | `a9a5f55e6b40`  |
| 1069   | No file  | `a9a5f55e6b40`  |
| 1064   | No file  | `a9a5f55e6b40`  |
| 1058   | No file  | `a9a5f55e6b40`  |
| 1051   | No file  | `a9a5f55e6b40`  |
| 1044   | No file  | `a9a5f55e6b40`  |
| 1036   | No file  | `a9a5f55e6b40`  |
| 1026   | No file  | `a9a5f55e6b40`  |
| 1016   | No file  | `a9a5f55e6b40`  |
| 1009   | No file  | `a9a5f55e6b40`  |
| 1005   | No file  | `a9a5f55e6b40`  |
| 1000   | No file  | `a9a5f55e6b40`  |
| 998    | No file  | `a9a5f55e6b40`  |
| 990    | No file  | `a9a5f55e6b40`  |
| 979    | No file  | `a9a5f55e6b40`  |
| 972    | No file  | `a9a5f55e6b40`  |
| 963    | No file  | `a9a5f55e6b40`  |
| 955    | No file  | `a9a5f55e6b40`  |
| 946    | No file  | `a9a5f55e6b40`  |
| 938    | No file  | `a9a5f55e6b40`  |
| 927    | No file  | `a9a5f55e6b40`  |
| 911    | No file  | `a9a5f55e6b40`  |
| 904    | No file  | `a9a5f55e6b40`  |
| 899    | No file  | `a9a5f55e6b40`  |
| 894    | No file  | `a9a5f55e6b40`  |
| 885    | No file  | `a9a5f55e6b40`  |
| 879    | No file  | `a9a5f55e6b40`  |
| 872    | No file  | `a9a5f55e6b40`  |
| 864    | No file  | `a9a5f55e6b40`  |
| 855    | No file  | `a9a5f55e6b40`  |
| 853    | No file  | `a9a5f55e6b40`  |
| 845    | No file  | `a9a5f55e6b40`  |
| 837    | No file  | `a9a5f55e6b40`  |
| 829    | No file  | `a9a5f55e6b40`  |
| 822    | No file  | `a9a5f55e6b40`  |
| 814    | No file  | `a9a5f55e6b40`  |
| 805    | No file  | `a9a5f55e6b40`  |
| 794    | No file  | `a9a5f55e6b40`  |
| 787    | No file  | `a9a5f55e6b40`  |
| 780    | No file  | `a9a5f55e6b40`  |
| 771    | No file  | `a9a5f55e6b40`  |
| 760    | No file  | `a9a5f55e6b40`  |
| 748    | No file  | `a9a5f55e6b40`  |
| 741    | No file  | `a9a5f55e6b40`  |
| 736    | No file  | `a9a5f55e6b40`  |
| 731    | No file  | `a9a5f55e6b40`  |
| 723    | No file  | `a9a5f55e6b40`  |
| 711    | No file  | `a9a5f55e6b40`  |
| 707    | No file  | `a9a5f55e6b40`  |
| 697    | No file  | `a9a5f55e6b40`  |
| 689    | No file  | `a9a5f55e6b40`  |
| 683    | No file  | `a9a5f55e6b40`  |
| 678    | No file  | `a9a5f55e6b40`  |
| 670    | No file  | `a9a5f55e6b40`  |
| 661    | No file  | `a9a5f55e6b40`  |
| 656    | No file  | `a9a5f55e6b40`  |
| 652    | No file  | `a9a5f55e6b40`  |
| 643    | No file  | `a9a5f55e6b40`  |
| 637    | No file  | `a9a5f55e6b40`  |
| 630    | No file  | `a9a5f55e6b40`  |
| 627    | No file  | `a9a5f55e6b40`  |
| 621    | No file  | `a9a5f55e6b40`  |
| 617    | No file  | `a9a5f55e6b40`  |
| 615    | No file  | `a9a5f55e6b40`  |
| 606    | No file  | `a9a5f55e6b40`  |
| 599    | No file  | `a9a5f55e6b40`  |
| 592    | No file  | `a9a5f55e6b40`  |
| 586    | No file  | `a9a5f55e6b40`  |
| 577    | No file  | `a9a5f55e6b40`  |
| 569    | No file  | `a9a5f55e6b40`  |
| 561    | No file  | `a9a5f55e6b40`  |
| 554    | No file  | `a9a5f55e6b40`  |
| 542    | No file  | `a9a5f55e6b40`  |
| 532    | No file  | `a9a5f55e6b40`  |
| 531    | No file  | `a9a5f55e6b40`  |
| 526    | No file  | `a9a5f55e6b40`  |
| 521    | No file  | `a9a5f55e6b40`  |
| 517    | No file  | `a9a5f55e6b40`  |
| 510    | No file  | `a9a5f55e6b40`  |
| 508    | No file  | `a9a5f55e6b40`  |
| 504    | No file  | `a9a5f55e6b40`  |
| 497    | No file  | `a9a5f55e6b40`  |
| 491    | No file  | `a9a5f55e6b40`  |
| 485    | No file  | `a9a5f55e6b40`  |
| 478    | No file  | `a9a5f55e6b40`  |
| 472    | No file  | `a9a5f55e6b40`  |
| 466    | No file  | `a9a5f55e6b40`  |
| 457    | No file  | `a9a5f55e6b40`  |
| 452    | No file  | `a9a5f55e6b40`  |
| 449    | No file  | `a9a5f55e6b40`  |
| 435    | No file  | `a9a5f55e6b40`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                         |
| ----------------------------- | -------- | ---------------------------------------------------------------------------- |
| `skillexperienceoffset.dbss`  | Required | `level -> (offset, size)` of every row                                       |
| `skillexperiencemaxlevel.bss` | Optional | Max level, see [skillexperiencemaxlevel](../bss/skillexperiencemaxlevel_bss.md)     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                 | Field     | Notes                                                |
| ------- | -------------------- | --------- | ---------------------------------------------------- |
| `+0x00` | u32                  | row_count | Number of rows; 2,001 (levels 0 to 2000) on client 3464 |
| `+0x04` | Level Row[row_count] | rows      | `row_count` rows of 16 bytes, not in level order     |

The rows fill the file exactly: 4 + 2,001 x 16 = 32,020 bytes on client 3464.

### Level Row (16 bytes)

| Offset  | Type | Field                   | Notes                                                    |
| ------- | ---- | ----------------------- | -------------------------------------------------------- |
| `+0x00` | u16  | level                   | Skill point level; equals the offset row's key           |
| `+0x02` | u16  | acquired_point          | `0` on every row (client 3474)                           |
| `+0x04` | u32  | exp                     | EXP to go from `level` to `level + 1` (Notes)            |
| `+0x08` | u32  | require_exp_limit       | `0` on every row (client 3474)                           |
| `+0x0C` | u32  | quest_require_exp_limit | `0` on every row (client 3474)                           |

The server rejects a row whose `exp`, `require_exp_limit` or `quest_require_exp_limit` is below 0 (Field Names), so the three fit an i32.

### `skillexperienceoffset.dbss`

Index into `skillexperience.dbss`: the bare u16 offset table of `_common/pabr_offset.py` (`parse_bare_offset_rows`), with no `PABR` magic and no trailer.

| Offset  | Type                  | Field     | Notes                                         |
| ------- | --------------------- | --------- | --------------------------------------------- |
| `+0x00` | u32                   | row_count | Equals the `skillexperience.dbss` row count   |
| `+0x04` | Offset Row[row_count] | rows      | `row_count` rows of 10 bytes                  |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                             |
| ------- | ---- | ----------- | ----------------------------------------------------------------- |
| `+0x00` | u16  | level       | Level of the row it points at                                     |
| `+0x02` | u32  | data_offset | Absolute byte offset of the row's `level` in `skillexperience.dbss` |
| `+0x06` | u32  | data_size   | Always 16                                                         |

Neither file keeps level order: the offset rows start with levels 0, 399, 1052, and the first data row (`0x04`) is level 1052. The parser reads every row through the offset table, checks that the row's `level` matches the offset row's key, and returns the rows sorted by level.

## Field Names

The names come from the server dump of a private server on client 1784 (`Instance_dumpFull.exe`). It loads the row twice into one static status: from the client's `skillexperience.dbss` (row reader at VA `0x140c84990`) and from the `SkillPointEXP_Table_New` developer sheet (column reads at VA `0x1408c2c87` to `0x1408c2d39`). Both write the same members:

| Field                     | Member  | Read from the file | Sheet column           |
| ------------------------- | ------- | ------------------ | ---------------------- |
| `level`                   | `+0x00` | u16                | `Index`                |
| `acquired_point`          | `+0x02` | u16                | `AquiredPoint`         |
| `exp`                     | `+0x04` | u32                | `RequireEXP`           |
| `require_exp_limit`       | `+0x08` | u32                | `RequireSkillExpLimit` |
| `quest_require_exp_limit` | `+0x0C` | u32                | `QuestRequireExpLimit` |

The row check (from VA `0x140c84702`) stores the key, then tests the three EXP members in member order and logs, for the first one below 0, "skill point level key(%#): (%#) EXP is not defined", "... the current level's max (%#) EXP is not defined" or "... the current level's quest max (%#) EXP is not defined". Only a row that passes gets a flag at member `+0x10`, which the file does not store. [guildskillexperience](guildskillexperience_dbss.md) and [productexperience](productexperience_dbss.md) store that flag as their last byte (`is_exp_defined`).

The sheet and the private server's own `skillexperience.dbss` hold the same 2,001 rows as client 3474: `exp` matches on every level, and `AquiredPoint`, `RequireSkillExpLimit` and `QuestRequireExpLimit` are `0` on every row of all three. Earlier versions of this doc read `+0x00` as a u32 level and `+0x04` as a u64 EXP; with those zero fields the values are the same, so only the field bounds changed.

## Notes

- The client has three skill point pools, numbered by `ToClient_getSkillPointInfo(type)`: `0` combat skill points (`panel_window_skillgroup_all_1.luac`), `2` life skill points (`panel_selfplayerexpgage.luac`) and `3` guild points (`panel_guildskill_all_1.luac`). `acquire.luac` names the matching level-up notices `GainCombatSkillPoint`, `GainProductSkillPoint` and `GainGuildSkillPoint`, shown with the `GAME` keys `ACQUIRE_OBJECTMESSAGE_2` ("Combat Skill Points Obtained"), `_1` ("Life Skill Points Obtained") and `_3` ("Guild Points Obtained"). The file stems follow the same names: `skillexperience`, `productexperience`, `guildskillexperience`.
- The skill window draws the bar as `getSkillPointExperience() / getSkillPointNeedExperience()`, and the guild window as `_currentExp / _nextLevelExp`, so the EXP restarts at 0 on every level, as in [lifeexp](lifeexp_dbss.md). The row direction (row N is the EXP from N to N + 1) follows `lifeexp.dbss`, where a packet capture confirmed it; a capture of the Skill EXP message against this table would flip it if the client divides by the level N + 1 row instead.
- Quest rewards of type `__eRewardSkillExp` give `_skillExperience` (`panel_dialog_quest_all_1.luac`), shown as "Skill EXP" (`LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP`).
- Curve on client 3464: level N needs 430 + 1,120 x N x (N + 1) EXP up to level 249 (69,720,430), then 557,760 more per level up to level 500 (209,718,190). Levels 501 to 1501 hold that same 209,718,190, and levels 1502 to 2000 ten times it, 2,097,181,900.
- Unlike `lifeexp.dbss` the file has no blocks and the rows open with a u16 level instead of a type byte; the offset table is the bare 10-byte layout that `petexpoffset.dbss` also uses.

## Open Questions

### What the Two EXP Limits Cap

`require_exp_limit` and `quest_require_exp_limit` are `0` on every row of client 3474 and of the 1784 sheet, and the skill window Lua reads only the current and needed EXP (`getSkillPointExperience()`, `getSkillPointNeedExperience()`). The Korean check messages call them the current level's max EXP and quest max EXP; what a non-zero value would cap needs a client where one is set.
