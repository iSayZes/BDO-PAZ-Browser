# `siegemercenarylimitcount.bss` Format

## Purpose

How many War Heroes (hired guild mercenaries, `전장의 영웅`) a guild can
bring into a Node War or Conquest War, one u32 per siege stage. The seven
values sit in the slot where a PABR table keeps its record count, followed
by an empty string table. On client 3474 they are `0, 0, 0, 3, 3, 3, 5`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | -------------- | --------- |
| 1      | 1754 and later | 3483    | `siegemercenarylimitcount.bss` | 44    | 1 String Table | 4         |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `siegemercenarylimitcount.bss` | 44 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `b55e26257f06`  |
| 3482   | Layout 1 | `b55e26257f06`  |
| 3474   | Layout 1 | `b55e26257f06`  |
| 3473   | Layout 1 | `b55e26257f06`  |
| 3464   | Layout 1 | `b55e26257f06`  |
| 3458   | Layout 1 | `b55e26257f06`  |
| 3454   | Layout 1 | `b55e26257f06`  |
| 3444   | Layout 1 | `b55e26257f06`  |
| 3435   | Layout 1 | `b55e26257f06`  |
| 3426   | Layout 1 | `b55e26257f06`  |
| 3418   | Layout 1 | `b55e26257f06`  |
| 3412   | Layout 1 | `b55e26257f06`  |
| 3402   | Layout 1 | `b55e26257f06`  |
| 3396   | Layout 1 | `b55e26257f06`  |
| 3387   | Layout 1 | `b55e26257f06`  |
| 3381   | Layout 1 | `b55e26257f06`  |
| 3373   | Layout 1 | `b55e26257f06`  |
| 3364   | Layout 1 | `b55e26257f06`  |
| 3356   | Layout 1 | `b55e26257f06`  |
| 3349   | Layout 1 | `b55e26257f06`  |
| 3342   | Layout 1 | `b55e26257f06`  |
| 3335   | Layout 1 | `b55e26257f06`  |
| 3326   | Layout 1 | `b55e26257f06`  |
| 3321   | Layout 1 | `b55e26257f06`  |
| 3314   | Layout 1 | `b55e26257f06`  |
| 3303   | Layout 1 | `b55e26257f06`  |
| 3302   | Layout 1 | `b55e26257f06`  |
| 3293   | Layout 1 | `b55e26257f06`  |
| 3283   | Layout 1 | `b55e26257f06`  |
| 3275   | Layout 1 | `b55e26257f06`  |
| 3267   | Layout 1 | `b55e26257f06`  |
| 3258   | Layout 1 | `b55e26257f06`  |
| 3251   | Layout 1 | `b55e26257f06`  |
| 3242   | Layout 1 | `b55e26257f06`  |
| 3235   | Layout 1 | `b55e26257f06`  |
| 3229   | Layout 1 | `b55e26257f06`  |
| 3212   | Layout 1 | `b55e26257f06`  |
| 3203   | Layout 1 | `b55e26257f06`  |
| 3193   | Layout 1 | `b55e26257f06`  |
| 3186   | Layout 1 | `b55e26257f06`  |
| 3177   | Layout 1 | `b55e26257f06`  |
| 3169   | Layout 1 | `b55e26257f06`  |
| 3158   | Layout 1 | `b55e26257f06`  |
| 3151   | Layout 1 | `b55e26257f06`  |
| 3144   | Layout 1 | `b55e26257f06`  |
| 3133   | Layout 1 | `b55e26257f06`  |
| 3125   | Layout 1 | `b55e26257f06`  |
| 3118   | Layout 1 | `b55e26257f06`  |
| 3111   | Layout 1 | `b55e26257f06`  |
| 3103   | Layout 1 | `b55e26257f06`  |
| 3095   | Layout 1 | `b55e26257f06`  |
| 3086   | Layout 1 | `b55e26257f06`  |
| 3072   | Layout 1 | `b55e26257f06`  |
| 3062   | Layout 1 | `b55e26257f06`  |
| 3052   | Layout 1 | `b55e26257f06`  |
| 3045   | Layout 1 | `b55e26257f06`  |
| 3037   | Layout 1 | `b55e26257f06`  |
| 3030   | Layout 1 | `b55e26257f06`  |
| 3021   | Layout 1 | `b55e26257f06`  |
| 3012   | Layout 1 | `b55e26257f06`  |
| 3002   | Layout 1 | `b55e26257f06`  |
| 2995   | Layout 1 | `b55e26257f06`  |
| 2987   | Layout 1 | `b55e26257f06`  |
| 2978   | Layout 1 | `b55e26257f06`  |
| 2970   | Layout 1 | `b55e26257f06`  |
| 2959   | Layout 1 | `b55e26257f06`  |
| 2951   | Layout 1 | `b55e26257f06`  |
| 2942   | Layout 1 | `b55e26257f06`  |
| 2935   | Layout 1 | `b55e26257f06`  |
| 2932   | Layout 1 | `b55e26257f06`  |
| 2923   | Layout 1 | `b55e26257f06`  |
| 2919   | Layout 1 | `b55e26257f06`  |
| 2907   | Layout 1 | `b55e26257f06`  |
| 2900   | Layout 1 | `b55e26257f06`  |
| 2891   | Layout 1 | `b55e26257f06`  |
| 2882   | Layout 1 | `b55e26257f06`  |
| 2872   | Layout 1 | `b55e26257f06`  |
| 2863   | Layout 1 | `b55e26257f06`  |
| 2855   | Layout 1 | `b55e26257f06`  |
| 2849   | Layout 1 | `b55e26257f06`  |
| 2844   | Layout 1 | `b55e26257f06`  |
| 2834   | Layout 1 | `b55e26257f06`  |
| 2825   | Layout 1 | `b55e26257f06`  |
| 2819   | Layout 1 | `b55e26257f06`  |
| 2811   | Layout 1 | `b55e26257f06`  |
| 2803   | Layout 1 | `b55e26257f06`  |
| 2794   | Layout 1 | `b55e26257f06`  |
| 2783   | Layout 1 | `b55e26257f06`  |
| 2774   | Layout 1 | `b55e26257f06`  |
| 2765   | Layout 1 | `b55e26257f06`  |
| 2756   | Layout 1 | `b55e26257f06`  |
| 2750   | Layout 1 | `b55e26257f06`  |
| 2743   | Layout 1 | `b55e26257f06`  |
| 2736   | Layout 1 | `b55e26257f06`  |
| 2726   | Layout 1 | `b55e26257f06`  |
| 2717   | Layout 1 | `b55e26257f06`  |
| 2709   | Layout 1 | `b55e26257f06`  |
| 2703   | Layout 1 | `b55e26257f06`  |
| 2695   | Layout 1 | `b55e26257f06`  |
| 2684   | Layout 1 | `b55e26257f06`  |
| 2672   | Layout 1 | `b55e26257f06`  |
| 2665   | Layout 1 | `b55e26257f06`  |
| 2657   | Layout 1 | `b55e26257f06`  |
| 2649   | Layout 1 | `b55e26257f06`  |
| 2644   | Layout 1 | `b55e26257f06`  |
| 2637   | Layout 1 | `b55e26257f06`  |
| 2629   | Layout 1 | `b55e26257f06`  |
| 2619   | Layout 1 | `b55e26257f06`  |
| 2612   | Layout 1 | `b55e26257f06`  |
| 2606   | Layout 1 | `b55e26257f06`  |
| 2602   | Layout 1 | `b55e26257f06`  |
| 2601   | Layout 1 | `b55e26257f06`  |
| 2592   | Layout 1 | `b55e26257f06`  |
| 2583   | Layout 1 | `b55e26257f06`  |
| 2575   | Layout 1 | `b55e26257f06`  |
| 2567   | Layout 1 | `b55e26257f06`  |
| 2560   | Layout 1 | `b55e26257f06`  |
| 2553   | Layout 1 | `b55e26257f06`  |
| 2545   | Layout 1 | `b55e26257f06`  |
| 2538   | Layout 1 | `b55e26257f06`  |
| 2529   | Layout 1 | `b55e26257f06`  |
| 2519   | Layout 1 | `b55e26257f06`  |
| 2513   | Layout 1 | `b55e26257f06`  |
| 2510   | Layout 1 | `b55e26257f06`  |
| 2507   | Layout 1 | `b55e26257f06`  |
| 2503   | Layout 1 | `b55e26257f06`  |
| 2498   | Layout 1 | `b55e26257f06`  |
| 2492   | Layout 1 | `b55e26257f06`  |
| 2487   | Layout 1 | `b55e26257f06`  |
| 2480   | Layout 1 | `b55e26257f06`  |
| 2474   | Layout 1 | `b55e26257f06`  |
| 2468   | Layout 1 | `b55e26257f06`  |
| 2460   | Layout 1 | `b55e26257f06`  |
| 2453   | Layout 1 | `b55e26257f06`  |
| 2444   | Layout 1 | `b55e26257f06`  |
| 2438   | Layout 1 | `b55e26257f06`  |
| 2434   | Layout 1 | `b55e26257f06`  |
| 2429   | Layout 1 | `b55e26257f06`  |
| 2421   | Layout 1 | `b55e26257f06`  |
| 2414   | Layout 1 | `b55e26257f06`  |
| 2407   | Layout 1 | `b55e26257f06`  |
| 2401   | Layout 1 | `b55e26257f06`  |
| 2397   | Layout 1 | `b55e26257f06`  |
| 2393   | Layout 1 | `b55e26257f06`  |
| 2384   | Layout 1 | `b55e26257f06`  |
| 2378   | Layout 1 | `b55e26257f06`  |
| 2372   | Layout 1 | `b55e26257f06`  |
| 2358   | Layout 1 | `b55e26257f06`  |
| 2352   | Layout 1 | `b55e26257f06`  |
| 2347   | Layout 1 | `b55e26257f06`  |
| 2343   | Layout 1 | `b55e26257f06`  |
| 2335   | Layout 1 | `b55e26257f06`  |
| 2327   | Layout 1 | `b55e26257f06`  |
| 2324   | Layout 1 | `b55e26257f06`  |
| 2319   | Layout 1 | `b55e26257f06`  |
| 2313   | Layout 1 | `b55e26257f06`  |
| 2308   | Layout 1 | `b55e26257f06`  |
| 2302   | Layout 1 | `b55e26257f06`  |
| 2295   | Layout 1 | `b55e26257f06`  |
| 2290   | Layout 1 | `b55e26257f06`  |
| 2284   | Layout 1 | `b55e26257f06`  |
| 2276   | Layout 1 | `b55e26257f06`  |
| 2269   | Layout 1 | `b55e26257f06`  |
| 2259   | Layout 1 | `b55e26257f06`  |
| 2250   | Layout 1 | `b55e26257f06`  |
| 2243   | Layout 1 | `b55e26257f06`  |
| 2235   | Layout 1 | `b55e26257f06`  |
| 2229   | Layout 1 | `b55e26257f06`  |
| 2224   | Layout 1 | `b55e26257f06`  |
| 2218   | Layout 1 | `b55e26257f06`  |
| 2215   | Layout 1 | `b55e26257f06`  |
| 2207   | Layout 1 | `b55e26257f06`  |
| 2203   | Layout 1 | `b55e26257f06`  |
| 2196   | Layout 1 | `b55e26257f06`  |
| 2192   | Layout 1 | `b55e26257f06`  |
| 2189   | Layout 1 | `b55e26257f06`  |
| 2183   | Layout 1 | `b55e26257f06`  |
| 2179   | Layout 1 | `b55e26257f06`  |
| 2171   | Layout 1 | `b55e26257f06`  |
| 2163   | Layout 1 | `b55e26257f06`  |
| 2156   | Layout 1 | `b55e26257f06`  |
| 2151   | Layout 1 | `b55e26257f06`  |
| 2147   | Layout 1 | `b55e26257f06`  |
| 2142   | Layout 1 | `b55e26257f06`  |
| 2138   | Layout 1 | `b55e26257f06`  |
| 2134   | Layout 1 | `b55e26257f06`  |
| 2130   | Layout 1 | `b55e26257f06`  |
| 2122   | Layout 1 | `b55e26257f06`  |
| 2107   | Layout 1 | `b55e26257f06`  |
| 2098   | Layout 1 | `b55e26257f06`  |
| 2089   | Layout 1 | `b55e26257f06`  |
| 2081   | Layout 1 | `b55e26257f06`  |
| 2073   | Layout 1 | `b55e26257f06`  |
| 2067   | Layout 1 | `b55e26257f06`  |
| 2063   | Layout 1 | `b55e26257f06`  |
| 2059   | Layout 1 | `b55e26257f06`  |
| 2052   | Layout 1 | `b55e26257f06`  |
| 2044   | Layout 1 | `b55e26257f06`  |
| 2039   | Layout 1 | `b55e26257f06`  |
| 2032   | Layout 1 | `b55e26257f06`  |
| 2025   | Layout 1 | `b55e26257f06`  |
| 2011   | Layout 1 | `b55e26257f06`  |
| 2005   | Layout 1 | `b55e26257f06`  |
| 2000   | Layout 1 | `b55e26257f06`  |
| 1996   | Layout 1 | `b55e26257f06`  |
| 1991   | Layout 1 | `b55e26257f06`  |
| 1985   | Layout 1 | `b55e26257f06`  |
| 1980   | Layout 1 | `b55e26257f06`  |
| 1969   | Layout 1 | `b55e26257f06`  |
| 1964   | Layout 1 | `b55e26257f06`  |
| 1958   | Layout 1 | `b55e26257f06`  |
| 1950   | Layout 1 | `b55e26257f06`  |
| 1945   | Layout 1 | `b55e26257f06`  |
| 1937   | Layout 1 | `b55e26257f06`  |
| 1933   | Layout 1 | `b55e26257f06`  |
| 1927   | Layout 1 | `b55e26257f06`  |
| 1921   | Layout 1 | `b55e26257f06`  |
| 1914   | Layout 1 | `b55e26257f06`  |
| 1908   | Layout 1 | `b55e26257f06`  |
| 1897   | Layout 1 | `b55e26257f06`  |
| 1892   | Layout 1 | `b55e26257f06`  |
| 1886   | Layout 1 | `b55e26257f06`  |
| 1881   | Layout 1 | `b55e26257f06`  |
| 1871   | Layout 1 | `b55e26257f06`  |
| 1866   | Layout 1 | `b55e26257f06`  |
| 1862   | Layout 1 | `b55e26257f06`  |
| 1854   | Layout 1 | `b55e26257f06`  |
| 1846   | Layout 1 | `b55e26257f06`  |
| 1838   | Layout 1 | `b55e26257f06`  |
| 1832   | Layout 1 | `b55e26257f06`  |
| 1826   | Layout 1 | `b55e26257f06`  |
| 1822   | Layout 1 | `b55e26257f06`  |
| 1818   | Layout 1 | `b55e26257f06`  |
| 1804   | Layout 1 | `b55e26257f06`  |
| 1794   | Layout 1 | `b55e26257f06`  |
| 1790   | Layout 1 | `b55e26257f06`  |
| 1784   | Layout 1 | `b55e26257f06`  |
| 1774   | Layout 1 | `b55e26257f06`  |
| 1771   | Layout 1 | `b55e26257f06`  |
| 1762   | Layout 1 | `b55e26257f06`  |
| 1759   | Layout 1 | `b55e26257f06`  |
| 1754   | Layout 1 | `b55e26257f06`  |
| 1749   | No file  | `b55e26257f06`  |
| 1743   | No file  | `b55e26257f06`  |
| 1737   | No file  | `b55e26257f06`  |
| 1731   | No file  | `b55e26257f06`  |
| 1725   | No file  | `b55e26257f06`  |
| 1717   | No file  | `b55e26257f06`  |
| 1710   | No file  | `b55e26257f06`  |
| 1704   | No file  | `b55e26257f06`  |
| 1698   | No file  | `b55e26257f06`  |
| 1690   | No file  | `b55e26257f06`  |
| 1685   | No file  | `b55e26257f06`  |
| 1680   | No file  | `b55e26257f06`  |
| 1674   | No file  | `b55e26257f06`  |
| 1668   | No file  | `b55e26257f06`  |
| 1659   | No file  | `b55e26257f06`  |
| 1649   | No file  | `b55e26257f06`  |
| 1642   | No file  | `b55e26257f06`  |
| 1636   | No file  | `b55e26257f06`  |
| 1628   | No file  | `b55e26257f06`  |
| 1622   | No file  | `b55e26257f06`  |
| 1614   | No file  | `b55e26257f06`  |
| 1608   | No file  | `b55e26257f06`  |
| 1602   | No file  | `b55e26257f06`  |
| 1598   | No file  | `b55e26257f06`  |
| 1594   | No file  | `b55e26257f06`  |
| 1590   | No file  | `b55e26257f06`  |
| 1587   | No file  | `b55e26257f06`  |
| 1584   | No file  | `b55e26257f06`  |
| 1579   | No file  | `b55e26257f06`  |
| 1572   | No file  | `b55e26257f06`  |
| 1565   | No file  | `b55e26257f06`  |
| 1559   | No file  | `b55e26257f06`  |
| 1554   | No file  | `b55e26257f06`  |
| 1547   | No file  | `b55e26257f06`  |
| 1537   | No file  | `b55e26257f06`  |
| 1529   | No file  | `b55e26257f06`  |
| 1524   | No file  | `b55e26257f06`  |
| 1519   | No file  | `b55e26257f06`  |
| 1509   | No file  | `b55e26257f06`  |
| 1506   | No file  | `b55e26257f06`  |
| 1504   | No file  | `b55e26257f06`  |
| 1500   | No file  | `b55e26257f06`  |
| 1493   | No file  | `b55e26257f06`  |
| 1489   | No file  | `b55e26257f06`  |
| 1485   | No file  | `b55e26257f06`  |
| 1481   | No file  | `b55e26257f06`  |
| 1474   | No file  | `b55e26257f06`  |
| 1466   | No file  | `b55e26257f06`  |
| 1462   | No file  | `b55e26257f06`  |
| 1459   | No file  | `b55e26257f06`  |
| 1453   | No file  | `b55e26257f06`  |
| 1450   | No file  | `b55e26257f06`  |
| 1445   | No file  | `b55e26257f06`  |
| 1439   | No file  | `b55e26257f06`  |
| 1433   | No file  | `b55e26257f06`  |
| 1430   | No file  | `b55e26257f06`  |
| 1426   | No file  | `b55e26257f06`  |
| 1421   | No file  | `b55e26257f06`  |
| 1417   | No file  | `b55e26257f06`  |
| 1416   | No file  | `b55e26257f06`  |
| 1409   | No file  | `b55e26257f06`  |
| 1405   | No file  | `b55e26257f06`  |
| 1401   | No file  | `b55e26257f06`  |
| 1396   | No file  | `b55e26257f06`  |
| 1391   | No file  | `b55e26257f06`  |
| 1390   | No file  | `b55e26257f06`  |
| 1386   | No file  | `b55e26257f06`  |
| 1381   | No file  | `b55e26257f06`  |
| 1379   | No file  | `b55e26257f06`  |
| 1372   | No file  | `b55e26257f06`  |
| 1366   | No file  | `b55e26257f06`  |
| 1364   | No file  | `b55e26257f06`  |
| 1363   | No file  | `b55e26257f06`  |
| 1360   | No file  | `b55e26257f06`  |
| 1358   | No file  | `b55e26257f06`  |
| 1355   | No file  | `b55e26257f06`  |
| 1351   | No file  | `b55e26257f06`  |
| 1348   | No file  | `b55e26257f06`  |
| 1346   | No file  | `b55e26257f06`  |
| 1341   | No file  | `b55e26257f06`  |
| 1340   | No file  | `b55e26257f06`  |
| 1338   | No file  | `b55e26257f06`  |
| 1335   | No file  | `b55e26257f06`  |
| 1333   | No file  | `b55e26257f06`  |
| 1329   | No file  | `b55e26257f06`  |
| 1327   | No file  | `b55e26257f06`  |
| 1324   | No file  | `b55e26257f06`  |
| 1321   | No file  | `b55e26257f06`  |
| 1319   | No file  | `b55e26257f06`  |
| 1318   | No file  | `b55e26257f06`  |
| 1316   | No file  | `b55e26257f06`  |
| 1313   | No file  | `b55e26257f06`  |
| 1311   | No file  | `b55e26257f06`  |
| 1309   | No file  | `b55e26257f06`  |
| 1304   | No file  | `b55e26257f06`  |
| 1292   | No file  | `b55e26257f06`  |
| 1286   | No file  | `b55e26257f06`  |
| 1280   | No file  | `b55e26257f06`  |
| 1276   | No file  | `b55e26257f06`  |
| 1267   | No file  | `b55e26257f06`  |
| 1261   | No file  | `b55e26257f06`  |
| 1256   | No file  | `b55e26257f06`  |
| 1250   | No file  | `b55e26257f06`  |
| 1246   | No file  | `b55e26257f06`  |
| 1239   | No file  | `b55e26257f06`  |
| 1230   | No file  | `b55e26257f06`  |
| 1226   | No file  | `b55e26257f06`  |
| 1220   | No file  | `b55e26257f06`  |
| 1217   | No file  | `b55e26257f06`  |
| 1211   | No file  | `b55e26257f06`  |
| 1210   | No file  | `b55e26257f06`  |
| 1208   | No file  | `b55e26257f06`  |
| 1203   | No file  | `b55e26257f06`  |
| 1197   | No file  | `b55e26257f06`  |
| 1194   | No file  | `b55e26257f06`  |
| 1192   | No file  | `b55e26257f06`  |
| 1187   | No file  | `b55e26257f06`  |
| 1183   | No file  | `b55e26257f06`  |
| 1177   | No file  | `b55e26257f06`  |
| 1173   | No file  | `b55e26257f06`  |
| 1167   | No file  | `b55e26257f06`  |
| 1164   | No file  | `b55e26257f06`  |
| 1156   | No file  | `b55e26257f06`  |
| 1149   | No file  | `b55e26257f06`  |
| 1144   | No file  | `b55e26257f06`  |
| 1137   | No file  | `b55e26257f06`  |
| 1132   | No file  | `b55e26257f06`  |
| 1127   | No file  | `b55e26257f06`  |
| 1122   | No file  | `b55e26257f06`  |
| 1118   | No file  | `b55e26257f06`  |
| 1114   | No file  | `b55e26257f06`  |
| 1109   | No file  | `b55e26257f06`  |
| 1102   | No file  | `b55e26257f06`  |
| 1096   | No file  | `b55e26257f06`  |
| 1088   | No file  | `b55e26257f06`  |
| 1081   | No file  | `b55e26257f06`  |
| 1076   | No file  | `b55e26257f06`  |
| 1069   | No file  | `b55e26257f06`  |
| 1064   | No file  | `b55e26257f06`  |
| 1058   | No file  | `b55e26257f06`  |
| 1051   | No file  | `b55e26257f06`  |
| 1044   | No file  | `b55e26257f06`  |
| 1036   | No file  | `b55e26257f06`  |
| 1026   | No file  | `b55e26257f06`  |
| 1016   | No file  | `b55e26257f06`  |
| 1009   | No file  | `b55e26257f06`  |
| 1005   | No file  | `b55e26257f06`  |
| 1000   | No file  | `b55e26257f06`  |
| 998    | No file  | `b55e26257f06`  |
| 990    | No file  | `b55e26257f06`  |
| 979    | No file  | `b55e26257f06`  |
| 972    | No file  | `b55e26257f06`  |
| 963    | No file  | `b55e26257f06`  |
| 955    | No file  | `b55e26257f06`  |
| 946    | No file  | `b55e26257f06`  |
| 938    | No file  | `b55e26257f06`  |
| 927    | No file  | `b55e26257f06`  |
| 911    | No file  | `b55e26257f06`  |
| 904    | No file  | `b55e26257f06`  |
| 899    | No file  | `b55e26257f06`  |
| 894    | No file  | `b55e26257f06`  |
| 885    | No file  | `b55e26257f06`  |
| 879    | No file  | `b55e26257f06`  |
| 872    | No file  | `b55e26257f06`  |
| 864    | No file  | `b55e26257f06`  |
| 855    | No file  | `b55e26257f06`  |
| 853    | No file  | `b55e26257f06`  |
| 845    | No file  | `b55e26257f06`  |
| 837    | No file  | `b55e26257f06`  |
| 829    | No file  | `b55e26257f06`  |
| 822    | No file  | `b55e26257f06`  |
| 814    | No file  | `b55e26257f06`  |
| 805    | No file  | `b55e26257f06`  |
| 794    | No file  | `b55e26257f06`  |
| 787    | No file  | `b55e26257f06`  |
| 780    | No file  | `b55e26257f06`  |
| 771    | No file  | `b55e26257f06`  |
| 760    | No file  | `b55e26257f06`  |
| 748    | No file  | `b55e26257f06`  |
| 741    | No file  | `b55e26257f06`  |
| 736    | No file  | `b55e26257f06`  |
| 731    | No file  | `b55e26257f06`  |
| 723    | No file  | `b55e26257f06`  |
| 711    | No file  | `b55e26257f06`  |
| 707    | No file  | `b55e26257f06`  |
| 697    | No file  | `b55e26257f06`  |
| 689    | No file  | `b55e26257f06`  |
| 683    | No file  | `b55e26257f06`  |
| 678    | No file  | `b55e26257f06`  |
| 670    | No file  | `b55e26257f06`  |
| 661    | No file  | `b55e26257f06`  |
| 656    | No file  | `b55e26257f06`  |
| 652    | No file  | `b55e26257f06`  |
| 643    | No file  | `b55e26257f06`  |
| 637    | No file  | `b55e26257f06`  |
| 630    | No file  | `b55e26257f06`  |
| 627    | No file  | `b55e26257f06`  |
| 621    | No file  | `b55e26257f06`  |
| 617    | No file  | `b55e26257f06`  |
| 615    | No file  | `b55e26257f06`  |
| 606    | No file  | `b55e26257f06`  |
| 599    | No file  | `b55e26257f06`  |
| 592    | No file  | `b55e26257f06`  |
| 586    | No file  | `b55e26257f06`  |
| 577    | No file  | `b55e26257f06`  |
| 569    | No file  | `b55e26257f06`  |
| 561    | No file  | `b55e26257f06`  |
| 554    | No file  | `b55e26257f06`  |
| 542    | No file  | `b55e26257f06`  |
| 532    | No file  | `b55e26257f06`  |
| 531    | No file  | `b55e26257f06`  |
| 526    | No file  | `b55e26257f06`  |
| 521    | No file  | `b55e26257f06`  |
| 517    | No file  | `b55e26257f06`  |
| 510    | No file  | `b55e26257f06`  |
| 508    | No file  | `b55e26257f06`  |
| 504    | No file  | `b55e26257f06`  |
| 497    | No file  | `b55e26257f06`  |
| 491    | No file  | `b55e26257f06`  |
| 485    | No file  | `b55e26257f06`  |
| 478    | No file  | `b55e26257f06`  |
| 472    | No file  | `b55e26257f06`  |
| 466    | No file  | `b55e26257f06`  |
| 457    | No file  | `b55e26257f06`  |
| 452    | No file  | `b55e26257f06`  |
| 449    | No file  | `b55e26257f06`  |
| 435    | No file  | `b55e26257f06`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field         | Notes                                                      |
| ------------------- | ------------ | ------------- | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic         | ASCII `PABR`                                               |
| `+0x04`             | u32          | siege_stage_0 | War Hero limit of stage 0; see Siege Stages                |
| `+0x08`             | u32          | siege_stage_1 | War Hero limit of stage 1                                  |
| `+0x0C`             | u32          | siege_stage_2 | War Hero limit of stage 2                                  |
| `+0x10`             | u32          | siege_stage_3 | War Hero limit of stage 3                                  |
| `+0x14`             | u32          | siege_stage_4 | War Hero limit of stage 4                                  |
| `+0x18`             | u32          | siege_stage_5 | War Hero limit of stage 5                                  |
| `+0x1C`             | u32          | siege_stage_6 | War Hero limit of stage 6                                  |
| `+0x20`             | String Table | string_table  | See String Table                                           |
| `string_table+0x00` | u32          | table_start   | Offset of the string table; `0x20` on every client checked |
| `string_table+0x04` | u32          | zero          | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Siege Stages

