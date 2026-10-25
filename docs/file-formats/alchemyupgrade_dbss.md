# `alchemyupgrade.dbss` Format

## Purpose

The materials that polish an alchemy stone in the Polishing tab of the
alchemy stone window, per alchemy stone type. A row is the stone type, the
material item and the EXP one unit of that material adds to the stone.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                        | Bytes | Records                      | Row bytes |
| ------ | -------------- | --------------------------- | ----- | ---------------------------- | --------- |
| 1      | 1256 and later | `alchemyupgrade.dbss`       | 2,028 | 166 Row, 8 Group             | 12        |
| 1      | 1256 and later | `alchemyupgradeoffset.dbss` | 2,028 | 166 Index Row, 8 Index Group | 12        |

| Layout | File                        | Known            | Unknown    |
| ------ | --------------------------- | ---------------- | ---------- |
| 1      | `alchemyupgrade.dbss`       | 2,028 B (100.0%) | 0 B (0.0%) |
| 1      | `alchemyupgradeoffset.dbss` | 2,028 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `47adb7288947`  |
| 3482   | Layout 1 | `47adb7288947`  |
| 3474   | Layout 1 | `47adb7288947`  |
| 3473   | Layout 1 | `47adb7288947`  |
| 3464   | Layout 1 | `47adb7288947`  |
| 3458   | Layout 1 | `47adb7288947`  |
| 3454   | Layout 1 | `47adb7288947`  |
| 3444   | Layout 1 | `47adb7288947`  |
| 3435   | Layout 1 | `47adb7288947`  |
| 3426   | Layout 1 | `47adb7288947`  |
| 3418   | Layout 1 | `47adb7288947`  |
| 3412   | Layout 1 | `47adb7288947`  |
| 3402   | Layout 1 | `47adb7288947`  |
| 3396   | Layout 1 | `47adb7288947`  |
| 3387   | Layout 1 | `47adb7288947`  |
| 3381   | Layout 1 | `47adb7288947`  |
| 3373   | Layout 1 | `47adb7288947`  |
| 3364   | Layout 1 | `47adb7288947`  |
| 3356   | Layout 1 | `47adb7288947`  |
| 3349   | Layout 1 | `47adb7288947`  |
| 3342   | Layout 1 | `47adb7288947`  |
| 3335   | Layout 1 | `47adb7288947`  |
| 3326   | Layout 1 | `47adb7288947`  |
| 3321   | Layout 1 | `47adb7288947`  |
| 3314   | Layout 1 | `47adb7288947`  |
| 3303   | Layout 1 | `47adb7288947`  |
| 3302   | Layout 1 | `47adb7288947`  |
| 3293   | Layout 1 | `47adb7288947`  |
| 3283   | Layout 1 | `47adb7288947`  |
| 3275   | Layout 1 | `47adb7288947`  |
| 3267   | Layout 1 | `47adb7288947`  |
| 3258   | Layout 1 | `47adb7288947`  |
| 3251   | Layout 1 | `47adb7288947`  |
| 3242   | Layout 1 | `47adb7288947`  |
| 3235   | Layout 1 | `47adb7288947`  |
| 3229   | Layout 1 | `47adb7288947`  |
| 3212   | Layout 1 | `47adb7288947`  |
| 3203   | Layout 1 | `47adb7288947`  |
| 3193   | Layout 1 | `47adb7288947`  |
| 3186   | Layout 1 | `47adb7288947`  |
| 3177   | Layout 1 | `47adb7288947`  |
| 3169   | Layout 1 | `47adb7288947`  |
| 3158   | Layout 1 | `47adb7288947`  |
| 3151   | Layout 1 | `47adb7288947`  |
| 3144   | Layout 1 | `47adb7288947`  |
| 3133   | Layout 1 | `47adb7288947`  |
| 3125   | Layout 1 | `47adb7288947`  |
| 3118   | Layout 1 | `47adb7288947`  |
| 3111   | Layout 1 | `47adb7288947`  |
| 3103   | Layout 1 | `47adb7288947`  |
| 3095   | Layout 1 | `47adb7288947`  |
| 3086   | Layout 1 | `47adb7288947`  |
| 3072   | Layout 1 | `47adb7288947`  |
| 3062   | Layout 1 | `47adb7288947`  |
| 3052   | Layout 1 | `47adb7288947`  |
| 3045   | Layout 1 | `47adb7288947`  |
| 3037   | Layout 1 | `47adb7288947`  |
| 3030   | Layout 1 | `47adb7288947`  |
| 3021   | Layout 1 | `47adb7288947`  |
| 3012   | Layout 1 | `47adb7288947`  |
| 3002   | Layout 1 | `47adb7288947`  |
| 2995   | Layout 1 | `47adb7288947`  |
| 2987   | Layout 1 | `47adb7288947`  |
| 2978   | Layout 1 | `47adb7288947`  |
| 2970   | Layout 1 | `47adb7288947`  |
| 2959   | Layout 1 | `47adb7288947`  |
| 2951   | Layout 1 | `47adb7288947`  |
| 2942   | Layout 1 | `47adb7288947`  |
| 2935   | Layout 1 | `47adb7288947`  |
| 2932   | Layout 1 | `47adb7288947`  |
| 2923   | Layout 1 | `47adb7288947`  |
| 2919   | Layout 1 | `47adb7288947`  |
| 2907   | Layout 1 | `47adb7288947`  |
| 2900   | Layout 1 | `47adb7288947`  |
| 2891   | Layout 1 | `47adb7288947`  |
| 2882   | Layout 1 | `47adb7288947`  |
| 2872   | Layout 1 | `47adb7288947`  |
| 2863   | Layout 1 | `47adb7288947`  |
| 2855   | Layout 1 | `47adb7288947`  |
| 2849   | Layout 1 | `47adb7288947`  |
| 2844   | Layout 1 | `47adb7288947`  |
| 2834   | Layout 1 | `47adb7288947`  |
| 2825   | Layout 1 | `47adb7288947`  |
| 2819   | Layout 1 | `47adb7288947`  |
| 2811   | Layout 1 | `47adb7288947`  |
| 2803   | Layout 1 | `47adb7288947`  |
| 2794   | Layout 1 | `47adb7288947`  |
| 2783   | Layout 1 | `47adb7288947`  |
| 2774   | Layout 1 | `47adb7288947`  |
| 2765   | Layout 1 | `47adb7288947`  |
| 2756   | Layout 1 | `47adb7288947`  |
| 2750   | Layout 1 | `47adb7288947`  |
| 2743   | Layout 1 | `47adb7288947`  |
| 2736   | Layout 1 | `47adb7288947`  |
| 2726   | Layout 1 | `47adb7288947`  |
| 2717   | Layout 1 | `47adb7288947`  |
| 2709   | Layout 1 | `47adb7288947`  |
| 2703   | Layout 1 | `47adb7288947`  |
| 2695   | Layout 1 | `47adb7288947`  |
| 2684   | Layout 1 | `47adb7288947`  |
| 2672   | Layout 1 | `47adb7288947`  |
| 2665   | Layout 1 | `47adb7288947`  |
| 2657   | Layout 1 | `47adb7288947`  |
| 2649   | Layout 1 | `47adb7288947`  |
| 2644   | Layout 1 | `47adb7288947`  |
| 2637   | Layout 1 | `47adb7288947`  |
| 2629   | Layout 1 | `47adb7288947`  |
| 2619   | Layout 1 | `47adb7288947`  |
| 2612   | Layout 1 | `47adb7288947`  |
| 2606   | Layout 1 | `47adb7288947`  |
| 2602   | Layout 1 | `47adb7288947`  |
| 2601   | Layout 1 | `47adb7288947`  |
| 2592   | Layout 1 | `47adb7288947`  |
| 2583   | Layout 1 | `47adb7288947`  |
| 2575   | Layout 1 | `47adb7288947`  |
| 2567   | Layout 1 | `47adb7288947`  |
| 2560   | Layout 1 | `47adb7288947`  |
| 2553   | Layout 1 | `47adb7288947`  |
| 2545   | Layout 1 | `47adb7288947`  |
| 2538   | Layout 1 | `47adb7288947`  |
| 2529   | Layout 1 | `47adb7288947`  |
| 2519   | Layout 1 | `47adb7288947`  |
| 2513   | Layout 1 | `47adb7288947`  |
| 2510   | Layout 1 | `47adb7288947`  |
| 2507   | Layout 1 | `47adb7288947`  |
| 2503   | Layout 1 | `47adb7288947`  |
| 2498   | Layout 1 | `47adb7288947`  |
| 2492   | Layout 1 | `47adb7288947`  |
| 2487   | Layout 1 | `47adb7288947`  |
| 2480   | Layout 1 | `47adb7288947`  |
| 2474   | Layout 1 | `47adb7288947`  |
| 2468   | Layout 1 | `47adb7288947`  |
| 2460   | Layout 1 | `47adb7288947`  |
| 2453   | Layout 1 | `47adb7288947`  |
| 2444   | Layout 1 | `47adb7288947`  |
| 2438   | Layout 1 | `47adb7288947`  |
| 2434   | Layout 1 | `47adb7288947`  |
| 2429   | Layout 1 | `47adb7288947`  |
| 2421   | Layout 1 | `47adb7288947`  |
| 2414   | Layout 1 | `47adb7288947`  |
| 2407   | Layout 1 | `47adb7288947`  |
| 2401   | Layout 1 | `47adb7288947`  |
| 2397   | Layout 1 | `47adb7288947`  |
| 2393   | Layout 1 | `47adb7288947`  |
| 2384   | Layout 1 | `47adb7288947`  |
| 2378   | Layout 1 | `47adb7288947`  |
| 2372   | Layout 1 | `47adb7288947`  |
| 2358   | Layout 1 | `47adb7288947`  |
| 2352   | Layout 1 | `47adb7288947`  |
| 2347   | Layout 1 | `47adb7288947`  |
| 2343   | Layout 1 | `47adb7288947`  |
| 2335   | Layout 1 | `47adb7288947`  |
| 2327   | Layout 1 | `47adb7288947`  |
| 2324   | Layout 1 | `47adb7288947`  |
| 2319   | Layout 1 | `47adb7288947`  |
| 2313   | Layout 1 | `47adb7288947`  |
| 2308   | Layout 1 | `47adb7288947`  |
| 2302   | Layout 1 | `47adb7288947`  |
| 2295   | Layout 1 | `47adb7288947`  |
| 2290   | Layout 1 | `47adb7288947`  |
| 2284   | Layout 1 | `47adb7288947`  |
| 2276   | Layout 1 | `47adb7288947`  |
| 2269   | Layout 1 | `47adb7288947`  |
| 2259   | Layout 1 | `47adb7288947`  |
| 2250   | Layout 1 | `47adb7288947`  |
| 2243   | Layout 1 | `47adb7288947`  |
| 2235   | Layout 1 | `47adb7288947`  |
| 2229   | Layout 1 | `47adb7288947`  |
| 2224   | Layout 1 | `47adb7288947`  |
| 2218   | Layout 1 | `47adb7288947`  |
| 2215   | Layout 1 | `47adb7288947`  |
| 2207   | Layout 1 | `47adb7288947`  |
| 2203   | Layout 1 | `47adb7288947`  |
| 2196   | Layout 1 | `47adb7288947`  |
| 2192   | Layout 1 | `47adb7288947`  |
| 2189   | Layout 1 | `47adb7288947`  |
| 2183   | Layout 1 | `47adb7288947`  |
| 2179   | Layout 1 | `47adb7288947`  |
| 2171   | Layout 1 | `47adb7288947`  |
| 2163   | Layout 1 | `47adb7288947`  |
| 2156   | Layout 1 | `47adb7288947`  |
| 2151   | Layout 1 | `47adb7288947`  |
| 2147   | Layout 1 | `47adb7288947`  |
| 2142   | Layout 1 | `47adb7288947`  |
| 2138   | Layout 1 | `47adb7288947`  |
| 2134   | Layout 1 | `47adb7288947`  |
| 2130   | Layout 1 | `47adb7288947`  |
| 2122   | Layout 1 | `47adb7288947`  |
| 2107   | Layout 1 | `47adb7288947`  |
| 2098   | Layout 1 | `47adb7288947`  |
| 2089   | Layout 1 | `47adb7288947`  |
| 2081   | Layout 1 | `47adb7288947`  |
| 2073   | Layout 1 | `47adb7288947`  |
| 2067   | Layout 1 | `47adb7288947`  |
| 2063   | Layout 1 | `47adb7288947`  |
| 2059   | Layout 1 | `47adb7288947`  |
| 2052   | Layout 1 | `47adb7288947`  |
| 2044   | Layout 1 | `47adb7288947`  |
| 2039   | Layout 1 | `47adb7288947`  |
| 2032   | Layout 1 | `47adb7288947`  |
| 2025   | Layout 1 | `47adb7288947`  |
| 2011   | Layout 1 | `47adb7288947`  |
| 2005   | Layout 1 | `47adb7288947`  |
| 2000   | Layout 1 | `47adb7288947`  |
| 1996   | Layout 1 | `47adb7288947`  |
| 1991   | Layout 1 | `47adb7288947`  |
| 1985   | Layout 1 | `47adb7288947`  |
| 1980   | Layout 1 | `47adb7288947`  |
| 1969   | Layout 1 | `47adb7288947`  |
| 1964   | Layout 1 | `47adb7288947`  |
| 1958   | Layout 1 | `47adb7288947`  |
| 1950   | Layout 1 | `47adb7288947`  |
| 1945   | Layout 1 | `47adb7288947`  |
| 1937   | Layout 1 | `47adb7288947`  |
| 1933   | Layout 1 | `47adb7288947`  |
| 1927   | Layout 1 | `47adb7288947`  |
| 1921   | Layout 1 | `47adb7288947`  |
| 1914   | Layout 1 | `47adb7288947`  |
| 1908   | Layout 1 | `47adb7288947`  |
| 1897   | Layout 1 | `47adb7288947`  |
| 1892   | Layout 1 | `47adb7288947`  |
| 1886   | Layout 1 | `47adb7288947`  |
| 1881   | Layout 1 | `47adb7288947`  |
| 1871   | Layout 1 | `47adb7288947`  |
| 1866   | Layout 1 | `47adb7288947`  |
| 1862   | Layout 1 | `47adb7288947`  |
| 1854   | Layout 1 | `47adb7288947`  |
| 1846   | Layout 1 | `47adb7288947`  |
| 1838   | Layout 1 | `47adb7288947`  |
| 1832   | Layout 1 | `47adb7288947`  |
| 1826   | Layout 1 | `47adb7288947`  |
| 1822   | Layout 1 | `47adb7288947`  |
| 1818   | Layout 1 | `47adb7288947`  |
| 1804   | Layout 1 | `47adb7288947`  |
| 1794   | Layout 1 | `47adb7288947`  |
| 1790   | Layout 1 | `47adb7288947`  |
| 1784   | Layout 1 | `47adb7288947`  |
| 1774   | Layout 1 | `47adb7288947`  |
| 1771   | Layout 1 | `47adb7288947`  |
| 1762   | Layout 1 | `47adb7288947`  |
| 1759   | Layout 1 | `47adb7288947`  |
| 1754   | Layout 1 | `47adb7288947`  |
| 1749   | Layout 1 | `47adb7288947`  |
| 1743   | Layout 1 | `47adb7288947`  |
| 1737   | Layout 1 | `47adb7288947`  |
| 1731   | Layout 1 | `47adb7288947`  |
| 1725   | Layout 1 | `47adb7288947`  |
| 1717   | Layout 1 | `47adb7288947`  |
| 1710   | Layout 1 | `47adb7288947`  |
| 1704   | Layout 1 | `47adb7288947`  |
| 1698   | Layout 1 | `47adb7288947`  |
| 1690   | Layout 1 | `47adb7288947`  |
| 1685   | Layout 1 | `47adb7288947`  |
| 1680   | Layout 1 | `47adb7288947`  |
| 1674   | Layout 1 | `47adb7288947`  |
| 1668   | Layout 1 | `47adb7288947`  |
| 1659   | Layout 1 | `47adb7288947`  |
| 1649   | Layout 1 | `47adb7288947`  |
| 1642   | Layout 1 | `47adb7288947`  |
| 1636   | Layout 1 | `47adb7288947`  |
| 1628   | Layout 1 | `47adb7288947`  |
| 1622   | Layout 1 | `47adb7288947`  |
| 1614   | Layout 1 | `47adb7288947`  |
| 1608   | Layout 1 | `47adb7288947`  |
| 1602   | Layout 1 | `47adb7288947`  |
| 1598   | Layout 1 | `47adb7288947`  |
| 1594   | Layout 1 | `47adb7288947`  |
| 1590   | Layout 1 | `47adb7288947`  |
| 1587   | Layout 1 | `47adb7288947`  |
| 1584   | Layout 1 | `47adb7288947`  |
| 1579   | Layout 1 | `47adb7288947`  |
| 1572   | Layout 1 | `47adb7288947`  |
| 1565   | Layout 1 | `47adb7288947`  |
| 1559   | Layout 1 | `47adb7288947`  |
| 1554   | Layout 1 | `47adb7288947`  |
| 1547   | Layout 1 | `47adb7288947`  |
| 1537   | Layout 1 | `47adb7288947`  |
| 1529   | Layout 1 | `47adb7288947`  |
| 1524   | Layout 1 | `47adb7288947`  |
| 1519   | Layout 1 | `47adb7288947`  |
| 1509   | Layout 1 | `47adb7288947`  |
| 1506   | Layout 1 | `47adb7288947`  |
| 1504   | Layout 1 | `47adb7288947`  |
| 1500   | Layout 1 | `47adb7288947`  |
| 1493   | Layout 1 | `47adb7288947`  |
| 1489   | Layout 1 | `47adb7288947`  |
| 1485   | Layout 1 | `47adb7288947`  |
| 1481   | Layout 1 | `47adb7288947`  |
| 1474   | Layout 1 | `47adb7288947`  |
| 1466   | Layout 1 | `47adb7288947`  |
| 1462   | Layout 1 | `47adb7288947`  |
| 1459   | Layout 1 | `47adb7288947`  |
| 1453   | Layout 1 | `47adb7288947`  |
| 1450   | Layout 1 | `47adb7288947`  |
| 1445   | Layout 1 | `47adb7288947`  |
| 1439   | Layout 1 | `47adb7288947`  |
| 1433   | Layout 1 | `47adb7288947`  |
| 1430   | Layout 1 | `47adb7288947`  |
| 1426   | Layout 1 | `47adb7288947`  |
| 1421   | Layout 1 | `47adb7288947`  |
| 1417   | Layout 1 | `47adb7288947`  |
| 1416   | Layout 1 | `47adb7288947`  |
| 1409   | Layout 1 | `47adb7288947`  |
| 1405   | Layout 1 | `47adb7288947`  |
| 1401   | Layout 1 | `47adb7288947`  |
| 1396   | Layout 1 | `47adb7288947`  |
| 1391   | Layout 1 | `47adb7288947`  |
| 1390   | Layout 1 | `47adb7288947`  |
| 1386   | Layout 1 | `47adb7288947`  |
| 1381   | Layout 1 | `47adb7288947`  |
| 1379   | Layout 1 | `47adb7288947`  |
| 1372   | Layout 1 | `47adb7288947`  |
| 1366   | Layout 1 | `47adb7288947`  |
| 1364   | Layout 1 | `47adb7288947`  |
| 1363   | Layout 1 | `47adb7288947`  |
| 1360   | Layout 1 | `47adb7288947`  |
| 1358   | Layout 1 | `47adb7288947`  |
| 1355   | Layout 1 | `47adb7288947`  |
| 1351   | Layout 1 | `47adb7288947`  |
| 1348   | Layout 1 | `47adb7288947`  |
| 1346   | Layout 1 | `47adb7288947`  |
| 1341   | Layout 1 | `47adb7288947`  |
| 1340   | Layout 1 | `47adb7288947`  |
| 1338   | Layout 1 | `47adb7288947`  |
| 1335   | Layout 1 | `47adb7288947`  |
| 1333   | Layout 1 | `47adb7288947`  |
| 1329   | Layout 1 | `47adb7288947`  |
| 1327   | Layout 1 | `47adb7288947`  |
| 1324   | Layout 1 | `47adb7288947`  |
| 1321   | Layout 1 | `47adb7288947`  |
| 1319   | Layout 1 | `47adb7288947`  |
| 1318   | Layout 1 | `47adb7288947`  |
| 1316   | Layout 1 | `47adb7288947`  |
| 1313   | Layout 1 | `47adb7288947`  |
| 1311   | Layout 1 | `47adb7288947`  |
| 1309   | Layout 1 | `47adb7288947`  |
| 1304   | Layout 1 | `47adb7288947`  |
| 1292   | Layout 1 | `47adb7288947`  |
| 1286   | Layout 1 | `47adb7288947`  |
| 1280   | Layout 1 | `47adb7288947`  |
| 1276   | Layout 1 | `47adb7288947`  |
| 1267   | Layout 1 | `47adb7288947`  |
| 1261   | Layout 1 | `47adb7288947`  |
| 1256   | Layout 1 | `47adb7288947`  |
| 1250   | No file  | `47adb7288947`  |
| 1246   | No file  | `47adb7288947`  |
| 1239   | No file  | `47adb7288947`  |
| 1230   | No file  | `47adb7288947`  |
| 1226   | No file  | `47adb7288947`  |
| 1220   | No file  | `47adb7288947`  |
| 1217   | No file  | `47adb7288947`  |
| 1211   | No file  | `47adb7288947`  |
| 1210   | No file  | `47adb7288947`  |
| 1208   | No file  | `47adb7288947`  |
| 1203   | No file  | `47adb7288947`  |
| 1197   | No file  | `47adb7288947`  |
| 1194   | No file  | `47adb7288947`  |
| 1192   | No file  | `47adb7288947`  |
| 1187   | No file  | `47adb7288947`  |
| 1183   | No file  | `47adb7288947`  |
| 1177   | No file  | `47adb7288947`  |
| 1173   | No file  | `47adb7288947`  |
| 1167   | No file  | `47adb7288947`  |
| 1164   | No file  | `47adb7288947`  |
| 1156   | No file  | `47adb7288947`  |
| 1149   | No file  | `47adb7288947`  |
| 1144   | No file  | `47adb7288947`  |
| 1137   | No file  | `47adb7288947`  |
| 1132   | No file  | `47adb7288947`  |
| 1127   | No file  | `47adb7288947`  |
| 1122   | No file  | `47adb7288947`  |
| 1118   | No file  | `47adb7288947`  |
| 1114   | No file  | `47adb7288947`  |
| 1109   | No file  | `47adb7288947`  |
| 1102   | No file  | `47adb7288947`  |
| 1096   | No file  | `47adb7288947`  |
| 1088   | No file  | `47adb7288947`  |
| 1081   | No file  | `47adb7288947`  |
| 1076   | No file  | `47adb7288947`  |
| 1069   | No file  | `47adb7288947`  |
| 1064   | No file  | `47adb7288947`  |
| 1058   | No file  | `47adb7288947`  |
| 1051   | No file  | `47adb7288947`  |
| 1044   | No file  | `47adb7288947`  |
| 1036   | No file  | `47adb7288947`  |
| 1026   | No file  | `47adb7288947`  |
| 1016   | No file  | `47adb7288947`  |
| 1009   | No file  | `47adb7288947`  |
| 1005   | No file  | `47adb7288947`  |
| 1000   | No file  | `47adb7288947`  |
| 998    | No file  | `47adb7288947`  |
| 990    | No file  | `47adb7288947`  |
| 979    | No file  | `47adb7288947`  |
| 972    | No file  | `47adb7288947`  |
| 963    | No file  | `47adb7288947`  |
| 955    | No file  | `47adb7288947`  |
| 946    | No file  | `47adb7288947`  |
| 938    | No file  | `47adb7288947`  |
| 927    | No file  | `47adb7288947`  |
| 911    | No file  | `47adb7288947`  |
| 904    | No file  | `47adb7288947`  |
| 899    | No file  | `47adb7288947`  |
| 894    | No file  | `47adb7288947`  |
| 885    | No file  | `47adb7288947`  |
| 879    | No file  | `47adb7288947`  |
| 872    | No file  | `47adb7288947`  |
| 864    | No file  | `47adb7288947`  |
| 855    | No file  | `47adb7288947`  |
| 853    | No file  | `47adb7288947`  |
| 845    | No file  | `47adb7288947`  |
| 837    | No file  | `47adb7288947`  |
| 829    | No file  | `47adb7288947`  |
| 822    | No file  | `47adb7288947`  |
| 814    | No file  | `47adb7288947`  |
| 805    | No file  | `47adb7288947`  |
| 794    | No file  | `47adb7288947`  |
| 787    | No file  | `47adb7288947`  |
| 780    | No file  | `47adb7288947`  |
| 771    | No file  | `47adb7288947`  |
| 760    | No file  | `47adb7288947`  |
| 748    | No file  | `47adb7288947`  |
| 741    | No file  | `47adb7288947`  |
| 736    | No file  | `47adb7288947`  |
| 731    | No file  | `47adb7288947`  |
| 723    | No file  | `47adb7288947`  |
| 711    | No file  | `47adb7288947`  |
| 707    | No file  | `47adb7288947`  |
| 697    | No file  | `47adb7288947`  |
| 689    | No file  | `47adb7288947`  |
| 683    | No file  | `47adb7288947`  |
| 678    | No file  | `47adb7288947`  |
| 670    | No file  | `47adb7288947`  |
| 661    | No file  | `47adb7288947`  |
| 656    | No file  | `47adb7288947`  |
| 652    | No file  | `47adb7288947`  |
| 643    | No file  | `47adb7288947`  |
| 637    | No file  | `47adb7288947`  |
| 630    | No file  | `47adb7288947`  |
| 627    | No file  | `47adb7288947`  |
| 621    | No file  | `47adb7288947`  |
| 617    | No file  | `47adb7288947`  |
| 615    | No file  | `47adb7288947`  |
| 606    | No file  | `47adb7288947`  |
| 599    | No file  | `47adb7288947`  |
| 592    | No file  | `47adb7288947`  |
| 586    | No file  | `47adb7288947`  |
| 577    | No file  | `47adb7288947`  |
| 569    | No file  | `47adb7288947`  |
| 561    | No file  | `47adb7288947`  |
| 554    | No file  | `47adb7288947`  |
| 542    | No file  | `47adb7288947`  |
| 532    | No file  | `47adb7288947`  |
| 531    | No file  | `47adb7288947`  |
| 526    | No file  | `47adb7288947`  |
| 521    | No file  | `47adb7288947`  |
| 517    | No file  | `47adb7288947`  |
| 510    | No file  | `47adb7288947`  |
| 508    | No file  | `47adb7288947`  |
| 504    | No file  | `47adb7288947`  |
| 497    | No file  | `47adb7288947`  |
| 491    | No file  | `47adb7288947`  |
| 485    | No file  | `47adb7288947`  |
| 478    | No file  | `47adb7288947`  |
| 472    | No file  | `47adb7288947`  |
| 466    | No file  | `47adb7288947`  |
| 457    | No file  | `47adb7288947`  |
| 452    | No file  | `47adb7288947`  |
| 449    | No file  | `47adb7288947`  |
| 435    | No file  | `47adb7288947`  |

