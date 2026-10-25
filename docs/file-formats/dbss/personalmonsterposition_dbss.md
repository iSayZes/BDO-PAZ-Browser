# `personalmonsterposition.dbss` Format

## Purpose

The spawn points of the Dark Rift bosses of
[`personalmonster.dbss`](personalmonster_dbss.md): per position index a
world position and the distance around it at which a boss spawns. On
client 3474 the file has 48 points, indexes `1` to `48`, each with a
spawn distance of `5000`. No key in the client files says which boss uses
which point. Companion `personalmonsterpositionoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                 | Bytes | Records       | Row bytes |
| ------ | -------------- | ------------------------------------ | ----- | ------------- | --------- |
| 2      | 2134 and later | `personalmonsterposition.dbss`       | 1,060 | 48 Row        | 22        |
| 2      | 2134 and later | `personalmonsterpositionoffset.dbss` | 580   | 48 Offset Row | 12        |
| 1      | 1280 to 2130   | `personalmonsterposition.dbss`       | 944   | 47 Row        | 20        |
| 1      | 1280 to 2130   | `personalmonsterpositionoffset.dbss` | 568   | 47 Offset Row | 12        |

| Layout | File                                 | Known          | Unknown     |
| ------ | ------------------------------------ | -------------- | ----------- |
| 2      | `personalmonsterposition.dbss`       | 964 B (90.9%)  | 96 B (9.1%) |
| 2      | `personalmonsterpositionoffset.dbss` | 580 B (100.0%) | 0 B (0.0%)  |
| 1      | `personalmonsterposition.dbss`       | 944 B (100.0%) | 0 B (0.0%)  |
| 1      | `personalmonsterpositionoffset.dbss` | 568 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `5c6d107f7ca6`  |
| 3482   | Layout 2 | `5c6d107f7ca6`  |
| 3474   | Layout 2 | `5c6d107f7ca6`  |
| 3473   | Layout 2 | `5c6d107f7ca6`  |
| 3464   | Layout 2 | `5c6d107f7ca6`  |
| 3458   | Layout 2 | `5c6d107f7ca6`  |
| 3454   | Layout 2 | `5c6d107f7ca6`  |
| 3444   | Layout 2 | `5c6d107f7ca6`  |
| 3435   | Layout 2 | `5c6d107f7ca6`  |
| 3426   | Layout 2 | `5c6d107f7ca6`  |
| 3418   | Layout 2 | `5c6d107f7ca6`  |
| 3412   | Layout 2 | `5c6d107f7ca6`  |
| 3402   | Layout 2 | `5c6d107f7ca6`  |
| 3396   | Layout 2 | `5c6d107f7ca6`  |
| 3387   | Layout 2 | `5c6d107f7ca6`  |
| 3381   | Layout 2 | `5c6d107f7ca6`  |
| 3373   | Layout 2 | `5c6d107f7ca6`  |
| 3364   | Layout 2 | `5c6d107f7ca6`  |
| 3356   | Layout 2 | `5c6d107f7ca6`  |
| 3349   | Layout 2 | `5c6d107f7ca6`  |
| 3342   | Layout 2 | `5c6d107f7ca6`  |
| 3335   | Layout 2 | `5c6d107f7ca6`  |
| 3326   | Layout 2 | `5c6d107f7ca6`  |
| 3321   | Layout 2 | `5c6d107f7ca6`  |
| 3314   | Layout 2 | `5c6d107f7ca6`  |
| 3303   | Layout 2 | `5c6d107f7ca6`  |
| 3302   | Layout 2 | `5c6d107f7ca6`  |
| 3293   | Layout 2 | `5c6d107f7ca6`  |
| 3283   | Layout 2 | `5c6d107f7ca6`  |
| 3275   | Layout 2 | `5c6d107f7ca6`  |
| 3267   | Layout 2 | `5c6d107f7ca6`  |
| 3258   | Layout 2 | `5c6d107f7ca6`  |
| 3251   | Layout 2 | `5c6d107f7ca6`  |
| 3242   | Layout 2 | `5c6d107f7ca6`  |
| 3235   | Layout 2 | `5c6d107f7ca6`  |
| 3229   | Layout 2 | `5c6d107f7ca6`  |
| 3212   | Layout 2 | `5c6d107f7ca6`  |
| 3203   | Layout 2 | `5c6d107f7ca6`  |
| 3193   | Layout 2 | `5c6d107f7ca6`  |
| 3186   | Layout 2 | `5c6d107f7ca6`  |
| 3177   | Layout 2 | `5c6d107f7ca6`  |
| 3169   | Layout 2 | `5c6d107f7ca6`  |
| 3158   | Layout 2 | `5c6d107f7ca6`  |
| 3151   | Layout 2 | `5c6d107f7ca6`  |
| 3144   | Layout 2 | `5c6d107f7ca6`  |
| 3133   | Layout 2 | `5c6d107f7ca6`  |
| 3125   | Layout 2 | `5c6d107f7ca6`  |
| 3118   | Layout 2 | `5c6d107f7ca6`  |
| 3111   | Layout 2 | `5c6d107f7ca6`  |
| 3103   | Layout 2 | `5c6d107f7ca6`  |
| 3095   | Layout 2 | `5c6d107f7ca6`  |
| 3086   | Layout 2 | `5c6d107f7ca6`  |
| 3072   | Layout 2 | `5c6d107f7ca6`  |
| 3062   | Layout 2 | `5c6d107f7ca6`  |
| 3052   | Layout 2 | `5c6d107f7ca6`  |
| 3045   | Layout 2 | `5c6d107f7ca6`  |
| 3037   | Layout 2 | `5c6d107f7ca6`  |
| 3030   | Layout 2 | `5c6d107f7ca6`  |
| 3021   | Layout 2 | `5c6d107f7ca6`  |
| 3012   | Layout 2 | `5c6d107f7ca6`  |
| 3002   | Layout 2 | `5c6d107f7ca6`  |
| 2995   | Layout 2 | `5c6d107f7ca6`  |
| 2987   | Layout 2 | `5c6d107f7ca6`  |
| 2978   | Layout 2 | `5c6d107f7ca6`  |
| 2970   | Layout 2 | `5c6d107f7ca6`  |
| 2959   | Layout 2 | `5c6d107f7ca6`  |
| 2951   | Layout 2 | `5c6d107f7ca6`  |
| 2942   | Layout 2 | `5c6d107f7ca6`  |
| 2935   | Layout 2 | `5c6d107f7ca6`  |
| 2932   | Layout 2 | `5c6d107f7ca6`  |
| 2923   | Layout 2 | `5c6d107f7ca6`  |
| 2919   | Layout 2 | `5c6d107f7ca6`  |
| 2907   | Layout 2 | `5c6d107f7ca6`  |
| 2900   | Layout 2 | `5c6d107f7ca6`  |
| 2891   | Layout 2 | `5c6d107f7ca6`  |
| 2882   | Layout 2 | `5c6d107f7ca6`  |
| 2872   | Layout 2 | `5c6d107f7ca6`  |
| 2863   | Layout 2 | `5c6d107f7ca6`  |
| 2855   | Layout 2 | `5c6d107f7ca6`  |
| 2849   | Layout 2 | `5c6d107f7ca6`  |
| 2844   | Layout 2 | `5c6d107f7ca6`  |
| 2834   | Layout 2 | `5c6d107f7ca6`  |
| 2825   | Layout 2 | `5c6d107f7ca6`  |
| 2819   | Layout 2 | `5c6d107f7ca6`  |
| 2811   | Layout 2 | `5c6d107f7ca6`  |
| 2803   | Layout 2 | `5c6d107f7ca6`  |
| 2794   | Layout 2 | `5c6d107f7ca6`  |
| 2783   | Layout 2 | `5c6d107f7ca6`  |
| 2774   | Layout 2 | `5c6d107f7ca6`  |
| 2765   | Layout 2 | `5c6d107f7ca6`  |
| 2756   | Layout 2 | `5c6d107f7ca6`  |
| 2750   | Layout 2 | `5c6d107f7ca6`  |
| 2743   | Layout 2 | `5c6d107f7ca6`  |
| 2736   | Layout 2 | `5c6d107f7ca6`  |
| 2726   | Layout 2 | `5c6d107f7ca6`  |
| 2717   | Layout 2 | `5c6d107f7ca6`  |
| 2709   | Layout 2 | `5c6d107f7ca6`  |
| 2703   | Layout 2 | `5c6d107f7ca6`  |
| 2695   | Layout 2 | `5c6d107f7ca6`  |
| 2684   | Layout 2 | `5c6d107f7ca6`  |
| 2672   | Layout 2 | `5c6d107f7ca6`  |
| 2665   | Layout 2 | `5c6d107f7ca6`  |
| 2657   | Layout 2 | `5c6d107f7ca6`  |
| 2649   | Layout 2 | `5c6d107f7ca6`  |
| 2644   | Layout 2 | `5c6d107f7ca6`  |
| 2637   | Layout 2 | `5c6d107f7ca6`  |
| 2629   | Layout 2 | `5c6d107f7ca6`  |
| 2619   | Layout 2 | `5c6d107f7ca6`  |
| 2612   | Layout 2 | `5c6d107f7ca6`  |
| 2606   | Layout 2 | `5c6d107f7ca6`  |
| 2602   | Layout 2 | `5c6d107f7ca6`  |
| 2601   | Layout 2 | `5c6d107f7ca6`  |
| 2592   | Layout 2 | `5c6d107f7ca6`  |
| 2583   | Layout 2 | `5c6d107f7ca6`  |
| 2575   | Layout 2 | `5c6d107f7ca6`  |
| 2567   | Layout 2 | `5c6d107f7ca6`  |
| 2560   | Layout 2 | `5c6d107f7ca6`  |
| 2553   | Layout 2 | `5c6d107f7ca6`  |
| 2545   | Layout 2 | `5c6d107f7ca6`  |
| 2538   | Layout 2 | `5c6d107f7ca6`  |
| 2529   | Layout 2 | `5c6d107f7ca6`  |
| 2519   | Layout 2 | `5c6d107f7ca6`  |
| 2513   | Layout 2 | `5c6d107f7ca6`  |
| 2510   | Layout 2 | `5c6d107f7ca6`  |
| 2507   | Layout 2 | `5c6d107f7ca6`  |
| 2503   | Layout 2 | `5c6d107f7ca6`  |
| 2498   | Layout 2 | `5c6d107f7ca6`  |
| 2492   | Layout 2 | `5c6d107f7ca6`  |
| 2487   | Layout 2 | `5c6d107f7ca6`  |
| 2480   | Layout 2 | `5c6d107f7ca6`  |
| 2474   | Layout 2 | `5c6d107f7ca6`  |
| 2468   | Layout 2 | `5c6d107f7ca6`  |
| 2460   | Layout 2 | `5c6d107f7ca6`  |
| 2453   | Layout 2 | `5c6d107f7ca6`  |
| 2444   | Layout 2 | `5c6d107f7ca6`  |
| 2438   | Layout 2 | `5c6d107f7ca6`  |
| 2434   | Layout 2 | `5c6d107f7ca6`  |
| 2429   | Layout 2 | `5c6d107f7ca6`  |
| 2421   | Layout 2 | `5c6d107f7ca6`  |
| 2414   | Layout 2 | `5c6d107f7ca6`  |
| 2407   | Layout 2 | `5c6d107f7ca6`  |
| 2401   | Layout 2 | `5c6d107f7ca6`  |
| 2397   | Layout 2 | `5c6d107f7ca6`  |
| 2393   | Layout 2 | `5c6d107f7ca6`  |
| 2384   | Layout 2 | `5c6d107f7ca6`  |
| 2378   | Layout 2 | `5c6d107f7ca6`  |
| 2372   | Layout 2 | `5c6d107f7ca6`  |
| 2358   | Layout 2 | `5c6d107f7ca6`  |
| 2352   | Layout 2 | `5c6d107f7ca6`  |
| 2347   | Layout 2 | `5c6d107f7ca6`  |
| 2343   | Layout 2 | `5c6d107f7ca6`  |
| 2335   | Layout 2 | `5c6d107f7ca6`  |
| 2327   | Layout 2 | `5c6d107f7ca6`  |
| 2324   | Layout 2 | `5c6d107f7ca6`  |
| 2319   | Layout 2 | `5c6d107f7ca6`  |
| 2313   | Layout 2 | `5c6d107f7ca6`  |
| 2308   | Layout 2 | `5c6d107f7ca6`  |
| 2302   | Layout 2 | `5c6d107f7ca6`  |
| 2295   | Layout 2 | `5c6d107f7ca6`  |
| 2290   | Layout 2 | `5c6d107f7ca6`  |
| 2284   | Layout 2 | `5c6d107f7ca6`  |
| 2276   | Layout 2 | `5c6d107f7ca6`  |
| 2269   | Layout 2 | `5c6d107f7ca6`  |
| 2259   | Layout 2 | `5c6d107f7ca6`  |
| 2250   | Layout 2 | `5c6d107f7ca6`  |
| 2243   | Layout 2 | `5c6d107f7ca6`  |
| 2235   | Layout 2 | `5c6d107f7ca6`  |
| 2229   | Layout 2 | `5c6d107f7ca6`  |
| 2224   | Layout 2 | `5c6d107f7ca6`  |
| 2218   | Layout 2 | `5c6d107f7ca6`  |
| 2215   | Layout 2 | `5c6d107f7ca6`  |
| 2207   | Layout 2 | `5c6d107f7ca6`  |
| 2203   | Layout 2 | `5c6d107f7ca6`  |
| 2196   | Layout 2 | `5c6d107f7ca6`  |
| 2192   | Layout 2 | `5c6d107f7ca6`  |
| 2189   | Layout 2 | `5c6d107f7ca6`  |
| 2183   | Layout 2 | `5c6d107f7ca6`  |
| 2179   | Layout 2 | `5c6d107f7ca6`  |
| 2171   | Layout 2 | `5c6d107f7ca6`  |
| 2163   | Layout 2 | `5c6d107f7ca6`  |
| 2156   | Layout 2 | `5c6d107f7ca6`  |
| 2151   | Layout 2 | `5c6d107f7ca6`  |
| 2147   | Layout 2 | `5c6d107f7ca6`  |
| 2142   | Layout 2 | `5c6d107f7ca6`  |
| 2138   | Layout 2 | `5c6d107f7ca6`  |
| 2134   | Layout 2 | `5c6d107f7ca6`  |
| 2130   | Layout 1 | `5c6d107f7ca6`  |
| 2122   | Layout 1 | `5c6d107f7ca6`  |
| 2107   | Layout 1 | `5c6d107f7ca6`  |
| 2098   | Layout 1 | `5c6d107f7ca6`  |
| 2089   | Layout 1 | `5c6d107f7ca6`  |
| 2081   | Layout 1 | `5c6d107f7ca6`  |
| 2073   | Layout 1 | `5c6d107f7ca6`  |
| 2067   | Layout 1 | `5c6d107f7ca6`  |
| 2063   | Layout 1 | `5c6d107f7ca6`  |
| 2059   | Layout 1 | `5c6d107f7ca6`  |
| 2052   | Layout 1 | `5c6d107f7ca6`  |
| 2044   | Layout 1 | `5c6d107f7ca6`  |
| 2039   | Layout 1 | `5c6d107f7ca6`  |
| 2032   | Layout 1 | `5c6d107f7ca6`  |
| 2025   | Layout 1 | `5c6d107f7ca6`  |
| 2011   | Layout 1 | `5c6d107f7ca6`  |
| 2005   | Layout 1 | `5c6d107f7ca6`  |
| 2000   | Layout 1 | `5c6d107f7ca6`  |
| 1996   | Layout 1 | `5c6d107f7ca6`  |
| 1991   | Layout 1 | `5c6d107f7ca6`  |
| 1985   | Layout 1 | `5c6d107f7ca6`  |
| 1980   | Layout 1 | `5c6d107f7ca6`  |
| 1969   | Layout 1 | `5c6d107f7ca6`  |
| 1964   | Layout 1 | `5c6d107f7ca6`  |
| 1958   | Layout 1 | `5c6d107f7ca6`  |
| 1950   | Layout 1 | `5c6d107f7ca6`  |
| 1945   | Layout 1 | `5c6d107f7ca6`  |
| 1937   | Layout 1 | `5c6d107f7ca6`  |
| 1933   | Layout 1 | `5c6d107f7ca6`  |
| 1927   | Layout 1 | `5c6d107f7ca6`  |
| 1921   | Layout 1 | `5c6d107f7ca6`  |
| 1914   | Layout 1 | `5c6d107f7ca6`  |
| 1908   | Layout 1 | `5c6d107f7ca6`  |
| 1897   | Layout 1 | `5c6d107f7ca6`  |
| 1892   | Layout 1 | `5c6d107f7ca6`  |
| 1886   | Layout 1 | `5c6d107f7ca6`  |
| 1881   | Layout 1 | `5c6d107f7ca6`  |
| 1871   | Layout 1 | `5c6d107f7ca6`  |
| 1866   | Layout 1 | `5c6d107f7ca6`  |
| 1862   | Layout 1 | `5c6d107f7ca6`  |
| 1854   | Layout 1 | `5c6d107f7ca6`  |
| 1846   | Layout 1 | `5c6d107f7ca6`  |
| 1838   | Layout 1 | `5c6d107f7ca6`  |
| 1832   | Layout 1 | `5c6d107f7ca6`  |
| 1826   | Layout 1 | `5c6d107f7ca6`  |
| 1822   | Layout 1 | `5c6d107f7ca6`  |
| 1818   | Layout 1 | `5c6d107f7ca6`  |
| 1804   | Layout 1 | `5c6d107f7ca6`  |
| 1794   | Layout 1 | `5c6d107f7ca6`  |
| 1790   | Layout 1 | `5c6d107f7ca6`  |
| 1784   | Layout 1 | `5c6d107f7ca6`  |
| 1774   | Layout 1 | `5c6d107f7ca6`  |
| 1771   | Layout 1 | `5c6d107f7ca6`  |
| 1762   | Layout 1 | `5c6d107f7ca6`  |
| 1759   | Layout 1 | `5c6d107f7ca6`  |
| 1754   | Layout 1 | `5c6d107f7ca6`  |
| 1749   | Layout 1 | `5c6d107f7ca6`  |
| 1743   | Layout 1 | `5c6d107f7ca6`  |
| 1737   | Layout 1 | `5c6d107f7ca6`  |
| 1731   | Layout 1 | `5c6d107f7ca6`  |
| 1725   | Layout 1 | `5c6d107f7ca6`  |
| 1717   | Layout 1 | `5c6d107f7ca6`  |
| 1710   | Layout 1 | `5c6d107f7ca6`  |
| 1704   | Layout 1 | `5c6d107f7ca6`  |
| 1698   | Layout 1 | `5c6d107f7ca6`  |
| 1690   | Layout 1 | `5c6d107f7ca6`  |
| 1685   | Layout 1 | `5c6d107f7ca6`  |
| 1680   | Layout 1 | `5c6d107f7ca6`  |
| 1674   | Layout 1 | `5c6d107f7ca6`  |
| 1668   | Layout 1 | `5c6d107f7ca6`  |
| 1659   | Layout 1 | `5c6d107f7ca6`  |
| 1649   | Layout 1 | `5c6d107f7ca6`  |
| 1642   | Layout 1 | `5c6d107f7ca6`  |
| 1636   | Layout 1 | `5c6d107f7ca6`  |
| 1628   | Layout 1 | `5c6d107f7ca6`  |
| 1622   | Layout 1 | `5c6d107f7ca6`  |
| 1614   | Layout 1 | `5c6d107f7ca6`  |
| 1608   | Layout 1 | `5c6d107f7ca6`  |
| 1602   | Layout 1 | `5c6d107f7ca6`  |
| 1598   | Layout 1 | `5c6d107f7ca6`  |
| 1594   | Layout 1 | `5c6d107f7ca6`  |
| 1590   | Layout 1 | `5c6d107f7ca6`  |
| 1587   | Layout 1 | `5c6d107f7ca6`  |
| 1584   | Layout 1 | `5c6d107f7ca6`  |
| 1579   | Layout 1 | `5c6d107f7ca6`  |
| 1572   | Layout 1 | `5c6d107f7ca6`  |
| 1565   | Layout 1 | `5c6d107f7ca6`  |
| 1559   | Layout 1 | `5c6d107f7ca6`  |
| 1554   | Layout 1 | `5c6d107f7ca6`  |
| 1547   | Layout 1 | `5c6d107f7ca6`  |
| 1537   | Layout 1 | `5c6d107f7ca6`  |
| 1529   | Layout 1 | `5c6d107f7ca6`  |
| 1524   | Layout 1 | `5c6d107f7ca6`  |
| 1519   | Layout 1 | `5c6d107f7ca6`  |
| 1509   | Layout 1 | `5c6d107f7ca6`  |
| 1506   | Layout 1 | `5c6d107f7ca6`  |
| 1504   | Layout 1 | `5c6d107f7ca6`  |
| 1500   | Layout 1 | `5c6d107f7ca6`  |
| 1493   | Layout 1 | `5c6d107f7ca6`  |
| 1489   | Layout 1 | `5c6d107f7ca6`  |
| 1485   | Layout 1 | `5c6d107f7ca6`  |
| 1481   | Layout 1 | `5c6d107f7ca6`  |
| 1474   | Layout 1 | `5c6d107f7ca6`  |
| 1466   | Layout 1 | `5c6d107f7ca6`  |
| 1462   | Layout 1 | `5c6d107f7ca6`  |
| 1459   | Layout 1 | `5c6d107f7ca6`  |
| 1453   | Layout 1 | `5c6d107f7ca6`  |
| 1450   | Layout 1 | `5c6d107f7ca6`  |
| 1445   | Layout 1 | `5c6d107f7ca6`  |
| 1439   | Layout 1 | `5c6d107f7ca6`  |
| 1433   | Layout 1 | `5c6d107f7ca6`  |
| 1430   | Layout 1 | `5c6d107f7ca6`  |
| 1426   | Layout 1 | `5c6d107f7ca6`  |
| 1421   | Layout 1 | `5c6d107f7ca6`  |
| 1417   | Layout 1 | `5c6d107f7ca6`  |
| 1416   | Layout 1 | `5c6d107f7ca6`  |
| 1409   | Layout 1 | `5c6d107f7ca6`  |
| 1405   | Layout 1 | `5c6d107f7ca6`  |
| 1401   | Layout 1 | `5c6d107f7ca6`  |
| 1396   | Layout 1 | `5c6d107f7ca6`  |
| 1391   | Layout 1 | `5c6d107f7ca6`  |
| 1390   | Layout 1 | `5c6d107f7ca6`  |
| 1386   | Layout 1 | `5c6d107f7ca6`  |
| 1381   | Layout 1 | `5c6d107f7ca6`  |
| 1379   | Layout 1 | `5c6d107f7ca6`  |
| 1372   | Layout 1 | `5c6d107f7ca6`  |
| 1366   | Layout 1 | `5c6d107f7ca6`  |
| 1364   | Layout 1 | `5c6d107f7ca6`  |
| 1363   | Layout 1 | `5c6d107f7ca6`  |
| 1360   | Layout 1 | `5c6d107f7ca6`  |
| 1358   | Layout 1 | `5c6d107f7ca6`  |
| 1355   | Layout 1 | `5c6d107f7ca6`  |
| 1351   | Layout 1 | `5c6d107f7ca6`  |
| 1348   | Layout 1 | `5c6d107f7ca6`  |
| 1346   | Layout 1 | `5c6d107f7ca6`  |
| 1341   | Layout 1 | `5c6d107f7ca6`  |
| 1340   | Layout 1 | `5c6d107f7ca6`  |
| 1338   | Layout 1 | `5c6d107f7ca6`  |
| 1335   | Layout 1 | `5c6d107f7ca6`  |
| 1333   | Layout 1 | `5c6d107f7ca6`  |
| 1329   | Layout 1 | `5c6d107f7ca6`  |
| 1327   | Layout 1 | `5c6d107f7ca6`  |
| 1324   | Layout 1 | `5c6d107f7ca6`  |
| 1321   | Layout 1 | `5c6d107f7ca6`  |
| 1319   | Layout 1 | `5c6d107f7ca6`  |
| 1318   | Layout 1 | `5c6d107f7ca6`  |
| 1316   | Layout 1 | `5c6d107f7ca6`  |
| 1313   | Layout 1 | `5c6d107f7ca6`  |
| 1311   | Layout 1 | `5c6d107f7ca6`  |
| 1309   | Layout 1 | `5c6d107f7ca6`  |
| 1304   | Layout 1 | `5c6d107f7ca6`  |
| 1292   | Layout 1 | `5c6d107f7ca6`  |
| 1286   | Layout 1 | `5c6d107f7ca6`  |
| 1280   | Layout 1 | `5c6d107f7ca6`  |
| 1276   | No file  | `5c6d107f7ca6`  |
| 1267   | No file  | `5c6d107f7ca6`  |
| 1261   | No file  | `5c6d107f7ca6`  |
| 1256   | No file  | `5c6d107f7ca6`  |
| 1250   | No file  | `5c6d107f7ca6`  |
| 1246   | No file  | `5c6d107f7ca6`  |
| 1239   | No file  | `5c6d107f7ca6`  |
| 1230   | No file  | `5c6d107f7ca6`  |
| 1226   | No file  | `5c6d107f7ca6`  |
| 1220   | No file  | `5c6d107f7ca6`  |
| 1217   | No file  | `5c6d107f7ca6`  |
| 1211   | No file  | `5c6d107f7ca6`  |
| 1210   | No file  | `5c6d107f7ca6`  |
| 1208   | No file  | `5c6d107f7ca6`  |
| 1203   | No file  | `5c6d107f7ca6`  |
| 1197   | No file  | `5c6d107f7ca6`  |
| 1194   | No file  | `5c6d107f7ca6`  |
| 1192   | No file  | `5c6d107f7ca6`  |
| 1187   | No file  | `5c6d107f7ca6`  |
| 1183   | No file  | `5c6d107f7ca6`  |
| 1177   | No file  | `5c6d107f7ca6`  |
| 1173   | No file  | `5c6d107f7ca6`  |
| 1167   | No file  | `5c6d107f7ca6`  |
| 1164   | No file  | `5c6d107f7ca6`  |
| 1156   | No file  | `5c6d107f7ca6`  |
| 1149   | No file  | `5c6d107f7ca6`  |
| 1144   | No file  | `5c6d107f7ca6`  |
| 1137   | No file  | `5c6d107f7ca6`  |
| 1132   | No file  | `5c6d107f7ca6`  |
| 1127   | No file  | `5c6d107f7ca6`  |
| 1122   | No file  | `5c6d107f7ca6`  |
| 1118   | No file  | `5c6d107f7ca6`  |
| 1114   | No file  | `5c6d107f7ca6`  |
| 1109   | No file  | `5c6d107f7ca6`  |
| 1102   | No file  | `5c6d107f7ca6`  |
| 1096   | No file  | `5c6d107f7ca6`  |
| 1088   | No file  | `5c6d107f7ca6`  |
| 1081   | No file  | `5c6d107f7ca6`  |
| 1076   | No file  | `5c6d107f7ca6`  |
| 1069   | No file  | `5c6d107f7ca6`  |
| 1064   | No file  | `5c6d107f7ca6`  |
| 1058   | No file  | `5c6d107f7ca6`  |
| 1051   | No file  | `5c6d107f7ca6`  |
| 1044   | No file  | `5c6d107f7ca6`  |
| 1036   | No file  | `5c6d107f7ca6`  |
| 1026   | No file  | `5c6d107f7ca6`  |
| 1016   | No file  | `5c6d107f7ca6`  |
| 1009   | No file  | `5c6d107f7ca6`  |
| 1005   | No file  | `5c6d107f7ca6`  |
| 1000   | No file  | `5c6d107f7ca6`  |
| 998    | No file  | `5c6d107f7ca6`  |
| 990    | No file  | `5c6d107f7ca6`  |
| 979    | No file  | `5c6d107f7ca6`  |
| 972    | No file  | `5c6d107f7ca6`  |
| 963    | No file  | `5c6d107f7ca6`  |
| 955    | No file  | `5c6d107f7ca6`  |
| 946    | No file  | `5c6d107f7ca6`  |
| 938    | No file  | `5c6d107f7ca6`  |
| 927    | No file  | `5c6d107f7ca6`  |
| 911    | No file  | `5c6d107f7ca6`  |
| 904    | No file  | `5c6d107f7ca6`  |
| 899    | No file  | `5c6d107f7ca6`  |
| 894    | No file  | `5c6d107f7ca6`  |
| 885    | No file  | `5c6d107f7ca6`  |
| 879    | No file  | `5c6d107f7ca6`  |
| 872    | No file  | `5c6d107f7ca6`  |
| 864    | No file  | `5c6d107f7ca6`  |
| 855    | No file  | `5c6d107f7ca6`  |
| 853    | No file  | `5c6d107f7ca6`  |
| 845    | No file  | `5c6d107f7ca6`  |
| 837    | No file  | `5c6d107f7ca6`  |
| 829    | No file  | `5c6d107f7ca6`  |
| 822    | No file  | `5c6d107f7ca6`  |
| 814    | No file  | `5c6d107f7ca6`  |
| 805    | No file  | `5c6d107f7ca6`  |
| 794    | No file  | `5c6d107f7ca6`  |
| 787    | No file  | `5c6d107f7ca6`  |
| 780    | No file  | `5c6d107f7ca6`  |
| 771    | No file  | `5c6d107f7ca6`  |
| 760    | No file  | `5c6d107f7ca6`  |
| 748    | No file  | `5c6d107f7ca6`  |
| 741    | No file  | `5c6d107f7ca6`  |
| 736    | No file  | `5c6d107f7ca6`  |
| 731    | No file  | `5c6d107f7ca6`  |
| 723    | No file  | `5c6d107f7ca6`  |
| 711    | No file  | `5c6d107f7ca6`  |
| 707    | No file  | `5c6d107f7ca6`  |
| 697    | No file  | `5c6d107f7ca6`  |
| 689    | No file  | `5c6d107f7ca6`  |
| 683    | No file  | `5c6d107f7ca6`  |
| 678    | No file  | `5c6d107f7ca6`  |
| 670    | No file  | `5c6d107f7ca6`  |
| 661    | No file  | `5c6d107f7ca6`  |
| 656    | No file  | `5c6d107f7ca6`  |
| 652    | No file  | `5c6d107f7ca6`  |
| 643    | No file  | `5c6d107f7ca6`  |
| 637    | No file  | `5c6d107f7ca6`  |
| 630    | No file  | `5c6d107f7ca6`  |
| 627    | No file  | `5c6d107f7ca6`  |
| 621    | No file  | `5c6d107f7ca6`  |
| 617    | No file  | `5c6d107f7ca6`  |
| 615    | No file  | `5c6d107f7ca6`  |
| 606    | No file  | `5c6d107f7ca6`  |
| 599    | No file  | `5c6d107f7ca6`  |
| 592    | No file  | `5c6d107f7ca6`  |
| 586    | No file  | `5c6d107f7ca6`  |
| 577    | No file  | `5c6d107f7ca6`  |
| 569    | No file  | `5c6d107f7ca6`  |
| 561    | No file  | `5c6d107f7ca6`  |
| 554    | No file  | `5c6d107f7ca6`  |
| 542    | No file  | `5c6d107f7ca6`  |
| 532    | No file  | `5c6d107f7ca6`  |
| 531    | No file  | `5c6d107f7ca6`  |
| 526    | No file  | `5c6d107f7ca6`  |
| 521    | No file  | `5c6d107f7ca6`  |
| 517    | No file  | `5c6d107f7ca6`  |
| 510    | No file  | `5c6d107f7ca6`  |
| 508    | No file  | `5c6d107f7ca6`  |
| 504    | No file  | `5c6d107f7ca6`  |
| 497    | No file  | `5c6d107f7ca6`  |
| 491    | No file  | `5c6d107f7ca6`  |
| 485    | No file  | `5c6d107f7ca6`  |
| 478    | No file  | `5c6d107f7ca6`  |
| 472    | No file  | `5c6d107f7ca6`  |
| 466    | No file  | `5c6d107f7ca6`  |
| 457    | No file  | `5c6d107f7ca6`  |
| 452    | No file  | `5c6d107f7ca6`  |
| 449    | No file  | `5c6d107f7ca6`  |
| 435    | No file  | `5c6d107f7ca6`  |

<!-- versions:end -->

## Companion Files

| File                                 | Required | Role                                                                       |
| ------------------------------------ | -------- | -------------------------------------------------------------------------- |
| `personalmonsterpositionoffset.dbss` | Optional | `position_index -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 48 x 22 = 1,060 bytes.

