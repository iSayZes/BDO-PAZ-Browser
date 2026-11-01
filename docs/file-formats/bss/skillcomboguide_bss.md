# `skillcomboguide.bss` Format

## Purpose

The skill combos of the combo guide, per class: each combo is a chain of
two to seven skills with the key binding text of every step. The first
combo of client 3482 is Hashashin skill 5534 (`MoveBack` + `Kick`), then
5501 (`Attack1`), then 5524 (`Dash` + `Attack2`). The skill command widget
shows the learned combos of the current class above the skill command
list.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes  | Records                                | Row bytes |
| ------ | -------------- | --------------------- | ------ | -------------------------------------- | --------- |
| 1      | 1421 and later | `skillcomboguide.bss` | 18,240 | 1,072 Step, 321 Combo, 26 Class Combos | 6         |

| Layout | File                  | Known             | Unknown    |
| ------ | --------------------- | ----------------- | ---------- |
| 1      | `skillcomboguide.bss` | 18,240 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `5e07d6695c80`  |
| 3482   | Layout 1 | `5e07d6695c80`  |
| 3474   | Layout 1 | `5e07d6695c80`  |
| 3473   | Layout 1 | `5e07d6695c80`  |
| 3464   | Layout 1 | `5e07d6695c80`  |
| 3458   | Layout 1 | `5e07d6695c80`  |
| 3454   | Layout 1 | `5e07d6695c80`  |
| 3444   | Layout 1 | `5e07d6695c80`  |
| 3435   | Layout 1 | `5e07d6695c80`  |
| 3426   | Layout 1 | `5e07d6695c80`  |
| 3418   | Layout 1 | `5e07d6695c80`  |
| 3412   | Layout 1 | `5e07d6695c80`  |
| 3402   | Layout 1 | `5e07d6695c80`  |
| 3396   | Layout 1 | `5e07d6695c80`  |
| 3387   | Layout 1 | `5e07d6695c80`  |
| 3381   | Layout 1 | `5e07d6695c80`  |
| 3373   | Layout 1 | `5e07d6695c80`  |
| 3364   | Layout 1 | `5e07d6695c80`  |
| 3356   | Layout 1 | `5e07d6695c80`  |
| 3349   | Layout 1 | `5e07d6695c80`  |
| 3342   | Layout 1 | `5e07d6695c80`  |
| 3335   | Layout 1 | `5e07d6695c80`  |
| 3326   | Layout 1 | `5e07d6695c80`  |
| 3321   | Layout 1 | `5e07d6695c80`  |
| 3314   | Layout 1 | `5e07d6695c80`  |
| 3303   | Layout 1 | `5e07d6695c80`  |
| 3302   | Layout 1 | `5e07d6695c80`  |
| 3293   | Layout 1 | `5e07d6695c80`  |
| 3283   | Layout 1 | `5e07d6695c80`  |
| 3275   | Layout 1 | `5e07d6695c80`  |
| 3267   | Layout 1 | `5e07d6695c80`  |
| 3258   | Layout 1 | `5e07d6695c80`  |
| 3251   | Layout 1 | `5e07d6695c80`  |
| 3242   | Layout 1 | `5e07d6695c80`  |
| 3235   | Layout 1 | `5e07d6695c80`  |
| 3229   | Layout 1 | `5e07d6695c80`  |
| 3212   | Layout 1 | `5e07d6695c80`  |
| 3203   | Layout 1 | `5e07d6695c80`  |
| 3193   | Layout 1 | `5e07d6695c80`  |
| 3186   | Layout 1 | `5e07d6695c80`  |
| 3177   | Layout 1 | `5e07d6695c80`  |
| 3169   | Layout 1 | `5e07d6695c80`  |
| 3158   | Layout 1 | `5e07d6695c80`  |
| 3151   | Layout 1 | `5e07d6695c80`  |
| 3144   | Layout 1 | `5e07d6695c80`  |
| 3133   | Layout 1 | `5e07d6695c80`  |
| 3125   | Layout 1 | `5e07d6695c80`  |
| 3118   | Layout 1 | `5e07d6695c80`  |
| 3111   | Layout 1 | `5e07d6695c80`  |
| 3103   | Layout 1 | `5e07d6695c80`  |
| 3095   | Layout 1 | `5e07d6695c80`  |
| 3086   | Layout 1 | `5e07d6695c80`  |
| 3072   | Layout 1 | `5e07d6695c80`  |
| 3062   | Layout 1 | `5e07d6695c80`  |
| 3052   | Layout 1 | `5e07d6695c80`  |
| 3045   | Layout 1 | `5e07d6695c80`  |
| 3037   | Layout 1 | `5e07d6695c80`  |
| 3030   | Layout 1 | `5e07d6695c80`  |
| 3021   | Layout 1 | `5e07d6695c80`  |
| 3012   | Layout 1 | `5e07d6695c80`  |
| 3002   | Layout 1 | `5e07d6695c80`  |
| 2995   | Layout 1 | `5e07d6695c80`  |
| 2987   | Layout 1 | `5e07d6695c80`  |
| 2978   | Layout 1 | `5e07d6695c80`  |
| 2970   | Layout 1 | `5e07d6695c80`  |
| 2959   | Layout 1 | `5e07d6695c80`  |
| 2951   | Layout 1 | `5e07d6695c80`  |
| 2942   | Layout 1 | `5e07d6695c80`  |
| 2935   | Layout 1 | `5e07d6695c80`  |
| 2932   | Layout 1 | `5e07d6695c80`  |
| 2923   | Layout 1 | `5e07d6695c80`  |
| 2919   | Layout 1 | `5e07d6695c80`  |
| 2907   | Layout 1 | `5e07d6695c80`  |
| 2900   | Layout 1 | `5e07d6695c80`  |
| 2891   | Layout 1 | `5e07d6695c80`  |
| 2882   | Layout 1 | `5e07d6695c80`  |
| 2872   | Layout 1 | `5e07d6695c80`  |
| 2863   | Layout 1 | `5e07d6695c80`  |
| 2855   | Layout 1 | `5e07d6695c80`  |
| 2849   | Layout 1 | `5e07d6695c80`  |
| 2844   | Layout 1 | `5e07d6695c80`  |
| 2834   | Layout 1 | `5e07d6695c80`  |
| 2825   | Layout 1 | `5e07d6695c80`  |
| 2819   | Layout 1 | `5e07d6695c80`  |
| 2811   | Layout 1 | `5e07d6695c80`  |
| 2803   | Layout 1 | `5e07d6695c80`  |
| 2794   | Layout 1 | `5e07d6695c80`  |
| 2783   | Layout 1 | `5e07d6695c80`  |
| 2774   | Layout 1 | `5e07d6695c80`  |
| 2765   | Layout 1 | `5e07d6695c80`  |
| 2756   | Layout 1 | `5e07d6695c80`  |
| 2750   | Layout 1 | `5e07d6695c80`  |
| 2743   | Layout 1 | `5e07d6695c80`  |
| 2736   | Layout 1 | `5e07d6695c80`  |
| 2726   | Layout 1 | `5e07d6695c80`  |
| 2717   | Layout 1 | `5e07d6695c80`  |
| 2709   | Layout 1 | `5e07d6695c80`  |
| 2703   | Layout 1 | `5e07d6695c80`  |
| 2695   | Layout 1 | `5e07d6695c80`  |
| 2684   | Layout 1 | `5e07d6695c80`  |
| 2672   | Layout 1 | `5e07d6695c80`  |
| 2665   | Layout 1 | `5e07d6695c80`  |
| 2657   | Layout 1 | `5e07d6695c80`  |
| 2649   | Layout 1 | `5e07d6695c80`  |
| 2644   | Layout 1 | `5e07d6695c80`  |
| 2637   | Layout 1 | `5e07d6695c80`  |
| 2629   | Layout 1 | `5e07d6695c80`  |
| 2619   | Layout 1 | `5e07d6695c80`  |
| 2612   | Layout 1 | `5e07d6695c80`  |
| 2606   | Layout 1 | `5e07d6695c80`  |
| 2602   | Layout 1 | `5e07d6695c80`  |
| 2601   | Layout 1 | `5e07d6695c80`  |
| 2592   | Layout 1 | `5e07d6695c80`  |
| 2583   | Layout 1 | `5e07d6695c80`  |
| 2575   | Layout 1 | `5e07d6695c80`  |
| 2567   | Layout 1 | `5e07d6695c80`  |
| 2560   | Layout 1 | `5e07d6695c80`  |
| 2553   | Layout 1 | `5e07d6695c80`  |
| 2545   | Layout 1 | `5e07d6695c80`  |
| 2538   | Layout 1 | `5e07d6695c80`  |
| 2529   | Layout 1 | `5e07d6695c80`  |
| 2519   | Layout 1 | `5e07d6695c80`  |
| 2513   | Layout 1 | `5e07d6695c80`  |
| 2510   | Layout 1 | `5e07d6695c80`  |
| 2507   | Layout 1 | `5e07d6695c80`  |
| 2503   | Layout 1 | `5e07d6695c80`  |
| 2498   | Layout 1 | `5e07d6695c80`  |
| 2492   | Layout 1 | `5e07d6695c80`  |
| 2487   | Layout 1 | `5e07d6695c80`  |
| 2480   | Layout 1 | `5e07d6695c80`  |
| 2474   | Layout 1 | `5e07d6695c80`  |
| 2468   | Layout 1 | `5e07d6695c80`  |
| 2460   | Layout 1 | `5e07d6695c80`  |
| 2453   | Layout 1 | `5e07d6695c80`  |
| 2444   | Layout 1 | `5e07d6695c80`  |
| 2438   | Layout 1 | `5e07d6695c80`  |
| 2434   | Layout 1 | `5e07d6695c80`  |
| 2429   | Layout 1 | `5e07d6695c80`  |
| 2421   | Layout 1 | `5e07d6695c80`  |
| 2414   | Layout 1 | `5e07d6695c80`  |
| 2407   | Layout 1 | `5e07d6695c80`  |
| 2401   | Layout 1 | `5e07d6695c80`  |
| 2397   | Layout 1 | `5e07d6695c80`  |
| 2393   | Layout 1 | `5e07d6695c80`  |
| 2384   | Layout 1 | `5e07d6695c80`  |
| 2378   | Layout 1 | `5e07d6695c80`  |
| 2372   | Layout 1 | `5e07d6695c80`  |
| 2358   | Layout 1 | `5e07d6695c80`  |
| 2352   | Layout 1 | `5e07d6695c80`  |
| 2347   | Layout 1 | `5e07d6695c80`  |
| 2343   | Layout 1 | `5e07d6695c80`  |
| 2335   | Layout 1 | `5e07d6695c80`  |
| 2327   | Layout 1 | `5e07d6695c80`  |
| 2324   | Layout 1 | `5e07d6695c80`  |
| 2319   | Layout 1 | `5e07d6695c80`  |
| 2313   | Layout 1 | `5e07d6695c80`  |
| 2308   | Layout 1 | `5e07d6695c80`  |
| 2302   | Layout 1 | `5e07d6695c80`  |
| 2295   | Layout 1 | `5e07d6695c80`  |
| 2290   | Layout 1 | `5e07d6695c80`  |
| 2284   | Layout 1 | `5e07d6695c80`  |
| 2276   | Layout 1 | `5e07d6695c80`  |
| 2269   | Layout 1 | `5e07d6695c80`  |
| 2259   | Layout 1 | `5e07d6695c80`  |
| 2250   | Layout 1 | `5e07d6695c80`  |
| 2243   | Layout 1 | `5e07d6695c80`  |
| 2235   | Layout 1 | `5e07d6695c80`  |
| 2229   | Layout 1 | `5e07d6695c80`  |
| 2224   | Layout 1 | `5e07d6695c80`  |
| 2218   | Layout 1 | `5e07d6695c80`  |
| 2215   | Layout 1 | `5e07d6695c80`  |
| 2207   | Layout 1 | `5e07d6695c80`  |
| 2203   | Layout 1 | `5e07d6695c80`  |
| 2196   | Layout 1 | `5e07d6695c80`  |
| 2192   | Layout 1 | `5e07d6695c80`  |
| 2189   | Layout 1 | `5e07d6695c80`  |
| 2183   | Layout 1 | `5e07d6695c80`  |
| 2179   | Layout 1 | `5e07d6695c80`  |
| 2171   | Layout 1 | `5e07d6695c80`  |
| 2163   | Layout 1 | `5e07d6695c80`  |
| 2156   | Layout 1 | `5e07d6695c80`  |
| 2151   | Layout 1 | `5e07d6695c80`  |
| 2147   | Layout 1 | `5e07d6695c80`  |
| 2142   | Layout 1 | `5e07d6695c80`  |
| 2138   | Layout 1 | `5e07d6695c80`  |
| 2134   | Layout 1 | `5e07d6695c80`  |
| 2130   | Layout 1 | `5e07d6695c80`  |
| 2122   | Layout 1 | `5e07d6695c80`  |
| 2107   | Layout 1 | `5e07d6695c80`  |
| 2098   | Layout 1 | `5e07d6695c80`  |
| 2089   | Layout 1 | `5e07d6695c80`  |
| 2081   | Layout 1 | `5e07d6695c80`  |
| 2073   | Layout 1 | `5e07d6695c80`  |
| 2067   | Layout 1 | `5e07d6695c80`  |
| 2063   | Layout 1 | `5e07d6695c80`  |
| 2059   | Layout 1 | `5e07d6695c80`  |
| 2052   | Layout 1 | `5e07d6695c80`  |
| 2044   | Layout 1 | `5e07d6695c80`  |
| 2039   | Layout 1 | `5e07d6695c80`  |
| 2032   | Layout 1 | `5e07d6695c80`  |
| 2025   | Layout 1 | `5e07d6695c80`  |
| 2011   | Layout 1 | `5e07d6695c80`  |
| 2005   | Layout 1 | `5e07d6695c80`  |
| 2000   | Layout 1 | `5e07d6695c80`  |
| 1996   | Layout 1 | `5e07d6695c80`  |
| 1991   | Layout 1 | `5e07d6695c80`  |
| 1985   | Layout 1 | `5e07d6695c80`  |
| 1980   | Layout 1 | `5e07d6695c80`  |
| 1969   | Layout 1 | `5e07d6695c80`  |
| 1964   | Layout 1 | `5e07d6695c80`  |
| 1958   | Layout 1 | `5e07d6695c80`  |
| 1950   | Layout 1 | `5e07d6695c80`  |
| 1945   | Layout 1 | `5e07d6695c80`  |
| 1937   | Layout 1 | `5e07d6695c80`  |
| 1933   | Layout 1 | `5e07d6695c80`  |
| 1927   | Layout 1 | `5e07d6695c80`  |
| 1921   | Layout 1 | `5e07d6695c80`  |
| 1914   | Layout 1 | `5e07d6695c80`  |
| 1908   | Layout 1 | `5e07d6695c80`  |
| 1897   | Layout 1 | `5e07d6695c80`  |
| 1892   | Layout 1 | `5e07d6695c80`  |
| 1886   | Layout 1 | `5e07d6695c80`  |
| 1881   | Layout 1 | `5e07d6695c80`  |
| 1871   | Layout 1 | `5e07d6695c80`  |
| 1866   | Layout 1 | `5e07d6695c80`  |
| 1862   | Layout 1 | `5e07d6695c80`  |
| 1854   | Layout 1 | `5e07d6695c80`  |
| 1846   | Layout 1 | `5e07d6695c80`  |
| 1838   | Layout 1 | `5e07d6695c80`  |
| 1832   | Layout 1 | `5e07d6695c80`  |
| 1826   | Layout 1 | `5e07d6695c80`  |
| 1822   | Layout 1 | `5e07d6695c80`  |
| 1818   | Layout 1 | `5e07d6695c80`  |
| 1804   | Layout 1 | `5e07d6695c80`  |
| 1794   | Layout 1 | `5e07d6695c80`  |
| 1790   | Layout 1 | `5e07d6695c80`  |
| 1784   | Layout 1 | `5e07d6695c80`  |
| 1774   | Layout 1 | `5e07d6695c80`  |
| 1771   | Layout 1 | `5e07d6695c80`  |
| 1762   | Layout 1 | `5e07d6695c80`  |
| 1759   | Layout 1 | `5e07d6695c80`  |
| 1754   | Layout 1 | `5e07d6695c80`  |
| 1749   | Layout 1 | `5e07d6695c80`  |
| 1743   | Layout 1 | `5e07d6695c80`  |
| 1737   | Layout 1 | `5e07d6695c80`  |
| 1731   | Layout 1 | `5e07d6695c80`  |
| 1725   | Layout 1 | `5e07d6695c80`  |
| 1717   | Layout 1 | `5e07d6695c80`  |
| 1710   | Layout 1 | `5e07d6695c80`  |
| 1704   | Layout 1 | `5e07d6695c80`  |
| 1698   | Layout 1 | `5e07d6695c80`  |
| 1690   | Layout 1 | `5e07d6695c80`  |
| 1685   | Layout 1 | `5e07d6695c80`  |
| 1680   | Layout 1 | `5e07d6695c80`  |
| 1674   | Layout 1 | `5e07d6695c80`  |
| 1668   | Layout 1 | `5e07d6695c80`  |
| 1659   | Layout 1 | `5e07d6695c80`  |
| 1649   | Layout 1 | `5e07d6695c80`  |
| 1642   | Layout 1 | `5e07d6695c80`  |
| 1636   | Layout 1 | `5e07d6695c80`  |
| 1628   | Layout 1 | `5e07d6695c80`  |
| 1622   | Layout 1 | `5e07d6695c80`  |
| 1614   | Layout 1 | `5e07d6695c80`  |
| 1608   | Layout 1 | `5e07d6695c80`  |
| 1602   | Layout 1 | `5e07d6695c80`  |
| 1598   | Layout 1 | `5e07d6695c80`  |
| 1594   | Layout 1 | `5e07d6695c80`  |
| 1590   | Layout 1 | `5e07d6695c80`  |
| 1587   | Layout 1 | `5e07d6695c80`  |
| 1584   | Layout 1 | `5e07d6695c80`  |
| 1579   | Layout 1 | `5e07d6695c80`  |
| 1572   | Layout 1 | `5e07d6695c80`  |
| 1565   | Layout 1 | `5e07d6695c80`  |
| 1559   | Layout 1 | `5e07d6695c80`  |
| 1554   | Layout 1 | `5e07d6695c80`  |
| 1547   | Layout 1 | `5e07d6695c80`  |
| 1537   | Layout 1 | `5e07d6695c80`  |
| 1529   | Layout 1 | `5e07d6695c80`  |
| 1524   | Layout 1 | `5e07d6695c80`  |
| 1519   | Layout 1 | `5e07d6695c80`  |
| 1509   | Layout 1 | `5e07d6695c80`  |
| 1506   | Layout 1 | `5e07d6695c80`  |
| 1504   | Layout 1 | `5e07d6695c80`  |
| 1500   | Layout 1 | `5e07d6695c80`  |
| 1493   | Layout 1 | `5e07d6695c80`  |
| 1489   | Layout 1 | `5e07d6695c80`  |
| 1485   | Layout 1 | `5e07d6695c80`  |
| 1481   | Layout 1 | `5e07d6695c80`  |
| 1474   | Layout 1 | `5e07d6695c80`  |
| 1466   | Layout 1 | `5e07d6695c80`  |
| 1462   | Layout 1 | `5e07d6695c80`  |
| 1459   | Layout 1 | `5e07d6695c80`  |
| 1453   | Layout 1 | `5e07d6695c80`  |
| 1450   | Layout 1 | `5e07d6695c80`  |
| 1445   | Layout 1 | `5e07d6695c80`  |
| 1439   | Layout 1 | `5e07d6695c80`  |
| 1433   | Layout 1 | `5e07d6695c80`  |
| 1430   | Layout 1 | `5e07d6695c80`  |
| 1426   | Layout 1 | `5e07d6695c80`  |
| 1421   | Layout 1 | `5e07d6695c80`  |
| 1417   | No file  | `5e07d6695c80`  |
| 1416   | No file  | `5e07d6695c80`  |
| 1409   | No file  | `5e07d6695c80`  |
| 1405   | No file  | `5e07d6695c80`  |
| 1401   | No file  | `5e07d6695c80`  |
| 1396   | No file  | `5e07d6695c80`  |
| 1391   | No file  | `5e07d6695c80`  |
| 1390   | No file  | `5e07d6695c80`  |
| 1386   | No file  | `5e07d6695c80`  |
| 1381   | No file  | `5e07d6695c80`  |
| 1379   | No file  | `5e07d6695c80`  |
| 1372   | No file  | `5e07d6695c80`  |
| 1366   | No file  | `5e07d6695c80`  |
| 1364   | No file  | `5e07d6695c80`  |
| 1363   | No file  | `5e07d6695c80`  |
| 1360   | No file  | `5e07d6695c80`  |
| 1358   | No file  | `5e07d6695c80`  |
| 1355   | No file  | `5e07d6695c80`  |
| 1351   | No file  | `5e07d6695c80`  |
| 1348   | No file  | `5e07d6695c80`  |
| 1346   | No file  | `5e07d6695c80`  |
| 1341   | No file  | `5e07d6695c80`  |
| 1340   | No file  | `5e07d6695c80`  |
| 1338   | No file  | `5e07d6695c80`  |
| 1335   | No file  | `5e07d6695c80`  |
| 1333   | No file  | `5e07d6695c80`  |
| 1329   | No file  | `5e07d6695c80`  |
| 1327   | No file  | `5e07d6695c80`  |
| 1324   | No file  | `5e07d6695c80`  |
| 1321   | No file  | `5e07d6695c80`  |
| 1319   | No file  | `5e07d6695c80`  |
| 1318   | No file  | `5e07d6695c80`  |
| 1316   | No file  | `5e07d6695c80`  |
| 1313   | No file  | `5e07d6695c80`  |
| 1311   | No file  | `5e07d6695c80`  |
| 1309   | No file  | `5e07d6695c80`  |
| 1304   | No file  | `5e07d6695c80`  |
| 1292   | No file  | `5e07d6695c80`  |
| 1286   | No file  | `5e07d6695c80`  |
| 1280   | No file  | `5e07d6695c80`  |
| 1276   | No file  | `5e07d6695c80`  |
| 1267   | No file  | `5e07d6695c80`  |
| 1261   | No file  | `5e07d6695c80`  |
| 1256   | No file  | `5e07d6695c80`  |
| 1250   | No file  | `5e07d6695c80`  |
| 1246   | No file  | `5e07d6695c80`  |
| 1239   | No file  | `5e07d6695c80`  |
| 1230   | No file  | `5e07d6695c80`  |
| 1226   | No file  | `5e07d6695c80`  |
| 1220   | No file  | `5e07d6695c80`  |
| 1217   | No file  | `5e07d6695c80`  |
| 1211   | No file  | `5e07d6695c80`  |
| 1210   | No file  | `5e07d6695c80`  |
| 1208   | No file  | `5e07d6695c80`  |
| 1203   | No file  | `5e07d6695c80`  |
| 1197   | No file  | `5e07d6695c80`  |
| 1194   | No file  | `5e07d6695c80`  |
| 1192   | No file  | `5e07d6695c80`  |
| 1187   | No file  | `5e07d6695c80`  |
| 1183   | No file  | `5e07d6695c80`  |
| 1177   | No file  | `5e07d6695c80`  |
| 1173   | No file  | `5e07d6695c80`  |
| 1167   | No file  | `5e07d6695c80`  |
| 1164   | No file  | `5e07d6695c80`  |
| 1156   | No file  | `5e07d6695c80`  |
| 1149   | No file  | `5e07d6695c80`  |
| 1144   | No file  | `5e07d6695c80`  |
| 1137   | No file  | `5e07d6695c80`  |
| 1132   | No file  | `5e07d6695c80`  |
| 1127   | No file  | `5e07d6695c80`  |
| 1122   | No file  | `5e07d6695c80`  |
| 1118   | No file  | `5e07d6695c80`  |
| 1114   | No file  | `5e07d6695c80`  |
| 1109   | No file  | `5e07d6695c80`  |
| 1102   | No file  | `5e07d6695c80`  |
| 1096   | No file  | `5e07d6695c80`  |
| 1088   | No file  | `5e07d6695c80`  |
| 1081   | No file  | `5e07d6695c80`  |
| 1076   | No file  | `5e07d6695c80`  |
| 1069   | No file  | `5e07d6695c80`  |
| 1064   | No file  | `5e07d6695c80`  |
| 1058   | No file  | `5e07d6695c80`  |
| 1051   | No file  | `5e07d6695c80`  |
| 1044   | No file  | `5e07d6695c80`  |
| 1036   | No file  | `5e07d6695c80`  |
| 1026   | No file  | `5e07d6695c80`  |
| 1016   | No file  | `5e07d6695c80`  |
| 1009   | No file  | `5e07d6695c80`  |
| 1005   | No file  | `5e07d6695c80`  |
| 1000   | No file  | `5e07d6695c80`  |
| 998    | No file  | `5e07d6695c80`  |
| 990    | No file  | `5e07d6695c80`  |
| 979    | No file  | `5e07d6695c80`  |
| 972    | No file  | `5e07d6695c80`  |
| 963    | No file  | `5e07d6695c80`  |
| 955    | No file  | `5e07d6695c80`  |
| 946    | No file  | `5e07d6695c80`  |
| 938    | No file  | `5e07d6695c80`  |
| 927    | No file  | `5e07d6695c80`  |
| 911    | No file  | `5e07d6695c80`  |
| 904    | No file  | `5e07d6695c80`  |
| 899    | No file  | `5e07d6695c80`  |
| 894    | No file  | `5e07d6695c80`  |
| 885    | No file  | `5e07d6695c80`  |
| 879    | No file  | `5e07d6695c80`  |
| 872    | No file  | `5e07d6695c80`  |
| 864    | No file  | `5e07d6695c80`  |
| 855    | No file  | `5e07d6695c80`  |
| 853    | No file  | `5e07d6695c80`  |
| 845    | No file  | `5e07d6695c80`  |
| 837    | No file  | `5e07d6695c80`  |
| 829    | No file  | `5e07d6695c80`  |
| 822    | No file  | `5e07d6695c80`  |
| 814    | No file  | `5e07d6695c80`  |
| 805    | No file  | `5e07d6695c80`  |
| 794    | No file  | `5e07d6695c80`  |
| 787    | No file  | `5e07d6695c80`  |
| 780    | No file  | `5e07d6695c80`  |
| 771    | No file  | `5e07d6695c80`  |
| 760    | No file  | `5e07d6695c80`  |
| 748    | No file  | `5e07d6695c80`  |
| 741    | No file  | `5e07d6695c80`  |
| 736    | No file  | `5e07d6695c80`  |
| 731    | No file  | `5e07d6695c80`  |
| 723    | No file  | `5e07d6695c80`  |
| 711    | No file  | `5e07d6695c80`  |
| 707    | No file  | `5e07d6695c80`  |
| 697    | No file  | `5e07d6695c80`  |
| 689    | No file  | `5e07d6695c80`  |
| 683    | No file  | `5e07d6695c80`  |
| 678    | No file  | `5e07d6695c80`  |
| 670    | No file  | `5e07d6695c80`  |
| 661    | No file  | `5e07d6695c80`  |
| 656    | No file  | `5e07d6695c80`  |
| 652    | No file  | `5e07d6695c80`  |
| 643    | No file  | `5e07d6695c80`  |
| 637    | No file  | `5e07d6695c80`  |
| 630    | No file  | `5e07d6695c80`  |
| 627    | No file  | `5e07d6695c80`  |
| 621    | No file  | `5e07d6695c80`  |
| 617    | No file  | `5e07d6695c80`  |
| 615    | No file  | `5e07d6695c80`  |
| 606    | No file  | `5e07d6695c80`  |
| 599    | No file  | `5e07d6695c80`  |
| 592    | No file  | `5e07d6695c80`  |
| 586    | No file  | `5e07d6695c80`  |
| 577    | No file  | `5e07d6695c80`  |
| 569    | No file  | `5e07d6695c80`  |
| 561    | No file  | `5e07d6695c80`  |
| 554    | No file  | `5e07d6695c80`  |
| 542    | No file  | `5e07d6695c80`  |
| 532    | No file  | `5e07d6695c80`  |
| 531    | No file  | `5e07d6695c80`  |
| 526    | No file  | `5e07d6695c80`  |
| 521    | No file  | `5e07d6695c80`  |
| 517    | No file  | `5e07d6695c80`  |
| 510    | No file  | `5e07d6695c80`  |
| 508    | No file  | `5e07d6695c80`  |
| 504    | No file  | `5e07d6695c80`  |
| 497    | No file  | `5e07d6695c80`  |
| 491    | No file  | `5e07d6695c80`  |
| 485    | No file  | `5e07d6695c80`  |
| 478    | No file  | `5e07d6695c80`  |
| 472    | No file  | `5e07d6695c80`  |
| 466    | No file  | `5e07d6695c80`  |
| 457    | No file  | `5e07d6695c80`  |
| 452    | No file  | `5e07d6695c80`  |
| 449    | No file  | `5e07d6695c80`  |
| 435    | No file  | `5e07d6695c80`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                    |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| `stringtable.bss`     | Optional | Hash of each `[ComboSheet_CommonString_N]` key in a command, `GAME` sheet |
| `languagedata_en.loc` | Optional | Class names (type `21`), skill names (type `10`), command words (type `37`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                       | Field        | Notes                                         |
| ------------------- | -------------------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]                    | magic        | `PABR`                                        |
| `+0x04`             | u32                        | class_count  | Number of class lists                         |
| `+0x08`             | Class Combos[class_count]  | classes      | One per class, in no class order; see Class Combos |
| `classes+0x00`      | String Table               | string_table | The command texts                             |
| `string_table+0x00` | u32                        | table_start  | Offset of the string table, where `classes` ends |
| `string_table+0x04` | u32                        | zero         | Always `0`                                    |

