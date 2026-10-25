# `questjournalvideoinfo.bss` Format

## Purpose

The video pages of the Land of the Morning Light journal: one fixed 13-byte
row per quest with a Bink video name and a full-size artwork image, both as
indices into a shared string table. The journal book shows the artwork on the
quest's page and plays the video from it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                        | Bytes | Records              | Row bytes |
| ------ | -------------- | --------------------------- | ----- | -------------------- | --------- |
| 1      | 2142 and later | `questjournalvideoinfo.bss` | 7,687 | 80 Journal Video Row | 13        |

| Layout | File                        | Known           | Unknown     |
| ------ | --------------------------- | --------------- | ----------- |
| 1      | `questjournalvideoinfo.bss` | 7,607 B (99.0%) | 80 B (1.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a918de485481`  |
| 3482   | Layout 1 | `a918de485481`  |
| 3474   | Layout 1 | `a918de485481`  |
| 3473   | Layout 1 | `a918de485481`  |
| 3464   | Layout 1 | `a918de485481`  |
| 3458   | Layout 1 | `a918de485481`  |
| 3454   | Layout 1 | `a918de485481`  |
| 3444   | Layout 1 | `a918de485481`  |
| 3435   | Layout 1 | `a918de485481`  |
| 3426   | Layout 1 | `a918de485481`  |
| 3418   | Layout 1 | `a918de485481`  |
| 3412   | Layout 1 | `a918de485481`  |
| 3402   | Layout 1 | `a918de485481`  |
| 3396   | Layout 1 | `a918de485481`  |
| 3387   | Layout 1 | `a918de485481`  |
| 3381   | Layout 1 | `a918de485481`  |
| 3373   | Layout 1 | `a918de485481`  |
| 3364   | Layout 1 | `a918de485481`  |
| 3356   | Layout 1 | `a918de485481`  |
| 3349   | Layout 1 | `a918de485481`  |
| 3342   | Layout 1 | `a918de485481`  |
| 3335   | Layout 1 | `a918de485481`  |
| 3326   | Layout 1 | `a918de485481`  |
| 3321   | Layout 1 | `a918de485481`  |
| 3314   | Layout 1 | `a918de485481`  |
| 3303   | Layout 1 | `a918de485481`  |
| 3302   | Layout 1 | `a918de485481`  |
| 3293   | Layout 1 | `a918de485481`  |
| 3283   | Layout 1 | `a918de485481`  |
| 3275   | Layout 1 | `a918de485481`  |
| 3267   | Layout 1 | `a918de485481`  |
| 3258   | Layout 1 | `a918de485481`  |
| 3251   | Layout 1 | `a918de485481`  |
| 3242   | Layout 1 | `a918de485481`  |
| 3235   | Layout 1 | `a918de485481`  |
| 3229   | Layout 1 | `a918de485481`  |
| 3212   | Layout 1 | `a918de485481`  |
| 3203   | Layout 1 | `a918de485481`  |
| 3193   | Layout 1 | `a918de485481`  |
| 3186   | Layout 1 | `a918de485481`  |
| 3177   | Layout 1 | `a918de485481`  |
| 3169   | Layout 1 | `a918de485481`  |
| 3158   | Layout 1 | `a918de485481`  |
| 3151   | Layout 1 | `a918de485481`  |
| 3144   | Layout 1 | `a918de485481`  |
| 3133   | Layout 1 | `a918de485481`  |
| 3125   | Layout 1 | `a918de485481`  |
| 3118   | Layout 1 | `a918de485481`  |
| 3111   | Layout 1 | `a918de485481`  |
| 3103   | Layout 1 | `a918de485481`  |
| 3095   | Layout 1 | `a918de485481`  |
| 3086   | Layout 1 | `a918de485481`  |
| 3072   | Layout 1 | `a918de485481`  |
| 3062   | Layout 1 | `a918de485481`  |
| 3052   | Layout 1 | `a918de485481`  |
| 3045   | Layout 1 | `a918de485481`  |
| 3037   | Layout 1 | `a918de485481`  |
| 3030   | Layout 1 | `a918de485481`  |
| 3021   | Layout 1 | `a918de485481`  |
| 3012   | Layout 1 | `a918de485481`  |
| 3002   | Layout 1 | `a918de485481`  |
| 2995   | Layout 1 | `a918de485481`  |
| 2987   | Layout 1 | `a918de485481`  |
| 2978   | Layout 1 | `a918de485481`  |
| 2970   | Layout 1 | `a918de485481`  |
| 2959   | Layout 1 | `a918de485481`  |
| 2951   | Layout 1 | `a918de485481`  |
| 2942   | Layout 1 | `a918de485481`  |
| 2935   | Layout 1 | `a918de485481`  |
| 2932   | Layout 1 | `a918de485481`  |
| 2923   | Layout 1 | `a918de485481`  |
| 2919   | Layout 1 | `a918de485481`  |
| 2907   | Layout 1 | `a918de485481`  |
| 2900   | Layout 1 | `a918de485481`  |
| 2891   | Layout 1 | `a918de485481`  |
| 2882   | Layout 1 | `a918de485481`  |
| 2872   | Layout 1 | `a918de485481`  |
| 2863   | Layout 1 | `a918de485481`  |
| 2855   | Layout 1 | `a918de485481`  |
| 2849   | Layout 1 | `a918de485481`  |
| 2844   | Layout 1 | `a918de485481`  |
| 2834   | Layout 1 | `a918de485481`  |
| 2825   | Layout 1 | `a918de485481`  |
| 2819   | Layout 1 | `a918de485481`  |
| 2811   | Layout 1 | `a918de485481`  |
| 2803   | Layout 1 | `a918de485481`  |
| 2794   | Layout 1 | `a918de485481`  |
| 2783   | Layout 1 | `a918de485481`  |
| 2774   | Layout 1 | `a918de485481`  |
| 2765   | Layout 1 | `a918de485481`  |
| 2756   | Layout 1 | `a918de485481`  |
| 2750   | Layout 1 | `a918de485481`  |
| 2743   | Layout 1 | `a918de485481`  |
| 2736   | Layout 1 | `a918de485481`  |
| 2726   | Layout 1 | `a918de485481`  |
| 2717   | Layout 1 | `a918de485481`  |
| 2709   | Layout 1 | `a918de485481`  |
| 2703   | Layout 1 | `a918de485481`  |
| 2695   | Layout 1 | `a918de485481`  |
| 2684   | Layout 1 | `a918de485481`  |
| 2672   | Layout 1 | `a918de485481`  |
| 2665   | Layout 1 | `a918de485481`  |
| 2657   | Layout 1 | `a918de485481`  |
| 2649   | Layout 1 | `a918de485481`  |
| 2644   | Layout 1 | `a918de485481`  |
| 2637   | Layout 1 | `a918de485481`  |
| 2629   | Layout 1 | `a918de485481`  |
| 2619   | Layout 1 | `a918de485481`  |
| 2612   | Layout 1 | `a918de485481`  |
| 2606   | Layout 1 | `a918de485481`  |
| 2602   | Layout 1 | `a918de485481`  |
| 2601   | Layout 1 | `a918de485481`  |
| 2592   | Layout 1 | `a918de485481`  |
| 2583   | Layout 1 | `a918de485481`  |
| 2575   | Layout 1 | `a918de485481`  |
| 2567   | Layout 1 | `a918de485481`  |
| 2560   | Layout 1 | `a918de485481`  |
| 2553   | Layout 1 | `a918de485481`  |
| 2545   | Layout 1 | `a918de485481`  |
| 2538   | Layout 1 | `a918de485481`  |
| 2529   | Layout 1 | `a918de485481`  |
| 2519   | Layout 1 | `a918de485481`  |
| 2513   | Layout 1 | `a918de485481`  |
| 2510   | Layout 1 | `a918de485481`  |
| 2507   | Layout 1 | `a918de485481`  |
| 2503   | Layout 1 | `a918de485481`  |
| 2498   | Layout 1 | `a918de485481`  |
| 2492   | Layout 1 | `a918de485481`  |
| 2487   | Layout 1 | `a918de485481`  |
| 2480   | Layout 1 | `a918de485481`  |
| 2474   | Layout 1 | `a918de485481`  |
| 2468   | Layout 1 | `a918de485481`  |
| 2460   | Layout 1 | `a918de485481`  |
| 2453   | Layout 1 | `a918de485481`  |
| 2444   | Layout 1 | `a918de485481`  |
| 2438   | Layout 1 | `a918de485481`  |
| 2434   | Layout 1 | `a918de485481`  |
| 2429   | Layout 1 | `a918de485481`  |
| 2421   | Layout 1 | `a918de485481`  |
| 2414   | Layout 1 | `a918de485481`  |
| 2407   | Layout 1 | `a918de485481`  |
| 2401   | Layout 1 | `a918de485481`  |
| 2397   | Layout 1 | `a918de485481`  |
| 2393   | Layout 1 | `a918de485481`  |
| 2384   | Layout 1 | `a918de485481`  |
| 2378   | Layout 1 | `a918de485481`  |
| 2372   | Layout 1 | `a918de485481`  |
| 2358   | Layout 1 | `a918de485481`  |
| 2352   | Layout 1 | `a918de485481`  |
| 2347   | Layout 1 | `a918de485481`  |
| 2343   | Layout 1 | `a918de485481`  |
| 2335   | Layout 1 | `a918de485481`  |
| 2327   | Layout 1 | `a918de485481`  |
| 2324   | Layout 1 | `a918de485481`  |
| 2319   | Layout 1 | `a918de485481`  |
| 2313   | Layout 1 | `a918de485481`  |
| 2308   | Layout 1 | `a918de485481`  |
| 2302   | Layout 1 | `a918de485481`  |
| 2295   | Layout 1 | `a918de485481`  |
| 2290   | Layout 1 | `a918de485481`  |
| 2284   | Layout 1 | `a918de485481`  |
| 2276   | Layout 1 | `a918de485481`  |
| 2269   | Layout 1 | `a918de485481`  |
| 2259   | Layout 1 | `a918de485481`  |
| 2250   | Layout 1 | `a918de485481`  |
| 2243   | Layout 1 | `a918de485481`  |
| 2235   | Layout 1 | `a918de485481`  |
| 2229   | Layout 1 | `a918de485481`  |
| 2224   | Layout 1 | `a918de485481`  |
| 2218   | Layout 1 | `a918de485481`  |
| 2215   | Layout 1 | `a918de485481`  |
| 2207   | Layout 1 | `a918de485481`  |
| 2203   | Layout 1 | `a918de485481`  |
| 2196   | Layout 1 | `a918de485481`  |
| 2192   | Layout 1 | `a918de485481`  |
| 2189   | Layout 1 | `a918de485481`  |
| 2183   | Layout 1 | `a918de485481`  |
| 2179   | Layout 1 | `a918de485481`  |
| 2171   | Layout 1 | `a918de485481`  |
| 2163   | Layout 1 | `a918de485481`  |
| 2156   | Layout 1 | `a918de485481`  |
| 2151   | Layout 1 | `a918de485481`  |
| 2147   | Layout 1 | `a918de485481`  |
| 2142   | Layout 1 | `a918de485481`  |
| 2138   | No file  | `a918de485481`  |
| 2134   | No file  | `a918de485481`  |
| 2130   | No file  | `a918de485481`  |
| 2122   | No file  | `a918de485481`  |
| 2107   | No file  | `a918de485481`  |
| 2098   | No file  | `a918de485481`  |
| 2089   | No file  | `a918de485481`  |
| 2081   | No file  | `a918de485481`  |
| 2073   | No file  | `a918de485481`  |
| 2067   | No file  | `a918de485481`  |
| 2063   | No file  | `a918de485481`  |
| 2059   | No file  | `a918de485481`  |
| 2052   | No file  | `a918de485481`  |
| 2044   | No file  | `a918de485481`  |
| 2039   | No file  | `a918de485481`  |
| 2032   | No file  | `a918de485481`  |
| 2025   | No file  | `a918de485481`  |
| 2011   | No file  | `a918de485481`  |
| 2005   | No file  | `a918de485481`  |
| 2000   | No file  | `a918de485481`  |
| 1996   | No file  | `a918de485481`  |
| 1991   | No file  | `a918de485481`  |
| 1985   | No file  | `a918de485481`  |
| 1980   | No file  | `a918de485481`  |
| 1969   | No file  | `a918de485481`  |
| 1964   | No file  | `a918de485481`  |
| 1958   | No file  | `a918de485481`  |
| 1950   | No file  | `a918de485481`  |
| 1945   | No file  | `a918de485481`  |
| 1937   | No file  | `a918de485481`  |
| 1933   | No file  | `a918de485481`  |
| 1927   | No file  | `a918de485481`  |
| 1921   | No file  | `a918de485481`  |
| 1914   | No file  | `a918de485481`  |
| 1908   | No file  | `a918de485481`  |
| 1897   | No file  | `a918de485481`  |
| 1892   | No file  | `a918de485481`  |
| 1886   | No file  | `a918de485481`  |
| 1881   | No file  | `a918de485481`  |
| 1871   | No file  | `a918de485481`  |
| 1866   | No file  | `a918de485481`  |
| 1862   | No file  | `a918de485481`  |
| 1854   | No file  | `a918de485481`  |
| 1846   | No file  | `a918de485481`  |
| 1838   | No file  | `a918de485481`  |
| 1832   | No file  | `a918de485481`  |
| 1826   | No file  | `a918de485481`  |
| 1822   | No file  | `a918de485481`  |
| 1818   | No file  | `a918de485481`  |
| 1804   | No file  | `a918de485481`  |
| 1794   | No file  | `a918de485481`  |
| 1790   | No file  | `a918de485481`  |
| 1784   | No file  | `a918de485481`  |
| 1774   | No file  | `a918de485481`  |
| 1771   | No file  | `a918de485481`  |
| 1762   | No file  | `a918de485481`  |
| 1759   | No file  | `a918de485481`  |
| 1754   | No file  | `a918de485481`  |
| 1749   | No file  | `a918de485481`  |
| 1743   | No file  | `a918de485481`  |
| 1737   | No file  | `a918de485481`  |
| 1731   | No file  | `a918de485481`  |
| 1725   | No file  | `a918de485481`  |
| 1717   | No file  | `a918de485481`  |
| 1710   | No file  | `a918de485481`  |
| 1704   | No file  | `a918de485481`  |
| 1698   | No file  | `a918de485481`  |
| 1690   | No file  | `a918de485481`  |
| 1685   | No file  | `a918de485481`  |
| 1680   | No file  | `a918de485481`  |
| 1674   | No file  | `a918de485481`  |
| 1668   | No file  | `a918de485481`  |
| 1659   | No file  | `a918de485481`  |
| 1649   | No file  | `a918de485481`  |
| 1642   | No file  | `a918de485481`  |
| 1636   | No file  | `a918de485481`  |
| 1628   | No file  | `a918de485481`  |
| 1622   | No file  | `a918de485481`  |
| 1614   | No file  | `a918de485481`  |
| 1608   | No file  | `a918de485481`  |
| 1602   | No file  | `a918de485481`  |
| 1598   | No file  | `a918de485481`  |
| 1594   | No file  | `a918de485481`  |
| 1590   | No file  | `a918de485481`  |
| 1587   | No file  | `a918de485481`  |
| 1584   | No file  | `a918de485481`  |
| 1579   | No file  | `a918de485481`  |
| 1572   | No file  | `a918de485481`  |
| 1565   | No file  | `a918de485481`  |
| 1559   | No file  | `a918de485481`  |
| 1554   | No file  | `a918de485481`  |
| 1547   | No file  | `a918de485481`  |
| 1537   | No file  | `a918de485481`  |
| 1529   | No file  | `a918de485481`  |
| 1524   | No file  | `a918de485481`  |
| 1519   | No file  | `a918de485481`  |
| 1509   | No file  | `a918de485481`  |
| 1506   | No file  | `a918de485481`  |
| 1504   | No file  | `a918de485481`  |
| 1500   | No file  | `a918de485481`  |
| 1493   | No file  | `a918de485481`  |
| 1489   | No file  | `a918de485481`  |
| 1485   | No file  | `a918de485481`  |
| 1481   | No file  | `a918de485481`  |
| 1474   | No file  | `a918de485481`  |
| 1466   | No file  | `a918de485481`  |
| 1462   | No file  | `a918de485481`  |
| 1459   | No file  | `a918de485481`  |
| 1453   | No file  | `a918de485481`  |
| 1450   | No file  | `a918de485481`  |
| 1445   | No file  | `a918de485481`  |
| 1439   | No file  | `a918de485481`  |
| 1433   | No file  | `a918de485481`  |
| 1430   | No file  | `a918de485481`  |
| 1426   | No file  | `a918de485481`  |
| 1421   | No file  | `a918de485481`  |
| 1417   | No file  | `a918de485481`  |
| 1416   | No file  | `a918de485481`  |
| 1409   | No file  | `a918de485481`  |
| 1405   | No file  | `a918de485481`  |
| 1401   | No file  | `a918de485481`  |
| 1396   | No file  | `a918de485481`  |
| 1391   | No file  | `a918de485481`  |
| 1390   | No file  | `a918de485481`  |
| 1386   | No file  | `a918de485481`  |
| 1381   | No file  | `a918de485481`  |
| 1379   | No file  | `a918de485481`  |
| 1372   | No file  | `a918de485481`  |
| 1366   | No file  | `a918de485481`  |
| 1364   | No file  | `a918de485481`  |
| 1363   | No file  | `a918de485481`  |
| 1360   | No file  | `a918de485481`  |
| 1358   | No file  | `a918de485481`  |
| 1355   | No file  | `a918de485481`  |
| 1351   | No file  | `a918de485481`  |
| 1348   | No file  | `a918de485481`  |
| 1346   | No file  | `a918de485481`  |
| 1341   | No file  | `a918de485481`  |
| 1340   | No file  | `a918de485481`  |
| 1338   | No file  | `a918de485481`  |
| 1335   | No file  | `a918de485481`  |
| 1333   | No file  | `a918de485481`  |
| 1329   | No file  | `a918de485481`  |
| 1327   | No file  | `a918de485481`  |
| 1324   | No file  | `a918de485481`  |
| 1321   | No file  | `a918de485481`  |
| 1319   | No file  | `a918de485481`  |
| 1318   | No file  | `a918de485481`  |
| 1316   | No file  | `a918de485481`  |
| 1313   | No file  | `a918de485481`  |
| 1311   | No file  | `a918de485481`  |
| 1309   | No file  | `a918de485481`  |
| 1304   | No file  | `a918de485481`  |
| 1292   | No file  | `a918de485481`  |
| 1286   | No file  | `a918de485481`  |
| 1280   | No file  | `a918de485481`  |
| 1276   | No file  | `a918de485481`  |
| 1267   | No file  | `a918de485481`  |
| 1261   | No file  | `a918de485481`  |
| 1256   | No file  | `a918de485481`  |
| 1250   | No file  | `a918de485481`  |
| 1246   | No file  | `a918de485481`  |
| 1239   | No file  | `a918de485481`  |
| 1230   | No file  | `a918de485481`  |
| 1226   | No file  | `a918de485481`  |
| 1220   | No file  | `a918de485481`  |
| 1217   | No file  | `a918de485481`  |
| 1211   | No file  | `a918de485481`  |
| 1210   | No file  | `a918de485481`  |
| 1208   | No file  | `a918de485481`  |
| 1203   | No file  | `a918de485481`  |
| 1197   | No file  | `a918de485481`  |
| 1194   | No file  | `a918de485481`  |
| 1192   | No file  | `a918de485481`  |
| 1187   | No file  | `a918de485481`  |
| 1183   | No file  | `a918de485481`  |
| 1177   | No file  | `a918de485481`  |
| 1173   | No file  | `a918de485481`  |
| 1167   | No file  | `a918de485481`  |
| 1164   | No file  | `a918de485481`  |
| 1156   | No file  | `a918de485481`  |
| 1149   | No file  | `a918de485481`  |
| 1144   | No file  | `a918de485481`  |
| 1137   | No file  | `a918de485481`  |
| 1132   | No file  | `a918de485481`  |
| 1127   | No file  | `a918de485481`  |
| 1122   | No file  | `a918de485481`  |
| 1118   | No file  | `a918de485481`  |
| 1114   | No file  | `a918de485481`  |
| 1109   | No file  | `a918de485481`  |
| 1102   | No file  | `a918de485481`  |
| 1096   | No file  | `a918de485481`  |
| 1088   | No file  | `a918de485481`  |
| 1081   | No file  | `a918de485481`  |
| 1076   | No file  | `a918de485481`  |
| 1069   | No file  | `a918de485481`  |
| 1064   | No file  | `a918de485481`  |
| 1058   | No file  | `a918de485481`  |
| 1051   | No file  | `a918de485481`  |
| 1044   | No file  | `a918de485481`  |
| 1036   | No file  | `a918de485481`  |
| 1026   | No file  | `a918de485481`  |
| 1016   | No file  | `a918de485481`  |
| 1009   | No file  | `a918de485481`  |
| 1005   | No file  | `a918de485481`  |
| 1000   | No file  | `a918de485481`  |
| 998    | No file  | `a918de485481`  |
| 990    | No file  | `a918de485481`  |
| 979    | No file  | `a918de485481`  |
| 972    | No file  | `a918de485481`  |
| 963    | No file  | `a918de485481`  |
| 955    | No file  | `a918de485481`  |
| 946    | No file  | `a918de485481`  |
| 938    | No file  | `a918de485481`  |
| 927    | No file  | `a918de485481`  |
| 911    | No file  | `a918de485481`  |
| 904    | No file  | `a918de485481`  |
| 899    | No file  | `a918de485481`  |
| 894    | No file  | `a918de485481`  |
| 885    | No file  | `a918de485481`  |
| 879    | No file  | `a918de485481`  |
| 872    | No file  | `a918de485481`  |
| 864    | No file  | `a918de485481`  |
| 855    | No file  | `a918de485481`  |
| 853    | No file  | `a918de485481`  |
| 845    | No file  | `a918de485481`  |
| 837    | No file  | `a918de485481`  |
| 829    | No file  | `a918de485481`  |
| 822    | No file  | `a918de485481`  |
| 814    | No file  | `a918de485481`  |
| 805    | No file  | `a918de485481`  |
| 794    | No file  | `a918de485481`  |
| 787    | No file  | `a918de485481`  |
| 780    | No file  | `a918de485481`  |
| 771    | No file  | `a918de485481`  |
| 760    | No file  | `a918de485481`  |
| 748    | No file  | `a918de485481`  |
| 741    | No file  | `a918de485481`  |
| 736    | No file  | `a918de485481`  |
| 731    | No file  | `a918de485481`  |
| 723    | No file  | `a918de485481`  |
| 711    | No file  | `a918de485481`  |
| 707    | No file  | `a918de485481`  |
| 697    | No file  | `a918de485481`  |
| 689    | No file  | `a918de485481`  |
| 683    | No file  | `a918de485481`  |
| 678    | No file  | `a918de485481`  |
| 670    | No file  | `a918de485481`  |
| 661    | No file  | `a918de485481`  |
| 656    | No file  | `a918de485481`  |
| 652    | No file  | `a918de485481`  |
| 643    | No file  | `a918de485481`  |
| 637    | No file  | `a918de485481`  |
| 630    | No file  | `a918de485481`  |
| 627    | No file  | `a918de485481`  |
| 621    | No file  | `a918de485481`  |
| 617    | No file  | `a918de485481`  |
| 615    | No file  | `a918de485481`  |
| 606    | No file  | `a918de485481`  |
| 599    | No file  | `a918de485481`  |
| 592    | No file  | `a918de485481`  |
| 586    | No file  | `a918de485481`  |
| 577    | No file  | `a918de485481`  |
| 569    | No file  | `a918de485481`  |
| 561    | No file  | `a918de485481`  |
| 554    | No file  | `a918de485481`  |
| 542    | No file  | `a918de485481`  |
| 532    | No file  | `a918de485481`  |
| 531    | No file  | `a918de485481`  |
| 526    | No file  | `a918de485481`  |
| 521    | No file  | `a918de485481`  |
| 517    | No file  | `a918de485481`  |
| 510    | No file  | `a918de485481`  |
| 508    | No file  | `a918de485481`  |
| 504    | No file  | `a918de485481`  |
| 497    | No file  | `a918de485481`  |
| 491    | No file  | `a918de485481`  |
| 485    | No file  | `a918de485481`  |
| 478    | No file  | `a918de485481`  |
| 472    | No file  | `a918de485481`  |
| 466    | No file  | `a918de485481`  |
| 457    | No file  | `a918de485481`  |
| 452    | No file  | `a918de485481`  |
| 449    | No file  | `a918de485481`  |
| 435    | No file  | `a918de485481`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 keyed by (`quest_chain_id`, `quest_id`)    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset              | Type                     | Field        | Notes                                          |
| ------------------- | ------------------------ | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]                  | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                      | count        | Number of rows; 80 on client 3458              |
| `+0x08`             | Journal Video Row[count] | rows         | 13-byte rows repeated `count` times            |
| `rows+0x00`         | String Table             | string_table | See String Table                               |
| `string_table+0x00` | u32                      | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                      | zero         | Always 0                                       |

The rows are grouped by quest chain but in no sorted order: chains 8700 to
8714 come first, then 8542 to 8554, and sub IDs run up in some chains and down
in others.

### Journal Video Row (13 bytes)

| Offset  | Type | Field          | Notes                                                                  |
| ------- | ---- | -------------- | ---------------------------------------------------------------------- |
| `+0x00` | u16  | quest_chain_id | Quest chain (main ID), 8542 to 8554 and 8700 to 8714 on client 3458    |
| `+0x02` | u16  | quest_id       | Quest within the chain (sub ID); `quest_id << 16 \| quest_chain_id` is the packed quest ID of `allquestlist.bss` |
| `+0x04` | u32  | video_ref      | String table index of the video name, relative to `ui_movie/pc/`, no extension |
| `+0x08` | u32  | artwork_ref    | String table index of the artwork path, relative to `ui_texture/`       |
| `+0x0C` | u8   | unknown_0c     | Always `1`                                                             |

### String Table (variable: 4 bytes + strings)

158 strings on client 3458, all referenced, never shared between a video and
an artwork entry. Two videos are used by two quests each
(`MorningLandPT2_Sub_8527_8_01` by 8550/4 and 8550/5,
`MorningLandPT2_Sub_8541_1_01` by 8554/2 and 8554/3); every artwork path is
used once.

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | 158 on client 3458                        |
| `+0x04` | pstr[string_count] | strings      | u8 is_wide, u32 byte length, then payload |

## Notes

- The journal book scripts (`window/achievement/panel_window_journal_book_all`
  and `panel_window_achievement_morningland_1`) ask
  `ToClient_IsExistJournalVideoData(questNo)` for a page's quest, mark it as a
  video page, and draw the artwork through
  `ToClient_ChangeQuestIconFromIconPath` into `_stc_artworkImage`.
- Every row's quest has a `quest.dbss` icon (`QUEST_ICON`), and in 74 of 80
  the artwork is that icon's full-size version: the same name with `_Full`
  added (`morningland_boss_03_02.dds` -> `MorningLand_Boss_03_02_Full.dds`).
  The other six use a different name (8551/3 shows `8551_4_Full.dds`;
  8543/9 has the icon `morninglandpt2_boss_8543_1.dds` but the artwork
  `MorningLandPT2_Boss_8534_1_Full.dds`). The app indexes the artwork by packed quest ID
  (`IndexKind.QUEST_ARTWORK_ICON`, read through `IconKind.QUEST_ARTWORK`),
  apart from the quest icons: it is a page illustration, not the quest's
  icon, so `QUEST_ICON` keeps its own paths.
- On client 3458 all 80 videos exist as `ui_movie/pc/<video>.bk2` (lowercased),
  each with a `.srt` subtitle file beside it and `_de_`, `_fr_` and `_sp_`
  subtitle variants; the voice banks are `sound2022/windows/<language>/bink_<name>.bnk`.
  All 80 artwork files exist.
- All 80 quests have a LOC type 18 title, all `[Storybook] ...`.

## Open Questions

### What does `unknown_0c` hold?

It is `1` in all 80 rows. It may be an "enabled" flag or a page kind for
the journal book, but with a single value on the current client nothing in
the file tells them apart. The client 1784 private server sources name
nothing here: its `binary/` folder has no `questjournalvideoinfo.bss`, its
server dump has no `Video` string, and its sheets have no video or artwork
sheet (`Quest_Journal` is the [`journalquest.dbss`](journalquest_dbss.md)
source).
