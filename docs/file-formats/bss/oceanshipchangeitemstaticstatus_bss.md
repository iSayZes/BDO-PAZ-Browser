# `oceanshipchangeitemstaticstatus.bss` Format

## Purpose

The ships a wharf can turn back into their Ship License item, and the
silver fee for it. On client 3482 the five rows are the Epheria Carrack
and its four upgraded forms, each with its own license. The servant list
offers the change only for a ship of `CppEnums.VehicleType.Type_Carrack`
that `ToClient_oceanShipChangeItemPossible(characterKey)` accepts
(`panel_dialog_servantlist_all_1.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------------------- | ----- | ------- | --------- |
| 1      | 2703 and later | `oceanshipchangeitemstaticstatus.bss` | 54    | 5 Row   | 6         |

| Layout | File                                  | Known         | Unknown    |
| ------ | ------------------------------------- | ------------- | ---------- |
| 1      | `oceanshipchangeitemstaticstatus.bss` | 54 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e57effe9a26b`  |
| 3482   | Layout 1 | `e57effe9a26b`  |
| 3474   | Layout 1 | `e57effe9a26b`  |
| 3473   | Layout 1 | `e57effe9a26b`  |
| 3464   | Layout 1 | `e57effe9a26b`  |
| 3458   | Layout 1 | `e57effe9a26b`  |
| 3454   | Layout 1 | `e57effe9a26b`  |
| 3444   | Layout 1 | `e57effe9a26b`  |
| 3435   | Layout 1 | `e57effe9a26b`  |
| 3426   | Layout 1 | `e57effe9a26b`  |
| 3418   | Layout 1 | `e57effe9a26b`  |
| 3412   | Layout 1 | `e57effe9a26b`  |
| 3402   | Layout 1 | `e57effe9a26b`  |
| 3396   | Layout 1 | `e57effe9a26b`  |
| 3387   | Layout 1 | `e57effe9a26b`  |
| 3381   | Layout 1 | `e57effe9a26b`  |
| 3373   | Layout 1 | `e57effe9a26b`  |
| 3364   | Layout 1 | `e57effe9a26b`  |
| 3356   | Layout 1 | `e57effe9a26b`  |
| 3349   | Layout 1 | `e57effe9a26b`  |
| 3342   | Layout 1 | `e57effe9a26b`  |
| 3335   | Layout 1 | `e57effe9a26b`  |
| 3326   | Layout 1 | `e57effe9a26b`  |
| 3321   | Layout 1 | `e57effe9a26b`  |
| 3314   | Layout 1 | `e57effe9a26b`  |
| 3303   | Layout 1 | `e57effe9a26b`  |
| 3302   | Layout 1 | `e57effe9a26b`  |
| 3293   | Layout 1 | `e57effe9a26b`  |
| 3283   | Layout 1 | `e57effe9a26b`  |
| 3275   | Layout 1 | `e57effe9a26b`  |
| 3267   | Layout 1 | `e57effe9a26b`  |
| 3258   | Layout 1 | `e57effe9a26b`  |
| 3251   | Layout 1 | `e57effe9a26b`  |
| 3242   | Layout 1 | `e57effe9a26b`  |
| 3235   | Layout 1 | `e57effe9a26b`  |
| 3229   | Layout 1 | `e57effe9a26b`  |
| 3212   | Layout 1 | `e57effe9a26b`  |
| 3203   | Layout 1 | `e57effe9a26b`  |
| 3193   | Layout 1 | `e57effe9a26b`  |
| 3186   | Layout 1 | `e57effe9a26b`  |
| 3177   | Layout 1 | `e57effe9a26b`  |
| 3169   | Layout 1 | `e57effe9a26b`  |
| 3158   | Layout 1 | `e57effe9a26b`  |
| 3151   | Layout 1 | `e57effe9a26b`  |
| 3144   | Layout 1 | `e57effe9a26b`  |
| 3133   | Layout 1 | `e57effe9a26b`  |
| 3125   | Layout 1 | `e57effe9a26b`  |
| 3118   | Layout 1 | `e57effe9a26b`  |
| 3111   | Layout 1 | `e57effe9a26b`  |
| 3103   | Layout 1 | `e57effe9a26b`  |
| 3095   | Layout 1 | `e57effe9a26b`  |
| 3086   | Layout 1 | `e57effe9a26b`  |
| 3072   | Layout 1 | `e57effe9a26b`  |
| 3062   | Layout 1 | `e57effe9a26b`  |
| 3052   | Layout 1 | `e57effe9a26b`  |
| 3045   | Layout 1 | `e57effe9a26b`  |
| 3037   | Layout 1 | `e57effe9a26b`  |
| 3030   | Layout 1 | `e57effe9a26b`  |
| 3021   | Layout 1 | `e57effe9a26b`  |
| 3012   | Layout 1 | `e57effe9a26b`  |
| 3002   | Layout 1 | `e57effe9a26b`  |
| 2995   | Layout 1 | `e57effe9a26b`  |
| 2987   | Layout 1 | `e57effe9a26b`  |
| 2978   | Layout 1 | `e57effe9a26b`  |
| 2970   | Layout 1 | `e57effe9a26b`  |
| 2959   | Layout 1 | `e57effe9a26b`  |
| 2951   | Layout 1 | `e57effe9a26b`  |
| 2942   | Layout 1 | `e57effe9a26b`  |
| 2935   | Layout 1 | `e57effe9a26b`  |
| 2932   | Layout 1 | `e57effe9a26b`  |
| 2923   | Layout 1 | `e57effe9a26b`  |
| 2919   | Layout 1 | `e57effe9a26b`  |
| 2907   | Layout 1 | `e57effe9a26b`  |
| 2900   | Layout 1 | `e57effe9a26b`  |
| 2891   | Layout 1 | `e57effe9a26b`  |
| 2882   | Layout 1 | `e57effe9a26b`  |
| 2872   | Layout 1 | `e57effe9a26b`  |
| 2863   | Layout 1 | `e57effe9a26b`  |
| 2855   | Layout 1 | `e57effe9a26b`  |
| 2849   | Layout 1 | `e57effe9a26b`  |
| 2844   | Layout 1 | `e57effe9a26b`  |
| 2834   | Layout 1 | `e57effe9a26b`  |
| 2825   | Layout 1 | `e57effe9a26b`  |
| 2819   | Layout 1 | `e57effe9a26b`  |
| 2811   | Layout 1 | `e57effe9a26b`  |
| 2803   | Layout 1 | `e57effe9a26b`  |
| 2794   | Layout 1 | `e57effe9a26b`  |
| 2783   | Layout 1 | `e57effe9a26b`  |
| 2774   | Layout 1 | `e57effe9a26b`  |
| 2765   | Layout 1 | `e57effe9a26b`  |
| 2756   | Layout 1 | `e57effe9a26b`  |
| 2750   | Layout 1 | `e57effe9a26b`  |
| 2743   | Layout 1 | `e57effe9a26b`  |
| 2736   | Layout 1 | `e57effe9a26b`  |
| 2726   | Layout 1 | `e57effe9a26b`  |
| 2717   | Layout 1 | `e57effe9a26b`  |
| 2709   | Layout 1 | `e57effe9a26b`  |
| 2703   | Layout 1 | `e57effe9a26b`  |
| 2695   | No file  | `e57effe9a26b`  |
| 2684   | No file  | `e57effe9a26b`  |
| 2672   | No file  | `e57effe9a26b`  |
| 2665   | No file  | `e57effe9a26b`  |
| 2657   | No file  | `e57effe9a26b`  |
| 2649   | No file  | `e57effe9a26b`  |
| 2644   | No file  | `e57effe9a26b`  |
| 2637   | No file  | `e57effe9a26b`  |
| 2629   | No file  | `e57effe9a26b`  |
| 2619   | No file  | `e57effe9a26b`  |
| 2612   | No file  | `e57effe9a26b`  |
| 2606   | No file  | `e57effe9a26b`  |
| 2602   | No file  | `e57effe9a26b`  |
| 2601   | No file  | `e57effe9a26b`  |
| 2592   | No file  | `e57effe9a26b`  |
| 2583   | No file  | `e57effe9a26b`  |
| 2575   | No file  | `e57effe9a26b`  |
| 2567   | No file  | `e57effe9a26b`  |
| 2560   | No file  | `e57effe9a26b`  |
| 2553   | No file  | `e57effe9a26b`  |
| 2545   | No file  | `e57effe9a26b`  |
| 2538   | No file  | `e57effe9a26b`  |
| 2529   | No file  | `e57effe9a26b`  |
| 2519   | No file  | `e57effe9a26b`  |
| 2513   | No file  | `e57effe9a26b`  |
| 2510   | No file  | `e57effe9a26b`  |
| 2507   | No file  | `e57effe9a26b`  |
| 2503   | No file  | `e57effe9a26b`  |
| 2498   | No file  | `e57effe9a26b`  |
| 2492   | No file  | `e57effe9a26b`  |
| 2487   | No file  | `e57effe9a26b`  |
| 2480   | No file  | `e57effe9a26b`  |
| 2474   | No file  | `e57effe9a26b`  |
| 2468   | No file  | `e57effe9a26b`  |
| 2460   | No file  | `e57effe9a26b`  |
| 2453   | No file  | `e57effe9a26b`  |
| 2444   | No file  | `e57effe9a26b`  |
| 2438   | No file  | `e57effe9a26b`  |
| 2434   | No file  | `e57effe9a26b`  |
| 2429   | No file  | `e57effe9a26b`  |
| 2421   | No file  | `e57effe9a26b`  |
| 2414   | No file  | `e57effe9a26b`  |
| 2407   | No file  | `e57effe9a26b`  |
| 2401   | No file  | `e57effe9a26b`  |
| 2397   | No file  | `e57effe9a26b`  |
| 2393   | No file  | `e57effe9a26b`  |
| 2384   | No file  | `e57effe9a26b`  |
| 2378   | No file  | `e57effe9a26b`  |
| 2372   | No file  | `e57effe9a26b`  |
| 2358   | No file  | `e57effe9a26b`  |
| 2352   | No file  | `e57effe9a26b`  |
| 2347   | No file  | `e57effe9a26b`  |
| 2343   | No file  | `e57effe9a26b`  |
| 2335   | No file  | `e57effe9a26b`  |
| 2327   | No file  | `e57effe9a26b`  |
| 2324   | No file  | `e57effe9a26b`  |
| 2319   | No file  | `e57effe9a26b`  |
| 2313   | No file  | `e57effe9a26b`  |
| 2308   | No file  | `e57effe9a26b`  |
| 2302   | No file  | `e57effe9a26b`  |
| 2295   | No file  | `e57effe9a26b`  |
| 2290   | No file  | `e57effe9a26b`  |
| 2284   | No file  | `e57effe9a26b`  |
| 2276   | No file  | `e57effe9a26b`  |
| 2269   | No file  | `e57effe9a26b`  |
| 2259   | No file  | `e57effe9a26b`  |
| 2250   | No file  | `e57effe9a26b`  |
| 2243   | No file  | `e57effe9a26b`  |
| 2235   | No file  | `e57effe9a26b`  |
| 2229   | No file  | `e57effe9a26b`  |
| 2224   | No file  | `e57effe9a26b`  |
| 2218   | No file  | `e57effe9a26b`  |
| 2215   | No file  | `e57effe9a26b`  |
| 2207   | No file  | `e57effe9a26b`  |
| 2203   | No file  | `e57effe9a26b`  |
| 2196   | No file  | `e57effe9a26b`  |
| 2192   | No file  | `e57effe9a26b`  |
| 2189   | No file  | `e57effe9a26b`  |
| 2183   | No file  | `e57effe9a26b`  |
| 2179   | No file  | `e57effe9a26b`  |
| 2171   | No file  | `e57effe9a26b`  |
| 2163   | No file  | `e57effe9a26b`  |
| 2156   | No file  | `e57effe9a26b`  |
| 2151   | No file  | `e57effe9a26b`  |
| 2147   | No file  | `e57effe9a26b`  |
| 2142   | No file  | `e57effe9a26b`  |
| 2138   | No file  | `e57effe9a26b`  |
| 2134   | No file  | `e57effe9a26b`  |
| 2130   | No file  | `e57effe9a26b`  |
| 2122   | No file  | `e57effe9a26b`  |
| 2107   | No file  | `e57effe9a26b`  |
| 2098   | No file  | `e57effe9a26b`  |
| 2089   | No file  | `e57effe9a26b`  |
| 2081   | No file  | `e57effe9a26b`  |
| 2073   | No file  | `e57effe9a26b`  |
| 2067   | No file  | `e57effe9a26b`  |
| 2063   | No file  | `e57effe9a26b`  |
| 2059   | No file  | `e57effe9a26b`  |
| 2052   | No file  | `e57effe9a26b`  |
| 2044   | No file  | `e57effe9a26b`  |
| 2039   | No file  | `e57effe9a26b`  |
| 2032   | No file  | `e57effe9a26b`  |
| 2025   | No file  | `e57effe9a26b`  |
| 2011   | No file  | `e57effe9a26b`  |
| 2005   | No file  | `e57effe9a26b`  |
| 2000   | No file  | `e57effe9a26b`  |
| 1996   | No file  | `e57effe9a26b`  |
| 1991   | No file  | `e57effe9a26b`  |
| 1985   | No file  | `e57effe9a26b`  |
| 1980   | No file  | `e57effe9a26b`  |
| 1969   | No file  | `e57effe9a26b`  |
| 1964   | No file  | `e57effe9a26b`  |
| 1958   | No file  | `e57effe9a26b`  |
| 1950   | No file  | `e57effe9a26b`  |
| 1945   | No file  | `e57effe9a26b`  |
| 1937   | No file  | `e57effe9a26b`  |
| 1933   | No file  | `e57effe9a26b`  |
| 1927   | No file  | `e57effe9a26b`  |
| 1921   | No file  | `e57effe9a26b`  |
| 1914   | No file  | `e57effe9a26b`  |
| 1908   | No file  | `e57effe9a26b`  |
| 1897   | No file  | `e57effe9a26b`  |
| 1892   | No file  | `e57effe9a26b`  |
| 1886   | No file  | `e57effe9a26b`  |
| 1881   | No file  | `e57effe9a26b`  |
| 1871   | No file  | `e57effe9a26b`  |
| 1866   | No file  | `e57effe9a26b`  |
| 1862   | No file  | `e57effe9a26b`  |
| 1854   | No file  | `e57effe9a26b`  |
| 1846   | No file  | `e57effe9a26b`  |
| 1838   | No file  | `e57effe9a26b`  |
| 1832   | No file  | `e57effe9a26b`  |
| 1826   | No file  | `e57effe9a26b`  |
| 1822   | No file  | `e57effe9a26b`  |
| 1818   | No file  | `e57effe9a26b`  |
| 1804   | No file  | `e57effe9a26b`  |
| 1794   | No file  | `e57effe9a26b`  |
| 1790   | No file  | `e57effe9a26b`  |
| 1784   | No file  | `e57effe9a26b`  |
| 1774   | No file  | `e57effe9a26b`  |
| 1771   | No file  | `e57effe9a26b`  |
| 1762   | No file  | `e57effe9a26b`  |
| 1759   | No file  | `e57effe9a26b`  |
| 1754   | No file  | `e57effe9a26b`  |
| 1749   | No file  | `e57effe9a26b`  |
| 1743   | No file  | `e57effe9a26b`  |
| 1737   | No file  | `e57effe9a26b`  |
| 1731   | No file  | `e57effe9a26b`  |
| 1725   | No file  | `e57effe9a26b`  |
| 1717   | No file  | `e57effe9a26b`  |
| 1710   | No file  | `e57effe9a26b`  |
| 1704   | No file  | `e57effe9a26b`  |
| 1698   | No file  | `e57effe9a26b`  |
| 1690   | No file  | `e57effe9a26b`  |
| 1685   | No file  | `e57effe9a26b`  |
| 1680   | No file  | `e57effe9a26b`  |
| 1674   | No file  | `e57effe9a26b`  |
| 1668   | No file  | `e57effe9a26b`  |
| 1659   | No file  | `e57effe9a26b`  |
| 1649   | No file  | `e57effe9a26b`  |
| 1642   | No file  | `e57effe9a26b`  |
| 1636   | No file  | `e57effe9a26b`  |
| 1628   | No file  | `e57effe9a26b`  |
| 1622   | No file  | `e57effe9a26b`  |
| 1614   | No file  | `e57effe9a26b`  |
| 1608   | No file  | `e57effe9a26b`  |
| 1602   | No file  | `e57effe9a26b`  |
| 1598   | No file  | `e57effe9a26b`  |
| 1594   | No file  | `e57effe9a26b`  |
| 1590   | No file  | `e57effe9a26b`  |
| 1587   | No file  | `e57effe9a26b`  |
| 1584   | No file  | `e57effe9a26b`  |
| 1579   | No file  | `e57effe9a26b`  |
| 1572   | No file  | `e57effe9a26b`  |
| 1565   | No file  | `e57effe9a26b`  |
| 1559   | No file  | `e57effe9a26b`  |
| 1554   | No file  | `e57effe9a26b`  |
| 1547   | No file  | `e57effe9a26b`  |
| 1537   | No file  | `e57effe9a26b`  |
| 1529   | No file  | `e57effe9a26b`  |
| 1524   | No file  | `e57effe9a26b`  |
| 1519   | No file  | `e57effe9a26b`  |
| 1509   | No file  | `e57effe9a26b`  |
| 1506   | No file  | `e57effe9a26b`  |
| 1504   | No file  | `e57effe9a26b`  |
| 1500   | No file  | `e57effe9a26b`  |
| 1493   | No file  | `e57effe9a26b`  |
| 1489   | No file  | `e57effe9a26b`  |
| 1485   | No file  | `e57effe9a26b`  |
| 1481   | No file  | `e57effe9a26b`  |
| 1474   | No file  | `e57effe9a26b`  |
| 1466   | No file  | `e57effe9a26b`  |
| 1462   | No file  | `e57effe9a26b`  |
| 1459   | No file  | `e57effe9a26b`  |
| 1453   | No file  | `e57effe9a26b`  |
| 1450   | No file  | `e57effe9a26b`  |
| 1445   | No file  | `e57effe9a26b`  |
| 1439   | No file  | `e57effe9a26b`  |
| 1433   | No file  | `e57effe9a26b`  |
| 1430   | No file  | `e57effe9a26b`  |
| 1426   | No file  | `e57effe9a26b`  |
| 1421   | No file  | `e57effe9a26b`  |
| 1417   | No file  | `e57effe9a26b`  |
| 1416   | No file  | `e57effe9a26b`  |
| 1409   | No file  | `e57effe9a26b`  |
| 1405   | No file  | `e57effe9a26b`  |
| 1401   | No file  | `e57effe9a26b`  |
| 1396   | No file  | `e57effe9a26b`  |
| 1391   | No file  | `e57effe9a26b`  |
| 1390   | No file  | `e57effe9a26b`  |
| 1386   | No file  | `e57effe9a26b`  |
| 1381   | No file  | `e57effe9a26b`  |
| 1379   | No file  | `e57effe9a26b`  |
| 1372   | No file  | `e57effe9a26b`  |
| 1366   | No file  | `e57effe9a26b`  |
| 1364   | No file  | `e57effe9a26b`  |
| 1363   | No file  | `e57effe9a26b`  |
| 1360   | No file  | `e57effe9a26b`  |
| 1358   | No file  | `e57effe9a26b`  |
| 1355   | No file  | `e57effe9a26b`  |
| 1351   | No file  | `e57effe9a26b`  |
| 1348   | No file  | `e57effe9a26b`  |
| 1346   | No file  | `e57effe9a26b`  |
| 1341   | No file  | `e57effe9a26b`  |
| 1340   | No file  | `e57effe9a26b`  |
| 1338   | No file  | `e57effe9a26b`  |
| 1335   | No file  | `e57effe9a26b`  |
| 1333   | No file  | `e57effe9a26b`  |
| 1329   | No file  | `e57effe9a26b`  |
| 1327   | No file  | `e57effe9a26b`  |
| 1324   | No file  | `e57effe9a26b`  |
| 1321   | No file  | `e57effe9a26b`  |
| 1319   | No file  | `e57effe9a26b`  |
| 1318   | No file  | `e57effe9a26b`  |
| 1316   | No file  | `e57effe9a26b`  |
| 1313   | No file  | `e57effe9a26b`  |
| 1311   | No file  | `e57effe9a26b`  |
| 1309   | No file  | `e57effe9a26b`  |
| 1304   | No file  | `e57effe9a26b`  |
| 1292   | No file  | `e57effe9a26b`  |
| 1286   | No file  | `e57effe9a26b`  |
| 1280   | No file  | `e57effe9a26b`  |
| 1276   | No file  | `e57effe9a26b`  |
| 1267   | No file  | `e57effe9a26b`  |
| 1261   | No file  | `e57effe9a26b`  |
| 1256   | No file  | `e57effe9a26b`  |
| 1250   | No file  | `e57effe9a26b`  |
| 1246   | No file  | `e57effe9a26b`  |
| 1239   | No file  | `e57effe9a26b`  |
| 1230   | No file  | `e57effe9a26b`  |
| 1226   | No file  | `e57effe9a26b`  |
| 1220   | No file  | `e57effe9a26b`  |
| 1217   | No file  | `e57effe9a26b`  |
| 1211   | No file  | `e57effe9a26b`  |
| 1210   | No file  | `e57effe9a26b`  |
| 1208   | No file  | `e57effe9a26b`  |
| 1203   | No file  | `e57effe9a26b`  |
| 1197   | No file  | `e57effe9a26b`  |
| 1194   | No file  | `e57effe9a26b`  |
| 1192   | No file  | `e57effe9a26b`  |
| 1187   | No file  | `e57effe9a26b`  |
| 1183   | No file  | `e57effe9a26b`  |
| 1177   | No file  | `e57effe9a26b`  |
| 1173   | No file  | `e57effe9a26b`  |
| 1167   | No file  | `e57effe9a26b`  |
| 1164   | No file  | `e57effe9a26b`  |
| 1156   | No file  | `e57effe9a26b`  |
| 1149   | No file  | `e57effe9a26b`  |
| 1144   | No file  | `e57effe9a26b`  |
| 1137   | No file  | `e57effe9a26b`  |
| 1132   | No file  | `e57effe9a26b`  |
| 1127   | No file  | `e57effe9a26b`  |
| 1122   | No file  | `e57effe9a26b`  |
| 1118   | No file  | `e57effe9a26b`  |
| 1114   | No file  | `e57effe9a26b`  |
| 1109   | No file  | `e57effe9a26b`  |
| 1102   | No file  | `e57effe9a26b`  |
| 1096   | No file  | `e57effe9a26b`  |
| 1088   | No file  | `e57effe9a26b`  |
| 1081   | No file  | `e57effe9a26b`  |
| 1076   | No file  | `e57effe9a26b`  |
| 1069   | No file  | `e57effe9a26b`  |
| 1064   | No file  | `e57effe9a26b`  |
| 1058   | No file  | `e57effe9a26b`  |
| 1051   | No file  | `e57effe9a26b`  |
| 1044   | No file  | `e57effe9a26b`  |
| 1036   | No file  | `e57effe9a26b`  |
| 1026   | No file  | `e57effe9a26b`  |
| 1016   | No file  | `e57effe9a26b`  |
| 1009   | No file  | `e57effe9a26b`  |
| 1005   | No file  | `e57effe9a26b`  |
| 1000   | No file  | `e57effe9a26b`  |
| 998    | No file  | `e57effe9a26b`  |
| 990    | No file  | `e57effe9a26b`  |
| 979    | No file  | `e57effe9a26b`  |
| 972    | No file  | `e57effe9a26b`  |
| 963    | No file  | `e57effe9a26b`  |
| 955    | No file  | `e57effe9a26b`  |
| 946    | No file  | `e57effe9a26b`  |
| 938    | No file  | `e57effe9a26b`  |
| 927    | No file  | `e57effe9a26b`  |
| 911    | No file  | `e57effe9a26b`  |
| 904    | No file  | `e57effe9a26b`  |
| 899    | No file  | `e57effe9a26b`  |
| 894    | No file  | `e57effe9a26b`  |
| 885    | No file  | `e57effe9a26b`  |
| 879    | No file  | `e57effe9a26b`  |
| 872    | No file  | `e57effe9a26b`  |
| 864    | No file  | `e57effe9a26b`  |
| 855    | No file  | `e57effe9a26b`  |
| 853    | No file  | `e57effe9a26b`  |
| 845    | No file  | `e57effe9a26b`  |
| 837    | No file  | `e57effe9a26b`  |
| 829    | No file  | `e57effe9a26b`  |
| 822    | No file  | `e57effe9a26b`  |
| 814    | No file  | `e57effe9a26b`  |
| 805    | No file  | `e57effe9a26b`  |
| 794    | No file  | `e57effe9a26b`  |
| 787    | No file  | `e57effe9a26b`  |
| 780    | No file  | `e57effe9a26b`  |
| 771    | No file  | `e57effe9a26b`  |
| 760    | No file  | `e57effe9a26b`  |
| 748    | No file  | `e57effe9a26b`  |
| 741    | No file  | `e57effe9a26b`  |
| 736    | No file  | `e57effe9a26b`  |
| 731    | No file  | `e57effe9a26b`  |
| 723    | No file  | `e57effe9a26b`  |
| 711    | No file  | `e57effe9a26b`  |
| 707    | No file  | `e57effe9a26b`  |
| 697    | No file  | `e57effe9a26b`  |
| 689    | No file  | `e57effe9a26b`  |
| 683    | No file  | `e57effe9a26b`  |
| 678    | No file  | `e57effe9a26b`  |
| 670    | No file  | `e57effe9a26b`  |
| 661    | No file  | `e57effe9a26b`  |
| 656    | No file  | `e57effe9a26b`  |
| 652    | No file  | `e57effe9a26b`  |
| 643    | No file  | `e57effe9a26b`  |
| 637    | No file  | `e57effe9a26b`  |
| 630    | No file  | `e57effe9a26b`  |
| 627    | No file  | `e57effe9a26b`  |
| 621    | No file  | `e57effe9a26b`  |
| 617    | No file  | `e57effe9a26b`  |
| 615    | No file  | `e57effe9a26b`  |
| 606    | No file  | `e57effe9a26b`  |
| 599    | No file  | `e57effe9a26b`  |
| 592    | No file  | `e57effe9a26b`  |
| 586    | No file  | `e57effe9a26b`  |
| 577    | No file  | `e57effe9a26b`  |
| 569    | No file  | `e57effe9a26b`  |
| 561    | No file  | `e57effe9a26b`  |
| 554    | No file  | `e57effe9a26b`  |
| 542    | No file  | `e57effe9a26b`  |
| 532    | No file  | `e57effe9a26b`  |
| 531    | No file  | `e57effe9a26b`  |
| 526    | No file  | `e57effe9a26b`  |
| 521    | No file  | `e57effe9a26b`  |
| 517    | No file  | `e57effe9a26b`  |
| 510    | No file  | `e57effe9a26b`  |
| 508    | No file  | `e57effe9a26b`  |
| 504    | No file  | `e57effe9a26b`  |
| 497    | No file  | `e57effe9a26b`  |
| 491    | No file  | `e57effe9a26b`  |
| 485    | No file  | `e57effe9a26b`  |
| 478    | No file  | `e57effe9a26b`  |
| 472    | No file  | `e57effe9a26b`  |
| 466    | No file  | `e57effe9a26b`  |
| 457    | No file  | `e57effe9a26b`  |
| 452    | No file  | `e57effe9a26b`  |
| 449    | No file  | `e57effe9a26b`  |
| 435    | No file  | `e57effe9a26b`  |

<!-- versions:end -->

## Companion Files

None. The handler names the ship (LOC type 6) and the item (LOC type 0)
from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                                                 |
| ------------------- | -------------- | ------------ | --------------------------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                                          |
| `+0x04`             | u32            | fee_money    | Silver fee of the change; `100000000` on client 3482                  |
| `+0x08`             | u32            | row_count    | Number of rows                                                        |
| `+0x0C`             | Row[row_count] | rows         | See Row; byte-packed                                                  |
| `rows+0x00`         | String Table   | string_table | See String Table                                                      |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends                         |
| `string_table+0x04` | u32            | zero         | Always `0`                                                            |

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                                  |
| ------- | ---- | ------------- | ---------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | The ship's character key (LOC type 6); unique per row                  |
| `+0x02` | u32  | item_id       | The Ship License the ship turns into (LOC type 0); unique per row      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Rows

Client 3482, in file order.

| `character_key` | Ship                     | `item_id` | Item                                    |
| --------------- | ------------------------ | --------- | --------------------------------------- |
| 31045           | Epheria Carrack          | 49021     | Ship License: Epheria Carrack           |
| 31054           | Epheria Carrack: Advance | 49029     | Ship License: Epheria Carrack - Advance |
| 31055           | Epheria Carrack: Balance | 49030     | Ship License: Epheria Carrack - Balance |
| 31056           | Epheria Carrack: Volante | 49031     | Ship License: Epheria Carrack - Volante |
| 31057           | Epheria Carrack: Valor   | 49032     | Ship License: Epheria Carrack - Valor   |

## Field Names

The file is newer than client 1784, and no sheet or column name of a
private server's `DataSheets.bexcel` on that client contains
`ShipChange`. The names come from the client Lua
(`panel_dialog_servantlist_all_2.luac`, client 3482): the confirm box
shows `makeDotMoney(ToClient_oceanShipChangeItemFeeMoney())` as the
`needSilver` of `LUA_OCEAN_SHIP_TRADE_ITEM_02`, so the value stored once
before the rows is `fee_money`. `character_key` resolves to the ship's
LOC type 6 name and `item_id` to the matching Ship License on every row.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/greatsea_tables.py`: the
  ship and its license with names and icon, and the fee on every row.
