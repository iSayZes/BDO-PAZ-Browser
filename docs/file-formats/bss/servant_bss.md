# `servant.bss` Format

## Purpose

Base data of the servants (horses, donkeys, camels, elephants, wagons,
boats, ships, the camping tent): one record per servant character with its
Korean dev name, servant kind, tier, grade, coat colors, breeding count,
lifespan, price, the vehicle skills it starts with or can keep, and the
mix and breeding flags. On client 3474 the file has 419 records. The level
stats live in [servantexperience.dbss](../dbss/servantexperience_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes  | Records        | Row bytes                 |
| ------ | -------------- | -------------------- | ------ | -------------- | ------------------------- |
| 2      | 2794 and later | `servant.bss`        | 45,128 | 419 Row        | 84 to 165, 108 on average |
| 1      | 1421 to 2783   | `servant.dbss`       | 40,590 | 384 Row        | 84 to 165, 106 on average |
| 1      | 1421 to 2783   | `servantoffset.dbss` | 3,844  | 384 Offset Row | 10                        |

| Layout | File                 | Known            | Unknown        |
| ------ | -------------------- | ---------------- | -------------- |
| 2      | `servant.bss`        | 42,195 B (93.5%) | 2,933 B (6.5%) |
| 1      | `servant.dbss`       | 37,902 B (93.4%) | 2,688 B (6.6%) |
| 1      | `servantoffset.dbss` | 3,844 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `10ad7530a2e1`  |
| 3482   | Layout 2             | `10ad7530a2e1`  |
| 3474   | Layout 2             | `10ad7530a2e1`  |
| 3473   | Layout 2             | `10ad7530a2e1`  |
| 3464   | Layout 2             | `10ad7530a2e1`  |
| 3458   | Layout 2             | `10ad7530a2e1`  |
| 3454   | Layout 2             | `10ad7530a2e1`  |
| 3444   | Layout 2             | `10ad7530a2e1`  |
| 3435   | Layout 2             | `10ad7530a2e1`  |
| 3426   | Layout 2             | `10ad7530a2e1`  |
| 3418   | Layout 2             | `10ad7530a2e1`  |
| 3412   | Layout 2             | `10ad7530a2e1`  |
| 3402   | Layout 2             | `10ad7530a2e1`  |
| 3396   | Layout 2             | `10ad7530a2e1`  |
| 3387   | Layout 2             | `10ad7530a2e1`  |
| 3381   | Layout 2             | `10ad7530a2e1`  |
| 3373   | Layout 2             | `10ad7530a2e1`  |
| 3364   | Layout 2             | `10ad7530a2e1`  |
| 3356   | Layout 2             | `10ad7530a2e1`  |
| 3349   | Layout 2             | `10ad7530a2e1`  |
| 3342   | Layout 2             | `10ad7530a2e1`  |
| 3335   | Layout 2             | `10ad7530a2e1`  |
| 3326   | Layout 2             | `10ad7530a2e1`  |
| 3321   | Layout 2             | `10ad7530a2e1`  |
| 3314   | Layout 2             | `10ad7530a2e1`  |
| 3303   | Layout 2             | `10ad7530a2e1`  |
| 3302   | Layout 2             | `10ad7530a2e1`  |
| 3293   | Layout 2             | `10ad7530a2e1`  |
| 3283   | Layout 2             | `10ad7530a2e1`  |
| 3275   | Layout 2             | `10ad7530a2e1`  |
| 3267   | Layout 2             | `10ad7530a2e1`  |
| 3258   | Layout 2             | `10ad7530a2e1`  |
| 3251   | Layout 2             | `10ad7530a2e1`  |
| 3242   | Layout 2             | `10ad7530a2e1`  |
| 3235   | Layout 2             | `10ad7530a2e1`  |
| 3229   | Layout 2             | `10ad7530a2e1`  |
| 3212   | Layout 2             | `10ad7530a2e1`  |
| 3203   | Layout 2             | `10ad7530a2e1`  |
| 3193   | Layout 2             | `10ad7530a2e1`  |
| 3186   | Layout 2             | `10ad7530a2e1`  |
| 3177   | Layout 2             | `10ad7530a2e1`  |
| 3169   | Layout 2             | `10ad7530a2e1`  |
| 3158   | Layout 2             | `10ad7530a2e1`  |
| 3151   | Layout 2             | `10ad7530a2e1`  |
| 3144   | Layout 2             | `10ad7530a2e1`  |
| 3133   | Layout 2             | `10ad7530a2e1`  |
| 3125   | Layout 2             | `10ad7530a2e1`  |
| 3118   | Layout 2             | `10ad7530a2e1`  |
| 3111   | Layout 2             | `10ad7530a2e1`  |
| 3103   | Layout 2             | `10ad7530a2e1`  |
| 3095   | Layout 2             | `10ad7530a2e1`  |
| 3086   | Layout 2             | `10ad7530a2e1`  |
| 3072   | Layout 2             | `10ad7530a2e1`  |
| 3062   | Layout 2             | `10ad7530a2e1`  |
| 3052   | Layout 2             | `10ad7530a2e1`  |
| 3045   | Layout 2             | `10ad7530a2e1`  |
| 3037   | Layout 2             | `10ad7530a2e1`  |
| 3030   | Layout 2             | `10ad7530a2e1`  |
| 3021   | Layout 2             | `10ad7530a2e1`  |
| 3012   | Layout 2             | `10ad7530a2e1`  |
| 3002   | Layout 2             | `10ad7530a2e1`  |
| 2995   | Layout 2             | `10ad7530a2e1`  |
| 2987   | Layout 2             | `10ad7530a2e1`  |
| 2978   | Layout 2             | `10ad7530a2e1`  |
| 2970   | Layout 2             | `10ad7530a2e1`  |
| 2959   | Layout 2             | `10ad7530a2e1`  |
| 2951   | Layout 2             | `10ad7530a2e1`  |
| 2942   | Layout 2             | `10ad7530a2e1`  |
| 2935   | Layout 2             | `10ad7530a2e1`  |
| 2932   | Layout 2             | `10ad7530a2e1`  |
| 2923   | Layout 2             | `10ad7530a2e1`  |
| 2919   | Layout 2             | `10ad7530a2e1`  |
| 2907   | Layout 2             | `10ad7530a2e1`  |
| 2900   | Layout 2             | `10ad7530a2e1`  |
| 2891   | Layout 2             | `10ad7530a2e1`  |
| 2882   | Layout 2             | `10ad7530a2e1`  |
| 2872   | Layout 2             | `10ad7530a2e1`  |
| 2863   | Layout 2             | `10ad7530a2e1`  |
| 2855   | Layout 2             | `10ad7530a2e1`  |
| 2849   | Layout 2             | `10ad7530a2e1`  |
| 2844   | Layout 2             | `10ad7530a2e1`  |
| 2834   | Layout 2             | `10ad7530a2e1`  |
| 2825   | Layout 2             | `10ad7530a2e1`  |
| 2819   | Layout 2             | `10ad7530a2e1`  |
| 2811   | Layout 2             | `10ad7530a2e1`  |
| 2803   | Layout 2             | `10ad7530a2e1`  |
| 2794   | Layout 2             | `10ad7530a2e1`  |
| 2783   | Layout 1             | `10ad7530a2e1`  |
| 2774   | Layout 1             | `10ad7530a2e1`  |
| 2765   | Layout 1             | `10ad7530a2e1`  |
| 2756   | Layout 1             | `10ad7530a2e1`  |
| 2750   | Layout 1             | `10ad7530a2e1`  |
| 2743   | Layout 1             | `10ad7530a2e1`  |
| 2736   | Layout 1             | `10ad7530a2e1`  |
| 2726   | Layout 1             | `10ad7530a2e1`  |
| 2717   | Layout 1             | `10ad7530a2e1`  |
| 2709   | Layout 1             | `10ad7530a2e1`  |
| 2703   | Layout 1             | `10ad7530a2e1`  |
| 2695   | Layout 1             | `10ad7530a2e1`  |
| 2684   | Layout 1             | `10ad7530a2e1`  |
| 2672   | Layout 1             | `10ad7530a2e1`  |
| 2665   | Layout 1             | `10ad7530a2e1`  |
| 2657   | Layout 1             | `10ad7530a2e1`  |
| 2649   | Layout 1             | `10ad7530a2e1`  |
| 2644   | Layout 1             | `10ad7530a2e1`  |
| 2637   | Layout 1             | `10ad7530a2e1`  |
| 2629   | Layout 1             | `10ad7530a2e1`  |
| 2619   | Layout 1             | `10ad7530a2e1`  |
| 2612   | Layout 1             | `10ad7530a2e1`  |
| 2606   | Layout 1             | `10ad7530a2e1`  |
| 2602   | Layout 1             | `10ad7530a2e1`  |
| 2601   | Layout 1             | `10ad7530a2e1`  |
| 2592   | Layout 1             | `10ad7530a2e1`  |
| 2583   | Layout 1             | `10ad7530a2e1`  |
| 2575   | Layout 1             | `10ad7530a2e1`  |
| 2567   | Layout 1             | `10ad7530a2e1`  |
| 2560   | Layout 1             | `10ad7530a2e1`  |
| 2553   | Layout 1             | `10ad7530a2e1`  |
| 2545   | Layout 1             | `10ad7530a2e1`  |
| 2538   | Layout 1             | `10ad7530a2e1`  |
| 2529   | Layout 1             | `10ad7530a2e1`  |
| 2519   | Layout 1             | `10ad7530a2e1`  |
| 2513   | Layout 1             | `10ad7530a2e1`  |
| 2510   | Layout 1             | `10ad7530a2e1`  |
| 2507   | Layout 1             | `10ad7530a2e1`  |
| 2503   | Layout 1             | `10ad7530a2e1`  |
| 2498   | Layout 1             | `10ad7530a2e1`  |
| 2492   | Layout 1             | `10ad7530a2e1`  |
| 2487   | Layout 1             | `10ad7530a2e1`  |
| 2480   | Layout 1             | `10ad7530a2e1`  |
| 2474   | Layout 1             | `10ad7530a2e1`  |
| 2468   | Layout 1             | `10ad7530a2e1`  |
| 2460   | Layout 1             | `10ad7530a2e1`  |
| 2453   | Layout 1             | `10ad7530a2e1`  |
| 2444   | Layout 1             | `10ad7530a2e1`  |
| 2438   | Layout 1             | `10ad7530a2e1`  |
| 2434   | Layout 1             | `10ad7530a2e1`  |
| 2429   | Layout 1             | `10ad7530a2e1`  |
| 2421   | Layout 1             | `10ad7530a2e1`  |
| 2414   | Layout 1             | `10ad7530a2e1`  |
| 2407   | Layout 1             | `10ad7530a2e1`  |
| 2401   | Layout 1             | `10ad7530a2e1`  |
| 2397   | Layout 1             | `10ad7530a2e1`  |
| 2393   | Layout 1             | `10ad7530a2e1`  |
| 2384   | Layout 1             | `10ad7530a2e1`  |
| 2378   | Layout 1             | `10ad7530a2e1`  |
| 2372   | Layout 1             | `10ad7530a2e1`  |
| 2358   | Layout 1             | `10ad7530a2e1`  |
| 2352   | Layout 1             | `10ad7530a2e1`  |
| 2347   | Layout 1             | `10ad7530a2e1`  |
| 2343   | Layout 1             | `10ad7530a2e1`  |
| 2335   | Layout 1             | `10ad7530a2e1`  |
| 2327   | Layout 1             | `10ad7530a2e1`  |
| 2324   | Layout 1             | `10ad7530a2e1`  |
| 2319   | Layout 1             | `10ad7530a2e1`  |
| 2313   | Layout 1             | `10ad7530a2e1`  |
| 2308   | Layout 1             | `10ad7530a2e1`  |
| 2302   | Layout 1             | `10ad7530a2e1`  |
| 2295   | Layout 1             | `10ad7530a2e1`  |
| 2290   | Layout 1             | `10ad7530a2e1`  |
| 2284   | Layout 1             | `10ad7530a2e1`  |
| 2276   | Layout 1             | `10ad7530a2e1`  |
| 2269   | Layout 1             | `10ad7530a2e1`  |
| 2259   | Layout 1             | `10ad7530a2e1`  |
| 2250   | Layout 1             | `10ad7530a2e1`  |
| 2243   | Layout 1             | `10ad7530a2e1`  |
| 2235   | Layout 1             | `10ad7530a2e1`  |
| 2229   | Layout 1             | `10ad7530a2e1`  |
| 2224   | Layout 1             | `10ad7530a2e1`  |
| 2218   | Layout 1             | `10ad7530a2e1`  |
| 2215   | Layout 1             | `10ad7530a2e1`  |
| 2207   | Layout 1             | `10ad7530a2e1`  |
| 2203   | Layout 1             | `10ad7530a2e1`  |
| 2196   | Layout 1             | `10ad7530a2e1`  |
| 2192   | Layout 1             | `10ad7530a2e1`  |
| 2189   | Layout 1             | `10ad7530a2e1`  |
| 2183   | Layout 1             | `10ad7530a2e1`  |
| 2179   | Layout 1             | `10ad7530a2e1`  |
| 2171   | Layout 1             | `10ad7530a2e1`  |
| 2163   | Layout 1             | `10ad7530a2e1`  |
| 2156   | Layout 1             | `10ad7530a2e1`  |
| 2151   | Layout 1             | `10ad7530a2e1`  |
| 2147   | Layout 1             | `10ad7530a2e1`  |
| 2142   | Layout 1             | `10ad7530a2e1`  |
| 2138   | Layout 1             | `10ad7530a2e1`  |
| 2134   | Layout 1             | `10ad7530a2e1`  |
| 2130   | Layout 1             | `10ad7530a2e1`  |
| 2122   | Layout 1             | `10ad7530a2e1`  |
| 2107   | Layout 1             | `10ad7530a2e1`  |
| 2098   | Layout 1             | `10ad7530a2e1`  |
| 2089   | Layout 1             | `10ad7530a2e1`  |
| 2081   | Layout 1             | `10ad7530a2e1`  |
| 2073   | Layout 1             | `10ad7530a2e1`  |
| 2067   | Layout 1             | `10ad7530a2e1`  |
| 2063   | Layout 1             | `10ad7530a2e1`  |
| 2059   | Layout 1             | `10ad7530a2e1`  |
| 2052   | Layout 1             | `10ad7530a2e1`  |
| 2044   | Layout 1             | `10ad7530a2e1`  |
| 2039   | Layout 1             | `10ad7530a2e1`  |
| 2032   | Layout 1             | `10ad7530a2e1`  |
| 2025   | Layout 1             | `10ad7530a2e1`  |
| 2011   | Layout 1             | `10ad7530a2e1`  |
| 2005   | Layout 1             | `10ad7530a2e1`  |
| 2000   | Layout 1             | `10ad7530a2e1`  |
| 1996   | Layout 1             | `10ad7530a2e1`  |
| 1991   | Layout 1             | `10ad7530a2e1`  |
| 1985   | Layout 1             | `10ad7530a2e1`  |
| 1980   | Layout 1             | `10ad7530a2e1`  |
| 1969   | Layout 1             | `10ad7530a2e1`  |
| 1964   | Layout 1             | `10ad7530a2e1`  |
| 1958   | Layout 1             | `10ad7530a2e1`  |
| 1950   | Layout 1             | `10ad7530a2e1`  |
| 1945   | Layout 1             | `10ad7530a2e1`  |
| 1937   | Layout 1             | `10ad7530a2e1`  |
| 1933   | Layout 1             | `10ad7530a2e1`  |
| 1927   | Layout 1             | `10ad7530a2e1`  |
| 1921   | Layout 1             | `10ad7530a2e1`  |
| 1914   | Layout 1             | `10ad7530a2e1`  |
| 1908   | Layout 1             | `10ad7530a2e1`  |
| 1897   | Layout 1             | `10ad7530a2e1`  |
| 1892   | Layout 1             | `10ad7530a2e1`  |
| 1886   | Layout 1             | `10ad7530a2e1`  |
| 1881   | Layout 1             | `10ad7530a2e1`  |
| 1871   | Layout 1             | `10ad7530a2e1`  |
| 1866   | Layout 1             | `10ad7530a2e1`  |
| 1862   | Layout 1             | `10ad7530a2e1`  |
| 1854   | Layout 1             | `10ad7530a2e1`  |
| 1846   | Layout 1             | `10ad7530a2e1`  |
| 1838   | Layout 1             | `10ad7530a2e1`  |
| 1832   | Layout 1             | `10ad7530a2e1`  |
| 1826   | Layout 1             | `10ad7530a2e1`  |
| 1822   | Layout 1             | `10ad7530a2e1`  |
| 1818   | Layout 1             | `10ad7530a2e1`  |
| 1804   | Layout 1             | `10ad7530a2e1`  |
| 1794   | Layout 1             | `10ad7530a2e1`  |
| 1790   | Layout 1             | `10ad7530a2e1`  |
| 1784   | Layout 1             | `10ad7530a2e1`  |
| 1774   | Layout 1             | `10ad7530a2e1`  |
| 1771   | Layout 1             | `10ad7530a2e1`  |
| 1762   | Layout 1             | `10ad7530a2e1`  |
| 1759   | Layout 1             | `10ad7530a2e1`  |
| 1754   | Layout 1             | `10ad7530a2e1`  |
| 1749   | Layout 1             | `10ad7530a2e1`  |
| 1743   | Layout 1             | `10ad7530a2e1`  |
| 1737   | Layout 1             | `10ad7530a2e1`  |
| 1731   | Layout 1             | `10ad7530a2e1`  |
| 1725   | Layout 1             | `10ad7530a2e1`  |
| 1717   | Layout 1             | `10ad7530a2e1`  |
| 1710   | Layout 1             | `10ad7530a2e1`  |
| 1704   | Layout 1             | `10ad7530a2e1`  |
| 1698   | Layout 1             | `10ad7530a2e1`  |
| 1690   | Layout 1             | `10ad7530a2e1`  |
| 1685   | Layout 1             | `10ad7530a2e1`  |
| 1680   | Layout 1             | `10ad7530a2e1`  |
| 1674   | Layout 1             | `10ad7530a2e1`  |
| 1668   | Layout 1             | `10ad7530a2e1`  |
| 1659   | Layout 1             | `10ad7530a2e1`  |
| 1649   | Layout 1             | `10ad7530a2e1`  |
| 1642   | Layout 1             | `10ad7530a2e1`  |
| 1636   | Layout 1             | `10ad7530a2e1`  |
| 1628   | Layout 1             | `10ad7530a2e1`  |
| 1622   | Layout 1             | `10ad7530a2e1`  |
| 1614   | Layout 1             | `10ad7530a2e1`  |
| 1608   | Layout 1             | `10ad7530a2e1`  |
| 1602   | Layout 1             | `10ad7530a2e1`  |
| 1598   | Layout 1             | `10ad7530a2e1`  |
| 1594   | Layout 1             | `10ad7530a2e1`  |
| 1590   | Layout 1             | `10ad7530a2e1`  |
| 1587   | Layout 1             | `10ad7530a2e1`  |
| 1584   | Layout 1             | `10ad7530a2e1`  |
| 1579   | Layout 1             | `10ad7530a2e1`  |
| 1572   | Layout 1             | `10ad7530a2e1`  |
| 1565   | Layout 1             | `10ad7530a2e1`  |
| 1559   | Layout 1             | `10ad7530a2e1`  |
| 1554   | Layout 1             | `10ad7530a2e1`  |
| 1547   | Layout 1             | `10ad7530a2e1`  |
| 1537   | Layout 1             | `10ad7530a2e1`  |
| 1529   | Layout 1             | `10ad7530a2e1`  |
| 1524   | Layout 1             | `10ad7530a2e1`  |
| 1519   | Layout 1             | `10ad7530a2e1`  |
| 1509   | Layout 1             | `10ad7530a2e1`  |
| 1506   | Layout 1             | `10ad7530a2e1`  |
| 1504   | Layout 1             | `10ad7530a2e1`  |
| 1500   | Layout 1             | `10ad7530a2e1`  |
| 1493   | Layout 1             | `10ad7530a2e1`  |
| 1489   | Layout 1             | `10ad7530a2e1`  |
| 1485   | Layout 1             | `10ad7530a2e1`  |
| 1481   | Layout 1             | `10ad7530a2e1`  |
| 1474   | Layout 1             | `10ad7530a2e1`  |
| 1466   | Layout 1             | `10ad7530a2e1`  |
| 1462   | Layout 1             | `10ad7530a2e1`  |
| 1459   | Layout 1             | `10ad7530a2e1`  |
| 1453   | Layout 1             | `10ad7530a2e1`  |
| 1450   | Layout 1             | `10ad7530a2e1`  |
| 1445   | Layout 1             | `10ad7530a2e1`  |
| 1439   | Layout 1             | `10ad7530a2e1`  |
| 1433   | Layout 1             | `10ad7530a2e1`  |
| 1430   | Layout 1             | `10ad7530a2e1`  |
| 1426   | Layout 1             | `10ad7530a2e1`  |
| 1421   | Layout 1             | `10ad7530a2e1`  |
| 1417   | No documented layout | `10ad7530a2e1`  |
| 1416   | No documented layout | `10ad7530a2e1`  |
| 1409   | No documented layout | `10ad7530a2e1`  |
| 1405   | No documented layout | `10ad7530a2e1`  |
| 1401   | No documented layout | `10ad7530a2e1`  |
| 1396   | No documented layout | `10ad7530a2e1`  |
| 1391   | No documented layout | `10ad7530a2e1`  |
| 1390   | No documented layout | `10ad7530a2e1`  |
| 1386   | No documented layout | `10ad7530a2e1`  |
| 1381   | No documented layout | `10ad7530a2e1`  |
| 1379   | No documented layout | `10ad7530a2e1`  |
| 1372   | No documented layout | `10ad7530a2e1`  |
| 1366   | No documented layout | `10ad7530a2e1`  |
| 1364   | No documented layout | `10ad7530a2e1`  |
| 1363   | No documented layout | `10ad7530a2e1`  |
| 1360   | No documented layout | `10ad7530a2e1`  |
| 1358   | No documented layout | `10ad7530a2e1`  |
| 1355   | No documented layout | `10ad7530a2e1`  |
| 1351   | No documented layout | `10ad7530a2e1`  |
| 1348   | No documented layout | `10ad7530a2e1`  |
| 1346   | No documented layout | `10ad7530a2e1`  |
| 1341   | No documented layout | `10ad7530a2e1`  |
| 1340   | No documented layout | `10ad7530a2e1`  |
| 1338   | No documented layout | `10ad7530a2e1`  |
| 1335   | No documented layout | `10ad7530a2e1`  |
| 1333   | No documented layout | `10ad7530a2e1`  |
| 1329   | No documented layout | `10ad7530a2e1`  |
| 1327   | No documented layout | `10ad7530a2e1`  |
| 1324   | No documented layout | `10ad7530a2e1`  |
| 1321   | No documented layout | `10ad7530a2e1`  |
| 1319   | No documented layout | `10ad7530a2e1`  |
| 1318   | No documented layout | `10ad7530a2e1`  |
| 1316   | No documented layout | `10ad7530a2e1`  |
| 1313   | No documented layout | `10ad7530a2e1`  |
| 1311   | No documented layout | `10ad7530a2e1`  |
| 1309   | No documented layout | `10ad7530a2e1`  |
| 1304   | No documented layout | `10ad7530a2e1`  |
| 1292   | No documented layout | `10ad7530a2e1`  |
| 1286   | No documented layout | `10ad7530a2e1`  |
| 1280   | No documented layout | `10ad7530a2e1`  |
| 1276   | No documented layout | `10ad7530a2e1`  |
| 1267   | No documented layout | `10ad7530a2e1`  |
| 1261   | No documented layout | `10ad7530a2e1`  |
| 1256   | No documented layout | `10ad7530a2e1`  |
| 1250   | No documented layout | `10ad7530a2e1`  |
| 1246   | No file              | `10ad7530a2e1`  |
| 1239   | No file              | `10ad7530a2e1`  |
| 1230   | No file              | `10ad7530a2e1`  |
| 1226   | No file              | `10ad7530a2e1`  |
| 1220   | No file              | `10ad7530a2e1`  |
| 1217   | No file              | `10ad7530a2e1`  |
| 1211   | No file              | `10ad7530a2e1`  |
| 1210   | No file              | `10ad7530a2e1`  |
| 1208   | No file              | `10ad7530a2e1`  |
| 1203   | No file              | `10ad7530a2e1`  |
| 1197   | No file              | `10ad7530a2e1`  |
| 1194   | No file              | `10ad7530a2e1`  |
| 1192   | No file              | `10ad7530a2e1`  |
| 1187   | No file              | `10ad7530a2e1`  |
| 1183   | No file              | `10ad7530a2e1`  |
| 1177   | No file              | `10ad7530a2e1`  |
| 1173   | No file              | `10ad7530a2e1`  |
| 1167   | No file              | `10ad7530a2e1`  |
| 1164   | No file              | `10ad7530a2e1`  |
| 1156   | No file              | `10ad7530a2e1`  |
| 1149   | No file              | `10ad7530a2e1`  |
| 1144   | No file              | `10ad7530a2e1`  |
| 1137   | No file              | `10ad7530a2e1`  |
| 1132   | No file              | `10ad7530a2e1`  |
| 1127   | No file              | `10ad7530a2e1`  |
| 1122   | No file              | `10ad7530a2e1`  |
| 1118   | No file              | `10ad7530a2e1`  |
| 1114   | No file              | `10ad7530a2e1`  |
| 1109   | No file              | `10ad7530a2e1`  |
| 1102   | No file              | `10ad7530a2e1`  |
| 1096   | No file              | `10ad7530a2e1`  |
| 1088   | No file              | `10ad7530a2e1`  |
| 1081   | No file              | `10ad7530a2e1`  |
| 1076   | No file              | `10ad7530a2e1`  |
| 1069   | No file              | `10ad7530a2e1`  |
| 1064   | No file              | `10ad7530a2e1`  |
| 1058   | No file              | `10ad7530a2e1`  |
| 1051   | No file              | `10ad7530a2e1`  |
| 1044   | No file              | `10ad7530a2e1`  |
| 1036   | No file              | `10ad7530a2e1`  |
| 1026   | No file              | `10ad7530a2e1`  |
| 1016   | No file              | `10ad7530a2e1`  |
| 1009   | No file              | `10ad7530a2e1`  |
| 1005   | No file              | `10ad7530a2e1`  |
| 1000   | No file              | `10ad7530a2e1`  |
| 998    | No file              | `10ad7530a2e1`  |
| 990    | No file              | `10ad7530a2e1`  |
| 979    | No file              | `10ad7530a2e1`  |
| 972    | No file              | `10ad7530a2e1`  |
| 963    | No file              | `10ad7530a2e1`  |
| 955    | No file              | `10ad7530a2e1`  |
| 946    | No file              | `10ad7530a2e1`  |
| 938    | No file              | `10ad7530a2e1`  |
| 927    | No file              | `10ad7530a2e1`  |
| 911    | No file              | `10ad7530a2e1`  |
| 904    | No file              | `10ad7530a2e1`  |
| 899    | No file              | `10ad7530a2e1`  |
| 894    | No file              | `10ad7530a2e1`  |
| 885    | No file              | `10ad7530a2e1`  |
| 879    | No file              | `10ad7530a2e1`  |
| 872    | No file              | `10ad7530a2e1`  |
| 864    | No file              | `10ad7530a2e1`  |
| 855    | No file              | `10ad7530a2e1`  |
| 853    | No file              | `10ad7530a2e1`  |
| 845    | No file              | `10ad7530a2e1`  |
| 837    | No file              | `10ad7530a2e1`  |
| 829    | No documented layout | `10ad7530a2e1`  |
| 822    | No documented layout | `10ad7530a2e1`  |
| 814    | No documented layout | `10ad7530a2e1`  |
| 805    | No documented layout | `10ad7530a2e1`  |
| 794    | No documented layout | `10ad7530a2e1`  |
| 787    | No documented layout | `10ad7530a2e1`  |
| 780    | No documented layout | `10ad7530a2e1`  |
| 771    | No documented layout | `10ad7530a2e1`  |
| 760    | No documented layout | `10ad7530a2e1`  |
| 748    | No documented layout | `10ad7530a2e1`  |
| 741    | No documented layout | `10ad7530a2e1`  |
| 736    | No documented layout | `10ad7530a2e1`  |
| 731    | No documented layout | `10ad7530a2e1`  |
| 723    | No documented layout | `10ad7530a2e1`  |
| 711    | No documented layout | `10ad7530a2e1`  |
| 707    | No documented layout | `10ad7530a2e1`  |
| 697    | No documented layout | `10ad7530a2e1`  |
| 689    | No documented layout | `10ad7530a2e1`  |
| 683    | No documented layout | `10ad7530a2e1`  |
| 678    | No documented layout | `10ad7530a2e1`  |
| 670    | No documented layout | `10ad7530a2e1`  |
| 661    | No documented layout | `10ad7530a2e1`  |
| 656    | No documented layout | `10ad7530a2e1`  |
| 652    | No documented layout | `10ad7530a2e1`  |
| 643    | No documented layout | `10ad7530a2e1`  |
| 637    | No documented layout | `10ad7530a2e1`  |
| 630    | No documented layout | `10ad7530a2e1`  |
| 627    | No documented layout | `10ad7530a2e1`  |
| 621    | No documented layout | `10ad7530a2e1`  |
| 617    | No documented layout | `10ad7530a2e1`  |
| 615    | No documented layout | `10ad7530a2e1`  |
| 606    | No documented layout | `10ad7530a2e1`  |
| 599    | No documented layout | `10ad7530a2e1`  |
| 592    | No documented layout | `10ad7530a2e1`  |
| 586    | No documented layout | `10ad7530a2e1`  |
| 577    | No documented layout | `10ad7530a2e1`  |
| 569    | No documented layout | `10ad7530a2e1`  |
| 561    | No documented layout | `10ad7530a2e1`  |
| 554    | No documented layout | `10ad7530a2e1`  |
| 542    | No documented layout | `10ad7530a2e1`  |
| 532    | No documented layout | `10ad7530a2e1`  |
| 531    | No documented layout | `10ad7530a2e1`  |
| 526    | No documented layout | `10ad7530a2e1`  |
| 521    | No documented layout | `10ad7530a2e1`  |
| 517    | No documented layout | `10ad7530a2e1`  |
| 510    | No documented layout | `10ad7530a2e1`  |
| 508    | No documented layout | `10ad7530a2e1`  |
| 504    | No documented layout | `10ad7530a2e1`  |
| 497    | No documented layout | `10ad7530a2e1`  |
| 491    | No documented layout | `10ad7530a2e1`  |
| 485    | No documented layout | `10ad7530a2e1`  |
| 478    | No documented layout | `10ad7530a2e1`  |
| 472    | No documented layout | `10ad7530a2e1`  |
| 466    | No documented layout | `10ad7530a2e1`  |
| 457    | No documented layout | `10ad7530a2e1`  |
| 452    | No documented layout | `10ad7530a2e1`  |
| 449    | No documented layout | `10ad7530a2e1`  |
| 435    | No documented layout | `10ad7530a2e1`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                 |
| ---------------------------- | -------- | -------------------------------------------------------------------- |
| `vehicleskill.dbss`          | Optional | Korean skill names for `basic_learn_skill_keys` and `stallion_skill_keys` when LOC has none |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |
| `languagedata_en.loc`        | Optional | Servant names (LOC type 6, `str_id1` = `character_id`) and skill names (LOC type 8, `str_id1` = skill key) |

Client 1784 ships the same records as `servant.dbss` with the index
`servantoffset.dbss` (Layout 1).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field   | Notes                                  |
| ------- | ---------- | ------- | -------------------------------------- |
| `+0x00` | u32        | count   | 419 on client 3474                     |
| `+0x04` | Row[count] | records | Back to back, variable size, up to EOF |

### Row (variable: 80 bytes + name text and skill lists)

| Offset                        | Type                           | Field                             | Notes |
| ----------------------------- | ------------------------------ | --------------------------------- | ----- |
| `+0x00`                       | u16                            | character_id                      | Servant character, as in `characterstatic.dbss`; records sort by it, highest first |
| `+0x02`                       | u16                            | character_id_dup                  | Equals `character_id` on every record |
| `+0x04`                       | str16                          | name_kr                           | Korean dev name (`탑승용 수말29`); the game name is LOC type 6 |
| `name_kr+0x00`                | u8                             | servant_kind                      | `ServantKind`: 0 horse on 332 records (client 3474); the groups are in [itemenchant.dbss](../dbss/itemenchant_dbss.md#equip_slot) |
| `name_kr+0x01`                | u8                             | servant_kind_sub                  | 0 to 10; non-zero on the dream horses and other kinds' variants |
| `name_kr+0x02`                | u16                            | tier                              | 0 to 9 |
| `name_kr+0x04`                | u16                            | grade                             | |
| `name_kr+0x06`                | u16                            | color1                            | |
| `name_kr+0x08`                | u16                            | color2                            | |
| `name_kr+0x0A`                | u16                            | color3                            | |
| `name_kr+0x0C`                | u8                             | mating_count                      | Breeding count; 0 on everything that cannot breed |
| `name_kr+0x0D`                | u32                            | lifespan                          | Seconds; 0 except 9057, an event Horse (259,200, 3 days) and 31125 Doomcaller (1,209,600, 14 days) on client 3474 |
| `name_kr+0x11`                | i64                            | base_price                        | Silver |
| `name_kr+0x19`                | i64                            | price_per_level                   | Silver |
| `name_kr+0x21`                | u8                             | is_male                           | |
| `name_kr+0x22`                | u8                             | is_display_gender                 | 0 on 22 records (client 3474), among them the dream horses, the dragons and the Twins |
| `name_kr+0x23`                | u8                             | servant_main_model                | 1 on one servant per kind (Notes) |
| `name_kr+0x24`                | u8                             | is_mating_result                  | |
| `name_kr+0x25`                | u8                             | is_trade                          | |
| `name_kr+0x26`                | u8                             | link_count                        | 0, 1, 2 or 4 |
| `name_kr+0x27`                | i32                            | experience_per_one                | 0, or 250,000 to 1,050,000 on 11 records (client 3474) |
| `name_kr+0x2B`                | u16                            | form_index                        | |
| `name_kr+0x2D`                | u8                             | basic_learn_skill_max_count       | |
| `name_kr+0x2E`                | u32                            | basic_learn_skill_count           | |
| `name_kr+0x32`                | u8[basic_learn_skill_count]    | basic_learn_skill_keys            | `vehicleskill.dbss` keys |
| `basic_learn_skill_keys+0x00` | bytes[5]                       | unknown_basic_learn_skill_keys_00 | `0` on every record (clients 1784 and 3474) |
| `basic_learn_skill_keys+0x05` | u32                            | reward_money_percent              | 500,000 on every record (clients 1784 and 3474) |
| `basic_learn_skill_keys+0x09` | u8                             | is_only_pcroom                    | 1 on 8 records (client 3474) |
| `basic_learn_skill_keys+0x0A` | u32                            | stallion_skill_count              | |
| `basic_learn_skill_keys+0x0E` | u8[stallion_skill_count]       | stallion_skill_keys               | `vehicleskill.dbss` keys: 3, 4, 8, 9, 10, 18 and 19 on client 3474 |
| `stallion_skill_keys+0x00`    | u8                             | can_mix                           | |
| `stallion_skill_keys+0x01`    | u8                             | can_mating                        | 1 exactly where `mating_count` is above 0 (Field Names) |
| `stallion_skill_keys+0x02`    | bytes[2]                       | unknown_stallion_skill_keys_02    | `0` on every record (clients 1784 and 3474) |

## Layout 1

Client 1784 names the file `servant.dbss`, with the same records, and adds
the index `servantoffset.dbss`.

### `servant.dbss`

| Offset  | Type       | Field   | Notes                                  |
| ------- | ---------- | ------- | -------------------------------------- |
| `+0x00` | u32        | count   | 333 on client 1784                     |
| `+0x04` | Row[count] | records | Back to back, variable size, up to EOF |

### `servantoffset.dbss`

| Offset  | Type              | Field   | Notes                       |
| ------- | ----------------- | ------- | --------------------------- |
| `+0x00` | u32               | count   | Equals the `servant.dbss` count |
| `+0x04` | Offset Row[count] | entries | `count` entries of 10 bytes |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u16  | character_id | The record's `character_id`                              |
| `+0x02` | u32  | offset       | Where the record's `character_id_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size         | Record size minus 2, from `character_id_dup` to the record end |

## Field Names

The names follow the `ServantSet_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched value by value against the
official client 1784 `servant.dbss` (333 records, every one in the sheet)
and client 3474 (329 of 419 records in the sheet):

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `RaceType` | `servant_kind` | 333 | 329 |
| `RaceSubType` | `servant_kind_sub` | 333 | 314 |
| `Tier`, `Grade` | `tier`, `grade` | 333 | 328, 329 |
| `Color1` to `Color3` | `color1` to `color3` | 333 | 329 |
| `MatingCount` | `mating_count` | 333 | 329 |
| `Lifespan` (minutes) | `lifespan` (seconds, x 60) | 333 | 329 |
| `basePrice`, `PricePerLevel` | `base_price`, `price_per_level` | 178 | 99, 101 |
| `IsMale`, `isDisplayGender` | `is_male`, `is_display_gender` | 333 | 329 |
| `ServantMainModel` | `servant_main_model` | 333 | 328 |
| `IsMatingResult`, `IsTrade` | `is_mating_result`, `is_trade` | 333 | 329 |
| `LinkCount`, `ExperiencePerOn` | `link_count`, `experience_per_one` | 333 | 329 |
| `FormIndex` | `form_index` | 333 | 329 |
| `basicLearnSkillMaxCount` | `basic_learn_skill_max_count` | 333 | 295 |
| `basicLearnSkillKey` (comma list) | `basic_learn_skill_keys` | 333 | 127 |
| `rewardMoneyPercent`, `isOnlyPcroom` | `reward_money_percent`, `is_only_pcroom` | 333 | 329 |
| `stallionSkillKey` (comma list) | `stallion_skill_keys` | 333 | 329 |
| `CanMix` | `can_mix` | 333 | 329 |

The prices are the private server's own; every other column matches all of
client 1784. The client 3474 misses are later changes: 15 dream horses
(Arduanatt, Diné, Doom and their dream and GT versions) have a
`servant_kind_sub` of 1 to 7 where the sheet has 0, Epheria Carrack:
Advance (31054) is a main model and Panokseon (31025) tier 3, and 183 of
the 202 `basic_learn_skill_keys` misses are the sheet's list plus vehicle
skill 4 (Sprint).

The sheet has no column for `can_mating`. The 2016 `gc::ServantStaticStatus`
ends with `_canMix` and `_canMating`, and the byte after `can_mix` is 1
exactly where `mating_count` is above 0 (419 of 419 records, client 3474).
The same struct holds `_servantKind`, `_servantExpirationPeriod` (the
`lifespan` slot) and `_experiencePerOne`, in the file's order. The client Lua
calls `getServantKind`, `getServantKindSub`, `getTier`, `getGrade`,
`isMale`, `isDisplayGender`, `getMatingCount`, `getLinkCount` and
`isPcroomOnly`.

## Notes

- `servant_main_model` is 1 on 8 records (client 3474), one per kind: 9909
  (Horse), 9010 (Brown Camel), 9113 (Donkey), 9052 (Merchant Wagon), 9032
  (Rowboat), 9065 (Fishing Boat), 31001 (Epheria Sailboat) and 31054
  (Epheria Carrack: Advance).
- The skill lists index [vehicleskill.dbss](../dbss/vehicleskill_dbss.md) by its
  u8 key (1 to 106 on client 3474): stallion skill 3 is `드리프트` (Drift), 4
  `전력질주` (Sprint), 8 `순간가속` (Instant Acceleration), 9 `돌진` (Charge).
- In game on client 3474, a Mythical horse with Base Coat "Breed 13" (only
  31619 fits, see [bdoservanttitless.bss](bdoservanttitless_bss.md)) shows
  Skill List (27), all locked at 100%: its 27 `basic_learn_skill_keys`.
- No field holds HP, stamina, weight or a movement stat, so the 500 HP and 1
  stamina that two horses start above their `servantexperience.dbss` level 1
  row (its Open Questions) do not come from this file.

## Open Questions

### The Zero Fields

`unknown_basic_learn_skill_keys_00` (5 bytes) and
`unknown_stallion_skill_keys_02` (2 bytes) are `0` on every record of
clients 1784 and 3474. In column order the first sits where the sheet has
`specialLearnSkillMaxCount` and `specialLearnSkillKey`, but the sheet holds
`1` in `specialLearnSkillMaxCount` on every row, so the bytes do not follow
it. A u8 plus a u32 count of an empty list would fit the 5 bytes as well.
