# `employeeexp.bss` Format

## Purpose

Sailor levelling table. One row per sailor (employee) and level holds the EXP
the sailor needs to reach the next level and, per employee ability, a dice
expression from the trailing string table (`1D2`, `1D5+30`) rolled for that
ability on level-up. The top level of each sailor has no growth and a
placeholder EXP value.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File              | Bytes  | Records | Row bytes |
| ------ | -------------- | ----------------- | ------ | ------- | --------- |
| 2      | 2743 and later | `employeeexp.bss` | 21,081 | 230 Row | 89        |
| 1      | 1340 to 2736   | `employeeexp.bss` | 19,237 | 230 Row | 81        |

| Layout | File              | Known            | Unknown        |
| ------ | ----------------- | ---------------- | -------------- |
| 2      | `employeeexp.bss` | 19,927 B (94.5%) | 1,154 B (5.5%) |
| 1      | `employeeexp.bss` | 18,087 B (94.0%) | 1,150 B (6.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `d0551222b474`  |
| 3482   | Layout 2             | `d0551222b474`  |
| 3474   | Layout 2             | `d0551222b474`  |
| 3473   | Layout 2             | `d0551222b474`  |
| 3464   | Layout 2             | `d0551222b474`  |
| 3458   | Layout 2             | `d0551222b474`  |
| 3454   | Layout 2             | `d0551222b474`  |
| 3444   | Layout 2             | `d0551222b474`  |
| 3435   | Layout 2             | `d0551222b474`  |
| 3426   | Layout 2             | `d0551222b474`  |
| 3418   | Layout 2             | `d0551222b474`  |
| 3412   | Layout 2             | `d0551222b474`  |
| 3402   | Layout 2             | `d0551222b474`  |
| 3396   | Layout 2             | `d0551222b474`  |
| 3387   | Layout 2             | `d0551222b474`  |
| 3381   | Layout 2             | `d0551222b474`  |
| 3373   | Layout 2             | `d0551222b474`  |
| 3364   | Layout 2             | `d0551222b474`  |
| 3356   | Layout 2             | `d0551222b474`  |
| 3349   | Layout 2             | `d0551222b474`  |
| 3342   | Layout 2             | `d0551222b474`  |
| 3335   | Layout 2             | `d0551222b474`  |
| 3326   | Layout 2             | `d0551222b474`  |
| 3321   | Layout 2             | `d0551222b474`  |
| 3314   | Layout 2             | `d0551222b474`  |
| 3303   | Layout 2             | `d0551222b474`  |
| 3302   | Layout 2             | `d0551222b474`  |
| 3293   | Layout 2             | `d0551222b474`  |
| 3283   | Layout 2             | `d0551222b474`  |
| 3275   | Layout 2             | `d0551222b474`  |
| 3267   | Layout 2             | `d0551222b474`  |
| 3258   | Layout 2             | `d0551222b474`  |
| 3251   | Layout 2             | `d0551222b474`  |
| 3242   | Layout 2             | `d0551222b474`  |
| 3235   | Layout 2             | `d0551222b474`  |
| 3229   | Layout 2             | `d0551222b474`  |
| 3212   | Layout 2             | `d0551222b474`  |
| 3203   | Layout 2             | `d0551222b474`  |
| 3193   | Layout 2             | `d0551222b474`  |
| 3186   | Layout 2             | `d0551222b474`  |
| 3177   | Layout 2             | `d0551222b474`  |
| 3169   | Layout 2             | `d0551222b474`  |
| 3158   | Layout 2             | `d0551222b474`  |
| 3151   | Layout 2             | `d0551222b474`  |
| 3144   | Layout 2             | `d0551222b474`  |
| 3133   | Layout 2             | `d0551222b474`  |
| 3125   | Layout 2             | `d0551222b474`  |
| 3118   | Layout 2             | `d0551222b474`  |
| 3111   | Layout 2             | `d0551222b474`  |
| 3103   | Layout 2             | `d0551222b474`  |
| 3095   | Layout 2             | `d0551222b474`  |
| 3086   | Layout 2             | `d0551222b474`  |
| 3072   | Layout 2             | `d0551222b474`  |
| 3062   | Layout 2             | `d0551222b474`  |
| 3052   | Layout 2             | `d0551222b474`  |
| 3045   | Layout 2             | `d0551222b474`  |
| 3037   | Layout 2             | `d0551222b474`  |
| 3030   | Layout 2             | `d0551222b474`  |
| 3021   | Layout 2             | `d0551222b474`  |
| 3012   | Layout 2             | `d0551222b474`  |
| 3002   | Layout 2             | `d0551222b474`  |
| 2995   | Layout 2             | `d0551222b474`  |
| 2987   | Layout 2             | `d0551222b474`  |
| 2978   | Layout 2             | `d0551222b474`  |
| 2970   | Layout 2             | `d0551222b474`  |
| 2959   | Layout 2             | `d0551222b474`  |
| 2951   | Layout 2             | `d0551222b474`  |
| 2942   | Layout 2             | `d0551222b474`  |
| 2935   | Layout 2             | `d0551222b474`  |
| 2932   | Layout 2             | `d0551222b474`  |
| 2923   | Layout 2             | `d0551222b474`  |
| 2919   | Layout 2             | `d0551222b474`  |
| 2907   | Layout 2             | `d0551222b474`  |
| 2900   | Layout 2             | `d0551222b474`  |
| 2891   | Layout 2             | `d0551222b474`  |
| 2882   | Layout 2             | `d0551222b474`  |
| 2872   | Layout 2             | `d0551222b474`  |
| 2863   | Layout 2             | `d0551222b474`  |
| 2855   | Layout 2             | `d0551222b474`  |
| 2849   | Layout 2             | `d0551222b474`  |
| 2844   | Layout 2             | `d0551222b474`  |
| 2834   | Layout 2             | `d0551222b474`  |
| 2825   | Layout 2             | `d0551222b474`  |
| 2819   | Layout 2             | `d0551222b474`  |
| 2811   | Layout 2             | `d0551222b474`  |
| 2803   | Layout 2             | `d0551222b474`  |
| 2794   | Layout 2             | `d0551222b474`  |
| 2783   | Layout 2             | `d0551222b474`  |
| 2774   | Layout 2             | `d0551222b474`  |
| 2765   | Layout 2             | `d0551222b474`  |
| 2756   | Layout 2             | `d0551222b474`  |
| 2750   | Layout 2             | `d0551222b474`  |
| 2743   | Layout 2             | `d0551222b474`  |
| 2736   | Layout 1             | `d0551222b474`  |
| 2726   | Layout 1             | `d0551222b474`  |
| 2717   | Layout 1             | `d0551222b474`  |
| 2709   | Layout 1             | `d0551222b474`  |
| 2703   | Layout 1             | `d0551222b474`  |
| 2695   | Layout 1             | `d0551222b474`  |
| 2684   | Layout 1             | `d0551222b474`  |
| 2672   | Layout 1             | `d0551222b474`  |
| 2665   | Layout 1             | `d0551222b474`  |
| 2657   | Layout 1             | `d0551222b474`  |
| 2649   | Layout 1             | `d0551222b474`  |
| 2644   | Layout 1             | `d0551222b474`  |
| 2637   | Layout 1             | `d0551222b474`  |
| 2629   | Layout 1             | `d0551222b474`  |
| 2619   | Layout 1             | `d0551222b474`  |
| 2612   | Layout 1             | `d0551222b474`  |
| 2606   | Layout 1             | `d0551222b474`  |
| 2602   | Layout 1             | `d0551222b474`  |
| 2601   | Layout 1             | `d0551222b474`  |
| 2592   | Layout 1             | `d0551222b474`  |
| 2583   | Layout 1             | `d0551222b474`  |
| 2575   | Layout 1             | `d0551222b474`  |
| 2567   | Layout 1             | `d0551222b474`  |
| 2560   | Layout 1             | `d0551222b474`  |
| 2553   | Layout 1             | `d0551222b474`  |
| 2545   | Layout 1             | `d0551222b474`  |
| 2538   | Layout 1             | `d0551222b474`  |
| 2529   | Layout 1             | `d0551222b474`  |
| 2519   | Layout 1             | `d0551222b474`  |
| 2513   | Layout 1             | `d0551222b474`  |
| 2510   | Layout 1             | `d0551222b474`  |
| 2507   | Layout 1             | `d0551222b474`  |
| 2503   | Layout 1             | `d0551222b474`  |
| 2498   | Layout 1             | `d0551222b474`  |
| 2492   | Layout 1             | `d0551222b474`  |
| 2487   | Layout 1             | `d0551222b474`  |
| 2480   | Layout 1             | `d0551222b474`  |
| 2474   | Layout 1             | `d0551222b474`  |
| 2468   | Layout 1             | `d0551222b474`  |
| 2460   | Layout 1             | `d0551222b474`  |
| 2453   | Layout 1             | `d0551222b474`  |
| 2444   | Layout 1             | `d0551222b474`  |
| 2438   | Layout 1             | `d0551222b474`  |
| 2434   | Layout 1             | `d0551222b474`  |
| 2429   | Layout 1             | `d0551222b474`  |
| 2421   | Layout 1             | `d0551222b474`  |
| 2414   | Layout 1             | `d0551222b474`  |
| 2407   | Layout 1             | `d0551222b474`  |
| 2401   | Layout 1             | `d0551222b474`  |
| 2397   | Layout 1             | `d0551222b474`  |
| 2393   | Layout 1             | `d0551222b474`  |
| 2384   | Layout 1             | `d0551222b474`  |
| 2378   | Layout 1             | `d0551222b474`  |
| 2372   | Layout 1             | `d0551222b474`  |
| 2358   | Layout 1             | `d0551222b474`  |
| 2352   | Layout 1             | `d0551222b474`  |
| 2347   | Layout 1             | `d0551222b474`  |
| 2343   | Layout 1             | `d0551222b474`  |
| 2335   | Layout 1             | `d0551222b474`  |
| 2327   | Layout 1             | `d0551222b474`  |
| 2324   | Layout 1             | `d0551222b474`  |
| 2319   | Layout 1             | `d0551222b474`  |
| 2313   | Layout 1             | `d0551222b474`  |
| 2308   | Layout 1             | `d0551222b474`  |
| 2302   | Layout 1             | `d0551222b474`  |
| 2295   | Layout 1             | `d0551222b474`  |
| 2290   | Layout 1             | `d0551222b474`  |
| 2284   | Layout 1             | `d0551222b474`  |
| 2276   | Layout 1             | `d0551222b474`  |
| 2269   | Layout 1             | `d0551222b474`  |
| 2259   | Layout 1             | `d0551222b474`  |
| 2250   | Layout 1             | `d0551222b474`  |
| 2243   | Layout 1             | `d0551222b474`  |
| 2235   | Layout 1             | `d0551222b474`  |
| 2229   | Layout 1             | `d0551222b474`  |
| 2224   | Layout 1             | `d0551222b474`  |
| 2218   | Layout 1             | `d0551222b474`  |
| 2215   | Layout 1             | `d0551222b474`  |
| 2207   | Layout 1             | `d0551222b474`  |
| 2203   | Layout 1             | `d0551222b474`  |
| 2196   | Layout 1             | `d0551222b474`  |
| 2192   | Layout 1             | `d0551222b474`  |
| 2189   | Layout 1             | `d0551222b474`  |
| 2183   | Layout 1             | `d0551222b474`  |
| 2179   | Layout 1             | `d0551222b474`  |
| 2171   | Layout 1             | `d0551222b474`  |
| 2163   | Layout 1             | `d0551222b474`  |
| 2156   | Layout 1             | `d0551222b474`  |
| 2151   | Layout 1             | `d0551222b474`  |
| 2147   | Layout 1             | `d0551222b474`  |
| 2142   | Layout 1             | `d0551222b474`  |
| 2138   | Layout 1             | `d0551222b474`  |
| 2134   | Layout 1             | `d0551222b474`  |
| 2130   | Layout 1             | `d0551222b474`  |
| 2122   | Layout 1             | `d0551222b474`  |
| 2107   | Layout 1             | `d0551222b474`  |
| 2098   | Layout 1             | `d0551222b474`  |
| 2089   | Layout 1             | `d0551222b474`  |
| 2081   | Layout 1             | `d0551222b474`  |
| 2073   | Layout 1             | `d0551222b474`  |
| 2067   | Layout 1             | `d0551222b474`  |
| 2063   | Layout 1             | `d0551222b474`  |
| 2059   | Layout 1             | `d0551222b474`  |
| 2052   | Layout 1             | `d0551222b474`  |
| 2044   | Layout 1             | `d0551222b474`  |
| 2039   | Layout 1             | `d0551222b474`  |
| 2032   | Layout 1             | `d0551222b474`  |
| 2025   | Layout 1             | `d0551222b474`  |
| 2011   | Layout 1             | `d0551222b474`  |
| 2005   | Layout 1             | `d0551222b474`  |
| 2000   | Layout 1             | `d0551222b474`  |
| 1996   | Layout 1             | `d0551222b474`  |
| 1991   | Layout 1             | `d0551222b474`  |
| 1985   | Layout 1             | `d0551222b474`  |
| 1980   | Layout 1             | `d0551222b474`  |
| 1969   | Layout 1             | `d0551222b474`  |
| 1964   | Layout 1             | `d0551222b474`  |
| 1958   | Layout 1             | `d0551222b474`  |
| 1950   | Layout 1             | `d0551222b474`  |
| 1945   | Layout 1             | `d0551222b474`  |
| 1937   | Layout 1             | `d0551222b474`  |
| 1933   | Layout 1             | `d0551222b474`  |
| 1927   | Layout 1             | `d0551222b474`  |
| 1921   | Layout 1             | `d0551222b474`  |
| 1914   | Layout 1             | `d0551222b474`  |
| 1908   | Layout 1             | `d0551222b474`  |
| 1897   | Layout 1             | `d0551222b474`  |
| 1892   | Layout 1             | `d0551222b474`  |
| 1886   | Layout 1             | `d0551222b474`  |
| 1881   | Layout 1             | `d0551222b474`  |
| 1871   | Layout 1             | `d0551222b474`  |
| 1866   | Layout 1             | `d0551222b474`  |
| 1862   | Layout 1             | `d0551222b474`  |
| 1854   | Layout 1             | `d0551222b474`  |
| 1846   | Layout 1             | `d0551222b474`  |
| 1838   | Layout 1             | `d0551222b474`  |
| 1832   | Layout 1             | `d0551222b474`  |
| 1826   | Layout 1             | `d0551222b474`  |
| 1822   | Layout 1             | `d0551222b474`  |
| 1818   | Layout 1             | `d0551222b474`  |
| 1804   | Layout 1             | `d0551222b474`  |
| 1794   | Layout 1             | `d0551222b474`  |
| 1790   | Layout 1             | `d0551222b474`  |
| 1784   | Layout 1             | `d0551222b474`  |
| 1774   | Layout 1             | `d0551222b474`  |
| 1771   | Layout 1             | `d0551222b474`  |
| 1762   | Layout 1             | `d0551222b474`  |
| 1759   | Layout 1             | `d0551222b474`  |
| 1754   | Layout 1             | `d0551222b474`  |
| 1749   | Layout 1             | `d0551222b474`  |
| 1743   | Layout 1             | `d0551222b474`  |
| 1737   | Layout 1             | `d0551222b474`  |
| 1731   | Layout 1             | `d0551222b474`  |
| 1725   | Layout 1             | `d0551222b474`  |
| 1717   | Layout 1             | `d0551222b474`  |
| 1710   | Layout 1             | `d0551222b474`  |
| 1704   | Layout 1             | `d0551222b474`  |
| 1698   | Layout 1             | `d0551222b474`  |
| 1690   | Layout 1             | `d0551222b474`  |
| 1685   | Layout 1             | `d0551222b474`  |
| 1680   | Layout 1             | `d0551222b474`  |
| 1674   | Layout 1             | `d0551222b474`  |
| 1668   | Layout 1             | `d0551222b474`  |
| 1659   | Layout 1             | `d0551222b474`  |
| 1649   | Layout 1             | `d0551222b474`  |
| 1642   | Layout 1             | `d0551222b474`  |
| 1636   | Layout 1             | `d0551222b474`  |
| 1628   | Layout 1             | `d0551222b474`  |
| 1622   | Layout 1             | `d0551222b474`  |
| 1614   | Layout 1             | `d0551222b474`  |
| 1608   | Layout 1             | `d0551222b474`  |
| 1602   | Layout 1             | `d0551222b474`  |
| 1598   | Layout 1             | `d0551222b474`  |
| 1594   | Layout 1             | `d0551222b474`  |
| 1590   | Layout 1             | `d0551222b474`  |
| 1587   | Layout 1             | `d0551222b474`  |
| 1584   | Layout 1             | `d0551222b474`  |
| 1579   | Layout 1             | `d0551222b474`  |
| 1572   | Layout 1             | `d0551222b474`  |
| 1565   | Layout 1             | `d0551222b474`  |
| 1559   | Layout 1             | `d0551222b474`  |
| 1554   | Layout 1             | `d0551222b474`  |
| 1547   | Layout 1             | `d0551222b474`  |
| 1537   | Layout 1             | `d0551222b474`  |
| 1529   | Layout 1             | `d0551222b474`  |
| 1524   | Layout 1             | `d0551222b474`  |
| 1519   | Layout 1             | `d0551222b474`  |
| 1509   | Layout 1             | `d0551222b474`  |
| 1506   | Layout 1             | `d0551222b474`  |
| 1504   | Layout 1             | `d0551222b474`  |
| 1500   | Layout 1             | `d0551222b474`  |
| 1493   | Layout 1             | `d0551222b474`  |
| 1489   | Layout 1             | `d0551222b474`  |
| 1485   | Layout 1             | `d0551222b474`  |
| 1481   | Layout 1             | `d0551222b474`  |
| 1474   | Layout 1             | `d0551222b474`  |
| 1466   | Layout 1             | `d0551222b474`  |
| 1462   | Layout 1             | `d0551222b474`  |
| 1459   | Layout 1             | `d0551222b474`  |
| 1453   | Layout 1             | `d0551222b474`  |
| 1450   | Layout 1             | `d0551222b474`  |
| 1445   | Layout 1             | `d0551222b474`  |
| 1439   | Layout 1             | `d0551222b474`  |
| 1433   | Layout 1             | `d0551222b474`  |
| 1430   | Layout 1             | `d0551222b474`  |
| 1426   | Layout 1             | `d0551222b474`  |
| 1421   | Layout 1             | `d0551222b474`  |
| 1417   | Layout 1             | `d0551222b474`  |
| 1416   | Layout 1             | `d0551222b474`  |
| 1409   | Layout 1             | `d0551222b474`  |
| 1405   | Layout 1             | `d0551222b474`  |
| 1401   | Layout 1             | `d0551222b474`  |
| 1396   | Layout 1             | `d0551222b474`  |
| 1391   | Layout 1             | `d0551222b474`  |
| 1390   | Layout 1             | `d0551222b474`  |
| 1386   | Layout 1             | `d0551222b474`  |
| 1381   | Layout 1             | `d0551222b474`  |
| 1379   | Layout 1             | `d0551222b474`  |
| 1372   | Layout 1             | `d0551222b474`  |
| 1366   | Layout 1             | `d0551222b474`  |
| 1364   | Layout 1             | `d0551222b474`  |
| 1363   | Layout 1             | `d0551222b474`  |
| 1360   | Layout 1             | `d0551222b474`  |
| 1358   | Layout 1             | `d0551222b474`  |
| 1355   | Layout 1             | `d0551222b474`  |
| 1351   | Layout 1             | `d0551222b474`  |
| 1348   | Layout 1             | `d0551222b474`  |
| 1346   | Layout 1             | `d0551222b474`  |
| 1341   | Layout 1             | `d0551222b474`  |
| 1340   | Layout 1             | `d0551222b474`  |
| 1338   | No documented layout | `d0551222b474`  |
| 1335   | No documented layout | `d0551222b474`  |
| 1333   | No documented layout | `d0551222b474`  |
| 1329   | No documented layout | `d0551222b474`  |
| 1327   | No documented layout | `d0551222b474`  |
| 1324   | No documented layout | `d0551222b474`  |
| 1321   | No documented layout | `d0551222b474`  |
| 1319   | No documented layout | `d0551222b474`  |
| 1318   | No documented layout | `d0551222b474`  |
| 1316   | No documented layout | `d0551222b474`  |
| 1313   | No documented layout | `d0551222b474`  |
| 1311   | No documented layout | `d0551222b474`  |
| 1309   | No documented layout | `d0551222b474`  |
| 1304   | No documented layout | `d0551222b474`  |
| 1292   | No documented layout | `d0551222b474`  |
| 1286   | No documented layout | `d0551222b474`  |
| 1280   | No documented layout | `d0551222b474`  |
| 1276   | No documented layout | `d0551222b474`  |
| 1267   | No documented layout | `d0551222b474`  |
| 1261   | No documented layout | `d0551222b474`  |
| 1256   | No documented layout | `d0551222b474`  |
| 1250   | No documented layout | `d0551222b474`  |
| 1246   | No documented layout | `d0551222b474`  |
| 1239   | No documented layout | `d0551222b474`  |
| 1230   | No file              | `d0551222b474`  |
| 1226   | No file              | `d0551222b474`  |
| 1220   | No file              | `d0551222b474`  |
| 1217   | No file              | `d0551222b474`  |
| 1211   | No file              | `d0551222b474`  |
| 1210   | No file              | `d0551222b474`  |
| 1208   | No file              | `d0551222b474`  |
| 1203   | No file              | `d0551222b474`  |
| 1197   | No file              | `d0551222b474`  |
| 1194   | No file              | `d0551222b474`  |
| 1192   | No file              | `d0551222b474`  |
| 1187   | No file              | `d0551222b474`  |
| 1183   | No file              | `d0551222b474`  |
| 1177   | No file              | `d0551222b474`  |
| 1173   | No file              | `d0551222b474`  |
| 1167   | No file              | `d0551222b474`  |
| 1164   | No file              | `d0551222b474`  |
| 1156   | No file              | `d0551222b474`  |
| 1149   | No file              | `d0551222b474`  |
| 1144   | No file              | `d0551222b474`  |
| 1137   | No file              | `d0551222b474`  |
| 1132   | No file              | `d0551222b474`  |
| 1127   | No file              | `d0551222b474`  |
| 1122   | No file              | `d0551222b474`  |
| 1118   | No file              | `d0551222b474`  |
| 1114   | No file              | `d0551222b474`  |
| 1109   | No file              | `d0551222b474`  |
| 1102   | No file              | `d0551222b474`  |
| 1096   | No file              | `d0551222b474`  |
| 1088   | No file              | `d0551222b474`  |
| 1081   | No file              | `d0551222b474`  |
| 1076   | No file              | `d0551222b474`  |
| 1069   | No file              | `d0551222b474`  |
| 1064   | No file              | `d0551222b474`  |
| 1058   | No file              | `d0551222b474`  |
| 1051   | No file              | `d0551222b474`  |
| 1044   | No file              | `d0551222b474`  |
| 1036   | No file              | `d0551222b474`  |
| 1026   | No file              | `d0551222b474`  |
| 1016   | No file              | `d0551222b474`  |
| 1009   | No file              | `d0551222b474`  |
| 1005   | No file              | `d0551222b474`  |
| 1000   | No file              | `d0551222b474`  |
| 998    | No file              | `d0551222b474`  |
| 990    | No file              | `d0551222b474`  |
| 979    | No file              | `d0551222b474`  |
| 972    | No file              | `d0551222b474`  |
| 963    | No file              | `d0551222b474`  |
| 955    | No file              | `d0551222b474`  |
| 946    | No file              | `d0551222b474`  |
| 938    | No file              | `d0551222b474`  |
| 927    | No file              | `d0551222b474`  |
| 911    | No file              | `d0551222b474`  |
| 904    | No file              | `d0551222b474`  |
| 899    | No file              | `d0551222b474`  |
| 894    | No file              | `d0551222b474`  |
| 885    | No file              | `d0551222b474`  |
| 879    | No file              | `d0551222b474`  |
| 872    | No file              | `d0551222b474`  |
| 864    | No file              | `d0551222b474`  |
| 855    | No file              | `d0551222b474`  |
| 853    | No file              | `d0551222b474`  |
| 845    | No file              | `d0551222b474`  |
| 837    | No file              | `d0551222b474`  |
| 829    | No file              | `d0551222b474`  |
| 822    | No file              | `d0551222b474`  |
| 814    | No file              | `d0551222b474`  |
| 805    | No file              | `d0551222b474`  |
| 794    | No file              | `d0551222b474`  |
| 787    | No file              | `d0551222b474`  |
| 780    | No file              | `d0551222b474`  |
| 771    | No file              | `d0551222b474`  |
| 760    | No file              | `d0551222b474`  |
| 748    | No file              | `d0551222b474`  |
| 741    | No file              | `d0551222b474`  |
| 736    | No file              | `d0551222b474`  |
| 731    | No file              | `d0551222b474`  |
| 723    | No file              | `d0551222b474`  |
| 711    | No file              | `d0551222b474`  |
| 707    | No file              | `d0551222b474`  |
| 697    | No file              | `d0551222b474`  |
| 689    | No file              | `d0551222b474`  |
| 683    | No file              | `d0551222b474`  |
| 678    | No file              | `d0551222b474`  |
| 670    | No file              | `d0551222b474`  |
| 661    | No file              | `d0551222b474`  |
| 656    | No file              | `d0551222b474`  |
| 652    | No file              | `d0551222b474`  |
| 643    | No file              | `d0551222b474`  |
| 637    | No file              | `d0551222b474`  |
| 630    | No file              | `d0551222b474`  |
| 627    | No file              | `d0551222b474`  |
| 621    | No file              | `d0551222b474`  |
| 617    | No file              | `d0551222b474`  |
| 615    | No file              | `d0551222b474`  |
| 606    | No file              | `d0551222b474`  |
| 599    | No file              | `d0551222b474`  |
| 592    | No file              | `d0551222b474`  |
| 586    | No file              | `d0551222b474`  |
| 577    | No file              | `d0551222b474`  |
| 569    | No file              | `d0551222b474`  |
| 561    | No file              | `d0551222b474`  |
| 554    | No file              | `d0551222b474`  |
| 542    | No file              | `d0551222b474`  |
| 532    | No file              | `d0551222b474`  |
| 531    | No file              | `d0551222b474`  |
| 526    | No file              | `d0551222b474`  |
| 521    | No file              | `d0551222b474`  |
| 517    | No file              | `d0551222b474`  |
| 510    | No file              | `d0551222b474`  |
| 508    | No file              | `d0551222b474`  |
| 504    | No file              | `d0551222b474`  |
| 497    | No file              | `d0551222b474`  |
| 491    | No file              | `d0551222b474`  |
| 485    | No file              | `d0551222b474`  |
| 478    | No file              | `d0551222b474`  |
| 472    | No file              | `d0551222b474`  |
| 466    | No file              | `d0551222b474`  |
| 457    | No file              | `d0551222b474`  |
| 452    | No file              | `d0551222b474`  |
| 449    | No file              | `d0551222b474`  |
| 435    | No file              | `d0551222b474`  |

<!-- versions:end -->

## Companion Files

The format is self-contained: no offset table, the dice text lives in the
file's own string table.

| File                       | Required | Role                                                                                 |
| -------------------------- | -------- | ------------------------------------------------------------------------------------ |
| `employeestaticstatus.bss` | Optional | Same 230 `(level, employee_key)` keys; its rows link `employee_key` to the sailor's character key |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table tail of `npcsimply.bss` and `plantexchangegroup.bss`
(`_common/pabr_strings.py`), with one empty u32 between the rows and the table.

| Offset              | Type         | Field              | Notes                                                                         |
| ------------------- | ------------ | ------------------ | ----------------------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                                                  |
| `+0x04`             | u32          | count              | Number of rows; 230 on client 3458 (23 sailors x 10 levels)                   |
| `+0x08`             | Row[count]   | rows               | See Row                                                                       |
| `rows+0x00`         | u32          | unknown_after_rows | Always `0`; read as an empty counted table, like the `exploration.bss` footer |
| `rows+0x04`         | String Table | string_table       | See String Table                                                              |
| `string_table+0x00` | u32          | string_table_start | Offset of the string table; equals the end of `unknown_after_rows`            |
| `string_table+0x04` | u32          | zero               | Always 0                                                                      |

The file tiles with no gaps: the rows end 4 bytes before `string_table_start`,
and the string table ends exactly at EOF - 8. The parser rejects a file where
this does not hold, since every field would then be suspect. Earlier versions
of this doc called `unknown_after_rows` `footer`.

Rows run level by level (all level 1 rows, then level 2, ...); inside a level
the `employee_key` order is 23 down to 8, then 1 up to 7.

### Row (89 bytes)

Fields are unaligned.

| Offset  | Type    | Field             | Notes                                                                                                                      |
| ------- | ------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `+0x00` | u8      | unknown_00        | Always `0`; the same lead byte as `fairyupgraderate.bss` rows                                                              |
| `+0x01` | u16     | level             | 1 to 10                                                                                                                    |
| `+0x03` | u16     | employee_key      | Sailor key, 1 to 23; together with `level` unique per row                                                                  |
| `+0x05` | u32     | exp_to_next_level | EXP from this level to the next; `1000` on level 10, see Notes                                                             |
| `+0x09` | u32     | unknown_09        | Always `0`                                                                                                                 |
| `+0x0D` | u32[19] | growth_ref        | String table index per employee ability (slot = ability index 0 to 18); `0` is the empty string, the ability does not grow |

### String Table (variable: 4 bytes + strings)

41 strings on client 3458. Index 0 is the empty string, every other entry is a
dice expression `<n>D<sides>` with an optional `+<bonus>` (`1D1`, `1D3+7`,
`1D15+25`). All are stored wide (UTF-16LE).

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 41 on client 3458   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Layout 1

On client 1784 `growth_ref` holds 17 slots (abilities 0 to 16), so the row
is 81 bytes, and the string table follows the rows with no
`unknown_after_rows`. The File Layout and the Row differ from Layout 2.

### File Layout

| Offset              | Type         | Field              | Notes                                                |
| ------------------- | ------------ | ------------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                         |
| `+0x04`             | u32          | count              | 230 on client 1784                                   |
| `+0x08`             | Row[count]   | rows               | See Row                                              |
| `rows+0x00`         | String Table | string_table       |                                                      |
| `string_table+0x00` | u32          | string_table_start | Offset of the string table; equals the end of `rows` |
| `string_table+0x04` | u32          | zero               |                                                      |

### Row (81 bytes)

| Offset  | Type    | Field             | Notes                                                                 |
| ------- | ------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u8      | unknown_00        | `0` on every row (client 1784)                                        |
| `+0x01` | u16     | level             |                                                                       |
| `+0x03` | u16     | employee_key      |                                                                       |
| `+0x05` | u32     | exp_to_next_level | The same on every row as on client 3473                               |
| `+0x09` | u32     | unknown_09        | `0` on every row (client 1784)                                        |
| `+0x0D` | u32[17] | growth_ref        | Slots 0 to 16; every slot but 15 holds the same strings as on client 3473 |

## Growth by Ability

Only seven ability slots are used on client 3458:

| Ability index | Rows using it | Notes                                                                                   |
| ------------- | ------------- | --------------------------------------------------------------------------------------- |
| 6, 7          | 207           | Endurance, Wits; every row below the top level                                          |
| 8, 9          | 201           | Awareness, Strength; every row below the top level except sailor 18 on levels 1, 2, 4, 5, 7 and 8 |
| 14, 15, 16    | 36            | Focus, Force, Vision; sailors 5, 8, 15 and 20 only; Vision also rolls large dice (`1D5+30`, `1D15+25`)|

The names come from `employeestaticstatus.bss`, where they are checked
against the Manage Sailors window (see that doc). The client Lua names the
abilities (`__eEmployeeAbility_Servant_*` and others) but their numbers live
in the game binary, so the link is that every growing type is one the
`employeestaticstatus.bss` row of the same sailor and level has, and the
level 6 checks in the Notes, where base plus these dice gives the window's
value stat by stat.

## EXP Curves

Every sailor follows one of four curves on client 3458 (level 1 to 9, then the
level 10 placeholder):

| Level 1 EXP | Levels 1 to 9                                                         | Sailors                                   |
| ----------- | --------------------------------------------------------------------- | ----------------------------------------- |
| 700         | 700, 1050, 1575, 3150, 6300, 12600, 37800, 113400, 340200             | 2, 11, 13                                 |
| 1000        | 1000, 1500, 2250, 4500, 9000, 18000, 54000, 162000, 486000            | 1, 4, 7, 10, 17, 19, 21                   |
| 1000        | Same as above but level 9 is 388800                                   | 22, 23                                    |
| 1300        | 1300, 1950, 2925, 5850, 11700, 23400, 70200, 210600, 631800           | 3, 5, 6, 8, 9, 12, 14, 15, 16, 18, 20     |

Each curve steps x1.5, x1.5, x2, x2, x2, x3, x3, x3 from level 1.

## Notes

- The game calls employees sailors: `employeename.dbss` holds sailor names
  (Guile, Tails), and the client Lua (`panel_window_sailormanager_all*.luac`)
  reads them through `ToClient_getEmployeeWrapperByIndex`, `getLevel` and
  `getExperienceRate`.
- `employee_key` maps to a character key through `employeestaticstatus.bss`:
  sailors 1 to 20 are the plain `Sailor` NPCs 59053 to 59072, 21 is Arkahn
  (59101), 22 is Hetario (59227) and 23 is Pacuna (59228). Every level row of a
  sailor there carries the same character key, which is why `employee_key` is
  the sailor and `level` the level, not the other way round.
- Level 10 is the top level: it is the last row of every sailor, its
  `exp_to_next_level` is `1000` for all 23 sailors, which breaks every curve,
  and it has no growth dice. Read as a placeholder.
- The abilities that grow are always a subset of the abilities the same
  `(level, employee_key)` row of `employeestaticstatus.bss` gives a nonzero
  value. That file stores abilities as `[u8 ability index][u32 value]` pairs
  using the same indices 0 to 18, with 19 as the empty slot; this is what ties
  `growth_ref` slot N to ability index N.
- The u32 at `+0x09` comes before ability 0 and is zero everywhere. Read as
  `growth_ref` slot 0 the indices would be one off from
  `employeestaticstatus.bss` on every row.
- The dice are rolls added to the ability on each level-up, one point = 0.1%
  (stored `1000` in `employeestaticstatus.bss`). The row for level N is
  rolled when reaching level N + 1, and the static file keeps the level 1
  base on every level. Checked in game on two level 6 sailors (2026-10-06):
  base plus the level 1 to 5 dice gives the window's value on all eight
  ship stats, e.g. Confident (`9`) Awareness 3.0% plus
  `1D2+2, 1D2+2, 1D3+2, 1D2+3, 1D2+3` (1.7 to 2.3) reads 5.0%, and
  Treasure-Seeking (`7`) Awareness 4.0% plus `1, 1, 1D2+1, 1D2, 1D2` (0.6
  to 0.9) reads 4.7%.

## Open Questions

### Sailor Names

The table shows `employee_key`. A name column needs the character key from
`employeestaticstatus.bss` (a shared sailor key to character lookup) and LOC
type 6 for that key.
