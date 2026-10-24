# `itemexchangebynpc.dbss` Format

## Purpose

The item exchanges NPCs offer: each row trades a count of one item for a
count of another. NPC dialogs list these rows by key through
[`displayexchangeitemnpc.dbss`](displayexchangeitemnpc_dbss.md); the
exchange window shows the need and result item, and the worker hire window
shows the need item only. `itemexchangebynpcoffset.dbss` is the index into
it, keyed by the exchange key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | -------------- | --------- |
| 1      | 1346 and later | 3483    | `itemexchangebynpc.dbss`       | 5,856 | 209 Row        | 28        |
| 1      | 1346 and later | 3483    | `itemexchangebynpcoffset.dbss` | 2,094 | 209 Offset Row | 10        |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 1      | `itemexchangebynpc.dbss`       | 5,856 B (100.0%) | 0 B (0.0%) |
| 1      | `itemexchangebynpcoffset.dbss` | 2,094 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `f977b8903a5a`  |
| 3482   | Layout 1             | `f977b8903a5a`  |
| 3474   | Layout 1             | `f977b8903a5a`  |
| 3473   | Layout 1             | `f977b8903a5a`  |
| 3464   | Layout 1             | `f977b8903a5a`  |
| 3458   | Layout 1             | `f977b8903a5a`  |
| 3454   | Layout 1             | `f977b8903a5a`  |
| 3444   | Layout 1             | `f977b8903a5a`  |
| 3435   | Layout 1             | `f977b8903a5a`  |
| 3426   | Layout 1             | `f977b8903a5a`  |
| 3418   | Layout 1             | `f977b8903a5a`  |
| 3412   | Layout 1             | `f977b8903a5a`  |
| 3402   | Layout 1             | `f977b8903a5a`  |
| 3396   | Layout 1             | `f977b8903a5a`  |
| 3387   | Layout 1             | `f977b8903a5a`  |
| 3381   | Layout 1             | `f977b8903a5a`  |
| 3373   | Layout 1             | `f977b8903a5a`  |
| 3364   | Layout 1             | `f977b8903a5a`  |
| 3356   | Layout 1             | `f977b8903a5a`  |
| 3349   | Layout 1             | `f977b8903a5a`  |
| 3342   | Layout 1             | `f977b8903a5a`  |
| 3335   | Layout 1             | `f977b8903a5a`  |
| 3326   | Layout 1             | `f977b8903a5a`  |
| 3321   | Layout 1             | `f977b8903a5a`  |
| 3314   | Layout 1             | `f977b8903a5a`  |
| 3303   | Layout 1             | `f977b8903a5a`  |
| 3302   | Layout 1             | `f977b8903a5a`  |
| 3293   | Layout 1             | `f977b8903a5a`  |
| 3283   | Layout 1             | `f977b8903a5a`  |
| 3275   | Layout 1             | `f977b8903a5a`  |
| 3267   | Layout 1             | `f977b8903a5a`  |
| 3258   | Layout 1             | `f977b8903a5a`  |
| 3251   | Layout 1             | `f977b8903a5a`  |
| 3242   | Layout 1             | `f977b8903a5a`  |
| 3235   | Layout 1             | `f977b8903a5a`  |
| 3229   | Layout 1             | `f977b8903a5a`  |
| 3212   | Layout 1             | `f977b8903a5a`  |
| 3203   | Layout 1             | `f977b8903a5a`  |
| 3193   | Layout 1             | `f977b8903a5a`  |
| 3186   | Layout 1             | `f977b8903a5a`  |
| 3177   | Layout 1             | `f977b8903a5a`  |
| 3169   | Layout 1             | `f977b8903a5a`  |
| 3158   | Layout 1             | `f977b8903a5a`  |
| 3151   | Layout 1             | `f977b8903a5a`  |
| 3144   | Layout 1             | `f977b8903a5a`  |
| 3133   | Layout 1             | `f977b8903a5a`  |
| 3125   | Layout 1             | `f977b8903a5a`  |
| 3118   | Layout 1             | `f977b8903a5a`  |
| 3111   | Layout 1             | `f977b8903a5a`  |
| 3103   | Layout 1             | `f977b8903a5a`  |
| 3095   | Layout 1             | `f977b8903a5a`  |
| 3086   | Layout 1             | `f977b8903a5a`  |
| 3072   | Layout 1             | `f977b8903a5a`  |
| 3062   | Layout 1             | `f977b8903a5a`  |
| 3052   | Layout 1             | `f977b8903a5a`  |
| 3045   | Layout 1             | `f977b8903a5a`  |
| 3037   | Layout 1             | `f977b8903a5a`  |
| 3030   | Layout 1             | `f977b8903a5a`  |
| 3021   | Layout 1             | `f977b8903a5a`  |
| 3012   | Layout 1             | `f977b8903a5a`  |
| 3002   | Layout 1             | `f977b8903a5a`  |
| 2995   | Layout 1             | `f977b8903a5a`  |
| 2987   | Layout 1             | `f977b8903a5a`  |
| 2978   | Layout 1             | `f977b8903a5a`  |
| 2970   | Layout 1             | `f977b8903a5a`  |
| 2959   | Layout 1             | `f977b8903a5a`  |
| 2951   | Layout 1             | `f977b8903a5a`  |
| 2942   | Layout 1             | `f977b8903a5a`  |
| 2935   | Layout 1             | `f977b8903a5a`  |
| 2932   | Layout 1             | `f977b8903a5a`  |
| 2923   | Layout 1             | `f977b8903a5a`  |
| 2919   | Layout 1             | `f977b8903a5a`  |
| 2907   | Layout 1             | `f977b8903a5a`  |
| 2900   | Layout 1             | `f977b8903a5a`  |
| 2891   | Layout 1             | `f977b8903a5a`  |
| 2882   | Layout 1             | `f977b8903a5a`  |
| 2872   | Layout 1             | `f977b8903a5a`  |
| 2863   | Layout 1             | `f977b8903a5a`  |
| 2855   | Layout 1             | `f977b8903a5a`  |
| 2849   | Layout 1             | `f977b8903a5a`  |
| 2844   | Layout 1             | `f977b8903a5a`  |
| 2834   | Layout 1             | `f977b8903a5a`  |
| 2825   | Layout 1             | `f977b8903a5a`  |
| 2819   | Layout 1             | `f977b8903a5a`  |
| 2811   | Layout 1             | `f977b8903a5a`  |
| 2803   | Layout 1             | `f977b8903a5a`  |
| 2794   | Layout 1             | `f977b8903a5a`  |
| 2783   | Layout 1             | `f977b8903a5a`  |
| 2774   | Layout 1             | `f977b8903a5a`  |
| 2765   | Layout 1             | `f977b8903a5a`  |
| 2756   | Layout 1             | `f977b8903a5a`  |
| 2750   | Layout 1             | `f977b8903a5a`  |
| 2743   | Layout 1             | `f977b8903a5a`  |
| 2736   | Layout 1             | `f977b8903a5a`  |
| 2726   | Layout 1             | `f977b8903a5a`  |
| 2717   | Layout 1             | `f977b8903a5a`  |
| 2709   | Layout 1             | `f977b8903a5a`  |
| 2703   | Layout 1             | `f977b8903a5a`  |
| 2695   | Layout 1             | `f977b8903a5a`  |
| 2684   | Layout 1             | `f977b8903a5a`  |
| 2672   | Layout 1             | `f977b8903a5a`  |
| 2665   | Layout 1             | `f977b8903a5a`  |
| 2657   | Layout 1             | `f977b8903a5a`  |
| 2649   | Layout 1             | `f977b8903a5a`  |
| 2644   | Layout 1             | `f977b8903a5a`  |
| 2637   | Layout 1             | `f977b8903a5a`  |
| 2629   | Layout 1             | `f977b8903a5a`  |
| 2619   | Layout 1             | `f977b8903a5a`  |
| 2612   | Layout 1             | `f977b8903a5a`  |
| 2606   | Layout 1             | `f977b8903a5a`  |
| 2602   | Layout 1             | `f977b8903a5a`  |
| 2601   | Layout 1             | `f977b8903a5a`  |
| 2592   | Layout 1             | `f977b8903a5a`  |
| 2583   | Layout 1             | `f977b8903a5a`  |
| 2575   | Layout 1             | `f977b8903a5a`  |
| 2567   | Layout 1             | `f977b8903a5a`  |
| 2560   | Layout 1             | `f977b8903a5a`  |
| 2553   | Layout 1             | `f977b8903a5a`  |
| 2545   | Layout 1             | `f977b8903a5a`  |
| 2538   | Layout 1             | `f977b8903a5a`  |
| 2529   | Layout 1             | `f977b8903a5a`  |
| 2519   | Layout 1             | `f977b8903a5a`  |
| 2513   | Layout 1             | `f977b8903a5a`  |
| 2510   | Layout 1             | `f977b8903a5a`  |
| 2507   | Layout 1             | `f977b8903a5a`  |
| 2503   | Layout 1             | `f977b8903a5a`  |
| 2498   | Layout 1             | `f977b8903a5a`  |
| 2492   | Layout 1             | `f977b8903a5a`  |
| 2487   | Layout 1             | `f977b8903a5a`  |
| 2480   | Layout 1             | `f977b8903a5a`  |
| 2474   | Layout 1             | `f977b8903a5a`  |
| 2468   | Layout 1             | `f977b8903a5a`  |
| 2460   | Layout 1             | `f977b8903a5a`  |
| 2453   | Layout 1             | `f977b8903a5a`  |
| 2444   | Layout 1             | `f977b8903a5a`  |
| 2438   | Layout 1             | `f977b8903a5a`  |
| 2434   | Layout 1             | `f977b8903a5a`  |
| 2429   | Layout 1             | `f977b8903a5a`  |
| 2421   | Layout 1             | `f977b8903a5a`  |
| 2414   | Layout 1             | `f977b8903a5a`  |
| 2407   | Layout 1             | `f977b8903a5a`  |
| 2401   | Layout 1             | `f977b8903a5a`  |
| 2397   | Layout 1             | `f977b8903a5a`  |
| 2393   | Layout 1             | `f977b8903a5a`  |
| 2384   | Layout 1             | `f977b8903a5a`  |
| 2378   | Layout 1             | `f977b8903a5a`  |
| 2372   | Layout 1             | `f977b8903a5a`  |
| 2358   | Layout 1             | `f977b8903a5a`  |
| 2352   | Layout 1             | `f977b8903a5a`  |
| 2347   | Layout 1             | `f977b8903a5a`  |
| 2343   | Layout 1             | `f977b8903a5a`  |
| 2335   | Layout 1             | `f977b8903a5a`  |
| 2327   | Layout 1             | `f977b8903a5a`  |
| 2324   | Layout 1             | `f977b8903a5a`  |
| 2319   | Layout 1             | `f977b8903a5a`  |
| 2313   | Layout 1             | `f977b8903a5a`  |
| 2308   | Layout 1             | `f977b8903a5a`  |
| 2302   | Layout 1             | `f977b8903a5a`  |
| 2295   | Layout 1             | `f977b8903a5a`  |
| 2290   | Layout 1             | `f977b8903a5a`  |
| 2284   | Layout 1             | `f977b8903a5a`  |
| 2276   | Layout 1             | `f977b8903a5a`  |
| 2269   | Layout 1             | `f977b8903a5a`  |
| 2259   | Layout 1             | `f977b8903a5a`  |
| 2250   | Layout 1             | `f977b8903a5a`  |
| 2243   | Layout 1             | `f977b8903a5a`  |
| 2235   | Layout 1             | `f977b8903a5a`  |
| 2229   | Layout 1             | `f977b8903a5a`  |
| 2224   | Layout 1             | `f977b8903a5a`  |
| 2218   | Layout 1             | `f977b8903a5a`  |
| 2215   | Layout 1             | `f977b8903a5a`  |
| 2207   | Layout 1             | `f977b8903a5a`  |
| 2203   | Layout 1             | `f977b8903a5a`  |
| 2196   | Layout 1             | `f977b8903a5a`  |
| 2192   | Layout 1             | `f977b8903a5a`  |
| 2189   | Layout 1             | `f977b8903a5a`  |
| 2183   | Layout 1             | `f977b8903a5a`  |
| 2179   | Layout 1             | `f977b8903a5a`  |
| 2171   | Layout 1             | `f977b8903a5a`  |
| 2163   | Layout 1             | `f977b8903a5a`  |
| 2156   | Layout 1             | `f977b8903a5a`  |
| 2151   | Layout 1             | `f977b8903a5a`  |
| 2147   | Layout 1             | `f977b8903a5a`  |
| 2142   | Layout 1             | `f977b8903a5a`  |
| 2138   | Layout 1             | `f977b8903a5a`  |
| 2134   | Layout 1             | `f977b8903a5a`  |
| 2130   | Layout 1             | `f977b8903a5a`  |
| 2122   | Layout 1             | `f977b8903a5a`  |
| 2107   | Layout 1             | `f977b8903a5a`  |
| 2098   | Layout 1             | `f977b8903a5a`  |
| 2089   | Layout 1             | `f977b8903a5a`  |
| 2081   | Layout 1             | `f977b8903a5a`  |
| 2073   | Layout 1             | `f977b8903a5a`  |
| 2067   | Layout 1             | `f977b8903a5a`  |
| 2063   | Layout 1             | `f977b8903a5a`  |
| 2059   | Layout 1             | `f977b8903a5a`  |
| 2052   | Layout 1             | `f977b8903a5a`  |
| 2044   | Layout 1             | `f977b8903a5a`  |
| 2039   | Layout 1             | `f977b8903a5a`  |
| 2032   | Layout 1             | `f977b8903a5a`  |
| 2025   | Layout 1             | `f977b8903a5a`  |
| 2011   | Layout 1             | `f977b8903a5a`  |
| 2005   | Layout 1             | `f977b8903a5a`  |
| 2000   | Layout 1             | `f977b8903a5a`  |
| 1996   | Layout 1             | `f977b8903a5a`  |
| 1991   | Layout 1             | `f977b8903a5a`  |
| 1985   | Layout 1             | `f977b8903a5a`  |
| 1980   | Layout 1             | `f977b8903a5a`  |
| 1969   | Layout 1             | `f977b8903a5a`  |
| 1964   | Layout 1             | `f977b8903a5a`  |
| 1958   | Layout 1             | `f977b8903a5a`  |
| 1950   | Layout 1             | `f977b8903a5a`  |
| 1945   | Layout 1             | `f977b8903a5a`  |
| 1937   | Layout 1             | `f977b8903a5a`  |
| 1933   | Layout 1             | `f977b8903a5a`  |
| 1927   | Layout 1             | `f977b8903a5a`  |
| 1921   | Layout 1             | `f977b8903a5a`  |
| 1914   | Layout 1             | `f977b8903a5a`  |
| 1908   | Layout 1             | `f977b8903a5a`  |
| 1897   | Layout 1             | `f977b8903a5a`  |
| 1892   | Layout 1             | `f977b8903a5a`  |
| 1886   | Layout 1             | `f977b8903a5a`  |
| 1881   | Layout 1             | `f977b8903a5a`  |
| 1871   | Layout 1             | `f977b8903a5a`  |
| 1866   | Layout 1             | `f977b8903a5a`  |
| 1862   | Layout 1             | `f977b8903a5a`  |
| 1854   | Layout 1             | `f977b8903a5a`  |
| 1846   | Layout 1             | `f977b8903a5a`  |
| 1838   | Layout 1             | `f977b8903a5a`  |
| 1832   | Layout 1             | `f977b8903a5a`  |
| 1826   | Layout 1             | `f977b8903a5a`  |
| 1822   | Layout 1             | `f977b8903a5a`  |
| 1818   | Layout 1             | `f977b8903a5a`  |
| 1804   | Layout 1             | `f977b8903a5a`  |
| 1794   | Layout 1             | `f977b8903a5a`  |
| 1790   | Layout 1             | `f977b8903a5a`  |
| 1784   | Layout 1             | `f977b8903a5a`  |
| 1774   | Layout 1             | `f977b8903a5a`  |
| 1771   | Layout 1             | `f977b8903a5a`  |
| 1762   | Layout 1             | `f977b8903a5a`  |
| 1759   | Layout 1             | `f977b8903a5a`  |
| 1754   | Layout 1             | `f977b8903a5a`  |
| 1749   | Layout 1             | `f977b8903a5a`  |
| 1743   | Layout 1             | `f977b8903a5a`  |
| 1737   | Layout 1             | `f977b8903a5a`  |
| 1731   | Layout 1             | `f977b8903a5a`  |
| 1725   | Layout 1             | `f977b8903a5a`  |
| 1717   | Layout 1             | `f977b8903a5a`  |
| 1710   | Layout 1             | `f977b8903a5a`  |
| 1704   | Layout 1             | `f977b8903a5a`  |
| 1698   | Layout 1             | `f977b8903a5a`  |
| 1690   | Layout 1             | `f977b8903a5a`  |
| 1685   | Layout 1             | `f977b8903a5a`  |
| 1680   | Layout 1             | `f977b8903a5a`  |
| 1674   | Layout 1             | `f977b8903a5a`  |
| 1668   | Layout 1             | `f977b8903a5a`  |
| 1659   | Layout 1             | `f977b8903a5a`  |
| 1649   | Layout 1             | `f977b8903a5a`  |
| 1642   | Layout 1             | `f977b8903a5a`  |
| 1636   | Layout 1             | `f977b8903a5a`  |
| 1628   | Layout 1             | `f977b8903a5a`  |
| 1622   | Layout 1             | `f977b8903a5a`  |
| 1614   | Layout 1             | `f977b8903a5a`  |
| 1608   | Layout 1             | `f977b8903a5a`  |
| 1602   | Layout 1             | `f977b8903a5a`  |
| 1598   | Layout 1             | `f977b8903a5a`  |
| 1594   | Layout 1             | `f977b8903a5a`  |
| 1590   | Layout 1             | `f977b8903a5a`  |
| 1587   | Layout 1             | `f977b8903a5a`  |
| 1584   | Layout 1             | `f977b8903a5a`  |
| 1579   | Layout 1             | `f977b8903a5a`  |
| 1572   | Layout 1             | `f977b8903a5a`  |
| 1565   | Layout 1             | `f977b8903a5a`  |
| 1559   | Layout 1             | `f977b8903a5a`  |
| 1554   | Layout 1             | `f977b8903a5a`  |
| 1547   | Layout 1             | `f977b8903a5a`  |
| 1537   | Layout 1             | `f977b8903a5a`  |
| 1529   | Layout 1             | `f977b8903a5a`  |
| 1524   | Layout 1             | `f977b8903a5a`  |
| 1519   | Layout 1             | `f977b8903a5a`  |
| 1509   | Layout 1             | `f977b8903a5a`  |
| 1506   | Layout 1             | `f977b8903a5a`  |
| 1504   | Layout 1             | `f977b8903a5a`  |
| 1500   | Layout 1             | `f977b8903a5a`  |
| 1493   | Layout 1             | `f977b8903a5a`  |
| 1489   | Layout 1             | `f977b8903a5a`  |
| 1485   | Layout 1             | `f977b8903a5a`  |
| 1481   | Layout 1             | `f977b8903a5a`  |
| 1474   | Layout 1             | `f977b8903a5a`  |
| 1466   | Layout 1             | `f977b8903a5a`  |
| 1462   | Layout 1             | `f977b8903a5a`  |
| 1459   | Layout 1             | `f977b8903a5a`  |
| 1453   | Layout 1             | `f977b8903a5a`  |
| 1450   | Layout 1             | `f977b8903a5a`  |
| 1445   | Layout 1             | `f977b8903a5a`  |
| 1439   | Layout 1             | `f977b8903a5a`  |
| 1433   | Layout 1             | `f977b8903a5a`  |
| 1430   | Layout 1             | `f977b8903a5a`  |
| 1426   | Layout 1             | `f977b8903a5a`  |
| 1421   | Layout 1             | `f977b8903a5a`  |
| 1417   | Layout 1             | `f977b8903a5a`  |
| 1416   | Layout 1             | `f977b8903a5a`  |
| 1409   | Layout 1             | `f977b8903a5a`  |
| 1405   | Layout 1             | `f977b8903a5a`  |
| 1401   | Layout 1             | `f977b8903a5a`  |
| 1396   | Layout 1             | `f977b8903a5a`  |
| 1391   | Layout 1             | `f977b8903a5a`  |
| 1390   | Layout 1             | `f977b8903a5a`  |
| 1386   | Layout 1             | `f977b8903a5a`  |
| 1381   | Layout 1             | `f977b8903a5a`  |
| 1379   | Layout 1             | `f977b8903a5a`  |
| 1372   | Layout 1             | `f977b8903a5a`  |
| 1366   | Layout 1             | `f977b8903a5a`  |
| 1364   | Layout 1             | `f977b8903a5a`  |
| 1363   | Layout 1             | `f977b8903a5a`  |
| 1360   | Layout 1             | `f977b8903a5a`  |
| 1358   | Layout 1             | `f977b8903a5a`  |
| 1355   | Layout 1             | `f977b8903a5a`  |
| 1351   | Layout 1             | `f977b8903a5a`  |
| 1348   | Layout 1             | `f977b8903a5a`  |
| 1346   | Layout 1             | `f977b8903a5a`  |
| 1341   | No documented layout | `f977b8903a5a`  |
| 1340   | No documented layout | `f977b8903a5a`  |
| 1338   | No documented layout | `f977b8903a5a`  |
| 1335   | No documented layout | `f977b8903a5a`  |
| 1333   | No documented layout | `f977b8903a5a`  |
| 1329   | No documented layout | `f977b8903a5a`  |
| 1327   | No documented layout | `f977b8903a5a`  |
| 1324   | No documented layout | `f977b8903a5a`  |
| 1321   | No documented layout | `f977b8903a5a`  |
| 1319   | No documented layout | `f977b8903a5a`  |
| 1318   | No documented layout | `f977b8903a5a`  |
| 1316   | No documented layout | `f977b8903a5a`  |
| 1313   | No documented layout | `f977b8903a5a`  |
| 1311   | No documented layout | `f977b8903a5a`  |
| 1309   | No documented layout | `f977b8903a5a`  |
| 1304   | No documented layout | `f977b8903a5a`  |
| 1292   | No documented layout | `f977b8903a5a`  |
| 1286   | No documented layout | `f977b8903a5a`  |
| 1280   | No documented layout | `f977b8903a5a`  |
| 1276   | No documented layout | `f977b8903a5a`  |
| 1267   | No file              | `f977b8903a5a`  |
| 1261   | No file              | `f977b8903a5a`  |
| 1256   | No file              | `f977b8903a5a`  |
| 1250   | No file              | `f977b8903a5a`  |
| 1246   | No file              | `f977b8903a5a`  |
| 1239   | No file              | `f977b8903a5a`  |
| 1230   | No file              | `f977b8903a5a`  |
| 1226   | No file              | `f977b8903a5a`  |
| 1220   | No file              | `f977b8903a5a`  |
| 1217   | No file              | `f977b8903a5a`  |
| 1211   | No file              | `f977b8903a5a`  |
| 1210   | No file              | `f977b8903a5a`  |
| 1208   | No file              | `f977b8903a5a`  |
| 1203   | No file              | `f977b8903a5a`  |
| 1197   | No file              | `f977b8903a5a`  |
| 1194   | No file              | `f977b8903a5a`  |
| 1192   | No file              | `f977b8903a5a`  |
| 1187   | No file              | `f977b8903a5a`  |
| 1183   | No file              | `f977b8903a5a`  |
| 1177   | No file              | `f977b8903a5a`  |
| 1173   | No file              | `f977b8903a5a`  |
| 1167   | No file              | `f977b8903a5a`  |
| 1164   | No file              | `f977b8903a5a`  |
| 1156   | No file              | `f977b8903a5a`  |
| 1149   | No file              | `f977b8903a5a`  |
| 1144   | No file              | `f977b8903a5a`  |
| 1137   | No file              | `f977b8903a5a`  |
| 1132   | No file              | `f977b8903a5a`  |
| 1127   | No file              | `f977b8903a5a`  |
| 1122   | No file              | `f977b8903a5a`  |
| 1118   | No file              | `f977b8903a5a`  |
| 1114   | No file              | `f977b8903a5a`  |
| 1109   | No file              | `f977b8903a5a`  |
| 1102   | No file              | `f977b8903a5a`  |
| 1096   | No file              | `f977b8903a5a`  |
| 1088   | No file              | `f977b8903a5a`  |
| 1081   | No file              | `f977b8903a5a`  |
| 1076   | No file              | `f977b8903a5a`  |
| 1069   | No file              | `f977b8903a5a`  |
| 1064   | No file              | `f977b8903a5a`  |
| 1058   | No file              | `f977b8903a5a`  |
| 1051   | No file              | `f977b8903a5a`  |
| 1044   | No file              | `f977b8903a5a`  |
| 1036   | No file              | `f977b8903a5a`  |
| 1026   | No file              | `f977b8903a5a`  |
| 1016   | No file              | `f977b8903a5a`  |
| 1009   | No file              | `f977b8903a5a`  |
| 1005   | No file              | `f977b8903a5a`  |
| 1000   | No file              | `f977b8903a5a`  |
| 998    | No file              | `f977b8903a5a`  |
| 990    | No file              | `f977b8903a5a`  |
| 979    | No file              | `f977b8903a5a`  |
| 972    | No file              | `f977b8903a5a`  |
| 963    | No file              | `f977b8903a5a`  |
| 955    | No file              | `f977b8903a5a`  |
| 946    | No file              | `f977b8903a5a`  |
| 938    | No file              | `f977b8903a5a`  |
| 927    | No file              | `f977b8903a5a`  |
| 911    | No file              | `f977b8903a5a`  |
| 904    | No file              | `f977b8903a5a`  |
| 899    | No file              | `f977b8903a5a`  |
| 894    | No file              | `f977b8903a5a`  |
| 885    | No file              | `f977b8903a5a`  |
| 879    | No file              | `f977b8903a5a`  |
| 872    | No file              | `f977b8903a5a`  |
| 864    | No file              | `f977b8903a5a`  |
| 855    | No file              | `f977b8903a5a`  |
| 853    | No file              | `f977b8903a5a`  |
| 845    | No file              | `f977b8903a5a`  |
| 837    | No file              | `f977b8903a5a`  |
| 829    | No file              | `f977b8903a5a`  |
| 822    | No file              | `f977b8903a5a`  |
| 814    | No file              | `f977b8903a5a`  |
| 805    | No file              | `f977b8903a5a`  |
| 794    | No file              | `f977b8903a5a`  |
| 787    | No file              | `f977b8903a5a`  |
| 780    | No file              | `f977b8903a5a`  |
| 771    | No file              | `f977b8903a5a`  |
| 760    | No file              | `f977b8903a5a`  |
| 748    | No file              | `f977b8903a5a`  |
| 741    | No file              | `f977b8903a5a`  |
| 736    | No file              | `f977b8903a5a`  |
| 731    | No file              | `f977b8903a5a`  |
| 723    | No file              | `f977b8903a5a`  |
| 711    | No file              | `f977b8903a5a`  |
| 707    | No file              | `f977b8903a5a`  |
| 697    | No file              | `f977b8903a5a`  |
| 689    | No file              | `f977b8903a5a`  |
| 683    | No file              | `f977b8903a5a`  |
| 678    | No file              | `f977b8903a5a`  |
| 670    | No file              | `f977b8903a5a`  |
| 661    | No file              | `f977b8903a5a`  |
| 656    | No file              | `f977b8903a5a`  |
| 652    | No file              | `f977b8903a5a`  |
| 643    | No file              | `f977b8903a5a`  |
| 637    | No file              | `f977b8903a5a`  |
| 630    | No file              | `f977b8903a5a`  |
| 627    | No file              | `f977b8903a5a`  |
| 621    | No file              | `f977b8903a5a`  |
| 617    | No file              | `f977b8903a5a`  |
| 615    | No file              | `f977b8903a5a`  |
| 606    | No file              | `f977b8903a5a`  |
| 599    | No file              | `f977b8903a5a`  |
| 592    | No file              | `f977b8903a5a`  |
| 586    | No file              | `f977b8903a5a`  |
| 577    | No file              | `f977b8903a5a`  |
| 569    | No file              | `f977b8903a5a`  |
| 561    | No file              | `f977b8903a5a`  |
| 554    | No file              | `f977b8903a5a`  |
| 542    | No file              | `f977b8903a5a`  |
| 532    | No file              | `f977b8903a5a`  |
| 531    | No file              | `f977b8903a5a`  |
| 526    | No file              | `f977b8903a5a`  |
| 521    | No file              | `f977b8903a5a`  |
| 517    | No file              | `f977b8903a5a`  |
| 510    | No file              | `f977b8903a5a`  |
| 508    | No file              | `f977b8903a5a`  |
| 504    | No file              | `f977b8903a5a`  |
| 497    | No file              | `f977b8903a5a`  |
| 491    | No file              | `f977b8903a5a`  |
| 485    | No file              | `f977b8903a5a`  |
| 478    | No file              | `f977b8903a5a`  |
| 472    | No file              | `f977b8903a5a`  |
| 466    | No file              | `f977b8903a5a`  |
| 457    | No file              | `f977b8903a5a`  |
| 452    | No file              | `f977b8903a5a`  |
| 449    | No file              | `f977b8903a5a`  |
| 435    | No file              | `f977b8903a5a`  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                      |
| ------------------------------- | -------- | --------------------------------------------------------- |
| `itemexchangebynpcoffset.dbss`  | Optional | `item_exchange_key -> (data_offset, data_size)` index; the rows are fixed size and can be walked without it |
| `displayexchangeitemnpc.dbss`   | Optional | The NPC dialogs that list each exchange key, for the NPC names |
| `languagedata_en.loc`           | Optional | Need and result item names (type `0`) and NPC names (type `6`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                       |
| ------- | ---------- | ----- | ------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `209` on client 3474        |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (28 bytes)

| Offset  | Type | Field                 | Notes                                                        |
| ------- | ---- | --------------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | item_exchange_key     | The key `displayexchangeitemnpc.dbss` lists; unique per row   |
| `+0x02` | u16  | item_exchange_key_dup | Equal to `item_exchange_key` in every row; the offset index points here |
| `+0x04` | u32  | need_item_key         | Item paid, an item enchant key (`enchant_level << 24 \| item_id`); level `0` on every row of clients 1784 and 3474 |
| `+0x08` | i64  | need_item_count       | Count of the need item; `1` to `600` (client 3474)            |
| `+0x10` | u32  | result_item_key       | Item received, packed as `need_item_key`; level `0` on every row of clients 1784 and 3474 |
| `+0x14` | i64  | result_item_count     | Count of the result item; `1` on every row but key `193` (`5`, client 3474) |

The rows are not sorted by key.

### `itemexchangebynpcoffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `itemexchangebynpc.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (10 bytes)

| Offset  | Type | Field             | Notes                                                  |
| ------- | ---- | ----------------- | ------------------------------------------------------ |
| `+0x00` | u16  | item_exchange_key | Key of the row                                         |
| `+0x02` | u32  | data_offset       | Row start + 2, at `item_exchange_key_dup`              |
| `+0x06` | u32  | data_size         | `26`, the row size - 2                                 |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Field Names

The 26 bytes from `+0x02` are the 2016 `gc::ItemExchangeByNpcStaticStatus`
packed without padding: `_itemExchangeByNpcKey` (u16 `gc::KeyType`),
`_needItemEnchantKey` (`gc::ItemEnchantKey`), `_needItemCount` (`__int64`),
`_toItemEnchantKey` (`gc::ItemEnchantKey`) and `_toItemCount` (`__int64`).
The struct's two `gc::ItemEnchantStaticStatus` pointers are not in the file.
The file writes the key once more in front of each row as the index key.

The values match the `ItemExchangeByNpc_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `Index`, and the `ItemExchangeByNpc_Table`
of a private server on client 519 by `Index`:

| Field             | Column              | Same value (client 1784 sheet, 1784 file) | Same value (client 1784 sheet, 3474 file) | Same value (client 519 table, 3474 file) |
| ----------------- | ------------------- | ----------------------------------------- | ----------------------------------------- | ---------------------------------------- |
| item_exchange_key | `Index`             | 222 of 222 rows                           | 209 of 209 rows                           | 207 of 209 rows                          |
| need_item_key     | `Itemkey`           | 222 of 222                                | 209 of 209                                | 207 of 207                               |
| need_item_count   | `ItemCount`         | 222 of 222                                | 209 of 209                                | 207 of 207                               |
| result_item_key   | `ExchangeItemKey`   | 222 of 222                                | 209 of 209                                | 207 of 207                               |
| result_item_count | `ExchangeItemCount` | 222 of 222                                | 209 of 209                                | 207 of 207                               |

The client 519 table has no row for two of the 209 keys of client 3474.

## Notes

- The exchange window Lua (`panel_dialog_exchange_item.luac`) takes each
  row through `getItemExchangeByNpcStaticStatusWrapperAtIndex()` of the
  open dialog's `displayexchangeitemnpc.dbss` row and shows
  `getNeedItemStaticStatusWrapper()` with `getNeedItemCount_s64()` and
  `getToItemStaticStatusWrapper()` with `getToItemCount_s64()`. The worker
  hire window (`panel_dialog_employee_hireitem_all_1.luac`) walks the same
  list and reads only the need item and its count.
- On client 3474 the 209 keys run from `4` to `261`, with 33 distinct need
  items and 175 distinct result items. The most used need items are Horse
  Race Seal (`1001`, 31 rows), Football (`16220`, 25), Shining Medal of
  Honor (`44388`, 22) and Gold Bar 100G (`4`, 18). Key `193` trades one
  [Event] Pet Seal (`16639`) for five Kanpacho's Chewable Tablet (`17728`).
- On client 3474 no `displayexchangeitemnpc.dbss` row lists keys `51`,
  `52`, `53`, `54` and `179`. The keys it lists that have no row here are
  in the [`displayexchangeitemnpc.dbss`](displayexchangeitemnpc_dbss.md)
  Notes.
