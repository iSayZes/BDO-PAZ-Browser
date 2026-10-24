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

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes   | Records   | Row bytes               |
| ------ | -------------- | ------- | ------------------------- | ------- | --------- | ----------------------- |
| 4      | 2156 and later | 3483    | `sequencetriggerdata.bss` | 390,727 | 1,101 Row | 84 to 86, 84 on average |
| 3      | 3242           | 3242    | `sequencetriggerdata.bss` | 264,735 | 731 Row   | 85                      |
| 2      | 3111 to 3212   | 3212    | `sequencetriggerdata.bss` | 261,790 | 727 Row   | 83                      |
| 1      | 2703 to 3103   | 3103    | `sequencetriggerdata.bss` | 249,445 | 705 Row   | 75                      |

| Layout | File                      | Known              | Unknown      |
| ------ | ------------------------- | ------------------ | ------------ |
| 4      | `sequencetriggerdata.bss` | 390,727 B (100.0%) | 0 B (0.0%)   |
| 3      | `sequencetriggerdata.bss` | 264,004 B (99.7%)  | 731 B (0.3%) |
| 2      | `sequencetriggerdata.bss` | 261,790 B (100.0%) | 0 B (0.0%)   |
| 1      | `sequencetriggerdata.bss` | 249,445 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 4             | `5fd7f2510d88`  |
| 3482   | Layout 4             | `5fd7f2510d88`  |
| 3474   | Layout 4             | `5fd7f2510d88`  |
| 3473   | Layout 4             | `5fd7f2510d88`  |
| 3464   | Layout 4             | `5fd7f2510d88`  |
| 3458   | Layout 4             | `5fd7f2510d88`  |
| 3454   | Layout 4             | `5fd7f2510d88`  |
| 3444   | Layout 4             | `5fd7f2510d88`  |
| 3435   | Layout 4             | `5fd7f2510d88`  |
| 3426   | Layout 4             | `5fd7f2510d88`  |
| 3418   | Layout 4             | `5fd7f2510d88`  |
| 3412   | Layout 4             | `5fd7f2510d88`  |
| 3402   | Layout 4             | `5fd7f2510d88`  |
| 3396   | Layout 4             | `5fd7f2510d88`  |
| 3387   | Layout 4             | `5fd7f2510d88`  |
| 3381   | Layout 4             | `5fd7f2510d88`  |
| 3373   | Layout 4             | `5fd7f2510d88`  |
| 3364   | Layout 4             | `5fd7f2510d88`  |
| 3356   | Layout 4             | `5fd7f2510d88`  |
| 3349   | Layout 4             | `5fd7f2510d88`  |
| 3342   | Layout 4             | `5fd7f2510d88`  |
| 3335   | Layout 4             | `5fd7f2510d88`  |
| 3326   | Layout 4             | `5fd7f2510d88`  |
| 3321   | Layout 4             | `5fd7f2510d88`  |
| 3314   | Layout 4             | `5fd7f2510d88`  |
| 3303   | Layout 4             | `5fd7f2510d88`  |
| 3302   | Layout 4             | `5fd7f2510d88`  |
| 3293   | Layout 4             | `5fd7f2510d88`  |
| 3283   | Layout 4             | `5fd7f2510d88`  |
| 3275   | Layout 4             | `5fd7f2510d88`  |
| 3267   | Layout 4             | `5fd7f2510d88`  |
| 3258   | Layout 4             | `5fd7f2510d88`  |
| 3251   | Layout 4             | `5fd7f2510d88`  |
| 3242   | Layout 3             | `5fd7f2510d88`  |
| 3235   | Layout 4             | `5fd7f2510d88`  |
| 3229   | Layout 4             | `5fd7f2510d88`  |
| 3212   | Layout 2             | `5fd7f2510d88`  |
| 3203   | Layout 2             | `5fd7f2510d88`  |
| 3193   | Layout 2             | `5fd7f2510d88`  |
| 3186   | Layout 2             | `5fd7f2510d88`  |
| 3177   | Layout 2             | `5fd7f2510d88`  |
| 3169   | Layout 2             | `5fd7f2510d88`  |
| 3158   | Layout 2             | `5fd7f2510d88`  |
| 3151   | Layout 2             | `5fd7f2510d88`  |
| 3144   | Layout 2             | `5fd7f2510d88`  |
| 3133   | Layout 2             | `5fd7f2510d88`  |
| 3125   | Layout 2             | `5fd7f2510d88`  |
| 3118   | Layout 2             | `5fd7f2510d88`  |
| 3111   | Layout 2             | `5fd7f2510d88`  |
| 3103   | Layout 1             | `5fd7f2510d88`  |
| 3095   | Layout 1             | `5fd7f2510d88`  |
| 3086   | Layout 1             | `5fd7f2510d88`  |
| 3072   | Layout 1             | `5fd7f2510d88`  |
| 3062   | Layout 1             | `5fd7f2510d88`  |
| 3052   | Layout 1             | `5fd7f2510d88`  |
| 3045   | Layout 1             | `5fd7f2510d88`  |
| 3037   | Layout 1             | `5fd7f2510d88`  |
| 3030   | Layout 1             | `5fd7f2510d88`  |
| 3021   | Layout 1             | `5fd7f2510d88`  |
| 3012   | Layout 1             | `5fd7f2510d88`  |
| 3002   | Layout 1             | `5fd7f2510d88`  |
| 2995   | Layout 1             | `5fd7f2510d88`  |
| 2987   | Layout 1             | `5fd7f2510d88`  |
| 2978   | Layout 1             | `5fd7f2510d88`  |
| 2970   | Layout 1             | `5fd7f2510d88`  |
| 2959   | Layout 1             | `5fd7f2510d88`  |
| 2951   | Layout 1             | `5fd7f2510d88`  |
| 2942   | Layout 1             | `5fd7f2510d88`  |
| 2935   | Layout 1             | `5fd7f2510d88`  |
| 2932   | Layout 1             | `5fd7f2510d88`  |
| 2923   | Layout 1             | `5fd7f2510d88`  |
| 2919   | Layout 1             | `5fd7f2510d88`  |
| 2907   | Layout 1             | `5fd7f2510d88`  |
| 2900   | Layout 1             | `5fd7f2510d88`  |
| 2891   | Layout 1             | `5fd7f2510d88`  |
| 2882   | Layout 1             | `5fd7f2510d88`  |
| 2872   | Layout 1             | `5fd7f2510d88`  |
| 2863   | Layout 1             | `5fd7f2510d88`  |
| 2855   | Layout 1             | `5fd7f2510d88`  |
| 2849   | Layout 1             | `5fd7f2510d88`  |
| 2844   | Layout 1             | `5fd7f2510d88`  |
| 2834   | Layout 1             | `5fd7f2510d88`  |
| 2825   | Layout 1             | `5fd7f2510d88`  |
| 2819   | Layout 1             | `5fd7f2510d88`  |
| 2811   | Layout 1             | `5fd7f2510d88`  |
| 2803   | Layout 1             | `5fd7f2510d88`  |
| 2794   | Layout 1             | `5fd7f2510d88`  |
| 2783   | Layout 1             | `5fd7f2510d88`  |
| 2774   | Layout 1             | `5fd7f2510d88`  |
| 2765   | Layout 1             | `5fd7f2510d88`  |
| 2756   | Layout 1             | `5fd7f2510d88`  |
| 2750   | Layout 1             | `5fd7f2510d88`  |
| 2743   | Layout 1             | `5fd7f2510d88`  |
| 2736   | Layout 1             | `5fd7f2510d88`  |
| 2726   | Layout 1             | `5fd7f2510d88`  |
| 2717   | Layout 1             | `5fd7f2510d88`  |
| 2709   | Layout 1             | `5fd7f2510d88`  |
| 2703   | Layout 1             | `5fd7f2510d88`  |
| 2695   | No documented layout | `5fd7f2510d88`  |
| 2684   | No documented layout | `5fd7f2510d88`  |
| 2672   | No documented layout | `5fd7f2510d88`  |
| 2665   | No documented layout | `5fd7f2510d88`  |
| 2657   | No documented layout | `5fd7f2510d88`  |
| 2649   | No documented layout | `5fd7f2510d88`  |
| 2644   | No documented layout | `5fd7f2510d88`  |
| 2637   | No documented layout | `5fd7f2510d88`  |
| 2629   | No documented layout | `5fd7f2510d88`  |
| 2619   | No documented layout | `5fd7f2510d88`  |
| 2612   | No documented layout | `5fd7f2510d88`  |
| 2606   | No documented layout | `5fd7f2510d88`  |
| 2602   | No documented layout | `5fd7f2510d88`  |
| 2601   | No documented layout | `5fd7f2510d88`  |
| 2592   | No documented layout | `5fd7f2510d88`  |
| 2583   | No documented layout | `5fd7f2510d88`  |
| 2575   | No documented layout | `5fd7f2510d88`  |
| 2567   | No documented layout | `5fd7f2510d88`  |
| 2560   | No documented layout | `5fd7f2510d88`  |
| 2553   | No documented layout | `5fd7f2510d88`  |
| 2545   | No documented layout | `5fd7f2510d88`  |
| 2538   | No documented layout | `5fd7f2510d88`  |
| 2529   | No documented layout | `5fd7f2510d88`  |
| 2519   | No documented layout | `5fd7f2510d88`  |
| 2513   | No documented layout | `5fd7f2510d88`  |
| 2510   | No documented layout | `5fd7f2510d88`  |
| 2507   | No documented layout | `5fd7f2510d88`  |
| 2503   | No documented layout | `5fd7f2510d88`  |
| 2498   | No documented layout | `5fd7f2510d88`  |
| 2492   | No documented layout | `5fd7f2510d88`  |
| 2487   | No documented layout | `5fd7f2510d88`  |
| 2480   | No documented layout | `5fd7f2510d88`  |
| 2474   | No documented layout | `5fd7f2510d88`  |
| 2468   | No documented layout | `5fd7f2510d88`  |
| 2460   | No documented layout | `5fd7f2510d88`  |
| 2453   | No documented layout | `5fd7f2510d88`  |
| 2444   | No documented layout | `5fd7f2510d88`  |
| 2438   | No documented layout | `5fd7f2510d88`  |
| 2434   | No documented layout | `5fd7f2510d88`  |
| 2429   | No documented layout | `5fd7f2510d88`  |
| 2421   | No documented layout | `5fd7f2510d88`  |
| 2414   | No documented layout | `5fd7f2510d88`  |
| 2407   | No documented layout | `5fd7f2510d88`  |
| 2401   | No documented layout | `5fd7f2510d88`  |
| 2397   | No documented layout | `5fd7f2510d88`  |
| 2393   | No documented layout | `5fd7f2510d88`  |
| 2384   | No documented layout | `5fd7f2510d88`  |
| 2378   | No documented layout | `5fd7f2510d88`  |
| 2372   | No documented layout | `5fd7f2510d88`  |
| 2358   | No documented layout | `5fd7f2510d88`  |
| 2352   | No documented layout | `5fd7f2510d88`  |
| 2347   | No documented layout | `5fd7f2510d88`  |
| 2343   | No documented layout | `5fd7f2510d88`  |
| 2335   | No documented layout | `5fd7f2510d88`  |
| 2327   | No documented layout | `5fd7f2510d88`  |
| 2324   | No documented layout | `5fd7f2510d88`  |
| 2319   | No documented layout | `5fd7f2510d88`  |
| 2313   | No documented layout | `5fd7f2510d88`  |
| 2308   | No documented layout | `5fd7f2510d88`  |
| 2302   | No documented layout | `5fd7f2510d88`  |
| 2295   | No documented layout | `5fd7f2510d88`  |
| 2290   | No documented layout | `5fd7f2510d88`  |
| 2284   | No documented layout | `5fd7f2510d88`  |
| 2276   | No documented layout | `5fd7f2510d88`  |
| 2269   | No documented layout | `5fd7f2510d88`  |
| 2259   | No documented layout | `5fd7f2510d88`  |
| 2250   | No documented layout | `5fd7f2510d88`  |
| 2243   | No documented layout | `5fd7f2510d88`  |
| 2235   | No documented layout | `5fd7f2510d88`  |
| 2229   | No documented layout | `5fd7f2510d88`  |
| 2224   | No documented layout | `5fd7f2510d88`  |
| 2218   | No documented layout | `5fd7f2510d88`  |
| 2215   | No documented layout | `5fd7f2510d88`  |
| 2207   | No documented layout | `5fd7f2510d88`  |
| 2203   | Layout 4             | `5fd7f2510d88`  |
| 2196   | Layout 4             | `5fd7f2510d88`  |
| 2192   | Layout 4             | `5fd7f2510d88`  |
| 2189   | Layout 4             | `5fd7f2510d88`  |
| 2183   | No documented layout | `5fd7f2510d88`  |
| 2179   | No documented layout | `5fd7f2510d88`  |
| 2171   | No documented layout | `5fd7f2510d88`  |
| 2163   | Layout 4             | `5fd7f2510d88`  |
| 2156   | Layout 4             | `5fd7f2510d88`  |
| 2151   | No file              | `5fd7f2510d88`  |
| 2147   | No file              | `5fd7f2510d88`  |
| 2142   | No file              | `5fd7f2510d88`  |
| 2138   | No file              | `5fd7f2510d88`  |
| 2134   | No file              | `5fd7f2510d88`  |
| 2130   | No file              | `5fd7f2510d88`  |
| 2122   | No file              | `5fd7f2510d88`  |
| 2107   | No file              | `5fd7f2510d88`  |
| 2098   | No file              | `5fd7f2510d88`  |
| 2089   | No file              | `5fd7f2510d88`  |
| 2081   | No file              | `5fd7f2510d88`  |
| 2073   | No file              | `5fd7f2510d88`  |
| 2067   | No file              | `5fd7f2510d88`  |
| 2063   | No file              | `5fd7f2510d88`  |
| 2059   | No file              | `5fd7f2510d88`  |
| 2052   | No file              | `5fd7f2510d88`  |
| 2044   | No file              | `5fd7f2510d88`  |
| 2039   | No file              | `5fd7f2510d88`  |
| 2032   | No file              | `5fd7f2510d88`  |
| 2025   | No file              | `5fd7f2510d88`  |
| 2011   | No file              | `5fd7f2510d88`  |
| 2005   | No file              | `5fd7f2510d88`  |
| 2000   | No file              | `5fd7f2510d88`  |
| 1996   | No file              | `5fd7f2510d88`  |
| 1991   | No file              | `5fd7f2510d88`  |
| 1985   | No file              | `5fd7f2510d88`  |
| 1980   | No file              | `5fd7f2510d88`  |
| 1969   | No file              | `5fd7f2510d88`  |
| 1964   | No file              | `5fd7f2510d88`  |
| 1958   | No file              | `5fd7f2510d88`  |
| 1950   | No file              | `5fd7f2510d88`  |
| 1945   | No file              | `5fd7f2510d88`  |
| 1937   | No file              | `5fd7f2510d88`  |
| 1933   | No file              | `5fd7f2510d88`  |
| 1927   | No file              | `5fd7f2510d88`  |
| 1921   | No file              | `5fd7f2510d88`  |
| 1914   | No file              | `5fd7f2510d88`  |
| 1908   | No file              | `5fd7f2510d88`  |
| 1897   | No file              | `5fd7f2510d88`  |
| 1892   | No file              | `5fd7f2510d88`  |
| 1886   | No file              | `5fd7f2510d88`  |
| 1881   | No file              | `5fd7f2510d88`  |
| 1871   | No file              | `5fd7f2510d88`  |
| 1866   | No file              | `5fd7f2510d88`  |
| 1862   | No file              | `5fd7f2510d88`  |
| 1854   | No file              | `5fd7f2510d88`  |
| 1846   | No file              | `5fd7f2510d88`  |
| 1838   | No file              | `5fd7f2510d88`  |
| 1832   | No file              | `5fd7f2510d88`  |
| 1826   | No file              | `5fd7f2510d88`  |
| 1822   | No file              | `5fd7f2510d88`  |
| 1818   | No file              | `5fd7f2510d88`  |
| 1804   | No file              | `5fd7f2510d88`  |
| 1794   | No file              | `5fd7f2510d88`  |
| 1790   | No file              | `5fd7f2510d88`  |
| 1784   | No file              | `5fd7f2510d88`  |
| 1774   | No file              | `5fd7f2510d88`  |
| 1771   | No file              | `5fd7f2510d88`  |
| 1762   | No file              | `5fd7f2510d88`  |
| 1759   | No file              | `5fd7f2510d88`  |
| 1754   | No file              | `5fd7f2510d88`  |
| 1749   | No file              | `5fd7f2510d88`  |
| 1743   | No file              | `5fd7f2510d88`  |
| 1737   | No file              | `5fd7f2510d88`  |
| 1731   | No file              | `5fd7f2510d88`  |
| 1725   | No file              | `5fd7f2510d88`  |
| 1717   | No file              | `5fd7f2510d88`  |
| 1710   | No file              | `5fd7f2510d88`  |
| 1704   | No file              | `5fd7f2510d88`  |
| 1698   | No file              | `5fd7f2510d88`  |
| 1690   | No file              | `5fd7f2510d88`  |
| 1685   | No file              | `5fd7f2510d88`  |
| 1680   | No file              | `5fd7f2510d88`  |
| 1674   | No file              | `5fd7f2510d88`  |
| 1668   | No file              | `5fd7f2510d88`  |
| 1659   | No file              | `5fd7f2510d88`  |
| 1649   | No file              | `5fd7f2510d88`  |
| 1642   | No file              | `5fd7f2510d88`  |
| 1636   | No file              | `5fd7f2510d88`  |
| 1628   | No file              | `5fd7f2510d88`  |
| 1622   | No file              | `5fd7f2510d88`  |
| 1614   | No file              | `5fd7f2510d88`  |
| 1608   | No file              | `5fd7f2510d88`  |
| 1602   | No file              | `5fd7f2510d88`  |
| 1598   | No file              | `5fd7f2510d88`  |
| 1594   | No file              | `5fd7f2510d88`  |
| 1590   | No file              | `5fd7f2510d88`  |
| 1587   | No file              | `5fd7f2510d88`  |
| 1584   | No file              | `5fd7f2510d88`  |
| 1579   | No file              | `5fd7f2510d88`  |
| 1572   | No file              | `5fd7f2510d88`  |
| 1565   | No file              | `5fd7f2510d88`  |
| 1559   | No file              | `5fd7f2510d88`  |
| 1554   | No file              | `5fd7f2510d88`  |
| 1547   | No file              | `5fd7f2510d88`  |
| 1537   | No file              | `5fd7f2510d88`  |
| 1529   | No file              | `5fd7f2510d88`  |
| 1524   | No file              | `5fd7f2510d88`  |
| 1519   | No file              | `5fd7f2510d88`  |
| 1509   | No file              | `5fd7f2510d88`  |
| 1506   | No file              | `5fd7f2510d88`  |
| 1504   | No file              | `5fd7f2510d88`  |
| 1500   | No file              | `5fd7f2510d88`  |
| 1493   | No file              | `5fd7f2510d88`  |
| 1489   | No file              | `5fd7f2510d88`  |
| 1485   | No file              | `5fd7f2510d88`  |
| 1481   | No file              | `5fd7f2510d88`  |
| 1474   | No file              | `5fd7f2510d88`  |
| 1466   | No file              | `5fd7f2510d88`  |
| 1462   | No file              | `5fd7f2510d88`  |
| 1459   | No file              | `5fd7f2510d88`  |
| 1453   | No file              | `5fd7f2510d88`  |
| 1450   | No file              | `5fd7f2510d88`  |
| 1445   | No file              | `5fd7f2510d88`  |
| 1439   | No file              | `5fd7f2510d88`  |
| 1433   | No file              | `5fd7f2510d88`  |
| 1430   | No file              | `5fd7f2510d88`  |
| 1426   | No file              | `5fd7f2510d88`  |
| 1421   | No file              | `5fd7f2510d88`  |
| 1417   | No file              | `5fd7f2510d88`  |
| 1416   | No file              | `5fd7f2510d88`  |
| 1409   | No file              | `5fd7f2510d88`  |
| 1405   | No file              | `5fd7f2510d88`  |
| 1401   | No file              | `5fd7f2510d88`  |
| 1396   | No file              | `5fd7f2510d88`  |
| 1391   | No file              | `5fd7f2510d88`  |
| 1390   | No file              | `5fd7f2510d88`  |
| 1386   | No file              | `5fd7f2510d88`  |
| 1381   | No file              | `5fd7f2510d88`  |
| 1379   | No file              | `5fd7f2510d88`  |
| 1372   | No file              | `5fd7f2510d88`  |
| 1366   | No file              | `5fd7f2510d88`  |
| 1364   | No file              | `5fd7f2510d88`  |
| 1363   | No file              | `5fd7f2510d88`  |
| 1360   | No file              | `5fd7f2510d88`  |
| 1358   | No file              | `5fd7f2510d88`  |
| 1355   | No file              | `5fd7f2510d88`  |
| 1351   | No file              | `5fd7f2510d88`  |
| 1348   | No file              | `5fd7f2510d88`  |
| 1346   | No file              | `5fd7f2510d88`  |
| 1341   | No file              | `5fd7f2510d88`  |
| 1340   | No file              | `5fd7f2510d88`  |
| 1338   | No file              | `5fd7f2510d88`  |
| 1335   | No file              | `5fd7f2510d88`  |
| 1333   | No file              | `5fd7f2510d88`  |
| 1329   | No file              | `5fd7f2510d88`  |
| 1327   | No file              | `5fd7f2510d88`  |
| 1324   | No file              | `5fd7f2510d88`  |
| 1321   | No file              | `5fd7f2510d88`  |
| 1319   | No file              | `5fd7f2510d88`  |
| 1318   | No file              | `5fd7f2510d88`  |
| 1316   | No file              | `5fd7f2510d88`  |
| 1313   | No file              | `5fd7f2510d88`  |
| 1311   | No file              | `5fd7f2510d88`  |
| 1309   | No file              | `5fd7f2510d88`  |
| 1304   | No file              | `5fd7f2510d88`  |
| 1292   | No file              | `5fd7f2510d88`  |
| 1286   | No file              | `5fd7f2510d88`  |
| 1280   | No file              | `5fd7f2510d88`  |
| 1276   | No file              | `5fd7f2510d88`  |
| 1267   | No file              | `5fd7f2510d88`  |
| 1261   | No file              | `5fd7f2510d88`  |
| 1256   | No file              | `5fd7f2510d88`  |
| 1250   | No file              | `5fd7f2510d88`  |
| 1246   | No file              | `5fd7f2510d88`  |
| 1239   | No file              | `5fd7f2510d88`  |
| 1230   | No file              | `5fd7f2510d88`  |
| 1226   | No file              | `5fd7f2510d88`  |
| 1220   | No file              | `5fd7f2510d88`  |
| 1217   | No file              | `5fd7f2510d88`  |
| 1211   | No file              | `5fd7f2510d88`  |
| 1210   | No file              | `5fd7f2510d88`  |
| 1208   | No file              | `5fd7f2510d88`  |
| 1203   | No file              | `5fd7f2510d88`  |
| 1197   | No file              | `5fd7f2510d88`  |
| 1194   | No file              | `5fd7f2510d88`  |
| 1192   | No file              | `5fd7f2510d88`  |
| 1187   | No file              | `5fd7f2510d88`  |
| 1183   | No file              | `5fd7f2510d88`  |
| 1177   | No file              | `5fd7f2510d88`  |
| 1173   | No file              | `5fd7f2510d88`  |
| 1167   | No file              | `5fd7f2510d88`  |
| 1164   | No file              | `5fd7f2510d88`  |
| 1156   | No file              | `5fd7f2510d88`  |
| 1149   | No file              | `5fd7f2510d88`  |
| 1144   | No file              | `5fd7f2510d88`  |
| 1137   | No file              | `5fd7f2510d88`  |
| 1132   | No file              | `5fd7f2510d88`  |
| 1127   | No file              | `5fd7f2510d88`  |
| 1122   | No file              | `5fd7f2510d88`  |
| 1118   | No file              | `5fd7f2510d88`  |
| 1114   | No file              | `5fd7f2510d88`  |
| 1109   | No file              | `5fd7f2510d88`  |
| 1102   | No file              | `5fd7f2510d88`  |
| 1096   | No file              | `5fd7f2510d88`  |
| 1088   | No file              | `5fd7f2510d88`  |
| 1081   | No file              | `5fd7f2510d88`  |
| 1076   | No file              | `5fd7f2510d88`  |
| 1069   | No file              | `5fd7f2510d88`  |
| 1064   | No file              | `5fd7f2510d88`  |
| 1058   | No file              | `5fd7f2510d88`  |
| 1051   | No file              | `5fd7f2510d88`  |
| 1044   | No file              | `5fd7f2510d88`  |
| 1036   | No file              | `5fd7f2510d88`  |
| 1026   | No file              | `5fd7f2510d88`  |
| 1016   | No file              | `5fd7f2510d88`  |
| 1009   | No file              | `5fd7f2510d88`  |
| 1005   | No file              | `5fd7f2510d88`  |
| 1000   | No file              | `5fd7f2510d88`  |
| 998    | No file              | `5fd7f2510d88`  |
| 990    | No file              | `5fd7f2510d88`  |
| 979    | No file              | `5fd7f2510d88`  |
| 972    | No file              | `5fd7f2510d88`  |
| 963    | No file              | `5fd7f2510d88`  |
| 955    | No file              | `5fd7f2510d88`  |
| 946    | No file              | `5fd7f2510d88`  |
| 938    | No file              | `5fd7f2510d88`  |
| 927    | No file              | `5fd7f2510d88`  |
| 911    | No file              | `5fd7f2510d88`  |
| 904    | No file              | `5fd7f2510d88`  |
| 899    | No file              | `5fd7f2510d88`  |
| 894    | No file              | `5fd7f2510d88`  |
| 885    | No file              | `5fd7f2510d88`  |
| 879    | No file              | `5fd7f2510d88`  |
| 872    | No file              | `5fd7f2510d88`  |
| 864    | No file              | `5fd7f2510d88`  |
| 855    | No file              | `5fd7f2510d88`  |
| 853    | No file              | `5fd7f2510d88`  |
| 845    | No file              | `5fd7f2510d88`  |
| 837    | No file              | `5fd7f2510d88`  |
| 829    | No file              | `5fd7f2510d88`  |
| 822    | No file              | `5fd7f2510d88`  |
| 814    | No file              | `5fd7f2510d88`  |
| 805    | No file              | `5fd7f2510d88`  |
| 794    | No file              | `5fd7f2510d88`  |
| 787    | No file              | `5fd7f2510d88`  |
| 780    | No file              | `5fd7f2510d88`  |
| 771    | No file              | `5fd7f2510d88`  |
| 760    | No file              | `5fd7f2510d88`  |
| 748    | No file              | `5fd7f2510d88`  |
| 741    | No file              | `5fd7f2510d88`  |
| 736    | No file              | `5fd7f2510d88`  |
| 731    | No file              | `5fd7f2510d88`  |
| 723    | No file              | `5fd7f2510d88`  |
| 711    | No file              | `5fd7f2510d88`  |
| 707    | No file              | `5fd7f2510d88`  |
| 697    | No file              | `5fd7f2510d88`  |
| 689    | No file              | `5fd7f2510d88`  |
| 683    | No file              | `5fd7f2510d88`  |
| 678    | No file              | `5fd7f2510d88`  |
| 670    | No file              | `5fd7f2510d88`  |
| 661    | No file              | `5fd7f2510d88`  |
| 656    | No file              | `5fd7f2510d88`  |
| 652    | No file              | `5fd7f2510d88`  |
| 643    | No file              | `5fd7f2510d88`  |
| 637    | No file              | `5fd7f2510d88`  |
| 630    | No file              | `5fd7f2510d88`  |
| 627    | No file              | `5fd7f2510d88`  |
| 621    | No file              | `5fd7f2510d88`  |
| 617    | No file              | `5fd7f2510d88`  |
| 615    | No file              | `5fd7f2510d88`  |
| 606    | No file              | `5fd7f2510d88`  |
| 599    | No file              | `5fd7f2510d88`  |
| 592    | No file              | `5fd7f2510d88`  |
| 586    | No file              | `5fd7f2510d88`  |
| 577    | No file              | `5fd7f2510d88`  |
| 569    | No file              | `5fd7f2510d88`  |
| 561    | No file              | `5fd7f2510d88`  |
| 554    | No file              | `5fd7f2510d88`  |
| 542    | No file              | `5fd7f2510d88`  |
| 532    | No file              | `5fd7f2510d88`  |
| 531    | No file              | `5fd7f2510d88`  |
| 526    | No file              | `5fd7f2510d88`  |
| 521    | No file              | `5fd7f2510d88`  |
| 517    | No file              | `5fd7f2510d88`  |
| 510    | No file              | `5fd7f2510d88`  |
| 508    | No file              | `5fd7f2510d88`  |
| 504    | No file              | `5fd7f2510d88`  |
| 497    | No file              | `5fd7f2510d88`  |
| 491    | No file              | `5fd7f2510d88`  |
| 485    | No file              | `5fd7f2510d88`  |
| 478    | No file              | `5fd7f2510d88`  |
| 472    | No file              | `5fd7f2510d88`  |
| 466    | No file              | `5fd7f2510d88`  |
| 457    | No file              | `5fd7f2510d88`  |
| 452    | No file              | `5fd7f2510d88`  |
| 449    | No file              | `5fd7f2510d88`  |
| 435    | No file              | `5fd7f2510d88`  |

