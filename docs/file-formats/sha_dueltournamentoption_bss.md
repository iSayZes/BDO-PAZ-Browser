# `sha_dueltournamentoption.bss` Format

## Purpose

The Shadow Arena duel tournament settings: the hashes of three action
names, the player count and the times of the tournament states. Clients
1784 and 2107 fill the values; from client 2519 every value is `0`, the
file size unchanged.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                           | Bytes | Records        | Row bytes |
| ------ | -------------- | ------------------------------ | ----- | -------------- | --------- |
| 1      | 1372 and later | `sha_dueltournamentoption.bss` | 60    | 1 String Table | 4         |

| Layout | File                           | Known        | Unknown      |
| ------ | ------------------------------ | ------------ | ------------ |
| 1      | `sha_dueltournamentoption.bss` | 36 B (60.0%) | 24 B (40.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `627df6c019f2`  |
| 3482   | Layout 1             | `627df6c019f2`  |
| 3474   | Layout 1             | `627df6c019f2`  |
| 3473   | Layout 1             | `627df6c019f2`  |
| 3464   | Layout 1             | `627df6c019f2`  |
| 3458   | Layout 1             | `627df6c019f2`  |
| 3454   | Layout 1             | `627df6c019f2`  |
| 3444   | Layout 1             | `627df6c019f2`  |
| 3435   | Layout 1             | `627df6c019f2`  |
| 3426   | Layout 1             | `627df6c019f2`  |
| 3418   | Layout 1             | `627df6c019f2`  |
| 3412   | Layout 1             | `627df6c019f2`  |
| 3402   | Layout 1             | `627df6c019f2`  |
| 3396   | Layout 1             | `627df6c019f2`  |
| 3387   | Layout 1             | `627df6c019f2`  |
| 3381   | Layout 1             | `627df6c019f2`  |
| 3373   | Layout 1             | `627df6c019f2`  |
| 3364   | Layout 1             | `627df6c019f2`  |
| 3356   | Layout 1             | `627df6c019f2`  |
| 3349   | Layout 1             | `627df6c019f2`  |
| 3342   | Layout 1             | `627df6c019f2`  |
| 3335   | Layout 1             | `627df6c019f2`  |
| 3326   | Layout 1             | `627df6c019f2`  |
| 3321   | Layout 1             | `627df6c019f2`  |
| 3314   | Layout 1             | `627df6c019f2`  |
| 3303   | Layout 1             | `627df6c019f2`  |
| 3302   | Layout 1             | `627df6c019f2`  |
| 3293   | Layout 1             | `627df6c019f2`  |
| 3283   | Layout 1             | `627df6c019f2`  |
| 3275   | Layout 1             | `627df6c019f2`  |
| 3267   | Layout 1             | `627df6c019f2`  |
| 3258   | Layout 1             | `627df6c019f2`  |
| 3251   | Layout 1             | `627df6c019f2`  |
| 3242   | Layout 1             | `627df6c019f2`  |
| 3235   | Layout 1             | `627df6c019f2`  |
| 3229   | Layout 1             | `627df6c019f2`  |
| 3212   | Layout 1             | `627df6c019f2`  |
| 3203   | Layout 1             | `627df6c019f2`  |
| 3193   | Layout 1             | `627df6c019f2`  |
| 3186   | Layout 1             | `627df6c019f2`  |
| 3177   | Layout 1             | `627df6c019f2`  |
| 3169   | Layout 1             | `627df6c019f2`  |
| 3158   | Layout 1             | `627df6c019f2`  |
| 3151   | Layout 1             | `627df6c019f2`  |
| 3144   | Layout 1             | `627df6c019f2`  |
| 3133   | Layout 1             | `627df6c019f2`  |
| 3125   | Layout 1             | `627df6c019f2`  |
| 3118   | Layout 1             | `627df6c019f2`  |
| 3111   | Layout 1             | `627df6c019f2`  |
| 3103   | Layout 1             | `627df6c019f2`  |
| 3095   | Layout 1             | `627df6c019f2`  |
| 3086   | Layout 1             | `627df6c019f2`  |
| 3072   | Layout 1             | `627df6c019f2`  |
| 3062   | Layout 1             | `627df6c019f2`  |
| 3052   | Layout 1             | `627df6c019f2`  |
| 3045   | Layout 1             | `627df6c019f2`  |
| 3037   | Layout 1             | `627df6c019f2`  |
| 3030   | Layout 1             | `627df6c019f2`  |
| 3021   | Layout 1             | `627df6c019f2`  |
| 3012   | Layout 1             | `627df6c019f2`  |
| 3002   | Layout 1             | `627df6c019f2`  |
| 2995   | Layout 1             | `627df6c019f2`  |
| 2987   | Layout 1             | `627df6c019f2`  |
| 2978   | Layout 1             | `627df6c019f2`  |
| 2970   | Layout 1             | `627df6c019f2`  |
| 2959   | Layout 1             | `627df6c019f2`  |
| 2951   | Layout 1             | `627df6c019f2`  |
| 2942   | Layout 1             | `627df6c019f2`  |
| 2935   | Layout 1             | `627df6c019f2`  |
| 2932   | Layout 1             | `627df6c019f2`  |
| 2923   | Layout 1             | `627df6c019f2`  |
| 2919   | Layout 1             | `627df6c019f2`  |
| 2907   | Layout 1             | `627df6c019f2`  |
| 2900   | Layout 1             | `627df6c019f2`  |
| 2891   | Layout 1             | `627df6c019f2`  |
| 2882   | Layout 1             | `627df6c019f2`  |
| 2872   | Layout 1             | `627df6c019f2`  |
| 2863   | Layout 1             | `627df6c019f2`  |
| 2855   | Layout 1             | `627df6c019f2`  |
| 2849   | Layout 1             | `627df6c019f2`  |
| 2844   | Layout 1             | `627df6c019f2`  |
| 2834   | Layout 1             | `627df6c019f2`  |
| 2825   | Layout 1             | `627df6c019f2`  |
| 2819   | Layout 1             | `627df6c019f2`  |
| 2811   | Layout 1             | `627df6c019f2`  |
| 2803   | Layout 1             | `627df6c019f2`  |
| 2794   | Layout 1             | `627df6c019f2`  |
| 2783   | Layout 1             | `627df6c019f2`  |
| 2774   | Layout 1             | `627df6c019f2`  |
| 2765   | Layout 1             | `627df6c019f2`  |
| 2756   | Layout 1             | `627df6c019f2`  |
| 2750   | Layout 1             | `627df6c019f2`  |
| 2743   | Layout 1             | `627df6c019f2`  |
| 2736   | Layout 1             | `627df6c019f2`  |
| 2726   | Layout 1             | `627df6c019f2`  |
| 2717   | Layout 1             | `627df6c019f2`  |
| 2709   | Layout 1             | `627df6c019f2`  |
| 2703   | Layout 1             | `627df6c019f2`  |
| 2695   | Layout 1             | `627df6c019f2`  |
| 2684   | Layout 1             | `627df6c019f2`  |
| 2672   | Layout 1             | `627df6c019f2`  |
| 2665   | Layout 1             | `627df6c019f2`  |
| 2657   | Layout 1             | `627df6c019f2`  |
| 2649   | Layout 1             | `627df6c019f2`  |
| 2644   | Layout 1             | `627df6c019f2`  |
| 2637   | Layout 1             | `627df6c019f2`  |
| 2629   | Layout 1             | `627df6c019f2`  |
| 2619   | Layout 1             | `627df6c019f2`  |
| 2612   | Layout 1             | `627df6c019f2`  |
| 2606   | Layout 1             | `627df6c019f2`  |
| 2602   | Layout 1             | `627df6c019f2`  |
| 2601   | Layout 1             | `627df6c019f2`  |
| 2592   | Layout 1             | `627df6c019f2`  |
| 2583   | Layout 1             | `627df6c019f2`  |
| 2575   | Layout 1             | `627df6c019f2`  |
| 2567   | Layout 1             | `627df6c019f2`  |
| 2560   | Layout 1             | `627df6c019f2`  |
| 2553   | Layout 1             | `627df6c019f2`  |
| 2545   | Layout 1             | `627df6c019f2`  |
| 2538   | Layout 1             | `627df6c019f2`  |
| 2529   | Layout 1             | `627df6c019f2`  |
| 2519   | Layout 1             | `627df6c019f2`  |
| 2513   | Layout 1             | `627df6c019f2`  |
| 2510   | Layout 1             | `627df6c019f2`  |
| 2507   | Layout 1             | `627df6c019f2`  |
| 2503   | Layout 1             | `627df6c019f2`  |
| 2498   | Layout 1             | `627df6c019f2`  |
| 2492   | Layout 1             | `627df6c019f2`  |
| 2487   | Layout 1             | `627df6c019f2`  |
| 2480   | Layout 1             | `627df6c019f2`  |
| 2474   | Layout 1             | `627df6c019f2`  |
| 2468   | Layout 1             | `627df6c019f2`  |
| 2460   | Layout 1             | `627df6c019f2`  |
| 2453   | Layout 1             | `627df6c019f2`  |
| 2444   | Layout 1             | `627df6c019f2`  |
| 2438   | Layout 1             | `627df6c019f2`  |
| 2434   | Layout 1             | `627df6c019f2`  |
| 2429   | Layout 1             | `627df6c019f2`  |
| 2421   | Layout 1             | `627df6c019f2`  |
| 2414   | Layout 1             | `627df6c019f2`  |
| 2407   | Layout 1             | `627df6c019f2`  |
| 2401   | Layout 1             | `627df6c019f2`  |
| 2397   | Layout 1             | `627df6c019f2`  |
| 2393   | Layout 1             | `627df6c019f2`  |
| 2384   | Layout 1             | `627df6c019f2`  |
| 2378   | Layout 1             | `627df6c019f2`  |
| 2372   | Layout 1             | `627df6c019f2`  |
| 2358   | Layout 1             | `627df6c019f2`  |
| 2352   | Layout 1             | `627df6c019f2`  |
| 2347   | Layout 1             | `627df6c019f2`  |
| 2343   | Layout 1             | `627df6c019f2`  |
| 2335   | Layout 1             | `627df6c019f2`  |
| 2327   | Layout 1             | `627df6c019f2`  |
| 2324   | Layout 1             | `627df6c019f2`  |
| 2319   | Layout 1             | `627df6c019f2`  |
| 2313   | Layout 1             | `627df6c019f2`  |
| 2308   | Layout 1             | `627df6c019f2`  |
| 2302   | Layout 1             | `627df6c019f2`  |
| 2295   | Layout 1             | `627df6c019f2`  |
| 2290   | Layout 1             | `627df6c019f2`  |
| 2284   | Layout 1             | `627df6c019f2`  |
| 2276   | Layout 1             | `627df6c019f2`  |
| 2269   | Layout 1             | `627df6c019f2`  |
| 2259   | Layout 1             | `627df6c019f2`  |
| 2250   | Layout 1             | `627df6c019f2`  |
| 2243   | Layout 1             | `627df6c019f2`  |
| 2235   | Layout 1             | `627df6c019f2`  |
| 2229   | Layout 1             | `627df6c019f2`  |
| 2224   | Layout 1             | `627df6c019f2`  |
| 2218   | Layout 1             | `627df6c019f2`  |
| 2215   | Layout 1             | `627df6c019f2`  |
| 2207   | Layout 1             | `627df6c019f2`  |
| 2203   | Layout 1             | `627df6c019f2`  |
| 2196   | Layout 1             | `627df6c019f2`  |
| 2192   | Layout 1             | `627df6c019f2`  |
| 2189   | Layout 1             | `627df6c019f2`  |
| 2183   | Layout 1             | `627df6c019f2`  |
| 2179   | Layout 1             | `627df6c019f2`  |
| 2171   | Layout 1             | `627df6c019f2`  |
| 2163   | Layout 1             | `627df6c019f2`  |
| 2156   | Layout 1             | `627df6c019f2`  |
| 2151   | Layout 1             | `627df6c019f2`  |
| 2147   | Layout 1             | `627df6c019f2`  |
| 2142   | Layout 1             | `627df6c019f2`  |
| 2138   | Layout 1             | `627df6c019f2`  |
| 2134   | Layout 1             | `627df6c019f2`  |
| 2130   | Layout 1             | `627df6c019f2`  |
| 2122   | Layout 1             | `627df6c019f2`  |
| 2107   | Layout 1             | `627df6c019f2`  |
| 2098   | Layout 1             | `627df6c019f2`  |
| 2089   | Layout 1             | `627df6c019f2`  |
| 2081   | Layout 1             | `627df6c019f2`  |
| 2073   | Layout 1             | `627df6c019f2`  |
| 2067   | Layout 1             | `627df6c019f2`  |
| 2063   | Layout 1             | `627df6c019f2`  |
| 2059   | Layout 1             | `627df6c019f2`  |
| 2052   | Layout 1             | `627df6c019f2`  |
| 2044   | Layout 1             | `627df6c019f2`  |
| 2039   | Layout 1             | `627df6c019f2`  |
| 2032   | Layout 1             | `627df6c019f2`  |
| 2025   | Layout 1             | `627df6c019f2`  |
| 2011   | Layout 1             | `627df6c019f2`  |
| 2005   | Layout 1             | `627df6c019f2`  |
| 2000   | Layout 1             | `627df6c019f2`  |
| 1996   | Layout 1             | `627df6c019f2`  |
| 1991   | Layout 1             | `627df6c019f2`  |
| 1985   | Layout 1             | `627df6c019f2`  |
| 1980   | Layout 1             | `627df6c019f2`  |
| 1969   | Layout 1             | `627df6c019f2`  |
| 1964   | Layout 1             | `627df6c019f2`  |
| 1958   | Layout 1             | `627df6c019f2`  |
| 1950   | Layout 1             | `627df6c019f2`  |
| 1945   | Layout 1             | `627df6c019f2`  |
| 1937   | Layout 1             | `627df6c019f2`  |
| 1933   | Layout 1             | `627df6c019f2`  |
| 1927   | Layout 1             | `627df6c019f2`  |
| 1921   | Layout 1             | `627df6c019f2`  |
| 1914   | Layout 1             | `627df6c019f2`  |
| 1908   | Layout 1             | `627df6c019f2`  |
| 1897   | Layout 1             | `627df6c019f2`  |
| 1892   | Layout 1             | `627df6c019f2`  |
| 1886   | Layout 1             | `627df6c019f2`  |
| 1881   | Layout 1             | `627df6c019f2`  |
| 1871   | Layout 1             | `627df6c019f2`  |
| 1866   | Layout 1             | `627df6c019f2`  |
| 1862   | Layout 1             | `627df6c019f2`  |
| 1854   | Layout 1             | `627df6c019f2`  |
| 1846   | Layout 1             | `627df6c019f2`  |
| 1838   | Layout 1             | `627df6c019f2`  |
| 1832   | Layout 1             | `627df6c019f2`  |
| 1826   | Layout 1             | `627df6c019f2`  |
| 1822   | Layout 1             | `627df6c019f2`  |
| 1818   | Layout 1             | `627df6c019f2`  |
| 1804   | Layout 1             | `627df6c019f2`  |
| 1794   | Layout 1             | `627df6c019f2`  |
| 1790   | Layout 1             | `627df6c019f2`  |
| 1784   | Layout 1             | `627df6c019f2`  |
| 1774   | Layout 1             | `627df6c019f2`  |
| 1771   | Layout 1             | `627df6c019f2`  |
| 1762   | Layout 1             | `627df6c019f2`  |
| 1759   | Layout 1             | `627df6c019f2`  |
| 1754   | Layout 1             | `627df6c019f2`  |
| 1749   | Layout 1             | `627df6c019f2`  |
| 1743   | Layout 1             | `627df6c019f2`  |
| 1737   | Layout 1             | `627df6c019f2`  |
| 1731   | Layout 1             | `627df6c019f2`  |
| 1725   | Layout 1             | `627df6c019f2`  |
| 1717   | Layout 1             | `627df6c019f2`  |
| 1710   | Layout 1             | `627df6c019f2`  |
| 1704   | Layout 1             | `627df6c019f2`  |
| 1698   | Layout 1             | `627df6c019f2`  |
| 1690   | Layout 1             | `627df6c019f2`  |
| 1685   | Layout 1             | `627df6c019f2`  |
| 1680   | Layout 1             | `627df6c019f2`  |
| 1674   | Layout 1             | `627df6c019f2`  |
| 1668   | Layout 1             | `627df6c019f2`  |
| 1659   | Layout 1             | `627df6c019f2`  |
| 1649   | Layout 1             | `627df6c019f2`  |
| 1642   | Layout 1             | `627df6c019f2`  |
| 1636   | Layout 1             | `627df6c019f2`  |
| 1628   | Layout 1             | `627df6c019f2`  |
| 1622   | Layout 1             | `627df6c019f2`  |
| 1614   | Layout 1             | `627df6c019f2`  |
| 1608   | Layout 1             | `627df6c019f2`  |
| 1602   | Layout 1             | `627df6c019f2`  |
| 1598   | Layout 1             | `627df6c019f2`  |
| 1594   | Layout 1             | `627df6c019f2`  |
| 1590   | Layout 1             | `627df6c019f2`  |
| 1587   | Layout 1             | `627df6c019f2`  |
| 1584   | Layout 1             | `627df6c019f2`  |
| 1579   | Layout 1             | `627df6c019f2`  |
| 1572   | Layout 1             | `627df6c019f2`  |
| 1565   | Layout 1             | `627df6c019f2`  |
| 1559   | Layout 1             | `627df6c019f2`  |
| 1554   | Layout 1             | `627df6c019f2`  |
| 1547   | Layout 1             | `627df6c019f2`  |
| 1537   | Layout 1             | `627df6c019f2`  |
| 1529   | Layout 1             | `627df6c019f2`  |
| 1524   | Layout 1             | `627df6c019f2`  |
| 1519   | Layout 1             | `627df6c019f2`  |
| 1509   | Layout 1             | `627df6c019f2`  |
| 1506   | Layout 1             | `627df6c019f2`  |
| 1504   | Layout 1             | `627df6c019f2`  |
| 1500   | Layout 1             | `627df6c019f2`  |
| 1493   | Layout 1             | `627df6c019f2`  |
| 1489   | Layout 1             | `627df6c019f2`  |
| 1485   | Layout 1             | `627df6c019f2`  |
| 1481   | Layout 1             | `627df6c019f2`  |
| 1474   | Layout 1             | `627df6c019f2`  |
| 1466   | Layout 1             | `627df6c019f2`  |
| 1462   | Layout 1             | `627df6c019f2`  |
| 1459   | Layout 1             | `627df6c019f2`  |
| 1453   | Layout 1             | `627df6c019f2`  |
| 1450   | Layout 1             | `627df6c019f2`  |
| 1445   | Layout 1             | `627df6c019f2`  |
| 1439   | Layout 1             | `627df6c019f2`  |
| 1433   | Layout 1             | `627df6c019f2`  |
| 1430   | Layout 1             | `627df6c019f2`  |
| 1426   | Layout 1             | `627df6c019f2`  |
| 1421   | Layout 1             | `627df6c019f2`  |
| 1417   | Layout 1             | `627df6c019f2`  |
| 1416   | Layout 1             | `627df6c019f2`  |
| 1409   | Layout 1             | `627df6c019f2`  |
| 1405   | Layout 1             | `627df6c019f2`  |
| 1401   | Layout 1             | `627df6c019f2`  |
| 1396   | Layout 1             | `627df6c019f2`  |
| 1391   | Layout 1             | `627df6c019f2`  |
| 1390   | Layout 1             | `627df6c019f2`  |
| 1386   | Layout 1             | `627df6c019f2`  |
| 1381   | No documented layout | `627df6c019f2`  |
| 1379   | No documented layout | `627df6c019f2`  |
| 1372   | Layout 1             | `627df6c019f2`  |
| 1366   | No documented layout | `627df6c019f2`  |
| 1364   | No file              | `627df6c019f2`  |
| 1363   | No file              | `627df6c019f2`  |
| 1360   | No file              | `627df6c019f2`  |
| 1358   | No file              | `627df6c019f2`  |
| 1355   | No file              | `627df6c019f2`  |
| 1351   | No file              | `627df6c019f2`  |
| 1348   | No file              | `627df6c019f2`  |
| 1346   | No file              | `627df6c019f2`  |
| 1341   | No file              | `627df6c019f2`  |
| 1340   | No file              | `627df6c019f2`  |
| 1338   | No file              | `627df6c019f2`  |
| 1335   | No file              | `627df6c019f2`  |
| 1333   | No file              | `627df6c019f2`  |
| 1329   | No file              | `627df6c019f2`  |
| 1327   | No file              | `627df6c019f2`  |
| 1324   | No file              | `627df6c019f2`  |
| 1321   | No file              | `627df6c019f2`  |
| 1319   | No file              | `627df6c019f2`  |
| 1318   | No file              | `627df6c019f2`  |
| 1316   | No file              | `627df6c019f2`  |
| 1313   | No file              | `627df6c019f2`  |
| 1311   | No file              | `627df6c019f2`  |
| 1309   | No file              | `627df6c019f2`  |
| 1304   | No file              | `627df6c019f2`  |
| 1292   | No file              | `627df6c019f2`  |
| 1286   | No file              | `627df6c019f2`  |
| 1280   | No file              | `627df6c019f2`  |
| 1276   | No file              | `627df6c019f2`  |
| 1267   | No file              | `627df6c019f2`  |
| 1261   | No file              | `627df6c019f2`  |
| 1256   | No file              | `627df6c019f2`  |
| 1250   | No file              | `627df6c019f2`  |
| 1246   | No file              | `627df6c019f2`  |
| 1239   | No file              | `627df6c019f2`  |
| 1230   | No file              | `627df6c019f2`  |
| 1226   | No file              | `627df6c019f2`  |
| 1220   | No file              | `627df6c019f2`  |
| 1217   | No file              | `627df6c019f2`  |
| 1211   | No file              | `627df6c019f2`  |
| 1210   | No file              | `627df6c019f2`  |
| 1208   | No file              | `627df6c019f2`  |
| 1203   | No file              | `627df6c019f2`  |
| 1197   | No file              | `627df6c019f2`  |
| 1194   | No file              | `627df6c019f2`  |
| 1192   | No file              | `627df6c019f2`  |
| 1187   | No file              | `627df6c019f2`  |
| 1183   | No file              | `627df6c019f2`  |
| 1177   | No file              | `627df6c019f2`  |
| 1173   | No file              | `627df6c019f2`  |
| 1167   | No file              | `627df6c019f2`  |
| 1164   | No file              | `627df6c019f2`  |
| 1156   | No file              | `627df6c019f2`  |
| 1149   | No file              | `627df6c019f2`  |
| 1144   | No file              | `627df6c019f2`  |
| 1137   | No file              | `627df6c019f2`  |
| 1132   | No file              | `627df6c019f2`  |
| 1127   | No file              | `627df6c019f2`  |
| 1122   | No file              | `627df6c019f2`  |
| 1118   | No file              | `627df6c019f2`  |
| 1114   | No file              | `627df6c019f2`  |
| 1109   | No file              | `627df6c019f2`  |
| 1102   | No file              | `627df6c019f2`  |
| 1096   | No file              | `627df6c019f2`  |
| 1088   | No file              | `627df6c019f2`  |
| 1081   | No file              | `627df6c019f2`  |
| 1076   | No file              | `627df6c019f2`  |
| 1069   | No file              | `627df6c019f2`  |
| 1064   | No file              | `627df6c019f2`  |
| 1058   | No file              | `627df6c019f2`  |
| 1051   | No file              | `627df6c019f2`  |
| 1044   | No file              | `627df6c019f2`  |
| 1036   | No file              | `627df6c019f2`  |
| 1026   | No file              | `627df6c019f2`  |
| 1016   | No file              | `627df6c019f2`  |
| 1009   | No file              | `627df6c019f2`  |
| 1005   | No file              | `627df6c019f2`  |
| 1000   | No file              | `627df6c019f2`  |
| 998    | No file              | `627df6c019f2`  |
| 990    | No file              | `627df6c019f2`  |
| 979    | No file              | `627df6c019f2`  |
| 972    | No file              | `627df6c019f2`  |
| 963    | No file              | `627df6c019f2`  |
| 955    | No file              | `627df6c019f2`  |
| 946    | No file              | `627df6c019f2`  |
| 938    | No file              | `627df6c019f2`  |
| 927    | No file              | `627df6c019f2`  |
| 911    | No file              | `627df6c019f2`  |
| 904    | No file              | `627df6c019f2`  |
| 899    | No file              | `627df6c019f2`  |
| 894    | No file              | `627df6c019f2`  |
| 885    | No file              | `627df6c019f2`  |
| 879    | No file              | `627df6c019f2`  |
| 872    | No file              | `627df6c019f2`  |
| 864    | No file              | `627df6c019f2`  |
| 855    | No file              | `627df6c019f2`  |
| 853    | No file              | `627df6c019f2`  |
| 845    | No file              | `627df6c019f2`  |
| 837    | No file              | `627df6c019f2`  |
| 829    | No file              | `627df6c019f2`  |
| 822    | No file              | `627df6c019f2`  |
| 814    | No file              | `627df6c019f2`  |
| 805    | No file              | `627df6c019f2`  |
| 794    | No file              | `627df6c019f2`  |
| 787    | No file              | `627df6c019f2`  |
| 780    | No file              | `627df6c019f2`  |
| 771    | No file              | `627df6c019f2`  |
| 760    | No file              | `627df6c019f2`  |
| 748    | No file              | `627df6c019f2`  |
| 741    | No file              | `627df6c019f2`  |
| 736    | No file              | `627df6c019f2`  |
| 731    | No file              | `627df6c019f2`  |
| 723    | No file              | `627df6c019f2`  |
| 711    | No file              | `627df6c019f2`  |
| 707    | No file              | `627df6c019f2`  |
| 697    | No file              | `627df6c019f2`  |
| 689    | No file              | `627df6c019f2`  |
| 683    | No file              | `627df6c019f2`  |
| 678    | No file              | `627df6c019f2`  |
| 670    | No file              | `627df6c019f2`  |
| 661    | No file              | `627df6c019f2`  |
| 656    | No file              | `627df6c019f2`  |
| 652    | No file              | `627df6c019f2`  |
| 643    | No file              | `627df6c019f2`  |
| 637    | No file              | `627df6c019f2`  |
| 630    | No file              | `627df6c019f2`  |
| 627    | No file              | `627df6c019f2`  |
| 621    | No file              | `627df6c019f2`  |
| 617    | No file              | `627df6c019f2`  |
| 615    | No file              | `627df6c019f2`  |
| 606    | No file              | `627df6c019f2`  |
| 599    | No file              | `627df6c019f2`  |
| 592    | No file              | `627df6c019f2`  |
| 586    | No file              | `627df6c019f2`  |
| 577    | No file              | `627df6c019f2`  |
| 569    | No file              | `627df6c019f2`  |
| 561    | No file              | `627df6c019f2`  |
| 554    | No file              | `627df6c019f2`  |
| 542    | No file              | `627df6c019f2`  |
| 532    | No file              | `627df6c019f2`  |
| 531    | No file              | `627df6c019f2`  |
| 526    | No file              | `627df6c019f2`  |
| 521    | No file              | `627df6c019f2`  |
| 517    | No file              | `627df6c019f2`  |
| 510    | No file              | `627df6c019f2`  |
| 508    | No file              | `627df6c019f2`  |
| 504    | No file              | `627df6c019f2`  |
| 497    | No file              | `627df6c019f2`  |
| 491    | No file              | `627df6c019f2`  |
| 485    | No file              | `627df6c019f2`  |
| 478    | No file              | `627df6c019f2`  |
| 472    | No file              | `627df6c019f2`  |
| 466    | No file              | `627df6c019f2`  |
| 457    | No file              | `627df6c019f2`  |
| 452    | No file              | `627df6c019f2`  |
| 449    | No file              | `627df6c019f2`  |
| 435    | No file              | `627df6c019f2`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field                   | Notes                                                                           |
| ------------------- | ------------ | ----------------------- | ------------------------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic                   | ASCII `PABR`                                                                    |
| `+0x04`             | u32          | game_start_action_hash  | `ascii_key_hash` of the action name: `BS_START` (`0x0E907704`) on client 1784    |
| `+0x08`             | u32          | fight_start_action_hash | `START_CHARACTER` (`0x8640C8B7`) on client 1784                                  |
| `+0x0C`             | u32          | winner_action_hash      | `SHADOW_ENDING_STUN` (`0x4CF4BE41`) on client 1784                               |
| `+0x10`             | u32          | max_player_count        | `6` on client 1784                                                              |
| `+0x14`             | u32          | unknown_14              | `180` on client 1784; see Open Questions                                        |
| `+0x18`             | u32          | unknown_18              | `60` on client 1784                                                             |
| `+0x1C`             | u32          | unknown_1c              | `60` on client 1784                                                             |
| `+0x20`             | u32          | unknown_20              | `10` on client 1784                                                             |
| `+0x24`             | u32          | unknown_24              | `10` on client 1784                                                             |
| `+0x28`             | u32          | after_time_end_state    | `120` on client 1784                                                            |
| `+0x2C`             | u32          | unknown_2c              | `180` on client 1784                                                            |
| `+0x30`             | String Table | string_table            | See String Table                                                                |
| `string_table+0x00` | u32          | table_start             | Offset of the string table, `0x30`                                              |
| `string_table+0x04` | u32          | zero                    | Always `0`                                                                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `SHA_DuelTournamentOption_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has one row with `GameStartAction`
`BS_START`, `FightStartAction` `START_CHARACTER` and `WinnerAction`
`SHADOW_ENDING_STUN`. The three hashes of the client 1784 file are
`ascii_key_hash` (lookup3 over the ASCII bytes, seed `0xC5EDE`) of exactly
these names, in that order.

The private server's server executable names eleven members of
`DuelTournamentOptionStaticStatus`: `_startAction`, `_duelStartAction`,
`_winnerStartAction`, `_maxPlayerCount`, `_waitMaxSec`, `_duelLimitSec`
and `_afterTimePlayState`, `_afterTimeDuelState`, `_afterTimeWaitState`,
`_afterTimeReayState`, `_afterTimeEndState`, which are the 11 fields of the
file. The sheet's numbers for these columns are `PlayerMaxCount` 6,
`AfterTimePlayState` 60, `AfterTimeDuelState` 10, `AfterTimeWaitState` 10,
`AfterTimeReadyState` 60, `AfterTimeEndState` 120, `DuelTimeLimit` 180 and
`GameForceStartTime` 180, the same 8 values as the file in another order.
`max_player_count` (6) and `after_time_end_state` (120) match one column
each; the other six values come in pairs and stay `unknown_*`.

## Notes

- The file is 60 bytes on every client checked (1784, 2107, 2519, 3002,
  3251, 3474). The sheet also has `MaxRound`, `MaxKillCount`,
  `StartGiveItem`, `ItemKey` and `ItemCount`, which the file does not
  store.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`,
  the action hashes as hex.

## Open Questions

### Paired Times

Which field of each equal pair is which column: `unknown_14` and
`unknown_2c` (180) are `DuelTimeLimit` and `GameForceStartTime` (the
server's `_duelLimitSec` and `_waitMaxSec`), `unknown_18` and `unknown_1c`
(60) are `AfterTimePlayState` and `AfterTimeReadyState`, `unknown_20` and
`unknown_24` (10) are `AfterTimeDuelState` and `AfterTimeWaitState`, each
pair in an unknown order. Every client from 2519 stores `0`, so only an
older client with other values could tell.
