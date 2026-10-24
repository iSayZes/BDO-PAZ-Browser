# `instancedungeonskillinfo.bss` Format

## Purpose

Skills of an instance dungeon mode, per class type: each class row holds
20 lists of skill keys, and a table after the rows gives some of those
skills a short list of byte values. Client 1784 fills 10 class rows
(class types 16 to 25) with 255 skills; client 3482 ships every list
empty and the table with no entries.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records                        | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ------ | ------------------------------ | --------- |
| 3      | 3381 and later | 3483    | `instancedungeonskillinfo.bss` | 15,540 | 1,940 Skill List, 97 Class Row | 8         |
| 2      | 2250 to 3373   | 3373    | `instancedungeonskillinfo.bss` | 13,940 | 1,740 Skill List, 87 Class Row | 8         |
| 1      | 1598 to 2243   | 2243    | `instancedungeonskillinfo.bss` | 13,140 | 1,640 Skill List, 82 Class Row | 8         |

| Layout | File                           | Known             | Unknown    |
| ------ | ------------------------------ | ----------------- | ---------- |
| 3      | `instancedungeonskillinfo.bss` | 15,540 B (100.0%) | 0 B (0.0%) |
| 2      | `instancedungeonskillinfo.bss` | 13,940 B (100.0%) | 0 B (0.0%) |
| 1      | `instancedungeonskillinfo.bss` | 13,140 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 3             | `39f33bf8d6e2`  |
| 3482   | Layout 3             | `39f33bf8d6e2`  |
| 3474   | Layout 3             | `39f33bf8d6e2`  |
| 3473   | Layout 3             | `39f33bf8d6e2`  |
| 3464   | Layout 3             | `39f33bf8d6e2`  |
| 3458   | Layout 3             | `39f33bf8d6e2`  |
| 3454   | Layout 3             | `39f33bf8d6e2`  |
| 3444   | Layout 3             | `39f33bf8d6e2`  |
| 3435   | Layout 3             | `39f33bf8d6e2`  |
| 3426   | Layout 3             | `39f33bf8d6e2`  |
| 3418   | Layout 3             | `39f33bf8d6e2`  |
| 3412   | Layout 3             | `39f33bf8d6e2`  |
| 3402   | Layout 3             | `39f33bf8d6e2`  |
| 3396   | Layout 3             | `39f33bf8d6e2`  |
| 3387   | Layout 3             | `39f33bf8d6e2`  |
| 3381   | Layout 3             | `39f33bf8d6e2`  |
| 3373   | Layout 2             | `39f33bf8d6e2`  |
| 3364   | Layout 2             | `39f33bf8d6e2`  |
| 3356   | Layout 2             | `39f33bf8d6e2`  |
| 3349   | Layout 2             | `39f33bf8d6e2`  |
| 3342   | Layout 2             | `39f33bf8d6e2`  |
| 3335   | Layout 2             | `39f33bf8d6e2`  |
| 3326   | Layout 2             | `39f33bf8d6e2`  |
| 3321   | Layout 2             | `39f33bf8d6e2`  |
| 3314   | Layout 2             | `39f33bf8d6e2`  |
| 3303   | Layout 2             | `39f33bf8d6e2`  |
| 3302   | Layout 2             | `39f33bf8d6e2`  |
| 3293   | Layout 2             | `39f33bf8d6e2`  |
| 3283   | Layout 2             | `39f33bf8d6e2`  |
| 3275   | Layout 2             | `39f33bf8d6e2`  |
| 3267   | Layout 2             | `39f33bf8d6e2`  |
| 3258   | Layout 2             | `39f33bf8d6e2`  |
| 3251   | Layout 2             | `39f33bf8d6e2`  |
| 3242   | Layout 2             | `39f33bf8d6e2`  |
| 3235   | Layout 2             | `39f33bf8d6e2`  |
| 3229   | Layout 2             | `39f33bf8d6e2`  |
| 3212   | Layout 2             | `39f33bf8d6e2`  |
| 3203   | Layout 2             | `39f33bf8d6e2`  |
| 3193   | Layout 2             | `39f33bf8d6e2`  |
| 3186   | Layout 2             | `39f33bf8d6e2`  |
| 3177   | Layout 2             | `39f33bf8d6e2`  |
| 3169   | Layout 2             | `39f33bf8d6e2`  |
| 3158   | Layout 2             | `39f33bf8d6e2`  |
| 3151   | Layout 2             | `39f33bf8d6e2`  |
| 3144   | Layout 2             | `39f33bf8d6e2`  |
| 3133   | Layout 2             | `39f33bf8d6e2`  |
| 3125   | Layout 2             | `39f33bf8d6e2`  |
| 3118   | Layout 2             | `39f33bf8d6e2`  |
| 3111   | Layout 2             | `39f33bf8d6e2`  |
| 3103   | Layout 2             | `39f33bf8d6e2`  |
| 3095   | Layout 2             | `39f33bf8d6e2`  |
| 3086   | Layout 2             | `39f33bf8d6e2`  |
| 3072   | Layout 2             | `39f33bf8d6e2`  |
| 3062   | Layout 2             | `39f33bf8d6e2`  |
| 3052   | Layout 2             | `39f33bf8d6e2`  |
| 3045   | Layout 2             | `39f33bf8d6e2`  |
| 3037   | Layout 2             | `39f33bf8d6e2`  |
| 3030   | Layout 2             | `39f33bf8d6e2`  |
| 3021   | Layout 2             | `39f33bf8d6e2`  |
| 3012   | Layout 2             | `39f33bf8d6e2`  |
| 3002   | Layout 2             | `39f33bf8d6e2`  |
| 2995   | Layout 2             | `39f33bf8d6e2`  |
| 2987   | Layout 2             | `39f33bf8d6e2`  |
| 2978   | Layout 2             | `39f33bf8d6e2`  |
| 2970   | Layout 2             | `39f33bf8d6e2`  |
| 2959   | Layout 2             | `39f33bf8d6e2`  |
| 2951   | Layout 2             | `39f33bf8d6e2`  |
| 2942   | Layout 2             | `39f33bf8d6e2`  |
| 2935   | Layout 2             | `39f33bf8d6e2`  |
| 2932   | Layout 2             | `39f33bf8d6e2`  |
| 2923   | Layout 2             | `39f33bf8d6e2`  |
| 2919   | Layout 2             | `39f33bf8d6e2`  |
| 2907   | Layout 2             | `39f33bf8d6e2`  |
| 2900   | Layout 2             | `39f33bf8d6e2`  |
| 2891   | Layout 2             | `39f33bf8d6e2`  |
| 2882   | Layout 2             | `39f33bf8d6e2`  |
| 2872   | Layout 2             | `39f33bf8d6e2`  |
| 2863   | Layout 2             | `39f33bf8d6e2`  |
| 2855   | Layout 2             | `39f33bf8d6e2`  |
| 2849   | Layout 2             | `39f33bf8d6e2`  |
| 2844   | Layout 2             | `39f33bf8d6e2`  |
| 2834   | Layout 2             | `39f33bf8d6e2`  |
| 2825   | Layout 2             | `39f33bf8d6e2`  |
| 2819   | Layout 2             | `39f33bf8d6e2`  |
| 2811   | Layout 2             | `39f33bf8d6e2`  |
| 2803   | Layout 2             | `39f33bf8d6e2`  |
| 2794   | Layout 2             | `39f33bf8d6e2`  |
| 2783   | Layout 2             | `39f33bf8d6e2`  |
| 2774   | Layout 2             | `39f33bf8d6e2`  |
| 2765   | Layout 2             | `39f33bf8d6e2`  |
| 2756   | Layout 2             | `39f33bf8d6e2`  |
| 2750   | Layout 2             | `39f33bf8d6e2`  |
| 2743   | Layout 2             | `39f33bf8d6e2`  |
| 2736   | Layout 2             | `39f33bf8d6e2`  |
| 2726   | Layout 2             | `39f33bf8d6e2`  |
| 2717   | Layout 2             | `39f33bf8d6e2`  |
| 2709   | Layout 2             | `39f33bf8d6e2`  |
| 2703   | Layout 2             | `39f33bf8d6e2`  |
| 2695   | Layout 2             | `39f33bf8d6e2`  |
| 2684   | Layout 2             | `39f33bf8d6e2`  |
| 2672   | Layout 2             | `39f33bf8d6e2`  |
| 2665   | Layout 2             | `39f33bf8d6e2`  |
| 2657   | Layout 2             | `39f33bf8d6e2`  |
| 2649   | Layout 2             | `39f33bf8d6e2`  |
| 2644   | Layout 2             | `39f33bf8d6e2`  |
| 2637   | Layout 2             | `39f33bf8d6e2`  |
| 2629   | Layout 2             | `39f33bf8d6e2`  |
| 2619   | Layout 2             | `39f33bf8d6e2`  |
| 2612   | Layout 2             | `39f33bf8d6e2`  |
| 2606   | Layout 2             | `39f33bf8d6e2`  |
| 2602   | Layout 2             | `39f33bf8d6e2`  |
| 2601   | Layout 2             | `39f33bf8d6e2`  |
| 2592   | Layout 2             | `39f33bf8d6e2`  |
| 2583   | Layout 2             | `39f33bf8d6e2`  |
| 2575   | Layout 2             | `39f33bf8d6e2`  |
| 2567   | Layout 2             | `39f33bf8d6e2`  |
| 2560   | Layout 2             | `39f33bf8d6e2`  |
| 2553   | Layout 2             | `39f33bf8d6e2`  |
| 2545   | Layout 2             | `39f33bf8d6e2`  |
| 2538   | Layout 2             | `39f33bf8d6e2`  |
| 2529   | Layout 2             | `39f33bf8d6e2`  |
| 2519   | Layout 2             | `39f33bf8d6e2`  |
| 2513   | Layout 2             | `39f33bf8d6e2`  |
| 2510   | Layout 2             | `39f33bf8d6e2`  |
| 2507   | Layout 2             | `39f33bf8d6e2`  |
| 2503   | Layout 2             | `39f33bf8d6e2`  |
| 2498   | Layout 2             | `39f33bf8d6e2`  |
| 2492   | Layout 2             | `39f33bf8d6e2`  |
| 2487   | Layout 2             | `39f33bf8d6e2`  |
| 2480   | Layout 2             | `39f33bf8d6e2`  |
| 2474   | Layout 2             | `39f33bf8d6e2`  |
| 2468   | Layout 2             | `39f33bf8d6e2`  |
| 2460   | Layout 2             | `39f33bf8d6e2`  |
| 2453   | Layout 2             | `39f33bf8d6e2`  |
| 2444   | Layout 2             | `39f33bf8d6e2`  |
| 2438   | Layout 2             | `39f33bf8d6e2`  |
| 2434   | Layout 2             | `39f33bf8d6e2`  |
| 2429   | Layout 2             | `39f33bf8d6e2`  |
| 2421   | Layout 2             | `39f33bf8d6e2`  |
| 2414   | Layout 2             | `39f33bf8d6e2`  |
| 2407   | Layout 2             | `39f33bf8d6e2`  |
| 2401   | Layout 2             | `39f33bf8d6e2`  |
| 2397   | Layout 2             | `39f33bf8d6e2`  |
| 2393   | Layout 2             | `39f33bf8d6e2`  |
| 2384   | Layout 2             | `39f33bf8d6e2`  |
| 2378   | Layout 2             | `39f33bf8d6e2`  |
| 2372   | Layout 2             | `39f33bf8d6e2`  |
| 2358   | Layout 2             | `39f33bf8d6e2`  |
| 2352   | Layout 2             | `39f33bf8d6e2`  |
| 2347   | Layout 2             | `39f33bf8d6e2`  |
| 2343   | Layout 2             | `39f33bf8d6e2`  |
| 2335   | Layout 2             | `39f33bf8d6e2`  |
| 2327   | Layout 2             | `39f33bf8d6e2`  |
| 2324   | Layout 2             | `39f33bf8d6e2`  |
| 2319   | Layout 2             | `39f33bf8d6e2`  |
| 2313   | Layout 2             | `39f33bf8d6e2`  |
| 2308   | Layout 2             | `39f33bf8d6e2`  |
| 2302   | Layout 2             | `39f33bf8d6e2`  |
| 2295   | Layout 2             | `39f33bf8d6e2`  |
| 2290   | Layout 2             | `39f33bf8d6e2`  |
| 2284   | Layout 2             | `39f33bf8d6e2`  |
| 2276   | Layout 2             | `39f33bf8d6e2`  |
| 2269   | Layout 2             | `39f33bf8d6e2`  |
| 2259   | Layout 2             | `39f33bf8d6e2`  |
| 2250   | Layout 2             | `39f33bf8d6e2`  |
| 2243   | Layout 1             | `39f33bf8d6e2`  |
| 2235   | Layout 1             | `39f33bf8d6e2`  |
| 2229   | Layout 1             | `39f33bf8d6e2`  |
| 2224   | Layout 1             | `39f33bf8d6e2`  |
| 2218   | Layout 1             | `39f33bf8d6e2`  |
| 2215   | Layout 1             | `39f33bf8d6e2`  |
| 2207   | Layout 1             | `39f33bf8d6e2`  |
| 2203   | Layout 1             | `39f33bf8d6e2`  |
| 2196   | Layout 1             | `39f33bf8d6e2`  |
| 2192   | Layout 1             | `39f33bf8d6e2`  |
| 2189   | Layout 1             | `39f33bf8d6e2`  |
| 2183   | Layout 1             | `39f33bf8d6e2`  |
| 2179   | Layout 1             | `39f33bf8d6e2`  |
| 2171   | Layout 1             | `39f33bf8d6e2`  |
| 2163   | Layout 1             | `39f33bf8d6e2`  |
| 2156   | Layout 1             | `39f33bf8d6e2`  |
| 2151   | Layout 1             | `39f33bf8d6e2`  |
| 2147   | Layout 1             | `39f33bf8d6e2`  |
| 2142   | Layout 1             | `39f33bf8d6e2`  |
| 2138   | Layout 1             | `39f33bf8d6e2`  |
| 2134   | Layout 1             | `39f33bf8d6e2`  |
| 2130   | Layout 1             | `39f33bf8d6e2`  |
| 2122   | Layout 1             | `39f33bf8d6e2`  |
| 2107   | Layout 1             | `39f33bf8d6e2`  |
| 2098   | Layout 1             | `39f33bf8d6e2`  |
| 2089   | Layout 1             | `39f33bf8d6e2`  |
| 2081   | Layout 1             | `39f33bf8d6e2`  |
| 2073   | Layout 1             | `39f33bf8d6e2`  |
| 2067   | Layout 1             | `39f33bf8d6e2`  |
| 2063   | Layout 1             | `39f33bf8d6e2`  |
| 2059   | Layout 1             | `39f33bf8d6e2`  |
| 2052   | Layout 1             | `39f33bf8d6e2`  |
| 2044   | Layout 1             | `39f33bf8d6e2`  |
| 2039   | Layout 1             | `39f33bf8d6e2`  |
| 2032   | Layout 1             | `39f33bf8d6e2`  |
| 2025   | Layout 1             | `39f33bf8d6e2`  |
| 2011   | Layout 1             | `39f33bf8d6e2`  |
| 2005   | Layout 1             | `39f33bf8d6e2`  |
| 2000   | Layout 1             | `39f33bf8d6e2`  |
| 1996   | Layout 1             | `39f33bf8d6e2`  |
| 1991   | Layout 1             | `39f33bf8d6e2`  |
| 1985   | Layout 1             | `39f33bf8d6e2`  |
| 1980   | Layout 1             | `39f33bf8d6e2`  |
| 1969   | Layout 1             | `39f33bf8d6e2`  |
| 1964   | Layout 1             | `39f33bf8d6e2`  |
| 1958   | Layout 1             | `39f33bf8d6e2`  |
| 1950   | Layout 1             | `39f33bf8d6e2`  |
| 1945   | Layout 1             | `39f33bf8d6e2`  |
| 1937   | Layout 1             | `39f33bf8d6e2`  |
| 1933   | Layout 1             | `39f33bf8d6e2`  |
| 1927   | Layout 1             | `39f33bf8d6e2`  |
| 1921   | Layout 1             | `39f33bf8d6e2`  |
| 1914   | Layout 1             | `39f33bf8d6e2`  |
| 1908   | Layout 1             | `39f33bf8d6e2`  |
| 1897   | Layout 1             | `39f33bf8d6e2`  |
| 1892   | Layout 1             | `39f33bf8d6e2`  |
| 1886   | Layout 1             | `39f33bf8d6e2`  |
| 1881   | Layout 1             | `39f33bf8d6e2`  |
| 1871   | Layout 1             | `39f33bf8d6e2`  |
| 1866   | Layout 1             | `39f33bf8d6e2`  |
| 1862   | Layout 1             | `39f33bf8d6e2`  |
| 1854   | Layout 1             | `39f33bf8d6e2`  |
| 1846   | Layout 1             | `39f33bf8d6e2`  |
| 1838   | Layout 1             | `39f33bf8d6e2`  |
| 1832   | Layout 1             | `39f33bf8d6e2`  |
| 1826   | Layout 1             | `39f33bf8d6e2`  |
| 1822   | Layout 1             | `39f33bf8d6e2`  |
| 1818   | Layout 1             | `39f33bf8d6e2`  |
| 1804   | Layout 1             | `39f33bf8d6e2`  |
| 1794   | Layout 1             | `39f33bf8d6e2`  |
| 1790   | Layout 1             | `39f33bf8d6e2`  |
| 1784   | Layout 1             | `39f33bf8d6e2`  |
| 1774   | Layout 1             | `39f33bf8d6e2`  |
| 1771   | Layout 1             | `39f33bf8d6e2`  |
| 1762   | Layout 1             | `39f33bf8d6e2`  |
| 1759   | Layout 1             | `39f33bf8d6e2`  |
| 1754   | Layout 1             | `39f33bf8d6e2`  |
| 1749   | Layout 1             | `39f33bf8d6e2`  |
| 1743   | Layout 1             | `39f33bf8d6e2`  |
| 1737   | Layout 1             | `39f33bf8d6e2`  |
| 1731   | Layout 1             | `39f33bf8d6e2`  |
| 1725   | Layout 1             | `39f33bf8d6e2`  |
| 1717   | Layout 1             | `39f33bf8d6e2`  |
| 1710   | Layout 1             | `39f33bf8d6e2`  |
| 1704   | Layout 1             | `39f33bf8d6e2`  |
| 1698   | Layout 1             | `39f33bf8d6e2`  |
| 1690   | Layout 1             | `39f33bf8d6e2`  |
| 1685   | Layout 1             | `39f33bf8d6e2`  |
| 1680   | Layout 1             | `39f33bf8d6e2`  |
| 1674   | Layout 1             | `39f33bf8d6e2`  |
| 1668   | Layout 1             | `39f33bf8d6e2`  |
| 1659   | Layout 1             | `39f33bf8d6e2`  |
| 1649   | Layout 1             | `39f33bf8d6e2`  |
| 1642   | Layout 1             | `39f33bf8d6e2`  |
| 1636   | Layout 1             | `39f33bf8d6e2`  |
| 1628   | Layout 1             | `39f33bf8d6e2`  |
| 1622   | Layout 1             | `39f33bf8d6e2`  |
| 1614   | Layout 1             | `39f33bf8d6e2`  |
| 1608   | Layout 1             | `39f33bf8d6e2`  |
| 1602   | Layout 1             | `39f33bf8d6e2`  |
| 1598   | Layout 1             | `39f33bf8d6e2`  |
| 1594   | No documented layout | `39f33bf8d6e2`  |
| 1590   | No documented layout | `39f33bf8d6e2`  |
| 1587   | No documented layout | `39f33bf8d6e2`  |
| 1584   | No documented layout | `39f33bf8d6e2`  |
| 1579   | No documented layout | `39f33bf8d6e2`  |
| 1572   | No documented layout | `39f33bf8d6e2`  |
| 1565   | No documented layout | `39f33bf8d6e2`  |
| 1559   | No documented layout | `39f33bf8d6e2`  |
| 1554   | No documented layout | `39f33bf8d6e2`  |
| 1547   | No documented layout | `39f33bf8d6e2`  |
| 1537   | No documented layout | `39f33bf8d6e2`  |
| 1529   | No documented layout | `39f33bf8d6e2`  |
| 1524   | No documented layout | `39f33bf8d6e2`  |
| 1519   | No documented layout | `39f33bf8d6e2`  |
| 1509   | No documented layout | `39f33bf8d6e2`  |
| 1506   | No documented layout | `39f33bf8d6e2`  |
| 1504   | No documented layout | `39f33bf8d6e2`  |
| 1500   | No documented layout | `39f33bf8d6e2`  |
| 1493   | No documented layout | `39f33bf8d6e2`  |
| 1489   | No documented layout | `39f33bf8d6e2`  |
| 1485   | No documented layout | `39f33bf8d6e2`  |
| 1481   | No documented layout | `39f33bf8d6e2`  |
| 1474   | No documented layout | `39f33bf8d6e2`  |
| 1466   | No documented layout | `39f33bf8d6e2`  |
| 1462   | No documented layout | `39f33bf8d6e2`  |
| 1459   | No documented layout | `39f33bf8d6e2`  |
| 1453   | No documented layout | `39f33bf8d6e2`  |
| 1450   | No documented layout | `39f33bf8d6e2`  |
| 1445   | No documented layout | `39f33bf8d6e2`  |
| 1439   | No documented layout | `39f33bf8d6e2`  |
| 1433   | No documented layout | `39f33bf8d6e2`  |
| 1430   | No documented layout | `39f33bf8d6e2`  |
| 1426   | No documented layout | `39f33bf8d6e2`  |
| 1421   | No documented layout | `39f33bf8d6e2`  |
| 1417   | No documented layout | `39f33bf8d6e2`  |
| 1416   | No documented layout | `39f33bf8d6e2`  |
| 1409   | No documented layout | `39f33bf8d6e2`  |
| 1405   | No documented layout | `39f33bf8d6e2`  |
| 1401   | No documented layout | `39f33bf8d6e2`  |
| 1396   | No documented layout | `39f33bf8d6e2`  |
| 1391   | No documented layout | `39f33bf8d6e2`  |
| 1390   | No documented layout | `39f33bf8d6e2`  |
| 1386   | No documented layout | `39f33bf8d6e2`  |
| 1381   | No documented layout | `39f33bf8d6e2`  |
| 1379   | No documented layout | `39f33bf8d6e2`  |
| 1372   | No documented layout | `39f33bf8d6e2`  |
| 1366   | No documented layout | `39f33bf8d6e2`  |
| 1364   | No documented layout | `39f33bf8d6e2`  |
| 1363   | No documented layout | `39f33bf8d6e2`  |
| 1360   | No documented layout | `39f33bf8d6e2`  |
| 1358   | No documented layout | `39f33bf8d6e2`  |
| 1355   | No documented layout | `39f33bf8d6e2`  |
| 1351   | No documented layout | `39f33bf8d6e2`  |
| 1348   | No documented layout | `39f33bf8d6e2`  |
| 1346   | No documented layout | `39f33bf8d6e2`  |
| 1341   | No documented layout | `39f33bf8d6e2`  |
| 1340   | No documented layout | `39f33bf8d6e2`  |
| 1338   | No documented layout | `39f33bf8d6e2`  |
| 1335   | No documented layout | `39f33bf8d6e2`  |
| 1333   | No documented layout | `39f33bf8d6e2`  |
| 1329   | No documented layout | `39f33bf8d6e2`  |
| 1327   | No documented layout | `39f33bf8d6e2`  |
| 1324   | No documented layout | `39f33bf8d6e2`  |
| 1321   | No documented layout | `39f33bf8d6e2`  |
| 1319   | No documented layout | `39f33bf8d6e2`  |
| 1318   | No documented layout | `39f33bf8d6e2`  |
| 1316   | No documented layout | `39f33bf8d6e2`  |
| 1313   | No documented layout | `39f33bf8d6e2`  |
| 1311   | No documented layout | `39f33bf8d6e2`  |
| 1309   | No documented layout | `39f33bf8d6e2`  |
| 1304   | No documented layout | `39f33bf8d6e2`  |
| 1292   | No documented layout | `39f33bf8d6e2`  |
| 1286   | No documented layout | `39f33bf8d6e2`  |
| 1280   | No documented layout | `39f33bf8d6e2`  |
| 1276   | No documented layout | `39f33bf8d6e2`  |
| 1267   | No documented layout | `39f33bf8d6e2`  |
| 1261   | No documented layout | `39f33bf8d6e2`  |
| 1256   | No documented layout | `39f33bf8d6e2`  |
| 1250   | No documented layout | `39f33bf8d6e2`  |
| 1246   | No documented layout | `39f33bf8d6e2`  |
| 1239   | No documented layout | `39f33bf8d6e2`  |
| 1230   | No documented layout | `39f33bf8d6e2`  |
| 1226   | No documented layout | `39f33bf8d6e2`  |
| 1220   | No documented layout | `39f33bf8d6e2`  |
| 1217   | No documented layout | `39f33bf8d6e2`  |
| 1211   | No documented layout | `39f33bf8d6e2`  |
| 1210   | No documented layout | `39f33bf8d6e2`  |
| 1208   | No documented layout | `39f33bf8d6e2`  |
| 1203   | No documented layout | `39f33bf8d6e2`  |
| 1197   | No documented layout | `39f33bf8d6e2`  |
| 1194   | No documented layout | `39f33bf8d6e2`  |
| 1192   | No documented layout | `39f33bf8d6e2`  |
| 1187   | No documented layout | `39f33bf8d6e2`  |
| 1183   | No documented layout | `39f33bf8d6e2`  |
| 1177   | No documented layout | `39f33bf8d6e2`  |
| 1173   | No documented layout | `39f33bf8d6e2`  |
| 1167   | No documented layout | `39f33bf8d6e2`  |
| 1164   | No documented layout | `39f33bf8d6e2`  |
| 1156   | No documented layout | `39f33bf8d6e2`  |
| 1149   | No documented layout | `39f33bf8d6e2`  |
| 1144   | No documented layout | `39f33bf8d6e2`  |
| 1137   | No documented layout | `39f33bf8d6e2`  |
| 1132   | No documented layout | `39f33bf8d6e2`  |
| 1127   | No documented layout | `39f33bf8d6e2`  |
| 1122   | No documented layout | `39f33bf8d6e2`  |
| 1118   | No documented layout | `39f33bf8d6e2`  |
| 1114   | No documented layout | `39f33bf8d6e2`  |
| 1109   | No documented layout | `39f33bf8d6e2`  |
| 1102   | No file              | `39f33bf8d6e2`  |
| 1096   | No file              | `39f33bf8d6e2`  |
| 1088   | No file              | `39f33bf8d6e2`  |
| 1081   | No file              | `39f33bf8d6e2`  |
| 1076   | No file              | `39f33bf8d6e2`  |
| 1069   | No file              | `39f33bf8d6e2`  |
| 1064   | No file              | `39f33bf8d6e2`  |
| 1058   | No file              | `39f33bf8d6e2`  |
| 1051   | No file              | `39f33bf8d6e2`  |
| 1044   | No file              | `39f33bf8d6e2`  |
| 1036   | No file              | `39f33bf8d6e2`  |
| 1026   | No file              | `39f33bf8d6e2`  |
| 1016   | No file              | `39f33bf8d6e2`  |
| 1009   | No file              | `39f33bf8d6e2`  |
| 1005   | No file              | `39f33bf8d6e2`  |
| 1000   | No file              | `39f33bf8d6e2`  |
| 998    | No file              | `39f33bf8d6e2`  |
| 990    | No file              | `39f33bf8d6e2`  |
| 979    | No file              | `39f33bf8d6e2`  |
| 972    | No file              | `39f33bf8d6e2`  |
| 963    | No file              | `39f33bf8d6e2`  |
| 955    | No file              | `39f33bf8d6e2`  |
| 946    | No file              | `39f33bf8d6e2`  |
| 938    | No file              | `39f33bf8d6e2`  |
| 927    | No file              | `39f33bf8d6e2`  |
| 911    | No file              | `39f33bf8d6e2`  |
| 904    | No file              | `39f33bf8d6e2`  |
| 899    | No file              | `39f33bf8d6e2`  |
| 894    | No file              | `39f33bf8d6e2`  |
| 885    | No file              | `39f33bf8d6e2`  |
| 879    | No file              | `39f33bf8d6e2`  |
| 872    | No file              | `39f33bf8d6e2`  |
| 864    | No file              | `39f33bf8d6e2`  |
| 855    | No file              | `39f33bf8d6e2`  |
| 853    | No file              | `39f33bf8d6e2`  |
| 845    | No file              | `39f33bf8d6e2`  |
| 837    | No file              | `39f33bf8d6e2`  |
| 829    | No file              | `39f33bf8d6e2`  |
| 822    | No file              | `39f33bf8d6e2`  |
| 814    | No file              | `39f33bf8d6e2`  |
| 805    | No file              | `39f33bf8d6e2`  |
| 794    | No file              | `39f33bf8d6e2`  |
| 787    | No file              | `39f33bf8d6e2`  |
| 780    | No file              | `39f33bf8d6e2`  |
| 771    | No file              | `39f33bf8d6e2`  |
| 760    | No file              | `39f33bf8d6e2`  |
| 748    | No file              | `39f33bf8d6e2`  |
| 741    | No file              | `39f33bf8d6e2`  |
| 736    | No file              | `39f33bf8d6e2`  |
| 731    | No file              | `39f33bf8d6e2`  |
| 723    | No file              | `39f33bf8d6e2`  |
| 711    | No file              | `39f33bf8d6e2`  |
| 707    | No file              | `39f33bf8d6e2`  |
| 697    | No file              | `39f33bf8d6e2`  |
| 689    | No file              | `39f33bf8d6e2`  |
| 683    | No file              | `39f33bf8d6e2`  |
| 678    | No file              | `39f33bf8d6e2`  |
| 670    | No file              | `39f33bf8d6e2`  |
| 661    | No file              | `39f33bf8d6e2`  |
| 656    | No file              | `39f33bf8d6e2`  |
| 652    | No file              | `39f33bf8d6e2`  |
| 643    | No file              | `39f33bf8d6e2`  |
| 637    | No file              | `39f33bf8d6e2`  |
| 630    | No file              | `39f33bf8d6e2`  |
| 627    | No file              | `39f33bf8d6e2`  |
| 621    | No file              | `39f33bf8d6e2`  |
| 617    | No file              | `39f33bf8d6e2`  |
| 615    | No file              | `39f33bf8d6e2`  |
| 606    | No file              | `39f33bf8d6e2`  |
| 599    | No file              | `39f33bf8d6e2`  |
| 592    | No file              | `39f33bf8d6e2`  |
| 586    | No file              | `39f33bf8d6e2`  |
| 577    | No file              | `39f33bf8d6e2`  |
| 569    | No file              | `39f33bf8d6e2`  |
| 561    | No file              | `39f33bf8d6e2`  |
| 554    | No file              | `39f33bf8d6e2`  |
| 542    | No file              | `39f33bf8d6e2`  |
| 532    | No file              | `39f33bf8d6e2`  |
| 531    | No file              | `39f33bf8d6e2`  |
| 526    | No file              | `39f33bf8d6e2`  |
| 521    | No file              | `39f33bf8d6e2`  |
| 517    | No file              | `39f33bf8d6e2`  |
| 510    | No file              | `39f33bf8d6e2`  |
| 508    | No file              | `39f33bf8d6e2`  |
| 504    | No file              | `39f33bf8d6e2`  |
| 497    | No file              | `39f33bf8d6e2`  |
| 491    | No file              | `39f33bf8d6e2`  |
| 485    | No file              | `39f33bf8d6e2`  |
| 478    | No file              | `39f33bf8d6e2`  |
| 472    | No file              | `39f33bf8d6e2`  |
| 466    | No file              | `39f33bf8d6e2`  |
| 457    | No file              | `39f33bf8d6e2`  |
| 452    | No file              | `39f33bf8d6e2`  |
| 449    | No file              | `39f33bf8d6e2`  |
| 435    | No file              | `39f33bf8d6e2`  |

