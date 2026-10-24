# `hardcorechanneltotalrankgradestaticstatusmanager.bss` Format

## Purpose

The grades of the Hardcore channel's total ranking: how many players the
ranking lists, then one row per grade. Grades 1 to 3 (Transcendent,
Conqueror, Reaper) go to ranks 1 to 3, grades 4 to 9 (Honorblade to Adept)
to the top 1, 5, 10, 30, 50 and 100 percent, and grade 0 is Novice, the
unranked grade (client 3474). The Hardcore Box items of LOC type 0 carry the
same tier names ("Transcendent's Hardcore Box" ... "Adept's Hardcore Box",
items 965002 to 965010), but no field of this file points at them.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                                   | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------------------------------ | ----- | ------- | --------- |
| 1      | 2834 and later | 3483    | `hardcorechanneltotalrankgradestaticstatusmanager.bss` | 128   | 10 Row  | 10        |

| Layout | File                                                   | Known         | Unknown    |
| ------ | ------------------------------------------------------ | ------------- | ---------- |
| 1      | `hardcorechanneltotalrankgradestaticstatusmanager.bss` | 124 B (96.9%) | 4 B (3.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `110614387bf4`  |
| 3482   | Layout 1 | `110614387bf4`  |
| 3474   | Layout 1 | `110614387bf4`  |
| 3473   | Layout 1 | `110614387bf4`  |
| 3464   | Layout 1 | `110614387bf4`  |
| 3458   | Layout 1 | `110614387bf4`  |
| 3454   | Layout 1 | `110614387bf4`  |
| 3444   | Layout 1 | `110614387bf4`  |
| 3435   | Layout 1 | `110614387bf4`  |
| 3426   | Layout 1 | `110614387bf4`  |
| 3418   | Layout 1 | `110614387bf4`  |
| 3412   | Layout 1 | `110614387bf4`  |
| 3402   | Layout 1 | `110614387bf4`  |
| 3396   | Layout 1 | `110614387bf4`  |
| 3387   | Layout 1 | `110614387bf4`  |
| 3381   | Layout 1 | `110614387bf4`  |
| 3373   | Layout 1 | `110614387bf4`  |
| 3364   | Layout 1 | `110614387bf4`  |
| 3356   | Layout 1 | `110614387bf4`  |
| 3349   | Layout 1 | `110614387bf4`  |
| 3342   | Layout 1 | `110614387bf4`  |
| 3335   | Layout 1 | `110614387bf4`  |
| 3326   | Layout 1 | `110614387bf4`  |
| 3321   | Layout 1 | `110614387bf4`  |
| 3314   | Layout 1 | `110614387bf4`  |
| 3303   | Layout 1 | `110614387bf4`  |
| 3302   | Layout 1 | `110614387bf4`  |
| 3293   | Layout 1 | `110614387bf4`  |
| 3283   | Layout 1 | `110614387bf4`  |
| 3275   | Layout 1 | `110614387bf4`  |
| 3267   | Layout 1 | `110614387bf4`  |
| 3258   | Layout 1 | `110614387bf4`  |
| 3251   | Layout 1 | `110614387bf4`  |
| 3242   | Layout 1 | `110614387bf4`  |
| 3235   | Layout 1 | `110614387bf4`  |
| 3229   | Layout 1 | `110614387bf4`  |
| 3212   | Layout 1 | `110614387bf4`  |
| 3203   | Layout 1 | `110614387bf4`  |
| 3193   | Layout 1 | `110614387bf4`  |
| 3186   | Layout 1 | `110614387bf4`  |
| 3177   | Layout 1 | `110614387bf4`  |
| 3169   | Layout 1 | `110614387bf4`  |
| 3158   | Layout 1 | `110614387bf4`  |
| 3151   | Layout 1 | `110614387bf4`  |
| 3144   | Layout 1 | `110614387bf4`  |
| 3133   | Layout 1 | `110614387bf4`  |
| 3125   | Layout 1 | `110614387bf4`  |
| 3118   | Layout 1 | `110614387bf4`  |
| 3111   | Layout 1 | `110614387bf4`  |
| 3103   | Layout 1 | `110614387bf4`  |
| 3095   | Layout 1 | `110614387bf4`  |
| 3086   | Layout 1 | `110614387bf4`  |
| 3072   | Layout 1 | `110614387bf4`  |
| 3062   | Layout 1 | `110614387bf4`  |
| 3052   | Layout 1 | `110614387bf4`  |
| 3045   | Layout 1 | `110614387bf4`  |
| 3037   | Layout 1 | `110614387bf4`  |
| 3030   | Layout 1 | `110614387bf4`  |
| 3021   | Layout 1 | `110614387bf4`  |
| 3012   | Layout 1 | `110614387bf4`  |
| 3002   | Layout 1 | `110614387bf4`  |
| 2995   | Layout 1 | `110614387bf4`  |
| 2987   | Layout 1 | `110614387bf4`  |
| 2978   | Layout 1 | `110614387bf4`  |
| 2970   | Layout 1 | `110614387bf4`  |
| 2959   | Layout 1 | `110614387bf4`  |
| 2951   | Layout 1 | `110614387bf4`  |
| 2942   | Layout 1 | `110614387bf4`  |
| 2935   | Layout 1 | `110614387bf4`  |
| 2932   | Layout 1 | `110614387bf4`  |
| 2923   | Layout 1 | `110614387bf4`  |
| 2919   | Layout 1 | `110614387bf4`  |
| 2907   | Layout 1 | `110614387bf4`  |
| 2900   | Layout 1 | `110614387bf4`  |
| 2891   | Layout 1 | `110614387bf4`  |
| 2882   | Layout 1 | `110614387bf4`  |
| 2872   | Layout 1 | `110614387bf4`  |
| 2863   | Layout 1 | `110614387bf4`  |
| 2855   | Layout 1 | `110614387bf4`  |
| 2849   | Layout 1 | `110614387bf4`  |
| 2844   | Layout 1 | `110614387bf4`  |
| 2834   | Layout 1 | `110614387bf4`  |
| 2825   | No file  | `110614387bf4`  |
| 2819   | No file  | `110614387bf4`  |
| 2811   | No file  | `110614387bf4`  |
| 2803   | No file  | `110614387bf4`  |
| 2794   | No file  | `110614387bf4`  |
| 2783   | No file  | `110614387bf4`  |
| 2774   | No file  | `110614387bf4`  |
| 2765   | No file  | `110614387bf4`  |
| 2756   | No file  | `110614387bf4`  |
| 2750   | No file  | `110614387bf4`  |
| 2743   | No file  | `110614387bf4`  |
| 2736   | No file  | `110614387bf4`  |
| 2726   | No file  | `110614387bf4`  |
| 2717   | No file  | `110614387bf4`  |
| 2709   | No file  | `110614387bf4`  |
| 2703   | No file  | `110614387bf4`  |
| 2695   | No file  | `110614387bf4`  |
| 2684   | No file  | `110614387bf4`  |
| 2672   | No file  | `110614387bf4`  |
| 2665   | No file  | `110614387bf4`  |
| 2657   | No file  | `110614387bf4`  |
| 2649   | No file  | `110614387bf4`  |
| 2644   | No file  | `110614387bf4`  |
| 2637   | No file  | `110614387bf4`  |
| 2629   | No file  | `110614387bf4`  |
| 2619   | No file  | `110614387bf4`  |
| 2612   | No file  | `110614387bf4`  |
| 2606   | No file  | `110614387bf4`  |
| 2602   | No file  | `110614387bf4`  |
| 2601   | No file  | `110614387bf4`  |
| 2592   | No file  | `110614387bf4`  |
| 2583   | No file  | `110614387bf4`  |
| 2575   | No file  | `110614387bf4`  |
| 2567   | No file  | `110614387bf4`  |
| 2560   | No file  | `110614387bf4`  |
| 2553   | No file  | `110614387bf4`  |
| 2545   | No file  | `110614387bf4`  |
| 2538   | No file  | `110614387bf4`  |
| 2529   | No file  | `110614387bf4`  |
| 2519   | No file  | `110614387bf4`  |
| 2513   | No file  | `110614387bf4`  |
| 2510   | No file  | `110614387bf4`  |
| 2507   | No file  | `110614387bf4`  |
| 2503   | No file  | `110614387bf4`  |
| 2498   | No file  | `110614387bf4`  |
| 2492   | No file  | `110614387bf4`  |
| 2487   | No file  | `110614387bf4`  |
| 2480   | No file  | `110614387bf4`  |
| 2474   | No file  | `110614387bf4`  |
| 2468   | No file  | `110614387bf4`  |
| 2460   | No file  | `110614387bf4`  |
| 2453   | No file  | `110614387bf4`  |
| 2444   | No file  | `110614387bf4`  |
| 2438   | No file  | `110614387bf4`  |
| 2434   | No file  | `110614387bf4`  |
| 2429   | No file  | `110614387bf4`  |
| 2421   | No file  | `110614387bf4`  |
| 2414   | No file  | `110614387bf4`  |
| 2407   | No file  | `110614387bf4`  |
| 2401   | No file  | `110614387bf4`  |
| 2397   | No file  | `110614387bf4`  |
| 2393   | No file  | `110614387bf4`  |
| 2384   | No file  | `110614387bf4`  |
| 2378   | No file  | `110614387bf4`  |
| 2372   | No file  | `110614387bf4`  |
| 2358   | No file  | `110614387bf4`  |
| 2352   | No file  | `110614387bf4`  |
| 2347   | No file  | `110614387bf4`  |
| 2343   | No file  | `110614387bf4`  |
| 2335   | No file  | `110614387bf4`  |
| 2327   | No file  | `110614387bf4`  |
| 2324   | No file  | `110614387bf4`  |
| 2319   | No file  | `110614387bf4`  |
| 2313   | No file  | `110614387bf4`  |
| 2308   | No file  | `110614387bf4`  |
| 2302   | No file  | `110614387bf4`  |
| 2295   | No file  | `110614387bf4`  |
| 2290   | No file  | `110614387bf4`  |
| 2284   | No file  | `110614387bf4`  |
| 2276   | No file  | `110614387bf4`  |
| 2269   | No file  | `110614387bf4`  |
| 2259   | No file  | `110614387bf4`  |
| 2250   | No file  | `110614387bf4`  |
| 2243   | No file  | `110614387bf4`  |
| 2235   | No file  | `110614387bf4`  |
| 2229   | No file  | `110614387bf4`  |
| 2224   | No file  | `110614387bf4`  |
| 2218   | No file  | `110614387bf4`  |
| 2215   | No file  | `110614387bf4`  |
| 2207   | No file  | `110614387bf4`  |
| 2203   | No file  | `110614387bf4`  |
| 2196   | No file  | `110614387bf4`  |
| 2192   | No file  | `110614387bf4`  |
| 2189   | No file  | `110614387bf4`  |
| 2183   | No file  | `110614387bf4`  |
| 2179   | No file  | `110614387bf4`  |
| 2171   | No file  | `110614387bf4`  |
| 2163   | No file  | `110614387bf4`  |
| 2156   | No file  | `110614387bf4`  |
| 2151   | No file  | `110614387bf4`  |
| 2147   | No file  | `110614387bf4`  |
| 2142   | No file  | `110614387bf4`  |
| 2138   | No file  | `110614387bf4`  |
| 2134   | No file  | `110614387bf4`  |
| 2130   | No file  | `110614387bf4`  |
| 2122   | No file  | `110614387bf4`  |
| 2107   | No file  | `110614387bf4`  |
| 2098   | No file  | `110614387bf4`  |
| 2089   | No file  | `110614387bf4`  |
| 2081   | No file  | `110614387bf4`  |
| 2073   | No file  | `110614387bf4`  |
| 2067   | No file  | `110614387bf4`  |
| 2063   | No file  | `110614387bf4`  |
| 2059   | No file  | `110614387bf4`  |
| 2052   | No file  | `110614387bf4`  |
| 2044   | No file  | `110614387bf4`  |
| 2039   | No file  | `110614387bf4`  |
| 2032   | No file  | `110614387bf4`  |
| 2025   | No file  | `110614387bf4`  |
| 2011   | No file  | `110614387bf4`  |
| 2005   | No file  | `110614387bf4`  |
| 2000   | No file  | `110614387bf4`  |
| 1996   | No file  | `110614387bf4`  |
| 1991   | No file  | `110614387bf4`  |
| 1985   | No file  | `110614387bf4`  |
| 1980   | No file  | `110614387bf4`  |
| 1969   | No file  | `110614387bf4`  |
| 1964   | No file  | `110614387bf4`  |
| 1958   | No file  | `110614387bf4`  |
| 1950   | No file  | `110614387bf4`  |
| 1945   | No file  | `110614387bf4`  |
| 1937   | No file  | `110614387bf4`  |
| 1933   | No file  | `110614387bf4`  |
| 1927   | No file  | `110614387bf4`  |
| 1921   | No file  | `110614387bf4`  |
| 1914   | No file  | `110614387bf4`  |
| 1908   | No file  | `110614387bf4`  |
| 1897   | No file  | `110614387bf4`  |
| 1892   | No file  | `110614387bf4`  |
| 1886   | No file  | `110614387bf4`  |
| 1881   | No file  | `110614387bf4`  |
| 1871   | No file  | `110614387bf4`  |
| 1866   | No file  | `110614387bf4`  |
| 1862   | No file  | `110614387bf4`  |
| 1854   | No file  | `110614387bf4`  |
| 1846   | No file  | `110614387bf4`  |
| 1838   | No file  | `110614387bf4`  |
| 1832   | No file  | `110614387bf4`  |
| 1826   | No file  | `110614387bf4`  |
| 1822   | No file  | `110614387bf4`  |
| 1818   | No file  | `110614387bf4`  |
| 1804   | No file  | `110614387bf4`  |
| 1794   | No file  | `110614387bf4`  |
| 1790   | No file  | `110614387bf4`  |
| 1784   | No file  | `110614387bf4`  |
| 1774   | No file  | `110614387bf4`  |
| 1771   | No file  | `110614387bf4`  |
| 1762   | No file  | `110614387bf4`  |
| 1759   | No file  | `110614387bf4`  |
| 1754   | No file  | `110614387bf4`  |
| 1749   | No file  | `110614387bf4`  |
| 1743   | No file  | `110614387bf4`  |
| 1737   | No file  | `110614387bf4`  |
| 1731   | No file  | `110614387bf4`  |
| 1725   | No file  | `110614387bf4`  |
| 1717   | No file  | `110614387bf4`  |
| 1710   | No file  | `110614387bf4`  |
| 1704   | No file  | `110614387bf4`  |
| 1698   | No file  | `110614387bf4`  |
| 1690   | No file  | `110614387bf4`  |
| 1685   | No file  | `110614387bf4`  |
| 1680   | No file  | `110614387bf4`  |
| 1674   | No file  | `110614387bf4`  |
| 1668   | No file  | `110614387bf4`  |
| 1659   | No file  | `110614387bf4`  |
| 1649   | No file  | `110614387bf4`  |
| 1642   | No file  | `110614387bf4`  |
| 1636   | No file  | `110614387bf4`  |
| 1628   | No file  | `110614387bf4`  |
| 1622   | No file  | `110614387bf4`  |
| 1614   | No file  | `110614387bf4`  |
| 1608   | No file  | `110614387bf4`  |
| 1602   | No file  | `110614387bf4`  |
| 1598   | No file  | `110614387bf4`  |
| 1594   | No file  | `110614387bf4`  |
| 1590   | No file  | `110614387bf4`  |
| 1587   | No file  | `110614387bf4`  |
| 1584   | No file  | `110614387bf4`  |
| 1579   | No file  | `110614387bf4`  |
| 1572   | No file  | `110614387bf4`  |
| 1565   | No file  | `110614387bf4`  |
| 1559   | No file  | `110614387bf4`  |
| 1554   | No file  | `110614387bf4`  |
| 1547   | No file  | `110614387bf4`  |
| 1537   | No file  | `110614387bf4`  |
| 1529   | No file  | `110614387bf4`  |
| 1524   | No file  | `110614387bf4`  |
| 1519   | No file  | `110614387bf4`  |
| 1509   | No file  | `110614387bf4`  |
| 1506   | No file  | `110614387bf4`  |
| 1504   | No file  | `110614387bf4`  |
| 1500   | No file  | `110614387bf4`  |
| 1493   | No file  | `110614387bf4`  |
| 1489   | No file  | `110614387bf4`  |
| 1485   | No file  | `110614387bf4`  |
| 1481   | No file  | `110614387bf4`  |
| 1474   | No file  | `110614387bf4`  |
| 1466   | No file  | `110614387bf4`  |
| 1462   | No file  | `110614387bf4`  |
| 1459   | No file  | `110614387bf4`  |
| 1453   | No file  | `110614387bf4`  |
| 1450   | No file  | `110614387bf4`  |
| 1445   | No file  | `110614387bf4`  |
| 1439   | No file  | `110614387bf4`  |
| 1433   | No file  | `110614387bf4`  |
| 1430   | No file  | `110614387bf4`  |
| 1426   | No file  | `110614387bf4`  |
| 1421   | No file  | `110614387bf4`  |
| 1417   | No file  | `110614387bf4`  |
| 1416   | No file  | `110614387bf4`  |
| 1409   | No file  | `110614387bf4`  |
| 1405   | No file  | `110614387bf4`  |
| 1401   | No file  | `110614387bf4`  |
| 1396   | No file  | `110614387bf4`  |
| 1391   | No file  | `110614387bf4`  |
| 1390   | No file  | `110614387bf4`  |
| 1386   | No file  | `110614387bf4`  |
| 1381   | No file  | `110614387bf4`  |
| 1379   | No file  | `110614387bf4`  |
| 1372   | No file  | `110614387bf4`  |
| 1366   | No file  | `110614387bf4`  |
| 1364   | No file  | `110614387bf4`  |
| 1363   | No file  | `110614387bf4`  |
| 1360   | No file  | `110614387bf4`  |
| 1358   | No file  | `110614387bf4`  |
| 1355   | No file  | `110614387bf4`  |
| 1351   | No file  | `110614387bf4`  |
| 1348   | No file  | `110614387bf4`  |
| 1346   | No file  | `110614387bf4`  |
| 1341   | No file  | `110614387bf4`  |
| 1340   | No file  | `110614387bf4`  |
| 1338   | No file  | `110614387bf4`  |
| 1335   | No file  | `110614387bf4`  |
| 1333   | No file  | `110614387bf4`  |
| 1329   | No file  | `110614387bf4`  |
| 1327   | No file  | `110614387bf4`  |
| 1324   | No file  | `110614387bf4`  |
| 1321   | No file  | `110614387bf4`  |
| 1319   | No file  | `110614387bf4`  |
| 1318   | No file  | `110614387bf4`  |
| 1316   | No file  | `110614387bf4`  |
| 1313   | No file  | `110614387bf4`  |
| 1311   | No file  | `110614387bf4`  |
| 1309   | No file  | `110614387bf4`  |
| 1304   | No file  | `110614387bf4`  |
| 1292   | No file  | `110614387bf4`  |
| 1286   | No file  | `110614387bf4`  |
| 1280   | No file  | `110614387bf4`  |
| 1276   | No file  | `110614387bf4`  |
| 1267   | No file  | `110614387bf4`  |
| 1261   | No file  | `110614387bf4`  |
| 1256   | No file  | `110614387bf4`  |
| 1250   | No file  | `110614387bf4`  |
| 1246   | No file  | `110614387bf4`  |
| 1239   | No file  | `110614387bf4`  |
| 1230   | No file  | `110614387bf4`  |
| 1226   | No file  | `110614387bf4`  |
| 1220   | No file  | `110614387bf4`  |
| 1217   | No file  | `110614387bf4`  |
| 1211   | No file  | `110614387bf4`  |
| 1210   | No file  | `110614387bf4`  |
| 1208   | No file  | `110614387bf4`  |
| 1203   | No file  | `110614387bf4`  |
| 1197   | No file  | `110614387bf4`  |
| 1194   | No file  | `110614387bf4`  |
| 1192   | No file  | `110614387bf4`  |
| 1187   | No file  | `110614387bf4`  |
| 1183   | No file  | `110614387bf4`  |
| 1177   | No file  | `110614387bf4`  |
| 1173   | No file  | `110614387bf4`  |
| 1167   | No file  | `110614387bf4`  |
| 1164   | No file  | `110614387bf4`  |
| 1156   | No file  | `110614387bf4`  |
| 1149   | No file  | `110614387bf4`  |
| 1144   | No file  | `110614387bf4`  |
| 1137   | No file  | `110614387bf4`  |
| 1132   | No file  | `110614387bf4`  |
| 1127   | No file  | `110614387bf4`  |
| 1122   | No file  | `110614387bf4`  |
| 1118   | No file  | `110614387bf4`  |
| 1114   | No file  | `110614387bf4`  |
| 1109   | No file  | `110614387bf4`  |
| 1102   | No file  | `110614387bf4`  |
| 1096   | No file  | `110614387bf4`  |
| 1088   | No file  | `110614387bf4`  |
| 1081   | No file  | `110614387bf4`  |
| 1076   | No file  | `110614387bf4`  |
| 1069   | No file  | `110614387bf4`  |
| 1064   | No file  | `110614387bf4`  |
| 1058   | No file  | `110614387bf4`  |
| 1051   | No file  | `110614387bf4`  |
| 1044   | No file  | `110614387bf4`  |
| 1036   | No file  | `110614387bf4`  |
| 1026   | No file  | `110614387bf4`  |
| 1016   | No file  | `110614387bf4`  |
| 1009   | No file  | `110614387bf4`  |
| 1005   | No file  | `110614387bf4`  |
| 1000   | No file  | `110614387bf4`  |
| 998    | No file  | `110614387bf4`  |
| 990    | No file  | `110614387bf4`  |
| 979    | No file  | `110614387bf4`  |
| 972    | No file  | `110614387bf4`  |
| 963    | No file  | `110614387bf4`  |
| 955    | No file  | `110614387bf4`  |
| 946    | No file  | `110614387bf4`  |
| 938    | No file  | `110614387bf4`  |
| 927    | No file  | `110614387bf4`  |
| 911    | No file  | `110614387bf4`  |
| 904    | No file  | `110614387bf4`  |
| 899    | No file  | `110614387bf4`  |
| 894    | No file  | `110614387bf4`  |
| 885    | No file  | `110614387bf4`  |
| 879    | No file  | `110614387bf4`  |
| 872    | No file  | `110614387bf4`  |
| 864    | No file  | `110614387bf4`  |
| 855    | No file  | `110614387bf4`  |
| 853    | No file  | `110614387bf4`  |
| 845    | No file  | `110614387bf4`  |
| 837    | No file  | `110614387bf4`  |
| 829    | No file  | `110614387bf4`  |
| 822    | No file  | `110614387bf4`  |
| 814    | No file  | `110614387bf4`  |
| 805    | No file  | `110614387bf4`  |
| 794    | No file  | `110614387bf4`  |
| 787    | No file  | `110614387bf4`  |
| 780    | No file  | `110614387bf4`  |
| 771    | No file  | `110614387bf4`  |
| 760    | No file  | `110614387bf4`  |
| 748    | No file  | `110614387bf4`  |
| 741    | No file  | `110614387bf4`  |
| 736    | No file  | `110614387bf4`  |
| 731    | No file  | `110614387bf4`  |
| 723    | No file  | `110614387bf4`  |
| 711    | No file  | `110614387bf4`  |
| 707    | No file  | `110614387bf4`  |
| 697    | No file  | `110614387bf4`  |
| 689    | No file  | `110614387bf4`  |
| 683    | No file  | `110614387bf4`  |
| 678    | No file  | `110614387bf4`  |
| 670    | No file  | `110614387bf4`  |
| 661    | No file  | `110614387bf4`  |
| 656    | No file  | `110614387bf4`  |
| 652    | No file  | `110614387bf4`  |
| 643    | No file  | `110614387bf4`  |
| 637    | No file  | `110614387bf4`  |
| 630    | No file  | `110614387bf4`  |
| 627    | No file  | `110614387bf4`  |
| 621    | No file  | `110614387bf4`  |
| 617    | No file  | `110614387bf4`  |
| 615    | No file  | `110614387bf4`  |
| 606    | No file  | `110614387bf4`  |
| 599    | No file  | `110614387bf4`  |
| 592    | No file  | `110614387bf4`  |
| 586    | No file  | `110614387bf4`  |
| 577    | No file  | `110614387bf4`  |
| 569    | No file  | `110614387bf4`  |
| 561    | No file  | `110614387bf4`  |
| 554    | No file  | `110614387bf4`  |
| 542    | No file  | `110614387bf4`  |
| 532    | No file  | `110614387bf4`  |
| 531    | No file  | `110614387bf4`  |
| 526    | No file  | `110614387bf4`  |
| 521    | No file  | `110614387bf4`  |
| 517    | No file  | `110614387bf4`  |
| 510    | No file  | `110614387bf4`  |
| 508    | No file  | `110614387bf4`  |
| 504    | No file  | `110614387bf4`  |
| 497    | No file  | `110614387bf4`  |
| 491    | No file  | `110614387bf4`  |
| 485    | No file  | `110614387bf4`  |
| 478    | No file  | `110614387bf4`  |
| 472    | No file  | `110614387bf4`  |
| 466    | No file  | `110614387bf4`  |
| 457    | No file  | `110614387bf4`  |
| 452    | No file  | `110614387bf4`  |
| 449    | No file  | `110614387bf4`  |
| 435    | No file  | `110614387bf4`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                  |
| --------------------- | -------- | --------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Grade names, LOC type 37 under the RESOURCE sheet key hash            |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field          | Notes                                                              |
| ------------------- | -------------- | -------------- | ------------------------------------------------------------------ |
| `+0x00`             | char[4]        | magic          | ASCII `PABR`                                                       |
| `+0x04`             | u32            | rank_threshold | Number of players the ranking lists; `100` on client 3474          |
| `+0x08`             | u32            | unknown_08     | `3` on client 3474                                                 |
| `+0x0C`             | u32            | row_count      | Number of rows                                                     |
| `+0x10`             | Row[row_count] | rows           | See Row; byte-packed                                               |
| `rows+0x00`         | String Table   | string_table   | See String Table                                                   |
| `string_table+0x00` | u32            | table_start    | Offset of the string table, where `rows` ends                      |
| `string_table+0x04` | u32            | zero           | Always `0`                                                         |

### Row (10 bytes)

| Offset  | Type | Field     | Notes                                                                           |
| ------- | ---- | --------- | ------------------------------------------------------------------------------- |
| `+0x00` | u16  | grade_key | Grade, `0` to `9`, unique; see Grades                                           |
| `+0x02` | u32  | rank      | The one rank that holds the grade; `0` for a grade by percentage and for `0`    |
| `+0x06` | f32  | percent   | Top percentage of the grade; `0` for a grade by rank and for `0`                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Grades

The ranking window names each grade with a RESOURCE sheet key
(`panel_widget_ranking_hardcore_1.luac`, `initTierList`): grade keys 1 to 3
the `PANEL_HARDCOE_RANKING_TIER_0_<key>` keys of its first row, grade keys 4
to 9 `PANEL_HARDCOE_RANKING_TIERNAME_<key - 3>`, and grade 0 (no grade)
`PANEL_HARDCOE_RANKING_TIERNAME_7`. Its `_totalGradeCount` is `10`, and the
tier icon of a grade is the texture `HardcoreServer_Tier<key - 1>` (grade 0
uses the last one, `HardcoreServer_Tier09`). Client 3474:

| `grade_key` | `rank` | `percent` | Name (LOC type 37) |
| ----------- | ------ | --------- | ------------------ |
| `0`         | `0`    | `0`       | Novice             |
| `1`         | `1`    | `0`       | Transcendent       |
| `2`         | `2`    | `0`       | Conqueror          |
| `3`         | `3`    | `0`       | Reaper             |
| `4`         | `0`    | `1`       | Honorblade         |
| `5`         | `0`    | `5`       | Dawnblade          |
| `6`         | `0`    | `10`      | Flameblade         |
| `7`         | `0`    | `30`      | Duskblade          |
| `8`         | `0`    | `50`      | Veteran            |
| `9`         | `0`    | `100`     | Adept              |

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. The names follow the client Lua of client
3474 (`panel_widget_ranking_hardcore_1.luac`):

| Field            | Lua                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| `rank_threshold` | `ToClient_GetHardCoreTotalRankThreshold()`, the number of ranking slots the window builds (`_highRankerMaxCount`); the window scrolls, and `100` is the only head value that fits |
| `grade_key`      | `ToClient_GetHardCoreTotalRankGradeKeyByRank(rank)` returns it, and the window indexes its tiers by it |
| `rank`           | Grades 1 to 3 hold ranks 1 to 3, the three top ranks the window draws with the `1st`, `2nd` and `3rd` slots (`_topRankerCount = 3`) |
| `percent`        | `ToClient_GetHardCoreTotalRankGradePercentByKey(key)` for keys 4 to 9, shown as "Top {percent}%"     |

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/hardcore_tables.py`:
  one row per grade with its name, and `rank_threshold` on every row.

## Open Questions

### The Second Head Value

What `unknown_08` (`3`) is. It equals the number of grades held by one rank
and the ranking window's own `_topRankerCount`, but the window sets that
count in its Lua and calls no getter for it.
