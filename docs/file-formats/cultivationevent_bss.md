# `cultivationevent.bss` Format

## Purpose

The farming event types: the keys of the `CultivationEventType_Table`
sheet, the events (pruning, insect removal, bird calls, wilting) a crop
can get. A u32 count follows the PABR magic, then one i16 key per entry.
On every client checked (1784 to 3474) the list is `1`, `0`. The event
ranges of the sheet are not in the client file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records        | Row bytes |
| ------ | -------------- | ---------------------- | ----- | -------------- | --------- |
| 1      | 1704 and later | `cultivationevent.bss` | 24    | 1 String Table | 4         |

| Layout | File                   | Known         | Unknown    |
| ------ | ---------------------- | ------------- | ---------- |
| 1      | `cultivationevent.bss` | 24 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `cdd38bd12573`  |
| 3482   | Layout 1 | `cdd38bd12573`  |
| 3474   | Layout 1 | `cdd38bd12573`  |
| 3473   | Layout 1 | `cdd38bd12573`  |
| 3464   | Layout 1 | `cdd38bd12573`  |
| 3458   | Layout 1 | `cdd38bd12573`  |
| 3454   | Layout 1 | `cdd38bd12573`  |
| 3444   | Layout 1 | `cdd38bd12573`  |
| 3435   | Layout 1 | `cdd38bd12573`  |
| 3426   | Layout 1 | `cdd38bd12573`  |
| 3418   | Layout 1 | `cdd38bd12573`  |
| 3412   | Layout 1 | `cdd38bd12573`  |
| 3402   | Layout 1 | `cdd38bd12573`  |
| 3396   | Layout 1 | `cdd38bd12573`  |
| 3387   | Layout 1 | `cdd38bd12573`  |
| 3381   | Layout 1 | `cdd38bd12573`  |
| 3373   | Layout 1 | `cdd38bd12573`  |
| 3364   | Layout 1 | `cdd38bd12573`  |
| 3356   | Layout 1 | `cdd38bd12573`  |
| 3349   | Layout 1 | `cdd38bd12573`  |
| 3342   | Layout 1 | `cdd38bd12573`  |
| 3335   | Layout 1 | `cdd38bd12573`  |
| 3326   | Layout 1 | `cdd38bd12573`  |
| 3321   | Layout 1 | `cdd38bd12573`  |
| 3314   | Layout 1 | `cdd38bd12573`  |
| 3303   | Layout 1 | `cdd38bd12573`  |
| 3302   | Layout 1 | `cdd38bd12573`  |
| 3293   | Layout 1 | `cdd38bd12573`  |
| 3283   | Layout 1 | `cdd38bd12573`  |
| 3275   | Layout 1 | `cdd38bd12573`  |
| 3267   | Layout 1 | `cdd38bd12573`  |
| 3258   | Layout 1 | `cdd38bd12573`  |
| 3251   | Layout 1 | `cdd38bd12573`  |
| 3242   | Layout 1 | `cdd38bd12573`  |
| 3235   | Layout 1 | `cdd38bd12573`  |
| 3229   | Layout 1 | `cdd38bd12573`  |
| 3212   | Layout 1 | `cdd38bd12573`  |
| 3203   | Layout 1 | `cdd38bd12573`  |
| 3193   | Layout 1 | `cdd38bd12573`  |
| 3186   | Layout 1 | `cdd38bd12573`  |
| 3177   | Layout 1 | `cdd38bd12573`  |
| 3169   | Layout 1 | `cdd38bd12573`  |
| 3158   | Layout 1 | `cdd38bd12573`  |
| 3151   | Layout 1 | `cdd38bd12573`  |
| 3144   | Layout 1 | `cdd38bd12573`  |
| 3133   | Layout 1 | `cdd38bd12573`  |
| 3125   | Layout 1 | `cdd38bd12573`  |
| 3118   | Layout 1 | `cdd38bd12573`  |
| 3111   | Layout 1 | `cdd38bd12573`  |
| 3103   | Layout 1 | `cdd38bd12573`  |
| 3095   | Layout 1 | `cdd38bd12573`  |
| 3086   | Layout 1 | `cdd38bd12573`  |
| 3072   | Layout 1 | `cdd38bd12573`  |
| 3062   | Layout 1 | `cdd38bd12573`  |
| 3052   | Layout 1 | `cdd38bd12573`  |
| 3045   | Layout 1 | `cdd38bd12573`  |
| 3037   | Layout 1 | `cdd38bd12573`  |
| 3030   | Layout 1 | `cdd38bd12573`  |
| 3021   | Layout 1 | `cdd38bd12573`  |
| 3012   | Layout 1 | `cdd38bd12573`  |
| 3002   | Layout 1 | `cdd38bd12573`  |
| 2995   | Layout 1 | `cdd38bd12573`  |
| 2987   | Layout 1 | `cdd38bd12573`  |
| 2978   | Layout 1 | `cdd38bd12573`  |
| 2970   | Layout 1 | `cdd38bd12573`  |
| 2959   | Layout 1 | `cdd38bd12573`  |
| 2951   | Layout 1 | `cdd38bd12573`  |
| 2942   | Layout 1 | `cdd38bd12573`  |
| 2935   | Layout 1 | `cdd38bd12573`  |
| 2932   | Layout 1 | `cdd38bd12573`  |
| 2923   | Layout 1 | `cdd38bd12573`  |
| 2919   | Layout 1 | `cdd38bd12573`  |
| 2907   | Layout 1 | `cdd38bd12573`  |
| 2900   | Layout 1 | `cdd38bd12573`  |
| 2891   | Layout 1 | `cdd38bd12573`  |
| 2882   | Layout 1 | `cdd38bd12573`  |
| 2872   | Layout 1 | `cdd38bd12573`  |
| 2863   | Layout 1 | `cdd38bd12573`  |
| 2855   | Layout 1 | `cdd38bd12573`  |
| 2849   | Layout 1 | `cdd38bd12573`  |
| 2844   | Layout 1 | `cdd38bd12573`  |
| 2834   | Layout 1 | `cdd38bd12573`  |
| 2825   | Layout 1 | `cdd38bd12573`  |
| 2819   | Layout 1 | `cdd38bd12573`  |
| 2811   | Layout 1 | `cdd38bd12573`  |
| 2803   | Layout 1 | `cdd38bd12573`  |
| 2794   | Layout 1 | `cdd38bd12573`  |
| 2783   | Layout 1 | `cdd38bd12573`  |
| 2774   | Layout 1 | `cdd38bd12573`  |
| 2765   | Layout 1 | `cdd38bd12573`  |
| 2756   | Layout 1 | `cdd38bd12573`  |
| 2750   | Layout 1 | `cdd38bd12573`  |
| 2743   | Layout 1 | `cdd38bd12573`  |
| 2736   | Layout 1 | `cdd38bd12573`  |
| 2726   | Layout 1 | `cdd38bd12573`  |
| 2717   | Layout 1 | `cdd38bd12573`  |
| 2709   | Layout 1 | `cdd38bd12573`  |
| 2703   | Layout 1 | `cdd38bd12573`  |
| 2695   | Layout 1 | `cdd38bd12573`  |
| 2684   | Layout 1 | `cdd38bd12573`  |
| 2672   | Layout 1 | `cdd38bd12573`  |
| 2665   | Layout 1 | `cdd38bd12573`  |
| 2657   | Layout 1 | `cdd38bd12573`  |
| 2649   | Layout 1 | `cdd38bd12573`  |
| 2644   | Layout 1 | `cdd38bd12573`  |
| 2637   | Layout 1 | `cdd38bd12573`  |
| 2629   | Layout 1 | `cdd38bd12573`  |
| 2619   | Layout 1 | `cdd38bd12573`  |
| 2612   | Layout 1 | `cdd38bd12573`  |
| 2606   | Layout 1 | `cdd38bd12573`  |
| 2602   | Layout 1 | `cdd38bd12573`  |
| 2601   | Layout 1 | `cdd38bd12573`  |
| 2592   | Layout 1 | `cdd38bd12573`  |
| 2583   | Layout 1 | `cdd38bd12573`  |
| 2575   | Layout 1 | `cdd38bd12573`  |
| 2567   | Layout 1 | `cdd38bd12573`  |
| 2560   | Layout 1 | `cdd38bd12573`  |
| 2553   | Layout 1 | `cdd38bd12573`  |
| 2545   | Layout 1 | `cdd38bd12573`  |
| 2538   | Layout 1 | `cdd38bd12573`  |
| 2529   | Layout 1 | `cdd38bd12573`  |
| 2519   | Layout 1 | `cdd38bd12573`  |
| 2513   | Layout 1 | `cdd38bd12573`  |
| 2510   | Layout 1 | `cdd38bd12573`  |
| 2507   | Layout 1 | `cdd38bd12573`  |
| 2503   | Layout 1 | `cdd38bd12573`  |
| 2498   | Layout 1 | `cdd38bd12573`  |
| 2492   | Layout 1 | `cdd38bd12573`  |
| 2487   | Layout 1 | `cdd38bd12573`  |
| 2480   | Layout 1 | `cdd38bd12573`  |
| 2474   | Layout 1 | `cdd38bd12573`  |
| 2468   | Layout 1 | `cdd38bd12573`  |
| 2460   | Layout 1 | `cdd38bd12573`  |
| 2453   | Layout 1 | `cdd38bd12573`  |
| 2444   | Layout 1 | `cdd38bd12573`  |
| 2438   | Layout 1 | `cdd38bd12573`  |
| 2434   | Layout 1 | `cdd38bd12573`  |
| 2429   | Layout 1 | `cdd38bd12573`  |
| 2421   | Layout 1 | `cdd38bd12573`  |
| 2414   | Layout 1 | `cdd38bd12573`  |
| 2407   | Layout 1 | `cdd38bd12573`  |
| 2401   | Layout 1 | `cdd38bd12573`  |
| 2397   | Layout 1 | `cdd38bd12573`  |
| 2393   | Layout 1 | `cdd38bd12573`  |
| 2384   | Layout 1 | `cdd38bd12573`  |
| 2378   | Layout 1 | `cdd38bd12573`  |
| 2372   | Layout 1 | `cdd38bd12573`  |
| 2358   | Layout 1 | `cdd38bd12573`  |
| 2352   | Layout 1 | `cdd38bd12573`  |
| 2347   | Layout 1 | `cdd38bd12573`  |
| 2343   | Layout 1 | `cdd38bd12573`  |
| 2335   | Layout 1 | `cdd38bd12573`  |
| 2327   | Layout 1 | `cdd38bd12573`  |
| 2324   | Layout 1 | `cdd38bd12573`  |
| 2319   | Layout 1 | `cdd38bd12573`  |
| 2313   | Layout 1 | `cdd38bd12573`  |
| 2308   | Layout 1 | `cdd38bd12573`  |
| 2302   | Layout 1 | `cdd38bd12573`  |
| 2295   | Layout 1 | `cdd38bd12573`  |
| 2290   | Layout 1 | `cdd38bd12573`  |
| 2284   | Layout 1 | `cdd38bd12573`  |
| 2276   | Layout 1 | `cdd38bd12573`  |
| 2269   | Layout 1 | `cdd38bd12573`  |
| 2259   | Layout 1 | `cdd38bd12573`  |
| 2250   | Layout 1 | `cdd38bd12573`  |
| 2243   | Layout 1 | `cdd38bd12573`  |
| 2235   | Layout 1 | `cdd38bd12573`  |
| 2229   | Layout 1 | `cdd38bd12573`  |
| 2224   | Layout 1 | `cdd38bd12573`  |
| 2218   | Layout 1 | `cdd38bd12573`  |
| 2215   | Layout 1 | `cdd38bd12573`  |
| 2207   | Layout 1 | `cdd38bd12573`  |
| 2203   | Layout 1 | `cdd38bd12573`  |
| 2196   | Layout 1 | `cdd38bd12573`  |
| 2192   | Layout 1 | `cdd38bd12573`  |
| 2189   | Layout 1 | `cdd38bd12573`  |
| 2183   | Layout 1 | `cdd38bd12573`  |
| 2179   | Layout 1 | `cdd38bd12573`  |
| 2171   | Layout 1 | `cdd38bd12573`  |
| 2163   | Layout 1 | `cdd38bd12573`  |
| 2156   | Layout 1 | `cdd38bd12573`  |
| 2151   | Layout 1 | `cdd38bd12573`  |
| 2147   | Layout 1 | `cdd38bd12573`  |
| 2142   | Layout 1 | `cdd38bd12573`  |
| 2138   | Layout 1 | `cdd38bd12573`  |
| 2134   | Layout 1 | `cdd38bd12573`  |
| 2130   | Layout 1 | `cdd38bd12573`  |
| 2122   | Layout 1 | `cdd38bd12573`  |
| 2107   | Layout 1 | `cdd38bd12573`  |
| 2098   | Layout 1 | `cdd38bd12573`  |
| 2089   | Layout 1 | `cdd38bd12573`  |
| 2081   | Layout 1 | `cdd38bd12573`  |
| 2073   | Layout 1 | `cdd38bd12573`  |
| 2067   | Layout 1 | `cdd38bd12573`  |
| 2063   | Layout 1 | `cdd38bd12573`  |
| 2059   | Layout 1 | `cdd38bd12573`  |
| 2052   | Layout 1 | `cdd38bd12573`  |
| 2044   | Layout 1 | `cdd38bd12573`  |
| 2039   | Layout 1 | `cdd38bd12573`  |
| 2032   | Layout 1 | `cdd38bd12573`  |
| 2025   | Layout 1 | `cdd38bd12573`  |
| 2011   | Layout 1 | `cdd38bd12573`  |
| 2005   | Layout 1 | `cdd38bd12573`  |
| 2000   | Layout 1 | `cdd38bd12573`  |
| 1996   | Layout 1 | `cdd38bd12573`  |
| 1991   | Layout 1 | `cdd38bd12573`  |
| 1985   | Layout 1 | `cdd38bd12573`  |
| 1980   | Layout 1 | `cdd38bd12573`  |
| 1969   | Layout 1 | `cdd38bd12573`  |
| 1964   | Layout 1 | `cdd38bd12573`  |
| 1958   | Layout 1 | `cdd38bd12573`  |
| 1950   | Layout 1 | `cdd38bd12573`  |
| 1945   | Layout 1 | `cdd38bd12573`  |
| 1937   | Layout 1 | `cdd38bd12573`  |
| 1933   | Layout 1 | `cdd38bd12573`  |
| 1927   | Layout 1 | `cdd38bd12573`  |
| 1921   | Layout 1 | `cdd38bd12573`  |
| 1914   | Layout 1 | `cdd38bd12573`  |
| 1908   | Layout 1 | `cdd38bd12573`  |
| 1897   | Layout 1 | `cdd38bd12573`  |
| 1892   | Layout 1 | `cdd38bd12573`  |
| 1886   | Layout 1 | `cdd38bd12573`  |
| 1881   | Layout 1 | `cdd38bd12573`  |
| 1871   | Layout 1 | `cdd38bd12573`  |
| 1866   | Layout 1 | `cdd38bd12573`  |
| 1862   | Layout 1 | `cdd38bd12573`  |
| 1854   | Layout 1 | `cdd38bd12573`  |
| 1846   | Layout 1 | `cdd38bd12573`  |
| 1838   | Layout 1 | `cdd38bd12573`  |
| 1832   | Layout 1 | `cdd38bd12573`  |
| 1826   | Layout 1 | `cdd38bd12573`  |
| 1822   | Layout 1 | `cdd38bd12573`  |
| 1818   | Layout 1 | `cdd38bd12573`  |
| 1804   | Layout 1 | `cdd38bd12573`  |
| 1794   | Layout 1 | `cdd38bd12573`  |
| 1790   | Layout 1 | `cdd38bd12573`  |
| 1784   | Layout 1 | `cdd38bd12573`  |
| 1774   | Layout 1 | `cdd38bd12573`  |
| 1771   | Layout 1 | `cdd38bd12573`  |
| 1762   | Layout 1 | `cdd38bd12573`  |
| 1759   | Layout 1 | `cdd38bd12573`  |
| 1754   | Layout 1 | `cdd38bd12573`  |
| 1749   | Layout 1 | `cdd38bd12573`  |
| 1743   | Layout 1 | `cdd38bd12573`  |
| 1737   | Layout 1 | `cdd38bd12573`  |
| 1731   | Layout 1 | `cdd38bd12573`  |
| 1725   | Layout 1 | `cdd38bd12573`  |
| 1717   | Layout 1 | `cdd38bd12573`  |
| 1710   | Layout 1 | `cdd38bd12573`  |
| 1704   | Layout 1 | `cdd38bd12573`  |
| 1698   | No file  | `cdd38bd12573`  |
| 1690   | No file  | `cdd38bd12573`  |
| 1685   | No file  | `cdd38bd12573`  |
| 1680   | No file  | `cdd38bd12573`  |
| 1674   | No file  | `cdd38bd12573`  |
| 1668   | No file  | `cdd38bd12573`  |
| 1659   | No file  | `cdd38bd12573`  |
| 1649   | No file  | `cdd38bd12573`  |
| 1642   | No file  | `cdd38bd12573`  |
| 1636   | No file  | `cdd38bd12573`  |
| 1628   | No file  | `cdd38bd12573`  |
| 1622   | No file  | `cdd38bd12573`  |
| 1614   | No file  | `cdd38bd12573`  |
| 1608   | No file  | `cdd38bd12573`  |
| 1602   | No file  | `cdd38bd12573`  |
| 1598   | No file  | `cdd38bd12573`  |
| 1594   | No file  | `cdd38bd12573`  |
| 1590   | No file  | `cdd38bd12573`  |
| 1587   | No file  | `cdd38bd12573`  |
| 1584   | No file  | `cdd38bd12573`  |
| 1579   | No file  | `cdd38bd12573`  |
| 1572   | No file  | `cdd38bd12573`  |
| 1565   | No file  | `cdd38bd12573`  |
| 1559   | No file  | `cdd38bd12573`  |
| 1554   | No file  | `cdd38bd12573`  |
| 1547   | No file  | `cdd38bd12573`  |
| 1537   | No file  | `cdd38bd12573`  |
| 1529   | No file  | `cdd38bd12573`  |
| 1524   | No file  | `cdd38bd12573`  |
| 1519   | No file  | `cdd38bd12573`  |
| 1509   | No file  | `cdd38bd12573`  |
| 1506   | No file  | `cdd38bd12573`  |
| 1504   | No file  | `cdd38bd12573`  |
| 1500   | No file  | `cdd38bd12573`  |
| 1493   | No file  | `cdd38bd12573`  |
| 1489   | No file  | `cdd38bd12573`  |
| 1485   | No file  | `cdd38bd12573`  |
| 1481   | No file  | `cdd38bd12573`  |
| 1474   | No file  | `cdd38bd12573`  |
| 1466   | No file  | `cdd38bd12573`  |
| 1462   | No file  | `cdd38bd12573`  |
| 1459   | No file  | `cdd38bd12573`  |
| 1453   | No file  | `cdd38bd12573`  |
| 1450   | No file  | `cdd38bd12573`  |
| 1445   | No file  | `cdd38bd12573`  |
| 1439   | No file  | `cdd38bd12573`  |
| 1433   | No file  | `cdd38bd12573`  |
| 1430   | No file  | `cdd38bd12573`  |
| 1426   | No file  | `cdd38bd12573`  |
| 1421   | No file  | `cdd38bd12573`  |
| 1417   | No file  | `cdd38bd12573`  |
| 1416   | No file  | `cdd38bd12573`  |
| 1409   | No file  | `cdd38bd12573`  |
| 1405   | No file  | `cdd38bd12573`  |
| 1401   | No file  | `cdd38bd12573`  |
| 1396   | No file  | `cdd38bd12573`  |
| 1391   | No file  | `cdd38bd12573`  |
| 1390   | No file  | `cdd38bd12573`  |
| 1386   | No file  | `cdd38bd12573`  |
| 1381   | No file  | `cdd38bd12573`  |
| 1379   | No file  | `cdd38bd12573`  |
| 1372   | No file  | `cdd38bd12573`  |
| 1366   | No file  | `cdd38bd12573`  |
| 1364   | No file  | `cdd38bd12573`  |
| 1363   | No file  | `cdd38bd12573`  |
| 1360   | No file  | `cdd38bd12573`  |
| 1358   | No file  | `cdd38bd12573`  |
| 1355   | No file  | `cdd38bd12573`  |
| 1351   | No file  | `cdd38bd12573`  |
| 1348   | No file  | `cdd38bd12573`  |
| 1346   | No file  | `cdd38bd12573`  |
| 1341   | No file  | `cdd38bd12573`  |
| 1340   | No file  | `cdd38bd12573`  |
| 1338   | No file  | `cdd38bd12573`  |
| 1335   | No file  | `cdd38bd12573`  |
| 1333   | No file  | `cdd38bd12573`  |
| 1329   | No file  | `cdd38bd12573`  |
| 1327   | No file  | `cdd38bd12573`  |
| 1324   | No file  | `cdd38bd12573`  |
| 1321   | No file  | `cdd38bd12573`  |
| 1319   | No file  | `cdd38bd12573`  |
| 1318   | No file  | `cdd38bd12573`  |
| 1316   | No file  | `cdd38bd12573`  |
| 1313   | No file  | `cdd38bd12573`  |
| 1311   | No file  | `cdd38bd12573`  |
| 1309   | No file  | `cdd38bd12573`  |
| 1304   | No file  | `cdd38bd12573`  |
| 1292   | No file  | `cdd38bd12573`  |
| 1286   | No file  | `cdd38bd12573`  |
| 1280   | No file  | `cdd38bd12573`  |
| 1276   | No file  | `cdd38bd12573`  |
| 1267   | No file  | `cdd38bd12573`  |
| 1261   | No file  | `cdd38bd12573`  |
| 1256   | No file  | `cdd38bd12573`  |
| 1250   | No file  | `cdd38bd12573`  |
| 1246   | No file  | `cdd38bd12573`  |
| 1239   | No file  | `cdd38bd12573`  |
| 1230   | No file  | `cdd38bd12573`  |
| 1226   | No file  | `cdd38bd12573`  |
| 1220   | No file  | `cdd38bd12573`  |
| 1217   | No file  | `cdd38bd12573`  |
| 1211   | No file  | `cdd38bd12573`  |
| 1210   | No file  | `cdd38bd12573`  |
| 1208   | No file  | `cdd38bd12573`  |
| 1203   | No file  | `cdd38bd12573`  |
| 1197   | No file  | `cdd38bd12573`  |
| 1194   | No file  | `cdd38bd12573`  |
| 1192   | No file  | `cdd38bd12573`  |
| 1187   | No file  | `cdd38bd12573`  |
| 1183   | No file  | `cdd38bd12573`  |
| 1177   | No file  | `cdd38bd12573`  |
| 1173   | No file  | `cdd38bd12573`  |
| 1167   | No file  | `cdd38bd12573`  |
| 1164   | No file  | `cdd38bd12573`  |
| 1156   | No file  | `cdd38bd12573`  |
| 1149   | No file  | `cdd38bd12573`  |
| 1144   | No file  | `cdd38bd12573`  |
| 1137   | No file  | `cdd38bd12573`  |
| 1132   | No file  | `cdd38bd12573`  |
| 1127   | No file  | `cdd38bd12573`  |
| 1122   | No file  | `cdd38bd12573`  |
| 1118   | No file  | `cdd38bd12573`  |
| 1114   | No file  | `cdd38bd12573`  |
| 1109   | No file  | `cdd38bd12573`  |
| 1102   | No file  | `cdd38bd12573`  |
| 1096   | No file  | `cdd38bd12573`  |
| 1088   | No file  | `cdd38bd12573`  |
| 1081   | No file  | `cdd38bd12573`  |
| 1076   | No file  | `cdd38bd12573`  |
| 1069   | No file  | `cdd38bd12573`  |
| 1064   | No file  | `cdd38bd12573`  |
| 1058   | No file  | `cdd38bd12573`  |
| 1051   | No file  | `cdd38bd12573`  |
| 1044   | No file  | `cdd38bd12573`  |
| 1036   | No file  | `cdd38bd12573`  |
| 1026   | No file  | `cdd38bd12573`  |
| 1016   | No file  | `cdd38bd12573`  |
| 1009   | No file  | `cdd38bd12573`  |
| 1005   | No file  | `cdd38bd12573`  |
| 1000   | No file  | `cdd38bd12573`  |
| 998    | No file  | `cdd38bd12573`  |
| 990    | No file  | `cdd38bd12573`  |
| 979    | No file  | `cdd38bd12573`  |
| 972    | No file  | `cdd38bd12573`  |
| 963    | No file  | `cdd38bd12573`  |
| 955    | No file  | `cdd38bd12573`  |
| 946    | No file  | `cdd38bd12573`  |
| 938    | No file  | `cdd38bd12573`  |
| 927    | No file  | `cdd38bd12573`  |
| 911    | No file  | `cdd38bd12573`  |
| 904    | No file  | `cdd38bd12573`  |
| 899    | No file  | `cdd38bd12573`  |
| 894    | No file  | `cdd38bd12573`  |
| 885    | No file  | `cdd38bd12573`  |
| 879    | No file  | `cdd38bd12573`  |
| 872    | No file  | `cdd38bd12573`  |
| 864    | No file  | `cdd38bd12573`  |
| 855    | No file  | `cdd38bd12573`  |
| 853    | No file  | `cdd38bd12573`  |
| 845    | No file  | `cdd38bd12573`  |
| 837    | No file  | `cdd38bd12573`  |
| 829    | No file  | `cdd38bd12573`  |
| 822    | No file  | `cdd38bd12573`  |
| 814    | No file  | `cdd38bd12573`  |
| 805    | No file  | `cdd38bd12573`  |
| 794    | No file  | `cdd38bd12573`  |
| 787    | No file  | `cdd38bd12573`  |
| 780    | No file  | `cdd38bd12573`  |
| 771    | No file  | `cdd38bd12573`  |
| 760    | No file  | `cdd38bd12573`  |
| 748    | No file  | `cdd38bd12573`  |
| 741    | No file  | `cdd38bd12573`  |
| 736    | No file  | `cdd38bd12573`  |
| 731    | No file  | `cdd38bd12573`  |
| 723    | No file  | `cdd38bd12573`  |
| 711    | No file  | `cdd38bd12573`  |
| 707    | No file  | `cdd38bd12573`  |
| 697    | No file  | `cdd38bd12573`  |
| 689    | No file  | `cdd38bd12573`  |
| 683    | No file  | `cdd38bd12573`  |
| 678    | No file  | `cdd38bd12573`  |
| 670    | No file  | `cdd38bd12573`  |
| 661    | No file  | `cdd38bd12573`  |
| 656    | No file  | `cdd38bd12573`  |
| 652    | No file  | `cdd38bd12573`  |
| 643    | No file  | `cdd38bd12573`  |
| 637    | No file  | `cdd38bd12573`  |
| 630    | No file  | `cdd38bd12573`  |
| 627    | No file  | `cdd38bd12573`  |
| 621    | No file  | `cdd38bd12573`  |
| 617    | No file  | `cdd38bd12573`  |
| 615    | No file  | `cdd38bd12573`  |
| 606    | No file  | `cdd38bd12573`  |
| 599    | No file  | `cdd38bd12573`  |
| 592    | No file  | `cdd38bd12573`  |
| 586    | No file  | `cdd38bd12573`  |
| 577    | No file  | `cdd38bd12573`  |
| 569    | No file  | `cdd38bd12573`  |
| 561    | No file  | `cdd38bd12573`  |
| 554    | No file  | `cdd38bd12573`  |
| 542    | No file  | `cdd38bd12573`  |
| 532    | No file  | `cdd38bd12573`  |
| 531    | No file  | `cdd38bd12573`  |
| 526    | No file  | `cdd38bd12573`  |
| 521    | No file  | `cdd38bd12573`  |
| 517    | No file  | `cdd38bd12573`  |
| 510    | No file  | `cdd38bd12573`  |
| 508    | No file  | `cdd38bd12573`  |
| 504    | No file  | `cdd38bd12573`  |
| 497    | No file  | `cdd38bd12573`  |
| 491    | No file  | `cdd38bd12573`  |
| 485    | No file  | `cdd38bd12573`  |
| 478    | No file  | `cdd38bd12573`  |
| 472    | No file  | `cdd38bd12573`  |
| 466    | No file  | `cdd38bd12573`  |
| 457    | No file  | `cdd38bd12573`  |
| 452    | No file  | `cdd38bd12573`  |
| 449    | No file  | `cdd38bd12573`  |
| 435    | No file  | `cdd38bd12573`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                   | Type             | Field                  | Notes                                                      |
| ------------------------ | ---------------- | ---------------------- | ---------------------------------------------------------- |
| `+0x00`                  | char[4]          | magic                  | ASCII `PABR`                                               |
| `+0x04`                  | u32              | type_count             | Number of event types                                      |
| `+0x08`                  | i16[type_count]  | cultivation_event_type | Event type key; unique, not in key order                   |
| `cultivation_event_type+0x00` | String Table | string_table           | See String Table                                           |
| `string_table+0x00`      | u32              | table_start            | Offset of the string table; `0x0C` on every client checked |
| `string_table+0x04`      | u32              | zero                   | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `CultivationEventType_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `CultivationEventType`,
`Pruning_Min`, `Pruning_Max`, `BugRemoval_Min`, `BugRemoval_Max`,
`BirdCall_Min`, `BirdCall_Max` and `Wilt_Harvest`, and two rows,
`CultivationEventType` `0` and `1`. The file holds those 2 of 2 keys and
none of the other columns; the client 1784 file is byte for byte the
private server's compiled `binary/cultivationevent.bss`.

The width comes from the server dump on client 1784: its RTTI names
`gc::CultivationEventStaticStatusManager`, a `StaticStatusManager` keyed by
`KeyType<short,-1>` (`KeyType@F$0?0@` in the mangled name), so the key is
an i16 with `-1` for no type. The loader is
`GameCommonParameterLoaderFromExcel::loadMain(loadCultivationEvent)`.

## Notes

- Raw bytes on clients 1784 to 3474:
  `50 41 42 52 02 00 00 00 01 00 00 00 00 00 00 00 0C 00 00 00 00 00 00 00`
  (24 bytes). The file is not in the archives of clients 794, 1230 and 1485.
- The `Object_Table` sheet on client 1784 has a `CultivationEventType`
  column too; one object (`1497`) holds `1`, the other 3,554 rows are empty.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per event type.
