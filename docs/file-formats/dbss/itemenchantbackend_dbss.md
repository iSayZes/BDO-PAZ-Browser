# `itemenchantbackend.dbss` Format

## Purpose

The back part of every [`itemenchant.dbss`](itemenchant_dbss.md) block: for
each (item, enchant level) the bytes from Message Tail `+0x2B` to the end of
the block. They hold the item fields the `itemenchant.dbss` header does not:
the market price limits, the crystal and gathering fields, the expiration
period, the window the item opens when used (`connect_ui`), the enhancement
difficulty, the use condition script, the Korean description, six counted
lists, the packed key and the crystal group. The front part, from the key to
`life_restrict_type`, is in
[`itemenchantbackendtest.dbss`](itemenchantbackendtest_dbss.md); that doc
has how the three files fit together. `itemenchantbackendoffset.dbss` indexes
the blocks with the keys of `itemenchantoffset.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                            | Bytes       | Records                                                     | Row bytes                    |
| ------ | -------------- | ------------------------------- | ----------- | ----------------------------------------------------------- | ---------------------------- |
| 1      | 3412 and later | `itemenchantbackend.dbss`       | 126,919,140 | 169,345 Block, 114 Popup Result Item, 1,044 Jewel Need Item | 320 to 4,484, 749 on average |
| 1      | 3412 and later | `itemenchantbackendoffset.dbss` | 2,032,160   | 169,345 Offset Row                                          | 12                           |

| Layout | File                            | Known                | Unknown              |
| ------ | ------------------------------- | -------------------- | -------------------- |
| 1      | `itemenchantbackend.dbss`       | 94,245,943 B (74.3%) | 32,673,197 B (25.7%) |
| 1      | `itemenchantbackendoffset.dbss` | 2,032,160 B (100.0%) | 0 B (0.0%)           |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `017505f66b44`  |
| 3482   | Layout 1             | `017505f66b44`  |
| 3474   | Layout 1             | `017505f66b44`  |
| 3473   | Layout 1             | `017505f66b44`  |
| 3464   | Layout 1             | `017505f66b44`  |
| 3458   | Layout 1             | `017505f66b44`  |
| 3454   | Layout 1             | `017505f66b44`  |
| 3444   | Layout 1             | `017505f66b44`  |
| 3435   | Layout 1             | `017505f66b44`  |
| 3426   | Layout 1             | `017505f66b44`  |
| 3418   | Layout 1             | `017505f66b44`  |
| 3412   | Layout 1             | `017505f66b44`  |
| 3402   | No documented layout | `017505f66b44`  |
| 3396   | No documented layout | `017505f66b44`  |
| 3387   | No documented layout | `017505f66b44`  |
| 3381   | No documented layout | `017505f66b44`  |
| 3373   | No documented layout | `017505f66b44`  |
| 3364   | No documented layout | `017505f66b44`  |
| 3356   | No documented layout | `017505f66b44`  |
| 3349   | No documented layout | `017505f66b44`  |
| 3342   | No documented layout | `017505f66b44`  |
| 3335   | No documented layout | `017505f66b44`  |
| 3326   | No documented layout | `017505f66b44`  |
| 3321   | No documented layout | `017505f66b44`  |
| 3314   | No documented layout | `017505f66b44`  |
| 3303   | No documented layout | `017505f66b44`  |
| 3302   | No documented layout | `017505f66b44`  |
| 3293   | No documented layout | `017505f66b44`  |
| 3283   | No documented layout | `017505f66b44`  |
| 3275   | No documented layout | `017505f66b44`  |
| 3267   | No documented layout | `017505f66b44`  |
| 3258   | No documented layout | `017505f66b44`  |
| 3251   | No documented layout | `017505f66b44`  |
| 3242   | No documented layout | `017505f66b44`  |
| 3235   | No documented layout | `017505f66b44`  |
| 3229   | No documented layout | `017505f66b44`  |
| 3212   | No documented layout | `017505f66b44`  |
| 3203   | No documented layout | `017505f66b44`  |
| 3193   | No documented layout | `017505f66b44`  |
| 3186   | No documented layout | `017505f66b44`  |
| 3177   | No documented layout | `017505f66b44`  |
| 3169   | No documented layout | `017505f66b44`  |
| 3158   | No documented layout | `017505f66b44`  |
| 3151   | No documented layout | `017505f66b44`  |
| 3144   | No documented layout | `017505f66b44`  |
| 3133   | No documented layout | `017505f66b44`  |
| 3125   | No documented layout | `017505f66b44`  |
| 3118   | No documented layout | `017505f66b44`  |
| 3111   | No documented layout | `017505f66b44`  |
| 3103   | No documented layout | `017505f66b44`  |
| 3095   | No documented layout | `017505f66b44`  |
| 3086   | No documented layout | `017505f66b44`  |
| 3072   | No documented layout | `017505f66b44`  |
| 3062   | No documented layout | `017505f66b44`  |
| 3052   | No documented layout | `017505f66b44`  |
| 3045   | No documented layout | `017505f66b44`  |
| 3037   | No documented layout | `017505f66b44`  |
| 3030   | No documented layout | `017505f66b44`  |
| 3021   | No documented layout | `017505f66b44`  |
| 3012   | No documented layout | `017505f66b44`  |
| 3002   | No documented layout | `017505f66b44`  |
| 2995   | No documented layout | `017505f66b44`  |
| 2987   | No documented layout | `017505f66b44`  |
| 2978   | No documented layout | `017505f66b44`  |
| 2970   | No documented layout | `017505f66b44`  |
| 2959   | No documented layout | `017505f66b44`  |
| 2951   | No documented layout | `017505f66b44`  |
| 2942   | No documented layout | `017505f66b44`  |
| 2935   | No documented layout | `017505f66b44`  |
| 2932   | No documented layout | `017505f66b44`  |
| 2923   | No documented layout | `017505f66b44`  |
| 2919   | No documented layout | `017505f66b44`  |
| 2907   | No documented layout | `017505f66b44`  |
| 2900   | No documented layout | `017505f66b44`  |
| 2891   | No documented layout | `017505f66b44`  |
| 2882   | No documented layout | `017505f66b44`  |
| 2872   | No documented layout | `017505f66b44`  |
| 2863   | No documented layout | `017505f66b44`  |
| 2855   | No documented layout | `017505f66b44`  |
| 2849   | No documented layout | `017505f66b44`  |
| 2844   | No documented layout | `017505f66b44`  |
| 2834   | No documented layout | `017505f66b44`  |
| 2825   | No documented layout | `017505f66b44`  |
| 2819   | No documented layout | `017505f66b44`  |
| 2811   | No documented layout | `017505f66b44`  |
| 2803   | No documented layout | `017505f66b44`  |
| 2794   | No documented layout | `017505f66b44`  |
| 2783   | No documented layout | `017505f66b44`  |
| 2774   | No documented layout | `017505f66b44`  |
| 2765   | No documented layout | `017505f66b44`  |
| 2756   | No documented layout | `017505f66b44`  |
| 2750   | No documented layout | `017505f66b44`  |
| 2743   | No documented layout | `017505f66b44`  |
| 2736   | No documented layout | `017505f66b44`  |
| 2726   | No documented layout | `017505f66b44`  |
| 2717   | No documented layout | `017505f66b44`  |
| 2709   | No documented layout | `017505f66b44`  |
| 2703   | No documented layout | `017505f66b44`  |
| 2695   | No documented layout | `017505f66b44`  |
| 2684   | No documented layout | `017505f66b44`  |
| 2672   | No documented layout | `017505f66b44`  |
| 2665   | No documented layout | `017505f66b44`  |
| 2657   | No documented layout | `017505f66b44`  |
| 2649   | No documented layout | `017505f66b44`  |
| 2644   | No documented layout | `017505f66b44`  |
| 2637   | No documented layout | `017505f66b44`  |
| 2629   | No documented layout | `017505f66b44`  |
| 2619   | No documented layout | `017505f66b44`  |
| 2612   | No documented layout | `017505f66b44`  |
| 2606   | No documented layout | `017505f66b44`  |
| 2602   | No documented layout | `017505f66b44`  |
| 2601   | No documented layout | `017505f66b44`  |
| 2592   | No documented layout | `017505f66b44`  |
| 2583   | No documented layout | `017505f66b44`  |
| 2575   | No documented layout | `017505f66b44`  |
| 2567   | No documented layout | `017505f66b44`  |
| 2560   | No documented layout | `017505f66b44`  |
| 2553   | No documented layout | `017505f66b44`  |
| 2545   | No documented layout | `017505f66b44`  |
| 2538   | No documented layout | `017505f66b44`  |
| 2529   | No documented layout | `017505f66b44`  |
| 2519   | No documented layout | `017505f66b44`  |
| 2513   | No documented layout | `017505f66b44`  |
| 2510   | No documented layout | `017505f66b44`  |
| 2507   | No documented layout | `017505f66b44`  |
| 2503   | No documented layout | `017505f66b44`  |
| 2498   | No documented layout | `017505f66b44`  |
| 2492   | No documented layout | `017505f66b44`  |
| 2487   | No documented layout | `017505f66b44`  |
| 2480   | No documented layout | `017505f66b44`  |
| 2474   | No documented layout | `017505f66b44`  |
| 2468   | No documented layout | `017505f66b44`  |
| 2460   | No documented layout | `017505f66b44`  |
| 2453   | No documented layout | `017505f66b44`  |
| 2444   | No documented layout | `017505f66b44`  |
| 2438   | No documented layout | `017505f66b44`  |
| 2434   | No documented layout | `017505f66b44`  |
| 2429   | No documented layout | `017505f66b44`  |
| 2421   | No documented layout | `017505f66b44`  |
| 2414   | No documented layout | `017505f66b44`  |
| 2407   | No documented layout | `017505f66b44`  |
| 2401   | No documented layout | `017505f66b44`  |
| 2397   | No documented layout | `017505f66b44`  |
| 2393   | No documented layout | `017505f66b44`  |
| 2384   | No documented layout | `017505f66b44`  |
| 2378   | No documented layout | `017505f66b44`  |
| 2372   | No documented layout | `017505f66b44`  |
| 2358   | No documented layout | `017505f66b44`  |
| 2352   | No documented layout | `017505f66b44`  |
| 2347   | No documented layout | `017505f66b44`  |
| 2343   | No documented layout | `017505f66b44`  |
| 2335   | No documented layout | `017505f66b44`  |
| 2327   | No documented layout | `017505f66b44`  |
| 2324   | No documented layout | `017505f66b44`  |
| 2319   | No documented layout | `017505f66b44`  |
| 2313   | No documented layout | `017505f66b44`  |
| 2308   | No documented layout | `017505f66b44`  |
| 2302   | No documented layout | `017505f66b44`  |
| 2295   | No documented layout | `017505f66b44`  |
| 2290   | No documented layout | `017505f66b44`  |
| 2284   | No documented layout | `017505f66b44`  |
| 2276   | No documented layout | `017505f66b44`  |
| 2269   | No documented layout | `017505f66b44`  |
| 2259   | No documented layout | `017505f66b44`  |
| 2250   | No documented layout | `017505f66b44`  |
| 2243   | No documented layout | `017505f66b44`  |
| 2235   | No documented layout | `017505f66b44`  |
| 2229   | No documented layout | `017505f66b44`  |
| 2224   | No documented layout | `017505f66b44`  |
| 2218   | No documented layout | `017505f66b44`  |
| 2215   | No documented layout | `017505f66b44`  |
| 2207   | No documented layout | `017505f66b44`  |
| 2203   | No documented layout | `017505f66b44`  |
| 2196   | No documented layout | `017505f66b44`  |
| 2192   | No documented layout | `017505f66b44`  |
| 2189   | No documented layout | `017505f66b44`  |
| 2183   | No documented layout | `017505f66b44`  |
| 2179   | No documented layout | `017505f66b44`  |
| 2171   | No documented layout | `017505f66b44`  |
| 2163   | No documented layout | `017505f66b44`  |
| 2156   | No documented layout | `017505f66b44`  |
| 2151   | No documented layout | `017505f66b44`  |
| 2147   | No documented layout | `017505f66b44`  |
| 2142   | No documented layout | `017505f66b44`  |
| 2138   | No documented layout | `017505f66b44`  |
| 2134   | No documented layout | `017505f66b44`  |
| 2130   | No documented layout | `017505f66b44`  |
| 2122   | No documented layout | `017505f66b44`  |
| 2107   | No documented layout | `017505f66b44`  |
| 2098   | No documented layout | `017505f66b44`  |
| 2089   | No documented layout | `017505f66b44`  |
| 2081   | No documented layout | `017505f66b44`  |
| 2073   | No documented layout | `017505f66b44`  |
| 2067   | No documented layout | `017505f66b44`  |
| 2063   | No documented layout | `017505f66b44`  |
| 2059   | No documented layout | `017505f66b44`  |
| 2052   | No documented layout | `017505f66b44`  |
| 2044   | No documented layout | `017505f66b44`  |
| 2039   | No documented layout | `017505f66b44`  |
| 2032   | No documented layout | `017505f66b44`  |
| 2025   | No documented layout | `017505f66b44`  |
| 2011   | No documented layout | `017505f66b44`  |
| 2005   | No documented layout | `017505f66b44`  |
| 2000   | No documented layout | `017505f66b44`  |
| 1996   | No documented layout | `017505f66b44`  |
| 1991   | No documented layout | `017505f66b44`  |
| 1985   | No documented layout | `017505f66b44`  |
| 1980   | No documented layout | `017505f66b44`  |
| 1969   | No documented layout | `017505f66b44`  |
| 1964   | No documented layout | `017505f66b44`  |
| 1958   | No file              | `017505f66b44`  |
| 1950   | No file              | `017505f66b44`  |
| 1945   | No file              | `017505f66b44`  |
| 1937   | No file              | `017505f66b44`  |
| 1933   | No file              | `017505f66b44`  |
| 1927   | No file              | `017505f66b44`  |
| 1921   | No file              | `017505f66b44`  |
| 1914   | No file              | `017505f66b44`  |
| 1908   | No file              | `017505f66b44`  |
| 1897   | No file              | `017505f66b44`  |
| 1892   | No file              | `017505f66b44`  |
| 1886   | No file              | `017505f66b44`  |
| 1881   | No file              | `017505f66b44`  |
| 1871   | No file              | `017505f66b44`  |
| 1866   | No file              | `017505f66b44`  |
| 1862   | No file              | `017505f66b44`  |
| 1854   | No file              | `017505f66b44`  |
| 1846   | No file              | `017505f66b44`  |
| 1838   | No file              | `017505f66b44`  |
| 1832   | No file              | `017505f66b44`  |
| 1826   | No file              | `017505f66b44`  |
| 1822   | No file              | `017505f66b44`  |
| 1818   | No file              | `017505f66b44`  |
| 1804   | No file              | `017505f66b44`  |
| 1794   | No file              | `017505f66b44`  |
| 1790   | No file              | `017505f66b44`  |
| 1784   | No file              | `017505f66b44`  |
| 1774   | No file              | `017505f66b44`  |
| 1771   | No file              | `017505f66b44`  |
| 1762   | No file              | `017505f66b44`  |
| 1759   | No file              | `017505f66b44`  |
| 1754   | No file              | `017505f66b44`  |
| 1749   | No file              | `017505f66b44`  |
| 1743   | No file              | `017505f66b44`  |
| 1737   | No file              | `017505f66b44`  |
| 1731   | No file              | `017505f66b44`  |
| 1725   | No file              | `017505f66b44`  |
| 1717   | No file              | `017505f66b44`  |
| 1710   | No file              | `017505f66b44`  |
| 1704   | No file              | `017505f66b44`  |
| 1698   | No file              | `017505f66b44`  |
| 1690   | No file              | `017505f66b44`  |
| 1685   | No file              | `017505f66b44`  |
| 1680   | No file              | `017505f66b44`  |
| 1674   | No file              | `017505f66b44`  |
| 1668   | No file              | `017505f66b44`  |
| 1659   | No file              | `017505f66b44`  |
| 1649   | No file              | `017505f66b44`  |
| 1642   | No file              | `017505f66b44`  |
| 1636   | No file              | `017505f66b44`  |
| 1628   | No file              | `017505f66b44`  |
| 1622   | No file              | `017505f66b44`  |
| 1614   | No file              | `017505f66b44`  |
| 1608   | No file              | `017505f66b44`  |
| 1602   | No file              | `017505f66b44`  |
| 1598   | No file              | `017505f66b44`  |
| 1594   | No file              | `017505f66b44`  |
| 1590   | No file              | `017505f66b44`  |
| 1587   | No file              | `017505f66b44`  |
| 1584   | No file              | `017505f66b44`  |
| 1579   | No file              | `017505f66b44`  |
| 1572   | No file              | `017505f66b44`  |
| 1565   | No file              | `017505f66b44`  |
| 1559   | No file              | `017505f66b44`  |
| 1554   | No file              | `017505f66b44`  |
| 1547   | No file              | `017505f66b44`  |
| 1537   | No file              | `017505f66b44`  |
| 1529   | No file              | `017505f66b44`  |
| 1524   | No file              | `017505f66b44`  |
| 1519   | No file              | `017505f66b44`  |
| 1509   | No file              | `017505f66b44`  |
| 1506   | No file              | `017505f66b44`  |
| 1504   | No file              | `017505f66b44`  |
| 1500   | No file              | `017505f66b44`  |
| 1493   | No file              | `017505f66b44`  |
| 1489   | No file              | `017505f66b44`  |
| 1485   | No file              | `017505f66b44`  |
| 1481   | No file              | `017505f66b44`  |
| 1474   | No file              | `017505f66b44`  |
| 1466   | No file              | `017505f66b44`  |
| 1462   | No file              | `017505f66b44`  |
| 1459   | No file              | `017505f66b44`  |
| 1453   | No file              | `017505f66b44`  |
| 1450   | No file              | `017505f66b44`  |
| 1445   | No file              | `017505f66b44`  |
| 1439   | No file              | `017505f66b44`  |
| 1433   | No file              | `017505f66b44`  |
| 1430   | No file              | `017505f66b44`  |
| 1426   | No file              | `017505f66b44`  |
| 1421   | No file              | `017505f66b44`  |
| 1417   | No file              | `017505f66b44`  |
| 1416   | No file              | `017505f66b44`  |
| 1409   | No file              | `017505f66b44`  |
| 1405   | No file              | `017505f66b44`  |
| 1401   | No file              | `017505f66b44`  |
| 1396   | No file              | `017505f66b44`  |
| 1391   | No file              | `017505f66b44`  |
| 1390   | No file              | `017505f66b44`  |
| 1386   | No file              | `017505f66b44`  |
| 1381   | No file              | `017505f66b44`  |
| 1379   | No file              | `017505f66b44`  |
| 1372   | No file              | `017505f66b44`  |
| 1366   | No file              | `017505f66b44`  |
| 1364   | No file              | `017505f66b44`  |
| 1363   | No file              | `017505f66b44`  |
| 1360   | No file              | `017505f66b44`  |
| 1358   | No file              | `017505f66b44`  |
| 1355   | No file              | `017505f66b44`  |
| 1351   | No file              | `017505f66b44`  |
| 1348   | No file              | `017505f66b44`  |
| 1346   | No file              | `017505f66b44`  |
| 1341   | No file              | `017505f66b44`  |
| 1340   | No file              | `017505f66b44`  |
| 1338   | No file              | `017505f66b44`  |
| 1335   | No file              | `017505f66b44`  |
| 1333   | No file              | `017505f66b44`  |
| 1329   | No file              | `017505f66b44`  |
| 1327   | No file              | `017505f66b44`  |
| 1324   | No file              | `017505f66b44`  |
| 1321   | No file              | `017505f66b44`  |
| 1319   | No file              | `017505f66b44`  |
| 1318   | No file              | `017505f66b44`  |
| 1316   | No file              | `017505f66b44`  |
| 1313   | No file              | `017505f66b44`  |
| 1311   | No file              | `017505f66b44`  |
| 1309   | No file              | `017505f66b44`  |
| 1304   | No file              | `017505f66b44`  |
| 1292   | No file              | `017505f66b44`  |
| 1286   | No file              | `017505f66b44`  |
| 1280   | No file              | `017505f66b44`  |
| 1276   | No file              | `017505f66b44`  |
| 1267   | No file              | `017505f66b44`  |
| 1261   | No file              | `017505f66b44`  |
| 1256   | No file              | `017505f66b44`  |
| 1250   | No file              | `017505f66b44`  |
| 1246   | No file              | `017505f66b44`  |
| 1239   | No file              | `017505f66b44`  |
| 1230   | No file              | `017505f66b44`  |
| 1226   | No file              | `017505f66b44`  |
| 1220   | No file              | `017505f66b44`  |
| 1217   | No file              | `017505f66b44`  |
| 1211   | No file              | `017505f66b44`  |
| 1210   | No file              | `017505f66b44`  |
| 1208   | No file              | `017505f66b44`  |
| 1203   | No file              | `017505f66b44`  |
| 1197   | No file              | `017505f66b44`  |
| 1194   | No file              | `017505f66b44`  |
| 1192   | No file              | `017505f66b44`  |
| 1187   | No file              | `017505f66b44`  |
| 1183   | No file              | `017505f66b44`  |
| 1177   | No file              | `017505f66b44`  |
| 1173   | No file              | `017505f66b44`  |
| 1167   | No file              | `017505f66b44`  |
| 1164   | No file              | `017505f66b44`  |
| 1156   | No file              | `017505f66b44`  |
| 1149   | No file              | `017505f66b44`  |
| 1144   | No file              | `017505f66b44`  |
| 1137   | No file              | `017505f66b44`  |
| 1132   | No file              | `017505f66b44`  |
| 1127   | No file              | `017505f66b44`  |
| 1122   | No file              | `017505f66b44`  |
| 1118   | No file              | `017505f66b44`  |
| 1114   | No file              | `017505f66b44`  |
| 1109   | No file              | `017505f66b44`  |
| 1102   | No file              | `017505f66b44`  |
| 1096   | No file              | `017505f66b44`  |
| 1088   | No file              | `017505f66b44`  |
| 1081   | No file              | `017505f66b44`  |
| 1076   | No file              | `017505f66b44`  |
| 1069   | No file              | `017505f66b44`  |
| 1064   | No file              | `017505f66b44`  |
| 1058   | No file              | `017505f66b44`  |
| 1051   | No file              | `017505f66b44`  |
| 1044   | No file              | `017505f66b44`  |
| 1036   | No file              | `017505f66b44`  |
| 1026   | No file              | `017505f66b44`  |
| 1016   | No file              | `017505f66b44`  |
| 1009   | No file              | `017505f66b44`  |
| 1005   | No file              | `017505f66b44`  |
| 1000   | No file              | `017505f66b44`  |
| 998    | No file              | `017505f66b44`  |
| 990    | No file              | `017505f66b44`  |
| 979    | No file              | `017505f66b44`  |
| 972    | No file              | `017505f66b44`  |
| 963    | No file              | `017505f66b44`  |
| 955    | No file              | `017505f66b44`  |
| 946    | No file              | `017505f66b44`  |
| 938    | No file              | `017505f66b44`  |
| 927    | No file              | `017505f66b44`  |
| 911    | No file              | `017505f66b44`  |
| 904    | No file              | `017505f66b44`  |
| 899    | No file              | `017505f66b44`  |
| 894    | No file              | `017505f66b44`  |
| 885    | No file              | `017505f66b44`  |
| 879    | No file              | `017505f66b44`  |
| 872    | No file              | `017505f66b44`  |
| 864    | No file              | `017505f66b44`  |
| 855    | No file              | `017505f66b44`  |
| 853    | No file              | `017505f66b44`  |
| 845    | No file              | `017505f66b44`  |
| 837    | No file              | `017505f66b44`  |
| 829    | No file              | `017505f66b44`  |
| 822    | No file              | `017505f66b44`  |
| 814    | No file              | `017505f66b44`  |
| 805    | No file              | `017505f66b44`  |
| 794    | No file              | `017505f66b44`  |
| 787    | No file              | `017505f66b44`  |
| 780    | No file              | `017505f66b44`  |
| 771    | No file              | `017505f66b44`  |
| 760    | No file              | `017505f66b44`  |
| 748    | No file              | `017505f66b44`  |
| 741    | No file              | `017505f66b44`  |
| 736    | No file              | `017505f66b44`  |
| 731    | No file              | `017505f66b44`  |
| 723    | No file              | `017505f66b44`  |
| 711    | No file              | `017505f66b44`  |
| 707    | No file              | `017505f66b44`  |
| 697    | No file              | `017505f66b44`  |
| 689    | No file              | `017505f66b44`  |
| 683    | No file              | `017505f66b44`  |
| 678    | No file              | `017505f66b44`  |
| 670    | No file              | `017505f66b44`  |
| 661    | No file              | `017505f66b44`  |
| 656    | No file              | `017505f66b44`  |
| 652    | No file              | `017505f66b44`  |
| 643    | No file              | `017505f66b44`  |
| 637    | No file              | `017505f66b44`  |
| 630    | No file              | `017505f66b44`  |
| 627    | No file              | `017505f66b44`  |
| 621    | No file              | `017505f66b44`  |
| 617    | No file              | `017505f66b44`  |
| 615    | No file              | `017505f66b44`  |
| 606    | No file              | `017505f66b44`  |
| 599    | No file              | `017505f66b44`  |
| 592    | No file              | `017505f66b44`  |
| 586    | No file              | `017505f66b44`  |
| 577    | No file              | `017505f66b44`  |
| 569    | No file              | `017505f66b44`  |
| 561    | No file              | `017505f66b44`  |
| 554    | No file              | `017505f66b44`  |
| 542    | No file              | `017505f66b44`  |
| 532    | No file              | `017505f66b44`  |
| 531    | No file              | `017505f66b44`  |
| 526    | No file              | `017505f66b44`  |
| 521    | No file              | `017505f66b44`  |
| 517    | No file              | `017505f66b44`  |
| 510    | No file              | `017505f66b44`  |
| 508    | No file              | `017505f66b44`  |
| 504    | No file              | `017505f66b44`  |
| 497    | No file              | `017505f66b44`  |
| 491    | No file              | `017505f66b44`  |
| 485    | No file              | `017505f66b44`  |
| 478    | No file              | `017505f66b44`  |
| 472    | No file              | `017505f66b44`  |
| 466    | No file              | `017505f66b44`  |
| 457    | No file              | `017505f66b44`  |
| 452    | No file              | `017505f66b44`  |
| 449    | No file              | `017505f66b44`  |
| 435    | No file              | `017505f66b44`  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                                                     |
| ------------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `itemenchantbackendoffset.dbss` | Required | Maps the packed key to a block offset and size                                           |
| `languagedata_en.loc`           | Optional | Item name for the item ID (`str_type=0`)                                                 |
| `jewelgroupstaticstatus.bss`    | Optional | Crystal group name and preset limit for `crystal_group`; without it the column shows the number |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes |
| ------- | ------------ | ------ | ----- |
| `+0x00` | u32          | count  | Block count, matching the companion |
| `+0x04` | Block[count] | blocks | Contiguous, in the order of the companion rows; the last block ends at the end of the file |

### Block (variable: 316 bytes + lists and strings, size from `itemenchantbackendoffset.dbss`)

The offsets in `itemenchant.dbss` are Message Tail `+0x2B` for `unknown_00`
and `+0x5A` for `item_access_level`. Six counted lists move the fields after
them; the hex in an `unknown_<hex>` name after a list is the offset in a
block whose lists are empty. On client 3483 every one of the 169,345 blocks
walks to its last byte by this table, and the key it ends with is the key of
its offset row.

The value counts are over the 70,826 base blocks of client 3483. "Client
1784" is `unknown_old_*` or the named field of Layout 1 in
[`itemenchant_dbss.md`](itemenchant_dbss.md), compared on the 41,408 base
items both clients have; the `Item_Table` column of each is in Field Names.

| Offset                      | Type                                       | Field                              | Notes |
| --------------------------- | ------------------------------------------ | ---------------------------------- | ----- |
| `+0x00`                     | u8[46]                                     | unknown_00                         | A list of up to three numbers, the rest filled with `0x77` (119); set in 3,770 base blocks, such as `11, 12, 13` on chest armour and `24, 25` on outfits. The numbers are not `__eEquipSlotNo` values. Equals client 1784 `unknown_old_30` (32 entries, filled with 92) on 41,262 shared items |
| `+0x2E`                     | u8                                         | unknown_2e                         | `0` in every base block, as client 1784 `unknown_old_50` |
| `+0x2F`                     | u8                                         | item_access_level                  | 2016 `_itemAccessLevel`, see Field Names in `itemenchant_dbss.md`: `0` (31,713 base items), `1` (21,179), `10` (12,389), `99` (3,204), `20` (2,298), and `15`, `19` and `40` on 41 more. Client 1784 value on 98.2% |
| `+0x30`                     | i32[3]                                     | original_price_rates               | `1000000` in all six rates of 69,637 base blocks. With `price_rates`, client 1784 `unknown_old_93` on every shared item |
| `+0x3C`                     | i32[3]                                     | price_rates                        |       |
| `+0x48`                     | i64                                        | repair_time                        | Set in 9,754 base blocks; client 1784 `unknown_old_b3` on every shared item but one |
| `+0x50`                     | i64[4]                                     | unknown_50                         | Four prices where client 1784 has `unknown_old_bb` (the 2016 `_maxPrice`, `_minPrice`, `_maxestPrice`, `_minestPrice`); the client 1784 value on 86.5% |
| `+0x70`                     | i32                                        | maxest_percent_for_item_market     | `0` in 55,226 base blocks, `150000` in 9,980; client 1784 value on 98.0% |
| `+0x74`                     | i32                                        | minest_percent_for_item_market     | Client 1784 value on 98.8% |
| `+0x78`                     | i64                                        | base_price_for_item_market         | Client 1784 value on 83.2%; prices change between patches |
| `+0x80`                     | u16                                        | max_register_count_for_item_market | `0` (56,725 base items), `1` (12,353), `500` (1,021); client 1784 value on 99.1% |
| `+0x82`                     | i64                                        | unknown_82                         | `0` in 57,341 base blocks, `10` in 9,386, `100` in 1,922, `10000` in 695; no client 1784 field |
| `+0x8A`                     | i64                                        | unknown_8a                         | Set in 1,170 base blocks (`10000` in 723); no client 1784 field |
| `+0x92`                     | i64                                        | unknown_92                         | Half of `unknown_8a` in most blocks that set it (`5000` with `10000`, `3000` with `6000`) |
| `+0x9A`                     | u64                                        | jewel_need_item_count              | `1` in 86 base blocks and `2` in 479 |
| `+0xA2`                     | Jewel Need Item[jewel_need_item_count]     | jewel_need_items                   | Items needed to take the crystal out of its socket, see Jewel Need Item |
| `jewel_need_items+0x00`     | u8                                         | jewel_equip_type                   | `19` in 70,256 base blocks, `0` to `18` in the other 570. Client 1784 value on all 225 shared items it does not store `18` on; client 1784 stores `18` where client 3483 stores `19` |
| `jewel_need_items+0x01`     | u8                                         | jewel_color_type                   | `6` in 70,256 base blocks, `0` to `5` in the other 570; client 1784 value on every shared item |
| `jewel_need_items+0x02`     | i32                                        | jewel_demolition_rate              | Set in 533 base blocks (`1000000`, `900000`, `700000` and lower); client 1784 value on every shared item |
| `jewel_need_items+0x06`     | u8                                         | collect_tool_type                  | `19` in 70,622 base blocks, `1` to `18` on the others. Client 1784 value on all 169 shared items it does not store `15` on |
| `jewel_need_items+0x07`     | i64                                        | collect_time                       | Set in 204 base blocks; client 1784 value on every shared item but seven |
| `jewel_need_items+0x0F`     | i32                                        | unknown_b1                         | `0` in every base block |
| `jewel_need_items+0x13`     | i16                                        | need_contribute                    | `0` in 70,586 base blocks, `50` in 120, `30` in 79; client 1784 value on every shared item |
| `jewel_need_items+0x15`     | u8                                         | unknown_b7                         | `1` in 2,493 base blocks; client 1784 `unknown_old_127` on 99.6% |
| `jewel_need_items+0x16`     | u8                                         | unknown_b8                         | `0` in 151 base blocks, else `1`; client 1784 `unknown_old_12b` on every shared item |
| `jewel_need_items+0x17`     | u8                                         | target_type                        | `1` in 28 base blocks; client 1784 value on every shared item |
| `jewel_need_items+0x18`     | u32                                        | unknown_ba                         | `0` in every base block |
| `jewel_need_items+0x1C`     | i32                                        | unknown_be                         | `0` in every base block |
| `jewel_need_items+0x20`     | u32                                        | popup_result_item_count            | `1` in 12 base blocks and `3` in 34 |
| `jewel_need_items+0x24`     | Popup Result Item[popup_result_item_count] | popup_result_items                 | See Popup Result Item |
| `popup_result_items+0x00`   | bytes[8]                                   | unknown_c6                         | `0` in every base block |
| `popup_result_items+0x08`   | u64                                        | unknown_ce                         | Entry count of `unknown_ce_entries`; set in 1,152 base blocks, `1` in 671 and `10` in 329 |
| `popup_result_items+0x10`   | u32[unknown_ce]                            | unknown_ce_entries                 | Values from `105538` to `125127`; client 1784 `unknown_old_14d` on 99.9% |
| `unknown_ce_entries+0x00`   | u16                                        | unknown_d6                         | Set in 515 base blocks, a few items per value; client 1784 `unknown_old_156` and the byte after it, value on every shared item |
| `unknown_ce_entries+0x02`   | bytes[7]                                   | unknown_d8                         | `0` in every base block |
| `unknown_ce_entries+0x09`   | u8                                         | enchant_difficulty                 | `0` (64,420 base items), `3` (3,633), `2` (2,182), `4` (586), `1` (5). The tooltip's enhancement difficulty line, see Enchant Difficulty. Client 1784 value on every shared item |
| `unknown_ce_entries+0x0A`   | u8                                         | expiration_period_type             | `2` in 70,789 base blocks, `0` in 30 and `1` in 7; client 1784 value on every shared item |
| `unknown_ce_entries+0x0B`   | i32                                        | expiration_period_param1           | `-1` in all 70,789 base blocks with type `2`, `0` to `5` with the others; client 1784 value on every shared item |
| `unknown_ce_entries+0x0F`   | i64                                        | expiration_period_param2           | Client 1784 value on every shared item |
| `unknown_ce_entries+0x17`   | i32                                        | connect_ui                         | The window the item opens when used, an `eConnectUiType` value; `-1` (`eConnectUi_Undefined`) in 68,785 base blocks. See Connect UI. Client 1784 value on every shared item |
| `unknown_ce_entries+0x1B`   | u8                                         | market_filter_1                    | `0` in 62,005 base blocks, else `1` to `31`; client 1784 value on 99.6% |
| `unknown_ce_entries+0x1C`   | u8                                         | market_filter_2                    | `1` in 604 base blocks, `4` in 19; client 1784 value on every shared item |
| `unknown_ce_entries+0x1D`   | i32                                        | unknown_f3                         | `1` in every base block |
| `unknown_ce_entries+0x21`   | u8                                         | item_properties                    | Set in 195 base blocks (`153` to `155` in 56 each); client 1784 value on all 139 shared items that set it |
| `unknown_ce_entries+0x22`   | u8                                         | unknown_f8                         | `0` in every base block |
| `unknown_ce_entries+0x23`   | u32                                        | unknown_f9                         | Entry count of `unknown_f9_entries`: `1` (60,559 base items) to `8` |
| `unknown_ce_entries+0x27`   | u32[unknown_f9]                            | unknown_f9_entries                 | 32-bit values with no pattern; `0x6016CFF7` is the first entry in 36,895 base blocks. Client 1784 `unknown_old_43a` on 96.8% |
| `unknown_f9_entries+0x00`   | u32                                        | unknown_fd                         | `9` in 70,026 base blocks, else `0` to `7`; client 1784 `unknown_old_44d` first u32 on every shared item |
| `unknown_f9_entries+0x04`   | u32                                        | unknown_101                        | `0` in 70,026 base blocks, `100` in 795, `500` in 5; client 1784 `unknown_old_44d` second u32 on every shared item but five |
| `unknown_f9_entries+0x08`   | i32                                        | unknown_105                        | `0` in every base block but one |
| `unknown_f9_entries+0x0C`   | u16                                        | fairy_feed_key                     | `1` in 2,761 base blocks, `2` in 323, `3` to `7` in 6; client 1784 `unknown_old_465` on 99.8% |
| `unknown_f9_entries+0x0E`   | str16                                      | use_condition                      | A condition script such as `!checkcompetition()` (970 base items) or `getlevel()>55;`; empty in 42,884. Client 1784 `unknown_condition` |
| `use_condition+0x00`        | str8                                       | acquire_action                     | `ITEM_BIC_HIT_1` to `ITEM_BIC_HIT_4` (9,330 base items) and `ITEM_BIC_HIT_6` (1); the `second_string` of the `itemenchant.dbss` parser |
| `acquire_action+0x00`       | str16                                      | description_kr                     | Korean item description; empty in 7,851 base blocks |
| `description_kr+0x00`       | u32                                        | unknown_tail_count                 | Entry count of `unknown_tail`, set in 20,531 base blocks |
| `description_kr+0x04`       | u32[unknown_tail_count]                    | unknown_tail                       | Values such as `112298` and `21040`; client 1784 `unknown_tail_entries`. Black Stone (Weapon) ends its 8 entries with the 2 of client 1784 |
| `unknown_tail+0x00`         | u8                                         | restore_type                       | `1` in 5,935 base blocks; client 1784 Tail `unknown_11` on 97.1% |
| `unknown_tail+0x01`         | u32                                        | unknown_end_count                  | Entry count of `unknown_end`: `1` in 1,110 base blocks, `2` in 31, `3` in 48 |
| `unknown_tail+0x05`         | u16[unknown_end_count]                     | unknown_end                        | Client 1784 `unknown_end_entries` on 99.6% |
| `unknown_end+0x00`          | bytes[10]                                  | unknown_after_unknown_end          | Only the third byte is set: `3` (30,095 base blocks), `100` (9,863), `1`, `50`; no client 1784 field holds it |
| `unknown_end+0x0A`          | u32                                        | key                                | The packed key of the offset row, `enchant_level << 24 \| item_id`, in every block (client 3483); `key_dup` in `itemenchant.dbss` |
| `unknown_end+0x0E`          | u16                                        | crystal_group                      | The crystal's [jewelgroupstaticstatus.bss](../bss/jewelgroupstaticstatus_bss.md) group; `0xFFFF` on everything else and on every higher level |

### Jewel Need Item (16 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u32  | item_id    | The 479 crystals with two entries all list `16000` and `17000` |
| `+0x04` | u32  | unknown_04 | `0` in all 1,044 entries of the base blocks |
| `+0x08` | i64  | count      | `1` in 1,042 of the 1,044 entries of the base blocks, `100` in 2 |

### Popup Result Item (12 bytes)

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | i64  | count   | `1000000` in the 12 base blocks with one entry; the 34 with three entries hold `0` in all of them |
| `+0x08` | u32  | item_id | `1` in the 12 base blocks with one entry |

### `itemenchantbackendoffset.dbss`

The layout of `itemenchantoffset.dbss`, with the same keys in the same
order (169,345 rows on client 3483).

| Offset              | Type              | Field        | Notes |
| ------------------- | ----------------- | ------------ | ----- |
| `+0x00`             | char[4]           | magic        | `PABR` (ASCII) |
| `+0x04`             | u32               | count        | Number of rows |
| `+0x08`             | Offset Row[count] | rows         | `count` × 12-byte rows |
| `rows+0x00`         | String Table      | string_table | The PABR string table, here with no strings |
| `string_table+0x00` | u32               | end_of_rows  | Equals `8 + count × 12` |
| `string_table+0x04` | u32               | zero         | Always zero |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes |
| ------- | ---- | ----------- | ----- |
| `+0x00` | u32  | key         | Packed item ID and enchant level, see Key Packing in `itemenchant_dbss.md` |
| `+0x04` | u32  | data_offset | Byte offset of the block in `itemenchantbackend.dbss` |
| `+0x08` | u32  | data_size   | Block length in bytes |

Rows are contiguous: `data_offset + data_size` of one row equals the next
row's `data_offset`. For every key, `data_size` is the `itemenchant.dbss`
block size less the `itemenchantbackendtest.dbss` block size (client 3483).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` in observed data |
| `+0x04` | pstr[string_count] | strings      | PABR string-table entries |

