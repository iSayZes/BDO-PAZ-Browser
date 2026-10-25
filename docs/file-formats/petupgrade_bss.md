# `petupgrade.bss` Format

## Purpose

The item cost of Tier 5 Pet Training, per pet tier. On client 3474 the file
holds one entry: a Tier 4 pet (stored tier `3`) trains into Tier 5 with one
Royal Plume (item `59376`). The file has no PABR magic and no trailer. The
alpha bonus of a Tier 5 pet is in [`petleaderbuff.bss`](petleaderbuff_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------- | ----- | ------- | --------- |
| 1      | 1927 and later | `petupgrade.bss` | 26    | 1 Entry | 22        |

| Layout | File             | Known        | Unknown     |
| ------ | ---------------- | ------------ | ----------- |
| 1      | `petupgrade.bss` | 22 B (84.6%) | 4 B (15.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `87dd52deeabd`  |
| 3482   | Layout 1 | `87dd52deeabd`  |
| 3474   | Layout 1 | `87dd52deeabd`  |
| 3473   | Layout 1 | `87dd52deeabd`  |
| 3464   | Layout 1 | `87dd52deeabd`  |
| 3458   | Layout 1 | `87dd52deeabd`  |
| 3454   | Layout 1 | `87dd52deeabd`  |
| 3444   | Layout 1 | `87dd52deeabd`  |
| 3435   | Layout 1 | `87dd52deeabd`  |
| 3426   | Layout 1 | `87dd52deeabd`  |
| 3418   | Layout 1 | `87dd52deeabd`  |
| 3412   | Layout 1 | `87dd52deeabd`  |
| 3402   | Layout 1 | `87dd52deeabd`  |
| 3396   | Layout 1 | `87dd52deeabd`  |
| 3387   | Layout 1 | `87dd52deeabd`  |
| 3381   | Layout 1 | `87dd52deeabd`  |
| 3373   | Layout 1 | `87dd52deeabd`  |
| 3364   | Layout 1 | `87dd52deeabd`  |
| 3356   | Layout 1 | `87dd52deeabd`  |
| 3349   | Layout 1 | `87dd52deeabd`  |
| 3342   | Layout 1 | `87dd52deeabd`  |
| 3335   | Layout 1 | `87dd52deeabd`  |
| 3326   | Layout 1 | `87dd52deeabd`  |
| 3321   | Layout 1 | `87dd52deeabd`  |
| 3314   | Layout 1 | `87dd52deeabd`  |
| 3303   | Layout 1 | `87dd52deeabd`  |
| 3302   | Layout 1 | `87dd52deeabd`  |
| 3293   | Layout 1 | `87dd52deeabd`  |
| 3283   | Layout 1 | `87dd52deeabd`  |
| 3275   | Layout 1 | `87dd52deeabd`  |
| 3267   | Layout 1 | `87dd52deeabd`  |
| 3258   | Layout 1 | `87dd52deeabd`  |
| 3251   | Layout 1 | `87dd52deeabd`  |
| 3242   | Layout 1 | `87dd52deeabd`  |
| 3235   | Layout 1 | `87dd52deeabd`  |
| 3229   | Layout 1 | `87dd52deeabd`  |
| 3212   | Layout 1 | `87dd52deeabd`  |
| 3203   | Layout 1 | `87dd52deeabd`  |
| 3193   | Layout 1 | `87dd52deeabd`  |
| 3186   | Layout 1 | `87dd52deeabd`  |
| 3177   | Layout 1 | `87dd52deeabd`  |
| 3169   | Layout 1 | `87dd52deeabd`  |
| 3158   | Layout 1 | `87dd52deeabd`  |
| 3151   | Layout 1 | `87dd52deeabd`  |
| 3144   | Layout 1 | `87dd52deeabd`  |
| 3133   | Layout 1 | `87dd52deeabd`  |
| 3125   | Layout 1 | `87dd52deeabd`  |
| 3118   | Layout 1 | `87dd52deeabd`  |
| 3111   | Layout 1 | `87dd52deeabd`  |
| 3103   | Layout 1 | `87dd52deeabd`  |
| 3095   | Layout 1 | `87dd52deeabd`  |
| 3086   | Layout 1 | `87dd52deeabd`  |
| 3072   | Layout 1 | `87dd52deeabd`  |
| 3062   | Layout 1 | `87dd52deeabd`  |
| 3052   | Layout 1 | `87dd52deeabd`  |
| 3045   | Layout 1 | `87dd52deeabd`  |
| 3037   | Layout 1 | `87dd52deeabd`  |
| 3030   | Layout 1 | `87dd52deeabd`  |
| 3021   | Layout 1 | `87dd52deeabd`  |
| 3012   | Layout 1 | `87dd52deeabd`  |
| 3002   | Layout 1 | `87dd52deeabd`  |
| 2995   | Layout 1 | `87dd52deeabd`  |
| 2987   | Layout 1 | `87dd52deeabd`  |
| 2978   | Layout 1 | `87dd52deeabd`  |
| 2970   | Layout 1 | `87dd52deeabd`  |
| 2959   | Layout 1 | `87dd52deeabd`  |
| 2951   | Layout 1 | `87dd52deeabd`  |
| 2942   | Layout 1 | `87dd52deeabd`  |
| 2935   | Layout 1 | `87dd52deeabd`  |
| 2932   | Layout 1 | `87dd52deeabd`  |
| 2923   | Layout 1 | `87dd52deeabd`  |
| 2919   | Layout 1 | `87dd52deeabd`  |
| 2907   | Layout 1 | `87dd52deeabd`  |
| 2900   | Layout 1 | `87dd52deeabd`  |
| 2891   | Layout 1 | `87dd52deeabd`  |
| 2882   | Layout 1 | `87dd52deeabd`  |
| 2872   | Layout 1 | `87dd52deeabd`  |
| 2863   | Layout 1 | `87dd52deeabd`  |
| 2855   | Layout 1 | `87dd52deeabd`  |
| 2849   | Layout 1 | `87dd52deeabd`  |
| 2844   | Layout 1 | `87dd52deeabd`  |
| 2834   | Layout 1 | `87dd52deeabd`  |
| 2825   | Layout 1 | `87dd52deeabd`  |
| 2819   | Layout 1 | `87dd52deeabd`  |
| 2811   | Layout 1 | `87dd52deeabd`  |
| 2803   | Layout 1 | `87dd52deeabd`  |
| 2794   | Layout 1 | `87dd52deeabd`  |
| 2783   | Layout 1 | `87dd52deeabd`  |
| 2774   | Layout 1 | `87dd52deeabd`  |
| 2765   | Layout 1 | `87dd52deeabd`  |
| 2756   | Layout 1 | `87dd52deeabd`  |
| 2750   | Layout 1 | `87dd52deeabd`  |
| 2743   | Layout 1 | `87dd52deeabd`  |
| 2736   | Layout 1 | `87dd52deeabd`  |
| 2726   | Layout 1 | `87dd52deeabd`  |
| 2717   | Layout 1 | `87dd52deeabd`  |
| 2709   | Layout 1 | `87dd52deeabd`  |
| 2703   | Layout 1 | `87dd52deeabd`  |
| 2695   | Layout 1 | `87dd52deeabd`  |
| 2684   | Layout 1 | `87dd52deeabd`  |
| 2672   | Layout 1 | `87dd52deeabd`  |
| 2665   | Layout 1 | `87dd52deeabd`  |
| 2657   | Layout 1 | `87dd52deeabd`  |
| 2649   | Layout 1 | `87dd52deeabd`  |
| 2644   | Layout 1 | `87dd52deeabd`  |
| 2637   | Layout 1 | `87dd52deeabd`  |
| 2629   | Layout 1 | `87dd52deeabd`  |
| 2619   | Layout 1 | `87dd52deeabd`  |
| 2612   | Layout 1 | `87dd52deeabd`  |
| 2606   | Layout 1 | `87dd52deeabd`  |
| 2602   | Layout 1 | `87dd52deeabd`  |
| 2601   | Layout 1 | `87dd52deeabd`  |
| 2592   | Layout 1 | `87dd52deeabd`  |
| 2583   | Layout 1 | `87dd52deeabd`  |
| 2575   | Layout 1 | `87dd52deeabd`  |
| 2567   | Layout 1 | `87dd52deeabd`  |
| 2560   | Layout 1 | `87dd52deeabd`  |
| 2553   | Layout 1 | `87dd52deeabd`  |
| 2545   | Layout 1 | `87dd52deeabd`  |
| 2538   | Layout 1 | `87dd52deeabd`  |
| 2529   | Layout 1 | `87dd52deeabd`  |
| 2519   | Layout 1 | `87dd52deeabd`  |
| 2513   | Layout 1 | `87dd52deeabd`  |
| 2510   | Layout 1 | `87dd52deeabd`  |
| 2507   | Layout 1 | `87dd52deeabd`  |
| 2503   | Layout 1 | `87dd52deeabd`  |
| 2498   | Layout 1 | `87dd52deeabd`  |
| 2492   | Layout 1 | `87dd52deeabd`  |
| 2487   | Layout 1 | `87dd52deeabd`  |
| 2480   | Layout 1 | `87dd52deeabd`  |
| 2474   | Layout 1 | `87dd52deeabd`  |
| 2468   | Layout 1 | `87dd52deeabd`  |
| 2460   | Layout 1 | `87dd52deeabd`  |
| 2453   | Layout 1 | `87dd52deeabd`  |
| 2444   | Layout 1 | `87dd52deeabd`  |
| 2438   | Layout 1 | `87dd52deeabd`  |
| 2434   | Layout 1 | `87dd52deeabd`  |
| 2429   | Layout 1 | `87dd52deeabd`  |
| 2421   | Layout 1 | `87dd52deeabd`  |
| 2414   | Layout 1 | `87dd52deeabd`  |
| 2407   | Layout 1 | `87dd52deeabd`  |
| 2401   | Layout 1 | `87dd52deeabd`  |
| 2397   | Layout 1 | `87dd52deeabd`  |
| 2393   | Layout 1 | `87dd52deeabd`  |
| 2384   | Layout 1 | `87dd52deeabd`  |
| 2378   | Layout 1 | `87dd52deeabd`  |
| 2372   | Layout 1 | `87dd52deeabd`  |
| 2358   | Layout 1 | `87dd52deeabd`  |
| 2352   | Layout 1 | `87dd52deeabd`  |
| 2347   | Layout 1 | `87dd52deeabd`  |
| 2343   | Layout 1 | `87dd52deeabd`  |
| 2335   | Layout 1 | `87dd52deeabd`  |
| 2327   | Layout 1 | `87dd52deeabd`  |
| 2324   | Layout 1 | `87dd52deeabd`  |
| 2319   | Layout 1 | `87dd52deeabd`  |
| 2313   | Layout 1 | `87dd52deeabd`  |
| 2308   | Layout 1 | `87dd52deeabd`  |
| 2302   | Layout 1 | `87dd52deeabd`  |
| 2295   | Layout 1 | `87dd52deeabd`  |
| 2290   | Layout 1 | `87dd52deeabd`  |
| 2284   | Layout 1 | `87dd52deeabd`  |
| 2276   | Layout 1 | `87dd52deeabd`  |
| 2269   | Layout 1 | `87dd52deeabd`  |
| 2259   | Layout 1 | `87dd52deeabd`  |
| 2250   | Layout 1 | `87dd52deeabd`  |
| 2243   | Layout 1 | `87dd52deeabd`  |
| 2235   | Layout 1 | `87dd52deeabd`  |
| 2229   | Layout 1 | `87dd52deeabd`  |
| 2224   | Layout 1 | `87dd52deeabd`  |
| 2218   | Layout 1 | `87dd52deeabd`  |
| 2215   | Layout 1 | `87dd52deeabd`  |
| 2207   | Layout 1 | `87dd52deeabd`  |
| 2203   | Layout 1 | `87dd52deeabd`  |
| 2196   | Layout 1 | `87dd52deeabd`  |
| 2192   | Layout 1 | `87dd52deeabd`  |
| 2189   | Layout 1 | `87dd52deeabd`  |
| 2183   | Layout 1 | `87dd52deeabd`  |
| 2179   | Layout 1 | `87dd52deeabd`  |
| 2171   | Layout 1 | `87dd52deeabd`  |
| 2163   | Layout 1 | `87dd52deeabd`  |
| 2156   | Layout 1 | `87dd52deeabd`  |
| 2151   | Layout 1 | `87dd52deeabd`  |
| 2147   | Layout 1 | `87dd52deeabd`  |
| 2142   | Layout 1 | `87dd52deeabd`  |
| 2138   | Layout 1 | `87dd52deeabd`  |
| 2134   | Layout 1 | `87dd52deeabd`  |
| 2130   | Layout 1 | `87dd52deeabd`  |
| 2122   | Layout 1 | `87dd52deeabd`  |
| 2107   | Layout 1 | `87dd52deeabd`  |
| 2098   | Layout 1 | `87dd52deeabd`  |
| 2089   | Layout 1 | `87dd52deeabd`  |
| 2081   | Layout 1 | `87dd52deeabd`  |
| 2073   | Layout 1 | `87dd52deeabd`  |
| 2067   | Layout 1 | `87dd52deeabd`  |
| 2063   | Layout 1 | `87dd52deeabd`  |
| 2059   | Layout 1 | `87dd52deeabd`  |
| 2052   | Layout 1 | `87dd52deeabd`  |
| 2044   | Layout 1 | `87dd52deeabd`  |
| 2039   | Layout 1 | `87dd52deeabd`  |
| 2032   | Layout 1 | `87dd52deeabd`  |
| 2025   | Layout 1 | `87dd52deeabd`  |
| 2011   | Layout 1 | `87dd52deeabd`  |
| 2005   | Layout 1 | `87dd52deeabd`  |
| 2000   | Layout 1 | `87dd52deeabd`  |
| 1996   | Layout 1 | `87dd52deeabd`  |
| 1991   | Layout 1 | `87dd52deeabd`  |
| 1985   | Layout 1 | `87dd52deeabd`  |
| 1980   | Layout 1 | `87dd52deeabd`  |
| 1969   | Layout 1 | `87dd52deeabd`  |
| 1964   | Layout 1 | `87dd52deeabd`  |
| 1958   | Layout 1 | `87dd52deeabd`  |
| 1950   | Layout 1 | `87dd52deeabd`  |
| 1945   | Layout 1 | `87dd52deeabd`  |
| 1937   | Layout 1 | `87dd52deeabd`  |
| 1933   | Layout 1 | `87dd52deeabd`  |
| 1927   | Layout 1 | `87dd52deeabd`  |
| 1921   | No file  | `87dd52deeabd`  |
| 1914   | No file  | `87dd52deeabd`  |
| 1908   | No file  | `87dd52deeabd`  |
| 1897   | No file  | `87dd52deeabd`  |
| 1892   | No file  | `87dd52deeabd`  |
| 1886   | No file  | `87dd52deeabd`  |
| 1881   | No file  | `87dd52deeabd`  |
| 1871   | No file  | `87dd52deeabd`  |
| 1866   | No file  | `87dd52deeabd`  |
| 1862   | No file  | `87dd52deeabd`  |
| 1854   | No file  | `87dd52deeabd`  |
| 1846   | No file  | `87dd52deeabd`  |
| 1838   | No file  | `87dd52deeabd`  |
| 1832   | No file  | `87dd52deeabd`  |
| 1826   | No file  | `87dd52deeabd`  |
| 1822   | No file  | `87dd52deeabd`  |
| 1818   | No file  | `87dd52deeabd`  |
| 1804   | No file  | `87dd52deeabd`  |
| 1794   | No file  | `87dd52deeabd`  |
| 1790   | No file  | `87dd52deeabd`  |
| 1784   | No file  | `87dd52deeabd`  |
| 1774   | No file  | `87dd52deeabd`  |
| 1771   | No file  | `87dd52deeabd`  |
| 1762   | No file  | `87dd52deeabd`  |
| 1759   | No file  | `87dd52deeabd`  |
| 1754   | No file  | `87dd52deeabd`  |
| 1749   | No file  | `87dd52deeabd`  |
| 1743   | No file  | `87dd52deeabd`  |
| 1737   | No file  | `87dd52deeabd`  |
| 1731   | No file  | `87dd52deeabd`  |
| 1725   | No file  | `87dd52deeabd`  |
| 1717   | No file  | `87dd52deeabd`  |
| 1710   | No file  | `87dd52deeabd`  |
| 1704   | No file  | `87dd52deeabd`  |
| 1698   | No file  | `87dd52deeabd`  |
| 1690   | No file  | `87dd52deeabd`  |
| 1685   | No file  | `87dd52deeabd`  |
| 1680   | No file  | `87dd52deeabd`  |
| 1674   | No file  | `87dd52deeabd`  |
| 1668   | No file  | `87dd52deeabd`  |
| 1659   | No file  | `87dd52deeabd`  |
| 1649   | No file  | `87dd52deeabd`  |
| 1642   | No file  | `87dd52deeabd`  |
| 1636   | No file  | `87dd52deeabd`  |
| 1628   | No file  | `87dd52deeabd`  |
| 1622   | No file  | `87dd52deeabd`  |
| 1614   | No file  | `87dd52deeabd`  |
| 1608   | No file  | `87dd52deeabd`  |
| 1602   | No file  | `87dd52deeabd`  |
| 1598   | No file  | `87dd52deeabd`  |
| 1594   | No file  | `87dd52deeabd`  |
| 1590   | No file  | `87dd52deeabd`  |
| 1587   | No file  | `87dd52deeabd`  |
| 1584   | No file  | `87dd52deeabd`  |
| 1579   | No file  | `87dd52deeabd`  |
| 1572   | No file  | `87dd52deeabd`  |
| 1565   | No file  | `87dd52deeabd`  |
| 1559   | No file  | `87dd52deeabd`  |
| 1554   | No file  | `87dd52deeabd`  |
| 1547   | No file  | `87dd52deeabd`  |
| 1537   | No file  | `87dd52deeabd`  |
| 1529   | No file  | `87dd52deeabd`  |
| 1524   | No file  | `87dd52deeabd`  |
| 1519   | No file  | `87dd52deeabd`  |
| 1509   | No file  | `87dd52deeabd`  |
| 1506   | No file  | `87dd52deeabd`  |
| 1504   | No file  | `87dd52deeabd`  |
| 1500   | No file  | `87dd52deeabd`  |
| 1493   | No file  | `87dd52deeabd`  |
| 1489   | No file  | `87dd52deeabd`  |
| 1485   | No file  | `87dd52deeabd`  |
| 1481   | No file  | `87dd52deeabd`  |
| 1474   | No file  | `87dd52deeabd`  |
| 1466   | No file  | `87dd52deeabd`  |
| 1462   | No file  | `87dd52deeabd`  |
| 1459   | No file  | `87dd52deeabd`  |
| 1453   | No file  | `87dd52deeabd`  |
| 1450   | No file  | `87dd52deeabd`  |
| 1445   | No file  | `87dd52deeabd`  |
| 1439   | No file  | `87dd52deeabd`  |
| 1433   | No file  | `87dd52deeabd`  |
| 1430   | No file  | `87dd52deeabd`  |
| 1426   | No file  | `87dd52deeabd`  |
| 1421   | No file  | `87dd52deeabd`  |
| 1417   | No file  | `87dd52deeabd`  |
| 1416   | No file  | `87dd52deeabd`  |
| 1409   | No file  | `87dd52deeabd`  |
| 1405   | No file  | `87dd52deeabd`  |
| 1401   | No file  | `87dd52deeabd`  |
| 1396   | No file  | `87dd52deeabd`  |
| 1391   | No file  | `87dd52deeabd`  |
| 1390   | No file  | `87dd52deeabd`  |
| 1386   | No file  | `87dd52deeabd`  |
| 1381   | No file  | `87dd52deeabd`  |
| 1379   | No file  | `87dd52deeabd`  |
| 1372   | No file  | `87dd52deeabd`  |
| 1366   | No file  | `87dd52deeabd`  |
| 1364   | No file  | `87dd52deeabd`  |
| 1363   | No file  | `87dd52deeabd`  |
| 1360   | No file  | `87dd52deeabd`  |
| 1358   | No file  | `87dd52deeabd`  |
| 1355   | No file  | `87dd52deeabd`  |
| 1351   | No file  | `87dd52deeabd`  |
| 1348   | No file  | `87dd52deeabd`  |
| 1346   | No file  | `87dd52deeabd`  |
| 1341   | No file  | `87dd52deeabd`  |
| 1340   | No file  | `87dd52deeabd`  |
| 1338   | No file  | `87dd52deeabd`  |
| 1335   | No file  | `87dd52deeabd`  |
| 1333   | No file  | `87dd52deeabd`  |
| 1329   | No file  | `87dd52deeabd`  |
| 1327   | No file  | `87dd52deeabd`  |
| 1324   | No file  | `87dd52deeabd`  |
| 1321   | No file  | `87dd52deeabd`  |
| 1319   | No file  | `87dd52deeabd`  |
| 1318   | No file  | `87dd52deeabd`  |
| 1316   | No file  | `87dd52deeabd`  |
| 1313   | No file  | `87dd52deeabd`  |
| 1311   | No file  | `87dd52deeabd`  |
| 1309   | No file  | `87dd52deeabd`  |
| 1304   | No file  | `87dd52deeabd`  |
| 1292   | No file  | `87dd52deeabd`  |
| 1286   | No file  | `87dd52deeabd`  |
| 1280   | No file  | `87dd52deeabd`  |
| 1276   | No file  | `87dd52deeabd`  |
| 1267   | No file  | `87dd52deeabd`  |
| 1261   | No file  | `87dd52deeabd`  |
| 1256   | No file  | `87dd52deeabd`  |
| 1250   | No file  | `87dd52deeabd`  |
| 1246   | No file  | `87dd52deeabd`  |
| 1239   | No file  | `87dd52deeabd`  |
| 1230   | No file  | `87dd52deeabd`  |
| 1226   | No file  | `87dd52deeabd`  |
| 1220   | No file  | `87dd52deeabd`  |
| 1217   | No file  | `87dd52deeabd`  |
| 1211   | No file  | `87dd52deeabd`  |
| 1210   | No file  | `87dd52deeabd`  |
| 1208   | No file  | `87dd52deeabd`  |
| 1203   | No file  | `87dd52deeabd`  |
| 1197   | No file  | `87dd52deeabd`  |
| 1194   | No file  | `87dd52deeabd`  |
| 1192   | No file  | `87dd52deeabd`  |
| 1187   | No file  | `87dd52deeabd`  |
| 1183   | No file  | `87dd52deeabd`  |
| 1177   | No file  | `87dd52deeabd`  |
| 1173   | No file  | `87dd52deeabd`  |
| 1167   | No file  | `87dd52deeabd`  |
| 1164   | No file  | `87dd52deeabd`  |
| 1156   | No file  | `87dd52deeabd`  |
| 1149   | No file  | `87dd52deeabd`  |
| 1144   | No file  | `87dd52deeabd`  |
| 1137   | No file  | `87dd52deeabd`  |
| 1132   | No file  | `87dd52deeabd`  |
| 1127   | No file  | `87dd52deeabd`  |
| 1122   | No file  | `87dd52deeabd`  |
| 1118   | No file  | `87dd52deeabd`  |
| 1114   | No file  | `87dd52deeabd`  |
| 1109   | No file  | `87dd52deeabd`  |
| 1102   | No file  | `87dd52deeabd`  |
| 1096   | No file  | `87dd52deeabd`  |
| 1088   | No file  | `87dd52deeabd`  |
| 1081   | No file  | `87dd52deeabd`  |
| 1076   | No file  | `87dd52deeabd`  |
| 1069   | No file  | `87dd52deeabd`  |
| 1064   | No file  | `87dd52deeabd`  |
| 1058   | No file  | `87dd52deeabd`  |
| 1051   | No file  | `87dd52deeabd`  |
| 1044   | No file  | `87dd52deeabd`  |
| 1036   | No file  | `87dd52deeabd`  |
| 1026   | No file  | `87dd52deeabd`  |
| 1016   | No file  | `87dd52deeabd`  |
| 1009   | No file  | `87dd52deeabd`  |
| 1005   | No file  | `87dd52deeabd`  |
| 1000   | No file  | `87dd52deeabd`  |
| 998    | No file  | `87dd52deeabd`  |
| 990    | No file  | `87dd52deeabd`  |
| 979    | No file  | `87dd52deeabd`  |
| 972    | No file  | `87dd52deeabd`  |
| 963    | No file  | `87dd52deeabd`  |
| 955    | No file  | `87dd52deeabd`  |
| 946    | No file  | `87dd52deeabd`  |
| 938    | No file  | `87dd52deeabd`  |
| 927    | No file  | `87dd52deeabd`  |
| 911    | No file  | `87dd52deeabd`  |
| 904    | No file  | `87dd52deeabd`  |
| 899    | No file  | `87dd52deeabd`  |
| 894    | No file  | `87dd52deeabd`  |
| 885    | No file  | `87dd52deeabd`  |
| 879    | No file  | `87dd52deeabd`  |
| 872    | No file  | `87dd52deeabd`  |
| 864    | No file  | `87dd52deeabd`  |
| 855    | No file  | `87dd52deeabd`  |
| 853    | No file  | `87dd52deeabd`  |
| 845    | No file  | `87dd52deeabd`  |
| 837    | No file  | `87dd52deeabd`  |
| 829    | No file  | `87dd52deeabd`  |
| 822    | No file  | `87dd52deeabd`  |
| 814    | No file  | `87dd52deeabd`  |
| 805    | No file  | `87dd52deeabd`  |
| 794    | No file  | `87dd52deeabd`  |
| 787    | No file  | `87dd52deeabd`  |
| 780    | No file  | `87dd52deeabd`  |
| 771    | No file  | `87dd52deeabd`  |
| 760    | No file  | `87dd52deeabd`  |
| 748    | No file  | `87dd52deeabd`  |
| 741    | No file  | `87dd52deeabd`  |
| 736    | No file  | `87dd52deeabd`  |
| 731    | No file  | `87dd52deeabd`  |
| 723    | No file  | `87dd52deeabd`  |
| 711    | No file  | `87dd52deeabd`  |
| 707    | No file  | `87dd52deeabd`  |
| 697    | No file  | `87dd52deeabd`  |
| 689    | No file  | `87dd52deeabd`  |
| 683    | No file  | `87dd52deeabd`  |
| 678    | No file  | `87dd52deeabd`  |
| 670    | No file  | `87dd52deeabd`  |
| 661    | No file  | `87dd52deeabd`  |
| 656    | No file  | `87dd52deeabd`  |
| 652    | No file  | `87dd52deeabd`  |
| 643    | No file  | `87dd52deeabd`  |
| 637    | No file  | `87dd52deeabd`  |
| 630    | No file  | `87dd52deeabd`  |
| 627    | No file  | `87dd52deeabd`  |
| 621    | No file  | `87dd52deeabd`  |
| 617    | No file  | `87dd52deeabd`  |
| 615    | No file  | `87dd52deeabd`  |
| 606    | No file  | `87dd52deeabd`  |
| 599    | No file  | `87dd52deeabd`  |
| 592    | No file  | `87dd52deeabd`  |
| 586    | No file  | `87dd52deeabd`  |
| 577    | No file  | `87dd52deeabd`  |
| 569    | No file  | `87dd52deeabd`  |
| 561    | No file  | `87dd52deeabd`  |
| 554    | No file  | `87dd52deeabd`  |
| 542    | No file  | `87dd52deeabd`  |
| 532    | No file  | `87dd52deeabd`  |
| 531    | No file  | `87dd52deeabd`  |
| 526    | No file  | `87dd52deeabd`  |
| 521    | No file  | `87dd52deeabd`  |
| 517    | No file  | `87dd52deeabd`  |
| 510    | No file  | `87dd52deeabd`  |
| 508    | No file  | `87dd52deeabd`  |
| 504    | No file  | `87dd52deeabd`  |
| 497    | No file  | `87dd52deeabd`  |
| 491    | No file  | `87dd52deeabd`  |
| 485    | No file  | `87dd52deeabd`  |
| 478    | No file  | `87dd52deeabd`  |
| 472    | No file  | `87dd52deeabd`  |
| 466    | No file  | `87dd52deeabd`  |
| 457    | No file  | `87dd52deeabd`  |
| 452    | No file  | `87dd52deeabd`  |
| 449    | No file  | `87dd52deeabd`  |
| 435    | No file  | `87dd52deeabd`  |

<!-- versions:end -->

## Companion Files

None. The handler names the item with its LOC type 0 name from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field   | Notes                                 |
| ------- | ------------ | ------- | ------------------------------------- |
| `+0x00` | u32          | count   | Number of entries; `1` on client 3474 |
| `+0x04` | Entry[count] | entries | See Entry                             |

### Entry (22 bytes)

| Offset  | Type | Field        | Notes                                                                 |
| ------- | ---- | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u8   | pet_tier     | Map key: the tier the pet trains from, as `tier` of [`pet.dbss`](pet_dbss.md) stores it, from 0; `3` is Tier 4 |
| `+0x01` | u32  | item_id      | Training item; `59376` Royal Plume on client 3474                     |
| `+0x05` | u64  | item_count   | Items one training uses; `1` on client 3474                           |
| `+0x0d` | u32  | success_rate | Training success rate; `1000000` (100%) on the only entry            |
| `+0x11` | u32  | unknown_11   | `1000000` on the only entry, see Open Questions                       |
| `+0x15` | u8   | pet_tier_dup | Equals `pet_tier` on the only entry                                   |

## Field Names

No reference source has the table: the file is in the client 2107 archive
but not in the client 1784 one, and a private server's `DataSheets.bexcel`
on client 1784 has no sheet with `Pet` and `Upgrade` in its name. The names
come from the client Lua of client 3474 (`panel_dialog_petleader_all_1.luac`
and `_2.luac`, the Tier 5 Pet Training window):

- `pet_tier` and `item_id`: the window asks for the training item with
  `ToClient_getPetUpgradeItem(petStaticStatus:getPetTier())` for the pet in
  the slot, and with `ToClient_getPetUpgradeItem(3)` for the empty slot. It
  turns the training button on only when the inventory holds that item. A
  pet below Tier 4 (`getPetTier() + 1 < 4`) gets
  `LUA_PETCOMPOSE_CANTBETOGETHER_TEXT`, so the key is the stored tier of the
  Tier 4 pet. Its item `59376` is Royal Plume, whose LOC text says "Usage:
  Tier 5 Pet Training".
- `item_count`: the window trains with
  `ToClient_requestPetUpgradeByItem(name, petNo, eInventory, itemSlotNo, 1)`,
  one item. Garmoth's "BDO Basics - Pets" guide (section "5. Tier 5 Pet
  Enhancement") says the training is done at a Pet Trainer NPC and consumes
  a Royal Plume. The official Black Desert wiki page "Tier 5 Pet
  Training/Alpha Appointment" says "To train a Tier 5 pet, you will need a
  "Royal Plume"" and that the menu trains "Tier 4 pets to Tier 5", which is
  `pet_tier` `3` and item `59376`.

## Notes

- Raw bytes on client 3474: `01 00 00 00 03 F0 E7 00 00 01 00 00 00 00 00
  00 00 40 42 0F 00 40 42 0F 00 03`. Clients 2107, 2519, 3002 and 3251 ship
  the same 26 bytes.
- `global_define_cpp_enum.luac` lists `Contents_PetUpgrade`, and the window
  calls `ToClient_UpdateOpenUICondition(__eCheckOpenUIType_5TierPetUpgrade)`
  when it opens.
- The window shows the trained pet from
  `ToClient_getPetUpgradeSimulationResult(characterKey)`, and the alpha
  bonus of the new tier from `ToClient_getPetLeaderBuff`
  ([`petleaderbuff.bss`](petleaderbuff_bss.md)). Which pet a pet trains
  into, and its talent as the alpha, is in
  [`petupgraderesult.bss`](petupgraderesult_bss.md).
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`, with the item's icon and name next to its ID.

## Open Questions

### Second Rate Value

`success_rate` and `unknown_11` are both `1000000`, 100% on the client's
1,000,000 = 100% rate scale. A private server's `Fairy_Upgrade` sheet on
client 1784 has the columns `Tier`, `NeedItem`, `ItemCount` and `Rate`, the
order of the first four fields here, with `Rate` `1000000` on every row,
and in game my Tier 5 Pet Training always succeeds; so the field after the
count is the success rate. No Lua reads a rate from the training window,
and the official Black Desert wiki page "Tier 5 Pet Training/Alpha
Appointment" names no success rate. What `unknown_11` holds is unknown.
