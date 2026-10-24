# `instanceetcoption.bss` Format

## Purpose

Instance options: two u32 values in the slot where a PABR table keeps its
record count, then an empty string table. On client 3474 they are
`5,000,000` and `0`; no source confirms what either holds.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | -------------- | --------- |
| 1      | 2421 and later | 3483    | `instanceetcoption.bss` | 24    | 1 String Table | 4         |

| Layout | File                    | Known        | Unknown     |
| ------ | ----------------------- | ------------ | ----------- |
| 1      | `instanceetcoption.bss` | 16 B (66.7%) | 8 B (33.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `8b8be5a5ceba`  |
| 3482   | Layout 1 | `8b8be5a5ceba`  |
| 3474   | Layout 1 | `8b8be5a5ceba`  |
| 3473   | Layout 1 | `8b8be5a5ceba`  |
| 3464   | Layout 1 | `8b8be5a5ceba`  |
| 3458   | Layout 1 | `8b8be5a5ceba`  |
| 3454   | Layout 1 | `8b8be5a5ceba`  |
| 3444   | Layout 1 | `8b8be5a5ceba`  |
| 3435   | Layout 1 | `8b8be5a5ceba`  |
| 3426   | Layout 1 | `8b8be5a5ceba`  |
| 3418   | Layout 1 | `8b8be5a5ceba`  |
| 3412   | Layout 1 | `8b8be5a5ceba`  |
| 3402   | Layout 1 | `8b8be5a5ceba`  |
| 3396   | Layout 1 | `8b8be5a5ceba`  |
| 3387   | Layout 1 | `8b8be5a5ceba`  |
| 3381   | Layout 1 | `8b8be5a5ceba`  |
| 3373   | Layout 1 | `8b8be5a5ceba`  |
| 3364   | Layout 1 | `8b8be5a5ceba`  |
| 3356   | Layout 1 | `8b8be5a5ceba`  |
| 3349   | Layout 1 | `8b8be5a5ceba`  |
| 3342   | Layout 1 | `8b8be5a5ceba`  |
| 3335   | Layout 1 | `8b8be5a5ceba`  |
| 3326   | Layout 1 | `8b8be5a5ceba`  |
| 3321   | Layout 1 | `8b8be5a5ceba`  |
| 3314   | Layout 1 | `8b8be5a5ceba`  |
| 3303   | Layout 1 | `8b8be5a5ceba`  |
| 3302   | Layout 1 | `8b8be5a5ceba`  |
| 3293   | Layout 1 | `8b8be5a5ceba`  |
| 3283   | Layout 1 | `8b8be5a5ceba`  |
| 3275   | Layout 1 | `8b8be5a5ceba`  |
| 3267   | Layout 1 | `8b8be5a5ceba`  |
| 3258   | Layout 1 | `8b8be5a5ceba`  |
| 3251   | Layout 1 | `8b8be5a5ceba`  |
| 3242   | Layout 1 | `8b8be5a5ceba`  |
| 3235   | Layout 1 | `8b8be5a5ceba`  |
| 3229   | Layout 1 | `8b8be5a5ceba`  |
| 3212   | Layout 1 | `8b8be5a5ceba`  |
| 3203   | Layout 1 | `8b8be5a5ceba`  |
| 3193   | Layout 1 | `8b8be5a5ceba`  |
| 3186   | Layout 1 | `8b8be5a5ceba`  |
| 3177   | Layout 1 | `8b8be5a5ceba`  |
| 3169   | Layout 1 | `8b8be5a5ceba`  |
| 3158   | Layout 1 | `8b8be5a5ceba`  |
| 3151   | Layout 1 | `8b8be5a5ceba`  |
| 3144   | Layout 1 | `8b8be5a5ceba`  |
| 3133   | Layout 1 | `8b8be5a5ceba`  |
| 3125   | Layout 1 | `8b8be5a5ceba`  |
| 3118   | Layout 1 | `8b8be5a5ceba`  |
| 3111   | Layout 1 | `8b8be5a5ceba`  |
| 3103   | Layout 1 | `8b8be5a5ceba`  |
| 3095   | Layout 1 | `8b8be5a5ceba`  |
| 3086   | Layout 1 | `8b8be5a5ceba`  |
| 3072   | Layout 1 | `8b8be5a5ceba`  |
| 3062   | Layout 1 | `8b8be5a5ceba`  |
| 3052   | Layout 1 | `8b8be5a5ceba`  |
| 3045   | Layout 1 | `8b8be5a5ceba`  |
| 3037   | Layout 1 | `8b8be5a5ceba`  |
| 3030   | Layout 1 | `8b8be5a5ceba`  |
| 3021   | Layout 1 | `8b8be5a5ceba`  |
| 3012   | Layout 1 | `8b8be5a5ceba`  |
| 3002   | Layout 1 | `8b8be5a5ceba`  |
| 2995   | Layout 1 | `8b8be5a5ceba`  |
| 2987   | Layout 1 | `8b8be5a5ceba`  |
| 2978   | Layout 1 | `8b8be5a5ceba`  |
| 2970   | Layout 1 | `8b8be5a5ceba`  |
| 2959   | Layout 1 | `8b8be5a5ceba`  |
| 2951   | Layout 1 | `8b8be5a5ceba`  |
| 2942   | Layout 1 | `8b8be5a5ceba`  |
| 2935   | Layout 1 | `8b8be5a5ceba`  |
| 2932   | Layout 1 | `8b8be5a5ceba`  |
| 2923   | Layout 1 | `8b8be5a5ceba`  |
| 2919   | Layout 1 | `8b8be5a5ceba`  |
| 2907   | Layout 1 | `8b8be5a5ceba`  |
| 2900   | Layout 1 | `8b8be5a5ceba`  |
| 2891   | Layout 1 | `8b8be5a5ceba`  |
| 2882   | Layout 1 | `8b8be5a5ceba`  |
| 2872   | Layout 1 | `8b8be5a5ceba`  |
| 2863   | Layout 1 | `8b8be5a5ceba`  |
| 2855   | Layout 1 | `8b8be5a5ceba`  |
| 2849   | Layout 1 | `8b8be5a5ceba`  |
| 2844   | Layout 1 | `8b8be5a5ceba`  |
| 2834   | Layout 1 | `8b8be5a5ceba`  |
| 2825   | Layout 1 | `8b8be5a5ceba`  |
| 2819   | Layout 1 | `8b8be5a5ceba`  |
| 2811   | Layout 1 | `8b8be5a5ceba`  |
| 2803   | Layout 1 | `8b8be5a5ceba`  |
| 2794   | Layout 1 | `8b8be5a5ceba`  |
| 2783   | Layout 1 | `8b8be5a5ceba`  |
| 2774   | Layout 1 | `8b8be5a5ceba`  |
| 2765   | Layout 1 | `8b8be5a5ceba`  |
| 2756   | Layout 1 | `8b8be5a5ceba`  |
| 2750   | Layout 1 | `8b8be5a5ceba`  |
| 2743   | Layout 1 | `8b8be5a5ceba`  |
| 2736   | Layout 1 | `8b8be5a5ceba`  |
| 2726   | Layout 1 | `8b8be5a5ceba`  |
| 2717   | Layout 1 | `8b8be5a5ceba`  |
| 2709   | Layout 1 | `8b8be5a5ceba`  |
| 2703   | Layout 1 | `8b8be5a5ceba`  |
| 2695   | Layout 1 | `8b8be5a5ceba`  |
| 2684   | Layout 1 | `8b8be5a5ceba`  |
| 2672   | Layout 1 | `8b8be5a5ceba`  |
| 2665   | Layout 1 | `8b8be5a5ceba`  |
| 2657   | Layout 1 | `8b8be5a5ceba`  |
| 2649   | Layout 1 | `8b8be5a5ceba`  |
| 2644   | Layout 1 | `8b8be5a5ceba`  |
| 2637   | Layout 1 | `8b8be5a5ceba`  |
| 2629   | Layout 1 | `8b8be5a5ceba`  |
| 2619   | Layout 1 | `8b8be5a5ceba`  |
| 2612   | Layout 1 | `8b8be5a5ceba`  |
| 2606   | Layout 1 | `8b8be5a5ceba`  |
| 2602   | Layout 1 | `8b8be5a5ceba`  |
| 2601   | Layout 1 | `8b8be5a5ceba`  |
| 2592   | Layout 1 | `8b8be5a5ceba`  |
| 2583   | Layout 1 | `8b8be5a5ceba`  |
| 2575   | Layout 1 | `8b8be5a5ceba`  |
| 2567   | Layout 1 | `8b8be5a5ceba`  |
| 2560   | Layout 1 | `8b8be5a5ceba`  |
| 2553   | Layout 1 | `8b8be5a5ceba`  |
| 2545   | Layout 1 | `8b8be5a5ceba`  |
| 2538   | Layout 1 | `8b8be5a5ceba`  |
| 2529   | Layout 1 | `8b8be5a5ceba`  |
| 2519   | Layout 1 | `8b8be5a5ceba`  |
| 2513   | Layout 1 | `8b8be5a5ceba`  |
| 2510   | Layout 1 | `8b8be5a5ceba`  |
| 2507   | Layout 1 | `8b8be5a5ceba`  |
| 2503   | Layout 1 | `8b8be5a5ceba`  |
| 2498   | Layout 1 | `8b8be5a5ceba`  |
| 2492   | Layout 1 | `8b8be5a5ceba`  |
| 2487   | Layout 1 | `8b8be5a5ceba`  |
| 2480   | Layout 1 | `8b8be5a5ceba`  |
| 2474   | Layout 1 | `8b8be5a5ceba`  |
| 2468   | Layout 1 | `8b8be5a5ceba`  |
| 2460   | Layout 1 | `8b8be5a5ceba`  |
| 2453   | Layout 1 | `8b8be5a5ceba`  |
| 2444   | Layout 1 | `8b8be5a5ceba`  |
| 2438   | Layout 1 | `8b8be5a5ceba`  |
| 2434   | Layout 1 | `8b8be5a5ceba`  |
| 2429   | Layout 1 | `8b8be5a5ceba`  |
| 2421   | Layout 1 | `8b8be5a5ceba`  |
| 2414   | No file  | `8b8be5a5ceba`  |
| 2407   | No file  | `8b8be5a5ceba`  |
| 2401   | No file  | `8b8be5a5ceba`  |
| 2397   | No file  | `8b8be5a5ceba`  |
| 2393   | No file  | `8b8be5a5ceba`  |
| 2384   | No file  | `8b8be5a5ceba`  |
| 2378   | No file  | `8b8be5a5ceba`  |
| 2372   | No file  | `8b8be5a5ceba`  |
| 2358   | No file  | `8b8be5a5ceba`  |
| 2352   | No file  | `8b8be5a5ceba`  |
| 2347   | No file  | `8b8be5a5ceba`  |
| 2343   | No file  | `8b8be5a5ceba`  |
| 2335   | No file  | `8b8be5a5ceba`  |
| 2327   | No file  | `8b8be5a5ceba`  |
| 2324   | No file  | `8b8be5a5ceba`  |
| 2319   | No file  | `8b8be5a5ceba`  |
| 2313   | No file  | `8b8be5a5ceba`  |
| 2308   | No file  | `8b8be5a5ceba`  |
| 2302   | No file  | `8b8be5a5ceba`  |
| 2295   | No file  | `8b8be5a5ceba`  |
| 2290   | No file  | `8b8be5a5ceba`  |
| 2284   | No file  | `8b8be5a5ceba`  |
| 2276   | No file  | `8b8be5a5ceba`  |
| 2269   | No file  | `8b8be5a5ceba`  |
| 2259   | No file  | `8b8be5a5ceba`  |
| 2250   | No file  | `8b8be5a5ceba`  |
| 2243   | No file  | `8b8be5a5ceba`  |
| 2235   | No file  | `8b8be5a5ceba`  |
| 2229   | No file  | `8b8be5a5ceba`  |
| 2224   | No file  | `8b8be5a5ceba`  |
| 2218   | No file  | `8b8be5a5ceba`  |
| 2215   | No file  | `8b8be5a5ceba`  |
| 2207   | No file  | `8b8be5a5ceba`  |
| 2203   | No file  | `8b8be5a5ceba`  |
| 2196   | No file  | `8b8be5a5ceba`  |
| 2192   | No file  | `8b8be5a5ceba`  |
| 2189   | No file  | `8b8be5a5ceba`  |
| 2183   | No file  | `8b8be5a5ceba`  |
| 2179   | No file  | `8b8be5a5ceba`  |
| 2171   | No file  | `8b8be5a5ceba`  |
| 2163   | No file  | `8b8be5a5ceba`  |
| 2156   | No file  | `8b8be5a5ceba`  |
| 2151   | No file  | `8b8be5a5ceba`  |
| 2147   | No file  | `8b8be5a5ceba`  |
| 2142   | No file  | `8b8be5a5ceba`  |
| 2138   | No file  | `8b8be5a5ceba`  |
| 2134   | No file  | `8b8be5a5ceba`  |
| 2130   | No file  | `8b8be5a5ceba`  |
| 2122   | No file  | `8b8be5a5ceba`  |
| 2107   | No file  | `8b8be5a5ceba`  |
| 2098   | No file  | `8b8be5a5ceba`  |
| 2089   | No file  | `8b8be5a5ceba`  |
| 2081   | No file  | `8b8be5a5ceba`  |
| 2073   | No file  | `8b8be5a5ceba`  |
| 2067   | No file  | `8b8be5a5ceba`  |
| 2063   | No file  | `8b8be5a5ceba`  |
| 2059   | No file  | `8b8be5a5ceba`  |
| 2052   | No file  | `8b8be5a5ceba`  |
| 2044   | No file  | `8b8be5a5ceba`  |
| 2039   | No file  | `8b8be5a5ceba`  |
| 2032   | No file  | `8b8be5a5ceba`  |
| 2025   | No file  | `8b8be5a5ceba`  |
| 2011   | No file  | `8b8be5a5ceba`  |
| 2005   | No file  | `8b8be5a5ceba`  |
| 2000   | No file  | `8b8be5a5ceba`  |
| 1996   | No file  | `8b8be5a5ceba`  |
| 1991   | No file  | `8b8be5a5ceba`  |
| 1985   | No file  | `8b8be5a5ceba`  |
| 1980   | No file  | `8b8be5a5ceba`  |
| 1969   | No file  | `8b8be5a5ceba`  |
| 1964   | No file  | `8b8be5a5ceba`  |
| 1958   | No file  | `8b8be5a5ceba`  |
| 1950   | No file  | `8b8be5a5ceba`  |
| 1945   | No file  | `8b8be5a5ceba`  |
| 1937   | No file  | `8b8be5a5ceba`  |
| 1933   | No file  | `8b8be5a5ceba`  |
| 1927   | No file  | `8b8be5a5ceba`  |
| 1921   | No file  | `8b8be5a5ceba`  |
| 1914   | No file  | `8b8be5a5ceba`  |
| 1908   | No file  | `8b8be5a5ceba`  |
| 1897   | No file  | `8b8be5a5ceba`  |
| 1892   | No file  | `8b8be5a5ceba`  |
| 1886   | No file  | `8b8be5a5ceba`  |
| 1881   | No file  | `8b8be5a5ceba`  |
| 1871   | No file  | `8b8be5a5ceba`  |
| 1866   | No file  | `8b8be5a5ceba`  |
| 1862   | No file  | `8b8be5a5ceba`  |
| 1854   | No file  | `8b8be5a5ceba`  |
| 1846   | No file  | `8b8be5a5ceba`  |
| 1838   | No file  | `8b8be5a5ceba`  |
| 1832   | No file  | `8b8be5a5ceba`  |
| 1826   | No file  | `8b8be5a5ceba`  |
| 1822   | No file  | `8b8be5a5ceba`  |
| 1818   | No file  | `8b8be5a5ceba`  |
| 1804   | No file  | `8b8be5a5ceba`  |
| 1794   | No file  | `8b8be5a5ceba`  |
| 1790   | No file  | `8b8be5a5ceba`  |
| 1784   | No file  | `8b8be5a5ceba`  |
| 1774   | No file  | `8b8be5a5ceba`  |
| 1771   | No file  | `8b8be5a5ceba`  |
| 1762   | No file  | `8b8be5a5ceba`  |
| 1759   | No file  | `8b8be5a5ceba`  |
| 1754   | No file  | `8b8be5a5ceba`  |
| 1749   | No file  | `8b8be5a5ceba`  |
| 1743   | No file  | `8b8be5a5ceba`  |
| 1737   | No file  | `8b8be5a5ceba`  |
| 1731   | No file  | `8b8be5a5ceba`  |
| 1725   | No file  | `8b8be5a5ceba`  |
| 1717   | No file  | `8b8be5a5ceba`  |
| 1710   | No file  | `8b8be5a5ceba`  |
| 1704   | No file  | `8b8be5a5ceba`  |
| 1698   | No file  | `8b8be5a5ceba`  |
| 1690   | No file  | `8b8be5a5ceba`  |
| 1685   | No file  | `8b8be5a5ceba`  |
| 1680   | No file  | `8b8be5a5ceba`  |
| 1674   | No file  | `8b8be5a5ceba`  |
| 1668   | No file  | `8b8be5a5ceba`  |
| 1659   | No file  | `8b8be5a5ceba`  |
| 1649   | No file  | `8b8be5a5ceba`  |
| 1642   | No file  | `8b8be5a5ceba`  |
| 1636   | No file  | `8b8be5a5ceba`  |
| 1628   | No file  | `8b8be5a5ceba`  |
| 1622   | No file  | `8b8be5a5ceba`  |
| 1614   | No file  | `8b8be5a5ceba`  |
| 1608   | No file  | `8b8be5a5ceba`  |
| 1602   | No file  | `8b8be5a5ceba`  |
| 1598   | No file  | `8b8be5a5ceba`  |
| 1594   | No file  | `8b8be5a5ceba`  |
| 1590   | No file  | `8b8be5a5ceba`  |
| 1587   | No file  | `8b8be5a5ceba`  |
| 1584   | No file  | `8b8be5a5ceba`  |
| 1579   | No file  | `8b8be5a5ceba`  |
| 1572   | No file  | `8b8be5a5ceba`  |
| 1565   | No file  | `8b8be5a5ceba`  |
| 1559   | No file  | `8b8be5a5ceba`  |
| 1554   | No file  | `8b8be5a5ceba`  |
| 1547   | No file  | `8b8be5a5ceba`  |
| 1537   | No file  | `8b8be5a5ceba`  |
| 1529   | No file  | `8b8be5a5ceba`  |
| 1524   | No file  | `8b8be5a5ceba`  |
| 1519   | No file  | `8b8be5a5ceba`  |
| 1509   | No file  | `8b8be5a5ceba`  |
| 1506   | No file  | `8b8be5a5ceba`  |
| 1504   | No file  | `8b8be5a5ceba`  |
| 1500   | No file  | `8b8be5a5ceba`  |
| 1493   | No file  | `8b8be5a5ceba`  |
| 1489   | No file  | `8b8be5a5ceba`  |
| 1485   | No file  | `8b8be5a5ceba`  |
| 1481   | No file  | `8b8be5a5ceba`  |
| 1474   | No file  | `8b8be5a5ceba`  |
| 1466   | No file  | `8b8be5a5ceba`  |
| 1462   | No file  | `8b8be5a5ceba`  |
| 1459   | No file  | `8b8be5a5ceba`  |
| 1453   | No file  | `8b8be5a5ceba`  |
| 1450   | No file  | `8b8be5a5ceba`  |
| 1445   | No file  | `8b8be5a5ceba`  |
| 1439   | No file  | `8b8be5a5ceba`  |
| 1433   | No file  | `8b8be5a5ceba`  |
| 1430   | No file  | `8b8be5a5ceba`  |
| 1426   | No file  | `8b8be5a5ceba`  |
| 1421   | No file  | `8b8be5a5ceba`  |
| 1417   | No file  | `8b8be5a5ceba`  |
| 1416   | No file  | `8b8be5a5ceba`  |
| 1409   | No file  | `8b8be5a5ceba`  |
| 1405   | No file  | `8b8be5a5ceba`  |
| 1401   | No file  | `8b8be5a5ceba`  |
| 1396   | No file  | `8b8be5a5ceba`  |
| 1391   | No file  | `8b8be5a5ceba`  |
| 1390   | No file  | `8b8be5a5ceba`  |
| 1386   | No file  | `8b8be5a5ceba`  |
| 1381   | No file  | `8b8be5a5ceba`  |
| 1379   | No file  | `8b8be5a5ceba`  |
| 1372   | No file  | `8b8be5a5ceba`  |
| 1366   | No file  | `8b8be5a5ceba`  |
| 1364   | No file  | `8b8be5a5ceba`  |
| 1363   | No file  | `8b8be5a5ceba`  |
| 1360   | No file  | `8b8be5a5ceba`  |
| 1358   | No file  | `8b8be5a5ceba`  |
| 1355   | No file  | `8b8be5a5ceba`  |
| 1351   | No file  | `8b8be5a5ceba`  |
| 1348   | No file  | `8b8be5a5ceba`  |
| 1346   | No file  | `8b8be5a5ceba`  |
| 1341   | No file  | `8b8be5a5ceba`  |
| 1340   | No file  | `8b8be5a5ceba`  |
| 1338   | No file  | `8b8be5a5ceba`  |
| 1335   | No file  | `8b8be5a5ceba`  |
| 1333   | No file  | `8b8be5a5ceba`  |
| 1329   | No file  | `8b8be5a5ceba`  |
| 1327   | No file  | `8b8be5a5ceba`  |
| 1324   | No file  | `8b8be5a5ceba`  |
| 1321   | No file  | `8b8be5a5ceba`  |
| 1319   | No file  | `8b8be5a5ceba`  |
| 1318   | No file  | `8b8be5a5ceba`  |
| 1316   | No file  | `8b8be5a5ceba`  |
| 1313   | No file  | `8b8be5a5ceba`  |
| 1311   | No file  | `8b8be5a5ceba`  |
| 1309   | No file  | `8b8be5a5ceba`  |
| 1304   | No file  | `8b8be5a5ceba`  |
| 1292   | No file  | `8b8be5a5ceba`  |
| 1286   | No file  | `8b8be5a5ceba`  |
| 1280   | No file  | `8b8be5a5ceba`  |
| 1276   | No file  | `8b8be5a5ceba`  |
| 1267   | No file  | `8b8be5a5ceba`  |
| 1261   | No file  | `8b8be5a5ceba`  |
| 1256   | No file  | `8b8be5a5ceba`  |
| 1250   | No file  | `8b8be5a5ceba`  |
| 1246   | No file  | `8b8be5a5ceba`  |
| 1239   | No file  | `8b8be5a5ceba`  |
| 1230   | No file  | `8b8be5a5ceba`  |
| 1226   | No file  | `8b8be5a5ceba`  |
| 1220   | No file  | `8b8be5a5ceba`  |
| 1217   | No file  | `8b8be5a5ceba`  |
| 1211   | No file  | `8b8be5a5ceba`  |
| 1210   | No file  | `8b8be5a5ceba`  |
| 1208   | No file  | `8b8be5a5ceba`  |
| 1203   | No file  | `8b8be5a5ceba`  |
| 1197   | No file  | `8b8be5a5ceba`  |
| 1194   | No file  | `8b8be5a5ceba`  |
| 1192   | No file  | `8b8be5a5ceba`  |
| 1187   | No file  | `8b8be5a5ceba`  |
| 1183   | No file  | `8b8be5a5ceba`  |
| 1177   | No file  | `8b8be5a5ceba`  |
| 1173   | No file  | `8b8be5a5ceba`  |
| 1167   | No file  | `8b8be5a5ceba`  |
| 1164   | No file  | `8b8be5a5ceba`  |
| 1156   | No file  | `8b8be5a5ceba`  |
| 1149   | No file  | `8b8be5a5ceba`  |
| 1144   | No file  | `8b8be5a5ceba`  |
| 1137   | No file  | `8b8be5a5ceba`  |
| 1132   | No file  | `8b8be5a5ceba`  |
| 1127   | No file  | `8b8be5a5ceba`  |
| 1122   | No file  | `8b8be5a5ceba`  |
| 1118   | No file  | `8b8be5a5ceba`  |
| 1114   | No file  | `8b8be5a5ceba`  |
| 1109   | No file  | `8b8be5a5ceba`  |
| 1102   | No file  | `8b8be5a5ceba`  |
| 1096   | No file  | `8b8be5a5ceba`  |
| 1088   | No file  | `8b8be5a5ceba`  |
| 1081   | No file  | `8b8be5a5ceba`  |
| 1076   | No file  | `8b8be5a5ceba`  |
| 1069   | No file  | `8b8be5a5ceba`  |
| 1064   | No file  | `8b8be5a5ceba`  |
| 1058   | No file  | `8b8be5a5ceba`  |
| 1051   | No file  | `8b8be5a5ceba`  |
| 1044   | No file  | `8b8be5a5ceba`  |
| 1036   | No file  | `8b8be5a5ceba`  |
| 1026   | No file  | `8b8be5a5ceba`  |
| 1016   | No file  | `8b8be5a5ceba`  |
| 1009   | No file  | `8b8be5a5ceba`  |
| 1005   | No file  | `8b8be5a5ceba`  |
| 1000   | No file  | `8b8be5a5ceba`  |
| 998    | No file  | `8b8be5a5ceba`  |
| 990    | No file  | `8b8be5a5ceba`  |
| 979    | No file  | `8b8be5a5ceba`  |
| 972    | No file  | `8b8be5a5ceba`  |
| 963    | No file  | `8b8be5a5ceba`  |
| 955    | No file  | `8b8be5a5ceba`  |
| 946    | No file  | `8b8be5a5ceba`  |
| 938    | No file  | `8b8be5a5ceba`  |
| 927    | No file  | `8b8be5a5ceba`  |
| 911    | No file  | `8b8be5a5ceba`  |
| 904    | No file  | `8b8be5a5ceba`  |
| 899    | No file  | `8b8be5a5ceba`  |
| 894    | No file  | `8b8be5a5ceba`  |
| 885    | No file  | `8b8be5a5ceba`  |
| 879    | No file  | `8b8be5a5ceba`  |
| 872    | No file  | `8b8be5a5ceba`  |
| 864    | No file  | `8b8be5a5ceba`  |
| 855    | No file  | `8b8be5a5ceba`  |
| 853    | No file  | `8b8be5a5ceba`  |
| 845    | No file  | `8b8be5a5ceba`  |
| 837    | No file  | `8b8be5a5ceba`  |
| 829    | No file  | `8b8be5a5ceba`  |
| 822    | No file  | `8b8be5a5ceba`  |
| 814    | No file  | `8b8be5a5ceba`  |
| 805    | No file  | `8b8be5a5ceba`  |
| 794    | No file  | `8b8be5a5ceba`  |
| 787    | No file  | `8b8be5a5ceba`  |
| 780    | No file  | `8b8be5a5ceba`  |
| 771    | No file  | `8b8be5a5ceba`  |
| 760    | No file  | `8b8be5a5ceba`  |
| 748    | No file  | `8b8be5a5ceba`  |
| 741    | No file  | `8b8be5a5ceba`  |
| 736    | No file  | `8b8be5a5ceba`  |
| 731    | No file  | `8b8be5a5ceba`  |
| 723    | No file  | `8b8be5a5ceba`  |
| 711    | No file  | `8b8be5a5ceba`  |
| 707    | No file  | `8b8be5a5ceba`  |
| 697    | No file  | `8b8be5a5ceba`  |
| 689    | No file  | `8b8be5a5ceba`  |
| 683    | No file  | `8b8be5a5ceba`  |
| 678    | No file  | `8b8be5a5ceba`  |
| 670    | No file  | `8b8be5a5ceba`  |
| 661    | No file  | `8b8be5a5ceba`  |
| 656    | No file  | `8b8be5a5ceba`  |
| 652    | No file  | `8b8be5a5ceba`  |
| 643    | No file  | `8b8be5a5ceba`  |
| 637    | No file  | `8b8be5a5ceba`  |
| 630    | No file  | `8b8be5a5ceba`  |
| 627    | No file  | `8b8be5a5ceba`  |
| 621    | No file  | `8b8be5a5ceba`  |
| 617    | No file  | `8b8be5a5ceba`  |
| 615    | No file  | `8b8be5a5ceba`  |
| 606    | No file  | `8b8be5a5ceba`  |
| 599    | No file  | `8b8be5a5ceba`  |
| 592    | No file  | `8b8be5a5ceba`  |
| 586    | No file  | `8b8be5a5ceba`  |
| 577    | No file  | `8b8be5a5ceba`  |
| 569    | No file  | `8b8be5a5ceba`  |
| 561    | No file  | `8b8be5a5ceba`  |
| 554    | No file  | `8b8be5a5ceba`  |
| 542    | No file  | `8b8be5a5ceba`  |
| 532    | No file  | `8b8be5a5ceba`  |
| 531    | No file  | `8b8be5a5ceba`  |
| 526    | No file  | `8b8be5a5ceba`  |
| 521    | No file  | `8b8be5a5ceba`  |
| 517    | No file  | `8b8be5a5ceba`  |
| 510    | No file  | `8b8be5a5ceba`  |
| 508    | No file  | `8b8be5a5ceba`  |
| 504    | No file  | `8b8be5a5ceba`  |
| 497    | No file  | `8b8be5a5ceba`  |
| 491    | No file  | `8b8be5a5ceba`  |
| 485    | No file  | `8b8be5a5ceba`  |
| 478    | No file  | `8b8be5a5ceba`  |
| 472    | No file  | `8b8be5a5ceba`  |
| 466    | No file  | `8b8be5a5ceba`  |
| 457    | No file  | `8b8be5a5ceba`  |
| 452    | No file  | `8b8be5a5ceba`  |
| 449    | No file  | `8b8be5a5ceba`  |
| 435    | No file  | `8b8be5a5ceba`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                                      |
| ------------------- | ------------ | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32          | unknown_04   | `1` on client 2519, `5000000` on clients 3002 to 3474      |
| `+0x08`             | u32          | unknown_08   | `0` on every client checked                                |
| `+0x0C`             | String Table | string_table | See String Table                                           |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x0C` on every client checked |
| `string_table+0x04` | u32          | zero         | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 40 4B 4C 00 00 00 00 00 00 00 00 00 0C 00 00 00 00 00 00 00`
  (24 bytes).
- The file is not in the archives of clients 1784 and 2107.
- The two u32 fields are a reading of the bytes. `unknown_08` is `0` on
  every client checked, so its width is not shown by the data.
- The `InstanceCommonOption` and `InstanceCamoDisableOption` sheets of a
  private server's `DataSheets.bexcel` on client 1784 start with
  `InstanceType` and `InstanceMode`; that client has no
  `instanceetcoption.bss`, so neither sheet can be matched.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. With no
  confirmed field, the preview shows the raw value bytes.

## Open Questions

### Instance Option Values

`unknown_04` changed from `1` (client 2519) to `5000000` (client 3002 and
later). No client Lua function on client 3474 has `InstanceEtc` in its name,
and no sheet or loader on client 1784 has `EtcOption` for instances (the
`EtcOption` sheet there is the general option sheet, with house auction,
trade and worker columns). What the two values limit or price is unknown.
