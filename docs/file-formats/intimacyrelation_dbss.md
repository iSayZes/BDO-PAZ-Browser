# `intimacyrelation.dbss` Format

## Purpose

The first meeting with an NPC, per NPC character key: the line the NPC says
while its knowledge cannot be gained yet (`covered_dialog_kr`), the line
and cutscene when it is discovered, the knowledge the discovery grants
(`discover_function`, a `Pushknowledge(<knowledge>,0)` script) and up to
five more lines, each with a condition string. Every text is Korean;
LOC type 23 holds the user-language text under the NPC key. Companion
`intimacyrelationoffset.dbss` lists where every record sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes   | Records                 | Row bytes                    |
| ------ | -------------- | ----------------------------- | ------- | ----------------------- | ---------------------------- |
| 3      | 2583 and later | `intimacyrelation.dbss`       | 748,525 | 2,206 Row, 2,206 Record | 136 to 1,504, 337 on average |
| 3      | 2583 and later | `intimacyrelationoffset.dbss` | 22,064  | 2,206 Offset Row        | 10                           |
| 2      | 1346 to 2575   | `intimacyrelation.dbss`       | 667,200 | 1,895 Row, 1,895 Record | 140 to 1,508, 350 on average |
| 2      | 1346 to 2575   | `intimacyrelationoffset.dbss` | 18,954  | 1,895 Offset Row        | 10                           |
| 1      | 1250 to 1341   | `intimacyrelation.dbss`       | 422,598 | 1,256 Row               | 140 to 1,582, 336 on average |
| 1      | 1250 to 1341   | `intimacyrelationoffset.dbss` | 12,564  | 1,256 Offset Row        | 10                           |

