# `pad00000.meta` Format

## Purpose

`pad00000.meta` sits in the `Paz` folder next to the `PAD*.PAZ` archives. It
lists every archive and every file inside them, with the archive, offset and
sizes of each file and its full path. `read_bdo_meta` in
`PAZ-Parser/paz/bdo_meta_reader.py` reads the header and the archive table;
`read_meta_entries` reads the file table and both name blocks, so a client's
whole file list is known from the `.meta` alone, without its archives.

One layout fits every client checked, 435 (2017-05) to 3482 (2026-10).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File            | Bytes      | Records                              | Row bytes |
| ------ | ------------- | --------------- | ---------- | ------------------------------------ | --------- |
| 1      | 435 and later | `pad00000.meta` | 46,269,472 | 11,256 Archive Row, 872,965 File Row | 28        |

| Layout | File            | Known                 | Unknown    |
| ------ | --------------- | --------------------- | ---------- |
| 1      | `pad00000.meta` | 46,269,472 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `52062dd7e383`  |
| 3482   | Layout 1 | `52062dd7e383`  |
| 3474   | Layout 1 | `52062dd7e383`  |
| 3473   | Layout 1 | `52062dd7e383`  |
| 3464   | Layout 1 | `52062dd7e383`  |
| 3458   | Layout 1 | `52062dd7e383`  |
| 3454   | Layout 1 | `52062dd7e383`  |
| 3444   | Layout 1 | `52062dd7e383`  |
| 3435   | Layout 1 | `52062dd7e383`  |
| 3426   | Layout 1 | `52062dd7e383`  |
| 3418   | Layout 1 | `52062dd7e383`  |
| 3412   | Layout 1 | `52062dd7e383`  |
| 3402   | Layout 1 | `52062dd7e383`  |
| 3396   | Layout 1 | `52062dd7e383`  |
| 3387   | Layout 1 | `52062dd7e383`  |
| 3381   | Layout 1 | `52062dd7e383`  |
| 3373   | Layout 1 | `52062dd7e383`  |
| 3364   | Layout 1 | `52062dd7e383`  |
| 3356   | Layout 1 | `52062dd7e383`  |
| 3349   | Layout 1 | `52062dd7e383`  |
| 3342   | Layout 1 | `52062dd7e383`  |
| 3335   | Layout 1 | `52062dd7e383`  |
| 3326   | Layout 1 | `52062dd7e383`  |
| 3321   | Layout 1 | `52062dd7e383`  |
| 3314   | Layout 1 | `52062dd7e383`  |
| 3303   | Layout 1 | `52062dd7e383`  |
| 3302   | Layout 1 | `52062dd7e383`  |
| 3293   | Layout 1 | `52062dd7e383`  |
| 3283   | Layout 1 | `52062dd7e383`  |
| 3275   | Layout 1 | `52062dd7e383`  |
| 3267   | Layout 1 | `52062dd7e383`  |
| 3258   | Layout 1 | `52062dd7e383`  |
| 3251   | Layout 1 | `52062dd7e383`  |
| 3242   | Layout 1 | `52062dd7e383`  |
| 3235   | Layout 1 | `52062dd7e383`  |
| 3229   | Layout 1 | `52062dd7e383`  |
| 3212   | Layout 1 | `52062dd7e383`  |
| 3203   | Layout 1 | `52062dd7e383`  |
| 3193   | Layout 1 | `52062dd7e383`  |
| 3186   | Layout 1 | `52062dd7e383`  |
| 3177   | Layout 1 | `52062dd7e383`  |
| 3169   | Layout 1 | `52062dd7e383`  |
| 3158   | Layout 1 | `52062dd7e383`  |
| 3151   | Layout 1 | `52062dd7e383`  |
| 3144   | Layout 1 | `52062dd7e383`  |
| 3133   | Layout 1 | `52062dd7e383`  |
| 3125   | Layout 1 | `52062dd7e383`  |
| 3118   | Layout 1 | `52062dd7e383`  |
| 3111   | Layout 1 | `52062dd7e383`  |
| 3103   | Layout 1 | `52062dd7e383`  |
| 3095   | Layout 1 | `52062dd7e383`  |
| 3086   | Layout 1 | `52062dd7e383`  |
| 3072   | Layout 1 | `52062dd7e383`  |
| 3062   | Layout 1 | `52062dd7e383`  |
| 3052   | Layout 1 | `52062dd7e383`  |
| 3045   | Layout 1 | `52062dd7e383`  |
| 3037   | Layout 1 | `52062dd7e383`  |
| 3030   | Layout 1 | `52062dd7e383`  |
| 3021   | Layout 1 | `52062dd7e383`  |
| 3012   | Layout 1 | `52062dd7e383`  |
| 3002   | Layout 1 | `52062dd7e383`  |
| 2995   | Layout 1 | `52062dd7e383`  |
| 2987   | Layout 1 | `52062dd7e383`  |
| 2978   | Layout 1 | `52062dd7e383`  |
| 2970   | Layout 1 | `52062dd7e383`  |
| 2959   | Layout 1 | `52062dd7e383`  |
| 2951   | Layout 1 | `52062dd7e383`  |
| 2942   | Layout 1 | `52062dd7e383`  |
| 2935   | Layout 1 | `52062dd7e383`  |
| 2932   | Layout 1 | `52062dd7e383`  |
| 2923   | Layout 1 | `52062dd7e383`  |
| 2919   | Layout 1 | `52062dd7e383`  |
| 2907   | Layout 1 | `52062dd7e383`  |
| 2900   | Layout 1 | `52062dd7e383`  |
| 2891   | Layout 1 | `52062dd7e383`  |
| 2882   | Layout 1 | `52062dd7e383`  |
| 2872   | Layout 1 | `52062dd7e383`  |
| 2863   | Layout 1 | `52062dd7e383`  |
| 2855   | Layout 1 | `52062dd7e383`  |
| 2849   | Layout 1 | `52062dd7e383`  |
| 2844   | Layout 1 | `52062dd7e383`  |
| 2834   | Layout 1 | `52062dd7e383`  |
| 2825   | Layout 1 | `52062dd7e383`  |
| 2819   | Layout 1 | `52062dd7e383`  |
| 2811   | Layout 1 | `52062dd7e383`  |
| 2803   | Layout 1 | `52062dd7e383`  |
| 2794   | Layout 1 | `52062dd7e383`  |
| 2783   | Layout 1 | `52062dd7e383`  |
| 2774   | Layout 1 | `52062dd7e383`  |
| 2765   | Layout 1 | `52062dd7e383`  |
| 2756   | Layout 1 | `52062dd7e383`  |
| 2750   | Layout 1 | `52062dd7e383`  |
| 2743   | Layout 1 | `52062dd7e383`  |
| 2736   | Layout 1 | `52062dd7e383`  |
| 2726   | Layout 1 | `52062dd7e383`  |
| 2717   | Layout 1 | `52062dd7e383`  |
| 2709   | Layout 1 | `52062dd7e383`  |
| 2703   | Layout 1 | `52062dd7e383`  |
| 2695   | Layout 1 | `52062dd7e383`  |
| 2684   | Layout 1 | `52062dd7e383`  |
| 2672   | Layout 1 | `52062dd7e383`  |
| 2665   | Layout 1 | `52062dd7e383`  |
| 2657   | Layout 1 | `52062dd7e383`  |
| 2649   | Layout 1 | `52062dd7e383`  |
| 2644   | Layout 1 | `52062dd7e383`  |
| 2637   | Layout 1 | `52062dd7e383`  |
| 2629   | Layout 1 | `52062dd7e383`  |
| 2619   | Layout 1 | `52062dd7e383`  |
| 2612   | Layout 1 | `52062dd7e383`  |
| 2606   | Layout 1 | `52062dd7e383`  |
| 2602   | Layout 1 | `52062dd7e383`  |
| 2601   | Layout 1 | `52062dd7e383`  |
| 2592   | Layout 1 | `52062dd7e383`  |
| 2583   | Layout 1 | `52062dd7e383`  |
| 2575   | Layout 1 | `52062dd7e383`  |
| 2567   | Layout 1 | `52062dd7e383`  |
| 2560   | Layout 1 | `52062dd7e383`  |
| 2553   | Layout 1 | `52062dd7e383`  |
| 2545   | Layout 1 | `52062dd7e383`  |
| 2538   | Layout 1 | `52062dd7e383`  |
| 2529   | Layout 1 | `52062dd7e383`  |
| 2519   | Layout 1 | `52062dd7e383`  |
| 2513   | Layout 1 | `52062dd7e383`  |
| 2510   | Layout 1 | `52062dd7e383`  |
| 2507   | Layout 1 | `52062dd7e383`  |
| 2503   | Layout 1 | `52062dd7e383`  |
| 2498   | Layout 1 | `52062dd7e383`  |
| 2492   | Layout 1 | `52062dd7e383`  |
| 2487   | Layout 1 | `52062dd7e383`  |
| 2480   | Layout 1 | `52062dd7e383`  |
| 2474   | Layout 1 | `52062dd7e383`  |
| 2468   | Layout 1 | `52062dd7e383`  |
| 2460   | Layout 1 | `52062dd7e383`  |
| 2453   | Layout 1 | `52062dd7e383`  |
| 2444   | Layout 1 | `52062dd7e383`  |
| 2438   | Layout 1 | `52062dd7e383`  |
| 2434   | Layout 1 | `52062dd7e383`  |
| 2429   | Layout 1 | `52062dd7e383`  |
| 2421   | Layout 1 | `52062dd7e383`  |
| 2414   | Layout 1 | `52062dd7e383`  |
| 2407   | Layout 1 | `52062dd7e383`  |
| 2401   | Layout 1 | `52062dd7e383`  |
| 2397   | Layout 1 | `52062dd7e383`  |
| 2393   | Layout 1 | `52062dd7e383`  |
| 2384   | Layout 1 | `52062dd7e383`  |
| 2378   | Layout 1 | `52062dd7e383`  |
| 2372   | Layout 1 | `52062dd7e383`  |
| 2358   | Layout 1 | `52062dd7e383`  |
| 2352   | Layout 1 | `52062dd7e383`  |
| 2347   | Layout 1 | `52062dd7e383`  |
| 2343   | Layout 1 | `52062dd7e383`  |
| 2335   | Layout 1 | `52062dd7e383`  |
| 2327   | Layout 1 | `52062dd7e383`  |
| 2324   | Layout 1 | `52062dd7e383`  |
| 2319   | Layout 1 | `52062dd7e383`  |
| 2313   | Layout 1 | `52062dd7e383`  |
| 2308   | Layout 1 | `52062dd7e383`  |
| 2302   | Layout 1 | `52062dd7e383`  |
| 2295   | Layout 1 | `52062dd7e383`  |
| 2290   | Layout 1 | `52062dd7e383`  |
| 2284   | Layout 1 | `52062dd7e383`  |
| 2276   | Layout 1 | `52062dd7e383`  |
| 2269   | Layout 1 | `52062dd7e383`  |
| 2259   | Layout 1 | `52062dd7e383`  |
| 2250   | Layout 1 | `52062dd7e383`  |
| 2243   | Layout 1 | `52062dd7e383`  |
| 2235   | Layout 1 | `52062dd7e383`  |
| 2229   | Layout 1 | `52062dd7e383`  |
| 2224   | Layout 1 | `52062dd7e383`  |
| 2218   | Layout 1 | `52062dd7e383`  |
| 2215   | Layout 1 | `52062dd7e383`  |
| 2207   | Layout 1 | `52062dd7e383`  |
| 2203   | Layout 1 | `52062dd7e383`  |
| 2196   | Layout 1 | `52062dd7e383`  |
| 2192   | Layout 1 | `52062dd7e383`  |
| 2189   | Layout 1 | `52062dd7e383`  |
| 2183   | Layout 1 | `52062dd7e383`  |
| 2179   | Layout 1 | `52062dd7e383`  |
| 2171   | Layout 1 | `52062dd7e383`  |
| 2163   | Layout 1 | `52062dd7e383`  |
| 2156   | Layout 1 | `52062dd7e383`  |
| 2151   | Layout 1 | `52062dd7e383`  |
| 2147   | Layout 1 | `52062dd7e383`  |
| 2142   | Layout 1 | `52062dd7e383`  |
| 2138   | Layout 1 | `52062dd7e383`  |
| 2134   | Layout 1 | `52062dd7e383`  |
| 2130   | Layout 1 | `52062dd7e383`  |
| 2122   | Layout 1 | `52062dd7e383`  |
| 2107   | Layout 1 | `52062dd7e383`  |
| 2098   | Layout 1 | `52062dd7e383`  |
| 2089   | Layout 1 | `52062dd7e383`  |
| 2081   | Layout 1 | `52062dd7e383`  |
| 2073   | Layout 1 | `52062dd7e383`  |
| 2067   | Layout 1 | `52062dd7e383`  |
| 2063   | Layout 1 | `52062dd7e383`  |
| 2059   | Layout 1 | `52062dd7e383`  |
| 2052   | Layout 1 | `52062dd7e383`  |
| 2044   | Layout 1 | `52062dd7e383`  |
| 2039   | Layout 1 | `52062dd7e383`  |
| 2032   | Layout 1 | `52062dd7e383`  |
| 2025   | Layout 1 | `52062dd7e383`  |
| 2011   | Layout 1 | `52062dd7e383`  |
| 2005   | Layout 1 | `52062dd7e383`  |
| 2000   | Layout 1 | `52062dd7e383`  |
| 1996   | Layout 1 | `52062dd7e383`  |
| 1991   | Layout 1 | `52062dd7e383`  |
| 1985   | Layout 1 | `52062dd7e383`  |
| 1980   | Layout 1 | `52062dd7e383`  |
| 1969   | Layout 1 | `52062dd7e383`  |
| 1964   | Layout 1 | `52062dd7e383`  |
| 1958   | Layout 1 | `52062dd7e383`  |
| 1950   | Layout 1 | `52062dd7e383`  |
| 1945   | Layout 1 | `52062dd7e383`  |
| 1937   | Layout 1 | `52062dd7e383`  |
| 1933   | Layout 1 | `52062dd7e383`  |
| 1927   | Layout 1 | `52062dd7e383`  |
| 1921   | Layout 1 | `52062dd7e383`  |
| 1914   | Layout 1 | `52062dd7e383`  |
| 1908   | Layout 1 | `52062dd7e383`  |
| 1897   | Layout 1 | `52062dd7e383`  |
| 1892   | Layout 1 | `52062dd7e383`  |
| 1886   | Layout 1 | `52062dd7e383`  |
| 1881   | Layout 1 | `52062dd7e383`  |
| 1871   | Layout 1 | `52062dd7e383`  |
| 1866   | Layout 1 | `52062dd7e383`  |
| 1862   | Layout 1 | `52062dd7e383`  |
| 1854   | Layout 1 | `52062dd7e383`  |
| 1846   | Layout 1 | `52062dd7e383`  |
| 1838   | Layout 1 | `52062dd7e383`  |
| 1832   | Layout 1 | `52062dd7e383`  |
| 1826   | Layout 1 | `52062dd7e383`  |
| 1822   | Layout 1 | `52062dd7e383`  |
| 1818   | Layout 1 | `52062dd7e383`  |
| 1804   | Layout 1 | `52062dd7e383`  |
| 1794   | Layout 1 | `52062dd7e383`  |
| 1790   | Layout 1 | `52062dd7e383`  |
| 1784   | Layout 1 | `52062dd7e383`  |
| 1774   | Layout 1 | `52062dd7e383`  |
| 1771   | Layout 1 | `52062dd7e383`  |
| 1762   | Layout 1 | `52062dd7e383`  |
| 1759   | Layout 1 | `52062dd7e383`  |
| 1754   | Layout 1 | `52062dd7e383`  |
| 1749   | Layout 1 | `52062dd7e383`  |
| 1743   | Layout 1 | `52062dd7e383`  |
| 1737   | Layout 1 | `52062dd7e383`  |
| 1731   | Layout 1 | `52062dd7e383`  |
| 1725   | Layout 1 | `52062dd7e383`  |
| 1717   | Layout 1 | `52062dd7e383`  |
| 1710   | Layout 1 | `52062dd7e383`  |
| 1704   | Layout 1 | `52062dd7e383`  |
| 1698   | Layout 1 | `52062dd7e383`  |
| 1690   | Layout 1 | `52062dd7e383`  |
| 1685   | Layout 1 | `52062dd7e383`  |
| 1680   | Layout 1 | `52062dd7e383`  |
| 1674   | Layout 1 | `52062dd7e383`  |
| 1668   | Layout 1 | `52062dd7e383`  |
| 1659   | Layout 1 | `52062dd7e383`  |
| 1649   | Layout 1 | `52062dd7e383`  |
| 1642   | Layout 1 | `52062dd7e383`  |
| 1636   | Layout 1 | `52062dd7e383`  |
| 1628   | Layout 1 | `52062dd7e383`  |
| 1622   | Layout 1 | `52062dd7e383`  |
| 1614   | Layout 1 | `52062dd7e383`  |
| 1608   | Layout 1 | `52062dd7e383`  |
| 1602   | Layout 1 | `52062dd7e383`  |
| 1598   | Layout 1 | `52062dd7e383`  |
| 1594   | Layout 1 | `52062dd7e383`  |
| 1590   | Layout 1 | `52062dd7e383`  |
| 1587   | Layout 1 | `52062dd7e383`  |
| 1584   | Layout 1 | `52062dd7e383`  |
| 1579   | Layout 1 | `52062dd7e383`  |
| 1572   | Layout 1 | `52062dd7e383`  |
| 1565   | Layout 1 | `52062dd7e383`  |
| 1559   | Layout 1 | `52062dd7e383`  |
| 1554   | Layout 1 | `52062dd7e383`  |
| 1547   | Layout 1 | `52062dd7e383`  |
| 1537   | Layout 1 | `52062dd7e383`  |
| 1529   | Layout 1 | `52062dd7e383`  |
| 1524   | Layout 1 | `52062dd7e383`  |
| 1519   | Layout 1 | `52062dd7e383`  |
| 1509   | Layout 1 | `52062dd7e383`  |
| 1506   | Layout 1 | `52062dd7e383`  |
| 1504   | Layout 1 | `52062dd7e383`  |
| 1500   | Layout 1 | `52062dd7e383`  |
| 1493   | Layout 1 | `52062dd7e383`  |
| 1489   | Layout 1 | `52062dd7e383`  |
| 1485   | Layout 1 | `52062dd7e383`  |
| 1481   | Layout 1 | `52062dd7e383`  |
| 1474   | Layout 1 | `52062dd7e383`  |
| 1466   | Layout 1 | `52062dd7e383`  |
| 1462   | Layout 1 | `52062dd7e383`  |
| 1459   | Layout 1 | `52062dd7e383`  |
| 1453   | Layout 1 | `52062dd7e383`  |
| 1450   | Layout 1 | `52062dd7e383`  |
| 1445   | Layout 1 | `52062dd7e383`  |
| 1439   | Layout 1 | `52062dd7e383`  |
| 1433   | Layout 1 | `52062dd7e383`  |
| 1430   | Layout 1 | `52062dd7e383`  |
| 1426   | Layout 1 | `52062dd7e383`  |
| 1421   | Layout 1 | `52062dd7e383`  |
| 1417   | Layout 1 | `52062dd7e383`  |
| 1416   | Layout 1 | `52062dd7e383`  |
| 1409   | Layout 1 | `52062dd7e383`  |
| 1405   | Layout 1 | `52062dd7e383`  |
| 1401   | Layout 1 | `52062dd7e383`  |
| 1396   | Layout 1 | `52062dd7e383`  |
| 1391   | Layout 1 | `52062dd7e383`  |
| 1390   | Layout 1 | `52062dd7e383`  |
| 1386   | Layout 1 | `52062dd7e383`  |
| 1381   | Layout 1 | `52062dd7e383`  |
| 1379   | Layout 1 | `52062dd7e383`  |
| 1372   | Layout 1 | `52062dd7e383`  |
| 1366   | Layout 1 | `52062dd7e383`  |
| 1364   | Layout 1 | `52062dd7e383`  |
| 1363   | Layout 1 | `52062dd7e383`  |
| 1360   | Layout 1 | `52062dd7e383`  |
| 1358   | Layout 1 | `52062dd7e383`  |
| 1355   | Layout 1 | `52062dd7e383`  |
| 1351   | Layout 1 | `52062dd7e383`  |
| 1348   | Layout 1 | `52062dd7e383`  |
| 1346   | Layout 1 | `52062dd7e383`  |
| 1341   | Layout 1 | `52062dd7e383`  |
| 1340   | Layout 1 | `52062dd7e383`  |
| 1338   | Layout 1 | `52062dd7e383`  |
| 1335   | Layout 1 | `52062dd7e383`  |
| 1333   | Layout 1 | `52062dd7e383`  |
| 1329   | Layout 1 | `52062dd7e383`  |
| 1327   | Layout 1 | `52062dd7e383`  |
| 1324   | Layout 1 | `52062dd7e383`  |
| 1321   | Layout 1 | `52062dd7e383`  |
| 1319   | Layout 1 | `52062dd7e383`  |
| 1318   | Layout 1 | `52062dd7e383`  |
| 1316   | Layout 1 | `52062dd7e383`  |
| 1313   | Layout 1 | `52062dd7e383`  |
| 1311   | Layout 1 | `52062dd7e383`  |
| 1309   | Layout 1 | `52062dd7e383`  |
| 1304   | Layout 1 | `52062dd7e383`  |
| 1292   | Layout 1 | `52062dd7e383`  |
| 1286   | Layout 1 | `52062dd7e383`  |
| 1280   | Layout 1 | `52062dd7e383`  |
| 1276   | Layout 1 | `52062dd7e383`  |
| 1267   | Layout 1 | `52062dd7e383`  |
| 1261   | Layout 1 | `52062dd7e383`  |
| 1256   | Layout 1 | `52062dd7e383`  |
| 1250   | Layout 1 | `52062dd7e383`  |
| 1246   | Layout 1 | `52062dd7e383`  |
| 1239   | Layout 1 | `52062dd7e383`  |
| 1230   | Layout 1 | `52062dd7e383`  |
| 1226   | Layout 1 | `52062dd7e383`  |
| 1220   | Layout 1 | `52062dd7e383`  |
| 1217   | Layout 1 | `52062dd7e383`  |
| 1211   | Layout 1 | `52062dd7e383`  |
| 1210   | Layout 1 | `52062dd7e383`  |
| 1208   | Layout 1 | `52062dd7e383`  |
| 1203   | Layout 1 | `52062dd7e383`  |
| 1197   | Layout 1 | `52062dd7e383`  |
| 1194   | Layout 1 | `52062dd7e383`  |
| 1192   | Layout 1 | `52062dd7e383`  |
| 1187   | Layout 1 | `52062dd7e383`  |
| 1183   | Layout 1 | `52062dd7e383`  |
| 1177   | Layout 1 | `52062dd7e383`  |
| 1173   | Layout 1 | `52062dd7e383`  |
| 1167   | Layout 1 | `52062dd7e383`  |
| 1164   | Layout 1 | `52062dd7e383`  |
| 1156   | Layout 1 | `52062dd7e383`  |
| 1149   | Layout 1 | `52062dd7e383`  |
| 1144   | Layout 1 | `52062dd7e383`  |
| 1137   | Layout 1 | `52062dd7e383`  |
| 1132   | Layout 1 | `52062dd7e383`  |
| 1127   | Layout 1 | `52062dd7e383`  |
| 1122   | Layout 1 | `52062dd7e383`  |
| 1118   | Layout 1 | `52062dd7e383`  |
| 1114   | Layout 1 | `52062dd7e383`  |
| 1109   | Layout 1 | `52062dd7e383`  |
| 1102   | Layout 1 | `52062dd7e383`  |
| 1096   | Layout 1 | `52062dd7e383`  |
| 1088   | Layout 1 | `52062dd7e383`  |
| 1081   | Layout 1 | `52062dd7e383`  |
| 1076   | Layout 1 | `52062dd7e383`  |
| 1069   | Layout 1 | `52062dd7e383`  |
| 1064   | Layout 1 | `52062dd7e383`  |
| 1058   | Layout 1 | `52062dd7e383`  |
| 1051   | Layout 1 | `52062dd7e383`  |
| 1044   | Layout 1 | `52062dd7e383`  |
| 1036   | Layout 1 | `52062dd7e383`  |
| 1026   | Layout 1 | `52062dd7e383`  |
| 1016   | Layout 1 | `52062dd7e383`  |
| 1009   | Layout 1 | `52062dd7e383`  |
| 1005   | Layout 1 | `52062dd7e383`  |
| 1000   | Layout 1 | `52062dd7e383`  |
| 998    | Layout 1 | `52062dd7e383`  |
| 990    | Layout 1 | `52062dd7e383`  |
| 979    | Layout 1 | `52062dd7e383`  |
| 972    | Layout 1 | `52062dd7e383`  |
| 963    | Layout 1 | `52062dd7e383`  |
| 955    | Layout 1 | `52062dd7e383`  |
| 946    | Layout 1 | `52062dd7e383`  |
| 938    | Layout 1 | `52062dd7e383`  |
| 927    | Layout 1 | `52062dd7e383`  |
| 911    | Layout 1 | `52062dd7e383`  |
| 904    | Layout 1 | `52062dd7e383`  |
| 899    | Layout 1 | `52062dd7e383`  |
| 894    | Layout 1 | `52062dd7e383`  |
| 885    | Layout 1 | `52062dd7e383`  |
| 879    | Layout 1 | `52062dd7e383`  |
| 872    | Layout 1 | `52062dd7e383`  |
| 864    | Layout 1 | `52062dd7e383`  |
| 855    | Layout 1 | `52062dd7e383`  |
| 853    | Layout 1 | `52062dd7e383`  |
| 845    | Layout 1 | `52062dd7e383`  |
| 837    | Layout 1 | `52062dd7e383`  |
| 829    | Layout 1 | `52062dd7e383`  |
| 822    | Layout 1 | `52062dd7e383`  |
| 814    | Layout 1 | `52062dd7e383`  |
| 805    | Layout 1 | `52062dd7e383`  |
| 794    | Layout 1 | `52062dd7e383`  |
| 787    | Layout 1 | `52062dd7e383`  |
| 780    | Layout 1 | `52062dd7e383`  |
| 771    | Layout 1 | `52062dd7e383`  |
| 760    | Layout 1 | `52062dd7e383`  |
| 748    | Layout 1 | `52062dd7e383`  |
| 741    | Layout 1 | `52062dd7e383`  |
| 736    | Layout 1 | `52062dd7e383`  |
| 731    | Layout 1 | `52062dd7e383`  |
| 723    | Layout 1 | `52062dd7e383`  |
| 711    | Layout 1 | `52062dd7e383`  |
| 707    | Layout 1 | `52062dd7e383`  |
| 697    | Layout 1 | `52062dd7e383`  |
| 689    | Layout 1 | `52062dd7e383`  |
| 683    | Layout 1 | `52062dd7e383`  |
| 678    | Layout 1 | `52062dd7e383`  |
| 670    | Layout 1 | `52062dd7e383`  |
| 661    | Layout 1 | `52062dd7e383`  |
| 656    | Layout 1 | `52062dd7e383`  |
| 652    | Layout 1 | `52062dd7e383`  |
| 643    | Layout 1 | `52062dd7e383`  |
| 637    | Layout 1 | `52062dd7e383`  |
| 630    | Layout 1 | `52062dd7e383`  |
| 627    | Layout 1 | `52062dd7e383`  |
| 621    | Layout 1 | `52062dd7e383`  |
| 617    | Layout 1 | `52062dd7e383`  |
| 615    | Layout 1 | `52062dd7e383`  |
| 606    | Layout 1 | `52062dd7e383`  |
| 599    | Layout 1 | `52062dd7e383`  |
| 592    | Layout 1 | `52062dd7e383`  |
| 586    | Layout 1 | `52062dd7e383`  |
| 577    | Layout 1 | `52062dd7e383`  |
| 569    | Layout 1 | `52062dd7e383`  |
| 561    | Layout 1 | `52062dd7e383`  |
| 554    | Layout 1 | `52062dd7e383`  |
| 542    | Layout 1 | `52062dd7e383`  |
| 532    | Layout 1 | `52062dd7e383`  |
| 531    | Layout 1 | `52062dd7e383`  |
| 526    | Layout 1 | `52062dd7e383`  |
| 521    | Layout 1 | `52062dd7e383`  |
| 517    | Layout 1 | `52062dd7e383`  |
| 510    | Layout 1 | `52062dd7e383`  |
| 508    | Layout 1 | `52062dd7e383`  |
| 504    | Layout 1 | `52062dd7e383`  |
| 497    | Layout 1 | `52062dd7e383`  |
| 491    | Layout 1 | `52062dd7e383`  |
| 485    | Layout 1 | `52062dd7e383`  |
| 478    | Layout 1 | `52062dd7e383`  |
| 472    | Layout 1 | `52062dd7e383`  |
| 466    | Layout 1 | `52062dd7e383`  |
| 457    | Layout 1 | `52062dd7e383`  |
| 452    | Layout 1 | `52062dd7e383`  |
| 449    | Layout 1 | `52062dd7e383`  |
| 435    | Layout 1 | `52062dd7e383`  |

