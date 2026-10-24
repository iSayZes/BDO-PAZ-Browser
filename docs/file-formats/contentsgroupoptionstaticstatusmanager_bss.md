# `contentsgroupoptionstaticstatusmanager.bss` Format

## Purpose

The contents group switches of the client's service: which feature groups
are open. A contents group is a decimal key string such as `"330"`, the
argument of the client Lua's `ToClient_IsContentsGroupOpen("330")`. The file
holds the sorted key hashes of the open groups, then every group key the
client knows with its hash. On client 3474 that is 1,492 open groups out of
2,463, keys `0` to `10043`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                         | Bytes  | Records     | Row bytes               |
| ------ | -------------- | ------- | -------------------------------------------- | ------ | ----------- | ----------------------- |
| 1      | 3062 and later | 3483    | `contentsgroupoptionstaticstatusmanager.bss` | 53,056 | 2,463 Group | 14 to 22, 19 on average |

| Layout | File                                         | Known             | Unknown    |
| ------ | -------------------------------------------- | ----------------- | ---------- |
| 1      | `contentsgroupoptionstaticstatusmanager.bss` | 53,056 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `958046f8abc5`  |
| 3482   | Layout 1 | `958046f8abc5`  |
| 3474   | Layout 1 | `958046f8abc5`  |
| 3473   | Layout 1 | `958046f8abc5`  |
| 3464   | Layout 1 | `958046f8abc5`  |
| 3458   | Layout 1 | `958046f8abc5`  |
| 3454   | Layout 1 | `958046f8abc5`  |
| 3444   | Layout 1 | `958046f8abc5`  |
| 3435   | Layout 1 | `958046f8abc5`  |
| 3426   | Layout 1 | `958046f8abc5`  |
| 3418   | Layout 1 | `958046f8abc5`  |
| 3412   | Layout 1 | `958046f8abc5`  |
| 3402   | Layout 1 | `958046f8abc5`  |
| 3396   | Layout 1 | `958046f8abc5`  |
| 3387   | Layout 1 | `958046f8abc5`  |
| 3381   | Layout 1 | `958046f8abc5`  |
| 3373   | Layout 1 | `958046f8abc5`  |
| 3364   | Layout 1 | `958046f8abc5`  |
| 3356   | Layout 1 | `958046f8abc5`  |
| 3349   | Layout 1 | `958046f8abc5`  |
| 3342   | Layout 1 | `958046f8abc5`  |
| 3335   | Layout 1 | `958046f8abc5`  |
| 3326   | Layout 1 | `958046f8abc5`  |
| 3321   | Layout 1 | `958046f8abc5`  |
| 3314   | Layout 1 | `958046f8abc5`  |
| 3303   | Layout 1 | `958046f8abc5`  |
| 3302   | Layout 1 | `958046f8abc5`  |
| 3293   | Layout 1 | `958046f8abc5`  |
| 3283   | Layout 1 | `958046f8abc5`  |
| 3275   | Layout 1 | `958046f8abc5`  |
| 3267   | Layout 1 | `958046f8abc5`  |
| 3258   | Layout 1 | `958046f8abc5`  |
| 3251   | Layout 1 | `958046f8abc5`  |
| 3242   | Layout 1 | `958046f8abc5`  |
| 3235   | Layout 1 | `958046f8abc5`  |
| 3229   | Layout 1 | `958046f8abc5`  |
| 3212   | Layout 1 | `958046f8abc5`  |
| 3203   | Layout 1 | `958046f8abc5`  |
| 3193   | Layout 1 | `958046f8abc5`  |
| 3186   | Layout 1 | `958046f8abc5`  |
| 3177   | Layout 1 | `958046f8abc5`  |
| 3169   | Layout 1 | `958046f8abc5`  |
| 3158   | Layout 1 | `958046f8abc5`  |
| 3151   | Layout 1 | `958046f8abc5`  |
| 3144   | Layout 1 | `958046f8abc5`  |
| 3133   | Layout 1 | `958046f8abc5`  |
| 3125   | Layout 1 | `958046f8abc5`  |
| 3118   | Layout 1 | `958046f8abc5`  |
| 3111   | Layout 1 | `958046f8abc5`  |
| 3103   | Layout 1 | `958046f8abc5`  |
| 3095   | Layout 1 | `958046f8abc5`  |
| 3086   | Layout 1 | `958046f8abc5`  |
| 3072   | Layout 1 | `958046f8abc5`  |
| 3062   | Layout 1 | `958046f8abc5`  |
| 3052   | No file  | `958046f8abc5`  |
| 3045   | No file  | `958046f8abc5`  |
| 3037   | No file  | `958046f8abc5`  |
| 3030   | No file  | `958046f8abc5`  |
| 3021   | No file  | `958046f8abc5`  |
| 3012   | No file  | `958046f8abc5`  |
| 3002   | No file  | `958046f8abc5`  |
| 2995   | No file  | `958046f8abc5`  |
| 2987   | No file  | `958046f8abc5`  |
| 2978   | No file  | `958046f8abc5`  |
| 2970   | No file  | `958046f8abc5`  |
| 2959   | No file  | `958046f8abc5`  |
| 2951   | No file  | `958046f8abc5`  |
| 2942   | No file  | `958046f8abc5`  |
| 2935   | No file  | `958046f8abc5`  |
| 2932   | No file  | `958046f8abc5`  |
| 2923   | No file  | `958046f8abc5`  |
| 2919   | No file  | `958046f8abc5`  |
| 2907   | No file  | `958046f8abc5`  |
| 2900   | No file  | `958046f8abc5`  |
| 2891   | No file  | `958046f8abc5`  |
| 2882   | No file  | `958046f8abc5`  |
| 2872   | No file  | `958046f8abc5`  |
| 2863   | No file  | `958046f8abc5`  |
| 2855   | No file  | `958046f8abc5`  |
| 2849   | No file  | `958046f8abc5`  |
| 2844   | No file  | `958046f8abc5`  |
| 2834   | No file  | `958046f8abc5`  |
| 2825   | No file  | `958046f8abc5`  |
| 2819   | No file  | `958046f8abc5`  |
| 2811   | No file  | `958046f8abc5`  |
| 2803   | No file  | `958046f8abc5`  |
| 2794   | No file  | `958046f8abc5`  |
| 2783   | No file  | `958046f8abc5`  |
| 2774   | No file  | `958046f8abc5`  |
| 2765   | No file  | `958046f8abc5`  |
| 2756   | No file  | `958046f8abc5`  |
| 2750   | No file  | `958046f8abc5`  |
| 2743   | No file  | `958046f8abc5`  |
| 2736   | No file  | `958046f8abc5`  |
| 2726   | No file  | `958046f8abc5`  |
| 2717   | No file  | `958046f8abc5`  |
| 2709   | No file  | `958046f8abc5`  |
| 2703   | No file  | `958046f8abc5`  |
| 2695   | No file  | `958046f8abc5`  |
| 2684   | No file  | `958046f8abc5`  |
| 2672   | No file  | `958046f8abc5`  |
| 2665   | No file  | `958046f8abc5`  |
| 2657   | No file  | `958046f8abc5`  |
| 2649   | No file  | `958046f8abc5`  |
| 2644   | No file  | `958046f8abc5`  |
| 2637   | No file  | `958046f8abc5`  |
| 2629   | No file  | `958046f8abc5`  |
| 2619   | No file  | `958046f8abc5`  |
| 2612   | No file  | `958046f8abc5`  |
| 2606   | No file  | `958046f8abc5`  |
| 2602   | No file  | `958046f8abc5`  |
| 2601   | No file  | `958046f8abc5`  |
| 2592   | No file  | `958046f8abc5`  |
| 2583   | No file  | `958046f8abc5`  |
| 2575   | No file  | `958046f8abc5`  |
| 2567   | No file  | `958046f8abc5`  |
| 2560   | No file  | `958046f8abc5`  |
| 2553   | No file  | `958046f8abc5`  |
| 2545   | No file  | `958046f8abc5`  |
| 2538   | No file  | `958046f8abc5`  |
| 2529   | No file  | `958046f8abc5`  |
| 2519   | No file  | `958046f8abc5`  |
| 2513   | No file  | `958046f8abc5`  |
| 2510   | No file  | `958046f8abc5`  |
| 2507   | No file  | `958046f8abc5`  |
| 2503   | No file  | `958046f8abc5`  |
| 2498   | No file  | `958046f8abc5`  |
| 2492   | No file  | `958046f8abc5`  |
| 2487   | No file  | `958046f8abc5`  |
| 2480   | No file  | `958046f8abc5`  |
| 2474   | No file  | `958046f8abc5`  |
| 2468   | No file  | `958046f8abc5`  |
| 2460   | No file  | `958046f8abc5`  |
| 2453   | No file  | `958046f8abc5`  |
| 2444   | No file  | `958046f8abc5`  |
| 2438   | No file  | `958046f8abc5`  |
| 2434   | No file  | `958046f8abc5`  |
| 2429   | No file  | `958046f8abc5`  |
| 2421   | No file  | `958046f8abc5`  |
| 2414   | No file  | `958046f8abc5`  |
| 2407   | No file  | `958046f8abc5`  |
| 2401   | No file  | `958046f8abc5`  |
| 2397   | No file  | `958046f8abc5`  |
| 2393   | No file  | `958046f8abc5`  |
| 2384   | No file  | `958046f8abc5`  |
| 2378   | No file  | `958046f8abc5`  |
| 2372   | No file  | `958046f8abc5`  |
| 2358   | No file  | `958046f8abc5`  |
| 2352   | No file  | `958046f8abc5`  |
| 2347   | No file  | `958046f8abc5`  |
| 2343   | No file  | `958046f8abc5`  |
| 2335   | No file  | `958046f8abc5`  |
| 2327   | No file  | `958046f8abc5`  |
| 2324   | No file  | `958046f8abc5`  |
| 2319   | No file  | `958046f8abc5`  |
| 2313   | No file  | `958046f8abc5`  |
| 2308   | No file  | `958046f8abc5`  |
| 2302   | No file  | `958046f8abc5`  |
| 2295   | No file  | `958046f8abc5`  |
| 2290   | No file  | `958046f8abc5`  |
| 2284   | No file  | `958046f8abc5`  |
| 2276   | No file  | `958046f8abc5`  |
| 2269   | No file  | `958046f8abc5`  |
| 2259   | No file  | `958046f8abc5`  |
| 2250   | No file  | `958046f8abc5`  |
| 2243   | No file  | `958046f8abc5`  |
| 2235   | No file  | `958046f8abc5`  |
| 2229   | No file  | `958046f8abc5`  |
| 2224   | No file  | `958046f8abc5`  |
| 2218   | No file  | `958046f8abc5`  |
| 2215   | No file  | `958046f8abc5`  |
| 2207   | No file  | `958046f8abc5`  |
| 2203   | No file  | `958046f8abc5`  |
| 2196   | No file  | `958046f8abc5`  |
| 2192   | No file  | `958046f8abc5`  |
| 2189   | No file  | `958046f8abc5`  |
| 2183   | No file  | `958046f8abc5`  |
| 2179   | No file  | `958046f8abc5`  |
| 2171   | No file  | `958046f8abc5`  |
| 2163   | No file  | `958046f8abc5`  |
| 2156   | No file  | `958046f8abc5`  |
| 2151   | No file  | `958046f8abc5`  |
| 2147   | No file  | `958046f8abc5`  |
| 2142   | No file  | `958046f8abc5`  |
| 2138   | No file  | `958046f8abc5`  |
| 2134   | No file  | `958046f8abc5`  |
| 2130   | No file  | `958046f8abc5`  |
| 2122   | No file  | `958046f8abc5`  |
| 2107   | No file  | `958046f8abc5`  |
| 2098   | No file  | `958046f8abc5`  |
| 2089   | No file  | `958046f8abc5`  |
| 2081   | No file  | `958046f8abc5`  |
| 2073   | No file  | `958046f8abc5`  |
| 2067   | No file  | `958046f8abc5`  |
| 2063   | No file  | `958046f8abc5`  |
| 2059   | No file  | `958046f8abc5`  |
| 2052   | No file  | `958046f8abc5`  |
| 2044   | No file  | `958046f8abc5`  |
| 2039   | No file  | `958046f8abc5`  |
| 2032   | No file  | `958046f8abc5`  |
| 2025   | No file  | `958046f8abc5`  |
| 2011   | No file  | `958046f8abc5`  |
| 2005   | No file  | `958046f8abc5`  |
| 2000   | No file  | `958046f8abc5`  |
| 1996   | No file  | `958046f8abc5`  |
| 1991   | No file  | `958046f8abc5`  |
| 1985   | No file  | `958046f8abc5`  |
| 1980   | No file  | `958046f8abc5`  |
| 1969   | No file  | `958046f8abc5`  |
| 1964   | No file  | `958046f8abc5`  |
| 1958   | No file  | `958046f8abc5`  |
| 1950   | No file  | `958046f8abc5`  |
| 1945   | No file  | `958046f8abc5`  |
| 1937   | No file  | `958046f8abc5`  |
| 1933   | No file  | `958046f8abc5`  |
| 1927   | No file  | `958046f8abc5`  |
| 1921   | No file  | `958046f8abc5`  |
| 1914   | No file  | `958046f8abc5`  |
| 1908   | No file  | `958046f8abc5`  |
| 1897   | No file  | `958046f8abc5`  |
| 1892   | No file  | `958046f8abc5`  |
| 1886   | No file  | `958046f8abc5`  |
| 1881   | No file  | `958046f8abc5`  |
| 1871   | No file  | `958046f8abc5`  |
| 1866   | No file  | `958046f8abc5`  |
| 1862   | No file  | `958046f8abc5`  |
| 1854   | No file  | `958046f8abc5`  |
| 1846   | No file  | `958046f8abc5`  |
| 1838   | No file  | `958046f8abc5`  |
| 1832   | No file  | `958046f8abc5`  |
| 1826   | No file  | `958046f8abc5`  |
| 1822   | No file  | `958046f8abc5`  |
| 1818   | No file  | `958046f8abc5`  |
| 1804   | No file  | `958046f8abc5`  |
| 1794   | No file  | `958046f8abc5`  |
| 1790   | No file  | `958046f8abc5`  |
| 1784   | No file  | `958046f8abc5`  |
| 1774   | No file  | `958046f8abc5`  |
| 1771   | No file  | `958046f8abc5`  |
| 1762   | No file  | `958046f8abc5`  |
| 1759   | No file  | `958046f8abc5`  |
| 1754   | No file  | `958046f8abc5`  |
| 1749   | No file  | `958046f8abc5`  |
| 1743   | No file  | `958046f8abc5`  |
| 1737   | No file  | `958046f8abc5`  |
| 1731   | No file  | `958046f8abc5`  |
| 1725   | No file  | `958046f8abc5`  |
| 1717   | No file  | `958046f8abc5`  |
| 1710   | No file  | `958046f8abc5`  |
| 1704   | No file  | `958046f8abc5`  |
| 1698   | No file  | `958046f8abc5`  |
| 1690   | No file  | `958046f8abc5`  |
| 1685   | No file  | `958046f8abc5`  |
| 1680   | No file  | `958046f8abc5`  |
| 1674   | No file  | `958046f8abc5`  |
| 1668   | No file  | `958046f8abc5`  |
| 1659   | No file  | `958046f8abc5`  |
| 1649   | No file  | `958046f8abc5`  |
| 1642   | No file  | `958046f8abc5`  |
| 1636   | No file  | `958046f8abc5`  |
| 1628   | No file  | `958046f8abc5`  |
| 1622   | No file  | `958046f8abc5`  |
| 1614   | No file  | `958046f8abc5`  |
| 1608   | No file  | `958046f8abc5`  |
| 1602   | No file  | `958046f8abc5`  |
| 1598   | No file  | `958046f8abc5`  |
| 1594   | No file  | `958046f8abc5`  |
| 1590   | No file  | `958046f8abc5`  |
| 1587   | No file  | `958046f8abc5`  |
| 1584   | No file  | `958046f8abc5`  |
| 1579   | No file  | `958046f8abc5`  |
| 1572   | No file  | `958046f8abc5`  |
| 1565   | No file  | `958046f8abc5`  |
| 1559   | No file  | `958046f8abc5`  |
| 1554   | No file  | `958046f8abc5`  |
| 1547   | No file  | `958046f8abc5`  |
| 1537   | No file  | `958046f8abc5`  |
| 1529   | No file  | `958046f8abc5`  |
| 1524   | No file  | `958046f8abc5`  |
| 1519   | No file  | `958046f8abc5`  |
| 1509   | No file  | `958046f8abc5`  |
| 1506   | No file  | `958046f8abc5`  |
| 1504   | No file  | `958046f8abc5`  |
| 1500   | No file  | `958046f8abc5`  |
| 1493   | No file  | `958046f8abc5`  |
| 1489   | No file  | `958046f8abc5`  |
| 1485   | No file  | `958046f8abc5`  |
| 1481   | No file  | `958046f8abc5`  |
| 1474   | No file  | `958046f8abc5`  |
| 1466   | No file  | `958046f8abc5`  |
| 1462   | No file  | `958046f8abc5`  |
| 1459   | No file  | `958046f8abc5`  |
| 1453   | No file  | `958046f8abc5`  |
| 1450   | No file  | `958046f8abc5`  |
| 1445   | No file  | `958046f8abc5`  |
| 1439   | No file  | `958046f8abc5`  |
| 1433   | No file  | `958046f8abc5`  |
| 1430   | No file  | `958046f8abc5`  |
| 1426   | No file  | `958046f8abc5`  |
| 1421   | No file  | `958046f8abc5`  |
| 1417   | No file  | `958046f8abc5`  |
| 1416   | No file  | `958046f8abc5`  |
| 1409   | No file  | `958046f8abc5`  |
| 1405   | No file  | `958046f8abc5`  |
| 1401   | No file  | `958046f8abc5`  |
| 1396   | No file  | `958046f8abc5`  |
| 1391   | No file  | `958046f8abc5`  |
| 1390   | No file  | `958046f8abc5`  |
| 1386   | No file  | `958046f8abc5`  |
| 1381   | No file  | `958046f8abc5`  |
| 1379   | No file  | `958046f8abc5`  |
| 1372   | No file  | `958046f8abc5`  |
| 1366   | No file  | `958046f8abc5`  |
| 1364   | No file  | `958046f8abc5`  |
| 1363   | No file  | `958046f8abc5`  |
| 1360   | No file  | `958046f8abc5`  |
| 1358   | No file  | `958046f8abc5`  |
| 1355   | No file  | `958046f8abc5`  |
| 1351   | No file  | `958046f8abc5`  |
| 1348   | No file  | `958046f8abc5`  |
| 1346   | No file  | `958046f8abc5`  |
| 1341   | No file  | `958046f8abc5`  |
| 1340   | No file  | `958046f8abc5`  |
| 1338   | No file  | `958046f8abc5`  |
| 1335   | No file  | `958046f8abc5`  |
| 1333   | No file  | `958046f8abc5`  |
| 1329   | No file  | `958046f8abc5`  |
| 1327   | No file  | `958046f8abc5`  |
| 1324   | No file  | `958046f8abc5`  |
| 1321   | No file  | `958046f8abc5`  |
| 1319   | No file  | `958046f8abc5`  |
| 1318   | No file  | `958046f8abc5`  |
| 1316   | No file  | `958046f8abc5`  |
| 1313   | No file  | `958046f8abc5`  |
| 1311   | No file  | `958046f8abc5`  |
| 1309   | No file  | `958046f8abc5`  |
| 1304   | No file  | `958046f8abc5`  |
| 1292   | No file  | `958046f8abc5`  |
| 1286   | No file  | `958046f8abc5`  |
| 1280   | No file  | `958046f8abc5`  |
| 1276   | No file  | `958046f8abc5`  |
| 1267   | No file  | `958046f8abc5`  |
| 1261   | No file  | `958046f8abc5`  |
| 1256   | No file  | `958046f8abc5`  |
| 1250   | No file  | `958046f8abc5`  |
| 1246   | No file  | `958046f8abc5`  |
| 1239   | No file  | `958046f8abc5`  |
| 1230   | No file  | `958046f8abc5`  |
| 1226   | No file  | `958046f8abc5`  |
| 1220   | No file  | `958046f8abc5`  |
| 1217   | No file  | `958046f8abc5`  |
| 1211   | No file  | `958046f8abc5`  |
| 1210   | No file  | `958046f8abc5`  |
| 1208   | No file  | `958046f8abc5`  |
| 1203   | No file  | `958046f8abc5`  |
| 1197   | No file  | `958046f8abc5`  |
| 1194   | No file  | `958046f8abc5`  |
| 1192   | No file  | `958046f8abc5`  |
| 1187   | No file  | `958046f8abc5`  |
| 1183   | No file  | `958046f8abc5`  |
| 1177   | No file  | `958046f8abc5`  |
| 1173   | No file  | `958046f8abc5`  |
| 1167   | No file  | `958046f8abc5`  |
| 1164   | No file  | `958046f8abc5`  |
| 1156   | No file  | `958046f8abc5`  |
| 1149   | No file  | `958046f8abc5`  |
| 1144   | No file  | `958046f8abc5`  |
| 1137   | No file  | `958046f8abc5`  |
| 1132   | No file  | `958046f8abc5`  |
| 1127   | No file  | `958046f8abc5`  |
| 1122   | No file  | `958046f8abc5`  |
| 1118   | No file  | `958046f8abc5`  |
| 1114   | No file  | `958046f8abc5`  |
| 1109   | No file  | `958046f8abc5`  |
| 1102   | No file  | `958046f8abc5`  |
| 1096   | No file  | `958046f8abc5`  |
| 1088   | No file  | `958046f8abc5`  |
| 1081   | No file  | `958046f8abc5`  |
| 1076   | No file  | `958046f8abc5`  |
| 1069   | No file  | `958046f8abc5`  |
| 1064   | No file  | `958046f8abc5`  |
| 1058   | No file  | `958046f8abc5`  |
| 1051   | No file  | `958046f8abc5`  |
| 1044   | No file  | `958046f8abc5`  |
| 1036   | No file  | `958046f8abc5`  |
| 1026   | No file  | `958046f8abc5`  |
| 1016   | No file  | `958046f8abc5`  |
| 1009   | No file  | `958046f8abc5`  |
| 1005   | No file  | `958046f8abc5`  |
| 1000   | No file  | `958046f8abc5`  |
| 998    | No file  | `958046f8abc5`  |
| 990    | No file  | `958046f8abc5`  |
| 979    | No file  | `958046f8abc5`  |
| 972    | No file  | `958046f8abc5`  |
| 963    | No file  | `958046f8abc5`  |
| 955    | No file  | `958046f8abc5`  |
| 946    | No file  | `958046f8abc5`  |
| 938    | No file  | `958046f8abc5`  |
| 927    | No file  | `958046f8abc5`  |
| 911    | No file  | `958046f8abc5`  |
| 904    | No file  | `958046f8abc5`  |
| 899    | No file  | `958046f8abc5`  |
| 894    | No file  | `958046f8abc5`  |
| 885    | No file  | `958046f8abc5`  |
| 879    | No file  | `958046f8abc5`  |
| 872    | No file  | `958046f8abc5`  |
| 864    | No file  | `958046f8abc5`  |
| 855    | No file  | `958046f8abc5`  |
| 853    | No file  | `958046f8abc5`  |
| 845    | No file  | `958046f8abc5`  |
| 837    | No file  | `958046f8abc5`  |
| 829    | No file  | `958046f8abc5`  |
| 822    | No file  | `958046f8abc5`  |
| 814    | No file  | `958046f8abc5`  |
| 805    | No file  | `958046f8abc5`  |
| 794    | No file  | `958046f8abc5`  |
| 787    | No file  | `958046f8abc5`  |
| 780    | No file  | `958046f8abc5`  |
| 771    | No file  | `958046f8abc5`  |
| 760    | No file  | `958046f8abc5`  |
| 748    | No file  | `958046f8abc5`  |
| 741    | No file  | `958046f8abc5`  |
| 736    | No file  | `958046f8abc5`  |
| 731    | No file  | `958046f8abc5`  |
| 723    | No file  | `958046f8abc5`  |
| 711    | No file  | `958046f8abc5`  |
| 707    | No file  | `958046f8abc5`  |
| 697    | No file  | `958046f8abc5`  |
| 689    | No file  | `958046f8abc5`  |
| 683    | No file  | `958046f8abc5`  |
| 678    | No file  | `958046f8abc5`  |
| 670    | No file  | `958046f8abc5`  |
| 661    | No file  | `958046f8abc5`  |
| 656    | No file  | `958046f8abc5`  |
| 652    | No file  | `958046f8abc5`  |
| 643    | No file  | `958046f8abc5`  |
| 637    | No file  | `958046f8abc5`  |
| 630    | No file  | `958046f8abc5`  |
| 627    | No file  | `958046f8abc5`  |
| 621    | No file  | `958046f8abc5`  |
| 617    | No file  | `958046f8abc5`  |
| 615    | No file  | `958046f8abc5`  |
| 606    | No file  | `958046f8abc5`  |
| 599    | No file  | `958046f8abc5`  |
| 592    | No file  | `958046f8abc5`  |
| 586    | No file  | `958046f8abc5`  |
| 577    | No file  | `958046f8abc5`  |
| 569    | No file  | `958046f8abc5`  |
| 561    | No file  | `958046f8abc5`  |
| 554    | No file  | `958046f8abc5`  |
| 542    | No file  | `958046f8abc5`  |
| 532    | No file  | `958046f8abc5`  |
| 531    | No file  | `958046f8abc5`  |
| 526    | No file  | `958046f8abc5`  |
| 521    | No file  | `958046f8abc5`  |
| 517    | No file  | `958046f8abc5`  |
| 510    | No file  | `958046f8abc5`  |
| 508    | No file  | `958046f8abc5`  |
| 504    | No file  | `958046f8abc5`  |
| 497    | No file  | `958046f8abc5`  |
| 491    | No file  | `958046f8abc5`  |
| 485    | No file  | `958046f8abc5`  |
| 478    | No file  | `958046f8abc5`  |
| 472    | No file  | `958046f8abc5`  |
| 466    | No file  | `958046f8abc5`  |
| 457    | No file  | `958046f8abc5`  |
| 452    | No file  | `958046f8abc5`  |
| 449    | No file  | `958046f8abc5`  |
| 435    | No file  | `958046f8abc5`  |

