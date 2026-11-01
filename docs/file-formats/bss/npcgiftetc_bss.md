# `npcgiftetc.bss` Format

## Purpose

The global values of the NPC gift and confession system: the Energy cost of a gift and of a confession, the lowest amity for a confession and the highest item price a gift may have. The file is one fixed-size `PABR` block with no row count or companion offset table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------- | ----- | ------- | --------- |
| 1      | 1246 and later | `npcgiftetc.bss` | 32    | -       | -         |

| Layout | File             | Known        | Unknown      |
| ------ | ---------------- | ------------ | ------------ |
| 1      | `npcgiftetc.bss` | 20 B (62.5%) | 12 B (37.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `dffef84dae8f`  |
| 3482   | Layout 1 | `dffef84dae8f`  |
| 3474   | Layout 1 | `dffef84dae8f`  |
| 3473   | Layout 1 | `dffef84dae8f`  |
| 3464   | Layout 1 | `dffef84dae8f`  |
| 3458   | Layout 1 | `dffef84dae8f`  |
| 3454   | Layout 1 | `dffef84dae8f`  |
| 3444   | Layout 1 | `dffef84dae8f`  |
| 3435   | Layout 1 | `dffef84dae8f`  |
| 3426   | Layout 1 | `dffef84dae8f`  |
| 3418   | Layout 1 | `dffef84dae8f`  |
| 3412   | Layout 1 | `dffef84dae8f`  |
| 3402   | Layout 1 | `dffef84dae8f`  |
| 3396   | Layout 1 | `dffef84dae8f`  |
| 3387   | Layout 1 | `dffef84dae8f`  |
| 3381   | Layout 1 | `dffef84dae8f`  |
| 3373   | Layout 1 | `dffef84dae8f`  |
| 3364   | Layout 1 | `dffef84dae8f`  |
| 3356   | Layout 1 | `dffef84dae8f`  |
| 3349   | Layout 1 | `dffef84dae8f`  |
| 3342   | Layout 1 | `dffef84dae8f`  |
| 3335   | Layout 1 | `dffef84dae8f`  |
| 3326   | Layout 1 | `dffef84dae8f`  |
| 3321   | Layout 1 | `dffef84dae8f`  |
| 3314   | Layout 1 | `dffef84dae8f`  |
| 3303   | Layout 1 | `dffef84dae8f`  |
| 3302   | Layout 1 | `dffef84dae8f`  |
| 3293   | Layout 1 | `dffef84dae8f`  |
| 3283   | Layout 1 | `dffef84dae8f`  |
| 3275   | Layout 1 | `dffef84dae8f`  |
| 3267   | Layout 1 | `dffef84dae8f`  |
| 3258   | Layout 1 | `dffef84dae8f`  |
| 3251   | Layout 1 | `dffef84dae8f`  |
| 3242   | Layout 1 | `dffef84dae8f`  |
| 3235   | Layout 1 | `dffef84dae8f`  |
| 3229   | Layout 1 | `dffef84dae8f`  |
| 3212   | Layout 1 | `dffef84dae8f`  |
| 3203   | Layout 1 | `dffef84dae8f`  |
| 3193   | Layout 1 | `dffef84dae8f`  |
| 3186   | Layout 1 | `dffef84dae8f`  |
| 3177   | Layout 1 | `dffef84dae8f`  |
| 3169   | Layout 1 | `dffef84dae8f`  |
| 3158   | Layout 1 | `dffef84dae8f`  |
| 3151   | Layout 1 | `dffef84dae8f`  |
| 3144   | Layout 1 | `dffef84dae8f`  |
| 3133   | Layout 1 | `dffef84dae8f`  |
| 3125   | Layout 1 | `dffef84dae8f`  |
| 3118   | Layout 1 | `dffef84dae8f`  |
| 3111   | Layout 1 | `dffef84dae8f`  |
| 3103   | Layout 1 | `dffef84dae8f`  |
| 3095   | Layout 1 | `dffef84dae8f`  |
| 3086   | Layout 1 | `dffef84dae8f`  |
| 3072   | Layout 1 | `dffef84dae8f`  |
| 3062   | Layout 1 | `dffef84dae8f`  |
| 3052   | Layout 1 | `dffef84dae8f`  |
| 3045   | Layout 1 | `dffef84dae8f`  |
| 3037   | Layout 1 | `dffef84dae8f`  |
| 3030   | Layout 1 | `dffef84dae8f`  |
| 3021   | Layout 1 | `dffef84dae8f`  |
| 3012   | Layout 1 | `dffef84dae8f`  |
| 3002   | Layout 1 | `dffef84dae8f`  |
| 2995   | Layout 1 | `dffef84dae8f`  |
| 2987   | Layout 1 | `dffef84dae8f`  |
| 2978   | Layout 1 | `dffef84dae8f`  |
| 2970   | Layout 1 | `dffef84dae8f`  |
| 2959   | Layout 1 | `dffef84dae8f`  |
| 2951   | Layout 1 | `dffef84dae8f`  |
| 2942   | Layout 1 | `dffef84dae8f`  |
| 2935   | Layout 1 | `dffef84dae8f`  |
| 2932   | Layout 1 | `dffef84dae8f`  |
| 2923   | Layout 1 | `dffef84dae8f`  |
| 2919   | Layout 1 | `dffef84dae8f`  |
| 2907   | Layout 1 | `dffef84dae8f`  |
| 2900   | Layout 1 | `dffef84dae8f`  |
| 2891   | Layout 1 | `dffef84dae8f`  |
| 2882   | Layout 1 | `dffef84dae8f`  |
| 2872   | Layout 1 | `dffef84dae8f`  |
| 2863   | Layout 1 | `dffef84dae8f`  |
| 2855   | Layout 1 | `dffef84dae8f`  |
| 2849   | Layout 1 | `dffef84dae8f`  |
| 2844   | Layout 1 | `dffef84dae8f`  |
| 2834   | Layout 1 | `dffef84dae8f`  |
| 2825   | Layout 1 | `dffef84dae8f`  |
| 2819   | Layout 1 | `dffef84dae8f`  |
| 2811   | Layout 1 | `dffef84dae8f`  |
| 2803   | Layout 1 | `dffef84dae8f`  |
| 2794   | Layout 1 | `dffef84dae8f`  |
| 2783   | Layout 1 | `dffef84dae8f`  |
| 2774   | Layout 1 | `dffef84dae8f`  |
| 2765   | Layout 1 | `dffef84dae8f`  |
| 2756   | Layout 1 | `dffef84dae8f`  |
| 2750   | Layout 1 | `dffef84dae8f`  |
| 2743   | Layout 1 | `dffef84dae8f`  |
| 2736   | Layout 1 | `dffef84dae8f`  |
| 2726   | Layout 1 | `dffef84dae8f`  |
| 2717   | Layout 1 | `dffef84dae8f`  |
| 2709   | Layout 1 | `dffef84dae8f`  |
| 2703   | Layout 1 | `dffef84dae8f`  |
| 2695   | Layout 1 | `dffef84dae8f`  |
| 2684   | Layout 1 | `dffef84dae8f`  |
| 2672   | Layout 1 | `dffef84dae8f`  |
| 2665   | Layout 1 | `dffef84dae8f`  |
| 2657   | Layout 1 | `dffef84dae8f`  |
| 2649   | Layout 1 | `dffef84dae8f`  |
| 2644   | Layout 1 | `dffef84dae8f`  |
| 2637   | Layout 1 | `dffef84dae8f`  |
| 2629   | Layout 1 | `dffef84dae8f`  |
| 2619   | Layout 1 | `dffef84dae8f`  |
| 2612   | Layout 1 | `dffef84dae8f`  |
| 2606   | Layout 1 | `dffef84dae8f`  |
| 2602   | Layout 1 | `dffef84dae8f`  |
| 2601   | Layout 1 | `dffef84dae8f`  |
| 2592   | Layout 1 | `dffef84dae8f`  |
| 2583   | Layout 1 | `dffef84dae8f`  |
| 2575   | Layout 1 | `dffef84dae8f`  |
| 2567   | Layout 1 | `dffef84dae8f`  |
| 2560   | Layout 1 | `dffef84dae8f`  |
| 2553   | Layout 1 | `dffef84dae8f`  |
| 2545   | Layout 1 | `dffef84dae8f`  |
| 2538   | Layout 1 | `dffef84dae8f`  |
| 2529   | Layout 1 | `dffef84dae8f`  |
| 2519   | Layout 1 | `dffef84dae8f`  |
| 2513   | Layout 1 | `dffef84dae8f`  |
| 2510   | Layout 1 | `dffef84dae8f`  |
| 2507   | Layout 1 | `dffef84dae8f`  |
| 2503   | Layout 1 | `dffef84dae8f`  |
| 2498   | Layout 1 | `dffef84dae8f`  |
| 2492   | Layout 1 | `dffef84dae8f`  |
| 2487   | Layout 1 | `dffef84dae8f`  |
| 2480   | Layout 1 | `dffef84dae8f`  |
| 2474   | Layout 1 | `dffef84dae8f`  |
| 2468   | Layout 1 | `dffef84dae8f`  |
| 2460   | Layout 1 | `dffef84dae8f`  |
| 2453   | Layout 1 | `dffef84dae8f`  |
| 2444   | Layout 1 | `dffef84dae8f`  |
| 2438   | Layout 1 | `dffef84dae8f`  |
| 2434   | Layout 1 | `dffef84dae8f`  |
| 2429   | Layout 1 | `dffef84dae8f`  |
| 2421   | Layout 1 | `dffef84dae8f`  |
| 2414   | Layout 1 | `dffef84dae8f`  |
| 2407   | Layout 1 | `dffef84dae8f`  |
| 2401   | Layout 1 | `dffef84dae8f`  |
| 2397   | Layout 1 | `dffef84dae8f`  |
| 2393   | Layout 1 | `dffef84dae8f`  |
| 2384   | Layout 1 | `dffef84dae8f`  |
| 2378   | Layout 1 | `dffef84dae8f`  |
| 2372   | Layout 1 | `dffef84dae8f`  |
| 2358   | Layout 1 | `dffef84dae8f`  |
| 2352   | Layout 1 | `dffef84dae8f`  |
| 2347   | Layout 1 | `dffef84dae8f`  |
| 2343   | Layout 1 | `dffef84dae8f`  |
| 2335   | Layout 1 | `dffef84dae8f`  |
| 2327   | Layout 1 | `dffef84dae8f`  |
| 2324   | Layout 1 | `dffef84dae8f`  |
| 2319   | Layout 1 | `dffef84dae8f`  |
| 2313   | Layout 1 | `dffef84dae8f`  |
| 2308   | Layout 1 | `dffef84dae8f`  |
| 2302   | Layout 1 | `dffef84dae8f`  |
| 2295   | Layout 1 | `dffef84dae8f`  |
| 2290   | Layout 1 | `dffef84dae8f`  |
| 2284   | Layout 1 | `dffef84dae8f`  |
| 2276   | Layout 1 | `dffef84dae8f`  |
| 2269   | Layout 1 | `dffef84dae8f`  |
| 2259   | Layout 1 | `dffef84dae8f`  |
| 2250   | Layout 1 | `dffef84dae8f`  |
| 2243   | Layout 1 | `dffef84dae8f`  |
| 2235   | Layout 1 | `dffef84dae8f`  |
| 2229   | Layout 1 | `dffef84dae8f`  |
| 2224   | Layout 1 | `dffef84dae8f`  |
| 2218   | Layout 1 | `dffef84dae8f`  |
| 2215   | Layout 1 | `dffef84dae8f`  |
| 2207   | Layout 1 | `dffef84dae8f`  |
| 2203   | Layout 1 | `dffef84dae8f`  |
| 2196   | Layout 1 | `dffef84dae8f`  |
| 2192   | Layout 1 | `dffef84dae8f`  |
| 2189   | Layout 1 | `dffef84dae8f`  |
| 2183   | Layout 1 | `dffef84dae8f`  |
| 2179   | Layout 1 | `dffef84dae8f`  |
| 2171   | Layout 1 | `dffef84dae8f`  |
| 2163   | Layout 1 | `dffef84dae8f`  |
| 2156   | Layout 1 | `dffef84dae8f`  |
| 2151   | Layout 1 | `dffef84dae8f`  |
| 2147   | Layout 1 | `dffef84dae8f`  |
| 2142   | Layout 1 | `dffef84dae8f`  |
| 2138   | Layout 1 | `dffef84dae8f`  |
| 2134   | Layout 1 | `dffef84dae8f`  |
| 2130   | Layout 1 | `dffef84dae8f`  |
| 2122   | Layout 1 | `dffef84dae8f`  |
| 2107   | Layout 1 | `dffef84dae8f`  |
| 2098   | Layout 1 | `dffef84dae8f`  |
| 2089   | Layout 1 | `dffef84dae8f`  |
| 2081   | Layout 1 | `dffef84dae8f`  |
| 2073   | Layout 1 | `dffef84dae8f`  |
| 2067   | Layout 1 | `dffef84dae8f`  |
| 2063   | Layout 1 | `dffef84dae8f`  |
| 2059   | Layout 1 | `dffef84dae8f`  |
| 2052   | Layout 1 | `dffef84dae8f`  |
| 2044   | Layout 1 | `dffef84dae8f`  |
| 2039   | Layout 1 | `dffef84dae8f`  |
| 2032   | Layout 1 | `dffef84dae8f`  |
| 2025   | Layout 1 | `dffef84dae8f`  |
| 2011   | Layout 1 | `dffef84dae8f`  |
| 2005   | Layout 1 | `dffef84dae8f`  |
| 2000   | Layout 1 | `dffef84dae8f`  |
| 1996   | Layout 1 | `dffef84dae8f`  |
| 1991   | Layout 1 | `dffef84dae8f`  |
| 1985   | Layout 1 | `dffef84dae8f`  |
| 1980   | Layout 1 | `dffef84dae8f`  |
| 1969   | Layout 1 | `dffef84dae8f`  |
| 1964   | Layout 1 | `dffef84dae8f`  |
| 1958   | Layout 1 | `dffef84dae8f`  |
| 1950   | Layout 1 | `dffef84dae8f`  |
| 1945   | Layout 1 | `dffef84dae8f`  |
| 1937   | Layout 1 | `dffef84dae8f`  |
| 1933   | Layout 1 | `dffef84dae8f`  |
| 1927   | Layout 1 | `dffef84dae8f`  |
| 1921   | Layout 1 | `dffef84dae8f`  |
| 1914   | Layout 1 | `dffef84dae8f`  |
| 1908   | Layout 1 | `dffef84dae8f`  |
| 1897   | Layout 1 | `dffef84dae8f`  |
| 1892   | Layout 1 | `dffef84dae8f`  |
| 1886   | Layout 1 | `dffef84dae8f`  |
| 1881   | Layout 1 | `dffef84dae8f`  |
| 1871   | Layout 1 | `dffef84dae8f`  |
| 1866   | Layout 1 | `dffef84dae8f`  |
| 1862   | Layout 1 | `dffef84dae8f`  |
| 1854   | Layout 1 | `dffef84dae8f`  |
| 1846   | Layout 1 | `dffef84dae8f`  |
| 1838   | Layout 1 | `dffef84dae8f`  |
| 1832   | Layout 1 | `dffef84dae8f`  |
| 1826   | Layout 1 | `dffef84dae8f`  |
| 1822   | Layout 1 | `dffef84dae8f`  |
| 1818   | Layout 1 | `dffef84dae8f`  |
| 1804   | Layout 1 | `dffef84dae8f`  |
| 1794   | Layout 1 | `dffef84dae8f`  |
| 1790   | Layout 1 | `dffef84dae8f`  |
| 1784   | Layout 1 | `dffef84dae8f`  |
| 1774   | Layout 1 | `dffef84dae8f`  |
| 1771   | Layout 1 | `dffef84dae8f`  |
| 1762   | Layout 1 | `dffef84dae8f`  |
| 1759   | Layout 1 | `dffef84dae8f`  |
| 1754   | Layout 1 | `dffef84dae8f`  |
| 1749   | Layout 1 | `dffef84dae8f`  |
| 1743   | Layout 1 | `dffef84dae8f`  |
| 1737   | Layout 1 | `dffef84dae8f`  |
| 1731   | Layout 1 | `dffef84dae8f`  |
| 1725   | Layout 1 | `dffef84dae8f`  |
| 1717   | Layout 1 | `dffef84dae8f`  |
| 1710   | Layout 1 | `dffef84dae8f`  |
| 1704   | Layout 1 | `dffef84dae8f`  |
| 1698   | Layout 1 | `dffef84dae8f`  |
| 1690   | Layout 1 | `dffef84dae8f`  |
| 1685   | Layout 1 | `dffef84dae8f`  |
| 1680   | Layout 1 | `dffef84dae8f`  |
| 1674   | Layout 1 | `dffef84dae8f`  |
| 1668   | Layout 1 | `dffef84dae8f`  |
| 1659   | Layout 1 | `dffef84dae8f`  |
| 1649   | Layout 1 | `dffef84dae8f`  |
| 1642   | Layout 1 | `dffef84dae8f`  |
| 1636   | Layout 1 | `dffef84dae8f`  |
| 1628   | Layout 1 | `dffef84dae8f`  |
| 1622   | Layout 1 | `dffef84dae8f`  |
| 1614   | Layout 1 | `dffef84dae8f`  |
| 1608   | Layout 1 | `dffef84dae8f`  |
| 1602   | Layout 1 | `dffef84dae8f`  |
| 1598   | Layout 1 | `dffef84dae8f`  |
| 1594   | Layout 1 | `dffef84dae8f`  |
| 1590   | Layout 1 | `dffef84dae8f`  |
| 1587   | Layout 1 | `dffef84dae8f`  |
| 1584   | Layout 1 | `dffef84dae8f`  |
| 1579   | Layout 1 | `dffef84dae8f`  |
| 1572   | Layout 1 | `dffef84dae8f`  |
| 1565   | Layout 1 | `dffef84dae8f`  |
| 1559   | Layout 1 | `dffef84dae8f`  |
| 1554   | Layout 1 | `dffef84dae8f`  |
| 1547   | Layout 1 | `dffef84dae8f`  |
| 1537   | Layout 1 | `dffef84dae8f`  |
| 1529   | Layout 1 | `dffef84dae8f`  |
| 1524   | Layout 1 | `dffef84dae8f`  |
| 1519   | Layout 1 | `dffef84dae8f`  |
| 1509   | Layout 1 | `dffef84dae8f`  |
| 1506   | Layout 1 | `dffef84dae8f`  |
| 1504   | Layout 1 | `dffef84dae8f`  |
| 1500   | Layout 1 | `dffef84dae8f`  |
| 1493   | Layout 1 | `dffef84dae8f`  |
| 1489   | Layout 1 | `dffef84dae8f`  |
| 1485   | Layout 1 | `dffef84dae8f`  |
| 1481   | Layout 1 | `dffef84dae8f`  |
| 1474   | Layout 1 | `dffef84dae8f`  |
| 1466   | Layout 1 | `dffef84dae8f`  |
| 1462   | Layout 1 | `dffef84dae8f`  |
| 1459   | Layout 1 | `dffef84dae8f`  |
| 1453   | Layout 1 | `dffef84dae8f`  |
| 1450   | Layout 1 | `dffef84dae8f`  |
| 1445   | Layout 1 | `dffef84dae8f`  |
| 1439   | Layout 1 | `dffef84dae8f`  |
| 1433   | Layout 1 | `dffef84dae8f`  |
| 1430   | Layout 1 | `dffef84dae8f`  |
| 1426   | Layout 1 | `dffef84dae8f`  |
| 1421   | Layout 1 | `dffef84dae8f`  |
| 1417   | Layout 1 | `dffef84dae8f`  |
| 1416   | Layout 1 | `dffef84dae8f`  |
| 1409   | Layout 1 | `dffef84dae8f`  |
| 1405   | Layout 1 | `dffef84dae8f`  |
| 1401   | Layout 1 | `dffef84dae8f`  |
| 1396   | Layout 1 | `dffef84dae8f`  |
| 1391   | Layout 1 | `dffef84dae8f`  |
| 1390   | Layout 1 | `dffef84dae8f`  |
| 1386   | Layout 1 | `dffef84dae8f`  |
| 1381   | Layout 1 | `dffef84dae8f`  |
| 1379   | Layout 1 | `dffef84dae8f`  |
| 1372   | Layout 1 | `dffef84dae8f`  |
| 1366   | Layout 1 | `dffef84dae8f`  |
| 1364   | Layout 1 | `dffef84dae8f`  |
| 1363   | Layout 1 | `dffef84dae8f`  |
| 1360   | Layout 1 | `dffef84dae8f`  |
| 1358   | Layout 1 | `dffef84dae8f`  |
| 1355   | Layout 1 | `dffef84dae8f`  |
| 1351   | Layout 1 | `dffef84dae8f`  |
| 1348   | Layout 1 | `dffef84dae8f`  |
| 1346   | Layout 1 | `dffef84dae8f`  |
| 1341   | Layout 1 | `dffef84dae8f`  |
| 1340   | Layout 1 | `dffef84dae8f`  |
| 1338   | Layout 1 | `dffef84dae8f`  |
| 1335   | Layout 1 | `dffef84dae8f`  |
| 1333   | Layout 1 | `dffef84dae8f`  |
| 1329   | Layout 1 | `dffef84dae8f`  |
| 1327   | Layout 1 | `dffef84dae8f`  |
| 1324   | Layout 1 | `dffef84dae8f`  |
| 1321   | Layout 1 | `dffef84dae8f`  |
| 1319   | Layout 1 | `dffef84dae8f`  |
| 1318   | Layout 1 | `dffef84dae8f`  |
| 1316   | Layout 1 | `dffef84dae8f`  |
| 1313   | Layout 1 | `dffef84dae8f`  |
| 1311   | Layout 1 | `dffef84dae8f`  |
| 1309   | Layout 1 | `dffef84dae8f`  |
| 1304   | Layout 1 | `dffef84dae8f`  |
| 1292   | Layout 1 | `dffef84dae8f`  |
| 1286   | Layout 1 | `dffef84dae8f`  |
| 1280   | Layout 1 | `dffef84dae8f`  |
| 1276   | Layout 1 | `dffef84dae8f`  |
| 1267   | Layout 1 | `dffef84dae8f`  |
| 1261   | Layout 1 | `dffef84dae8f`  |
| 1256   | Layout 1 | `dffef84dae8f`  |
| 1250   | Layout 1 | `dffef84dae8f`  |
| 1246   | Layout 1 | `dffef84dae8f`  |
| 1239   | No file  | `dffef84dae8f`  |
| 1230   | No file  | `dffef84dae8f`  |
| 1226   | No file  | `dffef84dae8f`  |
| 1220   | No file  | `dffef84dae8f`  |
| 1217   | No file  | `dffef84dae8f`  |
| 1211   | No file  | `dffef84dae8f`  |
| 1210   | No file  | `dffef84dae8f`  |
| 1208   | No file  | `dffef84dae8f`  |
| 1203   | No file  | `dffef84dae8f`  |
| 1197   | No file  | `dffef84dae8f`  |
| 1194   | No file  | `dffef84dae8f`  |
| 1192   | No file  | `dffef84dae8f`  |
| 1187   | No file  | `dffef84dae8f`  |
| 1183   | No file  | `dffef84dae8f`  |
| 1177   | No file  | `dffef84dae8f`  |
| 1173   | No file  | `dffef84dae8f`  |
| 1167   | No file  | `dffef84dae8f`  |
| 1164   | No file  | `dffef84dae8f`  |
| 1156   | No file  | `dffef84dae8f`  |
| 1149   | No file  | `dffef84dae8f`  |
| 1144   | No file  | `dffef84dae8f`  |
| 1137   | No file  | `dffef84dae8f`  |
| 1132   | No file  | `dffef84dae8f`  |
| 1127   | No file  | `dffef84dae8f`  |
| 1122   | No file  | `dffef84dae8f`  |
| 1118   | No file  | `dffef84dae8f`  |
| 1114   | No file  | `dffef84dae8f`  |
| 1109   | No file  | `dffef84dae8f`  |
| 1102   | No file  | `dffef84dae8f`  |
| 1096   | No file  | `dffef84dae8f`  |
| 1088   | No file  | `dffef84dae8f`  |
| 1081   | No file  | `dffef84dae8f`  |
| 1076   | No file  | `dffef84dae8f`  |
| 1069   | No file  | `dffef84dae8f`  |
| 1064   | No file  | `dffef84dae8f`  |
| 1058   | No file  | `dffef84dae8f`  |
| 1051   | No file  | `dffef84dae8f`  |
| 1044   | No file  | `dffef84dae8f`  |
| 1036   | No file  | `dffef84dae8f`  |
| 1026   | No file  | `dffef84dae8f`  |
| 1016   | No file  | `dffef84dae8f`  |
| 1009   | No file  | `dffef84dae8f`  |
| 1005   | No file  | `dffef84dae8f`  |
| 1000   | No file  | `dffef84dae8f`  |
| 998    | No file  | `dffef84dae8f`  |
| 990    | No file  | `dffef84dae8f`  |
| 979    | No file  | `dffef84dae8f`  |
| 972    | No file  | `dffef84dae8f`  |
| 963    | No file  | `dffef84dae8f`  |
| 955    | No file  | `dffef84dae8f`  |
| 946    | No file  | `dffef84dae8f`  |
| 938    | No file  | `dffef84dae8f`  |
| 927    | No file  | `dffef84dae8f`  |
| 911    | No file  | `dffef84dae8f`  |
| 904    | No file  | `dffef84dae8f`  |
| 899    | No file  | `dffef84dae8f`  |
| 894    | No file  | `dffef84dae8f`  |
| 885    | No file  | `dffef84dae8f`  |
| 879    | No file  | `dffef84dae8f`  |
| 872    | No file  | `dffef84dae8f`  |
| 864    | No file  | `dffef84dae8f`  |
| 855    | No file  | `dffef84dae8f`  |
| 853    | No file  | `dffef84dae8f`  |
| 845    | No file  | `dffef84dae8f`  |
| 837    | No file  | `dffef84dae8f`  |
| 829    | No file  | `dffef84dae8f`  |
| 822    | No file  | `dffef84dae8f`  |
| 814    | No file  | `dffef84dae8f`  |
| 805    | No file  | `dffef84dae8f`  |
| 794    | No file  | `dffef84dae8f`  |
| 787    | No file  | `dffef84dae8f`  |
| 780    | No file  | `dffef84dae8f`  |
| 771    | No file  | `dffef84dae8f`  |
| 760    | No file  | `dffef84dae8f`  |
| 748    | No file  | `dffef84dae8f`  |
| 741    | No file  | `dffef84dae8f`  |
| 736    | No file  | `dffef84dae8f`  |
| 731    | No file  | `dffef84dae8f`  |
| 723    | No file  | `dffef84dae8f`  |
| 711    | No file  | `dffef84dae8f`  |
| 707    | No file  | `dffef84dae8f`  |
| 697    | No file  | `dffef84dae8f`  |
| 689    | No file  | `dffef84dae8f`  |
| 683    | No file  | `dffef84dae8f`  |
| 678    | No file  | `dffef84dae8f`  |
| 670    | No file  | `dffef84dae8f`  |
| 661    | No file  | `dffef84dae8f`  |
| 656    | No file  | `dffef84dae8f`  |
| 652    | No file  | `dffef84dae8f`  |
| 643    | No file  | `dffef84dae8f`  |
| 637    | No file  | `dffef84dae8f`  |
| 630    | No file  | `dffef84dae8f`  |
| 627    | No file  | `dffef84dae8f`  |
| 621    | No file  | `dffef84dae8f`  |
| 617    | No file  | `dffef84dae8f`  |
| 615    | No file  | `dffef84dae8f`  |
| 606    | No file  | `dffef84dae8f`  |
| 599    | No file  | `dffef84dae8f`  |
| 592    | No file  | `dffef84dae8f`  |
| 586    | No file  | `dffef84dae8f`  |
| 577    | No file  | `dffef84dae8f`  |
| 569    | No file  | `dffef84dae8f`  |
| 561    | No file  | `dffef84dae8f`  |
| 554    | No file  | `dffef84dae8f`  |
| 542    | No file  | `dffef84dae8f`  |
| 532    | No file  | `dffef84dae8f`  |
| 531    | No file  | `dffef84dae8f`  |
| 526    | No file  | `dffef84dae8f`  |
| 521    | No file  | `dffef84dae8f`  |
| 517    | No file  | `dffef84dae8f`  |
| 510    | No file  | `dffef84dae8f`  |
| 508    | No file  | `dffef84dae8f`  |
| 504    | No file  | `dffef84dae8f`  |
| 497    | No file  | `dffef84dae8f`  |
| 491    | No file  | `dffef84dae8f`  |
| 485    | No file  | `dffef84dae8f`  |
| 478    | No file  | `dffef84dae8f`  |
| 472    | No file  | `dffef84dae8f`  |
| 466    | No file  | `dffef84dae8f`  |
| 457    | No file  | `dffef84dae8f`  |
| 452    | No file  | `dffef84dae8f`  |
| 449    | No file  | `dffef84dae8f`  |
| 435    | No file  | `dffef84dae8f`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The file is exactly 32 bytes. Unlike DBSS records, it does not start with a record count; the first four bytes are the ASCII magic `PABR`.

| Offset  | Type    | Field                | Client 3473 | Notes                                                 |
| ------- | ------- | -------------------- | ----------- | ----------------------------------------------------- |
| `+0x00` | char[4] | magic                | `PABR`      | Fixed ASCII file signature                            |
| `+0x04` | u16     | use_gift_wp          | 5           | Energy spent on one gift (`UseGiftWp`)                |
| `+0x06` | u16     | use_propose_wp       | 5           | Energy spent on one confession (`UseProposeWp`)       |
| `+0x08` | u32     | min_propose_intimacy | 1000        | Lowest amity for a confession (`MinProposeIntimacy`)  |
| `+0x0C` | u64     | limit_gift_price     | 50000000    | Highest item price a gift may have (`LimitGiftPrice`) |
| `+0x14` | u32     | unknown_14           | 0           | Observed zero                                         |
| `+0x18` | u32     | unknown_18           | 20          | Not a `NpcGift_Option` column                         |
| `+0x1C` | u32     | unknown_1c           | 0           | Observed zero                                         |

## Field Names

The four named fields are the columns of the one-row `NpcGift_Option` sheet, in sheet order, that a private server on client 1784 ships in its `DataSheets.bexcel` and in the developer workbook `DataSheet_IntimacyDataTable.xlsm`. The sheet row is `5`, `5`, `1000`, `50000000`, the same values as client 3473, and that private server's own `npcgiftetc.bss` built from the sheet is byte-identical to the client 3473 file. The workbook's Korean column comments give the meanings:

| Column               | Comment             | English                                        |
| -------------------- | ------------------- | ---------------------------------------------- |
| `UseGiftWp`          | 선물 줄 때 기운 소모        | Energy spent when giving a gift                |
| `UseProposeWp`       | 고백 할 때 기운 소모        | Energy spent when confessing                   |
| `MinProposeIntimacy` | 고백 가능 최소 친밀도        | Lowest amity at which a confession is possible |
| `LimitGiftPrice`     | 선물할 수 있는 아이템 가격 한계값 | Price limit of an item that can be given       |

The field widths come from the server dump of that private server. Its `NpcGift_Option` loader reads exactly these four columns and stores them in a 16-byte global: `UseGiftWp` and `UseProposeWp` as u16 at `+0` and `+2`, `MinProposeIntimacy` as u32 at `+4` and `LimitGiftPrice` as an 8-byte value at `+8`. That global is the file's `+0x04..+0x14`, so the price is a u64 and the former `unknown_10` is its high half.

Neither the 2016 client with debug symbols nor the code of a private server on client 519 has a gift option type or loader; the workbook comments date the gift sheets to 2019-04-09. That server's `NpcGift_Option` table holds `0` in every column. The client Lua gift window (`panel_dialog_npcgift_renew.lua`) calls `ToClient_giveNpcGift` and `ToClient_proposeToNpc` and reads none of these values.

## Notes

- `npcgiftetc.bss` is self-contained; no offset companion has been observed.
- The block uses the same `PABR` magic seen in several compact BSS lookup and config files, but this file holds scalar config values, not a repeated table.
- Earlier versions of this doc called `use_gift_wp`, `use_propose_wp`, `min_propose_intimacy`, the low half of `limit_gift_price` and `unknown_18` `config_a` to `config_e`, and then `unknown_04` to `unknown_18`.
- The file is byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.

## Open Questions

### The Three Trailing u32 Fields

`unknown_14`, `unknown_18` and `unknown_1c` (`0`, `20`, `0` on client 3473) are not `NpcGift_Option` columns, and the server dump's loader does not write them. The client 1784 build of the four-column sheet still writes `20` at `+0x18`, so the value comes from the client's own struct, not from the sheet. Its meaning is unknown.
