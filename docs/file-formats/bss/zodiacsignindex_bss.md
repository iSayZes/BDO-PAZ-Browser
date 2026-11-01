# `zodiacsignindex.bss` Format

## Purpose

Lists zodiac sign IDs in display/index order. The file is a compact `PABR` lookup table for the 12 horoscope signs defined by `zodiacsign.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records  | Row bytes |
| ------ | -------------- | --------------------- | ----- | -------- | --------- |
| 1      | 1210 and later | `zodiacsignindex.bss` | 32    | 12 Entry | 1         |

| Layout | File                  | Known         | Unknown    |
| ------ | --------------------- | ------------- | ---------- |
| 1      | `zodiacsignindex.bss` | 32 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fa8940bdbfff`  |
| 3482   | Layout 1 | `fa8940bdbfff`  |
| 3474   | Layout 1 | `fa8940bdbfff`  |
| 3473   | Layout 1 | `fa8940bdbfff`  |
| 3464   | Layout 1 | `fa8940bdbfff`  |
| 3458   | Layout 1 | `fa8940bdbfff`  |
| 3454   | Layout 1 | `fa8940bdbfff`  |
| 3444   | Layout 1 | `fa8940bdbfff`  |
| 3435   | Layout 1 | `fa8940bdbfff`  |
| 3426   | Layout 1 | `fa8940bdbfff`  |
| 3418   | Layout 1 | `fa8940bdbfff`  |
| 3412   | Layout 1 | `fa8940bdbfff`  |
| 3402   | Layout 1 | `fa8940bdbfff`  |
| 3396   | Layout 1 | `fa8940bdbfff`  |
| 3387   | Layout 1 | `fa8940bdbfff`  |
| 3381   | Layout 1 | `fa8940bdbfff`  |
| 3373   | Layout 1 | `fa8940bdbfff`  |
| 3364   | Layout 1 | `fa8940bdbfff`  |
| 3356   | Layout 1 | `fa8940bdbfff`  |
| 3349   | Layout 1 | `fa8940bdbfff`  |
| 3342   | Layout 1 | `fa8940bdbfff`  |
| 3335   | Layout 1 | `fa8940bdbfff`  |
| 3326   | Layout 1 | `fa8940bdbfff`  |
| 3321   | Layout 1 | `fa8940bdbfff`  |
| 3314   | Layout 1 | `fa8940bdbfff`  |
| 3303   | Layout 1 | `fa8940bdbfff`  |
| 3302   | Layout 1 | `fa8940bdbfff`  |
| 3293   | Layout 1 | `fa8940bdbfff`  |
| 3283   | Layout 1 | `fa8940bdbfff`  |
| 3275   | Layout 1 | `fa8940bdbfff`  |
| 3267   | Layout 1 | `fa8940bdbfff`  |
| 3258   | Layout 1 | `fa8940bdbfff`  |
| 3251   | Layout 1 | `fa8940bdbfff`  |
| 3242   | Layout 1 | `fa8940bdbfff`  |
| 3235   | Layout 1 | `fa8940bdbfff`  |
| 3229   | Layout 1 | `fa8940bdbfff`  |
| 3212   | Layout 1 | `fa8940bdbfff`  |
| 3203   | Layout 1 | `fa8940bdbfff`  |
| 3193   | Layout 1 | `fa8940bdbfff`  |
| 3186   | Layout 1 | `fa8940bdbfff`  |
| 3177   | Layout 1 | `fa8940bdbfff`  |
| 3169   | Layout 1 | `fa8940bdbfff`  |
| 3158   | Layout 1 | `fa8940bdbfff`  |
| 3151   | Layout 1 | `fa8940bdbfff`  |
| 3144   | Layout 1 | `fa8940bdbfff`  |
| 3133   | Layout 1 | `fa8940bdbfff`  |
| 3125   | Layout 1 | `fa8940bdbfff`  |
| 3118   | Layout 1 | `fa8940bdbfff`  |
| 3111   | Layout 1 | `fa8940bdbfff`  |
| 3103   | Layout 1 | `fa8940bdbfff`  |
| 3095   | Layout 1 | `fa8940bdbfff`  |
| 3086   | Layout 1 | `fa8940bdbfff`  |
| 3072   | Layout 1 | `fa8940bdbfff`  |
| 3062   | Layout 1 | `fa8940bdbfff`  |
| 3052   | Layout 1 | `fa8940bdbfff`  |
| 3045   | Layout 1 | `fa8940bdbfff`  |
| 3037   | Layout 1 | `fa8940bdbfff`  |
| 3030   | Layout 1 | `fa8940bdbfff`  |
| 3021   | Layout 1 | `fa8940bdbfff`  |
| 3012   | Layout 1 | `fa8940bdbfff`  |
| 3002   | Layout 1 | `fa8940bdbfff`  |
| 2995   | Layout 1 | `fa8940bdbfff`  |
| 2987   | Layout 1 | `fa8940bdbfff`  |
| 2978   | Layout 1 | `fa8940bdbfff`  |
| 2970   | Layout 1 | `fa8940bdbfff`  |
| 2959   | Layout 1 | `fa8940bdbfff`  |
| 2951   | Layout 1 | `fa8940bdbfff`  |
| 2942   | Layout 1 | `fa8940bdbfff`  |
| 2935   | Layout 1 | `fa8940bdbfff`  |
| 2932   | Layout 1 | `fa8940bdbfff`  |
| 2923   | Layout 1 | `fa8940bdbfff`  |
| 2919   | Layout 1 | `fa8940bdbfff`  |
| 2907   | Layout 1 | `fa8940bdbfff`  |
| 2900   | Layout 1 | `fa8940bdbfff`  |
| 2891   | Layout 1 | `fa8940bdbfff`  |
| 2882   | Layout 1 | `fa8940bdbfff`  |
| 2872   | Layout 1 | `fa8940bdbfff`  |
| 2863   | Layout 1 | `fa8940bdbfff`  |
| 2855   | Layout 1 | `fa8940bdbfff`  |
| 2849   | Layout 1 | `fa8940bdbfff`  |
| 2844   | Layout 1 | `fa8940bdbfff`  |
| 2834   | Layout 1 | `fa8940bdbfff`  |
| 2825   | Layout 1 | `fa8940bdbfff`  |
| 2819   | Layout 1 | `fa8940bdbfff`  |
| 2811   | Layout 1 | `fa8940bdbfff`  |
| 2803   | Layout 1 | `fa8940bdbfff`  |
| 2794   | Layout 1 | `fa8940bdbfff`  |
| 2783   | Layout 1 | `fa8940bdbfff`  |
| 2774   | Layout 1 | `fa8940bdbfff`  |
| 2765   | Layout 1 | `fa8940bdbfff`  |
| 2756   | Layout 1 | `fa8940bdbfff`  |
| 2750   | Layout 1 | `fa8940bdbfff`  |
| 2743   | Layout 1 | `fa8940bdbfff`  |
| 2736   | Layout 1 | `fa8940bdbfff`  |
| 2726   | Layout 1 | `fa8940bdbfff`  |
| 2717   | Layout 1 | `fa8940bdbfff`  |
| 2709   | Layout 1 | `fa8940bdbfff`  |
| 2703   | Layout 1 | `fa8940bdbfff`  |
| 2695   | Layout 1 | `fa8940bdbfff`  |
| 2684   | Layout 1 | `fa8940bdbfff`  |
| 2672   | Layout 1 | `fa8940bdbfff`  |
| 2665   | Layout 1 | `fa8940bdbfff`  |
| 2657   | Layout 1 | `fa8940bdbfff`  |
| 2649   | Layout 1 | `fa8940bdbfff`  |
| 2644   | Layout 1 | `fa8940bdbfff`  |
| 2637   | Layout 1 | `fa8940bdbfff`  |
| 2629   | Layout 1 | `fa8940bdbfff`  |
| 2619   | Layout 1 | `fa8940bdbfff`  |
| 2612   | Layout 1 | `fa8940bdbfff`  |
| 2606   | Layout 1 | `fa8940bdbfff`  |
| 2602   | Layout 1 | `fa8940bdbfff`  |
| 2601   | Layout 1 | `fa8940bdbfff`  |
| 2592   | Layout 1 | `fa8940bdbfff`  |
| 2583   | Layout 1 | `fa8940bdbfff`  |
| 2575   | Layout 1 | `fa8940bdbfff`  |
| 2567   | Layout 1 | `fa8940bdbfff`  |
| 2560   | Layout 1 | `fa8940bdbfff`  |
| 2553   | Layout 1 | `fa8940bdbfff`  |
| 2545   | Layout 1 | `fa8940bdbfff`  |
| 2538   | Layout 1 | `fa8940bdbfff`  |
| 2529   | Layout 1 | `fa8940bdbfff`  |
| 2519   | Layout 1 | `fa8940bdbfff`  |
| 2513   | Layout 1 | `fa8940bdbfff`  |
| 2510   | Layout 1 | `fa8940bdbfff`  |
| 2507   | Layout 1 | `fa8940bdbfff`  |
| 2503   | Layout 1 | `fa8940bdbfff`  |
| 2498   | Layout 1 | `fa8940bdbfff`  |
| 2492   | Layout 1 | `fa8940bdbfff`  |
| 2487   | Layout 1 | `fa8940bdbfff`  |
| 2480   | Layout 1 | `fa8940bdbfff`  |
| 2474   | Layout 1 | `fa8940bdbfff`  |
| 2468   | Layout 1 | `fa8940bdbfff`  |
| 2460   | Layout 1 | `fa8940bdbfff`  |
| 2453   | Layout 1 | `fa8940bdbfff`  |
| 2444   | Layout 1 | `fa8940bdbfff`  |
| 2438   | Layout 1 | `fa8940bdbfff`  |
| 2434   | Layout 1 | `fa8940bdbfff`  |
| 2429   | Layout 1 | `fa8940bdbfff`  |
| 2421   | Layout 1 | `fa8940bdbfff`  |
| 2414   | Layout 1 | `fa8940bdbfff`  |
| 2407   | Layout 1 | `fa8940bdbfff`  |
| 2401   | Layout 1 | `fa8940bdbfff`  |
| 2397   | Layout 1 | `fa8940bdbfff`  |
| 2393   | Layout 1 | `fa8940bdbfff`  |
| 2384   | Layout 1 | `fa8940bdbfff`  |
| 2378   | Layout 1 | `fa8940bdbfff`  |
| 2372   | Layout 1 | `fa8940bdbfff`  |
| 2358   | Layout 1 | `fa8940bdbfff`  |
| 2352   | Layout 1 | `fa8940bdbfff`  |
| 2347   | Layout 1 | `fa8940bdbfff`  |
| 2343   | Layout 1 | `fa8940bdbfff`  |
| 2335   | Layout 1 | `fa8940bdbfff`  |
| 2327   | Layout 1 | `fa8940bdbfff`  |
| 2324   | Layout 1 | `fa8940bdbfff`  |
| 2319   | Layout 1 | `fa8940bdbfff`  |
| 2313   | Layout 1 | `fa8940bdbfff`  |
| 2308   | Layout 1 | `fa8940bdbfff`  |
| 2302   | Layout 1 | `fa8940bdbfff`  |
| 2295   | Layout 1 | `fa8940bdbfff`  |
| 2290   | Layout 1 | `fa8940bdbfff`  |
| 2284   | Layout 1 | `fa8940bdbfff`  |
| 2276   | Layout 1 | `fa8940bdbfff`  |
| 2269   | Layout 1 | `fa8940bdbfff`  |
| 2259   | Layout 1 | `fa8940bdbfff`  |
| 2250   | Layout 1 | `fa8940bdbfff`  |
| 2243   | Layout 1 | `fa8940bdbfff`  |
| 2235   | Layout 1 | `fa8940bdbfff`  |
| 2229   | Layout 1 | `fa8940bdbfff`  |
| 2224   | Layout 1 | `fa8940bdbfff`  |
| 2218   | Layout 1 | `fa8940bdbfff`  |
| 2215   | Layout 1 | `fa8940bdbfff`  |
| 2207   | Layout 1 | `fa8940bdbfff`  |
| 2203   | Layout 1 | `fa8940bdbfff`  |
| 2196   | Layout 1 | `fa8940bdbfff`  |
| 2192   | Layout 1 | `fa8940bdbfff`  |
| 2189   | Layout 1 | `fa8940bdbfff`  |
| 2183   | Layout 1 | `fa8940bdbfff`  |
| 2179   | Layout 1 | `fa8940bdbfff`  |
| 2171   | Layout 1 | `fa8940bdbfff`  |
| 2163   | Layout 1 | `fa8940bdbfff`  |
| 2156   | Layout 1 | `fa8940bdbfff`  |
| 2151   | Layout 1 | `fa8940bdbfff`  |
| 2147   | Layout 1 | `fa8940bdbfff`  |
| 2142   | Layout 1 | `fa8940bdbfff`  |
| 2138   | Layout 1 | `fa8940bdbfff`  |
| 2134   | Layout 1 | `fa8940bdbfff`  |
| 2130   | Layout 1 | `fa8940bdbfff`  |
| 2122   | Layout 1 | `fa8940bdbfff`  |
| 2107   | Layout 1 | `fa8940bdbfff`  |
| 2098   | Layout 1 | `fa8940bdbfff`  |
| 2089   | Layout 1 | `fa8940bdbfff`  |
| 2081   | Layout 1 | `fa8940bdbfff`  |
| 2073   | Layout 1 | `fa8940bdbfff`  |
| 2067   | Layout 1 | `fa8940bdbfff`  |
| 2063   | Layout 1 | `fa8940bdbfff`  |
| 2059   | Layout 1 | `fa8940bdbfff`  |
| 2052   | Layout 1 | `fa8940bdbfff`  |
| 2044   | Layout 1 | `fa8940bdbfff`  |
| 2039   | Layout 1 | `fa8940bdbfff`  |
| 2032   | Layout 1 | `fa8940bdbfff`  |
| 2025   | Layout 1 | `fa8940bdbfff`  |
| 2011   | Layout 1 | `fa8940bdbfff`  |
| 2005   | Layout 1 | `fa8940bdbfff`  |
| 2000   | Layout 1 | `fa8940bdbfff`  |
| 1996   | Layout 1 | `fa8940bdbfff`  |
| 1991   | Layout 1 | `fa8940bdbfff`  |
| 1985   | Layout 1 | `fa8940bdbfff`  |
| 1980   | Layout 1 | `fa8940bdbfff`  |
| 1969   | Layout 1 | `fa8940bdbfff`  |
| 1964   | Layout 1 | `fa8940bdbfff`  |
| 1958   | Layout 1 | `fa8940bdbfff`  |
| 1950   | Layout 1 | `fa8940bdbfff`  |
| 1945   | Layout 1 | `fa8940bdbfff`  |
| 1937   | Layout 1 | `fa8940bdbfff`  |
| 1933   | Layout 1 | `fa8940bdbfff`  |
| 1927   | Layout 1 | `fa8940bdbfff`  |
| 1921   | Layout 1 | `fa8940bdbfff`  |
| 1914   | Layout 1 | `fa8940bdbfff`  |
| 1908   | Layout 1 | `fa8940bdbfff`  |
| 1897   | Layout 1 | `fa8940bdbfff`  |
| 1892   | Layout 1 | `fa8940bdbfff`  |
| 1886   | Layout 1 | `fa8940bdbfff`  |
| 1881   | Layout 1 | `fa8940bdbfff`  |
| 1871   | Layout 1 | `fa8940bdbfff`  |
| 1866   | Layout 1 | `fa8940bdbfff`  |
| 1862   | Layout 1 | `fa8940bdbfff`  |
| 1854   | Layout 1 | `fa8940bdbfff`  |
| 1846   | Layout 1 | `fa8940bdbfff`  |
| 1838   | Layout 1 | `fa8940bdbfff`  |
| 1832   | Layout 1 | `fa8940bdbfff`  |
| 1826   | Layout 1 | `fa8940bdbfff`  |
| 1822   | Layout 1 | `fa8940bdbfff`  |
| 1818   | Layout 1 | `fa8940bdbfff`  |
| 1804   | Layout 1 | `fa8940bdbfff`  |
| 1794   | Layout 1 | `fa8940bdbfff`  |
| 1790   | Layout 1 | `fa8940bdbfff`  |
| 1784   | Layout 1 | `fa8940bdbfff`  |
| 1774   | Layout 1 | `fa8940bdbfff`  |
| 1771   | Layout 1 | `fa8940bdbfff`  |
| 1762   | Layout 1 | `fa8940bdbfff`  |
| 1759   | Layout 1 | `fa8940bdbfff`  |
| 1754   | Layout 1 | `fa8940bdbfff`  |
| 1749   | Layout 1 | `fa8940bdbfff`  |
| 1743   | Layout 1 | `fa8940bdbfff`  |
| 1737   | Layout 1 | `fa8940bdbfff`  |
| 1731   | Layout 1 | `fa8940bdbfff`  |
| 1725   | Layout 1 | `fa8940bdbfff`  |
| 1717   | Layout 1 | `fa8940bdbfff`  |
| 1710   | Layout 1 | `fa8940bdbfff`  |
| 1704   | Layout 1 | `fa8940bdbfff`  |
| 1698   | Layout 1 | `fa8940bdbfff`  |
| 1690   | Layout 1 | `fa8940bdbfff`  |
| 1685   | Layout 1 | `fa8940bdbfff`  |
| 1680   | Layout 1 | `fa8940bdbfff`  |
| 1674   | Layout 1 | `fa8940bdbfff`  |
| 1668   | Layout 1 | `fa8940bdbfff`  |
| 1659   | Layout 1 | `fa8940bdbfff`  |
| 1649   | Layout 1 | `fa8940bdbfff`  |
| 1642   | Layout 1 | `fa8940bdbfff`  |
| 1636   | Layout 1 | `fa8940bdbfff`  |
| 1628   | Layout 1 | `fa8940bdbfff`  |
| 1622   | Layout 1 | `fa8940bdbfff`  |
| 1614   | Layout 1 | `fa8940bdbfff`  |
| 1608   | Layout 1 | `fa8940bdbfff`  |
| 1602   | Layout 1 | `fa8940bdbfff`  |
| 1598   | Layout 1 | `fa8940bdbfff`  |
| 1594   | Layout 1 | `fa8940bdbfff`  |
| 1590   | Layout 1 | `fa8940bdbfff`  |
| 1587   | Layout 1 | `fa8940bdbfff`  |
| 1584   | Layout 1 | `fa8940bdbfff`  |
| 1579   | Layout 1 | `fa8940bdbfff`  |
| 1572   | Layout 1 | `fa8940bdbfff`  |
| 1565   | Layout 1 | `fa8940bdbfff`  |
| 1559   | Layout 1 | `fa8940bdbfff`  |
| 1554   | Layout 1 | `fa8940bdbfff`  |
| 1547   | Layout 1 | `fa8940bdbfff`  |
| 1537   | Layout 1 | `fa8940bdbfff`  |
| 1529   | Layout 1 | `fa8940bdbfff`  |
| 1524   | Layout 1 | `fa8940bdbfff`  |
| 1519   | Layout 1 | `fa8940bdbfff`  |
| 1509   | Layout 1 | `fa8940bdbfff`  |
| 1506   | Layout 1 | `fa8940bdbfff`  |
| 1504   | Layout 1 | `fa8940bdbfff`  |
| 1500   | Layout 1 | `fa8940bdbfff`  |
| 1493   | Layout 1 | `fa8940bdbfff`  |
| 1489   | Layout 1 | `fa8940bdbfff`  |
| 1485   | Layout 1 | `fa8940bdbfff`  |
| 1481   | Layout 1 | `fa8940bdbfff`  |
| 1474   | Layout 1 | `fa8940bdbfff`  |
| 1466   | Layout 1 | `fa8940bdbfff`  |
| 1462   | Layout 1 | `fa8940bdbfff`  |
| 1459   | Layout 1 | `fa8940bdbfff`  |
| 1453   | Layout 1 | `fa8940bdbfff`  |
| 1450   | Layout 1 | `fa8940bdbfff`  |
| 1445   | Layout 1 | `fa8940bdbfff`  |
| 1439   | Layout 1 | `fa8940bdbfff`  |
| 1433   | Layout 1 | `fa8940bdbfff`  |
| 1430   | Layout 1 | `fa8940bdbfff`  |
| 1426   | Layout 1 | `fa8940bdbfff`  |
| 1421   | Layout 1 | `fa8940bdbfff`  |
| 1417   | Layout 1 | `fa8940bdbfff`  |
| 1416   | Layout 1 | `fa8940bdbfff`  |
| 1409   | Layout 1 | `fa8940bdbfff`  |
| 1405   | Layout 1 | `fa8940bdbfff`  |
| 1401   | Layout 1 | `fa8940bdbfff`  |
| 1396   | Layout 1 | `fa8940bdbfff`  |
| 1391   | Layout 1 | `fa8940bdbfff`  |
| 1390   | Layout 1 | `fa8940bdbfff`  |
| 1386   | Layout 1 | `fa8940bdbfff`  |
| 1381   | Layout 1 | `fa8940bdbfff`  |
| 1379   | Layout 1 | `fa8940bdbfff`  |
| 1372   | Layout 1 | `fa8940bdbfff`  |
| 1366   | Layout 1 | `fa8940bdbfff`  |
| 1364   | Layout 1 | `fa8940bdbfff`  |
| 1363   | Layout 1 | `fa8940bdbfff`  |
| 1360   | Layout 1 | `fa8940bdbfff`  |
| 1358   | Layout 1 | `fa8940bdbfff`  |
| 1355   | Layout 1 | `fa8940bdbfff`  |
| 1351   | Layout 1 | `fa8940bdbfff`  |
| 1348   | Layout 1 | `fa8940bdbfff`  |
| 1346   | Layout 1 | `fa8940bdbfff`  |
| 1341   | Layout 1 | `fa8940bdbfff`  |
| 1340   | Layout 1 | `fa8940bdbfff`  |
| 1338   | Layout 1 | `fa8940bdbfff`  |
| 1335   | Layout 1 | `fa8940bdbfff`  |
| 1333   | Layout 1 | `fa8940bdbfff`  |
| 1329   | Layout 1 | `fa8940bdbfff`  |
| 1327   | Layout 1 | `fa8940bdbfff`  |
| 1324   | Layout 1 | `fa8940bdbfff`  |
| 1321   | Layout 1 | `fa8940bdbfff`  |
| 1319   | Layout 1 | `fa8940bdbfff`  |
| 1318   | Layout 1 | `fa8940bdbfff`  |
| 1316   | Layout 1 | `fa8940bdbfff`  |
| 1313   | Layout 1 | `fa8940bdbfff`  |
| 1311   | Layout 1 | `fa8940bdbfff`  |
| 1309   | Layout 1 | `fa8940bdbfff`  |
| 1304   | Layout 1 | `fa8940bdbfff`  |
| 1292   | Layout 1 | `fa8940bdbfff`  |
| 1286   | Layout 1 | `fa8940bdbfff`  |
| 1280   | Layout 1 | `fa8940bdbfff`  |
| 1276   | Layout 1 | `fa8940bdbfff`  |
| 1267   | Layout 1 | `fa8940bdbfff`  |
| 1261   | Layout 1 | `fa8940bdbfff`  |
| 1256   | Layout 1 | `fa8940bdbfff`  |
| 1250   | Layout 1 | `fa8940bdbfff`  |
| 1246   | Layout 1 | `fa8940bdbfff`  |
| 1239   | Layout 1 | `fa8940bdbfff`  |
| 1230   | Layout 1 | `fa8940bdbfff`  |
| 1226   | Layout 1 | `fa8940bdbfff`  |
| 1220   | Layout 1 | `fa8940bdbfff`  |
| 1217   | Layout 1 | `fa8940bdbfff`  |
| 1211   | Layout 1 | `fa8940bdbfff`  |
| 1210   | Layout 1 | `fa8940bdbfff`  |
| 1208   | No file  | `fa8940bdbfff`  |
| 1203   | No file  | `fa8940bdbfff`  |
| 1197   | No file  | `fa8940bdbfff`  |
| 1194   | No file  | `fa8940bdbfff`  |
| 1192   | No file  | `fa8940bdbfff`  |
| 1187   | No file  | `fa8940bdbfff`  |
| 1183   | No file  | `fa8940bdbfff`  |
| 1177   | No file  | `fa8940bdbfff`  |
| 1173   | No file  | `fa8940bdbfff`  |
| 1167   | No file  | `fa8940bdbfff`  |
| 1164   | No file  | `fa8940bdbfff`  |
| 1156   | No file  | `fa8940bdbfff`  |
| 1149   | No file  | `fa8940bdbfff`  |
| 1144   | No file  | `fa8940bdbfff`  |
| 1137   | No file  | `fa8940bdbfff`  |
| 1132   | No file  | `fa8940bdbfff`  |
| 1127   | No file  | `fa8940bdbfff`  |
| 1122   | No file  | `fa8940bdbfff`  |
| 1118   | No file  | `fa8940bdbfff`  |
| 1114   | No file  | `fa8940bdbfff`  |
| 1109   | No file  | `fa8940bdbfff`  |
| 1102   | No file  | `fa8940bdbfff`  |
| 1096   | No file  | `fa8940bdbfff`  |
| 1088   | No file  | `fa8940bdbfff`  |
| 1081   | No file  | `fa8940bdbfff`  |
| 1076   | No file  | `fa8940bdbfff`  |
| 1069   | No file  | `fa8940bdbfff`  |
| 1064   | No file  | `fa8940bdbfff`  |
| 1058   | No file  | `fa8940bdbfff`  |
| 1051   | No file  | `fa8940bdbfff`  |
| 1044   | No file  | `fa8940bdbfff`  |
| 1036   | No file  | `fa8940bdbfff`  |
| 1026   | No file  | `fa8940bdbfff`  |
| 1016   | No file  | `fa8940bdbfff`  |
| 1009   | No file  | `fa8940bdbfff`  |
| 1005   | No file  | `fa8940bdbfff`  |
| 1000   | No file  | `fa8940bdbfff`  |
| 998    | No file  | `fa8940bdbfff`  |
| 990    | No file  | `fa8940bdbfff`  |
| 979    | No file  | `fa8940bdbfff`  |
| 972    | No file  | `fa8940bdbfff`  |
| 963    | No file  | `fa8940bdbfff`  |
| 955    | No file  | `fa8940bdbfff`  |
| 946    | No file  | `fa8940bdbfff`  |
| 938    | No file  | `fa8940bdbfff`  |
| 927    | No file  | `fa8940bdbfff`  |
| 911    | No file  | `fa8940bdbfff`  |
| 904    | No file  | `fa8940bdbfff`  |
| 899    | No file  | `fa8940bdbfff`  |
| 894    | No file  | `fa8940bdbfff`  |
| 885    | No file  | `fa8940bdbfff`  |
| 879    | No file  | `fa8940bdbfff`  |
| 872    | No file  | `fa8940bdbfff`  |
| 864    | No file  | `fa8940bdbfff`  |
| 855    | No file  | `fa8940bdbfff`  |
| 853    | No file  | `fa8940bdbfff`  |
| 845    | No file  | `fa8940bdbfff`  |
| 837    | No file  | `fa8940bdbfff`  |
| 829    | No file  | `fa8940bdbfff`  |
| 822    | No file  | `fa8940bdbfff`  |
| 814    | No file  | `fa8940bdbfff`  |
| 805    | No file  | `fa8940bdbfff`  |
| 794    | No file  | `fa8940bdbfff`  |
| 787    | No file  | `fa8940bdbfff`  |
| 780    | No file  | `fa8940bdbfff`  |
| 771    | No file  | `fa8940bdbfff`  |
| 760    | No file  | `fa8940bdbfff`  |
| 748    | No file  | `fa8940bdbfff`  |
| 741    | No file  | `fa8940bdbfff`  |
| 736    | No file  | `fa8940bdbfff`  |
| 731    | No file  | `fa8940bdbfff`  |
| 723    | No file  | `fa8940bdbfff`  |
| 711    | No file  | `fa8940bdbfff`  |
| 707    | No file  | `fa8940bdbfff`  |
| 697    | No file  | `fa8940bdbfff`  |
| 689    | No file  | `fa8940bdbfff`  |
| 683    | No file  | `fa8940bdbfff`  |
| 678    | No file  | `fa8940bdbfff`  |
| 670    | No file  | `fa8940bdbfff`  |
| 661    | No file  | `fa8940bdbfff`  |
| 656    | No file  | `fa8940bdbfff`  |
| 652    | No file  | `fa8940bdbfff`  |
| 643    | No file  | `fa8940bdbfff`  |
| 637    | No file  | `fa8940bdbfff`  |
| 630    | No file  | `fa8940bdbfff`  |
| 627    | No file  | `fa8940bdbfff`  |
| 621    | No file  | `fa8940bdbfff`  |
| 617    | No file  | `fa8940bdbfff`  |
| 615    | No file  | `fa8940bdbfff`  |
| 606    | No file  | `fa8940bdbfff`  |
| 599    | No file  | `fa8940bdbfff`  |
| 592    | No file  | `fa8940bdbfff`  |
| 586    | No file  | `fa8940bdbfff`  |
| 577    | No file  | `fa8940bdbfff`  |
| 569    | No file  | `fa8940bdbfff`  |
| 561    | No file  | `fa8940bdbfff`  |
| 554    | No file  | `fa8940bdbfff`  |
| 542    | No file  | `fa8940bdbfff`  |
| 532    | No file  | `fa8940bdbfff`  |
| 531    | No file  | `fa8940bdbfff`  |
| 526    | No file  | `fa8940bdbfff`  |
| 521    | No file  | `fa8940bdbfff`  |
| 517    | No file  | `fa8940bdbfff`  |
| 510    | No file  | `fa8940bdbfff`  |
| 508    | No file  | `fa8940bdbfff`  |
| 504    | No file  | `fa8940bdbfff`  |
| 497    | No file  | `fa8940bdbfff`  |
| 491    | No file  | `fa8940bdbfff`  |
| 485    | No file  | `fa8940bdbfff`  |
| 478    | No file  | `fa8940bdbfff`  |
| 472    | No file  | `fa8940bdbfff`  |
| 466    | No file  | `fa8940bdbfff`  |
| 457    | No file  | `fa8940bdbfff`  |
| 452    | No file  | `fa8940bdbfff`  |
| 449    | No file  | `fa8940bdbfff`  |
| 435    | No file  | `fa8940bdbfff`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                   |
| --------------------- | -------- | -------------------------------------- |
| `zodiacsign.dbss`     | Required | Resolves each `zodiac_id` to sign data |
| `languagedata_en.loc` | Optional | English names for display              |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field          | Notes                                                  |
| ------------------- | ------------ | -------------- | ------------------------------------------------------ |
| `+0x00`             | char[4]      | magic          | ASCII `PABR`                                           |
| `+0x04`             | u32          | count          | Number of entries; observed 12                         |
| `+0x08`             | Entry[count] | entries        | See Entry                                              |
| `entries+0x00`      | String Table | string_table   | The PABR string table, here with no strings            |
| `string_table+0x00` | u32          | end_of_entries | Byte offset immediately after entries; observed `0x14` |
| `string_table+0x04` | u32          | zero           | Always 0                                               |

