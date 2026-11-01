# `sequencetriggerdata.bss` Format

## Purpose

Where each sequence starts on its own, and what it runs. A row names one
sequence by folder and file (`Sadang` and
`CS_SadangSeoul_06_02_Pyeseja`, the file
`sequence/sadang/cs_sadangseoul_06_02_pyeseja.paseqfe`), the regions and
the world position and radius that trigger it, the position the player
revives at, a start condition (quest state checks, `getlevel`,
`checkclass`, `checkelementalmonsterkey`), the scripts run when it starts
and ends and when it is skipped, the contents group that must be open and
six flags. The file is compiled from `sequence/sequencetriggerdata.xml`,
which the client ships next to it. It is a PABR table of variable rows
whose text sits in the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes   | Records   | Row bytes               |
| ------ | -------------- | ------------------------- | ------- | --------- | ----------------------- |
| 9      | 2156 and later | `sequencetriggerdata.bss` | 390,727 | 1,101 Row | 84 to 86, 84 on average |
| 8      | 3242           | `sequencetriggerdata.bss` | 264,735 | 731 Row   | 85                      |
| 7      | 3111 to 3212   | `sequencetriggerdata.bss` | 261,790 | 727 Row   | 83                      |
| 6      | 2703 to 3103   | `sequencetriggerdata.bss` | 249,445 | 705 Row   | 75                      |
| 5      | 2602 to 2695   | `sequencetriggerdata.bss` | 185,188 | 527 Row   | 70                      |
| 4      | 2414 to 2601   | `sequencetriggerdata.bss` | 127,170 | 367 Row   | 69                      |
| 3      | 2393 to 2407   | `sequencetriggerdata.bss` | 87,641  | 225 Row   | 68                      |
| 2      | 2276 to 2384   | `sequencetriggerdata.bss` | 86,198  | 221 Row   | 67                      |
| 1      | 2171 to 2269   | `sequencetriggerdata.bss` | 71,312  | 179 Row   | 63                      |

