# `siegeobjectkindlistcache.bss` Format

## Purpose

The siege object kinds and one building character for each: rows of a u8
object kind and a `characterstatic.dbss` character key. On client 3482 the
14 rows are the Node War and Conquest War buildings a guild can install,
from the Barricade (kind `3`) to the Ballista Workshop (kind `29`). The
installation mode's war information window lists one line per row.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                           | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------------ | ----- | ------- | --------- |
| 1      | 1118 and later | `siegeobjectkindlistcache.bss` | 62    | 14 Row  | 3         |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `siegeobjectkindlistcache.bss` | 62 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c306d825a1c2`  |
| 3482   | Layout 1 | `c306d825a1c2`  |
| 3474   | Layout 1 | `c306d825a1c2`  |
| 3473   | Layout 1 | `c306d825a1c2`  |
| 3464   | Layout 1 | `c306d825a1c2`  |
| 3458   | Layout 1 | `c306d825a1c2`  |
| 3454   | Layout 1 | `c306d825a1c2`  |
| 3444   | Layout 1 | `c306d825a1c2`  |
| 3435   | Layout 1 | `c306d825a1c2`  |
| 3426   | Layout 1 | `c306d825a1c2`  |
| 3418   | Layout 1 | `c306d825a1c2`  |
| 3412   | Layout 1 | `c306d825a1c2`  |
| 3402   | Layout 1 | `c306d825a1c2`  |
| 3396   | Layout 1 | `c306d825a1c2`  |
| 3387   | Layout 1 | `c306d825a1c2`  |
| 3381   | Layout 1 | `c306d825a1c2`  |
| 3373   | Layout 1 | `c306d825a1c2`  |
| 3364   | Layout 1 | `c306d825a1c2`  |
| 3356   | Layout 1 | `c306d825a1c2`  |
| 3349   | Layout 1 | `c306d825a1c2`  |
| 3342   | Layout 1 | `c306d825a1c2`  |
| 3335   | Layout 1 | `c306d825a1c2`  |
| 3326   | Layout 1 | `c306d825a1c2`  |
| 3321   | Layout 1 | `c306d825a1c2`  |
| 3314   | Layout 1 | `c306d825a1c2`  |
| 3303   | Layout 1 | `c306d825a1c2`  |
| 3302   | Layout 1 | `c306d825a1c2`  |
| 3293   | Layout 1 | `c306d825a1c2`  |
| 3283   | Layout 1 | `c306d825a1c2`  |
| 3275   | Layout 1 | `c306d825a1c2`  |
| 3267   | Layout 1 | `c306d825a1c2`  |
| 3258   | Layout 1 | `c306d825a1c2`  |
| 3251   | Layout 1 | `c306d825a1c2`  |
| 3242   | Layout 1 | `c306d825a1c2`  |
| 3235   | Layout 1 | `c306d825a1c2`  |
| 3229   | Layout 1 | `c306d825a1c2`  |
| 3212   | Layout 1 | `c306d825a1c2`  |
| 3203   | Layout 1 | `c306d825a1c2`  |
| 3193   | Layout 1 | `c306d825a1c2`  |
| 3186   | Layout 1 | `c306d825a1c2`  |
| 3177   | Layout 1 | `c306d825a1c2`  |
| 3169   | Layout 1 | `c306d825a1c2`  |
| 3158   | Layout 1 | `c306d825a1c2`  |
| 3151   | Layout 1 | `c306d825a1c2`  |
| 3144   | Layout 1 | `c306d825a1c2`  |
| 3133   | Layout 1 | `c306d825a1c2`  |
| 3125   | Layout 1 | `c306d825a1c2`  |
| 3118   | Layout 1 | `c306d825a1c2`  |
| 3111   | Layout 1 | `c306d825a1c2`  |
| 3103   | Layout 1 | `c306d825a1c2`  |
| 3095   | Layout 1 | `c306d825a1c2`  |
| 3086   | Layout 1 | `c306d825a1c2`  |
| 3072   | Layout 1 | `c306d825a1c2`  |
| 3062   | Layout 1 | `c306d825a1c2`  |
| 3052   | Layout 1 | `c306d825a1c2`  |
| 3045   | Layout 1 | `c306d825a1c2`  |
| 3037   | Layout 1 | `c306d825a1c2`  |
| 3030   | Layout 1 | `c306d825a1c2`  |
| 3021   | Layout 1 | `c306d825a1c2`  |
| 3012   | Layout 1 | `c306d825a1c2`  |
| 3002   | Layout 1 | `c306d825a1c2`  |
| 2995   | Layout 1 | `c306d825a1c2`  |
| 2987   | Layout 1 | `c306d825a1c2`  |
| 2978   | Layout 1 | `c306d825a1c2`  |
| 2970   | Layout 1 | `c306d825a1c2`  |
| 2959   | Layout 1 | `c306d825a1c2`  |
| 2951   | Layout 1 | `c306d825a1c2`  |
| 2942   | Layout 1 | `c306d825a1c2`  |
| 2935   | Layout 1 | `c306d825a1c2`  |
| 2932   | Layout 1 | `c306d825a1c2`  |
| 2923   | Layout 1 | `c306d825a1c2`  |
| 2919   | Layout 1 | `c306d825a1c2`  |
| 2907   | Layout 1 | `c306d825a1c2`  |
| 2900   | Layout 1 | `c306d825a1c2`  |
| 2891   | Layout 1 | `c306d825a1c2`  |
| 2882   | Layout 1 | `c306d825a1c2`  |
| 2872   | Layout 1 | `c306d825a1c2`  |
| 2863   | Layout 1 | `c306d825a1c2`  |
| 2855   | Layout 1 | `c306d825a1c2`  |
| 2849   | Layout 1 | `c306d825a1c2`  |
| 2844   | Layout 1 | `c306d825a1c2`  |
| 2834   | Layout 1 | `c306d825a1c2`  |
| 2825   | Layout 1 | `c306d825a1c2`  |
| 2819   | Layout 1 | `c306d825a1c2`  |
| 2811   | Layout 1 | `c306d825a1c2`  |
| 2803   | Layout 1 | `c306d825a1c2`  |
| 2794   | Layout 1 | `c306d825a1c2`  |
| 2783   | Layout 1 | `c306d825a1c2`  |
| 2774   | Layout 1 | `c306d825a1c2`  |
| 2765   | Layout 1 | `c306d825a1c2`  |
| 2756   | Layout 1 | `c306d825a1c2`  |
| 2750   | Layout 1 | `c306d825a1c2`  |
| 2743   | Layout 1 | `c306d825a1c2`  |
| 2736   | Layout 1 | `c306d825a1c2`  |
| 2726   | Layout 1 | `c306d825a1c2`  |
| 2717   | Layout 1 | `c306d825a1c2`  |
| 2709   | Layout 1 | `c306d825a1c2`  |
| 2703   | Layout 1 | `c306d825a1c2`  |
| 2695   | Layout 1 | `c306d825a1c2`  |
| 2684   | Layout 1 | `c306d825a1c2`  |
| 2672   | Layout 1 | `c306d825a1c2`  |
| 2665   | Layout 1 | `c306d825a1c2`  |
| 2657   | Layout 1 | `c306d825a1c2`  |
| 2649   | Layout 1 | `c306d825a1c2`  |
| 2644   | Layout 1 | `c306d825a1c2`  |
| 2637   | Layout 1 | `c306d825a1c2`  |
| 2629   | Layout 1 | `c306d825a1c2`  |
| 2619   | Layout 1 | `c306d825a1c2`  |
| 2612   | Layout 1 | `c306d825a1c2`  |
| 2606   | Layout 1 | `c306d825a1c2`  |
| 2602   | Layout 1 | `c306d825a1c2`  |
| 2601   | Layout 1 | `c306d825a1c2`  |
| 2592   | Layout 1 | `c306d825a1c2`  |
| 2583   | Layout 1 | `c306d825a1c2`  |
| 2575   | Layout 1 | `c306d825a1c2`  |
| 2567   | Layout 1 | `c306d825a1c2`  |
| 2560   | Layout 1 | `c306d825a1c2`  |
| 2553   | Layout 1 | `c306d825a1c2`  |
| 2545   | Layout 1 | `c306d825a1c2`  |
| 2538   | Layout 1 | `c306d825a1c2`  |
| 2529   | Layout 1 | `c306d825a1c2`  |
| 2519   | Layout 1 | `c306d825a1c2`  |
| 2513   | Layout 1 | `c306d825a1c2`  |
| 2510   | Layout 1 | `c306d825a1c2`  |
| 2507   | Layout 1 | `c306d825a1c2`  |
| 2503   | Layout 1 | `c306d825a1c2`  |
| 2498   | Layout 1 | `c306d825a1c2`  |
| 2492   | Layout 1 | `c306d825a1c2`  |
| 2487   | Layout 1 | `c306d825a1c2`  |
| 2480   | Layout 1 | `c306d825a1c2`  |
| 2474   | Layout 1 | `c306d825a1c2`  |
| 2468   | Layout 1 | `c306d825a1c2`  |
| 2460   | Layout 1 | `c306d825a1c2`  |
| 2453   | Layout 1 | `c306d825a1c2`  |
| 2444   | Layout 1 | `c306d825a1c2`  |
| 2438   | Layout 1 | `c306d825a1c2`  |
| 2434   | Layout 1 | `c306d825a1c2`  |
| 2429   | Layout 1 | `c306d825a1c2`  |
| 2421   | Layout 1 | `c306d825a1c2`  |
| 2414   | Layout 1 | `c306d825a1c2`  |
| 2407   | Layout 1 | `c306d825a1c2`  |
| 2401   | Layout 1 | `c306d825a1c2`  |
| 2397   | Layout 1 | `c306d825a1c2`  |
| 2393   | Layout 1 | `c306d825a1c2`  |
| 2384   | Layout 1 | `c306d825a1c2`  |
| 2378   | Layout 1 | `c306d825a1c2`  |
| 2372   | Layout 1 | `c306d825a1c2`  |
| 2358   | Layout 1 | `c306d825a1c2`  |
| 2352   | Layout 1 | `c306d825a1c2`  |
| 2347   | Layout 1 | `c306d825a1c2`  |
| 2343   | Layout 1 | `c306d825a1c2`  |
| 2335   | Layout 1 | `c306d825a1c2`  |
| 2327   | Layout 1 | `c306d825a1c2`  |
| 2324   | Layout 1 | `c306d825a1c2`  |
| 2319   | Layout 1 | `c306d825a1c2`  |
| 2313   | Layout 1 | `c306d825a1c2`  |
| 2308   | Layout 1 | `c306d825a1c2`  |
| 2302   | Layout 1 | `c306d825a1c2`  |
| 2295   | Layout 1 | `c306d825a1c2`  |
| 2290   | Layout 1 | `c306d825a1c2`  |
| 2284   | Layout 1 | `c306d825a1c2`  |
| 2276   | Layout 1 | `c306d825a1c2`  |
| 2269   | Layout 1 | `c306d825a1c2`  |
| 2259   | Layout 1 | `c306d825a1c2`  |
| 2250   | Layout 1 | `c306d825a1c2`  |
| 2243   | Layout 1 | `c306d825a1c2`  |
| 2235   | Layout 1 | `c306d825a1c2`  |
| 2229   | Layout 1 | `c306d825a1c2`  |
| 2224   | Layout 1 | `c306d825a1c2`  |
| 2218   | Layout 1 | `c306d825a1c2`  |
| 2215   | Layout 1 | `c306d825a1c2`  |
| 2207   | Layout 1 | `c306d825a1c2`  |
| 2203   | Layout 1 | `c306d825a1c2`  |
| 2196   | Layout 1 | `c306d825a1c2`  |
| 2192   | Layout 1 | `c306d825a1c2`  |
| 2189   | Layout 1 | `c306d825a1c2`  |
| 2183   | Layout 1 | `c306d825a1c2`  |
| 2179   | Layout 1 | `c306d825a1c2`  |
| 2171   | Layout 1 | `c306d825a1c2`  |
| 2163   | Layout 1 | `c306d825a1c2`  |
| 2156   | Layout 1 | `c306d825a1c2`  |
| 2151   | Layout 1 | `c306d825a1c2`  |
| 2147   | Layout 1 | `c306d825a1c2`  |
| 2142   | Layout 1 | `c306d825a1c2`  |
| 2138   | Layout 1 | `c306d825a1c2`  |
| 2134   | Layout 1 | `c306d825a1c2`  |
| 2130   | Layout 1 | `c306d825a1c2`  |
| 2122   | Layout 1 | `c306d825a1c2`  |
| 2107   | Layout 1 | `c306d825a1c2`  |
| 2098   | Layout 1 | `c306d825a1c2`  |
| 2089   | Layout 1 | `c306d825a1c2`  |
| 2081   | Layout 1 | `c306d825a1c2`  |
| 2073   | Layout 1 | `c306d825a1c2`  |
| 2067   | Layout 1 | `c306d825a1c2`  |
| 2063   | Layout 1 | `c306d825a1c2`  |
| 2059   | Layout 1 | `c306d825a1c2`  |
| 2052   | Layout 1 | `c306d825a1c2`  |
| 2044   | Layout 1 | `c306d825a1c2`  |
| 2039   | Layout 1 | `c306d825a1c2`  |
| 2032   | Layout 1 | `c306d825a1c2`  |
| 2025   | Layout 1 | `c306d825a1c2`  |
| 2011   | Layout 1 | `c306d825a1c2`  |
| 2005   | Layout 1 | `c306d825a1c2`  |
| 2000   | Layout 1 | `c306d825a1c2`  |
| 1996   | Layout 1 | `c306d825a1c2`  |
| 1991   | Layout 1 | `c306d825a1c2`  |
| 1985   | Layout 1 | `c306d825a1c2`  |
| 1980   | Layout 1 | `c306d825a1c2`  |
| 1969   | Layout 1 | `c306d825a1c2`  |
| 1964   | Layout 1 | `c306d825a1c2`  |
| 1958   | Layout 1 | `c306d825a1c2`  |
| 1950   | Layout 1 | `c306d825a1c2`  |
| 1945   | Layout 1 | `c306d825a1c2`  |
| 1937   | Layout 1 | `c306d825a1c2`  |
| 1933   | Layout 1 | `c306d825a1c2`  |
| 1927   | Layout 1 | `c306d825a1c2`  |
| 1921   | Layout 1 | `c306d825a1c2`  |
| 1914   | Layout 1 | `c306d825a1c2`  |
| 1908   | Layout 1 | `c306d825a1c2`  |
| 1897   | Layout 1 | `c306d825a1c2`  |
| 1892   | Layout 1 | `c306d825a1c2`  |
| 1886   | Layout 1 | `c306d825a1c2`  |
| 1881   | Layout 1 | `c306d825a1c2`  |
| 1871   | Layout 1 | `c306d825a1c2`  |
| 1866   | Layout 1 | `c306d825a1c2`  |
| 1862   | Layout 1 | `c306d825a1c2`  |
| 1854   | Layout 1 | `c306d825a1c2`  |
| 1846   | Layout 1 | `c306d825a1c2`  |
| 1838   | Layout 1 | `c306d825a1c2`  |
| 1832   | Layout 1 | `c306d825a1c2`  |
| 1826   | Layout 1 | `c306d825a1c2`  |
| 1822   | Layout 1 | `c306d825a1c2`  |
| 1818   | Layout 1 | `c306d825a1c2`  |
| 1804   | Layout 1 | `c306d825a1c2`  |
| 1794   | Layout 1 | `c306d825a1c2`  |
| 1790   | Layout 1 | `c306d825a1c2`  |
| 1784   | Layout 1 | `c306d825a1c2`  |
| 1774   | Layout 1 | `c306d825a1c2`  |
| 1771   | Layout 1 | `c306d825a1c2`  |
| 1762   | Layout 1 | `c306d825a1c2`  |
| 1759   | Layout 1 | `c306d825a1c2`  |
| 1754   | Layout 1 | `c306d825a1c2`  |
| 1749   | Layout 1 | `c306d825a1c2`  |
| 1743   | Layout 1 | `c306d825a1c2`  |
| 1737   | Layout 1 | `c306d825a1c2`  |
| 1731   | Layout 1 | `c306d825a1c2`  |
| 1725   | Layout 1 | `c306d825a1c2`  |
| 1717   | Layout 1 | `c306d825a1c2`  |
| 1710   | Layout 1 | `c306d825a1c2`  |
| 1704   | Layout 1 | `c306d825a1c2`  |
| 1698   | Layout 1 | `c306d825a1c2`  |
| 1690   | Layout 1 | `c306d825a1c2`  |
| 1685   | Layout 1 | `c306d825a1c2`  |
| 1680   | Layout 1 | `c306d825a1c2`  |
| 1674   | Layout 1 | `c306d825a1c2`  |
| 1668   | Layout 1 | `c306d825a1c2`  |
| 1659   | Layout 1 | `c306d825a1c2`  |
| 1649   | Layout 1 | `c306d825a1c2`  |
| 1642   | Layout 1 | `c306d825a1c2`  |
| 1636   | Layout 1 | `c306d825a1c2`  |
| 1628   | Layout 1 | `c306d825a1c2`  |
| 1622   | Layout 1 | `c306d825a1c2`  |
| 1614   | Layout 1 | `c306d825a1c2`  |
| 1608   | Layout 1 | `c306d825a1c2`  |
| 1602   | Layout 1 | `c306d825a1c2`  |
| 1598   | Layout 1 | `c306d825a1c2`  |
| 1594   | Layout 1 | `c306d825a1c2`  |
| 1590   | Layout 1 | `c306d825a1c2`  |
| 1587   | Layout 1 | `c306d825a1c2`  |
| 1584   | Layout 1 | `c306d825a1c2`  |
| 1579   | Layout 1 | `c306d825a1c2`  |
| 1572   | Layout 1 | `c306d825a1c2`  |
| 1565   | Layout 1 | `c306d825a1c2`  |
| 1559   | Layout 1 | `c306d825a1c2`  |
| 1554   | Layout 1 | `c306d825a1c2`  |
| 1547   | Layout 1 | `c306d825a1c2`  |
| 1537   | Layout 1 | `c306d825a1c2`  |
| 1529   | Layout 1 | `c306d825a1c2`  |
| 1524   | Layout 1 | `c306d825a1c2`  |
| 1519   | Layout 1 | `c306d825a1c2`  |
| 1509   | Layout 1 | `c306d825a1c2`  |
| 1506   | Layout 1 | `c306d825a1c2`  |
| 1504   | Layout 1 | `c306d825a1c2`  |
| 1500   | Layout 1 | `c306d825a1c2`  |
| 1493   | Layout 1 | `c306d825a1c2`  |
| 1489   | Layout 1 | `c306d825a1c2`  |
| 1485   | Layout 1 | `c306d825a1c2`  |
| 1481   | Layout 1 | `c306d825a1c2`  |
| 1474   | Layout 1 | `c306d825a1c2`  |
| 1466   | Layout 1 | `c306d825a1c2`  |
| 1462   | Layout 1 | `c306d825a1c2`  |
| 1459   | Layout 1 | `c306d825a1c2`  |
| 1453   | Layout 1 | `c306d825a1c2`  |
| 1450   | Layout 1 | `c306d825a1c2`  |
| 1445   | Layout 1 | `c306d825a1c2`  |
| 1439   | Layout 1 | `c306d825a1c2`  |
| 1433   | Layout 1 | `c306d825a1c2`  |
| 1430   | Layout 1 | `c306d825a1c2`  |
| 1426   | Layout 1 | `c306d825a1c2`  |
| 1421   | Layout 1 | `c306d825a1c2`  |
| 1417   | Layout 1 | `c306d825a1c2`  |
| 1416   | Layout 1 | `c306d825a1c2`  |
| 1409   | Layout 1 | `c306d825a1c2`  |
| 1405   | Layout 1 | `c306d825a1c2`  |
| 1401   | Layout 1 | `c306d825a1c2`  |
| 1396   | Layout 1 | `c306d825a1c2`  |
| 1391   | Layout 1 | `c306d825a1c2`  |
| 1390   | Layout 1 | `c306d825a1c2`  |
| 1386   | Layout 1 | `c306d825a1c2`  |
| 1381   | Layout 1 | `c306d825a1c2`  |
| 1379   | Layout 1 | `c306d825a1c2`  |
| 1372   | Layout 1 | `c306d825a1c2`  |
| 1366   | Layout 1 | `c306d825a1c2`  |
| 1364   | Layout 1 | `c306d825a1c2`  |
| 1363   | Layout 1 | `c306d825a1c2`  |
| 1360   | Layout 1 | `c306d825a1c2`  |
| 1358   | Layout 1 | `c306d825a1c2`  |
| 1355   | Layout 1 | `c306d825a1c2`  |
| 1351   | Layout 1 | `c306d825a1c2`  |
| 1348   | Layout 1 | `c306d825a1c2`  |
| 1346   | Layout 1 | `c306d825a1c2`  |
| 1341   | Layout 1 | `c306d825a1c2`  |
| 1340   | Layout 1 | `c306d825a1c2`  |
| 1338   | Layout 1 | `c306d825a1c2`  |
| 1335   | Layout 1 | `c306d825a1c2`  |
| 1333   | Layout 1 | `c306d825a1c2`  |
| 1329   | Layout 1 | `c306d825a1c2`  |
| 1327   | Layout 1 | `c306d825a1c2`  |
| 1324   | Layout 1 | `c306d825a1c2`  |
| 1321   | Layout 1 | `c306d825a1c2`  |
| 1319   | Layout 1 | `c306d825a1c2`  |
| 1318   | Layout 1 | `c306d825a1c2`  |
| 1316   | Layout 1 | `c306d825a1c2`  |
| 1313   | Layout 1 | `c306d825a1c2`  |
| 1311   | Layout 1 | `c306d825a1c2`  |
| 1309   | Layout 1 | `c306d825a1c2`  |
| 1304   | Layout 1 | `c306d825a1c2`  |
| 1292   | Layout 1 | `c306d825a1c2`  |
| 1286   | Layout 1 | `c306d825a1c2`  |
| 1280   | Layout 1 | `c306d825a1c2`  |
| 1276   | Layout 1 | `c306d825a1c2`  |
| 1267   | Layout 1 | `c306d825a1c2`  |
| 1261   | Layout 1 | `c306d825a1c2`  |
| 1256   | Layout 1 | `c306d825a1c2`  |
| 1250   | Layout 1 | `c306d825a1c2`  |
| 1246   | Layout 1 | `c306d825a1c2`  |
| 1239   | Layout 1 | `c306d825a1c2`  |
| 1230   | Layout 1 | `c306d825a1c2`  |
| 1226   | Layout 1 | `c306d825a1c2`  |
| 1220   | Layout 1 | `c306d825a1c2`  |
| 1217   | Layout 1 | `c306d825a1c2`  |
| 1211   | Layout 1 | `c306d825a1c2`  |
| 1210   | Layout 1 | `c306d825a1c2`  |
| 1208   | Layout 1 | `c306d825a1c2`  |
| 1203   | Layout 1 | `c306d825a1c2`  |
| 1197   | Layout 1 | `c306d825a1c2`  |
| 1194   | Layout 1 | `c306d825a1c2`  |
| 1192   | Layout 1 | `c306d825a1c2`  |
| 1187   | Layout 1 | `c306d825a1c2`  |
| 1183   | Layout 1 | `c306d825a1c2`  |
| 1177   | Layout 1 | `c306d825a1c2`  |
| 1173   | Layout 1 | `c306d825a1c2`  |
| 1167   | Layout 1 | `c306d825a1c2`  |
| 1164   | Layout 1 | `c306d825a1c2`  |
| 1156   | Layout 1 | `c306d825a1c2`  |
| 1149   | Layout 1 | `c306d825a1c2`  |
| 1144   | Layout 1 | `c306d825a1c2`  |
| 1137   | Layout 1 | `c306d825a1c2`  |
| 1132   | Layout 1 | `c306d825a1c2`  |
| 1127   | Layout 1 | `c306d825a1c2`  |
| 1122   | Layout 1 | `c306d825a1c2`  |
| 1118   | Layout 1 | `c306d825a1c2`  |
| 1114   | No file  | `c306d825a1c2`  |
| 1109   | No file  | `c306d825a1c2`  |
| 1102   | No file  | `c306d825a1c2`  |
| 1096   | No file  | `c306d825a1c2`  |
| 1088   | No file  | `c306d825a1c2`  |
| 1081   | No file  | `c306d825a1c2`  |
| 1076   | No file  | `c306d825a1c2`  |
| 1069   | No file  | `c306d825a1c2`  |
| 1064   | No file  | `c306d825a1c2`  |
| 1058   | No file  | `c306d825a1c2`  |
| 1051   | No file  | `c306d825a1c2`  |
| 1044   | No file  | `c306d825a1c2`  |
| 1036   | No file  | `c306d825a1c2`  |
| 1026   | No file  | `c306d825a1c2`  |
| 1016   | No file  | `c306d825a1c2`  |
| 1009   | No file  | `c306d825a1c2`  |
| 1005   | No file  | `c306d825a1c2`  |
| 1000   | No file  | `c306d825a1c2`  |
| 998    | No file  | `c306d825a1c2`  |
| 990    | No file  | `c306d825a1c2`  |
| 979    | No file  | `c306d825a1c2`  |
| 972    | No file  | `c306d825a1c2`  |
| 963    | No file  | `c306d825a1c2`  |
| 955    | No file  | `c306d825a1c2`  |
| 946    | No file  | `c306d825a1c2`  |
| 938    | No file  | `c306d825a1c2`  |
| 927    | No file  | `c306d825a1c2`  |
| 911    | No file  | `c306d825a1c2`  |
| 904    | No file  | `c306d825a1c2`  |
| 899    | No file  | `c306d825a1c2`  |
| 894    | No file  | `c306d825a1c2`  |
| 885    | No file  | `c306d825a1c2`  |
| 879    | No file  | `c306d825a1c2`  |
| 872    | No file  | `c306d825a1c2`  |
| 864    | No file  | `c306d825a1c2`  |
| 855    | No file  | `c306d825a1c2`  |
| 853    | No file  | `c306d825a1c2`  |
| 845    | No file  | `c306d825a1c2`  |
| 837    | No file  | `c306d825a1c2`  |
| 829    | No file  | `c306d825a1c2`  |
| 822    | No file  | `c306d825a1c2`  |
| 814    | No file  | `c306d825a1c2`  |
| 805    | No file  | `c306d825a1c2`  |
| 794    | No file  | `c306d825a1c2`  |
| 787    | No file  | `c306d825a1c2`  |
| 780    | No file  | `c306d825a1c2`  |
| 771    | No file  | `c306d825a1c2`  |
| 760    | No file  | `c306d825a1c2`  |
| 748    | No file  | `c306d825a1c2`  |
| 741    | No file  | `c306d825a1c2`  |
| 736    | No file  | `c306d825a1c2`  |
| 731    | No file  | `c306d825a1c2`  |
| 723    | No file  | `c306d825a1c2`  |
| 711    | No file  | `c306d825a1c2`  |
| 707    | No file  | `c306d825a1c2`  |
| 697    | No file  | `c306d825a1c2`  |
| 689    | No file  | `c306d825a1c2`  |
| 683    | No file  | `c306d825a1c2`  |
| 678    | No file  | `c306d825a1c2`  |
| 670    | No file  | `c306d825a1c2`  |
| 661    | No file  | `c306d825a1c2`  |
| 656    | No file  | `c306d825a1c2`  |
| 652    | No file  | `c306d825a1c2`  |
| 643    | No file  | `c306d825a1c2`  |
| 637    | No file  | `c306d825a1c2`  |
| 630    | No file  | `c306d825a1c2`  |
| 627    | No file  | `c306d825a1c2`  |
| 621    | No file  | `c306d825a1c2`  |
| 617    | No file  | `c306d825a1c2`  |
| 615    | No file  | `c306d825a1c2`  |
| 606    | No file  | `c306d825a1c2`  |
| 599    | No file  | `c306d825a1c2`  |
| 592    | No file  | `c306d825a1c2`  |
| 586    | No file  | `c306d825a1c2`  |
| 577    | No file  | `c306d825a1c2`  |
| 569    | No file  | `c306d825a1c2`  |
| 561    | No file  | `c306d825a1c2`  |
| 554    | No file  | `c306d825a1c2`  |
| 542    | No file  | `c306d825a1c2`  |
| 532    | No file  | `c306d825a1c2`  |
| 531    | No file  | `c306d825a1c2`  |
| 526    | No file  | `c306d825a1c2`  |
| 521    | No file  | `c306d825a1c2`  |
| 517    | No file  | `c306d825a1c2`  |
| 510    | No file  | `c306d825a1c2`  |
| 508    | No file  | `c306d825a1c2`  |
| 504    | No file  | `c306d825a1c2`  |
| 497    | No file  | `c306d825a1c2`  |
| 491    | No file  | `c306d825a1c2`  |
| 485    | No file  | `c306d825a1c2`  |
| 478    | No file  | `c306d825a1c2`  |
| 472    | No file  | `c306d825a1c2`  |
| 466    | No file  | `c306d825a1c2`  |
| 457    | No file  | `c306d825a1c2`  |
| 452    | No file  | `c306d825a1c2`  |
| 449    | No file  | `c306d825a1c2`  |
| 435    | No file  | `c306d825a1c2`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (3 bytes)

| Offset  | Type | Field         | Notes                                                              |
| ------- | ---- | ------------- | ------------------------------------------------------------------ |
| `+0x00` | u8   | object_kind   | Siege object kind; unique per row, see Object Kinds                |
| `+0x01` | u16  | character_key | `characterstatic.dbss` key of a building of that kind              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Object Kinds

The rows of client 3482 in file order, with the LOC type 6 name of the
character, and the character key the same kind has on client 1784.

| `object_kind` | `character_key` (client 3482) | Name                       | `character_key` (client 1784) |
| ------------- | ----------------------------- | -------------------------- | ----------------------------- |
| 19            | 12837                         | Supply Depot               | 12650                         |
| 3             | 12605                         | Barricade                  | 12605                         |
| 21            | 2046                          | Wooden Fence               | 2046                          |
| 18            | 12835                         | Enhanced Flame Tower       | 12642                         |
| 26            | 12839                         | Indomitable Flag Factory   | 12660                         |
| 12            | 12832                         | Elephant Nursery           | 12629                         |
| 20            | 12838                         | Wooden Fence Gate          | 12655                         |
| 17            | 12836                         | Big Hwacha                 | 12645                         |
| 11            | 12808                         | Cannon Observatory         | 12623                         |
| 10            | 12807                         | Recovery Center            | 12619                         |
| 24            | 12804                         | Large Siege Tower Factory  | 2050                          |
| 23            | 12803                         | Medium Siege Tower Factory | 2049                          |
| 22            | 12802                         | Defense Tower              | 2047                          |
| 29            | 12800                         | Ballista Workshop          | 2070                          |

## Field Names

The `SiegeObjectType_Name` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `ObjectKind` and `RepCharacterIndex` (the
representative character) and two rows, `3, 12605` and `21, 2046`; both
are rows of the client 1784 file (2 of 2). The other 12 rows are not in
any sheet: that server's dump (client 1784) has the error text
`CharacterStaticStatusManager::readFromBinary() siegeObjectKindListCache
Open Failed.`, so the file is read with the character table, as a cache
of one character per object kind.

The client Lua of client 3482 reads the rows with
`ToClient_getSiegeObjectKindCount()` and
`ToClient_getObjectStaticStatusByObjectKindbyIndex(index)`
(`panel_house_installationmode_warinfomation_all_1.luac`), which returns
the row's character; the window skips characters with
`isRoseWarSpawnCharacter()`.

## Notes

- Clients 1784 and 3482 hold the same 14 kinds in another order. The
  character of 12 kinds changed between them; the Barricade and the
  Wooden Fence kept theirs.
- The kinds overlap the `Type` column of the `SiegeObjectTotalLimit` sheet
  on client 1784 (`3`, `10`, `11`, `12`, `17`, `18`, `19`, `20`, `26`).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  the object kind, then the character key with its name.

## Open Questions

### Object Kind Names

The server dump of client 1784 holds 24 `SiegeObjectType_*` names
(`SiegeObjectType_Baricade`, `SiegeObjectType_BaricadeDoor`, ...,
`SiegeObjectType_PlayerUpgradeBuilding`) but not their values, the 2016
PDB has no `SiegeObjectType` enum, and the client Lua of client 3482 has
no `__eSiegeObjectType` constant. Which name belongs to which kind number
is open, so the preview shows the number and the character name.