### Class Combos (variable: 4 bytes + combos)

| Offset  | Type              | Field       | Notes                                              |
| ------- | ----------------- | ----------- | -------------------------------------------------- |
| `+0x00` | u32               | combo_count | Number of combos of the class                      |
| `+0x04` | Combo[combo_count]| combos      | Every combo holds the same `class_type`; see Combo |

### Combo (variable: 9 bytes + steps)

| Offset  | Type              | Field             | Notes                                                    |
| ------- | ----------------- | ----------------- | -------------------------------------------------------- |
| `+0x00` | u8                | class_type        | Class, LOC type `21` (`1` Hashashin)                     |
| `+0x01` | u32               | combo_skill_count | Number of skills in the combo; equal to `step_count` on every combo |
| `+0x05` | u32               | step_count        | Number of `steps`; `2` to `7` on client 3482             |
| `+0x09` | Step[step_count]  | steps             | The skills in order; see Step                            |

### Step (6 bytes)

| Offset  | Type | Field         | Notes                                                      |
| ------- | ---- | ------------- | ---------------------------------------------------------- |
| `+0x00` | u16  | skill_no      | Skill number, LOC type `10`                                |
| `+0x02` | u32  | command_index | String table index of the step's key binding text; see Commands |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; 83 on client 3482      |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries, each text stored once |

