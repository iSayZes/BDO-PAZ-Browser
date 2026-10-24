# `title.dbss` Format

## Purpose

Stores title metadata, the raw Korean title text, raw Korean requirement text,
category, and optional inline PAColor markup for special title names.

`title.dbss` is block-addressed by `titleoffset.dbss`; it is not a flat fixed
record table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes   | Records          | Row bytes                  |
| ------ | -------------- | ------- | ------------------ | ------- | ---------------- | -------------------------- |
| 1      | 1698 and later | 3483    | `title.dbss`       | 870,292 | 3,179 Record     | 200 to 870, 274 on average |
| 1      | 1698 and later | 3483    | `titleoffset.dbss` | 38,152  | 3,179 Offset Row | 12                         |

| Layout | File               | Known             | Unknown           |
| ------ | ------------------ | ----------------- | ----------------- |
| 1      | `title.dbss`       | 704,984 B (81.0%) | 165,308 B (19.0%) |
| 1      | `titleoffset.dbss` | 38,152 B (100.0%) | 0 B (0.0%)        |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `686f627a8e93`  |
| 3482   | Layout 1             | `686f627a8e93`  |
| 3474   | Layout 1             | `686f627a8e93`  |
| 3473   | Layout 1             | `686f627a8e93`  |
| 3464   | Layout 1             | `686f627a8e93`  |
| 3458   | Layout 1             | `686f627a8e93`  |
| 3454   | Layout 1             | `686f627a8e93`  |
| 3444   | Layout 1             | `686f627a8e93`  |
| 3435   | Layout 1             | `686f627a8e93`  |
| 3426   | Layout 1             | `686f627a8e93`  |
| 3418   | Layout 1             | `686f627a8e93`  |
| 3412   | Layout 1             | `686f627a8e93`  |
| 3402   | Layout 1             | `686f627a8e93`  |
| 3396   | Layout 1             | `686f627a8e93`  |
| 3387   | Layout 1             | `686f627a8e93`  |
| 3381   | Layout 1             | `686f627a8e93`  |
| 3373   | Layout 1             | `686f627a8e93`  |
| 3364   | Layout 1             | `686f627a8e93`  |
| 3356   | Layout 1             | `686f627a8e93`  |
| 3349   | Layout 1             | `686f627a8e93`  |
| 3342   | Layout 1             | `686f627a8e93`  |
| 3335   | Layout 1             | `686f627a8e93`  |
| 3326   | Layout 1             | `686f627a8e93`  |
| 3321   | Layout 1             | `686f627a8e93`  |
| 3314   | Layout 1             | `686f627a8e93`  |
| 3303   | Layout 1             | `686f627a8e93`  |
| 3302   | Layout 1             | `686f627a8e93`  |
| 3293   | Layout 1             | `686f627a8e93`  |
| 3283   | Layout 1             | `686f627a8e93`  |
| 3275   | Layout 1             | `686f627a8e93`  |
| 3267   | Layout 1             | `686f627a8e93`  |
| 3258   | Layout 1             | `686f627a8e93`  |
| 3251   | Layout 1             | `686f627a8e93`  |
| 3242   | Layout 1             | `686f627a8e93`  |
| 3235   | Layout 1             | `686f627a8e93`  |
| 3229   | Layout 1             | `686f627a8e93`  |
| 3212   | Layout 1             | `686f627a8e93`  |
| 3203   | Layout 1             | `686f627a8e93`  |
| 3193   | Layout 1             | `686f627a8e93`  |
| 3186   | Layout 1             | `686f627a8e93`  |
| 3177   | Layout 1             | `686f627a8e93`  |
| 3169   | Layout 1             | `686f627a8e93`  |
| 3158   | Layout 1             | `686f627a8e93`  |
| 3151   | Layout 1             | `686f627a8e93`  |
| 3144   | Layout 1             | `686f627a8e93`  |
| 3133   | Layout 1             | `686f627a8e93`  |
| 3125   | Layout 1             | `686f627a8e93`  |
| 3118   | Layout 1             | `686f627a8e93`  |
| 3111   | Layout 1             | `686f627a8e93`  |
| 3103   | Layout 1             | `686f627a8e93`  |
| 3095   | Layout 1             | `686f627a8e93`  |
| 3086   | Layout 1             | `686f627a8e93`  |
| 3072   | Layout 1             | `686f627a8e93`  |
| 3062   | Layout 1             | `686f627a8e93`  |
| 3052   | Layout 1             | `686f627a8e93`  |
| 3045   | Layout 1             | `686f627a8e93`  |
| 3037   | Layout 1             | `686f627a8e93`  |
| 3030   | Layout 1             | `686f627a8e93`  |
| 3021   | Layout 1             | `686f627a8e93`  |
| 3012   | Layout 1             | `686f627a8e93`  |
| 3002   | Layout 1             | `686f627a8e93`  |
| 2995   | Layout 1             | `686f627a8e93`  |
| 2987   | Layout 1             | `686f627a8e93`  |
| 2978   | Layout 1             | `686f627a8e93`  |
| 2970   | Layout 1             | `686f627a8e93`  |
| 2959   | Layout 1             | `686f627a8e93`  |
| 2951   | Layout 1             | `686f627a8e93`  |
| 2942   | Layout 1             | `686f627a8e93`  |
| 2935   | Layout 1             | `686f627a8e93`  |
| 2932   | Layout 1             | `686f627a8e93`  |
| 2923   | Layout 1             | `686f627a8e93`  |
| 2919   | Layout 1             | `686f627a8e93`  |
| 2907   | Layout 1             | `686f627a8e93`  |
| 2900   | Layout 1             | `686f627a8e93`  |
| 2891   | Layout 1             | `686f627a8e93`  |
| 2882   | Layout 1             | `686f627a8e93`  |
| 2872   | Layout 1             | `686f627a8e93`  |
| 2863   | Layout 1             | `686f627a8e93`  |
| 2855   | Layout 1             | `686f627a8e93`  |
| 2849   | Layout 1             | `686f627a8e93`  |
| 2844   | Layout 1             | `686f627a8e93`  |
| 2834   | Layout 1             | `686f627a8e93`  |
| 2825   | Layout 1             | `686f627a8e93`  |
| 2819   | Layout 1             | `686f627a8e93`  |
| 2811   | Layout 1             | `686f627a8e93`  |
| 2803   | Layout 1             | `686f627a8e93`  |
| 2794   | Layout 1             | `686f627a8e93`  |
| 2783   | Layout 1             | `686f627a8e93`  |
| 2774   | Layout 1             | `686f627a8e93`  |
| 2765   | Layout 1             | `686f627a8e93`  |
| 2756   | Layout 1             | `686f627a8e93`  |
| 2750   | Layout 1             | `686f627a8e93`  |
| 2743   | Layout 1             | `686f627a8e93`  |
| 2736   | Layout 1             | `686f627a8e93`  |
| 2726   | Layout 1             | `686f627a8e93`  |
| 2717   | Layout 1             | `686f627a8e93`  |
| 2709   | Layout 1             | `686f627a8e93`  |
| 2703   | Layout 1             | `686f627a8e93`  |
| 2695   | Layout 1             | `686f627a8e93`  |
| 2684   | Layout 1             | `686f627a8e93`  |
| 2672   | Layout 1             | `686f627a8e93`  |
| 2665   | Layout 1             | `686f627a8e93`  |
| 2657   | Layout 1             | `686f627a8e93`  |
| 2649   | Layout 1             | `686f627a8e93`  |
| 2644   | Layout 1             | `686f627a8e93`  |
| 2637   | Layout 1             | `686f627a8e93`  |
| 2629   | Layout 1             | `686f627a8e93`  |
| 2619   | Layout 1             | `686f627a8e93`  |
| 2612   | Layout 1             | `686f627a8e93`  |
| 2606   | Layout 1             | `686f627a8e93`  |
| 2602   | Layout 1             | `686f627a8e93`  |
| 2601   | Layout 1             | `686f627a8e93`  |
| 2592   | Layout 1             | `686f627a8e93`  |
| 2583   | Layout 1             | `686f627a8e93`  |
| 2575   | Layout 1             | `686f627a8e93`  |
| 2567   | Layout 1             | `686f627a8e93`  |
| 2560   | Layout 1             | `686f627a8e93`  |
| 2553   | Layout 1             | `686f627a8e93`  |
| 2545   | Layout 1             | `686f627a8e93`  |
| 2538   | Layout 1             | `686f627a8e93`  |
| 2529   | Layout 1             | `686f627a8e93`  |
| 2519   | Layout 1             | `686f627a8e93`  |
| 2513   | Layout 1             | `686f627a8e93`  |
| 2510   | Layout 1             | `686f627a8e93`  |
| 2507   | Layout 1             | `686f627a8e93`  |
| 2503   | Layout 1             | `686f627a8e93`  |
| 2498   | Layout 1             | `686f627a8e93`  |
| 2492   | Layout 1             | `686f627a8e93`  |
| 2487   | Layout 1             | `686f627a8e93`  |
| 2480   | Layout 1             | `686f627a8e93`  |
| 2474   | Layout 1             | `686f627a8e93`  |
| 2468   | Layout 1             | `686f627a8e93`  |
| 2460   | Layout 1             | `686f627a8e93`  |
| 2453   | Layout 1             | `686f627a8e93`  |
| 2444   | Layout 1             | `686f627a8e93`  |
| 2438   | Layout 1             | `686f627a8e93`  |
| 2434   | Layout 1             | `686f627a8e93`  |
| 2429   | Layout 1             | `686f627a8e93`  |
| 2421   | Layout 1             | `686f627a8e93`  |
| 2414   | Layout 1             | `686f627a8e93`  |
| 2407   | Layout 1             | `686f627a8e93`  |
| 2401   | Layout 1             | `686f627a8e93`  |
| 2397   | Layout 1             | `686f627a8e93`  |
| 2393   | Layout 1             | `686f627a8e93`  |
| 2384   | Layout 1             | `686f627a8e93`  |
| 2378   | Layout 1             | `686f627a8e93`  |
| 2372   | Layout 1             | `686f627a8e93`  |
| 2358   | Layout 1             | `686f627a8e93`  |
| 2352   | Layout 1             | `686f627a8e93`  |
| 2347   | Layout 1             | `686f627a8e93`  |
| 2343   | Layout 1             | `686f627a8e93`  |
| 2335   | Layout 1             | `686f627a8e93`  |
| 2327   | Layout 1             | `686f627a8e93`  |
| 2324   | Layout 1             | `686f627a8e93`  |
| 2319   | Layout 1             | `686f627a8e93`  |
| 2313   | Layout 1             | `686f627a8e93`  |
| 2308   | Layout 1             | `686f627a8e93`  |
| 2302   | Layout 1             | `686f627a8e93`  |
| 2295   | Layout 1             | `686f627a8e93`  |
| 2290   | Layout 1             | `686f627a8e93`  |
| 2284   | Layout 1             | `686f627a8e93`  |
| 2276   | Layout 1             | `686f627a8e93`  |
| 2269   | Layout 1             | `686f627a8e93`  |
| 2259   | Layout 1             | `686f627a8e93`  |
| 2250   | Layout 1             | `686f627a8e93`  |
| 2243   | Layout 1             | `686f627a8e93`  |
| 2235   | Layout 1             | `686f627a8e93`  |
| 2229   | Layout 1             | `686f627a8e93`  |
| 2224   | Layout 1             | `686f627a8e93`  |
| 2218   | Layout 1             | `686f627a8e93`  |
| 2215   | Layout 1             | `686f627a8e93`  |
| 2207   | Layout 1             | `686f627a8e93`  |
| 2203   | Layout 1             | `686f627a8e93`  |
| 2196   | Layout 1             | `686f627a8e93`  |
| 2192   | Layout 1             | `686f627a8e93`  |
| 2189   | Layout 1             | `686f627a8e93`  |
| 2183   | Layout 1             | `686f627a8e93`  |
| 2179   | Layout 1             | `686f627a8e93`  |
| 2171   | Layout 1             | `686f627a8e93`  |
| 2163   | Layout 1             | `686f627a8e93`  |
| 2156   | Layout 1             | `686f627a8e93`  |
| 2151   | Layout 1             | `686f627a8e93`  |
| 2147   | Layout 1             | `686f627a8e93`  |
| 2142   | Layout 1             | `686f627a8e93`  |
| 2138   | Layout 1             | `686f627a8e93`  |
| 2134   | Layout 1             | `686f627a8e93`  |
| 2130   | Layout 1             | `686f627a8e93`  |
| 2122   | Layout 1             | `686f627a8e93`  |
| 2107   | Layout 1             | `686f627a8e93`  |
| 2098   | Layout 1             | `686f627a8e93`  |
| 2089   | Layout 1             | `686f627a8e93`  |
| 2081   | Layout 1             | `686f627a8e93`  |
| 2073   | Layout 1             | `686f627a8e93`  |
| 2067   | Layout 1             | `686f627a8e93`  |
| 2063   | Layout 1             | `686f627a8e93`  |
| 2059   | Layout 1             | `686f627a8e93`  |
| 2052   | Layout 1             | `686f627a8e93`  |
| 2044   | Layout 1             | `686f627a8e93`  |
| 2039   | Layout 1             | `686f627a8e93`  |
| 2032   | Layout 1             | `686f627a8e93`  |
| 2025   | Layout 1             | `686f627a8e93`  |
| 2011   | Layout 1             | `686f627a8e93`  |
| 2005   | Layout 1             | `686f627a8e93`  |
| 2000   | Layout 1             | `686f627a8e93`  |
| 1996   | Layout 1             | `686f627a8e93`  |
| 1991   | Layout 1             | `686f627a8e93`  |
| 1985   | Layout 1             | `686f627a8e93`  |
| 1980   | Layout 1             | `686f627a8e93`  |
| 1969   | Layout 1             | `686f627a8e93`  |
| 1964   | Layout 1             | `686f627a8e93`  |
| 1958   | Layout 1             | `686f627a8e93`  |
| 1950   | Layout 1             | `686f627a8e93`  |
| 1945   | Layout 1             | `686f627a8e93`  |
| 1937   | Layout 1             | `686f627a8e93`  |
| 1933   | Layout 1             | `686f627a8e93`  |
| 1927   | Layout 1             | `686f627a8e93`  |
| 1921   | Layout 1             | `686f627a8e93`  |
| 1914   | Layout 1             | `686f627a8e93`  |
| 1908   | Layout 1             | `686f627a8e93`  |
| 1897   | Layout 1             | `686f627a8e93`  |
| 1892   | Layout 1             | `686f627a8e93`  |
| 1886   | Layout 1             | `686f627a8e93`  |
| 1881   | Layout 1             | `686f627a8e93`  |
| 1871   | Layout 1             | `686f627a8e93`  |
| 1866   | Layout 1             | `686f627a8e93`  |
| 1862   | Layout 1             | `686f627a8e93`  |
| 1854   | Layout 1             | `686f627a8e93`  |
| 1846   | Layout 1             | `686f627a8e93`  |
| 1838   | Layout 1             | `686f627a8e93`  |
| 1832   | Layout 1             | `686f627a8e93`  |
| 1826   | Layout 1             | `686f627a8e93`  |
| 1822   | Layout 1             | `686f627a8e93`  |
| 1818   | Layout 1             | `686f627a8e93`  |
| 1804   | Layout 1             | `686f627a8e93`  |
| 1794   | Layout 1             | `686f627a8e93`  |
| 1790   | Layout 1             | `686f627a8e93`  |
| 1784   | Layout 1             | `686f627a8e93`  |
| 1774   | Layout 1             | `686f627a8e93`  |
| 1771   | Layout 1             | `686f627a8e93`  |
| 1762   | Layout 1             | `686f627a8e93`  |
| 1759   | Layout 1             | `686f627a8e93`  |
| 1754   | Layout 1             | `686f627a8e93`  |
| 1749   | Layout 1             | `686f627a8e93`  |
| 1743   | Layout 1             | `686f627a8e93`  |
| 1737   | Layout 1             | `686f627a8e93`  |
| 1731   | Layout 1             | `686f627a8e93`  |
| 1725   | Layout 1             | `686f627a8e93`  |
| 1717   | Layout 1             | `686f627a8e93`  |
| 1710   | Layout 1             | `686f627a8e93`  |
| 1704   | Layout 1             | `686f627a8e93`  |
| 1698   | Layout 1             | `686f627a8e93`  |
| 1690   | No documented layout | `686f627a8e93`  |
| 1685   | No documented layout | `686f627a8e93`  |
| 1680   | No documented layout | `686f627a8e93`  |
| 1674   | No documented layout | `686f627a8e93`  |
| 1668   | No documented layout | `686f627a8e93`  |
| 1659   | No documented layout | `686f627a8e93`  |
| 1649   | No documented layout | `686f627a8e93`  |
| 1642   | No documented layout | `686f627a8e93`  |
| 1636   | No documented layout | `686f627a8e93`  |
| 1628   | No documented layout | `686f627a8e93`  |
| 1622   | No documented layout | `686f627a8e93`  |
| 1614   | No documented layout | `686f627a8e93`  |
| 1608   | No documented layout | `686f627a8e93`  |
| 1602   | No documented layout | `686f627a8e93`  |
| 1598   | No documented layout | `686f627a8e93`  |
| 1594   | No documented layout | `686f627a8e93`  |
| 1590   | No documented layout | `686f627a8e93`  |
| 1587   | No documented layout | `686f627a8e93`  |
| 1584   | No documented layout | `686f627a8e93`  |
| 1579   | No documented layout | `686f627a8e93`  |
| 1572   | No documented layout | `686f627a8e93`  |
| 1565   | No documented layout | `686f627a8e93`  |
| 1559   | No documented layout | `686f627a8e93`  |
| 1554   | No documented layout | `686f627a8e93`  |
| 1547   | No documented layout | `686f627a8e93`  |
| 1537   | No documented layout | `686f627a8e93`  |
| 1529   | No documented layout | `686f627a8e93`  |
| 1524   | No documented layout | `686f627a8e93`  |
| 1519   | No documented layout | `686f627a8e93`  |
| 1509   | No documented layout | `686f627a8e93`  |
| 1506   | No documented layout | `686f627a8e93`  |
| 1504   | No documented layout | `686f627a8e93`  |
| 1500   | No documented layout | `686f627a8e93`  |
| 1493   | No documented layout | `686f627a8e93`  |
| 1489   | No documented layout | `686f627a8e93`  |
| 1485   | No documented layout | `686f627a8e93`  |
| 1481   | No documented layout | `686f627a8e93`  |
| 1474   | No documented layout | `686f627a8e93`  |
| 1466   | No documented layout | `686f627a8e93`  |
| 1462   | No documented layout | `686f627a8e93`  |
| 1459   | No documented layout | `686f627a8e93`  |
| 1453   | No documented layout | `686f627a8e93`  |
| 1450   | No documented layout | `686f627a8e93`  |
| 1445   | No documented layout | `686f627a8e93`  |
| 1439   | No documented layout | `686f627a8e93`  |
| 1433   | No documented layout | `686f627a8e93`  |
| 1430   | No documented layout | `686f627a8e93`  |
| 1426   | No documented layout | `686f627a8e93`  |
| 1421   | No documented layout | `686f627a8e93`  |
| 1417   | No documented layout | `686f627a8e93`  |
| 1416   | No documented layout | `686f627a8e93`  |
| 1409   | No documented layout | `686f627a8e93`  |
| 1405   | No documented layout | `686f627a8e93`  |
| 1401   | No documented layout | `686f627a8e93`  |
| 1396   | No documented layout | `686f627a8e93`  |
| 1391   | No documented layout | `686f627a8e93`  |
| 1390   | No documented layout | `686f627a8e93`  |
| 1386   | No documented layout | `686f627a8e93`  |
| 1381   | No documented layout | `686f627a8e93`  |
| 1379   | No documented layout | `686f627a8e93`  |
| 1372   | No documented layout | `686f627a8e93`  |
| 1366   | No documented layout | `686f627a8e93`  |
| 1364   | No documented layout | `686f627a8e93`  |
| 1363   | No documented layout | `686f627a8e93`  |
| 1360   | No documented layout | `686f627a8e93`  |
| 1358   | No documented layout | `686f627a8e93`  |
| 1355   | No documented layout | `686f627a8e93`  |
| 1351   | No documented layout | `686f627a8e93`  |
| 1348   | No documented layout | `686f627a8e93`  |
| 1346   | No documented layout | `686f627a8e93`  |
| 1341   | No documented layout | `686f627a8e93`  |
| 1340   | No documented layout | `686f627a8e93`  |
| 1338   | No documented layout | `686f627a8e93`  |
| 1335   | No documented layout | `686f627a8e93`  |
| 1333   | No documented layout | `686f627a8e93`  |
| 1329   | No documented layout | `686f627a8e93`  |
| 1327   | No documented layout | `686f627a8e93`  |
| 1324   | No documented layout | `686f627a8e93`  |
| 1321   | No documented layout | `686f627a8e93`  |
| 1319   | No documented layout | `686f627a8e93`  |
| 1318   | No documented layout | `686f627a8e93`  |
| 1316   | No documented layout | `686f627a8e93`  |
| 1313   | No documented layout | `686f627a8e93`  |
| 1311   | No documented layout | `686f627a8e93`  |
| 1309   | No documented layout | `686f627a8e93`  |
| 1304   | No documented layout | `686f627a8e93`  |
| 1292   | No documented layout | `686f627a8e93`  |
| 1286   | No documented layout | `686f627a8e93`  |
| 1280   | No documented layout | `686f627a8e93`  |
| 1276   | No documented layout | `686f627a8e93`  |
| 1267   | No documented layout | `686f627a8e93`  |
| 1261   | No documented layout | `686f627a8e93`  |
| 1256   | No documented layout | `686f627a8e93`  |
| 1250   | No documented layout | `686f627a8e93`  |
| 1246   | No file              | `686f627a8e93`  |
| 1239   | No file              | `686f627a8e93`  |
| 1230   | No file              | `686f627a8e93`  |
| 1226   | No file              | `686f627a8e93`  |
| 1220   | No file              | `686f627a8e93`  |
| 1217   | No file              | `686f627a8e93`  |
| 1211   | No file              | `686f627a8e93`  |
| 1210   | No file              | `686f627a8e93`  |
| 1208   | No file              | `686f627a8e93`  |
| 1203   | No file              | `686f627a8e93`  |
| 1197   | No file              | `686f627a8e93`  |
| 1194   | No file              | `686f627a8e93`  |
| 1192   | No file              | `686f627a8e93`  |
| 1187   | No file              | `686f627a8e93`  |
| 1183   | No file              | `686f627a8e93`  |
| 1177   | No file              | `686f627a8e93`  |
| 1173   | No file              | `686f627a8e93`  |
| 1167   | No file              | `686f627a8e93`  |
| 1164   | No file              | `686f627a8e93`  |
| 1156   | No file              | `686f627a8e93`  |
| 1149   | No file              | `686f627a8e93`  |
| 1144   | No file              | `686f627a8e93`  |
| 1137   | No file              | `686f627a8e93`  |
| 1132   | No file              | `686f627a8e93`  |
| 1127   | No file              | `686f627a8e93`  |
| 1122   | No file              | `686f627a8e93`  |
| 1118   | No file              | `686f627a8e93`  |
| 1114   | No file              | `686f627a8e93`  |
| 1109   | No file              | `686f627a8e93`  |
| 1102   | No file              | `686f627a8e93`  |
| 1096   | No file              | `686f627a8e93`  |
| 1088   | No file              | `686f627a8e93`  |
| 1081   | No file              | `686f627a8e93`  |
| 1076   | No file              | `686f627a8e93`  |
| 1069   | No file              | `686f627a8e93`  |
| 1064   | No file              | `686f627a8e93`  |
| 1058   | No file              | `686f627a8e93`  |
| 1051   | No file              | `686f627a8e93`  |
| 1044   | No file              | `686f627a8e93`  |
| 1036   | No file              | `686f627a8e93`  |
| 1026   | No file              | `686f627a8e93`  |
| 1016   | No file              | `686f627a8e93`  |
| 1009   | No file              | `686f627a8e93`  |
| 1005   | No file              | `686f627a8e93`  |
| 1000   | No file              | `686f627a8e93`  |
| 998    | No file              | `686f627a8e93`  |
| 990    | No file              | `686f627a8e93`  |
| 979    | No file              | `686f627a8e93`  |
| 972    | No file              | `686f627a8e93`  |
| 963    | No file              | `686f627a8e93`  |
| 955    | No file              | `686f627a8e93`  |
| 946    | No file              | `686f627a8e93`  |
| 938    | No file              | `686f627a8e93`  |
| 927    | No file              | `686f627a8e93`  |
| 911    | No file              | `686f627a8e93`  |
| 904    | No file              | `686f627a8e93`  |
| 899    | No file              | `686f627a8e93`  |
| 894    | No file              | `686f627a8e93`  |
| 885    | No file              | `686f627a8e93`  |
| 879    | No file              | `686f627a8e93`  |
| 872    | No file              | `686f627a8e93`  |
| 864    | No file              | `686f627a8e93`  |
| 855    | No file              | `686f627a8e93`  |
| 853    | No file              | `686f627a8e93`  |
| 845    | No file              | `686f627a8e93`  |
| 837    | No file              | `686f627a8e93`  |
| 829    | No file              | `686f627a8e93`  |
| 822    | No file              | `686f627a8e93`  |
| 814    | No file              | `686f627a8e93`  |
| 805    | No file              | `686f627a8e93`  |
| 794    | No file              | `686f627a8e93`  |
| 787    | No file              | `686f627a8e93`  |
| 780    | No file              | `686f627a8e93`  |
| 771    | No file              | `686f627a8e93`  |
| 760    | No file              | `686f627a8e93`  |
| 748    | No file              | `686f627a8e93`  |
| 741    | No file              | `686f627a8e93`  |
| 736    | No file              | `686f627a8e93`  |
| 731    | No file              | `686f627a8e93`  |
| 723    | No file              | `686f627a8e93`  |
| 711    | No file              | `686f627a8e93`  |
| 707    | No file              | `686f627a8e93`  |
| 697    | No file              | `686f627a8e93`  |
| 689    | No file              | `686f627a8e93`  |
| 683    | No file              | `686f627a8e93`  |
| 678    | No file              | `686f627a8e93`  |
| 670    | No file              | `686f627a8e93`  |
| 661    | No file              | `686f627a8e93`  |
| 656    | No file              | `686f627a8e93`  |
| 652    | No file              | `686f627a8e93`  |
| 643    | No file              | `686f627a8e93`  |
| 637    | No file              | `686f627a8e93`  |
| 630    | No file              | `686f627a8e93`  |
| 627    | No file              | `686f627a8e93`  |
| 621    | No file              | `686f627a8e93`  |
| 617    | No file              | `686f627a8e93`  |
| 615    | No file              | `686f627a8e93`  |
| 606    | No file              | `686f627a8e93`  |
| 599    | No file              | `686f627a8e93`  |
| 592    | No file              | `686f627a8e93`  |
| 586    | No file              | `686f627a8e93`  |
| 577    | No file              | `686f627a8e93`  |
| 569    | No file              | `686f627a8e93`  |
| 561    | No file              | `686f627a8e93`  |
| 554    | No file              | `686f627a8e93`  |
| 542    | No file              | `686f627a8e93`  |
| 532    | No file              | `686f627a8e93`  |
| 531    | No file              | `686f627a8e93`  |
| 526    | No file              | `686f627a8e93`  |
| 521    | No file              | `686f627a8e93`  |
| 517    | No file              | `686f627a8e93`  |
| 510    | No file              | `686f627a8e93`  |
| 508    | No file              | `686f627a8e93`  |
| 504    | No file              | `686f627a8e93`  |
| 497    | No file              | `686f627a8e93`  |
| 491    | No file              | `686f627a8e93`  |
| 485    | No file              | `686f627a8e93`  |
| 478    | No file              | `686f627a8e93`  |
| 472    | No file              | `686f627a8e93`  |
| 466    | No file              | `686f627a8e93`  |
| 457    | No file              | `686f627a8e93`  |
| 452    | No file              | `686f627a8e93`  |
| 449    | No file              | `686f627a8e93`  |
| 435    | No file              | `686f627a8e93`  |

