# `characteraudioradius.dbss` Format

## Purpose

The sound radius of a few characters whose sounds carry further than usual: world bosses (Khan, Vell, Erebjork, Moghulis, Org, the Wilderness Golem), weather actors (Sandstorm, Snowstorm), Lekrashan and a tutorial character. Each row is a character key and its radius. `characteraudioradiusoffset.dbss` indexes the rows by character key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                              | Bytes | Records      | Row bytes |
| ------ | -------------- | --------------------------------- | ----- | ------------ | --------- |
| 1      | 1416 and later | `characteraudioradius.dbss`       | 166   | 27 Row       | 6         |
| 1      | 1416 and later | `characteraudioradiusoffset.dbss` | 290   | 27 Index Row | 10        |

| Layout | File                              | Known          | Unknown    |
| ------ | --------------------------------- | -------------- | ---------- |
| 1      | `characteraudioradius.dbss`       | 166 B (100.0%) | 0 B (0.0%) |
| 1      | `characteraudioradiusoffset.dbss` | 290 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `8e6ff0d29100`  |
| 3482   | Layout 1 | `8e6ff0d29100`  |
| 3474   | Layout 1 | `8e6ff0d29100`  |
| 3473   | Layout 1 | `8e6ff0d29100`  |
| 3464   | Layout 1 | `8e6ff0d29100`  |
| 3458   | Layout 1 | `8e6ff0d29100`  |
| 3454   | Layout 1 | `8e6ff0d29100`  |
| 3444   | Layout 1 | `8e6ff0d29100`  |
| 3435   | Layout 1 | `8e6ff0d29100`  |
| 3426   | Layout 1 | `8e6ff0d29100`  |
| 3418   | Layout 1 | `8e6ff0d29100`  |
| 3412   | Layout 1 | `8e6ff0d29100`  |
| 3402   | Layout 1 | `8e6ff0d29100`  |
| 3396   | Layout 1 | `8e6ff0d29100`  |
| 3387   | Layout 1 | `8e6ff0d29100`  |
| 3381   | Layout 1 | `8e6ff0d29100`  |
| 3373   | Layout 1 | `8e6ff0d29100`  |
| 3364   | Layout 1 | `8e6ff0d29100`  |
| 3356   | Layout 1 | `8e6ff0d29100`  |
| 3349   | Layout 1 | `8e6ff0d29100`  |
| 3342   | Layout 1 | `8e6ff0d29100`  |
| 3335   | Layout 1 | `8e6ff0d29100`  |
| 3326   | Layout 1 | `8e6ff0d29100`  |
| 3321   | Layout 1 | `8e6ff0d29100`  |
| 3314   | Layout 1 | `8e6ff0d29100`  |
| 3303   | Layout 1 | `8e6ff0d29100`  |
| 3302   | Layout 1 | `8e6ff0d29100`  |
| 3293   | Layout 1 | `8e6ff0d29100`  |
| 3283   | Layout 1 | `8e6ff0d29100`  |
| 3275   | Layout 1 | `8e6ff0d29100`  |
| 3267   | Layout 1 | `8e6ff0d29100`  |
| 3258   | Layout 1 | `8e6ff0d29100`  |
| 3251   | Layout 1 | `8e6ff0d29100`  |
| 3242   | Layout 1 | `8e6ff0d29100`  |
| 3235   | Layout 1 | `8e6ff0d29100`  |
| 3229   | Layout 1 | `8e6ff0d29100`  |
| 3212   | Layout 1 | `8e6ff0d29100`  |
| 3203   | Layout 1 | `8e6ff0d29100`  |
| 3193   | Layout 1 | `8e6ff0d29100`  |
| 3186   | Layout 1 | `8e6ff0d29100`  |
| 3177   | Layout 1 | `8e6ff0d29100`  |
| 3169   | Layout 1 | `8e6ff0d29100`  |
| 3158   | Layout 1 | `8e6ff0d29100`  |
| 3151   | Layout 1 | `8e6ff0d29100`  |
| 3144   | Layout 1 | `8e6ff0d29100`  |
| 3133   | Layout 1 | `8e6ff0d29100`  |
| 3125   | Layout 1 | `8e6ff0d29100`  |
| 3118   | Layout 1 | `8e6ff0d29100`  |
| 3111   | Layout 1 | `8e6ff0d29100`  |
| 3103   | Layout 1 | `8e6ff0d29100`  |
| 3095   | Layout 1 | `8e6ff0d29100`  |
| 3086   | Layout 1 | `8e6ff0d29100`  |
| 3072   | Layout 1 | `8e6ff0d29100`  |
| 3062   | Layout 1 | `8e6ff0d29100`  |
| 3052   | Layout 1 | `8e6ff0d29100`  |
| 3045   | Layout 1 | `8e6ff0d29100`  |
| 3037   | Layout 1 | `8e6ff0d29100`  |
| 3030   | Layout 1 | `8e6ff0d29100`  |
| 3021   | Layout 1 | `8e6ff0d29100`  |
| 3012   | Layout 1 | `8e6ff0d29100`  |
| 3002   | Layout 1 | `8e6ff0d29100`  |
| 2995   | Layout 1 | `8e6ff0d29100`  |
| 2987   | Layout 1 | `8e6ff0d29100`  |
| 2978   | Layout 1 | `8e6ff0d29100`  |
| 2970   | Layout 1 | `8e6ff0d29100`  |
| 2959   | Layout 1 | `8e6ff0d29100`  |
| 2951   | Layout 1 | `8e6ff0d29100`  |
| 2942   | Layout 1 | `8e6ff0d29100`  |
| 2935   | Layout 1 | `8e6ff0d29100`  |
| 2932   | Layout 1 | `8e6ff0d29100`  |
| 2923   | Layout 1 | `8e6ff0d29100`  |
| 2919   | Layout 1 | `8e6ff0d29100`  |
| 2907   | Layout 1 | `8e6ff0d29100`  |
| 2900   | Layout 1 | `8e6ff0d29100`  |
| 2891   | Layout 1 | `8e6ff0d29100`  |
| 2882   | Layout 1 | `8e6ff0d29100`  |
| 2872   | Layout 1 | `8e6ff0d29100`  |
| 2863   | Layout 1 | `8e6ff0d29100`  |
| 2855   | Layout 1 | `8e6ff0d29100`  |
| 2849   | Layout 1 | `8e6ff0d29100`  |
| 2844   | Layout 1 | `8e6ff0d29100`  |
| 2834   | Layout 1 | `8e6ff0d29100`  |
| 2825   | Layout 1 | `8e6ff0d29100`  |
| 2819   | Layout 1 | `8e6ff0d29100`  |
| 2811   | Layout 1 | `8e6ff0d29100`  |
| 2803   | Layout 1 | `8e6ff0d29100`  |
| 2794   | Layout 1 | `8e6ff0d29100`  |
| 2783   | Layout 1 | `8e6ff0d29100`  |
| 2774   | Layout 1 | `8e6ff0d29100`  |
| 2765   | Layout 1 | `8e6ff0d29100`  |
| 2756   | Layout 1 | `8e6ff0d29100`  |
| 2750   | Layout 1 | `8e6ff0d29100`  |
| 2743   | Layout 1 | `8e6ff0d29100`  |
| 2736   | Layout 1 | `8e6ff0d29100`  |
| 2726   | Layout 1 | `8e6ff0d29100`  |
| 2717   | Layout 1 | `8e6ff0d29100`  |
| 2709   | Layout 1 | `8e6ff0d29100`  |
| 2703   | Layout 1 | `8e6ff0d29100`  |
| 2695   | Layout 1 | `8e6ff0d29100`  |
| 2684   | Layout 1 | `8e6ff0d29100`  |
| 2672   | Layout 1 | `8e6ff0d29100`  |
| 2665   | Layout 1 | `8e6ff0d29100`  |
| 2657   | Layout 1 | `8e6ff0d29100`  |
| 2649   | Layout 1 | `8e6ff0d29100`  |
| 2644   | Layout 1 | `8e6ff0d29100`  |
| 2637   | Layout 1 | `8e6ff0d29100`  |
| 2629   | Layout 1 | `8e6ff0d29100`  |
| 2619   | Layout 1 | `8e6ff0d29100`  |
| 2612   | Layout 1 | `8e6ff0d29100`  |
| 2606   | Layout 1 | `8e6ff0d29100`  |
| 2602   | Layout 1 | `8e6ff0d29100`  |
| 2601   | Layout 1 | `8e6ff0d29100`  |
| 2592   | Layout 1 | `8e6ff0d29100`  |
| 2583   | Layout 1 | `8e6ff0d29100`  |
| 2575   | Layout 1 | `8e6ff0d29100`  |
| 2567   | Layout 1 | `8e6ff0d29100`  |
| 2560   | Layout 1 | `8e6ff0d29100`  |
| 2553   | Layout 1 | `8e6ff0d29100`  |
| 2545   | Layout 1 | `8e6ff0d29100`  |
| 2538   | Layout 1 | `8e6ff0d29100`  |
| 2529   | Layout 1 | `8e6ff0d29100`  |
| 2519   | Layout 1 | `8e6ff0d29100`  |
| 2513   | Layout 1 | `8e6ff0d29100`  |
| 2510   | Layout 1 | `8e6ff0d29100`  |
| 2507   | Layout 1 | `8e6ff0d29100`  |
| 2503   | Layout 1 | `8e6ff0d29100`  |
| 2498   | Layout 1 | `8e6ff0d29100`  |
| 2492   | Layout 1 | `8e6ff0d29100`  |
| 2487   | Layout 1 | `8e6ff0d29100`  |
| 2480   | Layout 1 | `8e6ff0d29100`  |
| 2474   | Layout 1 | `8e6ff0d29100`  |
| 2468   | Layout 1 | `8e6ff0d29100`  |
| 2460   | Layout 1 | `8e6ff0d29100`  |
| 2453   | Layout 1 | `8e6ff0d29100`  |
| 2444   | Layout 1 | `8e6ff0d29100`  |
| 2438   | Layout 1 | `8e6ff0d29100`  |
| 2434   | Layout 1 | `8e6ff0d29100`  |
| 2429   | Layout 1 | `8e6ff0d29100`  |
| 2421   | Layout 1 | `8e6ff0d29100`  |
| 2414   | Layout 1 | `8e6ff0d29100`  |
| 2407   | Layout 1 | `8e6ff0d29100`  |
| 2401   | Layout 1 | `8e6ff0d29100`  |
| 2397   | Layout 1 | `8e6ff0d29100`  |
| 2393   | Layout 1 | `8e6ff0d29100`  |
| 2384   | Layout 1 | `8e6ff0d29100`  |
| 2378   | Layout 1 | `8e6ff0d29100`  |
| 2372   | Layout 1 | `8e6ff0d29100`  |
| 2358   | Layout 1 | `8e6ff0d29100`  |
| 2352   | Layout 1 | `8e6ff0d29100`  |
| 2347   | Layout 1 | `8e6ff0d29100`  |
| 2343   | Layout 1 | `8e6ff0d29100`  |
| 2335   | Layout 1 | `8e6ff0d29100`  |
| 2327   | Layout 1 | `8e6ff0d29100`  |
| 2324   | Layout 1 | `8e6ff0d29100`  |
| 2319   | Layout 1 | `8e6ff0d29100`  |
| 2313   | Layout 1 | `8e6ff0d29100`  |
| 2308   | Layout 1 | `8e6ff0d29100`  |
| 2302   | Layout 1 | `8e6ff0d29100`  |
| 2295   | Layout 1 | `8e6ff0d29100`  |
| 2290   | Layout 1 | `8e6ff0d29100`  |
| 2284   | Layout 1 | `8e6ff0d29100`  |
| 2276   | Layout 1 | `8e6ff0d29100`  |
| 2269   | Layout 1 | `8e6ff0d29100`  |
| 2259   | Layout 1 | `8e6ff0d29100`  |
| 2250   | Layout 1 | `8e6ff0d29100`  |
| 2243   | Layout 1 | `8e6ff0d29100`  |
| 2235   | Layout 1 | `8e6ff0d29100`  |
| 2229   | Layout 1 | `8e6ff0d29100`  |
| 2224   | Layout 1 | `8e6ff0d29100`  |
| 2218   | Layout 1 | `8e6ff0d29100`  |
| 2215   | Layout 1 | `8e6ff0d29100`  |
| 2207   | Layout 1 | `8e6ff0d29100`  |
| 2203   | Layout 1 | `8e6ff0d29100`  |
| 2196   | Layout 1 | `8e6ff0d29100`  |
| 2192   | Layout 1 | `8e6ff0d29100`  |
| 2189   | Layout 1 | `8e6ff0d29100`  |
| 2183   | Layout 1 | `8e6ff0d29100`  |
| 2179   | Layout 1 | `8e6ff0d29100`  |
| 2171   | Layout 1 | `8e6ff0d29100`  |
| 2163   | Layout 1 | `8e6ff0d29100`  |
| 2156   | Layout 1 | `8e6ff0d29100`  |
| 2151   | Layout 1 | `8e6ff0d29100`  |
| 2147   | Layout 1 | `8e6ff0d29100`  |
| 2142   | Layout 1 | `8e6ff0d29100`  |
| 2138   | Layout 1 | `8e6ff0d29100`  |
| 2134   | Layout 1 | `8e6ff0d29100`  |
| 2130   | Layout 1 | `8e6ff0d29100`  |
| 2122   | Layout 1 | `8e6ff0d29100`  |
| 2107   | Layout 1 | `8e6ff0d29100`  |
| 2098   | Layout 1 | `8e6ff0d29100`  |
| 2089   | Layout 1 | `8e6ff0d29100`  |
| 2081   | Layout 1 | `8e6ff0d29100`  |
| 2073   | Layout 1 | `8e6ff0d29100`  |
| 2067   | Layout 1 | `8e6ff0d29100`  |
| 2063   | Layout 1 | `8e6ff0d29100`  |
| 2059   | Layout 1 | `8e6ff0d29100`  |
| 2052   | Layout 1 | `8e6ff0d29100`  |
| 2044   | Layout 1 | `8e6ff0d29100`  |
| 2039   | Layout 1 | `8e6ff0d29100`  |
| 2032   | Layout 1 | `8e6ff0d29100`  |
| 2025   | Layout 1 | `8e6ff0d29100`  |
| 2011   | Layout 1 | `8e6ff0d29100`  |
| 2005   | Layout 1 | `8e6ff0d29100`  |
| 2000   | Layout 1 | `8e6ff0d29100`  |
| 1996   | Layout 1 | `8e6ff0d29100`  |
| 1991   | Layout 1 | `8e6ff0d29100`  |
| 1985   | Layout 1 | `8e6ff0d29100`  |
| 1980   | Layout 1 | `8e6ff0d29100`  |
| 1969   | Layout 1 | `8e6ff0d29100`  |
| 1964   | Layout 1 | `8e6ff0d29100`  |
| 1958   | Layout 1 | `8e6ff0d29100`  |
| 1950   | Layout 1 | `8e6ff0d29100`  |
| 1945   | Layout 1 | `8e6ff0d29100`  |
| 1937   | Layout 1 | `8e6ff0d29100`  |
| 1933   | Layout 1 | `8e6ff0d29100`  |
| 1927   | Layout 1 | `8e6ff0d29100`  |
| 1921   | Layout 1 | `8e6ff0d29100`  |
| 1914   | Layout 1 | `8e6ff0d29100`  |
| 1908   | Layout 1 | `8e6ff0d29100`  |
| 1897   | Layout 1 | `8e6ff0d29100`  |
| 1892   | Layout 1 | `8e6ff0d29100`  |
| 1886   | Layout 1 | `8e6ff0d29100`  |
| 1881   | Layout 1 | `8e6ff0d29100`  |
| 1871   | Layout 1 | `8e6ff0d29100`  |
| 1866   | Layout 1 | `8e6ff0d29100`  |
| 1862   | Layout 1 | `8e6ff0d29100`  |
| 1854   | Layout 1 | `8e6ff0d29100`  |
| 1846   | Layout 1 | `8e6ff0d29100`  |
| 1838   | Layout 1 | `8e6ff0d29100`  |
| 1832   | Layout 1 | `8e6ff0d29100`  |
| 1826   | Layout 1 | `8e6ff0d29100`  |
| 1822   | Layout 1 | `8e6ff0d29100`  |
| 1818   | Layout 1 | `8e6ff0d29100`  |
| 1804   | Layout 1 | `8e6ff0d29100`  |
| 1794   | Layout 1 | `8e6ff0d29100`  |
| 1790   | Layout 1 | `8e6ff0d29100`  |
| 1784   | Layout 1 | `8e6ff0d29100`  |
| 1774   | Layout 1 | `8e6ff0d29100`  |
| 1771   | Layout 1 | `8e6ff0d29100`  |
| 1762   | Layout 1 | `8e6ff0d29100`  |
| 1759   | Layout 1 | `8e6ff0d29100`  |
| 1754   | Layout 1 | `8e6ff0d29100`  |
| 1749   | Layout 1 | `8e6ff0d29100`  |
| 1743   | Layout 1 | `8e6ff0d29100`  |
| 1737   | Layout 1 | `8e6ff0d29100`  |
| 1731   | Layout 1 | `8e6ff0d29100`  |
| 1725   | Layout 1 | `8e6ff0d29100`  |
| 1717   | Layout 1 | `8e6ff0d29100`  |
| 1710   | Layout 1 | `8e6ff0d29100`  |
| 1704   | Layout 1 | `8e6ff0d29100`  |
| 1698   | Layout 1 | `8e6ff0d29100`  |
| 1690   | Layout 1 | `8e6ff0d29100`  |
| 1685   | Layout 1 | `8e6ff0d29100`  |
| 1680   | Layout 1 | `8e6ff0d29100`  |
| 1674   | Layout 1 | `8e6ff0d29100`  |
| 1668   | Layout 1 | `8e6ff0d29100`  |
| 1659   | Layout 1 | `8e6ff0d29100`  |
| 1649   | Layout 1 | `8e6ff0d29100`  |
| 1642   | Layout 1 | `8e6ff0d29100`  |
| 1636   | Layout 1 | `8e6ff0d29100`  |
| 1628   | Layout 1 | `8e6ff0d29100`  |
| 1622   | Layout 1 | `8e6ff0d29100`  |
| 1614   | Layout 1 | `8e6ff0d29100`  |
| 1608   | Layout 1 | `8e6ff0d29100`  |
| 1602   | Layout 1 | `8e6ff0d29100`  |
| 1598   | Layout 1 | `8e6ff0d29100`  |
| 1594   | Layout 1 | `8e6ff0d29100`  |
| 1590   | Layout 1 | `8e6ff0d29100`  |
| 1587   | Layout 1 | `8e6ff0d29100`  |
| 1584   | Layout 1 | `8e6ff0d29100`  |
| 1579   | Layout 1 | `8e6ff0d29100`  |
| 1572   | Layout 1 | `8e6ff0d29100`  |
| 1565   | Layout 1 | `8e6ff0d29100`  |
| 1559   | Layout 1 | `8e6ff0d29100`  |
| 1554   | Layout 1 | `8e6ff0d29100`  |
| 1547   | Layout 1 | `8e6ff0d29100`  |
| 1537   | Layout 1 | `8e6ff0d29100`  |
| 1529   | Layout 1 | `8e6ff0d29100`  |
| 1524   | Layout 1 | `8e6ff0d29100`  |
| 1519   | Layout 1 | `8e6ff0d29100`  |
| 1509   | Layout 1 | `8e6ff0d29100`  |
| 1506   | Layout 1 | `8e6ff0d29100`  |
| 1504   | Layout 1 | `8e6ff0d29100`  |
| 1500   | Layout 1 | `8e6ff0d29100`  |
| 1493   | Layout 1 | `8e6ff0d29100`  |
| 1489   | Layout 1 | `8e6ff0d29100`  |
| 1485   | Layout 1 | `8e6ff0d29100`  |
| 1481   | Layout 1 | `8e6ff0d29100`  |
| 1474   | Layout 1 | `8e6ff0d29100`  |
| 1466   | Layout 1 | `8e6ff0d29100`  |
| 1462   | Layout 1 | `8e6ff0d29100`  |
| 1459   | Layout 1 | `8e6ff0d29100`  |
| 1453   | Layout 1 | `8e6ff0d29100`  |
| 1450   | Layout 1 | `8e6ff0d29100`  |
| 1445   | Layout 1 | `8e6ff0d29100`  |
| 1439   | Layout 1 | `8e6ff0d29100`  |
| 1433   | Layout 1 | `8e6ff0d29100`  |
| 1430   | Layout 1 | `8e6ff0d29100`  |
| 1426   | Layout 1 | `8e6ff0d29100`  |
| 1421   | Layout 1 | `8e6ff0d29100`  |
| 1417   | Layout 1 | `8e6ff0d29100`  |
| 1416   | Layout 1 | `8e6ff0d29100`  |
| 1409   | No file  | `8e6ff0d29100`  |
| 1405   | No file  | `8e6ff0d29100`  |
| 1401   | No file  | `8e6ff0d29100`  |
| 1396   | No file  | `8e6ff0d29100`  |
| 1391   | No file  | `8e6ff0d29100`  |
| 1390   | No file  | `8e6ff0d29100`  |
| 1386   | No file  | `8e6ff0d29100`  |
| 1381   | No file  | `8e6ff0d29100`  |
| 1379   | No file  | `8e6ff0d29100`  |
| 1372   | No file  | `8e6ff0d29100`  |
| 1366   | No file  | `8e6ff0d29100`  |
| 1364   | No file  | `8e6ff0d29100`  |
| 1363   | No file  | `8e6ff0d29100`  |
| 1360   | No file  | `8e6ff0d29100`  |
| 1358   | No file  | `8e6ff0d29100`  |
| 1355   | No file  | `8e6ff0d29100`  |
| 1351   | No file  | `8e6ff0d29100`  |
| 1348   | No file  | `8e6ff0d29100`  |
| 1346   | No file  | `8e6ff0d29100`  |
| 1341   | No file  | `8e6ff0d29100`  |
| 1340   | No file  | `8e6ff0d29100`  |
| 1338   | No file  | `8e6ff0d29100`  |
| 1335   | No file  | `8e6ff0d29100`  |
| 1333   | No file  | `8e6ff0d29100`  |
| 1329   | No file  | `8e6ff0d29100`  |
| 1327   | No file  | `8e6ff0d29100`  |
| 1324   | No file  | `8e6ff0d29100`  |
| 1321   | No file  | `8e6ff0d29100`  |
| 1319   | No file  | `8e6ff0d29100`  |
| 1318   | No file  | `8e6ff0d29100`  |
| 1316   | No file  | `8e6ff0d29100`  |
| 1313   | No file  | `8e6ff0d29100`  |
| 1311   | No file  | `8e6ff0d29100`  |
| 1309   | No file  | `8e6ff0d29100`  |
| 1304   | No file  | `8e6ff0d29100`  |
| 1292   | No file  | `8e6ff0d29100`  |
| 1286   | No file  | `8e6ff0d29100`  |
| 1280   | No file  | `8e6ff0d29100`  |
| 1276   | No file  | `8e6ff0d29100`  |
| 1267   | No file  | `8e6ff0d29100`  |
| 1261   | No file  | `8e6ff0d29100`  |
| 1256   | No file  | `8e6ff0d29100`  |
| 1250   | No file  | `8e6ff0d29100`  |
| 1246   | No file  | `8e6ff0d29100`  |
| 1239   | No file  | `8e6ff0d29100`  |
| 1230   | No file  | `8e6ff0d29100`  |
| 1226   | No file  | `8e6ff0d29100`  |
| 1220   | No file  | `8e6ff0d29100`  |
| 1217   | No file  | `8e6ff0d29100`  |
| 1211   | No file  | `8e6ff0d29100`  |
| 1210   | No file  | `8e6ff0d29100`  |
| 1208   | No file  | `8e6ff0d29100`  |
| 1203   | No file  | `8e6ff0d29100`  |
| 1197   | No file  | `8e6ff0d29100`  |
| 1194   | No file  | `8e6ff0d29100`  |
| 1192   | No file  | `8e6ff0d29100`  |
| 1187   | No file  | `8e6ff0d29100`  |
| 1183   | No file  | `8e6ff0d29100`  |
| 1177   | No file  | `8e6ff0d29100`  |
| 1173   | No file  | `8e6ff0d29100`  |
| 1167   | No file  | `8e6ff0d29100`  |
| 1164   | No file  | `8e6ff0d29100`  |
| 1156   | No file  | `8e6ff0d29100`  |
| 1149   | No file  | `8e6ff0d29100`  |
| 1144   | No file  | `8e6ff0d29100`  |
| 1137   | No file  | `8e6ff0d29100`  |
| 1132   | No file  | `8e6ff0d29100`  |
| 1127   | No file  | `8e6ff0d29100`  |
| 1122   | No file  | `8e6ff0d29100`  |
| 1118   | No file  | `8e6ff0d29100`  |
| 1114   | No file  | `8e6ff0d29100`  |
| 1109   | No file  | `8e6ff0d29100`  |
| 1102   | No file  | `8e6ff0d29100`  |
| 1096   | No file  | `8e6ff0d29100`  |
| 1088   | No file  | `8e6ff0d29100`  |
| 1081   | No file  | `8e6ff0d29100`  |
| 1076   | No file  | `8e6ff0d29100`  |
| 1069   | No file  | `8e6ff0d29100`  |
| 1064   | No file  | `8e6ff0d29100`  |
| 1058   | No file  | `8e6ff0d29100`  |
| 1051   | No file  | `8e6ff0d29100`  |
| 1044   | No file  | `8e6ff0d29100`  |
| 1036   | No file  | `8e6ff0d29100`  |
| 1026   | No file  | `8e6ff0d29100`  |
| 1016   | No file  | `8e6ff0d29100`  |
| 1009   | No file  | `8e6ff0d29100`  |
| 1005   | No file  | `8e6ff0d29100`  |
| 1000   | No file  | `8e6ff0d29100`  |
| 998    | No file  | `8e6ff0d29100`  |
| 990    | No file  | `8e6ff0d29100`  |
| 979    | No file  | `8e6ff0d29100`  |
| 972    | No file  | `8e6ff0d29100`  |
| 963    | No file  | `8e6ff0d29100`  |
| 955    | No file  | `8e6ff0d29100`  |
| 946    | No file  | `8e6ff0d29100`  |
| 938    | No file  | `8e6ff0d29100`  |
| 927    | No file  | `8e6ff0d29100`  |
| 911    | No file  | `8e6ff0d29100`  |
| 904    | No file  | `8e6ff0d29100`  |
| 899    | No file  | `8e6ff0d29100`  |
| 894    | No file  | `8e6ff0d29100`  |
| 885    | No file  | `8e6ff0d29100`  |
| 879    | No file  | `8e6ff0d29100`  |
| 872    | No file  | `8e6ff0d29100`  |
| 864    | No file  | `8e6ff0d29100`  |
| 855    | No file  | `8e6ff0d29100`  |
| 853    | No file  | `8e6ff0d29100`  |
| 845    | No file  | `8e6ff0d29100`  |
| 837    | No file  | `8e6ff0d29100`  |
| 829    | No file  | `8e6ff0d29100`  |
| 822    | No file  | `8e6ff0d29100`  |
| 814    | No file  | `8e6ff0d29100`  |
| 805    | No file  | `8e6ff0d29100`  |
| 794    | No file  | `8e6ff0d29100`  |
| 787    | No file  | `8e6ff0d29100`  |
| 780    | No file  | `8e6ff0d29100`  |
| 771    | No file  | `8e6ff0d29100`  |
| 760    | No file  | `8e6ff0d29100`  |
| 748    | No file  | `8e6ff0d29100`  |
| 741    | No file  | `8e6ff0d29100`  |
| 736    | No file  | `8e6ff0d29100`  |
| 731    | No file  | `8e6ff0d29100`  |
| 723    | No file  | `8e6ff0d29100`  |
| 711    | No file  | `8e6ff0d29100`  |
| 707    | No file  | `8e6ff0d29100`  |
| 697    | No file  | `8e6ff0d29100`  |
| 689    | No file  | `8e6ff0d29100`  |
| 683    | No file  | `8e6ff0d29100`  |
| 678    | No file  | `8e6ff0d29100`  |
| 670    | No file  | `8e6ff0d29100`  |
| 661    | No file  | `8e6ff0d29100`  |
| 656    | No file  | `8e6ff0d29100`  |
| 652    | No file  | `8e6ff0d29100`  |
| 643    | No file  | `8e6ff0d29100`  |
| 637    | No file  | `8e6ff0d29100`  |
| 630    | No file  | `8e6ff0d29100`  |
| 627    | No file  | `8e6ff0d29100`  |
| 621    | No file  | `8e6ff0d29100`  |
| 617    | No file  | `8e6ff0d29100`  |
| 615    | No file  | `8e6ff0d29100`  |
| 606    | No file  | `8e6ff0d29100`  |
| 599    | No file  | `8e6ff0d29100`  |
| 592    | No file  | `8e6ff0d29100`  |
| 586    | No file  | `8e6ff0d29100`  |
| 577    | No file  | `8e6ff0d29100`  |
| 569    | No file  | `8e6ff0d29100`  |
| 561    | No file  | `8e6ff0d29100`  |
| 554    | No file  | `8e6ff0d29100`  |
| 542    | No file  | `8e6ff0d29100`  |
| 532    | No file  | `8e6ff0d29100`  |
| 531    | No file  | `8e6ff0d29100`  |
| 526    | No file  | `8e6ff0d29100`  |
| 521    | No file  | `8e6ff0d29100`  |
| 517    | No file  | `8e6ff0d29100`  |
| 510    | No file  | `8e6ff0d29100`  |
| 508    | No file  | `8e6ff0d29100`  |
| 504    | No file  | `8e6ff0d29100`  |
| 497    | No file  | `8e6ff0d29100`  |
| 491    | No file  | `8e6ff0d29100`  |
| 485    | No file  | `8e6ff0d29100`  |
| 478    | No file  | `8e6ff0d29100`  |
| 472    | No file  | `8e6ff0d29100`  |
| 466    | No file  | `8e6ff0d29100`  |
| 457    | No file  | `8e6ff0d29100`  |
| 452    | No file  | `8e6ff0d29100`  |
| 449    | No file  | `8e6ff0d29100`  |
| 435    | No file  | `8e6ff0d29100`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                 |
| --------------------------------- | -------- | -------------------------------------------------------------------- |
| `characteraudioradiusoffset.dbss` | Optional | Maps `character_key` to its row; the main file can be walked without it |
| `characterstaticoffset.dbss`      | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key link |
| `languagedata_en.loc`             | Optional | Character names (LOC type 6)                                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | Character key; unique, and every key has a `characterstatic.dbss` row (client 3474) |
| `+0x02` | f32  | sound_radius  | Distance the character's sounds carry; whole numbers from `8,000` to `100,000` (client 3474) |

