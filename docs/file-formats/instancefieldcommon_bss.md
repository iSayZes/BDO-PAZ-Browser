# `instancefieldcommon.bss` Format

## Purpose

Entry limits of an instance: per instance type and mode the lowest
character level, the quest that must be done first and the Korean message
shown when a character is turned away. The only row on client 3482 asks
for level 56 and quest `804, 1` ("[Awakening] The Black Spirit's Strange
Power"); its message says that `가시나무 성` can only be entered after the
character awakening quest, and not below level 56. The file is the
`InstanceCommonOption` sheet compiled into a PABR table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | --------------------- | --------- |
| 2      | 1459 and later | 3483    | `instancefieldcommon.bss` | 185   | 1 Row, 1 String Table | 22        |
| 1      | 1421 to 1453   | 1453    | `instancefieldcommon.bss` | 257   | 1 Row, 1 String Table | 16        |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 2      | `instancefieldcommon.bss` | 179 B (96.8%)  | 6 B (3.2%) |
| 1      | `instancefieldcommon.bss` | 257 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `5e4ebe76decb`  |
| 3482   | Layout 2 | `5e4ebe76decb`  |
| 3474   | Layout 2 | `5e4ebe76decb`  |
| 3473   | Layout 2 | `5e4ebe76decb`  |
| 3464   | Layout 2 | `5e4ebe76decb`  |
| 3458   | Layout 2 | `5e4ebe76decb`  |
| 3454   | Layout 2 | `5e4ebe76decb`  |
| 3444   | Layout 2 | `5e4ebe76decb`  |
| 3435   | Layout 2 | `5e4ebe76decb`  |
| 3426   | Layout 2 | `5e4ebe76decb`  |
| 3418   | Layout 2 | `5e4ebe76decb`  |
| 3412   | Layout 2 | `5e4ebe76decb`  |
| 3402   | Layout 2 | `5e4ebe76decb`  |
| 3396   | Layout 2 | `5e4ebe76decb`  |
| 3387   | Layout 2 | `5e4ebe76decb`  |
| 3381   | Layout 2 | `5e4ebe76decb`  |
| 3373   | Layout 2 | `5e4ebe76decb`  |
| 3364   | Layout 2 | `5e4ebe76decb`  |
| 3356   | Layout 2 | `5e4ebe76decb`  |
| 3349   | Layout 2 | `5e4ebe76decb`  |
| 3342   | Layout 2 | `5e4ebe76decb`  |
| 3335   | Layout 2 | `5e4ebe76decb`  |
| 3326   | Layout 2 | `5e4ebe76decb`  |
| 3321   | Layout 2 | `5e4ebe76decb`  |
| 3314   | Layout 2 | `5e4ebe76decb`  |
| 3303   | Layout 2 | `5e4ebe76decb`  |
| 3302   | Layout 2 | `5e4ebe76decb`  |
| 3293   | Layout 2 | `5e4ebe76decb`  |
| 3283   | Layout 2 | `5e4ebe76decb`  |
| 3275   | Layout 2 | `5e4ebe76decb`  |
| 3267   | Layout 2 | `5e4ebe76decb`  |
| 3258   | Layout 2 | `5e4ebe76decb`  |
| 3251   | Layout 2 | `5e4ebe76decb`  |
| 3242   | Layout 2 | `5e4ebe76decb`  |
| 3235   | Layout 2 | `5e4ebe76decb`  |
| 3229   | Layout 2 | `5e4ebe76decb`  |
| 3212   | Layout 2 | `5e4ebe76decb`  |
| 3203   | Layout 2 | `5e4ebe76decb`  |
| 3193   | Layout 2 | `5e4ebe76decb`  |
| 3186   | Layout 2 | `5e4ebe76decb`  |
| 3177   | Layout 2 | `5e4ebe76decb`  |
| 3169   | Layout 2 | `5e4ebe76decb`  |
| 3158   | Layout 2 | `5e4ebe76decb`  |
| 3151   | Layout 2 | `5e4ebe76decb`  |
| 3144   | Layout 2 | `5e4ebe76decb`  |
| 3133   | Layout 2 | `5e4ebe76decb`  |
| 3125   | Layout 2 | `5e4ebe76decb`  |
| 3118   | Layout 2 | `5e4ebe76decb`  |
| 3111   | Layout 2 | `5e4ebe76decb`  |
| 3103   | Layout 2 | `5e4ebe76decb`  |
| 3095   | Layout 2 | `5e4ebe76decb`  |
| 3086   | Layout 2 | `5e4ebe76decb`  |
| 3072   | Layout 2 | `5e4ebe76decb`  |
| 3062   | Layout 2 | `5e4ebe76decb`  |
| 3052   | Layout 2 | `5e4ebe76decb`  |
| 3045   | Layout 2 | `5e4ebe76decb`  |
| 3037   | Layout 2 | `5e4ebe76decb`  |
| 3030   | Layout 2 | `5e4ebe76decb`  |
| 3021   | Layout 2 | `5e4ebe76decb`  |
| 3012   | Layout 2 | `5e4ebe76decb`  |
| 3002   | Layout 2 | `5e4ebe76decb`  |
| 2995   | Layout 2 | `5e4ebe76decb`  |
| 2987   | Layout 2 | `5e4ebe76decb`  |
| 2978   | Layout 2 | `5e4ebe76decb`  |
| 2970   | Layout 2 | `5e4ebe76decb`  |
| 2959   | Layout 2 | `5e4ebe76decb`  |
| 2951   | Layout 2 | `5e4ebe76decb`  |
| 2942   | Layout 2 | `5e4ebe76decb`  |
| 2935   | Layout 2 | `5e4ebe76decb`  |
| 2932   | Layout 2 | `5e4ebe76decb`  |
| 2923   | Layout 2 | `5e4ebe76decb`  |
| 2919   | Layout 2 | `5e4ebe76decb`  |
| 2907   | Layout 2 | `5e4ebe76decb`  |
| 2900   | Layout 2 | `5e4ebe76decb`  |
| 2891   | Layout 2 | `5e4ebe76decb`  |
| 2882   | Layout 2 | `5e4ebe76decb`  |
| 2872   | Layout 2 | `5e4ebe76decb`  |
| 2863   | Layout 2 | `5e4ebe76decb`  |
| 2855   | Layout 2 | `5e4ebe76decb`  |
| 2849   | Layout 2 | `5e4ebe76decb`  |
| 2844   | Layout 2 | `5e4ebe76decb`  |
| 2834   | Layout 2 | `5e4ebe76decb`  |
| 2825   | Layout 2 | `5e4ebe76decb`  |
| 2819   | Layout 2 | `5e4ebe76decb`  |
| 2811   | Layout 2 | `5e4ebe76decb`  |
| 2803   | Layout 2 | `5e4ebe76decb`  |
| 2794   | Layout 2 | `5e4ebe76decb`  |
| 2783   | Layout 2 | `5e4ebe76decb`  |
| 2774   | Layout 2 | `5e4ebe76decb`  |
| 2765   | Layout 2 | `5e4ebe76decb`  |
| 2756   | Layout 2 | `5e4ebe76decb`  |
| 2750   | Layout 2 | `5e4ebe76decb`  |
| 2743   | Layout 2 | `5e4ebe76decb`  |
| 2736   | Layout 2 | `5e4ebe76decb`  |
| 2726   | Layout 2 | `5e4ebe76decb`  |
| 2717   | Layout 2 | `5e4ebe76decb`  |
| 2709   | Layout 2 | `5e4ebe76decb`  |
| 2703   | Layout 2 | `5e4ebe76decb`  |
| 2695   | Layout 2 | `5e4ebe76decb`  |
| 2684   | Layout 2 | `5e4ebe76decb`  |
| 2672   | Layout 2 | `5e4ebe76decb`  |
| 2665   | Layout 2 | `5e4ebe76decb`  |
| 2657   | Layout 2 | `5e4ebe76decb`  |
| 2649   | Layout 2 | `5e4ebe76decb`  |
| 2644   | Layout 2 | `5e4ebe76decb`  |
| 2637   | Layout 2 | `5e4ebe76decb`  |
| 2629   | Layout 2 | `5e4ebe76decb`  |
| 2619   | Layout 2 | `5e4ebe76decb`  |
| 2612   | Layout 2 | `5e4ebe76decb`  |
| 2606   | Layout 2 | `5e4ebe76decb`  |
| 2602   | Layout 2 | `5e4ebe76decb`  |
| 2601   | Layout 2 | `5e4ebe76decb`  |
| 2592   | Layout 2 | `5e4ebe76decb`  |
| 2583   | Layout 2 | `5e4ebe76decb`  |
| 2575   | Layout 2 | `5e4ebe76decb`  |
| 2567   | Layout 2 | `5e4ebe76decb`  |
| 2560   | Layout 2 | `5e4ebe76decb`  |
| 2553   | Layout 2 | `5e4ebe76decb`  |
| 2545   | Layout 2 | `5e4ebe76decb`  |
| 2538   | Layout 2 | `5e4ebe76decb`  |
| 2529   | Layout 2 | `5e4ebe76decb`  |
| 2519   | Layout 2 | `5e4ebe76decb`  |
| 2513   | Layout 2 | `5e4ebe76decb`  |
| 2510   | Layout 2 | `5e4ebe76decb`  |
| 2507   | Layout 2 | `5e4ebe76decb`  |
| 2503   | Layout 2 | `5e4ebe76decb`  |
| 2498   | Layout 2 | `5e4ebe76decb`  |
| 2492   | Layout 2 | `5e4ebe76decb`  |
| 2487   | Layout 2 | `5e4ebe76decb`  |
| 2480   | Layout 2 | `5e4ebe76decb`  |
| 2474   | Layout 2 | `5e4ebe76decb`  |
| 2468   | Layout 2 | `5e4ebe76decb`  |
| 2460   | Layout 2 | `5e4ebe76decb`  |
| 2453   | Layout 2 | `5e4ebe76decb`  |
| 2444   | Layout 2 | `5e4ebe76decb`  |
| 2438   | Layout 2 | `5e4ebe76decb`  |
| 2434   | Layout 2 | `5e4ebe76decb`  |
| 2429   | Layout 2 | `5e4ebe76decb`  |
| 2421   | Layout 2 | `5e4ebe76decb`  |
| 2414   | Layout 2 | `5e4ebe76decb`  |
| 2407   | Layout 2 | `5e4ebe76decb`  |
| 2401   | Layout 2 | `5e4ebe76decb`  |
| 2397   | Layout 2 | `5e4ebe76decb`  |
| 2393   | Layout 2 | `5e4ebe76decb`  |
| 2384   | Layout 2 | `5e4ebe76decb`  |
| 2378   | Layout 2 | `5e4ebe76decb`  |
| 2372   | Layout 2 | `5e4ebe76decb`  |
| 2358   | Layout 2 | `5e4ebe76decb`  |
| 2352   | Layout 2 | `5e4ebe76decb`  |
| 2347   | Layout 2 | `5e4ebe76decb`  |
| 2343   | Layout 2 | `5e4ebe76decb`  |
| 2335   | Layout 2 | `5e4ebe76decb`  |
| 2327   | Layout 2 | `5e4ebe76decb`  |
| 2324   | Layout 2 | `5e4ebe76decb`  |
| 2319   | Layout 2 | `5e4ebe76decb`  |
| 2313   | Layout 2 | `5e4ebe76decb`  |
| 2308   | Layout 2 | `5e4ebe76decb`  |
| 2302   | Layout 2 | `5e4ebe76decb`  |
| 2295   | Layout 2 | `5e4ebe76decb`  |
| 2290   | Layout 2 | `5e4ebe76decb`  |
| 2284   | Layout 2 | `5e4ebe76decb`  |
| 2276   | Layout 2 | `5e4ebe76decb`  |
| 2269   | Layout 2 | `5e4ebe76decb`  |
| 2259   | Layout 2 | `5e4ebe76decb`  |
| 2250   | Layout 2 | `5e4ebe76decb`  |
| 2243   | Layout 2 | `5e4ebe76decb`  |
| 2235   | Layout 2 | `5e4ebe76decb`  |
| 2229   | Layout 2 | `5e4ebe76decb`  |
| 2224   | Layout 2 | `5e4ebe76decb`  |
| 2218   | Layout 2 | `5e4ebe76decb`  |
| 2215   | Layout 2 | `5e4ebe76decb`  |
| 2207   | Layout 2 | `5e4ebe76decb`  |
| 2203   | Layout 2 | `5e4ebe76decb`  |
| 2196   | Layout 2 | `5e4ebe76decb`  |
| 2192   | Layout 2 | `5e4ebe76decb`  |
| 2189   | Layout 2 | `5e4ebe76decb`  |
| 2183   | Layout 2 | `5e4ebe76decb`  |
| 2179   | Layout 2 | `5e4ebe76decb`  |
| 2171   | Layout 2 | `5e4ebe76decb`  |
| 2163   | Layout 2 | `5e4ebe76decb`  |
| 2156   | Layout 2 | `5e4ebe76decb`  |
| 2151   | Layout 2 | `5e4ebe76decb`  |
| 2147   | Layout 2 | `5e4ebe76decb`  |
| 2142   | Layout 2 | `5e4ebe76decb`  |
| 2138   | Layout 2 | `5e4ebe76decb`  |
| 2134   | Layout 2 | `5e4ebe76decb`  |
| 2130   | Layout 2 | `5e4ebe76decb`  |
| 2122   | Layout 2 | `5e4ebe76decb`  |
| 2107   | Layout 2 | `5e4ebe76decb`  |
| 2098   | Layout 2 | `5e4ebe76decb`  |
| 2089   | Layout 2 | `5e4ebe76decb`  |
| 2081   | Layout 2 | `5e4ebe76decb`  |
| 2073   | Layout 2 | `5e4ebe76decb`  |
| 2067   | Layout 2 | `5e4ebe76decb`  |
| 2063   | Layout 2 | `5e4ebe76decb`  |
| 2059   | Layout 2 | `5e4ebe76decb`  |
| 2052   | Layout 2 | `5e4ebe76decb`  |
| 2044   | Layout 2 | `5e4ebe76decb`  |
| 2039   | Layout 2 | `5e4ebe76decb`  |
| 2032   | Layout 2 | `5e4ebe76decb`  |
| 2025   | Layout 2 | `5e4ebe76decb`  |
| 2011   | Layout 2 | `5e4ebe76decb`  |
| 2005   | Layout 2 | `5e4ebe76decb`  |
| 2000   | Layout 2 | `5e4ebe76decb`  |
| 1996   | Layout 2 | `5e4ebe76decb`  |
| 1991   | Layout 2 | `5e4ebe76decb`  |
| 1985   | Layout 2 | `5e4ebe76decb`  |
| 1980   | Layout 2 | `5e4ebe76decb`  |
| 1969   | Layout 2 | `5e4ebe76decb`  |
| 1964   | Layout 2 | `5e4ebe76decb`  |
| 1958   | Layout 2 | `5e4ebe76decb`  |
| 1950   | Layout 2 | `5e4ebe76decb`  |
| 1945   | Layout 2 | `5e4ebe76decb`  |
| 1937   | Layout 2 | `5e4ebe76decb`  |
| 1933   | Layout 2 | `5e4ebe76decb`  |
| 1927   | Layout 2 | `5e4ebe76decb`  |
| 1921   | Layout 2 | `5e4ebe76decb`  |
| 1914   | Layout 2 | `5e4ebe76decb`  |
| 1908   | Layout 2 | `5e4ebe76decb`  |
| 1897   | Layout 2 | `5e4ebe76decb`  |
| 1892   | Layout 2 | `5e4ebe76decb`  |
| 1886   | Layout 2 | `5e4ebe76decb`  |
| 1881   | Layout 2 | `5e4ebe76decb`  |
| 1871   | Layout 2 | `5e4ebe76decb`  |
| 1866   | Layout 2 | `5e4ebe76decb`  |
| 1862   | Layout 2 | `5e4ebe76decb`  |
| 1854   | Layout 2 | `5e4ebe76decb`  |
| 1846   | Layout 2 | `5e4ebe76decb`  |
| 1838   | Layout 2 | `5e4ebe76decb`  |
| 1832   | Layout 2 | `5e4ebe76decb`  |
| 1826   | Layout 2 | `5e4ebe76decb`  |
| 1822   | Layout 2 | `5e4ebe76decb`  |
| 1818   | Layout 2 | `5e4ebe76decb`  |
| 1804   | Layout 2 | `5e4ebe76decb`  |
| 1794   | Layout 2 | `5e4ebe76decb`  |
| 1790   | Layout 2 | `5e4ebe76decb`  |
| 1784   | Layout 2 | `5e4ebe76decb`  |
| 1774   | Layout 2 | `5e4ebe76decb`  |
| 1771   | Layout 2 | `5e4ebe76decb`  |
| 1762   | Layout 2 | `5e4ebe76decb`  |
| 1759   | Layout 2 | `5e4ebe76decb`  |
| 1754   | Layout 2 | `5e4ebe76decb`  |
| 1749   | Layout 2 | `5e4ebe76decb`  |
| 1743   | Layout 2 | `5e4ebe76decb`  |
| 1737   | Layout 2 | `5e4ebe76decb`  |
| 1731   | Layout 2 | `5e4ebe76decb`  |
| 1725   | Layout 2 | `5e4ebe76decb`  |
| 1717   | Layout 2 | `5e4ebe76decb`  |
| 1710   | Layout 2 | `5e4ebe76decb`  |
| 1704   | Layout 2 | `5e4ebe76decb`  |
| 1698   | Layout 2 | `5e4ebe76decb`  |
| 1690   | Layout 2 | `5e4ebe76decb`  |
| 1685   | Layout 2 | `5e4ebe76decb`  |
| 1680   | Layout 2 | `5e4ebe76decb`  |
| 1674   | Layout 2 | `5e4ebe76decb`  |
| 1668   | Layout 2 | `5e4ebe76decb`  |
| 1659   | Layout 2 | `5e4ebe76decb`  |
| 1649   | Layout 2 | `5e4ebe76decb`  |
| 1642   | Layout 2 | `5e4ebe76decb`  |
| 1636   | Layout 2 | `5e4ebe76decb`  |
| 1628   | Layout 2 | `5e4ebe76decb`  |
| 1622   | Layout 2 | `5e4ebe76decb`  |
| 1614   | Layout 2 | `5e4ebe76decb`  |
| 1608   | Layout 2 | `5e4ebe76decb`  |
| 1602   | Layout 2 | `5e4ebe76decb`  |
| 1598   | Layout 2 | `5e4ebe76decb`  |
| 1594   | Layout 2 | `5e4ebe76decb`  |
| 1590   | Layout 2 | `5e4ebe76decb`  |
| 1587   | Layout 2 | `5e4ebe76decb`  |
| 1584   | Layout 2 | `5e4ebe76decb`  |
| 1579   | Layout 2 | `5e4ebe76decb`  |
| 1572   | Layout 2 | `5e4ebe76decb`  |
| 1565   | Layout 2 | `5e4ebe76decb`  |
| 1559   | Layout 2 | `5e4ebe76decb`  |
| 1554   | Layout 2 | `5e4ebe76decb`  |
| 1547   | Layout 2 | `5e4ebe76decb`  |
| 1537   | Layout 2 | `5e4ebe76decb`  |
| 1529   | Layout 2 | `5e4ebe76decb`  |
| 1524   | Layout 2 | `5e4ebe76decb`  |
| 1519   | Layout 2 | `5e4ebe76decb`  |
| 1509   | Layout 2 | `5e4ebe76decb`  |
| 1506   | Layout 2 | `5e4ebe76decb`  |
| 1504   | Layout 2 | `5e4ebe76decb`  |
| 1500   | Layout 2 | `5e4ebe76decb`  |
| 1493   | Layout 2 | `5e4ebe76decb`  |
| 1489   | Layout 2 | `5e4ebe76decb`  |
| 1485   | Layout 2 | `5e4ebe76decb`  |
| 1481   | Layout 2 | `5e4ebe76decb`  |
| 1474   | Layout 2 | `5e4ebe76decb`  |
| 1466   | Layout 2 | `5e4ebe76decb`  |
| 1462   | Layout 2 | `5e4ebe76decb`  |
| 1459   | Layout 2 | `5e4ebe76decb`  |
| 1453   | Layout 1 | `5e4ebe76decb`  |
| 1450   | Layout 1 | `5e4ebe76decb`  |
| 1445   | Layout 1 | `5e4ebe76decb`  |
| 1439   | Layout 1 | `5e4ebe76decb`  |
| 1433   | Layout 1 | `5e4ebe76decb`  |
| 1430   | Layout 1 | `5e4ebe76decb`  |
| 1426   | Layout 1 | `5e4ebe76decb`  |
| 1421   | Layout 1 | `5e4ebe76decb`  |
| 1417   | No file  | `5e4ebe76decb`  |
| 1416   | No file  | `5e4ebe76decb`  |
| 1409   | No file  | `5e4ebe76decb`  |
| 1405   | No file  | `5e4ebe76decb`  |
| 1401   | No file  | `5e4ebe76decb`  |
| 1396   | No file  | `5e4ebe76decb`  |
| 1391   | No file  | `5e4ebe76decb`  |
| 1390   | No file  | `5e4ebe76decb`  |
| 1386   | No file  | `5e4ebe76decb`  |
| 1381   | No file  | `5e4ebe76decb`  |
| 1379   | No file  | `5e4ebe76decb`  |
| 1372   | No file  | `5e4ebe76decb`  |
| 1366   | No file  | `5e4ebe76decb`  |
| 1364   | No file  | `5e4ebe76decb`  |
| 1363   | No file  | `5e4ebe76decb`  |
| 1360   | No file  | `5e4ebe76decb`  |
| 1358   | No file  | `5e4ebe76decb`  |
| 1355   | No file  | `5e4ebe76decb`  |
| 1351   | No file  | `5e4ebe76decb`  |
| 1348   | No file  | `5e4ebe76decb`  |
| 1346   | No file  | `5e4ebe76decb`  |
| 1341   | No file  | `5e4ebe76decb`  |
| 1340   | No file  | `5e4ebe76decb`  |
| 1338   | No file  | `5e4ebe76decb`  |
| 1335   | No file  | `5e4ebe76decb`  |
| 1333   | No file  | `5e4ebe76decb`  |
| 1329   | No file  | `5e4ebe76decb`  |
| 1327   | No file  | `5e4ebe76decb`  |
| 1324   | No file  | `5e4ebe76decb`  |
| 1321   | No file  | `5e4ebe76decb`  |
| 1319   | No file  | `5e4ebe76decb`  |
| 1318   | No file  | `5e4ebe76decb`  |
| 1316   | No file  | `5e4ebe76decb`  |
| 1313   | No file  | `5e4ebe76decb`  |
| 1311   | No file  | `5e4ebe76decb`  |
| 1309   | No file  | `5e4ebe76decb`  |
| 1304   | No file  | `5e4ebe76decb`  |
| 1292   | No file  | `5e4ebe76decb`  |
| 1286   | No file  | `5e4ebe76decb`  |
| 1280   | No file  | `5e4ebe76decb`  |
| 1276   | No file  | `5e4ebe76decb`  |
| 1267   | No file  | `5e4ebe76decb`  |
| 1261   | No file  | `5e4ebe76decb`  |
| 1256   | No file  | `5e4ebe76decb`  |
| 1250   | No file  | `5e4ebe76decb`  |
| 1246   | No file  | `5e4ebe76decb`  |
| 1239   | No file  | `5e4ebe76decb`  |
| 1230   | No file  | `5e4ebe76decb`  |
| 1226   | No file  | `5e4ebe76decb`  |
| 1220   | No file  | `5e4ebe76decb`  |
| 1217   | No file  | `5e4ebe76decb`  |
| 1211   | No file  | `5e4ebe76decb`  |
| 1210   | No file  | `5e4ebe76decb`  |
| 1208   | No file  | `5e4ebe76decb`  |
| 1203   | No file  | `5e4ebe76decb`  |
| 1197   | No file  | `5e4ebe76decb`  |
| 1194   | No file  | `5e4ebe76decb`  |
| 1192   | No file  | `5e4ebe76decb`  |
| 1187   | No file  | `5e4ebe76decb`  |
| 1183   | No file  | `5e4ebe76decb`  |
| 1177   | No file  | `5e4ebe76decb`  |
| 1173   | No file  | `5e4ebe76decb`  |
| 1167   | No file  | `5e4ebe76decb`  |
| 1164   | No file  | `5e4ebe76decb`  |
| 1156   | No file  | `5e4ebe76decb`  |
| 1149   | No file  | `5e4ebe76decb`  |
| 1144   | No file  | `5e4ebe76decb`  |
| 1137   | No file  | `5e4ebe76decb`  |
| 1132   | No file  | `5e4ebe76decb`  |
| 1127   | No file  | `5e4ebe76decb`  |
| 1122   | No file  | `5e4ebe76decb`  |
| 1118   | No file  | `5e4ebe76decb`  |
| 1114   | No file  | `5e4ebe76decb`  |
| 1109   | No file  | `5e4ebe76decb`  |
| 1102   | No file  | `5e4ebe76decb`  |
| 1096   | No file  | `5e4ebe76decb`  |
| 1088   | No file  | `5e4ebe76decb`  |
| 1081   | No file  | `5e4ebe76decb`  |
| 1076   | No file  | `5e4ebe76decb`  |
| 1069   | No file  | `5e4ebe76decb`  |
| 1064   | No file  | `5e4ebe76decb`  |
| 1058   | No file  | `5e4ebe76decb`  |
| 1051   | No file  | `5e4ebe76decb`  |
| 1044   | No file  | `5e4ebe76decb`  |
| 1036   | No file  | `5e4ebe76decb`  |
| 1026   | No file  | `5e4ebe76decb`  |
| 1016   | No file  | `5e4ebe76decb`  |
| 1009   | No file  | `5e4ebe76decb`  |
| 1005   | No file  | `5e4ebe76decb`  |
| 1000   | No file  | `5e4ebe76decb`  |
| 998    | No file  | `5e4ebe76decb`  |
| 990    | No file  | `5e4ebe76decb`  |
| 979    | No file  | `5e4ebe76decb`  |
| 972    | No file  | `5e4ebe76decb`  |
| 963    | No file  | `5e4ebe76decb`  |
| 955    | No file  | `5e4ebe76decb`  |
| 946    | No file  | `5e4ebe76decb`  |
| 938    | No file  | `5e4ebe76decb`  |
| 927    | No file  | `5e4ebe76decb`  |
| 911    | No file  | `5e4ebe76decb`  |
| 904    | No file  | `5e4ebe76decb`  |
| 899    | No file  | `5e4ebe76decb`  |
| 894    | No file  | `5e4ebe76decb`  |
| 885    | No file  | `5e4ebe76decb`  |
| 879    | No file  | `5e4ebe76decb`  |
| 872    | No file  | `5e4ebe76decb`  |
| 864    | No file  | `5e4ebe76decb`  |
| 855    | No file  | `5e4ebe76decb`  |
| 853    | No file  | `5e4ebe76decb`  |
| 845    | No file  | `5e4ebe76decb`  |
| 837    | No file  | `5e4ebe76decb`  |
| 829    | No file  | `5e4ebe76decb`  |
| 822    | No file  | `5e4ebe76decb`  |
| 814    | No file  | `5e4ebe76decb`  |
| 805    | No file  | `5e4ebe76decb`  |
| 794    | No file  | `5e4ebe76decb`  |
| 787    | No file  | `5e4ebe76decb`  |
| 780    | No file  | `5e4ebe76decb`  |
| 771    | No file  | `5e4ebe76decb`  |
| 760    | No file  | `5e4ebe76decb`  |
| 748    | No file  | `5e4ebe76decb`  |
| 741    | No file  | `5e4ebe76decb`  |
| 736    | No file  | `5e4ebe76decb`  |
| 731    | No file  | `5e4ebe76decb`  |
| 723    | No file  | `5e4ebe76decb`  |
| 711    | No file  | `5e4ebe76decb`  |
| 707    | No file  | `5e4ebe76decb`  |
| 697    | No file  | `5e4ebe76decb`  |
| 689    | No file  | `5e4ebe76decb`  |
| 683    | No file  | `5e4ebe76decb`  |
| 678    | No file  | `5e4ebe76decb`  |
| 670    | No file  | `5e4ebe76decb`  |
| 661    | No file  | `5e4ebe76decb`  |
| 656    | No file  | `5e4ebe76decb`  |
| 652    | No file  | `5e4ebe76decb`  |
| 643    | No file  | `5e4ebe76decb`  |
| 637    | No file  | `5e4ebe76decb`  |
| 630    | No file  | `5e4ebe76decb`  |
| 627    | No file  | `5e4ebe76decb`  |
| 621    | No file  | `5e4ebe76decb`  |
| 617    | No file  | `5e4ebe76decb`  |
| 615    | No file  | `5e4ebe76decb`  |
| 606    | No file  | `5e4ebe76decb`  |
| 599    | No file  | `5e4ebe76decb`  |
| 592    | No file  | `5e4ebe76decb`  |
| 586    | No file  | `5e4ebe76decb`  |
| 577    | No file  | `5e4ebe76decb`  |
| 569    | No file  | `5e4ebe76decb`  |
| 561    | No file  | `5e4ebe76decb`  |
| 554    | No file  | `5e4ebe76decb`  |
| 542    | No file  | `5e4ebe76decb`  |
| 532    | No file  | `5e4ebe76decb`  |
| 531    | No file  | `5e4ebe76decb`  |
| 526    | No file  | `5e4ebe76decb`  |
| 521    | No file  | `5e4ebe76decb`  |
| 517    | No file  | `5e4ebe76decb`  |
| 510    | No file  | `5e4ebe76decb`  |
| 508    | No file  | `5e4ebe76decb`  |
| 504    | No file  | `5e4ebe76decb`  |
| 497    | No file  | `5e4ebe76decb`  |
| 491    | No file  | `5e4ebe76decb`  |
| 485    | No file  | `5e4ebe76decb`  |
| 478    | No file  | `5e4ebe76decb`  |
| 472    | No file  | `5e4ebe76decb`  |
| 466    | No file  | `5e4ebe76decb`  |
| 457    | No file  | `5e4ebe76decb`  |
| 452    | No file  | `5e4ebe76decb`  |
| 449    | No file  | `5e4ebe76decb`  |
| 435    | No file  | `5e4ebe76decb`  |

<!-- versions:end -->

## Companion Files

None. The handler names the quest from LOC type 18.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                              |
| ------------------- | ----------------- | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                             |
| `+0x04`             | u32               | record_count       | Number of rows                     |
| `+0x08`             | Row[record_count] | records            | See Row                            |
| `records+0x00`      | String Table      | string_table       | The limit messages                 |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`  |
| `string_table+0x04` | u32               | zero               | `0`                                |

### Row (variable: 20 bytes + list)

| Offset  | Type             | Field                   | Notes |
| ------- | ---------------- | ----------------------- | ----- |
| `+0x00` | u16              | instance_mode           | `0`; together with `instance_type` the row key |
| `+0x02` | u16              | instance_type           | `4` |
| `+0x04` | u32              | limited_character_level | Lowest character level, `56` |
| `+0x08` | u16              | limited_quest_group     | Quest chain of the required quest, `804` |
| `+0x0A` | u16              | limited_quest_id        | Quest number in that chain, `1` |
| `+0x0C` | u32              | limited_quest_string    | Index into `strings`: the message for a character that lacks the quest or the level |
| `+0x10` | u32              | unknown_10              | Number of `unknown_14` values, `1` |
| `+0x14` | u16[unknown_10]  | unknown_14              | `4`; see [unknown_10 and unknown_14](#unknown_10-and-unknown_14) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `1` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | Korean text, wide (`is_wide` 1); a `\n` is stored as the two characters `\` and `n` |

## Layout 1

Clients 1426 and 1445 end the row after `limited_quest_string`; their row
asks for quest `8003, 2` and level 56, with a longer message.

### Row (16 bytes)

| Offset  | Type | Field                   | Notes |
| ------- | ---- | ----------------------- | ----- |
| `+0x00` | u16  | instance_mode           | |
| `+0x02` | u16  | instance_type           | |
| `+0x04` | u32  | limited_character_level | |
| `+0x08` | u16  | limited_quest_group     | |
| `+0x0A` | u16  | limited_quest_id        | |
| `+0x0C` | u32  | limited_quest_string    | |

## Field Names

The names follow the `InstanceCommonOption` sheet of a private server's
`DataSheets.bexcel` on client 1784 (`InstanceType`, `InstanceMode`,
`LimitedCharacterLevel`, `LimitedQuestGroup`, `LimitedQuestID`,
`LimitedQuestString`). The sheet has one row, and every one of those six
values equals the file of client 1784, which is byte for byte the file of
client 3482. The server loader for the sheet in the client 1784 server
dump packs the key as `InstanceType << 16 | InstanceMode`, which puts
`instance_mode` in the low two bytes; it reads `LimitedQuestGroup` and
`LimitedQuestID` as 16-bit values.

## Notes

- The file has not changed from client 1784 to client 3482.

## Open Questions

### unknown_10 and unknown_14

The sheet's last column, `ContentsGroupKey`, is a list (the server loader
reads it as a list and turns every entry into another value before it
stores it), and `unknown_10` / `unknown_14` are the only list in the row.
The sheet holds `7` and the file `4`, so the list is not the contents
group key itself. What `4` stands for is open.
