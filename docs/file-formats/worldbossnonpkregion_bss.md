# `worldbossnonpkregion.bss` Format

## Purpose

The non-PK regions of each world boss: one row per boss character key with
a list of `regioninfo.bss` region keys. On client 3474 the file has 35
rows: the world bosses (Kzarka, Nouver, Karanda, Kutum, Offin, Garmoth,
Vell, Quint, Muraka) and their stronger forms, Black Wings, the Land of the
Morning Light bosses (Golden Pig King, Sangoon, Uturi, Bulgasal and the
four Dark Bonghwang), and event bosses such as Isabella, Targargo, Piku and
Gift Box, each with the regions around its spawn (Serendia Shrine for
Kzarka, Garmoth's Nest for Garmoth, Margoria for Vell).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes | Records | Row bytes               |
| ------ | -------------- | -------------------------- | ----- | ------- | ----------------------- |
| 1      | 1421 and later | `worldbossnonpkregion.bss` | 408   | 35 Row  | 10 to 18, 11 on average |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 1      | `worldbossnonpkregion.bss` | 408 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `657601802240`  |
| 3482   | Layout 1 | `657601802240`  |
| 3474   | Layout 1 | `657601802240`  |
| 3473   | Layout 1 | `657601802240`  |
| 3464   | Layout 1 | `657601802240`  |
| 3458   | Layout 1 | `657601802240`  |
| 3454   | Layout 1 | `657601802240`  |
| 3444   | Layout 1 | `657601802240`  |
| 3435   | Layout 1 | `657601802240`  |
| 3426   | Layout 1 | `657601802240`  |
| 3418   | Layout 1 | `657601802240`  |
| 3412   | Layout 1 | `657601802240`  |
| 3402   | Layout 1 | `657601802240`  |
| 3396   | Layout 1 | `657601802240`  |
| 3387   | Layout 1 | `657601802240`  |
| 3381   | Layout 1 | `657601802240`  |
| 3373   | Layout 1 | `657601802240`  |
| 3364   | Layout 1 | `657601802240`  |
| 3356   | Layout 1 | `657601802240`  |
| 3349   | Layout 1 | `657601802240`  |
| 3342   | Layout 1 | `657601802240`  |
| 3335   | Layout 1 | `657601802240`  |
| 3326   | Layout 1 | `657601802240`  |
| 3321   | Layout 1 | `657601802240`  |
| 3314   | Layout 1 | `657601802240`  |
| 3303   | Layout 1 | `657601802240`  |
| 3302   | Layout 1 | `657601802240`  |
| 3293   | Layout 1 | `657601802240`  |
| 3283   | Layout 1 | `657601802240`  |
| 3275   | Layout 1 | `657601802240`  |
| 3267   | Layout 1 | `657601802240`  |
| 3258   | Layout 1 | `657601802240`  |
| 3251   | Layout 1 | `657601802240`  |
| 3242   | Layout 1 | `657601802240`  |
| 3235   | Layout 1 | `657601802240`  |
| 3229   | Layout 1 | `657601802240`  |
| 3212   | Layout 1 | `657601802240`  |
| 3203   | Layout 1 | `657601802240`  |
| 3193   | Layout 1 | `657601802240`  |
| 3186   | Layout 1 | `657601802240`  |
| 3177   | Layout 1 | `657601802240`  |
| 3169   | Layout 1 | `657601802240`  |
| 3158   | Layout 1 | `657601802240`  |
| 3151   | Layout 1 | `657601802240`  |
| 3144   | Layout 1 | `657601802240`  |
| 3133   | Layout 1 | `657601802240`  |
| 3125   | Layout 1 | `657601802240`  |
| 3118   | Layout 1 | `657601802240`  |
| 3111   | Layout 1 | `657601802240`  |
| 3103   | Layout 1 | `657601802240`  |
| 3095   | Layout 1 | `657601802240`  |
| 3086   | Layout 1 | `657601802240`  |
| 3072   | Layout 1 | `657601802240`  |
| 3062   | Layout 1 | `657601802240`  |
| 3052   | Layout 1 | `657601802240`  |
| 3045   | Layout 1 | `657601802240`  |
| 3037   | Layout 1 | `657601802240`  |
| 3030   | Layout 1 | `657601802240`  |
| 3021   | Layout 1 | `657601802240`  |
| 3012   | Layout 1 | `657601802240`  |
| 3002   | Layout 1 | `657601802240`  |
| 2995   | Layout 1 | `657601802240`  |
| 2987   | Layout 1 | `657601802240`  |
| 2978   | Layout 1 | `657601802240`  |
| 2970   | Layout 1 | `657601802240`  |
| 2959   | Layout 1 | `657601802240`  |
| 2951   | Layout 1 | `657601802240`  |
| 2942   | Layout 1 | `657601802240`  |
| 2935   | Layout 1 | `657601802240`  |
| 2932   | Layout 1 | `657601802240`  |
| 2923   | Layout 1 | `657601802240`  |
| 2919   | Layout 1 | `657601802240`  |
| 2907   | Layout 1 | `657601802240`  |
| 2900   | Layout 1 | `657601802240`  |
| 2891   | Layout 1 | `657601802240`  |
| 2882   | Layout 1 | `657601802240`  |
| 2872   | Layout 1 | `657601802240`  |
| 2863   | Layout 1 | `657601802240`  |
| 2855   | Layout 1 | `657601802240`  |
| 2849   | Layout 1 | `657601802240`  |
| 2844   | Layout 1 | `657601802240`  |
| 2834   | Layout 1 | `657601802240`  |
| 2825   | Layout 1 | `657601802240`  |
| 2819   | Layout 1 | `657601802240`  |
| 2811   | Layout 1 | `657601802240`  |
| 2803   | Layout 1 | `657601802240`  |
| 2794   | Layout 1 | `657601802240`  |
| 2783   | Layout 1 | `657601802240`  |
| 2774   | Layout 1 | `657601802240`  |
| 2765   | Layout 1 | `657601802240`  |
| 2756   | Layout 1 | `657601802240`  |
| 2750   | Layout 1 | `657601802240`  |
| 2743   | Layout 1 | `657601802240`  |
| 2736   | Layout 1 | `657601802240`  |
| 2726   | Layout 1 | `657601802240`  |
| 2717   | Layout 1 | `657601802240`  |
| 2709   | Layout 1 | `657601802240`  |
| 2703   | Layout 1 | `657601802240`  |
| 2695   | Layout 1 | `657601802240`  |
| 2684   | Layout 1 | `657601802240`  |
| 2672   | Layout 1 | `657601802240`  |
| 2665   | Layout 1 | `657601802240`  |
| 2657   | Layout 1 | `657601802240`  |
| 2649   | Layout 1 | `657601802240`  |
| 2644   | Layout 1 | `657601802240`  |
| 2637   | Layout 1 | `657601802240`  |
| 2629   | Layout 1 | `657601802240`  |
| 2619   | Layout 1 | `657601802240`  |
| 2612   | Layout 1 | `657601802240`  |
| 2606   | Layout 1 | `657601802240`  |
| 2602   | Layout 1 | `657601802240`  |
| 2601   | Layout 1 | `657601802240`  |
| 2592   | Layout 1 | `657601802240`  |
| 2583   | Layout 1 | `657601802240`  |
| 2575   | Layout 1 | `657601802240`  |
| 2567   | Layout 1 | `657601802240`  |
| 2560   | Layout 1 | `657601802240`  |
| 2553   | Layout 1 | `657601802240`  |
| 2545   | Layout 1 | `657601802240`  |
| 2538   | Layout 1 | `657601802240`  |
| 2529   | Layout 1 | `657601802240`  |
| 2519   | Layout 1 | `657601802240`  |
| 2513   | Layout 1 | `657601802240`  |
| 2510   | Layout 1 | `657601802240`  |
| 2507   | Layout 1 | `657601802240`  |
| 2503   | Layout 1 | `657601802240`  |
| 2498   | Layout 1 | `657601802240`  |
| 2492   | Layout 1 | `657601802240`  |
| 2487   | Layout 1 | `657601802240`  |
| 2480   | Layout 1 | `657601802240`  |
| 2474   | Layout 1 | `657601802240`  |
| 2468   | Layout 1 | `657601802240`  |
| 2460   | Layout 1 | `657601802240`  |
| 2453   | Layout 1 | `657601802240`  |
| 2444   | Layout 1 | `657601802240`  |
| 2438   | Layout 1 | `657601802240`  |
| 2434   | Layout 1 | `657601802240`  |
| 2429   | Layout 1 | `657601802240`  |
| 2421   | Layout 1 | `657601802240`  |
| 2414   | Layout 1 | `657601802240`  |
| 2407   | Layout 1 | `657601802240`  |
| 2401   | Layout 1 | `657601802240`  |
| 2397   | Layout 1 | `657601802240`  |
| 2393   | Layout 1 | `657601802240`  |
| 2384   | Layout 1 | `657601802240`  |
| 2378   | Layout 1 | `657601802240`  |
| 2372   | Layout 1 | `657601802240`  |
| 2358   | Layout 1 | `657601802240`  |
| 2352   | Layout 1 | `657601802240`  |
| 2347   | Layout 1 | `657601802240`  |
| 2343   | Layout 1 | `657601802240`  |
| 2335   | Layout 1 | `657601802240`  |
| 2327   | Layout 1 | `657601802240`  |
| 2324   | Layout 1 | `657601802240`  |
| 2319   | Layout 1 | `657601802240`  |
| 2313   | Layout 1 | `657601802240`  |
| 2308   | Layout 1 | `657601802240`  |
| 2302   | Layout 1 | `657601802240`  |
| 2295   | Layout 1 | `657601802240`  |
| 2290   | Layout 1 | `657601802240`  |
| 2284   | Layout 1 | `657601802240`  |
| 2276   | Layout 1 | `657601802240`  |
| 2269   | Layout 1 | `657601802240`  |
| 2259   | Layout 1 | `657601802240`  |
| 2250   | Layout 1 | `657601802240`  |
| 2243   | Layout 1 | `657601802240`  |
| 2235   | Layout 1 | `657601802240`  |
| 2229   | Layout 1 | `657601802240`  |
| 2224   | Layout 1 | `657601802240`  |
| 2218   | Layout 1 | `657601802240`  |
| 2215   | Layout 1 | `657601802240`  |
| 2207   | Layout 1 | `657601802240`  |
| 2203   | Layout 1 | `657601802240`  |
| 2196   | Layout 1 | `657601802240`  |
| 2192   | Layout 1 | `657601802240`  |
| 2189   | Layout 1 | `657601802240`  |
| 2183   | Layout 1 | `657601802240`  |
| 2179   | Layout 1 | `657601802240`  |
| 2171   | Layout 1 | `657601802240`  |
| 2163   | Layout 1 | `657601802240`  |
| 2156   | Layout 1 | `657601802240`  |
| 2151   | Layout 1 | `657601802240`  |
| 2147   | Layout 1 | `657601802240`  |
| 2142   | Layout 1 | `657601802240`  |
| 2138   | Layout 1 | `657601802240`  |
| 2134   | Layout 1 | `657601802240`  |
| 2130   | Layout 1 | `657601802240`  |
| 2122   | Layout 1 | `657601802240`  |
| 2107   | Layout 1 | `657601802240`  |
| 2098   | Layout 1 | `657601802240`  |
| 2089   | Layout 1 | `657601802240`  |
| 2081   | Layout 1 | `657601802240`  |
| 2073   | Layout 1 | `657601802240`  |
| 2067   | Layout 1 | `657601802240`  |
| 2063   | Layout 1 | `657601802240`  |
| 2059   | Layout 1 | `657601802240`  |
| 2052   | Layout 1 | `657601802240`  |
| 2044   | Layout 1 | `657601802240`  |
| 2039   | Layout 1 | `657601802240`  |
| 2032   | Layout 1 | `657601802240`  |
| 2025   | Layout 1 | `657601802240`  |
| 2011   | Layout 1 | `657601802240`  |
| 2005   | Layout 1 | `657601802240`  |
| 2000   | Layout 1 | `657601802240`  |
| 1996   | Layout 1 | `657601802240`  |
| 1991   | Layout 1 | `657601802240`  |
| 1985   | Layout 1 | `657601802240`  |
| 1980   | Layout 1 | `657601802240`  |
| 1969   | Layout 1 | `657601802240`  |
| 1964   | Layout 1 | `657601802240`  |
| 1958   | Layout 1 | `657601802240`  |
| 1950   | Layout 1 | `657601802240`  |
| 1945   | Layout 1 | `657601802240`  |
| 1937   | Layout 1 | `657601802240`  |
| 1933   | Layout 1 | `657601802240`  |
| 1927   | Layout 1 | `657601802240`  |
| 1921   | Layout 1 | `657601802240`  |
| 1914   | Layout 1 | `657601802240`  |
| 1908   | Layout 1 | `657601802240`  |
| 1897   | Layout 1 | `657601802240`  |
| 1892   | Layout 1 | `657601802240`  |
| 1886   | Layout 1 | `657601802240`  |
| 1881   | Layout 1 | `657601802240`  |
| 1871   | Layout 1 | `657601802240`  |
| 1866   | Layout 1 | `657601802240`  |
| 1862   | Layout 1 | `657601802240`  |
| 1854   | Layout 1 | `657601802240`  |
| 1846   | Layout 1 | `657601802240`  |
| 1838   | Layout 1 | `657601802240`  |
| 1832   | Layout 1 | `657601802240`  |
| 1826   | Layout 1 | `657601802240`  |
| 1822   | Layout 1 | `657601802240`  |
| 1818   | Layout 1 | `657601802240`  |
| 1804   | Layout 1 | `657601802240`  |
| 1794   | Layout 1 | `657601802240`  |
| 1790   | Layout 1 | `657601802240`  |
| 1784   | Layout 1 | `657601802240`  |
| 1774   | Layout 1 | `657601802240`  |
| 1771   | Layout 1 | `657601802240`  |
| 1762   | Layout 1 | `657601802240`  |
| 1759   | Layout 1 | `657601802240`  |
| 1754   | Layout 1 | `657601802240`  |
| 1749   | Layout 1 | `657601802240`  |
| 1743   | Layout 1 | `657601802240`  |
| 1737   | Layout 1 | `657601802240`  |
| 1731   | Layout 1 | `657601802240`  |
| 1725   | Layout 1 | `657601802240`  |
| 1717   | Layout 1 | `657601802240`  |
| 1710   | Layout 1 | `657601802240`  |
| 1704   | Layout 1 | `657601802240`  |
| 1698   | Layout 1 | `657601802240`  |
| 1690   | Layout 1 | `657601802240`  |
| 1685   | Layout 1 | `657601802240`  |
| 1680   | Layout 1 | `657601802240`  |
| 1674   | Layout 1 | `657601802240`  |
| 1668   | Layout 1 | `657601802240`  |
| 1659   | Layout 1 | `657601802240`  |
| 1649   | Layout 1 | `657601802240`  |
| 1642   | Layout 1 | `657601802240`  |
| 1636   | Layout 1 | `657601802240`  |
| 1628   | Layout 1 | `657601802240`  |
| 1622   | Layout 1 | `657601802240`  |
| 1614   | Layout 1 | `657601802240`  |
| 1608   | Layout 1 | `657601802240`  |
| 1602   | Layout 1 | `657601802240`  |
| 1598   | Layout 1 | `657601802240`  |
| 1594   | Layout 1 | `657601802240`  |
| 1590   | Layout 1 | `657601802240`  |
| 1587   | Layout 1 | `657601802240`  |
| 1584   | Layout 1 | `657601802240`  |
| 1579   | Layout 1 | `657601802240`  |
| 1572   | Layout 1 | `657601802240`  |
| 1565   | Layout 1 | `657601802240`  |
| 1559   | Layout 1 | `657601802240`  |
| 1554   | Layout 1 | `657601802240`  |
| 1547   | Layout 1 | `657601802240`  |
| 1537   | Layout 1 | `657601802240`  |
| 1529   | Layout 1 | `657601802240`  |
| 1524   | Layout 1 | `657601802240`  |
| 1519   | Layout 1 | `657601802240`  |
| 1509   | Layout 1 | `657601802240`  |
| 1506   | Layout 1 | `657601802240`  |
| 1504   | Layout 1 | `657601802240`  |
| 1500   | Layout 1 | `657601802240`  |
| 1493   | Layout 1 | `657601802240`  |
| 1489   | Layout 1 | `657601802240`  |
| 1485   | Layout 1 | `657601802240`  |
| 1481   | Layout 1 | `657601802240`  |
| 1474   | Layout 1 | `657601802240`  |
| 1466   | Layout 1 | `657601802240`  |
| 1462   | Layout 1 | `657601802240`  |
| 1459   | Layout 1 | `657601802240`  |
| 1453   | Layout 1 | `657601802240`  |
| 1450   | Layout 1 | `657601802240`  |
| 1445   | Layout 1 | `657601802240`  |
| 1439   | Layout 1 | `657601802240`  |
| 1433   | Layout 1 | `657601802240`  |
| 1430   | Layout 1 | `657601802240`  |
| 1426   | Layout 1 | `657601802240`  |
| 1421   | Layout 1 | `657601802240`  |
| 1417   | No file  | `657601802240`  |
| 1416   | No file  | `657601802240`  |
| 1409   | No file  | `657601802240`  |
| 1405   | No file  | `657601802240`  |
| 1401   | No file  | `657601802240`  |
| 1396   | No file  | `657601802240`  |
| 1391   | No file  | `657601802240`  |
| 1390   | No file  | `657601802240`  |
| 1386   | No file  | `657601802240`  |
| 1381   | No file  | `657601802240`  |
| 1379   | No file  | `657601802240`  |
| 1372   | No file  | `657601802240`  |
| 1366   | No file  | `657601802240`  |
| 1364   | No file  | `657601802240`  |
| 1363   | No file  | `657601802240`  |
| 1360   | No file  | `657601802240`  |
| 1358   | No file  | `657601802240`  |
| 1355   | No file  | `657601802240`  |
| 1351   | No file  | `657601802240`  |
| 1348   | No file  | `657601802240`  |
| 1346   | No file  | `657601802240`  |
| 1341   | No file  | `657601802240`  |
| 1340   | No file  | `657601802240`  |
| 1338   | No file  | `657601802240`  |
| 1335   | No file  | `657601802240`  |
| 1333   | No file  | `657601802240`  |
| 1329   | No file  | `657601802240`  |
| 1327   | No file  | `657601802240`  |
| 1324   | No file  | `657601802240`  |
| 1321   | No file  | `657601802240`  |
| 1319   | No file  | `657601802240`  |
| 1318   | No file  | `657601802240`  |
| 1316   | No file  | `657601802240`  |
| 1313   | No file  | `657601802240`  |
| 1311   | No file  | `657601802240`  |
| 1309   | No file  | `657601802240`  |
| 1304   | No file  | `657601802240`  |
| 1292   | No file  | `657601802240`  |
| 1286   | No file  | `657601802240`  |
| 1280   | No file  | `657601802240`  |
| 1276   | No file  | `657601802240`  |
| 1267   | No file  | `657601802240`  |
| 1261   | No file  | `657601802240`  |
| 1256   | No file  | `657601802240`  |
| 1250   | No file  | `657601802240`  |
| 1246   | No file  | `657601802240`  |
| 1239   | No file  | `657601802240`  |
| 1230   | No file  | `657601802240`  |
| 1226   | No file  | `657601802240`  |
| 1220   | No file  | `657601802240`  |
| 1217   | No file  | `657601802240`  |
| 1211   | No file  | `657601802240`  |
| 1210   | No file  | `657601802240`  |
| 1208   | No file  | `657601802240`  |
| 1203   | No file  | `657601802240`  |
| 1197   | No file  | `657601802240`  |
| 1194   | No file  | `657601802240`  |
| 1192   | No file  | `657601802240`  |
| 1187   | No file  | `657601802240`  |
| 1183   | No file  | `657601802240`  |
| 1177   | No file  | `657601802240`  |
| 1173   | No file  | `657601802240`  |
| 1167   | No file  | `657601802240`  |
| 1164   | No file  | `657601802240`  |
| 1156   | No file  | `657601802240`  |
| 1149   | No file  | `657601802240`  |
| 1144   | No file  | `657601802240`  |
| 1137   | No file  | `657601802240`  |
| 1132   | No file  | `657601802240`  |
| 1127   | No file  | `657601802240`  |
| 1122   | No file  | `657601802240`  |
| 1118   | No file  | `657601802240`  |
| 1114   | No file  | `657601802240`  |
| 1109   | No file  | `657601802240`  |
| 1102   | No file  | `657601802240`  |
| 1096   | No file  | `657601802240`  |
| 1088   | No file  | `657601802240`  |
| 1081   | No file  | `657601802240`  |
| 1076   | No file  | `657601802240`  |
| 1069   | No file  | `657601802240`  |
| 1064   | No file  | `657601802240`  |
| 1058   | No file  | `657601802240`  |
| 1051   | No file  | `657601802240`  |
| 1044   | No file  | `657601802240`  |
| 1036   | No file  | `657601802240`  |
| 1026   | No file  | `657601802240`  |
| 1016   | No file  | `657601802240`  |
| 1009   | No file  | `657601802240`  |
| 1005   | No file  | `657601802240`  |
| 1000   | No file  | `657601802240`  |
| 998    | No file  | `657601802240`  |
| 990    | No file  | `657601802240`  |
| 979    | No file  | `657601802240`  |
| 972    | No file  | `657601802240`  |
| 963    | No file  | `657601802240`  |
| 955    | No file  | `657601802240`  |
| 946    | No file  | `657601802240`  |
| 938    | No file  | `657601802240`  |
| 927    | No file  | `657601802240`  |
| 911    | No file  | `657601802240`  |
| 904    | No file  | `657601802240`  |
| 899    | No file  | `657601802240`  |
| 894    | No file  | `657601802240`  |
| 885    | No file  | `657601802240`  |
| 879    | No file  | `657601802240`  |
| 872    | No file  | `657601802240`  |
| 864    | No file  | `657601802240`  |
| 855    | No file  | `657601802240`  |
| 853    | No file  | `657601802240`  |
| 845    | No file  | `657601802240`  |
| 837    | No file  | `657601802240`  |
| 829    | No file  | `657601802240`  |
| 822    | No file  | `657601802240`  |
| 814    | No file  | `657601802240`  |
| 805    | No file  | `657601802240`  |
| 794    | No file  | `657601802240`  |
| 787    | No file  | `657601802240`  |
| 780    | No file  | `657601802240`  |
| 771    | No file  | `657601802240`  |
| 760    | No file  | `657601802240`  |
| 748    | No file  | `657601802240`  |
| 741    | No file  | `657601802240`  |
| 736    | No file  | `657601802240`  |
| 731    | No file  | `657601802240`  |
| 723    | No file  | `657601802240`  |
| 711    | No file  | `657601802240`  |
| 707    | No file  | `657601802240`  |
| 697    | No file  | `657601802240`  |
| 689    | No file  | `657601802240`  |
| 683    | No file  | `657601802240`  |
| 678    | No file  | `657601802240`  |
| 670    | No file  | `657601802240`  |
| 661    | No file  | `657601802240`  |
| 656    | No file  | `657601802240`  |
| 652    | No file  | `657601802240`  |
| 643    | No file  | `657601802240`  |
| 637    | No file  | `657601802240`  |
| 630    | No file  | `657601802240`  |
| 627    | No file  | `657601802240`  |
| 621    | No file  | `657601802240`  |
| 617    | No file  | `657601802240`  |
| 615    | No file  | `657601802240`  |
| 606    | No file  | `657601802240`  |
| 599    | No file  | `657601802240`  |
| 592    | No file  | `657601802240`  |
| 586    | No file  | `657601802240`  |
| 577    | No file  | `657601802240`  |
| 569    | No file  | `657601802240`  |
| 561    | No file  | `657601802240`  |
| 554    | No file  | `657601802240`  |
| 542    | No file  | `657601802240`  |
| 532    | No file  | `657601802240`  |
| 531    | No file  | `657601802240`  |
| 526    | No file  | `657601802240`  |
| 521    | No file  | `657601802240`  |
| 517    | No file  | `657601802240`  |
| 510    | No file  | `657601802240`  |
| 508    | No file  | `657601802240`  |
| 504    | No file  | `657601802240`  |
| 497    | No file  | `657601802240`  |
| 491    | No file  | `657601802240`  |
| 485    | No file  | `657601802240`  |
| 478    | No file  | `657601802240`  |
| 472    | No file  | `657601802240`  |
| 466    | No file  | `657601802240`  |
| 457    | No file  | `657601802240`  |
| 452    | No file  | `657601802240`  |
| 449    | No file  | `657601802240`  |
| 435    | No file  | `657601802240`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                     |
| --------------------- | -------- | -------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6; region names, LOC type 17   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 8 bytes + region keys)

