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

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes   | Records                 | Row bytes                    |
| ------ | -------------- | ------- | ----------------------------- | ------- | ----------------------- | ---------------------------- |
| 2      | 2583 and later | 3483    | `intimacyrelation.dbss`       | 748,525 | 2,206 Row, 2,206 Record | 136 to 1,504, 337 on average |
| 2      | 2583 and later | 3483    | `intimacyrelationoffset.dbss` | 22,064  | 2,206 Offset Row        | 10                           |
| 1      | 1346 to 2575   | 2575    | `intimacyrelation.dbss`       | 667,200 | 1,895 Row, 1,895 Record | 140 to 1,508, 350 on average |
| 1      | 1346 to 2575   | 2575    | `intimacyrelationoffset.dbss` | 18,954  | 1,895 Offset Row        | 10                           |

| Layout | File                          | Known             | Unknown        |
| ------ | ----------------------------- | ----------------- | -------------- |
| 2      | `intimacyrelation.dbss`       | 739,701 B (98.8%) | 8,824 B (1.2%) |
| 2      | `intimacyrelationoffset.dbss` | 22,064 B (100.0%) | 0 B (0.0%)     |
| 1      | `intimacyrelation.dbss`       | 659,620 B (98.9%) | 7,580 B (1.1%) |
| 1      | `intimacyrelationoffset.dbss` | 18,954 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `7ea1453262f4`  |
| 3482   | Layout 2             | `7ea1453262f4`  |
| 3474   | Layout 2             | `7ea1453262f4`  |
| 3473   | Layout 2             | `7ea1453262f4`  |
| 3464   | Layout 2             | `7ea1453262f4`  |
| 3458   | Layout 2             | `7ea1453262f4`  |
| 3454   | Layout 2             | `7ea1453262f4`  |
| 3444   | Layout 2             | `7ea1453262f4`  |
| 3435   | Layout 2             | `7ea1453262f4`  |
| 3426   | Layout 2             | `7ea1453262f4`  |
| 3418   | Layout 2             | `7ea1453262f4`  |
| 3412   | Layout 2             | `7ea1453262f4`  |
| 3402   | Layout 2             | `7ea1453262f4`  |
| 3396   | Layout 2             | `7ea1453262f4`  |
| 3387   | Layout 2             | `7ea1453262f4`  |
| 3381   | Layout 2             | `7ea1453262f4`  |
| 3373   | Layout 2             | `7ea1453262f4`  |
| 3364   | Layout 2             | `7ea1453262f4`  |
| 3356   | Layout 2             | `7ea1453262f4`  |
| 3349   | Layout 2             | `7ea1453262f4`  |
| 3342   | Layout 2             | `7ea1453262f4`  |
| 3335   | Layout 2             | `7ea1453262f4`  |
| 3326   | Layout 2             | `7ea1453262f4`  |
| 3321   | Layout 2             | `7ea1453262f4`  |
| 3314   | Layout 2             | `7ea1453262f4`  |
| 3303   | Layout 2             | `7ea1453262f4`  |
| 3302   | Layout 2             | `7ea1453262f4`  |
| 3293   | Layout 2             | `7ea1453262f4`  |
| 3283   | Layout 2             | `7ea1453262f4`  |
| 3275   | Layout 2             | `7ea1453262f4`  |
| 3267   | Layout 2             | `7ea1453262f4`  |
| 3258   | Layout 2             | `7ea1453262f4`  |
| 3251   | Layout 2             | `7ea1453262f4`  |
| 3242   | Layout 2             | `7ea1453262f4`  |
| 3235   | Layout 2             | `7ea1453262f4`  |
| 3229   | Layout 2             | `7ea1453262f4`  |
| 3212   | Layout 2             | `7ea1453262f4`  |
| 3203   | Layout 2             | `7ea1453262f4`  |
| 3193   | Layout 2             | `7ea1453262f4`  |
| 3186   | Layout 2             | `7ea1453262f4`  |
| 3177   | Layout 2             | `7ea1453262f4`  |
| 3169   | Layout 2             | `7ea1453262f4`  |
| 3158   | Layout 2             | `7ea1453262f4`  |
| 3151   | Layout 2             | `7ea1453262f4`  |
| 3144   | Layout 2             | `7ea1453262f4`  |
| 3133   | Layout 2             | `7ea1453262f4`  |
| 3125   | Layout 2             | `7ea1453262f4`  |
| 3118   | Layout 2             | `7ea1453262f4`  |
| 3111   | Layout 2             | `7ea1453262f4`  |
| 3103   | Layout 2             | `7ea1453262f4`  |
| 3095   | Layout 2             | `7ea1453262f4`  |
| 3086   | Layout 2             | `7ea1453262f4`  |
| 3072   | Layout 2             | `7ea1453262f4`  |
| 3062   | Layout 2             | `7ea1453262f4`  |
| 3052   | Layout 2             | `7ea1453262f4`  |
| 3045   | Layout 2             | `7ea1453262f4`  |
| 3037   | Layout 2             | `7ea1453262f4`  |
| 3030   | Layout 2             | `7ea1453262f4`  |
| 3021   | Layout 2             | `7ea1453262f4`  |
| 3012   | Layout 2             | `7ea1453262f4`  |
| 3002   | Layout 2             | `7ea1453262f4`  |
| 2995   | Layout 2             | `7ea1453262f4`  |
| 2987   | Layout 2             | `7ea1453262f4`  |
| 2978   | Layout 2             | `7ea1453262f4`  |
| 2970   | Layout 2             | `7ea1453262f4`  |
| 2959   | Layout 2             | `7ea1453262f4`  |
| 2951   | Layout 2             | `7ea1453262f4`  |
| 2942   | Layout 2             | `7ea1453262f4`  |
| 2935   | Layout 2             | `7ea1453262f4`  |
| 2932   | Layout 2             | `7ea1453262f4`  |
| 2923   | Layout 2             | `7ea1453262f4`  |
| 2919   | Layout 2             | `7ea1453262f4`  |
| 2907   | Layout 2             | `7ea1453262f4`  |
| 2900   | Layout 2             | `7ea1453262f4`  |
| 2891   | Layout 2             | `7ea1453262f4`  |
| 2882   | Layout 2             | `7ea1453262f4`  |
| 2872   | Layout 2             | `7ea1453262f4`  |
| 2863   | Layout 2             | `7ea1453262f4`  |
| 2855   | Layout 2             | `7ea1453262f4`  |
| 2849   | Layout 2             | `7ea1453262f4`  |
| 2844   | Layout 2             | `7ea1453262f4`  |
| 2834   | Layout 2             | `7ea1453262f4`  |
| 2825   | Layout 2             | `7ea1453262f4`  |
| 2819   | Layout 2             | `7ea1453262f4`  |
| 2811   | Layout 2             | `7ea1453262f4`  |
| 2803   | Layout 2             | `7ea1453262f4`  |
| 2794   | Layout 2             | `7ea1453262f4`  |
| 2783   | Layout 2             | `7ea1453262f4`  |
| 2774   | Layout 2             | `7ea1453262f4`  |
| 2765   | Layout 2             | `7ea1453262f4`  |
| 2756   | Layout 2             | `7ea1453262f4`  |
| 2750   | Layout 2             | `7ea1453262f4`  |
| 2743   | Layout 2             | `7ea1453262f4`  |
| 2736   | Layout 2             | `7ea1453262f4`  |
| 2726   | Layout 2             | `7ea1453262f4`  |
| 2717   | Layout 2             | `7ea1453262f4`  |
| 2709   | Layout 2             | `7ea1453262f4`  |
| 2703   | Layout 2             | `7ea1453262f4`  |
| 2695   | Layout 2             | `7ea1453262f4`  |
| 2684   | Layout 2             | `7ea1453262f4`  |
| 2672   | Layout 2             | `7ea1453262f4`  |
| 2665   | Layout 2             | `7ea1453262f4`  |
| 2657   | Layout 2             | `7ea1453262f4`  |
| 2649   | Layout 2             | `7ea1453262f4`  |
| 2644   | Layout 2             | `7ea1453262f4`  |
| 2637   | Layout 2             | `7ea1453262f4`  |
| 2629   | Layout 2             | `7ea1453262f4`  |
| 2619   | Layout 2             | `7ea1453262f4`  |
| 2612   | Layout 2             | `7ea1453262f4`  |
| 2606   | Layout 2             | `7ea1453262f4`  |
| 2602   | Layout 2             | `7ea1453262f4`  |
| 2601   | Layout 2             | `7ea1453262f4`  |
| 2592   | Layout 2             | `7ea1453262f4`  |
| 2583   | Layout 2             | `7ea1453262f4`  |
| 2575   | Layout 1             | `7ea1453262f4`  |
| 2567   | Layout 1             | `7ea1453262f4`  |
| 2560   | Layout 1             | `7ea1453262f4`  |
| 2553   | Layout 1             | `7ea1453262f4`  |
| 2545   | Layout 1             | `7ea1453262f4`  |
| 2538   | Layout 1             | `7ea1453262f4`  |
| 2529   | Layout 1             | `7ea1453262f4`  |
| 2519   | Layout 1             | `7ea1453262f4`  |
| 2513   | Layout 1             | `7ea1453262f4`  |
| 2510   | Layout 1             | `7ea1453262f4`  |
| 2507   | Layout 1             | `7ea1453262f4`  |
| 2503   | Layout 1             | `7ea1453262f4`  |
| 2498   | Layout 1             | `7ea1453262f4`  |
| 2492   | Layout 1             | `7ea1453262f4`  |
| 2487   | Layout 1             | `7ea1453262f4`  |
| 2480   | Layout 1             | `7ea1453262f4`  |
| 2474   | Layout 1             | `7ea1453262f4`  |
| 2468   | Layout 1             | `7ea1453262f4`  |
| 2460   | Layout 1             | `7ea1453262f4`  |
| 2453   | Layout 1             | `7ea1453262f4`  |
| 2444   | Layout 1             | `7ea1453262f4`  |
| 2438   | Layout 1             | `7ea1453262f4`  |
| 2434   | Layout 1             | `7ea1453262f4`  |
| 2429   | Layout 1             | `7ea1453262f4`  |
| 2421   | Layout 1             | `7ea1453262f4`  |
| 2414   | Layout 1             | `7ea1453262f4`  |
| 2407   | Layout 1             | `7ea1453262f4`  |
| 2401   | Layout 1             | `7ea1453262f4`  |
| 2397   | Layout 1             | `7ea1453262f4`  |
| 2393   | Layout 1             | `7ea1453262f4`  |
| 2384   | Layout 1             | `7ea1453262f4`  |
| 2378   | Layout 1             | `7ea1453262f4`  |
| 2372   | Layout 1             | `7ea1453262f4`  |
| 2358   | Layout 1             | `7ea1453262f4`  |
| 2352   | Layout 1             | `7ea1453262f4`  |
| 2347   | Layout 1             | `7ea1453262f4`  |
| 2343   | Layout 1             | `7ea1453262f4`  |
| 2335   | Layout 1             | `7ea1453262f4`  |
| 2327   | Layout 1             | `7ea1453262f4`  |
| 2324   | Layout 1             | `7ea1453262f4`  |
| 2319   | Layout 1             | `7ea1453262f4`  |
| 2313   | Layout 1             | `7ea1453262f4`  |
| 2308   | Layout 1             | `7ea1453262f4`  |
| 2302   | Layout 1             | `7ea1453262f4`  |
| 2295   | Layout 1             | `7ea1453262f4`  |
| 2290   | Layout 1             | `7ea1453262f4`  |
| 2284   | Layout 1             | `7ea1453262f4`  |
| 2276   | Layout 1             | `7ea1453262f4`  |
| 2269   | Layout 1             | `7ea1453262f4`  |
| 2259   | Layout 1             | `7ea1453262f4`  |
| 2250   | Layout 1             | `7ea1453262f4`  |
| 2243   | Layout 1             | `7ea1453262f4`  |
| 2235   | Layout 1             | `7ea1453262f4`  |
| 2229   | Layout 1             | `7ea1453262f4`  |
| 2224   | Layout 1             | `7ea1453262f4`  |
| 2218   | Layout 1             | `7ea1453262f4`  |
| 2215   | Layout 1             | `7ea1453262f4`  |
| 2207   | Layout 1             | `7ea1453262f4`  |
| 2203   | Layout 1             | `7ea1453262f4`  |
| 2196   | Layout 1             | `7ea1453262f4`  |
| 2192   | Layout 1             | `7ea1453262f4`  |
| 2189   | Layout 1             | `7ea1453262f4`  |
| 2183   | Layout 1             | `7ea1453262f4`  |
| 2179   | Layout 1             | `7ea1453262f4`  |
| 2171   | Layout 1             | `7ea1453262f4`  |
| 2163   | Layout 1             | `7ea1453262f4`  |
| 2156   | Layout 1             | `7ea1453262f4`  |
| 2151   | Layout 1             | `7ea1453262f4`  |
| 2147   | Layout 1             | `7ea1453262f4`  |
| 2142   | Layout 1             | `7ea1453262f4`  |
| 2138   | Layout 1             | `7ea1453262f4`  |
| 2134   | Layout 1             | `7ea1453262f4`  |
| 2130   | Layout 1             | `7ea1453262f4`  |
| 2122   | Layout 1             | `7ea1453262f4`  |
| 2107   | Layout 1             | `7ea1453262f4`  |
| 2098   | Layout 1             | `7ea1453262f4`  |
| 2089   | Layout 1             | `7ea1453262f4`  |
| 2081   | Layout 1             | `7ea1453262f4`  |
| 2073   | Layout 1             | `7ea1453262f4`  |
| 2067   | Layout 1             | `7ea1453262f4`  |
| 2063   | Layout 1             | `7ea1453262f4`  |
| 2059   | Layout 1             | `7ea1453262f4`  |
| 2052   | Layout 1             | `7ea1453262f4`  |
| 2044   | Layout 1             | `7ea1453262f4`  |
| 2039   | Layout 1             | `7ea1453262f4`  |
| 2032   | Layout 1             | `7ea1453262f4`  |
| 2025   | Layout 1             | `7ea1453262f4`  |
| 2011   | Layout 1             | `7ea1453262f4`  |
| 2005   | Layout 1             | `7ea1453262f4`  |
| 2000   | Layout 1             | `7ea1453262f4`  |
| 1996   | Layout 1             | `7ea1453262f4`  |
| 1991   | Layout 1             | `7ea1453262f4`  |
| 1985   | Layout 1             | `7ea1453262f4`  |
| 1980   | Layout 1             | `7ea1453262f4`  |
| 1969   | Layout 1             | `7ea1453262f4`  |
| 1964   | Layout 1             | `7ea1453262f4`  |
| 1958   | Layout 1             | `7ea1453262f4`  |
| 1950   | Layout 1             | `7ea1453262f4`  |
| 1945   | Layout 1             | `7ea1453262f4`  |
| 1937   | Layout 1             | `7ea1453262f4`  |
| 1933   | Layout 1             | `7ea1453262f4`  |
| 1927   | Layout 1             | `7ea1453262f4`  |
| 1921   | Layout 1             | `7ea1453262f4`  |
| 1914   | Layout 1             | `7ea1453262f4`  |
| 1908   | Layout 1             | `7ea1453262f4`  |
| 1897   | Layout 1             | `7ea1453262f4`  |
| 1892   | Layout 1             | `7ea1453262f4`  |
| 1886   | Layout 1             | `7ea1453262f4`  |
| 1881   | Layout 1             | `7ea1453262f4`  |
| 1871   | Layout 1             | `7ea1453262f4`  |
| 1866   | Layout 1             | `7ea1453262f4`  |
| 1862   | Layout 1             | `7ea1453262f4`  |
| 1854   | Layout 1             | `7ea1453262f4`  |
| 1846   | Layout 1             | `7ea1453262f4`  |
| 1838   | Layout 1             | `7ea1453262f4`  |
| 1832   | Layout 1             | `7ea1453262f4`  |
| 1826   | Layout 1             | `7ea1453262f4`  |
| 1822   | Layout 1             | `7ea1453262f4`  |
| 1818   | Layout 1             | `7ea1453262f4`  |
| 1804   | Layout 1             | `7ea1453262f4`  |
| 1794   | Layout 1             | `7ea1453262f4`  |
| 1790   | Layout 1             | `7ea1453262f4`  |
| 1784   | Layout 1             | `7ea1453262f4`  |
| 1774   | Layout 1             | `7ea1453262f4`  |
| 1771   | Layout 1             | `7ea1453262f4`  |
| 1762   | Layout 1             | `7ea1453262f4`  |
| 1759   | Layout 1             | `7ea1453262f4`  |
| 1754   | Layout 1             | `7ea1453262f4`  |
| 1749   | Layout 1             | `7ea1453262f4`  |
| 1743   | Layout 1             | `7ea1453262f4`  |
| 1737   | Layout 1             | `7ea1453262f4`  |
| 1731   | Layout 1             | `7ea1453262f4`  |
| 1725   | Layout 1             | `7ea1453262f4`  |
| 1717   | Layout 1             | `7ea1453262f4`  |
| 1710   | Layout 1             | `7ea1453262f4`  |
| 1704   | Layout 1             | `7ea1453262f4`  |
| 1698   | Layout 1             | `7ea1453262f4`  |
| 1690   | Layout 1             | `7ea1453262f4`  |
| 1685   | Layout 1             | `7ea1453262f4`  |
| 1680   | Layout 1             | `7ea1453262f4`  |
| 1674   | Layout 1             | `7ea1453262f4`  |
| 1668   | Layout 1             | `7ea1453262f4`  |
| 1659   | Layout 1             | `7ea1453262f4`  |
| 1649   | Layout 1             | `7ea1453262f4`  |
| 1642   | Layout 1             | `7ea1453262f4`  |
| 1636   | Layout 1             | `7ea1453262f4`  |
| 1628   | Layout 1             | `7ea1453262f4`  |
| 1622   | Layout 1             | `7ea1453262f4`  |
| 1614   | Layout 1             | `7ea1453262f4`  |
| 1608   | Layout 1             | `7ea1453262f4`  |
| 1602   | Layout 1             | `7ea1453262f4`  |
| 1598   | Layout 1             | `7ea1453262f4`  |
| 1594   | Layout 1             | `7ea1453262f4`  |
| 1590   | Layout 1             | `7ea1453262f4`  |
| 1587   | Layout 1             | `7ea1453262f4`  |
| 1584   | Layout 1             | `7ea1453262f4`  |
| 1579   | Layout 1             | `7ea1453262f4`  |
| 1572   | Layout 1             | `7ea1453262f4`  |
| 1565   | Layout 1             | `7ea1453262f4`  |
| 1559   | Layout 1             | `7ea1453262f4`  |
| 1554   | Layout 1             | `7ea1453262f4`  |
| 1547   | Layout 1             | `7ea1453262f4`  |
| 1537   | Layout 1             | `7ea1453262f4`  |
| 1529   | Layout 1             | `7ea1453262f4`  |
| 1524   | Layout 1             | `7ea1453262f4`  |
| 1519   | Layout 1             | `7ea1453262f4`  |
| 1509   | Layout 1             | `7ea1453262f4`  |
| 1506   | Layout 1             | `7ea1453262f4`  |
| 1504   | Layout 1             | `7ea1453262f4`  |
| 1500   | Layout 1             | `7ea1453262f4`  |
| 1493   | Layout 1             | `7ea1453262f4`  |
| 1489   | Layout 1             | `7ea1453262f4`  |
| 1485   | Layout 1             | `7ea1453262f4`  |
| 1481   | Layout 1             | `7ea1453262f4`  |
| 1474   | Layout 1             | `7ea1453262f4`  |
| 1466   | Layout 1             | `7ea1453262f4`  |
| 1462   | Layout 1             | `7ea1453262f4`  |
| 1459   | Layout 1             | `7ea1453262f4`  |
| 1453   | Layout 1             | `7ea1453262f4`  |
| 1450   | Layout 1             | `7ea1453262f4`  |
| 1445   | Layout 1             | `7ea1453262f4`  |
| 1439   | Layout 1             | `7ea1453262f4`  |
| 1433   | Layout 1             | `7ea1453262f4`  |
| 1430   | Layout 1             | `7ea1453262f4`  |
| 1426   | Layout 1             | `7ea1453262f4`  |
| 1421   | Layout 1             | `7ea1453262f4`  |
| 1417   | Layout 1             | `7ea1453262f4`  |
| 1416   | Layout 1             | `7ea1453262f4`  |
| 1409   | Layout 1             | `7ea1453262f4`  |
| 1405   | Layout 1             | `7ea1453262f4`  |
| 1401   | Layout 1             | `7ea1453262f4`  |
| 1396   | Layout 1             | `7ea1453262f4`  |
| 1391   | Layout 1             | `7ea1453262f4`  |
| 1390   | Layout 1             | `7ea1453262f4`  |
| 1386   | Layout 1             | `7ea1453262f4`  |
| 1381   | Layout 1             | `7ea1453262f4`  |
| 1379   | Layout 1             | `7ea1453262f4`  |
| 1372   | Layout 1             | `7ea1453262f4`  |
| 1366   | Layout 1             | `7ea1453262f4`  |
| 1364   | Layout 1             | `7ea1453262f4`  |
| 1363   | Layout 1             | `7ea1453262f4`  |
| 1360   | Layout 1             | `7ea1453262f4`  |
| 1358   | Layout 1             | `7ea1453262f4`  |
| 1355   | Layout 1             | `7ea1453262f4`  |
| 1351   | Layout 1             | `7ea1453262f4`  |
| 1348   | Layout 1             | `7ea1453262f4`  |
| 1346   | Layout 1             | `7ea1453262f4`  |
| 1341   | No documented layout | `7ea1453262f4`  |
| 1340   | No documented layout | `7ea1453262f4`  |
| 1338   | No documented layout | `7ea1453262f4`  |
| 1335   | No documented layout | `7ea1453262f4`  |
| 1333   | No documented layout | `7ea1453262f4`  |
| 1329   | No documented layout | `7ea1453262f4`  |
| 1327   | No documented layout | `7ea1453262f4`  |
| 1324   | No documented layout | `7ea1453262f4`  |
| 1321   | No documented layout | `7ea1453262f4`  |
| 1319   | No documented layout | `7ea1453262f4`  |
| 1318   | No documented layout | `7ea1453262f4`  |
| 1316   | No documented layout | `7ea1453262f4`  |
| 1313   | No documented layout | `7ea1453262f4`  |
| 1311   | No documented layout | `7ea1453262f4`  |
| 1309   | No documented layout | `7ea1453262f4`  |
| 1304   | No documented layout | `7ea1453262f4`  |
| 1292   | No documented layout | `7ea1453262f4`  |
| 1286   | No documented layout | `7ea1453262f4`  |
| 1280   | No documented layout | `7ea1453262f4`  |
| 1276   | No documented layout | `7ea1453262f4`  |
| 1267   | No documented layout | `7ea1453262f4`  |
| 1261   | No documented layout | `7ea1453262f4`  |
| 1256   | No documented layout | `7ea1453262f4`  |
| 1250   | No documented layout | `7ea1453262f4`  |
| 1246   | No file              | `7ea1453262f4`  |
| 1239   | No file              | `7ea1453262f4`  |
| 1230   | No file              | `7ea1453262f4`  |
| 1226   | No file              | `7ea1453262f4`  |
| 1220   | No file              | `7ea1453262f4`  |
| 1217   | No file              | `7ea1453262f4`  |
| 1211   | No file              | `7ea1453262f4`  |
| 1210   | No file              | `7ea1453262f4`  |
| 1208   | No file              | `7ea1453262f4`  |
| 1203   | No file              | `7ea1453262f4`  |
| 1197   | No file              | `7ea1453262f4`  |
| 1194   | No file              | `7ea1453262f4`  |
| 1192   | No file              | `7ea1453262f4`  |
| 1187   | No file              | `7ea1453262f4`  |
| 1183   | No file              | `7ea1453262f4`  |
| 1177   | No file              | `7ea1453262f4`  |
| 1173   | No file              | `7ea1453262f4`  |
| 1167   | No file              | `7ea1453262f4`  |
| 1164   | No file              | `7ea1453262f4`  |
| 1156   | No file              | `7ea1453262f4`  |
| 1149   | No file              | `7ea1453262f4`  |
| 1144   | No file              | `7ea1453262f4`  |
| 1137   | No file              | `7ea1453262f4`  |
| 1132   | No file              | `7ea1453262f4`  |
| 1127   | No file              | `7ea1453262f4`  |
| 1122   | No file              | `7ea1453262f4`  |
| 1118   | No file              | `7ea1453262f4`  |
| 1114   | No file              | `7ea1453262f4`  |
| 1109   | No file              | `7ea1453262f4`  |
| 1102   | No file              | `7ea1453262f4`  |
| 1096   | No file              | `7ea1453262f4`  |
| 1088   | No file              | `7ea1453262f4`  |
| 1081   | No file              | `7ea1453262f4`  |
| 1076   | No file              | `7ea1453262f4`  |
| 1069   | No file              | `7ea1453262f4`  |
| 1064   | No file              | `7ea1453262f4`  |
| 1058   | No file              | `7ea1453262f4`  |
| 1051   | No file              | `7ea1453262f4`  |
| 1044   | No file              | `7ea1453262f4`  |
| 1036   | No file              | `7ea1453262f4`  |
| 1026   | No file              | `7ea1453262f4`  |
| 1016   | No file              | `7ea1453262f4`  |
| 1009   | No file              | `7ea1453262f4`  |
| 1005   | No file              | `7ea1453262f4`  |
| 1000   | No file              | `7ea1453262f4`  |
| 998    | No file              | `7ea1453262f4`  |
| 990    | No file              | `7ea1453262f4`  |
| 979    | No file              | `7ea1453262f4`  |
| 972    | No file              | `7ea1453262f4`  |
| 963    | No file              | `7ea1453262f4`  |
| 955    | No file              | `7ea1453262f4`  |
| 946    | No file              | `7ea1453262f4`  |
| 938    | No file              | `7ea1453262f4`  |
| 927    | No file              | `7ea1453262f4`  |
| 911    | No file              | `7ea1453262f4`  |
| 904    | No file              | `7ea1453262f4`  |
| 899    | No file              | `7ea1453262f4`  |
| 894    | No file              | `7ea1453262f4`  |
| 885    | No file              | `7ea1453262f4`  |
| 879    | No file              | `7ea1453262f4`  |
| 872    | No file              | `7ea1453262f4`  |
| 864    | No file              | `7ea1453262f4`  |
| 855    | No file              | `7ea1453262f4`  |
| 853    | No file              | `7ea1453262f4`  |
| 845    | No file              | `7ea1453262f4`  |
| 837    | No file              | `7ea1453262f4`  |
| 829    | No file              | `7ea1453262f4`  |
| 822    | No file              | `7ea1453262f4`  |
| 814    | No file              | `7ea1453262f4`  |
| 805    | No file              | `7ea1453262f4`  |
| 794    | No file              | `7ea1453262f4`  |
| 787    | No file              | `7ea1453262f4`  |
| 780    | No file              | `7ea1453262f4`  |
| 771    | No file              | `7ea1453262f4`  |
| 760    | No file              | `7ea1453262f4`  |
| 748    | No file              | `7ea1453262f4`  |
| 741    | No file              | `7ea1453262f4`  |
| 736    | No file              | `7ea1453262f4`  |
| 731    | No file              | `7ea1453262f4`  |
| 723    | No file              | `7ea1453262f4`  |
| 711    | No file              | `7ea1453262f4`  |
| 707    | No file              | `7ea1453262f4`  |
| 697    | No file              | `7ea1453262f4`  |
| 689    | No file              | `7ea1453262f4`  |
| 683    | No file              | `7ea1453262f4`  |
| 678    | No file              | `7ea1453262f4`  |
| 670    | No file              | `7ea1453262f4`  |
| 661    | No file              | `7ea1453262f4`  |
| 656    | No file              | `7ea1453262f4`  |
| 652    | No file              | `7ea1453262f4`  |
| 643    | No file              | `7ea1453262f4`  |
| 637    | No file              | `7ea1453262f4`  |
| 630    | No file              | `7ea1453262f4`  |
| 627    | No file              | `7ea1453262f4`  |
| 621    | No file              | `7ea1453262f4`  |
| 617    | No file              | `7ea1453262f4`  |
| 615    | No file              | `7ea1453262f4`  |
| 606    | No file              | `7ea1453262f4`  |
| 599    | No file              | `7ea1453262f4`  |
| 592    | No file              | `7ea1453262f4`  |
| 586    | No file              | `7ea1453262f4`  |
| 577    | No file              | `7ea1453262f4`  |
| 569    | No file              | `7ea1453262f4`  |
| 561    | No file              | `7ea1453262f4`  |
| 554    | No file              | `7ea1453262f4`  |
| 542    | No file              | `7ea1453262f4`  |
| 532    | No file              | `7ea1453262f4`  |
| 531    | No file              | `7ea1453262f4`  |
| 526    | No file              | `7ea1453262f4`  |
| 521    | No file              | `7ea1453262f4`  |
| 517    | No file              | `7ea1453262f4`  |
| 510    | No file              | `7ea1453262f4`  |
| 508    | No file              | `7ea1453262f4`  |
| 504    | No file              | `7ea1453262f4`  |
| 497    | No file              | `7ea1453262f4`  |
| 491    | No file              | `7ea1453262f4`  |
| 485    | No file              | `7ea1453262f4`  |
| 478    | No file              | `7ea1453262f4`  |
| 472    | No file              | `7ea1453262f4`  |
| 466    | No file              | `7ea1453262f4`  |
| 457    | No file              | `7ea1453262f4`  |
| 452    | No file              | `7ea1453262f4`  |
| 449    | No file              | `7ea1453262f4`  |
| 435    | No file              | `7ea1453262f4`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                            |
| --------------------------------- | -------- | ------------------------------------------------------------------------------- |
| `intimacyrelationoffset.dbss`     | Optional | `npc_key -> (offset, size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`             | Optional | NPC names (type 6), knowledge names (type 34) and the record's texts (type 23)  |

