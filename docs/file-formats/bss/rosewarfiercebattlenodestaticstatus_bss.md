# `rosewarfiercebattlenodestaticstatus.bss` Format

## Purpose

The links between the Rose War sanctums: one row per fierce battle key with
four u64-counted lists of fierce battle keys, the key itself last. The
first two lists hold the neighbouring sanctums toward the Kamasylvia end
(sanctum `1`) and toward the O'dyllita end (sanctum `11`). On client 3474
sanctums `1` to `7` and `11` to `17` form two lanes per side that meet at
`4`, `7`, `14` and `17`; `8` to `10`, `18` to `20` and the gimmick
sanctums `21` and `22` have empty lists.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                      | Bytes | Records | Row bytes               |
| ------ | -------------- | ----------------------------------------- | ----- | ------- | ----------------------- |
| 1      | 2575 and later | `rosewarfiercebattlenodestaticstatus.bss` | 880   | 22 Row  | 34 to 44, 39 on average |

| Layout | File                                      | Known         | Unknown       |
| ------ | ----------------------------------------- | ------------- | ------------- |
| 1      | `rosewarfiercebattlenodestaticstatus.bss` | 480 B (54.5%) | 400 B (45.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `eec03bd1cc3c`  |
| 3482   | Layout 1             | `eec03bd1cc3c`  |
| 3474   | Layout 1             | `eec03bd1cc3c`  |
| 3473   | Layout 1             | `eec03bd1cc3c`  |
| 3464   | Layout 1             | `eec03bd1cc3c`  |
| 3458   | Layout 1             | `eec03bd1cc3c`  |
| 3454   | Layout 1             | `eec03bd1cc3c`  |
| 3444   | Layout 1             | `eec03bd1cc3c`  |
| 3435   | Layout 1             | `eec03bd1cc3c`  |
| 3426   | Layout 1             | `eec03bd1cc3c`  |
| 3418   | Layout 1             | `eec03bd1cc3c`  |
| 3412   | Layout 1             | `eec03bd1cc3c`  |
| 3402   | Layout 1             | `eec03bd1cc3c`  |
| 3396   | Layout 1             | `eec03bd1cc3c`  |
| 3387   | Layout 1             | `eec03bd1cc3c`  |
| 3381   | Layout 1             | `eec03bd1cc3c`  |
| 3373   | Layout 1             | `eec03bd1cc3c`  |
| 3364   | Layout 1             | `eec03bd1cc3c`  |
| 3356   | Layout 1             | `eec03bd1cc3c`  |
| 3349   | Layout 1             | `eec03bd1cc3c`  |
| 3342   | Layout 1             | `eec03bd1cc3c`  |
| 3335   | Layout 1             | `eec03bd1cc3c`  |
| 3326   | Layout 1             | `eec03bd1cc3c`  |
| 3321   | Layout 1             | `eec03bd1cc3c`  |
| 3314   | Layout 1             | `eec03bd1cc3c`  |
| 3303   | Layout 1             | `eec03bd1cc3c`  |
| 3302   | Layout 1             | `eec03bd1cc3c`  |
| 3293   | Layout 1             | `eec03bd1cc3c`  |
| 3283   | Layout 1             | `eec03bd1cc3c`  |
| 3275   | Layout 1             | `eec03bd1cc3c`  |
| 3267   | Layout 1             | `eec03bd1cc3c`  |
| 3258   | Layout 1             | `eec03bd1cc3c`  |
| 3251   | Layout 1             | `eec03bd1cc3c`  |
| 3242   | Layout 1             | `eec03bd1cc3c`  |
| 3235   | Layout 1             | `eec03bd1cc3c`  |
| 3229   | Layout 1             | `eec03bd1cc3c`  |
| 3212   | Layout 1             | `eec03bd1cc3c`  |
| 3203   | Layout 1             | `eec03bd1cc3c`  |
| 3193   | Layout 1             | `eec03bd1cc3c`  |
| 3186   | Layout 1             | `eec03bd1cc3c`  |
| 3177   | Layout 1             | `eec03bd1cc3c`  |
| 3169   | Layout 1             | `eec03bd1cc3c`  |
| 3158   | Layout 1             | `eec03bd1cc3c`  |
| 3151   | Layout 1             | `eec03bd1cc3c`  |
| 3144   | Layout 1             | `eec03bd1cc3c`  |
| 3133   | Layout 1             | `eec03bd1cc3c`  |
| 3125   | Layout 1             | `eec03bd1cc3c`  |
| 3118   | Layout 1             | `eec03bd1cc3c`  |
| 3111   | Layout 1             | `eec03bd1cc3c`  |
| 3103   | Layout 1             | `eec03bd1cc3c`  |
| 3095   | Layout 1             | `eec03bd1cc3c`  |
| 3086   | Layout 1             | `eec03bd1cc3c`  |
| 3072   | Layout 1             | `eec03bd1cc3c`  |
| 3062   | Layout 1             | `eec03bd1cc3c`  |
| 3052   | Layout 1             | `eec03bd1cc3c`  |
| 3045   | Layout 1             | `eec03bd1cc3c`  |
| 3037   | Layout 1             | `eec03bd1cc3c`  |
| 3030   | Layout 1             | `eec03bd1cc3c`  |
| 3021   | Layout 1             | `eec03bd1cc3c`  |
| 3012   | Layout 1             | `eec03bd1cc3c`  |
| 3002   | Layout 1             | `eec03bd1cc3c`  |
| 2995   | Layout 1             | `eec03bd1cc3c`  |
| 2987   | Layout 1             | `eec03bd1cc3c`  |
| 2978   | Layout 1             | `eec03bd1cc3c`  |
| 2970   | Layout 1             | `eec03bd1cc3c`  |
| 2959   | Layout 1             | `eec03bd1cc3c`  |
| 2951   | Layout 1             | `eec03bd1cc3c`  |
| 2942   | Layout 1             | `eec03bd1cc3c`  |
| 2935   | Layout 1             | `eec03bd1cc3c`  |
| 2932   | Layout 1             | `eec03bd1cc3c`  |
| 2923   | Layout 1             | `eec03bd1cc3c`  |
| 2919   | Layout 1             | `eec03bd1cc3c`  |
| 2907   | Layout 1             | `eec03bd1cc3c`  |
| 2900   | Layout 1             | `eec03bd1cc3c`  |
| 2891   | Layout 1             | `eec03bd1cc3c`  |
| 2882   | Layout 1             | `eec03bd1cc3c`  |
| 2872   | Layout 1             | `eec03bd1cc3c`  |
| 2863   | Layout 1             | `eec03bd1cc3c`  |
| 2855   | Layout 1             | `eec03bd1cc3c`  |
| 2849   | Layout 1             | `eec03bd1cc3c`  |
| 2844   | Layout 1             | `eec03bd1cc3c`  |
| 2834   | Layout 1             | `eec03bd1cc3c`  |
| 2825   | Layout 1             | `eec03bd1cc3c`  |
| 2819   | Layout 1             | `eec03bd1cc3c`  |
| 2811   | Layout 1             | `eec03bd1cc3c`  |
| 2803   | Layout 1             | `eec03bd1cc3c`  |
| 2794   | Layout 1             | `eec03bd1cc3c`  |
| 2783   | Layout 1             | `eec03bd1cc3c`  |
| 2774   | Layout 1             | `eec03bd1cc3c`  |
| 2765   | Layout 1             | `eec03bd1cc3c`  |
| 2756   | Layout 1             | `eec03bd1cc3c`  |
| 2750   | Layout 1             | `eec03bd1cc3c`  |
| 2743   | Layout 1             | `eec03bd1cc3c`  |
| 2736   | Layout 1             | `eec03bd1cc3c`  |
| 2726   | Layout 1             | `eec03bd1cc3c`  |
| 2717   | Layout 1             | `eec03bd1cc3c`  |
| 2709   | Layout 1             | `eec03bd1cc3c`  |
| 2703   | Layout 1             | `eec03bd1cc3c`  |
| 2695   | Layout 1             | `eec03bd1cc3c`  |
| 2684   | Layout 1             | `eec03bd1cc3c`  |
| 2672   | Layout 1             | `eec03bd1cc3c`  |
| 2665   | Layout 1             | `eec03bd1cc3c`  |
| 2657   | Layout 1             | `eec03bd1cc3c`  |
| 2649   | Layout 1             | `eec03bd1cc3c`  |
| 2644   | Layout 1             | `eec03bd1cc3c`  |
| 2637   | Layout 1             | `eec03bd1cc3c`  |
| 2629   | Layout 1             | `eec03bd1cc3c`  |
| 2619   | Layout 1             | `eec03bd1cc3c`  |
| 2612   | Layout 1             | `eec03bd1cc3c`  |
| 2606   | Layout 1             | `eec03bd1cc3c`  |
| 2602   | Layout 1             | `eec03bd1cc3c`  |
| 2601   | Layout 1             | `eec03bd1cc3c`  |
| 2592   | Layout 1             | `eec03bd1cc3c`  |
| 2583   | Layout 1             | `eec03bd1cc3c`  |
| 2575   | Layout 1             | `eec03bd1cc3c`  |
| 2567   | No documented layout | `eec03bd1cc3c`  |
| 2560   | No documented layout | `eec03bd1cc3c`  |
| 2553   | No documented layout | `eec03bd1cc3c`  |
| 2545   | No documented layout | `eec03bd1cc3c`  |
| 2538   | No file              | `eec03bd1cc3c`  |
| 2529   | No file              | `eec03bd1cc3c`  |
| 2519   | No file              | `eec03bd1cc3c`  |
| 2513   | No file              | `eec03bd1cc3c`  |
| 2510   | No file              | `eec03bd1cc3c`  |
| 2507   | No file              | `eec03bd1cc3c`  |
| 2503   | No file              | `eec03bd1cc3c`  |
| 2498   | No file              | `eec03bd1cc3c`  |
| 2492   | No file              | `eec03bd1cc3c`  |
| 2487   | No file              | `eec03bd1cc3c`  |
| 2480   | No file              | `eec03bd1cc3c`  |
| 2474   | No file              | `eec03bd1cc3c`  |
| 2468   | No file              | `eec03bd1cc3c`  |
| 2460   | No file              | `eec03bd1cc3c`  |
| 2453   | No file              | `eec03bd1cc3c`  |
| 2444   | No file              | `eec03bd1cc3c`  |
| 2438   | No file              | `eec03bd1cc3c`  |
| 2434   | No file              | `eec03bd1cc3c`  |
| 2429   | No file              | `eec03bd1cc3c`  |
| 2421   | No file              | `eec03bd1cc3c`  |
| 2414   | No file              | `eec03bd1cc3c`  |
| 2407   | No file              | `eec03bd1cc3c`  |
| 2401   | No file              | `eec03bd1cc3c`  |
| 2397   | No file              | `eec03bd1cc3c`  |
| 2393   | No file              | `eec03bd1cc3c`  |
| 2384   | No file              | `eec03bd1cc3c`  |
| 2378   | No file              | `eec03bd1cc3c`  |
| 2372   | No file              | `eec03bd1cc3c`  |
| 2358   | No file              | `eec03bd1cc3c`  |
| 2352   | No file              | `eec03bd1cc3c`  |
| 2347   | No file              | `eec03bd1cc3c`  |
| 2343   | No file              | `eec03bd1cc3c`  |
| 2335   | No file              | `eec03bd1cc3c`  |
| 2327   | No file              | `eec03bd1cc3c`  |
| 2324   | No file              | `eec03bd1cc3c`  |
| 2319   | No file              | `eec03bd1cc3c`  |
| 2313   | No file              | `eec03bd1cc3c`  |
| 2308   | No file              | `eec03bd1cc3c`  |
| 2302   | No file              | `eec03bd1cc3c`  |
| 2295   | No file              | `eec03bd1cc3c`  |
| 2290   | No file              | `eec03bd1cc3c`  |
| 2284   | No file              | `eec03bd1cc3c`  |
| 2276   | No file              | `eec03bd1cc3c`  |
| 2269   | No file              | `eec03bd1cc3c`  |
| 2259   | No file              | `eec03bd1cc3c`  |
| 2250   | No file              | `eec03bd1cc3c`  |
| 2243   | No file              | `eec03bd1cc3c`  |
| 2235   | No file              | `eec03bd1cc3c`  |
| 2229   | No file              | `eec03bd1cc3c`  |
| 2224   | No file              | `eec03bd1cc3c`  |
| 2218   | No file              | `eec03bd1cc3c`  |
| 2215   | No file              | `eec03bd1cc3c`  |
| 2207   | No file              | `eec03bd1cc3c`  |
| 2203   | No file              | `eec03bd1cc3c`  |
| 2196   | No file              | `eec03bd1cc3c`  |
| 2192   | No file              | `eec03bd1cc3c`  |
| 2189   | No file              | `eec03bd1cc3c`  |
| 2183   | No file              | `eec03bd1cc3c`  |
| 2179   | No file              | `eec03bd1cc3c`  |
| 2171   | No file              | `eec03bd1cc3c`  |
| 2163   | No file              | `eec03bd1cc3c`  |
| 2156   | No file              | `eec03bd1cc3c`  |
| 2151   | No file              | `eec03bd1cc3c`  |
| 2147   | No file              | `eec03bd1cc3c`  |
| 2142   | No file              | `eec03bd1cc3c`  |
| 2138   | No file              | `eec03bd1cc3c`  |
| 2134   | No file              | `eec03bd1cc3c`  |
| 2130   | No file              | `eec03bd1cc3c`  |
| 2122   | No file              | `eec03bd1cc3c`  |
| 2107   | No file              | `eec03bd1cc3c`  |
| 2098   | No file              | `eec03bd1cc3c`  |
| 2089   | No file              | `eec03bd1cc3c`  |
| 2081   | No file              | `eec03bd1cc3c`  |
| 2073   | No file              | `eec03bd1cc3c`  |
| 2067   | No file              | `eec03bd1cc3c`  |
| 2063   | No file              | `eec03bd1cc3c`  |
| 2059   | No file              | `eec03bd1cc3c`  |
| 2052   | No file              | `eec03bd1cc3c`  |
| 2044   | No file              | `eec03bd1cc3c`  |
| 2039   | No file              | `eec03bd1cc3c`  |
| 2032   | No file              | `eec03bd1cc3c`  |
| 2025   | No file              | `eec03bd1cc3c`  |
| 2011   | No file              | `eec03bd1cc3c`  |
| 2005   | No file              | `eec03bd1cc3c`  |
| 2000   | No file              | `eec03bd1cc3c`  |
| 1996   | No file              | `eec03bd1cc3c`  |
| 1991   | No file              | `eec03bd1cc3c`  |
| 1985   | No file              | `eec03bd1cc3c`  |
| 1980   | No file              | `eec03bd1cc3c`  |
| 1969   | No file              | `eec03bd1cc3c`  |
| 1964   | No file              | `eec03bd1cc3c`  |
| 1958   | No file              | `eec03bd1cc3c`  |
| 1950   | No file              | `eec03bd1cc3c`  |
| 1945   | No file              | `eec03bd1cc3c`  |
| 1937   | No file              | `eec03bd1cc3c`  |
| 1933   | No file              | `eec03bd1cc3c`  |
| 1927   | No file              | `eec03bd1cc3c`  |
| 1921   | No file              | `eec03bd1cc3c`  |
| 1914   | No file              | `eec03bd1cc3c`  |
| 1908   | No file              | `eec03bd1cc3c`  |
| 1897   | No file              | `eec03bd1cc3c`  |
| 1892   | No file              | `eec03bd1cc3c`  |
| 1886   | No file              | `eec03bd1cc3c`  |
| 1881   | No file              | `eec03bd1cc3c`  |
| 1871   | No file              | `eec03bd1cc3c`  |
| 1866   | No file              | `eec03bd1cc3c`  |
| 1862   | No file              | `eec03bd1cc3c`  |
| 1854   | No file              | `eec03bd1cc3c`  |
| 1846   | No file              | `eec03bd1cc3c`  |
| 1838   | No file              | `eec03bd1cc3c`  |
| 1832   | No file              | `eec03bd1cc3c`  |
| 1826   | No file              | `eec03bd1cc3c`  |
| 1822   | No file              | `eec03bd1cc3c`  |
| 1818   | No file              | `eec03bd1cc3c`  |
| 1804   | No file              | `eec03bd1cc3c`  |
| 1794   | No file              | `eec03bd1cc3c`  |
| 1790   | No file              | `eec03bd1cc3c`  |
| 1784   | No file              | `eec03bd1cc3c`  |
| 1774   | No file              | `eec03bd1cc3c`  |
| 1771   | No file              | `eec03bd1cc3c`  |
| 1762   | No file              | `eec03bd1cc3c`  |
| 1759   | No file              | `eec03bd1cc3c`  |
| 1754   | No file              | `eec03bd1cc3c`  |
| 1749   | No file              | `eec03bd1cc3c`  |
| 1743   | No file              | `eec03bd1cc3c`  |
| 1737   | No file              | `eec03bd1cc3c`  |
| 1731   | No file              | `eec03bd1cc3c`  |
| 1725   | No file              | `eec03bd1cc3c`  |
| 1717   | No file              | `eec03bd1cc3c`  |
| 1710   | No file              | `eec03bd1cc3c`  |
| 1704   | No file              | `eec03bd1cc3c`  |
| 1698   | No file              | `eec03bd1cc3c`  |
| 1690   | No file              | `eec03bd1cc3c`  |
| 1685   | No file              | `eec03bd1cc3c`  |
| 1680   | No file              | `eec03bd1cc3c`  |
| 1674   | No file              | `eec03bd1cc3c`  |
| 1668   | No file              | `eec03bd1cc3c`  |
| 1659   | No file              | `eec03bd1cc3c`  |
| 1649   | No file              | `eec03bd1cc3c`  |
| 1642   | No file              | `eec03bd1cc3c`  |
| 1636   | No file              | `eec03bd1cc3c`  |
| 1628   | No file              | `eec03bd1cc3c`  |
| 1622   | No file              | `eec03bd1cc3c`  |
| 1614   | No file              | `eec03bd1cc3c`  |
| 1608   | No file              | `eec03bd1cc3c`  |
| 1602   | No file              | `eec03bd1cc3c`  |
| 1598   | No file              | `eec03bd1cc3c`  |
| 1594   | No file              | `eec03bd1cc3c`  |
| 1590   | No file              | `eec03bd1cc3c`  |
| 1587   | No file              | `eec03bd1cc3c`  |
| 1584   | No file              | `eec03bd1cc3c`  |
| 1579   | No file              | `eec03bd1cc3c`  |
| 1572   | No file              | `eec03bd1cc3c`  |
| 1565   | No file              | `eec03bd1cc3c`  |
| 1559   | No file              | `eec03bd1cc3c`  |
| 1554   | No file              | `eec03bd1cc3c`  |
| 1547   | No file              | `eec03bd1cc3c`  |
| 1537   | No file              | `eec03bd1cc3c`  |
| 1529   | No file              | `eec03bd1cc3c`  |
| 1524   | No file              | `eec03bd1cc3c`  |
| 1519   | No file              | `eec03bd1cc3c`  |
| 1509   | No file              | `eec03bd1cc3c`  |
| 1506   | No file              | `eec03bd1cc3c`  |
| 1504   | No file              | `eec03bd1cc3c`  |
| 1500   | No file              | `eec03bd1cc3c`  |
| 1493   | No file              | `eec03bd1cc3c`  |
| 1489   | No file              | `eec03bd1cc3c`  |
| 1485   | No file              | `eec03bd1cc3c`  |
| 1481   | No file              | `eec03bd1cc3c`  |
| 1474   | No file              | `eec03bd1cc3c`  |
| 1466   | No file              | `eec03bd1cc3c`  |
| 1462   | No file              | `eec03bd1cc3c`  |
| 1459   | No file              | `eec03bd1cc3c`  |
| 1453   | No file              | `eec03bd1cc3c`  |
| 1450   | No file              | `eec03bd1cc3c`  |
| 1445   | No file              | `eec03bd1cc3c`  |
| 1439   | No file              | `eec03bd1cc3c`  |
| 1433   | No file              | `eec03bd1cc3c`  |
| 1430   | No file              | `eec03bd1cc3c`  |
| 1426   | No file              | `eec03bd1cc3c`  |
| 1421   | No file              | `eec03bd1cc3c`  |
| 1417   | No file              | `eec03bd1cc3c`  |
| 1416   | No file              | `eec03bd1cc3c`  |
| 1409   | No file              | `eec03bd1cc3c`  |
| 1405   | No file              | `eec03bd1cc3c`  |
| 1401   | No file              | `eec03bd1cc3c`  |
| 1396   | No file              | `eec03bd1cc3c`  |
| 1391   | No file              | `eec03bd1cc3c`  |
| 1390   | No file              | `eec03bd1cc3c`  |
| 1386   | No file              | `eec03bd1cc3c`  |
| 1381   | No file              | `eec03bd1cc3c`  |
| 1379   | No file              | `eec03bd1cc3c`  |
| 1372   | No file              | `eec03bd1cc3c`  |
| 1366   | No file              | `eec03bd1cc3c`  |
| 1364   | No file              | `eec03bd1cc3c`  |
| 1363   | No file              | `eec03bd1cc3c`  |
| 1360   | No file              | `eec03bd1cc3c`  |
| 1358   | No file              | `eec03bd1cc3c`  |
| 1355   | No file              | `eec03bd1cc3c`  |
| 1351   | No file              | `eec03bd1cc3c`  |
| 1348   | No file              | `eec03bd1cc3c`  |
| 1346   | No file              | `eec03bd1cc3c`  |
| 1341   | No file              | `eec03bd1cc3c`  |
| 1340   | No file              | `eec03bd1cc3c`  |
| 1338   | No file              | `eec03bd1cc3c`  |
| 1335   | No file              | `eec03bd1cc3c`  |
| 1333   | No file              | `eec03bd1cc3c`  |
| 1329   | No file              | `eec03bd1cc3c`  |
| 1327   | No file              | `eec03bd1cc3c`  |
| 1324   | No file              | `eec03bd1cc3c`  |
| 1321   | No file              | `eec03bd1cc3c`  |
| 1319   | No file              | `eec03bd1cc3c`  |
| 1318   | No file              | `eec03bd1cc3c`  |
| 1316   | No file              | `eec03bd1cc3c`  |
| 1313   | No file              | `eec03bd1cc3c`  |
| 1311   | No file              | `eec03bd1cc3c`  |
| 1309   | No file              | `eec03bd1cc3c`  |
| 1304   | No file              | `eec03bd1cc3c`  |
| 1292   | No file              | `eec03bd1cc3c`  |
| 1286   | No file              | `eec03bd1cc3c`  |
| 1280   | No file              | `eec03bd1cc3c`  |
| 1276   | No file              | `eec03bd1cc3c`  |
| 1267   | No file              | `eec03bd1cc3c`  |
| 1261   | No file              | `eec03bd1cc3c`  |
| 1256   | No file              | `eec03bd1cc3c`  |
| 1250   | No file              | `eec03bd1cc3c`  |
| 1246   | No file              | `eec03bd1cc3c`  |
| 1239   | No file              | `eec03bd1cc3c`  |
| 1230   | No file              | `eec03bd1cc3c`  |
| 1226   | No file              | `eec03bd1cc3c`  |
| 1220   | No file              | `eec03bd1cc3c`  |
| 1217   | No file              | `eec03bd1cc3c`  |
| 1211   | No file              | `eec03bd1cc3c`  |
| 1210   | No file              | `eec03bd1cc3c`  |
| 1208   | No file              | `eec03bd1cc3c`  |
| 1203   | No file              | `eec03bd1cc3c`  |
| 1197   | No file              | `eec03bd1cc3c`  |
| 1194   | No file              | `eec03bd1cc3c`  |
| 1192   | No file              | `eec03bd1cc3c`  |
| 1187   | No file              | `eec03bd1cc3c`  |
| 1183   | No file              | `eec03bd1cc3c`  |
| 1177   | No file              | `eec03bd1cc3c`  |
| 1173   | No file              | `eec03bd1cc3c`  |
| 1167   | No file              | `eec03bd1cc3c`  |
| 1164   | No file              | `eec03bd1cc3c`  |
| 1156   | No file              | `eec03bd1cc3c`  |
| 1149   | No file              | `eec03bd1cc3c`  |
| 1144   | No file              | `eec03bd1cc3c`  |
| 1137   | No file              | `eec03bd1cc3c`  |
| 1132   | No file              | `eec03bd1cc3c`  |
| 1127   | No file              | `eec03bd1cc3c`  |
| 1122   | No file              | `eec03bd1cc3c`  |
| 1118   | No file              | `eec03bd1cc3c`  |
| 1114   | No file              | `eec03bd1cc3c`  |
| 1109   | No file              | `eec03bd1cc3c`  |
| 1102   | No file              | `eec03bd1cc3c`  |
| 1096   | No file              | `eec03bd1cc3c`  |
| 1088   | No file              | `eec03bd1cc3c`  |
| 1081   | No file              | `eec03bd1cc3c`  |
| 1076   | No file              | `eec03bd1cc3c`  |
| 1069   | No file              | `eec03bd1cc3c`  |
| 1064   | No file              | `eec03bd1cc3c`  |
| 1058   | No file              | `eec03bd1cc3c`  |
| 1051   | No file              | `eec03bd1cc3c`  |
| 1044   | No file              | `eec03bd1cc3c`  |
| 1036   | No file              | `eec03bd1cc3c`  |
| 1026   | No file              | `eec03bd1cc3c`  |
| 1016   | No file              | `eec03bd1cc3c`  |
| 1009   | No file              | `eec03bd1cc3c`  |
| 1005   | No file              | `eec03bd1cc3c`  |
| 1000   | No file              | `eec03bd1cc3c`  |
| 998    | No file              | `eec03bd1cc3c`  |
| 990    | No file              | `eec03bd1cc3c`  |
| 979    | No file              | `eec03bd1cc3c`  |
| 972    | No file              | `eec03bd1cc3c`  |
| 963    | No file              | `eec03bd1cc3c`  |
| 955    | No file              | `eec03bd1cc3c`  |
| 946    | No file              | `eec03bd1cc3c`  |
| 938    | No file              | `eec03bd1cc3c`  |
| 927    | No file              | `eec03bd1cc3c`  |
| 911    | No file              | `eec03bd1cc3c`  |
| 904    | No file              | `eec03bd1cc3c`  |
| 899    | No file              | `eec03bd1cc3c`  |
| 894    | No file              | `eec03bd1cc3c`  |
| 885    | No file              | `eec03bd1cc3c`  |
| 879    | No file              | `eec03bd1cc3c`  |
| 872    | No file              | `eec03bd1cc3c`  |
| 864    | No file              | `eec03bd1cc3c`  |
| 855    | No file              | `eec03bd1cc3c`  |
| 853    | No file              | `eec03bd1cc3c`  |
| 845    | No file              | `eec03bd1cc3c`  |
| 837    | No file              | `eec03bd1cc3c`  |
| 829    | No file              | `eec03bd1cc3c`  |
| 822    | No file              | `eec03bd1cc3c`  |
| 814    | No file              | `eec03bd1cc3c`  |
| 805    | No file              | `eec03bd1cc3c`  |
| 794    | No file              | `eec03bd1cc3c`  |
| 787    | No file              | `eec03bd1cc3c`  |
| 780    | No file              | `eec03bd1cc3c`  |
| 771    | No file              | `eec03bd1cc3c`  |
| 760    | No file              | `eec03bd1cc3c`  |
| 748    | No file              | `eec03bd1cc3c`  |
| 741    | No file              | `eec03bd1cc3c`  |
| 736    | No file              | `eec03bd1cc3c`  |
| 731    | No file              | `eec03bd1cc3c`  |
| 723    | No file              | `eec03bd1cc3c`  |
| 711    | No file              | `eec03bd1cc3c`  |
| 707    | No file              | `eec03bd1cc3c`  |
| 697    | No file              | `eec03bd1cc3c`  |
| 689    | No file              | `eec03bd1cc3c`  |
| 683    | No file              | `eec03bd1cc3c`  |
| 678    | No file              | `eec03bd1cc3c`  |
| 670    | No file              | `eec03bd1cc3c`  |
| 661    | No file              | `eec03bd1cc3c`  |
| 656    | No file              | `eec03bd1cc3c`  |
| 652    | No file              | `eec03bd1cc3c`  |
| 643    | No file              | `eec03bd1cc3c`  |
| 637    | No file              | `eec03bd1cc3c`  |
| 630    | No file              | `eec03bd1cc3c`  |
| 627    | No file              | `eec03bd1cc3c`  |
| 621    | No file              | `eec03bd1cc3c`  |
| 617    | No file              | `eec03bd1cc3c`  |
| 615    | No file              | `eec03bd1cc3c`  |
| 606    | No file              | `eec03bd1cc3c`  |
| 599    | No file              | `eec03bd1cc3c`  |
| 592    | No file              | `eec03bd1cc3c`  |
| 586    | No file              | `eec03bd1cc3c`  |
| 577    | No file              | `eec03bd1cc3c`  |
| 569    | No file              | `eec03bd1cc3c`  |
| 561    | No file              | `eec03bd1cc3c`  |
| 554    | No file              | `eec03bd1cc3c`  |
| 542    | No file              | `eec03bd1cc3c`  |
| 532    | No file              | `eec03bd1cc3c`  |
| 531    | No file              | `eec03bd1cc3c`  |
| 526    | No file              | `eec03bd1cc3c`  |
| 521    | No file              | `eec03bd1cc3c`  |
| 517    | No file              | `eec03bd1cc3c`  |
| 510    | No file              | `eec03bd1cc3c`  |
| 508    | No file              | `eec03bd1cc3c`  |
| 504    | No file              | `eec03bd1cc3c`  |
| 497    | No file              | `eec03bd1cc3c`  |
| 491    | No file              | `eec03bd1cc3c`  |
| 485    | No file              | `eec03bd1cc3c`  |
| 478    | No file              | `eec03bd1cc3c`  |
| 472    | No file              | `eec03bd1cc3c`  |
| 466    | No file              | `eec03bd1cc3c`  |
| 457    | No file              | `eec03bd1cc3c`  |
| 452    | No file              | `eec03bd1cc3c`  |
| 449    | No file              | `eec03bd1cc3c`  |
| 435    | No file              | `eec03bd1cc3c`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 34 bytes + key lists)

