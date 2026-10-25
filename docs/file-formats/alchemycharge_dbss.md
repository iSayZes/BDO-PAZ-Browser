# `alchemycharge.dbss` Format

## Purpose

The materials that recharge an alchemy stone's durability in the Recharge tab
of the alchemy stone window, per alchemy stone type. A row is the stone type,
the material item and the durability points that material counts for.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes | Records                     | Row bytes |
| ------ | -------------- | -------------------------- | ----- | --------------------------- | --------- |
| 1      | 1256 and later | `alchemycharge.dbss`       | 468   | 36 Row, 8 Group             | 12        |
| 1      | 1256 and later | `alchemychargeoffset.dbss` | 468   | 36 Index Row, 8 Index Group | 12        |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 1      | `alchemycharge.dbss`       | 468 B (100.0%) | 0 B (0.0%) |
| 1      | `alchemychargeoffset.dbss` | 468 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `0ab2c9bee231`  |
| 3482   | Layout 1 | `0ab2c9bee231`  |
| 3474   | Layout 1 | `0ab2c9bee231`  |
| 3473   | Layout 1 | `0ab2c9bee231`  |
| 3464   | Layout 1 | `0ab2c9bee231`  |
| 3458   | Layout 1 | `0ab2c9bee231`  |
| 3454   | Layout 1 | `0ab2c9bee231`  |
| 3444   | Layout 1 | `0ab2c9bee231`  |
| 3435   | Layout 1 | `0ab2c9bee231`  |
| 3426   | Layout 1 | `0ab2c9bee231`  |
| 3418   | Layout 1 | `0ab2c9bee231`  |
| 3412   | Layout 1 | `0ab2c9bee231`  |
| 3402   | Layout 1 | `0ab2c9bee231`  |
| 3396   | Layout 1 | `0ab2c9bee231`  |
| 3387   | Layout 1 | `0ab2c9bee231`  |
| 3381   | Layout 1 | `0ab2c9bee231`  |
| 3373   | Layout 1 | `0ab2c9bee231`  |
| 3364   | Layout 1 | `0ab2c9bee231`  |
| 3356   | Layout 1 | `0ab2c9bee231`  |
| 3349   | Layout 1 | `0ab2c9bee231`  |
| 3342   | Layout 1 | `0ab2c9bee231`  |
| 3335   | Layout 1 | `0ab2c9bee231`  |
| 3326   | Layout 1 | `0ab2c9bee231`  |
| 3321   | Layout 1 | `0ab2c9bee231`  |
| 3314   | Layout 1 | `0ab2c9bee231`  |
| 3303   | Layout 1 | `0ab2c9bee231`  |
| 3302   | Layout 1 | `0ab2c9bee231`  |
| 3293   | Layout 1 | `0ab2c9bee231`  |
| 3283   | Layout 1 | `0ab2c9bee231`  |
| 3275   | Layout 1 | `0ab2c9bee231`  |
| 3267   | Layout 1 | `0ab2c9bee231`  |
| 3258   | Layout 1 | `0ab2c9bee231`  |
| 3251   | Layout 1 | `0ab2c9bee231`  |
| 3242   | Layout 1 | `0ab2c9bee231`  |
| 3235   | Layout 1 | `0ab2c9bee231`  |
| 3229   | Layout 1 | `0ab2c9bee231`  |
| 3212   | Layout 1 | `0ab2c9bee231`  |
| 3203   | Layout 1 | `0ab2c9bee231`  |
| 3193   | Layout 1 | `0ab2c9bee231`  |
| 3186   | Layout 1 | `0ab2c9bee231`  |
| 3177   | Layout 1 | `0ab2c9bee231`  |
| 3169   | Layout 1 | `0ab2c9bee231`  |
| 3158   | Layout 1 | `0ab2c9bee231`  |
| 3151   | Layout 1 | `0ab2c9bee231`  |
| 3144   | Layout 1 | `0ab2c9bee231`  |
| 3133   | Layout 1 | `0ab2c9bee231`  |
| 3125   | Layout 1 | `0ab2c9bee231`  |
| 3118   | Layout 1 | `0ab2c9bee231`  |
| 3111   | Layout 1 | `0ab2c9bee231`  |
| 3103   | Layout 1 | `0ab2c9bee231`  |
| 3095   | Layout 1 | `0ab2c9bee231`  |
| 3086   | Layout 1 | `0ab2c9bee231`  |
| 3072   | Layout 1 | `0ab2c9bee231`  |
| 3062   | Layout 1 | `0ab2c9bee231`  |
| 3052   | Layout 1 | `0ab2c9bee231`  |
| 3045   | Layout 1 | `0ab2c9bee231`  |
| 3037   | Layout 1 | `0ab2c9bee231`  |
| 3030   | Layout 1 | `0ab2c9bee231`  |
| 3021   | Layout 1 | `0ab2c9bee231`  |
| 3012   | Layout 1 | `0ab2c9bee231`  |
| 3002   | Layout 1 | `0ab2c9bee231`  |
| 2995   | Layout 1 | `0ab2c9bee231`  |
| 2987   | Layout 1 | `0ab2c9bee231`  |
| 2978   | Layout 1 | `0ab2c9bee231`  |
| 2970   | Layout 1 | `0ab2c9bee231`  |
| 2959   | Layout 1 | `0ab2c9bee231`  |
| 2951   | Layout 1 | `0ab2c9bee231`  |
| 2942   | Layout 1 | `0ab2c9bee231`  |
| 2935   | Layout 1 | `0ab2c9bee231`  |
| 2932   | Layout 1 | `0ab2c9bee231`  |
| 2923   | Layout 1 | `0ab2c9bee231`  |
| 2919   | Layout 1 | `0ab2c9bee231`  |
| 2907   | Layout 1 | `0ab2c9bee231`  |
| 2900   | Layout 1 | `0ab2c9bee231`  |
| 2891   | Layout 1 | `0ab2c9bee231`  |
| 2882   | Layout 1 | `0ab2c9bee231`  |
| 2872   | Layout 1 | `0ab2c9bee231`  |
| 2863   | Layout 1 | `0ab2c9bee231`  |
| 2855   | Layout 1 | `0ab2c9bee231`  |
| 2849   | Layout 1 | `0ab2c9bee231`  |
| 2844   | Layout 1 | `0ab2c9bee231`  |
| 2834   | Layout 1 | `0ab2c9bee231`  |
| 2825   | Layout 1 | `0ab2c9bee231`  |
| 2819   | Layout 1 | `0ab2c9bee231`  |
| 2811   | Layout 1 | `0ab2c9bee231`  |
| 2803   | Layout 1 | `0ab2c9bee231`  |
| 2794   | Layout 1 | `0ab2c9bee231`  |
| 2783   | Layout 1 | `0ab2c9bee231`  |
| 2774   | Layout 1 | `0ab2c9bee231`  |
| 2765   | Layout 1 | `0ab2c9bee231`  |
| 2756   | Layout 1 | `0ab2c9bee231`  |
| 2750   | Layout 1 | `0ab2c9bee231`  |
| 2743   | Layout 1 | `0ab2c9bee231`  |
| 2736   | Layout 1 | `0ab2c9bee231`  |
| 2726   | Layout 1 | `0ab2c9bee231`  |
| 2717   | Layout 1 | `0ab2c9bee231`  |
| 2709   | Layout 1 | `0ab2c9bee231`  |
| 2703   | Layout 1 | `0ab2c9bee231`  |
| 2695   | Layout 1 | `0ab2c9bee231`  |
| 2684   | Layout 1 | `0ab2c9bee231`  |
| 2672   | Layout 1 | `0ab2c9bee231`  |
| 2665   | Layout 1 | `0ab2c9bee231`  |
| 2657   | Layout 1 | `0ab2c9bee231`  |
| 2649   | Layout 1 | `0ab2c9bee231`  |
| 2644   | Layout 1 | `0ab2c9bee231`  |
| 2637   | Layout 1 | `0ab2c9bee231`  |
| 2629   | Layout 1 | `0ab2c9bee231`  |
| 2619   | Layout 1 | `0ab2c9bee231`  |
| 2612   | Layout 1 | `0ab2c9bee231`  |
| 2606   | Layout 1 | `0ab2c9bee231`  |
| 2602   | Layout 1 | `0ab2c9bee231`  |
| 2601   | Layout 1 | `0ab2c9bee231`  |
| 2592   | Layout 1 | `0ab2c9bee231`  |
| 2583   | Layout 1 | `0ab2c9bee231`  |
| 2575   | Layout 1 | `0ab2c9bee231`  |
| 2567   | Layout 1 | `0ab2c9bee231`  |
| 2560   | Layout 1 | `0ab2c9bee231`  |
| 2553   | Layout 1 | `0ab2c9bee231`  |
| 2545   | Layout 1 | `0ab2c9bee231`  |
| 2538   | Layout 1 | `0ab2c9bee231`  |
| 2529   | Layout 1 | `0ab2c9bee231`  |
| 2519   | Layout 1 | `0ab2c9bee231`  |
| 2513   | Layout 1 | `0ab2c9bee231`  |
| 2510   | Layout 1 | `0ab2c9bee231`  |
| 2507   | Layout 1 | `0ab2c9bee231`  |
| 2503   | Layout 1 | `0ab2c9bee231`  |
| 2498   | Layout 1 | `0ab2c9bee231`  |
| 2492   | Layout 1 | `0ab2c9bee231`  |
| 2487   | Layout 1 | `0ab2c9bee231`  |
| 2480   | Layout 1 | `0ab2c9bee231`  |
| 2474   | Layout 1 | `0ab2c9bee231`  |
| 2468   | Layout 1 | `0ab2c9bee231`  |
| 2460   | Layout 1 | `0ab2c9bee231`  |
| 2453   | Layout 1 | `0ab2c9bee231`  |
| 2444   | Layout 1 | `0ab2c9bee231`  |
| 2438   | Layout 1 | `0ab2c9bee231`  |
| 2434   | Layout 1 | `0ab2c9bee231`  |
| 2429   | Layout 1 | `0ab2c9bee231`  |
| 2421   | Layout 1 | `0ab2c9bee231`  |
| 2414   | Layout 1 | `0ab2c9bee231`  |
| 2407   | Layout 1 | `0ab2c9bee231`  |
| 2401   | Layout 1 | `0ab2c9bee231`  |
| 2397   | Layout 1 | `0ab2c9bee231`  |
| 2393   | Layout 1 | `0ab2c9bee231`  |
| 2384   | Layout 1 | `0ab2c9bee231`  |
| 2378   | Layout 1 | `0ab2c9bee231`  |
| 2372   | Layout 1 | `0ab2c9bee231`  |
| 2358   | Layout 1 | `0ab2c9bee231`  |
| 2352   | Layout 1 | `0ab2c9bee231`  |
| 2347   | Layout 1 | `0ab2c9bee231`  |
| 2343   | Layout 1 | `0ab2c9bee231`  |
| 2335   | Layout 1 | `0ab2c9bee231`  |
| 2327   | Layout 1 | `0ab2c9bee231`  |
| 2324   | Layout 1 | `0ab2c9bee231`  |
| 2319   | Layout 1 | `0ab2c9bee231`  |
| 2313   | Layout 1 | `0ab2c9bee231`  |
| 2308   | Layout 1 | `0ab2c9bee231`  |
| 2302   | Layout 1 | `0ab2c9bee231`  |
| 2295   | Layout 1 | `0ab2c9bee231`  |
| 2290   | Layout 1 | `0ab2c9bee231`  |
| 2284   | Layout 1 | `0ab2c9bee231`  |
| 2276   | Layout 1 | `0ab2c9bee231`  |
| 2269   | Layout 1 | `0ab2c9bee231`  |
| 2259   | Layout 1 | `0ab2c9bee231`  |
| 2250   | Layout 1 | `0ab2c9bee231`  |
| 2243   | Layout 1 | `0ab2c9bee231`  |
| 2235   | Layout 1 | `0ab2c9bee231`  |
| 2229   | Layout 1 | `0ab2c9bee231`  |
| 2224   | Layout 1 | `0ab2c9bee231`  |
| 2218   | Layout 1 | `0ab2c9bee231`  |
| 2215   | Layout 1 | `0ab2c9bee231`  |
| 2207   | Layout 1 | `0ab2c9bee231`  |
| 2203   | Layout 1 | `0ab2c9bee231`  |
| 2196   | Layout 1 | `0ab2c9bee231`  |
| 2192   | Layout 1 | `0ab2c9bee231`  |
| 2189   | Layout 1 | `0ab2c9bee231`  |
| 2183   | Layout 1 | `0ab2c9bee231`  |
| 2179   | Layout 1 | `0ab2c9bee231`  |
| 2171   | Layout 1 | `0ab2c9bee231`  |
| 2163   | Layout 1 | `0ab2c9bee231`  |
| 2156   | Layout 1 | `0ab2c9bee231`  |
| 2151   | Layout 1 | `0ab2c9bee231`  |
| 2147   | Layout 1 | `0ab2c9bee231`  |
| 2142   | Layout 1 | `0ab2c9bee231`  |
| 2138   | Layout 1 | `0ab2c9bee231`  |
| 2134   | Layout 1 | `0ab2c9bee231`  |
| 2130   | Layout 1 | `0ab2c9bee231`  |
| 2122   | Layout 1 | `0ab2c9bee231`  |
| 2107   | Layout 1 | `0ab2c9bee231`  |
| 2098   | Layout 1 | `0ab2c9bee231`  |
| 2089   | Layout 1 | `0ab2c9bee231`  |
| 2081   | Layout 1 | `0ab2c9bee231`  |
| 2073   | Layout 1 | `0ab2c9bee231`  |
| 2067   | Layout 1 | `0ab2c9bee231`  |
| 2063   | Layout 1 | `0ab2c9bee231`  |
| 2059   | Layout 1 | `0ab2c9bee231`  |
| 2052   | Layout 1 | `0ab2c9bee231`  |
| 2044   | Layout 1 | `0ab2c9bee231`  |
| 2039   | Layout 1 | `0ab2c9bee231`  |
| 2032   | Layout 1 | `0ab2c9bee231`  |
| 2025   | Layout 1 | `0ab2c9bee231`  |
| 2011   | Layout 1 | `0ab2c9bee231`  |
| 2005   | Layout 1 | `0ab2c9bee231`  |
| 2000   | Layout 1 | `0ab2c9bee231`  |
| 1996   | Layout 1 | `0ab2c9bee231`  |
| 1991   | Layout 1 | `0ab2c9bee231`  |
| 1985   | Layout 1 | `0ab2c9bee231`  |
| 1980   | Layout 1 | `0ab2c9bee231`  |
| 1969   | Layout 1 | `0ab2c9bee231`  |
| 1964   | Layout 1 | `0ab2c9bee231`  |
| 1958   | Layout 1 | `0ab2c9bee231`  |
| 1950   | Layout 1 | `0ab2c9bee231`  |
| 1945   | Layout 1 | `0ab2c9bee231`  |
| 1937   | Layout 1 | `0ab2c9bee231`  |
| 1933   | Layout 1 | `0ab2c9bee231`  |
| 1927   | Layout 1 | `0ab2c9bee231`  |
| 1921   | Layout 1 | `0ab2c9bee231`  |
| 1914   | Layout 1 | `0ab2c9bee231`  |
| 1908   | Layout 1 | `0ab2c9bee231`  |
| 1897   | Layout 1 | `0ab2c9bee231`  |
| 1892   | Layout 1 | `0ab2c9bee231`  |
| 1886   | Layout 1 | `0ab2c9bee231`  |
| 1881   | Layout 1 | `0ab2c9bee231`  |
| 1871   | Layout 1 | `0ab2c9bee231`  |
| 1866   | Layout 1 | `0ab2c9bee231`  |
| 1862   | Layout 1 | `0ab2c9bee231`  |
| 1854   | Layout 1 | `0ab2c9bee231`  |
| 1846   | Layout 1 | `0ab2c9bee231`  |
| 1838   | Layout 1 | `0ab2c9bee231`  |
| 1832   | Layout 1 | `0ab2c9bee231`  |
| 1826   | Layout 1 | `0ab2c9bee231`  |
| 1822   | Layout 1 | `0ab2c9bee231`  |
| 1818   | Layout 1 | `0ab2c9bee231`  |
| 1804   | Layout 1 | `0ab2c9bee231`  |
| 1794   | Layout 1 | `0ab2c9bee231`  |
| 1790   | Layout 1 | `0ab2c9bee231`  |
| 1784   | Layout 1 | `0ab2c9bee231`  |
| 1774   | Layout 1 | `0ab2c9bee231`  |
| 1771   | Layout 1 | `0ab2c9bee231`  |
| 1762   | Layout 1 | `0ab2c9bee231`  |
| 1759   | Layout 1 | `0ab2c9bee231`  |
| 1754   | Layout 1 | `0ab2c9bee231`  |
| 1749   | Layout 1 | `0ab2c9bee231`  |
| 1743   | Layout 1 | `0ab2c9bee231`  |
| 1737   | Layout 1 | `0ab2c9bee231`  |
| 1731   | Layout 1 | `0ab2c9bee231`  |
| 1725   | Layout 1 | `0ab2c9bee231`  |
| 1717   | Layout 1 | `0ab2c9bee231`  |
| 1710   | Layout 1 | `0ab2c9bee231`  |
| 1704   | Layout 1 | `0ab2c9bee231`  |
| 1698   | Layout 1 | `0ab2c9bee231`  |
| 1690   | Layout 1 | `0ab2c9bee231`  |
| 1685   | Layout 1 | `0ab2c9bee231`  |
| 1680   | Layout 1 | `0ab2c9bee231`  |
| 1674   | Layout 1 | `0ab2c9bee231`  |
| 1668   | Layout 1 | `0ab2c9bee231`  |
| 1659   | Layout 1 | `0ab2c9bee231`  |
| 1649   | Layout 1 | `0ab2c9bee231`  |
| 1642   | Layout 1 | `0ab2c9bee231`  |
| 1636   | Layout 1 | `0ab2c9bee231`  |
| 1628   | Layout 1 | `0ab2c9bee231`  |
| 1622   | Layout 1 | `0ab2c9bee231`  |
| 1614   | Layout 1 | `0ab2c9bee231`  |
| 1608   | Layout 1 | `0ab2c9bee231`  |
| 1602   | Layout 1 | `0ab2c9bee231`  |
| 1598   | Layout 1 | `0ab2c9bee231`  |
| 1594   | Layout 1 | `0ab2c9bee231`  |
| 1590   | Layout 1 | `0ab2c9bee231`  |
| 1587   | Layout 1 | `0ab2c9bee231`  |
| 1584   | Layout 1 | `0ab2c9bee231`  |
| 1579   | Layout 1 | `0ab2c9bee231`  |
| 1572   | Layout 1 | `0ab2c9bee231`  |
| 1565   | Layout 1 | `0ab2c9bee231`  |
| 1559   | Layout 1 | `0ab2c9bee231`  |
| 1554   | Layout 1 | `0ab2c9bee231`  |
| 1547   | Layout 1 | `0ab2c9bee231`  |
| 1537   | Layout 1 | `0ab2c9bee231`  |
| 1529   | Layout 1 | `0ab2c9bee231`  |
| 1524   | Layout 1 | `0ab2c9bee231`  |
| 1519   | Layout 1 | `0ab2c9bee231`  |
| 1509   | Layout 1 | `0ab2c9bee231`  |
| 1506   | Layout 1 | `0ab2c9bee231`  |
| 1504   | Layout 1 | `0ab2c9bee231`  |
| 1500   | Layout 1 | `0ab2c9bee231`  |
| 1493   | Layout 1 | `0ab2c9bee231`  |
| 1489   | Layout 1 | `0ab2c9bee231`  |
| 1485   | Layout 1 | `0ab2c9bee231`  |
| 1481   | Layout 1 | `0ab2c9bee231`  |
| 1474   | Layout 1 | `0ab2c9bee231`  |
| 1466   | Layout 1 | `0ab2c9bee231`  |
| 1462   | Layout 1 | `0ab2c9bee231`  |
| 1459   | Layout 1 | `0ab2c9bee231`  |
| 1453   | Layout 1 | `0ab2c9bee231`  |
| 1450   | Layout 1 | `0ab2c9bee231`  |
| 1445   | Layout 1 | `0ab2c9bee231`  |
| 1439   | Layout 1 | `0ab2c9bee231`  |
| 1433   | Layout 1 | `0ab2c9bee231`  |
| 1430   | Layout 1 | `0ab2c9bee231`  |
| 1426   | Layout 1 | `0ab2c9bee231`  |
| 1421   | Layout 1 | `0ab2c9bee231`  |
| 1417   | Layout 1 | `0ab2c9bee231`  |
| 1416   | Layout 1 | `0ab2c9bee231`  |
| 1409   | Layout 1 | `0ab2c9bee231`  |
| 1405   | Layout 1 | `0ab2c9bee231`  |
| 1401   | Layout 1 | `0ab2c9bee231`  |
| 1396   | Layout 1 | `0ab2c9bee231`  |
| 1391   | Layout 1 | `0ab2c9bee231`  |
| 1390   | Layout 1 | `0ab2c9bee231`  |
| 1386   | Layout 1 | `0ab2c9bee231`  |
| 1381   | Layout 1 | `0ab2c9bee231`  |
| 1379   | Layout 1 | `0ab2c9bee231`  |
| 1372   | Layout 1 | `0ab2c9bee231`  |
| 1366   | Layout 1 | `0ab2c9bee231`  |
| 1364   | Layout 1 | `0ab2c9bee231`  |
| 1363   | Layout 1 | `0ab2c9bee231`  |
| 1360   | Layout 1 | `0ab2c9bee231`  |
| 1358   | Layout 1 | `0ab2c9bee231`  |
| 1355   | Layout 1 | `0ab2c9bee231`  |
| 1351   | Layout 1 | `0ab2c9bee231`  |
| 1348   | Layout 1 | `0ab2c9bee231`  |
| 1346   | Layout 1 | `0ab2c9bee231`  |
| 1341   | Layout 1 | `0ab2c9bee231`  |
| 1340   | Layout 1 | `0ab2c9bee231`  |
| 1338   | Layout 1 | `0ab2c9bee231`  |
| 1335   | Layout 1 | `0ab2c9bee231`  |
| 1333   | Layout 1 | `0ab2c9bee231`  |
| 1329   | Layout 1 | `0ab2c9bee231`  |
| 1327   | Layout 1 | `0ab2c9bee231`  |
| 1324   | Layout 1 | `0ab2c9bee231`  |
| 1321   | Layout 1 | `0ab2c9bee231`  |
| 1319   | Layout 1 | `0ab2c9bee231`  |
| 1318   | Layout 1 | `0ab2c9bee231`  |
| 1316   | Layout 1 | `0ab2c9bee231`  |
| 1313   | Layout 1 | `0ab2c9bee231`  |
| 1311   | Layout 1 | `0ab2c9bee231`  |
| 1309   | Layout 1 | `0ab2c9bee231`  |
| 1304   | Layout 1 | `0ab2c9bee231`  |
| 1292   | Layout 1 | `0ab2c9bee231`  |
| 1286   | Layout 1 | `0ab2c9bee231`  |
| 1280   | Layout 1 | `0ab2c9bee231`  |
| 1276   | Layout 1 | `0ab2c9bee231`  |
| 1267   | Layout 1 | `0ab2c9bee231`  |
| 1261   | Layout 1 | `0ab2c9bee231`  |
| 1256   | Layout 1 | `0ab2c9bee231`  |
| 1250   | No file  | `0ab2c9bee231`  |
| 1246   | No file  | `0ab2c9bee231`  |
| 1239   | No file  | `0ab2c9bee231`  |
| 1230   | No file  | `0ab2c9bee231`  |
| 1226   | No file  | `0ab2c9bee231`  |
| 1220   | No file  | `0ab2c9bee231`  |
| 1217   | No file  | `0ab2c9bee231`  |
| 1211   | No file  | `0ab2c9bee231`  |
| 1210   | No file  | `0ab2c9bee231`  |
| 1208   | No file  | `0ab2c9bee231`  |
| 1203   | No file  | `0ab2c9bee231`  |
| 1197   | No file  | `0ab2c9bee231`  |
| 1194   | No file  | `0ab2c9bee231`  |
| 1192   | No file  | `0ab2c9bee231`  |
| 1187   | No file  | `0ab2c9bee231`  |
| 1183   | No file  | `0ab2c9bee231`  |
| 1177   | No file  | `0ab2c9bee231`  |
| 1173   | No file  | `0ab2c9bee231`  |
| 1167   | No file  | `0ab2c9bee231`  |
| 1164   | No file  | `0ab2c9bee231`  |
| 1156   | No file  | `0ab2c9bee231`  |
| 1149   | No file  | `0ab2c9bee231`  |
| 1144   | No file  | `0ab2c9bee231`  |
| 1137   | No file  | `0ab2c9bee231`  |
| 1132   | No file  | `0ab2c9bee231`  |
| 1127   | No file  | `0ab2c9bee231`  |
| 1122   | No file  | `0ab2c9bee231`  |
| 1118   | No file  | `0ab2c9bee231`  |
| 1114   | No file  | `0ab2c9bee231`  |
| 1109   | No file  | `0ab2c9bee231`  |
| 1102   | No file  | `0ab2c9bee231`  |
| 1096   | No file  | `0ab2c9bee231`  |
| 1088   | No file  | `0ab2c9bee231`  |
| 1081   | No file  | `0ab2c9bee231`  |
| 1076   | No file  | `0ab2c9bee231`  |
| 1069   | No file  | `0ab2c9bee231`  |
| 1064   | No file  | `0ab2c9bee231`  |
| 1058   | No file  | `0ab2c9bee231`  |
| 1051   | No file  | `0ab2c9bee231`  |
| 1044   | No file  | `0ab2c9bee231`  |
| 1036   | No file  | `0ab2c9bee231`  |
| 1026   | No file  | `0ab2c9bee231`  |
| 1016   | No file  | `0ab2c9bee231`  |
| 1009   | No file  | `0ab2c9bee231`  |
| 1005   | No file  | `0ab2c9bee231`  |
| 1000   | No file  | `0ab2c9bee231`  |
| 998    | No file  | `0ab2c9bee231`  |
| 990    | No file  | `0ab2c9bee231`  |
| 979    | No file  | `0ab2c9bee231`  |
| 972    | No file  | `0ab2c9bee231`  |
| 963    | No file  | `0ab2c9bee231`  |
| 955    | No file  | `0ab2c9bee231`  |
| 946    | No file  | `0ab2c9bee231`  |
| 938    | No file  | `0ab2c9bee231`  |
| 927    | No file  | `0ab2c9bee231`  |
| 911    | No file  | `0ab2c9bee231`  |
| 904    | No file  | `0ab2c9bee231`  |
| 899    | No file  | `0ab2c9bee231`  |
| 894    | No file  | `0ab2c9bee231`  |
| 885    | No file  | `0ab2c9bee231`  |
| 879    | No file  | `0ab2c9bee231`  |
| 872    | No file  | `0ab2c9bee231`  |
| 864    | No file  | `0ab2c9bee231`  |
| 855    | No file  | `0ab2c9bee231`  |
| 853    | No file  | `0ab2c9bee231`  |
| 845    | No file  | `0ab2c9bee231`  |
| 837    | No file  | `0ab2c9bee231`  |
| 829    | No file  | `0ab2c9bee231`  |
| 822    | No file  | `0ab2c9bee231`  |
| 814    | No file  | `0ab2c9bee231`  |
| 805    | No file  | `0ab2c9bee231`  |
| 794    | No file  | `0ab2c9bee231`  |
| 787    | No file  | `0ab2c9bee231`  |
| 780    | No file  | `0ab2c9bee231`  |
| 771    | No file  | `0ab2c9bee231`  |
| 760    | No file  | `0ab2c9bee231`  |
| 748    | No file  | `0ab2c9bee231`  |
| 741    | No file  | `0ab2c9bee231`  |
| 736    | No file  | `0ab2c9bee231`  |
| 731    | No file  | `0ab2c9bee231`  |
| 723    | No file  | `0ab2c9bee231`  |
| 711    | No file  | `0ab2c9bee231`  |
| 707    | No file  | `0ab2c9bee231`  |
| 697    | No file  | `0ab2c9bee231`  |
| 689    | No file  | `0ab2c9bee231`  |
| 683    | No file  | `0ab2c9bee231`  |
| 678    | No file  | `0ab2c9bee231`  |
| 670    | No file  | `0ab2c9bee231`  |
| 661    | No file  | `0ab2c9bee231`  |
| 656    | No file  | `0ab2c9bee231`  |
| 652    | No file  | `0ab2c9bee231`  |
| 643    | No file  | `0ab2c9bee231`  |
| 637    | No file  | `0ab2c9bee231`  |
| 630    | No file  | `0ab2c9bee231`  |
| 627    | No file  | `0ab2c9bee231`  |
| 621    | No file  | `0ab2c9bee231`  |
| 617    | No file  | `0ab2c9bee231`  |
| 615    | No file  | `0ab2c9bee231`  |
| 606    | No file  | `0ab2c9bee231`  |
| 599    | No file  | `0ab2c9bee231`  |
| 592    | No file  | `0ab2c9bee231`  |
| 586    | No file  | `0ab2c9bee231`  |
| 577    | No file  | `0ab2c9bee231`  |
| 569    | No file  | `0ab2c9bee231`  |
| 561    | No file  | `0ab2c9bee231`  |
| 554    | No file  | `0ab2c9bee231`  |
| 542    | No file  | `0ab2c9bee231`  |
| 532    | No file  | `0ab2c9bee231`  |
| 531    | No file  | `0ab2c9bee231`  |
| 526    | No file  | `0ab2c9bee231`  |
| 521    | No file  | `0ab2c9bee231`  |
| 517    | No file  | `0ab2c9bee231`  |
| 510    | No file  | `0ab2c9bee231`  |
| 508    | No file  | `0ab2c9bee231`  |
| 504    | No file  | `0ab2c9bee231`  |
| 497    | No file  | `0ab2c9bee231`  |
| 491    | No file  | `0ab2c9bee231`  |
| 485    | No file  | `0ab2c9bee231`  |
| 478    | No file  | `0ab2c9bee231`  |
| 472    | No file  | `0ab2c9bee231`  |
| 466    | No file  | `0ab2c9bee231`  |
| 457    | No file  | `0ab2c9bee231`  |
| 452    | No file  | `0ab2c9bee231`  |
| 449    | No file  | `0ab2c9bee231`  |
| 435    | No file  | `0ab2c9bee231`  |

