# `growthpassquestlist.bss` Format

## Purpose

Quest list of the Growth Pass window (`panel_window_growthpass*.luac`).

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, where the trailer starts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes | Records   | Row bytes |
| ------ | -------------- | ------------------------- | ----- | --------- | --------- |
| 1      | 1704 and later | `growthpassquestlist.bss` | 916   | 224 Entry | 4         |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 1      | `growthpassquestlist.bss` | 916 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `afa1168a92da`  |
| 3482   | Layout 1 | `afa1168a92da`  |
| 3474   | Layout 1 | `afa1168a92da`  |
| 3473   | Layout 1 | `afa1168a92da`  |
| 3464   | Layout 1 | `afa1168a92da`  |
| 3458   | Layout 1 | `afa1168a92da`  |
| 3454   | Layout 1 | `afa1168a92da`  |
| 3444   | Layout 1 | `afa1168a92da`  |
| 3435   | Layout 1 | `afa1168a92da`  |
| 3426   | Layout 1 | `afa1168a92da`  |
| 3418   | Layout 1 | `afa1168a92da`  |
| 3412   | Layout 1 | `afa1168a92da`  |
| 3402   | Layout 1 | `afa1168a92da`  |
| 3396   | Layout 1 | `afa1168a92da`  |
| 3387   | Layout 1 | `afa1168a92da`  |
| 3381   | Layout 1 | `afa1168a92da`  |
| 3373   | Layout 1 | `afa1168a92da`  |
| 3364   | Layout 1 | `afa1168a92da`  |
| 3356   | Layout 1 | `afa1168a92da`  |
| 3349   | Layout 1 | `afa1168a92da`  |
| 3342   | Layout 1 | `afa1168a92da`  |
| 3335   | Layout 1 | `afa1168a92da`  |
| 3326   | Layout 1 | `afa1168a92da`  |
| 3321   | Layout 1 | `afa1168a92da`  |
| 3314   | Layout 1 | `afa1168a92da`  |
| 3303   | Layout 1 | `afa1168a92da`  |
| 3302   | Layout 1 | `afa1168a92da`  |
| 3293   | Layout 1 | `afa1168a92da`  |
| 3283   | Layout 1 | `afa1168a92da`  |
| 3275   | Layout 1 | `afa1168a92da`  |
| 3267   | Layout 1 | `afa1168a92da`  |
| 3258   | Layout 1 | `afa1168a92da`  |
| 3251   | Layout 1 | `afa1168a92da`  |
| 3242   | Layout 1 | `afa1168a92da`  |
| 3235   | Layout 1 | `afa1168a92da`  |
| 3229   | Layout 1 | `afa1168a92da`  |
| 3212   | Layout 1 | `afa1168a92da`  |
| 3203   | Layout 1 | `afa1168a92da`  |
| 3193   | Layout 1 | `afa1168a92da`  |
| 3186   | Layout 1 | `afa1168a92da`  |
| 3177   | Layout 1 | `afa1168a92da`  |
| 3169   | Layout 1 | `afa1168a92da`  |
| 3158   | Layout 1 | `afa1168a92da`  |
| 3151   | Layout 1 | `afa1168a92da`  |
| 3144   | Layout 1 | `afa1168a92da`  |
| 3133   | Layout 1 | `afa1168a92da`  |
| 3125   | Layout 1 | `afa1168a92da`  |
| 3118   | Layout 1 | `afa1168a92da`  |
| 3111   | Layout 1 | `afa1168a92da`  |
| 3103   | Layout 1 | `afa1168a92da`  |
| 3095   | Layout 1 | `afa1168a92da`  |
| 3086   | Layout 1 | `afa1168a92da`  |
| 3072   | Layout 1 | `afa1168a92da`  |
| 3062   | Layout 1 | `afa1168a92da`  |
| 3052   | Layout 1 | `afa1168a92da`  |
| 3045   | Layout 1 | `afa1168a92da`  |
| 3037   | Layout 1 | `afa1168a92da`  |
| 3030   | Layout 1 | `afa1168a92da`  |
| 3021   | Layout 1 | `afa1168a92da`  |
| 3012   | Layout 1 | `afa1168a92da`  |
| 3002   | Layout 1 | `afa1168a92da`  |
| 2995   | Layout 1 | `afa1168a92da`  |
| 2987   | Layout 1 | `afa1168a92da`  |
| 2978   | Layout 1 | `afa1168a92da`  |
| 2970   | Layout 1 | `afa1168a92da`  |
| 2959   | Layout 1 | `afa1168a92da`  |
| 2951   | Layout 1 | `afa1168a92da`  |
| 2942   | Layout 1 | `afa1168a92da`  |
| 2935   | Layout 1 | `afa1168a92da`  |
| 2932   | Layout 1 | `afa1168a92da`  |
| 2923   | Layout 1 | `afa1168a92da`  |
| 2919   | Layout 1 | `afa1168a92da`  |
| 2907   | Layout 1 | `afa1168a92da`  |
| 2900   | Layout 1 | `afa1168a92da`  |
| 2891   | Layout 1 | `afa1168a92da`  |
| 2882   | Layout 1 | `afa1168a92da`  |
| 2872   | Layout 1 | `afa1168a92da`  |
| 2863   | Layout 1 | `afa1168a92da`  |
| 2855   | Layout 1 | `afa1168a92da`  |
| 2849   | Layout 1 | `afa1168a92da`  |
| 2844   | Layout 1 | `afa1168a92da`  |
| 2834   | Layout 1 | `afa1168a92da`  |
| 2825   | Layout 1 | `afa1168a92da`  |
| 2819   | Layout 1 | `afa1168a92da`  |
| 2811   | Layout 1 | `afa1168a92da`  |
| 2803   | Layout 1 | `afa1168a92da`  |
| 2794   | Layout 1 | `afa1168a92da`  |
| 2783   | Layout 1 | `afa1168a92da`  |
| 2774   | Layout 1 | `afa1168a92da`  |
| 2765   | Layout 1 | `afa1168a92da`  |
| 2756   | Layout 1 | `afa1168a92da`  |
| 2750   | Layout 1 | `afa1168a92da`  |
| 2743   | Layout 1 | `afa1168a92da`  |
| 2736   | Layout 1 | `afa1168a92da`  |
| 2726   | Layout 1 | `afa1168a92da`  |
| 2717   | Layout 1 | `afa1168a92da`  |
| 2709   | Layout 1 | `afa1168a92da`  |
| 2703   | Layout 1 | `afa1168a92da`  |
| 2695   | Layout 1 | `afa1168a92da`  |
| 2684   | Layout 1 | `afa1168a92da`  |
| 2672   | Layout 1 | `afa1168a92da`  |
| 2665   | Layout 1 | `afa1168a92da`  |
| 2657   | Layout 1 | `afa1168a92da`  |
| 2649   | Layout 1 | `afa1168a92da`  |
| 2644   | Layout 1 | `afa1168a92da`  |
| 2637   | Layout 1 | `afa1168a92da`  |
| 2629   | Layout 1 | `afa1168a92da`  |
| 2619   | Layout 1 | `afa1168a92da`  |
| 2612   | Layout 1 | `afa1168a92da`  |
| 2606   | Layout 1 | `afa1168a92da`  |
| 2602   | Layout 1 | `afa1168a92da`  |
| 2601   | Layout 1 | `afa1168a92da`  |
| 2592   | Layout 1 | `afa1168a92da`  |
| 2583   | Layout 1 | `afa1168a92da`  |
| 2575   | Layout 1 | `afa1168a92da`  |
| 2567   | Layout 1 | `afa1168a92da`  |
| 2560   | Layout 1 | `afa1168a92da`  |
| 2553   | Layout 1 | `afa1168a92da`  |
| 2545   | Layout 1 | `afa1168a92da`  |
| 2538   | Layout 1 | `afa1168a92da`  |
| 2529   | Layout 1 | `afa1168a92da`  |
| 2519   | Layout 1 | `afa1168a92da`  |
| 2513   | Layout 1 | `afa1168a92da`  |
| 2510   | Layout 1 | `afa1168a92da`  |
| 2507   | Layout 1 | `afa1168a92da`  |
| 2503   | Layout 1 | `afa1168a92da`  |
| 2498   | Layout 1 | `afa1168a92da`  |
| 2492   | Layout 1 | `afa1168a92da`  |
| 2487   | Layout 1 | `afa1168a92da`  |
| 2480   | Layout 1 | `afa1168a92da`  |
| 2474   | Layout 1 | `afa1168a92da`  |
| 2468   | Layout 1 | `afa1168a92da`  |
| 2460   | Layout 1 | `afa1168a92da`  |
| 2453   | Layout 1 | `afa1168a92da`  |
| 2444   | Layout 1 | `afa1168a92da`  |
| 2438   | Layout 1 | `afa1168a92da`  |
| 2434   | Layout 1 | `afa1168a92da`  |
| 2429   | Layout 1 | `afa1168a92da`  |
| 2421   | Layout 1 | `afa1168a92da`  |
| 2414   | Layout 1 | `afa1168a92da`  |
| 2407   | Layout 1 | `afa1168a92da`  |
| 2401   | Layout 1 | `afa1168a92da`  |
| 2397   | Layout 1 | `afa1168a92da`  |
| 2393   | Layout 1 | `afa1168a92da`  |
| 2384   | Layout 1 | `afa1168a92da`  |
| 2378   | Layout 1 | `afa1168a92da`  |
| 2372   | Layout 1 | `afa1168a92da`  |
| 2358   | Layout 1 | `afa1168a92da`  |
| 2352   | Layout 1 | `afa1168a92da`  |
| 2347   | Layout 1 | `afa1168a92da`  |
| 2343   | Layout 1 | `afa1168a92da`  |
| 2335   | Layout 1 | `afa1168a92da`  |
| 2327   | Layout 1 | `afa1168a92da`  |
| 2324   | Layout 1 | `afa1168a92da`  |
| 2319   | Layout 1 | `afa1168a92da`  |
| 2313   | Layout 1 | `afa1168a92da`  |
| 2308   | Layout 1 | `afa1168a92da`  |
| 2302   | Layout 1 | `afa1168a92da`  |
| 2295   | Layout 1 | `afa1168a92da`  |
| 2290   | Layout 1 | `afa1168a92da`  |
| 2284   | Layout 1 | `afa1168a92da`  |
| 2276   | Layout 1 | `afa1168a92da`  |
| 2269   | Layout 1 | `afa1168a92da`  |
| 2259   | Layout 1 | `afa1168a92da`  |
| 2250   | Layout 1 | `afa1168a92da`  |
| 2243   | Layout 1 | `afa1168a92da`  |
| 2235   | Layout 1 | `afa1168a92da`  |
| 2229   | Layout 1 | `afa1168a92da`  |
| 2224   | Layout 1 | `afa1168a92da`  |
| 2218   | Layout 1 | `afa1168a92da`  |
| 2215   | Layout 1 | `afa1168a92da`  |
| 2207   | Layout 1 | `afa1168a92da`  |
| 2203   | Layout 1 | `afa1168a92da`  |
| 2196   | Layout 1 | `afa1168a92da`  |
| 2192   | Layout 1 | `afa1168a92da`  |
| 2189   | Layout 1 | `afa1168a92da`  |
| 2183   | Layout 1 | `afa1168a92da`  |
| 2179   | Layout 1 | `afa1168a92da`  |
| 2171   | Layout 1 | `afa1168a92da`  |
| 2163   | Layout 1 | `afa1168a92da`  |
| 2156   | Layout 1 | `afa1168a92da`  |
| 2151   | Layout 1 | `afa1168a92da`  |
| 2147   | Layout 1 | `afa1168a92da`  |
| 2142   | Layout 1 | `afa1168a92da`  |
| 2138   | Layout 1 | `afa1168a92da`  |
| 2134   | Layout 1 | `afa1168a92da`  |
| 2130   | Layout 1 | `afa1168a92da`  |
| 2122   | Layout 1 | `afa1168a92da`  |
| 2107   | Layout 1 | `afa1168a92da`  |
| 2098   | Layout 1 | `afa1168a92da`  |
| 2089   | Layout 1 | `afa1168a92da`  |
| 2081   | Layout 1 | `afa1168a92da`  |
| 2073   | Layout 1 | `afa1168a92da`  |
| 2067   | Layout 1 | `afa1168a92da`  |
| 2063   | Layout 1 | `afa1168a92da`  |
| 2059   | Layout 1 | `afa1168a92da`  |
| 2052   | Layout 1 | `afa1168a92da`  |
| 2044   | Layout 1 | `afa1168a92da`  |
| 2039   | Layout 1 | `afa1168a92da`  |
| 2032   | Layout 1 | `afa1168a92da`  |
| 2025   | Layout 1 | `afa1168a92da`  |
| 2011   | Layout 1 | `afa1168a92da`  |
| 2005   | Layout 1 | `afa1168a92da`  |
| 2000   | Layout 1 | `afa1168a92da`  |
| 1996   | Layout 1 | `afa1168a92da`  |
| 1991   | Layout 1 | `afa1168a92da`  |
| 1985   | Layout 1 | `afa1168a92da`  |
| 1980   | Layout 1 | `afa1168a92da`  |
| 1969   | Layout 1 | `afa1168a92da`  |
| 1964   | Layout 1 | `afa1168a92da`  |
| 1958   | Layout 1 | `afa1168a92da`  |
| 1950   | Layout 1 | `afa1168a92da`  |
| 1945   | Layout 1 | `afa1168a92da`  |
| 1937   | Layout 1 | `afa1168a92da`  |
| 1933   | Layout 1 | `afa1168a92da`  |
| 1927   | Layout 1 | `afa1168a92da`  |
| 1921   | Layout 1 | `afa1168a92da`  |
| 1914   | Layout 1 | `afa1168a92da`  |
| 1908   | Layout 1 | `afa1168a92da`  |
| 1897   | Layout 1 | `afa1168a92da`  |
| 1892   | Layout 1 | `afa1168a92da`  |
| 1886   | Layout 1 | `afa1168a92da`  |
| 1881   | Layout 1 | `afa1168a92da`  |
| 1871   | Layout 1 | `afa1168a92da`  |
| 1866   | Layout 1 | `afa1168a92da`  |
| 1862   | Layout 1 | `afa1168a92da`  |
| 1854   | Layout 1 | `afa1168a92da`  |
| 1846   | Layout 1 | `afa1168a92da`  |
| 1838   | Layout 1 | `afa1168a92da`  |
| 1832   | Layout 1 | `afa1168a92da`  |
| 1826   | Layout 1 | `afa1168a92da`  |
| 1822   | Layout 1 | `afa1168a92da`  |
| 1818   | Layout 1 | `afa1168a92da`  |
| 1804   | Layout 1 | `afa1168a92da`  |
| 1794   | Layout 1 | `afa1168a92da`  |
| 1790   | Layout 1 | `afa1168a92da`  |
| 1784   | Layout 1 | `afa1168a92da`  |
| 1774   | Layout 1 | `afa1168a92da`  |
| 1771   | Layout 1 | `afa1168a92da`  |
| 1762   | Layout 1 | `afa1168a92da`  |
| 1759   | Layout 1 | `afa1168a92da`  |
| 1754   | Layout 1 | `afa1168a92da`  |
| 1749   | Layout 1 | `afa1168a92da`  |
| 1743   | Layout 1 | `afa1168a92da`  |
| 1737   | Layout 1 | `afa1168a92da`  |
| 1731   | Layout 1 | `afa1168a92da`  |
| 1725   | Layout 1 | `afa1168a92da`  |
| 1717   | Layout 1 | `afa1168a92da`  |
| 1710   | Layout 1 | `afa1168a92da`  |
| 1704   | Layout 1 | `afa1168a92da`  |
| 1698   | No file  | `afa1168a92da`  |
| 1690   | No file  | `afa1168a92da`  |
| 1685   | No file  | `afa1168a92da`  |
| 1680   | No file  | `afa1168a92da`  |
| 1674   | No file  | `afa1168a92da`  |
| 1668   | No file  | `afa1168a92da`  |
| 1659   | No file  | `afa1168a92da`  |
| 1649   | No file  | `afa1168a92da`  |
| 1642   | No file  | `afa1168a92da`  |
| 1636   | No file  | `afa1168a92da`  |
| 1628   | No file  | `afa1168a92da`  |
| 1622   | No file  | `afa1168a92da`  |
| 1614   | No file  | `afa1168a92da`  |
| 1608   | No file  | `afa1168a92da`  |
| 1602   | No file  | `afa1168a92da`  |
| 1598   | No file  | `afa1168a92da`  |
| 1594   | No file  | `afa1168a92da`  |
| 1590   | No file  | `afa1168a92da`  |
| 1587   | No file  | `afa1168a92da`  |
| 1584   | No file  | `afa1168a92da`  |
| 1579   | No file  | `afa1168a92da`  |
| 1572   | No file  | `afa1168a92da`  |
| 1565   | No file  | `afa1168a92da`  |
| 1559   | No file  | `afa1168a92da`  |
| 1554   | No file  | `afa1168a92da`  |
| 1547   | No file  | `afa1168a92da`  |
| 1537   | No file  | `afa1168a92da`  |
| 1529   | No file  | `afa1168a92da`  |
| 1524   | No file  | `afa1168a92da`  |
| 1519   | No file  | `afa1168a92da`  |
| 1509   | No file  | `afa1168a92da`  |
| 1506   | No file  | `afa1168a92da`  |
| 1504   | No file  | `afa1168a92da`  |
| 1500   | No file  | `afa1168a92da`  |
| 1493   | No file  | `afa1168a92da`  |
| 1489   | No file  | `afa1168a92da`  |
| 1485   | No file  | `afa1168a92da`  |
| 1481   | No file  | `afa1168a92da`  |
| 1474   | No file  | `afa1168a92da`  |
| 1466   | No file  | `afa1168a92da`  |
| 1462   | No file  | `afa1168a92da`  |
| 1459   | No file  | `afa1168a92da`  |
| 1453   | No file  | `afa1168a92da`  |
| 1450   | No file  | `afa1168a92da`  |
| 1445   | No file  | `afa1168a92da`  |
| 1439   | No file  | `afa1168a92da`  |
| 1433   | No file  | `afa1168a92da`  |
| 1430   | No file  | `afa1168a92da`  |
| 1426   | No file  | `afa1168a92da`  |
| 1421   | No file  | `afa1168a92da`  |
| 1417   | No file  | `afa1168a92da`  |
| 1416   | No file  | `afa1168a92da`  |
| 1409   | No file  | `afa1168a92da`  |
| 1405   | No file  | `afa1168a92da`  |
| 1401   | No file  | `afa1168a92da`  |
| 1396   | No file  | `afa1168a92da`  |
| 1391   | No file  | `afa1168a92da`  |
| 1390   | No file  | `afa1168a92da`  |
| 1386   | No file  | `afa1168a92da`  |
| 1381   | No file  | `afa1168a92da`  |
| 1379   | No file  | `afa1168a92da`  |
| 1372   | No file  | `afa1168a92da`  |
| 1366   | No file  | `afa1168a92da`  |
| 1364   | No file  | `afa1168a92da`  |
| 1363   | No file  | `afa1168a92da`  |
| 1360   | No file  | `afa1168a92da`  |
| 1358   | No file  | `afa1168a92da`  |
| 1355   | No file  | `afa1168a92da`  |
| 1351   | No file  | `afa1168a92da`  |
| 1348   | No file  | `afa1168a92da`  |
| 1346   | No file  | `afa1168a92da`  |
| 1341   | No file  | `afa1168a92da`  |
| 1340   | No file  | `afa1168a92da`  |
| 1338   | No file  | `afa1168a92da`  |
| 1335   | No file  | `afa1168a92da`  |
| 1333   | No file  | `afa1168a92da`  |
| 1329   | No file  | `afa1168a92da`  |
| 1327   | No file  | `afa1168a92da`  |
| 1324   | No file  | `afa1168a92da`  |
| 1321   | No file  | `afa1168a92da`  |
| 1319   | No file  | `afa1168a92da`  |
| 1318   | No file  | `afa1168a92da`  |
| 1316   | No file  | `afa1168a92da`  |
| 1313   | No file  | `afa1168a92da`  |
| 1311   | No file  | `afa1168a92da`  |
| 1309   | No file  | `afa1168a92da`  |
| 1304   | No file  | `afa1168a92da`  |
| 1292   | No file  | `afa1168a92da`  |
| 1286   | No file  | `afa1168a92da`  |
| 1280   | No file  | `afa1168a92da`  |
| 1276   | No file  | `afa1168a92da`  |
| 1267   | No file  | `afa1168a92da`  |
| 1261   | No file  | `afa1168a92da`  |
| 1256   | No file  | `afa1168a92da`  |
| 1250   | No file  | `afa1168a92da`  |
| 1246   | No file  | `afa1168a92da`  |
| 1239   | No file  | `afa1168a92da`  |
| 1230   | No file  | `afa1168a92da`  |
| 1226   | No file  | `afa1168a92da`  |
| 1220   | No file  | `afa1168a92da`  |
| 1217   | No file  | `afa1168a92da`  |
| 1211   | No file  | `afa1168a92da`  |
| 1210   | No file  | `afa1168a92da`  |
| 1208   | No file  | `afa1168a92da`  |
| 1203   | No file  | `afa1168a92da`  |
| 1197   | No file  | `afa1168a92da`  |
| 1194   | No file  | `afa1168a92da`  |
| 1192   | No file  | `afa1168a92da`  |
| 1187   | No file  | `afa1168a92da`  |
| 1183   | No file  | `afa1168a92da`  |
| 1177   | No file  | `afa1168a92da`  |
| 1173   | No file  | `afa1168a92da`  |
| 1167   | No file  | `afa1168a92da`  |
| 1164   | No file  | `afa1168a92da`  |
| 1156   | No file  | `afa1168a92da`  |
| 1149   | No file  | `afa1168a92da`  |
| 1144   | No file  | `afa1168a92da`  |
| 1137   | No file  | `afa1168a92da`  |
| 1132   | No file  | `afa1168a92da`  |
| 1127   | No file  | `afa1168a92da`  |
| 1122   | No file  | `afa1168a92da`  |
| 1118   | No file  | `afa1168a92da`  |
| 1114   | No file  | `afa1168a92da`  |
| 1109   | No file  | `afa1168a92da`  |
| 1102   | No file  | `afa1168a92da`  |
| 1096   | No file  | `afa1168a92da`  |
| 1088   | No file  | `afa1168a92da`  |
| 1081   | No file  | `afa1168a92da`  |
| 1076   | No file  | `afa1168a92da`  |
| 1069   | No file  | `afa1168a92da`  |
| 1064   | No file  | `afa1168a92da`  |
| 1058   | No file  | `afa1168a92da`  |
| 1051   | No file  | `afa1168a92da`  |
| 1044   | No file  | `afa1168a92da`  |
| 1036   | No file  | `afa1168a92da`  |
| 1026   | No file  | `afa1168a92da`  |
| 1016   | No file  | `afa1168a92da`  |
| 1009   | No file  | `afa1168a92da`  |
| 1005   | No file  | `afa1168a92da`  |
| 1000   | No file  | `afa1168a92da`  |
| 998    | No file  | `afa1168a92da`  |
| 990    | No file  | `afa1168a92da`  |
| 979    | No file  | `afa1168a92da`  |
| 972    | No file  | `afa1168a92da`  |
| 963    | No file  | `afa1168a92da`  |
| 955    | No file  | `afa1168a92da`  |
| 946    | No file  | `afa1168a92da`  |
| 938    | No file  | `afa1168a92da`  |
| 927    | No file  | `afa1168a92da`  |
| 911    | No file  | `afa1168a92da`  |
| 904    | No file  | `afa1168a92da`  |
| 899    | No file  | `afa1168a92da`  |
| 894    | No file  | `afa1168a92da`  |
| 885    | No file  | `afa1168a92da`  |
| 879    | No file  | `afa1168a92da`  |
| 872    | No file  | `afa1168a92da`  |
| 864    | No file  | `afa1168a92da`  |
| 855    | No file  | `afa1168a92da`  |
| 853    | No file  | `afa1168a92da`  |
| 845    | No file  | `afa1168a92da`  |
| 837    | No file  | `afa1168a92da`  |
| 829    | No file  | `afa1168a92da`  |
| 822    | No file  | `afa1168a92da`  |
| 814    | No file  | `afa1168a92da`  |
| 805    | No file  | `afa1168a92da`  |
| 794    | No file  | `afa1168a92da`  |
| 787    | No file  | `afa1168a92da`  |
| 780    | No file  | `afa1168a92da`  |
| 771    | No file  | `afa1168a92da`  |
| 760    | No file  | `afa1168a92da`  |
| 748    | No file  | `afa1168a92da`  |
| 741    | No file  | `afa1168a92da`  |
| 736    | No file  | `afa1168a92da`  |
| 731    | No file  | `afa1168a92da`  |
| 723    | No file  | `afa1168a92da`  |
| 711    | No file  | `afa1168a92da`  |
| 707    | No file  | `afa1168a92da`  |
| 697    | No file  | `afa1168a92da`  |
| 689    | No file  | `afa1168a92da`  |
| 683    | No file  | `afa1168a92da`  |
| 678    | No file  | `afa1168a92da`  |
| 670    | No file  | `afa1168a92da`  |
| 661    | No file  | `afa1168a92da`  |
| 656    | No file  | `afa1168a92da`  |
| 652    | No file  | `afa1168a92da`  |
| 643    | No file  | `afa1168a92da`  |
| 637    | No file  | `afa1168a92da`  |
| 630    | No file  | `afa1168a92da`  |
| 627    | No file  | `afa1168a92da`  |
| 621    | No file  | `afa1168a92da`  |
| 617    | No file  | `afa1168a92da`  |
| 615    | No file  | `afa1168a92da`  |
| 606    | No file  | `afa1168a92da`  |
| 599    | No file  | `afa1168a92da`  |
| 592    | No file  | `afa1168a92da`  |
| 586    | No file  | `afa1168a92da`  |
| 577    | No file  | `afa1168a92da`  |
| 569    | No file  | `afa1168a92da`  |
| 561    | No file  | `afa1168a92da`  |
| 554    | No file  | `afa1168a92da`  |
| 542    | No file  | `afa1168a92da`  |
| 532    | No file  | `afa1168a92da`  |
| 531    | No file  | `afa1168a92da`  |
| 526    | No file  | `afa1168a92da`  |
| 521    | No file  | `afa1168a92da`  |
| 517    | No file  | `afa1168a92da`  |
| 510    | No file  | `afa1168a92da`  |
| 508    | No file  | `afa1168a92da`  |
| 504    | No file  | `afa1168a92da`  |
| 497    | No file  | `afa1168a92da`  |
| 491    | No file  | `afa1168a92da`  |
| 485    | No file  | `afa1168a92da`  |
| 478    | No file  | `afa1168a92da`  |
| 472    | No file  | `afa1168a92da`  |
| 466    | No file  | `afa1168a92da`  |
| 457    | No file  | `afa1168a92da`  |
| 452    | No file  | `afa1168a92da`  |
| 449    | No file  | `afa1168a92da`  |
| 435    | No file  | `afa1168a92da`  |

