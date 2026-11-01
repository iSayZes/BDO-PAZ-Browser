# `recommendationquest.bss` Format

## Purpose

Defines the recommended-quest list: quest IDs grouped under recommendations such as `[ADV Support] Inventory Expansion!` or `[Life 101] The Adventurer That Does It All`, each group named by LOC type 28, with a condition line per quest. 122 groups and 1,291 quest references on client 3458. All text sits in a string table at the end of the file (Korean group names, Korean condition lines, scripts).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes   | Records                              | Row bytes |
| ------ | -------------- | ------------------------- | ------- | ------------------------------------ | --------- |
| 1      | 1304 and later | `recommendationquest.bss` | 201,851 | 1,289 Quest Reference Row, 122 Group | 17        |

| Layout | File                      | Known             | Unknown      |
| ------ | ------------------------- | ----------------- | ------------ |
| 1      | `recommendationquest.bss` | 201,363 B (99.8%) | 488 B (0.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `d32cae352241`  |
| 3482   | Layout 1             | `d32cae352241`  |
| 3474   | Layout 1             | `d32cae352241`  |
| 3473   | Layout 1             | `d32cae352241`  |
| 3464   | Layout 1             | `d32cae352241`  |
| 3458   | Layout 1             | `d32cae352241`  |
| 3454   | Layout 1             | `d32cae352241`  |
| 3444   | Layout 1             | `d32cae352241`  |
| 3435   | Layout 1             | `d32cae352241`  |
| 3426   | Layout 1             | `d32cae352241`  |
| 3418   | Layout 1             | `d32cae352241`  |
| 3412   | Layout 1             | `d32cae352241`  |
| 3402   | Layout 1             | `d32cae352241`  |
| 3396   | Layout 1             | `d32cae352241`  |
| 3387   | Layout 1             | `d32cae352241`  |
| 3381   | Layout 1             | `d32cae352241`  |
| 3373   | Layout 1             | `d32cae352241`  |
| 3364   | Layout 1             | `d32cae352241`  |
| 3356   | Layout 1             | `d32cae352241`  |
| 3349   | Layout 1             | `d32cae352241`  |
| 3342   | Layout 1             | `d32cae352241`  |
| 3335   | Layout 1             | `d32cae352241`  |
| 3326   | Layout 1             | `d32cae352241`  |
| 3321   | Layout 1             | `d32cae352241`  |
| 3314   | Layout 1             | `d32cae352241`  |
| 3303   | Layout 1             | `d32cae352241`  |
| 3302   | Layout 1             | `d32cae352241`  |
| 3293   | Layout 1             | `d32cae352241`  |
| 3283   | Layout 1             | `d32cae352241`  |
| 3275   | Layout 1             | `d32cae352241`  |
| 3267   | Layout 1             | `d32cae352241`  |
| 3258   | Layout 1             | `d32cae352241`  |
| 3251   | Layout 1             | `d32cae352241`  |
| 3242   | Layout 1             | `d32cae352241`  |
| 3235   | Layout 1             | `d32cae352241`  |
| 3229   | Layout 1             | `d32cae352241`  |
| 3212   | Layout 1             | `d32cae352241`  |
| 3203   | Layout 1             | `d32cae352241`  |
| 3193   | Layout 1             | `d32cae352241`  |
| 3186   | Layout 1             | `d32cae352241`  |
| 3177   | Layout 1             | `d32cae352241`  |
| 3169   | Layout 1             | `d32cae352241`  |
| 3158   | Layout 1             | `d32cae352241`  |
| 3151   | Layout 1             | `d32cae352241`  |
| 3144   | Layout 1             | `d32cae352241`  |
| 3133   | Layout 1             | `d32cae352241`  |
| 3125   | Layout 1             | `d32cae352241`  |
| 3118   | Layout 1             | `d32cae352241`  |
| 3111   | Layout 1             | `d32cae352241`  |
| 3103   | Layout 1             | `d32cae352241`  |
| 3095   | Layout 1             | `d32cae352241`  |
| 3086   | Layout 1             | `d32cae352241`  |
| 3072   | Layout 1             | `d32cae352241`  |
| 3062   | Layout 1             | `d32cae352241`  |
| 3052   | Layout 1             | `d32cae352241`  |
| 3045   | Layout 1             | `d32cae352241`  |
| 3037   | Layout 1             | `d32cae352241`  |
| 3030   | Layout 1             | `d32cae352241`  |
| 3021   | Layout 1             | `d32cae352241`  |
| 3012   | Layout 1             | `d32cae352241`  |
| 3002   | Layout 1             | `d32cae352241`  |
| 2995   | Layout 1             | `d32cae352241`  |
| 2987   | Layout 1             | `d32cae352241`  |
| 2978   | Layout 1             | `d32cae352241`  |
| 2970   | Layout 1             | `d32cae352241`  |
| 2959   | Layout 1             | `d32cae352241`  |
| 2951   | Layout 1             | `d32cae352241`  |
| 2942   | Layout 1             | `d32cae352241`  |
| 2935   | Layout 1             | `d32cae352241`  |
| 2932   | Layout 1             | `d32cae352241`  |
| 2923   | Layout 1             | `d32cae352241`  |
| 2919   | Layout 1             | `d32cae352241`  |
| 2907   | Layout 1             | `d32cae352241`  |
| 2900   | Layout 1             | `d32cae352241`  |
| 2891   | Layout 1             | `d32cae352241`  |
| 2882   | Layout 1             | `d32cae352241`  |
| 2872   | Layout 1             | `d32cae352241`  |
| 2863   | Layout 1             | `d32cae352241`  |
| 2855   | Layout 1             | `d32cae352241`  |
| 2849   | Layout 1             | `d32cae352241`  |
| 2844   | Layout 1             | `d32cae352241`  |
| 2834   | Layout 1             | `d32cae352241`  |
| 2825   | Layout 1             | `d32cae352241`  |
| 2819   | Layout 1             | `d32cae352241`  |
| 2811   | Layout 1             | `d32cae352241`  |
| 2803   | Layout 1             | `d32cae352241`  |
| 2794   | Layout 1             | `d32cae352241`  |
| 2783   | Layout 1             | `d32cae352241`  |
| 2774   | Layout 1             | `d32cae352241`  |
| 2765   | Layout 1             | `d32cae352241`  |
| 2756   | Layout 1             | `d32cae352241`  |
| 2750   | Layout 1             | `d32cae352241`  |
| 2743   | Layout 1             | `d32cae352241`  |
| 2736   | Layout 1             | `d32cae352241`  |
| 2726   | Layout 1             | `d32cae352241`  |
| 2717   | Layout 1             | `d32cae352241`  |
| 2709   | Layout 1             | `d32cae352241`  |
| 2703   | Layout 1             | `d32cae352241`  |
| 2695   | Layout 1             | `d32cae352241`  |
| 2684   | Layout 1             | `d32cae352241`  |
| 2672   | Layout 1             | `d32cae352241`  |
| 2665   | Layout 1             | `d32cae352241`  |
| 2657   | Layout 1             | `d32cae352241`  |
| 2649   | Layout 1             | `d32cae352241`  |
| 2644   | Layout 1             | `d32cae352241`  |
| 2637   | Layout 1             | `d32cae352241`  |
| 2629   | Layout 1             | `d32cae352241`  |
| 2619   | Layout 1             | `d32cae352241`  |
| 2612   | Layout 1             | `d32cae352241`  |
| 2606   | Layout 1             | `d32cae352241`  |
| 2602   | Layout 1             | `d32cae352241`  |
| 2601   | Layout 1             | `d32cae352241`  |
| 2592   | Layout 1             | `d32cae352241`  |
| 2583   | Layout 1             | `d32cae352241`  |
| 2575   | Layout 1             | `d32cae352241`  |
| 2567   | Layout 1             | `d32cae352241`  |
| 2560   | Layout 1             | `d32cae352241`  |
| 2553   | Layout 1             | `d32cae352241`  |
| 2545   | Layout 1             | `d32cae352241`  |
| 2538   | Layout 1             | `d32cae352241`  |
| 2529   | Layout 1             | `d32cae352241`  |
| 2519   | Layout 1             | `d32cae352241`  |
| 2513   | Layout 1             | `d32cae352241`  |
| 2510   | Layout 1             | `d32cae352241`  |
| 2507   | Layout 1             | `d32cae352241`  |
| 2503   | Layout 1             | `d32cae352241`  |
| 2498   | Layout 1             | `d32cae352241`  |
| 2492   | Layout 1             | `d32cae352241`  |
| 2487   | Layout 1             | `d32cae352241`  |
| 2480   | Layout 1             | `d32cae352241`  |
| 2474   | Layout 1             | `d32cae352241`  |
| 2468   | Layout 1             | `d32cae352241`  |
| 2460   | Layout 1             | `d32cae352241`  |
| 2453   | Layout 1             | `d32cae352241`  |
| 2444   | Layout 1             | `d32cae352241`  |
| 2438   | Layout 1             | `d32cae352241`  |
| 2434   | Layout 1             | `d32cae352241`  |
| 2429   | Layout 1             | `d32cae352241`  |
| 2421   | Layout 1             | `d32cae352241`  |
| 2414   | Layout 1             | `d32cae352241`  |
| 2407   | Layout 1             | `d32cae352241`  |
| 2401   | Layout 1             | `d32cae352241`  |
| 2397   | Layout 1             | `d32cae352241`  |
| 2393   | Layout 1             | `d32cae352241`  |
| 2384   | Layout 1             | `d32cae352241`  |
| 2378   | Layout 1             | `d32cae352241`  |
| 2372   | Layout 1             | `d32cae352241`  |
| 2358   | Layout 1             | `d32cae352241`  |
| 2352   | Layout 1             | `d32cae352241`  |
| 2347   | Layout 1             | `d32cae352241`  |
| 2343   | Layout 1             | `d32cae352241`  |
| 2335   | Layout 1             | `d32cae352241`  |
| 2327   | Layout 1             | `d32cae352241`  |
| 2324   | Layout 1             | `d32cae352241`  |
| 2319   | Layout 1             | `d32cae352241`  |
| 2313   | Layout 1             | `d32cae352241`  |
| 2308   | Layout 1             | `d32cae352241`  |
| 2302   | Layout 1             | `d32cae352241`  |
| 2295   | Layout 1             | `d32cae352241`  |
| 2290   | Layout 1             | `d32cae352241`  |
| 2284   | Layout 1             | `d32cae352241`  |
| 2276   | Layout 1             | `d32cae352241`  |
| 2269   | Layout 1             | `d32cae352241`  |
| 2259   | Layout 1             | `d32cae352241`  |
| 2250   | Layout 1             | `d32cae352241`  |
| 2243   | Layout 1             | `d32cae352241`  |
| 2235   | Layout 1             | `d32cae352241`  |
| 2229   | Layout 1             | `d32cae352241`  |
| 2224   | Layout 1             | `d32cae352241`  |
| 2218   | Layout 1             | `d32cae352241`  |
| 2215   | Layout 1             | `d32cae352241`  |
| 2207   | Layout 1             | `d32cae352241`  |
| 2203   | Layout 1             | `d32cae352241`  |
| 2196   | Layout 1             | `d32cae352241`  |
| 2192   | Layout 1             | `d32cae352241`  |
| 2189   | Layout 1             | `d32cae352241`  |
| 2183   | Layout 1             | `d32cae352241`  |
| 2179   | Layout 1             | `d32cae352241`  |
| 2171   | Layout 1             | `d32cae352241`  |
| 2163   | Layout 1             | `d32cae352241`  |
| 2156   | Layout 1             | `d32cae352241`  |
| 2151   | Layout 1             | `d32cae352241`  |
| 2147   | Layout 1             | `d32cae352241`  |
| 2142   | Layout 1             | `d32cae352241`  |
| 2138   | Layout 1             | `d32cae352241`  |
| 2134   | Layout 1             | `d32cae352241`  |
| 2130   | Layout 1             | `d32cae352241`  |
| 2122   | Layout 1             | `d32cae352241`  |
| 2107   | Layout 1             | `d32cae352241`  |
| 2098   | Layout 1             | `d32cae352241`  |
| 2089   | Layout 1             | `d32cae352241`  |
| 2081   | Layout 1             | `d32cae352241`  |
| 2073   | Layout 1             | `d32cae352241`  |
| 2067   | Layout 1             | `d32cae352241`  |
| 2063   | Layout 1             | `d32cae352241`  |
| 2059   | Layout 1             | `d32cae352241`  |
| 2052   | Layout 1             | `d32cae352241`  |
| 2044   | Layout 1             | `d32cae352241`  |
| 2039   | Layout 1             | `d32cae352241`  |
| 2032   | Layout 1             | `d32cae352241`  |
| 2025   | Layout 1             | `d32cae352241`  |
| 2011   | Layout 1             | `d32cae352241`  |
| 2005   | Layout 1             | `d32cae352241`  |
| 2000   | Layout 1             | `d32cae352241`  |
| 1996   | Layout 1             | `d32cae352241`  |
| 1991   | Layout 1             | `d32cae352241`  |
| 1985   | Layout 1             | `d32cae352241`  |
| 1980   | Layout 1             | `d32cae352241`  |
| 1969   | Layout 1             | `d32cae352241`  |
| 1964   | Layout 1             | `d32cae352241`  |
| 1958   | Layout 1             | `d32cae352241`  |
| 1950   | Layout 1             | `d32cae352241`  |
| 1945   | Layout 1             | `d32cae352241`  |
| 1937   | Layout 1             | `d32cae352241`  |
| 1933   | Layout 1             | `d32cae352241`  |
| 1927   | Layout 1             | `d32cae352241`  |
| 1921   | Layout 1             | `d32cae352241`  |
| 1914   | Layout 1             | `d32cae352241`  |
| 1908   | Layout 1             | `d32cae352241`  |
| 1897   | Layout 1             | `d32cae352241`  |
| 1892   | Layout 1             | `d32cae352241`  |
| 1886   | Layout 1             | `d32cae352241`  |
| 1881   | Layout 1             | `d32cae352241`  |
| 1871   | Layout 1             | `d32cae352241`  |
| 1866   | Layout 1             | `d32cae352241`  |
| 1862   | Layout 1             | `d32cae352241`  |
| 1854   | Layout 1             | `d32cae352241`  |
| 1846   | Layout 1             | `d32cae352241`  |
| 1838   | Layout 1             | `d32cae352241`  |
| 1832   | Layout 1             | `d32cae352241`  |
| 1826   | Layout 1             | `d32cae352241`  |
| 1822   | Layout 1             | `d32cae352241`  |
| 1818   | Layout 1             | `d32cae352241`  |
| 1804   | Layout 1             | `d32cae352241`  |
| 1794   | Layout 1             | `d32cae352241`  |
| 1790   | Layout 1             | `d32cae352241`  |
| 1784   | Layout 1             | `d32cae352241`  |
| 1774   | Layout 1             | `d32cae352241`  |
| 1771   | Layout 1             | `d32cae352241`  |
| 1762   | Layout 1             | `d32cae352241`  |
| 1759   | Layout 1             | `d32cae352241`  |
| 1754   | Layout 1             | `d32cae352241`  |
| 1749   | Layout 1             | `d32cae352241`  |
| 1743   | Layout 1             | `d32cae352241`  |
| 1737   | Layout 1             | `d32cae352241`  |
| 1731   | Layout 1             | `d32cae352241`  |
| 1725   | Layout 1             | `d32cae352241`  |
| 1717   | Layout 1             | `d32cae352241`  |
| 1710   | Layout 1             | `d32cae352241`  |
| 1704   | Layout 1             | `d32cae352241`  |
| 1698   | Layout 1             | `d32cae352241`  |
| 1690   | Layout 1             | `d32cae352241`  |
| 1685   | Layout 1             | `d32cae352241`  |
| 1680   | Layout 1             | `d32cae352241`  |
| 1674   | Layout 1             | `d32cae352241`  |
| 1668   | Layout 1             | `d32cae352241`  |
| 1659   | Layout 1             | `d32cae352241`  |
| 1649   | Layout 1             | `d32cae352241`  |
| 1642   | Layout 1             | `d32cae352241`  |
| 1636   | Layout 1             | `d32cae352241`  |
| 1628   | Layout 1             | `d32cae352241`  |
| 1622   | Layout 1             | `d32cae352241`  |
| 1614   | Layout 1             | `d32cae352241`  |
| 1608   | Layout 1             | `d32cae352241`  |
| 1602   | Layout 1             | `d32cae352241`  |
| 1598   | Layout 1             | `d32cae352241`  |
| 1594   | Layout 1             | `d32cae352241`  |
| 1590   | Layout 1             | `d32cae352241`  |
| 1587   | Layout 1             | `d32cae352241`  |
| 1584   | Layout 1             | `d32cae352241`  |
| 1579   | Layout 1             | `d32cae352241`  |
| 1572   | Layout 1             | `d32cae352241`  |
| 1565   | Layout 1             | `d32cae352241`  |
| 1559   | Layout 1             | `d32cae352241`  |
| 1554   | Layout 1             | `d32cae352241`  |
| 1547   | Layout 1             | `d32cae352241`  |
| 1537   | Layout 1             | `d32cae352241`  |
| 1529   | Layout 1             | `d32cae352241`  |
| 1524   | Layout 1             | `d32cae352241`  |
| 1519   | Layout 1             | `d32cae352241`  |
| 1509   | Layout 1             | `d32cae352241`  |
| 1506   | Layout 1             | `d32cae352241`  |
| 1504   | Layout 1             | `d32cae352241`  |
| 1500   | Layout 1             | `d32cae352241`  |
| 1493   | Layout 1             | `d32cae352241`  |
| 1489   | Layout 1             | `d32cae352241`  |
| 1485   | Layout 1             | `d32cae352241`  |
| 1481   | Layout 1             | `d32cae352241`  |
| 1474   | Layout 1             | `d32cae352241`  |
| 1466   | Layout 1             | `d32cae352241`  |
| 1462   | Layout 1             | `d32cae352241`  |
| 1459   | Layout 1             | `d32cae352241`  |
| 1453   | Layout 1             | `d32cae352241`  |
| 1450   | Layout 1             | `d32cae352241`  |
| 1445   | Layout 1             | `d32cae352241`  |
| 1439   | Layout 1             | `d32cae352241`  |
| 1433   | Layout 1             | `d32cae352241`  |
| 1430   | Layout 1             | `d32cae352241`  |
| 1426   | Layout 1             | `d32cae352241`  |
| 1421   | Layout 1             | `d32cae352241`  |
| 1417   | Layout 1             | `d32cae352241`  |
| 1416   | Layout 1             | `d32cae352241`  |
| 1409   | Layout 1             | `d32cae352241`  |
| 1405   | Layout 1             | `d32cae352241`  |
| 1401   | Layout 1             | `d32cae352241`  |
| 1396   | Layout 1             | `d32cae352241`  |
| 1391   | Layout 1             | `d32cae352241`  |
| 1390   | Layout 1             | `d32cae352241`  |
| 1386   | Layout 1             | `d32cae352241`  |
| 1381   | Layout 1             | `d32cae352241`  |
| 1379   | Layout 1             | `d32cae352241`  |
| 1372   | Layout 1             | `d32cae352241`  |
| 1366   | Layout 1             | `d32cae352241`  |
| 1364   | Layout 1             | `d32cae352241`  |
| 1363   | Layout 1             | `d32cae352241`  |
| 1360   | Layout 1             | `d32cae352241`  |
| 1358   | Layout 1             | `d32cae352241`  |
| 1355   | Layout 1             | `d32cae352241`  |
| 1351   | Layout 1             | `d32cae352241`  |
| 1348   | Layout 1             | `d32cae352241`  |
| 1346   | Layout 1             | `d32cae352241`  |
| 1341   | Layout 1             | `d32cae352241`  |
| 1340   | Layout 1             | `d32cae352241`  |
| 1338   | Layout 1             | `d32cae352241`  |
| 1335   | Layout 1             | `d32cae352241`  |
| 1333   | Layout 1             | `d32cae352241`  |
| 1329   | Layout 1             | `d32cae352241`  |
| 1327   | Layout 1             | `d32cae352241`  |
| 1324   | Layout 1             | `d32cae352241`  |
| 1321   | Layout 1             | `d32cae352241`  |
| 1319   | Layout 1             | `d32cae352241`  |
| 1318   | Layout 1             | `d32cae352241`  |
| 1316   | Layout 1             | `d32cae352241`  |
| 1313   | Layout 1             | `d32cae352241`  |
| 1311   | Layout 1             | `d32cae352241`  |
| 1309   | Layout 1             | `d32cae352241`  |
| 1304   | Layout 1             | `d32cae352241`  |
| 1292   | No documented layout | `d32cae352241`  |
| 1286   | No documented layout | `d32cae352241`  |
| 1280   | No documented layout | `d32cae352241`  |
| 1276   | No documented layout | `d32cae352241`  |
| 1267   | No documented layout | `d32cae352241`  |
| 1261   | No documented layout | `d32cae352241`  |
| 1256   | No documented layout | `d32cae352241`  |
| 1250   | No documented layout | `d32cae352241`  |
| 1246   | No documented layout | `d32cae352241`  |
| 1239   | No documented layout | `d32cae352241`  |
| 1230   | No documented layout | `d32cae352241`  |
| 1226   | No documented layout | `d32cae352241`  |
| 1220   | No documented layout | `d32cae352241`  |
| 1217   | No documented layout | `d32cae352241`  |
| 1211   | No documented layout | `d32cae352241`  |
| 1210   | No documented layout | `d32cae352241`  |
| 1208   | No documented layout | `d32cae352241`  |
| 1203   | No documented layout | `d32cae352241`  |
| 1197   | No documented layout | `d32cae352241`  |
| 1194   | No documented layout | `d32cae352241`  |
| 1192   | No documented layout | `d32cae352241`  |
| 1187   | No documented layout | `d32cae352241`  |
| 1183   | No documented layout | `d32cae352241`  |
| 1177   | No documented layout | `d32cae352241`  |
| 1173   | No documented layout | `d32cae352241`  |
| 1167   | No documented layout | `d32cae352241`  |
| 1164   | No documented layout | `d32cae352241`  |
| 1156   | No documented layout | `d32cae352241`  |
| 1149   | No documented layout | `d32cae352241`  |
| 1144   | No documented layout | `d32cae352241`  |
| 1137   | No documented layout | `d32cae352241`  |
| 1132   | No documented layout | `d32cae352241`  |
| 1127   | No documented layout | `d32cae352241`  |
| 1122   | No documented layout | `d32cae352241`  |
| 1118   | No documented layout | `d32cae352241`  |
| 1114   | No documented layout | `d32cae352241`  |
| 1109   | No documented layout | `d32cae352241`  |
| 1102   | No documented layout | `d32cae352241`  |
| 1096   | No documented layout | `d32cae352241`  |
| 1088   | No documented layout | `d32cae352241`  |
| 1081   | No documented layout | `d32cae352241`  |
| 1076   | No documented layout | `d32cae352241`  |
| 1069   | No documented layout | `d32cae352241`  |
| 1064   | No documented layout | `d32cae352241`  |
| 1058   | No documented layout | `d32cae352241`  |
| 1051   | No documented layout | `d32cae352241`  |
| 1044   | No documented layout | `d32cae352241`  |
| 1036   | No documented layout | `d32cae352241`  |
| 1026   | No documented layout | `d32cae352241`  |
| 1016   | No documented layout | `d32cae352241`  |
| 1009   | No documented layout | `d32cae352241`  |
| 1005   | No documented layout | `d32cae352241`  |
| 1000   | No documented layout | `d32cae352241`  |
| 998    | No documented layout | `d32cae352241`  |
| 990    | No documented layout | `d32cae352241`  |
| 979    | No documented layout | `d32cae352241`  |
| 972    | No documented layout | `d32cae352241`  |
| 963    | No documented layout | `d32cae352241`  |
| 955    | No documented layout | `d32cae352241`  |
| 946    | No documented layout | `d32cae352241`  |
| 938    | No documented layout | `d32cae352241`  |
| 927    | No documented layout | `d32cae352241`  |
| 911    | No documented layout | `d32cae352241`  |
| 904    | No documented layout | `d32cae352241`  |
| 899    | No documented layout | `d32cae352241`  |
| 894    | No documented layout | `d32cae352241`  |
| 885    | No documented layout | `d32cae352241`  |
| 879    | No documented layout | `d32cae352241`  |
| 872    | No documented layout | `d32cae352241`  |
| 864    | No documented layout | `d32cae352241`  |
| 855    | No documented layout | `d32cae352241`  |
| 853    | No documented layout | `d32cae352241`  |
| 845    | No documented layout | `d32cae352241`  |
| 837    | No documented layout | `d32cae352241`  |
| 829    | No documented layout | `d32cae352241`  |
| 822    | No documented layout | `d32cae352241`  |
| 814    | No documented layout | `d32cae352241`  |
| 805    | No documented layout | `d32cae352241`  |
| 794    | No documented layout | `d32cae352241`  |
| 787    | No documented layout | `d32cae352241`  |
| 780    | No documented layout | `d32cae352241`  |
| 771    | No documented layout | `d32cae352241`  |
| 760    | No documented layout | `d32cae352241`  |
| 748    | No documented layout | `d32cae352241`  |
| 741    | No documented layout | `d32cae352241`  |
| 736    | No documented layout | `d32cae352241`  |
| 731    | No documented layout | `d32cae352241`  |
| 723    | No documented layout | `d32cae352241`  |
| 711    | No documented layout | `d32cae352241`  |
| 707    | No documented layout | `d32cae352241`  |
| 697    | No documented layout | `d32cae352241`  |
| 689    | No documented layout | `d32cae352241`  |
| 683    | No documented layout | `d32cae352241`  |
| 678    | No documented layout | `d32cae352241`  |
| 670    | No documented layout | `d32cae352241`  |
| 661    | No documented layout | `d32cae352241`  |
| 656    | No documented layout | `d32cae352241`  |
| 652    | No documented layout | `d32cae352241`  |
| 643    | No documented layout | `d32cae352241`  |
| 637    | No documented layout | `d32cae352241`  |
| 630    | No documented layout | `d32cae352241`  |
| 627    | No documented layout | `d32cae352241`  |
| 621    | No documented layout | `d32cae352241`  |
| 617    | No documented layout | `d32cae352241`  |
| 615    | No documented layout | `d32cae352241`  |
| 606    | No documented layout | `d32cae352241`  |
| 599    | No documented layout | `d32cae352241`  |
| 592    | No documented layout | `d32cae352241`  |
| 586    | No documented layout | `d32cae352241`  |
| 577    | No documented layout | `d32cae352241`  |
| 569    | No documented layout | `d32cae352241`  |
| 561    | No documented layout | `d32cae352241`  |
| 554    | No documented layout | `d32cae352241`  |
| 542    | No documented layout | `d32cae352241`  |
| 532    | No documented layout | `d32cae352241`  |
| 531    | No documented layout | `d32cae352241`  |
| 526    | No documented layout | `d32cae352241`  |
| 521    | No documented layout | `d32cae352241`  |
| 517    | No documented layout | `d32cae352241`  |
| 510    | No documented layout | `d32cae352241`  |
| 508    | No documented layout | `d32cae352241`  |
| 504    | No documented layout | `d32cae352241`  |
| 497    | No documented layout | `d32cae352241`  |
| 491    | No documented layout | `d32cae352241`  |
| 485    | No documented layout | `d32cae352241`  |
| 478    | No documented layout | `d32cae352241`  |
| 472    | No documented layout | `d32cae352241`  |
| 466    | No documented layout | `d32cae352241`  |
| 457    | No documented layout | `d32cae352241`  |
| 452    | No documented layout | `d32cae352241`  |
| 449    | No documented layout | `d32cae352241`  |
| 435    | No documented layout | `d32cae352241`  |

<!-- versions:end -->

## Observed Values

Same layout as [`newquest.bss`](newquest_bss.md), the layout reference: an 8-byte `PABR` header with a group count; per group an 11-byte header, 17-byte quest reference rows and a 12-byte trailer; a string table; an 8-byte file trailer. One handler reads all four quest lists. Values seen on client 3458:

| Field                                  | Observed                                              |
| -------------------------------------- | ----------------------------------------------------- |
| `group_count`                          | `122`                                                 |
| First group                            | key `165`, `9` rows                                   |
| Group header `group_type`              | `0` to `8`, see Open Questions                        |
| Group trailer start / end index        | Index `2`, the empty string: no event period          |
| Row `is_sub_quest`                       | `0` on every row                                      |
| Row `hide_conditions_index`                   | Empty string on 1,149 rows, a script on 142           |
| Row `visible_conditions_index`                   | Empty string on 1,045 rows, a script on 246           |
| String table                           | `1,456` strings; `string_count` at `0x000060B9`       |

The scripts check prerequisite quests, level, class, content groups, knowledge (`getknowledge(9917);`), items (`getItemCount`) and Olvia Academy enrolment (`checkOlviaAcademyStudent`); see String Table in the `newquest.bss` doc for the two script roles.

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

## Localization

LOC type `28` holds the English text of this list, keyed by the group's `group_key`:

| Key                                                               | Text                                                 |
| ----------------------------------------------------------------- | ---------------------------------------------------- |
| `str_id1 = group_key`, `str_id4 = 0`                              | Group name, e.g. key 165 `[Life 101] The Adventurer That Does It All` |
| `str_id1 = packed_quest_id`, `str_id2 = group_key`, `str_id4 = 1` | The quest's condition line, e.g. `<PAColor0xfff3d900>from Lv. 60<PAOldColor>, via <PAColor0xfff3d900>Fughar<PAOldColor>` |

On client 3458 all 122 groups have a name (type 28 has 192, keys 1 to 200, so some belong to groups no longer in the file) and all 1,291 rows have a condition line. Condition lines carry `<PAColor>` tags (all but 2); group names do not. The string table holds the Korean source of both, which the handler shows where LOC has no row.

## Notes

- Decompressed size is `203,307` bytes on client 3458.
- 23 quests sit in two groups, with a condition line under each key: quest 7215 / 1 is in key 13 (`[ADV Support] [Lv. 53] Legendary Leveling with Chenga and Quests`) and key 155 (`[Social Action] Please Read Quietly!`).

## Open Questions

### Group Header Byte `group_type`

`0` on 65 of 122 groups and `1` to `8` on the rest, grouped by theme: 1 holds Olvia Academy and `[ADV Support] [Lv. 53]` leveling groups, 2 mounts and outfits (`[Mount] Shai - Fwuzzy Alpaca`), 3 `[The Great Expedition]`, 4 to 7 the `[Life] [Leap]` gurus split by life skill (cooking and alchemy at 5, hunting at 7) and 8 a mix (`[ADV Support] Inventory Expansion!`, `[Music] ...`). It may be the category tab of the recommendation window; the server calls it `RecommendationQuestType` and sets the same value on 17 of the 19 shared groups where it is not `0`, but no Lua getter reads it.

### Shared Fields

What `group_type` selects is open for all four lists; see the Open Questions of [`newquest.bss`](newquest_bss.md).
