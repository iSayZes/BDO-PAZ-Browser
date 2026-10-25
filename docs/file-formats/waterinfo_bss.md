# `waterinfo.bss` Format

## Purpose

The water kinds of the server's water bitmap. A PABR list of colours; each
row is one colour key of the bitmap and nine bytes that are `0` on every
row, where the source sheet has a drop ID. On client 3482 it holds four
colours, one per water kind of the client 1784 sheet notes: sea,
freshwater, murky water and clean water.
[`undergroundinfo.bss`](undergroundinfo_bss.md) has the same layout for
the underground bitmap.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File            | Bytes | Records | Row bytes |
| ------ | -------------- | --------------- | ----- | ------- | --------- |
| 3      | 2726 and later | `waterinfo.bss` | 68    | 4 Row   | 12        |
| 2      | 805 to 2717    | `waterinfo.bss` | 60    | 4 Row   | 10        |
| 1      | 435 to 794     | `waterinfo.bss` | 44    | 4 Row   | 10        |

| Layout | File            | Known        | Unknown      |
| ------ | --------------- | ------------ | ------------ |
| 3      | `waterinfo.bss` | 32 B (47.1%) | 36 B (52.9%) |
| 2      | `waterinfo.bss` | 32 B (53.3%) | 28 B (46.7%) |
| 1      | `waterinfo.bss` | 16 B (36.4%) | 28 B (63.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `64a9d5cc85d6`  |
| 3482   | Layout 3 | `64a9d5cc85d6`  |
| 3474   | Layout 3 | `64a9d5cc85d6`  |
| 3473   | Layout 3 | `64a9d5cc85d6`  |
| 3464   | Layout 3 | `64a9d5cc85d6`  |
| 3458   | Layout 3 | `64a9d5cc85d6`  |
| 3454   | Layout 3 | `64a9d5cc85d6`  |
| 3444   | Layout 3 | `64a9d5cc85d6`  |
| 3435   | Layout 3 | `64a9d5cc85d6`  |
| 3426   | Layout 3 | `64a9d5cc85d6`  |
| 3418   | Layout 3 | `64a9d5cc85d6`  |
| 3412   | Layout 3 | `64a9d5cc85d6`  |
| 3402   | Layout 3 | `64a9d5cc85d6`  |
| 3396   | Layout 3 | `64a9d5cc85d6`  |
| 3387   | Layout 3 | `64a9d5cc85d6`  |
| 3381   | Layout 3 | `64a9d5cc85d6`  |
| 3373   | Layout 3 | `64a9d5cc85d6`  |
| 3364   | Layout 3 | `64a9d5cc85d6`  |
| 3356   | Layout 3 | `64a9d5cc85d6`  |
| 3349   | Layout 3 | `64a9d5cc85d6`  |
| 3342   | Layout 3 | `64a9d5cc85d6`  |
| 3335   | Layout 3 | `64a9d5cc85d6`  |
| 3326   | Layout 3 | `64a9d5cc85d6`  |
| 3321   | Layout 3 | `64a9d5cc85d6`  |
| 3314   | Layout 3 | `64a9d5cc85d6`  |
| 3303   | Layout 3 | `64a9d5cc85d6`  |
| 3302   | Layout 3 | `64a9d5cc85d6`  |
| 3293   | Layout 3 | `64a9d5cc85d6`  |
| 3283   | Layout 3 | `64a9d5cc85d6`  |
| 3275   | Layout 3 | `64a9d5cc85d6`  |
| 3267   | Layout 3 | `64a9d5cc85d6`  |
| 3258   | Layout 3 | `64a9d5cc85d6`  |
| 3251   | Layout 3 | `64a9d5cc85d6`  |
| 3242   | Layout 3 | `64a9d5cc85d6`  |
| 3235   | Layout 3 | `64a9d5cc85d6`  |
| 3229   | Layout 3 | `64a9d5cc85d6`  |
| 3212   | Layout 3 | `64a9d5cc85d6`  |
| 3203   | Layout 3 | `64a9d5cc85d6`  |
| 3193   | Layout 3 | `64a9d5cc85d6`  |
| 3186   | Layout 3 | `64a9d5cc85d6`  |
| 3177   | Layout 3 | `64a9d5cc85d6`  |
| 3169   | Layout 3 | `64a9d5cc85d6`  |
| 3158   | Layout 3 | `64a9d5cc85d6`  |
| 3151   | Layout 3 | `64a9d5cc85d6`  |
| 3144   | Layout 3 | `64a9d5cc85d6`  |
| 3133   | Layout 3 | `64a9d5cc85d6`  |
| 3125   | Layout 3 | `64a9d5cc85d6`  |
| 3118   | Layout 3 | `64a9d5cc85d6`  |
| 3111   | Layout 3 | `64a9d5cc85d6`  |
| 3103   | Layout 3 | `64a9d5cc85d6`  |
| 3095   | Layout 3 | `64a9d5cc85d6`  |
| 3086   | Layout 3 | `64a9d5cc85d6`  |
| 3072   | Layout 3 | `64a9d5cc85d6`  |
| 3062   | Layout 3 | `64a9d5cc85d6`  |
| 3052   | Layout 3 | `64a9d5cc85d6`  |
| 3045   | Layout 3 | `64a9d5cc85d6`  |
| 3037   | Layout 3 | `64a9d5cc85d6`  |
| 3030   | Layout 3 | `64a9d5cc85d6`  |
| 3021   | Layout 3 | `64a9d5cc85d6`  |
| 3012   | Layout 3 | `64a9d5cc85d6`  |
| 3002   | Layout 3 | `64a9d5cc85d6`  |
| 2995   | Layout 3 | `64a9d5cc85d6`  |
| 2987   | Layout 3 | `64a9d5cc85d6`  |
| 2978   | Layout 3 | `64a9d5cc85d6`  |
| 2970   | Layout 3 | `64a9d5cc85d6`  |
| 2959   | Layout 3 | `64a9d5cc85d6`  |
| 2951   | Layout 3 | `64a9d5cc85d6`  |
| 2942   | Layout 3 | `64a9d5cc85d6`  |
| 2935   | Layout 3 | `64a9d5cc85d6`  |
| 2932   | Layout 3 | `64a9d5cc85d6`  |
| 2923   | Layout 3 | `64a9d5cc85d6`  |
| 2919   | Layout 3 | `64a9d5cc85d6`  |
| 2907   | Layout 3 | `64a9d5cc85d6`  |
| 2900   | Layout 3 | `64a9d5cc85d6`  |
| 2891   | Layout 3 | `64a9d5cc85d6`  |
| 2882   | Layout 3 | `64a9d5cc85d6`  |
| 2872   | Layout 3 | `64a9d5cc85d6`  |
| 2863   | Layout 3 | `64a9d5cc85d6`  |
| 2855   | Layout 3 | `64a9d5cc85d6`  |
| 2849   | Layout 3 | `64a9d5cc85d6`  |
| 2844   | Layout 3 | `64a9d5cc85d6`  |
| 2834   | Layout 3 | `64a9d5cc85d6`  |
| 2825   | Layout 3 | `64a9d5cc85d6`  |
| 2819   | Layout 3 | `64a9d5cc85d6`  |
| 2811   | Layout 3 | `64a9d5cc85d6`  |
| 2803   | Layout 3 | `64a9d5cc85d6`  |
| 2794   | Layout 3 | `64a9d5cc85d6`  |
| 2783   | Layout 3 | `64a9d5cc85d6`  |
| 2774   | Layout 3 | `64a9d5cc85d6`  |
| 2765   | Layout 3 | `64a9d5cc85d6`  |
| 2756   | Layout 3 | `64a9d5cc85d6`  |
| 2750   | Layout 3 | `64a9d5cc85d6`  |
| 2743   | Layout 3 | `64a9d5cc85d6`  |
| 2736   | Layout 3 | `64a9d5cc85d6`  |
| 2726   | Layout 3 | `64a9d5cc85d6`  |
| 2717   | Layout 2 | `64a9d5cc85d6`  |
| 2709   | Layout 2 | `64a9d5cc85d6`  |
| 2703   | Layout 2 | `64a9d5cc85d6`  |
| 2695   | Layout 2 | `64a9d5cc85d6`  |
| 2684   | Layout 2 | `64a9d5cc85d6`  |
| 2672   | Layout 2 | `64a9d5cc85d6`  |
| 2665   | Layout 2 | `64a9d5cc85d6`  |
| 2657   | Layout 2 | `64a9d5cc85d6`  |
| 2649   | Layout 2 | `64a9d5cc85d6`  |
| 2644   | Layout 2 | `64a9d5cc85d6`  |
| 2637   | Layout 2 | `64a9d5cc85d6`  |
| 2629   | Layout 2 | `64a9d5cc85d6`  |
| 2619   | Layout 2 | `64a9d5cc85d6`  |
| 2612   | Layout 2 | `64a9d5cc85d6`  |
| 2606   | Layout 2 | `64a9d5cc85d6`  |
| 2602   | Layout 2 | `64a9d5cc85d6`  |
| 2601   | Layout 2 | `64a9d5cc85d6`  |
| 2592   | Layout 2 | `64a9d5cc85d6`  |
| 2583   | Layout 2 | `64a9d5cc85d6`  |
| 2575   | Layout 2 | `64a9d5cc85d6`  |
| 2567   | Layout 2 | `64a9d5cc85d6`  |
| 2560   | Layout 2 | `64a9d5cc85d6`  |
| 2553   | Layout 2 | `64a9d5cc85d6`  |
| 2545   | Layout 2 | `64a9d5cc85d6`  |
| 2538   | Layout 2 | `64a9d5cc85d6`  |
| 2529   | Layout 2 | `64a9d5cc85d6`  |
| 2519   | Layout 2 | `64a9d5cc85d6`  |
| 2513   | Layout 2 | `64a9d5cc85d6`  |
| 2510   | Layout 2 | `64a9d5cc85d6`  |
| 2507   | Layout 2 | `64a9d5cc85d6`  |
| 2503   | Layout 2 | `64a9d5cc85d6`  |
| 2498   | Layout 2 | `64a9d5cc85d6`  |
| 2492   | Layout 2 | `64a9d5cc85d6`  |
| 2487   | Layout 2 | `64a9d5cc85d6`  |
| 2480   | Layout 2 | `64a9d5cc85d6`  |
| 2474   | Layout 2 | `64a9d5cc85d6`  |
| 2468   | Layout 2 | `64a9d5cc85d6`  |
| 2460   | Layout 2 | `64a9d5cc85d6`  |
| 2453   | Layout 2 | `64a9d5cc85d6`  |
| 2444   | Layout 2 | `64a9d5cc85d6`  |
| 2438   | Layout 2 | `64a9d5cc85d6`  |
| 2434   | Layout 2 | `64a9d5cc85d6`  |
| 2429   | Layout 2 | `64a9d5cc85d6`  |
| 2421   | Layout 2 | `64a9d5cc85d6`  |
| 2414   | Layout 2 | `64a9d5cc85d6`  |
| 2407   | Layout 2 | `64a9d5cc85d6`  |
| 2401   | Layout 2 | `64a9d5cc85d6`  |
| 2397   | Layout 2 | `64a9d5cc85d6`  |
| 2393   | Layout 2 | `64a9d5cc85d6`  |
| 2384   | Layout 2 | `64a9d5cc85d6`  |
| 2378   | Layout 2 | `64a9d5cc85d6`  |
| 2372   | Layout 2 | `64a9d5cc85d6`  |
| 2358   | Layout 2 | `64a9d5cc85d6`  |
| 2352   | Layout 2 | `64a9d5cc85d6`  |
| 2347   | Layout 2 | `64a9d5cc85d6`  |
| 2343   | Layout 2 | `64a9d5cc85d6`  |
| 2335   | Layout 2 | `64a9d5cc85d6`  |
| 2327   | Layout 2 | `64a9d5cc85d6`  |
| 2324   | Layout 2 | `64a9d5cc85d6`  |
| 2319   | Layout 2 | `64a9d5cc85d6`  |
| 2313   | Layout 2 | `64a9d5cc85d6`  |
| 2308   | Layout 2 | `64a9d5cc85d6`  |
| 2302   | Layout 2 | `64a9d5cc85d6`  |
| 2295   | Layout 2 | `64a9d5cc85d6`  |
| 2290   | Layout 2 | `64a9d5cc85d6`  |
| 2284   | Layout 2 | `64a9d5cc85d6`  |
| 2276   | Layout 2 | `64a9d5cc85d6`  |
| 2269   | Layout 2 | `64a9d5cc85d6`  |
| 2259   | Layout 2 | `64a9d5cc85d6`  |
| 2250   | Layout 2 | `64a9d5cc85d6`  |
| 2243   | Layout 2 | `64a9d5cc85d6`  |
| 2235   | Layout 2 | `64a9d5cc85d6`  |
| 2229   | Layout 2 | `64a9d5cc85d6`  |
| 2224   | Layout 2 | `64a9d5cc85d6`  |
| 2218   | Layout 2 | `64a9d5cc85d6`  |
| 2215   | Layout 2 | `64a9d5cc85d6`  |
| 2207   | Layout 2 | `64a9d5cc85d6`  |
| 2203   | Layout 2 | `64a9d5cc85d6`  |
| 2196   | Layout 2 | `64a9d5cc85d6`  |
| 2192   | Layout 2 | `64a9d5cc85d6`  |
| 2189   | Layout 2 | `64a9d5cc85d6`  |
| 2183   | Layout 2 | `64a9d5cc85d6`  |
| 2179   | Layout 2 | `64a9d5cc85d6`  |
| 2171   | Layout 2 | `64a9d5cc85d6`  |
| 2163   | Layout 2 | `64a9d5cc85d6`  |
| 2156   | Layout 2 | `64a9d5cc85d6`  |
| 2151   | Layout 2 | `64a9d5cc85d6`  |
| 2147   | Layout 2 | `64a9d5cc85d6`  |
| 2142   | Layout 2 | `64a9d5cc85d6`  |
| 2138   | Layout 2 | `64a9d5cc85d6`  |
| 2134   | Layout 2 | `64a9d5cc85d6`  |
| 2130   | Layout 2 | `64a9d5cc85d6`  |
| 2122   | Layout 2 | `64a9d5cc85d6`  |
| 2107   | Layout 2 | `64a9d5cc85d6`  |
| 2098   | Layout 2 | `64a9d5cc85d6`  |
| 2089   | Layout 2 | `64a9d5cc85d6`  |
| 2081   | Layout 2 | `64a9d5cc85d6`  |
| 2073   | Layout 2 | `64a9d5cc85d6`  |
| 2067   | Layout 2 | `64a9d5cc85d6`  |
| 2063   | Layout 2 | `64a9d5cc85d6`  |
| 2059   | Layout 2 | `64a9d5cc85d6`  |
| 2052   | Layout 2 | `64a9d5cc85d6`  |
| 2044   | Layout 2 | `64a9d5cc85d6`  |
| 2039   | Layout 2 | `64a9d5cc85d6`  |
| 2032   | Layout 2 | `64a9d5cc85d6`  |
| 2025   | Layout 2 | `64a9d5cc85d6`  |
| 2011   | Layout 2 | `64a9d5cc85d6`  |
| 2005   | Layout 2 | `64a9d5cc85d6`  |
| 2000   | Layout 2 | `64a9d5cc85d6`  |
| 1996   | Layout 2 | `64a9d5cc85d6`  |
| 1991   | Layout 2 | `64a9d5cc85d6`  |
| 1985   | Layout 2 | `64a9d5cc85d6`  |
| 1980   | Layout 2 | `64a9d5cc85d6`  |
| 1969   | Layout 2 | `64a9d5cc85d6`  |
| 1964   | Layout 2 | `64a9d5cc85d6`  |
| 1958   | Layout 2 | `64a9d5cc85d6`  |
| 1950   | Layout 2 | `64a9d5cc85d6`  |
| 1945   | Layout 2 | `64a9d5cc85d6`  |
| 1937   | Layout 2 | `64a9d5cc85d6`  |
| 1933   | Layout 2 | `64a9d5cc85d6`  |
| 1927   | Layout 2 | `64a9d5cc85d6`  |
| 1921   | Layout 2 | `64a9d5cc85d6`  |
| 1914   | Layout 2 | `64a9d5cc85d6`  |
| 1908   | Layout 2 | `64a9d5cc85d6`  |
| 1897   | Layout 2 | `64a9d5cc85d6`  |
| 1892   | Layout 2 | `64a9d5cc85d6`  |
| 1886   | Layout 2 | `64a9d5cc85d6`  |
| 1881   | Layout 2 | `64a9d5cc85d6`  |
| 1871   | Layout 2 | `64a9d5cc85d6`  |
| 1866   | Layout 2 | `64a9d5cc85d6`  |
| 1862   | Layout 2 | `64a9d5cc85d6`  |
| 1854   | Layout 2 | `64a9d5cc85d6`  |
| 1846   | Layout 2 | `64a9d5cc85d6`  |
| 1838   | Layout 2 | `64a9d5cc85d6`  |
| 1832   | Layout 2 | `64a9d5cc85d6`  |
| 1826   | Layout 2 | `64a9d5cc85d6`  |
| 1822   | Layout 2 | `64a9d5cc85d6`  |
| 1818   | Layout 2 | `64a9d5cc85d6`  |
| 1804   | Layout 2 | `64a9d5cc85d6`  |
| 1794   | Layout 2 | `64a9d5cc85d6`  |
| 1790   | Layout 2 | `64a9d5cc85d6`  |
| 1784   | Layout 2 | `64a9d5cc85d6`  |
| 1774   | Layout 2 | `64a9d5cc85d6`  |
| 1771   | Layout 2 | `64a9d5cc85d6`  |
| 1762   | Layout 2 | `64a9d5cc85d6`  |
| 1759   | Layout 2 | `64a9d5cc85d6`  |
| 1754   | Layout 2 | `64a9d5cc85d6`  |
| 1749   | Layout 2 | `64a9d5cc85d6`  |
| 1743   | Layout 2 | `64a9d5cc85d6`  |
| 1737   | Layout 2 | `64a9d5cc85d6`  |
| 1731   | Layout 2 | `64a9d5cc85d6`  |
| 1725   | Layout 2 | `64a9d5cc85d6`  |
| 1717   | Layout 2 | `64a9d5cc85d6`  |
| 1710   | Layout 2 | `64a9d5cc85d6`  |
| 1704   | Layout 2 | `64a9d5cc85d6`  |
| 1698   | Layout 2 | `64a9d5cc85d6`  |
| 1690   | Layout 2 | `64a9d5cc85d6`  |
| 1685   | Layout 2 | `64a9d5cc85d6`  |
| 1680   | Layout 2 | `64a9d5cc85d6`  |
| 1674   | Layout 2 | `64a9d5cc85d6`  |
| 1668   | Layout 2 | `64a9d5cc85d6`  |
| 1659   | Layout 2 | `64a9d5cc85d6`  |
| 1649   | Layout 2 | `64a9d5cc85d6`  |
| 1642   | Layout 2 | `64a9d5cc85d6`  |
| 1636   | Layout 2 | `64a9d5cc85d6`  |
| 1628   | Layout 2 | `64a9d5cc85d6`  |
| 1622   | Layout 2 | `64a9d5cc85d6`  |
| 1614   | Layout 2 | `64a9d5cc85d6`  |
| 1608   | Layout 2 | `64a9d5cc85d6`  |
| 1602   | Layout 2 | `64a9d5cc85d6`  |
| 1598   | Layout 2 | `64a9d5cc85d6`  |
| 1594   | Layout 2 | `64a9d5cc85d6`  |
| 1590   | Layout 2 | `64a9d5cc85d6`  |
| 1587   | Layout 2 | `64a9d5cc85d6`  |
| 1584   | Layout 2 | `64a9d5cc85d6`  |
| 1579   | Layout 2 | `64a9d5cc85d6`  |
| 1572   | Layout 2 | `64a9d5cc85d6`  |
| 1565   | Layout 2 | `64a9d5cc85d6`  |
| 1559   | Layout 2 | `64a9d5cc85d6`  |
| 1554   | Layout 2 | `64a9d5cc85d6`  |
| 1547   | Layout 2 | `64a9d5cc85d6`  |
| 1537   | Layout 2 | `64a9d5cc85d6`  |
| 1529   | Layout 2 | `64a9d5cc85d6`  |
| 1524   | Layout 2 | `64a9d5cc85d6`  |
| 1519   | Layout 2 | `64a9d5cc85d6`  |
| 1509   | Layout 2 | `64a9d5cc85d6`  |
| 1506   | Layout 2 | `64a9d5cc85d6`  |
| 1504   | Layout 2 | `64a9d5cc85d6`  |
| 1500   | Layout 2 | `64a9d5cc85d6`  |
| 1493   | Layout 2 | `64a9d5cc85d6`  |
| 1489   | Layout 2 | `64a9d5cc85d6`  |
| 1485   | Layout 2 | `64a9d5cc85d6`  |
| 1481   | Layout 2 | `64a9d5cc85d6`  |
| 1474   | Layout 2 | `64a9d5cc85d6`  |
| 1466   | Layout 2 | `64a9d5cc85d6`  |
| 1462   | Layout 2 | `64a9d5cc85d6`  |
| 1459   | Layout 2 | `64a9d5cc85d6`  |
| 1453   | Layout 2 | `64a9d5cc85d6`  |
| 1450   | Layout 2 | `64a9d5cc85d6`  |
| 1445   | Layout 2 | `64a9d5cc85d6`  |
| 1439   | Layout 2 | `64a9d5cc85d6`  |
| 1433   | Layout 2 | `64a9d5cc85d6`  |
| 1430   | Layout 2 | `64a9d5cc85d6`  |
| 1426   | Layout 2 | `64a9d5cc85d6`  |
| 1421   | Layout 2 | `64a9d5cc85d6`  |
| 1417   | Layout 2 | `64a9d5cc85d6`  |
| 1416   | Layout 2 | `64a9d5cc85d6`  |
| 1409   | Layout 2 | `64a9d5cc85d6`  |
| 1405   | Layout 2 | `64a9d5cc85d6`  |
| 1401   | Layout 2 | `64a9d5cc85d6`  |
| 1396   | Layout 2 | `64a9d5cc85d6`  |
| 1391   | Layout 2 | `64a9d5cc85d6`  |
| 1390   | Layout 2 | `64a9d5cc85d6`  |
| 1386   | Layout 2 | `64a9d5cc85d6`  |
| 1381   | Layout 2 | `64a9d5cc85d6`  |
| 1379   | Layout 2 | `64a9d5cc85d6`  |
| 1372   | Layout 2 | `64a9d5cc85d6`  |
| 1366   | Layout 2 | `64a9d5cc85d6`  |
| 1364   | Layout 2 | `64a9d5cc85d6`  |
| 1363   | Layout 2 | `64a9d5cc85d6`  |
| 1360   | Layout 2 | `64a9d5cc85d6`  |
| 1358   | Layout 2 | `64a9d5cc85d6`  |
| 1355   | Layout 2 | `64a9d5cc85d6`  |
| 1351   | Layout 2 | `64a9d5cc85d6`  |
| 1348   | Layout 2 | `64a9d5cc85d6`  |
| 1346   | Layout 2 | `64a9d5cc85d6`  |
| 1341   | Layout 2 | `64a9d5cc85d6`  |
| 1340   | Layout 2 | `64a9d5cc85d6`  |
| 1338   | Layout 2 | `64a9d5cc85d6`  |
| 1335   | Layout 2 | `64a9d5cc85d6`  |
| 1333   | Layout 2 | `64a9d5cc85d6`  |
| 1329   | Layout 2 | `64a9d5cc85d6`  |
| 1327   | Layout 2 | `64a9d5cc85d6`  |
| 1324   | Layout 2 | `64a9d5cc85d6`  |
| 1321   | Layout 2 | `64a9d5cc85d6`  |
| 1319   | Layout 2 | `64a9d5cc85d6`  |
| 1318   | Layout 2 | `64a9d5cc85d6`  |
| 1316   | Layout 2 | `64a9d5cc85d6`  |
| 1313   | Layout 2 | `64a9d5cc85d6`  |
| 1311   | Layout 2 | `64a9d5cc85d6`  |
| 1309   | Layout 2 | `64a9d5cc85d6`  |
| 1304   | Layout 2 | `64a9d5cc85d6`  |
| 1292   | Layout 2 | `64a9d5cc85d6`  |
| 1286   | Layout 2 | `64a9d5cc85d6`  |
| 1280   | Layout 2 | `64a9d5cc85d6`  |
| 1276   | Layout 2 | `64a9d5cc85d6`  |
| 1267   | Layout 2 | `64a9d5cc85d6`  |
| 1261   | Layout 2 | `64a9d5cc85d6`  |
| 1256   | Layout 2 | `64a9d5cc85d6`  |
| 1250   | Layout 2 | `64a9d5cc85d6`  |
| 1246   | Layout 2 | `64a9d5cc85d6`  |
| 1239   | Layout 2 | `64a9d5cc85d6`  |
| 1230   | Layout 2 | `64a9d5cc85d6`  |
| 1226   | Layout 2 | `64a9d5cc85d6`  |
| 1220   | Layout 2 | `64a9d5cc85d6`  |
| 1217   | Layout 2 | `64a9d5cc85d6`  |
| 1211   | Layout 2 | `64a9d5cc85d6`  |
| 1210   | Layout 2 | `64a9d5cc85d6`  |
| 1208   | Layout 2 | `64a9d5cc85d6`  |
| 1203   | Layout 2 | `64a9d5cc85d6`  |
| 1197   | Layout 2 | `64a9d5cc85d6`  |
| 1194   | Layout 2 | `64a9d5cc85d6`  |
| 1192   | Layout 2 | `64a9d5cc85d6`  |
| 1187   | Layout 2 | `64a9d5cc85d6`  |
| 1183   | Layout 2 | `64a9d5cc85d6`  |
| 1177   | Layout 2 | `64a9d5cc85d6`  |
| 1173   | Layout 2 | `64a9d5cc85d6`  |
| 1167   | Layout 2 | `64a9d5cc85d6`  |
| 1164   | Layout 2 | `64a9d5cc85d6`  |
| 1156   | Layout 2 | `64a9d5cc85d6`  |
| 1149   | Layout 2 | `64a9d5cc85d6`  |
| 1144   | Layout 2 | `64a9d5cc85d6`  |
| 1137   | Layout 2 | `64a9d5cc85d6`  |
| 1132   | Layout 2 | `64a9d5cc85d6`  |
| 1127   | Layout 2 | `64a9d5cc85d6`  |
| 1122   | Layout 2 | `64a9d5cc85d6`  |
| 1118   | Layout 2 | `64a9d5cc85d6`  |
| 1114   | Layout 2 | `64a9d5cc85d6`  |
| 1109   | Layout 2 | `64a9d5cc85d6`  |
| 1102   | No file  | `64a9d5cc85d6`  |
| 1096   | No file  | `64a9d5cc85d6`  |
| 1088   | No file  | `64a9d5cc85d6`  |
| 1081   | No file  | `64a9d5cc85d6`  |
| 1076   | No file  | `64a9d5cc85d6`  |
| 1069   | No file  | `64a9d5cc85d6`  |
| 1064   | No file  | `64a9d5cc85d6`  |
| 1058   | No file  | `64a9d5cc85d6`  |
| 1051   | No file  | `64a9d5cc85d6`  |
| 1044   | No file  | `64a9d5cc85d6`  |
| 1036   | No file  | `64a9d5cc85d6`  |
| 1026   | No file  | `64a9d5cc85d6`  |
| 1016   | No file  | `64a9d5cc85d6`  |
| 1009   | No file  | `64a9d5cc85d6`  |
| 1005   | No file  | `64a9d5cc85d6`  |
| 1000   | No file  | `64a9d5cc85d6`  |
| 998    | No file  | `64a9d5cc85d6`  |
| 990    | No file  | `64a9d5cc85d6`  |
| 979    | No file  | `64a9d5cc85d6`  |
| 972    | No file  | `64a9d5cc85d6`  |
| 963    | No file  | `64a9d5cc85d6`  |
| 955    | No file  | `64a9d5cc85d6`  |
| 946    | No file  | `64a9d5cc85d6`  |
| 938    | No file  | `64a9d5cc85d6`  |
| 927    | No file  | `64a9d5cc85d6`  |
| 911    | No file  | `64a9d5cc85d6`  |
| 904    | No file  | `64a9d5cc85d6`  |
| 899    | No file  | `64a9d5cc85d6`  |
| 894    | No file  | `64a9d5cc85d6`  |
| 885    | No file  | `64a9d5cc85d6`  |
| 879    | No file  | `64a9d5cc85d6`  |
| 872    | No file  | `64a9d5cc85d6`  |
| 864    | No file  | `64a9d5cc85d6`  |
| 855    | No file  | `64a9d5cc85d6`  |
| 853    | No file  | `64a9d5cc85d6`  |
| 845    | No file  | `64a9d5cc85d6`  |
| 837    | No file  | `64a9d5cc85d6`  |
| 829    | Layout 2 | `64a9d5cc85d6`  |
| 822    | Layout 2 | `64a9d5cc85d6`  |
| 814    | Layout 2 | `64a9d5cc85d6`  |
| 805    | Layout 2 | `64a9d5cc85d6`  |
| 794    | Layout 1 | `64a9d5cc85d6`  |
| 787    | Layout 1 | `64a9d5cc85d6`  |
| 780    | Layout 1 | `64a9d5cc85d6`  |
| 771    | Layout 1 | `64a9d5cc85d6`  |
| 760    | Layout 1 | `64a9d5cc85d6`  |
| 748    | Layout 1 | `64a9d5cc85d6`  |
| 741    | Layout 1 | `64a9d5cc85d6`  |
| 736    | Layout 1 | `64a9d5cc85d6`  |
| 731    | Layout 1 | `64a9d5cc85d6`  |
| 723    | Layout 1 | `64a9d5cc85d6`  |
| 711    | Layout 1 | `64a9d5cc85d6`  |
| 707    | Layout 1 | `64a9d5cc85d6`  |
| 697    | Layout 1 | `64a9d5cc85d6`  |
| 689    | Layout 1 | `64a9d5cc85d6`  |
| 683    | Layout 1 | `64a9d5cc85d6`  |
| 678    | Layout 1 | `64a9d5cc85d6`  |
| 670    | Layout 1 | `64a9d5cc85d6`  |
| 661    | Layout 1 | `64a9d5cc85d6`  |
| 656    | Layout 1 | `64a9d5cc85d6`  |
| 652    | Layout 1 | `64a9d5cc85d6`  |
| 643    | Layout 1 | `64a9d5cc85d6`  |
| 637    | Layout 1 | `64a9d5cc85d6`  |
| 630    | Layout 1 | `64a9d5cc85d6`  |
| 627    | Layout 1 | `64a9d5cc85d6`  |
| 621    | Layout 1 | `64a9d5cc85d6`  |
| 617    | Layout 1 | `64a9d5cc85d6`  |
| 615    | Layout 1 | `64a9d5cc85d6`  |
| 606    | Layout 1 | `64a9d5cc85d6`  |
| 599    | Layout 1 | `64a9d5cc85d6`  |
| 592    | Layout 1 | `64a9d5cc85d6`  |
| 586    | Layout 1 | `64a9d5cc85d6`  |
| 577    | Layout 1 | `64a9d5cc85d6`  |
| 569    | Layout 1 | `64a9d5cc85d6`  |
| 561    | Layout 1 | `64a9d5cc85d6`  |
| 554    | Layout 1 | `64a9d5cc85d6`  |
| 542    | Layout 1 | `64a9d5cc85d6`  |
| 532    | Layout 1 | `64a9d5cc85d6`  |
| 531    | Layout 1 | `64a9d5cc85d6`  |
| 526    | Layout 1 | `64a9d5cc85d6`  |
| 521    | Layout 1 | `64a9d5cc85d6`  |
| 517    | Layout 1 | `64a9d5cc85d6`  |
| 510    | Layout 1 | `64a9d5cc85d6`  |
| 508    | Layout 1 | `64a9d5cc85d6`  |
| 504    | Layout 1 | `64a9d5cc85d6`  |
| 497    | Layout 1 | `64a9d5cc85d6`  |
| 491    | Layout 1 | `64a9d5cc85d6`  |
| 485    | Layout 1 | `64a9d5cc85d6`  |
| 478    | Layout 1 | `64a9d5cc85d6`  |
| 472    | Layout 1 | `64a9d5cc85d6`  |
| 466    | Layout 1 | `64a9d5cc85d6`  |
| 457    | Layout 1 | `64a9d5cc85d6`  |
| 452    | Layout 1 | `64a9d5cc85d6`  |
| 449    | Layout 1 | `64a9d5cc85d6`  |
| 435    | Layout 1 | `64a9d5cc85d6`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of colours                             |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (12 bytes)

| Offset  | Type     | Field      | Notes                                                                  |
| ------- | -------- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | bytes[3] | color_key  | Bitmap colour, stored blue, green, red; unique per row. See Colours   |
| `+0x03` | u8       | unknown_03 | `0` on every row; the alpha byte `a` of the 2016 `pa::Color`           |
| `+0x04` | bytes[8] | unknown_04 | `0` on every row. See Open Questions                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 2

### Row (10 bytes)

| Offset  | Type     | Field      | Notes                                  |
| ------- | -------- | ---------- | -------------------------------------- |
| `+0x00` | bytes[3] | color_key  | Same as Layout 3                       |
| `+0x03` | u8       | unknown_03 | `0` on every row                       |
| `+0x04` | bytes[6] | unknown_04 | `0` on clients 794 and 1784; see Notes |

## Layout 1

The file has no PABR magic, string table or trailer; the rows are the
Layout 2 rows.

### File Layout

| Offset  | Type           | Field     | Notes             |
| ------- | -------------- | --------- | ----------------- |
| `+0x00` | u32            | row_count | Number of colours |
| `+0x04` | Row[row_count] | rows      | See Row           |

## Colours

`color_key` read as `rrggbb`, in file order, with the note of the
`Water_Table` sheet in a private server's `datasheet_regiondatatable.xlsm`
on client 1784 and its `DropID`. Clients 1784 and 3482 hold the same four
colours in this order, and so do clients 435 and 504, with these drop
IDs in their rows (see Notes).

| `color_key` | Sheet note                | `DropID` on the sheet |
| ----------- | ------------------------- | --------------------- |
| `649664`    | `바다` (sea)              | `10056`               |
| `fac8c8`    | `민물` (freshwater)       | `10057`               |
| `643c3c`    | `탁한 물` (murky water)   | `10058`               |
| `5050c8`    | `일급수` (clean water)    | `10059`               |

## Field Names

The `Water_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `R`, `G`, `B` and `DropID` and four rows.
All 4 of 4 file colours on clients 1784 and 3482 are sheet rows, with the
bytes in blue, green, red order. The 2016 `gc::WaterInfoManager` holds
`gc::BitmapDropInfo` rows in a map keyed by colour; a
`gc::BitmapDropInfo` is `_colorKey`, a `pa::Color` of the bytes `b`, `g`,
`r` and `a`, followed by a u16 `_dropItemKey`. The first field takes that
member's name. The `Water_Table` of a private server on client 519 has
the same four colours and drop IDs.

## Notes

- The client has no water bitmap in `ui_texture/minimap/area/`; the
  2016 `gc::WaterMapInfo` reads an image file into the colour index, so
  the bitmap is a server or tool file.
- On clients 435 and 504 (Layout 1) `unknown_04` is not `0`: its first
  three bytes repeat `color_key`, the fourth is `0`, and its last two are
  a u16 that equals the sheet's `DropID` on 4 of 4 rows. Each row is then
  the 2016 map written out, the colour as the key and the
  `gc::BitmapDropInfo` (`_colorKey`, `_dropItemKey`) after it. On clients
  508, 794 and 1784 the six bytes are `0` on every row.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/server_tables.py`,
  `color_key` as `rrggbb`.

## Open Questions

### The Zero Bytes After the Colour

`unknown_04` is `0` on every row of clients 508, 794, 1784 and 3482. On
clients 435 and 504 the same six bytes hold a colour copy and the drop ID
(Notes), so the newer files likely keep those fields and the client build
no longer fills them. With every byte `0`, the split of the eight bytes of Layout 3 (a
wider drop ID, or padding) cannot be read off the file, so the bytes stay
one unnamed field.
