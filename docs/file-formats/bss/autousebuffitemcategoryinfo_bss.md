# `autousebuffitemcategoryinfo.bss` Format

## Purpose

The categories of the buff item auto-use (a Fairy skill): one 8-byte row
per category key with its Korean name. The items of each category are the
rows of [`buffitemautousestaticstatus.bss`](buffitemautousestaticstatus_bss.md).
The auto-use window (`panel_window_autousebuffitem_1.luac`, client 3482)
walks `ToClient_getAutoUseBuffItemCategoryCount()` and
`ToClient_getAutoUseBuffItemCategoryKey(index)`, and titles each group with
`ToClient_getAutoUseBuffItemCategoryStaticStatusWrapper(categoryKey):getCategoryName()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                              | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------------------- | ----- | ------- | --------- |
| 1      | 1969 and later | `autousebuffitemcategoryinfo.bss` | 239   | 9 Row   | 8         |

| Layout | File                              | Known          | Unknown    |
| ------ | --------------------------------- | -------------- | ---------- |
| 1      | `autousebuffitemcategoryinfo.bss` | 239 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `2e093ceb79ad`  |
| 3482   | Layout 1 | `2e093ceb79ad`  |
| 3474   | Layout 1 | `2e093ceb79ad`  |
| 3473   | Layout 1 | `2e093ceb79ad`  |
| 3464   | Layout 1 | `2e093ceb79ad`  |
| 3458   | Layout 1 | `2e093ceb79ad`  |
| 3454   | Layout 1 | `2e093ceb79ad`  |
| 3444   | Layout 1 | `2e093ceb79ad`  |
| 3435   | Layout 1 | `2e093ceb79ad`  |
| 3426   | Layout 1 | `2e093ceb79ad`  |
| 3418   | Layout 1 | `2e093ceb79ad`  |
| 3412   | Layout 1 | `2e093ceb79ad`  |
| 3402   | Layout 1 | `2e093ceb79ad`  |
| 3396   | Layout 1 | `2e093ceb79ad`  |
| 3387   | Layout 1 | `2e093ceb79ad`  |
| 3381   | Layout 1 | `2e093ceb79ad`  |
| 3373   | Layout 1 | `2e093ceb79ad`  |
| 3364   | Layout 1 | `2e093ceb79ad`  |
| 3356   | Layout 1 | `2e093ceb79ad`  |
| 3349   | Layout 1 | `2e093ceb79ad`  |
| 3342   | Layout 1 | `2e093ceb79ad`  |
| 3335   | Layout 1 | `2e093ceb79ad`  |
| 3326   | Layout 1 | `2e093ceb79ad`  |
| 3321   | Layout 1 | `2e093ceb79ad`  |
| 3314   | Layout 1 | `2e093ceb79ad`  |
| 3303   | Layout 1 | `2e093ceb79ad`  |
| 3302   | Layout 1 | `2e093ceb79ad`  |
| 3293   | Layout 1 | `2e093ceb79ad`  |
| 3283   | Layout 1 | `2e093ceb79ad`  |
| 3275   | Layout 1 | `2e093ceb79ad`  |
| 3267   | Layout 1 | `2e093ceb79ad`  |
| 3258   | Layout 1 | `2e093ceb79ad`  |
| 3251   | Layout 1 | `2e093ceb79ad`  |
| 3242   | Layout 1 | `2e093ceb79ad`  |
| 3235   | Layout 1 | `2e093ceb79ad`  |
| 3229   | Layout 1 | `2e093ceb79ad`  |
| 3212   | Layout 1 | `2e093ceb79ad`  |
| 3203   | Layout 1 | `2e093ceb79ad`  |
| 3193   | Layout 1 | `2e093ceb79ad`  |
| 3186   | Layout 1 | `2e093ceb79ad`  |
| 3177   | Layout 1 | `2e093ceb79ad`  |
| 3169   | Layout 1 | `2e093ceb79ad`  |
| 3158   | Layout 1 | `2e093ceb79ad`  |
| 3151   | Layout 1 | `2e093ceb79ad`  |
| 3144   | Layout 1 | `2e093ceb79ad`  |
| 3133   | Layout 1 | `2e093ceb79ad`  |
| 3125   | Layout 1 | `2e093ceb79ad`  |
| 3118   | Layout 1 | `2e093ceb79ad`  |
| 3111   | Layout 1 | `2e093ceb79ad`  |
| 3103   | Layout 1 | `2e093ceb79ad`  |
| 3095   | Layout 1 | `2e093ceb79ad`  |
| 3086   | Layout 1 | `2e093ceb79ad`  |
| 3072   | Layout 1 | `2e093ceb79ad`  |
| 3062   | Layout 1 | `2e093ceb79ad`  |
| 3052   | Layout 1 | `2e093ceb79ad`  |
| 3045   | Layout 1 | `2e093ceb79ad`  |
| 3037   | Layout 1 | `2e093ceb79ad`  |
| 3030   | Layout 1 | `2e093ceb79ad`  |
| 3021   | Layout 1 | `2e093ceb79ad`  |
| 3012   | Layout 1 | `2e093ceb79ad`  |
| 3002   | Layout 1 | `2e093ceb79ad`  |
| 2995   | Layout 1 | `2e093ceb79ad`  |
| 2987   | Layout 1 | `2e093ceb79ad`  |
| 2978   | Layout 1 | `2e093ceb79ad`  |
| 2970   | Layout 1 | `2e093ceb79ad`  |
| 2959   | Layout 1 | `2e093ceb79ad`  |
| 2951   | Layout 1 | `2e093ceb79ad`  |
| 2942   | Layout 1 | `2e093ceb79ad`  |
| 2935   | Layout 1 | `2e093ceb79ad`  |
| 2932   | Layout 1 | `2e093ceb79ad`  |
| 2923   | Layout 1 | `2e093ceb79ad`  |
| 2919   | Layout 1 | `2e093ceb79ad`  |
| 2907   | Layout 1 | `2e093ceb79ad`  |
| 2900   | Layout 1 | `2e093ceb79ad`  |
| 2891   | Layout 1 | `2e093ceb79ad`  |
| 2882   | Layout 1 | `2e093ceb79ad`  |
| 2872   | Layout 1 | `2e093ceb79ad`  |
| 2863   | Layout 1 | `2e093ceb79ad`  |
| 2855   | Layout 1 | `2e093ceb79ad`  |
| 2849   | Layout 1 | `2e093ceb79ad`  |
| 2844   | Layout 1 | `2e093ceb79ad`  |
| 2834   | Layout 1 | `2e093ceb79ad`  |
| 2825   | Layout 1 | `2e093ceb79ad`  |
| 2819   | Layout 1 | `2e093ceb79ad`  |
| 2811   | Layout 1 | `2e093ceb79ad`  |
| 2803   | Layout 1 | `2e093ceb79ad`  |
| 2794   | Layout 1 | `2e093ceb79ad`  |
| 2783   | Layout 1 | `2e093ceb79ad`  |
| 2774   | Layout 1 | `2e093ceb79ad`  |
| 2765   | Layout 1 | `2e093ceb79ad`  |
| 2756   | Layout 1 | `2e093ceb79ad`  |
| 2750   | Layout 1 | `2e093ceb79ad`  |
| 2743   | Layout 1 | `2e093ceb79ad`  |
| 2736   | Layout 1 | `2e093ceb79ad`  |
| 2726   | Layout 1 | `2e093ceb79ad`  |
| 2717   | Layout 1 | `2e093ceb79ad`  |
| 2709   | Layout 1 | `2e093ceb79ad`  |
| 2703   | Layout 1 | `2e093ceb79ad`  |
| 2695   | Layout 1 | `2e093ceb79ad`  |
| 2684   | Layout 1 | `2e093ceb79ad`  |
| 2672   | Layout 1 | `2e093ceb79ad`  |
| 2665   | Layout 1 | `2e093ceb79ad`  |
| 2657   | Layout 1 | `2e093ceb79ad`  |
| 2649   | Layout 1 | `2e093ceb79ad`  |
| 2644   | Layout 1 | `2e093ceb79ad`  |
| 2637   | Layout 1 | `2e093ceb79ad`  |
| 2629   | Layout 1 | `2e093ceb79ad`  |
| 2619   | Layout 1 | `2e093ceb79ad`  |
| 2612   | Layout 1 | `2e093ceb79ad`  |
| 2606   | Layout 1 | `2e093ceb79ad`  |
| 2602   | Layout 1 | `2e093ceb79ad`  |
| 2601   | Layout 1 | `2e093ceb79ad`  |
| 2592   | Layout 1 | `2e093ceb79ad`  |
| 2583   | Layout 1 | `2e093ceb79ad`  |
| 2575   | Layout 1 | `2e093ceb79ad`  |
| 2567   | Layout 1 | `2e093ceb79ad`  |
| 2560   | Layout 1 | `2e093ceb79ad`  |
| 2553   | Layout 1 | `2e093ceb79ad`  |
| 2545   | Layout 1 | `2e093ceb79ad`  |
| 2538   | Layout 1 | `2e093ceb79ad`  |
| 2529   | Layout 1 | `2e093ceb79ad`  |
| 2519   | Layout 1 | `2e093ceb79ad`  |
| 2513   | Layout 1 | `2e093ceb79ad`  |
| 2510   | Layout 1 | `2e093ceb79ad`  |
| 2507   | Layout 1 | `2e093ceb79ad`  |
| 2503   | Layout 1 | `2e093ceb79ad`  |
| 2498   | Layout 1 | `2e093ceb79ad`  |
| 2492   | Layout 1 | `2e093ceb79ad`  |
| 2487   | Layout 1 | `2e093ceb79ad`  |
| 2480   | Layout 1 | `2e093ceb79ad`  |
| 2474   | Layout 1 | `2e093ceb79ad`  |
| 2468   | Layout 1 | `2e093ceb79ad`  |
| 2460   | Layout 1 | `2e093ceb79ad`  |
| 2453   | Layout 1 | `2e093ceb79ad`  |
| 2444   | Layout 1 | `2e093ceb79ad`  |
| 2438   | Layout 1 | `2e093ceb79ad`  |
| 2434   | Layout 1 | `2e093ceb79ad`  |
| 2429   | Layout 1 | `2e093ceb79ad`  |
| 2421   | Layout 1 | `2e093ceb79ad`  |
| 2414   | Layout 1 | `2e093ceb79ad`  |
| 2407   | Layout 1 | `2e093ceb79ad`  |
| 2401   | Layout 1 | `2e093ceb79ad`  |
| 2397   | Layout 1 | `2e093ceb79ad`  |
| 2393   | Layout 1 | `2e093ceb79ad`  |
| 2384   | Layout 1 | `2e093ceb79ad`  |
| 2378   | Layout 1 | `2e093ceb79ad`  |
| 2372   | Layout 1 | `2e093ceb79ad`  |
| 2358   | Layout 1 | `2e093ceb79ad`  |
| 2352   | Layout 1 | `2e093ceb79ad`  |
| 2347   | Layout 1 | `2e093ceb79ad`  |
| 2343   | Layout 1 | `2e093ceb79ad`  |
| 2335   | Layout 1 | `2e093ceb79ad`  |
| 2327   | Layout 1 | `2e093ceb79ad`  |
| 2324   | Layout 1 | `2e093ceb79ad`  |
| 2319   | Layout 1 | `2e093ceb79ad`  |
| 2313   | Layout 1 | `2e093ceb79ad`  |
| 2308   | Layout 1 | `2e093ceb79ad`  |
| 2302   | Layout 1 | `2e093ceb79ad`  |
| 2295   | Layout 1 | `2e093ceb79ad`  |
| 2290   | Layout 1 | `2e093ceb79ad`  |
| 2284   | Layout 1 | `2e093ceb79ad`  |
| 2276   | Layout 1 | `2e093ceb79ad`  |
| 2269   | Layout 1 | `2e093ceb79ad`  |
| 2259   | Layout 1 | `2e093ceb79ad`  |
| 2250   | Layout 1 | `2e093ceb79ad`  |
| 2243   | Layout 1 | `2e093ceb79ad`  |
| 2235   | Layout 1 | `2e093ceb79ad`  |
| 2229   | Layout 1 | `2e093ceb79ad`  |
| 2224   | Layout 1 | `2e093ceb79ad`  |
| 2218   | Layout 1 | `2e093ceb79ad`  |
| 2215   | Layout 1 | `2e093ceb79ad`  |
| 2207   | Layout 1 | `2e093ceb79ad`  |
| 2203   | Layout 1 | `2e093ceb79ad`  |
| 2196   | Layout 1 | `2e093ceb79ad`  |
| 2192   | Layout 1 | `2e093ceb79ad`  |
| 2189   | Layout 1 | `2e093ceb79ad`  |
| 2183   | Layout 1 | `2e093ceb79ad`  |
| 2179   | Layout 1 | `2e093ceb79ad`  |
| 2171   | Layout 1 | `2e093ceb79ad`  |
| 2163   | Layout 1 | `2e093ceb79ad`  |
| 2156   | Layout 1 | `2e093ceb79ad`  |
| 2151   | Layout 1 | `2e093ceb79ad`  |
| 2147   | Layout 1 | `2e093ceb79ad`  |
| 2142   | Layout 1 | `2e093ceb79ad`  |
| 2138   | Layout 1 | `2e093ceb79ad`  |
| 2134   | Layout 1 | `2e093ceb79ad`  |
| 2130   | Layout 1 | `2e093ceb79ad`  |
| 2122   | Layout 1 | `2e093ceb79ad`  |
| 2107   | Layout 1 | `2e093ceb79ad`  |
| 2098   | Layout 1 | `2e093ceb79ad`  |
| 2089   | Layout 1 | `2e093ceb79ad`  |
| 2081   | Layout 1 | `2e093ceb79ad`  |
| 2073   | Layout 1 | `2e093ceb79ad`  |
| 2067   | Layout 1 | `2e093ceb79ad`  |
| 2063   | Layout 1 | `2e093ceb79ad`  |
| 2059   | Layout 1 | `2e093ceb79ad`  |
| 2052   | Layout 1 | `2e093ceb79ad`  |
| 2044   | Layout 1 | `2e093ceb79ad`  |
| 2039   | Layout 1 | `2e093ceb79ad`  |
| 2032   | Layout 1 | `2e093ceb79ad`  |
| 2025   | Layout 1 | `2e093ceb79ad`  |
| 2011   | Layout 1 | `2e093ceb79ad`  |
| 2005   | Layout 1 | `2e093ceb79ad`  |
| 2000   | Layout 1 | `2e093ceb79ad`  |
| 1996   | Layout 1 | `2e093ceb79ad`  |
| 1991   | Layout 1 | `2e093ceb79ad`  |
| 1985   | Layout 1 | `2e093ceb79ad`  |
| 1980   | Layout 1 | `2e093ceb79ad`  |
| 1969   | Layout 1 | `2e093ceb79ad`  |
| 1964   | No file  | `2e093ceb79ad`  |
| 1958   | No file  | `2e093ceb79ad`  |
| 1950   | No file  | `2e093ceb79ad`  |
| 1945   | No file  | `2e093ceb79ad`  |
| 1937   | No file  | `2e093ceb79ad`  |
| 1933   | No file  | `2e093ceb79ad`  |
| 1927   | No file  | `2e093ceb79ad`  |
| 1921   | No file  | `2e093ceb79ad`  |
| 1914   | No file  | `2e093ceb79ad`  |
| 1908   | No file  | `2e093ceb79ad`  |
| 1897   | No file  | `2e093ceb79ad`  |
| 1892   | No file  | `2e093ceb79ad`  |
| 1886   | No file  | `2e093ceb79ad`  |
| 1881   | No file  | `2e093ceb79ad`  |
| 1871   | No file  | `2e093ceb79ad`  |
| 1866   | No file  | `2e093ceb79ad`  |
| 1862   | No file  | `2e093ceb79ad`  |
| 1854   | No file  | `2e093ceb79ad`  |
| 1846   | No file  | `2e093ceb79ad`  |
| 1838   | No file  | `2e093ceb79ad`  |
| 1832   | No file  | `2e093ceb79ad`  |
| 1826   | No file  | `2e093ceb79ad`  |
| 1822   | No file  | `2e093ceb79ad`  |
| 1818   | No file  | `2e093ceb79ad`  |
| 1804   | No file  | `2e093ceb79ad`  |
| 1794   | No file  | `2e093ceb79ad`  |
| 1790   | No file  | `2e093ceb79ad`  |
| 1784   | No file  | `2e093ceb79ad`  |
| 1774   | No file  | `2e093ceb79ad`  |
| 1771   | No file  | `2e093ceb79ad`  |
| 1762   | No file  | `2e093ceb79ad`  |
| 1759   | No file  | `2e093ceb79ad`  |
| 1754   | No file  | `2e093ceb79ad`  |
| 1749   | No file  | `2e093ceb79ad`  |
| 1743   | No file  | `2e093ceb79ad`  |
| 1737   | No file  | `2e093ceb79ad`  |
| 1731   | No file  | `2e093ceb79ad`  |
| 1725   | No file  | `2e093ceb79ad`  |
| 1717   | No file  | `2e093ceb79ad`  |
| 1710   | No file  | `2e093ceb79ad`  |
| 1704   | No file  | `2e093ceb79ad`  |
| 1698   | No file  | `2e093ceb79ad`  |
| 1690   | No file  | `2e093ceb79ad`  |
| 1685   | No file  | `2e093ceb79ad`  |
| 1680   | No file  | `2e093ceb79ad`  |
| 1674   | No file  | `2e093ceb79ad`  |
| 1668   | No file  | `2e093ceb79ad`  |
| 1659   | No file  | `2e093ceb79ad`  |
| 1649   | No file  | `2e093ceb79ad`  |
| 1642   | No file  | `2e093ceb79ad`  |
| 1636   | No file  | `2e093ceb79ad`  |
| 1628   | No file  | `2e093ceb79ad`  |
| 1622   | No file  | `2e093ceb79ad`  |
| 1614   | No file  | `2e093ceb79ad`  |
| 1608   | No file  | `2e093ceb79ad`  |
| 1602   | No file  | `2e093ceb79ad`  |
| 1598   | No file  | `2e093ceb79ad`  |
| 1594   | No file  | `2e093ceb79ad`  |
| 1590   | No file  | `2e093ceb79ad`  |
| 1587   | No file  | `2e093ceb79ad`  |
| 1584   | No file  | `2e093ceb79ad`  |
| 1579   | No file  | `2e093ceb79ad`  |
| 1572   | No file  | `2e093ceb79ad`  |
| 1565   | No file  | `2e093ceb79ad`  |
| 1559   | No file  | `2e093ceb79ad`  |
| 1554   | No file  | `2e093ceb79ad`  |
| 1547   | No file  | `2e093ceb79ad`  |
| 1537   | No file  | `2e093ceb79ad`  |
| 1529   | No file  | `2e093ceb79ad`  |
| 1524   | No file  | `2e093ceb79ad`  |
| 1519   | No file  | `2e093ceb79ad`  |
| 1509   | No file  | `2e093ceb79ad`  |
| 1506   | No file  | `2e093ceb79ad`  |
| 1504   | No file  | `2e093ceb79ad`  |
| 1500   | No file  | `2e093ceb79ad`  |
| 1493   | No file  | `2e093ceb79ad`  |
| 1489   | No file  | `2e093ceb79ad`  |
| 1485   | No file  | `2e093ceb79ad`  |
| 1481   | No file  | `2e093ceb79ad`  |
| 1474   | No file  | `2e093ceb79ad`  |
| 1466   | No file  | `2e093ceb79ad`  |
| 1462   | No file  | `2e093ceb79ad`  |
| 1459   | No file  | `2e093ceb79ad`  |
| 1453   | No file  | `2e093ceb79ad`  |
| 1450   | No file  | `2e093ceb79ad`  |
| 1445   | No file  | `2e093ceb79ad`  |
| 1439   | No file  | `2e093ceb79ad`  |
| 1433   | No file  | `2e093ceb79ad`  |
| 1430   | No file  | `2e093ceb79ad`  |
| 1426   | No file  | `2e093ceb79ad`  |
| 1421   | No file  | `2e093ceb79ad`  |
| 1417   | No file  | `2e093ceb79ad`  |
| 1416   | No file  | `2e093ceb79ad`  |
| 1409   | No file  | `2e093ceb79ad`  |
| 1405   | No file  | `2e093ceb79ad`  |
| 1401   | No file  | `2e093ceb79ad`  |
| 1396   | No file  | `2e093ceb79ad`  |
| 1391   | No file  | `2e093ceb79ad`  |
| 1390   | No file  | `2e093ceb79ad`  |
| 1386   | No file  | `2e093ceb79ad`  |
| 1381   | No file  | `2e093ceb79ad`  |
| 1379   | No file  | `2e093ceb79ad`  |
| 1372   | No file  | `2e093ceb79ad`  |
| 1366   | No file  | `2e093ceb79ad`  |
| 1364   | No file  | `2e093ceb79ad`  |
| 1363   | No file  | `2e093ceb79ad`  |
| 1360   | No file  | `2e093ceb79ad`  |
| 1358   | No file  | `2e093ceb79ad`  |
| 1355   | No file  | `2e093ceb79ad`  |
| 1351   | No file  | `2e093ceb79ad`  |
| 1348   | No file  | `2e093ceb79ad`  |
| 1346   | No file  | `2e093ceb79ad`  |
| 1341   | No file  | `2e093ceb79ad`  |
| 1340   | No file  | `2e093ceb79ad`  |
| 1338   | No file  | `2e093ceb79ad`  |
| 1335   | No file  | `2e093ceb79ad`  |
| 1333   | No file  | `2e093ceb79ad`  |
| 1329   | No file  | `2e093ceb79ad`  |
| 1327   | No file  | `2e093ceb79ad`  |
| 1324   | No file  | `2e093ceb79ad`  |
| 1321   | No file  | `2e093ceb79ad`  |
| 1319   | No file  | `2e093ceb79ad`  |
| 1318   | No file  | `2e093ceb79ad`  |
| 1316   | No file  | `2e093ceb79ad`  |
| 1313   | No file  | `2e093ceb79ad`  |
| 1311   | No file  | `2e093ceb79ad`  |
| 1309   | No file  | `2e093ceb79ad`  |
| 1304   | No file  | `2e093ceb79ad`  |
| 1292   | No file  | `2e093ceb79ad`  |
| 1286   | No file  | `2e093ceb79ad`  |
| 1280   | No file  | `2e093ceb79ad`  |
| 1276   | No file  | `2e093ceb79ad`  |
| 1267   | No file  | `2e093ceb79ad`  |
| 1261   | No file  | `2e093ceb79ad`  |
| 1256   | No file  | `2e093ceb79ad`  |
| 1250   | No file  | `2e093ceb79ad`  |
| 1246   | No file  | `2e093ceb79ad`  |
| 1239   | No file  | `2e093ceb79ad`  |
| 1230   | No file  | `2e093ceb79ad`  |
| 1226   | No file  | `2e093ceb79ad`  |
| 1220   | No file  | `2e093ceb79ad`  |
| 1217   | No file  | `2e093ceb79ad`  |
| 1211   | No file  | `2e093ceb79ad`  |
| 1210   | No file  | `2e093ceb79ad`  |
| 1208   | No file  | `2e093ceb79ad`  |
| 1203   | No file  | `2e093ceb79ad`  |
| 1197   | No file  | `2e093ceb79ad`  |
| 1194   | No file  | `2e093ceb79ad`  |
| 1192   | No file  | `2e093ceb79ad`  |
| 1187   | No file  | `2e093ceb79ad`  |
| 1183   | No file  | `2e093ceb79ad`  |
| 1177   | No file  | `2e093ceb79ad`  |
| 1173   | No file  | `2e093ceb79ad`  |
| 1167   | No file  | `2e093ceb79ad`  |
| 1164   | No file  | `2e093ceb79ad`  |
| 1156   | No file  | `2e093ceb79ad`  |
| 1149   | No file  | `2e093ceb79ad`  |
| 1144   | No file  | `2e093ceb79ad`  |
| 1137   | No file  | `2e093ceb79ad`  |
| 1132   | No file  | `2e093ceb79ad`  |
| 1127   | No file  | `2e093ceb79ad`  |
| 1122   | No file  | `2e093ceb79ad`  |
| 1118   | No file  | `2e093ceb79ad`  |
| 1114   | No file  | `2e093ceb79ad`  |
| 1109   | No file  | `2e093ceb79ad`  |
| 1102   | No file  | `2e093ceb79ad`  |
| 1096   | No file  | `2e093ceb79ad`  |
| 1088   | No file  | `2e093ceb79ad`  |
| 1081   | No file  | `2e093ceb79ad`  |
| 1076   | No file  | `2e093ceb79ad`  |
| 1069   | No file  | `2e093ceb79ad`  |
| 1064   | No file  | `2e093ceb79ad`  |
| 1058   | No file  | `2e093ceb79ad`  |
| 1051   | No file  | `2e093ceb79ad`  |
| 1044   | No file  | `2e093ceb79ad`  |
| 1036   | No file  | `2e093ceb79ad`  |
| 1026   | No file  | `2e093ceb79ad`  |
| 1016   | No file  | `2e093ceb79ad`  |
| 1009   | No file  | `2e093ceb79ad`  |
| 1005   | No file  | `2e093ceb79ad`  |
| 1000   | No file  | `2e093ceb79ad`  |
| 998    | No file  | `2e093ceb79ad`  |
| 990    | No file  | `2e093ceb79ad`  |
| 979    | No file  | `2e093ceb79ad`  |
| 972    | No file  | `2e093ceb79ad`  |
| 963    | No file  | `2e093ceb79ad`  |
| 955    | No file  | `2e093ceb79ad`  |
| 946    | No file  | `2e093ceb79ad`  |
| 938    | No file  | `2e093ceb79ad`  |
| 927    | No file  | `2e093ceb79ad`  |
| 911    | No file  | `2e093ceb79ad`  |
| 904    | No file  | `2e093ceb79ad`  |
| 899    | No file  | `2e093ceb79ad`  |
| 894    | No file  | `2e093ceb79ad`  |
| 885    | No file  | `2e093ceb79ad`  |
| 879    | No file  | `2e093ceb79ad`  |
| 872    | No file  | `2e093ceb79ad`  |
| 864    | No file  | `2e093ceb79ad`  |
| 855    | No file  | `2e093ceb79ad`  |
| 853    | No file  | `2e093ceb79ad`  |
| 845    | No file  | `2e093ceb79ad`  |
| 837    | No file  | `2e093ceb79ad`  |
| 829    | No file  | `2e093ceb79ad`  |
| 822    | No file  | `2e093ceb79ad`  |
| 814    | No file  | `2e093ceb79ad`  |
| 805    | No file  | `2e093ceb79ad`  |
| 794    | No file  | `2e093ceb79ad`  |
| 787    | No file  | `2e093ceb79ad`  |
| 780    | No file  | `2e093ceb79ad`  |
| 771    | No file  | `2e093ceb79ad`  |
| 760    | No file  | `2e093ceb79ad`  |
| 748    | No file  | `2e093ceb79ad`  |
| 741    | No file  | `2e093ceb79ad`  |
| 736    | No file  | `2e093ceb79ad`  |
| 731    | No file  | `2e093ceb79ad`  |
| 723    | No file  | `2e093ceb79ad`  |
| 711    | No file  | `2e093ceb79ad`  |
| 707    | No file  | `2e093ceb79ad`  |
| 697    | No file  | `2e093ceb79ad`  |
| 689    | No file  | `2e093ceb79ad`  |
| 683    | No file  | `2e093ceb79ad`  |
| 678    | No file  | `2e093ceb79ad`  |
| 670    | No file  | `2e093ceb79ad`  |
| 661    | No file  | `2e093ceb79ad`  |
| 656    | No file  | `2e093ceb79ad`  |
| 652    | No file  | `2e093ceb79ad`  |
| 643    | No file  | `2e093ceb79ad`  |
| 637    | No file  | `2e093ceb79ad`  |
| 630    | No file  | `2e093ceb79ad`  |
| 627    | No file  | `2e093ceb79ad`  |
| 621    | No file  | `2e093ceb79ad`  |
| 617    | No file  | `2e093ceb79ad`  |
| 615    | No file  | `2e093ceb79ad`  |
| 606    | No file  | `2e093ceb79ad`  |
| 599    | No file  | `2e093ceb79ad`  |
| 592    | No file  | `2e093ceb79ad`  |
| 586    | No file  | `2e093ceb79ad`  |
| 577    | No file  | `2e093ceb79ad`  |
| 569    | No file  | `2e093ceb79ad`  |
| 561    | No file  | `2e093ceb79ad`  |
| 554    | No file  | `2e093ceb79ad`  |
| 542    | No file  | `2e093ceb79ad`  |
| 532    | No file  | `2e093ceb79ad`  |
| 531    | No file  | `2e093ceb79ad`  |
| 526    | No file  | `2e093ceb79ad`  |
| 521    | No file  | `2e093ceb79ad`  |
| 517    | No file  | `2e093ceb79ad`  |
| 510    | No file  | `2e093ceb79ad`  |
| 508    | No file  | `2e093ceb79ad`  |
| 504    | No file  | `2e093ceb79ad`  |
| 497    | No file  | `2e093ceb79ad`  |
| 491    | No file  | `2e093ceb79ad`  |
| 485    | No file  | `2e093ceb79ad`  |
| 478    | No file  | `2e093ceb79ad`  |
| 472    | No file  | `2e093ceb79ad`  |
| 466    | No file  | `2e093ceb79ad`  |
| 457    | No file  | `2e093ceb79ad`  |
| 452    | No file  | `2e093ceb79ad`  |
| 449    | No file  | `2e093ceb79ad`  |
| 435    | No file  | `2e093ceb79ad`  |

<!-- versions:end -->

## Companion Files

None. The handler names each category with LOC type 118 from
`languagedata_*.loc` when it is loaded, else with its Korean name.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of categories                          |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (8 bytes)

| Offset  | Type | Field             | Notes                                                        |
| ------- | ---- | ----------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | category_key      | The category; `1` to `9` in key order (client 3483)          |
| `+0x04` | u32  | category_name_ref | String table index of the category's Korean name             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                |
| ------- | ------------------ | ------------ | ---------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                    |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE category names, one per row, in row order   |

## Categories

The 9 rows of client 3483. LOC type 118 holds the name under `str_id1` =
`category_key` for every row.

| `category_key` | Korean name          | LOC type 118               |
| -------------- | -------------------- | -------------------------- |
| 1              | `크론 정식 /음식`    | Cron Meals/Food            |
| 2              | `영약 / 비약`        | Draughts/Elixirs           |
| 3              | `향수 `              | Perfumes                   |
| 4              | `별채 주문서`        | Villa Scrolls              |
| 5              | `모험의 가호 주문서` | Adventure's Boon Scrolls   |
| 6              | `영물의 축복`        | Blessings of Mystic Beasts |
| 7              | `황금 축복`          | Golden Blessings           |
| 8              | `주문서`             | Scrolls                    |
| 9              | `기타`               | Other                      |

The Korean name and the LOC text of category `3` both end in a space.

## Field Names

Client 1784 has no `autousebuffitemcategoryinfo.bss`, and no sheet of a
private server's `DataSheets.bexcel` on client 1784 holds these rows. The
names follow the client 3482 Lua getters
`ToClient_getAutoUseBuffItemCategoryKey` and `getCategoryName`, and
`category_key` is the name
[`buffitemautousestaticstatus.bss`](buffitemautousestaticstatus_bss.md)
gives the same key.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/item_tables.py`: the
  category key and its name.
