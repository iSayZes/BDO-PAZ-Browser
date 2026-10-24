# `mansionpartinfo.bss` Format

## Purpose

The part pictures of the manors whose parts can be changed in installation
mode: one fixed 12-byte row per manor part with the manor's ID, the part index
and the picture path as a string table index. Each picture is a blueprint of
the whole building, an overhead cutaway render with that part highlighted in
magenta. The rows name buildings, not characters, although the manor ID is the
building's key in `characterstatic.dbss`, where houses are records like NPCs.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ---------------- | --------- |
| 2      | 1642 and later | 3483    | `mansionpartinfo.bss` | 664   | 9 Manor Part Row | 12        |
| 1      | 1737 to 2151   | 2151    | `mansionpartinfo.bss` | 491   | 6 Manor Part Row | 16        |

| Layout | File                  | Known         | Unknown      |
| ------ | --------------------- | ------------- | ------------ |
| 2      | `mansionpartinfo.bss` | 619 B (93.2%) | 45 B (6.8%)  |
| 1      | `mansionpartinfo.bss` | 437 B (89.0%) | 54 B (11.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `d0a188773fff`  |
| 3482   | Layout 2 | `d0a188773fff`  |
| 3474   | Layout 2 | `d0a188773fff`  |
| 3473   | Layout 2 | `d0a188773fff`  |
| 3464   | Layout 2 | `d0a188773fff`  |
| 3458   | Layout 2 | `d0a188773fff`  |
| 3454   | Layout 2 | `d0a188773fff`  |
| 3444   | Layout 2 | `d0a188773fff`  |
| 3435   | Layout 2 | `d0a188773fff`  |
| 3426   | Layout 2 | `d0a188773fff`  |
| 3418   | Layout 2 | `d0a188773fff`  |
| 3412   | Layout 2 | `d0a188773fff`  |
| 3402   | Layout 2 | `d0a188773fff`  |
| 3396   | Layout 2 | `d0a188773fff`  |
| 3387   | Layout 2 | `d0a188773fff`  |
| 3381   | Layout 2 | `d0a188773fff`  |
| 3373   | Layout 2 | `d0a188773fff`  |
| 3364   | Layout 2 | `d0a188773fff`  |
| 3356   | Layout 2 | `d0a188773fff`  |
| 3349   | Layout 2 | `d0a188773fff`  |
| 3342   | Layout 2 | `d0a188773fff`  |
| 3335   | Layout 2 | `d0a188773fff`  |
| 3326   | Layout 2 | `d0a188773fff`  |
| 3321   | Layout 2 | `d0a188773fff`  |
| 3314   | Layout 2 | `d0a188773fff`  |
| 3303   | Layout 2 | `d0a188773fff`  |
| 3302   | Layout 2 | `d0a188773fff`  |
| 3293   | Layout 2 | `d0a188773fff`  |
| 3283   | Layout 2 | `d0a188773fff`  |
| 3275   | Layout 2 | `d0a188773fff`  |
| 3267   | Layout 2 | `d0a188773fff`  |
| 3258   | Layout 2 | `d0a188773fff`  |
| 3251   | Layout 2 | `d0a188773fff`  |
| 3242   | Layout 2 | `d0a188773fff`  |
| 3235   | Layout 2 | `d0a188773fff`  |
| 3229   | Layout 2 | `d0a188773fff`  |
| 3212   | Layout 2 | `d0a188773fff`  |
| 3203   | Layout 2 | `d0a188773fff`  |
| 3193   | Layout 2 | `d0a188773fff`  |
| 3186   | Layout 2 | `d0a188773fff`  |
| 3177   | Layout 2 | `d0a188773fff`  |
| 3169   | Layout 2 | `d0a188773fff`  |
| 3158   | Layout 2 | `d0a188773fff`  |
| 3151   | Layout 2 | `d0a188773fff`  |
| 3144   | Layout 2 | `d0a188773fff`  |
| 3133   | Layout 2 | `d0a188773fff`  |
| 3125   | Layout 2 | `d0a188773fff`  |
| 3118   | Layout 2 | `d0a188773fff`  |
| 3111   | Layout 2 | `d0a188773fff`  |
| 3103   | Layout 2 | `d0a188773fff`  |
| 3095   | Layout 2 | `d0a188773fff`  |
| 3086   | Layout 2 | `d0a188773fff`  |
| 3072   | Layout 2 | `d0a188773fff`  |
| 3062   | Layout 2 | `d0a188773fff`  |
| 3052   | Layout 2 | `d0a188773fff`  |
| 3045   | Layout 2 | `d0a188773fff`  |
| 3037   | Layout 2 | `d0a188773fff`  |
| 3030   | Layout 2 | `d0a188773fff`  |
| 3021   | Layout 2 | `d0a188773fff`  |
| 3012   | Layout 2 | `d0a188773fff`  |
| 3002   | Layout 2 | `d0a188773fff`  |
| 2995   | Layout 2 | `d0a188773fff`  |
| 2987   | Layout 2 | `d0a188773fff`  |
| 2978   | Layout 2 | `d0a188773fff`  |
| 2970   | Layout 2 | `d0a188773fff`  |
| 2959   | Layout 2 | `d0a188773fff`  |
| 2951   | Layout 2 | `d0a188773fff`  |
| 2942   | Layout 2 | `d0a188773fff`  |
| 2935   | Layout 2 | `d0a188773fff`  |
| 2932   | Layout 2 | `d0a188773fff`  |
| 2923   | Layout 2 | `d0a188773fff`  |
| 2919   | Layout 2 | `d0a188773fff`  |
| 2907   | Layout 2 | `d0a188773fff`  |
| 2900   | Layout 2 | `d0a188773fff`  |
| 2891   | Layout 2 | `d0a188773fff`  |
| 2882   | Layout 2 | `d0a188773fff`  |
| 2872   | Layout 2 | `d0a188773fff`  |
| 2863   | Layout 2 | `d0a188773fff`  |
| 2855   | Layout 2 | `d0a188773fff`  |
| 2849   | Layout 2 | `d0a188773fff`  |
| 2844   | Layout 2 | `d0a188773fff`  |
| 2834   | Layout 2 | `d0a188773fff`  |
| 2825   | Layout 2 | `d0a188773fff`  |
| 2819   | Layout 2 | `d0a188773fff`  |
| 2811   | Layout 2 | `d0a188773fff`  |
| 2803   | Layout 2 | `d0a188773fff`  |
| 2794   | Layout 2 | `d0a188773fff`  |
| 2783   | Layout 2 | `d0a188773fff`  |
| 2774   | Layout 2 | `d0a188773fff`  |
| 2765   | Layout 2 | `d0a188773fff`  |
| 2756   | Layout 2 | `d0a188773fff`  |
| 2750   | Layout 2 | `d0a188773fff`  |
| 2743   | Layout 2 | `d0a188773fff`  |
| 2736   | Layout 2 | `d0a188773fff`  |
| 2726   | Layout 2 | `d0a188773fff`  |
| 2717   | Layout 2 | `d0a188773fff`  |
| 2709   | Layout 2 | `d0a188773fff`  |
| 2703   | Layout 2 | `d0a188773fff`  |
| 2695   | Layout 2 | `d0a188773fff`  |
| 2684   | Layout 2 | `d0a188773fff`  |
| 2672   | Layout 2 | `d0a188773fff`  |
| 2665   | Layout 2 | `d0a188773fff`  |
| 2657   | Layout 2 | `d0a188773fff`  |
| 2649   | Layout 2 | `d0a188773fff`  |
| 2644   | Layout 2 | `d0a188773fff`  |
| 2637   | Layout 2 | `d0a188773fff`  |
| 2629   | Layout 2 | `d0a188773fff`  |
| 2619   | Layout 2 | `d0a188773fff`  |
| 2612   | Layout 2 | `d0a188773fff`  |
| 2606   | Layout 2 | `d0a188773fff`  |
| 2602   | Layout 2 | `d0a188773fff`  |
| 2601   | Layout 2 | `d0a188773fff`  |
| 2592   | Layout 2 | `d0a188773fff`  |
| 2583   | Layout 2 | `d0a188773fff`  |
| 2575   | Layout 2 | `d0a188773fff`  |
| 2567   | Layout 2 | `d0a188773fff`  |
| 2560   | Layout 2 | `d0a188773fff`  |
| 2553   | Layout 2 | `d0a188773fff`  |
| 2545   | Layout 2 | `d0a188773fff`  |
| 2538   | Layout 2 | `d0a188773fff`  |
| 2529   | Layout 2 | `d0a188773fff`  |
| 2519   | Layout 2 | `d0a188773fff`  |
| 2513   | Layout 2 | `d0a188773fff`  |
| 2510   | Layout 2 | `d0a188773fff`  |
| 2507   | Layout 2 | `d0a188773fff`  |
| 2503   | Layout 2 | `d0a188773fff`  |
| 2498   | Layout 2 | `d0a188773fff`  |
| 2492   | Layout 2 | `d0a188773fff`  |
| 2487   | Layout 2 | `d0a188773fff`  |
| 2480   | Layout 2 | `d0a188773fff`  |
| 2474   | Layout 2 | `d0a188773fff`  |
| 2468   | Layout 2 | `d0a188773fff`  |
| 2460   | Layout 2 | `d0a188773fff`  |
| 2453   | Layout 2 | `d0a188773fff`  |
| 2444   | Layout 2 | `d0a188773fff`  |
| 2438   | Layout 2 | `d0a188773fff`  |
| 2434   | Layout 2 | `d0a188773fff`  |
| 2429   | Layout 2 | `d0a188773fff`  |
| 2421   | Layout 2 | `d0a188773fff`  |
| 2414   | Layout 2 | `d0a188773fff`  |
| 2407   | Layout 2 | `d0a188773fff`  |
| 2401   | Layout 2 | `d0a188773fff`  |
| 2397   | Layout 2 | `d0a188773fff`  |
| 2393   | Layout 2 | `d0a188773fff`  |
| 2384   | Layout 2 | `d0a188773fff`  |
| 2378   | Layout 2 | `d0a188773fff`  |
| 2372   | Layout 2 | `d0a188773fff`  |
| 2358   | Layout 2 | `d0a188773fff`  |
| 2352   | Layout 2 | `d0a188773fff`  |
| 2347   | Layout 2 | `d0a188773fff`  |
| 2343   | Layout 2 | `d0a188773fff`  |
| 2335   | Layout 2 | `d0a188773fff`  |
| 2327   | Layout 2 | `d0a188773fff`  |
| 2324   | Layout 2 | `d0a188773fff`  |
| 2319   | Layout 2 | `d0a188773fff`  |
| 2313   | Layout 2 | `d0a188773fff`  |
| 2308   | Layout 2 | `d0a188773fff`  |
| 2302   | Layout 2 | `d0a188773fff`  |
| 2295   | Layout 2 | `d0a188773fff`  |
| 2290   | Layout 2 | `d0a188773fff`  |
| 2284   | Layout 2 | `d0a188773fff`  |
| 2276   | Layout 2 | `d0a188773fff`  |
| 2269   | Layout 2 | `d0a188773fff`  |
| 2259   | Layout 2 | `d0a188773fff`  |
| 2250   | Layout 2 | `d0a188773fff`  |
| 2243   | Layout 2 | `d0a188773fff`  |
| 2235   | Layout 2 | `d0a188773fff`  |
| 2229   | Layout 2 | `d0a188773fff`  |
| 2224   | Layout 2 | `d0a188773fff`  |
| 2218   | Layout 2 | `d0a188773fff`  |
| 2215   | Layout 2 | `d0a188773fff`  |
| 2207   | Layout 2 | `d0a188773fff`  |
| 2203   | Layout 2 | `d0a188773fff`  |
| 2196   | Layout 2 | `d0a188773fff`  |
| 2192   | Layout 2 | `d0a188773fff`  |
| 2189   | Layout 2 | `d0a188773fff`  |
| 2183   | Layout 2 | `d0a188773fff`  |
| 2179   | Layout 2 | `d0a188773fff`  |
| 2171   | Layout 2 | `d0a188773fff`  |
| 2163   | Layout 2 | `d0a188773fff`  |
| 2156   | Layout 2 | `d0a188773fff`  |
| 2151   | Layout 1 | `d0a188773fff`  |
| 2147   | Layout 1 | `d0a188773fff`  |
| 2142   | Layout 1 | `d0a188773fff`  |
| 2138   | Layout 1 | `d0a188773fff`  |
| 2134   | Layout 1 | `d0a188773fff`  |
| 2130   | Layout 1 | `d0a188773fff`  |
| 2122   | Layout 1 | `d0a188773fff`  |
| 2107   | Layout 1 | `d0a188773fff`  |
| 2098   | Layout 1 | `d0a188773fff`  |
| 2089   | Layout 1 | `d0a188773fff`  |
| 2081   | Layout 1 | `d0a188773fff`  |
| 2073   | Layout 1 | `d0a188773fff`  |
| 2067   | Layout 1 | `d0a188773fff`  |
| 2063   | Layout 1 | `d0a188773fff`  |
| 2059   | Layout 1 | `d0a188773fff`  |
| 2052   | Layout 1 | `d0a188773fff`  |
| 2044   | Layout 1 | `d0a188773fff`  |
| 2039   | Layout 1 | `d0a188773fff`  |
| 2032   | Layout 1 | `d0a188773fff`  |
| 2025   | Layout 1 | `d0a188773fff`  |
| 2011   | Layout 1 | `d0a188773fff`  |
| 2005   | Layout 1 | `d0a188773fff`  |
| 2000   | Layout 1 | `d0a188773fff`  |
| 1996   | Layout 1 | `d0a188773fff`  |
| 1991   | Layout 1 | `d0a188773fff`  |
| 1985   | Layout 1 | `d0a188773fff`  |
| 1980   | Layout 1 | `d0a188773fff`  |
| 1969   | Layout 1 | `d0a188773fff`  |
| 1964   | Layout 1 | `d0a188773fff`  |
| 1958   | Layout 1 | `d0a188773fff`  |
| 1950   | Layout 1 | `d0a188773fff`  |
| 1945   | Layout 1 | `d0a188773fff`  |
| 1937   | Layout 1 | `d0a188773fff`  |
| 1933   | Layout 1 | `d0a188773fff`  |
| 1927   | Layout 1 | `d0a188773fff`  |
| 1921   | Layout 1 | `d0a188773fff`  |
| 1914   | Layout 1 | `d0a188773fff`  |
| 1908   | Layout 1 | `d0a188773fff`  |
| 1897   | Layout 1 | `d0a188773fff`  |
| 1892   | Layout 1 | `d0a188773fff`  |
| 1886   | Layout 1 | `d0a188773fff`  |
| 1881   | Layout 1 | `d0a188773fff`  |
| 1871   | Layout 1 | `d0a188773fff`  |
| 1866   | Layout 1 | `d0a188773fff`  |
| 1862   | Layout 1 | `d0a188773fff`  |
| 1854   | Layout 1 | `d0a188773fff`  |
| 1846   | Layout 1 | `d0a188773fff`  |
| 1838   | Layout 1 | `d0a188773fff`  |
| 1832   | Layout 1 | `d0a188773fff`  |
| 1826   | Layout 1 | `d0a188773fff`  |
| 1822   | Layout 1 | `d0a188773fff`  |
| 1818   | Layout 1 | `d0a188773fff`  |
| 1804   | Layout 1 | `d0a188773fff`  |
| 1794   | Layout 1 | `d0a188773fff`  |
| 1790   | Layout 1 | `d0a188773fff`  |
| 1784   | Layout 1 | `d0a188773fff`  |
| 1774   | Layout 1 | `d0a188773fff`  |
| 1771   | Layout 1 | `d0a188773fff`  |
| 1762   | Layout 1 | `d0a188773fff`  |
| 1759   | Layout 1 | `d0a188773fff`  |
| 1754   | Layout 1 | `d0a188773fff`  |
| 1749   | Layout 1 | `d0a188773fff`  |
| 1743   | Layout 1 | `d0a188773fff`  |
| 1737   | Layout 1 | `d0a188773fff`  |
| 1731   | Layout 2 | `d0a188773fff`  |
| 1725   | Layout 2 | `d0a188773fff`  |
| 1717   | Layout 2 | `d0a188773fff`  |
| 1710   | Layout 2 | `d0a188773fff`  |
| 1704   | Layout 2 | `d0a188773fff`  |
| 1698   | Layout 2 | `d0a188773fff`  |
| 1690   | Layout 2 | `d0a188773fff`  |
| 1685   | Layout 2 | `d0a188773fff`  |
| 1680   | Layout 2 | `d0a188773fff`  |
| 1674   | Layout 2 | `d0a188773fff`  |
| 1668   | Layout 2 | `d0a188773fff`  |
| 1659   | Layout 2 | `d0a188773fff`  |
| 1649   | Layout 2 | `d0a188773fff`  |
| 1642   | Layout 2 | `d0a188773fff`  |
| 1636   | No file  | `d0a188773fff`  |
| 1628   | No file  | `d0a188773fff`  |
| 1622   | No file  | `d0a188773fff`  |
| 1614   | No file  | `d0a188773fff`  |
| 1608   | No file  | `d0a188773fff`  |
| 1602   | No file  | `d0a188773fff`  |
| 1598   | No file  | `d0a188773fff`  |
| 1594   | No file  | `d0a188773fff`  |
| 1590   | No file  | `d0a188773fff`  |
| 1587   | No file  | `d0a188773fff`  |
| 1584   | No file  | `d0a188773fff`  |
| 1579   | No file  | `d0a188773fff`  |
| 1572   | No file  | `d0a188773fff`  |
| 1565   | No file  | `d0a188773fff`  |
| 1559   | No file  | `d0a188773fff`  |
| 1554   | No file  | `d0a188773fff`  |
| 1547   | No file  | `d0a188773fff`  |
| 1537   | No file  | `d0a188773fff`  |
| 1529   | No file  | `d0a188773fff`  |
| 1524   | No file  | `d0a188773fff`  |
| 1519   | No file  | `d0a188773fff`  |
| 1509   | No file  | `d0a188773fff`  |
| 1506   | No file  | `d0a188773fff`  |
| 1504   | No file  | `d0a188773fff`  |
| 1500   | No file  | `d0a188773fff`  |
| 1493   | No file  | `d0a188773fff`  |
| 1489   | No file  | `d0a188773fff`  |
| 1485   | No file  | `d0a188773fff`  |
| 1481   | No file  | `d0a188773fff`  |
| 1474   | No file  | `d0a188773fff`  |
| 1466   | No file  | `d0a188773fff`  |
| 1462   | No file  | `d0a188773fff`  |
| 1459   | No file  | `d0a188773fff`  |
| 1453   | No file  | `d0a188773fff`  |
| 1450   | No file  | `d0a188773fff`  |
| 1445   | No file  | `d0a188773fff`  |
| 1439   | No file  | `d0a188773fff`  |
| 1433   | No file  | `d0a188773fff`  |
| 1430   | No file  | `d0a188773fff`  |
| 1426   | No file  | `d0a188773fff`  |
| 1421   | No file  | `d0a188773fff`  |
| 1417   | No file  | `d0a188773fff`  |
| 1416   | No file  | `d0a188773fff`  |
| 1409   | No file  | `d0a188773fff`  |
| 1405   | No file  | `d0a188773fff`  |
| 1401   | No file  | `d0a188773fff`  |
| 1396   | No file  | `d0a188773fff`  |
| 1391   | No file  | `d0a188773fff`  |
| 1390   | No file  | `d0a188773fff`  |
| 1386   | No file  | `d0a188773fff`  |
| 1381   | No file  | `d0a188773fff`  |
| 1379   | No file  | `d0a188773fff`  |
| 1372   | No file  | `d0a188773fff`  |
| 1366   | No file  | `d0a188773fff`  |
| 1364   | No file  | `d0a188773fff`  |
| 1363   | No file  | `d0a188773fff`  |
| 1360   | No file  | `d0a188773fff`  |
| 1358   | No file  | `d0a188773fff`  |
| 1355   | No file  | `d0a188773fff`  |
| 1351   | No file  | `d0a188773fff`  |
| 1348   | No file  | `d0a188773fff`  |
| 1346   | No file  | `d0a188773fff`  |
| 1341   | No file  | `d0a188773fff`  |
| 1340   | No file  | `d0a188773fff`  |
| 1338   | No file  | `d0a188773fff`  |
| 1335   | No file  | `d0a188773fff`  |
| 1333   | No file  | `d0a188773fff`  |
| 1329   | No file  | `d0a188773fff`  |
| 1327   | No file  | `d0a188773fff`  |
| 1324   | No file  | `d0a188773fff`  |
| 1321   | No file  | `d0a188773fff`  |
| 1319   | No file  | `d0a188773fff`  |
| 1318   | No file  | `d0a188773fff`  |
| 1316   | No file  | `d0a188773fff`  |
| 1313   | No file  | `d0a188773fff`  |
| 1311   | No file  | `d0a188773fff`  |
| 1309   | No file  | `d0a188773fff`  |
| 1304   | No file  | `d0a188773fff`  |
| 1292   | No file  | `d0a188773fff`  |
| 1286   | No file  | `d0a188773fff`  |
| 1280   | No file  | `d0a188773fff`  |
| 1276   | No file  | `d0a188773fff`  |
| 1267   | No file  | `d0a188773fff`  |
| 1261   | No file  | `d0a188773fff`  |
| 1256   | No file  | `d0a188773fff`  |
| 1250   | No file  | `d0a188773fff`  |
| 1246   | No file  | `d0a188773fff`  |
| 1239   | No file  | `d0a188773fff`  |
| 1230   | No file  | `d0a188773fff`  |
| 1226   | No file  | `d0a188773fff`  |
| 1220   | No file  | `d0a188773fff`  |
| 1217   | No file  | `d0a188773fff`  |
| 1211   | No file  | `d0a188773fff`  |
| 1210   | No file  | `d0a188773fff`  |
| 1208   | No file  | `d0a188773fff`  |
| 1203   | No file  | `d0a188773fff`  |
| 1197   | No file  | `d0a188773fff`  |
| 1194   | No file  | `d0a188773fff`  |
| 1192   | No file  | `d0a188773fff`  |
| 1187   | No file  | `d0a188773fff`  |
| 1183   | No file  | `d0a188773fff`  |
| 1177   | No file  | `d0a188773fff`  |
| 1173   | No file  | `d0a188773fff`  |
| 1167   | No file  | `d0a188773fff`  |
| 1164   | No file  | `d0a188773fff`  |
| 1156   | No file  | `d0a188773fff`  |
| 1149   | No file  | `d0a188773fff`  |
| 1144   | No file  | `d0a188773fff`  |
| 1137   | No file  | `d0a188773fff`  |
| 1132   | No file  | `d0a188773fff`  |
| 1127   | No file  | `d0a188773fff`  |
| 1122   | No file  | `d0a188773fff`  |
| 1118   | No file  | `d0a188773fff`  |
| 1114   | No file  | `d0a188773fff`  |
| 1109   | No file  | `d0a188773fff`  |
| 1102   | No file  | `d0a188773fff`  |
| 1096   | No file  | `d0a188773fff`  |
| 1088   | No file  | `d0a188773fff`  |
| 1081   | No file  | `d0a188773fff`  |
| 1076   | No file  | `d0a188773fff`  |
| 1069   | No file  | `d0a188773fff`  |
| 1064   | No file  | `d0a188773fff`  |
| 1058   | No file  | `d0a188773fff`  |
| 1051   | No file  | `d0a188773fff`  |
| 1044   | No file  | `d0a188773fff`  |
| 1036   | No file  | `d0a188773fff`  |
| 1026   | No file  | `d0a188773fff`  |
| 1016   | No file  | `d0a188773fff`  |
| 1009   | No file  | `d0a188773fff`  |
| 1005   | No file  | `d0a188773fff`  |
| 1000   | No file  | `d0a188773fff`  |
| 998    | No file  | `d0a188773fff`  |
| 990    | No file  | `d0a188773fff`  |
| 979    | No file  | `d0a188773fff`  |
| 972    | No file  | `d0a188773fff`  |
| 963    | No file  | `d0a188773fff`  |
| 955    | No file  | `d0a188773fff`  |
| 946    | No file  | `d0a188773fff`  |
| 938    | No file  | `d0a188773fff`  |
| 927    | No file  | `d0a188773fff`  |
| 911    | No file  | `d0a188773fff`  |
| 904    | No file  | `d0a188773fff`  |
| 899    | No file  | `d0a188773fff`  |
| 894    | No file  | `d0a188773fff`  |
| 885    | No file  | `d0a188773fff`  |
| 879    | No file  | `d0a188773fff`  |
| 872    | No file  | `d0a188773fff`  |
| 864    | No file  | `d0a188773fff`  |
| 855    | No file  | `d0a188773fff`  |
| 853    | No file  | `d0a188773fff`  |
| 845    | No file  | `d0a188773fff`  |
| 837    | No file  | `d0a188773fff`  |
| 829    | No file  | `d0a188773fff`  |
| 822    | No file  | `d0a188773fff`  |
| 814    | No file  | `d0a188773fff`  |
| 805    | No file  | `d0a188773fff`  |
| 794    | No file  | `d0a188773fff`  |
| 787    | No file  | `d0a188773fff`  |
| 780    | No file  | `d0a188773fff`  |
| 771    | No file  | `d0a188773fff`  |
| 760    | No file  | `d0a188773fff`  |
| 748    | No file  | `d0a188773fff`  |
| 741    | No file  | `d0a188773fff`  |
| 736    | No file  | `d0a188773fff`  |
| 731    | No file  | `d0a188773fff`  |
| 723    | No file  | `d0a188773fff`  |
| 711    | No file  | `d0a188773fff`  |
| 707    | No file  | `d0a188773fff`  |
| 697    | No file  | `d0a188773fff`  |
| 689    | No file  | `d0a188773fff`  |
| 683    | No file  | `d0a188773fff`  |
| 678    | No file  | `d0a188773fff`  |
| 670    | No file  | `d0a188773fff`  |
| 661    | No file  | `d0a188773fff`  |
| 656    | No file  | `d0a188773fff`  |
| 652    | No file  | `d0a188773fff`  |
| 643    | No file  | `d0a188773fff`  |
| 637    | No file  | `d0a188773fff`  |
| 630    | No file  | `d0a188773fff`  |
| 627    | No file  | `d0a188773fff`  |
| 621    | No file  | `d0a188773fff`  |
| 617    | No file  | `d0a188773fff`  |
| 615    | No file  | `d0a188773fff`  |
| 606    | No file  | `d0a188773fff`  |
| 599    | No file  | `d0a188773fff`  |
| 592    | No file  | `d0a188773fff`  |
| 586    | No file  | `d0a188773fff`  |
| 577    | No file  | `d0a188773fff`  |
| 569    | No file  | `d0a188773fff`  |
| 561    | No file  | `d0a188773fff`  |
| 554    | No file  | `d0a188773fff`  |
| 542    | No file  | `d0a188773fff`  |
| 532    | No file  | `d0a188773fff`  |
| 531    | No file  | `d0a188773fff`  |
| 526    | No file  | `d0a188773fff`  |
| 521    | No file  | `d0a188773fff`  |
| 517    | No file  | `d0a188773fff`  |
| 510    | No file  | `d0a188773fff`  |
| 508    | No file  | `d0a188773fff`  |
| 504    | No file  | `d0a188773fff`  |
| 497    | No file  | `d0a188773fff`  |
| 491    | No file  | `d0a188773fff`  |
| 485    | No file  | `d0a188773fff`  |
| 478    | No file  | `d0a188773fff`  |
| 472    | No file  | `d0a188773fff`  |
| 466    | No file  | `d0a188773fff`  |
| 457    | No file  | `d0a188773fff`  |
| 452    | No file  | `d0a188773fff`  |
| 449    | No file  | `d0a188773fff`  |
| 435    | No file  | `d0a188773fff`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Manor names, LOC type 6 keyed by `character_id`       |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset              | Type                  | Field        | Notes                                          |
| ------------------- | --------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]               | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                   | count        | Number of rows; 9 on client 3458               |
| `+0x08`             | Manor Part Row[count] | rows         | See Manor Part Row                             |
| `rows+0x00`         | String Table          | string_table | See String Table                               |
| `string_table+0x00` | u32                   | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                   | zero         | Always 0                                       |