<!-- versions:end -->

## Companion Files

- `titleoffset.dbss` - required. Provides `title_id -> (offset, size)` block
  lookup.
- `languagedata_en.loc` - optional for English title/requirement display.

## Layout 1

### File Layout

A record count, then the records back to back; `titleoffset.dbss` addresses
each one.

| Offset  | Type          | Field   | Notes                                           |
| ------- | ------------- | ------- | ----------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; equals the `titleoffset.dbss` count |
| `+0x04` | Record[count] | records | See Record                                      |

### Record (variable: 100 bytes + text)

All inspected records fit one generalized header. The older A/B/C layouts are
just `key_count` values 1, 2, and 3. The tail after `requirement_text_kr`
reads the same on all 3,177 records of client 3473; the tail names count from
the end of `requirement_text_kr`.

| Offset                     | Type           | Field                     | Notes                                                             |
| -------------------------- | -------------- | ------------------------- | ----------------------------------------------------------------- |
| `+0x00`                    | u32            | key_count                 | Number of 32-bit key/hash/group fields before `title_id`          |
| `+0x04`                    | u32[key_count] | key_values                | `key_count` values                                                |
| `key_values+0x00`          | u32            | title_id                  | Matches offset entry and loc string ID                            |
| `key_values+0x04`          | str16          | title_text_kr             | Korean title; PAColor-tagged on the styled title records, see Styled Title Records |
| `title_text_kr+0x00`       | str16          | requirement_text_kr       | Korean requirement, usually with PAColor tags                     |
| `requirement_text_kr+0x00` | u32            | unknown_tail_00           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x04` | u32            | category_id               | See Category IDs; `0` on 1,321 records, `1` on 900, `2` on 197, `3` on 759 (client 3473) |
| `requirement_text_kr+0x08` | bytes[20]      | unknown_tail_08           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x1C` | u32            | unknown_tail_1c           | `0` on 3,102 records; else `3600` to `7776000`, all multiples of 3,600 (`2592000` on 37) (client 3473) |
| `requirement_text_kr+0x20` | u32            | unknown_tail_20           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x24` | u32            | unknown_tail_24           | `0` on 3,082 records; else `604800` to `15552000`, all multiples of 3,600 (`2592000` on 50) (client 3473) |
| `requirement_text_kr+0x28` | u32            | unknown_tail_28           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x2C` | str8           | effect_name               | Aura/effect name, e.g. `vCalsutain_Buff_Aura_02A`; empty on 3,105 records (client 3473) |
| `effect_name+0x00`         | str8           | color_argb                | ASCII hex, e.g. `FFFF7124`; 8 characters on 365 records, else empty (client 3473) |
| `color_argb+0x00`          | u32            | color_value               | Same value as little-endian integer; `0` when `color_argb` is empty |
| `color_argb+0x04`          | bytes[12]      | unknown_after_color_value | Always `0` (client 3473)                                          |

