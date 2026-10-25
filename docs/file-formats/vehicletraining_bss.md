# `vehicletraining.bss` Format

## Purpose

The mount training items: per item the training skill it raises, the
skill EXP one item gives and a Korean description that names the item and
where to get it. The skills are the three of
[`vehicletrainingskill.bss`](vehicletrainingskill_bss.md) (`49` Skill,
`50` Elegance, `51` Strength in [`vehicleskill.dbss`](vehicleskill_dbss.md)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------- | ----- | ------- | --------- |
| 1      | 1280 and later | `vehicletraining.bss` | 1,428 | 9 Row   | 21        |

| Layout | File                  | Known           | Unknown     |
| ------ | --------------------- | --------------- | ----------- |
| 1      | `vehicletraining.bss` | 1,392 B (97.5%) | 36 B (2.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `b1f0b112068b`  |
| 3482   | Layout 1             | `b1f0b112068b`  |
| 3474   | Layout 1             | `b1f0b112068b`  |
| 3473   | Layout 1             | `b1f0b112068b`  |
| 3464   | Layout 1             | `b1f0b112068b`  |
| 3458   | Layout 1             | `b1f0b112068b`  |
| 3454   | Layout 1             | `b1f0b112068b`  |
| 3444   | Layout 1             | `b1f0b112068b`  |
| 3435   | Layout 1             | `b1f0b112068b`  |
| 3426   | Layout 1             | `b1f0b112068b`  |
| 3418   | Layout 1             | `b1f0b112068b`  |
| 3412   | Layout 1             | `b1f0b112068b`  |
| 3402   | Layout 1             | `b1f0b112068b`  |
| 3396   | Layout 1             | `b1f0b112068b`  |
| 3387   | Layout 1             | `b1f0b112068b`  |
| 3381   | Layout 1             | `b1f0b112068b`  |
| 3373   | Layout 1             | `b1f0b112068b`  |
| 3364   | Layout 1             | `b1f0b112068b`  |
| 3356   | Layout 1             | `b1f0b112068b`  |
| 3349   | Layout 1             | `b1f0b112068b`  |
| 3342   | Layout 1             | `b1f0b112068b`  |
| 3335   | Layout 1             | `b1f0b112068b`  |
| 3326   | Layout 1             | `b1f0b112068b`  |
| 3321   | Layout 1             | `b1f0b112068b`  |
| 3314   | Layout 1             | `b1f0b112068b`  |
| 3303   | Layout 1             | `b1f0b112068b`  |
| 3302   | Layout 1             | `b1f0b112068b`  |
| 3293   | Layout 1             | `b1f0b112068b`  |
| 3283   | Layout 1             | `b1f0b112068b`  |
| 3275   | Layout 1             | `b1f0b112068b`  |
| 3267   | Layout 1             | `b1f0b112068b`  |
| 3258   | Layout 1             | `b1f0b112068b`  |
| 3251   | Layout 1             | `b1f0b112068b`  |
| 3242   | Layout 1             | `b1f0b112068b`  |
| 3235   | Layout 1             | `b1f0b112068b`  |
| 3229   | Layout 1             | `b1f0b112068b`  |
| 3212   | Layout 1             | `b1f0b112068b`  |
| 3203   | Layout 1             | `b1f0b112068b`  |
| 3193   | Layout 1             | `b1f0b112068b`  |
| 3186   | Layout 1             | `b1f0b112068b`  |
| 3177   | Layout 1             | `b1f0b112068b`  |
| 3169   | Layout 1             | `b1f0b112068b`  |
| 3158   | Layout 1             | `b1f0b112068b`  |
| 3151   | Layout 1             | `b1f0b112068b`  |
| 3144   | Layout 1             | `b1f0b112068b`  |
| 3133   | Layout 1             | `b1f0b112068b`  |
| 3125   | Layout 1             | `b1f0b112068b`  |
| 3118   | Layout 1             | `b1f0b112068b`  |
| 3111   | Layout 1             | `b1f0b112068b`  |
| 3103   | Layout 1             | `b1f0b112068b`  |
| 3095   | Layout 1             | `b1f0b112068b`  |
| 3086   | Layout 1             | `b1f0b112068b`  |
| 3072   | Layout 1             | `b1f0b112068b`  |
| 3062   | Layout 1             | `b1f0b112068b`  |
| 3052   | Layout 1             | `b1f0b112068b`  |
| 3045   | Layout 1             | `b1f0b112068b`  |
| 3037   | Layout 1             | `b1f0b112068b`  |
| 3030   | Layout 1             | `b1f0b112068b`  |
| 3021   | Layout 1             | `b1f0b112068b`  |
| 3012   | Layout 1             | `b1f0b112068b`  |
| 3002   | Layout 1             | `b1f0b112068b`  |
| 2995   | Layout 1             | `b1f0b112068b`  |
| 2987   | Layout 1             | `b1f0b112068b`  |
| 2978   | Layout 1             | `b1f0b112068b`  |
| 2970   | Layout 1             | `b1f0b112068b`  |
| 2959   | Layout 1             | `b1f0b112068b`  |
| 2951   | Layout 1             | `b1f0b112068b`  |
| 2942   | Layout 1             | `b1f0b112068b`  |
| 2935   | Layout 1             | `b1f0b112068b`  |
| 2932   | Layout 1             | `b1f0b112068b`  |
| 2923   | Layout 1             | `b1f0b112068b`  |
| 2919   | Layout 1             | `b1f0b112068b`  |
| 2907   | Layout 1             | `b1f0b112068b`  |
| 2900   | Layout 1             | `b1f0b112068b`  |
| 2891   | Layout 1             | `b1f0b112068b`  |
| 2882   | Layout 1             | `b1f0b112068b`  |
| 2872   | Layout 1             | `b1f0b112068b`  |
| 2863   | Layout 1             | `b1f0b112068b`  |
| 2855   | Layout 1             | `b1f0b112068b`  |
| 2849   | Layout 1             | `b1f0b112068b`  |
| 2844   | Layout 1             | `b1f0b112068b`  |
| 2834   | Layout 1             | `b1f0b112068b`  |
| 2825   | Layout 1             | `b1f0b112068b`  |
| 2819   | Layout 1             | `b1f0b112068b`  |
| 2811   | Layout 1             | `b1f0b112068b`  |
| 2803   | Layout 1             | `b1f0b112068b`  |
| 2794   | Layout 1             | `b1f0b112068b`  |
| 2783   | Layout 1             | `b1f0b112068b`  |
| 2774   | Layout 1             | `b1f0b112068b`  |
| 2765   | Layout 1             | `b1f0b112068b`  |
| 2756   | Layout 1             | `b1f0b112068b`  |
| 2750   | Layout 1             | `b1f0b112068b`  |
| 2743   | Layout 1             | `b1f0b112068b`  |
| 2736   | Layout 1             | `b1f0b112068b`  |
| 2726   | Layout 1             | `b1f0b112068b`  |
| 2717   | Layout 1             | `b1f0b112068b`  |
| 2709   | Layout 1             | `b1f0b112068b`  |
| 2703   | Layout 1             | `b1f0b112068b`  |
| 2695   | Layout 1             | `b1f0b112068b`  |
| 2684   | Layout 1             | `b1f0b112068b`  |
| 2672   | Layout 1             | `b1f0b112068b`  |
| 2665   | Layout 1             | `b1f0b112068b`  |
| 2657   | Layout 1             | `b1f0b112068b`  |
| 2649   | Layout 1             | `b1f0b112068b`  |
| 2644   | Layout 1             | `b1f0b112068b`  |
| 2637   | Layout 1             | `b1f0b112068b`  |
| 2629   | Layout 1             | `b1f0b112068b`  |
| 2619   | Layout 1             | `b1f0b112068b`  |
| 2612   | Layout 1             | `b1f0b112068b`  |
| 2606   | Layout 1             | `b1f0b112068b`  |
| 2602   | Layout 1             | `b1f0b112068b`  |
| 2601   | Layout 1             | `b1f0b112068b`  |
| 2592   | Layout 1             | `b1f0b112068b`  |
| 2583   | Layout 1             | `b1f0b112068b`  |
| 2575   | Layout 1             | `b1f0b112068b`  |
| 2567   | Layout 1             | `b1f0b112068b`  |
| 2560   | Layout 1             | `b1f0b112068b`  |
| 2553   | Layout 1             | `b1f0b112068b`  |
| 2545   | Layout 1             | `b1f0b112068b`  |
| 2538   | Layout 1             | `b1f0b112068b`  |
| 2529   | Layout 1             | `b1f0b112068b`  |
| 2519   | Layout 1             | `b1f0b112068b`  |
| 2513   | Layout 1             | `b1f0b112068b`  |
| 2510   | Layout 1             | `b1f0b112068b`  |
| 2507   | Layout 1             | `b1f0b112068b`  |
| 2503   | Layout 1             | `b1f0b112068b`  |
| 2498   | Layout 1             | `b1f0b112068b`  |
| 2492   | Layout 1             | `b1f0b112068b`  |
| 2487   | Layout 1             | `b1f0b112068b`  |
| 2480   | Layout 1             | `b1f0b112068b`  |
| 2474   | Layout 1             | `b1f0b112068b`  |
| 2468   | Layout 1             | `b1f0b112068b`  |
| 2460   | Layout 1             | `b1f0b112068b`  |
| 2453   | Layout 1             | `b1f0b112068b`  |
| 2444   | Layout 1             | `b1f0b112068b`  |
| 2438   | Layout 1             | `b1f0b112068b`  |
| 2434   | Layout 1             | `b1f0b112068b`  |
| 2429   | Layout 1             | `b1f0b112068b`  |
| 2421   | Layout 1             | `b1f0b112068b`  |
| 2414   | Layout 1             | `b1f0b112068b`  |
| 2407   | Layout 1             | `b1f0b112068b`  |
| 2401   | Layout 1             | `b1f0b112068b`  |
| 2397   | Layout 1             | `b1f0b112068b`  |
| 2393   | Layout 1             | `b1f0b112068b`  |
| 2384   | Layout 1             | `b1f0b112068b`  |
| 2378   | Layout 1             | `b1f0b112068b`  |
| 2372   | Layout 1             | `b1f0b112068b`  |
| 2358   | Layout 1             | `b1f0b112068b`  |
| 2352   | Layout 1             | `b1f0b112068b`  |
| 2347   | Layout 1             | `b1f0b112068b`  |
| 2343   | Layout 1             | `b1f0b112068b`  |
| 2335   | Layout 1             | `b1f0b112068b`  |
| 2327   | Layout 1             | `b1f0b112068b`  |
| 2324   | Layout 1             | `b1f0b112068b`  |
| 2319   | Layout 1             | `b1f0b112068b`  |
| 2313   | Layout 1             | `b1f0b112068b`  |
| 2308   | Layout 1             | `b1f0b112068b`  |
| 2302   | Layout 1             | `b1f0b112068b`  |
| 2295   | Layout 1             | `b1f0b112068b`  |
| 2290   | Layout 1             | `b1f0b112068b`  |
| 2284   | Layout 1             | `b1f0b112068b`  |
| 2276   | Layout 1             | `b1f0b112068b`  |
| 2269   | Layout 1             | `b1f0b112068b`  |
| 2259   | Layout 1             | `b1f0b112068b`  |
| 2250   | Layout 1             | `b1f0b112068b`  |
| 2243   | Layout 1             | `b1f0b112068b`  |
| 2235   | Layout 1             | `b1f0b112068b`  |
| 2229   | Layout 1             | `b1f0b112068b`  |
| 2224   | Layout 1             | `b1f0b112068b`  |
| 2218   | Layout 1             | `b1f0b112068b`  |
| 2215   | Layout 1             | `b1f0b112068b`  |
| 2207   | Layout 1             | `b1f0b112068b`  |
| 2203   | Layout 1             | `b1f0b112068b`  |
| 2196   | Layout 1             | `b1f0b112068b`  |
| 2192   | Layout 1             | `b1f0b112068b`  |
| 2189   | Layout 1             | `b1f0b112068b`  |
| 2183   | Layout 1             | `b1f0b112068b`  |
| 2179   | Layout 1             | `b1f0b112068b`  |
| 2171   | Layout 1             | `b1f0b112068b`  |
| 2163   | Layout 1             | `b1f0b112068b`  |
| 2156   | Layout 1             | `b1f0b112068b`  |
| 2151   | Layout 1             | `b1f0b112068b`  |
| 2147   | Layout 1             | `b1f0b112068b`  |
| 2142   | Layout 1             | `b1f0b112068b`  |
| 2138   | Layout 1             | `b1f0b112068b`  |
| 2134   | Layout 1             | `b1f0b112068b`  |
| 2130   | Layout 1             | `b1f0b112068b`  |
| 2122   | Layout 1             | `b1f0b112068b`  |
| 2107   | Layout 1             | `b1f0b112068b`  |
| 2098   | Layout 1             | `b1f0b112068b`  |
| 2089   | Layout 1             | `b1f0b112068b`  |
| 2081   | Layout 1             | `b1f0b112068b`  |
| 2073   | Layout 1             | `b1f0b112068b`  |
| 2067   | Layout 1             | `b1f0b112068b`  |
| 2063   | Layout 1             | `b1f0b112068b`  |
| 2059   | Layout 1             | `b1f0b112068b`  |
| 2052   | Layout 1             | `b1f0b112068b`  |
| 2044   | Layout 1             | `b1f0b112068b`  |
| 2039   | Layout 1             | `b1f0b112068b`  |
| 2032   | Layout 1             | `b1f0b112068b`  |
| 2025   | Layout 1             | `b1f0b112068b`  |
| 2011   | Layout 1             | `b1f0b112068b`  |
| 2005   | Layout 1             | `b1f0b112068b`  |
| 2000   | Layout 1             | `b1f0b112068b`  |
| 1996   | Layout 1             | `b1f0b112068b`  |
| 1991   | Layout 1             | `b1f0b112068b`  |
| 1985   | Layout 1             | `b1f0b112068b`  |
| 1980   | Layout 1             | `b1f0b112068b`  |
| 1969   | Layout 1             | `b1f0b112068b`  |
| 1964   | Layout 1             | `b1f0b112068b`  |
| 1958   | Layout 1             | `b1f0b112068b`  |
| 1950   | Layout 1             | `b1f0b112068b`  |
| 1945   | Layout 1             | `b1f0b112068b`  |
| 1937   | Layout 1             | `b1f0b112068b`  |
| 1933   | Layout 1             | `b1f0b112068b`  |
| 1927   | Layout 1             | `b1f0b112068b`  |
| 1921   | Layout 1             | `b1f0b112068b`  |
| 1914   | Layout 1             | `b1f0b112068b`  |
| 1908   | Layout 1             | `b1f0b112068b`  |
| 1897   | Layout 1             | `b1f0b112068b`  |
| 1892   | Layout 1             | `b1f0b112068b`  |
| 1886   | Layout 1             | `b1f0b112068b`  |
| 1881   | Layout 1             | `b1f0b112068b`  |
| 1871   | Layout 1             | `b1f0b112068b`  |
| 1866   | Layout 1             | `b1f0b112068b`  |
| 1862   | Layout 1             | `b1f0b112068b`  |
| 1854   | Layout 1             | `b1f0b112068b`  |
| 1846   | Layout 1             | `b1f0b112068b`  |
| 1838   | Layout 1             | `b1f0b112068b`  |
| 1832   | Layout 1             | `b1f0b112068b`  |
| 1826   | Layout 1             | `b1f0b112068b`  |
| 1822   | Layout 1             | `b1f0b112068b`  |
| 1818   | Layout 1             | `b1f0b112068b`  |
| 1804   | Layout 1             | `b1f0b112068b`  |
| 1794   | Layout 1             | `b1f0b112068b`  |
| 1790   | Layout 1             | `b1f0b112068b`  |
| 1784   | Layout 1             | `b1f0b112068b`  |
| 1774   | Layout 1             | `b1f0b112068b`  |
| 1771   | Layout 1             | `b1f0b112068b`  |
| 1762   | Layout 1             | `b1f0b112068b`  |
| 1759   | Layout 1             | `b1f0b112068b`  |
| 1754   | Layout 1             | `b1f0b112068b`  |
| 1749   | Layout 1             | `b1f0b112068b`  |
| 1743   | Layout 1             | `b1f0b112068b`  |
| 1737   | Layout 1             | `b1f0b112068b`  |
| 1731   | Layout 1             | `b1f0b112068b`  |
| 1725   | Layout 1             | `b1f0b112068b`  |
| 1717   | Layout 1             | `b1f0b112068b`  |
| 1710   | Layout 1             | `b1f0b112068b`  |
| 1704   | Layout 1             | `b1f0b112068b`  |
| 1698   | Layout 1             | `b1f0b112068b`  |
| 1690   | Layout 1             | `b1f0b112068b`  |
| 1685   | Layout 1             | `b1f0b112068b`  |
| 1680   | Layout 1             | `b1f0b112068b`  |
| 1674   | Layout 1             | `b1f0b112068b`  |
| 1668   | Layout 1             | `b1f0b112068b`  |
| 1659   | Layout 1             | `b1f0b112068b`  |
| 1649   | Layout 1             | `b1f0b112068b`  |
| 1642   | Layout 1             | `b1f0b112068b`  |
| 1636   | Layout 1             | `b1f0b112068b`  |
| 1628   | Layout 1             | `b1f0b112068b`  |
| 1622   | Layout 1             | `b1f0b112068b`  |
| 1614   | Layout 1             | `b1f0b112068b`  |
| 1608   | Layout 1             | `b1f0b112068b`  |
| 1602   | Layout 1             | `b1f0b112068b`  |
| 1598   | Layout 1             | `b1f0b112068b`  |
| 1594   | Layout 1             | `b1f0b112068b`  |
| 1590   | Layout 1             | `b1f0b112068b`  |
| 1587   | Layout 1             | `b1f0b112068b`  |
| 1584   | Layout 1             | `b1f0b112068b`  |
| 1579   | Layout 1             | `b1f0b112068b`  |
| 1572   | Layout 1             | `b1f0b112068b`  |
| 1565   | Layout 1             | `b1f0b112068b`  |
| 1559   | Layout 1             | `b1f0b112068b`  |
| 1554   | Layout 1             | `b1f0b112068b`  |
| 1547   | Layout 1             | `b1f0b112068b`  |
| 1537   | Layout 1             | `b1f0b112068b`  |
| 1529   | Layout 1             | `b1f0b112068b`  |
| 1524   | Layout 1             | `b1f0b112068b`  |
| 1519   | Layout 1             | `b1f0b112068b`  |
| 1509   | Layout 1             | `b1f0b112068b`  |
| 1506   | Layout 1             | `b1f0b112068b`  |
| 1504   | Layout 1             | `b1f0b112068b`  |
| 1500   | Layout 1             | `b1f0b112068b`  |
| 1493   | Layout 1             | `b1f0b112068b`  |
| 1489   | Layout 1             | `b1f0b112068b`  |
| 1485   | Layout 1             | `b1f0b112068b`  |
| 1481   | Layout 1             | `b1f0b112068b`  |
| 1474   | Layout 1             | `b1f0b112068b`  |
| 1466   | Layout 1             | `b1f0b112068b`  |
| 1462   | Layout 1             | `b1f0b112068b`  |
| 1459   | Layout 1             | `b1f0b112068b`  |
| 1453   | Layout 1             | `b1f0b112068b`  |
| 1450   | Layout 1             | `b1f0b112068b`  |
| 1445   | Layout 1             | `b1f0b112068b`  |
| 1439   | Layout 1             | `b1f0b112068b`  |
| 1433   | Layout 1             | `b1f0b112068b`  |
| 1430   | Layout 1             | `b1f0b112068b`  |
| 1426   | Layout 1             | `b1f0b112068b`  |
| 1421   | Layout 1             | `b1f0b112068b`  |
| 1417   | Layout 1             | `b1f0b112068b`  |
| 1416   | Layout 1             | `b1f0b112068b`  |
| 1409   | Layout 1             | `b1f0b112068b`  |
| 1405   | Layout 1             | `b1f0b112068b`  |
| 1401   | Layout 1             | `b1f0b112068b`  |
| 1396   | Layout 1             | `b1f0b112068b`  |
| 1391   | Layout 1             | `b1f0b112068b`  |
| 1390   | Layout 1             | `b1f0b112068b`  |
| 1386   | Layout 1             | `b1f0b112068b`  |
| 1381   | Layout 1             | `b1f0b112068b`  |
| 1379   | Layout 1             | `b1f0b112068b`  |
| 1372   | Layout 1             | `b1f0b112068b`  |
| 1366   | Layout 1             | `b1f0b112068b`  |
| 1364   | Layout 1             | `b1f0b112068b`  |
| 1363   | Layout 1             | `b1f0b112068b`  |
| 1360   | Layout 1             | `b1f0b112068b`  |
| 1358   | Layout 1             | `b1f0b112068b`  |
| 1355   | Layout 1             | `b1f0b112068b`  |
| 1351   | Layout 1             | `b1f0b112068b`  |
| 1348   | Layout 1             | `b1f0b112068b`  |
| 1346   | Layout 1             | `b1f0b112068b`  |
| 1341   | Layout 1             | `b1f0b112068b`  |
| 1340   | Layout 1             | `b1f0b112068b`  |
| 1338   | Layout 1             | `b1f0b112068b`  |
| 1335   | Layout 1             | `b1f0b112068b`  |
| 1333   | Layout 1             | `b1f0b112068b`  |
| 1329   | Layout 1             | `b1f0b112068b`  |
| 1327   | Layout 1             | `b1f0b112068b`  |
| 1324   | Layout 1             | `b1f0b112068b`  |
| 1321   | Layout 1             | `b1f0b112068b`  |
| 1319   | Layout 1             | `b1f0b112068b`  |
| 1318   | Layout 1             | `b1f0b112068b`  |
| 1316   | Layout 1             | `b1f0b112068b`  |
| 1313   | Layout 1             | `b1f0b112068b`  |
| 1311   | Layout 1             | `b1f0b112068b`  |
| 1309   | Layout 1             | `b1f0b112068b`  |
| 1304   | Layout 1             | `b1f0b112068b`  |
| 1292   | Layout 1             | `b1f0b112068b`  |
| 1286   | Layout 1             | `b1f0b112068b`  |
| 1280   | Layout 1             | `b1f0b112068b`  |
| 1276   | No documented layout | `b1f0b112068b`  |
| 1267   | No documented layout | `b1f0b112068b`  |
| 1261   | No documented layout | `b1f0b112068b`  |
| 1256   | No documented layout | `b1f0b112068b`  |
| 1250   | No documented layout | `b1f0b112068b`  |
| 1246   | No documented layout | `b1f0b112068b`  |
| 1239   | No documented layout | `b1f0b112068b`  |
| 1230   | No documented layout | `b1f0b112068b`  |
| 1226   | No documented layout | `b1f0b112068b`  |
| 1220   | No documented layout | `b1f0b112068b`  |
| 1217   | No documented layout | `b1f0b112068b`  |
| 1211   | No documented layout | `b1f0b112068b`  |
| 1210   | No documented layout | `b1f0b112068b`  |
| 1208   | No documented layout | `b1f0b112068b`  |
| 1203   | No documented layout | `b1f0b112068b`  |
| 1197   | No documented layout | `b1f0b112068b`  |
| 1194   | No documented layout | `b1f0b112068b`  |
| 1192   | No documented layout | `b1f0b112068b`  |
| 1187   | No documented layout | `b1f0b112068b`  |
| 1183   | No documented layout | `b1f0b112068b`  |
| 1177   | No documented layout | `b1f0b112068b`  |
| 1173   | No documented layout | `b1f0b112068b`  |
| 1167   | No documented layout | `b1f0b112068b`  |
| 1164   | No documented layout | `b1f0b112068b`  |
| 1156   | No documented layout | `b1f0b112068b`  |
| 1149   | No documented layout | `b1f0b112068b`  |
| 1144   | No documented layout | `b1f0b112068b`  |
| 1137   | No documented layout | `b1f0b112068b`  |
| 1132   | No documented layout | `b1f0b112068b`  |
| 1127   | No documented layout | `b1f0b112068b`  |
| 1122   | No documented layout | `b1f0b112068b`  |
| 1118   | No documented layout | `b1f0b112068b`  |
| 1114   | No documented layout | `b1f0b112068b`  |
| 1109   | No documented layout | `b1f0b112068b`  |
| 1102   | No file              | `b1f0b112068b`  |
| 1096   | No file              | `b1f0b112068b`  |
| 1088   | No file              | `b1f0b112068b`  |
| 1081   | No file              | `b1f0b112068b`  |
| 1076   | No file              | `b1f0b112068b`  |
| 1069   | No file              | `b1f0b112068b`  |
| 1064   | No file              | `b1f0b112068b`  |
| 1058   | No file              | `b1f0b112068b`  |
| 1051   | No file              | `b1f0b112068b`  |
| 1044   | No file              | `b1f0b112068b`  |
| 1036   | No file              | `b1f0b112068b`  |
| 1026   | No file              | `b1f0b112068b`  |
| 1016   | No file              | `b1f0b112068b`  |
| 1009   | No file              | `b1f0b112068b`  |
| 1005   | No file              | `b1f0b112068b`  |
| 1000   | No file              | `b1f0b112068b`  |
| 998    | No file              | `b1f0b112068b`  |
| 990    | No file              | `b1f0b112068b`  |
| 979    | No file              | `b1f0b112068b`  |
| 972    | No file              | `b1f0b112068b`  |
| 963    | No file              | `b1f0b112068b`  |
| 955    | No file              | `b1f0b112068b`  |
| 946    | No file              | `b1f0b112068b`  |
| 938    | No file              | `b1f0b112068b`  |
| 927    | No file              | `b1f0b112068b`  |
| 911    | No file              | `b1f0b112068b`  |
| 904    | No file              | `b1f0b112068b`  |
| 899    | No file              | `b1f0b112068b`  |
| 894    | No file              | `b1f0b112068b`  |
| 885    | No file              | `b1f0b112068b`  |
| 879    | No file              | `b1f0b112068b`  |
| 872    | No file              | `b1f0b112068b`  |
| 864    | No file              | `b1f0b112068b`  |
| 855    | No file              | `b1f0b112068b`  |
| 853    | No file              | `b1f0b112068b`  |
| 845    | No file              | `b1f0b112068b`  |
| 837    | No file              | `b1f0b112068b`  |
| 829    | No documented layout | `b1f0b112068b`  |
| 822    | No documented layout | `b1f0b112068b`  |
| 814    | No documented layout | `b1f0b112068b`  |
| 805    | No documented layout | `b1f0b112068b`  |
| 794    | No documented layout | `b1f0b112068b`  |
| 787    | No documented layout | `b1f0b112068b`  |
| 780    | No documented layout | `b1f0b112068b`  |
| 771    | No documented layout | `b1f0b112068b`  |
| 760    | No documented layout | `b1f0b112068b`  |
| 748    | No documented layout | `b1f0b112068b`  |
| 741    | No documented layout | `b1f0b112068b`  |
| 736    | No documented layout | `b1f0b112068b`  |
| 731    | No documented layout | `b1f0b112068b`  |
| 723    | No documented layout | `b1f0b112068b`  |
| 711    | No documented layout | `b1f0b112068b`  |
| 707    | No documented layout | `b1f0b112068b`  |
| 697    | No documented layout | `b1f0b112068b`  |
| 689    | No documented layout | `b1f0b112068b`  |
| 683    | No documented layout | `b1f0b112068b`  |
| 678    | No documented layout | `b1f0b112068b`  |
| 670    | No documented layout | `b1f0b112068b`  |
| 661    | No documented layout | `b1f0b112068b`  |
| 656    | No documented layout | `b1f0b112068b`  |
| 652    | No documented layout | `b1f0b112068b`  |
| 643    | No documented layout | `b1f0b112068b`  |
| 637    | No documented layout | `b1f0b112068b`  |
| 630    | No documented layout | `b1f0b112068b`  |
| 627    | No documented layout | `b1f0b112068b`  |
| 621    | No documented layout | `b1f0b112068b`  |
| 617    | No documented layout | `b1f0b112068b`  |
| 615    | No documented layout | `b1f0b112068b`  |
| 606    | No documented layout | `b1f0b112068b`  |
| 599    | No documented layout | `b1f0b112068b`  |
| 592    | No documented layout | `b1f0b112068b`  |
| 586    | No documented layout | `b1f0b112068b`  |
| 577    | No documented layout | `b1f0b112068b`  |
| 569    | No documented layout | `b1f0b112068b`  |
| 561    | No documented layout | `b1f0b112068b`  |
| 554    | No documented layout | `b1f0b112068b`  |
| 542    | No documented layout | `b1f0b112068b`  |
| 532    | No documented layout | `b1f0b112068b`  |
| 531    | No documented layout | `b1f0b112068b`  |
| 526    | No documented layout | `b1f0b112068b`  |
| 521    | No documented layout | `b1f0b112068b`  |
| 517    | No documented layout | `b1f0b112068b`  |
| 510    | No documented layout | `b1f0b112068b`  |
| 508    | No documented layout | `b1f0b112068b`  |
| 504    | No documented layout | `b1f0b112068b`  |
| 497    | No documented layout | `b1f0b112068b`  |
| 491    | No documented layout | `b1f0b112068b`  |
| 485    | No documented layout | `b1f0b112068b`  |
| 478    | No documented layout | `b1f0b112068b`  |
| 472    | No documented layout | `b1f0b112068b`  |
| 466    | No documented layout | `b1f0b112068b`  |
| 457    | No documented layout | `b1f0b112068b`  |
| 452    | No documented layout | `b1f0b112068b`  |
| 449    | No documented layout | `b1f0b112068b`  |
| 435    | No documented layout | `b1f0b112068b`  |

<!-- versions:end -->

## Companion Files

None. The handler names each item with LOC type 0 and each skill with LOC
type 8 from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of training items                      |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (21 bytes)

| Offset  | Type | Field        | Notes                                                             |
| ------- | ---- | ------------ | ----------------------------------------------------------------- |
| `+0x00` | u32  | item_key     | Training item; LOC type 0 names it                                |
| `+0x04` | u32  | item_key_dup | Equals `item_key` on every row                                    |
| `+0x08` | u8   | skill_key    | `vehicleskill.dbss` key of the training skill; LOC type 8 names it |
| `+0x09` | u32  | experience   | Skill EXP one item gives: `300` or `600` (clients 1784 and 3482)  |
| `+0x0D` | u32  | desc_ref     | String table index of the description; row `n` holds `n`          |
| `+0x11` | u32  | unknown_11   | `0` on every row (clients 1784 and 3482)                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                        |
| ------- | ------------------ | ------------ | ------------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; one per row on clients 1784 and 3482      |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE Korean descriptions in row order                    |

## Training Items

The rows on clients 1784 and 3482 (the files are the same 1,428 bytes),
with the LOC type 0 and type 8 names of client 3482:

| `item_key` | Item                            | `skill_key`   | `experience` |
| ---------- | ------------------------------- | ------------- | ------------ |
| `50816`    | Fruit of Yianaros               | `49` Skill    | `600`        |
| `50808`    | Rainbow Gem Fruit               | `49` Skill    | `300`        |
| `50817`    | Mysterious Blue Conch           | `50` Elegance | `600`        |
| `50809`    | Breezy Conch Seaweed            | `50` Elegance | `300`        |
| `50810`    | Deep Blue Hoof Root             | `51` Strength | `300`        |
| `50807`    | Pure Forest Breath              | `51` Strength | `300`        |
| `50804`    | Stonetail Fodder                | `49` Skill    | `300`        |
| `50806`    | Spirit Pouch of Ferocious Beast | `50` Elegance | `300`        |
| `50815`    | Brilliant Crimson Fire Flower   | `51` Strength | `600`        |

Each description reads like `기술 훈련에는 "무지개 보석과일" 아이템이
필요합니다. "무지개 보석과일" 아이템은 무역 인장으로 교환이 가능합니다.`
("Skill training needs the Rainbow Gem Fruit item. It can be exchanged
for trade seals."). No LOC type holds an English copy.

## Field Names

The names follow the `VehicleTrainingSkill_Item_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784, also in that server's
`datasheet_vehicleskill.xlsm`: columns `ItemKey`, `SkillKey`, `Experience`
and `Desc`, 13 rows. The 9 file rows match 9 sheet rows on all four
columns by `ItemKey` (clients 1784 and 3482); the 4 sheet rows the file
leaves out are the QA items `50811` to `50814` (`Desc` `QA아이템은 명령어로
획득 할 수 있습니다.`, Experience `30000`). The server dump of the same
build reads `SkillKey` as an int, `Experience` through its 32-bit reader
and `Desc` as a wide string. The sheet's `#비고` note columns are not
compiled.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/servant_tables.py`: the
  item with its icon and name, the skill name, the EXP and the Korean
  description.

## Open Questions

### What unknown_11 Is

The 4 bytes after `desc_ref` are `0` on every row of clients 1784 and
3482, and the sheet has no fifth compiled column. They may be padding of
the client struct or the high half of a 64-bit field; no Lua reads the
file.