| Layout | File                          | Known             | Unknown        |
| ------ | ----------------------------- | ----------------- | -------------- |
| 3      | `intimacyrelation.dbss`       | 739,701 B (98.8%) | 8,824 B (1.2%) |
| 3      | `intimacyrelationoffset.dbss` | 22,064 B (100.0%) | 0 B (0.0%)     |
| 2      | `intimacyrelation.dbss`       | 659,620 B (98.9%) | 7,580 B (1.1%) |
| 2      | `intimacyrelationoffset.dbss` | 18,954 B (100.0%) | 0 B (0.0%)     |
| 1      | `intimacyrelation.dbss`       | 417,574 B (98.8%) | 5,024 B (1.2%) |
| 1      | `intimacyrelationoffset.dbss` | 12,564 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `5a4fdea8ba87`  |
| 3482   | Layout 3 | `5a4fdea8ba87`  |
| 3474   | Layout 3 | `5a4fdea8ba87`  |
| 3473   | Layout 3 | `5a4fdea8ba87`  |
| 3464   | Layout 3 | `5a4fdea8ba87`  |
| 3458   | Layout 3 | `5a4fdea8ba87`  |
| 3454   | Layout 3 | `5a4fdea8ba87`  |
| 3444   | Layout 3 | `5a4fdea8ba87`  |
| 3435   | Layout 3 | `5a4fdea8ba87`  |
| 3426   | Layout 3 | `5a4fdea8ba87`  |
| 3418   | Layout 3 | `5a4fdea8ba87`  |
| 3412   | Layout 3 | `5a4fdea8ba87`  |
| 3402   | Layout 3 | `5a4fdea8ba87`  |
| 3396   | Layout 3 | `5a4fdea8ba87`  |
| 3387   | Layout 3 | `5a4fdea8ba87`  |
| 3381   | Layout 3 | `5a4fdea8ba87`  |
| 3373   | Layout 3 | `5a4fdea8ba87`  |
| 3364   | Layout 3 | `5a4fdea8ba87`  |
| 3356   | Layout 3 | `5a4fdea8ba87`  |
| 3349   | Layout 3 | `5a4fdea8ba87`  |
| 3342   | Layout 3 | `5a4fdea8ba87`  |
| 3335   | Layout 3 | `5a4fdea8ba87`  |
| 3326   | Layout 3 | `5a4fdea8ba87`  |
| 3321   | Layout 3 | `5a4fdea8ba87`  |
| 3314   | Layout 3 | `5a4fdea8ba87`  |
| 3303   | Layout 3 | `5a4fdea8ba87`  |
| 3302   | Layout 3 | `5a4fdea8ba87`  |
| 3293   | Layout 3 | `5a4fdea8ba87`  |
| 3283   | Layout 3 | `5a4fdea8ba87`  |
| 3275   | Layout 3 | `5a4fdea8ba87`  |
| 3267   | Layout 3 | `5a4fdea8ba87`  |
| 3258   | Layout 3 | `5a4fdea8ba87`  |
| 3251   | Layout 3 | `5a4fdea8ba87`  |
| 3242   | Layout 3 | `5a4fdea8ba87`  |
| 3235   | Layout 3 | `5a4fdea8ba87`  |
| 3229   | Layout 3 | `5a4fdea8ba87`  |
| 3212   | Layout 3 | `5a4fdea8ba87`  |
| 3203   | Layout 3 | `5a4fdea8ba87`  |
| 3193   | Layout 3 | `5a4fdea8ba87`  |
| 3186   | Layout 3 | `5a4fdea8ba87`  |
| 3177   | Layout 3 | `5a4fdea8ba87`  |
| 3169   | Layout 3 | `5a4fdea8ba87`  |
| 3158   | Layout 3 | `5a4fdea8ba87`  |
| 3151   | Layout 3 | `5a4fdea8ba87`  |
| 3144   | Layout 3 | `5a4fdea8ba87`  |
| 3133   | Layout 3 | `5a4fdea8ba87`  |
| 3125   | Layout 3 | `5a4fdea8ba87`  |
| 3118   | Layout 3 | `5a4fdea8ba87`  |
| 3111   | Layout 3 | `5a4fdea8ba87`  |
| 3103   | Layout 3 | `5a4fdea8ba87`  |
| 3095   | Layout 3 | `5a4fdea8ba87`  |
| 3086   | Layout 3 | `5a4fdea8ba87`  |
| 3072   | Layout 3 | `5a4fdea8ba87`  |
| 3062   | Layout 3 | `5a4fdea8ba87`  |
| 3052   | Layout 3 | `5a4fdea8ba87`  |
| 3045   | Layout 3 | `5a4fdea8ba87`  |
| 3037   | Layout 3 | `5a4fdea8ba87`  |
| 3030   | Layout 3 | `5a4fdea8ba87`  |
| 3021   | Layout 3 | `5a4fdea8ba87`  |
| 3012   | Layout 3 | `5a4fdea8ba87`  |
| 3002   | Layout 3 | `5a4fdea8ba87`  |
| 2995   | Layout 3 | `5a4fdea8ba87`  |
| 2987   | Layout 3 | `5a4fdea8ba87`  |
| 2978   | Layout 3 | `5a4fdea8ba87`  |
| 2970   | Layout 3 | `5a4fdea8ba87`  |
| 2959   | Layout 3 | `5a4fdea8ba87`  |
| 2951   | Layout 3 | `5a4fdea8ba87`  |
| 2942   | Layout 3 | `5a4fdea8ba87`  |
| 2935   | Layout 3 | `5a4fdea8ba87`  |
| 2932   | Layout 3 | `5a4fdea8ba87`  |
| 2923   | Layout 3 | `5a4fdea8ba87`  |
| 2919   | Layout 3 | `5a4fdea8ba87`  |
| 2907   | Layout 3 | `5a4fdea8ba87`  |
| 2900   | Layout 3 | `5a4fdea8ba87`  |
| 2891   | Layout 3 | `5a4fdea8ba87`  |
| 2882   | Layout 3 | `5a4fdea8ba87`  |
| 2872   | Layout 3 | `5a4fdea8ba87`  |
| 2863   | Layout 3 | `5a4fdea8ba87`  |
| 2855   | Layout 3 | `5a4fdea8ba87`  |
| 2849   | Layout 3 | `5a4fdea8ba87`  |
| 2844   | Layout 3 | `5a4fdea8ba87`  |
| 2834   | Layout 3 | `5a4fdea8ba87`  |
| 2825   | Layout 3 | `5a4fdea8ba87`  |
| 2819   | Layout 3 | `5a4fdea8ba87`  |
| 2811   | Layout 3 | `5a4fdea8ba87`  |
| 2803   | Layout 3 | `5a4fdea8ba87`  |
| 2794   | Layout 3 | `5a4fdea8ba87`  |
| 2783   | Layout 3 | `5a4fdea8ba87`  |
| 2774   | Layout 3 | `5a4fdea8ba87`  |
| 2765   | Layout 3 | `5a4fdea8ba87`  |
| 2756   | Layout 3 | `5a4fdea8ba87`  |
| 2750   | Layout 3 | `5a4fdea8ba87`  |
| 2743   | Layout 3 | `5a4fdea8ba87`  |
| 2736   | Layout 3 | `5a4fdea8ba87`  |
| 2726   | Layout 3 | `5a4fdea8ba87`  |
| 2717   | Layout 3 | `5a4fdea8ba87`  |
| 2709   | Layout 3 | `5a4fdea8ba87`  |
| 2703   | Layout 3 | `5a4fdea8ba87`  |
| 2695   | Layout 3 | `5a4fdea8ba87`  |
| 2684   | Layout 3 | `5a4fdea8ba87`  |
| 2672   | Layout 3 | `5a4fdea8ba87`  |
| 2665   | Layout 3 | `5a4fdea8ba87`  |
| 2657   | Layout 3 | `5a4fdea8ba87`  |
| 2649   | Layout 3 | `5a4fdea8ba87`  |
| 2644   | Layout 3 | `5a4fdea8ba87`  |
| 2637   | Layout 3 | `5a4fdea8ba87`  |
| 2629   | Layout 3 | `5a4fdea8ba87`  |
| 2619   | Layout 3 | `5a4fdea8ba87`  |
| 2612   | Layout 3 | `5a4fdea8ba87`  |
| 2606   | Layout 3 | `5a4fdea8ba87`  |
| 2602   | Layout 3 | `5a4fdea8ba87`  |
| 2601   | Layout 3 | `5a4fdea8ba87`  |
| 2592   | Layout 3 | `5a4fdea8ba87`  |
| 2583   | Layout 3 | `5a4fdea8ba87`  |
| 2575   | Layout 2 | `5a4fdea8ba87`  |
| 2567   | Layout 2 | `5a4fdea8ba87`  |
| 2560   | Layout 2 | `5a4fdea8ba87`  |
| 2553   | Layout 2 | `5a4fdea8ba87`  |
| 2545   | Layout 2 | `5a4fdea8ba87`  |
| 2538   | Layout 2 | `5a4fdea8ba87`  |
| 2529   | Layout 2 | `5a4fdea8ba87`  |
| 2519   | Layout 2 | `5a4fdea8ba87`  |
| 2513   | Layout 2 | `5a4fdea8ba87`  |
| 2510   | Layout 2 | `5a4fdea8ba87`  |
| 2507   | Layout 2 | `5a4fdea8ba87`  |
| 2503   | Layout 2 | `5a4fdea8ba87`  |
| 2498   | Layout 2 | `5a4fdea8ba87`  |
| 2492   | Layout 2 | `5a4fdea8ba87`  |
| 2487   | Layout 2 | `5a4fdea8ba87`  |
| 2480   | Layout 2 | `5a4fdea8ba87`  |
| 2474   | Layout 2 | `5a4fdea8ba87`  |
| 2468   | Layout 2 | `5a4fdea8ba87`  |
| 2460   | Layout 2 | `5a4fdea8ba87`  |
| 2453   | Layout 2 | `5a4fdea8ba87`  |
| 2444   | Layout 2 | `5a4fdea8ba87`  |
| 2438   | Layout 2 | `5a4fdea8ba87`  |
| 2434   | Layout 2 | `5a4fdea8ba87`  |
| 2429   | Layout 2 | `5a4fdea8ba87`  |
| 2421   | Layout 2 | `5a4fdea8ba87`  |
| 2414   | Layout 2 | `5a4fdea8ba87`  |
| 2407   | Layout 2 | `5a4fdea8ba87`  |
| 2401   | Layout 2 | `5a4fdea8ba87`  |
| 2397   | Layout 2 | `5a4fdea8ba87`  |
| 2393   | Layout 2 | `5a4fdea8ba87`  |
| 2384   | Layout 2 | `5a4fdea8ba87`  |
| 2378   | Layout 2 | `5a4fdea8ba87`  |
| 2372   | Layout 2 | `5a4fdea8ba87`  |
| 2358   | Layout 2 | `5a4fdea8ba87`  |
| 2352   | Layout 2 | `5a4fdea8ba87`  |
| 2347   | Layout 2 | `5a4fdea8ba87`  |
| 2343   | Layout 2 | `5a4fdea8ba87`  |
| 2335   | Layout 2 | `5a4fdea8ba87`  |
| 2327   | Layout 2 | `5a4fdea8ba87`  |
| 2324   | Layout 2 | `5a4fdea8ba87`  |
| 2319   | Layout 2 | `5a4fdea8ba87`  |
| 2313   | Layout 2 | `5a4fdea8ba87`  |
| 2308   | Layout 2 | `5a4fdea8ba87`  |
| 2302   | Layout 2 | `5a4fdea8ba87`  |
| 2295   | Layout 2 | `5a4fdea8ba87`  |
| 2290   | Layout 2 | `5a4fdea8ba87`  |
| 2284   | Layout 2 | `5a4fdea8ba87`  |
| 2276   | Layout 2 | `5a4fdea8ba87`  |
| 2269   | Layout 2 | `5a4fdea8ba87`  |
| 2259   | Layout 2 | `5a4fdea8ba87`  |
| 2250   | Layout 2 | `5a4fdea8ba87`  |
| 2243   | Layout 2 | `5a4fdea8ba87`  |
| 2235   | Layout 2 | `5a4fdea8ba87`  |
| 2229   | Layout 2 | `5a4fdea8ba87`  |
| 2224   | Layout 2 | `5a4fdea8ba87`  |
| 2218   | Layout 2 | `5a4fdea8ba87`  |
| 2215   | Layout 2 | `5a4fdea8ba87`  |
| 2207   | Layout 2 | `5a4fdea8ba87`  |
| 2203   | Layout 2 | `5a4fdea8ba87`  |
| 2196   | Layout 2 | `5a4fdea8ba87`  |
| 2192   | Layout 2 | `5a4fdea8ba87`  |
| 2189   | Layout 2 | `5a4fdea8ba87`  |
| 2183   | Layout 2 | `5a4fdea8ba87`  |
| 2179   | Layout 2 | `5a4fdea8ba87`  |
| 2171   | Layout 2 | `5a4fdea8ba87`  |
| 2163   | Layout 2 | `5a4fdea8ba87`  |
| 2156   | Layout 2 | `5a4fdea8ba87`  |
| 2151   | Layout 2 | `5a4fdea8ba87`  |
| 2147   | Layout 2 | `5a4fdea8ba87`  |
| 2142   | Layout 2 | `5a4fdea8ba87`  |
| 2138   | Layout 2 | `5a4fdea8ba87`  |
| 2134   | Layout 2 | `5a4fdea8ba87`  |
| 2130   | Layout 2 | `5a4fdea8ba87`  |
| 2122   | Layout 2 | `5a4fdea8ba87`  |
| 2107   | Layout 2 | `5a4fdea8ba87`  |
| 2098   | Layout 2 | `5a4fdea8ba87`  |
| 2089   | Layout 2 | `5a4fdea8ba87`  |
| 2081   | Layout 2 | `5a4fdea8ba87`  |
| 2073   | Layout 2 | `5a4fdea8ba87`  |
| 2067   | Layout 2 | `5a4fdea8ba87`  |
| 2063   | Layout 2 | `5a4fdea8ba87`  |
| 2059   | Layout 2 | `5a4fdea8ba87`  |
| 2052   | Layout 2 | `5a4fdea8ba87`  |
| 2044   | Layout 2 | `5a4fdea8ba87`  |
| 2039   | Layout 2 | `5a4fdea8ba87`  |
| 2032   | Layout 2 | `5a4fdea8ba87`  |
| 2025   | Layout 2 | `5a4fdea8ba87`  |
| 2011   | Layout 2 | `5a4fdea8ba87`  |
| 2005   | Layout 2 | `5a4fdea8ba87`  |
| 2000   | Layout 2 | `5a4fdea8ba87`  |
| 1996   | Layout 2 | `5a4fdea8ba87`  |
| 1991   | Layout 2 | `5a4fdea8ba87`  |
| 1985   | Layout 2 | `5a4fdea8ba87`  |
| 1980   | Layout 2 | `5a4fdea8ba87`  |
| 1969   | Layout 2 | `5a4fdea8ba87`  |
| 1964   | Layout 2 | `5a4fdea8ba87`  |
| 1958   | Layout 2 | `5a4fdea8ba87`  |
| 1950   | Layout 2 | `5a4fdea8ba87`  |
| 1945   | Layout 2 | `5a4fdea8ba87`  |
| 1937   | Layout 2 | `5a4fdea8ba87`  |
| 1933   | Layout 2 | `5a4fdea8ba87`  |
| 1927   | Layout 2 | `5a4fdea8ba87`  |
| 1921   | Layout 2 | `5a4fdea8ba87`  |
| 1914   | Layout 2 | `5a4fdea8ba87`  |
| 1908   | Layout 2 | `5a4fdea8ba87`  |
| 1897   | Layout 2 | `5a4fdea8ba87`  |
| 1892   | Layout 2 | `5a4fdea8ba87`  |
| 1886   | Layout 2 | `5a4fdea8ba87`  |
| 1881   | Layout 2 | `5a4fdea8ba87`  |
| 1871   | Layout 2 | `5a4fdea8ba87`  |
| 1866   | Layout 2 | `5a4fdea8ba87`  |
| 1862   | Layout 2 | `5a4fdea8ba87`  |
| 1854   | Layout 2 | `5a4fdea8ba87`  |
| 1846   | Layout 2 | `5a4fdea8ba87`  |
| 1838   | Layout 2 | `5a4fdea8ba87`  |
| 1832   | Layout 2 | `5a4fdea8ba87`  |
| 1826   | Layout 2 | `5a4fdea8ba87`  |
| 1822   | Layout 2 | `5a4fdea8ba87`  |
| 1818   | Layout 2 | `5a4fdea8ba87`  |
| 1804   | Layout 2 | `5a4fdea8ba87`  |
| 1794   | Layout 2 | `5a4fdea8ba87`  |
| 1790   | Layout 2 | `5a4fdea8ba87`  |
| 1784   | Layout 2 | `5a4fdea8ba87`  |
| 1774   | Layout 2 | `5a4fdea8ba87`  |
| 1771   | Layout 2 | `5a4fdea8ba87`  |
| 1762   | Layout 2 | `5a4fdea8ba87`  |
| 1759   | Layout 2 | `5a4fdea8ba87`  |
| 1754   | Layout 2 | `5a4fdea8ba87`  |
| 1749   | Layout 2 | `5a4fdea8ba87`  |
| 1743   | Layout 2 | `5a4fdea8ba87`  |
| 1737   | Layout 2 | `5a4fdea8ba87`  |
| 1731   | Layout 2 | `5a4fdea8ba87`  |
| 1725   | Layout 2 | `5a4fdea8ba87`  |
| 1717   | Layout 2 | `5a4fdea8ba87`  |
| 1710   | Layout 2 | `5a4fdea8ba87`  |
| 1704   | Layout 2 | `5a4fdea8ba87`  |
| 1698   | Layout 2 | `5a4fdea8ba87`  |
| 1690   | Layout 2 | `5a4fdea8ba87`  |
| 1685   | Layout 2 | `5a4fdea8ba87`  |
| 1680   | Layout 2 | `5a4fdea8ba87`  |
| 1674   | Layout 2 | `5a4fdea8ba87`  |
| 1668   | Layout 2 | `5a4fdea8ba87`  |
| 1659   | Layout 2 | `5a4fdea8ba87`  |
| 1649   | Layout 2 | `5a4fdea8ba87`  |
| 1642   | Layout 2 | `5a4fdea8ba87`  |
| 1636   | Layout 2 | `5a4fdea8ba87`  |
| 1628   | Layout 2 | `5a4fdea8ba87`  |
| 1622   | Layout 2 | `5a4fdea8ba87`  |
| 1614   | Layout 2 | `5a4fdea8ba87`  |
| 1608   | Layout 2 | `5a4fdea8ba87`  |
| 1602   | Layout 2 | `5a4fdea8ba87`  |
| 1598   | Layout 2 | `5a4fdea8ba87`  |
| 1594   | Layout 2 | `5a4fdea8ba87`  |
| 1590   | Layout 2 | `5a4fdea8ba87`  |
| 1587   | Layout 2 | `5a4fdea8ba87`  |
| 1584   | Layout 2 | `5a4fdea8ba87`  |
| 1579   | Layout 2 | `5a4fdea8ba87`  |
| 1572   | Layout 2 | `5a4fdea8ba87`  |
| 1565   | Layout 2 | `5a4fdea8ba87`  |
| 1559   | Layout 2 | `5a4fdea8ba87`  |
| 1554   | Layout 2 | `5a4fdea8ba87`  |
| 1547   | Layout 2 | `5a4fdea8ba87`  |
| 1537   | Layout 2 | `5a4fdea8ba87`  |
| 1529   | Layout 2 | `5a4fdea8ba87`  |
| 1524   | Layout 2 | `5a4fdea8ba87`  |
| 1519   | Layout 2 | `5a4fdea8ba87`  |
| 1509   | Layout 2 | `5a4fdea8ba87`  |
| 1506   | Layout 2 | `5a4fdea8ba87`  |
| 1504   | Layout 2 | `5a4fdea8ba87`  |
| 1500   | Layout 2 | `5a4fdea8ba87`  |
| 1493   | Layout 2 | `5a4fdea8ba87`  |
| 1489   | Layout 2 | `5a4fdea8ba87`  |
| 1485   | Layout 2 | `5a4fdea8ba87`  |
| 1481   | Layout 2 | `5a4fdea8ba87`  |
| 1474   | Layout 2 | `5a4fdea8ba87`  |
| 1466   | Layout 2 | `5a4fdea8ba87`  |
| 1462   | Layout 2 | `5a4fdea8ba87`  |
| 1459   | Layout 2 | `5a4fdea8ba87`  |
| 1453   | Layout 2 | `5a4fdea8ba87`  |
| 1450   | Layout 2 | `5a4fdea8ba87`  |
| 1445   | Layout 2 | `5a4fdea8ba87`  |
| 1439   | Layout 2 | `5a4fdea8ba87`  |
| 1433   | Layout 2 | `5a4fdea8ba87`  |
| 1430   | Layout 2 | `5a4fdea8ba87`  |
| 1426   | Layout 2 | `5a4fdea8ba87`  |
| 1421   | Layout 2 | `5a4fdea8ba87`  |
| 1417   | Layout 2 | `5a4fdea8ba87`  |
| 1416   | Layout 2 | `5a4fdea8ba87`  |
| 1409   | Layout 2 | `5a4fdea8ba87`  |
| 1405   | Layout 2 | `5a4fdea8ba87`  |
| 1401   | Layout 2 | `5a4fdea8ba87`  |
| 1396   | Layout 2 | `5a4fdea8ba87`  |
| 1391   | Layout 2 | `5a4fdea8ba87`  |
| 1390   | Layout 2 | `5a4fdea8ba87`  |
| 1386   | Layout 2 | `5a4fdea8ba87`  |
| 1381   | Layout 2 | `5a4fdea8ba87`  |
| 1379   | Layout 2 | `5a4fdea8ba87`  |
| 1372   | Layout 2 | `5a4fdea8ba87`  |
| 1366   | Layout 2 | `5a4fdea8ba87`  |
| 1364   | Layout 2 | `5a4fdea8ba87`  |
| 1363   | Layout 2 | `5a4fdea8ba87`  |
| 1360   | Layout 2 | `5a4fdea8ba87`  |
| 1358   | Layout 2 | `5a4fdea8ba87`  |
| 1355   | Layout 2 | `5a4fdea8ba87`  |
| 1351   | Layout 2 | `5a4fdea8ba87`  |
| 1348   | Layout 2 | `5a4fdea8ba87`  |
| 1346   | Layout 2 | `5a4fdea8ba87`  |
| 1341   | Layout 1 | `5a4fdea8ba87`  |
| 1340   | Layout 1 | `5a4fdea8ba87`  |
| 1338   | Layout 1 | `5a4fdea8ba87`  |
| 1335   | Layout 1 | `5a4fdea8ba87`  |
| 1333   | Layout 1 | `5a4fdea8ba87`  |
| 1329   | Layout 1 | `5a4fdea8ba87`  |
| 1327   | Layout 1 | `5a4fdea8ba87`  |
| 1324   | Layout 1 | `5a4fdea8ba87`  |
| 1321   | Layout 1 | `5a4fdea8ba87`  |
| 1319   | Layout 1 | `5a4fdea8ba87`  |
| 1318   | Layout 1 | `5a4fdea8ba87`  |
| 1316   | Layout 1 | `5a4fdea8ba87`  |
| 1313   | Layout 1 | `5a4fdea8ba87`  |
| 1311   | Layout 1 | `5a4fdea8ba87`  |
| 1309   | Layout 1 | `5a4fdea8ba87`  |
| 1304   | Layout 1 | `5a4fdea8ba87`  |
| 1292   | Layout 1 | `5a4fdea8ba87`  |
| 1286   | Layout 1 | `5a4fdea8ba87`  |
| 1280   | Layout 1 | `5a4fdea8ba87`  |
| 1276   | Layout 1 | `5a4fdea8ba87`  |
| 1267   | Layout 1 | `5a4fdea8ba87`  |
| 1261   | Layout 1 | `5a4fdea8ba87`  |
| 1256   | Layout 1 | `5a4fdea8ba87`  |
| 1250   | Layout 1 | `5a4fdea8ba87`  |
| 1246   | No file  | `5a4fdea8ba87`  |
| 1239   | No file  | `5a4fdea8ba87`  |
| 1230   | No file  | `5a4fdea8ba87`  |
| 1226   | No file  | `5a4fdea8ba87`  |
| 1220   | No file  | `5a4fdea8ba87`  |
| 1217   | No file  | `5a4fdea8ba87`  |
| 1211   | No file  | `5a4fdea8ba87`  |
| 1210   | No file  | `5a4fdea8ba87`  |
| 1208   | No file  | `5a4fdea8ba87`  |
| 1203   | No file  | `5a4fdea8ba87`  |
| 1197   | No file  | `5a4fdea8ba87`  |
| 1194   | No file  | `5a4fdea8ba87`  |
| 1192   | No file  | `5a4fdea8ba87`  |
| 1187   | No file  | `5a4fdea8ba87`  |
| 1183   | No file  | `5a4fdea8ba87`  |
| 1177   | No file  | `5a4fdea8ba87`  |
| 1173   | No file  | `5a4fdea8ba87`  |
| 1167   | No file  | `5a4fdea8ba87`  |
| 1164   | No file  | `5a4fdea8ba87`  |
| 1156   | No file  | `5a4fdea8ba87`  |
| 1149   | No file  | `5a4fdea8ba87`  |
| 1144   | No file  | `5a4fdea8ba87`  |
| 1137   | No file  | `5a4fdea8ba87`  |
| 1132   | No file  | `5a4fdea8ba87`  |
| 1127   | No file  | `5a4fdea8ba87`  |
| 1122   | No file  | `5a4fdea8ba87`  |
| 1118   | No file  | `5a4fdea8ba87`  |
| 1114   | No file  | `5a4fdea8ba87`  |
| 1109   | No file  | `5a4fdea8ba87`  |
| 1102   | No file  | `5a4fdea8ba87`  |
| 1096   | No file  | `5a4fdea8ba87`  |
| 1088   | No file  | `5a4fdea8ba87`  |
| 1081   | No file  | `5a4fdea8ba87`  |
| 1076   | No file  | `5a4fdea8ba87`  |
| 1069   | No file  | `5a4fdea8ba87`  |
| 1064   | No file  | `5a4fdea8ba87`  |
| 1058   | No file  | `5a4fdea8ba87`  |
| 1051   | No file  | `5a4fdea8ba87`  |
| 1044   | No file  | `5a4fdea8ba87`  |
| 1036   | No file  | `5a4fdea8ba87`  |
| 1026   | No file  | `5a4fdea8ba87`  |
| 1016   | No file  | `5a4fdea8ba87`  |
| 1009   | No file  | `5a4fdea8ba87`  |
| 1005   | No file  | `5a4fdea8ba87`  |
| 1000   | No file  | `5a4fdea8ba87`  |
| 998    | No file  | `5a4fdea8ba87`  |
| 990    | No file  | `5a4fdea8ba87`  |
| 979    | No file  | `5a4fdea8ba87`  |
| 972    | No file  | `5a4fdea8ba87`  |
| 963    | No file  | `5a4fdea8ba87`  |
| 955    | No file  | `5a4fdea8ba87`  |
| 946    | No file  | `5a4fdea8ba87`  |
| 938    | No file  | `5a4fdea8ba87`  |
| 927    | No file  | `5a4fdea8ba87`  |
| 911    | No file  | `5a4fdea8ba87`  |
| 904    | No file  | `5a4fdea8ba87`  |
| 899    | No file  | `5a4fdea8ba87`  |
| 894    | No file  | `5a4fdea8ba87`  |
| 885    | No file  | `5a4fdea8ba87`  |
| 879    | No file  | `5a4fdea8ba87`  |
| 872    | No file  | `5a4fdea8ba87`  |
| 864    | No file  | `5a4fdea8ba87`  |
| 855    | No file  | `5a4fdea8ba87`  |
| 853    | No file  | `5a4fdea8ba87`  |
| 845    | No file  | `5a4fdea8ba87`  |
| 837    | No file  | `5a4fdea8ba87`  |
| 829    | No file  | `5a4fdea8ba87`  |
| 822    | No file  | `5a4fdea8ba87`  |
| 814    | No file  | `5a4fdea8ba87`  |
| 805    | No file  | `5a4fdea8ba87`  |
| 794    | No file  | `5a4fdea8ba87`  |
| 787    | No file  | `5a4fdea8ba87`  |
| 780    | No file  | `5a4fdea8ba87`  |
| 771    | No file  | `5a4fdea8ba87`  |
| 760    | No file  | `5a4fdea8ba87`  |
| 748    | No file  | `5a4fdea8ba87`  |
| 741    | No file  | `5a4fdea8ba87`  |
| 736    | No file  | `5a4fdea8ba87`  |
| 731    | No file  | `5a4fdea8ba87`  |
| 723    | No file  | `5a4fdea8ba87`  |
| 711    | No file  | `5a4fdea8ba87`  |
| 707    | No file  | `5a4fdea8ba87`  |
| 697    | No file  | `5a4fdea8ba87`  |
| 689    | No file  | `5a4fdea8ba87`  |
| 683    | No file  | `5a4fdea8ba87`  |
| 678    | No file  | `5a4fdea8ba87`  |
| 670    | No file  | `5a4fdea8ba87`  |
| 661    | No file  | `5a4fdea8ba87`  |
| 656    | No file  | `5a4fdea8ba87`  |
| 652    | No file  | `5a4fdea8ba87`  |
| 643    | No file  | `5a4fdea8ba87`  |
| 637    | No file  | `5a4fdea8ba87`  |
| 630    | No file  | `5a4fdea8ba87`  |
| 627    | No file  | `5a4fdea8ba87`  |
| 621    | No file  | `5a4fdea8ba87`  |
| 617    | No file  | `5a4fdea8ba87`  |
| 615    | No file  | `5a4fdea8ba87`  |
| 606    | No file  | `5a4fdea8ba87`  |
| 599    | No file  | `5a4fdea8ba87`  |
| 592    | No file  | `5a4fdea8ba87`  |
| 586    | No file  | `5a4fdea8ba87`  |
| 577    | No file  | `5a4fdea8ba87`  |
| 569    | No file  | `5a4fdea8ba87`  |
| 561    | No file  | `5a4fdea8ba87`  |
| 554    | No file  | `5a4fdea8ba87`  |
| 542    | No file  | `5a4fdea8ba87`  |
| 532    | No file  | `5a4fdea8ba87`  |
| 531    | No file  | `5a4fdea8ba87`  |
| 526    | No file  | `5a4fdea8ba87`  |
| 521    | No file  | `5a4fdea8ba87`  |
| 517    | No file  | `5a4fdea8ba87`  |
| 510    | No file  | `5a4fdea8ba87`  |
| 508    | No file  | `5a4fdea8ba87`  |
| 504    | No file  | `5a4fdea8ba87`  |
| 497    | No file  | `5a4fdea8ba87`  |
| 491    | No file  | `5a4fdea8ba87`  |
| 485    | No file  | `5a4fdea8ba87`  |
| 478    | No file  | `5a4fdea8ba87`  |
| 472    | No file  | `5a4fdea8ba87`  |
| 466    | No file  | `5a4fdea8ba87`  |
| 457    | No file  | `5a4fdea8ba87`  |
| 452    | No file  | `5a4fdea8ba87`  |
| 449    | No file  | `5a4fdea8ba87`  |
| 435    | No file  | `5a4fdea8ba87`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                            |
| --------------------------------- | -------- | ------------------------------------------------------------------------------- |
| `intimacyrelationoffset.dbss`     | Optional | `npc_key -> (offset, size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`             | Optional | NPC names (type 6), knowledge names (type 34) and the record's texts (type 23)  |