<!-- versions:end -->

## Companion Files

None. Class names come from LOC type 21 and skill names from LOC type 10.
[`instancedungeonskillstatic.dbss`](instancedungeonskillstatic_dbss.md)
holds a Korean text for 157 of the 255 skills of client 1784.

All multi-byte values are little-endian.

## Layout 3

### File Layout

The file stores no class row count; see Open Questions.

| Offset               | Type                             | Field             | Notes                                           |
| -------------------- | -------------------------------- | ----------------- | ----------------------------------------------- |
| `+0x00`              | char[4]                          | magic             | `PABR`                                          |
| `+0x04`              | Class Row[97]                    | rows              | Row `n` is class type `n`; see Class Row        |
| `rows+0x00`          | u32                              | skill_entry_count | Number of `skill_entries`; `0` on client 3482   |
| `rows+0x04`          | Skill Entry[skill_entry_count]   | skill_entries     | See Skill Entry                                 |
| `skill_entries+0x00` | String Table                     | string_table      | See String Table                                |
| `string_table+0x00`  | u32                              | table_start       | Offset of the string table                      |
| `string_table+0x04`  | u32                              | zero              | Always `0`                                      |

### Class Row (variable: 0 bytes + lists)

| Offset  | Type            | Field       | Notes                                 |
| ------- | --------------- | ----------- | ------------------------------------- |
| `+0x00` | Skill List[20]  | skill_lists | Lists 0 to 19 in order; see Skill List |