| Offset                      | Type                              | Field                     | Notes                                                                        |
| --------------------------- | --------------------------------- | ------------------------- | ---------------------------------------------------------------------------- |
| `+0x00`                     | u64                               | kamasylvia_side_key_count | Number of `kamasylvia_side_keys`                                             |
| `+0x08`                     | u16[kamasylvia_side_key_count]    | kamasylvia_side_keys      | Linked sanctums one step toward sanctum `1`; empty on sanctum `1`            |
| `kamasylvia_side_keys+0x00` | u64                               | odyllita_side_key_count   | Number of `odyllita_side_keys`                                               |
| `kamasylvia_side_keys+0x08` | u16[odyllita_side_key_count]      | odyllita_side_keys        | Linked sanctums one step toward sanctum `11`; empty on sanctum `11`          |
| `odyllita_side_keys+0x00`   | u64                               | unknown_list_3_count      | Number of `unknown_list_3`                                                   |
| `odyllita_side_keys+0x08`   | u16[unknown_list_3_count]         | unknown_list_3            | One key of `odyllita_side_keys`, or empty; see Open Questions                |
| `unknown_list_3+0x00`       | u64                               | unknown_list_4_count      | Number of `unknown_list_4`                                                   |
| `unknown_list_3+0x08`       | u16[unknown_list_4_count]         | unknown_list_4            | One key of `kamasylvia_side_keys`, or empty                                  |
| `unknown_list_4+0x00`       | u16                               | fierce_battle_key         | The sanctum the row is for, as in the monster table                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Sanctum Links

