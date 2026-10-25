# `othertownnotmovableitem.bss` Format

## Purpose

Items that cannot be put into another town's storage. When the storage window
opens on a town other than the one the player stands in and the client allows
moving items there (`ToClient_ablePushOrPopOtherWareHouse`), the inventory
filter `PaGlobal_Warehouse_All_OtherTownWareHouseItemFilter`
(`panel_window_warehouse_all_2.luac`) greys out every item whose
`movableOtherTown()` is false, and every bag holding one. The file's name
matches that method, and the server message `eErrNoCanNotMovableOtherTownWareHouse`
(`stringtable.bss` sheet `SymbolNo`, LOC type 37) reads "Cannot move to
another town's storage."

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes | Records | Row bytes |
| ------ | -------------- | ----------------------------- | ----- | ------- | --------- |
| 1      | 2207 and later | `othertownnotmovableitem.bss` | 24    | 5 Entry | 4         |

| Layout | File                          | Known         | Unknown    |
| ------ | ----------------------------- | ------------- | ---------- |
| 1      | `othertownnotmovableitem.bss` | 24 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `14c851e3e012`  |
| 3482   | Layout 1 | `14c851e3e012`  |
| 3474   | Layout 1 | `14c851e3e012`  |
| 3473   | Layout 1 | `14c851e3e012`  |
| 3464   | Layout 1 | `14c851e3e012`  |
| 3458   | Layout 1 | `14c851e3e012`  |
| 3454   | Layout 1 | `14c851e3e012`  |
| 3444   | Layout 1 | `14c851e3e012`  |
| 3435   | Layout 1 | `14c851e3e012`  |
| 3426   | Layout 1 | `14c851e3e012`  |
| 3418   | Layout 1 | `14c851e3e012`  |
| 3412   | Layout 1 | `14c851e3e012`  |
| 3402   | Layout 1 | `14c851e3e012`  |
| 3396   | Layout 1 | `14c851e3e012`  |
| 3387   | Layout 1 | `14c851e3e012`  |
| 3381   | Layout 1 | `14c851e3e012`  |
| 3373   | Layout 1 | `14c851e3e012`  |
| 3364   | Layout 1 | `14c851e3e012`  |
| 3356   | Layout 1 | `14c851e3e012`  |
| 3349   | Layout 1 | `14c851e3e012`  |
| 3342   | Layout 1 | `14c851e3e012`  |
| 3335   | Layout 1 | `14c851e3e012`  |
| 3326   | Layout 1 | `14c851e3e012`  |
| 3321   | Layout 1 | `14c851e3e012`  |
| 3314   | Layout 1 | `14c851e3e012`  |
| 3303   | Layout 1 | `14c851e3e012`  |
| 3302   | Layout 1 | `14c851e3e012`  |
| 3293   | Layout 1 | `14c851e3e012`  |
| 3283   | Layout 1 | `14c851e3e012`  |
| 3275   | Layout 1 | `14c851e3e012`  |
| 3267   | Layout 1 | `14c851e3e012`  |
| 3258   | Layout 1 | `14c851e3e012`  |
| 3251   | Layout 1 | `14c851e3e012`  |
| 3242   | Layout 1 | `14c851e3e012`  |
| 3235   | Layout 1 | `14c851e3e012`  |
| 3229   | Layout 1 | `14c851e3e012`  |
| 3212   | Layout 1 | `14c851e3e012`  |
| 3203   | Layout 1 | `14c851e3e012`  |
| 3193   | Layout 1 | `14c851e3e012`  |
| 3186   | Layout 1 | `14c851e3e012`  |
| 3177   | Layout 1 | `14c851e3e012`  |
| 3169   | Layout 1 | `14c851e3e012`  |
| 3158   | Layout 1 | `14c851e3e012`  |
| 3151   | Layout 1 | `14c851e3e012`  |
| 3144   | Layout 1 | `14c851e3e012`  |
| 3133   | Layout 1 | `14c851e3e012`  |
| 3125   | Layout 1 | `14c851e3e012`  |
| 3118   | Layout 1 | `14c851e3e012`  |
| 3111   | Layout 1 | `14c851e3e012`  |
| 3103   | Layout 1 | `14c851e3e012`  |
| 3095   | Layout 1 | `14c851e3e012`  |
| 3086   | Layout 1 | `14c851e3e012`  |
| 3072   | Layout 1 | `14c851e3e012`  |
| 3062   | Layout 1 | `14c851e3e012`  |
| 3052   | Layout 1 | `14c851e3e012`  |
| 3045   | Layout 1 | `14c851e3e012`  |
| 3037   | Layout 1 | `14c851e3e012`  |
| 3030   | Layout 1 | `14c851e3e012`  |
| 3021   | Layout 1 | `14c851e3e012`  |
| 3012   | Layout 1 | `14c851e3e012`  |
| 3002   | Layout 1 | `14c851e3e012`  |
| 2995   | Layout 1 | `14c851e3e012`  |
| 2987   | Layout 1 | `14c851e3e012`  |
| 2978   | Layout 1 | `14c851e3e012`  |
| 2970   | Layout 1 | `14c851e3e012`  |
| 2959   | Layout 1 | `14c851e3e012`  |
| 2951   | Layout 1 | `14c851e3e012`  |
| 2942   | Layout 1 | `14c851e3e012`  |
| 2935   | Layout 1 | `14c851e3e012`  |
| 2932   | Layout 1 | `14c851e3e012`  |
| 2923   | Layout 1 | `14c851e3e012`  |
| 2919   | Layout 1 | `14c851e3e012`  |
| 2907   | Layout 1 | `14c851e3e012`  |
| 2900   | Layout 1 | `14c851e3e012`  |
| 2891   | Layout 1 | `14c851e3e012`  |
| 2882   | Layout 1 | `14c851e3e012`  |
| 2872   | Layout 1 | `14c851e3e012`  |
| 2863   | Layout 1 | `14c851e3e012`  |
| 2855   | Layout 1 | `14c851e3e012`  |
| 2849   | Layout 1 | `14c851e3e012`  |
| 2844   | Layout 1 | `14c851e3e012`  |
| 2834   | Layout 1 | `14c851e3e012`  |
| 2825   | Layout 1 | `14c851e3e012`  |
| 2819   | Layout 1 | `14c851e3e012`  |
| 2811   | Layout 1 | `14c851e3e012`  |
| 2803   | Layout 1 | `14c851e3e012`  |
| 2794   | Layout 1 | `14c851e3e012`  |
| 2783   | Layout 1 | `14c851e3e012`  |
| 2774   | Layout 1 | `14c851e3e012`  |
| 2765   | Layout 1 | `14c851e3e012`  |
| 2756   | Layout 1 | `14c851e3e012`  |
| 2750   | Layout 1 | `14c851e3e012`  |
| 2743   | Layout 1 | `14c851e3e012`  |
| 2736   | Layout 1 | `14c851e3e012`  |
| 2726   | Layout 1 | `14c851e3e012`  |
| 2717   | Layout 1 | `14c851e3e012`  |
| 2709   | Layout 1 | `14c851e3e012`  |
| 2703   | Layout 1 | `14c851e3e012`  |
| 2695   | Layout 1 | `14c851e3e012`  |
| 2684   | Layout 1 | `14c851e3e012`  |
| 2672   | Layout 1 | `14c851e3e012`  |
| 2665   | Layout 1 | `14c851e3e012`  |
| 2657   | Layout 1 | `14c851e3e012`  |
| 2649   | Layout 1 | `14c851e3e012`  |
| 2644   | Layout 1 | `14c851e3e012`  |
| 2637   | Layout 1 | `14c851e3e012`  |
| 2629   | Layout 1 | `14c851e3e012`  |
| 2619   | Layout 1 | `14c851e3e012`  |
| 2612   | Layout 1 | `14c851e3e012`  |
| 2606   | Layout 1 | `14c851e3e012`  |
| 2602   | Layout 1 | `14c851e3e012`  |
| 2601   | Layout 1 | `14c851e3e012`  |
| 2592   | Layout 1 | `14c851e3e012`  |
| 2583   | Layout 1 | `14c851e3e012`  |
| 2575   | Layout 1 | `14c851e3e012`  |
| 2567   | Layout 1 | `14c851e3e012`  |
| 2560   | Layout 1 | `14c851e3e012`  |
| 2553   | Layout 1 | `14c851e3e012`  |
| 2545   | Layout 1 | `14c851e3e012`  |
| 2538   | Layout 1 | `14c851e3e012`  |
| 2529   | Layout 1 | `14c851e3e012`  |
| 2519   | Layout 1 | `14c851e3e012`  |
| 2513   | Layout 1 | `14c851e3e012`  |
| 2510   | Layout 1 | `14c851e3e012`  |
| 2507   | Layout 1 | `14c851e3e012`  |
| 2503   | Layout 1 | `14c851e3e012`  |
| 2498   | Layout 1 | `14c851e3e012`  |
| 2492   | Layout 1 | `14c851e3e012`  |
| 2487   | Layout 1 | `14c851e3e012`  |
| 2480   | Layout 1 | `14c851e3e012`  |
| 2474   | Layout 1 | `14c851e3e012`  |
| 2468   | Layout 1 | `14c851e3e012`  |
| 2460   | Layout 1 | `14c851e3e012`  |
| 2453   | Layout 1 | `14c851e3e012`  |
| 2444   | Layout 1 | `14c851e3e012`  |
| 2438   | Layout 1 | `14c851e3e012`  |
| 2434   | Layout 1 | `14c851e3e012`  |
| 2429   | Layout 1 | `14c851e3e012`  |
| 2421   | Layout 1 | `14c851e3e012`  |
| 2414   | Layout 1 | `14c851e3e012`  |
| 2407   | Layout 1 | `14c851e3e012`  |
| 2401   | Layout 1 | `14c851e3e012`  |
| 2397   | Layout 1 | `14c851e3e012`  |
| 2393   | Layout 1 | `14c851e3e012`  |
| 2384   | Layout 1 | `14c851e3e012`  |
| 2378   | Layout 1 | `14c851e3e012`  |
| 2372   | Layout 1 | `14c851e3e012`  |
| 2358   | Layout 1 | `14c851e3e012`  |
| 2352   | Layout 1 | `14c851e3e012`  |
| 2347   | Layout 1 | `14c851e3e012`  |
| 2343   | Layout 1 | `14c851e3e012`  |
| 2335   | Layout 1 | `14c851e3e012`  |
| 2327   | Layout 1 | `14c851e3e012`  |
| 2324   | Layout 1 | `14c851e3e012`  |
| 2319   | Layout 1 | `14c851e3e012`  |
| 2313   | Layout 1 | `14c851e3e012`  |
| 2308   | Layout 1 | `14c851e3e012`  |
| 2302   | Layout 1 | `14c851e3e012`  |
| 2295   | Layout 1 | `14c851e3e012`  |
| 2290   | Layout 1 | `14c851e3e012`  |
| 2284   | Layout 1 | `14c851e3e012`  |
| 2276   | Layout 1 | `14c851e3e012`  |
| 2269   | Layout 1 | `14c851e3e012`  |
| 2259   | Layout 1 | `14c851e3e012`  |
| 2250   | Layout 1 | `14c851e3e012`  |
| 2243   | Layout 1 | `14c851e3e012`  |
| 2235   | Layout 1 | `14c851e3e012`  |
| 2229   | Layout 1 | `14c851e3e012`  |
| 2224   | Layout 1 | `14c851e3e012`  |
| 2218   | Layout 1 | `14c851e3e012`  |
| 2215   | Layout 1 | `14c851e3e012`  |
| 2207   | Layout 1 | `14c851e3e012`  |
| 2203   | No file  | `14c851e3e012`  |
| 2196   | No file  | `14c851e3e012`  |
| 2192   | No file  | `14c851e3e012`  |
| 2189   | No file  | `14c851e3e012`  |
| 2183   | No file  | `14c851e3e012`  |
| 2179   | No file  | `14c851e3e012`  |
| 2171   | No file  | `14c851e3e012`  |
| 2163   | No file  | `14c851e3e012`  |
| 2156   | No file  | `14c851e3e012`  |
| 2151   | No file  | `14c851e3e012`  |
| 2147   | No file  | `14c851e3e012`  |
| 2142   | No file  | `14c851e3e012`  |
| 2138   | No file  | `14c851e3e012`  |
| 2134   | No file  | `14c851e3e012`  |
| 2130   | No file  | `14c851e3e012`  |
| 2122   | No file  | `14c851e3e012`  |
| 2107   | No file  | `14c851e3e012`  |
| 2098   | No file  | `14c851e3e012`  |
| 2089   | No file  | `14c851e3e012`  |
| 2081   | No file  | `14c851e3e012`  |
| 2073   | No file  | `14c851e3e012`  |
| 2067   | No file  | `14c851e3e012`  |
| 2063   | No file  | `14c851e3e012`  |
| 2059   | No file  | `14c851e3e012`  |
| 2052   | No file  | `14c851e3e012`  |
| 2044   | No file  | `14c851e3e012`  |
| 2039   | No file  | `14c851e3e012`  |
| 2032   | No file  | `14c851e3e012`  |
| 2025   | No file  | `14c851e3e012`  |
| 2011   | No file  | `14c851e3e012`  |
| 2005   | No file  | `14c851e3e012`  |
| 2000   | No file  | `14c851e3e012`  |
| 1996   | No file  | `14c851e3e012`  |
| 1991   | No file  | `14c851e3e012`  |
| 1985   | No file  | `14c851e3e012`  |
| 1980   | No file  | `14c851e3e012`  |
| 1969   | No file  | `14c851e3e012`  |
| 1964   | No file  | `14c851e3e012`  |
| 1958   | No file  | `14c851e3e012`  |
| 1950   | No file  | `14c851e3e012`  |
| 1945   | No file  | `14c851e3e012`  |
| 1937   | No file  | `14c851e3e012`  |
| 1933   | No file  | `14c851e3e012`  |
| 1927   | No file  | `14c851e3e012`  |
| 1921   | No file  | `14c851e3e012`  |
| 1914   | No file  | `14c851e3e012`  |
| 1908   | No file  | `14c851e3e012`  |
| 1897   | No file  | `14c851e3e012`  |
| 1892   | No file  | `14c851e3e012`  |
| 1886   | No file  | `14c851e3e012`  |
| 1881   | No file  | `14c851e3e012`  |
| 1871   | No file  | `14c851e3e012`  |
| 1866   | No file  | `14c851e3e012`  |
| 1862   | No file  | `14c851e3e012`  |
| 1854   | No file  | `14c851e3e012`  |
| 1846   | No file  | `14c851e3e012`  |
| 1838   | No file  | `14c851e3e012`  |
| 1832   | No file  | `14c851e3e012`  |
| 1826   | No file  | `14c851e3e012`  |
| 1822   | No file  | `14c851e3e012`  |
| 1818   | No file  | `14c851e3e012`  |
| 1804   | No file  | `14c851e3e012`  |
| 1794   | No file  | `14c851e3e012`  |
| 1790   | No file  | `14c851e3e012`  |
| 1784   | No file  | `14c851e3e012`  |
| 1774   | No file  | `14c851e3e012`  |
| 1771   | No file  | `14c851e3e012`  |
| 1762   | No file  | `14c851e3e012`  |
| 1759   | No file  | `14c851e3e012`  |
| 1754   | No file  | `14c851e3e012`  |
| 1749   | No file  | `14c851e3e012`  |
| 1743   | No file  | `14c851e3e012`  |
| 1737   | No file  | `14c851e3e012`  |
| 1731   | No file  | `14c851e3e012`  |
| 1725   | No file  | `14c851e3e012`  |
| 1717   | No file  | `14c851e3e012`  |
| 1710   | No file  | `14c851e3e012`  |
| 1704   | No file  | `14c851e3e012`  |
| 1698   | No file  | `14c851e3e012`  |
| 1690   | No file  | `14c851e3e012`  |
| 1685   | No file  | `14c851e3e012`  |
| 1680   | No file  | `14c851e3e012`  |
| 1674   | No file  | `14c851e3e012`  |
| 1668   | No file  | `14c851e3e012`  |
| 1659   | No file  | `14c851e3e012`  |
| 1649   | No file  | `14c851e3e012`  |
| 1642   | No file  | `14c851e3e012`  |
| 1636   | No file  | `14c851e3e012`  |
| 1628   | No file  | `14c851e3e012`  |
| 1622   | No file  | `14c851e3e012`  |
| 1614   | No file  | `14c851e3e012`  |
| 1608   | No file  | `14c851e3e012`  |
| 1602   | No file  | `14c851e3e012`  |
| 1598   | No file  | `14c851e3e012`  |
| 1594   | No file  | `14c851e3e012`  |
| 1590   | No file  | `14c851e3e012`  |
| 1587   | No file  | `14c851e3e012`  |
| 1584   | No file  | `14c851e3e012`  |
| 1579   | No file  | `14c851e3e012`  |
| 1572   | No file  | `14c851e3e012`  |
| 1565   | No file  | `14c851e3e012`  |
| 1559   | No file  | `14c851e3e012`  |
| 1554   | No file  | `14c851e3e012`  |
| 1547   | No file  | `14c851e3e012`  |
| 1537   | No file  | `14c851e3e012`  |
| 1529   | No file  | `14c851e3e012`  |
| 1524   | No file  | `14c851e3e012`  |
| 1519   | No file  | `14c851e3e012`  |
| 1509   | No file  | `14c851e3e012`  |
| 1506   | No file  | `14c851e3e012`  |
| 1504   | No file  | `14c851e3e012`  |
| 1500   | No file  | `14c851e3e012`  |
| 1493   | No file  | `14c851e3e012`  |
| 1489   | No file  | `14c851e3e012`  |
| 1485   | No file  | `14c851e3e012`  |
| 1481   | No file  | `14c851e3e012`  |
| 1474   | No file  | `14c851e3e012`  |
| 1466   | No file  | `14c851e3e012`  |
| 1462   | No file  | `14c851e3e012`  |
| 1459   | No file  | `14c851e3e012`  |
| 1453   | No file  | `14c851e3e012`  |
| 1450   | No file  | `14c851e3e012`  |
| 1445   | No file  | `14c851e3e012`  |
| 1439   | No file  | `14c851e3e012`  |
| 1433   | No file  | `14c851e3e012`  |
| 1430   | No file  | `14c851e3e012`  |
| 1426   | No file  | `14c851e3e012`  |
| 1421   | No file  | `14c851e3e012`  |
| 1417   | No file  | `14c851e3e012`  |
| 1416   | No file  | `14c851e3e012`  |
| 1409   | No file  | `14c851e3e012`  |
| 1405   | No file  | `14c851e3e012`  |
| 1401   | No file  | `14c851e3e012`  |
| 1396   | No file  | `14c851e3e012`  |
| 1391   | No file  | `14c851e3e012`  |
| 1390   | No file  | `14c851e3e012`  |
| 1386   | No file  | `14c851e3e012`  |
| 1381   | No file  | `14c851e3e012`  |
| 1379   | No file  | `14c851e3e012`  |
| 1372   | No file  | `14c851e3e012`  |
| 1366   | No file  | `14c851e3e012`  |
| 1364   | No file  | `14c851e3e012`  |
| 1363   | No file  | `14c851e3e012`  |
| 1360   | No file  | `14c851e3e012`  |
| 1358   | No file  | `14c851e3e012`  |
| 1355   | No file  | `14c851e3e012`  |
| 1351   | No file  | `14c851e3e012`  |
| 1348   | No file  | `14c851e3e012`  |
| 1346   | No file  | `14c851e3e012`  |
| 1341   | No file  | `14c851e3e012`  |
| 1340   | No file  | `14c851e3e012`  |
| 1338   | No file  | `14c851e3e012`  |
| 1335   | No file  | `14c851e3e012`  |
| 1333   | No file  | `14c851e3e012`  |
| 1329   | No file  | `14c851e3e012`  |
| 1327   | No file  | `14c851e3e012`  |
| 1324   | No file  | `14c851e3e012`  |
| 1321   | No file  | `14c851e3e012`  |
| 1319   | No file  | `14c851e3e012`  |
| 1318   | No file  | `14c851e3e012`  |
| 1316   | No file  | `14c851e3e012`  |
| 1313   | No file  | `14c851e3e012`  |
| 1311   | No file  | `14c851e3e012`  |
| 1309   | No file  | `14c851e3e012`  |
| 1304   | No file  | `14c851e3e012`  |
| 1292   | No file  | `14c851e3e012`  |
| 1286   | No file  | `14c851e3e012`  |
| 1280   | No file  | `14c851e3e012`  |
| 1276   | No file  | `14c851e3e012`  |
| 1267   | No file  | `14c851e3e012`  |
| 1261   | No file  | `14c851e3e012`  |
| 1256   | No file  | `14c851e3e012`  |
| 1250   | No file  | `14c851e3e012`  |
| 1246   | No file  | `14c851e3e012`  |
| 1239   | No file  | `14c851e3e012`  |
| 1230   | No file  | `14c851e3e012`  |
| 1226   | No file  | `14c851e3e012`  |
| 1220   | No file  | `14c851e3e012`  |
| 1217   | No file  | `14c851e3e012`  |
| 1211   | No file  | `14c851e3e012`  |
| 1210   | No file  | `14c851e3e012`  |
| 1208   | No file  | `14c851e3e012`  |
| 1203   | No file  | `14c851e3e012`  |
| 1197   | No file  | `14c851e3e012`  |
| 1194   | No file  | `14c851e3e012`  |
| 1192   | No file  | `14c851e3e012`  |
| 1187   | No file  | `14c851e3e012`  |
| 1183   | No file  | `14c851e3e012`  |
| 1177   | No file  | `14c851e3e012`  |
| 1173   | No file  | `14c851e3e012`  |
| 1167   | No file  | `14c851e3e012`  |
| 1164   | No file  | `14c851e3e012`  |
| 1156   | No file  | `14c851e3e012`  |
| 1149   | No file  | `14c851e3e012`  |
| 1144   | No file  | `14c851e3e012`  |
| 1137   | No file  | `14c851e3e012`  |
| 1132   | No file  | `14c851e3e012`  |
| 1127   | No file  | `14c851e3e012`  |
| 1122   | No file  | `14c851e3e012`  |
| 1118   | No file  | `14c851e3e012`  |
| 1114   | No file  | `14c851e3e012`  |
| 1109   | No file  | `14c851e3e012`  |
| 1102   | No file  | `14c851e3e012`  |
| 1096   | No file  | `14c851e3e012`  |
| 1088   | No file  | `14c851e3e012`  |
| 1081   | No file  | `14c851e3e012`  |
| 1076   | No file  | `14c851e3e012`  |
| 1069   | No file  | `14c851e3e012`  |
| 1064   | No file  | `14c851e3e012`  |
| 1058   | No file  | `14c851e3e012`  |
| 1051   | No file  | `14c851e3e012`  |
| 1044   | No file  | `14c851e3e012`  |
| 1036   | No file  | `14c851e3e012`  |
| 1026   | No file  | `14c851e3e012`  |
| 1016   | No file  | `14c851e3e012`  |
| 1009   | No file  | `14c851e3e012`  |
| 1005   | No file  | `14c851e3e012`  |
| 1000   | No file  | `14c851e3e012`  |
| 998    | No file  | `14c851e3e012`  |
| 990    | No file  | `14c851e3e012`  |
| 979    | No file  | `14c851e3e012`  |
| 972    | No file  | `14c851e3e012`  |
| 963    | No file  | `14c851e3e012`  |
| 955    | No file  | `14c851e3e012`  |
| 946    | No file  | `14c851e3e012`  |
| 938    | No file  | `14c851e3e012`  |
| 927    | No file  | `14c851e3e012`  |
| 911    | No file  | `14c851e3e012`  |
| 904    | No file  | `14c851e3e012`  |
| 899    | No file  | `14c851e3e012`  |
| 894    | No file  | `14c851e3e012`  |
| 885    | No file  | `14c851e3e012`  |
| 879    | No file  | `14c851e3e012`  |
| 872    | No file  | `14c851e3e012`  |
| 864    | No file  | `14c851e3e012`  |
| 855    | No file  | `14c851e3e012`  |
| 853    | No file  | `14c851e3e012`  |
| 845    | No file  | `14c851e3e012`  |
| 837    | No file  | `14c851e3e012`  |
| 829    | No file  | `14c851e3e012`  |
| 822    | No file  | `14c851e3e012`  |
| 814    | No file  | `14c851e3e012`  |
| 805    | No file  | `14c851e3e012`  |
| 794    | No file  | `14c851e3e012`  |
| 787    | No file  | `14c851e3e012`  |
| 780    | No file  | `14c851e3e012`  |
| 771    | No file  | `14c851e3e012`  |
| 760    | No file  | `14c851e3e012`  |
| 748    | No file  | `14c851e3e012`  |
| 741    | No file  | `14c851e3e012`  |
| 736    | No file  | `14c851e3e012`  |
| 731    | No file  | `14c851e3e012`  |
| 723    | No file  | `14c851e3e012`  |
| 711    | No file  | `14c851e3e012`  |
| 707    | No file  | `14c851e3e012`  |
| 697    | No file  | `14c851e3e012`  |
| 689    | No file  | `14c851e3e012`  |
| 683    | No file  | `14c851e3e012`  |
| 678    | No file  | `14c851e3e012`  |
| 670    | No file  | `14c851e3e012`  |
| 661    | No file  | `14c851e3e012`  |
| 656    | No file  | `14c851e3e012`  |
| 652    | No file  | `14c851e3e012`  |
| 643    | No file  | `14c851e3e012`  |
| 637    | No file  | `14c851e3e012`  |
| 630    | No file  | `14c851e3e012`  |
| 627    | No file  | `14c851e3e012`  |
| 621    | No file  | `14c851e3e012`  |
| 617    | No file  | `14c851e3e012`  |
| 615    | No file  | `14c851e3e012`  |
| 606    | No file  | `14c851e3e012`  |
| 599    | No file  | `14c851e3e012`  |
| 592    | No file  | `14c851e3e012`  |
| 586    | No file  | `14c851e3e012`  |
| 577    | No file  | `14c851e3e012`  |
| 569    | No file  | `14c851e3e012`  |
| 561    | No file  | `14c851e3e012`  |
| 554    | No file  | `14c851e3e012`  |
| 542    | No file  | `14c851e3e012`  |
| 532    | No file  | `14c851e3e012`  |
| 531    | No file  | `14c851e3e012`  |
| 526    | No file  | `14c851e3e012`  |
| 521    | No file  | `14c851e3e012`  |
| 517    | No file  | `14c851e3e012`  |
| 510    | No file  | `14c851e3e012`  |
| 508    | No file  | `14c851e3e012`  |
| 504    | No file  | `14c851e3e012`  |
| 497    | No file  | `14c851e3e012`  |
| 491    | No file  | `14c851e3e012`  |
| 485    | No file  | `14c851e3e012`  |
| 478    | No file  | `14c851e3e012`  |
| 472    | No file  | `14c851e3e012`  |
| 466    | No file  | `14c851e3e012`  |
| 457    | No file  | `14c851e3e012`  |
| 452    | No file  | `14c851e3e012`  |
| 449    | No file  | `14c851e3e012`  |
| 435    | No file  | `14c851e3e012`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0, `str_id1` = `item_id`)    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No magic and no trailer: a count, then the entries to the end of the file.

