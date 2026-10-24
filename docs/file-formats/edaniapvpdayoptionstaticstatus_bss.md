# `edaniapvpdayoptionstaticstatus.bss` Format

## Purpose

An Edania (Throne of Edana) schedule: three rows, each a list of entries
that hold a u8 and two times of the week (day, hour, minute), then one u8.
No client Lua call reads this file; the Edania window prints its times
with `ToClient_GetEdanaTimeString(__eEdaniaModeByTime_<mode>)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                 | Bytes | Records                 | Row bytes |
| ------ | -------------- | ------- | ------------------------------------ | ----- | ----------------------- | --------- |
| 1      | 3002 and later | 3483    | `edaniapvpdayoptionstaticstatus.bss` | 179   | 12 Time, 6 Entry, 3 Row | 12        |

| Layout | File                                 | Known         | Unknown    |
| ------ | ------------------------------------ | ------------- | ---------- |
| 1      | `edaniapvpdayoptionstaticstatus.bss` | 172 B (96.1%) | 7 B (3.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `42fbd62ff9d5`  |
| 3482   | Layout 1 | `42fbd62ff9d5`  |
| 3474   | Layout 1 | `42fbd62ff9d5`  |
| 3473   | Layout 1 | `42fbd62ff9d5`  |
| 3464   | Layout 1 | `42fbd62ff9d5`  |
| 3458   | Layout 1 | `42fbd62ff9d5`  |
| 3454   | Layout 1 | `42fbd62ff9d5`  |
| 3444   | Layout 1 | `42fbd62ff9d5`  |
| 3435   | Layout 1 | `42fbd62ff9d5`  |
| 3426   | Layout 1 | `42fbd62ff9d5`  |
| 3418   | Layout 1 | `42fbd62ff9d5`  |
| 3412   | Layout 1 | `42fbd62ff9d5`  |
| 3402   | Layout 1 | `42fbd62ff9d5`  |
| 3396   | Layout 1 | `42fbd62ff9d5`  |
| 3387   | Layout 1 | `42fbd62ff9d5`  |
| 3381   | Layout 1 | `42fbd62ff9d5`  |
| 3373   | Layout 1 | `42fbd62ff9d5`  |
| 3364   | Layout 1 | `42fbd62ff9d5`  |
| 3356   | Layout 1 | `42fbd62ff9d5`  |
| 3349   | Layout 1 | `42fbd62ff9d5`  |
| 3342   | Layout 1 | `42fbd62ff9d5`  |
| 3335   | Layout 1 | `42fbd62ff9d5`  |
| 3326   | Layout 1 | `42fbd62ff9d5`  |
| 3321   | Layout 1 | `42fbd62ff9d5`  |
| 3314   | Layout 1 | `42fbd62ff9d5`  |
| 3303   | Layout 1 | `42fbd62ff9d5`  |
| 3302   | Layout 1 | `42fbd62ff9d5`  |
| 3293   | Layout 1 | `42fbd62ff9d5`  |
| 3283   | Layout 1 | `42fbd62ff9d5`  |
| 3275   | Layout 1 | `42fbd62ff9d5`  |
| 3267   | Layout 1 | `42fbd62ff9d5`  |
| 3258   | Layout 1 | `42fbd62ff9d5`  |
| 3251   | Layout 1 | `42fbd62ff9d5`  |
| 3242   | Layout 1 | `42fbd62ff9d5`  |
| 3235   | Layout 1 | `42fbd62ff9d5`  |
| 3229   | Layout 1 | `42fbd62ff9d5`  |
| 3212   | Layout 1 | `42fbd62ff9d5`  |
| 3203   | Layout 1 | `42fbd62ff9d5`  |
| 3193   | Layout 1 | `42fbd62ff9d5`  |
| 3186   | Layout 1 | `42fbd62ff9d5`  |
| 3177   | Layout 1 | `42fbd62ff9d5`  |
| 3169   | Layout 1 | `42fbd62ff9d5`  |
| 3158   | Layout 1 | `42fbd62ff9d5`  |
| 3151   | Layout 1 | `42fbd62ff9d5`  |
| 3144   | Layout 1 | `42fbd62ff9d5`  |
| 3133   | Layout 1 | `42fbd62ff9d5`  |
| 3125   | Layout 1 | `42fbd62ff9d5`  |
| 3118   | Layout 1 | `42fbd62ff9d5`  |
| 3111   | Layout 1 | `42fbd62ff9d5`  |
| 3103   | Layout 1 | `42fbd62ff9d5`  |
| 3095   | Layout 1 | `42fbd62ff9d5`  |
| 3086   | Layout 1 | `42fbd62ff9d5`  |
| 3072   | Layout 1 | `42fbd62ff9d5`  |
| 3062   | Layout 1 | `42fbd62ff9d5`  |
| 3052   | Layout 1 | `42fbd62ff9d5`  |
| 3045   | Layout 1 | `42fbd62ff9d5`  |
| 3037   | Layout 1 | `42fbd62ff9d5`  |
| 3030   | Layout 1 | `42fbd62ff9d5`  |
| 3021   | Layout 1 | `42fbd62ff9d5`  |
| 3012   | Layout 1 | `42fbd62ff9d5`  |
| 3002   | Layout 1 | `42fbd62ff9d5`  |
| 2995   | No file  | `42fbd62ff9d5`  |
| 2987   | No file  | `42fbd62ff9d5`  |
| 2978   | No file  | `42fbd62ff9d5`  |
| 2970   | No file  | `42fbd62ff9d5`  |
| 2959   | No file  | `42fbd62ff9d5`  |
| 2951   | No file  | `42fbd62ff9d5`  |
| 2942   | No file  | `42fbd62ff9d5`  |
| 2935   | No file  | `42fbd62ff9d5`  |
| 2932   | No file  | `42fbd62ff9d5`  |
| 2923   | No file  | `42fbd62ff9d5`  |
| 2919   | No file  | `42fbd62ff9d5`  |
| 2907   | No file  | `42fbd62ff9d5`  |
| 2900   | No file  | `42fbd62ff9d5`  |
| 2891   | No file  | `42fbd62ff9d5`  |
| 2882   | No file  | `42fbd62ff9d5`  |
| 2872   | No file  | `42fbd62ff9d5`  |
| 2863   | No file  | `42fbd62ff9d5`  |
| 2855   | No file  | `42fbd62ff9d5`  |
| 2849   | No file  | `42fbd62ff9d5`  |
| 2844   | No file  | `42fbd62ff9d5`  |
| 2834   | No file  | `42fbd62ff9d5`  |
| 2825   | No file  | `42fbd62ff9d5`  |
| 2819   | No file  | `42fbd62ff9d5`  |
| 2811   | No file  | `42fbd62ff9d5`  |
| 2803   | No file  | `42fbd62ff9d5`  |
| 2794   | No file  | `42fbd62ff9d5`  |
| 2783   | No file  | `42fbd62ff9d5`  |
| 2774   | No file  | `42fbd62ff9d5`  |
| 2765   | No file  | `42fbd62ff9d5`  |
| 2756   | No file  | `42fbd62ff9d5`  |
| 2750   | No file  | `42fbd62ff9d5`  |
| 2743   | No file  | `42fbd62ff9d5`  |
| 2736   | No file  | `42fbd62ff9d5`  |
| 2726   | No file  | `42fbd62ff9d5`  |
| 2717   | No file  | `42fbd62ff9d5`  |
| 2709   | No file  | `42fbd62ff9d5`  |
| 2703   | No file  | `42fbd62ff9d5`  |
| 2695   | No file  | `42fbd62ff9d5`  |
| 2684   | No file  | `42fbd62ff9d5`  |
| 2672   | No file  | `42fbd62ff9d5`  |
| 2665   | No file  | `42fbd62ff9d5`  |
| 2657   | No file  | `42fbd62ff9d5`  |
| 2649   | No file  | `42fbd62ff9d5`  |
| 2644   | No file  | `42fbd62ff9d5`  |
| 2637   | No file  | `42fbd62ff9d5`  |
| 2629   | No file  | `42fbd62ff9d5`  |
| 2619   | No file  | `42fbd62ff9d5`  |
| 2612   | No file  | `42fbd62ff9d5`  |
| 2606   | No file  | `42fbd62ff9d5`  |
| 2602   | No file  | `42fbd62ff9d5`  |
| 2601   | No file  | `42fbd62ff9d5`  |
| 2592   | No file  | `42fbd62ff9d5`  |
| 2583   | No file  | `42fbd62ff9d5`  |
| 2575   | No file  | `42fbd62ff9d5`  |
| 2567   | No file  | `42fbd62ff9d5`  |
| 2560   | No file  | `42fbd62ff9d5`  |
| 2553   | No file  | `42fbd62ff9d5`  |
| 2545   | No file  | `42fbd62ff9d5`  |
| 2538   | No file  | `42fbd62ff9d5`  |
| 2529   | No file  | `42fbd62ff9d5`  |
| 2519   | No file  | `42fbd62ff9d5`  |
| 2513   | No file  | `42fbd62ff9d5`  |
| 2510   | No file  | `42fbd62ff9d5`  |
| 2507   | No file  | `42fbd62ff9d5`  |
| 2503   | No file  | `42fbd62ff9d5`  |
| 2498   | No file  | `42fbd62ff9d5`  |
| 2492   | No file  | `42fbd62ff9d5`  |
| 2487   | No file  | `42fbd62ff9d5`  |
| 2480   | No file  | `42fbd62ff9d5`  |
| 2474   | No file  | `42fbd62ff9d5`  |
| 2468   | No file  | `42fbd62ff9d5`  |
| 2460   | No file  | `42fbd62ff9d5`  |
| 2453   | No file  | `42fbd62ff9d5`  |
| 2444   | No file  | `42fbd62ff9d5`  |
| 2438   | No file  | `42fbd62ff9d5`  |
| 2434   | No file  | `42fbd62ff9d5`  |
| 2429   | No file  | `42fbd62ff9d5`  |
| 2421   | No file  | `42fbd62ff9d5`  |
| 2414   | No file  | `42fbd62ff9d5`  |
| 2407   | No file  | `42fbd62ff9d5`  |
| 2401   | No file  | `42fbd62ff9d5`  |
| 2397   | No file  | `42fbd62ff9d5`  |
| 2393   | No file  | `42fbd62ff9d5`  |
| 2384   | No file  | `42fbd62ff9d5`  |
| 2378   | No file  | `42fbd62ff9d5`  |
| 2372   | No file  | `42fbd62ff9d5`  |
| 2358   | No file  | `42fbd62ff9d5`  |
| 2352   | No file  | `42fbd62ff9d5`  |
| 2347   | No file  | `42fbd62ff9d5`  |
| 2343   | No file  | `42fbd62ff9d5`  |
| 2335   | No file  | `42fbd62ff9d5`  |
| 2327   | No file  | `42fbd62ff9d5`  |
| 2324   | No file  | `42fbd62ff9d5`  |
| 2319   | No file  | `42fbd62ff9d5`  |
| 2313   | No file  | `42fbd62ff9d5`  |
| 2308   | No file  | `42fbd62ff9d5`  |
| 2302   | No file  | `42fbd62ff9d5`  |
| 2295   | No file  | `42fbd62ff9d5`  |
| 2290   | No file  | `42fbd62ff9d5`  |
| 2284   | No file  | `42fbd62ff9d5`  |
| 2276   | No file  | `42fbd62ff9d5`  |
| 2269   | No file  | `42fbd62ff9d5`  |
| 2259   | No file  | `42fbd62ff9d5`  |
| 2250   | No file  | `42fbd62ff9d5`  |
| 2243   | No file  | `42fbd62ff9d5`  |
| 2235   | No file  | `42fbd62ff9d5`  |
| 2229   | No file  | `42fbd62ff9d5`  |
| 2224   | No file  | `42fbd62ff9d5`  |
| 2218   | No file  | `42fbd62ff9d5`  |
| 2215   | No file  | `42fbd62ff9d5`  |
| 2207   | No file  | `42fbd62ff9d5`  |
| 2203   | No file  | `42fbd62ff9d5`  |
| 2196   | No file  | `42fbd62ff9d5`  |
| 2192   | No file  | `42fbd62ff9d5`  |
| 2189   | No file  | `42fbd62ff9d5`  |
| 2183   | No file  | `42fbd62ff9d5`  |
| 2179   | No file  | `42fbd62ff9d5`  |
| 2171   | No file  | `42fbd62ff9d5`  |
| 2163   | No file  | `42fbd62ff9d5`  |
| 2156   | No file  | `42fbd62ff9d5`  |
| 2151   | No file  | `42fbd62ff9d5`  |
| 2147   | No file  | `42fbd62ff9d5`  |
| 2142   | No file  | `42fbd62ff9d5`  |
| 2138   | No file  | `42fbd62ff9d5`  |
| 2134   | No file  | `42fbd62ff9d5`  |
| 2130   | No file  | `42fbd62ff9d5`  |
| 2122   | No file  | `42fbd62ff9d5`  |
| 2107   | No file  | `42fbd62ff9d5`  |
| 2098   | No file  | `42fbd62ff9d5`  |
| 2089   | No file  | `42fbd62ff9d5`  |
| 2081   | No file  | `42fbd62ff9d5`  |
| 2073   | No file  | `42fbd62ff9d5`  |
| 2067   | No file  | `42fbd62ff9d5`  |
| 2063   | No file  | `42fbd62ff9d5`  |
| 2059   | No file  | `42fbd62ff9d5`  |
| 2052   | No file  | `42fbd62ff9d5`  |
| 2044   | No file  | `42fbd62ff9d5`  |
| 2039   | No file  | `42fbd62ff9d5`  |
| 2032   | No file  | `42fbd62ff9d5`  |
| 2025   | No file  | `42fbd62ff9d5`  |
| 2011   | No file  | `42fbd62ff9d5`  |
| 2005   | No file  | `42fbd62ff9d5`  |
| 2000   | No file  | `42fbd62ff9d5`  |
| 1996   | No file  | `42fbd62ff9d5`  |
| 1991   | No file  | `42fbd62ff9d5`  |
| 1985   | No file  | `42fbd62ff9d5`  |
| 1980   | No file  | `42fbd62ff9d5`  |
| 1969   | No file  | `42fbd62ff9d5`  |
| 1964   | No file  | `42fbd62ff9d5`  |
| 1958   | No file  | `42fbd62ff9d5`  |
| 1950   | No file  | `42fbd62ff9d5`  |
| 1945   | No file  | `42fbd62ff9d5`  |
| 1937   | No file  | `42fbd62ff9d5`  |
| 1933   | No file  | `42fbd62ff9d5`  |
| 1927   | No file  | `42fbd62ff9d5`  |
| 1921   | No file  | `42fbd62ff9d5`  |
| 1914   | No file  | `42fbd62ff9d5`  |
| 1908   | No file  | `42fbd62ff9d5`  |
| 1897   | No file  | `42fbd62ff9d5`  |
| 1892   | No file  | `42fbd62ff9d5`  |
| 1886   | No file  | `42fbd62ff9d5`  |
| 1881   | No file  | `42fbd62ff9d5`  |
| 1871   | No file  | `42fbd62ff9d5`  |
| 1866   | No file  | `42fbd62ff9d5`  |
| 1862   | No file  | `42fbd62ff9d5`  |
| 1854   | No file  | `42fbd62ff9d5`  |
| 1846   | No file  | `42fbd62ff9d5`  |
| 1838   | No file  | `42fbd62ff9d5`  |
| 1832   | No file  | `42fbd62ff9d5`  |
| 1826   | No file  | `42fbd62ff9d5`  |
| 1822   | No file  | `42fbd62ff9d5`  |
| 1818   | No file  | `42fbd62ff9d5`  |
| 1804   | No file  | `42fbd62ff9d5`  |
| 1794   | No file  | `42fbd62ff9d5`  |
| 1790   | No file  | `42fbd62ff9d5`  |
| 1784   | No file  | `42fbd62ff9d5`  |
| 1774   | No file  | `42fbd62ff9d5`  |
| 1771   | No file  | `42fbd62ff9d5`  |
| 1762   | No file  | `42fbd62ff9d5`  |
| 1759   | No file  | `42fbd62ff9d5`  |
| 1754   | No file  | `42fbd62ff9d5`  |
| 1749   | No file  | `42fbd62ff9d5`  |
| 1743   | No file  | `42fbd62ff9d5`  |
| 1737   | No file  | `42fbd62ff9d5`  |
| 1731   | No file  | `42fbd62ff9d5`  |
| 1725   | No file  | `42fbd62ff9d5`  |
| 1717   | No file  | `42fbd62ff9d5`  |
| 1710   | No file  | `42fbd62ff9d5`  |
| 1704   | No file  | `42fbd62ff9d5`  |
| 1698   | No file  | `42fbd62ff9d5`  |
| 1690   | No file  | `42fbd62ff9d5`  |
| 1685   | No file  | `42fbd62ff9d5`  |
| 1680   | No file  | `42fbd62ff9d5`  |
| 1674   | No file  | `42fbd62ff9d5`  |
| 1668   | No file  | `42fbd62ff9d5`  |
| 1659   | No file  | `42fbd62ff9d5`  |
| 1649   | No file  | `42fbd62ff9d5`  |
| 1642   | No file  | `42fbd62ff9d5`  |
| 1636   | No file  | `42fbd62ff9d5`  |
| 1628   | No file  | `42fbd62ff9d5`  |
| 1622   | No file  | `42fbd62ff9d5`  |
| 1614   | No file  | `42fbd62ff9d5`  |
| 1608   | No file  | `42fbd62ff9d5`  |
| 1602   | No file  | `42fbd62ff9d5`  |
| 1598   | No file  | `42fbd62ff9d5`  |
| 1594   | No file  | `42fbd62ff9d5`  |
| 1590   | No file  | `42fbd62ff9d5`  |
| 1587   | No file  | `42fbd62ff9d5`  |
| 1584   | No file  | `42fbd62ff9d5`  |
| 1579   | No file  | `42fbd62ff9d5`  |
| 1572   | No file  | `42fbd62ff9d5`  |
| 1565   | No file  | `42fbd62ff9d5`  |
| 1559   | No file  | `42fbd62ff9d5`  |
| 1554   | No file  | `42fbd62ff9d5`  |
| 1547   | No file  | `42fbd62ff9d5`  |
| 1537   | No file  | `42fbd62ff9d5`  |
| 1529   | No file  | `42fbd62ff9d5`  |
| 1524   | No file  | `42fbd62ff9d5`  |
| 1519   | No file  | `42fbd62ff9d5`  |
| 1509   | No file  | `42fbd62ff9d5`  |
| 1506   | No file  | `42fbd62ff9d5`  |
| 1504   | No file  | `42fbd62ff9d5`  |
| 1500   | No file  | `42fbd62ff9d5`  |
| 1493   | No file  | `42fbd62ff9d5`  |
| 1489   | No file  | `42fbd62ff9d5`  |
| 1485   | No file  | `42fbd62ff9d5`  |
| 1481   | No file  | `42fbd62ff9d5`  |
| 1474   | No file  | `42fbd62ff9d5`  |
| 1466   | No file  | `42fbd62ff9d5`  |
| 1462   | No file  | `42fbd62ff9d5`  |
| 1459   | No file  | `42fbd62ff9d5`  |
| 1453   | No file  | `42fbd62ff9d5`  |
| 1450   | No file  | `42fbd62ff9d5`  |
| 1445   | No file  | `42fbd62ff9d5`  |
| 1439   | No file  | `42fbd62ff9d5`  |
| 1433   | No file  | `42fbd62ff9d5`  |
| 1430   | No file  | `42fbd62ff9d5`  |
| 1426   | No file  | `42fbd62ff9d5`  |
| 1421   | No file  | `42fbd62ff9d5`  |
| 1417   | No file  | `42fbd62ff9d5`  |
| 1416   | No file  | `42fbd62ff9d5`  |
| 1409   | No file  | `42fbd62ff9d5`  |
| 1405   | No file  | `42fbd62ff9d5`  |
| 1401   | No file  | `42fbd62ff9d5`  |
| 1396   | No file  | `42fbd62ff9d5`  |
| 1391   | No file  | `42fbd62ff9d5`  |
| 1390   | No file  | `42fbd62ff9d5`  |
| 1386   | No file  | `42fbd62ff9d5`  |
| 1381   | No file  | `42fbd62ff9d5`  |
| 1379   | No file  | `42fbd62ff9d5`  |
| 1372   | No file  | `42fbd62ff9d5`  |
| 1366   | No file  | `42fbd62ff9d5`  |
| 1364   | No file  | `42fbd62ff9d5`  |
| 1363   | No file  | `42fbd62ff9d5`  |
| 1360   | No file  | `42fbd62ff9d5`  |
| 1358   | No file  | `42fbd62ff9d5`  |
| 1355   | No file  | `42fbd62ff9d5`  |
| 1351   | No file  | `42fbd62ff9d5`  |
| 1348   | No file  | `42fbd62ff9d5`  |
| 1346   | No file  | `42fbd62ff9d5`  |
| 1341   | No file  | `42fbd62ff9d5`  |
| 1340   | No file  | `42fbd62ff9d5`  |
| 1338   | No file  | `42fbd62ff9d5`  |
| 1335   | No file  | `42fbd62ff9d5`  |
| 1333   | No file  | `42fbd62ff9d5`  |
| 1329   | No file  | `42fbd62ff9d5`  |
| 1327   | No file  | `42fbd62ff9d5`  |
| 1324   | No file  | `42fbd62ff9d5`  |
| 1321   | No file  | `42fbd62ff9d5`  |
| 1319   | No file  | `42fbd62ff9d5`  |
| 1318   | No file  | `42fbd62ff9d5`  |
| 1316   | No file  | `42fbd62ff9d5`  |
| 1313   | No file  | `42fbd62ff9d5`  |
| 1311   | No file  | `42fbd62ff9d5`  |
| 1309   | No file  | `42fbd62ff9d5`  |
| 1304   | No file  | `42fbd62ff9d5`  |
| 1292   | No file  | `42fbd62ff9d5`  |
| 1286   | No file  | `42fbd62ff9d5`  |
| 1280   | No file  | `42fbd62ff9d5`  |
| 1276   | No file  | `42fbd62ff9d5`  |
| 1267   | No file  | `42fbd62ff9d5`  |
| 1261   | No file  | `42fbd62ff9d5`  |
| 1256   | No file  | `42fbd62ff9d5`  |
| 1250   | No file  | `42fbd62ff9d5`  |
| 1246   | No file  | `42fbd62ff9d5`  |
| 1239   | No file  | `42fbd62ff9d5`  |
| 1230   | No file  | `42fbd62ff9d5`  |
| 1226   | No file  | `42fbd62ff9d5`  |
| 1220   | No file  | `42fbd62ff9d5`  |
| 1217   | No file  | `42fbd62ff9d5`  |
| 1211   | No file  | `42fbd62ff9d5`  |
| 1210   | No file  | `42fbd62ff9d5`  |
| 1208   | No file  | `42fbd62ff9d5`  |
| 1203   | No file  | `42fbd62ff9d5`  |
| 1197   | No file  | `42fbd62ff9d5`  |
| 1194   | No file  | `42fbd62ff9d5`  |
| 1192   | No file  | `42fbd62ff9d5`  |
| 1187   | No file  | `42fbd62ff9d5`  |
| 1183   | No file  | `42fbd62ff9d5`  |
| 1177   | No file  | `42fbd62ff9d5`  |
| 1173   | No file  | `42fbd62ff9d5`  |
| 1167   | No file  | `42fbd62ff9d5`  |
| 1164   | No file  | `42fbd62ff9d5`  |
| 1156   | No file  | `42fbd62ff9d5`  |
| 1149   | No file  | `42fbd62ff9d5`  |
| 1144   | No file  | `42fbd62ff9d5`  |
| 1137   | No file  | `42fbd62ff9d5`  |
| 1132   | No file  | `42fbd62ff9d5`  |
| 1127   | No file  | `42fbd62ff9d5`  |
| 1122   | No file  | `42fbd62ff9d5`  |
| 1118   | No file  | `42fbd62ff9d5`  |
| 1114   | No file  | `42fbd62ff9d5`  |
| 1109   | No file  | `42fbd62ff9d5`  |
| 1102   | No file  | `42fbd62ff9d5`  |
| 1096   | No file  | `42fbd62ff9d5`  |
| 1088   | No file  | `42fbd62ff9d5`  |
| 1081   | No file  | `42fbd62ff9d5`  |
| 1076   | No file  | `42fbd62ff9d5`  |
| 1069   | No file  | `42fbd62ff9d5`  |
| 1064   | No file  | `42fbd62ff9d5`  |
| 1058   | No file  | `42fbd62ff9d5`  |
| 1051   | No file  | `42fbd62ff9d5`  |
| 1044   | No file  | `42fbd62ff9d5`  |
| 1036   | No file  | `42fbd62ff9d5`  |
| 1026   | No file  | `42fbd62ff9d5`  |
| 1016   | No file  | `42fbd62ff9d5`  |
| 1009   | No file  | `42fbd62ff9d5`  |
| 1005   | No file  | `42fbd62ff9d5`  |
| 1000   | No file  | `42fbd62ff9d5`  |
| 998    | No file  | `42fbd62ff9d5`  |
| 990    | No file  | `42fbd62ff9d5`  |
| 979    | No file  | `42fbd62ff9d5`  |
| 972    | No file  | `42fbd62ff9d5`  |
| 963    | No file  | `42fbd62ff9d5`  |
| 955    | No file  | `42fbd62ff9d5`  |
| 946    | No file  | `42fbd62ff9d5`  |
| 938    | No file  | `42fbd62ff9d5`  |
| 927    | No file  | `42fbd62ff9d5`  |
| 911    | No file  | `42fbd62ff9d5`  |
| 904    | No file  | `42fbd62ff9d5`  |
| 899    | No file  | `42fbd62ff9d5`  |
| 894    | No file  | `42fbd62ff9d5`  |
| 885    | No file  | `42fbd62ff9d5`  |
| 879    | No file  | `42fbd62ff9d5`  |
| 872    | No file  | `42fbd62ff9d5`  |
| 864    | No file  | `42fbd62ff9d5`  |
| 855    | No file  | `42fbd62ff9d5`  |
| 853    | No file  | `42fbd62ff9d5`  |
| 845    | No file  | `42fbd62ff9d5`  |
| 837    | No file  | `42fbd62ff9d5`  |
| 829    | No file  | `42fbd62ff9d5`  |
| 822    | No file  | `42fbd62ff9d5`  |
| 814    | No file  | `42fbd62ff9d5`  |
| 805    | No file  | `42fbd62ff9d5`  |
| 794    | No file  | `42fbd62ff9d5`  |
| 787    | No file  | `42fbd62ff9d5`  |
| 780    | No file  | `42fbd62ff9d5`  |
| 771    | No file  | `42fbd62ff9d5`  |
| 760    | No file  | `42fbd62ff9d5`  |
| 748    | No file  | `42fbd62ff9d5`  |
| 741    | No file  | `42fbd62ff9d5`  |
| 736    | No file  | `42fbd62ff9d5`  |
| 731    | No file  | `42fbd62ff9d5`  |
| 723    | No file  | `42fbd62ff9d5`  |
| 711    | No file  | `42fbd62ff9d5`  |
| 707    | No file  | `42fbd62ff9d5`  |
| 697    | No file  | `42fbd62ff9d5`  |
| 689    | No file  | `42fbd62ff9d5`  |
| 683    | No file  | `42fbd62ff9d5`  |
| 678    | No file  | `42fbd62ff9d5`  |
| 670    | No file  | `42fbd62ff9d5`  |
| 661    | No file  | `42fbd62ff9d5`  |
| 656    | No file  | `42fbd62ff9d5`  |
| 652    | No file  | `42fbd62ff9d5`  |
| 643    | No file  | `42fbd62ff9d5`  |
| 637    | No file  | `42fbd62ff9d5`  |
| 630    | No file  | `42fbd62ff9d5`  |
| 627    | No file  | `42fbd62ff9d5`  |
| 621    | No file  | `42fbd62ff9d5`  |
| 617    | No file  | `42fbd62ff9d5`  |
| 615    | No file  | `42fbd62ff9d5`  |
| 606    | No file  | `42fbd62ff9d5`  |
| 599    | No file  | `42fbd62ff9d5`  |
| 592    | No file  | `42fbd62ff9d5`  |
| 586    | No file  | `42fbd62ff9d5`  |
| 577    | No file  | `42fbd62ff9d5`  |
| 569    | No file  | `42fbd62ff9d5`  |
| 561    | No file  | `42fbd62ff9d5`  |
| 554    | No file  | `42fbd62ff9d5`  |
| 542    | No file  | `42fbd62ff9d5`  |
| 532    | No file  | `42fbd62ff9d5`  |
| 531    | No file  | `42fbd62ff9d5`  |
| 526    | No file  | `42fbd62ff9d5`  |
| 521    | No file  | `42fbd62ff9d5`  |
| 517    | No file  | `42fbd62ff9d5`  |
| 510    | No file  | `42fbd62ff9d5`  |
| 508    | No file  | `42fbd62ff9d5`  |
| 504    | No file  | `42fbd62ff9d5`  |
| 497    | No file  | `42fbd62ff9d5`  |
| 491    | No file  | `42fbd62ff9d5`  |
| 485    | No file  | `42fbd62ff9d5`  |
| 478    | No file  | `42fbd62ff9d5`  |
| 472    | No file  | `42fbd62ff9d5`  |
| 466    | No file  | `42fbd62ff9d5`  |
| 457    | No file  | `42fbd62ff9d5`  |
| 452    | No file  | `42fbd62ff9d5`  |
| 449    | No file  | `42fbd62ff9d5`  |
| 435    | No file  | `42fbd62ff9d5`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset      | Type         | Field           | Notes                                                    |
| ----------- | ------------ | --------------- | -------------------------------------------------------- |
| `+0x00`     | char[4]      | magic           | ASCII `PABR`                                             |
| `+0x04`     | Row[3]       | rows            | See Row; no row count                                    |
| `rows+0x00` | u8           | unknown_rows_00 | `1` on clients 3002, 3474 and 3482, `0` on client 3251   |
| `rows+0x01` | String Table | string_table    | See String Table                                         |
| `EOF-0x08`  | u32          | table_start     | Offset of the string table, where `unknown_rows_00` ends |
| `EOF-0x04`  | u32          | zero            | Always `0`                                               |

### Row (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                       |
| ------- | ------------------ | ----------- | ------------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; `2` on every client checked |
| `+0x04` | Entry[entry_count] | entries     | See Entry                                   |

### Entry (25 bytes)

| Offset  | Type    | Field      | Notes                                  |
| ------- | ------- | ---------- | -------------------------------------- |
| `+0x00` | u8      | unknown_00 | `0` on the first entry, `1` on the second |
| `+0x01` | Time[2] | times      | See Time and Schedule                  |

### Time (12 bytes)

| Offset  | Type | Field       | Notes       |
| ------- | ---- | ----------- | ----------- |
| `+0x00` | u32  | day_of_week | `0` Sunday to `6` Saturday |
| `+0x04` | u32  | hour        | `0` to `23` |
| `+0x08` | u32  | minute      | `0` to `59` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Schedule

The two times of each entry as day, hour and minute (client 3482):

| Row | `unknown_00` | Time 1    | Time 2    |
| --- | ------------ | --------- | --------- |
| 0   | `0`          | `1` 07:00 | `0` 07:00 |
| 0   | `1`          | `0` 22:00 | `6` 22:00 |
| 1   | `0`          | `1` 00:10 | `1` 00:20 |
| 1   | `1`          | `0` 17:10 | `0` 17:20 |
| 2   | `0`          | `1` 00:30 | `1` 00:50 |
| 2   | `1`          | `0` 17:30 | `0` 17:50 |

On client 3251 every hour of the `1` entries is one later (`0` 23:00,
`0` 18:10, `0` 18:30), the shift of a daylight saving change; the `0`
entries are the same. Client 3002 holds other times in row `0` (`4` 07:00
to `1` 00:00, and `4` 00:00 to `0` 17:00) and the same rows `1` and `2`.

## Field Names

Edania is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers this file. `day_of_week`,
`hour` and `minute` follow the Time of
[`rosewarstaticstatus.bss`](rosewarstaticstatus_bss.md), which has the
same u8-then-times entries: the values stay in `0` to `6`, `0` to `23` and
`0` to `59`, and a client update moves the hours of one entry by a whole
hour.

## Notes

- The file is 179 bytes on clients 3002, 3251, 3474 and 3482. It is not in
  the archives of client 1784.
- Within rows `1` and `2` the second time is 10 and 20 minutes after the
  first, on the same day.
- The official Throne of Edana page of the NA/EU game wiki (wikiNo 457)
  sets the EU battles on Sunday in UTC: the 10-challenger battle ("Game of
  the Edanas - Candidates") 17:10 to 17:20 and the final challenger vs.
  Edana battle ("Selection") from 17:30. Those are the times of the `1`
  entries of rows `1` and `2` on client 3482 (`0` 17:10 to `0` 17:20, `0`
  17:30 to `0` 17:50), which makes `0` Sunday, row `1` the challenger
  battle and row `2` the Edana battle. The handler shows the days by name.
- The handler shows one row per entry: the row number and both times as
  `<day name> <hh:mm>`.

## Open Questions

### Row 0

Row `0` spans most of a week (`1` 07:00 to `0` 07:00, and `0` 22:00 to
`6` 22:00), which fits the application period. The official wiki page
gives Monday 00:00 to Sunday 00:00 (UTC) for applications, with the NA
deadline Sunday 00:00 and the EU deadline Sunday 17:00 (UTC); neither
entry of row `0` matches those times.

### The Two Entries

`unknown_00` is `0` and `1` in every row. The `1` entries hold the EU
battle times in UTC (see Notes), and only they moved by an hour on client
3251, a daylight saving change. The `0` entries (`1` 00:10 and `1` 00:30,
Monday) match neither the NA times on the official wiki page (Sunday
00:10 and 00:30 UTC) nor the EU ones, so which region they serve is
open; `unknown_rows_00` is open too.
