# `snowboard.bss` Format

## Purpose

The snowboard courses of Snowfall Crasher: Alpine Glide. After a head
of settings for the whole field, each course gives its key, Korean name,
mode and chain of checkpoints; two lists of effect settings follow. The
snowboard menu (`panel_window_snowboard_menu_all_1.luac`, client 3482)
makes one tab per course from `ToClient_SnowBoardCourseCount()` and
`ToClient_GetSnowBoardStaticStatusByIndex(ii)`, reading `getKeyRaw()`,
`getMode()` and `getName()`; the race HUD reads `getCheckPointCount()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes | Records                                   | Row bytes |
| ------ | -------------- | ------- | --------------- | ----- | ----------------------------------------- | --------- |
| 1      | 3151 and later | 3483    | `snowboard.bss` | 3,293 | 45 Checkpoint, 3 Course, 2 Item, 7 Effect | 50        |

| Layout | File            | Known         | Unknown         |
| ------ | --------------- | ------------- | --------------- |
| 1      | `snowboard.bss` | 961 B (29.2%) | 2,332 B (70.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `f41b92a22070`  |
| 3482   | Layout 1 | `f41b92a22070`  |
| 3474   | Layout 1 | `f41b92a22070`  |
| 3473   | Layout 1 | `f41b92a22070`  |
| 3464   | Layout 1 | `f41b92a22070`  |
| 3458   | Layout 1 | `f41b92a22070`  |
| 3454   | Layout 1 | `f41b92a22070`  |
| 3444   | Layout 1 | `f41b92a22070`  |
| 3435   | Layout 1 | `f41b92a22070`  |
| 3426   | Layout 1 | `f41b92a22070`  |
| 3418   | Layout 1 | `f41b92a22070`  |
| 3412   | Layout 1 | `f41b92a22070`  |
| 3402   | Layout 1 | `f41b92a22070`  |
| 3396   | Layout 1 | `f41b92a22070`  |
| 3387   | Layout 1 | `f41b92a22070`  |
| 3381   | Layout 1 | `f41b92a22070`  |
| 3373   | Layout 1 | `f41b92a22070`  |
| 3364   | Layout 1 | `f41b92a22070`  |
| 3356   | Layout 1 | `f41b92a22070`  |
| 3349   | Layout 1 | `f41b92a22070`  |
| 3342   | Layout 1 | `f41b92a22070`  |
| 3335   | Layout 1 | `f41b92a22070`  |
| 3326   | Layout 1 | `f41b92a22070`  |
| 3321   | Layout 1 | `f41b92a22070`  |
| 3314   | Layout 1 | `f41b92a22070`  |
| 3303   | Layout 1 | `f41b92a22070`  |
| 3302   | Layout 1 | `f41b92a22070`  |
| 3293   | Layout 1 | `f41b92a22070`  |
| 3283   | Layout 1 | `f41b92a22070`  |
| 3275   | Layout 1 | `f41b92a22070`  |
| 3267   | Layout 1 | `f41b92a22070`  |
| 3258   | Layout 1 | `f41b92a22070`  |
| 3251   | Layout 1 | `f41b92a22070`  |
| 3242   | Layout 1 | `f41b92a22070`  |
| 3235   | Layout 1 | `f41b92a22070`  |
| 3229   | Layout 1 | `f41b92a22070`  |
| 3212   | Layout 1 | `f41b92a22070`  |
| 3203   | Layout 1 | `f41b92a22070`  |
| 3193   | Layout 1 | `f41b92a22070`  |
| 3186   | No file  | `f41b92a22070`  |
| 3177   | Layout 1 | `f41b92a22070`  |
| 3169   | Layout 1 | `f41b92a22070`  |
| 3158   | Layout 1 | `f41b92a22070`  |
| 3151   | Layout 1 | `f41b92a22070`  |
| 3144   | No file  | `f41b92a22070`  |
| 3133   | No file  | `f41b92a22070`  |
| 3125   | No file  | `f41b92a22070`  |
| 3118   | No file  | `f41b92a22070`  |
| 3111   | No file  | `f41b92a22070`  |
| 3103   | No file  | `f41b92a22070`  |
| 3095   | No file  | `f41b92a22070`  |
| 3086   | No file  | `f41b92a22070`  |
| 3072   | No file  | `f41b92a22070`  |
| 3062   | No file  | `f41b92a22070`  |
| 3052   | No file  | `f41b92a22070`  |
| 3045   | No file  | `f41b92a22070`  |
| 3037   | No file  | `f41b92a22070`  |
| 3030   | No file  | `f41b92a22070`  |
| 3021   | No file  | `f41b92a22070`  |
| 3012   | No file  | `f41b92a22070`  |
| 3002   | No file  | `f41b92a22070`  |
| 2995   | No file  | `f41b92a22070`  |
| 2987   | No file  | `f41b92a22070`  |
| 2978   | No file  | `f41b92a22070`  |
| 2970   | No file  | `f41b92a22070`  |
| 2959   | No file  | `f41b92a22070`  |
| 2951   | No file  | `f41b92a22070`  |
| 2942   | No file  | `f41b92a22070`  |
| 2935   | No file  | `f41b92a22070`  |
| 2932   | No file  | `f41b92a22070`  |
| 2923   | No file  | `f41b92a22070`  |
| 2919   | No file  | `f41b92a22070`  |
| 2907   | No file  | `f41b92a22070`  |
| 2900   | No file  | `f41b92a22070`  |
| 2891   | No file  | `f41b92a22070`  |
| 2882   | No file  | `f41b92a22070`  |
| 2872   | No file  | `f41b92a22070`  |
| 2863   | No file  | `f41b92a22070`  |
| 2855   | No file  | `f41b92a22070`  |
| 2849   | No file  | `f41b92a22070`  |
| 2844   | No file  | `f41b92a22070`  |
| 2834   | No file  | `f41b92a22070`  |
| 2825   | No file  | `f41b92a22070`  |
| 2819   | No file  | `f41b92a22070`  |
| 2811   | No file  | `f41b92a22070`  |
| 2803   | No file  | `f41b92a22070`  |
| 2794   | No file  | `f41b92a22070`  |
| 2783   | No file  | `f41b92a22070`  |
| 2774   | No file  | `f41b92a22070`  |
| 2765   | No file  | `f41b92a22070`  |
| 2756   | No file  | `f41b92a22070`  |
| 2750   | No file  | `f41b92a22070`  |
| 2743   | No file  | `f41b92a22070`  |
| 2736   | No file  | `f41b92a22070`  |
| 2726   | No file  | `f41b92a22070`  |
| 2717   | No file  | `f41b92a22070`  |
| 2709   | No file  | `f41b92a22070`  |
| 2703   | No file  | `f41b92a22070`  |
| 2695   | No file  | `f41b92a22070`  |
| 2684   | No file  | `f41b92a22070`  |
| 2672   | No file  | `f41b92a22070`  |
| 2665   | No file  | `f41b92a22070`  |
| 2657   | No file  | `f41b92a22070`  |
| 2649   | No file  | `f41b92a22070`  |
| 2644   | No file  | `f41b92a22070`  |
| 2637   | No file  | `f41b92a22070`  |
| 2629   | No file  | `f41b92a22070`  |
| 2619   | No file  | `f41b92a22070`  |
| 2612   | No file  | `f41b92a22070`  |
| 2606   | No file  | `f41b92a22070`  |
| 2602   | No file  | `f41b92a22070`  |
| 2601   | No file  | `f41b92a22070`  |
| 2592   | No file  | `f41b92a22070`  |
| 2583   | No file  | `f41b92a22070`  |
| 2575   | No file  | `f41b92a22070`  |
| 2567   | No file  | `f41b92a22070`  |
| 2560   | No file  | `f41b92a22070`  |
| 2553   | No file  | `f41b92a22070`  |
| 2545   | No file  | `f41b92a22070`  |
| 2538   | No file  | `f41b92a22070`  |
| 2529   | No file  | `f41b92a22070`  |
| 2519   | No file  | `f41b92a22070`  |
| 2513   | No file  | `f41b92a22070`  |
| 2510   | No file  | `f41b92a22070`  |
| 2507   | No file  | `f41b92a22070`  |
| 2503   | No file  | `f41b92a22070`  |
| 2498   | No file  | `f41b92a22070`  |
| 2492   | No file  | `f41b92a22070`  |
| 2487   | No file  | `f41b92a22070`  |
| 2480   | No file  | `f41b92a22070`  |
| 2474   | No file  | `f41b92a22070`  |
| 2468   | No file  | `f41b92a22070`  |
| 2460   | No file  | `f41b92a22070`  |
| 2453   | No file  | `f41b92a22070`  |
| 2444   | No file  | `f41b92a22070`  |
| 2438   | No file  | `f41b92a22070`  |
| 2434   | No file  | `f41b92a22070`  |
| 2429   | No file  | `f41b92a22070`  |
| 2421   | No file  | `f41b92a22070`  |
| 2414   | No file  | `f41b92a22070`  |
| 2407   | No file  | `f41b92a22070`  |
| 2401   | No file  | `f41b92a22070`  |
| 2397   | No file  | `f41b92a22070`  |
| 2393   | No file  | `f41b92a22070`  |
| 2384   | No file  | `f41b92a22070`  |
| 2378   | No file  | `f41b92a22070`  |
| 2372   | No file  | `f41b92a22070`  |
| 2358   | No file  | `f41b92a22070`  |
| 2352   | No file  | `f41b92a22070`  |
| 2347   | No file  | `f41b92a22070`  |
| 2343   | No file  | `f41b92a22070`  |
| 2335   | No file  | `f41b92a22070`  |
| 2327   | No file  | `f41b92a22070`  |
| 2324   | No file  | `f41b92a22070`  |
| 2319   | No file  | `f41b92a22070`  |
| 2313   | No file  | `f41b92a22070`  |
| 2308   | No file  | `f41b92a22070`  |
| 2302   | No file  | `f41b92a22070`  |
| 2295   | No file  | `f41b92a22070`  |
| 2290   | No file  | `f41b92a22070`  |
| 2284   | No file  | `f41b92a22070`  |
| 2276   | No file  | `f41b92a22070`  |
| 2269   | No file  | `f41b92a22070`  |
| 2259   | No file  | `f41b92a22070`  |
| 2250   | No file  | `f41b92a22070`  |
| 2243   | No file  | `f41b92a22070`  |
| 2235   | No file  | `f41b92a22070`  |
| 2229   | No file  | `f41b92a22070`  |
| 2224   | No file  | `f41b92a22070`  |
| 2218   | No file  | `f41b92a22070`  |
| 2215   | No file  | `f41b92a22070`  |
| 2207   | No file  | `f41b92a22070`  |
| 2203   | No file  | `f41b92a22070`  |
| 2196   | No file  | `f41b92a22070`  |
| 2192   | No file  | `f41b92a22070`  |
| 2189   | No file  | `f41b92a22070`  |
| 2183   | No file  | `f41b92a22070`  |
| 2179   | No file  | `f41b92a22070`  |
| 2171   | No file  | `f41b92a22070`  |
| 2163   | No file  | `f41b92a22070`  |
| 2156   | No file  | `f41b92a22070`  |
| 2151   | No file  | `f41b92a22070`  |
| 2147   | No file  | `f41b92a22070`  |
| 2142   | No file  | `f41b92a22070`  |
| 2138   | No file  | `f41b92a22070`  |
| 2134   | No file  | `f41b92a22070`  |
| 2130   | No file  | `f41b92a22070`  |
| 2122   | No file  | `f41b92a22070`  |
| 2107   | No file  | `f41b92a22070`  |
| 2098   | No file  | `f41b92a22070`  |
| 2089   | No file  | `f41b92a22070`  |
| 2081   | No file  | `f41b92a22070`  |
| 2073   | No file  | `f41b92a22070`  |
| 2067   | No file  | `f41b92a22070`  |
| 2063   | No file  | `f41b92a22070`  |
| 2059   | No file  | `f41b92a22070`  |
| 2052   | No file  | `f41b92a22070`  |
| 2044   | No file  | `f41b92a22070`  |
| 2039   | No file  | `f41b92a22070`  |
| 2032   | No file  | `f41b92a22070`  |
| 2025   | No file  | `f41b92a22070`  |
| 2011   | No file  | `f41b92a22070`  |
| 2005   | No file  | `f41b92a22070`  |
| 2000   | No file  | `f41b92a22070`  |
| 1996   | No file  | `f41b92a22070`  |
| 1991   | No file  | `f41b92a22070`  |
| 1985   | No file  | `f41b92a22070`  |
| 1980   | No file  | `f41b92a22070`  |
| 1969   | No file  | `f41b92a22070`  |
| 1964   | No file  | `f41b92a22070`  |
| 1958   | No file  | `f41b92a22070`  |
| 1950   | No file  | `f41b92a22070`  |
| 1945   | No file  | `f41b92a22070`  |
| 1937   | No file  | `f41b92a22070`  |
| 1933   | No file  | `f41b92a22070`  |
| 1927   | No file  | `f41b92a22070`  |
| 1921   | No file  | `f41b92a22070`  |
| 1914   | No file  | `f41b92a22070`  |
| 1908   | No file  | `f41b92a22070`  |
| 1897   | No file  | `f41b92a22070`  |
| 1892   | No file  | `f41b92a22070`  |
| 1886   | No file  | `f41b92a22070`  |
| 1881   | No file  | `f41b92a22070`  |
| 1871   | No file  | `f41b92a22070`  |
| 1866   | No file  | `f41b92a22070`  |
| 1862   | No file  | `f41b92a22070`  |
| 1854   | No file  | `f41b92a22070`  |
| 1846   | No file  | `f41b92a22070`  |
| 1838   | No file  | `f41b92a22070`  |
| 1832   | No file  | `f41b92a22070`  |
| 1826   | No file  | `f41b92a22070`  |
| 1822   | No file  | `f41b92a22070`  |
| 1818   | No file  | `f41b92a22070`  |
| 1804   | No file  | `f41b92a22070`  |
| 1794   | No file  | `f41b92a22070`  |
| 1790   | No file  | `f41b92a22070`  |
| 1784   | No file  | `f41b92a22070`  |
| 1774   | No file  | `f41b92a22070`  |
| 1771   | No file  | `f41b92a22070`  |
| 1762   | No file  | `f41b92a22070`  |
| 1759   | No file  | `f41b92a22070`  |
| 1754   | No file  | `f41b92a22070`  |
| 1749   | No file  | `f41b92a22070`  |
| 1743   | No file  | `f41b92a22070`  |
| 1737   | No file  | `f41b92a22070`  |
| 1731   | No file  | `f41b92a22070`  |
| 1725   | No file  | `f41b92a22070`  |
| 1717   | No file  | `f41b92a22070`  |
| 1710   | No file  | `f41b92a22070`  |
| 1704   | No file  | `f41b92a22070`  |
| 1698   | No file  | `f41b92a22070`  |
| 1690   | No file  | `f41b92a22070`  |
| 1685   | No file  | `f41b92a22070`  |
| 1680   | No file  | `f41b92a22070`  |
| 1674   | No file  | `f41b92a22070`  |
| 1668   | No file  | `f41b92a22070`  |
| 1659   | No file  | `f41b92a22070`  |
| 1649   | No file  | `f41b92a22070`  |
| 1642   | No file  | `f41b92a22070`  |
| 1636   | No file  | `f41b92a22070`  |
| 1628   | No file  | `f41b92a22070`  |
| 1622   | No file  | `f41b92a22070`  |
| 1614   | No file  | `f41b92a22070`  |
| 1608   | No file  | `f41b92a22070`  |
| 1602   | No file  | `f41b92a22070`  |
| 1598   | No file  | `f41b92a22070`  |
| 1594   | No file  | `f41b92a22070`  |
| 1590   | No file  | `f41b92a22070`  |
| 1587   | No file  | `f41b92a22070`  |
| 1584   | No file  | `f41b92a22070`  |
| 1579   | No file  | `f41b92a22070`  |
| 1572   | No file  | `f41b92a22070`  |
| 1565   | No file  | `f41b92a22070`  |
| 1559   | No file  | `f41b92a22070`  |
| 1554   | No file  | `f41b92a22070`  |
| 1547   | No file  | `f41b92a22070`  |
| 1537   | No file  | `f41b92a22070`  |
| 1529   | No file  | `f41b92a22070`  |
| 1524   | No file  | `f41b92a22070`  |
| 1519   | No file  | `f41b92a22070`  |
| 1509   | No file  | `f41b92a22070`  |
| 1506   | No file  | `f41b92a22070`  |
| 1504   | No file  | `f41b92a22070`  |
| 1500   | No file  | `f41b92a22070`  |
| 1493   | No file  | `f41b92a22070`  |
| 1489   | No file  | `f41b92a22070`  |
| 1485   | No file  | `f41b92a22070`  |
| 1481   | No file  | `f41b92a22070`  |
| 1474   | No file  | `f41b92a22070`  |
| 1466   | No file  | `f41b92a22070`  |
| 1462   | No file  | `f41b92a22070`  |
| 1459   | No file  | `f41b92a22070`  |
| 1453   | No file  | `f41b92a22070`  |
| 1450   | No file  | `f41b92a22070`  |
| 1445   | No file  | `f41b92a22070`  |
| 1439   | No file  | `f41b92a22070`  |
| 1433   | No file  | `f41b92a22070`  |
| 1430   | No file  | `f41b92a22070`  |
| 1426   | No file  | `f41b92a22070`  |
| 1421   | No file  | `f41b92a22070`  |
| 1417   | No file  | `f41b92a22070`  |
| 1416   | No file  | `f41b92a22070`  |
| 1409   | No file  | `f41b92a22070`  |
| 1405   | No file  | `f41b92a22070`  |
| 1401   | No file  | `f41b92a22070`  |
| 1396   | No file  | `f41b92a22070`  |
| 1391   | No file  | `f41b92a22070`  |
| 1390   | No file  | `f41b92a22070`  |
| 1386   | No file  | `f41b92a22070`  |
| 1381   | No file  | `f41b92a22070`  |
| 1379   | No file  | `f41b92a22070`  |
| 1372   | No file  | `f41b92a22070`  |
| 1366   | No file  | `f41b92a22070`  |
| 1364   | No file  | `f41b92a22070`  |
| 1363   | No file  | `f41b92a22070`  |
| 1360   | No file  | `f41b92a22070`  |
| 1358   | No file  | `f41b92a22070`  |
| 1355   | No file  | `f41b92a22070`  |
| 1351   | No file  | `f41b92a22070`  |
| 1348   | No file  | `f41b92a22070`  |
| 1346   | No file  | `f41b92a22070`  |
| 1341   | No file  | `f41b92a22070`  |
| 1340   | No file  | `f41b92a22070`  |
| 1338   | No file  | `f41b92a22070`  |
| 1335   | No file  | `f41b92a22070`  |
| 1333   | No file  | `f41b92a22070`  |
| 1329   | No file  | `f41b92a22070`  |
| 1327   | No file  | `f41b92a22070`  |
| 1324   | No file  | `f41b92a22070`  |
| 1321   | No file  | `f41b92a22070`  |
| 1319   | No file  | `f41b92a22070`  |
| 1318   | No file  | `f41b92a22070`  |
| 1316   | No file  | `f41b92a22070`  |
| 1313   | No file  | `f41b92a22070`  |
| 1311   | No file  | `f41b92a22070`  |
| 1309   | No file  | `f41b92a22070`  |
| 1304   | No file  | `f41b92a22070`  |
| 1292   | No file  | `f41b92a22070`  |
| 1286   | No file  | `f41b92a22070`  |
| 1280   | No file  | `f41b92a22070`  |
| 1276   | No file  | `f41b92a22070`  |
| 1267   | No file  | `f41b92a22070`  |
| 1261   | No file  | `f41b92a22070`  |
| 1256   | No file  | `f41b92a22070`  |
| 1250   | No file  | `f41b92a22070`  |
| 1246   | No file  | `f41b92a22070`  |
| 1239   | No file  | `f41b92a22070`  |
| 1230   | No file  | `f41b92a22070`  |
| 1226   | No file  | `f41b92a22070`  |
| 1220   | No file  | `f41b92a22070`  |
| 1217   | No file  | `f41b92a22070`  |
| 1211   | No file  | `f41b92a22070`  |
| 1210   | No file  | `f41b92a22070`  |
| 1208   | No file  | `f41b92a22070`  |
| 1203   | No file  | `f41b92a22070`  |
| 1197   | No file  | `f41b92a22070`  |
| 1194   | No file  | `f41b92a22070`  |
| 1192   | No file  | `f41b92a22070`  |
| 1187   | No file  | `f41b92a22070`  |
| 1183   | No file  | `f41b92a22070`  |
| 1177   | No file  | `f41b92a22070`  |
| 1173   | No file  | `f41b92a22070`  |
| 1167   | No file  | `f41b92a22070`  |
| 1164   | No file  | `f41b92a22070`  |
| 1156   | No file  | `f41b92a22070`  |
| 1149   | No file  | `f41b92a22070`  |
| 1144   | No file  | `f41b92a22070`  |
| 1137   | No file  | `f41b92a22070`  |
| 1132   | No file  | `f41b92a22070`  |
| 1127   | No file  | `f41b92a22070`  |
| 1122   | No file  | `f41b92a22070`  |
| 1118   | No file  | `f41b92a22070`  |
| 1114   | No file  | `f41b92a22070`  |
| 1109   | No file  | `f41b92a22070`  |
| 1102   | No file  | `f41b92a22070`  |
| 1096   | No file  | `f41b92a22070`  |
| 1088   | No file  | `f41b92a22070`  |
| 1081   | No file  | `f41b92a22070`  |
| 1076   | No file  | `f41b92a22070`  |
| 1069   | No file  | `f41b92a22070`  |
| 1064   | No file  | `f41b92a22070`  |
| 1058   | No file  | `f41b92a22070`  |
| 1051   | No file  | `f41b92a22070`  |
| 1044   | No file  | `f41b92a22070`  |
| 1036   | No file  | `f41b92a22070`  |
| 1026   | No file  | `f41b92a22070`  |
| 1016   | No file  | `f41b92a22070`  |
| 1009   | No file  | `f41b92a22070`  |
| 1005   | No file  | `f41b92a22070`  |
| 1000   | No file  | `f41b92a22070`  |
| 998    | No file  | `f41b92a22070`  |
| 990    | No file  | `f41b92a22070`  |
| 979    | No file  | `f41b92a22070`  |
| 972    | No file  | `f41b92a22070`  |
| 963    | No file  | `f41b92a22070`  |
| 955    | No file  | `f41b92a22070`  |
| 946    | No file  | `f41b92a22070`  |
| 938    | No file  | `f41b92a22070`  |
| 927    | No file  | `f41b92a22070`  |
| 911    | No file  | `f41b92a22070`  |
| 904    | No file  | `f41b92a22070`  |
| 899    | No file  | `f41b92a22070`  |
| 894    | No file  | `f41b92a22070`  |
| 885    | No file  | `f41b92a22070`  |
| 879    | No file  | `f41b92a22070`  |
| 872    | No file  | `f41b92a22070`  |
| 864    | No file  | `f41b92a22070`  |
| 855    | No file  | `f41b92a22070`  |
| 853    | No file  | `f41b92a22070`  |
| 845    | No file  | `f41b92a22070`  |
| 837    | No file  | `f41b92a22070`  |
| 829    | No file  | `f41b92a22070`  |
| 822    | No file  | `f41b92a22070`  |
| 814    | No file  | `f41b92a22070`  |
| 805    | No file  | `f41b92a22070`  |
| 794    | No file  | `f41b92a22070`  |
| 787    | No file  | `f41b92a22070`  |
| 780    | No file  | `f41b92a22070`  |
| 771    | No file  | `f41b92a22070`  |
| 760    | No file  | `f41b92a22070`  |
| 748    | No file  | `f41b92a22070`  |
| 741    | No file  | `f41b92a22070`  |
| 736    | No file  | `f41b92a22070`  |
| 731    | No file  | `f41b92a22070`  |
| 723    | No file  | `f41b92a22070`  |
| 711    | No file  | `f41b92a22070`  |
| 707    | No file  | `f41b92a22070`  |
| 697    | No file  | `f41b92a22070`  |
| 689    | No file  | `f41b92a22070`  |
| 683    | No file  | `f41b92a22070`  |
| 678    | No file  | `f41b92a22070`  |
| 670    | No file  | `f41b92a22070`  |
| 661    | No file  | `f41b92a22070`  |
| 656    | No file  | `f41b92a22070`  |
| 652    | No file  | `f41b92a22070`  |
| 643    | No file  | `f41b92a22070`  |
| 637    | No file  | `f41b92a22070`  |
| 630    | No file  | `f41b92a22070`  |
| 627    | No file  | `f41b92a22070`  |
| 621    | No file  | `f41b92a22070`  |
| 617    | No file  | `f41b92a22070`  |
| 615    | No file  | `f41b92a22070`  |
| 606    | No file  | `f41b92a22070`  |
| 599    | No file  | `f41b92a22070`  |
| 592    | No file  | `f41b92a22070`  |
| 586    | No file  | `f41b92a22070`  |
| 577    | No file  | `f41b92a22070`  |
| 569    | No file  | `f41b92a22070`  |
| 561    | No file  | `f41b92a22070`  |
| 554    | No file  | `f41b92a22070`  |
| 542    | No file  | `f41b92a22070`  |
| 532    | No file  | `f41b92a22070`  |
| 531    | No file  | `f41b92a22070`  |
| 526    | No file  | `f41b92a22070`  |
| 521    | No file  | `f41b92a22070`  |
| 517    | No file  | `f41b92a22070`  |
| 510    | No file  | `f41b92a22070`  |
| 508    | No file  | `f41b92a22070`  |
| 504    | No file  | `f41b92a22070`  |
| 497    | No file  | `f41b92a22070`  |
| 491    | No file  | `f41b92a22070`  |
| 485    | No file  | `f41b92a22070`  |
| 478    | No file  | `f41b92a22070`  |
| 472    | No file  | `f41b92a22070`  |
| 466    | No file  | `f41b92a22070`  |
| 457    | No file  | `f41b92a22070`  |
| 452    | No file  | `f41b92a22070`  |
| 449    | No file  | `f41b92a22070`  |
| 435    | No file  | `f41b92a22070`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                 | Field            | Notes                                                       |
| ------------------- | -------------------- | ---------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]              | magic            | ASCII `PABR`                                                |
| `+0x04`             | u16                  | unknown_04       | `1` (client 3482)                                           |
| `+0x06`             | u32                  | unknown_06       | `200` (client 3482)                                         |
| `+0x0A`             | u32                  | unknown_0a       | `10` (client 3482)                                          |
| `+0x0E`             | u32                  | unknown_item_key | Item ID: `1000383` [Event] Snowfall Crasher Seal (client 3482) |
| `+0x12`             | f32[3]               | unknown_12       | `180.0` three times (client 3482)                           |
| `+0x1E`             | u32                  | effect_ref       | String table index of an effect name; see Field Names       |
| `+0x22`             | u16                  | region_key       | `regioninfo.bss` region: `1176` Snowfall Crasher: Alpine Glide |
| `+0x24`             | f32[3]               | unknown_24       | A world position x, y, z in that region                     |
| `+0x30`             | bytes[8]             | unknown_30       | `D2 C4 AA 94 64 25 00 00` (client 3482)                     |
| `+0x38`             | u32                  | unknown_38       | `60` (client 3482)                                          |
| `+0x3C`             | u32                  | course_count     | Number of courses, `ToClient_SnowBoardCourseCount()`        |
| `+0x40`             | Course[course_count] | courses          | See Course; menu tab `ii` is course `ii`                    |
| `courses+0x00`      | u32                  | item_count       | Number of item effect entries                               |
| `courses+0x04`      | Item[item_count]     | items            | See Item                                                    |
| `items+0x00`        | u32                  | effect_count     | Number of checkpoint effect entries                         |
| `items+0x04`        | Effect[effect_count] | effects          | See Effect                                                  |
| `effects+0x00`      | String Table         | string_table     | See String Table                                            |
| `string_table+0x00` | u32                  | table_start      | Offset of the string table, where `effects` ends            |
| `string_table+0x04` | u32                  | zero             | Always `0`                                                  |

### Course (variable: 41 bytes + checkpoints)

| Offset  | Type                         | Field            | Notes                                                       |
| ------- | ---------------------------- | ---------------- | ----------------------------------------------------------- |
| `+0x00` | u32                          | course_key       | `getKeyRaw()`; `1` up in course order                       |
| `+0x04` | u32                          | name_ref         | String table index of the Korean course name, `getName()`   |
| `+0x08` | u8                           | mode             | `getMode()`: `0` Item, `1` Speed; see Course Modes          |
| `+0x09` | f32[3]                       | unknown_09       | A world position x, y, z; the same on every course (client 3482) |
| `+0x15` | f32                          | unknown_15       | `0.36` on every course (client 3482)                        |
| `+0x19` | f32                          | unknown_19       | `100.0` on every course (client 3482)                       |
| `+0x1D` | u32                          | unknown_1d       | `60` on the Item course, `0` on the others (client 3482)    |
| `+0x21` | u32                          | unknown_21       | `0`, `15000` and `5000` on courses `1` to `3` (client 3482) |
| `+0x25` | u32                          | checkpoint_count | Number of checkpoints, `getCheckPointCount()`               |
| `+0x29` | Checkpoint[checkpoint_count] | checkpoints      | See Checkpoint                                              |

### Checkpoint (50 bytes)

| Offset  | Type   | Field                 | Notes                                                                |
| ------- | ------ | --------------------- | -------------------------------------------------------------------- |
| `+0x00` | u32    | checkpoint_index      | `1` up in list order                                                 |
| `+0x04` | u32    | next_checkpoint_index | The checkpoint after this one; the last points back to `1`           |
| `+0x08` | f32[3] | unknown_08            | A world position x, y, z                                             |
| `+0x14` | f32    | unknown_14            | `-2.19` to `2.88` on client 3482, inside plus or minus pi            |
| `+0x18` | f32[6] | unknown_18            | Two sets of three; see Checkpoints                                   |
| `+0x30` | u8     | unknown_30            | `0` to `6`, below `effect_count`; see Checkpoints                    |
| `+0x31` | u8     | unknown_31            | `0` on the first checkpoint, `2` on the last, `1` between (client 3482) |

### Item (36 bytes)

| Offset  | Type   | Field             | Notes                                                    |
| ------- | ------ | ----------------- | -------------------------------------------------------- |
| `+0x00` | u32    | unknown_00        | `1` and `2` (client 3482)                                |
| `+0x04` | u32    | first_effect_ref  | String table index of an effect name                     |
| `+0x08` | u32    | second_effect_ref | String table index of an effect name                     |
| `+0x0C` | f32[3] | unknown_0c        | `0.0, 100.0, 0.0` on both entries (client 3482)          |
| `+0x18` | f32[3] | unknown_18        | `1.0` three times on both entries (client 3482)          |

### Effect (44 bytes)

| Offset  | Type   | Field             | Notes                                                        |
| ------- | ------ | ----------------- | ------------------------------------------------------------ |
| `+0x00` | u32    | first_effect_ref  | String table index of an effect name                         |
| `+0x04` | u32    | second_effect_ref | String table index of an effect name, or of the empty string |
| `+0x08` | f32[3] | unknown_08        | `0.0, -100.0, 0.0` on entries `1` to `5`, zeros on `0` and `6` (client 3482) |
| `+0x14` | f32[3] | unknown_14        | Zeros on every entry (client 3482)                           |
| `+0x20` | f32[3] | unknown_20        | `1.0` three times on every entry (client 3482)               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                 |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                     |
| `+0x04` | pstr[string_count] | strings      | UTF-8 effect names and UTF-16LE course names, in the order the fields first point to them |

## Course Modes

The client compares `getMode()` with `__eSnowBoardCourseMode_Item` and
`__eSnowBoardCourseMode_Speed`, which the Lua does not set. The menu shows
the item ranking for an Item course and the speed ranking for a Speed
course. On client 3482 course `1` (`스코어`, score) stores `0` and courses
`2` (`점프`, jump) and `3` (`스피드`, speed) store `1`, so `0` is Item and
`1` is Speed. The menu also picks a third title image for the Speed course
with key `3`.

## Checkpoints

The courses on client 3482:

| `course_key` | Name     | `mode` | `checkpoint_count` |
| ------------ | -------- | ------ | ------------------ |
| 1            | `스코어` | 0      | 2                  |
| 2            | `점프`   | 1      | 8                  |
| 3            | `스피드` | 1      | 35                 |

The last checkpoint of every course has the same position and
`unknown_18`, and `unknown_30` `6` and `unknown_31` `2`. Course `3`'s
checkpoints between the first and the last store `unknown_18` `650, 1000,
50, 4600, 1600, 50` and `unknown_30` `1`; course `2`'s store
`3700, 2500, 100` or `4300, 2500, 100` with zeros, and `unknown_30` `4`
or `5` to match.

`unknown_30` is one of the values `0` to `6`, and the Effect list has 7
entries: entry `0` and entry `6` name `fN_Event_Object_Start_Track_Aura_01A`,
entries `1` to `5` `fN_Event_Object_Check_Point_01A` (with `_01B` as its
second effect) to `_01F`. The first checkpoints store `0`, the last ones
`6`.

## Field Names

The file is not in client 1784, and no sheet of a private server's
`DataSheets.bexcel` on that client has `Snowboard` in its name.
`course_key`, `name_ref`, `mode` and `checkpoint_count` follow the Lua
getters (`getKeyRaw`, `getName`, `getMode`, `getCheckPointCount`): the
menu's tab count is the course count, and the three tabs carry the three
names. `next_checkpoint_index` holds the next checkpoint's index on every
checkpoint, and the last one's points back to `1`. `region_key` is the
`regioninfo.bss` key whose LOC type 17 name is Snowfall Crasher: Alpine
Glide.

Every string an `*_effect_ref` points to is the name of an
`effectbin/<name>.pae` file (`effectbin/fco_new_snowboard_item_01a.pae`,
`fn_event_object_check_point_01a.pae`). The strings sit in the order of
the first field that points to each, so string `0`,
`fN_Event_Object_Ghost_Location_01A`, belongs to the head's only string
index before the course names, `effect_ref` at `+0x1E` (value `0`). The
item effects are `fCO_New_SnowBoard_Item_01A` with `fCO_NEW_SnowBoard_Item_02A`
and `_01B` with `_02B`.

## Notes

- `snowboard.bss` has its own handler (`_bss/snowboard/`): one row per
  checkpoint with its course key, the Korean course name, the mode name
  and the checkpoint and next checkpoint index.
- [`snowboardcourseinfo.bss`](snowboardcourseinfo_bss.md) holds the
  colours of the snowboard course region map.

## Open Questions

### What the Checkpoint Values Are

`unknown_18` reads as two box sizes and `unknown_14` as an angle, and
`unknown_30` fits an index into the Effect list (the start and finish
effect on the first and last checkpoint), with `unknown_31` the kind of
checkpoint (start, between, finish). No Lua getter returns these values,
so the names stay open.

### What the Head Values Are

The head holds the region, an item (`1000383` [Event] Snowfall Crasher
Seal, maybe the course coin or reward), three `180.0` values, a world
position and the values `1`, `200`, `10` and `60`. The HUD and menu call
`ToClient_SnowBoardCoinCount()`, `ToClient_GetSnowBoardRankMax()` and
`ToClient_GetPossibleSnowBoardRecord()`, which may read some of them;
nothing in the Lua ties a call to a field.