| Layout | File                      | Known              | Unknown      |
| ------ | ------------------------- | ------------------ | ------------ |
| 9      | `sequencetriggerdata.bss` | 390,727 B (100.0%) | 0 B (0.0%)   |
| 8      | `sequencetriggerdata.bss` | 264,004 B (99.7%)  | 731 B (0.3%) |
| 7      | `sequencetriggerdata.bss` | 261,790 B (100.0%) | 0 B (0.0%)   |
| 6      | `sequencetriggerdata.bss` | 249,445 B (100.0%) | 0 B (0.0%)   |
| 5      | `sequencetriggerdata.bss` | 185,188 B (100.0%) | 0 B (0.0%)   |
| 4      | `sequencetriggerdata.bss` | 127,170 B (100.0%) | 0 B (0.0%)   |
| 3      | `sequencetriggerdata.bss` | 87,416 B (99.7%)   | 225 B (0.3%) |
| 2      | `sequencetriggerdata.bss` | 86,198 B (100.0%)  | 0 B (0.0%)   |
| 1      | `sequencetriggerdata.bss` | 71,312 B (100.0%)  | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 9 | `c095f68491d9`  |
| 3482   | Layout 9 | `c095f68491d9`  |
| 3474   | Layout 9 | `c095f68491d9`  |
| 3473   | Layout 9 | `c095f68491d9`  |
| 3464   | Layout 9 | `c095f68491d9`  |
| 3458   | Layout 9 | `c095f68491d9`  |
| 3454   | Layout 9 | `c095f68491d9`  |
| 3444   | Layout 9 | `c095f68491d9`  |
| 3435   | Layout 9 | `c095f68491d9`  |
| 3426   | Layout 9 | `c095f68491d9`  |
| 3418   | Layout 9 | `c095f68491d9`  |
| 3412   | Layout 9 | `c095f68491d9`  |
| 3402   | Layout 9 | `c095f68491d9`  |
| 3396   | Layout 9 | `c095f68491d9`  |
| 3387   | Layout 9 | `c095f68491d9`  |
| 3381   | Layout 9 | `c095f68491d9`  |
| 3373   | Layout 9 | `c095f68491d9`  |
| 3364   | Layout 9 | `c095f68491d9`  |
| 3356   | Layout 9 | `c095f68491d9`  |
| 3349   | Layout 9 | `c095f68491d9`  |
| 3342   | Layout 9 | `c095f68491d9`  |
| 3335   | Layout 9 | `c095f68491d9`  |
| 3326   | Layout 9 | `c095f68491d9`  |
| 3321   | Layout 9 | `c095f68491d9`  |
| 3314   | Layout 9 | `c095f68491d9`  |
| 3303   | Layout 9 | `c095f68491d9`  |
| 3302   | Layout 9 | `c095f68491d9`  |
| 3293   | Layout 9 | `c095f68491d9`  |
| 3283   | Layout 9 | `c095f68491d9`  |
| 3275   | Layout 9 | `c095f68491d9`  |
| 3267   | Layout 9 | `c095f68491d9`  |
| 3258   | Layout 9 | `c095f68491d9`  |
| 3251   | Layout 9 | `c095f68491d9`  |
| 3242   | Layout 8 | `c095f68491d9`  |
| 3235   | Layout 9 | `c095f68491d9`  |
| 3229   | Layout 9 | `c095f68491d9`  |
| 3212   | Layout 7 | `c095f68491d9`  |
| 3203   | Layout 7 | `c095f68491d9`  |
| 3193   | Layout 7 | `c095f68491d9`  |
| 3186   | Layout 7 | `c095f68491d9`  |
| 3177   | Layout 7 | `c095f68491d9`  |
| 3169   | Layout 7 | `c095f68491d9`  |
| 3158   | Layout 7 | `c095f68491d9`  |
| 3151   | Layout 7 | `c095f68491d9`  |
| 3144   | Layout 7 | `c095f68491d9`  |
| 3133   | Layout 7 | `c095f68491d9`  |
| 3125   | Layout 7 | `c095f68491d9`  |
| 3118   | Layout 7 | `c095f68491d9`  |
| 3111   | Layout 7 | `c095f68491d9`  |
| 3103   | Layout 6 | `c095f68491d9`  |
| 3095   | Layout 6 | `c095f68491d9`  |
| 3086   | Layout 6 | `c095f68491d9`  |
| 3072   | Layout 6 | `c095f68491d9`  |
| 3062   | Layout 6 | `c095f68491d9`  |
| 3052   | Layout 6 | `c095f68491d9`  |
| 3045   | Layout 6 | `c095f68491d9`  |
| 3037   | Layout 6 | `c095f68491d9`  |
| 3030   | Layout 6 | `c095f68491d9`  |
| 3021   | Layout 6 | `c095f68491d9`  |
| 3012   | Layout 6 | `c095f68491d9`  |
| 3002   | Layout 6 | `c095f68491d9`  |
| 2995   | Layout 6 | `c095f68491d9`  |
| 2987   | Layout 6 | `c095f68491d9`  |
| 2978   | Layout 6 | `c095f68491d9`  |
| 2970   | Layout 6 | `c095f68491d9`  |
| 2959   | Layout 6 | `c095f68491d9`  |
| 2951   | Layout 6 | `c095f68491d9`  |
| 2942   | Layout 6 | `c095f68491d9`  |
| 2935   | Layout 6 | `c095f68491d9`  |
| 2932   | Layout 6 | `c095f68491d9`  |
| 2923   | Layout 6 | `c095f68491d9`  |
| 2919   | Layout 6 | `c095f68491d9`  |
| 2907   | Layout 6 | `c095f68491d9`  |
| 2900   | Layout 6 | `c095f68491d9`  |
| 2891   | Layout 6 | `c095f68491d9`  |
| 2882   | Layout 6 | `c095f68491d9`  |
| 2872   | Layout 6 | `c095f68491d9`  |
| 2863   | Layout 6 | `c095f68491d9`  |
| 2855   | Layout 6 | `c095f68491d9`  |
| 2849   | Layout 6 | `c095f68491d9`  |
| 2844   | Layout 6 | `c095f68491d9`  |
| 2834   | Layout 6 | `c095f68491d9`  |
| 2825   | Layout 6 | `c095f68491d9`  |
| 2819   | Layout 6 | `c095f68491d9`  |
| 2811   | Layout 6 | `c095f68491d9`  |
| 2803   | Layout 6 | `c095f68491d9`  |
| 2794   | Layout 6 | `c095f68491d9`  |
| 2783   | Layout 6 | `c095f68491d9`  |
| 2774   | Layout 6 | `c095f68491d9`  |
| 2765   | Layout 6 | `c095f68491d9`  |
| 2756   | Layout 6 | `c095f68491d9`  |
| 2750   | Layout 6 | `c095f68491d9`  |
| 2743   | Layout 6 | `c095f68491d9`  |
| 2736   | Layout 6 | `c095f68491d9`  |
| 2726   | Layout 6 | `c095f68491d9`  |
| 2717   | Layout 6 | `c095f68491d9`  |
| 2709   | Layout 6 | `c095f68491d9`  |
| 2703   | Layout 6 | `c095f68491d9`  |
| 2695   | Layout 5 | `c095f68491d9`  |
| 2684   | Layout 5 | `c095f68491d9`  |
| 2672   | Layout 5 | `c095f68491d9`  |
| 2665   | Layout 5 | `c095f68491d9`  |
| 2657   | Layout 5 | `c095f68491d9`  |
| 2649   | Layout 5 | `c095f68491d9`  |
| 2644   | Layout 5 | `c095f68491d9`  |
| 2637   | Layout 5 | `c095f68491d9`  |
| 2629   | Layout 5 | `c095f68491d9`  |
| 2619   | Layout 5 | `c095f68491d9`  |
| 2612   | Layout 5 | `c095f68491d9`  |
| 2606   | Layout 5 | `c095f68491d9`  |
| 2602   | Layout 5 | `c095f68491d9`  |
| 2601   | Layout 4 | `c095f68491d9`  |
| 2592   | Layout 4 | `c095f68491d9`  |
| 2583   | Layout 4 | `c095f68491d9`  |
| 2575   | Layout 4 | `c095f68491d9`  |
| 2567   | Layout 4 | `c095f68491d9`  |
| 2560   | Layout 4 | `c095f68491d9`  |
| 2553   | Layout 4 | `c095f68491d9`  |
| 2545   | Layout 4 | `c095f68491d9`  |
| 2538   | Layout 4 | `c095f68491d9`  |
| 2529   | Layout 4 | `c095f68491d9`  |
| 2519   | Layout 4 | `c095f68491d9`  |
| 2513   | Layout 4 | `c095f68491d9`  |
| 2510   | Layout 4 | `c095f68491d9`  |
| 2507   | Layout 4 | `c095f68491d9`  |
| 2503   | Layout 4 | `c095f68491d9`  |
| 2498   | Layout 4 | `c095f68491d9`  |
| 2492   | Layout 4 | `c095f68491d9`  |
| 2487   | Layout 4 | `c095f68491d9`  |
| 2480   | Layout 4 | `c095f68491d9`  |
| 2474   | Layout 4 | `c095f68491d9`  |
| 2468   | Layout 4 | `c095f68491d9`  |
| 2460   | Layout 4 | `c095f68491d9`  |
| 2453   | Layout 4 | `c095f68491d9`  |
| 2444   | Layout 4 | `c095f68491d9`  |
| 2438   | Layout 4 | `c095f68491d9`  |
| 2434   | Layout 4 | `c095f68491d9`  |
| 2429   | Layout 4 | `c095f68491d9`  |
| 2421   | Layout 4 | `c095f68491d9`  |
| 2414   | Layout 4 | `c095f68491d9`  |
| 2407   | Layout 3 | `c095f68491d9`  |
| 2401   | Layout 3 | `c095f68491d9`  |
| 2397   | Layout 3 | `c095f68491d9`  |
| 2393   | Layout 3 | `c095f68491d9`  |
| 2384   | Layout 2 | `c095f68491d9`  |
| 2378   | Layout 2 | `c095f68491d9`  |
| 2372   | Layout 2 | `c095f68491d9`  |
| 2358   | Layout 2 | `c095f68491d9`  |
| 2352   | Layout 2 | `c095f68491d9`  |
| 2347   | Layout 2 | `c095f68491d9`  |
| 2343   | Layout 2 | `c095f68491d9`  |
| 2335   | Layout 2 | `c095f68491d9`  |
| 2327   | Layout 2 | `c095f68491d9`  |
| 2324   | Layout 2 | `c095f68491d9`  |
| 2319   | Layout 2 | `c095f68491d9`  |
| 2313   | Layout 2 | `c095f68491d9`  |
| 2308   | Layout 2 | `c095f68491d9`  |
| 2302   | Layout 2 | `c095f68491d9`  |
| 2295   | Layout 2 | `c095f68491d9`  |
| 2290   | Layout 2 | `c095f68491d9`  |
| 2284   | Layout 2 | `c095f68491d9`  |
| 2276   | Layout 2 | `c095f68491d9`  |
| 2269   | Layout 1 | `c095f68491d9`  |
| 2259   | Layout 1 | `c095f68491d9`  |
| 2250   | Layout 1 | `c095f68491d9`  |
| 2243   | Layout 1 | `c095f68491d9`  |
| 2235   | Layout 1 | `c095f68491d9`  |
| 2229   | Layout 1 | `c095f68491d9`  |
| 2224   | Layout 1 | `c095f68491d9`  |
| 2218   | Layout 1 | `c095f68491d9`  |
| 2215   | Layout 1 | `c095f68491d9`  |
| 2207   | Layout 1 | `c095f68491d9`  |
| 2203   | Layout 9 | `c095f68491d9`  |
| 2196   | Layout 9 | `c095f68491d9`  |
| 2192   | Layout 9 | `c095f68491d9`  |
| 2189   | Layout 9 | `c095f68491d9`  |
| 2183   | Layout 1 | `c095f68491d9`  |
| 2179   | Layout 1 | `c095f68491d9`  |
| 2171   | Layout 1 | `c095f68491d9`  |
| 2163   | Layout 9 | `c095f68491d9`  |
| 2156   | Layout 9 | `c095f68491d9`  |
| 2151   | No file  | `c095f68491d9`  |
| 2147   | No file  | `c095f68491d9`  |
| 2142   | No file  | `c095f68491d9`  |
| 2138   | No file  | `c095f68491d9`  |
| 2134   | No file  | `c095f68491d9`  |
| 2130   | No file  | `c095f68491d9`  |
| 2122   | No file  | `c095f68491d9`  |
| 2107   | No file  | `c095f68491d9`  |
| 2098   | No file  | `c095f68491d9`  |
| 2089   | No file  | `c095f68491d9`  |
| 2081   | No file  | `c095f68491d9`  |
| 2073   | No file  | `c095f68491d9`  |
| 2067   | No file  | `c095f68491d9`  |
| 2063   | No file  | `c095f68491d9`  |
| 2059   | No file  | `c095f68491d9`  |
| 2052   | No file  | `c095f68491d9`  |
| 2044   | No file  | `c095f68491d9`  |
| 2039   | No file  | `c095f68491d9`  |
| 2032   | No file  | `c095f68491d9`  |
| 2025   | No file  | `c095f68491d9`  |
| 2011   | No file  | `c095f68491d9`  |
| 2005   | No file  | `c095f68491d9`  |
| 2000   | No file  | `c095f68491d9`  |
| 1996   | No file  | `c095f68491d9`  |
| 1991   | No file  | `c095f68491d9`  |
| 1985   | No file  | `c095f68491d9`  |
| 1980   | No file  | `c095f68491d9`  |
| 1969   | No file  | `c095f68491d9`  |
| 1964   | No file  | `c095f68491d9`  |
| 1958   | No file  | `c095f68491d9`  |
| 1950   | No file  | `c095f68491d9`  |
| 1945   | No file  | `c095f68491d9`  |
| 1937   | No file  | `c095f68491d9`  |
| 1933   | No file  | `c095f68491d9`  |
| 1927   | No file  | `c095f68491d9`  |
| 1921   | No file  | `c095f68491d9`  |
| 1914   | No file  | `c095f68491d9`  |
| 1908   | No file  | `c095f68491d9`  |
| 1897   | No file  | `c095f68491d9`  |
| 1892   | No file  | `c095f68491d9`  |
| 1886   | No file  | `c095f68491d9`  |
| 1881   | No file  | `c095f68491d9`  |
| 1871   | No file  | `c095f68491d9`  |
| 1866   | No file  | `c095f68491d9`  |
| 1862   | No file  | `c095f68491d9`  |
| 1854   | No file  | `c095f68491d9`  |
| 1846   | No file  | `c095f68491d9`  |
| 1838   | No file  | `c095f68491d9`  |
| 1832   | No file  | `c095f68491d9`  |
| 1826   | No file  | `c095f68491d9`  |
| 1822   | No file  | `c095f68491d9`  |
| 1818   | No file  | `c095f68491d9`  |
| 1804   | No file  | `c095f68491d9`  |
| 1794   | No file  | `c095f68491d9`  |
| 1790   | No file  | `c095f68491d9`  |
| 1784   | No file  | `c095f68491d9`  |
| 1774   | No file  | `c095f68491d9`  |
| 1771   | No file  | `c095f68491d9`  |
| 1762   | No file  | `c095f68491d9`  |
| 1759   | No file  | `c095f68491d9`  |
| 1754   | No file  | `c095f68491d9`  |
| 1749   | No file  | `c095f68491d9`  |
| 1743   | No file  | `c095f68491d9`  |
| 1737   | No file  | `c095f68491d9`  |
| 1731   | No file  | `c095f68491d9`  |
| 1725   | No file  | `c095f68491d9`  |
| 1717   | No file  | `c095f68491d9`  |
| 1710   | No file  | `c095f68491d9`  |
| 1704   | No file  | `c095f68491d9`  |
| 1698   | No file  | `c095f68491d9`  |
| 1690   | No file  | `c095f68491d9`  |
| 1685   | No file  | `c095f68491d9`  |
| 1680   | No file  | `c095f68491d9`  |
| 1674   | No file  | `c095f68491d9`  |
| 1668   | No file  | `c095f68491d9`  |
| 1659   | No file  | `c095f68491d9`  |
| 1649   | No file  | `c095f68491d9`  |
| 1642   | No file  | `c095f68491d9`  |
| 1636   | No file  | `c095f68491d9`  |
| 1628   | No file  | `c095f68491d9`  |
| 1622   | No file  | `c095f68491d9`  |
| 1614   | No file  | `c095f68491d9`  |
| 1608   | No file  | `c095f68491d9`  |
| 1602   | No file  | `c095f68491d9`  |
| 1598   | No file  | `c095f68491d9`  |
| 1594   | No file  | `c095f68491d9`  |
| 1590   | No file  | `c095f68491d9`  |
| 1587   | No file  | `c095f68491d9`  |
| 1584   | No file  | `c095f68491d9`  |
| 1579   | No file  | `c095f68491d9`  |
| 1572   | No file  | `c095f68491d9`  |
| 1565   | No file  | `c095f68491d9`  |
| 1559   | No file  | `c095f68491d9`  |
| 1554   | No file  | `c095f68491d9`  |
| 1547   | No file  | `c095f68491d9`  |
| 1537   | No file  | `c095f68491d9`  |
| 1529   | No file  | `c095f68491d9`  |
| 1524   | No file  | `c095f68491d9`  |
| 1519   | No file  | `c095f68491d9`  |
| 1509   | No file  | `c095f68491d9`  |
| 1506   | No file  | `c095f68491d9`  |
| 1504   | No file  | `c095f68491d9`  |
| 1500   | No file  | `c095f68491d9`  |
| 1493   | No file  | `c095f68491d9`  |
| 1489   | No file  | `c095f68491d9`  |
| 1485   | No file  | `c095f68491d9`  |
| 1481   | No file  | `c095f68491d9`  |
| 1474   | No file  | `c095f68491d9`  |
| 1466   | No file  | `c095f68491d9`  |
| 1462   | No file  | `c095f68491d9`  |
| 1459   | No file  | `c095f68491d9`  |
| 1453   | No file  | `c095f68491d9`  |
| 1450   | No file  | `c095f68491d9`  |
| 1445   | No file  | `c095f68491d9`  |
| 1439   | No file  | `c095f68491d9`  |
| 1433   | No file  | `c095f68491d9`  |
| 1430   | No file  | `c095f68491d9`  |
| 1426   | No file  | `c095f68491d9`  |
| 1421   | No file  | `c095f68491d9`  |
| 1417   | No file  | `c095f68491d9`  |
| 1416   | No file  | `c095f68491d9`  |
| 1409   | No file  | `c095f68491d9`  |
| 1405   | No file  | `c095f68491d9`  |
| 1401   | No file  | `c095f68491d9`  |
| 1396   | No file  | `c095f68491d9`  |
| 1391   | No file  | `c095f68491d9`  |
| 1390   | No file  | `c095f68491d9`  |
| 1386   | No file  | `c095f68491d9`  |
| 1381   | No file  | `c095f68491d9`  |
| 1379   | No file  | `c095f68491d9`  |
| 1372   | No file  | `c095f68491d9`  |
| 1366   | No file  | `c095f68491d9`  |
| 1364   | No file  | `c095f68491d9`  |
| 1363   | No file  | `c095f68491d9`  |
| 1360   | No file  | `c095f68491d9`  |
| 1358   | No file  | `c095f68491d9`  |
| 1355   | No file  | `c095f68491d9`  |
| 1351   | No file  | `c095f68491d9`  |
| 1348   | No file  | `c095f68491d9`  |
| 1346   | No file  | `c095f68491d9`  |
| 1341   | No file  | `c095f68491d9`  |
| 1340   | No file  | `c095f68491d9`  |
| 1338   | No file  | `c095f68491d9`  |
| 1335   | No file  | `c095f68491d9`  |
| 1333   | No file  | `c095f68491d9`  |
| 1329   | No file  | `c095f68491d9`  |
| 1327   | No file  | `c095f68491d9`  |
| 1324   | No file  | `c095f68491d9`  |
| 1321   | No file  | `c095f68491d9`  |
| 1319   | No file  | `c095f68491d9`  |
| 1318   | No file  | `c095f68491d9`  |
| 1316   | No file  | `c095f68491d9`  |
| 1313   | No file  | `c095f68491d9`  |
| 1311   | No file  | `c095f68491d9`  |
| 1309   | No file  | `c095f68491d9`  |
| 1304   | No file  | `c095f68491d9`  |
| 1292   | No file  | `c095f68491d9`  |
| 1286   | No file  | `c095f68491d9`  |
| 1280   | No file  | `c095f68491d9`  |
| 1276   | No file  | `c095f68491d9`  |
| 1267   | No file  | `c095f68491d9`  |
| 1261   | No file  | `c095f68491d9`  |
| 1256   | No file  | `c095f68491d9`  |
| 1250   | No file  | `c095f68491d9`  |
| 1246   | No file  | `c095f68491d9`  |
| 1239   | No file  | `c095f68491d9`  |
| 1230   | No file  | `c095f68491d9`  |
| 1226   | No file  | `c095f68491d9`  |
| 1220   | No file  | `c095f68491d9`  |
| 1217   | No file  | `c095f68491d9`  |
| 1211   | No file  | `c095f68491d9`  |
| 1210   | No file  | `c095f68491d9`  |
| 1208   | No file  | `c095f68491d9`  |
| 1203   | No file  | `c095f68491d9`  |
| 1197   | No file  | `c095f68491d9`  |
| 1194   | No file  | `c095f68491d9`  |
| 1192   | No file  | `c095f68491d9`  |
| 1187   | No file  | `c095f68491d9`  |
| 1183   | No file  | `c095f68491d9`  |
| 1177   | No file  | `c095f68491d9`  |
| 1173   | No file  | `c095f68491d9`  |
| 1167   | No file  | `c095f68491d9`  |
| 1164   | No file  | `c095f68491d9`  |
| 1156   | No file  | `c095f68491d9`  |
| 1149   | No file  | `c095f68491d9`  |
| 1144   | No file  | `c095f68491d9`  |
| 1137   | No file  | `c095f68491d9`  |
| 1132   | No file  | `c095f68491d9`  |
| 1127   | No file  | `c095f68491d9`  |
| 1122   | No file  | `c095f68491d9`  |
| 1118   | No file  | `c095f68491d9`  |
| 1114   | No file  | `c095f68491d9`  |
| 1109   | No file  | `c095f68491d9`  |
| 1102   | No file  | `c095f68491d9`  |
| 1096   | No file  | `c095f68491d9`  |
| 1088   | No file  | `c095f68491d9`  |
| 1081   | No file  | `c095f68491d9`  |
| 1076   | No file  | `c095f68491d9`  |
| 1069   | No file  | `c095f68491d9`  |
| 1064   | No file  | `c095f68491d9`  |
| 1058   | No file  | `c095f68491d9`  |
| 1051   | No file  | `c095f68491d9`  |
| 1044   | No file  | `c095f68491d9`  |
| 1036   | No file  | `c095f68491d9`  |
| 1026   | No file  | `c095f68491d9`  |
| 1016   | No file  | `c095f68491d9`  |
| 1009   | No file  | `c095f68491d9`  |
| 1005   | No file  | `c095f68491d9`  |
| 1000   | No file  | `c095f68491d9`  |
| 998    | No file  | `c095f68491d9`  |
| 990    | No file  | `c095f68491d9`  |
| 979    | No file  | `c095f68491d9`  |
| 972    | No file  | `c095f68491d9`  |
| 963    | No file  | `c095f68491d9`  |
| 955    | No file  | `c095f68491d9`  |
| 946    | No file  | `c095f68491d9`  |
| 938    | No file  | `c095f68491d9`  |
| 927    | No file  | `c095f68491d9`  |
| 911    | No file  | `c095f68491d9`  |
| 904    | No file  | `c095f68491d9`  |
| 899    | No file  | `c095f68491d9`  |
| 894    | No file  | `c095f68491d9`  |
| 885    | No file  | `c095f68491d9`  |
| 879    | No file  | `c095f68491d9`  |
| 872    | No file  | `c095f68491d9`  |
| 864    | No file  | `c095f68491d9`  |
| 855    | No file  | `c095f68491d9`  |
| 853    | No file  | `c095f68491d9`  |
| 845    | No file  | `c095f68491d9`  |
| 837    | No file  | `c095f68491d9`  |
| 829    | No file  | `c095f68491d9`  |
| 822    | No file  | `c095f68491d9`  |
| 814    | No file  | `c095f68491d9`  |
| 805    | No file  | `c095f68491d9`  |
| 794    | No file  | `c095f68491d9`  |
| 787    | No file  | `c095f68491d9`  |
| 780    | No file  | `c095f68491d9`  |
| 771    | No file  | `c095f68491d9`  |
| 760    | No file  | `c095f68491d9`  |
| 748    | No file  | `c095f68491d9`  |
| 741    | No file  | `c095f68491d9`  |
| 736    | No file  | `c095f68491d9`  |
| 731    | No file  | `c095f68491d9`  |
| 723    | No file  | `c095f68491d9`  |
| 711    | No file  | `c095f68491d9`  |
| 707    | No file  | `c095f68491d9`  |
| 697    | No file  | `c095f68491d9`  |
| 689    | No file  | `c095f68491d9`  |
| 683    | No file  | `c095f68491d9`  |
| 678    | No file  | `c095f68491d9`  |
| 670    | No file  | `c095f68491d9`  |
| 661    | No file  | `c095f68491d9`  |
| 656    | No file  | `c095f68491d9`  |
| 652    | No file  | `c095f68491d9`  |
| 643    | No file  | `c095f68491d9`  |
| 637    | No file  | `c095f68491d9`  |
| 630    | No file  | `c095f68491d9`  |
| 627    | No file  | `c095f68491d9`  |
| 621    | No file  | `c095f68491d9`  |
| 617    | No file  | `c095f68491d9`  |
| 615    | No file  | `c095f68491d9`  |
| 606    | No file  | `c095f68491d9`  |
| 599    | No file  | `c095f68491d9`  |
| 592    | No file  | `c095f68491d9`  |
| 586    | No file  | `c095f68491d9`  |
| 577    | No file  | `c095f68491d9`  |
| 569    | No file  | `c095f68491d9`  |
| 561    | No file  | `c095f68491d9`  |
| 554    | No file  | `c095f68491d9`  |
| 542    | No file  | `c095f68491d9`  |
| 532    | No file  | `c095f68491d9`  |
| 531    | No file  | `c095f68491d9`  |
| 526    | No file  | `c095f68491d9`  |
| 521    | No file  | `c095f68491d9`  |
| 517    | No file  | `c095f68491d9`  |
| 510    | No file  | `c095f68491d9`  |
| 508    | No file  | `c095f68491d9`  |
| 504    | No file  | `c095f68491d9`  |
| 497    | No file  | `c095f68491d9`  |
| 491    | No file  | `c095f68491d9`  |
| 485    | No file  | `c095f68491d9`  |
| 478    | No file  | `c095f68491d9`  |
| 472    | No file  | `c095f68491d9`  |
| 466    | No file  | `c095f68491d9`  |
| 457    | No file  | `c095f68491d9`  |
| 452    | No file  | `c095f68491d9`  |
| 449    | No file  | `c095f68491d9`  |
| 435    | No file  | `c095f68491d9`  |

