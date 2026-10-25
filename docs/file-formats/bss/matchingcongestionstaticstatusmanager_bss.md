# `matchingcongestionstaticstatusmanager.bss` Format

## Purpose

Matching queue rows: a key counting from `0`, a byte and two numbers per
row. The name and the client Lua tie the file to the queue activity shown
on the Red Battlefield and Guild League matching buttons
(`ToClient_RequestMatchingCongestion`, `ToClient_GetMatchingCongestionString`,
`ToClient_GetMatchingCongestionCount`); which row belongs to which content
is not known. On client 3474 the file has 6 rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                        | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------------------------- | ----- | ------- | --------- |
| 1      | 3426 and later | `matchingcongestionstaticstatusmanager.bss` | 98    | 6 Row   | 13        |

| Layout | File                                        | Known        | Unknown      |
| ------ | ------------------------------------------- | ------------ | ------------ |
| 1      | `matchingcongestionstaticstatusmanager.bss` | 20 B (20.4%) | 78 B (79.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `020961545290`  |
| 3482   | Layout 1 | `020961545290`  |
| 3474   | Layout 1 | `020961545290`  |
| 3473   | Layout 1 | `020961545290`  |
| 3464   | Layout 1 | `020961545290`  |
| 3458   | Layout 1 | `020961545290`  |
| 3454   | Layout 1 | `020961545290`  |
| 3444   | Layout 1 | `020961545290`  |
| 3435   | Layout 1 | `020961545290`  |
| 3426   | Layout 1 | `020961545290`  |
| 3418   | No file  | `020961545290`  |
| 3412   | No file  | `020961545290`  |
| 3402   | No file  | `020961545290`  |
| 3396   | No file  | `020961545290`  |
| 3387   | No file  | `020961545290`  |
| 3381   | No file  | `020961545290`  |
| 3373   | No file  | `020961545290`  |
| 3364   | No file  | `020961545290`  |
| 3356   | No file  | `020961545290`  |
| 3349   | No file  | `020961545290`  |
| 3342   | No file  | `020961545290`  |
| 3335   | No file  | `020961545290`  |
| 3326   | No file  | `020961545290`  |
| 3321   | No file  | `020961545290`  |
| 3314   | No file  | `020961545290`  |
| 3303   | No file  | `020961545290`  |
| 3302   | No file  | `020961545290`  |
| 3293   | No file  | `020961545290`  |
| 3283   | No file  | `020961545290`  |
| 3275   | No file  | `020961545290`  |
| 3267   | No file  | `020961545290`  |
| 3258   | No file  | `020961545290`  |
| 3251   | No file  | `020961545290`  |
| 3242   | No file  | `020961545290`  |
| 3235   | No file  | `020961545290`  |
| 3229   | No file  | `020961545290`  |
| 3212   | No file  | `020961545290`  |
| 3203   | No file  | `020961545290`  |
| 3193   | No file  | `020961545290`  |
| 3186   | No file  | `020961545290`  |
| 3177   | No file  | `020961545290`  |
| 3169   | No file  | `020961545290`  |
| 3158   | No file  | `020961545290`  |
| 3151   | No file  | `020961545290`  |
| 3144   | No file  | `020961545290`  |
| 3133   | No file  | `020961545290`  |
| 3125   | No file  | `020961545290`  |
| 3118   | No file  | `020961545290`  |
| 3111   | No file  | `020961545290`  |
| 3103   | No file  | `020961545290`  |
| 3095   | No file  | `020961545290`  |
| 3086   | No file  | `020961545290`  |
| 3072   | No file  | `020961545290`  |
| 3062   | No file  | `020961545290`  |
| 3052   | No file  | `020961545290`  |
| 3045   | No file  | `020961545290`  |
| 3037   | No file  | `020961545290`  |
| 3030   | No file  | `020961545290`  |
| 3021   | No file  | `020961545290`  |
| 3012   | No file  | `020961545290`  |
| 3002   | No file  | `020961545290`  |
| 2995   | No file  | `020961545290`  |
| 2987   | No file  | `020961545290`  |
| 2978   | No file  | `020961545290`  |
| 2970   | No file  | `020961545290`  |
| 2959   | No file  | `020961545290`  |
| 2951   | No file  | `020961545290`  |
| 2942   | No file  | `020961545290`  |
| 2935   | No file  | `020961545290`  |
| 2932   | No file  | `020961545290`  |
| 2923   | No file  | `020961545290`  |
| 2919   | No file  | `020961545290`  |
| 2907   | No file  | `020961545290`  |
| 2900   | No file  | `020961545290`  |
| 2891   | No file  | `020961545290`  |
| 2882   | No file  | `020961545290`  |
| 2872   | No file  | `020961545290`  |
| 2863   | No file  | `020961545290`  |
| 2855   | No file  | `020961545290`  |
| 2849   | No file  | `020961545290`  |
| 2844   | No file  | `020961545290`  |
| 2834   | No file  | `020961545290`  |
| 2825   | No file  | `020961545290`  |
| 2819   | No file  | `020961545290`  |
| 2811   | No file  | `020961545290`  |
| 2803   | No file  | `020961545290`  |
| 2794   | No file  | `020961545290`  |
| 2783   | No file  | `020961545290`  |
| 2774   | No file  | `020961545290`  |
| 2765   | No file  | `020961545290`  |
| 2756   | No file  | `020961545290`  |
| 2750   | No file  | `020961545290`  |
| 2743   | No file  | `020961545290`  |
| 2736   | No file  | `020961545290`  |
| 2726   | No file  | `020961545290`  |
| 2717   | No file  | `020961545290`  |
| 2709   | No file  | `020961545290`  |
| 2703   | No file  | `020961545290`  |
| 2695   | No file  | `020961545290`  |
| 2684   | No file  | `020961545290`  |
| 2672   | No file  | `020961545290`  |
| 2665   | No file  | `020961545290`  |
| 2657   | No file  | `020961545290`  |
| 2649   | No file  | `020961545290`  |
| 2644   | No file  | `020961545290`  |
| 2637   | No file  | `020961545290`  |
| 2629   | No file  | `020961545290`  |
| 2619   | No file  | `020961545290`  |
| 2612   | No file  | `020961545290`  |
| 2606   | No file  | `020961545290`  |
| 2602   | No file  | `020961545290`  |
| 2601   | No file  | `020961545290`  |
| 2592   | No file  | `020961545290`  |
| 2583   | No file  | `020961545290`  |
| 2575   | No file  | `020961545290`  |
| 2567   | No file  | `020961545290`  |
| 2560   | No file  | `020961545290`  |
| 2553   | No file  | `020961545290`  |
| 2545   | No file  | `020961545290`  |
| 2538   | No file  | `020961545290`  |
| 2529   | No file  | `020961545290`  |
| 2519   | No file  | `020961545290`  |
| 2513   | No file  | `020961545290`  |
| 2510   | No file  | `020961545290`  |
| 2507   | No file  | `020961545290`  |
| 2503   | No file  | `020961545290`  |
| 2498   | No file  | `020961545290`  |
| 2492   | No file  | `020961545290`  |
| 2487   | No file  | `020961545290`  |
| 2480   | No file  | `020961545290`  |
| 2474   | No file  | `020961545290`  |
| 2468   | No file  | `020961545290`  |
| 2460   | No file  | `020961545290`  |
| 2453   | No file  | `020961545290`  |
| 2444   | No file  | `020961545290`  |
| 2438   | No file  | `020961545290`  |
| 2434   | No file  | `020961545290`  |
| 2429   | No file  | `020961545290`  |
| 2421   | No file  | `020961545290`  |
| 2414   | No file  | `020961545290`  |
| 2407   | No file  | `020961545290`  |
| 2401   | No file  | `020961545290`  |
| 2397   | No file  | `020961545290`  |
| 2393   | No file  | `020961545290`  |
| 2384   | No file  | `020961545290`  |
| 2378   | No file  | `020961545290`  |
| 2372   | No file  | `020961545290`  |
| 2358   | No file  | `020961545290`  |
| 2352   | No file  | `020961545290`  |
| 2347   | No file  | `020961545290`  |
| 2343   | No file  | `020961545290`  |
| 2335   | No file  | `020961545290`  |
| 2327   | No file  | `020961545290`  |
| 2324   | No file  | `020961545290`  |
| 2319   | No file  | `020961545290`  |
| 2313   | No file  | `020961545290`  |
| 2308   | No file  | `020961545290`  |
| 2302   | No file  | `020961545290`  |
| 2295   | No file  | `020961545290`  |
| 2290   | No file  | `020961545290`  |
| 2284   | No file  | `020961545290`  |
| 2276   | No file  | `020961545290`  |
| 2269   | No file  | `020961545290`  |
| 2259   | No file  | `020961545290`  |
| 2250   | No file  | `020961545290`  |
| 2243   | No file  | `020961545290`  |
| 2235   | No file  | `020961545290`  |
| 2229   | No file  | `020961545290`  |
| 2224   | No file  | `020961545290`  |
| 2218   | No file  | `020961545290`  |
| 2215   | No file  | `020961545290`  |
| 2207   | No file  | `020961545290`  |
| 2203   | No file  | `020961545290`  |
| 2196   | No file  | `020961545290`  |
| 2192   | No file  | `020961545290`  |
| 2189   | No file  | `020961545290`  |
| 2183   | No file  | `020961545290`  |
| 2179   | No file  | `020961545290`  |
| 2171   | No file  | `020961545290`  |
| 2163   | No file  | `020961545290`  |
| 2156   | No file  | `020961545290`  |
| 2151   | No file  | `020961545290`  |
| 2147   | No file  | `020961545290`  |
| 2142   | No file  | `020961545290`  |
| 2138   | No file  | `020961545290`  |
| 2134   | No file  | `020961545290`  |
| 2130   | No file  | `020961545290`  |
| 2122   | No file  | `020961545290`  |
| 2107   | No file  | `020961545290`  |
| 2098   | No file  | `020961545290`  |
| 2089   | No file  | `020961545290`  |
| 2081   | No file  | `020961545290`  |
| 2073   | No file  | `020961545290`  |
| 2067   | No file  | `020961545290`  |
| 2063   | No file  | `020961545290`  |
| 2059   | No file  | `020961545290`  |
| 2052   | No file  | `020961545290`  |
| 2044   | No file  | `020961545290`  |
| 2039   | No file  | `020961545290`  |
| 2032   | No file  | `020961545290`  |
| 2025   | No file  | `020961545290`  |
| 2011   | No file  | `020961545290`  |
| 2005   | No file  | `020961545290`  |
| 2000   | No file  | `020961545290`  |
| 1996   | No file  | `020961545290`  |
| 1991   | No file  | `020961545290`  |
| 1985   | No file  | `020961545290`  |
| 1980   | No file  | `020961545290`  |
| 1969   | No file  | `020961545290`  |
| 1964   | No file  | `020961545290`  |
| 1958   | No file  | `020961545290`  |
| 1950   | No file  | `020961545290`  |
| 1945   | No file  | `020961545290`  |
| 1937   | No file  | `020961545290`  |
| 1933   | No file  | `020961545290`  |
| 1927   | No file  | `020961545290`  |
| 1921   | No file  | `020961545290`  |
| 1914   | No file  | `020961545290`  |
| 1908   | No file  | `020961545290`  |
| 1897   | No file  | `020961545290`  |
| 1892   | No file  | `020961545290`  |
| 1886   | No file  | `020961545290`  |
| 1881   | No file  | `020961545290`  |
| 1871   | No file  | `020961545290`  |
| 1866   | No file  | `020961545290`  |
| 1862   | No file  | `020961545290`  |
| 1854   | No file  | `020961545290`  |
| 1846   | No file  | `020961545290`  |
| 1838   | No file  | `020961545290`  |
| 1832   | No file  | `020961545290`  |
| 1826   | No file  | `020961545290`  |
| 1822   | No file  | `020961545290`  |
| 1818   | No file  | `020961545290`  |
| 1804   | No file  | `020961545290`  |
| 1794   | No file  | `020961545290`  |
| 1790   | No file  | `020961545290`  |
| 1784   | No file  | `020961545290`  |
| 1774   | No file  | `020961545290`  |
| 1771   | No file  | `020961545290`  |
| 1762   | No file  | `020961545290`  |
| 1759   | No file  | `020961545290`  |
| 1754   | No file  | `020961545290`  |
| 1749   | No file  | `020961545290`  |
| 1743   | No file  | `020961545290`  |
| 1737   | No file  | `020961545290`  |
| 1731   | No file  | `020961545290`  |
| 1725   | No file  | `020961545290`  |
| 1717   | No file  | `020961545290`  |
| 1710   | No file  | `020961545290`  |
| 1704   | No file  | `020961545290`  |
| 1698   | No file  | `020961545290`  |
| 1690   | No file  | `020961545290`  |
| 1685   | No file  | `020961545290`  |
| 1680   | No file  | `020961545290`  |
| 1674   | No file  | `020961545290`  |
| 1668   | No file  | `020961545290`  |
| 1659   | No file  | `020961545290`  |
| 1649   | No file  | `020961545290`  |
| 1642   | No file  | `020961545290`  |
| 1636   | No file  | `020961545290`  |
| 1628   | No file  | `020961545290`  |
| 1622   | No file  | `020961545290`  |
| 1614   | No file  | `020961545290`  |
| 1608   | No file  | `020961545290`  |
| 1602   | No file  | `020961545290`  |
| 1598   | No file  | `020961545290`  |
| 1594   | No file  | `020961545290`  |
| 1590   | No file  | `020961545290`  |
| 1587   | No file  | `020961545290`  |
| 1584   | No file  | `020961545290`  |
| 1579   | No file  | `020961545290`  |
| 1572   | No file  | `020961545290`  |
| 1565   | No file  | `020961545290`  |
| 1559   | No file  | `020961545290`  |
| 1554   | No file  | `020961545290`  |
| 1547   | No file  | `020961545290`  |
| 1537   | No file  | `020961545290`  |
| 1529   | No file  | `020961545290`  |
| 1524   | No file  | `020961545290`  |
| 1519   | No file  | `020961545290`  |
| 1509   | No file  | `020961545290`  |
| 1506   | No file  | `020961545290`  |
| 1504   | No file  | `020961545290`  |
| 1500   | No file  | `020961545290`  |
| 1493   | No file  | `020961545290`  |
| 1489   | No file  | `020961545290`  |
| 1485   | No file  | `020961545290`  |
| 1481   | No file  | `020961545290`  |
| 1474   | No file  | `020961545290`  |
| 1466   | No file  | `020961545290`  |
| 1462   | No file  | `020961545290`  |
| 1459   | No file  | `020961545290`  |
| 1453   | No file  | `020961545290`  |
| 1450   | No file  | `020961545290`  |
| 1445   | No file  | `020961545290`  |
| 1439   | No file  | `020961545290`  |
| 1433   | No file  | `020961545290`  |
| 1430   | No file  | `020961545290`  |
| 1426   | No file  | `020961545290`  |
| 1421   | No file  | `020961545290`  |
| 1417   | No file  | `020961545290`  |
| 1416   | No file  | `020961545290`  |
| 1409   | No file  | `020961545290`  |
| 1405   | No file  | `020961545290`  |
| 1401   | No file  | `020961545290`  |
| 1396   | No file  | `020961545290`  |
| 1391   | No file  | `020961545290`  |
| 1390   | No file  | `020961545290`  |
| 1386   | No file  | `020961545290`  |
| 1381   | No file  | `020961545290`  |
| 1379   | No file  | `020961545290`  |
| 1372   | No file  | `020961545290`  |
| 1366   | No file  | `020961545290`  |
| 1364   | No file  | `020961545290`  |
| 1363   | No file  | `020961545290`  |
| 1360   | No file  | `020961545290`  |
| 1358   | No file  | `020961545290`  |
| 1355   | No file  | `020961545290`  |
| 1351   | No file  | `020961545290`  |
| 1348   | No file  | `020961545290`  |
| 1346   | No file  | `020961545290`  |
| 1341   | No file  | `020961545290`  |
| 1340   | No file  | `020961545290`  |
| 1338   | No file  | `020961545290`  |
| 1335   | No file  | `020961545290`  |
| 1333   | No file  | `020961545290`  |
| 1329   | No file  | `020961545290`  |
| 1327   | No file  | `020961545290`  |
| 1324   | No file  | `020961545290`  |
| 1321   | No file  | `020961545290`  |
| 1319   | No file  | `020961545290`  |
| 1318   | No file  | `020961545290`  |
| 1316   | No file  | `020961545290`  |
| 1313   | No file  | `020961545290`  |
| 1311   | No file  | `020961545290`  |
| 1309   | No file  | `020961545290`  |
| 1304   | No file  | `020961545290`  |
| 1292   | No file  | `020961545290`  |
| 1286   | No file  | `020961545290`  |
| 1280   | No file  | `020961545290`  |
| 1276   | No file  | `020961545290`  |
| 1267   | No file  | `020961545290`  |
| 1261   | No file  | `020961545290`  |
| 1256   | No file  | `020961545290`  |
| 1250   | No file  | `020961545290`  |
| 1246   | No file  | `020961545290`  |
| 1239   | No file  | `020961545290`  |
| 1230   | No file  | `020961545290`  |
| 1226   | No file  | `020961545290`  |
| 1220   | No file  | `020961545290`  |
| 1217   | No file  | `020961545290`  |
| 1211   | No file  | `020961545290`  |
| 1210   | No file  | `020961545290`  |
| 1208   | No file  | `020961545290`  |
| 1203   | No file  | `020961545290`  |
| 1197   | No file  | `020961545290`  |
| 1194   | No file  | `020961545290`  |
| 1192   | No file  | `020961545290`  |
| 1187   | No file  | `020961545290`  |
| 1183   | No file  | `020961545290`  |
| 1177   | No file  | `020961545290`  |
| 1173   | No file  | `020961545290`  |
| 1167   | No file  | `020961545290`  |
| 1164   | No file  | `020961545290`  |
| 1156   | No file  | `020961545290`  |
| 1149   | No file  | `020961545290`  |
| 1144   | No file  | `020961545290`  |
| 1137   | No file  | `020961545290`  |
| 1132   | No file  | `020961545290`  |
| 1127   | No file  | `020961545290`  |
| 1122   | No file  | `020961545290`  |
| 1118   | No file  | `020961545290`  |
| 1114   | No file  | `020961545290`  |
| 1109   | No file  | `020961545290`  |
| 1102   | No file  | `020961545290`  |
| 1096   | No file  | `020961545290`  |
| 1088   | No file  | `020961545290`  |
| 1081   | No file  | `020961545290`  |
| 1076   | No file  | `020961545290`  |
| 1069   | No file  | `020961545290`  |
| 1064   | No file  | `020961545290`  |
| 1058   | No file  | `020961545290`  |
| 1051   | No file  | `020961545290`  |
| 1044   | No file  | `020961545290`  |
| 1036   | No file  | `020961545290`  |
| 1026   | No file  | `020961545290`  |
| 1016   | No file  | `020961545290`  |
| 1009   | No file  | `020961545290`  |
| 1005   | No file  | `020961545290`  |
| 1000   | No file  | `020961545290`  |
| 998    | No file  | `020961545290`  |
| 990    | No file  | `020961545290`  |
| 979    | No file  | `020961545290`  |
| 972    | No file  | `020961545290`  |
| 963    | No file  | `020961545290`  |
| 955    | No file  | `020961545290`  |
| 946    | No file  | `020961545290`  |
| 938    | No file  | `020961545290`  |
| 927    | No file  | `020961545290`  |
| 911    | No file  | `020961545290`  |
| 904    | No file  | `020961545290`  |
| 899    | No file  | `020961545290`  |
| 894    | No file  | `020961545290`  |
| 885    | No file  | `020961545290`  |
| 879    | No file  | `020961545290`  |
| 872    | No file  | `020961545290`  |
| 864    | No file  | `020961545290`  |
| 855    | No file  | `020961545290`  |
| 853    | No file  | `020961545290`  |
| 845    | No file  | `020961545290`  |
| 837    | No file  | `020961545290`  |
| 829    | No file  | `020961545290`  |
| 822    | No file  | `020961545290`  |
| 814    | No file  | `020961545290`  |
| 805    | No file  | `020961545290`  |
| 794    | No file  | `020961545290`  |
| 787    | No file  | `020961545290`  |
| 780    | No file  | `020961545290`  |
| 771    | No file  | `020961545290`  |
| 760    | No file  | `020961545290`  |
| 748    | No file  | `020961545290`  |
| 741    | No file  | `020961545290`  |
| 736    | No file  | `020961545290`  |
| 731    | No file  | `020961545290`  |
| 723    | No file  | `020961545290`  |
| 711    | No file  | `020961545290`  |
| 707    | No file  | `020961545290`  |
| 697    | No file  | `020961545290`  |
| 689    | No file  | `020961545290`  |
| 683    | No file  | `020961545290`  |
| 678    | No file  | `020961545290`  |
| 670    | No file  | `020961545290`  |
| 661    | No file  | `020961545290`  |
| 656    | No file  | `020961545290`  |
| 652    | No file  | `020961545290`  |
| 643    | No file  | `020961545290`  |
| 637    | No file  | `020961545290`  |
| 630    | No file  | `020961545290`  |
| 627    | No file  | `020961545290`  |
| 621    | No file  | `020961545290`  |
| 617    | No file  | `020961545290`  |
| 615    | No file  | `020961545290`  |
| 606    | No file  | `020961545290`  |
| 599    | No file  | `020961545290`  |
| 592    | No file  | `020961545290`  |
| 586    | No file  | `020961545290`  |
| 577    | No file  | `020961545290`  |
| 569    | No file  | `020961545290`  |
| 561    | No file  | `020961545290`  |
| 554    | No file  | `020961545290`  |
| 542    | No file  | `020961545290`  |
| 532    | No file  | `020961545290`  |
| 531    | No file  | `020961545290`  |
| 526    | No file  | `020961545290`  |
| 521    | No file  | `020961545290`  |
| 517    | No file  | `020961545290`  |
| 510    | No file  | `020961545290`  |
| 508    | No file  | `020961545290`  |
| 504    | No file  | `020961545290`  |
| 497    | No file  | `020961545290`  |
| 491    | No file  | `020961545290`  |
| 485    | No file  | `020961545290`  |
| 478    | No file  | `020961545290`  |
| 472    | No file  | `020961545290`  |
| 466    | No file  | `020961545290`  |
| 457    | No file  | `020961545290`  |
| 452    | No file  | `020961545290`  |
| 449    | No file  | `020961545290`  |
| 435    | No file  | `020961545290`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (13 bytes)

| Offset  | Type | Field      | Notes                                                                   |
| ------- | ---- | ---------- | ----------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00 | `0` to `5` in row order (client 3474); see Open Questions               |
| `+0x04` | u8   | unknown_04 | `0` on every row                                                        |
| `+0x05` | u32  | unknown_05 | `2`, `15`, `15`, `1`, `2`, `1` by row (client 3474)                     |
| `+0x09` | u32  | unknown_09 | `4`, `29`, `29`, `2`, `3`, `2` by row; above `unknown_05` on every row  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3474          |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 covers
the file, which clients 1784 to 3251 do not ship. The client Lua names two
members of the enum the queue calls take, `__eMatchingContentsType_GuildMatch`
and `__eMatchingContentsType_RedBattleField`, without their values, so no
field is named yet.

## Notes

- The file is 98 bytes on client 3474, the only client checked that ships
  it.
- The Lua asks for a fresh queue count every 30 seconds
  (`_matchingCongestionTime > 30` in `panel_guildmatch_all` and
  `panel_redbattlefieldinfo_all`) and passes `0` to
  `ToClient_GetMatchingCongestionString` and `...Count`.
- With no named field, the handler for the PABR option tables
  (`_bss/pabr_values/`) shows each row's bytes, with the shared layout
  table in `_bss/pabr_values/pvp_tables.py`. `test_pvp_tables.py` checks
  that `unknown_00` counts up from `0`.

## Open Questions

### Row Key and Thresholds

Whether `unknown_00` is the `__eMatchingContentsType_*` value of a matching
content and `unknown_05` and `unknown_09` the queue counts at which the
queue text changes from one activity level to the next. Each row's
`unknown_09` is above its `unknown_05`, which fits two rising thresholds;
the enum values are not in the Lua.
