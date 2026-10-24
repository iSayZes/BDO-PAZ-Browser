# `knowledgelearningcharacterkey.bss` Format

## Purpose

Lists, for each knowledge card that a character teaches, every character that teaches it. It is the reverse of `knowledgelearning.dbss` table 0 (character → card), grouped by card: same pairs, no extra data.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes  | Records          | Row bytes               |
| ------ | -------------- | ------- | ----------------------------------- | ------ | ---------------- | ----------------------- |
| 1      | 1239 and later | 3483    | `knowledgelearningcharacterkey.bss` | 16,848 | 1,458 Card Entry | 10 to 70, 12 on average |

| Layout | File                                | Known             | Unknown    |
| ------ | ----------------------------------- | ----------------- | ---------- |
| 1      | `knowledgelearningcharacterkey.bss` | 16,848 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a52c5d133f9a`  |
| 3482   | Layout 1 | `a52c5d133f9a`  |
| 3474   | Layout 1 | `a52c5d133f9a`  |
| 3473   | Layout 1 | `a52c5d133f9a`  |
| 3464   | Layout 1 | `a52c5d133f9a`  |
| 3458   | Layout 1 | `a52c5d133f9a`  |
| 3454   | Layout 1 | `a52c5d133f9a`  |
| 3444   | Layout 1 | `a52c5d133f9a`  |
| 3435   | Layout 1 | `a52c5d133f9a`  |
| 3426   | Layout 1 | `a52c5d133f9a`  |
| 3418   | Layout 1 | `a52c5d133f9a`  |
| 3412   | Layout 1 | `a52c5d133f9a`  |
| 3402   | Layout 1 | `a52c5d133f9a`  |
| 3396   | Layout 1 | `a52c5d133f9a`  |
| 3387   | Layout 1 | `a52c5d133f9a`  |
| 3381   | Layout 1 | `a52c5d133f9a`  |
| 3373   | Layout 1 | `a52c5d133f9a`  |
| 3364   | Layout 1 | `a52c5d133f9a`  |
| 3356   | Layout 1 | `a52c5d133f9a`  |
| 3349   | Layout 1 | `a52c5d133f9a`  |
| 3342   | Layout 1 | `a52c5d133f9a`  |
| 3335   | Layout 1 | `a52c5d133f9a`  |
| 3326   | Layout 1 | `a52c5d133f9a`  |
| 3321   | Layout 1 | `a52c5d133f9a`  |
| 3314   | Layout 1 | `a52c5d133f9a`  |
| 3303   | Layout 1 | `a52c5d133f9a`  |
| 3302   | Layout 1 | `a52c5d133f9a`  |
| 3293   | Layout 1 | `a52c5d133f9a`  |
| 3283   | Layout 1 | `a52c5d133f9a`  |
| 3275   | Layout 1 | `a52c5d133f9a`  |
| 3267   | Layout 1 | `a52c5d133f9a`  |
| 3258   | Layout 1 | `a52c5d133f9a`  |
| 3251   | Layout 1 | `a52c5d133f9a`  |
| 3242   | Layout 1 | `a52c5d133f9a`  |
| 3235   | Layout 1 | `a52c5d133f9a`  |
| 3229   | Layout 1 | `a52c5d133f9a`  |
| 3212   | Layout 1 | `a52c5d133f9a`  |
| 3203   | Layout 1 | `a52c5d133f9a`  |
| 3193   | Layout 1 | `a52c5d133f9a`  |
| 3186   | Layout 1 | `a52c5d133f9a`  |
| 3177   | Layout 1 | `a52c5d133f9a`  |
| 3169   | Layout 1 | `a52c5d133f9a`  |
| 3158   | Layout 1 | `a52c5d133f9a`  |
| 3151   | Layout 1 | `a52c5d133f9a`  |
| 3144   | Layout 1 | `a52c5d133f9a`  |
| 3133   | Layout 1 | `a52c5d133f9a`  |
| 3125   | Layout 1 | `a52c5d133f9a`  |
| 3118   | Layout 1 | `a52c5d133f9a`  |
| 3111   | Layout 1 | `a52c5d133f9a`  |
| 3103   | Layout 1 | `a52c5d133f9a`  |
| 3095   | Layout 1 | `a52c5d133f9a`  |
| 3086   | Layout 1 | `a52c5d133f9a`  |
| 3072   | Layout 1 | `a52c5d133f9a`  |
| 3062   | Layout 1 | `a52c5d133f9a`  |
| 3052   | Layout 1 | `a52c5d133f9a`  |
| 3045   | Layout 1 | `a52c5d133f9a`  |
| 3037   | Layout 1 | `a52c5d133f9a`  |
| 3030   | Layout 1 | `a52c5d133f9a`  |
| 3021   | Layout 1 | `a52c5d133f9a`  |
| 3012   | Layout 1 | `a52c5d133f9a`  |
| 3002   | Layout 1 | `a52c5d133f9a`  |
| 2995   | Layout 1 | `a52c5d133f9a`  |
| 2987   | Layout 1 | `a52c5d133f9a`  |
| 2978   | Layout 1 | `a52c5d133f9a`  |
| 2970   | Layout 1 | `a52c5d133f9a`  |
| 2959   | Layout 1 | `a52c5d133f9a`  |
| 2951   | Layout 1 | `a52c5d133f9a`  |
| 2942   | Layout 1 | `a52c5d133f9a`  |
| 2935   | Layout 1 | `a52c5d133f9a`  |
| 2932   | Layout 1 | `a52c5d133f9a`  |
| 2923   | Layout 1 | `a52c5d133f9a`  |
| 2919   | Layout 1 | `a52c5d133f9a`  |
| 2907   | Layout 1 | `a52c5d133f9a`  |
| 2900   | Layout 1 | `a52c5d133f9a`  |
| 2891   | Layout 1 | `a52c5d133f9a`  |
| 2882   | Layout 1 | `a52c5d133f9a`  |
| 2872   | Layout 1 | `a52c5d133f9a`  |
| 2863   | Layout 1 | `a52c5d133f9a`  |
| 2855   | Layout 1 | `a52c5d133f9a`  |
| 2849   | Layout 1 | `a52c5d133f9a`  |
| 2844   | Layout 1 | `a52c5d133f9a`  |
| 2834   | Layout 1 | `a52c5d133f9a`  |
| 2825   | Layout 1 | `a52c5d133f9a`  |
| 2819   | Layout 1 | `a52c5d133f9a`  |
| 2811   | Layout 1 | `a52c5d133f9a`  |
| 2803   | Layout 1 | `a52c5d133f9a`  |
| 2794   | Layout 1 | `a52c5d133f9a`  |
| 2783   | Layout 1 | `a52c5d133f9a`  |
| 2774   | Layout 1 | `a52c5d133f9a`  |
| 2765   | Layout 1 | `a52c5d133f9a`  |
| 2756   | Layout 1 | `a52c5d133f9a`  |
| 2750   | Layout 1 | `a52c5d133f9a`  |
| 2743   | Layout 1 | `a52c5d133f9a`  |
| 2736   | Layout 1 | `a52c5d133f9a`  |
| 2726   | Layout 1 | `a52c5d133f9a`  |
| 2717   | Layout 1 | `a52c5d133f9a`  |
| 2709   | Layout 1 | `a52c5d133f9a`  |
| 2703   | Layout 1 | `a52c5d133f9a`  |
| 2695   | Layout 1 | `a52c5d133f9a`  |
| 2684   | Layout 1 | `a52c5d133f9a`  |
| 2672   | Layout 1 | `a52c5d133f9a`  |
| 2665   | Layout 1 | `a52c5d133f9a`  |
| 2657   | Layout 1 | `a52c5d133f9a`  |
| 2649   | Layout 1 | `a52c5d133f9a`  |
| 2644   | Layout 1 | `a52c5d133f9a`  |
| 2637   | Layout 1 | `a52c5d133f9a`  |
| 2629   | Layout 1 | `a52c5d133f9a`  |
| 2619   | Layout 1 | `a52c5d133f9a`  |
| 2612   | Layout 1 | `a52c5d133f9a`  |
| 2606   | Layout 1 | `a52c5d133f9a`  |
| 2602   | Layout 1 | `a52c5d133f9a`  |
| 2601   | Layout 1 | `a52c5d133f9a`  |
| 2592   | Layout 1 | `a52c5d133f9a`  |
| 2583   | Layout 1 | `a52c5d133f9a`  |
| 2575   | Layout 1 | `a52c5d133f9a`  |
| 2567   | Layout 1 | `a52c5d133f9a`  |
| 2560   | Layout 1 | `a52c5d133f9a`  |
| 2553   | Layout 1 | `a52c5d133f9a`  |
| 2545   | Layout 1 | `a52c5d133f9a`  |
| 2538   | Layout 1 | `a52c5d133f9a`  |
| 2529   | Layout 1 | `a52c5d133f9a`  |
| 2519   | Layout 1 | `a52c5d133f9a`  |
| 2513   | Layout 1 | `a52c5d133f9a`  |
| 2510   | Layout 1 | `a52c5d133f9a`  |
| 2507   | Layout 1 | `a52c5d133f9a`  |
| 2503   | Layout 1 | `a52c5d133f9a`  |
| 2498   | Layout 1 | `a52c5d133f9a`  |
| 2492   | Layout 1 | `a52c5d133f9a`  |
| 2487   | Layout 1 | `a52c5d133f9a`  |
| 2480   | Layout 1 | `a52c5d133f9a`  |
| 2474   | Layout 1 | `a52c5d133f9a`  |
| 2468   | Layout 1 | `a52c5d133f9a`  |
| 2460   | Layout 1 | `a52c5d133f9a`  |
| 2453   | Layout 1 | `a52c5d133f9a`  |
| 2444   | Layout 1 | `a52c5d133f9a`  |
| 2438   | Layout 1 | `a52c5d133f9a`  |
| 2434   | Layout 1 | `a52c5d133f9a`  |
| 2429   | Layout 1 | `a52c5d133f9a`  |
| 2421   | Layout 1 | `a52c5d133f9a`  |
| 2414   | Layout 1 | `a52c5d133f9a`  |
| 2407   | Layout 1 | `a52c5d133f9a`  |
| 2401   | Layout 1 | `a52c5d133f9a`  |
| 2397   | Layout 1 | `a52c5d133f9a`  |
| 2393   | Layout 1 | `a52c5d133f9a`  |
| 2384   | Layout 1 | `a52c5d133f9a`  |
| 2378   | Layout 1 | `a52c5d133f9a`  |
| 2372   | Layout 1 | `a52c5d133f9a`  |
| 2358   | Layout 1 | `a52c5d133f9a`  |
| 2352   | Layout 1 | `a52c5d133f9a`  |
| 2347   | Layout 1 | `a52c5d133f9a`  |
| 2343   | Layout 1 | `a52c5d133f9a`  |
| 2335   | Layout 1 | `a52c5d133f9a`  |
| 2327   | Layout 1 | `a52c5d133f9a`  |
| 2324   | Layout 1 | `a52c5d133f9a`  |
| 2319   | Layout 1 | `a52c5d133f9a`  |
| 2313   | Layout 1 | `a52c5d133f9a`  |
| 2308   | Layout 1 | `a52c5d133f9a`  |
| 2302   | Layout 1 | `a52c5d133f9a`  |
| 2295   | Layout 1 | `a52c5d133f9a`  |
| 2290   | Layout 1 | `a52c5d133f9a`  |
| 2284   | Layout 1 | `a52c5d133f9a`  |
| 2276   | Layout 1 | `a52c5d133f9a`  |
| 2269   | Layout 1 | `a52c5d133f9a`  |
| 2259   | Layout 1 | `a52c5d133f9a`  |
| 2250   | Layout 1 | `a52c5d133f9a`  |
| 2243   | Layout 1 | `a52c5d133f9a`  |
| 2235   | Layout 1 | `a52c5d133f9a`  |
| 2229   | Layout 1 | `a52c5d133f9a`  |
| 2224   | Layout 1 | `a52c5d133f9a`  |
| 2218   | Layout 1 | `a52c5d133f9a`  |
| 2215   | Layout 1 | `a52c5d133f9a`  |
| 2207   | Layout 1 | `a52c5d133f9a`  |
| 2203   | Layout 1 | `a52c5d133f9a`  |
| 2196   | Layout 1 | `a52c5d133f9a`  |
| 2192   | Layout 1 | `a52c5d133f9a`  |
| 2189   | Layout 1 | `a52c5d133f9a`  |
| 2183   | Layout 1 | `a52c5d133f9a`  |
| 2179   | Layout 1 | `a52c5d133f9a`  |
| 2171   | Layout 1 | `a52c5d133f9a`  |
| 2163   | Layout 1 | `a52c5d133f9a`  |
| 2156   | Layout 1 | `a52c5d133f9a`  |
| 2151   | Layout 1 | `a52c5d133f9a`  |
| 2147   | Layout 1 | `a52c5d133f9a`  |
| 2142   | Layout 1 | `a52c5d133f9a`  |
| 2138   | Layout 1 | `a52c5d133f9a`  |
| 2134   | Layout 1 | `a52c5d133f9a`  |
| 2130   | Layout 1 | `a52c5d133f9a`  |
| 2122   | Layout 1 | `a52c5d133f9a`  |
| 2107   | Layout 1 | `a52c5d133f9a`  |
| 2098   | Layout 1 | `a52c5d133f9a`  |
| 2089   | Layout 1 | `a52c5d133f9a`  |
| 2081   | Layout 1 | `a52c5d133f9a`  |
| 2073   | Layout 1 | `a52c5d133f9a`  |
| 2067   | Layout 1 | `a52c5d133f9a`  |
| 2063   | Layout 1 | `a52c5d133f9a`  |
| 2059   | Layout 1 | `a52c5d133f9a`  |
| 2052   | Layout 1 | `a52c5d133f9a`  |
| 2044   | Layout 1 | `a52c5d133f9a`  |
| 2039   | Layout 1 | `a52c5d133f9a`  |
| 2032   | Layout 1 | `a52c5d133f9a`  |
| 2025   | Layout 1 | `a52c5d133f9a`  |
| 2011   | Layout 1 | `a52c5d133f9a`  |
| 2005   | Layout 1 | `a52c5d133f9a`  |
| 2000   | Layout 1 | `a52c5d133f9a`  |
| 1996   | Layout 1 | `a52c5d133f9a`  |
| 1991   | Layout 1 | `a52c5d133f9a`  |
| 1985   | Layout 1 | `a52c5d133f9a`  |
| 1980   | Layout 1 | `a52c5d133f9a`  |
| 1969   | Layout 1 | `a52c5d133f9a`  |
| 1964   | Layout 1 | `a52c5d133f9a`  |
| 1958   | Layout 1 | `a52c5d133f9a`  |
| 1950   | Layout 1 | `a52c5d133f9a`  |
| 1945   | Layout 1 | `a52c5d133f9a`  |
| 1937   | Layout 1 | `a52c5d133f9a`  |
| 1933   | Layout 1 | `a52c5d133f9a`  |
| 1927   | Layout 1 | `a52c5d133f9a`  |
| 1921   | Layout 1 | `a52c5d133f9a`  |
| 1914   | Layout 1 | `a52c5d133f9a`  |
| 1908   | Layout 1 | `a52c5d133f9a`  |
| 1897   | Layout 1 | `a52c5d133f9a`  |
| 1892   | Layout 1 | `a52c5d133f9a`  |
| 1886   | Layout 1 | `a52c5d133f9a`  |
| 1881   | Layout 1 | `a52c5d133f9a`  |
| 1871   | Layout 1 | `a52c5d133f9a`  |
| 1866   | Layout 1 | `a52c5d133f9a`  |
| 1862   | Layout 1 | `a52c5d133f9a`  |
| 1854   | Layout 1 | `a52c5d133f9a`  |
| 1846   | Layout 1 | `a52c5d133f9a`  |
| 1838   | Layout 1 | `a52c5d133f9a`  |
| 1832   | Layout 1 | `a52c5d133f9a`  |
| 1826   | Layout 1 | `a52c5d133f9a`  |
| 1822   | Layout 1 | `a52c5d133f9a`  |
| 1818   | Layout 1 | `a52c5d133f9a`  |
| 1804   | Layout 1 | `a52c5d133f9a`  |
| 1794   | Layout 1 | `a52c5d133f9a`  |
| 1790   | Layout 1 | `a52c5d133f9a`  |
| 1784   | Layout 1 | `a52c5d133f9a`  |
| 1774   | Layout 1 | `a52c5d133f9a`  |
| 1771   | Layout 1 | `a52c5d133f9a`  |
| 1762   | Layout 1 | `a52c5d133f9a`  |
| 1759   | Layout 1 | `a52c5d133f9a`  |
| 1754   | Layout 1 | `a52c5d133f9a`  |
| 1749   | Layout 1 | `a52c5d133f9a`  |
| 1743   | Layout 1 | `a52c5d133f9a`  |
| 1737   | Layout 1 | `a52c5d133f9a`  |
| 1731   | Layout 1 | `a52c5d133f9a`  |
| 1725   | Layout 1 | `a52c5d133f9a`  |
| 1717   | Layout 1 | `a52c5d133f9a`  |
| 1710   | Layout 1 | `a52c5d133f9a`  |
| 1704   | Layout 1 | `a52c5d133f9a`  |
| 1698   | Layout 1 | `a52c5d133f9a`  |
| 1690   | Layout 1 | `a52c5d133f9a`  |
| 1685   | Layout 1 | `a52c5d133f9a`  |
| 1680   | Layout 1 | `a52c5d133f9a`  |
| 1674   | Layout 1 | `a52c5d133f9a`  |
| 1668   | Layout 1 | `a52c5d133f9a`  |
| 1659   | Layout 1 | `a52c5d133f9a`  |
| 1649   | Layout 1 | `a52c5d133f9a`  |
| 1642   | Layout 1 | `a52c5d133f9a`  |
| 1636   | Layout 1 | `a52c5d133f9a`  |
| 1628   | Layout 1 | `a52c5d133f9a`  |
| 1622   | Layout 1 | `a52c5d133f9a`  |
| 1614   | Layout 1 | `a52c5d133f9a`  |
| 1608   | Layout 1 | `a52c5d133f9a`  |
| 1602   | Layout 1 | `a52c5d133f9a`  |
| 1598   | Layout 1 | `a52c5d133f9a`  |
| 1594   | Layout 1 | `a52c5d133f9a`  |
| 1590   | Layout 1 | `a52c5d133f9a`  |
| 1587   | Layout 1 | `a52c5d133f9a`  |
| 1584   | Layout 1 | `a52c5d133f9a`  |
| 1579   | Layout 1 | `a52c5d133f9a`  |
| 1572   | Layout 1 | `a52c5d133f9a`  |
| 1565   | Layout 1 | `a52c5d133f9a`  |
| 1559   | Layout 1 | `a52c5d133f9a`  |
| 1554   | Layout 1 | `a52c5d133f9a`  |
| 1547   | Layout 1 | `a52c5d133f9a`  |
| 1537   | Layout 1 | `a52c5d133f9a`  |
| 1529   | Layout 1 | `a52c5d133f9a`  |
| 1524   | Layout 1 | `a52c5d133f9a`  |
| 1519   | Layout 1 | `a52c5d133f9a`  |
| 1509   | Layout 1 | `a52c5d133f9a`  |
| 1506   | Layout 1 | `a52c5d133f9a`  |
| 1504   | Layout 1 | `a52c5d133f9a`  |
| 1500   | Layout 1 | `a52c5d133f9a`  |
| 1493   | Layout 1 | `a52c5d133f9a`  |
| 1489   | Layout 1 | `a52c5d133f9a`  |
| 1485   | Layout 1 | `a52c5d133f9a`  |
| 1481   | Layout 1 | `a52c5d133f9a`  |
| 1474   | Layout 1 | `a52c5d133f9a`  |
| 1466   | Layout 1 | `a52c5d133f9a`  |
| 1462   | Layout 1 | `a52c5d133f9a`  |
| 1459   | Layout 1 | `a52c5d133f9a`  |
| 1453   | Layout 1 | `a52c5d133f9a`  |
| 1450   | Layout 1 | `a52c5d133f9a`  |
| 1445   | Layout 1 | `a52c5d133f9a`  |
| 1439   | Layout 1 | `a52c5d133f9a`  |
| 1433   | Layout 1 | `a52c5d133f9a`  |
| 1430   | Layout 1 | `a52c5d133f9a`  |
| 1426   | Layout 1 | `a52c5d133f9a`  |
| 1421   | Layout 1 | `a52c5d133f9a`  |
| 1417   | Layout 1 | `a52c5d133f9a`  |
| 1416   | Layout 1 | `a52c5d133f9a`  |
| 1409   | Layout 1 | `a52c5d133f9a`  |
| 1405   | Layout 1 | `a52c5d133f9a`  |
| 1401   | Layout 1 | `a52c5d133f9a`  |
| 1396   | Layout 1 | `a52c5d133f9a`  |
| 1391   | Layout 1 | `a52c5d133f9a`  |
| 1390   | Layout 1 | `a52c5d133f9a`  |
| 1386   | Layout 1 | `a52c5d133f9a`  |
| 1381   | Layout 1 | `a52c5d133f9a`  |
| 1379   | Layout 1 | `a52c5d133f9a`  |
| 1372   | Layout 1 | `a52c5d133f9a`  |
| 1366   | Layout 1 | `a52c5d133f9a`  |
| 1364   | Layout 1 | `a52c5d133f9a`  |
| 1363   | Layout 1 | `a52c5d133f9a`  |
| 1360   | Layout 1 | `a52c5d133f9a`  |
| 1358   | Layout 1 | `a52c5d133f9a`  |
| 1355   | Layout 1 | `a52c5d133f9a`  |
| 1351   | Layout 1 | `a52c5d133f9a`  |
| 1348   | Layout 1 | `a52c5d133f9a`  |
| 1346   | Layout 1 | `a52c5d133f9a`  |
| 1341   | Layout 1 | `a52c5d133f9a`  |
| 1340   | Layout 1 | `a52c5d133f9a`  |
| 1338   | Layout 1 | `a52c5d133f9a`  |
| 1335   | Layout 1 | `a52c5d133f9a`  |
| 1333   | Layout 1 | `a52c5d133f9a`  |
| 1329   | Layout 1 | `a52c5d133f9a`  |
| 1327   | Layout 1 | `a52c5d133f9a`  |
| 1324   | Layout 1 | `a52c5d133f9a`  |
| 1321   | Layout 1 | `a52c5d133f9a`  |
| 1319   | Layout 1 | `a52c5d133f9a`  |
| 1318   | Layout 1 | `a52c5d133f9a`  |
| 1316   | Layout 1 | `a52c5d133f9a`  |
| 1313   | Layout 1 | `a52c5d133f9a`  |
| 1311   | Layout 1 | `a52c5d133f9a`  |
| 1309   | Layout 1 | `a52c5d133f9a`  |
| 1304   | Layout 1 | `a52c5d133f9a`  |
| 1292   | Layout 1 | `a52c5d133f9a`  |
| 1286   | Layout 1 | `a52c5d133f9a`  |
| 1280   | Layout 1 | `a52c5d133f9a`  |
| 1276   | Layout 1 | `a52c5d133f9a`  |
| 1267   | Layout 1 | `a52c5d133f9a`  |
| 1261   | Layout 1 | `a52c5d133f9a`  |
| 1256   | Layout 1 | `a52c5d133f9a`  |
| 1250   | Layout 1 | `a52c5d133f9a`  |
| 1246   | Layout 1 | `a52c5d133f9a`  |
| 1239   | Layout 1 | `a52c5d133f9a`  |
| 1230   | No file  | `a52c5d133f9a`  |
| 1226   | No file  | `a52c5d133f9a`  |
| 1220   | No file  | `a52c5d133f9a`  |
| 1217   | No file  | `a52c5d133f9a`  |
| 1211   | No file  | `a52c5d133f9a`  |
| 1210   | No file  | `a52c5d133f9a`  |
| 1208   | No file  | `a52c5d133f9a`  |
| 1203   | No file  | `a52c5d133f9a`  |
| 1197   | No file  | `a52c5d133f9a`  |
| 1194   | No file  | `a52c5d133f9a`  |
| 1192   | No file  | `a52c5d133f9a`  |
| 1187   | No file  | `a52c5d133f9a`  |
| 1183   | No file  | `a52c5d133f9a`  |
| 1177   | No file  | `a52c5d133f9a`  |
| 1173   | No file  | `a52c5d133f9a`  |
| 1167   | No file  | `a52c5d133f9a`  |
| 1164   | No file  | `a52c5d133f9a`  |
| 1156   | No file  | `a52c5d133f9a`  |
| 1149   | No file  | `a52c5d133f9a`  |
| 1144   | No file  | `a52c5d133f9a`  |
| 1137   | No file  | `a52c5d133f9a`  |
| 1132   | No file  | `a52c5d133f9a`  |
| 1127   | No file  | `a52c5d133f9a`  |
| 1122   | No file  | `a52c5d133f9a`  |
| 1118   | No file  | `a52c5d133f9a`  |
| 1114   | No file  | `a52c5d133f9a`  |
| 1109   | No file  | `a52c5d133f9a`  |
| 1102   | No file  | `a52c5d133f9a`  |
| 1096   | No file  | `a52c5d133f9a`  |
| 1088   | No file  | `a52c5d133f9a`  |
| 1081   | No file  | `a52c5d133f9a`  |
| 1076   | No file  | `a52c5d133f9a`  |
| 1069   | No file  | `a52c5d133f9a`  |
| 1064   | No file  | `a52c5d133f9a`  |
| 1058   | No file  | `a52c5d133f9a`  |
| 1051   | No file  | `a52c5d133f9a`  |
| 1044   | No file  | `a52c5d133f9a`  |
| 1036   | No file  | `a52c5d133f9a`  |
| 1026   | No file  | `a52c5d133f9a`  |
| 1016   | No file  | `a52c5d133f9a`  |
| 1009   | No file  | `a52c5d133f9a`  |
| 1005   | No file  | `a52c5d133f9a`  |
| 1000   | No file  | `a52c5d133f9a`  |
| 998    | No file  | `a52c5d133f9a`  |
| 990    | No file  | `a52c5d133f9a`  |
| 979    | No file  | `a52c5d133f9a`  |
| 972    | No file  | `a52c5d133f9a`  |
| 963    | No file  | `a52c5d133f9a`  |
| 955    | No file  | `a52c5d133f9a`  |
| 946    | No file  | `a52c5d133f9a`  |
| 938    | No file  | `a52c5d133f9a`  |
| 927    | No file  | `a52c5d133f9a`  |
| 911    | No file  | `a52c5d133f9a`  |
| 904    | No file  | `a52c5d133f9a`  |
| 899    | No file  | `a52c5d133f9a`  |
| 894    | No file  | `a52c5d133f9a`  |
| 885    | No file  | `a52c5d133f9a`  |
| 879    | No file  | `a52c5d133f9a`  |
| 872    | No file  | `a52c5d133f9a`  |
| 864    | No file  | `a52c5d133f9a`  |
| 855    | No file  | `a52c5d133f9a`  |
| 853    | No file  | `a52c5d133f9a`  |
| 845    | No file  | `a52c5d133f9a`  |
| 837    | No file  | `a52c5d133f9a`  |
| 829    | No file  | `a52c5d133f9a`  |
| 822    | No file  | `a52c5d133f9a`  |
| 814    | No file  | `a52c5d133f9a`  |
| 805    | No file  | `a52c5d133f9a`  |
| 794    | No file  | `a52c5d133f9a`  |
| 787    | No file  | `a52c5d133f9a`  |
| 780    | No file  | `a52c5d133f9a`  |
| 771    | No file  | `a52c5d133f9a`  |
| 760    | No file  | `a52c5d133f9a`  |
| 748    | No file  | `a52c5d133f9a`  |
| 741    | No file  | `a52c5d133f9a`  |
| 736    | No file  | `a52c5d133f9a`  |
| 731    | No file  | `a52c5d133f9a`  |
| 723    | No file  | `a52c5d133f9a`  |
| 711    | No file  | `a52c5d133f9a`  |
| 707    | No file  | `a52c5d133f9a`  |
| 697    | No file  | `a52c5d133f9a`  |
| 689    | No file  | `a52c5d133f9a`  |
| 683    | No file  | `a52c5d133f9a`  |
| 678    | No file  | `a52c5d133f9a`  |
| 670    | No file  | `a52c5d133f9a`  |
| 661    | No file  | `a52c5d133f9a`  |
| 656    | No file  | `a52c5d133f9a`  |
| 652    | No file  | `a52c5d133f9a`  |
| 643    | No file  | `a52c5d133f9a`  |
| 637    | No file  | `a52c5d133f9a`  |
| 630    | No file  | `a52c5d133f9a`  |
| 627    | No file  | `a52c5d133f9a`  |
| 621    | No file  | `a52c5d133f9a`  |
| 617    | No file  | `a52c5d133f9a`  |
| 615    | No file  | `a52c5d133f9a`  |
| 606    | No file  | `a52c5d133f9a`  |
| 599    | No file  | `a52c5d133f9a`  |
| 592    | No file  | `a52c5d133f9a`  |
| 586    | No file  | `a52c5d133f9a`  |
| 577    | No file  | `a52c5d133f9a`  |
| 569    | No file  | `a52c5d133f9a`  |
| 561    | No file  | `a52c5d133f9a`  |
| 554    | No file  | `a52c5d133f9a`  |
| 542    | No file  | `a52c5d133f9a`  |
| 532    | No file  | `a52c5d133f9a`  |
| 531    | No file  | `a52c5d133f9a`  |
| 526    | No file  | `a52c5d133f9a`  |
| 521    | No file  | `a52c5d133f9a`  |
| 517    | No file  | `a52c5d133f9a`  |
| 510    | No file  | `a52c5d133f9a`  |
| 508    | No file  | `a52c5d133f9a`  |
| 504    | No file  | `a52c5d133f9a`  |
| 497    | No file  | `a52c5d133f9a`  |
| 491    | No file  | `a52c5d133f9a`  |
| 485    | No file  | `a52c5d133f9a`  |
| 478    | No file  | `a52c5d133f9a`  |
| 472    | No file  | `a52c5d133f9a`  |
| 466    | No file  | `a52c5d133f9a`  |
| 457    | No file  | `a52c5d133f9a`  |
| 452    | No file  | `a52c5d133f9a`  |
| 449    | No file  | `a52c5d133f9a`  |
| 435    | No file  | `a52c5d133f9a`  |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                              |
| ------------------------ | -------- | ----------------------------------------------------------------- |
| `knowledgelearning.dbss` | Optional | Table 0 holds the same character → card pairs, one row per character |
| `mentalcard.dbss`        | Optional | Card details; `card_id` is its key                                |

All multi-byte values are little-endian.

## Layout 1

### File Layout

Plain binary: no `PABR` magic, no index file and no trailer. The file ends exactly after the last entry.

| Offset  | Type              | Field   | Notes                                  |
| ------- | ----------------- | ------- | -------------------------------------- |
| `+0x00` | u32               | count   | Number of cards; `1458` on client 3458 |
| `+0x04` | Card Entry[count] | entries | See Card Entry                         |

### Card Entry (variable: 8 bytes + character IDs)

| Offset  | Type                 | Field           | Notes                                                       |
| ------- | -------------------- | --------------- | ----------------------------------------------------------- |
| `+0x00` | u32                  | character_count | Characters that teach this card; `1` to `31` observed       |
| `+0x04` | u32                  | card_id         | Knowledge card; LOC `str_type=34`, key of `mentalcard.dbss` |
| `+0x08` | u16[character_count] | character_ids   | Character IDs; LOC `str_type=6`, keys of `characterstatic.dbss` |

## Confirmed Examples

| card_id | Card name (LOC)          | character_ids                     | Character names (LOC)                |
| ------- | ------------------------ | --------------------------------- | ------------------------------------ |
| `4686`  | Khuruto Chaser           | `20665`                           | Khuruto Chaser                       |
| `4174`  | Demibeast Bandit Warrior | `24444`, `20170`                  | Demibeast Bandit Warrior (both)      |
| `4750`  | Lightning Trumpeter      | `20733`                           | Lightning Trumpeter                  |
| `7364`  | Wild Herb                | `10263`, `10273`, ... (31 IDs)    | Wild Herb                            |

## Notes

- Checked against `knowledgelearning.dbss` on client 3458: the 1,458 cards are exactly the distinct `card_id` values of table 0, the 2,596 character IDs are exactly its `source_id` values, and every card lists its characters in table 0 row order. No character appears twice.
- Character IDs are u16 here and u32 in `knowledgelearning.dbss`; the largest observed is `35405`.
- `card_id` is unique, but the entries are not sorted by it and do not follow table 0's order. The order looks like a hash map dump and carries no meaning found so far.
- There is no item counterpart: no `knowledgelearningitemkey` file exists for table 1.
- The app does not read this file for the `mentalcard.dbss` Learned From column; it builds the same links from `knowledgelearning.dbss` (`KNOWLEDGE_LEARNING_CHARACTERS`), which also holds the item sources.
