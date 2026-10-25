# `abyssmovecost.bss` Format

## Purpose

Move costs between pairs of regions for the Magnus (`AbyssOne`): one row
per region, each a list of the same set of other regions with a u64 cost.
On client 3482 the table is 16 rows of 16 moves; every cost is `5000000`
except one `0` per row, where the two regions are near each other
(Bartali Farm and Velia, Erethea's Belt and Zvier Highlands). The
file has no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes | Records          | Row bytes |
| ------ | -------------- | ------------------- | ----- | ---------------- | --------- |
| 1      | 2011 and later | `abyssmovecost.bss` | 3,140 | 256 Move, 16 Row | 12        |

| Layout | File                | Known            | Unknown    |
| ------ | ------------------- | ---------------- | ---------- |
| 1      | `abyssmovecost.bss` | 3,140 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `11e83c1f9364`  |
| 3482   | Layout 1 | `11e83c1f9364`  |
| 3474   | Layout 1 | `11e83c1f9364`  |
| 3473   | Layout 1 | `11e83c1f9364`  |
| 3464   | Layout 1 | `11e83c1f9364`  |
| 3458   | Layout 1 | `11e83c1f9364`  |
| 3454   | Layout 1 | `11e83c1f9364`  |
| 3444   | Layout 1 | `11e83c1f9364`  |
| 3435   | Layout 1 | `11e83c1f9364`  |
| 3426   | Layout 1 | `11e83c1f9364`  |
| 3418   | Layout 1 | `11e83c1f9364`  |
| 3412   | Layout 1 | `11e83c1f9364`  |
| 3402   | Layout 1 | `11e83c1f9364`  |
| 3396   | Layout 1 | `11e83c1f9364`  |
| 3387   | Layout 1 | `11e83c1f9364`  |
| 3381   | Layout 1 | `11e83c1f9364`  |
| 3373   | Layout 1 | `11e83c1f9364`  |
| 3364   | Layout 1 | `11e83c1f9364`  |
| 3356   | Layout 1 | `11e83c1f9364`  |
| 3349   | Layout 1 | `11e83c1f9364`  |
| 3342   | Layout 1 | `11e83c1f9364`  |
| 3335   | Layout 1 | `11e83c1f9364`  |
| 3326   | Layout 1 | `11e83c1f9364`  |
| 3321   | Layout 1 | `11e83c1f9364`  |
| 3314   | Layout 1 | `11e83c1f9364`  |
| 3303   | Layout 1 | `11e83c1f9364`  |
| 3302   | Layout 1 | `11e83c1f9364`  |
| 3293   | Layout 1 | `11e83c1f9364`  |
| 3283   | Layout 1 | `11e83c1f9364`  |
| 3275   | Layout 1 | `11e83c1f9364`  |
| 3267   | Layout 1 | `11e83c1f9364`  |
| 3258   | Layout 1 | `11e83c1f9364`  |
| 3251   | Layout 1 | `11e83c1f9364`  |
| 3242   | Layout 1 | `11e83c1f9364`  |
| 3235   | Layout 1 | `11e83c1f9364`  |
| 3229   | Layout 1 | `11e83c1f9364`  |
| 3212   | Layout 1 | `11e83c1f9364`  |
| 3203   | Layout 1 | `11e83c1f9364`  |
| 3193   | Layout 1 | `11e83c1f9364`  |
| 3186   | Layout 1 | `11e83c1f9364`  |
| 3177   | Layout 1 | `11e83c1f9364`  |
| 3169   | Layout 1 | `11e83c1f9364`  |
| 3158   | Layout 1 | `11e83c1f9364`  |
| 3151   | Layout 1 | `11e83c1f9364`  |
| 3144   | Layout 1 | `11e83c1f9364`  |
| 3133   | Layout 1 | `11e83c1f9364`  |
| 3125   | Layout 1 | `11e83c1f9364`  |
| 3118   | Layout 1 | `11e83c1f9364`  |
| 3111   | Layout 1 | `11e83c1f9364`  |
| 3103   | Layout 1 | `11e83c1f9364`  |
| 3095   | Layout 1 | `11e83c1f9364`  |
| 3086   | Layout 1 | `11e83c1f9364`  |
| 3072   | Layout 1 | `11e83c1f9364`  |
| 3062   | Layout 1 | `11e83c1f9364`  |
| 3052   | Layout 1 | `11e83c1f9364`  |
| 3045   | Layout 1 | `11e83c1f9364`  |
| 3037   | Layout 1 | `11e83c1f9364`  |
| 3030   | Layout 1 | `11e83c1f9364`  |
| 3021   | Layout 1 | `11e83c1f9364`  |
| 3012   | Layout 1 | `11e83c1f9364`  |
| 3002   | Layout 1 | `11e83c1f9364`  |
| 2995   | Layout 1 | `11e83c1f9364`  |
| 2987   | Layout 1 | `11e83c1f9364`  |
| 2978   | Layout 1 | `11e83c1f9364`  |
| 2970   | Layout 1 | `11e83c1f9364`  |
| 2959   | Layout 1 | `11e83c1f9364`  |
| 2951   | Layout 1 | `11e83c1f9364`  |
| 2942   | Layout 1 | `11e83c1f9364`  |
| 2935   | Layout 1 | `11e83c1f9364`  |
| 2932   | Layout 1 | `11e83c1f9364`  |
| 2923   | Layout 1 | `11e83c1f9364`  |
| 2919   | Layout 1 | `11e83c1f9364`  |
| 2907   | Layout 1 | `11e83c1f9364`  |
| 2900   | Layout 1 | `11e83c1f9364`  |
| 2891   | Layout 1 | `11e83c1f9364`  |
| 2882   | Layout 1 | `11e83c1f9364`  |
| 2872   | Layout 1 | `11e83c1f9364`  |
| 2863   | Layout 1 | `11e83c1f9364`  |
| 2855   | Layout 1 | `11e83c1f9364`  |
| 2849   | Layout 1 | `11e83c1f9364`  |
| 2844   | Layout 1 | `11e83c1f9364`  |
| 2834   | Layout 1 | `11e83c1f9364`  |
| 2825   | Layout 1 | `11e83c1f9364`  |
| 2819   | Layout 1 | `11e83c1f9364`  |
| 2811   | Layout 1 | `11e83c1f9364`  |
| 2803   | Layout 1 | `11e83c1f9364`  |
| 2794   | Layout 1 | `11e83c1f9364`  |
| 2783   | Layout 1 | `11e83c1f9364`  |
| 2774   | Layout 1 | `11e83c1f9364`  |
| 2765   | Layout 1 | `11e83c1f9364`  |
| 2756   | Layout 1 | `11e83c1f9364`  |
| 2750   | Layout 1 | `11e83c1f9364`  |
| 2743   | Layout 1 | `11e83c1f9364`  |
| 2736   | Layout 1 | `11e83c1f9364`  |
| 2726   | Layout 1 | `11e83c1f9364`  |
| 2717   | Layout 1 | `11e83c1f9364`  |
| 2709   | Layout 1 | `11e83c1f9364`  |
| 2703   | Layout 1 | `11e83c1f9364`  |
| 2695   | Layout 1 | `11e83c1f9364`  |
| 2684   | Layout 1 | `11e83c1f9364`  |
| 2672   | Layout 1 | `11e83c1f9364`  |
| 2665   | Layout 1 | `11e83c1f9364`  |
| 2657   | Layout 1 | `11e83c1f9364`  |
| 2649   | Layout 1 | `11e83c1f9364`  |
| 2644   | Layout 1 | `11e83c1f9364`  |
| 2637   | Layout 1 | `11e83c1f9364`  |
| 2629   | Layout 1 | `11e83c1f9364`  |
| 2619   | Layout 1 | `11e83c1f9364`  |
| 2612   | Layout 1 | `11e83c1f9364`  |
| 2606   | Layout 1 | `11e83c1f9364`  |
| 2602   | Layout 1 | `11e83c1f9364`  |
| 2601   | Layout 1 | `11e83c1f9364`  |
| 2592   | Layout 1 | `11e83c1f9364`  |
| 2583   | Layout 1 | `11e83c1f9364`  |
| 2575   | Layout 1 | `11e83c1f9364`  |
| 2567   | Layout 1 | `11e83c1f9364`  |
| 2560   | Layout 1 | `11e83c1f9364`  |
| 2553   | Layout 1 | `11e83c1f9364`  |
| 2545   | Layout 1 | `11e83c1f9364`  |
| 2538   | Layout 1 | `11e83c1f9364`  |
| 2529   | Layout 1 | `11e83c1f9364`  |
| 2519   | Layout 1 | `11e83c1f9364`  |
| 2513   | Layout 1 | `11e83c1f9364`  |
| 2510   | Layout 1 | `11e83c1f9364`  |
| 2507   | Layout 1 | `11e83c1f9364`  |
| 2503   | Layout 1 | `11e83c1f9364`  |
| 2498   | Layout 1 | `11e83c1f9364`  |
| 2492   | Layout 1 | `11e83c1f9364`  |
| 2487   | Layout 1 | `11e83c1f9364`  |
| 2480   | Layout 1 | `11e83c1f9364`  |
| 2474   | Layout 1 | `11e83c1f9364`  |
| 2468   | Layout 1 | `11e83c1f9364`  |
| 2460   | Layout 1 | `11e83c1f9364`  |
| 2453   | Layout 1 | `11e83c1f9364`  |
| 2444   | Layout 1 | `11e83c1f9364`  |
| 2438   | Layout 1 | `11e83c1f9364`  |
| 2434   | Layout 1 | `11e83c1f9364`  |
| 2429   | Layout 1 | `11e83c1f9364`  |
| 2421   | Layout 1 | `11e83c1f9364`  |
| 2414   | Layout 1 | `11e83c1f9364`  |
| 2407   | Layout 1 | `11e83c1f9364`  |
| 2401   | Layout 1 | `11e83c1f9364`  |
| 2397   | Layout 1 | `11e83c1f9364`  |
| 2393   | Layout 1 | `11e83c1f9364`  |
| 2384   | Layout 1 | `11e83c1f9364`  |
| 2378   | Layout 1 | `11e83c1f9364`  |
| 2372   | Layout 1 | `11e83c1f9364`  |
| 2358   | Layout 1 | `11e83c1f9364`  |
| 2352   | Layout 1 | `11e83c1f9364`  |
| 2347   | Layout 1 | `11e83c1f9364`  |
| 2343   | Layout 1 | `11e83c1f9364`  |
| 2335   | Layout 1 | `11e83c1f9364`  |
| 2327   | Layout 1 | `11e83c1f9364`  |
| 2324   | Layout 1 | `11e83c1f9364`  |
| 2319   | Layout 1 | `11e83c1f9364`  |
| 2313   | Layout 1 | `11e83c1f9364`  |
| 2308   | Layout 1 | `11e83c1f9364`  |
| 2302   | Layout 1 | `11e83c1f9364`  |
| 2295   | Layout 1 | `11e83c1f9364`  |
| 2290   | Layout 1 | `11e83c1f9364`  |
| 2284   | Layout 1 | `11e83c1f9364`  |
| 2276   | Layout 1 | `11e83c1f9364`  |
| 2269   | Layout 1 | `11e83c1f9364`  |
| 2259   | Layout 1 | `11e83c1f9364`  |
| 2250   | Layout 1 | `11e83c1f9364`  |
| 2243   | Layout 1 | `11e83c1f9364`  |
| 2235   | Layout 1 | `11e83c1f9364`  |
| 2229   | Layout 1 | `11e83c1f9364`  |
| 2224   | Layout 1 | `11e83c1f9364`  |
| 2218   | Layout 1 | `11e83c1f9364`  |
| 2215   | Layout 1 | `11e83c1f9364`  |
| 2207   | Layout 1 | `11e83c1f9364`  |
| 2203   | Layout 1 | `11e83c1f9364`  |
| 2196   | Layout 1 | `11e83c1f9364`  |
| 2192   | Layout 1 | `11e83c1f9364`  |
| 2189   | Layout 1 | `11e83c1f9364`  |
| 2183   | Layout 1 | `11e83c1f9364`  |
| 2179   | Layout 1 | `11e83c1f9364`  |
| 2171   | Layout 1 | `11e83c1f9364`  |
| 2163   | Layout 1 | `11e83c1f9364`  |
| 2156   | Layout 1 | `11e83c1f9364`  |
| 2151   | Layout 1 | `11e83c1f9364`  |
| 2147   | Layout 1 | `11e83c1f9364`  |
| 2142   | Layout 1 | `11e83c1f9364`  |
| 2138   | Layout 1 | `11e83c1f9364`  |
| 2134   | Layout 1 | `11e83c1f9364`  |
| 2130   | Layout 1 | `11e83c1f9364`  |
| 2122   | Layout 1 | `11e83c1f9364`  |
| 2107   | Layout 1 | `11e83c1f9364`  |
| 2098   | Layout 1 | `11e83c1f9364`  |
| 2089   | Layout 1 | `11e83c1f9364`  |
| 2081   | Layout 1 | `11e83c1f9364`  |
| 2073   | Layout 1 | `11e83c1f9364`  |
| 2067   | Layout 1 | `11e83c1f9364`  |
| 2063   | Layout 1 | `11e83c1f9364`  |
| 2059   | Layout 1 | `11e83c1f9364`  |
| 2052   | Layout 1 | `11e83c1f9364`  |
| 2044   | Layout 1 | `11e83c1f9364`  |
| 2039   | Layout 1 | `11e83c1f9364`  |
| 2032   | Layout 1 | `11e83c1f9364`  |
| 2025   | Layout 1 | `11e83c1f9364`  |
| 2011   | Layout 1 | `11e83c1f9364`  |
| 2005   | No file  | `11e83c1f9364`  |
| 2000   | No file  | `11e83c1f9364`  |
| 1996   | No file  | `11e83c1f9364`  |
| 1991   | No file  | `11e83c1f9364`  |
| 1985   | No file  | `11e83c1f9364`  |
| 1980   | No file  | `11e83c1f9364`  |
| 1969   | No file  | `11e83c1f9364`  |
| 1964   | No file  | `11e83c1f9364`  |
| 1958   | No file  | `11e83c1f9364`  |
| 1950   | No file  | `11e83c1f9364`  |
| 1945   | No file  | `11e83c1f9364`  |
| 1937   | No file  | `11e83c1f9364`  |
| 1933   | No file  | `11e83c1f9364`  |
| 1927   | No file  | `11e83c1f9364`  |
| 1921   | No file  | `11e83c1f9364`  |
| 1914   | No file  | `11e83c1f9364`  |
| 1908   | No file  | `11e83c1f9364`  |
| 1897   | No file  | `11e83c1f9364`  |
| 1892   | No file  | `11e83c1f9364`  |
| 1886   | No file  | `11e83c1f9364`  |
| 1881   | No file  | `11e83c1f9364`  |
| 1871   | No file  | `11e83c1f9364`  |
| 1866   | No file  | `11e83c1f9364`  |
| 1862   | No file  | `11e83c1f9364`  |
| 1854   | No file  | `11e83c1f9364`  |
| 1846   | No file  | `11e83c1f9364`  |
| 1838   | No file  | `11e83c1f9364`  |
| 1832   | No file  | `11e83c1f9364`  |
| 1826   | No file  | `11e83c1f9364`  |
| 1822   | No file  | `11e83c1f9364`  |
| 1818   | No file  | `11e83c1f9364`  |
| 1804   | No file  | `11e83c1f9364`  |
| 1794   | No file  | `11e83c1f9364`  |
| 1790   | No file  | `11e83c1f9364`  |
| 1784   | No file  | `11e83c1f9364`  |
| 1774   | No file  | `11e83c1f9364`  |
| 1771   | No file  | `11e83c1f9364`  |
| 1762   | No file  | `11e83c1f9364`  |
| 1759   | No file  | `11e83c1f9364`  |
| 1754   | No file  | `11e83c1f9364`  |
| 1749   | No file  | `11e83c1f9364`  |
| 1743   | No file  | `11e83c1f9364`  |
| 1737   | No file  | `11e83c1f9364`  |
| 1731   | No file  | `11e83c1f9364`  |
| 1725   | No file  | `11e83c1f9364`  |
| 1717   | No file  | `11e83c1f9364`  |
| 1710   | No file  | `11e83c1f9364`  |
| 1704   | No file  | `11e83c1f9364`  |
| 1698   | No file  | `11e83c1f9364`  |
| 1690   | No file  | `11e83c1f9364`  |
| 1685   | No file  | `11e83c1f9364`  |
| 1680   | No file  | `11e83c1f9364`  |
| 1674   | No file  | `11e83c1f9364`  |
| 1668   | No file  | `11e83c1f9364`  |
| 1659   | No file  | `11e83c1f9364`  |
| 1649   | No file  | `11e83c1f9364`  |
| 1642   | No file  | `11e83c1f9364`  |
| 1636   | No file  | `11e83c1f9364`  |
| 1628   | No file  | `11e83c1f9364`  |
| 1622   | No file  | `11e83c1f9364`  |
| 1614   | No file  | `11e83c1f9364`  |
| 1608   | No file  | `11e83c1f9364`  |
| 1602   | No file  | `11e83c1f9364`  |
| 1598   | No file  | `11e83c1f9364`  |
| 1594   | No file  | `11e83c1f9364`  |
| 1590   | No file  | `11e83c1f9364`  |
| 1587   | No file  | `11e83c1f9364`  |
| 1584   | No file  | `11e83c1f9364`  |
| 1579   | No file  | `11e83c1f9364`  |
| 1572   | No file  | `11e83c1f9364`  |
| 1565   | No file  | `11e83c1f9364`  |
| 1559   | No file  | `11e83c1f9364`  |
| 1554   | No file  | `11e83c1f9364`  |
| 1547   | No file  | `11e83c1f9364`  |
| 1537   | No file  | `11e83c1f9364`  |
| 1529   | No file  | `11e83c1f9364`  |
| 1524   | No file  | `11e83c1f9364`  |
| 1519   | No file  | `11e83c1f9364`  |
| 1509   | No file  | `11e83c1f9364`  |
| 1506   | No file  | `11e83c1f9364`  |
| 1504   | No file  | `11e83c1f9364`  |
| 1500   | No file  | `11e83c1f9364`  |
| 1493   | No file  | `11e83c1f9364`  |
| 1489   | No file  | `11e83c1f9364`  |
| 1485   | No file  | `11e83c1f9364`  |
| 1481   | No file  | `11e83c1f9364`  |
| 1474   | No file  | `11e83c1f9364`  |
| 1466   | No file  | `11e83c1f9364`  |
| 1462   | No file  | `11e83c1f9364`  |
| 1459   | No file  | `11e83c1f9364`  |
| 1453   | No file  | `11e83c1f9364`  |
| 1450   | No file  | `11e83c1f9364`  |
| 1445   | No file  | `11e83c1f9364`  |
| 1439   | No file  | `11e83c1f9364`  |
| 1433   | No file  | `11e83c1f9364`  |
| 1430   | No file  | `11e83c1f9364`  |
| 1426   | No file  | `11e83c1f9364`  |
| 1421   | No file  | `11e83c1f9364`  |
| 1417   | No file  | `11e83c1f9364`  |
| 1416   | No file  | `11e83c1f9364`  |
| 1409   | No file  | `11e83c1f9364`  |
| 1405   | No file  | `11e83c1f9364`  |
| 1401   | No file  | `11e83c1f9364`  |
| 1396   | No file  | `11e83c1f9364`  |
| 1391   | No file  | `11e83c1f9364`  |
| 1390   | No file  | `11e83c1f9364`  |
| 1386   | No file  | `11e83c1f9364`  |
| 1381   | No file  | `11e83c1f9364`  |
| 1379   | No file  | `11e83c1f9364`  |
| 1372   | No file  | `11e83c1f9364`  |
| 1366   | No file  | `11e83c1f9364`  |
| 1364   | No file  | `11e83c1f9364`  |
| 1363   | No file  | `11e83c1f9364`  |
| 1360   | No file  | `11e83c1f9364`  |
| 1358   | No file  | `11e83c1f9364`  |
| 1355   | No file  | `11e83c1f9364`  |
| 1351   | No file  | `11e83c1f9364`  |
| 1348   | No file  | `11e83c1f9364`  |
| 1346   | No file  | `11e83c1f9364`  |
| 1341   | No file  | `11e83c1f9364`  |
| 1340   | No file  | `11e83c1f9364`  |
| 1338   | No file  | `11e83c1f9364`  |
| 1335   | No file  | `11e83c1f9364`  |
| 1333   | No file  | `11e83c1f9364`  |
| 1329   | No file  | `11e83c1f9364`  |
| 1327   | No file  | `11e83c1f9364`  |
| 1324   | No file  | `11e83c1f9364`  |
| 1321   | No file  | `11e83c1f9364`  |
| 1319   | No file  | `11e83c1f9364`  |
| 1318   | No file  | `11e83c1f9364`  |
| 1316   | No file  | `11e83c1f9364`  |
| 1313   | No file  | `11e83c1f9364`  |
| 1311   | No file  | `11e83c1f9364`  |
| 1309   | No file  | `11e83c1f9364`  |
| 1304   | No file  | `11e83c1f9364`  |
| 1292   | No file  | `11e83c1f9364`  |
| 1286   | No file  | `11e83c1f9364`  |
| 1280   | No file  | `11e83c1f9364`  |
| 1276   | No file  | `11e83c1f9364`  |
| 1267   | No file  | `11e83c1f9364`  |
| 1261   | No file  | `11e83c1f9364`  |
| 1256   | No file  | `11e83c1f9364`  |
| 1250   | No file  | `11e83c1f9364`  |
| 1246   | No file  | `11e83c1f9364`  |
| 1239   | No file  | `11e83c1f9364`  |
| 1230   | No file  | `11e83c1f9364`  |
| 1226   | No file  | `11e83c1f9364`  |
| 1220   | No file  | `11e83c1f9364`  |
| 1217   | No file  | `11e83c1f9364`  |
| 1211   | No file  | `11e83c1f9364`  |
| 1210   | No file  | `11e83c1f9364`  |
| 1208   | No file  | `11e83c1f9364`  |
| 1203   | No file  | `11e83c1f9364`  |
| 1197   | No file  | `11e83c1f9364`  |
| 1194   | No file  | `11e83c1f9364`  |
| 1192   | No file  | `11e83c1f9364`  |
| 1187   | No file  | `11e83c1f9364`  |
| 1183   | No file  | `11e83c1f9364`  |
| 1177   | No file  | `11e83c1f9364`  |
| 1173   | No file  | `11e83c1f9364`  |
| 1167   | No file  | `11e83c1f9364`  |
| 1164   | No file  | `11e83c1f9364`  |
| 1156   | No file  | `11e83c1f9364`  |
| 1149   | No file  | `11e83c1f9364`  |
| 1144   | No file  | `11e83c1f9364`  |
| 1137   | No file  | `11e83c1f9364`  |
| 1132   | No file  | `11e83c1f9364`  |
| 1127   | No file  | `11e83c1f9364`  |
| 1122   | No file  | `11e83c1f9364`  |
| 1118   | No file  | `11e83c1f9364`  |
| 1114   | No file  | `11e83c1f9364`  |
| 1109   | No file  | `11e83c1f9364`  |
| 1102   | No file  | `11e83c1f9364`  |
| 1096   | No file  | `11e83c1f9364`  |
| 1088   | No file  | `11e83c1f9364`  |
| 1081   | No file  | `11e83c1f9364`  |
| 1076   | No file  | `11e83c1f9364`  |
| 1069   | No file  | `11e83c1f9364`  |
| 1064   | No file  | `11e83c1f9364`  |
| 1058   | No file  | `11e83c1f9364`  |
| 1051   | No file  | `11e83c1f9364`  |
| 1044   | No file  | `11e83c1f9364`  |
| 1036   | No file  | `11e83c1f9364`  |
| 1026   | No file  | `11e83c1f9364`  |
| 1016   | No file  | `11e83c1f9364`  |
| 1009   | No file  | `11e83c1f9364`  |
| 1005   | No file  | `11e83c1f9364`  |
| 1000   | No file  | `11e83c1f9364`  |
| 998    | No file  | `11e83c1f9364`  |
| 990    | No file  | `11e83c1f9364`  |
| 979    | No file  | `11e83c1f9364`  |
| 972    | No file  | `11e83c1f9364`  |
| 963    | No file  | `11e83c1f9364`  |
| 955    | No file  | `11e83c1f9364`  |
| 946    | No file  | `11e83c1f9364`  |
| 938    | No file  | `11e83c1f9364`  |
| 927    | No file  | `11e83c1f9364`  |
| 911    | No file  | `11e83c1f9364`  |
| 904    | No file  | `11e83c1f9364`  |
| 899    | No file  | `11e83c1f9364`  |
| 894    | No file  | `11e83c1f9364`  |
| 885    | No file  | `11e83c1f9364`  |
| 879    | No file  | `11e83c1f9364`  |
| 872    | No file  | `11e83c1f9364`  |
| 864    | No file  | `11e83c1f9364`  |
| 855    | No file  | `11e83c1f9364`  |
| 853    | No file  | `11e83c1f9364`  |
| 845    | No file  | `11e83c1f9364`  |
| 837    | No file  | `11e83c1f9364`  |
| 829    | No file  | `11e83c1f9364`  |
| 822    | No file  | `11e83c1f9364`  |
| 814    | No file  | `11e83c1f9364`  |
| 805    | No file  | `11e83c1f9364`  |
| 794    | No file  | `11e83c1f9364`  |
| 787    | No file  | `11e83c1f9364`  |
| 780    | No file  | `11e83c1f9364`  |
| 771    | No file  | `11e83c1f9364`  |
| 760    | No file  | `11e83c1f9364`  |
| 748    | No file  | `11e83c1f9364`  |
| 741    | No file  | `11e83c1f9364`  |
| 736    | No file  | `11e83c1f9364`  |
| 731    | No file  | `11e83c1f9364`  |
| 723    | No file  | `11e83c1f9364`  |
| 711    | No file  | `11e83c1f9364`  |
| 707    | No file  | `11e83c1f9364`  |
| 697    | No file  | `11e83c1f9364`  |
| 689    | No file  | `11e83c1f9364`  |
| 683    | No file  | `11e83c1f9364`  |
| 678    | No file  | `11e83c1f9364`  |
| 670    | No file  | `11e83c1f9364`  |
| 661    | No file  | `11e83c1f9364`  |
| 656    | No file  | `11e83c1f9364`  |
| 652    | No file  | `11e83c1f9364`  |
| 643    | No file  | `11e83c1f9364`  |
| 637    | No file  | `11e83c1f9364`  |
| 630    | No file  | `11e83c1f9364`  |
| 627    | No file  | `11e83c1f9364`  |
| 621    | No file  | `11e83c1f9364`  |
| 617    | No file  | `11e83c1f9364`  |
| 615    | No file  | `11e83c1f9364`  |
| 606    | No file  | `11e83c1f9364`  |
| 599    | No file  | `11e83c1f9364`  |
| 592    | No file  | `11e83c1f9364`  |
| 586    | No file  | `11e83c1f9364`  |
| 577    | No file  | `11e83c1f9364`  |
| 569    | No file  | `11e83c1f9364`  |
| 561    | No file  | `11e83c1f9364`  |
| 554    | No file  | `11e83c1f9364`  |
| 542    | No file  | `11e83c1f9364`  |
| 532    | No file  | `11e83c1f9364`  |
| 531    | No file  | `11e83c1f9364`  |
| 526    | No file  | `11e83c1f9364`  |
| 521    | No file  | `11e83c1f9364`  |
| 517    | No file  | `11e83c1f9364`  |
| 510    | No file  | `11e83c1f9364`  |
| 508    | No file  | `11e83c1f9364`  |
| 504    | No file  | `11e83c1f9364`  |
| 497    | No file  | `11e83c1f9364`  |
| 491    | No file  | `11e83c1f9364`  |
| 485    | No file  | `11e83c1f9364`  |
| 478    | No file  | `11e83c1f9364`  |
| 472    | No file  | `11e83c1f9364`  |
| 466    | No file  | `11e83c1f9364`  |
| 457    | No file  | `11e83c1f9364`  |
| 452    | No file  | `11e83c1f9364`  |
| 449    | No file  | `11e83c1f9364`  |
| 435    | No file  | `11e83c1f9364`  |

<!-- versions:end -->

## Companion Files

None. The handler names both regions (LOC type 17) from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

### Row (variable: 4 bytes + moves)

| Offset  | Type              | Field      | Notes                                         |
| ------- | ----------------- | ---------- | --------------------------------------------- |
| `+0x00` | u32               | move_count | Number of `moves`; the same on every row      |
| `+0x04` | Move[move_count]  | moves      | See Move                                      |

### Move (12 bytes)

| Offset  | Type | Field        | Notes                                                                            |
| ------- | ---- | ------------ | -------------------------------------------------------------------------------- |
| `+0x00` | u64  | move_cost    | `5000000` or `0` on client 3482; `0` on exactly one move per row                 |
| `+0x08` | u16  | region_key_1 | `regioninfo.bss` region key (LOC type 17); the same on every move of a row, unique per row |
| `+0x0A` | u16  | region_key_2 | `regioninfo.bss` region key (LOC type 17); every row lists the same set                              |

## Free Moves

Client 3482: each row's region and the region of its `0` move.

| `region_key_1`             | `region_key_2`               |
| -------------------------- | ---------------------------- |
| 1733 Angavu Outpost        | 1741 Radiant Lands           |
| 1677 Olvia Academy Grounds | 1681 Olvia Academy Dining Hall |
| 1553 Hakinza Sanctuary     | 1574 Great White Spot        |
| 1121 Erethea's Belt        | 1122 Zvier Highlands         |
| 1420 Yukjo Street          | 1419 Seoul                   |
| 1375 Muzgar                | 1383 Turba Farm              |
| 1319 Chief's Home          | 1219 Nampo's Moodle Village  |
| 735 Grána                  | 1073 Lake Flondor            |
| 639 Erdal Farm             | 641 Fohalam Farm             |
| 1000 Oquilla's Eye         | 984 Oquilla's Eye            |
| 1023 Delmira Plantation    | 1022 Salanar Pond            |
| 903 Marak Farm             | 926 Duvencrune Farmland      |
| 236 Altinova Gateway       | 204 Stonebeak Shore          |
| 16 Bartali Farm            | 5 Velia                      |
| 300 Gabino Farm            | 267 Falres Dirt Farm         |
| 318 Moretti Plantation     | 36 Eastern Border            |

## Field Names

The Magnus is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`Abyss` in its name. `move_cost` follows the file name; the two region
keys resolve to LOC type 17 names on every move. Which of the two is the
start of a move is not known, so they keep the numbers of their order in
the move.

## Notes

- Client 2107 holds 9 rows of 9 moves (1,012 bytes) with costs that grow
  with the distance between the two regions: from Erethea's Belt `0` to
  Zvier Highlands, `2100000` to Duvencrune Farmland and `11200000` to
  Fohalam Farm. Client 3482 has one cost for every move that is not free.
- Six of the 16 `region_key_1` regions (Angavu Outpost, Hakinza
  Sanctuary, Yukjo Street, Muzgar, Grána and Oquilla's Eye) are storage
  towns of [`abyssonewarehouse.bss`](abyssonewarehouse_bss.md) on client
  3482.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/abyssone_tables.py`: one
  row per region, each move as both regions with names and the cost.

## Open Questions

### What a Move Is

The rows pair 16 regions with 16 others and make one nearby pair per row
free. A move from the Magnus out to a vein
other than the one the character came in by would fit; no client Lua of
client 3482 names the file or a move cost getter. In game every move I
know of costs 5,000,000 silver in either direction, the same as the
`5000000` cost here, so the cost does not tell which region is the start.