## Connect UI

`connect_ui` decides what using the item from the inventory opens. The PC
inventory's right-click handler (`PaGlobalFunc_Inventory_All_SlotRClickXXX`
in [`panel_window_inventory_all_4.luac`](../lua/panel_window_inventory_all_4_luac.md))
reads `itemEnchantWrapper:getConnectUi()` and, when it is not
`eConnectUiType.eConnectUi_Undefined`, calls `ConnectUI(type, itemKey)` from
`connectui.luac`, or `ConnectLetterUI` for `eConnectUi_Letter`. The enum in
`connectui.luac` gives the numbers, and three items fit them: Black Stone
(Weapon) stores `0` (`eConnectUi_BlackStone`, the Black Spirit's
enhancement window), Caphras Stone `28` (`eConnectUi_Caphras`) and Ancient
Spirit's Crystal - Viper `1` (`eConnectUi_Socket`, the crystal preset
window). The eight most common values on client 3483:

| Value | `eConnectUiType`        | Base items |
| ----: | ----------------------- | ---------: |
| -1    | `eConnectUi_Undefined`  | 68,785     |
| 4     | `eConnectUi_DyePalette` | 1,129      |
| 1     | `eConnectUi_Socket`     | 471        |
| 3     | `eConnectUi_Improve`    | 119        |
| 0     | `eConnectUi_BlackStone` | 84         |
| 29    | `eConnectUi_LightStone` | 84         |
| 27    | `eConnectUi_Letter`     | 53         |
| 38    | `eConnectUi_ItemSkillOption` | 22    |

