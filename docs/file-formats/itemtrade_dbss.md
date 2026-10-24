# `itemtrade.dbss` Format

## Purpose

The character keys of the NPCs that buy trade goods: trade managers, node
managers with a trade counter and a few quest-area traders. A row is the u16
character key and nothing else.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------------- | --------- |
| 1      | 1276 and later | 3483    | `itemtrade.dbss`       | 256   | 126 Row       | 2         |
| 1      | 1276 and later | 3483    | `itemtradeoffset.dbss` | 1,264 | 126 Index Row | 10        |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `itemtrade.dbss`       | 256 B (100.0%)   | 0 B (0.0%) |
| 1      | `itemtradeoffset.dbss` | 1,264 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fc444cb02004`  |
| 3482   | Layout 1 | `fc444cb02004`  |
| 3474   | Layout 1 | `fc444cb02004`  |
| 3473   | Layout 1 | `fc444cb02004`  |
| 3464   | Layout 1 | `fc444cb02004`  |
| 3458   | Layout 1 | `fc444cb02004`  |
| 3454   | Layout 1 | `fc444cb02004`  |
| 3444   | Layout 1 | `fc444cb02004`  |
| 3435   | Layout 1 | `fc444cb02004`  |
| 3426   | Layout 1 | `fc444cb02004`  |
| 3418   | Layout 1 | `fc444cb02004`  |
| 3412   | Layout 1 | `fc444cb02004`  |
| 3402   | Layout 1 | `fc444cb02004`  |
| 3396   | Layout 1 | `fc444cb02004`  |
| 3387   | Layout 1 | `fc444cb02004`  |
| 3381   | Layout 1 | `fc444cb02004`  |
| 3373   | Layout 1 | `fc444cb02004`  |
| 3364   | Layout 1 | `fc444cb02004`  |
| 3356   | Layout 1 | `fc444cb02004`  |
| 3349   | Layout 1 | `fc444cb02004`  |
| 3342   | Layout 1 | `fc444cb02004`  |
| 3335   | Layout 1 | `fc444cb02004`  |
| 3326   | Layout 1 | `fc444cb02004`  |
| 3321   | Layout 1 | `fc444cb02004`  |
| 3314   | Layout 1 | `fc444cb02004`  |
| 3303   | Layout 1 | `fc444cb02004`  |
| 3302   | Layout 1 | `fc444cb02004`  |
| 3293   | Layout 1 | `fc444cb02004`  |
| 3283   | Layout 1 | `fc444cb02004`  |
| 3275   | Layout 1 | `fc444cb02004`  |
| 3267   | Layout 1 | `fc444cb02004`  |
| 3258   | Layout 1 | `fc444cb02004`  |
| 3251   | Layout 1 | `fc444cb02004`  |
| 3242   | Layout 1 | `fc444cb02004`  |
| 3235   | Layout 1 | `fc444cb02004`  |
| 3229   | Layout 1 | `fc444cb02004`  |
| 3212   | Layout 1 | `fc444cb02004`  |
| 3203   | Layout 1 | `fc444cb02004`  |
| 3193   | Layout 1 | `fc444cb02004`  |
| 3186   | Layout 1 | `fc444cb02004`  |
| 3177   | Layout 1 | `fc444cb02004`  |
| 3169   | Layout 1 | `fc444cb02004`  |
| 3158   | Layout 1 | `fc444cb02004`  |
| 3151   | Layout 1 | `fc444cb02004`  |
| 3144   | Layout 1 | `fc444cb02004`  |
| 3133   | Layout 1 | `fc444cb02004`  |
| 3125   | Layout 1 | `fc444cb02004`  |
| 3118   | Layout 1 | `fc444cb02004`  |
| 3111   | Layout 1 | `fc444cb02004`  |
| 3103   | Layout 1 | `fc444cb02004`  |
| 3095   | Layout 1 | `fc444cb02004`  |
| 3086   | Layout 1 | `fc444cb02004`  |
| 3072   | Layout 1 | `fc444cb02004`  |
| 3062   | Layout 1 | `fc444cb02004`  |
| 3052   | Layout 1 | `fc444cb02004`  |
| 3045   | Layout 1 | `fc444cb02004`  |
| 3037   | Layout 1 | `fc444cb02004`  |
| 3030   | Layout 1 | `fc444cb02004`  |
| 3021   | Layout 1 | `fc444cb02004`  |
| 3012   | Layout 1 | `fc444cb02004`  |
| 3002   | Layout 1 | `fc444cb02004`  |
| 2995   | Layout 1 | `fc444cb02004`  |
| 2987   | Layout 1 | `fc444cb02004`  |
| 2978   | Layout 1 | `fc444cb02004`  |
| 2970   | Layout 1 | `fc444cb02004`  |
| 2959   | Layout 1 | `fc444cb02004`  |
| 2951   | Layout 1 | `fc444cb02004`  |
| 2942   | Layout 1 | `fc444cb02004`  |
| 2935   | Layout 1 | `fc444cb02004`  |
| 2932   | Layout 1 | `fc444cb02004`  |
| 2923   | Layout 1 | `fc444cb02004`  |
| 2919   | Layout 1 | `fc444cb02004`  |
| 2907   | Layout 1 | `fc444cb02004`  |
| 2900   | Layout 1 | `fc444cb02004`  |
| 2891   | Layout 1 | `fc444cb02004`  |
| 2882   | Layout 1 | `fc444cb02004`  |
| 2872   | Layout 1 | `fc444cb02004`  |
| 2863   | Layout 1 | `fc444cb02004`  |
| 2855   | Layout 1 | `fc444cb02004`  |
| 2849   | Layout 1 | `fc444cb02004`  |
| 2844   | Layout 1 | `fc444cb02004`  |
| 2834   | Layout 1 | `fc444cb02004`  |
| 2825   | Layout 1 | `fc444cb02004`  |
| 2819   | Layout 1 | `fc444cb02004`  |
| 2811   | Layout 1 | `fc444cb02004`  |
| 2803   | Layout 1 | `fc444cb02004`  |
| 2794   | Layout 1 | `fc444cb02004`  |
| 2783   | Layout 1 | `fc444cb02004`  |
| 2774   | Layout 1 | `fc444cb02004`  |
| 2765   | Layout 1 | `fc444cb02004`  |
| 2756   | Layout 1 | `fc444cb02004`  |
| 2750   | Layout 1 | `fc444cb02004`  |
| 2743   | Layout 1 | `fc444cb02004`  |
| 2736   | Layout 1 | `fc444cb02004`  |
| 2726   | Layout 1 | `fc444cb02004`  |
| 2717   | Layout 1 | `fc444cb02004`  |
| 2709   | Layout 1 | `fc444cb02004`  |
| 2703   | Layout 1 | `fc444cb02004`  |
| 2695   | Layout 1 | `fc444cb02004`  |
| 2684   | Layout 1 | `fc444cb02004`  |
| 2672   | Layout 1 | `fc444cb02004`  |
| 2665   | Layout 1 | `fc444cb02004`  |
| 2657   | Layout 1 | `fc444cb02004`  |
| 2649   | Layout 1 | `fc444cb02004`  |
| 2644   | Layout 1 | `fc444cb02004`  |
| 2637   | Layout 1 | `fc444cb02004`  |
| 2629   | Layout 1 | `fc444cb02004`  |
| 2619   | Layout 1 | `fc444cb02004`  |
| 2612   | Layout 1 | `fc444cb02004`  |
| 2606   | Layout 1 | `fc444cb02004`  |
| 2602   | Layout 1 | `fc444cb02004`  |
| 2601   | Layout 1 | `fc444cb02004`  |
| 2592   | Layout 1 | `fc444cb02004`  |
| 2583   | Layout 1 | `fc444cb02004`  |
| 2575   | Layout 1 | `fc444cb02004`  |
| 2567   | Layout 1 | `fc444cb02004`  |
| 2560   | Layout 1 | `fc444cb02004`  |
| 2553   | Layout 1 | `fc444cb02004`  |
| 2545   | Layout 1 | `fc444cb02004`  |
| 2538   | Layout 1 | `fc444cb02004`  |
| 2529   | Layout 1 | `fc444cb02004`  |
| 2519   | Layout 1 | `fc444cb02004`  |
| 2513   | Layout 1 | `fc444cb02004`  |
| 2510   | Layout 1 | `fc444cb02004`  |
| 2507   | Layout 1 | `fc444cb02004`  |
| 2503   | Layout 1 | `fc444cb02004`  |
| 2498   | Layout 1 | `fc444cb02004`  |
| 2492   | Layout 1 | `fc444cb02004`  |
| 2487   | Layout 1 | `fc444cb02004`  |
| 2480   | Layout 1 | `fc444cb02004`  |
| 2474   | Layout 1 | `fc444cb02004`  |
| 2468   | Layout 1 | `fc444cb02004`  |
| 2460   | Layout 1 | `fc444cb02004`  |
| 2453   | Layout 1 | `fc444cb02004`  |
| 2444   | Layout 1 | `fc444cb02004`  |
| 2438   | Layout 1 | `fc444cb02004`  |
| 2434   | Layout 1 | `fc444cb02004`  |
| 2429   | Layout 1 | `fc444cb02004`  |
| 2421   | Layout 1 | `fc444cb02004`  |
| 2414   | Layout 1 | `fc444cb02004`  |
| 2407   | Layout 1 | `fc444cb02004`  |
| 2401   | Layout 1 | `fc444cb02004`  |
| 2397   | Layout 1 | `fc444cb02004`  |
| 2393   | Layout 1 | `fc444cb02004`  |
| 2384   | Layout 1 | `fc444cb02004`  |
| 2378   | Layout 1 | `fc444cb02004`  |
| 2372   | Layout 1 | `fc444cb02004`  |
| 2358   | Layout 1 | `fc444cb02004`  |
| 2352   | Layout 1 | `fc444cb02004`  |
| 2347   | Layout 1 | `fc444cb02004`  |
| 2343   | Layout 1 | `fc444cb02004`  |
| 2335   | Layout 1 | `fc444cb02004`  |
| 2327   | Layout 1 | `fc444cb02004`  |
| 2324   | Layout 1 | `fc444cb02004`  |
| 2319   | Layout 1 | `fc444cb02004`  |
| 2313   | Layout 1 | `fc444cb02004`  |
| 2308   | Layout 1 | `fc444cb02004`  |
| 2302   | Layout 1 | `fc444cb02004`  |
| 2295   | Layout 1 | `fc444cb02004`  |
| 2290   | Layout 1 | `fc444cb02004`  |
| 2284   | Layout 1 | `fc444cb02004`  |
| 2276   | Layout 1 | `fc444cb02004`  |
| 2269   | Layout 1 | `fc444cb02004`  |
| 2259   | Layout 1 | `fc444cb02004`  |
| 2250   | Layout 1 | `fc444cb02004`  |
| 2243   | Layout 1 | `fc444cb02004`  |
| 2235   | Layout 1 | `fc444cb02004`  |
| 2229   | Layout 1 | `fc444cb02004`  |
| 2224   | Layout 1 | `fc444cb02004`  |
| 2218   | Layout 1 | `fc444cb02004`  |
| 2215   | Layout 1 | `fc444cb02004`  |
| 2207   | Layout 1 | `fc444cb02004`  |
| 2203   | Layout 1 | `fc444cb02004`  |
| 2196   | Layout 1 | `fc444cb02004`  |
| 2192   | Layout 1 | `fc444cb02004`  |
| 2189   | Layout 1 | `fc444cb02004`  |
| 2183   | Layout 1 | `fc444cb02004`  |
| 2179   | Layout 1 | `fc444cb02004`  |
| 2171   | Layout 1 | `fc444cb02004`  |
| 2163   | Layout 1 | `fc444cb02004`  |
| 2156   | Layout 1 | `fc444cb02004`  |
| 2151   | Layout 1 | `fc444cb02004`  |
| 2147   | Layout 1 | `fc444cb02004`  |
| 2142   | Layout 1 | `fc444cb02004`  |
| 2138   | Layout 1 | `fc444cb02004`  |
| 2134   | Layout 1 | `fc444cb02004`  |
| 2130   | Layout 1 | `fc444cb02004`  |
| 2122   | Layout 1 | `fc444cb02004`  |
| 2107   | Layout 1 | `fc444cb02004`  |
| 2098   | Layout 1 | `fc444cb02004`  |
| 2089   | Layout 1 | `fc444cb02004`  |
| 2081   | Layout 1 | `fc444cb02004`  |
| 2073   | Layout 1 | `fc444cb02004`  |
| 2067   | Layout 1 | `fc444cb02004`  |
| 2063   | Layout 1 | `fc444cb02004`  |
| 2059   | Layout 1 | `fc444cb02004`  |
| 2052   | Layout 1 | `fc444cb02004`  |
| 2044   | Layout 1 | `fc444cb02004`  |
| 2039   | Layout 1 | `fc444cb02004`  |
| 2032   | Layout 1 | `fc444cb02004`  |
| 2025   | Layout 1 | `fc444cb02004`  |
| 2011   | Layout 1 | `fc444cb02004`  |
| 2005   | Layout 1 | `fc444cb02004`  |
| 2000   | Layout 1 | `fc444cb02004`  |
| 1996   | Layout 1 | `fc444cb02004`  |
| 1991   | Layout 1 | `fc444cb02004`  |
| 1985   | Layout 1 | `fc444cb02004`  |
| 1980   | Layout 1 | `fc444cb02004`  |
| 1969   | Layout 1 | `fc444cb02004`  |
| 1964   | Layout 1 | `fc444cb02004`  |
| 1958   | Layout 1 | `fc444cb02004`  |
| 1950   | Layout 1 | `fc444cb02004`  |
| 1945   | Layout 1 | `fc444cb02004`  |
| 1937   | Layout 1 | `fc444cb02004`  |
| 1933   | Layout 1 | `fc444cb02004`  |
| 1927   | Layout 1 | `fc444cb02004`  |
| 1921   | Layout 1 | `fc444cb02004`  |
| 1914   | Layout 1 | `fc444cb02004`  |
| 1908   | Layout 1 | `fc444cb02004`  |
| 1897   | Layout 1 | `fc444cb02004`  |
| 1892   | Layout 1 | `fc444cb02004`  |
| 1886   | Layout 1 | `fc444cb02004`  |
| 1881   | Layout 1 | `fc444cb02004`  |
| 1871   | Layout 1 | `fc444cb02004`  |
| 1866   | Layout 1 | `fc444cb02004`  |
| 1862   | Layout 1 | `fc444cb02004`  |
| 1854   | Layout 1 | `fc444cb02004`  |
| 1846   | Layout 1 | `fc444cb02004`  |
| 1838   | Layout 1 | `fc444cb02004`  |
| 1832   | Layout 1 | `fc444cb02004`  |
| 1826   | Layout 1 | `fc444cb02004`  |
| 1822   | Layout 1 | `fc444cb02004`  |
| 1818   | Layout 1 | `fc444cb02004`  |
| 1804   | Layout 1 | `fc444cb02004`  |
| 1794   | Layout 1 | `fc444cb02004`  |
| 1790   | Layout 1 | `fc444cb02004`  |
| 1784   | Layout 1 | `fc444cb02004`  |
| 1774   | Layout 1 | `fc444cb02004`  |
| 1771   | Layout 1 | `fc444cb02004`  |
| 1762   | Layout 1 | `fc444cb02004`  |
| 1759   | Layout 1 | `fc444cb02004`  |
| 1754   | Layout 1 | `fc444cb02004`  |
| 1749   | Layout 1 | `fc444cb02004`  |
| 1743   | Layout 1 | `fc444cb02004`  |
| 1737   | Layout 1 | `fc444cb02004`  |
| 1731   | Layout 1 | `fc444cb02004`  |
| 1725   | Layout 1 | `fc444cb02004`  |
| 1717   | Layout 1 | `fc444cb02004`  |
| 1710   | Layout 1 | `fc444cb02004`  |
| 1704   | Layout 1 | `fc444cb02004`  |
| 1698   | Layout 1 | `fc444cb02004`  |
| 1690   | Layout 1 | `fc444cb02004`  |
| 1685   | Layout 1 | `fc444cb02004`  |
| 1680   | Layout 1 | `fc444cb02004`  |
| 1674   | Layout 1 | `fc444cb02004`  |
| 1668   | Layout 1 | `fc444cb02004`  |
| 1659   | Layout 1 | `fc444cb02004`  |
| 1649   | Layout 1 | `fc444cb02004`  |
| 1642   | Layout 1 | `fc444cb02004`  |
| 1636   | Layout 1 | `fc444cb02004`  |
| 1628   | Layout 1 | `fc444cb02004`  |
| 1622   | Layout 1 | `fc444cb02004`  |
| 1614   | Layout 1 | `fc444cb02004`  |
| 1608   | Layout 1 | `fc444cb02004`  |
| 1602   | Layout 1 | `fc444cb02004`  |
| 1598   | Layout 1 | `fc444cb02004`  |
| 1594   | Layout 1 | `fc444cb02004`  |
| 1590   | Layout 1 | `fc444cb02004`  |
| 1587   | Layout 1 | `fc444cb02004`  |
| 1584   | Layout 1 | `fc444cb02004`  |
| 1579   | Layout 1 | `fc444cb02004`  |
| 1572   | Layout 1 | `fc444cb02004`  |
| 1565   | Layout 1 | `fc444cb02004`  |
| 1559   | Layout 1 | `fc444cb02004`  |
| 1554   | Layout 1 | `fc444cb02004`  |
| 1547   | Layout 1 | `fc444cb02004`  |
| 1537   | Layout 1 | `fc444cb02004`  |
| 1529   | Layout 1 | `fc444cb02004`  |
| 1524   | Layout 1 | `fc444cb02004`  |
| 1519   | Layout 1 | `fc444cb02004`  |
| 1509   | Layout 1 | `fc444cb02004`  |
| 1506   | Layout 1 | `fc444cb02004`  |
| 1504   | Layout 1 | `fc444cb02004`  |
| 1500   | Layout 1 | `fc444cb02004`  |
| 1493   | Layout 1 | `fc444cb02004`  |
| 1489   | Layout 1 | `fc444cb02004`  |
| 1485   | Layout 1 | `fc444cb02004`  |
| 1481   | Layout 1 | `fc444cb02004`  |
| 1474   | Layout 1 | `fc444cb02004`  |
| 1466   | Layout 1 | `fc444cb02004`  |
| 1462   | Layout 1 | `fc444cb02004`  |
| 1459   | Layout 1 | `fc444cb02004`  |
| 1453   | Layout 1 | `fc444cb02004`  |
| 1450   | Layout 1 | `fc444cb02004`  |
| 1445   | Layout 1 | `fc444cb02004`  |
| 1439   | Layout 1 | `fc444cb02004`  |
| 1433   | Layout 1 | `fc444cb02004`  |
| 1430   | Layout 1 | `fc444cb02004`  |
| 1426   | Layout 1 | `fc444cb02004`  |
| 1421   | Layout 1 | `fc444cb02004`  |
| 1417   | Layout 1 | `fc444cb02004`  |
| 1416   | Layout 1 | `fc444cb02004`  |
| 1409   | Layout 1 | `fc444cb02004`  |
| 1405   | Layout 1 | `fc444cb02004`  |
| 1401   | Layout 1 | `fc444cb02004`  |
| 1396   | Layout 1 | `fc444cb02004`  |
| 1391   | Layout 1 | `fc444cb02004`  |
| 1390   | Layout 1 | `fc444cb02004`  |
| 1386   | Layout 1 | `fc444cb02004`  |
| 1381   | Layout 1 | `fc444cb02004`  |
| 1379   | Layout 1 | `fc444cb02004`  |
| 1372   | Layout 1 | `fc444cb02004`  |
| 1366   | Layout 1 | `fc444cb02004`  |
| 1364   | Layout 1 | `fc444cb02004`  |
| 1363   | Layout 1 | `fc444cb02004`  |
| 1360   | Layout 1 | `fc444cb02004`  |
| 1358   | Layout 1 | `fc444cb02004`  |
| 1355   | Layout 1 | `fc444cb02004`  |
| 1351   | Layout 1 | `fc444cb02004`  |
| 1348   | Layout 1 | `fc444cb02004`  |
| 1346   | Layout 1 | `fc444cb02004`  |
| 1341   | Layout 1 | `fc444cb02004`  |
| 1340   | Layout 1 | `fc444cb02004`  |
| 1338   | Layout 1 | `fc444cb02004`  |
| 1335   | Layout 1 | `fc444cb02004`  |
| 1333   | Layout 1 | `fc444cb02004`  |
| 1329   | Layout 1 | `fc444cb02004`  |
| 1327   | No file  | `fc444cb02004`  |
| 1324   | No file  | `fc444cb02004`  |
| 1321   | No file  | `fc444cb02004`  |
| 1319   | No file  | `fc444cb02004`  |
| 1318   | No file  | `fc444cb02004`  |
| 1316   | No file  | `fc444cb02004`  |
| 1313   | No file  | `fc444cb02004`  |
| 1311   | Layout 1 | `fc444cb02004`  |
| 1309   | Layout 1 | `fc444cb02004`  |
| 1304   | Layout 1 | `fc444cb02004`  |
| 1292   | Layout 1 | `fc444cb02004`  |
| 1286   | Layout 1 | `fc444cb02004`  |
| 1280   | Layout 1 | `fc444cb02004`  |
| 1276   | Layout 1 | `fc444cb02004`  |
| 1267   | No file  | `fc444cb02004`  |
| 1261   | No file  | `fc444cb02004`  |
| 1256   | No file  | `fc444cb02004`  |
| 1250   | No file  | `fc444cb02004`  |
| 1246   | No file  | `fc444cb02004`  |
| 1239   | No file  | `fc444cb02004`  |
| 1230   | No file  | `fc444cb02004`  |
| 1226   | No file  | `fc444cb02004`  |
| 1220   | No file  | `fc444cb02004`  |
| 1217   | No file  | `fc444cb02004`  |
| 1211   | No file  | `fc444cb02004`  |
| 1210   | No file  | `fc444cb02004`  |
| 1208   | No file  | `fc444cb02004`  |
| 1203   | No file  | `fc444cb02004`  |
| 1197   | No file  | `fc444cb02004`  |
| 1194   | No file  | `fc444cb02004`  |
| 1192   | No file  | `fc444cb02004`  |
| 1187   | No file  | `fc444cb02004`  |
| 1183   | No file  | `fc444cb02004`  |
| 1177   | No file  | `fc444cb02004`  |
| 1173   | No file  | `fc444cb02004`  |
| 1167   | No file  | `fc444cb02004`  |
| 1164   | No file  | `fc444cb02004`  |
| 1156   | No file  | `fc444cb02004`  |
| 1149   | No file  | `fc444cb02004`  |
| 1144   | No file  | `fc444cb02004`  |
| 1137   | No file  | `fc444cb02004`  |
| 1132   | No file  | `fc444cb02004`  |
| 1127   | No file  | `fc444cb02004`  |
| 1122   | No file  | `fc444cb02004`  |
| 1118   | No file  | `fc444cb02004`  |
| 1114   | No file  | `fc444cb02004`  |
| 1109   | No file  | `fc444cb02004`  |
| 1102   | No file  | `fc444cb02004`  |
| 1096   | No file  | `fc444cb02004`  |
| 1088   | No file  | `fc444cb02004`  |
| 1081   | No file  | `fc444cb02004`  |
| 1076   | No file  | `fc444cb02004`  |
| 1069   | No file  | `fc444cb02004`  |
| 1064   | No file  | `fc444cb02004`  |
| 1058   | No file  | `fc444cb02004`  |
| 1051   | No file  | `fc444cb02004`  |
| 1044   | No file  | `fc444cb02004`  |
| 1036   | No file  | `fc444cb02004`  |
| 1026   | No file  | `fc444cb02004`  |
| 1016   | No file  | `fc444cb02004`  |
| 1009   | No file  | `fc444cb02004`  |
| 1005   | No file  | `fc444cb02004`  |
| 1000   | No file  | `fc444cb02004`  |
| 998    | No file  | `fc444cb02004`  |
| 990    | No file  | `fc444cb02004`  |
| 979    | No file  | `fc444cb02004`  |
| 972    | No file  | `fc444cb02004`  |
| 963    | No file  | `fc444cb02004`  |
| 955    | No file  | `fc444cb02004`  |
| 946    | No file  | `fc444cb02004`  |
| 938    | No file  | `fc444cb02004`  |
| 927    | No file  | `fc444cb02004`  |
| 911    | No file  | `fc444cb02004`  |
| 904    | No file  | `fc444cb02004`  |
| 899    | No file  | `fc444cb02004`  |
| 894    | No file  | `fc444cb02004`  |
| 885    | No file  | `fc444cb02004`  |
| 879    | No file  | `fc444cb02004`  |
| 872    | No file  | `fc444cb02004`  |
| 864    | No file  | `fc444cb02004`  |
| 855    | No file  | `fc444cb02004`  |
| 853    | No file  | `fc444cb02004`  |
| 845    | No file  | `fc444cb02004`  |
| 837    | No file  | `fc444cb02004`  |
| 829    | No file  | `fc444cb02004`  |
| 822    | No file  | `fc444cb02004`  |
| 814    | No file  | `fc444cb02004`  |
| 805    | No file  | `fc444cb02004`  |
| 794    | No file  | `fc444cb02004`  |
| 787    | No file  | `fc444cb02004`  |
| 780    | No file  | `fc444cb02004`  |
| 771    | No file  | `fc444cb02004`  |
| 760    | No file  | `fc444cb02004`  |
| 748    | No file  | `fc444cb02004`  |
| 741    | No file  | `fc444cb02004`  |
| 736    | No file  | `fc444cb02004`  |
| 731    | No file  | `fc444cb02004`  |
| 723    | No file  | `fc444cb02004`  |
| 711    | No file  | `fc444cb02004`  |
| 707    | No file  | `fc444cb02004`  |
| 697    | No file  | `fc444cb02004`  |
| 689    | No file  | `fc444cb02004`  |
| 683    | No file  | `fc444cb02004`  |
| 678    | No file  | `fc444cb02004`  |
| 670    | No file  | `fc444cb02004`  |
| 661    | No file  | `fc444cb02004`  |
| 656    | No file  | `fc444cb02004`  |
| 652    | No file  | `fc444cb02004`  |
| 643    | No file  | `fc444cb02004`  |
| 637    | No file  | `fc444cb02004`  |
| 630    | No file  | `fc444cb02004`  |
| 627    | No file  | `fc444cb02004`  |
| 621    | No file  | `fc444cb02004`  |
| 617    | No file  | `fc444cb02004`  |
| 615    | No file  | `fc444cb02004`  |
| 606    | No file  | `fc444cb02004`  |
| 599    | No file  | `fc444cb02004`  |
| 592    | No file  | `fc444cb02004`  |
| 586    | No file  | `fc444cb02004`  |
| 577    | No file  | `fc444cb02004`  |
| 569    | No file  | `fc444cb02004`  |
| 561    | No file  | `fc444cb02004`  |
| 554    | No file  | `fc444cb02004`  |
| 542    | No file  | `fc444cb02004`  |
| 532    | No file  | `fc444cb02004`  |
| 531    | No file  | `fc444cb02004`  |
| 526    | No file  | `fc444cb02004`  |
| 521    | No file  | `fc444cb02004`  |
| 517    | No file  | `fc444cb02004`  |
| 510    | No file  | `fc444cb02004`  |
| 508    | No file  | `fc444cb02004`  |
| 504    | No file  | `fc444cb02004`  |
| 497    | No file  | `fc444cb02004`  |
| 491    | No file  | `fc444cb02004`  |
| 485    | No file  | `fc444cb02004`  |
| 478    | No file  | `fc444cb02004`  |
| 472    | No file  | `fc444cb02004`  |
| 466    | No file  | `fc444cb02004`  |
| 457    | No file  | `fc444cb02004`  |
| 452    | No file  | `fc444cb02004`  |
| 449    | No file  | `fc444cb02004`  |
| 435    | No file  | `fc444cb02004`  |

<!-- versions:end -->

## Companion Files

None. The handler reads the keys in file order and does not need
`itemtradeoffset.dbss` (see below). Names and titles come from LOC type `6`
(`str_id4` `0` and `1`), else the Korean `characterstatic.dbss` ones
(`_common/character.py`).

All multi-byte values are little-endian.

## Layout 1

### File Layout

A bare table: no `PABR` magic and no string table. The file is exactly
`4 + 2 * count` bytes.

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of keys; `126` on client 3464         |
| `+0x04` | Row[count] | keys  | Character keys, unique, not sorted; see Row  |

### Row (2 bytes)

| Offset  | Type | Field        | Notes                                      |
| ------- | ---- | ------------ | ------------------------------------------ |
| `+0x00` | u16  | character_id | Character key, LOC type `6`                |

### `itemtradeoffset.dbss`

The bare u16 index layout of `petexpoffset.dbss`, read by
`parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type             | Field | Notes                                 |
| ------- | ---------------- | ----- | ------------------------------------- |
| `+0x00` | u32              | count | Equals the `itemtrade.dbss` count     |
| `+0x04` | Index Row[count] | rows  | No trailer; see Index Row             |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u16  | character_id | Row key                                                  |
| `+0x02` | u32  | offset       | Start of the key in `itemtrade.dbss` (`4 + 2 * row`)     |
| `+0x06` | u32  | size         | Always `2`, the key itself                               |