| Offset  | Type         | Field   | Notes                                    |
| ------- | ------------ | ------- | ---------------------------------------- |
| `+0x00` | u32          | count   | Number of entries                        |
| `+0x04` | Entry[count] | entries | `count` entries of 4 bytes, ending at EOF |

### Entry (4 bytes)

| Offset  | Type | Field   | Notes                                       |
| ------- | ---- | ------- | ------------------------------------------- |
| `+0x00` | u32  | item_id | Item, as in `itemenchant.dbss`; LOC type 0  |

## Items

The five entries on client 3474, in file order:

| Item ID | Item                                  |
| ------- | ------------------------------------- |
| 65299   | Lafi Bedmountain's Upgraded Telescope |
| 59321   | Ebenruth's Nol                        |
| 16019   | Archaeologist's Map                   |
| 16016   | Lafi Bedmountain's Upgraded Compass   |
| 12034   | Rich Merchant's Ring                  |

## Notes

- The file is 24 bytes, byte for byte the same on clients 2519, 3002, 3251
  and 3474. Client 1784 has no such file, and a private server's
  `DataSheets.bexcel` on client 1784 has no sheet or column by that name.
- The entries run in falling item ID order on every client checked.
- The Lua reaches the filter only when `_ContentsGroup_ProjectAbyssOne` is
  on or the client is a console build (`isGameServiceTypeConsole()`); on the
  PC client `checkOpenWithInventoryWhenOtherTown` returns before it.