All multi-byte values are little-endian.

## Layout 3

### File Layout

No `PABR` magic and no string table. A record count, then the records back
to back; the file ends after the last record.

| Offset  | Type          | Field   | Notes                                     |
| ------- | ------------- | ------- | ----------------------------------------- |
| `+0x00` | u32           | count   | Number of NPCs; `2206` on client 3483     |
| `+0x04` | Record[count] | records | See Record                                |

### Record (variable: 2 bytes + row)

| Offset  | Type | Field      | Notes                               |
| ------- | ---- | ---------- | ----------------------------------- |
| `+0x00` | u16  | key_prefix | Equals `npc_key`                    |
| `+0x02` | Row  | row        | The offset row points at this field |

### Row (variable: 38 bytes + texts)

| Offset                     | Type      | Field                          | Notes |
| -------------------------- | --------- | ------------------------------ | ----- |
| `+0x00`                    | u16       | npc_key                        | NPC character key (LOC type 6); every key has a LOC type 6 name on client 3483 |
| `+0x02`                    | str16     | covered_dialog_kr              | Korean line while the knowledge cannot be gained yet; LOC type 23 `(npc_key, 0)`. Lines that send the player to another NPC first open with `{Position(x, y, z)}` |
| `covered_dialog_kr+0x00`   | str8      | discover_cutscene              | `.pas` cutscene played on discovery (`CS_Velia_01_Lilia_0001.pas`); set on 16 of 2,206 rows of client 3483 |
| `discover_cutscene+0x00`   | str16     | discover_dialog_kr             | Korean line on discovery, often opening with `{AudioVoice(<voice>)}`; LOC type 23 `(npc_key, 1)` |
| `discover_dialog_kr+0x00`  | str16     | discover_function              | Script run on discovery: `Pushknowledge(<knowledge key>,0)` with an optional `;`, spelled in three cases; empty on 28 rows of client 3483 |
| `discover_function+0x00`   | str16[5]  | discover_conditions            | Condition string of each `discover_dialogs_kr` line: `0` where the line is set, empty where it is not (client 3483); see Discover Conditions |
| `discover_conditions+0x00` | str16[5]  | discover_dialogs_kr            | Five more Korean lines; line `n` (from 1) is LOC type 23 `(npc_key, n + 1)` |
| `discover_dialogs_kr+0x00` | u32       | unknown_discover_dialogs_kr_00 | `0` on every row of clients 1250, 1784 and 3483 |