Rows are sorted by `character_id`, then `part_index`.

### Manor Part Row (12 bytes)

| Offset  | Type | Field           | Notes                                                                 |
| ------- | ---- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_id    | The manor building's key in `characterstatic.dbss` (its house record) |
| `+0x02` | u8   | unknown_02      | Always `1`                                                            |
| `+0x03` | u8   | part_index      | Sub-mesh part of the manor, from 0                                    |
| `+0x04` | u32  | icon_ref        | String table index of the part icon, relative to `ui_texture/`        |
| `+0x08` | u32  | unknown_str_ref | String table index; always `1`, the empty string                      |

### String Table (variable: 4 bytes + strings)

10 strings on client 3458: the nine icon paths and, at index 1, an empty
string that every `unknown_str_ref` points at.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Layout 1

On client 1784 each row starts with a u32 `unknown_00` and every later field
sits 4 bytes later. Only the Manor Part Row differs from Layout 2. Field
names keep Layout 2's offsets, so `unknown_02` sits at `+0x06` here.

### Manor Part Row (16 bytes)

| Offset  | Type | Field           | Notes                                                                       |
| ------- | ---- | --------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00      | 1, 2, 3, 4, 5, 5 in row order on client 1784                                |
| `+0x04` | u16  | character_id    |                                                                             |
| `+0x06` | u8   | unknown_02      | Always `1` on client 1784                                                   |
| `+0x07` | u8   | part_index      |                                                                             |
| `+0x08` | u32  | icon_ref        |                                                                             |
| `+0x0C` | u32  | unknown_str_ref | String table index; on client 1784 a material name such as `Mansion_STR_border_01`, or the empty string |