<!-- versions:end -->

## Companion Files

None. The handler names the regions with their LOC type 17 names from
`languagedata_*.loc` when it is loaded. The sequence stays a path: the
`.paseqfe` sequences under `sequence/` have no handler.

All multi-byte values are little-endian.

## Layout 4

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

## Layout 3

The row has one more flag byte, `unknown_region_keys_0d`, between
`character_swap_sequence` and `force_skip_sequence`.

### Row (variable: 83 bytes + region keys)

| Offset             | Type              | Field                   | Notes                                                    |
| ------------------ | ----------------- | ----------------------- | -------------------------------------------------------- |
| `+0x00`            | u32               | file_name_hash          | As in Layout 4                                           |
| `+0x04`            | u32               | file_name               | As in Layout 4                                           |
| `+0x08`            | u32               | folder                  | As in Layout 4                                           |
| `+0x0C`            | u32               | start_condition         | As in Layout 4                                           |
| `+0x10`            | u32               | start_execute           | As in Layout 4                                           |
| `+0x14`            | u32               | end_execute             | As in Layout 4                                           |
| `+0x18`            | u32               | force_skip_end_execute  | As in Layout 4                                           |
| `+0x1C`            | u32               | skip_condition          | As in Layout 4                                           |
| `+0x20`            | u32               | contents_group_open     | As in Layout 4                                           |
| `+0x24`            | f32[3]            | position                | As in Layout 4                                           |
| `+0x30`            | f32[3]            | resurrect_position      | As in Layout 4                                           |
| `+0x3C`            | u64               | region_count            | As in Layout 4                                           |
| `+0x44`            | u16[region_count] | region_keys             | As in Layout 4                                           |
| `region_keys+0x00` | u32               | file_name_hash_dup      | As in Layout 4                                           |
| `region_keys+0x04` | f32               | radius                  | As in Layout 4                                           |
| `region_keys+0x08` | u8                | use_client_spawn        | As in Layout 4                                           |
| `region_keys+0x09` | u8                | exit_character_select   | As in Layout 4                                           |
| `region_keys+0x0A` | u8                | pre_update_fade_out     | As in Layout 4                                           |
| `region_keys+0x0B` | u8                | party_sequence          | As in Layout 4                                           |
| `region_keys+0x0C` | u8                | character_swap_sequence | As in Layout 4                                           |
| `region_keys+0x0D` | u8                | unknown_region_keys_0d  | `0` on every row of client 3242; see Notes               |
| `region_keys+0x0E` | u8                | force_skip_sequence     | As in Layout 4                                           |

