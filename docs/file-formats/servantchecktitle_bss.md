# `servantchecktitle.bss` Format

## Purpose

A title tied to owning a servant: the PABR magic, a u16, a `title.dbss`
title and a servant character key, then an empty string table. On client
3474 it holds title `2705` Captain Epheria ("Title Requirement: Exchange
Epheria Galleon Ship License") and character `31020` Epheria Galleon.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | -------------- | --------- |
| 1      | 2138 and later | 3483    | `servantchecktitle.bss` | 24    | 1 String Table | 4         |

| Layout | File                    | Known        | Unknown    |
| ------ | ----------------------- | ------------ | ---------- |
| 1      | `servantchecktitle.bss` | 22 B (91.7%) | 2 B (8.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fc6d04d010a2`  |
| 3482   | Layout 1 | `fc6d04d010a2`  |
| 3474   | Layout 1 | `fc6d04d010a2`  |
| 3473   | Layout 1 | `fc6d04d010a2`  |
| 3464   | Layout 1 | `fc6d04d010a2`  |
| 3458   | Layout 1 | `fc6d04d010a2`  |
| 3454   | Layout 1 | `fc6d04d010a2`  |
| 3444   | Layout 1 | `fc6d04d010a2`  |
| 3435   | Layout 1 | `fc6d04d010a2`  |
| 3426   | Layout 1 | `fc6d04d010a2`  |
| 3418   | Layout 1 | `fc6d04d010a2`  |
| 3412   | Layout 1 | `fc6d04d010a2`  |
| 3402   | Layout 1 | `fc6d04d010a2`  |
| 3396   | Layout 1 | `fc6d04d010a2`  |
| 3387   | Layout 1 | `fc6d04d010a2`  |
| 3381   | Layout 1 | `fc6d04d010a2`  |
| 3373   | Layout 1 | `fc6d04d010a2`  |
| 3364   | Layout 1 | `fc6d04d010a2`  |
| 3356   | Layout 1 | `fc6d04d010a2`  |
| 3349   | Layout 1 | `fc6d04d010a2`  |
| 3342   | Layout 1 | `fc6d04d010a2`  |
| 3335   | Layout 1 | `fc6d04d010a2`  |
| 3326   | Layout 1 | `fc6d04d010a2`  |
| 3321   | Layout 1 | `fc6d04d010a2`  |
| 3314   | Layout 1 | `fc6d04d010a2`  |
| 3303   | Layout 1 | `fc6d04d010a2`  |
| 3302   | Layout 1 | `fc6d04d010a2`  |
| 3293   | Layout 1 | `fc6d04d010a2`  |
| 3283   | Layout 1 | `fc6d04d010a2`  |
| 3275   | Layout 1 | `fc6d04d010a2`  |
| 3267   | Layout 1 | `fc6d04d010a2`  |
| 3258   | Layout 1 | `fc6d04d010a2`  |
| 3251   | Layout 1 | `fc6d04d010a2`  |
| 3242   | Layout 1 | `fc6d04d010a2`  |
| 3235   | Layout 1 | `fc6d04d010a2`  |
| 3229   | Layout 1 | `fc6d04d010a2`  |
| 3212   | Layout 1 | `fc6d04d010a2`  |
| 3203   | Layout 1 | `fc6d04d010a2`  |
| 3193   | Layout 1 | `fc6d04d010a2`  |
| 3186   | Layout 1 | `fc6d04d010a2`  |
| 3177   | Layout 1 | `fc6d04d010a2`  |
| 3169   | Layout 1 | `fc6d04d010a2`  |
| 3158   | Layout 1 | `fc6d04d010a2`  |
| 3151   | Layout 1 | `fc6d04d010a2`  |
| 3144   | Layout 1 | `fc6d04d010a2`  |
| 3133   | Layout 1 | `fc6d04d010a2`  |
| 3125   | Layout 1 | `fc6d04d010a2`  |
| 3118   | Layout 1 | `fc6d04d010a2`  |
| 3111   | Layout 1 | `fc6d04d010a2`  |
| 3103   | Layout 1 | `fc6d04d010a2`  |
| 3095   | Layout 1 | `fc6d04d010a2`  |
| 3086   | Layout 1 | `fc6d04d010a2`  |
| 3072   | Layout 1 | `fc6d04d010a2`  |
| 3062   | Layout 1 | `fc6d04d010a2`  |
| 3052   | Layout 1 | `fc6d04d010a2`  |
| 3045   | Layout 1 | `fc6d04d010a2`  |
| 3037   | Layout 1 | `fc6d04d010a2`  |
| 3030   | Layout 1 | `fc6d04d010a2`  |
| 3021   | Layout 1 | `fc6d04d010a2`  |
| 3012   | Layout 1 | `fc6d04d010a2`  |
| 3002   | Layout 1 | `fc6d04d010a2`  |
| 2995   | Layout 1 | `fc6d04d010a2`  |
| 2987   | Layout 1 | `fc6d04d010a2`  |
| 2978   | Layout 1 | `fc6d04d010a2`  |
| 2970   | Layout 1 | `fc6d04d010a2`  |
| 2959   | Layout 1 | `fc6d04d010a2`  |
| 2951   | Layout 1 | `fc6d04d010a2`  |
| 2942   | Layout 1 | `fc6d04d010a2`  |
| 2935   | Layout 1 | `fc6d04d010a2`  |
| 2932   | Layout 1 | `fc6d04d010a2`  |
| 2923   | Layout 1 | `fc6d04d010a2`  |
| 2919   | Layout 1 | `fc6d04d010a2`  |
| 2907   | Layout 1 | `fc6d04d010a2`  |
| 2900   | Layout 1 | `fc6d04d010a2`  |
| 2891   | Layout 1 | `fc6d04d010a2`  |
| 2882   | Layout 1 | `fc6d04d010a2`  |
| 2872   | Layout 1 | `fc6d04d010a2`  |
| 2863   | Layout 1 | `fc6d04d010a2`  |
| 2855   | Layout 1 | `fc6d04d010a2`  |
| 2849   | Layout 1 | `fc6d04d010a2`  |
| 2844   | Layout 1 | `fc6d04d010a2`  |
| 2834   | Layout 1 | `fc6d04d010a2`  |
| 2825   | Layout 1 | `fc6d04d010a2`  |
| 2819   | Layout 1 | `fc6d04d010a2`  |
| 2811   | Layout 1 | `fc6d04d010a2`  |
| 2803   | Layout 1 | `fc6d04d010a2`  |
| 2794   | Layout 1 | `fc6d04d010a2`  |
| 2783   | Layout 1 | `fc6d04d010a2`  |
| 2774   | Layout 1 | `fc6d04d010a2`  |
| 2765   | Layout 1 | `fc6d04d010a2`  |
| 2756   | Layout 1 | `fc6d04d010a2`  |
| 2750   | Layout 1 | `fc6d04d010a2`  |
| 2743   | Layout 1 | `fc6d04d010a2`  |
| 2736   | Layout 1 | `fc6d04d010a2`  |
| 2726   | Layout 1 | `fc6d04d010a2`  |
| 2717   | Layout 1 | `fc6d04d010a2`  |
| 2709   | Layout 1 | `fc6d04d010a2`  |
| 2703   | Layout 1 | `fc6d04d010a2`  |
| 2695   | Layout 1 | `fc6d04d010a2`  |
| 2684   | Layout 1 | `fc6d04d010a2`  |
| 2672   | Layout 1 | `fc6d04d010a2`  |
| 2665   | Layout 1 | `fc6d04d010a2`  |
| 2657   | Layout 1 | `fc6d04d010a2`  |
| 2649   | Layout 1 | `fc6d04d010a2`  |
| 2644   | Layout 1 | `fc6d04d010a2`  |
| 2637   | Layout 1 | `fc6d04d010a2`  |
| 2629   | Layout 1 | `fc6d04d010a2`  |
| 2619   | Layout 1 | `fc6d04d010a2`  |
| 2612   | Layout 1 | `fc6d04d010a2`  |
| 2606   | Layout 1 | `fc6d04d010a2`  |
| 2602   | Layout 1 | `fc6d04d010a2`  |
| 2601   | Layout 1 | `fc6d04d010a2`  |
| 2592   | Layout 1 | `fc6d04d010a2`  |
| 2583   | Layout 1 | `fc6d04d010a2`  |
| 2575   | Layout 1 | `fc6d04d010a2`  |
| 2567   | Layout 1 | `fc6d04d010a2`  |
| 2560   | Layout 1 | `fc6d04d010a2`  |
| 2553   | Layout 1 | `fc6d04d010a2`  |
| 2545   | Layout 1 | `fc6d04d010a2`  |
| 2538   | Layout 1 | `fc6d04d010a2`  |
| 2529   | Layout 1 | `fc6d04d010a2`  |
| 2519   | Layout 1 | `fc6d04d010a2`  |
| 2513   | Layout 1 | `fc6d04d010a2`  |
| 2510   | Layout 1 | `fc6d04d010a2`  |
| 2507   | Layout 1 | `fc6d04d010a2`  |
| 2503   | Layout 1 | `fc6d04d010a2`  |
| 2498   | Layout 1 | `fc6d04d010a2`  |
| 2492   | Layout 1 | `fc6d04d010a2`  |
| 2487   | Layout 1 | `fc6d04d010a2`  |
| 2480   | Layout 1 | `fc6d04d010a2`  |
| 2474   | Layout 1 | `fc6d04d010a2`  |
| 2468   | Layout 1 | `fc6d04d010a2`  |
| 2460   | Layout 1 | `fc6d04d010a2`  |
| 2453   | Layout 1 | `fc6d04d010a2`  |
| 2444   | Layout 1 | `fc6d04d010a2`  |
| 2438   | Layout 1 | `fc6d04d010a2`  |
| 2434   | Layout 1 | `fc6d04d010a2`  |
| 2429   | Layout 1 | `fc6d04d010a2`  |
| 2421   | Layout 1 | `fc6d04d010a2`  |
| 2414   | Layout 1 | `fc6d04d010a2`  |
| 2407   | Layout 1 | `fc6d04d010a2`  |
| 2401   | Layout 1 | `fc6d04d010a2`  |
| 2397   | Layout 1 | `fc6d04d010a2`  |
| 2393   | Layout 1 | `fc6d04d010a2`  |
| 2384   | Layout 1 | `fc6d04d010a2`  |
| 2378   | Layout 1 | `fc6d04d010a2`  |
| 2372   | Layout 1 | `fc6d04d010a2`  |
| 2358   | Layout 1 | `fc6d04d010a2`  |
| 2352   | Layout 1 | `fc6d04d010a2`  |
| 2347   | Layout 1 | `fc6d04d010a2`  |
| 2343   | Layout 1 | `fc6d04d010a2`  |
| 2335   | Layout 1 | `fc6d04d010a2`  |
| 2327   | Layout 1 | `fc6d04d010a2`  |
| 2324   | Layout 1 | `fc6d04d010a2`  |
| 2319   | Layout 1 | `fc6d04d010a2`  |
| 2313   | Layout 1 | `fc6d04d010a2`  |
| 2308   | Layout 1 | `fc6d04d010a2`  |
| 2302   | Layout 1 | `fc6d04d010a2`  |
| 2295   | Layout 1 | `fc6d04d010a2`  |
| 2290   | Layout 1 | `fc6d04d010a2`  |
| 2284   | Layout 1 | `fc6d04d010a2`  |
| 2276   | Layout 1 | `fc6d04d010a2`  |
| 2269   | Layout 1 | `fc6d04d010a2`  |
| 2259   | Layout 1 | `fc6d04d010a2`  |
| 2250   | Layout 1 | `fc6d04d010a2`  |
| 2243   | Layout 1 | `fc6d04d010a2`  |
| 2235   | Layout 1 | `fc6d04d010a2`  |
| 2229   | Layout 1 | `fc6d04d010a2`  |
| 2224   | Layout 1 | `fc6d04d010a2`  |
| 2218   | Layout 1 | `fc6d04d010a2`  |
| 2215   | Layout 1 | `fc6d04d010a2`  |
| 2207   | Layout 1 | `fc6d04d010a2`  |
| 2203   | Layout 1 | `fc6d04d010a2`  |
| 2196   | Layout 1 | `fc6d04d010a2`  |
| 2192   | Layout 1 | `fc6d04d010a2`  |
| 2189   | Layout 1 | `fc6d04d010a2`  |
| 2183   | Layout 1 | `fc6d04d010a2`  |
| 2179   | Layout 1 | `fc6d04d010a2`  |
| 2171   | Layout 1 | `fc6d04d010a2`  |
| 2163   | Layout 1 | `fc6d04d010a2`  |
| 2156   | Layout 1 | `fc6d04d010a2`  |
| 2151   | Layout 1 | `fc6d04d010a2`  |
| 2147   | Layout 1 | `fc6d04d010a2`  |
| 2142   | Layout 1 | `fc6d04d010a2`  |
| 2138   | Layout 1 | `fc6d04d010a2`  |
| 2134   | No file  | `fc6d04d010a2`  |
| 2130   | No file  | `fc6d04d010a2`  |
| 2122   | No file  | `fc6d04d010a2`  |
| 2107   | No file  | `fc6d04d010a2`  |
| 2098   | No file  | `fc6d04d010a2`  |
| 2089   | No file  | `fc6d04d010a2`  |
| 2081   | No file  | `fc6d04d010a2`  |
| 2073   | No file  | `fc6d04d010a2`  |
| 2067   | No file  | `fc6d04d010a2`  |
| 2063   | No file  | `fc6d04d010a2`  |
| 2059   | No file  | `fc6d04d010a2`  |
| 2052   | No file  | `fc6d04d010a2`  |
| 2044   | No file  | `fc6d04d010a2`  |
| 2039   | No file  | `fc6d04d010a2`  |
| 2032   | No file  | `fc6d04d010a2`  |
| 2025   | No file  | `fc6d04d010a2`  |
| 2011   | No file  | `fc6d04d010a2`  |
| 2005   | No file  | `fc6d04d010a2`  |
| 2000   | No file  | `fc6d04d010a2`  |
| 1996   | No file  | `fc6d04d010a2`  |
| 1991   | No file  | `fc6d04d010a2`  |
| 1985   | No file  | `fc6d04d010a2`  |
| 1980   | No file  | `fc6d04d010a2`  |
| 1969   | No file  | `fc6d04d010a2`  |
| 1964   | No file  | `fc6d04d010a2`  |
| 1958   | No file  | `fc6d04d010a2`  |
| 1950   | No file  | `fc6d04d010a2`  |
| 1945   | No file  | `fc6d04d010a2`  |
| 1937   | No file  | `fc6d04d010a2`  |
| 1933   | No file  | `fc6d04d010a2`  |
| 1927   | No file  | `fc6d04d010a2`  |
| 1921   | No file  | `fc6d04d010a2`  |
| 1914   | No file  | `fc6d04d010a2`  |
| 1908   | No file  | `fc6d04d010a2`  |
| 1897   | No file  | `fc6d04d010a2`  |
| 1892   | No file  | `fc6d04d010a2`  |
| 1886   | No file  | `fc6d04d010a2`  |
| 1881   | No file  | `fc6d04d010a2`  |
| 1871   | No file  | `fc6d04d010a2`  |
| 1866   | No file  | `fc6d04d010a2`  |
| 1862   | No file  | `fc6d04d010a2`  |
| 1854   | No file  | `fc6d04d010a2`  |
| 1846   | No file  | `fc6d04d010a2`  |
| 1838   | No file  | `fc6d04d010a2`  |
| 1832   | No file  | `fc6d04d010a2`  |
| 1826   | No file  | `fc6d04d010a2`  |
| 1822   | No file  | `fc6d04d010a2`  |
| 1818   | No file  | `fc6d04d010a2`  |
| 1804   | No file  | `fc6d04d010a2`  |
| 1794   | No file  | `fc6d04d010a2`  |
| 1790   | No file  | `fc6d04d010a2`  |
| 1784   | No file  | `fc6d04d010a2`  |
| 1774   | No file  | `fc6d04d010a2`  |
| 1771   | No file  | `fc6d04d010a2`  |
| 1762   | No file  | `fc6d04d010a2`  |
| 1759   | No file  | `fc6d04d010a2`  |
| 1754   | No file  | `fc6d04d010a2`  |
| 1749   | No file  | `fc6d04d010a2`  |
| 1743   | No file  | `fc6d04d010a2`  |
| 1737   | No file  | `fc6d04d010a2`  |
| 1731   | No file  | `fc6d04d010a2`  |
| 1725   | No file  | `fc6d04d010a2`  |
| 1717   | No file  | `fc6d04d010a2`  |
| 1710   | No file  | `fc6d04d010a2`  |
| 1704   | No file  | `fc6d04d010a2`  |
| 1698   | No file  | `fc6d04d010a2`  |
| 1690   | No file  | `fc6d04d010a2`  |
| 1685   | No file  | `fc6d04d010a2`  |
| 1680   | No file  | `fc6d04d010a2`  |
| 1674   | No file  | `fc6d04d010a2`  |
| 1668   | No file  | `fc6d04d010a2`  |
| 1659   | No file  | `fc6d04d010a2`  |
| 1649   | No file  | `fc6d04d010a2`  |
| 1642   | No file  | `fc6d04d010a2`  |
| 1636   | No file  | `fc6d04d010a2`  |
| 1628   | No file  | `fc6d04d010a2`  |
| 1622   | No file  | `fc6d04d010a2`  |
| 1614   | No file  | `fc6d04d010a2`  |
| 1608   | No file  | `fc6d04d010a2`  |
| 1602   | No file  | `fc6d04d010a2`  |
| 1598   | No file  | `fc6d04d010a2`  |
| 1594   | No file  | `fc6d04d010a2`  |
| 1590   | No file  | `fc6d04d010a2`  |
| 1587   | No file  | `fc6d04d010a2`  |
| 1584   | No file  | `fc6d04d010a2`  |
| 1579   | No file  | `fc6d04d010a2`  |
| 1572   | No file  | `fc6d04d010a2`  |
| 1565   | No file  | `fc6d04d010a2`  |
| 1559   | No file  | `fc6d04d010a2`  |
| 1554   | No file  | `fc6d04d010a2`  |
| 1547   | No file  | `fc6d04d010a2`  |
| 1537   | No file  | `fc6d04d010a2`  |
| 1529   | No file  | `fc6d04d010a2`  |
| 1524   | No file  | `fc6d04d010a2`  |
| 1519   | No file  | `fc6d04d010a2`  |
| 1509   | No file  | `fc6d04d010a2`  |
| 1506   | No file  | `fc6d04d010a2`  |
| 1504   | No file  | `fc6d04d010a2`  |
| 1500   | No file  | `fc6d04d010a2`  |
| 1493   | No file  | `fc6d04d010a2`  |
| 1489   | No file  | `fc6d04d010a2`  |
| 1485   | No file  | `fc6d04d010a2`  |
| 1481   | No file  | `fc6d04d010a2`  |
| 1474   | No file  | `fc6d04d010a2`  |
| 1466   | No file  | `fc6d04d010a2`  |
| 1462   | No file  | `fc6d04d010a2`  |
| 1459   | No file  | `fc6d04d010a2`  |
| 1453   | No file  | `fc6d04d010a2`  |
| 1450   | No file  | `fc6d04d010a2`  |
| 1445   | No file  | `fc6d04d010a2`  |
| 1439   | No file  | `fc6d04d010a2`  |
| 1433   | No file  | `fc6d04d010a2`  |
| 1430   | No file  | `fc6d04d010a2`  |
| 1426   | No file  | `fc6d04d010a2`  |
| 1421   | No file  | `fc6d04d010a2`  |
| 1417   | No file  | `fc6d04d010a2`  |
| 1416   | No file  | `fc6d04d010a2`  |
| 1409   | No file  | `fc6d04d010a2`  |
| 1405   | No file  | `fc6d04d010a2`  |
| 1401   | No file  | `fc6d04d010a2`  |
| 1396   | No file  | `fc6d04d010a2`  |
| 1391   | No file  | `fc6d04d010a2`  |
| 1390   | No file  | `fc6d04d010a2`  |
| 1386   | No file  | `fc6d04d010a2`  |
| 1381   | No file  | `fc6d04d010a2`  |
| 1379   | No file  | `fc6d04d010a2`  |
| 1372   | No file  | `fc6d04d010a2`  |
| 1366   | No file  | `fc6d04d010a2`  |
| 1364   | No file  | `fc6d04d010a2`  |
| 1363   | No file  | `fc6d04d010a2`  |
| 1360   | No file  | `fc6d04d010a2`  |
| 1358   | No file  | `fc6d04d010a2`  |
| 1355   | No file  | `fc6d04d010a2`  |
| 1351   | No file  | `fc6d04d010a2`  |
| 1348   | No file  | `fc6d04d010a2`  |
| 1346   | No file  | `fc6d04d010a2`  |
| 1341   | No file  | `fc6d04d010a2`  |
| 1340   | No file  | `fc6d04d010a2`  |
| 1338   | No file  | `fc6d04d010a2`  |
| 1335   | No file  | `fc6d04d010a2`  |
| 1333   | No file  | `fc6d04d010a2`  |
| 1329   | No file  | `fc6d04d010a2`  |
| 1327   | No file  | `fc6d04d010a2`  |
| 1324   | No file  | `fc6d04d010a2`  |
| 1321   | No file  | `fc6d04d010a2`  |
| 1319   | No file  | `fc6d04d010a2`  |
| 1318   | No file  | `fc6d04d010a2`  |
| 1316   | No file  | `fc6d04d010a2`  |
| 1313   | No file  | `fc6d04d010a2`  |
| 1311   | No file  | `fc6d04d010a2`  |
| 1309   | No file  | `fc6d04d010a2`  |
| 1304   | No file  | `fc6d04d010a2`  |
| 1292   | No file  | `fc6d04d010a2`  |
| 1286   | No file  | `fc6d04d010a2`  |
| 1280   | No file  | `fc6d04d010a2`  |
| 1276   | No file  | `fc6d04d010a2`  |
| 1267   | No file  | `fc6d04d010a2`  |
| 1261   | No file  | `fc6d04d010a2`  |
| 1256   | No file  | `fc6d04d010a2`  |
| 1250   | No file  | `fc6d04d010a2`  |
| 1246   | No file  | `fc6d04d010a2`  |
| 1239   | No file  | `fc6d04d010a2`  |
| 1230   | No file  | `fc6d04d010a2`  |
| 1226   | No file  | `fc6d04d010a2`  |
| 1220   | No file  | `fc6d04d010a2`  |
| 1217   | No file  | `fc6d04d010a2`  |
| 1211   | No file  | `fc6d04d010a2`  |
| 1210   | No file  | `fc6d04d010a2`  |
| 1208   | No file  | `fc6d04d010a2`  |
| 1203   | No file  | `fc6d04d010a2`  |
| 1197   | No file  | `fc6d04d010a2`  |
| 1194   | No file  | `fc6d04d010a2`  |
| 1192   | No file  | `fc6d04d010a2`  |
| 1187   | No file  | `fc6d04d010a2`  |
| 1183   | No file  | `fc6d04d010a2`  |
| 1177   | No file  | `fc6d04d010a2`  |
| 1173   | No file  | `fc6d04d010a2`  |
| 1167   | No file  | `fc6d04d010a2`  |
| 1164   | No file  | `fc6d04d010a2`  |
| 1156   | No file  | `fc6d04d010a2`  |
| 1149   | No file  | `fc6d04d010a2`  |
| 1144   | No file  | `fc6d04d010a2`  |
| 1137   | No file  | `fc6d04d010a2`  |
| 1132   | No file  | `fc6d04d010a2`  |
| 1127   | No file  | `fc6d04d010a2`  |
| 1122   | No file  | `fc6d04d010a2`  |
| 1118   | No file  | `fc6d04d010a2`  |
| 1114   | No file  | `fc6d04d010a2`  |
| 1109   | No file  | `fc6d04d010a2`  |
| 1102   | No file  | `fc6d04d010a2`  |
| 1096   | No file  | `fc6d04d010a2`  |
| 1088   | No file  | `fc6d04d010a2`  |
| 1081   | No file  | `fc6d04d010a2`  |
| 1076   | No file  | `fc6d04d010a2`  |
| 1069   | No file  | `fc6d04d010a2`  |
| 1064   | No file  | `fc6d04d010a2`  |
| 1058   | No file  | `fc6d04d010a2`  |
| 1051   | No file  | `fc6d04d010a2`  |
| 1044   | No file  | `fc6d04d010a2`  |
| 1036   | No file  | `fc6d04d010a2`  |
| 1026   | No file  | `fc6d04d010a2`  |
| 1016   | No file  | `fc6d04d010a2`  |
| 1009   | No file  | `fc6d04d010a2`  |
| 1005   | No file  | `fc6d04d010a2`  |
| 1000   | No file  | `fc6d04d010a2`  |
| 998    | No file  | `fc6d04d010a2`  |
| 990    | No file  | `fc6d04d010a2`  |
| 979    | No file  | `fc6d04d010a2`  |
| 972    | No file  | `fc6d04d010a2`  |
| 963    | No file  | `fc6d04d010a2`  |
| 955    | No file  | `fc6d04d010a2`  |
| 946    | No file  | `fc6d04d010a2`  |
| 938    | No file  | `fc6d04d010a2`  |
| 927    | No file  | `fc6d04d010a2`  |
| 911    | No file  | `fc6d04d010a2`  |
| 904    | No file  | `fc6d04d010a2`  |
| 899    | No file  | `fc6d04d010a2`  |
| 894    | No file  | `fc6d04d010a2`  |
| 885    | No file  | `fc6d04d010a2`  |
| 879    | No file  | `fc6d04d010a2`  |
| 872    | No file  | `fc6d04d010a2`  |
| 864    | No file  | `fc6d04d010a2`  |
| 855    | No file  | `fc6d04d010a2`  |
| 853    | No file  | `fc6d04d010a2`  |
| 845    | No file  | `fc6d04d010a2`  |
| 837    | No file  | `fc6d04d010a2`  |
| 829    | No file  | `fc6d04d010a2`  |
| 822    | No file  | `fc6d04d010a2`  |
| 814    | No file  | `fc6d04d010a2`  |
| 805    | No file  | `fc6d04d010a2`  |
| 794    | No file  | `fc6d04d010a2`  |
| 787    | No file  | `fc6d04d010a2`  |
| 780    | No file  | `fc6d04d010a2`  |
| 771    | No file  | `fc6d04d010a2`  |
| 760    | No file  | `fc6d04d010a2`  |
| 748    | No file  | `fc6d04d010a2`  |
| 741    | No file  | `fc6d04d010a2`  |
| 736    | No file  | `fc6d04d010a2`  |
| 731    | No file  | `fc6d04d010a2`  |
| 723    | No file  | `fc6d04d010a2`  |
| 711    | No file  | `fc6d04d010a2`  |
| 707    | No file  | `fc6d04d010a2`  |
| 697    | No file  | `fc6d04d010a2`  |
| 689    | No file  | `fc6d04d010a2`  |
| 683    | No file  | `fc6d04d010a2`  |
| 678    | No file  | `fc6d04d010a2`  |
| 670    | No file  | `fc6d04d010a2`  |
| 661    | No file  | `fc6d04d010a2`  |
| 656    | No file  | `fc6d04d010a2`  |
| 652    | No file  | `fc6d04d010a2`  |
| 643    | No file  | `fc6d04d010a2`  |
| 637    | No file  | `fc6d04d010a2`  |
| 630    | No file  | `fc6d04d010a2`  |
| 627    | No file  | `fc6d04d010a2`  |
| 621    | No file  | `fc6d04d010a2`  |
| 617    | No file  | `fc6d04d010a2`  |
| 615    | No file  | `fc6d04d010a2`  |
| 606    | No file  | `fc6d04d010a2`  |
| 599    | No file  | `fc6d04d010a2`  |
| 592    | No file  | `fc6d04d010a2`  |
| 586    | No file  | `fc6d04d010a2`  |
| 577    | No file  | `fc6d04d010a2`  |
| 569    | No file  | `fc6d04d010a2`  |
| 561    | No file  | `fc6d04d010a2`  |
| 554    | No file  | `fc6d04d010a2`  |
| 542    | No file  | `fc6d04d010a2`  |
| 532    | No file  | `fc6d04d010a2`  |
| 531    | No file  | `fc6d04d010a2`  |
| 526    | No file  | `fc6d04d010a2`  |
| 521    | No file  | `fc6d04d010a2`  |
| 517    | No file  | `fc6d04d010a2`  |
| 510    | No file  | `fc6d04d010a2`  |
| 508    | No file  | `fc6d04d010a2`  |
| 504    | No file  | `fc6d04d010a2`  |
| 497    | No file  | `fc6d04d010a2`  |
| 491    | No file  | `fc6d04d010a2`  |
| 485    | No file  | `fc6d04d010a2`  |
| 478    | No file  | `fc6d04d010a2`  |
| 472    | No file  | `fc6d04d010a2`  |
| 466    | No file  | `fc6d04d010a2`  |
| 457    | No file  | `fc6d04d010a2`  |
| 452    | No file  | `fc6d04d010a2`  |
| 449    | No file  | `fc6d04d010a2`  |
| 435    | No file  | `fc6d04d010a2`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Title names (LOC type 1), character names (LOC type 6) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field         | Notes                                                             |
| ------------------- | ------------ | ------------- | ----------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic         | ASCII `PABR`                                                      |
| `+0x04`             | u16          | unknown_04    | `1` on every client checked; see Open Questions                   |
| `+0x06`             | u32          | title_id      | `title.dbss` title; the handler shows its LOC type 1 name          |
| `+0x0A`             | u16          | character_key | Servant character key; the handler shows its LOC type 6 name      |
| `+0x0C`             | String Table | string_table  | See String Table                                                  |
| `string_table+0x00` | u32          | table_start   | Offset of the string table; `0x0C` on every client checked        |
| `string_table+0x04` | u32          | zero          | Always `0`                                                        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The file is newer than client 1784: no sheet of a private server's
`DataSheets.bexcel` on that client and no string of its server dump has
`CheckTitle` in the name. The two names come from the values, which agree
with each other: `2705` is a `title.dbss` title whose LOC type 1
requirement text reads "Exchange Epheria Galleon Ship License", and
`31020` is the LOC type 6 name Epheria Galleon.

## Notes

- Raw bytes on clients 2519 to 3474:
  `50 41 42 52 01 00 91 0A 00 00 2C 79 00 00 00 00 0C 00 00 00 00 00 00 00`
  (24 bytes). The file is not in the archives of clients 794 to 2107.
- No client Lua file on client 3474 has `ServantCheckTitle` or
  `CheckTitle` in a function name.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. The
  parser reads one entry and raises when the file holds more bytes.

## Open Questions

### The Leading u16

`unknown_04` is `1`. It reads as a count of (title, servant) entries,
with one entry on every client checked, or as a value of its own such as
a servant type (the Epheria Galleon is a ship). A file with two entries
would settle it.
