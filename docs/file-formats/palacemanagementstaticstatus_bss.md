# `palacemanagementstaticstatus.bss` Format

## Purpose

The palace management (royal workshop) boards: eight board groups, each
with its Korean name, texture, type (production or processing), NPC and
boards, then the production boards with their items and chances, the
processing boards with their items, six u16 settings and a u16 per service
nation code. Every item is an `itemexchangesource.bss` key. The Lua reads
it through the `ToClient_PalaceManage*` and `ToClient_GetPalaceManage*`
calls of `panel_window_palacemanagement_*.luac`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes | Records                                                                                                                     | Row bytes |
| ------ | -------------- | ---------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------- | --------- |
| 1      | 2726 and later | `palacemanagementstaticstatus.bss` | 4,325 | 32 Board Ref, 8 Board Group, 182 Production Item, 20 Production Board, 84 Manufacture Item, 12 Manufacture Board, 12 Nation | 10        |

| Layout | File                               | Known           | Unknown     |
| ------ | ---------------------------------- | --------------- | ----------- |
| 1      | `palacemanagementstaticstatus.bss` | 4,257 B (98.4%) | 68 B (1.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `4f471c8ece62`  |
| 3482   | Layout 1             | `4f471c8ece62`  |
| 3474   | Layout 1             | `4f471c8ece62`  |
| 3473   | Layout 1             | `4f471c8ece62`  |
| 3464   | Layout 1             | `4f471c8ece62`  |
| 3458   | Layout 1             | `4f471c8ece62`  |
| 3454   | Layout 1             | `4f471c8ece62`  |
| 3444   | Layout 1             | `4f471c8ece62`  |
| 3435   | Layout 1             | `4f471c8ece62`  |
| 3426   | Layout 1             | `4f471c8ece62`  |
| 3418   | Layout 1             | `4f471c8ece62`  |
| 3412   | Layout 1             | `4f471c8ece62`  |
| 3402   | Layout 1             | `4f471c8ece62`  |
| 3396   | Layout 1             | `4f471c8ece62`  |
| 3387   | Layout 1             | `4f471c8ece62`  |
| 3381   | Layout 1             | `4f471c8ece62`  |
| 3373   | Layout 1             | `4f471c8ece62`  |
| 3364   | Layout 1             | `4f471c8ece62`  |
| 3356   | Layout 1             | `4f471c8ece62`  |
| 3349   | Layout 1             | `4f471c8ece62`  |
| 3342   | Layout 1             | `4f471c8ece62`  |
| 3335   | Layout 1             | `4f471c8ece62`  |
| 3326   | Layout 1             | `4f471c8ece62`  |
| 3321   | Layout 1             | `4f471c8ece62`  |
| 3314   | Layout 1             | `4f471c8ece62`  |
| 3303   | Layout 1             | `4f471c8ece62`  |
| 3302   | Layout 1             | `4f471c8ece62`  |
| 3293   | Layout 1             | `4f471c8ece62`  |
| 3283   | Layout 1             | `4f471c8ece62`  |
| 3275   | Layout 1             | `4f471c8ece62`  |
| 3267   | Layout 1             | `4f471c8ece62`  |
| 3258   | Layout 1             | `4f471c8ece62`  |
| 3251   | Layout 1             | `4f471c8ece62`  |
| 3242   | Layout 1             | `4f471c8ece62`  |
| 3235   | Layout 1             | `4f471c8ece62`  |
| 3229   | Layout 1             | `4f471c8ece62`  |
| 3212   | Layout 1             | `4f471c8ece62`  |
| 3203   | Layout 1             | `4f471c8ece62`  |
| 3193   | Layout 1             | `4f471c8ece62`  |
| 3186   | Layout 1             | `4f471c8ece62`  |
| 3177   | Layout 1             | `4f471c8ece62`  |
| 3169   | Layout 1             | `4f471c8ece62`  |
| 3158   | Layout 1             | `4f471c8ece62`  |
| 3151   | Layout 1             | `4f471c8ece62`  |
| 3144   | Layout 1             | `4f471c8ece62`  |
| 3133   | Layout 1             | `4f471c8ece62`  |
| 3125   | Layout 1             | `4f471c8ece62`  |
| 3118   | Layout 1             | `4f471c8ece62`  |
| 3111   | Layout 1             | `4f471c8ece62`  |
| 3103   | Layout 1             | `4f471c8ece62`  |
| 3095   | Layout 1             | `4f471c8ece62`  |
| 3086   | Layout 1             | `4f471c8ece62`  |
| 3072   | Layout 1             | `4f471c8ece62`  |
| 3062   | Layout 1             | `4f471c8ece62`  |
| 3052   | Layout 1             | `4f471c8ece62`  |
| 3045   | Layout 1             | `4f471c8ece62`  |
| 3037   | Layout 1             | `4f471c8ece62`  |
| 3030   | Layout 1             | `4f471c8ece62`  |
| 3021   | Layout 1             | `4f471c8ece62`  |
| 3012   | Layout 1             | `4f471c8ece62`  |
| 3002   | Layout 1             | `4f471c8ece62`  |
| 2995   | Layout 1             | `4f471c8ece62`  |
| 2987   | Layout 1             | `4f471c8ece62`  |
| 2978   | Layout 1             | `4f471c8ece62`  |
| 2970   | Layout 1             | `4f471c8ece62`  |
| 2959   | Layout 1             | `4f471c8ece62`  |
| 2951   | Layout 1             | `4f471c8ece62`  |
| 2942   | Layout 1             | `4f471c8ece62`  |
| 2935   | Layout 1             | `4f471c8ece62`  |
| 2932   | Layout 1             | `4f471c8ece62`  |
| 2923   | Layout 1             | `4f471c8ece62`  |
| 2919   | Layout 1             | `4f471c8ece62`  |
| 2907   | Layout 1             | `4f471c8ece62`  |
| 2900   | Layout 1             | `4f471c8ece62`  |
| 2891   | Layout 1             | `4f471c8ece62`  |
| 2882   | Layout 1             | `4f471c8ece62`  |
| 2872   | Layout 1             | `4f471c8ece62`  |
| 2863   | Layout 1             | `4f471c8ece62`  |
| 2855   | Layout 1             | `4f471c8ece62`  |
| 2849   | Layout 1             | `4f471c8ece62`  |
| 2844   | Layout 1             | `4f471c8ece62`  |
| 2834   | Layout 1             | `4f471c8ece62`  |
| 2825   | Layout 1             | `4f471c8ece62`  |
| 2819   | Layout 1             | `4f471c8ece62`  |
| 2811   | Layout 1             | `4f471c8ece62`  |
| 2803   | Layout 1             | `4f471c8ece62`  |
| 2794   | Layout 1             | `4f471c8ece62`  |
| 2783   | Layout 1             | `4f471c8ece62`  |
| 2774   | Layout 1             | `4f471c8ece62`  |
| 2765   | Layout 1             | `4f471c8ece62`  |
| 2756   | Layout 1             | `4f471c8ece62`  |
| 2750   | Layout 1             | `4f471c8ece62`  |
| 2743   | Layout 1             | `4f471c8ece62`  |
| 2736   | Layout 1             | `4f471c8ece62`  |
| 2726   | Layout 1             | `4f471c8ece62`  |
| 2717   | No documented layout | `4f471c8ece62`  |
| 2709   | No documented layout | `4f471c8ece62`  |
| 2703   | No file              | `4f471c8ece62`  |
| 2695   | No file              | `4f471c8ece62`  |
| 2684   | No file              | `4f471c8ece62`  |
| 2672   | No file              | `4f471c8ece62`  |
| 2665   | No file              | `4f471c8ece62`  |
| 2657   | No file              | `4f471c8ece62`  |
| 2649   | No file              | `4f471c8ece62`  |
| 2644   | No file              | `4f471c8ece62`  |
| 2637   | No file              | `4f471c8ece62`  |
| 2629   | No file              | `4f471c8ece62`  |
| 2619   | No file              | `4f471c8ece62`  |
| 2612   | No file              | `4f471c8ece62`  |
| 2606   | No file              | `4f471c8ece62`  |
| 2602   | No file              | `4f471c8ece62`  |
| 2601   | No file              | `4f471c8ece62`  |
| 2592   | No file              | `4f471c8ece62`  |
| 2583   | No file              | `4f471c8ece62`  |
| 2575   | No file              | `4f471c8ece62`  |
| 2567   | No file              | `4f471c8ece62`  |
| 2560   | No file              | `4f471c8ece62`  |
| 2553   | No file              | `4f471c8ece62`  |
| 2545   | No file              | `4f471c8ece62`  |
| 2538   | No file              | `4f471c8ece62`  |
| 2529   | No file              | `4f471c8ece62`  |
| 2519   | No file              | `4f471c8ece62`  |
| 2513   | No file              | `4f471c8ece62`  |
| 2510   | No file              | `4f471c8ece62`  |
| 2507   | No file              | `4f471c8ece62`  |
| 2503   | No file              | `4f471c8ece62`  |
| 2498   | No file              | `4f471c8ece62`  |
| 2492   | No file              | `4f471c8ece62`  |
| 2487   | No file              | `4f471c8ece62`  |
| 2480   | No file              | `4f471c8ece62`  |
| 2474   | No file              | `4f471c8ece62`  |
| 2468   | No file              | `4f471c8ece62`  |
| 2460   | No file              | `4f471c8ece62`  |
| 2453   | No file              | `4f471c8ece62`  |
| 2444   | No file              | `4f471c8ece62`  |
| 2438   | No file              | `4f471c8ece62`  |
| 2434   | No file              | `4f471c8ece62`  |
| 2429   | No file              | `4f471c8ece62`  |
| 2421   | No file              | `4f471c8ece62`  |
| 2414   | No file              | `4f471c8ece62`  |
| 2407   | No file              | `4f471c8ece62`  |
| 2401   | No file              | `4f471c8ece62`  |
| 2397   | No file              | `4f471c8ece62`  |
| 2393   | No file              | `4f471c8ece62`  |
| 2384   | No file              | `4f471c8ece62`  |
| 2378   | No file              | `4f471c8ece62`  |
| 2372   | No file              | `4f471c8ece62`  |
| 2358   | No file              | `4f471c8ece62`  |
| 2352   | No file              | `4f471c8ece62`  |
| 2347   | No file              | `4f471c8ece62`  |
| 2343   | No file              | `4f471c8ece62`  |
| 2335   | No file              | `4f471c8ece62`  |
| 2327   | No file              | `4f471c8ece62`  |
| 2324   | No file              | `4f471c8ece62`  |
| 2319   | No file              | `4f471c8ece62`  |
| 2313   | No file              | `4f471c8ece62`  |
| 2308   | No file              | `4f471c8ece62`  |
| 2302   | No file              | `4f471c8ece62`  |
| 2295   | No file              | `4f471c8ece62`  |
| 2290   | No file              | `4f471c8ece62`  |
| 2284   | No file              | `4f471c8ece62`  |
| 2276   | No file              | `4f471c8ece62`  |
| 2269   | No file              | `4f471c8ece62`  |
| 2259   | No file              | `4f471c8ece62`  |
| 2250   | No file              | `4f471c8ece62`  |
| 2243   | No file              | `4f471c8ece62`  |
| 2235   | No file              | `4f471c8ece62`  |
| 2229   | No file              | `4f471c8ece62`  |
| 2224   | No file              | `4f471c8ece62`  |
| 2218   | No file              | `4f471c8ece62`  |
| 2215   | No file              | `4f471c8ece62`  |
| 2207   | No file              | `4f471c8ece62`  |
| 2203   | No file              | `4f471c8ece62`  |
| 2196   | No file              | `4f471c8ece62`  |
| 2192   | No file              | `4f471c8ece62`  |
| 2189   | No file              | `4f471c8ece62`  |
| 2183   | No file              | `4f471c8ece62`  |
| 2179   | No file              | `4f471c8ece62`  |
| 2171   | No file              | `4f471c8ece62`  |
| 2163   | No file              | `4f471c8ece62`  |
| 2156   | No file              | `4f471c8ece62`  |
| 2151   | No file              | `4f471c8ece62`  |
| 2147   | No file              | `4f471c8ece62`  |
| 2142   | No file              | `4f471c8ece62`  |
| 2138   | No file              | `4f471c8ece62`  |
| 2134   | No file              | `4f471c8ece62`  |
| 2130   | No file              | `4f471c8ece62`  |
| 2122   | No file              | `4f471c8ece62`  |
| 2107   | No file              | `4f471c8ece62`  |
| 2098   | No file              | `4f471c8ece62`  |
| 2089   | No file              | `4f471c8ece62`  |
| 2081   | No file              | `4f471c8ece62`  |
| 2073   | No file              | `4f471c8ece62`  |
| 2067   | No file              | `4f471c8ece62`  |
| 2063   | No file              | `4f471c8ece62`  |
| 2059   | No file              | `4f471c8ece62`  |
| 2052   | No file              | `4f471c8ece62`  |
| 2044   | No file              | `4f471c8ece62`  |
| 2039   | No file              | `4f471c8ece62`  |
| 2032   | No file              | `4f471c8ece62`  |
| 2025   | No file              | `4f471c8ece62`  |
| 2011   | No file              | `4f471c8ece62`  |
| 2005   | No file              | `4f471c8ece62`  |
| 2000   | No file              | `4f471c8ece62`  |
| 1996   | No file              | `4f471c8ece62`  |
| 1991   | No file              | `4f471c8ece62`  |
| 1985   | No file              | `4f471c8ece62`  |
| 1980   | No file              | `4f471c8ece62`  |
| 1969   | No file              | `4f471c8ece62`  |
| 1964   | No file              | `4f471c8ece62`  |
| 1958   | No file              | `4f471c8ece62`  |
| 1950   | No file              | `4f471c8ece62`  |
| 1945   | No file              | `4f471c8ece62`  |
| 1937   | No file              | `4f471c8ece62`  |
| 1933   | No file              | `4f471c8ece62`  |
| 1927   | No file              | `4f471c8ece62`  |
| 1921   | No file              | `4f471c8ece62`  |
| 1914   | No file              | `4f471c8ece62`  |
| 1908   | No file              | `4f471c8ece62`  |
| 1897   | No file              | `4f471c8ece62`  |
| 1892   | No file              | `4f471c8ece62`  |
| 1886   | No file              | `4f471c8ece62`  |
| 1881   | No file              | `4f471c8ece62`  |
| 1871   | No file              | `4f471c8ece62`  |
| 1866   | No file              | `4f471c8ece62`  |
| 1862   | No file              | `4f471c8ece62`  |
| 1854   | No file              | `4f471c8ece62`  |
| 1846   | No file              | `4f471c8ece62`  |
| 1838   | No file              | `4f471c8ece62`  |
| 1832   | No file              | `4f471c8ece62`  |
| 1826   | No file              | `4f471c8ece62`  |
| 1822   | No file              | `4f471c8ece62`  |
| 1818   | No file              | `4f471c8ece62`  |
| 1804   | No file              | `4f471c8ece62`  |
| 1794   | No file              | `4f471c8ece62`  |
| 1790   | No file              | `4f471c8ece62`  |
| 1784   | No file              | `4f471c8ece62`  |
| 1774   | No file              | `4f471c8ece62`  |
| 1771   | No file              | `4f471c8ece62`  |
| 1762   | No file              | `4f471c8ece62`  |
| 1759   | No file              | `4f471c8ece62`  |
| 1754   | No file              | `4f471c8ece62`  |
| 1749   | No file              | `4f471c8ece62`  |
| 1743   | No file              | `4f471c8ece62`  |
| 1737   | No file              | `4f471c8ece62`  |
| 1731   | No file              | `4f471c8ece62`  |
| 1725   | No file              | `4f471c8ece62`  |
| 1717   | No file              | `4f471c8ece62`  |
| 1710   | No file              | `4f471c8ece62`  |
| 1704   | No file              | `4f471c8ece62`  |
| 1698   | No file              | `4f471c8ece62`  |
| 1690   | No file              | `4f471c8ece62`  |
| 1685   | No file              | `4f471c8ece62`  |
| 1680   | No file              | `4f471c8ece62`  |
| 1674   | No file              | `4f471c8ece62`  |
| 1668   | No file              | `4f471c8ece62`  |
| 1659   | No file              | `4f471c8ece62`  |
| 1649   | No file              | `4f471c8ece62`  |
| 1642   | No file              | `4f471c8ece62`  |
| 1636   | No file              | `4f471c8ece62`  |
| 1628   | No file              | `4f471c8ece62`  |
| 1622   | No file              | `4f471c8ece62`  |
| 1614   | No file              | `4f471c8ece62`  |
| 1608   | No file              | `4f471c8ece62`  |
| 1602   | No file              | `4f471c8ece62`  |
| 1598   | No file              | `4f471c8ece62`  |
| 1594   | No file              | `4f471c8ece62`  |
| 1590   | No file              | `4f471c8ece62`  |
| 1587   | No file              | `4f471c8ece62`  |
| 1584   | No file              | `4f471c8ece62`  |
| 1579   | No file              | `4f471c8ece62`  |
| 1572   | No file              | `4f471c8ece62`  |
| 1565   | No file              | `4f471c8ece62`  |
| 1559   | No file              | `4f471c8ece62`  |
| 1554   | No file              | `4f471c8ece62`  |
| 1547   | No file              | `4f471c8ece62`  |
| 1537   | No file              | `4f471c8ece62`  |
| 1529   | No file              | `4f471c8ece62`  |
| 1524   | No file              | `4f471c8ece62`  |
| 1519   | No file              | `4f471c8ece62`  |
| 1509   | No file              | `4f471c8ece62`  |
| 1506   | No file              | `4f471c8ece62`  |
| 1504   | No file              | `4f471c8ece62`  |
| 1500   | No file              | `4f471c8ece62`  |
| 1493   | No file              | `4f471c8ece62`  |
| 1489   | No file              | `4f471c8ece62`  |
| 1485   | No file              | `4f471c8ece62`  |
| 1481   | No file              | `4f471c8ece62`  |
| 1474   | No file              | `4f471c8ece62`  |
| 1466   | No file              | `4f471c8ece62`  |
| 1462   | No file              | `4f471c8ece62`  |
| 1459   | No file              | `4f471c8ece62`  |
| 1453   | No file              | `4f471c8ece62`  |
| 1450   | No file              | `4f471c8ece62`  |
| 1445   | No file              | `4f471c8ece62`  |
| 1439   | No file              | `4f471c8ece62`  |
| 1433   | No file              | `4f471c8ece62`  |
| 1430   | No file              | `4f471c8ece62`  |
| 1426   | No file              | `4f471c8ece62`  |
| 1421   | No file              | `4f471c8ece62`  |
| 1417   | No file              | `4f471c8ece62`  |
| 1416   | No file              | `4f471c8ece62`  |
| 1409   | No file              | `4f471c8ece62`  |
| 1405   | No file              | `4f471c8ece62`  |
| 1401   | No file              | `4f471c8ece62`  |
| 1396   | No file              | `4f471c8ece62`  |
| 1391   | No file              | `4f471c8ece62`  |
| 1390   | No file              | `4f471c8ece62`  |
| 1386   | No file              | `4f471c8ece62`  |
| 1381   | No file              | `4f471c8ece62`  |
| 1379   | No file              | `4f471c8ece62`  |
| 1372   | No file              | `4f471c8ece62`  |
| 1366   | No file              | `4f471c8ece62`  |
| 1364   | No file              | `4f471c8ece62`  |
| 1363   | No file              | `4f471c8ece62`  |
| 1360   | No file              | `4f471c8ece62`  |
| 1358   | No file              | `4f471c8ece62`  |
| 1355   | No file              | `4f471c8ece62`  |
| 1351   | No file              | `4f471c8ece62`  |
| 1348   | No file              | `4f471c8ece62`  |
| 1346   | No file              | `4f471c8ece62`  |
| 1341   | No file              | `4f471c8ece62`  |
| 1340   | No file              | `4f471c8ece62`  |
| 1338   | No file              | `4f471c8ece62`  |
| 1335   | No file              | `4f471c8ece62`  |
| 1333   | No file              | `4f471c8ece62`  |
| 1329   | No file              | `4f471c8ece62`  |
| 1327   | No file              | `4f471c8ece62`  |
| 1324   | No file              | `4f471c8ece62`  |
| 1321   | No file              | `4f471c8ece62`  |
| 1319   | No file              | `4f471c8ece62`  |
| 1318   | No file              | `4f471c8ece62`  |
| 1316   | No file              | `4f471c8ece62`  |
| 1313   | No file              | `4f471c8ece62`  |
| 1311   | No file              | `4f471c8ece62`  |
| 1309   | No file              | `4f471c8ece62`  |
| 1304   | No file              | `4f471c8ece62`  |
| 1292   | No file              | `4f471c8ece62`  |
| 1286   | No file              | `4f471c8ece62`  |
| 1280   | No file              | `4f471c8ece62`  |
| 1276   | No file              | `4f471c8ece62`  |
| 1267   | No file              | `4f471c8ece62`  |
| 1261   | No file              | `4f471c8ece62`  |
| 1256   | No file              | `4f471c8ece62`  |
| 1250   | No file              | `4f471c8ece62`  |
| 1246   | No file              | `4f471c8ece62`  |
| 1239   | No file              | `4f471c8ece62`  |
| 1230   | No file              | `4f471c8ece62`  |
| 1226   | No file              | `4f471c8ece62`  |
| 1220   | No file              | `4f471c8ece62`  |
| 1217   | No file              | `4f471c8ece62`  |
| 1211   | No file              | `4f471c8ece62`  |
| 1210   | No file              | `4f471c8ece62`  |
| 1208   | No file              | `4f471c8ece62`  |
| 1203   | No file              | `4f471c8ece62`  |
| 1197   | No file              | `4f471c8ece62`  |
| 1194   | No file              | `4f471c8ece62`  |
| 1192   | No file              | `4f471c8ece62`  |
| 1187   | No file              | `4f471c8ece62`  |
| 1183   | No file              | `4f471c8ece62`  |
| 1177   | No file              | `4f471c8ece62`  |
| 1173   | No file              | `4f471c8ece62`  |
| 1167   | No file              | `4f471c8ece62`  |
| 1164   | No file              | `4f471c8ece62`  |
| 1156   | No file              | `4f471c8ece62`  |
| 1149   | No file              | `4f471c8ece62`  |
| 1144   | No file              | `4f471c8ece62`  |
| 1137   | No file              | `4f471c8ece62`  |
| 1132   | No file              | `4f471c8ece62`  |
| 1127   | No file              | `4f471c8ece62`  |
| 1122   | No file              | `4f471c8ece62`  |
| 1118   | No file              | `4f471c8ece62`  |
| 1114   | No file              | `4f471c8ece62`  |
| 1109   | No file              | `4f471c8ece62`  |
| 1102   | No file              | `4f471c8ece62`  |
| 1096   | No file              | `4f471c8ece62`  |
| 1088   | No file              | `4f471c8ece62`  |
| 1081   | No file              | `4f471c8ece62`  |
| 1076   | No file              | `4f471c8ece62`  |
| 1069   | No file              | `4f471c8ece62`  |
| 1064   | No file              | `4f471c8ece62`  |
| 1058   | No file              | `4f471c8ece62`  |
| 1051   | No file              | `4f471c8ece62`  |
| 1044   | No file              | `4f471c8ece62`  |
| 1036   | No file              | `4f471c8ece62`  |
| 1026   | No file              | `4f471c8ece62`  |
| 1016   | No file              | `4f471c8ece62`  |
| 1009   | No file              | `4f471c8ece62`  |
| 1005   | No file              | `4f471c8ece62`  |
| 1000   | No file              | `4f471c8ece62`  |
| 998    | No file              | `4f471c8ece62`  |
| 990    | No file              | `4f471c8ece62`  |
| 979    | No file              | `4f471c8ece62`  |
| 972    | No file              | `4f471c8ece62`  |
| 963    | No file              | `4f471c8ece62`  |
| 955    | No file              | `4f471c8ece62`  |
| 946    | No file              | `4f471c8ece62`  |
| 938    | No file              | `4f471c8ece62`  |
| 927    | No file              | `4f471c8ece62`  |
| 911    | No file              | `4f471c8ece62`  |
| 904    | No file              | `4f471c8ece62`  |
| 899    | No file              | `4f471c8ece62`  |
| 894    | No file              | `4f471c8ece62`  |
| 885    | No file              | `4f471c8ece62`  |
| 879    | No file              | `4f471c8ece62`  |
| 872    | No file              | `4f471c8ece62`  |
| 864    | No file              | `4f471c8ece62`  |
| 855    | No file              | `4f471c8ece62`  |
| 853    | No file              | `4f471c8ece62`  |
| 845    | No file              | `4f471c8ece62`  |
| 837    | No file              | `4f471c8ece62`  |
| 829    | No file              | `4f471c8ece62`  |
| 822    | No file              | `4f471c8ece62`  |
| 814    | No file              | `4f471c8ece62`  |
| 805    | No file              | `4f471c8ece62`  |
| 794    | No file              | `4f471c8ece62`  |
| 787    | No file              | `4f471c8ece62`  |
| 780    | No file              | `4f471c8ece62`  |
| 771    | No file              | `4f471c8ece62`  |
| 760    | No file              | `4f471c8ece62`  |
| 748    | No file              | `4f471c8ece62`  |
| 741    | No file              | `4f471c8ece62`  |
| 736    | No file              | `4f471c8ece62`  |
| 731    | No file              | `4f471c8ece62`  |
| 723    | No file              | `4f471c8ece62`  |
| 711    | No file              | `4f471c8ece62`  |
| 707    | No file              | `4f471c8ece62`  |
| 697    | No file              | `4f471c8ece62`  |
| 689    | No file              | `4f471c8ece62`  |
| 683    | No file              | `4f471c8ece62`  |
| 678    | No file              | `4f471c8ece62`  |
| 670    | No file              | `4f471c8ece62`  |
| 661    | No file              | `4f471c8ece62`  |
| 656    | No file              | `4f471c8ece62`  |
| 652    | No file              | `4f471c8ece62`  |
| 643    | No file              | `4f471c8ece62`  |
| 637    | No file              | `4f471c8ece62`  |
| 630    | No file              | `4f471c8ece62`  |
| 627    | No file              | `4f471c8ece62`  |
| 621    | No file              | `4f471c8ece62`  |
| 617    | No file              | `4f471c8ece62`  |
| 615    | No file              | `4f471c8ece62`  |
| 606    | No file              | `4f471c8ece62`  |
| 599    | No file              | `4f471c8ece62`  |
| 592    | No file              | `4f471c8ece62`  |
| 586    | No file              | `4f471c8ece62`  |
| 577    | No file              | `4f471c8ece62`  |
| 569    | No file              | `4f471c8ece62`  |
| 561    | No file              | `4f471c8ece62`  |
| 554    | No file              | `4f471c8ece62`  |
| 542    | No file              | `4f471c8ece62`  |
| 532    | No file              | `4f471c8ece62`  |
| 531    | No file              | `4f471c8ece62`  |
| 526    | No file              | `4f471c8ece62`  |
| 521    | No file              | `4f471c8ece62`  |
| 517    | No file              | `4f471c8ece62`  |
| 510    | No file              | `4f471c8ece62`  |
| 508    | No file              | `4f471c8ece62`  |
| 504    | No file              | `4f471c8ece62`  |
| 497    | No file              | `4f471c8ece62`  |
| 491    | No file              | `4f471c8ece62`  |
| 485    | No file              | `4f471c8ece62`  |
| 478    | No file              | `4f471c8ece62`  |
| 472    | No file              | `4f471c8ece62`  |
| 466    | No file              | `4f471c8ece62`  |
| 457    | No file              | `4f471c8ece62`  |
| 452    | No file              | `4f471c8ece62`  |
| 449    | No file              | `4f471c8ece62`  |
| 435    | No file              | `4f471c8ece62`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                           |
| --------------------- | -------- | -------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | NPC names (LOC type 6) and exchange names (LOC type 24)        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                    | Type                                       | Field                         | Notes                                                    |
| ------------------------- | ------------------------------------------ | ----------------------------- | -------------------------------------------------------- |
| `+0x00`                   | char[4]                                    | magic                         | ASCII `PABR`                                             |
| `+0x04`                   | u32                                        | board_group_count             | Number of `board_groups`; `8` on client 3482             |
| `+0x08`                   | Board Group[board_group_count]             | board_groups                  | See Board Group                                          |
| `board_groups+0x00`       | u32                                        | production_board_count        | Number of `production_boards`; `20` on client 3482       |
| `board_groups+0x04`       | Production Board[production_board_count]   | production_boards             | See Production Board                                     |
| `production_boards+0x00`  | u32                                        | manufacture_board_count       | Number of `manufacture_boards`; `12` on client 3482      |
| `production_boards+0x04`  | Manufacture Board[manufacture_board_count] | manufacture_boards            | See Manufacture Board                                    |
| `manufacture_boards+0x00` | u16                                        | unknown_manufacture_boards_00 | `0`                                                      |
| `manufacture_boards+0x02` | u16                                        | unknown_manufacture_boards_02 | `1`                                                      |
| `manufacture_boards+0x04` | u16                                        | unknown_manufacture_boards_04 | `1`                                                      |
| `manufacture_boards+0x06` | u16                                        | unknown_manufacture_boards_06 | `10`                                                     |
| `manufacture_boards+0x08` | u16                                        | unknown_manufacture_boards_08 | `1420`, a node key (Magoria); see Open Questions         |
| `manufacture_boards+0x0A` | u16                                        | unknown_manufacture_boards_0a | `1419`, a node key (Magoria)                             |
| `manufacture_boards+0x0C` | u32                                        | nation_count                  | Number of `nations`; `12` on client 3482                 |
| `manufacture_boards+0x10` | Nation[nation_count]                       | nations                       | See Nation                                               |
| `nations+0x00`            | String Table                               | string_table                  | See String Table                                         |
| `EOF-0x08`                | u32                                        | table_start                   | Offset of the string table, where `nations` ends         |
| `EOF-0x04`                | u32                                        | zero                          | Always `0`                                               |

### Board Group (variable: 23 bytes + boards)

| Offset  | Type                   | Field                | Notes                                                                        |
| ------- | ---------------------- | -------------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u16                    | board_group_key      | `1` to `8`                                                                   |
| `+0x02` | u32                    | board_group_name_ref | String-table index of the Korean group name (`경회루` for group `1`)         |
| `+0x06` | u32                    | texture_ref          | String-table index of the texture ID, `Combine_Etc_PalaceManagement_NodePopUpImg_<n>` |
| `+0x0A` | u32                    | desc_ref             | String-table index of the description; `2`, the empty string, on every group |
| `+0x0E` | u8                     | board_group_type     | `0` production (groups `1` to `4`), `1` processing (`5` to `8`)              |
| `+0x0F` | u16                    | npc_character_key    | The group's NPC; LOC type 6 title `<Royal Workshop Manager>` on every group |
| `+0x11` | u16                    | npc_dialog_index     | `1` on every group                                                           |
| `+0x13` | u32                    | board_count          | Number of `boards`; `5` per production group, `3` per processing group       |
| `+0x17` | Board Ref[board_count] | boards               | See Board Ref                                                                |

### Board Ref (3 bytes)

| Offset  | Type | Field      | Notes                                                                                    |
| ------- | ---- | ---------- | ---------------------------------------------------------------------------------------- |
| `+0x00` | u16  | board_key  | A `production_boards` key in a production group, a `manufacture_boards` key in a processing group |
| `+0x02` | u8   | unknown_02 | `1` on the first board of each group, else `0`                                           |

### Production Board (variable: 10 bytes + items)

| Offset  | Type                         | Field          | Notes                                                    |
| ------- | ---------------------------- | -------------- | -------------------------------------------------------- |
| `+0x00` | u16                          | board_key      | `1` to `20`                                              |
| `+0x02` | u32                          | board_name_ref | String-table index of the Korean board name              |
| `+0x06` | u32                          | item_count     | Number of `items`; `7` to `10` on client 3482            |
| `+0x0A` | Production Item[item_count]  | items          | See Production Item                                      |

### Production Item (10 bytes)

| Offset  | Type | Field        | Notes                                                                    |
| ------- | ---- | ------------ | ------------------------------------------------------------------------ |
| `+0x00` | u16  | item_index   | `0` up, the item's place on its board                                    |
| `+0x02` | u32  | probability  | Chance on the 1,000,000 = 100% scale; a board's items sum to `1000000`   |
| `+0x06` | u32  | exchange_key | `itemexchangesource.bss` key                                             |

### Manufacture Board (variable: 10 bytes + items)

| Offset  | Type                          | Field          | Notes                                       |
| ------- | ----------------------------- | -------------- | ------------------------------------------- |
| `+0x00` | u16                           | board_key      | `1` to `12`                                 |
| `+0x02` | u32                           | board_name_ref | String-table index of the Korean board name |
| `+0x06` | u32                           | item_count     | Number of `items`; `7` on every board       |
| `+0x0A` | Manufacture Item[item_count]  | items          | See Manufacture Item                        |

### Manufacture Item (6 bytes)

| Offset  | Type | Field        | Notes                                  |
| ------- | ---- | ------------ | -------------------------------------- |
| `+0x00` | u16  | item_index   | `0` to `6`                             |
| `+0x02` | u32  | exchange_key | `itemexchangesource.bss` key           |

### Nation (6 bytes)

| Offset  | Type | Field           | Notes                                                       |
| ------- | ---- | --------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | nation_code_ref | String-table index of a service nation code (`KR`, `NA`)    |
| `+0x04` | u16  | unknown_04      | `10` to `50`; see Open Questions                            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                       |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `61` on client 3482                                      |
| `+0x04` | pstr[string_count] | strings      | UTF-16 Korean names, texture IDs, one empty string and the nation codes     |

## Board Groups

The groups on client 3482, with the NPC's LOC type 6 name.

| `board_group_key` | Name       | Type       | `npc_character_key` | NPC           | Boards     |
| ----------------- | ---------- | ---------- | ------------------- | ------------- | ---------- |
| 1                 | 경회루     | Production | `62114`             | Yeongman      | `1` to `5`   |
| 2                 | 제생원     | Production | `62115`             | Choi Doyun    | `6` to `10`  |
| 3                 | 좌조       | Production | `62116`             | Kim Munki     | `11` to `15` |
| 4                 | 우조       | Production | `62117`             | Park Gyusik   | `16` to `20` |
| 5                 | 도서관사   | Processing | `62123`             | Seokdo        | `1` to `3`   |
| 6                 | 소주방     | Processing | `62120`             | Park Sugyeong | `4` to `6`   |
| 7                 | 선원전     | Processing | `62121`             | Sangdeok      | `7` to `9`   |
| 8                 | 군부       | Processing | `62125`             | Hyeokcheol    | `10` to `12` |

The nations on client 3482, as `nation_code` and `unknown_04`: KR `10`,
JP `10`, RU `25`, CH `10`, NA `50`, TW `10`, SA `10`, TH `10`, ID `10`,
TR `12`, ASIA `10`, CS `50`.

## Field Names

The palace management content is newer than client 1784's sheets (the
file first ships in client 2765), so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. The names come from the
Lua of client 3482 and from the values:

| Field                                   | Lua (client 3482) and values                                                                    |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `board_group_key`                       | `ToClient_GetPalaceManageBoardGroupKey(index)` over `ToClient_GetPalaceManageBoardGroupCount()` |
| `board_group_name_ref`, `texture_ref`, `desc_ref` | `ToClient_GetPalaceManageBoardGroupName`, `...GetBoardGroupTextureID` and `...GetBoardGroupDesc(boardGroupKey)`: the three strings of each group are a Korean name, a texture ID and the one empty string |
| `board_group_type`                      | `ToClient_PalaceManagegetBoadGroupTypeRaw(boardGroupKey)`, compared with `__ePalaceManageType_Production` and `_Manufacture`; only type `0` groups list boards with chances, and the window asks `ToClient_PalaceManageGetProbability` only for production |
| `npc_character_key`, `npc_dialog_index` | `ToClient_PalaceManageGetNpcCharacterKey` and `...GetNpcDialogIndex(boardGroupKey)`; all eight keys are NPCs titled `<Royal Workshop Manager>` (LOC type 6) |
| `board_key`, `board_name_ref`           | `ToClient_PalaceManagegetBoadKeyRaw(boardGroupKey, index)` and `ToClient_PalaceManageGetBoardName` |
| `probability`                           | `ToClient_PalaceManageGetProbability(boardGroupKey, boardIndex, itemIndex)`; each production board sums to `1000000` |
| `exchange_key`                          | `ToClient_PalaceManageSelectItemExchangeSource(boardGroupKey, boardKey, itemIndex)`; every value is an `itemexchangesource.bss` key, `생산 거점` (production node) or `가공 거점` (processing node) by name |
| `nation_code_ref`                       | The strings it points to are the service nation codes                                           |

## Notes

- Clients 2765 and 3002 hold 11 nations (no `CS`) and are otherwise laid
  out the same; client 3251 matches client 3482 byte for byte. The file is
  not in the archives of client 1784.
- The handler shows one row per board item: the board group, its type and
  NPC, the board, the item index, the chance and the exchange. The group
  texture, the settings and the nation list stay on every record.

## Open Questions

### The Settings and Nation Values

The window reads `ToClient_GetPalaceManageFreeRerollCount()`,
`ToClient_PalaceManageGetNeedPearlCountForReroll()`,
`Toclient_getPalaceManageRegionKeyRaw()`,
`Toclient_getPalaceManageRegionWaypointKey()` and
`Toclient_getPalaceManageWorkerRegionWaypointKey()` with no argument,
which may read the six u16 after the boards: `1420` and `1419` are both
node keys of Magoria. The nation values (`50` for NA and CS, `25` for RU,
`12` for TR, `10` elsewhere) fit a Pearl price per service region for the
reroll, but no source ties them to it.

### The Board Flag

`unknown_02` is `1` on the first board each group lists. The window asks
`ToClient_PalaceManageGetBoardIsOpen(boardGroupKey, index)`, which may
start from it.
