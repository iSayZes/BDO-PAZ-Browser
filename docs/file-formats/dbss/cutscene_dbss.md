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

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records           | Row bytes                  |
| ------ | -------------- | --------------------- | ----- | ----------------- | -------------------------- |
| 3      | 1346 and later | `cutscene.dbss`       | 8,882 | 68 Row, 68 Record | 100 to 160, 127 on average |
| 3      | 1346 and later | `cutsceneoffset.dbss` | 820   | 68 Offset Row     | 12                         |
| 2      | 1280 to 1341   | `cutscene.dbss`       | 8,610 | 68 Row            | 100 to 160, 127 on average |
| 2      | 1280 to 1341   | `cutsceneoffset.dbss` | 820   | 68 Offset Row     | 12                         |
| 1      | 1256 to 1276   | `cutscene.dbss`       | 8,338 | 68 Row            | 96 to 156, 123 on average  |
| 1      | 1256 to 1276   | `cutsceneoffset.dbss` | 820   | 68 Offset Row     | 12                         |

| Layout | File                  | Known            | Unknown      |
| ------ | --------------------- | ---------------- | ------------ |
| 3      | `cutscene.dbss`       | 8,610 B (96.9%)  | 272 B (3.1%) |
| 3      | `cutsceneoffset.dbss` | 820 B (100.0%)   | 0 B (0.0%)   |
| 2      | `cutscene.dbss`       | 8,338 B (96.8%)  | 272 B (3.2%) |
| 2      | `cutsceneoffset.dbss` | 820 B (100.0%)   | 0 B (0.0%)   |
| 1      | `cutscene.dbss`       | 8,338 B (100.0%) | 0 B (0.0%)   |
| 1      | `cutsceneoffset.dbss` | 820 B (100.0%)   | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `8fafdf60ab34`  |
| 3482   | Layout 3 | `8fafdf60ab34`  |
| 3474   | Layout 3 | `8fafdf60ab34`  |
| 3473   | Layout 3 | `8fafdf60ab34`  |
| 3464   | Layout 3 | `8fafdf60ab34`  |
| 3458   | Layout 3 | `8fafdf60ab34`  |
| 3454   | Layout 3 | `8fafdf60ab34`  |
| 3444   | Layout 3 | `8fafdf60ab34`  |
| 3435   | Layout 3 | `8fafdf60ab34`  |
| 3426   | Layout 3 | `8fafdf60ab34`  |
| 3418   | Layout 3 | `8fafdf60ab34`  |
| 3412   | Layout 3 | `8fafdf60ab34`  |
| 3402   | Layout 3 | `8fafdf60ab34`  |
| 3396   | Layout 3 | `8fafdf60ab34`  |
| 3387   | Layout 3 | `8fafdf60ab34`  |
| 3381   | Layout 3 | `8fafdf60ab34`  |
| 3373   | Layout 3 | `8fafdf60ab34`  |
| 3364   | Layout 3 | `8fafdf60ab34`  |
| 3356   | Layout 3 | `8fafdf60ab34`  |
| 3349   | Layout 3 | `8fafdf60ab34`  |
| 3342   | Layout 3 | `8fafdf60ab34`  |
| 3335   | Layout 3 | `8fafdf60ab34`  |
| 3326   | Layout 3 | `8fafdf60ab34`  |
| 3321   | Layout 3 | `8fafdf60ab34`  |
| 3314   | Layout 3 | `8fafdf60ab34`  |
| 3303   | Layout 3 | `8fafdf60ab34`  |
| 3302   | Layout 3 | `8fafdf60ab34`  |
| 3293   | Layout 3 | `8fafdf60ab34`  |
| 3283   | Layout 3 | `8fafdf60ab34`  |
| 3275   | Layout 3 | `8fafdf60ab34`  |
| 3267   | Layout 3 | `8fafdf60ab34`  |
| 3258   | Layout 3 | `8fafdf60ab34`  |
| 3251   | Layout 3 | `8fafdf60ab34`  |
| 3242   | Layout 3 | `8fafdf60ab34`  |
| 3235   | Layout 3 | `8fafdf60ab34`  |
| 3229   | Layout 3 | `8fafdf60ab34`  |
| 3212   | Layout 3 | `8fafdf60ab34`  |
| 3203   | Layout 3 | `8fafdf60ab34`  |
| 3193   | Layout 3 | `8fafdf60ab34`  |
| 3186   | Layout 3 | `8fafdf60ab34`  |
| 3177   | Layout 3 | `8fafdf60ab34`  |
| 3169   | Layout 3 | `8fafdf60ab34`  |
| 3158   | Layout 3 | `8fafdf60ab34`  |
| 3151   | Layout 3 | `8fafdf60ab34`  |
| 3144   | Layout 3 | `8fafdf60ab34`  |
| 3133   | Layout 3 | `8fafdf60ab34`  |
| 3125   | Layout 3 | `8fafdf60ab34`  |
| 3118   | Layout 3 | `8fafdf60ab34`  |
| 3111   | Layout 3 | `8fafdf60ab34`  |
| 3103   | Layout 3 | `8fafdf60ab34`  |
| 3095   | Layout 3 | `8fafdf60ab34`  |
| 3086   | Layout 3 | `8fafdf60ab34`  |
| 3072   | Layout 3 | `8fafdf60ab34`  |
| 3062   | Layout 3 | `8fafdf60ab34`  |
| 3052   | Layout 3 | `8fafdf60ab34`  |
| 3045   | Layout 3 | `8fafdf60ab34`  |
| 3037   | Layout 3 | `8fafdf60ab34`  |
| 3030   | Layout 3 | `8fafdf60ab34`  |
| 3021   | Layout 3 | `8fafdf60ab34`  |
| 3012   | Layout 3 | `8fafdf60ab34`  |
| 3002   | Layout 3 | `8fafdf60ab34`  |
| 2995   | Layout 3 | `8fafdf60ab34`  |
| 2987   | Layout 3 | `8fafdf60ab34`  |
| 2978   | Layout 3 | `8fafdf60ab34`  |
| 2970   | Layout 3 | `8fafdf60ab34`  |
| 2959   | Layout 3 | `8fafdf60ab34`  |
| 2951   | Layout 3 | `8fafdf60ab34`  |
| 2942   | Layout 3 | `8fafdf60ab34`  |
| 2935   | Layout 3 | `8fafdf60ab34`  |
| 2932   | Layout 3 | `8fafdf60ab34`  |
| 2923   | Layout 3 | `8fafdf60ab34`  |
| 2919   | Layout 3 | `8fafdf60ab34`  |
| 2907   | Layout 3 | `8fafdf60ab34`  |
| 2900   | Layout 3 | `8fafdf60ab34`  |
| 2891   | Layout 3 | `8fafdf60ab34`  |
| 2882   | Layout 3 | `8fafdf60ab34`  |
| 2872   | Layout 3 | `8fafdf60ab34`  |
| 2863   | Layout 3 | `8fafdf60ab34`  |
| 2855   | Layout 3 | `8fafdf60ab34`  |
| 2849   | Layout 3 | `8fafdf60ab34`  |
| 2844   | Layout 3 | `8fafdf60ab34`  |
| 2834   | Layout 3 | `8fafdf60ab34`  |
| 2825   | Layout 3 | `8fafdf60ab34`  |
| 2819   | Layout 3 | `8fafdf60ab34`  |
| 2811   | Layout 3 | `8fafdf60ab34`  |
| 2803   | Layout 3 | `8fafdf60ab34`  |
| 2794   | Layout 3 | `8fafdf60ab34`  |
| 2783   | Layout 3 | `8fafdf60ab34`  |
| 2774   | Layout 3 | `8fafdf60ab34`  |
| 2765   | Layout 3 | `8fafdf60ab34`  |
| 2756   | Layout 3 | `8fafdf60ab34`  |
| 2750   | Layout 3 | `8fafdf60ab34`  |
| 2743   | Layout 3 | `8fafdf60ab34`  |
| 2736   | Layout 3 | `8fafdf60ab34`  |
| 2726   | Layout 3 | `8fafdf60ab34`  |
| 2717   | Layout 3 | `8fafdf60ab34`  |
| 2709   | Layout 3 | `8fafdf60ab34`  |
| 2703   | Layout 3 | `8fafdf60ab34`  |
| 2695   | Layout 3 | `8fafdf60ab34`  |
| 2684   | Layout 3 | `8fafdf60ab34`  |
| 2672   | Layout 3 | `8fafdf60ab34`  |
| 2665   | Layout 3 | `8fafdf60ab34`  |
| 2657   | Layout 3 | `8fafdf60ab34`  |
| 2649   | Layout 3 | `8fafdf60ab34`  |
| 2644   | Layout 3 | `8fafdf60ab34`  |
| 2637   | Layout 3 | `8fafdf60ab34`  |
| 2629   | Layout 3 | `8fafdf60ab34`  |
| 2619   | Layout 3 | `8fafdf60ab34`  |
| 2612   | Layout 3 | `8fafdf60ab34`  |
| 2606   | Layout 3 | `8fafdf60ab34`  |
| 2602   | Layout 3 | `8fafdf60ab34`  |
| 2601   | Layout 3 | `8fafdf60ab34`  |
| 2592   | Layout 3 | `8fafdf60ab34`  |
| 2583   | Layout 3 | `8fafdf60ab34`  |
| 2575   | Layout 3 | `8fafdf60ab34`  |
| 2567   | Layout 3 | `8fafdf60ab34`  |
| 2560   | Layout 3 | `8fafdf60ab34`  |
| 2553   | Layout 3 | `8fafdf60ab34`  |
| 2545   | Layout 3 | `8fafdf60ab34`  |
| 2538   | Layout 3 | `8fafdf60ab34`  |
| 2529   | Layout 3 | `8fafdf60ab34`  |
| 2519   | Layout 3 | `8fafdf60ab34`  |
| 2513   | Layout 3 | `8fafdf60ab34`  |
| 2510   | Layout 3 | `8fafdf60ab34`  |
| 2507   | Layout 3 | `8fafdf60ab34`  |
| 2503   | Layout 3 | `8fafdf60ab34`  |
| 2498   | Layout 3 | `8fafdf60ab34`  |
| 2492   | Layout 3 | `8fafdf60ab34`  |
| 2487   | Layout 3 | `8fafdf60ab34`  |
| 2480   | Layout 3 | `8fafdf60ab34`  |
| 2474   | Layout 3 | `8fafdf60ab34`  |
| 2468   | Layout 3 | `8fafdf60ab34`  |
| 2460   | Layout 3 | `8fafdf60ab34`  |
| 2453   | Layout 3 | `8fafdf60ab34`  |
| 2444   | Layout 3 | `8fafdf60ab34`  |
| 2438   | Layout 3 | `8fafdf60ab34`  |
| 2434   | Layout 3 | `8fafdf60ab34`  |
| 2429   | Layout 3 | `8fafdf60ab34`  |
| 2421   | Layout 3 | `8fafdf60ab34`  |
| 2414   | Layout 3 | `8fafdf60ab34`  |
| 2407   | Layout 3 | `8fafdf60ab34`  |
| 2401   | Layout 3 | `8fafdf60ab34`  |
| 2397   | Layout 3 | `8fafdf60ab34`  |
| 2393   | Layout 3 | `8fafdf60ab34`  |
| 2384   | Layout 3 | `8fafdf60ab34`  |
| 2378   | Layout 3 | `8fafdf60ab34`  |
| 2372   | Layout 3 | `8fafdf60ab34`  |
| 2358   | Layout 3 | `8fafdf60ab34`  |
| 2352   | Layout 3 | `8fafdf60ab34`  |
| 2347   | Layout 3 | `8fafdf60ab34`  |
| 2343   | Layout 3 | `8fafdf60ab34`  |
| 2335   | Layout 3 | `8fafdf60ab34`  |
| 2327   | Layout 3 | `8fafdf60ab34`  |
| 2324   | Layout 3 | `8fafdf60ab34`  |
| 2319   | Layout 3 | `8fafdf60ab34`  |
| 2313   | Layout 3 | `8fafdf60ab34`  |
| 2308   | Layout 3 | `8fafdf60ab34`  |
| 2302   | Layout 3 | `8fafdf60ab34`  |
| 2295   | Layout 3 | `8fafdf60ab34`  |
| 2290   | Layout 3 | `8fafdf60ab34`  |
| 2284   | Layout 3 | `8fafdf60ab34`  |
| 2276   | Layout 3 | `8fafdf60ab34`  |
| 2269   | Layout 3 | `8fafdf60ab34`  |
| 2259   | Layout 3 | `8fafdf60ab34`  |
| 2250   | Layout 3 | `8fafdf60ab34`  |
| 2243   | Layout 3 | `8fafdf60ab34`  |
| 2235   | Layout 3 | `8fafdf60ab34`  |
| 2229   | Layout 3 | `8fafdf60ab34`  |
| 2224   | Layout 3 | `8fafdf60ab34`  |
| 2218   | Layout 3 | `8fafdf60ab34`  |
| 2215   | Layout 3 | `8fafdf60ab34`  |
| 2207   | Layout 3 | `8fafdf60ab34`  |
| 2203   | Layout 3 | `8fafdf60ab34`  |
| 2196   | Layout 3 | `8fafdf60ab34`  |
| 2192   | Layout 3 | `8fafdf60ab34`  |
| 2189   | Layout 3 | `8fafdf60ab34`  |
| 2183   | Layout 3 | `8fafdf60ab34`  |
| 2179   | Layout 3 | `8fafdf60ab34`  |
| 2171   | Layout 3 | `8fafdf60ab34`  |
| 2163   | Layout 3 | `8fafdf60ab34`  |
| 2156   | Layout 3 | `8fafdf60ab34`  |
| 2151   | Layout 3 | `8fafdf60ab34`  |
| 2147   | Layout 3 | `8fafdf60ab34`  |
| 2142   | Layout 3 | `8fafdf60ab34`  |
| 2138   | Layout 3 | `8fafdf60ab34`  |
| 2134   | Layout 3 | `8fafdf60ab34`  |
| 2130   | Layout 3 | `8fafdf60ab34`  |
| 2122   | Layout 3 | `8fafdf60ab34`  |
| 2107   | Layout 3 | `8fafdf60ab34`  |
| 2098   | Layout 3 | `8fafdf60ab34`  |
| 2089   | Layout 3 | `8fafdf60ab34`  |
| 2081   | Layout 3 | `8fafdf60ab34`  |
| 2073   | Layout 3 | `8fafdf60ab34`  |
| 2067   | Layout 3 | `8fafdf60ab34`  |
| 2063   | Layout 3 | `8fafdf60ab34`  |
| 2059   | Layout 3 | `8fafdf60ab34`  |
| 2052   | Layout 3 | `8fafdf60ab34`  |
| 2044   | Layout 3 | `8fafdf60ab34`  |
| 2039   | Layout 3 | `8fafdf60ab34`  |
| 2032   | Layout 3 | `8fafdf60ab34`  |
| 2025   | Layout 3 | `8fafdf60ab34`  |
| 2011   | Layout 3 | `8fafdf60ab34`  |
| 2005   | Layout 3 | `8fafdf60ab34`  |
| 2000   | Layout 3 | `8fafdf60ab34`  |
| 1996   | Layout 3 | `8fafdf60ab34`  |
| 1991   | Layout 3 | `8fafdf60ab34`  |
| 1985   | Layout 3 | `8fafdf60ab34`  |
| 1980   | Layout 3 | `8fafdf60ab34`  |
| 1969   | Layout 3 | `8fafdf60ab34`  |
| 1964   | Layout 3 | `8fafdf60ab34`  |
| 1958   | Layout 3 | `8fafdf60ab34`  |
| 1950   | Layout 3 | `8fafdf60ab34`  |
| 1945   | Layout 3 | `8fafdf60ab34`  |
| 1937   | Layout 3 | `8fafdf60ab34`  |
| 1933   | Layout 3 | `8fafdf60ab34`  |
| 1927   | Layout 3 | `8fafdf60ab34`  |
| 1921   | Layout 3 | `8fafdf60ab34`  |
| 1914   | Layout 3 | `8fafdf60ab34`  |
| 1908   | Layout 3 | `8fafdf60ab34`  |
| 1897   | Layout 3 | `8fafdf60ab34`  |
| 1892   | Layout 3 | `8fafdf60ab34`  |
| 1886   | Layout 3 | `8fafdf60ab34`  |
| 1881   | Layout 3 | `8fafdf60ab34`  |
| 1871   | Layout 3 | `8fafdf60ab34`  |
| 1866   | Layout 3 | `8fafdf60ab34`  |
| 1862   | Layout 3 | `8fafdf60ab34`  |
| 1854   | Layout 3 | `8fafdf60ab34`  |
| 1846   | Layout 3 | `8fafdf60ab34`  |
| 1838   | Layout 3 | `8fafdf60ab34`  |
| 1832   | Layout 3 | `8fafdf60ab34`  |
| 1826   | Layout 3 | `8fafdf60ab34`  |
| 1822   | Layout 3 | `8fafdf60ab34`  |
| 1818   | Layout 3 | `8fafdf60ab34`  |
| 1804   | Layout 3 | `8fafdf60ab34`  |
| 1794   | Layout 3 | `8fafdf60ab34`  |
| 1790   | Layout 3 | `8fafdf60ab34`  |
| 1784   | Layout 3 | `8fafdf60ab34`  |
| 1774   | Layout 3 | `8fafdf60ab34`  |
| 1771   | Layout 3 | `8fafdf60ab34`  |
| 1762   | Layout 3 | `8fafdf60ab34`  |
| 1759   | Layout 3 | `8fafdf60ab34`  |
| 1754   | Layout 3 | `8fafdf60ab34`  |
| 1749   | Layout 3 | `8fafdf60ab34`  |
| 1743   | Layout 3 | `8fafdf60ab34`  |
| 1737   | Layout 3 | `8fafdf60ab34`  |
| 1731   | Layout 3 | `8fafdf60ab34`  |
| 1725   | Layout 3 | `8fafdf60ab34`  |
| 1717   | Layout 3 | `8fafdf60ab34`  |
| 1710   | Layout 3 | `8fafdf60ab34`  |
| 1704   | Layout 3 | `8fafdf60ab34`  |
| 1698   | Layout 3 | `8fafdf60ab34`  |
| 1690   | Layout 3 | `8fafdf60ab34`  |
| 1685   | Layout 3 | `8fafdf60ab34`  |
| 1680   | Layout 3 | `8fafdf60ab34`  |
| 1674   | Layout 3 | `8fafdf60ab34`  |
| 1668   | Layout 3 | `8fafdf60ab34`  |
| 1659   | Layout 3 | `8fafdf60ab34`  |
| 1649   | Layout 3 | `8fafdf60ab34`  |
| 1642   | Layout 3 | `8fafdf60ab34`  |
| 1636   | Layout 3 | `8fafdf60ab34`  |
| 1628   | Layout 3 | `8fafdf60ab34`  |
| 1622   | Layout 3 | `8fafdf60ab34`  |
| 1614   | Layout 3 | `8fafdf60ab34`  |
| 1608   | Layout 3 | `8fafdf60ab34`  |
| 1602   | Layout 3 | `8fafdf60ab34`  |
| 1598   | Layout 3 | `8fafdf60ab34`  |
| 1594   | Layout 3 | `8fafdf60ab34`  |
| 1590   | Layout 3 | `8fafdf60ab34`  |
| 1587   | Layout 3 | `8fafdf60ab34`  |
| 1584   | Layout 3 | `8fafdf60ab34`  |
| 1579   | Layout 3 | `8fafdf60ab34`  |
| 1572   | Layout 3 | `8fafdf60ab34`  |
| 1565   | Layout 3 | `8fafdf60ab34`  |
| 1559   | Layout 3 | `8fafdf60ab34`  |
| 1554   | Layout 3 | `8fafdf60ab34`  |
| 1547   | Layout 3 | `8fafdf60ab34`  |
| 1537   | Layout 3 | `8fafdf60ab34`  |
| 1529   | Layout 3 | `8fafdf60ab34`  |
| 1524   | Layout 3 | `8fafdf60ab34`  |
| 1519   | Layout 3 | `8fafdf60ab34`  |
| 1509   | Layout 3 | `8fafdf60ab34`  |
| 1506   | Layout 3 | `8fafdf60ab34`  |
| 1504   | Layout 3 | `8fafdf60ab34`  |
| 1500   | Layout 3 | `8fafdf60ab34`  |
| 1493   | Layout 3 | `8fafdf60ab34`  |
| 1489   | Layout 3 | `8fafdf60ab34`  |
| 1485   | Layout 3 | `8fafdf60ab34`  |
| 1481   | Layout 3 | `8fafdf60ab34`  |
| 1474   | Layout 3 | `8fafdf60ab34`  |
| 1466   | Layout 3 | `8fafdf60ab34`  |
| 1462   | Layout 3 | `8fafdf60ab34`  |
| 1459   | Layout 3 | `8fafdf60ab34`  |
| 1453   | Layout 3 | `8fafdf60ab34`  |
| 1450   | Layout 3 | `8fafdf60ab34`  |
| 1445   | Layout 3 | `8fafdf60ab34`  |
| 1439   | Layout 3 | `8fafdf60ab34`  |
| 1433   | Layout 3 | `8fafdf60ab34`  |
| 1430   | Layout 3 | `8fafdf60ab34`  |
| 1426   | Layout 3 | `8fafdf60ab34`  |
| 1421   | Layout 3 | `8fafdf60ab34`  |
| 1417   | Layout 3 | `8fafdf60ab34`  |
| 1416   | Layout 3 | `8fafdf60ab34`  |
| 1409   | Layout 3 | `8fafdf60ab34`  |
| 1405   | Layout 3 | `8fafdf60ab34`  |
| 1401   | Layout 3 | `8fafdf60ab34`  |
| 1396   | Layout 3 | `8fafdf60ab34`  |
| 1391   | Layout 3 | `8fafdf60ab34`  |
| 1390   | Layout 3 | `8fafdf60ab34`  |
| 1386   | Layout 3 | `8fafdf60ab34`  |
| 1381   | Layout 3 | `8fafdf60ab34`  |
| 1379   | Layout 3 | `8fafdf60ab34`  |
| 1372   | Layout 3 | `8fafdf60ab34`  |
| 1366   | Layout 3 | `8fafdf60ab34`  |
| 1364   | Layout 3 | `8fafdf60ab34`  |
| 1363   | Layout 3 | `8fafdf60ab34`  |
| 1360   | Layout 3 | `8fafdf60ab34`  |
| 1358   | Layout 3 | `8fafdf60ab34`  |
| 1355   | Layout 3 | `8fafdf60ab34`  |
| 1351   | Layout 3 | `8fafdf60ab34`  |
| 1348   | Layout 3 | `8fafdf60ab34`  |
| 1346   | Layout 3 | `8fafdf60ab34`  |
| 1341   | Layout 2 | `8fafdf60ab34`  |
| 1340   | Layout 2 | `8fafdf60ab34`  |
| 1338   | Layout 2 | `8fafdf60ab34`  |
| 1335   | Layout 2 | `8fafdf60ab34`  |
| 1333   | Layout 2 | `8fafdf60ab34`  |
| 1329   | Layout 2 | `8fafdf60ab34`  |
| 1327   | Layout 2 | `8fafdf60ab34`  |
| 1324   | Layout 2 | `8fafdf60ab34`  |
| 1321   | Layout 2 | `8fafdf60ab34`  |
| 1319   | Layout 2 | `8fafdf60ab34`  |
| 1318   | Layout 2 | `8fafdf60ab34`  |
| 1316   | Layout 2 | `8fafdf60ab34`  |
| 1313   | Layout 2 | `8fafdf60ab34`  |
| 1311   | Layout 2 | `8fafdf60ab34`  |
| 1309   | Layout 2 | `8fafdf60ab34`  |
| 1304   | Layout 2 | `8fafdf60ab34`  |
| 1292   | Layout 2 | `8fafdf60ab34`  |
| 1286   | Layout 2 | `8fafdf60ab34`  |
| 1280   | Layout 2 | `8fafdf60ab34`  |
| 1276   | Layout 1 | `8fafdf60ab34`  |
| 1267   | Layout 1 | `8fafdf60ab34`  |
| 1261   | Layout 1 | `8fafdf60ab34`  |
| 1256   | Layout 1 | `8fafdf60ab34`  |
| 1250   | No file  | `8fafdf60ab34`  |
| 1246   | No file  | `8fafdf60ab34`  |
| 1239   | No file  | `8fafdf60ab34`  |
| 1230   | No file  | `8fafdf60ab34`  |
| 1226   | No file  | `8fafdf60ab34`  |
| 1220   | No file  | `8fafdf60ab34`  |
| 1217   | No file  | `8fafdf60ab34`  |
| 1211   | No file  | `8fafdf60ab34`  |
| 1210   | No file  | `8fafdf60ab34`  |
| 1208   | No file  | `8fafdf60ab34`  |
| 1203   | No file  | `8fafdf60ab34`  |
| 1197   | No file  | `8fafdf60ab34`  |
| 1194   | No file  | `8fafdf60ab34`  |
| 1192   | No file  | `8fafdf60ab34`  |
| 1187   | No file  | `8fafdf60ab34`  |
| 1183   | No file  | `8fafdf60ab34`  |
| 1177   | No file  | `8fafdf60ab34`  |
| 1173   | No file  | `8fafdf60ab34`  |
| 1167   | No file  | `8fafdf60ab34`  |
| 1164   | No file  | `8fafdf60ab34`  |
| 1156   | No file  | `8fafdf60ab34`  |
| 1149   | No file  | `8fafdf60ab34`  |
| 1144   | No file  | `8fafdf60ab34`  |
| 1137   | No file  | `8fafdf60ab34`  |
| 1132   | No file  | `8fafdf60ab34`  |
| 1127   | No file  | `8fafdf60ab34`  |
| 1122   | No file  | `8fafdf60ab34`  |
| 1118   | No file  | `8fafdf60ab34`  |
| 1114   | No file  | `8fafdf60ab34`  |
| 1109   | No file  | `8fafdf60ab34`  |
| 1102   | No file  | `8fafdf60ab34`  |
| 1096   | No file  | `8fafdf60ab34`  |
| 1088   | No file  | `8fafdf60ab34`  |
| 1081   | No file  | `8fafdf60ab34`  |
| 1076   | No file  | `8fafdf60ab34`  |
| 1069   | No file  | `8fafdf60ab34`  |
| 1064   | No file  | `8fafdf60ab34`  |
| 1058   | No file  | `8fafdf60ab34`  |
| 1051   | No file  | `8fafdf60ab34`  |
| 1044   | No file  | `8fafdf60ab34`  |
| 1036   | No file  | `8fafdf60ab34`  |
| 1026   | No file  | `8fafdf60ab34`  |
| 1016   | No file  | `8fafdf60ab34`  |
| 1009   | No file  | `8fafdf60ab34`  |
| 1005   | No file  | `8fafdf60ab34`  |
| 1000   | No file  | `8fafdf60ab34`  |
| 998    | No file  | `8fafdf60ab34`  |
| 990    | No file  | `8fafdf60ab34`  |
| 979    | No file  | `8fafdf60ab34`  |
| 972    | No file  | `8fafdf60ab34`  |
| 963    | No file  | `8fafdf60ab34`  |
| 955    | No file  | `8fafdf60ab34`  |
| 946    | No file  | `8fafdf60ab34`  |
| 938    | No file  | `8fafdf60ab34`  |
| 927    | No file  | `8fafdf60ab34`  |
| 911    | No file  | `8fafdf60ab34`  |
| 904    | No file  | `8fafdf60ab34`  |
| 899    | No file  | `8fafdf60ab34`  |
| 894    | No file  | `8fafdf60ab34`  |
| 885    | No file  | `8fafdf60ab34`  |
| 879    | No file  | `8fafdf60ab34`  |
| 872    | No file  | `8fafdf60ab34`  |
| 864    | No file  | `8fafdf60ab34`  |
| 855    | No file  | `8fafdf60ab34`  |
| 853    | No file  | `8fafdf60ab34`  |
| 845    | No file  | `8fafdf60ab34`  |
| 837    | No file  | `8fafdf60ab34`  |
| 829    | No file  | `8fafdf60ab34`  |
| 822    | No file  | `8fafdf60ab34`  |
| 814    | No file  | `8fafdf60ab34`  |
| 805    | No file  | `8fafdf60ab34`  |
| 794    | No file  | `8fafdf60ab34`  |
| 787    | No file  | `8fafdf60ab34`  |
| 780    | No file  | `8fafdf60ab34`  |
| 771    | No file  | `8fafdf60ab34`  |
| 760    | No file  | `8fafdf60ab34`  |
| 748    | No file  | `8fafdf60ab34`  |
| 741    | No file  | `8fafdf60ab34`  |
| 736    | No file  | `8fafdf60ab34`  |
| 731    | No file  | `8fafdf60ab34`  |
| 723    | No file  | `8fafdf60ab34`  |
| 711    | No file  | `8fafdf60ab34`  |
| 707    | No file  | `8fafdf60ab34`  |
| 697    | No file  | `8fafdf60ab34`  |
| 689    | No file  | `8fafdf60ab34`  |
| 683    | No file  | `8fafdf60ab34`  |
| 678    | No file  | `8fafdf60ab34`  |
| 670    | No file  | `8fafdf60ab34`  |
| 661    | No file  | `8fafdf60ab34`  |
| 656    | No file  | `8fafdf60ab34`  |
| 652    | No file  | `8fafdf60ab34`  |
| 643    | No file  | `8fafdf60ab34`  |
| 637    | No file  | `8fafdf60ab34`  |
| 630    | No file  | `8fafdf60ab34`  |
| 627    | No file  | `8fafdf60ab34`  |
| 621    | No file  | `8fafdf60ab34`  |
| 617    | No file  | `8fafdf60ab34`  |
| 615    | No file  | `8fafdf60ab34`  |
| 606    | No file  | `8fafdf60ab34`  |
| 599    | No file  | `8fafdf60ab34`  |
| 592    | No file  | `8fafdf60ab34`  |
| 586    | No file  | `8fafdf60ab34`  |
| 577    | No file  | `8fafdf60ab34`  |
| 569    | No file  | `8fafdf60ab34`  |
| 561    | No file  | `8fafdf60ab34`  |
| 554    | No file  | `8fafdf60ab34`  |
| 542    | No file  | `8fafdf60ab34`  |
| 532    | No file  | `8fafdf60ab34`  |
| 531    | No file  | `8fafdf60ab34`  |
| 526    | No file  | `8fafdf60ab34`  |
| 521    | No file  | `8fafdf60ab34`  |
| 517    | No file  | `8fafdf60ab34`  |
| 510    | No file  | `8fafdf60ab34`  |
| 508    | No file  | `8fafdf60ab34`  |
| 504    | No file  | `8fafdf60ab34`  |
| 497    | No file  | `8fafdf60ab34`  |
| 491    | No file  | `8fafdf60ab34`  |
| 485    | No file  | `8fafdf60ab34`  |
| 478    | No file  | `8fafdf60ab34`  |
| 472    | No file  | `8fafdf60ab34`  |
| 466    | No file  | `8fafdf60ab34`  |
| 457    | No file  | `8fafdf60ab34`  |
| 452    | No file  | `8fafdf60ab34`  |
| 449    | No file  | `8fafdf60ab34`  |
| 435    | No file  | `8fafdf60ab34`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `cutsceneoffset.dbss` | Optional | `cutscene_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 3

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

## Layout 2

The rows follow the count with no `key_prefix` in front: the file is the
count and the rows, and `cutsceneoffset.dbss` points at the row start, its
`data_size` the whole row. On client 1341 the file holds 68 cutscenes,
`unknown_description_00` is `0` on every row, and each index row points
at the row with its key. Only the File Layout differs from Layout 3.

### File Layout

| Offset  | Type       | Field | Notes                                    |
| ------- | ---------- | ----- | ---------------------------------------- |
| `+0x00` | u32        | count | Number of cutscenes; `68` on client 1341 |
| `+0x04` | Row[count] | rows  | See Row                                  |

## Layout 1

A row ends after `description_kr`: it has no `unknown_description_00`.
The `data_size` of `cutsceneoffset.dbss` is 4 bytes smaller per row. On
clients 1256 to 1276 the file holds 68 cutscenes, `cutscene_key` is the
`key_hash()` of `file_name` on all 68 rows, and each index row points at
the row with its key. Only the Row differs from Layout 2.

### Row (variable: 28 bytes + texts)

| Offset                  | Type  | Field            | Notes |
| ----------------------- | ----- | ---------------- | ----- |
| `+0x00`                 | u32   | cutscene_key     |       |
| `+0x04`                 | str16 | file_name        |       |
| `file_name+0x00`        | str16 | cutscene_name_kr |       |
| `cutscene_name_kr+0x00` | str16 | description_kr   |       |

## Field Names

The 2016 `gc::CutSceneStaticStatus` has the members `_key` (`u32`),
`_fileName`, `_cutSceneName` and `_description`, the Row of Layout 1;
`unknown_description_00` came with Layout 2 and `key_prefix` with Layout
3. The `CutScene_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `FileName`, `CutSceneName` and `Description`
and 68 rows: all 68 match the client 1784 file, and 67 match client 3482
(one name or place was edited).
