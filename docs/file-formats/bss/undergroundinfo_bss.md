# `undergroundinfo.bss` Format

## Purpose

The drop areas of the server's underground bitmap. A PABR list of
colours; each row is one colour key of the bitmap and bytes that are `0`
on every row, where the source sheet has a drop ID. On client 3482 it
holds 29 colours. The client 1784 sheet notes name what each area drops:
gold bars, ores and muddy water pouches by level, quest items, and
treasure maps for harpoon fishing.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------- | ----- | ------- | --------- |
| 3      | 2726 and later | `undergroundinfo.bss` | 368   | 29 Row  | 12        |
| 2      | 805 to 2717    | `undergroundinfo.bss` | 310   | 29 Row  | 10        |
| 1      | 435 to 794     | `undergroundinfo.bss` | 284   | 28 Row  | 10        |

| Layout | File                  | Known         | Unknown       |
| ------ | --------------------- | ------------- | ------------- |
| 3      | `undergroundinfo.bss` | 107 B (29.1%) | 261 B (70.9%) |
| 2      | `undergroundinfo.bss` | 107 B (34.5%) | 203 B (65.5%) |
| 1      | `undergroundinfo.bss` | 88 B (31.0%)  | 196 B (69.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `4b12cd52ee21`  |
| 3482   | Layout 3 | `4b12cd52ee21`  |
| 3474   | Layout 3 | `4b12cd52ee21`  |
| 3473   | Layout 3 | `4b12cd52ee21`  |
| 3464   | Layout 3 | `4b12cd52ee21`  |
| 3458   | Layout 3 | `4b12cd52ee21`  |
| 3454   | Layout 3 | `4b12cd52ee21`  |
| 3444   | Layout 3 | `4b12cd52ee21`  |
| 3435   | Layout 3 | `4b12cd52ee21`  |
| 3426   | Layout 3 | `4b12cd52ee21`  |
| 3418   | Layout 3 | `4b12cd52ee21`  |
| 3412   | Layout 3 | `4b12cd52ee21`  |
| 3402   | Layout 3 | `4b12cd52ee21`  |
| 3396   | Layout 3 | `4b12cd52ee21`  |
| 3387   | Layout 3 | `4b12cd52ee21`  |
| 3381   | Layout 3 | `4b12cd52ee21`  |
| 3373   | Layout 3 | `4b12cd52ee21`  |
| 3364   | Layout 3 | `4b12cd52ee21`  |
| 3356   | Layout 3 | `4b12cd52ee21`  |
| 3349   | Layout 3 | `4b12cd52ee21`  |
| 3342   | Layout 3 | `4b12cd52ee21`  |
| 3335   | Layout 3 | `4b12cd52ee21`  |
| 3326   | Layout 3 | `4b12cd52ee21`  |
| 3321   | Layout 3 | `4b12cd52ee21`  |
| 3314   | Layout 3 | `4b12cd52ee21`  |
| 3303   | Layout 3 | `4b12cd52ee21`  |
| 3302   | Layout 3 | `4b12cd52ee21`  |
| 3293   | Layout 3 | `4b12cd52ee21`  |
| 3283   | Layout 3 | `4b12cd52ee21`  |
| 3275   | Layout 3 | `4b12cd52ee21`  |
| 3267   | Layout 3 | `4b12cd52ee21`  |
| 3258   | Layout 3 | `4b12cd52ee21`  |
| 3251   | Layout 3 | `4b12cd52ee21`  |
| 3242   | Layout 3 | `4b12cd52ee21`  |
| 3235   | Layout 3 | `4b12cd52ee21`  |
| 3229   | Layout 3 | `4b12cd52ee21`  |
| 3212   | Layout 3 | `4b12cd52ee21`  |
| 3203   | Layout 3 | `4b12cd52ee21`  |
| 3193   | Layout 3 | `4b12cd52ee21`  |
| 3186   | Layout 3 | `4b12cd52ee21`  |
| 3177   | Layout 3 | `4b12cd52ee21`  |
| 3169   | Layout 3 | `4b12cd52ee21`  |
| 3158   | Layout 3 | `4b12cd52ee21`  |
| 3151   | Layout 3 | `4b12cd52ee21`  |
| 3144   | Layout 3 | `4b12cd52ee21`  |
| 3133   | Layout 3 | `4b12cd52ee21`  |
| 3125   | Layout 3 | `4b12cd52ee21`  |
| 3118   | Layout 3 | `4b12cd52ee21`  |
| 3111   | Layout 3 | `4b12cd52ee21`  |
| 3103   | Layout 3 | `4b12cd52ee21`  |
| 3095   | Layout 3 | `4b12cd52ee21`  |
| 3086   | Layout 3 | `4b12cd52ee21`  |
| 3072   | Layout 3 | `4b12cd52ee21`  |
| 3062   | Layout 3 | `4b12cd52ee21`  |
| 3052   | Layout 3 | `4b12cd52ee21`  |
| 3045   | Layout 3 | `4b12cd52ee21`  |
| 3037   | Layout 3 | `4b12cd52ee21`  |
| 3030   | Layout 3 | `4b12cd52ee21`  |
| 3021   | Layout 3 | `4b12cd52ee21`  |
| 3012   | Layout 3 | `4b12cd52ee21`  |
| 3002   | Layout 3 | `4b12cd52ee21`  |
| 2995   | Layout 3 | `4b12cd52ee21`  |
| 2987   | Layout 3 | `4b12cd52ee21`  |
| 2978   | Layout 3 | `4b12cd52ee21`  |
| 2970   | Layout 3 | `4b12cd52ee21`  |
| 2959   | Layout 3 | `4b12cd52ee21`  |
| 2951   | Layout 3 | `4b12cd52ee21`  |
| 2942   | Layout 3 | `4b12cd52ee21`  |
| 2935   | Layout 3 | `4b12cd52ee21`  |
| 2932   | Layout 3 | `4b12cd52ee21`  |
| 2923   | Layout 3 | `4b12cd52ee21`  |
| 2919   | Layout 3 | `4b12cd52ee21`  |
| 2907   | Layout 3 | `4b12cd52ee21`  |
| 2900   | Layout 3 | `4b12cd52ee21`  |
| 2891   | Layout 3 | `4b12cd52ee21`  |
| 2882   | Layout 3 | `4b12cd52ee21`  |
| 2872   | Layout 3 | `4b12cd52ee21`  |
| 2863   | Layout 3 | `4b12cd52ee21`  |
| 2855   | Layout 3 | `4b12cd52ee21`  |
| 2849   | Layout 3 | `4b12cd52ee21`  |
| 2844   | Layout 3 | `4b12cd52ee21`  |
| 2834   | Layout 3 | `4b12cd52ee21`  |
| 2825   | Layout 3 | `4b12cd52ee21`  |
| 2819   | Layout 3 | `4b12cd52ee21`  |
| 2811   | Layout 3 | `4b12cd52ee21`  |
| 2803   | Layout 3 | `4b12cd52ee21`  |
| 2794   | Layout 3 | `4b12cd52ee21`  |
| 2783   | Layout 3 | `4b12cd52ee21`  |
| 2774   | Layout 3 | `4b12cd52ee21`  |
| 2765   | Layout 3 | `4b12cd52ee21`  |
| 2756   | Layout 3 | `4b12cd52ee21`  |
| 2750   | Layout 3 | `4b12cd52ee21`  |
| 2743   | Layout 3 | `4b12cd52ee21`  |
| 2736   | Layout 3 | `4b12cd52ee21`  |
| 2726   | Layout 3 | `4b12cd52ee21`  |
| 2717   | Layout 2 | `4b12cd52ee21`  |
| 2709   | Layout 2 | `4b12cd52ee21`  |
| 2703   | Layout 2 | `4b12cd52ee21`  |
| 2695   | Layout 2 | `4b12cd52ee21`  |
| 2684   | Layout 2 | `4b12cd52ee21`  |
| 2672   | Layout 2 | `4b12cd52ee21`  |
| 2665   | Layout 2 | `4b12cd52ee21`  |
| 2657   | Layout 2 | `4b12cd52ee21`  |
| 2649   | Layout 2 | `4b12cd52ee21`  |
| 2644   | Layout 2 | `4b12cd52ee21`  |
| 2637   | Layout 2 | `4b12cd52ee21`  |
| 2629   | Layout 2 | `4b12cd52ee21`  |
| 2619   | Layout 2 | `4b12cd52ee21`  |
| 2612   | Layout 2 | `4b12cd52ee21`  |
| 2606   | Layout 2 | `4b12cd52ee21`  |
| 2602   | Layout 2 | `4b12cd52ee21`  |
| 2601   | Layout 2 | `4b12cd52ee21`  |
| 2592   | Layout 2 | `4b12cd52ee21`  |
| 2583   | Layout 2 | `4b12cd52ee21`  |
| 2575   | Layout 2 | `4b12cd52ee21`  |
| 2567   | Layout 2 | `4b12cd52ee21`  |
| 2560   | Layout 2 | `4b12cd52ee21`  |
| 2553   | Layout 2 | `4b12cd52ee21`  |
| 2545   | Layout 2 | `4b12cd52ee21`  |
| 2538   | Layout 2 | `4b12cd52ee21`  |
| 2529   | Layout 2 | `4b12cd52ee21`  |
| 2519   | Layout 2 | `4b12cd52ee21`  |
| 2513   | Layout 2 | `4b12cd52ee21`  |
| 2510   | Layout 2 | `4b12cd52ee21`  |
| 2507   | Layout 2 | `4b12cd52ee21`  |
| 2503   | Layout 2 | `4b12cd52ee21`  |
| 2498   | Layout 2 | `4b12cd52ee21`  |
| 2492   | Layout 2 | `4b12cd52ee21`  |
| 2487   | Layout 2 | `4b12cd52ee21`  |
| 2480   | Layout 2 | `4b12cd52ee21`  |
| 2474   | Layout 2 | `4b12cd52ee21`  |
| 2468   | Layout 2 | `4b12cd52ee21`  |
| 2460   | Layout 2 | `4b12cd52ee21`  |
| 2453   | Layout 2 | `4b12cd52ee21`  |
| 2444   | Layout 2 | `4b12cd52ee21`  |
| 2438   | Layout 2 | `4b12cd52ee21`  |
| 2434   | Layout 2 | `4b12cd52ee21`  |
| 2429   | Layout 2 | `4b12cd52ee21`  |
| 2421   | Layout 2 | `4b12cd52ee21`  |
| 2414   | Layout 2 | `4b12cd52ee21`  |
| 2407   | Layout 2 | `4b12cd52ee21`  |
| 2401   | Layout 2 | `4b12cd52ee21`  |
| 2397   | Layout 2 | `4b12cd52ee21`  |
| 2393   | Layout 2 | `4b12cd52ee21`  |
| 2384   | Layout 2 | `4b12cd52ee21`  |
| 2378   | Layout 2 | `4b12cd52ee21`  |
| 2372   | Layout 2 | `4b12cd52ee21`  |
| 2358   | Layout 2 | `4b12cd52ee21`  |
| 2352   | Layout 2 | `4b12cd52ee21`  |
| 2347   | Layout 2 | `4b12cd52ee21`  |
| 2343   | Layout 2 | `4b12cd52ee21`  |
| 2335   | Layout 2 | `4b12cd52ee21`  |
| 2327   | Layout 2 | `4b12cd52ee21`  |
| 2324   | Layout 2 | `4b12cd52ee21`  |
| 2319   | Layout 2 | `4b12cd52ee21`  |
| 2313   | Layout 2 | `4b12cd52ee21`  |
| 2308   | Layout 2 | `4b12cd52ee21`  |
| 2302   | Layout 2 | `4b12cd52ee21`  |
| 2295   | Layout 2 | `4b12cd52ee21`  |
| 2290   | Layout 2 | `4b12cd52ee21`  |
| 2284   | Layout 2 | `4b12cd52ee21`  |
| 2276   | Layout 2 | `4b12cd52ee21`  |
| 2269   | Layout 2 | `4b12cd52ee21`  |
| 2259   | Layout 2 | `4b12cd52ee21`  |
| 2250   | Layout 2 | `4b12cd52ee21`  |
| 2243   | Layout 2 | `4b12cd52ee21`  |
| 2235   | Layout 2 | `4b12cd52ee21`  |
| 2229   | Layout 2 | `4b12cd52ee21`  |
| 2224   | Layout 2 | `4b12cd52ee21`  |
| 2218   | Layout 2 | `4b12cd52ee21`  |
| 2215   | Layout 2 | `4b12cd52ee21`  |
| 2207   | Layout 2 | `4b12cd52ee21`  |
| 2203   | Layout 2 | `4b12cd52ee21`  |
| 2196   | Layout 2 | `4b12cd52ee21`  |
| 2192   | Layout 2 | `4b12cd52ee21`  |
| 2189   | Layout 2 | `4b12cd52ee21`  |
| 2183   | Layout 2 | `4b12cd52ee21`  |
| 2179   | Layout 2 | `4b12cd52ee21`  |
| 2171   | Layout 2 | `4b12cd52ee21`  |
| 2163   | Layout 2 | `4b12cd52ee21`  |
| 2156   | Layout 2 | `4b12cd52ee21`  |
| 2151   | Layout 2 | `4b12cd52ee21`  |
| 2147   | Layout 2 | `4b12cd52ee21`  |
| 2142   | Layout 2 | `4b12cd52ee21`  |
| 2138   | Layout 2 | `4b12cd52ee21`  |
| 2134   | Layout 2 | `4b12cd52ee21`  |
| 2130   | Layout 2 | `4b12cd52ee21`  |
| 2122   | Layout 2 | `4b12cd52ee21`  |
| 2107   | Layout 2 | `4b12cd52ee21`  |
| 2098   | Layout 2 | `4b12cd52ee21`  |
| 2089   | Layout 2 | `4b12cd52ee21`  |
| 2081   | Layout 2 | `4b12cd52ee21`  |
| 2073   | Layout 2 | `4b12cd52ee21`  |
| 2067   | Layout 2 | `4b12cd52ee21`  |
| 2063   | Layout 2 | `4b12cd52ee21`  |
| 2059   | Layout 2 | `4b12cd52ee21`  |
| 2052   | Layout 2 | `4b12cd52ee21`  |
| 2044   | Layout 2 | `4b12cd52ee21`  |
| 2039   | Layout 2 | `4b12cd52ee21`  |
| 2032   | Layout 2 | `4b12cd52ee21`  |
| 2025   | Layout 2 | `4b12cd52ee21`  |
| 2011   | Layout 2 | `4b12cd52ee21`  |
| 2005   | Layout 2 | `4b12cd52ee21`  |
| 2000   | Layout 2 | `4b12cd52ee21`  |
| 1996   | Layout 2 | `4b12cd52ee21`  |
| 1991   | Layout 2 | `4b12cd52ee21`  |
| 1985   | Layout 2 | `4b12cd52ee21`  |
| 1980   | Layout 2 | `4b12cd52ee21`  |
| 1969   | Layout 2 | `4b12cd52ee21`  |
| 1964   | Layout 2 | `4b12cd52ee21`  |
| 1958   | Layout 2 | `4b12cd52ee21`  |
| 1950   | Layout 2 | `4b12cd52ee21`  |
| 1945   | Layout 2 | `4b12cd52ee21`  |
| 1937   | Layout 2 | `4b12cd52ee21`  |
| 1933   | Layout 2 | `4b12cd52ee21`  |
| 1927   | Layout 2 | `4b12cd52ee21`  |
| 1921   | Layout 2 | `4b12cd52ee21`  |
| 1914   | Layout 2 | `4b12cd52ee21`  |
| 1908   | Layout 2 | `4b12cd52ee21`  |
| 1897   | Layout 2 | `4b12cd52ee21`  |
| 1892   | Layout 2 | `4b12cd52ee21`  |
| 1886   | Layout 2 | `4b12cd52ee21`  |
| 1881   | Layout 2 | `4b12cd52ee21`  |
| 1871   | Layout 2 | `4b12cd52ee21`  |
| 1866   | Layout 2 | `4b12cd52ee21`  |
| 1862   | Layout 2 | `4b12cd52ee21`  |
| 1854   | Layout 2 | `4b12cd52ee21`  |
| 1846   | Layout 2 | `4b12cd52ee21`  |
| 1838   | Layout 2 | `4b12cd52ee21`  |
| 1832   | Layout 2 | `4b12cd52ee21`  |
| 1826   | Layout 2 | `4b12cd52ee21`  |
| 1822   | Layout 2 | `4b12cd52ee21`  |
| 1818   | Layout 2 | `4b12cd52ee21`  |
| 1804   | Layout 2 | `4b12cd52ee21`  |
| 1794   | Layout 2 | `4b12cd52ee21`  |
| 1790   | Layout 2 | `4b12cd52ee21`  |
| 1784   | Layout 2 | `4b12cd52ee21`  |
| 1774   | Layout 2 | `4b12cd52ee21`  |
| 1771   | Layout 2 | `4b12cd52ee21`  |
| 1762   | Layout 2 | `4b12cd52ee21`  |
| 1759   | Layout 2 | `4b12cd52ee21`  |
| 1754   | Layout 2 | `4b12cd52ee21`  |
| 1749   | Layout 2 | `4b12cd52ee21`  |
| 1743   | Layout 2 | `4b12cd52ee21`  |
| 1737   | Layout 2 | `4b12cd52ee21`  |
| 1731   | Layout 2 | `4b12cd52ee21`  |
| 1725   | Layout 2 | `4b12cd52ee21`  |
| 1717   | Layout 2 | `4b12cd52ee21`  |
| 1710   | Layout 2 | `4b12cd52ee21`  |
| 1704   | Layout 2 | `4b12cd52ee21`  |
| 1698   | Layout 2 | `4b12cd52ee21`  |
| 1690   | Layout 2 | `4b12cd52ee21`  |
| 1685   | Layout 2 | `4b12cd52ee21`  |
| 1680   | Layout 2 | `4b12cd52ee21`  |
| 1674   | Layout 2 | `4b12cd52ee21`  |
| 1668   | Layout 2 | `4b12cd52ee21`  |
| 1659   | Layout 2 | `4b12cd52ee21`  |
| 1649   | Layout 2 | `4b12cd52ee21`  |
| 1642   | Layout 2 | `4b12cd52ee21`  |
| 1636   | Layout 2 | `4b12cd52ee21`  |
| 1628   | Layout 2 | `4b12cd52ee21`  |
| 1622   | Layout 2 | `4b12cd52ee21`  |
| 1614   | Layout 2 | `4b12cd52ee21`  |
| 1608   | Layout 2 | `4b12cd52ee21`  |
| 1602   | Layout 2 | `4b12cd52ee21`  |
| 1598   | Layout 2 | `4b12cd52ee21`  |
| 1594   | Layout 2 | `4b12cd52ee21`  |
| 1590   | Layout 2 | `4b12cd52ee21`  |
| 1587   | Layout 2 | `4b12cd52ee21`  |
| 1584   | Layout 2 | `4b12cd52ee21`  |
| 1579   | Layout 2 | `4b12cd52ee21`  |
| 1572   | Layout 2 | `4b12cd52ee21`  |
| 1565   | Layout 2 | `4b12cd52ee21`  |
| 1559   | Layout 2 | `4b12cd52ee21`  |
| 1554   | Layout 2 | `4b12cd52ee21`  |
| 1547   | Layout 2 | `4b12cd52ee21`  |
| 1537   | Layout 2 | `4b12cd52ee21`  |
| 1529   | Layout 2 | `4b12cd52ee21`  |
| 1524   | Layout 2 | `4b12cd52ee21`  |
| 1519   | Layout 2 | `4b12cd52ee21`  |
| 1509   | Layout 2 | `4b12cd52ee21`  |
| 1506   | Layout 2 | `4b12cd52ee21`  |
| 1504   | Layout 2 | `4b12cd52ee21`  |
| 1500   | Layout 2 | `4b12cd52ee21`  |
| 1493   | Layout 2 | `4b12cd52ee21`  |
| 1489   | Layout 2 | `4b12cd52ee21`  |
| 1485   | Layout 2 | `4b12cd52ee21`  |
| 1481   | Layout 2 | `4b12cd52ee21`  |
| 1474   | Layout 2 | `4b12cd52ee21`  |
| 1466   | Layout 2 | `4b12cd52ee21`  |
| 1462   | Layout 2 | `4b12cd52ee21`  |
| 1459   | Layout 2 | `4b12cd52ee21`  |
| 1453   | Layout 2 | `4b12cd52ee21`  |
| 1450   | Layout 2 | `4b12cd52ee21`  |
| 1445   | Layout 2 | `4b12cd52ee21`  |
| 1439   | Layout 2 | `4b12cd52ee21`  |
| 1433   | Layout 2 | `4b12cd52ee21`  |
| 1430   | Layout 2 | `4b12cd52ee21`  |
| 1426   | Layout 2 | `4b12cd52ee21`  |
| 1421   | Layout 2 | `4b12cd52ee21`  |
| 1417   | Layout 2 | `4b12cd52ee21`  |
| 1416   | Layout 2 | `4b12cd52ee21`  |
| 1409   | Layout 2 | `4b12cd52ee21`  |
| 1405   | Layout 2 | `4b12cd52ee21`  |
| 1401   | Layout 2 | `4b12cd52ee21`  |
| 1396   | Layout 2 | `4b12cd52ee21`  |
| 1391   | Layout 2 | `4b12cd52ee21`  |
| 1390   | Layout 2 | `4b12cd52ee21`  |
| 1386   | Layout 2 | `4b12cd52ee21`  |
| 1381   | Layout 2 | `4b12cd52ee21`  |
| 1379   | Layout 2 | `4b12cd52ee21`  |
| 1372   | Layout 2 | `4b12cd52ee21`  |
| 1366   | Layout 2 | `4b12cd52ee21`  |
| 1364   | Layout 2 | `4b12cd52ee21`  |
| 1363   | Layout 2 | `4b12cd52ee21`  |
| 1360   | Layout 2 | `4b12cd52ee21`  |
| 1358   | Layout 2 | `4b12cd52ee21`  |
| 1355   | Layout 2 | `4b12cd52ee21`  |
| 1351   | Layout 2 | `4b12cd52ee21`  |
| 1348   | Layout 2 | `4b12cd52ee21`  |
| 1346   | Layout 2 | `4b12cd52ee21`  |
| 1341   | Layout 2 | `4b12cd52ee21`  |
| 1340   | Layout 2 | `4b12cd52ee21`  |
| 1338   | Layout 2 | `4b12cd52ee21`  |
| 1335   | Layout 2 | `4b12cd52ee21`  |
| 1333   | Layout 2 | `4b12cd52ee21`  |
| 1329   | Layout 2 | `4b12cd52ee21`  |
| 1327   | Layout 2 | `4b12cd52ee21`  |
| 1324   | Layout 2 | `4b12cd52ee21`  |
| 1321   | Layout 2 | `4b12cd52ee21`  |
| 1319   | Layout 2 | `4b12cd52ee21`  |
| 1318   | Layout 2 | `4b12cd52ee21`  |
| 1316   | Layout 2 | `4b12cd52ee21`  |
| 1313   | Layout 2 | `4b12cd52ee21`  |
| 1311   | Layout 2 | `4b12cd52ee21`  |
| 1309   | Layout 2 | `4b12cd52ee21`  |
| 1304   | Layout 2 | `4b12cd52ee21`  |
| 1292   | Layout 2 | `4b12cd52ee21`  |
| 1286   | Layout 2 | `4b12cd52ee21`  |
| 1280   | Layout 2 | `4b12cd52ee21`  |
| 1276   | Layout 2 | `4b12cd52ee21`  |
| 1267   | Layout 2 | `4b12cd52ee21`  |
| 1261   | Layout 2 | `4b12cd52ee21`  |
| 1256   | Layout 2 | `4b12cd52ee21`  |
| 1250   | Layout 2 | `4b12cd52ee21`  |
| 1246   | Layout 2 | `4b12cd52ee21`  |
| 1239   | Layout 2 | `4b12cd52ee21`  |
| 1230   | Layout 2 | `4b12cd52ee21`  |
| 1226   | Layout 2 | `4b12cd52ee21`  |
| 1220   | Layout 2 | `4b12cd52ee21`  |
| 1217   | Layout 2 | `4b12cd52ee21`  |
| 1211   | Layout 2 | `4b12cd52ee21`  |
| 1210   | Layout 2 | `4b12cd52ee21`  |
| 1208   | Layout 2 | `4b12cd52ee21`  |
| 1203   | Layout 2 | `4b12cd52ee21`  |
| 1197   | Layout 2 | `4b12cd52ee21`  |
| 1194   | Layout 2 | `4b12cd52ee21`  |
| 1192   | Layout 2 | `4b12cd52ee21`  |
| 1187   | Layout 2 | `4b12cd52ee21`  |
| 1183   | Layout 2 | `4b12cd52ee21`  |
| 1177   | Layout 2 | `4b12cd52ee21`  |
| 1173   | Layout 2 | `4b12cd52ee21`  |
| 1167   | Layout 2 | `4b12cd52ee21`  |
| 1164   | Layout 2 | `4b12cd52ee21`  |
| 1156   | Layout 2 | `4b12cd52ee21`  |
| 1149   | Layout 2 | `4b12cd52ee21`  |
| 1144   | Layout 2 | `4b12cd52ee21`  |
| 1137   | Layout 2 | `4b12cd52ee21`  |
| 1132   | Layout 2 | `4b12cd52ee21`  |
| 1127   | Layout 2 | `4b12cd52ee21`  |
| 1122   | Layout 2 | `4b12cd52ee21`  |
| 1118   | Layout 2 | `4b12cd52ee21`  |
| 1114   | Layout 2 | `4b12cd52ee21`  |
| 1109   | Layout 2 | `4b12cd52ee21`  |
| 1102   | Layout 2 | `4b12cd52ee21`  |
| 1096   | Layout 2 | `4b12cd52ee21`  |
| 1088   | Layout 2 | `4b12cd52ee21`  |
| 1081   | Layout 2 | `4b12cd52ee21`  |
| 1076   | Layout 2 | `4b12cd52ee21`  |
| 1069   | Layout 2 | `4b12cd52ee21`  |
| 1064   | Layout 2 | `4b12cd52ee21`  |
| 1058   | Layout 2 | `4b12cd52ee21`  |
| 1051   | Layout 2 | `4b12cd52ee21`  |
| 1044   | Layout 2 | `4b12cd52ee21`  |
| 1036   | Layout 2 | `4b12cd52ee21`  |
| 1026   | Layout 2 | `4b12cd52ee21`  |
| 1016   | Layout 2 | `4b12cd52ee21`  |
| 1009   | Layout 2 | `4b12cd52ee21`  |
| 1005   | Layout 2 | `4b12cd52ee21`  |
| 1000   | Layout 2 | `4b12cd52ee21`  |
| 998    | Layout 2 | `4b12cd52ee21`  |
| 990    | Layout 2 | `4b12cd52ee21`  |
| 979    | Layout 2 | `4b12cd52ee21`  |
| 972    | Layout 2 | `4b12cd52ee21`  |
| 963    | Layout 2 | `4b12cd52ee21`  |
| 955    | Layout 2 | `4b12cd52ee21`  |
| 946    | Layout 2 | `4b12cd52ee21`  |
| 938    | Layout 2 | `4b12cd52ee21`  |
| 927    | Layout 2 | `4b12cd52ee21`  |
| 911    | Layout 2 | `4b12cd52ee21`  |
| 904    | Layout 2 | `4b12cd52ee21`  |
| 899    | Layout 2 | `4b12cd52ee21`  |
| 894    | Layout 2 | `4b12cd52ee21`  |
| 885    | Layout 2 | `4b12cd52ee21`  |
| 879    | Layout 2 | `4b12cd52ee21`  |
| 872    | Layout 2 | `4b12cd52ee21`  |
| 864    | Layout 2 | `4b12cd52ee21`  |
| 855    | Layout 2 | `4b12cd52ee21`  |
| 853    | Layout 2 | `4b12cd52ee21`  |
| 845    | Layout 2 | `4b12cd52ee21`  |
| 837    | Layout 2 | `4b12cd52ee21`  |
| 829    | Layout 2 | `4b12cd52ee21`  |
| 822    | Layout 2 | `4b12cd52ee21`  |
| 814    | Layout 2 | `4b12cd52ee21`  |
| 805    | Layout 2 | `4b12cd52ee21`  |
| 794    | Layout 1 | `4b12cd52ee21`  |
| 787    | Layout 1 | `4b12cd52ee21`  |
| 780    | Layout 1 | `4b12cd52ee21`  |
| 771    | Layout 1 | `4b12cd52ee21`  |
| 760    | Layout 1 | `4b12cd52ee21`  |
| 748    | Layout 1 | `4b12cd52ee21`  |
| 741    | Layout 1 | `4b12cd52ee21`  |
| 736    | Layout 1 | `4b12cd52ee21`  |
| 731    | Layout 1 | `4b12cd52ee21`  |
| 723    | Layout 1 | `4b12cd52ee21`  |
| 711    | Layout 1 | `4b12cd52ee21`  |
| 707    | Layout 1 | `4b12cd52ee21`  |
| 697    | Layout 1 | `4b12cd52ee21`  |
| 689    | Layout 1 | `4b12cd52ee21`  |
| 683    | Layout 1 | `4b12cd52ee21`  |
| 678    | Layout 1 | `4b12cd52ee21`  |
| 670    | Layout 1 | `4b12cd52ee21`  |
| 661    | Layout 1 | `4b12cd52ee21`  |
| 656    | Layout 1 | `4b12cd52ee21`  |
| 652    | Layout 1 | `4b12cd52ee21`  |
| 643    | Layout 1 | `4b12cd52ee21`  |
| 637    | Layout 1 | `4b12cd52ee21`  |
| 630    | Layout 1 | `4b12cd52ee21`  |
| 627    | Layout 1 | `4b12cd52ee21`  |
| 621    | Layout 1 | `4b12cd52ee21`  |
| 617    | Layout 1 | `4b12cd52ee21`  |
| 615    | Layout 1 | `4b12cd52ee21`  |
| 606    | Layout 1 | `4b12cd52ee21`  |
| 599    | Layout 1 | `4b12cd52ee21`  |
| 592    | Layout 1 | `4b12cd52ee21`  |
| 586    | Layout 1 | `4b12cd52ee21`  |
| 577    | Layout 1 | `4b12cd52ee21`  |
| 569    | Layout 1 | `4b12cd52ee21`  |
| 561    | Layout 1 | `4b12cd52ee21`  |
| 554    | Layout 1 | `4b12cd52ee21`  |
| 542    | Layout 1 | `4b12cd52ee21`  |
| 532    | Layout 1 | `4b12cd52ee21`  |
| 531    | Layout 1 | `4b12cd52ee21`  |
| 526    | Layout 1 | `4b12cd52ee21`  |
| 521    | Layout 1 | `4b12cd52ee21`  |
| 517    | Layout 1 | `4b12cd52ee21`  |
| 510    | Layout 1 | `4b12cd52ee21`  |
| 508    | Layout 1 | `4b12cd52ee21`  |
| 504    | Layout 1 | `4b12cd52ee21`  |
| 497    | Layout 1 | `4b12cd52ee21`  |
| 491    | Layout 1 | `4b12cd52ee21`  |
| 485    | Layout 1 | `4b12cd52ee21`  |
| 478    | Layout 1 | `4b12cd52ee21`  |
| 472    | Layout 1 | `4b12cd52ee21`  |
| 466    | Layout 1 | `4b12cd52ee21`  |
| 457    | Layout 1 | `4b12cd52ee21`  |
| 452    | Layout 1 | `4b12cd52ee21`  |
| 449    | Layout 1 | `4b12cd52ee21`  |
| 435    | Layout 1 | `4b12cd52ee21`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Shared Layout

Same layout as [`waterinfo.bss`](waterinfo_bss.md), read by the same
handler: a PABR u32 count of rows, each a 3-byte `color_key` stored blue,
green, red, an unnamed u8 that is always `0` and eight bytes that are
always `0` (six on older layouts), then the string table and the trailer.
Clients up to 794 have no PABR magic, string table or trailer, and clients
up to 504 store a copy of the colour and a u16 drop ID in the six bytes.

## Colours

The `Underground_Table` sheet of a private server's
`datasheet_regiondatatable.xlsm` on client 1784 has 29 rows with a note
each. `color_key` as `rrggbb`, grouped by the sheet note (client 1784):

| `color_key`                                 | Sheet note                                                                         |
| ------------------------------------------- | ---------------------------------------------------------------------------------- |
| `649664`, `643c3c`, `5050c8`                | `레벨1`, `레벨2 드랍`, `레벨3 드랍` (levels 1 to 3): gold bars, ores, muddy water pouches |
| `fac8c8`                                    | `발렌시아 전역` (all of Valencia): the same drops                                   |
| `000064`                                    | `기본` (default): muddy water pouch                                                |
| `c80a0a`, `c80b0b`, `c80c0c`, `c87878`      | `의뢰용` (for quests): one drop item each                                           |
| `c87896`                                    | `북미 트레져 헌터용` (NA treasure hunter)                                           |
| `f42c01` to `f42c0a`                        | `작살낚시 전용 보물 지도 #1` to `#10` (treasure maps for harpoon fishing only)      |
| `2bffee`, `93fff7`, `65fff3`, `4cfff1`, `16ffec`, `00ffea`, `3affef` | `이벤트 의뢰용 # 1` to `# 7` (for event quests)                    |
| `003232`                                    | `히스트리아 의뢰용` (for the Hystria quest)                                         |
| `983535`                                    | `아르티니 승급 의뢰용` (for the Artini promotion quest)                             |

## Field Names

The `Underground_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `R`, `G`, `B` and `DropID`. All 29 of 29 file
colours on clients 1784 and 3482 are sheet rows, with the bytes in blue,
green, red order, and the file order is not the sheet order. The 2016
`gc::UndergroundInfoManager` holds the same `gc::BitmapDropInfo` rows as
`gc::WaterInfoManager`, keyed by `_colorKey`; the names follow
[`waterinfo.bss`](waterinfo_bss.md). On clients 435 and 504 the file holds
20 colours, each with the colour copy and a u16 that equals the client
1784 sheet's `DropID` on 20 of 20 rows. The `Underground_Table` of a
private server on client 519 has 28 of the 29 colours; `983535` is not
there.

## Notes

- On clients 606, 794, 1784 and 3482 every byte after the colour is `0`,
  where the client 1784 sheet has drop IDs `10060` to `10077` and `10881`
  to `10890`, as in `waterinfo.bss`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/server_tables.py`,
  `color_key` as `rrggbb`.
