# `snowboardcourseinfo.bss` Format

## Purpose

The two colours of the snowboard course region map
(`ui_texture/minimap/area/snowboardcoursemap.bmp`), one 9-byte row each;
the courses themselves are in `snowboard.bss` (3.2 KB). A u32 count follows
the PABR magic. Each row holds the colour and a zero byte, a u8, and the
colour and zero byte again. On client 3474 the rows are `FF FF 14` with `1`
and `10 0D 10` with `0`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 2774 and later | 3483    | `snowboardcourseinfo.bss` | 38    | 2 Row   | 9         |

| Layout | File                      | Known        | Unknown      |
| ------ | ------------------------- | ------------ | ------------ |
| 1      | `snowboardcourseinfo.bss` | 26 B (68.4%) | 12 B (31.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `80e06bb8f5db`  |
| 3482   | Layout 1 | `80e06bb8f5db`  |
| 3474   | Layout 1 | `80e06bb8f5db`  |
| 3473   | Layout 1 | `80e06bb8f5db`  |
| 3464   | Layout 1 | `80e06bb8f5db`  |
| 3458   | Layout 1 | `80e06bb8f5db`  |
| 3454   | Layout 1 | `80e06bb8f5db`  |
| 3444   | Layout 1 | `80e06bb8f5db`  |
| 3435   | Layout 1 | `80e06bb8f5db`  |
| 3426   | Layout 1 | `80e06bb8f5db`  |
| 3418   | Layout 1 | `80e06bb8f5db`  |
| 3412   | Layout 1 | `80e06bb8f5db`  |
| 3402   | Layout 1 | `80e06bb8f5db`  |
| 3396   | Layout 1 | `80e06bb8f5db`  |
| 3387   | Layout 1 | `80e06bb8f5db`  |
| 3381   | Layout 1 | `80e06bb8f5db`  |
| 3373   | Layout 1 | `80e06bb8f5db`  |
| 3364   | Layout 1 | `80e06bb8f5db`  |
| 3356   | Layout 1 | `80e06bb8f5db`  |
| 3349   | Layout 1 | `80e06bb8f5db`  |
| 3342   | Layout 1 | `80e06bb8f5db`  |
| 3335   | Layout 1 | `80e06bb8f5db`  |
| 3326   | Layout 1 | `80e06bb8f5db`  |
| 3321   | Layout 1 | `80e06bb8f5db`  |
| 3314   | Layout 1 | `80e06bb8f5db`  |
| 3303   | Layout 1 | `80e06bb8f5db`  |
| 3302   | Layout 1 | `80e06bb8f5db`  |
| 3293   | Layout 1 | `80e06bb8f5db`  |
| 3283   | Layout 1 | `80e06bb8f5db`  |
| 3275   | Layout 1 | `80e06bb8f5db`  |
| 3267   | Layout 1 | `80e06bb8f5db`  |
| 3258   | Layout 1 | `80e06bb8f5db`  |
| 3251   | Layout 1 | `80e06bb8f5db`  |
| 3242   | Layout 1 | `80e06bb8f5db`  |
| 3235   | Layout 1 | `80e06bb8f5db`  |
| 3229   | Layout 1 | `80e06bb8f5db`  |
| 3212   | Layout 1 | `80e06bb8f5db`  |
| 3203   | Layout 1 | `80e06bb8f5db`  |
| 3193   | Layout 1 | `80e06bb8f5db`  |
| 3186   | Layout 1 | `80e06bb8f5db`  |
| 3177   | Layout 1 | `80e06bb8f5db`  |
| 3169   | Layout 1 | `80e06bb8f5db`  |
| 3158   | Layout 1 | `80e06bb8f5db`  |
| 3151   | Layout 1 | `80e06bb8f5db`  |
| 3144   | Layout 1 | `80e06bb8f5db`  |
| 3133   | Layout 1 | `80e06bb8f5db`  |
| 3125   | Layout 1 | `80e06bb8f5db`  |
| 3118   | Layout 1 | `80e06bb8f5db`  |
| 3111   | Layout 1 | `80e06bb8f5db`  |
| 3103   | Layout 1 | `80e06bb8f5db`  |
| 3095   | Layout 1 | `80e06bb8f5db`  |
| 3086   | Layout 1 | `80e06bb8f5db`  |
| 3072   | Layout 1 | `80e06bb8f5db`  |
| 3062   | Layout 1 | `80e06bb8f5db`  |
| 3052   | Layout 1 | `80e06bb8f5db`  |
| 3045   | Layout 1 | `80e06bb8f5db`  |
| 3037   | Layout 1 | `80e06bb8f5db`  |
| 3030   | Layout 1 | `80e06bb8f5db`  |
| 3021   | Layout 1 | `80e06bb8f5db`  |
| 3012   | Layout 1 | `80e06bb8f5db`  |
| 3002   | Layout 1 | `80e06bb8f5db`  |
| 2995   | Layout 1 | `80e06bb8f5db`  |
| 2987   | Layout 1 | `80e06bb8f5db`  |
| 2978   | Layout 1 | `80e06bb8f5db`  |
| 2970   | Layout 1 | `80e06bb8f5db`  |
| 2959   | Layout 1 | `80e06bb8f5db`  |
| 2951   | Layout 1 | `80e06bb8f5db`  |
| 2942   | Layout 1 | `80e06bb8f5db`  |
| 2935   | Layout 1 | `80e06bb8f5db`  |
| 2932   | Layout 1 | `80e06bb8f5db`  |
| 2923   | Layout 1 | `80e06bb8f5db`  |
| 2919   | Layout 1 | `80e06bb8f5db`  |
| 2907   | Layout 1 | `80e06bb8f5db`  |
| 2900   | Layout 1 | `80e06bb8f5db`  |
| 2891   | Layout 1 | `80e06bb8f5db`  |
| 2882   | Layout 1 | `80e06bb8f5db`  |
| 2872   | Layout 1 | `80e06bb8f5db`  |
| 2863   | Layout 1 | `80e06bb8f5db`  |
| 2855   | Layout 1 | `80e06bb8f5db`  |
| 2849   | Layout 1 | `80e06bb8f5db`  |
| 2844   | Layout 1 | `80e06bb8f5db`  |
| 2834   | Layout 1 | `80e06bb8f5db`  |
| 2825   | Layout 1 | `80e06bb8f5db`  |
| 2819   | Layout 1 | `80e06bb8f5db`  |
| 2811   | Layout 1 | `80e06bb8f5db`  |
| 2803   | Layout 1 | `80e06bb8f5db`  |
| 2794   | Layout 1 | `80e06bb8f5db`  |
| 2783   | Layout 1 | `80e06bb8f5db`  |
| 2774   | Layout 1 | `80e06bb8f5db`  |
| 2765   | No file  | `80e06bb8f5db`  |
| 2756   | No file  | `80e06bb8f5db`  |
| 2750   | No file  | `80e06bb8f5db`  |
| 2743   | No file  | `80e06bb8f5db`  |
| 2736   | No file  | `80e06bb8f5db`  |
| 2726   | No file  | `80e06bb8f5db`  |
| 2717   | No file  | `80e06bb8f5db`  |
| 2709   | No file  | `80e06bb8f5db`  |
| 2703   | No file  | `80e06bb8f5db`  |
| 2695   | No file  | `80e06bb8f5db`  |
| 2684   | No file  | `80e06bb8f5db`  |
| 2672   | No file  | `80e06bb8f5db`  |
| 2665   | No file  | `80e06bb8f5db`  |
| 2657   | No file  | `80e06bb8f5db`  |
| 2649   | No file  | `80e06bb8f5db`  |
| 2644   | No file  | `80e06bb8f5db`  |
| 2637   | No file  | `80e06bb8f5db`  |
| 2629   | No file  | `80e06bb8f5db`  |
| 2619   | No file  | `80e06bb8f5db`  |
| 2612   | No file  | `80e06bb8f5db`  |
| 2606   | No file  | `80e06bb8f5db`  |
| 2602   | No file  | `80e06bb8f5db`  |
| 2601   | No file  | `80e06bb8f5db`  |
| 2592   | No file  | `80e06bb8f5db`  |
| 2583   | No file  | `80e06bb8f5db`  |
| 2575   | No file  | `80e06bb8f5db`  |
| 2567   | No file  | `80e06bb8f5db`  |
| 2560   | No file  | `80e06bb8f5db`  |
| 2553   | No file  | `80e06bb8f5db`  |
| 2545   | No file  | `80e06bb8f5db`  |
| 2538   | No file  | `80e06bb8f5db`  |
| 2529   | No file  | `80e06bb8f5db`  |
| 2519   | No file  | `80e06bb8f5db`  |
| 2513   | No file  | `80e06bb8f5db`  |
| 2510   | No file  | `80e06bb8f5db`  |
| 2507   | No file  | `80e06bb8f5db`  |
| 2503   | No file  | `80e06bb8f5db`  |
| 2498   | No file  | `80e06bb8f5db`  |
| 2492   | No file  | `80e06bb8f5db`  |
| 2487   | No file  | `80e06bb8f5db`  |
| 2480   | No file  | `80e06bb8f5db`  |
| 2474   | No file  | `80e06bb8f5db`  |
| 2468   | No file  | `80e06bb8f5db`  |
| 2460   | No file  | `80e06bb8f5db`  |
| 2453   | No file  | `80e06bb8f5db`  |
| 2444   | No file  | `80e06bb8f5db`  |
| 2438   | No file  | `80e06bb8f5db`  |
| 2434   | No file  | `80e06bb8f5db`  |
| 2429   | No file  | `80e06bb8f5db`  |
| 2421   | No file  | `80e06bb8f5db`  |
| 2414   | No file  | `80e06bb8f5db`  |
| 2407   | No file  | `80e06bb8f5db`  |
| 2401   | No file  | `80e06bb8f5db`  |
| 2397   | No file  | `80e06bb8f5db`  |
| 2393   | No file  | `80e06bb8f5db`  |
| 2384   | No file  | `80e06bb8f5db`  |
| 2378   | No file  | `80e06bb8f5db`  |
| 2372   | No file  | `80e06bb8f5db`  |
| 2358   | No file  | `80e06bb8f5db`  |
| 2352   | No file  | `80e06bb8f5db`  |
| 2347   | No file  | `80e06bb8f5db`  |
| 2343   | No file  | `80e06bb8f5db`  |
| 2335   | No file  | `80e06bb8f5db`  |
| 2327   | No file  | `80e06bb8f5db`  |
| 2324   | No file  | `80e06bb8f5db`  |
| 2319   | No file  | `80e06bb8f5db`  |
| 2313   | No file  | `80e06bb8f5db`  |
| 2308   | No file  | `80e06bb8f5db`  |
| 2302   | No file  | `80e06bb8f5db`  |
| 2295   | No file  | `80e06bb8f5db`  |
| 2290   | No file  | `80e06bb8f5db`  |
| 2284   | No file  | `80e06bb8f5db`  |
| 2276   | No file  | `80e06bb8f5db`  |
| 2269   | No file  | `80e06bb8f5db`  |
| 2259   | No file  | `80e06bb8f5db`  |
| 2250   | No file  | `80e06bb8f5db`  |
| 2243   | No file  | `80e06bb8f5db`  |
| 2235   | No file  | `80e06bb8f5db`  |
| 2229   | No file  | `80e06bb8f5db`  |
| 2224   | No file  | `80e06bb8f5db`  |
| 2218   | No file  | `80e06bb8f5db`  |
| 2215   | No file  | `80e06bb8f5db`  |
| 2207   | No file  | `80e06bb8f5db`  |
| 2203   | No file  | `80e06bb8f5db`  |
| 2196   | No file  | `80e06bb8f5db`  |
| 2192   | No file  | `80e06bb8f5db`  |
| 2189   | No file  | `80e06bb8f5db`  |
| 2183   | No file  | `80e06bb8f5db`  |
| 2179   | No file  | `80e06bb8f5db`  |
| 2171   | No file  | `80e06bb8f5db`  |
| 2163   | No file  | `80e06bb8f5db`  |
| 2156   | No file  | `80e06bb8f5db`  |
| 2151   | No file  | `80e06bb8f5db`  |
| 2147   | No file  | `80e06bb8f5db`  |
| 2142   | No file  | `80e06bb8f5db`  |
| 2138   | No file  | `80e06bb8f5db`  |
| 2134   | No file  | `80e06bb8f5db`  |
| 2130   | No file  | `80e06bb8f5db`  |
| 2122   | No file  | `80e06bb8f5db`  |
| 2107   | No file  | `80e06bb8f5db`  |
| 2098   | No file  | `80e06bb8f5db`  |
| 2089   | No file  | `80e06bb8f5db`  |
| 2081   | No file  | `80e06bb8f5db`  |
| 2073   | No file  | `80e06bb8f5db`  |
| 2067   | No file  | `80e06bb8f5db`  |
| 2063   | No file  | `80e06bb8f5db`  |
| 2059   | No file  | `80e06bb8f5db`  |
| 2052   | No file  | `80e06bb8f5db`  |
| 2044   | No file  | `80e06bb8f5db`  |
| 2039   | No file  | `80e06bb8f5db`  |
| 2032   | No file  | `80e06bb8f5db`  |
| 2025   | No file  | `80e06bb8f5db`  |
| 2011   | No file  | `80e06bb8f5db`  |
| 2005   | No file  | `80e06bb8f5db`  |
| 2000   | No file  | `80e06bb8f5db`  |
| 1996   | No file  | `80e06bb8f5db`  |
| 1991   | No file  | `80e06bb8f5db`  |
| 1985   | No file  | `80e06bb8f5db`  |
| 1980   | No file  | `80e06bb8f5db`  |
| 1969   | No file  | `80e06bb8f5db`  |
| 1964   | No file  | `80e06bb8f5db`  |
| 1958   | No file  | `80e06bb8f5db`  |
| 1950   | No file  | `80e06bb8f5db`  |
| 1945   | No file  | `80e06bb8f5db`  |
| 1937   | No file  | `80e06bb8f5db`  |
| 1933   | No file  | `80e06bb8f5db`  |
| 1927   | No file  | `80e06bb8f5db`  |
| 1921   | No file  | `80e06bb8f5db`  |
| 1914   | No file  | `80e06bb8f5db`  |
| 1908   | No file  | `80e06bb8f5db`  |
| 1897   | No file  | `80e06bb8f5db`  |
| 1892   | No file  | `80e06bb8f5db`  |
| 1886   | No file  | `80e06bb8f5db`  |
| 1881   | No file  | `80e06bb8f5db`  |
| 1871   | No file  | `80e06bb8f5db`  |
| 1866   | No file  | `80e06bb8f5db`  |
| 1862   | No file  | `80e06bb8f5db`  |
| 1854   | No file  | `80e06bb8f5db`  |
| 1846   | No file  | `80e06bb8f5db`  |
| 1838   | No file  | `80e06bb8f5db`  |
| 1832   | No file  | `80e06bb8f5db`  |
| 1826   | No file  | `80e06bb8f5db`  |
| 1822   | No file  | `80e06bb8f5db`  |
| 1818   | No file  | `80e06bb8f5db`  |
| 1804   | No file  | `80e06bb8f5db`  |
| 1794   | No file  | `80e06bb8f5db`  |
| 1790   | No file  | `80e06bb8f5db`  |
| 1784   | No file  | `80e06bb8f5db`  |
| 1774   | No file  | `80e06bb8f5db`  |
| 1771   | No file  | `80e06bb8f5db`  |
| 1762   | No file  | `80e06bb8f5db`  |
| 1759   | No file  | `80e06bb8f5db`  |
| 1754   | No file  | `80e06bb8f5db`  |
| 1749   | No file  | `80e06bb8f5db`  |
| 1743   | No file  | `80e06bb8f5db`  |
| 1737   | No file  | `80e06bb8f5db`  |
| 1731   | No file  | `80e06bb8f5db`  |
| 1725   | No file  | `80e06bb8f5db`  |
| 1717   | No file  | `80e06bb8f5db`  |
| 1710   | No file  | `80e06bb8f5db`  |
| 1704   | No file  | `80e06bb8f5db`  |
| 1698   | No file  | `80e06bb8f5db`  |
| 1690   | No file  | `80e06bb8f5db`  |
| 1685   | No file  | `80e06bb8f5db`  |
| 1680   | No file  | `80e06bb8f5db`  |
| 1674   | No file  | `80e06bb8f5db`  |
| 1668   | No file  | `80e06bb8f5db`  |
| 1659   | No file  | `80e06bb8f5db`  |
| 1649   | No file  | `80e06bb8f5db`  |
| 1642   | No file  | `80e06bb8f5db`  |
| 1636   | No file  | `80e06bb8f5db`  |
| 1628   | No file  | `80e06bb8f5db`  |
| 1622   | No file  | `80e06bb8f5db`  |
| 1614   | No file  | `80e06bb8f5db`  |
| 1608   | No file  | `80e06bb8f5db`  |
| 1602   | No file  | `80e06bb8f5db`  |
| 1598   | No file  | `80e06bb8f5db`  |
| 1594   | No file  | `80e06bb8f5db`  |
| 1590   | No file  | `80e06bb8f5db`  |
| 1587   | No file  | `80e06bb8f5db`  |
| 1584   | No file  | `80e06bb8f5db`  |
| 1579   | No file  | `80e06bb8f5db`  |
| 1572   | No file  | `80e06bb8f5db`  |
| 1565   | No file  | `80e06bb8f5db`  |
| 1559   | No file  | `80e06bb8f5db`  |
| 1554   | No file  | `80e06bb8f5db`  |
| 1547   | No file  | `80e06bb8f5db`  |
| 1537   | No file  | `80e06bb8f5db`  |
| 1529   | No file  | `80e06bb8f5db`  |
| 1524   | No file  | `80e06bb8f5db`  |
| 1519   | No file  | `80e06bb8f5db`  |
| 1509   | No file  | `80e06bb8f5db`  |
| 1506   | No file  | `80e06bb8f5db`  |
| 1504   | No file  | `80e06bb8f5db`  |
| 1500   | No file  | `80e06bb8f5db`  |
| 1493   | No file  | `80e06bb8f5db`  |
| 1489   | No file  | `80e06bb8f5db`  |
| 1485   | No file  | `80e06bb8f5db`  |
| 1481   | No file  | `80e06bb8f5db`  |
| 1474   | No file  | `80e06bb8f5db`  |
| 1466   | No file  | `80e06bb8f5db`  |
| 1462   | No file  | `80e06bb8f5db`  |
| 1459   | No file  | `80e06bb8f5db`  |
| 1453   | No file  | `80e06bb8f5db`  |
| 1450   | No file  | `80e06bb8f5db`  |
| 1445   | No file  | `80e06bb8f5db`  |
| 1439   | No file  | `80e06bb8f5db`  |
| 1433   | No file  | `80e06bb8f5db`  |
| 1430   | No file  | `80e06bb8f5db`  |
| 1426   | No file  | `80e06bb8f5db`  |
| 1421   | No file  | `80e06bb8f5db`  |
| 1417   | No file  | `80e06bb8f5db`  |
| 1416   | No file  | `80e06bb8f5db`  |
| 1409   | No file  | `80e06bb8f5db`  |
| 1405   | No file  | `80e06bb8f5db`  |
| 1401   | No file  | `80e06bb8f5db`  |
| 1396   | No file  | `80e06bb8f5db`  |
| 1391   | No file  | `80e06bb8f5db`  |
| 1390   | No file  | `80e06bb8f5db`  |
| 1386   | No file  | `80e06bb8f5db`  |
| 1381   | No file  | `80e06bb8f5db`  |
| 1379   | No file  | `80e06bb8f5db`  |
| 1372   | No file  | `80e06bb8f5db`  |
| 1366   | No file  | `80e06bb8f5db`  |
| 1364   | No file  | `80e06bb8f5db`  |
| 1363   | No file  | `80e06bb8f5db`  |
| 1360   | No file  | `80e06bb8f5db`  |
| 1358   | No file  | `80e06bb8f5db`  |
| 1355   | No file  | `80e06bb8f5db`  |
| 1351   | No file  | `80e06bb8f5db`  |
| 1348   | No file  | `80e06bb8f5db`  |
| 1346   | No file  | `80e06bb8f5db`  |
| 1341   | No file  | `80e06bb8f5db`  |
| 1340   | No file  | `80e06bb8f5db`  |
| 1338   | No file  | `80e06bb8f5db`  |
| 1335   | No file  | `80e06bb8f5db`  |
| 1333   | No file  | `80e06bb8f5db`  |
| 1329   | No file  | `80e06bb8f5db`  |
| 1327   | No file  | `80e06bb8f5db`  |
| 1324   | No file  | `80e06bb8f5db`  |
| 1321   | No file  | `80e06bb8f5db`  |
| 1319   | No file  | `80e06bb8f5db`  |
| 1318   | No file  | `80e06bb8f5db`  |
| 1316   | No file  | `80e06bb8f5db`  |
| 1313   | No file  | `80e06bb8f5db`  |
| 1311   | No file  | `80e06bb8f5db`  |
| 1309   | No file  | `80e06bb8f5db`  |
| 1304   | No file  | `80e06bb8f5db`  |
| 1292   | No file  | `80e06bb8f5db`  |
| 1286   | No file  | `80e06bb8f5db`  |
| 1280   | No file  | `80e06bb8f5db`  |
| 1276   | No file  | `80e06bb8f5db`  |
| 1267   | No file  | `80e06bb8f5db`  |
| 1261   | No file  | `80e06bb8f5db`  |
| 1256   | No file  | `80e06bb8f5db`  |
| 1250   | No file  | `80e06bb8f5db`  |
| 1246   | No file  | `80e06bb8f5db`  |
| 1239   | No file  | `80e06bb8f5db`  |
| 1230   | No file  | `80e06bb8f5db`  |
| 1226   | No file  | `80e06bb8f5db`  |
| 1220   | No file  | `80e06bb8f5db`  |
| 1217   | No file  | `80e06bb8f5db`  |
| 1211   | No file  | `80e06bb8f5db`  |
| 1210   | No file  | `80e06bb8f5db`  |
| 1208   | No file  | `80e06bb8f5db`  |
| 1203   | No file  | `80e06bb8f5db`  |
| 1197   | No file  | `80e06bb8f5db`  |
| 1194   | No file  | `80e06bb8f5db`  |
| 1192   | No file  | `80e06bb8f5db`  |
| 1187   | No file  | `80e06bb8f5db`  |
| 1183   | No file  | `80e06bb8f5db`  |
| 1177   | No file  | `80e06bb8f5db`  |
| 1173   | No file  | `80e06bb8f5db`  |
| 1167   | No file  | `80e06bb8f5db`  |
| 1164   | No file  | `80e06bb8f5db`  |
| 1156   | No file  | `80e06bb8f5db`  |
| 1149   | No file  | `80e06bb8f5db`  |
| 1144   | No file  | `80e06bb8f5db`  |
| 1137   | No file  | `80e06bb8f5db`  |
| 1132   | No file  | `80e06bb8f5db`  |
| 1127   | No file  | `80e06bb8f5db`  |
| 1122   | No file  | `80e06bb8f5db`  |
| 1118   | No file  | `80e06bb8f5db`  |
| 1114   | No file  | `80e06bb8f5db`  |
| 1109   | No file  | `80e06bb8f5db`  |
| 1102   | No file  | `80e06bb8f5db`  |
| 1096   | No file  | `80e06bb8f5db`  |
| 1088   | No file  | `80e06bb8f5db`  |
| 1081   | No file  | `80e06bb8f5db`  |
| 1076   | No file  | `80e06bb8f5db`  |
| 1069   | No file  | `80e06bb8f5db`  |
| 1064   | No file  | `80e06bb8f5db`  |
| 1058   | No file  | `80e06bb8f5db`  |
| 1051   | No file  | `80e06bb8f5db`  |
| 1044   | No file  | `80e06bb8f5db`  |
| 1036   | No file  | `80e06bb8f5db`  |
| 1026   | No file  | `80e06bb8f5db`  |
| 1016   | No file  | `80e06bb8f5db`  |
| 1009   | No file  | `80e06bb8f5db`  |
| 1005   | No file  | `80e06bb8f5db`  |
| 1000   | No file  | `80e06bb8f5db`  |
| 998    | No file  | `80e06bb8f5db`  |
| 990    | No file  | `80e06bb8f5db`  |
| 979    | No file  | `80e06bb8f5db`  |
| 972    | No file  | `80e06bb8f5db`  |
| 963    | No file  | `80e06bb8f5db`  |
| 955    | No file  | `80e06bb8f5db`  |
| 946    | No file  | `80e06bb8f5db`  |
| 938    | No file  | `80e06bb8f5db`  |
| 927    | No file  | `80e06bb8f5db`  |
| 911    | No file  | `80e06bb8f5db`  |
| 904    | No file  | `80e06bb8f5db`  |
| 899    | No file  | `80e06bb8f5db`  |
| 894    | No file  | `80e06bb8f5db`  |
| 885    | No file  | `80e06bb8f5db`  |
| 879    | No file  | `80e06bb8f5db`  |
| 872    | No file  | `80e06bb8f5db`  |
| 864    | No file  | `80e06bb8f5db`  |
| 855    | No file  | `80e06bb8f5db`  |
| 853    | No file  | `80e06bb8f5db`  |
| 845    | No file  | `80e06bb8f5db`  |
| 837    | No file  | `80e06bb8f5db`  |
| 829    | No file  | `80e06bb8f5db`  |
| 822    | No file  | `80e06bb8f5db`  |
| 814    | No file  | `80e06bb8f5db`  |
| 805    | No file  | `80e06bb8f5db`  |
| 794    | No file  | `80e06bb8f5db`  |
| 787    | No file  | `80e06bb8f5db`  |
| 780    | No file  | `80e06bb8f5db`  |
| 771    | No file  | `80e06bb8f5db`  |
| 760    | No file  | `80e06bb8f5db`  |
| 748    | No file  | `80e06bb8f5db`  |
| 741    | No file  | `80e06bb8f5db`  |
| 736    | No file  | `80e06bb8f5db`  |
| 731    | No file  | `80e06bb8f5db`  |
| 723    | No file  | `80e06bb8f5db`  |
| 711    | No file  | `80e06bb8f5db`  |
| 707    | No file  | `80e06bb8f5db`  |
| 697    | No file  | `80e06bb8f5db`  |
| 689    | No file  | `80e06bb8f5db`  |
| 683    | No file  | `80e06bb8f5db`  |
| 678    | No file  | `80e06bb8f5db`  |
| 670    | No file  | `80e06bb8f5db`  |
| 661    | No file  | `80e06bb8f5db`  |
| 656    | No file  | `80e06bb8f5db`  |
| 652    | No file  | `80e06bb8f5db`  |
| 643    | No file  | `80e06bb8f5db`  |
| 637    | No file  | `80e06bb8f5db`  |
| 630    | No file  | `80e06bb8f5db`  |
| 627    | No file  | `80e06bb8f5db`  |
| 621    | No file  | `80e06bb8f5db`  |
| 617    | No file  | `80e06bb8f5db`  |
| 615    | No file  | `80e06bb8f5db`  |
| 606    | No file  | `80e06bb8f5db`  |
| 599    | No file  | `80e06bb8f5db`  |
| 592    | No file  | `80e06bb8f5db`  |
| 586    | No file  | `80e06bb8f5db`  |
| 577    | No file  | `80e06bb8f5db`  |
| 569    | No file  | `80e06bb8f5db`  |
| 561    | No file  | `80e06bb8f5db`  |
| 554    | No file  | `80e06bb8f5db`  |
| 542    | No file  | `80e06bb8f5db`  |
| 532    | No file  | `80e06bb8f5db`  |
| 531    | No file  | `80e06bb8f5db`  |
| 526    | No file  | `80e06bb8f5db`  |
| 521    | No file  | `80e06bb8f5db`  |
| 517    | No file  | `80e06bb8f5db`  |
| 510    | No file  | `80e06bb8f5db`  |
| 508    | No file  | `80e06bb8f5db`  |
| 504    | No file  | `80e06bb8f5db`  |
| 497    | No file  | `80e06bb8f5db`  |
| 491    | No file  | `80e06bb8f5db`  |
| 485    | No file  | `80e06bb8f5db`  |
| 478    | No file  | `80e06bb8f5db`  |
| 472    | No file  | `80e06bb8f5db`  |
| 466    | No file  | `80e06bb8f5db`  |
| 457    | No file  | `80e06bb8f5db`  |
| 452    | No file  | `80e06bb8f5db`  |
| 449    | No file  | `80e06bb8f5db`  |
| 435    | No file  | `80e06bb8f5db`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field        | Notes                                                      |
| ------------------- | --------------- | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32             | row_count    | Number of rows                                             |
| `+0x08`             | Row[row_count]  | rows         | See Row; byte-packed                                       |
| `rows+0x00`         | String Table    | string_table | See String Table                                           |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where `rows` ends              |
| `string_table+0x04` | u32             | zero         | Always `0`                                                 |

### Row (9 bytes)

| Offset  | Type     | Field      | Notes                                       |
| ------- | -------- | ---------- | ------------------------------------------- |
| `+0x00` | bytes[3] | map_color  | Region map colour, stored blue, green, red; `FF FF 14` and `10 0D 10` on client 3474 |
| `+0x03` | u8       | unknown_03 | Always `0`                                  |
| `+0x04` | u8       | unknown_04 | `1` and `0`, one per row                    |
| `+0x05` | bytes[3] | unknown_05 | Equals `map_color` on every row             |
| `+0x08` | u8       | unknown_08 | Always `0`                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 02 00 00 00 FF FF 14 00 01 FF FF 14 00 10 0D 10 00 00 10 0D 10 00 00 00 00 00 1A 00 00 00 00 00 00 00`
  (38 bytes). The file is not in the archives of clients 794 to 2519.
- `map_color` follows `ui_texture/minimap/area/snowboardcoursemap.bmp.rid`,
  the palette of the snowboard course region map, which lists exactly these
  two colours (`100d10` first) on client 3474; the same holds for the
  region maps of three other tables of this row shape
  ([`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md#field-names)
  Field Names).
