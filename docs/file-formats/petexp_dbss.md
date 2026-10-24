# `petexp.dbss` Format

## Purpose

Defines pet experience curves keyed by EXP table ID. Each record stores a maximum pet level and per-level u64 EXP thresholds. Companion `petexpoffset.dbss` provides keyed lookup into this fixed-size record stream.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------------------------ | --------- |
| 2      | 1964 and later | 3483    | `petexp.dbss`       | 3,676 | 9 Data Payload, 9 Record | 406       |
| 2      | 1964 and later | 3483    | `petexpoffset.dbss` | 94    | 9 Offset Row             | 10        |
| 1      | 1346 to 1958   | 1958    | `petexp.dbss`       | 2,956 | 9 Data Payload, 9 Record | 326       |
| 1      | 1346 to 1958   | 1958    | `petexpoffset.dbss` | 94    | 9 Offset Row             | 10        |

| Layout | File                | Known            | Unknown    |
| ------ | ------------------- | ---------------- | ---------- |
| 2      | `petexp.dbss`       | 3,676 B (100.0%) | 0 B (0.0%) |
| 2      | `petexpoffset.dbss` | 94 B (100.0%)    | 0 B (0.0%) |
| 1      | `petexp.dbss`       | 2,956 B (100.0%) | 0 B (0.0%) |
| 1      | `petexpoffset.dbss` | 94 B (100.0%)    | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `539a6d90b677`  |
| 3482   | Layout 2             | `539a6d90b677`  |
| 3474   | Layout 2             | `539a6d90b677`  |
| 3473   | Layout 2             | `539a6d90b677`  |
| 3464   | Layout 2             | `539a6d90b677`  |
| 3458   | Layout 2             | `539a6d90b677`  |
| 3454   | Layout 2             | `539a6d90b677`  |
| 3444   | Layout 2             | `539a6d90b677`  |
| 3435   | Layout 2             | `539a6d90b677`  |
| 3426   | Layout 2             | `539a6d90b677`  |
| 3418   | Layout 2             | `539a6d90b677`  |
| 3412   | Layout 2             | `539a6d90b677`  |
| 3402   | Layout 2             | `539a6d90b677`  |
| 3396   | Layout 2             | `539a6d90b677`  |
| 3387   | Layout 2             | `539a6d90b677`  |
| 3381   | Layout 2             | `539a6d90b677`  |
| 3373   | Layout 2             | `539a6d90b677`  |
| 3364   | Layout 2             | `539a6d90b677`  |
| 3356   | Layout 2             | `539a6d90b677`  |
| 3349   | Layout 2             | `539a6d90b677`  |
| 3342   | Layout 2             | `539a6d90b677`  |
| 3335   | Layout 2             | `539a6d90b677`  |
| 3326   | Layout 2             | `539a6d90b677`  |
| 3321   | Layout 2             | `539a6d90b677`  |
| 3314   | Layout 2             | `539a6d90b677`  |
| 3303   | Layout 2             | `539a6d90b677`  |
| 3302   | Layout 2             | `539a6d90b677`  |
| 3293   | Layout 2             | `539a6d90b677`  |
| 3283   | Layout 2             | `539a6d90b677`  |
| 3275   | Layout 2             | `539a6d90b677`  |
| 3267   | Layout 2             | `539a6d90b677`  |
| 3258   | Layout 2             | `539a6d90b677`  |
| 3251   | Layout 2             | `539a6d90b677`  |
| 3242   | Layout 2             | `539a6d90b677`  |
| 3235   | Layout 2             | `539a6d90b677`  |
| 3229   | Layout 2             | `539a6d90b677`  |
| 3212   | Layout 2             | `539a6d90b677`  |
| 3203   | Layout 2             | `539a6d90b677`  |
| 3193   | Layout 2             | `539a6d90b677`  |
| 3186   | Layout 2             | `539a6d90b677`  |
| 3177   | Layout 2             | `539a6d90b677`  |
| 3169   | Layout 2             | `539a6d90b677`  |
| 3158   | Layout 2             | `539a6d90b677`  |
| 3151   | Layout 2             | `539a6d90b677`  |
| 3144   | Layout 2             | `539a6d90b677`  |
| 3133   | Layout 2             | `539a6d90b677`  |
| 3125   | Layout 2             | `539a6d90b677`  |
| 3118   | Layout 2             | `539a6d90b677`  |
| 3111   | Layout 2             | `539a6d90b677`  |
| 3103   | Layout 2             | `539a6d90b677`  |
| 3095   | Layout 2             | `539a6d90b677`  |
| 3086   | Layout 2             | `539a6d90b677`  |
| 3072   | Layout 2             | `539a6d90b677`  |
| 3062   | Layout 2             | `539a6d90b677`  |
| 3052   | Layout 2             | `539a6d90b677`  |
| 3045   | Layout 2             | `539a6d90b677`  |
| 3037   | Layout 2             | `539a6d90b677`  |
| 3030   | Layout 2             | `539a6d90b677`  |
| 3021   | Layout 2             | `539a6d90b677`  |
| 3012   | Layout 2             | `539a6d90b677`  |
| 3002   | Layout 2             | `539a6d90b677`  |
| 2995   | Layout 2             | `539a6d90b677`  |
| 2987   | Layout 2             | `539a6d90b677`  |
| 2978   | Layout 2             | `539a6d90b677`  |
| 2970   | Layout 2             | `539a6d90b677`  |
| 2959   | Layout 2             | `539a6d90b677`  |
| 2951   | Layout 2             | `539a6d90b677`  |
| 2942   | Layout 2             | `539a6d90b677`  |
| 2935   | Layout 2             | `539a6d90b677`  |
| 2932   | Layout 2             | `539a6d90b677`  |
| 2923   | Layout 2             | `539a6d90b677`  |
| 2919   | Layout 2             | `539a6d90b677`  |
| 2907   | Layout 2             | `539a6d90b677`  |
| 2900   | Layout 2             | `539a6d90b677`  |
| 2891   | Layout 2             | `539a6d90b677`  |
| 2882   | Layout 2             | `539a6d90b677`  |
| 2872   | Layout 2             | `539a6d90b677`  |
| 2863   | Layout 2             | `539a6d90b677`  |
| 2855   | Layout 2             | `539a6d90b677`  |
| 2849   | Layout 2             | `539a6d90b677`  |
| 2844   | Layout 2             | `539a6d90b677`  |
| 2834   | Layout 2             | `539a6d90b677`  |
| 2825   | Layout 2             | `539a6d90b677`  |
| 2819   | Layout 2             | `539a6d90b677`  |
| 2811   | Layout 2             | `539a6d90b677`  |
| 2803   | Layout 2             | `539a6d90b677`  |
| 2794   | Layout 2             | `539a6d90b677`  |
| 2783   | Layout 2             | `539a6d90b677`  |
| 2774   | Layout 2             | `539a6d90b677`  |
| 2765   | Layout 2             | `539a6d90b677`  |
| 2756   | Layout 2             | `539a6d90b677`  |
| 2750   | Layout 2             | `539a6d90b677`  |
| 2743   | Layout 2             | `539a6d90b677`  |
| 2736   | Layout 2             | `539a6d90b677`  |
| 2726   | Layout 2             | `539a6d90b677`  |
| 2717   | Layout 2             | `539a6d90b677`  |
| 2709   | Layout 2             | `539a6d90b677`  |
| 2703   | Layout 2             | `539a6d90b677`  |
| 2695   | Layout 2             | `539a6d90b677`  |
| 2684   | Layout 2             | `539a6d90b677`  |
| 2672   | Layout 2             | `539a6d90b677`  |
| 2665   | Layout 2             | `539a6d90b677`  |
| 2657   | Layout 2             | `539a6d90b677`  |
| 2649   | Layout 2             | `539a6d90b677`  |
| 2644   | Layout 2             | `539a6d90b677`  |
| 2637   | Layout 2             | `539a6d90b677`  |
| 2629   | Layout 2             | `539a6d90b677`  |
| 2619   | Layout 2             | `539a6d90b677`  |
| 2612   | Layout 2             | `539a6d90b677`  |
| 2606   | Layout 2             | `539a6d90b677`  |
| 2602   | Layout 2             | `539a6d90b677`  |
| 2601   | Layout 2             | `539a6d90b677`  |
| 2592   | Layout 2             | `539a6d90b677`  |
| 2583   | Layout 2             | `539a6d90b677`  |
| 2575   | Layout 2             | `539a6d90b677`  |
| 2567   | Layout 2             | `539a6d90b677`  |
| 2560   | Layout 2             | `539a6d90b677`  |
| 2553   | Layout 2             | `539a6d90b677`  |
| 2545   | Layout 2             | `539a6d90b677`  |
| 2538   | Layout 2             | `539a6d90b677`  |
| 2529   | Layout 2             | `539a6d90b677`  |
| 2519   | Layout 2             | `539a6d90b677`  |
| 2513   | Layout 2             | `539a6d90b677`  |
| 2510   | Layout 2             | `539a6d90b677`  |
| 2507   | Layout 2             | `539a6d90b677`  |
| 2503   | Layout 2             | `539a6d90b677`  |
| 2498   | Layout 2             | `539a6d90b677`  |
| 2492   | Layout 2             | `539a6d90b677`  |
| 2487   | Layout 2             | `539a6d90b677`  |
| 2480   | Layout 2             | `539a6d90b677`  |
| 2474   | Layout 2             | `539a6d90b677`  |
| 2468   | Layout 2             | `539a6d90b677`  |
| 2460   | Layout 2             | `539a6d90b677`  |
| 2453   | Layout 2             | `539a6d90b677`  |
| 2444   | Layout 2             | `539a6d90b677`  |
| 2438   | Layout 2             | `539a6d90b677`  |
| 2434   | Layout 2             | `539a6d90b677`  |
| 2429   | Layout 2             | `539a6d90b677`  |
| 2421   | Layout 2             | `539a6d90b677`  |
| 2414   | Layout 2             | `539a6d90b677`  |
| 2407   | Layout 2             | `539a6d90b677`  |
| 2401   | Layout 2             | `539a6d90b677`  |
| 2397   | Layout 2             | `539a6d90b677`  |
| 2393   | Layout 2             | `539a6d90b677`  |
| 2384   | Layout 2             | `539a6d90b677`  |
| 2378   | Layout 2             | `539a6d90b677`  |
| 2372   | Layout 2             | `539a6d90b677`  |
| 2358   | Layout 2             | `539a6d90b677`  |
| 2352   | Layout 2             | `539a6d90b677`  |
| 2347   | Layout 2             | `539a6d90b677`  |
| 2343   | Layout 2             | `539a6d90b677`  |
| 2335   | Layout 2             | `539a6d90b677`  |
| 2327   | Layout 2             | `539a6d90b677`  |
| 2324   | Layout 2             | `539a6d90b677`  |
| 2319   | Layout 2             | `539a6d90b677`  |
| 2313   | Layout 2             | `539a6d90b677`  |
| 2308   | Layout 2             | `539a6d90b677`  |
| 2302   | Layout 2             | `539a6d90b677`  |
| 2295   | Layout 2             | `539a6d90b677`  |
| 2290   | Layout 2             | `539a6d90b677`  |
| 2284   | Layout 2             | `539a6d90b677`  |
| 2276   | Layout 2             | `539a6d90b677`  |
| 2269   | Layout 2             | `539a6d90b677`  |
| 2259   | Layout 2             | `539a6d90b677`  |
| 2250   | Layout 2             | `539a6d90b677`  |
| 2243   | Layout 2             | `539a6d90b677`  |
| 2235   | Layout 2             | `539a6d90b677`  |
| 2229   | Layout 2             | `539a6d90b677`  |
| 2224   | Layout 2             | `539a6d90b677`  |
| 2218   | Layout 2             | `539a6d90b677`  |
| 2215   | Layout 2             | `539a6d90b677`  |
| 2207   | Layout 2             | `539a6d90b677`  |
| 2203   | Layout 2             | `539a6d90b677`  |
| 2196   | Layout 2             | `539a6d90b677`  |
| 2192   | Layout 2             | `539a6d90b677`  |
| 2189   | Layout 2             | `539a6d90b677`  |
| 2183   | Layout 2             | `539a6d90b677`  |
| 2179   | Layout 2             | `539a6d90b677`  |
| 2171   | Layout 2             | `539a6d90b677`  |
| 2163   | Layout 2             | `539a6d90b677`  |
| 2156   | Layout 2             | `539a6d90b677`  |
| 2151   | Layout 2             | `539a6d90b677`  |
| 2147   | Layout 2             | `539a6d90b677`  |
| 2142   | Layout 2             | `539a6d90b677`  |
| 2138   | Layout 2             | `539a6d90b677`  |
| 2134   | Layout 2             | `539a6d90b677`  |
| 2130   | Layout 2             | `539a6d90b677`  |
| 2122   | Layout 2             | `539a6d90b677`  |
| 2107   | Layout 2             | `539a6d90b677`  |
| 2098   | Layout 2             | `539a6d90b677`  |
| 2089   | Layout 2             | `539a6d90b677`  |
| 2081   | Layout 2             | `539a6d90b677`  |
| 2073   | Layout 2             | `539a6d90b677`  |
| 2067   | Layout 2             | `539a6d90b677`  |
| 2063   | Layout 2             | `539a6d90b677`  |
| 2059   | Layout 2             | `539a6d90b677`  |
| 2052   | Layout 2             | `539a6d90b677`  |
| 2044   | Layout 2             | `539a6d90b677`  |
| 2039   | Layout 2             | `539a6d90b677`  |
| 2032   | Layout 2             | `539a6d90b677`  |
| 2025   | Layout 2             | `539a6d90b677`  |
| 2011   | Layout 2             | `539a6d90b677`  |
| 2005   | Layout 2             | `539a6d90b677`  |
| 2000   | Layout 2             | `539a6d90b677`  |
| 1996   | Layout 2             | `539a6d90b677`  |
| 1991   | Layout 2             | `539a6d90b677`  |
| 1985   | Layout 2             | `539a6d90b677`  |
| 1980   | Layout 2             | `539a6d90b677`  |
| 1969   | Layout 2             | `539a6d90b677`  |
| 1964   | Layout 2             | `539a6d90b677`  |
| 1958   | Layout 1             | `539a6d90b677`  |
| 1950   | Layout 1             | `539a6d90b677`  |
| 1945   | Layout 1             | `539a6d90b677`  |
| 1937   | Layout 1             | `539a6d90b677`  |
| 1933   | Layout 1             | `539a6d90b677`  |
| 1927   | Layout 1             | `539a6d90b677`  |
| 1921   | Layout 1             | `539a6d90b677`  |
| 1914   | Layout 1             | `539a6d90b677`  |
| 1908   | Layout 1             | `539a6d90b677`  |
| 1897   | Layout 1             | `539a6d90b677`  |
| 1892   | Layout 1             | `539a6d90b677`  |
| 1886   | Layout 1             | `539a6d90b677`  |
| 1881   | Layout 1             | `539a6d90b677`  |
| 1871   | Layout 1             | `539a6d90b677`  |
| 1866   | Layout 1             | `539a6d90b677`  |
| 1862   | Layout 1             | `539a6d90b677`  |
| 1854   | Layout 1             | `539a6d90b677`  |
| 1846   | Layout 1             | `539a6d90b677`  |
| 1838   | Layout 1             | `539a6d90b677`  |
| 1832   | Layout 1             | `539a6d90b677`  |
| 1826   | Layout 1             | `539a6d90b677`  |
| 1822   | Layout 1             | `539a6d90b677`  |
| 1818   | Layout 1             | `539a6d90b677`  |
| 1804   | Layout 1             | `539a6d90b677`  |
| 1794   | Layout 1             | `539a6d90b677`  |
| 1790   | Layout 1             | `539a6d90b677`  |
| 1784   | Layout 1             | `539a6d90b677`  |
| 1774   | Layout 1             | `539a6d90b677`  |
| 1771   | Layout 1             | `539a6d90b677`  |
| 1762   | Layout 1             | `539a6d90b677`  |
| 1759   | Layout 1             | `539a6d90b677`  |
| 1754   | Layout 1             | `539a6d90b677`  |
| 1749   | Layout 1             | `539a6d90b677`  |
| 1743   | Layout 1             | `539a6d90b677`  |
| 1737   | Layout 1             | `539a6d90b677`  |
| 1731   | Layout 1             | `539a6d90b677`  |
| 1725   | Layout 1             | `539a6d90b677`  |
| 1717   | Layout 1             | `539a6d90b677`  |
| 1710   | Layout 1             | `539a6d90b677`  |
| 1704   | Layout 1             | `539a6d90b677`  |
| 1698   | Layout 1             | `539a6d90b677`  |
| 1690   | Layout 1             | `539a6d90b677`  |
| 1685   | Layout 1             | `539a6d90b677`  |
| 1680   | Layout 1             | `539a6d90b677`  |
| 1674   | Layout 1             | `539a6d90b677`  |
| 1668   | Layout 1             | `539a6d90b677`  |
| 1659   | Layout 1             | `539a6d90b677`  |
| 1649   | Layout 1             | `539a6d90b677`  |
| 1642   | Layout 1             | `539a6d90b677`  |
| 1636   | Layout 1             | `539a6d90b677`  |
| 1628   | Layout 1             | `539a6d90b677`  |
| 1622   | Layout 1             | `539a6d90b677`  |
| 1614   | Layout 1             | `539a6d90b677`  |
| 1608   | Layout 1             | `539a6d90b677`  |
| 1602   | Layout 1             | `539a6d90b677`  |
| 1598   | Layout 1             | `539a6d90b677`  |
| 1594   | Layout 1             | `539a6d90b677`  |
| 1590   | Layout 1             | `539a6d90b677`  |
| 1587   | Layout 1             | `539a6d90b677`  |
| 1584   | Layout 1             | `539a6d90b677`  |
| 1579   | Layout 1             | `539a6d90b677`  |
| 1572   | Layout 1             | `539a6d90b677`  |
| 1565   | Layout 1             | `539a6d90b677`  |
| 1559   | Layout 1             | `539a6d90b677`  |
| 1554   | Layout 1             | `539a6d90b677`  |
| 1547   | Layout 1             | `539a6d90b677`  |
| 1537   | Layout 1             | `539a6d90b677`  |
| 1529   | Layout 1             | `539a6d90b677`  |
| 1524   | Layout 1             | `539a6d90b677`  |
| 1519   | Layout 1             | `539a6d90b677`  |
| 1509   | Layout 1             | `539a6d90b677`  |
| 1506   | Layout 1             | `539a6d90b677`  |
| 1504   | Layout 1             | `539a6d90b677`  |
| 1500   | Layout 1             | `539a6d90b677`  |
| 1493   | Layout 1             | `539a6d90b677`  |
| 1489   | Layout 1             | `539a6d90b677`  |
| 1485   | Layout 1             | `539a6d90b677`  |
| 1481   | Layout 1             | `539a6d90b677`  |
| 1474   | Layout 1             | `539a6d90b677`  |
| 1466   | Layout 1             | `539a6d90b677`  |
| 1462   | Layout 1             | `539a6d90b677`  |
| 1459   | Layout 1             | `539a6d90b677`  |
| 1453   | Layout 1             | `539a6d90b677`  |
| 1450   | Layout 1             | `539a6d90b677`  |
| 1445   | Layout 1             | `539a6d90b677`  |
| 1439   | Layout 1             | `539a6d90b677`  |
| 1433   | Layout 1             | `539a6d90b677`  |
| 1430   | Layout 1             | `539a6d90b677`  |
| 1426   | Layout 1             | `539a6d90b677`  |
| 1421   | Layout 1             | `539a6d90b677`  |
| 1417   | Layout 1             | `539a6d90b677`  |
| 1416   | Layout 1             | `539a6d90b677`  |
| 1409   | Layout 1             | `539a6d90b677`  |
| 1405   | Layout 1             | `539a6d90b677`  |
| 1401   | Layout 1             | `539a6d90b677`  |
| 1396   | Layout 1             | `539a6d90b677`  |
| 1391   | Layout 1             | `539a6d90b677`  |
| 1390   | Layout 1             | `539a6d90b677`  |
| 1386   | Layout 1             | `539a6d90b677`  |
| 1381   | Layout 1             | `539a6d90b677`  |
| 1379   | Layout 1             | `539a6d90b677`  |
| 1372   | Layout 1             | `539a6d90b677`  |
| 1366   | Layout 1             | `539a6d90b677`  |
| 1364   | Layout 1             | `539a6d90b677`  |
| 1363   | Layout 1             | `539a6d90b677`  |
| 1360   | Layout 1             | `539a6d90b677`  |
| 1358   | Layout 1             | `539a6d90b677`  |
| 1355   | Layout 1             | `539a6d90b677`  |
| 1351   | Layout 1             | `539a6d90b677`  |
| 1348   | Layout 1             | `539a6d90b677`  |
| 1346   | Layout 1             | `539a6d90b677`  |
| 1341   | No documented layout | `539a6d90b677`  |
| 1340   | No documented layout | `539a6d90b677`  |
| 1338   | No documented layout | `539a6d90b677`  |
| 1335   | No documented layout | `539a6d90b677`  |
| 1333   | No documented layout | `539a6d90b677`  |
| 1329   | No documented layout | `539a6d90b677`  |
| 1327   | No documented layout | `539a6d90b677`  |
| 1324   | No documented layout | `539a6d90b677`  |
| 1321   | No documented layout | `539a6d90b677`  |
| 1319   | No documented layout | `539a6d90b677`  |
| 1318   | No documented layout | `539a6d90b677`  |
| 1316   | No documented layout | `539a6d90b677`  |
| 1313   | No documented layout | `539a6d90b677`  |
| 1311   | No documented layout | `539a6d90b677`  |
| 1309   | No documented layout | `539a6d90b677`  |
| 1304   | No documented layout | `539a6d90b677`  |
| 1292   | No documented layout | `539a6d90b677`  |
| 1286   | No documented layout | `539a6d90b677`  |
| 1280   | No file              | `539a6d90b677`  |
| 1276   | No file              | `539a6d90b677`  |
| 1267   | No documented layout | `539a6d90b677`  |
| 1261   | No documented layout | `539a6d90b677`  |
| 1256   | No file              | `539a6d90b677`  |
| 1250   | No file              | `539a6d90b677`  |
| 1246   | No file              | `539a6d90b677`  |
| 1239   | No file              | `539a6d90b677`  |
| 1230   | No file              | `539a6d90b677`  |
| 1226   | No file              | `539a6d90b677`  |
| 1220   | No file              | `539a6d90b677`  |
| 1217   | No file              | `539a6d90b677`  |
| 1211   | No file              | `539a6d90b677`  |
| 1210   | No file              | `539a6d90b677`  |
| 1208   | No file              | `539a6d90b677`  |
| 1203   | No file              | `539a6d90b677`  |
| 1197   | No file              | `539a6d90b677`  |
| 1194   | No file              | `539a6d90b677`  |
| 1192   | No file              | `539a6d90b677`  |
| 1187   | No file              | `539a6d90b677`  |
| 1183   | No file              | `539a6d90b677`  |
| 1177   | No file              | `539a6d90b677`  |
| 1173   | No file              | `539a6d90b677`  |
| 1167   | No file              | `539a6d90b677`  |
| 1164   | No file              | `539a6d90b677`  |
| 1156   | No file              | `539a6d90b677`  |
| 1149   | No file              | `539a6d90b677`  |
| 1144   | No file              | `539a6d90b677`  |
| 1137   | No file              | `539a6d90b677`  |
| 1132   | No file              | `539a6d90b677`  |
| 1127   | No file              | `539a6d90b677`  |
| 1122   | No file              | `539a6d90b677`  |
| 1118   | No file              | `539a6d90b677`  |
| 1114   | No file              | `539a6d90b677`  |
| 1109   | No file              | `539a6d90b677`  |
| 1102   | No file              | `539a6d90b677`  |
| 1096   | No file              | `539a6d90b677`  |
| 1088   | No file              | `539a6d90b677`  |
| 1081   | No file              | `539a6d90b677`  |
| 1076   | No file              | `539a6d90b677`  |
| 1069   | No file              | `539a6d90b677`  |
| 1064   | No file              | `539a6d90b677`  |
| 1058   | No file              | `539a6d90b677`  |
| 1051   | No file              | `539a6d90b677`  |
| 1044   | No file              | `539a6d90b677`  |
| 1036   | No file              | `539a6d90b677`  |
| 1026   | No file              | `539a6d90b677`  |
| 1016   | No file              | `539a6d90b677`  |
| 1009   | No file              | `539a6d90b677`  |
| 1005   | No file              | `539a6d90b677`  |
| 1000   | No file              | `539a6d90b677`  |
| 998    | No file              | `539a6d90b677`  |
| 990    | No file              | `539a6d90b677`  |
| 979    | No file              | `539a6d90b677`  |
| 972    | No file              | `539a6d90b677`  |
| 963    | No file              | `539a6d90b677`  |
| 955    | No file              | `539a6d90b677`  |
| 946    | No file              | `539a6d90b677`  |
| 938    | No file              | `539a6d90b677`  |
| 927    | No file              | `539a6d90b677`  |
| 911    | No file              | `539a6d90b677`  |
| 904    | No file              | `539a6d90b677`  |
| 899    | No file              | `539a6d90b677`  |
| 894    | No file              | `539a6d90b677`  |
| 885    | No file              | `539a6d90b677`  |
| 879    | No file              | `539a6d90b677`  |
| 872    | No file              | `539a6d90b677`  |
| 864    | No file              | `539a6d90b677`  |
| 855    | No file              | `539a6d90b677`  |
| 853    | No file              | `539a6d90b677`  |
| 845    | No file              | `539a6d90b677`  |
| 837    | No file              | `539a6d90b677`  |
| 829    | No file              | `539a6d90b677`  |
| 822    | No file              | `539a6d90b677`  |
| 814    | No file              | `539a6d90b677`  |
| 805    | No file              | `539a6d90b677`  |
| 794    | No file              | `539a6d90b677`  |
| 787    | No file              | `539a6d90b677`  |
| 780    | No file              | `539a6d90b677`  |
| 771    | No file              | `539a6d90b677`  |
| 760    | No file              | `539a6d90b677`  |
| 748    | No file              | `539a6d90b677`  |
| 741    | No file              | `539a6d90b677`  |
| 736    | No file              | `539a6d90b677`  |
| 731    | No file              | `539a6d90b677`  |
| 723    | No file              | `539a6d90b677`  |
| 711    | No file              | `539a6d90b677`  |
| 707    | No file              | `539a6d90b677`  |
| 697    | No file              | `539a6d90b677`  |
| 689    | No file              | `539a6d90b677`  |
| 683    | No file              | `539a6d90b677`  |
| 678    | No file              | `539a6d90b677`  |
| 670    | No file              | `539a6d90b677`  |
| 661    | No file              | `539a6d90b677`  |
| 656    | No file              | `539a6d90b677`  |
| 652    | No file              | `539a6d90b677`  |
| 643    | No file              | `539a6d90b677`  |
| 637    | No file              | `539a6d90b677`  |
| 630    | No file              | `539a6d90b677`  |
| 627    | No file              | `539a6d90b677`  |
| 621    | No file              | `539a6d90b677`  |
| 617    | No file              | `539a6d90b677`  |
| 615    | No file              | `539a6d90b677`  |
| 606    | No file              | `539a6d90b677`  |
| 599    | No file              | `539a6d90b677`  |
| 592    | No file              | `539a6d90b677`  |
| 586    | No file              | `539a6d90b677`  |
| 577    | No file              | `539a6d90b677`  |
| 569    | No file              | `539a6d90b677`  |
| 561    | No file              | `539a6d90b677`  |
| 554    | No file              | `539a6d90b677`  |
| 542    | No file              | `539a6d90b677`  |
| 532    | No file              | `539a6d90b677`  |
| 531    | No file              | `539a6d90b677`  |
| 526    | No file              | `539a6d90b677`  |
| 521    | No file              | `539a6d90b677`  |
| 517    | No file              | `539a6d90b677`  |
| 510    | No file              | `539a6d90b677`  |
| 508    | No file              | `539a6d90b677`  |
| 504    | No file              | `539a6d90b677`  |
| 497    | No file              | `539a6d90b677`  |
| 491    | No file              | `539a6d90b677`  |
| 485    | No file              | `539a6d90b677`  |
| 478    | No file              | `539a6d90b677`  |
| 472    | No file              | `539a6d90b677`  |
| 466    | No file              | `539a6d90b677`  |
| 457    | No file              | `539a6d90b677`  |
| 452    | No file              | `539a6d90b677`  |
| 449    | No file              | `539a6d90b677`  |
| 435    | No file              | `539a6d90b677`  |