Client 3474, by `fierce_battle_key`:

| Key  | `kamasylvia_side_keys` | `odyllita_side_keys` | `unknown_list_3` | `unknown_list_4` |
| ---- | ---------------------- | -------------------- | ---------------- | ---------------- |
| `1`  |                        | `2`, `5`             |                  |                  |
| `2`  | `1`                    | `3`                  | `3`              | `1`              |
| `3`  | `2`                    | `4`                  | `4`              | `2`              |
| `4`  | `3`                    | `14`, `17`           | `14`             | `3`              |
| `5`  | `1`                    | `6`                  | `6`              | `1`              |
| `6`  | `5`                    | `7`                  | `7`              | `5`              |
| `7`  | `6`                    | `14`, `17`           | `17`             | `6`              |
| `11` | `12`, `15`             |                      |                  |                  |
| `12` | `13`                   | `11`                 | `11`             | `13`             |
| `13` | `14`                   | `12`                 | `12`             | `14`             |
| `14` | `4`, `7`               | `13`                 | `13`             | `4`              |
| `15` | `16`                   | `11`                 | `11`             | `16`             |
| `16` | `17`                   | `15`                 | `15`             | `17`             |
| `17` | `4`, `7`               | `16`                 | `16`             | `7`              |

Every link points both ways: a key in another row's `odyllita_side_keys`
has that row's key in its own `kamasylvia_side_keys`, and back.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. `fierce_battle_key` matches
the keys of [`rosewarfiercebattlemonsterstaticstatus.bss`](rosewarfiercebattlemonsterstaticstatus_bss.md),
whose keys `1` to `10` are the Kamasylvia side sanctums (`ElfWar_Kama_N1`
to `N10` images) and `11` to `20` the O'dyllita side ones (`ElfWar_Odyl_S1`
to `S10`). The first two lists are named by the side their keys lie on:
on every linked row the first list leads toward sanctum `1` and the second
toward sanctum `11`.

## Notes

- Client 3002 links all 20 sanctums in three lanes per side: sanctum `1`
  opens to `2`, `5` and `8`, sanctum `11` to `12`, `16` and `19`, and the
  lanes cross at `4`, `7`, `10`, `15`, `18` and `20` (940 bytes). Clients
  3251 and 3474 have the two-lane graph above (880 bytes). The file is not
  in the archives of client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  the key first.

## Open Questions

### The Third and Fourth Lists

`unknown_list_3` holds one key of `odyllita_side_keys` and `unknown_list_4`
one key of `kamasylvia_side_keys` on every linked row except the two end
sanctums, where both are empty. Where a row has two neighbours on a side,
the pick does not follow the key order (`4` takes `14`, `7` takes `17`,
`17` takes `7`). The revive window checks `canRevive()` per sanctum, and the
lists may be the path a team must hold to revive there, but no Lua reads
them.