## Enchant Difficulty

The item tooltip (`Panel_Tooltip_Item_ShowInfo` in
[`panel_tooltip_item.luac`](../lua/panel_tooltip_item_luac.md)) reads
`itemSSW:get():getEnchantDifficulty()` and shows a difficulty line when the
value is above `__eEnchantDifficulty_None`: Easy, Normal, or Hard for both
`__eEnchantDifficulty_Hard` and `__eEnchantDifficulty_NotExtractHard`. The
Lua does not give the numbers of these constants (an Open Question of the
script doc), so the Block table gives the stored values only. Kzarka
Gauntlet stores `3`.

## Notes

- The doc check walks every block of client 3483 to its last byte by Layout
  1. The `itemenchant.dbss` blocks hold these bytes after Message Tail
  `+0x2A`, so the fields above are also the `unknown_2b`, `item_access_level`
  and `unknown_after_message_tail` of that doc.
- Clients 1964 to 3402 store the blocks in an older layout that is not
  documented here. On client 3402 the Black Stone (Weapon) block is 19
  bytes longer than on client 3412: 2 more bytes before
  `item_access_level`, and the rest spread over the zero runs between
  `jewel_need_items` and `acquire_action`.
- The order follows the client 1784 record of `itemenchant.dbss` (Layout 1
  there) from `item_access_level` on, without the fields client 3483 keeps in
  the `itemenchant.dbss` header, Icon Tail or Message Tail, such as the
  prices, `contents_event_type`, the skill keys and the Tail fields. Client
  1784 has no field for `unknown_82`, `unknown_8a`, `unknown_92` and
  `unknown_after_unknown_end`.