The LOC type 23 key is `(npc_key, 0, 0, slot)`: slot `0` is
`covered_dialog_kr`, `1` is `discover_dialog_kr` and `2` to `6` are the five
`discover_dialogs_kr`. On client 3483 every non-empty text has its LOC row.

### `intimacyrelationoffset.dbss`

Bare offset table into `intimacyrelation.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                      |
| ------- | ----------------- | ----- | ------------------------------------------ |
| `+0x00` | u32               | count | Equals the `intimacyrelation.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                             |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                   |
| ------- | ---- | ----------- | ----------------------------------------------------------------------- |
| `+0x00` | u16  | npc_key     | Key of the record it points at                                          |
| `+0x02` | u32  | data_offset | Absolute offset in `intimacyrelation.dbss` of the row, past the key prefix |
| `+0x06` | u32  | data_size   | Row size in bytes, without the key prefix                               |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; read in offset order they cover the main file
from `+0x04` to its end, each record's key prefix included (clients 1784
and 3483).

## Layout 2

### Row (variable: 42 bytes + texts)

A u32 `npc_importance` sits between `discover_function` and
`discover_conditions`.

| Offset                     | Type     | Field                          | Notes |
| -------------------------- | -------- | ------------------------------ | ----- |
| `+0x00`                    | u16      | npc_key                        |       |
| `+0x02`                    | str16    | covered_dialog_kr              |       |
| `covered_dialog_kr+0x00`   | str8     | discover_cutscene              |       |
| `discover_cutscene+0x00`   | str16    | discover_dialog_kr             |       |
| `discover_dialog_kr+0x00`  | str16    | discover_function              |       |
| `discover_function+0x00`   | u32      | npc_importance                 | `100000` on 1,390 of 1,446 rows of client 1784, else `200000`, `300000` or `500000` |
| `discover_function+0x04`   | str16[5] | discover_conditions            |       |
| `discover_conditions+0x00` | str16[5] | discover_dialogs_kr            |       |
| `discover_dialogs_kr+0x00` | u32      | unknown_discover_dialogs_kr_00 |       |

