# `contentsschedulerss.bss` Format

## Purpose

The contents of the Contents Schedule window (`Panel_Window_ContentsSchedule_All`)
that a player can add to the list: per content type the `RESOURCE` sheet
key of its title, the texture key of its icon and the contents groups that
must be open. On client 3482 the four rows are the Black Shrine (Donghae
solo and Hwanghae party, the `MorningLand` keys), the Altar of Blood and
the War of the Roses, as LOC titles them. The file is a
u32 count and variable rows, with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | ----------------------- |
| 1      | 3444 and later | 3483    | `contentsschedulerss.bss` | 318   | 4 Row   | 69 to 83, 78 on average |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 1      | `contentsschedulerss.bss` | 318 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `f1fbb66e3a12`  |
| 3482   | Layout 1 | `f1fbb66e3a12`  |
| 3474   | Layout 1 | `f1fbb66e3a12`  |
| 3473   | Layout 1 | `f1fbb66e3a12`  |
| 3464   | Layout 1 | `f1fbb66e3a12`  |
| 3458   | Layout 1 | `f1fbb66e3a12`  |
| 3454   | Layout 1 | `f1fbb66e3a12`  |
| 3444   | Layout 1 | `f1fbb66e3a12`  |
| 3435   | No file  | `f1fbb66e3a12`  |
| 3426   | No file  | `f1fbb66e3a12`  |
| 3418   | No file  | `f1fbb66e3a12`  |
| 3412   | No file  | `f1fbb66e3a12`  |
| 3402   | No file  | `f1fbb66e3a12`  |
| 3396   | No file  | `f1fbb66e3a12`  |
| 3387   | No file  | `f1fbb66e3a12`  |
| 3381   | No file  | `f1fbb66e3a12`  |
| 3373   | No file  | `f1fbb66e3a12`  |
| 3364   | No file  | `f1fbb66e3a12`  |
| 3356   | No file  | `f1fbb66e3a12`  |
| 3349   | No file  | `f1fbb66e3a12`  |
| 3342   | No file  | `f1fbb66e3a12`  |
| 3335   | No file  | `f1fbb66e3a12`  |
| 3326   | No file  | `f1fbb66e3a12`  |
| 3321   | No file  | `f1fbb66e3a12`  |
| 3314   | No file  | `f1fbb66e3a12`  |
| 3303   | No file  | `f1fbb66e3a12`  |
| 3302   | No file  | `f1fbb66e3a12`  |
| 3293   | No file  | `f1fbb66e3a12`  |
| 3283   | No file  | `f1fbb66e3a12`  |
| 3275   | No file  | `f1fbb66e3a12`  |
| 3267   | No file  | `f1fbb66e3a12`  |
| 3258   | No file  | `f1fbb66e3a12`  |
| 3251   | No file  | `f1fbb66e3a12`  |
| 3242   | No file  | `f1fbb66e3a12`  |
| 3235   | No file  | `f1fbb66e3a12`  |
| 3229   | No file  | `f1fbb66e3a12`  |
| 3212   | No file  | `f1fbb66e3a12`  |
| 3203   | No file  | `f1fbb66e3a12`  |
| 3193   | No file  | `f1fbb66e3a12`  |
| 3186   | No file  | `f1fbb66e3a12`  |
| 3177   | No file  | `f1fbb66e3a12`  |
| 3169   | No file  | `f1fbb66e3a12`  |
| 3158   | No file  | `f1fbb66e3a12`  |
| 3151   | No file  | `f1fbb66e3a12`  |
| 3144   | No file  | `f1fbb66e3a12`  |
| 3133   | No file  | `f1fbb66e3a12`  |
| 3125   | No file  | `f1fbb66e3a12`  |
| 3118   | No file  | `f1fbb66e3a12`  |
| 3111   | No file  | `f1fbb66e3a12`  |
| 3103   | No file  | `f1fbb66e3a12`  |
| 3095   | No file  | `f1fbb66e3a12`  |
| 3086   | No file  | `f1fbb66e3a12`  |
| 3072   | No file  | `f1fbb66e3a12`  |
| 3062   | No file  | `f1fbb66e3a12`  |
| 3052   | No file  | `f1fbb66e3a12`  |
| 3045   | No file  | `f1fbb66e3a12`  |
| 3037   | No file  | `f1fbb66e3a12`  |
| 3030   | No file  | `f1fbb66e3a12`  |
| 3021   | No file  | `f1fbb66e3a12`  |
| 3012   | No file  | `f1fbb66e3a12`  |
| 3002   | No file  | `f1fbb66e3a12`  |
| 2995   | No file  | `f1fbb66e3a12`  |
| 2987   | No file  | `f1fbb66e3a12`  |
| 2978   | No file  | `f1fbb66e3a12`  |
| 2970   | No file  | `f1fbb66e3a12`  |
| 2959   | No file  | `f1fbb66e3a12`  |
| 2951   | No file  | `f1fbb66e3a12`  |
| 2942   | No file  | `f1fbb66e3a12`  |
| 2935   | No file  | `f1fbb66e3a12`  |
| 2932   | No file  | `f1fbb66e3a12`  |
| 2923   | No file  | `f1fbb66e3a12`  |
| 2919   | No file  | `f1fbb66e3a12`  |
| 2907   | No file  | `f1fbb66e3a12`  |
| 2900   | No file  | `f1fbb66e3a12`  |
| 2891   | No file  | `f1fbb66e3a12`  |
| 2882   | No file  | `f1fbb66e3a12`  |
| 2872   | No file  | `f1fbb66e3a12`  |
| 2863   | No file  | `f1fbb66e3a12`  |
| 2855   | No file  | `f1fbb66e3a12`  |
| 2849   | No file  | `f1fbb66e3a12`  |
| 2844   | No file  | `f1fbb66e3a12`  |
| 2834   | No file  | `f1fbb66e3a12`  |
| 2825   | No file  | `f1fbb66e3a12`  |
| 2819   | No file  | `f1fbb66e3a12`  |
| 2811   | No file  | `f1fbb66e3a12`  |
| 2803   | No file  | `f1fbb66e3a12`  |
| 2794   | No file  | `f1fbb66e3a12`  |
| 2783   | No file  | `f1fbb66e3a12`  |
| 2774   | No file  | `f1fbb66e3a12`  |
| 2765   | No file  | `f1fbb66e3a12`  |
| 2756   | No file  | `f1fbb66e3a12`  |
| 2750   | No file  | `f1fbb66e3a12`  |
| 2743   | No file  | `f1fbb66e3a12`  |
| 2736   | No file  | `f1fbb66e3a12`  |
| 2726   | No file  | `f1fbb66e3a12`  |
| 2717   | No file  | `f1fbb66e3a12`  |
| 2709   | No file  | `f1fbb66e3a12`  |
| 2703   | No file  | `f1fbb66e3a12`  |
| 2695   | No file  | `f1fbb66e3a12`  |
| 2684   | No file  | `f1fbb66e3a12`  |
| 2672   | No file  | `f1fbb66e3a12`  |
| 2665   | No file  | `f1fbb66e3a12`  |
| 2657   | No file  | `f1fbb66e3a12`  |
| 2649   | No file  | `f1fbb66e3a12`  |
| 2644   | No file  | `f1fbb66e3a12`  |
| 2637   | No file  | `f1fbb66e3a12`  |
| 2629   | No file  | `f1fbb66e3a12`  |
| 2619   | No file  | `f1fbb66e3a12`  |
| 2612   | No file  | `f1fbb66e3a12`  |
| 2606   | No file  | `f1fbb66e3a12`  |
| 2602   | No file  | `f1fbb66e3a12`  |
| 2601   | No file  | `f1fbb66e3a12`  |
| 2592   | No file  | `f1fbb66e3a12`  |
| 2583   | No file  | `f1fbb66e3a12`  |
| 2575   | No file  | `f1fbb66e3a12`  |
| 2567   | No file  | `f1fbb66e3a12`  |
| 2560   | No file  | `f1fbb66e3a12`  |
| 2553   | No file  | `f1fbb66e3a12`  |
| 2545   | No file  | `f1fbb66e3a12`  |
| 2538   | No file  | `f1fbb66e3a12`  |
| 2529   | No file  | `f1fbb66e3a12`  |
| 2519   | No file  | `f1fbb66e3a12`  |
| 2513   | No file  | `f1fbb66e3a12`  |
| 2510   | No file  | `f1fbb66e3a12`  |
| 2507   | No file  | `f1fbb66e3a12`  |
| 2503   | No file  | `f1fbb66e3a12`  |
| 2498   | No file  | `f1fbb66e3a12`  |
| 2492   | No file  | `f1fbb66e3a12`  |
| 2487   | No file  | `f1fbb66e3a12`  |
| 2480   | No file  | `f1fbb66e3a12`  |
| 2474   | No file  | `f1fbb66e3a12`  |
| 2468   | No file  | `f1fbb66e3a12`  |
| 2460   | No file  | `f1fbb66e3a12`  |
| 2453   | No file  | `f1fbb66e3a12`  |
| 2444   | No file  | `f1fbb66e3a12`  |
| 2438   | No file  | `f1fbb66e3a12`  |
| 2434   | No file  | `f1fbb66e3a12`  |
| 2429   | No file  | `f1fbb66e3a12`  |
| 2421   | No file  | `f1fbb66e3a12`  |
| 2414   | No file  | `f1fbb66e3a12`  |
| 2407   | No file  | `f1fbb66e3a12`  |
| 2401   | No file  | `f1fbb66e3a12`  |
| 2397   | No file  | `f1fbb66e3a12`  |
| 2393   | No file  | `f1fbb66e3a12`  |
| 2384   | No file  | `f1fbb66e3a12`  |
| 2378   | No file  | `f1fbb66e3a12`  |
| 2372   | No file  | `f1fbb66e3a12`  |
| 2358   | No file  | `f1fbb66e3a12`  |
| 2352   | No file  | `f1fbb66e3a12`  |
| 2347   | No file  | `f1fbb66e3a12`  |
| 2343   | No file  | `f1fbb66e3a12`  |
| 2335   | No file  | `f1fbb66e3a12`  |
| 2327   | No file  | `f1fbb66e3a12`  |
| 2324   | No file  | `f1fbb66e3a12`  |
| 2319   | No file  | `f1fbb66e3a12`  |
| 2313   | No file  | `f1fbb66e3a12`  |
| 2308   | No file  | `f1fbb66e3a12`  |
| 2302   | No file  | `f1fbb66e3a12`  |
| 2295   | No file  | `f1fbb66e3a12`  |
| 2290   | No file  | `f1fbb66e3a12`  |
| 2284   | No file  | `f1fbb66e3a12`  |
| 2276   | No file  | `f1fbb66e3a12`  |
| 2269   | No file  | `f1fbb66e3a12`  |
| 2259   | No file  | `f1fbb66e3a12`  |
| 2250   | No file  | `f1fbb66e3a12`  |
| 2243   | No file  | `f1fbb66e3a12`  |
| 2235   | No file  | `f1fbb66e3a12`  |
| 2229   | No file  | `f1fbb66e3a12`  |
| 2224   | No file  | `f1fbb66e3a12`  |
| 2218   | No file  | `f1fbb66e3a12`  |
| 2215   | No file  | `f1fbb66e3a12`  |
| 2207   | No file  | `f1fbb66e3a12`  |
| 2203   | No file  | `f1fbb66e3a12`  |
| 2196   | No file  | `f1fbb66e3a12`  |
| 2192   | No file  | `f1fbb66e3a12`  |
| 2189   | No file  | `f1fbb66e3a12`  |
| 2183   | No file  | `f1fbb66e3a12`  |
| 2179   | No file  | `f1fbb66e3a12`  |
| 2171   | No file  | `f1fbb66e3a12`  |
| 2163   | No file  | `f1fbb66e3a12`  |
| 2156   | No file  | `f1fbb66e3a12`  |
| 2151   | No file  | `f1fbb66e3a12`  |
| 2147   | No file  | `f1fbb66e3a12`  |
| 2142   | No file  | `f1fbb66e3a12`  |
| 2138   | No file  | `f1fbb66e3a12`  |
| 2134   | No file  | `f1fbb66e3a12`  |
| 2130   | No file  | `f1fbb66e3a12`  |
| 2122   | No file  | `f1fbb66e3a12`  |
| 2107   | No file  | `f1fbb66e3a12`  |
| 2098   | No file  | `f1fbb66e3a12`  |
| 2089   | No file  | `f1fbb66e3a12`  |
| 2081   | No file  | `f1fbb66e3a12`  |
| 2073   | No file  | `f1fbb66e3a12`  |
| 2067   | No file  | `f1fbb66e3a12`  |
| 2063   | No file  | `f1fbb66e3a12`  |
| 2059   | No file  | `f1fbb66e3a12`  |
| 2052   | No file  | `f1fbb66e3a12`  |
| 2044   | No file  | `f1fbb66e3a12`  |
| 2039   | No file  | `f1fbb66e3a12`  |
| 2032   | No file  | `f1fbb66e3a12`  |
| 2025   | No file  | `f1fbb66e3a12`  |
| 2011   | No file  | `f1fbb66e3a12`  |
| 2005   | No file  | `f1fbb66e3a12`  |
| 2000   | No file  | `f1fbb66e3a12`  |
| 1996   | No file  | `f1fbb66e3a12`  |
| 1991   | No file  | `f1fbb66e3a12`  |
| 1985   | No file  | `f1fbb66e3a12`  |
| 1980   | No file  | `f1fbb66e3a12`  |
| 1969   | No file  | `f1fbb66e3a12`  |
| 1964   | No file  | `f1fbb66e3a12`  |
| 1958   | No file  | `f1fbb66e3a12`  |
| 1950   | No file  | `f1fbb66e3a12`  |
| 1945   | No file  | `f1fbb66e3a12`  |
| 1937   | No file  | `f1fbb66e3a12`  |
| 1933   | No file  | `f1fbb66e3a12`  |
| 1927   | No file  | `f1fbb66e3a12`  |
| 1921   | No file  | `f1fbb66e3a12`  |
| 1914   | No file  | `f1fbb66e3a12`  |
| 1908   | No file  | `f1fbb66e3a12`  |
| 1897   | No file  | `f1fbb66e3a12`  |
| 1892   | No file  | `f1fbb66e3a12`  |
| 1886   | No file  | `f1fbb66e3a12`  |
| 1881   | No file  | `f1fbb66e3a12`  |
| 1871   | No file  | `f1fbb66e3a12`  |
| 1866   | No file  | `f1fbb66e3a12`  |
| 1862   | No file  | `f1fbb66e3a12`  |
| 1854   | No file  | `f1fbb66e3a12`  |
| 1846   | No file  | `f1fbb66e3a12`  |
| 1838   | No file  | `f1fbb66e3a12`  |
| 1832   | No file  | `f1fbb66e3a12`  |
| 1826   | No file  | `f1fbb66e3a12`  |
| 1822   | No file  | `f1fbb66e3a12`  |
| 1818   | No file  | `f1fbb66e3a12`  |
| 1804   | No file  | `f1fbb66e3a12`  |
| 1794   | No file  | `f1fbb66e3a12`  |
| 1790   | No file  | `f1fbb66e3a12`  |
| 1784   | No file  | `f1fbb66e3a12`  |
| 1774   | No file  | `f1fbb66e3a12`  |
| 1771   | No file  | `f1fbb66e3a12`  |
| 1762   | No file  | `f1fbb66e3a12`  |
| 1759   | No file  | `f1fbb66e3a12`  |
| 1754   | No file  | `f1fbb66e3a12`  |
| 1749   | No file  | `f1fbb66e3a12`  |
| 1743   | No file  | `f1fbb66e3a12`  |
| 1737   | No file  | `f1fbb66e3a12`  |
| 1731   | No file  | `f1fbb66e3a12`  |
| 1725   | No file  | `f1fbb66e3a12`  |
| 1717   | No file  | `f1fbb66e3a12`  |
| 1710   | No file  | `f1fbb66e3a12`  |
| 1704   | No file  | `f1fbb66e3a12`  |
| 1698   | No file  | `f1fbb66e3a12`  |
| 1690   | No file  | `f1fbb66e3a12`  |
| 1685   | No file  | `f1fbb66e3a12`  |
| 1680   | No file  | `f1fbb66e3a12`  |
| 1674   | No file  | `f1fbb66e3a12`  |
| 1668   | No file  | `f1fbb66e3a12`  |
| 1659   | No file  | `f1fbb66e3a12`  |
| 1649   | No file  | `f1fbb66e3a12`  |
| 1642   | No file  | `f1fbb66e3a12`  |
| 1636   | No file  | `f1fbb66e3a12`  |
| 1628   | No file  | `f1fbb66e3a12`  |
| 1622   | No file  | `f1fbb66e3a12`  |
| 1614   | No file  | `f1fbb66e3a12`  |
| 1608   | No file  | `f1fbb66e3a12`  |
| 1602   | No file  | `f1fbb66e3a12`  |
| 1598   | No file  | `f1fbb66e3a12`  |
| 1594   | No file  | `f1fbb66e3a12`  |
| 1590   | No file  | `f1fbb66e3a12`  |
| 1587   | No file  | `f1fbb66e3a12`  |
| 1584   | No file  | `f1fbb66e3a12`  |
| 1579   | No file  | `f1fbb66e3a12`  |
| 1572   | No file  | `f1fbb66e3a12`  |
| 1565   | No file  | `f1fbb66e3a12`  |
| 1559   | No file  | `f1fbb66e3a12`  |
| 1554   | No file  | `f1fbb66e3a12`  |
| 1547   | No file  | `f1fbb66e3a12`  |
| 1537   | No file  | `f1fbb66e3a12`  |
| 1529   | No file  | `f1fbb66e3a12`  |
| 1524   | No file  | `f1fbb66e3a12`  |
| 1519   | No file  | `f1fbb66e3a12`  |
| 1509   | No file  | `f1fbb66e3a12`  |
| 1506   | No file  | `f1fbb66e3a12`  |
| 1504   | No file  | `f1fbb66e3a12`  |
| 1500   | No file  | `f1fbb66e3a12`  |
| 1493   | No file  | `f1fbb66e3a12`  |
| 1489   | No file  | `f1fbb66e3a12`  |
| 1485   | No file  | `f1fbb66e3a12`  |
| 1481   | No file  | `f1fbb66e3a12`  |
| 1474   | No file  | `f1fbb66e3a12`  |
| 1466   | No file  | `f1fbb66e3a12`  |
| 1462   | No file  | `f1fbb66e3a12`  |
| 1459   | No file  | `f1fbb66e3a12`  |
| 1453   | No file  | `f1fbb66e3a12`  |
| 1450   | No file  | `f1fbb66e3a12`  |
| 1445   | No file  | `f1fbb66e3a12`  |
| 1439   | No file  | `f1fbb66e3a12`  |
| 1433   | No file  | `f1fbb66e3a12`  |
| 1430   | No file  | `f1fbb66e3a12`  |
| 1426   | No file  | `f1fbb66e3a12`  |
| 1421   | No file  | `f1fbb66e3a12`  |
| 1417   | No file  | `f1fbb66e3a12`  |
| 1416   | No file  | `f1fbb66e3a12`  |
| 1409   | No file  | `f1fbb66e3a12`  |
| 1405   | No file  | `f1fbb66e3a12`  |
| 1401   | No file  | `f1fbb66e3a12`  |
| 1396   | No file  | `f1fbb66e3a12`  |
| 1391   | No file  | `f1fbb66e3a12`  |
| 1390   | No file  | `f1fbb66e3a12`  |
| 1386   | No file  | `f1fbb66e3a12`  |
| 1381   | No file  | `f1fbb66e3a12`  |
| 1379   | No file  | `f1fbb66e3a12`  |
| 1372   | No file  | `f1fbb66e3a12`  |
| 1366   | No file  | `f1fbb66e3a12`  |
| 1364   | No file  | `f1fbb66e3a12`  |
| 1363   | No file  | `f1fbb66e3a12`  |
| 1360   | No file  | `f1fbb66e3a12`  |
| 1358   | No file  | `f1fbb66e3a12`  |
| 1355   | No file  | `f1fbb66e3a12`  |
| 1351   | No file  | `f1fbb66e3a12`  |
| 1348   | No file  | `f1fbb66e3a12`  |
| 1346   | No file  | `f1fbb66e3a12`  |
| 1341   | No file  | `f1fbb66e3a12`  |
| 1340   | No file  | `f1fbb66e3a12`  |
| 1338   | No file  | `f1fbb66e3a12`  |
| 1335   | No file  | `f1fbb66e3a12`  |
| 1333   | No file  | `f1fbb66e3a12`  |
| 1329   | No file  | `f1fbb66e3a12`  |
| 1327   | No file  | `f1fbb66e3a12`  |
| 1324   | No file  | `f1fbb66e3a12`  |
| 1321   | No file  | `f1fbb66e3a12`  |
| 1319   | No file  | `f1fbb66e3a12`  |
| 1318   | No file  | `f1fbb66e3a12`  |
| 1316   | No file  | `f1fbb66e3a12`  |
| 1313   | No file  | `f1fbb66e3a12`  |
| 1311   | No file  | `f1fbb66e3a12`  |
| 1309   | No file  | `f1fbb66e3a12`  |
| 1304   | No file  | `f1fbb66e3a12`  |
| 1292   | No file  | `f1fbb66e3a12`  |
| 1286   | No file  | `f1fbb66e3a12`  |
| 1280   | No file  | `f1fbb66e3a12`  |
| 1276   | No file  | `f1fbb66e3a12`  |
| 1267   | No file  | `f1fbb66e3a12`  |
| 1261   | No file  | `f1fbb66e3a12`  |
| 1256   | No file  | `f1fbb66e3a12`  |
| 1250   | No file  | `f1fbb66e3a12`  |
| 1246   | No file  | `f1fbb66e3a12`  |
| 1239   | No file  | `f1fbb66e3a12`  |
| 1230   | No file  | `f1fbb66e3a12`  |
| 1226   | No file  | `f1fbb66e3a12`  |
| 1220   | No file  | `f1fbb66e3a12`  |
| 1217   | No file  | `f1fbb66e3a12`  |
| 1211   | No file  | `f1fbb66e3a12`  |
| 1210   | No file  | `f1fbb66e3a12`  |
| 1208   | No file  | `f1fbb66e3a12`  |
| 1203   | No file  | `f1fbb66e3a12`  |
| 1197   | No file  | `f1fbb66e3a12`  |
| 1194   | No file  | `f1fbb66e3a12`  |
| 1192   | No file  | `f1fbb66e3a12`  |
| 1187   | No file  | `f1fbb66e3a12`  |
| 1183   | No file  | `f1fbb66e3a12`  |
| 1177   | No file  | `f1fbb66e3a12`  |
| 1173   | No file  | `f1fbb66e3a12`  |
| 1167   | No file  | `f1fbb66e3a12`  |
| 1164   | No file  | `f1fbb66e3a12`  |
| 1156   | No file  | `f1fbb66e3a12`  |
| 1149   | No file  | `f1fbb66e3a12`  |
| 1144   | No file  | `f1fbb66e3a12`  |
| 1137   | No file  | `f1fbb66e3a12`  |
| 1132   | No file  | `f1fbb66e3a12`  |
| 1127   | No file  | `f1fbb66e3a12`  |
| 1122   | No file  | `f1fbb66e3a12`  |
| 1118   | No file  | `f1fbb66e3a12`  |
| 1114   | No file  | `f1fbb66e3a12`  |
| 1109   | No file  | `f1fbb66e3a12`  |
| 1102   | No file  | `f1fbb66e3a12`  |
| 1096   | No file  | `f1fbb66e3a12`  |
| 1088   | No file  | `f1fbb66e3a12`  |
| 1081   | No file  | `f1fbb66e3a12`  |
| 1076   | No file  | `f1fbb66e3a12`  |
| 1069   | No file  | `f1fbb66e3a12`  |
| 1064   | No file  | `f1fbb66e3a12`  |
| 1058   | No file  | `f1fbb66e3a12`  |
| 1051   | No file  | `f1fbb66e3a12`  |
| 1044   | No file  | `f1fbb66e3a12`  |
| 1036   | No file  | `f1fbb66e3a12`  |
| 1026   | No file  | `f1fbb66e3a12`  |
| 1016   | No file  | `f1fbb66e3a12`  |
| 1009   | No file  | `f1fbb66e3a12`  |
| 1005   | No file  | `f1fbb66e3a12`  |
| 1000   | No file  | `f1fbb66e3a12`  |
| 998    | No file  | `f1fbb66e3a12`  |
| 990    | No file  | `f1fbb66e3a12`  |
| 979    | No file  | `f1fbb66e3a12`  |
| 972    | No file  | `f1fbb66e3a12`  |
| 963    | No file  | `f1fbb66e3a12`  |
| 955    | No file  | `f1fbb66e3a12`  |
| 946    | No file  | `f1fbb66e3a12`  |
| 938    | No file  | `f1fbb66e3a12`  |
| 927    | No file  | `f1fbb66e3a12`  |
| 911    | No file  | `f1fbb66e3a12`  |
| 904    | No file  | `f1fbb66e3a12`  |
| 899    | No file  | `f1fbb66e3a12`  |
| 894    | No file  | `f1fbb66e3a12`  |
| 885    | No file  | `f1fbb66e3a12`  |
| 879    | No file  | `f1fbb66e3a12`  |
| 872    | No file  | `f1fbb66e3a12`  |
| 864    | No file  | `f1fbb66e3a12`  |
| 855    | No file  | `f1fbb66e3a12`  |
| 853    | No file  | `f1fbb66e3a12`  |
| 845    | No file  | `f1fbb66e3a12`  |
| 837    | No file  | `f1fbb66e3a12`  |
| 829    | No file  | `f1fbb66e3a12`  |
| 822    | No file  | `f1fbb66e3a12`  |
| 814    | No file  | `f1fbb66e3a12`  |
| 805    | No file  | `f1fbb66e3a12`  |
| 794    | No file  | `f1fbb66e3a12`  |
| 787    | No file  | `f1fbb66e3a12`  |
| 780    | No file  | `f1fbb66e3a12`  |
| 771    | No file  | `f1fbb66e3a12`  |
| 760    | No file  | `f1fbb66e3a12`  |
| 748    | No file  | `f1fbb66e3a12`  |
| 741    | No file  | `f1fbb66e3a12`  |
| 736    | No file  | `f1fbb66e3a12`  |
| 731    | No file  | `f1fbb66e3a12`  |
| 723    | No file  | `f1fbb66e3a12`  |
| 711    | No file  | `f1fbb66e3a12`  |
| 707    | No file  | `f1fbb66e3a12`  |
| 697    | No file  | `f1fbb66e3a12`  |
| 689    | No file  | `f1fbb66e3a12`  |
| 683    | No file  | `f1fbb66e3a12`  |
| 678    | No file  | `f1fbb66e3a12`  |
| 670    | No file  | `f1fbb66e3a12`  |
| 661    | No file  | `f1fbb66e3a12`  |
| 656    | No file  | `f1fbb66e3a12`  |
| 652    | No file  | `f1fbb66e3a12`  |
| 643    | No file  | `f1fbb66e3a12`  |
| 637    | No file  | `f1fbb66e3a12`  |
| 630    | No file  | `f1fbb66e3a12`  |
| 627    | No file  | `f1fbb66e3a12`  |
| 621    | No file  | `f1fbb66e3a12`  |
| 617    | No file  | `f1fbb66e3a12`  |
| 615    | No file  | `f1fbb66e3a12`  |
| 606    | No file  | `f1fbb66e3a12`  |
| 599    | No file  | `f1fbb66e3a12`  |
| 592    | No file  | `f1fbb66e3a12`  |
| 586    | No file  | `f1fbb66e3a12`  |
| 577    | No file  | `f1fbb66e3a12`  |
| 569    | No file  | `f1fbb66e3a12`  |
| 561    | No file  | `f1fbb66e3a12`  |
| 554    | No file  | `f1fbb66e3a12`  |
| 542    | No file  | `f1fbb66e3a12`  |
| 532    | No file  | `f1fbb66e3a12`  |
| 531    | No file  | `f1fbb66e3a12`  |
| 526    | No file  | `f1fbb66e3a12`  |
| 521    | No file  | `f1fbb66e3a12`  |
| 517    | No file  | `f1fbb66e3a12`  |
| 510    | No file  | `f1fbb66e3a12`  |
| 508    | No file  | `f1fbb66e3a12`  |
| 504    | No file  | `f1fbb66e3a12`  |
| 497    | No file  | `f1fbb66e3a12`  |
| 491    | No file  | `f1fbb66e3a12`  |
| 485    | No file  | `f1fbb66e3a12`  |
| 478    | No file  | `f1fbb66e3a12`  |
| 472    | No file  | `f1fbb66e3a12`  |
| 466    | No file  | `f1fbb66e3a12`  |
| 457    | No file  | `f1fbb66e3a12`  |
| 452    | No file  | `f1fbb66e3a12`  |
| 449    | No file  | `f1fbb66e3a12`  |
| 435    | No file  | `f1fbb66e3a12`  |

