# `cashproduct_instant.bss` Format

## Purpose

The cost to finish a timed task at once, by the time it has left: one
group per `CppEnums.InstantCashType` (`0` ChangeHouseUseType, `1`
CompleteServantMating, `2` CompleteNpcWorking, `3` CompleteNpcWorkerUpgrade),
each a list of remaining minutes and the cost. The worker and house Lua
(`new_worldmap_working_progress.luac`, `panel_new_housecontrol.luac`)
asks for the cost with
`ToClient_GetUsingPearlByRemainingPearl(CppEnums.InstantCashType.eInstant_CompleteNpcWorking, remainingTime)`
and shows it as Silver (`LUA_WORLDMAP_WORKDING_PROGRESS_IMMEDIATELY_SILVER`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------------ | --------- |
| 1      | 1250 and later | 3483    | `cashproduct_instant.bss` | 3,668 | 226 Entry, 4 Group | 16        |

| Layout | File                      | Known           | Unknown    |
| ------ | ------------------------- | --------------- | ---------- |
| 1      | `cashproduct_instant.bss` | 3,664 B (99.9%) | 4 B (0.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `32b52d2caf84`  |
| 3482   | Layout 1 | `32b52d2caf84`  |
| 3474   | Layout 1 | `32b52d2caf84`  |
| 3473   | Layout 1 | `32b52d2caf84`  |
| 3464   | Layout 1 | `32b52d2caf84`  |
| 3458   | Layout 1 | `32b52d2caf84`  |
| 3454   | Layout 1 | `32b52d2caf84`  |
| 3444   | Layout 1 | `32b52d2caf84`  |
| 3435   | Layout 1 | `32b52d2caf84`  |
| 3426   | Layout 1 | `32b52d2caf84`  |
| 3418   | Layout 1 | `32b52d2caf84`  |
| 3412   | Layout 1 | `32b52d2caf84`  |
| 3402   | Layout 1 | `32b52d2caf84`  |
| 3396   | Layout 1 | `32b52d2caf84`  |
| 3387   | Layout 1 | `32b52d2caf84`  |
| 3381   | Layout 1 | `32b52d2caf84`  |
| 3373   | Layout 1 | `32b52d2caf84`  |
| 3364   | Layout 1 | `32b52d2caf84`  |
| 3356   | Layout 1 | `32b52d2caf84`  |
| 3349   | Layout 1 | `32b52d2caf84`  |
| 3342   | Layout 1 | `32b52d2caf84`  |
| 3335   | Layout 1 | `32b52d2caf84`  |
| 3326   | Layout 1 | `32b52d2caf84`  |
| 3321   | Layout 1 | `32b52d2caf84`  |
| 3314   | Layout 1 | `32b52d2caf84`  |
| 3303   | Layout 1 | `32b52d2caf84`  |
| 3302   | Layout 1 | `32b52d2caf84`  |
| 3293   | Layout 1 | `32b52d2caf84`  |
| 3283   | Layout 1 | `32b52d2caf84`  |
| 3275   | Layout 1 | `32b52d2caf84`  |
| 3267   | Layout 1 | `32b52d2caf84`  |
| 3258   | Layout 1 | `32b52d2caf84`  |
| 3251   | Layout 1 | `32b52d2caf84`  |
| 3242   | Layout 1 | `32b52d2caf84`  |
| 3235   | Layout 1 | `32b52d2caf84`  |
| 3229   | Layout 1 | `32b52d2caf84`  |
| 3212   | Layout 1 | `32b52d2caf84`  |
| 3203   | Layout 1 | `32b52d2caf84`  |
| 3193   | Layout 1 | `32b52d2caf84`  |
| 3186   | Layout 1 | `32b52d2caf84`  |
| 3177   | Layout 1 | `32b52d2caf84`  |
| 3169   | Layout 1 | `32b52d2caf84`  |
| 3158   | Layout 1 | `32b52d2caf84`  |
| 3151   | Layout 1 | `32b52d2caf84`  |
| 3144   | Layout 1 | `32b52d2caf84`  |
| 3133   | Layout 1 | `32b52d2caf84`  |
| 3125   | Layout 1 | `32b52d2caf84`  |
| 3118   | Layout 1 | `32b52d2caf84`  |
| 3111   | Layout 1 | `32b52d2caf84`  |
| 3103   | Layout 1 | `32b52d2caf84`  |
| 3095   | Layout 1 | `32b52d2caf84`  |
| 3086   | Layout 1 | `32b52d2caf84`  |
| 3072   | Layout 1 | `32b52d2caf84`  |
| 3062   | Layout 1 | `32b52d2caf84`  |
| 3052   | Layout 1 | `32b52d2caf84`  |
| 3045   | Layout 1 | `32b52d2caf84`  |
| 3037   | Layout 1 | `32b52d2caf84`  |
| 3030   | Layout 1 | `32b52d2caf84`  |
| 3021   | Layout 1 | `32b52d2caf84`  |
| 3012   | Layout 1 | `32b52d2caf84`  |
| 3002   | Layout 1 | `32b52d2caf84`  |
| 2995   | Layout 1 | `32b52d2caf84`  |
| 2987   | Layout 1 | `32b52d2caf84`  |
| 2978   | Layout 1 | `32b52d2caf84`  |
| 2970   | Layout 1 | `32b52d2caf84`  |
| 2959   | Layout 1 | `32b52d2caf84`  |
| 2951   | Layout 1 | `32b52d2caf84`  |
| 2942   | Layout 1 | `32b52d2caf84`  |
| 2935   | Layout 1 | `32b52d2caf84`  |
| 2932   | Layout 1 | `32b52d2caf84`  |
| 2923   | Layout 1 | `32b52d2caf84`  |
| 2919   | Layout 1 | `32b52d2caf84`  |
| 2907   | Layout 1 | `32b52d2caf84`  |
| 2900   | Layout 1 | `32b52d2caf84`  |
| 2891   | Layout 1 | `32b52d2caf84`  |
| 2882   | Layout 1 | `32b52d2caf84`  |
| 2872   | Layout 1 | `32b52d2caf84`  |
| 2863   | Layout 1 | `32b52d2caf84`  |
| 2855   | Layout 1 | `32b52d2caf84`  |
| 2849   | Layout 1 | `32b52d2caf84`  |
| 2844   | Layout 1 | `32b52d2caf84`  |
| 2834   | Layout 1 | `32b52d2caf84`  |
| 2825   | Layout 1 | `32b52d2caf84`  |
| 2819   | Layout 1 | `32b52d2caf84`  |
| 2811   | Layout 1 | `32b52d2caf84`  |
| 2803   | Layout 1 | `32b52d2caf84`  |
| 2794   | Layout 1 | `32b52d2caf84`  |
| 2783   | Layout 1 | `32b52d2caf84`  |
| 2774   | Layout 1 | `32b52d2caf84`  |
| 2765   | Layout 1 | `32b52d2caf84`  |
| 2756   | Layout 1 | `32b52d2caf84`  |
| 2750   | Layout 1 | `32b52d2caf84`  |
| 2743   | Layout 1 | `32b52d2caf84`  |
| 2736   | Layout 1 | `32b52d2caf84`  |
| 2726   | Layout 1 | `32b52d2caf84`  |
| 2717   | Layout 1 | `32b52d2caf84`  |
| 2709   | Layout 1 | `32b52d2caf84`  |
| 2703   | Layout 1 | `32b52d2caf84`  |
| 2695   | Layout 1 | `32b52d2caf84`  |
| 2684   | Layout 1 | `32b52d2caf84`  |
| 2672   | Layout 1 | `32b52d2caf84`  |
| 2665   | Layout 1 | `32b52d2caf84`  |
| 2657   | Layout 1 | `32b52d2caf84`  |
| 2649   | Layout 1 | `32b52d2caf84`  |
| 2644   | Layout 1 | `32b52d2caf84`  |
| 2637   | Layout 1 | `32b52d2caf84`  |
| 2629   | Layout 1 | `32b52d2caf84`  |
| 2619   | Layout 1 | `32b52d2caf84`  |
| 2612   | Layout 1 | `32b52d2caf84`  |
| 2606   | Layout 1 | `32b52d2caf84`  |
| 2602   | Layout 1 | `32b52d2caf84`  |
| 2601   | Layout 1 | `32b52d2caf84`  |
| 2592   | Layout 1 | `32b52d2caf84`  |
| 2583   | Layout 1 | `32b52d2caf84`  |
| 2575   | Layout 1 | `32b52d2caf84`  |
| 2567   | Layout 1 | `32b52d2caf84`  |
| 2560   | Layout 1 | `32b52d2caf84`  |
| 2553   | Layout 1 | `32b52d2caf84`  |
| 2545   | Layout 1 | `32b52d2caf84`  |
| 2538   | Layout 1 | `32b52d2caf84`  |
| 2529   | Layout 1 | `32b52d2caf84`  |
| 2519   | Layout 1 | `32b52d2caf84`  |
| 2513   | Layout 1 | `32b52d2caf84`  |
| 2510   | Layout 1 | `32b52d2caf84`  |
| 2507   | Layout 1 | `32b52d2caf84`  |
| 2503   | Layout 1 | `32b52d2caf84`  |
| 2498   | Layout 1 | `32b52d2caf84`  |
| 2492   | Layout 1 | `32b52d2caf84`  |
| 2487   | Layout 1 | `32b52d2caf84`  |
| 2480   | Layout 1 | `32b52d2caf84`  |
| 2474   | Layout 1 | `32b52d2caf84`  |
| 2468   | Layout 1 | `32b52d2caf84`  |
| 2460   | Layout 1 | `32b52d2caf84`  |
| 2453   | Layout 1 | `32b52d2caf84`  |
| 2444   | Layout 1 | `32b52d2caf84`  |
| 2438   | Layout 1 | `32b52d2caf84`  |
| 2434   | Layout 1 | `32b52d2caf84`  |
| 2429   | Layout 1 | `32b52d2caf84`  |
| 2421   | Layout 1 | `32b52d2caf84`  |
| 2414   | Layout 1 | `32b52d2caf84`  |
| 2407   | Layout 1 | `32b52d2caf84`  |
| 2401   | Layout 1 | `32b52d2caf84`  |
| 2397   | Layout 1 | `32b52d2caf84`  |
| 2393   | Layout 1 | `32b52d2caf84`  |
| 2384   | Layout 1 | `32b52d2caf84`  |
| 2378   | Layout 1 | `32b52d2caf84`  |
| 2372   | Layout 1 | `32b52d2caf84`  |
| 2358   | Layout 1 | `32b52d2caf84`  |
| 2352   | Layout 1 | `32b52d2caf84`  |
| 2347   | Layout 1 | `32b52d2caf84`  |
| 2343   | Layout 1 | `32b52d2caf84`  |
| 2335   | Layout 1 | `32b52d2caf84`  |
| 2327   | Layout 1 | `32b52d2caf84`  |
| 2324   | Layout 1 | `32b52d2caf84`  |
| 2319   | Layout 1 | `32b52d2caf84`  |
| 2313   | Layout 1 | `32b52d2caf84`  |
| 2308   | Layout 1 | `32b52d2caf84`  |
| 2302   | Layout 1 | `32b52d2caf84`  |
| 2295   | Layout 1 | `32b52d2caf84`  |
| 2290   | Layout 1 | `32b52d2caf84`  |
| 2284   | Layout 1 | `32b52d2caf84`  |
| 2276   | Layout 1 | `32b52d2caf84`  |
| 2269   | Layout 1 | `32b52d2caf84`  |
| 2259   | Layout 1 | `32b52d2caf84`  |
| 2250   | Layout 1 | `32b52d2caf84`  |
| 2243   | Layout 1 | `32b52d2caf84`  |
| 2235   | Layout 1 | `32b52d2caf84`  |
| 2229   | Layout 1 | `32b52d2caf84`  |
| 2224   | Layout 1 | `32b52d2caf84`  |
| 2218   | Layout 1 | `32b52d2caf84`  |
| 2215   | Layout 1 | `32b52d2caf84`  |
| 2207   | Layout 1 | `32b52d2caf84`  |
| 2203   | Layout 1 | `32b52d2caf84`  |
| 2196   | Layout 1 | `32b52d2caf84`  |
| 2192   | Layout 1 | `32b52d2caf84`  |
| 2189   | Layout 1 | `32b52d2caf84`  |
| 2183   | Layout 1 | `32b52d2caf84`  |
| 2179   | Layout 1 | `32b52d2caf84`  |
| 2171   | Layout 1 | `32b52d2caf84`  |
| 2163   | Layout 1 | `32b52d2caf84`  |
| 2156   | Layout 1 | `32b52d2caf84`  |
| 2151   | Layout 1 | `32b52d2caf84`  |
| 2147   | Layout 1 | `32b52d2caf84`  |
| 2142   | Layout 1 | `32b52d2caf84`  |
| 2138   | Layout 1 | `32b52d2caf84`  |
| 2134   | Layout 1 | `32b52d2caf84`  |
| 2130   | Layout 1 | `32b52d2caf84`  |
| 2122   | Layout 1 | `32b52d2caf84`  |
| 2107   | Layout 1 | `32b52d2caf84`  |
| 2098   | Layout 1 | `32b52d2caf84`  |
| 2089   | Layout 1 | `32b52d2caf84`  |
| 2081   | Layout 1 | `32b52d2caf84`  |
| 2073   | Layout 1 | `32b52d2caf84`  |
| 2067   | Layout 1 | `32b52d2caf84`  |
| 2063   | Layout 1 | `32b52d2caf84`  |
| 2059   | Layout 1 | `32b52d2caf84`  |
| 2052   | Layout 1 | `32b52d2caf84`  |
| 2044   | Layout 1 | `32b52d2caf84`  |
| 2039   | Layout 1 | `32b52d2caf84`  |
| 2032   | Layout 1 | `32b52d2caf84`  |
| 2025   | Layout 1 | `32b52d2caf84`  |
| 2011   | Layout 1 | `32b52d2caf84`  |
| 2005   | Layout 1 | `32b52d2caf84`  |
| 2000   | Layout 1 | `32b52d2caf84`  |
| 1996   | Layout 1 | `32b52d2caf84`  |
| 1991   | Layout 1 | `32b52d2caf84`  |
| 1985   | Layout 1 | `32b52d2caf84`  |
| 1980   | Layout 1 | `32b52d2caf84`  |
| 1969   | Layout 1 | `32b52d2caf84`  |
| 1964   | Layout 1 | `32b52d2caf84`  |
| 1958   | Layout 1 | `32b52d2caf84`  |
| 1950   | Layout 1 | `32b52d2caf84`  |
| 1945   | Layout 1 | `32b52d2caf84`  |
| 1937   | Layout 1 | `32b52d2caf84`  |
| 1933   | Layout 1 | `32b52d2caf84`  |
| 1927   | Layout 1 | `32b52d2caf84`  |
| 1921   | Layout 1 | `32b52d2caf84`  |
| 1914   | Layout 1 | `32b52d2caf84`  |
| 1908   | Layout 1 | `32b52d2caf84`  |
| 1897   | Layout 1 | `32b52d2caf84`  |
| 1892   | Layout 1 | `32b52d2caf84`  |
| 1886   | Layout 1 | `32b52d2caf84`  |
| 1881   | Layout 1 | `32b52d2caf84`  |
| 1871   | Layout 1 | `32b52d2caf84`  |
| 1866   | Layout 1 | `32b52d2caf84`  |
| 1862   | Layout 1 | `32b52d2caf84`  |
| 1854   | Layout 1 | `32b52d2caf84`  |
| 1846   | Layout 1 | `32b52d2caf84`  |
| 1838   | Layout 1 | `32b52d2caf84`  |
| 1832   | Layout 1 | `32b52d2caf84`  |
| 1826   | Layout 1 | `32b52d2caf84`  |
| 1822   | Layout 1 | `32b52d2caf84`  |
| 1818   | Layout 1 | `32b52d2caf84`  |
| 1804   | Layout 1 | `32b52d2caf84`  |
| 1794   | Layout 1 | `32b52d2caf84`  |
| 1790   | Layout 1 | `32b52d2caf84`  |
| 1784   | Layout 1 | `32b52d2caf84`  |
| 1774   | Layout 1 | `32b52d2caf84`  |
| 1771   | Layout 1 | `32b52d2caf84`  |
| 1762   | Layout 1 | `32b52d2caf84`  |
| 1759   | Layout 1 | `32b52d2caf84`  |
| 1754   | Layout 1 | `32b52d2caf84`  |
| 1749   | Layout 1 | `32b52d2caf84`  |
| 1743   | Layout 1 | `32b52d2caf84`  |
| 1737   | Layout 1 | `32b52d2caf84`  |
| 1731   | Layout 1 | `32b52d2caf84`  |
| 1725   | Layout 1 | `32b52d2caf84`  |
| 1717   | Layout 1 | `32b52d2caf84`  |
| 1710   | Layout 1 | `32b52d2caf84`  |
| 1704   | Layout 1 | `32b52d2caf84`  |
| 1698   | Layout 1 | `32b52d2caf84`  |
| 1690   | Layout 1 | `32b52d2caf84`  |
| 1685   | Layout 1 | `32b52d2caf84`  |
| 1680   | Layout 1 | `32b52d2caf84`  |
| 1674   | Layout 1 | `32b52d2caf84`  |
| 1668   | Layout 1 | `32b52d2caf84`  |
| 1659   | Layout 1 | `32b52d2caf84`  |
| 1649   | Layout 1 | `32b52d2caf84`  |
| 1642   | Layout 1 | `32b52d2caf84`  |
| 1636   | Layout 1 | `32b52d2caf84`  |
| 1628   | Layout 1 | `32b52d2caf84`  |
| 1622   | Layout 1 | `32b52d2caf84`  |
| 1614   | Layout 1 | `32b52d2caf84`  |
| 1608   | Layout 1 | `32b52d2caf84`  |
| 1602   | Layout 1 | `32b52d2caf84`  |
| 1598   | Layout 1 | `32b52d2caf84`  |
| 1594   | Layout 1 | `32b52d2caf84`  |
| 1590   | Layout 1 | `32b52d2caf84`  |
| 1587   | Layout 1 | `32b52d2caf84`  |
| 1584   | Layout 1 | `32b52d2caf84`  |
| 1579   | Layout 1 | `32b52d2caf84`  |
| 1572   | Layout 1 | `32b52d2caf84`  |
| 1565   | Layout 1 | `32b52d2caf84`  |
| 1559   | Layout 1 | `32b52d2caf84`  |
| 1554   | Layout 1 | `32b52d2caf84`  |
| 1547   | Layout 1 | `32b52d2caf84`  |
| 1537   | Layout 1 | `32b52d2caf84`  |
| 1529   | Layout 1 | `32b52d2caf84`  |
| 1524   | Layout 1 | `32b52d2caf84`  |
| 1519   | Layout 1 | `32b52d2caf84`  |
| 1509   | Layout 1 | `32b52d2caf84`  |
| 1506   | Layout 1 | `32b52d2caf84`  |
| 1504   | Layout 1 | `32b52d2caf84`  |
| 1500   | Layout 1 | `32b52d2caf84`  |
| 1493   | Layout 1 | `32b52d2caf84`  |
| 1489   | Layout 1 | `32b52d2caf84`  |
| 1485   | Layout 1 | `32b52d2caf84`  |
| 1481   | Layout 1 | `32b52d2caf84`  |
| 1474   | Layout 1 | `32b52d2caf84`  |
| 1466   | Layout 1 | `32b52d2caf84`  |
| 1462   | Layout 1 | `32b52d2caf84`  |
| 1459   | Layout 1 | `32b52d2caf84`  |
| 1453   | Layout 1 | `32b52d2caf84`  |
| 1450   | Layout 1 | `32b52d2caf84`  |
| 1445   | Layout 1 | `32b52d2caf84`  |
| 1439   | Layout 1 | `32b52d2caf84`  |
| 1433   | Layout 1 | `32b52d2caf84`  |
| 1430   | Layout 1 | `32b52d2caf84`  |
| 1426   | Layout 1 | `32b52d2caf84`  |
| 1421   | Layout 1 | `32b52d2caf84`  |
| 1417   | Layout 1 | `32b52d2caf84`  |
| 1416   | Layout 1 | `32b52d2caf84`  |
| 1409   | Layout 1 | `32b52d2caf84`  |
| 1405   | Layout 1 | `32b52d2caf84`  |
| 1401   | Layout 1 | `32b52d2caf84`  |
| 1396   | Layout 1 | `32b52d2caf84`  |
| 1391   | Layout 1 | `32b52d2caf84`  |
| 1390   | Layout 1 | `32b52d2caf84`  |
| 1386   | Layout 1 | `32b52d2caf84`  |
| 1381   | Layout 1 | `32b52d2caf84`  |
| 1379   | Layout 1 | `32b52d2caf84`  |
| 1372   | Layout 1 | `32b52d2caf84`  |
| 1366   | Layout 1 | `32b52d2caf84`  |
| 1364   | Layout 1 | `32b52d2caf84`  |
| 1363   | Layout 1 | `32b52d2caf84`  |
| 1360   | Layout 1 | `32b52d2caf84`  |
| 1358   | Layout 1 | `32b52d2caf84`  |
| 1355   | Layout 1 | `32b52d2caf84`  |
| 1351   | Layout 1 | `32b52d2caf84`  |
| 1348   | Layout 1 | `32b52d2caf84`  |
| 1346   | Layout 1 | `32b52d2caf84`  |
| 1341   | Layout 1 | `32b52d2caf84`  |
| 1340   | Layout 1 | `32b52d2caf84`  |
| 1338   | Layout 1 | `32b52d2caf84`  |
| 1335   | Layout 1 | `32b52d2caf84`  |
| 1333   | Layout 1 | `32b52d2caf84`  |
| 1329   | Layout 1 | `32b52d2caf84`  |
| 1327   | Layout 1 | `32b52d2caf84`  |
| 1324   | Layout 1 | `32b52d2caf84`  |
| 1321   | Layout 1 | `32b52d2caf84`  |
| 1319   | Layout 1 | `32b52d2caf84`  |
| 1318   | Layout 1 | `32b52d2caf84`  |
| 1316   | Layout 1 | `32b52d2caf84`  |
| 1313   | Layout 1 | `32b52d2caf84`  |
| 1311   | Layout 1 | `32b52d2caf84`  |
| 1309   | Layout 1 | `32b52d2caf84`  |
| 1304   | Layout 1 | `32b52d2caf84`  |
| 1292   | Layout 1 | `32b52d2caf84`  |
| 1286   | Layout 1 | `32b52d2caf84`  |
| 1280   | Layout 1 | `32b52d2caf84`  |
| 1276   | Layout 1 | `32b52d2caf84`  |
| 1267   | Layout 1 | `32b52d2caf84`  |
| 1261   | Layout 1 | `32b52d2caf84`  |
| 1256   | Layout 1 | `32b52d2caf84`  |
| 1250   | Layout 1 | `32b52d2caf84`  |
| 1246   | No file  | `32b52d2caf84`  |
| 1239   | No file  | `32b52d2caf84`  |
| 1230   | No file  | `32b52d2caf84`  |
| 1226   | No file  | `32b52d2caf84`  |
| 1220   | No file  | `32b52d2caf84`  |
| 1217   | No file  | `32b52d2caf84`  |
| 1211   | No file  | `32b52d2caf84`  |
| 1210   | No file  | `32b52d2caf84`  |
| 1208   | No file  | `32b52d2caf84`  |
| 1203   | No file  | `32b52d2caf84`  |
| 1197   | No file  | `32b52d2caf84`  |
| 1194   | No file  | `32b52d2caf84`  |
| 1192   | No file  | `32b52d2caf84`  |
| 1187   | No file  | `32b52d2caf84`  |
| 1183   | No file  | `32b52d2caf84`  |
| 1177   | No file  | `32b52d2caf84`  |
| 1173   | No file  | `32b52d2caf84`  |
| 1167   | No file  | `32b52d2caf84`  |
| 1164   | No file  | `32b52d2caf84`  |
| 1156   | No file  | `32b52d2caf84`  |
| 1149   | No file  | `32b52d2caf84`  |
| 1144   | No file  | `32b52d2caf84`  |
| 1137   | No file  | `32b52d2caf84`  |
| 1132   | No file  | `32b52d2caf84`  |
| 1127   | No file  | `32b52d2caf84`  |
| 1122   | No file  | `32b52d2caf84`  |
| 1118   | No file  | `32b52d2caf84`  |
| 1114   | No file  | `32b52d2caf84`  |
| 1109   | No file  | `32b52d2caf84`  |
| 1102   | No file  | `32b52d2caf84`  |
| 1096   | No file  | `32b52d2caf84`  |
| 1088   | No file  | `32b52d2caf84`  |
| 1081   | No file  | `32b52d2caf84`  |
| 1076   | No file  | `32b52d2caf84`  |
| 1069   | No file  | `32b52d2caf84`  |
| 1064   | No file  | `32b52d2caf84`  |
| 1058   | No file  | `32b52d2caf84`  |
| 1051   | No file  | `32b52d2caf84`  |
| 1044   | No file  | `32b52d2caf84`  |
| 1036   | No file  | `32b52d2caf84`  |
| 1026   | No file  | `32b52d2caf84`  |
| 1016   | No file  | `32b52d2caf84`  |
| 1009   | No file  | `32b52d2caf84`  |
| 1005   | No file  | `32b52d2caf84`  |
| 1000   | No file  | `32b52d2caf84`  |
| 998    | No file  | `32b52d2caf84`  |
| 990    | No file  | `32b52d2caf84`  |
| 979    | No file  | `32b52d2caf84`  |
| 972    | No file  | `32b52d2caf84`  |
| 963    | No file  | `32b52d2caf84`  |
| 955    | No file  | `32b52d2caf84`  |
| 946    | No file  | `32b52d2caf84`  |
| 938    | No file  | `32b52d2caf84`  |
| 927    | No file  | `32b52d2caf84`  |
| 911    | No file  | `32b52d2caf84`  |
| 904    | No file  | `32b52d2caf84`  |
| 899    | No file  | `32b52d2caf84`  |
| 894    | No file  | `32b52d2caf84`  |
| 885    | No file  | `32b52d2caf84`  |
| 879    | No file  | `32b52d2caf84`  |
| 872    | No file  | `32b52d2caf84`  |
| 864    | No file  | `32b52d2caf84`  |
| 855    | No file  | `32b52d2caf84`  |
| 853    | No file  | `32b52d2caf84`  |
| 845    | No file  | `32b52d2caf84`  |
| 837    | No file  | `32b52d2caf84`  |
| 829    | No file  | `32b52d2caf84`  |
| 822    | No file  | `32b52d2caf84`  |
| 814    | No file  | `32b52d2caf84`  |
| 805    | No file  | `32b52d2caf84`  |
| 794    | No file  | `32b52d2caf84`  |
| 787    | No file  | `32b52d2caf84`  |
| 780    | No file  | `32b52d2caf84`  |
| 771    | No file  | `32b52d2caf84`  |
| 760    | No file  | `32b52d2caf84`  |
| 748    | No file  | `32b52d2caf84`  |
| 741    | No file  | `32b52d2caf84`  |
| 736    | No file  | `32b52d2caf84`  |
| 731    | No file  | `32b52d2caf84`  |
| 723    | No file  | `32b52d2caf84`  |
| 711    | No file  | `32b52d2caf84`  |
| 707    | No file  | `32b52d2caf84`  |
| 697    | No file  | `32b52d2caf84`  |
| 689    | No file  | `32b52d2caf84`  |
| 683    | No file  | `32b52d2caf84`  |
| 678    | No file  | `32b52d2caf84`  |
| 670    | No file  | `32b52d2caf84`  |
| 661    | No file  | `32b52d2caf84`  |
| 656    | No file  | `32b52d2caf84`  |
| 652    | No file  | `32b52d2caf84`  |
| 643    | No file  | `32b52d2caf84`  |
| 637    | No file  | `32b52d2caf84`  |
| 630    | No file  | `32b52d2caf84`  |
| 627    | No file  | `32b52d2caf84`  |
| 621    | No file  | `32b52d2caf84`  |
| 617    | No file  | `32b52d2caf84`  |
| 615    | No file  | `32b52d2caf84`  |
| 606    | No file  | `32b52d2caf84`  |
| 599    | No file  | `32b52d2caf84`  |
| 592    | No file  | `32b52d2caf84`  |
| 586    | No file  | `32b52d2caf84`  |
| 577    | No file  | `32b52d2caf84`  |
| 569    | No file  | `32b52d2caf84`  |
| 561    | No file  | `32b52d2caf84`  |
| 554    | No file  | `32b52d2caf84`  |
| 542    | No file  | `32b52d2caf84`  |
| 532    | No file  | `32b52d2caf84`  |
| 531    | No file  | `32b52d2caf84`  |
| 526    | No file  | `32b52d2caf84`  |
| 521    | No file  | `32b52d2caf84`  |
| 517    | No file  | `32b52d2caf84`  |
| 510    | No file  | `32b52d2caf84`  |
| 508    | No file  | `32b52d2caf84`  |
| 504    | No file  | `32b52d2caf84`  |
| 497    | No file  | `32b52d2caf84`  |
| 491    | No file  | `32b52d2caf84`  |
| 485    | No file  | `32b52d2caf84`  |
| 478    | No file  | `32b52d2caf84`  |
| 472    | No file  | `32b52d2caf84`  |
| 466    | No file  | `32b52d2caf84`  |
| 457    | No file  | `32b52d2caf84`  |
| 452    | No file  | `32b52d2caf84`  |
| 449    | No file  | `32b52d2caf84`  |
| 435    | No file  | `32b52d2caf84`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The groups sit where other `PABR` files keep their row count: the file
stores no group count, and the four groups of `InstantCashType` follow in
type order (`eInstant_Count` is `4`).

| Offset              | Type         | Field        | Notes                                         |
| ------------------- | ------------ | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                  |
| `+0x04`             | Group[4]     | groups       | See Group; type `0` to `3` in order           |
| `groups+0x00`       | String Table | string_table | See String Table                              |
| `string_table+0x00` | u32          | table_start  | Offset of the string table, where `groups` ends |
| `string_table+0x04` | u32          | zero         | Always `0`                                    |

### Group (variable: 9 bytes + entries)

| Offset  | Type                | Field       | Notes                                                       |
| ------- | ------------------- | ----------- | ----------------------------------------------------------- |
| `+0x00` | u8                  | unknown_00  | `0` on all four groups of clients 1784 and 3482             |
| `+0x01` | u64                 | entry_count | Number of `entries`: `70`, `70`, `70` and `16` on client 3482 |
| `+0x09` | Entry[entry_count]  | entries     | See Entry; `minute` rises within a group                    |

### Entry (16 bytes)

The 2016 `gc::InstantCashItem::value_type`, 16 bytes with its padding.

| Offset  | Type     | Field       | Notes                                                                                      |
| ------- | -------- | ----------- | ------------------------------------------------------------------------------------------ |
| `+0x00` | u16      | minute      | Remaining minutes this entry covers (`_minute`): `10` to `2160` in types `0` to `2`, `30` to `500` in type `3` on client 3482 |
| `+0x02` | bytes[6] | padding_02  | Alignment of `pearl_count` to 8 bytes; one value per file (`70 3D FC 7F 00 00` on client 3482, `8D 36 FA 01 00 00` on 1784), so not zeroed |
| `+0x08` | i64      | pearl_count | Cost (`_pearlCount`): Pearls, and Silver in type `2` on client 3482 (`10000000` for 10 minutes) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                        |
| ------- | ------------------ | ------------ | -------------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482                 |
| `+0x04` | pstr[string_count] | strings      | None                                         |

## Field Names

The 2016 `gc::InstantCashItem` holds a vector `_pearlList` of
`value_type { unsigned short _minute; __int64 _pearlCount; }` and a
`gc::InstantCashType _instantType`. The `InstantCashItem` sheet of a private
server's `DataSheets.bexcel` on client 1784 has the columns `InstantType`,
`Pearl`, `Minute`, `Hour` and `Second` (the last two derived from
`Minute`), 70 rows per type. Entry `n` of group `t` is compared with the
`n`-th sheet row of `InstantType` `t`.

| Field       | Column   | Same value (client 1784) | Same value (client 3482) |
| ----------- | -------- | ------------------------ | ------------------------ |
| minute      | `Minute` | 280 of 280               | 210 of 226               |
| pearl_count | `Pearl`  | 210 of 280               | 140 of 226               |

`pearl_count` misses all 70 rows of type `2` on client 1784, where the
sheet has `100` per row and the file `10`; client 3482 changes type `2` to
Silver and type `3` to 16 entries from 30 minutes. Types `0` and `1` match
70 of 70 on both clients, which fixes the group order.

## Open Questions

### What the Group Byte Holds

`unknown_00` is `0` before each of the four groups on clients 1784 and
3482. The 2016 struct ends with the one-byte `_instantType`, which would
read `0` to `3` here; a serializer that writes a vector after a flag would
also give one byte.