<!-- versions:end -->

## Companion Files

None. The handler reads the groups in file order and does not need
`alchemyupgradeoffset.dbss` (see below). Item names come from LOC type 0 and
icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The grouped layout of [`alchemycharge.dbss`](alchemycharge_dbss.md): a u32
group count, then per group a u32 row count and that many 12-byte rows. No
`PABR` magic and no string table; the file ends after the last group.

| Offset  | Type               | Field       | Notes                                                |
| ------- | ------------------ | ----------- | ---------------------------------------------------- |
| `+0x00` | u32                | group_count | One group per alchemy stone type; `8` on client 3464 |
| `+0x04` | Group[group_count] | groups      | Group `i` holds stone type `i`; see Group            |

### Group (variable: 4 bytes + rows)

| Offset  | Type           | Field     | Notes                           |
| ------- | -------------- | --------- | ------------------------------- |
| `+0x00` | u32            | row_count | `0` for a type with no material |
| `+0x04` | Row[row_count] | rows      | See Row                         |

### Row (12 bytes)

| Offset  | Type | Field      | Notes                                                             |
| ------- | ---- | ---------- | ----------------------------------------------------------------- |
| `+0x00` | u32  | stone_type | Equals the group index; see Stone Types                           |
| `+0x04` | u32  | item_id    | Material item; unique within a group                              |
| `+0x08` | u32  | experience | EXP per unit of the material, percent x 10,000 (`20408` = 2.0408%) |

