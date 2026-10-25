# `bossmonsterhpsyncstaticstatus.bss` Format

## Purpose

Three boss characters, each with a key, a box of world sectors and two
unknown numbers. The name says "boss monster HP sync"; no client Lua names
the file, so what is synced and how is not known from the client.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                | Bytes | Records | Row bytes |
| ------ | -------------- | ----------------------------------- | ----- | ------- | --------- |
| 1      | 2284 and later | `bossmonsterhpsyncstaticstatus.bss` | 98    | 3 Row   | 26        |

| Layout | File                                | Known        | Unknown      |
| ------ | ----------------------------------- | ------------ | ------------ |
| 1      | `bossmonsterhpsyncstaticstatus.bss` | 80 B (81.6%) | 18 B (18.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `985fd9e2bc24`  |
| 3482   | Layout 1 | `985fd9e2bc24`  |
| 3474   | Layout 1 | `985fd9e2bc24`  |
| 3473   | Layout 1 | `985fd9e2bc24`  |
| 3464   | Layout 1 | `985fd9e2bc24`  |
| 3458   | Layout 1 | `985fd9e2bc24`  |
| 3454   | Layout 1 | `985fd9e2bc24`  |
| 3444   | Layout 1 | `985fd9e2bc24`  |
| 3435   | Layout 1 | `985fd9e2bc24`  |
| 3426   | Layout 1 | `985fd9e2bc24`  |
| 3418   | Layout 1 | `985fd9e2bc24`  |
| 3412   | Layout 1 | `985fd9e2bc24`  |
| 3402   | Layout 1 | `985fd9e2bc24`  |
| 3396   | Layout 1 | `985fd9e2bc24`  |
| 3387   | Layout 1 | `985fd9e2bc24`  |
| 3381   | Layout 1 | `985fd9e2bc24`  |
| 3373   | Layout 1 | `985fd9e2bc24`  |
| 3364   | Layout 1 | `985fd9e2bc24`  |
| 3356   | Layout 1 | `985fd9e2bc24`  |
| 3349   | Layout 1 | `985fd9e2bc24`  |
| 3342   | Layout 1 | `985fd9e2bc24`  |
| 3335   | Layout 1 | `985fd9e2bc24`  |
| 3326   | Layout 1 | `985fd9e2bc24`  |
| 3321   | Layout 1 | `985fd9e2bc24`  |
| 3314   | Layout 1 | `985fd9e2bc24`  |
| 3303   | Layout 1 | `985fd9e2bc24`  |
| 3302   | Layout 1 | `985fd9e2bc24`  |
| 3293   | Layout 1 | `985fd9e2bc24`  |
| 3283   | Layout 1 | `985fd9e2bc24`  |
| 3275   | Layout 1 | `985fd9e2bc24`  |
| 3267   | Layout 1 | `985fd9e2bc24`  |
| 3258   | Layout 1 | `985fd9e2bc24`  |
| 3251   | Layout 1 | `985fd9e2bc24`  |
| 3242   | Layout 1 | `985fd9e2bc24`  |
| 3235   | Layout 1 | `985fd9e2bc24`  |
| 3229   | Layout 1 | `985fd9e2bc24`  |
| 3212   | Layout 1 | `985fd9e2bc24`  |
| 3203   | Layout 1 | `985fd9e2bc24`  |
| 3193   | Layout 1 | `985fd9e2bc24`  |
| 3186   | Layout 1 | `985fd9e2bc24`  |
| 3177   | Layout 1 | `985fd9e2bc24`  |
| 3169   | Layout 1 | `985fd9e2bc24`  |
| 3158   | Layout 1 | `985fd9e2bc24`  |
| 3151   | Layout 1 | `985fd9e2bc24`  |
| 3144   | Layout 1 | `985fd9e2bc24`  |
| 3133   | Layout 1 | `985fd9e2bc24`  |
| 3125   | Layout 1 | `985fd9e2bc24`  |
| 3118   | Layout 1 | `985fd9e2bc24`  |
| 3111   | Layout 1 | `985fd9e2bc24`  |
| 3103   | Layout 1 | `985fd9e2bc24`  |
| 3095   | Layout 1 | `985fd9e2bc24`  |
| 3086   | Layout 1 | `985fd9e2bc24`  |
| 3072   | Layout 1 | `985fd9e2bc24`  |
| 3062   | Layout 1 | `985fd9e2bc24`  |
| 3052   | Layout 1 | `985fd9e2bc24`  |
| 3045   | Layout 1 | `985fd9e2bc24`  |
| 3037   | Layout 1 | `985fd9e2bc24`  |
| 3030   | Layout 1 | `985fd9e2bc24`  |
| 3021   | Layout 1 | `985fd9e2bc24`  |
| 3012   | Layout 1 | `985fd9e2bc24`  |
| 3002   | Layout 1 | `985fd9e2bc24`  |
| 2995   | Layout 1 | `985fd9e2bc24`  |
| 2987   | Layout 1 | `985fd9e2bc24`  |
| 2978   | Layout 1 | `985fd9e2bc24`  |
| 2970   | Layout 1 | `985fd9e2bc24`  |
| 2959   | Layout 1 | `985fd9e2bc24`  |
| 2951   | Layout 1 | `985fd9e2bc24`  |
| 2942   | Layout 1 | `985fd9e2bc24`  |
| 2935   | Layout 1 | `985fd9e2bc24`  |
| 2932   | Layout 1 | `985fd9e2bc24`  |
| 2923   | Layout 1 | `985fd9e2bc24`  |
| 2919   | Layout 1 | `985fd9e2bc24`  |
| 2907   | Layout 1 | `985fd9e2bc24`  |
| 2900   | Layout 1 | `985fd9e2bc24`  |
| 2891   | Layout 1 | `985fd9e2bc24`  |
| 2882   | Layout 1 | `985fd9e2bc24`  |
| 2872   | Layout 1 | `985fd9e2bc24`  |
| 2863   | Layout 1 | `985fd9e2bc24`  |
| 2855   | Layout 1 | `985fd9e2bc24`  |
| 2849   | Layout 1 | `985fd9e2bc24`  |
| 2844   | Layout 1 | `985fd9e2bc24`  |
| 2834   | Layout 1 | `985fd9e2bc24`  |
| 2825   | Layout 1 | `985fd9e2bc24`  |
| 2819   | Layout 1 | `985fd9e2bc24`  |
| 2811   | Layout 1 | `985fd9e2bc24`  |
| 2803   | Layout 1 | `985fd9e2bc24`  |
| 2794   | Layout 1 | `985fd9e2bc24`  |
| 2783   | Layout 1 | `985fd9e2bc24`  |
| 2774   | Layout 1 | `985fd9e2bc24`  |
| 2765   | Layout 1 | `985fd9e2bc24`  |
| 2756   | Layout 1 | `985fd9e2bc24`  |
| 2750   | Layout 1 | `985fd9e2bc24`  |
| 2743   | Layout 1 | `985fd9e2bc24`  |
| 2736   | Layout 1 | `985fd9e2bc24`  |
| 2726   | Layout 1 | `985fd9e2bc24`  |
| 2717   | Layout 1 | `985fd9e2bc24`  |
| 2709   | Layout 1 | `985fd9e2bc24`  |
| 2703   | Layout 1 | `985fd9e2bc24`  |
| 2695   | Layout 1 | `985fd9e2bc24`  |
| 2684   | Layout 1 | `985fd9e2bc24`  |
| 2672   | Layout 1 | `985fd9e2bc24`  |
| 2665   | Layout 1 | `985fd9e2bc24`  |
| 2657   | Layout 1 | `985fd9e2bc24`  |
| 2649   | Layout 1 | `985fd9e2bc24`  |
| 2644   | Layout 1 | `985fd9e2bc24`  |
| 2637   | Layout 1 | `985fd9e2bc24`  |
| 2629   | Layout 1 | `985fd9e2bc24`  |
| 2619   | Layout 1 | `985fd9e2bc24`  |
| 2612   | Layout 1 | `985fd9e2bc24`  |
| 2606   | Layout 1 | `985fd9e2bc24`  |
| 2602   | Layout 1 | `985fd9e2bc24`  |
| 2601   | Layout 1 | `985fd9e2bc24`  |
| 2592   | Layout 1 | `985fd9e2bc24`  |
| 2583   | Layout 1 | `985fd9e2bc24`  |
| 2575   | Layout 1 | `985fd9e2bc24`  |
| 2567   | Layout 1 | `985fd9e2bc24`  |
| 2560   | Layout 1 | `985fd9e2bc24`  |
| 2553   | Layout 1 | `985fd9e2bc24`  |
| 2545   | Layout 1 | `985fd9e2bc24`  |
| 2538   | Layout 1 | `985fd9e2bc24`  |
| 2529   | Layout 1 | `985fd9e2bc24`  |
| 2519   | Layout 1 | `985fd9e2bc24`  |
| 2513   | Layout 1 | `985fd9e2bc24`  |
| 2510   | Layout 1 | `985fd9e2bc24`  |
| 2507   | Layout 1 | `985fd9e2bc24`  |
| 2503   | Layout 1 | `985fd9e2bc24`  |
| 2498   | Layout 1 | `985fd9e2bc24`  |
| 2492   | Layout 1 | `985fd9e2bc24`  |
| 2487   | Layout 1 | `985fd9e2bc24`  |
| 2480   | Layout 1 | `985fd9e2bc24`  |
| 2474   | Layout 1 | `985fd9e2bc24`  |
| 2468   | Layout 1 | `985fd9e2bc24`  |
| 2460   | Layout 1 | `985fd9e2bc24`  |
| 2453   | Layout 1 | `985fd9e2bc24`  |
| 2444   | Layout 1 | `985fd9e2bc24`  |
| 2438   | Layout 1 | `985fd9e2bc24`  |
| 2434   | Layout 1 | `985fd9e2bc24`  |
| 2429   | Layout 1 | `985fd9e2bc24`  |
| 2421   | Layout 1 | `985fd9e2bc24`  |
| 2414   | Layout 1 | `985fd9e2bc24`  |
| 2407   | Layout 1 | `985fd9e2bc24`  |
| 2401   | Layout 1 | `985fd9e2bc24`  |
| 2397   | Layout 1 | `985fd9e2bc24`  |
| 2393   | Layout 1 | `985fd9e2bc24`  |
| 2384   | Layout 1 | `985fd9e2bc24`  |
| 2378   | Layout 1 | `985fd9e2bc24`  |
| 2372   | Layout 1 | `985fd9e2bc24`  |
| 2358   | Layout 1 | `985fd9e2bc24`  |
| 2352   | Layout 1 | `985fd9e2bc24`  |
| 2347   | Layout 1 | `985fd9e2bc24`  |
| 2343   | Layout 1 | `985fd9e2bc24`  |
| 2335   | Layout 1 | `985fd9e2bc24`  |
| 2327   | Layout 1 | `985fd9e2bc24`  |
| 2324   | Layout 1 | `985fd9e2bc24`  |
| 2319   | Layout 1 | `985fd9e2bc24`  |
| 2313   | Layout 1 | `985fd9e2bc24`  |
| 2308   | Layout 1 | `985fd9e2bc24`  |
| 2302   | Layout 1 | `985fd9e2bc24`  |
| 2295   | Layout 1 | `985fd9e2bc24`  |
| 2290   | Layout 1 | `985fd9e2bc24`  |
| 2284   | Layout 1 | `985fd9e2bc24`  |
| 2276   | No file  | `985fd9e2bc24`  |
| 2269   | No file  | `985fd9e2bc24`  |
| 2259   | No file  | `985fd9e2bc24`  |
| 2250   | No file  | `985fd9e2bc24`  |
| 2243   | No file  | `985fd9e2bc24`  |
| 2235   | No file  | `985fd9e2bc24`  |
| 2229   | No file  | `985fd9e2bc24`  |
| 2224   | No file  | `985fd9e2bc24`  |
| 2218   | No file  | `985fd9e2bc24`  |
| 2215   | No file  | `985fd9e2bc24`  |
| 2207   | No file  | `985fd9e2bc24`  |
| 2203   | No file  | `985fd9e2bc24`  |
| 2196   | No file  | `985fd9e2bc24`  |
| 2192   | No file  | `985fd9e2bc24`  |
| 2189   | No file  | `985fd9e2bc24`  |
| 2183   | No file  | `985fd9e2bc24`  |
| 2179   | No file  | `985fd9e2bc24`  |
| 2171   | No file  | `985fd9e2bc24`  |
| 2163   | No file  | `985fd9e2bc24`  |
| 2156   | No file  | `985fd9e2bc24`  |
| 2151   | No file  | `985fd9e2bc24`  |
| 2147   | No file  | `985fd9e2bc24`  |
| 2142   | No file  | `985fd9e2bc24`  |
| 2138   | No file  | `985fd9e2bc24`  |
| 2134   | No file  | `985fd9e2bc24`  |
| 2130   | No file  | `985fd9e2bc24`  |
| 2122   | No file  | `985fd9e2bc24`  |
| 2107   | No file  | `985fd9e2bc24`  |
| 2098   | No file  | `985fd9e2bc24`  |
| 2089   | No file  | `985fd9e2bc24`  |
| 2081   | No file  | `985fd9e2bc24`  |
| 2073   | No file  | `985fd9e2bc24`  |
| 2067   | No file  | `985fd9e2bc24`  |
| 2063   | No file  | `985fd9e2bc24`  |
| 2059   | No file  | `985fd9e2bc24`  |
| 2052   | No file  | `985fd9e2bc24`  |
| 2044   | No file  | `985fd9e2bc24`  |
| 2039   | No file  | `985fd9e2bc24`  |
| 2032   | No file  | `985fd9e2bc24`  |
| 2025   | No file  | `985fd9e2bc24`  |
| 2011   | No file  | `985fd9e2bc24`  |
| 2005   | No file  | `985fd9e2bc24`  |
| 2000   | No file  | `985fd9e2bc24`  |
| 1996   | No file  | `985fd9e2bc24`  |
| 1991   | No file  | `985fd9e2bc24`  |
| 1985   | No file  | `985fd9e2bc24`  |
| 1980   | No file  | `985fd9e2bc24`  |
| 1969   | No file  | `985fd9e2bc24`  |
| 1964   | No file  | `985fd9e2bc24`  |
| 1958   | No file  | `985fd9e2bc24`  |
| 1950   | No file  | `985fd9e2bc24`  |
| 1945   | No file  | `985fd9e2bc24`  |
| 1937   | No file  | `985fd9e2bc24`  |
| 1933   | No file  | `985fd9e2bc24`  |
| 1927   | No file  | `985fd9e2bc24`  |
| 1921   | No file  | `985fd9e2bc24`  |
| 1914   | No file  | `985fd9e2bc24`  |
| 1908   | No file  | `985fd9e2bc24`  |
| 1897   | No file  | `985fd9e2bc24`  |
| 1892   | No file  | `985fd9e2bc24`  |
| 1886   | No file  | `985fd9e2bc24`  |
| 1881   | No file  | `985fd9e2bc24`  |
| 1871   | No file  | `985fd9e2bc24`  |
| 1866   | No file  | `985fd9e2bc24`  |
| 1862   | No file  | `985fd9e2bc24`  |
| 1854   | No file  | `985fd9e2bc24`  |
| 1846   | No file  | `985fd9e2bc24`  |
| 1838   | No file  | `985fd9e2bc24`  |
| 1832   | No file  | `985fd9e2bc24`  |
| 1826   | No file  | `985fd9e2bc24`  |
| 1822   | No file  | `985fd9e2bc24`  |
| 1818   | No file  | `985fd9e2bc24`  |
| 1804   | No file  | `985fd9e2bc24`  |
| 1794   | No file  | `985fd9e2bc24`  |
| 1790   | No file  | `985fd9e2bc24`  |
| 1784   | No file  | `985fd9e2bc24`  |
| 1774   | No file  | `985fd9e2bc24`  |
| 1771   | No file  | `985fd9e2bc24`  |
| 1762   | No file  | `985fd9e2bc24`  |
| 1759   | No file  | `985fd9e2bc24`  |
| 1754   | No file  | `985fd9e2bc24`  |
| 1749   | No file  | `985fd9e2bc24`  |
| 1743   | No file  | `985fd9e2bc24`  |
| 1737   | No file  | `985fd9e2bc24`  |
| 1731   | No file  | `985fd9e2bc24`  |
| 1725   | No file  | `985fd9e2bc24`  |
| 1717   | No file  | `985fd9e2bc24`  |
| 1710   | No file  | `985fd9e2bc24`  |
| 1704   | No file  | `985fd9e2bc24`  |
| 1698   | No file  | `985fd9e2bc24`  |
| 1690   | No file  | `985fd9e2bc24`  |
| 1685   | No file  | `985fd9e2bc24`  |
| 1680   | No file  | `985fd9e2bc24`  |
| 1674   | No file  | `985fd9e2bc24`  |
| 1668   | No file  | `985fd9e2bc24`  |
| 1659   | No file  | `985fd9e2bc24`  |
| 1649   | No file  | `985fd9e2bc24`  |
| 1642   | No file  | `985fd9e2bc24`  |
| 1636   | No file  | `985fd9e2bc24`  |
| 1628   | No file  | `985fd9e2bc24`  |
| 1622   | No file  | `985fd9e2bc24`  |
| 1614   | No file  | `985fd9e2bc24`  |
| 1608   | No file  | `985fd9e2bc24`  |
| 1602   | No file  | `985fd9e2bc24`  |
| 1598   | No file  | `985fd9e2bc24`  |
| 1594   | No file  | `985fd9e2bc24`  |
| 1590   | No file  | `985fd9e2bc24`  |
| 1587   | No file  | `985fd9e2bc24`  |
| 1584   | No file  | `985fd9e2bc24`  |
| 1579   | No file  | `985fd9e2bc24`  |
| 1572   | No file  | `985fd9e2bc24`  |
| 1565   | No file  | `985fd9e2bc24`  |
| 1559   | No file  | `985fd9e2bc24`  |
| 1554   | No file  | `985fd9e2bc24`  |
| 1547   | No file  | `985fd9e2bc24`  |
| 1537   | No file  | `985fd9e2bc24`  |
| 1529   | No file  | `985fd9e2bc24`  |
| 1524   | No file  | `985fd9e2bc24`  |
| 1519   | No file  | `985fd9e2bc24`  |
| 1509   | No file  | `985fd9e2bc24`  |
| 1506   | No file  | `985fd9e2bc24`  |
| 1504   | No file  | `985fd9e2bc24`  |
| 1500   | No file  | `985fd9e2bc24`  |
| 1493   | No file  | `985fd9e2bc24`  |
| 1489   | No file  | `985fd9e2bc24`  |
| 1485   | No file  | `985fd9e2bc24`  |
| 1481   | No file  | `985fd9e2bc24`  |
| 1474   | No file  | `985fd9e2bc24`  |
| 1466   | No file  | `985fd9e2bc24`  |
| 1462   | No file  | `985fd9e2bc24`  |
| 1459   | No file  | `985fd9e2bc24`  |
| 1453   | No file  | `985fd9e2bc24`  |
| 1450   | No file  | `985fd9e2bc24`  |
| 1445   | No file  | `985fd9e2bc24`  |
| 1439   | No file  | `985fd9e2bc24`  |
| 1433   | No file  | `985fd9e2bc24`  |
| 1430   | No file  | `985fd9e2bc24`  |
| 1426   | No file  | `985fd9e2bc24`  |
| 1421   | No file  | `985fd9e2bc24`  |
| 1417   | No file  | `985fd9e2bc24`  |
| 1416   | No file  | `985fd9e2bc24`  |
| 1409   | No file  | `985fd9e2bc24`  |
| 1405   | No file  | `985fd9e2bc24`  |
| 1401   | No file  | `985fd9e2bc24`  |
| 1396   | No file  | `985fd9e2bc24`  |
| 1391   | No file  | `985fd9e2bc24`  |
| 1390   | No file  | `985fd9e2bc24`  |
| 1386   | No file  | `985fd9e2bc24`  |
| 1381   | No file  | `985fd9e2bc24`  |
| 1379   | No file  | `985fd9e2bc24`  |
| 1372   | No file  | `985fd9e2bc24`  |
| 1366   | No file  | `985fd9e2bc24`  |
| 1364   | No file  | `985fd9e2bc24`  |
| 1363   | No file  | `985fd9e2bc24`  |
| 1360   | No file  | `985fd9e2bc24`  |
| 1358   | No file  | `985fd9e2bc24`  |
| 1355   | No file  | `985fd9e2bc24`  |
| 1351   | No file  | `985fd9e2bc24`  |
| 1348   | No file  | `985fd9e2bc24`  |
| 1346   | No file  | `985fd9e2bc24`  |
| 1341   | No file  | `985fd9e2bc24`  |
| 1340   | No file  | `985fd9e2bc24`  |
| 1338   | No file  | `985fd9e2bc24`  |
| 1335   | No file  | `985fd9e2bc24`  |
| 1333   | No file  | `985fd9e2bc24`  |
| 1329   | No file  | `985fd9e2bc24`  |
| 1327   | No file  | `985fd9e2bc24`  |
| 1324   | No file  | `985fd9e2bc24`  |
| 1321   | No file  | `985fd9e2bc24`  |
| 1319   | No file  | `985fd9e2bc24`  |
| 1318   | No file  | `985fd9e2bc24`  |
| 1316   | No file  | `985fd9e2bc24`  |
| 1313   | No file  | `985fd9e2bc24`  |
| 1311   | No file  | `985fd9e2bc24`  |
| 1309   | No file  | `985fd9e2bc24`  |
| 1304   | No file  | `985fd9e2bc24`  |
| 1292   | No file  | `985fd9e2bc24`  |
| 1286   | No file  | `985fd9e2bc24`  |
| 1280   | No file  | `985fd9e2bc24`  |
| 1276   | No file  | `985fd9e2bc24`  |
| 1267   | No file  | `985fd9e2bc24`  |
| 1261   | No file  | `985fd9e2bc24`  |
| 1256   | No file  | `985fd9e2bc24`  |
| 1250   | No file  | `985fd9e2bc24`  |
| 1246   | No file  | `985fd9e2bc24`  |
| 1239   | No file  | `985fd9e2bc24`  |
| 1230   | No file  | `985fd9e2bc24`  |
| 1226   | No file  | `985fd9e2bc24`  |
| 1220   | No file  | `985fd9e2bc24`  |
| 1217   | No file  | `985fd9e2bc24`  |
| 1211   | No file  | `985fd9e2bc24`  |
| 1210   | No file  | `985fd9e2bc24`  |
| 1208   | No file  | `985fd9e2bc24`  |
| 1203   | No file  | `985fd9e2bc24`  |
| 1197   | No file  | `985fd9e2bc24`  |
| 1194   | No file  | `985fd9e2bc24`  |
| 1192   | No file  | `985fd9e2bc24`  |
| 1187   | No file  | `985fd9e2bc24`  |
| 1183   | No file  | `985fd9e2bc24`  |
| 1177   | No file  | `985fd9e2bc24`  |
| 1173   | No file  | `985fd9e2bc24`  |
| 1167   | No file  | `985fd9e2bc24`  |
| 1164   | No file  | `985fd9e2bc24`  |
| 1156   | No file  | `985fd9e2bc24`  |
| 1149   | No file  | `985fd9e2bc24`  |
| 1144   | No file  | `985fd9e2bc24`  |
| 1137   | No file  | `985fd9e2bc24`  |
| 1132   | No file  | `985fd9e2bc24`  |
| 1127   | No file  | `985fd9e2bc24`  |
| 1122   | No file  | `985fd9e2bc24`  |
| 1118   | No file  | `985fd9e2bc24`  |
| 1114   | No file  | `985fd9e2bc24`  |
| 1109   | No file  | `985fd9e2bc24`  |
| 1102   | No file  | `985fd9e2bc24`  |
| 1096   | No file  | `985fd9e2bc24`  |
| 1088   | No file  | `985fd9e2bc24`  |
| 1081   | No file  | `985fd9e2bc24`  |
| 1076   | No file  | `985fd9e2bc24`  |
| 1069   | No file  | `985fd9e2bc24`  |
| 1064   | No file  | `985fd9e2bc24`  |
| 1058   | No file  | `985fd9e2bc24`  |
| 1051   | No file  | `985fd9e2bc24`  |
| 1044   | No file  | `985fd9e2bc24`  |
| 1036   | No file  | `985fd9e2bc24`  |
| 1026   | No file  | `985fd9e2bc24`  |
| 1016   | No file  | `985fd9e2bc24`  |
| 1009   | No file  | `985fd9e2bc24`  |
| 1005   | No file  | `985fd9e2bc24`  |
| 1000   | No file  | `985fd9e2bc24`  |
| 998    | No file  | `985fd9e2bc24`  |
| 990    | No file  | `985fd9e2bc24`  |
| 979    | No file  | `985fd9e2bc24`  |
| 972    | No file  | `985fd9e2bc24`  |
| 963    | No file  | `985fd9e2bc24`  |
| 955    | No file  | `985fd9e2bc24`  |
| 946    | No file  | `985fd9e2bc24`  |
| 938    | No file  | `985fd9e2bc24`  |
| 927    | No file  | `985fd9e2bc24`  |
| 911    | No file  | `985fd9e2bc24`  |
| 904    | No file  | `985fd9e2bc24`  |
| 899    | No file  | `985fd9e2bc24`  |
| 894    | No file  | `985fd9e2bc24`  |
| 885    | No file  | `985fd9e2bc24`  |
| 879    | No file  | `985fd9e2bc24`  |
| 872    | No file  | `985fd9e2bc24`  |
| 864    | No file  | `985fd9e2bc24`  |
| 855    | No file  | `985fd9e2bc24`  |
| 853    | No file  | `985fd9e2bc24`  |
| 845    | No file  | `985fd9e2bc24`  |
| 837    | No file  | `985fd9e2bc24`  |
| 829    | No file  | `985fd9e2bc24`  |
| 822    | No file  | `985fd9e2bc24`  |
| 814    | No file  | `985fd9e2bc24`  |
| 805    | No file  | `985fd9e2bc24`  |
| 794    | No file  | `985fd9e2bc24`  |
| 787    | No file  | `985fd9e2bc24`  |
| 780    | No file  | `985fd9e2bc24`  |
| 771    | No file  | `985fd9e2bc24`  |
| 760    | No file  | `985fd9e2bc24`  |
| 748    | No file  | `985fd9e2bc24`  |
| 741    | No file  | `985fd9e2bc24`  |
| 736    | No file  | `985fd9e2bc24`  |
| 731    | No file  | `985fd9e2bc24`  |
| 723    | No file  | `985fd9e2bc24`  |
| 711    | No file  | `985fd9e2bc24`  |
| 707    | No file  | `985fd9e2bc24`  |
| 697    | No file  | `985fd9e2bc24`  |
| 689    | No file  | `985fd9e2bc24`  |
| 683    | No file  | `985fd9e2bc24`  |
| 678    | No file  | `985fd9e2bc24`  |
| 670    | No file  | `985fd9e2bc24`  |
| 661    | No file  | `985fd9e2bc24`  |
| 656    | No file  | `985fd9e2bc24`  |
| 652    | No file  | `985fd9e2bc24`  |
| 643    | No file  | `985fd9e2bc24`  |
| 637    | No file  | `985fd9e2bc24`  |
| 630    | No file  | `985fd9e2bc24`  |
| 627    | No file  | `985fd9e2bc24`  |
| 621    | No file  | `985fd9e2bc24`  |
| 617    | No file  | `985fd9e2bc24`  |
| 615    | No file  | `985fd9e2bc24`  |
| 606    | No file  | `985fd9e2bc24`  |
| 599    | No file  | `985fd9e2bc24`  |
| 592    | No file  | `985fd9e2bc24`  |
| 586    | No file  | `985fd9e2bc24`  |
| 577    | No file  | `985fd9e2bc24`  |
| 569    | No file  | `985fd9e2bc24`  |
| 561    | No file  | `985fd9e2bc24`  |
| 554    | No file  | `985fd9e2bc24`  |
| 542    | No file  | `985fd9e2bc24`  |
| 532    | No file  | `985fd9e2bc24`  |
| 531    | No file  | `985fd9e2bc24`  |
| 526    | No file  | `985fd9e2bc24`  |
| 521    | No file  | `985fd9e2bc24`  |
| 517    | No file  | `985fd9e2bc24`  |
| 510    | No file  | `985fd9e2bc24`  |
| 508    | No file  | `985fd9e2bc24`  |
| 504    | No file  | `985fd9e2bc24`  |
| 497    | No file  | `985fd9e2bc24`  |
| 491    | No file  | `985fd9e2bc24`  |
| 485    | No file  | `985fd9e2bc24`  |
| 478    | No file  | `985fd9e2bc24`  |
| 472    | No file  | `985fd9e2bc24`  |
| 466    | No file  | `985fd9e2bc24`  |
| 457    | No file  | `985fd9e2bc24`  |
| 452    | No file  | `985fd9e2bc24`  |
| 449    | No file  | `985fd9e2bc24`  |
| 435    | No file  | `985fd9e2bc24`  |

<!-- versions:end -->

## Companion Files

None. Names come from LOC type 6.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                 |
| ------------------- | -------------- | ------------ | ------------------------------------- |
| `+0x00`             | char[4]        | magic        | `PABR`                                |
| `+0x04`             | u32            | row_count    | `3` on client 3464                    |
| `+0x08`             | Row[row_count] | rows         | See Row                               |
| `rows+0x00`         | String Table   | string_table | The string table is empty             |
| `string_table+0x00` | u32            | table_start  | Where the rows end                    |
| `string_table+0x04` | u32            | zero         |                                       |

### Row (26 bytes)

| Offset  | Type | Field        | Notes                                                             |
| ------- | ---- | ------------ | ----------------------------------------------------------------- |
| `+0x00` | u16  | key          | `1, 3, 2` in file order on client 3464                            |
| `+0x02` | u16  | character_id | `characterstatic.dbss` character ID, LOC type 6                   |
| `+0x04` | i32  | min_x        | Sector box, lower corner; one sector is 12,800 world units, as in `instancefield.dbss` |
| `+0x08` | i32  | min_z        |                                                                   |
| `+0x0C` | i32  | max_x        | Upper corner; 2 above `min_x` on Garmoth and Baby Vell, 1 on Gift Box |
| `+0x10` | i32  | max_z        |                                                                   |
| `+0x14` | u16  | unknown_14   | `30` (Garmoth) or `10`                                            |
| `+0x16` | u32  | unknown_16   | `300000`, `1000000` or `800000`                                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Notes

- Garmoth's Boss Info position in
  [`bossinfostaicstatusmanager.bss`](bossinfostaicstatusmanager_bss.md)
  (x -21,954, z -324,742) is sector (-2, -26), inside Garmoth's box here.
  Gift Box's Boss Info position (x -12,325, z 37,767, sector (-1, 2)) is
  outside its box (2, 6) to (3, 7), so the box is not the Boss Info spot
  for every row. Baby Vell has no Boss Info record.
- Reading the four i32s as (min_x, max_x, min_z, max_z) puts a minimum
  above its maximum on Garmoth (-3, -27), so the order is
  (min_x, min_z, max_x, max_z).
- The Lua of the boss HP bar (`panel_widget_monsterbar_renew`,
  `panel_widget_enemygauge_new`) and of the Boss Info window
  (`ToClient_getBossHPPercent`, `ToClient_updateBossHPList`) reads HP from
  the client, not from this file.

## Open Questions

### unknown_14 and unknown_16

`unknown_14` is `30` on Garmoth and `10` on the other two; `unknown_16` is
`300000`, `1000000` and `800000`. They could be an interval and a range or
an HP threshold, but nothing in the client names them.

### Gift Box Box

Gift Box's sector box does not hold its Boss Info position. The event may
place the box elsewhere, or the box may mean something other than the
boss's area.
