# `npcgift.dbss` Format

## Purpose

The gift items of the in-game "Give Gift" interaction: per NPC, the accepted gift item IDs and the Amity gained for each. The NPC's reply to a confession is in [`npcgiftdata.dbss`](npcgiftdata_dbss.md), keyed by the same NPC IDs.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes | Records                      | Row bytes |
| ------ | -------------- | -------------------- | ----- | ---------------------------- | --------- |
| 1      | 1346 and later | `npcgift.dbss`       | 1,552 | 117 Gift Row, 24 Gift Record | 12        |
| 1      | 1346 and later | `npcgiftoffset.dbss` | 244   | 24 Offset Record             | 10        |

| Layout | File                 | Known            | Unknown      |
| ------ | -------------------- | ---------------- | ------------ |
| 1      | `npcgift.dbss`       | 1,552 B (100.0%) | 0 B (0.0%)   |
| 1      | `npcgiftoffset.dbss` | 196 B (80.3%)    | 48 B (19.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `1286a536ed20`  |
| 3482   | Layout 1             | `1286a536ed20`  |
| 3474   | Layout 1             | `1286a536ed20`  |
| 3473   | Layout 1             | `1286a536ed20`  |
| 3464   | Layout 1             | `1286a536ed20`  |
| 3458   | Layout 1             | `1286a536ed20`  |
| 3454   | Layout 1             | `1286a536ed20`  |
| 3444   | Layout 1             | `1286a536ed20`  |
| 3435   | Layout 1             | `1286a536ed20`  |
| 3426   | Layout 1             | `1286a536ed20`  |
| 3418   | Layout 1             | `1286a536ed20`  |
| 3412   | Layout 1             | `1286a536ed20`  |
| 3402   | Layout 1             | `1286a536ed20`  |
| 3396   | Layout 1             | `1286a536ed20`  |
| 3387   | Layout 1             | `1286a536ed20`  |
| 3381   | Layout 1             | `1286a536ed20`  |
| 3373   | Layout 1             | `1286a536ed20`  |
| 3364   | Layout 1             | `1286a536ed20`  |
| 3356   | Layout 1             | `1286a536ed20`  |
| 3349   | Layout 1             | `1286a536ed20`  |
| 3342   | Layout 1             | `1286a536ed20`  |
| 3335   | Layout 1             | `1286a536ed20`  |
| 3326   | Layout 1             | `1286a536ed20`  |
| 3321   | Layout 1             | `1286a536ed20`  |
| 3314   | Layout 1             | `1286a536ed20`  |
| 3303   | Layout 1             | `1286a536ed20`  |
| 3302   | Layout 1             | `1286a536ed20`  |
| 3293   | Layout 1             | `1286a536ed20`  |
| 3283   | Layout 1             | `1286a536ed20`  |
| 3275   | Layout 1             | `1286a536ed20`  |
| 3267   | Layout 1             | `1286a536ed20`  |
| 3258   | Layout 1             | `1286a536ed20`  |
| 3251   | Layout 1             | `1286a536ed20`  |
| 3242   | Layout 1             | `1286a536ed20`  |
| 3235   | Layout 1             | `1286a536ed20`  |
| 3229   | Layout 1             | `1286a536ed20`  |
| 3212   | Layout 1             | `1286a536ed20`  |
| 3203   | Layout 1             | `1286a536ed20`  |
| 3193   | Layout 1             | `1286a536ed20`  |
| 3186   | Layout 1             | `1286a536ed20`  |
| 3177   | Layout 1             | `1286a536ed20`  |
| 3169   | Layout 1             | `1286a536ed20`  |
| 3158   | Layout 1             | `1286a536ed20`  |
| 3151   | Layout 1             | `1286a536ed20`  |
| 3144   | Layout 1             | `1286a536ed20`  |
| 3133   | Layout 1             | `1286a536ed20`  |
| 3125   | Layout 1             | `1286a536ed20`  |
| 3118   | Layout 1             | `1286a536ed20`  |
| 3111   | Layout 1             | `1286a536ed20`  |
| 3103   | Layout 1             | `1286a536ed20`  |
| 3095   | Layout 1             | `1286a536ed20`  |
| 3086   | Layout 1             | `1286a536ed20`  |
| 3072   | Layout 1             | `1286a536ed20`  |
| 3062   | Layout 1             | `1286a536ed20`  |
| 3052   | Layout 1             | `1286a536ed20`  |
| 3045   | Layout 1             | `1286a536ed20`  |
| 3037   | Layout 1             | `1286a536ed20`  |
| 3030   | Layout 1             | `1286a536ed20`  |
| 3021   | Layout 1             | `1286a536ed20`  |
| 3012   | Layout 1             | `1286a536ed20`  |
| 3002   | Layout 1             | `1286a536ed20`  |
| 2995   | Layout 1             | `1286a536ed20`  |
| 2987   | Layout 1             | `1286a536ed20`  |
| 2978   | Layout 1             | `1286a536ed20`  |
| 2970   | Layout 1             | `1286a536ed20`  |
| 2959   | Layout 1             | `1286a536ed20`  |
| 2951   | Layout 1             | `1286a536ed20`  |
| 2942   | Layout 1             | `1286a536ed20`  |
| 2935   | Layout 1             | `1286a536ed20`  |
| 2932   | Layout 1             | `1286a536ed20`  |
| 2923   | Layout 1             | `1286a536ed20`  |
| 2919   | Layout 1             | `1286a536ed20`  |
| 2907   | Layout 1             | `1286a536ed20`  |
| 2900   | Layout 1             | `1286a536ed20`  |
| 2891   | Layout 1             | `1286a536ed20`  |
| 2882   | Layout 1             | `1286a536ed20`  |
| 2872   | Layout 1             | `1286a536ed20`  |
| 2863   | Layout 1             | `1286a536ed20`  |
| 2855   | Layout 1             | `1286a536ed20`  |
| 2849   | Layout 1             | `1286a536ed20`  |
| 2844   | Layout 1             | `1286a536ed20`  |
| 2834   | Layout 1             | `1286a536ed20`  |
| 2825   | Layout 1             | `1286a536ed20`  |
| 2819   | Layout 1             | `1286a536ed20`  |
| 2811   | Layout 1             | `1286a536ed20`  |
| 2803   | Layout 1             | `1286a536ed20`  |
| 2794   | Layout 1             | `1286a536ed20`  |
| 2783   | Layout 1             | `1286a536ed20`  |
| 2774   | Layout 1             | `1286a536ed20`  |
| 2765   | Layout 1             | `1286a536ed20`  |
| 2756   | Layout 1             | `1286a536ed20`  |
| 2750   | Layout 1             | `1286a536ed20`  |
| 2743   | Layout 1             | `1286a536ed20`  |
| 2736   | Layout 1             | `1286a536ed20`  |
| 2726   | Layout 1             | `1286a536ed20`  |
| 2717   | Layout 1             | `1286a536ed20`  |
| 2709   | Layout 1             | `1286a536ed20`  |
| 2703   | Layout 1             | `1286a536ed20`  |
| 2695   | Layout 1             | `1286a536ed20`  |
| 2684   | Layout 1             | `1286a536ed20`  |
| 2672   | Layout 1             | `1286a536ed20`  |
| 2665   | Layout 1             | `1286a536ed20`  |
| 2657   | Layout 1             | `1286a536ed20`  |
| 2649   | Layout 1             | `1286a536ed20`  |
| 2644   | Layout 1             | `1286a536ed20`  |
| 2637   | Layout 1             | `1286a536ed20`  |
| 2629   | Layout 1             | `1286a536ed20`  |
| 2619   | Layout 1             | `1286a536ed20`  |
| 2612   | Layout 1             | `1286a536ed20`  |
| 2606   | Layout 1             | `1286a536ed20`  |
| 2602   | Layout 1             | `1286a536ed20`  |
| 2601   | Layout 1             | `1286a536ed20`  |
| 2592   | Layout 1             | `1286a536ed20`  |
| 2583   | Layout 1             | `1286a536ed20`  |
| 2575   | Layout 1             | `1286a536ed20`  |
| 2567   | Layout 1             | `1286a536ed20`  |
| 2560   | Layout 1             | `1286a536ed20`  |
| 2553   | Layout 1             | `1286a536ed20`  |
| 2545   | Layout 1             | `1286a536ed20`  |
| 2538   | Layout 1             | `1286a536ed20`  |
| 2529   | Layout 1             | `1286a536ed20`  |
| 2519   | Layout 1             | `1286a536ed20`  |
| 2513   | Layout 1             | `1286a536ed20`  |
| 2510   | Layout 1             | `1286a536ed20`  |
| 2507   | Layout 1             | `1286a536ed20`  |
| 2503   | Layout 1             | `1286a536ed20`  |
| 2498   | Layout 1             | `1286a536ed20`  |
| 2492   | Layout 1             | `1286a536ed20`  |
| 2487   | Layout 1             | `1286a536ed20`  |
| 2480   | Layout 1             | `1286a536ed20`  |
| 2474   | Layout 1             | `1286a536ed20`  |
| 2468   | Layout 1             | `1286a536ed20`  |
| 2460   | Layout 1             | `1286a536ed20`  |
| 2453   | Layout 1             | `1286a536ed20`  |
| 2444   | Layout 1             | `1286a536ed20`  |
| 2438   | Layout 1             | `1286a536ed20`  |
| 2434   | Layout 1             | `1286a536ed20`  |
| 2429   | Layout 1             | `1286a536ed20`  |
| 2421   | Layout 1             | `1286a536ed20`  |
| 2414   | Layout 1             | `1286a536ed20`  |
| 2407   | Layout 1             | `1286a536ed20`  |
| 2401   | Layout 1             | `1286a536ed20`  |
| 2397   | Layout 1             | `1286a536ed20`  |
| 2393   | Layout 1             | `1286a536ed20`  |
| 2384   | Layout 1             | `1286a536ed20`  |
| 2378   | Layout 1             | `1286a536ed20`  |
| 2372   | Layout 1             | `1286a536ed20`  |
| 2358   | Layout 1             | `1286a536ed20`  |
| 2352   | Layout 1             | `1286a536ed20`  |
| 2347   | Layout 1             | `1286a536ed20`  |
| 2343   | Layout 1             | `1286a536ed20`  |
| 2335   | Layout 1             | `1286a536ed20`  |
| 2327   | Layout 1             | `1286a536ed20`  |
| 2324   | Layout 1             | `1286a536ed20`  |
| 2319   | Layout 1             | `1286a536ed20`  |
| 2313   | Layout 1             | `1286a536ed20`  |
| 2308   | Layout 1             | `1286a536ed20`  |
| 2302   | Layout 1             | `1286a536ed20`  |
| 2295   | Layout 1             | `1286a536ed20`  |
| 2290   | Layout 1             | `1286a536ed20`  |
| 2284   | Layout 1             | `1286a536ed20`  |
| 2276   | Layout 1             | `1286a536ed20`  |
| 2269   | Layout 1             | `1286a536ed20`  |
| 2259   | Layout 1             | `1286a536ed20`  |
| 2250   | Layout 1             | `1286a536ed20`  |
| 2243   | Layout 1             | `1286a536ed20`  |
| 2235   | Layout 1             | `1286a536ed20`  |
| 2229   | Layout 1             | `1286a536ed20`  |
| 2224   | Layout 1             | `1286a536ed20`  |
| 2218   | Layout 1             | `1286a536ed20`  |
| 2215   | Layout 1             | `1286a536ed20`  |
| 2207   | Layout 1             | `1286a536ed20`  |
| 2203   | Layout 1             | `1286a536ed20`  |
| 2196   | Layout 1             | `1286a536ed20`  |
| 2192   | Layout 1             | `1286a536ed20`  |
| 2189   | Layout 1             | `1286a536ed20`  |
| 2183   | Layout 1             | `1286a536ed20`  |
| 2179   | Layout 1             | `1286a536ed20`  |
| 2171   | Layout 1             | `1286a536ed20`  |
| 2163   | Layout 1             | `1286a536ed20`  |
| 2156   | Layout 1             | `1286a536ed20`  |
| 2151   | Layout 1             | `1286a536ed20`  |
| 2147   | Layout 1             | `1286a536ed20`  |
| 2142   | Layout 1             | `1286a536ed20`  |
| 2138   | Layout 1             | `1286a536ed20`  |
| 2134   | Layout 1             | `1286a536ed20`  |
| 2130   | Layout 1             | `1286a536ed20`  |
| 2122   | Layout 1             | `1286a536ed20`  |
| 2107   | Layout 1             | `1286a536ed20`  |
| 2098   | Layout 1             | `1286a536ed20`  |
| 2089   | Layout 1             | `1286a536ed20`  |
| 2081   | Layout 1             | `1286a536ed20`  |
| 2073   | Layout 1             | `1286a536ed20`  |
| 2067   | Layout 1             | `1286a536ed20`  |
| 2063   | Layout 1             | `1286a536ed20`  |
| 2059   | Layout 1             | `1286a536ed20`  |
| 2052   | Layout 1             | `1286a536ed20`  |
| 2044   | Layout 1             | `1286a536ed20`  |
| 2039   | Layout 1             | `1286a536ed20`  |
| 2032   | Layout 1             | `1286a536ed20`  |
| 2025   | Layout 1             | `1286a536ed20`  |
| 2011   | Layout 1             | `1286a536ed20`  |
| 2005   | Layout 1             | `1286a536ed20`  |
| 2000   | Layout 1             | `1286a536ed20`  |
| 1996   | Layout 1             | `1286a536ed20`  |
| 1991   | Layout 1             | `1286a536ed20`  |
| 1985   | Layout 1             | `1286a536ed20`  |
| 1980   | Layout 1             | `1286a536ed20`  |
| 1969   | Layout 1             | `1286a536ed20`  |
| 1964   | Layout 1             | `1286a536ed20`  |
| 1958   | Layout 1             | `1286a536ed20`  |
| 1950   | Layout 1             | `1286a536ed20`  |
| 1945   | Layout 1             | `1286a536ed20`  |
| 1937   | Layout 1             | `1286a536ed20`  |
| 1933   | Layout 1             | `1286a536ed20`  |
| 1927   | Layout 1             | `1286a536ed20`  |
| 1921   | Layout 1             | `1286a536ed20`  |
| 1914   | Layout 1             | `1286a536ed20`  |
| 1908   | Layout 1             | `1286a536ed20`  |
| 1897   | Layout 1             | `1286a536ed20`  |
| 1892   | Layout 1             | `1286a536ed20`  |
| 1886   | Layout 1             | `1286a536ed20`  |
| 1881   | Layout 1             | `1286a536ed20`  |
| 1871   | Layout 1             | `1286a536ed20`  |
| 1866   | Layout 1             | `1286a536ed20`  |
| 1862   | Layout 1             | `1286a536ed20`  |
| 1854   | Layout 1             | `1286a536ed20`  |
| 1846   | Layout 1             | `1286a536ed20`  |
| 1838   | Layout 1             | `1286a536ed20`  |
| 1832   | Layout 1             | `1286a536ed20`  |
| 1826   | Layout 1             | `1286a536ed20`  |
| 1822   | Layout 1             | `1286a536ed20`  |
| 1818   | Layout 1             | `1286a536ed20`  |
| 1804   | Layout 1             | `1286a536ed20`  |
| 1794   | Layout 1             | `1286a536ed20`  |
| 1790   | Layout 1             | `1286a536ed20`  |
| 1784   | Layout 1             | `1286a536ed20`  |
| 1774   | Layout 1             | `1286a536ed20`  |
| 1771   | Layout 1             | `1286a536ed20`  |
| 1762   | Layout 1             | `1286a536ed20`  |
| 1759   | Layout 1             | `1286a536ed20`  |
| 1754   | Layout 1             | `1286a536ed20`  |
| 1749   | Layout 1             | `1286a536ed20`  |
| 1743   | Layout 1             | `1286a536ed20`  |
| 1737   | Layout 1             | `1286a536ed20`  |
| 1731   | Layout 1             | `1286a536ed20`  |
| 1725   | Layout 1             | `1286a536ed20`  |
| 1717   | Layout 1             | `1286a536ed20`  |
| 1710   | Layout 1             | `1286a536ed20`  |
| 1704   | Layout 1             | `1286a536ed20`  |
| 1698   | Layout 1             | `1286a536ed20`  |
| 1690   | Layout 1             | `1286a536ed20`  |
| 1685   | Layout 1             | `1286a536ed20`  |
| 1680   | Layout 1             | `1286a536ed20`  |
| 1674   | Layout 1             | `1286a536ed20`  |
| 1668   | Layout 1             | `1286a536ed20`  |
| 1659   | Layout 1             | `1286a536ed20`  |
| 1649   | Layout 1             | `1286a536ed20`  |
| 1642   | Layout 1             | `1286a536ed20`  |
| 1636   | Layout 1             | `1286a536ed20`  |
| 1628   | Layout 1             | `1286a536ed20`  |
| 1622   | Layout 1             | `1286a536ed20`  |
| 1614   | Layout 1             | `1286a536ed20`  |
| 1608   | Layout 1             | `1286a536ed20`  |
| 1602   | Layout 1             | `1286a536ed20`  |
| 1598   | Layout 1             | `1286a536ed20`  |
| 1594   | Layout 1             | `1286a536ed20`  |
| 1590   | Layout 1             | `1286a536ed20`  |
| 1587   | Layout 1             | `1286a536ed20`  |
| 1584   | Layout 1             | `1286a536ed20`  |
| 1579   | Layout 1             | `1286a536ed20`  |
| 1572   | Layout 1             | `1286a536ed20`  |
| 1565   | Layout 1             | `1286a536ed20`  |
| 1559   | Layout 1             | `1286a536ed20`  |
| 1554   | Layout 1             | `1286a536ed20`  |
| 1547   | Layout 1             | `1286a536ed20`  |
| 1537   | Layout 1             | `1286a536ed20`  |
| 1529   | Layout 1             | `1286a536ed20`  |
| 1524   | Layout 1             | `1286a536ed20`  |
| 1519   | Layout 1             | `1286a536ed20`  |
| 1509   | Layout 1             | `1286a536ed20`  |
| 1506   | Layout 1             | `1286a536ed20`  |
| 1504   | Layout 1             | `1286a536ed20`  |
| 1500   | Layout 1             | `1286a536ed20`  |
| 1493   | Layout 1             | `1286a536ed20`  |
| 1489   | Layout 1             | `1286a536ed20`  |
| 1485   | Layout 1             | `1286a536ed20`  |
| 1481   | Layout 1             | `1286a536ed20`  |
| 1474   | Layout 1             | `1286a536ed20`  |
| 1466   | Layout 1             | `1286a536ed20`  |
| 1462   | Layout 1             | `1286a536ed20`  |
| 1459   | Layout 1             | `1286a536ed20`  |
| 1453   | Layout 1             | `1286a536ed20`  |
| 1450   | Layout 1             | `1286a536ed20`  |
| 1445   | Layout 1             | `1286a536ed20`  |
| 1439   | Layout 1             | `1286a536ed20`  |
| 1433   | Layout 1             | `1286a536ed20`  |
| 1430   | Layout 1             | `1286a536ed20`  |
| 1426   | Layout 1             | `1286a536ed20`  |
| 1421   | Layout 1             | `1286a536ed20`  |
| 1417   | Layout 1             | `1286a536ed20`  |
| 1416   | Layout 1             | `1286a536ed20`  |
| 1409   | Layout 1             | `1286a536ed20`  |
| 1405   | Layout 1             | `1286a536ed20`  |
| 1401   | Layout 1             | `1286a536ed20`  |
| 1396   | Layout 1             | `1286a536ed20`  |
| 1391   | Layout 1             | `1286a536ed20`  |
| 1390   | Layout 1             | `1286a536ed20`  |
| 1386   | Layout 1             | `1286a536ed20`  |
| 1381   | Layout 1             | `1286a536ed20`  |
| 1379   | Layout 1             | `1286a536ed20`  |
| 1372   | Layout 1             | `1286a536ed20`  |
| 1366   | Layout 1             | `1286a536ed20`  |
| 1364   | Layout 1             | `1286a536ed20`  |
| 1363   | Layout 1             | `1286a536ed20`  |
| 1360   | Layout 1             | `1286a536ed20`  |
| 1358   | Layout 1             | `1286a536ed20`  |
| 1355   | Layout 1             | `1286a536ed20`  |
| 1351   | Layout 1             | `1286a536ed20`  |
| 1348   | Layout 1             | `1286a536ed20`  |
| 1346   | Layout 1             | `1286a536ed20`  |
| 1341   | No documented layout | `1286a536ed20`  |
| 1340   | No documented layout | `1286a536ed20`  |
| 1338   | No documented layout | `1286a536ed20`  |
| 1335   | No documented layout | `1286a536ed20`  |
| 1333   | No documented layout | `1286a536ed20`  |
| 1329   | No documented layout | `1286a536ed20`  |
| 1327   | No documented layout | `1286a536ed20`  |
| 1324   | No documented layout | `1286a536ed20`  |
| 1321   | No documented layout | `1286a536ed20`  |
| 1319   | No documented layout | `1286a536ed20`  |
| 1318   | No documented layout | `1286a536ed20`  |
| 1316   | No documented layout | `1286a536ed20`  |
| 1313   | No documented layout | `1286a536ed20`  |
| 1311   | No documented layout | `1286a536ed20`  |
| 1309   | No documented layout | `1286a536ed20`  |
| 1304   | No documented layout | `1286a536ed20`  |
| 1292   | No documented layout | `1286a536ed20`  |
| 1286   | No documented layout | `1286a536ed20`  |
| 1280   | No file              | `1286a536ed20`  |
| 1276   | No file              | `1286a536ed20`  |
| 1267   | No file              | `1286a536ed20`  |
| 1261   | No file              | `1286a536ed20`  |
| 1256   | No file              | `1286a536ed20`  |
| 1250   | No file              | `1286a536ed20`  |
| 1246   | No file              | `1286a536ed20`  |
| 1239   | No file              | `1286a536ed20`  |
| 1230   | No file              | `1286a536ed20`  |
| 1226   | No file              | `1286a536ed20`  |
| 1220   | No file              | `1286a536ed20`  |
| 1217   | No file              | `1286a536ed20`  |
| 1211   | No file              | `1286a536ed20`  |
| 1210   | No file              | `1286a536ed20`  |
| 1208   | No file              | `1286a536ed20`  |
| 1203   | No file              | `1286a536ed20`  |
| 1197   | No file              | `1286a536ed20`  |
| 1194   | No file              | `1286a536ed20`  |
| 1192   | No file              | `1286a536ed20`  |
| 1187   | No file              | `1286a536ed20`  |
| 1183   | No file              | `1286a536ed20`  |
| 1177   | No file              | `1286a536ed20`  |
| 1173   | No file              | `1286a536ed20`  |
| 1167   | No file              | `1286a536ed20`  |
| 1164   | No file              | `1286a536ed20`  |
| 1156   | No file              | `1286a536ed20`  |
| 1149   | No file              | `1286a536ed20`  |
| 1144   | No file              | `1286a536ed20`  |
| 1137   | No file              | `1286a536ed20`  |
| 1132   | No file              | `1286a536ed20`  |
| 1127   | No file              | `1286a536ed20`  |
| 1122   | No file              | `1286a536ed20`  |
| 1118   | No file              | `1286a536ed20`  |
| 1114   | No file              | `1286a536ed20`  |
| 1109   | No file              | `1286a536ed20`  |
| 1102   | No file              | `1286a536ed20`  |
| 1096   | No file              | `1286a536ed20`  |
| 1088   | No file              | `1286a536ed20`  |
| 1081   | No file              | `1286a536ed20`  |
| 1076   | No file              | `1286a536ed20`  |
| 1069   | No file              | `1286a536ed20`  |
| 1064   | No file              | `1286a536ed20`  |
| 1058   | No file              | `1286a536ed20`  |
| 1051   | No file              | `1286a536ed20`  |
| 1044   | No file              | `1286a536ed20`  |
| 1036   | No file              | `1286a536ed20`  |
| 1026   | No file              | `1286a536ed20`  |
| 1016   | No file              | `1286a536ed20`  |
| 1009   | No file              | `1286a536ed20`  |
| 1005   | No file              | `1286a536ed20`  |
| 1000   | No file              | `1286a536ed20`  |
| 998    | No file              | `1286a536ed20`  |
| 990    | No file              | `1286a536ed20`  |
| 979    | No file              | `1286a536ed20`  |
| 972    | No file              | `1286a536ed20`  |
| 963    | No file              | `1286a536ed20`  |
| 955    | No file              | `1286a536ed20`  |
| 946    | No file              | `1286a536ed20`  |
| 938    | No file              | `1286a536ed20`  |
| 927    | No file              | `1286a536ed20`  |
| 911    | No file              | `1286a536ed20`  |
| 904    | No file              | `1286a536ed20`  |
| 899    | No file              | `1286a536ed20`  |
| 894    | No file              | `1286a536ed20`  |
| 885    | No file              | `1286a536ed20`  |
| 879    | No file              | `1286a536ed20`  |
| 872    | No file              | `1286a536ed20`  |
| 864    | No file              | `1286a536ed20`  |
| 855    | No file              | `1286a536ed20`  |
| 853    | No file              | `1286a536ed20`  |
| 845    | No file              | `1286a536ed20`  |
| 837    | No file              | `1286a536ed20`  |
| 829    | No file              | `1286a536ed20`  |
| 822    | No file              | `1286a536ed20`  |
| 814    | No file              | `1286a536ed20`  |
| 805    | No file              | `1286a536ed20`  |
| 794    | No file              | `1286a536ed20`  |
| 787    | No file              | `1286a536ed20`  |
| 780    | No file              | `1286a536ed20`  |
| 771    | No file              | `1286a536ed20`  |
| 760    | No file              | `1286a536ed20`  |
| 748    | No file              | `1286a536ed20`  |
| 741    | No file              | `1286a536ed20`  |
| 736    | No file              | `1286a536ed20`  |
| 731    | No file              | `1286a536ed20`  |
| 723    | No file              | `1286a536ed20`  |
| 711    | No file              | `1286a536ed20`  |
| 707    | No file              | `1286a536ed20`  |
| 697    | No file              | `1286a536ed20`  |
| 689    | No file              | `1286a536ed20`  |
| 683    | No file              | `1286a536ed20`  |
| 678    | No file              | `1286a536ed20`  |
| 670    | No file              | `1286a536ed20`  |
| 661    | No file              | `1286a536ed20`  |
| 656    | No file              | `1286a536ed20`  |
| 652    | No file              | `1286a536ed20`  |
| 643    | No file              | `1286a536ed20`  |
| 637    | No file              | `1286a536ed20`  |
| 630    | No file              | `1286a536ed20`  |
| 627    | No file              | `1286a536ed20`  |
| 621    | No file              | `1286a536ed20`  |
| 617    | No file              | `1286a536ed20`  |
| 615    | No file              | `1286a536ed20`  |
| 606    | No file              | `1286a536ed20`  |
| 599    | No file              | `1286a536ed20`  |
| 592    | No file              | `1286a536ed20`  |
| 586    | No file              | `1286a536ed20`  |
| 577    | No file              | `1286a536ed20`  |
| 569    | No file              | `1286a536ed20`  |
| 561    | No file              | `1286a536ed20`  |
| 554    | No file              | `1286a536ed20`  |
| 542    | No file              | `1286a536ed20`  |
| 532    | No file              | `1286a536ed20`  |
| 531    | No file              | `1286a536ed20`  |
| 526    | No file              | `1286a536ed20`  |
| 521    | No file              | `1286a536ed20`  |
| 517    | No file              | `1286a536ed20`  |
| 510    | No file              | `1286a536ed20`  |
| 508    | No file              | `1286a536ed20`  |
| 504    | No file              | `1286a536ed20`  |
| 497    | No file              | `1286a536ed20`  |
| 491    | No file              | `1286a536ed20`  |
| 485    | No file              | `1286a536ed20`  |
| 478    | No file              | `1286a536ed20`  |
| 472    | No file              | `1286a536ed20`  |
| 466    | No file              | `1286a536ed20`  |
| 457    | No file              | `1286a536ed20`  |
| 452    | No file              | `1286a536ed20`  |
| 449    | No file              | `1286a536ed20`  |
| 435    | No file              | `1286a536ed20`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                        |
| --------------------- | -------- | ------------------------------------------- |
| `languagedata_en.loc` | Optional | NPC names (6), item names (0)               |

`npcgiftoffset.dbss` is the ID-keyed index into this file (below).
`npcgiftetc.bss` holds the global gift-system values, see
[npcgiftetc_bss.md](npcgiftetc_bss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field   | Notes                                     |
| ------- | ------------------ | ------- | ----------------------------------------- |
| `+0x00` | u32                | count   | Number of NPC gift records (observed: 24) |
| `+0x04` | Gift Record[count] | records | See Gift Record                           |

### Gift Record (variable: 6 bytes + gift rows)

| Offset  | Type                 | Field      | Notes                            |
| ------- | -------------------- | ---------- | -------------------------------- |
| `+0x00` | u16                  | npc_id     | NPC key                          |
| `+0x02` | u32                  | gift_count | Number of gift rows              |
| `+0x06` | Gift Row[gift_count] | gifts      | `gift_count` rows, 12 bytes each |

Observed `gift_count` values: in the pre-2026-09-27 fixture 23 records have 5 rows and NPC 41002 has 4 (119 gift rows); in the 2026-09-27 client 22 have 5, NPC 43408 has 4 and NPC 41002 has 3 (117 gift rows). The companion `data_size` equals `4 + gift_count * 12`.

### Gift Row (12 bytes)

| Offset  | Type | Field   | Notes                                                              |
| ------- | ---- | ------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_id | Gift item ID; matches item LOC type 0 names                        |
| `+0x04` | u32  | amity_a | Amity gained by giving this item                                   |
| `+0x08` | u32  | amity_b | Duplicate Amity value; equal to `amity_a` on every observed row (119 pre-2026-09-27, 117 in the 2026-09-27 client) |

### `npcgiftoffset.dbss`

| Offset  | Type                 | Field   | Notes                                     |
| ------- | -------------------- | ------- | ----------------------------------------- |
| `+0x00` | u32                  | count   | Number of NPC gift records (observed: 24) |
| `+0x04` | Offset Record[count] | records | See Offset Record                         |

### Offset Record (10 bytes)

| Offset  | Type | Field       | Notes                                                                 |
| ------- | ---- | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | npc_id      | NPC key; matches the record's leading `npc_id`                        |
| `+0x02` | u32  | data_offset | Byte offset into `npcgift.dbss`; points 2 bytes past the record start |
| `+0x06` | u16  | data_size   | Byte count after the leading `npc_id`                                 |
| `+0x08` | u16  | unknown_08  | Observed: 0                                                           |

`record_start = data_offset - 2`

## Notes

- `npcgift.dbss` and [`npcgiftdata.dbss`](npcgiftdata_dbss.md) share the same 24 NPC IDs and offset record order, but the main records are not stored in ID-sorted order.
- `item_id` is ambiguous across LOC types; use str_type=0 for item display names, not str_type=34 knowledge names.
- Example: NPC 40012 (Crio) accepts item 7023, which resolves via str_type=0 to "Haystack" and via str_type=34 to "Omelet". Use str_type=0 for gift item names.
- `npc_id` resolves via LOC str_type=32, str_id4=29 for the "Give Gift" interaction label.
