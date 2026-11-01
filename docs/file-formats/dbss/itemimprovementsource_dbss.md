# `itemimprovementsource.dbss` Format

## Purpose

The reform stones of Gear Reform, see
[`itemimprovement.dbss`](itemimprovement_dbss.md). A record is a stone item
with a stone category and a reform group; the gear records of the same group
are what the stone reforms.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes | Records       | Row bytes |
| ------ | -------------- | ---------------------------------- | ----- | ------------- | --------- |
| 2      | 2507 and later | `itemimprovementsource.dbss`       | 4,246 | 101 Record    | 42        |
| 2      | 2507 and later | `itemimprovementsourceoffset.dbss` | 1,216 | 101 Index Row | 12        |
| 1      | 1504 to 2503   | `itemimprovementsource.dbss`       | 3,858 | 94 Record     | 41        |
| 1      | 1504 to 2503   | `itemimprovementsourceoffset.dbss` | 1,132 | 94 Index Row  | 12        |

| Layout | File                               | Known            | Unknown    |
| ------ | ---------------------------------- | ---------------- | ---------- |
| 2      | `itemimprovementsource.dbss`       | 4,246 B (100.0%) | 0 B (0.0%) |
| 2      | `itemimprovementsourceoffset.dbss` | 1,216 B (100.0%) | 0 B (0.0%) |
| 1      | `itemimprovementsource.dbss`       | 3,858 B (100.0%) | 0 B (0.0%) |
| 1      | `itemimprovementsourceoffset.dbss` | 1,132 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `d222603f1d62`  |
| 3482   | Layout 2             | `d222603f1d62`  |
| 3474   | Layout 2             | `d222603f1d62`  |
| 3473   | Layout 2             | `d222603f1d62`  |
| 3464   | Layout 2             | `d222603f1d62`  |
| 3458   | Layout 2             | `d222603f1d62`  |
| 3454   | Layout 2             | `d222603f1d62`  |
| 3444   | Layout 2             | `d222603f1d62`  |
| 3435   | Layout 2             | `d222603f1d62`  |
| 3426   | Layout 2             | `d222603f1d62`  |
| 3418   | Layout 2             | `d222603f1d62`  |
| 3412   | Layout 2             | `d222603f1d62`  |
| 3402   | Layout 2             | `d222603f1d62`  |
| 3396   | Layout 2             | `d222603f1d62`  |
| 3387   | Layout 2             | `d222603f1d62`  |
| 3381   | Layout 2             | `d222603f1d62`  |
| 3373   | Layout 2             | `d222603f1d62`  |
| 3364   | Layout 2             | `d222603f1d62`  |
| 3356   | Layout 2             | `d222603f1d62`  |
| 3349   | Layout 2             | `d222603f1d62`  |
| 3342   | Layout 2             | `d222603f1d62`  |
| 3335   | Layout 2             | `d222603f1d62`  |
| 3326   | Layout 2             | `d222603f1d62`  |
| 3321   | Layout 2             | `d222603f1d62`  |
| 3314   | Layout 2             | `d222603f1d62`  |
| 3303   | Layout 2             | `d222603f1d62`  |
| 3302   | Layout 2             | `d222603f1d62`  |
| 3293   | Layout 2             | `d222603f1d62`  |
| 3283   | Layout 2             | `d222603f1d62`  |
| 3275   | Layout 2             | `d222603f1d62`  |
| 3267   | Layout 2             | `d222603f1d62`  |
| 3258   | Layout 2             | `d222603f1d62`  |
| 3251   | Layout 2             | `d222603f1d62`  |
| 3242   | Layout 2             | `d222603f1d62`  |
| 3235   | Layout 2             | `d222603f1d62`  |
| 3229   | Layout 2             | `d222603f1d62`  |
| 3212   | Layout 2             | `d222603f1d62`  |
| 3203   | Layout 2             | `d222603f1d62`  |
| 3193   | Layout 2             | `d222603f1d62`  |
| 3186   | Layout 2             | `d222603f1d62`  |
| 3177   | Layout 2             | `d222603f1d62`  |
| 3169   | Layout 2             | `d222603f1d62`  |
| 3158   | Layout 2             | `d222603f1d62`  |
| 3151   | Layout 2             | `d222603f1d62`  |
| 3144   | Layout 2             | `d222603f1d62`  |
| 3133   | Layout 2             | `d222603f1d62`  |
| 3125   | Layout 2             | `d222603f1d62`  |
| 3118   | Layout 2             | `d222603f1d62`  |
| 3111   | Layout 2             | `d222603f1d62`  |
| 3103   | Layout 2             | `d222603f1d62`  |
| 3095   | Layout 2             | `d222603f1d62`  |
| 3086   | Layout 2             | `d222603f1d62`  |
| 3072   | Layout 2             | `d222603f1d62`  |
| 3062   | Layout 2             | `d222603f1d62`  |
| 3052   | Layout 2             | `d222603f1d62`  |
| 3045   | Layout 2             | `d222603f1d62`  |
| 3037   | Layout 2             | `d222603f1d62`  |
| 3030   | Layout 2             | `d222603f1d62`  |
| 3021   | Layout 2             | `d222603f1d62`  |
| 3012   | Layout 2             | `d222603f1d62`  |
| 3002   | Layout 2             | `d222603f1d62`  |
| 2995   | Layout 2             | `d222603f1d62`  |
| 2987   | Layout 2             | `d222603f1d62`  |
| 2978   | Layout 2             | `d222603f1d62`  |
| 2970   | Layout 2             | `d222603f1d62`  |
| 2959   | Layout 2             | `d222603f1d62`  |
| 2951   | Layout 2             | `d222603f1d62`  |
| 2942   | Layout 2             | `d222603f1d62`  |
| 2935   | Layout 2             | `d222603f1d62`  |
| 2932   | Layout 2             | `d222603f1d62`  |
| 2923   | Layout 2             | `d222603f1d62`  |
| 2919   | Layout 2             | `d222603f1d62`  |
| 2907   | Layout 2             | `d222603f1d62`  |
| 2900   | Layout 2             | `d222603f1d62`  |
| 2891   | Layout 2             | `d222603f1d62`  |
| 2882   | Layout 2             | `d222603f1d62`  |
| 2872   | Layout 2             | `d222603f1d62`  |
| 2863   | Layout 2             | `d222603f1d62`  |
| 2855   | Layout 2             | `d222603f1d62`  |
| 2849   | Layout 2             | `d222603f1d62`  |
| 2844   | Layout 2             | `d222603f1d62`  |
| 2834   | Layout 2             | `d222603f1d62`  |
| 2825   | Layout 2             | `d222603f1d62`  |
| 2819   | Layout 2             | `d222603f1d62`  |
| 2811   | Layout 2             | `d222603f1d62`  |
| 2803   | Layout 2             | `d222603f1d62`  |
| 2794   | Layout 2             | `d222603f1d62`  |
| 2783   | Layout 2             | `d222603f1d62`  |
| 2774   | Layout 2             | `d222603f1d62`  |
| 2765   | Layout 2             | `d222603f1d62`  |
| 2756   | Layout 2             | `d222603f1d62`  |
| 2750   | Layout 2             | `d222603f1d62`  |
| 2743   | Layout 2             | `d222603f1d62`  |
| 2736   | Layout 2             | `d222603f1d62`  |
| 2726   | Layout 2             | `d222603f1d62`  |
| 2717   | Layout 2             | `d222603f1d62`  |
| 2709   | Layout 2             | `d222603f1d62`  |
| 2703   | Layout 2             | `d222603f1d62`  |
| 2695   | Layout 2             | `d222603f1d62`  |
| 2684   | Layout 2             | `d222603f1d62`  |
| 2672   | Layout 2             | `d222603f1d62`  |
| 2665   | Layout 2             | `d222603f1d62`  |
| 2657   | Layout 2             | `d222603f1d62`  |
| 2649   | Layout 2             | `d222603f1d62`  |
| 2644   | Layout 2             | `d222603f1d62`  |
| 2637   | Layout 2             | `d222603f1d62`  |
| 2629   | Layout 2             | `d222603f1d62`  |
| 2619   | Layout 2             | `d222603f1d62`  |
| 2612   | Layout 2             | `d222603f1d62`  |
| 2606   | Layout 2             | `d222603f1d62`  |
| 2602   | Layout 2             | `d222603f1d62`  |
| 2601   | Layout 2             | `d222603f1d62`  |
| 2592   | Layout 2             | `d222603f1d62`  |
| 2583   | Layout 2             | `d222603f1d62`  |
| 2575   | Layout 2             | `d222603f1d62`  |
| 2567   | Layout 2             | `d222603f1d62`  |
| 2560   | Layout 2             | `d222603f1d62`  |
| 2553   | Layout 2             | `d222603f1d62`  |
| 2545   | Layout 2             | `d222603f1d62`  |
| 2538   | Layout 2             | `d222603f1d62`  |
| 2529   | Layout 2             | `d222603f1d62`  |
| 2519   | Layout 2             | `d222603f1d62`  |
| 2513   | Layout 2             | `d222603f1d62`  |
| 2510   | Layout 2             | `d222603f1d62`  |
| 2507   | Layout 2             | `d222603f1d62`  |
| 2503   | Layout 1             | `d222603f1d62`  |
| 2498   | Layout 1             | `d222603f1d62`  |
| 2492   | Layout 1             | `d222603f1d62`  |
| 2487   | Layout 1             | `d222603f1d62`  |
| 2480   | Layout 1             | `d222603f1d62`  |
| 2474   | Layout 1             | `d222603f1d62`  |
| 2468   | Layout 1             | `d222603f1d62`  |
| 2460   | Layout 1             | `d222603f1d62`  |
| 2453   | Layout 1             | `d222603f1d62`  |
| 2444   | Layout 1             | `d222603f1d62`  |
| 2438   | Layout 1             | `d222603f1d62`  |
| 2434   | Layout 1             | `d222603f1d62`  |
| 2429   | Layout 1             | `d222603f1d62`  |
| 2421   | Layout 1             | `d222603f1d62`  |
| 2414   | Layout 1             | `d222603f1d62`  |
| 2407   | Layout 1             | `d222603f1d62`  |
| 2401   | Layout 1             | `d222603f1d62`  |
| 2397   | Layout 1             | `d222603f1d62`  |
| 2393   | Layout 1             | `d222603f1d62`  |
| 2384   | Layout 1             | `d222603f1d62`  |
| 2378   | Layout 1             | `d222603f1d62`  |
| 2372   | Layout 1             | `d222603f1d62`  |
| 2358   | Layout 1             | `d222603f1d62`  |
| 2352   | Layout 1             | `d222603f1d62`  |
| 2347   | Layout 1             | `d222603f1d62`  |
| 2343   | Layout 1             | `d222603f1d62`  |
| 2335   | Layout 1             | `d222603f1d62`  |
| 2327   | Layout 1             | `d222603f1d62`  |
| 2324   | Layout 1             | `d222603f1d62`  |
| 2319   | Layout 1             | `d222603f1d62`  |
| 2313   | Layout 1             | `d222603f1d62`  |
| 2308   | Layout 1             | `d222603f1d62`  |
| 2302   | Layout 1             | `d222603f1d62`  |
| 2295   | Layout 1             | `d222603f1d62`  |
| 2290   | Layout 1             | `d222603f1d62`  |
| 2284   | Layout 1             | `d222603f1d62`  |
| 2276   | Layout 1             | `d222603f1d62`  |
| 2269   | Layout 1             | `d222603f1d62`  |
| 2259   | Layout 1             | `d222603f1d62`  |
| 2250   | Layout 1             | `d222603f1d62`  |
| 2243   | Layout 1             | `d222603f1d62`  |
| 2235   | Layout 1             | `d222603f1d62`  |
| 2229   | Layout 1             | `d222603f1d62`  |
| 2224   | Layout 1             | `d222603f1d62`  |
| 2218   | Layout 1             | `d222603f1d62`  |
| 2215   | Layout 1             | `d222603f1d62`  |
| 2207   | Layout 1             | `d222603f1d62`  |
| 2203   | Layout 1             | `d222603f1d62`  |
| 2196   | Layout 1             | `d222603f1d62`  |
| 2192   | Layout 1             | `d222603f1d62`  |
| 2189   | Layout 1             | `d222603f1d62`  |
| 2183   | Layout 1             | `d222603f1d62`  |
| 2179   | Layout 1             | `d222603f1d62`  |
| 2171   | Layout 1             | `d222603f1d62`  |
| 2163   | Layout 1             | `d222603f1d62`  |
| 2156   | Layout 1             | `d222603f1d62`  |
| 2151   | Layout 1             | `d222603f1d62`  |
| 2147   | Layout 1             | `d222603f1d62`  |
| 2142   | Layout 1             | `d222603f1d62`  |
| 2138   | Layout 1             | `d222603f1d62`  |
| 2134   | Layout 1             | `d222603f1d62`  |
| 2130   | Layout 1             | `d222603f1d62`  |
| 2122   | Layout 1             | `d222603f1d62`  |
| 2107   | Layout 1             | `d222603f1d62`  |
| 2098   | Layout 1             | `d222603f1d62`  |
| 2089   | Layout 1             | `d222603f1d62`  |
| 2081   | Layout 1             | `d222603f1d62`  |
| 2073   | Layout 1             | `d222603f1d62`  |
| 2067   | Layout 1             | `d222603f1d62`  |
| 2063   | Layout 1             | `d222603f1d62`  |
| 2059   | Layout 1             | `d222603f1d62`  |
| 2052   | Layout 1             | `d222603f1d62`  |
| 2044   | Layout 1             | `d222603f1d62`  |
| 2039   | Layout 1             | `d222603f1d62`  |
| 2032   | Layout 1             | `d222603f1d62`  |
| 2025   | Layout 1             | `d222603f1d62`  |
| 2011   | Layout 1             | `d222603f1d62`  |
| 2005   | Layout 1             | `d222603f1d62`  |
| 2000   | Layout 1             | `d222603f1d62`  |
| 1996   | Layout 1             | `d222603f1d62`  |
| 1991   | Layout 1             | `d222603f1d62`  |
| 1985   | Layout 1             | `d222603f1d62`  |
| 1980   | Layout 1             | `d222603f1d62`  |
| 1969   | Layout 1             | `d222603f1d62`  |
| 1964   | Layout 1             | `d222603f1d62`  |
| 1958   | Layout 1             | `d222603f1d62`  |
| 1950   | Layout 1             | `d222603f1d62`  |
| 1945   | Layout 1             | `d222603f1d62`  |
| 1937   | Layout 1             | `d222603f1d62`  |
| 1933   | Layout 1             | `d222603f1d62`  |
| 1927   | Layout 1             | `d222603f1d62`  |
| 1921   | Layout 1             | `d222603f1d62`  |
| 1914   | Layout 1             | `d222603f1d62`  |
| 1908   | Layout 1             | `d222603f1d62`  |
| 1897   | Layout 1             | `d222603f1d62`  |
| 1892   | Layout 1             | `d222603f1d62`  |
| 1886   | Layout 1             | `d222603f1d62`  |
| 1881   | Layout 1             | `d222603f1d62`  |
| 1871   | Layout 1             | `d222603f1d62`  |
| 1866   | Layout 1             | `d222603f1d62`  |
| 1862   | Layout 1             | `d222603f1d62`  |
| 1854   | Layout 1             | `d222603f1d62`  |
| 1846   | Layout 1             | `d222603f1d62`  |
| 1838   | Layout 1             | `d222603f1d62`  |
| 1832   | Layout 1             | `d222603f1d62`  |
| 1826   | Layout 1             | `d222603f1d62`  |
| 1822   | Layout 1             | `d222603f1d62`  |
| 1818   | Layout 1             | `d222603f1d62`  |
| 1804   | Layout 1             | `d222603f1d62`  |
| 1794   | Layout 1             | `d222603f1d62`  |
| 1790   | Layout 1             | `d222603f1d62`  |
| 1784   | Layout 1             | `d222603f1d62`  |
| 1774   | Layout 1             | `d222603f1d62`  |
| 1771   | Layout 1             | `d222603f1d62`  |
| 1762   | Layout 1             | `d222603f1d62`  |
| 1759   | Layout 1             | `d222603f1d62`  |
| 1754   | Layout 1             | `d222603f1d62`  |
| 1749   | Layout 1             | `d222603f1d62`  |
| 1743   | Layout 1             | `d222603f1d62`  |
| 1737   | Layout 1             | `d222603f1d62`  |
| 1731   | Layout 1             | `d222603f1d62`  |
| 1725   | Layout 1             | `d222603f1d62`  |
| 1717   | Layout 1             | `d222603f1d62`  |
| 1710   | Layout 1             | `d222603f1d62`  |
| 1704   | Layout 1             | `d222603f1d62`  |
| 1698   | Layout 1             | `d222603f1d62`  |
| 1690   | Layout 1             | `d222603f1d62`  |
| 1685   | Layout 1             | `d222603f1d62`  |
| 1680   | Layout 1             | `d222603f1d62`  |
| 1674   | Layout 1             | `d222603f1d62`  |
| 1668   | Layout 1             | `d222603f1d62`  |
| 1659   | Layout 1             | `d222603f1d62`  |
| 1649   | Layout 1             | `d222603f1d62`  |
| 1642   | Layout 1             | `d222603f1d62`  |
| 1636   | Layout 1             | `d222603f1d62`  |
| 1628   | Layout 1             | `d222603f1d62`  |
| 1622   | Layout 1             | `d222603f1d62`  |
| 1614   | Layout 1             | `d222603f1d62`  |
| 1608   | Layout 1             | `d222603f1d62`  |
| 1602   | Layout 1             | `d222603f1d62`  |
| 1598   | Layout 1             | `d222603f1d62`  |
| 1594   | Layout 1             | `d222603f1d62`  |
| 1590   | Layout 1             | `d222603f1d62`  |
| 1587   | Layout 1             | `d222603f1d62`  |
| 1584   | Layout 1             | `d222603f1d62`  |
| 1579   | Layout 1             | `d222603f1d62`  |
| 1572   | Layout 1             | `d222603f1d62`  |
| 1565   | Layout 1             | `d222603f1d62`  |
| 1559   | Layout 1             | `d222603f1d62`  |
| 1554   | Layout 1             | `d222603f1d62`  |
| 1547   | Layout 1             | `d222603f1d62`  |
| 1537   | Layout 1             | `d222603f1d62`  |
| 1529   | Layout 1             | `d222603f1d62`  |
| 1524   | Layout 1             | `d222603f1d62`  |
| 1519   | Layout 1             | `d222603f1d62`  |
| 1509   | Layout 1             | `d222603f1d62`  |
| 1506   | Layout 1             | `d222603f1d62`  |
| 1504   | Layout 1             | `d222603f1d62`  |
| 1500   | No documented layout | `d222603f1d62`  |
| 1493   | No documented layout | `d222603f1d62`  |
| 1489   | No documented layout | `d222603f1d62`  |
| 1485   | No documented layout | `d222603f1d62`  |
| 1481   | No documented layout | `d222603f1d62`  |
| 1474   | No documented layout | `d222603f1d62`  |
| 1466   | No documented layout | `d222603f1d62`  |
| 1462   | No documented layout | `d222603f1d62`  |
| 1459   | No documented layout | `d222603f1d62`  |
| 1453   | No documented layout | `d222603f1d62`  |
| 1450   | No documented layout | `d222603f1d62`  |
| 1445   | No documented layout | `d222603f1d62`  |
| 1439   | No documented layout | `d222603f1d62`  |
| 1433   | No documented layout | `d222603f1d62`  |
| 1430   | No documented layout | `d222603f1d62`  |
| 1426   | No documented layout | `d222603f1d62`  |
| 1421   | No documented layout | `d222603f1d62`  |
| 1417   | No documented layout | `d222603f1d62`  |
| 1416   | No documented layout | `d222603f1d62`  |
| 1409   | No documented layout | `d222603f1d62`  |
| 1405   | No documented layout | `d222603f1d62`  |
| 1401   | No documented layout | `d222603f1d62`  |
| 1396   | No documented layout | `d222603f1d62`  |
| 1391   | No documented layout | `d222603f1d62`  |
| 1390   | No documented layout | `d222603f1d62`  |
| 1386   | No documented layout | `d222603f1d62`  |
| 1381   | No documented layout | `d222603f1d62`  |
| 1379   | No documented layout | `d222603f1d62`  |
| 1372   | No documented layout | `d222603f1d62`  |
| 1366   | No documented layout | `d222603f1d62`  |
| 1364   | No documented layout | `d222603f1d62`  |
| 1363   | No documented layout | `d222603f1d62`  |
| 1360   | No documented layout | `d222603f1d62`  |
| 1358   | No documented layout | `d222603f1d62`  |
| 1355   | No documented layout | `d222603f1d62`  |
| 1351   | No documented layout | `d222603f1d62`  |
| 1348   | No documented layout | `d222603f1d62`  |
| 1346   | No documented layout | `d222603f1d62`  |
| 1341   | No documented layout | `d222603f1d62`  |
| 1340   | No documented layout | `d222603f1d62`  |
| 1338   | No documented layout | `d222603f1d62`  |
| 1335   | No documented layout | `d222603f1d62`  |
| 1333   | No documented layout | `d222603f1d62`  |
| 1329   | No documented layout | `d222603f1d62`  |
| 1327   | No documented layout | `d222603f1d62`  |
| 1324   | No documented layout | `d222603f1d62`  |
| 1321   | No documented layout | `d222603f1d62`  |
| 1319   | No documented layout | `d222603f1d62`  |
| 1318   | No documented layout | `d222603f1d62`  |
| 1316   | No documented layout | `d222603f1d62`  |
| 1313   | No documented layout | `d222603f1d62`  |
| 1311   | No documented layout | `d222603f1d62`  |
| 1309   | No documented layout | `d222603f1d62`  |
| 1304   | No documented layout | `d222603f1d62`  |
| 1292   | No documented layout | `d222603f1d62`  |
| 1286   | No documented layout | `d222603f1d62`  |
| 1280   | No documented layout | `d222603f1d62`  |
| 1276   | No file              | `d222603f1d62`  |
| 1267   | No file              | `d222603f1d62`  |
| 1261   | No file              | `d222603f1d62`  |
| 1256   | No file              | `d222603f1d62`  |
| 1250   | No file              | `d222603f1d62`  |
| 1246   | No file              | `d222603f1d62`  |
| 1239   | No file              | `d222603f1d62`  |
| 1230   | No file              | `d222603f1d62`  |
| 1226   | No file              | `d222603f1d62`  |
| 1220   | No file              | `d222603f1d62`  |
| 1217   | No file              | `d222603f1d62`  |
| 1211   | No file              | `d222603f1d62`  |
| 1210   | No file              | `d222603f1d62`  |
| 1208   | No file              | `d222603f1d62`  |
| 1203   | No file              | `d222603f1d62`  |
| 1197   | No file              | `d222603f1d62`  |
| 1194   | No file              | `d222603f1d62`  |
| 1192   | No file              | `d222603f1d62`  |
| 1187   | No file              | `d222603f1d62`  |
| 1183   | No file              | `d222603f1d62`  |
| 1177   | No file              | `d222603f1d62`  |
| 1173   | No file              | `d222603f1d62`  |
| 1167   | No file              | `d222603f1d62`  |
| 1164   | No file              | `d222603f1d62`  |
| 1156   | No file              | `d222603f1d62`  |
| 1149   | No file              | `d222603f1d62`  |
| 1144   | No file              | `d222603f1d62`  |
| 1137   | No file              | `d222603f1d62`  |
| 1132   | No file              | `d222603f1d62`  |
| 1127   | No file              | `d222603f1d62`  |
| 1122   | No file              | `d222603f1d62`  |
| 1118   | No file              | `d222603f1d62`  |
| 1114   | No file              | `d222603f1d62`  |
| 1109   | No file              | `d222603f1d62`  |
| 1102   | No file              | `d222603f1d62`  |
| 1096   | No file              | `d222603f1d62`  |
| 1088   | No file              | `d222603f1d62`  |
| 1081   | No file              | `d222603f1d62`  |
| 1076   | No file              | `d222603f1d62`  |
| 1069   | No file              | `d222603f1d62`  |
| 1064   | No file              | `d222603f1d62`  |
| 1058   | No file              | `d222603f1d62`  |
| 1051   | No file              | `d222603f1d62`  |
| 1044   | No file              | `d222603f1d62`  |
| 1036   | No file              | `d222603f1d62`  |
| 1026   | No file              | `d222603f1d62`  |
| 1016   | No file              | `d222603f1d62`  |
| 1009   | No file              | `d222603f1d62`  |
| 1005   | No file              | `d222603f1d62`  |
| 1000   | No file              | `d222603f1d62`  |
| 998    | No file              | `d222603f1d62`  |
| 990    | No file              | `d222603f1d62`  |
| 979    | No file              | `d222603f1d62`  |
| 972    | No file              | `d222603f1d62`  |
| 963    | No file              | `d222603f1d62`  |
| 955    | No file              | `d222603f1d62`  |
| 946    | No file              | `d222603f1d62`  |
| 938    | No file              | `d222603f1d62`  |
| 927    | No file              | `d222603f1d62`  |
| 911    | No file              | `d222603f1d62`  |
| 904    | No file              | `d222603f1d62`  |
| 899    | No file              | `d222603f1d62`  |
| 894    | No file              | `d222603f1d62`  |
| 885    | No file              | `d222603f1d62`  |
| 879    | No file              | `d222603f1d62`  |
| 872    | No file              | `d222603f1d62`  |
| 864    | No file              | `d222603f1d62`  |
| 855    | No file              | `d222603f1d62`  |
| 853    | No file              | `d222603f1d62`  |
| 845    | No file              | `d222603f1d62`  |
| 837    | No file              | `d222603f1d62`  |
| 829    | No file              | `d222603f1d62`  |
| 822    | No file              | `d222603f1d62`  |
| 814    | No file              | `d222603f1d62`  |
| 805    | No file              | `d222603f1d62`  |
| 794    | No file              | `d222603f1d62`  |
| 787    | No file              | `d222603f1d62`  |
| 780    | No file              | `d222603f1d62`  |
| 771    | No file              | `d222603f1d62`  |
| 760    | No file              | `d222603f1d62`  |
| 748    | No file              | `d222603f1d62`  |
| 741    | No file              | `d222603f1d62`  |
| 736    | No file              | `d222603f1d62`  |
| 731    | No file              | `d222603f1d62`  |
| 723    | No file              | `d222603f1d62`  |
| 711    | No file              | `d222603f1d62`  |
| 707    | No file              | `d222603f1d62`  |
| 697    | No file              | `d222603f1d62`  |
| 689    | No file              | `d222603f1d62`  |
| 683    | No file              | `d222603f1d62`  |
| 678    | No file              | `d222603f1d62`  |
| 670    | No file              | `d222603f1d62`  |
| 661    | No file              | `d222603f1d62`  |
| 656    | No file              | `d222603f1d62`  |
| 652    | No file              | `d222603f1d62`  |
| 643    | No file              | `d222603f1d62`  |
| 637    | No file              | `d222603f1d62`  |
| 630    | No file              | `d222603f1d62`  |
| 627    | No file              | `d222603f1d62`  |
| 621    | No file              | `d222603f1d62`  |
| 617    | No file              | `d222603f1d62`  |
| 615    | No file              | `d222603f1d62`  |
| 606    | No file              | `d222603f1d62`  |
| 599    | No file              | `d222603f1d62`  |
| 592    | No file              | `d222603f1d62`  |
| 586    | No file              | `d222603f1d62`  |
| 577    | No file              | `d222603f1d62`  |
| 569    | No file              | `d222603f1d62`  |
| 561    | No file              | `d222603f1d62`  |
| 554    | No file              | `d222603f1d62`  |
| 542    | No file              | `d222603f1d62`  |
| 532    | No file              | `d222603f1d62`  |
| 531    | No file              | `d222603f1d62`  |
| 526    | No file              | `d222603f1d62`  |
| 521    | No file              | `d222603f1d62`  |
| 517    | No file              | `d222603f1d62`  |
| 510    | No file              | `d222603f1d62`  |
| 508    | No file              | `d222603f1d62`  |
| 504    | No file              | `d222603f1d62`  |
| 497    | No file              | `d222603f1d62`  |
| 491    | No file              | `d222603f1d62`  |
| 485    | No file              | `d222603f1d62`  |
| 478    | No file              | `d222603f1d62`  |
| 472    | No file              | `d222603f1d62`  |
| 466    | No file              | `d222603f1d62`  |
| 457    | No file              | `d222603f1d62`  |
| 452    | No file              | `d222603f1d62`  |
| 449    | No file              | `d222603f1d62`  |
| 435    | No file              | `d222603f1d62`  |

