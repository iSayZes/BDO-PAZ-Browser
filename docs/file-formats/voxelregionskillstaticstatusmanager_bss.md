# `voxelregionskillstaticstatusmanager.bss` Format

## Purpose

Skills tied to a voxel region type: a u32 count after the PABR magic, then
one 5-byte row per entry, a u8 value and a `skill.dbss` skill key. On
client 3474 the file has 2 rows, `4` with All-Consuming Heat (skill 42501,
"Edania (Demon Realm) Region Red Lava Debuff") and `8` with Dead Soul's
Chill (skill 42502, "Edania (Demon Realm) Region Blue Ice Debuff").

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                      | Bytes | Records | Row bytes |
| ------ | -------------- | ----------------------------------------- | ----- | ------- | --------- |
| 1      | 2987 and later | `voxelregionskillstaticstatusmanager.bss` | 30    | 2 Row   | 5         |

| Layout | File                                      | Known        | Unknown    |
| ------ | ----------------------------------------- | ------------ | ---------- |
| 1      | `voxelregionskillstaticstatusmanager.bss` | 28 B (93.3%) | 2 B (6.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e3fcc5571f31`  |
| 3482   | Layout 1 | `e3fcc5571f31`  |
| 3474   | Layout 1 | `e3fcc5571f31`  |
| 3473   | Layout 1 | `e3fcc5571f31`  |
| 3464   | Layout 1 | `e3fcc5571f31`  |
| 3458   | Layout 1 | `e3fcc5571f31`  |
| 3454   | Layout 1 | `e3fcc5571f31`  |
| 3444   | Layout 1 | `e3fcc5571f31`  |
| 3435   | Layout 1 | `e3fcc5571f31`  |
| 3426   | Layout 1 | `e3fcc5571f31`  |
| 3418   | Layout 1 | `e3fcc5571f31`  |
| 3412   | Layout 1 | `e3fcc5571f31`  |
| 3402   | Layout 1 | `e3fcc5571f31`  |
| 3396   | Layout 1 | `e3fcc5571f31`  |
| 3387   | Layout 1 | `e3fcc5571f31`  |
| 3381   | Layout 1 | `e3fcc5571f31`  |
| 3373   | Layout 1 | `e3fcc5571f31`  |
| 3364   | Layout 1 | `e3fcc5571f31`  |
| 3356   | Layout 1 | `e3fcc5571f31`  |
| 3349   | Layout 1 | `e3fcc5571f31`  |
| 3342   | Layout 1 | `e3fcc5571f31`  |
| 3335   | Layout 1 | `e3fcc5571f31`  |
| 3326   | Layout 1 | `e3fcc5571f31`  |
| 3321   | Layout 1 | `e3fcc5571f31`  |
| 3314   | Layout 1 | `e3fcc5571f31`  |
| 3303   | Layout 1 | `e3fcc5571f31`  |
| 3302   | Layout 1 | `e3fcc5571f31`  |
| 3293   | Layout 1 | `e3fcc5571f31`  |
| 3283   | Layout 1 | `e3fcc5571f31`  |
| 3275   | Layout 1 | `e3fcc5571f31`  |
| 3267   | Layout 1 | `e3fcc5571f31`  |
| 3258   | Layout 1 | `e3fcc5571f31`  |
| 3251   | Layout 1 | `e3fcc5571f31`  |
| 3242   | Layout 1 | `e3fcc5571f31`  |
| 3235   | Layout 1 | `e3fcc5571f31`  |
| 3229   | Layout 1 | `e3fcc5571f31`  |
| 3212   | Layout 1 | `e3fcc5571f31`  |
| 3203   | Layout 1 | `e3fcc5571f31`  |
| 3193   | Layout 1 | `e3fcc5571f31`  |
| 3186   | Layout 1 | `e3fcc5571f31`  |
| 3177   | Layout 1 | `e3fcc5571f31`  |
| 3169   | Layout 1 | `e3fcc5571f31`  |
| 3158   | Layout 1 | `e3fcc5571f31`  |
| 3151   | Layout 1 | `e3fcc5571f31`  |
| 3144   | Layout 1 | `e3fcc5571f31`  |
| 3133   | Layout 1 | `e3fcc5571f31`  |
| 3125   | Layout 1 | `e3fcc5571f31`  |
| 3118   | Layout 1 | `e3fcc5571f31`  |
| 3111   | Layout 1 | `e3fcc5571f31`  |
| 3103   | Layout 1 | `e3fcc5571f31`  |
| 3095   | Layout 1 | `e3fcc5571f31`  |
| 3086   | Layout 1 | `e3fcc5571f31`  |
| 3072   | Layout 1 | `e3fcc5571f31`  |
| 3062   | Layout 1 | `e3fcc5571f31`  |
| 3052   | Layout 1 | `e3fcc5571f31`  |
| 3045   | Layout 1 | `e3fcc5571f31`  |
| 3037   | Layout 1 | `e3fcc5571f31`  |
| 3030   | Layout 1 | `e3fcc5571f31`  |
| 3021   | Layout 1 | `e3fcc5571f31`  |
| 3012   | Layout 1 | `e3fcc5571f31`  |
| 3002   | Layout 1 | `e3fcc5571f31`  |
| 2995   | Layout 1 | `e3fcc5571f31`  |
| 2987   | Layout 1 | `e3fcc5571f31`  |
| 2978   | No file  | `e3fcc5571f31`  |
| 2970   | No file  | `e3fcc5571f31`  |
| 2959   | No file  | `e3fcc5571f31`  |
| 2951   | No file  | `e3fcc5571f31`  |
| 2942   | No file  | `e3fcc5571f31`  |
| 2935   | No file  | `e3fcc5571f31`  |
| 2932   | No file  | `e3fcc5571f31`  |
| 2923   | No file  | `e3fcc5571f31`  |
| 2919   | No file  | `e3fcc5571f31`  |
| 2907   | No file  | `e3fcc5571f31`  |
| 2900   | No file  | `e3fcc5571f31`  |
| 2891   | No file  | `e3fcc5571f31`  |
| 2882   | No file  | `e3fcc5571f31`  |
| 2872   | No file  | `e3fcc5571f31`  |
| 2863   | No file  | `e3fcc5571f31`  |
| 2855   | No file  | `e3fcc5571f31`  |
| 2849   | No file  | `e3fcc5571f31`  |
| 2844   | No file  | `e3fcc5571f31`  |
| 2834   | No file  | `e3fcc5571f31`  |
| 2825   | No file  | `e3fcc5571f31`  |
| 2819   | No file  | `e3fcc5571f31`  |
| 2811   | No file  | `e3fcc5571f31`  |
| 2803   | No file  | `e3fcc5571f31`  |
| 2794   | No file  | `e3fcc5571f31`  |
| 2783   | No file  | `e3fcc5571f31`  |
| 2774   | No file  | `e3fcc5571f31`  |
| 2765   | No file  | `e3fcc5571f31`  |
| 2756   | No file  | `e3fcc5571f31`  |
| 2750   | No file  | `e3fcc5571f31`  |
| 2743   | No file  | `e3fcc5571f31`  |
| 2736   | No file  | `e3fcc5571f31`  |
| 2726   | No file  | `e3fcc5571f31`  |
| 2717   | No file  | `e3fcc5571f31`  |
| 2709   | No file  | `e3fcc5571f31`  |
| 2703   | No file  | `e3fcc5571f31`  |
| 2695   | No file  | `e3fcc5571f31`  |
| 2684   | No file  | `e3fcc5571f31`  |
| 2672   | No file  | `e3fcc5571f31`  |
| 2665   | No file  | `e3fcc5571f31`  |
| 2657   | No file  | `e3fcc5571f31`  |
| 2649   | No file  | `e3fcc5571f31`  |
| 2644   | No file  | `e3fcc5571f31`  |
| 2637   | No file  | `e3fcc5571f31`  |
| 2629   | No file  | `e3fcc5571f31`  |
| 2619   | No file  | `e3fcc5571f31`  |
| 2612   | No file  | `e3fcc5571f31`  |
| 2606   | No file  | `e3fcc5571f31`  |
| 2602   | No file  | `e3fcc5571f31`  |
| 2601   | No file  | `e3fcc5571f31`  |
| 2592   | No file  | `e3fcc5571f31`  |
| 2583   | No file  | `e3fcc5571f31`  |
| 2575   | No file  | `e3fcc5571f31`  |
| 2567   | No file  | `e3fcc5571f31`  |
| 2560   | No file  | `e3fcc5571f31`  |
| 2553   | No file  | `e3fcc5571f31`  |
| 2545   | No file  | `e3fcc5571f31`  |
| 2538   | No file  | `e3fcc5571f31`  |
| 2529   | No file  | `e3fcc5571f31`  |
| 2519   | No file  | `e3fcc5571f31`  |
| 2513   | No file  | `e3fcc5571f31`  |
| 2510   | No file  | `e3fcc5571f31`  |
| 2507   | No file  | `e3fcc5571f31`  |
| 2503   | No file  | `e3fcc5571f31`  |
| 2498   | No file  | `e3fcc5571f31`  |
| 2492   | No file  | `e3fcc5571f31`  |
| 2487   | No file  | `e3fcc5571f31`  |
| 2480   | No file  | `e3fcc5571f31`  |
| 2474   | No file  | `e3fcc5571f31`  |
| 2468   | No file  | `e3fcc5571f31`  |
| 2460   | No file  | `e3fcc5571f31`  |
| 2453   | No file  | `e3fcc5571f31`  |
| 2444   | No file  | `e3fcc5571f31`  |
| 2438   | No file  | `e3fcc5571f31`  |
| 2434   | No file  | `e3fcc5571f31`  |
| 2429   | No file  | `e3fcc5571f31`  |
| 2421   | No file  | `e3fcc5571f31`  |
| 2414   | No file  | `e3fcc5571f31`  |
| 2407   | No file  | `e3fcc5571f31`  |
| 2401   | No file  | `e3fcc5571f31`  |
| 2397   | No file  | `e3fcc5571f31`  |
| 2393   | No file  | `e3fcc5571f31`  |
| 2384   | No file  | `e3fcc5571f31`  |
| 2378   | No file  | `e3fcc5571f31`  |
| 2372   | No file  | `e3fcc5571f31`  |
| 2358   | No file  | `e3fcc5571f31`  |
| 2352   | No file  | `e3fcc5571f31`  |
| 2347   | No file  | `e3fcc5571f31`  |
| 2343   | No file  | `e3fcc5571f31`  |
| 2335   | No file  | `e3fcc5571f31`  |
| 2327   | No file  | `e3fcc5571f31`  |
| 2324   | No file  | `e3fcc5571f31`  |
| 2319   | No file  | `e3fcc5571f31`  |
| 2313   | No file  | `e3fcc5571f31`  |
| 2308   | No file  | `e3fcc5571f31`  |
| 2302   | No file  | `e3fcc5571f31`  |
| 2295   | No file  | `e3fcc5571f31`  |
| 2290   | No file  | `e3fcc5571f31`  |
| 2284   | No file  | `e3fcc5571f31`  |
| 2276   | No file  | `e3fcc5571f31`  |
| 2269   | No file  | `e3fcc5571f31`  |
| 2259   | No file  | `e3fcc5571f31`  |
| 2250   | No file  | `e3fcc5571f31`  |
| 2243   | No file  | `e3fcc5571f31`  |
| 2235   | No file  | `e3fcc5571f31`  |
| 2229   | No file  | `e3fcc5571f31`  |
| 2224   | No file  | `e3fcc5571f31`  |
| 2218   | No file  | `e3fcc5571f31`  |
| 2215   | No file  | `e3fcc5571f31`  |
| 2207   | No file  | `e3fcc5571f31`  |
| 2203   | No file  | `e3fcc5571f31`  |
| 2196   | No file  | `e3fcc5571f31`  |
| 2192   | No file  | `e3fcc5571f31`  |
| 2189   | No file  | `e3fcc5571f31`  |
| 2183   | No file  | `e3fcc5571f31`  |
| 2179   | No file  | `e3fcc5571f31`  |
| 2171   | No file  | `e3fcc5571f31`  |
| 2163   | No file  | `e3fcc5571f31`  |
| 2156   | No file  | `e3fcc5571f31`  |
| 2151   | No file  | `e3fcc5571f31`  |
| 2147   | No file  | `e3fcc5571f31`  |
| 2142   | No file  | `e3fcc5571f31`  |
| 2138   | No file  | `e3fcc5571f31`  |
| 2134   | No file  | `e3fcc5571f31`  |
| 2130   | No file  | `e3fcc5571f31`  |
| 2122   | No file  | `e3fcc5571f31`  |
| 2107   | No file  | `e3fcc5571f31`  |
| 2098   | No file  | `e3fcc5571f31`  |
| 2089   | No file  | `e3fcc5571f31`  |
| 2081   | No file  | `e3fcc5571f31`  |
| 2073   | No file  | `e3fcc5571f31`  |
| 2067   | No file  | `e3fcc5571f31`  |
| 2063   | No file  | `e3fcc5571f31`  |
| 2059   | No file  | `e3fcc5571f31`  |
| 2052   | No file  | `e3fcc5571f31`  |
| 2044   | No file  | `e3fcc5571f31`  |
| 2039   | No file  | `e3fcc5571f31`  |
| 2032   | No file  | `e3fcc5571f31`  |
| 2025   | No file  | `e3fcc5571f31`  |
| 2011   | No file  | `e3fcc5571f31`  |
| 2005   | No file  | `e3fcc5571f31`  |
| 2000   | No file  | `e3fcc5571f31`  |
| 1996   | No file  | `e3fcc5571f31`  |
| 1991   | No file  | `e3fcc5571f31`  |
| 1985   | No file  | `e3fcc5571f31`  |
| 1980   | No file  | `e3fcc5571f31`  |
| 1969   | No file  | `e3fcc5571f31`  |
| 1964   | No file  | `e3fcc5571f31`  |
| 1958   | No file  | `e3fcc5571f31`  |
| 1950   | No file  | `e3fcc5571f31`  |
| 1945   | No file  | `e3fcc5571f31`  |
| 1937   | No file  | `e3fcc5571f31`  |
| 1933   | No file  | `e3fcc5571f31`  |
| 1927   | No file  | `e3fcc5571f31`  |
| 1921   | No file  | `e3fcc5571f31`  |
| 1914   | No file  | `e3fcc5571f31`  |
| 1908   | No file  | `e3fcc5571f31`  |
| 1897   | No file  | `e3fcc5571f31`  |
| 1892   | No file  | `e3fcc5571f31`  |
| 1886   | No file  | `e3fcc5571f31`  |
| 1881   | No file  | `e3fcc5571f31`  |
| 1871   | No file  | `e3fcc5571f31`  |
| 1866   | No file  | `e3fcc5571f31`  |
| 1862   | No file  | `e3fcc5571f31`  |
| 1854   | No file  | `e3fcc5571f31`  |
| 1846   | No file  | `e3fcc5571f31`  |
| 1838   | No file  | `e3fcc5571f31`  |
| 1832   | No file  | `e3fcc5571f31`  |
| 1826   | No file  | `e3fcc5571f31`  |
| 1822   | No file  | `e3fcc5571f31`  |
| 1818   | No file  | `e3fcc5571f31`  |
| 1804   | No file  | `e3fcc5571f31`  |
| 1794   | No file  | `e3fcc5571f31`  |
| 1790   | No file  | `e3fcc5571f31`  |
| 1784   | No file  | `e3fcc5571f31`  |
| 1774   | No file  | `e3fcc5571f31`  |
| 1771   | No file  | `e3fcc5571f31`  |
| 1762   | No file  | `e3fcc5571f31`  |
| 1759   | No file  | `e3fcc5571f31`  |
| 1754   | No file  | `e3fcc5571f31`  |
| 1749   | No file  | `e3fcc5571f31`  |
| 1743   | No file  | `e3fcc5571f31`  |
| 1737   | No file  | `e3fcc5571f31`  |
| 1731   | No file  | `e3fcc5571f31`  |
| 1725   | No file  | `e3fcc5571f31`  |
| 1717   | No file  | `e3fcc5571f31`  |
| 1710   | No file  | `e3fcc5571f31`  |
| 1704   | No file  | `e3fcc5571f31`  |
| 1698   | No file  | `e3fcc5571f31`  |
| 1690   | No file  | `e3fcc5571f31`  |
| 1685   | No file  | `e3fcc5571f31`  |
| 1680   | No file  | `e3fcc5571f31`  |
| 1674   | No file  | `e3fcc5571f31`  |
| 1668   | No file  | `e3fcc5571f31`  |
| 1659   | No file  | `e3fcc5571f31`  |
| 1649   | No file  | `e3fcc5571f31`  |
| 1642   | No file  | `e3fcc5571f31`  |
| 1636   | No file  | `e3fcc5571f31`  |
| 1628   | No file  | `e3fcc5571f31`  |
| 1622   | No file  | `e3fcc5571f31`  |
| 1614   | No file  | `e3fcc5571f31`  |
| 1608   | No file  | `e3fcc5571f31`  |
| 1602   | No file  | `e3fcc5571f31`  |
| 1598   | No file  | `e3fcc5571f31`  |
| 1594   | No file  | `e3fcc5571f31`  |
| 1590   | No file  | `e3fcc5571f31`  |
| 1587   | No file  | `e3fcc5571f31`  |
| 1584   | No file  | `e3fcc5571f31`  |
| 1579   | No file  | `e3fcc5571f31`  |
| 1572   | No file  | `e3fcc5571f31`  |
| 1565   | No file  | `e3fcc5571f31`  |
| 1559   | No file  | `e3fcc5571f31`  |
| 1554   | No file  | `e3fcc5571f31`  |
| 1547   | No file  | `e3fcc5571f31`  |
| 1537   | No file  | `e3fcc5571f31`  |
| 1529   | No file  | `e3fcc5571f31`  |
| 1524   | No file  | `e3fcc5571f31`  |
| 1519   | No file  | `e3fcc5571f31`  |
| 1509   | No file  | `e3fcc5571f31`  |
| 1506   | No file  | `e3fcc5571f31`  |
| 1504   | No file  | `e3fcc5571f31`  |
| 1500   | No file  | `e3fcc5571f31`  |
| 1493   | No file  | `e3fcc5571f31`  |
| 1489   | No file  | `e3fcc5571f31`  |
| 1485   | No file  | `e3fcc5571f31`  |
| 1481   | No file  | `e3fcc5571f31`  |
| 1474   | No file  | `e3fcc5571f31`  |
| 1466   | No file  | `e3fcc5571f31`  |
| 1462   | No file  | `e3fcc5571f31`  |
| 1459   | No file  | `e3fcc5571f31`  |
| 1453   | No file  | `e3fcc5571f31`  |
| 1450   | No file  | `e3fcc5571f31`  |
| 1445   | No file  | `e3fcc5571f31`  |
| 1439   | No file  | `e3fcc5571f31`  |
| 1433   | No file  | `e3fcc5571f31`  |
| 1430   | No file  | `e3fcc5571f31`  |
| 1426   | No file  | `e3fcc5571f31`  |
| 1421   | No file  | `e3fcc5571f31`  |
| 1417   | No file  | `e3fcc5571f31`  |
| 1416   | No file  | `e3fcc5571f31`  |
| 1409   | No file  | `e3fcc5571f31`  |
| 1405   | No file  | `e3fcc5571f31`  |
| 1401   | No file  | `e3fcc5571f31`  |
| 1396   | No file  | `e3fcc5571f31`  |
| 1391   | No file  | `e3fcc5571f31`  |
| 1390   | No file  | `e3fcc5571f31`  |
| 1386   | No file  | `e3fcc5571f31`  |
| 1381   | No file  | `e3fcc5571f31`  |
| 1379   | No file  | `e3fcc5571f31`  |
| 1372   | No file  | `e3fcc5571f31`  |
| 1366   | No file  | `e3fcc5571f31`  |
| 1364   | No file  | `e3fcc5571f31`  |
| 1363   | No file  | `e3fcc5571f31`  |
| 1360   | No file  | `e3fcc5571f31`  |
| 1358   | No file  | `e3fcc5571f31`  |
| 1355   | No file  | `e3fcc5571f31`  |
| 1351   | No file  | `e3fcc5571f31`  |
| 1348   | No file  | `e3fcc5571f31`  |
| 1346   | No file  | `e3fcc5571f31`  |
| 1341   | No file  | `e3fcc5571f31`  |
| 1340   | No file  | `e3fcc5571f31`  |
| 1338   | No file  | `e3fcc5571f31`  |
| 1335   | No file  | `e3fcc5571f31`  |
| 1333   | No file  | `e3fcc5571f31`  |
| 1329   | No file  | `e3fcc5571f31`  |
| 1327   | No file  | `e3fcc5571f31`  |
| 1324   | No file  | `e3fcc5571f31`  |
| 1321   | No file  | `e3fcc5571f31`  |
| 1319   | No file  | `e3fcc5571f31`  |
| 1318   | No file  | `e3fcc5571f31`  |
| 1316   | No file  | `e3fcc5571f31`  |
| 1313   | No file  | `e3fcc5571f31`  |
| 1311   | No file  | `e3fcc5571f31`  |
| 1309   | No file  | `e3fcc5571f31`  |
| 1304   | No file  | `e3fcc5571f31`  |
| 1292   | No file  | `e3fcc5571f31`  |
| 1286   | No file  | `e3fcc5571f31`  |
| 1280   | No file  | `e3fcc5571f31`  |
| 1276   | No file  | `e3fcc5571f31`  |
| 1267   | No file  | `e3fcc5571f31`  |
| 1261   | No file  | `e3fcc5571f31`  |
| 1256   | No file  | `e3fcc5571f31`  |
| 1250   | No file  | `e3fcc5571f31`  |
| 1246   | No file  | `e3fcc5571f31`  |
| 1239   | No file  | `e3fcc5571f31`  |
| 1230   | No file  | `e3fcc5571f31`  |
| 1226   | No file  | `e3fcc5571f31`  |
| 1220   | No file  | `e3fcc5571f31`  |
| 1217   | No file  | `e3fcc5571f31`  |
| 1211   | No file  | `e3fcc5571f31`  |
| 1210   | No file  | `e3fcc5571f31`  |
| 1208   | No file  | `e3fcc5571f31`  |
| 1203   | No file  | `e3fcc5571f31`  |
| 1197   | No file  | `e3fcc5571f31`  |
| 1194   | No file  | `e3fcc5571f31`  |
| 1192   | No file  | `e3fcc5571f31`  |
| 1187   | No file  | `e3fcc5571f31`  |
| 1183   | No file  | `e3fcc5571f31`  |
| 1177   | No file  | `e3fcc5571f31`  |
| 1173   | No file  | `e3fcc5571f31`  |
| 1167   | No file  | `e3fcc5571f31`  |
| 1164   | No file  | `e3fcc5571f31`  |
| 1156   | No file  | `e3fcc5571f31`  |
| 1149   | No file  | `e3fcc5571f31`  |
| 1144   | No file  | `e3fcc5571f31`  |
| 1137   | No file  | `e3fcc5571f31`  |
| 1132   | No file  | `e3fcc5571f31`  |
| 1127   | No file  | `e3fcc5571f31`  |
| 1122   | No file  | `e3fcc5571f31`  |
| 1118   | No file  | `e3fcc5571f31`  |
| 1114   | No file  | `e3fcc5571f31`  |
| 1109   | No file  | `e3fcc5571f31`  |
| 1102   | No file  | `e3fcc5571f31`  |
| 1096   | No file  | `e3fcc5571f31`  |
| 1088   | No file  | `e3fcc5571f31`  |
| 1081   | No file  | `e3fcc5571f31`  |
| 1076   | No file  | `e3fcc5571f31`  |
| 1069   | No file  | `e3fcc5571f31`  |
| 1064   | No file  | `e3fcc5571f31`  |
| 1058   | No file  | `e3fcc5571f31`  |
| 1051   | No file  | `e3fcc5571f31`  |
| 1044   | No file  | `e3fcc5571f31`  |
| 1036   | No file  | `e3fcc5571f31`  |
| 1026   | No file  | `e3fcc5571f31`  |
| 1016   | No file  | `e3fcc5571f31`  |
| 1009   | No file  | `e3fcc5571f31`  |
| 1005   | No file  | `e3fcc5571f31`  |
| 1000   | No file  | `e3fcc5571f31`  |
| 998    | No file  | `e3fcc5571f31`  |
| 990    | No file  | `e3fcc5571f31`  |
| 979    | No file  | `e3fcc5571f31`  |
| 972    | No file  | `e3fcc5571f31`  |
| 963    | No file  | `e3fcc5571f31`  |
| 955    | No file  | `e3fcc5571f31`  |
| 946    | No file  | `e3fcc5571f31`  |
| 938    | No file  | `e3fcc5571f31`  |
| 927    | No file  | `e3fcc5571f31`  |
| 911    | No file  | `e3fcc5571f31`  |
| 904    | No file  | `e3fcc5571f31`  |
| 899    | No file  | `e3fcc5571f31`  |
| 894    | No file  | `e3fcc5571f31`  |
| 885    | No file  | `e3fcc5571f31`  |
| 879    | No file  | `e3fcc5571f31`  |
| 872    | No file  | `e3fcc5571f31`  |
| 864    | No file  | `e3fcc5571f31`  |
| 855    | No file  | `e3fcc5571f31`  |
| 853    | No file  | `e3fcc5571f31`  |
| 845    | No file  | `e3fcc5571f31`  |
| 837    | No file  | `e3fcc5571f31`  |
| 829    | No file  | `e3fcc5571f31`  |
| 822    | No file  | `e3fcc5571f31`  |
| 814    | No file  | `e3fcc5571f31`  |
| 805    | No file  | `e3fcc5571f31`  |
| 794    | No file  | `e3fcc5571f31`  |
| 787    | No file  | `e3fcc5571f31`  |
| 780    | No file  | `e3fcc5571f31`  |
| 771    | No file  | `e3fcc5571f31`  |
| 760    | No file  | `e3fcc5571f31`  |
| 748    | No file  | `e3fcc5571f31`  |
| 741    | No file  | `e3fcc5571f31`  |
| 736    | No file  | `e3fcc5571f31`  |
| 731    | No file  | `e3fcc5571f31`  |
| 723    | No file  | `e3fcc5571f31`  |
| 711    | No file  | `e3fcc5571f31`  |
| 707    | No file  | `e3fcc5571f31`  |
| 697    | No file  | `e3fcc5571f31`  |
| 689    | No file  | `e3fcc5571f31`  |
| 683    | No file  | `e3fcc5571f31`  |
| 678    | No file  | `e3fcc5571f31`  |
| 670    | No file  | `e3fcc5571f31`  |
| 661    | No file  | `e3fcc5571f31`  |
| 656    | No file  | `e3fcc5571f31`  |
| 652    | No file  | `e3fcc5571f31`  |
| 643    | No file  | `e3fcc5571f31`  |
| 637    | No file  | `e3fcc5571f31`  |
| 630    | No file  | `e3fcc5571f31`  |
| 627    | No file  | `e3fcc5571f31`  |
| 621    | No file  | `e3fcc5571f31`  |
| 617    | No file  | `e3fcc5571f31`  |
| 615    | No file  | `e3fcc5571f31`  |
| 606    | No file  | `e3fcc5571f31`  |
| 599    | No file  | `e3fcc5571f31`  |
| 592    | No file  | `e3fcc5571f31`  |
| 586    | No file  | `e3fcc5571f31`  |
| 577    | No file  | `e3fcc5571f31`  |
| 569    | No file  | `e3fcc5571f31`  |
| 561    | No file  | `e3fcc5571f31`  |
| 554    | No file  | `e3fcc5571f31`  |
| 542    | No file  | `e3fcc5571f31`  |
| 532    | No file  | `e3fcc5571f31`  |
| 531    | No file  | `e3fcc5571f31`  |
| 526    | No file  | `e3fcc5571f31`  |
| 521    | No file  | `e3fcc5571f31`  |
| 517    | No file  | `e3fcc5571f31`  |
| 510    | No file  | `e3fcc5571f31`  |
| 508    | No file  | `e3fcc5571f31`  |
| 504    | No file  | `e3fcc5571f31`  |
| 497    | No file  | `e3fcc5571f31`  |
| 491    | No file  | `e3fcc5571f31`  |
| 485    | No file  | `e3fcc5571f31`  |
| 478    | No file  | `e3fcc5571f31`  |
| 472    | No file  | `e3fcc5571f31`  |
| 466    | No file  | `e3fcc5571f31`  |
| 457    | No file  | `e3fcc5571f31`  |
| 452    | No file  | `e3fcc5571f31`  |
| 449    | No file  | `e3fcc5571f31`  |
| 435    | No file  | `e3fcc5571f31`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                          |
| --------------------- | -------- | ----------------------------- |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10      |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field        | Notes                                                      |
| ------------------- | --------------- | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32             | row_count    | Number of rows                                             |
| `+0x08`             | Row[row_count]  | rows         | See Row; byte-packed                                       |
| `rows+0x00`         | String Table    | string_table | See String Table                                           |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where `rows` ends              |
| `string_table+0x04` | u32             | zero         | Always `0`                                                 |

### Row (5 bytes)

| Offset  | Type | Field      | Notes                                                                                   |
| ------- | ---- | ---------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u8   | unknown_00 | `4` and `8` on client 3474; unique                                                      |
| `+0x01` | u32  | skill_key  | `skill.dbss` key, `skill_no << 16 \| level`; the handler shows the LOC type 10 skill name |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The file is newer than client 1784: no sheet of a private server's
`DataSheets.bexcel` on that client and no string of its server dump has
`Voxel` in the name, and the 2016 client predates it. `skill_key` is named
by value: both values (`2785345537` and `2785411073`) are row keys of
`skill.dbss` on client 3474, skills 42501 and 42502 at level 1, and the
LOC type 10 description of each names an Edania region debuff.

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 02 00 00 00 04 01 00 05 A6 08 01 00 06 A6 00 00 00 00 12 00 00 00 00 00 00 00`
  (30 bytes). The file is not in the archives of clients 794 to 2519.
- `skill.dbss` on client 3474 links buff 42859 (All-Consuming Heat) to
  skill 42501, and buffs 42860 (Dead Soul's Chill) and 40035 (Movement
  Speed -25% for 5 sec) to skill 42502.
- No client Lua file on client 3474 has `VoxelRegion` in a string.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per skill.

## Open Questions

### Region Type Values

`unknown_00` is `4` for the lava debuff and `8` for the ice debuff. The
values look like voxel region types or bit flags (`4` and `8` are single
bits), but no client enum or Lua call with `Voxel` in its name lists them.
