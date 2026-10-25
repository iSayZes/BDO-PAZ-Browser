# `journalquestoffset.dbss` Format

## Purpose

Index file for `journalquest.dbss`. Maps each `(journal_key, book_key)` pair to a `(byte_offset, byte_size)` location within the main file. Field names follow [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor), re-verified against our files.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes | Records                              | Row bytes |
| ------ | -------------- | ------------------------- | ----- | ------------------------------------ | --------- |
| 1      | 1286 and later | `journalquestoffset.dbss` | 1,512 | 117 Book Index Entry, 13 Group Block | 12        |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `journalquestoffset.dbss` | 1,512 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6ab2c87fa763`  |
| 3482   | Layout 1 | `6ab2c87fa763`  |
| 3474   | Layout 1 | `6ab2c87fa763`  |
| 3473   | Layout 1 | `6ab2c87fa763`  |
| 3464   | Layout 1 | `6ab2c87fa763`  |
| 3458   | Layout 1 | `6ab2c87fa763`  |
| 3454   | Layout 1 | `6ab2c87fa763`  |
| 3444   | Layout 1 | `6ab2c87fa763`  |
| 3435   | Layout 1 | `6ab2c87fa763`  |
| 3426   | Layout 1 | `6ab2c87fa763`  |
| 3418   | Layout 1 | `6ab2c87fa763`  |
| 3412   | Layout 1 | `6ab2c87fa763`  |
| 3402   | Layout 1 | `6ab2c87fa763`  |
| 3396   | Layout 1 | `6ab2c87fa763`  |
| 3387   | Layout 1 | `6ab2c87fa763`  |
| 3381   | Layout 1 | `6ab2c87fa763`  |
| 3373   | Layout 1 | `6ab2c87fa763`  |
| 3364   | Layout 1 | `6ab2c87fa763`  |
| 3356   | Layout 1 | `6ab2c87fa763`  |
| 3349   | Layout 1 | `6ab2c87fa763`  |
| 3342   | Layout 1 | `6ab2c87fa763`  |
| 3335   | Layout 1 | `6ab2c87fa763`  |
| 3326   | Layout 1 | `6ab2c87fa763`  |
| 3321   | Layout 1 | `6ab2c87fa763`  |
| 3314   | Layout 1 | `6ab2c87fa763`  |
| 3303   | Layout 1 | `6ab2c87fa763`  |
| 3302   | Layout 1 | `6ab2c87fa763`  |
| 3293   | Layout 1 | `6ab2c87fa763`  |
| 3283   | Layout 1 | `6ab2c87fa763`  |
| 3275   | Layout 1 | `6ab2c87fa763`  |
| 3267   | Layout 1 | `6ab2c87fa763`  |
| 3258   | Layout 1 | `6ab2c87fa763`  |
| 3251   | Layout 1 | `6ab2c87fa763`  |
| 3242   | Layout 1 | `6ab2c87fa763`  |
| 3235   | Layout 1 | `6ab2c87fa763`  |
| 3229   | Layout 1 | `6ab2c87fa763`  |
| 3212   | Layout 1 | `6ab2c87fa763`  |
| 3203   | Layout 1 | `6ab2c87fa763`  |
| 3193   | Layout 1 | `6ab2c87fa763`  |
| 3186   | Layout 1 | `6ab2c87fa763`  |
| 3177   | Layout 1 | `6ab2c87fa763`  |
| 3169   | Layout 1 | `6ab2c87fa763`  |
| 3158   | Layout 1 | `6ab2c87fa763`  |
| 3151   | Layout 1 | `6ab2c87fa763`  |
| 3144   | Layout 1 | `6ab2c87fa763`  |
| 3133   | Layout 1 | `6ab2c87fa763`  |
| 3125   | Layout 1 | `6ab2c87fa763`  |
| 3118   | Layout 1 | `6ab2c87fa763`  |
| 3111   | Layout 1 | `6ab2c87fa763`  |
| 3103   | Layout 1 | `6ab2c87fa763`  |
| 3095   | Layout 1 | `6ab2c87fa763`  |
| 3086   | Layout 1 | `6ab2c87fa763`  |
| 3072   | Layout 1 | `6ab2c87fa763`  |
| 3062   | Layout 1 | `6ab2c87fa763`  |
| 3052   | Layout 1 | `6ab2c87fa763`  |
| 3045   | Layout 1 | `6ab2c87fa763`  |
| 3037   | Layout 1 | `6ab2c87fa763`  |
| 3030   | Layout 1 | `6ab2c87fa763`  |
| 3021   | Layout 1 | `6ab2c87fa763`  |
| 3012   | Layout 1 | `6ab2c87fa763`  |
| 3002   | Layout 1 | `6ab2c87fa763`  |
| 2995   | Layout 1 | `6ab2c87fa763`  |
| 2987   | Layout 1 | `6ab2c87fa763`  |
| 2978   | Layout 1 | `6ab2c87fa763`  |
| 2970   | Layout 1 | `6ab2c87fa763`  |
| 2959   | Layout 1 | `6ab2c87fa763`  |
| 2951   | Layout 1 | `6ab2c87fa763`  |
| 2942   | Layout 1 | `6ab2c87fa763`  |
| 2935   | Layout 1 | `6ab2c87fa763`  |
| 2932   | Layout 1 | `6ab2c87fa763`  |
| 2923   | Layout 1 | `6ab2c87fa763`  |
| 2919   | Layout 1 | `6ab2c87fa763`  |
| 2907   | Layout 1 | `6ab2c87fa763`  |
| 2900   | Layout 1 | `6ab2c87fa763`  |
| 2891   | Layout 1 | `6ab2c87fa763`  |
| 2882   | Layout 1 | `6ab2c87fa763`  |
| 2872   | Layout 1 | `6ab2c87fa763`  |
| 2863   | Layout 1 | `6ab2c87fa763`  |
| 2855   | Layout 1 | `6ab2c87fa763`  |
| 2849   | Layout 1 | `6ab2c87fa763`  |
| 2844   | Layout 1 | `6ab2c87fa763`  |
| 2834   | Layout 1 | `6ab2c87fa763`  |
| 2825   | Layout 1 | `6ab2c87fa763`  |
| 2819   | Layout 1 | `6ab2c87fa763`  |
| 2811   | Layout 1 | `6ab2c87fa763`  |
| 2803   | Layout 1 | `6ab2c87fa763`  |
| 2794   | Layout 1 | `6ab2c87fa763`  |
| 2783   | Layout 1 | `6ab2c87fa763`  |
| 2774   | Layout 1 | `6ab2c87fa763`  |
| 2765   | Layout 1 | `6ab2c87fa763`  |
| 2756   | Layout 1 | `6ab2c87fa763`  |
| 2750   | Layout 1 | `6ab2c87fa763`  |
| 2743   | Layout 1 | `6ab2c87fa763`  |
| 2736   | Layout 1 | `6ab2c87fa763`  |
| 2726   | Layout 1 | `6ab2c87fa763`  |
| 2717   | Layout 1 | `6ab2c87fa763`  |
| 2709   | Layout 1 | `6ab2c87fa763`  |
| 2703   | Layout 1 | `6ab2c87fa763`  |
| 2695   | Layout 1 | `6ab2c87fa763`  |
| 2684   | Layout 1 | `6ab2c87fa763`  |
| 2672   | Layout 1 | `6ab2c87fa763`  |
| 2665   | Layout 1 | `6ab2c87fa763`  |
| 2657   | Layout 1 | `6ab2c87fa763`  |
| 2649   | Layout 1 | `6ab2c87fa763`  |
| 2644   | Layout 1 | `6ab2c87fa763`  |
| 2637   | Layout 1 | `6ab2c87fa763`  |
| 2629   | Layout 1 | `6ab2c87fa763`  |
| 2619   | Layout 1 | `6ab2c87fa763`  |
| 2612   | Layout 1 | `6ab2c87fa763`  |
| 2606   | Layout 1 | `6ab2c87fa763`  |
| 2602   | Layout 1 | `6ab2c87fa763`  |
| 2601   | Layout 1 | `6ab2c87fa763`  |
| 2592   | Layout 1 | `6ab2c87fa763`  |
| 2583   | Layout 1 | `6ab2c87fa763`  |
| 2575   | Layout 1 | `6ab2c87fa763`  |
| 2567   | Layout 1 | `6ab2c87fa763`  |
| 2560   | Layout 1 | `6ab2c87fa763`  |
| 2553   | Layout 1 | `6ab2c87fa763`  |
| 2545   | Layout 1 | `6ab2c87fa763`  |
| 2538   | Layout 1 | `6ab2c87fa763`  |
| 2529   | Layout 1 | `6ab2c87fa763`  |
| 2519   | Layout 1 | `6ab2c87fa763`  |
| 2513   | Layout 1 | `6ab2c87fa763`  |
| 2510   | Layout 1 | `6ab2c87fa763`  |
| 2507   | Layout 1 | `6ab2c87fa763`  |
| 2503   | Layout 1 | `6ab2c87fa763`  |
| 2498   | Layout 1 | `6ab2c87fa763`  |
| 2492   | Layout 1 | `6ab2c87fa763`  |
| 2487   | Layout 1 | `6ab2c87fa763`  |
| 2480   | Layout 1 | `6ab2c87fa763`  |
| 2474   | Layout 1 | `6ab2c87fa763`  |
| 2468   | Layout 1 | `6ab2c87fa763`  |
| 2460   | Layout 1 | `6ab2c87fa763`  |
| 2453   | Layout 1 | `6ab2c87fa763`  |
| 2444   | Layout 1 | `6ab2c87fa763`  |
| 2438   | Layout 1 | `6ab2c87fa763`  |
| 2434   | Layout 1 | `6ab2c87fa763`  |
| 2429   | Layout 1 | `6ab2c87fa763`  |
| 2421   | Layout 1 | `6ab2c87fa763`  |
| 2414   | Layout 1 | `6ab2c87fa763`  |
| 2407   | Layout 1 | `6ab2c87fa763`  |
| 2401   | Layout 1 | `6ab2c87fa763`  |
| 2397   | Layout 1 | `6ab2c87fa763`  |
| 2393   | Layout 1 | `6ab2c87fa763`  |
| 2384   | Layout 1 | `6ab2c87fa763`  |
| 2378   | Layout 1 | `6ab2c87fa763`  |
| 2372   | Layout 1 | `6ab2c87fa763`  |
| 2358   | Layout 1 | `6ab2c87fa763`  |
| 2352   | Layout 1 | `6ab2c87fa763`  |
| 2347   | Layout 1 | `6ab2c87fa763`  |
| 2343   | Layout 1 | `6ab2c87fa763`  |
| 2335   | Layout 1 | `6ab2c87fa763`  |
| 2327   | Layout 1 | `6ab2c87fa763`  |
| 2324   | Layout 1 | `6ab2c87fa763`  |
| 2319   | Layout 1 | `6ab2c87fa763`  |
| 2313   | Layout 1 | `6ab2c87fa763`  |
| 2308   | Layout 1 | `6ab2c87fa763`  |
| 2302   | Layout 1 | `6ab2c87fa763`  |
| 2295   | Layout 1 | `6ab2c87fa763`  |
| 2290   | Layout 1 | `6ab2c87fa763`  |
| 2284   | Layout 1 | `6ab2c87fa763`  |
| 2276   | Layout 1 | `6ab2c87fa763`  |
| 2269   | Layout 1 | `6ab2c87fa763`  |
| 2259   | Layout 1 | `6ab2c87fa763`  |
| 2250   | Layout 1 | `6ab2c87fa763`  |
| 2243   | Layout 1 | `6ab2c87fa763`  |
| 2235   | Layout 1 | `6ab2c87fa763`  |
| 2229   | Layout 1 | `6ab2c87fa763`  |
| 2224   | Layout 1 | `6ab2c87fa763`  |
| 2218   | Layout 1 | `6ab2c87fa763`  |
| 2215   | Layout 1 | `6ab2c87fa763`  |
| 2207   | Layout 1 | `6ab2c87fa763`  |
| 2203   | Layout 1 | `6ab2c87fa763`  |
| 2196   | Layout 1 | `6ab2c87fa763`  |
| 2192   | Layout 1 | `6ab2c87fa763`  |
| 2189   | Layout 1 | `6ab2c87fa763`  |
| 2183   | Layout 1 | `6ab2c87fa763`  |
| 2179   | Layout 1 | `6ab2c87fa763`  |
| 2171   | Layout 1 | `6ab2c87fa763`  |
| 2163   | Layout 1 | `6ab2c87fa763`  |
| 2156   | Layout 1 | `6ab2c87fa763`  |
| 2151   | Layout 1 | `6ab2c87fa763`  |
| 2147   | Layout 1 | `6ab2c87fa763`  |
| 2142   | Layout 1 | `6ab2c87fa763`  |
| 2138   | Layout 1 | `6ab2c87fa763`  |
| 2134   | Layout 1 | `6ab2c87fa763`  |
| 2130   | Layout 1 | `6ab2c87fa763`  |
| 2122   | Layout 1 | `6ab2c87fa763`  |
| 2107   | Layout 1 | `6ab2c87fa763`  |
| 2098   | Layout 1 | `6ab2c87fa763`  |
| 2089   | Layout 1 | `6ab2c87fa763`  |
| 2081   | Layout 1 | `6ab2c87fa763`  |
| 2073   | Layout 1 | `6ab2c87fa763`  |
| 2067   | Layout 1 | `6ab2c87fa763`  |
| 2063   | Layout 1 | `6ab2c87fa763`  |
| 2059   | Layout 1 | `6ab2c87fa763`  |
| 2052   | Layout 1 | `6ab2c87fa763`  |
| 2044   | Layout 1 | `6ab2c87fa763`  |
| 2039   | Layout 1 | `6ab2c87fa763`  |
| 2032   | Layout 1 | `6ab2c87fa763`  |
| 2025   | Layout 1 | `6ab2c87fa763`  |
| 2011   | Layout 1 | `6ab2c87fa763`  |
| 2005   | Layout 1 | `6ab2c87fa763`  |
| 2000   | Layout 1 | `6ab2c87fa763`  |
| 1996   | Layout 1 | `6ab2c87fa763`  |
| 1991   | Layout 1 | `6ab2c87fa763`  |
| 1985   | Layout 1 | `6ab2c87fa763`  |
| 1980   | Layout 1 | `6ab2c87fa763`  |
| 1969   | Layout 1 | `6ab2c87fa763`  |
| 1964   | Layout 1 | `6ab2c87fa763`  |
| 1958   | Layout 1 | `6ab2c87fa763`  |
| 1950   | Layout 1 | `6ab2c87fa763`  |
| 1945   | Layout 1 | `6ab2c87fa763`  |
| 1937   | Layout 1 | `6ab2c87fa763`  |
| 1933   | Layout 1 | `6ab2c87fa763`  |
| 1927   | Layout 1 | `6ab2c87fa763`  |
| 1921   | Layout 1 | `6ab2c87fa763`  |
| 1914   | Layout 1 | `6ab2c87fa763`  |
| 1908   | Layout 1 | `6ab2c87fa763`  |
| 1897   | Layout 1 | `6ab2c87fa763`  |
| 1892   | Layout 1 | `6ab2c87fa763`  |
| 1886   | Layout 1 | `6ab2c87fa763`  |
| 1881   | Layout 1 | `6ab2c87fa763`  |
| 1871   | Layout 1 | `6ab2c87fa763`  |
| 1866   | Layout 1 | `6ab2c87fa763`  |
| 1862   | Layout 1 | `6ab2c87fa763`  |
| 1854   | Layout 1 | `6ab2c87fa763`  |
| 1846   | Layout 1 | `6ab2c87fa763`  |
| 1838   | Layout 1 | `6ab2c87fa763`  |
| 1832   | Layout 1 | `6ab2c87fa763`  |
| 1826   | Layout 1 | `6ab2c87fa763`  |
| 1822   | Layout 1 | `6ab2c87fa763`  |
| 1818   | Layout 1 | `6ab2c87fa763`  |
| 1804   | Layout 1 | `6ab2c87fa763`  |
| 1794   | Layout 1 | `6ab2c87fa763`  |
| 1790   | Layout 1 | `6ab2c87fa763`  |
| 1784   | Layout 1 | `6ab2c87fa763`  |
| 1774   | Layout 1 | `6ab2c87fa763`  |
| 1771   | Layout 1 | `6ab2c87fa763`  |
| 1762   | Layout 1 | `6ab2c87fa763`  |
| 1759   | Layout 1 | `6ab2c87fa763`  |
| 1754   | Layout 1 | `6ab2c87fa763`  |
| 1749   | Layout 1 | `6ab2c87fa763`  |
| 1743   | Layout 1 | `6ab2c87fa763`  |
| 1737   | Layout 1 | `6ab2c87fa763`  |
| 1731   | Layout 1 | `6ab2c87fa763`  |
| 1725   | Layout 1 | `6ab2c87fa763`  |
| 1717   | Layout 1 | `6ab2c87fa763`  |
| 1710   | Layout 1 | `6ab2c87fa763`  |
| 1704   | Layout 1 | `6ab2c87fa763`  |
| 1698   | Layout 1 | `6ab2c87fa763`  |
| 1690   | Layout 1 | `6ab2c87fa763`  |
| 1685   | Layout 1 | `6ab2c87fa763`  |
| 1680   | Layout 1 | `6ab2c87fa763`  |
| 1674   | Layout 1 | `6ab2c87fa763`  |
| 1668   | Layout 1 | `6ab2c87fa763`  |
| 1659   | Layout 1 | `6ab2c87fa763`  |
| 1649   | Layout 1 | `6ab2c87fa763`  |
| 1642   | Layout 1 | `6ab2c87fa763`  |
| 1636   | Layout 1 | `6ab2c87fa763`  |
| 1628   | Layout 1 | `6ab2c87fa763`  |
| 1622   | Layout 1 | `6ab2c87fa763`  |
| 1614   | Layout 1 | `6ab2c87fa763`  |
| 1608   | Layout 1 | `6ab2c87fa763`  |
| 1602   | Layout 1 | `6ab2c87fa763`  |
| 1598   | Layout 1 | `6ab2c87fa763`  |
| 1594   | Layout 1 | `6ab2c87fa763`  |
| 1590   | Layout 1 | `6ab2c87fa763`  |
| 1587   | Layout 1 | `6ab2c87fa763`  |
| 1584   | Layout 1 | `6ab2c87fa763`  |
| 1579   | Layout 1 | `6ab2c87fa763`  |
| 1572   | Layout 1 | `6ab2c87fa763`  |
| 1565   | Layout 1 | `6ab2c87fa763`  |
| 1559   | Layout 1 | `6ab2c87fa763`  |
| 1554   | Layout 1 | `6ab2c87fa763`  |
| 1547   | Layout 1 | `6ab2c87fa763`  |
| 1537   | Layout 1 | `6ab2c87fa763`  |
| 1529   | Layout 1 | `6ab2c87fa763`  |
| 1524   | Layout 1 | `6ab2c87fa763`  |
| 1519   | Layout 1 | `6ab2c87fa763`  |
| 1509   | Layout 1 | `6ab2c87fa763`  |
| 1506   | Layout 1 | `6ab2c87fa763`  |
| 1504   | Layout 1 | `6ab2c87fa763`  |
| 1500   | Layout 1 | `6ab2c87fa763`  |
| 1493   | Layout 1 | `6ab2c87fa763`  |
| 1489   | Layout 1 | `6ab2c87fa763`  |
| 1485   | Layout 1 | `6ab2c87fa763`  |
| 1481   | Layout 1 | `6ab2c87fa763`  |
| 1474   | Layout 1 | `6ab2c87fa763`  |
| 1466   | Layout 1 | `6ab2c87fa763`  |
| 1462   | Layout 1 | `6ab2c87fa763`  |
| 1459   | Layout 1 | `6ab2c87fa763`  |
| 1453   | Layout 1 | `6ab2c87fa763`  |
| 1450   | Layout 1 | `6ab2c87fa763`  |
| 1445   | Layout 1 | `6ab2c87fa763`  |
| 1439   | Layout 1 | `6ab2c87fa763`  |
| 1433   | Layout 1 | `6ab2c87fa763`  |
| 1430   | Layout 1 | `6ab2c87fa763`  |
| 1426   | Layout 1 | `6ab2c87fa763`  |
| 1421   | Layout 1 | `6ab2c87fa763`  |
| 1417   | Layout 1 | `6ab2c87fa763`  |
| 1416   | Layout 1 | `6ab2c87fa763`  |
| 1409   | Layout 1 | `6ab2c87fa763`  |
| 1405   | Layout 1 | `6ab2c87fa763`  |
| 1401   | Layout 1 | `6ab2c87fa763`  |
| 1396   | Layout 1 | `6ab2c87fa763`  |
| 1391   | Layout 1 | `6ab2c87fa763`  |
| 1390   | Layout 1 | `6ab2c87fa763`  |
| 1386   | Layout 1 | `6ab2c87fa763`  |
| 1381   | Layout 1 | `6ab2c87fa763`  |
| 1379   | Layout 1 | `6ab2c87fa763`  |
| 1372   | Layout 1 | `6ab2c87fa763`  |
| 1366   | Layout 1 | `6ab2c87fa763`  |
| 1364   | Layout 1 | `6ab2c87fa763`  |
| 1363   | Layout 1 | `6ab2c87fa763`  |
| 1360   | Layout 1 | `6ab2c87fa763`  |
| 1358   | Layout 1 | `6ab2c87fa763`  |
| 1355   | Layout 1 | `6ab2c87fa763`  |
| 1351   | Layout 1 | `6ab2c87fa763`  |
| 1348   | Layout 1 | `6ab2c87fa763`  |
| 1346   | Layout 1 | `6ab2c87fa763`  |
| 1341   | Layout 1 | `6ab2c87fa763`  |
| 1340   | Layout 1 | `6ab2c87fa763`  |
| 1338   | Layout 1 | `6ab2c87fa763`  |
| 1335   | Layout 1 | `6ab2c87fa763`  |
| 1333   | Layout 1 | `6ab2c87fa763`  |
| 1329   | Layout 1 | `6ab2c87fa763`  |
| 1327   | Layout 1 | `6ab2c87fa763`  |
| 1324   | Layout 1 | `6ab2c87fa763`  |
| 1321   | Layout 1 | `6ab2c87fa763`  |
| 1319   | Layout 1 | `6ab2c87fa763`  |
| 1318   | Layout 1 | `6ab2c87fa763`  |
| 1316   | Layout 1 | `6ab2c87fa763`  |
| 1313   | Layout 1 | `6ab2c87fa763`  |
| 1311   | Layout 1 | `6ab2c87fa763`  |
| 1309   | Layout 1 | `6ab2c87fa763`  |
| 1304   | Layout 1 | `6ab2c87fa763`  |
| 1292   | Layout 1 | `6ab2c87fa763`  |
| 1286   | Layout 1 | `6ab2c87fa763`  |
| 1280   | No file  | `6ab2c87fa763`  |
| 1276   | No file  | `6ab2c87fa763`  |
| 1267   | No file  | `6ab2c87fa763`  |
| 1261   | No file  | `6ab2c87fa763`  |
| 1256   | No file  | `6ab2c87fa763`  |
| 1250   | No file  | `6ab2c87fa763`  |
| 1246   | No file  | `6ab2c87fa763`  |
| 1239   | No file  | `6ab2c87fa763`  |
| 1230   | No file  | `6ab2c87fa763`  |
| 1226   | No file  | `6ab2c87fa763`  |
| 1220   | No file  | `6ab2c87fa763`  |
| 1217   | No file  | `6ab2c87fa763`  |
| 1211   | No file  | `6ab2c87fa763`  |
| 1210   | No file  | `6ab2c87fa763`  |
| 1208   | No file  | `6ab2c87fa763`  |
| 1203   | No file  | `6ab2c87fa763`  |
| 1197   | No file  | `6ab2c87fa763`  |
| 1194   | No file  | `6ab2c87fa763`  |
| 1192   | No file  | `6ab2c87fa763`  |
| 1187   | No file  | `6ab2c87fa763`  |
| 1183   | No file  | `6ab2c87fa763`  |
| 1177   | No file  | `6ab2c87fa763`  |
| 1173   | No file  | `6ab2c87fa763`  |
| 1167   | No file  | `6ab2c87fa763`  |
| 1164   | No file  | `6ab2c87fa763`  |
| 1156   | No file  | `6ab2c87fa763`  |
| 1149   | No file  | `6ab2c87fa763`  |
| 1144   | No file  | `6ab2c87fa763`  |
| 1137   | No file  | `6ab2c87fa763`  |
| 1132   | No file  | `6ab2c87fa763`  |
| 1127   | No file  | `6ab2c87fa763`  |
| 1122   | No file  | `6ab2c87fa763`  |
| 1118   | No file  | `6ab2c87fa763`  |
| 1114   | No file  | `6ab2c87fa763`  |
| 1109   | No file  | `6ab2c87fa763`  |
| 1102   | No file  | `6ab2c87fa763`  |
| 1096   | No file  | `6ab2c87fa763`  |
| 1088   | No file  | `6ab2c87fa763`  |
| 1081   | No file  | `6ab2c87fa763`  |
| 1076   | No file  | `6ab2c87fa763`  |
| 1069   | No file  | `6ab2c87fa763`  |
| 1064   | No file  | `6ab2c87fa763`  |
| 1058   | No file  | `6ab2c87fa763`  |
| 1051   | No file  | `6ab2c87fa763`  |
| 1044   | No file  | `6ab2c87fa763`  |
| 1036   | No file  | `6ab2c87fa763`  |
| 1026   | No file  | `6ab2c87fa763`  |
| 1016   | No file  | `6ab2c87fa763`  |
| 1009   | No file  | `6ab2c87fa763`  |
| 1005   | No file  | `6ab2c87fa763`  |
| 1000   | No file  | `6ab2c87fa763`  |
| 998    | No file  | `6ab2c87fa763`  |
| 990    | No file  | `6ab2c87fa763`  |
| 979    | No file  | `6ab2c87fa763`  |
| 972    | No file  | `6ab2c87fa763`  |
| 963    | No file  | `6ab2c87fa763`  |
| 955    | No file  | `6ab2c87fa763`  |
| 946    | No file  | `6ab2c87fa763`  |
| 938    | No file  | `6ab2c87fa763`  |
| 927    | No file  | `6ab2c87fa763`  |
| 911    | No file  | `6ab2c87fa763`  |
| 904    | No file  | `6ab2c87fa763`  |
| 899    | No file  | `6ab2c87fa763`  |
| 894    | No file  | `6ab2c87fa763`  |
| 885    | No file  | `6ab2c87fa763`  |
| 879    | No file  | `6ab2c87fa763`  |
| 872    | No file  | `6ab2c87fa763`  |
| 864    | No file  | `6ab2c87fa763`  |
| 855    | No file  | `6ab2c87fa763`  |
| 853    | No file  | `6ab2c87fa763`  |
| 845    | No file  | `6ab2c87fa763`  |
| 837    | No file  | `6ab2c87fa763`  |
| 829    | No file  | `6ab2c87fa763`  |
| 822    | No file  | `6ab2c87fa763`  |
| 814    | No file  | `6ab2c87fa763`  |
| 805    | No file  | `6ab2c87fa763`  |
| 794    | No file  | `6ab2c87fa763`  |
| 787    | No file  | `6ab2c87fa763`  |
| 780    | No file  | `6ab2c87fa763`  |
| 771    | No file  | `6ab2c87fa763`  |
| 760    | No file  | `6ab2c87fa763`  |
| 748    | No file  | `6ab2c87fa763`  |
| 741    | No file  | `6ab2c87fa763`  |
| 736    | No file  | `6ab2c87fa763`  |
| 731    | No file  | `6ab2c87fa763`  |
| 723    | No file  | `6ab2c87fa763`  |
| 711    | No file  | `6ab2c87fa763`  |
| 707    | No file  | `6ab2c87fa763`  |
| 697    | No file  | `6ab2c87fa763`  |
| 689    | No file  | `6ab2c87fa763`  |
| 683    | No file  | `6ab2c87fa763`  |
| 678    | No file  | `6ab2c87fa763`  |
| 670    | No file  | `6ab2c87fa763`  |
| 661    | No file  | `6ab2c87fa763`  |
| 656    | No file  | `6ab2c87fa763`  |
| 652    | No file  | `6ab2c87fa763`  |
| 643    | No file  | `6ab2c87fa763`  |
| 637    | No file  | `6ab2c87fa763`  |
| 630    | No file  | `6ab2c87fa763`  |
| 627    | No file  | `6ab2c87fa763`  |
| 621    | No file  | `6ab2c87fa763`  |
| 617    | No file  | `6ab2c87fa763`  |
| 615    | No file  | `6ab2c87fa763`  |
| 606    | No file  | `6ab2c87fa763`  |
| 599    | No file  | `6ab2c87fa763`  |
| 592    | No file  | `6ab2c87fa763`  |
| 586    | No file  | `6ab2c87fa763`  |
| 577    | No file  | `6ab2c87fa763`  |
| 569    | No file  | `6ab2c87fa763`  |
| 561    | No file  | `6ab2c87fa763`  |
| 554    | No file  | `6ab2c87fa763`  |
| 542    | No file  | `6ab2c87fa763`  |
| 532    | No file  | `6ab2c87fa763`  |
| 531    | No file  | `6ab2c87fa763`  |
| 526    | No file  | `6ab2c87fa763`  |
| 521    | No file  | `6ab2c87fa763`  |
| 517    | No file  | `6ab2c87fa763`  |
| 510    | No file  | `6ab2c87fa763`  |
| 508    | No file  | `6ab2c87fa763`  |
| 504    | No file  | `6ab2c87fa763`  |
| 497    | No file  | `6ab2c87fa763`  |
| 491    | No file  | `6ab2c87fa763`  |
| 485    | No file  | `6ab2c87fa763`  |
| 478    | No file  | `6ab2c87fa763`  |
| 472    | No file  | `6ab2c87fa763`  |
| 466    | No file  | `6ab2c87fa763`  |
| 457    | No file  | `6ab2c87fa763`  |
| 452    | No file  | `6ab2c87fa763`  |
| 449    | No file  | `6ab2c87fa763`  |
| 435    | No file  | `6ab2c87fa763`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                          |
| --------------------- | -------- | --------------------------------------------- |
| `journalquest.dbss`   | Required | Contains the actual book records              |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                     | Field       | Notes                                   |
| ------- | ------------------------ | ----------- | --------------------------------------- |
| `+0x00` | u32                      | group_count | Number of journal groups; observed `12` |
| `+0x04` | Group Block[group_count] | groups      | See Group Block                         |

Immediately after the header, `group_count` variable-length group blocks follow back to back:

```
for i in range(group_count):
    journal_key = read_u32()
    book_count  = read_u32()
    for j in range(book_count):
        book_key    = read_u32()
        byte_offset = read_u32()
        byte_size   = read_u32()
