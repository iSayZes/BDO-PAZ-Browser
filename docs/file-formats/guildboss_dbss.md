# `guildboss.dbss` Format

## Purpose

One row per guild boss character with the skill EXP and guild funds amounts
of the `GuildBoss_Table` sheet. On client 3474 the file has 1 row, character
`23014` Black Shadow `<Boss>` (Korean label `Cal_사우닐 주둔지 보스_미완성`, a
Calpheon Saunil camp boss marked unfinished, model
`monster/m0180_wyvern_f_boss`). Companion `guildbossoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records      | Row bytes |
| ------ | -------------- | ---------------------- | ----- | ------------ | --------- |
| 1      | 1346 and later | `guildboss.dbss`       | 21    | 1 Row        | 17        |
| 1      | 1346 and later | `guildbossoffset.dbss` | 14    | 1 Offset Row | 10        |

| Layout | File                   | Known         | Unknown    |
| ------ | ---------------------- | ------------- | ---------- |
| 1      | `guildboss.dbss`       | 20 B (95.2%)  | 1 B (4.8%) |
| 1      | `guildbossoffset.dbss` | 14 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `ac495f32aca3`  |
| 3482   | Layout 1             | `ac495f32aca3`  |
| 3474   | Layout 1             | `ac495f32aca3`  |
| 3473   | Layout 1             | `ac495f32aca3`  |
| 3464   | Layout 1             | `ac495f32aca3`  |
| 3458   | Layout 1             | `ac495f32aca3`  |
| 3454   | Layout 1             | `ac495f32aca3`  |
| 3444   | Layout 1             | `ac495f32aca3`  |
| 3435   | Layout 1             | `ac495f32aca3`  |
| 3426   | Layout 1             | `ac495f32aca3`  |
| 3418   | Layout 1             | `ac495f32aca3`  |
| 3412   | Layout 1             | `ac495f32aca3`  |
| 3402   | Layout 1             | `ac495f32aca3`  |
| 3396   | Layout 1             | `ac495f32aca3`  |
| 3387   | Layout 1             | `ac495f32aca3`  |
| 3381   | Layout 1             | `ac495f32aca3`  |
| 3373   | Layout 1             | `ac495f32aca3`  |
| 3364   | Layout 1             | `ac495f32aca3`  |
| 3356   | Layout 1             | `ac495f32aca3`  |
| 3349   | Layout 1             | `ac495f32aca3`  |
| 3342   | Layout 1             | `ac495f32aca3`  |
| 3335   | Layout 1             | `ac495f32aca3`  |
| 3326   | Layout 1             | `ac495f32aca3`  |
| 3321   | Layout 1             | `ac495f32aca3`  |
| 3314   | Layout 1             | `ac495f32aca3`  |
| 3303   | Layout 1             | `ac495f32aca3`  |
| 3302   | Layout 1             | `ac495f32aca3`  |
| 3293   | Layout 1             | `ac495f32aca3`  |
| 3283   | Layout 1             | `ac495f32aca3`  |
| 3275   | Layout 1             | `ac495f32aca3`  |
| 3267   | Layout 1             | `ac495f32aca3`  |
| 3258   | Layout 1             | `ac495f32aca3`  |
| 3251   | Layout 1             | `ac495f32aca3`  |
| 3242   | Layout 1             | `ac495f32aca3`  |
| 3235   | Layout 1             | `ac495f32aca3`  |
| 3229   | Layout 1             | `ac495f32aca3`  |
| 3212   | Layout 1             | `ac495f32aca3`  |
| 3203   | Layout 1             | `ac495f32aca3`  |
| 3193   | Layout 1             | `ac495f32aca3`  |
| 3186   | Layout 1             | `ac495f32aca3`  |
| 3177   | Layout 1             | `ac495f32aca3`  |
| 3169   | Layout 1             | `ac495f32aca3`  |
| 3158   | Layout 1             | `ac495f32aca3`  |
| 3151   | Layout 1             | `ac495f32aca3`  |
| 3144   | Layout 1             | `ac495f32aca3`  |
| 3133   | Layout 1             | `ac495f32aca3`  |
| 3125   | Layout 1             | `ac495f32aca3`  |
| 3118   | Layout 1             | `ac495f32aca3`  |
| 3111   | Layout 1             | `ac495f32aca3`  |
| 3103   | Layout 1             | `ac495f32aca3`  |
| 3095   | Layout 1             | `ac495f32aca3`  |
| 3086   | Layout 1             | `ac495f32aca3`  |
| 3072   | Layout 1             | `ac495f32aca3`  |
| 3062   | Layout 1             | `ac495f32aca3`  |
| 3052   | Layout 1             | `ac495f32aca3`  |
| 3045   | Layout 1             | `ac495f32aca3`  |
| 3037   | Layout 1             | `ac495f32aca3`  |
| 3030   | Layout 1             | `ac495f32aca3`  |
| 3021   | Layout 1             | `ac495f32aca3`  |
| 3012   | Layout 1             | `ac495f32aca3`  |
| 3002   | Layout 1             | `ac495f32aca3`  |
| 2995   | Layout 1             | `ac495f32aca3`  |
| 2987   | Layout 1             | `ac495f32aca3`  |
| 2978   | Layout 1             | `ac495f32aca3`  |
| 2970   | Layout 1             | `ac495f32aca3`  |
| 2959   | Layout 1             | `ac495f32aca3`  |
| 2951   | Layout 1             | `ac495f32aca3`  |
| 2942   | Layout 1             | `ac495f32aca3`  |
| 2935   | Layout 1             | `ac495f32aca3`  |
| 2932   | Layout 1             | `ac495f32aca3`  |
| 2923   | Layout 1             | `ac495f32aca3`  |
| 2919   | Layout 1             | `ac495f32aca3`  |
| 2907   | Layout 1             | `ac495f32aca3`  |
| 2900   | Layout 1             | `ac495f32aca3`  |
| 2891   | Layout 1             | `ac495f32aca3`  |
| 2882   | Layout 1             | `ac495f32aca3`  |
| 2872   | Layout 1             | `ac495f32aca3`  |
| 2863   | Layout 1             | `ac495f32aca3`  |
| 2855   | Layout 1             | `ac495f32aca3`  |
| 2849   | Layout 1             | `ac495f32aca3`  |
| 2844   | Layout 1             | `ac495f32aca3`  |
| 2834   | Layout 1             | `ac495f32aca3`  |
| 2825   | Layout 1             | `ac495f32aca3`  |
| 2819   | Layout 1             | `ac495f32aca3`  |
| 2811   | Layout 1             | `ac495f32aca3`  |
| 2803   | Layout 1             | `ac495f32aca3`  |
| 2794   | Layout 1             | `ac495f32aca3`  |
| 2783   | Layout 1             | `ac495f32aca3`  |
| 2774   | Layout 1             | `ac495f32aca3`  |
| 2765   | Layout 1             | `ac495f32aca3`  |
| 2756   | Layout 1             | `ac495f32aca3`  |
| 2750   | Layout 1             | `ac495f32aca3`  |
| 2743   | Layout 1             | `ac495f32aca3`  |
| 2736   | Layout 1             | `ac495f32aca3`  |
| 2726   | Layout 1             | `ac495f32aca3`  |
| 2717   | Layout 1             | `ac495f32aca3`  |
| 2709   | Layout 1             | `ac495f32aca3`  |
| 2703   | Layout 1             | `ac495f32aca3`  |
| 2695   | Layout 1             | `ac495f32aca3`  |
| 2684   | Layout 1             | `ac495f32aca3`  |
| 2672   | Layout 1             | `ac495f32aca3`  |
| 2665   | Layout 1             | `ac495f32aca3`  |
| 2657   | Layout 1             | `ac495f32aca3`  |
| 2649   | Layout 1             | `ac495f32aca3`  |
| 2644   | Layout 1             | `ac495f32aca3`  |
| 2637   | Layout 1             | `ac495f32aca3`  |
| 2629   | Layout 1             | `ac495f32aca3`  |
| 2619   | Layout 1             | `ac495f32aca3`  |
| 2612   | Layout 1             | `ac495f32aca3`  |
| 2606   | Layout 1             | `ac495f32aca3`  |
| 2602   | Layout 1             | `ac495f32aca3`  |
| 2601   | Layout 1             | `ac495f32aca3`  |
| 2592   | Layout 1             | `ac495f32aca3`  |
| 2583   | Layout 1             | `ac495f32aca3`  |
| 2575   | Layout 1             | `ac495f32aca3`  |
| 2567   | Layout 1             | `ac495f32aca3`  |
| 2560   | Layout 1             | `ac495f32aca3`  |
| 2553   | Layout 1             | `ac495f32aca3`  |
| 2545   | Layout 1             | `ac495f32aca3`  |
| 2538   | Layout 1             | `ac495f32aca3`  |
| 2529   | Layout 1             | `ac495f32aca3`  |
| 2519   | Layout 1             | `ac495f32aca3`  |
| 2513   | Layout 1             | `ac495f32aca3`  |
| 2510   | Layout 1             | `ac495f32aca3`  |
| 2507   | Layout 1             | `ac495f32aca3`  |
| 2503   | Layout 1             | `ac495f32aca3`  |
| 2498   | Layout 1             | `ac495f32aca3`  |
| 2492   | Layout 1             | `ac495f32aca3`  |
| 2487   | Layout 1             | `ac495f32aca3`  |
| 2480   | Layout 1             | `ac495f32aca3`  |
| 2474   | Layout 1             | `ac495f32aca3`  |
| 2468   | Layout 1             | `ac495f32aca3`  |
| 2460   | Layout 1             | `ac495f32aca3`  |
| 2453   | Layout 1             | `ac495f32aca3`  |
| 2444   | Layout 1             | `ac495f32aca3`  |
| 2438   | Layout 1             | `ac495f32aca3`  |
| 2434   | Layout 1             | `ac495f32aca3`  |
| 2429   | Layout 1             | `ac495f32aca3`  |
| 2421   | Layout 1             | `ac495f32aca3`  |
| 2414   | Layout 1             | `ac495f32aca3`  |
| 2407   | Layout 1             | `ac495f32aca3`  |
| 2401   | Layout 1             | `ac495f32aca3`  |
| 2397   | Layout 1             | `ac495f32aca3`  |
| 2393   | Layout 1             | `ac495f32aca3`  |
| 2384   | Layout 1             | `ac495f32aca3`  |
| 2378   | Layout 1             | `ac495f32aca3`  |
| 2372   | Layout 1             | `ac495f32aca3`  |
| 2358   | Layout 1             | `ac495f32aca3`  |
| 2352   | Layout 1             | `ac495f32aca3`  |
| 2347   | Layout 1             | `ac495f32aca3`  |
| 2343   | Layout 1             | `ac495f32aca3`  |
| 2335   | Layout 1             | `ac495f32aca3`  |
| 2327   | Layout 1             | `ac495f32aca3`  |
| 2324   | Layout 1             | `ac495f32aca3`  |
| 2319   | Layout 1             | `ac495f32aca3`  |
| 2313   | Layout 1             | `ac495f32aca3`  |
| 2308   | Layout 1             | `ac495f32aca3`  |
| 2302   | Layout 1             | `ac495f32aca3`  |
| 2295   | Layout 1             | `ac495f32aca3`  |
| 2290   | Layout 1             | `ac495f32aca3`  |
| 2284   | Layout 1             | `ac495f32aca3`  |
| 2276   | Layout 1             | `ac495f32aca3`  |
| 2269   | Layout 1             | `ac495f32aca3`  |
| 2259   | Layout 1             | `ac495f32aca3`  |
| 2250   | Layout 1             | `ac495f32aca3`  |
| 2243   | Layout 1             | `ac495f32aca3`  |
| 2235   | Layout 1             | `ac495f32aca3`  |
| 2229   | Layout 1             | `ac495f32aca3`  |
| 2224   | Layout 1             | `ac495f32aca3`  |
| 2218   | Layout 1             | `ac495f32aca3`  |
| 2215   | Layout 1             | `ac495f32aca3`  |
| 2207   | Layout 1             | `ac495f32aca3`  |
| 2203   | Layout 1             | `ac495f32aca3`  |
| 2196   | Layout 1             | `ac495f32aca3`  |
| 2192   | Layout 1             | `ac495f32aca3`  |
| 2189   | Layout 1             | `ac495f32aca3`  |
| 2183   | Layout 1             | `ac495f32aca3`  |
| 2179   | Layout 1             | `ac495f32aca3`  |
| 2171   | Layout 1             | `ac495f32aca3`  |
| 2163   | Layout 1             | `ac495f32aca3`  |
| 2156   | Layout 1             | `ac495f32aca3`  |
| 2151   | Layout 1             | `ac495f32aca3`  |
| 2147   | Layout 1             | `ac495f32aca3`  |
| 2142   | Layout 1             | `ac495f32aca3`  |
| 2138   | Layout 1             | `ac495f32aca3`  |
| 2134   | Layout 1             | `ac495f32aca3`  |
| 2130   | Layout 1             | `ac495f32aca3`  |
| 2122   | Layout 1             | `ac495f32aca3`  |
| 2107   | Layout 1             | `ac495f32aca3`  |
| 2098   | Layout 1             | `ac495f32aca3`  |
| 2089   | Layout 1             | `ac495f32aca3`  |
| 2081   | Layout 1             | `ac495f32aca3`  |
| 2073   | Layout 1             | `ac495f32aca3`  |
| 2067   | Layout 1             | `ac495f32aca3`  |
| 2063   | Layout 1             | `ac495f32aca3`  |
| 2059   | Layout 1             | `ac495f32aca3`  |
| 2052   | Layout 1             | `ac495f32aca3`  |
| 2044   | Layout 1             | `ac495f32aca3`  |
| 2039   | Layout 1             | `ac495f32aca3`  |
| 2032   | Layout 1             | `ac495f32aca3`  |
| 2025   | Layout 1             | `ac495f32aca3`  |
| 2011   | Layout 1             | `ac495f32aca3`  |
| 2005   | Layout 1             | `ac495f32aca3`  |
| 2000   | Layout 1             | `ac495f32aca3`  |
| 1996   | Layout 1             | `ac495f32aca3`  |
| 1991   | Layout 1             | `ac495f32aca3`  |
| 1985   | Layout 1             | `ac495f32aca3`  |
| 1980   | Layout 1             | `ac495f32aca3`  |
| 1969   | Layout 1             | `ac495f32aca3`  |
| 1964   | Layout 1             | `ac495f32aca3`  |
| 1958   | Layout 1             | `ac495f32aca3`  |
| 1950   | Layout 1             | `ac495f32aca3`  |
| 1945   | Layout 1             | `ac495f32aca3`  |
| 1937   | Layout 1             | `ac495f32aca3`  |
| 1933   | Layout 1             | `ac495f32aca3`  |
| 1927   | Layout 1             | `ac495f32aca3`  |
| 1921   | Layout 1             | `ac495f32aca3`  |
| 1914   | Layout 1             | `ac495f32aca3`  |
| 1908   | Layout 1             | `ac495f32aca3`  |
| 1897   | Layout 1             | `ac495f32aca3`  |
| 1892   | Layout 1             | `ac495f32aca3`  |
| 1886   | Layout 1             | `ac495f32aca3`  |
| 1881   | Layout 1             | `ac495f32aca3`  |
| 1871   | Layout 1             | `ac495f32aca3`  |
| 1866   | Layout 1             | `ac495f32aca3`  |
| 1862   | Layout 1             | `ac495f32aca3`  |
| 1854   | Layout 1             | `ac495f32aca3`  |
| 1846   | Layout 1             | `ac495f32aca3`  |
| 1838   | Layout 1             | `ac495f32aca3`  |
| 1832   | Layout 1             | `ac495f32aca3`  |
| 1826   | Layout 1             | `ac495f32aca3`  |
| 1822   | Layout 1             | `ac495f32aca3`  |
| 1818   | Layout 1             | `ac495f32aca3`  |
| 1804   | Layout 1             | `ac495f32aca3`  |
| 1794   | Layout 1             | `ac495f32aca3`  |
| 1790   | Layout 1             | `ac495f32aca3`  |
| 1784   | Layout 1             | `ac495f32aca3`  |
| 1774   | Layout 1             | `ac495f32aca3`  |
| 1771   | Layout 1             | `ac495f32aca3`  |
| 1762   | Layout 1             | `ac495f32aca3`  |
| 1759   | Layout 1             | `ac495f32aca3`  |
| 1754   | Layout 1             | `ac495f32aca3`  |
| 1749   | Layout 1             | `ac495f32aca3`  |
| 1743   | Layout 1             | `ac495f32aca3`  |
| 1737   | Layout 1             | `ac495f32aca3`  |
| 1731   | Layout 1             | `ac495f32aca3`  |
| 1725   | Layout 1             | `ac495f32aca3`  |
| 1717   | Layout 1             | `ac495f32aca3`  |
| 1710   | Layout 1             | `ac495f32aca3`  |
| 1704   | Layout 1             | `ac495f32aca3`  |
| 1698   | Layout 1             | `ac495f32aca3`  |
| 1690   | Layout 1             | `ac495f32aca3`  |
| 1685   | Layout 1             | `ac495f32aca3`  |
| 1680   | Layout 1             | `ac495f32aca3`  |
| 1674   | Layout 1             | `ac495f32aca3`  |
| 1668   | Layout 1             | `ac495f32aca3`  |
| 1659   | Layout 1             | `ac495f32aca3`  |
| 1649   | Layout 1             | `ac495f32aca3`  |
| 1642   | Layout 1             | `ac495f32aca3`  |
| 1636   | Layout 1             | `ac495f32aca3`  |
| 1628   | Layout 1             | `ac495f32aca3`  |
| 1622   | Layout 1             | `ac495f32aca3`  |
| 1614   | Layout 1             | `ac495f32aca3`  |
| 1608   | Layout 1             | `ac495f32aca3`  |
| 1602   | Layout 1             | `ac495f32aca3`  |
| 1598   | Layout 1             | `ac495f32aca3`  |
| 1594   | Layout 1             | `ac495f32aca3`  |
| 1590   | Layout 1             | `ac495f32aca3`  |
| 1587   | Layout 1             | `ac495f32aca3`  |
| 1584   | Layout 1             | `ac495f32aca3`  |
| 1579   | Layout 1             | `ac495f32aca3`  |
| 1572   | Layout 1             | `ac495f32aca3`  |
| 1565   | Layout 1             | `ac495f32aca3`  |
| 1559   | Layout 1             | `ac495f32aca3`  |
| 1554   | Layout 1             | `ac495f32aca3`  |
| 1547   | Layout 1             | `ac495f32aca3`  |
| 1537   | Layout 1             | `ac495f32aca3`  |
| 1529   | Layout 1             | `ac495f32aca3`  |
| 1524   | Layout 1             | `ac495f32aca3`  |
| 1519   | Layout 1             | `ac495f32aca3`  |
| 1509   | Layout 1             | `ac495f32aca3`  |
| 1506   | Layout 1             | `ac495f32aca3`  |
| 1504   | Layout 1             | `ac495f32aca3`  |
| 1500   | Layout 1             | `ac495f32aca3`  |
| 1493   | Layout 1             | `ac495f32aca3`  |
| 1489   | Layout 1             | `ac495f32aca3`  |
| 1485   | Layout 1             | `ac495f32aca3`  |
| 1481   | Layout 1             | `ac495f32aca3`  |
| 1474   | Layout 1             | `ac495f32aca3`  |
| 1466   | Layout 1             | `ac495f32aca3`  |
| 1462   | Layout 1             | `ac495f32aca3`  |
| 1459   | Layout 1             | `ac495f32aca3`  |
| 1453   | Layout 1             | `ac495f32aca3`  |
| 1450   | Layout 1             | `ac495f32aca3`  |
| 1445   | Layout 1             | `ac495f32aca3`  |
| 1439   | Layout 1             | `ac495f32aca3`  |
| 1433   | Layout 1             | `ac495f32aca3`  |
| 1430   | Layout 1             | `ac495f32aca3`  |
| 1426   | Layout 1             | `ac495f32aca3`  |
| 1421   | Layout 1             | `ac495f32aca3`  |
| 1417   | Layout 1             | `ac495f32aca3`  |
| 1416   | Layout 1             | `ac495f32aca3`  |
| 1409   | Layout 1             | `ac495f32aca3`  |
| 1405   | Layout 1             | `ac495f32aca3`  |
| 1401   | Layout 1             | `ac495f32aca3`  |
| 1396   | Layout 1             | `ac495f32aca3`  |
| 1391   | Layout 1             | `ac495f32aca3`  |
| 1390   | Layout 1             | `ac495f32aca3`  |
| 1386   | Layout 1             | `ac495f32aca3`  |
| 1381   | Layout 1             | `ac495f32aca3`  |
| 1379   | Layout 1             | `ac495f32aca3`  |
| 1372   | Layout 1             | `ac495f32aca3`  |
| 1366   | Layout 1             | `ac495f32aca3`  |
| 1364   | Layout 1             | `ac495f32aca3`  |
| 1363   | Layout 1             | `ac495f32aca3`  |
| 1360   | Layout 1             | `ac495f32aca3`  |
| 1358   | Layout 1             | `ac495f32aca3`  |
| 1355   | Layout 1             | `ac495f32aca3`  |
| 1351   | Layout 1             | `ac495f32aca3`  |
| 1348   | Layout 1             | `ac495f32aca3`  |
| 1346   | Layout 1             | `ac495f32aca3`  |
| 1341   | No documented layout | `ac495f32aca3`  |
| 1340   | No documented layout | `ac495f32aca3`  |
| 1338   | No documented layout | `ac495f32aca3`  |
| 1335   | No documented layout | `ac495f32aca3`  |
| 1333   | No documented layout | `ac495f32aca3`  |
| 1329   | No documented layout | `ac495f32aca3`  |
| 1327   | No documented layout | `ac495f32aca3`  |
| 1324   | No documented layout | `ac495f32aca3`  |
| 1321   | No documented layout | `ac495f32aca3`  |
| 1319   | No documented layout | `ac495f32aca3`  |
| 1318   | No documented layout | `ac495f32aca3`  |
| 1316   | No documented layout | `ac495f32aca3`  |
| 1313   | No documented layout | `ac495f32aca3`  |
| 1311   | No documented layout | `ac495f32aca3`  |
| 1309   | No documented layout | `ac495f32aca3`  |
| 1304   | No documented layout | `ac495f32aca3`  |
| 1292   | No documented layout | `ac495f32aca3`  |
| 1286   | No documented layout | `ac495f32aca3`  |
| 1280   | No documented layout | `ac495f32aca3`  |
| 1276   | No documented layout | `ac495f32aca3`  |
| 1267   | No file              | `ac495f32aca3`  |
| 1261   | No file              | `ac495f32aca3`  |
| 1256   | No file              | `ac495f32aca3`  |
| 1250   | No file              | `ac495f32aca3`  |
| 1246   | No file              | `ac495f32aca3`  |
| 1239   | No file              | `ac495f32aca3`  |
| 1230   | No file              | `ac495f32aca3`  |
| 1226   | No file              | `ac495f32aca3`  |
| 1220   | No file              | `ac495f32aca3`  |
| 1217   | No file              | `ac495f32aca3`  |
| 1211   | No file              | `ac495f32aca3`  |
| 1210   | No file              | `ac495f32aca3`  |
| 1208   | No file              | `ac495f32aca3`  |
| 1203   | No file              | `ac495f32aca3`  |
| 1197   | No file              | `ac495f32aca3`  |
| 1194   | No file              | `ac495f32aca3`  |
| 1192   | No file              | `ac495f32aca3`  |
| 1187   | No file              | `ac495f32aca3`  |
| 1183   | No file              | `ac495f32aca3`  |
| 1177   | No file              | `ac495f32aca3`  |
| 1173   | No file              | `ac495f32aca3`  |
| 1167   | No file              | `ac495f32aca3`  |
| 1164   | No file              | `ac495f32aca3`  |
| 1156   | No file              | `ac495f32aca3`  |
| 1149   | No file              | `ac495f32aca3`  |
| 1144   | No file              | `ac495f32aca3`  |
| 1137   | No file              | `ac495f32aca3`  |
| 1132   | No file              | `ac495f32aca3`  |
| 1127   | No file              | `ac495f32aca3`  |
| 1122   | No file              | `ac495f32aca3`  |
| 1118   | No file              | `ac495f32aca3`  |
| 1114   | No file              | `ac495f32aca3`  |
| 1109   | No file              | `ac495f32aca3`  |
| 1102   | No file              | `ac495f32aca3`  |
| 1096   | No file              | `ac495f32aca3`  |
| 1088   | No file              | `ac495f32aca3`  |
| 1081   | No file              | `ac495f32aca3`  |
| 1076   | No file              | `ac495f32aca3`  |
| 1069   | No file              | `ac495f32aca3`  |
| 1064   | No file              | `ac495f32aca3`  |
| 1058   | No file              | `ac495f32aca3`  |
| 1051   | No file              | `ac495f32aca3`  |
| 1044   | No file              | `ac495f32aca3`  |
| 1036   | No file              | `ac495f32aca3`  |
| 1026   | No file              | `ac495f32aca3`  |
| 1016   | No file              | `ac495f32aca3`  |
| 1009   | No file              | `ac495f32aca3`  |
| 1005   | No file              | `ac495f32aca3`  |
| 1000   | No file              | `ac495f32aca3`  |
| 998    | No file              | `ac495f32aca3`  |
| 990    | No file              | `ac495f32aca3`  |
| 979    | No file              | `ac495f32aca3`  |
| 972    | No file              | `ac495f32aca3`  |
| 963    | No file              | `ac495f32aca3`  |
| 955    | No file              | `ac495f32aca3`  |
| 946    | No file              | `ac495f32aca3`  |
| 938    | No file              | `ac495f32aca3`  |
| 927    | No file              | `ac495f32aca3`  |
| 911    | No file              | `ac495f32aca3`  |
| 904    | No file              | `ac495f32aca3`  |
| 899    | No file              | `ac495f32aca3`  |
| 894    | No file              | `ac495f32aca3`  |
| 885    | No file              | `ac495f32aca3`  |
| 879    | No file              | `ac495f32aca3`  |
| 872    | No file              | `ac495f32aca3`  |
| 864    | No file              | `ac495f32aca3`  |
| 855    | No file              | `ac495f32aca3`  |
| 853    | No file              | `ac495f32aca3`  |
| 845    | No file              | `ac495f32aca3`  |
| 837    | No file              | `ac495f32aca3`  |
| 829    | No file              | `ac495f32aca3`  |
| 822    | No file              | `ac495f32aca3`  |
| 814    | No file              | `ac495f32aca3`  |
| 805    | No file              | `ac495f32aca3`  |
| 794    | No file              | `ac495f32aca3`  |
| 787    | No file              | `ac495f32aca3`  |
| 780    | No file              | `ac495f32aca3`  |
| 771    | No file              | `ac495f32aca3`  |
| 760    | No file              | `ac495f32aca3`  |
| 748    | No file              | `ac495f32aca3`  |
| 741    | No file              | `ac495f32aca3`  |
| 736    | No file              | `ac495f32aca3`  |
| 731    | No file              | `ac495f32aca3`  |
| 723    | No file              | `ac495f32aca3`  |
| 711    | No file              | `ac495f32aca3`  |
| 707    | No file              | `ac495f32aca3`  |
| 697    | No file              | `ac495f32aca3`  |
| 689    | No file              | `ac495f32aca3`  |
| 683    | No file              | `ac495f32aca3`  |
| 678    | No file              | `ac495f32aca3`  |
| 670    | No file              | `ac495f32aca3`  |
| 661    | No file              | `ac495f32aca3`  |
| 656    | No file              | `ac495f32aca3`  |
| 652    | No file              | `ac495f32aca3`  |
| 643    | No file              | `ac495f32aca3`  |
| 637    | No file              | `ac495f32aca3`  |
| 630    | No file              | `ac495f32aca3`  |
| 627    | No file              | `ac495f32aca3`  |
| 621    | No file              | `ac495f32aca3`  |
| 617    | No file              | `ac495f32aca3`  |
| 615    | No file              | `ac495f32aca3`  |
| 606    | No file              | `ac495f32aca3`  |
| 599    | No file              | `ac495f32aca3`  |
| 592    | No file              | `ac495f32aca3`  |
| 586    | No file              | `ac495f32aca3`  |
| 577    | No file              | `ac495f32aca3`  |
| 569    | No file              | `ac495f32aca3`  |
| 561    | No file              | `ac495f32aca3`  |
| 554    | No file              | `ac495f32aca3`  |
| 542    | No file              | `ac495f32aca3`  |
| 532    | No file              | `ac495f32aca3`  |
| 531    | No file              | `ac495f32aca3`  |
| 526    | No file              | `ac495f32aca3`  |
| 521    | No file              | `ac495f32aca3`  |
| 517    | No file              | `ac495f32aca3`  |
| 510    | No file              | `ac495f32aca3`  |
| 508    | No file              | `ac495f32aca3`  |
| 504    | No file              | `ac495f32aca3`  |
| 497    | No file              | `ac495f32aca3`  |
| 491    | No file              | `ac495f32aca3`  |
| 485    | No file              | `ac495f32aca3`  |
| 478    | No file              | `ac495f32aca3`  |
| 472    | No file              | `ac495f32aca3`  |
| 466    | No file              | `ac495f32aca3`  |
| 457    | No file              | `ac495f32aca3`  |
| 452    | No file              | `ac495f32aca3`  |
| 449    | No file              | `ac495f32aca3`  |
| 435    | No file              | `ac495f32aca3`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                 |
| ---------------------------- | -------- | -------------------------------------------------------------------- |
| `guildbossoffset.dbss`       | Optional | `character_key -> (offset, size)` of every row; the main file can be walked without it |
| `characterstaticoffset.dbss` | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key link |
| `languagedata_en.loc`        | Optional | Character names (LOC type 6)                                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (17 bytes)

| Offset  | Type | Field             | Notes                                                       |
| ------- | ---- | ----------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key     | Boss character; has a `characterstatic.dbss` row (client 3474) |
| `+0x02` | u8   | unknown_02        | `1`; the offset file points here                            |
| `+0x03` | u16  | character_key_dup | Equal to `character_key`                                    |
| `+0x05` | i32  | skill_point_exp   | `100000` (client 3474)                                      |
| `+0x09` | i64  | guild_money       | `100000000` (client 3474)                                   |

### `guildbossoffset.dbss`

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `guildboss.dbss` count       |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row    |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                   |
| ------- | ---- | ------------- | ------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                             |
| `+0x02` | u32  | offset        | Row start + 2, at `unknown_02`                          |
| `+0x06` | u32  | size          | The row without its leading `character_key`: always `15` |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`.