## Commands

A command is the key binding text of one step, the same text LOC type 2
holds for the skill (`str_id4` 1): `<{KeyBind:MoveBack}> + <{KeyBind:Kick}>`
for skill 5534, Sand Divider I. Each `{KeyBind:Name}` is a player action
whose key the game fills from the key settings, and the angle brackets
draw it as a key. Words between the keys are `GAME` sheet keys of
[`stringtable.bss`](stringtable_bss.md) in square brackets; the English is
LOC type 37 under the key's hash. Client 3482 uses these eight:

| Key                          | English (LOC)          |
| ---------------------------- | ---------------------- |
| `ComboSheet_CommonString_1`  | Directional Key        |
| `ComboSheet_CommonString_2`  | Maintain               |
| `ComboSheet_CommonString_3`  | Back                   |
| `ComboSheet_CommonString_4`  | Sprinting              |
| `ComboSheet_CommonString_5`  | While Jumping          |
| `ComboSheet_CommonString_6`  | Leaping laterally      |
| `ComboSheet_CommonString_7`  | Jumping in a direction |
| `ComboSheet_CommonString_8`  | While charging         |

`[/]` between two keys (`<{KeyBind:MoveLeft}> [/] <{KeyBind:MoveRight}>`)
is a literal "or".

## Field Names

