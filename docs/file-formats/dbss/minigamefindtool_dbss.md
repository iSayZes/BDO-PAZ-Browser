# `minigamefindtool.dbss` Format

## Purpose

The hoe values of the Lakiaro digging minigame
([`minigamefind.bss`](../bss/minigamefind_bss.md)): one 9-byte row per hoe item
grade and enhancement level (+0 to PEN), with the number of right clicks,
the slots a click opens and a damage rate. The client Lua asks the table for
the right clicks of the equipped hoe through
`ToClient_MiniGameFindMaxRClickCount(grade, enchantLevel)`. On client 3482
the file holds six grades (0 to 5) of 21 levels each.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes | Records                      | Row bytes |
| ------ | -------------- | ----------------------------- | ----- | ---------------------------- | --------- |
| 2      | 2583 and later | `minigamefindtool.dbss`       | 1,140 | 126 Level Row, 6 Grade Block | 9         |
| 2      | 2583 and later | `minigamefindtooloffset.dbss` | 1,158 | 126 Index Row, 6 Index Group | 9         |
| 1      | 1261 to 2575   | `minigamefindtool.dbss`       | 945   | 105 Level Row, 5 Grade Block | 9         |
| 1      | 1261 to 2575   | `minigamefindtooloffset.dbss` | 965   | 105 Index Row, 5 Index Group | 9         |

