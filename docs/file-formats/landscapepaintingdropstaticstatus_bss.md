# `landscapepaintingdropstaticstatus.bss` Format

## Purpose

The landscape paintings of the `Panel_Window_LandscapePaintingDrop`
window: one row per painting with its Korean name, a list of u32 keys and
the treasure item piece the window names for it. The window Lua
(`panel_window_landscapepaintingdrop_1.luac`) reads a painting by its type
through `ToClient_landscapePaintingDropString(type)` (the name) and
`ToClient_landscapePaintingDropItemEnchantKey(type)` (the drop item), and
the paints that charge it through
`ToClient_getItemLandScapePaintingChargeByIndex(type, index)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes  | Records | Row bytes                      |
| ------ | -------------- | ------- | --------------------------------------- | ------ | ------- | ------------------------------ |
| 2      | 3387 and later | 3483    | `landscapepaintingdropstaticstatus.bss` | 15,776 | 14 Row  | 953 to 1,153, 1,106 on average |
| 1      | 3012 to 3381   | 3381    | `landscapepaintingdropstaticstatus.bss` | 10,926 | 12 Row  | 849 to 925, 889 on average     |

| Layout | File                                    | Known        | Unknown          |
| ------ | --------------------------------------- | ------------ | ---------------- |
| 2      | `landscapepaintingdropstaticstatus.bss` | 424 B (2.7%) | 15,352 B (97.3%) |
| 1      | `landscapepaintingdropstaticstatus.bss` | 318 B (2.9%) | 10,608 B (97.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `a6cd4998129a`  |
| 3482   | Layout 2 | `a6cd4998129a`  |
| 3474   | Layout 2 | `a6cd4998129a`  |
| 3473   | Layout 2 | `a6cd4998129a`  |
| 3464   | Layout 2 | `a6cd4998129a`  |
| 3458   | Layout 2 | `a6cd4998129a`  |
| 3454   | Layout 2 | `a6cd4998129a`  |
| 3444   | Layout 2 | `a6cd4998129a`  |
| 3435   | Layout 2 | `a6cd4998129a`  |
| 3426   | Layout 2 | `a6cd4998129a`  |
| 3418   | Layout 2 | `a6cd4998129a`  |
| 3412   | Layout 2 | `a6cd4998129a`  |
| 3402   | Layout 2 | `a6cd4998129a`  |
| 3396   | Layout 2 | `a6cd4998129a`  |
| 3387   | Layout 2 | `a6cd4998129a`  |
| 3381   | Layout 1 | `a6cd4998129a`  |
| 3373   | Layout 1 | `a6cd4998129a`  |
| 3364   | Layout 1 | `a6cd4998129a`  |
| 3356   | Layout 1 | `a6cd4998129a`  |
| 3349   | Layout 1 | `a6cd4998129a`  |
| 3342   | Layout 1 | `a6cd4998129a`  |
| 3335   | Layout 1 | `a6cd4998129a`  |
| 3326   | Layout 1 | `a6cd4998129a`  |
| 3321   | Layout 1 | `a6cd4998129a`  |
| 3314   | Layout 1 | `a6cd4998129a`  |
| 3303   | Layout 1 | `a6cd4998129a`  |
| 3302   | Layout 1 | `a6cd4998129a`  |
| 3293   | Layout 1 | `a6cd4998129a`  |
| 3283   | Layout 1 | `a6cd4998129a`  |
| 3275   | Layout 1 | `a6cd4998129a`  |
| 3267   | Layout 1 | `a6cd4998129a`  |
| 3258   | Layout 1 | `a6cd4998129a`  |
| 3251   | Layout 1 | `a6cd4998129a`  |
| 3242   | Layout 1 | `a6cd4998129a`  |
| 3235   | Layout 1 | `a6cd4998129a`  |
| 3229   | Layout 1 | `a6cd4998129a`  |
| 3212   | Layout 1 | `a6cd4998129a`  |
| 3203   | Layout 1 | `a6cd4998129a`  |
| 3193   | Layout 1 | `a6cd4998129a`  |
| 3186   | Layout 1 | `a6cd4998129a`  |
| 3177   | Layout 1 | `a6cd4998129a`  |
| 3169   | Layout 1 | `a6cd4998129a`  |
| 3158   | Layout 1 | `a6cd4998129a`  |
| 3151   | Layout 1 | `a6cd4998129a`  |
| 3144   | Layout 1 | `a6cd4998129a`  |
| 3133   | Layout 1 | `a6cd4998129a`  |
| 3125   | Layout 1 | `a6cd4998129a`  |
| 3118   | Layout 1 | `a6cd4998129a`  |
| 3111   | Layout 1 | `a6cd4998129a`  |
| 3103   | Layout 1 | `a6cd4998129a`  |
| 3095   | Layout 1 | `a6cd4998129a`  |
| 3086   | Layout 1 | `a6cd4998129a`  |
| 3072   | Layout 1 | `a6cd4998129a`  |
| 3062   | Layout 1 | `a6cd4998129a`  |
| 3052   | Layout 1 | `a6cd4998129a`  |
| 3045   | Layout 1 | `a6cd4998129a`  |
| 3037   | Layout 1 | `a6cd4998129a`  |
| 3030   | Layout 1 | `a6cd4998129a`  |
| 3021   | Layout 1 | `a6cd4998129a`  |
| 3012   | Layout 1 | `a6cd4998129a`  |
| 3002   | No file  | `a6cd4998129a`  |
| 2995   | No file  | `a6cd4998129a`  |
| 2987   | No file  | `a6cd4998129a`  |
| 2978   | No file  | `a6cd4998129a`  |
| 2970   | No file  | `a6cd4998129a`  |
| 2959   | No file  | `a6cd4998129a`  |
| 2951   | No file  | `a6cd4998129a`  |
| 2942   | No file  | `a6cd4998129a`  |
| 2935   | No file  | `a6cd4998129a`  |
| 2932   | No file  | `a6cd4998129a`  |
| 2923   | No file  | `a6cd4998129a`  |
| 2919   | No file  | `a6cd4998129a`  |
| 2907   | No file  | `a6cd4998129a`  |
| 2900   | No file  | `a6cd4998129a`  |
| 2891   | No file  | `a6cd4998129a`  |
| 2882   | No file  | `a6cd4998129a`  |
| 2872   | No file  | `a6cd4998129a`  |
| 2863   | No file  | `a6cd4998129a`  |
| 2855   | No file  | `a6cd4998129a`  |
| 2849   | No file  | `a6cd4998129a`  |
| 2844   | No file  | `a6cd4998129a`  |
| 2834   | No file  | `a6cd4998129a`  |
| 2825   | No file  | `a6cd4998129a`  |
| 2819   | No file  | `a6cd4998129a`  |
| 2811   | No file  | `a6cd4998129a`  |
| 2803   | No file  | `a6cd4998129a`  |
| 2794   | No file  | `a6cd4998129a`  |
| 2783   | No file  | `a6cd4998129a`  |
| 2774   | No file  | `a6cd4998129a`  |
| 2765   | No file  | `a6cd4998129a`  |
| 2756   | No file  | `a6cd4998129a`  |
| 2750   | No file  | `a6cd4998129a`  |
| 2743   | No file  | `a6cd4998129a`  |
| 2736   | No file  | `a6cd4998129a`  |
| 2726   | No file  | `a6cd4998129a`  |
| 2717   | No file  | `a6cd4998129a`  |
| 2709   | No file  | `a6cd4998129a`  |
| 2703   | No file  | `a6cd4998129a`  |
| 2695   | No file  | `a6cd4998129a`  |
| 2684   | No file  | `a6cd4998129a`  |
| 2672   | No file  | `a6cd4998129a`  |
| 2665   | No file  | `a6cd4998129a`  |
| 2657   | No file  | `a6cd4998129a`  |
| 2649   | No file  | `a6cd4998129a`  |
| 2644   | No file  | `a6cd4998129a`  |
| 2637   | No file  | `a6cd4998129a`  |
| 2629   | No file  | `a6cd4998129a`  |
| 2619   | No file  | `a6cd4998129a`  |
| 2612   | No file  | `a6cd4998129a`  |
| 2606   | No file  | `a6cd4998129a`  |
| 2602   | No file  | `a6cd4998129a`  |
| 2601   | No file  | `a6cd4998129a`  |
| 2592   | No file  | `a6cd4998129a`  |
| 2583   | No file  | `a6cd4998129a`  |
| 2575   | No file  | `a6cd4998129a`  |
| 2567   | No file  | `a6cd4998129a`  |
| 2560   | No file  | `a6cd4998129a`  |
| 2553   | No file  | `a6cd4998129a`  |
| 2545   | No file  | `a6cd4998129a`  |
| 2538   | No file  | `a6cd4998129a`  |
| 2529   | No file  | `a6cd4998129a`  |
| 2519   | No file  | `a6cd4998129a`  |
| 2513   | No file  | `a6cd4998129a`  |
| 2510   | No file  | `a6cd4998129a`  |
| 2507   | No file  | `a6cd4998129a`  |
| 2503   | No file  | `a6cd4998129a`  |
| 2498   | No file  | `a6cd4998129a`  |
| 2492   | No file  | `a6cd4998129a`  |
| 2487   | No file  | `a6cd4998129a`  |
| 2480   | No file  | `a6cd4998129a`  |
| 2474   | No file  | `a6cd4998129a`  |
| 2468   | No file  | `a6cd4998129a`  |
| 2460   | No file  | `a6cd4998129a`  |
| 2453   | No file  | `a6cd4998129a`  |
| 2444   | No file  | `a6cd4998129a`  |
| 2438   | No file  | `a6cd4998129a`  |
| 2434   | No file  | `a6cd4998129a`  |
| 2429   | No file  | `a6cd4998129a`  |
| 2421   | No file  | `a6cd4998129a`  |
| 2414   | No file  | `a6cd4998129a`  |
| 2407   | No file  | `a6cd4998129a`  |
| 2401   | No file  | `a6cd4998129a`  |
| 2397   | No file  | `a6cd4998129a`  |
| 2393   | No file  | `a6cd4998129a`  |
| 2384   | No file  | `a6cd4998129a`  |
| 2378   | No file  | `a6cd4998129a`  |
| 2372   | No file  | `a6cd4998129a`  |
| 2358   | No file  | `a6cd4998129a`  |
| 2352   | No file  | `a6cd4998129a`  |
| 2347   | No file  | `a6cd4998129a`  |
| 2343   | No file  | `a6cd4998129a`  |
| 2335   | No file  | `a6cd4998129a`  |
| 2327   | No file  | `a6cd4998129a`  |
| 2324   | No file  | `a6cd4998129a`  |
| 2319   | No file  | `a6cd4998129a`  |
| 2313   | No file  | `a6cd4998129a`  |
| 2308   | No file  | `a6cd4998129a`  |
| 2302   | No file  | `a6cd4998129a`  |
| 2295   | No file  | `a6cd4998129a`  |
| 2290   | No file  | `a6cd4998129a`  |
| 2284   | No file  | `a6cd4998129a`  |
| 2276   | No file  | `a6cd4998129a`  |
| 2269   | No file  | `a6cd4998129a`  |
| 2259   | No file  | `a6cd4998129a`  |
| 2250   | No file  | `a6cd4998129a`  |
| 2243   | No file  | `a6cd4998129a`  |
| 2235   | No file  | `a6cd4998129a`  |
| 2229   | No file  | `a6cd4998129a`  |
| 2224   | No file  | `a6cd4998129a`  |
| 2218   | No file  | `a6cd4998129a`  |
| 2215   | No file  | `a6cd4998129a`  |
| 2207   | No file  | `a6cd4998129a`  |
| 2203   | No file  | `a6cd4998129a`  |
| 2196   | No file  | `a6cd4998129a`  |
| 2192   | No file  | `a6cd4998129a`  |
| 2189   | No file  | `a6cd4998129a`  |
| 2183   | No file  | `a6cd4998129a`  |
| 2179   | No file  | `a6cd4998129a`  |
| 2171   | No file  | `a6cd4998129a`  |
| 2163   | No file  | `a6cd4998129a`  |
| 2156   | No file  | `a6cd4998129a`  |
| 2151   | No file  | `a6cd4998129a`  |
| 2147   | No file  | `a6cd4998129a`  |
| 2142   | No file  | `a6cd4998129a`  |
| 2138   | No file  | `a6cd4998129a`  |
| 2134   | No file  | `a6cd4998129a`  |
| 2130   | No file  | `a6cd4998129a`  |
| 2122   | No file  | `a6cd4998129a`  |
| 2107   | No file  | `a6cd4998129a`  |
| 2098   | No file  | `a6cd4998129a`  |
| 2089   | No file  | `a6cd4998129a`  |
| 2081   | No file  | `a6cd4998129a`  |
| 2073   | No file  | `a6cd4998129a`  |
| 2067   | No file  | `a6cd4998129a`  |
| 2063   | No file  | `a6cd4998129a`  |
| 2059   | No file  | `a6cd4998129a`  |
| 2052   | No file  | `a6cd4998129a`  |
| 2044   | No file  | `a6cd4998129a`  |
| 2039   | No file  | `a6cd4998129a`  |
| 2032   | No file  | `a6cd4998129a`  |
| 2025   | No file  | `a6cd4998129a`  |
| 2011   | No file  | `a6cd4998129a`  |
| 2005   | No file  | `a6cd4998129a`  |
| 2000   | No file  | `a6cd4998129a`  |
| 1996   | No file  | `a6cd4998129a`  |
| 1991   | No file  | `a6cd4998129a`  |
| 1985   | No file  | `a6cd4998129a`  |
| 1980   | No file  | `a6cd4998129a`  |
| 1969   | No file  | `a6cd4998129a`  |
| 1964   | No file  | `a6cd4998129a`  |
| 1958   | No file  | `a6cd4998129a`  |
| 1950   | No file  | `a6cd4998129a`  |
| 1945   | No file  | `a6cd4998129a`  |
| 1937   | No file  | `a6cd4998129a`  |
| 1933   | No file  | `a6cd4998129a`  |
| 1927   | No file  | `a6cd4998129a`  |
| 1921   | No file  | `a6cd4998129a`  |
| 1914   | No file  | `a6cd4998129a`  |
| 1908   | No file  | `a6cd4998129a`  |
| 1897   | No file  | `a6cd4998129a`  |
| 1892   | No file  | `a6cd4998129a`  |
| 1886   | No file  | `a6cd4998129a`  |
| 1881   | No file  | `a6cd4998129a`  |
| 1871   | No file  | `a6cd4998129a`  |
| 1866   | No file  | `a6cd4998129a`  |
| 1862   | No file  | `a6cd4998129a`  |
| 1854   | No file  | `a6cd4998129a`  |
| 1846   | No file  | `a6cd4998129a`  |
| 1838   | No file  | `a6cd4998129a`  |
| 1832   | No file  | `a6cd4998129a`  |
| 1826   | No file  | `a6cd4998129a`  |
| 1822   | No file  | `a6cd4998129a`  |
| 1818   | No file  | `a6cd4998129a`  |
| 1804   | No file  | `a6cd4998129a`  |
| 1794   | No file  | `a6cd4998129a`  |
| 1790   | No file  | `a6cd4998129a`  |
| 1784   | No file  | `a6cd4998129a`  |
| 1774   | No file  | `a6cd4998129a`  |
| 1771   | No file  | `a6cd4998129a`  |
| 1762   | No file  | `a6cd4998129a`  |
| 1759   | No file  | `a6cd4998129a`  |
| 1754   | No file  | `a6cd4998129a`  |
| 1749   | No file  | `a6cd4998129a`  |
| 1743   | No file  | `a6cd4998129a`  |
| 1737   | No file  | `a6cd4998129a`  |
| 1731   | No file  | `a6cd4998129a`  |
| 1725   | No file  | `a6cd4998129a`  |
| 1717   | No file  | `a6cd4998129a`  |
| 1710   | No file  | `a6cd4998129a`  |
| 1704   | No file  | `a6cd4998129a`  |
| 1698   | No file  | `a6cd4998129a`  |
| 1690   | No file  | `a6cd4998129a`  |
| 1685   | No file  | `a6cd4998129a`  |
| 1680   | No file  | `a6cd4998129a`  |
| 1674   | No file  | `a6cd4998129a`  |
| 1668   | No file  | `a6cd4998129a`  |
| 1659   | No file  | `a6cd4998129a`  |
| 1649   | No file  | `a6cd4998129a`  |
| 1642   | No file  | `a6cd4998129a`  |
| 1636   | No file  | `a6cd4998129a`  |
| 1628   | No file  | `a6cd4998129a`  |
| 1622   | No file  | `a6cd4998129a`  |
| 1614   | No file  | `a6cd4998129a`  |
| 1608   | No file  | `a6cd4998129a`  |
| 1602   | No file  | `a6cd4998129a`  |
| 1598   | No file  | `a6cd4998129a`  |
| 1594   | No file  | `a6cd4998129a`  |
| 1590   | No file  | `a6cd4998129a`  |
| 1587   | No file  | `a6cd4998129a`  |
| 1584   | No file  | `a6cd4998129a`  |
| 1579   | No file  | `a6cd4998129a`  |
| 1572   | No file  | `a6cd4998129a`  |
| 1565   | No file  | `a6cd4998129a`  |
| 1559   | No file  | `a6cd4998129a`  |
| 1554   | No file  | `a6cd4998129a`  |
| 1547   | No file  | `a6cd4998129a`  |
| 1537   | No file  | `a6cd4998129a`  |
| 1529   | No file  | `a6cd4998129a`  |
| 1524   | No file  | `a6cd4998129a`  |
| 1519   | No file  | `a6cd4998129a`  |
| 1509   | No file  | `a6cd4998129a`  |
| 1506   | No file  | `a6cd4998129a`  |
| 1504   | No file  | `a6cd4998129a`  |
| 1500   | No file  | `a6cd4998129a`  |
| 1493   | No file  | `a6cd4998129a`  |
| 1489   | No file  | `a6cd4998129a`  |
| 1485   | No file  | `a6cd4998129a`  |
| 1481   | No file  | `a6cd4998129a`  |
| 1474   | No file  | `a6cd4998129a`  |
| 1466   | No file  | `a6cd4998129a`  |
| 1462   | No file  | `a6cd4998129a`  |
| 1459   | No file  | `a6cd4998129a`  |
| 1453   | No file  | `a6cd4998129a`  |
| 1450   | No file  | `a6cd4998129a`  |
| 1445   | No file  | `a6cd4998129a`  |
| 1439   | No file  | `a6cd4998129a`  |
| 1433   | No file  | `a6cd4998129a`  |
| 1430   | No file  | `a6cd4998129a`  |
| 1426   | No file  | `a6cd4998129a`  |
| 1421   | No file  | `a6cd4998129a`  |
| 1417   | No file  | `a6cd4998129a`  |
| 1416   | No file  | `a6cd4998129a`  |
| 1409   | No file  | `a6cd4998129a`  |
| 1405   | No file  | `a6cd4998129a`  |
| 1401   | No file  | `a6cd4998129a`  |
| 1396   | No file  | `a6cd4998129a`  |
| 1391   | No file  | `a6cd4998129a`  |
| 1390   | No file  | `a6cd4998129a`  |
| 1386   | No file  | `a6cd4998129a`  |
| 1381   | No file  | `a6cd4998129a`  |
| 1379   | No file  | `a6cd4998129a`  |
| 1372   | No file  | `a6cd4998129a`  |
| 1366   | No file  | `a6cd4998129a`  |
| 1364   | No file  | `a6cd4998129a`  |
| 1363   | No file  | `a6cd4998129a`  |
| 1360   | No file  | `a6cd4998129a`  |
| 1358   | No file  | `a6cd4998129a`  |
| 1355   | No file  | `a6cd4998129a`  |
| 1351   | No file  | `a6cd4998129a`  |
| 1348   | No file  | `a6cd4998129a`  |
| 1346   | No file  | `a6cd4998129a`  |
| 1341   | No file  | `a6cd4998129a`  |
| 1340   | No file  | `a6cd4998129a`  |
| 1338   | No file  | `a6cd4998129a`  |
| 1335   | No file  | `a6cd4998129a`  |
| 1333   | No file  | `a6cd4998129a`  |
| 1329   | No file  | `a6cd4998129a`  |
| 1327   | No file  | `a6cd4998129a`  |
| 1324   | No file  | `a6cd4998129a`  |
| 1321   | No file  | `a6cd4998129a`  |
| 1319   | No file  | `a6cd4998129a`  |
| 1318   | No file  | `a6cd4998129a`  |
| 1316   | No file  | `a6cd4998129a`  |
| 1313   | No file  | `a6cd4998129a`  |
| 1311   | No file  | `a6cd4998129a`  |
| 1309   | No file  | `a6cd4998129a`  |
| 1304   | No file  | `a6cd4998129a`  |
| 1292   | No file  | `a6cd4998129a`  |
| 1286   | No file  | `a6cd4998129a`  |
| 1280   | No file  | `a6cd4998129a`  |
| 1276   | No file  | `a6cd4998129a`  |
| 1267   | No file  | `a6cd4998129a`  |
| 1261   | No file  | `a6cd4998129a`  |
| 1256   | No file  | `a6cd4998129a`  |
| 1250   | No file  | `a6cd4998129a`  |
| 1246   | No file  | `a6cd4998129a`  |
| 1239   | No file  | `a6cd4998129a`  |
| 1230   | No file  | `a6cd4998129a`  |
| 1226   | No file  | `a6cd4998129a`  |
| 1220   | No file  | `a6cd4998129a`  |
| 1217   | No file  | `a6cd4998129a`  |
| 1211   | No file  | `a6cd4998129a`  |
| 1210   | No file  | `a6cd4998129a`  |
| 1208   | No file  | `a6cd4998129a`  |
| 1203   | No file  | `a6cd4998129a`  |
| 1197   | No file  | `a6cd4998129a`  |
| 1194   | No file  | `a6cd4998129a`  |
| 1192   | No file  | `a6cd4998129a`  |
| 1187   | No file  | `a6cd4998129a`  |
| 1183   | No file  | `a6cd4998129a`  |
| 1177   | No file  | `a6cd4998129a`  |
| 1173   | No file  | `a6cd4998129a`  |
| 1167   | No file  | `a6cd4998129a`  |
| 1164   | No file  | `a6cd4998129a`  |
| 1156   | No file  | `a6cd4998129a`  |
| 1149   | No file  | `a6cd4998129a`  |
| 1144   | No file  | `a6cd4998129a`  |
| 1137   | No file  | `a6cd4998129a`  |
| 1132   | No file  | `a6cd4998129a`  |
| 1127   | No file  | `a6cd4998129a`  |
| 1122   | No file  | `a6cd4998129a`  |
| 1118   | No file  | `a6cd4998129a`  |
| 1114   | No file  | `a6cd4998129a`  |
| 1109   | No file  | `a6cd4998129a`  |
| 1102   | No file  | `a6cd4998129a`  |
| 1096   | No file  | `a6cd4998129a`  |
| 1088   | No file  | `a6cd4998129a`  |
| 1081   | No file  | `a6cd4998129a`  |
| 1076   | No file  | `a6cd4998129a`  |
| 1069   | No file  | `a6cd4998129a`  |
| 1064   | No file  | `a6cd4998129a`  |
| 1058   | No file  | `a6cd4998129a`  |
| 1051   | No file  | `a6cd4998129a`  |
| 1044   | No file  | `a6cd4998129a`  |
| 1036   | No file  | `a6cd4998129a`  |
| 1026   | No file  | `a6cd4998129a`  |
| 1016   | No file  | `a6cd4998129a`  |
| 1009   | No file  | `a6cd4998129a`  |
| 1005   | No file  | `a6cd4998129a`  |
| 1000   | No file  | `a6cd4998129a`  |
| 998    | No file  | `a6cd4998129a`  |
| 990    | No file  | `a6cd4998129a`  |
| 979    | No file  | `a6cd4998129a`  |
| 972    | No file  | `a6cd4998129a`  |
| 963    | No file  | `a6cd4998129a`  |
| 955    | No file  | `a6cd4998129a`  |
| 946    | No file  | `a6cd4998129a`  |
| 938    | No file  | `a6cd4998129a`  |
| 927    | No file  | `a6cd4998129a`  |
| 911    | No file  | `a6cd4998129a`  |
| 904    | No file  | `a6cd4998129a`  |
| 899    | No file  | `a6cd4998129a`  |
| 894    | No file  | `a6cd4998129a`  |
| 885    | No file  | `a6cd4998129a`  |
| 879    | No file  | `a6cd4998129a`  |
| 872    | No file  | `a6cd4998129a`  |
| 864    | No file  | `a6cd4998129a`  |
| 855    | No file  | `a6cd4998129a`  |
| 853    | No file  | `a6cd4998129a`  |
| 845    | No file  | `a6cd4998129a`  |
| 837    | No file  | `a6cd4998129a`  |
| 829    | No file  | `a6cd4998129a`  |
| 822    | No file  | `a6cd4998129a`  |
| 814    | No file  | `a6cd4998129a`  |
| 805    | No file  | `a6cd4998129a`  |
| 794    | No file  | `a6cd4998129a`  |
| 787    | No file  | `a6cd4998129a`  |
| 780    | No file  | `a6cd4998129a`  |
| 771    | No file  | `a6cd4998129a`  |
| 760    | No file  | `a6cd4998129a`  |
| 748    | No file  | `a6cd4998129a`  |
| 741    | No file  | `a6cd4998129a`  |
| 736    | No file  | `a6cd4998129a`  |
| 731    | No file  | `a6cd4998129a`  |
| 723    | No file  | `a6cd4998129a`  |
| 711    | No file  | `a6cd4998129a`  |
| 707    | No file  | `a6cd4998129a`  |
| 697    | No file  | `a6cd4998129a`  |
| 689    | No file  | `a6cd4998129a`  |
| 683    | No file  | `a6cd4998129a`  |
| 678    | No file  | `a6cd4998129a`  |
| 670    | No file  | `a6cd4998129a`  |
| 661    | No file  | `a6cd4998129a`  |
| 656    | No file  | `a6cd4998129a`  |
| 652    | No file  | `a6cd4998129a`  |
| 643    | No file  | `a6cd4998129a`  |
| 637    | No file  | `a6cd4998129a`  |
| 630    | No file  | `a6cd4998129a`  |
| 627    | No file  | `a6cd4998129a`  |
| 621    | No file  | `a6cd4998129a`  |
| 617    | No file  | `a6cd4998129a`  |
| 615    | No file  | `a6cd4998129a`  |
| 606    | No file  | `a6cd4998129a`  |
| 599    | No file  | `a6cd4998129a`  |
| 592    | No file  | `a6cd4998129a`  |
| 586    | No file  | `a6cd4998129a`  |
| 577    | No file  | `a6cd4998129a`  |
| 569    | No file  | `a6cd4998129a`  |
| 561    | No file  | `a6cd4998129a`  |
| 554    | No file  | `a6cd4998129a`  |
| 542    | No file  | `a6cd4998129a`  |
| 532    | No file  | `a6cd4998129a`  |
| 531    | No file  | `a6cd4998129a`  |
| 526    | No file  | `a6cd4998129a`  |
| 521    | No file  | `a6cd4998129a`  |
| 517    | No file  | `a6cd4998129a`  |
| 510    | No file  | `a6cd4998129a`  |
| 508    | No file  | `a6cd4998129a`  |
| 504    | No file  | `a6cd4998129a`  |
| 497    | No file  | `a6cd4998129a`  |
| 491    | No file  | `a6cd4998129a`  |
| 485    | No file  | `a6cd4998129a`  |
| 478    | No file  | `a6cd4998129a`  |
| 472    | No file  | `a6cd4998129a`  |
| 466    | No file  | `a6cd4998129a`  |
| 457    | No file  | `a6cd4998129a`  |
| 452    | No file  | `a6cd4998129a`  |
| 449    | No file  | `a6cd4998129a`  |
| 435    | No file  | `a6cd4998129a`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                      |
| --------------------- | -------- | --------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Painting names (type 126) and drop item names (type 0)    |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of paintings; `14` on client 3482      |
| `+0x08`             | Row[row_count] | rows         | See Row; in type order                        |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 17 bytes + unknown_0d list)

| Offset            | Type             | Field                   | Notes                                                                          |
| ----------------- | ---------------- | ----------------------- | ------------------------------------------------------------------------------ |
| `+0x00`           | u8               | landscape_painting_type | The painting, `0` to `13`; LOC type 126 name. See Paintings                    |
| `+0x01`           | u32              | unknown_01              | `30009` plus `landscape_painting_type` on every row (client 3482)              |
| `+0x05`           | u32              | name_index              | Index into `strings`: the Korean name; equal to the type on every row          |
| `+0x09`           | u32              | unknown_09              | Number of `unknown_0d` entries; `234` to `284` on client 3482                  |
| `+0x0D`           | u32[unknown_09]  | unknown_0d              | Keys `217619` to `226141` on client 3482; see Open Questions                   |
| `unknown_0d+0x00` | u32              | drop_item_key           | The treasure piece (LOC type 0 name); the window opens the drop search on its name |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                            |
| ------- | ------------------ | ------------ | ------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `14` on client 3482           |
| `+0x04` | pstr[string_count] | strings      | The Korean painting names, UTF-16LE, in row order |

## Layout 1

No `drop_item_key`: the row ends with the `unknown_0d` list. 12 paintings
on client 3251. Only the Row differs from Layout 2.

### Row (variable: 13 bytes + unknown_0d list)

| Offset  | Type            | Field                   | Notes |
| ------- | --------------- | ----------------------- | ----- |
| `+0x00` | u8              | landscape_painting_type |       |
| `+0x01` | u32             | unknown_01              |       |
| `+0x05` | u32             | name_index              |       |
| `+0x09` | u32             | unknown_09              |       |
| `+0x0D` | u32[unknown_09] | unknown_0d              |       |

## Paintings

Client 3482, in file order. The type is the index the window Lua passes
to every `ToClient_*LandScapePainting*` call; its `_indexForType` table
names the same order with the `__eLandscapePaintingType_*` members, whose
numbers are not in the Lua. LOC type 126 `str_id1` is the type.

| Type | LOC type 126 name         | Lua member               | `drop_item_key`                                    |
| ---- | ------------------------- | ------------------------ | -------------------------------------------------- |
| 0    | Roud Sulfur Mine          | `Sulfur`                 | 44273 Archaeologist's Map Piece                    |
| 1    | Pila Ku Jail              | `PilaKu`                 | 44273 Archaeologist's Map Piece                    |
| 2    | Aakman Temple             | `Aakman`                 | 44278 Lafi Bedmountain's Upgraded Compass Parts    |
| 3    | Hystria Ruins             | `Hystria`                | 44278 Lafi Bedmountain's Upgraded Compass Parts    |
| 4    | Sycraia Underwater Ruins  | `SycraiaUpper`           | 44270 Al Yurad's Ring Piece                        |
| 5    | Padix Island              | `Padix`                  | 44270 Al Yurad's Ring Piece                        |
| 6    | Ash Forest                | `AshForest`              | 44270 Al Yurad's Ring Piece                        |
| 7    | Crypt of Resting Thoughts | `CryptOfRestingThoughts` | 44270 Al Yurad's Ring Piece                        |
| 8    | Olun's Valley             | `OlunsValley`            | 44270 Al Yurad's Ring Piece                        |
| 9    | City of the Dead          | `CityOfTheDead`          | 65331 Lafi Bedmountain's Upgraded Telescope Parts  |
| 10   | Tungrad Ruins             | `Tungrad`                | 65331 Lafi Bedmountain's Upgraded Telescope Parts  |
| 11   | Darkseekers' Retreat      | `Darkseekers`            | 65331 Lafi Bedmountain's Upgraded Telescope Parts  |
| 12   | Gavinya Coastal Cliff     | `SulfurGolem`            | 44270 Al Yurad's Ring Piece                        |
| 13   | La Orzeca                 | `LaOrzeca`               | 45013 Quturan's Left Lung                          |

## Notes

- The paints that charge a painting (Roud Sulfur Mine Paint `761714`,
  Pila Ku Jail Paint `761715`, Aakman Temple Paint `761716`) are items
  with `contents_event_type` `154` in `itemenchant.dbss`, their
  `contents_event_param1` the painting type and `contents_event_param2`
  the points (`10000`). The window reads the points with
  `getContentsEventParam2()`.
- The file is not in client 1784.

## Open Questions

### What `unknown_0d` Lists

Each row lists 234 to 284 u32 keys between `217619` and `226141` (client
3482); the lists of the 14 paintings are nearly the same, so they do not
name the monsters of one area. No other `gamecommondata/binary` table of
client 3482 holds these values, and they are no item or character keys.

### What `unknown_01` Is

`unknown_01` runs from `30009` to `30022`, one per painting. LOC type 0
and 10 have names under these numbers (`30009` Tachros), which do not fit
the paintings, so the key is from another table.
