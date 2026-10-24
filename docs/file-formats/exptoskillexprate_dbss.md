# `exptoskillexprate.dbss` Format

## Purpose

An EXP to skill EXP rate per character level, levels `1` to `100`. The
rate is a server-only column, so the client file holds the levels and a
`0` for every rate. Companion `exptoskillexprateoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | -------------- | --------- |
| 1      | 1346 and later | 3483    | `exptoskillexprate.dbss`       | 1,204 | 100 Row        | 12        |
| 1      | 1346 and later | 3483    | `exptoskillexprateoffset.dbss` | 1,204 | 100 Offset Row | 12        |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 1      | `exptoskillexprate.dbss`       | 1,204 B (100.0%) | 0 B (0.0%) |
| 1      | `exptoskillexprateoffset.dbss` | 1,204 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `d31cf7fd3648`  |
| 3482   | Layout 1             | `d31cf7fd3648`  |
| 3474   | Layout 1             | `d31cf7fd3648`  |
| 3473   | Layout 1             | `d31cf7fd3648`  |
| 3464   | Layout 1             | `d31cf7fd3648`  |
| 3458   | Layout 1             | `d31cf7fd3648`  |
| 3454   | Layout 1             | `d31cf7fd3648`  |
| 3444   | Layout 1             | `d31cf7fd3648`  |
| 3435   | Layout 1             | `d31cf7fd3648`  |
| 3426   | Layout 1             | `d31cf7fd3648`  |
| 3418   | Layout 1             | `d31cf7fd3648`  |
| 3412   | Layout 1             | `d31cf7fd3648`  |
| 3402   | Layout 1             | `d31cf7fd3648`  |
| 3396   | Layout 1             | `d31cf7fd3648`  |
| 3387   | Layout 1             | `d31cf7fd3648`  |
| 3381   | Layout 1             | `d31cf7fd3648`  |
| 3373   | Layout 1             | `d31cf7fd3648`  |
| 3364   | Layout 1             | `d31cf7fd3648`  |
| 3356   | Layout 1             | `d31cf7fd3648`  |
| 3349   | Layout 1             | `d31cf7fd3648`  |
| 3342   | Layout 1             | `d31cf7fd3648`  |
| 3335   | Layout 1             | `d31cf7fd3648`  |
| 3326   | Layout 1             | `d31cf7fd3648`  |
| 3321   | Layout 1             | `d31cf7fd3648`  |
| 3314   | Layout 1             | `d31cf7fd3648`  |
| 3303   | Layout 1             | `d31cf7fd3648`  |
| 3302   | Layout 1             | `d31cf7fd3648`  |
| 3293   | Layout 1             | `d31cf7fd3648`  |
| 3283   | Layout 1             | `d31cf7fd3648`  |
| 3275   | Layout 1             | `d31cf7fd3648`  |
| 3267   | Layout 1             | `d31cf7fd3648`  |
| 3258   | Layout 1             | `d31cf7fd3648`  |
| 3251   | Layout 1             | `d31cf7fd3648`  |
| 3242   | Layout 1             | `d31cf7fd3648`  |
| 3235   | Layout 1             | `d31cf7fd3648`  |
| 3229   | Layout 1             | `d31cf7fd3648`  |
| 3212   | Layout 1             | `d31cf7fd3648`  |
| 3203   | Layout 1             | `d31cf7fd3648`  |
| 3193   | Layout 1             | `d31cf7fd3648`  |
| 3186   | Layout 1             | `d31cf7fd3648`  |
| 3177   | Layout 1             | `d31cf7fd3648`  |
| 3169   | Layout 1             | `d31cf7fd3648`  |
| 3158   | Layout 1             | `d31cf7fd3648`  |
| 3151   | Layout 1             | `d31cf7fd3648`  |
| 3144   | Layout 1             | `d31cf7fd3648`  |
| 3133   | Layout 1             | `d31cf7fd3648`  |
| 3125   | Layout 1             | `d31cf7fd3648`  |
| 3118   | Layout 1             | `d31cf7fd3648`  |
| 3111   | Layout 1             | `d31cf7fd3648`  |
| 3103   | Layout 1             | `d31cf7fd3648`  |
| 3095   | Layout 1             | `d31cf7fd3648`  |
| 3086   | Layout 1             | `d31cf7fd3648`  |
| 3072   | Layout 1             | `d31cf7fd3648`  |
| 3062   | Layout 1             | `d31cf7fd3648`  |
| 3052   | Layout 1             | `d31cf7fd3648`  |
| 3045   | Layout 1             | `d31cf7fd3648`  |
| 3037   | Layout 1             | `d31cf7fd3648`  |
| 3030   | Layout 1             | `d31cf7fd3648`  |
| 3021   | Layout 1             | `d31cf7fd3648`  |
| 3012   | Layout 1             | `d31cf7fd3648`  |
| 3002   | Layout 1             | `d31cf7fd3648`  |
| 2995   | Layout 1             | `d31cf7fd3648`  |
| 2987   | Layout 1             | `d31cf7fd3648`  |
| 2978   | Layout 1             | `d31cf7fd3648`  |
| 2970   | Layout 1             | `d31cf7fd3648`  |
| 2959   | Layout 1             | `d31cf7fd3648`  |
| 2951   | Layout 1             | `d31cf7fd3648`  |
| 2942   | Layout 1             | `d31cf7fd3648`  |
| 2935   | Layout 1             | `d31cf7fd3648`  |
| 2932   | Layout 1             | `d31cf7fd3648`  |
| 2923   | Layout 1             | `d31cf7fd3648`  |
| 2919   | Layout 1             | `d31cf7fd3648`  |
| 2907   | Layout 1             | `d31cf7fd3648`  |
| 2900   | Layout 1             | `d31cf7fd3648`  |
| 2891   | Layout 1             | `d31cf7fd3648`  |
| 2882   | Layout 1             | `d31cf7fd3648`  |
| 2872   | Layout 1             | `d31cf7fd3648`  |
| 2863   | Layout 1             | `d31cf7fd3648`  |
| 2855   | Layout 1             | `d31cf7fd3648`  |
| 2849   | Layout 1             | `d31cf7fd3648`  |
| 2844   | Layout 1             | `d31cf7fd3648`  |
| 2834   | Layout 1             | `d31cf7fd3648`  |
| 2825   | Layout 1             | `d31cf7fd3648`  |
| 2819   | Layout 1             | `d31cf7fd3648`  |
| 2811   | Layout 1             | `d31cf7fd3648`  |
| 2803   | Layout 1             | `d31cf7fd3648`  |
| 2794   | Layout 1             | `d31cf7fd3648`  |
| 2783   | Layout 1             | `d31cf7fd3648`  |
| 2774   | Layout 1             | `d31cf7fd3648`  |
| 2765   | Layout 1             | `d31cf7fd3648`  |
| 2756   | Layout 1             | `d31cf7fd3648`  |
| 2750   | Layout 1             | `d31cf7fd3648`  |
| 2743   | Layout 1             | `d31cf7fd3648`  |
| 2736   | Layout 1             | `d31cf7fd3648`  |
| 2726   | Layout 1             | `d31cf7fd3648`  |
| 2717   | Layout 1             | `d31cf7fd3648`  |
| 2709   | Layout 1             | `d31cf7fd3648`  |
| 2703   | Layout 1             | `d31cf7fd3648`  |
| 2695   | Layout 1             | `d31cf7fd3648`  |
| 2684   | Layout 1             | `d31cf7fd3648`  |
| 2672   | Layout 1             | `d31cf7fd3648`  |
| 2665   | Layout 1             | `d31cf7fd3648`  |
| 2657   | Layout 1             | `d31cf7fd3648`  |
| 2649   | Layout 1             | `d31cf7fd3648`  |
| 2644   | Layout 1             | `d31cf7fd3648`  |
| 2637   | Layout 1             | `d31cf7fd3648`  |
| 2629   | Layout 1             | `d31cf7fd3648`  |
| 2619   | Layout 1             | `d31cf7fd3648`  |
| 2612   | Layout 1             | `d31cf7fd3648`  |
| 2606   | Layout 1             | `d31cf7fd3648`  |
| 2602   | Layout 1             | `d31cf7fd3648`  |
| 2601   | Layout 1             | `d31cf7fd3648`  |
| 2592   | Layout 1             | `d31cf7fd3648`  |
| 2583   | Layout 1             | `d31cf7fd3648`  |
| 2575   | Layout 1             | `d31cf7fd3648`  |
| 2567   | Layout 1             | `d31cf7fd3648`  |
| 2560   | Layout 1             | `d31cf7fd3648`  |
| 2553   | Layout 1             | `d31cf7fd3648`  |
| 2545   | Layout 1             | `d31cf7fd3648`  |
| 2538   | Layout 1             | `d31cf7fd3648`  |
| 2529   | Layout 1             | `d31cf7fd3648`  |
| 2519   | Layout 1             | `d31cf7fd3648`  |
| 2513   | Layout 1             | `d31cf7fd3648`  |
| 2510   | Layout 1             | `d31cf7fd3648`  |
| 2507   | Layout 1             | `d31cf7fd3648`  |
| 2503   | Layout 1             | `d31cf7fd3648`  |
| 2498   | Layout 1             | `d31cf7fd3648`  |
| 2492   | Layout 1             | `d31cf7fd3648`  |
| 2487   | Layout 1             | `d31cf7fd3648`  |
| 2480   | Layout 1             | `d31cf7fd3648`  |
| 2474   | Layout 1             | `d31cf7fd3648`  |
| 2468   | Layout 1             | `d31cf7fd3648`  |
| 2460   | Layout 1             | `d31cf7fd3648`  |
| 2453   | Layout 1             | `d31cf7fd3648`  |
| 2444   | Layout 1             | `d31cf7fd3648`  |
| 2438   | Layout 1             | `d31cf7fd3648`  |
| 2434   | Layout 1             | `d31cf7fd3648`  |
| 2429   | Layout 1             | `d31cf7fd3648`  |
| 2421   | Layout 1             | `d31cf7fd3648`  |
| 2414   | Layout 1             | `d31cf7fd3648`  |
| 2407   | Layout 1             | `d31cf7fd3648`  |
| 2401   | Layout 1             | `d31cf7fd3648`  |
| 2397   | Layout 1             | `d31cf7fd3648`  |
| 2393   | Layout 1             | `d31cf7fd3648`  |
| 2384   | Layout 1             | `d31cf7fd3648`  |
| 2378   | Layout 1             | `d31cf7fd3648`  |
| 2372   | Layout 1             | `d31cf7fd3648`  |
| 2358   | Layout 1             | `d31cf7fd3648`  |
| 2352   | Layout 1             | `d31cf7fd3648`  |
| 2347   | Layout 1             | `d31cf7fd3648`  |
| 2343   | Layout 1             | `d31cf7fd3648`  |
| 2335   | Layout 1             | `d31cf7fd3648`  |
| 2327   | Layout 1             | `d31cf7fd3648`  |
| 2324   | Layout 1             | `d31cf7fd3648`  |
| 2319   | Layout 1             | `d31cf7fd3648`  |
| 2313   | Layout 1             | `d31cf7fd3648`  |
| 2308   | Layout 1             | `d31cf7fd3648`  |
| 2302   | Layout 1             | `d31cf7fd3648`  |
| 2295   | Layout 1             | `d31cf7fd3648`  |
| 2290   | Layout 1             | `d31cf7fd3648`  |
| 2284   | Layout 1             | `d31cf7fd3648`  |
| 2276   | Layout 1             | `d31cf7fd3648`  |
| 2269   | Layout 1             | `d31cf7fd3648`  |
| 2259   | Layout 1             | `d31cf7fd3648`  |
| 2250   | Layout 1             | `d31cf7fd3648`  |
| 2243   | Layout 1             | `d31cf7fd3648`  |
| 2235   | Layout 1             | `d31cf7fd3648`  |
| 2229   | Layout 1             | `d31cf7fd3648`  |
| 2224   | Layout 1             | `d31cf7fd3648`  |
| 2218   | Layout 1             | `d31cf7fd3648`  |
| 2215   | Layout 1             | `d31cf7fd3648`  |
| 2207   | Layout 1             | `d31cf7fd3648`  |
| 2203   | Layout 1             | `d31cf7fd3648`  |
| 2196   | Layout 1             | `d31cf7fd3648`  |
| 2192   | Layout 1             | `d31cf7fd3648`  |
| 2189   | Layout 1             | `d31cf7fd3648`  |
| 2183   | Layout 1             | `d31cf7fd3648`  |
| 2179   | Layout 1             | `d31cf7fd3648`  |
| 2171   | Layout 1             | `d31cf7fd3648`  |
| 2163   | Layout 1             | `d31cf7fd3648`  |
| 2156   | Layout 1             | `d31cf7fd3648`  |
| 2151   | Layout 1             | `d31cf7fd3648`  |
| 2147   | Layout 1             | `d31cf7fd3648`  |
| 2142   | Layout 1             | `d31cf7fd3648`  |
| 2138   | Layout 1             | `d31cf7fd3648`  |
| 2134   | Layout 1             | `d31cf7fd3648`  |
| 2130   | Layout 1             | `d31cf7fd3648`  |
| 2122   | Layout 1             | `d31cf7fd3648`  |
| 2107   | Layout 1             | `d31cf7fd3648`  |
| 2098   | Layout 1             | `d31cf7fd3648`  |
| 2089   | Layout 1             | `d31cf7fd3648`  |
| 2081   | Layout 1             | `d31cf7fd3648`  |
| 2073   | Layout 1             | `d31cf7fd3648`  |
| 2067   | Layout 1             | `d31cf7fd3648`  |
| 2063   | Layout 1             | `d31cf7fd3648`  |
| 2059   | Layout 1             | `d31cf7fd3648`  |
| 2052   | Layout 1             | `d31cf7fd3648`  |
| 2044   | Layout 1             | `d31cf7fd3648`  |
| 2039   | Layout 1             | `d31cf7fd3648`  |
| 2032   | Layout 1             | `d31cf7fd3648`  |
| 2025   | Layout 1             | `d31cf7fd3648`  |
| 2011   | Layout 1             | `d31cf7fd3648`  |
| 2005   | Layout 1             | `d31cf7fd3648`  |
| 2000   | Layout 1             | `d31cf7fd3648`  |
| 1996   | Layout 1             | `d31cf7fd3648`  |
| 1991   | Layout 1             | `d31cf7fd3648`  |
| 1985   | Layout 1             | `d31cf7fd3648`  |
| 1980   | Layout 1             | `d31cf7fd3648`  |
| 1969   | Layout 1             | `d31cf7fd3648`  |
| 1964   | Layout 1             | `d31cf7fd3648`  |
| 1958   | Layout 1             | `d31cf7fd3648`  |
| 1950   | Layout 1             | `d31cf7fd3648`  |
| 1945   | Layout 1             | `d31cf7fd3648`  |
| 1937   | Layout 1             | `d31cf7fd3648`  |
| 1933   | Layout 1             | `d31cf7fd3648`  |
| 1927   | Layout 1             | `d31cf7fd3648`  |
| 1921   | Layout 1             | `d31cf7fd3648`  |
| 1914   | Layout 1             | `d31cf7fd3648`  |
| 1908   | Layout 1             | `d31cf7fd3648`  |
| 1897   | Layout 1             | `d31cf7fd3648`  |
| 1892   | Layout 1             | `d31cf7fd3648`  |
| 1886   | Layout 1             | `d31cf7fd3648`  |
| 1881   | Layout 1             | `d31cf7fd3648`  |
| 1871   | Layout 1             | `d31cf7fd3648`  |
| 1866   | Layout 1             | `d31cf7fd3648`  |
| 1862   | Layout 1             | `d31cf7fd3648`  |
| 1854   | Layout 1             | `d31cf7fd3648`  |
| 1846   | Layout 1             | `d31cf7fd3648`  |
| 1838   | Layout 1             | `d31cf7fd3648`  |
| 1832   | Layout 1             | `d31cf7fd3648`  |
| 1826   | Layout 1             | `d31cf7fd3648`  |
| 1822   | Layout 1             | `d31cf7fd3648`  |
| 1818   | Layout 1             | `d31cf7fd3648`  |
| 1804   | Layout 1             | `d31cf7fd3648`  |
| 1794   | Layout 1             | `d31cf7fd3648`  |
| 1790   | Layout 1             | `d31cf7fd3648`  |
| 1784   | Layout 1             | `d31cf7fd3648`  |
| 1774   | Layout 1             | `d31cf7fd3648`  |
| 1771   | Layout 1             | `d31cf7fd3648`  |
| 1762   | Layout 1             | `d31cf7fd3648`  |
| 1759   | Layout 1             | `d31cf7fd3648`  |
| 1754   | Layout 1             | `d31cf7fd3648`  |
| 1749   | Layout 1             | `d31cf7fd3648`  |
| 1743   | Layout 1             | `d31cf7fd3648`  |
| 1737   | Layout 1             | `d31cf7fd3648`  |
| 1731   | Layout 1             | `d31cf7fd3648`  |
| 1725   | Layout 1             | `d31cf7fd3648`  |
| 1717   | Layout 1             | `d31cf7fd3648`  |
| 1710   | Layout 1             | `d31cf7fd3648`  |
| 1704   | Layout 1             | `d31cf7fd3648`  |
| 1698   | Layout 1             | `d31cf7fd3648`  |
| 1690   | Layout 1             | `d31cf7fd3648`  |
| 1685   | Layout 1             | `d31cf7fd3648`  |
| 1680   | Layout 1             | `d31cf7fd3648`  |
| 1674   | Layout 1             | `d31cf7fd3648`  |
| 1668   | Layout 1             | `d31cf7fd3648`  |
| 1659   | Layout 1             | `d31cf7fd3648`  |
| 1649   | Layout 1             | `d31cf7fd3648`  |
| 1642   | Layout 1             | `d31cf7fd3648`  |
| 1636   | Layout 1             | `d31cf7fd3648`  |
| 1628   | Layout 1             | `d31cf7fd3648`  |
| 1622   | Layout 1             | `d31cf7fd3648`  |
| 1614   | Layout 1             | `d31cf7fd3648`  |
| 1608   | Layout 1             | `d31cf7fd3648`  |
| 1602   | Layout 1             | `d31cf7fd3648`  |
| 1598   | Layout 1             | `d31cf7fd3648`  |
| 1594   | Layout 1             | `d31cf7fd3648`  |
| 1590   | Layout 1             | `d31cf7fd3648`  |
| 1587   | Layout 1             | `d31cf7fd3648`  |
| 1584   | Layout 1             | `d31cf7fd3648`  |
| 1579   | Layout 1             | `d31cf7fd3648`  |
| 1572   | Layout 1             | `d31cf7fd3648`  |
| 1565   | Layout 1             | `d31cf7fd3648`  |
| 1559   | Layout 1             | `d31cf7fd3648`  |
| 1554   | Layout 1             | `d31cf7fd3648`  |
| 1547   | Layout 1             | `d31cf7fd3648`  |
| 1537   | Layout 1             | `d31cf7fd3648`  |
| 1529   | Layout 1             | `d31cf7fd3648`  |
| 1524   | Layout 1             | `d31cf7fd3648`  |
| 1519   | Layout 1             | `d31cf7fd3648`  |
| 1509   | Layout 1             | `d31cf7fd3648`  |
| 1506   | Layout 1             | `d31cf7fd3648`  |
| 1504   | Layout 1             | `d31cf7fd3648`  |
| 1500   | Layout 1             | `d31cf7fd3648`  |
| 1493   | Layout 1             | `d31cf7fd3648`  |
| 1489   | Layout 1             | `d31cf7fd3648`  |
| 1485   | Layout 1             | `d31cf7fd3648`  |
| 1481   | Layout 1             | `d31cf7fd3648`  |
| 1474   | Layout 1             | `d31cf7fd3648`  |
| 1466   | Layout 1             | `d31cf7fd3648`  |
| 1462   | Layout 1             | `d31cf7fd3648`  |
| 1459   | Layout 1             | `d31cf7fd3648`  |
| 1453   | Layout 1             | `d31cf7fd3648`  |
| 1450   | Layout 1             | `d31cf7fd3648`  |
| 1445   | Layout 1             | `d31cf7fd3648`  |
| 1439   | Layout 1             | `d31cf7fd3648`  |
| 1433   | Layout 1             | `d31cf7fd3648`  |
| 1430   | Layout 1             | `d31cf7fd3648`  |
| 1426   | Layout 1             | `d31cf7fd3648`  |
| 1421   | Layout 1             | `d31cf7fd3648`  |
| 1417   | Layout 1             | `d31cf7fd3648`  |
| 1416   | Layout 1             | `d31cf7fd3648`  |
| 1409   | Layout 1             | `d31cf7fd3648`  |
| 1405   | Layout 1             | `d31cf7fd3648`  |
| 1401   | Layout 1             | `d31cf7fd3648`  |
| 1396   | Layout 1             | `d31cf7fd3648`  |
| 1391   | Layout 1             | `d31cf7fd3648`  |
| 1390   | Layout 1             | `d31cf7fd3648`  |
| 1386   | Layout 1             | `d31cf7fd3648`  |
| 1381   | Layout 1             | `d31cf7fd3648`  |
| 1379   | Layout 1             | `d31cf7fd3648`  |
| 1372   | Layout 1             | `d31cf7fd3648`  |
| 1366   | Layout 1             | `d31cf7fd3648`  |
| 1364   | Layout 1             | `d31cf7fd3648`  |
| 1363   | Layout 1             | `d31cf7fd3648`  |
| 1360   | Layout 1             | `d31cf7fd3648`  |
| 1358   | Layout 1             | `d31cf7fd3648`  |
| 1355   | Layout 1             | `d31cf7fd3648`  |
| 1351   | Layout 1             | `d31cf7fd3648`  |
| 1348   | Layout 1             | `d31cf7fd3648`  |
| 1346   | Layout 1             | `d31cf7fd3648`  |
| 1341   | No documented layout | `d31cf7fd3648`  |
| 1340   | No documented layout | `d31cf7fd3648`  |
| 1338   | No documented layout | `d31cf7fd3648`  |
| 1335   | No documented layout | `d31cf7fd3648`  |
| 1333   | No documented layout | `d31cf7fd3648`  |
| 1329   | No documented layout | `d31cf7fd3648`  |
| 1327   | No documented layout | `d31cf7fd3648`  |
| 1324   | No documented layout | `d31cf7fd3648`  |
| 1321   | No documented layout | `d31cf7fd3648`  |
| 1319   | No documented layout | `d31cf7fd3648`  |
| 1318   | No documented layout | `d31cf7fd3648`  |
| 1316   | No documented layout | `d31cf7fd3648`  |
| 1313   | No documented layout | `d31cf7fd3648`  |
| 1311   | No documented layout | `d31cf7fd3648`  |
| 1309   | No documented layout | `d31cf7fd3648`  |
| 1304   | No documented layout | `d31cf7fd3648`  |
| 1292   | No documented layout | `d31cf7fd3648`  |
| 1286   | No documented layout | `d31cf7fd3648`  |
| 1280   | No documented layout | `d31cf7fd3648`  |
| 1276   | No documented layout | `d31cf7fd3648`  |
| 1267   | No file              | `d31cf7fd3648`  |
| 1261   | No file              | `d31cf7fd3648`  |
| 1256   | No file              | `d31cf7fd3648`  |
| 1250   | No file              | `d31cf7fd3648`  |
| 1246   | No file              | `d31cf7fd3648`  |
| 1239   | No file              | `d31cf7fd3648`  |
| 1230   | No file              | `d31cf7fd3648`  |
| 1226   | No file              | `d31cf7fd3648`  |
| 1220   | No file              | `d31cf7fd3648`  |
| 1217   | No file              | `d31cf7fd3648`  |
| 1211   | No file              | `d31cf7fd3648`  |
| 1210   | No file              | `d31cf7fd3648`  |
| 1208   | No file              | `d31cf7fd3648`  |
| 1203   | No file              | `d31cf7fd3648`  |
| 1197   | No file              | `d31cf7fd3648`  |
| 1194   | No file              | `d31cf7fd3648`  |
| 1192   | No file              | `d31cf7fd3648`  |
| 1187   | No file              | `d31cf7fd3648`  |
| 1183   | No file              | `d31cf7fd3648`  |
| 1177   | No file              | `d31cf7fd3648`  |
| 1173   | No file              | `d31cf7fd3648`  |
| 1167   | No file              | `d31cf7fd3648`  |
| 1164   | No file              | `d31cf7fd3648`  |
| 1156   | No file              | `d31cf7fd3648`  |
| 1149   | No file              | `d31cf7fd3648`  |
| 1144   | No file              | `d31cf7fd3648`  |
| 1137   | No file              | `d31cf7fd3648`  |
| 1132   | No file              | `d31cf7fd3648`  |
| 1127   | No file              | `d31cf7fd3648`  |
| 1122   | No file              | `d31cf7fd3648`  |
| 1118   | No file              | `d31cf7fd3648`  |
| 1114   | No file              | `d31cf7fd3648`  |
| 1109   | No file              | `d31cf7fd3648`  |
| 1102   | No file              | `d31cf7fd3648`  |
| 1096   | No file              | `d31cf7fd3648`  |
| 1088   | No file              | `d31cf7fd3648`  |
| 1081   | No file              | `d31cf7fd3648`  |
| 1076   | No file              | `d31cf7fd3648`  |
| 1069   | No file              | `d31cf7fd3648`  |
| 1064   | No file              | `d31cf7fd3648`  |
| 1058   | No file              | `d31cf7fd3648`  |
| 1051   | No file              | `d31cf7fd3648`  |
| 1044   | No file              | `d31cf7fd3648`  |
| 1036   | No file              | `d31cf7fd3648`  |
| 1026   | No file              | `d31cf7fd3648`  |
| 1016   | No file              | `d31cf7fd3648`  |
| 1009   | No file              | `d31cf7fd3648`  |
| 1005   | No file              | `d31cf7fd3648`  |
| 1000   | No file              | `d31cf7fd3648`  |
| 998    | No file              | `d31cf7fd3648`  |
| 990    | No file              | `d31cf7fd3648`  |
| 979    | No file              | `d31cf7fd3648`  |
| 972    | No file              | `d31cf7fd3648`  |
| 963    | No file              | `d31cf7fd3648`  |
| 955    | No file              | `d31cf7fd3648`  |
| 946    | No file              | `d31cf7fd3648`  |
| 938    | No file              | `d31cf7fd3648`  |
| 927    | No file              | `d31cf7fd3648`  |
| 911    | No file              | `d31cf7fd3648`  |
| 904    | No file              | `d31cf7fd3648`  |
| 899    | No file              | `d31cf7fd3648`  |
| 894    | No file              | `d31cf7fd3648`  |
| 885    | No file              | `d31cf7fd3648`  |
| 879    | No file              | `d31cf7fd3648`  |
| 872    | No file              | `d31cf7fd3648`  |
| 864    | No file              | `d31cf7fd3648`  |
| 855    | No file              | `d31cf7fd3648`  |
| 853    | No file              | `d31cf7fd3648`  |
| 845    | No file              | `d31cf7fd3648`  |
| 837    | No file              | `d31cf7fd3648`  |
| 829    | No file              | `d31cf7fd3648`  |
| 822    | No file              | `d31cf7fd3648`  |
| 814    | No file              | `d31cf7fd3648`  |
| 805    | No file              | `d31cf7fd3648`  |
| 794    | No file              | `d31cf7fd3648`  |
| 787    | No file              | `d31cf7fd3648`  |
| 780    | No file              | `d31cf7fd3648`  |
| 771    | No file              | `d31cf7fd3648`  |
| 760    | No file              | `d31cf7fd3648`  |
| 748    | No file              | `d31cf7fd3648`  |
| 741    | No file              | `d31cf7fd3648`  |
| 736    | No file              | `d31cf7fd3648`  |
| 731    | No file              | `d31cf7fd3648`  |
| 723    | No file              | `d31cf7fd3648`  |
| 711    | No file              | `d31cf7fd3648`  |
| 707    | No file              | `d31cf7fd3648`  |
| 697    | No file              | `d31cf7fd3648`  |
| 689    | No file              | `d31cf7fd3648`  |
| 683    | No file              | `d31cf7fd3648`  |
| 678    | No file              | `d31cf7fd3648`  |
| 670    | No file              | `d31cf7fd3648`  |
| 661    | No file              | `d31cf7fd3648`  |
| 656    | No file              | `d31cf7fd3648`  |
| 652    | No file              | `d31cf7fd3648`  |
| 643    | No file              | `d31cf7fd3648`  |
| 637    | No file              | `d31cf7fd3648`  |
| 630    | No file              | `d31cf7fd3648`  |
| 627    | No file              | `d31cf7fd3648`  |
| 621    | No file              | `d31cf7fd3648`  |
| 617    | No file              | `d31cf7fd3648`  |
| 615    | No file              | `d31cf7fd3648`  |
| 606    | No file              | `d31cf7fd3648`  |
| 599    | No file              | `d31cf7fd3648`  |
| 592    | No file              | `d31cf7fd3648`  |
| 586    | No file              | `d31cf7fd3648`  |
| 577    | No file              | `d31cf7fd3648`  |
| 569    | No file              | `d31cf7fd3648`  |
| 561    | No file              | `d31cf7fd3648`  |
| 554    | No file              | `d31cf7fd3648`  |
| 542    | No file              | `d31cf7fd3648`  |
| 532    | No file              | `d31cf7fd3648`  |
| 531    | No file              | `d31cf7fd3648`  |
| 526    | No file              | `d31cf7fd3648`  |
| 521    | No file              | `d31cf7fd3648`  |
| 517    | No file              | `d31cf7fd3648`  |
| 510    | No file              | `d31cf7fd3648`  |
| 508    | No file              | `d31cf7fd3648`  |
| 504    | No file              | `d31cf7fd3648`  |
| 497    | No file              | `d31cf7fd3648`  |
| 491    | No file              | `d31cf7fd3648`  |
| 485    | No file              | `d31cf7fd3648`  |
| 478    | No file              | `d31cf7fd3648`  |
| 472    | No file              | `d31cf7fd3648`  |
| 466    | No file              | `d31cf7fd3648`  |
| 457    | No file              | `d31cf7fd3648`  |
| 452    | No file              | `d31cf7fd3648`  |
| 449    | No file              | `d31cf7fd3648`  |
| 435    | No file              | `d31cf7fd3648`  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                                  |
| ------------------------------ | -------- | --------------------------------------------------------------------- |
| `exptoskillexprateoffset.dbss` | Optional | `level -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 100 x 12 = 1,204 bytes.

