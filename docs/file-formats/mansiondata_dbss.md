# `mansiondata.dbss` Format

## Purpose

The furniture characters that belong to the manor: one 6-byte row per
installation character. On client 3482 the file lists 498 characters (304
on client 1784): 234 named `[Manor] ...` ("[Manor] Starspun Chandelier",
`4398`) or `[Event] [Manor] ...` in LOC type 6, 216 development objects
named `Dev ...` ("Dev Plant13- AfricanIron", `4454`), 4 more with a name and
44 keys (`6956` to `15993`) with no `characterstatic.dbss` row. Companion
`mansiondataoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records        | Row bytes |
| ------ | -------------- | ------------------------ | ----- | -------------- | --------- |
| 1      | 1537 and later | `mansiondata.dbss`       | 2,992 | 498 Row        | 6         |
| 1      | 1537 and later | `mansiondataoffset.dbss` | 4,984 | 498 Offset Row | 10        |

| Layout | File                     | Known            | Unknown       |
| ------ | ------------------------ | ---------------- | ------------- |
| 1      | `mansiondata.dbss`       | 1,996 B (66.7%)  | 996 B (33.3%) |
| 1      | `mansiondataoffset.dbss` | 4,984 B (100.0%) | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e4efd28cf73f`  |
| 3482   | Layout 1 | `e4efd28cf73f`  |
| 3474   | Layout 1 | `e4efd28cf73f`  |
| 3473   | Layout 1 | `e4efd28cf73f`  |
| 3464   | Layout 1 | `e4efd28cf73f`  |
| 3458   | Layout 1 | `e4efd28cf73f`  |
| 3454   | Layout 1 | `e4efd28cf73f`  |
| 3444   | Layout 1 | `e4efd28cf73f`  |
| 3435   | Layout 1 | `e4efd28cf73f`  |
| 3426   | Layout 1 | `e4efd28cf73f`  |
| 3418   | Layout 1 | `e4efd28cf73f`  |
| 3412   | Layout 1 | `e4efd28cf73f`  |
| 3402   | Layout 1 | `e4efd28cf73f`  |
| 3396   | Layout 1 | `e4efd28cf73f`  |
| 3387   | Layout 1 | `e4efd28cf73f`  |
| 3381   | Layout 1 | `e4efd28cf73f`  |
| 3373   | Layout 1 | `e4efd28cf73f`  |
| 3364   | Layout 1 | `e4efd28cf73f`  |
| 3356   | Layout 1 | `e4efd28cf73f`  |
| 3349   | Layout 1 | `e4efd28cf73f`  |
| 3342   | Layout 1 | `e4efd28cf73f`  |
| 3335   | Layout 1 | `e4efd28cf73f`  |
| 3326   | Layout 1 | `e4efd28cf73f`  |
| 3321   | Layout 1 | `e4efd28cf73f`  |
| 3314   | Layout 1 | `e4efd28cf73f`  |
| 3303   | Layout 1 | `e4efd28cf73f`  |
| 3302   | Layout 1 | `e4efd28cf73f`  |
| 3293   | Layout 1 | `e4efd28cf73f`  |
| 3283   | Layout 1 | `e4efd28cf73f`  |
| 3275   | Layout 1 | `e4efd28cf73f`  |
| 3267   | Layout 1 | `e4efd28cf73f`  |
| 3258   | Layout 1 | `e4efd28cf73f`  |
| 3251   | Layout 1 | `e4efd28cf73f`  |
| 3242   | Layout 1 | `e4efd28cf73f`  |
| 3235   | Layout 1 | `e4efd28cf73f`  |
| 3229   | Layout 1 | `e4efd28cf73f`  |
| 3212   | Layout 1 | `e4efd28cf73f`  |
| 3203   | Layout 1 | `e4efd28cf73f`  |
| 3193   | Layout 1 | `e4efd28cf73f`  |
| 3186   | Layout 1 | `e4efd28cf73f`  |
| 3177   | Layout 1 | `e4efd28cf73f`  |
| 3169   | Layout 1 | `e4efd28cf73f`  |
| 3158   | Layout 1 | `e4efd28cf73f`  |
| 3151   | Layout 1 | `e4efd28cf73f`  |
| 3144   | Layout 1 | `e4efd28cf73f`  |
| 3133   | Layout 1 | `e4efd28cf73f`  |
| 3125   | Layout 1 | `e4efd28cf73f`  |
| 3118   | Layout 1 | `e4efd28cf73f`  |
| 3111   | Layout 1 | `e4efd28cf73f`  |
| 3103   | Layout 1 | `e4efd28cf73f`  |
| 3095   | Layout 1 | `e4efd28cf73f`  |
| 3086   | Layout 1 | `e4efd28cf73f`  |
| 3072   | Layout 1 | `e4efd28cf73f`  |
| 3062   | Layout 1 | `e4efd28cf73f`  |
| 3052   | Layout 1 | `e4efd28cf73f`  |
| 3045   | Layout 1 | `e4efd28cf73f`  |
| 3037   | Layout 1 | `e4efd28cf73f`  |
| 3030   | Layout 1 | `e4efd28cf73f`  |
| 3021   | Layout 1 | `e4efd28cf73f`  |
| 3012   | Layout 1 | `e4efd28cf73f`  |
| 3002   | Layout 1 | `e4efd28cf73f`  |
| 2995   | Layout 1 | `e4efd28cf73f`  |
| 2987   | Layout 1 | `e4efd28cf73f`  |
| 2978   | Layout 1 | `e4efd28cf73f`  |
| 2970   | Layout 1 | `e4efd28cf73f`  |
| 2959   | Layout 1 | `e4efd28cf73f`  |
| 2951   | Layout 1 | `e4efd28cf73f`  |
| 2942   | Layout 1 | `e4efd28cf73f`  |
| 2935   | Layout 1 | `e4efd28cf73f`  |
| 2932   | Layout 1 | `e4efd28cf73f`  |
| 2923   | Layout 1 | `e4efd28cf73f`  |
| 2919   | Layout 1 | `e4efd28cf73f`  |
| 2907   | Layout 1 | `e4efd28cf73f`  |
| 2900   | Layout 1 | `e4efd28cf73f`  |
| 2891   | Layout 1 | `e4efd28cf73f`  |
| 2882   | Layout 1 | `e4efd28cf73f`  |
| 2872   | Layout 1 | `e4efd28cf73f`  |
| 2863   | Layout 1 | `e4efd28cf73f`  |
| 2855   | Layout 1 | `e4efd28cf73f`  |
| 2849   | Layout 1 | `e4efd28cf73f`  |
| 2844   | Layout 1 | `e4efd28cf73f`  |
| 2834   | Layout 1 | `e4efd28cf73f`  |
| 2825   | Layout 1 | `e4efd28cf73f`  |
| 2819   | Layout 1 | `e4efd28cf73f`  |
| 2811   | Layout 1 | `e4efd28cf73f`  |
| 2803   | Layout 1 | `e4efd28cf73f`  |
| 2794   | Layout 1 | `e4efd28cf73f`  |
| 2783   | Layout 1 | `e4efd28cf73f`  |
| 2774   | Layout 1 | `e4efd28cf73f`  |
| 2765   | Layout 1 | `e4efd28cf73f`  |
| 2756   | Layout 1 | `e4efd28cf73f`  |
| 2750   | Layout 1 | `e4efd28cf73f`  |
| 2743   | Layout 1 | `e4efd28cf73f`  |
| 2736   | Layout 1 | `e4efd28cf73f`  |
| 2726   | Layout 1 | `e4efd28cf73f`  |
| 2717   | Layout 1 | `e4efd28cf73f`  |
| 2709   | Layout 1 | `e4efd28cf73f`  |
| 2703   | Layout 1 | `e4efd28cf73f`  |
| 2695   | Layout 1 | `e4efd28cf73f`  |
| 2684   | Layout 1 | `e4efd28cf73f`  |
| 2672   | Layout 1 | `e4efd28cf73f`  |
| 2665   | Layout 1 | `e4efd28cf73f`  |
| 2657   | Layout 1 | `e4efd28cf73f`  |
| 2649   | Layout 1 | `e4efd28cf73f`  |
| 2644   | Layout 1 | `e4efd28cf73f`  |
| 2637   | Layout 1 | `e4efd28cf73f`  |
| 2629   | Layout 1 | `e4efd28cf73f`  |
| 2619   | Layout 1 | `e4efd28cf73f`  |
| 2612   | Layout 1 | `e4efd28cf73f`  |
| 2606   | Layout 1 | `e4efd28cf73f`  |
| 2602   | Layout 1 | `e4efd28cf73f`  |
| 2601   | Layout 1 | `e4efd28cf73f`  |
| 2592   | Layout 1 | `e4efd28cf73f`  |
| 2583   | Layout 1 | `e4efd28cf73f`  |
| 2575   | Layout 1 | `e4efd28cf73f`  |
| 2567   | Layout 1 | `e4efd28cf73f`  |
| 2560   | Layout 1 | `e4efd28cf73f`  |
| 2553   | Layout 1 | `e4efd28cf73f`  |
| 2545   | Layout 1 | `e4efd28cf73f`  |
| 2538   | Layout 1 | `e4efd28cf73f`  |
| 2529   | Layout 1 | `e4efd28cf73f`  |
| 2519   | Layout 1 | `e4efd28cf73f`  |
| 2513   | Layout 1 | `e4efd28cf73f`  |
| 2510   | Layout 1 | `e4efd28cf73f`  |
| 2507   | Layout 1 | `e4efd28cf73f`  |
| 2503   | Layout 1 | `e4efd28cf73f`  |
| 2498   | Layout 1 | `e4efd28cf73f`  |
| 2492   | Layout 1 | `e4efd28cf73f`  |
| 2487   | Layout 1 | `e4efd28cf73f`  |
| 2480   | Layout 1 | `e4efd28cf73f`  |
| 2474   | Layout 1 | `e4efd28cf73f`  |
| 2468   | Layout 1 | `e4efd28cf73f`  |
| 2460   | Layout 1 | `e4efd28cf73f`  |
| 2453   | Layout 1 | `e4efd28cf73f`  |
| 2444   | Layout 1 | `e4efd28cf73f`  |
| 2438   | Layout 1 | `e4efd28cf73f`  |
| 2434   | Layout 1 | `e4efd28cf73f`  |
| 2429   | Layout 1 | `e4efd28cf73f`  |
| 2421   | Layout 1 | `e4efd28cf73f`  |
| 2414   | Layout 1 | `e4efd28cf73f`  |
| 2407   | Layout 1 | `e4efd28cf73f`  |
| 2401   | Layout 1 | `e4efd28cf73f`  |
| 2397   | Layout 1 | `e4efd28cf73f`  |
| 2393   | Layout 1 | `e4efd28cf73f`  |
| 2384   | Layout 1 | `e4efd28cf73f`  |
| 2378   | Layout 1 | `e4efd28cf73f`  |
| 2372   | Layout 1 | `e4efd28cf73f`  |
| 2358   | Layout 1 | `e4efd28cf73f`  |
| 2352   | Layout 1 | `e4efd28cf73f`  |
| 2347   | Layout 1 | `e4efd28cf73f`  |
| 2343   | Layout 1 | `e4efd28cf73f`  |
| 2335   | Layout 1 | `e4efd28cf73f`  |
| 2327   | Layout 1 | `e4efd28cf73f`  |
| 2324   | Layout 1 | `e4efd28cf73f`  |
| 2319   | Layout 1 | `e4efd28cf73f`  |
| 2313   | Layout 1 | `e4efd28cf73f`  |
| 2308   | Layout 1 | `e4efd28cf73f`  |
| 2302   | Layout 1 | `e4efd28cf73f`  |
| 2295   | Layout 1 | `e4efd28cf73f`  |
| 2290   | Layout 1 | `e4efd28cf73f`  |
| 2284   | Layout 1 | `e4efd28cf73f`  |
| 2276   | Layout 1 | `e4efd28cf73f`  |
| 2269   | Layout 1 | `e4efd28cf73f`  |
| 2259   | Layout 1 | `e4efd28cf73f`  |
| 2250   | Layout 1 | `e4efd28cf73f`  |
| 2243   | Layout 1 | `e4efd28cf73f`  |
| 2235   | Layout 1 | `e4efd28cf73f`  |
| 2229   | Layout 1 | `e4efd28cf73f`  |
| 2224   | Layout 1 | `e4efd28cf73f`  |
| 2218   | Layout 1 | `e4efd28cf73f`  |
| 2215   | Layout 1 | `e4efd28cf73f`  |
| 2207   | Layout 1 | `e4efd28cf73f`  |
| 2203   | Layout 1 | `e4efd28cf73f`  |
| 2196   | Layout 1 | `e4efd28cf73f`  |
| 2192   | Layout 1 | `e4efd28cf73f`  |
| 2189   | Layout 1 | `e4efd28cf73f`  |
| 2183   | Layout 1 | `e4efd28cf73f`  |
| 2179   | Layout 1 | `e4efd28cf73f`  |
| 2171   | Layout 1 | `e4efd28cf73f`  |
| 2163   | Layout 1 | `e4efd28cf73f`  |
| 2156   | Layout 1 | `e4efd28cf73f`  |
| 2151   | Layout 1 | `e4efd28cf73f`  |
| 2147   | Layout 1 | `e4efd28cf73f`  |
| 2142   | Layout 1 | `e4efd28cf73f`  |
| 2138   | Layout 1 | `e4efd28cf73f`  |
| 2134   | Layout 1 | `e4efd28cf73f`  |
| 2130   | Layout 1 | `e4efd28cf73f`  |
| 2122   | Layout 1 | `e4efd28cf73f`  |
| 2107   | Layout 1 | `e4efd28cf73f`  |
| 2098   | Layout 1 | `e4efd28cf73f`  |
| 2089   | Layout 1 | `e4efd28cf73f`  |
| 2081   | Layout 1 | `e4efd28cf73f`  |
| 2073   | Layout 1 | `e4efd28cf73f`  |
| 2067   | Layout 1 | `e4efd28cf73f`  |
| 2063   | Layout 1 | `e4efd28cf73f`  |
| 2059   | Layout 1 | `e4efd28cf73f`  |
| 2052   | Layout 1 | `e4efd28cf73f`  |
| 2044   | Layout 1 | `e4efd28cf73f`  |
| 2039   | Layout 1 | `e4efd28cf73f`  |
| 2032   | Layout 1 | `e4efd28cf73f`  |
| 2025   | Layout 1 | `e4efd28cf73f`  |
| 2011   | Layout 1 | `e4efd28cf73f`  |
| 2005   | Layout 1 | `e4efd28cf73f`  |
| 2000   | Layout 1 | `e4efd28cf73f`  |
| 1996   | Layout 1 | `e4efd28cf73f`  |
| 1991   | Layout 1 | `e4efd28cf73f`  |
| 1985   | Layout 1 | `e4efd28cf73f`  |
| 1980   | Layout 1 | `e4efd28cf73f`  |
| 1969   | Layout 1 | `e4efd28cf73f`  |
| 1964   | Layout 1 | `e4efd28cf73f`  |
| 1958   | Layout 1 | `e4efd28cf73f`  |
| 1950   | Layout 1 | `e4efd28cf73f`  |
| 1945   | Layout 1 | `e4efd28cf73f`  |
| 1937   | Layout 1 | `e4efd28cf73f`  |
| 1933   | Layout 1 | `e4efd28cf73f`  |
| 1927   | Layout 1 | `e4efd28cf73f`  |
| 1921   | Layout 1 | `e4efd28cf73f`  |
| 1914   | Layout 1 | `e4efd28cf73f`  |
| 1908   | Layout 1 | `e4efd28cf73f`  |
| 1897   | Layout 1 | `e4efd28cf73f`  |
| 1892   | Layout 1 | `e4efd28cf73f`  |
| 1886   | Layout 1 | `e4efd28cf73f`  |
| 1881   | Layout 1 | `e4efd28cf73f`  |
| 1871   | Layout 1 | `e4efd28cf73f`  |
| 1866   | Layout 1 | `e4efd28cf73f`  |
| 1862   | Layout 1 | `e4efd28cf73f`  |
| 1854   | Layout 1 | `e4efd28cf73f`  |
| 1846   | Layout 1 | `e4efd28cf73f`  |
| 1838   | Layout 1 | `e4efd28cf73f`  |
| 1832   | Layout 1 | `e4efd28cf73f`  |
| 1826   | Layout 1 | `e4efd28cf73f`  |
| 1822   | Layout 1 | `e4efd28cf73f`  |
| 1818   | Layout 1 | `e4efd28cf73f`  |
| 1804   | Layout 1 | `e4efd28cf73f`  |
| 1794   | Layout 1 | `e4efd28cf73f`  |
| 1790   | Layout 1 | `e4efd28cf73f`  |
| 1784   | Layout 1 | `e4efd28cf73f`  |
| 1774   | Layout 1 | `e4efd28cf73f`  |
| 1771   | Layout 1 | `e4efd28cf73f`  |
| 1762   | Layout 1 | `e4efd28cf73f`  |
| 1759   | Layout 1 | `e4efd28cf73f`  |
| 1754   | Layout 1 | `e4efd28cf73f`  |
| 1749   | Layout 1 | `e4efd28cf73f`  |
| 1743   | Layout 1 | `e4efd28cf73f`  |
| 1737   | Layout 1 | `e4efd28cf73f`  |
| 1731   | Layout 1 | `e4efd28cf73f`  |
| 1725   | Layout 1 | `e4efd28cf73f`  |
| 1717   | Layout 1 | `e4efd28cf73f`  |
| 1710   | Layout 1 | `e4efd28cf73f`  |
| 1704   | Layout 1 | `e4efd28cf73f`  |
| 1698   | Layout 1 | `e4efd28cf73f`  |
| 1690   | Layout 1 | `e4efd28cf73f`  |
| 1685   | Layout 1 | `e4efd28cf73f`  |
| 1680   | Layout 1 | `e4efd28cf73f`  |
| 1674   | Layout 1 | `e4efd28cf73f`  |
| 1668   | Layout 1 | `e4efd28cf73f`  |
| 1659   | Layout 1 | `e4efd28cf73f`  |
| 1649   | Layout 1 | `e4efd28cf73f`  |
| 1642   | Layout 1 | `e4efd28cf73f`  |
| 1636   | Layout 1 | `e4efd28cf73f`  |
| 1628   | Layout 1 | `e4efd28cf73f`  |
| 1622   | Layout 1 | `e4efd28cf73f`  |
| 1614   | Layout 1 | `e4efd28cf73f`  |
| 1608   | Layout 1 | `e4efd28cf73f`  |
| 1602   | Layout 1 | `e4efd28cf73f`  |
| 1598   | Layout 1 | `e4efd28cf73f`  |
| 1594   | Layout 1 | `e4efd28cf73f`  |
| 1590   | Layout 1 | `e4efd28cf73f`  |
| 1587   | Layout 1 | `e4efd28cf73f`  |
| 1584   | Layout 1 | `e4efd28cf73f`  |
| 1579   | Layout 1 | `e4efd28cf73f`  |
| 1572   | Layout 1 | `e4efd28cf73f`  |
| 1565   | Layout 1 | `e4efd28cf73f`  |
| 1559   | Layout 1 | `e4efd28cf73f`  |
| 1554   | Layout 1 | `e4efd28cf73f`  |
| 1547   | Layout 1 | `e4efd28cf73f`  |
| 1537   | Layout 1 | `e4efd28cf73f`  |
| 1529   | No file  | `e4efd28cf73f`  |
| 1524   | No file  | `e4efd28cf73f`  |
| 1519   | No file  | `e4efd28cf73f`  |
| 1509   | No file  | `e4efd28cf73f`  |
| 1506   | No file  | `e4efd28cf73f`  |
| 1504   | No file  | `e4efd28cf73f`  |
| 1500   | No file  | `e4efd28cf73f`  |
| 1493   | No file  | `e4efd28cf73f`  |
| 1489   | No file  | `e4efd28cf73f`  |
| 1485   | No file  | `e4efd28cf73f`  |
| 1481   | No file  | `e4efd28cf73f`  |
| 1474   | No file  | `e4efd28cf73f`  |
| 1466   | No file  | `e4efd28cf73f`  |
| 1462   | No file  | `e4efd28cf73f`  |
| 1459   | No file  | `e4efd28cf73f`  |
| 1453   | No file  | `e4efd28cf73f`  |
| 1450   | No file  | `e4efd28cf73f`  |
| 1445   | No file  | `e4efd28cf73f`  |
| 1439   | No file  | `e4efd28cf73f`  |
| 1433   | No file  | `e4efd28cf73f`  |
| 1430   | No file  | `e4efd28cf73f`  |
| 1426   | No file  | `e4efd28cf73f`  |
| 1421   | No file  | `e4efd28cf73f`  |
| 1417   | No file  | `e4efd28cf73f`  |
| 1416   | No file  | `e4efd28cf73f`  |
| 1409   | No file  | `e4efd28cf73f`  |
| 1405   | No file  | `e4efd28cf73f`  |
| 1401   | No file  | `e4efd28cf73f`  |
| 1396   | No file  | `e4efd28cf73f`  |
| 1391   | No file  | `e4efd28cf73f`  |
| 1390   | No file  | `e4efd28cf73f`  |
| 1386   | No file  | `e4efd28cf73f`  |
| 1381   | No file  | `e4efd28cf73f`  |
| 1379   | No file  | `e4efd28cf73f`  |
| 1372   | No file  | `e4efd28cf73f`  |
| 1366   | No file  | `e4efd28cf73f`  |
| 1364   | No file  | `e4efd28cf73f`  |
| 1363   | No file  | `e4efd28cf73f`  |
| 1360   | No file  | `e4efd28cf73f`  |
| 1358   | No file  | `e4efd28cf73f`  |
| 1355   | No file  | `e4efd28cf73f`  |
| 1351   | No file  | `e4efd28cf73f`  |
| 1348   | No file  | `e4efd28cf73f`  |
| 1346   | No file  | `e4efd28cf73f`  |
| 1341   | No file  | `e4efd28cf73f`  |
| 1340   | No file  | `e4efd28cf73f`  |
| 1338   | No file  | `e4efd28cf73f`  |
| 1335   | No file  | `e4efd28cf73f`  |
| 1333   | No file  | `e4efd28cf73f`  |
| 1329   | No file  | `e4efd28cf73f`  |
| 1327   | No file  | `e4efd28cf73f`  |
| 1324   | No file  | `e4efd28cf73f`  |
| 1321   | No file  | `e4efd28cf73f`  |
| 1319   | No file  | `e4efd28cf73f`  |
| 1318   | No file  | `e4efd28cf73f`  |
| 1316   | No file  | `e4efd28cf73f`  |
| 1313   | No file  | `e4efd28cf73f`  |
| 1311   | No file  | `e4efd28cf73f`  |
| 1309   | No file  | `e4efd28cf73f`  |
| 1304   | No file  | `e4efd28cf73f`  |
| 1292   | No file  | `e4efd28cf73f`  |
| 1286   | No file  | `e4efd28cf73f`  |
| 1280   | No file  | `e4efd28cf73f`  |
| 1276   | No file  | `e4efd28cf73f`  |
| 1267   | No file  | `e4efd28cf73f`  |
| 1261   | No file  | `e4efd28cf73f`  |
| 1256   | No file  | `e4efd28cf73f`  |
| 1250   | No file  | `e4efd28cf73f`  |
| 1246   | No file  | `e4efd28cf73f`  |
| 1239   | No file  | `e4efd28cf73f`  |
| 1230   | No file  | `e4efd28cf73f`  |
| 1226   | No file  | `e4efd28cf73f`  |
| 1220   | No file  | `e4efd28cf73f`  |
| 1217   | No file  | `e4efd28cf73f`  |
| 1211   | No file  | `e4efd28cf73f`  |
| 1210   | No file  | `e4efd28cf73f`  |
| 1208   | No file  | `e4efd28cf73f`  |
| 1203   | No file  | `e4efd28cf73f`  |
| 1197   | No file  | `e4efd28cf73f`  |
| 1194   | No file  | `e4efd28cf73f`  |
| 1192   | No file  | `e4efd28cf73f`  |
| 1187   | No file  | `e4efd28cf73f`  |
| 1183   | No file  | `e4efd28cf73f`  |
| 1177   | No file  | `e4efd28cf73f`  |
| 1173   | No file  | `e4efd28cf73f`  |
| 1167   | No file  | `e4efd28cf73f`  |
| 1164   | No file  | `e4efd28cf73f`  |
| 1156   | No file  | `e4efd28cf73f`  |
| 1149   | No file  | `e4efd28cf73f`  |
| 1144   | No file  | `e4efd28cf73f`  |
| 1137   | No file  | `e4efd28cf73f`  |
| 1132   | No file  | `e4efd28cf73f`  |
| 1127   | No file  | `e4efd28cf73f`  |
| 1122   | No file  | `e4efd28cf73f`  |
| 1118   | No file  | `e4efd28cf73f`  |
| 1114   | No file  | `e4efd28cf73f`  |
| 1109   | No file  | `e4efd28cf73f`  |
| 1102   | No file  | `e4efd28cf73f`  |
| 1096   | No file  | `e4efd28cf73f`  |
| 1088   | No file  | `e4efd28cf73f`  |
| 1081   | No file  | `e4efd28cf73f`  |
| 1076   | No file  | `e4efd28cf73f`  |
| 1069   | No file  | `e4efd28cf73f`  |
| 1064   | No file  | `e4efd28cf73f`  |
| 1058   | No file  | `e4efd28cf73f`  |
| 1051   | No file  | `e4efd28cf73f`  |
| 1044   | No file  | `e4efd28cf73f`  |
| 1036   | No file  | `e4efd28cf73f`  |
| 1026   | No file  | `e4efd28cf73f`  |
| 1016   | No file  | `e4efd28cf73f`  |
| 1009   | No file  | `e4efd28cf73f`  |
| 1005   | No file  | `e4efd28cf73f`  |
| 1000   | No file  | `e4efd28cf73f`  |
| 998    | No file  | `e4efd28cf73f`  |
| 990    | No file  | `e4efd28cf73f`  |
| 979    | No file  | `e4efd28cf73f`  |
| 972    | No file  | `e4efd28cf73f`  |
| 963    | No file  | `e4efd28cf73f`  |
| 955    | No file  | `e4efd28cf73f`  |
| 946    | No file  | `e4efd28cf73f`  |
| 938    | No file  | `e4efd28cf73f`  |
| 927    | No file  | `e4efd28cf73f`  |
| 911    | No file  | `e4efd28cf73f`  |
| 904    | No file  | `e4efd28cf73f`  |
| 899    | No file  | `e4efd28cf73f`  |
| 894    | No file  | `e4efd28cf73f`  |
| 885    | No file  | `e4efd28cf73f`  |
| 879    | No file  | `e4efd28cf73f`  |
| 872    | No file  | `e4efd28cf73f`  |
| 864    | No file  | `e4efd28cf73f`  |
| 855    | No file  | `e4efd28cf73f`  |
| 853    | No file  | `e4efd28cf73f`  |
| 845    | No file  | `e4efd28cf73f`  |
| 837    | No file  | `e4efd28cf73f`  |
| 829    | No file  | `e4efd28cf73f`  |
| 822    | No file  | `e4efd28cf73f`  |
| 814    | No file  | `e4efd28cf73f`  |
| 805    | No file  | `e4efd28cf73f`  |
| 794    | No file  | `e4efd28cf73f`  |
| 787    | No file  | `e4efd28cf73f`  |
| 780    | No file  | `e4efd28cf73f`  |
| 771    | No file  | `e4efd28cf73f`  |
| 760    | No file  | `e4efd28cf73f`  |
| 748    | No file  | `e4efd28cf73f`  |
| 741    | No file  | `e4efd28cf73f`  |
| 736    | No file  | `e4efd28cf73f`  |
| 731    | No file  | `e4efd28cf73f`  |
| 723    | No file  | `e4efd28cf73f`  |
| 711    | No file  | `e4efd28cf73f`  |
| 707    | No file  | `e4efd28cf73f`  |
| 697    | No file  | `e4efd28cf73f`  |
| 689    | No file  | `e4efd28cf73f`  |
| 683    | No file  | `e4efd28cf73f`  |
| 678    | No file  | `e4efd28cf73f`  |
| 670    | No file  | `e4efd28cf73f`  |
| 661    | No file  | `e4efd28cf73f`  |
| 656    | No file  | `e4efd28cf73f`  |
| 652    | No file  | `e4efd28cf73f`  |
| 643    | No file  | `e4efd28cf73f`  |
| 637    | No file  | `e4efd28cf73f`  |
| 630    | No file  | `e4efd28cf73f`  |
| 627    | No file  | `e4efd28cf73f`  |
| 621    | No file  | `e4efd28cf73f`  |
| 617    | No file  | `e4efd28cf73f`  |
| 615    | No file  | `e4efd28cf73f`  |
| 606    | No file  | `e4efd28cf73f`  |
| 599    | No file  | `e4efd28cf73f`  |
| 592    | No file  | `e4efd28cf73f`  |
| 586    | No file  | `e4efd28cf73f`  |
| 577    | No file  | `e4efd28cf73f`  |
| 569    | No file  | `e4efd28cf73f`  |
| 561    | No file  | `e4efd28cf73f`  |
| 554    | No file  | `e4efd28cf73f`  |
| 542    | No file  | `e4efd28cf73f`  |
| 532    | No file  | `e4efd28cf73f`  |
| 531    | No file  | `e4efd28cf73f`  |
| 526    | No file  | `e4efd28cf73f`  |
| 521    | No file  | `e4efd28cf73f`  |
| 517    | No file  | `e4efd28cf73f`  |
| 510    | No file  | `e4efd28cf73f`  |
| 508    | No file  | `e4efd28cf73f`  |
| 504    | No file  | `e4efd28cf73f`  |
| 497    | No file  | `e4efd28cf73f`  |
| 491    | No file  | `e4efd28cf73f`  |
| 485    | No file  | `e4efd28cf73f`  |
| 478    | No file  | `e4efd28cf73f`  |
| 472    | No file  | `e4efd28cf73f`  |
| 466    | No file  | `e4efd28cf73f`  |
| 457    | No file  | `e4efd28cf73f`  |
| 452    | No file  | `e4efd28cf73f`  |
| 449    | No file  | `e4efd28cf73f`  |
| 435    | No file  | `e4efd28cf73f`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                    |
| ---------------------------- | -------- | --------------------------------------------------------------------------------------- |
| `mansiondataoffset.dbss`     | Optional | `character_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a key without a row shows as plain text              |
| `languagedata_en.loc`        | Optional | Furniture names, LOC type 6                                                              |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3482 the file is 4 + 498 x 6 = 2,992 bytes.

### Row (6 bytes)

| Offset  | Type | Field             | Notes                                                               |
| ------- | ---- | ----------------- | ------------------------------------------------------------------- |
| `+0x00` | u16  | character_key     | Row key: the furniture installation, a `characterstatic.dbss` character |
| `+0x02` | u16  | character_key_dup | Equal to `character_key` on every row; the offset index points here |
| `+0x04` | u8   | unknown_04        | `1` on every row (clients 1784 and 3482); see Open Questions        |
| `+0x05` | u8   | unknown_05        | `0` on every row (clients 1784 and 3482); see Open Questions        |

The rows are in no key order; client 3482 opens with 4398, 4454, 4390.

### `mansiondataoffset.dbss`

Bare offset table into `mansiondata.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `mansiondata.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                 |
| ------- | ---- | ------------- | ----------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                           |
| `+0x02` | u32  | data_offset   | Row start + 2, at `character_key_dup`                 |
| `+0x06` | u32  | data_size     | `4` on every row: the row less its key                |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3482 every
index row points at the row with its key.

## Field Names

The `MansionData_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CharacterKey`, `Type`, `Kind` and
`ContentsGroupKey`, 304 rows: `character_key` matches `CharacterKey` on 304
of 304. Every row of the sheet holds `Type` `1`, `Kind` `2` and
`ContentsGroupKey` `1622`. The 2016 client's debug symbols have no struct
for the table.

## Notes

- The client Lua asks whether an item is manor furniture through
  `ToClient_isMansionInstallationItem()`; no Lua call reads a field of this
  table.

## Open Questions

### What the Two u8 Fields Hold

`unknown_04` is `1` and `unknown_05` is `0` on every row of clients 1784
and 3482. The sheet's `Type` (`1` on every row) is a lead for
`unknown_04`, but a match on one constant value does not fix the column,
and `Kind` (`2` on every row) matches neither field.
