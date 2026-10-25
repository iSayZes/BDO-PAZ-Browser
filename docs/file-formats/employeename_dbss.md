# `employeename.dbss` Format

## Purpose

Employee name table. Maps small employee name IDs to inline Korean UTF-16LE source names used by employee-related records. English display names are available through LOC `str_type=71`, `str_id1=employee_name_id`, `str_id3=12`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes | Records          | Row bytes               |
| ------ | -------------- | ------------------------- | ----- | ---------------- | ----------------------- |
| 1      | 1280 and later | `employeename.dbss`       | 1,298 | 60 Name Record   | 18 to 26, 22 on average |
| 1      | 1280 and later | `employeenameoffset.dbss` | 724   | 60 Offset Record | 12                      |

| Layout | File                      | Known           | Unknown       |
| ------ | ------------------------- | --------------- | ------------- |
| 1      | `employeename.dbss`       | 1,058 B (81.5%) | 240 B (18.5%) |
| 1      | `employeenameoffset.dbss` | 724 B (100.0%)  | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `c53ad546058f`  |
| 3482   | Layout 1             | `c53ad546058f`  |
| 3474   | Layout 1             | `c53ad546058f`  |
| 3473   | Layout 1             | `c53ad546058f`  |
| 3464   | Layout 1             | `c53ad546058f`  |
| 3458   | Layout 1             | `c53ad546058f`  |
| 3454   | Layout 1             | `c53ad546058f`  |
| 3444   | Layout 1             | `c53ad546058f`  |
| 3435   | Layout 1             | `c53ad546058f`  |
| 3426   | Layout 1             | `c53ad546058f`  |
| 3418   | Layout 1             | `c53ad546058f`  |
| 3412   | Layout 1             | `c53ad546058f`  |
| 3402   | Layout 1             | `c53ad546058f`  |
| 3396   | Layout 1             | `c53ad546058f`  |
| 3387   | Layout 1             | `c53ad546058f`  |
| 3381   | Layout 1             | `c53ad546058f`  |
| 3373   | Layout 1             | `c53ad546058f`  |
| 3364   | Layout 1             | `c53ad546058f`  |
| 3356   | Layout 1             | `c53ad546058f`  |
| 3349   | Layout 1             | `c53ad546058f`  |
| 3342   | Layout 1             | `c53ad546058f`  |
| 3335   | Layout 1             | `c53ad546058f`  |
| 3326   | Layout 1             | `c53ad546058f`  |
| 3321   | Layout 1             | `c53ad546058f`  |
| 3314   | Layout 1             | `c53ad546058f`  |
| 3303   | Layout 1             | `c53ad546058f`  |
| 3302   | Layout 1             | `c53ad546058f`  |
| 3293   | Layout 1             | `c53ad546058f`  |
| 3283   | Layout 1             | `c53ad546058f`  |
| 3275   | Layout 1             | `c53ad546058f`  |
| 3267   | Layout 1             | `c53ad546058f`  |
| 3258   | Layout 1             | `c53ad546058f`  |
| 3251   | Layout 1             | `c53ad546058f`  |
| 3242   | Layout 1             | `c53ad546058f`  |
| 3235   | Layout 1             | `c53ad546058f`  |
| 3229   | Layout 1             | `c53ad546058f`  |
| 3212   | Layout 1             | `c53ad546058f`  |
| 3203   | Layout 1             | `c53ad546058f`  |
| 3193   | Layout 1             | `c53ad546058f`  |
| 3186   | Layout 1             | `c53ad546058f`  |
| 3177   | Layout 1             | `c53ad546058f`  |
| 3169   | Layout 1             | `c53ad546058f`  |
| 3158   | Layout 1             | `c53ad546058f`  |
| 3151   | Layout 1             | `c53ad546058f`  |
| 3144   | Layout 1             | `c53ad546058f`  |
| 3133   | Layout 1             | `c53ad546058f`  |
| 3125   | Layout 1             | `c53ad546058f`  |
| 3118   | Layout 1             | `c53ad546058f`  |
| 3111   | Layout 1             | `c53ad546058f`  |
| 3103   | Layout 1             | `c53ad546058f`  |
| 3095   | Layout 1             | `c53ad546058f`  |
| 3086   | Layout 1             | `c53ad546058f`  |
| 3072   | Layout 1             | `c53ad546058f`  |
| 3062   | Layout 1             | `c53ad546058f`  |
| 3052   | Layout 1             | `c53ad546058f`  |
| 3045   | Layout 1             | `c53ad546058f`  |
| 3037   | Layout 1             | `c53ad546058f`  |
| 3030   | Layout 1             | `c53ad546058f`  |
| 3021   | Layout 1             | `c53ad546058f`  |
| 3012   | Layout 1             | `c53ad546058f`  |
| 3002   | Layout 1             | `c53ad546058f`  |
| 2995   | Layout 1             | `c53ad546058f`  |
| 2987   | Layout 1             | `c53ad546058f`  |
| 2978   | Layout 1             | `c53ad546058f`  |
| 2970   | Layout 1             | `c53ad546058f`  |
| 2959   | Layout 1             | `c53ad546058f`  |
| 2951   | Layout 1             | `c53ad546058f`  |
| 2942   | Layout 1             | `c53ad546058f`  |
| 2935   | Layout 1             | `c53ad546058f`  |
| 2932   | Layout 1             | `c53ad546058f`  |
| 2923   | Layout 1             | `c53ad546058f`  |
| 2919   | Layout 1             | `c53ad546058f`  |
| 2907   | Layout 1             | `c53ad546058f`  |
| 2900   | Layout 1             | `c53ad546058f`  |
| 2891   | Layout 1             | `c53ad546058f`  |
| 2882   | Layout 1             | `c53ad546058f`  |
| 2872   | Layout 1             | `c53ad546058f`  |
| 2863   | Layout 1             | `c53ad546058f`  |
| 2855   | Layout 1             | `c53ad546058f`  |
| 2849   | Layout 1             | `c53ad546058f`  |
| 2844   | Layout 1             | `c53ad546058f`  |
| 2834   | Layout 1             | `c53ad546058f`  |
| 2825   | Layout 1             | `c53ad546058f`  |
| 2819   | Layout 1             | `c53ad546058f`  |
| 2811   | Layout 1             | `c53ad546058f`  |
| 2803   | Layout 1             | `c53ad546058f`  |
| 2794   | Layout 1             | `c53ad546058f`  |
| 2783   | Layout 1             | `c53ad546058f`  |
| 2774   | Layout 1             | `c53ad546058f`  |
| 2765   | Layout 1             | `c53ad546058f`  |
| 2756   | Layout 1             | `c53ad546058f`  |
| 2750   | Layout 1             | `c53ad546058f`  |
| 2743   | Layout 1             | `c53ad546058f`  |
| 2736   | Layout 1             | `c53ad546058f`  |
| 2726   | Layout 1             | `c53ad546058f`  |
| 2717   | Layout 1             | `c53ad546058f`  |
| 2709   | Layout 1             | `c53ad546058f`  |
| 2703   | Layout 1             | `c53ad546058f`  |
| 2695   | Layout 1             | `c53ad546058f`  |
| 2684   | Layout 1             | `c53ad546058f`  |
| 2672   | Layout 1             | `c53ad546058f`  |
| 2665   | Layout 1             | `c53ad546058f`  |
| 2657   | Layout 1             | `c53ad546058f`  |
| 2649   | Layout 1             | `c53ad546058f`  |
| 2644   | Layout 1             | `c53ad546058f`  |
| 2637   | Layout 1             | `c53ad546058f`  |
| 2629   | Layout 1             | `c53ad546058f`  |
| 2619   | Layout 1             | `c53ad546058f`  |
| 2612   | Layout 1             | `c53ad546058f`  |
| 2606   | Layout 1             | `c53ad546058f`  |
| 2602   | Layout 1             | `c53ad546058f`  |
| 2601   | Layout 1             | `c53ad546058f`  |
| 2592   | Layout 1             | `c53ad546058f`  |
| 2583   | Layout 1             | `c53ad546058f`  |
| 2575   | Layout 1             | `c53ad546058f`  |
| 2567   | Layout 1             | `c53ad546058f`  |
| 2560   | Layout 1             | `c53ad546058f`  |
| 2553   | Layout 1             | `c53ad546058f`  |
| 2545   | Layout 1             | `c53ad546058f`  |
| 2538   | Layout 1             | `c53ad546058f`  |
| 2529   | Layout 1             | `c53ad546058f`  |
| 2519   | Layout 1             | `c53ad546058f`  |
| 2513   | Layout 1             | `c53ad546058f`  |
| 2510   | Layout 1             | `c53ad546058f`  |
| 2507   | Layout 1             | `c53ad546058f`  |
| 2503   | Layout 1             | `c53ad546058f`  |
| 2498   | Layout 1             | `c53ad546058f`  |
| 2492   | Layout 1             | `c53ad546058f`  |
| 2487   | Layout 1             | `c53ad546058f`  |
| 2480   | Layout 1             | `c53ad546058f`  |
| 2474   | Layout 1             | `c53ad546058f`  |
| 2468   | Layout 1             | `c53ad546058f`  |
| 2460   | Layout 1             | `c53ad546058f`  |
| 2453   | Layout 1             | `c53ad546058f`  |
| 2444   | Layout 1             | `c53ad546058f`  |
| 2438   | Layout 1             | `c53ad546058f`  |
| 2434   | Layout 1             | `c53ad546058f`  |
| 2429   | Layout 1             | `c53ad546058f`  |
| 2421   | Layout 1             | `c53ad546058f`  |
| 2414   | Layout 1             | `c53ad546058f`  |
| 2407   | Layout 1             | `c53ad546058f`  |
| 2401   | Layout 1             | `c53ad546058f`  |
| 2397   | Layout 1             | `c53ad546058f`  |
| 2393   | Layout 1             | `c53ad546058f`  |
| 2384   | Layout 1             | `c53ad546058f`  |
| 2378   | Layout 1             | `c53ad546058f`  |
| 2372   | Layout 1             | `c53ad546058f`  |
| 2358   | Layout 1             | `c53ad546058f`  |
| 2352   | Layout 1             | `c53ad546058f`  |
| 2347   | Layout 1             | `c53ad546058f`  |
| 2343   | Layout 1             | `c53ad546058f`  |
| 2335   | Layout 1             | `c53ad546058f`  |
| 2327   | Layout 1             | `c53ad546058f`  |
| 2324   | Layout 1             | `c53ad546058f`  |
| 2319   | Layout 1             | `c53ad546058f`  |
| 2313   | Layout 1             | `c53ad546058f`  |
| 2308   | Layout 1             | `c53ad546058f`  |
| 2302   | Layout 1             | `c53ad546058f`  |
| 2295   | Layout 1             | `c53ad546058f`  |
| 2290   | Layout 1             | `c53ad546058f`  |
| 2284   | Layout 1             | `c53ad546058f`  |
| 2276   | Layout 1             | `c53ad546058f`  |
| 2269   | Layout 1             | `c53ad546058f`  |
| 2259   | Layout 1             | `c53ad546058f`  |
| 2250   | Layout 1             | `c53ad546058f`  |
| 2243   | Layout 1             | `c53ad546058f`  |
| 2235   | Layout 1             | `c53ad546058f`  |
| 2229   | Layout 1             | `c53ad546058f`  |
| 2224   | Layout 1             | `c53ad546058f`  |
| 2218   | Layout 1             | `c53ad546058f`  |
| 2215   | Layout 1             | `c53ad546058f`  |
| 2207   | Layout 1             | `c53ad546058f`  |
| 2203   | Layout 1             | `c53ad546058f`  |
| 2196   | Layout 1             | `c53ad546058f`  |
| 2192   | Layout 1             | `c53ad546058f`  |
| 2189   | Layout 1             | `c53ad546058f`  |
| 2183   | Layout 1             | `c53ad546058f`  |
| 2179   | Layout 1             | `c53ad546058f`  |
| 2171   | Layout 1             | `c53ad546058f`  |
| 2163   | Layout 1             | `c53ad546058f`  |
| 2156   | Layout 1             | `c53ad546058f`  |
| 2151   | Layout 1             | `c53ad546058f`  |
| 2147   | Layout 1             | `c53ad546058f`  |
| 2142   | Layout 1             | `c53ad546058f`  |
| 2138   | Layout 1             | `c53ad546058f`  |
| 2134   | Layout 1             | `c53ad546058f`  |
| 2130   | Layout 1             | `c53ad546058f`  |
| 2122   | Layout 1             | `c53ad546058f`  |
| 2107   | Layout 1             | `c53ad546058f`  |
| 2098   | Layout 1             | `c53ad546058f`  |
| 2089   | Layout 1             | `c53ad546058f`  |
| 2081   | Layout 1             | `c53ad546058f`  |
| 2073   | Layout 1             | `c53ad546058f`  |
| 2067   | Layout 1             | `c53ad546058f`  |
| 2063   | Layout 1             | `c53ad546058f`  |
| 2059   | Layout 1             | `c53ad546058f`  |
| 2052   | Layout 1             | `c53ad546058f`  |
| 2044   | Layout 1             | `c53ad546058f`  |
| 2039   | Layout 1             | `c53ad546058f`  |
| 2032   | Layout 1             | `c53ad546058f`  |
| 2025   | Layout 1             | `c53ad546058f`  |
| 2011   | Layout 1             | `c53ad546058f`  |
| 2005   | Layout 1             | `c53ad546058f`  |
| 2000   | Layout 1             | `c53ad546058f`  |
| 1996   | Layout 1             | `c53ad546058f`  |
| 1991   | Layout 1             | `c53ad546058f`  |
| 1985   | Layout 1             | `c53ad546058f`  |
| 1980   | Layout 1             | `c53ad546058f`  |
| 1969   | Layout 1             | `c53ad546058f`  |
| 1964   | Layout 1             | `c53ad546058f`  |
| 1958   | Layout 1             | `c53ad546058f`  |
| 1950   | Layout 1             | `c53ad546058f`  |
| 1945   | Layout 1             | `c53ad546058f`  |
| 1937   | Layout 1             | `c53ad546058f`  |
| 1933   | Layout 1             | `c53ad546058f`  |
| 1927   | Layout 1             | `c53ad546058f`  |
| 1921   | Layout 1             | `c53ad546058f`  |
| 1914   | Layout 1             | `c53ad546058f`  |
| 1908   | Layout 1             | `c53ad546058f`  |
| 1897   | Layout 1             | `c53ad546058f`  |
| 1892   | Layout 1             | `c53ad546058f`  |
| 1886   | Layout 1             | `c53ad546058f`  |
| 1881   | Layout 1             | `c53ad546058f`  |
| 1871   | Layout 1             | `c53ad546058f`  |
| 1866   | Layout 1             | `c53ad546058f`  |
| 1862   | Layout 1             | `c53ad546058f`  |
| 1854   | Layout 1             | `c53ad546058f`  |
| 1846   | Layout 1             | `c53ad546058f`  |
| 1838   | Layout 1             | `c53ad546058f`  |
| 1832   | Layout 1             | `c53ad546058f`  |
| 1826   | Layout 1             | `c53ad546058f`  |
| 1822   | Layout 1             | `c53ad546058f`  |
| 1818   | Layout 1             | `c53ad546058f`  |
| 1804   | Layout 1             | `c53ad546058f`  |
| 1794   | Layout 1             | `c53ad546058f`  |
| 1790   | Layout 1             | `c53ad546058f`  |
| 1784   | Layout 1             | `c53ad546058f`  |
| 1774   | Layout 1             | `c53ad546058f`  |
| 1771   | Layout 1             | `c53ad546058f`  |
| 1762   | Layout 1             | `c53ad546058f`  |
| 1759   | Layout 1             | `c53ad546058f`  |
| 1754   | Layout 1             | `c53ad546058f`  |
| 1749   | Layout 1             | `c53ad546058f`  |
| 1743   | Layout 1             | `c53ad546058f`  |
| 1737   | Layout 1             | `c53ad546058f`  |
| 1731   | Layout 1             | `c53ad546058f`  |
| 1725   | Layout 1             | `c53ad546058f`  |
| 1717   | Layout 1             | `c53ad546058f`  |
| 1710   | Layout 1             | `c53ad546058f`  |
| 1704   | Layout 1             | `c53ad546058f`  |
| 1698   | Layout 1             | `c53ad546058f`  |
| 1690   | Layout 1             | `c53ad546058f`  |
| 1685   | Layout 1             | `c53ad546058f`  |
| 1680   | Layout 1             | `c53ad546058f`  |
| 1674   | Layout 1             | `c53ad546058f`  |
| 1668   | Layout 1             | `c53ad546058f`  |
| 1659   | Layout 1             | `c53ad546058f`  |
| 1649   | Layout 1             | `c53ad546058f`  |
| 1642   | Layout 1             | `c53ad546058f`  |
| 1636   | Layout 1             | `c53ad546058f`  |
| 1628   | Layout 1             | `c53ad546058f`  |
| 1622   | Layout 1             | `c53ad546058f`  |
| 1614   | Layout 1             | `c53ad546058f`  |
| 1608   | Layout 1             | `c53ad546058f`  |
| 1602   | Layout 1             | `c53ad546058f`  |
| 1598   | Layout 1             | `c53ad546058f`  |
| 1594   | Layout 1             | `c53ad546058f`  |
| 1590   | Layout 1             | `c53ad546058f`  |
| 1587   | Layout 1             | `c53ad546058f`  |
| 1584   | Layout 1             | `c53ad546058f`  |
| 1579   | Layout 1             | `c53ad546058f`  |
| 1572   | Layout 1             | `c53ad546058f`  |
| 1565   | Layout 1             | `c53ad546058f`  |
| 1559   | Layout 1             | `c53ad546058f`  |
| 1554   | Layout 1             | `c53ad546058f`  |
| 1547   | Layout 1             | `c53ad546058f`  |
| 1537   | Layout 1             | `c53ad546058f`  |
| 1529   | Layout 1             | `c53ad546058f`  |
| 1524   | Layout 1             | `c53ad546058f`  |
| 1519   | Layout 1             | `c53ad546058f`  |
| 1509   | Layout 1             | `c53ad546058f`  |
| 1506   | Layout 1             | `c53ad546058f`  |
| 1504   | Layout 1             | `c53ad546058f`  |
| 1500   | Layout 1             | `c53ad546058f`  |
| 1493   | Layout 1             | `c53ad546058f`  |
| 1489   | Layout 1             | `c53ad546058f`  |
| 1485   | Layout 1             | `c53ad546058f`  |
| 1481   | Layout 1             | `c53ad546058f`  |
| 1474   | Layout 1             | `c53ad546058f`  |
| 1466   | Layout 1             | `c53ad546058f`  |
| 1462   | Layout 1             | `c53ad546058f`  |
| 1459   | Layout 1             | `c53ad546058f`  |
| 1453   | Layout 1             | `c53ad546058f`  |
| 1450   | Layout 1             | `c53ad546058f`  |
| 1445   | Layout 1             | `c53ad546058f`  |
| 1439   | Layout 1             | `c53ad546058f`  |
| 1433   | Layout 1             | `c53ad546058f`  |
| 1430   | Layout 1             | `c53ad546058f`  |
| 1426   | Layout 1             | `c53ad546058f`  |
| 1421   | Layout 1             | `c53ad546058f`  |
| 1417   | Layout 1             | `c53ad546058f`  |
| 1416   | Layout 1             | `c53ad546058f`  |
| 1409   | Layout 1             | `c53ad546058f`  |
| 1405   | Layout 1             | `c53ad546058f`  |
| 1401   | Layout 1             | `c53ad546058f`  |
| 1396   | Layout 1             | `c53ad546058f`  |
| 1391   | Layout 1             | `c53ad546058f`  |
| 1390   | Layout 1             | `c53ad546058f`  |
| 1386   | Layout 1             | `c53ad546058f`  |
| 1381   | Layout 1             | `c53ad546058f`  |
| 1379   | Layout 1             | `c53ad546058f`  |
| 1372   | Layout 1             | `c53ad546058f`  |
| 1366   | Layout 1             | `c53ad546058f`  |
| 1364   | Layout 1             | `c53ad546058f`  |
| 1363   | Layout 1             | `c53ad546058f`  |
| 1360   | Layout 1             | `c53ad546058f`  |
| 1358   | Layout 1             | `c53ad546058f`  |
| 1355   | Layout 1             | `c53ad546058f`  |
| 1351   | Layout 1             | `c53ad546058f`  |
| 1348   | Layout 1             | `c53ad546058f`  |
| 1346   | Layout 1             | `c53ad546058f`  |
| 1341   | Layout 1             | `c53ad546058f`  |
| 1340   | Layout 1             | `c53ad546058f`  |
| 1338   | Layout 1             | `c53ad546058f`  |
| 1335   | Layout 1             | `c53ad546058f`  |
| 1333   | Layout 1             | `c53ad546058f`  |
| 1329   | Layout 1             | `c53ad546058f`  |
| 1327   | Layout 1             | `c53ad546058f`  |
| 1324   | Layout 1             | `c53ad546058f`  |
| 1321   | Layout 1             | `c53ad546058f`  |
| 1319   | Layout 1             | `c53ad546058f`  |
| 1318   | Layout 1             | `c53ad546058f`  |
| 1316   | Layout 1             | `c53ad546058f`  |
| 1313   | Layout 1             | `c53ad546058f`  |
| 1311   | Layout 1             | `c53ad546058f`  |
| 1309   | Layout 1             | `c53ad546058f`  |
| 1304   | Layout 1             | `c53ad546058f`  |
| 1292   | Layout 1             | `c53ad546058f`  |
| 1286   | Layout 1             | `c53ad546058f`  |
| 1280   | Layout 1             | `c53ad546058f`  |
| 1276   | No documented layout | `c53ad546058f`  |
| 1267   | No documented layout | `c53ad546058f`  |
| 1261   | No file              | `c53ad546058f`  |
| 1256   | No file              | `c53ad546058f`  |
| 1250   | No file              | `c53ad546058f`  |
| 1246   | No file              | `c53ad546058f`  |
| 1239   | No file              | `c53ad546058f`  |
| 1230   | No file              | `c53ad546058f`  |
| 1226   | No file              | `c53ad546058f`  |
| 1220   | No file              | `c53ad546058f`  |
| 1217   | No file              | `c53ad546058f`  |
| 1211   | No file              | `c53ad546058f`  |
| 1210   | No file              | `c53ad546058f`  |
| 1208   | No file              | `c53ad546058f`  |
| 1203   | No file              | `c53ad546058f`  |
| 1197   | No file              | `c53ad546058f`  |
| 1194   | No file              | `c53ad546058f`  |
| 1192   | No file              | `c53ad546058f`  |
| 1187   | No file              | `c53ad546058f`  |
| 1183   | No file              | `c53ad546058f`  |
| 1177   | No file              | `c53ad546058f`  |
| 1173   | No file              | `c53ad546058f`  |
| 1167   | No file              | `c53ad546058f`  |
| 1164   | No file              | `c53ad546058f`  |
| 1156   | No file              | `c53ad546058f`  |
| 1149   | No file              | `c53ad546058f`  |
| 1144   | No file              | `c53ad546058f`  |
| 1137   | No file              | `c53ad546058f`  |
| 1132   | No file              | `c53ad546058f`  |
| 1127   | No file              | `c53ad546058f`  |
| 1122   | No file              | `c53ad546058f`  |
| 1118   | No file              | `c53ad546058f`  |
| 1114   | No file              | `c53ad546058f`  |
| 1109   | No file              | `c53ad546058f`  |
| 1102   | No file              | `c53ad546058f`  |
| 1096   | No file              | `c53ad546058f`  |
| 1088   | No file              | `c53ad546058f`  |
| 1081   | No file              | `c53ad546058f`  |
| 1076   | No file              | `c53ad546058f`  |
| 1069   | No file              | `c53ad546058f`  |
| 1064   | No file              | `c53ad546058f`  |
| 1058   | No file              | `c53ad546058f`  |
| 1051   | No file              | `c53ad546058f`  |
| 1044   | No file              | `c53ad546058f`  |
| 1036   | No file              | `c53ad546058f`  |
| 1026   | No file              | `c53ad546058f`  |
| 1016   | No file              | `c53ad546058f`  |
| 1009   | No file              | `c53ad546058f`  |
| 1005   | No file              | `c53ad546058f`  |
| 1000   | No file              | `c53ad546058f`  |
| 998    | No file              | `c53ad546058f`  |
| 990    | No file              | `c53ad546058f`  |
| 979    | No file              | `c53ad546058f`  |
| 972    | No file              | `c53ad546058f`  |
| 963    | No file              | `c53ad546058f`  |
| 955    | No file              | `c53ad546058f`  |
| 946    | No file              | `c53ad546058f`  |
| 938    | No file              | `c53ad546058f`  |
| 927    | No file              | `c53ad546058f`  |
| 911    | No file              | `c53ad546058f`  |
| 904    | No file              | `c53ad546058f`  |
| 899    | No file              | `c53ad546058f`  |
| 894    | No file              | `c53ad546058f`  |
| 885    | No file              | `c53ad546058f`  |
| 879    | No file              | `c53ad546058f`  |
| 872    | No file              | `c53ad546058f`  |
| 864    | No file              | `c53ad546058f`  |
| 855    | No file              | `c53ad546058f`  |
| 853    | No file              | `c53ad546058f`  |
| 845    | No file              | `c53ad546058f`  |
| 837    | No file              | `c53ad546058f`  |
| 829    | No file              | `c53ad546058f`  |
| 822    | No file              | `c53ad546058f`  |
| 814    | No file              | `c53ad546058f`  |
| 805    | No file              | `c53ad546058f`  |
| 794    | No file              | `c53ad546058f`  |
| 787    | No file              | `c53ad546058f`  |
| 780    | No file              | `c53ad546058f`  |
| 771    | No file              | `c53ad546058f`  |
| 760    | No file              | `c53ad546058f`  |
| 748    | No file              | `c53ad546058f`  |
| 741    | No file              | `c53ad546058f`  |
| 736    | No file              | `c53ad546058f`  |
| 731    | No file              | `c53ad546058f`  |
| 723    | No file              | `c53ad546058f`  |
| 711    | No file              | `c53ad546058f`  |
| 707    | No file              | `c53ad546058f`  |
| 697    | No file              | `c53ad546058f`  |
| 689    | No file              | `c53ad546058f`  |
| 683    | No file              | `c53ad546058f`  |
| 678    | No file              | `c53ad546058f`  |
| 670    | No file              | `c53ad546058f`  |
| 661    | No file              | `c53ad546058f`  |
| 656    | No file              | `c53ad546058f`  |
| 652    | No file              | `c53ad546058f`  |
| 643    | No file              | `c53ad546058f`  |
| 637    | No file              | `c53ad546058f`  |
| 630    | No file              | `c53ad546058f`  |
| 627    | No file              | `c53ad546058f`  |
| 621    | No file              | `c53ad546058f`  |
| 617    | No file              | `c53ad546058f`  |
| 615    | No file              | `c53ad546058f`  |
| 606    | No file              | `c53ad546058f`  |
| 599    | No file              | `c53ad546058f`  |
| 592    | No file              | `c53ad546058f`  |
| 586    | No file              | `c53ad546058f`  |
| 577    | No file              | `c53ad546058f`  |
| 569    | No file              | `c53ad546058f`  |
| 561    | No file              | `c53ad546058f`  |
| 554    | No file              | `c53ad546058f`  |
| 542    | No file              | `c53ad546058f`  |
| 532    | No file              | `c53ad546058f`  |
| 531    | No file              | `c53ad546058f`  |
| 526    | No file              | `c53ad546058f`  |
| 521    | No file              | `c53ad546058f`  |
| 517    | No file              | `c53ad546058f`  |
| 510    | No file              | `c53ad546058f`  |
| 508    | No file              | `c53ad546058f`  |
| 504    | No file              | `c53ad546058f`  |
| 497    | No file              | `c53ad546058f`  |
| 491    | No file              | `c53ad546058f`  |
| 485    | No file              | `c53ad546058f`  |
| 478    | No file              | `c53ad546058f`  |
| 472    | No file              | `c53ad546058f`  |
| 466    | No file              | `c53ad546058f`  |
| 457    | No file              | `c53ad546058f`  |
| 452    | No file              | `c53ad546058f`  |
| 449    | No file              | `c53ad546058f`  |
| 435    | No file              | `c53ad546058f`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                 |
| ------------------------- | -------- | ---------------------------------------------------- |
| `employeenameoffset.dbss` | Required | Maps employee name ID -> byte offset and record size |
| `languagedata_en.loc`     | Optional | English display name lookup                          |