Observed `key_count` distribution:

| key_count | Count | Former Layout  |
| --------- | ----- | -------------- |
| 1         | 2,844 | A              |
| 2         | 175   | B              |
| 3         | 15    | C              |
| 4         | 1     | Previously `?` |
| 6         | 13    | Previously `?` |

Earlier versions of this doc read the count of `title_text_kr` as a u32
`style_or_title_len` and a u32 `zero`, and the count of
`requirement_text_kr` as a u16 `requirement_text_length` and three u16 `0`.
Both are the u64 count of a `str16`.

### `titleoffset.dbss`

| Offset  | Type              | Field | Notes       |
| ------- | ----------------- | ----- | ----------- |
| `+0x00` | u32               | count | Entry count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row |

Observed entries: 3,048 in the pre-2026-09-27 test fixture, 3,172 in the
2026-09-27 client. The largest `offset + size` equals the `title.dbss` byte
length, so the offset table accounts for the full file.

### Offset Row (12 bytes)

| Offset  | Type | Field    | Notes                                                |
| ------- | ---- | -------- | ---------------------------------------------------- |
| `+0x00` | u32  | title_id | Title ID                                             |
| `+0x04` | u32  | offset   | Offset into `title.dbss`, at the record's `key_count` |
| `+0x08` | u32  | size     | Block size                                           |