<!-- versions:end -->

## Companion Files

| File                                       | Required | Role |
| ------------------------------------------ | -------- | ---- |
| `stringtable.bss`                          | Optional | Hash of the `title` key, for its LOC type 37 text |
| `ui_texture/texturestringkey/texturestring_combine.xml` | Optional | Sprite sheet and rectangle of the `icon_texture` key |
| `languagedata_en.loc`                      | Optional | Title in the user's language |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 21 bytes + texts + groups)

| Offset               | Type                         | Field                 | Notes |
| -------------------- | ---------------------------- | --------------------- | ----- |
| `+0x00`              | u8                           | content_type          | Row key, `0` to `3` in file order (client 3482) |
| `+0x01`              | str8                         | title                 | `RESOURCE` sheet key (`PANEL_MORNINGLAND_PART1`, `PANEL_ROSEWAR_TITLE`) |
| `title+0x00`         | str8                         | icon_texture          | Texture key (`Combine_TitleIcon_RoseWar`) |
| `icon_texture+0x00`  | u32                          | contents_group_count  | Number of contents groups, `1` on every row |
| `icon_texture+0x04`  | u32[contents_group_count]    | contents_group_hashes | Contents group keys as the client's string hash of their decimal text, as in `characterstatic.dbss` |

## Rows (Client 3482)