### Row (22 bytes)

| Offset  | Type | Field          | Notes                                                        |
| ------- | ---- | -------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | position_index | Row key; `1` to `48` on client 3474, in that order           |
| `+0x04` | f32  | x              | World position                                               |
| `+0x08` | f32  | y              | Height                                                       |
| `+0x0C` | f32  | z              |                                                              |
| `+0x10` | f32  | spawn_distance | How far from the point the boss spawns; `5000` on every row of clients 1784 and 3474 |
| `+0x14` | u16  | unknown_14     | `1` on every row of client 3474; not in client 1784          |

### `personalmonsterpositionoffset.dbss`

Bare offset table into `personalmonsterposition.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                           |
| ------- | ----------------- | ----- | ----------------------------------------------- |
| `+0x00` | u32               | count | Equals the `personalmonsterposition.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                  |

### Offset Row (12 bytes)

| Offset  | Type | Field          | Notes                                                                   |
| ------- | ---- | -------------- | ----------------------------------------------------------------------- |
| `+0x00` | u32  | position_index | Key of the row it points at                                             |
| `+0x04` | u32  | data_offset    | Absolute offset of the row in `personalmonsterposition.dbss`, at its `position_index` |
| `+0x08` | u32  | data_size      | The whole row: `22` on client 3474, `20` on client 1784                  |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. On
clients 1784 and 3474 every index row points at the row with its key, and
the rows fill the file.

