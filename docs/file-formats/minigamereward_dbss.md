# `minigamereward.dbss` Format

## Purpose

The energy and item drop of three minigames, one row each: the energy of a
success and of a failure, the `itemmaingroup.bss` drop group a success
gives, and the vehicle type the player must be on. On client 3474 the rows
are minigame `1` on a Cow (vehicle type `26`, group 65021: Milk), `2` on a
herbal machine (`24`, group 65023: Sunrise Herb, Silver Azalea and the other
herbs) and `3` on an extractor (`25`, group 65022: Black Stone Powder, Rough
Stone).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                        | Bytes | Records      | Row bytes |
| ------ | -------------- | --------------------------- | ----- | ------------ | --------- |
| 2      | 2726 and later | `minigamereward.dbss`       | 43    | 3 Row        | 13        |
| 2      | 2726 and later | `minigamerewardoffset.dbss` | 34    | 3 Offset Row | 10        |
| 1      | 1346 to 2717   | `minigamereward.dbss`       | 37    | 3 Row        | 11        |
| 1      | 1346 to 2717   | `minigamerewardoffset.dbss` | 34    | 3 Offset Row | 10        |

| Layout | File                        | Known         | Unknown    |
| ------ | --------------------------- | ------------- | ---------- |
| 2      | `minigamereward.dbss`       | 43 B (100.0%) | 0 B (0.0%) |
| 2      | `minigamerewardoffset.dbss` | 34 B (100.0%) | 0 B (0.0%) |
| 1      | `minigamereward.dbss`       | 37 B (100.0%) | 0 B (0.0%) |
| 1      | `minigamerewardoffset.dbss` | 34 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `ee641b220186`  |
| 3482   | Layout 2             | `ee641b220186`  |
| 3474   | Layout 2             | `ee641b220186`  |
| 3473   | Layout 2             | `ee641b220186`  |
| 3464   | Layout 2             | `ee641b220186`  |
| 3458   | Layout 2             | `ee641b220186`  |
| 3454   | Layout 2             | `ee641b220186`  |
| 3444   | Layout 2             | `ee641b220186`  |
| 3435   | Layout 2             | `ee641b220186`  |
| 3426   | Layout 2             | `ee641b220186`  |
| 3418   | Layout 2             | `ee641b220186`  |
| 3412   | Layout 2             | `ee641b220186`  |
| 3402   | Layout 2             | `ee641b220186`  |
| 3396   | Layout 2             | `ee641b220186`  |
| 3387   | Layout 2             | `ee641b220186`  |
| 3381   | Layout 2             | `ee641b220186`  |
| 3373   | Layout 2             | `ee641b220186`  |
| 3364   | Layout 2             | `ee641b220186`  |
| 3356   | Layout 2             | `ee641b220186`  |
| 3349   | Layout 2             | `ee641b220186`  |
| 3342   | Layout 2             | `ee641b220186`  |
| 3335   | Layout 2             | `ee641b220186`  |
| 3326   | Layout 2             | `ee641b220186`  |
| 3321   | Layout 2             | `ee641b220186`  |
| 3314   | Layout 2             | `ee641b220186`  |
| 3303   | Layout 2             | `ee641b220186`  |
| 3302   | Layout 2             | `ee641b220186`  |
| 3293   | Layout 2             | `ee641b220186`  |
| 3283   | Layout 2             | `ee641b220186`  |
| 3275   | Layout 2             | `ee641b220186`  |
| 3267   | Layout 2             | `ee641b220186`  |
| 3258   | Layout 2             | `ee641b220186`  |
| 3251   | Layout 2             | `ee641b220186`  |
| 3242   | Layout 2             | `ee641b220186`  |
| 3235   | Layout 2             | `ee641b220186`  |
| 3229   | Layout 2             | `ee641b220186`  |
| 3212   | Layout 2             | `ee641b220186`  |
| 3203   | Layout 2             | `ee641b220186`  |
| 3193   | Layout 2             | `ee641b220186`  |
| 3186   | Layout 2             | `ee641b220186`  |
| 3177   | Layout 2             | `ee641b220186`  |
| 3169   | Layout 2             | `ee641b220186`  |
| 3158   | Layout 2             | `ee641b220186`  |
| 3151   | Layout 2             | `ee641b220186`  |
| 3144   | Layout 2             | `ee641b220186`  |
| 3133   | Layout 2             | `ee641b220186`  |
| 3125   | Layout 2             | `ee641b220186`  |
| 3118   | Layout 2             | `ee641b220186`  |
| 3111   | Layout 2             | `ee641b220186`  |
| 3103   | Layout 2             | `ee641b220186`  |
| 3095   | Layout 2             | `ee641b220186`  |
| 3086   | Layout 2             | `ee641b220186`  |
| 3072   | Layout 2             | `ee641b220186`  |
| 3062   | Layout 2             | `ee641b220186`  |
| 3052   | Layout 2             | `ee641b220186`  |
| 3045   | Layout 2             | `ee641b220186`  |
| 3037   | Layout 2             | `ee641b220186`  |
| 3030   | Layout 2             | `ee641b220186`  |
| 3021   | Layout 2             | `ee641b220186`  |
| 3012   | Layout 2             | `ee641b220186`  |
| 3002   | Layout 2             | `ee641b220186`  |
| 2995   | Layout 2             | `ee641b220186`  |
| 2987   | Layout 2             | `ee641b220186`  |
| 2978   | Layout 2             | `ee641b220186`  |
| 2970   | Layout 2             | `ee641b220186`  |
| 2959   | Layout 2             | `ee641b220186`  |
| 2951   | Layout 2             | `ee641b220186`  |
| 2942   | Layout 2             | `ee641b220186`  |
| 2935   | Layout 2             | `ee641b220186`  |
| 2932   | Layout 2             | `ee641b220186`  |
| 2923   | Layout 2             | `ee641b220186`  |
| 2919   | Layout 2             | `ee641b220186`  |
| 2907   | Layout 2             | `ee641b220186`  |
| 2900   | Layout 2             | `ee641b220186`  |
| 2891   | Layout 2             | `ee641b220186`  |
| 2882   | Layout 2             | `ee641b220186`  |
| 2872   | Layout 2             | `ee641b220186`  |
| 2863   | Layout 2             | `ee641b220186`  |
| 2855   | Layout 2             | `ee641b220186`  |
| 2849   | Layout 2             | `ee641b220186`  |
| 2844   | Layout 2             | `ee641b220186`  |
| 2834   | Layout 2             | `ee641b220186`  |
| 2825   | Layout 2             | `ee641b220186`  |
| 2819   | Layout 2             | `ee641b220186`  |
| 2811   | Layout 2             | `ee641b220186`  |
| 2803   | Layout 2             | `ee641b220186`  |
| 2794   | Layout 2             | `ee641b220186`  |
| 2783   | Layout 2             | `ee641b220186`  |
| 2774   | Layout 2             | `ee641b220186`  |
| 2765   | Layout 2             | `ee641b220186`  |
| 2756   | Layout 2             | `ee641b220186`  |
| 2750   | Layout 2             | `ee641b220186`  |
| 2743   | Layout 2             | `ee641b220186`  |
| 2736   | Layout 2             | `ee641b220186`  |
| 2726   | Layout 2             | `ee641b220186`  |
| 2717   | Layout 1             | `ee641b220186`  |
| 2709   | Layout 1             | `ee641b220186`  |
| 2703   | Layout 1             | `ee641b220186`  |
| 2695   | Layout 1             | `ee641b220186`  |
| 2684   | Layout 1             | `ee641b220186`  |
| 2672   | Layout 1             | `ee641b220186`  |
| 2665   | Layout 1             | `ee641b220186`  |
| 2657   | Layout 1             | `ee641b220186`  |
| 2649   | Layout 1             | `ee641b220186`  |
| 2644   | Layout 1             | `ee641b220186`  |
| 2637   | Layout 1             | `ee641b220186`  |
| 2629   | Layout 1             | `ee641b220186`  |
| 2619   | Layout 1             | `ee641b220186`  |
| 2612   | Layout 1             | `ee641b220186`  |
| 2606   | Layout 1             | `ee641b220186`  |
| 2602   | Layout 1             | `ee641b220186`  |
| 2601   | Layout 1             | `ee641b220186`  |
| 2592   | Layout 1             | `ee641b220186`  |
| 2583   | Layout 1             | `ee641b220186`  |
| 2575   | Layout 1             | `ee641b220186`  |
| 2567   | Layout 1             | `ee641b220186`  |
| 2560   | Layout 1             | `ee641b220186`  |
| 2553   | Layout 1             | `ee641b220186`  |
| 2545   | Layout 1             | `ee641b220186`  |
| 2538   | Layout 1             | `ee641b220186`  |
| 2529   | Layout 1             | `ee641b220186`  |
| 2519   | Layout 1             | `ee641b220186`  |
| 2513   | Layout 1             | `ee641b220186`  |
| 2510   | Layout 1             | `ee641b220186`  |
| 2507   | Layout 1             | `ee641b220186`  |
| 2503   | Layout 1             | `ee641b220186`  |
| 2498   | Layout 1             | `ee641b220186`  |
| 2492   | Layout 1             | `ee641b220186`  |
| 2487   | Layout 1             | `ee641b220186`  |
| 2480   | Layout 1             | `ee641b220186`  |
| 2474   | Layout 1             | `ee641b220186`  |
| 2468   | Layout 1             | `ee641b220186`  |
| 2460   | Layout 1             | `ee641b220186`  |
| 2453   | Layout 1             | `ee641b220186`  |
| 2444   | Layout 1             | `ee641b220186`  |
| 2438   | Layout 1             | `ee641b220186`  |
| 2434   | Layout 1             | `ee641b220186`  |
| 2429   | Layout 1             | `ee641b220186`  |
| 2421   | Layout 1             | `ee641b220186`  |
| 2414   | Layout 1             | `ee641b220186`  |
| 2407   | Layout 1             | `ee641b220186`  |
| 2401   | Layout 1             | `ee641b220186`  |
| 2397   | Layout 1             | `ee641b220186`  |
| 2393   | Layout 1             | `ee641b220186`  |
| 2384   | Layout 1             | `ee641b220186`  |
| 2378   | Layout 1             | `ee641b220186`  |
| 2372   | Layout 1             | `ee641b220186`  |
| 2358   | Layout 1             | `ee641b220186`  |
| 2352   | Layout 1             | `ee641b220186`  |
| 2347   | Layout 1             | `ee641b220186`  |
| 2343   | Layout 1             | `ee641b220186`  |
| 2335   | Layout 1             | `ee641b220186`  |
| 2327   | Layout 1             | `ee641b220186`  |
| 2324   | Layout 1             | `ee641b220186`  |
| 2319   | Layout 1             | `ee641b220186`  |
| 2313   | Layout 1             | `ee641b220186`  |
| 2308   | Layout 1             | `ee641b220186`  |
| 2302   | Layout 1             | `ee641b220186`  |
| 2295   | Layout 1             | `ee641b220186`  |
| 2290   | Layout 1             | `ee641b220186`  |
| 2284   | Layout 1             | `ee641b220186`  |
| 2276   | Layout 1             | `ee641b220186`  |
| 2269   | Layout 1             | `ee641b220186`  |
| 2259   | Layout 1             | `ee641b220186`  |
| 2250   | Layout 1             | `ee641b220186`  |
| 2243   | Layout 1             | `ee641b220186`  |
| 2235   | Layout 1             | `ee641b220186`  |
| 2229   | Layout 1             | `ee641b220186`  |
| 2224   | Layout 1             | `ee641b220186`  |
| 2218   | Layout 1             | `ee641b220186`  |
| 2215   | Layout 1             | `ee641b220186`  |
| 2207   | Layout 1             | `ee641b220186`  |
| 2203   | Layout 1             | `ee641b220186`  |
| 2196   | Layout 1             | `ee641b220186`  |
| 2192   | Layout 1             | `ee641b220186`  |
| 2189   | Layout 1             | `ee641b220186`  |
| 2183   | Layout 1             | `ee641b220186`  |
| 2179   | Layout 1             | `ee641b220186`  |
| 2171   | Layout 1             | `ee641b220186`  |
| 2163   | Layout 1             | `ee641b220186`  |
| 2156   | Layout 1             | `ee641b220186`  |
| 2151   | Layout 1             | `ee641b220186`  |
| 2147   | Layout 1             | `ee641b220186`  |
| 2142   | Layout 1             | `ee641b220186`  |
| 2138   | Layout 1             | `ee641b220186`  |
| 2134   | Layout 1             | `ee641b220186`  |
| 2130   | Layout 1             | `ee641b220186`  |
| 2122   | Layout 1             | `ee641b220186`  |
| 2107   | Layout 1             | `ee641b220186`  |
| 2098   | Layout 1             | `ee641b220186`  |
| 2089   | Layout 1             | `ee641b220186`  |
| 2081   | Layout 1             | `ee641b220186`  |
| 2073   | Layout 1             | `ee641b220186`  |
| 2067   | Layout 1             | `ee641b220186`  |
| 2063   | Layout 1             | `ee641b220186`  |
| 2059   | Layout 1             | `ee641b220186`  |
| 2052   | Layout 1             | `ee641b220186`  |
| 2044   | Layout 1             | `ee641b220186`  |
| 2039   | Layout 1             | `ee641b220186`  |
| 2032   | Layout 1             | `ee641b220186`  |
| 2025   | Layout 1             | `ee641b220186`  |
| 2011   | Layout 1             | `ee641b220186`  |
| 2005   | Layout 1             | `ee641b220186`  |
| 2000   | Layout 1             | `ee641b220186`  |
| 1996   | Layout 1             | `ee641b220186`  |
| 1991   | Layout 1             | `ee641b220186`  |
| 1985   | Layout 1             | `ee641b220186`  |
| 1980   | Layout 1             | `ee641b220186`  |
| 1969   | Layout 1             | `ee641b220186`  |
| 1964   | Layout 1             | `ee641b220186`  |
| 1958   | Layout 1             | `ee641b220186`  |
| 1950   | Layout 1             | `ee641b220186`  |
| 1945   | Layout 1             | `ee641b220186`  |
| 1937   | Layout 1             | `ee641b220186`  |
| 1933   | Layout 1             | `ee641b220186`  |
| 1927   | Layout 1             | `ee641b220186`  |
| 1921   | Layout 1             | `ee641b220186`  |
| 1914   | Layout 1             | `ee641b220186`  |
| 1908   | Layout 1             | `ee641b220186`  |
| 1897   | Layout 1             | `ee641b220186`  |
| 1892   | Layout 1             | `ee641b220186`  |
| 1886   | Layout 1             | `ee641b220186`  |
| 1881   | Layout 1             | `ee641b220186`  |
| 1871   | Layout 1             | `ee641b220186`  |
| 1866   | Layout 1             | `ee641b220186`  |
| 1862   | Layout 1             | `ee641b220186`  |
| 1854   | Layout 1             | `ee641b220186`  |
| 1846   | Layout 1             | `ee641b220186`  |
| 1838   | Layout 1             | `ee641b220186`  |
| 1832   | Layout 1             | `ee641b220186`  |
| 1826   | Layout 1             | `ee641b220186`  |
| 1822   | Layout 1             | `ee641b220186`  |
| 1818   | Layout 1             | `ee641b220186`  |
| 1804   | Layout 1             | `ee641b220186`  |
| 1794   | Layout 1             | `ee641b220186`  |
| 1790   | Layout 1             | `ee641b220186`  |
| 1784   | Layout 1             | `ee641b220186`  |
| 1774   | Layout 1             | `ee641b220186`  |
| 1771   | Layout 1             | `ee641b220186`  |
| 1762   | Layout 1             | `ee641b220186`  |
| 1759   | Layout 1             | `ee641b220186`  |
| 1754   | Layout 1             | `ee641b220186`  |
| 1749   | Layout 1             | `ee641b220186`  |
| 1743   | Layout 1             | `ee641b220186`  |
| 1737   | Layout 1             | `ee641b220186`  |
| 1731   | Layout 1             | `ee641b220186`  |
| 1725   | Layout 1             | `ee641b220186`  |
| 1717   | Layout 1             | `ee641b220186`  |
| 1710   | Layout 1             | `ee641b220186`  |
| 1704   | Layout 1             | `ee641b220186`  |
| 1698   | Layout 1             | `ee641b220186`  |
| 1690   | Layout 1             | `ee641b220186`  |
| 1685   | Layout 1             | `ee641b220186`  |
| 1680   | Layout 1             | `ee641b220186`  |
| 1674   | Layout 1             | `ee641b220186`  |
| 1668   | Layout 1             | `ee641b220186`  |
| 1659   | Layout 1             | `ee641b220186`  |
| 1649   | Layout 1             | `ee641b220186`  |
| 1642   | Layout 1             | `ee641b220186`  |
| 1636   | Layout 1             | `ee641b220186`  |
| 1628   | Layout 1             | `ee641b220186`  |
| 1622   | Layout 1             | `ee641b220186`  |
| 1614   | Layout 1             | `ee641b220186`  |
| 1608   | Layout 1             | `ee641b220186`  |
| 1602   | Layout 1             | `ee641b220186`  |
| 1598   | Layout 1             | `ee641b220186`  |
| 1594   | Layout 1             | `ee641b220186`  |
| 1590   | Layout 1             | `ee641b220186`  |
| 1587   | Layout 1             | `ee641b220186`  |
| 1584   | Layout 1             | `ee641b220186`  |
| 1579   | Layout 1             | `ee641b220186`  |
| 1572   | Layout 1             | `ee641b220186`  |
| 1565   | Layout 1             | `ee641b220186`  |
| 1559   | Layout 1             | `ee641b220186`  |
| 1554   | Layout 1             | `ee641b220186`  |
| 1547   | Layout 1             | `ee641b220186`  |
| 1537   | Layout 1             | `ee641b220186`  |
| 1529   | Layout 1             | `ee641b220186`  |
| 1524   | Layout 1             | `ee641b220186`  |
| 1519   | Layout 1             | `ee641b220186`  |
| 1509   | Layout 1             | `ee641b220186`  |
| 1506   | Layout 1             | `ee641b220186`  |
| 1504   | Layout 1             | `ee641b220186`  |
| 1500   | Layout 1             | `ee641b220186`  |
| 1493   | Layout 1             | `ee641b220186`  |
| 1489   | Layout 1             | `ee641b220186`  |
| 1485   | Layout 1             | `ee641b220186`  |
| 1481   | Layout 1             | `ee641b220186`  |
| 1474   | Layout 1             | `ee641b220186`  |
| 1466   | Layout 1             | `ee641b220186`  |
| 1462   | Layout 1             | `ee641b220186`  |
| 1459   | Layout 1             | `ee641b220186`  |
| 1453   | Layout 1             | `ee641b220186`  |
| 1450   | Layout 1             | `ee641b220186`  |
| 1445   | Layout 1             | `ee641b220186`  |
| 1439   | Layout 1             | `ee641b220186`  |
| 1433   | Layout 1             | `ee641b220186`  |
| 1430   | Layout 1             | `ee641b220186`  |
| 1426   | Layout 1             | `ee641b220186`  |
| 1421   | Layout 1             | `ee641b220186`  |
| 1417   | Layout 1             | `ee641b220186`  |
| 1416   | Layout 1             | `ee641b220186`  |
| 1409   | Layout 1             | `ee641b220186`  |
| 1405   | Layout 1             | `ee641b220186`  |
| 1401   | Layout 1             | `ee641b220186`  |
| 1396   | Layout 1             | `ee641b220186`  |
| 1391   | Layout 1             | `ee641b220186`  |
| 1390   | Layout 1             | `ee641b220186`  |
| 1386   | Layout 1             | `ee641b220186`  |
| 1381   | Layout 1             | `ee641b220186`  |
| 1379   | Layout 1             | `ee641b220186`  |
| 1372   | Layout 1             | `ee641b220186`  |
| 1366   | Layout 1             | `ee641b220186`  |
| 1364   | Layout 1             | `ee641b220186`  |
| 1363   | Layout 1             | `ee641b220186`  |
| 1360   | Layout 1             | `ee641b220186`  |
| 1358   | Layout 1             | `ee641b220186`  |
| 1355   | Layout 1             | `ee641b220186`  |
| 1351   | Layout 1             | `ee641b220186`  |
| 1348   | Layout 1             | `ee641b220186`  |
| 1346   | Layout 1             | `ee641b220186`  |
| 1341   | No documented layout | `ee641b220186`  |
| 1340   | No documented layout | `ee641b220186`  |
| 1338   | No documented layout | `ee641b220186`  |
| 1335   | No documented layout | `ee641b220186`  |
| 1333   | No documented layout | `ee641b220186`  |
| 1329   | No documented layout | `ee641b220186`  |
| 1327   | No documented layout | `ee641b220186`  |
| 1324   | No documented layout | `ee641b220186`  |
| 1321   | No documented layout | `ee641b220186`  |
| 1319   | No documented layout | `ee641b220186`  |
| 1318   | No documented layout | `ee641b220186`  |
| 1316   | No documented layout | `ee641b220186`  |
| 1313   | No documented layout | `ee641b220186`  |
| 1311   | No documented layout | `ee641b220186`  |
| 1309   | No documented layout | `ee641b220186`  |
| 1304   | No documented layout | `ee641b220186`  |
| 1292   | No documented layout | `ee641b220186`  |
| 1286   | No documented layout | `ee641b220186`  |
| 1280   | No documented layout | `ee641b220186`  |
| 1276   | No documented layout | `ee641b220186`  |
| 1267   | No documented layout | `ee641b220186`  |
| 1261   | No documented layout | `ee641b220186`  |
| 1256   | No file              | `ee641b220186`  |
| 1250   | No file              | `ee641b220186`  |
| 1246   | No file              | `ee641b220186`  |
| 1239   | No file              | `ee641b220186`  |
| 1230   | No file              | `ee641b220186`  |
| 1226   | No file              | `ee641b220186`  |
| 1220   | No file              | `ee641b220186`  |
| 1217   | No file              | `ee641b220186`  |
| 1211   | No file              | `ee641b220186`  |
| 1210   | No file              | `ee641b220186`  |
| 1208   | No file              | `ee641b220186`  |
| 1203   | No file              | `ee641b220186`  |
| 1197   | No file              | `ee641b220186`  |
| 1194   | No file              | `ee641b220186`  |
| 1192   | No file              | `ee641b220186`  |
| 1187   | No file              | `ee641b220186`  |
| 1183   | No file              | `ee641b220186`  |
| 1177   | No file              | `ee641b220186`  |
| 1173   | No file              | `ee641b220186`  |
| 1167   | No file              | `ee641b220186`  |
| 1164   | No file              | `ee641b220186`  |
| 1156   | No file              | `ee641b220186`  |
| 1149   | No file              | `ee641b220186`  |
| 1144   | No file              | `ee641b220186`  |
| 1137   | No file              | `ee641b220186`  |
| 1132   | No file              | `ee641b220186`  |
| 1127   | No file              | `ee641b220186`  |
| 1122   | No file              | `ee641b220186`  |
| 1118   | No file              | `ee641b220186`  |
| 1114   | No file              | `ee641b220186`  |
| 1109   | No file              | `ee641b220186`  |
| 1102   | No file              | `ee641b220186`  |
| 1096   | No file              | `ee641b220186`  |
| 1088   | No file              | `ee641b220186`  |
| 1081   | No file              | `ee641b220186`  |
| 1076   | No file              | `ee641b220186`  |
| 1069   | No file              | `ee641b220186`  |
| 1064   | No file              | `ee641b220186`  |
| 1058   | No file              | `ee641b220186`  |
| 1051   | No file              | `ee641b220186`  |
| 1044   | No file              | `ee641b220186`  |
| 1036   | No file              | `ee641b220186`  |
| 1026   | No file              | `ee641b220186`  |
| 1016   | No file              | `ee641b220186`  |
| 1009   | No file              | `ee641b220186`  |
| 1005   | No file              | `ee641b220186`  |
| 1000   | No file              | `ee641b220186`  |
| 998    | No file              | `ee641b220186`  |
| 990    | No file              | `ee641b220186`  |
| 979    | No file              | `ee641b220186`  |
| 972    | No file              | `ee641b220186`  |
| 963    | No file              | `ee641b220186`  |
| 955    | No file              | `ee641b220186`  |
| 946    | No file              | `ee641b220186`  |
| 938    | No file              | `ee641b220186`  |
| 927    | No file              | `ee641b220186`  |
| 911    | No file              | `ee641b220186`  |
| 904    | No file              | `ee641b220186`  |
| 899    | No file              | `ee641b220186`  |
| 894    | No file              | `ee641b220186`  |
| 885    | No file              | `ee641b220186`  |
| 879    | No file              | `ee641b220186`  |
| 872    | No file              | `ee641b220186`  |
| 864    | No file              | `ee641b220186`  |
| 855    | No file              | `ee641b220186`  |
| 853    | No file              | `ee641b220186`  |
| 845    | No file              | `ee641b220186`  |
| 837    | No file              | `ee641b220186`  |
| 829    | No file              | `ee641b220186`  |
| 822    | No file              | `ee641b220186`  |
| 814    | No file              | `ee641b220186`  |
| 805    | No file              | `ee641b220186`  |
| 794    | No file              | `ee641b220186`  |
| 787    | No file              | `ee641b220186`  |
| 780    | No file              | `ee641b220186`  |
| 771    | No file              | `ee641b220186`  |
| 760    | No file              | `ee641b220186`  |
| 748    | No file              | `ee641b220186`  |
| 741    | No file              | `ee641b220186`  |
| 736    | No file              | `ee641b220186`  |
| 731    | No file              | `ee641b220186`  |
| 723    | No file              | `ee641b220186`  |
| 711    | No file              | `ee641b220186`  |
| 707    | No file              | `ee641b220186`  |
| 697    | No file              | `ee641b220186`  |
| 689    | No file              | `ee641b220186`  |
| 683    | No file              | `ee641b220186`  |
| 678    | No file              | `ee641b220186`  |
| 670    | No file              | `ee641b220186`  |
| 661    | No file              | `ee641b220186`  |
| 656    | No file              | `ee641b220186`  |
| 652    | No file              | `ee641b220186`  |
| 643    | No file              | `ee641b220186`  |
| 637    | No file              | `ee641b220186`  |
| 630    | No file              | `ee641b220186`  |
| 627    | No file              | `ee641b220186`  |
| 621    | No file              | `ee641b220186`  |
| 617    | No file              | `ee641b220186`  |
| 615    | No file              | `ee641b220186`  |
| 606    | No file              | `ee641b220186`  |
| 599    | No file              | `ee641b220186`  |
| 592    | No file              | `ee641b220186`  |
| 586    | No file              | `ee641b220186`  |
| 577    | No file              | `ee641b220186`  |
| 569    | No file              | `ee641b220186`  |
| 561    | No file              | `ee641b220186`  |
| 554    | No file              | `ee641b220186`  |
| 542    | No file              | `ee641b220186`  |
| 532    | No file              | `ee641b220186`  |
| 531    | No file              | `ee641b220186`  |
| 526    | No file              | `ee641b220186`  |
| 521    | No file              | `ee641b220186`  |
| 517    | No file              | `ee641b220186`  |
| 510    | No file              | `ee641b220186`  |
| 508    | No file              | `ee641b220186`  |
| 504    | No file              | `ee641b220186`  |
| 497    | No file              | `ee641b220186`  |
| 491    | No file              | `ee641b220186`  |
| 485    | No file              | `ee641b220186`  |
| 478    | No file              | `ee641b220186`  |
| 472    | No file              | `ee641b220186`  |
| 466    | No file              | `ee641b220186`  |
| 457    | No file              | `ee641b220186`  |
| 452    | No file              | `ee641b220186`  |
| 449    | No file              | `ee641b220186`  |
| 435    | No file              | `ee641b220186`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                              |
| ----------------------------- | -------- | ----------------------------------------------------------------- |
| `minigamerewardoffset.dbss`   | Optional | `minigame_key -> (data_offset, data_size)` index; the rows are fixed size and can be walked without it |
| [`itemmaingroup.bss`](itemmaingroup_bss.md) | Optional | The drop group a `drop_group` names; the handler links each group to its row |
| `itemsubgroup.dbss`, `itemsubgroupoffset.dbss` | Optional | The items of the drop group's subgroups |

