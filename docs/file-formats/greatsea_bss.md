# `greatsea.bss` Format

## Purpose

The areas of the Great Ocean map: one row per colour of
`ui_texture/minimap/area/greatseamap.bmp`, with three f32 values, a
magnification, a list of vehicle types, a restricted area state and a
wind impact value. On client 3482 two rows list vehicle types, the same
five ship types of `CppEnums.VehicleType` from `Type_Carrack` to
`Type_SailingBoat`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File           | Bytes | Records | Row bytes               |
| ------ | -------------- | -------------- | ----- | ------- | ----------------------- |
| 1      | 1239 and later | `greatsea.bss` | 5,173 | 139 Row | 37 to 42, 37 on average |

| Layout | File           | Known           | Unknown       |
| ------ | -------------- | --------------- | ------------- |
| 1      | `greatsea.bss` | 4,478 B (86.6%) | 695 B (13.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c2a963bd2d3e`  |
| 3482   | Layout 1 | `c2a963bd2d3e`  |
| 3474   | Layout 1 | `c2a963bd2d3e`  |
| 3473   | Layout 1 | `c2a963bd2d3e`  |
| 3464   | Layout 1 | `c2a963bd2d3e`  |
| 3458   | Layout 1 | `c2a963bd2d3e`  |
| 3454   | Layout 1 | `c2a963bd2d3e`  |
| 3444   | Layout 1 | `c2a963bd2d3e`  |
| 3435   | Layout 1 | `c2a963bd2d3e`  |
| 3426   | Layout 1 | `c2a963bd2d3e`  |
| 3418   | Layout 1 | `c2a963bd2d3e`  |
| 3412   | Layout 1 | `c2a963bd2d3e`  |
| 3402   | Layout 1 | `c2a963bd2d3e`  |
| 3396   | Layout 1 | `c2a963bd2d3e`  |
| 3387   | Layout 1 | `c2a963bd2d3e`  |
| 3381   | Layout 1 | `c2a963bd2d3e`  |
| 3373   | Layout 1 | `c2a963bd2d3e`  |
| 3364   | Layout 1 | `c2a963bd2d3e`  |
| 3356   | Layout 1 | `c2a963bd2d3e`  |
| 3349   | Layout 1 | `c2a963bd2d3e`  |
| 3342   | Layout 1 | `c2a963bd2d3e`  |
| 3335   | Layout 1 | `c2a963bd2d3e`  |
| 3326   | Layout 1 | `c2a963bd2d3e`  |
| 3321   | Layout 1 | `c2a963bd2d3e`  |
| 3314   | Layout 1 | `c2a963bd2d3e`  |
| 3303   | Layout 1 | `c2a963bd2d3e`  |
| 3302   | Layout 1 | `c2a963bd2d3e`  |
| 3293   | Layout 1 | `c2a963bd2d3e`  |
| 3283   | Layout 1 | `c2a963bd2d3e`  |
| 3275   | Layout 1 | `c2a963bd2d3e`  |
| 3267   | Layout 1 | `c2a963bd2d3e`  |
| 3258   | Layout 1 | `c2a963bd2d3e`  |
| 3251   | Layout 1 | `c2a963bd2d3e`  |
| 3242   | Layout 1 | `c2a963bd2d3e`  |
| 3235   | Layout 1 | `c2a963bd2d3e`  |
| 3229   | Layout 1 | `c2a963bd2d3e`  |
| 3212   | Layout 1 | `c2a963bd2d3e`  |
| 3203   | Layout 1 | `c2a963bd2d3e`  |
| 3193   | Layout 1 | `c2a963bd2d3e`  |
| 3186   | Layout 1 | `c2a963bd2d3e`  |
| 3177   | Layout 1 | `c2a963bd2d3e`  |
| 3169   | Layout 1 | `c2a963bd2d3e`  |
| 3158   | Layout 1 | `c2a963bd2d3e`  |
| 3151   | Layout 1 | `c2a963bd2d3e`  |
| 3144   | Layout 1 | `c2a963bd2d3e`  |
| 3133   | Layout 1 | `c2a963bd2d3e`  |
| 3125   | Layout 1 | `c2a963bd2d3e`  |
| 3118   | Layout 1 | `c2a963bd2d3e`  |
| 3111   | Layout 1 | `c2a963bd2d3e`  |
| 3103   | Layout 1 | `c2a963bd2d3e`  |
| 3095   | Layout 1 | `c2a963bd2d3e`  |
| 3086   | Layout 1 | `c2a963bd2d3e`  |
| 3072   | Layout 1 | `c2a963bd2d3e`  |
| 3062   | Layout 1 | `c2a963bd2d3e`  |
| 3052   | Layout 1 | `c2a963bd2d3e`  |
| 3045   | Layout 1 | `c2a963bd2d3e`  |
| 3037   | Layout 1 | `c2a963bd2d3e`  |
| 3030   | Layout 1 | `c2a963bd2d3e`  |
| 3021   | Layout 1 | `c2a963bd2d3e`  |
| 3012   | Layout 1 | `c2a963bd2d3e`  |
| 3002   | Layout 1 | `c2a963bd2d3e`  |
| 2995   | Layout 1 | `c2a963bd2d3e`  |
| 2987   | Layout 1 | `c2a963bd2d3e`  |
| 2978   | Layout 1 | `c2a963bd2d3e`  |
| 2970   | Layout 1 | `c2a963bd2d3e`  |
| 2959   | Layout 1 | `c2a963bd2d3e`  |
| 2951   | Layout 1 | `c2a963bd2d3e`  |
| 2942   | Layout 1 | `c2a963bd2d3e`  |
| 2935   | Layout 1 | `c2a963bd2d3e`  |
| 2932   | Layout 1 | `c2a963bd2d3e`  |
| 2923   | Layout 1 | `c2a963bd2d3e`  |
| 2919   | Layout 1 | `c2a963bd2d3e`  |
| 2907   | Layout 1 | `c2a963bd2d3e`  |
| 2900   | Layout 1 | `c2a963bd2d3e`  |
| 2891   | Layout 1 | `c2a963bd2d3e`  |
| 2882   | Layout 1 | `c2a963bd2d3e`  |
| 2872   | Layout 1 | `c2a963bd2d3e`  |
| 2863   | Layout 1 | `c2a963bd2d3e`  |
| 2855   | Layout 1 | `c2a963bd2d3e`  |
| 2849   | Layout 1 | `c2a963bd2d3e`  |
| 2844   | Layout 1 | `c2a963bd2d3e`  |
| 2834   | Layout 1 | `c2a963bd2d3e`  |
| 2825   | Layout 1 | `c2a963bd2d3e`  |
| 2819   | Layout 1 | `c2a963bd2d3e`  |
| 2811   | Layout 1 | `c2a963bd2d3e`  |
| 2803   | Layout 1 | `c2a963bd2d3e`  |
| 2794   | Layout 1 | `c2a963bd2d3e`  |
| 2783   | Layout 1 | `c2a963bd2d3e`  |
| 2774   | Layout 1 | `c2a963bd2d3e`  |
| 2765   | Layout 1 | `c2a963bd2d3e`  |
| 2756   | Layout 1 | `c2a963bd2d3e`  |
| 2750   | Layout 1 | `c2a963bd2d3e`  |
| 2743   | Layout 1 | `c2a963bd2d3e`  |
| 2736   | Layout 1 | `c2a963bd2d3e`  |
| 2726   | Layout 1 | `c2a963bd2d3e`  |
| 2717   | Layout 1 | `c2a963bd2d3e`  |
| 2709   | Layout 1 | `c2a963bd2d3e`  |
| 2703   | Layout 1 | `c2a963bd2d3e`  |
| 2695   | Layout 1 | `c2a963bd2d3e`  |
| 2684   | Layout 1 | `c2a963bd2d3e`  |
| 2672   | Layout 1 | `c2a963bd2d3e`  |
| 2665   | Layout 1 | `c2a963bd2d3e`  |
| 2657   | Layout 1 | `c2a963bd2d3e`  |
| 2649   | Layout 1 | `c2a963bd2d3e`  |
| 2644   | Layout 1 | `c2a963bd2d3e`  |
| 2637   | Layout 1 | `c2a963bd2d3e`  |
| 2629   | Layout 1 | `c2a963bd2d3e`  |
| 2619   | Layout 1 | `c2a963bd2d3e`  |
| 2612   | Layout 1 | `c2a963bd2d3e`  |
| 2606   | Layout 1 | `c2a963bd2d3e`  |
| 2602   | Layout 1 | `c2a963bd2d3e`  |
| 2601   | Layout 1 | `c2a963bd2d3e`  |
| 2592   | Layout 1 | `c2a963bd2d3e`  |
| 2583   | Layout 1 | `c2a963bd2d3e`  |
| 2575   | Layout 1 | `c2a963bd2d3e`  |
| 2567   | Layout 1 | `c2a963bd2d3e`  |
| 2560   | Layout 1 | `c2a963bd2d3e`  |
| 2553   | Layout 1 | `c2a963bd2d3e`  |
| 2545   | Layout 1 | `c2a963bd2d3e`  |
| 2538   | Layout 1 | `c2a963bd2d3e`  |
| 2529   | Layout 1 | `c2a963bd2d3e`  |
| 2519   | Layout 1 | `c2a963bd2d3e`  |
| 2513   | Layout 1 | `c2a963bd2d3e`  |
| 2510   | Layout 1 | `c2a963bd2d3e`  |
| 2507   | Layout 1 | `c2a963bd2d3e`  |
| 2503   | Layout 1 | `c2a963bd2d3e`  |
| 2498   | Layout 1 | `c2a963bd2d3e`  |
| 2492   | Layout 1 | `c2a963bd2d3e`  |
| 2487   | Layout 1 | `c2a963bd2d3e`  |
| 2480   | Layout 1 | `c2a963bd2d3e`  |
| 2474   | Layout 1 | `c2a963bd2d3e`  |
| 2468   | Layout 1 | `c2a963bd2d3e`  |
| 2460   | Layout 1 | `c2a963bd2d3e`  |
| 2453   | Layout 1 | `c2a963bd2d3e`  |
| 2444   | Layout 1 | `c2a963bd2d3e`  |
| 2438   | Layout 1 | `c2a963bd2d3e`  |
| 2434   | Layout 1 | `c2a963bd2d3e`  |
| 2429   | Layout 1 | `c2a963bd2d3e`  |
| 2421   | Layout 1 | `c2a963bd2d3e`  |
| 2414   | Layout 1 | `c2a963bd2d3e`  |
| 2407   | Layout 1 | `c2a963bd2d3e`  |
| 2401   | Layout 1 | `c2a963bd2d3e`  |
| 2397   | Layout 1 | `c2a963bd2d3e`  |
| 2393   | Layout 1 | `c2a963bd2d3e`  |
| 2384   | Layout 1 | `c2a963bd2d3e`  |
| 2378   | Layout 1 | `c2a963bd2d3e`  |
| 2372   | Layout 1 | `c2a963bd2d3e`  |
| 2358   | Layout 1 | `c2a963bd2d3e`  |
| 2352   | Layout 1 | `c2a963bd2d3e`  |
| 2347   | Layout 1 | `c2a963bd2d3e`  |
| 2343   | Layout 1 | `c2a963bd2d3e`  |
| 2335   | Layout 1 | `c2a963bd2d3e`  |
| 2327   | Layout 1 | `c2a963bd2d3e`  |
| 2324   | Layout 1 | `c2a963bd2d3e`  |
| 2319   | Layout 1 | `c2a963bd2d3e`  |
| 2313   | Layout 1 | `c2a963bd2d3e`  |
| 2308   | Layout 1 | `c2a963bd2d3e`  |
| 2302   | Layout 1 | `c2a963bd2d3e`  |
| 2295   | Layout 1 | `c2a963bd2d3e`  |
| 2290   | Layout 1 | `c2a963bd2d3e`  |
| 2284   | Layout 1 | `c2a963bd2d3e`  |
| 2276   | Layout 1 | `c2a963bd2d3e`  |
| 2269   | Layout 1 | `c2a963bd2d3e`  |
| 2259   | Layout 1 | `c2a963bd2d3e`  |
| 2250   | Layout 1 | `c2a963bd2d3e`  |
| 2243   | Layout 1 | `c2a963bd2d3e`  |
| 2235   | Layout 1 | `c2a963bd2d3e`  |
| 2229   | Layout 1 | `c2a963bd2d3e`  |
| 2224   | Layout 1 | `c2a963bd2d3e`  |
| 2218   | Layout 1 | `c2a963bd2d3e`  |
| 2215   | Layout 1 | `c2a963bd2d3e`  |
| 2207   | Layout 1 | `c2a963bd2d3e`  |
| 2203   | Layout 1 | `c2a963bd2d3e`  |
| 2196   | Layout 1 | `c2a963bd2d3e`  |
| 2192   | Layout 1 | `c2a963bd2d3e`  |
| 2189   | Layout 1 | `c2a963bd2d3e`  |
| 2183   | Layout 1 | `c2a963bd2d3e`  |
| 2179   | Layout 1 | `c2a963bd2d3e`  |
| 2171   | Layout 1 | `c2a963bd2d3e`  |
| 2163   | Layout 1 | `c2a963bd2d3e`  |
| 2156   | Layout 1 | `c2a963bd2d3e`  |
| 2151   | Layout 1 | `c2a963bd2d3e`  |
| 2147   | Layout 1 | `c2a963bd2d3e`  |
| 2142   | Layout 1 | `c2a963bd2d3e`  |
| 2138   | Layout 1 | `c2a963bd2d3e`  |
| 2134   | Layout 1 | `c2a963bd2d3e`  |
| 2130   | Layout 1 | `c2a963bd2d3e`  |
| 2122   | Layout 1 | `c2a963bd2d3e`  |
| 2107   | Layout 1 | `c2a963bd2d3e`  |
| 2098   | Layout 1 | `c2a963bd2d3e`  |
| 2089   | Layout 1 | `c2a963bd2d3e`  |
| 2081   | Layout 1 | `c2a963bd2d3e`  |
| 2073   | Layout 1 | `c2a963bd2d3e`  |
| 2067   | Layout 1 | `c2a963bd2d3e`  |
| 2063   | Layout 1 | `c2a963bd2d3e`  |
| 2059   | Layout 1 | `c2a963bd2d3e`  |
| 2052   | Layout 1 | `c2a963bd2d3e`  |
| 2044   | Layout 1 | `c2a963bd2d3e`  |
| 2039   | Layout 1 | `c2a963bd2d3e`  |
| 2032   | Layout 1 | `c2a963bd2d3e`  |
| 2025   | Layout 1 | `c2a963bd2d3e`  |
| 2011   | Layout 1 | `c2a963bd2d3e`  |
| 2005   | Layout 1 | `c2a963bd2d3e`  |
| 2000   | Layout 1 | `c2a963bd2d3e`  |
| 1996   | Layout 1 | `c2a963bd2d3e`  |
| 1991   | Layout 1 | `c2a963bd2d3e`  |
| 1985   | Layout 1 | `c2a963bd2d3e`  |
| 1980   | Layout 1 | `c2a963bd2d3e`  |
| 1969   | Layout 1 | `c2a963bd2d3e`  |
| 1964   | Layout 1 | `c2a963bd2d3e`  |
| 1958   | Layout 1 | `c2a963bd2d3e`  |
| 1950   | Layout 1 | `c2a963bd2d3e`  |
| 1945   | Layout 1 | `c2a963bd2d3e`  |
| 1937   | Layout 1 | `c2a963bd2d3e`  |
| 1933   | Layout 1 | `c2a963bd2d3e`  |
| 1927   | Layout 1 | `c2a963bd2d3e`  |
| 1921   | Layout 1 | `c2a963bd2d3e`  |
| 1914   | Layout 1 | `c2a963bd2d3e`  |
| 1908   | Layout 1 | `c2a963bd2d3e`  |
| 1897   | Layout 1 | `c2a963bd2d3e`  |
| 1892   | Layout 1 | `c2a963bd2d3e`  |
| 1886   | Layout 1 | `c2a963bd2d3e`  |
| 1881   | Layout 1 | `c2a963bd2d3e`  |
| 1871   | Layout 1 | `c2a963bd2d3e`  |
| 1866   | Layout 1 | `c2a963bd2d3e`  |
| 1862   | Layout 1 | `c2a963bd2d3e`  |
| 1854   | Layout 1 | `c2a963bd2d3e`  |
| 1846   | Layout 1 | `c2a963bd2d3e`  |
| 1838   | Layout 1 | `c2a963bd2d3e`  |
| 1832   | Layout 1 | `c2a963bd2d3e`  |
| 1826   | Layout 1 | `c2a963bd2d3e`  |
| 1822   | Layout 1 | `c2a963bd2d3e`  |
| 1818   | Layout 1 | `c2a963bd2d3e`  |
| 1804   | Layout 1 | `c2a963bd2d3e`  |
| 1794   | Layout 1 | `c2a963bd2d3e`  |
| 1790   | Layout 1 | `c2a963bd2d3e`  |
| 1784   | Layout 1 | `c2a963bd2d3e`  |
| 1774   | Layout 1 | `c2a963bd2d3e`  |
| 1771   | Layout 1 | `c2a963bd2d3e`  |
| 1762   | Layout 1 | `c2a963bd2d3e`  |
| 1759   | Layout 1 | `c2a963bd2d3e`  |
| 1754   | Layout 1 | `c2a963bd2d3e`  |
| 1749   | Layout 1 | `c2a963bd2d3e`  |
| 1743   | Layout 1 | `c2a963bd2d3e`  |
| 1737   | Layout 1 | `c2a963bd2d3e`  |
| 1731   | Layout 1 | `c2a963bd2d3e`  |
| 1725   | Layout 1 | `c2a963bd2d3e`  |
| 1717   | Layout 1 | `c2a963bd2d3e`  |
| 1710   | Layout 1 | `c2a963bd2d3e`  |
| 1704   | Layout 1 | `c2a963bd2d3e`  |
| 1698   | Layout 1 | `c2a963bd2d3e`  |
| 1690   | Layout 1 | `c2a963bd2d3e`  |
| 1685   | Layout 1 | `c2a963bd2d3e`  |
| 1680   | Layout 1 | `c2a963bd2d3e`  |
| 1674   | Layout 1 | `c2a963bd2d3e`  |
| 1668   | Layout 1 | `c2a963bd2d3e`  |
| 1659   | Layout 1 | `c2a963bd2d3e`  |
| 1649   | Layout 1 | `c2a963bd2d3e`  |
| 1642   | Layout 1 | `c2a963bd2d3e`  |
| 1636   | Layout 1 | `c2a963bd2d3e`  |
| 1628   | Layout 1 | `c2a963bd2d3e`  |
| 1622   | Layout 1 | `c2a963bd2d3e`  |
| 1614   | Layout 1 | `c2a963bd2d3e`  |
| 1608   | Layout 1 | `c2a963bd2d3e`  |
| 1602   | Layout 1 | `c2a963bd2d3e`  |
| 1598   | Layout 1 | `c2a963bd2d3e`  |
| 1594   | Layout 1 | `c2a963bd2d3e`  |
| 1590   | Layout 1 | `c2a963bd2d3e`  |
| 1587   | Layout 1 | `c2a963bd2d3e`  |
| 1584   | Layout 1 | `c2a963bd2d3e`  |
| 1579   | Layout 1 | `c2a963bd2d3e`  |
| 1572   | Layout 1 | `c2a963bd2d3e`  |
| 1565   | Layout 1 | `c2a963bd2d3e`  |
| 1559   | Layout 1 | `c2a963bd2d3e`  |
| 1554   | Layout 1 | `c2a963bd2d3e`  |
| 1547   | Layout 1 | `c2a963bd2d3e`  |
| 1537   | Layout 1 | `c2a963bd2d3e`  |
| 1529   | Layout 1 | `c2a963bd2d3e`  |
| 1524   | Layout 1 | `c2a963bd2d3e`  |
| 1519   | Layout 1 | `c2a963bd2d3e`  |
| 1509   | Layout 1 | `c2a963bd2d3e`  |
| 1506   | Layout 1 | `c2a963bd2d3e`  |
| 1504   | Layout 1 | `c2a963bd2d3e`  |
| 1500   | Layout 1 | `c2a963bd2d3e`  |
| 1493   | Layout 1 | `c2a963bd2d3e`  |
| 1489   | Layout 1 | `c2a963bd2d3e`  |
| 1485   | Layout 1 | `c2a963bd2d3e`  |
| 1481   | Layout 1 | `c2a963bd2d3e`  |
| 1474   | Layout 1 | `c2a963bd2d3e`  |
| 1466   | Layout 1 | `c2a963bd2d3e`  |
| 1462   | Layout 1 | `c2a963bd2d3e`  |
| 1459   | Layout 1 | `c2a963bd2d3e`  |
| 1453   | Layout 1 | `c2a963bd2d3e`  |
| 1450   | Layout 1 | `c2a963bd2d3e`  |
| 1445   | Layout 1 | `c2a963bd2d3e`  |
| 1439   | Layout 1 | `c2a963bd2d3e`  |
| 1433   | Layout 1 | `c2a963bd2d3e`  |
| 1430   | Layout 1 | `c2a963bd2d3e`  |
| 1426   | Layout 1 | `c2a963bd2d3e`  |
| 1421   | Layout 1 | `c2a963bd2d3e`  |
| 1417   | Layout 1 | `c2a963bd2d3e`  |
| 1416   | Layout 1 | `c2a963bd2d3e`  |
| 1409   | Layout 1 | `c2a963bd2d3e`  |
| 1405   | Layout 1 | `c2a963bd2d3e`  |
| 1401   | Layout 1 | `c2a963bd2d3e`  |
| 1396   | Layout 1 | `c2a963bd2d3e`  |
| 1391   | Layout 1 | `c2a963bd2d3e`  |
| 1390   | Layout 1 | `c2a963bd2d3e`  |
| 1386   | Layout 1 | `c2a963bd2d3e`  |
| 1381   | Layout 1 | `c2a963bd2d3e`  |
| 1379   | Layout 1 | `c2a963bd2d3e`  |
| 1372   | Layout 1 | `c2a963bd2d3e`  |
| 1366   | Layout 1 | `c2a963bd2d3e`  |
| 1364   | Layout 1 | `c2a963bd2d3e`  |
| 1363   | Layout 1 | `c2a963bd2d3e`  |
| 1360   | Layout 1 | `c2a963bd2d3e`  |
| 1358   | Layout 1 | `c2a963bd2d3e`  |
| 1355   | Layout 1 | `c2a963bd2d3e`  |
| 1351   | Layout 1 | `c2a963bd2d3e`  |
| 1348   | Layout 1 | `c2a963bd2d3e`  |
| 1346   | Layout 1 | `c2a963bd2d3e`  |
| 1341   | Layout 1 | `c2a963bd2d3e`  |
| 1340   | Layout 1 | `c2a963bd2d3e`  |
| 1338   | Layout 1 | `c2a963bd2d3e`  |
| 1335   | Layout 1 | `c2a963bd2d3e`  |
| 1333   | Layout 1 | `c2a963bd2d3e`  |
| 1329   | Layout 1 | `c2a963bd2d3e`  |
| 1327   | Layout 1 | `c2a963bd2d3e`  |
| 1324   | Layout 1 | `c2a963bd2d3e`  |
| 1321   | Layout 1 | `c2a963bd2d3e`  |
| 1319   | Layout 1 | `c2a963bd2d3e`  |
| 1318   | Layout 1 | `c2a963bd2d3e`  |
| 1316   | Layout 1 | `c2a963bd2d3e`  |
| 1313   | Layout 1 | `c2a963bd2d3e`  |
| 1311   | Layout 1 | `c2a963bd2d3e`  |
| 1309   | Layout 1 | `c2a963bd2d3e`  |
| 1304   | Layout 1 | `c2a963bd2d3e`  |
| 1292   | Layout 1 | `c2a963bd2d3e`  |
| 1286   | Layout 1 | `c2a963bd2d3e`  |
| 1280   | Layout 1 | `c2a963bd2d3e`  |
| 1276   | Layout 1 | `c2a963bd2d3e`  |
| 1267   | Layout 1 | `c2a963bd2d3e`  |
| 1261   | Layout 1 | `c2a963bd2d3e`  |
| 1256   | Layout 1 | `c2a963bd2d3e`  |
| 1250   | Layout 1 | `c2a963bd2d3e`  |
| 1246   | Layout 1 | `c2a963bd2d3e`  |
| 1239   | Layout 1 | `c2a963bd2d3e`  |
| 1230   | No file  | `c2a963bd2d3e`  |
| 1226   | No file  | `c2a963bd2d3e`  |
| 1220   | No file  | `c2a963bd2d3e`  |
| 1217   | No file  | `c2a963bd2d3e`  |
| 1211   | No file  | `c2a963bd2d3e`  |
| 1210   | No file  | `c2a963bd2d3e`  |
| 1208   | No file  | `c2a963bd2d3e`  |
| 1203   | No file  | `c2a963bd2d3e`  |
| 1197   | No file  | `c2a963bd2d3e`  |
| 1194   | No file  | `c2a963bd2d3e`  |
| 1192   | No file  | `c2a963bd2d3e`  |
| 1187   | No file  | `c2a963bd2d3e`  |
| 1183   | No file  | `c2a963bd2d3e`  |
| 1177   | No file  | `c2a963bd2d3e`  |
| 1173   | No file  | `c2a963bd2d3e`  |
| 1167   | No file  | `c2a963bd2d3e`  |
| 1164   | No file  | `c2a963bd2d3e`  |
| 1156   | No file  | `c2a963bd2d3e`  |
| 1149   | No file  | `c2a963bd2d3e`  |
| 1144   | No file  | `c2a963bd2d3e`  |
| 1137   | No file  | `c2a963bd2d3e`  |
| 1132   | No file  | `c2a963bd2d3e`  |
| 1127   | No file  | `c2a963bd2d3e`  |
| 1122   | No file  | `c2a963bd2d3e`  |
| 1118   | No file  | `c2a963bd2d3e`  |
| 1114   | No file  | `c2a963bd2d3e`  |
| 1109   | No file  | `c2a963bd2d3e`  |
| 1102   | No file  | `c2a963bd2d3e`  |
| 1096   | No file  | `c2a963bd2d3e`  |
| 1088   | No file  | `c2a963bd2d3e`  |
| 1081   | No file  | `c2a963bd2d3e`  |
| 1076   | No file  | `c2a963bd2d3e`  |
| 1069   | No file  | `c2a963bd2d3e`  |
| 1064   | No file  | `c2a963bd2d3e`  |
| 1058   | No file  | `c2a963bd2d3e`  |
| 1051   | No file  | `c2a963bd2d3e`  |
| 1044   | No file  | `c2a963bd2d3e`  |
| 1036   | No file  | `c2a963bd2d3e`  |
| 1026   | No file  | `c2a963bd2d3e`  |
| 1016   | No file  | `c2a963bd2d3e`  |
| 1009   | No file  | `c2a963bd2d3e`  |
| 1005   | No file  | `c2a963bd2d3e`  |
| 1000   | No file  | `c2a963bd2d3e`  |
| 998    | No file  | `c2a963bd2d3e`  |
| 990    | No file  | `c2a963bd2d3e`  |
| 979    | No file  | `c2a963bd2d3e`  |
| 972    | No file  | `c2a963bd2d3e`  |
| 963    | No file  | `c2a963bd2d3e`  |
| 955    | No file  | `c2a963bd2d3e`  |
| 946    | No file  | `c2a963bd2d3e`  |
| 938    | No file  | `c2a963bd2d3e`  |
| 927    | No file  | `c2a963bd2d3e`  |
| 911    | No file  | `c2a963bd2d3e`  |
| 904    | No file  | `c2a963bd2d3e`  |
| 899    | No file  | `c2a963bd2d3e`  |
| 894    | No file  | `c2a963bd2d3e`  |
| 885    | No file  | `c2a963bd2d3e`  |
| 879    | No file  | `c2a963bd2d3e`  |
| 872    | No file  | `c2a963bd2d3e`  |
| 864    | No file  | `c2a963bd2d3e`  |
| 855    | No file  | `c2a963bd2d3e`  |
| 853    | No file  | `c2a963bd2d3e`  |
| 845    | No file  | `c2a963bd2d3e`  |
| 837    | No file  | `c2a963bd2d3e`  |
| 829    | No file  | `c2a963bd2d3e`  |
| 822    | No file  | `c2a963bd2d3e`  |
| 814    | No file  | `c2a963bd2d3e`  |
| 805    | No file  | `c2a963bd2d3e`  |
| 794    | No file  | `c2a963bd2d3e`  |
| 787    | No file  | `c2a963bd2d3e`  |
| 780    | No file  | `c2a963bd2d3e`  |
| 771    | No file  | `c2a963bd2d3e`  |
| 760    | No file  | `c2a963bd2d3e`  |
| 748    | No file  | `c2a963bd2d3e`  |
| 741    | No file  | `c2a963bd2d3e`  |
| 736    | No file  | `c2a963bd2d3e`  |
| 731    | No file  | `c2a963bd2d3e`  |
| 723    | No file  | `c2a963bd2d3e`  |
| 711    | No file  | `c2a963bd2d3e`  |
| 707    | No file  | `c2a963bd2d3e`  |
| 697    | No file  | `c2a963bd2d3e`  |
| 689    | No file  | `c2a963bd2d3e`  |
| 683    | No file  | `c2a963bd2d3e`  |
| 678    | No file  | `c2a963bd2d3e`  |
| 670    | No file  | `c2a963bd2d3e`  |
| 661    | No file  | `c2a963bd2d3e`  |
| 656    | No file  | `c2a963bd2d3e`  |
| 652    | No file  | `c2a963bd2d3e`  |
| 643    | No file  | `c2a963bd2d3e`  |
| 637    | No file  | `c2a963bd2d3e`  |
| 630    | No file  | `c2a963bd2d3e`  |
| 627    | No file  | `c2a963bd2d3e`  |
| 621    | No file  | `c2a963bd2d3e`  |
| 617    | No file  | `c2a963bd2d3e`  |
| 615    | No file  | `c2a963bd2d3e`  |
| 606    | No file  | `c2a963bd2d3e`  |
| 599    | No file  | `c2a963bd2d3e`  |
| 592    | No file  | `c2a963bd2d3e`  |
| 586    | No file  | `c2a963bd2d3e`  |
| 577    | No file  | `c2a963bd2d3e`  |
| 569    | No file  | `c2a963bd2d3e`  |
| 561    | No file  | `c2a963bd2d3e`  |
| 554    | No file  | `c2a963bd2d3e`  |
| 542    | No file  | `c2a963bd2d3e`  |
| 532    | No file  | `c2a963bd2d3e`  |
| 531    | No file  | `c2a963bd2d3e`  |
| 526    | No file  | `c2a963bd2d3e`  |
| 521    | No file  | `c2a963bd2d3e`  |
| 517    | No file  | `c2a963bd2d3e`  |
| 510    | No file  | `c2a963bd2d3e`  |
| 508    | No file  | `c2a963bd2d3e`  |
| 504    | No file  | `c2a963bd2d3e`  |
| 497    | No file  | `c2a963bd2d3e`  |
| 491    | No file  | `c2a963bd2d3e`  |
| 485    | No file  | `c2a963bd2d3e`  |
| 478    | No file  | `c2a963bd2d3e`  |
| 472    | No file  | `c2a963bd2d3e`  |
| 466    | No file  | `c2a963bd2d3e`  |
| 457    | No file  | `c2a963bd2d3e`  |
| 452    | No file  | `c2a963bd2d3e`  |
| 449    | No file  | `c2a963bd2d3e`  |
| 435    | No file  | `c2a963bd2d3e`  |

<!-- versions:end -->

## Companion Files

None. The handler names each vehicle type with its `CppEnums.VehicleType`
member name.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 37 bytes + vehicle types)

| Offset               | Type                    | Field                 | Notes                                                                                 |
| -------------------- | ----------------------- | --------------------- | ------------------------------------------------------------------------------------- |
| `+0x00`              | bytes[3]                | map_color             | Great Ocean map colour, stored blue, green, red; unique per row                       |
| `+0x03`              | u8                      | unknown_03            | Always `0`                                                                            |
| `+0x04`              | bytes[3]                | unknown_04            | Equals `map_color` on every row                                                       |
| `+0x07`              | u8                      | unknown_07            | Always `0`                                                                            |
| `+0x08`              | f32                     | x                     | `-6` to `6` on client 3482                                                            |
| `+0x0C`              | f32                     | y                     | `0` to `71` on client 3482                                                            |
| `+0x10`              | f32                     | z                     | `-6` to `6` on client 3482                                                            |
| `+0x14`              | f32                     | magnification         | `1`, `1.25` or `1.7` on client 3482                                                   |
| `+0x18`              | u64                     | vehicle_type_count    | Number of `vehicle_types`; `0` or `5` on client 3482                                  |
| `+0x20`              | u8[vehicle_type_count]  | vehicle_types         | `CppEnums.VehicleType` values; `60, 56, 46, 44, 34` on both rows that have a list     |
| `vehicle_types+0x00` | u8                      | restricted_area_state | `0` on 137 rows, `1` and `2` on the two rows with vehicle types (client 3482)         |
| `vehicle_types+0x01` | u32                     | wind_impact           | Six values from `20000` to `500000` on client 3482                                    |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `GreatSea_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `R`, `G`, `B`, `X`, `Y`, `Z`,
`Magnification`, `VehicleType`, `RestrictedAreaState` and `WindImpact` and
139 rows. Keyed by colour, all 139 rows of the client 1784 file match the
sheet on every column (139 of 139). `VehicleType` holds the list as text,
`60,56,46,44,34`. That server's dump names the members `GreatSeaStaticStatus
x`, `z`, `magnitude`, `WindImpact` and `State` in its check messages; the
field names follow the sheet columns.

On client 3482 the same 139 colours carry the same values except
`magnification`: seven rows read `1.25` where the sheet and the client
1784 file have `1`.

## Vehicle Types

The two rows with a list name the same five ships, in this order
(`global_define_cpp_enum.luac`, client 3482):

| Value | `CppEnums.VehicleType` |
| ----- | ---------------------- |
| 60    | `Type_Carrack`         |
| 56    | `Type_CashPersonalTradeShip` |
| 46    | `Type_PersonTradeShip` |
| 44    | `Type_PersonalBattleShip` |
| 34    | `Type_SailingBoat`     |

## Notes

- `map_color` follows the region map files, as in
  [`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md#field-names):
  on client 3482 `greatseamap.bmp.rid` lists 103 colours, `32 FF 00`
  first, and all 103 are `map_color` values of this file; the other 36
  rows are colours the `.rid` does not list.
- The two rows with vehicle types are `e0bfbf` (`restricted_area_state`
  `2`) and `e0cccc` (`1`), both with `x`, `y` and `z` `0` and the lowest
  `wind_impact`, `20000`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/greatsea_tables.py`:
  `map_color` as `rrggbb`, the f32 values, the vehicle types with their
  names and the two values after them.

## Open Questions

### What `x`, `y` and `z` Hold

The three f32 values are small (`-6` to `6`, `0` to `71`), far below world
coordinates, and `y` grows where `x` and `z` move away from `0`. They may
be a wind or current vector per area, which `wind_impact` scales; no
client Lua names a getter for them.

### What the Restricted Area States Mean

Only the two rows with vehicle types have a `restricted_area_state`
(`1` and `2`). Whether the list names the ships allowed into the area or
the ones kept out is not in the client data checked.

### Why the Colour Is Stored Twice

`unknown_04` equals `map_color` on every row, and `unknown_03` and
`unknown_07` are always `0`, as in the other region map colour tables.
The sheet has one `R`, `G`, `B` set only.
