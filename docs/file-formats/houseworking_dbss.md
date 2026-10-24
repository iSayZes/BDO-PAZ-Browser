# `houseworking.dbss` Format

## Purpose

The work a worker can do at a crafting tool installed in a house: one row
per tool installation character (Metal Processing Tool `1001`,
Intermediate Cooking Utensil `1032`) with a list of item exchanges and a
unit production for each. On client 3482 the 17 rows each hold one entry,
exchange `5001` with unit production `3`. Companion `houseworkingoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records         | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | --------------- | --------- |
| 2      | 2726 and later | 3483    | `houseworking.dbss`       | 242   | 17 Work, 17 Row | 8         |
| 2      | 2726 and later | 3483    | `houseworkingoffset.dbss` | 174   | 17 Offset Row   | 10        |
| 1      | 1267 to 2717   | 2717    | `houseworking.dbss`       | 208   | 17 Work, 17 Row | 6         |
| 1      | 1267 to 2717   | 2717    | `houseworkingoffset.dbss` | 174   | 17 Offset Row   | 10        |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 2      | `houseworking.dbss`       | 242 B (100.0%) | 0 B (0.0%) |
| 2      | `houseworkingoffset.dbss` | 174 B (100.0%) | 0 B (0.0%) |
| 1      | `houseworking.dbss`       | 208 B (100.0%) | 0 B (0.0%) |
| 1      | `houseworkingoffset.dbss` | 174 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `6c775673f131`  |
| 3482   | Layout 2 | `6c775673f131`  |
| 3474   | Layout 2 | `6c775673f131`  |
| 3473   | Layout 2 | `6c775673f131`  |
| 3464   | Layout 2 | `6c775673f131`  |
| 3458   | Layout 2 | `6c775673f131`  |
| 3454   | Layout 2 | `6c775673f131`  |
| 3444   | Layout 2 | `6c775673f131`  |
| 3435   | Layout 2 | `6c775673f131`  |
| 3426   | Layout 2 | `6c775673f131`  |
| 3418   | Layout 2 | `6c775673f131`  |
| 3412   | Layout 2 | `6c775673f131`  |
| 3402   | Layout 2 | `6c775673f131`  |
| 3396   | Layout 2 | `6c775673f131`  |
| 3387   | Layout 2 | `6c775673f131`  |
| 3381   | Layout 2 | `6c775673f131`  |
| 3373   | Layout 2 | `6c775673f131`  |
| 3364   | Layout 2 | `6c775673f131`  |
| 3356   | Layout 2 | `6c775673f131`  |
| 3349   | Layout 2 | `6c775673f131`  |
| 3342   | Layout 2 | `6c775673f131`  |
| 3335   | Layout 2 | `6c775673f131`  |
| 3326   | Layout 2 | `6c775673f131`  |
| 3321   | Layout 2 | `6c775673f131`  |
| 3314   | Layout 2 | `6c775673f131`  |
| 3303   | Layout 2 | `6c775673f131`  |
| 3302   | Layout 2 | `6c775673f131`  |
| 3293   | Layout 2 | `6c775673f131`  |
| 3283   | Layout 2 | `6c775673f131`  |
| 3275   | Layout 2 | `6c775673f131`  |
| 3267   | Layout 2 | `6c775673f131`  |
| 3258   | Layout 2 | `6c775673f131`  |
| 3251   | Layout 2 | `6c775673f131`  |
| 3242   | Layout 2 | `6c775673f131`  |
| 3235   | Layout 2 | `6c775673f131`  |
| 3229   | Layout 2 | `6c775673f131`  |
| 3212   | Layout 2 | `6c775673f131`  |
| 3203   | Layout 2 | `6c775673f131`  |
| 3193   | Layout 2 | `6c775673f131`  |
| 3186   | Layout 2 | `6c775673f131`  |
| 3177   | Layout 2 | `6c775673f131`  |
| 3169   | Layout 2 | `6c775673f131`  |
| 3158   | Layout 2 | `6c775673f131`  |
| 3151   | Layout 2 | `6c775673f131`  |
| 3144   | Layout 2 | `6c775673f131`  |
| 3133   | Layout 2 | `6c775673f131`  |
| 3125   | Layout 2 | `6c775673f131`  |
| 3118   | Layout 2 | `6c775673f131`  |
| 3111   | Layout 2 | `6c775673f131`  |
| 3103   | Layout 2 | `6c775673f131`  |
| 3095   | Layout 2 | `6c775673f131`  |
| 3086   | Layout 2 | `6c775673f131`  |
| 3072   | Layout 2 | `6c775673f131`  |
| 3062   | Layout 2 | `6c775673f131`  |
| 3052   | Layout 2 | `6c775673f131`  |
| 3045   | Layout 2 | `6c775673f131`  |
| 3037   | Layout 2 | `6c775673f131`  |
| 3030   | Layout 2 | `6c775673f131`  |
| 3021   | Layout 2 | `6c775673f131`  |
| 3012   | Layout 2 | `6c775673f131`  |
| 3002   | Layout 2 | `6c775673f131`  |
| 2995   | Layout 2 | `6c775673f131`  |
| 2987   | Layout 2 | `6c775673f131`  |
| 2978   | Layout 2 | `6c775673f131`  |
| 2970   | Layout 2 | `6c775673f131`  |
| 2959   | Layout 2 | `6c775673f131`  |
| 2951   | Layout 2 | `6c775673f131`  |
| 2942   | Layout 2 | `6c775673f131`  |
| 2935   | Layout 2 | `6c775673f131`  |
| 2932   | Layout 2 | `6c775673f131`  |
| 2923   | Layout 2 | `6c775673f131`  |
| 2919   | Layout 2 | `6c775673f131`  |
| 2907   | Layout 2 | `6c775673f131`  |
| 2900   | Layout 2 | `6c775673f131`  |
| 2891   | Layout 2 | `6c775673f131`  |
| 2882   | Layout 2 | `6c775673f131`  |
| 2872   | Layout 2 | `6c775673f131`  |
| 2863   | Layout 2 | `6c775673f131`  |
| 2855   | Layout 2 | `6c775673f131`  |
| 2849   | Layout 2 | `6c775673f131`  |
| 2844   | Layout 2 | `6c775673f131`  |
| 2834   | Layout 2 | `6c775673f131`  |
| 2825   | Layout 2 | `6c775673f131`  |
| 2819   | Layout 2 | `6c775673f131`  |
| 2811   | Layout 2 | `6c775673f131`  |
| 2803   | Layout 2 | `6c775673f131`  |
| 2794   | Layout 2 | `6c775673f131`  |
| 2783   | Layout 2 | `6c775673f131`  |
| 2774   | Layout 2 | `6c775673f131`  |
| 2765   | Layout 2 | `6c775673f131`  |
| 2756   | Layout 2 | `6c775673f131`  |
| 2750   | Layout 2 | `6c775673f131`  |
| 2743   | Layout 2 | `6c775673f131`  |
| 2736   | Layout 2 | `6c775673f131`  |
| 2726   | Layout 2 | `6c775673f131`  |
| 2717   | Layout 1 | `6c775673f131`  |
| 2709   | Layout 1 | `6c775673f131`  |
| 2703   | Layout 1 | `6c775673f131`  |
| 2695   | Layout 1 | `6c775673f131`  |
| 2684   | Layout 1 | `6c775673f131`  |
| 2672   | Layout 1 | `6c775673f131`  |
| 2665   | Layout 1 | `6c775673f131`  |
| 2657   | Layout 1 | `6c775673f131`  |
| 2649   | Layout 1 | `6c775673f131`  |
| 2644   | Layout 1 | `6c775673f131`  |
| 2637   | Layout 1 | `6c775673f131`  |
| 2629   | Layout 1 | `6c775673f131`  |
| 2619   | Layout 1 | `6c775673f131`  |
| 2612   | Layout 1 | `6c775673f131`  |
| 2606   | Layout 1 | `6c775673f131`  |
| 2602   | Layout 1 | `6c775673f131`  |
| 2601   | Layout 1 | `6c775673f131`  |
| 2592   | Layout 1 | `6c775673f131`  |
| 2583   | Layout 1 | `6c775673f131`  |
| 2575   | Layout 1 | `6c775673f131`  |
| 2567   | Layout 1 | `6c775673f131`  |
| 2560   | Layout 1 | `6c775673f131`  |
| 2553   | Layout 1 | `6c775673f131`  |
| 2545   | Layout 1 | `6c775673f131`  |
| 2538   | Layout 1 | `6c775673f131`  |
| 2529   | Layout 1 | `6c775673f131`  |
| 2519   | Layout 1 | `6c775673f131`  |
| 2513   | Layout 1 | `6c775673f131`  |
| 2510   | Layout 1 | `6c775673f131`  |
| 2507   | Layout 1 | `6c775673f131`  |
| 2503   | Layout 1 | `6c775673f131`  |
| 2498   | Layout 1 | `6c775673f131`  |
| 2492   | Layout 1 | `6c775673f131`  |
| 2487   | Layout 1 | `6c775673f131`  |
| 2480   | Layout 1 | `6c775673f131`  |
| 2474   | Layout 1 | `6c775673f131`  |
| 2468   | Layout 1 | `6c775673f131`  |
| 2460   | Layout 1 | `6c775673f131`  |
| 2453   | Layout 1 | `6c775673f131`  |
| 2444   | Layout 1 | `6c775673f131`  |
| 2438   | Layout 1 | `6c775673f131`  |
| 2434   | Layout 1 | `6c775673f131`  |
| 2429   | Layout 1 | `6c775673f131`  |
| 2421   | Layout 1 | `6c775673f131`  |
| 2414   | Layout 1 | `6c775673f131`  |
| 2407   | Layout 1 | `6c775673f131`  |
| 2401   | Layout 1 | `6c775673f131`  |
| 2397   | Layout 1 | `6c775673f131`  |
| 2393   | Layout 1 | `6c775673f131`  |
| 2384   | Layout 1 | `6c775673f131`  |
| 2378   | Layout 1 | `6c775673f131`  |
| 2372   | Layout 1 | `6c775673f131`  |
| 2358   | Layout 1 | `6c775673f131`  |
| 2352   | Layout 1 | `6c775673f131`  |
| 2347   | Layout 1 | `6c775673f131`  |
| 2343   | Layout 1 | `6c775673f131`  |
| 2335   | Layout 1 | `6c775673f131`  |
| 2327   | Layout 1 | `6c775673f131`  |
| 2324   | Layout 1 | `6c775673f131`  |
| 2319   | Layout 1 | `6c775673f131`  |
| 2313   | Layout 1 | `6c775673f131`  |
| 2308   | Layout 1 | `6c775673f131`  |
| 2302   | Layout 1 | `6c775673f131`  |
| 2295   | Layout 1 | `6c775673f131`  |
| 2290   | Layout 1 | `6c775673f131`  |
| 2284   | Layout 1 | `6c775673f131`  |
| 2276   | Layout 1 | `6c775673f131`  |
| 2269   | Layout 1 | `6c775673f131`  |
| 2259   | Layout 1 | `6c775673f131`  |
| 2250   | Layout 1 | `6c775673f131`  |
| 2243   | Layout 1 | `6c775673f131`  |
| 2235   | Layout 1 | `6c775673f131`  |
| 2229   | Layout 1 | `6c775673f131`  |
| 2224   | Layout 1 | `6c775673f131`  |
| 2218   | Layout 1 | `6c775673f131`  |
| 2215   | Layout 1 | `6c775673f131`  |
| 2207   | Layout 1 | `6c775673f131`  |
| 2203   | Layout 1 | `6c775673f131`  |
| 2196   | Layout 1 | `6c775673f131`  |
| 2192   | Layout 1 | `6c775673f131`  |
| 2189   | Layout 1 | `6c775673f131`  |
| 2183   | Layout 1 | `6c775673f131`  |
| 2179   | Layout 1 | `6c775673f131`  |
| 2171   | Layout 1 | `6c775673f131`  |
| 2163   | Layout 1 | `6c775673f131`  |
| 2156   | Layout 1 | `6c775673f131`  |
| 2151   | Layout 1 | `6c775673f131`  |
| 2147   | Layout 1 | `6c775673f131`  |
| 2142   | Layout 1 | `6c775673f131`  |
| 2138   | Layout 1 | `6c775673f131`  |
| 2134   | Layout 1 | `6c775673f131`  |
| 2130   | Layout 1 | `6c775673f131`  |
| 2122   | Layout 1 | `6c775673f131`  |
| 2107   | Layout 1 | `6c775673f131`  |
| 2098   | Layout 1 | `6c775673f131`  |
| 2089   | Layout 1 | `6c775673f131`  |
| 2081   | Layout 1 | `6c775673f131`  |
| 2073   | Layout 1 | `6c775673f131`  |
| 2067   | Layout 1 | `6c775673f131`  |
| 2063   | Layout 1 | `6c775673f131`  |
| 2059   | Layout 1 | `6c775673f131`  |
| 2052   | Layout 1 | `6c775673f131`  |
| 2044   | Layout 1 | `6c775673f131`  |
| 2039   | Layout 1 | `6c775673f131`  |
| 2032   | Layout 1 | `6c775673f131`  |
| 2025   | Layout 1 | `6c775673f131`  |
| 2011   | Layout 1 | `6c775673f131`  |
| 2005   | Layout 1 | `6c775673f131`  |
| 2000   | Layout 1 | `6c775673f131`  |
| 1996   | Layout 1 | `6c775673f131`  |
| 1991   | Layout 1 | `6c775673f131`  |
| 1985   | Layout 1 | `6c775673f131`  |
| 1980   | Layout 1 | `6c775673f131`  |
| 1969   | Layout 1 | `6c775673f131`  |
| 1964   | Layout 1 | `6c775673f131`  |
| 1958   | Layout 1 | `6c775673f131`  |
| 1950   | Layout 1 | `6c775673f131`  |
| 1945   | Layout 1 | `6c775673f131`  |
| 1937   | Layout 1 | `6c775673f131`  |
| 1933   | Layout 1 | `6c775673f131`  |
| 1927   | Layout 1 | `6c775673f131`  |
| 1921   | Layout 1 | `6c775673f131`  |
| 1914   | Layout 1 | `6c775673f131`  |
| 1908   | Layout 1 | `6c775673f131`  |
| 1897   | Layout 1 | `6c775673f131`  |
| 1892   | Layout 1 | `6c775673f131`  |
| 1886   | Layout 1 | `6c775673f131`  |
| 1881   | Layout 1 | `6c775673f131`  |
| 1871   | Layout 1 | `6c775673f131`  |
| 1866   | Layout 1 | `6c775673f131`  |
| 1862   | Layout 1 | `6c775673f131`  |
| 1854   | Layout 1 | `6c775673f131`  |
| 1846   | Layout 1 | `6c775673f131`  |
| 1838   | Layout 1 | `6c775673f131`  |
| 1832   | Layout 1 | `6c775673f131`  |
| 1826   | Layout 1 | `6c775673f131`  |
| 1822   | Layout 1 | `6c775673f131`  |
| 1818   | Layout 1 | `6c775673f131`  |
| 1804   | Layout 1 | `6c775673f131`  |
| 1794   | Layout 1 | `6c775673f131`  |
| 1790   | Layout 1 | `6c775673f131`  |
| 1784   | Layout 1 | `6c775673f131`  |
| 1774   | Layout 1 | `6c775673f131`  |
| 1771   | Layout 1 | `6c775673f131`  |
| 1762   | Layout 1 | `6c775673f131`  |
| 1759   | Layout 1 | `6c775673f131`  |
| 1754   | Layout 1 | `6c775673f131`  |
| 1749   | Layout 1 | `6c775673f131`  |
| 1743   | Layout 1 | `6c775673f131`  |
| 1737   | Layout 1 | `6c775673f131`  |
| 1731   | Layout 1 | `6c775673f131`  |
| 1725   | Layout 1 | `6c775673f131`  |
| 1717   | Layout 1 | `6c775673f131`  |
| 1710   | Layout 1 | `6c775673f131`  |
| 1704   | Layout 1 | `6c775673f131`  |
| 1698   | Layout 1 | `6c775673f131`  |
| 1690   | Layout 1 | `6c775673f131`  |
| 1685   | Layout 1 | `6c775673f131`  |
| 1680   | Layout 1 | `6c775673f131`  |
| 1674   | Layout 1 | `6c775673f131`  |
| 1668   | Layout 1 | `6c775673f131`  |
| 1659   | Layout 1 | `6c775673f131`  |
| 1649   | Layout 1 | `6c775673f131`  |
| 1642   | Layout 1 | `6c775673f131`  |
| 1636   | Layout 1 | `6c775673f131`  |
| 1628   | Layout 1 | `6c775673f131`  |
| 1622   | Layout 1 | `6c775673f131`  |
| 1614   | Layout 1 | `6c775673f131`  |
| 1608   | Layout 1 | `6c775673f131`  |
| 1602   | Layout 1 | `6c775673f131`  |
| 1598   | Layout 1 | `6c775673f131`  |
| 1594   | Layout 1 | `6c775673f131`  |
| 1590   | Layout 1 | `6c775673f131`  |
| 1587   | Layout 1 | `6c775673f131`  |
| 1584   | Layout 1 | `6c775673f131`  |
| 1579   | Layout 1 | `6c775673f131`  |
| 1572   | Layout 1 | `6c775673f131`  |
| 1565   | Layout 1 | `6c775673f131`  |
| 1559   | Layout 1 | `6c775673f131`  |
| 1554   | Layout 1 | `6c775673f131`  |
| 1547   | Layout 1 | `6c775673f131`  |
| 1537   | Layout 1 | `6c775673f131`  |
| 1529   | Layout 1 | `6c775673f131`  |
| 1524   | Layout 1 | `6c775673f131`  |
| 1519   | Layout 1 | `6c775673f131`  |
| 1509   | Layout 1 | `6c775673f131`  |
| 1506   | Layout 1 | `6c775673f131`  |
| 1504   | Layout 1 | `6c775673f131`  |
| 1500   | Layout 1 | `6c775673f131`  |
| 1493   | Layout 1 | `6c775673f131`  |
| 1489   | Layout 1 | `6c775673f131`  |
| 1485   | Layout 1 | `6c775673f131`  |
| 1481   | Layout 1 | `6c775673f131`  |
| 1474   | Layout 1 | `6c775673f131`  |
| 1466   | Layout 1 | `6c775673f131`  |
| 1462   | Layout 1 | `6c775673f131`  |
| 1459   | Layout 1 | `6c775673f131`  |
| 1453   | Layout 1 | `6c775673f131`  |
| 1450   | Layout 1 | `6c775673f131`  |
| 1445   | Layout 1 | `6c775673f131`  |
| 1439   | Layout 1 | `6c775673f131`  |
| 1433   | Layout 1 | `6c775673f131`  |
| 1430   | Layout 1 | `6c775673f131`  |
| 1426   | Layout 1 | `6c775673f131`  |
| 1421   | Layout 1 | `6c775673f131`  |
| 1417   | Layout 1 | `6c775673f131`  |
| 1416   | Layout 1 | `6c775673f131`  |
| 1409   | Layout 1 | `6c775673f131`  |
| 1405   | Layout 1 | `6c775673f131`  |
| 1401   | Layout 1 | `6c775673f131`  |
| 1396   | Layout 1 | `6c775673f131`  |
| 1391   | Layout 1 | `6c775673f131`  |
| 1390   | Layout 1 | `6c775673f131`  |
| 1386   | Layout 1 | `6c775673f131`  |
| 1381   | Layout 1 | `6c775673f131`  |
| 1379   | Layout 1 | `6c775673f131`  |
| 1372   | Layout 1 | `6c775673f131`  |
| 1366   | Layout 1 | `6c775673f131`  |
| 1364   | Layout 1 | `6c775673f131`  |
| 1363   | Layout 1 | `6c775673f131`  |
| 1360   | Layout 1 | `6c775673f131`  |
| 1358   | Layout 1 | `6c775673f131`  |
| 1355   | Layout 1 | `6c775673f131`  |
| 1351   | Layout 1 | `6c775673f131`  |
| 1348   | Layout 1 | `6c775673f131`  |
| 1346   | Layout 1 | `6c775673f131`  |
| 1341   | Layout 1 | `6c775673f131`  |
| 1340   | Layout 1 | `6c775673f131`  |
| 1338   | Layout 1 | `6c775673f131`  |
| 1335   | Layout 1 | `6c775673f131`  |
| 1333   | Layout 1 | `6c775673f131`  |
| 1329   | Layout 1 | `6c775673f131`  |
| 1327   | Layout 1 | `6c775673f131`  |
| 1324   | Layout 1 | `6c775673f131`  |
| 1321   | Layout 1 | `6c775673f131`  |
| 1319   | Layout 1 | `6c775673f131`  |
| 1318   | Layout 1 | `6c775673f131`  |
| 1316   | Layout 1 | `6c775673f131`  |
| 1313   | Layout 1 | `6c775673f131`  |
| 1311   | Layout 1 | `6c775673f131`  |
| 1309   | Layout 1 | `6c775673f131`  |
| 1304   | Layout 1 | `6c775673f131`  |
| 1292   | Layout 1 | `6c775673f131`  |
| 1286   | Layout 1 | `6c775673f131`  |
| 1280   | Layout 1 | `6c775673f131`  |
| 1276   | Layout 1 | `6c775673f131`  |
| 1267   | Layout 1 | `6c775673f131`  |
| 1261   | No file  | `6c775673f131`  |
| 1256   | No file  | `6c775673f131`  |
| 1250   | No file  | `6c775673f131`  |
| 1246   | No file  | `6c775673f131`  |
| 1239   | No file  | `6c775673f131`  |
| 1230   | No file  | `6c775673f131`  |
| 1226   | No file  | `6c775673f131`  |
| 1220   | No file  | `6c775673f131`  |
| 1217   | No file  | `6c775673f131`  |
| 1211   | No file  | `6c775673f131`  |
| 1210   | No file  | `6c775673f131`  |
| 1208   | No file  | `6c775673f131`  |
| 1203   | No file  | `6c775673f131`  |
| 1197   | No file  | `6c775673f131`  |
| 1194   | No file  | `6c775673f131`  |
| 1192   | No file  | `6c775673f131`  |
| 1187   | No file  | `6c775673f131`  |
| 1183   | No file  | `6c775673f131`  |
| 1177   | No file  | `6c775673f131`  |
| 1173   | No file  | `6c775673f131`  |
| 1167   | No file  | `6c775673f131`  |
| 1164   | No file  | `6c775673f131`  |
| 1156   | No file  | `6c775673f131`  |
| 1149   | No file  | `6c775673f131`  |
| 1144   | No file  | `6c775673f131`  |
| 1137   | No file  | `6c775673f131`  |
| 1132   | No file  | `6c775673f131`  |
| 1127   | No file  | `6c775673f131`  |
| 1122   | No file  | `6c775673f131`  |
| 1118   | No file  | `6c775673f131`  |
| 1114   | No file  | `6c775673f131`  |
| 1109   | No file  | `6c775673f131`  |
| 1102   | No file  | `6c775673f131`  |
| 1096   | No file  | `6c775673f131`  |
| 1088   | No file  | `6c775673f131`  |
| 1081   | No file  | `6c775673f131`  |
| 1076   | No file  | `6c775673f131`  |
| 1069   | No file  | `6c775673f131`  |
| 1064   | No file  | `6c775673f131`  |
| 1058   | No file  | `6c775673f131`  |
| 1051   | No file  | `6c775673f131`  |
| 1044   | No file  | `6c775673f131`  |
| 1036   | No file  | `6c775673f131`  |
| 1026   | No file  | `6c775673f131`  |
| 1016   | No file  | `6c775673f131`  |
| 1009   | No file  | `6c775673f131`  |
| 1005   | No file  | `6c775673f131`  |
| 1000   | No file  | `6c775673f131`  |
| 998    | No file  | `6c775673f131`  |
| 990    | No file  | `6c775673f131`  |
| 979    | No file  | `6c775673f131`  |
| 972    | No file  | `6c775673f131`  |
| 963    | No file  | `6c775673f131`  |
| 955    | No file  | `6c775673f131`  |
| 946    | No file  | `6c775673f131`  |
| 938    | No file  | `6c775673f131`  |
| 927    | No file  | `6c775673f131`  |
| 911    | No file  | `6c775673f131`  |
| 904    | No file  | `6c775673f131`  |
| 899    | No file  | `6c775673f131`  |
| 894    | No file  | `6c775673f131`  |
| 885    | No file  | `6c775673f131`  |
| 879    | No file  | `6c775673f131`  |
| 872    | No file  | `6c775673f131`  |
| 864    | No file  | `6c775673f131`  |
| 855    | No file  | `6c775673f131`  |
| 853    | No file  | `6c775673f131`  |
| 845    | No file  | `6c775673f131`  |
| 837    | No file  | `6c775673f131`  |
| 829    | No file  | `6c775673f131`  |
| 822    | No file  | `6c775673f131`  |
| 814    | No file  | `6c775673f131`  |
| 805    | No file  | `6c775673f131`  |
| 794    | No file  | `6c775673f131`  |
| 787    | No file  | `6c775673f131`  |
| 780    | No file  | `6c775673f131`  |
| 771    | No file  | `6c775673f131`  |
| 760    | No file  | `6c775673f131`  |
| 748    | No file  | `6c775673f131`  |
| 741    | No file  | `6c775673f131`  |
| 736    | No file  | `6c775673f131`  |
| 731    | No file  | `6c775673f131`  |
| 723    | No file  | `6c775673f131`  |
| 711    | No file  | `6c775673f131`  |
| 707    | No file  | `6c775673f131`  |
| 697    | No file  | `6c775673f131`  |
| 689    | No file  | `6c775673f131`  |
| 683    | No file  | `6c775673f131`  |
| 678    | No file  | `6c775673f131`  |
| 670    | No file  | `6c775673f131`  |
| 661    | No file  | `6c775673f131`  |
| 656    | No file  | `6c775673f131`  |
| 652    | No file  | `6c775673f131`  |
| 643    | No file  | `6c775673f131`  |
| 637    | No file  | `6c775673f131`  |
| 630    | No file  | `6c775673f131`  |
| 627    | No file  | `6c775673f131`  |
| 621    | No file  | `6c775673f131`  |
| 617    | No file  | `6c775673f131`  |
| 615    | No file  | `6c775673f131`  |
| 606    | No file  | `6c775673f131`  |
| 599    | No file  | `6c775673f131`  |
| 592    | No file  | `6c775673f131`  |
| 586    | No file  | `6c775673f131`  |
| 577    | No file  | `6c775673f131`  |
| 569    | No file  | `6c775673f131`  |
| 561    | No file  | `6c775673f131`  |
| 554    | No file  | `6c775673f131`  |
| 542    | No file  | `6c775673f131`  |
| 532    | No file  | `6c775673f131`  |
| 531    | No file  | `6c775673f131`  |
| 526    | No file  | `6c775673f131`  |
| 521    | No file  | `6c775673f131`  |
| 517    | No file  | `6c775673f131`  |
| 510    | No file  | `6c775673f131`  |
| 508    | No file  | `6c775673f131`  |
| 504    | No file  | `6c775673f131`  |
| 497    | No file  | `6c775673f131`  |
| 491    | No file  | `6c775673f131`  |
| 485    | No file  | `6c775673f131`  |
| 478    | No file  | `6c775673f131`  |
| 472    | No file  | `6c775673f131`  |
| 466    | No file  | `6c775673f131`  |
| 457    | No file  | `6c775673f131`  |
| 452    | No file  | `6c775673f131`  |
| 449    | No file  | `6c775673f131`  |
| 435    | No file  | `6c775673f131`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                      |
| ---------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `houseworkingoffset.dbss`    | Optional | `install_object_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a tool key without a row shows as plain text           |
| `languagedata_en.loc`        | Optional | Tool names (type 6) and exchange names (type 24)                                           |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3482 the file is 4 + 17 x 14 = 242 bytes.

