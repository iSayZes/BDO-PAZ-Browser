# `manufacture.bss` Format

## Purpose

Processing recipes: each row is one material set for one processing action (Heating, Grinding, Simple Alchemy, Imperial Cuisine, Manufacture and the rest) and the [`itemmaingroup.bss`](itemmaingroup_bss.md) group the action hands out. The plain PABR file holds the rows, then a string table of the action names the processing window passes to the client (`actionName` in `panel_window_manufacture_all.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File              | Bytes   | Records                    | Row bytes |
| ------ | -------------- | ----------------- | ------- | -------------------------- | --------- |
| 2      | 2726 and later | `manufacture.bss` | 417,753 | 15,361 Material, 7,064 Row | 12        |
| 1      | 805 to 2717    | `manufacture.bss` | 345,839 | 12,483 Material, 6,314 Row | 12        |

| Layout | File              | Known              | Unknown    |
| ------ | ----------------- | ------------------ | ---------- |
| 2      | `manufacture.bss` | 417,753 B (100.0%) | 0 B (0.0%) |
| 1      | `manufacture.bss` | 345,839 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `28a446c89d8c`  |
| 3482   | Layout 2             | `28a446c89d8c`  |
| 3474   | Layout 2             | `28a446c89d8c`  |
| 3473   | Layout 2             | `28a446c89d8c`  |
| 3464   | Layout 2             | `28a446c89d8c`  |
| 3458   | Layout 2             | `28a446c89d8c`  |
| 3454   | Layout 2             | `28a446c89d8c`  |
| 3444   | Layout 2             | `28a446c89d8c`  |
| 3435   | Layout 2             | `28a446c89d8c`  |
| 3426   | Layout 2             | `28a446c89d8c`  |
| 3418   | Layout 2             | `28a446c89d8c`  |
| 3412   | Layout 2             | `28a446c89d8c`  |
| 3402   | Layout 2             | `28a446c89d8c`  |
| 3396   | Layout 2             | `28a446c89d8c`  |
| 3387   | Layout 2             | `28a446c89d8c`  |
| 3381   | Layout 2             | `28a446c89d8c`  |
| 3373   | Layout 2             | `28a446c89d8c`  |
| 3364   | Layout 2             | `28a446c89d8c`  |
| 3356   | Layout 2             | `28a446c89d8c`  |
| 3349   | Layout 2             | `28a446c89d8c`  |
| 3342   | Layout 2             | `28a446c89d8c`  |
| 3335   | Layout 2             | `28a446c89d8c`  |
| 3326   | Layout 2             | `28a446c89d8c`  |
| 3321   | Layout 2             | `28a446c89d8c`  |
| 3314   | Layout 2             | `28a446c89d8c`  |
| 3303   | Layout 2             | `28a446c89d8c`  |
| 3302   | Layout 2             | `28a446c89d8c`  |
| 3293   | Layout 2             | `28a446c89d8c`  |
| 3283   | Layout 2             | `28a446c89d8c`  |
| 3275   | Layout 2             | `28a446c89d8c`  |
| 3267   | Layout 2             | `28a446c89d8c`  |
| 3258   | Layout 2             | `28a446c89d8c`  |
| 3251   | Layout 2             | `28a446c89d8c`  |
| 3242   | Layout 2             | `28a446c89d8c`  |
| 3235   | Layout 2             | `28a446c89d8c`  |
| 3229   | Layout 2             | `28a446c89d8c`  |
| 3212   | Layout 2             | `28a446c89d8c`  |
| 3203   | Layout 2             | `28a446c89d8c`  |
| 3193   | Layout 2             | `28a446c89d8c`  |
| 3186   | Layout 2             | `28a446c89d8c`  |
| 3177   | Layout 2             | `28a446c89d8c`  |
| 3169   | Layout 2             | `28a446c89d8c`  |
| 3158   | Layout 2             | `28a446c89d8c`  |
| 3151   | Layout 2             | `28a446c89d8c`  |
| 3144   | Layout 2             | `28a446c89d8c`  |
| 3133   | Layout 2             | `28a446c89d8c`  |
| 3125   | Layout 2             | `28a446c89d8c`  |
| 3118   | Layout 2             | `28a446c89d8c`  |
| 3111   | Layout 2             | `28a446c89d8c`  |
| 3103   | Layout 2             | `28a446c89d8c`  |
| 3095   | Layout 2             | `28a446c89d8c`  |
| 3086   | Layout 2             | `28a446c89d8c`  |
| 3072   | Layout 2             | `28a446c89d8c`  |
| 3062   | Layout 2             | `28a446c89d8c`  |
| 3052   | Layout 2             | `28a446c89d8c`  |
| 3045   | Layout 2             | `28a446c89d8c`  |
| 3037   | Layout 2             | `28a446c89d8c`  |
| 3030   | Layout 2             | `28a446c89d8c`  |
| 3021   | Layout 2             | `28a446c89d8c`  |
| 3012   | Layout 2             | `28a446c89d8c`  |
| 3002   | Layout 2             | `28a446c89d8c`  |
| 2995   | Layout 2             | `28a446c89d8c`  |
| 2987   | Layout 2             | `28a446c89d8c`  |
| 2978   | Layout 2             | `28a446c89d8c`  |
| 2970   | Layout 2             | `28a446c89d8c`  |
| 2959   | Layout 2             | `28a446c89d8c`  |
| 2951   | Layout 2             | `28a446c89d8c`  |
| 2942   | Layout 2             | `28a446c89d8c`  |
| 2935   | Layout 2             | `28a446c89d8c`  |
| 2932   | Layout 2             | `28a446c89d8c`  |
| 2923   | Layout 2             | `28a446c89d8c`  |
| 2919   | Layout 2             | `28a446c89d8c`  |
| 2907   | Layout 2             | `28a446c89d8c`  |
| 2900   | Layout 2             | `28a446c89d8c`  |
| 2891   | Layout 2             | `28a446c89d8c`  |
| 2882   | Layout 2             | `28a446c89d8c`  |
| 2872   | Layout 2             | `28a446c89d8c`  |
| 2863   | Layout 2             | `28a446c89d8c`  |
| 2855   | Layout 2             | `28a446c89d8c`  |
| 2849   | Layout 2             | `28a446c89d8c`  |
| 2844   | Layout 2             | `28a446c89d8c`  |
| 2834   | Layout 2             | `28a446c89d8c`  |
| 2825   | Layout 2             | `28a446c89d8c`  |
| 2819   | Layout 2             | `28a446c89d8c`  |
| 2811   | Layout 2             | `28a446c89d8c`  |
| 2803   | Layout 2             | `28a446c89d8c`  |
| 2794   | Layout 2             | `28a446c89d8c`  |
| 2783   | Layout 2             | `28a446c89d8c`  |
| 2774   | Layout 2             | `28a446c89d8c`  |
| 2765   | Layout 2             | `28a446c89d8c`  |
| 2756   | Layout 2             | `28a446c89d8c`  |
| 2750   | Layout 2             | `28a446c89d8c`  |
| 2743   | Layout 2             | `28a446c89d8c`  |
| 2736   | Layout 2             | `28a446c89d8c`  |
| 2726   | Layout 2             | `28a446c89d8c`  |
| 2717   | Layout 1             | `28a446c89d8c`  |
| 2709   | Layout 1             | `28a446c89d8c`  |
| 2703   | Layout 1             | `28a446c89d8c`  |
| 2695   | Layout 1             | `28a446c89d8c`  |
| 2684   | Layout 1             | `28a446c89d8c`  |
| 2672   | Layout 1             | `28a446c89d8c`  |
| 2665   | Layout 1             | `28a446c89d8c`  |
| 2657   | Layout 1             | `28a446c89d8c`  |
| 2649   | Layout 1             | `28a446c89d8c`  |
| 2644   | Layout 1             | `28a446c89d8c`  |
| 2637   | Layout 1             | `28a446c89d8c`  |
| 2629   | Layout 1             | `28a446c89d8c`  |
| 2619   | Layout 1             | `28a446c89d8c`  |
| 2612   | Layout 1             | `28a446c89d8c`  |
| 2606   | Layout 1             | `28a446c89d8c`  |
| 2602   | Layout 1             | `28a446c89d8c`  |
| 2601   | Layout 1             | `28a446c89d8c`  |
| 2592   | Layout 1             | `28a446c89d8c`  |
| 2583   | Layout 1             | `28a446c89d8c`  |
| 2575   | Layout 1             | `28a446c89d8c`  |
| 2567   | Layout 1             | `28a446c89d8c`  |
| 2560   | Layout 1             | `28a446c89d8c`  |
| 2553   | Layout 1             | `28a446c89d8c`  |
| 2545   | Layout 1             | `28a446c89d8c`  |
| 2538   | Layout 1             | `28a446c89d8c`  |
| 2529   | Layout 1             | `28a446c89d8c`  |
| 2519   | Layout 1             | `28a446c89d8c`  |
| 2513   | Layout 1             | `28a446c89d8c`  |
| 2510   | Layout 1             | `28a446c89d8c`  |
| 2507   | Layout 1             | `28a446c89d8c`  |
| 2503   | Layout 1             | `28a446c89d8c`  |
| 2498   | Layout 1             | `28a446c89d8c`  |
| 2492   | Layout 1             | `28a446c89d8c`  |
| 2487   | Layout 1             | `28a446c89d8c`  |
| 2480   | Layout 1             | `28a446c89d8c`  |
| 2474   | Layout 1             | `28a446c89d8c`  |
| 2468   | Layout 1             | `28a446c89d8c`  |
| 2460   | Layout 1             | `28a446c89d8c`  |
| 2453   | Layout 1             | `28a446c89d8c`  |
| 2444   | Layout 1             | `28a446c89d8c`  |
| 2438   | Layout 1             | `28a446c89d8c`  |
| 2434   | Layout 1             | `28a446c89d8c`  |
| 2429   | Layout 1             | `28a446c89d8c`  |
| 2421   | Layout 1             | `28a446c89d8c`  |
| 2414   | Layout 1             | `28a446c89d8c`  |
| 2407   | Layout 1             | `28a446c89d8c`  |
| 2401   | Layout 1             | `28a446c89d8c`  |
| 2397   | Layout 1             | `28a446c89d8c`  |
| 2393   | Layout 1             | `28a446c89d8c`  |
| 2384   | Layout 1             | `28a446c89d8c`  |
| 2378   | Layout 1             | `28a446c89d8c`  |
| 2372   | Layout 1             | `28a446c89d8c`  |
| 2358   | Layout 1             | `28a446c89d8c`  |
| 2352   | Layout 1             | `28a446c89d8c`  |
| 2347   | Layout 1             | `28a446c89d8c`  |
| 2343   | Layout 1             | `28a446c89d8c`  |
| 2335   | Layout 1             | `28a446c89d8c`  |
| 2327   | Layout 1             | `28a446c89d8c`  |
| 2324   | Layout 1             | `28a446c89d8c`  |
| 2319   | Layout 1             | `28a446c89d8c`  |
| 2313   | Layout 1             | `28a446c89d8c`  |
| 2308   | Layout 1             | `28a446c89d8c`  |
| 2302   | Layout 1             | `28a446c89d8c`  |
| 2295   | Layout 1             | `28a446c89d8c`  |
| 2290   | Layout 1             | `28a446c89d8c`  |
| 2284   | Layout 1             | `28a446c89d8c`  |
| 2276   | Layout 1             | `28a446c89d8c`  |
| 2269   | Layout 1             | `28a446c89d8c`  |
| 2259   | Layout 1             | `28a446c89d8c`  |
| 2250   | Layout 1             | `28a446c89d8c`  |
| 2243   | Layout 1             | `28a446c89d8c`  |
| 2235   | Layout 1             | `28a446c89d8c`  |
| 2229   | Layout 1             | `28a446c89d8c`  |
| 2224   | Layout 1             | `28a446c89d8c`  |
| 2218   | Layout 1             | `28a446c89d8c`  |
| 2215   | Layout 1             | `28a446c89d8c`  |
| 2207   | Layout 1             | `28a446c89d8c`  |
| 2203   | Layout 1             | `28a446c89d8c`  |
| 2196   | Layout 1             | `28a446c89d8c`  |
| 2192   | Layout 1             | `28a446c89d8c`  |
| 2189   | Layout 1             | `28a446c89d8c`  |
| 2183   | Layout 1             | `28a446c89d8c`  |
| 2179   | Layout 1             | `28a446c89d8c`  |
| 2171   | Layout 1             | `28a446c89d8c`  |
| 2163   | Layout 1             | `28a446c89d8c`  |
| 2156   | Layout 1             | `28a446c89d8c`  |
| 2151   | Layout 1             | `28a446c89d8c`  |
| 2147   | Layout 1             | `28a446c89d8c`  |
| 2142   | Layout 1             | `28a446c89d8c`  |
| 2138   | Layout 1             | `28a446c89d8c`  |
| 2134   | Layout 1             | `28a446c89d8c`  |
| 2130   | Layout 1             | `28a446c89d8c`  |
| 2122   | Layout 1             | `28a446c89d8c`  |
| 2107   | Layout 1             | `28a446c89d8c`  |
| 2098   | Layout 1             | `28a446c89d8c`  |
| 2089   | Layout 1             | `28a446c89d8c`  |
| 2081   | Layout 1             | `28a446c89d8c`  |
| 2073   | Layout 1             | `28a446c89d8c`  |
| 2067   | Layout 1             | `28a446c89d8c`  |
| 2063   | Layout 1             | `28a446c89d8c`  |
| 2059   | Layout 1             | `28a446c89d8c`  |
| 2052   | Layout 1             | `28a446c89d8c`  |
| 2044   | Layout 1             | `28a446c89d8c`  |
| 2039   | Layout 1             | `28a446c89d8c`  |
| 2032   | Layout 1             | `28a446c89d8c`  |
| 2025   | Layout 1             | `28a446c89d8c`  |
| 2011   | Layout 1             | `28a446c89d8c`  |
| 2005   | Layout 1             | `28a446c89d8c`  |
| 2000   | Layout 1             | `28a446c89d8c`  |
| 1996   | Layout 1             | `28a446c89d8c`  |
| 1991   | Layout 1             | `28a446c89d8c`  |
| 1985   | Layout 1             | `28a446c89d8c`  |
| 1980   | Layout 1             | `28a446c89d8c`  |
| 1969   | Layout 1             | `28a446c89d8c`  |
| 1964   | Layout 1             | `28a446c89d8c`  |
| 1958   | Layout 1             | `28a446c89d8c`  |
| 1950   | Layout 1             | `28a446c89d8c`  |
| 1945   | Layout 1             | `28a446c89d8c`  |
| 1937   | Layout 1             | `28a446c89d8c`  |
| 1933   | Layout 1             | `28a446c89d8c`  |
| 1927   | Layout 1             | `28a446c89d8c`  |
| 1921   | Layout 1             | `28a446c89d8c`  |
| 1914   | Layout 1             | `28a446c89d8c`  |
| 1908   | Layout 1             | `28a446c89d8c`  |
| 1897   | Layout 1             | `28a446c89d8c`  |
| 1892   | Layout 1             | `28a446c89d8c`  |
| 1886   | Layout 1             | `28a446c89d8c`  |
| 1881   | Layout 1             | `28a446c89d8c`  |
| 1871   | Layout 1             | `28a446c89d8c`  |
| 1866   | Layout 1             | `28a446c89d8c`  |
| 1862   | Layout 1             | `28a446c89d8c`  |
| 1854   | Layout 1             | `28a446c89d8c`  |
| 1846   | Layout 1             | `28a446c89d8c`  |
| 1838   | Layout 1             | `28a446c89d8c`  |
| 1832   | Layout 1             | `28a446c89d8c`  |
| 1826   | Layout 1             | `28a446c89d8c`  |
| 1822   | Layout 1             | `28a446c89d8c`  |
| 1818   | Layout 1             | `28a446c89d8c`  |
| 1804   | Layout 1             | `28a446c89d8c`  |
| 1794   | Layout 1             | `28a446c89d8c`  |
| 1790   | Layout 1             | `28a446c89d8c`  |
| 1784   | Layout 1             | `28a446c89d8c`  |
| 1774   | Layout 1             | `28a446c89d8c`  |
| 1771   | Layout 1             | `28a446c89d8c`  |
| 1762   | Layout 1             | `28a446c89d8c`  |
| 1759   | Layout 1             | `28a446c89d8c`  |
| 1754   | Layout 1             | `28a446c89d8c`  |
| 1749   | Layout 1             | `28a446c89d8c`  |
| 1743   | Layout 1             | `28a446c89d8c`  |
| 1737   | Layout 1             | `28a446c89d8c`  |
| 1731   | Layout 1             | `28a446c89d8c`  |
| 1725   | Layout 1             | `28a446c89d8c`  |
| 1717   | Layout 1             | `28a446c89d8c`  |
| 1710   | Layout 1             | `28a446c89d8c`  |
| 1704   | Layout 1             | `28a446c89d8c`  |
| 1698   | Layout 1             | `28a446c89d8c`  |
| 1690   | Layout 1             | `28a446c89d8c`  |
| 1685   | Layout 1             | `28a446c89d8c`  |
| 1680   | Layout 1             | `28a446c89d8c`  |
| 1674   | Layout 1             | `28a446c89d8c`  |
| 1668   | Layout 1             | `28a446c89d8c`  |
| 1659   | Layout 1             | `28a446c89d8c`  |
| 1649   | Layout 1             | `28a446c89d8c`  |
| 1642   | Layout 1             | `28a446c89d8c`  |
| 1636   | Layout 1             | `28a446c89d8c`  |
| 1628   | Layout 1             | `28a446c89d8c`  |
| 1622   | Layout 1             | `28a446c89d8c`  |
| 1614   | Layout 1             | `28a446c89d8c`  |
| 1608   | Layout 1             | `28a446c89d8c`  |
| 1602   | Layout 1             | `28a446c89d8c`  |
| 1598   | Layout 1             | `28a446c89d8c`  |
| 1594   | Layout 1             | `28a446c89d8c`  |
| 1590   | Layout 1             | `28a446c89d8c`  |
| 1587   | Layout 1             | `28a446c89d8c`  |
| 1584   | Layout 1             | `28a446c89d8c`  |
| 1579   | Layout 1             | `28a446c89d8c`  |
| 1572   | Layout 1             | `28a446c89d8c`  |
| 1565   | Layout 1             | `28a446c89d8c`  |
| 1559   | Layout 1             | `28a446c89d8c`  |
| 1554   | Layout 1             | `28a446c89d8c`  |
| 1547   | Layout 1             | `28a446c89d8c`  |
| 1537   | Layout 1             | `28a446c89d8c`  |
| 1529   | Layout 1             | `28a446c89d8c`  |
| 1524   | Layout 1             | `28a446c89d8c`  |
| 1519   | Layout 1             | `28a446c89d8c`  |
| 1509   | Layout 1             | `28a446c89d8c`  |
| 1506   | Layout 1             | `28a446c89d8c`  |
| 1504   | Layout 1             | `28a446c89d8c`  |
| 1500   | Layout 1             | `28a446c89d8c`  |
| 1493   | Layout 1             | `28a446c89d8c`  |
| 1489   | Layout 1             | `28a446c89d8c`  |
| 1485   | Layout 1             | `28a446c89d8c`  |
| 1481   | Layout 1             | `28a446c89d8c`  |
| 1474   | Layout 1             | `28a446c89d8c`  |
| 1466   | Layout 1             | `28a446c89d8c`  |
| 1462   | Layout 1             | `28a446c89d8c`  |
| 1459   | Layout 1             | `28a446c89d8c`  |
| 1453   | Layout 1             | `28a446c89d8c`  |
| 1450   | Layout 1             | `28a446c89d8c`  |
| 1445   | Layout 1             | `28a446c89d8c`  |
| 1439   | Layout 1             | `28a446c89d8c`  |
| 1433   | Layout 1             | `28a446c89d8c`  |
| 1430   | Layout 1             | `28a446c89d8c`  |
| 1426   | Layout 1             | `28a446c89d8c`  |
| 1421   | Layout 1             | `28a446c89d8c`  |
| 1417   | Layout 1             | `28a446c89d8c`  |
| 1416   | Layout 1             | `28a446c89d8c`  |
| 1409   | Layout 1             | `28a446c89d8c`  |
| 1405   | Layout 1             | `28a446c89d8c`  |
| 1401   | Layout 1             | `28a446c89d8c`  |
| 1396   | Layout 1             | `28a446c89d8c`  |
| 1391   | Layout 1             | `28a446c89d8c`  |
| 1390   | Layout 1             | `28a446c89d8c`  |
| 1386   | Layout 1             | `28a446c89d8c`  |
| 1381   | Layout 1             | `28a446c89d8c`  |
| 1379   | Layout 1             | `28a446c89d8c`  |
| 1372   | Layout 1             | `28a446c89d8c`  |
| 1366   | Layout 1             | `28a446c89d8c`  |
| 1364   | Layout 1             | `28a446c89d8c`  |
| 1363   | Layout 1             | `28a446c89d8c`  |
| 1360   | Layout 1             | `28a446c89d8c`  |
| 1358   | Layout 1             | `28a446c89d8c`  |
| 1355   | Layout 1             | `28a446c89d8c`  |
| 1351   | Layout 1             | `28a446c89d8c`  |
| 1348   | Layout 1             | `28a446c89d8c`  |
| 1346   | Layout 1             | `28a446c89d8c`  |
| 1341   | Layout 1             | `28a446c89d8c`  |
| 1340   | Layout 1             | `28a446c89d8c`  |
| 1338   | Layout 1             | `28a446c89d8c`  |
| 1335   | Layout 1             | `28a446c89d8c`  |
| 1333   | Layout 1             | `28a446c89d8c`  |
| 1329   | Layout 1             | `28a446c89d8c`  |
| 1327   | Layout 1             | `28a446c89d8c`  |
| 1324   | Layout 1             | `28a446c89d8c`  |
| 1321   | Layout 1             | `28a446c89d8c`  |
| 1319   | Layout 1             | `28a446c89d8c`  |
| 1318   | Layout 1             | `28a446c89d8c`  |
| 1316   | Layout 1             | `28a446c89d8c`  |
| 1313   | Layout 1             | `28a446c89d8c`  |
| 1311   | Layout 1             | `28a446c89d8c`  |
| 1309   | Layout 1             | `28a446c89d8c`  |
| 1304   | Layout 1             | `28a446c89d8c`  |
| 1292   | Layout 1             | `28a446c89d8c`  |
| 1286   | Layout 1             | `28a446c89d8c`  |
| 1280   | Layout 1             | `28a446c89d8c`  |
| 1276   | Layout 1             | `28a446c89d8c`  |
| 1267   | Layout 1             | `28a446c89d8c`  |
| 1261   | Layout 1             | `28a446c89d8c`  |
| 1256   | Layout 1             | `28a446c89d8c`  |
| 1250   | Layout 1             | `28a446c89d8c`  |
| 1246   | Layout 1             | `28a446c89d8c`  |
| 1239   | Layout 1             | `28a446c89d8c`  |
| 1230   | Layout 1             | `28a446c89d8c`  |
| 1226   | Layout 1             | `28a446c89d8c`  |
| 1220   | Layout 1             | `28a446c89d8c`  |
| 1217   | Layout 1             | `28a446c89d8c`  |
| 1211   | Layout 1             | `28a446c89d8c`  |
| 1210   | Layout 1             | `28a446c89d8c`  |
| 1208   | Layout 1             | `28a446c89d8c`  |
| 1203   | Layout 1             | `28a446c89d8c`  |
| 1197   | Layout 1             | `28a446c89d8c`  |
| 1194   | Layout 1             | `28a446c89d8c`  |
| 1192   | Layout 1             | `28a446c89d8c`  |
| 1187   | Layout 1             | `28a446c89d8c`  |
| 1183   | Layout 1             | `28a446c89d8c`  |
| 1177   | Layout 1             | `28a446c89d8c`  |
| 1173   | Layout 1             | `28a446c89d8c`  |
| 1167   | Layout 1             | `28a446c89d8c`  |
| 1164   | Layout 1             | `28a446c89d8c`  |
| 1156   | Layout 1             | `28a446c89d8c`  |
| 1149   | Layout 1             | `28a446c89d8c`  |
| 1144   | Layout 1             | `28a446c89d8c`  |
| 1137   | Layout 1             | `28a446c89d8c`  |
| 1132   | Layout 1             | `28a446c89d8c`  |
| 1127   | Layout 1             | `28a446c89d8c`  |
| 1122   | Layout 1             | `28a446c89d8c`  |
| 1118   | Layout 1             | `28a446c89d8c`  |
| 1114   | Layout 1             | `28a446c89d8c`  |
| 1109   | Layout 1             | `28a446c89d8c`  |
| 1102   | Layout 1             | `28a446c89d8c`  |
| 1096   | Layout 1             | `28a446c89d8c`  |
| 1088   | Layout 1             | `28a446c89d8c`  |
| 1081   | Layout 1             | `28a446c89d8c`  |
| 1076   | Layout 1             | `28a446c89d8c`  |
| 1069   | Layout 1             | `28a446c89d8c`  |
| 1064   | Layout 1             | `28a446c89d8c`  |
| 1058   | Layout 1             | `28a446c89d8c`  |
| 1051   | Layout 1             | `28a446c89d8c`  |
| 1044   | Layout 1             | `28a446c89d8c`  |
| 1036   | Layout 1             | `28a446c89d8c`  |
| 1026   | Layout 1             | `28a446c89d8c`  |
| 1016   | Layout 1             | `28a446c89d8c`  |
| 1009   | Layout 1             | `28a446c89d8c`  |
| 1005   | Layout 1             | `28a446c89d8c`  |
| 1000   | Layout 1             | `28a446c89d8c`  |
| 998    | Layout 1             | `28a446c89d8c`  |
| 990    | Layout 1             | `28a446c89d8c`  |
| 979    | Layout 1             | `28a446c89d8c`  |
| 972    | Layout 1             | `28a446c89d8c`  |
| 963    | Layout 1             | `28a446c89d8c`  |
| 955    | Layout 1             | `28a446c89d8c`  |
| 946    | Layout 1             | `28a446c89d8c`  |
| 938    | Layout 1             | `28a446c89d8c`  |
| 927    | Layout 1             | `28a446c89d8c`  |
| 911    | Layout 1             | `28a446c89d8c`  |
| 904    | Layout 1             | `28a446c89d8c`  |
| 899    | Layout 1             | `28a446c89d8c`  |
| 894    | Layout 1             | `28a446c89d8c`  |
| 885    | Layout 1             | `28a446c89d8c`  |
| 879    | Layout 1             | `28a446c89d8c`  |
| 872    | Layout 1             | `28a446c89d8c`  |
| 864    | Layout 1             | `28a446c89d8c`  |
| 855    | Layout 1             | `28a446c89d8c`  |
| 853    | Layout 1             | `28a446c89d8c`  |
| 845    | Layout 1             | `28a446c89d8c`  |
| 837    | Layout 1             | `28a446c89d8c`  |
| 829    | Layout 1             | `28a446c89d8c`  |
| 822    | Layout 1             | `28a446c89d8c`  |
| 814    | Layout 1             | `28a446c89d8c`  |
| 805    | Layout 1             | `28a446c89d8c`  |
| 794    | No documented layout | `28a446c89d8c`  |
| 787    | No documented layout | `28a446c89d8c`  |
| 780    | No documented layout | `28a446c89d8c`  |
| 771    | No documented layout | `28a446c89d8c`  |
| 760    | No documented layout | `28a446c89d8c`  |
| 748    | No documented layout | `28a446c89d8c`  |
| 741    | No documented layout | `28a446c89d8c`  |
| 736    | No documented layout | `28a446c89d8c`  |
| 731    | No documented layout | `28a446c89d8c`  |
| 723    | No documented layout | `28a446c89d8c`  |
| 711    | No documented layout | `28a446c89d8c`  |
| 707    | No documented layout | `28a446c89d8c`  |
| 697    | No documented layout | `28a446c89d8c`  |
| 689    | No documented layout | `28a446c89d8c`  |
| 683    | No documented layout | `28a446c89d8c`  |
| 678    | No documented layout | `28a446c89d8c`  |
| 670    | No documented layout | `28a446c89d8c`  |
| 661    | No documented layout | `28a446c89d8c`  |
| 656    | No documented layout | `28a446c89d8c`  |
| 652    | No documented layout | `28a446c89d8c`  |
| 643    | No documented layout | `28a446c89d8c`  |
| 637    | No documented layout | `28a446c89d8c`  |
| 630    | No documented layout | `28a446c89d8c`  |
| 627    | No documented layout | `28a446c89d8c`  |
| 621    | No documented layout | `28a446c89d8c`  |
| 617    | No documented layout | `28a446c89d8c`  |
| 615    | No documented layout | `28a446c89d8c`  |
| 606    | No documented layout | `28a446c89d8c`  |
| 599    | No documented layout | `28a446c89d8c`  |
| 592    | No documented layout | `28a446c89d8c`  |
| 586    | No documented layout | `28a446c89d8c`  |
| 577    | No documented layout | `28a446c89d8c`  |
| 569    | No documented layout | `28a446c89d8c`  |
| 561    | No documented layout | `28a446c89d8c`  |
| 554    | No documented layout | `28a446c89d8c`  |
| 542    | No documented layout | `28a446c89d8c`  |
| 532    | No documented layout | `28a446c89d8c`  |
| 531    | No documented layout | `28a446c89d8c`  |
| 526    | No documented layout | `28a446c89d8c`  |
| 521    | No documented layout | `28a446c89d8c`  |
| 517    | No documented layout | `28a446c89d8c`  |
| 510    | No documented layout | `28a446c89d8c`  |
| 508    | No documented layout | `28a446c89d8c`  |
| 504    | No documented layout | `28a446c89d8c`  |
| 497    | No documented layout | `28a446c89d8c`  |
| 491    | No documented layout | `28a446c89d8c`  |
| 485    | No documented layout | `28a446c89d8c`  |
| 478    | No documented layout | `28a446c89d8c`  |
| 472    | No documented layout | `28a446c89d8c`  |
| 466    | No documented layout | `28a446c89d8c`  |
| 457    | No documented layout | `28a446c89d8c`  |
| 452    | No documented layout | `28a446c89d8c`  |
| 449    | No documented layout | `28a446c89d8c`  |
| 435    | No documented layout | `28a446c89d8c`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                 |
| --------------------- | -------- | ------------------------------------------------------------------------------------ |
| `itemmaingroup.bss`   | Optional | The result group of a row, when the client ships it                                  |
| `itemsubgroup.dbss`   | Optional | The items of the result group's subgroups                                            |
| `itemsubgroupoffset.dbss` | Optional | Index the subgroup lookup reads `itemsubgroup.dbss` through                      |
| `languagedata_en.loc` | Optional | Item names (type 0 at `str_id1=item_id`) and the action names (type 37, see below)    |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type         | Field              | Notes                                         |
| ------------------- | ------------ | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32          | count              | Number of rows; `7,064` on client 3464        |
| `+0x08`             | Row[count]   | rows               | See Row                                       |
| `rows+0x00`         | String Table | string_table       | See String Table                              |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end  |
| `string_table+0x04` | u32          | zero               | Always `0`                                    |

The string table has the shape `itemmaingroup.bss`, `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Every string here is narrow (`is_wide = 0`, ASCII). Walking `count` rows ends exactly at `string_table_start`, and the string table ends exactly at the trailer.

### Row (variable: 33 bytes + materials)

| Offset  | Type                     | Field             | Notes                                                                             |
| ------- | ------------------------ | ----------------- | --------------------------------------------------------------------------------- |
| `+0x00` | u32                      | first_item_key    | Packed item key, equal to `materials[0].item_key` on every row                    |
| `+0x04` | i64                      | check_time        | Always `0`                                                                        |
| `+0x0C` | u32                      | action_index      | Index into the string table, see [Actions](#actions)                              |
| `+0x10` | i32                      | success_percent   | `1,000,000`, `700,000`, `900,000` or `850,000`, see In-Game Checks                |
| `+0x14` | u32                      | action_hash       | Hash of the action name, see below; matches `action_index` on every row           |
| `+0x18` | u8                       | installation_type | Always `40`, `InstallationType.TypeCount`, see [Field Names](#field-names)        |
| `+0x19` | u32                      | result_group      | `itemmaingroup.bss` group ID; unaligned                                           |
| `+0x1D` | u32                      | material_count    | `1` to `5`; unaligned                                                             |
| `+0x21` | Material[material_count] | materials         | See Material                                                                      |

### Material (12 bytes)

| Offset  | Type | Field    | Notes                                                       |
| ------- | ---- | -------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_key | `(enchant_level << 24) \| item_id`, as in `itemsubgroup.dbss` |
| `+0x04` | u64  | count    | How many of the item the recipe takes                       |

On client 3464 the 7,064 rows hold 15,361 material entries: 3,072 rows have one, 1,551 two, 1,121 three, 776 four and 544 five. Counts run from `1` to `39,000`. Every one of the 5,304 distinct material keys is a key in `itemenchantoffset.dbss`. 675 entries carry an enchant level (`1` to `5`, `16` to `18` or `20`), such as Dandelion Jade Pillar at `18` for Simple Alchemy.

The entries of a row are in ascending `item_key` order on every row, so `first_item_key` is the row's lowest key. The same key can fill more than one entry: 17 rows (client 3464) list one key two or three times with count `1`, such as row 162 (Simple Alchemy) with three entries of Bonghwang's Fragment.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `12` on client 3464         |
| `+0x04` | pstr[string_count] | strings      | `u8 is_wide`, `u32 byte_length`, then the text |

## Layout 1

On client 1784 `result_group` is a u16, the width of the struct member it
fills (see [Field Names](#field-names)), so `material_count` sits at `+0x1B`
and the fixed part is 31 bytes. Only the Row differs from Layout 2.

### Row (variable: 31 bytes + materials)

| Offset  | Type                     | Field             | Notes                                                 |
| ------- | ------------------------ | ----------------- | ----------------------------------------------------- |
| `+0x00` | u32                      | first_item_key    |                                                       |
| `+0x04` | i64                      | check_time        | Always `0` on client 1784                             |
| `+0x0C` | u32                      | action_index      |                                                       |
| `+0x10` | i32                      | success_percent   | Always `0` on client 1784                             |
| `+0x14` | u32                      | action_hash       |                                                       |
| `+0x18` | u8                       | installation_type | Always `39` on client 1784, that client's `TypeCount` |
| `+0x19` | u16                      | result_group      | Always `0` on client 1784                             |
| `+0x1B` | u32                      | material_count    | `1` to `5`                                            |
| `+0x1F` | Material[material_count] | materials         |                                                       |

## Field Names

The 2016 client's debug symbols (`BlackDesert64.pdb`) list the members of
`gc::ManufactureStaticStatus` in this order: the material list,
`__int64 _checkTime`, `int _successPercent`, `_strActionName`,
`unsigned int _hashcodeActionName`, the one-byte
`gc::InstallationType _installationType`,
`KeyType<unsigned short> _resultItemGroupKey` and a contents group key list.
The manager keeps the rows in a multimap keyed by `gc::ItemEnchantKey`, the
role of `first_item_key`.

The `Manufacture_Table` sheet of a private server on client 1784 has one
column per member: `MaterialItem1` to `5` with `MaterialItemCount` and
`EnchantLevel`, `ResultDropGroup`, `CheckTime`, `SuccessPercent`,
`ActionName`, `UsingInstallationType` and `ContentsGroupKey`. That server's
dump (`Instance_dumpFull.exe`) loads the sheet (loader at VA `0x1409ac090`)
into members in the 2016 order:

| Field               | Sheet column            | Member (2016)         | Column read in the dump                                          |
| ------------------- | ----------------------- | --------------------- | ---------------------------------------------------------------- |
| `check_time`        | `CheckTime`             | `_checkTime`          | VA `0x1409ac9f6`, widened to 64 bits                             |
| `success_percent`   | `SuccessPercent`        | `_successPercent`     | VA `0x1409aca34`, 32 bits                                        |
| `action_index`      | `ActionName`            | `_strActionName`      | VA `0x1409aca7b`, a string                                       |
| `installation_type` | `UsingInstallationType` | `_installationType`   | VA `0x1409acad0`, one byte; an empty cell keeps the default `39` |
| `result_group`      | `ResultDropGroup`       | `_resultItemGroupKey` | VA `0x1409ac7ec`, stored as 16 bits                              |

No reader for the client file turned up in the dump, so the names rest on
the values:

- The private server's own `manufacture.bss`, compiled from that sheet,
  matches it: 8,648 of its 8,651 rows join exactly one sheet row on action
  and material list, and so do 4,538 of the 4,542 rows of the client 1784
  file. `CheckTime`, `SuccessPercent` and `ResultDropGroup` are `0` on
  every sheet row, as are `check_time`, `success_percent` and
  `result_group` in both files. `ContentsGroupKey` is set on 7,190 of the
  private server file's joined rows and has no field in the file.
- 1,232 rows of the `Manufacture_Table` of a private server on client 519
  join exactly one row of client 3474 on action and material list.
  `success_percent` equals `SuccessPercent` on 1,091 of the 1,130 of them
  where the column is not `0`, and `result_group` equals `ResultDropGroup`
  on 942 of the 1,116 where it is not `0`. `CheckTime` there is mostly
  `7000` (829 rows) or `9000` (289 rows), where the client file has `0`.
- `UsingInstallationType` is empty on every row of both tables. The client
  Lua (`global_define_cpp_enum.luac`) ends `CppEnums.InstallationType`, the
  enum of [`characterobject.dbss`](../dbss/characterobject_dbss.md)
  `installation_type`, with `TypeCount = 39` on client 1784 (last type
  `eType_MansionTree = 38`) and `TypeCount = 40` on client 3474
  (`eType_EventPersonalTent = 39` added).
  `installation_type` is `39` and `40` on those clients: the count, one past
  the last real type, marks a recipe that needs no installation. The 2016
  enum ends at `TypeCount = 33`.

The file stores `action_index` before `success_percent`, the reverse of the
member order. The two are told apart by value: `action_hash` matches
`action_index` on every row.

## `action_hash`

`action_hash` is Bob Jenkins' lookup3 `hashlittle` over the action name's ASCII bytes with seed `0xC5EDE`, the function and seed of `_common/string_hash.py`. That module's `key_hash` runs over UTF-16LE text instead, so the stored value is `hashlittle(name.encode("ascii"), 0xC5EDE)`. It reproduces the hash for all 12 names, and on every row it is the hash of the string at `action_index`.

## Actions

The display name is the `PAGetString(Defines.StringSheet_GAME, key)` text the processing window (`MANUFACTURE_INFO` in `panel_window_manufacture_all.luac`) shows for that `actionName`, read from LOC type 37 at `str_id1 = key_hash(key)`. The index is the position in this file's string table and can move between clients; the hash cannot.

| Index | Action name                     | `action_hash` | Display name     | Rows (client 3464) |
| ----- | ------------------------------- | ------------- | ---------------- | ------------------ |
| 0     | `MANUFACTURE_HEAT`              | `0x1B6F02F1`  | Heating          | 1,610              |
| 1     | `MANUFACTURE_ALCHEMY`           | `0x8347A078`  | Simple Alchemy   | 2,134              |
| 2     | `MANUFACTURE_DRY`               | `0xF00F4092`  | Drying           | 262                |
| 3     | `MANUFACTURE_GRIND`             | `0x42AE9CE7`  | Grinding         | 182                |
| 4     | `MANUFACTURE_CRAFT`             | `0xC48B5E9F`  | Manufacture      | 1,353              |
| 5     | `MANUFACTURE_COOK`              | `0x4437F6B7`  | Simple Cooking   | 139                |
| 6     | `MANUFACTURE_SHAKE`             | `0xB61F6930`  | Shaking          | 203                |
| 7     | `MANUFACTURE_ROYALGIFT_ALCHEMY` | `0x810D0D4C`  | Imperial Alchemy | 300                |
| 8     | `MANUFACTURE_GUILD`             | `0x3D249288`  | Guild Processing | 6                  |
| 9     | `MANUFACTURE_ROYALGIFT_COOK`    | `0x431295C7`  | Imperial Cuisine | 811                |
| 10    | `MANUFACTURE_THINNING`          | `0x77B04381`  | Filtering        | 12                 |
| 11    | `MANUFACTURE_FIREWOOD`          | `0x68721E0B`  | Chopping         | 52                 |

The display keys are `ALCHEMY_MANUFACTURE_HEATING`, `LUA_ALCHEMY_MANUFACTURE_ALCHEMY`, `ALCHEMY_MANUFACTURE_DRY`, `ALCHEMY_MANUFACTURE_GRIND`, `LUA_MANUFACTURE_CRAFT_NAME`, `LUA_ALCHEMY_MANUFACTURE_COOK`, `ALCHEMY_MANUFACTURE_SHAKE`, `LUA_ALCHEMY_MANUFACTURE_ROYALGIFT_ALCHEMY`, `LUA_MANUFACTURE_GUILDMANURACTURE_NAME` (the client's spelling), `LUA_ALCHEMY_MANUFACTURE_ROYALGIFT_COOK`, `ALCHEMY_MANUFACTURE_THINNING` and `ALCHEMY_MANUFACTURE_WOODSPLITTING`. The window also lists `MANUFACTURE_RAINWATER` (Collect rainwater) and `REPAIR_ITEM` (Repair), which have no rows here.

## Notes

- No two rows share both the action and the full material list (client 3464), so (action, materials) identifies a row. `first_item_key` alone does not: Elixir of Demihuman Hunt starts eleven rows over Simple and Imperial Alchemy.
- On client 3464, 201 of the 2,791 distinct `result_group` values are group IDs in `itemmaingroup.bss`, covering 901 rows (525 Heating, 375 Manufacture, 1 Simple Alchemy). Each of those groups has one subgroup with the group's own key, and its items fit the recipe: Heating Steel Taritas Helmet gives group 9978 (Melted Iron Shard, Mud Crystal), Heating Bares Necklace gives 9901 (Ruby, Melted Silver Shard). Each of the 58 Manufacture rows with La Orzeca's Orb gives a La Orzeca part of the same name and enchant level as its other material, under a different item ID (`[Valkyrie] La Orzeca Helmet` 601603 gives 604001).
- The other 2,590 values (6,163 rows) fall between 10129 and 19994. The client's `itemmaingroup.bss` holds one group from 10000 to 29999 (group 10000), so the groups for most processing results are absent from the client files, not a different ID space.
- 439 of the 2,791 groups are shared by more than one row (client 3464). Group 12537 is the result of all 25 Heating rows of Black Alloy with a Black Abyssal weapon or the Black Abyssal Amulet. Only one group serves two actions (Simple Alchemy and Manufacture).
- The processing window has five material slots (`_slotMaxCount = 5`), the largest `material_count` in the file.
- [`manufacturecondition.dbss`](../dbss/manufacturecondition_dbss.md) (14 records) is keyed by the same `action_hash` values: it holds the 12 action names of this file plus `REPAIR_ITEM` and `MANUFACTURE_RAINWATER`, each with the condition scripts that show and enable the action's tab, such as `getlevel()>0` or `getWeatherFactor(WindForce,0)>300;`.

## Open Questions

### What `check_time` Holds

`check_time` is `0` on every row of client 3474 and client 1784. The client 519 private server's `CheckTime` values (`7000`, `9000`, `10000`) read like a processing time in milliseconds, but no client row sets one and no client Lua reads the field.

### Missing Result Groups

Most `result_group` values (2,590 of 2,791 on client 3464) are not in `itemmaingroup.bss`, so a preview cannot show what Heating Melted Copper Shard or any Imperial Cuisine recipe gives. No other client table found so far holds groups 10000 to 29999.

## In-Game Checks

### Recipe Success Rate

This settles whether `success_percent` is the chance that one processing run succeeds, in millionths.

`success_percent` is `1,000,000` on 3,641 rows, `700,000` on 3,336, `900,000` on 81 and `850,000` on 6 (client 3464). `1,000,000` is also the usual value of `itemsubgroup.dbss` `unknown_33`. `700,000` is the common value for ordinary processing (1,423 of 1,610 Heating rows, all 262 Drying rows), `1,000,000` dominates Imperial Cuisine (783 of 811) and Imperial Alchemy, and 79 of the 81 `900,000` rows are Heating, most of them Black Abyssal or Delphad Castillion's Carnage gear with Black Alloy, Obsidian Alloy or Targak Steel Shard. No client Lua reads a per-recipe value: the rate list window (`panel_alchemy_rateviewlist.luac`) gets its percentages from `ToClient_calculateManufacturePercent` through `FromClient_CalculateGroupPercent`, which reports per-item drop rates. The name comes from the `SuccessPercent` sheet column (see [Field Names](#field-names)); the scale does not.

Needs item: [Melted Copper Shard](https://bdocodex.com/us/item/4057/), 300 or more

1. Open the processing window and pick Heating.
2. Turn Mass Processing off.
3. Put in Melted Copper Shard (row 0, 10 per run, `success_percent` = `700,000`).
4. Start processing and let it repeat 30 runs.
5. Count the runs that end in a failure message and give no item.

About 9 failures in 30 runs (30%) means `success_percent` is the success chance in millionths. No failures means it is something else.