### `characteraudioradiusoffset.dbss`

| Offset              | Type               | Field          | Notes                                                |
| ------------------- | ------------------ | -------------- | ---------------------------------------------------- |
| `+0x00`             | char[4]            | magic          | `PABR` (ASCII)                                       |
| `+0x04`             | u32                | count          | Number of index rows; equals the main file's `count` |
| `+0x08`             | Index Row[count]   | records        | See Index Row                                        |
| `records+0x00`      | String Table       | string_table   | The 12-byte trailer starts here; see String Table    |
| `string_table+0x00` | u32                | end_of_records | Byte offset of the end of `records` in this file     |
| `string_table+0x04` | u32                | zero           | Always `0`                                           |

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | character_key | Equals the row's own `character_key`                         |
| `+0x02` | u32  | offset        | Byte offset of the row in `characteraudioradius.dbss`, at its `character_key` |
| `+0x06` | u32  | size          | Row byte count; always `6`                                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Field Names

The names come from the `Monster_SoundRadius` sheet of a private server's `DataSheets.bexcel` on client 1784, columns `CharacterKey` and `SoundRadius`. The sheet's third column, `ContentsGroupKey`, is not in the file. Of the sheet's 12 rows, 11 are in the client 3474 file and all 11 match `sound_radius`. The 12th, Lekrashan `29779` (`8,000`, contents group `705`), is missing from both the client 1784 and the client 3474 file.

## Notes

- The main file stores the rows in a different order than the index; neither is sorted by key.
- Client 1784 holds 11 rows, client 3474 holds 27. The 16 added keys are four each of Moghulis (`29697` to `29700`), Org (`29693` to `29696`) and Wilderness Golem (`28628` to `28630`, `29692`), then Baby Vell (`21060`), Snowstorm (`23469`), Tripped Safeguard (`24688`) and `Tutorial_Illezra_Move` (`411`). The 11 shared keys have the same `sound_radius` in both clients.
- On client 3474 three rows set less than `100,000`: Lekrashan `21477` (`8,000`), Snowstorm `23469` (`10,000`) and Tripped Safeguard `24688` (`15,000`). The other 24 set `100,000`.

## Open Questions

### Radius Unit and Default

`sound_radius` is probably in centimetres, the unit of world positions, which makes `100,000` one kilometre. Neither the unit nor the radius a character without a row gets is in the file; the client code that reads the table would answer both.
