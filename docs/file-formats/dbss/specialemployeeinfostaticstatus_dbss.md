# `specialemployeeinfostaticstatus.dbss` Format

## Purpose

The special sailors: one row per sailor that is hired with an item of its
own instead of the Sailor Contract Certificate of the port sailors in
[`employeespawninfo.dbss`](employeespawninfo_dbss.md). Each row holds the
sailor character, the item and count the hire takes, the success rate and
the Korean lines the sailor says when hired and when it refuses. Client
3474 has three: Arkahn (`59101`, Proix's Old Compass), Hetario (`59227`)
and Pacuna (`59228`). Companion
`specialemployeeinfostaticstatusoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                         | Bytes | Records                      | Row bytes                 |
| ------ | -------------- | -------------------------------------------- | ----- | ---------------------------- | ------------------------- |
| 1      | 1346 and later | `specialemployeeinfostaticstatus.dbss`       | 391   | 3 Row, 2 Group               | 87 to 187, 128 on average |
| 1      | 1346 and later | `specialemployeeinfostaticstatusoffset.dbss` | 42    | 3 Offset Row, 2 Offset Group | 10                        |

| Layout | File                                         | Known         | Unknown     |
| ------ | -------------------------------------------- | ------------- | ----------- |
| 1      | `specialemployeeinfostaticstatus.dbss`       | 379 B (96.9%) | 12 B (3.1%) |
| 1      | `specialemployeeinfostaticstatusoffset.dbss` | 42 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `b82340553afb`  |
| 3482   | Layout 1             | `b82340553afb`  |
| 3474   | Layout 1             | `b82340553afb`  |
| 3473   | Layout 1             | `b82340553afb`  |
| 3464   | Layout 1             | `b82340553afb`  |
| 3458   | Layout 1             | `b82340553afb`  |
| 3454   | Layout 1             | `b82340553afb`  |
| 3444   | Layout 1             | `b82340553afb`  |
| 3435   | Layout 1             | `b82340553afb`  |
| 3426   | Layout 1             | `b82340553afb`  |
| 3418   | Layout 1             | `b82340553afb`  |
| 3412   | Layout 1             | `b82340553afb`  |
| 3402   | Layout 1             | `b82340553afb`  |
| 3396   | Layout 1             | `b82340553afb`  |
| 3387   | Layout 1             | `b82340553afb`  |
| 3381   | Layout 1             | `b82340553afb`  |
| 3373   | Layout 1             | `b82340553afb`  |
| 3364   | Layout 1             | `b82340553afb`  |
| 3356   | Layout 1             | `b82340553afb`  |
| 3349   | Layout 1             | `b82340553afb`  |
| 3342   | Layout 1             | `b82340553afb`  |
| 3335   | Layout 1             | `b82340553afb`  |
| 3326   | Layout 1             | `b82340553afb`  |
| 3321   | Layout 1             | `b82340553afb`  |
| 3314   | Layout 1             | `b82340553afb`  |
| 3303   | Layout 1             | `b82340553afb`  |
| 3302   | Layout 1             | `b82340553afb`  |
| 3293   | Layout 1             | `b82340553afb`  |
| 3283   | Layout 1             | `b82340553afb`  |
| 3275   | Layout 1             | `b82340553afb`  |
| 3267   | Layout 1             | `b82340553afb`  |
| 3258   | Layout 1             | `b82340553afb`  |
| 3251   | Layout 1             | `b82340553afb`  |
| 3242   | Layout 1             | `b82340553afb`  |
| 3235   | Layout 1             | `b82340553afb`  |
| 3229   | Layout 1             | `b82340553afb`  |
| 3212   | Layout 1             | `b82340553afb`  |
| 3203   | Layout 1             | `b82340553afb`  |
| 3193   | Layout 1             | `b82340553afb`  |
| 3186   | Layout 1             | `b82340553afb`  |
| 3177   | Layout 1             | `b82340553afb`  |
| 3169   | Layout 1             | `b82340553afb`  |
| 3158   | Layout 1             | `b82340553afb`  |
| 3151   | Layout 1             | `b82340553afb`  |
| 3144   | Layout 1             | `b82340553afb`  |
| 3133   | Layout 1             | `b82340553afb`  |
| 3125   | Layout 1             | `b82340553afb`  |
| 3118   | Layout 1             | `b82340553afb`  |
| 3111   | Layout 1             | `b82340553afb`  |
| 3103   | Layout 1             | `b82340553afb`  |
| 3095   | Layout 1             | `b82340553afb`  |
| 3086   | Layout 1             | `b82340553afb`  |
| 3072   | Layout 1             | `b82340553afb`  |
| 3062   | Layout 1             | `b82340553afb`  |
| 3052   | Layout 1             | `b82340553afb`  |
| 3045   | Layout 1             | `b82340553afb`  |
| 3037   | Layout 1             | `b82340553afb`  |
| 3030   | Layout 1             | `b82340553afb`  |
| 3021   | Layout 1             | `b82340553afb`  |
| 3012   | Layout 1             | `b82340553afb`  |
| 3002   | Layout 1             | `b82340553afb`  |
| 2995   | Layout 1             | `b82340553afb`  |
| 2987   | Layout 1             | `b82340553afb`  |
| 2978   | Layout 1             | `b82340553afb`  |
| 2970   | Layout 1             | `b82340553afb`  |
| 2959   | Layout 1             | `b82340553afb`  |
| 2951   | Layout 1             | `b82340553afb`  |
| 2942   | Layout 1             | `b82340553afb`  |
| 2935   | Layout 1             | `b82340553afb`  |
| 2932   | Layout 1             | `b82340553afb`  |
| 2923   | Layout 1             | `b82340553afb`  |
| 2919   | Layout 1             | `b82340553afb`  |
| 2907   | Layout 1             | `b82340553afb`  |
| 2900   | Layout 1             | `b82340553afb`  |
| 2891   | Layout 1             | `b82340553afb`  |
| 2882   | Layout 1             | `b82340553afb`  |
| 2872   | Layout 1             | `b82340553afb`  |
| 2863   | Layout 1             | `b82340553afb`  |
| 2855   | Layout 1             | `b82340553afb`  |
| 2849   | Layout 1             | `b82340553afb`  |
| 2844   | Layout 1             | `b82340553afb`  |
| 2834   | Layout 1             | `b82340553afb`  |
| 2825   | Layout 1             | `b82340553afb`  |
| 2819   | Layout 1             | `b82340553afb`  |
| 2811   | Layout 1             | `b82340553afb`  |
| 2803   | Layout 1             | `b82340553afb`  |
| 2794   | Layout 1             | `b82340553afb`  |
| 2783   | Layout 1             | `b82340553afb`  |
| 2774   | Layout 1             | `b82340553afb`  |
| 2765   | Layout 1             | `b82340553afb`  |
| 2756   | Layout 1             | `b82340553afb`  |
| 2750   | Layout 1             | `b82340553afb`  |
| 2743   | Layout 1             | `b82340553afb`  |
| 2736   | Layout 1             | `b82340553afb`  |
| 2726   | Layout 1             | `b82340553afb`  |
| 2717   | Layout 1             | `b82340553afb`  |
| 2709   | Layout 1             | `b82340553afb`  |
| 2703   | Layout 1             | `b82340553afb`  |
| 2695   | Layout 1             | `b82340553afb`  |
| 2684   | Layout 1             | `b82340553afb`  |
| 2672   | Layout 1             | `b82340553afb`  |
| 2665   | Layout 1             | `b82340553afb`  |
| 2657   | Layout 1             | `b82340553afb`  |
| 2649   | Layout 1             | `b82340553afb`  |
| 2644   | Layout 1             | `b82340553afb`  |
| 2637   | Layout 1             | `b82340553afb`  |
| 2629   | Layout 1             | `b82340553afb`  |
| 2619   | Layout 1             | `b82340553afb`  |
| 2612   | Layout 1             | `b82340553afb`  |
| 2606   | Layout 1             | `b82340553afb`  |
| 2602   | Layout 1             | `b82340553afb`  |
| 2601   | Layout 1             | `b82340553afb`  |
| 2592   | Layout 1             | `b82340553afb`  |
| 2583   | Layout 1             | `b82340553afb`  |
| 2575   | Layout 1             | `b82340553afb`  |
| 2567   | Layout 1             | `b82340553afb`  |
| 2560   | Layout 1             | `b82340553afb`  |
| 2553   | Layout 1             | `b82340553afb`  |
| 2545   | Layout 1             | `b82340553afb`  |
| 2538   | Layout 1             | `b82340553afb`  |
| 2529   | Layout 1             | `b82340553afb`  |
| 2519   | Layout 1             | `b82340553afb`  |
| 2513   | Layout 1             | `b82340553afb`  |
| 2510   | Layout 1             | `b82340553afb`  |
| 2507   | Layout 1             | `b82340553afb`  |
| 2503   | Layout 1             | `b82340553afb`  |
| 2498   | Layout 1             | `b82340553afb`  |
| 2492   | Layout 1             | `b82340553afb`  |
| 2487   | Layout 1             | `b82340553afb`  |
| 2480   | Layout 1             | `b82340553afb`  |
| 2474   | Layout 1             | `b82340553afb`  |
| 2468   | Layout 1             | `b82340553afb`  |
| 2460   | Layout 1             | `b82340553afb`  |
| 2453   | Layout 1             | `b82340553afb`  |
| 2444   | Layout 1             | `b82340553afb`  |
| 2438   | Layout 1             | `b82340553afb`  |
| 2434   | Layout 1             | `b82340553afb`  |
| 2429   | Layout 1             | `b82340553afb`  |
| 2421   | Layout 1             | `b82340553afb`  |
| 2414   | Layout 1             | `b82340553afb`  |
| 2407   | Layout 1             | `b82340553afb`  |
| 2401   | Layout 1             | `b82340553afb`  |
| 2397   | Layout 1             | `b82340553afb`  |
| 2393   | Layout 1             | `b82340553afb`  |
| 2384   | Layout 1             | `b82340553afb`  |
| 2378   | Layout 1             | `b82340553afb`  |
| 2372   | Layout 1             | `b82340553afb`  |
| 2358   | Layout 1             | `b82340553afb`  |
| 2352   | Layout 1             | `b82340553afb`  |
| 2347   | Layout 1             | `b82340553afb`  |
| 2343   | Layout 1             | `b82340553afb`  |
| 2335   | Layout 1             | `b82340553afb`  |
| 2327   | Layout 1             | `b82340553afb`  |
| 2324   | Layout 1             | `b82340553afb`  |
| 2319   | Layout 1             | `b82340553afb`  |
| 2313   | Layout 1             | `b82340553afb`  |
| 2308   | Layout 1             | `b82340553afb`  |
| 2302   | Layout 1             | `b82340553afb`  |
| 2295   | Layout 1             | `b82340553afb`  |
| 2290   | Layout 1             | `b82340553afb`  |
| 2284   | Layout 1             | `b82340553afb`  |
| 2276   | Layout 1             | `b82340553afb`  |
| 2269   | Layout 1             | `b82340553afb`  |
| 2259   | Layout 1             | `b82340553afb`  |
| 2250   | Layout 1             | `b82340553afb`  |
| 2243   | Layout 1             | `b82340553afb`  |
| 2235   | Layout 1             | `b82340553afb`  |
| 2229   | Layout 1             | `b82340553afb`  |
| 2224   | Layout 1             | `b82340553afb`  |
| 2218   | Layout 1             | `b82340553afb`  |
| 2215   | Layout 1             | `b82340553afb`  |
| 2207   | Layout 1             | `b82340553afb`  |
| 2203   | Layout 1             | `b82340553afb`  |
| 2196   | Layout 1             | `b82340553afb`  |
| 2192   | Layout 1             | `b82340553afb`  |
| 2189   | Layout 1             | `b82340553afb`  |
| 2183   | Layout 1             | `b82340553afb`  |
| 2179   | Layout 1             | `b82340553afb`  |
| 2171   | Layout 1             | `b82340553afb`  |
| 2163   | Layout 1             | `b82340553afb`  |
| 2156   | Layout 1             | `b82340553afb`  |
| 2151   | Layout 1             | `b82340553afb`  |
| 2147   | Layout 1             | `b82340553afb`  |
| 2142   | Layout 1             | `b82340553afb`  |
| 2138   | Layout 1             | `b82340553afb`  |
| 2134   | Layout 1             | `b82340553afb`  |
| 2130   | Layout 1             | `b82340553afb`  |
| 2122   | Layout 1             | `b82340553afb`  |
| 2107   | Layout 1             | `b82340553afb`  |
| 2098   | Layout 1             | `b82340553afb`  |
| 2089   | Layout 1             | `b82340553afb`  |
| 2081   | Layout 1             | `b82340553afb`  |
| 2073   | Layout 1             | `b82340553afb`  |
| 2067   | Layout 1             | `b82340553afb`  |
| 2063   | Layout 1             | `b82340553afb`  |
| 2059   | Layout 1             | `b82340553afb`  |
| 2052   | Layout 1             | `b82340553afb`  |
| 2044   | Layout 1             | `b82340553afb`  |
| 2039   | Layout 1             | `b82340553afb`  |
| 2032   | Layout 1             | `b82340553afb`  |
| 2025   | Layout 1             | `b82340553afb`  |
| 2011   | Layout 1             | `b82340553afb`  |
| 2005   | Layout 1             | `b82340553afb`  |
| 2000   | Layout 1             | `b82340553afb`  |
| 1996   | Layout 1             | `b82340553afb`  |
| 1991   | Layout 1             | `b82340553afb`  |
| 1985   | Layout 1             | `b82340553afb`  |
| 1980   | Layout 1             | `b82340553afb`  |
| 1969   | Layout 1             | `b82340553afb`  |
| 1964   | Layout 1             | `b82340553afb`  |
| 1958   | Layout 1             | `b82340553afb`  |
| 1950   | Layout 1             | `b82340553afb`  |
| 1945   | Layout 1             | `b82340553afb`  |
| 1937   | Layout 1             | `b82340553afb`  |
| 1933   | Layout 1             | `b82340553afb`  |
| 1927   | Layout 1             | `b82340553afb`  |
| 1921   | Layout 1             | `b82340553afb`  |
| 1914   | Layout 1             | `b82340553afb`  |
| 1908   | Layout 1             | `b82340553afb`  |
| 1897   | Layout 1             | `b82340553afb`  |
| 1892   | Layout 1             | `b82340553afb`  |
| 1886   | Layout 1             | `b82340553afb`  |
| 1881   | Layout 1             | `b82340553afb`  |
| 1871   | Layout 1             | `b82340553afb`  |
| 1866   | Layout 1             | `b82340553afb`  |
| 1862   | Layout 1             | `b82340553afb`  |
| 1854   | Layout 1             | `b82340553afb`  |
| 1846   | Layout 1             | `b82340553afb`  |
| 1838   | Layout 1             | `b82340553afb`  |
| 1832   | Layout 1             | `b82340553afb`  |
| 1826   | Layout 1             | `b82340553afb`  |
| 1822   | Layout 1             | `b82340553afb`  |
| 1818   | Layout 1             | `b82340553afb`  |
| 1804   | Layout 1             | `b82340553afb`  |
| 1794   | Layout 1             | `b82340553afb`  |
| 1790   | Layout 1             | `b82340553afb`  |
| 1784   | Layout 1             | `b82340553afb`  |
| 1774   | Layout 1             | `b82340553afb`  |
| 1771   | Layout 1             | `b82340553afb`  |
| 1762   | Layout 1             | `b82340553afb`  |
| 1759   | Layout 1             | `b82340553afb`  |
| 1754   | Layout 1             | `b82340553afb`  |
| 1749   | Layout 1             | `b82340553afb`  |
| 1743   | Layout 1             | `b82340553afb`  |
| 1737   | Layout 1             | `b82340553afb`  |
| 1731   | Layout 1             | `b82340553afb`  |
| 1725   | Layout 1             | `b82340553afb`  |
| 1717   | Layout 1             | `b82340553afb`  |
| 1710   | Layout 1             | `b82340553afb`  |
| 1704   | Layout 1             | `b82340553afb`  |
| 1698   | Layout 1             | `b82340553afb`  |
| 1690   | Layout 1             | `b82340553afb`  |
| 1685   | Layout 1             | `b82340553afb`  |
| 1680   | Layout 1             | `b82340553afb`  |
| 1674   | Layout 1             | `b82340553afb`  |
| 1668   | Layout 1             | `b82340553afb`  |
| 1659   | Layout 1             | `b82340553afb`  |
| 1649   | Layout 1             | `b82340553afb`  |
| 1642   | Layout 1             | `b82340553afb`  |
| 1636   | Layout 1             | `b82340553afb`  |
| 1628   | Layout 1             | `b82340553afb`  |
| 1622   | Layout 1             | `b82340553afb`  |
| 1614   | Layout 1             | `b82340553afb`  |
| 1608   | Layout 1             | `b82340553afb`  |
| 1602   | Layout 1             | `b82340553afb`  |
| 1598   | Layout 1             | `b82340553afb`  |
| 1594   | Layout 1             | `b82340553afb`  |
| 1590   | Layout 1             | `b82340553afb`  |
| 1587   | Layout 1             | `b82340553afb`  |
| 1584   | Layout 1             | `b82340553afb`  |
| 1579   | Layout 1             | `b82340553afb`  |
| 1572   | Layout 1             | `b82340553afb`  |
| 1565   | Layout 1             | `b82340553afb`  |
| 1559   | Layout 1             | `b82340553afb`  |
| 1554   | Layout 1             | `b82340553afb`  |
| 1547   | Layout 1             | `b82340553afb`  |
| 1537   | Layout 1             | `b82340553afb`  |
| 1529   | Layout 1             | `b82340553afb`  |
| 1524   | Layout 1             | `b82340553afb`  |
| 1519   | Layout 1             | `b82340553afb`  |
| 1509   | Layout 1             | `b82340553afb`  |
| 1506   | Layout 1             | `b82340553afb`  |
| 1504   | Layout 1             | `b82340553afb`  |
| 1500   | Layout 1             | `b82340553afb`  |
| 1493   | Layout 1             | `b82340553afb`  |
| 1489   | Layout 1             | `b82340553afb`  |
| 1485   | Layout 1             | `b82340553afb`  |
| 1481   | Layout 1             | `b82340553afb`  |
| 1474   | Layout 1             | `b82340553afb`  |
| 1466   | Layout 1             | `b82340553afb`  |
| 1462   | Layout 1             | `b82340553afb`  |
| 1459   | Layout 1             | `b82340553afb`  |
| 1453   | Layout 1             | `b82340553afb`  |
| 1450   | Layout 1             | `b82340553afb`  |
| 1445   | Layout 1             | `b82340553afb`  |
| 1439   | Layout 1             | `b82340553afb`  |
| 1433   | Layout 1             | `b82340553afb`  |
| 1430   | Layout 1             | `b82340553afb`  |
| 1426   | Layout 1             | `b82340553afb`  |
| 1421   | Layout 1             | `b82340553afb`  |
| 1417   | Layout 1             | `b82340553afb`  |
| 1416   | Layout 1             | `b82340553afb`  |
| 1409   | Layout 1             | `b82340553afb`  |
| 1405   | Layout 1             | `b82340553afb`  |
| 1401   | Layout 1             | `b82340553afb`  |
| 1396   | Layout 1             | `b82340553afb`  |
| 1391   | Layout 1             | `b82340553afb`  |
| 1390   | Layout 1             | `b82340553afb`  |
| 1386   | Layout 1             | `b82340553afb`  |
| 1381   | Layout 1             | `b82340553afb`  |
| 1379   | Layout 1             | `b82340553afb`  |
| 1372   | Layout 1             | `b82340553afb`  |
| 1366   | Layout 1             | `b82340553afb`  |
| 1364   | Layout 1             | `b82340553afb`  |
| 1363   | Layout 1             | `b82340553afb`  |
| 1360   | Layout 1             | `b82340553afb`  |
| 1358   | Layout 1             | `b82340553afb`  |
| 1355   | Layout 1             | `b82340553afb`  |
| 1351   | Layout 1             | `b82340553afb`  |
| 1348   | Layout 1             | `b82340553afb`  |
| 1346   | Layout 1             | `b82340553afb`  |
| 1341   | No documented layout | `b82340553afb`  |
| 1340   | No documented layout | `b82340553afb`  |
| 1338   | No documented layout | `b82340553afb`  |
| 1335   | No documented layout | `b82340553afb`  |
| 1333   | No documented layout | `b82340553afb`  |
| 1329   | No documented layout | `b82340553afb`  |
| 1327   | No documented layout | `b82340553afb`  |
| 1324   | No documented layout | `b82340553afb`  |
| 1321   | No documented layout | `b82340553afb`  |
| 1319   | No documented layout | `b82340553afb`  |
| 1318   | No documented layout | `b82340553afb`  |
| 1316   | No documented layout | `b82340553afb`  |
| 1313   | No documented layout | `b82340553afb`  |
| 1311   | No documented layout | `b82340553afb`  |
| 1309   | No documented layout | `b82340553afb`  |
| 1304   | No documented layout | `b82340553afb`  |
| 1292   | No documented layout | `b82340553afb`  |
| 1286   | No documented layout | `b82340553afb`  |
| 1280   | No documented layout | `b82340553afb`  |
| 1276   | No documented layout | `b82340553afb`  |
| 1267   | No documented layout | `b82340553afb`  |
| 1261   | No file              | `b82340553afb`  |
| 1256   | No file              | `b82340553afb`  |
| 1250   | No file              | `b82340553afb`  |
| 1246   | No file              | `b82340553afb`  |
| 1239   | No file              | `b82340553afb`  |
| 1230   | No file              | `b82340553afb`  |
| 1226   | No file              | `b82340553afb`  |
| 1220   | No file              | `b82340553afb`  |
| 1217   | No file              | `b82340553afb`  |
| 1211   | No file              | `b82340553afb`  |
| 1210   | No file              | `b82340553afb`  |
| 1208   | No file              | `b82340553afb`  |
| 1203   | No file              | `b82340553afb`  |
| 1197   | No file              | `b82340553afb`  |
| 1194   | No file              | `b82340553afb`  |
| 1192   | No file              | `b82340553afb`  |
| 1187   | No file              | `b82340553afb`  |
| 1183   | No file              | `b82340553afb`  |
| 1177   | No file              | `b82340553afb`  |
| 1173   | No file              | `b82340553afb`  |
| 1167   | No file              | `b82340553afb`  |
| 1164   | No file              | `b82340553afb`  |
| 1156   | No file              | `b82340553afb`  |
| 1149   | No file              | `b82340553afb`  |
| 1144   | No file              | `b82340553afb`  |
| 1137   | No file              | `b82340553afb`  |
| 1132   | No file              | `b82340553afb`  |
| 1127   | No file              | `b82340553afb`  |
| 1122   | No file              | `b82340553afb`  |
| 1118   | No file              | `b82340553afb`  |
| 1114   | No file              | `b82340553afb`  |
| 1109   | No file              | `b82340553afb`  |
| 1102   | No file              | `b82340553afb`  |
| 1096   | No file              | `b82340553afb`  |
| 1088   | No file              | `b82340553afb`  |
| 1081   | No file              | `b82340553afb`  |
| 1076   | No file              | `b82340553afb`  |
| 1069   | No file              | `b82340553afb`  |
| 1064   | No file              | `b82340553afb`  |
| 1058   | No file              | `b82340553afb`  |
| 1051   | No file              | `b82340553afb`  |
| 1044   | No file              | `b82340553afb`  |
| 1036   | No file              | `b82340553afb`  |
| 1026   | No file              | `b82340553afb`  |
| 1016   | No file              | `b82340553afb`  |
| 1009   | No file              | `b82340553afb`  |
| 1005   | No file              | `b82340553afb`  |
| 1000   | No file              | `b82340553afb`  |
| 998    | No file              | `b82340553afb`  |
| 990    | No file              | `b82340553afb`  |
| 979    | No file              | `b82340553afb`  |
| 972    | No file              | `b82340553afb`  |
| 963    | No file              | `b82340553afb`  |
| 955    | No file              | `b82340553afb`  |
| 946    | No file              | `b82340553afb`  |
| 938    | No file              | `b82340553afb`  |
| 927    | No file              | `b82340553afb`  |
| 911    | No file              | `b82340553afb`  |
| 904    | No file              | `b82340553afb`  |
| 899    | No file              | `b82340553afb`  |
| 894    | No file              | `b82340553afb`  |
| 885    | No file              | `b82340553afb`  |
| 879    | No file              | `b82340553afb`  |
| 872    | No file              | `b82340553afb`  |
| 864    | No file              | `b82340553afb`  |
| 855    | No file              | `b82340553afb`  |
| 853    | No file              | `b82340553afb`  |
| 845    | No file              | `b82340553afb`  |
| 837    | No file              | `b82340553afb`  |
| 829    | No file              | `b82340553afb`  |
| 822    | No file              | `b82340553afb`  |
| 814    | No file              | `b82340553afb`  |
| 805    | No file              | `b82340553afb`  |
| 794    | No file              | `b82340553afb`  |
| 787    | No file              | `b82340553afb`  |
| 780    | No file              | `b82340553afb`  |
| 771    | No file              | `b82340553afb`  |
| 760    | No file              | `b82340553afb`  |
| 748    | No file              | `b82340553afb`  |
| 741    | No file              | `b82340553afb`  |
| 736    | No file              | `b82340553afb`  |
| 731    | No file              | `b82340553afb`  |
| 723    | No file              | `b82340553afb`  |
| 711    | No file              | `b82340553afb`  |
| 707    | No file              | `b82340553afb`  |
| 697    | No file              | `b82340553afb`  |
| 689    | No file              | `b82340553afb`  |
| 683    | No file              | `b82340553afb`  |
| 678    | No file              | `b82340553afb`  |
| 670    | No file              | `b82340553afb`  |
| 661    | No file              | `b82340553afb`  |
| 656    | No file              | `b82340553afb`  |
| 652    | No file              | `b82340553afb`  |
| 643    | No file              | `b82340553afb`  |
| 637    | No file              | `b82340553afb`  |
| 630    | No file              | `b82340553afb`  |
| 627    | No file              | `b82340553afb`  |
| 621    | No file              | `b82340553afb`  |
| 617    | No file              | `b82340553afb`  |
| 615    | No file              | `b82340553afb`  |
| 606    | No file              | `b82340553afb`  |
| 599    | No file              | `b82340553afb`  |
| 592    | No file              | `b82340553afb`  |
| 586    | No file              | `b82340553afb`  |
| 577    | No file              | `b82340553afb`  |
| 569    | No file              | `b82340553afb`  |
| 561    | No file              | `b82340553afb`  |
| 554    | No file              | `b82340553afb`  |
| 542    | No file              | `b82340553afb`  |
| 532    | No file              | `b82340553afb`  |
| 531    | No file              | `b82340553afb`  |
| 526    | No file              | `b82340553afb`  |
| 521    | No file              | `b82340553afb`  |
| 517    | No file              | `b82340553afb`  |
| 510    | No file              | `b82340553afb`  |
| 508    | No file              | `b82340553afb`  |
| 504    | No file              | `b82340553afb`  |
| 497    | No file              | `b82340553afb`  |
| 491    | No file              | `b82340553afb`  |
| 485    | No file              | `b82340553afb`  |
| 478    | No file              | `b82340553afb`  |
| 472    | No file              | `b82340553afb`  |
| 466    | No file              | `b82340553afb`  |
| 457    | No file              | `b82340553afb`  |
| 452    | No file              | `b82340553afb`  |
| 449    | No file              | `b82340553afb`  |
| 435    | No file              | `b82340553afb`  |

<!-- versions:end -->

## Companion Files

| File                                              | Required | Role                                                                |
| ------------------------------------------------- | -------- | ------------------------------------------------------------------- |
| `specialemployeeinfostaticstatusoffset.dbss`      | Optional | `type -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row |
| `languagedata_en.loc`                             | Optional | Sailor names (LOC type `6`) and item names (LOC type `0`)            |

LOC type 70, which holds the lines of the port sailors, has no lines for
these three characters on client 3474; the handler shows the inline
Korean text.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes                                                     |
| ------- | ------------ | ------ | --------------------------------------------------------- |
| `+0x00` | Group[..end] | groups | Back to back to the end of the file; see Group            |

The file has no group count; `specialemployeeinfostaticstatusoffset.dbss`
stores it. Client 3474 has two groups, the second empty (its count `0` is
the last 4 bytes of the file); client 1784 has one.

### Group (variable: 4 bytes + rows)

| Offset  | Type       | Field | Notes                                 |
| ------- | ---------- | ----- | ------------------------------------- |
| `+0x00` | u32        | count | Number of rows in the group           |
| `+0x04` | Row[count] | rows  | See Row                               |

### Row (variable: 41 bytes + line text)

| Offset                       | Type  | Field                          | Notes                                                                 |
| ---------------------------- | ----- | ------------------------------ | --------------------------------------------------------------------- |
| `+0x00`                      | u8    | category                       | `0` on every row of clients 1784 and 3474                              |
| `+0x01`                      | u16   | type                           | Row key, `21` to `23` on client 3474; see Open Questions               |
| `+0x03`                      | u16   | character_key                  | The sailor character                                                  |
| `+0x05`                      | u32   | need_item_key                  | Item the hire takes (LOC type `0`)                                    |
| `+0x09`                      | u64   | need_item_count                | `1` on every row of client 3474                                       |
| `+0x11`                      | u32   | employ_success_rate            | Out of 1,000,000; `1000000` (100%) on every row of client 3474         |
| `+0x15`                      | str16 | employ_success_word_kr         | Korean line when the sailor is hired; real line breaks (`0x0A`)        |
| `employ_success_word_kr+0x00` | str16 | employ_fail_word_kr            | Korean line when the hire fails                                       |
| `employ_fail_word_kr+0x00`   | u32   | unknown_employ_fail_word_kr_00 | `0` on every row of clients 1784 and 3474; the row ends after it       |

### `specialemployeeinfostaticstatusoffset.dbss`

Offset table into `specialemployeeinfostaticstatus.dbss` with a group
count before the same groups (no PABR magic, no trailer).

| Offset  | Type                       | Field       | Notes                                                    |
| ------- | -------------------------- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32                        | group_count | Number of groups; `2` on client 3474, `1` on client 1784 |
| `+0x04` | Offset Group[group_count]  | groups      | See Offset Group                                         |

### Offset Group (variable: 4 bytes + rows)

| Offset  | Type              | Field | Notes                                                    |
| ------- | ----------------- | ----- | -------------------------------------------------------- |
| `+0x00` | u32               | count | Equals the `count` of the same group in the main file    |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                           |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                           |
| ------- | ---- | ----------- | --------------------------------------------------------------- |
| `+0x00` | u16  | type        | Key of the row it points at                                     |
| `+0x02` | u32  | data_offset | Absolute offset of the row in the main file, at `category`      |
| `+0x06` | u32  | data_size   | Row size in bytes, `category` to `unknown_employ_fail_word_kr_00` |

The index rows are in file order; on clients 1784 and 3474 every index
row points at the row with its type, and the rows and group counts fill
the main file.

## Field Names

The `SpecialEmployee_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Category`, `Type`, `CharacterKey`,
`ActionIndex`, `EmploySuccessRate`, `NeedItemKey`, `NeedItemCount`,
`EmploySuccessWord` and `EmployFailWord`. Its three rows match the file on
all three types and on every column but `ActionIndex`, on client 1784 and
on client 3474; the file stores the columns in its own order. `Category`
is `0` on every row of the sheet and the file, so `category` rests on the
column order alone. `ActionIndex` holds the same values as `Type` (`21` to
`23`), so it has no field of its own in the file, or it is the field named
`type` here. No client Lua names the table, and the 2016 client's debug
symbols have no struct for it.

## Notes

- The row tail matches the hire block of
  [`employeespawninfo.dbss`](employeespawninfo_dbss.md): an item key, a u64
  count, a u32 `1000000`, two Korean lines and a u32 `0`. There the
  `1000000` before the lines is `unknown_28`.
- The hire items of Hetario (`65623`) and Pacuna (`65622`) are named
  `NO USE` in LOC type 0 on client 3474; their descriptions call them a
  fishing rod of the Otters and a honey jar of the Papus.

## Open Questions

### Type or ActionIndex

The u16 at `+0x01` holds `21`, `22` and `23`, the values of both the
`Type` and the `ActionIndex` column of the sheet. A row where the two
differ would show which one the file keeps.

### What the Groups Are

Client 3474 adds a second, empty group that client 1784 does not have.
The groups may split the rows by `category`: every row is in the first
group and has `category` `0`. A row with another category would test it.