All multi-byte values are little-endian.

## Layout 2

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
| `discover_function+0x00`   | str16[5]  | discover_conditions            | Condition string of each `discover_dialogs_kr` line: `0` where the line is set, empty where it is not (client 3483) |
| `discover_conditions+0x00` | str16[5]  | discover_dialogs_kr            | Five more Korean lines; line `n` (from 1) is LOC type 23 `(npc_key, n + 1)` |
| `discover_dialogs_kr+0x00` | u32       | unknown_discover_dialogs_kr_00 | `0` on every row of clients 1784 and 3483 |

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

## Layout 1

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
| npc_importance      | `NPC_Importance`                | 1,446 of 1,446           | (Layout 2 has no field)  |

The client 3483 misses are edited texts and scripts (`Pushknowledge(372,0);`
where the sheet has no `;`). `NpcIcon` (`Icon/Quest/Messien.dds` on every
row) is not compiled. The client Lua of client 3483 reads nothing of this
table.

## Notes

- `discover_function` names a knowledge with a LOC type 34 name on 2,177
  of the 2,178 rows that set it; on 2,153 rows that name is the NPC's own
  LOC type 6 name (client 3483).
- LOC type 23 holds texts for 103 NPC keys with no row here (client 3483).
- The `covered_dialog_kr` lines that send the player to another NPC end
  with a note, in the English LOC of client 3483 (Zaaira, `40002`): "※ You
  must meet a certain requirement to obtain this NPC's knowledge. Visit the
  NPC marked on the world map, then return to acquire the knowledge." That
  is the line shown while the knowledge is covered.
- `discover_dialogs_kr` line 1 repeats `discover_dialog_kr` on 17 of the
  371 rows that set it (client 3483).

## Open Questions

### What the Last u32 Holds

`unknown_discover_dialogs_kr_00` is `0` on every row of clients 1784 and
3483. The 2016 struct has one i32 member, `_supportPointPercent`, and Layout
1 has two u32 fields: `npc_importance` (the `NPC_Importance` column by
value) and this one. Which of the two was `_supportPointPercent`, and what
the client does with it, is open.

### What a Condition String Selects

`discover_conditions` holds `0` exactly where its line is set. The 2016
struct parses each string into a `gc::DlgConditionList`; whether `0` means
"no condition" or a condition kind, and when the client shows each of the
five lines, is open.
