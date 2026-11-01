# `privateskill.bss` Format

## Purpose

The active and passive skills and the classes that can learn each: two
lists of a level `1` skill key and its class mask, the first for every
active skill (`kind` `1`) and the second for every passive skill (`kind`
`2`) whose `skill_owner_type` is `0`. The item and event skills are in
[`publicskill.bss`](publicskill_bss.md), which has its own layout; its
[Skill Keys](publicskill_bss.md#skill-keys) section splits the skills of
`skillsimply.dbss` over the three lists.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File               | Bytes   | Records    | Row bytes |
| ------ | -------------- | ------------------ | ------- | ---------- | --------- |
| 2      | 1267 and later | `privateskill.bss` | 183,552 | 15,294 Row | 12        |
| 1      | 1194 to 1261   | `privateskill.bss` | 302,892 | 8,413 Row  | 36        |

| Layout | File               | Known              | Unknown    |
| ------ | ------------------ | ------------------ | ---------- |
| 2      | `privateskill.bss` | 183,552 B (100.0%) | 0 B (0.0%) |
| 1      | `privateskill.bss` | 302,892 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `fe79e8d2483d`  |
| 3482   | Layout 2 | `fe79e8d2483d`  |
| 3474   | Layout 2 | `fe79e8d2483d`  |
| 3473   | Layout 2 | `fe79e8d2483d`  |
| 3464   | Layout 2 | `fe79e8d2483d`  |
| 3458   | Layout 2 | `fe79e8d2483d`  |
| 3454   | Layout 2 | `fe79e8d2483d`  |
| 3444   | Layout 2 | `fe79e8d2483d`  |
| 3435   | Layout 2 | `fe79e8d2483d`  |
| 3426   | Layout 2 | `fe79e8d2483d`  |
| 3418   | Layout 2 | `fe79e8d2483d`  |
| 3412   | Layout 2 | `fe79e8d2483d`  |
| 3402   | Layout 2 | `fe79e8d2483d`  |
| 3396   | Layout 2 | `fe79e8d2483d`  |
| 3387   | Layout 2 | `fe79e8d2483d`  |
| 3381   | Layout 2 | `fe79e8d2483d`  |
| 3373   | Layout 2 | `fe79e8d2483d`  |
| 3364   | Layout 2 | `fe79e8d2483d`  |
| 3356   | Layout 2 | `fe79e8d2483d`  |
| 3349   | Layout 2 | `fe79e8d2483d`  |
| 3342   | Layout 2 | `fe79e8d2483d`  |
| 3335   | Layout 2 | `fe79e8d2483d`  |
| 3326   | Layout 2 | `fe79e8d2483d`  |
| 3321   | Layout 2 | `fe79e8d2483d`  |
| 3314   | Layout 2 | `fe79e8d2483d`  |
| 3303   | Layout 2 | `fe79e8d2483d`  |
| 3302   | Layout 2 | `fe79e8d2483d`  |
| 3293   | Layout 2 | `fe79e8d2483d`  |
| 3283   | Layout 2 | `fe79e8d2483d`  |
| 3275   | Layout 2 | `fe79e8d2483d`  |
| 3267   | Layout 2 | `fe79e8d2483d`  |
| 3258   | Layout 2 | `fe79e8d2483d`  |
| 3251   | Layout 2 | `fe79e8d2483d`  |
| 3242   | Layout 2 | `fe79e8d2483d`  |
| 3235   | Layout 2 | `fe79e8d2483d`  |
| 3229   | Layout 2 | `fe79e8d2483d`  |
| 3212   | Layout 2 | `fe79e8d2483d`  |
| 3203   | Layout 2 | `fe79e8d2483d`  |
| 3193   | Layout 2 | `fe79e8d2483d`  |
| 3186   | Layout 2 | `fe79e8d2483d`  |
| 3177   | Layout 2 | `fe79e8d2483d`  |
| 3169   | Layout 2 | `fe79e8d2483d`  |
| 3158   | Layout 2 | `fe79e8d2483d`  |
| 3151   | Layout 2 | `fe79e8d2483d`  |
| 3144   | Layout 2 | `fe79e8d2483d`  |
| 3133   | Layout 2 | `fe79e8d2483d`  |
| 3125   | Layout 2 | `fe79e8d2483d`  |
| 3118   | Layout 2 | `fe79e8d2483d`  |
| 3111   | Layout 2 | `fe79e8d2483d`  |
| 3103   | Layout 2 | `fe79e8d2483d`  |
| 3095   | Layout 2 | `fe79e8d2483d`  |
| 3086   | Layout 2 | `fe79e8d2483d`  |
| 3072   | Layout 2 | `fe79e8d2483d`  |
| 3062   | Layout 2 | `fe79e8d2483d`  |
| 3052   | Layout 2 | `fe79e8d2483d`  |
| 3045   | Layout 2 | `fe79e8d2483d`  |
| 3037   | Layout 2 | `fe79e8d2483d`  |
| 3030   | Layout 2 | `fe79e8d2483d`  |
| 3021   | Layout 2 | `fe79e8d2483d`  |
| 3012   | Layout 2 | `fe79e8d2483d`  |
| 3002   | Layout 2 | `fe79e8d2483d`  |
| 2995   | Layout 2 | `fe79e8d2483d`  |
| 2987   | Layout 2 | `fe79e8d2483d`  |
| 2978   | Layout 2 | `fe79e8d2483d`  |
| 2970   | Layout 2 | `fe79e8d2483d`  |
| 2959   | Layout 2 | `fe79e8d2483d`  |
| 2951   | Layout 2 | `fe79e8d2483d`  |
| 2942   | Layout 2 | `fe79e8d2483d`  |
| 2935   | Layout 2 | `fe79e8d2483d`  |
| 2932   | Layout 2 | `fe79e8d2483d`  |
| 2923   | Layout 2 | `fe79e8d2483d`  |
| 2919   | Layout 2 | `fe79e8d2483d`  |
| 2907   | Layout 2 | `fe79e8d2483d`  |
| 2900   | Layout 2 | `fe79e8d2483d`  |
| 2891   | Layout 2 | `fe79e8d2483d`  |
| 2882   | Layout 2 | `fe79e8d2483d`  |
| 2872   | Layout 2 | `fe79e8d2483d`  |
| 2863   | Layout 2 | `fe79e8d2483d`  |
| 2855   | Layout 2 | `fe79e8d2483d`  |
| 2849   | Layout 2 | `fe79e8d2483d`  |
| 2844   | Layout 2 | `fe79e8d2483d`  |
| 2834   | Layout 2 | `fe79e8d2483d`  |
| 2825   | Layout 2 | `fe79e8d2483d`  |
| 2819   | Layout 2 | `fe79e8d2483d`  |
| 2811   | Layout 2 | `fe79e8d2483d`  |
| 2803   | Layout 2 | `fe79e8d2483d`  |
| 2794   | Layout 2 | `fe79e8d2483d`  |
| 2783   | Layout 2 | `fe79e8d2483d`  |
| 2774   | Layout 2 | `fe79e8d2483d`  |
| 2765   | Layout 2 | `fe79e8d2483d`  |
| 2756   | Layout 2 | `fe79e8d2483d`  |
| 2750   | Layout 2 | `fe79e8d2483d`  |
| 2743   | Layout 2 | `fe79e8d2483d`  |
| 2736   | Layout 2 | `fe79e8d2483d`  |
| 2726   | Layout 2 | `fe79e8d2483d`  |
| 2717   | Layout 2 | `fe79e8d2483d`  |
| 2709   | Layout 2 | `fe79e8d2483d`  |
| 2703   | Layout 2 | `fe79e8d2483d`  |
| 2695   | Layout 2 | `fe79e8d2483d`  |
| 2684   | Layout 2 | `fe79e8d2483d`  |
| 2672   | Layout 2 | `fe79e8d2483d`  |
| 2665   | Layout 2 | `fe79e8d2483d`  |
| 2657   | Layout 2 | `fe79e8d2483d`  |
| 2649   | Layout 2 | `fe79e8d2483d`  |
| 2644   | Layout 2 | `fe79e8d2483d`  |
| 2637   | Layout 2 | `fe79e8d2483d`  |
| 2629   | Layout 2 | `fe79e8d2483d`  |
| 2619   | Layout 2 | `fe79e8d2483d`  |
| 2612   | Layout 2 | `fe79e8d2483d`  |
| 2606   | Layout 2 | `fe79e8d2483d`  |
| 2602   | Layout 2 | `fe79e8d2483d`  |
| 2601   | Layout 2 | `fe79e8d2483d`  |
| 2592   | Layout 2 | `fe79e8d2483d`  |
| 2583   | Layout 2 | `fe79e8d2483d`  |
| 2575   | Layout 2 | `fe79e8d2483d`  |
| 2567   | Layout 2 | `fe79e8d2483d`  |
| 2560   | Layout 2 | `fe79e8d2483d`  |
| 2553   | Layout 2 | `fe79e8d2483d`  |
| 2545   | Layout 2 | `fe79e8d2483d`  |
| 2538   | Layout 2 | `fe79e8d2483d`  |
| 2529   | Layout 2 | `fe79e8d2483d`  |
| 2519   | Layout 2 | `fe79e8d2483d`  |
| 2513   | Layout 2 | `fe79e8d2483d`  |
| 2510   | Layout 2 | `fe79e8d2483d`  |
| 2507   | Layout 2 | `fe79e8d2483d`  |
| 2503   | Layout 2 | `fe79e8d2483d`  |
| 2498   | Layout 2 | `fe79e8d2483d`  |
| 2492   | Layout 2 | `fe79e8d2483d`  |
| 2487   | Layout 2 | `fe79e8d2483d`  |
| 2480   | Layout 2 | `fe79e8d2483d`  |
| 2474   | Layout 2 | `fe79e8d2483d`  |
| 2468   | Layout 2 | `fe79e8d2483d`  |
| 2460   | Layout 2 | `fe79e8d2483d`  |
| 2453   | Layout 2 | `fe79e8d2483d`  |
| 2444   | Layout 2 | `fe79e8d2483d`  |
| 2438   | Layout 2 | `fe79e8d2483d`  |
| 2434   | Layout 2 | `fe79e8d2483d`  |
| 2429   | Layout 2 | `fe79e8d2483d`  |
| 2421   | Layout 2 | `fe79e8d2483d`  |
| 2414   | Layout 2 | `fe79e8d2483d`  |
| 2407   | Layout 2 | `fe79e8d2483d`  |
| 2401   | Layout 2 | `fe79e8d2483d`  |
| 2397   | Layout 2 | `fe79e8d2483d`  |
| 2393   | Layout 2 | `fe79e8d2483d`  |
| 2384   | Layout 2 | `fe79e8d2483d`  |
| 2378   | Layout 2 | `fe79e8d2483d`  |
| 2372   | Layout 2 | `fe79e8d2483d`  |
| 2358   | Layout 2 | `fe79e8d2483d`  |
| 2352   | Layout 2 | `fe79e8d2483d`  |
| 2347   | Layout 2 | `fe79e8d2483d`  |
| 2343   | Layout 2 | `fe79e8d2483d`  |
| 2335   | Layout 2 | `fe79e8d2483d`  |
| 2327   | Layout 2 | `fe79e8d2483d`  |
| 2324   | Layout 2 | `fe79e8d2483d`  |
| 2319   | Layout 2 | `fe79e8d2483d`  |
| 2313   | Layout 2 | `fe79e8d2483d`  |
| 2308   | Layout 2 | `fe79e8d2483d`  |
| 2302   | Layout 2 | `fe79e8d2483d`  |
| 2295   | Layout 2 | `fe79e8d2483d`  |
| 2290   | Layout 2 | `fe79e8d2483d`  |
| 2284   | Layout 2 | `fe79e8d2483d`  |
| 2276   | Layout 2 | `fe79e8d2483d`  |
| 2269   | Layout 2 | `fe79e8d2483d`  |
| 2259   | Layout 2 | `fe79e8d2483d`  |
| 2250   | Layout 2 | `fe79e8d2483d`  |
| 2243   | Layout 2 | `fe79e8d2483d`  |
| 2235   | Layout 2 | `fe79e8d2483d`  |
| 2229   | Layout 2 | `fe79e8d2483d`  |
| 2224   | Layout 2 | `fe79e8d2483d`  |
| 2218   | Layout 2 | `fe79e8d2483d`  |
| 2215   | Layout 2 | `fe79e8d2483d`  |
| 2207   | Layout 2 | `fe79e8d2483d`  |
| 2203   | Layout 2 | `fe79e8d2483d`  |
| 2196   | Layout 2 | `fe79e8d2483d`  |
| 2192   | Layout 2 | `fe79e8d2483d`  |
| 2189   | Layout 2 | `fe79e8d2483d`  |
| 2183   | Layout 2 | `fe79e8d2483d`  |
| 2179   | Layout 2 | `fe79e8d2483d`  |
| 2171   | Layout 2 | `fe79e8d2483d`  |
| 2163   | Layout 2 | `fe79e8d2483d`  |
| 2156   | Layout 2 | `fe79e8d2483d`  |
| 2151   | Layout 2 | `fe79e8d2483d`  |
| 2147   | Layout 2 | `fe79e8d2483d`  |
| 2142   | Layout 2 | `fe79e8d2483d`  |
| 2138   | Layout 2 | `fe79e8d2483d`  |
| 2134   | Layout 2 | `fe79e8d2483d`  |
| 2130   | Layout 2 | `fe79e8d2483d`  |
| 2122   | Layout 2 | `fe79e8d2483d`  |
| 2107   | Layout 2 | `fe79e8d2483d`  |
| 2098   | Layout 2 | `fe79e8d2483d`  |
| 2089   | Layout 2 | `fe79e8d2483d`  |
| 2081   | Layout 2 | `fe79e8d2483d`  |
| 2073   | Layout 2 | `fe79e8d2483d`  |
| 2067   | Layout 2 | `fe79e8d2483d`  |
| 2063   | Layout 2 | `fe79e8d2483d`  |
| 2059   | Layout 2 | `fe79e8d2483d`  |
| 2052   | Layout 2 | `fe79e8d2483d`  |
| 2044   | Layout 2 | `fe79e8d2483d`  |
| 2039   | Layout 2 | `fe79e8d2483d`  |
| 2032   | Layout 2 | `fe79e8d2483d`  |
| 2025   | Layout 2 | `fe79e8d2483d`  |
| 2011   | Layout 2 | `fe79e8d2483d`  |
| 2005   | Layout 2 | `fe79e8d2483d`  |
| 2000   | Layout 2 | `fe79e8d2483d`  |
| 1996   | Layout 2 | `fe79e8d2483d`  |
| 1991   | Layout 2 | `fe79e8d2483d`  |
| 1985   | Layout 2 | `fe79e8d2483d`  |
| 1980   | Layout 2 | `fe79e8d2483d`  |
| 1969   | Layout 2 | `fe79e8d2483d`  |
| 1964   | Layout 2 | `fe79e8d2483d`  |
| 1958   | Layout 2 | `fe79e8d2483d`  |
| 1950   | Layout 2 | `fe79e8d2483d`  |
| 1945   | Layout 2 | `fe79e8d2483d`  |
| 1937   | Layout 2 | `fe79e8d2483d`  |
| 1933   | Layout 2 | `fe79e8d2483d`  |
| 1927   | Layout 2 | `fe79e8d2483d`  |
| 1921   | Layout 2 | `fe79e8d2483d`  |
| 1914   | Layout 2 | `fe79e8d2483d`  |
| 1908   | Layout 2 | `fe79e8d2483d`  |
| 1897   | Layout 2 | `fe79e8d2483d`  |
| 1892   | Layout 2 | `fe79e8d2483d`  |
| 1886   | Layout 2 | `fe79e8d2483d`  |
| 1881   | Layout 2 | `fe79e8d2483d`  |
| 1871   | Layout 2 | `fe79e8d2483d`  |
| 1866   | Layout 2 | `fe79e8d2483d`  |
| 1862   | Layout 2 | `fe79e8d2483d`  |
| 1854   | Layout 2 | `fe79e8d2483d`  |
| 1846   | Layout 2 | `fe79e8d2483d`  |
| 1838   | Layout 2 | `fe79e8d2483d`  |
| 1832   | Layout 2 | `fe79e8d2483d`  |
| 1826   | Layout 2 | `fe79e8d2483d`  |
| 1822   | Layout 2 | `fe79e8d2483d`  |
| 1818   | Layout 2 | `fe79e8d2483d`  |
| 1804   | Layout 2 | `fe79e8d2483d`  |
| 1794   | Layout 2 | `fe79e8d2483d`  |
| 1790   | Layout 2 | `fe79e8d2483d`  |
| 1784   | Layout 2 | `fe79e8d2483d`  |
| 1774   | Layout 2 | `fe79e8d2483d`  |
| 1771   | Layout 2 | `fe79e8d2483d`  |
| 1762   | Layout 2 | `fe79e8d2483d`  |
| 1759   | Layout 2 | `fe79e8d2483d`  |
| 1754   | Layout 2 | `fe79e8d2483d`  |
| 1749   | Layout 2 | `fe79e8d2483d`  |
| 1743   | Layout 2 | `fe79e8d2483d`  |
| 1737   | Layout 2 | `fe79e8d2483d`  |
| 1731   | Layout 2 | `fe79e8d2483d`  |
| 1725   | Layout 2 | `fe79e8d2483d`  |
| 1717   | Layout 2 | `fe79e8d2483d`  |
| 1710   | Layout 2 | `fe79e8d2483d`  |
| 1704   | Layout 2 | `fe79e8d2483d`  |
| 1698   | Layout 2 | `fe79e8d2483d`  |
| 1690   | Layout 2 | `fe79e8d2483d`  |
| 1685   | Layout 2 | `fe79e8d2483d`  |
| 1680   | Layout 2 | `fe79e8d2483d`  |
| 1674   | Layout 2 | `fe79e8d2483d`  |
| 1668   | Layout 2 | `fe79e8d2483d`  |
| 1659   | Layout 2 | `fe79e8d2483d`  |
| 1649   | Layout 2 | `fe79e8d2483d`  |
| 1642   | Layout 2 | `fe79e8d2483d`  |
| 1636   | Layout 2 | `fe79e8d2483d`  |
| 1628   | Layout 2 | `fe79e8d2483d`  |
| 1622   | Layout 2 | `fe79e8d2483d`  |
| 1614   | Layout 2 | `fe79e8d2483d`  |
| 1608   | Layout 2 | `fe79e8d2483d`  |
| 1602   | Layout 2 | `fe79e8d2483d`  |
| 1598   | Layout 2 | `fe79e8d2483d`  |
| 1594   | Layout 2 | `fe79e8d2483d`  |
| 1590   | Layout 2 | `fe79e8d2483d`  |
| 1587   | Layout 2 | `fe79e8d2483d`  |
| 1584   | Layout 2 | `fe79e8d2483d`  |
| 1579   | Layout 2 | `fe79e8d2483d`  |
| 1572   | Layout 2 | `fe79e8d2483d`  |
| 1565   | Layout 2 | `fe79e8d2483d`  |
| 1559   | Layout 2 | `fe79e8d2483d`  |
| 1554   | Layout 2 | `fe79e8d2483d`  |
| 1547   | Layout 2 | `fe79e8d2483d`  |
| 1537   | Layout 2 | `fe79e8d2483d`  |
| 1529   | Layout 2 | `fe79e8d2483d`  |
| 1524   | Layout 2 | `fe79e8d2483d`  |
| 1519   | Layout 2 | `fe79e8d2483d`  |
| 1509   | Layout 2 | `fe79e8d2483d`  |
| 1506   | Layout 2 | `fe79e8d2483d`  |
| 1504   | Layout 2 | `fe79e8d2483d`  |
| 1500   | Layout 2 | `fe79e8d2483d`  |
| 1493   | Layout 2 | `fe79e8d2483d`  |
| 1489   | Layout 2 | `fe79e8d2483d`  |
| 1485   | Layout 2 | `fe79e8d2483d`  |
| 1481   | Layout 2 | `fe79e8d2483d`  |
| 1474   | Layout 2 | `fe79e8d2483d`  |
| 1466   | Layout 2 | `fe79e8d2483d`  |
| 1462   | Layout 2 | `fe79e8d2483d`  |
| 1459   | Layout 2 | `fe79e8d2483d`  |
| 1453   | Layout 2 | `fe79e8d2483d`  |
| 1450   | Layout 2 | `fe79e8d2483d`  |
| 1445   | Layout 2 | `fe79e8d2483d`  |
| 1439   | Layout 2 | `fe79e8d2483d`  |
| 1433   | Layout 2 | `fe79e8d2483d`  |
| 1430   | Layout 2 | `fe79e8d2483d`  |
| 1426   | Layout 2 | `fe79e8d2483d`  |
| 1421   | Layout 2 | `fe79e8d2483d`  |
| 1417   | Layout 2 | `fe79e8d2483d`  |
| 1416   | Layout 2 | `fe79e8d2483d`  |
| 1409   | Layout 2 | `fe79e8d2483d`  |
| 1405   | Layout 2 | `fe79e8d2483d`  |
| 1401   | Layout 2 | `fe79e8d2483d`  |
| 1396   | Layout 2 | `fe79e8d2483d`  |
| 1391   | Layout 2 | `fe79e8d2483d`  |
| 1390   | Layout 2 | `fe79e8d2483d`  |
| 1386   | Layout 2 | `fe79e8d2483d`  |
| 1381   | Layout 2 | `fe79e8d2483d`  |
| 1379   | Layout 2 | `fe79e8d2483d`  |
| 1372   | Layout 2 | `fe79e8d2483d`  |
| 1366   | Layout 2 | `fe79e8d2483d`  |
| 1364   | Layout 2 | `fe79e8d2483d`  |
| 1363   | Layout 2 | `fe79e8d2483d`  |
| 1360   | Layout 2 | `fe79e8d2483d`  |
| 1358   | Layout 2 | `fe79e8d2483d`  |
| 1355   | Layout 2 | `fe79e8d2483d`  |
| 1351   | Layout 2 | `fe79e8d2483d`  |
| 1348   | Layout 2 | `fe79e8d2483d`  |
| 1346   | Layout 2 | `fe79e8d2483d`  |
| 1341   | Layout 2 | `fe79e8d2483d`  |
| 1340   | Layout 2 | `fe79e8d2483d`  |
| 1338   | Layout 2 | `fe79e8d2483d`  |
| 1335   | Layout 2 | `fe79e8d2483d`  |
| 1333   | Layout 2 | `fe79e8d2483d`  |
| 1329   | Layout 2 | `fe79e8d2483d`  |
| 1327   | Layout 2 | `fe79e8d2483d`  |
| 1324   | Layout 2 | `fe79e8d2483d`  |
| 1321   | Layout 2 | `fe79e8d2483d`  |
| 1319   | Layout 2 | `fe79e8d2483d`  |
| 1318   | Layout 2 | `fe79e8d2483d`  |
| 1316   | Layout 2 | `fe79e8d2483d`  |
| 1313   | Layout 2 | `fe79e8d2483d`  |
| 1311   | Layout 2 | `fe79e8d2483d`  |
| 1309   | Layout 2 | `fe79e8d2483d`  |
| 1304   | Layout 2 | `fe79e8d2483d`  |
| 1292   | Layout 2 | `fe79e8d2483d`  |
| 1286   | Layout 2 | `fe79e8d2483d`  |
| 1280   | Layout 2 | `fe79e8d2483d`  |
| 1276   | Layout 2 | `fe79e8d2483d`  |
| 1267   | Layout 2 | `fe79e8d2483d`  |
| 1261   | Layout 1 | `fe79e8d2483d`  |
| 1256   | Layout 1 | `fe79e8d2483d`  |
| 1250   | Layout 1 | `fe79e8d2483d`  |
| 1246   | Layout 1 | `fe79e8d2483d`  |
| 1239   | Layout 1 | `fe79e8d2483d`  |
| 1230   | Layout 1 | `fe79e8d2483d`  |
| 1226   | Layout 1 | `fe79e8d2483d`  |
| 1220   | Layout 1 | `fe79e8d2483d`  |
| 1217   | Layout 1 | `fe79e8d2483d`  |
| 1211   | Layout 1 | `fe79e8d2483d`  |
| 1210   | Layout 1 | `fe79e8d2483d`  |
| 1208   | Layout 1 | `fe79e8d2483d`  |
| 1203   | Layout 1 | `fe79e8d2483d`  |
| 1197   | Layout 1 | `fe79e8d2483d`  |
| 1194   | Layout 1 | `fe79e8d2483d`  |
| 1192   | No file  | `fe79e8d2483d`  |
| 1187   | No file  | `fe79e8d2483d`  |
| 1183   | No file  | `fe79e8d2483d`  |
| 1177   | No file  | `fe79e8d2483d`  |
| 1173   | No file  | `fe79e8d2483d`  |
| 1167   | No file  | `fe79e8d2483d`  |
| 1164   | No file  | `fe79e8d2483d`  |
| 1156   | No file  | `fe79e8d2483d`  |
| 1149   | No file  | `fe79e8d2483d`  |
| 1144   | No file  | `fe79e8d2483d`  |
| 1137   | No file  | `fe79e8d2483d`  |
| 1132   | No file  | `fe79e8d2483d`  |
| 1127   | No file  | `fe79e8d2483d`  |
| 1122   | No file  | `fe79e8d2483d`  |
| 1118   | No file  | `fe79e8d2483d`  |
| 1114   | No file  | `fe79e8d2483d`  |
| 1109   | No file  | `fe79e8d2483d`  |
| 1102   | No file  | `fe79e8d2483d`  |
| 1096   | No file  | `fe79e8d2483d`  |
| 1088   | No file  | `fe79e8d2483d`  |
| 1081   | No file  | `fe79e8d2483d`  |
| 1076   | No file  | `fe79e8d2483d`  |
| 1069   | No file  | `fe79e8d2483d`  |
| 1064   | No file  | `fe79e8d2483d`  |
| 1058   | No file  | `fe79e8d2483d`  |
| 1051   | No file  | `fe79e8d2483d`  |
| 1044   | No file  | `fe79e8d2483d`  |
| 1036   | No file  | `fe79e8d2483d`  |
| 1026   | No file  | `fe79e8d2483d`  |
| 1016   | No file  | `fe79e8d2483d`  |
| 1009   | No file  | `fe79e8d2483d`  |
| 1005   | No file  | `fe79e8d2483d`  |
| 1000   | No file  | `fe79e8d2483d`  |
| 998    | No file  | `fe79e8d2483d`  |
| 990    | No file  | `fe79e8d2483d`  |
| 979    | No file  | `fe79e8d2483d`  |
| 972    | No file  | `fe79e8d2483d`  |
| 963    | No file  | `fe79e8d2483d`  |
| 955    | No file  | `fe79e8d2483d`  |
| 946    | No file  | `fe79e8d2483d`  |
| 938    | No file  | `fe79e8d2483d`  |
| 927    | No file  | `fe79e8d2483d`  |
| 911    | No file  | `fe79e8d2483d`  |
| 904    | No file  | `fe79e8d2483d`  |
| 899    | No file  | `fe79e8d2483d`  |
| 894    | No file  | `fe79e8d2483d`  |
| 885    | No file  | `fe79e8d2483d`  |
| 879    | No file  | `fe79e8d2483d`  |
| 872    | No file  | `fe79e8d2483d`  |
| 864    | No file  | `fe79e8d2483d`  |
| 855    | No file  | `fe79e8d2483d`  |
| 853    | No file  | `fe79e8d2483d`  |
| 845    | No file  | `fe79e8d2483d`  |
| 837    | No file  | `fe79e8d2483d`  |
| 829    | No file  | `fe79e8d2483d`  |
| 822    | No file  | `fe79e8d2483d`  |
| 814    | No file  | `fe79e8d2483d`  |
| 805    | No file  | `fe79e8d2483d`  |
| 794    | No file  | `fe79e8d2483d`  |
| 787    | No file  | `fe79e8d2483d`  |
| 780    | No file  | `fe79e8d2483d`  |
| 771    | No file  | `fe79e8d2483d`  |
| 760    | No file  | `fe79e8d2483d`  |
| 748    | No file  | `fe79e8d2483d`  |
| 741    | No file  | `fe79e8d2483d`  |
| 736    | No file  | `fe79e8d2483d`  |
| 731    | No file  | `fe79e8d2483d`  |
| 723    | No file  | `fe79e8d2483d`  |
| 711    | No file  | `fe79e8d2483d`  |
| 707    | No file  | `fe79e8d2483d`  |
| 697    | No file  | `fe79e8d2483d`  |
| 689    | No file  | `fe79e8d2483d`  |
| 683    | No file  | `fe79e8d2483d`  |
| 678    | No file  | `fe79e8d2483d`  |
| 670    | No file  | `fe79e8d2483d`  |
| 661    | No file  | `fe79e8d2483d`  |
| 656    | No file  | `fe79e8d2483d`  |
| 652    | No file  | `fe79e8d2483d`  |
| 643    | No file  | `fe79e8d2483d`  |
| 637    | No file  | `fe79e8d2483d`  |
| 630    | No file  | `fe79e8d2483d`  |
| 627    | No file  | `fe79e8d2483d`  |
| 621    | No file  | `fe79e8d2483d`  |
| 617    | No file  | `fe79e8d2483d`  |
| 615    | No file  | `fe79e8d2483d`  |
| 606    | No file  | `fe79e8d2483d`  |
| 599    | No file  | `fe79e8d2483d`  |
| 592    | No file  | `fe79e8d2483d`  |
| 586    | No file  | `fe79e8d2483d`  |
| 577    | No file  | `fe79e8d2483d`  |
| 569    | No file  | `fe79e8d2483d`  |
| 561    | No file  | `fe79e8d2483d`  |
| 554    | No file  | `fe79e8d2483d`  |
| 542    | No file  | `fe79e8d2483d`  |
| 532    | No file  | `fe79e8d2483d`  |
| 531    | No file  | `fe79e8d2483d`  |
| 526    | No file  | `fe79e8d2483d`  |
| 521    | No file  | `fe79e8d2483d`  |
| 517    | No file  | `fe79e8d2483d`  |
| 510    | No file  | `fe79e8d2483d`  |
| 508    | No file  | `fe79e8d2483d`  |
| 504    | No file  | `fe79e8d2483d`  |
| 497    | No file  | `fe79e8d2483d`  |
| 491    | No file  | `fe79e8d2483d`  |
| 485    | No file  | `fe79e8d2483d`  |
| 478    | No file  | `fe79e8d2483d`  |
| 472    | No file  | `fe79e8d2483d`  |
| 466    | No file  | `fe79e8d2483d`  |
| 457    | No file  | `fe79e8d2483d`  |
| 452    | No file  | `fe79e8d2483d`  |
| 449    | No file  | `fe79e8d2483d`  |
| 435    | No file  | `fe79e8d2483d`  |

<!-- versions:end -->

## Companion Files

The file is self-contained. The handler reads names through the shared LOC
lookup and the skill icons through the skill icon index:

| File                  | Required | Role                                                                  |
| --------------------- | -------- | --------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Skill names (LOC type `10`, `str_id1` = skill number) and class names (LOC type `21`) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset                | Type               | Field          | Notes                                                    |
| --------------------- | ------------------ | -------------- | -------------------------------------------------------- |
| `+0x00`               | char[4]            | magic          | ASCII `PABR`                                             |
| `+0x04`               | u32                | active_count   | Number of active skills; `10044` on client 3482          |
| `+0x08`               | Row[active_count]  | active_skills  | See Row; every key's `kind` is `1`                       |
| `active_skills+0x00`  | u32                | passive_count  | Number of passive skills; `5250` on client 3482          |
| `active_skills+0x04`  | Row[passive_count] | passive_skills | See Row; every key's `kind` is `2`                       |
| `passive_skills+0x00` | String Table       | string_table   | Empty: `string_count` is `0`                             |
| `string_table+0x00`   | u32                | table_start    | Offset of the string table, where `passive_skills` ends  |
| `string_table+0x04`   | u32                | zero           | Always `0`                                               |

### Row (12 bytes)

| Offset  | Type | Field      | Notes                                                              |
| ------- | ---- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | skill_key  | `skill_no << 16 \| level`; level `1` on every row                  |
| `+0x04` | u64  | class_mask | Bit `n` set: class type `n` (LOC type `21`) can learn the skill; see [`class_mask`](#class_mask) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                        |
| ------- | ------------------ | ------------ | ---------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | No field reads a string      |

## Layout 1

The File Layout and String Table of Layout 2, with a 36-byte Row: the
class set is one byte per class type, the 2016 `gc::ClassTypeFlag` (32
bytes), where Layout 2 has one bit per class type.

### Row (36 bytes)

| Offset  | Type   | Field      | Notes                                                                 |
| ------- | ------ | ---------- | --------------------------------------------------------------------- |
| `+0x00` | u32    | skill_key  | `skill_no << 16 \| level`; level `1` on every row                     |
| `+0x04` | u8[32] | class_mask | Byte `n` is `1` when class type `n` can learn the skill, else `0`     |

On client 1194 the lists hold 4,865 active and 2,516 passive skills.

Client 1267 holds all 8,413 keys of client 1261, 8,411 of them in the same
list, and on every one bits `0` to `31` of the Layout 2 `class_mask` are the
class bytes of client 1261. The 1,519 rows of client 1261 with all 32 bytes
set store `0xFFFFFFFFFFFFFFFF` on client 1267.

## `class_mask`

On every row of client 3482 the mask equals the `class_mask` of the same
key in [`skillsimply.dbss`](../dbss/skillsimply_dbss.md#class_mask), 15,294 of
15,294 rows:

| Mask             | Active (client 3482) | Passive (client 3482) | Meaning                       |
| ---------------- | -------------------- | --------------------- | ----------------------------- |
| one bit          | 6,328                | 825                   | One class                     |
| two to eight bits | 572                 | 112                   | Classes that share the skill  |
| `0x7FFFFFFFFFFF` | 610                  | 2,557                 | Every class                   |
| `0`              | 2,534                | 1,756                 | No class                      |

On clients 1267 to 2243 the mask is a 32-bit mask with bit `31` copied into
the high half: every row with bit `31` set has a high half of `0xFFFFFFFF`
and every other row a high half of `0`, so every-class rows store
`0xFFFFFFFFFFFFFFFF`. The parser keeps the low half of such a file and reads
it with 32 class slots, like Layout 1. Clients 2243 and 2250 hold the same
12,765 keys; on client 2250 the 2,333 rows that store all 64 bits on 2243
store `0x1FFFFFFFFF` (class types `0` to `36`), and 267 rows have bit `31`
set with a high half of `0`.

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 has a
publicskill or privateskill name, and no client Lua on client 3482 names
either file; the `binary/` folder of that private server holds both files
in the same layouts. The names come from the matching `skill.dbss` and
`skillsimply.dbss` fields on client 3482:

| Field          | Source                                                                              |
| -------------- | ----------------------------------------------------------------------------------- |
| skill_key      | The `skill_no << 16 \| level` key of every skill table; 15,294 of 15,294 keys are `skill.dbss` keys |
| class_mask     | Equal to `skillsimply.dbss` `class_mask` on 15,294 of 15,294 rows; the 2016 `gc::SkillTypeStaticStatus` member `_usableClassType` is a `gc::ClassTypeFlag` of 32 bytes, the Layout 1 field |
| active_skills  | Every key's `skillsimply.dbss` `kind` is `1`, the 2016 enum value `eActiveSkillType` |
| passive_skills | Every key's `kind` is `2`, `ePassiveSkillType`                                       |

## Notes

- Within each list the skill keys are unique and in no key order; no key is
  in both lists or in `publicskill.bss`.
- On client 3482 the active list holds all 909 skills of
  `skillawakeningability2.bss` and all 517 skill numbers of
  `classskilllist.bss`; the passive list holds none of either.
- The handler shows one row per key, the active list first: the skill
  number linked to its `skill.dbss` row, the skill icon and LOC type `10`
  name, Active or Passive, and the LOC type `21` names of the classes in
  `class_mask` (All for every class, and for a row with all 32 class slots
  set in a Layout 1 file or a Layout 2 file of clients 1267 to 2243).
- Nothing in the file names its layout. The parser reads it with Layout 2,
  then Layout 1, and keeps the first whose rows end where the string table
  starts.
- The 2016 exe binds `isPrivateSkill` on `SkillTypeStaticStatusWrapper` for
  the Lua; no `.luac` on client 3482 calls it.