| `content_type` | `title`                         | `icon_texture`                       | Contents group |
| -------------- | ------------------------------- | ------------------------------------ | -------------- |
| 0              | `PANEL_MORNINGLAND_PART1`       | `Combine_TitleIcon_MorningLandBoss`  | 9              |
| 1              | `PANEL_MORNINGLAND_PART2`       | `Combine_TitleIcon_MorningLandBoss`  | 863            |
| 2              | `PANEL_WINDOW_BLOODALTAR_TITLE` | `Combine_Title_Icon_BloodAltar`      | 2195           |
| 3              | `PANEL_ROSEWAR_TITLE`           | `Combine_TitleIcon_RoseWar`          | 1880           |

Every hash is the hash of a key that
[`contentsgroupoptionstaticstatusmanager.bss`](contentsgroupoptionstaticstatusmanager_bss.md)
lists.

## Field Names

The names follow the getters of the object that
`ToClient_GetContentsSchedulerStaticStatus(index)` returns in
`panel_window_contentsschedule_addcontents_1.luac` (client 3482):
`getContentType()`, `getTitle()` (shown with
`PAGetString(Defines.StringSheet_RESOURCE, ...)`), `getIconTexture()`
(passed to `ChangeTextureInfoTextureIDAsync`) and `isContentsGroupOpen()`.
The window loops `ToClient_GetContentsSchedulerCount()` rows from index 0.

## Notes

- The file is in client 3454 and later; clients 3412 and older do not have
  it.
- The Lua names three content types, `__eContentsScheduler_MorningLandBoss_Part`,
  `__eContentsScheduler_BloodAltar` and `__eContentsScheduler_RoseWar`. The
  client sets their values, so the Lua does not show which number each
  one is; the title keys of the rows match the three names in the order
  `0` and `1`, `2`, `3`.