### Skill List (variable: 8 bytes + keys)

| Offset  | Type                   | Field           | Notes                                                    |
| ------- | ---------------------- | --------------- | -------------------------------------------------------- |
| `+0x00` | u64                    | skill_key_count | Number of keys; `0` for an empty list                    |
| `+0x08` | u32[skill_key_count]   | skill_keys      | Skill keys `skill_no << 16 \| level`, level `1` on client 1784 |

### Skill Entry (variable: 8 bytes + values)

| Offset  | Type              | Field      | Notes                                                       |
| ------- | ----------------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u16               | skill_no   | A skill of the lists, LOC type `10`                         |
| `+0x02` | u16               | unknown_02 | `1` on every entry of client 1784                           |
| `+0x04` | u32               | unknown_04 | Number of `unknown_08` values; `1` or `2`                   |
| `+0x08` | u8[unknown_04]    | unknown_08 | `2` (127 entries) or `3` (38) on client 1784; one entry holds `1, 2` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482          |
| `+0x04` | pstr[string_count] | strings      | No field reads a string               |

## Layout 2

87 class rows.

### File Layout

| Offset               | Type                             | Field             | Notes                                           |
| -------------------- | -------------------------------- | ----------------- | ----------------------------------------------- |
| `+0x00`              | char[4]                          | magic             | `PABR`                                          |
| `+0x04`              | Class Row[87]                    | rows              | Row `n` is class type `n`                       |
| `rows+0x00`          | u32                              | skill_entry_count | Number of `skill_entries`                       |
| `rows+0x04`          | Skill Entry[skill_entry_count]   | skill_entries     | See Skill Entry                                 |
| `skill_entries+0x00` | String Table                     | string_table      | See String Table                                |
| `string_table+0x00`  | u32                              | table_start       | Offset of the string table                      |
| `string_table+0x04`  | u32                              | zero              | Always `0`                                      |

