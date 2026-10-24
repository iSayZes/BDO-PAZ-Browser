# `instancefieldranking.bss` Format

## Purpose

Which season rankings each instance field type shows on the client's
service: per instance field type a list of `ranking_idx` keys of
[`instancefieldrankingmanage.bss`](instancefieldrankingmanage_bss.md). On
client 3482 types `0` to `23` have a row; types `11` to `23` list ranking
`7`, the NA/EU season 1 ranking of the Old Moon Grand Prix (instance
type `11`), and the others list none. The file is the `InstanceRanking`
sheet compiled into a PABR table, with the sheet's row for one service.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records | Row bytes             |
| ------ | -------------- | ------- | -------------------------- | ----- | ------- | --------------------- |
| 1      | 1506 and later | 3483    | `instancefieldranking.bss` | 216   | 24 Row  | 6 to 10, 8 on average |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 1      | `instancefieldranking.bss` | 216 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `7a2c05c04d03`  |
| 3482   | Layout 1 | `7a2c05c04d03`  |
| 3474   | Layout 1 | `7a2c05c04d03`  |
| 3473   | Layout 1 | `7a2c05c04d03`  |
| 3464   | Layout 1 | `7a2c05c04d03`  |
| 3458   | Layout 1 | `7a2c05c04d03`  |
| 3454   | Layout 1 | `7a2c05c04d03`  |
| 3444   | Layout 1 | `7a2c05c04d03`  |
| 3435   | Layout 1 | `7a2c05c04d03`  |
| 3426   | Layout 1 | `7a2c05c04d03`  |
| 3418   | Layout 1 | `7a2c05c04d03`  |
| 3412   | Layout 1 | `7a2c05c04d03`  |
| 3402   | Layout 1 | `7a2c05c04d03`  |
| 3396   | Layout 1 | `7a2c05c04d03`  |
| 3387   | Layout 1 | `7a2c05c04d03`  |
| 3381   | Layout 1 | `7a2c05c04d03`  |
| 3373   | Layout 1 | `7a2c05c04d03`  |
| 3364   | Layout 1 | `7a2c05c04d03`  |
| 3356   | Layout 1 | `7a2c05c04d03`  |
| 3349   | Layout 1 | `7a2c05c04d03`  |
| 3342   | Layout 1 | `7a2c05c04d03`  |
| 3335   | Layout 1 | `7a2c05c04d03`  |
| 3326   | Layout 1 | `7a2c05c04d03`  |
| 3321   | Layout 1 | `7a2c05c04d03`  |
| 3314   | Layout 1 | `7a2c05c04d03`  |
| 3303   | Layout 1 | `7a2c05c04d03`  |
| 3302   | Layout 1 | `7a2c05c04d03`  |
| 3293   | Layout 1 | `7a2c05c04d03`  |
| 3283   | Layout 1 | `7a2c05c04d03`  |
| 3275   | Layout 1 | `7a2c05c04d03`  |
| 3267   | Layout 1 | `7a2c05c04d03`  |
| 3258   | Layout 1 | `7a2c05c04d03`  |
| 3251   | Layout 1 | `7a2c05c04d03`  |
| 3242   | Layout 1 | `7a2c05c04d03`  |
| 3235   | Layout 1 | `7a2c05c04d03`  |
| 3229   | Layout 1 | `7a2c05c04d03`  |
| 3212   | Layout 1 | `7a2c05c04d03`  |
| 3203   | Layout 1 | `7a2c05c04d03`  |
| 3193   | Layout 1 | `7a2c05c04d03`  |
| 3186   | Layout 1 | `7a2c05c04d03`  |
| 3177   | Layout 1 | `7a2c05c04d03`  |
| 3169   | Layout 1 | `7a2c05c04d03`  |
| 3158   | Layout 1 | `7a2c05c04d03`  |
| 3151   | Layout 1 | `7a2c05c04d03`  |
| 3144   | Layout 1 | `7a2c05c04d03`  |
| 3133   | Layout 1 | `7a2c05c04d03`  |
| 3125   | Layout 1 | `7a2c05c04d03`  |
| 3118   | Layout 1 | `7a2c05c04d03`  |
| 3111   | Layout 1 | `7a2c05c04d03`  |
| 3103   | Layout 1 | `7a2c05c04d03`  |
| 3095   | Layout 1 | `7a2c05c04d03`  |
| 3086   | Layout 1 | `7a2c05c04d03`  |
| 3072   | Layout 1 | `7a2c05c04d03`  |
| 3062   | Layout 1 | `7a2c05c04d03`  |
| 3052   | Layout 1 | `7a2c05c04d03`  |
| 3045   | Layout 1 | `7a2c05c04d03`  |
| 3037   | Layout 1 | `7a2c05c04d03`  |
| 3030   | Layout 1 | `7a2c05c04d03`  |
| 3021   | Layout 1 | `7a2c05c04d03`  |
| 3012   | Layout 1 | `7a2c05c04d03`  |
| 3002   | Layout 1 | `7a2c05c04d03`  |
| 2995   | Layout 1 | `7a2c05c04d03`  |
| 2987   | Layout 1 | `7a2c05c04d03`  |
| 2978   | Layout 1 | `7a2c05c04d03`  |
| 2970   | Layout 1 | `7a2c05c04d03`  |
| 2959   | Layout 1 | `7a2c05c04d03`  |
| 2951   | Layout 1 | `7a2c05c04d03`  |
| 2942   | Layout 1 | `7a2c05c04d03`  |
| 2935   | Layout 1 | `7a2c05c04d03`  |
| 2932   | Layout 1 | `7a2c05c04d03`  |
| 2923   | Layout 1 | `7a2c05c04d03`  |
| 2919   | Layout 1 | `7a2c05c04d03`  |
| 2907   | Layout 1 | `7a2c05c04d03`  |
| 2900   | Layout 1 | `7a2c05c04d03`  |
| 2891   | Layout 1 | `7a2c05c04d03`  |
| 2882   | Layout 1 | `7a2c05c04d03`  |
| 2872   | Layout 1 | `7a2c05c04d03`  |
| 2863   | Layout 1 | `7a2c05c04d03`  |
| 2855   | Layout 1 | `7a2c05c04d03`  |
| 2849   | Layout 1 | `7a2c05c04d03`  |
| 2844   | Layout 1 | `7a2c05c04d03`  |
| 2834   | Layout 1 | `7a2c05c04d03`  |
| 2825   | Layout 1 | `7a2c05c04d03`  |
| 2819   | Layout 1 | `7a2c05c04d03`  |
| 2811   | Layout 1 | `7a2c05c04d03`  |
| 2803   | Layout 1 | `7a2c05c04d03`  |
| 2794   | Layout 1 | `7a2c05c04d03`  |
| 2783   | Layout 1 | `7a2c05c04d03`  |
| 2774   | Layout 1 | `7a2c05c04d03`  |
| 2765   | Layout 1 | `7a2c05c04d03`  |
| 2756   | Layout 1 | `7a2c05c04d03`  |
| 2750   | Layout 1 | `7a2c05c04d03`  |
| 2743   | Layout 1 | `7a2c05c04d03`  |
| 2736   | Layout 1 | `7a2c05c04d03`  |
| 2726   | Layout 1 | `7a2c05c04d03`  |
| 2717   | Layout 1 | `7a2c05c04d03`  |
| 2709   | Layout 1 | `7a2c05c04d03`  |
| 2703   | Layout 1 | `7a2c05c04d03`  |
| 2695   | Layout 1 | `7a2c05c04d03`  |
| 2684   | Layout 1 | `7a2c05c04d03`  |
| 2672   | Layout 1 | `7a2c05c04d03`  |
| 2665   | Layout 1 | `7a2c05c04d03`  |
| 2657   | Layout 1 | `7a2c05c04d03`  |
| 2649   | Layout 1 | `7a2c05c04d03`  |
| 2644   | Layout 1 | `7a2c05c04d03`  |
| 2637   | Layout 1 | `7a2c05c04d03`  |
| 2629   | Layout 1 | `7a2c05c04d03`  |
| 2619   | Layout 1 | `7a2c05c04d03`  |
| 2612   | Layout 1 | `7a2c05c04d03`  |
| 2606   | Layout 1 | `7a2c05c04d03`  |
| 2602   | Layout 1 | `7a2c05c04d03`  |
| 2601   | Layout 1 | `7a2c05c04d03`  |
| 2592   | Layout 1 | `7a2c05c04d03`  |
| 2583   | Layout 1 | `7a2c05c04d03`  |
| 2575   | Layout 1 | `7a2c05c04d03`  |
| 2567   | Layout 1 | `7a2c05c04d03`  |
| 2560   | Layout 1 | `7a2c05c04d03`  |
| 2553   | Layout 1 | `7a2c05c04d03`  |
| 2545   | Layout 1 | `7a2c05c04d03`  |
| 2538   | Layout 1 | `7a2c05c04d03`  |
| 2529   | Layout 1 | `7a2c05c04d03`  |
| 2519   | Layout 1 | `7a2c05c04d03`  |
| 2513   | Layout 1 | `7a2c05c04d03`  |
| 2510   | Layout 1 | `7a2c05c04d03`  |
| 2507   | Layout 1 | `7a2c05c04d03`  |
| 2503   | Layout 1 | `7a2c05c04d03`  |
| 2498   | Layout 1 | `7a2c05c04d03`  |
| 2492   | Layout 1 | `7a2c05c04d03`  |
| 2487   | Layout 1 | `7a2c05c04d03`  |
| 2480   | Layout 1 | `7a2c05c04d03`  |
| 2474   | Layout 1 | `7a2c05c04d03`  |
| 2468   | Layout 1 | `7a2c05c04d03`  |
| 2460   | Layout 1 | `7a2c05c04d03`  |
| 2453   | Layout 1 | `7a2c05c04d03`  |
| 2444   | Layout 1 | `7a2c05c04d03`  |
| 2438   | Layout 1 | `7a2c05c04d03`  |
| 2434   | Layout 1 | `7a2c05c04d03`  |
| 2429   | Layout 1 | `7a2c05c04d03`  |
| 2421   | Layout 1 | `7a2c05c04d03`  |
| 2414   | Layout 1 | `7a2c05c04d03`  |
| 2407   | Layout 1 | `7a2c05c04d03`  |
| 2401   | Layout 1 | `7a2c05c04d03`  |
| 2397   | Layout 1 | `7a2c05c04d03`  |
| 2393   | Layout 1 | `7a2c05c04d03`  |
| 2384   | Layout 1 | `7a2c05c04d03`  |
| 2378   | Layout 1 | `7a2c05c04d03`  |
| 2372   | Layout 1 | `7a2c05c04d03`  |
| 2358   | Layout 1 | `7a2c05c04d03`  |
| 2352   | Layout 1 | `7a2c05c04d03`  |
| 2347   | Layout 1 | `7a2c05c04d03`  |
| 2343   | Layout 1 | `7a2c05c04d03`  |
| 2335   | Layout 1 | `7a2c05c04d03`  |
| 2327   | Layout 1 | `7a2c05c04d03`  |
| 2324   | Layout 1 | `7a2c05c04d03`  |
| 2319   | Layout 1 | `7a2c05c04d03`  |
| 2313   | Layout 1 | `7a2c05c04d03`  |
| 2308   | Layout 1 | `7a2c05c04d03`  |
| 2302   | Layout 1 | `7a2c05c04d03`  |
| 2295   | Layout 1 | `7a2c05c04d03`  |
| 2290   | Layout 1 | `7a2c05c04d03`  |
| 2284   | Layout 1 | `7a2c05c04d03`  |
| 2276   | Layout 1 | `7a2c05c04d03`  |
| 2269   | Layout 1 | `7a2c05c04d03`  |
| 2259   | Layout 1 | `7a2c05c04d03`  |
| 2250   | Layout 1 | `7a2c05c04d03`  |
| 2243   | Layout 1 | `7a2c05c04d03`  |
| 2235   | Layout 1 | `7a2c05c04d03`  |
| 2229   | Layout 1 | `7a2c05c04d03`  |
| 2224   | Layout 1 | `7a2c05c04d03`  |
| 2218   | Layout 1 | `7a2c05c04d03`  |
| 2215   | Layout 1 | `7a2c05c04d03`  |
| 2207   | Layout 1 | `7a2c05c04d03`  |
| 2203   | Layout 1 | `7a2c05c04d03`  |
| 2196   | Layout 1 | `7a2c05c04d03`  |
| 2192   | Layout 1 | `7a2c05c04d03`  |
| 2189   | Layout 1 | `7a2c05c04d03`  |
| 2183   | Layout 1 | `7a2c05c04d03`  |
| 2179   | Layout 1 | `7a2c05c04d03`  |
| 2171   | Layout 1 | `7a2c05c04d03`  |
| 2163   | Layout 1 | `7a2c05c04d03`  |
| 2156   | Layout 1 | `7a2c05c04d03`  |
| 2151   | Layout 1 | `7a2c05c04d03`  |
| 2147   | Layout 1 | `7a2c05c04d03`  |
| 2142   | Layout 1 | `7a2c05c04d03`  |
| 2138   | Layout 1 | `7a2c05c04d03`  |
| 2134   | Layout 1 | `7a2c05c04d03`  |
| 2130   | Layout 1 | `7a2c05c04d03`  |
| 2122   | Layout 1 | `7a2c05c04d03`  |
| 2107   | Layout 1 | `7a2c05c04d03`  |
| 2098   | Layout 1 | `7a2c05c04d03`  |
| 2089   | Layout 1 | `7a2c05c04d03`  |
| 2081   | Layout 1 | `7a2c05c04d03`  |
| 2073   | Layout 1 | `7a2c05c04d03`  |
| 2067   | Layout 1 | `7a2c05c04d03`  |
| 2063   | Layout 1 | `7a2c05c04d03`  |
| 2059   | Layout 1 | `7a2c05c04d03`  |
| 2052   | Layout 1 | `7a2c05c04d03`  |
| 2044   | Layout 1 | `7a2c05c04d03`  |
| 2039   | Layout 1 | `7a2c05c04d03`  |
| 2032   | Layout 1 | `7a2c05c04d03`  |
| 2025   | Layout 1 | `7a2c05c04d03`  |
| 2011   | Layout 1 | `7a2c05c04d03`  |
| 2005   | Layout 1 | `7a2c05c04d03`  |
| 2000   | Layout 1 | `7a2c05c04d03`  |
| 1996   | Layout 1 | `7a2c05c04d03`  |
| 1991   | Layout 1 | `7a2c05c04d03`  |
| 1985   | Layout 1 | `7a2c05c04d03`  |
| 1980   | Layout 1 | `7a2c05c04d03`  |
| 1969   | Layout 1 | `7a2c05c04d03`  |
| 1964   | Layout 1 | `7a2c05c04d03`  |
| 1958   | Layout 1 | `7a2c05c04d03`  |
| 1950   | Layout 1 | `7a2c05c04d03`  |
| 1945   | Layout 1 | `7a2c05c04d03`  |
| 1937   | Layout 1 | `7a2c05c04d03`  |
| 1933   | Layout 1 | `7a2c05c04d03`  |
| 1927   | Layout 1 | `7a2c05c04d03`  |
| 1921   | Layout 1 | `7a2c05c04d03`  |
| 1914   | Layout 1 | `7a2c05c04d03`  |
| 1908   | Layout 1 | `7a2c05c04d03`  |
| 1897   | Layout 1 | `7a2c05c04d03`  |
| 1892   | Layout 1 | `7a2c05c04d03`  |
| 1886   | Layout 1 | `7a2c05c04d03`  |
| 1881   | Layout 1 | `7a2c05c04d03`  |
| 1871   | Layout 1 | `7a2c05c04d03`  |
| 1866   | Layout 1 | `7a2c05c04d03`  |
| 1862   | Layout 1 | `7a2c05c04d03`  |
| 1854   | Layout 1 | `7a2c05c04d03`  |
| 1846   | Layout 1 | `7a2c05c04d03`  |
| 1838   | Layout 1 | `7a2c05c04d03`  |
| 1832   | Layout 1 | `7a2c05c04d03`  |
| 1826   | Layout 1 | `7a2c05c04d03`  |
| 1822   | Layout 1 | `7a2c05c04d03`  |
| 1818   | Layout 1 | `7a2c05c04d03`  |
| 1804   | Layout 1 | `7a2c05c04d03`  |
| 1794   | Layout 1 | `7a2c05c04d03`  |
| 1790   | Layout 1 | `7a2c05c04d03`  |
| 1784   | Layout 1 | `7a2c05c04d03`  |
| 1774   | Layout 1 | `7a2c05c04d03`  |
| 1771   | Layout 1 | `7a2c05c04d03`  |
| 1762   | Layout 1 | `7a2c05c04d03`  |
| 1759   | Layout 1 | `7a2c05c04d03`  |
| 1754   | Layout 1 | `7a2c05c04d03`  |
| 1749   | Layout 1 | `7a2c05c04d03`  |
| 1743   | Layout 1 | `7a2c05c04d03`  |
| 1737   | Layout 1 | `7a2c05c04d03`  |
| 1731   | Layout 1 | `7a2c05c04d03`  |
| 1725   | Layout 1 | `7a2c05c04d03`  |
| 1717   | Layout 1 | `7a2c05c04d03`  |
| 1710   | Layout 1 | `7a2c05c04d03`  |
| 1704   | Layout 1 | `7a2c05c04d03`  |
| 1698   | Layout 1 | `7a2c05c04d03`  |
| 1690   | Layout 1 | `7a2c05c04d03`  |
| 1685   | Layout 1 | `7a2c05c04d03`  |
| 1680   | Layout 1 | `7a2c05c04d03`  |
| 1674   | Layout 1 | `7a2c05c04d03`  |
| 1668   | Layout 1 | `7a2c05c04d03`  |
| 1659   | Layout 1 | `7a2c05c04d03`  |
| 1649   | Layout 1 | `7a2c05c04d03`  |
| 1642   | Layout 1 | `7a2c05c04d03`  |
| 1636   | Layout 1 | `7a2c05c04d03`  |
| 1628   | Layout 1 | `7a2c05c04d03`  |
| 1622   | Layout 1 | `7a2c05c04d03`  |
| 1614   | Layout 1 | `7a2c05c04d03`  |
| 1608   | Layout 1 | `7a2c05c04d03`  |
| 1602   | Layout 1 | `7a2c05c04d03`  |
| 1598   | Layout 1 | `7a2c05c04d03`  |
| 1594   | Layout 1 | `7a2c05c04d03`  |
| 1590   | Layout 1 | `7a2c05c04d03`  |
| 1587   | Layout 1 | `7a2c05c04d03`  |
| 1584   | Layout 1 | `7a2c05c04d03`  |
| 1579   | Layout 1 | `7a2c05c04d03`  |
| 1572   | Layout 1 | `7a2c05c04d03`  |
| 1565   | Layout 1 | `7a2c05c04d03`  |
| 1559   | Layout 1 | `7a2c05c04d03`  |
| 1554   | Layout 1 | `7a2c05c04d03`  |
| 1547   | Layout 1 | `7a2c05c04d03`  |
| 1537   | Layout 1 | `7a2c05c04d03`  |
| 1529   | Layout 1 | `7a2c05c04d03`  |
| 1524   | Layout 1 | `7a2c05c04d03`  |
| 1519   | Layout 1 | `7a2c05c04d03`  |
| 1509   | Layout 1 | `7a2c05c04d03`  |
| 1506   | Layout 1 | `7a2c05c04d03`  |
| 1504   | No file  | `7a2c05c04d03`  |
| 1500   | No file  | `7a2c05c04d03`  |
| 1493   | No file  | `7a2c05c04d03`  |
| 1489   | No file  | `7a2c05c04d03`  |
| 1485   | No file  | `7a2c05c04d03`  |
| 1481   | No file  | `7a2c05c04d03`  |
| 1474   | No file  | `7a2c05c04d03`  |
| 1466   | No file  | `7a2c05c04d03`  |
| 1462   | No file  | `7a2c05c04d03`  |
| 1459   | No file  | `7a2c05c04d03`  |
| 1453   | No file  | `7a2c05c04d03`  |
| 1450   | No file  | `7a2c05c04d03`  |
| 1445   | No file  | `7a2c05c04d03`  |
| 1439   | No file  | `7a2c05c04d03`  |
| 1433   | No file  | `7a2c05c04d03`  |
| 1430   | No file  | `7a2c05c04d03`  |
| 1426   | No file  | `7a2c05c04d03`  |
| 1421   | No file  | `7a2c05c04d03`  |
| 1417   | No file  | `7a2c05c04d03`  |
| 1416   | No file  | `7a2c05c04d03`  |
| 1409   | No file  | `7a2c05c04d03`  |
| 1405   | No file  | `7a2c05c04d03`  |
| 1401   | No file  | `7a2c05c04d03`  |
| 1396   | No file  | `7a2c05c04d03`  |
| 1391   | No file  | `7a2c05c04d03`  |
| 1390   | No file  | `7a2c05c04d03`  |
| 1386   | No file  | `7a2c05c04d03`  |
| 1381   | No file  | `7a2c05c04d03`  |
| 1379   | No file  | `7a2c05c04d03`  |
| 1372   | No file  | `7a2c05c04d03`  |
| 1366   | No file  | `7a2c05c04d03`  |
| 1364   | No file  | `7a2c05c04d03`  |
| 1363   | No file  | `7a2c05c04d03`  |
| 1360   | No file  | `7a2c05c04d03`  |
| 1358   | No file  | `7a2c05c04d03`  |
| 1355   | No file  | `7a2c05c04d03`  |
| 1351   | No file  | `7a2c05c04d03`  |
| 1348   | No file  | `7a2c05c04d03`  |
| 1346   | No file  | `7a2c05c04d03`  |
| 1341   | No file  | `7a2c05c04d03`  |
| 1340   | No file  | `7a2c05c04d03`  |
| 1338   | No file  | `7a2c05c04d03`  |
| 1335   | No file  | `7a2c05c04d03`  |
| 1333   | No file  | `7a2c05c04d03`  |
| 1329   | No file  | `7a2c05c04d03`  |
| 1327   | No file  | `7a2c05c04d03`  |
| 1324   | No file  | `7a2c05c04d03`  |
| 1321   | No file  | `7a2c05c04d03`  |
| 1319   | No file  | `7a2c05c04d03`  |
| 1318   | No file  | `7a2c05c04d03`  |
| 1316   | No file  | `7a2c05c04d03`  |
| 1313   | No file  | `7a2c05c04d03`  |
| 1311   | No file  | `7a2c05c04d03`  |
| 1309   | No file  | `7a2c05c04d03`  |
| 1304   | No file  | `7a2c05c04d03`  |
| 1292   | No file  | `7a2c05c04d03`  |
| 1286   | No file  | `7a2c05c04d03`  |
| 1280   | No file  | `7a2c05c04d03`  |
| 1276   | No file  | `7a2c05c04d03`  |
| 1267   | No file  | `7a2c05c04d03`  |
| 1261   | No file  | `7a2c05c04d03`  |
| 1256   | No file  | `7a2c05c04d03`  |
| 1250   | No file  | `7a2c05c04d03`  |
| 1246   | No file  | `7a2c05c04d03`  |
| 1239   | No file  | `7a2c05c04d03`  |
| 1230   | No file  | `7a2c05c04d03`  |
| 1226   | No file  | `7a2c05c04d03`  |
| 1220   | No file  | `7a2c05c04d03`  |
| 1217   | No file  | `7a2c05c04d03`  |
| 1211   | No file  | `7a2c05c04d03`  |
| 1210   | No file  | `7a2c05c04d03`  |
| 1208   | No file  | `7a2c05c04d03`  |
| 1203   | No file  | `7a2c05c04d03`  |
| 1197   | No file  | `7a2c05c04d03`  |
| 1194   | No file  | `7a2c05c04d03`  |
| 1192   | No file  | `7a2c05c04d03`  |
| 1187   | No file  | `7a2c05c04d03`  |
| 1183   | No file  | `7a2c05c04d03`  |
| 1177   | No file  | `7a2c05c04d03`  |
| 1173   | No file  | `7a2c05c04d03`  |
| 1167   | No file  | `7a2c05c04d03`  |
| 1164   | No file  | `7a2c05c04d03`  |
| 1156   | No file  | `7a2c05c04d03`  |
| 1149   | No file  | `7a2c05c04d03`  |
| 1144   | No file  | `7a2c05c04d03`  |
| 1137   | No file  | `7a2c05c04d03`  |
| 1132   | No file  | `7a2c05c04d03`  |
| 1127   | No file  | `7a2c05c04d03`  |
| 1122   | No file  | `7a2c05c04d03`  |
| 1118   | No file  | `7a2c05c04d03`  |
| 1114   | No file  | `7a2c05c04d03`  |
| 1109   | No file  | `7a2c05c04d03`  |
| 1102   | No file  | `7a2c05c04d03`  |
| 1096   | No file  | `7a2c05c04d03`  |
| 1088   | No file  | `7a2c05c04d03`  |
| 1081   | No file  | `7a2c05c04d03`  |
| 1076   | No file  | `7a2c05c04d03`  |
| 1069   | No file  | `7a2c05c04d03`  |
| 1064   | No file  | `7a2c05c04d03`  |
| 1058   | No file  | `7a2c05c04d03`  |
| 1051   | No file  | `7a2c05c04d03`  |
| 1044   | No file  | `7a2c05c04d03`  |
| 1036   | No file  | `7a2c05c04d03`  |
| 1026   | No file  | `7a2c05c04d03`  |
| 1016   | No file  | `7a2c05c04d03`  |
| 1009   | No file  | `7a2c05c04d03`  |
| 1005   | No file  | `7a2c05c04d03`  |
| 1000   | No file  | `7a2c05c04d03`  |
| 998    | No file  | `7a2c05c04d03`  |
| 990    | No file  | `7a2c05c04d03`  |
| 979    | No file  | `7a2c05c04d03`  |
| 972    | No file  | `7a2c05c04d03`  |
| 963    | No file  | `7a2c05c04d03`  |
| 955    | No file  | `7a2c05c04d03`  |
| 946    | No file  | `7a2c05c04d03`  |
| 938    | No file  | `7a2c05c04d03`  |
| 927    | No file  | `7a2c05c04d03`  |
| 911    | No file  | `7a2c05c04d03`  |
| 904    | No file  | `7a2c05c04d03`  |
| 899    | No file  | `7a2c05c04d03`  |
| 894    | No file  | `7a2c05c04d03`  |
| 885    | No file  | `7a2c05c04d03`  |
| 879    | No file  | `7a2c05c04d03`  |
| 872    | No file  | `7a2c05c04d03`  |
| 864    | No file  | `7a2c05c04d03`  |
| 855    | No file  | `7a2c05c04d03`  |
| 853    | No file  | `7a2c05c04d03`  |
| 845    | No file  | `7a2c05c04d03`  |
| 837    | No file  | `7a2c05c04d03`  |
| 829    | No file  | `7a2c05c04d03`  |
| 822    | No file  | `7a2c05c04d03`  |
| 814    | No file  | `7a2c05c04d03`  |
| 805    | No file  | `7a2c05c04d03`  |
| 794    | No file  | `7a2c05c04d03`  |
| 787    | No file  | `7a2c05c04d03`  |
| 780    | No file  | `7a2c05c04d03`  |
| 771    | No file  | `7a2c05c04d03`  |
| 760    | No file  | `7a2c05c04d03`  |
| 748    | No file  | `7a2c05c04d03`  |
| 741    | No file  | `7a2c05c04d03`  |
| 736    | No file  | `7a2c05c04d03`  |
| 731    | No file  | `7a2c05c04d03`  |
| 723    | No file  | `7a2c05c04d03`  |
| 711    | No file  | `7a2c05c04d03`  |
| 707    | No file  | `7a2c05c04d03`  |
| 697    | No file  | `7a2c05c04d03`  |
| 689    | No file  | `7a2c05c04d03`  |
| 683    | No file  | `7a2c05c04d03`  |
| 678    | No file  | `7a2c05c04d03`  |
| 670    | No file  | `7a2c05c04d03`  |
| 661    | No file  | `7a2c05c04d03`  |
| 656    | No file  | `7a2c05c04d03`  |
| 652    | No file  | `7a2c05c04d03`  |
| 643    | No file  | `7a2c05c04d03`  |
| 637    | No file  | `7a2c05c04d03`  |
| 630    | No file  | `7a2c05c04d03`  |
| 627    | No file  | `7a2c05c04d03`  |
| 621    | No file  | `7a2c05c04d03`  |
| 617    | No file  | `7a2c05c04d03`  |
| 615    | No file  | `7a2c05c04d03`  |
| 606    | No file  | `7a2c05c04d03`  |
| 599    | No file  | `7a2c05c04d03`  |
| 592    | No file  | `7a2c05c04d03`  |
| 586    | No file  | `7a2c05c04d03`  |
| 577    | No file  | `7a2c05c04d03`  |
| 569    | No file  | `7a2c05c04d03`  |
| 561    | No file  | `7a2c05c04d03`  |
| 554    | No file  | `7a2c05c04d03`  |
| 542    | No file  | `7a2c05c04d03`  |
| 532    | No file  | `7a2c05c04d03`  |
| 531    | No file  | `7a2c05c04d03`  |
| 526    | No file  | `7a2c05c04d03`  |
| 521    | No file  | `7a2c05c04d03`  |
| 517    | No file  | `7a2c05c04d03`  |
| 510    | No file  | `7a2c05c04d03`  |
| 508    | No file  | `7a2c05c04d03`  |
| 504    | No file  | `7a2c05c04d03`  |
| 497    | No file  | `7a2c05c04d03`  |
| 491    | No file  | `7a2c05c04d03`  |
| 485    | No file  | `7a2c05c04d03`  |
| 478    | No file  | `7a2c05c04d03`  |
| 472    | No file  | `7a2c05c04d03`  |
| 466    | No file  | `7a2c05c04d03`  |
| 457    | No file  | `7a2c05c04d03`  |
| 452    | No file  | `7a2c05c04d03`  |
| 449    | No file  | `7a2c05c04d03`  |
| 435    | No file  | `7a2c05c04d03`  |