<!-- versions:end -->

## Companion Files

| File                 | Required | Role                                                     |
| -------------------- | -------- | -------------------------------------------------------- |
| `petexpoffset.dbss`  | Required | `exp_table_id -> (data_offset, data_size)` lookup index |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                     |
| ------- | ------------- | ------- | ----------------------------------------- |
| `+0x00` | u32           | count   | Number of EXP table records (observed: 9) |
| `+0x04` | Record[count] | records | See Record                                |

Records begin immediately after the u32 count. The two bytes at `+0x04` are
the first record's key prefix (`first_record_key` in earlier versions of this
doc), not header payload.

### Record (408 bytes)

Each record is stored as `[u16 key_prefix][data_bytes]`. The companion offset points to `data_bytes`, so `record_start = data_offset - 2`.

| Offset  | Type         | Field      | Notes                                               |
| ------- | ------------ | ---------- | --------------------------------------------------- |
| `+0x00` | u16          | key_prefix | Equals `exp_table_id` in the following data payload |
| `+0x02` | Data Payload | data_bytes | 406-byte payload; see Data Payload                  |

### Data Payload (406 bytes)

Offsets are relative to `data_offset` from `petexpoffset.dbss`.

| Offset  | Type    | Field        | Notes                                                                                  |
| ------- | ------- | ------------ | -------------------------------------------------------------------------------------- |
| `+0x00` | u16     | exp_table_id | Matches the 2-byte key prefix and the companion offset key                              |
| `+0x02` | u32     | max_level    | Number of valid EXP thresholds in `level_exp` (observed: 10, 20, 30, 50)               |
| `+0x06` | u64[50] | level_exp    | Fixed-capacity threshold array; only first `max_level` values are populated            |