## Notes

- The installation mode list (`window/housing/panel_house_installationmode_list_all_1`)
  shows these icons on its "BaseMaterial" tab when the visited house is a
  manor: it reads the manor from `ToClient_VisitHouseHoldCharacterKey`, the
  number of parts from `ToClient_GetSubMeshCount`, and each part slot's icon
  from `ToClient_getPartIconPath(characterKey, partIndex)`.
- Client 3458 lists four manors: Blue Maned Lion's Manor (3815, parts 0 to 2,
  `Mantion_In1` to `Mantion_In3`) and the three Land of the Morning Light
  houses Shimhyangje (3842), Solbaram Neowa House (3844) and Hyeollokdang
  (3848), each with a wall and a floor picture. The part order is not fixed
  by kind: Shimhyangje's part 0 is its wall, the other two start with the
  floor. Blue Maned Lion's Manor highlights one wing per picture instead.
- All nine icons exist once resolved under `ui_texture/` and lowercased.
- The app indexes the part icons (`IndexKind.MANOR_PART_ICON`, read through
  `IconKind.MANOR_PART`) by `manor_part_key()`, `part_index << 16 |
  character_id`. They are blueprints of a part, so they never replace the
  manor's own `characterstatic.dbss` icon.

## Open Questions

### What do `unknown_02` and `unknown_str_ref` hold?

`unknown_02` is `1` and `unknown_str_ref` points at the empty string in all
nine rows. The string may be a part name the client never fills; with one
value each on the current client nothing tells their meaning apart.