The `Skill_Combo` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `ClassType`, `ComboSkillCount`, `ComboType`, then
`Combo1` to `Combo10` and `Command1` to `Command10`; the developer workbook
`datasheet_skillcomboguide.xlsm` adds the note columns `#ComboIndex`,
`#LimitLevel`, `#Reward` and `#Desc`. Its 280 rows match the file combo by
combo in class, position within the class, skills and command texts: 280
of 280 on client 1784 and 280 of 280 on client 3482.

| Field             | Column            |
| ----------------- | ----------------- |
| class_type        | `ClassType`       |
| combo_skill_count | `ComboSkillCount` |
| skill_no          | `Combo1` to `Combo10` |
| command_index     | `Command1` to `Command10`, stored once in the string table |

`ComboType` is `0` on every sheet row and has no byte in the file. The file
of client 1784 adds class 10 (290 combos, 23 classes); client 3482 adds
classes 7, 10, 15 and 30 (321 combos, 26 classes). The 2016 PDB has no
struct for the table.

## Notes

- `ui_widget_skillcommand.luac` (client 3482) reads the learned combos
  with `Toclient_getLearnSkillComboListCount()`,
  `Toclient_getSkillComboListCount(index)`,
  `Toclient_getLearnSkillComboListSkillNo(index, step)` and
  `Toclient_getLearnSkillComboListCommand(index, step)`, joins the commands
  with ` | ` and draws them while `_ContentsGroup_SkillComboGuide` is on.
  It skips combos whose `Toclient_getLearnSkillComboType(index)` differs
  from the current skill type of the player.
- The class lists follow no class order (`1`, `16`, ... on client 3482);
  inside a list the combos keep the sheet order.

## Open Questions

### Where the Combo Type Comes From

The widget compares `Toclient_getLearnSkillComboType()` with the player's
current skill type (`0` when the class has no Succession), but the file has
no type byte and the sheet's `ComboType` is `0` on every row. The client
may take it from the skills of the combo.