Unused `level_exp` slots after `max_level` are zero-filled. Data size is always 406 bytes (`2 + 4 + 50 * 8`) even when `max_level` is less than 50.

### `petexpoffset.dbss`

Provides keyed lookup into `petexp.dbss`.

| Offset  | Type              | Field | Notes                          |
| ------- | ----------------- | ----- | ------------------------------ |
| `+0x00` | u32               | count | Must equal `petexp.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                 |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                                               |
| ------- | ---- | ------------ | ----------------------------------------------------------------------------------- |
| `+0x00` | u16  | exp_table_id | Matches `key_prefix` and data payload `exp_table_id`                                |
| `+0x02` | u32  | data_offset  | Absolute byte offset in `petexp.dbss` to the data payload, after the 2-byte prefix  |
| `+0x06` | u32  | data_size    | Size of data payload in bytes (observed: 406 for every record)                      |

Offset records are ordered by descending key: 9, 8, 7, 6, 5, 4, 3, 2, 1.

The rows are the same `[u16 id][u32 offset][u32 size]` rows as a PABR offset table, but the file has no `PABR` magic and no 12-byte trailer (94 bytes = 4 + 9 x 10). The parser reads it with `parse_bare_offset_rows` from `_common/pabr_offset.py`.

## Layout 1

On client 1784 `level_exp` holds 40 slots, so every payload is 326 bytes
(`2 + 4 + 40 * 8`) and `data_size` is 326. The Record and Data Payload
differ from Layout 2.

### Record (328 bytes)

| Offset  | Type         | Field      | Notes                                               |
| ------- | ------------ | ---------- | --------------------------------------------------- |
| `+0x00` | u16          | key_prefix | Equals `exp_table_id` in the following data payload |
| `+0x02` | Data Payload | data_bytes | 326-byte payload; see Data Payload                  |

### Data Payload (326 bytes)

| Offset  | Type    | Field        | Notes                                                    |
| ------- | ------- | ------------ | -------------------------------------------------------- |
| `+0x00` | u16     | exp_table_id | Matches the 2-byte key prefix and the companion offset key |
| `+0x02` | u32     | max_level    | 10 to 40 on client 1784                                  |
| `+0x06` | u64[40] | level_exp    | Only the first `max_level` values are populated          |

## Observed Records

| EXP Table ID | Max Level | First EXP Values                       | Last Populated EXP Values |
| ------------ | --------- | -------------------------------------- | ------------------------- |
| 9            | 50        | 2055, 2260, 2599, 2989, 3437          | 13588, 13724, 13861       |
| 8            | 30        | 1746, 1921, 2209, 2541, 2922          | 9105, 9196, 9288          |
| 7            | 20        | 2055, 2260, 2599, 2989, 3437          | 9328, 9794, 10284         |
| 6            | 10        | 2055, 2260, 2599, 2989, 3437          | 5228, 6012, 6914          |
| 5            | 10        | 100, 300, 500, 700, 900               | 1500, 1700, 1900          |
| 4            | 10        | 300, 450, 660, 860, 860               | 1760, 2020, 3020          |
| 3            | 10        | 216, 324, 468, 612, 756               | 1260, 1440, 2160          |
| 2            | 10        | 144, 216, 312, 408, 504               | 840, 960, 1440            |
| 1            | 10        | 120, 180, 260, 340, 420               | 700, 800, 1200            |

Together the nine tables hold 160 level thresholds. Both files are byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.

## Notes

- `pet.dbss` selects the table with `exp_key` (header `+0x0F`, the `Pet_Table` sheet's `RequireEXPType`): keys 1 to 4 for pets, 6 to 9 for Laila. Its `max_level` matches the table's `max_level` on every record.
- Tables 6 to 9 are the fairy curves: 6 Faint, 7 Glimmering, 8 Brilliant, 9 Radiant, matching the grade level caps 10, 20, 30 and 50 in [fairyskillchange.dbss](fairyskillchange_dbss.md). The Ornette's Dark Honey Wine tooltip confirms the split: its `13,300` EXP from [fairyfeedingitem.dbss](fairyfeedingitem_dbss.md) lands on Lv. 5 98.84% on tables 6, 7 and 9 (the tooltip's Faint, Glimmering and Radiant line) and on Lv. 6 58.36% on table 8 (its Brilliant line).
- Records are fixed-capacity, not variable length. `petexpoffset.dbss` still stores offsets and sizes, following the same keyed-index pattern as other DBSS companions.
- The first bytes after the main count (`09 00`) are the first record key prefix, so the apparent 6-byte header should be treated as u32 count plus record 0 prefix.
