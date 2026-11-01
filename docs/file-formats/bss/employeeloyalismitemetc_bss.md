# `employeeloyalismitemetc.bss` Format

## Purpose

A PABR file with 16 value bytes next to
[`employeeloyalismitem.dbss`](../dbss/employeeloyalismitem_dbss.md), the items
that restore a sailor's condition. Read as four u32 they are `2, 0, 2, 0`
on every client checked (1485 to 3474). No field is named yet.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes | Records        | Row bytes |
| ------ | -------------- | ----------------------------- | ----- | -------------- | --------- |
| 1      | 1239 and later | `employeeloyalismitemetc.bss` | 32    | 1 String Table | 4         |

| Layout | File                          | Known        | Unknown      |
| ------ | ----------------------------- | ------------ | ------------ |
| 1      | `employeeloyalismitemetc.bss` | 16 B (50.0%) | 16 B (50.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `89601366da6a`  |
| 3482   | Layout 1 | `89601366da6a`  |
| 3474   | Layout 1 | `89601366da6a`  |
| 3473   | Layout 1 | `89601366da6a`  |
| 3464   | Layout 1 | `89601366da6a`  |
| 3458   | Layout 1 | `89601366da6a`  |
| 3454   | Layout 1 | `89601366da6a`  |
| 3444   | Layout 1 | `89601366da6a`  |
| 3435   | Layout 1 | `89601366da6a`  |
| 3426   | Layout 1 | `89601366da6a`  |
| 3418   | Layout 1 | `89601366da6a`  |
| 3412   | Layout 1 | `89601366da6a`  |
| 3402   | Layout 1 | `89601366da6a`  |
| 3396   | Layout 1 | `89601366da6a`  |
| 3387   | Layout 1 | `89601366da6a`  |
| 3381   | Layout 1 | `89601366da6a`  |
| 3373   | Layout 1 | `89601366da6a`  |
| 3364   | Layout 1 | `89601366da6a`  |
| 3356   | Layout 1 | `89601366da6a`  |
| 3349   | Layout 1 | `89601366da6a`  |
| 3342   | Layout 1 | `89601366da6a`  |
| 3335   | Layout 1 | `89601366da6a`  |
| 3326   | Layout 1 | `89601366da6a`  |
| 3321   | Layout 1 | `89601366da6a`  |
| 3314   | Layout 1 | `89601366da6a`  |
| 3303   | Layout 1 | `89601366da6a`  |
| 3302   | Layout 1 | `89601366da6a`  |
| 3293   | Layout 1 | `89601366da6a`  |
| 3283   | Layout 1 | `89601366da6a`  |
| 3275   | Layout 1 | `89601366da6a`  |
| 3267   | Layout 1 | `89601366da6a`  |
| 3258   | Layout 1 | `89601366da6a`  |
| 3251   | Layout 1 | `89601366da6a`  |
| 3242   | Layout 1 | `89601366da6a`  |
| 3235   | Layout 1 | `89601366da6a`  |
| 3229   | Layout 1 | `89601366da6a`  |
| 3212   | Layout 1 | `89601366da6a`  |
| 3203   | Layout 1 | `89601366da6a`  |
| 3193   | Layout 1 | `89601366da6a`  |
| 3186   | Layout 1 | `89601366da6a`  |
| 3177   | Layout 1 | `89601366da6a`  |
| 3169   | Layout 1 | `89601366da6a`  |
| 3158   | Layout 1 | `89601366da6a`  |
| 3151   | Layout 1 | `89601366da6a`  |
| 3144   | Layout 1 | `89601366da6a`  |
| 3133   | Layout 1 | `89601366da6a`  |
| 3125   | Layout 1 | `89601366da6a`  |
| 3118   | Layout 1 | `89601366da6a`  |
| 3111   | Layout 1 | `89601366da6a`  |
| 3103   | Layout 1 | `89601366da6a`  |
| 3095   | Layout 1 | `89601366da6a`  |
| 3086   | Layout 1 | `89601366da6a`  |
| 3072   | Layout 1 | `89601366da6a`  |
| 3062   | Layout 1 | `89601366da6a`  |
| 3052   | Layout 1 | `89601366da6a`  |
| 3045   | Layout 1 | `89601366da6a`  |
| 3037   | Layout 1 | `89601366da6a`  |
| 3030   | Layout 1 | `89601366da6a`  |
| 3021   | Layout 1 | `89601366da6a`  |
| 3012   | Layout 1 | `89601366da6a`  |
| 3002   | Layout 1 | `89601366da6a`  |
| 2995   | Layout 1 | `89601366da6a`  |
| 2987   | Layout 1 | `89601366da6a`  |
| 2978   | Layout 1 | `89601366da6a`  |
| 2970   | Layout 1 | `89601366da6a`  |
| 2959   | Layout 1 | `89601366da6a`  |
| 2951   | Layout 1 | `89601366da6a`  |
| 2942   | Layout 1 | `89601366da6a`  |
| 2935   | Layout 1 | `89601366da6a`  |
| 2932   | Layout 1 | `89601366da6a`  |
| 2923   | Layout 1 | `89601366da6a`  |
| 2919   | Layout 1 | `89601366da6a`  |
| 2907   | Layout 1 | `89601366da6a`  |
| 2900   | Layout 1 | `89601366da6a`  |
| 2891   | Layout 1 | `89601366da6a`  |
| 2882   | Layout 1 | `89601366da6a`  |
| 2872   | Layout 1 | `89601366da6a`  |
| 2863   | Layout 1 | `89601366da6a`  |
| 2855   | Layout 1 | `89601366da6a`  |
| 2849   | Layout 1 | `89601366da6a`  |
| 2844   | Layout 1 | `89601366da6a`  |
| 2834   | Layout 1 | `89601366da6a`  |
| 2825   | Layout 1 | `89601366da6a`  |
| 2819   | Layout 1 | `89601366da6a`  |
| 2811   | Layout 1 | `89601366da6a`  |
| 2803   | Layout 1 | `89601366da6a`  |
| 2794   | Layout 1 | `89601366da6a`  |
| 2783   | Layout 1 | `89601366da6a`  |
| 2774   | Layout 1 | `89601366da6a`  |
| 2765   | Layout 1 | `89601366da6a`  |
| 2756   | Layout 1 | `89601366da6a`  |
| 2750   | Layout 1 | `89601366da6a`  |
| 2743   | Layout 1 | `89601366da6a`  |
| 2736   | Layout 1 | `89601366da6a`  |
| 2726   | Layout 1 | `89601366da6a`  |
| 2717   | Layout 1 | `89601366da6a`  |
| 2709   | Layout 1 | `89601366da6a`  |
| 2703   | Layout 1 | `89601366da6a`  |
| 2695   | Layout 1 | `89601366da6a`  |
| 2684   | Layout 1 | `89601366da6a`  |
| 2672   | Layout 1 | `89601366da6a`  |
| 2665   | Layout 1 | `89601366da6a`  |
| 2657   | Layout 1 | `89601366da6a`  |
| 2649   | Layout 1 | `89601366da6a`  |
| 2644   | Layout 1 | `89601366da6a`  |
| 2637   | Layout 1 | `89601366da6a`  |
| 2629   | Layout 1 | `89601366da6a`  |
| 2619   | Layout 1 | `89601366da6a`  |
| 2612   | Layout 1 | `89601366da6a`  |
| 2606   | Layout 1 | `89601366da6a`  |
| 2602   | Layout 1 | `89601366da6a`  |
| 2601   | Layout 1 | `89601366da6a`  |
| 2592   | Layout 1 | `89601366da6a`  |
| 2583   | Layout 1 | `89601366da6a`  |
| 2575   | Layout 1 | `89601366da6a`  |
| 2567   | Layout 1 | `89601366da6a`  |
| 2560   | Layout 1 | `89601366da6a`  |
| 2553   | Layout 1 | `89601366da6a`  |
| 2545   | Layout 1 | `89601366da6a`  |
| 2538   | Layout 1 | `89601366da6a`  |
| 2529   | Layout 1 | `89601366da6a`  |
| 2519   | Layout 1 | `89601366da6a`  |
| 2513   | Layout 1 | `89601366da6a`  |
| 2510   | Layout 1 | `89601366da6a`  |
| 2507   | Layout 1 | `89601366da6a`  |
| 2503   | Layout 1 | `89601366da6a`  |
| 2498   | Layout 1 | `89601366da6a`  |
| 2492   | Layout 1 | `89601366da6a`  |
| 2487   | Layout 1 | `89601366da6a`  |
| 2480   | Layout 1 | `89601366da6a`  |
| 2474   | Layout 1 | `89601366da6a`  |
| 2468   | Layout 1 | `89601366da6a`  |
| 2460   | Layout 1 | `89601366da6a`  |
| 2453   | Layout 1 | `89601366da6a`  |
| 2444   | Layout 1 | `89601366da6a`  |
| 2438   | Layout 1 | `89601366da6a`  |
| 2434   | Layout 1 | `89601366da6a`  |
| 2429   | Layout 1 | `89601366da6a`  |
| 2421   | Layout 1 | `89601366da6a`  |
| 2414   | Layout 1 | `89601366da6a`  |
| 2407   | Layout 1 | `89601366da6a`  |
| 2401   | Layout 1 | `89601366da6a`  |
| 2397   | Layout 1 | `89601366da6a`  |
| 2393   | Layout 1 | `89601366da6a`  |
| 2384   | Layout 1 | `89601366da6a`  |
| 2378   | Layout 1 | `89601366da6a`  |
| 2372   | Layout 1 | `89601366da6a`  |
| 2358   | Layout 1 | `89601366da6a`  |
| 2352   | Layout 1 | `89601366da6a`  |
| 2347   | Layout 1 | `89601366da6a`  |
| 2343   | Layout 1 | `89601366da6a`  |
| 2335   | Layout 1 | `89601366da6a`  |
| 2327   | Layout 1 | `89601366da6a`  |
| 2324   | Layout 1 | `89601366da6a`  |
| 2319   | Layout 1 | `89601366da6a`  |
| 2313   | Layout 1 | `89601366da6a`  |
| 2308   | Layout 1 | `89601366da6a`  |
| 2302   | Layout 1 | `89601366da6a`  |
| 2295   | Layout 1 | `89601366da6a`  |
| 2290   | Layout 1 | `89601366da6a`  |
| 2284   | Layout 1 | `89601366da6a`  |
| 2276   | Layout 1 | `89601366da6a`  |
| 2269   | Layout 1 | `89601366da6a`  |
| 2259   | Layout 1 | `89601366da6a`  |
| 2250   | Layout 1 | `89601366da6a`  |
| 2243   | Layout 1 | `89601366da6a`  |
| 2235   | Layout 1 | `89601366da6a`  |
| 2229   | Layout 1 | `89601366da6a`  |
| 2224   | Layout 1 | `89601366da6a`  |
| 2218   | Layout 1 | `89601366da6a`  |
| 2215   | Layout 1 | `89601366da6a`  |
| 2207   | Layout 1 | `89601366da6a`  |
| 2203   | Layout 1 | `89601366da6a`  |
| 2196   | Layout 1 | `89601366da6a`  |
| 2192   | Layout 1 | `89601366da6a`  |
| 2189   | Layout 1 | `89601366da6a`  |
| 2183   | Layout 1 | `89601366da6a`  |
| 2179   | Layout 1 | `89601366da6a`  |
| 2171   | Layout 1 | `89601366da6a`  |
| 2163   | Layout 1 | `89601366da6a`  |
| 2156   | Layout 1 | `89601366da6a`  |
| 2151   | Layout 1 | `89601366da6a`  |
| 2147   | Layout 1 | `89601366da6a`  |
| 2142   | Layout 1 | `89601366da6a`  |
| 2138   | Layout 1 | `89601366da6a`  |
| 2134   | Layout 1 | `89601366da6a`  |
| 2130   | Layout 1 | `89601366da6a`  |
| 2122   | Layout 1 | `89601366da6a`  |
| 2107   | Layout 1 | `89601366da6a`  |
| 2098   | Layout 1 | `89601366da6a`  |
| 2089   | Layout 1 | `89601366da6a`  |
| 2081   | Layout 1 | `89601366da6a`  |
| 2073   | Layout 1 | `89601366da6a`  |
| 2067   | Layout 1 | `89601366da6a`  |
| 2063   | Layout 1 | `89601366da6a`  |
| 2059   | Layout 1 | `89601366da6a`  |
| 2052   | Layout 1 | `89601366da6a`  |
| 2044   | Layout 1 | `89601366da6a`  |
| 2039   | Layout 1 | `89601366da6a`  |
| 2032   | Layout 1 | `89601366da6a`  |
| 2025   | Layout 1 | `89601366da6a`  |
| 2011   | Layout 1 | `89601366da6a`  |
| 2005   | Layout 1 | `89601366da6a`  |
| 2000   | Layout 1 | `89601366da6a`  |
| 1996   | Layout 1 | `89601366da6a`  |
| 1991   | Layout 1 | `89601366da6a`  |
| 1985   | Layout 1 | `89601366da6a`  |
| 1980   | Layout 1 | `89601366da6a`  |
| 1969   | Layout 1 | `89601366da6a`  |
| 1964   | Layout 1 | `89601366da6a`  |
| 1958   | Layout 1 | `89601366da6a`  |
| 1950   | Layout 1 | `89601366da6a`  |
| 1945   | Layout 1 | `89601366da6a`  |
| 1937   | Layout 1 | `89601366da6a`  |
| 1933   | Layout 1 | `89601366da6a`  |
| 1927   | Layout 1 | `89601366da6a`  |
| 1921   | Layout 1 | `89601366da6a`  |
| 1914   | Layout 1 | `89601366da6a`  |
| 1908   | Layout 1 | `89601366da6a`  |
| 1897   | Layout 1 | `89601366da6a`  |
| 1892   | Layout 1 | `89601366da6a`  |
| 1886   | Layout 1 | `89601366da6a`  |
| 1881   | Layout 1 | `89601366da6a`  |
| 1871   | Layout 1 | `89601366da6a`  |
| 1866   | Layout 1 | `89601366da6a`  |
| 1862   | Layout 1 | `89601366da6a`  |
| 1854   | Layout 1 | `89601366da6a`  |
| 1846   | Layout 1 | `89601366da6a`  |
| 1838   | Layout 1 | `89601366da6a`  |
| 1832   | Layout 1 | `89601366da6a`  |
| 1826   | Layout 1 | `89601366da6a`  |
| 1822   | Layout 1 | `89601366da6a`  |
| 1818   | Layout 1 | `89601366da6a`  |
| 1804   | Layout 1 | `89601366da6a`  |
| 1794   | Layout 1 | `89601366da6a`  |
| 1790   | Layout 1 | `89601366da6a`  |
| 1784   | Layout 1 | `89601366da6a`  |
| 1774   | Layout 1 | `89601366da6a`  |
| 1771   | Layout 1 | `89601366da6a`  |
| 1762   | Layout 1 | `89601366da6a`  |
| 1759   | Layout 1 | `89601366da6a`  |
| 1754   | Layout 1 | `89601366da6a`  |
| 1749   | Layout 1 | `89601366da6a`  |
| 1743   | Layout 1 | `89601366da6a`  |
| 1737   | Layout 1 | `89601366da6a`  |
| 1731   | Layout 1 | `89601366da6a`  |
| 1725   | Layout 1 | `89601366da6a`  |
| 1717   | Layout 1 | `89601366da6a`  |
| 1710   | Layout 1 | `89601366da6a`  |
| 1704   | Layout 1 | `89601366da6a`  |
| 1698   | Layout 1 | `89601366da6a`  |
| 1690   | Layout 1 | `89601366da6a`  |
| 1685   | Layout 1 | `89601366da6a`  |
| 1680   | Layout 1 | `89601366da6a`  |
| 1674   | Layout 1 | `89601366da6a`  |
| 1668   | Layout 1 | `89601366da6a`  |
| 1659   | Layout 1 | `89601366da6a`  |
| 1649   | Layout 1 | `89601366da6a`  |
| 1642   | Layout 1 | `89601366da6a`  |
| 1636   | Layout 1 | `89601366da6a`  |
| 1628   | Layout 1 | `89601366da6a`  |
| 1622   | Layout 1 | `89601366da6a`  |
| 1614   | Layout 1 | `89601366da6a`  |
| 1608   | Layout 1 | `89601366da6a`  |
| 1602   | Layout 1 | `89601366da6a`  |
| 1598   | Layout 1 | `89601366da6a`  |
| 1594   | Layout 1 | `89601366da6a`  |
| 1590   | Layout 1 | `89601366da6a`  |
| 1587   | Layout 1 | `89601366da6a`  |
| 1584   | Layout 1 | `89601366da6a`  |
| 1579   | Layout 1 | `89601366da6a`  |
| 1572   | Layout 1 | `89601366da6a`  |
| 1565   | Layout 1 | `89601366da6a`  |
| 1559   | Layout 1 | `89601366da6a`  |
| 1554   | Layout 1 | `89601366da6a`  |
| 1547   | Layout 1 | `89601366da6a`  |
| 1537   | Layout 1 | `89601366da6a`  |
| 1529   | Layout 1 | `89601366da6a`  |
| 1524   | Layout 1 | `89601366da6a`  |
| 1519   | Layout 1 | `89601366da6a`  |
| 1509   | Layout 1 | `89601366da6a`  |
| 1506   | Layout 1 | `89601366da6a`  |
| 1504   | Layout 1 | `89601366da6a`  |
| 1500   | Layout 1 | `89601366da6a`  |
| 1493   | Layout 1 | `89601366da6a`  |
| 1489   | Layout 1 | `89601366da6a`  |
| 1485   | Layout 1 | `89601366da6a`  |
| 1481   | Layout 1 | `89601366da6a`  |
| 1474   | Layout 1 | `89601366da6a`  |
| 1466   | Layout 1 | `89601366da6a`  |
| 1462   | Layout 1 | `89601366da6a`  |
| 1459   | Layout 1 | `89601366da6a`  |
| 1453   | Layout 1 | `89601366da6a`  |
| 1450   | Layout 1 | `89601366da6a`  |
| 1445   | Layout 1 | `89601366da6a`  |
| 1439   | Layout 1 | `89601366da6a`  |
| 1433   | Layout 1 | `89601366da6a`  |
| 1430   | Layout 1 | `89601366da6a`  |
| 1426   | Layout 1 | `89601366da6a`  |
| 1421   | Layout 1 | `89601366da6a`  |
| 1417   | Layout 1 | `89601366da6a`  |
| 1416   | Layout 1 | `89601366da6a`  |
| 1409   | Layout 1 | `89601366da6a`  |
| 1405   | Layout 1 | `89601366da6a`  |
| 1401   | Layout 1 | `89601366da6a`  |
| 1396   | Layout 1 | `89601366da6a`  |
| 1391   | Layout 1 | `89601366da6a`  |
| 1390   | Layout 1 | `89601366da6a`  |
| 1386   | Layout 1 | `89601366da6a`  |
| 1381   | Layout 1 | `89601366da6a`  |
| 1379   | Layout 1 | `89601366da6a`  |
| 1372   | Layout 1 | `89601366da6a`  |
| 1366   | Layout 1 | `89601366da6a`  |
| 1364   | Layout 1 | `89601366da6a`  |
| 1363   | Layout 1 | `89601366da6a`  |
| 1360   | Layout 1 | `89601366da6a`  |
| 1358   | Layout 1 | `89601366da6a`  |
| 1355   | Layout 1 | `89601366da6a`  |
| 1351   | Layout 1 | `89601366da6a`  |
| 1348   | Layout 1 | `89601366da6a`  |
| 1346   | Layout 1 | `89601366da6a`  |
| 1341   | Layout 1 | `89601366da6a`  |
| 1340   | Layout 1 | `89601366da6a`  |
| 1338   | Layout 1 | `89601366da6a`  |
| 1335   | Layout 1 | `89601366da6a`  |
| 1333   | Layout 1 | `89601366da6a`  |
| 1329   | Layout 1 | `89601366da6a`  |
| 1327   | Layout 1 | `89601366da6a`  |
| 1324   | Layout 1 | `89601366da6a`  |
| 1321   | Layout 1 | `89601366da6a`  |
| 1319   | Layout 1 | `89601366da6a`  |
| 1318   | Layout 1 | `89601366da6a`  |
| 1316   | Layout 1 | `89601366da6a`  |
| 1313   | Layout 1 | `89601366da6a`  |
| 1311   | Layout 1 | `89601366da6a`  |
| 1309   | Layout 1 | `89601366da6a`  |
| 1304   | Layout 1 | `89601366da6a`  |
| 1292   | Layout 1 | `89601366da6a`  |
| 1286   | Layout 1 | `89601366da6a`  |
| 1280   | Layout 1 | `89601366da6a`  |
| 1276   | Layout 1 | `89601366da6a`  |
| 1267   | Layout 1 | `89601366da6a`  |
| 1261   | Layout 1 | `89601366da6a`  |
| 1256   | Layout 1 | `89601366da6a`  |
| 1250   | Layout 1 | `89601366da6a`  |
| 1246   | Layout 1 | `89601366da6a`  |
| 1239   | Layout 1 | `89601366da6a`  |
| 1230   | No file  | `89601366da6a`  |
| 1226   | No file  | `89601366da6a`  |
| 1220   | No file  | `89601366da6a`  |
| 1217   | No file  | `89601366da6a`  |
| 1211   | No file  | `89601366da6a`  |
| 1210   | No file  | `89601366da6a`  |
| 1208   | No file  | `89601366da6a`  |
| 1203   | No file  | `89601366da6a`  |
| 1197   | No file  | `89601366da6a`  |
| 1194   | No file  | `89601366da6a`  |
| 1192   | No file  | `89601366da6a`  |
| 1187   | No file  | `89601366da6a`  |
| 1183   | No file  | `89601366da6a`  |
| 1177   | No file  | `89601366da6a`  |
| 1173   | No file  | `89601366da6a`  |
| 1167   | No file  | `89601366da6a`  |
| 1164   | No file  | `89601366da6a`  |
| 1156   | No file  | `89601366da6a`  |
| 1149   | No file  | `89601366da6a`  |
| 1144   | No file  | `89601366da6a`  |
| 1137   | No file  | `89601366da6a`  |
| 1132   | No file  | `89601366da6a`  |
| 1127   | No file  | `89601366da6a`  |
| 1122   | No file  | `89601366da6a`  |
| 1118   | No file  | `89601366da6a`  |
| 1114   | No file  | `89601366da6a`  |
| 1109   | No file  | `89601366da6a`  |
| 1102   | No file  | `89601366da6a`  |
| 1096   | No file  | `89601366da6a`  |
| 1088   | No file  | `89601366da6a`  |
| 1081   | No file  | `89601366da6a`  |
| 1076   | No file  | `89601366da6a`  |
| 1069   | No file  | `89601366da6a`  |
| 1064   | No file  | `89601366da6a`  |
| 1058   | No file  | `89601366da6a`  |
| 1051   | No file  | `89601366da6a`  |
| 1044   | No file  | `89601366da6a`  |
| 1036   | No file  | `89601366da6a`  |
| 1026   | No file  | `89601366da6a`  |
| 1016   | No file  | `89601366da6a`  |
| 1009   | No file  | `89601366da6a`  |
| 1005   | No file  | `89601366da6a`  |
| 1000   | No file  | `89601366da6a`  |
| 998    | No file  | `89601366da6a`  |
| 990    | No file  | `89601366da6a`  |
| 979    | No file  | `89601366da6a`  |
| 972    | No file  | `89601366da6a`  |
| 963    | No file  | `89601366da6a`  |
| 955    | No file  | `89601366da6a`  |
| 946    | No file  | `89601366da6a`  |
| 938    | No file  | `89601366da6a`  |
| 927    | No file  | `89601366da6a`  |
| 911    | No file  | `89601366da6a`  |
| 904    | No file  | `89601366da6a`  |
| 899    | No file  | `89601366da6a`  |
| 894    | No file  | `89601366da6a`  |
| 885    | No file  | `89601366da6a`  |
| 879    | No file  | `89601366da6a`  |
| 872    | No file  | `89601366da6a`  |
| 864    | No file  | `89601366da6a`  |
| 855    | No file  | `89601366da6a`  |
| 853    | No file  | `89601366da6a`  |
| 845    | No file  | `89601366da6a`  |
| 837    | No file  | `89601366da6a`  |
| 829    | No file  | `89601366da6a`  |
| 822    | No file  | `89601366da6a`  |
| 814    | No file  | `89601366da6a`  |
| 805    | No file  | `89601366da6a`  |
| 794    | No file  | `89601366da6a`  |
| 787    | No file  | `89601366da6a`  |
| 780    | No file  | `89601366da6a`  |
| 771    | No file  | `89601366da6a`  |
| 760    | No file  | `89601366da6a`  |
| 748    | No file  | `89601366da6a`  |
| 741    | No file  | `89601366da6a`  |
| 736    | No file  | `89601366da6a`  |
| 731    | No file  | `89601366da6a`  |
| 723    | No file  | `89601366da6a`  |
| 711    | No file  | `89601366da6a`  |
| 707    | No file  | `89601366da6a`  |
| 697    | No file  | `89601366da6a`  |
| 689    | No file  | `89601366da6a`  |
| 683    | No file  | `89601366da6a`  |
| 678    | No file  | `89601366da6a`  |
| 670    | No file  | `89601366da6a`  |
| 661    | No file  | `89601366da6a`  |
| 656    | No file  | `89601366da6a`  |
| 652    | No file  | `89601366da6a`  |
| 643    | No file  | `89601366da6a`  |
| 637    | No file  | `89601366da6a`  |
| 630    | No file  | `89601366da6a`  |
| 627    | No file  | `89601366da6a`  |
| 621    | No file  | `89601366da6a`  |
| 617    | No file  | `89601366da6a`  |
| 615    | No file  | `89601366da6a`  |
| 606    | No file  | `89601366da6a`  |
| 599    | No file  | `89601366da6a`  |
| 592    | No file  | `89601366da6a`  |
| 586    | No file  | `89601366da6a`  |
| 577    | No file  | `89601366da6a`  |
| 569    | No file  | `89601366da6a`  |
| 561    | No file  | `89601366da6a`  |
| 554    | No file  | `89601366da6a`  |
| 542    | No file  | `89601366da6a`  |
| 532    | No file  | `89601366da6a`  |
| 531    | No file  | `89601366da6a`  |
| 526    | No file  | `89601366da6a`  |
| 521    | No file  | `89601366da6a`  |
| 517    | No file  | `89601366da6a`  |
| 510    | No file  | `89601366da6a`  |
| 508    | No file  | `89601366da6a`  |
| 504    | No file  | `89601366da6a`  |
| 497    | No file  | `89601366da6a`  |
| 491    | No file  | `89601366da6a`  |
| 485    | No file  | `89601366da6a`  |
| 478    | No file  | `89601366da6a`  |
| 472    | No file  | `89601366da6a`  |
| 466    | No file  | `89601366da6a`  |
| 457    | No file  | `89601366da6a`  |
| 452    | No file  | `89601366da6a`  |
| 449    | No file  | `89601366da6a`  |
| 435    | No file  | `89601366da6a`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                                      |
| ------------------- | ------------ | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32          | unknown_04   | `2` on every client checked                                |
| `+0x08`             | u32          | unknown_08   | `0` on every client checked                                |
| `+0x0C`             | u32          | unknown_0c   | `2` on every client checked                                |
| `+0x10`             | u32          | unknown_10   | `0` on every client checked                                |
| `+0x14`             | String Table | string_table | See String Table                                           |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x14` on every client checked |
| `string_table+0x04` | u32          | zero         | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 1485 to 3474:
  `50 41 42 52 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00`
  (32 bytes). The file is not in the archives of clients 794 and 1230.
- The client 1784 file is byte for byte the private server's compiled
  `binary/employeeloyalismitemetc.bss` on that client, but no sheet of its
  `DataSheets.bexcel` matches: `Employee_Loyalism` (`Type`,
  `RecoveryItemKey`, `RecoveryCount`, 4 rows) compiles to
  `employeeloyalismitem.dbss`, and `Employee_Option` holds seven other
  sailor options. The server dump has `employeeLoyalismItem` and the
  loader `loadEmployeeLoyalismInfo`, but no `Etc` name.
- The four u32 are a reading of the bytes; each `0` could be part of a
  wider or narrower field.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. With no
  confirmed field, the preview shows the raw value bytes.

## Open Questions

### What the Values Count

`employeeloyalismitem.dbss` has two items of each loyalism type (type `0`
Chowder and Raisin Bread, type `1` Elixir of Regeneration and Tears of the
Star), so each `2` may be the item count of one type. The client 3474
sailor preset window (`panel_window_sailorpresetmanager_all_2.luac`) reads
two such counts: `ToClient_getRecoveryItemCount()` for the Loyalty items
(type `0`, slots `Static_RecoverySlotBg1` to `N`) and
`ToClient_getResurrectionItemCount()` for the resurrection items (type
`1`, slots `Static_TreatmentSlotBg1` to `N`). That fits `unknown_04` and
`unknown_0c` as these two counts in type order, but the client may as well
count the `employeeloyalismitem.dbss` rows of each type, which also gives
`2` and `2`. The bytes also read as two counted u32 lists (`[0, 2]` and an
empty one). Read as a u32 count `2` and two 6-byte entries (u32 item, u16
value) the item keys are `0`, which no item has, so that reading is
unlikely. A patch that changes the item count of one type would show
whether the file follows it.