## Layout 1

Client 1784 has no `unknown_14`: its rows are 20 bytes, and the file is
4 + 47 x 20 = 944 bytes.

### Row (20 bytes)

| Offset  | Type | Field          | Notes |
| ------- | ---- | -------------- | ----- |
| `+0x00` | u32  | position_index |       |
| `+0x04` | f32  | x              |       |
| `+0x08` | f32  | y              |       |
| `+0x0C` | f32  | z              |       |
| `+0x10` | f32  | spawn_distance |       |

## Field Names

The `PersonalMonsterPosition_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `Index`,
`SpawnPosition` (three numbers) and `SpawnDistance`. Its 47 rows match the
client 1784 file on all 47 indexes for the position (to 0.01) and the
distance. On client 3474, 37 of those 47 points are unchanged, 10 moved
(indexes `5`, `7`, `8`, `9`, `12`, `14`, `15`, `16`, `17` and `40`) and
index `48` is new. The sheet's developer note on `SpawnDistance` says it
sets how far from the place the monster spawns. `position_index` is the
sheet's `Index`, which the server-only `PositionIndex` column of
`PersonalMonster_Table` names; the 2016 client's debug symbols have no
personal monster type.

## Notes

- The client Lua of client 3474 reads no row of this file directly: it
  navigates to `ToClient_GetReservePersonalMonsterPosition(reserveIndex)`,
  the point the server reserved for a boss, and
  `ToClient_FindReservedPersonalMonsterInfoWrapper(characterKey):getSpawnPosition()`.
- The rows hold no region key. The sheet's note column (`#비고`, not
  compiled) names a place per index on client 1784, `아그리스 제단`
  (Altar of Agris) for index `1`.

## Open Questions

### unknown_14

Client 3474 added a u16 that is `1` on all 48 rows. Field `1` of
[`fieldinfo.bss`](../bss/fieldinfo_bss.md) is the open world (`월드`), and the
Lua calls `ToClient_GetPersonalMonsterFieldNobyIndex(reserveIndex)` before
it navigates to a reserved boss, so the u16 may be the field number of the
point. With one value on every row, nothing confirms it.
