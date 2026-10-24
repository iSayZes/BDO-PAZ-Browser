# `fileinfo.bss` Format

## Purpose

The list of [x_y.bss](x_y_bss.md) cell files in one spawn grid folder
`mapdata_<resource>/spawnplacementfieldgrid/<field_no>/7/`. Each entry is
the first grid square of a cell file, the two numbers of its name
(`553_364.bss`). On client 3482 the field `1` file lists 1,430 cells,
field `700` 1 and field `701` 2; the 66 `A1_` fields `4001` to `4066` have
an empty list and no cell files.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                                                    | Bytes | Records    | Row bytes |
| ------ | ------------- | ------- | ------------------------------------------------------- | ----- | ---------- | --------- |
| 1      | 805 and later | 3483    | `mapdata_real/spawnplacementfieldgrid/1/7/fileinfo.bss` | 5,736 | 1,430 Cell | 4         |

| Layout | File                                                    | Known            | Unknown    |
| ------ | ------------------------------------------------------- | ---------------- | ---------- |
| 1      | `mapdata_real/spawnplacementfieldgrid/1/7/fileinfo.bss` | 5,736 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `4075c4d1f87f`  |
| 3482   | No file              | `4075c4d1f87f`  |
| 3474   | Layout 1             | `4075c4d1f87f`  |
| 3473   | Layout 1             | `4075c4d1f87f`  |
| 3464   | Layout 1             | `4075c4d1f87f`  |
| 3458   | Layout 1             | `4075c4d1f87f`  |
| 3454   | Layout 1             | `4075c4d1f87f`  |
| 3444   | Layout 1             | `4075c4d1f87f`  |
| 3435   | Layout 1             | `4075c4d1f87f`  |
| 3426   | Layout 1             | `4075c4d1f87f`  |
| 3418   | Layout 1             | `4075c4d1f87f`  |
| 3412   | Layout 1             | `4075c4d1f87f`  |
| 3402   | Layout 1             | `4075c4d1f87f`  |
| 3396   | Layout 1             | `4075c4d1f87f`  |
| 3387   | Layout 1             | `4075c4d1f87f`  |
| 3381   | Layout 1             | `4075c4d1f87f`  |
| 3373   | Layout 1             | `4075c4d1f87f`  |
| 3364   | Layout 1             | `4075c4d1f87f`  |
| 3356   | Layout 1             | `4075c4d1f87f`  |
| 3349   | Layout 1             | `4075c4d1f87f`  |
| 3342   | Layout 1             | `4075c4d1f87f`  |
| 3335   | Layout 1             | `4075c4d1f87f`  |
| 3326   | Layout 1             | `4075c4d1f87f`  |
| 3321   | Layout 1             | `4075c4d1f87f`  |
| 3314   | Layout 1             | `4075c4d1f87f`  |
| 3303   | Layout 1             | `4075c4d1f87f`  |
| 3302   | Layout 1             | `4075c4d1f87f`  |
| 3293   | Layout 1             | `4075c4d1f87f`  |
| 3283   | Layout 1             | `4075c4d1f87f`  |
| 3275   | Layout 1             | `4075c4d1f87f`  |
| 3267   | Layout 1             | `4075c4d1f87f`  |
| 3258   | Layout 1             | `4075c4d1f87f`  |
| 3251   | Layout 1             | `4075c4d1f87f`  |
| 3242   | Layout 1             | `4075c4d1f87f`  |
| 3235   | Layout 1             | `4075c4d1f87f`  |
| 3229   | Layout 1             | `4075c4d1f87f`  |
| 3212   | Layout 1             | `4075c4d1f87f`  |
| 3203   | Layout 1             | `4075c4d1f87f`  |
| 3193   | Layout 1             | `4075c4d1f87f`  |
| 3186   | Layout 1             | `4075c4d1f87f`  |
| 3177   | Layout 1             | `4075c4d1f87f`  |
| 3169   | Layout 1             | `4075c4d1f87f`  |
| 3158   | Layout 1             | `4075c4d1f87f`  |
| 3151   | Layout 1             | `4075c4d1f87f`  |
| 3144   | Layout 1             | `4075c4d1f87f`  |
| 3133   | Layout 1             | `4075c4d1f87f`  |
| 3125   | Layout 1             | `4075c4d1f87f`  |
| 3118   | Layout 1             | `4075c4d1f87f`  |
| 3111   | Layout 1             | `4075c4d1f87f`  |
| 3103   | Layout 1             | `4075c4d1f87f`  |
| 3095   | Layout 1             | `4075c4d1f87f`  |
| 3086   | Layout 1             | `4075c4d1f87f`  |
| 3072   | Layout 1             | `4075c4d1f87f`  |
| 3062   | Layout 1             | `4075c4d1f87f`  |
| 3052   | Layout 1             | `4075c4d1f87f`  |
| 3045   | Layout 1             | `4075c4d1f87f`  |
| 3037   | Layout 1             | `4075c4d1f87f`  |
| 3030   | Layout 1             | `4075c4d1f87f`  |
| 3021   | Layout 1             | `4075c4d1f87f`  |
| 3012   | Layout 1             | `4075c4d1f87f`  |
| 3002   | Layout 1             | `4075c4d1f87f`  |
| 2995   | Layout 1             | `4075c4d1f87f`  |
| 2987   | Layout 1             | `4075c4d1f87f`  |
| 2978   | Layout 1             | `4075c4d1f87f`  |
| 2970   | Layout 1             | `4075c4d1f87f`  |
| 2959   | Layout 1             | `4075c4d1f87f`  |
| 2951   | Layout 1             | `4075c4d1f87f`  |
| 2942   | Layout 1             | `4075c4d1f87f`  |
| 2935   | Layout 1             | `4075c4d1f87f`  |
| 2932   | Layout 1             | `4075c4d1f87f`  |
| 2923   | Layout 1             | `4075c4d1f87f`  |
| 2919   | Layout 1             | `4075c4d1f87f`  |
| 2907   | Layout 1             | `4075c4d1f87f`  |
| 2900   | Layout 1             | `4075c4d1f87f`  |
| 2891   | Layout 1             | `4075c4d1f87f`  |
| 2882   | Layout 1             | `4075c4d1f87f`  |
| 2872   | Layout 1             | `4075c4d1f87f`  |
| 2863   | Layout 1             | `4075c4d1f87f`  |
| 2855   | Layout 1             | `4075c4d1f87f`  |
| 2849   | Layout 1             | `4075c4d1f87f`  |
| 2844   | Layout 1             | `4075c4d1f87f`  |
| 2834   | Layout 1             | `4075c4d1f87f`  |
| 2825   | Layout 1             | `4075c4d1f87f`  |
| 2819   | Layout 1             | `4075c4d1f87f`  |
| 2811   | Layout 1             | `4075c4d1f87f`  |
| 2803   | Layout 1             | `4075c4d1f87f`  |
| 2794   | Layout 1             | `4075c4d1f87f`  |
| 2783   | Layout 1             | `4075c4d1f87f`  |
| 2774   | Layout 1             | `4075c4d1f87f`  |
| 2765   | Layout 1             | `4075c4d1f87f`  |
| 2756   | Layout 1             | `4075c4d1f87f`  |
| 2750   | Layout 1             | `4075c4d1f87f`  |
| 2743   | Layout 1             | `4075c4d1f87f`  |
| 2736   | Layout 1             | `4075c4d1f87f`  |
| 2726   | Layout 1             | `4075c4d1f87f`  |
| 2717   | Layout 1             | `4075c4d1f87f`  |
| 2709   | Layout 1             | `4075c4d1f87f`  |
| 2703   | Layout 1             | `4075c4d1f87f`  |
| 2695   | Layout 1             | `4075c4d1f87f`  |
| 2684   | Layout 1             | `4075c4d1f87f`  |
| 2672   | Layout 1             | `4075c4d1f87f`  |
| 2665   | Layout 1             | `4075c4d1f87f`  |
| 2657   | Layout 1             | `4075c4d1f87f`  |
| 2649   | Layout 1             | `4075c4d1f87f`  |
| 2644   | Layout 1             | `4075c4d1f87f`  |
| 2637   | Layout 1             | `4075c4d1f87f`  |
| 2629   | Layout 1             | `4075c4d1f87f`  |
| 2619   | Layout 1             | `4075c4d1f87f`  |
| 2612   | Layout 1             | `4075c4d1f87f`  |
| 2606   | Layout 1             | `4075c4d1f87f`  |
| 2602   | Layout 1             | `4075c4d1f87f`  |
| 2601   | Layout 1             | `4075c4d1f87f`  |
| 2592   | Layout 1             | `4075c4d1f87f`  |
| 2583   | Layout 1             | `4075c4d1f87f`  |
| 2575   | Layout 1             | `4075c4d1f87f`  |
| 2567   | Layout 1             | `4075c4d1f87f`  |
| 2560   | Layout 1             | `4075c4d1f87f`  |
| 2553   | Layout 1             | `4075c4d1f87f`  |
| 2545   | Layout 1             | `4075c4d1f87f`  |
| 2538   | Layout 1             | `4075c4d1f87f`  |
| 2529   | Layout 1             | `4075c4d1f87f`  |
| 2519   | Layout 1             | `4075c4d1f87f`  |
| 2513   | Layout 1             | `4075c4d1f87f`  |
| 2510   | Layout 1             | `4075c4d1f87f`  |
| 2507   | Layout 1             | `4075c4d1f87f`  |
| 2503   | Layout 1             | `4075c4d1f87f`  |
| 2498   | Layout 1             | `4075c4d1f87f`  |
| 2492   | Layout 1             | `4075c4d1f87f`  |
| 2487   | Layout 1             | `4075c4d1f87f`  |
| 2480   | Layout 1             | `4075c4d1f87f`  |
| 2474   | Layout 1             | `4075c4d1f87f`  |
| 2468   | Layout 1             | `4075c4d1f87f`  |
| 2460   | Layout 1             | `4075c4d1f87f`  |
| 2453   | Layout 1             | `4075c4d1f87f`  |
| 2444   | Layout 1             | `4075c4d1f87f`  |
| 2438   | Layout 1             | `4075c4d1f87f`  |
| 2434   | Layout 1             | `4075c4d1f87f`  |
| 2429   | Layout 1             | `4075c4d1f87f`  |
| 2421   | Layout 1             | `4075c4d1f87f`  |
| 2414   | Layout 1             | `4075c4d1f87f`  |
| 2407   | Layout 1             | `4075c4d1f87f`  |
| 2401   | Layout 1             | `4075c4d1f87f`  |
| 2397   | Layout 1             | `4075c4d1f87f`  |
| 2393   | Layout 1             | `4075c4d1f87f`  |
| 2384   | Layout 1             | `4075c4d1f87f`  |
| 2378   | Layout 1             | `4075c4d1f87f`  |
| 2372   | Layout 1             | `4075c4d1f87f`  |
| 2358   | Layout 1             | `4075c4d1f87f`  |
| 2352   | Layout 1             | `4075c4d1f87f`  |
| 2347   | Layout 1             | `4075c4d1f87f`  |
| 2343   | Layout 1             | `4075c4d1f87f`  |
| 2335   | Layout 1             | `4075c4d1f87f`  |
| 2327   | Layout 1             | `4075c4d1f87f`  |
| 2324   | Layout 1             | `4075c4d1f87f`  |
| 2319   | Layout 1             | `4075c4d1f87f`  |
| 2313   | Layout 1             | `4075c4d1f87f`  |
| 2308   | Layout 1             | `4075c4d1f87f`  |
| 2302   | Layout 1             | `4075c4d1f87f`  |
| 2295   | Layout 1             | `4075c4d1f87f`  |
| 2290   | Layout 1             | `4075c4d1f87f`  |
| 2284   | Layout 1             | `4075c4d1f87f`  |
| 2276   | Layout 1             | `4075c4d1f87f`  |
| 2269   | Layout 1             | `4075c4d1f87f`  |
| 2259   | Layout 1             | `4075c4d1f87f`  |
| 2250   | Layout 1             | `4075c4d1f87f`  |
| 2243   | Layout 1             | `4075c4d1f87f`  |
| 2235   | Layout 1             | `4075c4d1f87f`  |
| 2229   | Layout 1             | `4075c4d1f87f`  |
| 2224   | Layout 1             | `4075c4d1f87f`  |
| 2218   | Layout 1             | `4075c4d1f87f`  |
| 2215   | Layout 1             | `4075c4d1f87f`  |
| 2207   | Layout 1             | `4075c4d1f87f`  |
| 2203   | Layout 1             | `4075c4d1f87f`  |
| 2196   | Layout 1             | `4075c4d1f87f`  |
| 2192   | Layout 1             | `4075c4d1f87f`  |
| 2189   | Layout 1             | `4075c4d1f87f`  |
| 2183   | Layout 1             | `4075c4d1f87f`  |
| 2179   | Layout 1             | `4075c4d1f87f`  |
| 2171   | Layout 1             | `4075c4d1f87f`  |
| 2163   | Layout 1             | `4075c4d1f87f`  |
| 2156   | Layout 1             | `4075c4d1f87f`  |
| 2151   | Layout 1             | `4075c4d1f87f`  |
| 2147   | Layout 1             | `4075c4d1f87f`  |
| 2142   | Layout 1             | `4075c4d1f87f`  |
| 2138   | Layout 1             | `4075c4d1f87f`  |
| 2134   | Layout 1             | `4075c4d1f87f`  |
| 2130   | Layout 1             | `4075c4d1f87f`  |
| 2122   | Layout 1             | `4075c4d1f87f`  |
| 2107   | Layout 1             | `4075c4d1f87f`  |
| 2098   | Layout 1             | `4075c4d1f87f`  |
| 2089   | Layout 1             | `4075c4d1f87f`  |
| 2081   | Layout 1             | `4075c4d1f87f`  |
| 2073   | Layout 1             | `4075c4d1f87f`  |
| 2067   | Layout 1             | `4075c4d1f87f`  |
| 2063   | Layout 1             | `4075c4d1f87f`  |
| 2059   | Layout 1             | `4075c4d1f87f`  |
| 2052   | Layout 1             | `4075c4d1f87f`  |
| 2044   | Layout 1             | `4075c4d1f87f`  |
| 2039   | Layout 1             | `4075c4d1f87f`  |
| 2032   | Layout 1             | `4075c4d1f87f`  |
| 2025   | Layout 1             | `4075c4d1f87f`  |
| 2011   | Layout 1             | `4075c4d1f87f`  |
| 2005   | Layout 1             | `4075c4d1f87f`  |
| 2000   | Layout 1             | `4075c4d1f87f`  |
| 1996   | Layout 1             | `4075c4d1f87f`  |
| 1991   | Layout 1             | `4075c4d1f87f`  |
| 1985   | Layout 1             | `4075c4d1f87f`  |
| 1980   | Layout 1             | `4075c4d1f87f`  |
| 1969   | Layout 1             | `4075c4d1f87f`  |
| 1964   | Layout 1             | `4075c4d1f87f`  |
| 1958   | Layout 1             | `4075c4d1f87f`  |
| 1950   | Layout 1             | `4075c4d1f87f`  |
| 1945   | Layout 1             | `4075c4d1f87f`  |
| 1937   | Layout 1             | `4075c4d1f87f`  |
| 1933   | Layout 1             | `4075c4d1f87f`  |
| 1927   | Layout 1             | `4075c4d1f87f`  |
| 1921   | Layout 1             | `4075c4d1f87f`  |
| 1914   | Layout 1             | `4075c4d1f87f`  |
| 1908   | Layout 1             | `4075c4d1f87f`  |
| 1897   | Layout 1             | `4075c4d1f87f`  |
| 1892   | Layout 1             | `4075c4d1f87f`  |
| 1886   | Layout 1             | `4075c4d1f87f`  |
| 1881   | Layout 1             | `4075c4d1f87f`  |
| 1871   | Layout 1             | `4075c4d1f87f`  |
| 1866   | Layout 1             | `4075c4d1f87f`  |
| 1862   | Layout 1             | `4075c4d1f87f`  |
| 1854   | Layout 1             | `4075c4d1f87f`  |
| 1846   | Layout 1             | `4075c4d1f87f`  |
| 1838   | Layout 1             | `4075c4d1f87f`  |
| 1832   | Layout 1             | `4075c4d1f87f`  |
| 1826   | Layout 1             | `4075c4d1f87f`  |
| 1822   | Layout 1             | `4075c4d1f87f`  |
| 1818   | Layout 1             | `4075c4d1f87f`  |
| 1804   | Layout 1             | `4075c4d1f87f`  |
| 1794   | Layout 1             | `4075c4d1f87f`  |
| 1790   | Layout 1             | `4075c4d1f87f`  |
| 1784   | Layout 1             | `4075c4d1f87f`  |
| 1774   | Layout 1             | `4075c4d1f87f`  |
| 1771   | Layout 1             | `4075c4d1f87f`  |
| 1762   | Layout 1             | `4075c4d1f87f`  |
| 1759   | Layout 1             | `4075c4d1f87f`  |
| 1754   | Layout 1             | `4075c4d1f87f`  |
| 1749   | Layout 1             | `4075c4d1f87f`  |
| 1743   | Layout 1             | `4075c4d1f87f`  |
| 1737   | Layout 1             | `4075c4d1f87f`  |
| 1731   | Layout 1             | `4075c4d1f87f`  |
| 1725   | Layout 1             | `4075c4d1f87f`  |
| 1717   | Layout 1             | `4075c4d1f87f`  |
| 1710   | Layout 1             | `4075c4d1f87f`  |
| 1704   | Layout 1             | `4075c4d1f87f`  |
| 1698   | Layout 1             | `4075c4d1f87f`  |
| 1690   | Layout 1             | `4075c4d1f87f`  |
| 1685   | Layout 1             | `4075c4d1f87f`  |
| 1680   | Layout 1             | `4075c4d1f87f`  |
| 1674   | Layout 1             | `4075c4d1f87f`  |
| 1668   | Layout 1             | `4075c4d1f87f`  |
| 1659   | Layout 1             | `4075c4d1f87f`  |
| 1649   | Layout 1             | `4075c4d1f87f`  |
| 1642   | Layout 1             | `4075c4d1f87f`  |
| 1636   | Layout 1             | `4075c4d1f87f`  |
| 1628   | Layout 1             | `4075c4d1f87f`  |
| 1622   | Layout 1             | `4075c4d1f87f`  |
| 1614   | Layout 1             | `4075c4d1f87f`  |
| 1608   | Layout 1             | `4075c4d1f87f`  |
| 1602   | Layout 1             | `4075c4d1f87f`  |
| 1598   | Layout 1             | `4075c4d1f87f`  |
| 1594   | Layout 1             | `4075c4d1f87f`  |
| 1590   | Layout 1             | `4075c4d1f87f`  |
| 1587   | Layout 1             | `4075c4d1f87f`  |
| 1584   | Layout 1             | `4075c4d1f87f`  |
| 1579   | Layout 1             | `4075c4d1f87f`  |
| 1572   | Layout 1             | `4075c4d1f87f`  |
| 1565   | Layout 1             | `4075c4d1f87f`  |
| 1559   | Layout 1             | `4075c4d1f87f`  |
| 1554   | Layout 1             | `4075c4d1f87f`  |
| 1547   | Layout 1             | `4075c4d1f87f`  |
| 1537   | Layout 1             | `4075c4d1f87f`  |
| 1529   | Layout 1             | `4075c4d1f87f`  |
| 1524   | Layout 1             | `4075c4d1f87f`  |
| 1519   | Layout 1             | `4075c4d1f87f`  |
| 1509   | Layout 1             | `4075c4d1f87f`  |
| 1506   | Layout 1             | `4075c4d1f87f`  |
| 1504   | Layout 1             | `4075c4d1f87f`  |
| 1500   | Layout 1             | `4075c4d1f87f`  |
| 1493   | Layout 1             | `4075c4d1f87f`  |
| 1489   | Layout 1             | `4075c4d1f87f`  |
| 1485   | Layout 1             | `4075c4d1f87f`  |
| 1481   | Layout 1             | `4075c4d1f87f`  |
| 1474   | Layout 1             | `4075c4d1f87f`  |
| 1466   | Layout 1             | `4075c4d1f87f`  |
| 1462   | Layout 1             | `4075c4d1f87f`  |
| 1459   | Layout 1             | `4075c4d1f87f`  |
| 1453   | Layout 1             | `4075c4d1f87f`  |
| 1450   | Layout 1             | `4075c4d1f87f`  |
| 1445   | Layout 1             | `4075c4d1f87f`  |
| 1439   | Layout 1             | `4075c4d1f87f`  |
| 1433   | Layout 1             | `4075c4d1f87f`  |
| 1430   | Layout 1             | `4075c4d1f87f`  |
| 1426   | Layout 1             | `4075c4d1f87f`  |
| 1421   | Layout 1             | `4075c4d1f87f`  |
| 1417   | Layout 1             | `4075c4d1f87f`  |
| 1416   | Layout 1             | `4075c4d1f87f`  |
| 1409   | Layout 1             | `4075c4d1f87f`  |
| 1405   | Layout 1             | `4075c4d1f87f`  |
| 1401   | Layout 1             | `4075c4d1f87f`  |
| 1396   | Layout 1             | `4075c4d1f87f`  |
| 1391   | Layout 1             | `4075c4d1f87f`  |
| 1390   | Layout 1             | `4075c4d1f87f`  |
| 1386   | Layout 1             | `4075c4d1f87f`  |
| 1381   | Layout 1             | `4075c4d1f87f`  |
| 1379   | Layout 1             | `4075c4d1f87f`  |
| 1372   | Layout 1             | `4075c4d1f87f`  |
| 1366   | Layout 1             | `4075c4d1f87f`  |
| 1364   | Layout 1             | `4075c4d1f87f`  |
| 1363   | Layout 1             | `4075c4d1f87f`  |
| 1360   | Layout 1             | `4075c4d1f87f`  |
| 1358   | Layout 1             | `4075c4d1f87f`  |
| 1355   | Layout 1             | `4075c4d1f87f`  |
| 1351   | Layout 1             | `4075c4d1f87f`  |
| 1348   | Layout 1             | `4075c4d1f87f`  |
| 1346   | Layout 1             | `4075c4d1f87f`  |
| 1341   | Layout 1             | `4075c4d1f87f`  |
| 1340   | Layout 1             | `4075c4d1f87f`  |
| 1338   | Layout 1             | `4075c4d1f87f`  |
| 1335   | Layout 1             | `4075c4d1f87f`  |
| 1333   | Layout 1             | `4075c4d1f87f`  |
| 1329   | Layout 1             | `4075c4d1f87f`  |
| 1327   | Layout 1             | `4075c4d1f87f`  |
| 1324   | Layout 1             | `4075c4d1f87f`  |
| 1321   | Layout 1             | `4075c4d1f87f`  |
| 1319   | Layout 1             | `4075c4d1f87f`  |
| 1318   | Layout 1             | `4075c4d1f87f`  |
| 1316   | Layout 1             | `4075c4d1f87f`  |
| 1313   | Layout 1             | `4075c4d1f87f`  |
| 1311   | Layout 1             | `4075c4d1f87f`  |
| 1309   | Layout 1             | `4075c4d1f87f`  |
| 1304   | Layout 1             | `4075c4d1f87f`  |
| 1292   | Layout 1             | `4075c4d1f87f`  |
| 1286   | Layout 1             | `4075c4d1f87f`  |
| 1280   | Layout 1             | `4075c4d1f87f`  |
| 1276   | Layout 1             | `4075c4d1f87f`  |
| 1267   | Layout 1             | `4075c4d1f87f`  |
| 1261   | Layout 1             | `4075c4d1f87f`  |
| 1256   | Layout 1             | `4075c4d1f87f`  |
| 1250   | Layout 1             | `4075c4d1f87f`  |
| 1246   | Layout 1             | `4075c4d1f87f`  |
| 1239   | Layout 1             | `4075c4d1f87f`  |
| 1230   | Layout 1             | `4075c4d1f87f`  |
| 1226   | Layout 1             | `4075c4d1f87f`  |
| 1220   | Layout 1             | `4075c4d1f87f`  |
| 1217   | Layout 1             | `4075c4d1f87f`  |
| 1211   | Layout 1             | `4075c4d1f87f`  |
| 1210   | Layout 1             | `4075c4d1f87f`  |
| 1208   | Layout 1             | `4075c4d1f87f`  |
| 1203   | Layout 1             | `4075c4d1f87f`  |
| 1197   | Layout 1             | `4075c4d1f87f`  |
| 1194   | Layout 1             | `4075c4d1f87f`  |
| 1192   | Layout 1             | `4075c4d1f87f`  |
| 1187   | Layout 1             | `4075c4d1f87f`  |
| 1183   | Layout 1             | `4075c4d1f87f`  |
| 1177   | Layout 1             | `4075c4d1f87f`  |
| 1173   | Layout 1             | `4075c4d1f87f`  |
| 1167   | Layout 1             | `4075c4d1f87f`  |
| 1164   | Layout 1             | `4075c4d1f87f`  |
| 1156   | Layout 1             | `4075c4d1f87f`  |
| 1149   | Layout 1             | `4075c4d1f87f`  |
| 1144   | Layout 1             | `4075c4d1f87f`  |
| 1137   | Layout 1             | `4075c4d1f87f`  |
| 1132   | Layout 1             | `4075c4d1f87f`  |
| 1127   | Layout 1             | `4075c4d1f87f`  |
| 1122   | Layout 1             | `4075c4d1f87f`  |
| 1118   | Layout 1             | `4075c4d1f87f`  |
| 1114   | Layout 1             | `4075c4d1f87f`  |
| 1109   | Layout 1             | `4075c4d1f87f`  |
| 1102   | Layout 1             | `4075c4d1f87f`  |
| 1096   | Layout 1             | `4075c4d1f87f`  |
| 1088   | Layout 1             | `4075c4d1f87f`  |
| 1081   | Layout 1             | `4075c4d1f87f`  |
| 1076   | Layout 1             | `4075c4d1f87f`  |
| 1069   | Layout 1             | `4075c4d1f87f`  |
| 1064   | Layout 1             | `4075c4d1f87f`  |
| 1058   | Layout 1             | `4075c4d1f87f`  |
| 1051   | Layout 1             | `4075c4d1f87f`  |
| 1044   | Layout 1             | `4075c4d1f87f`  |
| 1036   | Layout 1             | `4075c4d1f87f`  |
| 1026   | Layout 1             | `4075c4d1f87f`  |
| 1016   | Layout 1             | `4075c4d1f87f`  |
| 1009   | Layout 1             | `4075c4d1f87f`  |
| 1005   | Layout 1             | `4075c4d1f87f`  |
| 1000   | Layout 1             | `4075c4d1f87f`  |
| 998    | Layout 1             | `4075c4d1f87f`  |
| 990    | Layout 1             | `4075c4d1f87f`  |
| 979    | Layout 1             | `4075c4d1f87f`  |
| 972    | Layout 1             | `4075c4d1f87f`  |
| 963    | Layout 1             | `4075c4d1f87f`  |
| 955    | Layout 1             | `4075c4d1f87f`  |
| 946    | Layout 1             | `4075c4d1f87f`  |
| 938    | Layout 1             | `4075c4d1f87f`  |
| 927    | Layout 1             | `4075c4d1f87f`  |
| 911    | Layout 1             | `4075c4d1f87f`  |
| 904    | Layout 1             | `4075c4d1f87f`  |
| 899    | Layout 1             | `4075c4d1f87f`  |
| 894    | Layout 1             | `4075c4d1f87f`  |
| 885    | Layout 1             | `4075c4d1f87f`  |
| 879    | Layout 1             | `4075c4d1f87f`  |
| 872    | Layout 1             | `4075c4d1f87f`  |
| 864    | Layout 1             | `4075c4d1f87f`  |
| 855    | Layout 1             | `4075c4d1f87f`  |
| 853    | Layout 1             | `4075c4d1f87f`  |
| 845    | Layout 1             | `4075c4d1f87f`  |
| 837    | Layout 1             | `4075c4d1f87f`  |
| 829    | Layout 1             | `4075c4d1f87f`  |
| 822    | Layout 1             | `4075c4d1f87f`  |
| 814    | Layout 1             | `4075c4d1f87f`  |
| 805    | Layout 1             | `4075c4d1f87f`  |
| 794    | No documented layout | `4075c4d1f87f`  |
| 787    | No documented layout | `4075c4d1f87f`  |
| 780    | No documented layout | `4075c4d1f87f`  |
| 771    | No documented layout | `4075c4d1f87f`  |
| 760    | No file              | `4075c4d1f87f`  |
| 748    | No file              | `4075c4d1f87f`  |
| 741    | No file              | `4075c4d1f87f`  |
| 736    | No file              | `4075c4d1f87f`  |
| 731    | No file              | `4075c4d1f87f`  |
| 723    | No file              | `4075c4d1f87f`  |
| 711    | No file              | `4075c4d1f87f`  |
| 707    | No file              | `4075c4d1f87f`  |
| 697    | No file              | `4075c4d1f87f`  |
| 689    | No file              | `4075c4d1f87f`  |
| 683    | No file              | `4075c4d1f87f`  |
| 678    | No file              | `4075c4d1f87f`  |
| 670    | No file              | `4075c4d1f87f`  |
| 661    | No file              | `4075c4d1f87f`  |
| 656    | No file              | `4075c4d1f87f`  |
| 652    | No file              | `4075c4d1f87f`  |
| 643    | No file              | `4075c4d1f87f`  |
| 637    | No file              | `4075c4d1f87f`  |
| 630    | No file              | `4075c4d1f87f`  |
| 627    | No file              | `4075c4d1f87f`  |
| 621    | No file              | `4075c4d1f87f`  |
| 617    | No file              | `4075c4d1f87f`  |
| 615    | No file              | `4075c4d1f87f`  |
| 606    | No file              | `4075c4d1f87f`  |
| 599    | No file              | `4075c4d1f87f`  |
| 592    | No file              | `4075c4d1f87f`  |
| 586    | No file              | `4075c4d1f87f`  |
| 577    | No file              | `4075c4d1f87f`  |
| 569    | No file              | `4075c4d1f87f`  |
| 561    | No file              | `4075c4d1f87f`  |
| 554    | No file              | `4075c4d1f87f`  |
| 542    | No file              | `4075c4d1f87f`  |
| 532    | No file              | `4075c4d1f87f`  |
| 531    | No file              | `4075c4d1f87f`  |
| 526    | No file              | `4075c4d1f87f`  |
| 521    | No file              | `4075c4d1f87f`  |
| 517    | No file              | `4075c4d1f87f`  |
| 510    | No file              | `4075c4d1f87f`  |
| 508    | No file              | `4075c4d1f87f`  |
| 504    | No file              | `4075c4d1f87f`  |
| 497    | No file              | `4075c4d1f87f`  |
| 491    | No file              | `4075c4d1f87f`  |
| 485    | No file              | `4075c4d1f87f`  |
| 478    | No file              | `4075c4d1f87f`  |
| 472    | No file              | `4075c4d1f87f`  |
| 466    | No file              | `4075c4d1f87f`  |
| 457    | No file              | `4075c4d1f87f`  |
| 452    | No file              | `4075c4d1f87f`  |
| 449    | No file              | `4075c4d1f87f`  |
| 435    | No file              | `4075c4d1f87f`  |

