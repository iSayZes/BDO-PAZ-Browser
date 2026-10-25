# `itemmovedata.bss` Format

## Purpose

The exception filters of the item move settings window
(`Panel_Window_ItemMoveSet`), which moves inventory items into storage: one
9-byte row per filter with the item type, item classify and contents event
type of the items it leaves out, and its Korean name. The window
(`panel_window_itemmoveset_1.luac`, client 3482) makes one checkbox per
filter from `ToClient_getItemMoveKeyCount()` and
`ToClient_getItemMoveKeyByIndex(index):get()`, labels it with
`ToClient_getMoveItemFilterName(keyRaw)` and, on Apply, passes each checked
filter to `ToClient_insertExceptionMoveItemKey(keyRaw)` and each unchecked
one to `ToClient_deleteExceptionMoveItemKey(keyRaw)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File               | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------ | ----- | ------- | --------- |
| 1      | 1614 and later | `itemmovedata.bss` | 156   | 4 Row   | 9         |

| Layout | File               | Known          | Unknown    |
| ------ | ------------------ | -------------- | ---------- |
| 1      | `itemmovedata.bss` | 156 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `06fdea284db2`  |
| 3482   | Layout 1 | `06fdea284db2`  |
| 3474   | Layout 1 | `06fdea284db2`  |
| 3473   | Layout 1 | `06fdea284db2`  |
| 3464   | Layout 1 | `06fdea284db2`  |
| 3458   | Layout 1 | `06fdea284db2`  |
| 3454   | Layout 1 | `06fdea284db2`  |
| 3444   | Layout 1 | `06fdea284db2`  |
| 3435   | Layout 1 | `06fdea284db2`  |
| 3426   | Layout 1 | `06fdea284db2`  |
| 3418   | Layout 1 | `06fdea284db2`  |
| 3412   | Layout 1 | `06fdea284db2`  |
| 3402   | Layout 1 | `06fdea284db2`  |
| 3396   | Layout 1 | `06fdea284db2`  |
| 3387   | Layout 1 | `06fdea284db2`  |
| 3381   | Layout 1 | `06fdea284db2`  |
| 3373   | Layout 1 | `06fdea284db2`  |
| 3364   | Layout 1 | `06fdea284db2`  |
| 3356   | Layout 1 | `06fdea284db2`  |
| 3349   | Layout 1 | `06fdea284db2`  |
| 3342   | Layout 1 | `06fdea284db2`  |
| 3335   | Layout 1 | `06fdea284db2`  |
| 3326   | Layout 1 | `06fdea284db2`  |
| 3321   | Layout 1 | `06fdea284db2`  |
| 3314   | Layout 1 | `06fdea284db2`  |
| 3303   | Layout 1 | `06fdea284db2`  |
| 3302   | Layout 1 | `06fdea284db2`  |
| 3293   | Layout 1 | `06fdea284db2`  |
| 3283   | Layout 1 | `06fdea284db2`  |
| 3275   | Layout 1 | `06fdea284db2`  |
| 3267   | Layout 1 | `06fdea284db2`  |
| 3258   | Layout 1 | `06fdea284db2`  |
| 3251   | Layout 1 | `06fdea284db2`  |
| 3242   | Layout 1 | `06fdea284db2`  |
| 3235   | Layout 1 | `06fdea284db2`  |
| 3229   | Layout 1 | `06fdea284db2`  |
| 3212   | Layout 1 | `06fdea284db2`  |
| 3203   | Layout 1 | `06fdea284db2`  |
| 3193   | Layout 1 | `06fdea284db2`  |
| 3186   | Layout 1 | `06fdea284db2`  |
| 3177   | Layout 1 | `06fdea284db2`  |
| 3169   | Layout 1 | `06fdea284db2`  |
| 3158   | Layout 1 | `06fdea284db2`  |
| 3151   | Layout 1 | `06fdea284db2`  |
| 3144   | Layout 1 | `06fdea284db2`  |
| 3133   | Layout 1 | `06fdea284db2`  |
| 3125   | Layout 1 | `06fdea284db2`  |
| 3118   | Layout 1 | `06fdea284db2`  |
| 3111   | Layout 1 | `06fdea284db2`  |
| 3103   | Layout 1 | `06fdea284db2`  |
| 3095   | Layout 1 | `06fdea284db2`  |
| 3086   | Layout 1 | `06fdea284db2`  |
| 3072   | Layout 1 | `06fdea284db2`  |
| 3062   | Layout 1 | `06fdea284db2`  |
| 3052   | Layout 1 | `06fdea284db2`  |
| 3045   | Layout 1 | `06fdea284db2`  |
| 3037   | Layout 1 | `06fdea284db2`  |
| 3030   | Layout 1 | `06fdea284db2`  |
| 3021   | Layout 1 | `06fdea284db2`  |
| 3012   | Layout 1 | `06fdea284db2`  |
| 3002   | Layout 1 | `06fdea284db2`  |
| 2995   | Layout 1 | `06fdea284db2`  |
| 2987   | Layout 1 | `06fdea284db2`  |
| 2978   | Layout 1 | `06fdea284db2`  |
| 2970   | Layout 1 | `06fdea284db2`  |
| 2959   | Layout 1 | `06fdea284db2`  |
| 2951   | Layout 1 | `06fdea284db2`  |
| 2942   | Layout 1 | `06fdea284db2`  |
| 2935   | Layout 1 | `06fdea284db2`  |
| 2932   | Layout 1 | `06fdea284db2`  |
| 2923   | Layout 1 | `06fdea284db2`  |
| 2919   | Layout 1 | `06fdea284db2`  |
| 2907   | Layout 1 | `06fdea284db2`  |
| 2900   | Layout 1 | `06fdea284db2`  |
| 2891   | Layout 1 | `06fdea284db2`  |
| 2882   | Layout 1 | `06fdea284db2`  |
| 2872   | Layout 1 | `06fdea284db2`  |
| 2863   | Layout 1 | `06fdea284db2`  |
| 2855   | Layout 1 | `06fdea284db2`  |
| 2849   | Layout 1 | `06fdea284db2`  |
| 2844   | Layout 1 | `06fdea284db2`  |
| 2834   | Layout 1 | `06fdea284db2`  |
| 2825   | Layout 1 | `06fdea284db2`  |
| 2819   | Layout 1 | `06fdea284db2`  |
| 2811   | Layout 1 | `06fdea284db2`  |
| 2803   | Layout 1 | `06fdea284db2`  |
| 2794   | Layout 1 | `06fdea284db2`  |
| 2783   | Layout 1 | `06fdea284db2`  |
| 2774   | Layout 1 | `06fdea284db2`  |
| 2765   | Layout 1 | `06fdea284db2`  |
| 2756   | Layout 1 | `06fdea284db2`  |
| 2750   | Layout 1 | `06fdea284db2`  |
| 2743   | Layout 1 | `06fdea284db2`  |
| 2736   | Layout 1 | `06fdea284db2`  |
| 2726   | Layout 1 | `06fdea284db2`  |
| 2717   | Layout 1 | `06fdea284db2`  |
| 2709   | Layout 1 | `06fdea284db2`  |
| 2703   | Layout 1 | `06fdea284db2`  |
| 2695   | Layout 1 | `06fdea284db2`  |
| 2684   | Layout 1 | `06fdea284db2`  |
| 2672   | Layout 1 | `06fdea284db2`  |
| 2665   | Layout 1 | `06fdea284db2`  |
| 2657   | Layout 1 | `06fdea284db2`  |
| 2649   | Layout 1 | `06fdea284db2`  |
| 2644   | Layout 1 | `06fdea284db2`  |
| 2637   | Layout 1 | `06fdea284db2`  |
| 2629   | Layout 1 | `06fdea284db2`  |
| 2619   | Layout 1 | `06fdea284db2`  |
| 2612   | Layout 1 | `06fdea284db2`  |
| 2606   | Layout 1 | `06fdea284db2`  |
| 2602   | Layout 1 | `06fdea284db2`  |
| 2601   | Layout 1 | `06fdea284db2`  |
| 2592   | Layout 1 | `06fdea284db2`  |
| 2583   | Layout 1 | `06fdea284db2`  |
| 2575   | Layout 1 | `06fdea284db2`  |
| 2567   | Layout 1 | `06fdea284db2`  |
| 2560   | Layout 1 | `06fdea284db2`  |
| 2553   | Layout 1 | `06fdea284db2`  |
| 2545   | Layout 1 | `06fdea284db2`  |
| 2538   | Layout 1 | `06fdea284db2`  |
| 2529   | Layout 1 | `06fdea284db2`  |
| 2519   | Layout 1 | `06fdea284db2`  |
| 2513   | Layout 1 | `06fdea284db2`  |
| 2510   | Layout 1 | `06fdea284db2`  |
| 2507   | Layout 1 | `06fdea284db2`  |
| 2503   | Layout 1 | `06fdea284db2`  |
| 2498   | Layout 1 | `06fdea284db2`  |
| 2492   | Layout 1 | `06fdea284db2`  |
| 2487   | Layout 1 | `06fdea284db2`  |
| 2480   | Layout 1 | `06fdea284db2`  |
| 2474   | Layout 1 | `06fdea284db2`  |
| 2468   | Layout 1 | `06fdea284db2`  |
| 2460   | Layout 1 | `06fdea284db2`  |
| 2453   | Layout 1 | `06fdea284db2`  |
| 2444   | Layout 1 | `06fdea284db2`  |
| 2438   | Layout 1 | `06fdea284db2`  |
| 2434   | Layout 1 | `06fdea284db2`  |
| 2429   | Layout 1 | `06fdea284db2`  |
| 2421   | Layout 1 | `06fdea284db2`  |
| 2414   | Layout 1 | `06fdea284db2`  |
| 2407   | Layout 1 | `06fdea284db2`  |
| 2401   | Layout 1 | `06fdea284db2`  |
| 2397   | Layout 1 | `06fdea284db2`  |
| 2393   | Layout 1 | `06fdea284db2`  |
| 2384   | Layout 1 | `06fdea284db2`  |
| 2378   | Layout 1 | `06fdea284db2`  |
| 2372   | Layout 1 | `06fdea284db2`  |
| 2358   | Layout 1 | `06fdea284db2`  |
| 2352   | Layout 1 | `06fdea284db2`  |
| 2347   | Layout 1 | `06fdea284db2`  |
| 2343   | Layout 1 | `06fdea284db2`  |
| 2335   | Layout 1 | `06fdea284db2`  |
| 2327   | Layout 1 | `06fdea284db2`  |
| 2324   | Layout 1 | `06fdea284db2`  |
| 2319   | Layout 1 | `06fdea284db2`  |
| 2313   | Layout 1 | `06fdea284db2`  |
| 2308   | Layout 1 | `06fdea284db2`  |
| 2302   | Layout 1 | `06fdea284db2`  |
| 2295   | Layout 1 | `06fdea284db2`  |
| 2290   | Layout 1 | `06fdea284db2`  |
| 2284   | Layout 1 | `06fdea284db2`  |
| 2276   | Layout 1 | `06fdea284db2`  |
| 2269   | Layout 1 | `06fdea284db2`  |
| 2259   | Layout 1 | `06fdea284db2`  |
| 2250   | Layout 1 | `06fdea284db2`  |
| 2243   | Layout 1 | `06fdea284db2`  |
| 2235   | Layout 1 | `06fdea284db2`  |
| 2229   | Layout 1 | `06fdea284db2`  |
| 2224   | Layout 1 | `06fdea284db2`  |
| 2218   | Layout 1 | `06fdea284db2`  |
| 2215   | Layout 1 | `06fdea284db2`  |
| 2207   | Layout 1 | `06fdea284db2`  |
| 2203   | Layout 1 | `06fdea284db2`  |
| 2196   | Layout 1 | `06fdea284db2`  |
| 2192   | Layout 1 | `06fdea284db2`  |
| 2189   | Layout 1 | `06fdea284db2`  |
| 2183   | Layout 1 | `06fdea284db2`  |
| 2179   | Layout 1 | `06fdea284db2`  |
| 2171   | Layout 1 | `06fdea284db2`  |
| 2163   | Layout 1 | `06fdea284db2`  |
| 2156   | Layout 1 | `06fdea284db2`  |
| 2151   | Layout 1 | `06fdea284db2`  |
| 2147   | Layout 1 | `06fdea284db2`  |
| 2142   | Layout 1 | `06fdea284db2`  |
| 2138   | Layout 1 | `06fdea284db2`  |
| 2134   | Layout 1 | `06fdea284db2`  |
| 2130   | Layout 1 | `06fdea284db2`  |
| 2122   | Layout 1 | `06fdea284db2`  |
| 2107   | Layout 1 | `06fdea284db2`  |
| 2098   | Layout 1 | `06fdea284db2`  |
| 2089   | Layout 1 | `06fdea284db2`  |
| 2081   | Layout 1 | `06fdea284db2`  |
| 2073   | Layout 1 | `06fdea284db2`  |
| 2067   | Layout 1 | `06fdea284db2`  |
| 2063   | Layout 1 | `06fdea284db2`  |
| 2059   | Layout 1 | `06fdea284db2`  |
| 2052   | Layout 1 | `06fdea284db2`  |
| 2044   | Layout 1 | `06fdea284db2`  |
| 2039   | Layout 1 | `06fdea284db2`  |
| 2032   | Layout 1 | `06fdea284db2`  |
| 2025   | Layout 1 | `06fdea284db2`  |
| 2011   | Layout 1 | `06fdea284db2`  |
| 2005   | Layout 1 | `06fdea284db2`  |
| 2000   | Layout 1 | `06fdea284db2`  |
| 1996   | Layout 1 | `06fdea284db2`  |
| 1991   | Layout 1 | `06fdea284db2`  |
| 1985   | Layout 1 | `06fdea284db2`  |
| 1980   | Layout 1 | `06fdea284db2`  |
| 1969   | Layout 1 | `06fdea284db2`  |
| 1964   | Layout 1 | `06fdea284db2`  |
| 1958   | Layout 1 | `06fdea284db2`  |
| 1950   | Layout 1 | `06fdea284db2`  |
| 1945   | Layout 1 | `06fdea284db2`  |
| 1937   | Layout 1 | `06fdea284db2`  |
| 1933   | Layout 1 | `06fdea284db2`  |
| 1927   | Layout 1 | `06fdea284db2`  |
| 1921   | Layout 1 | `06fdea284db2`  |
| 1914   | Layout 1 | `06fdea284db2`  |
| 1908   | Layout 1 | `06fdea284db2`  |
| 1897   | Layout 1 | `06fdea284db2`  |
| 1892   | Layout 1 | `06fdea284db2`  |
| 1886   | Layout 1 | `06fdea284db2`  |
| 1881   | Layout 1 | `06fdea284db2`  |
| 1871   | Layout 1 | `06fdea284db2`  |
| 1866   | Layout 1 | `06fdea284db2`  |
| 1862   | Layout 1 | `06fdea284db2`  |
| 1854   | Layout 1 | `06fdea284db2`  |
| 1846   | Layout 1 | `06fdea284db2`  |
| 1838   | Layout 1 | `06fdea284db2`  |
| 1832   | Layout 1 | `06fdea284db2`  |
| 1826   | Layout 1 | `06fdea284db2`  |
| 1822   | Layout 1 | `06fdea284db2`  |
| 1818   | Layout 1 | `06fdea284db2`  |
| 1804   | Layout 1 | `06fdea284db2`  |
| 1794   | Layout 1 | `06fdea284db2`  |
| 1790   | Layout 1 | `06fdea284db2`  |
| 1784   | Layout 1 | `06fdea284db2`  |
| 1774   | Layout 1 | `06fdea284db2`  |
| 1771   | Layout 1 | `06fdea284db2`  |
| 1762   | Layout 1 | `06fdea284db2`  |
| 1759   | Layout 1 | `06fdea284db2`  |
| 1754   | Layout 1 | `06fdea284db2`  |
| 1749   | Layout 1 | `06fdea284db2`  |
| 1743   | Layout 1 | `06fdea284db2`  |
| 1737   | Layout 1 | `06fdea284db2`  |
| 1731   | Layout 1 | `06fdea284db2`  |
| 1725   | Layout 1 | `06fdea284db2`  |
| 1717   | Layout 1 | `06fdea284db2`  |
| 1710   | Layout 1 | `06fdea284db2`  |
| 1704   | Layout 1 | `06fdea284db2`  |
| 1698   | Layout 1 | `06fdea284db2`  |
| 1690   | Layout 1 | `06fdea284db2`  |
| 1685   | Layout 1 | `06fdea284db2`  |
| 1680   | Layout 1 | `06fdea284db2`  |
| 1674   | Layout 1 | `06fdea284db2`  |
| 1668   | Layout 1 | `06fdea284db2`  |
| 1659   | Layout 1 | `06fdea284db2`  |
| 1649   | Layout 1 | `06fdea284db2`  |
| 1642   | Layout 1 | `06fdea284db2`  |
| 1636   | Layout 1 | `06fdea284db2`  |
| 1628   | Layout 1 | `06fdea284db2`  |
| 1622   | Layout 1 | `06fdea284db2`  |
| 1614   | Layout 1 | `06fdea284db2`  |
| 1608   | No file  | `06fdea284db2`  |
| 1602   | No file  | `06fdea284db2`  |
| 1598   | No file  | `06fdea284db2`  |
| 1594   | No file  | `06fdea284db2`  |
| 1590   | No file  | `06fdea284db2`  |
| 1587   | No file  | `06fdea284db2`  |
| 1584   | No file  | `06fdea284db2`  |
| 1579   | No file  | `06fdea284db2`  |
| 1572   | No file  | `06fdea284db2`  |
| 1565   | No file  | `06fdea284db2`  |
| 1559   | No file  | `06fdea284db2`  |
| 1554   | No file  | `06fdea284db2`  |
| 1547   | No file  | `06fdea284db2`  |
| 1537   | No file  | `06fdea284db2`  |
| 1529   | No file  | `06fdea284db2`  |
| 1524   | No file  | `06fdea284db2`  |
| 1519   | No file  | `06fdea284db2`  |
| 1509   | No file  | `06fdea284db2`  |
| 1506   | No file  | `06fdea284db2`  |
| 1504   | No file  | `06fdea284db2`  |
| 1500   | No file  | `06fdea284db2`  |
| 1493   | No file  | `06fdea284db2`  |
| 1489   | No file  | `06fdea284db2`  |
| 1485   | No file  | `06fdea284db2`  |
| 1481   | No file  | `06fdea284db2`  |
| 1474   | No file  | `06fdea284db2`  |
| 1466   | No file  | `06fdea284db2`  |
| 1462   | No file  | `06fdea284db2`  |
| 1459   | No file  | `06fdea284db2`  |
| 1453   | No file  | `06fdea284db2`  |
| 1450   | No file  | `06fdea284db2`  |
| 1445   | No file  | `06fdea284db2`  |
| 1439   | No file  | `06fdea284db2`  |
| 1433   | No file  | `06fdea284db2`  |
| 1430   | No file  | `06fdea284db2`  |
| 1426   | No file  | `06fdea284db2`  |
| 1421   | No file  | `06fdea284db2`  |
| 1417   | No file  | `06fdea284db2`  |
| 1416   | No file  | `06fdea284db2`  |
| 1409   | No file  | `06fdea284db2`  |
| 1405   | No file  | `06fdea284db2`  |
| 1401   | No file  | `06fdea284db2`  |
| 1396   | No file  | `06fdea284db2`  |
| 1391   | No file  | `06fdea284db2`  |
| 1390   | No file  | `06fdea284db2`  |
| 1386   | No file  | `06fdea284db2`  |
| 1381   | No file  | `06fdea284db2`  |
| 1379   | No file  | `06fdea284db2`  |
| 1372   | No file  | `06fdea284db2`  |
| 1366   | No file  | `06fdea284db2`  |
| 1364   | No file  | `06fdea284db2`  |
| 1363   | No file  | `06fdea284db2`  |
| 1360   | No file  | `06fdea284db2`  |
| 1358   | No file  | `06fdea284db2`  |
| 1355   | No file  | `06fdea284db2`  |
| 1351   | No file  | `06fdea284db2`  |
| 1348   | No file  | `06fdea284db2`  |
| 1346   | No file  | `06fdea284db2`  |
| 1341   | No file  | `06fdea284db2`  |
| 1340   | No file  | `06fdea284db2`  |
| 1338   | No file  | `06fdea284db2`  |
| 1335   | No file  | `06fdea284db2`  |
| 1333   | No file  | `06fdea284db2`  |
| 1329   | No file  | `06fdea284db2`  |
| 1327   | No file  | `06fdea284db2`  |
| 1324   | No file  | `06fdea284db2`  |
| 1321   | No file  | `06fdea284db2`  |
| 1319   | No file  | `06fdea284db2`  |
| 1318   | No file  | `06fdea284db2`  |
| 1316   | No file  | `06fdea284db2`  |
| 1313   | No file  | `06fdea284db2`  |
| 1311   | No file  | `06fdea284db2`  |
| 1309   | No file  | `06fdea284db2`  |
| 1304   | No file  | `06fdea284db2`  |
| 1292   | No file  | `06fdea284db2`  |
| 1286   | No file  | `06fdea284db2`  |
| 1280   | No file  | `06fdea284db2`  |
| 1276   | No file  | `06fdea284db2`  |
| 1267   | No file  | `06fdea284db2`  |
| 1261   | No file  | `06fdea284db2`  |
| 1256   | No file  | `06fdea284db2`  |
| 1250   | No file  | `06fdea284db2`  |
| 1246   | No file  | `06fdea284db2`  |
| 1239   | No file  | `06fdea284db2`  |
| 1230   | No file  | `06fdea284db2`  |
| 1226   | No file  | `06fdea284db2`  |
| 1220   | No file  | `06fdea284db2`  |
| 1217   | No file  | `06fdea284db2`  |
| 1211   | No file  | `06fdea284db2`  |
| 1210   | No file  | `06fdea284db2`  |
| 1208   | No file  | `06fdea284db2`  |
| 1203   | No file  | `06fdea284db2`  |
| 1197   | No file  | `06fdea284db2`  |
| 1194   | No file  | `06fdea284db2`  |
| 1192   | No file  | `06fdea284db2`  |
| 1187   | No file  | `06fdea284db2`  |
| 1183   | No file  | `06fdea284db2`  |
| 1177   | No file  | `06fdea284db2`  |
| 1173   | No file  | `06fdea284db2`  |
| 1167   | No file  | `06fdea284db2`  |
| 1164   | No file  | `06fdea284db2`  |
| 1156   | No file  | `06fdea284db2`  |
| 1149   | No file  | `06fdea284db2`  |
| 1144   | No file  | `06fdea284db2`  |
| 1137   | No file  | `06fdea284db2`  |
| 1132   | No file  | `06fdea284db2`  |
| 1127   | No file  | `06fdea284db2`  |
| 1122   | No file  | `06fdea284db2`  |
| 1118   | No file  | `06fdea284db2`  |
| 1114   | No file  | `06fdea284db2`  |
| 1109   | No file  | `06fdea284db2`  |
| 1102   | No file  | `06fdea284db2`  |
| 1096   | No file  | `06fdea284db2`  |
| 1088   | No file  | `06fdea284db2`  |
| 1081   | No file  | `06fdea284db2`  |
| 1076   | No file  | `06fdea284db2`  |
| 1069   | No file  | `06fdea284db2`  |
| 1064   | No file  | `06fdea284db2`  |
| 1058   | No file  | `06fdea284db2`  |
| 1051   | No file  | `06fdea284db2`  |
| 1044   | No file  | `06fdea284db2`  |
| 1036   | No file  | `06fdea284db2`  |
| 1026   | No file  | `06fdea284db2`  |
| 1016   | No file  | `06fdea284db2`  |
| 1009   | No file  | `06fdea284db2`  |
| 1005   | No file  | `06fdea284db2`  |
| 1000   | No file  | `06fdea284db2`  |
| 998    | No file  | `06fdea284db2`  |
| 990    | No file  | `06fdea284db2`  |
| 979    | No file  | `06fdea284db2`  |
| 972    | No file  | `06fdea284db2`  |
| 963    | No file  | `06fdea284db2`  |
| 955    | No file  | `06fdea284db2`  |
| 946    | No file  | `06fdea284db2`  |
| 938    | No file  | `06fdea284db2`  |
| 927    | No file  | `06fdea284db2`  |
| 911    | No file  | `06fdea284db2`  |
| 904    | No file  | `06fdea284db2`  |
| 899    | No file  | `06fdea284db2`  |
| 894    | No file  | `06fdea284db2`  |
| 885    | No file  | `06fdea284db2`  |
| 879    | No file  | `06fdea284db2`  |
| 872    | No file  | `06fdea284db2`  |
| 864    | No file  | `06fdea284db2`  |
| 855    | No file  | `06fdea284db2`  |
| 853    | No file  | `06fdea284db2`  |
| 845    | No file  | `06fdea284db2`  |
| 837    | No file  | `06fdea284db2`  |
| 829    | No file  | `06fdea284db2`  |
| 822    | No file  | `06fdea284db2`  |
| 814    | No file  | `06fdea284db2`  |
| 805    | No file  | `06fdea284db2`  |
| 794    | No file  | `06fdea284db2`  |
| 787    | No file  | `06fdea284db2`  |
| 780    | No file  | `06fdea284db2`  |
| 771    | No file  | `06fdea284db2`  |
| 760    | No file  | `06fdea284db2`  |
| 748    | No file  | `06fdea284db2`  |
| 741    | No file  | `06fdea284db2`  |
| 736    | No file  | `06fdea284db2`  |
| 731    | No file  | `06fdea284db2`  |
| 723    | No file  | `06fdea284db2`  |
| 711    | No file  | `06fdea284db2`  |
| 707    | No file  | `06fdea284db2`  |
| 697    | No file  | `06fdea284db2`  |
| 689    | No file  | `06fdea284db2`  |
| 683    | No file  | `06fdea284db2`  |
| 678    | No file  | `06fdea284db2`  |
| 670    | No file  | `06fdea284db2`  |
| 661    | No file  | `06fdea284db2`  |
| 656    | No file  | `06fdea284db2`  |
| 652    | No file  | `06fdea284db2`  |
| 643    | No file  | `06fdea284db2`  |
| 637    | No file  | `06fdea284db2`  |
| 630    | No file  | `06fdea284db2`  |
| 627    | No file  | `06fdea284db2`  |
| 621    | No file  | `06fdea284db2`  |
| 617    | No file  | `06fdea284db2`  |
| 615    | No file  | `06fdea284db2`  |
| 606    | No file  | `06fdea284db2`  |
| 599    | No file  | `06fdea284db2`  |
| 592    | No file  | `06fdea284db2`  |
| 586    | No file  | `06fdea284db2`  |
| 577    | No file  | `06fdea284db2`  |
| 569    | No file  | `06fdea284db2`  |
| 561    | No file  | `06fdea284db2`  |
| 554    | No file  | `06fdea284db2`  |
| 542    | No file  | `06fdea284db2`  |
| 532    | No file  | `06fdea284db2`  |
| 531    | No file  | `06fdea284db2`  |
| 526    | No file  | `06fdea284db2`  |
| 521    | No file  | `06fdea284db2`  |
| 517    | No file  | `06fdea284db2`  |
| 510    | No file  | `06fdea284db2`  |
| 508    | No file  | `06fdea284db2`  |
| 504    | No file  | `06fdea284db2`  |
| 497    | No file  | `06fdea284db2`  |
| 491    | No file  | `06fdea284db2`  |
| 485    | No file  | `06fdea284db2`  |
| 478    | No file  | `06fdea284db2`  |
| 472    | No file  | `06fdea284db2`  |
| 466    | No file  | `06fdea284db2`  |
| 457    | No file  | `06fdea284db2`  |
| 452    | No file  | `06fdea284db2`  |
| 449    | No file  | `06fdea284db2`  |
| 435    | No file  | `06fdea284db2`  |

<!-- versions:end -->

## Companion Files

None. The handler names each filter with LOC type 101 from
`languagedata_*.loc` when it is loaded, else with its Korean name.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of filters                             |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (9 bytes)

| Offset  | Type | Field                         | Notes                                                                 |
| ------- | ---- | ----------------------------- | --------------------------------------------------------------------- |
| `+0x00` | u8   | index                         | The filter key `ToClient_getItemMoveKeyByIndex(index):get()` returns; unique per file |
| `+0x01` | u16  | contents_event_type           | `CppEnums.ContentsEventType` of the items the filter leaves out       |
| `+0x03` | u8   | item_classify                 | `CppEnums.ItemClassifyType` of those items                            |
| `+0x04` | u8   | item_type                     | `CppEnums.ItemType` of those items                                    |
| `+0x05` | u32  | exception_filter_name_tag_ref | String table index of the filter's Korean name                        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                   |
| ------- | ------------------ | ------------ | ------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                       |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE filter names, one per row, in row order        |

## Filters

The 4 rows of client 3483, in file order. The enum names are from the client
3482 `global_define_cpp_enum.luac`.

| `index` | `item_type`       | `item_classify` | `contents_event_type`  | Korean name               | LOC type 101                  |
| ------- | ----------------- | --------------- | ---------------------- | ------------------------- | ----------------------------- |
| 2       | `10` ContentsEvent | `8` Cook       | `17` NpcWorkerRecovery | `일꾼 행동력 회복류 제외` | Exclude Worker Recovery Items |
| 3       | `10` ContentsEvent | `11` Vehicle   | `13` PetFeed           | `반려동물 먹이류 제외`    | Exclude Pet Feed              |
| 0       | `2` Skill          | `8` Cook       | `45` Banquet           | `요리류 제외`             | Exclude Food                  |
| 1       | `2` Skill          | `7` Potion     | `171`                  | `회복제/비약류 제외`      | Exclude Potions/Elixirs       |

`171` is the `contents_event_type` that `itemenchant.dbss` stores on items
whose use does nothing (see [itemenchant](../dbss/itemenchant_dbss.md)); client
1784 stores `125` in that row.

## Filter Names

LOC type 101 names a filter by `str_id1 = item_type << 24 | item_classify
<< 16 | contents_event_type`, which is the u32 at row `+0x01` read
little-endian. All 4 rows of client 3483 have a LOC type 101 name that way
(`0x0A0B000D`, 168493069, is `Exclude Pet Feed`). LOC type 101 also holds
`Exclude Potions/Elixirs` under the 7 keys of `item_type` 2 and
`item_classify` 7 with `contents_event_type` 166 to 172.

## Field Names

The names follow the `Auto_Warehouse_Order_Filter` sheet of a private
server's `DataSheets.bexcel` on client 1784, also in that server's
`datasheet_itemdatatable_contribution.xlsm`: columns `Index`,
`ExceptionFilterNameTag`, `ItemType`, `ItemClassify` and
`ContentsEventType`, 4 rows. All 4 rows of the client 1784 file match a
sheet row on `Index`, `ExceptionFilterNameTag` (the Korean name),
`ItemType` and `ItemClassify` (4 of 4), and 3 of 4 on
`ContentsEventType`: the sheet leaves row `1` empty (`<null>`), where the
client 1784 file stores `125`. The file stores the sheet's columns after
`Index` in reverse order.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/item_tables.py`: the
  index, the filter name (LOC type 101, else Korean) and the three enum
  values with their member names.
