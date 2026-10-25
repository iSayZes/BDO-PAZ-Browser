# `itemimprovementdefaultdisplaylist.bss` Format

## Purpose

The reform stones the Gear Reform window lists by default, in order. Each
entry is a stone item ID of
[`itemimprovementsource.dbss`](../dbss/itemimprovementsource_dbss.md); the window
loads them through `ToClient_GetImprovementSourceItemCount()` and
`ToClient_GetDefaultDisplayImprovementSourceItemByIndex(index)`
(`panel_improvement_all_1`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                    | Bytes | Records        | Row bytes |
| ------ | -------------- | --------------------------------------- | ----- | -------------- | --------- |
| 1      | 1504 and later | `itemimprovementdefaultdisplaylist.bss` | 116   | 1 String Table | 4         |

| Layout | File                                    | Known          | Unknown    |
| ------ | --------------------------------------- | -------------- | ---------- |
| 1      | `itemimprovementdefaultdisplaylist.bss` | 116 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6f720d73f999`  |
| 3482   | Layout 1 | `6f720d73f999`  |
| 3474   | Layout 1 | `6f720d73f999`  |
| 3473   | Layout 1 | `6f720d73f999`  |
| 3464   | Layout 1 | `6f720d73f999`  |
| 3458   | Layout 1 | `6f720d73f999`  |
| 3454   | Layout 1 | `6f720d73f999`  |
| 3444   | Layout 1 | `6f720d73f999`  |
| 3435   | Layout 1 | `6f720d73f999`  |
| 3426   | Layout 1 | `6f720d73f999`  |
| 3418   | Layout 1 | `6f720d73f999`  |
| 3412   | Layout 1 | `6f720d73f999`  |
| 3402   | Layout 1 | `6f720d73f999`  |
| 3396   | Layout 1 | `6f720d73f999`  |
| 3387   | Layout 1 | `6f720d73f999`  |
| 3381   | Layout 1 | `6f720d73f999`  |
| 3373   | Layout 1 | `6f720d73f999`  |
| 3364   | Layout 1 | `6f720d73f999`  |
| 3356   | Layout 1 | `6f720d73f999`  |
| 3349   | Layout 1 | `6f720d73f999`  |
| 3342   | Layout 1 | `6f720d73f999`  |
| 3335   | Layout 1 | `6f720d73f999`  |
| 3326   | Layout 1 | `6f720d73f999`  |
| 3321   | Layout 1 | `6f720d73f999`  |
| 3314   | Layout 1 | `6f720d73f999`  |
| 3303   | Layout 1 | `6f720d73f999`  |
| 3302   | Layout 1 | `6f720d73f999`  |
| 3293   | Layout 1 | `6f720d73f999`  |
| 3283   | Layout 1 | `6f720d73f999`  |
| 3275   | Layout 1 | `6f720d73f999`  |
| 3267   | Layout 1 | `6f720d73f999`  |
| 3258   | Layout 1 | `6f720d73f999`  |
| 3251   | Layout 1 | `6f720d73f999`  |
| 3242   | Layout 1 | `6f720d73f999`  |
| 3235   | Layout 1 | `6f720d73f999`  |
| 3229   | Layout 1 | `6f720d73f999`  |
| 3212   | Layout 1 | `6f720d73f999`  |
| 3203   | Layout 1 | `6f720d73f999`  |
| 3193   | Layout 1 | `6f720d73f999`  |
| 3186   | Layout 1 | `6f720d73f999`  |
| 3177   | Layout 1 | `6f720d73f999`  |
| 3169   | Layout 1 | `6f720d73f999`  |
| 3158   | Layout 1 | `6f720d73f999`  |
| 3151   | Layout 1 | `6f720d73f999`  |
| 3144   | Layout 1 | `6f720d73f999`  |
| 3133   | Layout 1 | `6f720d73f999`  |
| 3125   | Layout 1 | `6f720d73f999`  |
| 3118   | Layout 1 | `6f720d73f999`  |
| 3111   | Layout 1 | `6f720d73f999`  |
| 3103   | Layout 1 | `6f720d73f999`  |
| 3095   | Layout 1 | `6f720d73f999`  |
| 3086   | Layout 1 | `6f720d73f999`  |
| 3072   | Layout 1 | `6f720d73f999`  |
| 3062   | Layout 1 | `6f720d73f999`  |
| 3052   | Layout 1 | `6f720d73f999`  |
| 3045   | Layout 1 | `6f720d73f999`  |
| 3037   | Layout 1 | `6f720d73f999`  |
| 3030   | Layout 1 | `6f720d73f999`  |
| 3021   | Layout 1 | `6f720d73f999`  |
| 3012   | Layout 1 | `6f720d73f999`  |
| 3002   | Layout 1 | `6f720d73f999`  |
| 2995   | Layout 1 | `6f720d73f999`  |
| 2987   | Layout 1 | `6f720d73f999`  |
| 2978   | Layout 1 | `6f720d73f999`  |
| 2970   | Layout 1 | `6f720d73f999`  |
| 2959   | Layout 1 | `6f720d73f999`  |
| 2951   | Layout 1 | `6f720d73f999`  |
| 2942   | Layout 1 | `6f720d73f999`  |
| 2935   | Layout 1 | `6f720d73f999`  |
| 2932   | Layout 1 | `6f720d73f999`  |
| 2923   | Layout 1 | `6f720d73f999`  |
| 2919   | Layout 1 | `6f720d73f999`  |
| 2907   | Layout 1 | `6f720d73f999`  |
| 2900   | Layout 1 | `6f720d73f999`  |
| 2891   | Layout 1 | `6f720d73f999`  |
| 2882   | Layout 1 | `6f720d73f999`  |
| 2872   | Layout 1 | `6f720d73f999`  |
| 2863   | Layout 1 | `6f720d73f999`  |
| 2855   | Layout 1 | `6f720d73f999`  |
| 2849   | Layout 1 | `6f720d73f999`  |
| 2844   | Layout 1 | `6f720d73f999`  |
| 2834   | Layout 1 | `6f720d73f999`  |
| 2825   | Layout 1 | `6f720d73f999`  |
| 2819   | Layout 1 | `6f720d73f999`  |
| 2811   | Layout 1 | `6f720d73f999`  |
| 2803   | Layout 1 | `6f720d73f999`  |
| 2794   | Layout 1 | `6f720d73f999`  |
| 2783   | Layout 1 | `6f720d73f999`  |
| 2774   | Layout 1 | `6f720d73f999`  |
| 2765   | Layout 1 | `6f720d73f999`  |
| 2756   | Layout 1 | `6f720d73f999`  |
| 2750   | Layout 1 | `6f720d73f999`  |
| 2743   | Layout 1 | `6f720d73f999`  |
| 2736   | Layout 1 | `6f720d73f999`  |
| 2726   | Layout 1 | `6f720d73f999`  |
| 2717   | Layout 1 | `6f720d73f999`  |
| 2709   | Layout 1 | `6f720d73f999`  |
| 2703   | Layout 1 | `6f720d73f999`  |
| 2695   | Layout 1 | `6f720d73f999`  |
| 2684   | Layout 1 | `6f720d73f999`  |
| 2672   | Layout 1 | `6f720d73f999`  |
| 2665   | Layout 1 | `6f720d73f999`  |
| 2657   | Layout 1 | `6f720d73f999`  |
| 2649   | Layout 1 | `6f720d73f999`  |
| 2644   | Layout 1 | `6f720d73f999`  |
| 2637   | Layout 1 | `6f720d73f999`  |
| 2629   | Layout 1 | `6f720d73f999`  |
| 2619   | Layout 1 | `6f720d73f999`  |
| 2612   | Layout 1 | `6f720d73f999`  |
| 2606   | Layout 1 | `6f720d73f999`  |
| 2602   | Layout 1 | `6f720d73f999`  |
| 2601   | Layout 1 | `6f720d73f999`  |
| 2592   | Layout 1 | `6f720d73f999`  |
| 2583   | Layout 1 | `6f720d73f999`  |
| 2575   | Layout 1 | `6f720d73f999`  |
| 2567   | Layout 1 | `6f720d73f999`  |
| 2560   | Layout 1 | `6f720d73f999`  |
| 2553   | Layout 1 | `6f720d73f999`  |
| 2545   | Layout 1 | `6f720d73f999`  |
| 2538   | Layout 1 | `6f720d73f999`  |
| 2529   | Layout 1 | `6f720d73f999`  |
| 2519   | Layout 1 | `6f720d73f999`  |
| 2513   | Layout 1 | `6f720d73f999`  |
| 2510   | Layout 1 | `6f720d73f999`  |
| 2507   | Layout 1 | `6f720d73f999`  |
| 2503   | Layout 1 | `6f720d73f999`  |
| 2498   | Layout 1 | `6f720d73f999`  |
| 2492   | Layout 1 | `6f720d73f999`  |
| 2487   | Layout 1 | `6f720d73f999`  |
| 2480   | Layout 1 | `6f720d73f999`  |
| 2474   | Layout 1 | `6f720d73f999`  |
| 2468   | Layout 1 | `6f720d73f999`  |
| 2460   | Layout 1 | `6f720d73f999`  |
| 2453   | Layout 1 | `6f720d73f999`  |
| 2444   | Layout 1 | `6f720d73f999`  |
| 2438   | Layout 1 | `6f720d73f999`  |
| 2434   | Layout 1 | `6f720d73f999`  |
| 2429   | Layout 1 | `6f720d73f999`  |
| 2421   | Layout 1 | `6f720d73f999`  |
| 2414   | Layout 1 | `6f720d73f999`  |
| 2407   | Layout 1 | `6f720d73f999`  |
| 2401   | Layout 1 | `6f720d73f999`  |
| 2397   | Layout 1 | `6f720d73f999`  |
| 2393   | Layout 1 | `6f720d73f999`  |
| 2384   | Layout 1 | `6f720d73f999`  |
| 2378   | Layout 1 | `6f720d73f999`  |
| 2372   | Layout 1 | `6f720d73f999`  |
| 2358   | Layout 1 | `6f720d73f999`  |
| 2352   | Layout 1 | `6f720d73f999`  |
| 2347   | Layout 1 | `6f720d73f999`  |
| 2343   | Layout 1 | `6f720d73f999`  |
| 2335   | Layout 1 | `6f720d73f999`  |
| 2327   | Layout 1 | `6f720d73f999`  |
| 2324   | Layout 1 | `6f720d73f999`  |
| 2319   | Layout 1 | `6f720d73f999`  |
| 2313   | Layout 1 | `6f720d73f999`  |
| 2308   | Layout 1 | `6f720d73f999`  |
| 2302   | Layout 1 | `6f720d73f999`  |
| 2295   | Layout 1 | `6f720d73f999`  |
| 2290   | Layout 1 | `6f720d73f999`  |
| 2284   | Layout 1 | `6f720d73f999`  |
| 2276   | Layout 1 | `6f720d73f999`  |
| 2269   | Layout 1 | `6f720d73f999`  |
| 2259   | Layout 1 | `6f720d73f999`  |
| 2250   | Layout 1 | `6f720d73f999`  |
| 2243   | Layout 1 | `6f720d73f999`  |
| 2235   | Layout 1 | `6f720d73f999`  |
| 2229   | Layout 1 | `6f720d73f999`  |
| 2224   | Layout 1 | `6f720d73f999`  |
| 2218   | Layout 1 | `6f720d73f999`  |
| 2215   | Layout 1 | `6f720d73f999`  |
| 2207   | Layout 1 | `6f720d73f999`  |
| 2203   | Layout 1 | `6f720d73f999`  |
| 2196   | Layout 1 | `6f720d73f999`  |
| 2192   | Layout 1 | `6f720d73f999`  |
| 2189   | Layout 1 | `6f720d73f999`  |
| 2183   | Layout 1 | `6f720d73f999`  |
| 2179   | Layout 1 | `6f720d73f999`  |
| 2171   | Layout 1 | `6f720d73f999`  |
| 2163   | Layout 1 | `6f720d73f999`  |
| 2156   | Layout 1 | `6f720d73f999`  |
| 2151   | Layout 1 | `6f720d73f999`  |
| 2147   | Layout 1 | `6f720d73f999`  |
| 2142   | Layout 1 | `6f720d73f999`  |
| 2138   | Layout 1 | `6f720d73f999`  |
| 2134   | Layout 1 | `6f720d73f999`  |
| 2130   | Layout 1 | `6f720d73f999`  |
| 2122   | Layout 1 | `6f720d73f999`  |
| 2107   | Layout 1 | `6f720d73f999`  |
| 2098   | Layout 1 | `6f720d73f999`  |
| 2089   | Layout 1 | `6f720d73f999`  |
| 2081   | Layout 1 | `6f720d73f999`  |
| 2073   | Layout 1 | `6f720d73f999`  |
| 2067   | Layout 1 | `6f720d73f999`  |
| 2063   | Layout 1 | `6f720d73f999`  |
| 2059   | Layout 1 | `6f720d73f999`  |
| 2052   | Layout 1 | `6f720d73f999`  |
| 2044   | Layout 1 | `6f720d73f999`  |
| 2039   | Layout 1 | `6f720d73f999`  |
| 2032   | Layout 1 | `6f720d73f999`  |
| 2025   | Layout 1 | `6f720d73f999`  |
| 2011   | Layout 1 | `6f720d73f999`  |
| 2005   | Layout 1 | `6f720d73f999`  |
| 2000   | Layout 1 | `6f720d73f999`  |
| 1996   | Layout 1 | `6f720d73f999`  |
| 1991   | Layout 1 | `6f720d73f999`  |
| 1985   | Layout 1 | `6f720d73f999`  |
| 1980   | Layout 1 | `6f720d73f999`  |
| 1969   | Layout 1 | `6f720d73f999`  |
| 1964   | Layout 1 | `6f720d73f999`  |
| 1958   | Layout 1 | `6f720d73f999`  |
| 1950   | Layout 1 | `6f720d73f999`  |
| 1945   | Layout 1 | `6f720d73f999`  |
| 1937   | Layout 1 | `6f720d73f999`  |
| 1933   | Layout 1 | `6f720d73f999`  |
| 1927   | Layout 1 | `6f720d73f999`  |
| 1921   | Layout 1 | `6f720d73f999`  |
| 1914   | Layout 1 | `6f720d73f999`  |
| 1908   | Layout 1 | `6f720d73f999`  |
| 1897   | Layout 1 | `6f720d73f999`  |
| 1892   | Layout 1 | `6f720d73f999`  |
| 1886   | Layout 1 | `6f720d73f999`  |
| 1881   | Layout 1 | `6f720d73f999`  |
| 1871   | Layout 1 | `6f720d73f999`  |
| 1866   | Layout 1 | `6f720d73f999`  |
| 1862   | Layout 1 | `6f720d73f999`  |
| 1854   | Layout 1 | `6f720d73f999`  |
| 1846   | Layout 1 | `6f720d73f999`  |
| 1838   | Layout 1 | `6f720d73f999`  |
| 1832   | Layout 1 | `6f720d73f999`  |
| 1826   | Layout 1 | `6f720d73f999`  |
| 1822   | Layout 1 | `6f720d73f999`  |
| 1818   | Layout 1 | `6f720d73f999`  |
| 1804   | Layout 1 | `6f720d73f999`  |
| 1794   | Layout 1 | `6f720d73f999`  |
| 1790   | Layout 1 | `6f720d73f999`  |
| 1784   | Layout 1 | `6f720d73f999`  |
| 1774   | Layout 1 | `6f720d73f999`  |
| 1771   | Layout 1 | `6f720d73f999`  |
| 1762   | Layout 1 | `6f720d73f999`  |
| 1759   | Layout 1 | `6f720d73f999`  |
| 1754   | Layout 1 | `6f720d73f999`  |
| 1749   | Layout 1 | `6f720d73f999`  |
| 1743   | Layout 1 | `6f720d73f999`  |
| 1737   | Layout 1 | `6f720d73f999`  |
| 1731   | Layout 1 | `6f720d73f999`  |
| 1725   | Layout 1 | `6f720d73f999`  |
| 1717   | Layout 1 | `6f720d73f999`  |
| 1710   | Layout 1 | `6f720d73f999`  |
| 1704   | Layout 1 | `6f720d73f999`  |
| 1698   | Layout 1 | `6f720d73f999`  |
| 1690   | Layout 1 | `6f720d73f999`  |
| 1685   | Layout 1 | `6f720d73f999`  |
| 1680   | Layout 1 | `6f720d73f999`  |
| 1674   | Layout 1 | `6f720d73f999`  |
| 1668   | Layout 1 | `6f720d73f999`  |
| 1659   | Layout 1 | `6f720d73f999`  |
| 1649   | Layout 1 | `6f720d73f999`  |
| 1642   | Layout 1 | `6f720d73f999`  |
| 1636   | Layout 1 | `6f720d73f999`  |
| 1628   | Layout 1 | `6f720d73f999`  |
| 1622   | Layout 1 | `6f720d73f999`  |
| 1614   | Layout 1 | `6f720d73f999`  |
| 1608   | Layout 1 | `6f720d73f999`  |
| 1602   | Layout 1 | `6f720d73f999`  |
| 1598   | Layout 1 | `6f720d73f999`  |
| 1594   | Layout 1 | `6f720d73f999`  |
| 1590   | Layout 1 | `6f720d73f999`  |
| 1587   | Layout 1 | `6f720d73f999`  |
| 1584   | Layout 1 | `6f720d73f999`  |
| 1579   | Layout 1 | `6f720d73f999`  |
| 1572   | Layout 1 | `6f720d73f999`  |
| 1565   | Layout 1 | `6f720d73f999`  |
| 1559   | Layout 1 | `6f720d73f999`  |
| 1554   | Layout 1 | `6f720d73f999`  |
| 1547   | Layout 1 | `6f720d73f999`  |
| 1537   | Layout 1 | `6f720d73f999`  |
| 1529   | Layout 1 | `6f720d73f999`  |
| 1524   | Layout 1 | `6f720d73f999`  |
| 1519   | Layout 1 | `6f720d73f999`  |
| 1509   | Layout 1 | `6f720d73f999`  |
| 1506   | Layout 1 | `6f720d73f999`  |
| 1504   | Layout 1 | `6f720d73f999`  |
| 1500   | No file  | `6f720d73f999`  |
| 1493   | No file  | `6f720d73f999`  |
| 1489   | No file  | `6f720d73f999`  |
| 1485   | No file  | `6f720d73f999`  |
| 1481   | No file  | `6f720d73f999`  |
| 1474   | No file  | `6f720d73f999`  |
| 1466   | No file  | `6f720d73f999`  |
| 1462   | No file  | `6f720d73f999`  |
| 1459   | No file  | `6f720d73f999`  |
| 1453   | No file  | `6f720d73f999`  |
| 1450   | No file  | `6f720d73f999`  |
| 1445   | No file  | `6f720d73f999`  |
| 1439   | No file  | `6f720d73f999`  |
| 1433   | No file  | `6f720d73f999`  |
| 1430   | No file  | `6f720d73f999`  |
| 1426   | No file  | `6f720d73f999`  |
| 1421   | No file  | `6f720d73f999`  |
| 1417   | No file  | `6f720d73f999`  |
| 1416   | No file  | `6f720d73f999`  |
| 1409   | No file  | `6f720d73f999`  |
| 1405   | No file  | `6f720d73f999`  |
| 1401   | No file  | `6f720d73f999`  |
| 1396   | No file  | `6f720d73f999`  |
| 1391   | No file  | `6f720d73f999`  |
| 1390   | No file  | `6f720d73f999`  |
| 1386   | No file  | `6f720d73f999`  |
| 1381   | No file  | `6f720d73f999`  |
| 1379   | No file  | `6f720d73f999`  |
| 1372   | No file  | `6f720d73f999`  |
| 1366   | No file  | `6f720d73f999`  |
| 1364   | No file  | `6f720d73f999`  |
| 1363   | No file  | `6f720d73f999`  |
| 1360   | No file  | `6f720d73f999`  |
| 1358   | No file  | `6f720d73f999`  |
| 1355   | No file  | `6f720d73f999`  |
| 1351   | No file  | `6f720d73f999`  |
| 1348   | No file  | `6f720d73f999`  |
| 1346   | No file  | `6f720d73f999`  |
| 1341   | No file  | `6f720d73f999`  |
| 1340   | No file  | `6f720d73f999`  |
| 1338   | No file  | `6f720d73f999`  |
| 1335   | No file  | `6f720d73f999`  |
| 1333   | No file  | `6f720d73f999`  |
| 1329   | No file  | `6f720d73f999`  |
| 1327   | No file  | `6f720d73f999`  |
| 1324   | No file  | `6f720d73f999`  |
| 1321   | No file  | `6f720d73f999`  |
| 1319   | No file  | `6f720d73f999`  |
| 1318   | No file  | `6f720d73f999`  |
| 1316   | No file  | `6f720d73f999`  |
| 1313   | No file  | `6f720d73f999`  |
| 1311   | No file  | `6f720d73f999`  |
| 1309   | No file  | `6f720d73f999`  |
| 1304   | No file  | `6f720d73f999`  |
| 1292   | No file  | `6f720d73f999`  |
| 1286   | No file  | `6f720d73f999`  |
| 1280   | No file  | `6f720d73f999`  |
| 1276   | No file  | `6f720d73f999`  |
| 1267   | No file  | `6f720d73f999`  |
| 1261   | No file  | `6f720d73f999`  |
| 1256   | No file  | `6f720d73f999`  |
| 1250   | No file  | `6f720d73f999`  |
| 1246   | No file  | `6f720d73f999`  |
| 1239   | No file  | `6f720d73f999`  |
| 1230   | No file  | `6f720d73f999`  |
| 1226   | No file  | `6f720d73f999`  |
| 1220   | No file  | `6f720d73f999`  |
| 1217   | No file  | `6f720d73f999`  |
| 1211   | No file  | `6f720d73f999`  |
| 1210   | No file  | `6f720d73f999`  |
| 1208   | No file  | `6f720d73f999`  |
| 1203   | No file  | `6f720d73f999`  |
| 1197   | No file  | `6f720d73f999`  |
| 1194   | No file  | `6f720d73f999`  |
| 1192   | No file  | `6f720d73f999`  |
| 1187   | No file  | `6f720d73f999`  |
| 1183   | No file  | `6f720d73f999`  |
| 1177   | No file  | `6f720d73f999`  |
| 1173   | No file  | `6f720d73f999`  |
| 1167   | No file  | `6f720d73f999`  |
| 1164   | No file  | `6f720d73f999`  |
| 1156   | No file  | `6f720d73f999`  |
| 1149   | No file  | `6f720d73f999`  |
| 1144   | No file  | `6f720d73f999`  |
| 1137   | No file  | `6f720d73f999`  |
| 1132   | No file  | `6f720d73f999`  |
| 1127   | No file  | `6f720d73f999`  |
| 1122   | No file  | `6f720d73f999`  |
| 1118   | No file  | `6f720d73f999`  |
| 1114   | No file  | `6f720d73f999`  |
| 1109   | No file  | `6f720d73f999`  |
| 1102   | No file  | `6f720d73f999`  |
| 1096   | No file  | `6f720d73f999`  |
| 1088   | No file  | `6f720d73f999`  |
| 1081   | No file  | `6f720d73f999`  |
| 1076   | No file  | `6f720d73f999`  |
| 1069   | No file  | `6f720d73f999`  |
| 1064   | No file  | `6f720d73f999`  |
| 1058   | No file  | `6f720d73f999`  |
| 1051   | No file  | `6f720d73f999`  |
| 1044   | No file  | `6f720d73f999`  |
| 1036   | No file  | `6f720d73f999`  |
| 1026   | No file  | `6f720d73f999`  |
| 1016   | No file  | `6f720d73f999`  |
| 1009   | No file  | `6f720d73f999`  |
| 1005   | No file  | `6f720d73f999`  |
| 1000   | No file  | `6f720d73f999`  |
| 998    | No file  | `6f720d73f999`  |
| 990    | No file  | `6f720d73f999`  |
| 979    | No file  | `6f720d73f999`  |
| 972    | No file  | `6f720d73f999`  |
| 963    | No file  | `6f720d73f999`  |
| 955    | No file  | `6f720d73f999`  |
| 946    | No file  | `6f720d73f999`  |
| 938    | No file  | `6f720d73f999`  |
| 927    | No file  | `6f720d73f999`  |
| 911    | No file  | `6f720d73f999`  |
| 904    | No file  | `6f720d73f999`  |
| 899    | No file  | `6f720d73f999`  |
| 894    | No file  | `6f720d73f999`  |
| 885    | No file  | `6f720d73f999`  |
| 879    | No file  | `6f720d73f999`  |
| 872    | No file  | `6f720d73f999`  |
| 864    | No file  | `6f720d73f999`  |
| 855    | No file  | `6f720d73f999`  |
| 853    | No file  | `6f720d73f999`  |
| 845    | No file  | `6f720d73f999`  |
| 837    | No file  | `6f720d73f999`  |
| 829    | No file  | `6f720d73f999`  |
| 822    | No file  | `6f720d73f999`  |
| 814    | No file  | `6f720d73f999`  |
| 805    | No file  | `6f720d73f999`  |
| 794    | No file  | `6f720d73f999`  |
| 787    | No file  | `6f720d73f999`  |
| 780    | No file  | `6f720d73f999`  |
| 771    | No file  | `6f720d73f999`  |
| 760    | No file  | `6f720d73f999`  |
| 748    | No file  | `6f720d73f999`  |
| 741    | No file  | `6f720d73f999`  |
| 736    | No file  | `6f720d73f999`  |
| 731    | No file  | `6f720d73f999`  |
| 723    | No file  | `6f720d73f999`  |
| 711    | No file  | `6f720d73f999`  |
| 707    | No file  | `6f720d73f999`  |
| 697    | No file  | `6f720d73f999`  |
| 689    | No file  | `6f720d73f999`  |
| 683    | No file  | `6f720d73f999`  |
| 678    | No file  | `6f720d73f999`  |
| 670    | No file  | `6f720d73f999`  |
| 661    | No file  | `6f720d73f999`  |
| 656    | No file  | `6f720d73f999`  |
| 652    | No file  | `6f720d73f999`  |
| 643    | No file  | `6f720d73f999`  |
| 637    | No file  | `6f720d73f999`  |
| 630    | No file  | `6f720d73f999`  |
| 627    | No file  | `6f720d73f999`  |
| 621    | No file  | `6f720d73f999`  |
| 617    | No file  | `6f720d73f999`  |
| 615    | No file  | `6f720d73f999`  |
| 606    | No file  | `6f720d73f999`  |
| 599    | No file  | `6f720d73f999`  |
| 592    | No file  | `6f720d73f999`  |
| 586    | No file  | `6f720d73f999`  |
| 577    | No file  | `6f720d73f999`  |
| 569    | No file  | `6f720d73f999`  |
| 561    | No file  | `6f720d73f999`  |
| 554    | No file  | `6f720d73f999`  |
| 542    | No file  | `6f720d73f999`  |
| 532    | No file  | `6f720d73f999`  |
| 531    | No file  | `6f720d73f999`  |
| 526    | No file  | `6f720d73f999`  |
| 521    | No file  | `6f720d73f999`  |
| 517    | No file  | `6f720d73f999`  |
| 510    | No file  | `6f720d73f999`  |
| 508    | No file  | `6f720d73f999`  |
| 504    | No file  | `6f720d73f999`  |
| 497    | No file  | `6f720d73f999`  |
| 491    | No file  | `6f720d73f999`  |
| 485    | No file  | `6f720d73f999`  |
| 478    | No file  | `6f720d73f999`  |
| 472    | No file  | `6f720d73f999`  |
| 466    | No file  | `6f720d73f999`  |
| 457    | No file  | `6f720d73f999`  |
| 452    | No file  | `6f720d73f999`  |
| 449    | No file  | `6f720d73f999`  |
| 435    | No file  | `6f720d73f999`  |

<!-- versions:end -->

## Companion Files

None. The stone records are in [`itemimprovementsource.dbss`](../dbss/itemimprovementsource_dbss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of u32 rows with an empty string table, read by
`u32_rows()` in `_common/pabr_strings.py`.

| Offset              | Type         | Field        | Notes                                                       |
| ------------------- | ------------ | ------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | `PABR`                                                      |
| `+0x04`             | u32          | count        | Number of stones; `24` on client 3464                       |
| `+0x08`             | u32[count]   | item_ids     | `count` stone item IDs                                      |
| `item_ids+0x00`     | String Table | string_table | Empty string table                                          |
| `string_table+0x00` | u32          | table_start  | End of the rows (`8 + 4 * count`)                           |
| `string_table+0x04` | u32          | zero         | `0`                                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Notes

- On client 3464 the 24 stones are exactly the `itemimprovementsource.dbss`
  records with `is_default_display = 1`.