## Text Payload

Most records have a plain Korean title followed by the Korean requirement
string.

The count of `requirement_text_kr` is the UTF-16 code-unit length of the tagged
requirement string, not the visible text length after stripping PA tags.

Example, title ID `44`:

| Field                     | Value                    |
| ------------------------- | ------------------------ |
| English title             | `Stoneback Crab Artisan` |
| Korean title              | `돌멘게 공예가`          |
| Requirement length marker | `66`                     |
| Tagged requirement length | `66`                     |
| Plain requirement length  | `35`                     |
| Category                  | `1` / Combat             |

## Styled Title Records

Thirty records, title IDs `3645..3674`, begin their text payload with a PAColor
tag. These are class "MASTER ..." titles. For these records, as for every
other, the header field after `title_id` is the count of `title_text_kr`, here
the length of the styled title payload.

Example, title ID `3645`:

| Field                            | Value                   |
| -------------------------------- | ----------------------- |
| Header field                     | `231`                   |
| Styled title payload length      | `231` UTF-16 code units |
| Plain title after stripping tags | `MASTER WARRIOR`        |
| Requirement length marker        | `115`                   |
| Category                         | `0` / World             |

An earlier version of this doc read the styled title payload as 232 code units,
the header field plus one, with the requirement length marker as its final code
unit. That last unit is the low half of the `requirement_text_kr` count.