### Row (12 bytes)

| Offset  | Type | Field                 | Notes                                                                       |
| ------- | ---- | --------------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | level                 | Character level, the row key; `1` to `count` in order                        |
| `+0x04` | u32  | level_dup             | Equal to `level` on every row; the offset index points here                  |
| `+0x08` | u32  | exp_to_skill_exp_rate | `0` on every row of clients 1784 and 3474, see Field Names                   |

### `exptoskillexprateoffset.dbss`

Bare offset table into `exptoskillexprate.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                     |
| ------- | ----------------- | ----- | ----------------------------------------- |
| `+0x00` | u32               | count | Equals the `exptoskillexprate.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                            |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | level       | Key of the row it points at             |
| `+0x04` | u32  | data_offset | Row start + 4, at `level_dup`           |
| `+0x08` | u32  | data_size   | `8` on every row: the row less its key  |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in level order, as the file; on clients 1784 and 3474 every
index row points at the row with its key.

## Field Names

The 2016 client's debug symbols have `gc::ExpToSkillExpRateStaticStatus`
as `_level` and `_expToSkillExpRate` (8 bytes): the part of the row the
offset index points at. The `ExpToSkillExpRate_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784 has the columns `Level` and
`ExpToSkillExpRate`; its 100 rows match the file on all 100 levels and
both values, on client 1784 and on client 3474. In the `.xlsm` copy of the
sheet (`datasheet_pcdatatable.xlsm`) the column is `%ExpToSkillExpRate`,
server-only, which the client build writes as `0`; the sheet's values are
`0` as well. Its note columns `#필요 스킬 포인트` (skill points needed) and
`#필요 PC 경험치` (character EXP needed) are not compiled.

## Notes

- No client Lua names the table or a getter for it.
