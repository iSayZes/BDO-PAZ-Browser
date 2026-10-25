# `autoseasonclosechangeitemstaticstatus.bss` Format

## Purpose

The Season server gear conversions: per row a conversion item ([Season]
Tuvala Helmet Conversion Stone), the Season item it applies to and the
normal item it turns into. After the rows come four lists of the season's
graduation settings: the season challenges with their reward items, the
character types, the graduation quest and the graduation items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                        | Bytes | Records                                      | Row bytes |
| ------ | -------------- | ------------------------------------------- | ----- | -------------------------------------------- | --------- |
| 1      | 1590 and later | `autoseasonclosechangeitemstaticstatus.bss` | 1,496 | 89 Row, 2 Season Challenge, 2 Character Type | 16        |

| Layout | File                                        | Known           | Unknown     |
| ------ | ------------------------------------------- | --------------- | ----------- |
| 1      | `autoseasonclosechangeitemstaticstatus.bss` | 1,484 B (99.2%) | 12 B (0.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `25878210e894`  |
| 3482   | Layout 1 | `25878210e894`  |
| 3474   | Layout 1 | `25878210e894`  |
| 3473   | Layout 1 | `25878210e894`  |
| 3464   | Layout 1 | `25878210e894`  |
| 3458   | Layout 1 | `25878210e894`  |
| 3454   | Layout 1 | `25878210e894`  |
| 3444   | Layout 1 | `25878210e894`  |
| 3435   | Layout 1 | `25878210e894`  |
| 3426   | Layout 1 | `25878210e894`  |
| 3418   | Layout 1 | `25878210e894`  |
| 3412   | Layout 1 | `25878210e894`  |
| 3402   | Layout 1 | `25878210e894`  |
| 3396   | Layout 1 | `25878210e894`  |
| 3387   | Layout 1 | `25878210e894`  |
| 3381   | Layout 1 | `25878210e894`  |
| 3373   | Layout 1 | `25878210e894`  |
| 3364   | Layout 1 | `25878210e894`  |
| 3356   | Layout 1 | `25878210e894`  |
| 3349   | Layout 1 | `25878210e894`  |
| 3342   | Layout 1 | `25878210e894`  |
| 3335   | Layout 1 | `25878210e894`  |
| 3326   | Layout 1 | `25878210e894`  |
| 3321   | Layout 1 | `25878210e894`  |
| 3314   | Layout 1 | `25878210e894`  |
| 3303   | Layout 1 | `25878210e894`  |
| 3302   | Layout 1 | `25878210e894`  |
| 3293   | Layout 1 | `25878210e894`  |
| 3283   | Layout 1 | `25878210e894`  |
| 3275   | Layout 1 | `25878210e894`  |
| 3267   | Layout 1 | `25878210e894`  |
| 3258   | Layout 1 | `25878210e894`  |
| 3251   | Layout 1 | `25878210e894`  |
| 3242   | Layout 1 | `25878210e894`  |
| 3235   | Layout 1 | `25878210e894`  |
| 3229   | Layout 1 | `25878210e894`  |
| 3212   | Layout 1 | `25878210e894`  |
| 3203   | Layout 1 | `25878210e894`  |
| 3193   | Layout 1 | `25878210e894`  |
| 3186   | Layout 1 | `25878210e894`  |
| 3177   | Layout 1 | `25878210e894`  |
| 3169   | Layout 1 | `25878210e894`  |
| 3158   | Layout 1 | `25878210e894`  |
| 3151   | Layout 1 | `25878210e894`  |
| 3144   | Layout 1 | `25878210e894`  |
| 3133   | Layout 1 | `25878210e894`  |
| 3125   | Layout 1 | `25878210e894`  |
| 3118   | Layout 1 | `25878210e894`  |
| 3111   | Layout 1 | `25878210e894`  |
| 3103   | Layout 1 | `25878210e894`  |
| 3095   | Layout 1 | `25878210e894`  |
| 3086   | Layout 1 | `25878210e894`  |
| 3072   | Layout 1 | `25878210e894`  |
| 3062   | Layout 1 | `25878210e894`  |
| 3052   | Layout 1 | `25878210e894`  |
| 3045   | Layout 1 | `25878210e894`  |
| 3037   | Layout 1 | `25878210e894`  |
| 3030   | Layout 1 | `25878210e894`  |
| 3021   | Layout 1 | `25878210e894`  |
| 3012   | Layout 1 | `25878210e894`  |
| 3002   | Layout 1 | `25878210e894`  |
| 2995   | Layout 1 | `25878210e894`  |
| 2987   | Layout 1 | `25878210e894`  |
| 2978   | Layout 1 | `25878210e894`  |
| 2970   | Layout 1 | `25878210e894`  |
| 2959   | Layout 1 | `25878210e894`  |
| 2951   | Layout 1 | `25878210e894`  |
| 2942   | Layout 1 | `25878210e894`  |
| 2935   | Layout 1 | `25878210e894`  |
| 2932   | Layout 1 | `25878210e894`  |
| 2923   | Layout 1 | `25878210e894`  |
| 2919   | Layout 1 | `25878210e894`  |
| 2907   | Layout 1 | `25878210e894`  |
| 2900   | Layout 1 | `25878210e894`  |
| 2891   | Layout 1 | `25878210e894`  |
| 2882   | Layout 1 | `25878210e894`  |
| 2872   | Layout 1 | `25878210e894`  |
| 2863   | Layout 1 | `25878210e894`  |
| 2855   | Layout 1 | `25878210e894`  |
| 2849   | Layout 1 | `25878210e894`  |
| 2844   | Layout 1 | `25878210e894`  |
| 2834   | Layout 1 | `25878210e894`  |
| 2825   | Layout 1 | `25878210e894`  |
| 2819   | Layout 1 | `25878210e894`  |
| 2811   | Layout 1 | `25878210e894`  |
| 2803   | Layout 1 | `25878210e894`  |
| 2794   | Layout 1 | `25878210e894`  |
| 2783   | Layout 1 | `25878210e894`  |
| 2774   | Layout 1 | `25878210e894`  |
| 2765   | Layout 1 | `25878210e894`  |
| 2756   | Layout 1 | `25878210e894`  |
| 2750   | Layout 1 | `25878210e894`  |
| 2743   | Layout 1 | `25878210e894`  |
| 2736   | Layout 1 | `25878210e894`  |
| 2726   | Layout 1 | `25878210e894`  |
| 2717   | Layout 1 | `25878210e894`  |
| 2709   | Layout 1 | `25878210e894`  |
| 2703   | Layout 1 | `25878210e894`  |
| 2695   | Layout 1 | `25878210e894`  |
| 2684   | Layout 1 | `25878210e894`  |
| 2672   | Layout 1 | `25878210e894`  |
| 2665   | Layout 1 | `25878210e894`  |
| 2657   | Layout 1 | `25878210e894`  |
| 2649   | Layout 1 | `25878210e894`  |
| 2644   | Layout 1 | `25878210e894`  |
| 2637   | Layout 1 | `25878210e894`  |
| 2629   | Layout 1 | `25878210e894`  |
| 2619   | Layout 1 | `25878210e894`  |
| 2612   | Layout 1 | `25878210e894`  |
| 2606   | Layout 1 | `25878210e894`  |
| 2602   | Layout 1 | `25878210e894`  |
| 2601   | Layout 1 | `25878210e894`  |
| 2592   | Layout 1 | `25878210e894`  |
| 2583   | Layout 1 | `25878210e894`  |
| 2575   | Layout 1 | `25878210e894`  |
| 2567   | Layout 1 | `25878210e894`  |
| 2560   | Layout 1 | `25878210e894`  |
| 2553   | Layout 1 | `25878210e894`  |
| 2545   | Layout 1 | `25878210e894`  |
| 2538   | Layout 1 | `25878210e894`  |
| 2529   | Layout 1 | `25878210e894`  |
| 2519   | Layout 1 | `25878210e894`  |
| 2513   | Layout 1 | `25878210e894`  |
| 2510   | Layout 1 | `25878210e894`  |
| 2507   | Layout 1 | `25878210e894`  |
| 2503   | Layout 1 | `25878210e894`  |
| 2498   | Layout 1 | `25878210e894`  |
| 2492   | Layout 1 | `25878210e894`  |
| 2487   | Layout 1 | `25878210e894`  |
| 2480   | Layout 1 | `25878210e894`  |
| 2474   | Layout 1 | `25878210e894`  |
| 2468   | Layout 1 | `25878210e894`  |
| 2460   | Layout 1 | `25878210e894`  |
| 2453   | Layout 1 | `25878210e894`  |
| 2444   | Layout 1 | `25878210e894`  |
| 2438   | Layout 1 | `25878210e894`  |
| 2434   | Layout 1 | `25878210e894`  |
| 2429   | Layout 1 | `25878210e894`  |
| 2421   | Layout 1 | `25878210e894`  |
| 2414   | Layout 1 | `25878210e894`  |
| 2407   | Layout 1 | `25878210e894`  |
| 2401   | Layout 1 | `25878210e894`  |
| 2397   | Layout 1 | `25878210e894`  |
| 2393   | Layout 1 | `25878210e894`  |
| 2384   | Layout 1 | `25878210e894`  |
| 2378   | Layout 1 | `25878210e894`  |
| 2372   | Layout 1 | `25878210e894`  |
| 2358   | Layout 1 | `25878210e894`  |
| 2352   | Layout 1 | `25878210e894`  |
| 2347   | Layout 1 | `25878210e894`  |
| 2343   | Layout 1 | `25878210e894`  |
| 2335   | Layout 1 | `25878210e894`  |
| 2327   | Layout 1 | `25878210e894`  |
| 2324   | Layout 1 | `25878210e894`  |
| 2319   | Layout 1 | `25878210e894`  |
| 2313   | Layout 1 | `25878210e894`  |
| 2308   | Layout 1 | `25878210e894`  |
| 2302   | Layout 1 | `25878210e894`  |
| 2295   | Layout 1 | `25878210e894`  |
| 2290   | Layout 1 | `25878210e894`  |
| 2284   | Layout 1 | `25878210e894`  |
| 2276   | Layout 1 | `25878210e894`  |
| 2269   | Layout 1 | `25878210e894`  |
| 2259   | Layout 1 | `25878210e894`  |
| 2250   | Layout 1 | `25878210e894`  |
| 2243   | Layout 1 | `25878210e894`  |
| 2235   | Layout 1 | `25878210e894`  |
| 2229   | Layout 1 | `25878210e894`  |
| 2224   | Layout 1 | `25878210e894`  |
| 2218   | Layout 1 | `25878210e894`  |
| 2215   | Layout 1 | `25878210e894`  |
| 2207   | Layout 1 | `25878210e894`  |
| 2203   | Layout 1 | `25878210e894`  |
| 2196   | Layout 1 | `25878210e894`  |
| 2192   | Layout 1 | `25878210e894`  |
| 2189   | Layout 1 | `25878210e894`  |
| 2183   | Layout 1 | `25878210e894`  |
| 2179   | Layout 1 | `25878210e894`  |
| 2171   | Layout 1 | `25878210e894`  |
| 2163   | Layout 1 | `25878210e894`  |
| 2156   | Layout 1 | `25878210e894`  |
| 2151   | Layout 1 | `25878210e894`  |
| 2147   | Layout 1 | `25878210e894`  |
| 2142   | Layout 1 | `25878210e894`  |
| 2138   | Layout 1 | `25878210e894`  |
| 2134   | Layout 1 | `25878210e894`  |
| 2130   | Layout 1 | `25878210e894`  |
| 2122   | Layout 1 | `25878210e894`  |
| 2107   | Layout 1 | `25878210e894`  |
| 2098   | Layout 1 | `25878210e894`  |
| 2089   | Layout 1 | `25878210e894`  |
| 2081   | Layout 1 | `25878210e894`  |
| 2073   | Layout 1 | `25878210e894`  |
| 2067   | Layout 1 | `25878210e894`  |
| 2063   | Layout 1 | `25878210e894`  |
| 2059   | Layout 1 | `25878210e894`  |
| 2052   | Layout 1 | `25878210e894`  |
| 2044   | Layout 1 | `25878210e894`  |
| 2039   | Layout 1 | `25878210e894`  |
| 2032   | Layout 1 | `25878210e894`  |
| 2025   | Layout 1 | `25878210e894`  |
| 2011   | Layout 1 | `25878210e894`  |
| 2005   | Layout 1 | `25878210e894`  |
| 2000   | Layout 1 | `25878210e894`  |
| 1996   | Layout 1 | `25878210e894`  |
| 1991   | Layout 1 | `25878210e894`  |
| 1985   | Layout 1 | `25878210e894`  |
| 1980   | Layout 1 | `25878210e894`  |
| 1969   | Layout 1 | `25878210e894`  |
| 1964   | Layout 1 | `25878210e894`  |
| 1958   | Layout 1 | `25878210e894`  |
| 1950   | Layout 1 | `25878210e894`  |
| 1945   | Layout 1 | `25878210e894`  |
| 1937   | Layout 1 | `25878210e894`  |
| 1933   | Layout 1 | `25878210e894`  |
| 1927   | Layout 1 | `25878210e894`  |
| 1921   | Layout 1 | `25878210e894`  |
| 1914   | Layout 1 | `25878210e894`  |
| 1908   | Layout 1 | `25878210e894`  |
| 1897   | Layout 1 | `25878210e894`  |
| 1892   | Layout 1 | `25878210e894`  |
| 1886   | Layout 1 | `25878210e894`  |
| 1881   | Layout 1 | `25878210e894`  |
| 1871   | Layout 1 | `25878210e894`  |
| 1866   | Layout 1 | `25878210e894`  |
| 1862   | Layout 1 | `25878210e894`  |
| 1854   | Layout 1 | `25878210e894`  |
| 1846   | Layout 1 | `25878210e894`  |
| 1838   | Layout 1 | `25878210e894`  |
| 1832   | Layout 1 | `25878210e894`  |
| 1826   | Layout 1 | `25878210e894`  |
| 1822   | Layout 1 | `25878210e894`  |
| 1818   | Layout 1 | `25878210e894`  |
| 1804   | Layout 1 | `25878210e894`  |
| 1794   | Layout 1 | `25878210e894`  |
| 1790   | Layout 1 | `25878210e894`  |
| 1784   | Layout 1 | `25878210e894`  |
| 1774   | Layout 1 | `25878210e894`  |
| 1771   | Layout 1 | `25878210e894`  |
| 1762   | Layout 1 | `25878210e894`  |
| 1759   | Layout 1 | `25878210e894`  |
| 1754   | Layout 1 | `25878210e894`  |
| 1749   | Layout 1 | `25878210e894`  |
| 1743   | Layout 1 | `25878210e894`  |
| 1737   | Layout 1 | `25878210e894`  |
| 1731   | Layout 1 | `25878210e894`  |
| 1725   | Layout 1 | `25878210e894`  |
| 1717   | Layout 1 | `25878210e894`  |
| 1710   | Layout 1 | `25878210e894`  |
| 1704   | Layout 1 | `25878210e894`  |
| 1698   | Layout 1 | `25878210e894`  |
| 1690   | Layout 1 | `25878210e894`  |
| 1685   | Layout 1 | `25878210e894`  |
| 1680   | Layout 1 | `25878210e894`  |
| 1674   | Layout 1 | `25878210e894`  |
| 1668   | Layout 1 | `25878210e894`  |
| 1659   | Layout 1 | `25878210e894`  |
| 1649   | Layout 1 | `25878210e894`  |
| 1642   | Layout 1 | `25878210e894`  |
| 1636   | Layout 1 | `25878210e894`  |
| 1628   | Layout 1 | `25878210e894`  |
| 1622   | Layout 1 | `25878210e894`  |
| 1614   | Layout 1 | `25878210e894`  |
| 1608   | Layout 1 | `25878210e894`  |
| 1602   | Layout 1 | `25878210e894`  |
| 1598   | Layout 1 | `25878210e894`  |
| 1594   | Layout 1 | `25878210e894`  |
| 1590   | Layout 1 | `25878210e894`  |
| 1587   | No file  | `25878210e894`  |
| 1584   | No file  | `25878210e894`  |
| 1579   | No file  | `25878210e894`  |
| 1572   | No file  | `25878210e894`  |
| 1565   | No file  | `25878210e894`  |
| 1559   | No file  | `25878210e894`  |
| 1554   | No file  | `25878210e894`  |
| 1547   | No file  | `25878210e894`  |
| 1537   | No file  | `25878210e894`  |
| 1529   | No file  | `25878210e894`  |
| 1524   | No file  | `25878210e894`  |
| 1519   | No file  | `25878210e894`  |
| 1509   | No file  | `25878210e894`  |
| 1506   | No file  | `25878210e894`  |
| 1504   | No file  | `25878210e894`  |
| 1500   | No file  | `25878210e894`  |
| 1493   | No file  | `25878210e894`  |
| 1489   | No file  | `25878210e894`  |
| 1485   | No file  | `25878210e894`  |
| 1481   | No file  | `25878210e894`  |
| 1474   | No file  | `25878210e894`  |
| 1466   | No file  | `25878210e894`  |
| 1462   | No file  | `25878210e894`  |
| 1459   | No file  | `25878210e894`  |
| 1453   | No file  | `25878210e894`  |
| 1450   | No file  | `25878210e894`  |
| 1445   | No file  | `25878210e894`  |
| 1439   | No file  | `25878210e894`  |
| 1433   | No file  | `25878210e894`  |
| 1430   | No file  | `25878210e894`  |
| 1426   | No file  | `25878210e894`  |
| 1421   | No file  | `25878210e894`  |
| 1417   | No file  | `25878210e894`  |
| 1416   | No file  | `25878210e894`  |
| 1409   | No file  | `25878210e894`  |
| 1405   | No file  | `25878210e894`  |
| 1401   | No file  | `25878210e894`  |
| 1396   | No file  | `25878210e894`  |
| 1391   | No file  | `25878210e894`  |
| 1390   | No file  | `25878210e894`  |
| 1386   | No file  | `25878210e894`  |
| 1381   | No file  | `25878210e894`  |
| 1379   | No file  | `25878210e894`  |
| 1372   | No file  | `25878210e894`  |
| 1366   | No file  | `25878210e894`  |
| 1364   | No file  | `25878210e894`  |
| 1363   | No file  | `25878210e894`  |
| 1360   | No file  | `25878210e894`  |
| 1358   | No file  | `25878210e894`  |
| 1355   | No file  | `25878210e894`  |
| 1351   | No file  | `25878210e894`  |
| 1348   | No file  | `25878210e894`  |
| 1346   | No file  | `25878210e894`  |
| 1341   | No file  | `25878210e894`  |
| 1340   | No file  | `25878210e894`  |
| 1338   | No file  | `25878210e894`  |
| 1335   | No file  | `25878210e894`  |
| 1333   | No file  | `25878210e894`  |
| 1329   | No file  | `25878210e894`  |
| 1327   | No file  | `25878210e894`  |
| 1324   | No file  | `25878210e894`  |
| 1321   | No file  | `25878210e894`  |
| 1319   | No file  | `25878210e894`  |
| 1318   | No file  | `25878210e894`  |
| 1316   | No file  | `25878210e894`  |
| 1313   | No file  | `25878210e894`  |
| 1311   | No file  | `25878210e894`  |
| 1309   | No file  | `25878210e894`  |
| 1304   | No file  | `25878210e894`  |
| 1292   | No file  | `25878210e894`  |
| 1286   | No file  | `25878210e894`  |
| 1280   | No file  | `25878210e894`  |
| 1276   | No file  | `25878210e894`  |
| 1267   | No file  | `25878210e894`  |
| 1261   | No file  | `25878210e894`  |
| 1256   | No file  | `25878210e894`  |
| 1250   | No file  | `25878210e894`  |
| 1246   | No file  | `25878210e894`  |
| 1239   | No file  | `25878210e894`  |
| 1230   | No file  | `25878210e894`  |
| 1226   | No file  | `25878210e894`  |
| 1220   | No file  | `25878210e894`  |
| 1217   | No file  | `25878210e894`  |
| 1211   | No file  | `25878210e894`  |
| 1210   | No file  | `25878210e894`  |
| 1208   | No file  | `25878210e894`  |
| 1203   | No file  | `25878210e894`  |
| 1197   | No file  | `25878210e894`  |
| 1194   | No file  | `25878210e894`  |
| 1192   | No file  | `25878210e894`  |
| 1187   | No file  | `25878210e894`  |
| 1183   | No file  | `25878210e894`  |
| 1177   | No file  | `25878210e894`  |
| 1173   | No file  | `25878210e894`  |
| 1167   | No file  | `25878210e894`  |
| 1164   | No file  | `25878210e894`  |
| 1156   | No file  | `25878210e894`  |
| 1149   | No file  | `25878210e894`  |
| 1144   | No file  | `25878210e894`  |
| 1137   | No file  | `25878210e894`  |
| 1132   | No file  | `25878210e894`  |
| 1127   | No file  | `25878210e894`  |
| 1122   | No file  | `25878210e894`  |
| 1118   | No file  | `25878210e894`  |
| 1114   | No file  | `25878210e894`  |
| 1109   | No file  | `25878210e894`  |
| 1102   | No file  | `25878210e894`  |
| 1096   | No file  | `25878210e894`  |
| 1088   | No file  | `25878210e894`  |
| 1081   | No file  | `25878210e894`  |
| 1076   | No file  | `25878210e894`  |
| 1069   | No file  | `25878210e894`  |
| 1064   | No file  | `25878210e894`  |
| 1058   | No file  | `25878210e894`  |
| 1051   | No file  | `25878210e894`  |
| 1044   | No file  | `25878210e894`  |
| 1036   | No file  | `25878210e894`  |
| 1026   | No file  | `25878210e894`  |
| 1016   | No file  | `25878210e894`  |
| 1009   | No file  | `25878210e894`  |
| 1005   | No file  | `25878210e894`  |
| 1000   | No file  | `25878210e894`  |
| 998    | No file  | `25878210e894`  |
| 990    | No file  | `25878210e894`  |
| 979    | No file  | `25878210e894`  |
| 972    | No file  | `25878210e894`  |
| 963    | No file  | `25878210e894`  |
| 955    | No file  | `25878210e894`  |
| 946    | No file  | `25878210e894`  |
| 938    | No file  | `25878210e894`  |
| 927    | No file  | `25878210e894`  |
| 911    | No file  | `25878210e894`  |
| 904    | No file  | `25878210e894`  |
| 899    | No file  | `25878210e894`  |
| 894    | No file  | `25878210e894`  |
| 885    | No file  | `25878210e894`  |
| 879    | No file  | `25878210e894`  |
| 872    | No file  | `25878210e894`  |
| 864    | No file  | `25878210e894`  |
| 855    | No file  | `25878210e894`  |
| 853    | No file  | `25878210e894`  |
| 845    | No file  | `25878210e894`  |
| 837    | No file  | `25878210e894`  |
| 829    | No file  | `25878210e894`  |
| 822    | No file  | `25878210e894`  |
| 814    | No file  | `25878210e894`  |
| 805    | No file  | `25878210e894`  |
| 794    | No file  | `25878210e894`  |
| 787    | No file  | `25878210e894`  |
| 780    | No file  | `25878210e894`  |
| 771    | No file  | `25878210e894`  |
| 760    | No file  | `25878210e894`  |
| 748    | No file  | `25878210e894`  |
| 741    | No file  | `25878210e894`  |
| 736    | No file  | `25878210e894`  |
| 731    | No file  | `25878210e894`  |
| 723    | No file  | `25878210e894`  |
| 711    | No file  | `25878210e894`  |
| 707    | No file  | `25878210e894`  |
| 697    | No file  | `25878210e894`  |
| 689    | No file  | `25878210e894`  |
| 683    | No file  | `25878210e894`  |
| 678    | No file  | `25878210e894`  |
| 670    | No file  | `25878210e894`  |
| 661    | No file  | `25878210e894`  |
| 656    | No file  | `25878210e894`  |
| 652    | No file  | `25878210e894`  |
| 643    | No file  | `25878210e894`  |
| 637    | No file  | `25878210e894`  |
| 630    | No file  | `25878210e894`  |
| 627    | No file  | `25878210e894`  |
| 621    | No file  | `25878210e894`  |
| 617    | No file  | `25878210e894`  |
| 615    | No file  | `25878210e894`  |
| 606    | No file  | `25878210e894`  |
| 599    | No file  | `25878210e894`  |
| 592    | No file  | `25878210e894`  |
| 586    | No file  | `25878210e894`  |
| 577    | No file  | `25878210e894`  |
| 569    | No file  | `25878210e894`  |
| 561    | No file  | `25878210e894`  |
| 554    | No file  | `25878210e894`  |
| 542    | No file  | `25878210e894`  |
| 532    | No file  | `25878210e894`  |
| 531    | No file  | `25878210e894`  |
| 526    | No file  | `25878210e894`  |
| 521    | No file  | `25878210e894`  |
| 517    | No file  | `25878210e894`  |
| 510    | No file  | `25878210e894`  |
| 508    | No file  | `25878210e894`  |
| 504    | No file  | `25878210e894`  |
| 497    | No file  | `25878210e894`  |
| 491    | No file  | `25878210e894`  |
| 485    | No file  | `25878210e894`  |
| 478    | No file  | `25878210e894`  |
| 472    | No file  | `25878210e894`  |
| 466    | No file  | `25878210e894`  |
| 457    | No file  | `25878210e894`  |
| 452    | No file  | `25878210e894`  |
| 449    | No file  | `25878210e894`  |
| 435    | No file  | `25878210e894`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                                   | Type                                            | Field                                | Notes                                                    |
| ---------------------------------------- | ----------------------------------------------- | ------------------------------------ | -------------------------------------------------------- |
| `+0x00`                                  | char[4]                                         | magic                                | ASCII `PABR`                                             |
| `+0x04`                                  | u32                                             | row_count                            | Number of rows                                           |
| `+0x08`                                  | Row[row_count]                                  | rows                                 | See Row                                                  |
| `rows+0x00`                              | u32                                             | season_challenge_count               | Number of `season_challenges`; `2` on every client checked |
| `rows+0x04`                              | Season Challenge[season_challenge_count]        | season_challenges                    | See Season Challenge                                     |
| `season_challenges+0x00`                 | u32                                             | character_type_count                 | Number of `auto_graduation_character_types`              |
| `season_challenges+0x04`                 | Character Type[character_type_count]            | auto_graduation_character_types      | See Character Type                                       |
| `auto_graduation_character_types+0x00`   | u32                                             | graduation_quest_count               | Number of `auto_graduation_quests`; `1`                  |
| `auto_graduation_character_types+0x04`   | u32[graduation_quest_count]                     | auto_graduation_quests               | Packed quest IDs (low u16 chain, high u16 quest); `40071/2` on client 3482 |
| `auto_graduation_quests+0x00`            | u32                                             | graduation_item_count                | Number of `auto_graduation_items`; `2`                   |
| `auto_graduation_quests+0x04`            | u32[graduation_item_count]                      | auto_graduation_items                | Item IDs; Season Graduation Gift Box and Fughar's Letter of Encouragement on client 3482 |
| `auto_graduation_items+0x00`             | bytes[4]                                        | unknown_auto_graduation_items_00     | Differs between clients; see Open Questions              |
| `auto_graduation_items+0x04`             | String Table                                    | string_table                         | See String Table                                         |
| `EOF-0x08`                               | u32                                             | table_start                          | Offset of the string table                               |
| `EOF-0x04`                               | u32                                             | zero                                 | Always `0`                                               |

### Row (16 bytes)

| Offset  | Type | Field           | Notes                                                                                  |
| ------- | ---- | --------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u32  | index           | Row number; `54` and `85` appear twice on client 3482                                   |
| `+0x04` | u32  | change_item_key | Conversion item, a packed item key (`8046` [Season] Tuvala Helmet Conversion Stone)     |
| `+0x08` | u32  | before_item_key | Season item the conversion applies to (`694105` Tuvala Helmet); unique per row          |
| `+0x0C` | u32  | after_item_key  | Normal item it turns into (`695105` Tuvala Helmet)                                      |

### Season Challenge (8 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | challenge_key | Challenge key; `2964` and `2965` on clients 1784 to 3482     |
| `+0x02` | u32  | item_id       | Item; `694111` Tuvala Ring and `694110` Tuvala Earring       |
| `+0x06` | u8   | unknown_06    | `5` on both entries; see Open Questions                      |
| `+0x07` | u8   | unknown_07    | `1` on both entries                                          |

### Character Type (2 bytes)

| Offset  | Type | Field      | Notes                         |
| ------- | ---- | ---------- | ----------------------------- |
| `+0x00` | u8   | unknown_00 | `1` and `2`                    |
| `+0x01` | u8   | unknown_01 | `0` on both entries            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

A private server's `DataSheets.bexcel` on client 1784 has the rows in the
`SeasonAutoChangeItem` sheet (`Index`, `ChangeItemKey`, `BeforeItemKey`,
`AfterItemKey`), 63 of 63 rows equal to the file of that client. The
lists come from two sheets of the same workbook:

| Field                           | Sheet and column                                   | Client 1784                                    |
| ------------------------------- | -------------------------------------------------- | ---------------------------------------------- |
| season_challenges               | `SeasonChallenges` `ChallengesKey`                 | `2964, 694111, 5, 1; 2965, 694110, 5, 1;` (the row for service type 12, nations 0 and 1), equal |
| auto_graduation_character_types | `SeasonEtc` `SeasonAutoGraduationCharacterType`    | `1, 0; 2, 0;`, equal                            |
| auto_graduation_quests          | `SeasonEtc` `SeasonAutoGraduationQuest`            | `40041, 2` against `40036/2` in the file        |
| auto_graduation_items           | `SeasonEtc` `SeasonAutoGraduationItem`             | `8089, 8200`, equal                             |

The quest differs (private server values are edited); the column order
places it. `SeasonEtc` also has the graduation mail title, sender and text
(`{TextBind:SEASON_TITLE5}`) and `RunSeasonAutoGraduation`, which the
file does not hold. The sheet names each challenge entry's four numbers as
one `ChallengesKey` cell, so the two u8 stay unnamed.

## Notes

- The 89 rows of client 3482 convert Tuvala gear and accessories to the
  normal Tuvala items, several Season items through one conversion item
  (`8044`, `8045` Tuvala Awakening Weapon Conversion Stone).
- The four lists hold the same values on clients 1784 to 3482, apart
  from the quest (`40036/2` on 1784, `40056/2` on 2107, `40071/2` from
  2519) and the first item (`8089` up to 3251, `890081` Season Graduation
  Gift Box from 3474); the second item is `8200`, `5919` and from 2519
  `8445`.
- Client 1784 has 63 rows in index order; client 3482 adds rows out of
  order (`86, 85, 87` at the end) and repeats indices 54 and 85.
- The handler (`_bss/autoseasonclosechangeitemstaticstatus/`) shows one
  row per conversion with the three items; the lists after the rows are
  read and checked but not shown.

## Open Questions

### What the Season Challenge Bytes and Character Types Are

Each season challenge entry ends with `5` and `1`, which fit an
enhancement level (PEN) and a count of its Tuvala ring or earring; the
character types `1, 0` and `2, 0` may name the Season character kinds
that graduate. Neither is read by a Lua getter of client 3482.

### What the Four Bytes After the Lists Hold

`unknown_auto_graduation_items_00` is `00 00 00 00` on clients 1784, 3002,
3474 and 3482, `01 00 01 00` on 2765 and 3251, `00 00 e5 44` on 2107 and
`00 00 a9 69` on 2519. It matches no `SeasonEtc` column, and as u16 pairs,
a u32 or an f32 none of the values names anything in the other lists.