On client 3464 the groups hold:

| Group | Rows | Materials                                                    | experience        |
| ----- | ---- | ------------------------------------------------------------ | ----------------- |
| `0`   | 28   | Ingots and pure crystals (4052 Iron Ingot, 4053 Pure Iron Crystal, 4253 Pure Silver Crystal, ...) | `18182` to `142857` |
| `1`   | 31   | Plywood and sturdy plywood (4652 Ash Plywood, 4653 Sturdy Ash Plywood, ...) | `18182` to `250000` |
| `2`   | 107  | High-quality and special crops (5444 High-quality Sunrise Herb, 7322 Special Strawberry, ...) | `649` to `6623` |
| `3` to `7` | 0 | Empty groups                                              |                   |

Every `experience` value on client 3464 is `1,000,000 / N` rounded, with `N`
a whole number: Iron Ingot `20408` is 1/49 of 100% EXP, Ash Plywood `18182`
1/55, High-quality Wheat `730` 1/1370.

### `alchemyupgradeoffset.dbss`

The grouped walk of `alchemychargeoffset.dbss`: a u32 group count (equal to
the main file's), then per group a u32 row count and 12-byte rows. A row
leaves out the stone type; its group index stands for it.

| Offset  | Type                     | Field       | Notes                                           |
| ------- | ------------------------ | ----------- | ----------------------------------------------- |
| `+0x00` | u32                      | group_count | Equals the main file's `group_count`            |
| `+0x04` | Index Group[group_count] | groups      | Group `i` holds stone type `i`; see Index Group |

### Index Group (variable: 4 bytes + rows)

| Offset  | Type                 | Field     | Notes                               |
| ------- | -------------------- | --------- | ----------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main group's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                       |

### Index Row (12 bytes)

| Offset  | Type | Field   | Notes                                                          |
| ------- | ---- | ------- | -------------------------------------------------------------- |
| `+0x00` | u32  | item_id | Row key together with the group index                          |
| `+0x04` | u32  | offset  | Start of the row in `alchemyupgrade.dbss`, at its `stone_type` |
| `+0x08` | u32  | size    | Always `12`, the main row size                                 |

Every index row points at the main row with the same stone type and item.
Unlike `alchemychargeoffset.dbss`, the rows inside a group are not in the
main file's order (group 0 lists 4052, 4061, 4253 where the main file has
4052, 4253, 4061). Both files are 2,028 bytes on client 3464.