- The lists that hold item IDs match their `Item_Table` columns of the
  private server's `DataSheets.bexcel` on client 1784: `jewel_need_items`
  lists the items of `JewelSubtractionNeedItem` with the count of
  `JewelSubtractionNeedItemCount` on all 279 items the sheet and client 3483
  share that set it, and `popup_result_items` holds the `item:count` pairs of
  `PopupResultItem` (`1:1000000`) on all 12.
- Why the client data stores these blocks a second time, split from their
  front part, is the Which File the Client Reads question of
  `itemenchantbackendtest_dbss.md`.

## Field Names

Each name is the `Item_Table` column of the private server's
`DataSheets.bexcel` on client 1784 that the field holds, taken from the
client 1784 field at the same place: its column in Layout 1 of
`itemenchant_dbss.md`, or the row field the 1784 server dump's record
reader (`0x140b57130`) reads it into. The client 3483 value matches the
client 1784 value on the share the Block table gives, so the names rest on
the live file as well as on the private server's. The lists and strings
were matched with the sheet directly (Notes).

| Field | `Item_Table` column | Other evidence |
| ----- | ------------------- | -------------- |
| original_price_rates | `OriginalPriceRate_0` to `_2` | |
| price_rates | `PriceRate_0` to `_2` | |
| repair_time | `RepairTime` | read as a time |
| maxest_percent_for_item_market | `maxestPercentForItemMarket` | |
| minest_percent_for_item_market | `minestPercentForItemMarket` | |
| base_price_for_item_market | `basePriceForItemMarket` | |
| max_register_count_for_item_market | `maxRegisterCountForItemMarket` | |
| jewel_need_items | `JewelSubtractionNeedItem`, `JewelSubtractionNeedItemCount` | 2016 `_needItemListToPopJewel` at this place |
| jewel_equip_type | `JewelEquipType` | |
| jewel_color_type | `JewelColorType` | |
| jewel_demolition_rate | `JewelDemolitionRate` | |
| collect_tool_type | `CollectToolType` | |
| collect_time | `CollectTime` | |
| need_contribute | `NeedContribute` | |
| target_type | `TargetType` | |
| popup_result_items | `PopupResultItem` | |
| enchant_difficulty | `EnchantDifficulty` | `getEnchantDifficulty()`, see Enchant Difficulty |
| expiration_period_type | `ExpirationPeriod Type` | |
| expiration_period_param1 | `ExpirationPeriod Param1` | |
| expiration_period_param2 | `ExpirationPeriod Param2` | |
| connect_ui | `ConnectUi` | `getConnectUi()`, see Connect UI |
| market_filter_1 | `MarketFilter1` | |
| market_filter_2 | `MarketFilter2` | |
| item_properties | `ItemProperties` | |
| fairy_feed_key | `FairyFeedKey` | |
| use_condition | `UseCondition` | 2016 `_useConditionString` at this place |
| acquire_action | `AcquireAction` | the sheet text on 3,237 of the 4,431 shared items that set it |
| description_kr | `Description` | Korean text |
| restore_type | `RestoreType` | |

