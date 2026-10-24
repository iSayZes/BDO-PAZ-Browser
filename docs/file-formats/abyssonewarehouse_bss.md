# `abyssonewarehouse.bss` Format

## Purpose

The town storages of the Magnus (`AbyssOne` in the client's names): one
row per town region with the knowledge entry of its area, an Abyssal Vein
(`Abyssal Veins - Serendia` for Heidel and Glish) or `The Magnus` itself
(Velia, Olvia, Iliya Island and Oquilla's Eye on client 3482). The file
has no PABR magic. The client opens a Magnus storage with the
`FromClient_AbyssOneWarehouseOpenNak(warehouseName)` message
`LUA_ABYSSONE_WAREHOUSE_OPEN_TITLE` (`nakmessage_warehouse_clear_all.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 2      | 2207 and later | 3483    | `abyssonewarehouse.bss` | 202   | 33 Row  | 6         |
| 1      | 2011 to 2203   | 2203    | `abyssonewarehouse.bss` | 260   | 22 Row  | 6         |

| Layout | File                    | Known          | Unknown    |
| ------ | ----------------------- | -------------- | ---------- |
| 2      | `abyssonewarehouse.bss` | 202 B (100.0%) | 0 B (0.0%) |
| 1      | `abyssonewarehouse.bss` | 260 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `636a8a313b03`  |
| 3482   | Layout 2 | `636a8a313b03`  |
| 3474   | Layout 2 | `636a8a313b03`  |
| 3473   | Layout 2 | `636a8a313b03`  |
| 3464   | Layout 2 | `636a8a313b03`  |
| 3458   | Layout 2 | `636a8a313b03`  |
| 3454   | Layout 2 | `636a8a313b03`  |
| 3444   | Layout 2 | `636a8a313b03`  |
| 3435   | Layout 2 | `636a8a313b03`  |
| 3426   | Layout 2 | `636a8a313b03`  |
| 3418   | Layout 2 | `636a8a313b03`  |
| 3412   | Layout 2 | `636a8a313b03`  |
| 3402   | Layout 2 | `636a8a313b03`  |
| 3396   | Layout 2 | `636a8a313b03`  |
| 3387   | Layout 2 | `636a8a313b03`  |
| 3381   | Layout 2 | `636a8a313b03`  |
| 3373   | Layout 2 | `636a8a313b03`  |
| 3364   | Layout 2 | `636a8a313b03`  |
| 3356   | Layout 2 | `636a8a313b03`  |
| 3349   | Layout 2 | `636a8a313b03`  |
| 3342   | Layout 2 | `636a8a313b03`  |
| 3335   | Layout 2 | `636a8a313b03`  |
| 3326   | Layout 2 | `636a8a313b03`  |
| 3321   | Layout 2 | `636a8a313b03`  |
| 3314   | Layout 2 | `636a8a313b03`  |
| 3303   | Layout 2 | `636a8a313b03`  |
| 3302   | Layout 2 | `636a8a313b03`  |
| 3293   | Layout 2 | `636a8a313b03`  |
| 3283   | Layout 2 | `636a8a313b03`  |
| 3275   | Layout 2 | `636a8a313b03`  |
| 3267   | Layout 2 | `636a8a313b03`  |
| 3258   | Layout 2 | `636a8a313b03`  |
| 3251   | Layout 2 | `636a8a313b03`  |
| 3242   | Layout 2 | `636a8a313b03`  |
| 3235   | Layout 2 | `636a8a313b03`  |
| 3229   | Layout 2 | `636a8a313b03`  |
| 3212   | Layout 2 | `636a8a313b03`  |
| 3203   | Layout 2 | `636a8a313b03`  |
| 3193   | Layout 2 | `636a8a313b03`  |
| 3186   | Layout 2 | `636a8a313b03`  |
| 3177   | Layout 2 | `636a8a313b03`  |
| 3169   | Layout 2 | `636a8a313b03`  |
| 3158   | Layout 2 | `636a8a313b03`  |
| 3151   | Layout 2 | `636a8a313b03`  |
| 3144   | Layout 2 | `636a8a313b03`  |
| 3133   | Layout 2 | `636a8a313b03`  |
| 3125   | Layout 2 | `636a8a313b03`  |
| 3118   | Layout 2 | `636a8a313b03`  |
| 3111   | Layout 2 | `636a8a313b03`  |
| 3103   | Layout 2 | `636a8a313b03`  |
| 3095   | Layout 2 | `636a8a313b03`  |
| 3086   | Layout 2 | `636a8a313b03`  |
| 3072   | Layout 2 | `636a8a313b03`  |
| 3062   | Layout 2 | `636a8a313b03`  |
| 3052   | Layout 2 | `636a8a313b03`  |
| 3045   | Layout 2 | `636a8a313b03`  |
| 3037   | Layout 2 | `636a8a313b03`  |
| 3030   | Layout 2 | `636a8a313b03`  |
| 3021   | Layout 2 | `636a8a313b03`  |
| 3012   | Layout 2 | `636a8a313b03`  |
| 3002   | Layout 2 | `636a8a313b03`  |
| 2995   | Layout 2 | `636a8a313b03`  |
| 2987   | Layout 2 | `636a8a313b03`  |
| 2978   | Layout 2 | `636a8a313b03`  |
| 2970   | Layout 2 | `636a8a313b03`  |
| 2959   | Layout 2 | `636a8a313b03`  |
| 2951   | Layout 2 | `636a8a313b03`  |
| 2942   | Layout 2 | `636a8a313b03`  |
| 2935   | Layout 2 | `636a8a313b03`  |
| 2932   | Layout 2 | `636a8a313b03`  |
| 2923   | Layout 2 | `636a8a313b03`  |
| 2919   | Layout 2 | `636a8a313b03`  |
| 2907   | Layout 2 | `636a8a313b03`  |
| 2900   | Layout 2 | `636a8a313b03`  |
| 2891   | Layout 2 | `636a8a313b03`  |
| 2882   | Layout 2 | `636a8a313b03`  |
| 2872   | Layout 2 | `636a8a313b03`  |
| 2863   | Layout 2 | `636a8a313b03`  |
| 2855   | Layout 2 | `636a8a313b03`  |
| 2849   | Layout 2 | `636a8a313b03`  |
| 2844   | Layout 2 | `636a8a313b03`  |
| 2834   | Layout 2 | `636a8a313b03`  |
| 2825   | Layout 2 | `636a8a313b03`  |
| 2819   | Layout 2 | `636a8a313b03`  |
| 2811   | Layout 2 | `636a8a313b03`  |
| 2803   | Layout 2 | `636a8a313b03`  |
| 2794   | Layout 2 | `636a8a313b03`  |
| 2783   | Layout 2 | `636a8a313b03`  |
| 2774   | Layout 2 | `636a8a313b03`  |
| 2765   | Layout 2 | `636a8a313b03`  |
| 2756   | Layout 2 | `636a8a313b03`  |
| 2750   | Layout 2 | `636a8a313b03`  |
| 2743   | Layout 2 | `636a8a313b03`  |
| 2736   | Layout 2 | `636a8a313b03`  |
| 2726   | Layout 2 | `636a8a313b03`  |
| 2717   | Layout 2 | `636a8a313b03`  |
| 2709   | Layout 2 | `636a8a313b03`  |
| 2703   | Layout 2 | `636a8a313b03`  |
| 2695   | Layout 2 | `636a8a313b03`  |
| 2684   | Layout 2 | `636a8a313b03`  |
| 2672   | Layout 2 | `636a8a313b03`  |
| 2665   | Layout 2 | `636a8a313b03`  |
| 2657   | Layout 2 | `636a8a313b03`  |
| 2649   | Layout 2 | `636a8a313b03`  |
| 2644   | Layout 2 | `636a8a313b03`  |
| 2637   | Layout 2 | `636a8a313b03`  |
| 2629   | Layout 2 | `636a8a313b03`  |
| 2619   | Layout 2 | `636a8a313b03`  |
| 2612   | Layout 2 | `636a8a313b03`  |
| 2606   | Layout 2 | `636a8a313b03`  |
| 2602   | Layout 2 | `636a8a313b03`  |
| 2601   | Layout 2 | `636a8a313b03`  |
| 2592   | Layout 2 | `636a8a313b03`  |
| 2583   | Layout 2 | `636a8a313b03`  |
| 2575   | Layout 2 | `636a8a313b03`  |
| 2567   | Layout 2 | `636a8a313b03`  |
| 2560   | Layout 2 | `636a8a313b03`  |
| 2553   | Layout 2 | `636a8a313b03`  |
| 2545   | Layout 2 | `636a8a313b03`  |
| 2538   | Layout 2 | `636a8a313b03`  |
| 2529   | Layout 2 | `636a8a313b03`  |
| 2519   | Layout 2 | `636a8a313b03`  |
| 2513   | Layout 2 | `636a8a313b03`  |
| 2510   | Layout 2 | `636a8a313b03`  |
| 2507   | Layout 2 | `636a8a313b03`  |
| 2503   | Layout 2 | `636a8a313b03`  |
| 2498   | Layout 2 | `636a8a313b03`  |
| 2492   | Layout 2 | `636a8a313b03`  |
| 2487   | Layout 2 | `636a8a313b03`  |
| 2480   | Layout 2 | `636a8a313b03`  |
| 2474   | Layout 2 | `636a8a313b03`  |
| 2468   | Layout 2 | `636a8a313b03`  |
| 2460   | Layout 2 | `636a8a313b03`  |
| 2453   | Layout 2 | `636a8a313b03`  |
| 2444   | Layout 2 | `636a8a313b03`  |
| 2438   | Layout 2 | `636a8a313b03`  |
| 2434   | Layout 2 | `636a8a313b03`  |
| 2429   | Layout 2 | `636a8a313b03`  |
| 2421   | Layout 2 | `636a8a313b03`  |
| 2414   | Layout 2 | `636a8a313b03`  |
| 2407   | Layout 2 | `636a8a313b03`  |
| 2401   | Layout 2 | `636a8a313b03`  |
| 2397   | Layout 2 | `636a8a313b03`  |
| 2393   | Layout 2 | `636a8a313b03`  |
| 2384   | Layout 2 | `636a8a313b03`  |
| 2378   | Layout 2 | `636a8a313b03`  |
| 2372   | Layout 2 | `636a8a313b03`  |
| 2358   | Layout 2 | `636a8a313b03`  |
| 2352   | Layout 2 | `636a8a313b03`  |
| 2347   | Layout 2 | `636a8a313b03`  |
| 2343   | Layout 2 | `636a8a313b03`  |
| 2335   | Layout 2 | `636a8a313b03`  |
| 2327   | Layout 2 | `636a8a313b03`  |
| 2324   | Layout 2 | `636a8a313b03`  |
| 2319   | Layout 2 | `636a8a313b03`  |
| 2313   | Layout 2 | `636a8a313b03`  |
| 2308   | Layout 2 | `636a8a313b03`  |
| 2302   | Layout 2 | `636a8a313b03`  |
| 2295   | Layout 2 | `636a8a313b03`  |
| 2290   | Layout 2 | `636a8a313b03`  |
| 2284   | Layout 2 | `636a8a313b03`  |
| 2276   | Layout 2 | `636a8a313b03`  |
| 2269   | Layout 2 | `636a8a313b03`  |
| 2259   | Layout 2 | `636a8a313b03`  |
| 2250   | Layout 2 | `636a8a313b03`  |
| 2243   | Layout 2 | `636a8a313b03`  |
| 2235   | Layout 2 | `636a8a313b03`  |
| 2229   | Layout 2 | `636a8a313b03`  |
| 2224   | Layout 2 | `636a8a313b03`  |
| 2218   | Layout 2 | `636a8a313b03`  |
| 2215   | Layout 2 | `636a8a313b03`  |
| 2207   | Layout 2 | `636a8a313b03`  |
| 2203   | Layout 1 | `636a8a313b03`  |
| 2196   | Layout 1 | `636a8a313b03`  |
| 2192   | Layout 1 | `636a8a313b03`  |
| 2189   | Layout 1 | `636a8a313b03`  |
| 2183   | Layout 1 | `636a8a313b03`  |
| 2179   | Layout 1 | `636a8a313b03`  |
| 2171   | Layout 1 | `636a8a313b03`  |
| 2163   | Layout 1 | `636a8a313b03`  |
| 2156   | Layout 1 | `636a8a313b03`  |
| 2151   | Layout 1 | `636a8a313b03`  |
| 2147   | Layout 1 | `636a8a313b03`  |
| 2142   | Layout 1 | `636a8a313b03`  |
| 2138   | Layout 1 | `636a8a313b03`  |
| 2134   | Layout 1 | `636a8a313b03`  |
| 2130   | Layout 1 | `636a8a313b03`  |
| 2122   | Layout 1 | `636a8a313b03`  |
| 2107   | Layout 1 | `636a8a313b03`  |
| 2098   | Layout 1 | `636a8a313b03`  |
| 2089   | Layout 1 | `636a8a313b03`  |
| 2081   | Layout 1 | `636a8a313b03`  |
| 2073   | Layout 1 | `636a8a313b03`  |
| 2067   | Layout 1 | `636a8a313b03`  |
| 2063   | Layout 1 | `636a8a313b03`  |
| 2059   | Layout 1 | `636a8a313b03`  |
| 2052   | Layout 1 | `636a8a313b03`  |
| 2044   | Layout 1 | `636a8a313b03`  |
| 2039   | Layout 1 | `636a8a313b03`  |
| 2032   | Layout 1 | `636a8a313b03`  |
| 2025   | Layout 1 | `636a8a313b03`  |
| 2011   | Layout 1 | `636a8a313b03`  |
| 2005   | No file  | `636a8a313b03`  |
| 2000   | No file  | `636a8a313b03`  |
| 1996   | No file  | `636a8a313b03`  |
| 1991   | No file  | `636a8a313b03`  |
| 1985   | No file  | `636a8a313b03`  |
| 1980   | No file  | `636a8a313b03`  |
| 1969   | No file  | `636a8a313b03`  |
| 1964   | No file  | `636a8a313b03`  |
| 1958   | No file  | `636a8a313b03`  |
| 1950   | No file  | `636a8a313b03`  |
| 1945   | No file  | `636a8a313b03`  |
| 1937   | No file  | `636a8a313b03`  |
| 1933   | No file  | `636a8a313b03`  |
| 1927   | No file  | `636a8a313b03`  |
| 1921   | No file  | `636a8a313b03`  |
| 1914   | No file  | `636a8a313b03`  |
| 1908   | No file  | `636a8a313b03`  |
| 1897   | No file  | `636a8a313b03`  |
| 1892   | No file  | `636a8a313b03`  |
| 1886   | No file  | `636a8a313b03`  |
| 1881   | No file  | `636a8a313b03`  |
| 1871   | No file  | `636a8a313b03`  |
| 1866   | No file  | `636a8a313b03`  |
| 1862   | No file  | `636a8a313b03`  |
| 1854   | No file  | `636a8a313b03`  |
| 1846   | No file  | `636a8a313b03`  |
| 1838   | No file  | `636a8a313b03`  |
| 1832   | No file  | `636a8a313b03`  |
| 1826   | No file  | `636a8a313b03`  |
| 1822   | No file  | `636a8a313b03`  |
| 1818   | No file  | `636a8a313b03`  |
| 1804   | No file  | `636a8a313b03`  |
| 1794   | No file  | `636a8a313b03`  |
| 1790   | No file  | `636a8a313b03`  |
| 1784   | No file  | `636a8a313b03`  |
| 1774   | No file  | `636a8a313b03`  |
| 1771   | No file  | `636a8a313b03`  |
| 1762   | No file  | `636a8a313b03`  |
| 1759   | No file  | `636a8a313b03`  |
| 1754   | No file  | `636a8a313b03`  |
| 1749   | No file  | `636a8a313b03`  |
| 1743   | No file  | `636a8a313b03`  |
| 1737   | No file  | `636a8a313b03`  |
| 1731   | No file  | `636a8a313b03`  |
| 1725   | No file  | `636a8a313b03`  |
| 1717   | No file  | `636a8a313b03`  |
| 1710   | No file  | `636a8a313b03`  |
| 1704   | No file  | `636a8a313b03`  |
| 1698   | No file  | `636a8a313b03`  |
| 1690   | No file  | `636a8a313b03`  |
| 1685   | No file  | `636a8a313b03`  |
| 1680   | No file  | `636a8a313b03`  |
| 1674   | No file  | `636a8a313b03`  |
| 1668   | No file  | `636a8a313b03`  |
| 1659   | No file  | `636a8a313b03`  |
| 1649   | No file  | `636a8a313b03`  |
| 1642   | No file  | `636a8a313b03`  |
| 1636   | No file  | `636a8a313b03`  |
| 1628   | No file  | `636a8a313b03`  |
| 1622   | No file  | `636a8a313b03`  |
| 1614   | No file  | `636a8a313b03`  |
| 1608   | No file  | `636a8a313b03`  |
| 1602   | No file  | `636a8a313b03`  |
| 1598   | No file  | `636a8a313b03`  |
| 1594   | No file  | `636a8a313b03`  |
| 1590   | No file  | `636a8a313b03`  |
| 1587   | No file  | `636a8a313b03`  |
| 1584   | No file  | `636a8a313b03`  |
| 1579   | No file  | `636a8a313b03`  |
| 1572   | No file  | `636a8a313b03`  |
| 1565   | No file  | `636a8a313b03`  |
| 1559   | No file  | `636a8a313b03`  |
| 1554   | No file  | `636a8a313b03`  |
| 1547   | No file  | `636a8a313b03`  |
| 1537   | No file  | `636a8a313b03`  |
| 1529   | No file  | `636a8a313b03`  |
| 1524   | No file  | `636a8a313b03`  |
| 1519   | No file  | `636a8a313b03`  |
| 1509   | No file  | `636a8a313b03`  |
| 1506   | No file  | `636a8a313b03`  |
| 1504   | No file  | `636a8a313b03`  |
| 1500   | No file  | `636a8a313b03`  |
| 1493   | No file  | `636a8a313b03`  |
| 1489   | No file  | `636a8a313b03`  |
| 1485   | No file  | `636a8a313b03`  |
| 1481   | No file  | `636a8a313b03`  |
| 1474   | No file  | `636a8a313b03`  |
| 1466   | No file  | `636a8a313b03`  |
| 1462   | No file  | `636a8a313b03`  |
| 1459   | No file  | `636a8a313b03`  |
| 1453   | No file  | `636a8a313b03`  |
| 1450   | No file  | `636a8a313b03`  |
| 1445   | No file  | `636a8a313b03`  |
| 1439   | No file  | `636a8a313b03`  |
| 1433   | No file  | `636a8a313b03`  |
| 1430   | No file  | `636a8a313b03`  |
| 1426   | No file  | `636a8a313b03`  |
| 1421   | No file  | `636a8a313b03`  |
| 1417   | No file  | `636a8a313b03`  |
| 1416   | No file  | `636a8a313b03`  |
| 1409   | No file  | `636a8a313b03`  |
| 1405   | No file  | `636a8a313b03`  |
| 1401   | No file  | `636a8a313b03`  |
| 1396   | No file  | `636a8a313b03`  |
| 1391   | No file  | `636a8a313b03`  |
| 1390   | No file  | `636a8a313b03`  |
| 1386   | No file  | `636a8a313b03`  |
| 1381   | No file  | `636a8a313b03`  |
| 1379   | No file  | `636a8a313b03`  |
| 1372   | No file  | `636a8a313b03`  |
| 1366   | No file  | `636a8a313b03`  |
| 1364   | No file  | `636a8a313b03`  |
| 1363   | No file  | `636a8a313b03`  |
| 1360   | No file  | `636a8a313b03`  |
| 1358   | No file  | `636a8a313b03`  |
| 1355   | No file  | `636a8a313b03`  |
| 1351   | No file  | `636a8a313b03`  |
| 1348   | No file  | `636a8a313b03`  |
| 1346   | No file  | `636a8a313b03`  |
| 1341   | No file  | `636a8a313b03`  |
| 1340   | No file  | `636a8a313b03`  |
| 1338   | No file  | `636a8a313b03`  |
| 1335   | No file  | `636a8a313b03`  |
| 1333   | No file  | `636a8a313b03`  |
| 1329   | No file  | `636a8a313b03`  |
| 1327   | No file  | `636a8a313b03`  |
| 1324   | No file  | `636a8a313b03`  |
| 1321   | No file  | `636a8a313b03`  |
| 1319   | No file  | `636a8a313b03`  |
| 1318   | No file  | `636a8a313b03`  |
| 1316   | No file  | `636a8a313b03`  |
| 1313   | No file  | `636a8a313b03`  |
| 1311   | No file  | `636a8a313b03`  |
| 1309   | No file  | `636a8a313b03`  |
| 1304   | No file  | `636a8a313b03`  |
| 1292   | No file  | `636a8a313b03`  |
| 1286   | No file  | `636a8a313b03`  |
| 1280   | No file  | `636a8a313b03`  |
| 1276   | No file  | `636a8a313b03`  |
| 1267   | No file  | `636a8a313b03`  |
| 1261   | No file  | `636a8a313b03`  |
| 1256   | No file  | `636a8a313b03`  |
| 1250   | No file  | `636a8a313b03`  |
| 1246   | No file  | `636a8a313b03`  |
| 1239   | No file  | `636a8a313b03`  |
| 1230   | No file  | `636a8a313b03`  |
| 1226   | No file  | `636a8a313b03`  |
| 1220   | No file  | `636a8a313b03`  |
| 1217   | No file  | `636a8a313b03`  |
| 1211   | No file  | `636a8a313b03`  |
| 1210   | No file  | `636a8a313b03`  |
| 1208   | No file  | `636a8a313b03`  |
| 1203   | No file  | `636a8a313b03`  |
| 1197   | No file  | `636a8a313b03`  |
| 1194   | No file  | `636a8a313b03`  |
| 1192   | No file  | `636a8a313b03`  |
| 1187   | No file  | `636a8a313b03`  |
| 1183   | No file  | `636a8a313b03`  |
| 1177   | No file  | `636a8a313b03`  |
| 1173   | No file  | `636a8a313b03`  |
| 1167   | No file  | `636a8a313b03`  |
| 1164   | No file  | `636a8a313b03`  |
| 1156   | No file  | `636a8a313b03`  |
| 1149   | No file  | `636a8a313b03`  |
| 1144   | No file  | `636a8a313b03`  |
| 1137   | No file  | `636a8a313b03`  |
| 1132   | No file  | `636a8a313b03`  |
| 1127   | No file  | `636a8a313b03`  |
| 1122   | No file  | `636a8a313b03`  |
| 1118   | No file  | `636a8a313b03`  |
| 1114   | No file  | `636a8a313b03`  |
| 1109   | No file  | `636a8a313b03`  |
| 1102   | No file  | `636a8a313b03`  |
| 1096   | No file  | `636a8a313b03`  |
| 1088   | No file  | `636a8a313b03`  |
| 1081   | No file  | `636a8a313b03`  |
| 1076   | No file  | `636a8a313b03`  |
| 1069   | No file  | `636a8a313b03`  |
| 1064   | No file  | `636a8a313b03`  |
| 1058   | No file  | `636a8a313b03`  |
| 1051   | No file  | `636a8a313b03`  |
| 1044   | No file  | `636a8a313b03`  |
| 1036   | No file  | `636a8a313b03`  |
| 1026   | No file  | `636a8a313b03`  |
| 1016   | No file  | `636a8a313b03`  |
| 1009   | No file  | `636a8a313b03`  |
| 1005   | No file  | `636a8a313b03`  |
| 1000   | No file  | `636a8a313b03`  |
| 998    | No file  | `636a8a313b03`  |
| 990    | No file  | `636a8a313b03`  |
| 979    | No file  | `636a8a313b03`  |
| 972    | No file  | `636a8a313b03`  |
| 963    | No file  | `636a8a313b03`  |
| 955    | No file  | `636a8a313b03`  |
| 946    | No file  | `636a8a313b03`  |
| 938    | No file  | `636a8a313b03`  |
| 927    | No file  | `636a8a313b03`  |
| 911    | No file  | `636a8a313b03`  |
| 904    | No file  | `636a8a313b03`  |
| 899    | No file  | `636a8a313b03`  |
| 894    | No file  | `636a8a313b03`  |
| 885    | No file  | `636a8a313b03`  |
| 879    | No file  | `636a8a313b03`  |
| 872    | No file  | `636a8a313b03`  |
| 864    | No file  | `636a8a313b03`  |
| 855    | No file  | `636a8a313b03`  |
| 853    | No file  | `636a8a313b03`  |
| 845    | No file  | `636a8a313b03`  |
| 837    | No file  | `636a8a313b03`  |
| 829    | No file  | `636a8a313b03`  |
| 822    | No file  | `636a8a313b03`  |
| 814    | No file  | `636a8a313b03`  |
| 805    | No file  | `636a8a313b03`  |
| 794    | No file  | `636a8a313b03`  |
| 787    | No file  | `636a8a313b03`  |
| 780    | No file  | `636a8a313b03`  |
| 771    | No file  | `636a8a313b03`  |
| 760    | No file  | `636a8a313b03`  |
| 748    | No file  | `636a8a313b03`  |
| 741    | No file  | `636a8a313b03`  |
| 736    | No file  | `636a8a313b03`  |
| 731    | No file  | `636a8a313b03`  |
| 723    | No file  | `636a8a313b03`  |
| 711    | No file  | `636a8a313b03`  |
| 707    | No file  | `636a8a313b03`  |
| 697    | No file  | `636a8a313b03`  |
| 689    | No file  | `636a8a313b03`  |
| 683    | No file  | `636a8a313b03`  |
| 678    | No file  | `636a8a313b03`  |
| 670    | No file  | `636a8a313b03`  |
| 661    | No file  | `636a8a313b03`  |
| 656    | No file  | `636a8a313b03`  |
| 652    | No file  | `636a8a313b03`  |
| 643    | No file  | `636a8a313b03`  |
| 637    | No file  | `636a8a313b03`  |
| 630    | No file  | `636a8a313b03`  |
| 627    | No file  | `636a8a313b03`  |
| 621    | No file  | `636a8a313b03`  |
| 617    | No file  | `636a8a313b03`  |
| 615    | No file  | `636a8a313b03`  |
| 606    | No file  | `636a8a313b03`  |
| 599    | No file  | `636a8a313b03`  |
| 592    | No file  | `636a8a313b03`  |
| 586    | No file  | `636a8a313b03`  |
| 577    | No file  | `636a8a313b03`  |
| 569    | No file  | `636a8a313b03`  |
| 561    | No file  | `636a8a313b03`  |
| 554    | No file  | `636a8a313b03`  |
| 542    | No file  | `636a8a313b03`  |
| 532    | No file  | `636a8a313b03`  |
| 531    | No file  | `636a8a313b03`  |
| 526    | No file  | `636a8a313b03`  |
| 521    | No file  | `636a8a313b03`  |
| 517    | No file  | `636a8a313b03`  |
| 510    | No file  | `636a8a313b03`  |
| 508    | No file  | `636a8a313b03`  |
| 504    | No file  | `636a8a313b03`  |
| 497    | No file  | `636a8a313b03`  |
| 491    | No file  | `636a8a313b03`  |
| 485    | No file  | `636a8a313b03`  |
| 478    | No file  | `636a8a313b03`  |
| 472    | No file  | `636a8a313b03`  |
| 466    | No file  | `636a8a313b03`  |
| 457    | No file  | `636a8a313b03`  |
| 452    | No file  | `636a8a313b03`  |
| 449    | No file  | `636a8a313b03`  |
| 435    | No file  | `636a8a313b03`  |

<!-- versions:end -->

## Companion Files

None. The handler names the region (LOC type 17) and the knowledge entry
(LOC type 34) from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                                          |
| ------- | ---- | ------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u16  | region_key    | `regioninfo.bss` region key of a storage town (LOC type 17); unique per row    |
| `+0x02` | u32  | knowledge_key | Knowledge entry (LOC type 34) of the town's area; shared by the towns of one area |

## Layout 1

A list of item IDs after the rows.

### File Layout

| Offset         | Type              | Field      | Notes                                                       |
| -------------- | ----------------- | ---------- | ----------------------------------------------------------- |
| `+0x00`        | u32               | row_count  | Number of rows                                              |
| `+0x04`        | Row[row_count]    | rows       | See Row                                                     |
| `rows+0x00`    | u32               | item_count | Number of `item_ids`; `30` on client 2107                   |
| `rows+0x04`    | u32[item_count]   | item_ids   | Item IDs (LOC type 0), from `40780` Greater Blessed Spirit Essence; see Notes |

## Field Names

The Magnus is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`Abyss` in its name. Both fields are named by what they resolve to. Every
`region_key` has a LOC type 17 name and is a town with a storage
(Heidel, Calpheon City, Altinova, Grána, Duvencrune, O'draxxia, Eilton,
Nampo's Moodle Village and more on client 3482). Every `knowledge_key` has
a LOC type 34 name: eleven Abyssal Vein entries, one per area, and
`11358` The Magnus.

## Notes

- On client 3482, 33 towns share 12 knowledge keys: `11355` Abyssal Vein -
  Land of the Morning Light covers six towns, `11358` The Magnus four.
  The row count grows with the clients: 21 on client 2107, 28 on 2519, 31
  on 2637, 32 on 3002 and 33 on 3474.
- Layout 1 (client 2107) ends with 30 item IDs. Its last four (`59321`
  Ebenruth's Nol, `16019` Archaeologist's Map, `16016` Lafi Bedmountain's
  Upgraded Compass and `12034` Rich Merchant's Ring) are four of the five
  entries of [`othertownnotmovableitem.bss`](othertownnotmovableitem_bss.md)
  on client 2519, where this file no longer has the list. Client 2107
  does not ship `othertownnotmovableitem.bss`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/abyssone_tables.py`: the
  region and the knowledge entry with their names. It reads Layout 2 only.

## Open Questions

### What the Knowledge Entry Unlocks

Each town carries the Abyssal Vein knowledge of its area. Whether the
storage opens in the Magnus once the character has that knowledge, or the
entry only groups the towns by area, is not in the client Lua checked
(`nakmessage_warehouse_clear_all.luac` gets the storage name only).