The stage of each field comes from the developer comments on the
`SiegeStage_0` to `SiegeStage_6` columns of the `SiegeMercenaryLimitCount`
sheet in a private server's `datasheet_siegedatatable.xlsm` on client 1784.
Each comment reads "the number of War Heroes (mercenaries) that can take
part, per Node War stage and in the Conquest War; a guild can hire more,
but no more than this number can join the war". The client's English word
for `단계` is "Tier" (`LUA_NODEGRADE_1`, `2단계`, is "Tier 2"). The preview
labels its columns with these client 1784 stages.

| Field           | Stage on client 1784 (comment)  | Client 1784 to 2519 | Clients 3002 to 3474 |
| --------------- | ------------------------------- | ------------------- | -------------------- |
| `siege_stage_0` | Node War Tier 1 Beginner (`거점전 1단계 초급`) | `0` | `0` |
| `siege_stage_1` | Node War Tier 1 Intermediate (`거점전 1단계 중급`) | `0` | `0` |
| `siege_stage_2` | Node War Tier 1 Advanced (`거점전 1단계 상급`) | `0` | `0` |
| `siege_stage_3` | Node War Tier 2 (`거점전 2단계`) | `3` | `3` |
| `siege_stage_4` | Node War Tier 3 (`거점전 3단계`) | `4` | `3` |
| `siege_stage_5` | Node War Tier 4 (`거점전 4단계`) | `5` | `3` |
| `siege_stage_6` | Conquest War (`점령전`)         | `5` | `5` |

