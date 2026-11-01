# `skillclasstypelist.bss` Format

## Purpose

One row for every level `1` skill key of a non-guild skill: the skill key
followed by a u64 `unknown_04`. The keys are the keys of
[`publicskill.bss`](publicskill_bss.md) and
[`privateskill.bss`](privateskill_bss.md) together, item, active and
passive skills in one list, and `unknown_04` holds the same value on every
row.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes   | Records    | Row bytes |
| ------ | -------------- | ------------------------ | ------- | ---------- | --------- |
| 2      | 1267 and later | `skillclasstypelist.bss` | 356,408 | 29,699 Row | 12        |
| 1      | 1226 to 1261   | `skillclasstypelist.bss` | 656,012 | 18,222 Row | 36        |

| Layout | File                     | Known             | Unknown           |
| ------ | ------------------------ | ----------------- | ----------------- |
| 2      | `skillclasstypelist.bss` | 118,816 B (33.3%) | 237,592 B (66.7%) |
| 1      | `skillclasstypelist.bss` | 72,908 B (11.1%)  | 583,104 B (88.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `ebacd74a4c55`  |
| 3482   | Layout 2 | `ebacd74a4c55`  |
| 3474   | Layout 2 | `ebacd74a4c55`  |
| 3473   | Layout 2 | `ebacd74a4c55`  |
| 3464   | Layout 2 | `ebacd74a4c55`  |
| 3458   | Layout 2 | `ebacd74a4c55`  |
| 3454   | Layout 2 | `ebacd74a4c55`  |
| 3444   | Layout 2 | `ebacd74a4c55`  |
| 3435   | Layout 2 | `ebacd74a4c55`  |
| 3426   | Layout 2 | `ebacd74a4c55`  |
| 3418   | Layout 2 | `ebacd74a4c55`  |
| 3412   | Layout 2 | `ebacd74a4c55`  |
| 3402   | Layout 2 | `ebacd74a4c55`  |
| 3396   | Layout 2 | `ebacd74a4c55`  |
| 3387   | Layout 2 | `ebacd74a4c55`  |
| 3381   | Layout 2 | `ebacd74a4c55`  |
| 3373   | Layout 2 | `ebacd74a4c55`  |
| 3364   | Layout 2 | `ebacd74a4c55`  |
| 3356   | Layout 2 | `ebacd74a4c55`  |
| 3349   | Layout 2 | `ebacd74a4c55`  |
| 3342   | Layout 2 | `ebacd74a4c55`  |
| 3335   | Layout 2 | `ebacd74a4c55`  |
| 3326   | Layout 2 | `ebacd74a4c55`  |
| 3321   | Layout 2 | `ebacd74a4c55`  |
| 3314   | Layout 2 | `ebacd74a4c55`  |
| 3303   | Layout 2 | `ebacd74a4c55`  |
| 3302   | Layout 2 | `ebacd74a4c55`  |
| 3293   | Layout 2 | `ebacd74a4c55`  |
| 3283   | Layout 2 | `ebacd74a4c55`  |
| 3275   | Layout 2 | `ebacd74a4c55`  |
| 3267   | Layout 2 | `ebacd74a4c55`  |
| 3258   | Layout 2 | `ebacd74a4c55`  |
| 3251   | Layout 2 | `ebacd74a4c55`  |
| 3242   | Layout 2 | `ebacd74a4c55`  |
| 3235   | Layout 2 | `ebacd74a4c55`  |
| 3229   | Layout 2 | `ebacd74a4c55`  |
| 3212   | Layout 2 | `ebacd74a4c55`  |
| 3203   | Layout 2 | `ebacd74a4c55`  |
| 3193   | Layout 2 | `ebacd74a4c55`  |
| 3186   | Layout 2 | `ebacd74a4c55`  |
| 3177   | Layout 2 | `ebacd74a4c55`  |
| 3169   | Layout 2 | `ebacd74a4c55`  |
| 3158   | Layout 2 | `ebacd74a4c55`  |
| 3151   | Layout 2 | `ebacd74a4c55`  |
| 3144   | Layout 2 | `ebacd74a4c55`  |
| 3133   | Layout 2 | `ebacd74a4c55`  |
| 3125   | Layout 2 | `ebacd74a4c55`  |
| 3118   | Layout 2 | `ebacd74a4c55`  |
| 3111   | Layout 2 | `ebacd74a4c55`  |
| 3103   | Layout 2 | `ebacd74a4c55`  |
| 3095   | Layout 2 | `ebacd74a4c55`  |
| 3086   | Layout 2 | `ebacd74a4c55`  |
| 3072   | Layout 2 | `ebacd74a4c55`  |
| 3062   | Layout 2 | `ebacd74a4c55`  |
| 3052   | Layout 2 | `ebacd74a4c55`  |
| 3045   | Layout 2 | `ebacd74a4c55`  |
| 3037   | Layout 2 | `ebacd74a4c55`  |
| 3030   | Layout 2 | `ebacd74a4c55`  |
| 3021   | Layout 2 | `ebacd74a4c55`  |
| 3012   | Layout 2 | `ebacd74a4c55`  |
| 3002   | Layout 2 | `ebacd74a4c55`  |
| 2995   | Layout 2 | `ebacd74a4c55`  |
| 2987   | Layout 2 | `ebacd74a4c55`  |
| 2978   | Layout 2 | `ebacd74a4c55`  |
| 2970   | Layout 2 | `ebacd74a4c55`  |
| 2959   | Layout 2 | `ebacd74a4c55`  |
| 2951   | Layout 2 | `ebacd74a4c55`  |
| 2942   | Layout 2 | `ebacd74a4c55`  |
| 2935   | Layout 2 | `ebacd74a4c55`  |
| 2932   | Layout 2 | `ebacd74a4c55`  |
| 2923   | Layout 2 | `ebacd74a4c55`  |
| 2919   | Layout 2 | `ebacd74a4c55`  |
| 2907   | Layout 2 | `ebacd74a4c55`  |
| 2900   | Layout 2 | `ebacd74a4c55`  |
| 2891   | Layout 2 | `ebacd74a4c55`  |
| 2882   | Layout 2 | `ebacd74a4c55`  |
| 2872   | Layout 2 | `ebacd74a4c55`  |
| 2863   | Layout 2 | `ebacd74a4c55`  |
| 2855   | Layout 2 | `ebacd74a4c55`  |
| 2849   | Layout 2 | `ebacd74a4c55`  |
| 2844   | Layout 2 | `ebacd74a4c55`  |
| 2834   | Layout 2 | `ebacd74a4c55`  |
| 2825   | Layout 2 | `ebacd74a4c55`  |
| 2819   | Layout 2 | `ebacd74a4c55`  |
| 2811   | Layout 2 | `ebacd74a4c55`  |
| 2803   | Layout 2 | `ebacd74a4c55`  |
| 2794   | Layout 2 | `ebacd74a4c55`  |
| 2783   | Layout 2 | `ebacd74a4c55`  |
| 2774   | Layout 2 | `ebacd74a4c55`  |
| 2765   | Layout 2 | `ebacd74a4c55`  |
| 2756   | Layout 2 | `ebacd74a4c55`  |
| 2750   | Layout 2 | `ebacd74a4c55`  |
| 2743   | Layout 2 | `ebacd74a4c55`  |
| 2736   | Layout 2 | `ebacd74a4c55`  |
| 2726   | Layout 2 | `ebacd74a4c55`  |
| 2717   | Layout 2 | `ebacd74a4c55`  |
| 2709   | Layout 2 | `ebacd74a4c55`  |
| 2703   | Layout 2 | `ebacd74a4c55`  |
| 2695   | Layout 2 | `ebacd74a4c55`  |
| 2684   | Layout 2 | `ebacd74a4c55`  |
| 2672   | Layout 2 | `ebacd74a4c55`  |
| 2665   | Layout 2 | `ebacd74a4c55`  |
| 2657   | Layout 2 | `ebacd74a4c55`  |
| 2649   | Layout 2 | `ebacd74a4c55`  |
| 2644   | Layout 2 | `ebacd74a4c55`  |
| 2637   | Layout 2 | `ebacd74a4c55`  |
| 2629   | Layout 2 | `ebacd74a4c55`  |
| 2619   | Layout 2 | `ebacd74a4c55`  |
| 2612   | Layout 2 | `ebacd74a4c55`  |
| 2606   | Layout 2 | `ebacd74a4c55`  |
| 2602   | Layout 2 | `ebacd74a4c55`  |
| 2601   | Layout 2 | `ebacd74a4c55`  |
| 2592   | Layout 2 | `ebacd74a4c55`  |
| 2583   | Layout 2 | `ebacd74a4c55`  |
| 2575   | Layout 2 | `ebacd74a4c55`  |
| 2567   | Layout 2 | `ebacd74a4c55`  |
| 2560   | Layout 2 | `ebacd74a4c55`  |
| 2553   | Layout 2 | `ebacd74a4c55`  |
| 2545   | Layout 2 | `ebacd74a4c55`  |
| 2538   | Layout 2 | `ebacd74a4c55`  |
| 2529   | Layout 2 | `ebacd74a4c55`  |
| 2519   | Layout 2 | `ebacd74a4c55`  |
| 2513   | Layout 2 | `ebacd74a4c55`  |
| 2510   | Layout 2 | `ebacd74a4c55`  |
| 2507   | Layout 2 | `ebacd74a4c55`  |
| 2503   | Layout 2 | `ebacd74a4c55`  |
| 2498   | Layout 2 | `ebacd74a4c55`  |
| 2492   | Layout 2 | `ebacd74a4c55`  |
| 2487   | Layout 2 | `ebacd74a4c55`  |
| 2480   | Layout 2 | `ebacd74a4c55`  |
| 2474   | Layout 2 | `ebacd74a4c55`  |
| 2468   | Layout 2 | `ebacd74a4c55`  |
| 2460   | Layout 2 | `ebacd74a4c55`  |
| 2453   | Layout 2 | `ebacd74a4c55`  |
| 2444   | Layout 2 | `ebacd74a4c55`  |
| 2438   | Layout 2 | `ebacd74a4c55`  |
| 2434   | Layout 2 | `ebacd74a4c55`  |
| 2429   | Layout 2 | `ebacd74a4c55`  |
| 2421   | Layout 2 | `ebacd74a4c55`  |
| 2414   | Layout 2 | `ebacd74a4c55`  |
| 2407   | Layout 2 | `ebacd74a4c55`  |
| 2401   | Layout 2 | `ebacd74a4c55`  |
| 2397   | Layout 2 | `ebacd74a4c55`  |
| 2393   | Layout 2 | `ebacd74a4c55`  |
| 2384   | Layout 2 | `ebacd74a4c55`  |
| 2378   | Layout 2 | `ebacd74a4c55`  |
| 2372   | Layout 2 | `ebacd74a4c55`  |
| 2358   | Layout 2 | `ebacd74a4c55`  |
| 2352   | Layout 2 | `ebacd74a4c55`  |
| 2347   | Layout 2 | `ebacd74a4c55`  |
| 2343   | Layout 2 | `ebacd74a4c55`  |
| 2335   | Layout 2 | `ebacd74a4c55`  |
| 2327   | Layout 2 | `ebacd74a4c55`  |
| 2324   | Layout 2 | `ebacd74a4c55`  |
| 2319   | Layout 2 | `ebacd74a4c55`  |
| 2313   | Layout 2 | `ebacd74a4c55`  |
| 2308   | Layout 2 | `ebacd74a4c55`  |
| 2302   | Layout 2 | `ebacd74a4c55`  |
| 2295   | Layout 2 | `ebacd74a4c55`  |
| 2290   | Layout 2 | `ebacd74a4c55`  |
| 2284   | Layout 2 | `ebacd74a4c55`  |
| 2276   | Layout 2 | `ebacd74a4c55`  |
| 2269   | Layout 2 | `ebacd74a4c55`  |
| 2259   | Layout 2 | `ebacd74a4c55`  |
| 2250   | Layout 2 | `ebacd74a4c55`  |
| 2243   | Layout 2 | `ebacd74a4c55`  |
| 2235   | Layout 2 | `ebacd74a4c55`  |
| 2229   | Layout 2 | `ebacd74a4c55`  |
| 2224   | Layout 2 | `ebacd74a4c55`  |
| 2218   | Layout 2 | `ebacd74a4c55`  |
| 2215   | Layout 2 | `ebacd74a4c55`  |
| 2207   | Layout 2 | `ebacd74a4c55`  |
| 2203   | Layout 2 | `ebacd74a4c55`  |
| 2196   | Layout 2 | `ebacd74a4c55`  |
| 2192   | Layout 2 | `ebacd74a4c55`  |
| 2189   | Layout 2 | `ebacd74a4c55`  |
| 2183   | Layout 2 | `ebacd74a4c55`  |
| 2179   | Layout 2 | `ebacd74a4c55`  |
| 2171   | Layout 2 | `ebacd74a4c55`  |
| 2163   | Layout 2 | `ebacd74a4c55`  |
| 2156   | Layout 2 | `ebacd74a4c55`  |
| 2151   | Layout 2 | `ebacd74a4c55`  |
| 2147   | Layout 2 | `ebacd74a4c55`  |
| 2142   | Layout 2 | `ebacd74a4c55`  |
| 2138   | Layout 2 | `ebacd74a4c55`  |
| 2134   | Layout 2 | `ebacd74a4c55`  |
| 2130   | Layout 2 | `ebacd74a4c55`  |
| 2122   | Layout 2 | `ebacd74a4c55`  |
| 2107   | Layout 2 | `ebacd74a4c55`  |
| 2098   | Layout 2 | `ebacd74a4c55`  |
| 2089   | Layout 2 | `ebacd74a4c55`  |
| 2081   | Layout 2 | `ebacd74a4c55`  |
| 2073   | Layout 2 | `ebacd74a4c55`  |
| 2067   | Layout 2 | `ebacd74a4c55`  |
| 2063   | Layout 2 | `ebacd74a4c55`  |
| 2059   | Layout 2 | `ebacd74a4c55`  |
| 2052   | Layout 2 | `ebacd74a4c55`  |
| 2044   | Layout 2 | `ebacd74a4c55`  |
| 2039   | Layout 2 | `ebacd74a4c55`  |
| 2032   | Layout 2 | `ebacd74a4c55`  |
| 2025   | Layout 2 | `ebacd74a4c55`  |
| 2011   | Layout 2 | `ebacd74a4c55`  |
| 2005   | Layout 2 | `ebacd74a4c55`  |
| 2000   | Layout 2 | `ebacd74a4c55`  |
| 1996   | Layout 2 | `ebacd74a4c55`  |
| 1991   | Layout 2 | `ebacd74a4c55`  |
| 1985   | Layout 2 | `ebacd74a4c55`  |
| 1980   | Layout 2 | `ebacd74a4c55`  |
| 1969   | Layout 2 | `ebacd74a4c55`  |
| 1964   | Layout 2 | `ebacd74a4c55`  |
| 1958   | Layout 2 | `ebacd74a4c55`  |
| 1950   | Layout 2 | `ebacd74a4c55`  |
| 1945   | Layout 2 | `ebacd74a4c55`  |
| 1937   | Layout 2 | `ebacd74a4c55`  |
| 1933   | Layout 2 | `ebacd74a4c55`  |
| 1927   | Layout 2 | `ebacd74a4c55`  |
| 1921   | Layout 2 | `ebacd74a4c55`  |
| 1914   | Layout 2 | `ebacd74a4c55`  |
| 1908   | Layout 2 | `ebacd74a4c55`  |
| 1897   | Layout 2 | `ebacd74a4c55`  |
| 1892   | Layout 2 | `ebacd74a4c55`  |
| 1886   | Layout 2 | `ebacd74a4c55`  |
| 1881   | Layout 2 | `ebacd74a4c55`  |
| 1871   | Layout 2 | `ebacd74a4c55`  |
| 1866   | Layout 2 | `ebacd74a4c55`  |
| 1862   | Layout 2 | `ebacd74a4c55`  |
| 1854   | Layout 2 | `ebacd74a4c55`  |
| 1846   | Layout 2 | `ebacd74a4c55`  |
| 1838   | Layout 2 | `ebacd74a4c55`  |
| 1832   | Layout 2 | `ebacd74a4c55`  |
| 1826   | Layout 2 | `ebacd74a4c55`  |
| 1822   | Layout 2 | `ebacd74a4c55`  |
| 1818   | Layout 2 | `ebacd74a4c55`  |
| 1804   | Layout 2 | `ebacd74a4c55`  |
| 1794   | Layout 2 | `ebacd74a4c55`  |
| 1790   | Layout 2 | `ebacd74a4c55`  |
| 1784   | Layout 2 | `ebacd74a4c55`  |
| 1774   | Layout 2 | `ebacd74a4c55`  |
| 1771   | Layout 2 | `ebacd74a4c55`  |
| 1762   | Layout 2 | `ebacd74a4c55`  |
| 1759   | Layout 2 | `ebacd74a4c55`  |
| 1754   | Layout 2 | `ebacd74a4c55`  |
| 1749   | Layout 2 | `ebacd74a4c55`  |
| 1743   | Layout 2 | `ebacd74a4c55`  |
| 1737   | Layout 2 | `ebacd74a4c55`  |
| 1731   | Layout 2 | `ebacd74a4c55`  |
| 1725   | Layout 2 | `ebacd74a4c55`  |
| 1717   | Layout 2 | `ebacd74a4c55`  |
| 1710   | Layout 2 | `ebacd74a4c55`  |
| 1704   | Layout 2 | `ebacd74a4c55`  |
| 1698   | Layout 2 | `ebacd74a4c55`  |
| 1690   | Layout 2 | `ebacd74a4c55`  |
| 1685   | Layout 2 | `ebacd74a4c55`  |
| 1680   | Layout 2 | `ebacd74a4c55`  |
| 1674   | Layout 2 | `ebacd74a4c55`  |
| 1668   | Layout 2 | `ebacd74a4c55`  |
| 1659   | Layout 2 | `ebacd74a4c55`  |
| 1649   | Layout 2 | `ebacd74a4c55`  |
| 1642   | Layout 2 | `ebacd74a4c55`  |
| 1636   | Layout 2 | `ebacd74a4c55`  |
| 1628   | Layout 2 | `ebacd74a4c55`  |
| 1622   | Layout 2 | `ebacd74a4c55`  |
| 1614   | Layout 2 | `ebacd74a4c55`  |
| 1608   | Layout 2 | `ebacd74a4c55`  |
| 1602   | Layout 2 | `ebacd74a4c55`  |
| 1598   | Layout 2 | `ebacd74a4c55`  |
| 1594   | Layout 2 | `ebacd74a4c55`  |
| 1590   | Layout 2 | `ebacd74a4c55`  |
| 1587   | Layout 2 | `ebacd74a4c55`  |
| 1584   | Layout 2 | `ebacd74a4c55`  |
| 1579   | Layout 2 | `ebacd74a4c55`  |
| 1572   | Layout 2 | `ebacd74a4c55`  |
| 1565   | Layout 2 | `ebacd74a4c55`  |
| 1559   | Layout 2 | `ebacd74a4c55`  |
| 1554   | Layout 2 | `ebacd74a4c55`  |
| 1547   | Layout 2 | `ebacd74a4c55`  |
| 1537   | Layout 2 | `ebacd74a4c55`  |
| 1529   | Layout 2 | `ebacd74a4c55`  |
| 1524   | Layout 2 | `ebacd74a4c55`  |
| 1519   | Layout 2 | `ebacd74a4c55`  |
| 1509   | Layout 2 | `ebacd74a4c55`  |
| 1506   | Layout 2 | `ebacd74a4c55`  |
| 1504   | Layout 2 | `ebacd74a4c55`  |
| 1500   | Layout 2 | `ebacd74a4c55`  |
| 1493   | Layout 2 | `ebacd74a4c55`  |
| 1489   | Layout 2 | `ebacd74a4c55`  |
| 1485   | Layout 2 | `ebacd74a4c55`  |
| 1481   | Layout 2 | `ebacd74a4c55`  |
| 1474   | Layout 2 | `ebacd74a4c55`  |
| 1466   | Layout 2 | `ebacd74a4c55`  |
| 1462   | Layout 2 | `ebacd74a4c55`  |
| 1459   | Layout 2 | `ebacd74a4c55`  |
| 1453   | Layout 2 | `ebacd74a4c55`  |
| 1450   | Layout 2 | `ebacd74a4c55`  |
| 1445   | Layout 2 | `ebacd74a4c55`  |
| 1439   | Layout 2 | `ebacd74a4c55`  |
| 1433   | Layout 2 | `ebacd74a4c55`  |
| 1430   | Layout 2 | `ebacd74a4c55`  |
| 1426   | Layout 2 | `ebacd74a4c55`  |
| 1421   | Layout 2 | `ebacd74a4c55`  |
| 1417   | Layout 2 | `ebacd74a4c55`  |
| 1416   | Layout 2 | `ebacd74a4c55`  |
| 1409   | Layout 2 | `ebacd74a4c55`  |
| 1405   | Layout 2 | `ebacd74a4c55`  |
| 1401   | Layout 2 | `ebacd74a4c55`  |
| 1396   | Layout 2 | `ebacd74a4c55`  |
| 1391   | Layout 2 | `ebacd74a4c55`  |
| 1390   | Layout 2 | `ebacd74a4c55`  |
| 1386   | Layout 2 | `ebacd74a4c55`  |
| 1381   | Layout 2 | `ebacd74a4c55`  |
| 1379   | Layout 2 | `ebacd74a4c55`  |
| 1372   | Layout 2 | `ebacd74a4c55`  |
| 1366   | Layout 2 | `ebacd74a4c55`  |
| 1364   | Layout 2 | `ebacd74a4c55`  |
| 1363   | Layout 2 | `ebacd74a4c55`  |
| 1360   | Layout 2 | `ebacd74a4c55`  |
| 1358   | Layout 2 | `ebacd74a4c55`  |
| 1355   | Layout 2 | `ebacd74a4c55`  |
| 1351   | Layout 2 | `ebacd74a4c55`  |
| 1348   | Layout 2 | `ebacd74a4c55`  |
| 1346   | Layout 2 | `ebacd74a4c55`  |
| 1341   | Layout 2 | `ebacd74a4c55`  |
| 1340   | Layout 2 | `ebacd74a4c55`  |
| 1338   | Layout 2 | `ebacd74a4c55`  |
| 1335   | Layout 2 | `ebacd74a4c55`  |
| 1333   | Layout 2 | `ebacd74a4c55`  |
| 1329   | Layout 2 | `ebacd74a4c55`  |
| 1327   | Layout 2 | `ebacd74a4c55`  |
| 1324   | Layout 2 | `ebacd74a4c55`  |
| 1321   | Layout 2 | `ebacd74a4c55`  |
| 1319   | Layout 2 | `ebacd74a4c55`  |
| 1318   | Layout 2 | `ebacd74a4c55`  |
| 1316   | Layout 2 | `ebacd74a4c55`  |
| 1313   | Layout 2 | `ebacd74a4c55`  |
| 1311   | Layout 2 | `ebacd74a4c55`  |
| 1309   | Layout 2 | `ebacd74a4c55`  |
| 1304   | Layout 2 | `ebacd74a4c55`  |
| 1292   | Layout 2 | `ebacd74a4c55`  |
| 1286   | Layout 2 | `ebacd74a4c55`  |
| 1280   | Layout 2 | `ebacd74a4c55`  |
| 1276   | Layout 2 | `ebacd74a4c55`  |
| 1267   | Layout 2 | `ebacd74a4c55`  |
| 1261   | Layout 1 | `ebacd74a4c55`  |
| 1256   | Layout 1 | `ebacd74a4c55`  |
| 1250   | Layout 1 | `ebacd74a4c55`  |
| 1246   | Layout 1 | `ebacd74a4c55`  |
| 1239   | Layout 1 | `ebacd74a4c55`  |
| 1230   | Layout 1 | `ebacd74a4c55`  |
| 1226   | Layout 1 | `ebacd74a4c55`  |
| 1220   | No file  | `ebacd74a4c55`  |
| 1217   | No file  | `ebacd74a4c55`  |
| 1211   | No file  | `ebacd74a4c55`  |
| 1210   | No file  | `ebacd74a4c55`  |
| 1208   | No file  | `ebacd74a4c55`  |
| 1203   | No file  | `ebacd74a4c55`  |
| 1197   | No file  | `ebacd74a4c55`  |
| 1194   | No file  | `ebacd74a4c55`  |
| 1192   | No file  | `ebacd74a4c55`  |
| 1187   | No file  | `ebacd74a4c55`  |
| 1183   | No file  | `ebacd74a4c55`  |
| 1177   | No file  | `ebacd74a4c55`  |
| 1173   | No file  | `ebacd74a4c55`  |
| 1167   | No file  | `ebacd74a4c55`  |
| 1164   | No file  | `ebacd74a4c55`  |
| 1156   | No file  | `ebacd74a4c55`  |
| 1149   | No file  | `ebacd74a4c55`  |
| 1144   | No file  | `ebacd74a4c55`  |
| 1137   | No file  | `ebacd74a4c55`  |
| 1132   | No file  | `ebacd74a4c55`  |
| 1127   | No file  | `ebacd74a4c55`  |
| 1122   | No file  | `ebacd74a4c55`  |
| 1118   | No file  | `ebacd74a4c55`  |
| 1114   | No file  | `ebacd74a4c55`  |
| 1109   | No file  | `ebacd74a4c55`  |
| 1102   | No file  | `ebacd74a4c55`  |
| 1096   | No file  | `ebacd74a4c55`  |
| 1088   | No file  | `ebacd74a4c55`  |
| 1081   | No file  | `ebacd74a4c55`  |
| 1076   | No file  | `ebacd74a4c55`  |
| 1069   | No file  | `ebacd74a4c55`  |
| 1064   | No file  | `ebacd74a4c55`  |
| 1058   | No file  | `ebacd74a4c55`  |
| 1051   | No file  | `ebacd74a4c55`  |
| 1044   | No file  | `ebacd74a4c55`  |
| 1036   | No file  | `ebacd74a4c55`  |
| 1026   | No file  | `ebacd74a4c55`  |
| 1016   | No file  | `ebacd74a4c55`  |
| 1009   | No file  | `ebacd74a4c55`  |
| 1005   | No file  | `ebacd74a4c55`  |
| 1000   | No file  | `ebacd74a4c55`  |
| 998    | No file  | `ebacd74a4c55`  |
| 990    | No file  | `ebacd74a4c55`  |
| 979    | No file  | `ebacd74a4c55`  |
| 972    | No file  | `ebacd74a4c55`  |
| 963    | No file  | `ebacd74a4c55`  |
| 955    | No file  | `ebacd74a4c55`  |
| 946    | No file  | `ebacd74a4c55`  |
| 938    | No file  | `ebacd74a4c55`  |
| 927    | No file  | `ebacd74a4c55`  |
| 911    | No file  | `ebacd74a4c55`  |
| 904    | No file  | `ebacd74a4c55`  |
| 899    | No file  | `ebacd74a4c55`  |
| 894    | No file  | `ebacd74a4c55`  |
| 885    | No file  | `ebacd74a4c55`  |
| 879    | No file  | `ebacd74a4c55`  |
| 872    | No file  | `ebacd74a4c55`  |
| 864    | No file  | `ebacd74a4c55`  |
| 855    | No file  | `ebacd74a4c55`  |
| 853    | No file  | `ebacd74a4c55`  |
| 845    | No file  | `ebacd74a4c55`  |
| 837    | No file  | `ebacd74a4c55`  |
| 829    | No file  | `ebacd74a4c55`  |
| 822    | No file  | `ebacd74a4c55`  |
| 814    | No file  | `ebacd74a4c55`  |
| 805    | No file  | `ebacd74a4c55`  |
| 794    | No file  | `ebacd74a4c55`  |
| 787    | No file  | `ebacd74a4c55`  |
| 780    | No file  | `ebacd74a4c55`  |
| 771    | No file  | `ebacd74a4c55`  |
| 760    | No file  | `ebacd74a4c55`  |
| 748    | No file  | `ebacd74a4c55`  |
| 741    | No file  | `ebacd74a4c55`  |
| 736    | No file  | `ebacd74a4c55`  |
| 731    | No file  | `ebacd74a4c55`  |
| 723    | No file  | `ebacd74a4c55`  |
| 711    | No file  | `ebacd74a4c55`  |
| 707    | No file  | `ebacd74a4c55`  |
| 697    | No file  | `ebacd74a4c55`  |
| 689    | No file  | `ebacd74a4c55`  |
| 683    | No file  | `ebacd74a4c55`  |
| 678    | No file  | `ebacd74a4c55`  |
| 670    | No file  | `ebacd74a4c55`  |
| 661    | No file  | `ebacd74a4c55`  |
| 656    | No file  | `ebacd74a4c55`  |
| 652    | No file  | `ebacd74a4c55`  |
| 643    | No file  | `ebacd74a4c55`  |
| 637    | No file  | `ebacd74a4c55`  |
| 630    | No file  | `ebacd74a4c55`  |
| 627    | No file  | `ebacd74a4c55`  |
| 621    | No file  | `ebacd74a4c55`  |
| 617    | No file  | `ebacd74a4c55`  |
| 615    | No file  | `ebacd74a4c55`  |
| 606    | No file  | `ebacd74a4c55`  |
| 599    | No file  | `ebacd74a4c55`  |
| 592    | No file  | `ebacd74a4c55`  |
| 586    | No file  | `ebacd74a4c55`  |
| 577    | No file  | `ebacd74a4c55`  |
| 569    | No file  | `ebacd74a4c55`  |
| 561    | No file  | `ebacd74a4c55`  |
| 554    | No file  | `ebacd74a4c55`  |
| 542    | No file  | `ebacd74a4c55`  |
| 532    | No file  | `ebacd74a4c55`  |
| 531    | No file  | `ebacd74a4c55`  |
| 526    | No file  | `ebacd74a4c55`  |
| 521    | No file  | `ebacd74a4c55`  |
| 517    | No file  | `ebacd74a4c55`  |
| 510    | No file  | `ebacd74a4c55`  |
| 508    | No file  | `ebacd74a4c55`  |
| 504    | No file  | `ebacd74a4c55`  |
| 497    | No file  | `ebacd74a4c55`  |
| 491    | No file  | `ebacd74a4c55`  |
| 485    | No file  | `ebacd74a4c55`  |
| 478    | No file  | `ebacd74a4c55`  |
| 472    | No file  | `ebacd74a4c55`  |
| 466    | No file  | `ebacd74a4c55`  |
| 457    | No file  | `ebacd74a4c55`  |
| 452    | No file  | `ebacd74a4c55`  |
| 449    | No file  | `ebacd74a4c55`  |
| 435    | No file  | `ebacd74a4c55`  |

<!-- versions:end -->

## Companion Files

The file is self-contained. The handler reads names through the shared LOC
lookup and the skill icons through the skill icon index:

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Skill names (LOC type `10`, `str_id1` = skill number) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                                |
| ------------------- | -------------- | ------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                         |
| `+0x04`             | u32            | skill_count  | Number of rows; `29699` on client 3483               |
| `+0x08`             | Row[skill_count] | rows       | See Row                                              |
| `rows+0x00`         | String Table   | string_table | Empty: `string_count` is `0`                         |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends        |
| `string_table+0x04` | u32            | zero         | Always `0`                                           |

On client 3483 the rows end at `0x5702C`, the stored `table_start`, and the
file is 356,408 bytes. The parser rejects a file whose rows do not end
there.

### Row (12 bytes)

| Offset  | Type | Field      | Notes                                                                 |
| ------- | ---- | ---------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | skill_key  | `skill_no << 16 \| level`; level `1` on every row, each skill once    |
| `+0x04` | u64  | unknown_04 | One value on every row, the every-class mask of `skillsimply.dbss`; see [Open Questions](#open-questions) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                        |
| ------- | ------------------ | ------------ | ---------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3483 |
| `+0x04` | pstr[string_count] | strings      | No field reads a string      |

## Layout 1

The File Layout and String Table of Layout 2, with a 36-byte Row:
`unknown_04` is 32 bytes, as the class set of Layout 1 of
[`privateskill.bss`](privateskill_bss.md) is one byte per class type.

### Row (36 bytes)

| Offset  | Type   | Field      | Notes                                                             |
| ------- | ------ | ---------- | ----------------------------------------------------------------- |
| `+0x00` | u32    | skill_key  | `skill_no << 16 \| level`; level `1` on every row                 |
| `+0x04` | u8[32] | unknown_04 | Every byte `1` on every row of client 1230                        |

On client 1230 the file holds 17,607 rows, every row level `1` with all 32
bytes `1`.

## Skill Keys

On client 3483 the 29,699 keys are exactly the 14,405 keys of
`publicskill.bss` and the 10,044 active and 5,250 passive keys of
`privateskill.bss`, each once. They are every level `1` key of
[`skillsimply.dbss`](../dbss/skillsimply_dbss.md) whose `skill_owner_type` is `0`;
the 766 guild skills (`skill_owner_type` `1`) are left out. Client 1784
has the same split: 22,160 rows, the 11,327 keys of its `publicskill.bss`
and the 10,833 of its `privateskill.bss`, with the 724 guild skills left
out.

The rows are in no key order, and not in the order of the two other files
either: the first keys are `57005`, `57004`, `57007` and `57006`, as in
`publicskill.bss`, but from the 88th row on (client 3483) keys of the two
files mix.

## `unknown_04` Values

Every row holds the mask `skillsimply.dbss` `class_mask` stores for a skill
every class can learn, on both checked clients:

| Client | `unknown_04` on every row      | `skillsimply.dbss` every-class value |
| ------ | ------------------------------ | ------------------------------------ |
| 3483   | `0x7FFFFFFFFFFF` (47 bits)     | `0x7FFFFFFFFFFF`                     |
| 1784   | `0xFFFFFFFFFFFFFFFF` (64 bits) | `0xFFFFFFFFFFFFFFFF`                 |

It is not the learning mask of the skill: on client 3483 it equals the
`skillsimply.dbss` `class_mask` of the same key on 17,572 of 29,699 rows,
the skills every class learns. The other 12,127 rows, such as the Warrior
skill `216` Ground Roar, have one class or none there.

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 has a
skill class type name, no string of that server's executable names the
file, the 2016 PDB has no type of that name, and no `.luac` on client 3482
holds a name with `SkillClassType` in it. The `binary/` folder of that
private server holds the file, 26,806 rows in the same layout, every row
level `1` and `0xFFFFFFFFFFFFFFFF`.

| Field     | Source                                                                  |
| --------- | ----------------------------------------------------------------------- |
| skill_key | The `skill_no << 16 \| level` key of every skill table; 29,699 of 29,699 keys are `skillsimply.dbss` keys (client 3483) |

## Notes

- The handler shows one row per key: the skill number linked to its
  `skill.dbss` row, then the skill icon and LOC type `10` name, as the
  `publicskill.bss` handler does.

## Open Questions

### What `unknown_04` Is

The lead is a class mask. The file name says `ClassType`; the value
follows the every-class mask of `skillsimply.dbss` `class_mask` (the 2016
`_usableClassType`) from 64 bits on client 1784 to 47 bits on client 3483;
and `privateskill.bss` stores the same row of u32 skill key and u64
`class_mask`, with a 32-byte class set in its older layout as Layout 1
here has. Against it, the value differs from the `skillsimply.dbss` mask
of the same key on 12,127 of 29,699 rows (client 3483), so it is not the
learning mask. With the same value on every row, the file tells the
client nothing a skill key alone does not. No loader for the file has
been traced in an executable. The skill window's panel for viewing other
classes' skills (`panel_window_skill_showallclasses_all.luac`) is a
candidate reader: it lists every class type and calls
`PaGlobalFunc_SkillGroup_All_ShowOtherClassSkill`.
