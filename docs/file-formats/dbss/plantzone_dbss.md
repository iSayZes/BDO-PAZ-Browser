# `plantzone.dbss` Format

## Purpose

Defines worker production zones. Each record belongs to one worldmap production sub-node (`record_id` is an `exploration.bss` node key, named through LOC type 29), stores the worker's work animation type, links to a production key in `plantexchangegroup.bss` with a capacity level, and lists a set of worker species per zone (not a worker lock; its use is unknown, see Open Questions). `plantzoneoffset.dbss` is required to address the variable-length records.

Observed records: 394 in the pre-2026-09-27 fixture, 439 in the 2026-09-27 client (45 more 37-byte zones). Record payloads are 32, 34, or 37 bytes depending on the worker-species list length.

The production-key reading and the worker-species field boundaries follow [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, "Worker-production item tables"), checked against the current client files below.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes  | Records               | Row bytes               |
| ------ | -------------- | ---------------------- | ------ | --------------------- | ----------------------- |
| 2      | 2142 and later | `plantzone.dbss`       | 16,111 | 439 Plant Zone Record | 32 to 37, 37 on average |
| 2      | 2142 and later | `plantzoneoffset.dbss` | 5,272  | 439 Offset Row        | 12                      |
| 1      | 1261 to 2138   | `plantzone.dbss`       | 8,725  | 323 Plant Zone Record | 27                      |
| 1      | 1261 to 2138   | `plantzoneoffset.dbss` | 3,880  | 323 Offset Row        | 12                      |