## Layout 2

The row has five flag bytes: no `character_swap_sequence`.

### Row (variable: 81 bytes + region keys)

| Offset             | Type              | Field                   | Notes                                                    |
| ------------------ | ----------------- | ----------------------- | -------------------------------------------------------- |
| `+0x00`            | u32               | file_name_hash          | As in Layout 4                                           |
| `+0x04`            | u32               | file_name               | As in Layout 4                                           |
| `+0x08`            | u32               | folder                  | As in Layout 4                                           |
| `+0x0C`            | u32               | start_condition         | As in Layout 4                                           |
| `+0x10`            | u32               | start_execute           | As in Layout 4                                           |
| `+0x14`            | u32               | end_execute             | As in Layout 4                                           |
| `+0x18`            | u32               | force_skip_end_execute  | As in Layout 4                                           |
| `+0x1C`            | u32               | skip_condition          | As in Layout 4                                           |
| `+0x20`            | u32               | contents_group_open     | As in Layout 4                                           |
| `+0x24`            | f32[3]            | position                | As in Layout 4                                           |
| `+0x30`            | f32[3]            | resurrect_position      | As in Layout 4                                           |
| `+0x3C`            | u64               | region_count            | As in Layout 4                                           |
| `+0x44`            | u16[region_count] | region_keys             | As in Layout 4                                           |
| `region_keys+0x00` | u32               | file_name_hash_dup      | As in Layout 4                                           |
| `region_keys+0x04` | f32               | radius                  | As in Layout 4                                           |
| `region_keys+0x08` | u8                | use_client_spawn        | As in Layout 4                                           |
| `region_keys+0x09` | u8                | exit_character_select   | As in Layout 4                                           |
| `region_keys+0x0A` | u8                | pre_update_fade_out     | As in Layout 4                                           |
| `region_keys+0x0B` | u8                | party_sequence          | As in Layout 4                                           |
| `region_keys+0x0C` | u8                | force_skip_sequence     | As in Layout 4                                           |