Other extracted `employee*` files may reference the same employee ID/name namespace. `employeespawnposition.dbss` keys (1 to 5, 41 to 50) fall in this table's ID range but are spawn position keys, not name IDs (see [employeespawnposition](employeespawnposition_dbss.md)); larger employee files need separate reverse-engineering before their foreign-key fields can be confirmed.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The first record starts immediately at `+0x04`. Records are variable length and should be read through `employeenameoffset.dbss`.

| Offset  | Type               | Field   | Notes                                                                                            |
| ------- | ------------------ | ------- | ------------------------------------------------------------------------------------------------ |
| `+0x00` | u32                | count   | Number of name records; observed `60` in the pre-2026-09-27 fixture and in the 2026-09-27 client |
| `+0x04` | Name Record[count] | records | Variable-length name rows                                                                        |

### Name Record (variable: 16 bytes + name text)

A record is `16 + char_count * 2` bytes.

| Offset      | Type  | Field              | Notes                                                                                                                           |
| ----------- | ----- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `+0x00`     | u32   | employee_name_id   | Matches ID in `employeenameoffset.dbss`                                                                                         |
| `+0x04`     | str16 | name               | Inline Korean source name; the parser reads the u64 count as u32 `char_count` and u32 `unknown_08`, always `0` in observed data |
| `name+0x00` | u32   | unknown_after_name | Always `0` after the name text in observed data                                                                                 |

