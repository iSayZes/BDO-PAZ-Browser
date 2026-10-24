# `itemexchangesource.bss` Format

## Purpose

Item exchanges: one row per recipe a worker, a house, a guild house or a garden carries out, and per item box the client opens. A row lists the material items with their counts, the product category and work time, and the two [`itemmaingroup.bss`](itemmaingroup_bss.md) groups it hands out: the product and the worker luck drop. Worker production ([`plantexchangegroup.bss`](plantexchangegroup_bss.md)), house crafting ([`houseinforeceipe.dbss`](houseinforeceipe_dbss.md)) and Guild Crafting ([`guildmanufacture.dbss`](guildmanufacture_dbss.md)) point at rows by their key. The plain PABR file holds the rows, then a string table of the Korean names, descriptions and icon paths.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes     | Records                     | Row bytes |
| ------ | -------------- | ------- | ------------------------ | --------- | --------------------------- | --------- |
| 2      | 2726 and later | 3483    | `itemexchangesource.bss` | 3,214,251 | 34,801 Material, 14,217 Row | 12        |
| 1      | 1280 to 2717   | 2717    | `itemexchangesource.bss` | 2,466,879 | 28,343 Material, 11,188 Row | 12        |

| Layout | File                     | Known               | Unknown             |
| ------ | ------------------------ | ------------------- | ------------------- |
| 2      | `itemexchangesource.bss` | 1,433,466 B (44.6%) | 1,780,785 B (55.4%) |
| 1      | `itemexchangesource.bss` | 1,065,083 B (43.2%) | 1,401,796 B (56.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `0b5aebaf1869`  |
| 3482   | Layout 2             | `0b5aebaf1869`  |
| 3474   | Layout 2             | `0b5aebaf1869`  |
| 3473   | Layout 2             | `0b5aebaf1869`  |
| 3464   | Layout 2             | `0b5aebaf1869`  |
| 3458   | Layout 2             | `0b5aebaf1869`  |
| 3454   | Layout 2             | `0b5aebaf1869`  |
| 3444   | Layout 2             | `0b5aebaf1869`  |
| 3435   | Layout 2             | `0b5aebaf1869`  |
| 3426   | Layout 2             | `0b5aebaf1869`  |
| 3418   | Layout 2             | `0b5aebaf1869`  |
| 3412   | Layout 2             | `0b5aebaf1869`  |
| 3402   | Layout 2             | `0b5aebaf1869`  |
| 3396   | Layout 2             | `0b5aebaf1869`  |
| 3387   | Layout 2             | `0b5aebaf1869`  |
| 3381   | Layout 2             | `0b5aebaf1869`  |
| 3373   | Layout 2             | `0b5aebaf1869`  |
| 3364   | Layout 2             | `0b5aebaf1869`  |
| 3356   | Layout 2             | `0b5aebaf1869`  |
| 3349   | Layout 2             | `0b5aebaf1869`  |
| 3342   | Layout 2             | `0b5aebaf1869`  |
| 3335   | Layout 2             | `0b5aebaf1869`  |
| 3326   | Layout 2             | `0b5aebaf1869`  |
| 3321   | Layout 2             | `0b5aebaf1869`  |
| 3314   | Layout 2             | `0b5aebaf1869`  |
| 3303   | Layout 2             | `0b5aebaf1869`  |
| 3302   | Layout 2             | `0b5aebaf1869`  |
| 3293   | Layout 2             | `0b5aebaf1869`  |
| 3283   | Layout 2             | `0b5aebaf1869`  |
| 3275   | Layout 2             | `0b5aebaf1869`  |
| 3267   | Layout 2             | `0b5aebaf1869`  |
| 3258   | Layout 2             | `0b5aebaf1869`  |
| 3251   | Layout 2             | `0b5aebaf1869`  |
| 3242   | Layout 2             | `0b5aebaf1869`  |
| 3235   | Layout 2             | `0b5aebaf1869`  |
| 3229   | Layout 2             | `0b5aebaf1869`  |
| 3212   | Layout 2             | `0b5aebaf1869`  |
| 3203   | Layout 2             | `0b5aebaf1869`  |
| 3193   | Layout 2             | `0b5aebaf1869`  |
| 3186   | Layout 2             | `0b5aebaf1869`  |
| 3177   | Layout 2             | `0b5aebaf1869`  |
| 3169   | Layout 2             | `0b5aebaf1869`  |
| 3158   | Layout 2             | `0b5aebaf1869`  |
| 3151   | Layout 2             | `0b5aebaf1869`  |
| 3144   | Layout 2             | `0b5aebaf1869`  |
| 3133   | Layout 2             | `0b5aebaf1869`  |
| 3125   | Layout 2             | `0b5aebaf1869`  |
| 3118   | Layout 2             | `0b5aebaf1869`  |
| 3111   | Layout 2             | `0b5aebaf1869`  |
| 3103   | Layout 2             | `0b5aebaf1869`  |
| 3095   | Layout 2             | `0b5aebaf1869`  |
| 3086   | Layout 2             | `0b5aebaf1869`  |
| 3072   | Layout 2             | `0b5aebaf1869`  |
| 3062   | Layout 2             | `0b5aebaf1869`  |
| 3052   | Layout 2             | `0b5aebaf1869`  |
| 3045   | Layout 2             | `0b5aebaf1869`  |
| 3037   | Layout 2             | `0b5aebaf1869`  |
| 3030   | Layout 2             | `0b5aebaf1869`  |
| 3021   | Layout 2             | `0b5aebaf1869`  |
| 3012   | Layout 2             | `0b5aebaf1869`  |
| 3002   | Layout 2             | `0b5aebaf1869`  |
| 2995   | Layout 2             | `0b5aebaf1869`  |
| 2987   | Layout 2             | `0b5aebaf1869`  |
| 2978   | Layout 2             | `0b5aebaf1869`  |
| 2970   | Layout 2             | `0b5aebaf1869`  |
| 2959   | Layout 2             | `0b5aebaf1869`  |
| 2951   | Layout 2             | `0b5aebaf1869`  |
| 2942   | Layout 2             | `0b5aebaf1869`  |
| 2935   | Layout 2             | `0b5aebaf1869`  |
| 2932   | Layout 2             | `0b5aebaf1869`  |
| 2923   | Layout 2             | `0b5aebaf1869`  |
| 2919   | Layout 2             | `0b5aebaf1869`  |
| 2907   | Layout 2             | `0b5aebaf1869`  |
| 2900   | Layout 2             | `0b5aebaf1869`  |
| 2891   | Layout 2             | `0b5aebaf1869`  |
| 2882   | Layout 2             | `0b5aebaf1869`  |
| 2872   | Layout 2             | `0b5aebaf1869`  |
| 2863   | Layout 2             | `0b5aebaf1869`  |
| 2855   | Layout 2             | `0b5aebaf1869`  |
| 2849   | Layout 2             | `0b5aebaf1869`  |
| 2844   | Layout 2             | `0b5aebaf1869`  |
| 2834   | Layout 2             | `0b5aebaf1869`  |
| 2825   | Layout 2             | `0b5aebaf1869`  |
| 2819   | Layout 2             | `0b5aebaf1869`  |
| 2811   | Layout 2             | `0b5aebaf1869`  |
| 2803   | Layout 2             | `0b5aebaf1869`  |
| 2794   | Layout 2             | `0b5aebaf1869`  |
| 2783   | Layout 2             | `0b5aebaf1869`  |
| 2774   | Layout 2             | `0b5aebaf1869`  |
| 2765   | Layout 2             | `0b5aebaf1869`  |
| 2756   | Layout 2             | `0b5aebaf1869`  |
| 2750   | Layout 2             | `0b5aebaf1869`  |
| 2743   | Layout 2             | `0b5aebaf1869`  |
| 2736   | Layout 2             | `0b5aebaf1869`  |
| 2726   | Layout 2             | `0b5aebaf1869`  |
| 2717   | Layout 1             | `0b5aebaf1869`  |
| 2709   | Layout 1             | `0b5aebaf1869`  |
| 2703   | Layout 1             | `0b5aebaf1869`  |
| 2695   | Layout 1             | `0b5aebaf1869`  |
| 2684   | Layout 1             | `0b5aebaf1869`  |
| 2672   | Layout 1             | `0b5aebaf1869`  |
| 2665   | Layout 1             | `0b5aebaf1869`  |
| 2657   | Layout 1             | `0b5aebaf1869`  |
| 2649   | Layout 1             | `0b5aebaf1869`  |
| 2644   | Layout 1             | `0b5aebaf1869`  |
| 2637   | Layout 1             | `0b5aebaf1869`  |
| 2629   | Layout 1             | `0b5aebaf1869`  |
| 2619   | Layout 1             | `0b5aebaf1869`  |
| 2612   | Layout 1             | `0b5aebaf1869`  |
| 2606   | Layout 1             | `0b5aebaf1869`  |
| 2602   | Layout 1             | `0b5aebaf1869`  |
| 2601   | Layout 1             | `0b5aebaf1869`  |
| 2592   | Layout 1             | `0b5aebaf1869`  |
| 2583   | Layout 1             | `0b5aebaf1869`  |
| 2575   | Layout 1             | `0b5aebaf1869`  |
| 2567   | Layout 1             | `0b5aebaf1869`  |
| 2560   | Layout 1             | `0b5aebaf1869`  |
| 2553   | Layout 1             | `0b5aebaf1869`  |
| 2545   | Layout 1             | `0b5aebaf1869`  |
| 2538   | Layout 1             | `0b5aebaf1869`  |
| 2529   | Layout 1             | `0b5aebaf1869`  |
| 2519   | Layout 1             | `0b5aebaf1869`  |
| 2513   | Layout 1             | `0b5aebaf1869`  |
| 2510   | Layout 1             | `0b5aebaf1869`  |
| 2507   | Layout 1             | `0b5aebaf1869`  |
| 2503   | Layout 1             | `0b5aebaf1869`  |
| 2498   | Layout 1             | `0b5aebaf1869`  |
| 2492   | Layout 1             | `0b5aebaf1869`  |
| 2487   | Layout 1             | `0b5aebaf1869`  |
| 2480   | Layout 1             | `0b5aebaf1869`  |
| 2474   | Layout 1             | `0b5aebaf1869`  |
| 2468   | Layout 1             | `0b5aebaf1869`  |
| 2460   | Layout 1             | `0b5aebaf1869`  |
| 2453   | Layout 1             | `0b5aebaf1869`  |
| 2444   | Layout 1             | `0b5aebaf1869`  |
| 2438   | Layout 1             | `0b5aebaf1869`  |
| 2434   | Layout 1             | `0b5aebaf1869`  |
| 2429   | Layout 1             | `0b5aebaf1869`  |
| 2421   | Layout 1             | `0b5aebaf1869`  |
| 2414   | Layout 1             | `0b5aebaf1869`  |
| 2407   | Layout 1             | `0b5aebaf1869`  |
| 2401   | Layout 1             | `0b5aebaf1869`  |
| 2397   | Layout 1             | `0b5aebaf1869`  |
| 2393   | Layout 1             | `0b5aebaf1869`  |
| 2384   | Layout 1             | `0b5aebaf1869`  |
| 2378   | Layout 1             | `0b5aebaf1869`  |
| 2372   | Layout 1             | `0b5aebaf1869`  |
| 2358   | Layout 1             | `0b5aebaf1869`  |
| 2352   | Layout 1             | `0b5aebaf1869`  |
| 2347   | Layout 1             | `0b5aebaf1869`  |
| 2343   | Layout 1             | `0b5aebaf1869`  |
| 2335   | Layout 1             | `0b5aebaf1869`  |
| 2327   | Layout 1             | `0b5aebaf1869`  |
| 2324   | Layout 1             | `0b5aebaf1869`  |
| 2319   | Layout 1             | `0b5aebaf1869`  |
| 2313   | Layout 1             | `0b5aebaf1869`  |
| 2308   | Layout 1             | `0b5aebaf1869`  |
| 2302   | Layout 1             | `0b5aebaf1869`  |
| 2295   | Layout 1             | `0b5aebaf1869`  |
| 2290   | Layout 1             | `0b5aebaf1869`  |
| 2284   | Layout 1             | `0b5aebaf1869`  |
| 2276   | Layout 1             | `0b5aebaf1869`  |
| 2269   | Layout 1             | `0b5aebaf1869`  |
| 2259   | Layout 1             | `0b5aebaf1869`  |
| 2250   | Layout 1             | `0b5aebaf1869`  |
| 2243   | Layout 1             | `0b5aebaf1869`  |
| 2235   | Layout 1             | `0b5aebaf1869`  |
| 2229   | Layout 1             | `0b5aebaf1869`  |
| 2224   | Layout 1             | `0b5aebaf1869`  |
| 2218   | Layout 1             | `0b5aebaf1869`  |
| 2215   | Layout 1             | `0b5aebaf1869`  |
| 2207   | Layout 1             | `0b5aebaf1869`  |
| 2203   | Layout 1             | `0b5aebaf1869`  |
| 2196   | Layout 1             | `0b5aebaf1869`  |
| 2192   | Layout 1             | `0b5aebaf1869`  |
| 2189   | Layout 1             | `0b5aebaf1869`  |
| 2183   | Layout 1             | `0b5aebaf1869`  |
| 2179   | Layout 1             | `0b5aebaf1869`  |
| 2171   | Layout 1             | `0b5aebaf1869`  |
| 2163   | Layout 1             | `0b5aebaf1869`  |
| 2156   | Layout 1             | `0b5aebaf1869`  |
| 2151   | Layout 1             | `0b5aebaf1869`  |
| 2147   | Layout 1             | `0b5aebaf1869`  |
| 2142   | Layout 1             | `0b5aebaf1869`  |
| 2138   | Layout 1             | `0b5aebaf1869`  |
| 2134   | Layout 1             | `0b5aebaf1869`  |
| 2130   | Layout 1             | `0b5aebaf1869`  |
| 2122   | Layout 1             | `0b5aebaf1869`  |
| 2107   | Layout 1             | `0b5aebaf1869`  |
| 2098   | Layout 1             | `0b5aebaf1869`  |
| 2089   | Layout 1             | `0b5aebaf1869`  |
| 2081   | Layout 1             | `0b5aebaf1869`  |
| 2073   | Layout 1             | `0b5aebaf1869`  |
| 2067   | Layout 1             | `0b5aebaf1869`  |
| 2063   | Layout 1             | `0b5aebaf1869`  |
| 2059   | Layout 1             | `0b5aebaf1869`  |
| 2052   | Layout 1             | `0b5aebaf1869`  |
| 2044   | Layout 1             | `0b5aebaf1869`  |
| 2039   | Layout 1             | `0b5aebaf1869`  |
| 2032   | Layout 1             | `0b5aebaf1869`  |
| 2025   | Layout 1             | `0b5aebaf1869`  |
| 2011   | Layout 1             | `0b5aebaf1869`  |
| 2005   | Layout 1             | `0b5aebaf1869`  |
| 2000   | Layout 1             | `0b5aebaf1869`  |
| 1996   | Layout 1             | `0b5aebaf1869`  |
| 1991   | Layout 1             | `0b5aebaf1869`  |
| 1985   | Layout 1             | `0b5aebaf1869`  |
| 1980   | Layout 1             | `0b5aebaf1869`  |
| 1969   | Layout 1             | `0b5aebaf1869`  |
| 1964   | Layout 1             | `0b5aebaf1869`  |
| 1958   | Layout 1             | `0b5aebaf1869`  |
| 1950   | Layout 1             | `0b5aebaf1869`  |
| 1945   | Layout 1             | `0b5aebaf1869`  |
| 1937   | Layout 1             | `0b5aebaf1869`  |
| 1933   | Layout 1             | `0b5aebaf1869`  |
| 1927   | Layout 1             | `0b5aebaf1869`  |
| 1921   | Layout 1             | `0b5aebaf1869`  |
| 1914   | Layout 1             | `0b5aebaf1869`  |
| 1908   | Layout 1             | `0b5aebaf1869`  |
| 1897   | Layout 1             | `0b5aebaf1869`  |
| 1892   | Layout 1             | `0b5aebaf1869`  |
| 1886   | Layout 1             | `0b5aebaf1869`  |
| 1881   | Layout 1             | `0b5aebaf1869`  |
| 1871   | Layout 1             | `0b5aebaf1869`  |
| 1866   | Layout 1             | `0b5aebaf1869`  |
| 1862   | Layout 1             | `0b5aebaf1869`  |
| 1854   | Layout 1             | `0b5aebaf1869`  |
| 1846   | Layout 1             | `0b5aebaf1869`  |
| 1838   | Layout 1             | `0b5aebaf1869`  |
| 1832   | Layout 1             | `0b5aebaf1869`  |
| 1826   | Layout 1             | `0b5aebaf1869`  |
| 1822   | Layout 1             | `0b5aebaf1869`  |
| 1818   | Layout 1             | `0b5aebaf1869`  |
| 1804   | Layout 1             | `0b5aebaf1869`  |
| 1794   | Layout 1             | `0b5aebaf1869`  |
| 1790   | Layout 1             | `0b5aebaf1869`  |
| 1784   | Layout 1             | `0b5aebaf1869`  |
| 1774   | Layout 1             | `0b5aebaf1869`  |
| 1771   | Layout 1             | `0b5aebaf1869`  |
| 1762   | Layout 1             | `0b5aebaf1869`  |
| 1759   | Layout 1             | `0b5aebaf1869`  |
| 1754   | Layout 1             | `0b5aebaf1869`  |
| 1749   | Layout 1             | `0b5aebaf1869`  |
| 1743   | Layout 1             | `0b5aebaf1869`  |
| 1737   | Layout 1             | `0b5aebaf1869`  |
| 1731   | Layout 1             | `0b5aebaf1869`  |
| 1725   | Layout 1             | `0b5aebaf1869`  |
| 1717   | Layout 1             | `0b5aebaf1869`  |
| 1710   | Layout 1             | `0b5aebaf1869`  |
| 1704   | Layout 1             | `0b5aebaf1869`  |
| 1698   | Layout 1             | `0b5aebaf1869`  |
| 1690   | Layout 1             | `0b5aebaf1869`  |
| 1685   | Layout 1             | `0b5aebaf1869`  |
| 1680   | Layout 1             | `0b5aebaf1869`  |
| 1674   | Layout 1             | `0b5aebaf1869`  |
| 1668   | Layout 1             | `0b5aebaf1869`  |
| 1659   | Layout 1             | `0b5aebaf1869`  |
| 1649   | Layout 1             | `0b5aebaf1869`  |
| 1642   | Layout 1             | `0b5aebaf1869`  |
| 1636   | Layout 1             | `0b5aebaf1869`  |
| 1628   | Layout 1             | `0b5aebaf1869`  |
| 1622   | Layout 1             | `0b5aebaf1869`  |
| 1614   | Layout 1             | `0b5aebaf1869`  |
| 1608   | Layout 1             | `0b5aebaf1869`  |
| 1602   | Layout 1             | `0b5aebaf1869`  |
| 1598   | Layout 1             | `0b5aebaf1869`  |
| 1594   | Layout 1             | `0b5aebaf1869`  |
| 1590   | Layout 1             | `0b5aebaf1869`  |
| 1587   | Layout 1             | `0b5aebaf1869`  |
| 1584   | Layout 1             | `0b5aebaf1869`  |
| 1579   | Layout 1             | `0b5aebaf1869`  |
| 1572   | Layout 1             | `0b5aebaf1869`  |
| 1565   | Layout 1             | `0b5aebaf1869`  |
| 1559   | Layout 1             | `0b5aebaf1869`  |
| 1554   | Layout 1             | `0b5aebaf1869`  |
| 1547   | Layout 1             | `0b5aebaf1869`  |
| 1537   | Layout 1             | `0b5aebaf1869`  |
| 1529   | Layout 1             | `0b5aebaf1869`  |
| 1524   | Layout 1             | `0b5aebaf1869`  |
| 1519   | Layout 1             | `0b5aebaf1869`  |
| 1509   | Layout 1             | `0b5aebaf1869`  |
| 1506   | Layout 1             | `0b5aebaf1869`  |
| 1504   | Layout 1             | `0b5aebaf1869`  |
| 1500   | Layout 1             | `0b5aebaf1869`  |
| 1493   | Layout 1             | `0b5aebaf1869`  |
| 1489   | Layout 1             | `0b5aebaf1869`  |
| 1485   | Layout 1             | `0b5aebaf1869`  |
| 1481   | Layout 1             | `0b5aebaf1869`  |
| 1474   | Layout 1             | `0b5aebaf1869`  |
| 1466   | Layout 1             | `0b5aebaf1869`  |
| 1462   | Layout 1             | `0b5aebaf1869`  |
| 1459   | Layout 1             | `0b5aebaf1869`  |
| 1453   | Layout 1             | `0b5aebaf1869`  |
| 1450   | Layout 1             | `0b5aebaf1869`  |
| 1445   | Layout 1             | `0b5aebaf1869`  |
| 1439   | Layout 1             | `0b5aebaf1869`  |
| 1433   | Layout 1             | `0b5aebaf1869`  |
| 1430   | Layout 1             | `0b5aebaf1869`  |
| 1426   | Layout 1             | `0b5aebaf1869`  |
| 1421   | Layout 1             | `0b5aebaf1869`  |
| 1417   | Layout 1             | `0b5aebaf1869`  |
| 1416   | Layout 1             | `0b5aebaf1869`  |
| 1409   | Layout 1             | `0b5aebaf1869`  |
| 1405   | Layout 1             | `0b5aebaf1869`  |
| 1401   | Layout 1             | `0b5aebaf1869`  |
| 1396   | Layout 1             | `0b5aebaf1869`  |
| 1391   | Layout 1             | `0b5aebaf1869`  |
| 1390   | Layout 1             | `0b5aebaf1869`  |
| 1386   | Layout 1             | `0b5aebaf1869`  |
| 1381   | Layout 1             | `0b5aebaf1869`  |
| 1379   | Layout 1             | `0b5aebaf1869`  |
| 1372   | Layout 1             | `0b5aebaf1869`  |
| 1366   | Layout 1             | `0b5aebaf1869`  |
| 1364   | Layout 1             | `0b5aebaf1869`  |
| 1363   | Layout 1             | `0b5aebaf1869`  |
| 1360   | Layout 1             | `0b5aebaf1869`  |
| 1358   | Layout 1             | `0b5aebaf1869`  |
| 1355   | Layout 1             | `0b5aebaf1869`  |
| 1351   | Layout 1             | `0b5aebaf1869`  |
| 1348   | Layout 1             | `0b5aebaf1869`  |
| 1346   | Layout 1             | `0b5aebaf1869`  |
| 1341   | Layout 1             | `0b5aebaf1869`  |
| 1340   | Layout 1             | `0b5aebaf1869`  |
| 1338   | Layout 1             | `0b5aebaf1869`  |
| 1335   | Layout 1             | `0b5aebaf1869`  |
| 1333   | Layout 1             | `0b5aebaf1869`  |
| 1329   | Layout 1             | `0b5aebaf1869`  |
| 1327   | Layout 1             | `0b5aebaf1869`  |
| 1324   | Layout 1             | `0b5aebaf1869`  |
| 1321   | Layout 1             | `0b5aebaf1869`  |
| 1319   | Layout 1             | `0b5aebaf1869`  |
| 1318   | Layout 1             | `0b5aebaf1869`  |
| 1316   | Layout 1             | `0b5aebaf1869`  |
| 1313   | Layout 1             | `0b5aebaf1869`  |
| 1311   | Layout 1             | `0b5aebaf1869`  |
| 1309   | Layout 1             | `0b5aebaf1869`  |
| 1304   | Layout 1             | `0b5aebaf1869`  |
| 1292   | Layout 1             | `0b5aebaf1869`  |
| 1286   | Layout 1             | `0b5aebaf1869`  |
| 1280   | Layout 1             | `0b5aebaf1869`  |
| 1276   | No documented layout | `0b5aebaf1869`  |
| 1267   | No documented layout | `0b5aebaf1869`  |
| 1261   | No documented layout | `0b5aebaf1869`  |
| 1256   | No documented layout | `0b5aebaf1869`  |
| 1250   | No documented layout | `0b5aebaf1869`  |
| 1246   | No documented layout | `0b5aebaf1869`  |
| 1239   | No documented layout | `0b5aebaf1869`  |
| 1230   | No documented layout | `0b5aebaf1869`  |
| 1226   | No documented layout | `0b5aebaf1869`  |
| 1220   | No documented layout | `0b5aebaf1869`  |
| 1217   | No documented layout | `0b5aebaf1869`  |
| 1211   | No documented layout | `0b5aebaf1869`  |
| 1210   | No documented layout | `0b5aebaf1869`  |
| 1208   | No documented layout | `0b5aebaf1869`  |
| 1203   | No documented layout | `0b5aebaf1869`  |
| 1197   | No documented layout | `0b5aebaf1869`  |
| 1194   | No documented layout | `0b5aebaf1869`  |
| 1192   | No documented layout | `0b5aebaf1869`  |
| 1187   | No documented layout | `0b5aebaf1869`  |
| 1183   | No documented layout | `0b5aebaf1869`  |
| 1177   | No documented layout | `0b5aebaf1869`  |
| 1173   | No documented layout | `0b5aebaf1869`  |
| 1167   | No documented layout | `0b5aebaf1869`  |
| 1164   | No documented layout | `0b5aebaf1869`  |
| 1156   | No documented layout | `0b5aebaf1869`  |
| 1149   | No documented layout | `0b5aebaf1869`  |
| 1144   | No documented layout | `0b5aebaf1869`  |
| 1137   | No documented layout | `0b5aebaf1869`  |
| 1132   | No documented layout | `0b5aebaf1869`  |
| 1127   | No documented layout | `0b5aebaf1869`  |
| 1122   | No documented layout | `0b5aebaf1869`  |
| 1118   | No documented layout | `0b5aebaf1869`  |
| 1114   | No documented layout | `0b5aebaf1869`  |
| 1109   | No documented layout | `0b5aebaf1869`  |
| 1102   | No file              | `0b5aebaf1869`  |
| 1096   | No file              | `0b5aebaf1869`  |
| 1088   | No file              | `0b5aebaf1869`  |
| 1081   | No file              | `0b5aebaf1869`  |
| 1076   | No file              | `0b5aebaf1869`  |
| 1069   | No file              | `0b5aebaf1869`  |
| 1064   | No file              | `0b5aebaf1869`  |
| 1058   | No file              | `0b5aebaf1869`  |
| 1051   | No file              | `0b5aebaf1869`  |
| 1044   | No file              | `0b5aebaf1869`  |
| 1036   | No file              | `0b5aebaf1869`  |
| 1026   | No file              | `0b5aebaf1869`  |
| 1016   | No file              | `0b5aebaf1869`  |
| 1009   | No file              | `0b5aebaf1869`  |
| 1005   | No file              | `0b5aebaf1869`  |
| 1000   | No file              | `0b5aebaf1869`  |
| 998    | No file              | `0b5aebaf1869`  |
| 990    | No file              | `0b5aebaf1869`  |
| 979    | No file              | `0b5aebaf1869`  |
| 972    | No file              | `0b5aebaf1869`  |
| 963    | No file              | `0b5aebaf1869`  |
| 955    | No file              | `0b5aebaf1869`  |
| 946    | No file              | `0b5aebaf1869`  |
| 938    | No file              | `0b5aebaf1869`  |
| 927    | No file              | `0b5aebaf1869`  |
| 911    | No file              | `0b5aebaf1869`  |
| 904    | No file              | `0b5aebaf1869`  |
| 899    | No file              | `0b5aebaf1869`  |
| 894    | No file              | `0b5aebaf1869`  |
| 885    | No file              | `0b5aebaf1869`  |
| 879    | No file              | `0b5aebaf1869`  |
| 872    | No file              | `0b5aebaf1869`  |
| 864    | No file              | `0b5aebaf1869`  |
| 855    | No file              | `0b5aebaf1869`  |
| 853    | No file              | `0b5aebaf1869`  |
| 845    | No file              | `0b5aebaf1869`  |
| 837    | No file              | `0b5aebaf1869`  |
| 829    | No documented layout | `0b5aebaf1869`  |
| 822    | No documented layout | `0b5aebaf1869`  |
| 814    | No documented layout | `0b5aebaf1869`  |
| 805    | No documented layout | `0b5aebaf1869`  |
| 794    | No documented layout | `0b5aebaf1869`  |
| 787    | No documented layout | `0b5aebaf1869`  |
| 780    | No documented layout | `0b5aebaf1869`  |
| 771    | No documented layout | `0b5aebaf1869`  |
| 760    | No documented layout | `0b5aebaf1869`  |
| 748    | No documented layout | `0b5aebaf1869`  |
| 741    | No documented layout | `0b5aebaf1869`  |
| 736    | No documented layout | `0b5aebaf1869`  |
| 731    | No documented layout | `0b5aebaf1869`  |
| 723    | No documented layout | `0b5aebaf1869`  |
| 711    | No documented layout | `0b5aebaf1869`  |
| 707    | No documented layout | `0b5aebaf1869`  |
| 697    | No documented layout | `0b5aebaf1869`  |
| 689    | No documented layout | `0b5aebaf1869`  |
| 683    | No documented layout | `0b5aebaf1869`  |
| 678    | No documented layout | `0b5aebaf1869`  |
| 670    | No documented layout | `0b5aebaf1869`  |
| 661    | No documented layout | `0b5aebaf1869`  |
| 656    | No documented layout | `0b5aebaf1869`  |
| 652    | No documented layout | `0b5aebaf1869`  |
| 643    | No documented layout | `0b5aebaf1869`  |
| 637    | No documented layout | `0b5aebaf1869`  |
| 630    | No documented layout | `0b5aebaf1869`  |
| 627    | No documented layout | `0b5aebaf1869`  |
| 621    | No documented layout | `0b5aebaf1869`  |
| 617    | No documented layout | `0b5aebaf1869`  |
| 615    | No documented layout | `0b5aebaf1869`  |
| 606    | No documented layout | `0b5aebaf1869`  |
| 599    | No documented layout | `0b5aebaf1869`  |
| 592    | No documented layout | `0b5aebaf1869`  |
| 586    | No documented layout | `0b5aebaf1869`  |
| 577    | No documented layout | `0b5aebaf1869`  |
| 569    | No documented layout | `0b5aebaf1869`  |
| 561    | No documented layout | `0b5aebaf1869`  |
| 554    | No documented layout | `0b5aebaf1869`  |
| 542    | No documented layout | `0b5aebaf1869`  |
| 532    | No documented layout | `0b5aebaf1869`  |
| 531    | No documented layout | `0b5aebaf1869`  |
| 526    | No documented layout | `0b5aebaf1869`  |
| 521    | No documented layout | `0b5aebaf1869`  |
| 517    | No documented layout | `0b5aebaf1869`  |
| 510    | No documented layout | `0b5aebaf1869`  |
| 508    | No documented layout | `0b5aebaf1869`  |
| 504    | No documented layout | `0b5aebaf1869`  |
| 497    | No documented layout | `0b5aebaf1869`  |
| 491    | No documented layout | `0b5aebaf1869`  |
| 485    | No documented layout | `0b5aebaf1869`  |
| 478    | No documented layout | `0b5aebaf1869`  |
| 472    | No documented layout | `0b5aebaf1869`  |
| 466    | No documented layout | `0b5aebaf1869`  |
| 457    | No documented layout | `0b5aebaf1869`  |
| 452    | No documented layout | `0b5aebaf1869`  |
| 449    | No documented layout | `0b5aebaf1869`  |
| 435    | No documented layout | `0b5aebaf1869`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                          |
| ------------------------- | -------- | ----------------------------------------------------------------------------- |
| `itemmaingroup.bss`       | Optional | The product and luck drop groups                                              |
| `itemsubgroup.dbss`       | Optional | The items of those groups' subgroups                                          |
| `itemsubgroupoffset.dbss` | Optional | Index into `itemsubgroup.dbss`                                                |
| `languagedata_en.loc`     | Optional | Exchange names and descriptions (type 24), item names (type 0), character names (type 6) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type         | Field              | Notes                                                    |
| ------------------- | ------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                             |
| `+0x04`             | u32          | count              | Number of rows; `13,848` on client 3474                  |
| `+0x08`             | Row[count]   | rows               | Variable-size rows, back to back; see Row                |
| `rows+0x00`         | String Table | string_table       | See String Table                                         |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end             |
| `string_table+0x04` | u32          | zero               | Always `0`                                               |

Walking `count` rows ends exactly at `string_table_start`. The rows are not sorted by key: the file opens with key 965007.

### Row (variable: 196 bytes + materials and lists)

Row counts in the Notes column are from client 3474.

| Offset                        | Type                        | Field                  | Notes                                                                                    |
| ----------------------------- | --------------------------- | ---------------------- | ---------------------------------------------------------------------------------------- |
| `+0x00`                       | u32                         | key                    | Exchange key; unique, `5,001` to `965,010` (client 3474)                                 |
| `+0x04`                       | u32                         | key_dup                | Equals `key` on every row                                                                |
| `+0x08`                       | u8                          | unknown_08             | `0` on every row; the 2016 `_isBlockedNpcWork` slot                                      |
| `+0x09`                       | u8                          | exchange_type          | See [Exchange Types](#exchange-types)                                                    |
| `+0x0A`                       | bytes[36]                   | unknown_0a             | Always zero; where the 2016 struct has three 12-byte item slots, see Field Names         |
| `+0x2E`                       | u32                         | material_count         | `0` to `6`                                                                               |
| `+0x32`                       | Material[material_count]    | materials              | The items the exchange uses up; see Material                                             |
| `materials+0x00`              | Material                    | source_item            | Copy of the first material on every row that has one; all zero on the 1,214 rows without (client 3474) |
| `materials+0x0C`              | u8                          | product_category       | See [Product Categories](#product-categories)                                            |
| `materials+0x0D`              | bytes[12]                   | unknown_materials_0d   | Always zero; the 2016 `_productSkillPointExp` (i32) and `_productCharacterExp` (i64) slots |
| `materials+0x19`              | u64                         | product_time           | Work time in milliseconds; the worker windows show it divided by 1,000 as the workload   |
| `materials+0x21`              | i16                         | unknown_materials_21   | `0` on every row; the 2016 `_usingEndurance` slot                                        |
| `materials+0x23`              | u32                         | product_drop_key       | [`itemmaingroup.bss`](itemmaingroup_bss.md) group the exchange hands out; `0` on 223 Gamble rows |
| `materials+0x27`              | u32                         | luck_drop_key          | `itemmaingroup.bss` group of the worker luck drop; set on 414 rows, all worker rows      |
| `materials+0x2B`              | u16                         | craft_character_key    | Character that stands for the work in progress (`9097` "Galley under Construction"); set on 48 rows |
| `materials+0x2D`              | u32                         | icon_ref               | String table index of the icon path under `ui_texture/icon/`; `0` (empty) on most rows   |
| `materials+0x31`              | u32                         | description_ref        | String table index of the Korean name the work windows show                              |
| `materials+0x35`              | u32                         | detail_description_ref | String table index of the Korean description                                             |
| `materials+0x39`              | bytes[60]                   | unknown_materials_39   | Always zero                                                                              |
| `materials+0x75`              | u8                          | work_ani_type          | Worker animation; see [Work Animations](#work-animations)                                |
| `materials+0x76`              | i32                         | unknown_materials_76   | `-1` on every row; the 2016 `_dynamicEnchantLevelIndex` slot                             |
| `materials+0x7A`              | u32                         | unknown_list_count     | `2` on the 915 rows that set `repeat_group_key`, else `0` (client 3474)                  |
| `materials+0x7E`              | u16[unknown_list_count]     | unknown_list           | Always `0`                                                                               |
| `unknown_list+0x00`           | u16                         | unknown_list_00        | Always `0`                                                                               |
| `unknown_list+0x02`           | u16                         | repeat_group_key       | Repeat group (`5001` to `5004`, `9001` to `9006`); `0` for none                          |
| `unknown_list+0x04`           | i32                         | daily_working_count    | Daily limit of the work; `0` for none, set on 29 Guild Crafting rows                     |
| `unknown_list+0x08`           | i32                         | first_working_index    | `-1` for none; `1` on keys 7901 and 7927 only (client 3474)                              |
| `unknown_list+0x0C`           | u32                         | contents_group_count   | `1` to `7`                                                                               |
| `unknown_list+0x10`           | u32[contents_group_count]   | contents_group_hashes  | One hash per contents group key, as in [`characterstatic.dbss`](characterstatic_dbss.md); all 16,145 resolve (client 3474) |
| `contents_group_hashes+0x00`  | u32                         | unknown_end            | `0` on every row                                                                         |

### Material (12 bytes)

| Offset  | Type | Field    | Notes                                                       |
| ------- | ---- | -------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_key | Item key: `enchant_level << 24 \| item_id`                  |
| `+0x04` | u64  | count    | Number of items                                             |

On client 3474 the 13,848 rows hold 20,215 materials, and 54 of them carry an enchant level (`10`). Row 5026 (Azwell Longsword) uses Steel x5, Pure Copper Crystal x1, Fine Tough Hide x1 and Black Stone Powder x5.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                         |
| ------- | ------------------ | ------------ | --------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `3,180` on client 3474     |
| `+0x04` | pstr[string_count] | strings      | String `0` is empty; icon paths are not wide  |

The table has the shape of the [`itemmaingroup.bss` String Table](itemmaingroup_bss.md#string-table-variable-4-bytes--strings). Rows share entries: every row whose name repeats another's points at the same index.

## Layout 1

Client 1784 stores `key`, `key_dup` and both drop keys as u16, so the row head is 4 bytes and the drop keys 4 bytes shorter. Only the Row differs from Layout 2.

### Row (variable: 188 bytes + materials and lists)

| Offset                        | Type                        | Field                  | Notes                         |
| ----------------------------- | --------------------------- | ---------------------- | ----------------------------- |
| `+0x00`                       | u16                         | key                    | `7,053` rows (client 1784)    |
| `+0x02`                       | u16                         | key_dup                |                               |
| `+0x04`                       | u8                          | unknown_08             |                               |
| `+0x05`                       | u8                          | exchange_type          |                               |
| `+0x06`                       | bytes[36]                   | unknown_0a             |                               |
| `+0x2A`                       | u32                         | material_count         |                               |
| `+0x2E`                       | Material[material_count]    | materials              |                               |
| `materials+0x00`              | Material                    | source_item            |                               |
| `materials+0x0C`              | u8                          | product_category       |                               |
| `materials+0x0D`              | bytes[12]                   | unknown_materials_0d   |                               |
| `materials+0x19`              | u64                         | product_time           |                               |
| `materials+0x21`              | i16                         | unknown_materials_21   |                               |
| `materials+0x23`              | u16                         | product_drop_key       |                               |
| `materials+0x25`              | u16                         | luck_drop_key          |                               |
| `materials+0x27`              | u16                         | craft_character_key    |                               |
| `materials+0x29`              | u32                         | icon_ref               |                               |
| `materials+0x2D`              | u32                         | description_ref        |                               |
| `materials+0x31`              | u32                         | detail_description_ref |                               |
| `materials+0x35`              | bytes[60]                   | unknown_materials_39   |                               |
| `materials+0x71`              | u8                          | work_ani_type          |                               |
| `materials+0x72`              | i32                         | unknown_materials_76   |                               |
| `materials+0x76`              | u32                         | unknown_list_count     |                               |
| `materials+0x7A`              | u16[unknown_list_count]     | unknown_list           |                               |
| `unknown_list+0x00`           | u16                         | unknown_list_00        |                               |
| `unknown_list+0x02`           | u16                         | repeat_group_key       |                               |
| `unknown_list+0x04`           | i32                         | daily_working_count    |                               |
| `unknown_list+0x08`           | i32                         | first_working_index    |                               |
| `unknown_list+0x0C`           | u32                         | contents_group_count   |                               |
| `unknown_list+0x10`           | u32[contents_group_count]   | contents_group_hashes  |                               |
| `contents_group_hashes+0x00`  | u32                         | unknown_end            |                               |

## Exchange Types

`exchange_type` values, named after the 2016 `gc::ItemExchangeType::Type` enum (the client Lua of client 3474 has no copy). Rows on client 3474:

| Value | 2016 name            | Rows   | Content on client 3474                                                       |
| ----- | -------------------- | ------ | ---------------------------------------------------------------------------- |
| 3     | Gamble               | 10,001 | One material and a product group: items the player opens (Flameblade's Hardcore Box, outfit sets, Reward Bundle of Regret); `product_time` is `1000` |
| 4     | Plant                | 498    | Worker production at nodes (keys 40001 to 45019); the `plantexchangegroup.bss` exchanges |
| 5     | NonRecipeCraft       | 2,558  | House crafting (5026 Azwell Longsword); 2,364 of the 2,405 `houseinforeceipe.dbss` exchange keys |
| 6     | LargeCraft           | 19     | Ship and wagon registrations built in a house                                |
| 8     | GuildHouseLargeCraft | 29     | Guild Crafting (`[길드]` names, keys 7901 to 9776)                            |
| 9     | Garden               | 733    | Crops (keys 57001 to 58000), no materials                                    |
| 10    | GardenManage         | 10     | Keys 28023 to 28032, no materials and a `product_time` of `0`                |

The 2016 enum also has 0 Undefined, 1 Recipe, 2 Disassemble and 7 Improved; no row uses them.

## Product Categories

`product_category` values, named after `CppEnums.ProductCategory` in the client Lua (`global_define_cpp_enum.luac`, client 3474). The worker windows (`panel_worldmap_housecraft_renew.luac`) pass the row's `_productCategory` to the worker list to rate each worker's work speed.

| Value | Lua name        | Rows on client 3474                           |
| ----- | --------------- | --------------------------------------------- |
| 2     | Farm            | 508: the Plant and GardenManage rows          |
| 3     | Mine            | 10,734: the Gamble and Garden rows            |
| 5     | UseRecipe       | 2,558: the NonRecipeCraft rows                |
| 8     | LargeCraft      | 48: the LargeCraft and GuildHouseLargeCraft rows |

## Work Animations

`work_ani_type` values, named after the 2016 `gc::EWorkAniType` enum. Value 9 is the enum's `eWorkAniType_Count`, the value of every row whose sheet cell is empty (see Field Names).

| Value | 2016 name    | Rows on client 3474 |
| ----- | ------------ | ------------------- |
| 0     | Mining       | 262                 |
| 1     | Gather       | 64                  |
| 2     | Cultivation  | 66                  |
| 3     | Logging      | 66                  |
| 4     | Making       | 2,472               |
| 6     | Hide         | 180                 |
| 8     | Breeding     | 4                   |
| 9     | (none)       | 10,734              |

## Notes

- The exchange name and description are in LOC type 24 as well, keyed by `key` (`str_id4` `0` the name, `1` the description). On client 3474 the 3,104 rows with a Korean name all have a LOC type 24 name, and no other row has one.
- Every `plantexchangegroup.bss` exchange key (`+0x06`) is a key here: on client 3474 all 403 keys are Plant rows, and each one's `product_drop_key` is an `itemmaingroup.bss` group. 335 of them set `luck_drop_key`. Production key 1928 points at exchange 42356 (Lumbering), which drops group 42356 and luck group 44961.
- Every `houseinforeceipe.dbss` level key and every `guildmanufacture.dbss` `exchange_item_key` is a key here. On client 3474 the 2,405 distinct house keys are 2,364 NonRecipeCraft, 19 LargeCraft and 22 GuildHouseLargeCraft rows, and the 16 guild keys are GuildHouseLargeCraft rows.
- Three tables link to rows here without opening this file: the `plantexchangegroup.bss` Exchange column, the `houseinforeceipe.dbss` Exchanges column and the `guildmanufacture.dbss` Exchange Key column show each key as `Name (key)` and open its row. They read the name from LOC type 24, else from the `EXCHANGE_NAME_KR` lookup index, which holds every key with its Korean name (see `docs/handler.md`). The product items of the Plant rows reach `plantexchangegroup.bss` and `plantzone.dbss` through the `PRODUCTION_ITEMS` index, and their luck items reach `plantexchangegroup.bss` through `PRODUCTION_LUCK_ITEMS`.
- On client 3474 every non-zero `product_drop_key` (13,625) and `luck_drop_key` (414) is an `itemmaingroup.bss` group.
- The client Lua reads the row through an exchange wrapper: `getDescription()` and `getDetailDescription()` give the two texts, `getIcon()` the icon path (`"icon/" .. path`), and `_productTime / 1000` the workload (`panel_worldmap_housecraft_renew.luac`, client 3474).

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::ItemExchangeSourceStaticStatus` holds `_key` (u16), `_isBlockedNpcWork`, `_itemExchangeType`, three item slots (`_recipeItem`, `_publicNeedItem`, `_privateNeedItem`; each an item key and an i64 count), the material list, `_distintSourceItem`, `_productCategory`, `_productSkillPointExp`, `_productCharacterExp`, `_productTime`, `_usingEndurance`, `_productItemDropKey`, `_npcWorkerDropKeyForLuck`, `_characterKey`, `_icon`, `_description`, `_detailDescription`, `_lifeNpcWorkingCondition` (i32[9]), `_workAniType`, `_dynamicEnchantLevelIndex`, `_itemExchangeRepatGroupKeyList` (u16 list), `_dailyWorkingCount`, `_firstWorkingIndex` and `_contentsGroupKey`. The file stores them in that order.

The `ItemExchangeSource` sheet of a private server's `DataSheets.bexcel` on client 1784 shares 7,193 keys with client 3474:

| Field               | Sheet column                                   | Matching keys (client 3474)                                    |
| ------------------- | ---------------------------------------------- | -------------------------------------------------------------- |
| exchange_type       | `ExchangeType`                                 | 7,193 of 7,193                                                 |
| materials           | `ItemIndex0` to `5`, `ItemCount0` to `5`, `ItemIndex0EnchantLevel` to `5` | 6,985 of 7,193 (item keys alone 6,998)  |
| product_category    | `ProductDataType`                              | 7,193 of 7,193                                                 |
| product_time        | `CraftingTime`                                 | 7,177 of 7,193                                                 |
| product_drop_key    | `ItemDropID`                                   | 7,029 of 7,193                                                 |
| luck_drop_key       | `NpcWorkerDropIDForLuck`                       | 6,964 of 7,193; on client 1784, 7,053 of 7,053 with all 150 set keys |
| craft_character_key | `CraftCharacterKey`                            | 7,193 of 7,193 (43 set)                                        |
| icon_ref            | `ReciepeResultIcon`                            | 7,181 of 7,193, as the indexed text                            |
| description_ref     | `PlantDescription`                             | 7,169 of 7,193, as the indexed text                            |
| detail_description_ref | `PlantDetailDescription`                    | 7,177 of 7,193, as the indexed text                            |
| work_ani_type       | `WorkAniType`                                  | 1,872 of the 1,873 set cells; all 5,320 empty cells read `9`   |
| repeat_group_key    | `ItemExchangeRepatGroupKey`                    | 7,130 of 7,193                                                 |
| daily_working_count | `DailyWorkingCount`                            | 7,193 of 7,193                                                 |
| first_working_index | `FirstWorkingIndex`                            | 7,193 of 7,193; an empty cell reads `-1`                       |
| contents_group_hashes | `ContentsGroupKey`                           | 6,579 of 7,193; the misses are keys the sheet leaves at `0`    |

The `luck_drop_key` misses on client 3474 are renumbered groups: the sheet and client 1784 give exchange 44847 luck group 44947, client 3474 gives it 42013. `source_item` is `_distintSourceItem`; it equals the first material on every row.

`unknown_0a`, `unknown_materials_0d` and `unknown_materials_21` sit where the 2016 struct has the three item slots, the two experience fields and `_usingEndurance`. They are zero on every row, and so are the matching sheet columns (`CraftingRecipeItemID`, `CraftingPublicNeedItemID`, `CraftingPrivateNeedItemID` and their counts, `Exp`, `ProductExpSkillPoint`, `UsingEndurance`), so no value confirms the slots. `unknown_materials_39` is 60 zero bytes where the 2016 struct has the 36-byte `_lifeNpcWorkingCondition`; the sheet's `LifeLevelCondition`, `NeedObjectSkillNo` and `NeedObjeckSkillLevel` are empty. `unknown_materials_76` holds `-1` where the 2016 struct has `_dynamicEnchantLevelIndex`, which no sheet column holds.

## Open Questions

### The u16 List Before `repeat_group_key`

The 2016 struct has `_itemExchangeRepatGroupKeyList`, a u16 list, between `_dynamicEnchantLevelIndex` and `_dailyWorkingCount`. The file has a counted u16 list there, then `unknown_list_00` and `repeat_group_key`. The list holds two zeros on exactly the 915 rows with a repeat group and is empty on the others (client 3474; 587 rows on client 1784). Whether the list, `unknown_list_00` and `repeat_group_key` are one structure (a key list stored with its slots) or three fields is open, and so is what the zeros stand for.

### `unknown_end`

Every row ends with a u32 `0` after the contents group hashes, on client 3474 and client 1784. The 2016 struct ends with `_contentsGroupKey`, so the field is newer than 2016. A zero count of a list would read the same; no row sets it.
