# `dialogtext.dbss` Format

## Purpose

Stores named pools of NPC lines. A dialog greeting in `detail_dialog.dbss` can be the tag `{GetRandomText(<name>)}`, and the client then shows a random line from the pool with that name each time the dialog opens. Most lines start with an `{AudioVoice(...)}` tag that names the voice file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                    | Bytes   | Records                                     | Row bytes                 |
| ------ | -------------- | ----------------------- | ------- | ------------------------------------------- | ------------------------- |
| 1      | 1346 and later | `dialogtext.dbss`       | 614,336 | 3,645 Line, 1,043 Pool Record, 1,043 Record | 20 to 308, 153 on average |
| 1      | 1346 and later | `dialogtextoffset.dbss` | 12,520  | 1,043 Index Row                             | 12                        |

| Layout | File                    | Known             | Unknown        |
| ------ | ----------------------- | ----------------- | -------------- |
| 1      | `dialogtext.dbss`       | 610,164 B (99.3%) | 4,172 B (0.7%) |
| 1      | `dialogtextoffset.dbss` | 12,520 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `e5d537413524`  |
| 3482   | Layout 1             | `e5d537413524`  |
| 3474   | Layout 1             | `e5d537413524`  |
| 3473   | Layout 1             | `e5d537413524`  |
| 3464   | Layout 1             | `e5d537413524`  |
| 3458   | Layout 1             | `e5d537413524`  |
| 3454   | Layout 1             | `e5d537413524`  |
| 3444   | Layout 1             | `e5d537413524`  |
| 3435   | Layout 1             | `e5d537413524`  |
| 3426   | Layout 1             | `e5d537413524`  |
| 3418   | Layout 1             | `e5d537413524`  |
| 3412   | Layout 1             | `e5d537413524`  |
| 3402   | Layout 1             | `e5d537413524`  |
| 3396   | Layout 1             | `e5d537413524`  |
| 3387   | Layout 1             | `e5d537413524`  |
| 3381   | Layout 1             | `e5d537413524`  |
| 3373   | Layout 1             | `e5d537413524`  |
| 3364   | Layout 1             | `e5d537413524`  |
| 3356   | Layout 1             | `e5d537413524`  |
| 3349   | Layout 1             | `e5d537413524`  |
| 3342   | Layout 1             | `e5d537413524`  |
| 3335   | Layout 1             | `e5d537413524`  |
| 3326   | Layout 1             | `e5d537413524`  |
| 3321   | Layout 1             | `e5d537413524`  |
| 3314   | Layout 1             | `e5d537413524`  |
| 3303   | Layout 1             | `e5d537413524`  |
| 3302   | Layout 1             | `e5d537413524`  |
| 3293   | Layout 1             | `e5d537413524`  |
| 3283   | Layout 1             | `e5d537413524`  |
| 3275   | Layout 1             | `e5d537413524`  |
| 3267   | Layout 1             | `e5d537413524`  |
| 3258   | Layout 1             | `e5d537413524`  |
| 3251   | Layout 1             | `e5d537413524`  |
| 3242   | Layout 1             | `e5d537413524`  |
| 3235   | Layout 1             | `e5d537413524`  |
| 3229   | Layout 1             | `e5d537413524`  |
| 3212   | Layout 1             | `e5d537413524`  |
| 3203   | Layout 1             | `e5d537413524`  |
| 3193   | Layout 1             | `e5d537413524`  |
| 3186   | Layout 1             | `e5d537413524`  |
| 3177   | Layout 1             | `e5d537413524`  |
| 3169   | Layout 1             | `e5d537413524`  |
| 3158   | Layout 1             | `e5d537413524`  |
| 3151   | Layout 1             | `e5d537413524`  |
| 3144   | Layout 1             | `e5d537413524`  |
| 3133   | Layout 1             | `e5d537413524`  |
| 3125   | Layout 1             | `e5d537413524`  |
| 3118   | Layout 1             | `e5d537413524`  |
| 3111   | Layout 1             | `e5d537413524`  |
| 3103   | Layout 1             | `e5d537413524`  |
| 3095   | Layout 1             | `e5d537413524`  |
| 3086   | Layout 1             | `e5d537413524`  |
| 3072   | Layout 1             | `e5d537413524`  |
| 3062   | Layout 1             | `e5d537413524`  |
| 3052   | Layout 1             | `e5d537413524`  |
| 3045   | Layout 1             | `e5d537413524`  |
| 3037   | Layout 1             | `e5d537413524`  |
| 3030   | Layout 1             | `e5d537413524`  |
| 3021   | Layout 1             | `e5d537413524`  |
| 3012   | Layout 1             | `e5d537413524`  |
| 3002   | Layout 1             | `e5d537413524`  |
| 2995   | Layout 1             | `e5d537413524`  |
| 2987   | Layout 1             | `e5d537413524`  |
| 2978   | No documented layout | `e5d537413524`  |
| 2970   | No documented layout | `e5d537413524`  |
| 2959   | No documented layout | `e5d537413524`  |
| 2951   | Layout 1             | `e5d537413524`  |
| 2942   | Layout 1             | `e5d537413524`  |
| 2935   | Layout 1             | `e5d537413524`  |
| 2932   | Layout 1             | `e5d537413524`  |
| 2923   | Layout 1             | `e5d537413524`  |
| 2919   | Layout 1             | `e5d537413524`  |
| 2907   | Layout 1             | `e5d537413524`  |
| 2900   | Layout 1             | `e5d537413524`  |
| 2891   | Layout 1             | `e5d537413524`  |
| 2882   | Layout 1             | `e5d537413524`  |
| 2872   | Layout 1             | `e5d537413524`  |
| 2863   | Layout 1             | `e5d537413524`  |
| 2855   | Layout 1             | `e5d537413524`  |
| 2849   | Layout 1             | `e5d537413524`  |
| 2844   | Layout 1             | `e5d537413524`  |
| 2834   | Layout 1             | `e5d537413524`  |
| 2825   | Layout 1             | `e5d537413524`  |
| 2819   | Layout 1             | `e5d537413524`  |
| 2811   | Layout 1             | `e5d537413524`  |
| 2803   | Layout 1             | `e5d537413524`  |
| 2794   | Layout 1             | `e5d537413524`  |
| 2783   | Layout 1             | `e5d537413524`  |
| 2774   | Layout 1             | `e5d537413524`  |
| 2765   | Layout 1             | `e5d537413524`  |
| 2756   | Layout 1             | `e5d537413524`  |
| 2750   | Layout 1             | `e5d537413524`  |
| 2743   | Layout 1             | `e5d537413524`  |
| 2736   | Layout 1             | `e5d537413524`  |
| 2726   | Layout 1             | `e5d537413524`  |
| 2717   | Layout 1             | `e5d537413524`  |
| 2709   | Layout 1             | `e5d537413524`  |
| 2703   | Layout 1             | `e5d537413524`  |
| 2695   | Layout 1             | `e5d537413524`  |
| 2684   | Layout 1             | `e5d537413524`  |
| 2672   | Layout 1             | `e5d537413524`  |
| 2665   | Layout 1             | `e5d537413524`  |
| 2657   | Layout 1             | `e5d537413524`  |
| 2649   | Layout 1             | `e5d537413524`  |
| 2644   | Layout 1             | `e5d537413524`  |
| 2637   | Layout 1             | `e5d537413524`  |
| 2629   | Layout 1             | `e5d537413524`  |
| 2619   | Layout 1             | `e5d537413524`  |
| 2612   | Layout 1             | `e5d537413524`  |
| 2606   | Layout 1             | `e5d537413524`  |
| 2602   | Layout 1             | `e5d537413524`  |
| 2601   | Layout 1             | `e5d537413524`  |
| 2592   | Layout 1             | `e5d537413524`  |
| 2583   | Layout 1             | `e5d537413524`  |
| 2575   | Layout 1             | `e5d537413524`  |
| 2567   | Layout 1             | `e5d537413524`  |
| 2560   | Layout 1             | `e5d537413524`  |
| 2553   | Layout 1             | `e5d537413524`  |
| 2545   | Layout 1             | `e5d537413524`  |
| 2538   | Layout 1             | `e5d537413524`  |
| 2529   | Layout 1             | `e5d537413524`  |
| 2519   | Layout 1             | `e5d537413524`  |
| 2513   | Layout 1             | `e5d537413524`  |
| 2510   | Layout 1             | `e5d537413524`  |
| 2507   | Layout 1             | `e5d537413524`  |
| 2503   | Layout 1             | `e5d537413524`  |
| 2498   | Layout 1             | `e5d537413524`  |
| 2492   | Layout 1             | `e5d537413524`  |
| 2487   | Layout 1             | `e5d537413524`  |
| 2480   | Layout 1             | `e5d537413524`  |
| 2474   | Layout 1             | `e5d537413524`  |
| 2468   | Layout 1             | `e5d537413524`  |
| 2460   | Layout 1             | `e5d537413524`  |
| 2453   | Layout 1             | `e5d537413524`  |
| 2444   | Layout 1             | `e5d537413524`  |
| 2438   | Layout 1             | `e5d537413524`  |
| 2434   | Layout 1             | `e5d537413524`  |
| 2429   | Layout 1             | `e5d537413524`  |
| 2421   | Layout 1             | `e5d537413524`  |
| 2414   | Layout 1             | `e5d537413524`  |
| 2407   | Layout 1             | `e5d537413524`  |
| 2401   | Layout 1             | `e5d537413524`  |
| 2397   | Layout 1             | `e5d537413524`  |
| 2393   | Layout 1             | `e5d537413524`  |
| 2384   | Layout 1             | `e5d537413524`  |
| 2378   | Layout 1             | `e5d537413524`  |
| 2372   | Layout 1             | `e5d537413524`  |
| 2358   | Layout 1             | `e5d537413524`  |
| 2352   | Layout 1             | `e5d537413524`  |
| 2347   | Layout 1             | `e5d537413524`  |
| 2343   | Layout 1             | `e5d537413524`  |
| 2335   | Layout 1             | `e5d537413524`  |
| 2327   | Layout 1             | `e5d537413524`  |
| 2324   | Layout 1             | `e5d537413524`  |
| 2319   | Layout 1             | `e5d537413524`  |
| 2313   | Layout 1             | `e5d537413524`  |
| 2308   | Layout 1             | `e5d537413524`  |
| 2302   | Layout 1             | `e5d537413524`  |
| 2295   | Layout 1             | `e5d537413524`  |
| 2290   | Layout 1             | `e5d537413524`  |
| 2284   | Layout 1             | `e5d537413524`  |
| 2276   | Layout 1             | `e5d537413524`  |
| 2269   | Layout 1             | `e5d537413524`  |
| 2259   | Layout 1             | `e5d537413524`  |
| 2250   | Layout 1             | `e5d537413524`  |
| 2243   | Layout 1             | `e5d537413524`  |
| 2235   | Layout 1             | `e5d537413524`  |
| 2229   | Layout 1             | `e5d537413524`  |
| 2224   | Layout 1             | `e5d537413524`  |
| 2218   | Layout 1             | `e5d537413524`  |
| 2215   | Layout 1             | `e5d537413524`  |
| 2207   | Layout 1             | `e5d537413524`  |
| 2203   | Layout 1             | `e5d537413524`  |
| 2196   | Layout 1             | `e5d537413524`  |
| 2192   | Layout 1             | `e5d537413524`  |
| 2189   | Layout 1             | `e5d537413524`  |
| 2183   | Layout 1             | `e5d537413524`  |
| 2179   | Layout 1             | `e5d537413524`  |
| 2171   | Layout 1             | `e5d537413524`  |
| 2163   | Layout 1             | `e5d537413524`  |
| 2156   | Layout 1             | `e5d537413524`  |
| 2151   | Layout 1             | `e5d537413524`  |
| 2147   | Layout 1             | `e5d537413524`  |
| 2142   | Layout 1             | `e5d537413524`  |
| 2138   | Layout 1             | `e5d537413524`  |
| 2134   | Layout 1             | `e5d537413524`  |
| 2130   | Layout 1             | `e5d537413524`  |
| 2122   | Layout 1             | `e5d537413524`  |
| 2107   | Layout 1             | `e5d537413524`  |
| 2098   | Layout 1             | `e5d537413524`  |
| 2089   | Layout 1             | `e5d537413524`  |
| 2081   | Layout 1             | `e5d537413524`  |
| 2073   | Layout 1             | `e5d537413524`  |
| 2067   | Layout 1             | `e5d537413524`  |
| 2063   | Layout 1             | `e5d537413524`  |
| 2059   | Layout 1             | `e5d537413524`  |
| 2052   | Layout 1             | `e5d537413524`  |
| 2044   | Layout 1             | `e5d537413524`  |
| 2039   | Layout 1             | `e5d537413524`  |
| 2032   | Layout 1             | `e5d537413524`  |
| 2025   | Layout 1             | `e5d537413524`  |
| 2011   | Layout 1             | `e5d537413524`  |
| 2005   | Layout 1             | `e5d537413524`  |
| 2000   | Layout 1             | `e5d537413524`  |
| 1996   | Layout 1             | `e5d537413524`  |
| 1991   | Layout 1             | `e5d537413524`  |
| 1985   | Layout 1             | `e5d537413524`  |
| 1980   | Layout 1             | `e5d537413524`  |
| 1969   | Layout 1             | `e5d537413524`  |
| 1964   | Layout 1             | `e5d537413524`  |
| 1958   | Layout 1             | `e5d537413524`  |
| 1950   | Layout 1             | `e5d537413524`  |
| 1945   | Layout 1             | `e5d537413524`  |
| 1937   | Layout 1             | `e5d537413524`  |
| 1933   | Layout 1             | `e5d537413524`  |
| 1927   | Layout 1             | `e5d537413524`  |
| 1921   | Layout 1             | `e5d537413524`  |
| 1914   | Layout 1             | `e5d537413524`  |
| 1908   | Layout 1             | `e5d537413524`  |
| 1897   | Layout 1             | `e5d537413524`  |
| 1892   | Layout 1             | `e5d537413524`  |
| 1886   | Layout 1             | `e5d537413524`  |
| 1881   | Layout 1             | `e5d537413524`  |
| 1871   | Layout 1             | `e5d537413524`  |
| 1866   | Layout 1             | `e5d537413524`  |
| 1862   | Layout 1             | `e5d537413524`  |
| 1854   | Layout 1             | `e5d537413524`  |
| 1846   | Layout 1             | `e5d537413524`  |
| 1838   | Layout 1             | `e5d537413524`  |
| 1832   | Layout 1             | `e5d537413524`  |
| 1826   | Layout 1             | `e5d537413524`  |
| 1822   | Layout 1             | `e5d537413524`  |
| 1818   | Layout 1             | `e5d537413524`  |
| 1804   | Layout 1             | `e5d537413524`  |
| 1794   | Layout 1             | `e5d537413524`  |
| 1790   | Layout 1             | `e5d537413524`  |
| 1784   | Layout 1             | `e5d537413524`  |
| 1774   | Layout 1             | `e5d537413524`  |
| 1771   | Layout 1             | `e5d537413524`  |
| 1762   | Layout 1             | `e5d537413524`  |
| 1759   | Layout 1             | `e5d537413524`  |
| 1754   | Layout 1             | `e5d537413524`  |
| 1749   | Layout 1             | `e5d537413524`  |
| 1743   | Layout 1             | `e5d537413524`  |
| 1737   | Layout 1             | `e5d537413524`  |
| 1731   | Layout 1             | `e5d537413524`  |
| 1725   | Layout 1             | `e5d537413524`  |
| 1717   | Layout 1             | `e5d537413524`  |
| 1710   | Layout 1             | `e5d537413524`  |
| 1704   | Layout 1             | `e5d537413524`  |
| 1698   | Layout 1             | `e5d537413524`  |
| 1690   | Layout 1             | `e5d537413524`  |
| 1685   | Layout 1             | `e5d537413524`  |
| 1680   | Layout 1             | `e5d537413524`  |
| 1674   | Layout 1             | `e5d537413524`  |
| 1668   | Layout 1             | `e5d537413524`  |
| 1659   | Layout 1             | `e5d537413524`  |
| 1649   | Layout 1             | `e5d537413524`  |
| 1642   | Layout 1             | `e5d537413524`  |
| 1636   | Layout 1             | `e5d537413524`  |
| 1628   | Layout 1             | `e5d537413524`  |
| 1622   | Layout 1             | `e5d537413524`  |
| 1614   | Layout 1             | `e5d537413524`  |
| 1608   | Layout 1             | `e5d537413524`  |
| 1602   | Layout 1             | `e5d537413524`  |
| 1598   | Layout 1             | `e5d537413524`  |
| 1594   | Layout 1             | `e5d537413524`  |
| 1590   | Layout 1             | `e5d537413524`  |
| 1587   | Layout 1             | `e5d537413524`  |
| 1584   | Layout 1             | `e5d537413524`  |
| 1579   | Layout 1             | `e5d537413524`  |
| 1572   | Layout 1             | `e5d537413524`  |
| 1565   | Layout 1             | `e5d537413524`  |
| 1559   | Layout 1             | `e5d537413524`  |
| 1554   | Layout 1             | `e5d537413524`  |
| 1547   | Layout 1             | `e5d537413524`  |
| 1537   | Layout 1             | `e5d537413524`  |
| 1529   | Layout 1             | `e5d537413524`  |
| 1524   | Layout 1             | `e5d537413524`  |
| 1519   | Layout 1             | `e5d537413524`  |
| 1509   | Layout 1             | `e5d537413524`  |
| 1506   | Layout 1             | `e5d537413524`  |
| 1504   | Layout 1             | `e5d537413524`  |
| 1500   | Layout 1             | `e5d537413524`  |
| 1493   | Layout 1             | `e5d537413524`  |
| 1489   | Layout 1             | `e5d537413524`  |
| 1485   | Layout 1             | `e5d537413524`  |
| 1481   | Layout 1             | `e5d537413524`  |
| 1474   | Layout 1             | `e5d537413524`  |
| 1466   | Layout 1             | `e5d537413524`  |
| 1462   | Layout 1             | `e5d537413524`  |
| 1459   | Layout 1             | `e5d537413524`  |
| 1453   | Layout 1             | `e5d537413524`  |
| 1450   | Layout 1             | `e5d537413524`  |
| 1445   | Layout 1             | `e5d537413524`  |
| 1439   | Layout 1             | `e5d537413524`  |
| 1433   | Layout 1             | `e5d537413524`  |
| 1430   | Layout 1             | `e5d537413524`  |
| 1426   | Layout 1             | `e5d537413524`  |
| 1421   | Layout 1             | `e5d537413524`  |
| 1417   | Layout 1             | `e5d537413524`  |
| 1416   | Layout 1             | `e5d537413524`  |
| 1409   | Layout 1             | `e5d537413524`  |
| 1405   | Layout 1             | `e5d537413524`  |
| 1401   | Layout 1             | `e5d537413524`  |
| 1396   | Layout 1             | `e5d537413524`  |
| 1391   | Layout 1             | `e5d537413524`  |
| 1390   | Layout 1             | `e5d537413524`  |
| 1386   | Layout 1             | `e5d537413524`  |
| 1381   | Layout 1             | `e5d537413524`  |
| 1379   | Layout 1             | `e5d537413524`  |
| 1372   | Layout 1             | `e5d537413524`  |
| 1366   | Layout 1             | `e5d537413524`  |
| 1364   | Layout 1             | `e5d537413524`  |
| 1363   | Layout 1             | `e5d537413524`  |
| 1360   | Layout 1             | `e5d537413524`  |
| 1358   | Layout 1             | `e5d537413524`  |
| 1355   | Layout 1             | `e5d537413524`  |
| 1351   | Layout 1             | `e5d537413524`  |
| 1348   | Layout 1             | `e5d537413524`  |
| 1346   | Layout 1             | `e5d537413524`  |
| 1341   | No documented layout | `e5d537413524`  |
| 1340   | No documented layout | `e5d537413524`  |
| 1338   | No documented layout | `e5d537413524`  |
| 1335   | No documented layout | `e5d537413524`  |
| 1333   | No documented layout | `e5d537413524`  |
| 1329   | No documented layout | `e5d537413524`  |
| 1327   | No documented layout | `e5d537413524`  |
| 1324   | No documented layout | `e5d537413524`  |
| 1321   | No documented layout | `e5d537413524`  |
| 1319   | No documented layout | `e5d537413524`  |
| 1318   | No documented layout | `e5d537413524`  |
| 1316   | No documented layout | `e5d537413524`  |
| 1313   | No documented layout | `e5d537413524`  |
| 1311   | No documented layout | `e5d537413524`  |
| 1309   | No documented layout | `e5d537413524`  |
| 1304   | No documented layout | `e5d537413524`  |
| 1292   | No documented layout | `e5d537413524`  |
| 1286   | No documented layout | `e5d537413524`  |
| 1280   | No documented layout | `e5d537413524`  |
| 1276   | No documented layout | `e5d537413524`  |
| 1267   | No documented layout | `e5d537413524`  |
| 1261   | No documented layout | `e5d537413524`  |
| 1256   | No documented layout | `e5d537413524`  |
| 1250   | No documented layout | `e5d537413524`  |
| 1246   | No documented layout | `e5d537413524`  |
| 1239   | No documented layout | `e5d537413524`  |
| 1230   | No documented layout | `e5d537413524`  |
| 1226   | No documented layout | `e5d537413524`  |
| 1220   | No documented layout | `e5d537413524`  |
| 1217   | No documented layout | `e5d537413524`  |
| 1211   | No file              | `e5d537413524`  |
| 1210   | No file              | `e5d537413524`  |
| 1208   | No file              | `e5d537413524`  |
| 1203   | No file              | `e5d537413524`  |
| 1197   | No file              | `e5d537413524`  |
| 1194   | No file              | `e5d537413524`  |
| 1192   | No file              | `e5d537413524`  |
| 1187   | No file              | `e5d537413524`  |
| 1183   | No file              | `e5d537413524`  |
| 1177   | No file              | `e5d537413524`  |
| 1173   | No file              | `e5d537413524`  |
| 1167   | No file              | `e5d537413524`  |
| 1164   | No file              | `e5d537413524`  |
| 1156   | No file              | `e5d537413524`  |
| 1149   | No file              | `e5d537413524`  |
| 1144   | No file              | `e5d537413524`  |
| 1137   | No file              | `e5d537413524`  |
| 1132   | No file              | `e5d537413524`  |
| 1127   | No file              | `e5d537413524`  |
| 1122   | No file              | `e5d537413524`  |
| 1118   | No file              | `e5d537413524`  |
| 1114   | No file              | `e5d537413524`  |
| 1109   | No file              | `e5d537413524`  |
| 1102   | No file              | `e5d537413524`  |
| 1096   | No file              | `e5d537413524`  |
| 1088   | No file              | `e5d537413524`  |
| 1081   | No file              | `e5d537413524`  |
| 1076   | No file              | `e5d537413524`  |
| 1069   | No file              | `e5d537413524`  |
| 1064   | No file              | `e5d537413524`  |
| 1058   | No file              | `e5d537413524`  |
| 1051   | No file              | `e5d537413524`  |
| 1044   | No file              | `e5d537413524`  |
| 1036   | No file              | `e5d537413524`  |
| 1026   | No file              | `e5d537413524`  |
| 1016   | No file              | `e5d537413524`  |
| 1009   | No file              | `e5d537413524`  |
| 1005   | No file              | `e5d537413524`  |
| 1000   | No file              | `e5d537413524`  |
| 998    | No file              | `e5d537413524`  |
| 990    | No file              | `e5d537413524`  |
| 979    | No file              | `e5d537413524`  |
| 972    | No file              | `e5d537413524`  |
| 963    | No file              | `e5d537413524`  |
| 955    | No file              | `e5d537413524`  |
| 946    | No file              | `e5d537413524`  |
| 938    | No file              | `e5d537413524`  |
| 927    | No file              | `e5d537413524`  |
| 911    | No file              | `e5d537413524`  |
| 904    | No file              | `e5d537413524`  |
| 899    | No file              | `e5d537413524`  |
| 894    | No file              | `e5d537413524`  |
| 885    | No file              | `e5d537413524`  |
| 879    | No file              | `e5d537413524`  |
| 872    | No file              | `e5d537413524`  |
| 864    | No file              | `e5d537413524`  |
| 855    | No file              | `e5d537413524`  |
| 853    | No file              | `e5d537413524`  |
| 845    | No file              | `e5d537413524`  |
| 837    | No file              | `e5d537413524`  |
| 829    | No file              | `e5d537413524`  |
| 822    | No file              | `e5d537413524`  |
| 814    | No file              | `e5d537413524`  |
| 805    | No file              | `e5d537413524`  |
| 794    | No file              | `e5d537413524`  |
| 787    | No file              | `e5d537413524`  |
| 780    | No file              | `e5d537413524`  |
| 771    | No file              | `e5d537413524`  |
| 760    | No file              | `e5d537413524`  |
| 748    | No file              | `e5d537413524`  |
| 741    | No file              | `e5d537413524`  |
| 736    | No file              | `e5d537413524`  |
| 731    | No file              | `e5d537413524`  |
| 723    | No file              | `e5d537413524`  |
| 711    | No file              | `e5d537413524`  |
| 707    | No file              | `e5d537413524`  |
| 697    | No file              | `e5d537413524`  |
| 689    | No file              | `e5d537413524`  |
| 683    | No file              | `e5d537413524`  |
| 678    | No file              | `e5d537413524`  |
| 670    | No file              | `e5d537413524`  |
| 661    | No file              | `e5d537413524`  |
| 656    | No file              | `e5d537413524`  |
| 652    | No file              | `e5d537413524`  |
| 643    | No file              | `e5d537413524`  |
| 637    | No file              | `e5d537413524`  |
| 630    | No file              | `e5d537413524`  |
| 627    | No file              | `e5d537413524`  |
| 621    | No file              | `e5d537413524`  |
| 617    | No file              | `e5d537413524`  |
| 615    | No file              | `e5d537413524`  |
| 606    | No file              | `e5d537413524`  |
| 599    | No file              | `e5d537413524`  |
| 592    | No file              | `e5d537413524`  |
| 586    | No file              | `e5d537413524`  |
| 577    | No file              | `e5d537413524`  |
| 569    | No file              | `e5d537413524`  |
| 561    | No file              | `e5d537413524`  |
| 554    | No file              | `e5d537413524`  |
| 542    | No file              | `e5d537413524`  |
| 532    | No file              | `e5d537413524`  |
| 531    | No file              | `e5d537413524`  |
| 526    | No file              | `e5d537413524`  |
| 521    | No file              | `e5d537413524`  |
| 517    | No file              | `e5d537413524`  |
| 510    | No file              | `e5d537413524`  |
| 508    | No file              | `e5d537413524`  |
| 504    | No file              | `e5d537413524`  |
| 497    | No file              | `e5d537413524`  |
| 491    | No file              | `e5d537413524`  |
| 485    | No file              | `e5d537413524`  |
| 478    | No file              | `e5d537413524`  |
| 472    | No file              | `e5d537413524`  |
| 466    | No file              | `e5d537413524`  |
| 457    | No file              | `e5d537413524`  |
| 452    | No file              | `e5d537413524`  |
| 449    | No file              | `e5d537413524`  |
| 435    | No file              | `e5d537413524`  |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                         |
| ----------------------- | -------- | -------------------------------------------- |
| `dialogtextoffset.dbss` | Required | Maps each pool key to its record offset and size |
| `languagedata_*.loc`    | Optional | The lines in the user's language, LOC type `36` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                                        |
| ------- | ------------- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32           | count   | Number of records; matches the offset file                   |
| `+0x04` | Record[count] | records | Each record is preceded by a repeated copy of its `u32` key; see Record |