## Layout 1

### File Layout

The rows follow the count with no key prefix in front of each. The
`intimacyrelationoffset.dbss` rows have the Layout 3 shape, but their
`data_offset` points at the row start, so the first is `0x04` (clients 1250
to 1341). The Row is the one of Layout 2.

| Offset  | Type       | Field | Notes                                 |
| ------- | ---------- | ----- | ------------------------------------- |
| `+0x00` | u32        | count | Number of NPCs; `1255` on client 1250 |
| `+0x04` | Row[count] | rows  | See Row in Layout 2                   |

## Field Names

The 2016 `gc::IntimacyRelationStaticStatus` holds `_conditionList` (five
`gc::DlgConditionList`), `_conditionStringList` and `_discoverDialogList`
(five wide strings each), `_coveredDialog` (wide), `_discoverCutScene`
(narrow, as the `str8` here), `_discoverDialog` (wide), `_discoverExecutes`
(a `gc::DlgCommonExecute` list), `_key` (u16) and `_supportPointPercent`
(i32). The `NpcRelation` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `NpcKey`, `NPC_Importance`, `NpcIcon`,
`CoveredDialog`, `DiscoverDialog`, `DiscoverFunction`, `DiscoverCutScene`
and `DiscoverCondition1` to `5` with `DiscoverDialog1` to `5`, 1,643 rows.
Matched by `NpcKey`, empty cells (`<null>`) as empty strings:

