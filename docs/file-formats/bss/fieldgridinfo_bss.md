# `fieldgridinfo.bss` Format

## Purpose

The list of field grid squares that hold spawns, one file per spawn grid
folder `mapdata_<resource>/spawnplacementfieldgrid/<field_no>/7/`. Each
entry is a square of 3,700 x 3,700 world units that one of the folder's
[x_y.bss](x_y_bss.md) cell files lists spawns under; see
[Grid Squares](x_y_bss.md#grid-squares) for how a square maps to world
coordinates. On client 3482 the field `1` file lists 13,110 squares, field
`700` 4 and field `701` 7; the 66 `A1_` fields `4001` to `4066` have an
empty list.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                                                         | Bytes  | Records       | Row bytes |
| ------ | ------------- | ------------------------------------------------------------ | ------ | ------------- | --------- |
| 1      | 805 and later | `mapdata_real/spawnplacementfieldgrid/1/7/fieldgridinfo.bss` | 52,456 | 13,110 Square | 4         |

| Layout | File                                                         | Known             | Unknown    |
| ------ | ------------------------------------------------------------ | ----------------- | ---------- |
| 1      | `mapdata_real/spawnplacementfieldgrid/1/7/fieldgridinfo.bss` | 52,456 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `921d6f04777a`  |
| 3482   | No file              | `921d6f04777a`  |
| 3474   | Layout 1             | `921d6f04777a`  |
| 3473   | Layout 1             | `921d6f04777a`  |
| 3464   | Layout 1             | `921d6f04777a`  |
| 3458   | Layout 1             | `921d6f04777a`  |
| 3454   | Layout 1             | `921d6f04777a`  |
| 3444   | Layout 1             | `921d6f04777a`  |
| 3435   | Layout 1             | `921d6f04777a`  |
| 3426   | Layout 1             | `921d6f04777a`  |
| 3418   | Layout 1             | `921d6f04777a`  |
| 3412   | Layout 1             | `921d6f04777a`  |
| 3402   | Layout 1             | `921d6f04777a`  |
| 3396   | Layout 1             | `921d6f04777a`  |
| 3387   | Layout 1             | `921d6f04777a`  |
| 3381   | Layout 1             | `921d6f04777a`  |
| 3373   | Layout 1             | `921d6f04777a`  |
| 3364   | Layout 1             | `921d6f04777a`  |
| 3356   | Layout 1             | `921d6f04777a`  |
| 3349   | Layout 1             | `921d6f04777a`  |
| 3342   | Layout 1             | `921d6f04777a`  |
| 3335   | Layout 1             | `921d6f04777a`  |
| 3326   | Layout 1             | `921d6f04777a`  |
| 3321   | Layout 1             | `921d6f04777a`  |
| 3314   | Layout 1             | `921d6f04777a`  |
| 3303   | Layout 1             | `921d6f04777a`  |
| 3302   | Layout 1             | `921d6f04777a`  |
| 3293   | Layout 1             | `921d6f04777a`  |
| 3283   | Layout 1             | `921d6f04777a`  |
| 3275   | Layout 1             | `921d6f04777a`  |
| 3267   | Layout 1             | `921d6f04777a`  |
| 3258   | Layout 1             | `921d6f04777a`  |
| 3251   | Layout 1             | `921d6f04777a`  |
| 3242   | Layout 1             | `921d6f04777a`  |
| 3235   | Layout 1             | `921d6f04777a`  |
| 3229   | Layout 1             | `921d6f04777a`  |
| 3212   | Layout 1             | `921d6f04777a`  |
| 3203   | Layout 1             | `921d6f04777a`  |
| 3193   | Layout 1             | `921d6f04777a`  |
| 3186   | Layout 1             | `921d6f04777a`  |
| 3177   | Layout 1             | `921d6f04777a`  |
| 3169   | Layout 1             | `921d6f04777a`  |
| 3158   | Layout 1             | `921d6f04777a`  |
| 3151   | Layout 1             | `921d6f04777a`  |
| 3144   | Layout 1             | `921d6f04777a`  |
| 3133   | Layout 1             | `921d6f04777a`  |
| 3125   | Layout 1             | `921d6f04777a`  |
| 3118   | Layout 1             | `921d6f04777a`  |
| 3111   | Layout 1             | `921d6f04777a`  |
| 3103   | Layout 1             | `921d6f04777a`  |
| 3095   | Layout 1             | `921d6f04777a`  |
| 3086   | Layout 1             | `921d6f04777a`  |
| 3072   | Layout 1             | `921d6f04777a`  |
| 3062   | Layout 1             | `921d6f04777a`  |
| 3052   | Layout 1             | `921d6f04777a`  |
| 3045   | Layout 1             | `921d6f04777a`  |
| 3037   | Layout 1             | `921d6f04777a`  |
| 3030   | Layout 1             | `921d6f04777a`  |
| 3021   | Layout 1             | `921d6f04777a`  |
| 3012   | Layout 1             | `921d6f04777a`  |
| 3002   | Layout 1             | `921d6f04777a`  |
| 2995   | Layout 1             | `921d6f04777a`  |
| 2987   | Layout 1             | `921d6f04777a`  |
| 2978   | Layout 1             | `921d6f04777a`  |
| 2970   | Layout 1             | `921d6f04777a`  |
| 2959   | Layout 1             | `921d6f04777a`  |
| 2951   | Layout 1             | `921d6f04777a`  |
| 2942   | Layout 1             | `921d6f04777a`  |
| 2935   | Layout 1             | `921d6f04777a`  |
| 2932   | Layout 1             | `921d6f04777a`  |
| 2923   | Layout 1             | `921d6f04777a`  |
| 2919   | Layout 1             | `921d6f04777a`  |
| 2907   | Layout 1             | `921d6f04777a`  |
| 2900   | Layout 1             | `921d6f04777a`  |
| 2891   | Layout 1             | `921d6f04777a`  |
| 2882   | Layout 1             | `921d6f04777a`  |
| 2872   | Layout 1             | `921d6f04777a`  |
| 2863   | Layout 1             | `921d6f04777a`  |
| 2855   | Layout 1             | `921d6f04777a`  |
| 2849   | Layout 1             | `921d6f04777a`  |
| 2844   | Layout 1             | `921d6f04777a`  |
| 2834   | Layout 1             | `921d6f04777a`  |
| 2825   | Layout 1             | `921d6f04777a`  |
| 2819   | Layout 1             | `921d6f04777a`  |
| 2811   | Layout 1             | `921d6f04777a`  |
| 2803   | Layout 1             | `921d6f04777a`  |
| 2794   | Layout 1             | `921d6f04777a`  |
| 2783   | Layout 1             | `921d6f04777a`  |
| 2774   | Layout 1             | `921d6f04777a`  |
| 2765   | Layout 1             | `921d6f04777a`  |
| 2756   | Layout 1             | `921d6f04777a`  |
| 2750   | Layout 1             | `921d6f04777a`  |
| 2743   | Layout 1             | `921d6f04777a`  |
| 2736   | Layout 1             | `921d6f04777a`  |
| 2726   | Layout 1             | `921d6f04777a`  |
| 2717   | Layout 1             | `921d6f04777a`  |
| 2709   | Layout 1             | `921d6f04777a`  |
| 2703   | Layout 1             | `921d6f04777a`  |
| 2695   | Layout 1             | `921d6f04777a`  |
| 2684   | Layout 1             | `921d6f04777a`  |
| 2672   | Layout 1             | `921d6f04777a`  |
| 2665   | Layout 1             | `921d6f04777a`  |
| 2657   | Layout 1             | `921d6f04777a`  |
| 2649   | Layout 1             | `921d6f04777a`  |
| 2644   | Layout 1             | `921d6f04777a`  |
| 2637   | Layout 1             | `921d6f04777a`  |
| 2629   | Layout 1             | `921d6f04777a`  |
| 2619   | Layout 1             | `921d6f04777a`  |
| 2612   | Layout 1             | `921d6f04777a`  |
| 2606   | Layout 1             | `921d6f04777a`  |
| 2602   | Layout 1             | `921d6f04777a`  |
| 2601   | Layout 1             | `921d6f04777a`  |
| 2592   | Layout 1             | `921d6f04777a`  |
| 2583   | Layout 1             | `921d6f04777a`  |
| 2575   | Layout 1             | `921d6f04777a`  |
| 2567   | Layout 1             | `921d6f04777a`  |
| 2560   | Layout 1             | `921d6f04777a`  |
| 2553   | Layout 1             | `921d6f04777a`  |
| 2545   | Layout 1             | `921d6f04777a`  |
| 2538   | Layout 1             | `921d6f04777a`  |
| 2529   | Layout 1             | `921d6f04777a`  |
| 2519   | Layout 1             | `921d6f04777a`  |
| 2513   | Layout 1             | `921d6f04777a`  |
| 2510   | Layout 1             | `921d6f04777a`  |
| 2507   | Layout 1             | `921d6f04777a`  |
| 2503   | Layout 1             | `921d6f04777a`  |
| 2498   | Layout 1             | `921d6f04777a`  |
| 2492   | Layout 1             | `921d6f04777a`  |
| 2487   | Layout 1             | `921d6f04777a`  |
| 2480   | Layout 1             | `921d6f04777a`  |
| 2474   | Layout 1             | `921d6f04777a`  |
| 2468   | Layout 1             | `921d6f04777a`  |
| 2460   | Layout 1             | `921d6f04777a`  |
| 2453   | Layout 1             | `921d6f04777a`  |
| 2444   | Layout 1             | `921d6f04777a`  |
| 2438   | Layout 1             | `921d6f04777a`  |
| 2434   | Layout 1             | `921d6f04777a`  |
| 2429   | Layout 1             | `921d6f04777a`  |
| 2421   | Layout 1             | `921d6f04777a`  |
| 2414   | Layout 1             | `921d6f04777a`  |
| 2407   | Layout 1             | `921d6f04777a`  |
| 2401   | Layout 1             | `921d6f04777a`  |
| 2397   | Layout 1             | `921d6f04777a`  |
| 2393   | Layout 1             | `921d6f04777a`  |
| 2384   | Layout 1             | `921d6f04777a`  |
| 2378   | Layout 1             | `921d6f04777a`  |
| 2372   | Layout 1             | `921d6f04777a`  |
| 2358   | Layout 1             | `921d6f04777a`  |
| 2352   | Layout 1             | `921d6f04777a`  |
| 2347   | Layout 1             | `921d6f04777a`  |
| 2343   | Layout 1             | `921d6f04777a`  |
| 2335   | Layout 1             | `921d6f04777a`  |
| 2327   | Layout 1             | `921d6f04777a`  |
| 2324   | Layout 1             | `921d6f04777a`  |
| 2319   | Layout 1             | `921d6f04777a`  |
| 2313   | Layout 1             | `921d6f04777a`  |
| 2308   | Layout 1             | `921d6f04777a`  |
| 2302   | Layout 1             | `921d6f04777a`  |
| 2295   | Layout 1             | `921d6f04777a`  |
| 2290   | Layout 1             | `921d6f04777a`  |
| 2284   | Layout 1             | `921d6f04777a`  |
| 2276   | Layout 1             | `921d6f04777a`  |
| 2269   | Layout 1             | `921d6f04777a`  |
| 2259   | Layout 1             | `921d6f04777a`  |
| 2250   | Layout 1             | `921d6f04777a`  |
| 2243   | Layout 1             | `921d6f04777a`  |
| 2235   | Layout 1             | `921d6f04777a`  |
| 2229   | Layout 1             | `921d6f04777a`  |
| 2224   | Layout 1             | `921d6f04777a`  |
| 2218   | Layout 1             | `921d6f04777a`  |
| 2215   | Layout 1             | `921d6f04777a`  |
| 2207   | Layout 1             | `921d6f04777a`  |
| 2203   | Layout 1             | `921d6f04777a`  |
| 2196   | Layout 1             | `921d6f04777a`  |
| 2192   | Layout 1             | `921d6f04777a`  |
| 2189   | Layout 1             | `921d6f04777a`  |
| 2183   | Layout 1             | `921d6f04777a`  |
| 2179   | Layout 1             | `921d6f04777a`  |
| 2171   | Layout 1             | `921d6f04777a`  |
| 2163   | Layout 1             | `921d6f04777a`  |
| 2156   | Layout 1             | `921d6f04777a`  |
| 2151   | Layout 1             | `921d6f04777a`  |
| 2147   | Layout 1             | `921d6f04777a`  |
| 2142   | Layout 1             | `921d6f04777a`  |
| 2138   | Layout 1             | `921d6f04777a`  |
| 2134   | Layout 1             | `921d6f04777a`  |
| 2130   | Layout 1             | `921d6f04777a`  |
| 2122   | Layout 1             | `921d6f04777a`  |
| 2107   | Layout 1             | `921d6f04777a`  |
| 2098   | Layout 1             | `921d6f04777a`  |
| 2089   | Layout 1             | `921d6f04777a`  |
| 2081   | Layout 1             | `921d6f04777a`  |
| 2073   | Layout 1             | `921d6f04777a`  |
| 2067   | Layout 1             | `921d6f04777a`  |
| 2063   | Layout 1             | `921d6f04777a`  |
| 2059   | Layout 1             | `921d6f04777a`  |
| 2052   | Layout 1             | `921d6f04777a`  |
| 2044   | Layout 1             | `921d6f04777a`  |
| 2039   | Layout 1             | `921d6f04777a`  |
| 2032   | Layout 1             | `921d6f04777a`  |
| 2025   | Layout 1             | `921d6f04777a`  |
| 2011   | Layout 1             | `921d6f04777a`  |
| 2005   | Layout 1             | `921d6f04777a`  |
| 2000   | Layout 1             | `921d6f04777a`  |
| 1996   | Layout 1             | `921d6f04777a`  |
| 1991   | Layout 1             | `921d6f04777a`  |
| 1985   | Layout 1             | `921d6f04777a`  |
| 1980   | Layout 1             | `921d6f04777a`  |
| 1969   | Layout 1             | `921d6f04777a`  |
| 1964   | Layout 1             | `921d6f04777a`  |
| 1958   | Layout 1             | `921d6f04777a`  |
| 1950   | Layout 1             | `921d6f04777a`  |
| 1945   | Layout 1             | `921d6f04777a`  |
| 1937   | Layout 1             | `921d6f04777a`  |
| 1933   | Layout 1             | `921d6f04777a`  |
| 1927   | Layout 1             | `921d6f04777a`  |
| 1921   | Layout 1             | `921d6f04777a`  |
| 1914   | Layout 1             | `921d6f04777a`  |
| 1908   | Layout 1             | `921d6f04777a`  |
| 1897   | Layout 1             | `921d6f04777a`  |
| 1892   | Layout 1             | `921d6f04777a`  |
| 1886   | Layout 1             | `921d6f04777a`  |
| 1881   | Layout 1             | `921d6f04777a`  |
| 1871   | Layout 1             | `921d6f04777a`  |
| 1866   | Layout 1             | `921d6f04777a`  |
| 1862   | Layout 1             | `921d6f04777a`  |
| 1854   | Layout 1             | `921d6f04777a`  |
| 1846   | Layout 1             | `921d6f04777a`  |
| 1838   | Layout 1             | `921d6f04777a`  |
| 1832   | Layout 1             | `921d6f04777a`  |
| 1826   | Layout 1             | `921d6f04777a`  |
| 1822   | Layout 1             | `921d6f04777a`  |
| 1818   | Layout 1             | `921d6f04777a`  |
| 1804   | Layout 1             | `921d6f04777a`  |
| 1794   | Layout 1             | `921d6f04777a`  |
| 1790   | Layout 1             | `921d6f04777a`  |
| 1784   | Layout 1             | `921d6f04777a`  |
| 1774   | Layout 1             | `921d6f04777a`  |
| 1771   | Layout 1             | `921d6f04777a`  |
| 1762   | Layout 1             | `921d6f04777a`  |
| 1759   | Layout 1             | `921d6f04777a`  |
| 1754   | Layout 1             | `921d6f04777a`  |
| 1749   | Layout 1             | `921d6f04777a`  |
| 1743   | Layout 1             | `921d6f04777a`  |
| 1737   | Layout 1             | `921d6f04777a`  |
| 1731   | Layout 1             | `921d6f04777a`  |
| 1725   | Layout 1             | `921d6f04777a`  |
| 1717   | Layout 1             | `921d6f04777a`  |
| 1710   | Layout 1             | `921d6f04777a`  |
| 1704   | Layout 1             | `921d6f04777a`  |
| 1698   | Layout 1             | `921d6f04777a`  |
| 1690   | Layout 1             | `921d6f04777a`  |
| 1685   | Layout 1             | `921d6f04777a`  |
| 1680   | Layout 1             | `921d6f04777a`  |
| 1674   | Layout 1             | `921d6f04777a`  |
| 1668   | Layout 1             | `921d6f04777a`  |
| 1659   | Layout 1             | `921d6f04777a`  |
| 1649   | Layout 1             | `921d6f04777a`  |
| 1642   | Layout 1             | `921d6f04777a`  |
| 1636   | Layout 1             | `921d6f04777a`  |
| 1628   | Layout 1             | `921d6f04777a`  |
| 1622   | Layout 1             | `921d6f04777a`  |
| 1614   | Layout 1             | `921d6f04777a`  |
| 1608   | Layout 1             | `921d6f04777a`  |
| 1602   | Layout 1             | `921d6f04777a`  |
| 1598   | Layout 1             | `921d6f04777a`  |
| 1594   | Layout 1             | `921d6f04777a`  |
| 1590   | Layout 1             | `921d6f04777a`  |
| 1587   | Layout 1             | `921d6f04777a`  |
| 1584   | Layout 1             | `921d6f04777a`  |
| 1579   | Layout 1             | `921d6f04777a`  |
| 1572   | Layout 1             | `921d6f04777a`  |
| 1565   | Layout 1             | `921d6f04777a`  |
| 1559   | Layout 1             | `921d6f04777a`  |
| 1554   | Layout 1             | `921d6f04777a`  |
| 1547   | Layout 1             | `921d6f04777a`  |
| 1537   | Layout 1             | `921d6f04777a`  |
| 1529   | Layout 1             | `921d6f04777a`  |
| 1524   | Layout 1             | `921d6f04777a`  |
| 1519   | Layout 1             | `921d6f04777a`  |
| 1509   | Layout 1             | `921d6f04777a`  |
| 1506   | Layout 1             | `921d6f04777a`  |
| 1504   | Layout 1             | `921d6f04777a`  |
| 1500   | Layout 1             | `921d6f04777a`  |
| 1493   | Layout 1             | `921d6f04777a`  |
| 1489   | Layout 1             | `921d6f04777a`  |
| 1485   | Layout 1             | `921d6f04777a`  |
| 1481   | Layout 1             | `921d6f04777a`  |
| 1474   | Layout 1             | `921d6f04777a`  |
| 1466   | Layout 1             | `921d6f04777a`  |
| 1462   | Layout 1             | `921d6f04777a`  |
| 1459   | Layout 1             | `921d6f04777a`  |
| 1453   | Layout 1             | `921d6f04777a`  |
| 1450   | Layout 1             | `921d6f04777a`  |
| 1445   | Layout 1             | `921d6f04777a`  |
| 1439   | Layout 1             | `921d6f04777a`  |
| 1433   | Layout 1             | `921d6f04777a`  |
| 1430   | Layout 1             | `921d6f04777a`  |
| 1426   | Layout 1             | `921d6f04777a`  |
| 1421   | Layout 1             | `921d6f04777a`  |
| 1417   | Layout 1             | `921d6f04777a`  |
| 1416   | Layout 1             | `921d6f04777a`  |
| 1409   | Layout 1             | `921d6f04777a`  |
| 1405   | Layout 1             | `921d6f04777a`  |
| 1401   | Layout 1             | `921d6f04777a`  |
| 1396   | Layout 1             | `921d6f04777a`  |
| 1391   | Layout 1             | `921d6f04777a`  |
| 1390   | Layout 1             | `921d6f04777a`  |
| 1386   | Layout 1             | `921d6f04777a`  |
| 1381   | Layout 1             | `921d6f04777a`  |
| 1379   | Layout 1             | `921d6f04777a`  |
| 1372   | Layout 1             | `921d6f04777a`  |
| 1366   | Layout 1             | `921d6f04777a`  |
| 1364   | Layout 1             | `921d6f04777a`  |
| 1363   | Layout 1             | `921d6f04777a`  |
| 1360   | Layout 1             | `921d6f04777a`  |
| 1358   | Layout 1             | `921d6f04777a`  |
| 1355   | Layout 1             | `921d6f04777a`  |
| 1351   | Layout 1             | `921d6f04777a`  |
| 1348   | Layout 1             | `921d6f04777a`  |
| 1346   | Layout 1             | `921d6f04777a`  |
| 1341   | Layout 1             | `921d6f04777a`  |
| 1340   | Layout 1             | `921d6f04777a`  |
| 1338   | Layout 1             | `921d6f04777a`  |
| 1335   | Layout 1             | `921d6f04777a`  |
| 1333   | Layout 1             | `921d6f04777a`  |
| 1329   | Layout 1             | `921d6f04777a`  |
| 1327   | Layout 1             | `921d6f04777a`  |
| 1324   | Layout 1             | `921d6f04777a`  |
| 1321   | Layout 1             | `921d6f04777a`  |
| 1319   | Layout 1             | `921d6f04777a`  |
| 1318   | Layout 1             | `921d6f04777a`  |
| 1316   | Layout 1             | `921d6f04777a`  |
| 1313   | Layout 1             | `921d6f04777a`  |
| 1311   | Layout 1             | `921d6f04777a`  |
| 1309   | Layout 1             | `921d6f04777a`  |
| 1304   | Layout 1             | `921d6f04777a`  |
| 1292   | Layout 1             | `921d6f04777a`  |
| 1286   | Layout 1             | `921d6f04777a`  |
| 1280   | Layout 1             | `921d6f04777a`  |
| 1276   | Layout 1             | `921d6f04777a`  |
| 1267   | Layout 1             | `921d6f04777a`  |
| 1261   | Layout 1             | `921d6f04777a`  |
| 1256   | Layout 1             | `921d6f04777a`  |
| 1250   | Layout 1             | `921d6f04777a`  |
| 1246   | Layout 1             | `921d6f04777a`  |
| 1239   | Layout 1             | `921d6f04777a`  |
| 1230   | Layout 1             | `921d6f04777a`  |
| 1226   | Layout 1             | `921d6f04777a`  |
| 1220   | Layout 1             | `921d6f04777a`  |
| 1217   | Layout 1             | `921d6f04777a`  |
| 1211   | Layout 1             | `921d6f04777a`  |
| 1210   | Layout 1             | `921d6f04777a`  |
| 1208   | Layout 1             | `921d6f04777a`  |
| 1203   | Layout 1             | `921d6f04777a`  |
| 1197   | Layout 1             | `921d6f04777a`  |
| 1194   | Layout 1             | `921d6f04777a`  |
| 1192   | Layout 1             | `921d6f04777a`  |
| 1187   | Layout 1             | `921d6f04777a`  |
| 1183   | Layout 1             | `921d6f04777a`  |
| 1177   | Layout 1             | `921d6f04777a`  |
| 1173   | Layout 1             | `921d6f04777a`  |
| 1167   | Layout 1             | `921d6f04777a`  |
| 1164   | Layout 1             | `921d6f04777a`  |
| 1156   | Layout 1             | `921d6f04777a`  |
| 1149   | Layout 1             | `921d6f04777a`  |
| 1144   | Layout 1             | `921d6f04777a`  |
| 1137   | Layout 1             | `921d6f04777a`  |
| 1132   | Layout 1             | `921d6f04777a`  |
| 1127   | Layout 1             | `921d6f04777a`  |
| 1122   | Layout 1             | `921d6f04777a`  |
| 1118   | Layout 1             | `921d6f04777a`  |
| 1114   | Layout 1             | `921d6f04777a`  |
| 1109   | Layout 1             | `921d6f04777a`  |
| 1102   | Layout 1             | `921d6f04777a`  |
| 1096   | Layout 1             | `921d6f04777a`  |
| 1088   | Layout 1             | `921d6f04777a`  |
| 1081   | Layout 1             | `921d6f04777a`  |
| 1076   | Layout 1             | `921d6f04777a`  |
| 1069   | Layout 1             | `921d6f04777a`  |
| 1064   | Layout 1             | `921d6f04777a`  |
| 1058   | Layout 1             | `921d6f04777a`  |
| 1051   | Layout 1             | `921d6f04777a`  |
| 1044   | Layout 1             | `921d6f04777a`  |
| 1036   | Layout 1             | `921d6f04777a`  |
| 1026   | Layout 1             | `921d6f04777a`  |
| 1016   | Layout 1             | `921d6f04777a`  |
| 1009   | Layout 1             | `921d6f04777a`  |
| 1005   | Layout 1             | `921d6f04777a`  |
| 1000   | Layout 1             | `921d6f04777a`  |
| 998    | Layout 1             | `921d6f04777a`  |
| 990    | Layout 1             | `921d6f04777a`  |
| 979    | Layout 1             | `921d6f04777a`  |
| 972    | Layout 1             | `921d6f04777a`  |
| 963    | Layout 1             | `921d6f04777a`  |
| 955    | Layout 1             | `921d6f04777a`  |
| 946    | Layout 1             | `921d6f04777a`  |
| 938    | Layout 1             | `921d6f04777a`  |
| 927    | Layout 1             | `921d6f04777a`  |
| 911    | Layout 1             | `921d6f04777a`  |
| 904    | Layout 1             | `921d6f04777a`  |
| 899    | Layout 1             | `921d6f04777a`  |
| 894    | Layout 1             | `921d6f04777a`  |
| 885    | Layout 1             | `921d6f04777a`  |
| 879    | Layout 1             | `921d6f04777a`  |
| 872    | Layout 1             | `921d6f04777a`  |
| 864    | Layout 1             | `921d6f04777a`  |
| 855    | Layout 1             | `921d6f04777a`  |
| 853    | Layout 1             | `921d6f04777a`  |
| 845    | Layout 1             | `921d6f04777a`  |
| 837    | Layout 1             | `921d6f04777a`  |
| 829    | Layout 1             | `921d6f04777a`  |
| 822    | Layout 1             | `921d6f04777a`  |
| 814    | Layout 1             | `921d6f04777a`  |
| 805    | Layout 1             | `921d6f04777a`  |
| 794    | No documented layout | `921d6f04777a`  |
| 787    | No documented layout | `921d6f04777a`  |
| 780    | No documented layout | `921d6f04777a`  |
| 771    | No documented layout | `921d6f04777a`  |
| 760    | No file              | `921d6f04777a`  |
| 748    | No file              | `921d6f04777a`  |
| 741    | No file              | `921d6f04777a`  |
| 736    | No file              | `921d6f04777a`  |
| 731    | No file              | `921d6f04777a`  |
| 723    | No file              | `921d6f04777a`  |
| 711    | No file              | `921d6f04777a`  |
| 707    | No file              | `921d6f04777a`  |
| 697    | No file              | `921d6f04777a`  |
| 689    | No file              | `921d6f04777a`  |
| 683    | No file              | `921d6f04777a`  |
| 678    | No file              | `921d6f04777a`  |
| 670    | No file              | `921d6f04777a`  |
| 661    | No file              | `921d6f04777a`  |
| 656    | No file              | `921d6f04777a`  |
| 652    | No file              | `921d6f04777a`  |
| 643    | No file              | `921d6f04777a`  |
| 637    | No file              | `921d6f04777a`  |
| 630    | No file              | `921d6f04777a`  |
| 627    | No file              | `921d6f04777a`  |
| 621    | No file              | `921d6f04777a`  |
| 617    | No file              | `921d6f04777a`  |
| 615    | No file              | `921d6f04777a`  |
| 606    | No file              | `921d6f04777a`  |
| 599    | No file              | `921d6f04777a`  |
| 592    | No file              | `921d6f04777a`  |
| 586    | No file              | `921d6f04777a`  |
| 577    | No file              | `921d6f04777a`  |
| 569    | No file              | `921d6f04777a`  |
| 561    | No file              | `921d6f04777a`  |
| 554    | No file              | `921d6f04777a`  |
| 542    | No file              | `921d6f04777a`  |
| 532    | No file              | `921d6f04777a`  |
| 531    | No file              | `921d6f04777a`  |
| 526    | No file              | `921d6f04777a`  |
| 521    | No file              | `921d6f04777a`  |
| 517    | No file              | `921d6f04777a`  |
| 510    | No file              | `921d6f04777a`  |
| 508    | No file              | `921d6f04777a`  |
| 504    | No file              | `921d6f04777a`  |
| 497    | No file              | `921d6f04777a`  |
| 491    | No file              | `921d6f04777a`  |
| 485    | No file              | `921d6f04777a`  |
| 478    | No file              | `921d6f04777a`  |
| 472    | No file              | `921d6f04777a`  |
| 466    | No file              | `921d6f04777a`  |
| 457    | No file              | `921d6f04777a`  |
| 452    | No file              | `921d6f04777a`  |
| 449    | No file              | `921d6f04777a`  |
| 435    | No file              | `921d6f04777a`  |

<!-- versions:end -->

## Companion Files

| File            | Required | Role                                                                      |
| --------------- | -------- | ------------------------------------------------------------------------- |
| `fieldinfo.bss` | Optional | `world_start_x` and `world_start_z` of the folder's field, for the world corner of each square |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR with no row count: the squares run up to the string table, whose
offset the trailer holds. An empty list is 16 bytes,
`50 41 42 52 00 00 00 00 04 00 00 00 00 00 00 00`.

| Offset         | Type                  | Field        | Notes                                             |
| -------------- | --------------------- | ------------ | ------------------------------------------------- |
| `+0x00`        | char[4]               | magic        | ASCII `PABR`                                      |
| `+0x04`        | Square[..table_start] | squares      | Squares back to back until `table_start`; see Square |
| `squares+0x00` | String Table          | string_table | See String Table                                  |
| `EOF-0x08`     | u32                   | table_start  | Offset of the string table, where `squares` ends  |
| `EOF-0x04`     | u32                   | zero         | Always `0`                                        |

### Square (4 bytes)

| Offset  | Type | Field  | Notes                                   |
| ------- | ---- | ------ | --------------------------------------- |
| `+0x00` | u16  | grid_x | Field grid square column, as in `x_y.bss` |
| `+0x02` | u16  | grid_z | Field grid square row                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | `0` in every file       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Field Names

The 2016 client's debug symbols name the pair `gc::FieldGridSectorIndex`
(u16 `_x`, u16 `_z`). The names `grid_x` and `grid_z` match the square
fields of [x_y.bss](x_y_bss.md): on client 3482 each file lists exactly the
squares its folder's cell files hold, each once (13,121 squares in the three
folders with cells).

## Notes

- The squares are not sorted; the field `1` list of client 3482 starts at
  (131, 636).
- A private server's copy of `spawnplacementfieldgrid/1/7/` on client 1784
  lists 9,664 squares; the client 1784 test client holds no `mapdata_*`
  files.