As in `detail_dialog.dbss`, the first record starts at `8`, every record starts 4 bytes after the previous one ends, and the last ends at end of file.

### Record (variable: 4 bytes + pool record)

| Offset  | Type        | Field      | Notes                                                       |
| ------- | ----------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32         | key_prefix | Repeated copy of the record's `key`                         |
| `+0x04` | Pool Record | pool       | `size` bytes; the index row's `offset` points at this field |

### Pool Record (variable: 20 bytes + name and lines)

| Offset      | Type             | Field       | Notes |
| ----------- | ---------------- | ----------- | ----- |
| `+0x00`     | u32              | key         | Same as the index key |
| `+0x04`     | str16            | name        | Pool name, unique; e.g. `PEDU_47759_1`, `Morning_47295`, `SnowyMountain_50953` |
| `name+0x00` | u32              | line_count  | `3` on 527 of 1,043 pools, `2` on 222, `4` on 170, up to `30` |
| `name+0x04` | Line[line_count] | lines       | See Line |
| `lines+0x00` | u32              | unknown_end | Always `0`; the record ends exactly here |

### Line (variable: 10 bytes + text)

| Offset  | Type  | Field   | Notes |
| ------- | ----- | ------- | ----- |
| `+0x00` | u16   | text_id | LOC text ID of the line: LOC type `36`, `str_id1 = key`, `str_id2 = text_id`; counts up by one inside a pool, from `1` in 260 pools and from a larger number elsewhere (`379` in `Morning_47295`) |
| `+0x02` | str16 | text    | Korean, usually with a leading `{AudioVoice(...)}` tag; line breaks are the two characters `\n`, not a newline |

