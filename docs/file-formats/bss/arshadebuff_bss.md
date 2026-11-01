# `arshadebuff.bss` Format

## Purpose

The Arena of Arsha debuff steps: one row per step with its timer and two
values that are `0` on every row. On client 3474 the file has 3 rows with
timers `0`, `330000` and `660000`. The client Lua turns the debuff on and
off with `ToClient_ArshaDebuffOnOff(isOn)` (`panel_window_arsha_func_all`)
and listens for `FromClient_ArshaDebuff`; it reads no row of this file by
name.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File              | Bytes | Records | Row bytes |
| ------ | ------------- | ----------------- | ----- | ------- | --------- |
| 1      | 805 and later | `arshadebuff.bss` | 56    | 3 Row   | 12        |

| Layout | File              | Known        | Unknown      |
| ------ | ----------------- | ------------ | ------------ |
| 1      | `arshadebuff.bss` | 32 B (57.1%) | 24 B (42.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `a7380205d0f2`  |
| 3482   | Layout 1             | `a7380205d0f2`  |
| 3474   | Layout 1             | `a7380205d0f2`  |
| 3473   | Layout 1             | `a7380205d0f2`  |
| 3464   | Layout 1             | `a7380205d0f2`  |
| 3458   | Layout 1             | `a7380205d0f2`  |
| 3454   | Layout 1             | `a7380205d0f2`  |
| 3444   | Layout 1             | `a7380205d0f2`  |
| 3435   | Layout 1             | `a7380205d0f2`  |
| 3426   | Layout 1             | `a7380205d0f2`  |
| 3418   | Layout 1             | `a7380205d0f2`  |
| 3412   | Layout 1             | `a7380205d0f2`  |
| 3402   | Layout 1             | `a7380205d0f2`  |
| 3396   | Layout 1             | `a7380205d0f2`  |
| 3387   | Layout 1             | `a7380205d0f2`  |
| 3381   | Layout 1             | `a7380205d0f2`  |
| 3373   | Layout 1             | `a7380205d0f2`  |
| 3364   | Layout 1             | `a7380205d0f2`  |
| 3356   | Layout 1             | `a7380205d0f2`  |
| 3349   | Layout 1             | `a7380205d0f2`  |
| 3342   | Layout 1             | `a7380205d0f2`  |
| 3335   | Layout 1             | `a7380205d0f2`  |
| 3326   | Layout 1             | `a7380205d0f2`  |
| 3321   | Layout 1             | `a7380205d0f2`  |
| 3314   | Layout 1             | `a7380205d0f2`  |
| 3303   | Layout 1             | `a7380205d0f2`  |
| 3302   | Layout 1             | `a7380205d0f2`  |
| 3293   | Layout 1             | `a7380205d0f2`  |
| 3283   | Layout 1             | `a7380205d0f2`  |
| 3275   | Layout 1             | `a7380205d0f2`  |
| 3267   | Layout 1             | `a7380205d0f2`  |
| 3258   | Layout 1             | `a7380205d0f2`  |
| 3251   | Layout 1             | `a7380205d0f2`  |
| 3242   | Layout 1             | `a7380205d0f2`  |
| 3235   | Layout 1             | `a7380205d0f2`  |
| 3229   | Layout 1             | `a7380205d0f2`  |
| 3212   | Layout 1             | `a7380205d0f2`  |
| 3203   | Layout 1             | `a7380205d0f2`  |
| 3193   | Layout 1             | `a7380205d0f2`  |
| 3186   | Layout 1             | `a7380205d0f2`  |
| 3177   | Layout 1             | `a7380205d0f2`  |
| 3169   | Layout 1             | `a7380205d0f2`  |
| 3158   | Layout 1             | `a7380205d0f2`  |
| 3151   | Layout 1             | `a7380205d0f2`  |
| 3144   | Layout 1             | `a7380205d0f2`  |
| 3133   | Layout 1             | `a7380205d0f2`  |
| 3125   | Layout 1             | `a7380205d0f2`  |
| 3118   | Layout 1             | `a7380205d0f2`  |
| 3111   | Layout 1             | `a7380205d0f2`  |
| 3103   | Layout 1             | `a7380205d0f2`  |
| 3095   | Layout 1             | `a7380205d0f2`  |
| 3086   | Layout 1             | `a7380205d0f2`  |
| 3072   | Layout 1             | `a7380205d0f2`  |
| 3062   | Layout 1             | `a7380205d0f2`  |
| 3052   | Layout 1             | `a7380205d0f2`  |
| 3045   | Layout 1             | `a7380205d0f2`  |
| 3037   | Layout 1             | `a7380205d0f2`  |
| 3030   | Layout 1             | `a7380205d0f2`  |
| 3021   | Layout 1             | `a7380205d0f2`  |
| 3012   | Layout 1             | `a7380205d0f2`  |
| 3002   | Layout 1             | `a7380205d0f2`  |
| 2995   | Layout 1             | `a7380205d0f2`  |
| 2987   | Layout 1             | `a7380205d0f2`  |
| 2978   | Layout 1             | `a7380205d0f2`  |
| 2970   | Layout 1             | `a7380205d0f2`  |
| 2959   | Layout 1             | `a7380205d0f2`  |
| 2951   | Layout 1             | `a7380205d0f2`  |
| 2942   | Layout 1             | `a7380205d0f2`  |
| 2935   | Layout 1             | `a7380205d0f2`  |
| 2932   | Layout 1             | `a7380205d0f2`  |
| 2923   | Layout 1             | `a7380205d0f2`  |
| 2919   | Layout 1             | `a7380205d0f2`  |
| 2907   | Layout 1             | `a7380205d0f2`  |
| 2900   | Layout 1             | `a7380205d0f2`  |
| 2891   | Layout 1             | `a7380205d0f2`  |
| 2882   | Layout 1             | `a7380205d0f2`  |
| 2872   | Layout 1             | `a7380205d0f2`  |
| 2863   | Layout 1             | `a7380205d0f2`  |
| 2855   | Layout 1             | `a7380205d0f2`  |
| 2849   | Layout 1             | `a7380205d0f2`  |
| 2844   | Layout 1             | `a7380205d0f2`  |
| 2834   | Layout 1             | `a7380205d0f2`  |
| 2825   | Layout 1             | `a7380205d0f2`  |
| 2819   | Layout 1             | `a7380205d0f2`  |
| 2811   | Layout 1             | `a7380205d0f2`  |
| 2803   | Layout 1             | `a7380205d0f2`  |
| 2794   | Layout 1             | `a7380205d0f2`  |
| 2783   | Layout 1             | `a7380205d0f2`  |
| 2774   | Layout 1             | `a7380205d0f2`  |
| 2765   | Layout 1             | `a7380205d0f2`  |
| 2756   | Layout 1             | `a7380205d0f2`  |
| 2750   | Layout 1             | `a7380205d0f2`  |
| 2743   | Layout 1             | `a7380205d0f2`  |
| 2736   | Layout 1             | `a7380205d0f2`  |
| 2726   | Layout 1             | `a7380205d0f2`  |
| 2717   | Layout 1             | `a7380205d0f2`  |
| 2709   | Layout 1             | `a7380205d0f2`  |
| 2703   | Layout 1             | `a7380205d0f2`  |
| 2695   | Layout 1             | `a7380205d0f2`  |
| 2684   | Layout 1             | `a7380205d0f2`  |
| 2672   | Layout 1             | `a7380205d0f2`  |
| 2665   | Layout 1             | `a7380205d0f2`  |
| 2657   | Layout 1             | `a7380205d0f2`  |
| 2649   | Layout 1             | `a7380205d0f2`  |
| 2644   | Layout 1             | `a7380205d0f2`  |
| 2637   | Layout 1             | `a7380205d0f2`  |
| 2629   | Layout 1             | `a7380205d0f2`  |
| 2619   | Layout 1             | `a7380205d0f2`  |
| 2612   | Layout 1             | `a7380205d0f2`  |
| 2606   | Layout 1             | `a7380205d0f2`  |
| 2602   | Layout 1             | `a7380205d0f2`  |
| 2601   | Layout 1             | `a7380205d0f2`  |
| 2592   | Layout 1             | `a7380205d0f2`  |
| 2583   | Layout 1             | `a7380205d0f2`  |
| 2575   | Layout 1             | `a7380205d0f2`  |
| 2567   | Layout 1             | `a7380205d0f2`  |
| 2560   | Layout 1             | `a7380205d0f2`  |
| 2553   | Layout 1             | `a7380205d0f2`  |
| 2545   | Layout 1             | `a7380205d0f2`  |
| 2538   | Layout 1             | `a7380205d0f2`  |
| 2529   | Layout 1             | `a7380205d0f2`  |
| 2519   | Layout 1             | `a7380205d0f2`  |
| 2513   | Layout 1             | `a7380205d0f2`  |
| 2510   | Layout 1             | `a7380205d0f2`  |
| 2507   | Layout 1             | `a7380205d0f2`  |
| 2503   | Layout 1             | `a7380205d0f2`  |
| 2498   | Layout 1             | `a7380205d0f2`  |
| 2492   | Layout 1             | `a7380205d0f2`  |
| 2487   | Layout 1             | `a7380205d0f2`  |
| 2480   | Layout 1             | `a7380205d0f2`  |
| 2474   | Layout 1             | `a7380205d0f2`  |
| 2468   | Layout 1             | `a7380205d0f2`  |
| 2460   | Layout 1             | `a7380205d0f2`  |
| 2453   | Layout 1             | `a7380205d0f2`  |
| 2444   | Layout 1             | `a7380205d0f2`  |
| 2438   | Layout 1             | `a7380205d0f2`  |
| 2434   | Layout 1             | `a7380205d0f2`  |
| 2429   | Layout 1             | `a7380205d0f2`  |
| 2421   | Layout 1             | `a7380205d0f2`  |
| 2414   | Layout 1             | `a7380205d0f2`  |
| 2407   | Layout 1             | `a7380205d0f2`  |
| 2401   | Layout 1             | `a7380205d0f2`  |
| 2397   | Layout 1             | `a7380205d0f2`  |
| 2393   | Layout 1             | `a7380205d0f2`  |
| 2384   | Layout 1             | `a7380205d0f2`  |
| 2378   | Layout 1             | `a7380205d0f2`  |
| 2372   | Layout 1             | `a7380205d0f2`  |
| 2358   | Layout 1             | `a7380205d0f2`  |
| 2352   | Layout 1             | `a7380205d0f2`  |
| 2347   | Layout 1             | `a7380205d0f2`  |
| 2343   | Layout 1             | `a7380205d0f2`  |
| 2335   | Layout 1             | `a7380205d0f2`  |
| 2327   | Layout 1             | `a7380205d0f2`  |
| 2324   | Layout 1             | `a7380205d0f2`  |
| 2319   | Layout 1             | `a7380205d0f2`  |
| 2313   | Layout 1             | `a7380205d0f2`  |
| 2308   | Layout 1             | `a7380205d0f2`  |
| 2302   | Layout 1             | `a7380205d0f2`  |
| 2295   | Layout 1             | `a7380205d0f2`  |
| 2290   | Layout 1             | `a7380205d0f2`  |
| 2284   | Layout 1             | `a7380205d0f2`  |
| 2276   | Layout 1             | `a7380205d0f2`  |
| 2269   | Layout 1             | `a7380205d0f2`  |
| 2259   | Layout 1             | `a7380205d0f2`  |
| 2250   | Layout 1             | `a7380205d0f2`  |
| 2243   | Layout 1             | `a7380205d0f2`  |
| 2235   | Layout 1             | `a7380205d0f2`  |
| 2229   | Layout 1             | `a7380205d0f2`  |
| 2224   | Layout 1             | `a7380205d0f2`  |
| 2218   | Layout 1             | `a7380205d0f2`  |
| 2215   | Layout 1             | `a7380205d0f2`  |
| 2207   | Layout 1             | `a7380205d0f2`  |
| 2203   | Layout 1             | `a7380205d0f2`  |
| 2196   | Layout 1             | `a7380205d0f2`  |
| 2192   | Layout 1             | `a7380205d0f2`  |
| 2189   | Layout 1             | `a7380205d0f2`  |
| 2183   | Layout 1             | `a7380205d0f2`  |
| 2179   | Layout 1             | `a7380205d0f2`  |
| 2171   | Layout 1             | `a7380205d0f2`  |
| 2163   | Layout 1             | `a7380205d0f2`  |
| 2156   | Layout 1             | `a7380205d0f2`  |
| 2151   | Layout 1             | `a7380205d0f2`  |
| 2147   | Layout 1             | `a7380205d0f2`  |
| 2142   | Layout 1             | `a7380205d0f2`  |
| 2138   | Layout 1             | `a7380205d0f2`  |
| 2134   | Layout 1             | `a7380205d0f2`  |
| 2130   | Layout 1             | `a7380205d0f2`  |
| 2122   | Layout 1             | `a7380205d0f2`  |
| 2107   | Layout 1             | `a7380205d0f2`  |
| 2098   | Layout 1             | `a7380205d0f2`  |
| 2089   | Layout 1             | `a7380205d0f2`  |
| 2081   | Layout 1             | `a7380205d0f2`  |
| 2073   | Layout 1             | `a7380205d0f2`  |
| 2067   | Layout 1             | `a7380205d0f2`  |
| 2063   | Layout 1             | `a7380205d0f2`  |
| 2059   | Layout 1             | `a7380205d0f2`  |
| 2052   | Layout 1             | `a7380205d0f2`  |
| 2044   | Layout 1             | `a7380205d0f2`  |
| 2039   | Layout 1             | `a7380205d0f2`  |
| 2032   | Layout 1             | `a7380205d0f2`  |
| 2025   | Layout 1             | `a7380205d0f2`  |
| 2011   | Layout 1             | `a7380205d0f2`  |
| 2005   | Layout 1             | `a7380205d0f2`  |
| 2000   | Layout 1             | `a7380205d0f2`  |
| 1996   | Layout 1             | `a7380205d0f2`  |
| 1991   | Layout 1             | `a7380205d0f2`  |
| 1985   | Layout 1             | `a7380205d0f2`  |
| 1980   | Layout 1             | `a7380205d0f2`  |
| 1969   | Layout 1             | `a7380205d0f2`  |
| 1964   | Layout 1             | `a7380205d0f2`  |
| 1958   | Layout 1             | `a7380205d0f2`  |
| 1950   | Layout 1             | `a7380205d0f2`  |
| 1945   | Layout 1             | `a7380205d0f2`  |
| 1937   | Layout 1             | `a7380205d0f2`  |
| 1933   | Layout 1             | `a7380205d0f2`  |
| 1927   | Layout 1             | `a7380205d0f2`  |
| 1921   | Layout 1             | `a7380205d0f2`  |
| 1914   | Layout 1             | `a7380205d0f2`  |
| 1908   | Layout 1             | `a7380205d0f2`  |
| 1897   | Layout 1             | `a7380205d0f2`  |
| 1892   | Layout 1             | `a7380205d0f2`  |
| 1886   | Layout 1             | `a7380205d0f2`  |
| 1881   | Layout 1             | `a7380205d0f2`  |
| 1871   | Layout 1             | `a7380205d0f2`  |
| 1866   | Layout 1             | `a7380205d0f2`  |
| 1862   | Layout 1             | `a7380205d0f2`  |
| 1854   | Layout 1             | `a7380205d0f2`  |
| 1846   | Layout 1             | `a7380205d0f2`  |
| 1838   | Layout 1             | `a7380205d0f2`  |
| 1832   | Layout 1             | `a7380205d0f2`  |
| 1826   | Layout 1             | `a7380205d0f2`  |
| 1822   | Layout 1             | `a7380205d0f2`  |
| 1818   | Layout 1             | `a7380205d0f2`  |
| 1804   | Layout 1             | `a7380205d0f2`  |
| 1794   | Layout 1             | `a7380205d0f2`  |
| 1790   | Layout 1             | `a7380205d0f2`  |
| 1784   | Layout 1             | `a7380205d0f2`  |
| 1774   | Layout 1             | `a7380205d0f2`  |
| 1771   | Layout 1             | `a7380205d0f2`  |
| 1762   | Layout 1             | `a7380205d0f2`  |
| 1759   | Layout 1             | `a7380205d0f2`  |
| 1754   | Layout 1             | `a7380205d0f2`  |
| 1749   | Layout 1             | `a7380205d0f2`  |
| 1743   | Layout 1             | `a7380205d0f2`  |
| 1737   | Layout 1             | `a7380205d0f2`  |
| 1731   | Layout 1             | `a7380205d0f2`  |
| 1725   | Layout 1             | `a7380205d0f2`  |
| 1717   | Layout 1             | `a7380205d0f2`  |
| 1710   | Layout 1             | `a7380205d0f2`  |
| 1704   | Layout 1             | `a7380205d0f2`  |
| 1698   | Layout 1             | `a7380205d0f2`  |
| 1690   | Layout 1             | `a7380205d0f2`  |
| 1685   | Layout 1             | `a7380205d0f2`  |
| 1680   | Layout 1             | `a7380205d0f2`  |
| 1674   | Layout 1             | `a7380205d0f2`  |
| 1668   | Layout 1             | `a7380205d0f2`  |
| 1659   | Layout 1             | `a7380205d0f2`  |
| 1649   | Layout 1             | `a7380205d0f2`  |
| 1642   | Layout 1             | `a7380205d0f2`  |
| 1636   | Layout 1             | `a7380205d0f2`  |
| 1628   | Layout 1             | `a7380205d0f2`  |
| 1622   | Layout 1             | `a7380205d0f2`  |
| 1614   | Layout 1             | `a7380205d0f2`  |
| 1608   | Layout 1             | `a7380205d0f2`  |
| 1602   | Layout 1             | `a7380205d0f2`  |
| 1598   | Layout 1             | `a7380205d0f2`  |
| 1594   | Layout 1             | `a7380205d0f2`  |
| 1590   | Layout 1             | `a7380205d0f2`  |
| 1587   | Layout 1             | `a7380205d0f2`  |
| 1584   | Layout 1             | `a7380205d0f2`  |
| 1579   | Layout 1             | `a7380205d0f2`  |
| 1572   | Layout 1             | `a7380205d0f2`  |
| 1565   | Layout 1             | `a7380205d0f2`  |
| 1559   | Layout 1             | `a7380205d0f2`  |
| 1554   | Layout 1             | `a7380205d0f2`  |
| 1547   | Layout 1             | `a7380205d0f2`  |
| 1537   | Layout 1             | `a7380205d0f2`  |
| 1529   | Layout 1             | `a7380205d0f2`  |
| 1524   | Layout 1             | `a7380205d0f2`  |
| 1519   | Layout 1             | `a7380205d0f2`  |
| 1509   | Layout 1             | `a7380205d0f2`  |
| 1506   | Layout 1             | `a7380205d0f2`  |
| 1504   | Layout 1             | `a7380205d0f2`  |
| 1500   | Layout 1             | `a7380205d0f2`  |
| 1493   | Layout 1             | `a7380205d0f2`  |
| 1489   | Layout 1             | `a7380205d0f2`  |
| 1485   | Layout 1             | `a7380205d0f2`  |
| 1481   | Layout 1             | `a7380205d0f2`  |
| 1474   | Layout 1             | `a7380205d0f2`  |
| 1466   | Layout 1             | `a7380205d0f2`  |
| 1462   | Layout 1             | `a7380205d0f2`  |
| 1459   | Layout 1             | `a7380205d0f2`  |
| 1453   | Layout 1             | `a7380205d0f2`  |
| 1450   | Layout 1             | `a7380205d0f2`  |
| 1445   | Layout 1             | `a7380205d0f2`  |
| 1439   | Layout 1             | `a7380205d0f2`  |
| 1433   | Layout 1             | `a7380205d0f2`  |
| 1430   | Layout 1             | `a7380205d0f2`  |
| 1426   | Layout 1             | `a7380205d0f2`  |
| 1421   | Layout 1             | `a7380205d0f2`  |
| 1417   | Layout 1             | `a7380205d0f2`  |
| 1416   | Layout 1             | `a7380205d0f2`  |
| 1409   | Layout 1             | `a7380205d0f2`  |
| 1405   | Layout 1             | `a7380205d0f2`  |
| 1401   | Layout 1             | `a7380205d0f2`  |
| 1396   | Layout 1             | `a7380205d0f2`  |
| 1391   | Layout 1             | `a7380205d0f2`  |
| 1390   | Layout 1             | `a7380205d0f2`  |
| 1386   | Layout 1             | `a7380205d0f2`  |
| 1381   | Layout 1             | `a7380205d0f2`  |
| 1379   | Layout 1             | `a7380205d0f2`  |
| 1372   | Layout 1             | `a7380205d0f2`  |
| 1366   | Layout 1             | `a7380205d0f2`  |
| 1364   | Layout 1             | `a7380205d0f2`  |
| 1363   | Layout 1             | `a7380205d0f2`  |
| 1360   | Layout 1             | `a7380205d0f2`  |
| 1358   | Layout 1             | `a7380205d0f2`  |
| 1355   | Layout 1             | `a7380205d0f2`  |
| 1351   | Layout 1             | `a7380205d0f2`  |
| 1348   | Layout 1             | `a7380205d0f2`  |
| 1346   | Layout 1             | `a7380205d0f2`  |
| 1341   | Layout 1             | `a7380205d0f2`  |
| 1340   | Layout 1             | `a7380205d0f2`  |
| 1338   | Layout 1             | `a7380205d0f2`  |
| 1335   | Layout 1             | `a7380205d0f2`  |
| 1333   | Layout 1             | `a7380205d0f2`  |
| 1329   | Layout 1             | `a7380205d0f2`  |
| 1327   | Layout 1             | `a7380205d0f2`  |
| 1324   | Layout 1             | `a7380205d0f2`  |
| 1321   | Layout 1             | `a7380205d0f2`  |
| 1319   | Layout 1             | `a7380205d0f2`  |
| 1318   | Layout 1             | `a7380205d0f2`  |
| 1316   | Layout 1             | `a7380205d0f2`  |
| 1313   | Layout 1             | `a7380205d0f2`  |
| 1311   | Layout 1             | `a7380205d0f2`  |
| 1309   | Layout 1             | `a7380205d0f2`  |
| 1304   | Layout 1             | `a7380205d0f2`  |
| 1292   | Layout 1             | `a7380205d0f2`  |
| 1286   | Layout 1             | `a7380205d0f2`  |
| 1280   | Layout 1             | `a7380205d0f2`  |
| 1276   | Layout 1             | `a7380205d0f2`  |
| 1267   | Layout 1             | `a7380205d0f2`  |
| 1261   | Layout 1             | `a7380205d0f2`  |
| 1256   | Layout 1             | `a7380205d0f2`  |
| 1250   | Layout 1             | `a7380205d0f2`  |
| 1246   | Layout 1             | `a7380205d0f2`  |
| 1239   | Layout 1             | `a7380205d0f2`  |
| 1230   | Layout 1             | `a7380205d0f2`  |
| 1226   | Layout 1             | `a7380205d0f2`  |
| 1220   | Layout 1             | `a7380205d0f2`  |
| 1217   | Layout 1             | `a7380205d0f2`  |
| 1211   | Layout 1             | `a7380205d0f2`  |
| 1210   | Layout 1             | `a7380205d0f2`  |
| 1208   | Layout 1             | `a7380205d0f2`  |
| 1203   | Layout 1             | `a7380205d0f2`  |
| 1197   | Layout 1             | `a7380205d0f2`  |
| 1194   | Layout 1             | `a7380205d0f2`  |
| 1192   | Layout 1             | `a7380205d0f2`  |
| 1187   | Layout 1             | `a7380205d0f2`  |
| 1183   | Layout 1             | `a7380205d0f2`  |
| 1177   | Layout 1             | `a7380205d0f2`  |
| 1173   | Layout 1             | `a7380205d0f2`  |
| 1167   | Layout 1             | `a7380205d0f2`  |
| 1164   | Layout 1             | `a7380205d0f2`  |
| 1156   | Layout 1             | `a7380205d0f2`  |
| 1149   | Layout 1             | `a7380205d0f2`  |
| 1144   | Layout 1             | `a7380205d0f2`  |
| 1137   | Layout 1             | `a7380205d0f2`  |
| 1132   | Layout 1             | `a7380205d0f2`  |
| 1127   | Layout 1             | `a7380205d0f2`  |
| 1122   | Layout 1             | `a7380205d0f2`  |
| 1118   | Layout 1             | `a7380205d0f2`  |
| 1114   | Layout 1             | `a7380205d0f2`  |
| 1109   | Layout 1             | `a7380205d0f2`  |
| 1102   | Layout 1             | `a7380205d0f2`  |
| 1096   | Layout 1             | `a7380205d0f2`  |
| 1088   | Layout 1             | `a7380205d0f2`  |
| 1081   | Layout 1             | `a7380205d0f2`  |
| 1076   | Layout 1             | `a7380205d0f2`  |
| 1069   | Layout 1             | `a7380205d0f2`  |
| 1064   | Layout 1             | `a7380205d0f2`  |
| 1058   | Layout 1             | `a7380205d0f2`  |
| 1051   | Layout 1             | `a7380205d0f2`  |
| 1044   | Layout 1             | `a7380205d0f2`  |
| 1036   | Layout 1             | `a7380205d0f2`  |
| 1026   | Layout 1             | `a7380205d0f2`  |
| 1016   | Layout 1             | `a7380205d0f2`  |
| 1009   | Layout 1             | `a7380205d0f2`  |
| 1005   | Layout 1             | `a7380205d0f2`  |
| 1000   | Layout 1             | `a7380205d0f2`  |
| 998    | Layout 1             | `a7380205d0f2`  |
| 990    | Layout 1             | `a7380205d0f2`  |
| 979    | Layout 1             | `a7380205d0f2`  |
| 972    | Layout 1             | `a7380205d0f2`  |
| 963    | Layout 1             | `a7380205d0f2`  |
| 955    | Layout 1             | `a7380205d0f2`  |
| 946    | Layout 1             | `a7380205d0f2`  |
| 938    | Layout 1             | `a7380205d0f2`  |
| 927    | Layout 1             | `a7380205d0f2`  |
| 911    | Layout 1             | `a7380205d0f2`  |
| 904    | Layout 1             | `a7380205d0f2`  |
| 899    | Layout 1             | `a7380205d0f2`  |
| 894    | Layout 1             | `a7380205d0f2`  |
| 885    | Layout 1             | `a7380205d0f2`  |
| 879    | Layout 1             | `a7380205d0f2`  |
| 872    | Layout 1             | `a7380205d0f2`  |
| 864    | Layout 1             | `a7380205d0f2`  |
| 855    | Layout 1             | `a7380205d0f2`  |
| 853    | Layout 1             | `a7380205d0f2`  |
| 845    | Layout 1             | `a7380205d0f2`  |
| 837    | Layout 1             | `a7380205d0f2`  |
| 829    | Layout 1             | `a7380205d0f2`  |
| 822    | Layout 1             | `a7380205d0f2`  |
| 814    | Layout 1             | `a7380205d0f2`  |
| 805    | Layout 1             | `a7380205d0f2`  |
| 794    | No documented layout | `a7380205d0f2`  |
| 787    | No documented layout | `a7380205d0f2`  |
| 780    | No documented layout | `a7380205d0f2`  |
| 771    | No documented layout | `a7380205d0f2`  |
| 760    | No documented layout | `a7380205d0f2`  |
| 748    | No documented layout | `a7380205d0f2`  |
| 741    | No documented layout | `a7380205d0f2`  |
| 736    | No documented layout | `a7380205d0f2`  |
| 731    | No documented layout | `a7380205d0f2`  |
| 723    | No documented layout | `a7380205d0f2`  |
| 711    | No documented layout | `a7380205d0f2`  |
| 707    | No documented layout | `a7380205d0f2`  |
| 697    | No documented layout | `a7380205d0f2`  |
| 689    | No documented layout | `a7380205d0f2`  |
| 683    | No documented layout | `a7380205d0f2`  |
| 678    | No documented layout | `a7380205d0f2`  |
| 670    | No documented layout | `a7380205d0f2`  |
| 661    | No documented layout | `a7380205d0f2`  |
| 656    | No documented layout | `a7380205d0f2`  |
| 652    | No documented layout | `a7380205d0f2`  |
| 643    | No documented layout | `a7380205d0f2`  |
| 637    | No documented layout | `a7380205d0f2`  |
| 630    | No documented layout | `a7380205d0f2`  |
| 627    | No documented layout | `a7380205d0f2`  |
| 621    | No documented layout | `a7380205d0f2`  |
| 617    | No documented layout | `a7380205d0f2`  |
| 615    | No documented layout | `a7380205d0f2`  |
| 606    | No documented layout | `a7380205d0f2`  |
| 599    | No documented layout | `a7380205d0f2`  |
| 592    | No file              | `a7380205d0f2`  |
| 586    | No file              | `a7380205d0f2`  |
| 577    | No file              | `a7380205d0f2`  |
| 569    | No file              | `a7380205d0f2`  |
| 561    | No file              | `a7380205d0f2`  |
| 554    | No file              | `a7380205d0f2`  |
| 542    | No file              | `a7380205d0f2`  |
| 532    | No file              | `a7380205d0f2`  |
| 531    | No file              | `a7380205d0f2`  |
| 526    | No file              | `a7380205d0f2`  |
| 521    | No file              | `a7380205d0f2`  |
| 517    | No file              | `a7380205d0f2`  |
| 510    | No file              | `a7380205d0f2`  |
| 508    | No file              | `a7380205d0f2`  |
| 504    | No file              | `a7380205d0f2`  |
| 497    | No file              | `a7380205d0f2`  |
| 491    | No file              | `a7380205d0f2`  |
| 485    | No file              | `a7380205d0f2`  |
| 478    | No file              | `a7380205d0f2`  |
| 472    | No file              | `a7380205d0f2`  |
| 466    | No file              | `a7380205d0f2`  |
| 457    | No file              | `a7380205d0f2`  |
| 452    | No file              | `a7380205d0f2`  |
| 449    | No file              | `a7380205d0f2`  |
| 435    | No file              | `a7380205d0f2`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone.

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

### Row (12 bytes)

| Offset  | Type | Field        | Notes                                                               |
| ------- | ---- | ------------ | ------------------------------------------------------------------- |
| `+0x00` | u32  | debuff_timer | `0`, `330000`, `660000` on every client checked; see Field Names    |
| `+0x04` | u32  | unknown_04   | `0` on every row; see Open Questions                                |
| `+0x08` | u32  | unknown_08   | `0` on every row; see Open Questions                                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `ArshaDebuff_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `debuffTimer`, `decreaseMaxHp` and
`decreaseRecoveryHp` and 3 rows, `330000` and `660000` after a first row of
`0`. `debuff_timer` matches 3 of 3 rows of the client 1784 file, and the
file is the same on client 3474. The sheet's other two columns are `0` on
every row, as are `unknown_04` and `unknown_08`, so the values do not tell
which column is which.

## Notes

- The file is 56 bytes and the same on clients 1784, 2107, 2519, 3002, 3251
  and 3474.
- The server reads the sheet in `ArshaStaticStatus` next to the personal
  match HP debuff (`ArshaPersonalMatchHPDebuff`: `WinCount`,
  `DebuffHPRate`, `RemainTimeMultiplier`), which has no client file.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`.

## Open Questions

### Max HP and Recovery Columns

Which of `unknown_04` and `unknown_08` is `decreaseMaxHp` and which
`decreaseRecoveryHp`. Both are `0` on every row of every client checked,
and the sheet order and the order of the server's column strings disagree.
A file with a non-zero value in one of them would tell.

### Timer Unit

The unit of `debuff_timer`. As milliseconds, `330000` and `660000` are
5 min 30 s and 11 min of a match; no Lua shows the value.