| Layout | File                          | Known            | Unknown    |
| ------ | ----------------------------- | ---------------- | ---------- |
| 2      | `minigamefindtool.dbss`       | 1,134 B (99.5%)  | 6 B (0.5%) |
| 2      | `minigamefindtooloffset.dbss` | 1,158 B (100.0%) | 0 B (0.0%) |
| 1      | `minigamefindtool.dbss`       | 945 B (100.0%)   | 0 B (0.0%) |
| 1      | `minigamefindtooloffset.dbss` | 965 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `bd8cd35379c7`  |
| 3482   | Layout 2 | `bd8cd35379c7`  |
| 3474   | Layout 2 | `bd8cd35379c7`  |
| 3473   | Layout 2 | `bd8cd35379c7`  |
| 3464   | Layout 2 | `bd8cd35379c7`  |
| 3458   | Layout 2 | `bd8cd35379c7`  |
| 3454   | Layout 2 | `bd8cd35379c7`  |
| 3444   | Layout 2 | `bd8cd35379c7`  |
| 3435   | Layout 2 | `bd8cd35379c7`  |
| 3426   | Layout 2 | `bd8cd35379c7`  |
| 3418   | Layout 2 | `bd8cd35379c7`  |
| 3412   | Layout 2 | `bd8cd35379c7`  |
| 3402   | Layout 2 | `bd8cd35379c7`  |
| 3396   | Layout 2 | `bd8cd35379c7`  |
| 3387   | Layout 2 | `bd8cd35379c7`  |
| 3381   | Layout 2 | `bd8cd35379c7`  |
| 3373   | Layout 2 | `bd8cd35379c7`  |
| 3364   | Layout 2 | `bd8cd35379c7`  |
| 3356   | Layout 2 | `bd8cd35379c7`  |
| 3349   | Layout 2 | `bd8cd35379c7`  |
| 3342   | Layout 2 | `bd8cd35379c7`  |
| 3335   | Layout 2 | `bd8cd35379c7`  |
| 3326   | Layout 2 | `bd8cd35379c7`  |
| 3321   | Layout 2 | `bd8cd35379c7`  |
| 3314   | Layout 2 | `bd8cd35379c7`  |
| 3303   | Layout 2 | `bd8cd35379c7`  |
| 3302   | Layout 2 | `bd8cd35379c7`  |
| 3293   | Layout 2 | `bd8cd35379c7`  |
| 3283   | Layout 2 | `bd8cd35379c7`  |
| 3275   | Layout 2 | `bd8cd35379c7`  |
| 3267   | Layout 2 | `bd8cd35379c7`  |
| 3258   | Layout 2 | `bd8cd35379c7`  |
| 3251   | Layout 2 | `bd8cd35379c7`  |
| 3242   | Layout 2 | `bd8cd35379c7`  |
| 3235   | Layout 2 | `bd8cd35379c7`  |
| 3229   | Layout 2 | `bd8cd35379c7`  |
| 3212   | Layout 2 | `bd8cd35379c7`  |
| 3203   | Layout 2 | `bd8cd35379c7`  |
| 3193   | Layout 2 | `bd8cd35379c7`  |
| 3186   | Layout 2 | `bd8cd35379c7`  |
| 3177   | Layout 2 | `bd8cd35379c7`  |
| 3169   | Layout 2 | `bd8cd35379c7`  |
| 3158   | Layout 2 | `bd8cd35379c7`  |
| 3151   | Layout 2 | `bd8cd35379c7`  |
| 3144   | Layout 2 | `bd8cd35379c7`  |
| 3133   | Layout 2 | `bd8cd35379c7`  |
| 3125   | Layout 2 | `bd8cd35379c7`  |
| 3118   | Layout 2 | `bd8cd35379c7`  |
| 3111   | Layout 2 | `bd8cd35379c7`  |
| 3103   | Layout 2 | `bd8cd35379c7`  |
| 3095   | Layout 2 | `bd8cd35379c7`  |
| 3086   | Layout 2 | `bd8cd35379c7`  |
| 3072   | Layout 2 | `bd8cd35379c7`  |
| 3062   | Layout 2 | `bd8cd35379c7`  |
| 3052   | Layout 2 | `bd8cd35379c7`  |
| 3045   | Layout 2 | `bd8cd35379c7`  |
| 3037   | Layout 2 | `bd8cd35379c7`  |
| 3030   | Layout 2 | `bd8cd35379c7`  |
| 3021   | Layout 2 | `bd8cd35379c7`  |
| 3012   | Layout 2 | `bd8cd35379c7`  |
| 3002   | Layout 2 | `bd8cd35379c7`  |
| 2995   | Layout 2 | `bd8cd35379c7`  |
| 2987   | Layout 2 | `bd8cd35379c7`  |
| 2978   | Layout 2 | `bd8cd35379c7`  |
| 2970   | Layout 2 | `bd8cd35379c7`  |
| 2959   | Layout 2 | `bd8cd35379c7`  |
| 2951   | Layout 2 | `bd8cd35379c7`  |
| 2942   | Layout 2 | `bd8cd35379c7`  |
| 2935   | Layout 2 | `bd8cd35379c7`  |
| 2932   | Layout 2 | `bd8cd35379c7`  |
| 2923   | Layout 2 | `bd8cd35379c7`  |
| 2919   | Layout 2 | `bd8cd35379c7`  |
| 2907   | Layout 2 | `bd8cd35379c7`  |
| 2900   | Layout 2 | `bd8cd35379c7`  |
| 2891   | Layout 2 | `bd8cd35379c7`  |
| 2882   | Layout 2 | `bd8cd35379c7`  |
| 2872   | Layout 2 | `bd8cd35379c7`  |
| 2863   | Layout 2 | `bd8cd35379c7`  |
| 2855   | Layout 2 | `bd8cd35379c7`  |
| 2849   | Layout 2 | `bd8cd35379c7`  |
| 2844   | Layout 2 | `bd8cd35379c7`  |
| 2834   | Layout 2 | `bd8cd35379c7`  |
| 2825   | Layout 2 | `bd8cd35379c7`  |
| 2819   | Layout 2 | `bd8cd35379c7`  |
| 2811   | Layout 2 | `bd8cd35379c7`  |
| 2803   | Layout 2 | `bd8cd35379c7`  |
| 2794   | Layout 2 | `bd8cd35379c7`  |
| 2783   | Layout 2 | `bd8cd35379c7`  |
| 2774   | Layout 2 | `bd8cd35379c7`  |
| 2765   | Layout 2 | `bd8cd35379c7`  |
| 2756   | Layout 2 | `bd8cd35379c7`  |
| 2750   | Layout 2 | `bd8cd35379c7`  |
| 2743   | Layout 2 | `bd8cd35379c7`  |
| 2736   | Layout 2 | `bd8cd35379c7`  |
| 2726   | Layout 2 | `bd8cd35379c7`  |
| 2717   | Layout 2 | `bd8cd35379c7`  |
| 2709   | Layout 2 | `bd8cd35379c7`  |
| 2703   | Layout 2 | `bd8cd35379c7`  |
| 2695   | Layout 2 | `bd8cd35379c7`  |
| 2684   | Layout 2 | `bd8cd35379c7`  |
| 2672   | Layout 2 | `bd8cd35379c7`  |
| 2665   | Layout 2 | `bd8cd35379c7`  |
| 2657   | Layout 2 | `bd8cd35379c7`  |
| 2649   | Layout 2 | `bd8cd35379c7`  |
| 2644   | Layout 2 | `bd8cd35379c7`  |
| 2637   | Layout 2 | `bd8cd35379c7`  |
| 2629   | Layout 2 | `bd8cd35379c7`  |
| 2619   | Layout 2 | `bd8cd35379c7`  |
| 2612   | Layout 2 | `bd8cd35379c7`  |
| 2606   | Layout 2 | `bd8cd35379c7`  |
| 2602   | Layout 2 | `bd8cd35379c7`  |
| 2601   | Layout 2 | `bd8cd35379c7`  |
| 2592   | Layout 2 | `bd8cd35379c7`  |
| 2583   | Layout 2 | `bd8cd35379c7`  |
| 2575   | Layout 1 | `bd8cd35379c7`  |
| 2567   | Layout 1 | `bd8cd35379c7`  |
| 2560   | Layout 1 | `bd8cd35379c7`  |
| 2553   | Layout 1 | `bd8cd35379c7`  |
| 2545   | Layout 1 | `bd8cd35379c7`  |
| 2538   | Layout 1 | `bd8cd35379c7`  |
| 2529   | Layout 1 | `bd8cd35379c7`  |
| 2519   | Layout 1 | `bd8cd35379c7`  |
| 2513   | Layout 1 | `bd8cd35379c7`  |
| 2510   | Layout 1 | `bd8cd35379c7`  |
| 2507   | Layout 1 | `bd8cd35379c7`  |
| 2503   | Layout 1 | `bd8cd35379c7`  |
| 2498   | Layout 1 | `bd8cd35379c7`  |
| 2492   | Layout 1 | `bd8cd35379c7`  |
| 2487   | Layout 1 | `bd8cd35379c7`  |
| 2480   | Layout 1 | `bd8cd35379c7`  |
| 2474   | Layout 1 | `bd8cd35379c7`  |
| 2468   | Layout 1 | `bd8cd35379c7`  |
| 2460   | Layout 1 | `bd8cd35379c7`  |
| 2453   | Layout 1 | `bd8cd35379c7`  |
| 2444   | Layout 1 | `bd8cd35379c7`  |
| 2438   | Layout 1 | `bd8cd35379c7`  |
| 2434   | Layout 1 | `bd8cd35379c7`  |
| 2429   | Layout 1 | `bd8cd35379c7`  |
| 2421   | Layout 1 | `bd8cd35379c7`  |
| 2414   | Layout 1 | `bd8cd35379c7`  |
| 2407   | Layout 1 | `bd8cd35379c7`  |
| 2401   | Layout 1 | `bd8cd35379c7`  |
| 2397   | Layout 1 | `bd8cd35379c7`  |
| 2393   | Layout 1 | `bd8cd35379c7`  |
| 2384   | Layout 1 | `bd8cd35379c7`  |
| 2378   | Layout 1 | `bd8cd35379c7`  |
| 2372   | Layout 1 | `bd8cd35379c7`  |
| 2358   | Layout 1 | `bd8cd35379c7`  |
| 2352   | Layout 1 | `bd8cd35379c7`  |
| 2347   | Layout 1 | `bd8cd35379c7`  |
| 2343   | Layout 1 | `bd8cd35379c7`  |
| 2335   | Layout 1 | `bd8cd35379c7`  |
| 2327   | Layout 1 | `bd8cd35379c7`  |
| 2324   | Layout 1 | `bd8cd35379c7`  |
| 2319   | Layout 1 | `bd8cd35379c7`  |
| 2313   | Layout 1 | `bd8cd35379c7`  |
| 2308   | Layout 1 | `bd8cd35379c7`  |
| 2302   | Layout 1 | `bd8cd35379c7`  |
| 2295   | Layout 1 | `bd8cd35379c7`  |
| 2290   | Layout 1 | `bd8cd35379c7`  |
| 2284   | Layout 1 | `bd8cd35379c7`  |
| 2276   | Layout 1 | `bd8cd35379c7`  |
| 2269   | Layout 1 | `bd8cd35379c7`  |
| 2259   | Layout 1 | `bd8cd35379c7`  |
| 2250   | Layout 1 | `bd8cd35379c7`  |
| 2243   | Layout 1 | `bd8cd35379c7`  |
| 2235   | Layout 1 | `bd8cd35379c7`  |
| 2229   | Layout 1 | `bd8cd35379c7`  |
| 2224   | Layout 1 | `bd8cd35379c7`  |
| 2218   | Layout 1 | `bd8cd35379c7`  |
| 2215   | Layout 1 | `bd8cd35379c7`  |
| 2207   | Layout 1 | `bd8cd35379c7`  |
| 2203   | Layout 1 | `bd8cd35379c7`  |
| 2196   | Layout 1 | `bd8cd35379c7`  |
| 2192   | Layout 1 | `bd8cd35379c7`  |
| 2189   | Layout 1 | `bd8cd35379c7`  |
| 2183   | Layout 1 | `bd8cd35379c7`  |
| 2179   | Layout 1 | `bd8cd35379c7`  |
| 2171   | Layout 1 | `bd8cd35379c7`  |
| 2163   | Layout 1 | `bd8cd35379c7`  |
| 2156   | Layout 1 | `bd8cd35379c7`  |
| 2151   | Layout 1 | `bd8cd35379c7`  |
| 2147   | Layout 1 | `bd8cd35379c7`  |
| 2142   | Layout 1 | `bd8cd35379c7`  |
| 2138   | Layout 1 | `bd8cd35379c7`  |
| 2134   | Layout 1 | `bd8cd35379c7`  |
| 2130   | Layout 1 | `bd8cd35379c7`  |
| 2122   | Layout 1 | `bd8cd35379c7`  |
| 2107   | Layout 1 | `bd8cd35379c7`  |
| 2098   | Layout 1 | `bd8cd35379c7`  |
| 2089   | Layout 1 | `bd8cd35379c7`  |
| 2081   | Layout 1 | `bd8cd35379c7`  |
| 2073   | Layout 1 | `bd8cd35379c7`  |
| 2067   | Layout 1 | `bd8cd35379c7`  |
| 2063   | Layout 1 | `bd8cd35379c7`  |
| 2059   | Layout 1 | `bd8cd35379c7`  |
| 2052   | Layout 1 | `bd8cd35379c7`  |
| 2044   | Layout 1 | `bd8cd35379c7`  |
| 2039   | Layout 1 | `bd8cd35379c7`  |
| 2032   | Layout 1 | `bd8cd35379c7`  |
| 2025   | Layout 1 | `bd8cd35379c7`  |
| 2011   | Layout 1 | `bd8cd35379c7`  |
| 2005   | Layout 1 | `bd8cd35379c7`  |
| 2000   | Layout 1 | `bd8cd35379c7`  |
| 1996   | Layout 1 | `bd8cd35379c7`  |
| 1991   | Layout 1 | `bd8cd35379c7`  |
| 1985   | Layout 1 | `bd8cd35379c7`  |
| 1980   | Layout 1 | `bd8cd35379c7`  |
| 1969   | Layout 1 | `bd8cd35379c7`  |
| 1964   | Layout 1 | `bd8cd35379c7`  |
| 1958   | Layout 1 | `bd8cd35379c7`  |
| 1950   | Layout 1 | `bd8cd35379c7`  |
| 1945   | Layout 1 | `bd8cd35379c7`  |
| 1937   | Layout 1 | `bd8cd35379c7`  |
| 1933   | Layout 1 | `bd8cd35379c7`  |
| 1927   | Layout 1 | `bd8cd35379c7`  |
| 1921   | Layout 1 | `bd8cd35379c7`  |
| 1914   | Layout 1 | `bd8cd35379c7`  |
| 1908   | Layout 1 | `bd8cd35379c7`  |
| 1897   | Layout 1 | `bd8cd35379c7`  |
| 1892   | Layout 1 | `bd8cd35379c7`  |
| 1886   | Layout 1 | `bd8cd35379c7`  |
| 1881   | Layout 1 | `bd8cd35379c7`  |
| 1871   | Layout 1 | `bd8cd35379c7`  |
| 1866   | Layout 1 | `bd8cd35379c7`  |
| 1862   | Layout 1 | `bd8cd35379c7`  |
| 1854   | Layout 1 | `bd8cd35379c7`  |
| 1846   | Layout 1 | `bd8cd35379c7`  |
| 1838   | Layout 1 | `bd8cd35379c7`  |
| 1832   | Layout 1 | `bd8cd35379c7`  |
| 1826   | Layout 1 | `bd8cd35379c7`  |
| 1822   | Layout 1 | `bd8cd35379c7`  |
| 1818   | Layout 1 | `bd8cd35379c7`  |
| 1804   | Layout 1 | `bd8cd35379c7`  |
| 1794   | Layout 1 | `bd8cd35379c7`  |
| 1790   | Layout 1 | `bd8cd35379c7`  |
| 1784   | Layout 1 | `bd8cd35379c7`  |
| 1774   | Layout 1 | `bd8cd35379c7`  |
| 1771   | Layout 1 | `bd8cd35379c7`  |
| 1762   | Layout 1 | `bd8cd35379c7`  |
| 1759   | Layout 1 | `bd8cd35379c7`  |
| 1754   | Layout 1 | `bd8cd35379c7`  |
| 1749   | Layout 1 | `bd8cd35379c7`  |
| 1743   | Layout 1 | `bd8cd35379c7`  |
| 1737   | Layout 1 | `bd8cd35379c7`  |
| 1731   | Layout 1 | `bd8cd35379c7`  |
| 1725   | Layout 1 | `bd8cd35379c7`  |
| 1717   | Layout 1 | `bd8cd35379c7`  |
| 1710   | Layout 1 | `bd8cd35379c7`  |
| 1704   | Layout 1 | `bd8cd35379c7`  |
| 1698   | Layout 1 | `bd8cd35379c7`  |
| 1690   | Layout 1 | `bd8cd35379c7`  |
| 1685   | Layout 1 | `bd8cd35379c7`  |
| 1680   | Layout 1 | `bd8cd35379c7`  |
| 1674   | Layout 1 | `bd8cd35379c7`  |
| 1668   | Layout 1 | `bd8cd35379c7`  |
| 1659   | Layout 1 | `bd8cd35379c7`  |
| 1649   | Layout 1 | `bd8cd35379c7`  |
| 1642   | Layout 1 | `bd8cd35379c7`  |
| 1636   | Layout 1 | `bd8cd35379c7`  |
| 1628   | Layout 1 | `bd8cd35379c7`  |
| 1622   | Layout 1 | `bd8cd35379c7`  |
| 1614   | Layout 1 | `bd8cd35379c7`  |
| 1608   | Layout 1 | `bd8cd35379c7`  |
| 1602   | Layout 1 | `bd8cd35379c7`  |
| 1598   | Layout 1 | `bd8cd35379c7`  |
| 1594   | Layout 1 | `bd8cd35379c7`  |
| 1590   | Layout 1 | `bd8cd35379c7`  |
| 1587   | Layout 1 | `bd8cd35379c7`  |
| 1584   | Layout 1 | `bd8cd35379c7`  |
| 1579   | Layout 1 | `bd8cd35379c7`  |
| 1572   | Layout 1 | `bd8cd35379c7`  |
| 1565   | Layout 1 | `bd8cd35379c7`  |
| 1559   | Layout 1 | `bd8cd35379c7`  |
| 1554   | Layout 1 | `bd8cd35379c7`  |
| 1547   | Layout 1 | `bd8cd35379c7`  |
| 1537   | Layout 1 | `bd8cd35379c7`  |
| 1529   | Layout 1 | `bd8cd35379c7`  |
| 1524   | Layout 1 | `bd8cd35379c7`  |
| 1519   | Layout 1 | `bd8cd35379c7`  |
| 1509   | Layout 1 | `bd8cd35379c7`  |
| 1506   | Layout 1 | `bd8cd35379c7`  |
| 1504   | Layout 1 | `bd8cd35379c7`  |
| 1500   | Layout 1 | `bd8cd35379c7`  |
| 1493   | Layout 1 | `bd8cd35379c7`  |
| 1489   | Layout 1 | `bd8cd35379c7`  |
| 1485   | Layout 1 | `bd8cd35379c7`  |
| 1481   | Layout 1 | `bd8cd35379c7`  |
| 1474   | Layout 1 | `bd8cd35379c7`  |
| 1466   | Layout 1 | `bd8cd35379c7`  |
| 1462   | Layout 1 | `bd8cd35379c7`  |
| 1459   | Layout 1 | `bd8cd35379c7`  |
| 1453   | Layout 1 | `bd8cd35379c7`  |
| 1450   | Layout 1 | `bd8cd35379c7`  |
| 1445   | Layout 1 | `bd8cd35379c7`  |
| 1439   | Layout 1 | `bd8cd35379c7`  |
| 1433   | Layout 1 | `bd8cd35379c7`  |
| 1430   | Layout 1 | `bd8cd35379c7`  |
| 1426   | Layout 1 | `bd8cd35379c7`  |
| 1421   | Layout 1 | `bd8cd35379c7`  |
| 1417   | Layout 1 | `bd8cd35379c7`  |
| 1416   | Layout 1 | `bd8cd35379c7`  |
| 1409   | Layout 1 | `bd8cd35379c7`  |
| 1405   | Layout 1 | `bd8cd35379c7`  |
| 1401   | Layout 1 | `bd8cd35379c7`  |
| 1396   | Layout 1 | `bd8cd35379c7`  |
| 1391   | Layout 1 | `bd8cd35379c7`  |
| 1390   | Layout 1 | `bd8cd35379c7`  |
| 1386   | Layout 1 | `bd8cd35379c7`  |
| 1381   | Layout 1 | `bd8cd35379c7`  |
| 1379   | Layout 1 | `bd8cd35379c7`  |
| 1372   | Layout 1 | `bd8cd35379c7`  |
| 1366   | Layout 1 | `bd8cd35379c7`  |
| 1364   | Layout 1 | `bd8cd35379c7`  |
| 1363   | Layout 1 | `bd8cd35379c7`  |
| 1360   | Layout 1 | `bd8cd35379c7`  |
| 1358   | Layout 1 | `bd8cd35379c7`  |
| 1355   | Layout 1 | `bd8cd35379c7`  |
| 1351   | Layout 1 | `bd8cd35379c7`  |
| 1348   | Layout 1 | `bd8cd35379c7`  |
| 1346   | Layout 1 | `bd8cd35379c7`  |
| 1341   | Layout 1 | `bd8cd35379c7`  |
| 1340   | Layout 1 | `bd8cd35379c7`  |
| 1338   | Layout 1 | `bd8cd35379c7`  |
| 1335   | Layout 1 | `bd8cd35379c7`  |
| 1333   | Layout 1 | `bd8cd35379c7`  |
| 1329   | Layout 1 | `bd8cd35379c7`  |
| 1327   | Layout 1 | `bd8cd35379c7`  |
| 1324   | Layout 1 | `bd8cd35379c7`  |
| 1321   | Layout 1 | `bd8cd35379c7`  |
| 1319   | Layout 1 | `bd8cd35379c7`  |
| 1318   | Layout 1 | `bd8cd35379c7`  |
| 1316   | Layout 1 | `bd8cd35379c7`  |
| 1313   | Layout 1 | `bd8cd35379c7`  |
| 1311   | Layout 1 | `bd8cd35379c7`  |
| 1309   | Layout 1 | `bd8cd35379c7`  |
| 1304   | Layout 1 | `bd8cd35379c7`  |
| 1292   | Layout 1 | `bd8cd35379c7`  |
| 1286   | Layout 1 | `bd8cd35379c7`  |
| 1280   | Layout 1 | `bd8cd35379c7`  |
| 1276   | Layout 1 | `bd8cd35379c7`  |
| 1267   | Layout 1 | `bd8cd35379c7`  |
| 1261   | Layout 1 | `bd8cd35379c7`  |
| 1256   | No file  | `bd8cd35379c7`  |
| 1250   | No file  | `bd8cd35379c7`  |
| 1246   | No file  | `bd8cd35379c7`  |
| 1239   | No file  | `bd8cd35379c7`  |
| 1230   | No file  | `bd8cd35379c7`  |
| 1226   | No file  | `bd8cd35379c7`  |
| 1220   | No file  | `bd8cd35379c7`  |
| 1217   | No file  | `bd8cd35379c7`  |
| 1211   | No file  | `bd8cd35379c7`  |
| 1210   | No file  | `bd8cd35379c7`  |
| 1208   | No file  | `bd8cd35379c7`  |
| 1203   | No file  | `bd8cd35379c7`  |
| 1197   | No file  | `bd8cd35379c7`  |
| 1194   | No file  | `bd8cd35379c7`  |
| 1192   | No file  | `bd8cd35379c7`  |
| 1187   | No file  | `bd8cd35379c7`  |
| 1183   | No file  | `bd8cd35379c7`  |
| 1177   | No file  | `bd8cd35379c7`  |
| 1173   | No file  | `bd8cd35379c7`  |
| 1167   | No file  | `bd8cd35379c7`  |
| 1164   | No file  | `bd8cd35379c7`  |
| 1156   | No file  | `bd8cd35379c7`  |
| 1149   | No file  | `bd8cd35379c7`  |
| 1144   | No file  | `bd8cd35379c7`  |
| 1137   | No file  | `bd8cd35379c7`  |
| 1132   | No file  | `bd8cd35379c7`  |
| 1127   | No file  | `bd8cd35379c7`  |
| 1122   | No file  | `bd8cd35379c7`  |
| 1118   | No file  | `bd8cd35379c7`  |
| 1114   | No file  | `bd8cd35379c7`  |
| 1109   | No file  | `bd8cd35379c7`  |
| 1102   | No file  | `bd8cd35379c7`  |
| 1096   | No file  | `bd8cd35379c7`  |
| 1088   | No file  | `bd8cd35379c7`  |
| 1081   | No file  | `bd8cd35379c7`  |
| 1076   | No file  | `bd8cd35379c7`  |
| 1069   | No file  | `bd8cd35379c7`  |
| 1064   | No file  | `bd8cd35379c7`  |
| 1058   | No file  | `bd8cd35379c7`  |
| 1051   | No file  | `bd8cd35379c7`  |
| 1044   | No file  | `bd8cd35379c7`  |
| 1036   | No file  | `bd8cd35379c7`  |
| 1026   | No file  | `bd8cd35379c7`  |
| 1016   | No file  | `bd8cd35379c7`  |
| 1009   | No file  | `bd8cd35379c7`  |
| 1005   | No file  | `bd8cd35379c7`  |
| 1000   | No file  | `bd8cd35379c7`  |
| 998    | No file  | `bd8cd35379c7`  |
| 990    | No file  | `bd8cd35379c7`  |
| 979    | No file  | `bd8cd35379c7`  |
| 972    | No file  | `bd8cd35379c7`  |
| 963    | No file  | `bd8cd35379c7`  |
| 955    | No file  | `bd8cd35379c7`  |
| 946    | No file  | `bd8cd35379c7`  |
| 938    | No file  | `bd8cd35379c7`  |
| 927    | No file  | `bd8cd35379c7`  |
| 911    | No file  | `bd8cd35379c7`  |
| 904    | No file  | `bd8cd35379c7`  |
| 899    | No file  | `bd8cd35379c7`  |
| 894    | No file  | `bd8cd35379c7`  |
| 885    | No file  | `bd8cd35379c7`  |
| 879    | No file  | `bd8cd35379c7`  |
| 872    | No file  | `bd8cd35379c7`  |
| 864    | No file  | `bd8cd35379c7`  |
| 855    | No file  | `bd8cd35379c7`  |
| 853    | No file  | `bd8cd35379c7`  |
| 845    | No file  | `bd8cd35379c7`  |
| 837    | No file  | `bd8cd35379c7`  |
| 829    | No file  | `bd8cd35379c7`  |
| 822    | No file  | `bd8cd35379c7`  |
| 814    | No file  | `bd8cd35379c7`  |
| 805    | No file  | `bd8cd35379c7`  |
| 794    | No file  | `bd8cd35379c7`  |
| 787    | No file  | `bd8cd35379c7`  |
| 780    | No file  | `bd8cd35379c7`  |
| 771    | No file  | `bd8cd35379c7`  |
| 760    | No file  | `bd8cd35379c7`  |
| 748    | No file  | `bd8cd35379c7`  |
| 741    | No file  | `bd8cd35379c7`  |
| 736    | No file  | `bd8cd35379c7`  |
| 731    | No file  | `bd8cd35379c7`  |
| 723    | No file  | `bd8cd35379c7`  |
| 711    | No file  | `bd8cd35379c7`  |
| 707    | No file  | `bd8cd35379c7`  |
| 697    | No file  | `bd8cd35379c7`  |
| 689    | No file  | `bd8cd35379c7`  |
| 683    | No file  | `bd8cd35379c7`  |
| 678    | No file  | `bd8cd35379c7`  |
| 670    | No file  | `bd8cd35379c7`  |
| 661    | No file  | `bd8cd35379c7`  |
| 656    | No file  | `bd8cd35379c7`  |
| 652    | No file  | `bd8cd35379c7`  |
| 643    | No file  | `bd8cd35379c7`  |
| 637    | No file  | `bd8cd35379c7`  |
| 630    | No file  | `bd8cd35379c7`  |
| 627    | No file  | `bd8cd35379c7`  |
| 621    | No file  | `bd8cd35379c7`  |
| 617    | No file  | `bd8cd35379c7`  |
| 615    | No file  | `bd8cd35379c7`  |
| 606    | No file  | `bd8cd35379c7`  |
| 599    | No file  | `bd8cd35379c7`  |
| 592    | No file  | `bd8cd35379c7`  |
| 586    | No file  | `bd8cd35379c7`  |
| 577    | No file  | `bd8cd35379c7`  |
| 569    | No file  | `bd8cd35379c7`  |
| 561    | No file  | `bd8cd35379c7`  |
| 554    | No file  | `bd8cd35379c7`  |
| 542    | No file  | `bd8cd35379c7`  |
| 532    | No file  | `bd8cd35379c7`  |
| 531    | No file  | `bd8cd35379c7`  |
| 526    | No file  | `bd8cd35379c7`  |
| 521    | No file  | `bd8cd35379c7`  |
| 517    | No file  | `bd8cd35379c7`  |
| 510    | No file  | `bd8cd35379c7`  |
| 508    | No file  | `bd8cd35379c7`  |
| 504    | No file  | `bd8cd35379c7`  |
| 497    | No file  | `bd8cd35379c7`  |
| 491    | No file  | `bd8cd35379c7`  |
| 485    | No file  | `bd8cd35379c7`  |
| 478    | No file  | `bd8cd35379c7`  |
| 472    | No file  | `bd8cd35379c7`  |
| 466    | No file  | `bd8cd35379c7`  |
| 457    | No file  | `bd8cd35379c7`  |
| 452    | No file  | `bd8cd35379c7`  |
| 449    | No file  | `bd8cd35379c7`  |
| 435    | No file  | `bd8cd35379c7`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                     |
| ---------------------------- | -------- | ------------------------------------------------------------------------ |
| `minigamefindtooloffset.dbss` | Optional | `(item grade, enchant_level) -> (data_offset, data_size)`; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No count and no `PABR` magic: grade blocks back to back up to the end of the
file. Block `i` holds item grade `i`; the file stores no grade field.