### Entry (1 byte)

| Offset  | Type | Field     | Notes                                                       |
| ------- | ---- | --------- | ----------------------------------------------------------- |
| `+0x00` | u8   | zodiac_id | The 1-based ID into `zodiacsign.dbss`; observed 1-12        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes    |
| ------- | ------------------ | ------------ | -------- |
| `+0x00` | u32                | string_count | Always 0 |
| `+0x04` | pstr[string_count] | strings      | Empty    |

## Reference Table

| Slot | Zodiac ID | English Name  |
| ---- | --------- | ------------- |
| 0    | 1         | Hammer        |
| 1    | 2         | Boat          |
| 2    | 3         | Shield        |
| 3    | 4         | Giant         |
| 4    | 5         | Camel         |
| 5    | 6         | Black Dragon  |
| 6    | 7         | Treant Owl    |
| 7    | 8         | Elephant      |
| 8    | 9         | Key           |
| 9    | 10        | Wagon         |
| 10   | 11        | Sealing Stone |
| 11   | 12        | Goblin        |

## Notes

- File size is 32 bytes: 8-byte header, 12 one-byte entries, and 12-byte trailer.
- Entry IDs match `zodiacsignoffset.dbss` exactly: `1..12`.
- `end_of_entries` is `20` decimal (`0x14`), equal to `8 + count`.
- Existing `zodiacsign.dbss` parsing does not require this file because the main and offset files already store the same zodiac IDs.