## Category IDs

`title.dbss` itself carries a category field after the requirement text.

| ID  | Name       |
| --- | ---------- |
| 0   | World      |
| 1   | Combat     |
| 2   | Life Skill |
| 3   | Fishing    |

## Extra Payload And Title Color

Most default-color titles have no non-zero payload after the category field.
Most non-default-color titles have a 64-byte or 88-byte extra payload. The title
color is encoded near the end of that payload as both an ASCII `AARRGGBB`
string and the same value as a little-endian u32.

The extra payload is the Record tail from `unknown_tail_08` to
`unknown_after_color_value` with its trailing zeros cut: 64 bytes when
`effect_name` is empty and `color_argb` holds 8 characters, 88 bytes when
`effect_name` holds 24. `color_argb` is the `color_len` and `color_argb` of
earlier versions of this doc, and `effect_name` their `effect_len` and
`effect_name`.

Example:

```text
46 46 46 46 37 31 32 34 24 71 ff ff
F  F  F  F  7  1  2  4  packed 0xFFFF7124
```

This decodes to `0xFFFF7124`, displayed in CSS as `#FF7124`.

88-byte payloads add an aura/effect string before the color. The name is
probably misspelled data (`Calsutain` instead of `Calustian` or similar), so
parsers should preserve it exactly.