| Field               | Column                          | Same value (client 1784) | Same value (client 3483) |
| ------------------- | ------------------------------- | ------------------------ | ------------------------ |
| npc_key             | `NpcKey`                        | 1,446 of 1,446           | 1,592 of 1,592           |
| covered_dialog_kr   | `CoveredDialog`                 | 1,446 of 1,446           | 1,574 of 1,592           |
| discover_cutscene   | `DiscoverCutScene`              | 1,446 of 1,446           | 1,585 of 1,592           |
| discover_dialog_kr  | `DiscoverDialog`                | 1,446 of 1,446           | 1,525 of 1,592           |
| discover_function   | `DiscoverFunction`              | 1,446 of 1,446           | 1,584 of 1,592           |
| discover_conditions | `DiscoverCondition1` to `5`     | 1,446 of 1,446 each      | 1,577 to 1,584 of 1,592  |
| discover_dialogs_kr | `DiscoverDialog1` to `5`        | 1,443 to 1,446 of 1,446  | 1,562 to 1,584 of 1,592  |
| npc_importance      | `NPC_Importance`                | 1,446 of 1,446           | (Layout 3 has no field)  |

The client 3483 misses are edited texts and scripts (`Pushknowledge(372,0);`
where the sheet has no `;`). `NpcIcon` (`Icon/Quest/Messien.dds` on every
row) is not compiled. The client Lua of client 3483 reads nothing of this
table.