| Offset  | Type               | Field  | Notes                                     |
| ------- | ------------------ | ------ | ----------------------------------------- |
| `+0x00` | Grade Block[..end] | blocks | One block per item grade; see Grade Block |

On client 3482 the file is 6 x 190 = 1,140 bytes.

### Grade Block (190 bytes)

| Offset  | Type          | Field      | Notes                                                   |
| ------- | ------------- | ---------- | ------------------------------------------------------- |
| `+0x00` | u8            | unknown_00 | `1` in every block (client 3482); see Open Questions    |
| `+0x01` | Level Row[21] | rows       | Enhancement levels 0 to 20, in order; see Level Row     |

The block holds 21 rows on every client read; the index gives the count
(`row_count`), the main file does not.

### Level Row (9 bytes)

| Offset  | Type | Field                | Notes                                                        |
| ------- | ---- | -------------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | r_click_count        | Right clicks the hoe allows: `10` to `28` on client 3482      |
| `+0x04` | u8   | open_slot_count      | `1` to `9` on client 3482                                    |
| `+0x05` | u32  | decrease_damage_rate | `20000` to `1000000` on client 3482                          |

### `minigamefindtooloffset.dbss`

Index into `minigamefindtool.dbss` with the same blocks, no magic and no
trailer.

| Offset  | Type               | Field  | Notes                                       |
| ------- | ------------------ | ------ | ------------------------------------------- |
| `+0x00` | Index Group[..end] | groups | Group `i` holds item grade `i`; see Index Group |