## Layout 1

82 class rows.

### File Layout

| Offset               | Type                             | Field             | Notes                                           |
| -------------------- | -------------------------------- | ----------------- | ----------------------------------------------- |
| `+0x00`              | char[4]                          | magic             | `PABR`                                          |
| `+0x04`              | Class Row[82]                    | rows              | Row `n` is class type `n`                       |
| `rows+0x00`          | u32                              | skill_entry_count | `166` on client 1784                            |
| `rows+0x04`          | Skill Entry[skill_entry_count]   | skill_entries     | See Skill Entry                                 |
| `skill_entries+0x00` | String Table                     | string_table      | See String Table                                |
| `string_table+0x00`  | u32                              | table_start       | Offset of the string table                      |
| `string_table+0x04`  | u32                              | zero              | Always `0`                                      |

## Field Names

No sheet of the private server's `DataSheets.bexcel` on client 1784 and no
2016 struct has this shape, so only the skill fields are named, by value:
every list key is a skill key whose skill number has a LOC type 10 name,
and every entry's `skill_no` is a skill of the lists (166 of 166 on client
1784). The two halves store a skill differently: a list key has the skill
number in the high half (`01 00 9F 42`, skill 17055 level 1), an entry the
skill number first (`AD 44 01 00`, skill 17581, then `1`).

