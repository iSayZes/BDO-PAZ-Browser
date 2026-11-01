# `petdetectposition.dbss` Format

## Purpose

The world positions behind the pet Location Find skill (`skill_type` `4`,
`ePetSkill_DetectPosition`, in [`petskill.dbss`](petskill_dbss.md)): each
row is a position key, a world position and a position type. In the client
files every position reads `0, 0, 0`: the position columns are server-only in
the source sheet. Companion
`petdetectpositionoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                           | Bytes | Records      | Row bytes |
| ------ | -------------- | ------------------------------ | ----- | ------------ | --------- |
| 1      | 1261 and later | `petdetectposition.dbss`       | 64    | 4 Row        | 15        |
| 1      | 1261 and later | `petdetectpositionoffset.dbss` | 44    | 4 Offset Row | 10        |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `petdetectposition.dbss`       | 64 B (100.0%) | 0 B (0.0%) |
| 1      | `petdetectpositionoffset.dbss` | 44 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `da78907a3620`  |
| 3482   | Layout 1 | `da78907a3620`  |
| 3474   | Layout 1 | `da78907a3620`  |
| 3473   | Layout 1 | `da78907a3620`  |
| 3464   | Layout 1 | `da78907a3620`  |
| 3458   | Layout 1 | `da78907a3620`  |
| 3454   | Layout 1 | `da78907a3620`  |
| 3444   | Layout 1 | `da78907a3620`  |
| 3435   | Layout 1 | `da78907a3620`  |
| 3426   | Layout 1 | `da78907a3620`  |
| 3418   | Layout 1 | `da78907a3620`  |
| 3412   | Layout 1 | `da78907a3620`  |
| 3402   | Layout 1 | `da78907a3620`  |
| 3396   | Layout 1 | `da78907a3620`  |
| 3387   | Layout 1 | `da78907a3620`  |
| 3381   | Layout 1 | `da78907a3620`  |
| 3373   | Layout 1 | `da78907a3620`  |
| 3364   | Layout 1 | `da78907a3620`  |
| 3356   | Layout 1 | `da78907a3620`  |
| 3349   | Layout 1 | `da78907a3620`  |
| 3342   | Layout 1 | `da78907a3620`  |
| 3335   | Layout 1 | `da78907a3620`  |
| 3326   | Layout 1 | `da78907a3620`  |
| 3321   | Layout 1 | `da78907a3620`  |
| 3314   | Layout 1 | `da78907a3620`  |
| 3303   | Layout 1 | `da78907a3620`  |
| 3302   | Layout 1 | `da78907a3620`  |
| 3293   | Layout 1 | `da78907a3620`  |
| 3283   | Layout 1 | `da78907a3620`  |
| 3275   | Layout 1 | `da78907a3620`  |
| 3267   | Layout 1 | `da78907a3620`  |
| 3258   | Layout 1 | `da78907a3620`  |
| 3251   | Layout 1 | `da78907a3620`  |
| 3242   | Layout 1 | `da78907a3620`  |
| 3235   | Layout 1 | `da78907a3620`  |
| 3229   | Layout 1 | `da78907a3620`  |
| 3212   | Layout 1 | `da78907a3620`  |
| 3203   | Layout 1 | `da78907a3620`  |
| 3193   | Layout 1 | `da78907a3620`  |
| 3186   | Layout 1 | `da78907a3620`  |
| 3177   | Layout 1 | `da78907a3620`  |
| 3169   | Layout 1 | `da78907a3620`  |
| 3158   | Layout 1 | `da78907a3620`  |
| 3151   | Layout 1 | `da78907a3620`  |
| 3144   | Layout 1 | `da78907a3620`  |
| 3133   | Layout 1 | `da78907a3620`  |
| 3125   | Layout 1 | `da78907a3620`  |
| 3118   | Layout 1 | `da78907a3620`  |
| 3111   | Layout 1 | `da78907a3620`  |
| 3103   | Layout 1 | `da78907a3620`  |
| 3095   | Layout 1 | `da78907a3620`  |
| 3086   | Layout 1 | `da78907a3620`  |
| 3072   | Layout 1 | `da78907a3620`  |
| 3062   | Layout 1 | `da78907a3620`  |
| 3052   | Layout 1 | `da78907a3620`  |
| 3045   | Layout 1 | `da78907a3620`  |
| 3037   | Layout 1 | `da78907a3620`  |
| 3030   | Layout 1 | `da78907a3620`  |
| 3021   | Layout 1 | `da78907a3620`  |
| 3012   | Layout 1 | `da78907a3620`  |
| 3002   | Layout 1 | `da78907a3620`  |
| 2995   | Layout 1 | `da78907a3620`  |
| 2987   | Layout 1 | `da78907a3620`  |
| 2978   | Layout 1 | `da78907a3620`  |
| 2970   | Layout 1 | `da78907a3620`  |
| 2959   | Layout 1 | `da78907a3620`  |
| 2951   | Layout 1 | `da78907a3620`  |
| 2942   | Layout 1 | `da78907a3620`  |
| 2935   | Layout 1 | `da78907a3620`  |
| 2932   | Layout 1 | `da78907a3620`  |
| 2923   | Layout 1 | `da78907a3620`  |
| 2919   | Layout 1 | `da78907a3620`  |
| 2907   | Layout 1 | `da78907a3620`  |
| 2900   | Layout 1 | `da78907a3620`  |
| 2891   | Layout 1 | `da78907a3620`  |
| 2882   | Layout 1 | `da78907a3620`  |
| 2872   | Layout 1 | `da78907a3620`  |
| 2863   | Layout 1 | `da78907a3620`  |
| 2855   | Layout 1 | `da78907a3620`  |
| 2849   | Layout 1 | `da78907a3620`  |
| 2844   | Layout 1 | `da78907a3620`  |
| 2834   | Layout 1 | `da78907a3620`  |
| 2825   | Layout 1 | `da78907a3620`  |
| 2819   | Layout 1 | `da78907a3620`  |
| 2811   | Layout 1 | `da78907a3620`  |
| 2803   | Layout 1 | `da78907a3620`  |
| 2794   | Layout 1 | `da78907a3620`  |
| 2783   | Layout 1 | `da78907a3620`  |
| 2774   | Layout 1 | `da78907a3620`  |
| 2765   | Layout 1 | `da78907a3620`  |
| 2756   | Layout 1 | `da78907a3620`  |
| 2750   | Layout 1 | `da78907a3620`  |
| 2743   | Layout 1 | `da78907a3620`  |
| 2736   | Layout 1 | `da78907a3620`  |
| 2726   | Layout 1 | `da78907a3620`  |
| 2717   | Layout 1 | `da78907a3620`  |
| 2709   | Layout 1 | `da78907a3620`  |
| 2703   | Layout 1 | `da78907a3620`  |
| 2695   | Layout 1 | `da78907a3620`  |
| 2684   | Layout 1 | `da78907a3620`  |
| 2672   | Layout 1 | `da78907a3620`  |
| 2665   | Layout 1 | `da78907a3620`  |
| 2657   | Layout 1 | `da78907a3620`  |
| 2649   | Layout 1 | `da78907a3620`  |
| 2644   | Layout 1 | `da78907a3620`  |
| 2637   | Layout 1 | `da78907a3620`  |
| 2629   | Layout 1 | `da78907a3620`  |
| 2619   | Layout 1 | `da78907a3620`  |
| 2612   | Layout 1 | `da78907a3620`  |
| 2606   | Layout 1 | `da78907a3620`  |
| 2602   | Layout 1 | `da78907a3620`  |
| 2601   | Layout 1 | `da78907a3620`  |
| 2592   | Layout 1 | `da78907a3620`  |
| 2583   | Layout 1 | `da78907a3620`  |
| 2575   | Layout 1 | `da78907a3620`  |
| 2567   | Layout 1 | `da78907a3620`  |
| 2560   | Layout 1 | `da78907a3620`  |
| 2553   | Layout 1 | `da78907a3620`  |
| 2545   | Layout 1 | `da78907a3620`  |
| 2538   | Layout 1 | `da78907a3620`  |
| 2529   | Layout 1 | `da78907a3620`  |
| 2519   | Layout 1 | `da78907a3620`  |
| 2513   | Layout 1 | `da78907a3620`  |
| 2510   | Layout 1 | `da78907a3620`  |
| 2507   | Layout 1 | `da78907a3620`  |
| 2503   | Layout 1 | `da78907a3620`  |
| 2498   | Layout 1 | `da78907a3620`  |
| 2492   | Layout 1 | `da78907a3620`  |
| 2487   | Layout 1 | `da78907a3620`  |
| 2480   | Layout 1 | `da78907a3620`  |
| 2474   | Layout 1 | `da78907a3620`  |
| 2468   | Layout 1 | `da78907a3620`  |
| 2460   | Layout 1 | `da78907a3620`  |
| 2453   | Layout 1 | `da78907a3620`  |
| 2444   | Layout 1 | `da78907a3620`  |
| 2438   | Layout 1 | `da78907a3620`  |
| 2434   | Layout 1 | `da78907a3620`  |
| 2429   | Layout 1 | `da78907a3620`  |
| 2421   | Layout 1 | `da78907a3620`  |
| 2414   | Layout 1 | `da78907a3620`  |
| 2407   | Layout 1 | `da78907a3620`  |
| 2401   | Layout 1 | `da78907a3620`  |
| 2397   | Layout 1 | `da78907a3620`  |
| 2393   | Layout 1 | `da78907a3620`  |
| 2384   | Layout 1 | `da78907a3620`  |
| 2378   | Layout 1 | `da78907a3620`  |
| 2372   | Layout 1 | `da78907a3620`  |
| 2358   | Layout 1 | `da78907a3620`  |
| 2352   | Layout 1 | `da78907a3620`  |
| 2347   | Layout 1 | `da78907a3620`  |
| 2343   | Layout 1 | `da78907a3620`  |
| 2335   | Layout 1 | `da78907a3620`  |
| 2327   | Layout 1 | `da78907a3620`  |
| 2324   | Layout 1 | `da78907a3620`  |
| 2319   | Layout 1 | `da78907a3620`  |
| 2313   | Layout 1 | `da78907a3620`  |
| 2308   | Layout 1 | `da78907a3620`  |
| 2302   | Layout 1 | `da78907a3620`  |
| 2295   | Layout 1 | `da78907a3620`  |
| 2290   | Layout 1 | `da78907a3620`  |
| 2284   | Layout 1 | `da78907a3620`  |
| 2276   | Layout 1 | `da78907a3620`  |
| 2269   | Layout 1 | `da78907a3620`  |
| 2259   | Layout 1 | `da78907a3620`  |
| 2250   | Layout 1 | `da78907a3620`  |
| 2243   | Layout 1 | `da78907a3620`  |
| 2235   | Layout 1 | `da78907a3620`  |
| 2229   | Layout 1 | `da78907a3620`  |
| 2224   | Layout 1 | `da78907a3620`  |
| 2218   | Layout 1 | `da78907a3620`  |
| 2215   | Layout 1 | `da78907a3620`  |
| 2207   | Layout 1 | `da78907a3620`  |
| 2203   | Layout 1 | `da78907a3620`  |
| 2196   | Layout 1 | `da78907a3620`  |
| 2192   | Layout 1 | `da78907a3620`  |
| 2189   | Layout 1 | `da78907a3620`  |
| 2183   | Layout 1 | `da78907a3620`  |
| 2179   | Layout 1 | `da78907a3620`  |
| 2171   | Layout 1 | `da78907a3620`  |
| 2163   | Layout 1 | `da78907a3620`  |
| 2156   | Layout 1 | `da78907a3620`  |
| 2151   | Layout 1 | `da78907a3620`  |
| 2147   | Layout 1 | `da78907a3620`  |
| 2142   | Layout 1 | `da78907a3620`  |
| 2138   | Layout 1 | `da78907a3620`  |
| 2134   | Layout 1 | `da78907a3620`  |
| 2130   | Layout 1 | `da78907a3620`  |
| 2122   | Layout 1 | `da78907a3620`  |
| 2107   | Layout 1 | `da78907a3620`  |
| 2098   | Layout 1 | `da78907a3620`  |
| 2089   | Layout 1 | `da78907a3620`  |
| 2081   | Layout 1 | `da78907a3620`  |
| 2073   | Layout 1 | `da78907a3620`  |
| 2067   | Layout 1 | `da78907a3620`  |
| 2063   | Layout 1 | `da78907a3620`  |
| 2059   | Layout 1 | `da78907a3620`  |
| 2052   | Layout 1 | `da78907a3620`  |
| 2044   | Layout 1 | `da78907a3620`  |
| 2039   | Layout 1 | `da78907a3620`  |
| 2032   | Layout 1 | `da78907a3620`  |
| 2025   | Layout 1 | `da78907a3620`  |
| 2011   | Layout 1 | `da78907a3620`  |
| 2005   | Layout 1 | `da78907a3620`  |
| 2000   | Layout 1 | `da78907a3620`  |
| 1996   | Layout 1 | `da78907a3620`  |
| 1991   | Layout 1 | `da78907a3620`  |
| 1985   | Layout 1 | `da78907a3620`  |
| 1980   | Layout 1 | `da78907a3620`  |
| 1969   | Layout 1 | `da78907a3620`  |
| 1964   | Layout 1 | `da78907a3620`  |
| 1958   | Layout 1 | `da78907a3620`  |
| 1950   | Layout 1 | `da78907a3620`  |
| 1945   | Layout 1 | `da78907a3620`  |
| 1937   | Layout 1 | `da78907a3620`  |
| 1933   | Layout 1 | `da78907a3620`  |
| 1927   | Layout 1 | `da78907a3620`  |
| 1921   | Layout 1 | `da78907a3620`  |
| 1914   | Layout 1 | `da78907a3620`  |
| 1908   | Layout 1 | `da78907a3620`  |
| 1897   | Layout 1 | `da78907a3620`  |
| 1892   | Layout 1 | `da78907a3620`  |
| 1886   | Layout 1 | `da78907a3620`  |
| 1881   | Layout 1 | `da78907a3620`  |
| 1871   | Layout 1 | `da78907a3620`  |
| 1866   | Layout 1 | `da78907a3620`  |
| 1862   | Layout 1 | `da78907a3620`  |
| 1854   | Layout 1 | `da78907a3620`  |
| 1846   | Layout 1 | `da78907a3620`  |
| 1838   | Layout 1 | `da78907a3620`  |
| 1832   | Layout 1 | `da78907a3620`  |
| 1826   | Layout 1 | `da78907a3620`  |
| 1822   | Layout 1 | `da78907a3620`  |
| 1818   | Layout 1 | `da78907a3620`  |
| 1804   | Layout 1 | `da78907a3620`  |
| 1794   | Layout 1 | `da78907a3620`  |
| 1790   | Layout 1 | `da78907a3620`  |
| 1784   | Layout 1 | `da78907a3620`  |
| 1774   | Layout 1 | `da78907a3620`  |
| 1771   | Layout 1 | `da78907a3620`  |
| 1762   | Layout 1 | `da78907a3620`  |
| 1759   | Layout 1 | `da78907a3620`  |
| 1754   | Layout 1 | `da78907a3620`  |
| 1749   | Layout 1 | `da78907a3620`  |
| 1743   | Layout 1 | `da78907a3620`  |
| 1737   | Layout 1 | `da78907a3620`  |
| 1731   | Layout 1 | `da78907a3620`  |
| 1725   | Layout 1 | `da78907a3620`  |
| 1717   | Layout 1 | `da78907a3620`  |
| 1710   | Layout 1 | `da78907a3620`  |
| 1704   | Layout 1 | `da78907a3620`  |
| 1698   | Layout 1 | `da78907a3620`  |
| 1690   | Layout 1 | `da78907a3620`  |
| 1685   | Layout 1 | `da78907a3620`  |
| 1680   | Layout 1 | `da78907a3620`  |
| 1674   | Layout 1 | `da78907a3620`  |
| 1668   | Layout 1 | `da78907a3620`  |
| 1659   | Layout 1 | `da78907a3620`  |
| 1649   | Layout 1 | `da78907a3620`  |
| 1642   | Layout 1 | `da78907a3620`  |
| 1636   | Layout 1 | `da78907a3620`  |
| 1628   | Layout 1 | `da78907a3620`  |
| 1622   | Layout 1 | `da78907a3620`  |
| 1614   | Layout 1 | `da78907a3620`  |
| 1608   | Layout 1 | `da78907a3620`  |
| 1602   | Layout 1 | `da78907a3620`  |
| 1598   | Layout 1 | `da78907a3620`  |
| 1594   | Layout 1 | `da78907a3620`  |
| 1590   | Layout 1 | `da78907a3620`  |
| 1587   | Layout 1 | `da78907a3620`  |
| 1584   | Layout 1 | `da78907a3620`  |
| 1579   | Layout 1 | `da78907a3620`  |
| 1572   | Layout 1 | `da78907a3620`  |
| 1565   | Layout 1 | `da78907a3620`  |
| 1559   | Layout 1 | `da78907a3620`  |
| 1554   | Layout 1 | `da78907a3620`  |
| 1547   | Layout 1 | `da78907a3620`  |
| 1537   | Layout 1 | `da78907a3620`  |
| 1529   | Layout 1 | `da78907a3620`  |
| 1524   | Layout 1 | `da78907a3620`  |
| 1519   | Layout 1 | `da78907a3620`  |
| 1509   | Layout 1 | `da78907a3620`  |
| 1506   | Layout 1 | `da78907a3620`  |
| 1504   | Layout 1 | `da78907a3620`  |
| 1500   | Layout 1 | `da78907a3620`  |
| 1493   | Layout 1 | `da78907a3620`  |
| 1489   | Layout 1 | `da78907a3620`  |
| 1485   | Layout 1 | `da78907a3620`  |
| 1481   | Layout 1 | `da78907a3620`  |
| 1474   | Layout 1 | `da78907a3620`  |
| 1466   | Layout 1 | `da78907a3620`  |
| 1462   | Layout 1 | `da78907a3620`  |
| 1459   | Layout 1 | `da78907a3620`  |
| 1453   | Layout 1 | `da78907a3620`  |
| 1450   | Layout 1 | `da78907a3620`  |
| 1445   | Layout 1 | `da78907a3620`  |
| 1439   | Layout 1 | `da78907a3620`  |
| 1433   | Layout 1 | `da78907a3620`  |
| 1430   | Layout 1 | `da78907a3620`  |
| 1426   | Layout 1 | `da78907a3620`  |
| 1421   | Layout 1 | `da78907a3620`  |
| 1417   | Layout 1 | `da78907a3620`  |
| 1416   | Layout 1 | `da78907a3620`  |
| 1409   | Layout 1 | `da78907a3620`  |
| 1405   | Layout 1 | `da78907a3620`  |
| 1401   | Layout 1 | `da78907a3620`  |
| 1396   | Layout 1 | `da78907a3620`  |
| 1391   | Layout 1 | `da78907a3620`  |
| 1390   | Layout 1 | `da78907a3620`  |
| 1386   | Layout 1 | `da78907a3620`  |
| 1381   | Layout 1 | `da78907a3620`  |
| 1379   | Layout 1 | `da78907a3620`  |
| 1372   | Layout 1 | `da78907a3620`  |
| 1366   | Layout 1 | `da78907a3620`  |
| 1364   | Layout 1 | `da78907a3620`  |
| 1363   | Layout 1 | `da78907a3620`  |
| 1360   | Layout 1 | `da78907a3620`  |
| 1358   | Layout 1 | `da78907a3620`  |
| 1355   | Layout 1 | `da78907a3620`  |
| 1351   | Layout 1 | `da78907a3620`  |
| 1348   | Layout 1 | `da78907a3620`  |
| 1346   | Layout 1 | `da78907a3620`  |
| 1341   | Layout 1 | `da78907a3620`  |
| 1340   | Layout 1 | `da78907a3620`  |
| 1338   | Layout 1 | `da78907a3620`  |
| 1335   | Layout 1 | `da78907a3620`  |
| 1333   | Layout 1 | `da78907a3620`  |
| 1329   | Layout 1 | `da78907a3620`  |
| 1327   | Layout 1 | `da78907a3620`  |
| 1324   | Layout 1 | `da78907a3620`  |
| 1321   | Layout 1 | `da78907a3620`  |
| 1319   | Layout 1 | `da78907a3620`  |
| 1318   | Layout 1 | `da78907a3620`  |
| 1316   | Layout 1 | `da78907a3620`  |
| 1313   | Layout 1 | `da78907a3620`  |
| 1311   | Layout 1 | `da78907a3620`  |
| 1309   | Layout 1 | `da78907a3620`  |
| 1304   | Layout 1 | `da78907a3620`  |
| 1292   | Layout 1 | `da78907a3620`  |
| 1286   | Layout 1 | `da78907a3620`  |
| 1280   | No file  | `da78907a3620`  |
| 1276   | No file  | `da78907a3620`  |
| 1267   | Layout 1 | `da78907a3620`  |
| 1261   | Layout 1 | `da78907a3620`  |
| 1256   | No file  | `da78907a3620`  |
| 1250   | No file  | `da78907a3620`  |
| 1246   | No file  | `da78907a3620`  |
| 1239   | No file  | `da78907a3620`  |
| 1230   | No file  | `da78907a3620`  |
| 1226   | No file  | `da78907a3620`  |
| 1220   | No file  | `da78907a3620`  |
| 1217   | No file  | `da78907a3620`  |
| 1211   | No file  | `da78907a3620`  |
| 1210   | No file  | `da78907a3620`  |
| 1208   | No file  | `da78907a3620`  |
| 1203   | No file  | `da78907a3620`  |
| 1197   | No file  | `da78907a3620`  |
| 1194   | No file  | `da78907a3620`  |
| 1192   | No file  | `da78907a3620`  |
| 1187   | No file  | `da78907a3620`  |
| 1183   | No file  | `da78907a3620`  |
| 1177   | No file  | `da78907a3620`  |
| 1173   | No file  | `da78907a3620`  |
| 1167   | No file  | `da78907a3620`  |
| 1164   | No file  | `da78907a3620`  |
| 1156   | No file  | `da78907a3620`  |
| 1149   | No file  | `da78907a3620`  |
| 1144   | No file  | `da78907a3620`  |
| 1137   | No file  | `da78907a3620`  |
| 1132   | No file  | `da78907a3620`  |
| 1127   | No file  | `da78907a3620`  |
| 1122   | No file  | `da78907a3620`  |
| 1118   | No file  | `da78907a3620`  |
| 1114   | No file  | `da78907a3620`  |
| 1109   | No file  | `da78907a3620`  |
| 1102   | No file  | `da78907a3620`  |
| 1096   | No file  | `da78907a3620`  |
| 1088   | No file  | `da78907a3620`  |
| 1081   | No file  | `da78907a3620`  |
| 1076   | No file  | `da78907a3620`  |
| 1069   | No file  | `da78907a3620`  |
| 1064   | No file  | `da78907a3620`  |
| 1058   | No file  | `da78907a3620`  |
| 1051   | No file  | `da78907a3620`  |
| 1044   | No file  | `da78907a3620`  |
| 1036   | No file  | `da78907a3620`  |
| 1026   | No file  | `da78907a3620`  |
| 1016   | No file  | `da78907a3620`  |
| 1009   | No file  | `da78907a3620`  |
| 1005   | No file  | `da78907a3620`  |
| 1000   | No file  | `da78907a3620`  |
| 998    | No file  | `da78907a3620`  |
| 990    | No file  | `da78907a3620`  |
| 979    | No file  | `da78907a3620`  |
| 972    | No file  | `da78907a3620`  |
| 963    | No file  | `da78907a3620`  |
| 955    | No file  | `da78907a3620`  |
| 946    | No file  | `da78907a3620`  |
| 938    | No file  | `da78907a3620`  |
| 927    | No file  | `da78907a3620`  |
| 911    | No file  | `da78907a3620`  |
| 904    | No file  | `da78907a3620`  |
| 899    | No file  | `da78907a3620`  |
| 894    | No file  | `da78907a3620`  |
| 885    | No file  | `da78907a3620`  |
| 879    | No file  | `da78907a3620`  |
| 872    | No file  | `da78907a3620`  |
| 864    | No file  | `da78907a3620`  |
| 855    | No file  | `da78907a3620`  |
| 853    | No file  | `da78907a3620`  |
| 845    | No file  | `da78907a3620`  |
| 837    | No file  | `da78907a3620`  |
| 829    | No file  | `da78907a3620`  |
| 822    | No file  | `da78907a3620`  |
| 814    | No file  | `da78907a3620`  |
| 805    | No file  | `da78907a3620`  |
| 794    | No file  | `da78907a3620`  |
| 787    | No file  | `da78907a3620`  |
| 780    | No file  | `da78907a3620`  |
| 771    | No file  | `da78907a3620`  |
| 760    | No file  | `da78907a3620`  |
| 748    | No file  | `da78907a3620`  |
| 741    | No file  | `da78907a3620`  |
| 736    | No file  | `da78907a3620`  |
| 731    | No file  | `da78907a3620`  |
| 723    | No file  | `da78907a3620`  |
| 711    | No file  | `da78907a3620`  |
| 707    | No file  | `da78907a3620`  |
| 697    | No file  | `da78907a3620`  |
| 689    | No file  | `da78907a3620`  |
| 683    | No file  | `da78907a3620`  |
| 678    | No file  | `da78907a3620`  |
| 670    | No file  | `da78907a3620`  |
| 661    | No file  | `da78907a3620`  |
| 656    | No file  | `da78907a3620`  |
| 652    | No file  | `da78907a3620`  |
| 643    | No file  | `da78907a3620`  |
| 637    | No file  | `da78907a3620`  |
| 630    | No file  | `da78907a3620`  |
| 627    | No file  | `da78907a3620`  |
| 621    | No file  | `da78907a3620`  |
| 617    | No file  | `da78907a3620`  |
| 615    | No file  | `da78907a3620`  |
| 606    | No file  | `da78907a3620`  |
| 599    | No file  | `da78907a3620`  |
| 592    | No file  | `da78907a3620`  |
| 586    | No file  | `da78907a3620`  |
| 577    | No file  | `da78907a3620`  |
| 569    | No file  | `da78907a3620`  |
| 561    | No file  | `da78907a3620`  |
| 554    | No file  | `da78907a3620`  |
| 542    | No file  | `da78907a3620`  |
| 532    | No file  | `da78907a3620`  |
| 531    | No file  | `da78907a3620`  |
| 526    | No file  | `da78907a3620`  |
| 521    | No file  | `da78907a3620`  |
| 517    | No file  | `da78907a3620`  |
| 510    | No file  | `da78907a3620`  |
| 508    | No file  | `da78907a3620`  |
| 504    | No file  | `da78907a3620`  |
| 497    | No file  | `da78907a3620`  |
| 491    | No file  | `da78907a3620`  |
| 485    | No file  | `da78907a3620`  |
| 478    | No file  | `da78907a3620`  |
| 472    | No file  | `da78907a3620`  |
| 466    | No file  | `da78907a3620`  |
| 457    | No file  | `da78907a3620`  |
| 452    | No file  | `da78907a3620`  |
| 449    | No file  | `da78907a3620`  |
| 435    | No file  | `da78907a3620`  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                      |
| ------------------------------ | -------- | --------------------------------------------------------- |
| `petdetectpositionoffset.dbss` | Optional | `pet_detect_position_key -> (offset, size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 4 x 15 = 64 bytes on client 3474.

### Row (15 bytes)

| Offset  | Type | Field                    | Notes                                                        |
| ------- | ---- | ------------------------ | ------------------------------------------------------------ |
| `+0x00` | u16  | pet_detect_position_key  | Row key; `1` to `4` (client 3474)                            |
| `+0x02` | f32  | pos_x                    | World X; `0` on every row, see Field Names                   |
| `+0x06` | f32  | pos_y                    | World Y (height); `0` on every row                           |
| `+0x0A` | f32  | pos_z                    | World Z; `0` on every row                                    |
| `+0x0E` | u8   | pet_detect_position_type | `gc::PetDetectPositionType`; `0` (`None`) on every row        |

The rows have no padding: the 2016 struct is 20 bytes in memory with 2
bytes of padding after the key and 3 after the type byte, and the file packs
its members back to back.

### `petdetectpositionoffset.dbss`

Bare offset table into `petdetectposition.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                      |
| ------- | ----------------- | ----- | ------------------------------------------ |
| `+0x00` | u32               | count | Equals the `petdetectposition.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                             |

### Offset Row (10 bytes)

| Offset  | Type | Field                   | Notes                                                       |
| ------- | ---- | ----------------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | pet_detect_position_key | Key of the row it points at                                 |
| `+0x02` | u32  | offset                  | Absolute byte offset of the row in `petdetectposition.dbss`, at its `pet_detect_position_key` |
| `+0x06` | u32  | size                    | The whole row: always `15`                                  |

Both files list the keys in descending order, 4, 3, 2, 1. The offset
points at the row's own key; the rows of
[`guildboss.dbss`](guildboss_dbss.md) and [`petexp.dbss`](petexp_dbss.md)
start with a key copy that their offsets skip.

## Pet Detect Position Type

`pet_detect_position_type` is the 2016 enum `gc::PetDetectPositionType`
(`unsigned char`):

| Value | Name                           |
| ----: | ------------------------------ |
| 0     | `ePetDetectPositionType_None`  |
| 1     | `ePetDetectPositionType_Count` |

`Count` is the enum's end marker, so `None` is the only real value.

## Field Names

The 2016 client's debug symbols hold `gc::PetDetectPositionStaticStatus`
(20 bytes), keyed by a `KeyType<unsigned short>`, with the members
`_petDetectPositionKey` (u16 at `+0x00`), `_petDetectPosition` (a
`pa::float3` of `x`, `y`, `z` at `+0x04`) and `_petDetectPositionType`
(`gc::PetDetectPositionType`, one byte at `+0x10`). Packed in that order they
are the 15-byte row, and the loader is
`GameCommonParameterLoaderFromExcel::LoadPetDetectPositionStaticInformation`.
The position fields use the `pos_x`, `pos_y`, `pos_z` names of
[`employeespawnposition.dbss`](employeespawnposition_dbss.md).

The `Pet_DetectPosition` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `No`, `PositionX`, `PositionY` and `PositionZ`
and the keys 1 to 4, the same 4 of 4 keys as the file on clients 1784 and
3474. Its developer workbook (`datasheet_petdatatable.xlsm`) marks the three
position columns `%`, server-only, which is why the client files write `0`
in them. The private server's own compiled `petdetectposition.dbss` is the
same 64 bytes as the client files. The client 1784 server dump reads the
sheet in `Load_Pet_DetectPosition` (VA `0x140870f20`): `No` with
`ReadCellInt` into a u16 at `+0x00`, `PositionX`, `PositionY` and
`PositionZ` with `ReadColumnFloat` at `+0x04`, `+0x08` and `+0x0C`, and a
byte at `+0x10` it sets to `0` and never fills from the sheet, the 2016
layout. The `Pet_DetectPosition` table of a private server on client 519 has
the same 4 keys with `0` in all three positions.

## Notes

- Clients 1485, 1784, 2107, 2519, 3002, 3251 and 3474 have the same 64-byte
  file and 44-byte offset file, byte for byte.
- The `#Name` note column of the client 1784 developer workbook labels the
  four rows: 1 해안절벽 은밀한 동굴 (coastal cliff hidden cave), 2 해안절벽
  동굴 입구 (coastal cliff cave entrance), 3 해안동굴 보스 소환 위치 (coastal
  cave boss summon position), 4 고대인의 석실 입구 (entrance to the
  ancient ones' stone chamber). A `#` column is not compiled into the file.
- The 2016 client has an AI proxy class `ge::AiPetDetectPositionProxy` with
  a `getPosition` method that returns a `pa::float3`. The AI target types of
  a private server on client 519 include `PetDetectPosition` (`4194304`,
  bit 22).
- Pet skill `5` is the only Location Find skill in `petskill.dbss` (client
  3474). Nothing in its row points at a `pet_detect_position_key`.
- No client Lua reads the table: of the 3,073 `.luac` files of client 3474,
  only `global_define_cpp_enum` holds the text `DetectPosition`, as the
  `PetSkillType` enum value.

## Open Questions

### Which Position a Pet Finds

The rows carry no region, quest or pet key, and the client files hold no
coordinates. Whether a Location Find pet reacts to every row near the
player, or the server picks rows some other way, cannot be read from the
client data.
