# `rosewarrevivepositionstaticstatus.bss` Format

## Purpose

Where Rose War players revive: two counted groups after the PABR magic.
The first holds the team revive points by `respawn_position_type`, the
second the sanctum revive points by fierce battle key. Each point is a list
of x, y, z positions and an f32. On client 3474 the file has 6 team points
(types `1` to `3` near Grána, `4` to `6` near O'draxxia) and 14 sanctum
points, one for each linked sanctum.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records                                     | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ------------------------------------------- | --------- |
| 1      | 2545 and later | 3483    | `rosewarrevivepositionstaticstatus.bss` | 674   | 38 Position, 6 Team Point, 14 Sanctum Point | 12        |

| Layout | File                                    | Known         | Unknown      |
| ------ | --------------------------------------- | ------------- | ------------ |
| 1      | `rosewarrevivepositionstaticstatus.bss` | 594 B (88.1%) | 80 B (11.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `35c2ded82250`  |
| 3482   | Layout 1 | `35c2ded82250`  |
| 3474   | Layout 1 | `35c2ded82250`  |
| 3473   | Layout 1 | `35c2ded82250`  |
| 3464   | Layout 1 | `35c2ded82250`  |
| 3458   | Layout 1 | `35c2ded82250`  |
| 3454   | Layout 1 | `35c2ded82250`  |
| 3444   | Layout 1 | `35c2ded82250`  |
| 3435   | Layout 1 | `35c2ded82250`  |
| 3426   | Layout 1 | `35c2ded82250`  |
| 3418   | Layout 1 | `35c2ded82250`  |
| 3412   | Layout 1 | `35c2ded82250`  |
| 3402   | Layout 1 | `35c2ded82250`  |
| 3396   | Layout 1 | `35c2ded82250`  |
| 3387   | Layout 1 | `35c2ded82250`  |
| 3381   | Layout 1 | `35c2ded82250`  |
| 3373   | Layout 1 | `35c2ded82250`  |
| 3364   | Layout 1 | `35c2ded82250`  |
| 3356   | Layout 1 | `35c2ded82250`  |
| 3349   | Layout 1 | `35c2ded82250`  |
| 3342   | Layout 1 | `35c2ded82250`  |
| 3335   | Layout 1 | `35c2ded82250`  |
| 3326   | Layout 1 | `35c2ded82250`  |
| 3321   | Layout 1 | `35c2ded82250`  |
| 3314   | Layout 1 | `35c2ded82250`  |
| 3303   | Layout 1 | `35c2ded82250`  |
| 3302   | Layout 1 | `35c2ded82250`  |
| 3293   | Layout 1 | `35c2ded82250`  |
| 3283   | Layout 1 | `35c2ded82250`  |
| 3275   | Layout 1 | `35c2ded82250`  |
| 3267   | Layout 1 | `35c2ded82250`  |
| 3258   | Layout 1 | `35c2ded82250`  |
| 3251   | Layout 1 | `35c2ded82250`  |
| 3242   | Layout 1 | `35c2ded82250`  |
| 3235   | Layout 1 | `35c2ded82250`  |
| 3229   | Layout 1 | `35c2ded82250`  |
| 3212   | Layout 1 | `35c2ded82250`  |
| 3203   | Layout 1 | `35c2ded82250`  |
| 3193   | Layout 1 | `35c2ded82250`  |
| 3186   | Layout 1 | `35c2ded82250`  |
| 3177   | Layout 1 | `35c2ded82250`  |
| 3169   | Layout 1 | `35c2ded82250`  |
| 3158   | Layout 1 | `35c2ded82250`  |
| 3151   | Layout 1 | `35c2ded82250`  |
| 3144   | Layout 1 | `35c2ded82250`  |
| 3133   | Layout 1 | `35c2ded82250`  |
| 3125   | Layout 1 | `35c2ded82250`  |
| 3118   | Layout 1 | `35c2ded82250`  |
| 3111   | Layout 1 | `35c2ded82250`  |
| 3103   | Layout 1 | `35c2ded82250`  |
| 3095   | Layout 1 | `35c2ded82250`  |
| 3086   | Layout 1 | `35c2ded82250`  |
| 3072   | Layout 1 | `35c2ded82250`  |
| 3062   | Layout 1 | `35c2ded82250`  |
| 3052   | Layout 1 | `35c2ded82250`  |
| 3045   | Layout 1 | `35c2ded82250`  |
| 3037   | Layout 1 | `35c2ded82250`  |
| 3030   | Layout 1 | `35c2ded82250`  |
| 3021   | Layout 1 | `35c2ded82250`  |
| 3012   | Layout 1 | `35c2ded82250`  |
| 3002   | Layout 1 | `35c2ded82250`  |
| 2995   | Layout 1 | `35c2ded82250`  |
| 2987   | Layout 1 | `35c2ded82250`  |
| 2978   | Layout 1 | `35c2ded82250`  |
| 2970   | Layout 1 | `35c2ded82250`  |
| 2959   | Layout 1 | `35c2ded82250`  |
| 2951   | Layout 1 | `35c2ded82250`  |
| 2942   | Layout 1 | `35c2ded82250`  |
| 2935   | Layout 1 | `35c2ded82250`  |
| 2932   | Layout 1 | `35c2ded82250`  |
| 2923   | Layout 1 | `35c2ded82250`  |
| 2919   | Layout 1 | `35c2ded82250`  |
| 2907   | Layout 1 | `35c2ded82250`  |
| 2900   | Layout 1 | `35c2ded82250`  |
| 2891   | Layout 1 | `35c2ded82250`  |
| 2882   | Layout 1 | `35c2ded82250`  |
| 2872   | Layout 1 | `35c2ded82250`  |
| 2863   | Layout 1 | `35c2ded82250`  |
| 2855   | Layout 1 | `35c2ded82250`  |
| 2849   | Layout 1 | `35c2ded82250`  |
| 2844   | Layout 1 | `35c2ded82250`  |
| 2834   | Layout 1 | `35c2ded82250`  |
| 2825   | Layout 1 | `35c2ded82250`  |
| 2819   | Layout 1 | `35c2ded82250`  |
| 2811   | Layout 1 | `35c2ded82250`  |
| 2803   | Layout 1 | `35c2ded82250`  |
| 2794   | Layout 1 | `35c2ded82250`  |
| 2783   | Layout 1 | `35c2ded82250`  |
| 2774   | Layout 1 | `35c2ded82250`  |
| 2765   | Layout 1 | `35c2ded82250`  |
| 2756   | Layout 1 | `35c2ded82250`  |
| 2750   | Layout 1 | `35c2ded82250`  |
| 2743   | Layout 1 | `35c2ded82250`  |
| 2736   | Layout 1 | `35c2ded82250`  |
| 2726   | Layout 1 | `35c2ded82250`  |
| 2717   | Layout 1 | `35c2ded82250`  |
| 2709   | Layout 1 | `35c2ded82250`  |
| 2703   | Layout 1 | `35c2ded82250`  |
| 2695   | Layout 1 | `35c2ded82250`  |
| 2684   | Layout 1 | `35c2ded82250`  |
| 2672   | Layout 1 | `35c2ded82250`  |
| 2665   | Layout 1 | `35c2ded82250`  |
| 2657   | Layout 1 | `35c2ded82250`  |
| 2649   | Layout 1 | `35c2ded82250`  |
| 2644   | Layout 1 | `35c2ded82250`  |
| 2637   | Layout 1 | `35c2ded82250`  |
| 2629   | Layout 1 | `35c2ded82250`  |
| 2619   | Layout 1 | `35c2ded82250`  |
| 2612   | Layout 1 | `35c2ded82250`  |
| 2606   | Layout 1 | `35c2ded82250`  |
| 2602   | Layout 1 | `35c2ded82250`  |
| 2601   | Layout 1 | `35c2ded82250`  |
| 2592   | Layout 1 | `35c2ded82250`  |
| 2583   | Layout 1 | `35c2ded82250`  |
| 2575   | Layout 1 | `35c2ded82250`  |
| 2567   | Layout 1 | `35c2ded82250`  |
| 2560   | Layout 1 | `35c2ded82250`  |
| 2553   | Layout 1 | `35c2ded82250`  |
| 2545   | Layout 1 | `35c2ded82250`  |
| 2538   | No file  | `35c2ded82250`  |
| 2529   | No file  | `35c2ded82250`  |
| 2519   | No file  | `35c2ded82250`  |
| 2513   | No file  | `35c2ded82250`  |
| 2510   | No file  | `35c2ded82250`  |
| 2507   | No file  | `35c2ded82250`  |
| 2503   | No file  | `35c2ded82250`  |
| 2498   | No file  | `35c2ded82250`  |
| 2492   | No file  | `35c2ded82250`  |
| 2487   | No file  | `35c2ded82250`  |
| 2480   | No file  | `35c2ded82250`  |
| 2474   | No file  | `35c2ded82250`  |
| 2468   | No file  | `35c2ded82250`  |
| 2460   | No file  | `35c2ded82250`  |
| 2453   | No file  | `35c2ded82250`  |
| 2444   | No file  | `35c2ded82250`  |
| 2438   | No file  | `35c2ded82250`  |
| 2434   | No file  | `35c2ded82250`  |
| 2429   | No file  | `35c2ded82250`  |
| 2421   | No file  | `35c2ded82250`  |
| 2414   | No file  | `35c2ded82250`  |
| 2407   | No file  | `35c2ded82250`  |
| 2401   | No file  | `35c2ded82250`  |
| 2397   | No file  | `35c2ded82250`  |
| 2393   | No file  | `35c2ded82250`  |
| 2384   | No file  | `35c2ded82250`  |
| 2378   | No file  | `35c2ded82250`  |
| 2372   | No file  | `35c2ded82250`  |
| 2358   | No file  | `35c2ded82250`  |
| 2352   | No file  | `35c2ded82250`  |
| 2347   | No file  | `35c2ded82250`  |
| 2343   | No file  | `35c2ded82250`  |
| 2335   | No file  | `35c2ded82250`  |
| 2327   | No file  | `35c2ded82250`  |
| 2324   | No file  | `35c2ded82250`  |
| 2319   | No file  | `35c2ded82250`  |
| 2313   | No file  | `35c2ded82250`  |
| 2308   | No file  | `35c2ded82250`  |
| 2302   | No file  | `35c2ded82250`  |
| 2295   | No file  | `35c2ded82250`  |
| 2290   | No file  | `35c2ded82250`  |
| 2284   | No file  | `35c2ded82250`  |
| 2276   | No file  | `35c2ded82250`  |
| 2269   | No file  | `35c2ded82250`  |
| 2259   | No file  | `35c2ded82250`  |
| 2250   | No file  | `35c2ded82250`  |
| 2243   | No file  | `35c2ded82250`  |
| 2235   | No file  | `35c2ded82250`  |
| 2229   | No file  | `35c2ded82250`  |
| 2224   | No file  | `35c2ded82250`  |
| 2218   | No file  | `35c2ded82250`  |
| 2215   | No file  | `35c2ded82250`  |
| 2207   | No file  | `35c2ded82250`  |
| 2203   | No file  | `35c2ded82250`  |
| 2196   | No file  | `35c2ded82250`  |
| 2192   | No file  | `35c2ded82250`  |
| 2189   | No file  | `35c2ded82250`  |
| 2183   | No file  | `35c2ded82250`  |
| 2179   | No file  | `35c2ded82250`  |
| 2171   | No file  | `35c2ded82250`  |
| 2163   | No file  | `35c2ded82250`  |
| 2156   | No file  | `35c2ded82250`  |
| 2151   | No file  | `35c2ded82250`  |
| 2147   | No file  | `35c2ded82250`  |
| 2142   | No file  | `35c2ded82250`  |
| 2138   | No file  | `35c2ded82250`  |
| 2134   | No file  | `35c2ded82250`  |
| 2130   | No file  | `35c2ded82250`  |
| 2122   | No file  | `35c2ded82250`  |
| 2107   | No file  | `35c2ded82250`  |
| 2098   | No file  | `35c2ded82250`  |
| 2089   | No file  | `35c2ded82250`  |
| 2081   | No file  | `35c2ded82250`  |
| 2073   | No file  | `35c2ded82250`  |
| 2067   | No file  | `35c2ded82250`  |
| 2063   | No file  | `35c2ded82250`  |
| 2059   | No file  | `35c2ded82250`  |
| 2052   | No file  | `35c2ded82250`  |
| 2044   | No file  | `35c2ded82250`  |
| 2039   | No file  | `35c2ded82250`  |
| 2032   | No file  | `35c2ded82250`  |
| 2025   | No file  | `35c2ded82250`  |
| 2011   | No file  | `35c2ded82250`  |
| 2005   | No file  | `35c2ded82250`  |
| 2000   | No file  | `35c2ded82250`  |
| 1996   | No file  | `35c2ded82250`  |
| 1991   | No file  | `35c2ded82250`  |
| 1985   | No file  | `35c2ded82250`  |
| 1980   | No file  | `35c2ded82250`  |
| 1969   | No file  | `35c2ded82250`  |
| 1964   | No file  | `35c2ded82250`  |
| 1958   | No file  | `35c2ded82250`  |
| 1950   | No file  | `35c2ded82250`  |
| 1945   | No file  | `35c2ded82250`  |
| 1937   | No file  | `35c2ded82250`  |
| 1933   | No file  | `35c2ded82250`  |
| 1927   | No file  | `35c2ded82250`  |
| 1921   | No file  | `35c2ded82250`  |
| 1914   | No file  | `35c2ded82250`  |
| 1908   | No file  | `35c2ded82250`  |
| 1897   | No file  | `35c2ded82250`  |
| 1892   | No file  | `35c2ded82250`  |
| 1886   | No file  | `35c2ded82250`  |
| 1881   | No file  | `35c2ded82250`  |
| 1871   | No file  | `35c2ded82250`  |
| 1866   | No file  | `35c2ded82250`  |
| 1862   | No file  | `35c2ded82250`  |
| 1854   | No file  | `35c2ded82250`  |
| 1846   | No file  | `35c2ded82250`  |
| 1838   | No file  | `35c2ded82250`  |
| 1832   | No file  | `35c2ded82250`  |
| 1826   | No file  | `35c2ded82250`  |
| 1822   | No file  | `35c2ded82250`  |
| 1818   | No file  | `35c2ded82250`  |
| 1804   | No file  | `35c2ded82250`  |
| 1794   | No file  | `35c2ded82250`  |
| 1790   | No file  | `35c2ded82250`  |
| 1784   | No file  | `35c2ded82250`  |
| 1774   | No file  | `35c2ded82250`  |
| 1771   | No file  | `35c2ded82250`  |
| 1762   | No file  | `35c2ded82250`  |
| 1759   | No file  | `35c2ded82250`  |
| 1754   | No file  | `35c2ded82250`  |
| 1749   | No file  | `35c2ded82250`  |
| 1743   | No file  | `35c2ded82250`  |
| 1737   | No file  | `35c2ded82250`  |
| 1731   | No file  | `35c2ded82250`  |
| 1725   | No file  | `35c2ded82250`  |
| 1717   | No file  | `35c2ded82250`  |
| 1710   | No file  | `35c2ded82250`  |
| 1704   | No file  | `35c2ded82250`  |
| 1698   | No file  | `35c2ded82250`  |
| 1690   | No file  | `35c2ded82250`  |
| 1685   | No file  | `35c2ded82250`  |
| 1680   | No file  | `35c2ded82250`  |
| 1674   | No file  | `35c2ded82250`  |
| 1668   | No file  | `35c2ded82250`  |
| 1659   | No file  | `35c2ded82250`  |
| 1649   | No file  | `35c2ded82250`  |
| 1642   | No file  | `35c2ded82250`  |
| 1636   | No file  | `35c2ded82250`  |
| 1628   | No file  | `35c2ded82250`  |
| 1622   | No file  | `35c2ded82250`  |
| 1614   | No file  | `35c2ded82250`  |
| 1608   | No file  | `35c2ded82250`  |
| 1602   | No file  | `35c2ded82250`  |
| 1598   | No file  | `35c2ded82250`  |
| 1594   | No file  | `35c2ded82250`  |
| 1590   | No file  | `35c2ded82250`  |
| 1587   | No file  | `35c2ded82250`  |
| 1584   | No file  | `35c2ded82250`  |
| 1579   | No file  | `35c2ded82250`  |
| 1572   | No file  | `35c2ded82250`  |
| 1565   | No file  | `35c2ded82250`  |
| 1559   | No file  | `35c2ded82250`  |
| 1554   | No file  | `35c2ded82250`  |
| 1547   | No file  | `35c2ded82250`  |
| 1537   | No file  | `35c2ded82250`  |
| 1529   | No file  | `35c2ded82250`  |
| 1524   | No file  | `35c2ded82250`  |
| 1519   | No file  | `35c2ded82250`  |
| 1509   | No file  | `35c2ded82250`  |
| 1506   | No file  | `35c2ded82250`  |
| 1504   | No file  | `35c2ded82250`  |
| 1500   | No file  | `35c2ded82250`  |
| 1493   | No file  | `35c2ded82250`  |
| 1489   | No file  | `35c2ded82250`  |
| 1485   | No file  | `35c2ded82250`  |
| 1481   | No file  | `35c2ded82250`  |
| 1474   | No file  | `35c2ded82250`  |
| 1466   | No file  | `35c2ded82250`  |
| 1462   | No file  | `35c2ded82250`  |
| 1459   | No file  | `35c2ded82250`  |
| 1453   | No file  | `35c2ded82250`  |
| 1450   | No file  | `35c2ded82250`  |
| 1445   | No file  | `35c2ded82250`  |
| 1439   | No file  | `35c2ded82250`  |
| 1433   | No file  | `35c2ded82250`  |
| 1430   | No file  | `35c2ded82250`  |
| 1426   | No file  | `35c2ded82250`  |
| 1421   | No file  | `35c2ded82250`  |
| 1417   | No file  | `35c2ded82250`  |
| 1416   | No file  | `35c2ded82250`  |
| 1409   | No file  | `35c2ded82250`  |
| 1405   | No file  | `35c2ded82250`  |
| 1401   | No file  | `35c2ded82250`  |
| 1396   | No file  | `35c2ded82250`  |
| 1391   | No file  | `35c2ded82250`  |
| 1390   | No file  | `35c2ded82250`  |
| 1386   | No file  | `35c2ded82250`  |
| 1381   | No file  | `35c2ded82250`  |
| 1379   | No file  | `35c2ded82250`  |
| 1372   | No file  | `35c2ded82250`  |
| 1366   | No file  | `35c2ded82250`  |
| 1364   | No file  | `35c2ded82250`  |
| 1363   | No file  | `35c2ded82250`  |
| 1360   | No file  | `35c2ded82250`  |
| 1358   | No file  | `35c2ded82250`  |
| 1355   | No file  | `35c2ded82250`  |
| 1351   | No file  | `35c2ded82250`  |
| 1348   | No file  | `35c2ded82250`  |
| 1346   | No file  | `35c2ded82250`  |
| 1341   | No file  | `35c2ded82250`  |
| 1340   | No file  | `35c2ded82250`  |
| 1338   | No file  | `35c2ded82250`  |
| 1335   | No file  | `35c2ded82250`  |
| 1333   | No file  | `35c2ded82250`  |
| 1329   | No file  | `35c2ded82250`  |
| 1327   | No file  | `35c2ded82250`  |
| 1324   | No file  | `35c2ded82250`  |
| 1321   | No file  | `35c2ded82250`  |
| 1319   | No file  | `35c2ded82250`  |
| 1318   | No file  | `35c2ded82250`  |
| 1316   | No file  | `35c2ded82250`  |
| 1313   | No file  | `35c2ded82250`  |
| 1311   | No file  | `35c2ded82250`  |
| 1309   | No file  | `35c2ded82250`  |
| 1304   | No file  | `35c2ded82250`  |
| 1292   | No file  | `35c2ded82250`  |
| 1286   | No file  | `35c2ded82250`  |
| 1280   | No file  | `35c2ded82250`  |
| 1276   | No file  | `35c2ded82250`  |
| 1267   | No file  | `35c2ded82250`  |
| 1261   | No file  | `35c2ded82250`  |
| 1256   | No file  | `35c2ded82250`  |
| 1250   | No file  | `35c2ded82250`  |
| 1246   | No file  | `35c2ded82250`  |
| 1239   | No file  | `35c2ded82250`  |
| 1230   | No file  | `35c2ded82250`  |
| 1226   | No file  | `35c2ded82250`  |
| 1220   | No file  | `35c2ded82250`  |
| 1217   | No file  | `35c2ded82250`  |
| 1211   | No file  | `35c2ded82250`  |
| 1210   | No file  | `35c2ded82250`  |
| 1208   | No file  | `35c2ded82250`  |
| 1203   | No file  | `35c2ded82250`  |
| 1197   | No file  | `35c2ded82250`  |
| 1194   | No file  | `35c2ded82250`  |
| 1192   | No file  | `35c2ded82250`  |
| 1187   | No file  | `35c2ded82250`  |
| 1183   | No file  | `35c2ded82250`  |
| 1177   | No file  | `35c2ded82250`  |
| 1173   | No file  | `35c2ded82250`  |
| 1167   | No file  | `35c2ded82250`  |
| 1164   | No file  | `35c2ded82250`  |
| 1156   | No file  | `35c2ded82250`  |
| 1149   | No file  | `35c2ded82250`  |
| 1144   | No file  | `35c2ded82250`  |
| 1137   | No file  | `35c2ded82250`  |
| 1132   | No file  | `35c2ded82250`  |
| 1127   | No file  | `35c2ded82250`  |
| 1122   | No file  | `35c2ded82250`  |
| 1118   | No file  | `35c2ded82250`  |
| 1114   | No file  | `35c2ded82250`  |
| 1109   | No file  | `35c2ded82250`  |
| 1102   | No file  | `35c2ded82250`  |
| 1096   | No file  | `35c2ded82250`  |
| 1088   | No file  | `35c2ded82250`  |
| 1081   | No file  | `35c2ded82250`  |
| 1076   | No file  | `35c2ded82250`  |
| 1069   | No file  | `35c2ded82250`  |
| 1064   | No file  | `35c2ded82250`  |
| 1058   | No file  | `35c2ded82250`  |
| 1051   | No file  | `35c2ded82250`  |
| 1044   | No file  | `35c2ded82250`  |
| 1036   | No file  | `35c2ded82250`  |
| 1026   | No file  | `35c2ded82250`  |
| 1016   | No file  | `35c2ded82250`  |
| 1009   | No file  | `35c2ded82250`  |
| 1005   | No file  | `35c2ded82250`  |
| 1000   | No file  | `35c2ded82250`  |
| 998    | No file  | `35c2ded82250`  |
| 990    | No file  | `35c2ded82250`  |
| 979    | No file  | `35c2ded82250`  |
| 972    | No file  | `35c2ded82250`  |
| 963    | No file  | `35c2ded82250`  |
| 955    | No file  | `35c2ded82250`  |
| 946    | No file  | `35c2ded82250`  |
| 938    | No file  | `35c2ded82250`  |
| 927    | No file  | `35c2ded82250`  |
| 911    | No file  | `35c2ded82250`  |
| 904    | No file  | `35c2ded82250`  |
| 899    | No file  | `35c2ded82250`  |
| 894    | No file  | `35c2ded82250`  |
| 885    | No file  | `35c2ded82250`  |
| 879    | No file  | `35c2ded82250`  |
| 872    | No file  | `35c2ded82250`  |
| 864    | No file  | `35c2ded82250`  |
| 855    | No file  | `35c2ded82250`  |
| 853    | No file  | `35c2ded82250`  |
| 845    | No file  | `35c2ded82250`  |
| 837    | No file  | `35c2ded82250`  |
| 829    | No file  | `35c2ded82250`  |
| 822    | No file  | `35c2ded82250`  |
| 814    | No file  | `35c2ded82250`  |
| 805    | No file  | `35c2ded82250`  |
| 794    | No file  | `35c2ded82250`  |
| 787    | No file  | `35c2ded82250`  |
| 780    | No file  | `35c2ded82250`  |
| 771    | No file  | `35c2ded82250`  |
| 760    | No file  | `35c2ded82250`  |
| 748    | No file  | `35c2ded82250`  |
| 741    | No file  | `35c2ded82250`  |
| 736    | No file  | `35c2ded82250`  |
| 731    | No file  | `35c2ded82250`  |
| 723    | No file  | `35c2ded82250`  |
| 711    | No file  | `35c2ded82250`  |
| 707    | No file  | `35c2ded82250`  |
| 697    | No file  | `35c2ded82250`  |
| 689    | No file  | `35c2ded82250`  |
| 683    | No file  | `35c2ded82250`  |
| 678    | No file  | `35c2ded82250`  |
| 670    | No file  | `35c2ded82250`  |
| 661    | No file  | `35c2ded82250`  |
| 656    | No file  | `35c2ded82250`  |
| 652    | No file  | `35c2ded82250`  |
| 643    | No file  | `35c2ded82250`  |
| 637    | No file  | `35c2ded82250`  |
| 630    | No file  | `35c2ded82250`  |
| 627    | No file  | `35c2ded82250`  |
| 621    | No file  | `35c2ded82250`  |
| 617    | No file  | `35c2ded82250`  |
| 615    | No file  | `35c2ded82250`  |
| 606    | No file  | `35c2ded82250`  |
| 599    | No file  | `35c2ded82250`  |
| 592    | No file  | `35c2ded82250`  |
| 586    | No file  | `35c2ded82250`  |
| 577    | No file  | `35c2ded82250`  |
| 569    | No file  | `35c2ded82250`  |
| 561    | No file  | `35c2ded82250`  |
| 554    | No file  | `35c2ded82250`  |
| 542    | No file  | `35c2ded82250`  |
| 532    | No file  | `35c2ded82250`  |
| 531    | No file  | `35c2ded82250`  |
| 526    | No file  | `35c2ded82250`  |
| 521    | No file  | `35c2ded82250`  |
| 517    | No file  | `35c2ded82250`  |
| 510    | No file  | `35c2ded82250`  |
| 508    | No file  | `35c2ded82250`  |
| 504    | No file  | `35c2ded82250`  |
| 497    | No file  | `35c2ded82250`  |
| 491    | No file  | `35c2ded82250`  |
| 485    | No file  | `35c2ded82250`  |
| 478    | No file  | `35c2ded82250`  |
| 472    | No file  | `35c2ded82250`  |
| 466    | No file  | `35c2ded82250`  |
| 457    | No file  | `35c2ded82250`  |
| 452    | No file  | `35c2ded82250`  |
| 449    | No file  | `35c2ded82250`  |
| 435    | No file  | `35c2ded82250`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset               | Type                          | Field              | Notes                                         |
| -------------------- | ----------------------------- | ------------------ | --------------------------------------------- |
| `+0x00`              | char[4]                       | magic              | ASCII `PABR`                                  |
| `+0x04`              | u32                           | team_point_count   | Number of team points                         |
| `+0x08`              | Team Point[team_point_count]  | team_points        | See Team Point                                |
| `team_points+0x00`   | u32                           | sanctum_point_count| Number of sanctum points                      |
| `team_points+0x04`   | Sanctum Point[sanctum_point_count] | sanctum_points | See Sanctum Point                             |
| `sanctum_points+0x00`| String Table                  | string_table       | See String Table                              |
| `string_table+0x00`  | u32                           | table_start        | Offset of the string table, where `sanctum_points` ends |
| `string_table+0x04`  | u32                           | zero               | Always `0`                                    |

### Team Point (variable: 9 bytes + positions)

| Offset            | Type                     | Field                 | Notes                                                       |
| ----------------- | ------------------------ | --------------------- | ----------------------------------------------------------- |
| `+0x00`           | u8                       | respawn_position_type | `1` to `6` on client 3474; see Revive Point Types           |
| `+0x01`           | u32                      | position_count        | Number of positions, `1` or `3`                             |
| `+0x05`           | Position[position_count] | positions             | See Position                                                |
| `positions+0x00`  | f32                      | unknown_positions_00  | `500` on every team point                                   |

### Sanctum Point (variable: 10 bytes + positions)

| Offset            | Type                     | Field                 | Notes                                                       |
| ----------------- | ------------------------ | --------------------- | ----------------------------------------------------------- |
| `+0x00`           | u16                      | fierce_battle_key     | Sanctum key of the monster table                            |
| `+0x02`           | u32                      | position_count        | Number of positions, `2` on client 3474                     |
| `+0x06`           | Position[position_count] | positions             | See Position                                                |
| `positions+0x00`  | f32                      | unknown_positions_00  | `500`, `400` on sanctums `12` and `14` (client 3474)        |

### Position (12 bytes)

| Offset  | Type | Field | Notes                         |
| ------- | ---- | ----- | ----------------------------- |
| `+0x00` | f32  | x     | World x                       |
| `+0x04` | f32  | y     | Height                        |
| `+0x08` | f32  | z     | World z                       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Revive Point Types

The client Lua names seven `__eRoseWarRespawnPositionType_*` values without
their numbers: `Kamasylvia_Plaza`, `Kamasylvia_InsideCastleGate`,
`Kamasylvia_OuterCastleGate`, the same three for `Odyllita`, and
`FierceBattle`. The six team points split by place (client 3474):

| `respawn_position_type` | Positions | Area (x, z)                         |
| ----------------------- | --------- | ----------------------------------- |
| `1`, `2`                | 1 each    | Near Grána (x about -550,000)       |
| `3`                     | 3         | Near Grána                          |
| `4`, `5`                | 1 each    | Near O'draxxia (x about -295,000)   |
| `6`                     | 3         | Near O'draxxia                      |

Which of plaza, inner gate and outer gate each of `1` to `3` is stays open.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. `respawn_position_type`
follows the Lua enum, whose six team names match the six team points and
whose `FierceBattle` value matches the second group; the Lua error
`eErrNoSelectRoseWarRevivePositionType` names the revive position type.
`fierce_battle_key` matches the keys of
[`rosewarfiercebattlemonsterstaticstatus.bss`](rosewarfiercebattlemonsterstaticstatus_bss.md):
on client 3474 the sanctum points are `1` to `7` and `11` to `17`, the
sanctums [`rosewarfiercebattlenodestaticstatus.bss`](rosewarfiercebattlenodestaticstatus_bss.md)
links. The positions read as BDO world coordinates (y is the height,
`-5,288` to `7,074`).

## Notes

- Client 3002 has the same 6 team points and 20 sanctum points, one per
  sanctum `1` to `20` (866 bytes), matching its three-lane sanctum graph.
  The file is not in the archives of client 1784.
- The handler (`_bss/rosewarrevivepositionstaticstatus/`) shows one row per
  point: the type or the sanctum key, then its positions rounded to whole
  units, in file order.

## Open Questions

### The f32 After the Positions

`unknown_positions_00` is `500` on every team point and on 12 of the 14
sanctum points, `400` on sanctums `12` and `14` (client 3474). A spread
radius around the positions fits the values, but no Lua reads it.
