# `variedtradecount.bss` Format

## Purpose

The Central Market trade counts by family points. A PABR list of family
point ranges; each row gives the range's first and last point value and
the trade count a family in that range gets on top. On client 3482 it
holds six ranges, from `0` to `500` points (`0` added) up to `2,501` to
`999,999` points (`30` added).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------------- | ----- | ------- | --------- |
| 1      | 1109 and later | `variedtradecount.bss` | 164   | 6 Row   | 24        |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `variedtradecount.bss` | 164 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6735746aac15`  |
| 3482   | Layout 1 | `6735746aac15`  |
| 3474   | Layout 1 | `6735746aac15`  |
| 3473   | Layout 1 | `6735746aac15`  |
| 3464   | Layout 1 | `6735746aac15`  |
| 3458   | Layout 1 | `6735746aac15`  |
| 3454   | Layout 1 | `6735746aac15`  |
| 3444   | Layout 1 | `6735746aac15`  |
| 3435   | Layout 1 | `6735746aac15`  |
| 3426   | Layout 1 | `6735746aac15`  |
| 3418   | Layout 1 | `6735746aac15`  |
| 3412   | Layout 1 | `6735746aac15`  |
| 3402   | Layout 1 | `6735746aac15`  |
| 3396   | Layout 1 | `6735746aac15`  |
| 3387   | Layout 1 | `6735746aac15`  |
| 3381   | Layout 1 | `6735746aac15`  |
| 3373   | Layout 1 | `6735746aac15`  |
| 3364   | Layout 1 | `6735746aac15`  |
| 3356   | Layout 1 | `6735746aac15`  |
| 3349   | Layout 1 | `6735746aac15`  |
| 3342   | Layout 1 | `6735746aac15`  |
| 3335   | Layout 1 | `6735746aac15`  |
| 3326   | Layout 1 | `6735746aac15`  |
| 3321   | Layout 1 | `6735746aac15`  |
| 3314   | Layout 1 | `6735746aac15`  |
| 3303   | Layout 1 | `6735746aac15`  |
| 3302   | Layout 1 | `6735746aac15`  |
| 3293   | Layout 1 | `6735746aac15`  |
| 3283   | Layout 1 | `6735746aac15`  |
| 3275   | Layout 1 | `6735746aac15`  |
| 3267   | Layout 1 | `6735746aac15`  |
| 3258   | Layout 1 | `6735746aac15`  |
| 3251   | Layout 1 | `6735746aac15`  |
| 3242   | Layout 1 | `6735746aac15`  |
| 3235   | Layout 1 | `6735746aac15`  |
| 3229   | Layout 1 | `6735746aac15`  |
| 3212   | Layout 1 | `6735746aac15`  |
| 3203   | Layout 1 | `6735746aac15`  |
| 3193   | Layout 1 | `6735746aac15`  |
| 3186   | Layout 1 | `6735746aac15`  |
| 3177   | Layout 1 | `6735746aac15`  |
| 3169   | Layout 1 | `6735746aac15`  |
| 3158   | Layout 1 | `6735746aac15`  |
| 3151   | Layout 1 | `6735746aac15`  |
| 3144   | Layout 1 | `6735746aac15`  |
| 3133   | Layout 1 | `6735746aac15`  |
| 3125   | Layout 1 | `6735746aac15`  |
| 3118   | Layout 1 | `6735746aac15`  |
| 3111   | Layout 1 | `6735746aac15`  |
| 3103   | Layout 1 | `6735746aac15`  |
| 3095   | Layout 1 | `6735746aac15`  |
| 3086   | Layout 1 | `6735746aac15`  |
| 3072   | Layout 1 | `6735746aac15`  |
| 3062   | Layout 1 | `6735746aac15`  |
| 3052   | Layout 1 | `6735746aac15`  |
| 3045   | Layout 1 | `6735746aac15`  |
| 3037   | Layout 1 | `6735746aac15`  |
| 3030   | Layout 1 | `6735746aac15`  |
| 3021   | Layout 1 | `6735746aac15`  |
| 3012   | Layout 1 | `6735746aac15`  |
| 3002   | Layout 1 | `6735746aac15`  |
| 2995   | Layout 1 | `6735746aac15`  |
| 2987   | Layout 1 | `6735746aac15`  |
| 2978   | Layout 1 | `6735746aac15`  |
| 2970   | Layout 1 | `6735746aac15`  |
| 2959   | Layout 1 | `6735746aac15`  |
| 2951   | Layout 1 | `6735746aac15`  |
| 2942   | Layout 1 | `6735746aac15`  |
| 2935   | Layout 1 | `6735746aac15`  |
| 2932   | Layout 1 | `6735746aac15`  |
| 2923   | Layout 1 | `6735746aac15`  |
| 2919   | Layout 1 | `6735746aac15`  |
| 2907   | Layout 1 | `6735746aac15`  |
| 2900   | Layout 1 | `6735746aac15`  |
| 2891   | Layout 1 | `6735746aac15`  |
| 2882   | Layout 1 | `6735746aac15`  |
| 2872   | Layout 1 | `6735746aac15`  |
| 2863   | Layout 1 | `6735746aac15`  |
| 2855   | Layout 1 | `6735746aac15`  |
| 2849   | Layout 1 | `6735746aac15`  |
| 2844   | Layout 1 | `6735746aac15`  |
| 2834   | Layout 1 | `6735746aac15`  |
| 2825   | Layout 1 | `6735746aac15`  |
| 2819   | Layout 1 | `6735746aac15`  |
| 2811   | Layout 1 | `6735746aac15`  |
| 2803   | Layout 1 | `6735746aac15`  |
| 2794   | Layout 1 | `6735746aac15`  |
| 2783   | Layout 1 | `6735746aac15`  |
| 2774   | Layout 1 | `6735746aac15`  |
| 2765   | Layout 1 | `6735746aac15`  |
| 2756   | Layout 1 | `6735746aac15`  |
| 2750   | Layout 1 | `6735746aac15`  |
| 2743   | Layout 1 | `6735746aac15`  |
| 2736   | Layout 1 | `6735746aac15`  |
| 2726   | Layout 1 | `6735746aac15`  |
| 2717   | Layout 1 | `6735746aac15`  |
| 2709   | Layout 1 | `6735746aac15`  |
| 2703   | Layout 1 | `6735746aac15`  |
| 2695   | Layout 1 | `6735746aac15`  |
| 2684   | Layout 1 | `6735746aac15`  |
| 2672   | Layout 1 | `6735746aac15`  |
| 2665   | Layout 1 | `6735746aac15`  |
| 2657   | Layout 1 | `6735746aac15`  |
| 2649   | Layout 1 | `6735746aac15`  |
| 2644   | Layout 1 | `6735746aac15`  |
| 2637   | Layout 1 | `6735746aac15`  |
| 2629   | Layout 1 | `6735746aac15`  |
| 2619   | Layout 1 | `6735746aac15`  |
| 2612   | Layout 1 | `6735746aac15`  |
| 2606   | Layout 1 | `6735746aac15`  |
| 2602   | Layout 1 | `6735746aac15`  |
| 2601   | Layout 1 | `6735746aac15`  |
| 2592   | Layout 1 | `6735746aac15`  |
| 2583   | Layout 1 | `6735746aac15`  |
| 2575   | Layout 1 | `6735746aac15`  |
| 2567   | Layout 1 | `6735746aac15`  |
| 2560   | Layout 1 | `6735746aac15`  |
| 2553   | Layout 1 | `6735746aac15`  |
| 2545   | Layout 1 | `6735746aac15`  |
| 2538   | Layout 1 | `6735746aac15`  |
| 2529   | Layout 1 | `6735746aac15`  |
| 2519   | Layout 1 | `6735746aac15`  |
| 2513   | Layout 1 | `6735746aac15`  |
| 2510   | Layout 1 | `6735746aac15`  |
| 2507   | Layout 1 | `6735746aac15`  |
| 2503   | Layout 1 | `6735746aac15`  |
| 2498   | Layout 1 | `6735746aac15`  |
| 2492   | Layout 1 | `6735746aac15`  |
| 2487   | Layout 1 | `6735746aac15`  |
| 2480   | Layout 1 | `6735746aac15`  |
| 2474   | Layout 1 | `6735746aac15`  |
| 2468   | Layout 1 | `6735746aac15`  |
| 2460   | Layout 1 | `6735746aac15`  |
| 2453   | Layout 1 | `6735746aac15`  |
| 2444   | Layout 1 | `6735746aac15`  |
| 2438   | Layout 1 | `6735746aac15`  |
| 2434   | Layout 1 | `6735746aac15`  |
| 2429   | Layout 1 | `6735746aac15`  |
| 2421   | Layout 1 | `6735746aac15`  |
| 2414   | Layout 1 | `6735746aac15`  |
| 2407   | Layout 1 | `6735746aac15`  |
| 2401   | Layout 1 | `6735746aac15`  |
| 2397   | Layout 1 | `6735746aac15`  |
| 2393   | Layout 1 | `6735746aac15`  |
| 2384   | Layout 1 | `6735746aac15`  |
| 2378   | Layout 1 | `6735746aac15`  |
| 2372   | Layout 1 | `6735746aac15`  |
| 2358   | Layout 1 | `6735746aac15`  |
| 2352   | Layout 1 | `6735746aac15`  |
| 2347   | Layout 1 | `6735746aac15`  |
| 2343   | Layout 1 | `6735746aac15`  |
| 2335   | Layout 1 | `6735746aac15`  |
| 2327   | Layout 1 | `6735746aac15`  |
| 2324   | Layout 1 | `6735746aac15`  |
| 2319   | Layout 1 | `6735746aac15`  |
| 2313   | Layout 1 | `6735746aac15`  |
| 2308   | Layout 1 | `6735746aac15`  |
| 2302   | Layout 1 | `6735746aac15`  |
| 2295   | Layout 1 | `6735746aac15`  |
| 2290   | Layout 1 | `6735746aac15`  |
| 2284   | Layout 1 | `6735746aac15`  |
| 2276   | Layout 1 | `6735746aac15`  |
| 2269   | Layout 1 | `6735746aac15`  |
| 2259   | Layout 1 | `6735746aac15`  |
| 2250   | Layout 1 | `6735746aac15`  |
| 2243   | Layout 1 | `6735746aac15`  |
| 2235   | Layout 1 | `6735746aac15`  |
| 2229   | Layout 1 | `6735746aac15`  |
| 2224   | Layout 1 | `6735746aac15`  |
| 2218   | Layout 1 | `6735746aac15`  |
| 2215   | Layout 1 | `6735746aac15`  |
| 2207   | Layout 1 | `6735746aac15`  |
| 2203   | Layout 1 | `6735746aac15`  |
| 2196   | Layout 1 | `6735746aac15`  |
| 2192   | Layout 1 | `6735746aac15`  |
| 2189   | Layout 1 | `6735746aac15`  |
| 2183   | Layout 1 | `6735746aac15`  |
| 2179   | Layout 1 | `6735746aac15`  |
| 2171   | Layout 1 | `6735746aac15`  |
| 2163   | Layout 1 | `6735746aac15`  |
| 2156   | Layout 1 | `6735746aac15`  |
| 2151   | Layout 1 | `6735746aac15`  |
| 2147   | Layout 1 | `6735746aac15`  |
| 2142   | Layout 1 | `6735746aac15`  |
| 2138   | Layout 1 | `6735746aac15`  |
| 2134   | Layout 1 | `6735746aac15`  |
| 2130   | Layout 1 | `6735746aac15`  |
| 2122   | Layout 1 | `6735746aac15`  |
| 2107   | Layout 1 | `6735746aac15`  |
| 2098   | Layout 1 | `6735746aac15`  |
| 2089   | Layout 1 | `6735746aac15`  |
| 2081   | Layout 1 | `6735746aac15`  |
| 2073   | Layout 1 | `6735746aac15`  |
| 2067   | Layout 1 | `6735746aac15`  |
| 2063   | Layout 1 | `6735746aac15`  |
| 2059   | Layout 1 | `6735746aac15`  |
| 2052   | Layout 1 | `6735746aac15`  |
| 2044   | Layout 1 | `6735746aac15`  |
| 2039   | Layout 1 | `6735746aac15`  |
| 2032   | Layout 1 | `6735746aac15`  |
| 2025   | Layout 1 | `6735746aac15`  |
| 2011   | Layout 1 | `6735746aac15`  |
| 2005   | Layout 1 | `6735746aac15`  |
| 2000   | Layout 1 | `6735746aac15`  |
| 1996   | Layout 1 | `6735746aac15`  |
| 1991   | Layout 1 | `6735746aac15`  |
| 1985   | Layout 1 | `6735746aac15`  |
| 1980   | Layout 1 | `6735746aac15`  |
| 1969   | Layout 1 | `6735746aac15`  |
| 1964   | Layout 1 | `6735746aac15`  |
| 1958   | Layout 1 | `6735746aac15`  |
| 1950   | Layout 1 | `6735746aac15`  |
| 1945   | Layout 1 | `6735746aac15`  |
| 1937   | Layout 1 | `6735746aac15`  |
| 1933   | Layout 1 | `6735746aac15`  |
| 1927   | Layout 1 | `6735746aac15`  |
| 1921   | Layout 1 | `6735746aac15`  |
| 1914   | Layout 1 | `6735746aac15`  |
| 1908   | Layout 1 | `6735746aac15`  |
| 1897   | Layout 1 | `6735746aac15`  |
| 1892   | Layout 1 | `6735746aac15`  |
| 1886   | Layout 1 | `6735746aac15`  |
| 1881   | Layout 1 | `6735746aac15`  |
| 1871   | Layout 1 | `6735746aac15`  |
| 1866   | Layout 1 | `6735746aac15`  |
| 1862   | Layout 1 | `6735746aac15`  |
| 1854   | Layout 1 | `6735746aac15`  |
| 1846   | Layout 1 | `6735746aac15`  |
| 1838   | Layout 1 | `6735746aac15`  |
| 1832   | Layout 1 | `6735746aac15`  |
| 1826   | Layout 1 | `6735746aac15`  |
| 1822   | Layout 1 | `6735746aac15`  |
| 1818   | Layout 1 | `6735746aac15`  |
| 1804   | Layout 1 | `6735746aac15`  |
| 1794   | Layout 1 | `6735746aac15`  |
| 1790   | Layout 1 | `6735746aac15`  |
| 1784   | Layout 1 | `6735746aac15`  |
| 1774   | Layout 1 | `6735746aac15`  |
| 1771   | Layout 1 | `6735746aac15`  |
| 1762   | Layout 1 | `6735746aac15`  |
| 1759   | Layout 1 | `6735746aac15`  |
| 1754   | Layout 1 | `6735746aac15`  |
| 1749   | Layout 1 | `6735746aac15`  |
| 1743   | Layout 1 | `6735746aac15`  |
| 1737   | Layout 1 | `6735746aac15`  |
| 1731   | Layout 1 | `6735746aac15`  |
| 1725   | Layout 1 | `6735746aac15`  |
| 1717   | Layout 1 | `6735746aac15`  |
| 1710   | Layout 1 | `6735746aac15`  |
| 1704   | Layout 1 | `6735746aac15`  |
| 1698   | Layout 1 | `6735746aac15`  |
| 1690   | Layout 1 | `6735746aac15`  |
| 1685   | Layout 1 | `6735746aac15`  |
| 1680   | Layout 1 | `6735746aac15`  |
| 1674   | Layout 1 | `6735746aac15`  |
| 1668   | Layout 1 | `6735746aac15`  |
| 1659   | Layout 1 | `6735746aac15`  |
| 1649   | Layout 1 | `6735746aac15`  |
| 1642   | Layout 1 | `6735746aac15`  |
| 1636   | Layout 1 | `6735746aac15`  |
| 1628   | Layout 1 | `6735746aac15`  |
| 1622   | Layout 1 | `6735746aac15`  |
| 1614   | Layout 1 | `6735746aac15`  |
| 1608   | Layout 1 | `6735746aac15`  |
| 1602   | Layout 1 | `6735746aac15`  |
| 1598   | Layout 1 | `6735746aac15`  |
| 1594   | Layout 1 | `6735746aac15`  |
| 1590   | Layout 1 | `6735746aac15`  |
| 1587   | Layout 1 | `6735746aac15`  |
| 1584   | Layout 1 | `6735746aac15`  |
| 1579   | Layout 1 | `6735746aac15`  |
| 1572   | Layout 1 | `6735746aac15`  |
| 1565   | Layout 1 | `6735746aac15`  |
| 1559   | Layout 1 | `6735746aac15`  |
| 1554   | Layout 1 | `6735746aac15`  |
| 1547   | Layout 1 | `6735746aac15`  |
| 1537   | Layout 1 | `6735746aac15`  |
| 1529   | Layout 1 | `6735746aac15`  |
| 1524   | Layout 1 | `6735746aac15`  |
| 1519   | Layout 1 | `6735746aac15`  |
| 1509   | Layout 1 | `6735746aac15`  |
| 1506   | Layout 1 | `6735746aac15`  |
| 1504   | Layout 1 | `6735746aac15`  |
| 1500   | Layout 1 | `6735746aac15`  |
| 1493   | Layout 1 | `6735746aac15`  |
| 1489   | Layout 1 | `6735746aac15`  |
| 1485   | Layout 1 | `6735746aac15`  |
| 1481   | Layout 1 | `6735746aac15`  |
| 1474   | Layout 1 | `6735746aac15`  |
| 1466   | Layout 1 | `6735746aac15`  |
| 1462   | Layout 1 | `6735746aac15`  |
| 1459   | Layout 1 | `6735746aac15`  |
| 1453   | Layout 1 | `6735746aac15`  |
| 1450   | Layout 1 | `6735746aac15`  |
| 1445   | Layout 1 | `6735746aac15`  |
| 1439   | Layout 1 | `6735746aac15`  |
| 1433   | Layout 1 | `6735746aac15`  |
| 1430   | Layout 1 | `6735746aac15`  |
| 1426   | Layout 1 | `6735746aac15`  |
| 1421   | Layout 1 | `6735746aac15`  |
| 1417   | Layout 1 | `6735746aac15`  |
| 1416   | Layout 1 | `6735746aac15`  |
| 1409   | Layout 1 | `6735746aac15`  |
| 1405   | Layout 1 | `6735746aac15`  |
| 1401   | Layout 1 | `6735746aac15`  |
| 1396   | Layout 1 | `6735746aac15`  |
| 1391   | Layout 1 | `6735746aac15`  |
| 1390   | Layout 1 | `6735746aac15`  |
| 1386   | Layout 1 | `6735746aac15`  |
| 1381   | Layout 1 | `6735746aac15`  |
| 1379   | Layout 1 | `6735746aac15`  |
| 1372   | Layout 1 | `6735746aac15`  |
| 1366   | Layout 1 | `6735746aac15`  |
| 1364   | Layout 1 | `6735746aac15`  |
| 1363   | Layout 1 | `6735746aac15`  |
| 1360   | Layout 1 | `6735746aac15`  |
| 1358   | Layout 1 | `6735746aac15`  |
| 1355   | Layout 1 | `6735746aac15`  |
| 1351   | Layout 1 | `6735746aac15`  |
| 1348   | Layout 1 | `6735746aac15`  |
| 1346   | Layout 1 | `6735746aac15`  |
| 1341   | Layout 1 | `6735746aac15`  |
| 1340   | Layout 1 | `6735746aac15`  |
| 1338   | Layout 1 | `6735746aac15`  |
| 1335   | Layout 1 | `6735746aac15`  |
| 1333   | Layout 1 | `6735746aac15`  |
| 1329   | Layout 1 | `6735746aac15`  |
| 1327   | Layout 1 | `6735746aac15`  |
| 1324   | Layout 1 | `6735746aac15`  |
| 1321   | Layout 1 | `6735746aac15`  |
| 1319   | Layout 1 | `6735746aac15`  |
| 1318   | Layout 1 | `6735746aac15`  |
| 1316   | Layout 1 | `6735746aac15`  |
| 1313   | Layout 1 | `6735746aac15`  |
| 1311   | Layout 1 | `6735746aac15`  |
| 1309   | Layout 1 | `6735746aac15`  |
| 1304   | Layout 1 | `6735746aac15`  |
| 1292   | Layout 1 | `6735746aac15`  |
| 1286   | Layout 1 | `6735746aac15`  |
| 1280   | Layout 1 | `6735746aac15`  |
| 1276   | Layout 1 | `6735746aac15`  |
| 1267   | Layout 1 | `6735746aac15`  |
| 1261   | Layout 1 | `6735746aac15`  |
| 1256   | Layout 1 | `6735746aac15`  |
| 1250   | Layout 1 | `6735746aac15`  |
| 1246   | Layout 1 | `6735746aac15`  |
| 1239   | Layout 1 | `6735746aac15`  |
| 1230   | Layout 1 | `6735746aac15`  |
| 1226   | Layout 1 | `6735746aac15`  |
| 1220   | Layout 1 | `6735746aac15`  |
| 1217   | Layout 1 | `6735746aac15`  |
| 1211   | Layout 1 | `6735746aac15`  |
| 1210   | Layout 1 | `6735746aac15`  |
| 1208   | Layout 1 | `6735746aac15`  |
| 1203   | Layout 1 | `6735746aac15`  |
| 1197   | Layout 1 | `6735746aac15`  |
| 1194   | Layout 1 | `6735746aac15`  |
| 1192   | Layout 1 | `6735746aac15`  |
| 1187   | Layout 1 | `6735746aac15`  |
| 1183   | Layout 1 | `6735746aac15`  |
| 1177   | Layout 1 | `6735746aac15`  |
| 1173   | Layout 1 | `6735746aac15`  |
| 1167   | Layout 1 | `6735746aac15`  |
| 1164   | Layout 1 | `6735746aac15`  |
| 1156   | Layout 1 | `6735746aac15`  |
| 1149   | Layout 1 | `6735746aac15`  |
| 1144   | Layout 1 | `6735746aac15`  |
| 1137   | Layout 1 | `6735746aac15`  |
| 1132   | Layout 1 | `6735746aac15`  |
| 1127   | Layout 1 | `6735746aac15`  |
| 1122   | Layout 1 | `6735746aac15`  |
| 1118   | Layout 1 | `6735746aac15`  |
| 1114   | Layout 1 | `6735746aac15`  |
| 1109   | Layout 1 | `6735746aac15`  |
| 1102   | No file  | `6735746aac15`  |
| 1096   | No file  | `6735746aac15`  |
| 1088   | No file  | `6735746aac15`  |
| 1081   | No file  | `6735746aac15`  |
| 1076   | No file  | `6735746aac15`  |
| 1069   | No file  | `6735746aac15`  |
| 1064   | No file  | `6735746aac15`  |
| 1058   | No file  | `6735746aac15`  |
| 1051   | No file  | `6735746aac15`  |
| 1044   | No file  | `6735746aac15`  |
| 1036   | No file  | `6735746aac15`  |
| 1026   | No file  | `6735746aac15`  |
| 1016   | No file  | `6735746aac15`  |
| 1009   | No file  | `6735746aac15`  |
| 1005   | No file  | `6735746aac15`  |
| 1000   | No file  | `6735746aac15`  |
| 998    | No file  | `6735746aac15`  |
| 990    | No file  | `6735746aac15`  |
| 979    | No file  | `6735746aac15`  |
| 972    | No file  | `6735746aac15`  |
| 963    | No file  | `6735746aac15`  |
| 955    | No file  | `6735746aac15`  |
| 946    | No file  | `6735746aac15`  |
| 938    | No file  | `6735746aac15`  |
| 927    | No file  | `6735746aac15`  |
| 911    | No file  | `6735746aac15`  |
| 904    | No file  | `6735746aac15`  |
| 899    | No file  | `6735746aac15`  |
| 894    | No file  | `6735746aac15`  |
| 885    | No file  | `6735746aac15`  |
| 879    | No file  | `6735746aac15`  |
| 872    | No file  | `6735746aac15`  |
| 864    | No file  | `6735746aac15`  |
| 855    | No file  | `6735746aac15`  |
| 853    | No file  | `6735746aac15`  |
| 845    | No file  | `6735746aac15`  |
| 837    | No file  | `6735746aac15`  |
| 829    | No file  | `6735746aac15`  |
| 822    | No file  | `6735746aac15`  |
| 814    | No file  | `6735746aac15`  |
| 805    | No file  | `6735746aac15`  |
| 794    | No file  | `6735746aac15`  |
| 787    | No file  | `6735746aac15`  |
| 780    | No file  | `6735746aac15`  |
| 771    | No file  | `6735746aac15`  |
| 760    | No file  | `6735746aac15`  |
| 748    | No file  | `6735746aac15`  |
| 741    | No file  | `6735746aac15`  |
| 736    | No file  | `6735746aac15`  |
| 731    | No file  | `6735746aac15`  |
| 723    | No file  | `6735746aac15`  |
| 711    | No file  | `6735746aac15`  |
| 707    | No file  | `6735746aac15`  |
| 697    | No file  | `6735746aac15`  |
| 689    | No file  | `6735746aac15`  |
| 683    | No file  | `6735746aac15`  |
| 678    | No file  | `6735746aac15`  |
| 670    | No file  | `6735746aac15`  |
| 661    | No file  | `6735746aac15`  |
| 656    | No file  | `6735746aac15`  |
| 652    | No file  | `6735746aac15`  |
| 643    | No file  | `6735746aac15`  |
| 637    | No file  | `6735746aac15`  |
| 630    | No file  | `6735746aac15`  |
| 627    | No file  | `6735746aac15`  |
| 621    | No file  | `6735746aac15`  |
| 617    | No file  | `6735746aac15`  |
| 615    | No file  | `6735746aac15`  |
| 606    | No file  | `6735746aac15`  |
| 599    | No file  | `6735746aac15`  |
| 592    | No file  | `6735746aac15`  |
| 586    | No file  | `6735746aac15`  |
| 577    | No file  | `6735746aac15`  |
| 569    | No file  | `6735746aac15`  |
| 561    | No file  | `6735746aac15`  |
| 554    | No file  | `6735746aac15`  |
| 542    | No file  | `6735746aac15`  |
| 532    | No file  | `6735746aac15`  |
| 531    | No file  | `6735746aac15`  |
| 526    | No file  | `6735746aac15`  |
| 521    | No file  | `6735746aac15`  |
| 517    | No file  | `6735746aac15`  |
| 510    | No file  | `6735746aac15`  |
| 508    | No file  | `6735746aac15`  |
| 504    | No file  | `6735746aac15`  |
| 497    | No file  | `6735746aac15`  |
| 491    | No file  | `6735746aac15`  |
| 485    | No file  | `6735746aac15`  |
| 478    | No file  | `6735746aac15`  |
| 472    | No file  | `6735746aac15`  |
| 466    | No file  | `6735746aac15`  |
| 457    | No file  | `6735746aac15`  |
| 452    | No file  | `6735746aac15`  |
| 449    | No file  | `6735746aac15`  |
| 435    | No file  | `6735746aac15`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of family point ranges                 |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (24 bytes)

| Offset  | Type | Field            | Notes                                                                          |
| ------- | ---- | ---------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u64  | min_family_point | First family point value of the range; one more than the previous row's max    |
| `+0x08` | u64  | max_family_point | Last family point value of the range                                           |
| `+0x10` | u64  | add_trade_count  | Trade count added in the range: `0`, `5`, `10`, `15`, `20`, `30` on client 3482 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names are the `MinFamilyPoint`, `MaxFamilyPoint` and `AddTradeCount`
columns of the `WorldMarketVariedTradeCount` sheet of a private server's
`DataSheets.bexcel` on client 1784, in that order. The client 1784 file
and the client 3482 file hold the same six rows, and all 6 of 6 match the
sheet on all three columns. The `WorldMarketVariedTradeCount` table of a
private server on client 519 has the same columns; its last
`MaxFamilyPoint` is `9999` where the files hold `999,999`.

## Notes

- The ranges are `0` to `500`, `501` to `1,000`, `1,001` to `1,500`,
  `1,501` to `2,000`, `2,001` to `2,500` and `2,501` to `999,999` on
  client 3482.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/server_tables.py`.

## Open Questions

### Which Trade Count the Rows Raise

`add_trade_count` keeps its sheet name; the client Lua does not name the
table, so which Central Market count it adds to is open, and so is whether
the family points are the family's Family Fame.
