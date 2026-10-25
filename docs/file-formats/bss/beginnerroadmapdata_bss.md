# `beginnerroadmapdata.bss` Format

## Purpose

The slots of the roadmap window `Panel_Window_BeginnerRoadmap`, shown next
to the season pass: on client 3482 16 steps from the main quest and the
season pass to Tuvala gear, season graduation, the growth pass, horses and
Blackstar gear. Each slot has a Korean title and text, an icon, a
background and a character texture, and an optional event button that
opens a UI window. The Lua walks the slots with
`ToClient_getBeginnerRoadMapDataCount()` and
`ToClient_getBeginnerRoadMapDataKey(index)` and reads each through
`ToClient_getBeginnerRoadMapStaticStatusWrapper(key)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------- | ----- | ------- | --------- |
| 1      | 1950 and later | `beginnerroadmapdata.bss` | 5,052 | 16 Row  | 40        |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `beginnerroadmapdata.bss` | 5,052 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `43a69c5d324e`  |
| 3482   | Layout 1 | `43a69c5d324e`  |
| 3474   | Layout 1 | `43a69c5d324e`  |
| 3473   | Layout 1 | `43a69c5d324e`  |
| 3464   | Layout 1 | `43a69c5d324e`  |
| 3458   | Layout 1 | `43a69c5d324e`  |
| 3454   | Layout 1 | `43a69c5d324e`  |
| 3444   | Layout 1 | `43a69c5d324e`  |
| 3435   | Layout 1 | `43a69c5d324e`  |
| 3426   | Layout 1 | `43a69c5d324e`  |
| 3418   | Layout 1 | `43a69c5d324e`  |
| 3412   | Layout 1 | `43a69c5d324e`  |
| 3402   | Layout 1 | `43a69c5d324e`  |
| 3396   | Layout 1 | `43a69c5d324e`  |
| 3387   | Layout 1 | `43a69c5d324e`  |
| 3381   | Layout 1 | `43a69c5d324e`  |
| 3373   | Layout 1 | `43a69c5d324e`  |
| 3364   | Layout 1 | `43a69c5d324e`  |
| 3356   | Layout 1 | `43a69c5d324e`  |
| 3349   | Layout 1 | `43a69c5d324e`  |
| 3342   | Layout 1 | `43a69c5d324e`  |
| 3335   | Layout 1 | `43a69c5d324e`  |
| 3326   | Layout 1 | `43a69c5d324e`  |
| 3321   | Layout 1 | `43a69c5d324e`  |
| 3314   | Layout 1 | `43a69c5d324e`  |
| 3303   | Layout 1 | `43a69c5d324e`  |
| 3302   | Layout 1 | `43a69c5d324e`  |
| 3293   | Layout 1 | `43a69c5d324e`  |
| 3283   | Layout 1 | `43a69c5d324e`  |
| 3275   | Layout 1 | `43a69c5d324e`  |
| 3267   | Layout 1 | `43a69c5d324e`  |
| 3258   | Layout 1 | `43a69c5d324e`  |
| 3251   | Layout 1 | `43a69c5d324e`  |
| 3242   | Layout 1 | `43a69c5d324e`  |
| 3235   | Layout 1 | `43a69c5d324e`  |
| 3229   | Layout 1 | `43a69c5d324e`  |
| 3212   | Layout 1 | `43a69c5d324e`  |
| 3203   | Layout 1 | `43a69c5d324e`  |
| 3193   | Layout 1 | `43a69c5d324e`  |
| 3186   | Layout 1 | `43a69c5d324e`  |
| 3177   | Layout 1 | `43a69c5d324e`  |
| 3169   | Layout 1 | `43a69c5d324e`  |
| 3158   | Layout 1 | `43a69c5d324e`  |
| 3151   | Layout 1 | `43a69c5d324e`  |
| 3144   | Layout 1 | `43a69c5d324e`  |
| 3133   | Layout 1 | `43a69c5d324e`  |
| 3125   | Layout 1 | `43a69c5d324e`  |
| 3118   | Layout 1 | `43a69c5d324e`  |
| 3111   | Layout 1 | `43a69c5d324e`  |
| 3103   | Layout 1 | `43a69c5d324e`  |
| 3095   | Layout 1 | `43a69c5d324e`  |
| 3086   | Layout 1 | `43a69c5d324e`  |
| 3072   | Layout 1 | `43a69c5d324e`  |
| 3062   | Layout 1 | `43a69c5d324e`  |
| 3052   | Layout 1 | `43a69c5d324e`  |
| 3045   | Layout 1 | `43a69c5d324e`  |
| 3037   | Layout 1 | `43a69c5d324e`  |
| 3030   | Layout 1 | `43a69c5d324e`  |
| 3021   | Layout 1 | `43a69c5d324e`  |
| 3012   | Layout 1 | `43a69c5d324e`  |
| 3002   | Layout 1 | `43a69c5d324e`  |
| 2995   | Layout 1 | `43a69c5d324e`  |
| 2987   | Layout 1 | `43a69c5d324e`  |
| 2978   | Layout 1 | `43a69c5d324e`  |
| 2970   | Layout 1 | `43a69c5d324e`  |
| 2959   | Layout 1 | `43a69c5d324e`  |
| 2951   | Layout 1 | `43a69c5d324e`  |
| 2942   | Layout 1 | `43a69c5d324e`  |
| 2935   | Layout 1 | `43a69c5d324e`  |
| 2932   | Layout 1 | `43a69c5d324e`  |
| 2923   | Layout 1 | `43a69c5d324e`  |
| 2919   | Layout 1 | `43a69c5d324e`  |
| 2907   | Layout 1 | `43a69c5d324e`  |
| 2900   | Layout 1 | `43a69c5d324e`  |
| 2891   | Layout 1 | `43a69c5d324e`  |
| 2882   | Layout 1 | `43a69c5d324e`  |
| 2872   | Layout 1 | `43a69c5d324e`  |
| 2863   | Layout 1 | `43a69c5d324e`  |
| 2855   | Layout 1 | `43a69c5d324e`  |
| 2849   | Layout 1 | `43a69c5d324e`  |
| 2844   | Layout 1 | `43a69c5d324e`  |
| 2834   | Layout 1 | `43a69c5d324e`  |
| 2825   | Layout 1 | `43a69c5d324e`  |
| 2819   | Layout 1 | `43a69c5d324e`  |
| 2811   | Layout 1 | `43a69c5d324e`  |
| 2803   | Layout 1 | `43a69c5d324e`  |
| 2794   | Layout 1 | `43a69c5d324e`  |
| 2783   | Layout 1 | `43a69c5d324e`  |
| 2774   | Layout 1 | `43a69c5d324e`  |
| 2765   | Layout 1 | `43a69c5d324e`  |
| 2756   | Layout 1 | `43a69c5d324e`  |
| 2750   | Layout 1 | `43a69c5d324e`  |
| 2743   | Layout 1 | `43a69c5d324e`  |
| 2736   | Layout 1 | `43a69c5d324e`  |
| 2726   | Layout 1 | `43a69c5d324e`  |
| 2717   | Layout 1 | `43a69c5d324e`  |
| 2709   | Layout 1 | `43a69c5d324e`  |
| 2703   | Layout 1 | `43a69c5d324e`  |
| 2695   | Layout 1 | `43a69c5d324e`  |
| 2684   | Layout 1 | `43a69c5d324e`  |
| 2672   | Layout 1 | `43a69c5d324e`  |
| 2665   | Layout 1 | `43a69c5d324e`  |
| 2657   | Layout 1 | `43a69c5d324e`  |
| 2649   | Layout 1 | `43a69c5d324e`  |
| 2644   | Layout 1 | `43a69c5d324e`  |
| 2637   | Layout 1 | `43a69c5d324e`  |
| 2629   | Layout 1 | `43a69c5d324e`  |
| 2619   | Layout 1 | `43a69c5d324e`  |
| 2612   | Layout 1 | `43a69c5d324e`  |
| 2606   | Layout 1 | `43a69c5d324e`  |
| 2602   | Layout 1 | `43a69c5d324e`  |
| 2601   | Layout 1 | `43a69c5d324e`  |
| 2592   | Layout 1 | `43a69c5d324e`  |
| 2583   | Layout 1 | `43a69c5d324e`  |
| 2575   | Layout 1 | `43a69c5d324e`  |
| 2567   | Layout 1 | `43a69c5d324e`  |
| 2560   | Layout 1 | `43a69c5d324e`  |
| 2553   | Layout 1 | `43a69c5d324e`  |
| 2545   | Layout 1 | `43a69c5d324e`  |
| 2538   | Layout 1 | `43a69c5d324e`  |
| 2529   | Layout 1 | `43a69c5d324e`  |
| 2519   | Layout 1 | `43a69c5d324e`  |
| 2513   | Layout 1 | `43a69c5d324e`  |
| 2510   | Layout 1 | `43a69c5d324e`  |
| 2507   | Layout 1 | `43a69c5d324e`  |
| 2503   | Layout 1 | `43a69c5d324e`  |
| 2498   | Layout 1 | `43a69c5d324e`  |
| 2492   | Layout 1 | `43a69c5d324e`  |
| 2487   | Layout 1 | `43a69c5d324e`  |
| 2480   | Layout 1 | `43a69c5d324e`  |
| 2474   | Layout 1 | `43a69c5d324e`  |
| 2468   | Layout 1 | `43a69c5d324e`  |
| 2460   | Layout 1 | `43a69c5d324e`  |
| 2453   | Layout 1 | `43a69c5d324e`  |
| 2444   | Layout 1 | `43a69c5d324e`  |
| 2438   | Layout 1 | `43a69c5d324e`  |
| 2434   | Layout 1 | `43a69c5d324e`  |
| 2429   | Layout 1 | `43a69c5d324e`  |
| 2421   | Layout 1 | `43a69c5d324e`  |
| 2414   | Layout 1 | `43a69c5d324e`  |
| 2407   | Layout 1 | `43a69c5d324e`  |
| 2401   | Layout 1 | `43a69c5d324e`  |
| 2397   | Layout 1 | `43a69c5d324e`  |
| 2393   | Layout 1 | `43a69c5d324e`  |
| 2384   | Layout 1 | `43a69c5d324e`  |
| 2378   | Layout 1 | `43a69c5d324e`  |
| 2372   | Layout 1 | `43a69c5d324e`  |
| 2358   | Layout 1 | `43a69c5d324e`  |
| 2352   | Layout 1 | `43a69c5d324e`  |
| 2347   | Layout 1 | `43a69c5d324e`  |
| 2343   | Layout 1 | `43a69c5d324e`  |
| 2335   | Layout 1 | `43a69c5d324e`  |
| 2327   | Layout 1 | `43a69c5d324e`  |
| 2324   | Layout 1 | `43a69c5d324e`  |
| 2319   | Layout 1 | `43a69c5d324e`  |
| 2313   | Layout 1 | `43a69c5d324e`  |
| 2308   | Layout 1 | `43a69c5d324e`  |
| 2302   | Layout 1 | `43a69c5d324e`  |
| 2295   | Layout 1 | `43a69c5d324e`  |
| 2290   | Layout 1 | `43a69c5d324e`  |
| 2284   | Layout 1 | `43a69c5d324e`  |
| 2276   | Layout 1 | `43a69c5d324e`  |
| 2269   | Layout 1 | `43a69c5d324e`  |
| 2259   | Layout 1 | `43a69c5d324e`  |
| 2250   | Layout 1 | `43a69c5d324e`  |
| 2243   | Layout 1 | `43a69c5d324e`  |
| 2235   | Layout 1 | `43a69c5d324e`  |
| 2229   | Layout 1 | `43a69c5d324e`  |
| 2224   | Layout 1 | `43a69c5d324e`  |
| 2218   | Layout 1 | `43a69c5d324e`  |
| 2215   | Layout 1 | `43a69c5d324e`  |
| 2207   | Layout 1 | `43a69c5d324e`  |
| 2203   | Layout 1 | `43a69c5d324e`  |
| 2196   | Layout 1 | `43a69c5d324e`  |
| 2192   | Layout 1 | `43a69c5d324e`  |
| 2189   | Layout 1 | `43a69c5d324e`  |
| 2183   | Layout 1 | `43a69c5d324e`  |
| 2179   | Layout 1 | `43a69c5d324e`  |
| 2171   | Layout 1 | `43a69c5d324e`  |
| 2163   | Layout 1 | `43a69c5d324e`  |
| 2156   | Layout 1 | `43a69c5d324e`  |
| 2151   | Layout 1 | `43a69c5d324e`  |
| 2147   | Layout 1 | `43a69c5d324e`  |
| 2142   | Layout 1 | `43a69c5d324e`  |
| 2138   | Layout 1 | `43a69c5d324e`  |
| 2134   | Layout 1 | `43a69c5d324e`  |
| 2130   | Layout 1 | `43a69c5d324e`  |
| 2122   | Layout 1 | `43a69c5d324e`  |
| 2107   | Layout 1 | `43a69c5d324e`  |
| 2098   | Layout 1 | `43a69c5d324e`  |
| 2089   | Layout 1 | `43a69c5d324e`  |
| 2081   | Layout 1 | `43a69c5d324e`  |
| 2073   | Layout 1 | `43a69c5d324e`  |
| 2067   | Layout 1 | `43a69c5d324e`  |
| 2063   | Layout 1 | `43a69c5d324e`  |
| 2059   | Layout 1 | `43a69c5d324e`  |
| 2052   | Layout 1 | `43a69c5d324e`  |
| 2044   | Layout 1 | `43a69c5d324e`  |
| 2039   | Layout 1 | `43a69c5d324e`  |
| 2032   | Layout 1 | `43a69c5d324e`  |
| 2025   | Layout 1 | `43a69c5d324e`  |
| 2011   | Layout 1 | `43a69c5d324e`  |
| 2005   | Layout 1 | `43a69c5d324e`  |
| 2000   | Layout 1 | `43a69c5d324e`  |
| 1996   | Layout 1 | `43a69c5d324e`  |
| 1991   | Layout 1 | `43a69c5d324e`  |
| 1985   | Layout 1 | `43a69c5d324e`  |
| 1980   | Layout 1 | `43a69c5d324e`  |
| 1969   | Layout 1 | `43a69c5d324e`  |
| 1964   | Layout 1 | `43a69c5d324e`  |
| 1958   | Layout 1 | `43a69c5d324e`  |
| 1950   | Layout 1 | `43a69c5d324e`  |
| 1945   | No file  | `43a69c5d324e`  |
| 1937   | No file  | `43a69c5d324e`  |
| 1933   | No file  | `43a69c5d324e`  |
| 1927   | No file  | `43a69c5d324e`  |
| 1921   | No file  | `43a69c5d324e`  |
| 1914   | No file  | `43a69c5d324e`  |
| 1908   | No file  | `43a69c5d324e`  |
| 1897   | No file  | `43a69c5d324e`  |
| 1892   | No file  | `43a69c5d324e`  |
| 1886   | No file  | `43a69c5d324e`  |
| 1881   | No file  | `43a69c5d324e`  |
| 1871   | No file  | `43a69c5d324e`  |
| 1866   | No file  | `43a69c5d324e`  |
| 1862   | No file  | `43a69c5d324e`  |
| 1854   | No file  | `43a69c5d324e`  |
| 1846   | No file  | `43a69c5d324e`  |
| 1838   | No file  | `43a69c5d324e`  |
| 1832   | No file  | `43a69c5d324e`  |
| 1826   | No file  | `43a69c5d324e`  |
| 1822   | No file  | `43a69c5d324e`  |
| 1818   | No file  | `43a69c5d324e`  |
| 1804   | No file  | `43a69c5d324e`  |
| 1794   | No file  | `43a69c5d324e`  |
| 1790   | No file  | `43a69c5d324e`  |
| 1784   | No file  | `43a69c5d324e`  |
| 1774   | No file  | `43a69c5d324e`  |
| 1771   | No file  | `43a69c5d324e`  |
| 1762   | No file  | `43a69c5d324e`  |
| 1759   | No file  | `43a69c5d324e`  |
| 1754   | No file  | `43a69c5d324e`  |
| 1749   | No file  | `43a69c5d324e`  |
| 1743   | No file  | `43a69c5d324e`  |
| 1737   | No file  | `43a69c5d324e`  |
| 1731   | No file  | `43a69c5d324e`  |
| 1725   | No file  | `43a69c5d324e`  |
| 1717   | No file  | `43a69c5d324e`  |
| 1710   | No file  | `43a69c5d324e`  |
| 1704   | No file  | `43a69c5d324e`  |
| 1698   | No file  | `43a69c5d324e`  |
| 1690   | No file  | `43a69c5d324e`  |
| 1685   | No file  | `43a69c5d324e`  |
| 1680   | No file  | `43a69c5d324e`  |
| 1674   | No file  | `43a69c5d324e`  |
| 1668   | No file  | `43a69c5d324e`  |
| 1659   | No file  | `43a69c5d324e`  |
| 1649   | No file  | `43a69c5d324e`  |
| 1642   | No file  | `43a69c5d324e`  |
| 1636   | No file  | `43a69c5d324e`  |
| 1628   | No file  | `43a69c5d324e`  |
| 1622   | No file  | `43a69c5d324e`  |
| 1614   | No file  | `43a69c5d324e`  |
| 1608   | No file  | `43a69c5d324e`  |
| 1602   | No file  | `43a69c5d324e`  |
| 1598   | No file  | `43a69c5d324e`  |
| 1594   | No file  | `43a69c5d324e`  |
| 1590   | No file  | `43a69c5d324e`  |
| 1587   | No file  | `43a69c5d324e`  |
| 1584   | No file  | `43a69c5d324e`  |
| 1579   | No file  | `43a69c5d324e`  |
| 1572   | No file  | `43a69c5d324e`  |
| 1565   | No file  | `43a69c5d324e`  |
| 1559   | No file  | `43a69c5d324e`  |
| 1554   | No file  | `43a69c5d324e`  |
| 1547   | No file  | `43a69c5d324e`  |
| 1537   | No file  | `43a69c5d324e`  |
| 1529   | No file  | `43a69c5d324e`  |
| 1524   | No file  | `43a69c5d324e`  |
| 1519   | No file  | `43a69c5d324e`  |
| 1509   | No file  | `43a69c5d324e`  |
| 1506   | No file  | `43a69c5d324e`  |
| 1504   | No file  | `43a69c5d324e`  |
| 1500   | No file  | `43a69c5d324e`  |
| 1493   | No file  | `43a69c5d324e`  |
| 1489   | No file  | `43a69c5d324e`  |
| 1485   | No file  | `43a69c5d324e`  |
| 1481   | No file  | `43a69c5d324e`  |
| 1474   | No file  | `43a69c5d324e`  |
| 1466   | No file  | `43a69c5d324e`  |
| 1462   | No file  | `43a69c5d324e`  |
| 1459   | No file  | `43a69c5d324e`  |
| 1453   | No file  | `43a69c5d324e`  |
| 1450   | No file  | `43a69c5d324e`  |
| 1445   | No file  | `43a69c5d324e`  |
| 1439   | No file  | `43a69c5d324e`  |
| 1433   | No file  | `43a69c5d324e`  |
| 1430   | No file  | `43a69c5d324e`  |
| 1426   | No file  | `43a69c5d324e`  |
| 1421   | No file  | `43a69c5d324e`  |
| 1417   | No file  | `43a69c5d324e`  |
| 1416   | No file  | `43a69c5d324e`  |
| 1409   | No file  | `43a69c5d324e`  |
| 1405   | No file  | `43a69c5d324e`  |
| 1401   | No file  | `43a69c5d324e`  |
| 1396   | No file  | `43a69c5d324e`  |
| 1391   | No file  | `43a69c5d324e`  |
| 1390   | No file  | `43a69c5d324e`  |
| 1386   | No file  | `43a69c5d324e`  |
| 1381   | No file  | `43a69c5d324e`  |
| 1379   | No file  | `43a69c5d324e`  |
| 1372   | No file  | `43a69c5d324e`  |
| 1366   | No file  | `43a69c5d324e`  |
| 1364   | No file  | `43a69c5d324e`  |
| 1363   | No file  | `43a69c5d324e`  |
| 1360   | No file  | `43a69c5d324e`  |
| 1358   | No file  | `43a69c5d324e`  |
| 1355   | No file  | `43a69c5d324e`  |
| 1351   | No file  | `43a69c5d324e`  |
| 1348   | No file  | `43a69c5d324e`  |
| 1346   | No file  | `43a69c5d324e`  |
| 1341   | No file  | `43a69c5d324e`  |
| 1340   | No file  | `43a69c5d324e`  |
| 1338   | No file  | `43a69c5d324e`  |
| 1335   | No file  | `43a69c5d324e`  |
| 1333   | No file  | `43a69c5d324e`  |
| 1329   | No file  | `43a69c5d324e`  |
| 1327   | No file  | `43a69c5d324e`  |
| 1324   | No file  | `43a69c5d324e`  |
| 1321   | No file  | `43a69c5d324e`  |
| 1319   | No file  | `43a69c5d324e`  |
| 1318   | No file  | `43a69c5d324e`  |
| 1316   | No file  | `43a69c5d324e`  |
| 1313   | No file  | `43a69c5d324e`  |
| 1311   | No file  | `43a69c5d324e`  |
| 1309   | No file  | `43a69c5d324e`  |
| 1304   | No file  | `43a69c5d324e`  |
| 1292   | No file  | `43a69c5d324e`  |
| 1286   | No file  | `43a69c5d324e`  |
| 1280   | No file  | `43a69c5d324e`  |
| 1276   | No file  | `43a69c5d324e`  |
| 1267   | No file  | `43a69c5d324e`  |
| 1261   | No file  | `43a69c5d324e`  |
| 1256   | No file  | `43a69c5d324e`  |
| 1250   | No file  | `43a69c5d324e`  |
| 1246   | No file  | `43a69c5d324e`  |
| 1239   | No file  | `43a69c5d324e`  |
| 1230   | No file  | `43a69c5d324e`  |
| 1226   | No file  | `43a69c5d324e`  |
| 1220   | No file  | `43a69c5d324e`  |
| 1217   | No file  | `43a69c5d324e`  |
| 1211   | No file  | `43a69c5d324e`  |
| 1210   | No file  | `43a69c5d324e`  |
| 1208   | No file  | `43a69c5d324e`  |
| 1203   | No file  | `43a69c5d324e`  |
| 1197   | No file  | `43a69c5d324e`  |
| 1194   | No file  | `43a69c5d324e`  |
| 1192   | No file  | `43a69c5d324e`  |
| 1187   | No file  | `43a69c5d324e`  |
| 1183   | No file  | `43a69c5d324e`  |
| 1177   | No file  | `43a69c5d324e`  |
| 1173   | No file  | `43a69c5d324e`  |
| 1167   | No file  | `43a69c5d324e`  |
| 1164   | No file  | `43a69c5d324e`  |
| 1156   | No file  | `43a69c5d324e`  |
| 1149   | No file  | `43a69c5d324e`  |
| 1144   | No file  | `43a69c5d324e`  |
| 1137   | No file  | `43a69c5d324e`  |
| 1132   | No file  | `43a69c5d324e`  |
| 1127   | No file  | `43a69c5d324e`  |
| 1122   | No file  | `43a69c5d324e`  |
| 1118   | No file  | `43a69c5d324e`  |
| 1114   | No file  | `43a69c5d324e`  |
| 1109   | No file  | `43a69c5d324e`  |
| 1102   | No file  | `43a69c5d324e`  |
| 1096   | No file  | `43a69c5d324e`  |
| 1088   | No file  | `43a69c5d324e`  |
| 1081   | No file  | `43a69c5d324e`  |
| 1076   | No file  | `43a69c5d324e`  |
| 1069   | No file  | `43a69c5d324e`  |
| 1064   | No file  | `43a69c5d324e`  |
| 1058   | No file  | `43a69c5d324e`  |
| 1051   | No file  | `43a69c5d324e`  |
| 1044   | No file  | `43a69c5d324e`  |
| 1036   | No file  | `43a69c5d324e`  |
| 1026   | No file  | `43a69c5d324e`  |
| 1016   | No file  | `43a69c5d324e`  |
| 1009   | No file  | `43a69c5d324e`  |
| 1005   | No file  | `43a69c5d324e`  |
| 1000   | No file  | `43a69c5d324e`  |
| 998    | No file  | `43a69c5d324e`  |
| 990    | No file  | `43a69c5d324e`  |
| 979    | No file  | `43a69c5d324e`  |
| 972    | No file  | `43a69c5d324e`  |
| 963    | No file  | `43a69c5d324e`  |
| 955    | No file  | `43a69c5d324e`  |
| 946    | No file  | `43a69c5d324e`  |
| 938    | No file  | `43a69c5d324e`  |
| 927    | No file  | `43a69c5d324e`  |
| 911    | No file  | `43a69c5d324e`  |
| 904    | No file  | `43a69c5d324e`  |
| 899    | No file  | `43a69c5d324e`  |
| 894    | No file  | `43a69c5d324e`  |
| 885    | No file  | `43a69c5d324e`  |
| 879    | No file  | `43a69c5d324e`  |
| 872    | No file  | `43a69c5d324e`  |
| 864    | No file  | `43a69c5d324e`  |
| 855    | No file  | `43a69c5d324e`  |
| 853    | No file  | `43a69c5d324e`  |
| 845    | No file  | `43a69c5d324e`  |
| 837    | No file  | `43a69c5d324e`  |
| 829    | No file  | `43a69c5d324e`  |
| 822    | No file  | `43a69c5d324e`  |
| 814    | No file  | `43a69c5d324e`  |
| 805    | No file  | `43a69c5d324e`  |
| 794    | No file  | `43a69c5d324e`  |
| 787    | No file  | `43a69c5d324e`  |
| 780    | No file  | `43a69c5d324e`  |
| 771    | No file  | `43a69c5d324e`  |
| 760    | No file  | `43a69c5d324e`  |
| 748    | No file  | `43a69c5d324e`  |
| 741    | No file  | `43a69c5d324e`  |
| 736    | No file  | `43a69c5d324e`  |
| 731    | No file  | `43a69c5d324e`  |
| 723    | No file  | `43a69c5d324e`  |
| 711    | No file  | `43a69c5d324e`  |
| 707    | No file  | `43a69c5d324e`  |
| 697    | No file  | `43a69c5d324e`  |
| 689    | No file  | `43a69c5d324e`  |
| 683    | No file  | `43a69c5d324e`  |
| 678    | No file  | `43a69c5d324e`  |
| 670    | No file  | `43a69c5d324e`  |
| 661    | No file  | `43a69c5d324e`  |
| 656    | No file  | `43a69c5d324e`  |
| 652    | No file  | `43a69c5d324e`  |
| 643    | No file  | `43a69c5d324e`  |
| 637    | No file  | `43a69c5d324e`  |
| 630    | No file  | `43a69c5d324e`  |
| 627    | No file  | `43a69c5d324e`  |
| 621    | No file  | `43a69c5d324e`  |
| 617    | No file  | `43a69c5d324e`  |
| 615    | No file  | `43a69c5d324e`  |
| 606    | No file  | `43a69c5d324e`  |
| 599    | No file  | `43a69c5d324e`  |
| 592    | No file  | `43a69c5d324e`  |
| 586    | No file  | `43a69c5d324e`  |
| 577    | No file  | `43a69c5d324e`  |
| 569    | No file  | `43a69c5d324e`  |
| 561    | No file  | `43a69c5d324e`  |
| 554    | No file  | `43a69c5d324e`  |
| 542    | No file  | `43a69c5d324e`  |
| 532    | No file  | `43a69c5d324e`  |
| 531    | No file  | `43a69c5d324e`  |
| 526    | No file  | `43a69c5d324e`  |
| 521    | No file  | `43a69c5d324e`  |
| 517    | No file  | `43a69c5d324e`  |
| 510    | No file  | `43a69c5d324e`  |
| 508    | No file  | `43a69c5d324e`  |
| 504    | No file  | `43a69c5d324e`  |
| 497    | No file  | `43a69c5d324e`  |
| 491    | No file  | `43a69c5d324e`  |
| 485    | No file  | `43a69c5d324e`  |
| 478    | No file  | `43a69c5d324e`  |
| 472    | No file  | `43a69c5d324e`  |
| 466    | No file  | `43a69c5d324e`  |
| 457    | No file  | `43a69c5d324e`  |
| 452    | No file  | `43a69c5d324e`  |
| 449    | No file  | `43a69c5d324e`  |
| 435    | No file  | `43a69c5d324e`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone; it shows the icon from
`texturestring_combine.xml` when that file is there.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of slots; `16` on client 3482          |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (40 bytes)

Every `*_ref` field is an index into `strings`.

| Offset  | Type   | Field                    | Notes |
| ------- | ------ | ------------------------ | ----- |
| `+0x00` | u32    | roadmap_key              | Slot key, `1` to `16` in file order on client 3482 |
| `+0x04` | u32    | title_ref                | `getTitle()`: Korean slot title (`메인 의뢰`, `시즌 패스`) |
| `+0x08` | u32    | desc_ref                 | `getDesc()`: Korean slot text |
| `+0x0C` | u32    | event_name_ref           | `getEventName()`: Korean text of the event button; empty on the 14 slots without an event |
| `+0x10` | u32    | icon_texture_id_ref      | `getIconTextureId()`: UI texture ID (`Combine_Etc_SeasonMap_01_Slot_Title_1` to `_6`) |
| `+0x14` | u32    | background_texture_id_ref | `getBackGroundTextureId()`: UI texture ID; the Lua adds `_Over` and `_Click` for the other two button states |
| `+0x18` | u32    | character_texture_id_ref | `getCharacterTextureId()`: `Combine_RoadMap_CharacterTexture_00` on every slot |
| `+0x1C` | i32[3] | event_parameters         | `getEventParameter(i)`; `-1` where unused. See [Events](#events) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `45` on client 3482    |
| `+0x04` | pstr[string_count] | strings      | Each text is stored once                  |

## Events

`processRoadMapEvent` in `panel_window_beginnerroadmap_1.luac` reads the
first parameter as the event category and asserts on `-1`. Category `1`
opens a UI window named by the second parameter; category `2` has no code.

| Parameters    | Slots (client 3482)          | Lua action                                   |
| ------------- | ---------------------------- | -------------------------------------------- |
| `1, 1, -1`    | `1` (`의뢰 UI 바로가기`)      | Quest window on the main quest tab           |
| `1, 2, -1`    | `3` (`흑정령 부르기`)          | Closes the roadmap, opens the Black Spirit   |
| `-1, -1, -1`  | the other 14                 | No event button (`isHaveEvent()` false)      |

## Field Names

The names follow the getters of the wrapper in
`panel_window_beginnerroadmap_1.luac` (client 3482): `getTitle()`,
`getDesc()`, `getEventName()`, `getIconTextureId()`,
`getBackGroundTextureId()`, `getCharacterTextureId()` and
`getEventParameterCount()` / `getEventParameter(i)`. The three texture
fields are told apart by their IDs (`_Slot_Title_`, `_Slot_BG_`,
`_CharacterTexture_`). Client 1784 has no file and no matching sheet.

## Notes

- `getAdventureNoteURL()` has no field in this file; on client 3482
  `beginnerroadmaplinkurldata.bss` is an empty table.