In the current extracted sample, 335 records decode a title color from this
payload. For example, title ID `3451` (`Fisher`) has the same `0xFFAFEEEE`
payload color as `Angel`. This was visually confirmed in-game.

Other visual confirmations:

| Titles                                                           | Payload Color | Result                                |
| ---------------------------------------------------------------- | ------------- | ------------------------------------- |
| `The Greatest Guardian`, `#BDORemastered`, `One of the Greatest` | `0xFFFF7124`  | Same color                            |
| `REBOOT`                                                         | `0xFFFF7124`  | Same color family as the titles above |
| `Nouverikant`                                                    | `0xFFFFB400`  | Not the same as `REBOOT`              |

These confirmations support using the DBSS payload color as the precise source
for individual non-default title display.

## PAColor Tags

Requirement text commonly starts with:

```text
<PAColor0xFFf32200>칭호 조건<PAOldColor>:
```

This default requirement label color is not the visible title-name color.
The English requirement (LOC type 1, `str_id4` 1) carries the same tag on its
`Title Requirement` label in all 3,322 rows on client 3458. The parser keeps the
tags in `requirement_text_kr`, and the table draws them.

Special "MASTER ..." title names are different: their title payload itself is
PAColor-tagged, so those PAColor tags are part of the displayed title name. The
tags draw a gradient, one colour per letter pair: `MASTER WARRIOR` goes from
`0xffffffff` on `MA` down to `0xff424242` on `R`, as in game. The parser keeps
the tags in `title_text_kr`, and the English LOC name (type 1) carries the same
tags. Two more LOC names are tagged without a styled payload (`Seasonal
Sensation!`, `Rise Above the Disorder`); 1348 `Lights, Camera, Action!` has a
stored payload colour and a different LOC tag colour; the table draws the tag
colour (unchecked in game).

