# `bgmstatesa.bss` Format

## Purpose

The background music states of Shadow Arena (`SA`). A PABR list of rows;
each row names the audio event the client posts for one game condition,
such as `Set_State_SA_States_Login` for `Login`. On client 3482 it holds
16 conditions, from the login screen to the arena modes (`ArenaTension`,
`DeathMatch_Tension`, `Trio_Ascention`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------- | ----- | ------- | --------- |
| 2      | 1886 and later | `bgmstatesa.bss` | 1,228 | 16 Row  | 14        |
| 1      | 1267 to 1881   | `bgmstatesa.bss` | 498   | 7 Row   | 18        |

| Layout | File             | Known           | Unknown     |
| ------ | ---------------- | --------------- | ----------- |
| 2      | `bgmstatesa.bss` | 1,164 B (94.8%) | 64 B (5.2%) |
| 1      | `bgmstatesa.bss` | 498 B (100.0%)  | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `ccce9ebd38aa`  |
| 3482   | Layout 2 | `ccce9ebd38aa`  |
| 3474   | Layout 2 | `ccce9ebd38aa`  |
| 3473   | Layout 2 | `ccce9ebd38aa`  |
| 3464   | Layout 2 | `ccce9ebd38aa`  |
| 3458   | Layout 2 | `ccce9ebd38aa`  |
| 3454   | Layout 2 | `ccce9ebd38aa`  |
| 3444   | Layout 2 | `ccce9ebd38aa`  |
| 3435   | Layout 2 | `ccce9ebd38aa`  |
| 3426   | Layout 2 | `ccce9ebd38aa`  |
| 3418   | Layout 2 | `ccce9ebd38aa`  |
| 3412   | Layout 2 | `ccce9ebd38aa`  |
| 3402   | Layout 2 | `ccce9ebd38aa`  |
| 3396   | Layout 2 | `ccce9ebd38aa`  |
| 3387   | Layout 2 | `ccce9ebd38aa`  |
| 3381   | Layout 2 | `ccce9ebd38aa`  |
| 3373   | Layout 2 | `ccce9ebd38aa`  |
| 3364   | Layout 2 | `ccce9ebd38aa`  |
| 3356   | Layout 2 | `ccce9ebd38aa`  |
| 3349   | Layout 2 | `ccce9ebd38aa`  |
| 3342   | Layout 2 | `ccce9ebd38aa`  |
| 3335   | Layout 2 | `ccce9ebd38aa`  |
| 3326   | Layout 2 | `ccce9ebd38aa`  |
| 3321   | Layout 2 | `ccce9ebd38aa`  |
| 3314   | Layout 2 | `ccce9ebd38aa`  |
| 3303   | Layout 2 | `ccce9ebd38aa`  |
| 3302   | Layout 2 | `ccce9ebd38aa`  |
| 3293   | Layout 2 | `ccce9ebd38aa`  |
| 3283   | Layout 2 | `ccce9ebd38aa`  |
| 3275   | Layout 2 | `ccce9ebd38aa`  |
| 3267   | Layout 2 | `ccce9ebd38aa`  |
| 3258   | Layout 2 | `ccce9ebd38aa`  |
| 3251   | Layout 2 | `ccce9ebd38aa`  |
| 3242   | Layout 2 | `ccce9ebd38aa`  |
| 3235   | Layout 2 | `ccce9ebd38aa`  |
| 3229   | Layout 2 | `ccce9ebd38aa`  |
| 3212   | Layout 2 | `ccce9ebd38aa`  |
| 3203   | Layout 2 | `ccce9ebd38aa`  |
| 3193   | Layout 2 | `ccce9ebd38aa`  |
| 3186   | Layout 2 | `ccce9ebd38aa`  |
| 3177   | Layout 2 | `ccce9ebd38aa`  |
| 3169   | Layout 2 | `ccce9ebd38aa`  |
| 3158   | Layout 2 | `ccce9ebd38aa`  |
| 3151   | Layout 2 | `ccce9ebd38aa`  |
| 3144   | Layout 2 | `ccce9ebd38aa`  |
| 3133   | Layout 2 | `ccce9ebd38aa`  |
| 3125   | Layout 2 | `ccce9ebd38aa`  |
| 3118   | Layout 2 | `ccce9ebd38aa`  |
| 3111   | Layout 2 | `ccce9ebd38aa`  |
| 3103   | Layout 2 | `ccce9ebd38aa`  |
| 3095   | Layout 2 | `ccce9ebd38aa`  |
| 3086   | Layout 2 | `ccce9ebd38aa`  |
| 3072   | Layout 2 | `ccce9ebd38aa`  |
| 3062   | Layout 2 | `ccce9ebd38aa`  |
| 3052   | Layout 2 | `ccce9ebd38aa`  |
| 3045   | Layout 2 | `ccce9ebd38aa`  |
| 3037   | Layout 2 | `ccce9ebd38aa`  |
| 3030   | Layout 2 | `ccce9ebd38aa`  |
| 3021   | Layout 2 | `ccce9ebd38aa`  |
| 3012   | Layout 2 | `ccce9ebd38aa`  |
| 3002   | Layout 2 | `ccce9ebd38aa`  |
| 2995   | Layout 2 | `ccce9ebd38aa`  |
| 2987   | Layout 2 | `ccce9ebd38aa`  |
| 2978   | Layout 2 | `ccce9ebd38aa`  |
| 2970   | Layout 2 | `ccce9ebd38aa`  |
| 2959   | Layout 2 | `ccce9ebd38aa`  |
| 2951   | Layout 2 | `ccce9ebd38aa`  |
| 2942   | Layout 2 | `ccce9ebd38aa`  |
| 2935   | Layout 2 | `ccce9ebd38aa`  |
| 2932   | Layout 2 | `ccce9ebd38aa`  |
| 2923   | Layout 2 | `ccce9ebd38aa`  |
| 2919   | Layout 2 | `ccce9ebd38aa`  |
| 2907   | Layout 2 | `ccce9ebd38aa`  |
| 2900   | Layout 2 | `ccce9ebd38aa`  |
| 2891   | Layout 2 | `ccce9ebd38aa`  |
| 2882   | Layout 2 | `ccce9ebd38aa`  |
| 2872   | Layout 2 | `ccce9ebd38aa`  |
| 2863   | Layout 2 | `ccce9ebd38aa`  |
| 2855   | Layout 2 | `ccce9ebd38aa`  |
| 2849   | Layout 2 | `ccce9ebd38aa`  |
| 2844   | Layout 2 | `ccce9ebd38aa`  |
| 2834   | Layout 2 | `ccce9ebd38aa`  |
| 2825   | Layout 2 | `ccce9ebd38aa`  |
| 2819   | Layout 2 | `ccce9ebd38aa`  |
| 2811   | Layout 2 | `ccce9ebd38aa`  |
| 2803   | Layout 2 | `ccce9ebd38aa`  |
| 2794   | Layout 2 | `ccce9ebd38aa`  |
| 2783   | Layout 2 | `ccce9ebd38aa`  |
| 2774   | Layout 2 | `ccce9ebd38aa`  |
| 2765   | Layout 2 | `ccce9ebd38aa`  |
| 2756   | Layout 2 | `ccce9ebd38aa`  |
| 2750   | Layout 2 | `ccce9ebd38aa`  |
| 2743   | Layout 2 | `ccce9ebd38aa`  |
| 2736   | Layout 2 | `ccce9ebd38aa`  |
| 2726   | Layout 2 | `ccce9ebd38aa`  |
| 2717   | Layout 2 | `ccce9ebd38aa`  |
| 2709   | Layout 2 | `ccce9ebd38aa`  |
| 2703   | Layout 2 | `ccce9ebd38aa`  |
| 2695   | Layout 2 | `ccce9ebd38aa`  |
| 2684   | Layout 2 | `ccce9ebd38aa`  |
| 2672   | Layout 2 | `ccce9ebd38aa`  |
| 2665   | Layout 2 | `ccce9ebd38aa`  |
| 2657   | Layout 2 | `ccce9ebd38aa`  |
| 2649   | Layout 2 | `ccce9ebd38aa`  |
| 2644   | Layout 2 | `ccce9ebd38aa`  |
| 2637   | Layout 2 | `ccce9ebd38aa`  |
| 2629   | Layout 2 | `ccce9ebd38aa`  |
| 2619   | Layout 2 | `ccce9ebd38aa`  |
| 2612   | Layout 2 | `ccce9ebd38aa`  |
| 2606   | Layout 2 | `ccce9ebd38aa`  |
| 2602   | Layout 2 | `ccce9ebd38aa`  |
| 2601   | Layout 2 | `ccce9ebd38aa`  |
| 2592   | Layout 2 | `ccce9ebd38aa`  |
| 2583   | Layout 2 | `ccce9ebd38aa`  |
| 2575   | Layout 2 | `ccce9ebd38aa`  |
| 2567   | Layout 2 | `ccce9ebd38aa`  |
| 2560   | Layout 2 | `ccce9ebd38aa`  |
| 2553   | Layout 2 | `ccce9ebd38aa`  |
| 2545   | Layout 2 | `ccce9ebd38aa`  |
| 2538   | Layout 2 | `ccce9ebd38aa`  |
| 2529   | Layout 2 | `ccce9ebd38aa`  |
| 2519   | Layout 2 | `ccce9ebd38aa`  |
| 2513   | Layout 2 | `ccce9ebd38aa`  |
| 2510   | Layout 2 | `ccce9ebd38aa`  |
| 2507   | Layout 2 | `ccce9ebd38aa`  |
| 2503   | Layout 2 | `ccce9ebd38aa`  |
| 2498   | Layout 2 | `ccce9ebd38aa`  |
| 2492   | Layout 2 | `ccce9ebd38aa`  |
| 2487   | Layout 2 | `ccce9ebd38aa`  |
| 2480   | Layout 2 | `ccce9ebd38aa`  |
| 2474   | Layout 2 | `ccce9ebd38aa`  |
| 2468   | Layout 2 | `ccce9ebd38aa`  |
| 2460   | Layout 2 | `ccce9ebd38aa`  |
| 2453   | Layout 2 | `ccce9ebd38aa`  |
| 2444   | Layout 2 | `ccce9ebd38aa`  |
| 2438   | Layout 2 | `ccce9ebd38aa`  |
| 2434   | Layout 2 | `ccce9ebd38aa`  |
| 2429   | Layout 2 | `ccce9ebd38aa`  |
| 2421   | Layout 2 | `ccce9ebd38aa`  |
| 2414   | Layout 2 | `ccce9ebd38aa`  |
| 2407   | Layout 2 | `ccce9ebd38aa`  |
| 2401   | Layout 2 | `ccce9ebd38aa`  |
| 2397   | Layout 2 | `ccce9ebd38aa`  |
| 2393   | Layout 2 | `ccce9ebd38aa`  |
| 2384   | Layout 2 | `ccce9ebd38aa`  |
| 2378   | Layout 2 | `ccce9ebd38aa`  |
| 2372   | Layout 2 | `ccce9ebd38aa`  |
| 2358   | Layout 2 | `ccce9ebd38aa`  |
| 2352   | Layout 2 | `ccce9ebd38aa`  |
| 2347   | Layout 2 | `ccce9ebd38aa`  |
| 2343   | Layout 2 | `ccce9ebd38aa`  |
| 2335   | Layout 2 | `ccce9ebd38aa`  |
| 2327   | Layout 2 | `ccce9ebd38aa`  |
| 2324   | Layout 2 | `ccce9ebd38aa`  |
| 2319   | Layout 2 | `ccce9ebd38aa`  |
| 2313   | Layout 2 | `ccce9ebd38aa`  |
| 2308   | Layout 2 | `ccce9ebd38aa`  |
| 2302   | Layout 2 | `ccce9ebd38aa`  |
| 2295   | Layout 2 | `ccce9ebd38aa`  |
| 2290   | Layout 2 | `ccce9ebd38aa`  |
| 2284   | Layout 2 | `ccce9ebd38aa`  |
| 2276   | Layout 2 | `ccce9ebd38aa`  |
| 2269   | Layout 2 | `ccce9ebd38aa`  |
| 2259   | Layout 2 | `ccce9ebd38aa`  |
| 2250   | Layout 2 | `ccce9ebd38aa`  |
| 2243   | Layout 2 | `ccce9ebd38aa`  |
| 2235   | Layout 2 | `ccce9ebd38aa`  |
| 2229   | Layout 2 | `ccce9ebd38aa`  |
| 2224   | Layout 2 | `ccce9ebd38aa`  |
| 2218   | Layout 2 | `ccce9ebd38aa`  |
| 2215   | Layout 2 | `ccce9ebd38aa`  |
| 2207   | Layout 2 | `ccce9ebd38aa`  |
| 2203   | Layout 2 | `ccce9ebd38aa`  |
| 2196   | Layout 2 | `ccce9ebd38aa`  |
| 2192   | Layout 2 | `ccce9ebd38aa`  |
| 2189   | Layout 2 | `ccce9ebd38aa`  |
| 2183   | Layout 2 | `ccce9ebd38aa`  |
| 2179   | Layout 2 | `ccce9ebd38aa`  |
| 2171   | Layout 2 | `ccce9ebd38aa`  |
| 2163   | Layout 2 | `ccce9ebd38aa`  |
| 2156   | Layout 2 | `ccce9ebd38aa`  |
| 2151   | Layout 2 | `ccce9ebd38aa`  |
| 2147   | Layout 2 | `ccce9ebd38aa`  |
| 2142   | Layout 2 | `ccce9ebd38aa`  |
| 2138   | Layout 2 | `ccce9ebd38aa`  |
| 2134   | Layout 2 | `ccce9ebd38aa`  |
| 2130   | Layout 2 | `ccce9ebd38aa`  |
| 2122   | Layout 2 | `ccce9ebd38aa`  |
| 2107   | Layout 2 | `ccce9ebd38aa`  |
| 2098   | Layout 2 | `ccce9ebd38aa`  |
| 2089   | Layout 2 | `ccce9ebd38aa`  |
| 2081   | Layout 2 | `ccce9ebd38aa`  |
| 2073   | Layout 2 | `ccce9ebd38aa`  |
| 2067   | Layout 2 | `ccce9ebd38aa`  |
| 2063   | Layout 2 | `ccce9ebd38aa`  |
| 2059   | Layout 2 | `ccce9ebd38aa`  |
| 2052   | Layout 2 | `ccce9ebd38aa`  |
| 2044   | Layout 2 | `ccce9ebd38aa`  |
| 2039   | Layout 2 | `ccce9ebd38aa`  |
| 2032   | Layout 2 | `ccce9ebd38aa`  |
| 2025   | Layout 2 | `ccce9ebd38aa`  |
| 2011   | Layout 2 | `ccce9ebd38aa`  |
| 2005   | Layout 2 | `ccce9ebd38aa`  |
| 2000   | Layout 2 | `ccce9ebd38aa`  |
| 1996   | Layout 2 | `ccce9ebd38aa`  |
| 1991   | Layout 2 | `ccce9ebd38aa`  |
| 1985   | Layout 2 | `ccce9ebd38aa`  |
| 1980   | Layout 2 | `ccce9ebd38aa`  |
| 1969   | Layout 2 | `ccce9ebd38aa`  |
| 1964   | Layout 2 | `ccce9ebd38aa`  |
| 1958   | Layout 2 | `ccce9ebd38aa`  |
| 1950   | Layout 2 | `ccce9ebd38aa`  |
| 1945   | Layout 2 | `ccce9ebd38aa`  |
| 1937   | Layout 2 | `ccce9ebd38aa`  |
| 1933   | Layout 2 | `ccce9ebd38aa`  |
| 1927   | Layout 2 | `ccce9ebd38aa`  |
| 1921   | Layout 2 | `ccce9ebd38aa`  |
| 1914   | Layout 2 | `ccce9ebd38aa`  |
| 1908   | Layout 2 | `ccce9ebd38aa`  |
| 1897   | Layout 2 | `ccce9ebd38aa`  |
| 1892   | Layout 2 | `ccce9ebd38aa`  |
| 1886   | Layout 2 | `ccce9ebd38aa`  |
| 1881   | Layout 1 | `ccce9ebd38aa`  |
| 1871   | Layout 1 | `ccce9ebd38aa`  |
| 1866   | Layout 1 | `ccce9ebd38aa`  |
| 1862   | Layout 1 | `ccce9ebd38aa`  |
| 1854   | Layout 1 | `ccce9ebd38aa`  |
| 1846   | Layout 1 | `ccce9ebd38aa`  |
| 1838   | Layout 1 | `ccce9ebd38aa`  |
| 1832   | Layout 1 | `ccce9ebd38aa`  |
| 1826   | Layout 1 | `ccce9ebd38aa`  |
| 1822   | Layout 1 | `ccce9ebd38aa`  |
| 1818   | Layout 1 | `ccce9ebd38aa`  |
| 1804   | Layout 1 | `ccce9ebd38aa`  |
| 1794   | Layout 1 | `ccce9ebd38aa`  |
| 1790   | Layout 1 | `ccce9ebd38aa`  |
| 1784   | Layout 1 | `ccce9ebd38aa`  |
| 1774   | Layout 1 | `ccce9ebd38aa`  |
| 1771   | Layout 1 | `ccce9ebd38aa`  |
| 1762   | Layout 1 | `ccce9ebd38aa`  |
| 1759   | Layout 1 | `ccce9ebd38aa`  |
| 1754   | Layout 1 | `ccce9ebd38aa`  |
| 1749   | Layout 1 | `ccce9ebd38aa`  |
| 1743   | Layout 1 | `ccce9ebd38aa`  |
| 1737   | Layout 1 | `ccce9ebd38aa`  |
| 1731   | Layout 1 | `ccce9ebd38aa`  |
| 1725   | Layout 1 | `ccce9ebd38aa`  |
| 1717   | Layout 1 | `ccce9ebd38aa`  |
| 1710   | Layout 1 | `ccce9ebd38aa`  |
| 1704   | Layout 1 | `ccce9ebd38aa`  |
| 1698   | Layout 1 | `ccce9ebd38aa`  |
| 1690   | Layout 1 | `ccce9ebd38aa`  |
| 1685   | Layout 1 | `ccce9ebd38aa`  |
| 1680   | Layout 1 | `ccce9ebd38aa`  |
| 1674   | Layout 1 | `ccce9ebd38aa`  |
| 1668   | Layout 1 | `ccce9ebd38aa`  |
| 1659   | Layout 1 | `ccce9ebd38aa`  |
| 1649   | Layout 1 | `ccce9ebd38aa`  |
| 1642   | Layout 1 | `ccce9ebd38aa`  |
| 1636   | Layout 1 | `ccce9ebd38aa`  |
| 1628   | Layout 1 | `ccce9ebd38aa`  |
| 1622   | Layout 1 | `ccce9ebd38aa`  |
| 1614   | Layout 1 | `ccce9ebd38aa`  |
| 1608   | Layout 1 | `ccce9ebd38aa`  |
| 1602   | Layout 1 | `ccce9ebd38aa`  |
| 1598   | Layout 1 | `ccce9ebd38aa`  |
| 1594   | Layout 1 | `ccce9ebd38aa`  |
| 1590   | Layout 1 | `ccce9ebd38aa`  |
| 1587   | Layout 1 | `ccce9ebd38aa`  |
| 1584   | Layout 1 | `ccce9ebd38aa`  |
| 1579   | Layout 1 | `ccce9ebd38aa`  |
| 1572   | Layout 1 | `ccce9ebd38aa`  |
| 1565   | Layout 1 | `ccce9ebd38aa`  |
| 1559   | Layout 1 | `ccce9ebd38aa`  |
| 1554   | Layout 1 | `ccce9ebd38aa`  |
| 1547   | Layout 1 | `ccce9ebd38aa`  |
| 1537   | Layout 1 | `ccce9ebd38aa`  |
| 1529   | Layout 1 | `ccce9ebd38aa`  |
| 1524   | Layout 1 | `ccce9ebd38aa`  |
| 1519   | Layout 1 | `ccce9ebd38aa`  |
| 1509   | Layout 1 | `ccce9ebd38aa`  |
| 1506   | Layout 1 | `ccce9ebd38aa`  |
| 1504   | Layout 1 | `ccce9ebd38aa`  |
| 1500   | Layout 1 | `ccce9ebd38aa`  |
| 1493   | Layout 1 | `ccce9ebd38aa`  |
| 1489   | Layout 1 | `ccce9ebd38aa`  |
| 1485   | Layout 1 | `ccce9ebd38aa`  |
| 1481   | Layout 1 | `ccce9ebd38aa`  |
| 1474   | Layout 1 | `ccce9ebd38aa`  |
| 1466   | Layout 1 | `ccce9ebd38aa`  |
| 1462   | Layout 1 | `ccce9ebd38aa`  |
| 1459   | Layout 1 | `ccce9ebd38aa`  |
| 1453   | Layout 1 | `ccce9ebd38aa`  |
| 1450   | Layout 1 | `ccce9ebd38aa`  |
| 1445   | Layout 1 | `ccce9ebd38aa`  |
| 1439   | Layout 1 | `ccce9ebd38aa`  |
| 1433   | Layout 1 | `ccce9ebd38aa`  |
| 1430   | Layout 1 | `ccce9ebd38aa`  |
| 1426   | Layout 1 | `ccce9ebd38aa`  |
| 1421   | Layout 1 | `ccce9ebd38aa`  |
| 1417   | Layout 1 | `ccce9ebd38aa`  |
| 1416   | Layout 1 | `ccce9ebd38aa`  |
| 1409   | Layout 1 | `ccce9ebd38aa`  |
| 1405   | Layout 1 | `ccce9ebd38aa`  |
| 1401   | Layout 1 | `ccce9ebd38aa`  |
| 1396   | Layout 1 | `ccce9ebd38aa`  |
| 1391   | Layout 1 | `ccce9ebd38aa`  |
| 1390   | Layout 1 | `ccce9ebd38aa`  |
| 1386   | Layout 1 | `ccce9ebd38aa`  |
| 1381   | Layout 1 | `ccce9ebd38aa`  |
| 1379   | Layout 1 | `ccce9ebd38aa`  |
| 1372   | Layout 1 | `ccce9ebd38aa`  |
| 1366   | Layout 1 | `ccce9ebd38aa`  |
| 1364   | Layout 1 | `ccce9ebd38aa`  |
| 1363   | Layout 1 | `ccce9ebd38aa`  |
| 1360   | Layout 1 | `ccce9ebd38aa`  |
| 1358   | Layout 1 | `ccce9ebd38aa`  |
| 1355   | Layout 1 | `ccce9ebd38aa`  |
| 1351   | Layout 1 | `ccce9ebd38aa`  |
| 1348   | Layout 1 | `ccce9ebd38aa`  |
| 1346   | Layout 1 | `ccce9ebd38aa`  |
| 1341   | Layout 1 | `ccce9ebd38aa`  |
| 1340   | Layout 1 | `ccce9ebd38aa`  |
| 1338   | Layout 1 | `ccce9ebd38aa`  |
| 1335   | Layout 1 | `ccce9ebd38aa`  |
| 1333   | Layout 1 | `ccce9ebd38aa`  |
| 1329   | Layout 1 | `ccce9ebd38aa`  |
| 1327   | Layout 1 | `ccce9ebd38aa`  |
| 1324   | Layout 1 | `ccce9ebd38aa`  |
| 1321   | Layout 1 | `ccce9ebd38aa`  |
| 1319   | Layout 1 | `ccce9ebd38aa`  |
| 1318   | Layout 1 | `ccce9ebd38aa`  |
| 1316   | Layout 1 | `ccce9ebd38aa`  |
| 1313   | Layout 1 | `ccce9ebd38aa`  |
| 1311   | Layout 1 | `ccce9ebd38aa`  |
| 1309   | Layout 1 | `ccce9ebd38aa`  |
| 1304   | Layout 1 | `ccce9ebd38aa`  |
| 1292   | Layout 1 | `ccce9ebd38aa`  |
| 1286   | Layout 1 | `ccce9ebd38aa`  |
| 1280   | Layout 1 | `ccce9ebd38aa`  |
| 1276   | Layout 1 | `ccce9ebd38aa`  |
| 1267   | Layout 1 | `ccce9ebd38aa`  |
| 1261   | No file  | `ccce9ebd38aa`  |
| 1256   | No file  | `ccce9ebd38aa`  |
| 1250   | No file  | `ccce9ebd38aa`  |
| 1246   | No file  | `ccce9ebd38aa`  |
| 1239   | No file  | `ccce9ebd38aa`  |
| 1230   | No file  | `ccce9ebd38aa`  |
| 1226   | No file  | `ccce9ebd38aa`  |
| 1220   | No file  | `ccce9ebd38aa`  |
| 1217   | No file  | `ccce9ebd38aa`  |
| 1211   | No file  | `ccce9ebd38aa`  |
| 1210   | No file  | `ccce9ebd38aa`  |
| 1208   | No file  | `ccce9ebd38aa`  |
| 1203   | No file  | `ccce9ebd38aa`  |
| 1197   | No file  | `ccce9ebd38aa`  |
| 1194   | No file  | `ccce9ebd38aa`  |
| 1192   | No file  | `ccce9ebd38aa`  |
| 1187   | No file  | `ccce9ebd38aa`  |
| 1183   | No file  | `ccce9ebd38aa`  |
| 1177   | No file  | `ccce9ebd38aa`  |
| 1173   | No file  | `ccce9ebd38aa`  |
| 1167   | No file  | `ccce9ebd38aa`  |
| 1164   | No file  | `ccce9ebd38aa`  |
| 1156   | No file  | `ccce9ebd38aa`  |
| 1149   | No file  | `ccce9ebd38aa`  |
| 1144   | No file  | `ccce9ebd38aa`  |
| 1137   | No file  | `ccce9ebd38aa`  |
| 1132   | No file  | `ccce9ebd38aa`  |
| 1127   | No file  | `ccce9ebd38aa`  |
| 1122   | No file  | `ccce9ebd38aa`  |
| 1118   | No file  | `ccce9ebd38aa`  |
| 1114   | No file  | `ccce9ebd38aa`  |
| 1109   | No file  | `ccce9ebd38aa`  |
| 1102   | No file  | `ccce9ebd38aa`  |
| 1096   | No file  | `ccce9ebd38aa`  |
| 1088   | No file  | `ccce9ebd38aa`  |
| 1081   | No file  | `ccce9ebd38aa`  |
| 1076   | No file  | `ccce9ebd38aa`  |
| 1069   | No file  | `ccce9ebd38aa`  |
| 1064   | No file  | `ccce9ebd38aa`  |
| 1058   | No file  | `ccce9ebd38aa`  |
| 1051   | No file  | `ccce9ebd38aa`  |
| 1044   | No file  | `ccce9ebd38aa`  |
| 1036   | No file  | `ccce9ebd38aa`  |
| 1026   | No file  | `ccce9ebd38aa`  |
| 1016   | No file  | `ccce9ebd38aa`  |
| 1009   | No file  | `ccce9ebd38aa`  |
| 1005   | No file  | `ccce9ebd38aa`  |
| 1000   | No file  | `ccce9ebd38aa`  |
| 998    | No file  | `ccce9ebd38aa`  |
| 990    | No file  | `ccce9ebd38aa`  |
| 979    | No file  | `ccce9ebd38aa`  |
| 972    | No file  | `ccce9ebd38aa`  |
| 963    | No file  | `ccce9ebd38aa`  |
| 955    | No file  | `ccce9ebd38aa`  |
| 946    | No file  | `ccce9ebd38aa`  |
| 938    | No file  | `ccce9ebd38aa`  |
| 927    | No file  | `ccce9ebd38aa`  |
| 911    | No file  | `ccce9ebd38aa`  |
| 904    | No file  | `ccce9ebd38aa`  |
| 899    | No file  | `ccce9ebd38aa`  |
| 894    | No file  | `ccce9ebd38aa`  |
| 885    | No file  | `ccce9ebd38aa`  |
| 879    | No file  | `ccce9ebd38aa`  |
| 872    | No file  | `ccce9ebd38aa`  |
| 864    | No file  | `ccce9ebd38aa`  |
| 855    | No file  | `ccce9ebd38aa`  |
| 853    | No file  | `ccce9ebd38aa`  |
| 845    | No file  | `ccce9ebd38aa`  |
| 837    | No file  | `ccce9ebd38aa`  |
| 829    | No file  | `ccce9ebd38aa`  |
| 822    | No file  | `ccce9ebd38aa`  |
| 814    | No file  | `ccce9ebd38aa`  |
| 805    | No file  | `ccce9ebd38aa`  |
| 794    | No file  | `ccce9ebd38aa`  |
| 787    | No file  | `ccce9ebd38aa`  |
| 780    | No file  | `ccce9ebd38aa`  |
| 771    | No file  | `ccce9ebd38aa`  |
| 760    | No file  | `ccce9ebd38aa`  |
| 748    | No file  | `ccce9ebd38aa`  |
| 741    | No file  | `ccce9ebd38aa`  |
| 736    | No file  | `ccce9ebd38aa`  |
| 731    | No file  | `ccce9ebd38aa`  |
| 723    | No file  | `ccce9ebd38aa`  |
| 711    | No file  | `ccce9ebd38aa`  |
| 707    | No file  | `ccce9ebd38aa`  |
| 697    | No file  | `ccce9ebd38aa`  |
| 689    | No file  | `ccce9ebd38aa`  |
| 683    | No file  | `ccce9ebd38aa`  |
| 678    | No file  | `ccce9ebd38aa`  |
| 670    | No file  | `ccce9ebd38aa`  |
| 661    | No file  | `ccce9ebd38aa`  |
| 656    | No file  | `ccce9ebd38aa`  |
| 652    | No file  | `ccce9ebd38aa`  |
| 643    | No file  | `ccce9ebd38aa`  |
| 637    | No file  | `ccce9ebd38aa`  |
| 630    | No file  | `ccce9ebd38aa`  |
| 627    | No file  | `ccce9ebd38aa`  |
| 621    | No file  | `ccce9ebd38aa`  |
| 617    | No file  | `ccce9ebd38aa`  |
| 615    | No file  | `ccce9ebd38aa`  |
| 606    | No file  | `ccce9ebd38aa`  |
| 599    | No file  | `ccce9ebd38aa`  |
| 592    | No file  | `ccce9ebd38aa`  |
| 586    | No file  | `ccce9ebd38aa`  |
| 577    | No file  | `ccce9ebd38aa`  |
| 569    | No file  | `ccce9ebd38aa`  |
| 561    | No file  | `ccce9ebd38aa`  |
| 554    | No file  | `ccce9ebd38aa`  |
| 542    | No file  | `ccce9ebd38aa`  |
| 532    | No file  | `ccce9ebd38aa`  |
| 531    | No file  | `ccce9ebd38aa`  |
| 526    | No file  | `ccce9ebd38aa`  |
| 521    | No file  | `ccce9ebd38aa`  |
| 517    | No file  | `ccce9ebd38aa`  |
| 510    | No file  | `ccce9ebd38aa`  |
| 508    | No file  | `ccce9ebd38aa`  |
| 504    | No file  | `ccce9ebd38aa`  |
| 497    | No file  | `ccce9ebd38aa`  |
| 491    | No file  | `ccce9ebd38aa`  |
| 485    | No file  | `ccce9ebd38aa`  |
| 478    | No file  | `ccce9ebd38aa`  |
| 472    | No file  | `ccce9ebd38aa`  |
| 466    | No file  | `ccce9ebd38aa`  |
| 457    | No file  | `ccce9ebd38aa`  |
| 452    | No file  | `ccce9ebd38aa`  |
| 449    | No file  | `ccce9ebd38aa`  |
| 435    | No file  | `ccce9ebd38aa`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of game conditions                     |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (14 bytes)

| Offset  | Type | Field              | Notes                                                                          |
| ------- | ---- | ------------------ | ------------------------------------------------------------------------------ |
| `+0x00` | u32  | event_name_ref     | String table index of the audio event name, `Set_State_SA_States_<condition>`  |
| `+0x04` | u32  | unknown_04         | String table index of a second state name, `BGM_SA_1` to `BGM_SA_10` or `BGM_SA_Mute` on client 3482 |
| `+0x08` | u32  | game_condition_ref | String table index of the game condition, `Login` to `Trio_Ascention`          |
| `+0x0C` | u16  | index              | Row key, `1` to `17` on client 3482 (no `15`)                                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                  |
| ------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `42` on client 3482                 |
| `+0x04` | pstr[string_count] | strings      | UTF-8 event, state and condition names in first-use order |

## Layout 1

### Row (18 bytes)

| Offset  | Type | Field              | Notes                                                             |
| ------- | ---- | ------------------ | ----------------------------------------------------------------- |
| `+0x00` | u16  | index              | Row key                                                           |
| `+0x02` | u32  | bank_name_ref      | String table index of the sound bank name, `BGM_0_0` on every row |
| `+0x06` | u32  | event_name_ref     | String table index of the audio event name                        |
| `+0x0A` | u32  | music_index        | `0`, `1` or `6` on client 1784                                    |
| `+0x0E` | u32  | game_condition_ref | String table index of the game condition                          |

## Conditions

Client 3482:

| `index` | Game condition         | `unknown_04`  |
| ------- | ---------------------- | ------------- |
| `1`     | `Login`                | `BGM_SA_1`    |
| `2`     | `Lobby`                | `BGM_SA_2`    |
| `3`     | `CharacterSelection`   | `BGM_SA_3`    |
| `4`     | `Loading`              | `BGM_SA_1`    |
| `5`     | `ArenaDefault`         | `BGM_SA_Mute` |
| `6`     | `ArenaTension`         | `BGM_SA_6`    |
| `7`     | `Result`               | `BGM_SA_4`    |
| `8`     | `DefaultWin`           | `BGM_SA_Mute` |
| `9`     | `DefaultLoose`         | `BGM_SA_Mute` |
| `10`    | `TensionWin`           | `BGM_SA_6`    |
| `11`    | `TensionLoose`         | `BGM_SA_6`    |
| `12`    | `DualTournament_Round` | `BGM_SA_7`    |
| `13`    | `Lobby_BGMOff`         | `BGM_SA_Mute` |
| `14`    | `DeathMatch_Tension`   | `BGM_SA_8`    |
| `16`    | `Trio_Tension`         | `BGM_SA_9`    |
| `17`    | `Trio_Ascention`       | `BGM_SA_10`   |

Every `event_name_ref` string is `Set_State_SA_States_` followed by the
game condition.

## Field Names

The names are the `Index`, `BankName`, `EventName`, `MusicIndex` and
`GameCondition` columns of the `BgmStateSA_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784. The client 1784 file holds
the sheet's 7 rows and all 7 match it on these five columns.

On client 3482 rows `1` to `7` match the sheet on `Index`, `EventName`
and `GameCondition` (7 of 7); `bank_name_ref` and `music_index` are gone,
and `unknown_04` is new. Rows `8` to `17` are newer than the sheet.

## Notes

- `SA` reads as Shadow Arena: the conditions are arena rounds
  (`ArenaTension`, `DeathMatch_Tension`, `Trio_Ascention`), and the same
  prefix names the `SA_Web_URL` sheet of
  [`sha_weburl.bss`](sha_weburl_bss.md), whose URLs are
  `*-shadowarena.pearlabyss.com` hosts.
- [`bgmstate.bss`](bgmstate_bss.md) is the same table for the game client
  and went through the same change between the two layouts.
- No client Lua file of client 3482 names the table or a
  `Set_State_SA_*` string.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/client_tables.py`, with
  the event name and the game condition.

## Open Questions

### What the Second State Name Is

`unknown_04` took the place of the sheet's `MusicIndex`, as in
`bgmstate.bss`. Where client 1784 stores `music_index` `0` (row `5`),
client 3482 stores `BGM_SA_Mute`; `music_index` `6` became `BGM_SA_6`
on row `6` and `BGM_SA_4` on row `7`, and `1` became `BGM_SA_1` to
`BGM_SA_3`. Whether it names the music track of the condition is open.