<!-- versions:end -->

## Companion Files

| File                             | Required | Role                                                     |
| -------------------------------- | -------- | -------------------------------------------------------- |
| `itemimprovementsourceoffset.dbss` | Optional | `item_id -> (data_offset, data_size)` index, see below; the handler walks the records without it |

Item names come from LOC type 0 and icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                                |
| ------- | ------------- | ------- | ---------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `101` on client 3464              |
| `+0x04` | Record[count] | records | Back to back to the end of the file; see Record      |

### Record (variable: 22 bytes + values)

| Offset            | Type             | Field              | Notes                                                    |
| ----------------- | ---------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`           | u32              | item_id            | The stone; the index's `data_offset` points past it      |
| `+0x04`           | u64              | value_count        | `5` in every record                                      |
| `+0x0C`           | u32[value_count] | results            | `1,000,000` in every slot of every record (client 3474); see Field Names |
| `results+0x00`    | u32              | category           | Gear the stone takes, see below                          |
| `results+0x04`    | u32              | group              | Reform group, `1` to `48`; matches `group` of the gear records |
| `results+0x08`    | u16              | is_default_display | `1` for the 24 stones of [`itemimprovementdefaultdisplaylist.bss`](../bss/itemimprovementdefaultdisplaylist_bss.md), else `0` |

Each `(category, group)` pair belongs to one stone (101 pairs, client 3464).

| category | Stones (client 3464)                                                             |
| -------- | -------------------------------------------------------------------------------- |
| `1`      | Weapon stones: Heart of Kutum, Resplendent Boss Weapon Reform Stone I to V, `[Season] Tuvala Main Weapon Conversion Stone` |
| `2`      | Armor stones: Resplendent Boss Armor Reform Stone I to V, `Combatant's Stone (Armor)`, `[Season] Tuvala Helmet Conversion Stone` |
| `3`      | Accessory stones: Cup of Destined Dawn and the other Cups, `[Season] Tuvala Necklace Conversion Stone` |
| `4`      | Blessed Soul Fragment, Exalted Soul Fragment, Crimson Behelit Alchemy Stone Appearance |
| `5`      | Flawless Herald's Crystal                                                        |

