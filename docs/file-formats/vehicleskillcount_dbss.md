# `vehicleskillcount.dbss` Format

## Purpose

One byte: the highest mount and ship skill key in
[vehicleskill.dbss](vehicleskill_dbss.md) plus one. On client 3474 it is
`107` (`0x6B`), and `vehicleskill.dbss` holds the 106 skills with keys 1
to 106. The client Lua reads the value through
`vehicleSkillStaticStatus_skillCount()` and walks the skill keys from 1 to
one below it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------ | ----- | ------- | --------- |
| 1      | 1261 and later | `vehicleskillcount.dbss` | 1     | -       | -         |

| Layout | File                     | Known        | Unknown    |
| ------ | ------------------------ | ------------ | ---------- |
| 1      | `vehicleskillcount.dbss` | 1 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fadfefe74d36`  |
| 3482   | Layout 1 | `fadfefe74d36`  |
| 3474   | Layout 1 | `fadfefe74d36`  |
| 3473   | Layout 1 | `fadfefe74d36`  |
| 3464   | Layout 1 | `fadfefe74d36`  |
| 3458   | Layout 1 | `fadfefe74d36`  |
| 3454   | Layout 1 | `fadfefe74d36`  |
| 3444   | Layout 1 | `fadfefe74d36`  |
| 3435   | Layout 1 | `fadfefe74d36`  |
| 3426   | Layout 1 | `fadfefe74d36`  |
| 3418   | Layout 1 | `fadfefe74d36`  |
| 3412   | Layout 1 | `fadfefe74d36`  |
| 3402   | Layout 1 | `fadfefe74d36`  |
| 3396   | Layout 1 | `fadfefe74d36`  |
| 3387   | Layout 1 | `fadfefe74d36`  |
| 3381   | Layout 1 | `fadfefe74d36`  |
| 3373   | Layout 1 | `fadfefe74d36`  |
| 3364   | Layout 1 | `fadfefe74d36`  |
| 3356   | Layout 1 | `fadfefe74d36`  |
| 3349   | Layout 1 | `fadfefe74d36`  |
| 3342   | Layout 1 | `fadfefe74d36`  |
| 3335   | Layout 1 | `fadfefe74d36`  |
| 3326   | Layout 1 | `fadfefe74d36`  |
| 3321   | Layout 1 | `fadfefe74d36`  |
| 3314   | Layout 1 | `fadfefe74d36`  |
| 3303   | Layout 1 | `fadfefe74d36`  |
| 3302   | Layout 1 | `fadfefe74d36`  |
| 3293   | Layout 1 | `fadfefe74d36`  |
| 3283   | Layout 1 | `fadfefe74d36`  |
| 3275   | Layout 1 | `fadfefe74d36`  |
| 3267   | Layout 1 | `fadfefe74d36`  |
| 3258   | Layout 1 | `fadfefe74d36`  |
| 3251   | Layout 1 | `fadfefe74d36`  |
| 3242   | Layout 1 | `fadfefe74d36`  |
| 3235   | Layout 1 | `fadfefe74d36`  |
| 3229   | Layout 1 | `fadfefe74d36`  |
| 3212   | Layout 1 | `fadfefe74d36`  |
| 3203   | Layout 1 | `fadfefe74d36`  |
| 3193   | Layout 1 | `fadfefe74d36`  |
| 3186   | Layout 1 | `fadfefe74d36`  |
| 3177   | Layout 1 | `fadfefe74d36`  |
| 3169   | Layout 1 | `fadfefe74d36`  |
| 3158   | Layout 1 | `fadfefe74d36`  |
| 3151   | Layout 1 | `fadfefe74d36`  |
| 3144   | Layout 1 | `fadfefe74d36`  |
| 3133   | Layout 1 | `fadfefe74d36`  |
| 3125   | Layout 1 | `fadfefe74d36`  |
| 3118   | Layout 1 | `fadfefe74d36`  |
| 3111   | Layout 1 | `fadfefe74d36`  |
| 3103   | Layout 1 | `fadfefe74d36`  |
| 3095   | Layout 1 | `fadfefe74d36`  |
| 3086   | Layout 1 | `fadfefe74d36`  |
| 3072   | Layout 1 | `fadfefe74d36`  |
| 3062   | Layout 1 | `fadfefe74d36`  |
| 3052   | Layout 1 | `fadfefe74d36`  |
| 3045   | Layout 1 | `fadfefe74d36`  |
| 3037   | Layout 1 | `fadfefe74d36`  |
| 3030   | Layout 1 | `fadfefe74d36`  |
| 3021   | Layout 1 | `fadfefe74d36`  |
| 3012   | Layout 1 | `fadfefe74d36`  |
| 3002   | Layout 1 | `fadfefe74d36`  |
| 2995   | Layout 1 | `fadfefe74d36`  |
| 2987   | Layout 1 | `fadfefe74d36`  |
| 2978   | Layout 1 | `fadfefe74d36`  |
| 2970   | Layout 1 | `fadfefe74d36`  |
| 2959   | Layout 1 | `fadfefe74d36`  |
| 2951   | Layout 1 | `fadfefe74d36`  |
| 2942   | Layout 1 | `fadfefe74d36`  |
| 2935   | Layout 1 | `fadfefe74d36`  |
| 2932   | Layout 1 | `fadfefe74d36`  |
| 2923   | Layout 1 | `fadfefe74d36`  |
| 2919   | Layout 1 | `fadfefe74d36`  |
| 2907   | Layout 1 | `fadfefe74d36`  |
| 2900   | Layout 1 | `fadfefe74d36`  |
| 2891   | Layout 1 | `fadfefe74d36`  |
| 2882   | Layout 1 | `fadfefe74d36`  |
| 2872   | Layout 1 | `fadfefe74d36`  |
| 2863   | Layout 1 | `fadfefe74d36`  |
| 2855   | Layout 1 | `fadfefe74d36`  |
| 2849   | Layout 1 | `fadfefe74d36`  |
| 2844   | Layout 1 | `fadfefe74d36`  |
| 2834   | Layout 1 | `fadfefe74d36`  |
| 2825   | Layout 1 | `fadfefe74d36`  |
| 2819   | Layout 1 | `fadfefe74d36`  |
| 2811   | Layout 1 | `fadfefe74d36`  |
| 2803   | Layout 1 | `fadfefe74d36`  |
| 2794   | Layout 1 | `fadfefe74d36`  |
| 2783   | Layout 1 | `fadfefe74d36`  |
| 2774   | Layout 1 | `fadfefe74d36`  |
| 2765   | Layout 1 | `fadfefe74d36`  |
| 2756   | Layout 1 | `fadfefe74d36`  |
| 2750   | Layout 1 | `fadfefe74d36`  |
| 2743   | Layout 1 | `fadfefe74d36`  |
| 2736   | Layout 1 | `fadfefe74d36`  |
| 2726   | Layout 1 | `fadfefe74d36`  |
| 2717   | Layout 1 | `fadfefe74d36`  |
| 2709   | Layout 1 | `fadfefe74d36`  |
| 2703   | Layout 1 | `fadfefe74d36`  |
| 2695   | Layout 1 | `fadfefe74d36`  |
| 2684   | Layout 1 | `fadfefe74d36`  |
| 2672   | Layout 1 | `fadfefe74d36`  |
| 2665   | Layout 1 | `fadfefe74d36`  |
| 2657   | Layout 1 | `fadfefe74d36`  |
| 2649   | Layout 1 | `fadfefe74d36`  |
| 2644   | Layout 1 | `fadfefe74d36`  |
| 2637   | Layout 1 | `fadfefe74d36`  |
| 2629   | Layout 1 | `fadfefe74d36`  |
| 2619   | Layout 1 | `fadfefe74d36`  |
| 2612   | Layout 1 | `fadfefe74d36`  |
| 2606   | Layout 1 | `fadfefe74d36`  |
| 2602   | Layout 1 | `fadfefe74d36`  |
| 2601   | Layout 1 | `fadfefe74d36`  |
| 2592   | Layout 1 | `fadfefe74d36`  |
| 2583   | Layout 1 | `fadfefe74d36`  |
| 2575   | Layout 1 | `fadfefe74d36`  |
| 2567   | Layout 1 | `fadfefe74d36`  |
| 2560   | Layout 1 | `fadfefe74d36`  |
| 2553   | Layout 1 | `fadfefe74d36`  |
| 2545   | Layout 1 | `fadfefe74d36`  |
| 2538   | Layout 1 | `fadfefe74d36`  |
| 2529   | Layout 1 | `fadfefe74d36`  |
| 2519   | Layout 1 | `fadfefe74d36`  |
| 2513   | Layout 1 | `fadfefe74d36`  |
| 2510   | Layout 1 | `fadfefe74d36`  |
| 2507   | Layout 1 | `fadfefe74d36`  |
| 2503   | Layout 1 | `fadfefe74d36`  |
| 2498   | Layout 1 | `fadfefe74d36`  |
| 2492   | Layout 1 | `fadfefe74d36`  |
| 2487   | Layout 1 | `fadfefe74d36`  |
| 2480   | Layout 1 | `fadfefe74d36`  |
| 2474   | Layout 1 | `fadfefe74d36`  |
| 2468   | Layout 1 | `fadfefe74d36`  |
| 2460   | Layout 1 | `fadfefe74d36`  |
| 2453   | Layout 1 | `fadfefe74d36`  |
| 2444   | Layout 1 | `fadfefe74d36`  |
| 2438   | Layout 1 | `fadfefe74d36`  |
| 2434   | Layout 1 | `fadfefe74d36`  |
| 2429   | Layout 1 | `fadfefe74d36`  |
| 2421   | Layout 1 | `fadfefe74d36`  |
| 2414   | Layout 1 | `fadfefe74d36`  |
| 2407   | Layout 1 | `fadfefe74d36`  |
| 2401   | Layout 1 | `fadfefe74d36`  |
| 2397   | Layout 1 | `fadfefe74d36`  |
| 2393   | Layout 1 | `fadfefe74d36`  |
| 2384   | Layout 1 | `fadfefe74d36`  |
| 2378   | Layout 1 | `fadfefe74d36`  |
| 2372   | Layout 1 | `fadfefe74d36`  |
| 2358   | Layout 1 | `fadfefe74d36`  |
| 2352   | Layout 1 | `fadfefe74d36`  |
| 2347   | Layout 1 | `fadfefe74d36`  |
| 2343   | Layout 1 | `fadfefe74d36`  |
| 2335   | Layout 1 | `fadfefe74d36`  |
| 2327   | Layout 1 | `fadfefe74d36`  |
| 2324   | Layout 1 | `fadfefe74d36`  |
| 2319   | Layout 1 | `fadfefe74d36`  |
| 2313   | Layout 1 | `fadfefe74d36`  |
| 2308   | Layout 1 | `fadfefe74d36`  |
| 2302   | Layout 1 | `fadfefe74d36`  |
| 2295   | Layout 1 | `fadfefe74d36`  |
| 2290   | Layout 1 | `fadfefe74d36`  |
| 2284   | Layout 1 | `fadfefe74d36`  |
| 2276   | Layout 1 | `fadfefe74d36`  |
| 2269   | Layout 1 | `fadfefe74d36`  |
| 2259   | Layout 1 | `fadfefe74d36`  |
| 2250   | Layout 1 | `fadfefe74d36`  |
| 2243   | Layout 1 | `fadfefe74d36`  |
| 2235   | Layout 1 | `fadfefe74d36`  |
| 2229   | Layout 1 | `fadfefe74d36`  |
| 2224   | Layout 1 | `fadfefe74d36`  |
| 2218   | Layout 1 | `fadfefe74d36`  |
| 2215   | Layout 1 | `fadfefe74d36`  |
| 2207   | Layout 1 | `fadfefe74d36`  |
| 2203   | Layout 1 | `fadfefe74d36`  |
| 2196   | Layout 1 | `fadfefe74d36`  |
| 2192   | Layout 1 | `fadfefe74d36`  |
| 2189   | Layout 1 | `fadfefe74d36`  |
| 2183   | Layout 1 | `fadfefe74d36`  |
| 2179   | Layout 1 | `fadfefe74d36`  |
| 2171   | Layout 1 | `fadfefe74d36`  |
| 2163   | Layout 1 | `fadfefe74d36`  |
| 2156   | Layout 1 | `fadfefe74d36`  |
| 2151   | Layout 1 | `fadfefe74d36`  |
| 2147   | Layout 1 | `fadfefe74d36`  |
| 2142   | Layout 1 | `fadfefe74d36`  |
| 2138   | Layout 1 | `fadfefe74d36`  |
| 2134   | Layout 1 | `fadfefe74d36`  |
| 2130   | Layout 1 | `fadfefe74d36`  |
| 2122   | Layout 1 | `fadfefe74d36`  |
| 2107   | Layout 1 | `fadfefe74d36`  |
| 2098   | Layout 1 | `fadfefe74d36`  |
| 2089   | Layout 1 | `fadfefe74d36`  |
| 2081   | Layout 1 | `fadfefe74d36`  |
| 2073   | Layout 1 | `fadfefe74d36`  |
| 2067   | Layout 1 | `fadfefe74d36`  |
| 2063   | Layout 1 | `fadfefe74d36`  |
| 2059   | Layout 1 | `fadfefe74d36`  |
| 2052   | Layout 1 | `fadfefe74d36`  |
| 2044   | Layout 1 | `fadfefe74d36`  |
| 2039   | Layout 1 | `fadfefe74d36`  |
| 2032   | Layout 1 | `fadfefe74d36`  |
| 2025   | Layout 1 | `fadfefe74d36`  |
| 2011   | Layout 1 | `fadfefe74d36`  |
| 2005   | Layout 1 | `fadfefe74d36`  |
| 2000   | Layout 1 | `fadfefe74d36`  |
| 1996   | Layout 1 | `fadfefe74d36`  |
| 1991   | Layout 1 | `fadfefe74d36`  |
| 1985   | Layout 1 | `fadfefe74d36`  |
| 1980   | Layout 1 | `fadfefe74d36`  |
| 1969   | Layout 1 | `fadfefe74d36`  |
| 1964   | Layout 1 | `fadfefe74d36`  |
| 1958   | Layout 1 | `fadfefe74d36`  |
| 1950   | Layout 1 | `fadfefe74d36`  |
| 1945   | Layout 1 | `fadfefe74d36`  |
| 1937   | Layout 1 | `fadfefe74d36`  |
| 1933   | Layout 1 | `fadfefe74d36`  |
| 1927   | Layout 1 | `fadfefe74d36`  |
| 1921   | Layout 1 | `fadfefe74d36`  |
| 1914   | Layout 1 | `fadfefe74d36`  |
| 1908   | Layout 1 | `fadfefe74d36`  |
| 1897   | Layout 1 | `fadfefe74d36`  |
| 1892   | Layout 1 | `fadfefe74d36`  |
| 1886   | Layout 1 | `fadfefe74d36`  |
| 1881   | Layout 1 | `fadfefe74d36`  |
| 1871   | Layout 1 | `fadfefe74d36`  |
| 1866   | Layout 1 | `fadfefe74d36`  |
| 1862   | Layout 1 | `fadfefe74d36`  |
| 1854   | Layout 1 | `fadfefe74d36`  |
| 1846   | Layout 1 | `fadfefe74d36`  |
| 1838   | Layout 1 | `fadfefe74d36`  |
| 1832   | Layout 1 | `fadfefe74d36`  |
| 1826   | Layout 1 | `fadfefe74d36`  |
| 1822   | Layout 1 | `fadfefe74d36`  |
| 1818   | Layout 1 | `fadfefe74d36`  |
| 1804   | Layout 1 | `fadfefe74d36`  |
| 1794   | Layout 1 | `fadfefe74d36`  |
| 1790   | Layout 1 | `fadfefe74d36`  |
| 1784   | Layout 1 | `fadfefe74d36`  |
| 1774   | Layout 1 | `fadfefe74d36`  |
| 1771   | Layout 1 | `fadfefe74d36`  |
| 1762   | Layout 1 | `fadfefe74d36`  |
| 1759   | Layout 1 | `fadfefe74d36`  |
| 1754   | Layout 1 | `fadfefe74d36`  |
| 1749   | Layout 1 | `fadfefe74d36`  |
| 1743   | Layout 1 | `fadfefe74d36`  |
| 1737   | Layout 1 | `fadfefe74d36`  |
| 1731   | Layout 1 | `fadfefe74d36`  |
| 1725   | Layout 1 | `fadfefe74d36`  |
| 1717   | Layout 1 | `fadfefe74d36`  |
| 1710   | Layout 1 | `fadfefe74d36`  |
| 1704   | Layout 1 | `fadfefe74d36`  |
| 1698   | Layout 1 | `fadfefe74d36`  |
| 1690   | Layout 1 | `fadfefe74d36`  |
| 1685   | Layout 1 | `fadfefe74d36`  |
| 1680   | Layout 1 | `fadfefe74d36`  |
| 1674   | Layout 1 | `fadfefe74d36`  |
| 1668   | Layout 1 | `fadfefe74d36`  |
| 1659   | Layout 1 | `fadfefe74d36`  |
| 1649   | Layout 1 | `fadfefe74d36`  |
| 1642   | Layout 1 | `fadfefe74d36`  |
| 1636   | Layout 1 | `fadfefe74d36`  |
| 1628   | Layout 1 | `fadfefe74d36`  |
| 1622   | Layout 1 | `fadfefe74d36`  |
| 1614   | Layout 1 | `fadfefe74d36`  |
| 1608   | Layout 1 | `fadfefe74d36`  |
| 1602   | Layout 1 | `fadfefe74d36`  |
| 1598   | Layout 1 | `fadfefe74d36`  |
| 1594   | Layout 1 | `fadfefe74d36`  |
| 1590   | Layout 1 | `fadfefe74d36`  |
| 1587   | Layout 1 | `fadfefe74d36`  |
| 1584   | Layout 1 | `fadfefe74d36`  |
| 1579   | Layout 1 | `fadfefe74d36`  |
| 1572   | Layout 1 | `fadfefe74d36`  |
| 1565   | Layout 1 | `fadfefe74d36`  |
| 1559   | Layout 1 | `fadfefe74d36`  |
| 1554   | Layout 1 | `fadfefe74d36`  |
| 1547   | Layout 1 | `fadfefe74d36`  |
| 1537   | Layout 1 | `fadfefe74d36`  |
| 1529   | Layout 1 | `fadfefe74d36`  |
| 1524   | Layout 1 | `fadfefe74d36`  |
| 1519   | Layout 1 | `fadfefe74d36`  |
| 1509   | Layout 1 | `fadfefe74d36`  |
| 1506   | Layout 1 | `fadfefe74d36`  |
| 1504   | Layout 1 | `fadfefe74d36`  |
| 1500   | Layout 1 | `fadfefe74d36`  |
| 1493   | Layout 1 | `fadfefe74d36`  |
| 1489   | Layout 1 | `fadfefe74d36`  |
| 1485   | Layout 1 | `fadfefe74d36`  |
| 1481   | Layout 1 | `fadfefe74d36`  |
| 1474   | Layout 1 | `fadfefe74d36`  |
| 1466   | Layout 1 | `fadfefe74d36`  |
| 1462   | Layout 1 | `fadfefe74d36`  |
| 1459   | Layout 1 | `fadfefe74d36`  |
| 1453   | Layout 1 | `fadfefe74d36`  |
| 1450   | Layout 1 | `fadfefe74d36`  |
| 1445   | Layout 1 | `fadfefe74d36`  |
| 1439   | Layout 1 | `fadfefe74d36`  |
| 1433   | Layout 1 | `fadfefe74d36`  |
| 1430   | Layout 1 | `fadfefe74d36`  |
| 1426   | Layout 1 | `fadfefe74d36`  |
| 1421   | Layout 1 | `fadfefe74d36`  |
| 1417   | Layout 1 | `fadfefe74d36`  |
| 1416   | Layout 1 | `fadfefe74d36`  |
| 1409   | Layout 1 | `fadfefe74d36`  |
| 1405   | Layout 1 | `fadfefe74d36`  |
| 1401   | Layout 1 | `fadfefe74d36`  |
| 1396   | Layout 1 | `fadfefe74d36`  |
| 1391   | Layout 1 | `fadfefe74d36`  |
| 1390   | Layout 1 | `fadfefe74d36`  |
| 1386   | Layout 1 | `fadfefe74d36`  |
| 1381   | Layout 1 | `fadfefe74d36`  |
| 1379   | Layout 1 | `fadfefe74d36`  |
| 1372   | Layout 1 | `fadfefe74d36`  |
| 1366   | Layout 1 | `fadfefe74d36`  |
| 1364   | Layout 1 | `fadfefe74d36`  |
| 1363   | Layout 1 | `fadfefe74d36`  |
| 1360   | Layout 1 | `fadfefe74d36`  |
| 1358   | Layout 1 | `fadfefe74d36`  |
| 1355   | Layout 1 | `fadfefe74d36`  |
| 1351   | Layout 1 | `fadfefe74d36`  |
| 1348   | Layout 1 | `fadfefe74d36`  |
| 1346   | Layout 1 | `fadfefe74d36`  |
| 1341   | Layout 1 | `fadfefe74d36`  |
| 1340   | Layout 1 | `fadfefe74d36`  |
| 1338   | Layout 1 | `fadfefe74d36`  |
| 1335   | Layout 1 | `fadfefe74d36`  |
| 1333   | Layout 1 | `fadfefe74d36`  |
| 1329   | Layout 1 | `fadfefe74d36`  |
| 1327   | Layout 1 | `fadfefe74d36`  |
| 1324   | Layout 1 | `fadfefe74d36`  |
| 1321   | Layout 1 | `fadfefe74d36`  |
| 1319   | Layout 1 | `fadfefe74d36`  |
| 1318   | Layout 1 | `fadfefe74d36`  |
| 1316   | Layout 1 | `fadfefe74d36`  |
| 1313   | Layout 1 | `fadfefe74d36`  |
| 1311   | Layout 1 | `fadfefe74d36`  |
| 1309   | Layout 1 | `fadfefe74d36`  |
| 1304   | Layout 1 | `fadfefe74d36`  |
| 1292   | Layout 1 | `fadfefe74d36`  |
| 1286   | Layout 1 | `fadfefe74d36`  |
| 1280   | No file  | `fadfefe74d36`  |
| 1276   | Layout 1 | `fadfefe74d36`  |
| 1267   | Layout 1 | `fadfefe74d36`  |
| 1261   | Layout 1 | `fadfefe74d36`  |
| 1256   | No file  | `fadfefe74d36`  |
| 1250   | No file  | `fadfefe74d36`  |
| 1246   | No file  | `fadfefe74d36`  |
| 1239   | No file  | `fadfefe74d36`  |
| 1230   | No file  | `fadfefe74d36`  |
| 1226   | No file  | `fadfefe74d36`  |
| 1220   | No file  | `fadfefe74d36`  |
| 1217   | No file  | `fadfefe74d36`  |
| 1211   | No file  | `fadfefe74d36`  |
| 1210   | No file  | `fadfefe74d36`  |
| 1208   | No file  | `fadfefe74d36`  |
| 1203   | No file  | `fadfefe74d36`  |
| 1197   | No file  | `fadfefe74d36`  |
| 1194   | No file  | `fadfefe74d36`  |
| 1192   | No file  | `fadfefe74d36`  |
| 1187   | No file  | `fadfefe74d36`  |
| 1183   | No file  | `fadfefe74d36`  |
| 1177   | No file  | `fadfefe74d36`  |
| 1173   | No file  | `fadfefe74d36`  |
| 1167   | No file  | `fadfefe74d36`  |
| 1164   | No file  | `fadfefe74d36`  |
| 1156   | No file  | `fadfefe74d36`  |
| 1149   | No file  | `fadfefe74d36`  |
| 1144   | No file  | `fadfefe74d36`  |
| 1137   | No file  | `fadfefe74d36`  |
| 1132   | No file  | `fadfefe74d36`  |
| 1127   | No file  | `fadfefe74d36`  |
| 1122   | No file  | `fadfefe74d36`  |
| 1118   | No file  | `fadfefe74d36`  |
| 1114   | No file  | `fadfefe74d36`  |
| 1109   | No file  | `fadfefe74d36`  |
| 1102   | No file  | `fadfefe74d36`  |
| 1096   | No file  | `fadfefe74d36`  |
| 1088   | No file  | `fadfefe74d36`  |
| 1081   | No file  | `fadfefe74d36`  |
| 1076   | No file  | `fadfefe74d36`  |
| 1069   | No file  | `fadfefe74d36`  |
| 1064   | No file  | `fadfefe74d36`  |
| 1058   | No file  | `fadfefe74d36`  |
| 1051   | No file  | `fadfefe74d36`  |
| 1044   | No file  | `fadfefe74d36`  |
| 1036   | No file  | `fadfefe74d36`  |
| 1026   | No file  | `fadfefe74d36`  |
| 1016   | No file  | `fadfefe74d36`  |
| 1009   | No file  | `fadfefe74d36`  |
| 1005   | No file  | `fadfefe74d36`  |
| 1000   | No file  | `fadfefe74d36`  |
| 998    | No file  | `fadfefe74d36`  |
| 990    | No file  | `fadfefe74d36`  |
| 979    | No file  | `fadfefe74d36`  |
| 972    | No file  | `fadfefe74d36`  |
| 963    | No file  | `fadfefe74d36`  |
| 955    | No file  | `fadfefe74d36`  |
| 946    | No file  | `fadfefe74d36`  |
| 938    | No file  | `fadfefe74d36`  |
| 927    | No file  | `fadfefe74d36`  |
| 911    | No file  | `fadfefe74d36`  |
| 904    | No file  | `fadfefe74d36`  |
| 899    | No file  | `fadfefe74d36`  |
| 894    | No file  | `fadfefe74d36`  |
| 885    | No file  | `fadfefe74d36`  |
| 879    | No file  | `fadfefe74d36`  |
| 872    | No file  | `fadfefe74d36`  |
| 864    | No file  | `fadfefe74d36`  |
| 855    | No file  | `fadfefe74d36`  |
| 853    | No file  | `fadfefe74d36`  |
| 845    | No file  | `fadfefe74d36`  |
| 837    | No file  | `fadfefe74d36`  |
| 829    | No file  | `fadfefe74d36`  |
| 822    | No file  | `fadfefe74d36`  |
| 814    | No file  | `fadfefe74d36`  |
| 805    | No file  | `fadfefe74d36`  |
| 794    | No file  | `fadfefe74d36`  |
| 787    | No file  | `fadfefe74d36`  |
| 780    | No file  | `fadfefe74d36`  |
| 771    | No file  | `fadfefe74d36`  |
| 760    | No file  | `fadfefe74d36`  |
| 748    | No file  | `fadfefe74d36`  |
| 741    | No file  | `fadfefe74d36`  |
| 736    | No file  | `fadfefe74d36`  |
| 731    | No file  | `fadfefe74d36`  |
| 723    | No file  | `fadfefe74d36`  |
| 711    | No file  | `fadfefe74d36`  |
| 707    | No file  | `fadfefe74d36`  |
| 697    | No file  | `fadfefe74d36`  |
| 689    | No file  | `fadfefe74d36`  |
| 683    | No file  | `fadfefe74d36`  |
| 678    | No file  | `fadfefe74d36`  |
| 670    | No file  | `fadfefe74d36`  |
| 661    | No file  | `fadfefe74d36`  |
| 656    | No file  | `fadfefe74d36`  |
| 652    | No file  | `fadfefe74d36`  |
| 643    | No file  | `fadfefe74d36`  |
| 637    | No file  | `fadfefe74d36`  |
| 630    | No file  | `fadfefe74d36`  |
| 627    | No file  | `fadfefe74d36`  |
| 621    | No file  | `fadfefe74d36`  |
| 617    | No file  | `fadfefe74d36`  |
| 615    | No file  | `fadfefe74d36`  |
| 606    | No file  | `fadfefe74d36`  |
| 599    | No file  | `fadfefe74d36`  |
| 592    | No file  | `fadfefe74d36`  |
| 586    | No file  | `fadfefe74d36`  |
| 577    | No file  | `fadfefe74d36`  |
| 569    | No file  | `fadfefe74d36`  |
| 561    | No file  | `fadfefe74d36`  |
| 554    | No file  | `fadfefe74d36`  |
| 542    | No file  | `fadfefe74d36`  |
| 532    | No file  | `fadfefe74d36`  |
| 531    | No file  | `fadfefe74d36`  |
| 526    | No file  | `fadfefe74d36`  |
| 521    | No file  | `fadfefe74d36`  |
| 517    | No file  | `fadfefe74d36`  |
| 510    | No file  | `fadfefe74d36`  |
| 508    | No file  | `fadfefe74d36`  |
| 504    | No file  | `fadfefe74d36`  |
| 497    | No file  | `fadfefe74d36`  |
| 491    | No file  | `fadfefe74d36`  |
| 485    | No file  | `fadfefe74d36`  |
| 478    | No file  | `fadfefe74d36`  |
| 472    | No file  | `fadfefe74d36`  |
| 466    | No file  | `fadfefe74d36`  |
| 457    | No file  | `fadfefe74d36`  |
| 452    | No file  | `fadfefe74d36`  |
| 449    | No file  | `fadfefe74d36`  |
| 435    | No file  | `fadfefe74d36`  |

<!-- versions:end -->

## Companion Files

None. The file has no offset index.

## Layout 1

### File Layout

| Offset  | Type | Field | Notes                                                     |
| ------- | ---- | ----- | --------------------------------------------------------- |
| `+0x00` | u8   | count | Highest `vehicleskill.dbss` `key` + 1; `107` on client 3474 |

## Values per Client

The byte against `vehicleskill.dbss` on every test client that has the
file. The keys run from 1 to the record count with no gap on all of them,
so the byte is also the record count plus one.

| Client | `count` | `vehicleskill.dbss` records | Highest key |
| ------ | ------- | --------------------------- | ----------- |
| 1485   | 72      | 71                          | 71          |
| 1784   | 77      | 76                          | 76          |
| 2107   | 88      | 87                          | 87          |
| 2519   | 95      | 94                          | 94          |
| 3002   | 106     | 105                         | 105         |
| 3251   | 107     | 106                         | 106         |
| 3474   | 107     | 106                         | 106         |

Clients 794 and 1230 have neither file; their skills are in
`vehicleskill.bss`.

## Field Names

The 2016 `gc::VehicleSkillStaticStatusManager` starts with
`unsigned char _count`, followed by `_list`, a fixed array of
`gc::VehicleSkillStaticStatus` indexed by the u8 skill key (31 slots in
2016). Its `insert_StaticStatus` stores each skill at `_list[key]` and then
sets `_count` to `key + 1` when `_count` is not above `key`, so `_count` is
the highest key plus one; a gap in the keys would put it more than one
above the number of skills. The field takes that name. The client Lua on client 3474 agrees:
`panel_worldmap_stablelist`, `panel_dialog_servantmarket_all` and
`panel_dialog_servantmarket_rental_mating_all` count a servant's learned
skills with `for skillIdx = 1, vehicleSkillStaticStatus_skillCount() - 1`,
and `panel_window_vehicleinfo_all` loops up to the value itself.

## Notes

- The first byte of `vehicleskill.dbss` (`unknown_00` there) holds the
  same value on every client in the table above.
- `count` is a u8 because the skill key is one; it cannot pass 255.