Observed record sizes are `18`, `20`, `22`, `24`, and `26` bytes, matching names from 1 to 5 UTF-16 code units.

### `employeenameoffset.dbss`

Required offset index for `employeename.dbss`.

| Offset  | Type                 | Field | Notes                                                    |
| ------- | -------------------- | ----- | -------------------------------------------------------- |
| `+0x00` | u32                  | count | Number of offset rows; observed `60`, matching main file |
| `+0x04` | Offset Record[count] | rows  | See Offset Record                                        |

### Offset Record (12 bytes)

| Offset  | Type | Field            | Notes                                |
| ------- | ---- | ---------------- | ------------------------------------ |
| `+0x00` | u32  | employee_name_id | Key for a name record                |
| `+0x04` | u32  | offset           | Byte offset into `employeename.dbss` |
| `+0x08` | u32  | size             | Record byte count                    |

To read a name record: seek to `offset` in `employeename.dbss`, read `size` bytes, and parse the Name Record structure above.

## Notes

- Record order is not numeric: observed order starts `47` down to `32`, then `60` down to `48`, then `15` down to `1`, then `31` down to `16`.
- Every offset-row ID matches the `employee_name_id` stored at the beginning of its target record.
- Every observed `unknown_08` and trailing `unknown_after_name` is zero. Earlier versions of this doc called `unknown_08` `unknown_0`, and `unknown_after_name` `terminator`.
- English LOC matches were confirmed for sampled IDs: `47` -> Guile, `34` -> Pilgrave, `15` -> Neil Moss, `1` -> Philav, `60` -> Tails.
- Earlier versions of this doc read the `employeespawnposition.dbss` keys `1`-`5` and `41`-`50` as IDs from this table. They are spawn position keys that `employeespawninfo.dbss` lists per sailor character; the overlap is by value only.

## Open Questions

### Employee Foreign Keys

None of the decoded sailor files hold an ID from this table. `employeestaticstatus.bss` and `employeeexp.bss` key their rows by sailor key (`1` to `29` and `1` to `23`), see [employeestaticstatus](employeestaticstatus_bss.md) and [employeeexp](employeeexp_bss.md); `employeespawnposition.dbss` keys are spawn position keys, and `employeespawninfo.dbss` holds a sailor key (`1` to `20`) and spawn position keys, see [employeespawninfo](employeespawninfo_dbss.md). Other employee DBSS files contain values that overlap this table's IDs, but those formats are not decoded enough to name exact fields here.
