# `attendance.dbss` Format

## Purpose

The daily login reward events (the Daily Login Rewards window): per event
its Korean title, start and end dates, the period and claim texts the
window shows, which players it is for, the reward of each login day, the
weekdays with an extra check-in and the order of the window tabs. The
window Lua (`panel_window_dailystamp_all_1.luac` and `_2.luac`) reads an
event through `ToClient_GetAttendanceInfoWrapper(index)` and the getters
`getKey()`, `getName()`, `getDisplayOrder()`, `getRewardCount()`,
`getRewardItem(index)`, `getRewardItemGradeType(index)`,
`getPeriodDate()` and `getExpireDate()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                    | Bytes   | Records               | Row bytes |
| ------ | -------------- | ----------------------- | ------- | --------------------- | --------- |
| 3      | 2235 and later | `attendance.dbss`       | 275,558 | 6,810 Reward, 298 Row | 25        |
| 3      | 2235 and later | `attendanceoffset.dbss` | 2,984   | 298 Offset Row        | 10        |
| 2      | 1749 to 2229   | `attendance.dbss`       | 175,848 | 4,524 Reward, 185 Row | 25        |
| 2      | 1749 to 2229   | `attendanceoffset.dbss` | 1,854   | 185 Offset Row        | 10        |
| 1      | 1250 to 1743   | `attendance.dbss`       | 97,195  | 3,269 Reward, 126 Row | 17        |
| 1      | 1250 to 1743   | `attendanceoffset.dbss` | 1,264   | 126 Offset Row        | 10        |

| Layout | File                    | Known             | Unknown         |
| ------ | ----------------------- | ----------------- | --------------- |
| 3      | `attendance.dbss`       | 261,254 B (94.8%) | 14,304 B (5.2%) |
| 3      | `attendanceoffset.dbss` | 2,984 B (100.0%)  | 0 B (0.0%)      |
| 2      | `attendance.dbss`       | 166,968 B (95.0%) | 8,880 B (5.0%)  |
| 2      | `attendanceoffset.dbss` | 1,854 B (100.0%)  | 0 B (0.0%)      |
| 1      | `attendance.dbss`       | 91,147 B (93.8%)  | 6,048 B (6.2%)  |
| 1      | `attendanceoffset.dbss` | 1,264 B (100.0%)  | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `48e666f70906`  |
| 3482   | Layout 3 | `48e666f70906`  |
| 3474   | Layout 3 | `48e666f70906`  |
| 3473   | Layout 3 | `48e666f70906`  |
| 3464   | Layout 3 | `48e666f70906`  |
| 3458   | Layout 3 | `48e666f70906`  |
| 3454   | Layout 3 | `48e666f70906`  |
| 3444   | Layout 3 | `48e666f70906`  |
| 3435   | Layout 3 | `48e666f70906`  |
| 3426   | Layout 3 | `48e666f70906`  |
| 3418   | Layout 3 | `48e666f70906`  |
| 3412   | Layout 3 | `48e666f70906`  |
| 3402   | Layout 3 | `48e666f70906`  |
| 3396   | Layout 3 | `48e666f70906`  |
| 3387   | Layout 3 | `48e666f70906`  |
| 3381   | Layout 3 | `48e666f70906`  |
| 3373   | Layout 3 | `48e666f70906`  |
| 3364   | Layout 3 | `48e666f70906`  |
| 3356   | Layout 3 | `48e666f70906`  |
| 3349   | Layout 3 | `48e666f70906`  |
| 3342   | Layout 3 | `48e666f70906`  |
| 3335   | Layout 3 | `48e666f70906`  |
| 3326   | Layout 3 | `48e666f70906`  |
| 3321   | Layout 3 | `48e666f70906`  |
| 3314   | Layout 3 | `48e666f70906`  |
| 3303   | Layout 3 | `48e666f70906`  |
| 3302   | Layout 3 | `48e666f70906`  |
| 3293   | Layout 3 | `48e666f70906`  |
| 3283   | Layout 3 | `48e666f70906`  |
| 3275   | Layout 3 | `48e666f70906`  |
| 3267   | Layout 3 | `48e666f70906`  |
| 3258   | Layout 3 | `48e666f70906`  |
| 3251   | Layout 3 | `48e666f70906`  |
| 3242   | Layout 3 | `48e666f70906`  |
| 3235   | Layout 3 | `48e666f70906`  |
| 3229   | Layout 3 | `48e666f70906`  |
| 3212   | Layout 3 | `48e666f70906`  |
| 3203   | Layout 3 | `48e666f70906`  |
| 3193   | Layout 3 | `48e666f70906`  |
| 3186   | Layout 3 | `48e666f70906`  |
| 3177   | Layout 3 | `48e666f70906`  |
| 3169   | Layout 3 | `48e666f70906`  |
| 3158   | Layout 3 | `48e666f70906`  |
| 3151   | Layout 3 | `48e666f70906`  |
| 3144   | Layout 3 | `48e666f70906`  |
| 3133   | Layout 3 | `48e666f70906`  |
| 3125   | Layout 3 | `48e666f70906`  |
| 3118   | Layout 3 | `48e666f70906`  |
| 3111   | Layout 3 | `48e666f70906`  |
| 3103   | Layout 3 | `48e666f70906`  |
| 3095   | Layout 3 | `48e666f70906`  |
| 3086   | Layout 3 | `48e666f70906`  |
| 3072   | Layout 3 | `48e666f70906`  |
| 3062   | Layout 3 | `48e666f70906`  |
| 3052   | Layout 3 | `48e666f70906`  |
| 3045   | Layout 3 | `48e666f70906`  |
| 3037   | Layout 3 | `48e666f70906`  |
| 3030   | Layout 3 | `48e666f70906`  |
| 3021   | Layout 3 | `48e666f70906`  |
| 3012   | Layout 3 | `48e666f70906`  |
| 3002   | Layout 3 | `48e666f70906`  |
| 2995   | Layout 3 | `48e666f70906`  |
| 2987   | Layout 3 | `48e666f70906`  |
| 2978   | Layout 3 | `48e666f70906`  |
| 2970   | Layout 3 | `48e666f70906`  |
| 2959   | Layout 3 | `48e666f70906`  |
| 2951   | Layout 3 | `48e666f70906`  |
| 2942   | Layout 3 | `48e666f70906`  |
| 2935   | Layout 3 | `48e666f70906`  |
| 2932   | Layout 3 | `48e666f70906`  |
| 2923   | Layout 3 | `48e666f70906`  |
| 2919   | Layout 3 | `48e666f70906`  |
| 2907   | Layout 3 | `48e666f70906`  |
| 2900   | Layout 3 | `48e666f70906`  |
| 2891   | Layout 3 | `48e666f70906`  |
| 2882   | Layout 3 | `48e666f70906`  |
| 2872   | Layout 3 | `48e666f70906`  |
| 2863   | Layout 3 | `48e666f70906`  |
| 2855   | Layout 3 | `48e666f70906`  |
| 2849   | Layout 3 | `48e666f70906`  |
| 2844   | Layout 3 | `48e666f70906`  |
| 2834   | Layout 3 | `48e666f70906`  |
| 2825   | Layout 3 | `48e666f70906`  |
| 2819   | Layout 3 | `48e666f70906`  |
| 2811   | Layout 3 | `48e666f70906`  |
| 2803   | Layout 3 | `48e666f70906`  |
| 2794   | Layout 3 | `48e666f70906`  |
| 2783   | Layout 3 | `48e666f70906`  |
| 2774   | Layout 3 | `48e666f70906`  |
| 2765   | Layout 3 | `48e666f70906`  |
| 2756   | Layout 3 | `48e666f70906`  |
| 2750   | Layout 3 | `48e666f70906`  |
| 2743   | Layout 3 | `48e666f70906`  |
| 2736   | Layout 3 | `48e666f70906`  |
| 2726   | Layout 3 | `48e666f70906`  |
| 2717   | Layout 3 | `48e666f70906`  |
| 2709   | Layout 3 | `48e666f70906`  |
| 2703   | Layout 3 | `48e666f70906`  |
| 2695   | Layout 3 | `48e666f70906`  |
| 2684   | Layout 3 | `48e666f70906`  |
| 2672   | Layout 3 | `48e666f70906`  |
| 2665   | Layout 3 | `48e666f70906`  |
| 2657   | Layout 3 | `48e666f70906`  |
| 2649   | Layout 3 | `48e666f70906`  |
| 2644   | Layout 3 | `48e666f70906`  |
| 2637   | Layout 3 | `48e666f70906`  |
| 2629   | Layout 3 | `48e666f70906`  |
| 2619   | Layout 3 | `48e666f70906`  |
| 2612   | Layout 3 | `48e666f70906`  |
| 2606   | Layout 3 | `48e666f70906`  |
| 2602   | Layout 3 | `48e666f70906`  |
| 2601   | Layout 3 | `48e666f70906`  |
| 2592   | Layout 3 | `48e666f70906`  |
| 2583   | Layout 3 | `48e666f70906`  |
| 2575   | Layout 3 | `48e666f70906`  |
| 2567   | Layout 3 | `48e666f70906`  |
| 2560   | Layout 3 | `48e666f70906`  |
| 2553   | Layout 3 | `48e666f70906`  |
| 2545   | Layout 3 | `48e666f70906`  |
| 2538   | Layout 3 | `48e666f70906`  |
| 2529   | Layout 3 | `48e666f70906`  |
| 2519   | Layout 3 | `48e666f70906`  |
| 2513   | Layout 3 | `48e666f70906`  |
| 2510   | Layout 3 | `48e666f70906`  |
| 2507   | Layout 3 | `48e666f70906`  |
| 2503   | Layout 3 | `48e666f70906`  |
| 2498   | Layout 3 | `48e666f70906`  |
| 2492   | Layout 3 | `48e666f70906`  |
| 2487   | Layout 3 | `48e666f70906`  |
| 2480   | Layout 3 | `48e666f70906`  |
| 2474   | Layout 3 | `48e666f70906`  |
| 2468   | Layout 3 | `48e666f70906`  |
| 2460   | Layout 3 | `48e666f70906`  |
| 2453   | Layout 3 | `48e666f70906`  |
| 2444   | Layout 3 | `48e666f70906`  |
| 2438   | Layout 3 | `48e666f70906`  |
| 2434   | Layout 3 | `48e666f70906`  |
| 2429   | Layout 3 | `48e666f70906`  |
| 2421   | Layout 3 | `48e666f70906`  |
| 2414   | Layout 3 | `48e666f70906`  |
| 2407   | Layout 3 | `48e666f70906`  |
| 2401   | Layout 3 | `48e666f70906`  |
| 2397   | Layout 3 | `48e666f70906`  |
| 2393   | Layout 3 | `48e666f70906`  |
| 2384   | Layout 3 | `48e666f70906`  |
| 2378   | Layout 3 | `48e666f70906`  |
| 2372   | Layout 3 | `48e666f70906`  |
| 2358   | Layout 3 | `48e666f70906`  |
| 2352   | Layout 3 | `48e666f70906`  |
| 2347   | Layout 3 | `48e666f70906`  |
| 2343   | Layout 3 | `48e666f70906`  |
| 2335   | Layout 3 | `48e666f70906`  |
| 2327   | Layout 3 | `48e666f70906`  |
| 2324   | Layout 3 | `48e666f70906`  |
| 2319   | Layout 3 | `48e666f70906`  |
| 2313   | Layout 3 | `48e666f70906`  |
| 2308   | Layout 3 | `48e666f70906`  |
| 2302   | Layout 3 | `48e666f70906`  |
| 2295   | Layout 3 | `48e666f70906`  |
| 2290   | Layout 3 | `48e666f70906`  |
| 2284   | Layout 3 | `48e666f70906`  |
| 2276   | Layout 3 | `48e666f70906`  |
| 2269   | Layout 3 | `48e666f70906`  |
| 2259   | Layout 3 | `48e666f70906`  |
| 2250   | Layout 3 | `48e666f70906`  |
| 2243   | Layout 3 | `48e666f70906`  |
| 2235   | Layout 3 | `48e666f70906`  |
| 2229   | Layout 2 | `48e666f70906`  |
| 2224   | Layout 2 | `48e666f70906`  |
| 2218   | Layout 2 | `48e666f70906`  |
| 2215   | Layout 2 | `48e666f70906`  |
| 2207   | Layout 2 | `48e666f70906`  |
| 2203   | Layout 2 | `48e666f70906`  |
| 2196   | Layout 2 | `48e666f70906`  |
| 2192   | Layout 2 | `48e666f70906`  |
| 2189   | Layout 2 | `48e666f70906`  |
| 2183   | Layout 2 | `48e666f70906`  |
| 2179   | Layout 2 | `48e666f70906`  |
| 2171   | Layout 2 | `48e666f70906`  |
| 2163   | Layout 2 | `48e666f70906`  |
| 2156   | Layout 2 | `48e666f70906`  |
| 2151   | Layout 2 | `48e666f70906`  |
| 2147   | Layout 2 | `48e666f70906`  |
| 2142   | Layout 2 | `48e666f70906`  |
| 2138   | Layout 2 | `48e666f70906`  |
| 2134   | Layout 2 | `48e666f70906`  |
| 2130   | Layout 2 | `48e666f70906`  |
| 2122   | Layout 2 | `48e666f70906`  |
| 2107   | Layout 2 | `48e666f70906`  |
| 2098   | Layout 2 | `48e666f70906`  |
| 2089   | Layout 2 | `48e666f70906`  |
| 2081   | Layout 2 | `48e666f70906`  |
| 2073   | Layout 2 | `48e666f70906`  |
| 2067   | Layout 2 | `48e666f70906`  |
| 2063   | Layout 2 | `48e666f70906`  |
| 2059   | Layout 2 | `48e666f70906`  |
| 2052   | Layout 2 | `48e666f70906`  |
| 2044   | Layout 2 | `48e666f70906`  |
| 2039   | Layout 2 | `48e666f70906`  |
| 2032   | Layout 2 | `48e666f70906`  |
| 2025   | Layout 2 | `48e666f70906`  |
| 2011   | Layout 2 | `48e666f70906`  |
| 2005   | Layout 2 | `48e666f70906`  |
| 2000   | Layout 2 | `48e666f70906`  |
| 1996   | Layout 2 | `48e666f70906`  |
| 1991   | Layout 2 | `48e666f70906`  |
| 1985   | Layout 2 | `48e666f70906`  |
| 1980   | Layout 2 | `48e666f70906`  |
| 1969   | Layout 2 | `48e666f70906`  |
| 1964   | Layout 2 | `48e666f70906`  |
| 1958   | Layout 2 | `48e666f70906`  |
| 1950   | Layout 2 | `48e666f70906`  |
| 1945   | Layout 2 | `48e666f70906`  |
| 1937   | Layout 2 | `48e666f70906`  |
| 1933   | Layout 2 | `48e666f70906`  |
| 1927   | Layout 2 | `48e666f70906`  |
| 1921   | Layout 2 | `48e666f70906`  |
| 1914   | Layout 2 | `48e666f70906`  |
| 1908   | Layout 2 | `48e666f70906`  |
| 1897   | Layout 2 | `48e666f70906`  |
| 1892   | Layout 2 | `48e666f70906`  |
| 1886   | Layout 2 | `48e666f70906`  |
| 1881   | Layout 2 | `48e666f70906`  |
| 1871   | Layout 2 | `48e666f70906`  |
| 1866   | Layout 2 | `48e666f70906`  |
| 1862   | Layout 2 | `48e666f70906`  |
| 1854   | Layout 2 | `48e666f70906`  |
| 1846   | Layout 2 | `48e666f70906`  |
| 1838   | Layout 2 | `48e666f70906`  |
| 1832   | Layout 2 | `48e666f70906`  |
| 1826   | Layout 2 | `48e666f70906`  |
| 1822   | Layout 2 | `48e666f70906`  |
| 1818   | Layout 2 | `48e666f70906`  |
| 1804   | Layout 2 | `48e666f70906`  |
| 1794   | Layout 2 | `48e666f70906`  |
| 1790   | Layout 2 | `48e666f70906`  |
| 1784   | Layout 2 | `48e666f70906`  |
| 1774   | Layout 2 | `48e666f70906`  |
| 1771   | Layout 2 | `48e666f70906`  |
| 1762   | Layout 2 | `48e666f70906`  |
| 1759   | Layout 2 | `48e666f70906`  |
| 1754   | Layout 2 | `48e666f70906`  |
| 1749   | Layout 2 | `48e666f70906`  |
| 1743   | Layout 1 | `48e666f70906`  |
| 1737   | Layout 1 | `48e666f70906`  |
| 1731   | Layout 1 | `48e666f70906`  |
| 1725   | Layout 1 | `48e666f70906`  |
| 1717   | Layout 1 | `48e666f70906`  |
| 1710   | Layout 1 | `48e666f70906`  |
| 1704   | Layout 1 | `48e666f70906`  |
| 1698   | Layout 1 | `48e666f70906`  |
| 1690   | Layout 1 | `48e666f70906`  |
| 1685   | Layout 1 | `48e666f70906`  |
| 1680   | Layout 1 | `48e666f70906`  |
| 1674   | Layout 1 | `48e666f70906`  |
| 1668   | Layout 1 | `48e666f70906`  |
| 1659   | Layout 1 | `48e666f70906`  |
| 1649   | Layout 1 | `48e666f70906`  |
| 1642   | Layout 1 | `48e666f70906`  |
| 1636   | Layout 1 | `48e666f70906`  |
| 1628   | Layout 1 | `48e666f70906`  |
| 1622   | Layout 1 | `48e666f70906`  |
| 1614   | Layout 1 | `48e666f70906`  |
| 1608   | Layout 1 | `48e666f70906`  |
| 1602   | Layout 1 | `48e666f70906`  |
| 1598   | Layout 1 | `48e666f70906`  |
| 1594   | Layout 1 | `48e666f70906`  |
| 1590   | Layout 1 | `48e666f70906`  |
| 1587   | Layout 1 | `48e666f70906`  |
| 1584   | Layout 1 | `48e666f70906`  |
| 1579   | Layout 1 | `48e666f70906`  |
| 1572   | Layout 1 | `48e666f70906`  |
| 1565   | Layout 1 | `48e666f70906`  |
| 1559   | Layout 1 | `48e666f70906`  |
| 1554   | Layout 1 | `48e666f70906`  |
| 1547   | Layout 1 | `48e666f70906`  |
| 1537   | Layout 1 | `48e666f70906`  |
| 1529   | Layout 1 | `48e666f70906`  |
| 1524   | Layout 1 | `48e666f70906`  |
| 1519   | Layout 1 | `48e666f70906`  |
| 1509   | Layout 1 | `48e666f70906`  |
| 1506   | Layout 1 | `48e666f70906`  |
| 1504   | Layout 1 | `48e666f70906`  |
| 1500   | Layout 1 | `48e666f70906`  |
| 1493   | Layout 1 | `48e666f70906`  |
| 1489   | Layout 1 | `48e666f70906`  |
| 1485   | Layout 1 | `48e666f70906`  |
| 1481   | Layout 1 | `48e666f70906`  |
| 1474   | Layout 1 | `48e666f70906`  |
| 1466   | Layout 1 | `48e666f70906`  |
| 1462   | Layout 1 | `48e666f70906`  |
| 1459   | Layout 1 | `48e666f70906`  |
| 1453   | Layout 1 | `48e666f70906`  |
| 1450   | Layout 1 | `48e666f70906`  |
| 1445   | Layout 1 | `48e666f70906`  |
| 1439   | Layout 1 | `48e666f70906`  |
| 1433   | Layout 1 | `48e666f70906`  |
| 1430   | Layout 1 | `48e666f70906`  |
| 1426   | Layout 1 | `48e666f70906`  |
| 1421   | Layout 1 | `48e666f70906`  |
| 1417   | Layout 1 | `48e666f70906`  |
| 1416   | Layout 1 | `48e666f70906`  |
| 1409   | Layout 1 | `48e666f70906`  |
| 1405   | Layout 1 | `48e666f70906`  |
| 1401   | Layout 1 | `48e666f70906`  |
| 1396   | Layout 1 | `48e666f70906`  |
| 1391   | Layout 1 | `48e666f70906`  |
| 1390   | Layout 1 | `48e666f70906`  |
| 1386   | Layout 1 | `48e666f70906`  |
| 1381   | Layout 1 | `48e666f70906`  |
| 1379   | Layout 1 | `48e666f70906`  |
| 1372   | Layout 1 | `48e666f70906`  |
| 1366   | Layout 1 | `48e666f70906`  |
| 1364   | Layout 1 | `48e666f70906`  |
| 1363   | Layout 1 | `48e666f70906`  |
| 1360   | Layout 1 | `48e666f70906`  |
| 1358   | Layout 1 | `48e666f70906`  |
| 1355   | Layout 1 | `48e666f70906`  |
| 1351   | Layout 1 | `48e666f70906`  |
| 1348   | Layout 1 | `48e666f70906`  |
| 1346   | Layout 1 | `48e666f70906`  |
| 1341   | Layout 1 | `48e666f70906`  |
| 1340   | Layout 1 | `48e666f70906`  |
| 1338   | Layout 1 | `48e666f70906`  |
| 1335   | Layout 1 | `48e666f70906`  |
| 1333   | Layout 1 | `48e666f70906`  |
| 1329   | Layout 1 | `48e666f70906`  |
| 1327   | Layout 1 | `48e666f70906`  |
| 1324   | Layout 1 | `48e666f70906`  |
| 1321   | Layout 1 | `48e666f70906`  |
| 1319   | Layout 1 | `48e666f70906`  |
| 1318   | Layout 1 | `48e666f70906`  |
| 1316   | Layout 1 | `48e666f70906`  |
| 1313   | Layout 1 | `48e666f70906`  |
| 1311   | Layout 1 | `48e666f70906`  |
| 1309   | Layout 1 | `48e666f70906`  |
| 1304   | Layout 1 | `48e666f70906`  |
| 1292   | Layout 1 | `48e666f70906`  |
| 1286   | Layout 1 | `48e666f70906`  |
| 1280   | Layout 1 | `48e666f70906`  |
| 1276   | Layout 1 | `48e666f70906`  |
| 1267   | Layout 1 | `48e666f70906`  |
| 1261   | Layout 1 | `48e666f70906`  |
| 1256   | Layout 1 | `48e666f70906`  |
| 1250   | Layout 1 | `48e666f70906`  |
| 1246   | No file  | `48e666f70906`  |
| 1239   | No file  | `48e666f70906`  |
| 1230   | No file  | `48e666f70906`  |
| 1226   | No file  | `48e666f70906`  |
| 1220   | No file  | `48e666f70906`  |
| 1217   | No file  | `48e666f70906`  |
| 1211   | No file  | `48e666f70906`  |
| 1210   | No file  | `48e666f70906`  |
| 1208   | No file  | `48e666f70906`  |
| 1203   | No file  | `48e666f70906`  |
| 1197   | No file  | `48e666f70906`  |
| 1194   | No file  | `48e666f70906`  |
| 1192   | No file  | `48e666f70906`  |
| 1187   | No file  | `48e666f70906`  |
| 1183   | No file  | `48e666f70906`  |
| 1177   | No file  | `48e666f70906`  |
| 1173   | No file  | `48e666f70906`  |
| 1167   | No file  | `48e666f70906`  |
| 1164   | No file  | `48e666f70906`  |
| 1156   | No file  | `48e666f70906`  |
| 1149   | No file  | `48e666f70906`  |
| 1144   | No file  | `48e666f70906`  |
| 1137   | No file  | `48e666f70906`  |
| 1132   | No file  | `48e666f70906`  |
| 1127   | No file  | `48e666f70906`  |
| 1122   | No file  | `48e666f70906`  |
| 1118   | No file  | `48e666f70906`  |
| 1114   | No file  | `48e666f70906`  |
| 1109   | No file  | `48e666f70906`  |
| 1102   | No file  | `48e666f70906`  |
| 1096   | No file  | `48e666f70906`  |
| 1088   | No file  | `48e666f70906`  |
| 1081   | No file  | `48e666f70906`  |
| 1076   | No file  | `48e666f70906`  |
| 1069   | No file  | `48e666f70906`  |
| 1064   | No file  | `48e666f70906`  |
| 1058   | No file  | `48e666f70906`  |
| 1051   | No file  | `48e666f70906`  |
| 1044   | No file  | `48e666f70906`  |
| 1036   | No file  | `48e666f70906`  |
| 1026   | No file  | `48e666f70906`  |
| 1016   | No file  | `48e666f70906`  |
| 1009   | No file  | `48e666f70906`  |
| 1005   | No file  | `48e666f70906`  |
| 1000   | No file  | `48e666f70906`  |
| 998    | No file  | `48e666f70906`  |
| 990    | No file  | `48e666f70906`  |
| 979    | No file  | `48e666f70906`  |
| 972    | No file  | `48e666f70906`  |
| 963    | No file  | `48e666f70906`  |
| 955    | No file  | `48e666f70906`  |
| 946    | No file  | `48e666f70906`  |
| 938    | No file  | `48e666f70906`  |
| 927    | No file  | `48e666f70906`  |
| 911    | No file  | `48e666f70906`  |
| 904    | No file  | `48e666f70906`  |
| 899    | No file  | `48e666f70906`  |
| 894    | No file  | `48e666f70906`  |
| 885    | No file  | `48e666f70906`  |
| 879    | No file  | `48e666f70906`  |
| 872    | No file  | `48e666f70906`  |
| 864    | No file  | `48e666f70906`  |
| 855    | No file  | `48e666f70906`  |
| 853    | No file  | `48e666f70906`  |
| 845    | No file  | `48e666f70906`  |
| 837    | No file  | `48e666f70906`  |
| 829    | No file  | `48e666f70906`  |
| 822    | No file  | `48e666f70906`  |
| 814    | No file  | `48e666f70906`  |
| 805    | No file  | `48e666f70906`  |
| 794    | No file  | `48e666f70906`  |
| 787    | No file  | `48e666f70906`  |
| 780    | No file  | `48e666f70906`  |
| 771    | No file  | `48e666f70906`  |
| 760    | No file  | `48e666f70906`  |
| 748    | No file  | `48e666f70906`  |
| 741    | No file  | `48e666f70906`  |
| 736    | No file  | `48e666f70906`  |
| 731    | No file  | `48e666f70906`  |
| 723    | No file  | `48e666f70906`  |
| 711    | No file  | `48e666f70906`  |
| 707    | No file  | `48e666f70906`  |
| 697    | No file  | `48e666f70906`  |
| 689    | No file  | `48e666f70906`  |
| 683    | No file  | `48e666f70906`  |
| 678    | No file  | `48e666f70906`  |
| 670    | No file  | `48e666f70906`  |
| 661    | No file  | `48e666f70906`  |
| 656    | No file  | `48e666f70906`  |
| 652    | No file  | `48e666f70906`  |
| 643    | No file  | `48e666f70906`  |
| 637    | No file  | `48e666f70906`  |
| 630    | No file  | `48e666f70906`  |
| 627    | No file  | `48e666f70906`  |
| 621    | No file  | `48e666f70906`  |
| 617    | No file  | `48e666f70906`  |
| 615    | No file  | `48e666f70906`  |
| 606    | No file  | `48e666f70906`  |
| 599    | No file  | `48e666f70906`  |
| 592    | No file  | `48e666f70906`  |
| 586    | No file  | `48e666f70906`  |
| 577    | No file  | `48e666f70906`  |
| 569    | No file  | `48e666f70906`  |
| 561    | No file  | `48e666f70906`  |
| 554    | No file  | `48e666f70906`  |
| 542    | No file  | `48e666f70906`  |
| 532    | No file  | `48e666f70906`  |
| 531    | No file  | `48e666f70906`  |
| 526    | No file  | `48e666f70906`  |
| 521    | No file  | `48e666f70906`  |
| 517    | No file  | `48e666f70906`  |
| 510    | No file  | `48e666f70906`  |
| 508    | No file  | `48e666f70906`  |
| 504    | No file  | `48e666f70906`  |
| 497    | No file  | `48e666f70906`  |
| 491    | No file  | `48e666f70906`  |
| 485    | No file  | `48e666f70906`  |
| 478    | No file  | `48e666f70906`  |
| 472    | No file  | `48e666f70906`  |
| 466    | No file  | `48e666f70906`  |
| 457    | No file  | `48e666f70906`  |
| 452    | No file  | `48e666f70906`  |
| 449    | No file  | `48e666f70906`  |
| 435    | No file  | `48e666f70906`  |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                                                                       |
| ----------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `attendanceoffset.dbss` | Optional | `attendance_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`   | Optional | Event titles, period and claim texts (LOC type 49) and the reward item names (LOC type 0)  |

All multi-byte values are little-endian.

## Layout 3

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type       | Field | Notes                |
| ------- | ---------- | ----- | -------------------- |
| `+0x00` | u32        | count | Number of events     |
| `+0x04` | Row[count] | rows  | See Row              |

### Row (variable: 126 bytes + texts, rewards and guild levels)

| Offset                           | Type                   | Field                          | Notes                                                                                                      |
| -------------------------------- | ---------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `+0x00`                          | u16                    | attendance_key                 | Row key; LOC type 49 `str_id1` of the texts                                                                |
| `+0x02`                          | str16                  | title_kr                       | Korean title (`복귀 길드 보상`); some old rows are English (`Loyal`)                                         |
| `title_kr+0x00`                  | bytes[8]               | unknown_title_00               | All zero on every row of clients 1784 and 3482                                                             |
| `title_kr+0x08`                  | str16                  | start_date                     | Event start as text, `2026-08-07 00:00`; older rows drop leading zeros (`2016-7-21 00:00`)                  |
| `start_date+0x00`                | bytes[8]               | unknown_start_date_00          | All zero on every row of clients 1784 and 3482                                                             |
| `start_date+0x08`                | str16                  | attendance_end_date            | Last check-in time as text                                                                                 |
| `attendance_end_date+0x00`       | bytes[8]               | unknown_attendance_end_date_00 | All zero on every row of clients 1784 and 3482                                                             |
| `attendance_end_date+0x08`       | str16                  | reward_end_date                | Last time to claim rewards as text; later than `attendance_end_date` on key 8 (client 1784)                 |
| `reward_end_date+0x00`           | bytes[8]               | unknown_reward_end_date_00     | All zero on every row of clients 1784 and 3482                                                             |
| `reward_end_date+0x08`           | str16                  | event_period_kr                | Korean period text the window shows after its event period label, `getPeriodDate()`                        |
| `event_period_kr+0x00`           | str16                  | event_expired_kr               | Korean claim deadline text the window shows after its claim period label, `getExpireDate()`                |
| `event_expired_kr+0x00`          | bytes[8]               | unknown_event_expired_kr_00    | All zero on every row of clients 1784 and 3482                                                             |
| `event_expired_kr+0x08`          | u8                     | user_connection_type           | Which players the event is for; see User Connection Types                                                  |
| `event_expired_kr+0x09`          | u32                    | reward_count                   | Login days with a reward, `getRewardCount()`; 2 to 35 on client 3482                                       |
| `event_expired_kr+0x0D`          | Reward[reward_count]   | rewards                        | See Reward                                                                                                 |
| `rewards+0x00`                   | u32                    | overlap_count                  | Extra check-ins on a `day_of_week` day; `1` on every row of clients 1784 and 3482; see Notes               |
| `rewards+0x04`                   | u32                    | overlap_waiting_time           | Wait before the extra check-in in seconds; `3600` (60 minutes) on every row of clients 1784 and 3482       |
| `rewards+0x08`                   | u32                    | unknown_rewards_08             | `0` on every row of clients 1784 and 3482                                                                  |
| `rewards+0x0C`                   | u8[7]                  | day_of_week                    | One flag per weekday with an extra check-in, index = sheet day number; `1` at 0 and 6 (the weekend) on most rows |
| `rewards+0x13`                   | u32                    | display_order                  | Tab order, `getDisplayOrder()`; equals `attendance_key` on 280 of 298 rows (client 3482)                   |
| `rewards+0x17`                   | bytes[4]               | unknown_rewards_17             | All zero on every row of clients 1784 and 3482                                                             |
| `rewards+0x1B`                   | u32                    | guild_level_count              | `0`, or `3` or `4` on the guild events                                                                     |
| `rewards+0x1F`                   | u16[guild_level_count] | guild_level                    | `2, 3, 4` or `1, 2, 3, 4` on the guild events                                                              |

On client 3482 the file holds 298 events with 6,810 rewards.

### Reward (variable: 25 bytes + description text)

| Offset           | Type  | Field      | Notes                                                                                     |
| ---------------- | ----- | ---------- | ----------------------------------------------------------------------------------------- |
| `+0x00`          | u32   | day        | Login day, `1` up to `reward_count` in order on every row of clients 1784 and 3482        |
| `+0x04`          | u32   | item_id    | Reward item, `getRewardItem(index)`; below `2^24` on every reward of client 3482          |
| `+0x08`          | u64   | item_count | Item count                                                                                |
| `+0x10`          | u8    | grade_type | Day slot frame, `getRewardItemGradeType(index)`; see Notes                                  |
| `+0x11`          | str16 | desc_kr    | Empty on every reward of clients 1784 and 3482                                             |

### `attendanceoffset.dbss`

Bare offset table into `attendance.dbss` (no PABR magic, no trailer), read
by `parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type              | Field | Notes                              |
| ------- | ----------------- | ----- | ---------------------------------- |
| `+0x00` | u32               | count | Equals the `attendance.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                     |

### Offset Row (10 bytes)

| Offset  | Type | Field          | Notes                                                              |
| ------- | ---- | -------------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | attendance_key | Key of the row it points at                                        |
| `+0x02` | u32  | data_offset    | Absolute offset of the row in `attendance.dbss`, at `attendance_key` |
| `+0x06` | u32  | data_size      | The whole row                                                      |

The index rows are in another order than the file; on clients 1784 and
3482 every index row points at the row with its key.

## Layout 2

On clients 1784 to 2107 the row ends after `unknown_rewards_17`: there is
no `guild_level_count` and no `guild_level`. Only the Row differs from
Layout 3.

### Row (variable: 122 bytes + texts and rewards)

| Offset                     | Type                 | Field                          | Notes                                      |
| -------------------------- | -------------------- | ------------------------------ | ------------------------------------------ |
| `+0x00`                    | u16                  | attendance_key                 |                                            |
| `+0x02`                    | str16                | title_kr                       |                                            |
| `title_kr+0x00`            | bytes[8]             | unknown_title_00               |                                            |
| `title_kr+0x08`            | str16                | start_date                     |                                            |
| `start_date+0x00`          | bytes[8]             | unknown_start_date_00          |                                            |
| `start_date+0x08`          | str16                | attendance_end_date            |                                            |
| `attendance_end_date+0x00` | bytes[8]             | unknown_attendance_end_date_00 |                                            |
| `attendance_end_date+0x08` | str16                | reward_end_date                |                                            |
| `reward_end_date+0x00`     | bytes[8]             | unknown_reward_end_date_00     |                                            |
| `reward_end_date+0x08`     | str16                | event_period_kr                |                                            |
| `event_period_kr+0x00`     | str16                | event_expired_kr               |                                            |
| `event_expired_kr+0x00`    | bytes[8]             | unknown_event_expired_kr_00    |                                            |
| `event_expired_kr+0x08`    | u8                   | user_connection_type           |                                            |
| `event_expired_kr+0x09`    | u32                  | reward_count                   |                                            |
| `event_expired_kr+0x0D`    | Reward[reward_count] | rewards                        |                                            |
| `rewards+0x00`             | u32                  | overlap_count                  |                                            |
| `rewards+0x04`             | u32                  | overlap_waiting_time           |                                            |
| `rewards+0x08`             | u32                  | unknown_rewards_08             |                                            |
| `rewards+0x0C`             | u8[7]                | day_of_week                    |                                            |
| `rewards+0x13`             | u32                  | display_order                  |                                            |
| `rewards+0x17`             | bytes[4]             | unknown_rewards_17             | The row ends here                          |

## Layout 1

On clients 1256 to 1636 a Reward has no `desc_kr`. Only the Reward
differs from Layout 2; the Row is the same as there.

### Reward (17 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u32  | day        |       |
| `+0x04` | u32  | item_id    |       |
| `+0x08` | u64  | item_count |       |
| `+0x10` | u8   | grade_type |       |

## User Connection Types

`user_connection_type` against the event titles of client 3482:

| Value | Players                | Rows (client 3482) | Titles                                                        |
| ----- | ---------------------- | ------------------ | ------------------------------------------------------------- |
| 0     | Everyone               | 203                | `일반 접속보상` (general), `Loyal`, `스페셜 접속보상`, `길드 접속보상` |
| 1     | Returning players      | 48                 | `돌아오셨네요!`, `Returning`, `복귀 접속보상`, `복귀 길드 보상`      |
| 2     | New players            | 46                 | `환영합니다!`, `Rookie`, `신규 접속보상`, `신규 길드 보상`          |
| 3     | Pre-transfer players   | 1                  | `사전이관 접속보상` (key 103)                                   |

## Field Names

The `Attendance_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Key`, `Title`, `DisplayOrder`,
`UserConnectionType`, `OverlapCount`, `OverlapWaitingTime`, `DayOfWeek`,
`GuildLevel`, `StartDate`, `EventPeriod`, `TimeZone`, `AttendanceEndDate`,
`AcceptCondition`, `EventExpired`, `RewardEndDate`, and per day `dayN`,
`rewardN` (item and count), `GradeTypeN` and `descN` for N = 1 to 60, 155
rows. Keys 1 to 131 (130 rows, no key 46) are the events of the 1784
client file; from key 132 on the sheet holds other events than the client
(month rows `January` to `December`, keys 132 to 144 and 445 to 456). The
comparison covers the 130 keys. `DayOfWeek` is a list of day numbers (`0, 6`), each
setting that `day_of_week` flag; `GuildLevel` is a list (`2,3,4`).

| Field                | Column               | Same value (client 1784) | Same value (client 3482) |
| -------------------- | -------------------- | ------------------------ | ------------------------ |
| attendance_key       | `Key`                | 130 of 130               | 130 of 130               |
| title_kr             | `Title`              | 130 of 130               | 130 of 130               |
| start_date           | `StartDate`          | 130 of 130               | 130 of 130               |
| attendance_end_date  | `AttendanceEndDate`  | 130 of 130               | 130 of 130               |
| reward_end_date      | `RewardEndDate`      | 130 of 130               | 130 of 130               |
| event_period_kr      | `EventPeriod`        | 130 of 130               | 130 of 130               |
| event_expired_kr     | `EventExpired`       | 130 of 130               | 130 of 130               |
| user_connection_type | `UserConnectionType` | 130 of 130               | 130 of 130               |
| overlap_count        | `OverlapCount`       | 130 of 130               | 130 of 130               |
| overlap_waiting_time | `OverlapWaitingTime` | 130 of 130               | 130 of 130               |
| day_of_week          | `DayOfWeek`          | 130 of 130               | 130 of 130               |
| display_order        | `DisplayOrder`       | 130 of 130               | 130 of 130               |
| guild_level          | `GuildLevel`         | no field                 | 130 of 130               |
| day                  | `dayN`               | 3,361 of 3,361           | 3,361 of 3,361           |
| item_id              | `rewardN` item       | 3,361 of 3,361           | 2,815 of 3,361           |
| item_count           | `rewardN` count      | 3,361 of 3,361           | 3,359 of 3,361           |
| grade_type           | `GradeTypeN`         | 3,361 of 3,361           | 3,361 of 3,361           |
| desc_kr              | `descN`              | 3,361 of 3,361           | 3,361 of 3,361           |

The reward rows are compared by day. On client 3482 old events point at
newer items where the client replaced one (key 1 day 2: `16002` in the
sheet, `16001` in the file). A day whose `rewardN` cell is empty (key 123,
days 34 and 35) has no Reward in the file. The 1784 file has no
`guild_level` although the sheet has the column; on client 3482 the five
guild events among the 130 keys (17, 25, 38, 67, 106) hold `2, 3, 4` as
the sheet does. `TimeZone` is `0` and `AcceptCondition` empty on every
row, so neither can be placed on a field.

## Notes

- LOC type 49 holds the event texts under `str_id1 = attendance_key`,
  `str_id2 = 0` and a service code in `str_id3` (`12`, as in LOC type 50):
  `str_id4 = 0` the title (`Guild Returnee` for key 527), `1` the period
  text, `2` the claim deadline text and `2 + day` a reward description
  (key 197 has days 1 to 35). On client 3482 the en file has a code `12`
  title for all 298 events and for keys 46, 515, 516 and 517, which the
  file does not hold; keys 1 to 25 also have rows under code `0`, key 1
  under code `26`.
- `grade_type` picks the day slot frame in
  `Combine/Etc/Combine_ETC_AccessReward_00.dds`
  (`PaGlobalFunc_DailyStamp_All_ChangeTexture`): `1` the top row
  (`y1 = 1`), `2` the middle row (`y1 = 97`), `0` the bottom row
  (`y1 = 193`), for every claim state.
- The window's note (LOC type 37 key 526457345) reads "You can check in
  up to two times a day during weekends, ... (This does not apply to Guild
  Login Rewards)". The fields line up with it: `overlap_count` `1`,
  `day_of_week` flags at 0 and 6, and no flags on 32 of the 34 guild
  events of client 3482. The window Lua checks the second check-in with
  `isPossibleOverlapAttendance()` and
  `ToClient_getWaitingTimeForNextAttendance(key)`.
- On client 3482, 34 events hold guild levels, all with a guild title
  (`길드 접속보상`, `복귀 길드 보상`, `신규 길드 보상`). Keys 17 and 25 have
  `day_of_week` flags 0 and 6, as their sheet rows do.

## Open Questions

### What the Zero Blocks After the Texts Hold

Five 8-byte blocks (`unknown_title_00`, `unknown_start_date_00`,
`unknown_attendance_end_date_00`, `unknown_reward_end_date_00`,
`unknown_event_expired_kr_00`) are zero on every row of clients 1784 and
3482. Three follow a date text, so they may be the parsed times the client
fills in on load; `AcceptCondition` (an empty text in the sheet) would
also be 8 zero bytes as an empty `str16`. A row with an accept condition
would show which block is a text.

### What unknown_rewards_08 and unknown_rewards_17 Hold

`unknown_rewards_08` is a u32 `0` and `unknown_rewards_17` four zero bytes
on every row. `TimeZone` (`0` on every sheet row) is the one sheet column
left with a number; whether `display_order` is a u32 or the low half of a
u64 that takes in `unknown_rewards_17` is also open.