Item names come from LOC type 0.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `3` on client 3474           |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (13 bytes)

| Offset  | Type | Field              | Notes                                                                    |
| ------- | ---- | ------------------ | ------------------------------------------------------------------------ |
| `+0x00` | u16  | minigame_key       | Minigame; unique per row, the index key                                  |
| `+0x02` | u16  | minigame_key_dup   | Equal to `minigame_key` in every row; the index's `data_offset` points here |
| `+0x04` | i16  | success_wp         | Energy (WP) on a success; see Open Questions                            |
| `+0x06` | i16  | fail_wp            | Energy (WP) on a failure                                                 |
| `+0x08` | u32  | drop_group         | `itemmaingroup.bss` group a success gives                                |
| `+0x0C` | u8   | check_vehicle_type | `CppEnums.VehicleType` the player must be on: `24`, `25` or `26` (client 3474) |

The rows are stored in key order `3`, `2`, `1` on clients 1784 and 3474.

### `minigamerewardoffset.dbss`

| Offset  | Type              | Field | Notes                                     |
| ------- | ----------------- | ----- | ----------------------------------------- |
| `+0x00` | u32               | count | Equals the `minigamereward.dbss` count    |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row      |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                   |
| ------- | ---- | ------------ | --------------------------------------- |
| `+0x00` | u16  | minigame_key | Row key                                 |
| `+0x02` | u32  | data_offset  | Row start + 2, at `minigame_key_dup`    |
| `+0x06` | u32  | data_size    | Row size - 2: `11` on client 3474       |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on clients 1784 and 3474 every index row points at
the row with its key.