### `itemimprovementsourceoffset.dbss`

| Offset  | Type             | Field | Notes                                            |
| ------- | ---------------- | ----- | ------------------------------------------------ |
| `+0x00` | u32              | count | Equals the `itemimprovementsource.dbss` count    |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row              |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | item_id     | Record key                              |
| `+0x04` | u32  | data_offset | Record start + 4, past `item_id`        |
| `+0x08` | u32  | data_size   | Record size - 4: `38`                   |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`; on client
3464 every row matches the record walked from the start of the file.

## Layout 1

Client 1784 stores `is_default_display` as a u8, so each record is one
byte shorter. Only the Record differs from Layout 2.

### Record (variable: 21 bytes + values)

| Offset            | Type             | Field              | Notes                                       |
| ----------------- | ---------------- | ------------------ | ------------------------------------------- |
| `+0x00`           | u32              | item_id            |                                             |
| `+0x04`           | u64              | value_count        |                                             |
| `+0x0C`           | u32[value_count] | results            |                                             |
| `results+0x00`    | u32              | category           | `1` to `3` on client 1784                   |
| `results+0x04`    | u32              | group              |                                             |
| `results+0x08`    | u8               | is_default_display | `1` on 19 of the 95 records (client 1784)   |

## Field Names

The record is the `Item_ImprovementSource_Table` sheet of a private server
on client 1784. That server's dump (`Instance_dumpFull.exe`) reads the
client file with the row reader at VA `0x140b365e0`: a u64 count and that
many u32 values into a list, then `category`, `group` and
`is_default_display`. Its sheet loader fills the same members:

| Field                | Sheet column                    |
| -------------------- | ------------------------------- |
| `item_id`            | `SourceItemKey`                 |
| `results`            | `result0` to `result4`          |
| `category`           | `equipType`                     |
| `group`              | `Grade`                         |
| `is_default_display` | `SourceItemDisplay`             |

The loader formats the column name `result%d` for `0` to `4` (VA
`0x1408c02f3`), reads each as a u32, skips a value above 1,000,000 (VA
`0x1408c034d`) and appends the rest, so `value_count` is the number of
`result` columns at or under 1,000,000. It accepts `equipType` `1` to `3`
only and a `Grade` above 0.

The private server's own file holds 95 of the sheet's 98 stones; on all 95
the five `results`, `category`, `group` and `is_default_display` equal the
sheet. On that build six stones (`4906` to `4911`) have a `result0` of
10,000, 20,000 or 50,000; client 3474 has `1,000,000` in all 505 slots.

## Notes

- `category` follows from the stone names; the gear side of the match is an
  open question in [`itemimprovement.dbss`](itemimprovement_dbss.md#which-stone-a-record-takes).
- 28 groups (`17` to `32`, `36`, `38` to `48`) have stones but no gear record
  on client 3464.
- `is_default_display` and the default display list hold the same 24 stones;
  the Reform window loads the list through
  `ToClient_GetImprovementSourceItemCount()` and
  `ToClient_GetDefaultDisplayImprovementSourceItemByIndex(index)`
  (`panel_improvement_all_1`).

## Open Questions

### What the Five `results` Do

The server caps each value at 1,000,000, the scale of rates elsewhere
(`buff.dbss` `apply_rate`), and the window text says a higher-grade stone
gives a higher chance of higher-grade gear, but no code in the client 1784
server dump reads the list after loading it. Whether slot `i` pairs with
the `i`-th result item of [`itemimprovement.dbss`](itemimprovement_dbss.md)
is open.
