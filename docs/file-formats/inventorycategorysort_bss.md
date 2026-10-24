# `inventorycategorysort.bss` Format

## Purpose

The categories of the inventory's category view: one row per category
with its Korean name and two bytes. The inventory Lua
(`panel_window_inventory_all_6.luac`) builds one group per category type
from `0` to `__eInvenCategoryType_Count - 1`, titles it with
`ToClient_getCategoryNameByType(categoryType)`, and orders the groups by
`ToClient_getCategoryShowIndexByType(categoryType)`. Each item's group
comes from `getInventCategoryType()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | --------------------------- | ----- | ------- | ----------------------- |
| 1      | 2259 and later | 3483    | `inventorycategorysort.bss` | 416   | 20 Row  | 15 to 29, 21 on average |

| Layout | File                        | Known         | Unknown     |
| ------ | --------------------------- | ------------- | ----------- |
| 1      | `inventorycategorysort.bss` | 396 B (95.2%) | 20 B (4.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `edea77d873a3`  |
| 3482   | Layout 1 | `edea77d873a3`  |
| 3474   | Layout 1 | `edea77d873a3`  |
| 3473   | Layout 1 | `edea77d873a3`  |
| 3464   | Layout 1 | `edea77d873a3`  |
| 3458   | Layout 1 | `edea77d873a3`  |
| 3454   | Layout 1 | `edea77d873a3`  |
| 3444   | Layout 1 | `edea77d873a3`  |
| 3435   | Layout 1 | `edea77d873a3`  |
| 3426   | Layout 1 | `edea77d873a3`  |
| 3418   | Layout 1 | `edea77d873a3`  |
| 3412   | Layout 1 | `edea77d873a3`  |
| 3402   | Layout 1 | `edea77d873a3`  |
| 3396   | Layout 1 | `edea77d873a3`  |
| 3387   | Layout 1 | `edea77d873a3`  |
| 3381   | Layout 1 | `edea77d873a3`  |
| 3373   | Layout 1 | `edea77d873a3`  |
| 3364   | Layout 1 | `edea77d873a3`  |
| 3356   | Layout 1 | `edea77d873a3`  |
| 3349   | Layout 1 | `edea77d873a3`  |
| 3342   | Layout 1 | `edea77d873a3`  |
| 3335   | Layout 1 | `edea77d873a3`  |
| 3326   | Layout 1 | `edea77d873a3`  |
| 3321   | Layout 1 | `edea77d873a3`  |
| 3314   | Layout 1 | `edea77d873a3`  |
| 3303   | Layout 1 | `edea77d873a3`  |
| 3302   | Layout 1 | `edea77d873a3`  |
| 3293   | Layout 1 | `edea77d873a3`  |
| 3283   | Layout 1 | `edea77d873a3`  |
| 3275   | Layout 1 | `edea77d873a3`  |
| 3267   | Layout 1 | `edea77d873a3`  |
| 3258   | Layout 1 | `edea77d873a3`  |
| 3251   | Layout 1 | `edea77d873a3`  |
| 3242   | Layout 1 | `edea77d873a3`  |
| 3235   | Layout 1 | `edea77d873a3`  |
| 3229   | Layout 1 | `edea77d873a3`  |
| 3212   | Layout 1 | `edea77d873a3`  |
| 3203   | Layout 1 | `edea77d873a3`  |
| 3193   | Layout 1 | `edea77d873a3`  |
| 3186   | Layout 1 | `edea77d873a3`  |
| 3177   | Layout 1 | `edea77d873a3`  |
| 3169   | Layout 1 | `edea77d873a3`  |
| 3158   | Layout 1 | `edea77d873a3`  |
| 3151   | Layout 1 | `edea77d873a3`  |
| 3144   | Layout 1 | `edea77d873a3`  |
| 3133   | Layout 1 | `edea77d873a3`  |
| 3125   | Layout 1 | `edea77d873a3`  |
| 3118   | Layout 1 | `edea77d873a3`  |
| 3111   | Layout 1 | `edea77d873a3`  |
| 3103   | Layout 1 | `edea77d873a3`  |
| 3095   | Layout 1 | `edea77d873a3`  |
| 3086   | Layout 1 | `edea77d873a3`  |
| 3072   | Layout 1 | `edea77d873a3`  |
| 3062   | Layout 1 | `edea77d873a3`  |
| 3052   | Layout 1 | `edea77d873a3`  |
| 3045   | Layout 1 | `edea77d873a3`  |
| 3037   | Layout 1 | `edea77d873a3`  |
| 3030   | Layout 1 | `edea77d873a3`  |
| 3021   | Layout 1 | `edea77d873a3`  |
| 3012   | Layout 1 | `edea77d873a3`  |
| 3002   | Layout 1 | `edea77d873a3`  |
| 2995   | Layout 1 | `edea77d873a3`  |
| 2987   | Layout 1 | `edea77d873a3`  |
| 2978   | Layout 1 | `edea77d873a3`  |
| 2970   | Layout 1 | `edea77d873a3`  |
| 2959   | Layout 1 | `edea77d873a3`  |
| 2951   | Layout 1 | `edea77d873a3`  |
| 2942   | Layout 1 | `edea77d873a3`  |
| 2935   | Layout 1 | `edea77d873a3`  |
| 2932   | Layout 1 | `edea77d873a3`  |
| 2923   | Layout 1 | `edea77d873a3`  |
| 2919   | Layout 1 | `edea77d873a3`  |
| 2907   | Layout 1 | `edea77d873a3`  |
| 2900   | Layout 1 | `edea77d873a3`  |
| 2891   | Layout 1 | `edea77d873a3`  |
| 2882   | Layout 1 | `edea77d873a3`  |
| 2872   | Layout 1 | `edea77d873a3`  |
| 2863   | Layout 1 | `edea77d873a3`  |
| 2855   | Layout 1 | `edea77d873a3`  |
| 2849   | Layout 1 | `edea77d873a3`  |
| 2844   | Layout 1 | `edea77d873a3`  |
| 2834   | Layout 1 | `edea77d873a3`  |
| 2825   | Layout 1 | `edea77d873a3`  |
| 2819   | Layout 1 | `edea77d873a3`  |
| 2811   | Layout 1 | `edea77d873a3`  |
| 2803   | Layout 1 | `edea77d873a3`  |
| 2794   | Layout 1 | `edea77d873a3`  |
| 2783   | Layout 1 | `edea77d873a3`  |
| 2774   | Layout 1 | `edea77d873a3`  |
| 2765   | Layout 1 | `edea77d873a3`  |
| 2756   | Layout 1 | `edea77d873a3`  |
| 2750   | Layout 1 | `edea77d873a3`  |
| 2743   | Layout 1 | `edea77d873a3`  |
| 2736   | Layout 1 | `edea77d873a3`  |
| 2726   | Layout 1 | `edea77d873a3`  |
| 2717   | Layout 1 | `edea77d873a3`  |
| 2709   | Layout 1 | `edea77d873a3`  |
| 2703   | Layout 1 | `edea77d873a3`  |
| 2695   | Layout 1 | `edea77d873a3`  |
| 2684   | Layout 1 | `edea77d873a3`  |
| 2672   | Layout 1 | `edea77d873a3`  |
| 2665   | Layout 1 | `edea77d873a3`  |
| 2657   | Layout 1 | `edea77d873a3`  |
| 2649   | Layout 1 | `edea77d873a3`  |
| 2644   | Layout 1 | `edea77d873a3`  |
| 2637   | Layout 1 | `edea77d873a3`  |
| 2629   | Layout 1 | `edea77d873a3`  |
| 2619   | Layout 1 | `edea77d873a3`  |
| 2612   | Layout 1 | `edea77d873a3`  |
| 2606   | Layout 1 | `edea77d873a3`  |
| 2602   | Layout 1 | `edea77d873a3`  |
| 2601   | Layout 1 | `edea77d873a3`  |
| 2592   | Layout 1 | `edea77d873a3`  |
| 2583   | Layout 1 | `edea77d873a3`  |
| 2575   | Layout 1 | `edea77d873a3`  |
| 2567   | Layout 1 | `edea77d873a3`  |
| 2560   | Layout 1 | `edea77d873a3`  |
| 2553   | Layout 1 | `edea77d873a3`  |
| 2545   | Layout 1 | `edea77d873a3`  |
| 2538   | Layout 1 | `edea77d873a3`  |
| 2529   | Layout 1 | `edea77d873a3`  |
| 2519   | Layout 1 | `edea77d873a3`  |
| 2513   | Layout 1 | `edea77d873a3`  |
| 2510   | Layout 1 | `edea77d873a3`  |
| 2507   | Layout 1 | `edea77d873a3`  |
| 2503   | Layout 1 | `edea77d873a3`  |
| 2498   | Layout 1 | `edea77d873a3`  |
| 2492   | Layout 1 | `edea77d873a3`  |
| 2487   | Layout 1 | `edea77d873a3`  |
| 2480   | Layout 1 | `edea77d873a3`  |
| 2474   | Layout 1 | `edea77d873a3`  |
| 2468   | Layout 1 | `edea77d873a3`  |
| 2460   | Layout 1 | `edea77d873a3`  |
| 2453   | Layout 1 | `edea77d873a3`  |
| 2444   | Layout 1 | `edea77d873a3`  |
| 2438   | Layout 1 | `edea77d873a3`  |
| 2434   | Layout 1 | `edea77d873a3`  |
| 2429   | Layout 1 | `edea77d873a3`  |
| 2421   | Layout 1 | `edea77d873a3`  |
| 2414   | Layout 1 | `edea77d873a3`  |
| 2407   | Layout 1 | `edea77d873a3`  |
| 2401   | Layout 1 | `edea77d873a3`  |
| 2397   | Layout 1 | `edea77d873a3`  |
| 2393   | Layout 1 | `edea77d873a3`  |
| 2384   | Layout 1 | `edea77d873a3`  |
| 2378   | Layout 1 | `edea77d873a3`  |
| 2372   | Layout 1 | `edea77d873a3`  |
| 2358   | Layout 1 | `edea77d873a3`  |
| 2352   | Layout 1 | `edea77d873a3`  |
| 2347   | Layout 1 | `edea77d873a3`  |
| 2343   | Layout 1 | `edea77d873a3`  |
| 2335   | Layout 1 | `edea77d873a3`  |
| 2327   | Layout 1 | `edea77d873a3`  |
| 2324   | Layout 1 | `edea77d873a3`  |
| 2319   | Layout 1 | `edea77d873a3`  |
| 2313   | Layout 1 | `edea77d873a3`  |
| 2308   | Layout 1 | `edea77d873a3`  |
| 2302   | Layout 1 | `edea77d873a3`  |
| 2295   | Layout 1 | `edea77d873a3`  |
| 2290   | Layout 1 | `edea77d873a3`  |
| 2284   | Layout 1 | `edea77d873a3`  |
| 2276   | Layout 1 | `edea77d873a3`  |
| 2269   | Layout 1 | `edea77d873a3`  |
| 2259   | Layout 1 | `edea77d873a3`  |
| 2250   | No file  | `edea77d873a3`  |
| 2243   | No file  | `edea77d873a3`  |
| 2235   | No file  | `edea77d873a3`  |
| 2229   | No file  | `edea77d873a3`  |
| 2224   | No file  | `edea77d873a3`  |
| 2218   | No file  | `edea77d873a3`  |
| 2215   | No file  | `edea77d873a3`  |
| 2207   | No file  | `edea77d873a3`  |
| 2203   | No file  | `edea77d873a3`  |
| 2196   | No file  | `edea77d873a3`  |
| 2192   | No file  | `edea77d873a3`  |
| 2189   | No file  | `edea77d873a3`  |
| 2183   | No file  | `edea77d873a3`  |
| 2179   | No file  | `edea77d873a3`  |
| 2171   | No file  | `edea77d873a3`  |
| 2163   | No file  | `edea77d873a3`  |
| 2156   | No file  | `edea77d873a3`  |
| 2151   | No file  | `edea77d873a3`  |
| 2147   | No file  | `edea77d873a3`  |
| 2142   | No file  | `edea77d873a3`  |
| 2138   | No file  | `edea77d873a3`  |
| 2134   | No file  | `edea77d873a3`  |
| 2130   | No file  | `edea77d873a3`  |
| 2122   | No file  | `edea77d873a3`  |
| 2107   | No file  | `edea77d873a3`  |
| 2098   | No file  | `edea77d873a3`  |
| 2089   | No file  | `edea77d873a3`  |
| 2081   | No file  | `edea77d873a3`  |
| 2073   | No file  | `edea77d873a3`  |
| 2067   | No file  | `edea77d873a3`  |
| 2063   | No file  | `edea77d873a3`  |
| 2059   | No file  | `edea77d873a3`  |
| 2052   | No file  | `edea77d873a3`  |
| 2044   | No file  | `edea77d873a3`  |
| 2039   | No file  | `edea77d873a3`  |
| 2032   | No file  | `edea77d873a3`  |
| 2025   | No file  | `edea77d873a3`  |
| 2011   | No file  | `edea77d873a3`  |
| 2005   | No file  | `edea77d873a3`  |
| 2000   | No file  | `edea77d873a3`  |
| 1996   | No file  | `edea77d873a3`  |
| 1991   | No file  | `edea77d873a3`  |
| 1985   | No file  | `edea77d873a3`  |
| 1980   | No file  | `edea77d873a3`  |
| 1969   | No file  | `edea77d873a3`  |
| 1964   | No file  | `edea77d873a3`  |
| 1958   | No file  | `edea77d873a3`  |
| 1950   | No file  | `edea77d873a3`  |
| 1945   | No file  | `edea77d873a3`  |
| 1937   | No file  | `edea77d873a3`  |
| 1933   | No file  | `edea77d873a3`  |
| 1927   | No file  | `edea77d873a3`  |
| 1921   | No file  | `edea77d873a3`  |
| 1914   | No file  | `edea77d873a3`  |
| 1908   | No file  | `edea77d873a3`  |
| 1897   | No file  | `edea77d873a3`  |
| 1892   | No file  | `edea77d873a3`  |
| 1886   | No file  | `edea77d873a3`  |
| 1881   | No file  | `edea77d873a3`  |
| 1871   | No file  | `edea77d873a3`  |
| 1866   | No file  | `edea77d873a3`  |
| 1862   | No file  | `edea77d873a3`  |
| 1854   | No file  | `edea77d873a3`  |
| 1846   | No file  | `edea77d873a3`  |
| 1838   | No file  | `edea77d873a3`  |
| 1832   | No file  | `edea77d873a3`  |
| 1826   | No file  | `edea77d873a3`  |
| 1822   | No file  | `edea77d873a3`  |
| 1818   | No file  | `edea77d873a3`  |
| 1804   | No file  | `edea77d873a3`  |
| 1794   | No file  | `edea77d873a3`  |
| 1790   | No file  | `edea77d873a3`  |
| 1784   | No file  | `edea77d873a3`  |
| 1774   | No file  | `edea77d873a3`  |
| 1771   | No file  | `edea77d873a3`  |
| 1762   | No file  | `edea77d873a3`  |
| 1759   | No file  | `edea77d873a3`  |
| 1754   | No file  | `edea77d873a3`  |
| 1749   | No file  | `edea77d873a3`  |
| 1743   | No file  | `edea77d873a3`  |
| 1737   | No file  | `edea77d873a3`  |
| 1731   | No file  | `edea77d873a3`  |
| 1725   | No file  | `edea77d873a3`  |
| 1717   | No file  | `edea77d873a3`  |
| 1710   | No file  | `edea77d873a3`  |
| 1704   | No file  | `edea77d873a3`  |
| 1698   | No file  | `edea77d873a3`  |
| 1690   | No file  | `edea77d873a3`  |
| 1685   | No file  | `edea77d873a3`  |
| 1680   | No file  | `edea77d873a3`  |
| 1674   | No file  | `edea77d873a3`  |
| 1668   | No file  | `edea77d873a3`  |
| 1659   | No file  | `edea77d873a3`  |
| 1649   | No file  | `edea77d873a3`  |
| 1642   | No file  | `edea77d873a3`  |
| 1636   | No file  | `edea77d873a3`  |
| 1628   | No file  | `edea77d873a3`  |
| 1622   | No file  | `edea77d873a3`  |
| 1614   | No file  | `edea77d873a3`  |
| 1608   | No file  | `edea77d873a3`  |
| 1602   | No file  | `edea77d873a3`  |
| 1598   | No file  | `edea77d873a3`  |
| 1594   | No file  | `edea77d873a3`  |
| 1590   | No file  | `edea77d873a3`  |
| 1587   | No file  | `edea77d873a3`  |
| 1584   | No file  | `edea77d873a3`  |
| 1579   | No file  | `edea77d873a3`  |
| 1572   | No file  | `edea77d873a3`  |
| 1565   | No file  | `edea77d873a3`  |
| 1559   | No file  | `edea77d873a3`  |
| 1554   | No file  | `edea77d873a3`  |
| 1547   | No file  | `edea77d873a3`  |
| 1537   | No file  | `edea77d873a3`  |
| 1529   | No file  | `edea77d873a3`  |
| 1524   | No file  | `edea77d873a3`  |
| 1519   | No file  | `edea77d873a3`  |
| 1509   | No file  | `edea77d873a3`  |
| 1506   | No file  | `edea77d873a3`  |
| 1504   | No file  | `edea77d873a3`  |
| 1500   | No file  | `edea77d873a3`  |
| 1493   | No file  | `edea77d873a3`  |
| 1489   | No file  | `edea77d873a3`  |
| 1485   | No file  | `edea77d873a3`  |
| 1481   | No file  | `edea77d873a3`  |
| 1474   | No file  | `edea77d873a3`  |
| 1466   | No file  | `edea77d873a3`  |
| 1462   | No file  | `edea77d873a3`  |
| 1459   | No file  | `edea77d873a3`  |
| 1453   | No file  | `edea77d873a3`  |
| 1450   | No file  | `edea77d873a3`  |
| 1445   | No file  | `edea77d873a3`  |
| 1439   | No file  | `edea77d873a3`  |
| 1433   | No file  | `edea77d873a3`  |
| 1430   | No file  | `edea77d873a3`  |
| 1426   | No file  | `edea77d873a3`  |
| 1421   | No file  | `edea77d873a3`  |
| 1417   | No file  | `edea77d873a3`  |
| 1416   | No file  | `edea77d873a3`  |
| 1409   | No file  | `edea77d873a3`  |
| 1405   | No file  | `edea77d873a3`  |
| 1401   | No file  | `edea77d873a3`  |
| 1396   | No file  | `edea77d873a3`  |
| 1391   | No file  | `edea77d873a3`  |
| 1390   | No file  | `edea77d873a3`  |
| 1386   | No file  | `edea77d873a3`  |
| 1381   | No file  | `edea77d873a3`  |
| 1379   | No file  | `edea77d873a3`  |
| 1372   | No file  | `edea77d873a3`  |
| 1366   | No file  | `edea77d873a3`  |
| 1364   | No file  | `edea77d873a3`  |
| 1363   | No file  | `edea77d873a3`  |
| 1360   | No file  | `edea77d873a3`  |
| 1358   | No file  | `edea77d873a3`  |
| 1355   | No file  | `edea77d873a3`  |
| 1351   | No file  | `edea77d873a3`  |
| 1348   | No file  | `edea77d873a3`  |
| 1346   | No file  | `edea77d873a3`  |
| 1341   | No file  | `edea77d873a3`  |
| 1340   | No file  | `edea77d873a3`  |
| 1338   | No file  | `edea77d873a3`  |
| 1335   | No file  | `edea77d873a3`  |
| 1333   | No file  | `edea77d873a3`  |
| 1329   | No file  | `edea77d873a3`  |
| 1327   | No file  | `edea77d873a3`  |
| 1324   | No file  | `edea77d873a3`  |
| 1321   | No file  | `edea77d873a3`  |
| 1319   | No file  | `edea77d873a3`  |
| 1318   | No file  | `edea77d873a3`  |
| 1316   | No file  | `edea77d873a3`  |
| 1313   | No file  | `edea77d873a3`  |
| 1311   | No file  | `edea77d873a3`  |
| 1309   | No file  | `edea77d873a3`  |
| 1304   | No file  | `edea77d873a3`  |
| 1292   | No file  | `edea77d873a3`  |
| 1286   | No file  | `edea77d873a3`  |
| 1280   | No file  | `edea77d873a3`  |
| 1276   | No file  | `edea77d873a3`  |
| 1267   | No file  | `edea77d873a3`  |
| 1261   | No file  | `edea77d873a3`  |
| 1256   | No file  | `edea77d873a3`  |
| 1250   | No file  | `edea77d873a3`  |
| 1246   | No file  | `edea77d873a3`  |
| 1239   | No file  | `edea77d873a3`  |
| 1230   | No file  | `edea77d873a3`  |
| 1226   | No file  | `edea77d873a3`  |
| 1220   | No file  | `edea77d873a3`  |
| 1217   | No file  | `edea77d873a3`  |
| 1211   | No file  | `edea77d873a3`  |
| 1210   | No file  | `edea77d873a3`  |
| 1208   | No file  | `edea77d873a3`  |
| 1203   | No file  | `edea77d873a3`  |
| 1197   | No file  | `edea77d873a3`  |
| 1194   | No file  | `edea77d873a3`  |
| 1192   | No file  | `edea77d873a3`  |
| 1187   | No file  | `edea77d873a3`  |
| 1183   | No file  | `edea77d873a3`  |
| 1177   | No file  | `edea77d873a3`  |
| 1173   | No file  | `edea77d873a3`  |
| 1167   | No file  | `edea77d873a3`  |
| 1164   | No file  | `edea77d873a3`  |
| 1156   | No file  | `edea77d873a3`  |
| 1149   | No file  | `edea77d873a3`  |
| 1144   | No file  | `edea77d873a3`  |
| 1137   | No file  | `edea77d873a3`  |
| 1132   | No file  | `edea77d873a3`  |
| 1127   | No file  | `edea77d873a3`  |
| 1122   | No file  | `edea77d873a3`  |
| 1118   | No file  | `edea77d873a3`  |
| 1114   | No file  | `edea77d873a3`  |
| 1109   | No file  | `edea77d873a3`  |
| 1102   | No file  | `edea77d873a3`  |
| 1096   | No file  | `edea77d873a3`  |
| 1088   | No file  | `edea77d873a3`  |
| 1081   | No file  | `edea77d873a3`  |
| 1076   | No file  | `edea77d873a3`  |
| 1069   | No file  | `edea77d873a3`  |
| 1064   | No file  | `edea77d873a3`  |
| 1058   | No file  | `edea77d873a3`  |
| 1051   | No file  | `edea77d873a3`  |
| 1044   | No file  | `edea77d873a3`  |
| 1036   | No file  | `edea77d873a3`  |
| 1026   | No file  | `edea77d873a3`  |
| 1016   | No file  | `edea77d873a3`  |
| 1009   | No file  | `edea77d873a3`  |
| 1005   | No file  | `edea77d873a3`  |
| 1000   | No file  | `edea77d873a3`  |
| 998    | No file  | `edea77d873a3`  |
| 990    | No file  | `edea77d873a3`  |
| 979    | No file  | `edea77d873a3`  |
| 972    | No file  | `edea77d873a3`  |
| 963    | No file  | `edea77d873a3`  |
| 955    | No file  | `edea77d873a3`  |
| 946    | No file  | `edea77d873a3`  |
| 938    | No file  | `edea77d873a3`  |
| 927    | No file  | `edea77d873a3`  |
| 911    | No file  | `edea77d873a3`  |
| 904    | No file  | `edea77d873a3`  |
| 899    | No file  | `edea77d873a3`  |
| 894    | No file  | `edea77d873a3`  |
| 885    | No file  | `edea77d873a3`  |
| 879    | No file  | `edea77d873a3`  |
| 872    | No file  | `edea77d873a3`  |
| 864    | No file  | `edea77d873a3`  |
| 855    | No file  | `edea77d873a3`  |
| 853    | No file  | `edea77d873a3`  |
| 845    | No file  | `edea77d873a3`  |
| 837    | No file  | `edea77d873a3`  |
| 829    | No file  | `edea77d873a3`  |
| 822    | No file  | `edea77d873a3`  |
| 814    | No file  | `edea77d873a3`  |
| 805    | No file  | `edea77d873a3`  |
| 794    | No file  | `edea77d873a3`  |
| 787    | No file  | `edea77d873a3`  |
| 780    | No file  | `edea77d873a3`  |
| 771    | No file  | `edea77d873a3`  |
| 760    | No file  | `edea77d873a3`  |
| 748    | No file  | `edea77d873a3`  |
| 741    | No file  | `edea77d873a3`  |
| 736    | No file  | `edea77d873a3`  |
| 731    | No file  | `edea77d873a3`  |
| 723    | No file  | `edea77d873a3`  |
| 711    | No file  | `edea77d873a3`  |
| 707    | No file  | `edea77d873a3`  |
| 697    | No file  | `edea77d873a3`  |
| 689    | No file  | `edea77d873a3`  |
| 683    | No file  | `edea77d873a3`  |
| 678    | No file  | `edea77d873a3`  |
| 670    | No file  | `edea77d873a3`  |
| 661    | No file  | `edea77d873a3`  |
| 656    | No file  | `edea77d873a3`  |
| 652    | No file  | `edea77d873a3`  |
| 643    | No file  | `edea77d873a3`  |
| 637    | No file  | `edea77d873a3`  |
| 630    | No file  | `edea77d873a3`  |
| 627    | No file  | `edea77d873a3`  |
| 621    | No file  | `edea77d873a3`  |
| 617    | No file  | `edea77d873a3`  |
| 615    | No file  | `edea77d873a3`  |
| 606    | No file  | `edea77d873a3`  |
| 599    | No file  | `edea77d873a3`  |
| 592    | No file  | `edea77d873a3`  |
| 586    | No file  | `edea77d873a3`  |
| 577    | No file  | `edea77d873a3`  |
| 569    | No file  | `edea77d873a3`  |
| 561    | No file  | `edea77d873a3`  |
| 554    | No file  | `edea77d873a3`  |
| 542    | No file  | `edea77d873a3`  |
| 532    | No file  | `edea77d873a3`  |
| 531    | No file  | `edea77d873a3`  |
| 526    | No file  | `edea77d873a3`  |
| 521    | No file  | `edea77d873a3`  |
| 517    | No file  | `edea77d873a3`  |
| 510    | No file  | `edea77d873a3`  |
| 508    | No file  | `edea77d873a3`  |
| 504    | No file  | `edea77d873a3`  |
| 497    | No file  | `edea77d873a3`  |
| 491    | No file  | `edea77d873a3`  |
| 485    | No file  | `edea77d873a3`  |
| 478    | No file  | `edea77d873a3`  |
| 472    | No file  | `edea77d873a3`  |
| 466    | No file  | `edea77d873a3`  |
| 457    | No file  | `edea77d873a3`  |
| 452    | No file  | `edea77d873a3`  |
| 449    | No file  | `edea77d873a3`  |
| 435    | No file  | `edea77d873a3`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                           |
| --------------------- | -------- | ------------------------------ |
| `languagedata_en.loc` | Optional | Category names (type 122)      |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No PABR magic and no string table.

| Offset  | Type           | Field     | Notes                                       |
| ------- | -------------- | --------- | ------------------------------------------- |
| `+0x00` | u32            | row_count | Number of categories; `20` on client 3482   |
| `+0x04` | Row[row_count] | rows      | See Row                                     |

### Row (variable: 11 bytes + name text)

| Offset         | Type  | Field              | Notes                                                                      |
| -------------- | ----- | ------------------ | -------------------------------------------------------------------------- |
| `+0x00`        | u8    | category_key       | Row key, `0` to `19`, each once; rows run from `15` down to `0`, then `19` down to `16` |
| `+0x01`        | str16 | name_kr            | Korean name (`의뢰`, `가구`)                                               |
| `name_kr+0x00` | u8    | unknown_name_kr_00 | `0` to `19`, each once; see Open Questions                                 |
| `name_kr+0x01` | u8    | category_key_dup   | Equal to `category_key` on every row (client 3482)                         |

## Categories

Client 3482. LOC type 122 holds the name under `str_id1`
`unknown_name_kr_00` and `str_id2` `category_key`.

| `category_key` | `unknown_name_kr_00` | `name_kr`          | LOC type 122 name   |
| -------------- | -------------------- | ------------------ | ------------------- |
| 0              | 19                   | `기타`             | Etc.                |
| 1              | 0                    | `의뢰`             | Quest               |
| 2              | 13                   | `사용 가능 물품`   | Usable              |
| 3              | 2                    | `장착류`           | Equippable          |
| 4              | 4                    | `강화`             | Enhancement         |
| 5              | 3                    | `수정/광명석`      | Crystal/Lightstone  |
| 6              | 15                   | `탑승물/반려동물`  | Mount/Pet           |
| 7              | 14                   | `재료`             | Life Skill Material |
| 8              | 16                   | `무역`             | Trade               |
| 9              | 18                   | `기타`             | Etc.                |
| 10             | 17                   | `가구`             | Furniture           |
| 11             | 1                    | `잡동사니`         | Junk                |
| 12             | 6                    | `투구(의상)`       | Helmet              |
| 13             | 5                    | `개봉 가능 물품`   | Openable            |
| 14             | 7                    | `상의(의상)`       | Armor (Appearance)  |
| 15             | 8                    | `신발(의상)`       | Shoes               |
| 16             | 9                    | `장갑(의상)`       | Gloves              |
| 17             | 10                   | `무기(의상)`       | Weapon              |
| 18             | 11                   | `속옷(의상)`       | Underwear           |
| 19             | 12                   | `악세서리류(의상)` | Accessory           |

## Notes

- The file is not in client 1784.

## Open Questions

### Which Byte Is the Category Type

One of the two bytes is the category type that items carry and the other
the show index. `category_key` is copied at the row's end like other row
keys and starts with `기타` at `0`, which reads as an enum with a default
member; `unknown_name_kr_00` puts Quest first and the two `기타` rows last
(`18`, `19`), which reads as a display order. LOC type 122 keys the names
the other way round, `unknown_name_kr_00` first. An item whose inventory
category is known would settle it.