### Index Group (variable: 4 bytes + rows)

| Offset  | Type                 | Field     | Notes                               |
| ------- | -------------------- | --------- | ----------------------------------- |
| `+0x00` | u32                  | row_count | `21` in every group (client 3482)    |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                       |

### Index Row (9 bytes)

| Offset  | Type | Field         | Notes                                                 |
| ------- | ---- | ------------- | ----------------------------------------------------- |
| `+0x00` | u8   | enchant_level | Row key together with the group index: `0` to `20`    |
| `+0x01` | u32  | data_offset   | Start of the Level Row in `minigamefindtool.dbss`     |
| `+0x05` | u32  | data_size     | `9` on every row, the Level Row size                  |

On client 3482 every index row points at the main row of its grade and
level, in file order, and the first row of a block sits one byte past the
block start, after `unknown_00`.

## Layout 1

The grade block has no leading u8: 21 rows and nothing else. On client 1784
the file holds five grades (0 to 4), 5 x 189 = 945 bytes, and the index
points at `0x00` for the first row.

### Grade Block (189 bytes)

| Offset  | Type          | Field | Notes                                |
| ------- | ------------- | ----- | ------------------------------------ |
| `+0x00` | Level Row[21] | rows  | Enhancement levels 0 to 20, in order |

## Field Names