<!-- versions:end -->

## Companion Files

The same as [`allquestlist.bss`](allquestlist_bss.md).

All multi-byte values are little-endian.

## Quest Chains

On client 3464 the list holds 224 quests in nine chains, 4464 to 4472, and every quest of those chains that `allquestlist.bss` has. Some chains skip sub IDs (4471 runs to 47 with 20 quests); the skipped ones are not in `quest.dbss` either. Titles open with a topic tag such as `[Main]`, `[Buffs]`, `[Worker]`, `[Quest]`, `[Menu]` or `[Olvia Academy]`.

| Chain (client 3464) | Quests | Quest 1                                                 |
| ------------------- | ------ | ------------------------------------------------------- |
| 4464                | 28     | [Main] Complete Embarking on an Adventure               |
| 4465                | 28     | [Buffs] Eat a Simple Cron Meal                          |
| 4466                | 28     | [Buffs] Eat a Seafood Cron Meal                         |
| 4467                | 26     | [Worker] Hire a Worker in Velia and Check Worker List   |
| 4468                | 25     | [Quest] Complete Bee Hurts Farm                         |
| 4469                | 16     | [Quest] Complete Have You Ever... Tamed a Horse?        |
| 4470                | 40     | [Menu] Chat Groups                                      |
| 4471                | 20     | [Quest] Complete Old Moon Guild's Trade Offer           |
| 4472                | 13     | [Olvia Academy] Academy Enrollment                      |

The window does not read this list by index. It walks the categories of [`growthpasscategory.dbss`](growthpasscategory_dbss.md) and places each quest in a grid cell of the category's layout in [`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md). Each category names one quest chain, and its grid holds that chain's quests. On client 3464 only two chains have a category: 4470 (category 7, Game Tips, quests 1 to 40) and 4472 (category 9, HYPERBOOST, quests 1 to 13). The other seven chains are in this list with no category or grid. LOC type 107 still names categories 1 to 9.

## Notes

- Decompressed size on client 3464: `916` bytes, `8 + 224 * 4 + 12`.
- calpheonlabs (`growthpassquestlist.bss.mdx`) reads the same layout: a u32-counted array of (u16 quest group, u16 quest number) and a 12-byte pad.
- `test_pass_lists.py` checks this file next to the three [Black Spirit Pass lists](seasonpassquestlist_bss.md).