| Layout | File                   | Known            | Unknown         |
| ------ | ---------------------- | ---------------- | --------------- |
| 2      | `plantzone.dbss`       | 11,721 B (72.8%) | 4,390 B (27.2%) |
| 2      | `plantzoneoffset.dbss` | 4,394 B (83.3%)  | 878 B (16.7%)   |
| 1      | `plantzone.dbss`       | 5,495 B (63.0%)  | 3,230 B (37.0%) |
| 1      | `plantzoneoffset.dbss` | 3,234 B (83.4%)  | 646 B (16.6%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `e6b0bcf19251`  |
| 3482   | Layout 2 | `e6b0bcf19251`  |
| 3474   | Layout 2 | `e6b0bcf19251`  |
| 3473   | Layout 2 | `e6b0bcf19251`  |
| 3464   | Layout 2 | `e6b0bcf19251`  |
| 3458   | Layout 2 | `e6b0bcf19251`  |
| 3454   | Layout 2 | `e6b0bcf19251`  |
| 3444   | Layout 2 | `e6b0bcf19251`  |
| 3435   | Layout 2 | `e6b0bcf19251`  |
| 3426   | Layout 2 | `e6b0bcf19251`  |
| 3418   | Layout 2 | `e6b0bcf19251`  |
| 3412   | Layout 2 | `e6b0bcf19251`  |
| 3402   | Layout 2 | `e6b0bcf19251`  |
| 3396   | Layout 2 | `e6b0bcf19251`  |
| 3387   | Layout 2 | `e6b0bcf19251`  |
| 3381   | Layout 2 | `e6b0bcf19251`  |
| 3373   | Layout 2 | `e6b0bcf19251`  |
| 3364   | Layout 2 | `e6b0bcf19251`  |
| 3356   | Layout 2 | `e6b0bcf19251`  |
| 3349   | Layout 2 | `e6b0bcf19251`  |
| 3342   | Layout 2 | `e6b0bcf19251`  |
| 3335   | Layout 2 | `e6b0bcf19251`  |
| 3326   | Layout 2 | `e6b0bcf19251`  |
| 3321   | Layout 2 | `e6b0bcf19251`  |
| 3314   | Layout 2 | `e6b0bcf19251`  |
| 3303   | Layout 2 | `e6b0bcf19251`  |
| 3302   | Layout 2 | `e6b0bcf19251`  |
| 3293   | Layout 2 | `e6b0bcf19251`  |
| 3283   | Layout 2 | `e6b0bcf19251`  |
| 3275   | Layout 2 | `e6b0bcf19251`  |
| 3267   | Layout 2 | `e6b0bcf19251`  |
| 3258   | Layout 2 | `e6b0bcf19251`  |
| 3251   | Layout 2 | `e6b0bcf19251`  |
| 3242   | Layout 2 | `e6b0bcf19251`  |
| 3235   | Layout 2 | `e6b0bcf19251`  |
| 3229   | Layout 2 | `e6b0bcf19251`  |
| 3212   | Layout 2 | `e6b0bcf19251`  |
| 3203   | Layout 2 | `e6b0bcf19251`  |
| 3193   | Layout 2 | `e6b0bcf19251`  |
| 3186   | Layout 2 | `e6b0bcf19251`  |
| 3177   | Layout 2 | `e6b0bcf19251`  |
| 3169   | Layout 2 | `e6b0bcf19251`  |
| 3158   | Layout 2 | `e6b0bcf19251`  |
| 3151   | Layout 2 | `e6b0bcf19251`  |
| 3144   | Layout 2 | `e6b0bcf19251`  |
| 3133   | Layout 2 | `e6b0bcf19251`  |
| 3125   | Layout 2 | `e6b0bcf19251`  |
| 3118   | Layout 2 | `e6b0bcf19251`  |
| 3111   | Layout 2 | `e6b0bcf19251`  |
| 3103   | Layout 2 | `e6b0bcf19251`  |
| 3095   | Layout 2 | `e6b0bcf19251`  |
| 3086   | Layout 2 | `e6b0bcf19251`  |
| 3072   | Layout 2 | `e6b0bcf19251`  |
| 3062   | Layout 2 | `e6b0bcf19251`  |
| 3052   | Layout 2 | `e6b0bcf19251`  |
| 3045   | Layout 2 | `e6b0bcf19251`  |
| 3037   | Layout 2 | `e6b0bcf19251`  |
| 3030   | Layout 2 | `e6b0bcf19251`  |
| 3021   | Layout 2 | `e6b0bcf19251`  |
| 3012   | Layout 2 | `e6b0bcf19251`  |
| 3002   | Layout 2 | `e6b0bcf19251`  |
| 2995   | Layout 2 | `e6b0bcf19251`  |
| 2987   | Layout 2 | `e6b0bcf19251`  |
| 2978   | Layout 2 | `e6b0bcf19251`  |
| 2970   | Layout 2 | `e6b0bcf19251`  |
| 2959   | Layout 2 | `e6b0bcf19251`  |
| 2951   | Layout 2 | `e6b0bcf19251`  |
| 2942   | Layout 2 | `e6b0bcf19251`  |
| 2935   | Layout 2 | `e6b0bcf19251`  |
| 2932   | Layout 2 | `e6b0bcf19251`  |
| 2923   | Layout 2 | `e6b0bcf19251`  |
| 2919   | Layout 2 | `e6b0bcf19251`  |
| 2907   | Layout 2 | `e6b0bcf19251`  |
| 2900   | Layout 2 | `e6b0bcf19251`  |
| 2891   | Layout 2 | `e6b0bcf19251`  |
| 2882   | Layout 2 | `e6b0bcf19251`  |
| 2872   | Layout 2 | `e6b0bcf19251`  |
| 2863   | Layout 2 | `e6b0bcf19251`  |
| 2855   | Layout 2 | `e6b0bcf19251`  |
| 2849   | Layout 2 | `e6b0bcf19251`  |
| 2844   | Layout 2 | `e6b0bcf19251`  |
| 2834   | Layout 2 | `e6b0bcf19251`  |
| 2825   | Layout 2 | `e6b0bcf19251`  |
| 2819   | Layout 2 | `e6b0bcf19251`  |
| 2811   | Layout 2 | `e6b0bcf19251`  |
| 2803   | Layout 2 | `e6b0bcf19251`  |
| 2794   | Layout 2 | `e6b0bcf19251`  |
| 2783   | Layout 2 | `e6b0bcf19251`  |
| 2774   | Layout 2 | `e6b0bcf19251`  |
| 2765   | Layout 2 | `e6b0bcf19251`  |
| 2756   | Layout 2 | `e6b0bcf19251`  |
| 2750   | Layout 2 | `e6b0bcf19251`  |
| 2743   | Layout 2 | `e6b0bcf19251`  |
| 2736   | Layout 2 | `e6b0bcf19251`  |
| 2726   | Layout 2 | `e6b0bcf19251`  |
| 2717   | Layout 2 | `e6b0bcf19251`  |
| 2709   | Layout 2 | `e6b0bcf19251`  |
| 2703   | Layout 2 | `e6b0bcf19251`  |
| 2695   | Layout 2 | `e6b0bcf19251`  |
| 2684   | Layout 2 | `e6b0bcf19251`  |
| 2672   | Layout 2 | `e6b0bcf19251`  |
| 2665   | Layout 2 | `e6b0bcf19251`  |
| 2657   | Layout 2 | `e6b0bcf19251`  |
| 2649   | Layout 2 | `e6b0bcf19251`  |
| 2644   | Layout 2 | `e6b0bcf19251`  |
| 2637   | Layout 2 | `e6b0bcf19251`  |
| 2629   | Layout 2 | `e6b0bcf19251`  |
| 2619   | Layout 2 | `e6b0bcf19251`  |
| 2612   | Layout 2 | `e6b0bcf19251`  |
| 2606   | Layout 2 | `e6b0bcf19251`  |
| 2602   | Layout 2 | `e6b0bcf19251`  |
| 2601   | Layout 2 | `e6b0bcf19251`  |
| 2592   | Layout 2 | `e6b0bcf19251`  |
| 2583   | Layout 2 | `e6b0bcf19251`  |
| 2575   | Layout 2 | `e6b0bcf19251`  |
| 2567   | Layout 2 | `e6b0bcf19251`  |
| 2560   | Layout 2 | `e6b0bcf19251`  |
| 2553   | Layout 2 | `e6b0bcf19251`  |
| 2545   | Layout 2 | `e6b0bcf19251`  |
| 2538   | Layout 2 | `e6b0bcf19251`  |
| 2529   | Layout 2 | `e6b0bcf19251`  |
| 2519   | Layout 2 | `e6b0bcf19251`  |
| 2513   | Layout 2 | `e6b0bcf19251`  |
| 2510   | Layout 2 | `e6b0bcf19251`  |
| 2507   | Layout 2 | `e6b0bcf19251`  |
| 2503   | Layout 2 | `e6b0bcf19251`  |
| 2498   | Layout 2 | `e6b0bcf19251`  |
| 2492   | Layout 2 | `e6b0bcf19251`  |
| 2487   | Layout 2 | `e6b0bcf19251`  |
| 2480   | Layout 2 | `e6b0bcf19251`  |
| 2474   | Layout 2 | `e6b0bcf19251`  |
| 2468   | Layout 2 | `e6b0bcf19251`  |
| 2460   | Layout 2 | `e6b0bcf19251`  |
| 2453   | Layout 2 | `e6b0bcf19251`  |
| 2444   | Layout 2 | `e6b0bcf19251`  |
| 2438   | Layout 2 | `e6b0bcf19251`  |
| 2434   | Layout 2 | `e6b0bcf19251`  |
| 2429   | Layout 2 | `e6b0bcf19251`  |
| 2421   | Layout 2 | `e6b0bcf19251`  |
| 2414   | Layout 2 | `e6b0bcf19251`  |
| 2407   | Layout 2 | `e6b0bcf19251`  |
| 2401   | Layout 2 | `e6b0bcf19251`  |
| 2397   | Layout 2 | `e6b0bcf19251`  |
| 2393   | Layout 2 | `e6b0bcf19251`  |
| 2384   | Layout 2 | `e6b0bcf19251`  |
| 2378   | Layout 2 | `e6b0bcf19251`  |
| 2372   | Layout 2 | `e6b0bcf19251`  |
| 2358   | Layout 2 | `e6b0bcf19251`  |
| 2352   | Layout 2 | `e6b0bcf19251`  |
| 2347   | Layout 2 | `e6b0bcf19251`  |
| 2343   | Layout 2 | `e6b0bcf19251`  |
| 2335   | Layout 2 | `e6b0bcf19251`  |
| 2327   | Layout 2 | `e6b0bcf19251`  |
| 2324   | Layout 2 | `e6b0bcf19251`  |
| 2319   | Layout 2 | `e6b0bcf19251`  |
| 2313   | Layout 2 | `e6b0bcf19251`  |
| 2308   | Layout 2 | `e6b0bcf19251`  |
| 2302   | Layout 2 | `e6b0bcf19251`  |
| 2295   | Layout 2 | `e6b0bcf19251`  |
| 2290   | Layout 2 | `e6b0bcf19251`  |
| 2284   | Layout 2 | `e6b0bcf19251`  |
| 2276   | Layout 2 | `e6b0bcf19251`  |
| 2269   | Layout 2 | `e6b0bcf19251`  |
| 2259   | Layout 2 | `e6b0bcf19251`  |
| 2250   | Layout 2 | `e6b0bcf19251`  |
| 2243   | Layout 2 | `e6b0bcf19251`  |
| 2235   | Layout 2 | `e6b0bcf19251`  |
| 2229   | Layout 2 | `e6b0bcf19251`  |
| 2224   | Layout 2 | `e6b0bcf19251`  |
| 2218   | Layout 2 | `e6b0bcf19251`  |
| 2215   | Layout 2 | `e6b0bcf19251`  |
| 2207   | Layout 2 | `e6b0bcf19251`  |
| 2203   | Layout 2 | `e6b0bcf19251`  |
| 2196   | Layout 2 | `e6b0bcf19251`  |
| 2192   | Layout 2 | `e6b0bcf19251`  |
| 2189   | Layout 2 | `e6b0bcf19251`  |
| 2183   | Layout 2 | `e6b0bcf19251`  |
| 2179   | Layout 2 | `e6b0bcf19251`  |
| 2171   | Layout 2 | `e6b0bcf19251`  |
| 2163   | Layout 2 | `e6b0bcf19251`  |
| 2156   | Layout 2 | `e6b0bcf19251`  |
| 2151   | Layout 2 | `e6b0bcf19251`  |
| 2147   | Layout 2 | `e6b0bcf19251`  |
| 2142   | Layout 2 | `e6b0bcf19251`  |
| 2138   | Layout 1 | `e6b0bcf19251`  |
| 2134   | Layout 1 | `e6b0bcf19251`  |
| 2130   | Layout 1 | `e6b0bcf19251`  |
| 2122   | Layout 1 | `e6b0bcf19251`  |
| 2107   | Layout 1 | `e6b0bcf19251`  |
| 2098   | Layout 1 | `e6b0bcf19251`  |
| 2089   | Layout 1 | `e6b0bcf19251`  |
| 2081   | Layout 1 | `e6b0bcf19251`  |
| 2073   | Layout 1 | `e6b0bcf19251`  |
| 2067   | Layout 1 | `e6b0bcf19251`  |
| 2063   | Layout 1 | `e6b0bcf19251`  |
| 2059   | Layout 1 | `e6b0bcf19251`  |
| 2052   | Layout 1 | `e6b0bcf19251`  |
| 2044   | Layout 1 | `e6b0bcf19251`  |
| 2039   | Layout 1 | `e6b0bcf19251`  |
| 2032   | Layout 1 | `e6b0bcf19251`  |
| 2025   | Layout 1 | `e6b0bcf19251`  |
| 2011   | Layout 1 | `e6b0bcf19251`  |
| 2005   | Layout 1 | `e6b0bcf19251`  |
| 2000   | Layout 1 | `e6b0bcf19251`  |
| 1996   | Layout 1 | `e6b0bcf19251`  |
| 1991   | Layout 1 | `e6b0bcf19251`  |
| 1985   | Layout 1 | `e6b0bcf19251`  |
| 1980   | Layout 1 | `e6b0bcf19251`  |
| 1969   | Layout 1 | `e6b0bcf19251`  |
| 1964   | Layout 1 | `e6b0bcf19251`  |
| 1958   | Layout 1 | `e6b0bcf19251`  |
| 1950   | Layout 1 | `e6b0bcf19251`  |
| 1945   | Layout 1 | `e6b0bcf19251`  |
| 1937   | Layout 1 | `e6b0bcf19251`  |
| 1933   | Layout 1 | `e6b0bcf19251`  |
| 1927   | Layout 1 | `e6b0bcf19251`  |
| 1921   | Layout 1 | `e6b0bcf19251`  |
| 1914   | Layout 1 | `e6b0bcf19251`  |
| 1908   | Layout 1 | `e6b0bcf19251`  |
| 1897   | Layout 1 | `e6b0bcf19251`  |
| 1892   | Layout 1 | `e6b0bcf19251`  |
| 1886   | Layout 1 | `e6b0bcf19251`  |
| 1881   | Layout 1 | `e6b0bcf19251`  |
| 1871   | Layout 1 | `e6b0bcf19251`  |
| 1866   | Layout 1 | `e6b0bcf19251`  |
| 1862   | Layout 1 | `e6b0bcf19251`  |
| 1854   | Layout 1 | `e6b0bcf19251`  |
| 1846   | Layout 1 | `e6b0bcf19251`  |
| 1838   | Layout 1 | `e6b0bcf19251`  |
| 1832   | Layout 1 | `e6b0bcf19251`  |
| 1826   | Layout 1 | `e6b0bcf19251`  |
| 1822   | Layout 1 | `e6b0bcf19251`  |
| 1818   | Layout 1 | `e6b0bcf19251`  |
| 1804   | Layout 1 | `e6b0bcf19251`  |
| 1794   | Layout 1 | `e6b0bcf19251`  |
| 1790   | Layout 1 | `e6b0bcf19251`  |
| 1784   | Layout 1 | `e6b0bcf19251`  |
| 1774   | Layout 1 | `e6b0bcf19251`  |
| 1771   | Layout 1 | `e6b0bcf19251`  |
| 1762   | Layout 1 | `e6b0bcf19251`  |
| 1759   | Layout 1 | `e6b0bcf19251`  |
| 1754   | Layout 1 | `e6b0bcf19251`  |
| 1749   | Layout 1 | `e6b0bcf19251`  |
| 1743   | Layout 1 | `e6b0bcf19251`  |
| 1737   | Layout 1 | `e6b0bcf19251`  |
| 1731   | Layout 1 | `e6b0bcf19251`  |
| 1725   | Layout 1 | `e6b0bcf19251`  |
| 1717   | Layout 1 | `e6b0bcf19251`  |
| 1710   | Layout 1 | `e6b0bcf19251`  |
| 1704   | Layout 1 | `e6b0bcf19251`  |
| 1698   | Layout 1 | `e6b0bcf19251`  |
| 1690   | Layout 1 | `e6b0bcf19251`  |
| 1685   | Layout 1 | `e6b0bcf19251`  |
| 1680   | Layout 1 | `e6b0bcf19251`  |
| 1674   | Layout 1 | `e6b0bcf19251`  |
| 1668   | Layout 1 | `e6b0bcf19251`  |
| 1659   | Layout 1 | `e6b0bcf19251`  |
| 1649   | Layout 1 | `e6b0bcf19251`  |
| 1642   | Layout 1 | `e6b0bcf19251`  |
| 1636   | Layout 1 | `e6b0bcf19251`  |
| 1628   | Layout 1 | `e6b0bcf19251`  |
| 1622   | Layout 1 | `e6b0bcf19251`  |
| 1614   | Layout 1 | `e6b0bcf19251`  |
| 1608   | Layout 1 | `e6b0bcf19251`  |
| 1602   | Layout 1 | `e6b0bcf19251`  |
| 1598   | Layout 1 | `e6b0bcf19251`  |
| 1594   | Layout 1 | `e6b0bcf19251`  |
| 1590   | Layout 1 | `e6b0bcf19251`  |
| 1587   | Layout 1 | `e6b0bcf19251`  |
| 1584   | Layout 1 | `e6b0bcf19251`  |
| 1579   | Layout 1 | `e6b0bcf19251`  |
| 1572   | Layout 1 | `e6b0bcf19251`  |
| 1565   | Layout 1 | `e6b0bcf19251`  |
| 1559   | Layout 1 | `e6b0bcf19251`  |
| 1554   | Layout 1 | `e6b0bcf19251`  |
| 1547   | Layout 1 | `e6b0bcf19251`  |
| 1537   | Layout 1 | `e6b0bcf19251`  |
| 1529   | Layout 1 | `e6b0bcf19251`  |
| 1524   | Layout 1 | `e6b0bcf19251`  |
| 1519   | Layout 1 | `e6b0bcf19251`  |
| 1509   | Layout 1 | `e6b0bcf19251`  |
| 1506   | Layout 1 | `e6b0bcf19251`  |
| 1504   | Layout 1 | `e6b0bcf19251`  |
| 1500   | Layout 1 | `e6b0bcf19251`  |
| 1493   | Layout 1 | `e6b0bcf19251`  |
| 1489   | Layout 1 | `e6b0bcf19251`  |
| 1485   | Layout 1 | `e6b0bcf19251`  |
| 1481   | Layout 1 | `e6b0bcf19251`  |
| 1474   | Layout 1 | `e6b0bcf19251`  |
| 1466   | Layout 1 | `e6b0bcf19251`  |
| 1462   | Layout 1 | `e6b0bcf19251`  |
| 1459   | Layout 1 | `e6b0bcf19251`  |
| 1453   | Layout 1 | `e6b0bcf19251`  |
| 1450   | Layout 1 | `e6b0bcf19251`  |
| 1445   | Layout 1 | `e6b0bcf19251`  |
| 1439   | Layout 1 | `e6b0bcf19251`  |
| 1433   | Layout 1 | `e6b0bcf19251`  |
| 1430   | Layout 1 | `e6b0bcf19251`  |
| 1426   | Layout 1 | `e6b0bcf19251`  |
| 1421   | Layout 1 | `e6b0bcf19251`  |
| 1417   | Layout 1 | `e6b0bcf19251`  |
| 1416   | Layout 1 | `e6b0bcf19251`  |
| 1409   | Layout 1 | `e6b0bcf19251`  |
| 1405   | Layout 1 | `e6b0bcf19251`  |
| 1401   | Layout 1 | `e6b0bcf19251`  |
| 1396   | Layout 1 | `e6b0bcf19251`  |
| 1391   | Layout 1 | `e6b0bcf19251`  |
| 1390   | Layout 1 | `e6b0bcf19251`  |
| 1386   | Layout 1 | `e6b0bcf19251`  |
| 1381   | Layout 1 | `e6b0bcf19251`  |
| 1379   | Layout 1 | `e6b0bcf19251`  |
| 1372   | Layout 1 | `e6b0bcf19251`  |
| 1366   | Layout 1 | `e6b0bcf19251`  |
| 1364   | Layout 1 | `e6b0bcf19251`  |
| 1363   | Layout 1 | `e6b0bcf19251`  |
| 1360   | Layout 1 | `e6b0bcf19251`  |
| 1358   | Layout 1 | `e6b0bcf19251`  |
| 1355   | Layout 1 | `e6b0bcf19251`  |
| 1351   | Layout 1 | `e6b0bcf19251`  |
| 1348   | Layout 1 | `e6b0bcf19251`  |
| 1346   | Layout 1 | `e6b0bcf19251`  |
| 1341   | Layout 1 | `e6b0bcf19251`  |
| 1340   | Layout 1 | `e6b0bcf19251`  |
| 1338   | Layout 1 | `e6b0bcf19251`  |
| 1335   | Layout 1 | `e6b0bcf19251`  |
| 1333   | Layout 1 | `e6b0bcf19251`  |
| 1329   | Layout 1 | `e6b0bcf19251`  |
| 1327   | Layout 1 | `e6b0bcf19251`  |
| 1324   | Layout 1 | `e6b0bcf19251`  |
| 1321   | Layout 1 | `e6b0bcf19251`  |
| 1319   | Layout 1 | `e6b0bcf19251`  |
| 1318   | Layout 1 | `e6b0bcf19251`  |
| 1316   | Layout 1 | `e6b0bcf19251`  |
| 1313   | Layout 1 | `e6b0bcf19251`  |
| 1311   | Layout 1 | `e6b0bcf19251`  |
| 1309   | Layout 1 | `e6b0bcf19251`  |
| 1304   | Layout 1 | `e6b0bcf19251`  |
| 1292   | Layout 1 | `e6b0bcf19251`  |
| 1286   | Layout 1 | `e6b0bcf19251`  |
| 1280   | Layout 1 | `e6b0bcf19251`  |
| 1276   | Layout 1 | `e6b0bcf19251`  |
| 1267   | Layout 1 | `e6b0bcf19251`  |
| 1261   | Layout 1 | `e6b0bcf19251`  |
| 1256   | No file  | `e6b0bcf19251`  |
| 1250   | No file  | `e6b0bcf19251`  |
| 1246   | No file  | `e6b0bcf19251`  |
| 1239   | No file  | `e6b0bcf19251`  |
| 1230   | No file  | `e6b0bcf19251`  |
| 1226   | No file  | `e6b0bcf19251`  |
| 1220   | No file  | `e6b0bcf19251`  |
| 1217   | No file  | `e6b0bcf19251`  |
| 1211   | No file  | `e6b0bcf19251`  |
| 1210   | No file  | `e6b0bcf19251`  |
| 1208   | No file  | `e6b0bcf19251`  |
| 1203   | No file  | `e6b0bcf19251`  |
| 1197   | No file  | `e6b0bcf19251`  |
| 1194   | No file  | `e6b0bcf19251`  |
| 1192   | No file  | `e6b0bcf19251`  |
| 1187   | No file  | `e6b0bcf19251`  |
| 1183   | No file  | `e6b0bcf19251`  |
| 1177   | No file  | `e6b0bcf19251`  |
| 1173   | No file  | `e6b0bcf19251`  |
| 1167   | No file  | `e6b0bcf19251`  |
| 1164   | No file  | `e6b0bcf19251`  |
| 1156   | No file  | `e6b0bcf19251`  |
| 1149   | No file  | `e6b0bcf19251`  |
| 1144   | No file  | `e6b0bcf19251`  |
| 1137   | No file  | `e6b0bcf19251`  |
| 1132   | No file  | `e6b0bcf19251`  |
| 1127   | No file  | `e6b0bcf19251`  |
| 1122   | No file  | `e6b0bcf19251`  |
| 1118   | No file  | `e6b0bcf19251`  |
| 1114   | No file  | `e6b0bcf19251`  |
| 1109   | No file  | `e6b0bcf19251`  |
| 1102   | No file  | `e6b0bcf19251`  |
| 1096   | No file  | `e6b0bcf19251`  |
| 1088   | No file  | `e6b0bcf19251`  |
| 1081   | No file  | `e6b0bcf19251`  |
| 1076   | No file  | `e6b0bcf19251`  |
| 1069   | No file  | `e6b0bcf19251`  |
| 1064   | No file  | `e6b0bcf19251`  |
| 1058   | No file  | `e6b0bcf19251`  |
| 1051   | No file  | `e6b0bcf19251`  |
| 1044   | No file  | `e6b0bcf19251`  |
| 1036   | No file  | `e6b0bcf19251`  |
| 1026   | No file  | `e6b0bcf19251`  |
| 1016   | No file  | `e6b0bcf19251`  |
| 1009   | No file  | `e6b0bcf19251`  |
| 1005   | No file  | `e6b0bcf19251`  |
| 1000   | No file  | `e6b0bcf19251`  |
| 998    | No file  | `e6b0bcf19251`  |
| 990    | No file  | `e6b0bcf19251`  |
| 979    | No file  | `e6b0bcf19251`  |
| 972    | No file  | `e6b0bcf19251`  |
| 963    | No file  | `e6b0bcf19251`  |
| 955    | No file  | `e6b0bcf19251`  |
| 946    | No file  | `e6b0bcf19251`  |
| 938    | No file  | `e6b0bcf19251`  |
| 927    | No file  | `e6b0bcf19251`  |
| 911    | No file  | `e6b0bcf19251`  |
| 904    | No file  | `e6b0bcf19251`  |
| 899    | No file  | `e6b0bcf19251`  |
| 894    | No file  | `e6b0bcf19251`  |
| 885    | No file  | `e6b0bcf19251`  |
| 879    | No file  | `e6b0bcf19251`  |
| 872    | No file  | `e6b0bcf19251`  |
| 864    | No file  | `e6b0bcf19251`  |
| 855    | No file  | `e6b0bcf19251`  |
| 853    | No file  | `e6b0bcf19251`  |
| 845    | No file  | `e6b0bcf19251`  |
| 837    | No file  | `e6b0bcf19251`  |
| 829    | No file  | `e6b0bcf19251`  |
| 822    | No file  | `e6b0bcf19251`  |
| 814    | No file  | `e6b0bcf19251`  |
| 805    | No file  | `e6b0bcf19251`  |
| 794    | No file  | `e6b0bcf19251`  |
| 787    | No file  | `e6b0bcf19251`  |
| 780    | No file  | `e6b0bcf19251`  |
| 771    | No file  | `e6b0bcf19251`  |
| 760    | No file  | `e6b0bcf19251`  |
| 748    | No file  | `e6b0bcf19251`  |
| 741    | No file  | `e6b0bcf19251`  |
| 736    | No file  | `e6b0bcf19251`  |
| 731    | No file  | `e6b0bcf19251`  |
| 723    | No file  | `e6b0bcf19251`  |
| 711    | No file  | `e6b0bcf19251`  |
| 707    | No file  | `e6b0bcf19251`  |
| 697    | No file  | `e6b0bcf19251`  |
| 689    | No file  | `e6b0bcf19251`  |
| 683    | No file  | `e6b0bcf19251`  |
| 678    | No file  | `e6b0bcf19251`  |
| 670    | No file  | `e6b0bcf19251`  |
| 661    | No file  | `e6b0bcf19251`  |
| 656    | No file  | `e6b0bcf19251`  |
| 652    | No file  | `e6b0bcf19251`  |
| 643    | No file  | `e6b0bcf19251`  |
| 637    | No file  | `e6b0bcf19251`  |
| 630    | No file  | `e6b0bcf19251`  |
| 627    | No file  | `e6b0bcf19251`  |
| 621    | No file  | `e6b0bcf19251`  |
| 617    | No file  | `e6b0bcf19251`  |
| 615    | No file  | `e6b0bcf19251`  |
| 606    | No file  | `e6b0bcf19251`  |
| 599    | No file  | `e6b0bcf19251`  |
| 592    | No file  | `e6b0bcf19251`  |
| 586    | No file  | `e6b0bcf19251`  |
| 577    | No file  | `e6b0bcf19251`  |
| 569    | No file  | `e6b0bcf19251`  |
| 561    | No file  | `e6b0bcf19251`  |
| 554    | No file  | `e6b0bcf19251`  |
| 542    | No file  | `e6b0bcf19251`  |
| 532    | No file  | `e6b0bcf19251`  |
| 531    | No file  | `e6b0bcf19251`  |
| 526    | No file  | `e6b0bcf19251`  |
| 521    | No file  | `e6b0bcf19251`  |
| 517    | No file  | `e6b0bcf19251`  |
| 510    | No file  | `e6b0bcf19251`  |
| 508    | No file  | `e6b0bcf19251`  |
| 504    | No file  | `e6b0bcf19251`  |
| 497    | No file  | `e6b0bcf19251`  |
| 491    | No file  | `e6b0bcf19251`  |
| 485    | No file  | `e6b0bcf19251`  |
| 478    | No file  | `e6b0bcf19251`  |
| 472    | No file  | `e6b0bcf19251`  |
| 466    | No file  | `e6b0bcf19251`  |
| 457    | No file  | `e6b0bcf19251`  |
| 452    | No file  | `e6b0bcf19251`  |
| 449    | No file  | `e6b0bcf19251`  |
| 435    | No file  | `e6b0bcf19251`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                   |
| ---------------------- | -------- | ------------------------------------------------------ |
| `plantzoneoffset.dbss` | Required | Maps `record_id` to byte offset and payload byte count |

All multi-byte values are little-endian unless noted otherwise.

## Layout 2

### File Layout

| Offset  | Type                             | Field         | Notes                                      |
| ------- | -------------------------------- | ------------- | ------------------------------------------ |
| `+0x00` | u32                              | record_count  | Number of records; observed `394` (2026-09-27 client: `439`) |
| `+0x04` | Plant Zone Record[record_count]  | record_stream | Variable-length records, packed back-to-back |

`(file_size - 4) / record_count` is not integral, so records must be sliced with `plantzoneoffset.dbss`.

### Plant Zone Record (variable: 31 bytes + species)

32, 34, or 37 bytes on the observed clients.

| Offset  | Type | Field                | Notes                                                                    |
| ------- | ---- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | record_id            | `exploration.bss` node key; matches `record_id` in `plantzoneoffset.dbss` |
| `+0x04` | u32  | unknown_04           | Always observed as `2`; see Open Questions                               |
| `+0x08` | u32  | unknown_08           | Always observed as `0`; see Open Questions                               |
| `+0x0C` | u16  | unknown_0c           | Always observed as `2`; see Open Questions                               |
| `+0x0E` | u8   | work_ani_type        | `gc::EWorkAniType`, see below                                            |
| `+0x0F` | u16  | productivity_upgrade_group_index | `PlantUpgradeParam_Table` index; always observed as `101`; note unaligned offset |
| `+0x11` | u16  | luck_productivity_upgrade_group_index | `PlantUpgradeParam_Table` index; always observed as `201`; note unaligned offset |
| `+0x13` | u32  | production_count     | Number of (`production_key`, `max_capacity_level`) pairs; always observed as `1`; note unaligned offset |
| `+0x17` | u16  | production_key       | `plantexchangegroup.bss` key; note unaligned offset                      |
| `+0x19` | u16  | max_capacity_level   | The sheet's `MaxCapacityLevel` minus 1; usually `0`, see below           |
| `+0x1B` | u32  | worker_species_count | Number of trailing `worker_species`; observed `1`, `3`, or `6`           |
| `+0x1F` | u8[worker_species_count] | worker_species | Worker species values, `worker_species_count` bytes; not a worker lock   |

`+0x13` to `+0x1A` is a list: the 2016 client keeps `_productionList`, a map from the exchange group key to a `ProductionInfo` with `_maxCountLevel`. Every zone lists one pair, so the offsets after it are fixed; the parser raises an error on a zone with another count. Earlier versions of this doc read `+0x17` as one u32 `production_key` with an unexplained high word; that high word is `max_capacity_level`. Earlier versions also called `work_ani_type` `variant` and `unknown_0e`.

Observed record-size distribution:

| Size | Count | `worker_species_count` | `worker_species`    | Zones                                     |
| ---- | ----- | ---------------------- | ------------------- | ----------------------------------------- |
| 32   | 2     | 1                      | `06`                | Dokkebi Forest excavation (1807, 1808)    |
| 34   | 42    | 3                      | `06 07 08`          | Land of the Morning Light production nodes |
| 37   | 350   | 6                      | `00 01 02 03 04 05` | All other zones                           |

### `plantzoneoffset.dbss`

Provides the byte ranges for records in `plantzone.dbss`.

| Offset  | Type                     | Field        | Notes                             |
| ------- | ------------------------ | ------------ | --------------------------------- |
| `+0x00` | u32                      | record_count | Must equal `plantzone.dbss` count |
| `+0x04` | Offset Row[record_count] | rows         | 12-byte rows repeated `count` times |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                             |
| ------- | ---- | ----------- | ------------------------------------------------- |
| `+0x00` | u16  | record_id   | Matches `plantzone.dbss` record `+0x00`           |
| `+0x02` | u16  | unknown_02  | Always `0`                                        |
| `+0x04` | u32  | data_offset | Absolute byte offset into `plantzone.dbss`        |
| `+0x08` | u32  | data_size   | Record payload byte count: `32`, `34`, or `37`    |

Offset rows are not sorted by `data_offset`, but sorted rows cover every byte from `plantzone.dbss +0x04` through EOF with no gaps or overlaps. The parser reads `record_id` and `unknown_02` as one u32 (`parse_bare_u32_offset_rows()`).

## Layout 1

On client 1784 a Plant Zone Record was 27 bytes: it ended after
`max_capacity_level`, without `worker_species_count` and `worker_species`.
Only the Plant Zone Record differs from Layout 2; every offset row's
`data_size` is `27`. On client 1784 the file holds 309 records.

### Plant Zone Record (27 bytes)

| Offset  | Type | Field                                 | Notes |
| ------- | ---- | ------------------------------------- | ----- |
| `+0x00` | u32  | record_id                             |       |
| `+0x04` | u32  | unknown_04                            |       |
| `+0x08` | u32  | unknown_08                            |       |
| `+0x0C` | u16  | unknown_0c                            |       |
| `+0x0E` | u8   | work_ani_type                         |       |
| `+0x0F` | u16  | productivity_upgrade_group_index      |       |
| `+0x11` | u16  | luck_productivity_upgrade_group_index |       |
| `+0x13` | u32  | production_count                      |       |
| `+0x17` | u16  | production_key                        |       |
| `+0x19` | u16  | max_capacity_level                    |       |

## `worker_species` Values

The same byte is the last byte (`+0x38F`) of every `plantworker.bss` record. Names below come from the LOC type 6 names of the workers carrying each value; the client enum for this byte was not found in `global_define_cpp_enum.luac`.

| Value | Workers                                                  |
| ----- | -------------------------------------------------------- |
| 0     | Goblin workers (plus named special workers such as Torres, Darifu) |
| 1     | Human workers (plus Demibeast workers)                   |
| 2     | Giant workers                                            |
| 3     | Papu workers                                             |
| 4     | Fadus workers                                            |
| 5     | Dwarf workers                                            |
| 6     | Dokkebi workers                                          |
| 7     | Dolswe workers                                           |
| 8     | Shellfolk workers                                        |

## `work_ani_type` Values

Names from `gc::EWorkAniType` of the 2016 client's debug symbols. On client 3473 the zones use `0` to `4`; the `exploration.bss` `node_kind` of each zone's node, counted per value:

| Value | Name         | Zones | Node kinds |
| ----- | ------------ | ----- | ---------- |
| 0     | Mining       | 84    | Quarry 79, MonopolyFarm 3, Excavation 1, Logging 1 |
| 1     | Gather       | 80    | Collect 46, Farm 15, Excavation 12, MonopolyFarm 4, Logging 2, Craft 1 |
| 2     | Cultivation  | 63    | Farm 35, Collect 13, MonopolyFarm 11, Quarry 2, Logging 2 |
| 3     | Logging      | 77    | Logging 73, Excavation 3, Quarry 1 |
| 4     | Making       | 135   | FishTrap 41, Excavation 34, MonopolyFarm 25, Finance 24, Craft 7, MinorFinance 2, Logging 1, Quarry 1 |
| 5     | Architecture | 0     | |
| 6     | Hide         | 0     | |
| 7     | HouseParty   | 0     | |
| 8     | Breeding     | 0     | |

The value does not follow the node kind: Farm nodes split between Gather and Cultivation, and Excavation nodes fall under four of the five.

## `max_capacity_level` Values

On client 3473, `max_capacity_level` is `0` on 420 zones and `1` to `7` on 19 (`node_kind` MonopolyFarm 15, Quarry 2, Collect 1, Excavation 1):

| `max_capacity_level` | Zones |
| -------------------- | ----- |
| `0`                  | 420   |
| `1`                  | 3     |
| `2`                  | 6     |
| `3`                  | 2     |
| `4`                  | 2     |
| `5`                  | 2     |
| `6`                  | 2     |
| `7`                  | 2     |

It counts up across consecutive Specialties (MonopolyFarm) node keys: 104-110 (Balenos farms such as Bartali, Finto and Wale Farm) carry `1`-`7`, and 613-619 (Calpheon farms such as Falres Dirt and Dias Farm) carry `1`-`7` again. All `production_key` values are `plantexchangegroup.bss` keys; read together with `max_capacity_level` as a u32, the 19 non-zero ones are not.

## Production Item Chain

```text
production_key -> plantexchangegroup.bss production_key (+0x00)
plantexchangegroup.bss exchange_key (+0x06) -> itemexchangesource.bss key
itemexchangesource.bss product_drop_key, luck_drop_key -> itemmaingroup.bss group_id
itemmaingroup.bss subgroup keys -> itemsubgroup.dbss entries -> item_key & 0xFFFFFF -> item name (LOC type 0)
```

The tables are documented in [plantexchangegroup_bss.md](../bss/plantexchangegroup_bss.md), [itemexchangesource_bss.md](../bss/itemexchangesource_bss.md), [itemmaingroup_bss.md](../bss/itemmaingroup_bss.md) and [itemsubgroup_dbss.md](itemsubgroup_dbss.md); row counts for the chain are in [`plantexchangegroup.bss` Field Names](../bss/plantexchangegroup_bss.md#field-names). The Produced Items column shows the product drop group, read from the `PRODUCTION_ITEMS` lookup index (see `docs/handler.md`), and the Luck Drops column the luck drop group, read from `PRODUCTION_LUCK_ITEMS`.

Example: zone 2050 (Lumbering) -> production key 1928 -> exchange 42356 -> product group 42356 -> subgroup 42356 -> Elder Tree Timber, Bloody Tree Knot, Elder Tree Sap. On client 3474 all 439 zones resolve to items, and 370 of them also have a luck drop group with items.

Earlier versions of the handler read `+0x06` as an `itemsubgroup.dbss` key, which left 36 zones without items: their exchange key has no subgroup of the same number. All 36 resolve through the exchange. Zone 2051 `Fish Drying Yard` (production key 1929, exchange 45018) is one of them: the exchange drops group 44064 (4 items) with luck group 41165 (2 items), the 4 items plus 2 lucky drops the zone produces in game.

## Field Names

The names of `work_ani_type`, `productivity_upgrade_group_index`, `luck_productivity_upgrade_group_index`, `production_key` and `max_capacity_level` follow the `PlantZone_Table` and `PlantZoneWorking_Table` sheets of a private server's `DataSheets.bexcel` on client 1784 (columns `WorkAniType`, `ProductivityUpgradeGroupIndex`, `LuckProductivityUpgradeGroupIndex`, `ExchangeGroupIndex`, `MaxCapacityLevel`) and the same tables of a second private server on client 519. Matched by value over the zone keys (`WaypointKey`) each shares with client 3473:

| Column | Field | Equal (client 1784, 304 keys) | Equal (client 519, 288 keys) |
| ------ | ----- | ------------------------ | ------------------------ |
| `WorkAniType` | `work_ani_type` | 303 | 273 |
| `ExchangeGroupIndex` | `production_key` | 293 | 277 |
| `MaxCapacityLevel` | `max_capacity_level` + 1 | 304 | 288 |

Both sheets store `101` and `201` in the two upgrade-group columns on every row, and `PlantUpgradeParam_Table` has rows with index `101` and `201`. The client Lua enum `CppEnums.PlantZoneLevelType` (`global_define_cpp_enum.luac`) has the two matching levels, `ePlantZoneLevelType_GeneralEfficiency` (`0`) and `ePlantZoneLevelType_LuckEfficiency` (`1`); no other Lua file uses it. The 2016 client (build of 2016-01-11) ships with debug symbols: `gc::PlantZoneStaticStatus` holds `_productCategory`, `_workAniType`, `_productivityParamKey`, `_luckProductivityParamKey` and `_productionList` in this order, the order of `+0x0E` to `+0x1A` here; `GameCommonParameterLoaderFromExcel::LoadPlantZoneStaticInformation` reads `WorkAniType` into `_workAniType` and the two upgrade-group columns into the two param keys. `_productionList` maps the exchange group key to `_maxCountLevel`, filled from `PlantZoneWorking_Table`.

The file has no field for `ContentsGroupKey` (10 distinct values in the bexcel). The private server's own `plantzone.dbss` (client 1784) has 309 zones of 27 bytes each: the same fields up to `max_capacity_level`, with no worker species list.

## Notes

- `plantzone.dbss` and `plantzoneoffset.dbss` both report `394` records.
- The offset table's `record_id` equals the record payload's first u32 for all records.
- `worker_species_count` always equals the number of trailing bytes.
- Every `record_id` is an `exploration.bss` sub-node (`is_sub_node=1`) of a production kind; only three production sub-nodes have no plant zone (1564 Specialties and the disabled `UnKnown` records 1831 and 1839).
- The reference project reports 425 plant zones with 389 resolving to items; reading `+0x06` of `plantexchangegroup.bss` as a subgroup key, the client file had 394 zones with 358 resolving, and the same 36 unresolved. The exchange chain resolves all of them (see Production Item Chain).
- Worker output quantities are not identified in these tables. The luck bonus drops are the luck drop group of the production key's exchange (see Production Item Chain).

## Open Questions

### The Constant Block at `+0x04`

`unknown_04` (`2`), `unknown_08` (`0`) and `unknown_0c` (`2`) are constant on clients 1784 and 3473, and so are the sheet columns that have no field yet: `PlantObjectKind` (`2`, the 2016 `_productCategory`, where `2` is `ProductCategory_Farm`), `UpgradeResource` (`2`, `_upgradeResourceKey`), `MaxLevel` (`_maxLevel`), `WorkableCount` (`_workableCountMax`) and `isRandomRecipeLevel` (all `0`). The 10 bytes do not follow the 2016 member order, where `_productCategory` sits right before `_workAniType` (`+0x0D`, always `0` here), so neither value nor order tells which column each byte holds.

### What `max_capacity_level` Controls

It is `1` to `7` only on 19 zones, mostly consecutive Specialties nodes. The client 519 private server loads `MaxCapacityLevel` into `PlantZoneWorkingT` but never reads it back, and the client Lua has no getter for it.

### What `worker_species` Controls

It is not a per-zone worker lock. In game, which worker types can be hired is
set per town, and any hired worker can work any node connected to its town
(I checked in game, 2026-09-27). The list still differs by region: 350
zones list the six base species (Goblin to Dwarf), the 42 Land of the Morning
Light zones only Dokkebi, Dolswe and Shellfolk, and the two Dokkebi Forest
excavation zones only Dokkebi. The values match the `plantworker.bss` species
byte, but what the client uses the list for (a bonus, a default, a leftover
restriction) is unknown.