The index rows are in neither key nor file order; each points at its own key
in `itemtrade.dbss` (`test_every_offset_row_points_at_its_key`).

## Notes

- Titles on client 3464: 57 `<Trade Manager>`, 54 `<Node Management>`, 2
  `<Farm Owner>`, 12 single titles such as `<Acher Trade Manager>`,
  `<Katan Military - Trade Manager>` and `<Trader of Shakatu>`, and one key
  without a title (40075 Fish Dad).
- On client 3464 the file holds every character whose
  `characterfunction.dbss` buttons include Trade (122 keys), plus four more:
  47546 Taeseok, 47563 Gyeonghwan and 47600 Chunsu (`<Trade Manager>`, whose
  LOC type `32` button reads `Trading`) and 40075 Fish Dad.
- [`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md) and its offset table hold the same 126 keys on
  client 3464, in a different order.
- No NPC has a character icon in the `CHARACTER_ICON` index, so the table has
  no icon column.
- 40075 Fish Dad has no `characterfunction.dbss` record, no `npcsimply.bss`
  record and no title; `characterstatic.dbss` gives it only the action script
  `getknowledge(19);`. In game it reads as a removed or unused NPC, but in
  `itemtradegrouptonpc.dbss` its key holds 1,501 trade items on client 3464,
  where every other key holds one. I read 40075 as the holder of the default
  trade list; whether every trade NPC uses that list is open in the
  [`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md) doc.