## Field Names

The names follow the `GuildBoss_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, columns `CharacterKey`, `SkillPointExp`
and `GuildMoney`. Its one row, `23014`, `100000`, `100000000`, matches the
file on clients 1784 and 3474 (1 of 1 keys, both values). The
`GuildBoss_Table` of a private server on client 519 holds the same row.

The client 1784 server dump (`Instance_dumpFull.exe`) reads the sheet in the
function at VA `0x140959be0`. It builds a 24-byte row: a byte at `+0x00` that
it sets to `0` and never fills from the sheet, the `CharacterKey` cell
truncated to a u16 at `+0x02`, `SkillPointExp` with `ReadColumnInt` at
`+0x04` and `GuildMoney` with `ReadColumnInt64` at `+0x08`, then 8 zero
bytes. The file holds the same order after its leading key (u8, u16, 4-byte
and 8-byte values), so `skill_point_exp` is an `i32` and `guild_money` an
`i64`. The 2016 client's debug symbols have no guild boss static status.

## Notes

- Client 1784 has the same 21-byte file, byte for byte.
- The same `u16 key | u8 1 | u16 character key` head starts the rows of
  [`fieldboss.dbss`](fieldboss_dbss.md) and
  [`weatheractor.dbss`](weatheractor_dbss.md), where the byte is `1` on every
  row as well.
- The Guild Boss Summon window (`panel_guild_bosssummon_all`) lists its
  bosses through `ToClient_bossSpawnList()` and `BossSpawnKey`, the
  [`boss_spawn.bss`](boss_spawn_bss.md) records, and never names this file.
  Of the 3,073 `.luac` files of client 3474, only the season character and
  EXP exchange windows hold the text `skillPointExp`, for the player's own
  skill EXP.

## Open Questions

### What the Row Rewards

`23014` Black Shadow is marked unfinished in its Korean label, and the
current guild boss summons come from `boss_spawn.bss`. Whether the server
still pays `skill_point_exp` and `guild_money` for a guild boss kill, and to
whom (each member's skill EXP, the guild's funds), is open; no client Lua or
UI text reads the table.

### unknown_02

The byte is `1` in the one row, and the client 1784 server loader leaves its
copy of it at `0`, so the data cannot tell a flag from a constant. The same
byte is `1` on every row of `fieldboss.dbss` and `weatheractor.dbss`.