<!-- versions:end -->

## Companion Files

None. The handler reads the groups in file order and does not need
`alchemychargeoffset.dbss` (see below). Item names come from LOC type 0 and
icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A group count, then the groups back to
back; the file ends after the last group.

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

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u32  | stone_type   | Equals the group index; see Stone Types                  |
| `+0x04` | u32  | item_id      | Material item; unique within a group                     |
| `+0x08` | u32  | charge_point | Durability points per use of the material (see Notes)    |

On client 3464 groups 0 to 2 hold the same 12 materials in the same order and
groups 3 to 7 are empty:

| Materials                                                          | charge_point |
| ------------------------------------------------------------------ | ------------ |
| Oils 6601 to 6605 (Regeneration, Storms, Fortitude, Corruption, Tranquility) | `10` |
| Bloods 6351 to 6355 (Legendary Beast's, Tyrant's, Clown's, Sinner's, Wise Man's) | `4` |
| Reagents 5301 Clear Liquid Reagent, 5302 Pure Powder Reagent       | `1`          |

### `alchemychargeoffset.dbss`

The same grouped walk: a u32 group count (equal to the main file's), then per
group a u32 row count and 12-byte rows. A row leaves out the stone type; its
group index stands for it.

| Offset  | Type                     | Field       | Notes                                  |
| ------- | ------------------------ | ----------- | -------------------------------------- |
| `+0x00` | u32                      | group_count | Equals the main file's `group_count`   |
| `+0x04` | Index Group[group_count] | groups      | Group `i` holds stone type `i`; see Index Group |

### Index Group (variable: 4 bytes + rows)

| Offset  | Type                 | Field     | Notes                                |
| ------- | -------------------- | --------- | ------------------------------------ |
| `+0x00` | u32                  | row_count | Equals the main group's `row_count`  |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                        |

### Index Row (12 bytes)

| Offset  | Type | Field   | Notes                                                        |
| ------- | ---- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32  | item_id | Row key together with the group index                        |
| `+0x04` | u32  | offset  | Start of the row in `alchemycharge.dbss`, at its `stone_type` |
| `+0x08` | u32  | size    | Always `12`, the main row size                               |

Every index row points at the main row with the same stone type and item, in
the same order. Both files are 468 bytes on client 3464, since every row is
12 bytes in both.

## Stone Types

The group index and `stone_type` are the alchemy stone's `_contentsEventParam1`,
which the alchemy stone Lua reads as the stone type
(`panel_window_alchemystone_all`, `invenStoneRClick`).

| stone_type | Stone       | Evidence                                                                 |
| ---------- | ----------- | ------------------------------------------------------------------------ |
| `0`        | Destruction | Lua names the Polishing material `LUA_ALCHEMYSTONE_PURESTONE` "Pure Metals"; the Alchemy Stone of Destruction tooltip says "Polishing Material: Pure metal crystals, ingots" |
| `1`        | Protection  | Lua `LUA_ALCHEMYSTONE_HARDWOOD` "Sturdy Plywood"; Protection tooltip "Sturdy plywood, plywood" |
| `2`        | Life        | Lua `LUA_ALCHEMYSTONE_CHOICEGOOD` "Special Crop"; Life tooltip "Special & high-quality crops" |
| `3` to `5` | `unknown`   | Empty groups                                                            |
| `6`, `7`   | Vell's Heart | `isAlchemyBellHeart()` in the same Lua returns true for these two types; empty groups |

The sibling [`alchemyupgrade.dbss`](alchemyupgrade_dbss.md) (the Polishing
materials) has the same grouped layout with 8 groups: group 0 holds ingots and
pure metal crystals, group 1 plywood and group 2 crops, which agrees with the
table above.

## Notes

- The Recharge tab asks the client for the points of one stone and material
  pair, `ToClient_GetAlchmeyStoneChargePoint(stone slot, material slot)`, and
  shows the material count needed to refill the stone as
  `ceil(lost durability / charge point) * getAlchemyStoneGrade()`
  (`panel_window_alchemystone_all`, `invenMatRClick`). The inventory filter
  for the material slot is `isAlchemyRepair(stone type)`. The pair key and the
  per-type groups match this file; the client code that reads it is not in Lua.
- The Recharge tab text (`LUA_ALCHEMYSTONE_RENEWAL_BOTTOM_DESC1`) lists
  "Oils, bloods, reagents, Mystical Spirit Powder, Vell's Fine Powder" as fuel.
  The last two are not in this file on client 3464.
- `charge_point` follows the material, not the stone: on client 3464 all three
  filled groups give the same value per item.

## Open Questions

### Stone Types 3 to 5

Groups 3, 4 and 5 are empty on client 3464 and no Lua names these types. The
renewal window (`panel_window_alchemystone_renewal_all`) skips stones with a
type above `2` in its Growth tab, so they are neither the three main stones
nor, by `isAlchemyBellHeart()`, Vell's Heart.

### Mystical Spirit Powder and Vell's Fine Powder

The Recharge tab lists both as fuel, but neither has a row here. Their points
may come from another table or from the item itself: the Mystical Spirit
Powder tooltip (item 4924) lists a count per stone grade, from "Imperfect
alchemy stone: x1" to "Shining alchemy stone: x8".

## In-Game Checks

### Durability per Material

Needs item (all):

- [Imperfect Alchemy Stone of Destruction](https://bdocodex.com/us/item/45201/), with lost durability
- [Oil of Regeneration](https://bdocodex.com/us/item/6601/)
- [Clown's Blood](https://bdocodex.com/us/item/6353/)

Put the stone in the Recharge tab, note its durability (`current / max`), then
pick each material and read Required Amount. The Lua shows
`ceil(lost / charge point) * grade`, so if the Oil's amount is
`ceil(lost / 10)` and the Blood's `ceil(lost / 4)` times the same whole
number, `charge_point` reaches the Lua as stored. A different ratio means the
client scales it by the stone first.