## Field Names

The field names are the `SiegeStage_0` to `SiegeStage_6` columns of the
`SiegeMercenaryLimitCount` sheet in a private server's `DataSheets.bexcel`
on client 1784. The sheet has one row per `PA_GAME_SERVICE_TYPE`; every row
with values (JPN, RUS, NA, TW, SA, TH, ID, TR, GT and CS) holds
`<null>, <null>, <null>, 3, 4, 5, 5`, and a `<null>` compiles to `0`. All 7
of 7 columns match the client 1784 file by value, and that client's file is
byte for byte the private server's compiled `binary/siegemercenarylimitcount.bss`.
The server dump on client 1784 has the sheet name `SiegeMercenaryLimitCount`
and the column format `SiegeStage_%d` as UTF-16 strings.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 03 00 00 00 03 00 00 00 05 00 00 00 00 00 00 00 20 00 00 00 00 00 00 00`
  (44 bytes).
- Clients 1784, 2107 and 2519 hold `0, 0, 0, 3, 4, 5, 5`; clients 3002, 3251
  and 3474 hold `0, 0, 0, 3, 3, 3, 5`. The file is not in the archives of
  clients 794, 1230 and 1485.
- The node tooltip on client 3474 (`panel_worldmap_nodetooltip_villagewar_all_1.luac`,
  `new_worldmap_actortooltip.luac`) shows "Max War Heroes: {count}"
  (`LUA_WORLDMAP_ACTORTOOLTIP_GUILDMAXMECENARY`) from
  `siegeTerritoryOptionWrapper._limitVolunteerCount` or
  `regionWrapper:getSiegeGuildVolunteerLimitCount()`. The second is a per
  region value: `SiegeGuildVolunteerLimitCount` is a column of the
  `SiegeOptionByRegion` and `SiegeOptionRegion` sheets on client 1784, not
  of this file.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`.

## Open Questions

### Stages on the Live Client

The stage of each field comes from the client 1784 sheet comments. The
client 3474 string table has Node War tiers `LUA_NODEGRADE_0` to
`LUA_NODEGRADE_4` ("Tier 1" to "Tier 5") and Conquest tiers
`LUA_NODEGRADE2_1` to `LUA_NODEGRADE2_3`, and no client Lua function on
client 3474 has `SiegeStage` or `MercenaryLimit` in its name. Whether `siege_stage_0` to `siege_stage_6`
still stand for the same seven stages on client 3474 is unknown.