The 2016 loader `gc::GameCommonParameterLoaderFromExcel::loadIntimacyRelationInformation`
stores `NPC_Importance` in `_supportPointPercent` (struct offset `0x2cc`),
and `gc::IntimacyRelationStaticStatus::set` rejects a value below `0` or
above `3000000`; its error text calls the range 0 to 300 percent. So
`npc_importance` is `_supportPointPercent`, and the last u32 is a field the
2016 struct did not have yet.

The 1784 server reads a Layout 2 row in file order
(`gc::IntimacyRelationStaticStatusManager::ReadRecord_intimacyRelation`):
the key, the four texts, the u32 `npc_importance` into its record at `+0x04`
next to the key, the five condition strings, the five lines, then it parses
`discover_function` into a command list and reads the last u32 into its
record at `+0x260`. The private server's `NpcRelation` sheet in
`datasheet_relationdatatable.xlsm` on client 1784 has no column for that
u32.

## Discover Conditions

The 2016 client handles the five condition strings as follows:

1. The loader reads `DiscoverDialog<n>` only when the cell
   `DiscoverCondition<n>` is filled, which is why `0` sits exactly where a
   line is set.
2. `gc::IntimacyRelationStaticStatusManager::linkAndCheckValid` parses each
   string with `gc::DlgConditionList::parse`: split on `<or>`, then each part
   by `gc::DlgCommonCondition::parseConditions`, which knows names such as
   `getknowledge`, `getlevel`, `getintimacy` and `checkquestcondition`.
