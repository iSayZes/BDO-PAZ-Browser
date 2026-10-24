# `edanacastleinfostaicstatusmanager.bss` Format

## Purpose

The world map marks of the Edania castles: one row per castle with the
texture of its territory mark, a world map position and the castle's node.
The rows follow the `__eEdaniaRegion` order (Aetherion to Voidekaia). No
client Lua calls read this file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3483    | `edanacastleinfostaicstatusmanager.bss` | 748   | 10 Row  | 16        |

| Layout | File                                    | Known          | Unknown    |
| ------ | --------------------------------------- | -------------- | ---------- |
| 1      | `edanacastleinfostaicstatusmanager.bss` | 748 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `dda3494db7bc`  |
| 3482   | Layout 1 | `dda3494db7bc`  |
| 3474   | Layout 1 | `dda3494db7bc`  |
| 3473   | Layout 1 | `dda3494db7bc`  |
| 3464   | Layout 1 | `dda3494db7bc`  |
| 3458   | Layout 1 | `dda3494db7bc`  |
| 3454   | Layout 1 | `dda3494db7bc`  |
| 3444   | Layout 1 | `dda3494db7bc`  |
| 3435   | Layout 1 | `dda3494db7bc`  |
| 3426   | Layout 1 | `dda3494db7bc`  |
| 3418   | Layout 1 | `dda3494db7bc`  |
| 3412   | Layout 1 | `dda3494db7bc`  |
| 3402   | Layout 1 | `dda3494db7bc`  |
| 3396   | Layout 1 | `dda3494db7bc`  |
| 3387   | Layout 1 | `dda3494db7bc`  |
| 3381   | Layout 1 | `dda3494db7bc`  |
| 3373   | Layout 1 | `dda3494db7bc`  |
| 3364   | Layout 1 | `dda3494db7bc`  |
| 3356   | Layout 1 | `dda3494db7bc`  |
| 3349   | Layout 1 | `dda3494db7bc`  |
| 3342   | Layout 1 | `dda3494db7bc`  |
| 3335   | Layout 1 | `dda3494db7bc`  |
| 3326   | Layout 1 | `dda3494db7bc`  |
| 3321   | Layout 1 | `dda3494db7bc`  |
| 3314   | Layout 1 | `dda3494db7bc`  |
| 3303   | Layout 1 | `dda3494db7bc`  |
| 3302   | Layout 1 | `dda3494db7bc`  |
| 3293   | Layout 1 | `dda3494db7bc`  |
| 3283   | Layout 1 | `dda3494db7bc`  |
| 3275   | Layout 1 | `dda3494db7bc`  |
| 3267   | Layout 1 | `dda3494db7bc`  |
| 3258   | Layout 1 | `dda3494db7bc`  |
| 3251   | Layout 1 | `dda3494db7bc`  |
| 3242   | Layout 1 | `dda3494db7bc`  |
| 3235   | Layout 1 | `dda3494db7bc`  |
| 3229   | Layout 1 | `dda3494db7bc`  |
| 3212   | Layout 1 | `dda3494db7bc`  |
| 3203   | Layout 1 | `dda3494db7bc`  |
| 3193   | Layout 1 | `dda3494db7bc`  |
| 3186   | Layout 1 | `dda3494db7bc`  |
| 3177   | Layout 1 | `dda3494db7bc`  |
| 3169   | Layout 1 | `dda3494db7bc`  |
| 3158   | Layout 1 | `dda3494db7bc`  |
| 3151   | Layout 1 | `dda3494db7bc`  |
| 3144   | Layout 1 | `dda3494db7bc`  |
| 3133   | Layout 1 | `dda3494db7bc`  |
| 3125   | Layout 1 | `dda3494db7bc`  |
| 3118   | Layout 1 | `dda3494db7bc`  |
| 3111   | Layout 1 | `dda3494db7bc`  |
| 3103   | Layout 1 | `dda3494db7bc`  |
| 3095   | Layout 1 | `dda3494db7bc`  |
| 3086   | Layout 1 | `dda3494db7bc`  |
| 3072   | Layout 1 | `dda3494db7bc`  |
| 3062   | Layout 1 | `dda3494db7bc`  |
| 3052   | Layout 1 | `dda3494db7bc`  |
| 3045   | Layout 1 | `dda3494db7bc`  |
| 3037   | Layout 1 | `dda3494db7bc`  |
| 3030   | Layout 1 | `dda3494db7bc`  |
| 3021   | Layout 1 | `dda3494db7bc`  |
| 3012   | Layout 1 | `dda3494db7bc`  |
| 3002   | Layout 1 | `dda3494db7bc`  |
| 2995   | No file  | `dda3494db7bc`  |
| 2987   | No file  | `dda3494db7bc`  |
| 2978   | No file  | `dda3494db7bc`  |
| 2970   | No file  | `dda3494db7bc`  |
| 2959   | No file  | `dda3494db7bc`  |
| 2951   | No file  | `dda3494db7bc`  |
| 2942   | No file  | `dda3494db7bc`  |
| 2935   | No file  | `dda3494db7bc`  |
| 2932   | No file  | `dda3494db7bc`  |
| 2923   | No file  | `dda3494db7bc`  |
| 2919   | No file  | `dda3494db7bc`  |
| 2907   | No file  | `dda3494db7bc`  |
| 2900   | No file  | `dda3494db7bc`  |
| 2891   | No file  | `dda3494db7bc`  |
| 2882   | No file  | `dda3494db7bc`  |
| 2872   | No file  | `dda3494db7bc`  |
| 2863   | No file  | `dda3494db7bc`  |
| 2855   | No file  | `dda3494db7bc`  |
| 2849   | No file  | `dda3494db7bc`  |
| 2844   | No file  | `dda3494db7bc`  |
| 2834   | No file  | `dda3494db7bc`  |
| 2825   | No file  | `dda3494db7bc`  |
| 2819   | No file  | `dda3494db7bc`  |
| 2811   | No file  | `dda3494db7bc`  |
| 2803   | No file  | `dda3494db7bc`  |
| 2794   | No file  | `dda3494db7bc`  |
| 2783   | No file  | `dda3494db7bc`  |
| 2774   | No file  | `dda3494db7bc`  |
| 2765   | No file  | `dda3494db7bc`  |
| 2756   | No file  | `dda3494db7bc`  |
| 2750   | No file  | `dda3494db7bc`  |
| 2743   | No file  | `dda3494db7bc`  |
| 2736   | No file  | `dda3494db7bc`  |
| 2726   | No file  | `dda3494db7bc`  |
| 2717   | No file  | `dda3494db7bc`  |
| 2709   | No file  | `dda3494db7bc`  |
| 2703   | No file  | `dda3494db7bc`  |
| 2695   | No file  | `dda3494db7bc`  |
| 2684   | No file  | `dda3494db7bc`  |
| 2672   | No file  | `dda3494db7bc`  |
| 2665   | No file  | `dda3494db7bc`  |
| 2657   | No file  | `dda3494db7bc`  |
| 2649   | No file  | `dda3494db7bc`  |
| 2644   | No file  | `dda3494db7bc`  |
| 2637   | No file  | `dda3494db7bc`  |
| 2629   | No file  | `dda3494db7bc`  |
| 2619   | No file  | `dda3494db7bc`  |
| 2612   | No file  | `dda3494db7bc`  |
| 2606   | No file  | `dda3494db7bc`  |
| 2602   | No file  | `dda3494db7bc`  |
| 2601   | No file  | `dda3494db7bc`  |
| 2592   | No file  | `dda3494db7bc`  |
| 2583   | No file  | `dda3494db7bc`  |
| 2575   | No file  | `dda3494db7bc`  |
| 2567   | No file  | `dda3494db7bc`  |
| 2560   | No file  | `dda3494db7bc`  |
| 2553   | No file  | `dda3494db7bc`  |
| 2545   | No file  | `dda3494db7bc`  |
| 2538   | No file  | `dda3494db7bc`  |
| 2529   | No file  | `dda3494db7bc`  |
| 2519   | No file  | `dda3494db7bc`  |
| 2513   | No file  | `dda3494db7bc`  |
| 2510   | No file  | `dda3494db7bc`  |
| 2507   | No file  | `dda3494db7bc`  |
| 2503   | No file  | `dda3494db7bc`  |
| 2498   | No file  | `dda3494db7bc`  |
| 2492   | No file  | `dda3494db7bc`  |
| 2487   | No file  | `dda3494db7bc`  |
| 2480   | No file  | `dda3494db7bc`  |
| 2474   | No file  | `dda3494db7bc`  |
| 2468   | No file  | `dda3494db7bc`  |
| 2460   | No file  | `dda3494db7bc`  |
| 2453   | No file  | `dda3494db7bc`  |
| 2444   | No file  | `dda3494db7bc`  |
| 2438   | No file  | `dda3494db7bc`  |
| 2434   | No file  | `dda3494db7bc`  |
| 2429   | No file  | `dda3494db7bc`  |
| 2421   | No file  | `dda3494db7bc`  |
| 2414   | No file  | `dda3494db7bc`  |
| 2407   | No file  | `dda3494db7bc`  |
| 2401   | No file  | `dda3494db7bc`  |
| 2397   | No file  | `dda3494db7bc`  |
| 2393   | No file  | `dda3494db7bc`  |
| 2384   | No file  | `dda3494db7bc`  |
| 2378   | No file  | `dda3494db7bc`  |
| 2372   | No file  | `dda3494db7bc`  |
| 2358   | No file  | `dda3494db7bc`  |
| 2352   | No file  | `dda3494db7bc`  |
| 2347   | No file  | `dda3494db7bc`  |
| 2343   | No file  | `dda3494db7bc`  |
| 2335   | No file  | `dda3494db7bc`  |
| 2327   | No file  | `dda3494db7bc`  |
| 2324   | No file  | `dda3494db7bc`  |
| 2319   | No file  | `dda3494db7bc`  |
| 2313   | No file  | `dda3494db7bc`  |
| 2308   | No file  | `dda3494db7bc`  |
| 2302   | No file  | `dda3494db7bc`  |
| 2295   | No file  | `dda3494db7bc`  |
| 2290   | No file  | `dda3494db7bc`  |
| 2284   | No file  | `dda3494db7bc`  |
| 2276   | No file  | `dda3494db7bc`  |
| 2269   | No file  | `dda3494db7bc`  |
| 2259   | No file  | `dda3494db7bc`  |
| 2250   | No file  | `dda3494db7bc`  |
| 2243   | No file  | `dda3494db7bc`  |
| 2235   | No file  | `dda3494db7bc`  |
| 2229   | No file  | `dda3494db7bc`  |
| 2224   | No file  | `dda3494db7bc`  |
| 2218   | No file  | `dda3494db7bc`  |
| 2215   | No file  | `dda3494db7bc`  |
| 2207   | No file  | `dda3494db7bc`  |
| 2203   | No file  | `dda3494db7bc`  |
| 2196   | No file  | `dda3494db7bc`  |
| 2192   | No file  | `dda3494db7bc`  |
| 2189   | No file  | `dda3494db7bc`  |
| 2183   | No file  | `dda3494db7bc`  |
| 2179   | No file  | `dda3494db7bc`  |
| 2171   | No file  | `dda3494db7bc`  |
| 2163   | No file  | `dda3494db7bc`  |
| 2156   | No file  | `dda3494db7bc`  |
| 2151   | No file  | `dda3494db7bc`  |
| 2147   | No file  | `dda3494db7bc`  |
| 2142   | No file  | `dda3494db7bc`  |
| 2138   | No file  | `dda3494db7bc`  |
| 2134   | No file  | `dda3494db7bc`  |
| 2130   | No file  | `dda3494db7bc`  |
| 2122   | No file  | `dda3494db7bc`  |
| 2107   | No file  | `dda3494db7bc`  |
| 2098   | No file  | `dda3494db7bc`  |
| 2089   | No file  | `dda3494db7bc`  |
| 2081   | No file  | `dda3494db7bc`  |
| 2073   | No file  | `dda3494db7bc`  |
| 2067   | No file  | `dda3494db7bc`  |
| 2063   | No file  | `dda3494db7bc`  |
| 2059   | No file  | `dda3494db7bc`  |
| 2052   | No file  | `dda3494db7bc`  |
| 2044   | No file  | `dda3494db7bc`  |
| 2039   | No file  | `dda3494db7bc`  |
| 2032   | No file  | `dda3494db7bc`  |
| 2025   | No file  | `dda3494db7bc`  |
| 2011   | No file  | `dda3494db7bc`  |
| 2005   | No file  | `dda3494db7bc`  |
| 2000   | No file  | `dda3494db7bc`  |
| 1996   | No file  | `dda3494db7bc`  |
| 1991   | No file  | `dda3494db7bc`  |
| 1985   | No file  | `dda3494db7bc`  |
| 1980   | No file  | `dda3494db7bc`  |
| 1969   | No file  | `dda3494db7bc`  |
| 1964   | No file  | `dda3494db7bc`  |
| 1958   | No file  | `dda3494db7bc`  |
| 1950   | No file  | `dda3494db7bc`  |
| 1945   | No file  | `dda3494db7bc`  |
| 1937   | No file  | `dda3494db7bc`  |
| 1933   | No file  | `dda3494db7bc`  |
| 1927   | No file  | `dda3494db7bc`  |
| 1921   | No file  | `dda3494db7bc`  |
| 1914   | No file  | `dda3494db7bc`  |
| 1908   | No file  | `dda3494db7bc`  |
| 1897   | No file  | `dda3494db7bc`  |
| 1892   | No file  | `dda3494db7bc`  |
| 1886   | No file  | `dda3494db7bc`  |
| 1881   | No file  | `dda3494db7bc`  |
| 1871   | No file  | `dda3494db7bc`  |
| 1866   | No file  | `dda3494db7bc`  |
| 1862   | No file  | `dda3494db7bc`  |
| 1854   | No file  | `dda3494db7bc`  |
| 1846   | No file  | `dda3494db7bc`  |
| 1838   | No file  | `dda3494db7bc`  |
| 1832   | No file  | `dda3494db7bc`  |
| 1826   | No file  | `dda3494db7bc`  |
| 1822   | No file  | `dda3494db7bc`  |
| 1818   | No file  | `dda3494db7bc`  |
| 1804   | No file  | `dda3494db7bc`  |
| 1794   | No file  | `dda3494db7bc`  |
| 1790   | No file  | `dda3494db7bc`  |
| 1784   | No file  | `dda3494db7bc`  |
| 1774   | No file  | `dda3494db7bc`  |
| 1771   | No file  | `dda3494db7bc`  |
| 1762   | No file  | `dda3494db7bc`  |
| 1759   | No file  | `dda3494db7bc`  |
| 1754   | No file  | `dda3494db7bc`  |
| 1749   | No file  | `dda3494db7bc`  |
| 1743   | No file  | `dda3494db7bc`  |
| 1737   | No file  | `dda3494db7bc`  |
| 1731   | No file  | `dda3494db7bc`  |
| 1725   | No file  | `dda3494db7bc`  |
| 1717   | No file  | `dda3494db7bc`  |
| 1710   | No file  | `dda3494db7bc`  |
| 1704   | No file  | `dda3494db7bc`  |
| 1698   | No file  | `dda3494db7bc`  |
| 1690   | No file  | `dda3494db7bc`  |
| 1685   | No file  | `dda3494db7bc`  |
| 1680   | No file  | `dda3494db7bc`  |
| 1674   | No file  | `dda3494db7bc`  |
| 1668   | No file  | `dda3494db7bc`  |
| 1659   | No file  | `dda3494db7bc`  |
| 1649   | No file  | `dda3494db7bc`  |
| 1642   | No file  | `dda3494db7bc`  |
| 1636   | No file  | `dda3494db7bc`  |
| 1628   | No file  | `dda3494db7bc`  |
| 1622   | No file  | `dda3494db7bc`  |
| 1614   | No file  | `dda3494db7bc`  |
| 1608   | No file  | `dda3494db7bc`  |
| 1602   | No file  | `dda3494db7bc`  |
| 1598   | No file  | `dda3494db7bc`  |
| 1594   | No file  | `dda3494db7bc`  |
| 1590   | No file  | `dda3494db7bc`  |
| 1587   | No file  | `dda3494db7bc`  |
| 1584   | No file  | `dda3494db7bc`  |
| 1579   | No file  | `dda3494db7bc`  |
| 1572   | No file  | `dda3494db7bc`  |
| 1565   | No file  | `dda3494db7bc`  |
| 1559   | No file  | `dda3494db7bc`  |
| 1554   | No file  | `dda3494db7bc`  |
| 1547   | No file  | `dda3494db7bc`  |
| 1537   | No file  | `dda3494db7bc`  |
| 1529   | No file  | `dda3494db7bc`  |
| 1524   | No file  | `dda3494db7bc`  |
| 1519   | No file  | `dda3494db7bc`  |
| 1509   | No file  | `dda3494db7bc`  |
| 1506   | No file  | `dda3494db7bc`  |
| 1504   | No file  | `dda3494db7bc`  |
| 1500   | No file  | `dda3494db7bc`  |
| 1493   | No file  | `dda3494db7bc`  |
| 1489   | No file  | `dda3494db7bc`  |
| 1485   | No file  | `dda3494db7bc`  |
| 1481   | No file  | `dda3494db7bc`  |
| 1474   | No file  | `dda3494db7bc`  |
| 1466   | No file  | `dda3494db7bc`  |
| 1462   | No file  | `dda3494db7bc`  |
| 1459   | No file  | `dda3494db7bc`  |
| 1453   | No file  | `dda3494db7bc`  |
| 1450   | No file  | `dda3494db7bc`  |
| 1445   | No file  | `dda3494db7bc`  |
| 1439   | No file  | `dda3494db7bc`  |
| 1433   | No file  | `dda3494db7bc`  |
| 1430   | No file  | `dda3494db7bc`  |
| 1426   | No file  | `dda3494db7bc`  |
| 1421   | No file  | `dda3494db7bc`  |
| 1417   | No file  | `dda3494db7bc`  |
| 1416   | No file  | `dda3494db7bc`  |
| 1409   | No file  | `dda3494db7bc`  |
| 1405   | No file  | `dda3494db7bc`  |
| 1401   | No file  | `dda3494db7bc`  |
| 1396   | No file  | `dda3494db7bc`  |
| 1391   | No file  | `dda3494db7bc`  |
| 1390   | No file  | `dda3494db7bc`  |
| 1386   | No file  | `dda3494db7bc`  |
| 1381   | No file  | `dda3494db7bc`  |
| 1379   | No file  | `dda3494db7bc`  |
| 1372   | No file  | `dda3494db7bc`  |
| 1366   | No file  | `dda3494db7bc`  |
| 1364   | No file  | `dda3494db7bc`  |
| 1363   | No file  | `dda3494db7bc`  |
| 1360   | No file  | `dda3494db7bc`  |
| 1358   | No file  | `dda3494db7bc`  |
| 1355   | No file  | `dda3494db7bc`  |
| 1351   | No file  | `dda3494db7bc`  |
| 1348   | No file  | `dda3494db7bc`  |
| 1346   | No file  | `dda3494db7bc`  |
| 1341   | No file  | `dda3494db7bc`  |
| 1340   | No file  | `dda3494db7bc`  |
| 1338   | No file  | `dda3494db7bc`  |
| 1335   | No file  | `dda3494db7bc`  |
| 1333   | No file  | `dda3494db7bc`  |
| 1329   | No file  | `dda3494db7bc`  |
| 1327   | No file  | `dda3494db7bc`  |
| 1324   | No file  | `dda3494db7bc`  |
| 1321   | No file  | `dda3494db7bc`  |
| 1319   | No file  | `dda3494db7bc`  |
| 1318   | No file  | `dda3494db7bc`  |
| 1316   | No file  | `dda3494db7bc`  |
| 1313   | No file  | `dda3494db7bc`  |
| 1311   | No file  | `dda3494db7bc`  |
| 1309   | No file  | `dda3494db7bc`  |
| 1304   | No file  | `dda3494db7bc`  |
| 1292   | No file  | `dda3494db7bc`  |
| 1286   | No file  | `dda3494db7bc`  |
| 1280   | No file  | `dda3494db7bc`  |
| 1276   | No file  | `dda3494db7bc`  |
| 1267   | No file  | `dda3494db7bc`  |
| 1261   | No file  | `dda3494db7bc`  |
| 1256   | No file  | `dda3494db7bc`  |
| 1250   | No file  | `dda3494db7bc`  |
| 1246   | No file  | `dda3494db7bc`  |
| 1239   | No file  | `dda3494db7bc`  |
| 1230   | No file  | `dda3494db7bc`  |
| 1226   | No file  | `dda3494db7bc`  |
| 1220   | No file  | `dda3494db7bc`  |
| 1217   | No file  | `dda3494db7bc`  |
| 1211   | No file  | `dda3494db7bc`  |
| 1210   | No file  | `dda3494db7bc`  |
| 1208   | No file  | `dda3494db7bc`  |
| 1203   | No file  | `dda3494db7bc`  |
| 1197   | No file  | `dda3494db7bc`  |
| 1194   | No file  | `dda3494db7bc`  |
| 1192   | No file  | `dda3494db7bc`  |
| 1187   | No file  | `dda3494db7bc`  |
| 1183   | No file  | `dda3494db7bc`  |
| 1177   | No file  | `dda3494db7bc`  |
| 1173   | No file  | `dda3494db7bc`  |
| 1167   | No file  | `dda3494db7bc`  |
| 1164   | No file  | `dda3494db7bc`  |
| 1156   | No file  | `dda3494db7bc`  |
| 1149   | No file  | `dda3494db7bc`  |
| 1144   | No file  | `dda3494db7bc`  |
| 1137   | No file  | `dda3494db7bc`  |
| 1132   | No file  | `dda3494db7bc`  |
| 1127   | No file  | `dda3494db7bc`  |
| 1122   | No file  | `dda3494db7bc`  |
| 1118   | No file  | `dda3494db7bc`  |
| 1114   | No file  | `dda3494db7bc`  |
| 1109   | No file  | `dda3494db7bc`  |
| 1102   | No file  | `dda3494db7bc`  |
| 1096   | No file  | `dda3494db7bc`  |
| 1088   | No file  | `dda3494db7bc`  |
| 1081   | No file  | `dda3494db7bc`  |
| 1076   | No file  | `dda3494db7bc`  |
| 1069   | No file  | `dda3494db7bc`  |
| 1064   | No file  | `dda3494db7bc`  |
| 1058   | No file  | `dda3494db7bc`  |
| 1051   | No file  | `dda3494db7bc`  |
| 1044   | No file  | `dda3494db7bc`  |
| 1036   | No file  | `dda3494db7bc`  |
| 1026   | No file  | `dda3494db7bc`  |
| 1016   | No file  | `dda3494db7bc`  |
| 1009   | No file  | `dda3494db7bc`  |
| 1005   | No file  | `dda3494db7bc`  |
| 1000   | No file  | `dda3494db7bc`  |
| 998    | No file  | `dda3494db7bc`  |
| 990    | No file  | `dda3494db7bc`  |
| 979    | No file  | `dda3494db7bc`  |
| 972    | No file  | `dda3494db7bc`  |
| 963    | No file  | `dda3494db7bc`  |
| 955    | No file  | `dda3494db7bc`  |
| 946    | No file  | `dda3494db7bc`  |
| 938    | No file  | `dda3494db7bc`  |
| 927    | No file  | `dda3494db7bc`  |
| 911    | No file  | `dda3494db7bc`  |
| 904    | No file  | `dda3494db7bc`  |
| 899    | No file  | `dda3494db7bc`  |
| 894    | No file  | `dda3494db7bc`  |
| 885    | No file  | `dda3494db7bc`  |
| 879    | No file  | `dda3494db7bc`  |
| 872    | No file  | `dda3494db7bc`  |
| 864    | No file  | `dda3494db7bc`  |
| 855    | No file  | `dda3494db7bc`  |
| 853    | No file  | `dda3494db7bc`  |
| 845    | No file  | `dda3494db7bc`  |
| 837    | No file  | `dda3494db7bc`  |
| 829    | No file  | `dda3494db7bc`  |
| 822    | No file  | `dda3494db7bc`  |
| 814    | No file  | `dda3494db7bc`  |
| 805    | No file  | `dda3494db7bc`  |
| 794    | No file  | `dda3494db7bc`  |
| 787    | No file  | `dda3494db7bc`  |
| 780    | No file  | `dda3494db7bc`  |
| 771    | No file  | `dda3494db7bc`  |
| 760    | No file  | `dda3494db7bc`  |
| 748    | No file  | `dda3494db7bc`  |
| 741    | No file  | `dda3494db7bc`  |
| 736    | No file  | `dda3494db7bc`  |
| 731    | No file  | `dda3494db7bc`  |
| 723    | No file  | `dda3494db7bc`  |
| 711    | No file  | `dda3494db7bc`  |
| 707    | No file  | `dda3494db7bc`  |
| 697    | No file  | `dda3494db7bc`  |
| 689    | No file  | `dda3494db7bc`  |
| 683    | No file  | `dda3494db7bc`  |
| 678    | No file  | `dda3494db7bc`  |
| 670    | No file  | `dda3494db7bc`  |
| 661    | No file  | `dda3494db7bc`  |
| 656    | No file  | `dda3494db7bc`  |
| 652    | No file  | `dda3494db7bc`  |
| 643    | No file  | `dda3494db7bc`  |
| 637    | No file  | `dda3494db7bc`  |
| 630    | No file  | `dda3494db7bc`  |
| 627    | No file  | `dda3494db7bc`  |
| 621    | No file  | `dda3494db7bc`  |
| 617    | No file  | `dda3494db7bc`  |
| 615    | No file  | `dda3494db7bc`  |
| 606    | No file  | `dda3494db7bc`  |
| 599    | No file  | `dda3494db7bc`  |
| 592    | No file  | `dda3494db7bc`  |
| 586    | No file  | `dda3494db7bc`  |
| 577    | No file  | `dda3494db7bc`  |
| 569    | No file  | `dda3494db7bc`  |
| 561    | No file  | `dda3494db7bc`  |
| 554    | No file  | `dda3494db7bc`  |
| 542    | No file  | `dda3494db7bc`  |
| 532    | No file  | `dda3494db7bc`  |
| 531    | No file  | `dda3494db7bc`  |
| 526    | No file  | `dda3494db7bc`  |
| 521    | No file  | `dda3494db7bc`  |
| 517    | No file  | `dda3494db7bc`  |
| 510    | No file  | `dda3494db7bc`  |
| 508    | No file  | `dda3494db7bc`  |
| 504    | No file  | `dda3494db7bc`  |
| 497    | No file  | `dda3494db7bc`  |
| 491    | No file  | `dda3494db7bc`  |
| 485    | No file  | `dda3494db7bc`  |
| 478    | No file  | `dda3494db7bc`  |
| 472    | No file  | `dda3494db7bc`  |
| 466    | No file  | `dda3494db7bc`  |
| 457    | No file  | `dda3494db7bc`  |
| 452    | No file  | `dda3494db7bc`  |
| 449    | No file  | `dda3494db7bc`  |
| 435    | No file  | `dda3494db7bc`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                      |
| --------------------- | -------- | ----------------------------------------- |
| `languagedata_en.loc` | Optional | Node names, LOC type 29                   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset      | Type               | Field        | Notes                                         |
| ----------- | ------------------ | ------------ | --------------------------------------------- |
| `+0x00`     | char[4]            | magic        | ASCII `PABR`                                  |
| `+0x04`     | Row[..table_start] | rows         | See Row; no row count                         |
| `rows+0x00` | String Table       | string_table | See String Table                              |
| `EOF-0x08`  | u32                | table_start  | Offset of the string table, where `rows` ends |
| `EOF-0x04`  | u32                | zero         | Always `0`                                    |