- The colours recur in other small tables of this client:
  `FF FF 14` in the 9-byte rows of `hardcorechannelinfo.bss`, and
  `10 0D 10` there, in [`rosewarinfo.bss`](rosewarinfo_bss.md) and in the
  `_Count` row of [`edaniaregioninfo.bss`](edaniaregioninfo_bss.md). Those
  files put the u8 after both copies; this file puts it between them.
- The snowboard menu (`panel_window_snowboard_menu_all_1.luac`, client
  3474) reads each course with `ToClient_GetSnowBoardStaticStatusByIndex`
  and `getKeyRaw()`, `getMode()` (`__eSnowBoardCourseMode_Item` or
  `_Speed`), `getName()` and `getCheckPointCount()`. None of these returns
  a 3-byte value.
- The file is newer than client 1784: no sheet of a private server's
  `DataSheets.bexcel` on that client has `Snowboard` in its name.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`:
  `map_color` as `rrggbb`.

## Open Questions

### The Value of Each Colour

Read as `rrggbb`, the rows are `14ffff` (cyan) with `1` and `100d10` (near
black, the first colour of every region map palette of this row shape) with
`0`. Whether `unknown_04` is a course mode, a course key or a flag, and
what the second copy of the colour is for, is not known; no client Lua call
reads the file.