### Row (variable: 6 bytes + works)

| Offset       | Type             | Field              | Notes                                                                 |
| ------------ | ---------------- | ------------------ | --------------------------------------------------------------------- |
| `+0x00`      | u32              | work_count         | Number of `works`; `1` on every row (clients 1784 and 3482)           |
| `+0x04`      | Work[work_count] | works              | See Work                                                              |
| `works+0x00` | u16              | install_object_key | Row key: the tool installation, a `characterstatic.dbss` character     |

The rows are in no key order; client 3482 opens with 1032, 1028, 1025.

### Work (8 bytes)

| Offset  | Type | Field           | Notes                                                                                   |
| ------- | ---- | --------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | exchange_key    | An [`itemexchangesource.bss`](itemexchangesource_bss.md) key; `5001` (Veid Longsword) on every row |
| `+0x04` | u32  | unit_production | `3` on every row                                                                        |

### `houseworkingoffset.dbss`

Bare offset table into `houseworking.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `houseworking.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (10 bytes)

| Offset  | Type | Field              | Notes                                                      |
| ------- | ---- | ------------------ | ---------------------------------------------------------- |
| `+0x00` | u16  | install_object_key | Key of the row it points at                                |
| `+0x02` | u32  | data_offset        | Absolute offset of the row in `houseworking.dbss`, at `work_count` |
| `+0x06` | u32  | data_size          | The whole row: `14` on every row of client 3482            |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on clients 1784 and 3482 every index row points at
the row whose `install_object_key` is its key.