The rows are the `MiniGameFindToolData` sheet of a private server's
`DataSheets.bexcel` on client 1784, keyed by `ItemGrade` and
`EnchantLevel` (105 rows, grades 0 to 4). The group index is `ItemGrade` and
the index key `EnchantLevel`; `r_click_count`, `open_slot_count` and
`decrease_damage_rate` match `RClickCount`, `OpenSlotCount` and
`DecreaseDamageRate` on 105 of 105 keys on clients 1784 and 3482. Grade 5
(client 3482 only) has no sheet rows.

The minigame window Lua (`panel_minigame_find_all_1`, `updateValue`) passes
the equipped hoe's `getGradeType()` and, when its durability is not 0, its
enchant level to `ToClient_MiniGameFindMaxRClickCount` and shows the result
less the clicks used as the right clicks left.

## Notes

- On client 3482 grades 0 and 1 hold `10` right clicks, `2` open slots and
  `210000` on every level except grade 0 +0 (`22`, `7`, `600000`). In
  grades 2 to 5 the right clicks rise from `10` (+0 to +9) to `22` (grade
  2) or `28` (grades 3 to 5) at PEN. Grades 4 and 5 hold the same 21 rows;
  grade 3 differs from them at +0 only (`9` open slots, `1000000`).

## Open Questions

### What the Grade Block's Leading u8 Holds

`unknown_00` is `1` in all six blocks of client 3482. Client 1784 has no
such byte, and the sheet no column for it.