## Notes

- On client 1784 the filled lists are lists 0 to 3, 8 to 13, 18 and 19 of
  class rows 16 to 25: 110 lists, 80 of three keys and 30 of one.
- All 157 keys of the client 1784 `instancedungeonskillstatic.dbss` are
  skills of these lists. That file is empty from client 2519 on.
- The `InstanceDungeonPcStat` sheet of the same private server indexes its
  32 rows the same way (`0` `F0 파이터`, `4` `E0 레인저`, `16` `P0 금수랑`,
  `24` `K0 발키리`, `28` `N0 백마법사`), four rows per class letter.

## Open Questions

### What Fixes the Class Row Count

The file stores no row count. The rows are 82 on clients 1636 to 2107, 87
on clients 2313 to 3251 and 97 from client 3474, each time the row count
of [`skillquickslotinfo.bss`](skillquickslotinfo_bss.md) of the same
client. Clients 1156 to 1485 fit no layout. On 1348 and 1485 the file is 9,155 bytes,
6,560 (1,640 x 4) shorter than the 15,715 of client 1784 with the same
1,751 non-zero bytes before the string table, so the 1,640 lists of 82
rows may have u32 counts there. The parser reads the newest layout's 97 and fails when the entry table does
not then end at `table_start`.

### What the 20 Lists and the Entry Values Mean

Twenty matches the slot count of the 2016 `gc::QuickSlot`, so a list may
be the skills of one quick slot, but no Lua of client 3482 reads the file.
The entry values `2` and `3` are unknown.
