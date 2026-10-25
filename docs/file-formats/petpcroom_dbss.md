# `petpcroom.dbss` Format

## Purpose

The equip skills of the PC room pets: each row is a pet key from
[`pet.dbss`](pet_dbss.md) and three `equip_skill_id`s from Section 1 of
[`petequipskill.bss`](petequipskill_bss.md). Companion
`petpcroomoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records       | Row bytes |
| ------ | -------------- | ---------------------- | ----- | ------------- | --------- |
| 1      | 1261 and later | `petpcroom.dbss`       | 144   | 10 Row        | 14        |
| 1      | 1261 and later | `petpcroomoffset.dbss` | 104   | 10 Offset Row | 10        |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `petpcroom.dbss`       | 144 B (100.0%) | 0 B (0.0%) |
| 1      | `petpcroomoffset.dbss` | 104 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `dfaa1dd8a47d`  |
| 3482   | Layout 1 | `dfaa1dd8a47d`  |
| 3474   | Layout 1 | `dfaa1dd8a47d`  |
| 3473   | Layout 1 | `dfaa1dd8a47d`  |
| 3464   | Layout 1 | `dfaa1dd8a47d`  |
| 3458   | Layout 1 | `dfaa1dd8a47d`  |
| 3454   | Layout 1 | `dfaa1dd8a47d`  |
| 3444   | Layout 1 | `dfaa1dd8a47d`  |
| 3435   | Layout 1 | `dfaa1dd8a47d`  |
| 3426   | Layout 1 | `dfaa1dd8a47d`  |
| 3418   | Layout 1 | `dfaa1dd8a47d`  |
| 3412   | Layout 1 | `dfaa1dd8a47d`  |
| 3402   | Layout 1 | `dfaa1dd8a47d`  |
| 3396   | Layout 1 | `dfaa1dd8a47d`  |
| 3387   | Layout 1 | `dfaa1dd8a47d`  |
| 3381   | Layout 1 | `dfaa1dd8a47d`  |
| 3373   | Layout 1 | `dfaa1dd8a47d`  |
| 3364   | Layout 1 | `dfaa1dd8a47d`  |
| 3356   | Layout 1 | `dfaa1dd8a47d`  |
| 3349   | Layout 1 | `dfaa1dd8a47d`  |
| 3342   | Layout 1 | `dfaa1dd8a47d`  |
| 3335   | Layout 1 | `dfaa1dd8a47d`  |
| 3326   | Layout 1 | `dfaa1dd8a47d`  |
| 3321   | Layout 1 | `dfaa1dd8a47d`  |
| 3314   | Layout 1 | `dfaa1dd8a47d`  |
| 3303   | Layout 1 | `dfaa1dd8a47d`  |
| 3302   | Layout 1 | `dfaa1dd8a47d`  |
| 3293   | Layout 1 | `dfaa1dd8a47d`  |
| 3283   | Layout 1 | `dfaa1dd8a47d`  |
| 3275   | Layout 1 | `dfaa1dd8a47d`  |
| 3267   | Layout 1 | `dfaa1dd8a47d`  |
| 3258   | Layout 1 | `dfaa1dd8a47d`  |
| 3251   | Layout 1 | `dfaa1dd8a47d`  |
| 3242   | Layout 1 | `dfaa1dd8a47d`  |
| 3235   | Layout 1 | `dfaa1dd8a47d`  |
| 3229   | Layout 1 | `dfaa1dd8a47d`  |
| 3212   | Layout 1 | `dfaa1dd8a47d`  |
| 3203   | Layout 1 | `dfaa1dd8a47d`  |
| 3193   | Layout 1 | `dfaa1dd8a47d`  |
| 3186   | Layout 1 | `dfaa1dd8a47d`  |
| 3177   | Layout 1 | `dfaa1dd8a47d`  |
| 3169   | Layout 1 | `dfaa1dd8a47d`  |
| 3158   | Layout 1 | `dfaa1dd8a47d`  |
| 3151   | Layout 1 | `dfaa1dd8a47d`  |
| 3144   | Layout 1 | `dfaa1dd8a47d`  |
| 3133   | Layout 1 | `dfaa1dd8a47d`  |
| 3125   | Layout 1 | `dfaa1dd8a47d`  |
| 3118   | Layout 1 | `dfaa1dd8a47d`  |
| 3111   | Layout 1 | `dfaa1dd8a47d`  |
| 3103   | Layout 1 | `dfaa1dd8a47d`  |
| 3095   | Layout 1 | `dfaa1dd8a47d`  |
| 3086   | Layout 1 | `dfaa1dd8a47d`  |
| 3072   | Layout 1 | `dfaa1dd8a47d`  |
| 3062   | Layout 1 | `dfaa1dd8a47d`  |
| 3052   | Layout 1 | `dfaa1dd8a47d`  |
| 3045   | Layout 1 | `dfaa1dd8a47d`  |
| 3037   | Layout 1 | `dfaa1dd8a47d`  |
| 3030   | Layout 1 | `dfaa1dd8a47d`  |
| 3021   | Layout 1 | `dfaa1dd8a47d`  |
| 3012   | Layout 1 | `dfaa1dd8a47d`  |
| 3002   | Layout 1 | `dfaa1dd8a47d`  |
| 2995   | Layout 1 | `dfaa1dd8a47d`  |
| 2987   | Layout 1 | `dfaa1dd8a47d`  |
| 2978   | Layout 1 | `dfaa1dd8a47d`  |
| 2970   | Layout 1 | `dfaa1dd8a47d`  |
| 2959   | Layout 1 | `dfaa1dd8a47d`  |
| 2951   | Layout 1 | `dfaa1dd8a47d`  |
| 2942   | Layout 1 | `dfaa1dd8a47d`  |
| 2935   | Layout 1 | `dfaa1dd8a47d`  |
| 2932   | Layout 1 | `dfaa1dd8a47d`  |
| 2923   | Layout 1 | `dfaa1dd8a47d`  |
| 2919   | Layout 1 | `dfaa1dd8a47d`  |
| 2907   | Layout 1 | `dfaa1dd8a47d`  |
| 2900   | Layout 1 | `dfaa1dd8a47d`  |
| 2891   | Layout 1 | `dfaa1dd8a47d`  |
| 2882   | Layout 1 | `dfaa1dd8a47d`  |
| 2872   | Layout 1 | `dfaa1dd8a47d`  |
| 2863   | Layout 1 | `dfaa1dd8a47d`  |
| 2855   | Layout 1 | `dfaa1dd8a47d`  |
| 2849   | Layout 1 | `dfaa1dd8a47d`  |
| 2844   | Layout 1 | `dfaa1dd8a47d`  |
| 2834   | Layout 1 | `dfaa1dd8a47d`  |
| 2825   | Layout 1 | `dfaa1dd8a47d`  |
| 2819   | Layout 1 | `dfaa1dd8a47d`  |
| 2811   | Layout 1 | `dfaa1dd8a47d`  |
| 2803   | Layout 1 | `dfaa1dd8a47d`  |
| 2794   | Layout 1 | `dfaa1dd8a47d`  |
| 2783   | Layout 1 | `dfaa1dd8a47d`  |
| 2774   | Layout 1 | `dfaa1dd8a47d`  |
| 2765   | Layout 1 | `dfaa1dd8a47d`  |
| 2756   | Layout 1 | `dfaa1dd8a47d`  |
| 2750   | Layout 1 | `dfaa1dd8a47d`  |
| 2743   | Layout 1 | `dfaa1dd8a47d`  |
| 2736   | Layout 1 | `dfaa1dd8a47d`  |
| 2726   | Layout 1 | `dfaa1dd8a47d`  |
| 2717   | Layout 1 | `dfaa1dd8a47d`  |
| 2709   | Layout 1 | `dfaa1dd8a47d`  |
| 2703   | Layout 1 | `dfaa1dd8a47d`  |
| 2695   | Layout 1 | `dfaa1dd8a47d`  |
| 2684   | Layout 1 | `dfaa1dd8a47d`  |
| 2672   | Layout 1 | `dfaa1dd8a47d`  |
| 2665   | Layout 1 | `dfaa1dd8a47d`  |
| 2657   | Layout 1 | `dfaa1dd8a47d`  |
| 2649   | Layout 1 | `dfaa1dd8a47d`  |
| 2644   | Layout 1 | `dfaa1dd8a47d`  |
| 2637   | Layout 1 | `dfaa1dd8a47d`  |
| 2629   | Layout 1 | `dfaa1dd8a47d`  |
| 2619   | Layout 1 | `dfaa1dd8a47d`  |
| 2612   | Layout 1 | `dfaa1dd8a47d`  |
| 2606   | Layout 1 | `dfaa1dd8a47d`  |
| 2602   | Layout 1 | `dfaa1dd8a47d`  |
| 2601   | Layout 1 | `dfaa1dd8a47d`  |
| 2592   | Layout 1 | `dfaa1dd8a47d`  |
| 2583   | Layout 1 | `dfaa1dd8a47d`  |
| 2575   | Layout 1 | `dfaa1dd8a47d`  |
| 2567   | Layout 1 | `dfaa1dd8a47d`  |
| 2560   | Layout 1 | `dfaa1dd8a47d`  |
| 2553   | Layout 1 | `dfaa1dd8a47d`  |
| 2545   | Layout 1 | `dfaa1dd8a47d`  |
| 2538   | Layout 1 | `dfaa1dd8a47d`  |
| 2529   | Layout 1 | `dfaa1dd8a47d`  |
| 2519   | Layout 1 | `dfaa1dd8a47d`  |
| 2513   | Layout 1 | `dfaa1dd8a47d`  |
| 2510   | Layout 1 | `dfaa1dd8a47d`  |
| 2507   | Layout 1 | `dfaa1dd8a47d`  |
| 2503   | Layout 1 | `dfaa1dd8a47d`  |
| 2498   | Layout 1 | `dfaa1dd8a47d`  |
| 2492   | Layout 1 | `dfaa1dd8a47d`  |
| 2487   | Layout 1 | `dfaa1dd8a47d`  |
| 2480   | Layout 1 | `dfaa1dd8a47d`  |
| 2474   | Layout 1 | `dfaa1dd8a47d`  |
| 2468   | Layout 1 | `dfaa1dd8a47d`  |
| 2460   | Layout 1 | `dfaa1dd8a47d`  |
| 2453   | Layout 1 | `dfaa1dd8a47d`  |
| 2444   | Layout 1 | `dfaa1dd8a47d`  |
| 2438   | Layout 1 | `dfaa1dd8a47d`  |
| 2434   | Layout 1 | `dfaa1dd8a47d`  |
| 2429   | Layout 1 | `dfaa1dd8a47d`  |
| 2421   | Layout 1 | `dfaa1dd8a47d`  |
| 2414   | Layout 1 | `dfaa1dd8a47d`  |
| 2407   | Layout 1 | `dfaa1dd8a47d`  |
| 2401   | Layout 1 | `dfaa1dd8a47d`  |
| 2397   | Layout 1 | `dfaa1dd8a47d`  |
| 2393   | Layout 1 | `dfaa1dd8a47d`  |
| 2384   | Layout 1 | `dfaa1dd8a47d`  |
| 2378   | Layout 1 | `dfaa1dd8a47d`  |
| 2372   | Layout 1 | `dfaa1dd8a47d`  |
| 2358   | Layout 1 | `dfaa1dd8a47d`  |
| 2352   | Layout 1 | `dfaa1dd8a47d`  |
| 2347   | Layout 1 | `dfaa1dd8a47d`  |
| 2343   | Layout 1 | `dfaa1dd8a47d`  |
| 2335   | Layout 1 | `dfaa1dd8a47d`  |
| 2327   | Layout 1 | `dfaa1dd8a47d`  |
| 2324   | Layout 1 | `dfaa1dd8a47d`  |
| 2319   | Layout 1 | `dfaa1dd8a47d`  |
| 2313   | Layout 1 | `dfaa1dd8a47d`  |
| 2308   | Layout 1 | `dfaa1dd8a47d`  |
| 2302   | Layout 1 | `dfaa1dd8a47d`  |
| 2295   | Layout 1 | `dfaa1dd8a47d`  |
| 2290   | Layout 1 | `dfaa1dd8a47d`  |
| 2284   | Layout 1 | `dfaa1dd8a47d`  |
| 2276   | Layout 1 | `dfaa1dd8a47d`  |
| 2269   | Layout 1 | `dfaa1dd8a47d`  |
| 2259   | Layout 1 | `dfaa1dd8a47d`  |
| 2250   | Layout 1 | `dfaa1dd8a47d`  |
| 2243   | Layout 1 | `dfaa1dd8a47d`  |
| 2235   | Layout 1 | `dfaa1dd8a47d`  |
| 2229   | Layout 1 | `dfaa1dd8a47d`  |
| 2224   | Layout 1 | `dfaa1dd8a47d`  |
| 2218   | Layout 1 | `dfaa1dd8a47d`  |
| 2215   | Layout 1 | `dfaa1dd8a47d`  |
| 2207   | Layout 1 | `dfaa1dd8a47d`  |
| 2203   | Layout 1 | `dfaa1dd8a47d`  |
| 2196   | Layout 1 | `dfaa1dd8a47d`  |
| 2192   | Layout 1 | `dfaa1dd8a47d`  |
| 2189   | Layout 1 | `dfaa1dd8a47d`  |
| 2183   | Layout 1 | `dfaa1dd8a47d`  |
| 2179   | Layout 1 | `dfaa1dd8a47d`  |
| 2171   | Layout 1 | `dfaa1dd8a47d`  |
| 2163   | Layout 1 | `dfaa1dd8a47d`  |
| 2156   | Layout 1 | `dfaa1dd8a47d`  |
| 2151   | Layout 1 | `dfaa1dd8a47d`  |
| 2147   | Layout 1 | `dfaa1dd8a47d`  |
| 2142   | Layout 1 | `dfaa1dd8a47d`  |
| 2138   | Layout 1 | `dfaa1dd8a47d`  |
| 2134   | Layout 1 | `dfaa1dd8a47d`  |
| 2130   | Layout 1 | `dfaa1dd8a47d`  |
| 2122   | Layout 1 | `dfaa1dd8a47d`  |
| 2107   | Layout 1 | `dfaa1dd8a47d`  |
| 2098   | Layout 1 | `dfaa1dd8a47d`  |
| 2089   | Layout 1 | `dfaa1dd8a47d`  |
| 2081   | Layout 1 | `dfaa1dd8a47d`  |
| 2073   | Layout 1 | `dfaa1dd8a47d`  |
| 2067   | Layout 1 | `dfaa1dd8a47d`  |
| 2063   | Layout 1 | `dfaa1dd8a47d`  |
| 2059   | Layout 1 | `dfaa1dd8a47d`  |
| 2052   | Layout 1 | `dfaa1dd8a47d`  |
| 2044   | Layout 1 | `dfaa1dd8a47d`  |
| 2039   | Layout 1 | `dfaa1dd8a47d`  |
| 2032   | Layout 1 | `dfaa1dd8a47d`  |
| 2025   | Layout 1 | `dfaa1dd8a47d`  |
| 2011   | Layout 1 | `dfaa1dd8a47d`  |
| 2005   | Layout 1 | `dfaa1dd8a47d`  |
| 2000   | Layout 1 | `dfaa1dd8a47d`  |
| 1996   | Layout 1 | `dfaa1dd8a47d`  |
| 1991   | Layout 1 | `dfaa1dd8a47d`  |
| 1985   | Layout 1 | `dfaa1dd8a47d`  |
| 1980   | Layout 1 | `dfaa1dd8a47d`  |
| 1969   | Layout 1 | `dfaa1dd8a47d`  |
| 1964   | Layout 1 | `dfaa1dd8a47d`  |
| 1958   | Layout 1 | `dfaa1dd8a47d`  |
| 1950   | Layout 1 | `dfaa1dd8a47d`  |
| 1945   | Layout 1 | `dfaa1dd8a47d`  |
| 1937   | Layout 1 | `dfaa1dd8a47d`  |
| 1933   | Layout 1 | `dfaa1dd8a47d`  |
| 1927   | Layout 1 | `dfaa1dd8a47d`  |
| 1921   | Layout 1 | `dfaa1dd8a47d`  |
| 1914   | Layout 1 | `dfaa1dd8a47d`  |
| 1908   | Layout 1 | `dfaa1dd8a47d`  |
| 1897   | Layout 1 | `dfaa1dd8a47d`  |
| 1892   | Layout 1 | `dfaa1dd8a47d`  |
| 1886   | Layout 1 | `dfaa1dd8a47d`  |
| 1881   | Layout 1 | `dfaa1dd8a47d`  |
| 1871   | Layout 1 | `dfaa1dd8a47d`  |
| 1866   | Layout 1 | `dfaa1dd8a47d`  |
| 1862   | Layout 1 | `dfaa1dd8a47d`  |
| 1854   | Layout 1 | `dfaa1dd8a47d`  |
| 1846   | Layout 1 | `dfaa1dd8a47d`  |
| 1838   | Layout 1 | `dfaa1dd8a47d`  |
| 1832   | Layout 1 | `dfaa1dd8a47d`  |
| 1826   | Layout 1 | `dfaa1dd8a47d`  |
| 1822   | Layout 1 | `dfaa1dd8a47d`  |
| 1818   | Layout 1 | `dfaa1dd8a47d`  |
| 1804   | Layout 1 | `dfaa1dd8a47d`  |
| 1794   | Layout 1 | `dfaa1dd8a47d`  |
| 1790   | Layout 1 | `dfaa1dd8a47d`  |
| 1784   | Layout 1 | `dfaa1dd8a47d`  |
| 1774   | Layout 1 | `dfaa1dd8a47d`  |
| 1771   | Layout 1 | `dfaa1dd8a47d`  |
| 1762   | Layout 1 | `dfaa1dd8a47d`  |
| 1759   | Layout 1 | `dfaa1dd8a47d`  |
| 1754   | Layout 1 | `dfaa1dd8a47d`  |
| 1749   | Layout 1 | `dfaa1dd8a47d`  |
| 1743   | Layout 1 | `dfaa1dd8a47d`  |
| 1737   | Layout 1 | `dfaa1dd8a47d`  |
| 1731   | Layout 1 | `dfaa1dd8a47d`  |
| 1725   | Layout 1 | `dfaa1dd8a47d`  |
| 1717   | Layout 1 | `dfaa1dd8a47d`  |
| 1710   | Layout 1 | `dfaa1dd8a47d`  |
| 1704   | Layout 1 | `dfaa1dd8a47d`  |
| 1698   | Layout 1 | `dfaa1dd8a47d`  |
| 1690   | Layout 1 | `dfaa1dd8a47d`  |
| 1685   | Layout 1 | `dfaa1dd8a47d`  |
| 1680   | Layout 1 | `dfaa1dd8a47d`  |
| 1674   | Layout 1 | `dfaa1dd8a47d`  |
| 1668   | Layout 1 | `dfaa1dd8a47d`  |
| 1659   | Layout 1 | `dfaa1dd8a47d`  |
| 1649   | Layout 1 | `dfaa1dd8a47d`  |
| 1642   | Layout 1 | `dfaa1dd8a47d`  |
| 1636   | Layout 1 | `dfaa1dd8a47d`  |
| 1628   | Layout 1 | `dfaa1dd8a47d`  |
| 1622   | Layout 1 | `dfaa1dd8a47d`  |
| 1614   | Layout 1 | `dfaa1dd8a47d`  |
| 1608   | Layout 1 | `dfaa1dd8a47d`  |
| 1602   | Layout 1 | `dfaa1dd8a47d`  |
| 1598   | Layout 1 | `dfaa1dd8a47d`  |
| 1594   | Layout 1 | `dfaa1dd8a47d`  |
| 1590   | Layout 1 | `dfaa1dd8a47d`  |
| 1587   | Layout 1 | `dfaa1dd8a47d`  |
| 1584   | Layout 1 | `dfaa1dd8a47d`  |
| 1579   | Layout 1 | `dfaa1dd8a47d`  |
| 1572   | Layout 1 | `dfaa1dd8a47d`  |
| 1565   | Layout 1 | `dfaa1dd8a47d`  |
| 1559   | Layout 1 | `dfaa1dd8a47d`  |
| 1554   | Layout 1 | `dfaa1dd8a47d`  |
| 1547   | Layout 1 | `dfaa1dd8a47d`  |
| 1537   | Layout 1 | `dfaa1dd8a47d`  |
| 1529   | Layout 1 | `dfaa1dd8a47d`  |
| 1524   | Layout 1 | `dfaa1dd8a47d`  |
| 1519   | Layout 1 | `dfaa1dd8a47d`  |
| 1509   | Layout 1 | `dfaa1dd8a47d`  |
| 1506   | Layout 1 | `dfaa1dd8a47d`  |
| 1504   | Layout 1 | `dfaa1dd8a47d`  |
| 1500   | Layout 1 | `dfaa1dd8a47d`  |
| 1493   | Layout 1 | `dfaa1dd8a47d`  |
| 1489   | Layout 1 | `dfaa1dd8a47d`  |
| 1485   | Layout 1 | `dfaa1dd8a47d`  |
| 1481   | Layout 1 | `dfaa1dd8a47d`  |
| 1474   | Layout 1 | `dfaa1dd8a47d`  |
| 1466   | Layout 1 | `dfaa1dd8a47d`  |
| 1462   | Layout 1 | `dfaa1dd8a47d`  |
| 1459   | Layout 1 | `dfaa1dd8a47d`  |
| 1453   | Layout 1 | `dfaa1dd8a47d`  |
| 1450   | Layout 1 | `dfaa1dd8a47d`  |
| 1445   | Layout 1 | `dfaa1dd8a47d`  |
| 1439   | Layout 1 | `dfaa1dd8a47d`  |
| 1433   | Layout 1 | `dfaa1dd8a47d`  |
| 1430   | Layout 1 | `dfaa1dd8a47d`  |
| 1426   | Layout 1 | `dfaa1dd8a47d`  |
| 1421   | Layout 1 | `dfaa1dd8a47d`  |
| 1417   | Layout 1 | `dfaa1dd8a47d`  |
| 1416   | Layout 1 | `dfaa1dd8a47d`  |
| 1409   | Layout 1 | `dfaa1dd8a47d`  |
| 1405   | Layout 1 | `dfaa1dd8a47d`  |
| 1401   | Layout 1 | `dfaa1dd8a47d`  |
| 1396   | Layout 1 | `dfaa1dd8a47d`  |
| 1391   | Layout 1 | `dfaa1dd8a47d`  |
| 1390   | Layout 1 | `dfaa1dd8a47d`  |
| 1386   | Layout 1 | `dfaa1dd8a47d`  |
| 1381   | Layout 1 | `dfaa1dd8a47d`  |
| 1379   | Layout 1 | `dfaa1dd8a47d`  |
| 1372   | Layout 1 | `dfaa1dd8a47d`  |
| 1366   | Layout 1 | `dfaa1dd8a47d`  |
| 1364   | Layout 1 | `dfaa1dd8a47d`  |
| 1363   | Layout 1 | `dfaa1dd8a47d`  |
| 1360   | Layout 1 | `dfaa1dd8a47d`  |
| 1358   | Layout 1 | `dfaa1dd8a47d`  |
| 1355   | Layout 1 | `dfaa1dd8a47d`  |
| 1351   | Layout 1 | `dfaa1dd8a47d`  |
| 1348   | Layout 1 | `dfaa1dd8a47d`  |
| 1346   | Layout 1 | `dfaa1dd8a47d`  |
| 1341   | Layout 1 | `dfaa1dd8a47d`  |
| 1340   | Layout 1 | `dfaa1dd8a47d`  |
| 1338   | Layout 1 | `dfaa1dd8a47d`  |
| 1335   | Layout 1 | `dfaa1dd8a47d`  |
| 1333   | Layout 1 | `dfaa1dd8a47d`  |
| 1329   | Layout 1 | `dfaa1dd8a47d`  |
| 1327   | Layout 1 | `dfaa1dd8a47d`  |
| 1324   | Layout 1 | `dfaa1dd8a47d`  |
| 1321   | Layout 1 | `dfaa1dd8a47d`  |
| 1319   | Layout 1 | `dfaa1dd8a47d`  |
| 1318   | Layout 1 | `dfaa1dd8a47d`  |
| 1316   | Layout 1 | `dfaa1dd8a47d`  |
| 1313   | Layout 1 | `dfaa1dd8a47d`  |
| 1311   | Layout 1 | `dfaa1dd8a47d`  |
| 1309   | Layout 1 | `dfaa1dd8a47d`  |
| 1304   | Layout 1 | `dfaa1dd8a47d`  |
| 1292   | Layout 1 | `dfaa1dd8a47d`  |
| 1286   | Layout 1 | `dfaa1dd8a47d`  |
| 1280   | No file  | `dfaa1dd8a47d`  |
| 1276   | No file  | `dfaa1dd8a47d`  |
| 1267   | Layout 1 | `dfaa1dd8a47d`  |
| 1261   | Layout 1 | `dfaa1dd8a47d`  |
| 1256   | No file  | `dfaa1dd8a47d`  |
| 1250   | No file  | `dfaa1dd8a47d`  |
| 1246   | No file  | `dfaa1dd8a47d`  |
| 1239   | No file  | `dfaa1dd8a47d`  |
| 1230   | No file  | `dfaa1dd8a47d`  |
| 1226   | No file  | `dfaa1dd8a47d`  |
| 1220   | No file  | `dfaa1dd8a47d`  |
| 1217   | No file  | `dfaa1dd8a47d`  |
| 1211   | No file  | `dfaa1dd8a47d`  |
| 1210   | No file  | `dfaa1dd8a47d`  |
| 1208   | No file  | `dfaa1dd8a47d`  |
| 1203   | No file  | `dfaa1dd8a47d`  |
| 1197   | No file  | `dfaa1dd8a47d`  |
| 1194   | No file  | `dfaa1dd8a47d`  |
| 1192   | No file  | `dfaa1dd8a47d`  |
| 1187   | No file  | `dfaa1dd8a47d`  |
| 1183   | No file  | `dfaa1dd8a47d`  |
| 1177   | No file  | `dfaa1dd8a47d`  |
| 1173   | No file  | `dfaa1dd8a47d`  |
| 1167   | No file  | `dfaa1dd8a47d`  |
| 1164   | No file  | `dfaa1dd8a47d`  |
| 1156   | No file  | `dfaa1dd8a47d`  |
| 1149   | No file  | `dfaa1dd8a47d`  |
| 1144   | No file  | `dfaa1dd8a47d`  |
| 1137   | No file  | `dfaa1dd8a47d`  |
| 1132   | No file  | `dfaa1dd8a47d`  |
| 1127   | No file  | `dfaa1dd8a47d`  |
| 1122   | No file  | `dfaa1dd8a47d`  |
| 1118   | No file  | `dfaa1dd8a47d`  |
| 1114   | No file  | `dfaa1dd8a47d`  |
| 1109   | No file  | `dfaa1dd8a47d`  |
| 1102   | No file  | `dfaa1dd8a47d`  |
| 1096   | No file  | `dfaa1dd8a47d`  |
| 1088   | No file  | `dfaa1dd8a47d`  |
| 1081   | No file  | `dfaa1dd8a47d`  |
| 1076   | No file  | `dfaa1dd8a47d`  |
| 1069   | No file  | `dfaa1dd8a47d`  |
| 1064   | No file  | `dfaa1dd8a47d`  |
| 1058   | No file  | `dfaa1dd8a47d`  |
| 1051   | No file  | `dfaa1dd8a47d`  |
| 1044   | No file  | `dfaa1dd8a47d`  |
| 1036   | No file  | `dfaa1dd8a47d`  |
| 1026   | No file  | `dfaa1dd8a47d`  |
| 1016   | No file  | `dfaa1dd8a47d`  |
| 1009   | No file  | `dfaa1dd8a47d`  |
| 1005   | No file  | `dfaa1dd8a47d`  |
| 1000   | No file  | `dfaa1dd8a47d`  |
| 998    | No file  | `dfaa1dd8a47d`  |
| 990    | No file  | `dfaa1dd8a47d`  |
| 979    | No file  | `dfaa1dd8a47d`  |
| 972    | No file  | `dfaa1dd8a47d`  |
| 963    | No file  | `dfaa1dd8a47d`  |
| 955    | No file  | `dfaa1dd8a47d`  |
| 946    | No file  | `dfaa1dd8a47d`  |
| 938    | No file  | `dfaa1dd8a47d`  |
| 927    | No file  | `dfaa1dd8a47d`  |
| 911    | No file  | `dfaa1dd8a47d`  |
| 904    | No file  | `dfaa1dd8a47d`  |
| 899    | No file  | `dfaa1dd8a47d`  |
| 894    | No file  | `dfaa1dd8a47d`  |
| 885    | No file  | `dfaa1dd8a47d`  |
| 879    | No file  | `dfaa1dd8a47d`  |
| 872    | No file  | `dfaa1dd8a47d`  |
| 864    | No file  | `dfaa1dd8a47d`  |
| 855    | No file  | `dfaa1dd8a47d`  |
| 853    | No file  | `dfaa1dd8a47d`  |
| 845    | No file  | `dfaa1dd8a47d`  |
| 837    | No file  | `dfaa1dd8a47d`  |
| 829    | No file  | `dfaa1dd8a47d`  |
| 822    | No file  | `dfaa1dd8a47d`  |
| 814    | No file  | `dfaa1dd8a47d`  |
| 805    | No file  | `dfaa1dd8a47d`  |
| 794    | No file  | `dfaa1dd8a47d`  |
| 787    | No file  | `dfaa1dd8a47d`  |
| 780    | No file  | `dfaa1dd8a47d`  |
| 771    | No file  | `dfaa1dd8a47d`  |
| 760    | No file  | `dfaa1dd8a47d`  |
| 748    | No file  | `dfaa1dd8a47d`  |
| 741    | No file  | `dfaa1dd8a47d`  |
| 736    | No file  | `dfaa1dd8a47d`  |
| 731    | No file  | `dfaa1dd8a47d`  |
| 723    | No file  | `dfaa1dd8a47d`  |
| 711    | No file  | `dfaa1dd8a47d`  |
| 707    | No file  | `dfaa1dd8a47d`  |
| 697    | No file  | `dfaa1dd8a47d`  |
| 689    | No file  | `dfaa1dd8a47d`  |
| 683    | No file  | `dfaa1dd8a47d`  |
| 678    | No file  | `dfaa1dd8a47d`  |
| 670    | No file  | `dfaa1dd8a47d`  |
| 661    | No file  | `dfaa1dd8a47d`  |
| 656    | No file  | `dfaa1dd8a47d`  |
| 652    | No file  | `dfaa1dd8a47d`  |
| 643    | No file  | `dfaa1dd8a47d`  |
| 637    | No file  | `dfaa1dd8a47d`  |
| 630    | No file  | `dfaa1dd8a47d`  |
| 627    | No file  | `dfaa1dd8a47d`  |
| 621    | No file  | `dfaa1dd8a47d`  |
| 617    | No file  | `dfaa1dd8a47d`  |
| 615    | No file  | `dfaa1dd8a47d`  |
| 606    | No file  | `dfaa1dd8a47d`  |
| 599    | No file  | `dfaa1dd8a47d`  |
| 592    | No file  | `dfaa1dd8a47d`  |
| 586    | No file  | `dfaa1dd8a47d`  |
| 577    | No file  | `dfaa1dd8a47d`  |
| 569    | No file  | `dfaa1dd8a47d`  |
| 561    | No file  | `dfaa1dd8a47d`  |
| 554    | No file  | `dfaa1dd8a47d`  |
| 542    | No file  | `dfaa1dd8a47d`  |
| 532    | No file  | `dfaa1dd8a47d`  |
| 531    | No file  | `dfaa1dd8a47d`  |
| 526    | No file  | `dfaa1dd8a47d`  |
| 521    | No file  | `dfaa1dd8a47d`  |
| 517    | No file  | `dfaa1dd8a47d`  |
| 510    | No file  | `dfaa1dd8a47d`  |
| 508    | No file  | `dfaa1dd8a47d`  |
| 504    | No file  | `dfaa1dd8a47d`  |
| 497    | No file  | `dfaa1dd8a47d`  |
| 491    | No file  | `dfaa1dd8a47d`  |
| 485    | No file  | `dfaa1dd8a47d`  |
| 478    | No file  | `dfaa1dd8a47d`  |
| 472    | No file  | `dfaa1dd8a47d`  |
| 466    | No file  | `dfaa1dd8a47d`  |
| 457    | No file  | `dfaa1dd8a47d`  |
| 452    | No file  | `dfaa1dd8a47d`  |
| 449    | No file  | `dfaa1dd8a47d`  |
| 435    | No file  | `dfaa1dd8a47d`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                                     |
| ---------------------- | -------- | ------------------------------------------------------------------------ |
| `petpcroomoffset.dbss` | Optional | `pet_id -> (offset, size)` of every row; the parser walks the main file without it |
| `petequipskill.bss`    | Optional | `equip_skill_id -> skill_no`, for the skill names (LOC type 10)          |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 10 x 14 = 144 bytes on client 3474.

### Row (14 bytes)

| Offset  | Type | Field            | Notes                                                                        |
| ------- | ---- | ---------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id           | Row key; the `pet_id` of a [`pet.dbss`](pet_dbss.md) record                  |
| `+0x02` | u32  | equip_skill_id_0 | Section 1 `equip_skill_id` of [`petequipskill.bss`](petequipskill_bss.md)    |
| `+0x06` | u32  | equip_skill_id_1 | Section 1 `equip_skill_id` of `petequipskill.bss`                            |
| `+0x0A` | u32  | equip_skill_id_2 | Section 1 `equip_skill_id` of `petequipskill.bss`                            |

The rows have no padding: the client 1784 server loader fills a 24-byte
entry with the key at `+0x00` and the three skill ids at `+0x04`, `+0x08`
and `+0x0C`, and the file packs those members back to back.

### `petpcroomoffset.dbss`

Bare offset table into `petpcroom.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `petpcroom.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (10 bytes)

| Offset  | Type | Field  | Notes                                                                 |
| ------- | ---- | ------ | --------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id | Key of the row it points at                                           |
| `+0x02` | u32  | offset | Absolute byte offset of the row in `petpcroom.dbss`, at its `pet_id`  |
| `+0x06` | u32  | size   | The whole row: always `14`                                            |

Both files list the keys in the same order: 55663 first, then 55672 down
to 55664. The offset points at the row's own key, as in
[`petdetectposition.dbss`](petdetectposition_dbss.md).

## PC Room Pets

On client 3474 the ten rows key the pets `55663` to `55672`, one each of
ten species (Puppy, Red Panda, Panda, Polar Bear, Desert Fox, Young
Griffon, Newborn Crimson Dragon, Hawk, Hedgehog, Cat), all `tier` `3` and
all with `pc_room_type` `1` in `pet.dbss`. `pet.dbss` sets `pc_room_type`
on ten more pets, `56572` to `56581` (`tier` `4`, the same ten species),
which have no row here; they are not in the client 1784 `Pet_Table` sheet.

Every row has `equip_skill_id_0` `4` (Combat EXP +5%). `equip_skill_id_1`
is `41` (Skill EXP +5%), `38` (Life EXP +5%), `39` (Weight Limit +50 LT)
or `13` (Death Penalty Resistance +4%), and `equip_skill_id_2` one of
`9`, `10`, `11`, `13`, `40`, `41`, `42`. The names are the LOC type 10
names of the catalog's `skill_no` (client 3474).

## Field Names

The `Pet_PcRoom_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CharacterKey`, `Skillindex_0`, `Skillindex_1`
and `Skillindex_2`, and its 10 rows match the file on all 10 keys and all
three skill columns (clients 1784 and 3474). The developer workbook
(`datasheet_petdatatable.xlsm`) adds note columns: `#CharName` names each
pet with a `_PC방` (PC room) suffix (`반려동물_황백 악동개_T4_PC방` for
`55663`), and `#SkillName_0` to `#SkillName_2` name each skill index with
the skill Section 1 of `petequipskill.bss` holds at that `equip_skill_id`
(`전투 경험치 +5%`, combat EXP +5%, for `4`; `행운 1단계`, luck level 1,
for `9`). `CharacterKey` is the `pet.dbss` key, named `pet_id` there.