<!-- versions:end -->

## Companion Files

None. The keys point into
[`instancefieldrankingmanage.bss`](instancefieldrankingmanage_bss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                             |
| ------------------- | ----------------- | ------------------ | --------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                            |
| `+0x04`             | u32               | record_count       | Number of rows                    |
| `+0x08`             | Row[record_count] | records            | See Row                           |
| `records+0x00`      | String Table      | string_table       | Empty                             |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count` |
| `string_table+0x04` | u32               | zero               | `0`                               |

### Row (variable: 6 bytes + list)

| Offset  | Type                | Field               | Notes |
| ------- | ------------------- | ------------------- | ----- |
| `+0x00` | u16                 | instance_field_type | Row key, `0` up, one row per type in key order |
| `+0x02` | u32                 | ranking_count       | Number of rankings |
| `+0x06` | u32[ranking_count]  | ranking_idxs        | `ranking_idx` keys of `instancefieldrankingmanage.bss` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Field Names

The `InstanceRanking` sheet of a private server's `DataSheets.bexcel` on
client 1784 has one row per `PA_GAME_SERVICE_TYPE` and the columns
`instanceFieldType_0` to `instanceFieldType_23`; each cell is a list of
`RankingIdx` values of the `InstanceRankingManage` sheet. The file of the
NA/EU client 1784 holds the cells of the `NA_REAL` row (service type
`12`): `instanceFieldType_11` is `7` there and in the file. The row key is
the `N` of the column name, so it is named `instance_field_type`.

## Notes

- Row counts: 20 on client 1784 (types `0` to `19`), 23 on clients 2107 to 2765 and
  24 from client 3002 on. Every row from type `11` on lists ranking `7` on
  each of those clients.

## Open Questions

### Rankings on Types 12 and Up

On client 1784 the sheet fills only `instanceFieldType_11`; `12` to `19`
are `<null>` there, yet the file gives types `12` to `19` the same list
`7`. Whether the build tool copies an empty cell from the column before
it, or the live sheet holds these lists, is open. No instance field type
other than `11` has a row in `instancefieldrankingmanage.bss`.