## Layout 1

The row has one region key and no `region_count`, and the five flag
bytes of Layout 2.

### Row (75 bytes)

| Offset            | Type   | Field                  | Notes                                                    |
| ----------------- | ------ | ---------------------- | -------------------------------------------------------- |
| `+0x00`           | u32    | file_name_hash         | As in Layout 4                                           |
| `+0x04`           | u32    | file_name              | As in Layout 4                                           |
| `+0x08`           | u32    | folder                 | As in Layout 4                                           |
| `+0x0C`           | u32    | start_condition        | As in Layout 4                                           |
| `+0x10`           | u32    | start_execute          | As in Layout 4                                           |
| `+0x14`           | u32    | end_execute            | As in Layout 4                                           |
| `+0x18`           | u32    | force_skip_end_execute | As in Layout 4                                           |
| `+0x1C`           | u32    | skip_condition         | As in Layout 4                                           |
| `+0x20`           | u32    | contents_group_open    | As in Layout 4                                           |
| `+0x24`           | f32[3] | position               | As in Layout 4                                           |
| `+0x30`           | f32[3] | resurrect_position     | As in Layout 4                                           |
| `+0x3C`           | u16    | region_keys            | The one region of the trigger; no count before it        |
| `+0x3E`           | u32    | file_name_hash_dup     | As in Layout 4                                           |
| `+0x42`           | f32    | radius                 | As in Layout 4                                           |
| `+0x46`           | u8     | use_client_spawn       | As in Layout 4                                           |
| `+0x47`           | u8     | exit_character_select  | As in Layout 4                                           |
| `+0x48`           | u8     | pre_update_fade_out    | As in Layout 4                                           |
| `+0x49`           | u8     | party_sequence         | As in Layout 4                                           |
| `+0x4A`           | u8     | force_skip_sequence    | As in Layout 4                                           |

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
placed by that order alone.

## Notes

- Clients 2171 to 2183 and 2207 to 2695 store rows of another shape,
  which no layout of this doc reads yet: client 2207 has 2 rows of 63
  bytes with six string indexes (no `folder`), one region key and one flag
  byte. The other clients from 2156 to 2203 ship the table empty (row
  count `0`), which every layout reads.
- Client 3242 stores 7 flag bytes (Layout 3). Matched by file name to
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