## Layout 1

The exchange key is a u16, so a work entry is 6 bytes and a row 12
(`data_size` `12`). Only the Work differs from Layout 2.

### Work (6 bytes)

| Offset  | Type | Field           | Notes                                    |
| ------- | ---- | --------------- | ---------------------------------------- |
| `+0x00` | u16  | exchange_key    | `5001` on every row (client 1784)        |
| `+0x02` | u32  | unit_production | `3` on every row (client 1784)           |

## Field Names

The `PlantHouseWorking_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `InstallObjectKey`,
`ExchangeKey` and `UnitProduction`, 17 rows. The 2016
`gc::HouseWorkingStaticStatus` holds `_key` (u16) and `_availableWorkList`,
a map of u16 exchange key to `gc::PlantWorking` (`_key`, `_unitProduction`);
the client file stores the map as `work_count` and its entries, before the
key.

| Field              | Column             | Same value (client 1784) | Same value (client 3482) |
| ------------------ | ------------------ | ------------------------ | ------------------------ |
| install_object_key | `InstallObjectKey` | 17 of 17                 | 17 of 17                 |
| exchange_key       | `ExchangeKey`      | 17 of 17                 | 17 of 17                 |
| unit_production    | `UnitProduction`   | 17 of 17                 | 17 of 17                 |

## Notes

- The 17 keys are tool installations (LOC type 6): Metal Processing Tool
  (`1001`) to Furniture Crafting Tool (`1008`), Crafting Tool (`1025`),
  Cooking Utensil (`1028`), Intermediate Cooking Utensil (`1032`) and
  `1521` to `1525` and `1527`, Weapon Refining Tool (Metal) to Masonry Tool.
- Exchange `5001` is the Veid Longsword exchange of
  [`itemexchangesource.bss`](itemexchangesource_bss.md); every row of
  clients 1784 and 3482 holds it.
- The worker Lua (`new_worldmap_household.luac`,
  `panel_worldmap_housemanagement_renew.luac` and four more) lists the
  workers of a house through `ToClient_getHouseWorkingWorkerList(houseInfo)`
  and `ToClient_getHouseWorkingWorkerByIndex(houseInfo, index)`; those calls
  take a house, not a tool key, and no Lua call names this table's fields.
