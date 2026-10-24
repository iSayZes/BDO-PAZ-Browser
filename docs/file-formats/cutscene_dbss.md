# `cutscene.dbss` Format

## Purpose

The names of the `.pas` cutscenes: on client 3482 68 cutscenes, by the
region in their file names 29 of Velia (the 12 class prologues among them),
19 of Calpheon, 15 of Serendia, 4 of Obsidian and 1 of Mediah.
Per cutscene the file holds its file name, keyed by the file name's hash,
a Korean name (`도나트의 일지`, `위치 프롤로그`) and the Korean place it plays
in (`글리시 마을 폐허`, `올비아`). The cutscene itself is the `.pas` file;
this table only names it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records           | Row bytes                  |
| ------ | -------------- | ------- | --------------------- | ----- | ----------------- | -------------------------- |
| 1      | 1346 and later | 3483    | `cutscene.dbss`       | 8,882 | 68 Row, 68 Record | 100 to 160, 127 on average |
| 1      | 1346 and later | 3483    | `cutsceneoffset.dbss` | 820   | 68 Offset Row     | 12                         |

| Layout | File                  | Known           | Unknown      |
| ------ | --------------------- | --------------- | ------------ |
| 1      | `cutscene.dbss`       | 8,610 B (96.9%) | 272 B (3.1%) |
| 1      | `cutsceneoffset.dbss` | 820 B (100.0%)  | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `152c8f7f1b82`  |
| 3482   | Layout 1             | `152c8f7f1b82`  |
| 3474   | Layout 1             | `152c8f7f1b82`  |
| 3473   | Layout 1             | `152c8f7f1b82`  |
| 3464   | Layout 1             | `152c8f7f1b82`  |
| 3458   | Layout 1             | `152c8f7f1b82`  |
| 3454   | Layout 1             | `152c8f7f1b82`  |
| 3444   | Layout 1             | `152c8f7f1b82`  |
| 3435   | Layout 1             | `152c8f7f1b82`  |
| 3426   | Layout 1             | `152c8f7f1b82`  |
| 3418   | Layout 1             | `152c8f7f1b82`  |
| 3412   | Layout 1             | `152c8f7f1b82`  |
| 3402   | Layout 1             | `152c8f7f1b82`  |
| 3396   | Layout 1             | `152c8f7f1b82`  |
| 3387   | Layout 1             | `152c8f7f1b82`  |
| 3381   | Layout 1             | `152c8f7f1b82`  |
| 3373   | Layout 1             | `152c8f7f1b82`  |
| 3364   | Layout 1             | `152c8f7f1b82`  |
| 3356   | Layout 1             | `152c8f7f1b82`  |
| 3349   | Layout 1             | `152c8f7f1b82`  |
| 3342   | Layout 1             | `152c8f7f1b82`  |
| 3335   | Layout 1             | `152c8f7f1b82`  |
| 3326   | Layout 1             | `152c8f7f1b82`  |
| 3321   | Layout 1             | `152c8f7f1b82`  |
| 3314   | Layout 1             | `152c8f7f1b82`  |
| 3303   | Layout 1             | `152c8f7f1b82`  |
| 3302   | Layout 1             | `152c8f7f1b82`  |
| 3293   | Layout 1             | `152c8f7f1b82`  |
| 3283   | Layout 1             | `152c8f7f1b82`  |
| 3275   | Layout 1             | `152c8f7f1b82`  |
| 3267   | Layout 1             | `152c8f7f1b82`  |
| 3258   | Layout 1             | `152c8f7f1b82`  |
| 3251   | Layout 1             | `152c8f7f1b82`  |
| 3242   | Layout 1             | `152c8f7f1b82`  |
| 3235   | Layout 1             | `152c8f7f1b82`  |
| 3229   | Layout 1             | `152c8f7f1b82`  |
| 3212   | Layout 1             | `152c8f7f1b82`  |
| 3203   | Layout 1             | `152c8f7f1b82`  |
| 3193   | Layout 1             | `152c8f7f1b82`  |
| 3186   | Layout 1             | `152c8f7f1b82`  |
| 3177   | Layout 1             | `152c8f7f1b82`  |
| 3169   | Layout 1             | `152c8f7f1b82`  |
| 3158   | Layout 1             | `152c8f7f1b82`  |
| 3151   | Layout 1             | `152c8f7f1b82`  |
| 3144   | Layout 1             | `152c8f7f1b82`  |
| 3133   | Layout 1             | `152c8f7f1b82`  |
| 3125   | Layout 1             | `152c8f7f1b82`  |
| 3118   | Layout 1             | `152c8f7f1b82`  |
| 3111   | Layout 1             | `152c8f7f1b82`  |
| 3103   | Layout 1             | `152c8f7f1b82`  |
| 3095   | Layout 1             | `152c8f7f1b82`  |
| 3086   | Layout 1             | `152c8f7f1b82`  |
| 3072   | Layout 1             | `152c8f7f1b82`  |
| 3062   | Layout 1             | `152c8f7f1b82`  |
| 3052   | Layout 1             | `152c8f7f1b82`  |
| 3045   | Layout 1             | `152c8f7f1b82`  |
| 3037   | Layout 1             | `152c8f7f1b82`  |
| 3030   | Layout 1             | `152c8f7f1b82`  |
| 3021   | Layout 1             | `152c8f7f1b82`  |
| 3012   | Layout 1             | `152c8f7f1b82`  |
| 3002   | Layout 1             | `152c8f7f1b82`  |
| 2995   | Layout 1             | `152c8f7f1b82`  |
| 2987   | Layout 1             | `152c8f7f1b82`  |
| 2978   | Layout 1             | `152c8f7f1b82`  |
| 2970   | Layout 1             | `152c8f7f1b82`  |
| 2959   | Layout 1             | `152c8f7f1b82`  |
| 2951   | Layout 1             | `152c8f7f1b82`  |
| 2942   | Layout 1             | `152c8f7f1b82`  |
| 2935   | Layout 1             | `152c8f7f1b82`  |
| 2932   | Layout 1             | `152c8f7f1b82`  |
| 2923   | Layout 1             | `152c8f7f1b82`  |
| 2919   | Layout 1             | `152c8f7f1b82`  |
| 2907   | Layout 1             | `152c8f7f1b82`  |
| 2900   | Layout 1             | `152c8f7f1b82`  |
| 2891   | Layout 1             | `152c8f7f1b82`  |
| 2882   | Layout 1             | `152c8f7f1b82`  |
| 2872   | Layout 1             | `152c8f7f1b82`  |
| 2863   | Layout 1             | `152c8f7f1b82`  |
| 2855   | Layout 1             | `152c8f7f1b82`  |
| 2849   | Layout 1             | `152c8f7f1b82`  |
| 2844   | Layout 1             | `152c8f7f1b82`  |
| 2834   | Layout 1             | `152c8f7f1b82`  |
| 2825   | Layout 1             | `152c8f7f1b82`  |
| 2819   | Layout 1             | `152c8f7f1b82`  |
| 2811   | Layout 1             | `152c8f7f1b82`  |
| 2803   | Layout 1             | `152c8f7f1b82`  |
| 2794   | Layout 1             | `152c8f7f1b82`  |
| 2783   | Layout 1             | `152c8f7f1b82`  |
| 2774   | Layout 1             | `152c8f7f1b82`  |
| 2765   | Layout 1             | `152c8f7f1b82`  |
| 2756   | Layout 1             | `152c8f7f1b82`  |
| 2750   | Layout 1             | `152c8f7f1b82`  |
| 2743   | Layout 1             | `152c8f7f1b82`  |
| 2736   | Layout 1             | `152c8f7f1b82`  |
| 2726   | Layout 1             | `152c8f7f1b82`  |
| 2717   | Layout 1             | `152c8f7f1b82`  |
| 2709   | Layout 1             | `152c8f7f1b82`  |
| 2703   | Layout 1             | `152c8f7f1b82`  |
| 2695   | Layout 1             | `152c8f7f1b82`  |
| 2684   | Layout 1             | `152c8f7f1b82`  |
| 2672   | Layout 1             | `152c8f7f1b82`  |
| 2665   | Layout 1             | `152c8f7f1b82`  |
| 2657   | Layout 1             | `152c8f7f1b82`  |
| 2649   | Layout 1             | `152c8f7f1b82`  |
| 2644   | Layout 1             | `152c8f7f1b82`  |
| 2637   | Layout 1             | `152c8f7f1b82`  |
| 2629   | Layout 1             | `152c8f7f1b82`  |
| 2619   | Layout 1             | `152c8f7f1b82`  |
| 2612   | Layout 1             | `152c8f7f1b82`  |
| 2606   | Layout 1             | `152c8f7f1b82`  |
| 2602   | Layout 1             | `152c8f7f1b82`  |
| 2601   | Layout 1             | `152c8f7f1b82`  |
| 2592   | Layout 1             | `152c8f7f1b82`  |
| 2583   | Layout 1             | `152c8f7f1b82`  |
| 2575   | Layout 1             | `152c8f7f1b82`  |
| 2567   | Layout 1             | `152c8f7f1b82`  |
| 2560   | Layout 1             | `152c8f7f1b82`  |
| 2553   | Layout 1             | `152c8f7f1b82`  |
| 2545   | Layout 1             | `152c8f7f1b82`  |
| 2538   | Layout 1             | `152c8f7f1b82`  |
| 2529   | Layout 1             | `152c8f7f1b82`  |
| 2519   | Layout 1             | `152c8f7f1b82`  |
| 2513   | Layout 1             | `152c8f7f1b82`  |
| 2510   | Layout 1             | `152c8f7f1b82`  |
| 2507   | Layout 1             | `152c8f7f1b82`  |
| 2503   | Layout 1             | `152c8f7f1b82`  |
| 2498   | Layout 1             | `152c8f7f1b82`  |
| 2492   | Layout 1             | `152c8f7f1b82`  |
| 2487   | Layout 1             | `152c8f7f1b82`  |
| 2480   | Layout 1             | `152c8f7f1b82`  |
| 2474   | Layout 1             | `152c8f7f1b82`  |
| 2468   | Layout 1             | `152c8f7f1b82`  |
| 2460   | Layout 1             | `152c8f7f1b82`  |
| 2453   | Layout 1             | `152c8f7f1b82`  |
| 2444   | Layout 1             | `152c8f7f1b82`  |
| 2438   | Layout 1             | `152c8f7f1b82`  |
| 2434   | Layout 1             | `152c8f7f1b82`  |
| 2429   | Layout 1             | `152c8f7f1b82`  |
| 2421   | Layout 1             | `152c8f7f1b82`  |
| 2414   | Layout 1             | `152c8f7f1b82`  |
| 2407   | Layout 1             | `152c8f7f1b82`  |
| 2401   | Layout 1             | `152c8f7f1b82`  |
| 2397   | Layout 1             | `152c8f7f1b82`  |
| 2393   | Layout 1             | `152c8f7f1b82`  |
| 2384   | Layout 1             | `152c8f7f1b82`  |
| 2378   | Layout 1             | `152c8f7f1b82`  |
| 2372   | Layout 1             | `152c8f7f1b82`  |
| 2358   | Layout 1             | `152c8f7f1b82`  |
| 2352   | Layout 1             | `152c8f7f1b82`  |
| 2347   | Layout 1             | `152c8f7f1b82`  |
| 2343   | Layout 1             | `152c8f7f1b82`  |
| 2335   | Layout 1             | `152c8f7f1b82`  |
| 2327   | Layout 1             | `152c8f7f1b82`  |
| 2324   | Layout 1             | `152c8f7f1b82`  |
| 2319   | Layout 1             | `152c8f7f1b82`  |
| 2313   | Layout 1             | `152c8f7f1b82`  |
| 2308   | Layout 1             | `152c8f7f1b82`  |
| 2302   | Layout 1             | `152c8f7f1b82`  |
| 2295   | Layout 1             | `152c8f7f1b82`  |
| 2290   | Layout 1             | `152c8f7f1b82`  |
| 2284   | Layout 1             | `152c8f7f1b82`  |
| 2276   | Layout 1             | `152c8f7f1b82`  |
| 2269   | Layout 1             | `152c8f7f1b82`  |
| 2259   | Layout 1             | `152c8f7f1b82`  |
| 2250   | Layout 1             | `152c8f7f1b82`  |
| 2243   | Layout 1             | `152c8f7f1b82`  |
| 2235   | Layout 1             | `152c8f7f1b82`  |
| 2229   | Layout 1             | `152c8f7f1b82`  |
| 2224   | Layout 1             | `152c8f7f1b82`  |
| 2218   | Layout 1             | `152c8f7f1b82`  |
| 2215   | Layout 1             | `152c8f7f1b82`  |
| 2207   | Layout 1             | `152c8f7f1b82`  |
| 2203   | Layout 1             | `152c8f7f1b82`  |
| 2196   | Layout 1             | `152c8f7f1b82`  |
| 2192   | Layout 1             | `152c8f7f1b82`  |
| 2189   | Layout 1             | `152c8f7f1b82`  |
| 2183   | Layout 1             | `152c8f7f1b82`  |
| 2179   | Layout 1             | `152c8f7f1b82`  |
| 2171   | Layout 1             | `152c8f7f1b82`  |
| 2163   | Layout 1             | `152c8f7f1b82`  |
| 2156   | Layout 1             | `152c8f7f1b82`  |
| 2151   | Layout 1             | `152c8f7f1b82`  |
| 2147   | Layout 1             | `152c8f7f1b82`  |
| 2142   | Layout 1             | `152c8f7f1b82`  |
| 2138   | Layout 1             | `152c8f7f1b82`  |
| 2134   | Layout 1             | `152c8f7f1b82`  |
| 2130   | Layout 1             | `152c8f7f1b82`  |
| 2122   | Layout 1             | `152c8f7f1b82`  |
| 2107   | Layout 1             | `152c8f7f1b82`  |
| 2098   | Layout 1             | `152c8f7f1b82`  |
| 2089   | Layout 1             | `152c8f7f1b82`  |
| 2081   | Layout 1             | `152c8f7f1b82`  |
| 2073   | Layout 1             | `152c8f7f1b82`  |
| 2067   | Layout 1             | `152c8f7f1b82`  |
| 2063   | Layout 1             | `152c8f7f1b82`  |
| 2059   | Layout 1             | `152c8f7f1b82`  |
| 2052   | Layout 1             | `152c8f7f1b82`  |
| 2044   | Layout 1             | `152c8f7f1b82`  |
| 2039   | Layout 1             | `152c8f7f1b82`  |
| 2032   | Layout 1             | `152c8f7f1b82`  |
| 2025   | Layout 1             | `152c8f7f1b82`  |
| 2011   | Layout 1             | `152c8f7f1b82`  |
| 2005   | Layout 1             | `152c8f7f1b82`  |
| 2000   | Layout 1             | `152c8f7f1b82`  |
| 1996   | Layout 1             | `152c8f7f1b82`  |
| 1991   | Layout 1             | `152c8f7f1b82`  |
| 1985   | Layout 1             | `152c8f7f1b82`  |
| 1980   | Layout 1             | `152c8f7f1b82`  |
| 1969   | Layout 1             | `152c8f7f1b82`  |
| 1964   | Layout 1             | `152c8f7f1b82`  |
| 1958   | Layout 1             | `152c8f7f1b82`  |
| 1950   | Layout 1             | `152c8f7f1b82`  |
| 1945   | Layout 1             | `152c8f7f1b82`  |
| 1937   | Layout 1             | `152c8f7f1b82`  |
| 1933   | Layout 1             | `152c8f7f1b82`  |
| 1927   | Layout 1             | `152c8f7f1b82`  |
| 1921   | Layout 1             | `152c8f7f1b82`  |
| 1914   | Layout 1             | `152c8f7f1b82`  |
| 1908   | Layout 1             | `152c8f7f1b82`  |
| 1897   | Layout 1             | `152c8f7f1b82`  |
| 1892   | Layout 1             | `152c8f7f1b82`  |
| 1886   | Layout 1             | `152c8f7f1b82`  |
| 1881   | Layout 1             | `152c8f7f1b82`  |
| 1871   | Layout 1             | `152c8f7f1b82`  |
| 1866   | Layout 1             | `152c8f7f1b82`  |
| 1862   | Layout 1             | `152c8f7f1b82`  |
| 1854   | Layout 1             | `152c8f7f1b82`  |
| 1846   | Layout 1             | `152c8f7f1b82`  |
| 1838   | Layout 1             | `152c8f7f1b82`  |
| 1832   | Layout 1             | `152c8f7f1b82`  |
| 1826   | Layout 1             | `152c8f7f1b82`  |
| 1822   | Layout 1             | `152c8f7f1b82`  |
| 1818   | Layout 1             | `152c8f7f1b82`  |
| 1804   | Layout 1             | `152c8f7f1b82`  |
| 1794   | Layout 1             | `152c8f7f1b82`  |
| 1790   | Layout 1             | `152c8f7f1b82`  |
| 1784   | Layout 1             | `152c8f7f1b82`  |
| 1774   | Layout 1             | `152c8f7f1b82`  |
| 1771   | Layout 1             | `152c8f7f1b82`  |
| 1762   | Layout 1             | `152c8f7f1b82`  |
| 1759   | Layout 1             | `152c8f7f1b82`  |
| 1754   | Layout 1             | `152c8f7f1b82`  |
| 1749   | Layout 1             | `152c8f7f1b82`  |
| 1743   | Layout 1             | `152c8f7f1b82`  |
| 1737   | Layout 1             | `152c8f7f1b82`  |
| 1731   | Layout 1             | `152c8f7f1b82`  |
| 1725   | Layout 1             | `152c8f7f1b82`  |
| 1717   | Layout 1             | `152c8f7f1b82`  |
| 1710   | Layout 1             | `152c8f7f1b82`  |
| 1704   | Layout 1             | `152c8f7f1b82`  |
| 1698   | Layout 1             | `152c8f7f1b82`  |
| 1690   | Layout 1             | `152c8f7f1b82`  |
| 1685   | Layout 1             | `152c8f7f1b82`  |
| 1680   | Layout 1             | `152c8f7f1b82`  |
| 1674   | Layout 1             | `152c8f7f1b82`  |
| 1668   | Layout 1             | `152c8f7f1b82`  |
| 1659   | Layout 1             | `152c8f7f1b82`  |
| 1649   | Layout 1             | `152c8f7f1b82`  |
| 1642   | Layout 1             | `152c8f7f1b82`  |
| 1636   | Layout 1             | `152c8f7f1b82`  |
| 1628   | Layout 1             | `152c8f7f1b82`  |
| 1622   | Layout 1             | `152c8f7f1b82`  |
| 1614   | Layout 1             | `152c8f7f1b82`  |
| 1608   | Layout 1             | `152c8f7f1b82`  |
| 1602   | Layout 1             | `152c8f7f1b82`  |
| 1598   | Layout 1             | `152c8f7f1b82`  |
| 1594   | Layout 1             | `152c8f7f1b82`  |
| 1590   | Layout 1             | `152c8f7f1b82`  |
| 1587   | Layout 1             | `152c8f7f1b82`  |
| 1584   | Layout 1             | `152c8f7f1b82`  |
| 1579   | Layout 1             | `152c8f7f1b82`  |
| 1572   | Layout 1             | `152c8f7f1b82`  |
| 1565   | Layout 1             | `152c8f7f1b82`  |
| 1559   | Layout 1             | `152c8f7f1b82`  |
| 1554   | Layout 1             | `152c8f7f1b82`  |
| 1547   | Layout 1             | `152c8f7f1b82`  |
| 1537   | Layout 1             | `152c8f7f1b82`  |
| 1529   | Layout 1             | `152c8f7f1b82`  |
| 1524   | Layout 1             | `152c8f7f1b82`  |
| 1519   | Layout 1             | `152c8f7f1b82`  |
| 1509   | Layout 1             | `152c8f7f1b82`  |
| 1506   | Layout 1             | `152c8f7f1b82`  |
| 1504   | Layout 1             | `152c8f7f1b82`  |
| 1500   | Layout 1             | `152c8f7f1b82`  |
| 1493   | Layout 1             | `152c8f7f1b82`  |
| 1489   | Layout 1             | `152c8f7f1b82`  |
| 1485   | Layout 1             | `152c8f7f1b82`  |
| 1481   | Layout 1             | `152c8f7f1b82`  |
| 1474   | Layout 1             | `152c8f7f1b82`  |
| 1466   | Layout 1             | `152c8f7f1b82`  |
| 1462   | Layout 1             | `152c8f7f1b82`  |
| 1459   | Layout 1             | `152c8f7f1b82`  |
| 1453   | Layout 1             | `152c8f7f1b82`  |
| 1450   | Layout 1             | `152c8f7f1b82`  |
| 1445   | Layout 1             | `152c8f7f1b82`  |
| 1439   | Layout 1             | `152c8f7f1b82`  |
| 1433   | Layout 1             | `152c8f7f1b82`  |
| 1430   | Layout 1             | `152c8f7f1b82`  |
| 1426   | Layout 1             | `152c8f7f1b82`  |
| 1421   | Layout 1             | `152c8f7f1b82`  |
| 1417   | Layout 1             | `152c8f7f1b82`  |
| 1416   | Layout 1             | `152c8f7f1b82`  |
| 1409   | Layout 1             | `152c8f7f1b82`  |
| 1405   | Layout 1             | `152c8f7f1b82`  |
| 1401   | Layout 1             | `152c8f7f1b82`  |
| 1396   | Layout 1             | `152c8f7f1b82`  |
| 1391   | Layout 1             | `152c8f7f1b82`  |
| 1390   | Layout 1             | `152c8f7f1b82`  |
| 1386   | Layout 1             | `152c8f7f1b82`  |
| 1381   | Layout 1             | `152c8f7f1b82`  |
| 1379   | Layout 1             | `152c8f7f1b82`  |
| 1372   | Layout 1             | `152c8f7f1b82`  |
| 1366   | Layout 1             | `152c8f7f1b82`  |
| 1364   | Layout 1             | `152c8f7f1b82`  |
| 1363   | Layout 1             | `152c8f7f1b82`  |
| 1360   | Layout 1             | `152c8f7f1b82`  |
| 1358   | Layout 1             | `152c8f7f1b82`  |
| 1355   | Layout 1             | `152c8f7f1b82`  |
| 1351   | Layout 1             | `152c8f7f1b82`  |
| 1348   | Layout 1             | `152c8f7f1b82`  |
| 1346   | Layout 1             | `152c8f7f1b82`  |
| 1341   | No documented layout | `152c8f7f1b82`  |
| 1340   | No documented layout | `152c8f7f1b82`  |
| 1338   | No documented layout | `152c8f7f1b82`  |
| 1335   | No documented layout | `152c8f7f1b82`  |
| 1333   | No documented layout | `152c8f7f1b82`  |
| 1329   | No documented layout | `152c8f7f1b82`  |
| 1327   | No documented layout | `152c8f7f1b82`  |
| 1324   | No documented layout | `152c8f7f1b82`  |
| 1321   | No documented layout | `152c8f7f1b82`  |
| 1319   | No documented layout | `152c8f7f1b82`  |
| 1318   | No documented layout | `152c8f7f1b82`  |
| 1316   | No documented layout | `152c8f7f1b82`  |
| 1313   | No documented layout | `152c8f7f1b82`  |
| 1311   | No documented layout | `152c8f7f1b82`  |
| 1309   | No documented layout | `152c8f7f1b82`  |
| 1304   | No documented layout | `152c8f7f1b82`  |
| 1292   | No documented layout | `152c8f7f1b82`  |
| 1286   | No documented layout | `152c8f7f1b82`  |
| 1280   | No documented layout | `152c8f7f1b82`  |
| 1276   | No documented layout | `152c8f7f1b82`  |
| 1267   | No documented layout | `152c8f7f1b82`  |
| 1261   | No documented layout | `152c8f7f1b82`  |
| 1256   | No documented layout | `152c8f7f1b82`  |
| 1250   | No file              | `152c8f7f1b82`  |
| 1246   | No file              | `152c8f7f1b82`  |
| 1239   | No file              | `152c8f7f1b82`  |
| 1230   | No file              | `152c8f7f1b82`  |
| 1226   | No file              | `152c8f7f1b82`  |
| 1220   | No file              | `152c8f7f1b82`  |
| 1217   | No file              | `152c8f7f1b82`  |
| 1211   | No file              | `152c8f7f1b82`  |
| 1210   | No file              | `152c8f7f1b82`  |
| 1208   | No file              | `152c8f7f1b82`  |
| 1203   | No file              | `152c8f7f1b82`  |
| 1197   | No file              | `152c8f7f1b82`  |
| 1194   | No file              | `152c8f7f1b82`  |
| 1192   | No file              | `152c8f7f1b82`  |
| 1187   | No file              | `152c8f7f1b82`  |
| 1183   | No file              | `152c8f7f1b82`  |
| 1177   | No file              | `152c8f7f1b82`  |
| 1173   | No file              | `152c8f7f1b82`  |
| 1167   | No file              | `152c8f7f1b82`  |
| 1164   | No file              | `152c8f7f1b82`  |
| 1156   | No file              | `152c8f7f1b82`  |
| 1149   | No file              | `152c8f7f1b82`  |
| 1144   | No file              | `152c8f7f1b82`  |
| 1137   | No file              | `152c8f7f1b82`  |
| 1132   | No file              | `152c8f7f1b82`  |
| 1127   | No file              | `152c8f7f1b82`  |
| 1122   | No file              | `152c8f7f1b82`  |
| 1118   | No file              | `152c8f7f1b82`  |
| 1114   | No file              | `152c8f7f1b82`  |
| 1109   | No file              | `152c8f7f1b82`  |
| 1102   | No file              | `152c8f7f1b82`  |
| 1096   | No file              | `152c8f7f1b82`  |
| 1088   | No file              | `152c8f7f1b82`  |
| 1081   | No file              | `152c8f7f1b82`  |
| 1076   | No file              | `152c8f7f1b82`  |
| 1069   | No file              | `152c8f7f1b82`  |
| 1064   | No file              | `152c8f7f1b82`  |
| 1058   | No file              | `152c8f7f1b82`  |
| 1051   | No file              | `152c8f7f1b82`  |
| 1044   | No file              | `152c8f7f1b82`  |
| 1036   | No file              | `152c8f7f1b82`  |
| 1026   | No file              | `152c8f7f1b82`  |
| 1016   | No file              | `152c8f7f1b82`  |
| 1009   | No file              | `152c8f7f1b82`  |
| 1005   | No file              | `152c8f7f1b82`  |
| 1000   | No file              | `152c8f7f1b82`  |
| 998    | No file              | `152c8f7f1b82`  |
| 990    | No file              | `152c8f7f1b82`  |
| 979    | No file              | `152c8f7f1b82`  |
| 972    | No file              | `152c8f7f1b82`  |
| 963    | No file              | `152c8f7f1b82`  |
| 955    | No file              | `152c8f7f1b82`  |
| 946    | No file              | `152c8f7f1b82`  |
| 938    | No file              | `152c8f7f1b82`  |
| 927    | No file              | `152c8f7f1b82`  |
| 911    | No file              | `152c8f7f1b82`  |
| 904    | No file              | `152c8f7f1b82`  |
| 899    | No file              | `152c8f7f1b82`  |
| 894    | No file              | `152c8f7f1b82`  |
| 885    | No file              | `152c8f7f1b82`  |
| 879    | No file              | `152c8f7f1b82`  |
| 872    | No file              | `152c8f7f1b82`  |
| 864    | No file              | `152c8f7f1b82`  |
| 855    | No file              | `152c8f7f1b82`  |
| 853    | No file              | `152c8f7f1b82`  |
| 845    | No file              | `152c8f7f1b82`  |
| 837    | No file              | `152c8f7f1b82`  |
| 829    | No file              | `152c8f7f1b82`  |
| 822    | No file              | `152c8f7f1b82`  |
| 814    | No file              | `152c8f7f1b82`  |
| 805    | No file              | `152c8f7f1b82`  |
| 794    | No file              | `152c8f7f1b82`  |
| 787    | No file              | `152c8f7f1b82`  |
| 780    | No file              | `152c8f7f1b82`  |
| 771    | No file              | `152c8f7f1b82`  |
| 760    | No file              | `152c8f7f1b82`  |
| 748    | No file              | `152c8f7f1b82`  |
| 741    | No file              | `152c8f7f1b82`  |
| 736    | No file              | `152c8f7f1b82`  |
| 731    | No file              | `152c8f7f1b82`  |
| 723    | No file              | `152c8f7f1b82`  |
| 711    | No file              | `152c8f7f1b82`  |
| 707    | No file              | `152c8f7f1b82`  |
| 697    | No file              | `152c8f7f1b82`  |
| 689    | No file              | `152c8f7f1b82`  |
| 683    | No file              | `152c8f7f1b82`  |
| 678    | No file              | `152c8f7f1b82`  |
| 670    | No file              | `152c8f7f1b82`  |
| 661    | No file              | `152c8f7f1b82`  |
| 656    | No file              | `152c8f7f1b82`  |
| 652    | No file              | `152c8f7f1b82`  |
| 643    | No file              | `152c8f7f1b82`  |
| 637    | No file              | `152c8f7f1b82`  |
| 630    | No file              | `152c8f7f1b82`  |
| 627    | No file              | `152c8f7f1b82`  |
| 621    | No file              | `152c8f7f1b82`  |
| 617    | No file              | `152c8f7f1b82`  |
| 615    | No file              | `152c8f7f1b82`  |
| 606    | No file              | `152c8f7f1b82`  |
| 599    | No file              | `152c8f7f1b82`  |
| 592    | No file              | `152c8f7f1b82`  |
| 586    | No file              | `152c8f7f1b82`  |
| 577    | No file              | `152c8f7f1b82`  |
| 569    | No file              | `152c8f7f1b82`  |
| 561    | No file              | `152c8f7f1b82`  |
| 554    | No file              | `152c8f7f1b82`  |
| 542    | No file              | `152c8f7f1b82`  |
| 532    | No file              | `152c8f7f1b82`  |
| 531    | No file              | `152c8f7f1b82`  |
| 526    | No file              | `152c8f7f1b82`  |
| 521    | No file              | `152c8f7f1b82`  |
| 517    | No file              | `152c8f7f1b82`  |
| 510    | No file              | `152c8f7f1b82`  |
| 508    | No file              | `152c8f7f1b82`  |
| 504    | No file              | `152c8f7f1b82`  |
| 497    | No file              | `152c8f7f1b82`  |
| 491    | No file              | `152c8f7f1b82`  |
| 485    | No file              | `152c8f7f1b82`  |
| 478    | No file              | `152c8f7f1b82`  |
| 472    | No file              | `152c8f7f1b82`  |
| 466    | No file              | `152c8f7f1b82`  |
| 457    | No file              | `152c8f7f1b82`  |
| 452    | No file              | `152c8f7f1b82`  |
| 449    | No file              | `152c8f7f1b82`  |
| 435    | No file              | `152c8f7f1b82`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `cutsceneoffset.dbss` | Optional | `cutscene_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then the records back
to back; the file ends after the last record.

| Offset  | Type          | Field   | Notes                                    |
| ------- | ------------- | ------- | ---------------------------------------- |
| `+0x00` | u32           | count   | Number of cutscenes; `68` on client 3482 |
| `+0x04` | Record[count] | records | See Record                               |

### Record (variable: 4 bytes + row)

| Offset  | Type | Field      | Notes                                       |
| ------- | ---- | ---------- | ------------------------------------------- |
| `+0x00` | u32  | key_prefix | Equals `cutscene_key`                       |
| `+0x04` | Row  | row        | The offset row points at this field         |

### Row (variable: 32 bytes + texts)

| Offset                | Type  | Field                  | Notes |
| --------------------- | ----- | ---------------------- | ----- |
| `+0x00`               | u32   | cutscene_key           | `key_hash()` of `file_name` (lookup3 over the UTF-16LE text, seed `0xC5EDE`) on 68 of 68 rows |
| `+0x04`               | str16 | file_name              | Cutscene file name (`CS_Serendia_01_Diary_0001.pas`); every name starts with `CS_` |
| `file_name+0x00`      | str16 | cutscene_name_kr       | Korean cutscene name |
| `cutscene_name_kr+0x00` | str16 | description_kr       | Korean place name; `올비아` on 18 rows |
| `description_kr+0x00` | u32   | unknown_description_00 | `0` on every row of clients 1784 and 3482 |

### `cutsceneoffset.dbss`

Bare offset table into `cutscene.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                              |
| ------- | ----------------- | ----- | ---------------------------------- |
| `+0x00` | u32               | count | Equals the `cutscene.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                     |

### Offset Row (12 bytes)

| Offset  | Type | Field        | Notes                                                                     |
| ------- | ---- | ------------ | ------------------------------------------------------------------------- |
| `+0x00` | u32  | cutscene_key | Key of the record it points at                                            |
| `+0x04` | u32  | data_offset  | Absolute offset in `cutscene.dbss` of the row, past the key prefix         |
| `+0x08` | u32  | data_size    | Row size in bytes, without the key prefix                                 |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are not in file order; on clients 1784 and 3482 every one
points at the row with its key.

## Field Names

The 2016 `gc::CutSceneStaticStatus` has the members `_key` (`u32`),
`_fileName`, `_cutSceneName` and `_description`; `unknown_description_00`
is newer. The `CutScene_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `FileName`,
`CutSceneName` and `Description` and 68 rows: all 68 match the client 1784
file, and 67 match client 3482 (one name or place was edited).
