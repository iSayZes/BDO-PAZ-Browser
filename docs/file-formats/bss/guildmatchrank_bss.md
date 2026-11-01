# `guildmatchrank.bss` Format

## Purpose

The point ranges of the Guild League ranks: one row per rank with the
lowest and highest point of its range. On client 3474 the file has 20
rows; rank `1` covers `3801` to `99999` points and each lower rank the 200
points below it, down to rank `20` at `0` to `200`. The ranges join
without a gap. The Guild League rewards and options are in
[guildmatchoption](guildmatchoption_bss.md), its EXP in
[guildmatchexp](guildmatchexp_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | -------------------- | ----- | ------- | --------- |
| 1      | 2429 and later | `guildmatchrank.bss` | 380   | 20 Row  | 18        |

| Layout | File                 | Known         | Unknown       |
| ------ | -------------------- | ------------- | ------------- |
| 1      | `guildmatchrank.bss` | 220 B (57.9%) | 160 B (42.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `227e27a9247a`  |
| 3482   | Layout 1             | `227e27a9247a`  |
| 3474   | Layout 1             | `227e27a9247a`  |
| 3473   | Layout 1             | `227e27a9247a`  |
| 3464   | Layout 1             | `227e27a9247a`  |
| 3458   | Layout 1             | `227e27a9247a`  |
| 3454   | Layout 1             | `227e27a9247a`  |
| 3444   | Layout 1             | `227e27a9247a`  |
| 3435   | Layout 1             | `227e27a9247a`  |
| 3426   | Layout 1             | `227e27a9247a`  |
| 3418   | Layout 1             | `227e27a9247a`  |
| 3412   | Layout 1             | `227e27a9247a`  |
| 3402   | Layout 1             | `227e27a9247a`  |
| 3396   | Layout 1             | `227e27a9247a`  |
| 3387   | Layout 1             | `227e27a9247a`  |
| 3381   | Layout 1             | `227e27a9247a`  |
| 3373   | Layout 1             | `227e27a9247a`  |
| 3364   | Layout 1             | `227e27a9247a`  |
| 3356   | Layout 1             | `227e27a9247a`  |
| 3349   | Layout 1             | `227e27a9247a`  |
| 3342   | Layout 1             | `227e27a9247a`  |
| 3335   | Layout 1             | `227e27a9247a`  |
| 3326   | Layout 1             | `227e27a9247a`  |
| 3321   | Layout 1             | `227e27a9247a`  |
| 3314   | Layout 1             | `227e27a9247a`  |
| 3303   | Layout 1             | `227e27a9247a`  |
| 3302   | Layout 1             | `227e27a9247a`  |
| 3293   | Layout 1             | `227e27a9247a`  |
| 3283   | Layout 1             | `227e27a9247a`  |
| 3275   | Layout 1             | `227e27a9247a`  |
| 3267   | Layout 1             | `227e27a9247a`  |
| 3258   | Layout 1             | `227e27a9247a`  |
| 3251   | Layout 1             | `227e27a9247a`  |
| 3242   | Layout 1             | `227e27a9247a`  |
| 3235   | Layout 1             | `227e27a9247a`  |
| 3229   | Layout 1             | `227e27a9247a`  |
| 3212   | Layout 1             | `227e27a9247a`  |
| 3203   | Layout 1             | `227e27a9247a`  |
| 3193   | Layout 1             | `227e27a9247a`  |
| 3186   | Layout 1             | `227e27a9247a`  |
| 3177   | Layout 1             | `227e27a9247a`  |
| 3169   | Layout 1             | `227e27a9247a`  |
| 3158   | Layout 1             | `227e27a9247a`  |
| 3151   | Layout 1             | `227e27a9247a`  |
| 3144   | Layout 1             | `227e27a9247a`  |
| 3133   | Layout 1             | `227e27a9247a`  |
| 3125   | Layout 1             | `227e27a9247a`  |
| 3118   | Layout 1             | `227e27a9247a`  |
| 3111   | Layout 1             | `227e27a9247a`  |
| 3103   | Layout 1             | `227e27a9247a`  |
| 3095   | Layout 1             | `227e27a9247a`  |
| 3086   | Layout 1             | `227e27a9247a`  |
| 3072   | Layout 1             | `227e27a9247a`  |
| 3062   | Layout 1             | `227e27a9247a`  |
| 3052   | Layout 1             | `227e27a9247a`  |
| 3045   | Layout 1             | `227e27a9247a`  |
| 3037   | Layout 1             | `227e27a9247a`  |
| 3030   | Layout 1             | `227e27a9247a`  |
| 3021   | Layout 1             | `227e27a9247a`  |
| 3012   | Layout 1             | `227e27a9247a`  |
| 3002   | Layout 1             | `227e27a9247a`  |
| 2995   | Layout 1             | `227e27a9247a`  |
| 2987   | Layout 1             | `227e27a9247a`  |
| 2978   | Layout 1             | `227e27a9247a`  |
| 2970   | Layout 1             | `227e27a9247a`  |
| 2959   | Layout 1             | `227e27a9247a`  |
| 2951   | Layout 1             | `227e27a9247a`  |
| 2942   | Layout 1             | `227e27a9247a`  |
| 2935   | Layout 1             | `227e27a9247a`  |
| 2932   | Layout 1             | `227e27a9247a`  |
| 2923   | Layout 1             | `227e27a9247a`  |
| 2919   | Layout 1             | `227e27a9247a`  |
| 2907   | Layout 1             | `227e27a9247a`  |
| 2900   | Layout 1             | `227e27a9247a`  |
| 2891   | Layout 1             | `227e27a9247a`  |
| 2882   | Layout 1             | `227e27a9247a`  |
| 2872   | Layout 1             | `227e27a9247a`  |
| 2863   | Layout 1             | `227e27a9247a`  |
| 2855   | Layout 1             | `227e27a9247a`  |
| 2849   | Layout 1             | `227e27a9247a`  |
| 2844   | Layout 1             | `227e27a9247a`  |
| 2834   | Layout 1             | `227e27a9247a`  |
| 2825   | Layout 1             | `227e27a9247a`  |
| 2819   | Layout 1             | `227e27a9247a`  |
| 2811   | Layout 1             | `227e27a9247a`  |
| 2803   | Layout 1             | `227e27a9247a`  |
| 2794   | Layout 1             | `227e27a9247a`  |
| 2783   | Layout 1             | `227e27a9247a`  |
| 2774   | Layout 1             | `227e27a9247a`  |
| 2765   | Layout 1             | `227e27a9247a`  |
| 2756   | Layout 1             | `227e27a9247a`  |
| 2750   | Layout 1             | `227e27a9247a`  |
| 2743   | Layout 1             | `227e27a9247a`  |
| 2736   | Layout 1             | `227e27a9247a`  |
| 2726   | Layout 1             | `227e27a9247a`  |
| 2717   | Layout 1             | `227e27a9247a`  |
| 2709   | Layout 1             | `227e27a9247a`  |
| 2703   | Layout 1             | `227e27a9247a`  |
| 2695   | Layout 1             | `227e27a9247a`  |
| 2684   | Layout 1             | `227e27a9247a`  |
| 2672   | Layout 1             | `227e27a9247a`  |
| 2665   | Layout 1             | `227e27a9247a`  |
| 2657   | Layout 1             | `227e27a9247a`  |
| 2649   | Layout 1             | `227e27a9247a`  |
| 2644   | Layout 1             | `227e27a9247a`  |
| 2637   | Layout 1             | `227e27a9247a`  |
| 2629   | Layout 1             | `227e27a9247a`  |
| 2619   | Layout 1             | `227e27a9247a`  |
| 2612   | Layout 1             | `227e27a9247a`  |
| 2606   | Layout 1             | `227e27a9247a`  |
| 2602   | Layout 1             | `227e27a9247a`  |
| 2601   | Layout 1             | `227e27a9247a`  |
| 2592   | Layout 1             | `227e27a9247a`  |
| 2583   | Layout 1             | `227e27a9247a`  |
| 2575   | Layout 1             | `227e27a9247a`  |
| 2567   | Layout 1             | `227e27a9247a`  |
| 2560   | Layout 1             | `227e27a9247a`  |
| 2553   | Layout 1             | `227e27a9247a`  |
| 2545   | Layout 1             | `227e27a9247a`  |
| 2538   | Layout 1             | `227e27a9247a`  |
| 2529   | Layout 1             | `227e27a9247a`  |
| 2519   | Layout 1             | `227e27a9247a`  |
| 2513   | Layout 1             | `227e27a9247a`  |
| 2510   | Layout 1             | `227e27a9247a`  |
| 2507   | Layout 1             | `227e27a9247a`  |
| 2503   | Layout 1             | `227e27a9247a`  |
| 2498   | Layout 1             | `227e27a9247a`  |
| 2492   | Layout 1             | `227e27a9247a`  |
| 2487   | Layout 1             | `227e27a9247a`  |
| 2480   | Layout 1             | `227e27a9247a`  |
| 2474   | Layout 1             | `227e27a9247a`  |
| 2468   | Layout 1             | `227e27a9247a`  |
| 2460   | Layout 1             | `227e27a9247a`  |
| 2453   | Layout 1             | `227e27a9247a`  |
| 2444   | No documented layout | `227e27a9247a`  |
| 2438   | No documented layout | `227e27a9247a`  |
| 2434   | No documented layout | `227e27a9247a`  |
| 2429   | Layout 1             | `227e27a9247a`  |
| 2421   | No file              | `227e27a9247a`  |
| 2414   | No file              | `227e27a9247a`  |
| 2407   | No file              | `227e27a9247a`  |
| 2401   | No file              | `227e27a9247a`  |
| 2397   | No file              | `227e27a9247a`  |
| 2393   | No file              | `227e27a9247a`  |
| 2384   | No file              | `227e27a9247a`  |
| 2378   | No file              | `227e27a9247a`  |
| 2372   | No file              | `227e27a9247a`  |
| 2358   | No file              | `227e27a9247a`  |
| 2352   | No file              | `227e27a9247a`  |
| 2347   | No file              | `227e27a9247a`  |
| 2343   | No file              | `227e27a9247a`  |
| 2335   | No file              | `227e27a9247a`  |
| 2327   | No file              | `227e27a9247a`  |
| 2324   | No file              | `227e27a9247a`  |
| 2319   | No file              | `227e27a9247a`  |
| 2313   | No file              | `227e27a9247a`  |
| 2308   | No file              | `227e27a9247a`  |
| 2302   | No file              | `227e27a9247a`  |
| 2295   | No file              | `227e27a9247a`  |
| 2290   | No file              | `227e27a9247a`  |
| 2284   | No file              | `227e27a9247a`  |
| 2276   | No file              | `227e27a9247a`  |
| 2269   | No file              | `227e27a9247a`  |
| 2259   | No file              | `227e27a9247a`  |
| 2250   | No file              | `227e27a9247a`  |
| 2243   | No file              | `227e27a9247a`  |
| 2235   | No file              | `227e27a9247a`  |
| 2229   | No file              | `227e27a9247a`  |
| 2224   | No file              | `227e27a9247a`  |
| 2218   | No file              | `227e27a9247a`  |
| 2215   | No file              | `227e27a9247a`  |
| 2207   | No file              | `227e27a9247a`  |
| 2203   | No file              | `227e27a9247a`  |
| 2196   | No file              | `227e27a9247a`  |
| 2192   | No file              | `227e27a9247a`  |
| 2189   | No file              | `227e27a9247a`  |
| 2183   | No file              | `227e27a9247a`  |
| 2179   | No file              | `227e27a9247a`  |
| 2171   | No file              | `227e27a9247a`  |
| 2163   | No file              | `227e27a9247a`  |
| 2156   | No file              | `227e27a9247a`  |
| 2151   | No file              | `227e27a9247a`  |
| 2147   | No file              | `227e27a9247a`  |
| 2142   | No file              | `227e27a9247a`  |
| 2138   | No file              | `227e27a9247a`  |
| 2134   | No file              | `227e27a9247a`  |
| 2130   | No file              | `227e27a9247a`  |
| 2122   | No file              | `227e27a9247a`  |
| 2107   | No file              | `227e27a9247a`  |
| 2098   | No file              | `227e27a9247a`  |
| 2089   | No file              | `227e27a9247a`  |
| 2081   | No file              | `227e27a9247a`  |
| 2073   | No file              | `227e27a9247a`  |
| 2067   | No file              | `227e27a9247a`  |
| 2063   | No file              | `227e27a9247a`  |
| 2059   | No file              | `227e27a9247a`  |
| 2052   | No file              | `227e27a9247a`  |
| 2044   | No file              | `227e27a9247a`  |
| 2039   | No file              | `227e27a9247a`  |
| 2032   | No file              | `227e27a9247a`  |
| 2025   | No file              | `227e27a9247a`  |
| 2011   | No file              | `227e27a9247a`  |
| 2005   | No file              | `227e27a9247a`  |
| 2000   | No file              | `227e27a9247a`  |
| 1996   | No file              | `227e27a9247a`  |
| 1991   | No file              | `227e27a9247a`  |
| 1985   | No file              | `227e27a9247a`  |
| 1980   | No file              | `227e27a9247a`  |
| 1969   | No file              | `227e27a9247a`  |
| 1964   | No file              | `227e27a9247a`  |
| 1958   | No file              | `227e27a9247a`  |
| 1950   | No file              | `227e27a9247a`  |
| 1945   | No file              | `227e27a9247a`  |
| 1937   | No file              | `227e27a9247a`  |
| 1933   | No file              | `227e27a9247a`  |
| 1927   | No file              | `227e27a9247a`  |
| 1921   | No file              | `227e27a9247a`  |
| 1914   | No file              | `227e27a9247a`  |
| 1908   | No file              | `227e27a9247a`  |
| 1897   | No file              | `227e27a9247a`  |
| 1892   | No file              | `227e27a9247a`  |
| 1886   | No file              | `227e27a9247a`  |
| 1881   | No file              | `227e27a9247a`  |
| 1871   | No file              | `227e27a9247a`  |
| 1866   | No file              | `227e27a9247a`  |
| 1862   | No file              | `227e27a9247a`  |
| 1854   | No file              | `227e27a9247a`  |
| 1846   | No file              | `227e27a9247a`  |
| 1838   | No file              | `227e27a9247a`  |
| 1832   | No file              | `227e27a9247a`  |
| 1826   | No file              | `227e27a9247a`  |
| 1822   | No file              | `227e27a9247a`  |
| 1818   | No file              | `227e27a9247a`  |
| 1804   | No file              | `227e27a9247a`  |
| 1794   | No file              | `227e27a9247a`  |
| 1790   | No file              | `227e27a9247a`  |
| 1784   | No file              | `227e27a9247a`  |
| 1774   | No file              | `227e27a9247a`  |
| 1771   | No file              | `227e27a9247a`  |
| 1762   | No file              | `227e27a9247a`  |
| 1759   | No file              | `227e27a9247a`  |
| 1754   | No file              | `227e27a9247a`  |
| 1749   | No file              | `227e27a9247a`  |
| 1743   | No file              | `227e27a9247a`  |
| 1737   | No file              | `227e27a9247a`  |
| 1731   | No file              | `227e27a9247a`  |
| 1725   | No file              | `227e27a9247a`  |
| 1717   | No file              | `227e27a9247a`  |
| 1710   | No file              | `227e27a9247a`  |
| 1704   | No file              | `227e27a9247a`  |
| 1698   | No file              | `227e27a9247a`  |
| 1690   | No file              | `227e27a9247a`  |
| 1685   | No file              | `227e27a9247a`  |
| 1680   | No file              | `227e27a9247a`  |
| 1674   | No file              | `227e27a9247a`  |
| 1668   | No file              | `227e27a9247a`  |
| 1659   | No file              | `227e27a9247a`  |
| 1649   | No file              | `227e27a9247a`  |
| 1642   | No file              | `227e27a9247a`  |
| 1636   | No file              | `227e27a9247a`  |
| 1628   | No file              | `227e27a9247a`  |
| 1622   | No file              | `227e27a9247a`  |
| 1614   | No file              | `227e27a9247a`  |
| 1608   | No file              | `227e27a9247a`  |
| 1602   | No file              | `227e27a9247a`  |
| 1598   | No file              | `227e27a9247a`  |
| 1594   | No file              | `227e27a9247a`  |
| 1590   | No file              | `227e27a9247a`  |
| 1587   | No file              | `227e27a9247a`  |
| 1584   | No file              | `227e27a9247a`  |
| 1579   | No file              | `227e27a9247a`  |
| 1572   | No file              | `227e27a9247a`  |
| 1565   | No file              | `227e27a9247a`  |
| 1559   | No file              | `227e27a9247a`  |
| 1554   | No file              | `227e27a9247a`  |
| 1547   | No file              | `227e27a9247a`  |
| 1537   | No file              | `227e27a9247a`  |
| 1529   | No file              | `227e27a9247a`  |
| 1524   | No file              | `227e27a9247a`  |
| 1519   | No file              | `227e27a9247a`  |
| 1509   | No file              | `227e27a9247a`  |
| 1506   | No file              | `227e27a9247a`  |
| 1504   | No file              | `227e27a9247a`  |
| 1500   | No file              | `227e27a9247a`  |
| 1493   | No file              | `227e27a9247a`  |
| 1489   | No file              | `227e27a9247a`  |
| 1485   | No file              | `227e27a9247a`  |
| 1481   | No file              | `227e27a9247a`  |
| 1474   | No file              | `227e27a9247a`  |
| 1466   | No file              | `227e27a9247a`  |
| 1462   | No file              | `227e27a9247a`  |
| 1459   | No file              | `227e27a9247a`  |
| 1453   | No file              | `227e27a9247a`  |
| 1450   | No file              | `227e27a9247a`  |
| 1445   | No file              | `227e27a9247a`  |
| 1439   | No file              | `227e27a9247a`  |
| 1433   | No file              | `227e27a9247a`  |
| 1430   | No file              | `227e27a9247a`  |
| 1426   | No file              | `227e27a9247a`  |
| 1421   | No file              | `227e27a9247a`  |
| 1417   | No file              | `227e27a9247a`  |
| 1416   | No file              | `227e27a9247a`  |
| 1409   | No file              | `227e27a9247a`  |
| 1405   | No file              | `227e27a9247a`  |
| 1401   | No file              | `227e27a9247a`  |
| 1396   | No file              | `227e27a9247a`  |
| 1391   | No file              | `227e27a9247a`  |
| 1390   | No file              | `227e27a9247a`  |
| 1386   | No file              | `227e27a9247a`  |
| 1381   | No file              | `227e27a9247a`  |
| 1379   | No file              | `227e27a9247a`  |
| 1372   | No file              | `227e27a9247a`  |
| 1366   | No file              | `227e27a9247a`  |
| 1364   | No file              | `227e27a9247a`  |
| 1363   | No file              | `227e27a9247a`  |
| 1360   | No file              | `227e27a9247a`  |
| 1358   | No file              | `227e27a9247a`  |
| 1355   | No file              | `227e27a9247a`  |
| 1351   | No file              | `227e27a9247a`  |
| 1348   | No file              | `227e27a9247a`  |
| 1346   | No file              | `227e27a9247a`  |
| 1341   | No file              | `227e27a9247a`  |
| 1340   | No file              | `227e27a9247a`  |
| 1338   | No file              | `227e27a9247a`  |
| 1335   | No file              | `227e27a9247a`  |
| 1333   | No file              | `227e27a9247a`  |
| 1329   | No file              | `227e27a9247a`  |
| 1327   | No file              | `227e27a9247a`  |
| 1324   | No file              | `227e27a9247a`  |
| 1321   | No file              | `227e27a9247a`  |
| 1319   | No file              | `227e27a9247a`  |
| 1318   | No file              | `227e27a9247a`  |
| 1316   | No file              | `227e27a9247a`  |
| 1313   | No file              | `227e27a9247a`  |
| 1311   | No file              | `227e27a9247a`  |
| 1309   | No file              | `227e27a9247a`  |
| 1304   | No file              | `227e27a9247a`  |
| 1292   | No file              | `227e27a9247a`  |
| 1286   | No file              | `227e27a9247a`  |
| 1280   | No file              | `227e27a9247a`  |
| 1276   | No file              | `227e27a9247a`  |
| 1267   | No file              | `227e27a9247a`  |
| 1261   | No file              | `227e27a9247a`  |
| 1256   | No file              | `227e27a9247a`  |
| 1250   | No file              | `227e27a9247a`  |
| 1246   | No file              | `227e27a9247a`  |
| 1239   | No file              | `227e27a9247a`  |
| 1230   | No file              | `227e27a9247a`  |
| 1226   | No file              | `227e27a9247a`  |
| 1220   | No file              | `227e27a9247a`  |
| 1217   | No file              | `227e27a9247a`  |
| 1211   | No file              | `227e27a9247a`  |
| 1210   | No file              | `227e27a9247a`  |
| 1208   | No file              | `227e27a9247a`  |
| 1203   | No file              | `227e27a9247a`  |
| 1197   | No file              | `227e27a9247a`  |
| 1194   | No file              | `227e27a9247a`  |
| 1192   | No file              | `227e27a9247a`  |
| 1187   | No file              | `227e27a9247a`  |
| 1183   | No file              | `227e27a9247a`  |
| 1177   | No file              | `227e27a9247a`  |
| 1173   | No file              | `227e27a9247a`  |
| 1167   | No file              | `227e27a9247a`  |
| 1164   | No file              | `227e27a9247a`  |
| 1156   | No file              | `227e27a9247a`  |
| 1149   | No file              | `227e27a9247a`  |
| 1144   | No file              | `227e27a9247a`  |
| 1137   | No file              | `227e27a9247a`  |
| 1132   | No file              | `227e27a9247a`  |
| 1127   | No file              | `227e27a9247a`  |
| 1122   | No file              | `227e27a9247a`  |
| 1118   | No file              | `227e27a9247a`  |
| 1114   | No file              | `227e27a9247a`  |
| 1109   | No file              | `227e27a9247a`  |
| 1102   | No file              | `227e27a9247a`  |
| 1096   | No file              | `227e27a9247a`  |
| 1088   | No file              | `227e27a9247a`  |
| 1081   | No file              | `227e27a9247a`  |
| 1076   | No file              | `227e27a9247a`  |
| 1069   | No file              | `227e27a9247a`  |
| 1064   | No file              | `227e27a9247a`  |
| 1058   | No file              | `227e27a9247a`  |
| 1051   | No file              | `227e27a9247a`  |
| 1044   | No file              | `227e27a9247a`  |
| 1036   | No file              | `227e27a9247a`  |
| 1026   | No file              | `227e27a9247a`  |
| 1016   | No file              | `227e27a9247a`  |
| 1009   | No file              | `227e27a9247a`  |
| 1005   | No file              | `227e27a9247a`  |
| 1000   | No file              | `227e27a9247a`  |
| 998    | No file              | `227e27a9247a`  |
| 990    | No file              | `227e27a9247a`  |
| 979    | No file              | `227e27a9247a`  |
| 972    | No file              | `227e27a9247a`  |
| 963    | No file              | `227e27a9247a`  |
| 955    | No file              | `227e27a9247a`  |
| 946    | No file              | `227e27a9247a`  |
| 938    | No file              | `227e27a9247a`  |
| 927    | No file              | `227e27a9247a`  |
| 911    | No file              | `227e27a9247a`  |
| 904    | No file              | `227e27a9247a`  |
| 899    | No file              | `227e27a9247a`  |
| 894    | No file              | `227e27a9247a`  |
| 885    | No file              | `227e27a9247a`  |
| 879    | No file              | `227e27a9247a`  |
| 872    | No file              | `227e27a9247a`  |
| 864    | No file              | `227e27a9247a`  |
| 855    | No file              | `227e27a9247a`  |
| 853    | No file              | `227e27a9247a`  |
| 845    | No file              | `227e27a9247a`  |
| 837    | No file              | `227e27a9247a`  |
| 829    | No file              | `227e27a9247a`  |
| 822    | No file              | `227e27a9247a`  |
| 814    | No file              | `227e27a9247a`  |
| 805    | No file              | `227e27a9247a`  |
| 794    | No file              | `227e27a9247a`  |
| 787    | No file              | `227e27a9247a`  |
| 780    | No file              | `227e27a9247a`  |
| 771    | No file              | `227e27a9247a`  |
| 760    | No file              | `227e27a9247a`  |
| 748    | No file              | `227e27a9247a`  |
| 741    | No file              | `227e27a9247a`  |
| 736    | No file              | `227e27a9247a`  |
| 731    | No file              | `227e27a9247a`  |
| 723    | No file              | `227e27a9247a`  |
| 711    | No file              | `227e27a9247a`  |
| 707    | No file              | `227e27a9247a`  |
| 697    | No file              | `227e27a9247a`  |
| 689    | No file              | `227e27a9247a`  |
| 683    | No file              | `227e27a9247a`  |
| 678    | No file              | `227e27a9247a`  |
| 670    | No file              | `227e27a9247a`  |
| 661    | No file              | `227e27a9247a`  |
| 656    | No file              | `227e27a9247a`  |
| 652    | No file              | `227e27a9247a`  |
| 643    | No file              | `227e27a9247a`  |
| 637    | No file              | `227e27a9247a`  |
| 630    | No file              | `227e27a9247a`  |
| 627    | No file              | `227e27a9247a`  |
| 621    | No file              | `227e27a9247a`  |
| 617    | No file              | `227e27a9247a`  |
| 615    | No file              | `227e27a9247a`  |
| 606    | No file              | `227e27a9247a`  |
| 599    | No file              | `227e27a9247a`  |
| 592    | No file              | `227e27a9247a`  |
| 586    | No file              | `227e27a9247a`  |
| 577    | No file              | `227e27a9247a`  |
| 569    | No file              | `227e27a9247a`  |
| 561    | No file              | `227e27a9247a`  |
| 554    | No file              | `227e27a9247a`  |
| 542    | No file              | `227e27a9247a`  |
| 532    | No file              | `227e27a9247a`  |
| 531    | No file              | `227e27a9247a`  |
| 526    | No file              | `227e27a9247a`  |
| 521    | No file              | `227e27a9247a`  |
| 517    | No file              | `227e27a9247a`  |
| 510    | No file              | `227e27a9247a`  |
| 508    | No file              | `227e27a9247a`  |
| 504    | No file              | `227e27a9247a`  |
| 497    | No file              | `227e27a9247a`  |
| 491    | No file              | `227e27a9247a`  |
| 485    | No file              | `227e27a9247a`  |
| 478    | No file              | `227e27a9247a`  |
| 472    | No file              | `227e27a9247a`  |
| 466    | No file              | `227e27a9247a`  |
| 457    | No file              | `227e27a9247a`  |
| 452    | No file              | `227e27a9247a`  |
| 449    | No file              | `227e27a9247a`  |
| 435    | No file              | `227e27a9247a`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed, in rank order           |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (18 bytes)

| Offset  | Type | Field      | Notes                                                                         |
| ------- | ---- | ---------- | ----------------------------------------------------------------------------- |
| `+0x00` | u16  | unknown_00 | `0` on every row (clients 2519 to 3474)                                        |
| `+0x02` | u32  | rank       | Row key, `1` to `row_count`; `1` has the highest range                        |
| `+0x06` | u8   | unknown_06 | `0` on every row (clients 2519 to 3474)                                        |
| `+0x07` | u16  | min_point  | Lowest point of the range; `0` on the last rank                               |
| `+0x09` | u32  | max_point  | Highest point of the range, the next higher rank's `min_point` minus 1        |
| `+0x0D` | u8   | unknown_0d | `5` on ranks 1 to 10, else `0` (client 3474)                                   |
| `+0x0E` | u8   | unknown_0e | `2` on ranks 1 to 10, else `0` (client 3474)                                   |
| `+0x0F` | u8   | unknown_0f | `50` on ranks 1 to 3, `40` on 4 to 7, `30` on 8 to 10, else `0` (client 3474)  |
| `+0x10` | u8   | unknown_10 | `3`, `5` and `7` on ranks 18, 19 and 20, else `0` (client 3474)                |
| `+0x11` | u8   | unknown_11 | Equal to `unknown_10` on every row (clients 2519 to 3474)                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The Guild League is newer than client 1784 and 2107, which do not ship the
file, so no sheet of a private server's `DataSheets.bexcel` covers it. The
names describe what the bytes hold: `rank` counts the rows from `1`, and
`min_point` and `max_point` bound one range each, the ranges joining from
`0` up to `99999` (client 3474). The client Lua shows a guild's league
points with `getRankPoint()` (`panel_window_guildmatch_rank_1.luac`); that
these ranges are in those points is the reading, not a confirmed fact.
`min_point` is a u16 next to a u32 `max_point`: a u32 at `+0x05` or `+0x07`
would take bytes of its neighbours on every row.

## Notes

- Client 2519 has 10 ranks: ranks 2 to 10 of 200 points each from `0` to
  `1800`, rank `1` at `1801` to `9999`. There `unknown_0d` and
  `unknown_0e` are `5` and `2` on ranks 1 to 3, `unknown_0f` is `50`, `40`
  and `30` on ranks 1 to 3, and `unknown_10` is `3` and `5` on ranks 9 and
  10. Clients 3002 to 3474 have the 20 ranks above.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`.

## Open Questions

### Rank Bonus Bytes

What `unknown_0d`, `unknown_0e` and `unknown_0f` set on the upper ranks
and `unknown_10` and `unknown_11` on the lowest three. They change with the
rank only, which fits a per-rank reward or matchmaking setting; the Lua
reads none of them by name.
