# `growthpasspointshop.dbss` Format

## Purpose

A keyed table whose name points at a Growth Pass point shop. On client 3473
the file holds no records: it is a u32 count of `0`, and so is its offset
file. On client 1784 it holds 15 fixed-size 28-byte records; what their
fields mean is not known.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes | Records              | Row bytes |
| ------ | -------------- | -------------------------------- | ----- | -------------------- | --------- |
| 2      | 3418 and later | `growthpasspointshop.dbss`       | 4     | -                    | -         |
| 2      | 3418 and later | `growthpasspointshopoffset.dbss` | 4     | -                    | -         |
| 1      | 1717 to 3412   | `growthpasspointshop.dbss`       | 424   | 15 Point Shop Record | 28        |
| 1      | 1717 to 3412   | `growthpasspointshopoffset.dbss` | 184   | 15 Index Row         | 12        |

| Layout | File                             | Known          | Unknown       |
| ------ | -------------------------------- | -------------- | ------------- |
| 2      | `growthpasspointshop.dbss`       | 4 B (100.0%)   | 0 B (0.0%)    |
| 2      | `growthpasspointshopoffset.dbss` | 4 B (100.0%)   | 0 B (0.0%)    |
| 1      | `growthpasspointshop.dbss`       | 124 B (29.2%)  | 300 B (70.8%) |
| 1      | `growthpasspointshopoffset.dbss` | 184 B (100.0%) | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `17ff61920871`  |
| 3482   | Layout 2 | `17ff61920871`  |
| 3474   | Layout 2 | `17ff61920871`  |
| 3473   | Layout 2 | `17ff61920871`  |
| 3464   | Layout 2 | `17ff61920871`  |
| 3458   | Layout 2 | `17ff61920871`  |
| 3454   | Layout 2 | `17ff61920871`  |
| 3444   | Layout 2 | `17ff61920871`  |
| 3435   | Layout 2 | `17ff61920871`  |
| 3426   | Layout 2 | `17ff61920871`  |
| 3418   | Layout 2 | `17ff61920871`  |
| 3412   | Layout 1 | `17ff61920871`  |
| 3402   | Layout 1 | `17ff61920871`  |
| 3396   | Layout 1 | `17ff61920871`  |
| 3387   | Layout 1 | `17ff61920871`  |
| 3381   | Layout 1 | `17ff61920871`  |
| 3373   | Layout 1 | `17ff61920871`  |
| 3364   | Layout 1 | `17ff61920871`  |
| 3356   | Layout 1 | `17ff61920871`  |
| 3349   | Layout 1 | `17ff61920871`  |
| 3342   | Layout 1 | `17ff61920871`  |
| 3335   | Layout 1 | `17ff61920871`  |
| 3326   | Layout 1 | `17ff61920871`  |
| 3321   | Layout 1 | `17ff61920871`  |
| 3314   | Layout 1 | `17ff61920871`  |
| 3303   | Layout 1 | `17ff61920871`  |
| 3302   | Layout 1 | `17ff61920871`  |
| 3293   | Layout 1 | `17ff61920871`  |
| 3283   | Layout 1 | `17ff61920871`  |
| 3275   | Layout 1 | `17ff61920871`  |
| 3267   | Layout 1 | `17ff61920871`  |
| 3258   | Layout 1 | `17ff61920871`  |
| 3251   | Layout 1 | `17ff61920871`  |
| 3242   | Layout 1 | `17ff61920871`  |
| 3235   | Layout 1 | `17ff61920871`  |
| 3229   | Layout 1 | `17ff61920871`  |
| 3212   | Layout 1 | `17ff61920871`  |
| 3203   | Layout 1 | `17ff61920871`  |
| 3193   | Layout 1 | `17ff61920871`  |
| 3186   | Layout 1 | `17ff61920871`  |
| 3177   | Layout 1 | `17ff61920871`  |
| 3169   | Layout 1 | `17ff61920871`  |
| 3158   | Layout 1 | `17ff61920871`  |
| 3151   | Layout 1 | `17ff61920871`  |
| 3144   | Layout 1 | `17ff61920871`  |
| 3133   | Layout 1 | `17ff61920871`  |
| 3125   | Layout 1 | `17ff61920871`  |
| 3118   | Layout 1 | `17ff61920871`  |
| 3111   | Layout 1 | `17ff61920871`  |
| 3103   | Layout 1 | `17ff61920871`  |
| 3095   | Layout 1 | `17ff61920871`  |
| 3086   | Layout 1 | `17ff61920871`  |
| 3072   | Layout 1 | `17ff61920871`  |
| 3062   | Layout 1 | `17ff61920871`  |
| 3052   | Layout 1 | `17ff61920871`  |
| 3045   | Layout 1 | `17ff61920871`  |
| 3037   | Layout 1 | `17ff61920871`  |
| 3030   | Layout 1 | `17ff61920871`  |
| 3021   | Layout 1 | `17ff61920871`  |
| 3012   | Layout 1 | `17ff61920871`  |
| 3002   | Layout 1 | `17ff61920871`  |
| 2995   | Layout 1 | `17ff61920871`  |
| 2987   | Layout 1 | `17ff61920871`  |
| 2978   | Layout 1 | `17ff61920871`  |
| 2970   | Layout 1 | `17ff61920871`  |
| 2959   | Layout 1 | `17ff61920871`  |
| 2951   | Layout 1 | `17ff61920871`  |
| 2942   | Layout 1 | `17ff61920871`  |
| 2935   | Layout 1 | `17ff61920871`  |
| 2932   | Layout 1 | `17ff61920871`  |
| 2923   | Layout 1 | `17ff61920871`  |
| 2919   | Layout 1 | `17ff61920871`  |
| 2907   | Layout 1 | `17ff61920871`  |
| 2900   | Layout 1 | `17ff61920871`  |
| 2891   | Layout 1 | `17ff61920871`  |
| 2882   | Layout 1 | `17ff61920871`  |
| 2872   | Layout 1 | `17ff61920871`  |
| 2863   | Layout 1 | `17ff61920871`  |
| 2855   | Layout 1 | `17ff61920871`  |
| 2849   | Layout 1 | `17ff61920871`  |
| 2844   | Layout 1 | `17ff61920871`  |
| 2834   | Layout 1 | `17ff61920871`  |
| 2825   | Layout 1 | `17ff61920871`  |
| 2819   | Layout 1 | `17ff61920871`  |
| 2811   | Layout 1 | `17ff61920871`  |
| 2803   | Layout 1 | `17ff61920871`  |
| 2794   | Layout 1 | `17ff61920871`  |
| 2783   | Layout 1 | `17ff61920871`  |
| 2774   | Layout 1 | `17ff61920871`  |
| 2765   | Layout 1 | `17ff61920871`  |
| 2756   | Layout 1 | `17ff61920871`  |
| 2750   | Layout 1 | `17ff61920871`  |
| 2743   | Layout 1 | `17ff61920871`  |
| 2736   | Layout 1 | `17ff61920871`  |
| 2726   | Layout 1 | `17ff61920871`  |
| 2717   | Layout 1 | `17ff61920871`  |
| 2709   | Layout 1 | `17ff61920871`  |
| 2703   | Layout 1 | `17ff61920871`  |
| 2695   | Layout 1 | `17ff61920871`  |
| 2684   | Layout 1 | `17ff61920871`  |
| 2672   | Layout 1 | `17ff61920871`  |
| 2665   | Layout 1 | `17ff61920871`  |
| 2657   | Layout 1 | `17ff61920871`  |
| 2649   | Layout 1 | `17ff61920871`  |
| 2644   | Layout 1 | `17ff61920871`  |
| 2637   | Layout 1 | `17ff61920871`  |
| 2629   | Layout 1 | `17ff61920871`  |
| 2619   | Layout 1 | `17ff61920871`  |
| 2612   | Layout 1 | `17ff61920871`  |
| 2606   | Layout 1 | `17ff61920871`  |
| 2602   | Layout 1 | `17ff61920871`  |
| 2601   | Layout 1 | `17ff61920871`  |
| 2592   | Layout 1 | `17ff61920871`  |
| 2583   | Layout 1 | `17ff61920871`  |
| 2575   | Layout 1 | `17ff61920871`  |
| 2567   | Layout 1 | `17ff61920871`  |
| 2560   | Layout 1 | `17ff61920871`  |
| 2553   | Layout 1 | `17ff61920871`  |
| 2545   | Layout 1 | `17ff61920871`  |
| 2538   | Layout 1 | `17ff61920871`  |
| 2529   | Layout 1 | `17ff61920871`  |
| 2519   | Layout 1 | `17ff61920871`  |
| 2513   | Layout 1 | `17ff61920871`  |
| 2510   | Layout 1 | `17ff61920871`  |
| 2507   | Layout 1 | `17ff61920871`  |
| 2503   | Layout 1 | `17ff61920871`  |
| 2498   | Layout 1 | `17ff61920871`  |
| 2492   | Layout 1 | `17ff61920871`  |
| 2487   | Layout 1 | `17ff61920871`  |
| 2480   | Layout 1 | `17ff61920871`  |
| 2474   | Layout 1 | `17ff61920871`  |
| 2468   | Layout 1 | `17ff61920871`  |
| 2460   | Layout 1 | `17ff61920871`  |
| 2453   | Layout 1 | `17ff61920871`  |
| 2444   | Layout 1 | `17ff61920871`  |
| 2438   | Layout 1 | `17ff61920871`  |
| 2434   | Layout 1 | `17ff61920871`  |
| 2429   | Layout 1 | `17ff61920871`  |
| 2421   | Layout 1 | `17ff61920871`  |
| 2414   | Layout 1 | `17ff61920871`  |
| 2407   | Layout 1 | `17ff61920871`  |
| 2401   | Layout 1 | `17ff61920871`  |
| 2397   | Layout 1 | `17ff61920871`  |
| 2393   | Layout 1 | `17ff61920871`  |
| 2384   | Layout 1 | `17ff61920871`  |
| 2378   | Layout 1 | `17ff61920871`  |
| 2372   | Layout 1 | `17ff61920871`  |
| 2358   | Layout 1 | `17ff61920871`  |
| 2352   | Layout 1 | `17ff61920871`  |
| 2347   | Layout 1 | `17ff61920871`  |
| 2343   | Layout 1 | `17ff61920871`  |
| 2335   | Layout 1 | `17ff61920871`  |
| 2327   | Layout 1 | `17ff61920871`  |
| 2324   | Layout 1 | `17ff61920871`  |
| 2319   | Layout 1 | `17ff61920871`  |
| 2313   | Layout 1 | `17ff61920871`  |
| 2308   | Layout 1 | `17ff61920871`  |
| 2302   | Layout 1 | `17ff61920871`  |
| 2295   | Layout 1 | `17ff61920871`  |
| 2290   | Layout 1 | `17ff61920871`  |
| 2284   | Layout 1 | `17ff61920871`  |
| 2276   | Layout 1 | `17ff61920871`  |
| 2269   | Layout 1 | `17ff61920871`  |
| 2259   | Layout 1 | `17ff61920871`  |
| 2250   | Layout 1 | `17ff61920871`  |
| 2243   | Layout 1 | `17ff61920871`  |
| 2235   | Layout 1 | `17ff61920871`  |
| 2229   | Layout 1 | `17ff61920871`  |
| 2224   | Layout 1 | `17ff61920871`  |
| 2218   | Layout 1 | `17ff61920871`  |
| 2215   | Layout 1 | `17ff61920871`  |
| 2207   | Layout 1 | `17ff61920871`  |
| 2203   | Layout 1 | `17ff61920871`  |
| 2196   | Layout 1 | `17ff61920871`  |
| 2192   | Layout 1 | `17ff61920871`  |
| 2189   | Layout 1 | `17ff61920871`  |
| 2183   | Layout 1 | `17ff61920871`  |
| 2179   | Layout 1 | `17ff61920871`  |
| 2171   | Layout 1 | `17ff61920871`  |
| 2163   | Layout 1 | `17ff61920871`  |
| 2156   | Layout 1 | `17ff61920871`  |
| 2151   | Layout 1 | `17ff61920871`  |
| 2147   | Layout 1 | `17ff61920871`  |
| 2142   | Layout 1 | `17ff61920871`  |
| 2138   | Layout 1 | `17ff61920871`  |
| 2134   | Layout 1 | `17ff61920871`  |
| 2130   | Layout 1 | `17ff61920871`  |
| 2122   | Layout 1 | `17ff61920871`  |
| 2107   | Layout 1 | `17ff61920871`  |
| 2098   | Layout 1 | `17ff61920871`  |
| 2089   | Layout 1 | `17ff61920871`  |
| 2081   | Layout 1 | `17ff61920871`  |
| 2073   | Layout 1 | `17ff61920871`  |
| 2067   | Layout 1 | `17ff61920871`  |
| 2063   | Layout 1 | `17ff61920871`  |
| 2059   | Layout 1 | `17ff61920871`  |
| 2052   | Layout 1 | `17ff61920871`  |
| 2044   | Layout 1 | `17ff61920871`  |
| 2039   | Layout 1 | `17ff61920871`  |
| 2032   | Layout 1 | `17ff61920871`  |
| 2025   | Layout 1 | `17ff61920871`  |
| 2011   | Layout 1 | `17ff61920871`  |
| 2005   | Layout 1 | `17ff61920871`  |
| 2000   | Layout 1 | `17ff61920871`  |
| 1996   | Layout 1 | `17ff61920871`  |
| 1991   | Layout 1 | `17ff61920871`  |
| 1985   | Layout 1 | `17ff61920871`  |
| 1980   | Layout 1 | `17ff61920871`  |
| 1969   | Layout 1 | `17ff61920871`  |
| 1964   | Layout 1 | `17ff61920871`  |
| 1958   | Layout 1 | `17ff61920871`  |
| 1950   | Layout 1 | `17ff61920871`  |
| 1945   | Layout 1 | `17ff61920871`  |
| 1937   | Layout 1 | `17ff61920871`  |
| 1933   | Layout 1 | `17ff61920871`  |
| 1927   | Layout 1 | `17ff61920871`  |
| 1921   | Layout 1 | `17ff61920871`  |
| 1914   | Layout 1 | `17ff61920871`  |
| 1908   | Layout 1 | `17ff61920871`  |
| 1897   | Layout 1 | `17ff61920871`  |
| 1892   | Layout 1 | `17ff61920871`  |
| 1886   | Layout 1 | `17ff61920871`  |
| 1881   | Layout 1 | `17ff61920871`  |
| 1871   | Layout 1 | `17ff61920871`  |
| 1866   | Layout 1 | `17ff61920871`  |
| 1862   | Layout 1 | `17ff61920871`  |
| 1854   | Layout 1 | `17ff61920871`  |
| 1846   | Layout 1 | `17ff61920871`  |
| 1838   | Layout 1 | `17ff61920871`  |
| 1832   | Layout 1 | `17ff61920871`  |
| 1826   | Layout 1 | `17ff61920871`  |
| 1822   | Layout 1 | `17ff61920871`  |
| 1818   | Layout 1 | `17ff61920871`  |
| 1804   | Layout 1 | `17ff61920871`  |
| 1794   | Layout 1 | `17ff61920871`  |
| 1790   | Layout 1 | `17ff61920871`  |
| 1784   | Layout 1 | `17ff61920871`  |
| 1774   | Layout 1 | `17ff61920871`  |
| 1771   | Layout 1 | `17ff61920871`  |
| 1762   | Layout 1 | `17ff61920871`  |
| 1759   | Layout 1 | `17ff61920871`  |
| 1754   | Layout 1 | `17ff61920871`  |
| 1749   | Layout 1 | `17ff61920871`  |
| 1743   | Layout 1 | `17ff61920871`  |
| 1737   | Layout 1 | `17ff61920871`  |
| 1731   | Layout 1 | `17ff61920871`  |
| 1725   | Layout 1 | `17ff61920871`  |
| 1717   | Layout 1 | `17ff61920871`  |
| 1710   | No file  | `17ff61920871`  |
| 1704   | No file  | `17ff61920871`  |
| 1698   | No file  | `17ff61920871`  |
| 1690   | No file  | `17ff61920871`  |
| 1685   | No file  | `17ff61920871`  |
| 1680   | No file  | `17ff61920871`  |
| 1674   | No file  | `17ff61920871`  |
| 1668   | No file  | `17ff61920871`  |
| 1659   | No file  | `17ff61920871`  |
| 1649   | No file  | `17ff61920871`  |
| 1642   | No file  | `17ff61920871`  |
| 1636   | No file  | `17ff61920871`  |
| 1628   | No file  | `17ff61920871`  |
| 1622   | No file  | `17ff61920871`  |
| 1614   | No file  | `17ff61920871`  |
| 1608   | No file  | `17ff61920871`  |
| 1602   | No file  | `17ff61920871`  |
| 1598   | No file  | `17ff61920871`  |
| 1594   | No file  | `17ff61920871`  |
| 1590   | No file  | `17ff61920871`  |
| 1587   | No file  | `17ff61920871`  |
| 1584   | No file  | `17ff61920871`  |
| 1579   | No file  | `17ff61920871`  |
| 1572   | No file  | `17ff61920871`  |
| 1565   | No file  | `17ff61920871`  |
| 1559   | No file  | `17ff61920871`  |
| 1554   | No file  | `17ff61920871`  |
| 1547   | No file  | `17ff61920871`  |
| 1537   | No file  | `17ff61920871`  |
| 1529   | No file  | `17ff61920871`  |
| 1524   | No file  | `17ff61920871`  |
| 1519   | No file  | `17ff61920871`  |
| 1509   | No file  | `17ff61920871`  |
| 1506   | No file  | `17ff61920871`  |
| 1504   | No file  | `17ff61920871`  |
| 1500   | No file  | `17ff61920871`  |
| 1493   | No file  | `17ff61920871`  |
| 1489   | No file  | `17ff61920871`  |
| 1485   | No file  | `17ff61920871`  |
| 1481   | No file  | `17ff61920871`  |
| 1474   | No file  | `17ff61920871`  |
| 1466   | No file  | `17ff61920871`  |
| 1462   | No file  | `17ff61920871`  |
| 1459   | No file  | `17ff61920871`  |
| 1453   | No file  | `17ff61920871`  |
| 1450   | No file  | `17ff61920871`  |
| 1445   | No file  | `17ff61920871`  |
| 1439   | No file  | `17ff61920871`  |
| 1433   | No file  | `17ff61920871`  |
| 1430   | No file  | `17ff61920871`  |
| 1426   | No file  | `17ff61920871`  |
| 1421   | No file  | `17ff61920871`  |
| 1417   | No file  | `17ff61920871`  |
| 1416   | No file  | `17ff61920871`  |
| 1409   | No file  | `17ff61920871`  |
| 1405   | No file  | `17ff61920871`  |
| 1401   | No file  | `17ff61920871`  |
| 1396   | No file  | `17ff61920871`  |
| 1391   | No file  | `17ff61920871`  |
| 1390   | No file  | `17ff61920871`  |
| 1386   | No file  | `17ff61920871`  |
| 1381   | No file  | `17ff61920871`  |
| 1379   | No file  | `17ff61920871`  |
| 1372   | No file  | `17ff61920871`  |
| 1366   | No file  | `17ff61920871`  |
| 1364   | No file  | `17ff61920871`  |
| 1363   | No file  | `17ff61920871`  |
| 1360   | No file  | `17ff61920871`  |
| 1358   | No file  | `17ff61920871`  |
| 1355   | No file  | `17ff61920871`  |
| 1351   | No file  | `17ff61920871`  |
| 1348   | No file  | `17ff61920871`  |
| 1346   | No file  | `17ff61920871`  |
| 1341   | No file  | `17ff61920871`  |
| 1340   | No file  | `17ff61920871`  |
| 1338   | No file  | `17ff61920871`  |
| 1335   | No file  | `17ff61920871`  |
| 1333   | No file  | `17ff61920871`  |
| 1329   | No file  | `17ff61920871`  |
| 1327   | No file  | `17ff61920871`  |
| 1324   | No file  | `17ff61920871`  |
| 1321   | No file  | `17ff61920871`  |
| 1319   | No file  | `17ff61920871`  |
| 1318   | No file  | `17ff61920871`  |
| 1316   | No file  | `17ff61920871`  |
| 1313   | No file  | `17ff61920871`  |
| 1311   | No file  | `17ff61920871`  |
| 1309   | No file  | `17ff61920871`  |
| 1304   | No file  | `17ff61920871`  |
| 1292   | No file  | `17ff61920871`  |
| 1286   | No file  | `17ff61920871`  |
| 1280   | No file  | `17ff61920871`  |
| 1276   | No file  | `17ff61920871`  |
| 1267   | No file  | `17ff61920871`  |
| 1261   | No file  | `17ff61920871`  |
| 1256   | No file  | `17ff61920871`  |
| 1250   | No file  | `17ff61920871`  |
| 1246   | No file  | `17ff61920871`  |
| 1239   | No file  | `17ff61920871`  |
| 1230   | No file  | `17ff61920871`  |
| 1226   | No file  | `17ff61920871`  |
| 1220   | No file  | `17ff61920871`  |
| 1217   | No file  | `17ff61920871`  |
| 1211   | No file  | `17ff61920871`  |
| 1210   | No file  | `17ff61920871`  |
| 1208   | No file  | `17ff61920871`  |
| 1203   | No file  | `17ff61920871`  |
| 1197   | No file  | `17ff61920871`  |
| 1194   | No file  | `17ff61920871`  |
| 1192   | No file  | `17ff61920871`  |
| 1187   | No file  | `17ff61920871`  |
| 1183   | No file  | `17ff61920871`  |
| 1177   | No file  | `17ff61920871`  |
| 1173   | No file  | `17ff61920871`  |
| 1167   | No file  | `17ff61920871`  |
| 1164   | No file  | `17ff61920871`  |
| 1156   | No file  | `17ff61920871`  |
| 1149   | No file  | `17ff61920871`  |
| 1144   | No file  | `17ff61920871`  |
| 1137   | No file  | `17ff61920871`  |
| 1132   | No file  | `17ff61920871`  |
| 1127   | No file  | `17ff61920871`  |
| 1122   | No file  | `17ff61920871`  |
| 1118   | No file  | `17ff61920871`  |
| 1114   | No file  | `17ff61920871`  |
| 1109   | No file  | `17ff61920871`  |
| 1102   | No file  | `17ff61920871`  |
| 1096   | No file  | `17ff61920871`  |
| 1088   | No file  | `17ff61920871`  |
| 1081   | No file  | `17ff61920871`  |
| 1076   | No file  | `17ff61920871`  |
| 1069   | No file  | `17ff61920871`  |
| 1064   | No file  | `17ff61920871`  |
| 1058   | No file  | `17ff61920871`  |
| 1051   | No file  | `17ff61920871`  |
| 1044   | No file  | `17ff61920871`  |
| 1036   | No file  | `17ff61920871`  |
| 1026   | No file  | `17ff61920871`  |
| 1016   | No file  | `17ff61920871`  |
| 1009   | No file  | `17ff61920871`  |
| 1005   | No file  | `17ff61920871`  |
| 1000   | No file  | `17ff61920871`  |
| 998    | No file  | `17ff61920871`  |
| 990    | No file  | `17ff61920871`  |
| 979    | No file  | `17ff61920871`  |
| 972    | No file  | `17ff61920871`  |
| 963    | No file  | `17ff61920871`  |
| 955    | No file  | `17ff61920871`  |
| 946    | No file  | `17ff61920871`  |
| 938    | No file  | `17ff61920871`  |
| 927    | No file  | `17ff61920871`  |
| 911    | No file  | `17ff61920871`  |
| 904    | No file  | `17ff61920871`  |
| 899    | No file  | `17ff61920871`  |
| 894    | No file  | `17ff61920871`  |
| 885    | No file  | `17ff61920871`  |
| 879    | No file  | `17ff61920871`  |
| 872    | No file  | `17ff61920871`  |
| 864    | No file  | `17ff61920871`  |
| 855    | No file  | `17ff61920871`  |
| 853    | No file  | `17ff61920871`  |
| 845    | No file  | `17ff61920871`  |
| 837    | No file  | `17ff61920871`  |
| 829    | No file  | `17ff61920871`  |
| 822    | No file  | `17ff61920871`  |
| 814    | No file  | `17ff61920871`  |
| 805    | No file  | `17ff61920871`  |
| 794    | No file  | `17ff61920871`  |
| 787    | No file  | `17ff61920871`  |
| 780    | No file  | `17ff61920871`  |
| 771    | No file  | `17ff61920871`  |
| 760    | No file  | `17ff61920871`  |
| 748    | No file  | `17ff61920871`  |
| 741    | No file  | `17ff61920871`  |
| 736    | No file  | `17ff61920871`  |
| 731    | No file  | `17ff61920871`  |
| 723    | No file  | `17ff61920871`  |
| 711    | No file  | `17ff61920871`  |
| 707    | No file  | `17ff61920871`  |
| 697    | No file  | `17ff61920871`  |
| 689    | No file  | `17ff61920871`  |
| 683    | No file  | `17ff61920871`  |
| 678    | No file  | `17ff61920871`  |
| 670    | No file  | `17ff61920871`  |
| 661    | No file  | `17ff61920871`  |
| 656    | No file  | `17ff61920871`  |
| 652    | No file  | `17ff61920871`  |
| 643    | No file  | `17ff61920871`  |
| 637    | No file  | `17ff61920871`  |
| 630    | No file  | `17ff61920871`  |
| 627    | No file  | `17ff61920871`  |
| 621    | No file  | `17ff61920871`  |
| 617    | No file  | `17ff61920871`  |
| 615    | No file  | `17ff61920871`  |
| 606    | No file  | `17ff61920871`  |
| 599    | No file  | `17ff61920871`  |
| 592    | No file  | `17ff61920871`  |
| 586    | No file  | `17ff61920871`  |
| 577    | No file  | `17ff61920871`  |
| 569    | No file  | `17ff61920871`  |
| 561    | No file  | `17ff61920871`  |
| 554    | No file  | `17ff61920871`  |
| 542    | No file  | `17ff61920871`  |
| 532    | No file  | `17ff61920871`  |
| 531    | No file  | `17ff61920871`  |
| 526    | No file  | `17ff61920871`  |
| 521    | No file  | `17ff61920871`  |
| 517    | No file  | `17ff61920871`  |
| 510    | No file  | `17ff61920871`  |
| 508    | No file  | `17ff61920871`  |
| 504    | No file  | `17ff61920871`  |
| 497    | No file  | `17ff61920871`  |
| 491    | No file  | `17ff61920871`  |
| 485    | No file  | `17ff61920871`  |
| 478    | No file  | `17ff61920871`  |
| 472    | No file  | `17ff61920871`  |
| 466    | No file  | `17ff61920871`  |
| 457    | No file  | `17ff61920871`  |
| 452    | No file  | `17ff61920871`  |
| 449    | No file  | `17ff61920871`  |
| 435    | No file  | `17ff61920871`  |