## Layout 1

### Row (11 bytes)

| Offset  | Type | Field              | Notes                                                |
| ------- | ---- | ------------------ | ---------------------------------------------------- |
| `+0x00` | u16  | minigame_key       | Minigame                                             |
| `+0x02` | u16  | minigame_key_dup   | Equal to `minigame_key` in every row                 |
| `+0x04` | i16  | success_wp         | Energy (WP) on a success                             |
| `+0x06` | i16  | fail_wp            | Energy (WP) on a failure                             |
| `+0x08` | u16  | drop_group         | `itemmaingroup.bss` group a success gives            |
| `+0x0A` | u8   | check_vehicle_type | `CppEnums.VehicleType` the player must be on         |

`drop_group` is u16 here and u32 in Layout 2; the index's `data_size` is
`9`.

## Field Names

The row is the 2016 `gc::MiniGameRewardStaticStatus` in member order:
`_key` (u16), `_successWp` (short), `_failWp` (short), `_dropKey` (u16, with
a pointer to its `gc::ItemMainGroupStaticStatus` that the file does not
store) and `_checkVehicleType` (`gc::VehicleType`). The 2016 drop key is
u16, as in Layout 1.

The values match the `MiniGameReward` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `MiniGameKey`, 3 of 3 keys on clients
1784 and 3474 in every column:

| Field                | Column         | Same value (client 1784) | Same value (client 3474) |
| -------------------- | -------------- | ------------------------ | ------------------------ |
| `minigame_key`       | `MiniGameKey`  | 3 of 3                   | 3 of 3                   |
| `success_wp`         | `SuccessWp`    | 3 of 3                   | 3 of 3                   |
| `fail_wp`            | `FailWp`       | 3 of 3                   | 3 of 3                   |
| `drop_group`         | `DropGroup`    | 3 of 3                   | 3 of 3                   |
| `check_vehicle_type` | `CheckVehicle` | 3 of 3                   | 3 of 3                   |

The sheet's developer comment on `MiniGameKey` (`DataSheet_MiniGameReward.xlsm`)
names the keys: `1` 소 (cow), `2` 약탕기 (herbal machine), `3` 추출장
(extractor). They match the vehicle types the rows check: `26` Cow, `24`
QuestObjectHerbalMachines and `25` QuestObjectExtractor in
`CppEnums.VehicleType` (`_common/vehicle_type.py`).

WP is the client's name for energy: `panel_characterinfo_basic_all_3.luac`
writes `getWp()` / `getMaxWp()` into the character window's
`StaticText_Energy` control.

## Notes

- The drop groups on client 3474: 65021 holds subgroups 65021, 49477 and
  49478, which give Milk (9065) and Gathering EXP (350); 65022 gives Black
  Stone Powder (4901) or Rough Stone (4006); 65023 gives one of 11 herbs
  (5401 to 5406, 5421 to 5425).
- On client 3474, minigame `1` has `success_wp` 10 and `fail_wp` 4, the
  other two 5 and 2. The `MiniGameReward` table of a private server on
  client 519 has 5 and 2 for all three keys, with the same drop groups and
  vehicle types.
- The client 794 and 1230 builds do not ship the file.

## Open Questions

### Energy Taken or Given

The sheet calls the columns `SuccessWp` and `FailWp` and both are positive
on every row. The BdoEmu server code on client 519
(`CMMiniGameResult.java`) subtracts `SuccessWp` from the player's energy on
a success, then gives the drop group's items, and subtracts `FailWp` on a
failure. That code is a reconstruction, not Pearl Abyss's server; the client
Lua (`luacscript/x64/widget/minigame/`) only sends the result through
`SetMiniGameResult` and shows no energy change.
