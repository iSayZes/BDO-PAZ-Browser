# `personalnotifyitemlist.bss` Format

## Purpose

A list of item IDs in ascending order: 24,433 of the 70,826 items of
client 3482. Every entry is an item with a record in `itemenchant.dbss`.
No Lua file of client 3482 names the list, and what the client notifies
about these items is open.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ------ | -------------- | --------- |
| 1      | 1921 and later | 3483    | `personalnotifyitemlist.bss` | 97,752 | 1 String Table | 4         |

| Layout | File                         | Known             | Unknown    |
| ------ | ---------------------------- | ----------------- | ---------- |
| 1      | `personalnotifyitemlist.bss` | 97,752 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `5900dafeca10`  |
| 3482   | Layout 1 | `5900dafeca10`  |
| 3474   | Layout 1 | `5900dafeca10`  |
| 3473   | Layout 1 | `5900dafeca10`  |
| 3464   | Layout 1 | `5900dafeca10`  |
| 3458   | Layout 1 | `5900dafeca10`  |
| 3454   | Layout 1 | `5900dafeca10`  |
| 3444   | Layout 1 | `5900dafeca10`  |
| 3435   | Layout 1 | `5900dafeca10`  |
| 3426   | Layout 1 | `5900dafeca10`  |
| 3418   | Layout 1 | `5900dafeca10`  |
| 3412   | Layout 1 | `5900dafeca10`  |
| 3402   | Layout 1 | `5900dafeca10`  |
| 3396   | Layout 1 | `5900dafeca10`  |
| 3387   | Layout 1 | `5900dafeca10`  |
| 3381   | Layout 1 | `5900dafeca10`  |
| 3373   | Layout 1 | `5900dafeca10`  |
| 3364   | Layout 1 | `5900dafeca10`  |
| 3356   | Layout 1 | `5900dafeca10`  |
| 3349   | Layout 1 | `5900dafeca10`  |
| 3342   | Layout 1 | `5900dafeca10`  |
| 3335   | Layout 1 | `5900dafeca10`  |
| 3326   | Layout 1 | `5900dafeca10`  |
| 3321   | Layout 1 | `5900dafeca10`  |
| 3314   | Layout 1 | `5900dafeca10`  |
| 3303   | Layout 1 | `5900dafeca10`  |
| 3302   | Layout 1 | `5900dafeca10`  |
| 3293   | Layout 1 | `5900dafeca10`  |
| 3283   | Layout 1 | `5900dafeca10`  |
| 3275   | Layout 1 | `5900dafeca10`  |
| 3267   | Layout 1 | `5900dafeca10`  |
| 3258   | Layout 1 | `5900dafeca10`  |
| 3251   | Layout 1 | `5900dafeca10`  |
| 3242   | Layout 1 | `5900dafeca10`  |
| 3235   | Layout 1 | `5900dafeca10`  |
| 3229   | Layout 1 | `5900dafeca10`  |
| 3212   | Layout 1 | `5900dafeca10`  |
| 3203   | Layout 1 | `5900dafeca10`  |
| 3193   | Layout 1 | `5900dafeca10`  |
| 3186   | Layout 1 | `5900dafeca10`  |
| 3177   | Layout 1 | `5900dafeca10`  |
| 3169   | Layout 1 | `5900dafeca10`  |
| 3158   | Layout 1 | `5900dafeca10`  |
| 3151   | Layout 1 | `5900dafeca10`  |
| 3144   | Layout 1 | `5900dafeca10`  |
| 3133   | Layout 1 | `5900dafeca10`  |
| 3125   | Layout 1 | `5900dafeca10`  |
| 3118   | Layout 1 | `5900dafeca10`  |
| 3111   | Layout 1 | `5900dafeca10`  |
| 3103   | Layout 1 | `5900dafeca10`  |
| 3095   | Layout 1 | `5900dafeca10`  |
| 3086   | Layout 1 | `5900dafeca10`  |
| 3072   | Layout 1 | `5900dafeca10`  |
| 3062   | Layout 1 | `5900dafeca10`  |
| 3052   | Layout 1 | `5900dafeca10`  |
| 3045   | Layout 1 | `5900dafeca10`  |
| 3037   | Layout 1 | `5900dafeca10`  |
| 3030   | Layout 1 | `5900dafeca10`  |
| 3021   | Layout 1 | `5900dafeca10`  |
| 3012   | Layout 1 | `5900dafeca10`  |
| 3002   | Layout 1 | `5900dafeca10`  |
| 2995   | Layout 1 | `5900dafeca10`  |
| 2987   | Layout 1 | `5900dafeca10`  |
| 2978   | Layout 1 | `5900dafeca10`  |
| 2970   | Layout 1 | `5900dafeca10`  |
| 2959   | Layout 1 | `5900dafeca10`  |
| 2951   | Layout 1 | `5900dafeca10`  |
| 2942   | Layout 1 | `5900dafeca10`  |
| 2935   | Layout 1 | `5900dafeca10`  |
| 2932   | Layout 1 | `5900dafeca10`  |
| 2923   | Layout 1 | `5900dafeca10`  |
| 2919   | Layout 1 | `5900dafeca10`  |
| 2907   | Layout 1 | `5900dafeca10`  |
| 2900   | Layout 1 | `5900dafeca10`  |
| 2891   | Layout 1 | `5900dafeca10`  |
| 2882   | Layout 1 | `5900dafeca10`  |
| 2872   | Layout 1 | `5900dafeca10`  |
| 2863   | Layout 1 | `5900dafeca10`  |
| 2855   | Layout 1 | `5900dafeca10`  |
| 2849   | Layout 1 | `5900dafeca10`  |
| 2844   | Layout 1 | `5900dafeca10`  |
| 2834   | Layout 1 | `5900dafeca10`  |
| 2825   | Layout 1 | `5900dafeca10`  |
| 2819   | Layout 1 | `5900dafeca10`  |
| 2811   | Layout 1 | `5900dafeca10`  |
| 2803   | Layout 1 | `5900dafeca10`  |
| 2794   | Layout 1 | `5900dafeca10`  |
| 2783   | Layout 1 | `5900dafeca10`  |
| 2774   | Layout 1 | `5900dafeca10`  |
| 2765   | Layout 1 | `5900dafeca10`  |
| 2756   | Layout 1 | `5900dafeca10`  |
| 2750   | Layout 1 | `5900dafeca10`  |
| 2743   | Layout 1 | `5900dafeca10`  |
| 2736   | Layout 1 | `5900dafeca10`  |
| 2726   | Layout 1 | `5900dafeca10`  |
| 2717   | Layout 1 | `5900dafeca10`  |
| 2709   | Layout 1 | `5900dafeca10`  |
| 2703   | Layout 1 | `5900dafeca10`  |
| 2695   | Layout 1 | `5900dafeca10`  |
| 2684   | Layout 1 | `5900dafeca10`  |
| 2672   | Layout 1 | `5900dafeca10`  |
| 2665   | Layout 1 | `5900dafeca10`  |
| 2657   | Layout 1 | `5900dafeca10`  |
| 2649   | Layout 1 | `5900dafeca10`  |
| 2644   | Layout 1 | `5900dafeca10`  |
| 2637   | Layout 1 | `5900dafeca10`  |
| 2629   | Layout 1 | `5900dafeca10`  |
| 2619   | Layout 1 | `5900dafeca10`  |
| 2612   | Layout 1 | `5900dafeca10`  |
| 2606   | Layout 1 | `5900dafeca10`  |
| 2602   | Layout 1 | `5900dafeca10`  |
| 2601   | Layout 1 | `5900dafeca10`  |
| 2592   | Layout 1 | `5900dafeca10`  |
| 2583   | Layout 1 | `5900dafeca10`  |
| 2575   | Layout 1 | `5900dafeca10`  |
| 2567   | Layout 1 | `5900dafeca10`  |
| 2560   | Layout 1 | `5900dafeca10`  |
| 2553   | Layout 1 | `5900dafeca10`  |
| 2545   | Layout 1 | `5900dafeca10`  |
| 2538   | Layout 1 | `5900dafeca10`  |
| 2529   | Layout 1 | `5900dafeca10`  |
| 2519   | Layout 1 | `5900dafeca10`  |
| 2513   | Layout 1 | `5900dafeca10`  |
| 2510   | Layout 1 | `5900dafeca10`  |
| 2507   | Layout 1 | `5900dafeca10`  |
| 2503   | Layout 1 | `5900dafeca10`  |
| 2498   | Layout 1 | `5900dafeca10`  |
| 2492   | Layout 1 | `5900dafeca10`  |
| 2487   | Layout 1 | `5900dafeca10`  |
| 2480   | Layout 1 | `5900dafeca10`  |
| 2474   | Layout 1 | `5900dafeca10`  |
| 2468   | Layout 1 | `5900dafeca10`  |
| 2460   | Layout 1 | `5900dafeca10`  |
| 2453   | Layout 1 | `5900dafeca10`  |
| 2444   | Layout 1 | `5900dafeca10`  |
| 2438   | Layout 1 | `5900dafeca10`  |
| 2434   | Layout 1 | `5900dafeca10`  |
| 2429   | Layout 1 | `5900dafeca10`  |
| 2421   | Layout 1 | `5900dafeca10`  |
| 2414   | Layout 1 | `5900dafeca10`  |
| 2407   | Layout 1 | `5900dafeca10`  |
| 2401   | Layout 1 | `5900dafeca10`  |
| 2397   | Layout 1 | `5900dafeca10`  |
| 2393   | Layout 1 | `5900dafeca10`  |
| 2384   | Layout 1 | `5900dafeca10`  |
| 2378   | Layout 1 | `5900dafeca10`  |
| 2372   | Layout 1 | `5900dafeca10`  |
| 2358   | Layout 1 | `5900dafeca10`  |
| 2352   | Layout 1 | `5900dafeca10`  |
| 2347   | Layout 1 | `5900dafeca10`  |
| 2343   | Layout 1 | `5900dafeca10`  |
| 2335   | Layout 1 | `5900dafeca10`  |
| 2327   | Layout 1 | `5900dafeca10`  |
| 2324   | Layout 1 | `5900dafeca10`  |
| 2319   | Layout 1 | `5900dafeca10`  |
| 2313   | Layout 1 | `5900dafeca10`  |
| 2308   | Layout 1 | `5900dafeca10`  |
| 2302   | Layout 1 | `5900dafeca10`  |
| 2295   | Layout 1 | `5900dafeca10`  |
| 2290   | Layout 1 | `5900dafeca10`  |
| 2284   | Layout 1 | `5900dafeca10`  |
| 2276   | Layout 1 | `5900dafeca10`  |
| 2269   | Layout 1 | `5900dafeca10`  |
| 2259   | Layout 1 | `5900dafeca10`  |
| 2250   | Layout 1 | `5900dafeca10`  |
| 2243   | Layout 1 | `5900dafeca10`  |
| 2235   | Layout 1 | `5900dafeca10`  |
| 2229   | Layout 1 | `5900dafeca10`  |
| 2224   | Layout 1 | `5900dafeca10`  |
| 2218   | Layout 1 | `5900dafeca10`  |
| 2215   | Layout 1 | `5900dafeca10`  |
| 2207   | Layout 1 | `5900dafeca10`  |
| 2203   | Layout 1 | `5900dafeca10`  |
| 2196   | Layout 1 | `5900dafeca10`  |
| 2192   | Layout 1 | `5900dafeca10`  |
| 2189   | Layout 1 | `5900dafeca10`  |
| 2183   | Layout 1 | `5900dafeca10`  |
| 2179   | Layout 1 | `5900dafeca10`  |
| 2171   | Layout 1 | `5900dafeca10`  |
| 2163   | Layout 1 | `5900dafeca10`  |
| 2156   | Layout 1 | `5900dafeca10`  |
| 2151   | Layout 1 | `5900dafeca10`  |
| 2147   | Layout 1 | `5900dafeca10`  |
| 2142   | Layout 1 | `5900dafeca10`  |
| 2138   | Layout 1 | `5900dafeca10`  |
| 2134   | Layout 1 | `5900dafeca10`  |
| 2130   | Layout 1 | `5900dafeca10`  |
| 2122   | Layout 1 | `5900dafeca10`  |
| 2107   | Layout 1 | `5900dafeca10`  |
| 2098   | Layout 1 | `5900dafeca10`  |
| 2089   | Layout 1 | `5900dafeca10`  |
| 2081   | Layout 1 | `5900dafeca10`  |
| 2073   | Layout 1 | `5900dafeca10`  |
| 2067   | Layout 1 | `5900dafeca10`  |
| 2063   | Layout 1 | `5900dafeca10`  |
| 2059   | Layout 1 | `5900dafeca10`  |
| 2052   | Layout 1 | `5900dafeca10`  |
| 2044   | Layout 1 | `5900dafeca10`  |
| 2039   | Layout 1 | `5900dafeca10`  |
| 2032   | Layout 1 | `5900dafeca10`  |
| 2025   | Layout 1 | `5900dafeca10`  |
| 2011   | Layout 1 | `5900dafeca10`  |
| 2005   | Layout 1 | `5900dafeca10`  |
| 2000   | Layout 1 | `5900dafeca10`  |
| 1996   | Layout 1 | `5900dafeca10`  |
| 1991   | Layout 1 | `5900dafeca10`  |
| 1985   | Layout 1 | `5900dafeca10`  |
| 1980   | Layout 1 | `5900dafeca10`  |
| 1969   | Layout 1 | `5900dafeca10`  |
| 1964   | Layout 1 | `5900dafeca10`  |
| 1958   | Layout 1 | `5900dafeca10`  |
| 1950   | Layout 1 | `5900dafeca10`  |
| 1945   | Layout 1 | `5900dafeca10`  |
| 1937   | Layout 1 | `5900dafeca10`  |
| 1933   | Layout 1 | `5900dafeca10`  |
| 1927   | Layout 1 | `5900dafeca10`  |
| 1921   | Layout 1 | `5900dafeca10`  |
| 1914   | No file  | `5900dafeca10`  |
| 1908   | No file  | `5900dafeca10`  |
| 1897   | No file  | `5900dafeca10`  |
| 1892   | No file  | `5900dafeca10`  |
| 1886   | No file  | `5900dafeca10`  |
| 1881   | No file  | `5900dafeca10`  |
| 1871   | No file  | `5900dafeca10`  |
| 1866   | No file  | `5900dafeca10`  |
| 1862   | No file  | `5900dafeca10`  |
| 1854   | No file  | `5900dafeca10`  |
| 1846   | No file  | `5900dafeca10`  |
| 1838   | No file  | `5900dafeca10`  |
| 1832   | No file  | `5900dafeca10`  |
| 1826   | No file  | `5900dafeca10`  |
| 1822   | No file  | `5900dafeca10`  |
| 1818   | No file  | `5900dafeca10`  |
| 1804   | No file  | `5900dafeca10`  |
| 1794   | No file  | `5900dafeca10`  |
| 1790   | No file  | `5900dafeca10`  |
| 1784   | No file  | `5900dafeca10`  |
| 1774   | No file  | `5900dafeca10`  |
| 1771   | No file  | `5900dafeca10`  |
| 1762   | No file  | `5900dafeca10`  |
| 1759   | No file  | `5900dafeca10`  |
| 1754   | No file  | `5900dafeca10`  |
| 1749   | No file  | `5900dafeca10`  |
| 1743   | No file  | `5900dafeca10`  |
| 1737   | No file  | `5900dafeca10`  |
| 1731   | No file  | `5900dafeca10`  |
| 1725   | No file  | `5900dafeca10`  |
| 1717   | No file  | `5900dafeca10`  |
| 1710   | No file  | `5900dafeca10`  |
| 1704   | No file  | `5900dafeca10`  |
| 1698   | No file  | `5900dafeca10`  |
| 1690   | No file  | `5900dafeca10`  |
| 1685   | No file  | `5900dafeca10`  |
| 1680   | No file  | `5900dafeca10`  |
| 1674   | No file  | `5900dafeca10`  |
| 1668   | No file  | `5900dafeca10`  |
| 1659   | No file  | `5900dafeca10`  |
| 1649   | No file  | `5900dafeca10`  |
| 1642   | No file  | `5900dafeca10`  |
| 1636   | No file  | `5900dafeca10`  |
| 1628   | No file  | `5900dafeca10`  |
| 1622   | No file  | `5900dafeca10`  |
| 1614   | No file  | `5900dafeca10`  |
| 1608   | No file  | `5900dafeca10`  |
| 1602   | No file  | `5900dafeca10`  |
| 1598   | No file  | `5900dafeca10`  |
| 1594   | No file  | `5900dafeca10`  |
| 1590   | No file  | `5900dafeca10`  |
| 1587   | No file  | `5900dafeca10`  |
| 1584   | No file  | `5900dafeca10`  |
| 1579   | No file  | `5900dafeca10`  |
| 1572   | No file  | `5900dafeca10`  |
| 1565   | No file  | `5900dafeca10`  |
| 1559   | No file  | `5900dafeca10`  |
| 1554   | No file  | `5900dafeca10`  |
| 1547   | No file  | `5900dafeca10`  |
| 1537   | No file  | `5900dafeca10`  |
| 1529   | No file  | `5900dafeca10`  |
| 1524   | No file  | `5900dafeca10`  |
| 1519   | No file  | `5900dafeca10`  |
| 1509   | No file  | `5900dafeca10`  |
| 1506   | No file  | `5900dafeca10`  |
| 1504   | No file  | `5900dafeca10`  |
| 1500   | No file  | `5900dafeca10`  |
| 1493   | No file  | `5900dafeca10`  |
| 1489   | No file  | `5900dafeca10`  |
| 1485   | No file  | `5900dafeca10`  |
| 1481   | No file  | `5900dafeca10`  |
| 1474   | No file  | `5900dafeca10`  |
| 1466   | No file  | `5900dafeca10`  |
| 1462   | No file  | `5900dafeca10`  |
| 1459   | No file  | `5900dafeca10`  |
| 1453   | No file  | `5900dafeca10`  |
| 1450   | No file  | `5900dafeca10`  |
| 1445   | No file  | `5900dafeca10`  |
| 1439   | No file  | `5900dafeca10`  |
| 1433   | No file  | `5900dafeca10`  |
| 1430   | No file  | `5900dafeca10`  |
| 1426   | No file  | `5900dafeca10`  |
| 1421   | No file  | `5900dafeca10`  |
| 1417   | No file  | `5900dafeca10`  |
| 1416   | No file  | `5900dafeca10`  |
| 1409   | No file  | `5900dafeca10`  |
| 1405   | No file  | `5900dafeca10`  |
| 1401   | No file  | `5900dafeca10`  |
| 1396   | No file  | `5900dafeca10`  |
| 1391   | No file  | `5900dafeca10`  |
| 1390   | No file  | `5900dafeca10`  |
| 1386   | No file  | `5900dafeca10`  |
| 1381   | No file  | `5900dafeca10`  |
| 1379   | No file  | `5900dafeca10`  |
| 1372   | No file  | `5900dafeca10`  |
| 1366   | No file  | `5900dafeca10`  |
| 1364   | No file  | `5900dafeca10`  |
| 1363   | No file  | `5900dafeca10`  |
| 1360   | No file  | `5900dafeca10`  |
| 1358   | No file  | `5900dafeca10`  |
| 1355   | No file  | `5900dafeca10`  |
| 1351   | No file  | `5900dafeca10`  |
| 1348   | No file  | `5900dafeca10`  |
| 1346   | No file  | `5900dafeca10`  |
| 1341   | No file  | `5900dafeca10`  |
| 1340   | No file  | `5900dafeca10`  |
| 1338   | No file  | `5900dafeca10`  |
| 1335   | No file  | `5900dafeca10`  |
| 1333   | No file  | `5900dafeca10`  |
| 1329   | No file  | `5900dafeca10`  |
| 1327   | No file  | `5900dafeca10`  |
| 1324   | No file  | `5900dafeca10`  |
| 1321   | No file  | `5900dafeca10`  |
| 1319   | No file  | `5900dafeca10`  |
| 1318   | No file  | `5900dafeca10`  |
| 1316   | No file  | `5900dafeca10`  |
| 1313   | No file  | `5900dafeca10`  |
| 1311   | No file  | `5900dafeca10`  |
| 1309   | No file  | `5900dafeca10`  |
| 1304   | No file  | `5900dafeca10`  |
| 1292   | No file  | `5900dafeca10`  |
| 1286   | No file  | `5900dafeca10`  |
| 1280   | No file  | `5900dafeca10`  |
| 1276   | No file  | `5900dafeca10`  |
| 1267   | No file  | `5900dafeca10`  |
| 1261   | No file  | `5900dafeca10`  |
| 1256   | No file  | `5900dafeca10`  |
| 1250   | No file  | `5900dafeca10`  |
| 1246   | No file  | `5900dafeca10`  |
| 1239   | No file  | `5900dafeca10`  |
| 1230   | No file  | `5900dafeca10`  |
| 1226   | No file  | `5900dafeca10`  |
| 1220   | No file  | `5900dafeca10`  |
| 1217   | No file  | `5900dafeca10`  |
| 1211   | No file  | `5900dafeca10`  |
| 1210   | No file  | `5900dafeca10`  |
| 1208   | No file  | `5900dafeca10`  |
| 1203   | No file  | `5900dafeca10`  |
| 1197   | No file  | `5900dafeca10`  |
| 1194   | No file  | `5900dafeca10`  |
| 1192   | No file  | `5900dafeca10`  |
| 1187   | No file  | `5900dafeca10`  |
| 1183   | No file  | `5900dafeca10`  |
| 1177   | No file  | `5900dafeca10`  |
| 1173   | No file  | `5900dafeca10`  |
| 1167   | No file  | `5900dafeca10`  |
| 1164   | No file  | `5900dafeca10`  |
| 1156   | No file  | `5900dafeca10`  |
| 1149   | No file  | `5900dafeca10`  |
| 1144   | No file  | `5900dafeca10`  |
| 1137   | No file  | `5900dafeca10`  |
| 1132   | No file  | `5900dafeca10`  |
| 1127   | No file  | `5900dafeca10`  |
| 1122   | No file  | `5900dafeca10`  |
| 1118   | No file  | `5900dafeca10`  |
| 1114   | No file  | `5900dafeca10`  |
| 1109   | No file  | `5900dafeca10`  |
| 1102   | No file  | `5900dafeca10`  |
| 1096   | No file  | `5900dafeca10`  |
| 1088   | No file  | `5900dafeca10`  |
| 1081   | No file  | `5900dafeca10`  |
| 1076   | No file  | `5900dafeca10`  |
| 1069   | No file  | `5900dafeca10`  |
| 1064   | No file  | `5900dafeca10`  |
| 1058   | No file  | `5900dafeca10`  |
| 1051   | No file  | `5900dafeca10`  |
| 1044   | No file  | `5900dafeca10`  |
| 1036   | No file  | `5900dafeca10`  |
| 1026   | No file  | `5900dafeca10`  |
| 1016   | No file  | `5900dafeca10`  |
| 1009   | No file  | `5900dafeca10`  |
| 1005   | No file  | `5900dafeca10`  |
| 1000   | No file  | `5900dafeca10`  |
| 998    | No file  | `5900dafeca10`  |
| 990    | No file  | `5900dafeca10`  |
| 979    | No file  | `5900dafeca10`  |
| 972    | No file  | `5900dafeca10`  |
| 963    | No file  | `5900dafeca10`  |
| 955    | No file  | `5900dafeca10`  |
| 946    | No file  | `5900dafeca10`  |
| 938    | No file  | `5900dafeca10`  |
| 927    | No file  | `5900dafeca10`  |
| 911    | No file  | `5900dafeca10`  |
| 904    | No file  | `5900dafeca10`  |
| 899    | No file  | `5900dafeca10`  |
| 894    | No file  | `5900dafeca10`  |
| 885    | No file  | `5900dafeca10`  |
| 879    | No file  | `5900dafeca10`  |
| 872    | No file  | `5900dafeca10`  |
| 864    | No file  | `5900dafeca10`  |
| 855    | No file  | `5900dafeca10`  |
| 853    | No file  | `5900dafeca10`  |
| 845    | No file  | `5900dafeca10`  |
| 837    | No file  | `5900dafeca10`  |
| 829    | No file  | `5900dafeca10`  |
| 822    | No file  | `5900dafeca10`  |
| 814    | No file  | `5900dafeca10`  |
| 805    | No file  | `5900dafeca10`  |
| 794    | No file  | `5900dafeca10`  |
| 787    | No file  | `5900dafeca10`  |
| 780    | No file  | `5900dafeca10`  |
| 771    | No file  | `5900dafeca10`  |
| 760    | No file  | `5900dafeca10`  |
| 748    | No file  | `5900dafeca10`  |
| 741    | No file  | `5900dafeca10`  |
| 736    | No file  | `5900dafeca10`  |
| 731    | No file  | `5900dafeca10`  |
| 723    | No file  | `5900dafeca10`  |
| 711    | No file  | `5900dafeca10`  |
| 707    | No file  | `5900dafeca10`  |
| 697    | No file  | `5900dafeca10`  |
| 689    | No file  | `5900dafeca10`  |
| 683    | No file  | `5900dafeca10`  |
| 678    | No file  | `5900dafeca10`  |
| 670    | No file  | `5900dafeca10`  |
| 661    | No file  | `5900dafeca10`  |
| 656    | No file  | `5900dafeca10`  |
| 652    | No file  | `5900dafeca10`  |
| 643    | No file  | `5900dafeca10`  |
| 637    | No file  | `5900dafeca10`  |
| 630    | No file  | `5900dafeca10`  |
| 627    | No file  | `5900dafeca10`  |
| 621    | No file  | `5900dafeca10`  |
| 617    | No file  | `5900dafeca10`  |
| 615    | No file  | `5900dafeca10`  |
| 606    | No file  | `5900dafeca10`  |
| 599    | No file  | `5900dafeca10`  |
| 592    | No file  | `5900dafeca10`  |
| 586    | No file  | `5900dafeca10`  |
| 577    | No file  | `5900dafeca10`  |
| 569    | No file  | `5900dafeca10`  |
| 561    | No file  | `5900dafeca10`  |
| 554    | No file  | `5900dafeca10`  |
| 542    | No file  | `5900dafeca10`  |
| 532    | No file  | `5900dafeca10`  |
| 531    | No file  | `5900dafeca10`  |
| 526    | No file  | `5900dafeca10`  |
| 521    | No file  | `5900dafeca10`  |
| 517    | No file  | `5900dafeca10`  |
| 510    | No file  | `5900dafeca10`  |
| 508    | No file  | `5900dafeca10`  |
| 504    | No file  | `5900dafeca10`  |
| 497    | No file  | `5900dafeca10`  |
| 491    | No file  | `5900dafeca10`  |
| 485    | No file  | `5900dafeca10`  |
| 478    | No file  | `5900dafeca10`  |
| 472    | No file  | `5900dafeca10`  |
| 466    | No file  | `5900dafeca10`  |
| 457    | No file  | `5900dafeca10`  |
| 452    | No file  | `5900dafeca10`  |
| 449    | No file  | `5900dafeca10`  |
| 435    | No file  | `5900dafeca10`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                |
| --------------------- | -------- | ------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of u32 rows with an empty string table, read by
`u32_rows()` in `_common/pabr_strings.py`.

| Offset              | Type         | Field        | Notes                                             |
| ------------------- | ------------ | ------------ | ------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | `PABR`                                            |
| `+0x04`             | u32          | count        | Number of items                                   |
| `+0x08`             | u32[count]   | item_ids     | Item IDs (LOC type 0 names), ascending and unique |
| `item_ids+0x00`     | String Table | string_table | Empty string table                                |
| `string_table+0x00` | u32          | table_start  | End of the rows (`8 + 4 * count`)                 |
| `string_table+0x04` | u32          | zero         | `0`                                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Notes

- The list starts with the gold bars (`2` to `5`). Among the lowest item
  IDs it leaves out silver (`1`), Pearls (`6`), Mileage (`7`) and the
  skill and life EXP items from `51` to `92`.
- The file is not in client 1784.

## Open Questions

### What the List Selects

Which items the list holds, and what the client does with them, is not
in the Lua. The name reads as a personal notice when the item is
obtained; nothing in the item records of client 3482 has been matched to
the list yet.