```

### Group Block (variable: 8 bytes + book entries)

| Offset  | Type                         | Field        | Notes                                                          |
| ------- | ---------------------------- | ------------ | -------------------------------------------------------------- |
| `+0x00` | u32                          | journal_key  | Journal group key (1 to 12; not in numeric order in file)      |
| `+0x04` | u32                          | book_count   | Number of books; equals the `book_count` word in the data file |
| `+0x08` | Book Index Entry[book_count] | books        | See Book Index Entry                                           |

### Book Index Entry (12 bytes)

| Offset  | Type | Field         | Notes                                                   |
| ------- | ---- | ------------- | ------------------------------------------------------- |
| `+0x00` | u32  | book_key      | Book key within the group; usually 1-based and contiguous, but journal 6 uses 1, 2, 10, 7, 8, 11, 12 |
| `+0x04` | u32  | byte_offset   | Absolute byte offset of the record in `journalquest.dbss` |
| `+0x08` | u32  | byte_size     | Exact byte size of the record                           |

## Notes

- File size is `4 + 8 × group_count + 12 × total_books`: `4 + 96 + 1,344 = 1,444` bytes for 12 groups and 112 books. The earlier reading of "120-byte physical chunks" was a coincidence (`1,440 = 12 × 120`); there is no chunking.
- Groups are stored in the order 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 10 (journal 10 last). This is also the physical group order in `journalquest.dbss`.
- `byte_offset` values are absolute offsets into `journalquest.dbss`. Every `byte_size` is exact: each record ends precisely on its `unknown_end` word, and the indexed records plus the 4-byte header and one 4-byte `book_count` per group tile the data file with no gaps (112 of 112 records, current file and fixture).
- Within a group, index order equals physical order except in journal 6, where books 2 and 10 are swapped physically.
- The current file and the older fixture are both `1,444` bytes with the same keys; only offsets and sizes differ.

## Display Order

[bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) states that the book index order is the UI order, independent of file order. It is neither: the journal shelf sorts books by `book_key`. The only journal where the file orders differ is journal 6 ("Event Logs"), which the offset file lists as 1, 2, 10, 7, 8, 11, 12 and the game shows as 1, 2, 7, 8, 10, 11, 12 (checked in game, 2026-09-28; see `journalquest_dbss.md`).
