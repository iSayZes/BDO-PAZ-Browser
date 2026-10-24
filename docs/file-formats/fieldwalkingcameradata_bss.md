# `fieldwalkingcameradata.bss` Format

## Purpose

The camera paths of the field walking camera: each row is one named event
(`rebalenos_velia_001`, `recalpheon_peace_001`) in a region, with a list
of camera points the camera moves through, each a world position, a
rotation, a field of view and a speed or time to the next point. The file
is compiled from `fieldwalkingcamera/fieldwalkingcameradata.xml`, which
the client ships next to it. It is a PABR table of variable rows whose
event names sit in the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records         | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | --------------- | --------- |
| 1      | 2171 and later | 3483    | `fieldwalkingcameradata.bss` | 1,848 | 43 Point, 4 Row | 38        |

| Layout | File                         | Known           | Unknown     |
| ------ | ---------------------------- | --------------- | ----------- |
| 1      | `fieldwalkingcameradata.bss` | 1,832 B (99.1%) | 16 B (0.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `1501615fa31c`  |
| 3482   | Layout 1 | `1501615fa31c`  |
| 3474   | Layout 1 | `1501615fa31c`  |
| 3473   | Layout 1 | `1501615fa31c`  |
| 3464   | Layout 1 | `1501615fa31c`  |
| 3458   | Layout 1 | `1501615fa31c`  |
| 3454   | Layout 1 | `1501615fa31c`  |
| 3444   | Layout 1 | `1501615fa31c`  |
| 3435   | Layout 1 | `1501615fa31c`  |
| 3426   | Layout 1 | `1501615fa31c`  |
| 3418   | Layout 1 | `1501615fa31c`  |
| 3412   | Layout 1 | `1501615fa31c`  |
| 3402   | Layout 1 | `1501615fa31c`  |
| 3396   | Layout 1 | `1501615fa31c`  |
| 3387   | Layout 1 | `1501615fa31c`  |
| 3381   | Layout 1 | `1501615fa31c`  |
| 3373   | Layout 1 | `1501615fa31c`  |
| 3364   | Layout 1 | `1501615fa31c`  |
| 3356   | Layout 1 | `1501615fa31c`  |
| 3349   | Layout 1 | `1501615fa31c`  |
| 3342   | Layout 1 | `1501615fa31c`  |
| 3335   | Layout 1 | `1501615fa31c`  |
| 3326   | Layout 1 | `1501615fa31c`  |
| 3321   | Layout 1 | `1501615fa31c`  |
| 3314   | Layout 1 | `1501615fa31c`  |
| 3303   | Layout 1 | `1501615fa31c`  |
| 3302   | Layout 1 | `1501615fa31c`  |
| 3293   | Layout 1 | `1501615fa31c`  |
| 3283   | Layout 1 | `1501615fa31c`  |
| 3275   | Layout 1 | `1501615fa31c`  |
| 3267   | Layout 1 | `1501615fa31c`  |
| 3258   | Layout 1 | `1501615fa31c`  |
| 3251   | Layout 1 | `1501615fa31c`  |
| 3242   | Layout 1 | `1501615fa31c`  |
| 3235   | Layout 1 | `1501615fa31c`  |
| 3229   | Layout 1 | `1501615fa31c`  |
| 3212   | Layout 1 | `1501615fa31c`  |
| 3203   | Layout 1 | `1501615fa31c`  |
| 3193   | Layout 1 | `1501615fa31c`  |
| 3186   | Layout 1 | `1501615fa31c`  |
| 3177   | Layout 1 | `1501615fa31c`  |
| 3169   | Layout 1 | `1501615fa31c`  |
| 3158   | Layout 1 | `1501615fa31c`  |
| 3151   | Layout 1 | `1501615fa31c`  |
| 3144   | Layout 1 | `1501615fa31c`  |
| 3133   | Layout 1 | `1501615fa31c`  |
| 3125   | Layout 1 | `1501615fa31c`  |
| 3118   | Layout 1 | `1501615fa31c`  |
| 3111   | Layout 1 | `1501615fa31c`  |
| 3103   | Layout 1 | `1501615fa31c`  |
| 3095   | Layout 1 | `1501615fa31c`  |
| 3086   | Layout 1 | `1501615fa31c`  |
| 3072   | Layout 1 | `1501615fa31c`  |
| 3062   | Layout 1 | `1501615fa31c`  |
| 3052   | Layout 1 | `1501615fa31c`  |
| 3045   | Layout 1 | `1501615fa31c`  |
| 3037   | Layout 1 | `1501615fa31c`  |
| 3030   | Layout 1 | `1501615fa31c`  |
| 3021   | Layout 1 | `1501615fa31c`  |
| 3012   | Layout 1 | `1501615fa31c`  |
| 3002   | Layout 1 | `1501615fa31c`  |
| 2995   | Layout 1 | `1501615fa31c`  |
| 2987   | Layout 1 | `1501615fa31c`  |
| 2978   | Layout 1 | `1501615fa31c`  |
| 2970   | Layout 1 | `1501615fa31c`  |
| 2959   | Layout 1 | `1501615fa31c`  |
| 2951   | Layout 1 | `1501615fa31c`  |
| 2942   | Layout 1 | `1501615fa31c`  |
| 2935   | Layout 1 | `1501615fa31c`  |
| 2932   | Layout 1 | `1501615fa31c`  |
| 2923   | Layout 1 | `1501615fa31c`  |
| 2919   | Layout 1 | `1501615fa31c`  |
| 2907   | Layout 1 | `1501615fa31c`  |
| 2900   | Layout 1 | `1501615fa31c`  |
| 2891   | Layout 1 | `1501615fa31c`  |
| 2882   | Layout 1 | `1501615fa31c`  |
| 2872   | Layout 1 | `1501615fa31c`  |
| 2863   | Layout 1 | `1501615fa31c`  |
| 2855   | Layout 1 | `1501615fa31c`  |
| 2849   | Layout 1 | `1501615fa31c`  |
| 2844   | Layout 1 | `1501615fa31c`  |
| 2834   | Layout 1 | `1501615fa31c`  |
| 2825   | Layout 1 | `1501615fa31c`  |
| 2819   | Layout 1 | `1501615fa31c`  |
| 2811   | Layout 1 | `1501615fa31c`  |
| 2803   | Layout 1 | `1501615fa31c`  |
| 2794   | Layout 1 | `1501615fa31c`  |
| 2783   | Layout 1 | `1501615fa31c`  |
| 2774   | Layout 1 | `1501615fa31c`  |
| 2765   | Layout 1 | `1501615fa31c`  |
| 2756   | Layout 1 | `1501615fa31c`  |
| 2750   | Layout 1 | `1501615fa31c`  |
| 2743   | Layout 1 | `1501615fa31c`  |
| 2736   | Layout 1 | `1501615fa31c`  |
| 2726   | Layout 1 | `1501615fa31c`  |
| 2717   | Layout 1 | `1501615fa31c`  |
| 2709   | Layout 1 | `1501615fa31c`  |
| 2703   | Layout 1 | `1501615fa31c`  |
| 2695   | Layout 1 | `1501615fa31c`  |
| 2684   | Layout 1 | `1501615fa31c`  |
| 2672   | Layout 1 | `1501615fa31c`  |
| 2665   | Layout 1 | `1501615fa31c`  |
| 2657   | Layout 1 | `1501615fa31c`  |
| 2649   | Layout 1 | `1501615fa31c`  |
| 2644   | Layout 1 | `1501615fa31c`  |
| 2637   | Layout 1 | `1501615fa31c`  |
| 2629   | Layout 1 | `1501615fa31c`  |
| 2619   | Layout 1 | `1501615fa31c`  |
| 2612   | Layout 1 | `1501615fa31c`  |
| 2606   | Layout 1 | `1501615fa31c`  |
| 2602   | Layout 1 | `1501615fa31c`  |
| 2601   | Layout 1 | `1501615fa31c`  |
| 2592   | Layout 1 | `1501615fa31c`  |
| 2583   | Layout 1 | `1501615fa31c`  |
| 2575   | Layout 1 | `1501615fa31c`  |
| 2567   | Layout 1 | `1501615fa31c`  |
| 2560   | Layout 1 | `1501615fa31c`  |
| 2553   | Layout 1 | `1501615fa31c`  |
| 2545   | Layout 1 | `1501615fa31c`  |
| 2538   | Layout 1 | `1501615fa31c`  |
| 2529   | Layout 1 | `1501615fa31c`  |
| 2519   | Layout 1 | `1501615fa31c`  |
| 2513   | Layout 1 | `1501615fa31c`  |
| 2510   | Layout 1 | `1501615fa31c`  |
| 2507   | Layout 1 | `1501615fa31c`  |
| 2503   | Layout 1 | `1501615fa31c`  |
| 2498   | Layout 1 | `1501615fa31c`  |
| 2492   | Layout 1 | `1501615fa31c`  |
| 2487   | Layout 1 | `1501615fa31c`  |
| 2480   | Layout 1 | `1501615fa31c`  |
| 2474   | Layout 1 | `1501615fa31c`  |
| 2468   | Layout 1 | `1501615fa31c`  |
| 2460   | Layout 1 | `1501615fa31c`  |
| 2453   | Layout 1 | `1501615fa31c`  |
| 2444   | Layout 1 | `1501615fa31c`  |
| 2438   | Layout 1 | `1501615fa31c`  |
| 2434   | Layout 1 | `1501615fa31c`  |
| 2429   | Layout 1 | `1501615fa31c`  |
| 2421   | Layout 1 | `1501615fa31c`  |
| 2414   | Layout 1 | `1501615fa31c`  |
| 2407   | Layout 1 | `1501615fa31c`  |
| 2401   | Layout 1 | `1501615fa31c`  |
| 2397   | Layout 1 | `1501615fa31c`  |
| 2393   | Layout 1 | `1501615fa31c`  |
| 2384   | Layout 1 | `1501615fa31c`  |
| 2378   | Layout 1 | `1501615fa31c`  |
| 2372   | Layout 1 | `1501615fa31c`  |
| 2358   | Layout 1 | `1501615fa31c`  |
| 2352   | Layout 1 | `1501615fa31c`  |
| 2347   | Layout 1 | `1501615fa31c`  |
| 2343   | Layout 1 | `1501615fa31c`  |
| 2335   | Layout 1 | `1501615fa31c`  |
| 2327   | Layout 1 | `1501615fa31c`  |
| 2324   | Layout 1 | `1501615fa31c`  |
| 2319   | Layout 1 | `1501615fa31c`  |
| 2313   | Layout 1 | `1501615fa31c`  |
| 2308   | Layout 1 | `1501615fa31c`  |
| 2302   | Layout 1 | `1501615fa31c`  |
| 2295   | Layout 1 | `1501615fa31c`  |
| 2290   | Layout 1 | `1501615fa31c`  |
| 2284   | Layout 1 | `1501615fa31c`  |
| 2276   | Layout 1 | `1501615fa31c`  |
| 2269   | Layout 1 | `1501615fa31c`  |
| 2259   | Layout 1 | `1501615fa31c`  |
| 2250   | Layout 1 | `1501615fa31c`  |
| 2243   | Layout 1 | `1501615fa31c`  |
| 2235   | Layout 1 | `1501615fa31c`  |
| 2229   | Layout 1 | `1501615fa31c`  |
| 2224   | Layout 1 | `1501615fa31c`  |
| 2218   | Layout 1 | `1501615fa31c`  |
| 2215   | Layout 1 | `1501615fa31c`  |
| 2207   | Layout 1 | `1501615fa31c`  |
| 2203   | Layout 1 | `1501615fa31c`  |
| 2196   | Layout 1 | `1501615fa31c`  |
| 2192   | Layout 1 | `1501615fa31c`  |
| 2189   | Layout 1 | `1501615fa31c`  |
| 2183   | Layout 1 | `1501615fa31c`  |
| 2179   | Layout 1 | `1501615fa31c`  |
| 2171   | Layout 1 | `1501615fa31c`  |
| 2163   | No file  | `1501615fa31c`  |
| 2156   | No file  | `1501615fa31c`  |
| 2151   | No file  | `1501615fa31c`  |
| 2147   | No file  | `1501615fa31c`  |
| 2142   | No file  | `1501615fa31c`  |
| 2138   | No file  | `1501615fa31c`  |
| 2134   | No file  | `1501615fa31c`  |
| 2130   | No file  | `1501615fa31c`  |
| 2122   | No file  | `1501615fa31c`  |
| 2107   | No file  | `1501615fa31c`  |
| 2098   | No file  | `1501615fa31c`  |
| 2089   | No file  | `1501615fa31c`  |
| 2081   | No file  | `1501615fa31c`  |
| 2073   | No file  | `1501615fa31c`  |
| 2067   | No file  | `1501615fa31c`  |
| 2063   | No file  | `1501615fa31c`  |
| 2059   | No file  | `1501615fa31c`  |
| 2052   | No file  | `1501615fa31c`  |
| 2044   | No file  | `1501615fa31c`  |
| 2039   | No file  | `1501615fa31c`  |
| 2032   | No file  | `1501615fa31c`  |
| 2025   | No file  | `1501615fa31c`  |
| 2011   | No file  | `1501615fa31c`  |
| 2005   | No file  | `1501615fa31c`  |
| 2000   | No file  | `1501615fa31c`  |
| 1996   | No file  | `1501615fa31c`  |
| 1991   | No file  | `1501615fa31c`  |
| 1985   | No file  | `1501615fa31c`  |
| 1980   | No file  | `1501615fa31c`  |
| 1969   | No file  | `1501615fa31c`  |
| 1964   | No file  | `1501615fa31c`  |
| 1958   | No file  | `1501615fa31c`  |
| 1950   | No file  | `1501615fa31c`  |
| 1945   | No file  | `1501615fa31c`  |
| 1937   | No file  | `1501615fa31c`  |
| 1933   | No file  | `1501615fa31c`  |
| 1927   | No file  | `1501615fa31c`  |
| 1921   | No file  | `1501615fa31c`  |
| 1914   | No file  | `1501615fa31c`  |
| 1908   | No file  | `1501615fa31c`  |
| 1897   | No file  | `1501615fa31c`  |
| 1892   | No file  | `1501615fa31c`  |
| 1886   | No file  | `1501615fa31c`  |
| 1881   | No file  | `1501615fa31c`  |
| 1871   | No file  | `1501615fa31c`  |
| 1866   | No file  | `1501615fa31c`  |
| 1862   | No file  | `1501615fa31c`  |
| 1854   | No file  | `1501615fa31c`  |
| 1846   | No file  | `1501615fa31c`  |
| 1838   | No file  | `1501615fa31c`  |
| 1832   | No file  | `1501615fa31c`  |
| 1826   | No file  | `1501615fa31c`  |
| 1822   | No file  | `1501615fa31c`  |
| 1818   | No file  | `1501615fa31c`  |
| 1804   | No file  | `1501615fa31c`  |
| 1794   | No file  | `1501615fa31c`  |
| 1790   | No file  | `1501615fa31c`  |
| 1784   | No file  | `1501615fa31c`  |
| 1774   | No file  | `1501615fa31c`  |
| 1771   | No file  | `1501615fa31c`  |
| 1762   | No file  | `1501615fa31c`  |
| 1759   | No file  | `1501615fa31c`  |
| 1754   | No file  | `1501615fa31c`  |
| 1749   | No file  | `1501615fa31c`  |
| 1743   | No file  | `1501615fa31c`  |
| 1737   | No file  | `1501615fa31c`  |
| 1731   | No file  | `1501615fa31c`  |
| 1725   | No file  | `1501615fa31c`  |
| 1717   | No file  | `1501615fa31c`  |
| 1710   | No file  | `1501615fa31c`  |
| 1704   | No file  | `1501615fa31c`  |
| 1698   | No file  | `1501615fa31c`  |
| 1690   | No file  | `1501615fa31c`  |
| 1685   | No file  | `1501615fa31c`  |
| 1680   | No file  | `1501615fa31c`  |
| 1674   | No file  | `1501615fa31c`  |
| 1668   | No file  | `1501615fa31c`  |
| 1659   | No file  | `1501615fa31c`  |
| 1649   | No file  | `1501615fa31c`  |
| 1642   | No file  | `1501615fa31c`  |
| 1636   | No file  | `1501615fa31c`  |
| 1628   | No file  | `1501615fa31c`  |
| 1622   | No file  | `1501615fa31c`  |
| 1614   | No file  | `1501615fa31c`  |
| 1608   | No file  | `1501615fa31c`  |
| 1602   | No file  | `1501615fa31c`  |
| 1598   | No file  | `1501615fa31c`  |
| 1594   | No file  | `1501615fa31c`  |
| 1590   | No file  | `1501615fa31c`  |
| 1587   | No file  | `1501615fa31c`  |
| 1584   | No file  | `1501615fa31c`  |
| 1579   | No file  | `1501615fa31c`  |
| 1572   | No file  | `1501615fa31c`  |
| 1565   | No file  | `1501615fa31c`  |
| 1559   | No file  | `1501615fa31c`  |
| 1554   | No file  | `1501615fa31c`  |
| 1547   | No file  | `1501615fa31c`  |
| 1537   | No file  | `1501615fa31c`  |
| 1529   | No file  | `1501615fa31c`  |
| 1524   | No file  | `1501615fa31c`  |
| 1519   | No file  | `1501615fa31c`  |
| 1509   | No file  | `1501615fa31c`  |
| 1506   | No file  | `1501615fa31c`  |
| 1504   | No file  | `1501615fa31c`  |
| 1500   | No file  | `1501615fa31c`  |
| 1493   | No file  | `1501615fa31c`  |
| 1489   | No file  | `1501615fa31c`  |
| 1485   | No file  | `1501615fa31c`  |
| 1481   | No file  | `1501615fa31c`  |
| 1474   | No file  | `1501615fa31c`  |
| 1466   | No file  | `1501615fa31c`  |
| 1462   | No file  | `1501615fa31c`  |
| 1459   | No file  | `1501615fa31c`  |
| 1453   | No file  | `1501615fa31c`  |
| 1450   | No file  | `1501615fa31c`  |
| 1445   | No file  | `1501615fa31c`  |
| 1439   | No file  | `1501615fa31c`  |
| 1433   | No file  | `1501615fa31c`  |
| 1430   | No file  | `1501615fa31c`  |
| 1426   | No file  | `1501615fa31c`  |
| 1421   | No file  | `1501615fa31c`  |
| 1417   | No file  | `1501615fa31c`  |
| 1416   | No file  | `1501615fa31c`  |
| 1409   | No file  | `1501615fa31c`  |
| 1405   | No file  | `1501615fa31c`  |
| 1401   | No file  | `1501615fa31c`  |
| 1396   | No file  | `1501615fa31c`  |
| 1391   | No file  | `1501615fa31c`  |
| 1390   | No file  | `1501615fa31c`  |
| 1386   | No file  | `1501615fa31c`  |
| 1381   | No file  | `1501615fa31c`  |
| 1379   | No file  | `1501615fa31c`  |
| 1372   | No file  | `1501615fa31c`  |
| 1366   | No file  | `1501615fa31c`  |
| 1364   | No file  | `1501615fa31c`  |
| 1363   | No file  | `1501615fa31c`  |
| 1360   | No file  | `1501615fa31c`  |
| 1358   | No file  | `1501615fa31c`  |
| 1355   | No file  | `1501615fa31c`  |
| 1351   | No file  | `1501615fa31c`  |
| 1348   | No file  | `1501615fa31c`  |
| 1346   | No file  | `1501615fa31c`  |
| 1341   | No file  | `1501615fa31c`  |
| 1340   | No file  | `1501615fa31c`  |
| 1338   | No file  | `1501615fa31c`  |
| 1335   | No file  | `1501615fa31c`  |
| 1333   | No file  | `1501615fa31c`  |
| 1329   | No file  | `1501615fa31c`  |
| 1327   | No file  | `1501615fa31c`  |
| 1324   | No file  | `1501615fa31c`  |
| 1321   | No file  | `1501615fa31c`  |
| 1319   | No file  | `1501615fa31c`  |
| 1318   | No file  | `1501615fa31c`  |
| 1316   | No file  | `1501615fa31c`  |
| 1313   | No file  | `1501615fa31c`  |
| 1311   | No file  | `1501615fa31c`  |
| 1309   | No file  | `1501615fa31c`  |
| 1304   | No file  | `1501615fa31c`  |
| 1292   | No file  | `1501615fa31c`  |
| 1286   | No file  | `1501615fa31c`  |
| 1280   | No file  | `1501615fa31c`  |
| 1276   | No file  | `1501615fa31c`  |
| 1267   | No file  | `1501615fa31c`  |
| 1261   | No file  | `1501615fa31c`  |
| 1256   | No file  | `1501615fa31c`  |
| 1250   | No file  | `1501615fa31c`  |
| 1246   | No file  | `1501615fa31c`  |
| 1239   | No file  | `1501615fa31c`  |
| 1230   | No file  | `1501615fa31c`  |
| 1226   | No file  | `1501615fa31c`  |
| 1220   | No file  | `1501615fa31c`  |
| 1217   | No file  | `1501615fa31c`  |
| 1211   | No file  | `1501615fa31c`  |
| 1210   | No file  | `1501615fa31c`  |
| 1208   | No file  | `1501615fa31c`  |
| 1203   | No file  | `1501615fa31c`  |
| 1197   | No file  | `1501615fa31c`  |
| 1194   | No file  | `1501615fa31c`  |
| 1192   | No file  | `1501615fa31c`  |
| 1187   | No file  | `1501615fa31c`  |
| 1183   | No file  | `1501615fa31c`  |
| 1177   | No file  | `1501615fa31c`  |
| 1173   | No file  | `1501615fa31c`  |
| 1167   | No file  | `1501615fa31c`  |
| 1164   | No file  | `1501615fa31c`  |
| 1156   | No file  | `1501615fa31c`  |
| 1149   | No file  | `1501615fa31c`  |
| 1144   | No file  | `1501615fa31c`  |
| 1137   | No file  | `1501615fa31c`  |
| 1132   | No file  | `1501615fa31c`  |
| 1127   | No file  | `1501615fa31c`  |
| 1122   | No file  | `1501615fa31c`  |
| 1118   | No file  | `1501615fa31c`  |
| 1114   | No file  | `1501615fa31c`  |
| 1109   | No file  | `1501615fa31c`  |
| 1102   | No file  | `1501615fa31c`  |
| 1096   | No file  | `1501615fa31c`  |
| 1088   | No file  | `1501615fa31c`  |
| 1081   | No file  | `1501615fa31c`  |
| 1076   | No file  | `1501615fa31c`  |
| 1069   | No file  | `1501615fa31c`  |
| 1064   | No file  | `1501615fa31c`  |
| 1058   | No file  | `1501615fa31c`  |
| 1051   | No file  | `1501615fa31c`  |
| 1044   | No file  | `1501615fa31c`  |
| 1036   | No file  | `1501615fa31c`  |
| 1026   | No file  | `1501615fa31c`  |
| 1016   | No file  | `1501615fa31c`  |
| 1009   | No file  | `1501615fa31c`  |
| 1005   | No file  | `1501615fa31c`  |
| 1000   | No file  | `1501615fa31c`  |
| 998    | No file  | `1501615fa31c`  |
| 990    | No file  | `1501615fa31c`  |
| 979    | No file  | `1501615fa31c`  |
| 972    | No file  | `1501615fa31c`  |
| 963    | No file  | `1501615fa31c`  |
| 955    | No file  | `1501615fa31c`  |
| 946    | No file  | `1501615fa31c`  |
| 938    | No file  | `1501615fa31c`  |
| 927    | No file  | `1501615fa31c`  |
| 911    | No file  | `1501615fa31c`  |
| 904    | No file  | `1501615fa31c`  |
| 899    | No file  | `1501615fa31c`  |
| 894    | No file  | `1501615fa31c`  |
| 885    | No file  | `1501615fa31c`  |
| 879    | No file  | `1501615fa31c`  |
| 872    | No file  | `1501615fa31c`  |
| 864    | No file  | `1501615fa31c`  |
| 855    | No file  | `1501615fa31c`  |
| 853    | No file  | `1501615fa31c`  |
| 845    | No file  | `1501615fa31c`  |
| 837    | No file  | `1501615fa31c`  |
| 829    | No file  | `1501615fa31c`  |
| 822    | No file  | `1501615fa31c`  |
| 814    | No file  | `1501615fa31c`  |
| 805    | No file  | `1501615fa31c`  |
| 794    | No file  | `1501615fa31c`  |
| 787    | No file  | `1501615fa31c`  |
| 780    | No file  | `1501615fa31c`  |
| 771    | No file  | `1501615fa31c`  |
| 760    | No file  | `1501615fa31c`  |
| 748    | No file  | `1501615fa31c`  |
| 741    | No file  | `1501615fa31c`  |
| 736    | No file  | `1501615fa31c`  |
| 731    | No file  | `1501615fa31c`  |
| 723    | No file  | `1501615fa31c`  |
| 711    | No file  | `1501615fa31c`  |
| 707    | No file  | `1501615fa31c`  |
| 697    | No file  | `1501615fa31c`  |
| 689    | No file  | `1501615fa31c`  |
| 683    | No file  | `1501615fa31c`  |
| 678    | No file  | `1501615fa31c`  |
| 670    | No file  | `1501615fa31c`  |
| 661    | No file  | `1501615fa31c`  |
| 656    | No file  | `1501615fa31c`  |
| 652    | No file  | `1501615fa31c`  |
| 643    | No file  | `1501615fa31c`  |
| 637    | No file  | `1501615fa31c`  |
| 630    | No file  | `1501615fa31c`  |
| 627    | No file  | `1501615fa31c`  |
| 621    | No file  | `1501615fa31c`  |
| 617    | No file  | `1501615fa31c`  |
| 615    | No file  | `1501615fa31c`  |
| 606    | No file  | `1501615fa31c`  |
| 599    | No file  | `1501615fa31c`  |
| 592    | No file  | `1501615fa31c`  |
| 586    | No file  | `1501615fa31c`  |
| 577    | No file  | `1501615fa31c`  |
| 569    | No file  | `1501615fa31c`  |
| 561    | No file  | `1501615fa31c`  |
| 554    | No file  | `1501615fa31c`  |
| 542    | No file  | `1501615fa31c`  |
| 532    | No file  | `1501615fa31c`  |
| 531    | No file  | `1501615fa31c`  |
| 526    | No file  | `1501615fa31c`  |
| 521    | No file  | `1501615fa31c`  |
| 517    | No file  | `1501615fa31c`  |
| 510    | No file  | `1501615fa31c`  |
| 508    | No file  | `1501615fa31c`  |
| 504    | No file  | `1501615fa31c`  |
| 497    | No file  | `1501615fa31c`  |
| 491    | No file  | `1501615fa31c`  |
| 485    | No file  | `1501615fa31c`  |
| 478    | No file  | `1501615fa31c`  |
| 472    | No file  | `1501615fa31c`  |
| 466    | No file  | `1501615fa31c`  |
| 457    | No file  | `1501615fa31c`  |
| 452    | No file  | `1501615fa31c`  |
| 449    | No file  | `1501615fa31c`  |
| 435    | No file  | `1501615fa31c`  |

<!-- versions:end -->

## Companion Files

None. The handler names the region with its LOC type 17 name from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of events                              |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (variable: 18 bytes + points)

| Offset        | Type               | Field             | Notes                                                                                           |
| ------------- | ------------------ | ----------------- | ----------------------------------------------------------------------------------------------- |
| `+0x00`       | u32                | event_name_hash   | `key_hash()` (lookup3, seed `0xC5EDE`) of `event_name` over its UTF-16LE bytes; matches on every row |
| `+0x04`       | u32                | event_name        | Index into `strings`: the XML `EventName` (`tooltest`, `rebalenos_velia_001`)                   |
| `+0x08`       | u16                | region_key        | XML `RegionKey`: `regioninfo.bss` region of the event (`5` Velia, `77` Calpheon City), LOC type 17 |
| `+0x0A`       | u32                | point_count       | Number of camera points                                                                         |
| `+0x0E`       | Point[point_count] | points            | See Point                                                                                       |
| `points+0x00` | u32                | unknown_points_00 | `0` on every row; see Open Questions                                                            |

### Point (38 bytes)

| Offset  | Type   | Field         | Notes                                                                                      |
| ------- | ------ | ------------- | ------------------------------------------------------------------------------------------ |
| `+0x00` | f32[3] | position      | XML `Position`: world x, y, z of the camera                                                |
| `+0x0C` | f32[4] | rotation      | XML `Rotation`: the camera rotation as a unit quaternion, x, y, z, w                       |
| `+0x1C` | f32    | fov           | XML `Fov` in radians: the XML's `70` is `1.2217`, `45` is `0.7854`                         |
| `+0x20` | f32    | speed_or_time | XML `SpeedOrTime`: the time to the next point, or the speed when `is_speed_mode` is `1`; `0` on the last point |
| `+0x24` | u8     | is_speed_mode | XML `IsSpeedMode`: `1` reads `speed_or_time` as a speed; `0` on every point                |
| `+0x25` | u8     | is_spline     | XML `IsSpline`: `1` moves along a spline through the point                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                          |
| ------- | ------------------ | ------------ | ------------------------------ |
| `+0x00` | u32                | string_count | Number of strings              |
| `+0x04` | pstr[string_count] | strings      | UTF-8 event names, one per row |

## Events

On client 3482 the file has 4 events and 43 points.

| Event                  | Region             | Points |
| ---------------------- | ------------------ | ------ |
| `tooltest`             | `5` Velia          | 4      |
| `rebalenos_velia_001`  | `5` Velia          | 9      |
| `test`                 | `5` Velia          | 18     |
| `recalpheon_peace_001` | `77` Calpheon City | 12     |

`recalpheon_peace_001` holds each of its four camera positions three
times: the first with a time of `10` and `is_spline` `1`, the next two
with a time of `0` and `is_spline` `0`.

## Field Names

Every field but `unknown_points_00` is an element or attribute of
`fieldwalkingcamera/fieldwalkingcameradata.xml` in the same client:
`<FieldWalkingCameraEvent EventName>`, `<RegionKey Value>` and per
`<Point>` the `Position`, `Rotation`, `Fov`, `SpeedOrTime`, `IsSpeedMode`
and `IsSpline` attributes. All 4 events and all 43 points match the XML
value for value on client 3482, `Fov` after the conversion from degrees
to radians. The XML lists the events in another order (`tooltest`,
`recalpheon_peace_001`, `test`, `rebalenos_velia_001`). `event_name_hash`
is not in the XML.

## Notes

- `panel_fieldwalkingcamera.luac` answers `FromClient_PlayFieldWalkingCamera`
  by switching to `eRenderMode_FieldWalkingCamera` and
  `eUIMode_FieldWalkingCamera` with the crosshair hidden, and
  `FromClient_StopFieldWalkingCamera` switches back. No Lua names an event.
- The event name hash runs over UTF-16LE text (`key_hash()`), where the
  sequence and cutscene tables hash ASCII names (`ascii_key_hash()`).

## Open Questions

### What `unknown_points_00` Counts

The u32 after the points is `0` on all 4 rows of client 3482, and the XML
has no element for it. It sits where a second list's count would go, but
no row fills one, so its type and meaning cannot be read from the data.