<!-- versions:end -->

## Companion Files

| File            | Required | Role                                                                      |
| --------------- | -------- | ------------------------------------------------------------------------- |
| `fieldinfo.bss` | Optional | `world_start_x` and `world_start_z` of the folder's field, for the world corner of each cell |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR with no row count: the cells run up to the string table, whose offset
the trailer holds. An empty list is 16 bytes,
`50 41 42 52 00 00 00 00 04 00 00 00 00 00 00 00`.

| Offset       | Type                | Field        | Notes                                           |
| ------------ | ------------------- | ------------ | ----------------------------------------------- |
| `+0x00`      | char[4]             | magic        | ASCII `PABR`                                    |
| `+0x04`      | Cell[..table_start] | cells        | Cells back to back until `table_start`; see Cell |
| `cells+0x00` | String Table        | string_table | See String Table                                |
| `EOF-0x08`   | u32                 | table_start  | Offset of the string table, where `cells` ends  |
| `EOF-0x04`   | u32                 | zero         | Always `0`                                      |

### Cell (4 bytes)

| Offset  | Type | Field  | Notes                                                        |
| ------- | ---- | ------ | ------------------------------------------------------------ |
| `+0x00` | u16  | cell_x | First grid square column of the cell, a multiple of 7; the `x` of `<x>_<z>.bss` |
| `+0x02` | u16  | cell_z | First grid square row of the cell, a multiple of 7; the `z`  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | `0` in every file       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Field Names

On client 3482 each list names exactly the cell files of its folder, each
once (1,433 cells in the three folders with cells). A cell covers 7 x 7
grid squares from (`cell_x`, `cell_z`); see
[Grid Squares](x_y_bss.md#grid-squares).

## Notes

- The cells are not sorted; the field `1` list of client 3482 starts at
  `126_630.bss`.
- A private server's copy of `spawnplacementfieldgrid/1/7/` on client 1784
  lists 1,015 cells; the client 1784 test client holds no `mapdata_*`
  files.
