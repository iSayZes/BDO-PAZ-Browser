# `possiblefusionpet.bss` Format

## Purpose

The pets a pet exchange can give, grouped by fusion key: each row is one
fusion key (variant, species and tier, the four bytes `pet.dbss` stores at
payload `+0x02`) and one [`pet.dbss`](../dbss/pet_dbss.md) `pet_id` with that key.
The rows are sorted by the fusion key read as a u32, so the pets of one key
sit together. The file has no PABR magic and no trailer.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                    | Bytes | Records   | Row bytes |
| ------ | -------------- | ----------------------- | ----- | --------- | --------- |
| 1      | 1226 and later | `possiblefusionpet.bss` | 7,726 | 1,287 Row | 6         |

| Layout | File                    | Known           | Unknown         |
| ------ | ----------------------- | --------------- | --------------- |
| 1      | `possiblefusionpet.bss` | 6,439 B (83.3%) | 1,287 B (16.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `1add4de5ad1e`  |
| 3482   | Layout 1 | `1add4de5ad1e`  |
| 3474   | Layout 1 | `1add4de5ad1e`  |
| 3473   | Layout 1 | `1add4de5ad1e`  |
| 3464   | Layout 1 | `1add4de5ad1e`  |
| 3458   | Layout 1 | `1add4de5ad1e`  |
| 3454   | Layout 1 | `1add4de5ad1e`  |
| 3444   | Layout 1 | `1add4de5ad1e`  |
| 3435   | Layout 1 | `1add4de5ad1e`  |
| 3426   | Layout 1 | `1add4de5ad1e`  |
| 3418   | Layout 1 | `1add4de5ad1e`  |
| 3412   | Layout 1 | `1add4de5ad1e`  |
| 3402   | Layout 1 | `1add4de5ad1e`  |
| 3396   | Layout 1 | `1add4de5ad1e`  |
| 3387   | Layout 1 | `1add4de5ad1e`  |
| 3381   | Layout 1 | `1add4de5ad1e`  |
| 3373   | Layout 1 | `1add4de5ad1e`  |
| 3364   | Layout 1 | `1add4de5ad1e`  |
| 3356   | Layout 1 | `1add4de5ad1e`  |
| 3349   | Layout 1 | `1add4de5ad1e`  |
| 3342   | Layout 1 | `1add4de5ad1e`  |
| 3335   | Layout 1 | `1add4de5ad1e`  |
| 3326   | Layout 1 | `1add4de5ad1e`  |
| 3321   | Layout 1 | `1add4de5ad1e`  |
| 3314   | Layout 1 | `1add4de5ad1e`  |
| 3303   | Layout 1 | `1add4de5ad1e`  |
| 3302   | Layout 1 | `1add4de5ad1e`  |
| 3293   | Layout 1 | `1add4de5ad1e`  |
| 3283   | Layout 1 | `1add4de5ad1e`  |
| 3275   | Layout 1 | `1add4de5ad1e`  |
| 3267   | Layout 1 | `1add4de5ad1e`  |
| 3258   | Layout 1 | `1add4de5ad1e`  |
| 3251   | Layout 1 | `1add4de5ad1e`  |
| 3242   | Layout 1 | `1add4de5ad1e`  |
| 3235   | Layout 1 | `1add4de5ad1e`  |
| 3229   | Layout 1 | `1add4de5ad1e`  |
| 3212   | Layout 1 | `1add4de5ad1e`  |
| 3203   | Layout 1 | `1add4de5ad1e`  |
| 3193   | Layout 1 | `1add4de5ad1e`  |
| 3186   | Layout 1 | `1add4de5ad1e`  |
| 3177   | Layout 1 | `1add4de5ad1e`  |
| 3169   | Layout 1 | `1add4de5ad1e`  |
| 3158   | Layout 1 | `1add4de5ad1e`  |
| 3151   | Layout 1 | `1add4de5ad1e`  |
| 3144   | Layout 1 | `1add4de5ad1e`  |
| 3133   | Layout 1 | `1add4de5ad1e`  |
| 3125   | Layout 1 | `1add4de5ad1e`  |
| 3118   | Layout 1 | `1add4de5ad1e`  |
| 3111   | Layout 1 | `1add4de5ad1e`  |
| 3103   | Layout 1 | `1add4de5ad1e`  |
| 3095   | Layout 1 | `1add4de5ad1e`  |
| 3086   | Layout 1 | `1add4de5ad1e`  |
| 3072   | Layout 1 | `1add4de5ad1e`  |
| 3062   | Layout 1 | `1add4de5ad1e`  |
| 3052   | Layout 1 | `1add4de5ad1e`  |
| 3045   | Layout 1 | `1add4de5ad1e`  |
| 3037   | Layout 1 | `1add4de5ad1e`  |
| 3030   | Layout 1 | `1add4de5ad1e`  |
| 3021   | Layout 1 | `1add4de5ad1e`  |
| 3012   | Layout 1 | `1add4de5ad1e`  |
| 3002   | Layout 1 | `1add4de5ad1e`  |
| 2995   | Layout 1 | `1add4de5ad1e`  |
| 2987   | Layout 1 | `1add4de5ad1e`  |
| 2978   | Layout 1 | `1add4de5ad1e`  |
| 2970   | Layout 1 | `1add4de5ad1e`  |
| 2959   | Layout 1 | `1add4de5ad1e`  |
| 2951   | Layout 1 | `1add4de5ad1e`  |
| 2942   | Layout 1 | `1add4de5ad1e`  |
| 2935   | Layout 1 | `1add4de5ad1e`  |
| 2932   | Layout 1 | `1add4de5ad1e`  |
| 2923   | Layout 1 | `1add4de5ad1e`  |
| 2919   | Layout 1 | `1add4de5ad1e`  |
| 2907   | Layout 1 | `1add4de5ad1e`  |
| 2900   | Layout 1 | `1add4de5ad1e`  |
| 2891   | Layout 1 | `1add4de5ad1e`  |
| 2882   | Layout 1 | `1add4de5ad1e`  |
| 2872   | Layout 1 | `1add4de5ad1e`  |
| 2863   | Layout 1 | `1add4de5ad1e`  |
| 2855   | Layout 1 | `1add4de5ad1e`  |
| 2849   | Layout 1 | `1add4de5ad1e`  |
| 2844   | Layout 1 | `1add4de5ad1e`  |
| 2834   | Layout 1 | `1add4de5ad1e`  |
| 2825   | Layout 1 | `1add4de5ad1e`  |
| 2819   | Layout 1 | `1add4de5ad1e`  |
| 2811   | Layout 1 | `1add4de5ad1e`  |
| 2803   | Layout 1 | `1add4de5ad1e`  |
| 2794   | Layout 1 | `1add4de5ad1e`  |
| 2783   | Layout 1 | `1add4de5ad1e`  |
| 2774   | Layout 1 | `1add4de5ad1e`  |
| 2765   | Layout 1 | `1add4de5ad1e`  |
| 2756   | Layout 1 | `1add4de5ad1e`  |
| 2750   | Layout 1 | `1add4de5ad1e`  |
| 2743   | Layout 1 | `1add4de5ad1e`  |
| 2736   | Layout 1 | `1add4de5ad1e`  |
| 2726   | Layout 1 | `1add4de5ad1e`  |
| 2717   | Layout 1 | `1add4de5ad1e`  |
| 2709   | Layout 1 | `1add4de5ad1e`  |
| 2703   | Layout 1 | `1add4de5ad1e`  |
| 2695   | Layout 1 | `1add4de5ad1e`  |
| 2684   | Layout 1 | `1add4de5ad1e`  |
| 2672   | Layout 1 | `1add4de5ad1e`  |
| 2665   | Layout 1 | `1add4de5ad1e`  |
| 2657   | Layout 1 | `1add4de5ad1e`  |
| 2649   | Layout 1 | `1add4de5ad1e`  |
| 2644   | Layout 1 | `1add4de5ad1e`  |
| 2637   | Layout 1 | `1add4de5ad1e`  |
| 2629   | Layout 1 | `1add4de5ad1e`  |
| 2619   | Layout 1 | `1add4de5ad1e`  |
| 2612   | Layout 1 | `1add4de5ad1e`  |
| 2606   | Layout 1 | `1add4de5ad1e`  |
| 2602   | Layout 1 | `1add4de5ad1e`  |
| 2601   | Layout 1 | `1add4de5ad1e`  |
| 2592   | Layout 1 | `1add4de5ad1e`  |
| 2583   | Layout 1 | `1add4de5ad1e`  |
| 2575   | Layout 1 | `1add4de5ad1e`  |
| 2567   | Layout 1 | `1add4de5ad1e`  |
| 2560   | Layout 1 | `1add4de5ad1e`  |
| 2553   | Layout 1 | `1add4de5ad1e`  |
| 2545   | Layout 1 | `1add4de5ad1e`  |
| 2538   | Layout 1 | `1add4de5ad1e`  |
| 2529   | Layout 1 | `1add4de5ad1e`  |
| 2519   | Layout 1 | `1add4de5ad1e`  |
| 2513   | Layout 1 | `1add4de5ad1e`  |
| 2510   | Layout 1 | `1add4de5ad1e`  |
| 2507   | Layout 1 | `1add4de5ad1e`  |
| 2503   | Layout 1 | `1add4de5ad1e`  |
| 2498   | Layout 1 | `1add4de5ad1e`  |
| 2492   | Layout 1 | `1add4de5ad1e`  |
| 2487   | Layout 1 | `1add4de5ad1e`  |
| 2480   | Layout 1 | `1add4de5ad1e`  |
| 2474   | Layout 1 | `1add4de5ad1e`  |
| 2468   | Layout 1 | `1add4de5ad1e`  |
| 2460   | Layout 1 | `1add4de5ad1e`  |
| 2453   | Layout 1 | `1add4de5ad1e`  |
| 2444   | Layout 1 | `1add4de5ad1e`  |
| 2438   | Layout 1 | `1add4de5ad1e`  |
| 2434   | Layout 1 | `1add4de5ad1e`  |
| 2429   | Layout 1 | `1add4de5ad1e`  |
| 2421   | Layout 1 | `1add4de5ad1e`  |
| 2414   | Layout 1 | `1add4de5ad1e`  |
| 2407   | Layout 1 | `1add4de5ad1e`  |
| 2401   | Layout 1 | `1add4de5ad1e`  |
| 2397   | Layout 1 | `1add4de5ad1e`  |
| 2393   | Layout 1 | `1add4de5ad1e`  |
| 2384   | Layout 1 | `1add4de5ad1e`  |
| 2378   | Layout 1 | `1add4de5ad1e`  |
| 2372   | Layout 1 | `1add4de5ad1e`  |
| 2358   | Layout 1 | `1add4de5ad1e`  |
| 2352   | Layout 1 | `1add4de5ad1e`  |
| 2347   | Layout 1 | `1add4de5ad1e`  |
| 2343   | Layout 1 | `1add4de5ad1e`  |
| 2335   | Layout 1 | `1add4de5ad1e`  |
| 2327   | Layout 1 | `1add4de5ad1e`  |
| 2324   | Layout 1 | `1add4de5ad1e`  |
| 2319   | Layout 1 | `1add4de5ad1e`  |
| 2313   | Layout 1 | `1add4de5ad1e`  |
| 2308   | Layout 1 | `1add4de5ad1e`  |
| 2302   | Layout 1 | `1add4de5ad1e`  |
| 2295   | Layout 1 | `1add4de5ad1e`  |
| 2290   | Layout 1 | `1add4de5ad1e`  |
| 2284   | Layout 1 | `1add4de5ad1e`  |
| 2276   | Layout 1 | `1add4de5ad1e`  |
| 2269   | Layout 1 | `1add4de5ad1e`  |
| 2259   | Layout 1 | `1add4de5ad1e`  |
| 2250   | Layout 1 | `1add4de5ad1e`  |
| 2243   | Layout 1 | `1add4de5ad1e`  |
| 2235   | Layout 1 | `1add4de5ad1e`  |
| 2229   | Layout 1 | `1add4de5ad1e`  |
| 2224   | Layout 1 | `1add4de5ad1e`  |
| 2218   | Layout 1 | `1add4de5ad1e`  |
| 2215   | Layout 1 | `1add4de5ad1e`  |
| 2207   | Layout 1 | `1add4de5ad1e`  |
| 2203   | Layout 1 | `1add4de5ad1e`  |
| 2196   | Layout 1 | `1add4de5ad1e`  |
| 2192   | Layout 1 | `1add4de5ad1e`  |
| 2189   | Layout 1 | `1add4de5ad1e`  |
| 2183   | Layout 1 | `1add4de5ad1e`  |
| 2179   | Layout 1 | `1add4de5ad1e`  |
| 2171   | Layout 1 | `1add4de5ad1e`  |
| 2163   | Layout 1 | `1add4de5ad1e`  |
| 2156   | Layout 1 | `1add4de5ad1e`  |
| 2151   | Layout 1 | `1add4de5ad1e`  |
| 2147   | Layout 1 | `1add4de5ad1e`  |
| 2142   | Layout 1 | `1add4de5ad1e`  |
| 2138   | Layout 1 | `1add4de5ad1e`  |
| 2134   | Layout 1 | `1add4de5ad1e`  |
| 2130   | Layout 1 | `1add4de5ad1e`  |
| 2122   | Layout 1 | `1add4de5ad1e`  |
| 2107   | Layout 1 | `1add4de5ad1e`  |
| 2098   | Layout 1 | `1add4de5ad1e`  |
| 2089   | Layout 1 | `1add4de5ad1e`  |
| 2081   | Layout 1 | `1add4de5ad1e`  |
| 2073   | Layout 1 | `1add4de5ad1e`  |
| 2067   | Layout 1 | `1add4de5ad1e`  |
| 2063   | Layout 1 | `1add4de5ad1e`  |
| 2059   | Layout 1 | `1add4de5ad1e`  |
| 2052   | Layout 1 | `1add4de5ad1e`  |
| 2044   | Layout 1 | `1add4de5ad1e`  |
| 2039   | Layout 1 | `1add4de5ad1e`  |
| 2032   | Layout 1 | `1add4de5ad1e`  |
| 2025   | Layout 1 | `1add4de5ad1e`  |
| 2011   | Layout 1 | `1add4de5ad1e`  |
| 2005   | Layout 1 | `1add4de5ad1e`  |
| 2000   | Layout 1 | `1add4de5ad1e`  |
| 1996   | Layout 1 | `1add4de5ad1e`  |
| 1991   | Layout 1 | `1add4de5ad1e`  |
| 1985   | Layout 1 | `1add4de5ad1e`  |
| 1980   | Layout 1 | `1add4de5ad1e`  |
| 1969   | Layout 1 | `1add4de5ad1e`  |
| 1964   | Layout 1 | `1add4de5ad1e`  |
| 1958   | Layout 1 | `1add4de5ad1e`  |
| 1950   | Layout 1 | `1add4de5ad1e`  |
| 1945   | Layout 1 | `1add4de5ad1e`  |
| 1937   | Layout 1 | `1add4de5ad1e`  |
| 1933   | Layout 1 | `1add4de5ad1e`  |
| 1927   | Layout 1 | `1add4de5ad1e`  |
| 1921   | Layout 1 | `1add4de5ad1e`  |
| 1914   | Layout 1 | `1add4de5ad1e`  |
| 1908   | Layout 1 | `1add4de5ad1e`  |
| 1897   | Layout 1 | `1add4de5ad1e`  |
| 1892   | Layout 1 | `1add4de5ad1e`  |
| 1886   | Layout 1 | `1add4de5ad1e`  |
| 1881   | Layout 1 | `1add4de5ad1e`  |
| 1871   | Layout 1 | `1add4de5ad1e`  |
| 1866   | Layout 1 | `1add4de5ad1e`  |
| 1862   | Layout 1 | `1add4de5ad1e`  |
| 1854   | Layout 1 | `1add4de5ad1e`  |
| 1846   | Layout 1 | `1add4de5ad1e`  |
| 1838   | Layout 1 | `1add4de5ad1e`  |
| 1832   | Layout 1 | `1add4de5ad1e`  |
| 1826   | Layout 1 | `1add4de5ad1e`  |
| 1822   | Layout 1 | `1add4de5ad1e`  |
| 1818   | Layout 1 | `1add4de5ad1e`  |
| 1804   | Layout 1 | `1add4de5ad1e`  |
| 1794   | Layout 1 | `1add4de5ad1e`  |
| 1790   | Layout 1 | `1add4de5ad1e`  |
| 1784   | Layout 1 | `1add4de5ad1e`  |
| 1774   | Layout 1 | `1add4de5ad1e`  |
| 1771   | Layout 1 | `1add4de5ad1e`  |
| 1762   | Layout 1 | `1add4de5ad1e`  |
| 1759   | Layout 1 | `1add4de5ad1e`  |
| 1754   | Layout 1 | `1add4de5ad1e`  |
| 1749   | Layout 1 | `1add4de5ad1e`  |
| 1743   | Layout 1 | `1add4de5ad1e`  |
| 1737   | Layout 1 | `1add4de5ad1e`  |
| 1731   | Layout 1 | `1add4de5ad1e`  |
| 1725   | Layout 1 | `1add4de5ad1e`  |
| 1717   | Layout 1 | `1add4de5ad1e`  |
| 1710   | Layout 1 | `1add4de5ad1e`  |
| 1704   | Layout 1 | `1add4de5ad1e`  |
| 1698   | Layout 1 | `1add4de5ad1e`  |
| 1690   | Layout 1 | `1add4de5ad1e`  |
| 1685   | Layout 1 | `1add4de5ad1e`  |
| 1680   | Layout 1 | `1add4de5ad1e`  |
| 1674   | Layout 1 | `1add4de5ad1e`  |
| 1668   | Layout 1 | `1add4de5ad1e`  |
| 1659   | Layout 1 | `1add4de5ad1e`  |
| 1649   | Layout 1 | `1add4de5ad1e`  |
| 1642   | Layout 1 | `1add4de5ad1e`  |
| 1636   | Layout 1 | `1add4de5ad1e`  |
| 1628   | Layout 1 | `1add4de5ad1e`  |
| 1622   | Layout 1 | `1add4de5ad1e`  |
| 1614   | Layout 1 | `1add4de5ad1e`  |
| 1608   | Layout 1 | `1add4de5ad1e`  |
| 1602   | Layout 1 | `1add4de5ad1e`  |
| 1598   | Layout 1 | `1add4de5ad1e`  |
| 1594   | Layout 1 | `1add4de5ad1e`  |
| 1590   | Layout 1 | `1add4de5ad1e`  |
| 1587   | Layout 1 | `1add4de5ad1e`  |
| 1584   | Layout 1 | `1add4de5ad1e`  |
| 1579   | Layout 1 | `1add4de5ad1e`  |
| 1572   | Layout 1 | `1add4de5ad1e`  |
| 1565   | Layout 1 | `1add4de5ad1e`  |
| 1559   | Layout 1 | `1add4de5ad1e`  |
| 1554   | Layout 1 | `1add4de5ad1e`  |
| 1547   | Layout 1 | `1add4de5ad1e`  |
| 1537   | Layout 1 | `1add4de5ad1e`  |
| 1529   | Layout 1 | `1add4de5ad1e`  |
| 1524   | Layout 1 | `1add4de5ad1e`  |
| 1519   | Layout 1 | `1add4de5ad1e`  |
| 1509   | Layout 1 | `1add4de5ad1e`  |
| 1506   | Layout 1 | `1add4de5ad1e`  |
| 1504   | Layout 1 | `1add4de5ad1e`  |
| 1500   | Layout 1 | `1add4de5ad1e`  |
| 1493   | Layout 1 | `1add4de5ad1e`  |
| 1489   | Layout 1 | `1add4de5ad1e`  |
| 1485   | Layout 1 | `1add4de5ad1e`  |
| 1481   | Layout 1 | `1add4de5ad1e`  |
| 1474   | Layout 1 | `1add4de5ad1e`  |
| 1466   | Layout 1 | `1add4de5ad1e`  |
| 1462   | Layout 1 | `1add4de5ad1e`  |
| 1459   | Layout 1 | `1add4de5ad1e`  |
| 1453   | Layout 1 | `1add4de5ad1e`  |
| 1450   | Layout 1 | `1add4de5ad1e`  |
| 1445   | Layout 1 | `1add4de5ad1e`  |
| 1439   | Layout 1 | `1add4de5ad1e`  |
| 1433   | Layout 1 | `1add4de5ad1e`  |
| 1430   | Layout 1 | `1add4de5ad1e`  |
| 1426   | Layout 1 | `1add4de5ad1e`  |
| 1421   | Layout 1 | `1add4de5ad1e`  |
| 1417   | Layout 1 | `1add4de5ad1e`  |
| 1416   | Layout 1 | `1add4de5ad1e`  |
| 1409   | Layout 1 | `1add4de5ad1e`  |
| 1405   | Layout 1 | `1add4de5ad1e`  |
| 1401   | Layout 1 | `1add4de5ad1e`  |
| 1396   | Layout 1 | `1add4de5ad1e`  |
| 1391   | Layout 1 | `1add4de5ad1e`  |
| 1390   | Layout 1 | `1add4de5ad1e`  |
| 1386   | Layout 1 | `1add4de5ad1e`  |
| 1381   | Layout 1 | `1add4de5ad1e`  |
| 1379   | Layout 1 | `1add4de5ad1e`  |
| 1372   | Layout 1 | `1add4de5ad1e`  |
| 1366   | Layout 1 | `1add4de5ad1e`  |
| 1364   | Layout 1 | `1add4de5ad1e`  |
| 1363   | Layout 1 | `1add4de5ad1e`  |
| 1360   | Layout 1 | `1add4de5ad1e`  |
| 1358   | Layout 1 | `1add4de5ad1e`  |
| 1355   | Layout 1 | `1add4de5ad1e`  |
| 1351   | Layout 1 | `1add4de5ad1e`  |
| 1348   | Layout 1 | `1add4de5ad1e`  |
| 1346   | Layout 1 | `1add4de5ad1e`  |
| 1341   | Layout 1 | `1add4de5ad1e`  |
| 1340   | Layout 1 | `1add4de5ad1e`  |
| 1338   | Layout 1 | `1add4de5ad1e`  |
| 1335   | Layout 1 | `1add4de5ad1e`  |
| 1333   | Layout 1 | `1add4de5ad1e`  |
| 1329   | Layout 1 | `1add4de5ad1e`  |
| 1327   | Layout 1 | `1add4de5ad1e`  |
| 1324   | Layout 1 | `1add4de5ad1e`  |
| 1321   | Layout 1 | `1add4de5ad1e`  |
| 1319   | Layout 1 | `1add4de5ad1e`  |
| 1318   | Layout 1 | `1add4de5ad1e`  |
| 1316   | Layout 1 | `1add4de5ad1e`  |
| 1313   | Layout 1 | `1add4de5ad1e`  |
| 1311   | Layout 1 | `1add4de5ad1e`  |
| 1309   | Layout 1 | `1add4de5ad1e`  |
| 1304   | Layout 1 | `1add4de5ad1e`  |
| 1292   | Layout 1 | `1add4de5ad1e`  |
| 1286   | Layout 1 | `1add4de5ad1e`  |
| 1280   | Layout 1 | `1add4de5ad1e`  |
| 1276   | Layout 1 | `1add4de5ad1e`  |
| 1267   | Layout 1 | `1add4de5ad1e`  |
| 1261   | Layout 1 | `1add4de5ad1e`  |
| 1256   | Layout 1 | `1add4de5ad1e`  |
| 1250   | Layout 1 | `1add4de5ad1e`  |
| 1246   | Layout 1 | `1add4de5ad1e`  |
| 1239   | Layout 1 | `1add4de5ad1e`  |
| 1230   | Layout 1 | `1add4de5ad1e`  |
| 1226   | Layout 1 | `1add4de5ad1e`  |
| 1220   | No file  | `1add4de5ad1e`  |
| 1217   | No file  | `1add4de5ad1e`  |
| 1211   | No file  | `1add4de5ad1e`  |
| 1210   | No file  | `1add4de5ad1e`  |
| 1208   | No file  | `1add4de5ad1e`  |
| 1203   | No file  | `1add4de5ad1e`  |
| 1197   | No file  | `1add4de5ad1e`  |
| 1194   | No file  | `1add4de5ad1e`  |
| 1192   | No file  | `1add4de5ad1e`  |
| 1187   | No file  | `1add4de5ad1e`  |
| 1183   | No file  | `1add4de5ad1e`  |
| 1177   | No file  | `1add4de5ad1e`  |
| 1173   | No file  | `1add4de5ad1e`  |
| 1167   | No file  | `1add4de5ad1e`  |
| 1164   | No file  | `1add4de5ad1e`  |
| 1156   | No file  | `1add4de5ad1e`  |
| 1149   | No file  | `1add4de5ad1e`  |
| 1144   | No file  | `1add4de5ad1e`  |
| 1137   | No file  | `1add4de5ad1e`  |
| 1132   | No file  | `1add4de5ad1e`  |
| 1127   | No file  | `1add4de5ad1e`  |
| 1122   | No file  | `1add4de5ad1e`  |
| 1118   | No file  | `1add4de5ad1e`  |
| 1114   | No file  | `1add4de5ad1e`  |
| 1109   | No file  | `1add4de5ad1e`  |
| 1102   | No file  | `1add4de5ad1e`  |
| 1096   | No file  | `1add4de5ad1e`  |
| 1088   | No file  | `1add4de5ad1e`  |
| 1081   | No file  | `1add4de5ad1e`  |
| 1076   | No file  | `1add4de5ad1e`  |
| 1069   | No file  | `1add4de5ad1e`  |
| 1064   | No file  | `1add4de5ad1e`  |
| 1058   | No file  | `1add4de5ad1e`  |
| 1051   | No file  | `1add4de5ad1e`  |
| 1044   | No file  | `1add4de5ad1e`  |
| 1036   | No file  | `1add4de5ad1e`  |
| 1026   | No file  | `1add4de5ad1e`  |
| 1016   | No file  | `1add4de5ad1e`  |
| 1009   | No file  | `1add4de5ad1e`  |
| 1005   | No file  | `1add4de5ad1e`  |
| 1000   | No file  | `1add4de5ad1e`  |
| 998    | No file  | `1add4de5ad1e`  |
| 990    | No file  | `1add4de5ad1e`  |
| 979    | No file  | `1add4de5ad1e`  |
| 972    | No file  | `1add4de5ad1e`  |
| 963    | No file  | `1add4de5ad1e`  |
| 955    | No file  | `1add4de5ad1e`  |
| 946    | No file  | `1add4de5ad1e`  |
| 938    | No file  | `1add4de5ad1e`  |
| 927    | No file  | `1add4de5ad1e`  |
| 911    | No file  | `1add4de5ad1e`  |
| 904    | No file  | `1add4de5ad1e`  |
| 899    | No file  | `1add4de5ad1e`  |
| 894    | No file  | `1add4de5ad1e`  |
| 885    | No file  | `1add4de5ad1e`  |
| 879    | No file  | `1add4de5ad1e`  |
| 872    | No file  | `1add4de5ad1e`  |
| 864    | No file  | `1add4de5ad1e`  |
| 855    | No file  | `1add4de5ad1e`  |
| 853    | No file  | `1add4de5ad1e`  |
| 845    | No file  | `1add4de5ad1e`  |
| 837    | No file  | `1add4de5ad1e`  |
| 829    | No file  | `1add4de5ad1e`  |
| 822    | No file  | `1add4de5ad1e`  |
| 814    | No file  | `1add4de5ad1e`  |
| 805    | No file  | `1add4de5ad1e`  |
| 794    | No file  | `1add4de5ad1e`  |
| 787    | No file  | `1add4de5ad1e`  |
| 780    | No file  | `1add4de5ad1e`  |
| 771    | No file  | `1add4de5ad1e`  |
| 760    | No file  | `1add4de5ad1e`  |
| 748    | No file  | `1add4de5ad1e`  |
| 741    | No file  | `1add4de5ad1e`  |
| 736    | No file  | `1add4de5ad1e`  |
| 731    | No file  | `1add4de5ad1e`  |
| 723    | No file  | `1add4de5ad1e`  |
| 711    | No file  | `1add4de5ad1e`  |
| 707    | No file  | `1add4de5ad1e`  |
| 697    | No file  | `1add4de5ad1e`  |
| 689    | No file  | `1add4de5ad1e`  |
| 683    | No file  | `1add4de5ad1e`  |
| 678    | No file  | `1add4de5ad1e`  |
| 670    | No file  | `1add4de5ad1e`  |
| 661    | No file  | `1add4de5ad1e`  |
| 656    | No file  | `1add4de5ad1e`  |
| 652    | No file  | `1add4de5ad1e`  |
| 643    | No file  | `1add4de5ad1e`  |
| 637    | No file  | `1add4de5ad1e`  |
| 630    | No file  | `1add4de5ad1e`  |
| 627    | No file  | `1add4de5ad1e`  |
| 621    | No file  | `1add4de5ad1e`  |
| 617    | No file  | `1add4de5ad1e`  |
| 615    | No file  | `1add4de5ad1e`  |
| 606    | No file  | `1add4de5ad1e`  |
| 599    | No file  | `1add4de5ad1e`  |
| 592    | No file  | `1add4de5ad1e`  |
| 586    | No file  | `1add4de5ad1e`  |
| 577    | No file  | `1add4de5ad1e`  |
| 569    | No file  | `1add4de5ad1e`  |
| 561    | No file  | `1add4de5ad1e`  |
| 554    | No file  | `1add4de5ad1e`  |
| 542    | No file  | `1add4de5ad1e`  |
| 532    | No file  | `1add4de5ad1e`  |
| 531    | No file  | `1add4de5ad1e`  |
| 526    | No file  | `1add4de5ad1e`  |
| 521    | No file  | `1add4de5ad1e`  |
| 517    | No file  | `1add4de5ad1e`  |
| 510    | No file  | `1add4de5ad1e`  |
| 508    | No file  | `1add4de5ad1e`  |
| 504    | No file  | `1add4de5ad1e`  |
| 497    | No file  | `1add4de5ad1e`  |
| 491    | No file  | `1add4de5ad1e`  |
| 485    | No file  | `1add4de5ad1e`  |
| 478    | No file  | `1add4de5ad1e`  |
| 472    | No file  | `1add4de5ad1e`  |
| 466    | No file  | `1add4de5ad1e`  |
| 457    | No file  | `1add4de5ad1e`  |
| 452    | No file  | `1add4de5ad1e`  |
| 449    | No file  | `1add4de5ad1e`  |
| 435    | No file  | `1add4de5ad1e`  |

<!-- versions:end -->

## Companion Files

None. The handler names each pet with its LOC type 6 name when LOC is
loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 1,287 x 6 = 7,726 bytes.

### Row (6 bytes)

| Offset  | Type | Field      | Notes                                                                              |
| ------- | ---- | ---------- | ---------------------------------------------------------------------------------- |
| `+0x00` | u8   | variant    | Fusion key byte 0: `variant` (sheet `Kind`) of the pet in `pet.dbss`               |
| `+0x01` | u8   | species    | Fusion key byte 1: `species` (sheet `Race`)                                        |
| `+0x02` | u8   | unknown_02 | Fusion key byte 2: `0` on every row, as `unknown_04` of `pet.dbss`                  |
| `+0x03` | u8   | tier       | Fusion key byte 3: `tier`, from 0 (Tier 1); `0` to `3` on client 3474              |
| `+0x04` | u16  | pet_id     | A [`pet.dbss`](../dbss/pet_dbss.md) `pet_id` whose four key bytes equal this row's          |

## Pets per Key

On client 3474 the 1,287 rows hold 903 fusion keys and 1,287 different
pets. 805 keys have one pet. The largest groups are the four keys of
species `23`, variant `1` (one per tier), with 53 pets each of different
LOC names (Boar, Worm, Saurus, Lizard, Iguana); five keys of species `1`
(Cat) hold 6 to 9 pets each.

Which pets have a row (client 3474, against the 2,009 `pet.dbss` records):

| `pet.dbss` records                      | Rows  |
| --------------------------------------- | ----- |
| `tier` `0` to `3`, `acquire_type_id` not `0` | 1,287 of 1,287 |
| `tier` `0` to `3`, `acquire_type_id` `0`     | 0 of 278       |
| `tier` `4` (Tier 5)                          | 0 of 444       |

The 278 pets with `acquire_type_id` `0` are 151 named Dog, 117 named Cat,
nine other PC room pets and one Wizard Gosphy; all ten PC room pets below
Tier 5 (`pc_room_type` `1`) are among them. 273 of the 278 share their fusion key
with a pet that has a row.

## Field Names

The fusion key is the 2016 `gc::PetStaticStatus` member `_fusionKey`, a u32
the pet doc splits into `variant`, `species`, a zero byte and `tier`, and
the 2016 client keys `gc::PetFusionStaticStatus` with a `gc::PetFusionKey`
of one u32 `_value`. The four bytes of every row equal the four bytes of
its pet in `pet.dbss` (1,287 of 1,287 rows, client 3474), so the fields
take the `pet.dbss` names; the zero byte keeps an `unknown_` name there
too. The `Pet_Fusion_Table` of a private server on client 519 (4 rows:
`Tier`, `SelectRate_0`, `SelectTier_0`, `SelectRate_1`, `SelectTier_1`) is
the source of
[`petfusionnew.dbss`](../dbss/petfusionnew_dbss.md), not of this file. A private
server's `DataSheets.bexcel` on client 1784 has no sheet with `Possible` in
its name, and its server dump has no `PossibleFusion` text.

## Notes

- Clients 1485, 1784, 2107, 2519, 3002 and 3251 ship the file with the
  same row layout; client 1784 has 986 rows.
- No client Lua reads the file. The exchange window
  (`panel_window_petfusion_all_1.luac`) sends the pets with
  `ToClient_pushFusionPetList(petNo, index)` and lets the player pick the
  look of one of them (`openSelectLook`); the new pet's tier comes from
  [`petfusionnew.dbss`](../dbss/petfusionnew_dbss.md).
- The installed `BlackDesert64.exe` (client 3474) holds no
  `possiblefusionpet` or `PossibleFusion` text as ASCII or UTF-16.

## Open Questions

### How the Exchange Uses the Groups

A fusion key with several pets (the 53 of species `23`) would need a rule
to pick one of them as the exchange result: the first row, a random row,
or a match on another field. The client Lua sends only the pet numbers and
the chosen look, so the pick happens on the server.

### Rows Only for `acquire_type_id` Other Than 0

The split by `acquire_type_id` in Pets per Key holds on all 1,565 pets
below Tier 5 on client 3474. Whether the compiler leaves those pets out on
purpose (the exchange then cannot give them) or the split follows from
another column is not in the client data.