<!-- versions:end -->

## Companion Files

None. `growthpasspointshopoffset.dbss` is the offset file of this table; the
PAZ Browser reads both with the Layout 1 records, so client 3473 shows an
empty table and client 1784 its 15 records.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type | Field | Notes                                 |
| ------- | ---- | ----- | ------------------------------------- |
| `+0x00` | u32  | count | Number of records; `0` on client 3473 |

### `growthpasspointshopoffset.dbss`

| Offset  | Type | Field | Notes                                       |
| ------- | ---- | ----- | ------------------------------------------- |
| `+0x00` | u32  | count | Equals the `growthpasspointshop.dbss` count |

## Layout 1

On client 1784 the table holds 15 records, each with an index row in
`growthpasspointshopoffset.dbss`.

### File Layout

| Offset  | Type                     | Field   | Notes                 |
| ------- | ------------------------ | ------- | --------------------- |
| `+0x00` | u32                      | count   | `15` on client 1784   |
| `+0x04` | Point Shop Record[count] | records | See Point Shop Record |

### Point Shop Record (28 bytes)

| Offset  | Type | Field      | Notes                                                    |
| ------- | ---- | ---------- | -------------------------------------------------------- |
| `+0x00` | u32  | key        | Record key, `15` down to `1`; equals the index row key   |
| `+0x04` | u32  | key_dup    | Repeats `key` on every record                            |
| `+0x08` | u32  | unknown_08 | `750367` on every record (client 1784)                   |
| `+0x0C` | u32  | unknown_0c | `2` on every record (client 1784)                        |
| `+0x10` | u32  | unknown_10 | `0` on every record (client 1784)                        |
| `+0x14` | u32  | unknown_14 | `1` to `100`; `10` on 10 of the 15 records (client 1784) |
| `+0x18` | u32  | unknown_18 | `1`, `2`, `5` or `10` (client 1784)                      |

### `growthpasspointshopoffset.dbss`

| Offset  | Type             | Field | Notes                                       |
| ------- | ---------------- | ----- | ------------------------------------------- |
| `+0x00` | u32              | count | Equals the `growthpasspointshop.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row                               |

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u32  | key    | The record's `key`                                       |
| `+0x04` | u32  | offset | Start of the record in the main file plus 4, after `key` |
| `+0x08` | u32  | size   | Record length minus the 4-byte `key`                     |

## Open Questions

### Current Record Layout

Client 3473 ships no records, so whether a filled table would still read
as the client 1784 Point Shop Record is unknown. The handler reads
a filled table as Layout 1 and raises an error when the bytes do not fit it.

### What the Point Shop Record Fields Hold

`unknown_08` to `unknown_18` have no name in client data. Only `unknown_14`
and `unknown_18` vary per record (client 1784); what they count is open.