The client 1784 server dump names the type `gc::PetPcRoomStaticStatus`,
held in a `BinaryUnorderedMap` keyed by `KeyType<unsigned short>`, with the
manager `PetPcRoomStaticStatusManager`. Its sheet loader (VA `0x14086f440`)
reads `CharacterKey` with `ReadCellInt` and keeps the low u16 at `+0x00`,
then formats `Skillindex_%#` for indexes 0 to 2 and reads each with
`ReadCellInt` into a 4-byte slot at `+0x04`, `+0x08` and `+0x0C`. Each slot
starts at `43` (`0x2B`) before the read, one past the last Section 1
`equip_skill_id`. The 2016 client's debug symbols and the client 519
server tables have no PC room pet type.

## Notes

- Clients 1485, 1784, 2107, 2519, 3002, 3251 and 3474 have the same
  144-byte file and 104-byte offset file, byte for byte. Clients 794 and
  1230 have neither file. The private server's own compiled
  `petpcroom.dbss` and `petpcroomoffset.dbss` (client 1784) are the same
  bytes as the client files.
- `pet.dbss` gives all 20 PC room pets `acquire_type_id` `0`, the same
  roll group as 344 other pets (client 3474), so the roll tables in
  [`petequipskillaquire.dbss`](petequipskillaquire_dbss.md) do not single
  them out.
- The client Lua of the pet list (`panel_window_petlist_all`) shows the
  PC room parts only in a premium PC room with the content group
  `_ContentsGroup_PcRoomPet`: it adds `ToClient_getPetUseMaxCountPcRoom()`
  to the summon limit, filters pets by `getPetStaticStatus():isOnlyPcRoom()`
  and registers the pets with `ToClient_requestPetForPcRoomRegister()`. No
  client Lua reads the skill indexes.
- The NA/EU LOC (client 3474) has no PC room pet text; the pet names in the
  PC Room Pets section are the LOC type 6 names of the pet keys.

## Open Questions

### How the Server Applies the Three Skills

The rows give each PC room pet three fixed equip skills, while other pets
roll theirs from `petequipskillaquire.dbss`. Whether the server gives the
three skills in place of a roll or on top of it, and why the second set of
PC room pets (`56572` to `56581`) has no row, cannot be read from the
client data.