### Row (16 bytes)

| Offset  | Type | Field            | Notes                                                                                   |
| ------- | ---- | ---------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | mark_texture_ref | String-table index of the mark texture name; equals the row number on every client checked |
| `+0x04` | f32  | x                | World X of the mark                                                                     |
| `+0x08` | f32  | z                | World Z of the mark                                                                     |
| `+0x0C` | u32  | node_key         | The castle's node; `2002` Aetherion Castle to `2112` Event Horizon                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                      |
| ------- | ------------------ | ------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; one per row                                             |
| `+0x04` | pstr[string_count] | strings      | UTF-16 texture names, `territorymark_Jordine_large` to `territorymark_Hadum_large` |

## Castles

The rows on client 3482, with the node's LOC name. Each texture is a
`ui_texture/renewal/etc/wordmap/<name>.dds` file, named after the castle's
god; the same gods name the faction icons the client draws for each
`__eEdaniaRegion` value (`Combine_Etc_EdaniaIcon_Jordain_Normal` for
Aetherion, see [`edaniaregioninfo.bss`](edaniaregioninfo_bss.md#notes)).

| Row | `mark_texture`                   | `node_key` | Node                  |
| --- | -------------------------------- | ---------- | --------------------- |
| 0   | `territorymark_Jordine_large`    | `2002`     | Aetherion Castle      |
| 1   | `territorymark_Rusalka_large`    | `2006`     | Nymphamaré Castle     |
| 2   | `territorymark_Enslar_large`     | `2003`     | Orbita Castle         |
| 3   | `territorymark_Cartian_large`    | `2005`     | Tenebraum Castle      |
| 4   | `territorymark_Caphras_large`    | `2004`     | Zephyros Castle       |
| 5   | `territorymark_Agris_large`      | `2111`     | Aphrodon Temple       |
| 6   | `territorymark_Marctanan_large`  | `2109`     | Hermesia Inner Castle |
| 7   | `territorymark_Alien_large`      | `2108`     | Magaia Temple         |
| 8   | `territorymark_Aal_large`        | `2110`     | Aresion Temple        |
| 9   | `territorymark_Hadum_large`      | `2112`     | Event Horizon         |

## Field Names

Edania is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers this file, and no Lua call reads
it. The names come from the values:

- `mark_texture_ref` indexes the string table, which holds one texture
  name per row in row order. Each name is a world map territory mark
  (`territorymark_<god>_large.dds`, next to `territorymark_edania_large.dds`
  in `ui_texture/renewal/etc/wordmap/`). The official Throne of Edana
  page of the NA/EU game wiki (wikiNo 457) pairs each castle with the same
  god: "Aetherion Castle (Jordine)", "Nymphamaré Castle (Rusalka)" through
  "Zephyros Castle (Caphras)".
- `node_key` is a node key: each value has a LOC type 29 node name, the
  castle of the same row. The node order matches the `__eEdaniaRegion`
  order of [`edaniaregioninfo.bss`](edaniaregioninfo_bss.md#enum-values).
- `x` and `z` lie 3,700 to 20,400 units from the castle node's own world
  position on client 3482 (Aetherion: `559141, 573692` against the node's
  `566128, 570954`), so they read as world X and Z.

## Notes

- Clients 3002 and 3251 hold the first five rows (Aetherion to Zephyros),
  client 3474 all ten. The file is not in the archives of client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/edania_tables.py`: the node key and name, the mark
  texture and the position.
