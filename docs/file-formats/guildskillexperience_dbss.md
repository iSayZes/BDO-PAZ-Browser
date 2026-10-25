# `guildskillexperience.dbss` Format

## Purpose

EXP table of the guild points (skill point pool `3`, the points guild skills cost): the EXP a guild needs to go from one guild point level to the next, from level 0 to the max level in [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md) (`guildskillexperiencemaxlevel.bss`). Companion `guildskillexperienceoffset.dbss` lists where every row sits. The container and offset table are the ones of [skillexperience](skillexperience_dbss.md); only the row differs.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                              | Bytes  | Records          | Row bytes |
| ------ | -------------- | --------------------------------- | ------ | ---------------- | --------- |
| 1      | 1276 and later | `guildskillexperience.dbss`       | 13,017 | 1,001 Level Row  | 13        |
| 1      | 1276 and later | `guildskillexperienceoffset.dbss` | 10,014 | 1,001 Offset Row | 10        |

| Layout | File                              | Known             | Unknown    |
| ------ | --------------------------------- | ----------------- | ---------- |
| 1      | `guildskillexperience.dbss`       | 13,017 B (100.0%) | 0 B (0.0%) |
| 1      | `guildskillexperienceoffset.dbss` | 10,014 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `425bf9534d8e`  |
| 3482   | Layout 1 | `425bf9534d8e`  |
| 3474   | Layout 1 | `425bf9534d8e`  |
| 3473   | Layout 1 | `425bf9534d8e`  |
| 3464   | Layout 1 | `425bf9534d8e`  |
| 3458   | Layout 1 | `425bf9534d8e`  |
| 3454   | Layout 1 | `425bf9534d8e`  |
| 3444   | Layout 1 | `425bf9534d8e`  |
| 3435   | Layout 1 | `425bf9534d8e`  |
| 3426   | Layout 1 | `425bf9534d8e`  |
| 3418   | Layout 1 | `425bf9534d8e`  |
| 3412   | Layout 1 | `425bf9534d8e`  |
| 3402   | Layout 1 | `425bf9534d8e`  |
| 3396   | Layout 1 | `425bf9534d8e`  |
| 3387   | Layout 1 | `425bf9534d8e`  |
| 3381   | Layout 1 | `425bf9534d8e`  |
| 3373   | Layout 1 | `425bf9534d8e`  |
| 3364   | Layout 1 | `425bf9534d8e`  |
| 3356   | Layout 1 | `425bf9534d8e`  |
| 3349   | Layout 1 | `425bf9534d8e`  |
| 3342   | Layout 1 | `425bf9534d8e`  |
| 3335   | Layout 1 | `425bf9534d8e`  |
| 3326   | Layout 1 | `425bf9534d8e`  |
| 3321   | Layout 1 | `425bf9534d8e`  |
| 3314   | Layout 1 | `425bf9534d8e`  |
| 3303   | Layout 1 | `425bf9534d8e`  |
| 3302   | Layout 1 | `425bf9534d8e`  |
| 3293   | Layout 1 | `425bf9534d8e`  |
| 3283   | Layout 1 | `425bf9534d8e`  |
| 3275   | Layout 1 | `425bf9534d8e`  |
| 3267   | Layout 1 | `425bf9534d8e`  |
| 3258   | Layout 1 | `425bf9534d8e`  |
| 3251   | Layout 1 | `425bf9534d8e`  |
| 3242   | Layout 1 | `425bf9534d8e`  |
| 3235   | Layout 1 | `425bf9534d8e`  |
| 3229   | Layout 1 | `425bf9534d8e`  |
| 3212   | Layout 1 | `425bf9534d8e`  |
| 3203   | Layout 1 | `425bf9534d8e`  |
| 3193   | Layout 1 | `425bf9534d8e`  |
| 3186   | Layout 1 | `425bf9534d8e`  |
| 3177   | Layout 1 | `425bf9534d8e`  |
| 3169   | Layout 1 | `425bf9534d8e`  |
| 3158   | Layout 1 | `425bf9534d8e`  |
| 3151   | Layout 1 | `425bf9534d8e`  |
| 3144   | Layout 1 | `425bf9534d8e`  |
| 3133   | Layout 1 | `425bf9534d8e`  |
| 3125   | Layout 1 | `425bf9534d8e`  |
| 3118   | Layout 1 | `425bf9534d8e`  |
| 3111   | Layout 1 | `425bf9534d8e`  |
| 3103   | Layout 1 | `425bf9534d8e`  |
| 3095   | Layout 1 | `425bf9534d8e`  |
| 3086   | Layout 1 | `425bf9534d8e`  |
| 3072   | Layout 1 | `425bf9534d8e`  |
| 3062   | Layout 1 | `425bf9534d8e`  |
| 3052   | Layout 1 | `425bf9534d8e`  |
| 3045   | Layout 1 | `425bf9534d8e`  |
| 3037   | Layout 1 | `425bf9534d8e`  |
| 3030   | Layout 1 | `425bf9534d8e`  |
| 3021   | Layout 1 | `425bf9534d8e`  |
| 3012   | Layout 1 | `425bf9534d8e`  |
| 3002   | Layout 1 | `425bf9534d8e`  |
| 2995   | Layout 1 | `425bf9534d8e`  |
| 2987   | Layout 1 | `425bf9534d8e`  |
| 2978   | Layout 1 | `425bf9534d8e`  |
| 2970   | Layout 1 | `425bf9534d8e`  |
| 2959   | Layout 1 | `425bf9534d8e`  |
| 2951   | Layout 1 | `425bf9534d8e`  |
| 2942   | Layout 1 | `425bf9534d8e`  |
| 2935   | Layout 1 | `425bf9534d8e`  |
| 2932   | Layout 1 | `425bf9534d8e`  |
| 2923   | Layout 1 | `425bf9534d8e`  |
| 2919   | Layout 1 | `425bf9534d8e`  |
| 2907   | Layout 1 | `425bf9534d8e`  |
| 2900   | Layout 1 | `425bf9534d8e`  |
| 2891   | Layout 1 | `425bf9534d8e`  |
| 2882   | Layout 1 | `425bf9534d8e`  |
| 2872   | Layout 1 | `425bf9534d8e`  |
| 2863   | Layout 1 | `425bf9534d8e`  |
| 2855   | Layout 1 | `425bf9534d8e`  |
| 2849   | Layout 1 | `425bf9534d8e`  |
| 2844   | Layout 1 | `425bf9534d8e`  |
| 2834   | Layout 1 | `425bf9534d8e`  |
| 2825   | Layout 1 | `425bf9534d8e`  |
| 2819   | Layout 1 | `425bf9534d8e`  |
| 2811   | Layout 1 | `425bf9534d8e`  |
| 2803   | Layout 1 | `425bf9534d8e`  |
| 2794   | Layout 1 | `425bf9534d8e`  |
| 2783   | Layout 1 | `425bf9534d8e`  |
| 2774   | Layout 1 | `425bf9534d8e`  |
| 2765   | Layout 1 | `425bf9534d8e`  |
| 2756   | Layout 1 | `425bf9534d8e`  |
| 2750   | Layout 1 | `425bf9534d8e`  |
| 2743   | Layout 1 | `425bf9534d8e`  |
| 2736   | Layout 1 | `425bf9534d8e`  |
| 2726   | Layout 1 | `425bf9534d8e`  |
| 2717   | Layout 1 | `425bf9534d8e`  |
| 2709   | Layout 1 | `425bf9534d8e`  |
| 2703   | Layout 1 | `425bf9534d8e`  |
| 2695   | Layout 1 | `425bf9534d8e`  |
| 2684   | Layout 1 | `425bf9534d8e`  |
| 2672   | Layout 1 | `425bf9534d8e`  |
| 2665   | Layout 1 | `425bf9534d8e`  |
| 2657   | Layout 1 | `425bf9534d8e`  |
| 2649   | Layout 1 | `425bf9534d8e`  |
| 2644   | Layout 1 | `425bf9534d8e`  |
| 2637   | Layout 1 | `425bf9534d8e`  |
| 2629   | Layout 1 | `425bf9534d8e`  |
| 2619   | Layout 1 | `425bf9534d8e`  |
| 2612   | Layout 1 | `425bf9534d8e`  |
| 2606   | Layout 1 | `425bf9534d8e`  |
| 2602   | Layout 1 | `425bf9534d8e`  |
| 2601   | Layout 1 | `425bf9534d8e`  |
| 2592   | Layout 1 | `425bf9534d8e`  |
| 2583   | Layout 1 | `425bf9534d8e`  |
| 2575   | Layout 1 | `425bf9534d8e`  |
| 2567   | Layout 1 | `425bf9534d8e`  |
| 2560   | Layout 1 | `425bf9534d8e`  |
| 2553   | Layout 1 | `425bf9534d8e`  |
| 2545   | Layout 1 | `425bf9534d8e`  |
| 2538   | Layout 1 | `425bf9534d8e`  |
| 2529   | Layout 1 | `425bf9534d8e`  |
| 2519   | Layout 1 | `425bf9534d8e`  |
| 2513   | Layout 1 | `425bf9534d8e`  |
| 2510   | Layout 1 | `425bf9534d8e`  |
| 2507   | Layout 1 | `425bf9534d8e`  |
| 2503   | Layout 1 | `425bf9534d8e`  |
| 2498   | Layout 1 | `425bf9534d8e`  |
| 2492   | Layout 1 | `425bf9534d8e`  |
| 2487   | Layout 1 | `425bf9534d8e`  |
| 2480   | Layout 1 | `425bf9534d8e`  |
| 2474   | Layout 1 | `425bf9534d8e`  |
| 2468   | Layout 1 | `425bf9534d8e`  |
| 2460   | Layout 1 | `425bf9534d8e`  |
| 2453   | Layout 1 | `425bf9534d8e`  |
| 2444   | Layout 1 | `425bf9534d8e`  |
| 2438   | Layout 1 | `425bf9534d8e`  |
| 2434   | Layout 1 | `425bf9534d8e`  |
| 2429   | Layout 1 | `425bf9534d8e`  |
| 2421   | Layout 1 | `425bf9534d8e`  |
| 2414   | Layout 1 | `425bf9534d8e`  |
| 2407   | Layout 1 | `425bf9534d8e`  |
| 2401   | Layout 1 | `425bf9534d8e`  |
| 2397   | Layout 1 | `425bf9534d8e`  |
| 2393   | Layout 1 | `425bf9534d8e`  |
| 2384   | Layout 1 | `425bf9534d8e`  |
| 2378   | Layout 1 | `425bf9534d8e`  |
| 2372   | Layout 1 | `425bf9534d8e`  |
| 2358   | Layout 1 | `425bf9534d8e`  |
| 2352   | Layout 1 | `425bf9534d8e`  |
| 2347   | Layout 1 | `425bf9534d8e`  |
| 2343   | Layout 1 | `425bf9534d8e`  |
| 2335   | Layout 1 | `425bf9534d8e`  |
| 2327   | Layout 1 | `425bf9534d8e`  |
| 2324   | Layout 1 | `425bf9534d8e`  |
| 2319   | Layout 1 | `425bf9534d8e`  |
| 2313   | Layout 1 | `425bf9534d8e`  |
| 2308   | Layout 1 | `425bf9534d8e`  |
| 2302   | Layout 1 | `425bf9534d8e`  |
| 2295   | Layout 1 | `425bf9534d8e`  |
| 2290   | Layout 1 | `425bf9534d8e`  |
| 2284   | Layout 1 | `425bf9534d8e`  |
| 2276   | Layout 1 | `425bf9534d8e`  |
| 2269   | Layout 1 | `425bf9534d8e`  |
| 2259   | Layout 1 | `425bf9534d8e`  |
| 2250   | Layout 1 | `425bf9534d8e`  |
| 2243   | Layout 1 | `425bf9534d8e`  |
| 2235   | Layout 1 | `425bf9534d8e`  |
| 2229   | Layout 1 | `425bf9534d8e`  |
| 2224   | Layout 1 | `425bf9534d8e`  |
| 2218   | Layout 1 | `425bf9534d8e`  |
| 2215   | Layout 1 | `425bf9534d8e`  |
| 2207   | Layout 1 | `425bf9534d8e`  |
| 2203   | Layout 1 | `425bf9534d8e`  |
| 2196   | Layout 1 | `425bf9534d8e`  |
| 2192   | Layout 1 | `425bf9534d8e`  |
| 2189   | Layout 1 | `425bf9534d8e`  |
| 2183   | Layout 1 | `425bf9534d8e`  |
| 2179   | Layout 1 | `425bf9534d8e`  |
| 2171   | Layout 1 | `425bf9534d8e`  |
| 2163   | Layout 1 | `425bf9534d8e`  |
| 2156   | Layout 1 | `425bf9534d8e`  |
| 2151   | Layout 1 | `425bf9534d8e`  |
| 2147   | Layout 1 | `425bf9534d8e`  |
| 2142   | Layout 1 | `425bf9534d8e`  |
| 2138   | Layout 1 | `425bf9534d8e`  |
| 2134   | Layout 1 | `425bf9534d8e`  |
| 2130   | Layout 1 | `425bf9534d8e`  |
| 2122   | Layout 1 | `425bf9534d8e`  |
| 2107   | Layout 1 | `425bf9534d8e`  |
| 2098   | Layout 1 | `425bf9534d8e`  |
| 2089   | Layout 1 | `425bf9534d8e`  |
| 2081   | Layout 1 | `425bf9534d8e`  |
| 2073   | Layout 1 | `425bf9534d8e`  |
| 2067   | Layout 1 | `425bf9534d8e`  |
| 2063   | Layout 1 | `425bf9534d8e`  |
| 2059   | Layout 1 | `425bf9534d8e`  |
| 2052   | Layout 1 | `425bf9534d8e`  |
| 2044   | Layout 1 | `425bf9534d8e`  |
| 2039   | Layout 1 | `425bf9534d8e`  |
| 2032   | Layout 1 | `425bf9534d8e`  |
| 2025   | Layout 1 | `425bf9534d8e`  |
| 2011   | Layout 1 | `425bf9534d8e`  |
| 2005   | Layout 1 | `425bf9534d8e`  |
| 2000   | Layout 1 | `425bf9534d8e`  |
| 1996   | Layout 1 | `425bf9534d8e`  |
| 1991   | Layout 1 | `425bf9534d8e`  |
| 1985   | Layout 1 | `425bf9534d8e`  |
| 1980   | Layout 1 | `425bf9534d8e`  |
| 1969   | Layout 1 | `425bf9534d8e`  |
| 1964   | Layout 1 | `425bf9534d8e`  |
| 1958   | Layout 1 | `425bf9534d8e`  |
| 1950   | Layout 1 | `425bf9534d8e`  |
| 1945   | Layout 1 | `425bf9534d8e`  |
| 1937   | Layout 1 | `425bf9534d8e`  |
| 1933   | Layout 1 | `425bf9534d8e`  |
| 1927   | Layout 1 | `425bf9534d8e`  |
| 1921   | Layout 1 | `425bf9534d8e`  |
| 1914   | Layout 1 | `425bf9534d8e`  |
| 1908   | Layout 1 | `425bf9534d8e`  |
| 1897   | Layout 1 | `425bf9534d8e`  |
| 1892   | Layout 1 | `425bf9534d8e`  |
| 1886   | Layout 1 | `425bf9534d8e`  |
| 1881   | Layout 1 | `425bf9534d8e`  |
| 1871   | Layout 1 | `425bf9534d8e`  |
| 1866   | Layout 1 | `425bf9534d8e`  |
| 1862   | Layout 1 | `425bf9534d8e`  |
| 1854   | Layout 1 | `425bf9534d8e`  |
| 1846   | Layout 1 | `425bf9534d8e`  |
| 1838   | Layout 1 | `425bf9534d8e`  |
| 1832   | Layout 1 | `425bf9534d8e`  |
| 1826   | Layout 1 | `425bf9534d8e`  |
| 1822   | Layout 1 | `425bf9534d8e`  |
| 1818   | Layout 1 | `425bf9534d8e`  |
| 1804   | Layout 1 | `425bf9534d8e`  |
| 1794   | Layout 1 | `425bf9534d8e`  |
| 1790   | Layout 1 | `425bf9534d8e`  |
| 1784   | Layout 1 | `425bf9534d8e`  |
| 1774   | Layout 1 | `425bf9534d8e`  |
| 1771   | Layout 1 | `425bf9534d8e`  |
| 1762   | Layout 1 | `425bf9534d8e`  |
| 1759   | Layout 1 | `425bf9534d8e`  |
| 1754   | Layout 1 | `425bf9534d8e`  |
| 1749   | Layout 1 | `425bf9534d8e`  |
| 1743   | Layout 1 | `425bf9534d8e`  |
| 1737   | Layout 1 | `425bf9534d8e`  |
| 1731   | Layout 1 | `425bf9534d8e`  |
| 1725   | Layout 1 | `425bf9534d8e`  |
| 1717   | Layout 1 | `425bf9534d8e`  |
| 1710   | Layout 1 | `425bf9534d8e`  |
| 1704   | Layout 1 | `425bf9534d8e`  |
| 1698   | Layout 1 | `425bf9534d8e`  |
| 1690   | Layout 1 | `425bf9534d8e`  |
| 1685   | Layout 1 | `425bf9534d8e`  |
| 1680   | Layout 1 | `425bf9534d8e`  |
| 1674   | Layout 1 | `425bf9534d8e`  |
| 1668   | Layout 1 | `425bf9534d8e`  |
| 1659   | Layout 1 | `425bf9534d8e`  |
| 1649   | Layout 1 | `425bf9534d8e`  |
| 1642   | Layout 1 | `425bf9534d8e`  |
| 1636   | Layout 1 | `425bf9534d8e`  |
| 1628   | Layout 1 | `425bf9534d8e`  |
| 1622   | Layout 1 | `425bf9534d8e`  |
| 1614   | Layout 1 | `425bf9534d8e`  |
| 1608   | Layout 1 | `425bf9534d8e`  |
| 1602   | Layout 1 | `425bf9534d8e`  |
| 1598   | Layout 1 | `425bf9534d8e`  |
| 1594   | Layout 1 | `425bf9534d8e`  |
| 1590   | Layout 1 | `425bf9534d8e`  |
| 1587   | Layout 1 | `425bf9534d8e`  |
| 1584   | Layout 1 | `425bf9534d8e`  |
| 1579   | Layout 1 | `425bf9534d8e`  |
| 1572   | Layout 1 | `425bf9534d8e`  |
| 1565   | Layout 1 | `425bf9534d8e`  |
| 1559   | Layout 1 | `425bf9534d8e`  |
| 1554   | Layout 1 | `425bf9534d8e`  |
| 1547   | Layout 1 | `425bf9534d8e`  |
| 1537   | Layout 1 | `425bf9534d8e`  |
| 1529   | Layout 1 | `425bf9534d8e`  |
| 1524   | Layout 1 | `425bf9534d8e`  |
| 1519   | Layout 1 | `425bf9534d8e`  |
| 1509   | Layout 1 | `425bf9534d8e`  |
| 1506   | Layout 1 | `425bf9534d8e`  |
| 1504   | Layout 1 | `425bf9534d8e`  |
| 1500   | Layout 1 | `425bf9534d8e`  |
| 1493   | Layout 1 | `425bf9534d8e`  |
| 1489   | Layout 1 | `425bf9534d8e`  |
| 1485   | Layout 1 | `425bf9534d8e`  |
| 1481   | Layout 1 | `425bf9534d8e`  |
| 1474   | Layout 1 | `425bf9534d8e`  |
| 1466   | Layout 1 | `425bf9534d8e`  |
| 1462   | Layout 1 | `425bf9534d8e`  |
| 1459   | Layout 1 | `425bf9534d8e`  |
| 1453   | Layout 1 | `425bf9534d8e`  |
| 1450   | Layout 1 | `425bf9534d8e`  |
| 1445   | Layout 1 | `425bf9534d8e`  |
| 1439   | Layout 1 | `425bf9534d8e`  |
| 1433   | Layout 1 | `425bf9534d8e`  |
| 1430   | Layout 1 | `425bf9534d8e`  |
| 1426   | Layout 1 | `425bf9534d8e`  |
| 1421   | Layout 1 | `425bf9534d8e`  |
| 1417   | Layout 1 | `425bf9534d8e`  |
| 1416   | Layout 1 | `425bf9534d8e`  |
| 1409   | Layout 1 | `425bf9534d8e`  |
| 1405   | Layout 1 | `425bf9534d8e`  |
| 1401   | Layout 1 | `425bf9534d8e`  |
| 1396   | Layout 1 | `425bf9534d8e`  |
| 1391   | Layout 1 | `425bf9534d8e`  |
| 1390   | Layout 1 | `425bf9534d8e`  |
| 1386   | Layout 1 | `425bf9534d8e`  |
| 1381   | Layout 1 | `425bf9534d8e`  |
| 1379   | Layout 1 | `425bf9534d8e`  |
| 1372   | Layout 1 | `425bf9534d8e`  |
| 1366   | Layout 1 | `425bf9534d8e`  |
| 1364   | Layout 1 | `425bf9534d8e`  |
| 1363   | Layout 1 | `425bf9534d8e`  |
| 1360   | Layout 1 | `425bf9534d8e`  |
| 1358   | Layout 1 | `425bf9534d8e`  |
| 1355   | Layout 1 | `425bf9534d8e`  |
| 1351   | Layout 1 | `425bf9534d8e`  |
| 1348   | Layout 1 | `425bf9534d8e`  |
| 1346   | Layout 1 | `425bf9534d8e`  |
| 1341   | Layout 1 | `425bf9534d8e`  |
| 1340   | Layout 1 | `425bf9534d8e`  |
| 1338   | Layout 1 | `425bf9534d8e`  |
| 1335   | Layout 1 | `425bf9534d8e`  |
| 1333   | Layout 1 | `425bf9534d8e`  |
| 1329   | Layout 1 | `425bf9534d8e`  |
| 1327   | Layout 1 | `425bf9534d8e`  |
| 1324   | Layout 1 | `425bf9534d8e`  |
| 1321   | Layout 1 | `425bf9534d8e`  |
| 1319   | Layout 1 | `425bf9534d8e`  |
| 1318   | Layout 1 | `425bf9534d8e`  |
| 1316   | Layout 1 | `425bf9534d8e`  |
| 1313   | Layout 1 | `425bf9534d8e`  |
| 1311   | Layout 1 | `425bf9534d8e`  |
| 1309   | Layout 1 | `425bf9534d8e`  |
| 1304   | Layout 1 | `425bf9534d8e`  |
| 1292   | Layout 1 | `425bf9534d8e`  |
| 1286   | Layout 1 | `425bf9534d8e`  |
| 1280   | Layout 1 | `425bf9534d8e`  |
| 1276   | Layout 1 | `425bf9534d8e`  |
| 1267   | No file  | `425bf9534d8e`  |
| 1261   | No file  | `425bf9534d8e`  |
| 1256   | No file  | `425bf9534d8e`  |
| 1250   | No file  | `425bf9534d8e`  |
| 1246   | No file  | `425bf9534d8e`  |
| 1239   | No file  | `425bf9534d8e`  |
| 1230   | No file  | `425bf9534d8e`  |
| 1226   | No file  | `425bf9534d8e`  |
| 1220   | No file  | `425bf9534d8e`  |
| 1217   | No file  | `425bf9534d8e`  |
| 1211   | No file  | `425bf9534d8e`  |
| 1210   | No file  | `425bf9534d8e`  |
| 1208   | No file  | `425bf9534d8e`  |
| 1203   | No file  | `425bf9534d8e`  |
| 1197   | No file  | `425bf9534d8e`  |
| 1194   | No file  | `425bf9534d8e`  |
| 1192   | No file  | `425bf9534d8e`  |
| 1187   | No file  | `425bf9534d8e`  |
| 1183   | No file  | `425bf9534d8e`  |
| 1177   | No file  | `425bf9534d8e`  |
| 1173   | No file  | `425bf9534d8e`  |
| 1167   | No file  | `425bf9534d8e`  |
| 1164   | No file  | `425bf9534d8e`  |
| 1156   | No file  | `425bf9534d8e`  |
| 1149   | No file  | `425bf9534d8e`  |
| 1144   | No file  | `425bf9534d8e`  |
| 1137   | No file  | `425bf9534d8e`  |
| 1132   | No file  | `425bf9534d8e`  |
| 1127   | No file  | `425bf9534d8e`  |
| 1122   | No file  | `425bf9534d8e`  |
| 1118   | No file  | `425bf9534d8e`  |
| 1114   | No file  | `425bf9534d8e`  |
| 1109   | No file  | `425bf9534d8e`  |
| 1102   | No file  | `425bf9534d8e`  |
| 1096   | No file  | `425bf9534d8e`  |
| 1088   | No file  | `425bf9534d8e`  |
| 1081   | No file  | `425bf9534d8e`  |
| 1076   | No file  | `425bf9534d8e`  |
| 1069   | No file  | `425bf9534d8e`  |
| 1064   | No file  | `425bf9534d8e`  |
| 1058   | No file  | `425bf9534d8e`  |
| 1051   | No file  | `425bf9534d8e`  |
| 1044   | No file  | `425bf9534d8e`  |
| 1036   | No file  | `425bf9534d8e`  |
| 1026   | No file  | `425bf9534d8e`  |
| 1016   | No file  | `425bf9534d8e`  |
| 1009   | No file  | `425bf9534d8e`  |
| 1005   | No file  | `425bf9534d8e`  |
| 1000   | No file  | `425bf9534d8e`  |
| 998    | No file  | `425bf9534d8e`  |
| 990    | No file  | `425bf9534d8e`  |
| 979    | No file  | `425bf9534d8e`  |
| 972    | No file  | `425bf9534d8e`  |
| 963    | No file  | `425bf9534d8e`  |
| 955    | No file  | `425bf9534d8e`  |
| 946    | No file  | `425bf9534d8e`  |
| 938    | No file  | `425bf9534d8e`  |
| 927    | No file  | `425bf9534d8e`  |
| 911    | No file  | `425bf9534d8e`  |
| 904    | No file  | `425bf9534d8e`  |
| 899    | No file  | `425bf9534d8e`  |
| 894    | No file  | `425bf9534d8e`  |
| 885    | No file  | `425bf9534d8e`  |
| 879    | No file  | `425bf9534d8e`  |
| 872    | No file  | `425bf9534d8e`  |
| 864    | No file  | `425bf9534d8e`  |
| 855    | No file  | `425bf9534d8e`  |
| 853    | No file  | `425bf9534d8e`  |
| 845    | No file  | `425bf9534d8e`  |
| 837    | No file  | `425bf9534d8e`  |
| 829    | No file  | `425bf9534d8e`  |
| 822    | No file  | `425bf9534d8e`  |
| 814    | No file  | `425bf9534d8e`  |
| 805    | No file  | `425bf9534d8e`  |
| 794    | No file  | `425bf9534d8e`  |
| 787    | No file  | `425bf9534d8e`  |
| 780    | No file  | `425bf9534d8e`  |
| 771    | No file  | `425bf9534d8e`  |
| 760    | No file  | `425bf9534d8e`  |
| 748    | No file  | `425bf9534d8e`  |
| 741    | No file  | `425bf9534d8e`  |
| 736    | No file  | `425bf9534d8e`  |
| 731    | No file  | `425bf9534d8e`  |
| 723    | No file  | `425bf9534d8e`  |
| 711    | No file  | `425bf9534d8e`  |
| 707    | No file  | `425bf9534d8e`  |
| 697    | No file  | `425bf9534d8e`  |
| 689    | No file  | `425bf9534d8e`  |
| 683    | No file  | `425bf9534d8e`  |
| 678    | No file  | `425bf9534d8e`  |
| 670    | No file  | `425bf9534d8e`  |
| 661    | No file  | `425bf9534d8e`  |
| 656    | No file  | `425bf9534d8e`  |
| 652    | No file  | `425bf9534d8e`  |
| 643    | No file  | `425bf9534d8e`  |
| 637    | No file  | `425bf9534d8e`  |
| 630    | No file  | `425bf9534d8e`  |
| 627    | No file  | `425bf9534d8e`  |
| 621    | No file  | `425bf9534d8e`  |
| 617    | No file  | `425bf9534d8e`  |
| 615    | No file  | `425bf9534d8e`  |
| 606    | No file  | `425bf9534d8e`  |
| 599    | No file  | `425bf9534d8e`  |
| 592    | No file  | `425bf9534d8e`  |
| 586    | No file  | `425bf9534d8e`  |
| 577    | No file  | `425bf9534d8e`  |
| 569    | No file  | `425bf9534d8e`  |
| 561    | No file  | `425bf9534d8e`  |
| 554    | No file  | `425bf9534d8e`  |
| 542    | No file  | `425bf9534d8e`  |
| 532    | No file  | `425bf9534d8e`  |
| 531    | No file  | `425bf9534d8e`  |
| 526    | No file  | `425bf9534d8e`  |
| 521    | No file  | `425bf9534d8e`  |
| 517    | No file  | `425bf9534d8e`  |
| 510    | No file  | `425bf9534d8e`  |
| 508    | No file  | `425bf9534d8e`  |
| 504    | No file  | `425bf9534d8e`  |
| 497    | No file  | `425bf9534d8e`  |
| 491    | No file  | `425bf9534d8e`  |
| 485    | No file  | `425bf9534d8e`  |
| 478    | No file  | `425bf9534d8e`  |
| 472    | No file  | `425bf9534d8e`  |
| 466    | No file  | `425bf9534d8e`  |
| 457    | No file  | `425bf9534d8e`  |
| 452    | No file  | `425bf9534d8e`  |
| 449    | No file  | `425bf9534d8e`  |
| 435    | No file  | `425bf9534d8e`  |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                                     |
| ---------------------------------- | -------- | ------------------------------------------------------------------------ |
| `guildskillexperienceoffset.dbss`  | Required | `level -> (offset, size)` of every row                                   |
| `guildskillexperiencemaxlevel.bss` | Optional | Max level, see [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                 | Field     | Notes                                                   |
| ------- | -------------------- | --------- | ------------------------------------------------------- |
| `+0x00` | u32                  | row_count | Number of rows; 1,001 (levels 0 to 1000) on client 3464 |
| `+0x04` | Level Row[row_count] | rows      | See Level Row; not in level order                       |

The rows fill the file exactly: 4 + 1,001 x 13 = 13,017 bytes on client 3464.

### Level Row (13 bytes)

| Offset  | Type | Field             | Notes                                                    |
| ------- | ---- | ----------------- | -------------------------------------------------------- |
| `+0x00` | u16  | level             | Guild point level; equals the offset row's key           |
| `+0x02` | u16  | acquired_point    | `0` on every row (client 3474)                           |
| `+0x04` | u32  | exp               | EXP to go from `level` to `level + 1`, as in [skillexperience](skillexperience_dbss.md) |
| `+0x08` | u32  | require_exp_limit | `0` on every row (client 3474)                           |
| `+0x0C` | u8   | is_exp_defined    | `1` on every row (client 3474); see Field Names          |

### `guildskillexperienceoffset.dbss`

The layout of `skillexperienceoffset.dbss` (see [skillexperience](skillexperience_dbss.md)), with no magic and no trailer.

| Offset  | Type                  | Field     | Notes                              |
| ------- | --------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                   | row_count | Equals the main file's `row_count` |
| `+0x04` | Offset Row[row_count] | rows      | See Offset Row                     |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                          |
| ------- | ---- | ----------- | ------------------------------------------------------------------------------ |
| `+0x00` | u16  | level       | Level of the row it points at                                                  |
| `+0x02` | u32  | data_offset | Absolute byte offset of the row's `level` in `guildskillexperience.dbss`       |
| `+0x06` | u32  | data_size   | Always 13                                                                      |

The rows are not in level order (0, 399, 944, ...); the parser returns the main rows sorted by level.

## Field Names

The row is the `GuildSkillPointEXP_Table` sheet of a private server on client 1784, read the way its server dump (`Instance_dumpFull.exe`) reads it. The dump fills one static status from the client's `guildskillexperience.dbss` (row reader at VA `0x140ae1f20`) and from the sheet (column reads at VA `0x1408c33c4` to `0x1408c3458`):

| Field               | Member  | Read from the file | Sheet column           |
| ------------------- | ------- | ------------------ | ---------------------- |
| `level`             | `+0x00` | u16                | `Index`                |
| `acquired_point`    | `+0x02` | u16                | `AquiredPoint`         |
| `exp`               | `+0x04` | u32                | `RequireEXP`           |
| `require_exp_limit` | `+0x08` | u32                | `RequireSkillExpLimit` |
| `is_exp_defined`    | `+0x0C` | u8                 | none                   |

`is_exp_defined` has no sheet column. The sheet loader starts it at `0`, and the row check (VA `0x140ae1c70`) sets it to `1` only when `exp` and `require_exp_limit` are both at least 0; otherwise it logs "guild skill point level key(%#): EXP is not defined" or "... the current level's max EXP is not defined". The client file stores the checked flag, `1` on every row. The name follows those messages.

The sheet and the private server's own file hold the same 1,001 rows as client 3474: `exp` matches on every level, `AquiredPoint` and `RequireSkillExpLimit` are `0` on every row. Earlier versions of this doc read `+0x00` as a u32 level and `+0x04` as a u64 EXP; with those zero fields the values are the same.

## Notes

- The guild window (`panel_guildskill_all_1.luac`, `panel_guildinfo_all_1.luac`) reads `ToClient_getSkillPointInfo(3)` and shows `_remainPoint` / `_acquirePoint - 1` with the bar `_currentExp / _nextLevelExp`; `acquire.luac` announces a new point as `GainGuildSkillPoint` with `ACQUIRE_OBJECTMESSAGE_3` ("Guild Points Obtained"). See the [skillexperience](skillexperience_dbss.md) Notes for the three pools and the row direction, which follows `lifeexp.dbss`.
- Curve on client 3464: level N needs (700 + 550 x N) x a multiplier that steps up with the level: x1 on levels 0 to 14, x1.3 on 15 to 20, x1.4 on 21 to 30, x1.5 on 31 to 40, x1.8 on 41 to 49, x2.2 on 50 to 70 and x3 on 71 to 1000. Level 1000 is (700 + 550,000) x 3 = 1,652,100.
