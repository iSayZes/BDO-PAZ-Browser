# `extractitem.dbss` Format

## Purpose

Reform stone extraction (`PANEL_EXTRACTIONSYSTEM_TITLE` "Extract Reform
Stone"): the blacksmith window that splits reformed gear back into the gear
it was made from and the reform stone. A row names the reformed item, the
item the extraction uses up, and the two items it returns.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes   | Records         | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ------- | --------------- | --------- |
| 1      | 1280 and later | 3483    | `extractitem.dbss`       | 112,132 | 2,336 Row       | 48        |
| 1      | 1280 and later | 3483    | `extractitemoffset.dbss` | 28,036  | 2,336 Index Row | 12        |

| Layout | File                     | Known              | Unknown    |
| ------ | ------------------------ | ------------------ | ---------- |
| 1      | `extractitem.dbss`       | 112,132 B (100.0%) | 0 B (0.0%) |
| 1      | `extractitemoffset.dbss` | 28,036 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `732ea3f5167c`  |
| 3482   | Layout 1 | `732ea3f5167c`  |
| 3474   | Layout 1 | `732ea3f5167c`  |
| 3473   | Layout 1 | `732ea3f5167c`  |
| 3464   | Layout 1 | `732ea3f5167c`  |
| 3458   | Layout 1 | `732ea3f5167c`  |
| 3454   | Layout 1 | `732ea3f5167c`  |
| 3444   | Layout 1 | `732ea3f5167c`  |
| 3435   | Layout 1 | `732ea3f5167c`  |
| 3426   | Layout 1 | `732ea3f5167c`  |
| 3418   | Layout 1 | `732ea3f5167c`  |
| 3412   | Layout 1 | `732ea3f5167c`  |
| 3402   | Layout 1 | `732ea3f5167c`  |
| 3396   | Layout 1 | `732ea3f5167c`  |
| 3387   | Layout 1 | `732ea3f5167c`  |
| 3381   | Layout 1 | `732ea3f5167c`  |
| 3373   | Layout 1 | `732ea3f5167c`  |
| 3364   | Layout 1 | `732ea3f5167c`  |
| 3356   | Layout 1 | `732ea3f5167c`  |
| 3349   | Layout 1 | `732ea3f5167c`  |
| 3342   | Layout 1 | `732ea3f5167c`  |
| 3335   | Layout 1 | `732ea3f5167c`  |
| 3326   | Layout 1 | `732ea3f5167c`  |
| 3321   | Layout 1 | `732ea3f5167c`  |
| 3314   | Layout 1 | `732ea3f5167c`  |
| 3303   | Layout 1 | `732ea3f5167c`  |
| 3302   | Layout 1 | `732ea3f5167c`  |
| 3293   | Layout 1 | `732ea3f5167c`  |
| 3283   | Layout 1 | `732ea3f5167c`  |
| 3275   | Layout 1 | `732ea3f5167c`  |
| 3267   | Layout 1 | `732ea3f5167c`  |
| 3258   | Layout 1 | `732ea3f5167c`  |
| 3251   | Layout 1 | `732ea3f5167c`  |
| 3242   | Layout 1 | `732ea3f5167c`  |
| 3235   | Layout 1 | `732ea3f5167c`  |
| 3229   | Layout 1 | `732ea3f5167c`  |
| 3212   | Layout 1 | `732ea3f5167c`  |
| 3203   | Layout 1 | `732ea3f5167c`  |
| 3193   | Layout 1 | `732ea3f5167c`  |
| 3186   | Layout 1 | `732ea3f5167c`  |
| 3177   | Layout 1 | `732ea3f5167c`  |
| 3169   | Layout 1 | `732ea3f5167c`  |
| 3158   | Layout 1 | `732ea3f5167c`  |
| 3151   | Layout 1 | `732ea3f5167c`  |
| 3144   | Layout 1 | `732ea3f5167c`  |
| 3133   | Layout 1 | `732ea3f5167c`  |
| 3125   | Layout 1 | `732ea3f5167c`  |
| 3118   | Layout 1 | `732ea3f5167c`  |
| 3111   | Layout 1 | `732ea3f5167c`  |
| 3103   | Layout 1 | `732ea3f5167c`  |
| 3095   | Layout 1 | `732ea3f5167c`  |
| 3086   | Layout 1 | `732ea3f5167c`  |
| 3072   | Layout 1 | `732ea3f5167c`  |
| 3062   | Layout 1 | `732ea3f5167c`  |
| 3052   | Layout 1 | `732ea3f5167c`  |
| 3045   | Layout 1 | `732ea3f5167c`  |
| 3037   | Layout 1 | `732ea3f5167c`  |
| 3030   | Layout 1 | `732ea3f5167c`  |
| 3021   | Layout 1 | `732ea3f5167c`  |
| 3012   | Layout 1 | `732ea3f5167c`  |
| 3002   | Layout 1 | `732ea3f5167c`  |
| 2995   | Layout 1 | `732ea3f5167c`  |
| 2987   | Layout 1 | `732ea3f5167c`  |
| 2978   | Layout 1 | `732ea3f5167c`  |
| 2970   | Layout 1 | `732ea3f5167c`  |
| 2959   | Layout 1 | `732ea3f5167c`  |
| 2951   | Layout 1 | `732ea3f5167c`  |
| 2942   | Layout 1 | `732ea3f5167c`  |
| 2935   | Layout 1 | `732ea3f5167c`  |
| 2932   | Layout 1 | `732ea3f5167c`  |
| 2923   | Layout 1 | `732ea3f5167c`  |
| 2919   | Layout 1 | `732ea3f5167c`  |
| 2907   | Layout 1 | `732ea3f5167c`  |
| 2900   | Layout 1 | `732ea3f5167c`  |
| 2891   | Layout 1 | `732ea3f5167c`  |
| 2882   | Layout 1 | `732ea3f5167c`  |
| 2872   | Layout 1 | `732ea3f5167c`  |
| 2863   | Layout 1 | `732ea3f5167c`  |
| 2855   | Layout 1 | `732ea3f5167c`  |
| 2849   | Layout 1 | `732ea3f5167c`  |
| 2844   | Layout 1 | `732ea3f5167c`  |
| 2834   | Layout 1 | `732ea3f5167c`  |
| 2825   | Layout 1 | `732ea3f5167c`  |
| 2819   | Layout 1 | `732ea3f5167c`  |
| 2811   | Layout 1 | `732ea3f5167c`  |
| 2803   | Layout 1 | `732ea3f5167c`  |
| 2794   | Layout 1 | `732ea3f5167c`  |
| 2783   | Layout 1 | `732ea3f5167c`  |
| 2774   | Layout 1 | `732ea3f5167c`  |
| 2765   | Layout 1 | `732ea3f5167c`  |
| 2756   | Layout 1 | `732ea3f5167c`  |
| 2750   | Layout 1 | `732ea3f5167c`  |
| 2743   | Layout 1 | `732ea3f5167c`  |
| 2736   | Layout 1 | `732ea3f5167c`  |
| 2726   | Layout 1 | `732ea3f5167c`  |
| 2717   | Layout 1 | `732ea3f5167c`  |
| 2709   | Layout 1 | `732ea3f5167c`  |
| 2703   | Layout 1 | `732ea3f5167c`  |
| 2695   | Layout 1 | `732ea3f5167c`  |
| 2684   | Layout 1 | `732ea3f5167c`  |
| 2672   | Layout 1 | `732ea3f5167c`  |
| 2665   | Layout 1 | `732ea3f5167c`  |
| 2657   | Layout 1 | `732ea3f5167c`  |
| 2649   | Layout 1 | `732ea3f5167c`  |
| 2644   | Layout 1 | `732ea3f5167c`  |
| 2637   | Layout 1 | `732ea3f5167c`  |
| 2629   | Layout 1 | `732ea3f5167c`  |
| 2619   | Layout 1 | `732ea3f5167c`  |
| 2612   | Layout 1 | `732ea3f5167c`  |
| 2606   | Layout 1 | `732ea3f5167c`  |
| 2602   | Layout 1 | `732ea3f5167c`  |
| 2601   | Layout 1 | `732ea3f5167c`  |
| 2592   | Layout 1 | `732ea3f5167c`  |
| 2583   | Layout 1 | `732ea3f5167c`  |
| 2575   | Layout 1 | `732ea3f5167c`  |
| 2567   | Layout 1 | `732ea3f5167c`  |
| 2560   | Layout 1 | `732ea3f5167c`  |
| 2553   | Layout 1 | `732ea3f5167c`  |
| 2545   | Layout 1 | `732ea3f5167c`  |
| 2538   | Layout 1 | `732ea3f5167c`  |
| 2529   | Layout 1 | `732ea3f5167c`  |
| 2519   | Layout 1 | `732ea3f5167c`  |
| 2513   | Layout 1 | `732ea3f5167c`  |
| 2510   | Layout 1 | `732ea3f5167c`  |
| 2507   | Layout 1 | `732ea3f5167c`  |
| 2503   | Layout 1 | `732ea3f5167c`  |
| 2498   | Layout 1 | `732ea3f5167c`  |
| 2492   | Layout 1 | `732ea3f5167c`  |
| 2487   | Layout 1 | `732ea3f5167c`  |
| 2480   | Layout 1 | `732ea3f5167c`  |
| 2474   | Layout 1 | `732ea3f5167c`  |
| 2468   | Layout 1 | `732ea3f5167c`  |
| 2460   | Layout 1 | `732ea3f5167c`  |
| 2453   | Layout 1 | `732ea3f5167c`  |
| 2444   | Layout 1 | `732ea3f5167c`  |
| 2438   | Layout 1 | `732ea3f5167c`  |
| 2434   | Layout 1 | `732ea3f5167c`  |
| 2429   | Layout 1 | `732ea3f5167c`  |
| 2421   | Layout 1 | `732ea3f5167c`  |
| 2414   | Layout 1 | `732ea3f5167c`  |
| 2407   | Layout 1 | `732ea3f5167c`  |
| 2401   | Layout 1 | `732ea3f5167c`  |
| 2397   | Layout 1 | `732ea3f5167c`  |
| 2393   | Layout 1 | `732ea3f5167c`  |
| 2384   | Layout 1 | `732ea3f5167c`  |
| 2378   | Layout 1 | `732ea3f5167c`  |
| 2372   | Layout 1 | `732ea3f5167c`  |
| 2358   | Layout 1 | `732ea3f5167c`  |
| 2352   | Layout 1 | `732ea3f5167c`  |
| 2347   | Layout 1 | `732ea3f5167c`  |
| 2343   | Layout 1 | `732ea3f5167c`  |
| 2335   | Layout 1 | `732ea3f5167c`  |
| 2327   | Layout 1 | `732ea3f5167c`  |
| 2324   | Layout 1 | `732ea3f5167c`  |
| 2319   | Layout 1 | `732ea3f5167c`  |
| 2313   | Layout 1 | `732ea3f5167c`  |
| 2308   | Layout 1 | `732ea3f5167c`  |
| 2302   | Layout 1 | `732ea3f5167c`  |
| 2295   | Layout 1 | `732ea3f5167c`  |
| 2290   | Layout 1 | `732ea3f5167c`  |
| 2284   | Layout 1 | `732ea3f5167c`  |
| 2276   | Layout 1 | `732ea3f5167c`  |
| 2269   | Layout 1 | `732ea3f5167c`  |
| 2259   | Layout 1 | `732ea3f5167c`  |
| 2250   | Layout 1 | `732ea3f5167c`  |
| 2243   | Layout 1 | `732ea3f5167c`  |
| 2235   | Layout 1 | `732ea3f5167c`  |
| 2229   | Layout 1 | `732ea3f5167c`  |
| 2224   | Layout 1 | `732ea3f5167c`  |
| 2218   | Layout 1 | `732ea3f5167c`  |
| 2215   | Layout 1 | `732ea3f5167c`  |
| 2207   | Layout 1 | `732ea3f5167c`  |
| 2203   | Layout 1 | `732ea3f5167c`  |
| 2196   | Layout 1 | `732ea3f5167c`  |
| 2192   | Layout 1 | `732ea3f5167c`  |
| 2189   | Layout 1 | `732ea3f5167c`  |
| 2183   | Layout 1 | `732ea3f5167c`  |
| 2179   | Layout 1 | `732ea3f5167c`  |
| 2171   | Layout 1 | `732ea3f5167c`  |
| 2163   | Layout 1 | `732ea3f5167c`  |
| 2156   | Layout 1 | `732ea3f5167c`  |
| 2151   | Layout 1 | `732ea3f5167c`  |
| 2147   | Layout 1 | `732ea3f5167c`  |
| 2142   | Layout 1 | `732ea3f5167c`  |
| 2138   | Layout 1 | `732ea3f5167c`  |
| 2134   | Layout 1 | `732ea3f5167c`  |
| 2130   | Layout 1 | `732ea3f5167c`  |
| 2122   | Layout 1 | `732ea3f5167c`  |
| 2107   | Layout 1 | `732ea3f5167c`  |
| 2098   | Layout 1 | `732ea3f5167c`  |
| 2089   | Layout 1 | `732ea3f5167c`  |
| 2081   | Layout 1 | `732ea3f5167c`  |
| 2073   | Layout 1 | `732ea3f5167c`  |
| 2067   | Layout 1 | `732ea3f5167c`  |
| 2063   | Layout 1 | `732ea3f5167c`  |
| 2059   | Layout 1 | `732ea3f5167c`  |
| 2052   | Layout 1 | `732ea3f5167c`  |
| 2044   | Layout 1 | `732ea3f5167c`  |
| 2039   | Layout 1 | `732ea3f5167c`  |
| 2032   | Layout 1 | `732ea3f5167c`  |
| 2025   | Layout 1 | `732ea3f5167c`  |
| 2011   | Layout 1 | `732ea3f5167c`  |
| 2005   | Layout 1 | `732ea3f5167c`  |
| 2000   | Layout 1 | `732ea3f5167c`  |
| 1996   | Layout 1 | `732ea3f5167c`  |
| 1991   | Layout 1 | `732ea3f5167c`  |
| 1985   | Layout 1 | `732ea3f5167c`  |
| 1980   | Layout 1 | `732ea3f5167c`  |
| 1969   | Layout 1 | `732ea3f5167c`  |
| 1964   | Layout 1 | `732ea3f5167c`  |
| 1958   | Layout 1 | `732ea3f5167c`  |
| 1950   | Layout 1 | `732ea3f5167c`  |
| 1945   | Layout 1 | `732ea3f5167c`  |
| 1937   | Layout 1 | `732ea3f5167c`  |
| 1933   | Layout 1 | `732ea3f5167c`  |
| 1927   | Layout 1 | `732ea3f5167c`  |
| 1921   | Layout 1 | `732ea3f5167c`  |
| 1914   | Layout 1 | `732ea3f5167c`  |
| 1908   | Layout 1 | `732ea3f5167c`  |
| 1897   | Layout 1 | `732ea3f5167c`  |
| 1892   | Layout 1 | `732ea3f5167c`  |
| 1886   | Layout 1 | `732ea3f5167c`  |
| 1881   | Layout 1 | `732ea3f5167c`  |
| 1871   | Layout 1 | `732ea3f5167c`  |
| 1866   | Layout 1 | `732ea3f5167c`  |
| 1862   | Layout 1 | `732ea3f5167c`  |
| 1854   | Layout 1 | `732ea3f5167c`  |
| 1846   | Layout 1 | `732ea3f5167c`  |
| 1838   | Layout 1 | `732ea3f5167c`  |
| 1832   | Layout 1 | `732ea3f5167c`  |
| 1826   | Layout 1 | `732ea3f5167c`  |
| 1822   | Layout 1 | `732ea3f5167c`  |
| 1818   | Layout 1 | `732ea3f5167c`  |
| 1804   | Layout 1 | `732ea3f5167c`  |
| 1794   | Layout 1 | `732ea3f5167c`  |
| 1790   | Layout 1 | `732ea3f5167c`  |
| 1784   | Layout 1 | `732ea3f5167c`  |
| 1774   | Layout 1 | `732ea3f5167c`  |
| 1771   | Layout 1 | `732ea3f5167c`  |
| 1762   | Layout 1 | `732ea3f5167c`  |
| 1759   | Layout 1 | `732ea3f5167c`  |
| 1754   | Layout 1 | `732ea3f5167c`  |
| 1749   | Layout 1 | `732ea3f5167c`  |
| 1743   | Layout 1 | `732ea3f5167c`  |
| 1737   | Layout 1 | `732ea3f5167c`  |
| 1731   | Layout 1 | `732ea3f5167c`  |
| 1725   | Layout 1 | `732ea3f5167c`  |
| 1717   | Layout 1 | `732ea3f5167c`  |
| 1710   | Layout 1 | `732ea3f5167c`  |
| 1704   | Layout 1 | `732ea3f5167c`  |
| 1698   | Layout 1 | `732ea3f5167c`  |
| 1690   | Layout 1 | `732ea3f5167c`  |
| 1685   | Layout 1 | `732ea3f5167c`  |
| 1680   | Layout 1 | `732ea3f5167c`  |
| 1674   | Layout 1 | `732ea3f5167c`  |
| 1668   | Layout 1 | `732ea3f5167c`  |
| 1659   | Layout 1 | `732ea3f5167c`  |
| 1649   | Layout 1 | `732ea3f5167c`  |
| 1642   | Layout 1 | `732ea3f5167c`  |
| 1636   | Layout 1 | `732ea3f5167c`  |
| 1628   | Layout 1 | `732ea3f5167c`  |
| 1622   | Layout 1 | `732ea3f5167c`  |
| 1614   | Layout 1 | `732ea3f5167c`  |
| 1608   | Layout 1 | `732ea3f5167c`  |
| 1602   | Layout 1 | `732ea3f5167c`  |
| 1598   | Layout 1 | `732ea3f5167c`  |
| 1594   | Layout 1 | `732ea3f5167c`  |
| 1590   | Layout 1 | `732ea3f5167c`  |
| 1587   | Layout 1 | `732ea3f5167c`  |
| 1584   | Layout 1 | `732ea3f5167c`  |
| 1579   | Layout 1 | `732ea3f5167c`  |
| 1572   | Layout 1 | `732ea3f5167c`  |
| 1565   | Layout 1 | `732ea3f5167c`  |
| 1559   | Layout 1 | `732ea3f5167c`  |
| 1554   | Layout 1 | `732ea3f5167c`  |
| 1547   | Layout 1 | `732ea3f5167c`  |
| 1537   | Layout 1 | `732ea3f5167c`  |
| 1529   | Layout 1 | `732ea3f5167c`  |
| 1524   | Layout 1 | `732ea3f5167c`  |
| 1519   | Layout 1 | `732ea3f5167c`  |
| 1509   | Layout 1 | `732ea3f5167c`  |
| 1506   | Layout 1 | `732ea3f5167c`  |
| 1504   | Layout 1 | `732ea3f5167c`  |
| 1500   | Layout 1 | `732ea3f5167c`  |
| 1493   | Layout 1 | `732ea3f5167c`  |
| 1489   | Layout 1 | `732ea3f5167c`  |
| 1485   | Layout 1 | `732ea3f5167c`  |
| 1481   | Layout 1 | `732ea3f5167c`  |
| 1474   | Layout 1 | `732ea3f5167c`  |
| 1466   | Layout 1 | `732ea3f5167c`  |
| 1462   | Layout 1 | `732ea3f5167c`  |
| 1459   | Layout 1 | `732ea3f5167c`  |
| 1453   | Layout 1 | `732ea3f5167c`  |
| 1450   | Layout 1 | `732ea3f5167c`  |
| 1445   | Layout 1 | `732ea3f5167c`  |
| 1439   | Layout 1 | `732ea3f5167c`  |
| 1433   | Layout 1 | `732ea3f5167c`  |
| 1430   | Layout 1 | `732ea3f5167c`  |
| 1426   | Layout 1 | `732ea3f5167c`  |
| 1421   | Layout 1 | `732ea3f5167c`  |
| 1417   | Layout 1 | `732ea3f5167c`  |
| 1416   | Layout 1 | `732ea3f5167c`  |
| 1409   | Layout 1 | `732ea3f5167c`  |
| 1405   | Layout 1 | `732ea3f5167c`  |
| 1401   | Layout 1 | `732ea3f5167c`  |
| 1396   | Layout 1 | `732ea3f5167c`  |
| 1391   | Layout 1 | `732ea3f5167c`  |
| 1390   | Layout 1 | `732ea3f5167c`  |
| 1386   | Layout 1 | `732ea3f5167c`  |
| 1381   | Layout 1 | `732ea3f5167c`  |
| 1379   | Layout 1 | `732ea3f5167c`  |
| 1372   | Layout 1 | `732ea3f5167c`  |
| 1366   | Layout 1 | `732ea3f5167c`  |
| 1364   | Layout 1 | `732ea3f5167c`  |
| 1363   | Layout 1 | `732ea3f5167c`  |
| 1360   | Layout 1 | `732ea3f5167c`  |
| 1358   | Layout 1 | `732ea3f5167c`  |
| 1355   | Layout 1 | `732ea3f5167c`  |
| 1351   | Layout 1 | `732ea3f5167c`  |
| 1348   | Layout 1 | `732ea3f5167c`  |
| 1346   | Layout 1 | `732ea3f5167c`  |
| 1341   | Layout 1 | `732ea3f5167c`  |
| 1340   | Layout 1 | `732ea3f5167c`  |
| 1338   | Layout 1 | `732ea3f5167c`  |
| 1335   | Layout 1 | `732ea3f5167c`  |
| 1333   | Layout 1 | `732ea3f5167c`  |
| 1329   | Layout 1 | `732ea3f5167c`  |
| 1327   | Layout 1 | `732ea3f5167c`  |
| 1324   | Layout 1 | `732ea3f5167c`  |
| 1321   | Layout 1 | `732ea3f5167c`  |
| 1319   | Layout 1 | `732ea3f5167c`  |
| 1318   | Layout 1 | `732ea3f5167c`  |
| 1316   | Layout 1 | `732ea3f5167c`  |
| 1313   | Layout 1 | `732ea3f5167c`  |
| 1311   | Layout 1 | `732ea3f5167c`  |
| 1309   | Layout 1 | `732ea3f5167c`  |
| 1304   | Layout 1 | `732ea3f5167c`  |
| 1292   | Layout 1 | `732ea3f5167c`  |
| 1286   | Layout 1 | `732ea3f5167c`  |
| 1280   | Layout 1 | `732ea3f5167c`  |
| 1276   | No file  | `732ea3f5167c`  |
| 1267   | No file  | `732ea3f5167c`  |
| 1261   | No file  | `732ea3f5167c`  |
| 1256   | No file  | `732ea3f5167c`  |
| 1250   | No file  | `732ea3f5167c`  |
| 1246   | No file  | `732ea3f5167c`  |
| 1239   | No file  | `732ea3f5167c`  |
| 1230   | No file  | `732ea3f5167c`  |
| 1226   | No file  | `732ea3f5167c`  |
| 1220   | No file  | `732ea3f5167c`  |
| 1217   | No file  | `732ea3f5167c`  |
| 1211   | No file  | `732ea3f5167c`  |
| 1210   | No file  | `732ea3f5167c`  |
| 1208   | No file  | `732ea3f5167c`  |
| 1203   | No file  | `732ea3f5167c`  |
| 1197   | No file  | `732ea3f5167c`  |
| 1194   | No file  | `732ea3f5167c`  |
| 1192   | No file  | `732ea3f5167c`  |
| 1187   | No file  | `732ea3f5167c`  |
| 1183   | No file  | `732ea3f5167c`  |
| 1177   | No file  | `732ea3f5167c`  |
| 1173   | No file  | `732ea3f5167c`  |
| 1167   | No file  | `732ea3f5167c`  |
| 1164   | No file  | `732ea3f5167c`  |
| 1156   | No file  | `732ea3f5167c`  |
| 1149   | No file  | `732ea3f5167c`  |
| 1144   | No file  | `732ea3f5167c`  |
| 1137   | No file  | `732ea3f5167c`  |
| 1132   | No file  | `732ea3f5167c`  |
| 1127   | No file  | `732ea3f5167c`  |
| 1122   | No file  | `732ea3f5167c`  |
| 1118   | No file  | `732ea3f5167c`  |
| 1114   | No file  | `732ea3f5167c`  |
| 1109   | No file  | `732ea3f5167c`  |
| 1102   | No file  | `732ea3f5167c`  |
| 1096   | No file  | `732ea3f5167c`  |
| 1088   | No file  | `732ea3f5167c`  |
| 1081   | No file  | `732ea3f5167c`  |
| 1076   | No file  | `732ea3f5167c`  |
| 1069   | No file  | `732ea3f5167c`  |
| 1064   | No file  | `732ea3f5167c`  |
| 1058   | No file  | `732ea3f5167c`  |
| 1051   | No file  | `732ea3f5167c`  |
| 1044   | No file  | `732ea3f5167c`  |
| 1036   | No file  | `732ea3f5167c`  |
| 1026   | No file  | `732ea3f5167c`  |
| 1016   | No file  | `732ea3f5167c`  |
| 1009   | No file  | `732ea3f5167c`  |
| 1005   | No file  | `732ea3f5167c`  |
| 1000   | No file  | `732ea3f5167c`  |
| 998    | No file  | `732ea3f5167c`  |
| 990    | No file  | `732ea3f5167c`  |
| 979    | No file  | `732ea3f5167c`  |
| 972    | No file  | `732ea3f5167c`  |
| 963    | No file  | `732ea3f5167c`  |
| 955    | No file  | `732ea3f5167c`  |
| 946    | No file  | `732ea3f5167c`  |
| 938    | No file  | `732ea3f5167c`  |
| 927    | No file  | `732ea3f5167c`  |
| 911    | No file  | `732ea3f5167c`  |
| 904    | No file  | `732ea3f5167c`  |
| 899    | No file  | `732ea3f5167c`  |
| 894    | No file  | `732ea3f5167c`  |
| 885    | No file  | `732ea3f5167c`  |
| 879    | No file  | `732ea3f5167c`  |
| 872    | No file  | `732ea3f5167c`  |
| 864    | No file  | `732ea3f5167c`  |
| 855    | No file  | `732ea3f5167c`  |
| 853    | No file  | `732ea3f5167c`  |
| 845    | No file  | `732ea3f5167c`  |
| 837    | No file  | `732ea3f5167c`  |
| 829    | No file  | `732ea3f5167c`  |
| 822    | No file  | `732ea3f5167c`  |
| 814    | No file  | `732ea3f5167c`  |
| 805    | No file  | `732ea3f5167c`  |
| 794    | No file  | `732ea3f5167c`  |
| 787    | No file  | `732ea3f5167c`  |
| 780    | No file  | `732ea3f5167c`  |
| 771    | No file  | `732ea3f5167c`  |
| 760    | No file  | `732ea3f5167c`  |
| 748    | No file  | `732ea3f5167c`  |
| 741    | No file  | `732ea3f5167c`  |
| 736    | No file  | `732ea3f5167c`  |
| 731    | No file  | `732ea3f5167c`  |
| 723    | No file  | `732ea3f5167c`  |
| 711    | No file  | `732ea3f5167c`  |
| 707    | No file  | `732ea3f5167c`  |
| 697    | No file  | `732ea3f5167c`  |
| 689    | No file  | `732ea3f5167c`  |
| 683    | No file  | `732ea3f5167c`  |
| 678    | No file  | `732ea3f5167c`  |
| 670    | No file  | `732ea3f5167c`  |
| 661    | No file  | `732ea3f5167c`  |
| 656    | No file  | `732ea3f5167c`  |
| 652    | No file  | `732ea3f5167c`  |
| 643    | No file  | `732ea3f5167c`  |
| 637    | No file  | `732ea3f5167c`  |
| 630    | No file  | `732ea3f5167c`  |
| 627    | No file  | `732ea3f5167c`  |
| 621    | No file  | `732ea3f5167c`  |
| 617    | No file  | `732ea3f5167c`  |
| 615    | No file  | `732ea3f5167c`  |
| 606    | No file  | `732ea3f5167c`  |
| 599    | No file  | `732ea3f5167c`  |
| 592    | No file  | `732ea3f5167c`  |
| 586    | No file  | `732ea3f5167c`  |
| 577    | No file  | `732ea3f5167c`  |
| 569    | No file  | `732ea3f5167c`  |
| 561    | No file  | `732ea3f5167c`  |
| 554    | No file  | `732ea3f5167c`  |
| 542    | No file  | `732ea3f5167c`  |
| 532    | No file  | `732ea3f5167c`  |
| 531    | No file  | `732ea3f5167c`  |
| 526    | No file  | `732ea3f5167c`  |
| 521    | No file  | `732ea3f5167c`  |
| 517    | No file  | `732ea3f5167c`  |
| 510    | No file  | `732ea3f5167c`  |
| 508    | No file  | `732ea3f5167c`  |
| 504    | No file  | `732ea3f5167c`  |
| 497    | No file  | `732ea3f5167c`  |
| 491    | No file  | `732ea3f5167c`  |
| 485    | No file  | `732ea3f5167c`  |
| 478    | No file  | `732ea3f5167c`  |
| 472    | No file  | `732ea3f5167c`  |
| 466    | No file  | `732ea3f5167c`  |
| 457    | No file  | `732ea3f5167c`  |
| 452    | No file  | `732ea3f5167c`  |
| 449    | No file  | `732ea3f5167c`  |
| 435    | No file  | `732ea3f5167c`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                      |
| ------------------------- | -------- | --------------------------------------------------------- |
| `extractitemoffset.dbss`  | Optional | `item_id -> (data_offset, data_size)` index, see below; the rows can be walked without it |
| [`itemimprovement.dbss`](itemimprovement_dbss.md) | Optional | Reform records; the handler's Reform Group column, see Notes |
| [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md) | Optional | Reform stone groups; picks one group when a reform pair has several |

Item names come from LOC type 0.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                                     |
| ------- | ---------- | ----- | --------------------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `2,336` on client 3464                    |
| `+0x04` | Row[count] | rows  | `count` 48-byte rows, back to back to the end of the file |

### Row (48 bytes)

The row is four 12-byte slots of a u32 item ID and its u64 count. Every
count is `1` on all 2,336 rows (client 3473).

| Offset  | Type | Field                 | Notes                                                         |
| ------- | ---- | --------------------- | ------------------------------------------------------------- |
| `+0x00` | u32  | item_id               | Reformed gear the window takes; unique per row, the index key |
| `+0x04` | u64  | item_count            | Fixed `1`, see Field Names                                    |
| `+0x0C` | u32  | need_item_id          | Item the extraction uses up, see below                        |
| `+0x10` | u64  | need_item_count       | How many `need_item_id` the extraction uses up                |
| `+0x18` | u32  | result_item_id        | Gear returned; never equal to `item_id`                       |
| `+0x1C` | u64  | result_item_count     | Fixed `1`, see Field Names                                    |
| `+0x24` | u32  | result_material_id    | Reform stone (or other material) returned                     |
| `+0x28` | u64  | result_material_count | Fixed `1`, see Field Names                                    |

Byte `+0x03` of each item ID is `0` on every row, so no ID carries an
enchant level in its top byte. The rows are not sorted by `item_id`.

Each `result_material_id` goes with one `need_item_id` (client 3464):

| need_item_id                         | result_material_id                                   | Rows |
| ------------------------------------ | ---------------------------------------------------- | ---- |
| `320060` Mirror of Equilibrium       | `9771` Inverted Heart of Garmoth                     | 844  |
| `320060` Mirror of Equilibrium       | `9793` Heart of Kutum                                | 455  |
| `320060` Mirror of Equilibrium       | `9787` Heart of Karanda                              | 363  |
| `320060` Mirror of Equilibrium       | `8421` Blessed Soul Fragment, `8432` Exalted Soul Fragment | 26 each |
| `320060` Mirror of Equilibrium       | Six Cups (`8141`, `8148`, `8149`, `8181`, `8182`, `8417`) | 10 each |
| `320060` Mirror of Equilibrium       | `9788` Obsidian Specter's Energy                     | 4    |
| `320060` Mirror of Equilibrium       | `820974` to `820977` Cups, `821251` Flawless Herald's Crystal | 3 each |
| `320060` Mirror of Equilibrium       | `820018` Gauche Rawr-Rawr's Heart                    | 2    |
| `320060` Mirror of Equilibrium       | `820969` Crimson Behelit Alchemy Stone Appearance    | 1    |
| `4929` Restoration Stone             | `4912` Ultimate Weapon Reform Stone                  | 407  |
| `4929` Restoration Stone             | `4913` Ultimate Armor Reform Stone                   | 44   |
| `4929` Restoration Stone             | `8179` Sunset Glow Crystal                           | 6    |
| `8172` Combatant's Restoration Stone | `8170` Combatant's Stone (Weapon)                    | 79   |
| `8172` Combatant's Restoration Stone | `8171` Combatant's Stone (Armor)                     | 4    |

The three need items' own texts list these pairs: the Mirror of Equilibrium
(TextBind `MIRROR_OF_EQUILIBRIUM`) reads "Extract Heart of Karanda from
Storm Devoured gear", "Extract Inverted Heart of Garmoth from Fiery gear"
and so on; Restoration Stone (`4929`) names the two Ultimate Reform Stones
and Sunset Glow Crystal; Combatant's Restoration Stone (`8172`) names the
two Combatant's Stones.

### `extractitemoffset.dbss`

| Offset  | Type             | Field | Notes                                      |
| ------- | ---------------- | ----- | ------------------------------------------ |
| `+0x00` | u32              | count | Equals the `extractitem.dbss` count        |
| `+0x04` | Index Row[count] | rows  | `count` 12-byte rows; no magic, no trailer |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                         |
| ------- | ---- | ----------- | --------------------------------------------- |
| `+0x00` | u32  | item_id     | Row key, the `item_id` at `data_offset`       |
| `+0x04` | u32  | data_offset | Row start, the `item_id` itself (not past it) |
| `+0x08` | u32  | data_size   | `48`, the whole row                           |

Unlike the `itemimprovementoffset.dbss` index, `data_offset` points at the
key and `data_size` covers it. The index rows are not in file order; on
client 3464 the 2,336 offsets are exactly the 2,336 row starts, and the key
at each offset equals the index `item_id`.

## Field Names

The row is the `Item_ImprovementExtract_Table` sheet that a private server
on client 1784 ships in its `DataSheets.bexcel`. Its columns are
`ExtractionItem`, `NeedExtractMaterialKey`, `NeedExtractMaterialCount`,
`ExtractDropItem1`, `ExtractDropItem2` and `ContentsGroupKey`; the last one
is not in the row.

| Field                 | Column                     |
| --------------------- | -------------------------- |
| `item_id`             | `ExtractionItem`           |
| `need_item_id`        | `NeedExtractMaterialKey`   |
| `need_item_count`     | `NeedExtractMaterialCount` |
| `result_item_id`      | `ExtractDropItem1`         |
| `result_material_id`  | `ExtractDropItem2`         |

Matched by `ExtractionItem` against client 3473, the sheet and the client
file share 1,127 keys. `need_item_id` and `result_item_id` match on all
1,127 and `result_material_id` on 1,086; the other 41 are Cups whose key
changed (sheet `8135`, `8146` and `8147`, client `8141`, `8148`, `8149`,
`8181` and `8182`). That private server's own `extractitem.dbss`, built from
the sheet, holds 1,196 rows; all three item columns match on every one.

`NeedExtractMaterialCount` is `1` on every sheet row, so the values do not
place it. The server dump of that private server does. Its
`Item_ImprovementExtract_Table` loader builds four (item key, 8-byte count)
pairs per row, in row order: `ExtractionItem` with a literal count of `1`,
`NeedExtractMaterialKey` with `NeedExtractMaterialCount`, then
`ExtractDropItem1` and `ExtractDropItem2` (one `ExtractDropItem%#` string,
read for 1 and 2), each with a literal `1`. It rejects a row when any key is
`0` or any count is not above `0`. So `need_item_count` is the only count
the sheet sets, and the other three are `1` by the loader.

Neither the 2016 client with debug symbols nor the tables of a private server on
client 519 have an extraction type or table.

## Notes

- The window is `panel_window_extraction_system_all`
  (`PaGlobal_Extraction_System_All`, decompiled with unluac). For the item in
  the window it calls `ToClient_ExtractNeedItemEnchantKey(itemKey)` for the
  item to use up (shown with `PANEL_EXTRACTIONSYSTEM_NEEDCATALYST` "※ You
  need a [{itemName}]." when the inventory has none),
  `ToClient_ExtractToItemEnchantKey(itemKey, 0)` for the result item and
  `ToClient_ExtractToItemEnchantKey(itemKey, 1)` for the result material, the
  three IDs at `+0x0C`, `+0x18` and `+0x24`. The inventory list takes items
  for which `ToClient_isExtractFromItem(key)` is true, and the request is
  `ToClient_requestExtractItem(extractableSlotNo, materialSlotNo)`. The
  result line is `LUA_EXTRACTIONSYSTEM_RESULTMSG` "{item1} and {itme2} were
  separated.", and the two result icons hide their count. The need item is
  drawn with a literal `1` (or `0` when the inventory has none), not with
  `need_item_count`.
- The window refuses gear with Caphras EXP (`LUA_EXTRACTIONSYSTEM_FAIL_DESC_1`)
  or transfused crystals (`LUA_EXTRACTIONSYSTEM_FAIL_DESC_2`); the table has no
  field for either.
- A row is a [`itemimprovement.dbss`](itemimprovement_dbss.md) reform run
  backwards. On client 3464, 2,323 of the 2,336 rows have a 5-item reform
  record whose result is `item_id` and whose input is `result_item_id`, and
  `result_material_id` is a stone of that record's group in
  [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md). This holds
  for all three need items, the Ultimate and Combatant's gear included.
  20 (result, input) pairs have reform records in two groups; on the 10
  rows that hit one (client 3464), Dandelion Purgatum gear from `742928` to
  `743330`, only one of the two groups holds `result_material_id` as a
  stone. The handler's Reform Group is that one group, and `-` on the other
  13 rows.
- The other 13 rows (client 3464) return a different gear key than the
  reform input: ten Dandelion Purgatum rows (`742932`, `742933`, `743032`,
  `743033`, `743132`, `743133`, `743232`, `743233`, `743332`, `743333`) and
  three Hexround rows (`736624`, `736724`, `736824`). For example `743332`
  (Fiery Dandelion Purgatum) is reformed from `743232` but extracts to
  `743231` (Dandelion Purgatum).
- 41 `result_item_id` values (client 3464) are themselves an `item_id` of
  another row, so reformed gear can be extracted down more than one step.
- One `item_id` has no LOC type 0 name on client 3464: `748603`, which
  extracts to `748601` Dandelion Enlightened Blade and Heart of Karanda. The
  handler shows the Korean name `itemenchant.dbss` stores for it
  (폭풍을 삼킨 단델리온 선검).
- calpheonlabs' page gives the example `731222` and `320060` to `694273` and
  `9771` (Inverted Heart of Garmoth). On client 3464 the `731222` row returns
  `9787` (Heart of Karanda), which is what the Mirror of Equilibrium text
  says for Storm Devoured gear; its capture has 2,328 rows.

## Open Questions

### Enchant Level on the Key

The Lua passes the item's `getKey()`, an item enchant key, to
`ToClient_isExtractFromItem` and the two lookup functions, while the table
stores plain item IDs. Whether the client drops the enchant level before
the lookup, and whether the returned gear keeps the enchant level of the
extracted gear, is not in the table.