The 1784 server reads `unknown_d6`, `unknown_b7`, `unknown_b8`,
`unknown_f3`, `unknown_fd` and `unknown_101` into row fields no
`Item_Table` column fills, and `unknown_ce_entries`, `unknown_f9_entries`,
`unknown_tail` and `unknown_end` into lists no column fills. `unknown_105`
sits where it reads `DropMeshKey`, but only one base block sets it, so one
item is all the match rests on. `unknown_00` equals the sheet's
`OccupiedEquipNo` on 2,517 of the 2,520 shared items that set it and its
`NewOccupiedEquipNo` nearly as often, so it stays unnamed until one of the
two is told apart.

## Open Questions

### The Three Market Values Past the Register Count

`unknown_82`, `unknown_8a` and `unknown_92` have no client 1784 field, and
`unknown_92` is half of `unknown_8a` where both are set. Their place after
the item market fields and the `Item_Table` columns that client 1784 does
not store in this file (`basePriceForWorldMarket`,
`minestPercentForWorldMarket`, `maxestPercentForWorldMarket`,
`TradeCountToUpdate`) suggest the world market, but no column holds their
values.

### The Slot List at the Block Start

`unknown_00` holds runs like `11, 12, 13` and `24, 25`, numbers the
`__eEquipSlotNo` enum gives other slots, and the fill grew from 92 on client
1784 to 119. Which slot numbering it uses (the `NewEquipSlot` sheet of the
private server is a candidate) is open.