3. The token `0` builds a `gc::CheckFalse`. Its `compare` returns true only
   when `_checkValue` is false, and the parser creates every condition with
   `_checkValue` set to true.
4. `gc::IntimacyRelationStaticStatus::checkCondition` returns the first of
   the five slots whose string is not empty and whose conditions pass, or
   `-1`.

With `0` in every set slot, no slot passes in the 2016 client. The 1784
server still has a `gc::CheckFalse` class.

## Notes

- `discover_function` names a knowledge with a LOC type 34 name on 2,177
  of the 2,178 rows that set it; on 2,153 rows that name is the NPC's own
  LOC type 6 name (client 3483).
- On client 3483, LOC type 23 holds 103 texts for 53 NPC keys with no row
  here. 51 of the 53 keys have no `characterstatic.dbss` row, while every
  key with a row here has one. The 2016 loader drops a `NpcRelation` row
  whose `NpcKey` has no character and logs
  `(로컬라이징때문인지)캐릭터가 존재하지 않기에, 제외합니다.` ("the
  character does not exist, perhaps because of localization, so it is left
  out"); the texts still reach the LOC. 38 of the 53 keys are rows of the
  private server `NpcRelation` sheets on clients 1485 and 1784: Girgo Viano
  copies (`45563`, `45592`, `46040`, `47021`, `47054`, `49494` to `49517`,
  most of them PC-room or paid-service merchants by the sheet's comment
  column), the Eiorah global test server merchants (`50751` to `50757`),
  Devan `49490` and Fuba `44634`.
- The `covered_dialog_kr` lines that send the player to another NPC end
  with a note, in the English LOC of client 3483 (Zaaira, `40002`): "※ You
  must meet a certain requirement to obtain this NPC's knowledge. Visit the
  NPC marked on the world map, then return to acquire the knowledge." That
  is the line shown while the knowledge is covered.
- `discover_dialogs_kr` line 1 repeats `discover_dialog_kr` on 17 of the
  371 rows that set it (client 3483).

## Open Questions

### What the Last u32 Holds

`unknown_discover_dialogs_kr_00` is `0` on every row of clients 1250, 1784
and 3483. It is not `_supportPointPercent` (see Field Names), the 1784
server reads it into its record at `+0x260`, and the private server
`NpcRelation` sheets on clients 1485 and 1784 have no column for it.
What it holds, and what reads it, is open.

### Whether the Live Client Shows the Five Lines

In the 2016 client the condition `0` is a `gc::CheckFalse` that never
passes, so `checkCondition` picks none of the five `discover_dialogs_kr`
lines (see Discover Conditions). Whether `0` still parses that way on
client 3483, and whether anything else shows these lines, is open.

### Why Spook Has No Row

Spook `62103` and `62104` have LOC type 23 texts and `characterstatic.dbss`
rows on client 3483 but no row here, so the missing-character rule does not
explain them. Which other check leaves them out is open.