<!-- versions:end -->

## Companion Files

None. The handler names the regions with their LOC type 17 names from
`languagedata_*.loc` when it is loaded. The sequence stays a path: the
`.paseqfe` sequences under `sequence/` have no handler.

All multi-byte values are little-endian.

## Layout 9

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of rows                                |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (variable: 82 bytes + region keys)

| Offset             | Type              | Field                   | Notes                                                                                                   |
| ------------------ | ----------------- | ----------------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00`            | u32               | file_name_hash          | ASCII key hash (lookup3, seed `0xC5EDE`) of `file_name`; matches on every row                           |
| `+0x04`            | u32               | file_name               | Index into `strings`: the sequence file without folder or extension (`CS_SadangSeoul_06_02_Pyeseja`); unique |
| `+0x08`            | u32               | folder                  | Index into `strings`: the folder under `sequence/` (`Sadang`, `PEDU/EdaniaBoss`); empty on 6 rows of client 3482       |
| `+0x0C`            | u32               | start_condition         | Index into `strings`: the script that must hold for the sequence to start; empty when none              |
| `+0x10`            | u32               | start_execute           | Index into `strings`: the script run when the sequence starts                                           |
| `+0x14`            | u32               | end_execute             | Index into `strings`: the script run when the sequence ends                                             |
| `+0x18`            | u32               | force_skip_end_execute  | Index into `strings`: the script run in place of `end_execute` when the sequence is force skipped       |
| `+0x1C`            | u32               | skip_condition          | Index into `strings`: the condition for skipping; empty on every row of client 3482                     |
| `+0x20`            | u32               | contents_group_open     | Index into `strings`: the contents group key as decimal text (`863`, `2186`)                            |
| `+0x24`            | f32[3]            | position                | World x, y, z of the trigger area                                                                       |
| `+0x30`            | f32[3]            | resurrect_position      | World x, y, z the player revives at during the sequence                                                 |
| `+0x3C`            | u64               | region_count            | Number of region keys; `1` on all but one row of client 3482                                                           |
| `+0x44`            | u16[region_count] | region_keys             | `regioninfo.bss` regions of the trigger (`1496` Geunjeongjeon Hall), LOC type 17                        |
| `region_keys+0x00` | u32               | file_name_hash_dup      | Same value as `file_name_hash` on every row                                                             |
| `region_keys+0x04` | f32               | radius                  | Radius of the trigger area around `position`, in world units; `0` on 149 rows of client 3482                           |
| `region_keys+0x08` | u8                | use_client_spawn        | XML `UseClientSpawn`                                                                                    |
| `region_keys+0x09` | u8                | exit_character_select   | XML `ExitCharacterSelect`                                                                               |
| `region_keys+0x0A` | u8                | pre_update_fade_out     | XML `PreUpdateFadeOut`                                                                                  |
| `region_keys+0x0B` | u8                | party_sequence          | XML `PartySequence`                                                                                     |
| `region_keys+0x0C` | u8                | character_swap_sequence | XML `CharacterSwapSequence`; `0` on every row of client 3482                                            |
| `region_keys+0x0D` | u8                | force_skip_sequence     | XML `ForceSkipSequence`                                                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                         |
| ------- | ------------------ | ------------ | ----------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                             |
| `+0x04` | pstr[string_count] | strings      | UTF-8 names, folders, scripts and keys; one empty string serves every empty field |

## Layout 8

The row has one more flag byte, `unknown_region_keys_0d`, between
`character_swap_sequence` and `force_skip_sequence`.

### Row (variable: 83 bytes + region keys)

| Offset             | Type              | Field                   | Notes                                                    |
| ------------------ | ----------------- | ----------------------- | -------------------------------------------------------- |
| `+0x00`            | u32               | file_name_hash          | As in Layout 9                                           |
| `+0x04`            | u32               | file_name               | As in Layout 9                                           |
| `+0x08`            | u32               | folder                  | As in Layout 9                                           |
| `+0x0C`            | u32               | start_condition         | As in Layout 9                                           |
| `+0x10`            | u32               | start_execute           | As in Layout 9                                           |
| `+0x14`            | u32               | end_execute             | As in Layout 9                                           |
| `+0x18`            | u32               | force_skip_end_execute  | As in Layout 9                                           |
| `+0x1C`            | u32               | skip_condition          | As in Layout 9                                           |
| `+0x20`            | u32               | contents_group_open     | As in Layout 9                                           |
| `+0x24`            | f32[3]            | position                | As in Layout 9                                           |
| `+0x30`            | f32[3]            | resurrect_position      | As in Layout 9                                           |
| `+0x3C`            | u64               | region_count            | As in Layout 9                                           |
| `+0x44`            | u16[region_count] | region_keys             | As in Layout 9                                           |
| `region_keys+0x00` | u32               | file_name_hash_dup      | As in Layout 9                                           |
| `region_keys+0x04` | f32               | radius                  | As in Layout 9                                           |
| `region_keys+0x08` | u8                | use_client_spawn        | As in Layout 9                                           |
| `region_keys+0x09` | u8                | exit_character_select   | As in Layout 9                                           |
| `region_keys+0x0A` | u8                | pre_update_fade_out     | As in Layout 9                                           |
| `region_keys+0x0B` | u8                | party_sequence          | As in Layout 9                                           |
| `region_keys+0x0C` | u8                | character_swap_sequence | As in Layout 9                                           |
| `region_keys+0x0D` | u8                | unknown_region_keys_0d  | `0` on every row of client 3242; see Notes               |
| `region_keys+0x0E` | u8                | force_skip_sequence     | As in Layout 9                                           |

## Layout 7

The row has five flag bytes: no `character_swap_sequence`.

### Row (variable: 81 bytes + region keys)

| Offset             | Type              | Field                   | Notes                                                    |
| ------------------ | ----------------- | ----------------------- | -------------------------------------------------------- |
| `+0x00`            | u32               | file_name_hash          | As in Layout 9                                           |
| `+0x04`            | u32               | file_name               | As in Layout 9                                           |
| `+0x08`            | u32               | folder                  | As in Layout 9                                           |
| `+0x0C`            | u32               | start_condition         | As in Layout 9                                           |
| `+0x10`            | u32               | start_execute           | As in Layout 9                                           |
| `+0x14`            | u32               | end_execute             | As in Layout 9                                           |
| `+0x18`            | u32               | force_skip_end_execute  | As in Layout 9                                           |
| `+0x1C`            | u32               | skip_condition          | As in Layout 9                                           |
| `+0x20`            | u32               | contents_group_open     | As in Layout 9                                           |
| `+0x24`            | f32[3]            | position                | As in Layout 9                                           |
| `+0x30`            | f32[3]            | resurrect_position      | As in Layout 9                                           |
| `+0x3C`            | u64               | region_count            | As in Layout 9                                           |
| `+0x44`            | u16[region_count] | region_keys             | As in Layout 9                                           |
| `region_keys+0x00` | u32               | file_name_hash_dup      | As in Layout 9                                           |
| `region_keys+0x04` | f32               | radius                  | As in Layout 9                                           |
| `region_keys+0x08` | u8                | use_client_spawn        | As in Layout 9                                           |
| `region_keys+0x09` | u8                | exit_character_select   | As in Layout 9                                           |
| `region_keys+0x0A` | u8                | pre_update_fade_out     | As in Layout 9                                           |
| `region_keys+0x0B` | u8                | party_sequence          | As in Layout 9                                           |
| `region_keys+0x0C` | u8                | force_skip_sequence     | As in Layout 9                                           |

## Layout 6

The row has one region key and no `region_count`, and the five flag
bytes of Layout 7.

### Row (75 bytes)

| Offset            | Type   | Field                  | Notes                                                    |
| ----------------- | ------ | ---------------------- | -------------------------------------------------------- |
| `+0x00`           | u32    | file_name_hash         | As in Layout 9                                           |
| `+0x04`           | u32    | file_name              | As in Layout 9                                           |
| `+0x08`           | u32    | folder                 | As in Layout 9                                           |
| `+0x0C`           | u32    | start_condition        | As in Layout 9                                           |
| `+0x10`           | u32    | start_execute          | As in Layout 9                                           |
| `+0x14`           | u32    | end_execute            | As in Layout 9                                           |
| `+0x18`           | u32    | force_skip_end_execute | As in Layout 9                                           |
| `+0x1C`           | u32    | skip_condition         | As in Layout 9                                           |
| `+0x20`           | u32    | contents_group_open    | As in Layout 9                                           |
| `+0x24`           | f32[3] | position               | As in Layout 9                                           |
| `+0x30`           | f32[3] | resurrect_position     | As in Layout 9                                           |
| `+0x3C`           | u16    | region_keys            | The one region of the trigger; no count before it        |
| `+0x3E`           | u32    | file_name_hash_dup     | As in Layout 9                                           |
| `+0x42`           | f32    | radius                 | As in Layout 9                                           |
| `+0x46`           | u8     | use_client_spawn       | As in Layout 9                                           |
| `+0x47`           | u8     | exit_character_select  | As in Layout 9                                           |
| `+0x48`           | u8     | pre_update_fade_out    | As in Layout 9                                           |
| `+0x49`           | u8     | party_sequence         | As in Layout 9                                           |
| `+0x4A`           | u8     | force_skip_sequence    | As in Layout 9                                           |

## Layout 5

The row has seven string indexes, no `force_skip_end_execute`, and four
flag bytes, no `force_skip_sequence`.

### Row (70 bytes)

| Offset  | Type   | Field                 | Notes                                             |
| ------- | ------ | --------------------- | ------------------------------------------------- |
| `+0x00` | u32    | file_name_hash        | As in Layout 9                                    |
| `+0x04` | u32    | file_name             | As in Layout 9                                    |
| `+0x08` | u32    | folder                | As in Layout 9                                    |
| `+0x0C` | u32    | start_condition       | As in Layout 9                                    |
| `+0x10` | u32    | start_execute         | As in Layout 9                                    |
| `+0x14` | u32    | end_execute           | As in Layout 9                                    |
| `+0x18` | u32    | skip_condition        | As in Layout 9; see Field Names                   |
| `+0x1C` | u32    | contents_group_open   | As in Layout 9                                    |
| `+0x20` | f32[3] | position              | As in Layout 9                                    |
| `+0x2C` | f32[3] | resurrect_position    | As in Layout 9                                    |
| `+0x38` | u16    | region_keys           | The one region of the trigger; no count before it |
| `+0x3A` | u32    | file_name_hash_dup    | As in Layout 9                                    |
| `+0x3E` | f32    | radius                | As in Layout 9                                    |
| `+0x42` | u8     | use_client_spawn      | As in Layout 9                                    |
| `+0x43` | u8     | exit_character_select | As in Layout 9                                    |
| `+0x44` | u8     | pre_update_fade_out   | As in Layout 9                                    |
| `+0x45` | u8     | party_sequence        | As in Layout 9                                    |

## Layout 4

The row has three flag bytes: no `party_sequence`.

### Row (69 bytes)

| Offset  | Type   | Field                 | Notes                                             |
| ------- | ------ | --------------------- | ------------------------------------------------- |
| `+0x00` | u32    | file_name_hash        | As in Layout 9                                    |
| `+0x04` | u32    | file_name             | As in Layout 9                                    |
| `+0x08` | u32    | folder                | As in Layout 9                                    |
| `+0x0C` | u32    | start_condition       | As in Layout 9                                    |
| `+0x10` | u32    | start_execute         | As in Layout 9                                    |
| `+0x14` | u32    | end_execute           | As in Layout 9                                    |
| `+0x18` | u32    | skip_condition        | As in Layout 9; see Field Names                   |
| `+0x1C` | u32    | contents_group_open   | As in Layout 9                                    |
| `+0x20` | f32[3] | position              | As in Layout 9                                    |
| `+0x2C` | f32[3] | resurrect_position    | As in Layout 9                                    |
| `+0x38` | u16    | region_keys           | The one region of the trigger; no count before it |
| `+0x3A` | u32    | file_name_hash_dup    | As in Layout 9                                    |
| `+0x3E` | f32    | radius                | As in Layout 9                                    |
| `+0x42` | u8     | use_client_spawn      | As in Layout 9                                    |
| `+0x43` | u8     | exit_character_select | As in Layout 9                                    |
| `+0x44` | u8     | pre_update_fade_out   | As in Layout 9                                    |

## Layout 3

The row has two flag bytes. The second is `0` on every row; see Open
Questions.

### Row (68 bytes)

| Offset  | Type   | Field               | Notes                                             |
| ------- | ------ | ------------------- | ------------------------------------------------- |
| `+0x00` | u32    | file_name_hash      | As in Layout 9                                    |
| `+0x04` | u32    | file_name           | As in Layout 9                                    |
| `+0x08` | u32    | folder              | As in Layout 9                                    |
| `+0x0C` | u32    | start_condition     | As in Layout 9                                    |
| `+0x10` | u32    | start_execute       | As in Layout 9                                    |
| `+0x14` | u32    | end_execute         | As in Layout 9                                    |
| `+0x18` | u32    | skip_condition      | As in Layout 9; see Field Names                   |
| `+0x1C` | u32    | contents_group_open | As in Layout 9                                    |
| `+0x20` | f32[3] | position            | As in Layout 9                                    |
| `+0x2C` | f32[3] | resurrect_position  | As in Layout 9                                    |
| `+0x38` | u16    | region_keys         | The one region of the trigger; no count before it |
| `+0x3A` | u32    | file_name_hash_dup  | As in Layout 9                                    |
| `+0x3E` | f32    | radius              | As in Layout 9                                    |
| `+0x42` | u8     | use_client_spawn    | As in Layout 9                                    |
| `+0x43` | u8     | unknown_43          | `0` on every row of clients 2393 to 2407          |

## Layout 2

The row has one flag byte, `use_client_spawn`.

### Row (67 bytes)

| Offset  | Type   | Field               | Notes                                             |
| ------- | ------ | ------------------- | ------------------------------------------------- |
| `+0x00` | u32    | file_name_hash      | As in Layout 9                                    |
| `+0x04` | u32    | file_name           | As in Layout 9                                    |
| `+0x08` | u32    | folder              | As in Layout 9                                    |
| `+0x0C` | u32    | start_condition     | As in Layout 9                                    |
| `+0x10` | u32    | start_execute       | As in Layout 9                                    |
| `+0x14` | u32    | end_execute         | As in Layout 9                                    |
| `+0x18` | u32    | skip_condition      | As in Layout 9; see Field Names                   |
| `+0x1C` | u32    | contents_group_open | As in Layout 9                                    |
| `+0x20` | f32[3] | position            | As in Layout 9                                    |
| `+0x2C` | f32[3] | resurrect_position  | As in Layout 9                                    |
| `+0x38` | u16    | region_keys         | The one region of the trigger; no count before it |
| `+0x3A` | u32    | file_name_hash_dup  | As in Layout 9                                    |
| `+0x3E` | f32    | radius              | As in Layout 9                                    |
| `+0x42` | u8     | use_client_spawn    | As in Layout 9                                    |

## Layout 1

The row has six string indexes: no `folder`.

### Row (63 bytes)

| Offset  | Type   | Field               | Notes                                                                   |
| ------- | ------ | ------------------- | ----------------------------------------------------------------------- |
| `+0x00` | u32    | file_name_hash      | As in Layout 9                                                          |
| `+0x04` | u32    | file_name           | As in Layout 9                                                          |
| `+0x08` | u32    | start_condition     | As in Layout 9                                                          |
| `+0x0C` | u32    | start_execute       | As in Layout 9                                                          |
| `+0x10` | u32    | end_execute         | As in Layout 9                                                          |
| `+0x14` | u32    | skip_condition      | As in Layout 9; `getknowledge(11773);` and other `getknowledge` calls on clients 2207 to 2250, see Field Names |
| `+0x18` | u32    | contents_group_open | As in Layout 9                                                          |
| `+0x1C` | f32[3] | position            | As in Layout 9                                                          |
| `+0x28` | f32[3] | resurrect_position  | As in Layout 9                                                          |
| `+0x34` | u16    | region_keys         | The one region of the trigger; no count before it                       |
| `+0x36` | u32    | file_name_hash_dup  | As in Layout 9                                                          |
| `+0x3A` | f32    | radius              | As in Layout 9                                                          |
| `+0x3E` | u8     | use_client_spawn    | As in Layout 9                                                          |

## Scripts

The script fields hold calls joined by `;`. A `!` in front of a call
negates it, and `<or>` splits a condition into alternatives. Counts are
rows using each call, client 3482 (1,101 rows, 3,346 strings).

| Field                    | Calls (rows)                                                                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `start_condition`        | `checkquestcondition` (715), `progressquest` (631), `clearquest` (457), `getlevel` (144), `checkclass` (118), `checkwoman` (50), `checkelementalmonsterkey` (21) and 8 more; empty on 63 rows |
| `start_execute`          | `acceptquest` (370); empty on 731 rows                                                                                                    |
| `end_execute`            | `completequestcondition` (855), `setposition` (250), `completequest` (84), `acceptquest` (57), `pushitem` (33), `pushknowledge` (10) and 4 more; empty on 117 rows |
| `force_skip_end_execute` | `pushitem`, `completequest` and `tutorialendteleportroute`, on 2 rows                                                                     |

## Flags

Rows with each flag set, client 3482:

| Flag                      | Rows |
| ------------------------- | ---- |
| `use_client_spawn`        | 26   |
| `exit_character_select`   | 67   |
| `pre_update_fade_out`     | 9    |
| `party_sequence`          | 11   |
| `character_swap_sequence` | 0    |
| `force_skip_sequence`     | 2    |

## Field Names

Every field but `file_name_hash` and its copy is a `<TriggerData>`
element of `sequence/sequencetriggerdata.xml` in the same client. The
XML's `FileName` attribute is `folder` and `file_name` joined by `/`
(`Sadang/CS_SadangSeoul_06_02_PyesejaHard`); `RegionKey` (`1109,1110`
on the row with two regions), `Position`, `Radius`, `ResurrectPosition`,
`StartCondition`, `StartExecute`, `EndExecute`, `ForceSkipEndExecute`,
`SkipCondition`, `ContentsGroupOpen` and the six flags follow. On client
3482 all 1,101 rows match their XML element in every field and in file
order; the XML has 21 more elements the file leaves out, test and console
sequences among them (`CS_TEST_VelliaTest`,
`Seoul/CS_Seoul_01_00_BalanhosuToNampo_Console`). The XML writes the flags
as `True` and `False` in the order the file stores them;
`CharacterSwapSequence` is `False` on every element, so its byte is
placed by that order alone. Clients 3275 to 3373 set it on their
`characterswap` rows (`striker_sorceress`), the only rows with it set.

The clients of Layouts 1 to 5 ship no XML. Their fields are named by
matching each row to the row with the same `file_name_hash` in the first
client of the next layout. At each step the rows keep their values in
every field both layouts have, and one field or flag byte is new:

| Step   | Clients    | Rows matched | Rows equal in every shared field | New in the newer layout                         |
| ------ | ---------- | ------------ | -------------------------------- | ----------------------------------------------- |
| 1 to 2 | 2269, 2276 | 179          | 178                              | `folder` after `file_name`                      |
| 2 to 3 | 2384, 2393 | 221          | 221                              | `unknown_43` after `use_client_spawn`           |
| 3 to 4 | 2407, 2414 | 225          | 225                              | A third flag byte                               |
| 4 to 5 | 2601, 2602 | 364          | 364                              | `party_sequence` after `pre_update_fade_out`    |
| 5 to 6 | 2695, 2703 | 527          | 523                              | `force_skip_end_execute` and `force_skip_sequence` |

The rows that differ changed a script (`end_execute` of
`CS_Tutorial_Illezra_00` gains `PushItem(66242,0,1);` on client 2703) or
moved (`CS_Calpheon_90_06_AfterCalpheon`). On client 2601 the three flags
of Layout 4 are set on 18, 58 and 2 rows, the counts of
`use_client_spawn`, `exit_character_select` and `pre_update_fade_out` on
client 2602, and the 364 rows both clients hold keep every flag, so Layout
4 holds these three in this order.

The text field between `end_execute` and `contents_group_open` in Layouts
1 to 5 is `skip_condition`. Client 2703 adds `force_skip_end_execute` and
`force_skip_sequence` together: the two `CS_Tutorial_Illezra` rows that
set the new flag are the only rows with the new script
(`completequest(14002,1);tutorialEndTeleportRoute();PushItem(768674,0,1);`),
and both rows are in client 2695 without it. The older field holds
`getknowledge(11773);` and other `getknowledge` calls on 57 rows of client
2224, a condition call the start conditions also use
(`!getknowledge(3590);`); the scripts run on a trigger use
`pushknowledge`. It is empty on every row from client 2259 to 2695.

## Notes

- Clients 2156, 2163 and 2189 to 2203 ship the table empty (row count
  `0`), which every layout reads; the doc check counts them as Layout 9.
- Layouts 1 to 6 store region key `0` on rows with no trigger area: on
  client 2695, 122 of the 527 rows, all with `radius` `0`.
- On clients 3275 to 3373 the `characterswap` rows store the file name in
  lower case (`striker_striker`) and the hash of `Striker_Striker`, so
  `file_name_hash` matches the stored name on every other row only.
- Client 3242 stores 7 flag bytes (Layout 8). Matched by file name to
  client 3482, its rows hold the same values in the first four flags and
  in `force_skip_sequence`. The two bytes between them are `0` on all 731
  rows, so which of the two is the dropped field, and what it held, is
  not known; the doc takes the second.
- `file_name_hash` is the hash the cutscene tables compute from a file
  name without `.pas` (`cutscene_file_hash()` in
  `_bss/sequence_scripts/reader.py`). On client 3482 the 2 rows of
  [`sequence_skill.bss`](sequence_skill_bss.md) and the 4 of
  [`sequencetutorial_equipment.bss`](tutorial_equipment_bss.md) all key a
  sequence of this file, and their handlers show the sequence path from
  here (`_bss/sequencetriggerdata/lookup.py`); none of the 1,101 file names
  is a `sequencedatatable.bss` cutscene.
- `folder` writes both separators: `PEDU/EdaniaSub` (3 rows) and
  `PEDU\EdaniaSub` (4 rows) are one folder.
- On client 3482 the rows cover 268 regions and 75 contents groups; the
  157 `PEDU2` rows all have contents group `2186`, the group the `PEDU2`
  videos of [`videotriggerdata.bss`](videotriggerdata_bss.md) have.
- The QA scripts `abyssonehelp.luac` and `qasupportmain.luac` start a
  sequence by name with `ToClient_SequenceTriggerForQA()`.

## Open Questions

### Which Flag the Second Byte of Layout 3 Is

Clients 2393 to 2407 store two flag bytes and client 2414 three. The second
byte is `0` on every row of those clients, as is the new byte of client
2414, so whether the second byte is `exit_character_select` (the new byte
then `pre_update_fade_out`) or the other way round is not known. Each other
step adds its flag at the end of the row, which points to
`exit_character_select`. The doc names the byte `unknown_43` and the
parser reads no flag from it.
