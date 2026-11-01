# `seasonpassquestlist.bss` Format

## Purpose

Quest lists of the Black Spirit Pass (season pass) window. Three files share one layout, the packed quest ID list of [`allquestlist.bss`](allquestlist_bss.md), and one handler:

| File                               | Holds                                                         |
| ---------------------------------- | ------------------------------------------------------------- |
| `seasonpassquestlistfornormal.bss` | The free quest of each pass row                               |
| `seasonpassquestlistforcash.bss`   | The Black Spirit Pass (premium) quest of each pass row        |
| `seasonpassquestlist.bss`          | Both: every quest of the two files above, in another order    |

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes | Records   | Row bytes |
| ------ | -------------- | ---------------------------------- | ----- | --------- | --------- |
| 1      | 1327 and later | `seasonpassquestlist.bss`          | 1,660 | 410 Entry | 4         |
| 1      | 1381 and later | `seasonpassquestlistforcash.bss`   | 840   | 205 Entry | 4         |
| 1      | 1381 and later | `seasonpassquestlistfornormal.bss` | 840   | 205 Entry | 4         |

| Layout | File                               | Known            | Unknown    |
| ------ | ---------------------------------- | ---------------- | ---------- |
| 1      | `seasonpassquestlist.bss`          | 1,660 B (100.0%) | 0 B (0.0%) |
| 1      | `seasonpassquestlistforcash.bss`   | 840 B (100.0%)   | 0 B (0.0%) |
| 1      | `seasonpassquestlistfornormal.bss` | 840 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c704d11112ce`  |
| 3482   | Layout 1 | `c704d11112ce`  |
| 3474   | Layout 1 | `c704d11112ce`  |
| 3473   | Layout 1 | `c704d11112ce`  |
| 3464   | Layout 1 | `c704d11112ce`  |
| 3458   | Layout 1 | `c704d11112ce`  |
| 3454   | Layout 1 | `c704d11112ce`  |
| 3444   | Layout 1 | `c704d11112ce`  |
| 3435   | Layout 1 | `c704d11112ce`  |
| 3426   | Layout 1 | `c704d11112ce`  |
| 3418   | Layout 1 | `c704d11112ce`  |
| 3412   | Layout 1 | `c704d11112ce`  |
| 3402   | Layout 1 | `c704d11112ce`  |
| 3396   | Layout 1 | `c704d11112ce`  |
| 3387   | Layout 1 | `c704d11112ce`  |
| 3381   | Layout 1 | `c704d11112ce`  |
| 3373   | Layout 1 | `c704d11112ce`  |
| 3364   | Layout 1 | `c704d11112ce`  |
| 3356   | Layout 1 | `c704d11112ce`  |
| 3349   | Layout 1 | `c704d11112ce`  |
| 3342   | Layout 1 | `c704d11112ce`  |
| 3335   | Layout 1 | `c704d11112ce`  |
| 3326   | Layout 1 | `c704d11112ce`  |
| 3321   | Layout 1 | `c704d11112ce`  |
| 3314   | Layout 1 | `c704d11112ce`  |
| 3303   | Layout 1 | `c704d11112ce`  |
| 3302   | Layout 1 | `c704d11112ce`  |
| 3293   | Layout 1 | `c704d11112ce`  |
| 3283   | Layout 1 | `c704d11112ce`  |
| 3275   | Layout 1 | `c704d11112ce`  |
| 3267   | Layout 1 | `c704d11112ce`  |
| 3258   | Layout 1 | `c704d11112ce`  |
| 3251   | Layout 1 | `c704d11112ce`  |
| 3242   | Layout 1 | `c704d11112ce`  |
| 3235   | Layout 1 | `c704d11112ce`  |
| 3229   | Layout 1 | `c704d11112ce`  |
| 3212   | Layout 1 | `c704d11112ce`  |
| 3203   | Layout 1 | `c704d11112ce`  |
| 3193   | Layout 1 | `c704d11112ce`  |
| 3186   | Layout 1 | `c704d11112ce`  |
| 3177   | Layout 1 | `c704d11112ce`  |
| 3169   | Layout 1 | `c704d11112ce`  |
| 3158   | Layout 1 | `c704d11112ce`  |
| 3151   | Layout 1 | `c704d11112ce`  |
| 3144   | Layout 1 | `c704d11112ce`  |
| 3133   | Layout 1 | `c704d11112ce`  |
| 3125   | Layout 1 | `c704d11112ce`  |
| 3118   | Layout 1 | `c704d11112ce`  |
| 3111   | Layout 1 | `c704d11112ce`  |
| 3103   | Layout 1 | `c704d11112ce`  |
| 3095   | Layout 1 | `c704d11112ce`  |
| 3086   | Layout 1 | `c704d11112ce`  |
| 3072   | Layout 1 | `c704d11112ce`  |
| 3062   | Layout 1 | `c704d11112ce`  |
| 3052   | Layout 1 | `c704d11112ce`  |
| 3045   | Layout 1 | `c704d11112ce`  |
| 3037   | Layout 1 | `c704d11112ce`  |
| 3030   | Layout 1 | `c704d11112ce`  |
| 3021   | Layout 1 | `c704d11112ce`  |
| 3012   | Layout 1 | `c704d11112ce`  |
| 3002   | Layout 1 | `c704d11112ce`  |
| 2995   | Layout 1 | `c704d11112ce`  |
| 2987   | Layout 1 | `c704d11112ce`  |
| 2978   | Layout 1 | `c704d11112ce`  |
| 2970   | Layout 1 | `c704d11112ce`  |
| 2959   | Layout 1 | `c704d11112ce`  |
| 2951   | Layout 1 | `c704d11112ce`  |
| 2942   | Layout 1 | `c704d11112ce`  |
| 2935   | Layout 1 | `c704d11112ce`  |
| 2932   | Layout 1 | `c704d11112ce`  |
| 2923   | Layout 1 | `c704d11112ce`  |
| 2919   | Layout 1 | `c704d11112ce`  |
| 2907   | Layout 1 | `c704d11112ce`  |
| 2900   | Layout 1 | `c704d11112ce`  |
| 2891   | Layout 1 | `c704d11112ce`  |
| 2882   | Layout 1 | `c704d11112ce`  |
| 2872   | Layout 1 | `c704d11112ce`  |
| 2863   | Layout 1 | `c704d11112ce`  |
| 2855   | Layout 1 | `c704d11112ce`  |
| 2849   | Layout 1 | `c704d11112ce`  |
| 2844   | Layout 1 | `c704d11112ce`  |
| 2834   | Layout 1 | `c704d11112ce`  |
| 2825   | Layout 1 | `c704d11112ce`  |
| 2819   | Layout 1 | `c704d11112ce`  |
| 2811   | Layout 1 | `c704d11112ce`  |
| 2803   | Layout 1 | `c704d11112ce`  |
| 2794   | Layout 1 | `c704d11112ce`  |
| 2783   | Layout 1 | `c704d11112ce`  |
| 2774   | Layout 1 | `c704d11112ce`  |
| 2765   | Layout 1 | `c704d11112ce`  |
| 2756   | Layout 1 | `c704d11112ce`  |
| 2750   | Layout 1 | `c704d11112ce`  |
| 2743   | Layout 1 | `c704d11112ce`  |
| 2736   | Layout 1 | `c704d11112ce`  |
| 2726   | Layout 1 | `c704d11112ce`  |
| 2717   | Layout 1 | `c704d11112ce`  |
| 2709   | Layout 1 | `c704d11112ce`  |
| 2703   | Layout 1 | `c704d11112ce`  |
| 2695   | Layout 1 | `c704d11112ce`  |
| 2684   | Layout 1 | `c704d11112ce`  |
| 2672   | Layout 1 | `c704d11112ce`  |
| 2665   | Layout 1 | `c704d11112ce`  |
| 2657   | Layout 1 | `c704d11112ce`  |
| 2649   | Layout 1 | `c704d11112ce`  |
| 2644   | Layout 1 | `c704d11112ce`  |
| 2637   | Layout 1 | `c704d11112ce`  |
| 2629   | Layout 1 | `c704d11112ce`  |
| 2619   | Layout 1 | `c704d11112ce`  |
| 2612   | Layout 1 | `c704d11112ce`  |
| 2606   | Layout 1 | `c704d11112ce`  |
| 2602   | Layout 1 | `c704d11112ce`  |
| 2601   | Layout 1 | `c704d11112ce`  |
| 2592   | Layout 1 | `c704d11112ce`  |
| 2583   | Layout 1 | `c704d11112ce`  |
| 2575   | Layout 1 | `c704d11112ce`  |
| 2567   | Layout 1 | `c704d11112ce`  |
| 2560   | Layout 1 | `c704d11112ce`  |
| 2553   | Layout 1 | `c704d11112ce`  |
| 2545   | Layout 1 | `c704d11112ce`  |
| 2538   | Layout 1 | `c704d11112ce`  |
| 2529   | Layout 1 | `c704d11112ce`  |
| 2519   | Layout 1 | `c704d11112ce`  |
| 2513   | Layout 1 | `c704d11112ce`  |
| 2510   | Layout 1 | `c704d11112ce`  |
| 2507   | Layout 1 | `c704d11112ce`  |
| 2503   | Layout 1 | `c704d11112ce`  |
| 2498   | Layout 1 | `c704d11112ce`  |
| 2492   | Layout 1 | `c704d11112ce`  |
| 2487   | Layout 1 | `c704d11112ce`  |
| 2480   | Layout 1 | `c704d11112ce`  |
| 2474   | Layout 1 | `c704d11112ce`  |
| 2468   | Layout 1 | `c704d11112ce`  |
| 2460   | Layout 1 | `c704d11112ce`  |
| 2453   | Layout 1 | `c704d11112ce`  |
| 2444   | Layout 1 | `c704d11112ce`  |
| 2438   | Layout 1 | `c704d11112ce`  |
| 2434   | Layout 1 | `c704d11112ce`  |
| 2429   | Layout 1 | `c704d11112ce`  |
| 2421   | Layout 1 | `c704d11112ce`  |
| 2414   | Layout 1 | `c704d11112ce`  |
| 2407   | Layout 1 | `c704d11112ce`  |
| 2401   | Layout 1 | `c704d11112ce`  |
| 2397   | Layout 1 | `c704d11112ce`  |
| 2393   | Layout 1 | `c704d11112ce`  |
| 2384   | Layout 1 | `c704d11112ce`  |
| 2378   | Layout 1 | `c704d11112ce`  |
| 2372   | Layout 1 | `c704d11112ce`  |
| 2358   | Layout 1 | `c704d11112ce`  |
| 2352   | Layout 1 | `c704d11112ce`  |
| 2347   | Layout 1 | `c704d11112ce`  |
| 2343   | Layout 1 | `c704d11112ce`  |
| 2335   | Layout 1 | `c704d11112ce`  |
| 2327   | Layout 1 | `c704d11112ce`  |
| 2324   | Layout 1 | `c704d11112ce`  |
| 2319   | Layout 1 | `c704d11112ce`  |
| 2313   | Layout 1 | `c704d11112ce`  |
| 2308   | Layout 1 | `c704d11112ce`  |
| 2302   | Layout 1 | `c704d11112ce`  |
| 2295   | Layout 1 | `c704d11112ce`  |
| 2290   | Layout 1 | `c704d11112ce`  |
| 2284   | Layout 1 | `c704d11112ce`  |
| 2276   | Layout 1 | `c704d11112ce`  |
| 2269   | Layout 1 | `c704d11112ce`  |
| 2259   | Layout 1 | `c704d11112ce`  |
| 2250   | Layout 1 | `c704d11112ce`  |
| 2243   | Layout 1 | `c704d11112ce`  |
| 2235   | Layout 1 | `c704d11112ce`  |
| 2229   | Layout 1 | `c704d11112ce`  |
| 2224   | Layout 1 | `c704d11112ce`  |
| 2218   | Layout 1 | `c704d11112ce`  |
| 2215   | Layout 1 | `c704d11112ce`  |
| 2207   | Layout 1 | `c704d11112ce`  |
| 2203   | Layout 1 | `c704d11112ce`  |
| 2196   | Layout 1 | `c704d11112ce`  |
| 2192   | Layout 1 | `c704d11112ce`  |
| 2189   | Layout 1 | `c704d11112ce`  |
| 2183   | Layout 1 | `c704d11112ce`  |
| 2179   | Layout 1 | `c704d11112ce`  |
| 2171   | Layout 1 | `c704d11112ce`  |
| 2163   | Layout 1 | `c704d11112ce`  |
| 2156   | Layout 1 | `c704d11112ce`  |
| 2151   | Layout 1 | `c704d11112ce`  |
| 2147   | Layout 1 | `c704d11112ce`  |
| 2142   | Layout 1 | `c704d11112ce`  |
| 2138   | Layout 1 | `c704d11112ce`  |
| 2134   | Layout 1 | `c704d11112ce`  |
| 2130   | Layout 1 | `c704d11112ce`  |
| 2122   | Layout 1 | `c704d11112ce`  |
| 2107   | Layout 1 | `c704d11112ce`  |
| 2098   | Layout 1 | `c704d11112ce`  |
| 2089   | Layout 1 | `c704d11112ce`  |
| 2081   | Layout 1 | `c704d11112ce`  |
| 2073   | Layout 1 | `c704d11112ce`  |
| 2067   | Layout 1 | `c704d11112ce`  |
| 2063   | Layout 1 | `c704d11112ce`  |
| 2059   | Layout 1 | `c704d11112ce`  |
| 2052   | Layout 1 | `c704d11112ce`  |
| 2044   | Layout 1 | `c704d11112ce`  |
| 2039   | Layout 1 | `c704d11112ce`  |
| 2032   | Layout 1 | `c704d11112ce`  |
| 2025   | Layout 1 | `c704d11112ce`  |
| 2011   | Layout 1 | `c704d11112ce`  |
| 2005   | Layout 1 | `c704d11112ce`  |
| 2000   | Layout 1 | `c704d11112ce`  |
| 1996   | Layout 1 | `c704d11112ce`  |
| 1991   | Layout 1 | `c704d11112ce`  |
| 1985   | Layout 1 | `c704d11112ce`  |
| 1980   | Layout 1 | `c704d11112ce`  |
| 1969   | Layout 1 | `c704d11112ce`  |
| 1964   | Layout 1 | `c704d11112ce`  |
| 1958   | Layout 1 | `c704d11112ce`  |
| 1950   | Layout 1 | `c704d11112ce`  |
| 1945   | Layout 1 | `c704d11112ce`  |
| 1937   | Layout 1 | `c704d11112ce`  |
| 1933   | Layout 1 | `c704d11112ce`  |
| 1927   | Layout 1 | `c704d11112ce`  |
| 1921   | Layout 1 | `c704d11112ce`  |
| 1914   | Layout 1 | `c704d11112ce`  |
| 1908   | Layout 1 | `c704d11112ce`  |
| 1897   | Layout 1 | `c704d11112ce`  |
| 1892   | Layout 1 | `c704d11112ce`  |
| 1886   | Layout 1 | `c704d11112ce`  |
| 1881   | Layout 1 | `c704d11112ce`  |
| 1871   | Layout 1 | `c704d11112ce`  |
| 1866   | Layout 1 | `c704d11112ce`  |
| 1862   | Layout 1 | `c704d11112ce`  |
| 1854   | Layout 1 | `c704d11112ce`  |
| 1846   | Layout 1 | `c704d11112ce`  |
| 1838   | Layout 1 | `c704d11112ce`  |
| 1832   | Layout 1 | `c704d11112ce`  |
| 1826   | Layout 1 | `c704d11112ce`  |
| 1822   | Layout 1 | `c704d11112ce`  |
| 1818   | Layout 1 | `c704d11112ce`  |
| 1804   | Layout 1 | `c704d11112ce`  |
| 1794   | Layout 1 | `c704d11112ce`  |
| 1790   | Layout 1 | `c704d11112ce`  |
| 1784   | Layout 1 | `c704d11112ce`  |
| 1774   | Layout 1 | `c704d11112ce`  |
| 1771   | Layout 1 | `c704d11112ce`  |
| 1762   | Layout 1 | `c704d11112ce`  |
| 1759   | Layout 1 | `c704d11112ce`  |
| 1754   | Layout 1 | `c704d11112ce`  |
| 1749   | Layout 1 | `c704d11112ce`  |
| 1743   | Layout 1 | `c704d11112ce`  |
| 1737   | Layout 1 | `c704d11112ce`  |
| 1731   | Layout 1 | `c704d11112ce`  |
| 1725   | Layout 1 | `c704d11112ce`  |
| 1717   | Layout 1 | `c704d11112ce`  |
| 1710   | Layout 1 | `c704d11112ce`  |
| 1704   | Layout 1 | `c704d11112ce`  |
| 1698   | Layout 1 | `c704d11112ce`  |
| 1690   | Layout 1 | `c704d11112ce`  |
| 1685   | Layout 1 | `c704d11112ce`  |
| 1680   | Layout 1 | `c704d11112ce`  |
| 1674   | Layout 1 | `c704d11112ce`  |
| 1668   | Layout 1 | `c704d11112ce`  |
| 1659   | Layout 1 | `c704d11112ce`  |
| 1649   | Layout 1 | `c704d11112ce`  |
| 1642   | Layout 1 | `c704d11112ce`  |
| 1636   | Layout 1 | `c704d11112ce`  |
| 1628   | Layout 1 | `c704d11112ce`  |
| 1622   | Layout 1 | `c704d11112ce`  |
| 1614   | Layout 1 | `c704d11112ce`  |
| 1608   | Layout 1 | `c704d11112ce`  |
| 1602   | Layout 1 | `c704d11112ce`  |
| 1598   | Layout 1 | `c704d11112ce`  |
| 1594   | Layout 1 | `c704d11112ce`  |
| 1590   | Layout 1 | `c704d11112ce`  |
| 1587   | Layout 1 | `c704d11112ce`  |
| 1584   | Layout 1 | `c704d11112ce`  |
| 1579   | Layout 1 | `c704d11112ce`  |
| 1572   | Layout 1 | `c704d11112ce`  |
| 1565   | Layout 1 | `c704d11112ce`  |
| 1559   | Layout 1 | `c704d11112ce`  |
| 1554   | Layout 1 | `c704d11112ce`  |
| 1547   | Layout 1 | `c704d11112ce`  |
| 1537   | Layout 1 | `c704d11112ce`  |
| 1529   | Layout 1 | `c704d11112ce`  |
| 1524   | Layout 1 | `c704d11112ce`  |
| 1519   | Layout 1 | `c704d11112ce`  |
| 1509   | Layout 1 | `c704d11112ce`  |
| 1506   | Layout 1 | `c704d11112ce`  |
| 1504   | Layout 1 | `c704d11112ce`  |
| 1500   | Layout 1 | `c704d11112ce`  |
| 1493   | Layout 1 | `c704d11112ce`  |
| 1489   | Layout 1 | `c704d11112ce`  |
| 1485   | Layout 1 | `c704d11112ce`  |
| 1481   | Layout 1 | `c704d11112ce`  |
| 1474   | Layout 1 | `c704d11112ce`  |
| 1466   | Layout 1 | `c704d11112ce`  |
| 1462   | Layout 1 | `c704d11112ce`  |
| 1459   | Layout 1 | `c704d11112ce`  |
| 1453   | Layout 1 | `c704d11112ce`  |
| 1450   | Layout 1 | `c704d11112ce`  |
| 1445   | Layout 1 | `c704d11112ce`  |
| 1439   | Layout 1 | `c704d11112ce`  |
| 1433   | Layout 1 | `c704d11112ce`  |
| 1430   | Layout 1 | `c704d11112ce`  |
| 1426   | Layout 1 | `c704d11112ce`  |
| 1421   | Layout 1 | `c704d11112ce`  |
| 1417   | Layout 1 | `c704d11112ce`  |
| 1416   | Layout 1 | `c704d11112ce`  |
| 1409   | Layout 1 | `c704d11112ce`  |
| 1405   | Layout 1 | `c704d11112ce`  |
| 1401   | Layout 1 | `c704d11112ce`  |
| 1396   | Layout 1 | `c704d11112ce`  |
| 1391   | Layout 1 | `c704d11112ce`  |
| 1390   | Layout 1 | `c704d11112ce`  |
| 1386   | Layout 1 | `c704d11112ce`  |
| 1381   | Layout 1 | `c704d11112ce`  |
| 1379   | Layout 1 | `c704d11112ce`  |
| 1372   | Layout 1 | `c704d11112ce`  |
| 1366   | Layout 1 | `c704d11112ce`  |
| 1364   | Layout 1 | `c704d11112ce`  |
| 1363   | Layout 1 | `c704d11112ce`  |
| 1360   | Layout 1 | `c704d11112ce`  |
| 1358   | Layout 1 | `c704d11112ce`  |
| 1355   | Layout 1 | `c704d11112ce`  |
| 1351   | Layout 1 | `c704d11112ce`  |
| 1348   | Layout 1 | `c704d11112ce`  |
| 1346   | Layout 1 | `c704d11112ce`  |
| 1341   | Layout 1 | `c704d11112ce`  |
| 1340   | Layout 1 | `c704d11112ce`  |
| 1338   | Layout 1 | `c704d11112ce`  |
| 1335   | Layout 1 | `c704d11112ce`  |
| 1333   | Layout 1 | `c704d11112ce`  |
| 1329   | Layout 1 | `c704d11112ce`  |
| 1327   | Layout 1 | `c704d11112ce`  |
| 1324   | No file  | `c704d11112ce`  |
| 1321   | No file  | `c704d11112ce`  |
| 1319   | No file  | `c704d11112ce`  |
| 1318   | No file  | `c704d11112ce`  |
| 1316   | No file  | `c704d11112ce`  |
| 1313   | No file  | `c704d11112ce`  |
| 1311   | No file  | `c704d11112ce`  |
| 1309   | No file  | `c704d11112ce`  |
| 1304   | No file  | `c704d11112ce`  |
| 1292   | No file  | `c704d11112ce`  |
| 1286   | No file  | `c704d11112ce`  |
| 1280   | No file  | `c704d11112ce`  |
| 1276   | No file  | `c704d11112ce`  |
| 1267   | No file  | `c704d11112ce`  |
| 1261   | No file  | `c704d11112ce`  |
| 1256   | No file  | `c704d11112ce`  |
| 1250   | No file  | `c704d11112ce`  |
| 1246   | No file  | `c704d11112ce`  |
| 1239   | No file  | `c704d11112ce`  |
| 1230   | No file  | `c704d11112ce`  |
| 1226   | No file  | `c704d11112ce`  |
| 1220   | No file  | `c704d11112ce`  |
| 1217   | No file  | `c704d11112ce`  |
| 1211   | No file  | `c704d11112ce`  |
| 1210   | No file  | `c704d11112ce`  |
| 1208   | No file  | `c704d11112ce`  |
| 1203   | No file  | `c704d11112ce`  |
| 1197   | No file  | `c704d11112ce`  |
| 1194   | No file  | `c704d11112ce`  |
| 1192   | No file  | `c704d11112ce`  |
| 1187   | No file  | `c704d11112ce`  |
| 1183   | No file  | `c704d11112ce`  |
| 1177   | No file  | `c704d11112ce`  |
| 1173   | No file  | `c704d11112ce`  |
| 1167   | No file  | `c704d11112ce`  |
| 1164   | No file  | `c704d11112ce`  |
| 1156   | No file  | `c704d11112ce`  |
| 1149   | No file  | `c704d11112ce`  |
| 1144   | No file  | `c704d11112ce`  |
| 1137   | No file  | `c704d11112ce`  |
| 1132   | No file  | `c704d11112ce`  |
| 1127   | No file  | `c704d11112ce`  |
| 1122   | No file  | `c704d11112ce`  |
| 1118   | No file  | `c704d11112ce`  |
| 1114   | No file  | `c704d11112ce`  |
| 1109   | No file  | `c704d11112ce`  |
| 1102   | No file  | `c704d11112ce`  |
| 1096   | No file  | `c704d11112ce`  |
| 1088   | No file  | `c704d11112ce`  |
| 1081   | No file  | `c704d11112ce`  |
| 1076   | No file  | `c704d11112ce`  |
| 1069   | No file  | `c704d11112ce`  |
| 1064   | No file  | `c704d11112ce`  |
| 1058   | No file  | `c704d11112ce`  |
| 1051   | No file  | `c704d11112ce`  |
| 1044   | No file  | `c704d11112ce`  |
| 1036   | No file  | `c704d11112ce`  |
| 1026   | No file  | `c704d11112ce`  |
| 1016   | No file  | `c704d11112ce`  |
| 1009   | No file  | `c704d11112ce`  |
| 1005   | No file  | `c704d11112ce`  |
| 1000   | No file  | `c704d11112ce`  |
| 998    | No file  | `c704d11112ce`  |
| 990    | No file  | `c704d11112ce`  |
| 979    | No file  | `c704d11112ce`  |
| 972    | No file  | `c704d11112ce`  |
| 963    | No file  | `c704d11112ce`  |
| 955    | No file  | `c704d11112ce`  |
| 946    | No file  | `c704d11112ce`  |
| 938    | No file  | `c704d11112ce`  |
| 927    | No file  | `c704d11112ce`  |
| 911    | No file  | `c704d11112ce`  |
| 904    | No file  | `c704d11112ce`  |
| 899    | No file  | `c704d11112ce`  |
| 894    | No file  | `c704d11112ce`  |
| 885    | No file  | `c704d11112ce`  |
| 879    | No file  | `c704d11112ce`  |
| 872    | No file  | `c704d11112ce`  |
| 864    | No file  | `c704d11112ce`  |
| 855    | No file  | `c704d11112ce`  |
| 853    | No file  | `c704d11112ce`  |
| 845    | No file  | `c704d11112ce`  |
| 837    | No file  | `c704d11112ce`  |
| 829    | No file  | `c704d11112ce`  |
| 822    | No file  | `c704d11112ce`  |
| 814    | No file  | `c704d11112ce`  |
| 805    | No file  | `c704d11112ce`  |
| 794    | No file  | `c704d11112ce`  |
| 787    | No file  | `c704d11112ce`  |
| 780    | No file  | `c704d11112ce`  |
| 771    | No file  | `c704d11112ce`  |
| 760    | No file  | `c704d11112ce`  |
| 748    | No file  | `c704d11112ce`  |
| 741    | No file  | `c704d11112ce`  |
| 736    | No file  | `c704d11112ce`  |
| 731    | No file  | `c704d11112ce`  |
| 723    | No file  | `c704d11112ce`  |
| 711    | No file  | `c704d11112ce`  |
| 707    | No file  | `c704d11112ce`  |
| 697    | No file  | `c704d11112ce`  |
| 689    | No file  | `c704d11112ce`  |
| 683    | No file  | `c704d11112ce`  |
| 678    | No file  | `c704d11112ce`  |
| 670    | No file  | `c704d11112ce`  |
| 661    | No file  | `c704d11112ce`  |
| 656    | No file  | `c704d11112ce`  |
| 652    | No file  | `c704d11112ce`  |
| 643    | No file  | `c704d11112ce`  |
| 637    | No file  | `c704d11112ce`  |
| 630    | No file  | `c704d11112ce`  |
| 627    | No file  | `c704d11112ce`  |
| 621    | No file  | `c704d11112ce`  |
| 617    | No file  | `c704d11112ce`  |
| 615    | No file  | `c704d11112ce`  |
| 606    | No file  | `c704d11112ce`  |
| 599    | No file  | `c704d11112ce`  |
| 592    | No file  | `c704d11112ce`  |
| 586    | No file  | `c704d11112ce`  |
| 577    | No file  | `c704d11112ce`  |
| 569    | No file  | `c704d11112ce`  |
| 561    | No file  | `c704d11112ce`  |
| 554    | No file  | `c704d11112ce`  |
| 542    | No file  | `c704d11112ce`  |
| 532    | No file  | `c704d11112ce`  |
| 531    | No file  | `c704d11112ce`  |
| 526    | No file  | `c704d11112ce`  |
| 521    | No file  | `c704d11112ce`  |
| 517    | No file  | `c704d11112ce`  |
| 510    | No file  | `c704d11112ce`  |
| 508    | No file  | `c704d11112ce`  |
| 504    | No file  | `c704d11112ce`  |
| 497    | No file  | `c704d11112ce`  |
| 491    | No file  | `c704d11112ce`  |
| 485    | No file  | `c704d11112ce`  |
| 478    | No file  | `c704d11112ce`  |
| 472    | No file  | `c704d11112ce`  |
| 466    | No file  | `c704d11112ce`  |
| 457    | No file  | `c704d11112ce`  |
| 452    | No file  | `c704d11112ce`  |
| 449    | No file  | `c704d11112ce`  |
| 435    | No file  | `c704d11112ce`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field          | Notes                                     |
| ------------------- | ------------ | -------------- | ----------------------------------------- |
| `+0x00`             | char[4]      | magic          | `PABR` (ASCII)                            |
| `+0x04`             | u32          | count          | Number of entries                         |
| `+0x08`             | Entry[count] | entries        | See Entry                                 |
| `entries+0x00`      | String Table | string_table   | The 12-byte trailer starts here; see String Table |
| `string_table+0x00` | u32          | end_of_entries | `8 + count * 4`, where the trailer starts |
| `string_table+0x04` | u32          | zero           | `0`                                       |

### Entry (4 bytes)

| Offset  | Type | Field           | Notes                                                       |
| ------- | ---- | --------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | packed_quest_id | `(quest_id << 16) \| quest_chain_id`; LOC type 18 title key |

### String Table (variable: 4 bytes + strings)

The PABR string table, here with no strings.

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Pass Rows

`panel_window_blackspiritpass_1.luac` walks `ToClient_SeasonPassQuestCount()` rows and asks for two quests per row: `ToClient_GetSeasonPassQuestAt(listIdx, __eSeasonPassQuest_Normal)` for the free reward and `ToClient_GetSeasonPassQuestAt(listIdx, __eSeasonPassQuest_SeasonPass)` for the premium reward. A premium reward counts as claimable only when the player's `isSeasonPass()` is true (`panel_window_blackspiritpass_2.luac`). The two type values match the two files:

- Each free quest `(chain, n)` in `fornormal` has its premium quest `(chain, n + 1)` in `forcash`. Free quests have odd sub IDs, premium quests even ones.
- Every `forcash` title ends in `(Black Spirit Pass)`; no `fornormal` title does.
- `seasonpassquestlist.bss` holds exactly the quests of both files, none twice.

The file order is not the row order: index `i` of `fornormal` and index `i` of `forcash` belong to the same row on only 6 of 205 indexes (client 3464).

On client 3464 both side files hold 205 quests and the full list 410, all with a LOC type 18 title. The quest chains fall in three blocks: 50000 to 50057 (titles start `[Summer Season]`), 50100 to 50146, and 50150 to 50152 (74, 74 and 52 quests in the full list).

## Notes

- Decompressed sizes on client 3464: `1,660` bytes for `seasonpassquestlist.bss`, `840` bytes for each side file; all match `8 + count * 4 + 12`.
- calpheonlabs (`seasonpassquestlist.bss.ts`, capture PAZ 3595) reads the same layout: a u32-counted array of (u16 quest group, u16 quest number) and a 12-byte pad. It names the cash file's quests "paid Season Pass quest IDs".
- `seasonpass.dbss` (7.6 KB, not documented yet) is the next file to check for the row order and the season period.
- `test_pass_lists.py` asserts that the full list is the two side files together and that every free quest has its premium quest at sub ID + 1.

## Open Questions

### Row Order

The window's row order (`listIdx`) does not follow the order of any of the three files. `seasonpass.dbss` is the first candidate for it.