| Offset  | Type              | Field         | Notes                                                                     |
| ------- | ----------------- | ------------- | ------------------------------------------------------------------------- |
| `+0x00` | u16               | key           | Row key; equals `character_key` on every row                              |
| `+0x02` | u16               | character_key | `characterstatic.dbss` key of the boss; the handler shows its LOC type 6 name |
| `+0x04` | u32               | region_count  | Number of region keys, `1` to `5` (client 3474)                           |
| `+0x08` | u16[region_count] | region_keys   | `regioninfo.bss` keys, ascending; the handler shows their LOC type 17 names |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `WorldBossNonPkRegion` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `CharacterKey`, `RegionKey` (a list) and
`ContentsGroupKey` (`1` on every row). Its 17 character keys are the 17 rows
of the client 1784 file. Its region lists are the file's lists with region
877 (Garmoth's Nest) added to each, except Garmoth's own row, which lists
877 alone in both; the private server's compiled file has the same extra
877, so the sheet was edited after the client file was built. The file does
not store `ContentsGroupKey`. The private server's server executable logs
`WorldBossNonPkRegionStaticStatus::set() _key, key(%#)`, which names `key`.

## Notes

- The file grew from 17 rows (214 bytes, client 1784) to 35 (408 bytes,
  client 3474); clients 2107, 2519, 3002 and 3251 lie between.
- Several bosses share a region list: the three Isabella rows list Naga
  Marsh and Costa Farm, Vell (`23080`, `23162`) lists the three Margoria
  regions, Golden Pig King and Dark Bonghwang `28736` list Golden Pig Cave.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`.
  `test_pvp_tables.py` checks that `key` equals `character_key`.

## Open Questions

### Non-PK Rule

What the client does with the list. The sheet and file name say the regions
turn non-PK while the boss is up, but no client Lua reads the file, so the
rule is unconfirmed in game.