- `movableOtherTown()` is a method of the item instance, not of its static
  status, and the same filter also greys out duel copies, guild stock, trade
  goods and barter items through other checks.
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`, one row per item. `test_every_key_has_a_loc_name` in its
  `test_handler.py` asserts that every entry names an item.
- Two other Lua paths in `panel_window_warehouse_all_1.luac` move items to
  or from another town's storage through `ToClient_ablePushOrPopOtherWareHouse`
  and run on the PC client: the auto-move button for an NPC, installation or
  maid storage (`_ContentsGroup_ItemMove`), and the market-register and
  cargo-sell buttons for an NPC storage (`_ContentsGroup_SellItemInOtherWarehouse`).
  Neither calls `movableOtherTown()`. They are the paths the In-Game Check
  below tests.

## Open Questions

### Other Inputs to `movableOtherTown()`

The Lua shows only the result of `movableOtherTown()`. Whether the client
decides it from this list alone, or also from instance state such as bound or
expiring items, needs the executable of client 2519 or later. The 2016
client, the client 1485 client and server and the client 1784 server have no
other-town storage code, and their names hold no `OtherTown` string.

## In-Game Checks

### Use on the PC Client

Needs item (any one):

- [Archaeologist's Map](https://bdocodex.com/us/item/16019/)
- [Rich Merchant's Ring](https://bdocodex.com/us/item/12034/)

The Lua filter runs only on console builds and under
`_ContentsGroup_ProjectAbyssOne`. This check tests whether the PC client or
the server also blocks the listed items between towns.

1. Put the item in the storage of the town you stand in.
2. Open Transport at the storage keeper and try to send the item to another
   town's storage.
3. If Transport lists it, also try a maid's storage in another town.

The message "Cannot move to another town's storage." or a greyed-out item
means the list is checked on PC too. If the item moves, the list only applies
where the Lua filter runs.