<!-- versions:end -->

## Companion Files

The handler reads no companion files.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                 | Type               | Field           | Notes                                                                    |
| ---------------------- | ------------------ | --------------- | ------------------------------------------------------------------------ |
| `+0x00`                | u32                | open_count      | Number of open groups; `1492` on client 3474                             |
| `+0x04`                | u32[open_count]    | open_key_hashes | `key_hash` of each open group, ascending, unique                         |
| `open_key_hashes+0x00` | u32                | group_count     | Number of groups; `2463` on client 3474                                  |
| `open_key_hashes+0x04` | Group[group_count] | groups          | See Group; the last one ends at the end of the file                      |

### Group (variable: 12 bytes + key text)

| Offset  | Type  | Field              | Notes                                                                       |
| ------- | ----- | ------------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32   | key_hash           | Hash of `contents_group_key`, see [Key Hash](#key-hash)                     |
| `+0x04` | str16 | contents_group_key | Decimal group key (`"49"`, `"2295"`); the string `ToClient_IsContentsGroupOpen` takes |

## Key Hash

`key_hash` is the client's string-key hash (`_common/string_hash.py`):
lookup3 `hashlittle` over the UTF-16LE bytes of `contents_group_key` with
seed `0xC5EDE`, the hash of the `stringtable.bss` keys. It reproduces all
2,463 `key_hash` values of client 3474, and every `open_key_hashes` entry is
the `key_hash` of one group.

## Field Names

`contents_group_key` is the `ContentsGroupKey` column of the
`ContentsGroupOption` sheet in a private server's `DataSheets.bexcel` on
client 1784. The sheet has one `0`/`1` column per service (`DEV`,
`KOR_REAL`, `JPN_REAL`, `RUS_REAL`, `NA_REAL`, `TW_REAL`, `SA_REAL`,
`KOR_2`, `TH_REAL`, `ID_REAL`, `TR_REAL`, `XB_REAL`, `PS_REAL`, `GT_REAL`,
`CS_REAL`, `LV_REAL`, `DD_SERVER`) and a `TranslationRegionKey`. 1,551 of
its 1,561 keys are groups of the client 3474 file. Over those 1,551 keys,
membership in `open_key_hashes` agrees with `NA_REAL` on 1,468, more than
any other column (`TW_REAL` 1,446, `KOR_REAL` 1,391, `DEV` 1,050). That and
the Lua function name give `open_key_hashes` its name: the groups whose
service column is `1` for the client's service.

## Notes

- `global_contentsoptions.luac` (client 3474) sets 476 globals as
  `_ContentsGroup_<Name> = ToClient_IsContentsGroupOpen("<key>")`. Every
  key is a group of the file and 386 of them are open, among them
  `330` `_ContentsGroup_DuelCharacter`, `345` `_ContentsGroup_3DMiniMapOpen`
  and `357` `_ContentsGroup_isFairy`. Closed ones include `383`
  `_ContentsGroup_DamageMeter`, `1145` `_ContentsGroup_PearlShopGift` and
  `1151` `_ContentsGroup_PearlShopMileage`.
- `groups` is sorted neither by key nor by hash; `open_key_hashes` is
  sorted by hash, so a lookup can binary-search it.
- Of the 83 keys where the list and `NA_REAL` disagree, 51 are open on
  client 3474 and `0` in the sheet, 32 the reverse. The sheet is a
  private server's copy from early 2022, so these rows are not evidence
  against the reading.
- The client 1784 test client has no `contentsgroupoptionstaticstatusmanager.bss`.
  The 2016 client names `gc::GameOptionManager::isContentsGroupOpen` and
  `ToClient_IsContentsGroupOpen`, but no loader for this file.

## Open Questions

### Which Service the Open List Follows

The list matches the `NA_REAL` column best, and the checked client is the
NA/EU client. Whether a client of another service ships the same `groups`
with its own `open_key_hashes`, and whether NA and EU share one list, needs
a file from another service's client.