## Style Field

Earlier versions of this doc read the header field after `title_id`
(`style_or_title_len`) as a style/category-like value for normal records, with
common values `2..17`, rare values through `28` and `43`, and a few high values
used only by styled title records. It is the count of `title_text_kr`: the
title's length in UTF-16 code units.

It does not identify the final visible title color. Counterexample: three
titles of 7 code units each.

| Title ID | Title                      | Header Field | Visual Result |
| -------- | -------------------------- | ------------ | ------------- |
| `2117`   | The Greatest Guardian      | `7`          | Special color |
| `44`     | Stoneback Crab Artisan     | `7`          | Normal blue   |
| `45`     | Stoneback Crab Philosopher | `7`          | Normal blue   |

## Optional Extra Payload

Some color payloads also include small non-zero integers at `unknown_tail_1c`
and `unknown_tail_24` (`+0x14` and `+0x1C` of the extra payload). These look
like grouping/effect parameters, not the title color itself.

## Recommended Parser Behavior

1. Use `titleoffset.dbss` to slice blocks.
2. Read `key_count`, then `key_values` and `title_id`.
3. Read `title_text_kr` and `requirement_text_kr` through their u64 counts.
4. Read `category_id`, then `effect_name`, `color_argb` and `color_value` at
   their Record offsets.