<!-- versions:end -->

## Companion Files

None. The file is not inside the archives; the doc check reads it from the
`Paz` folder.

## Layout 1

### File Layout

| Offset                   | Type                       | Field             | Notes                                                                 |
| ------------------------ | -------------------------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00`                  | u32                        | version           | The client number (`fixtures: up to date with client NNNN` in pytest) |
| `+0x04`                  | u32                        | archive_count     | Rows in the archive table                                             |
| `+0x08`                  | Archive Row[archive_count] | archives          |                                                                       |
| `archives+0x00`          | u32                        | file_count        | Rows in the file table                                                |
| `archives+0x04`          | File Row[file_count]       | files             |                                                                       |
| `files+0x00`             | u32                        | folder_block_size | A multiple of 8                                                       |
| `files+0x04`             | bytes[folder_block_size]   | folder_block      | ICE-encrypted Folder Records, see Decrypted Blocks                    |
| `folder_block+0x00`      | u32                        | name_block_size   | A multiple of 8                                                       |
| `folder_block+0x04`      | bytes[name_block_size]     | name_block        | ICE-encrypted file names, see Decrypted Blocks; the file ends here    |

### Archive Row (12 bytes)

| Offset  | Type | Field    | Notes                                                                 |
| ------- | ---- | -------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | archive  | Archive number: `PAD00001.PAZ` is 1                                   |
| `+0x04` | u32  | checksum | Checksum of the archive file from byte 4 on; the archive's own header starts with the same value |
| `+0x08` | u32  | size     | Size of the archive file in bytes                                     |

### File Row (28 bytes)

The file's path is the folder path followed by the name:
`gamecommondata/binary/` + `stringtable.bss`.

| Offset  | Type | Field           | Notes                                                                 |
| ------- | ---- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | path_hash       | Checksum of the file's path (folder path and name, bytes as stored); the archive header row starts with the same value |
| `+0x04` | u32  | folder_index    | Index of the Folder Record that holds the file's folder path          |
| `+0x08` | u32  | name_index      | Index of the file's name in the name block                            |
| `+0x0C` | u32  | archive         | Archive number of the archive that stores the file                    |
| `+0x10` | u32  | offset          | Offset of the payload in that archive                                 |
| `+0x14` | u32  | compressed_size | Stored size of the payload                                            |
| `+0x18` | u32  | original_size   | Size after decompression                                              |

## Decrypted Blocks

Both blocks decrypt with ICE (see Notes). Their contents are not walked by
the doc check, which sees the encrypted bytes.

A folder block holds Folder Records, one after another without gaps: a u32
`first_name_index` (index of the folder's first file name in the name
block), a u32 `name_count` (file names in the folder), then the folder
`path` ending in `/` and a zero byte. Each record's `first_name_index` is
the previous record's `first_name_index + name_count`, and every file row's
`name_index` lies in its folder's range (every row on clients 435 and
3482). Zero bytes after the last record pad the block to 8 bytes.

The name block holds the file names, each ending in a zero byte, in
`name_index` order. Zero bytes after the last name pad the block to 8 bytes;
the padding is not a name.

## Checksum

`checksum` and `path_hash` use one function: Bob Jenkins' lookup3
`hashlittle` with its own start value and final mix. All arithmetic is on
u32 values.

1. `a`, `b` and `c` start at `length - 0x2145E233` (the input length in
   bytes; `0xDEADBEEF + length + 0xC5EDE` in lookup3 terms). An empty input
   gives 0.
2. While more than 12 bytes remain, add the next three little-endian u32 to
   `a`, `b` and `c` and run lookup3's `mix`.
3. Add the last 1 to 12 bytes, zero-padded to 12, to `a`, `b` and `c` the
   same way.
4. Final mix, where `rol` and `ror` rotate left and right:

| Step | Value |
| ---- | ----- |
| 1    | `p = (b ^ c) - rol(b, 14)` |
| 2    | `q = (a ^ p) - rol(p, 11)` |
| 3    | `r = (q ^ b) - ror(q, 7)` |
| 4    | `s = (r ^ p) - rol(r, 16)` |
| 5    | `t = (q ^ s) - rol(s, 4)` |
| 6    | `u = (t ^ r) - rol(t, 14)` |
| 7    | result `(u ^ s) - ror(u, 8)` |

On clients 435, 1784 and 3482, `path_hash` matches every file row
(471,162, 568,977 and 872,965 rows) and `checksum` matches every archive on
disk (30, 32 and 30). `pa_checksum` in `PAZ-Parser/paz/bdo_checksum.py` computes it, and
`PAZ-Parser/tests/test_checksum.py` checks it on the smallest archive of the
installed client. The function is `PaChecksum` in
MrIkso/CrimsonDesertTools (`Utils/PaChecksum.cs`, written for Crimson
Desert); `calculatePackCRC` in kukdh1/PAZ-Unpacker starts from the same
`length - 0x2145E233`.

## Notes

Both blocks are encrypted with ICE and the same key as the path block of a
`PAD*.PAZ` header (`BDO_ICE_KEY` in `PAZ-Parser/paz/bdo_ice.py`). ICE has no
chaining between 8-byte blocks, so each block decrypts in one call.

`read_meta_entries` decodes paths as UTF-8 with invalid bytes replaced, as
`parse_paz_files` does for the archive headers, so the two give the same
paths. A few names are CP949 (Korean) bytes and come out as replacement
characters in both; decoded as CP949 they read `gamecommondata/dialogscene/스폰.zip`
and `character/ai 스크립트_메뉴얼.xml`.

On clients 435, 508, 1058, 2313 and 3482, the entries `read_meta_entries`
gives for every archive on disk equal the entries `parse_paz_files` reads
from those archives' headers. `PAZ-Parser/tests/test_meta_reader.py` checks
this on the first 20 archives of the installed client.