All 1,043 records of client 3458 walk with this layout and end exactly at their index size.

### `dialogtextoffset.dbss`

No `PABR` magic and no trailer.

| Offset  | Type             | Field | Notes                                       |
| ------- | ---------------- | ----- | ------------------------------------------- |
| `+0x00` | u32              | count | Number of index rows; `1043` in client 3458 |
| `+0x04` | Index Row[count] | rows  | See Index Row                               |

The key is a u32 unique per pool with no visible structure (`0x24E52C6C` for `PEDU_47759_1`); it is not a plain CRC-32 of the name (ASCII, lowercase or UTF-16).

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                          |
| ------- | ---- | ------ | ---------------------------------------------- |
| `+0x00` | u32  | key    | Pool key                                       |
| `+0x04` | u32  | offset | Byte offset of the record in `dialogtext.dbss` |
| `+0x08` | u32  | size   | Record size in bytes                           |

## Notes

- Checked in game 2026-09-29: Ganin Arth (`47744`) has the greeting `{GetRandomText(PEDU_47744_1)}`, and talking to her three times showed all three pool lines: `1` ("It has been some time, Adventurer..."), `2` ("If you seek to hone your skills, say the word...") and `3` ("I am here to oversee the Hashashin..."). A random line is picked each time the dialog opens, not only on the first talk.
- 82 of the first 200 pool names occur in `detail_dialog.dbss` greetings as `{GetRandomText(<name>)}`.
- The names mostly start with a region or content prefix: `Morning` (290, Land of the Morning Light), `SnowyMountain` (163), `PEDU` (149), `Ulukita` (143), `MediaS` (100), `Olvia` (49).
- 2,931 of the 3,645 lines carry an `{AudioVoice(...)}` tag. The last number of the voice name equals `text_id` on only 553 of them.
- All 3,645 lines have a LOC type `36` row (`36, key, text_id, 0, 0`), e.g. `PEDU_47759_1` line `1`: "{AudioVoice(NPC_VCE_47759_1_1_Jamalko)}Fish for the Imperial..."; the English text keeps the voice tag.