## Stone Types

The group index and `stone_type` are the alchemy stone's `_contentsEventParam1`,
the same stone type as in `alchemycharge.dbss`; see its
[Stone Types](alchemycharge_dbss.md#stone-types) table. The Polishing tab
names each type's material from the same number (`panel_window_alchemystone_all`,
`invenStoneRClick`), and the groups hold those materials:

| stone_type | Stone       | Polishing Material (Lua)                                                  |
| ---------- | ----------- | ------------------------------------------------------------------------- |
| `0`        | Destruction | `LUA_ALCHEMYSTONE_PURESTONE` "Pure Metals", `LUA_ALCHEMYSTONE_PURESTONE2` "Metal Ingot" |
| `1`        | Protection  | `LUA_ALCHEMYSTONE_HARDWOOD` "Sturdy Plywood", `LUA_ALCHEMYSTONE_HARDWOOD2` "Plywood" |
| `2`        | Life        | `LUA_ALCHEMYSTONE_CHOICEGOOD` "Special Crop", `LUA_ALCHEMYSTONE_CHOICEGOOD2` "High-quality Crop" |

## Notes

- `experience` is named after the Polishing tab. Its guide text
  `LUA_ALCHEMYSTONE_DESC_2` reads "Polish your stone with material items to
  increase its EXP", and the tab (`_TAB_TYPE.EXP`, label
  `LUA_ALCHEMYSTONE_EXP` "Polishing") sends `alchemyUpgrade(material slot,
  count, stone slot)`; the Growth tab sends `alchemyEvolve()` instead
  (`panel_window_alchemystone_all`, `Panel_AlchemyStone_All_UpdateTime`). The inventory filter for
  a polishing material is `isAlchemyUpgradeItem(stone type)`.