5. A `title_text_kr` that starts with a PAColor tag is a styled title.
6. Strip PA tags only for readable display; keep raw PA tags for debugging.
7. Look up English name/requirement from `languagedata_en.loc`:
   - Name: `str_type=1, str_id1=title_id, str_id4=0`
   - Requirement: `str_type=1, str_id1=title_id, str_id4=1`

## Notes

- The previously unknown `?` layouts are now explained by `key_count` values 4
  and 6.
- The old `u32_14`, `u32_18`, and similar columns can be UTF-16 text fragments,
  not structured integers.
- `titlecategory.bss` is not needed for category display; `title.dbss` carries
  the category after the requirement string.

## Open Questions

### Extra Payload Parameters

The color value and optional aura/effect name are now decoded, but
`unknown_tail_1c` and `unknown_tail_24` in the extra payload are still
unresolved.

### Normal Title Name Color

For titles without an extra color payload, the default visible color is still
not stored as a per-record RGB value in `title.dbss`. Disproven candidates:

- Requirement `_PA_COLOR_MARKER`
- `style_or_title_len` alone (the count of `title_text_kr`)
- A fixed early `u32` field after the title text

Likely sources still to investigate:

- client-side title color table
- UI scripts / title rendering logic
- another DBSS file related to title grade/type/color
- implicit default color chosen by title category/UI code