- The window shows a stone's EXP as `getExperience() / 10000` with a `%`
  (`LUA_ALCHEMYSTONE_EXPERIENCE` "EXP {exp}%"), so a stone at 100% holds
  `1,000,000`. `experience` reads on the same scale, which the
  `1,000,000 / N` values above agree with. The client code that reads this
  file is not in Lua.
- The Polishing tab refuses a stone at 150% EXP or more
  (`LUA_ALCHEMYSTONE_EXPMAX_WARRING` "Cannot grow any further.",
  `HandleEventLUp_AlchemyStone_Doit`), and Growth
  opens from 80% (`LUA_ALCHEMYSTONE_DESC_3`).
- Item IDs are unique across the whole file on client 3464, not only within
  a group.

## Open Questions

### Stone Types 3 to 7

Groups 3 to 7 are empty on client 3464, as in `alchemycharge.dbss`. The
Polishing tab names a material only for types `0` to `2`; see that file's
Open Questions.

## In-Game Checks

### EXP per Material

Needs item (all):

- [Imperfect Alchemy Stone of Destruction](https://bdocodex.com/us/item/45201/)
- [Rough Alchemy Stone of Destruction](https://bdocodex.com/us/item/45205/)
- [Iron Ingot](https://bdocodex.com/us/item/4052/)

Polish each stone with one Iron Ingot and read its EXP before and after. A
rise of 2.04% on both stones means `experience` reaches the stone as
stored. A smaller rise on the Rough stone means the client scales it by the
stone's grade, as the Recharge tab does with durability.
