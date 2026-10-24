# `siegeangerskill.bss` Format

## Purpose

The guild skills of the siege Spirit of Battle gauge and the gauge's
values. Rows of a skill number, its cost, a skill type and a resource
type, then one block of eight u32: how much Spirit of Battle a death, a
kill and the war itself give, the maximum, and the survival rates. Client
3482 has 15 skills; the two with resource type `1` (Breath of Life and
Blessing of Battle) cost the whole gauge.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------- | --------- |
| 1      | 1659 and later | 3483    | `siegeangerskill.bss` | 172   | 15 Row  | 8         |

| Layout | File                  | Known          | Unknown    |
| ------ | --------------------- | -------------- | ---------- |
| 1      | `siegeangerskill.bss` | 172 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a95af7a8f873`  |
| 3482   | Layout 1 | `a95af7a8f873`  |
| 3474   | Layout 1 | `a95af7a8f873`  |
| 3473   | Layout 1 | `a95af7a8f873`  |
| 3464   | Layout 1 | `a95af7a8f873`  |
| 3458   | Layout 1 | `a95af7a8f873`  |
| 3454   | Layout 1 | `a95af7a8f873`  |
| 3444   | Layout 1 | `a95af7a8f873`  |
| 3435   | Layout 1 | `a95af7a8f873`  |
| 3426   | Layout 1 | `a95af7a8f873`  |
| 3418   | Layout 1 | `a95af7a8f873`  |
| 3412   | Layout 1 | `a95af7a8f873`  |
| 3402   | Layout 1 | `a95af7a8f873`  |
| 3396   | Layout 1 | `a95af7a8f873`  |
| 3387   | Layout 1 | `a95af7a8f873`  |
| 3381   | Layout 1 | `a95af7a8f873`  |
| 3373   | Layout 1 | `a95af7a8f873`  |
| 3364   | Layout 1 | `a95af7a8f873`  |
| 3356   | Layout 1 | `a95af7a8f873`  |
| 3349   | Layout 1 | `a95af7a8f873`  |
| 3342   | Layout 1 | `a95af7a8f873`  |
| 3335   | Layout 1 | `a95af7a8f873`  |
| 3326   | Layout 1 | `a95af7a8f873`  |
| 3321   | Layout 1 | `a95af7a8f873`  |
| 3314   | Layout 1 | `a95af7a8f873`  |
| 3303   | Layout 1 | `a95af7a8f873`  |
| 3302   | Layout 1 | `a95af7a8f873`  |
| 3293   | Layout 1 | `a95af7a8f873`  |
| 3283   | Layout 1 | `a95af7a8f873`  |
| 3275   | Layout 1 | `a95af7a8f873`  |
| 3267   | Layout 1 | `a95af7a8f873`  |
| 3258   | Layout 1 | `a95af7a8f873`  |
| 3251   | Layout 1 | `a95af7a8f873`  |
| 3242   | Layout 1 | `a95af7a8f873`  |
| 3235   | Layout 1 | `a95af7a8f873`  |
| 3229   | Layout 1 | `a95af7a8f873`  |
| 3212   | Layout 1 | `a95af7a8f873`  |
| 3203   | Layout 1 | `a95af7a8f873`  |
| 3193   | Layout 1 | `a95af7a8f873`  |
| 3186   | Layout 1 | `a95af7a8f873`  |
| 3177   | Layout 1 | `a95af7a8f873`  |
| 3169   | Layout 1 | `a95af7a8f873`  |
| 3158   | Layout 1 | `a95af7a8f873`  |
| 3151   | Layout 1 | `a95af7a8f873`  |
| 3144   | Layout 1 | `a95af7a8f873`  |
| 3133   | Layout 1 | `a95af7a8f873`  |
| 3125   | Layout 1 | `a95af7a8f873`  |
| 3118   | Layout 1 | `a95af7a8f873`  |
| 3111   | Layout 1 | `a95af7a8f873`  |
| 3103   | Layout 1 | `a95af7a8f873`  |
| 3095   | Layout 1 | `a95af7a8f873`  |
| 3086   | Layout 1 | `a95af7a8f873`  |
| 3072   | Layout 1 | `a95af7a8f873`  |
| 3062   | Layout 1 | `a95af7a8f873`  |
| 3052   | Layout 1 | `a95af7a8f873`  |
| 3045   | Layout 1 | `a95af7a8f873`  |
| 3037   | Layout 1 | `a95af7a8f873`  |
| 3030   | Layout 1 | `a95af7a8f873`  |
| 3021   | Layout 1 | `a95af7a8f873`  |
| 3012   | Layout 1 | `a95af7a8f873`  |
| 3002   | Layout 1 | `a95af7a8f873`  |
| 2995   | Layout 1 | `a95af7a8f873`  |
| 2987   | Layout 1 | `a95af7a8f873`  |
| 2978   | Layout 1 | `a95af7a8f873`  |
| 2970   | Layout 1 | `a95af7a8f873`  |
| 2959   | Layout 1 | `a95af7a8f873`  |
| 2951   | Layout 1 | `a95af7a8f873`  |
| 2942   | Layout 1 | `a95af7a8f873`  |
| 2935   | Layout 1 | `a95af7a8f873`  |
| 2932   | Layout 1 | `a95af7a8f873`  |
| 2923   | Layout 1 | `a95af7a8f873`  |
| 2919   | Layout 1 | `a95af7a8f873`  |
| 2907   | Layout 1 | `a95af7a8f873`  |
| 2900   | Layout 1 | `a95af7a8f873`  |
| 2891   | Layout 1 | `a95af7a8f873`  |
| 2882   | Layout 1 | `a95af7a8f873`  |
| 2872   | Layout 1 | `a95af7a8f873`  |
| 2863   | Layout 1 | `a95af7a8f873`  |
| 2855   | Layout 1 | `a95af7a8f873`  |
| 2849   | Layout 1 | `a95af7a8f873`  |
| 2844   | Layout 1 | `a95af7a8f873`  |
| 2834   | Layout 1 | `a95af7a8f873`  |
| 2825   | Layout 1 | `a95af7a8f873`  |
| 2819   | Layout 1 | `a95af7a8f873`  |
| 2811   | Layout 1 | `a95af7a8f873`  |
| 2803   | Layout 1 | `a95af7a8f873`  |
| 2794   | Layout 1 | `a95af7a8f873`  |
| 2783   | Layout 1 | `a95af7a8f873`  |
| 2774   | Layout 1 | `a95af7a8f873`  |
| 2765   | Layout 1 | `a95af7a8f873`  |
| 2756   | Layout 1 | `a95af7a8f873`  |
| 2750   | Layout 1 | `a95af7a8f873`  |
| 2743   | Layout 1 | `a95af7a8f873`  |
| 2736   | Layout 1 | `a95af7a8f873`  |
| 2726   | Layout 1 | `a95af7a8f873`  |
| 2717   | Layout 1 | `a95af7a8f873`  |
| 2709   | Layout 1 | `a95af7a8f873`  |
| 2703   | Layout 1 | `a95af7a8f873`  |
| 2695   | Layout 1 | `a95af7a8f873`  |
| 2684   | Layout 1 | `a95af7a8f873`  |
| 2672   | Layout 1 | `a95af7a8f873`  |
| 2665   | Layout 1 | `a95af7a8f873`  |
| 2657   | Layout 1 | `a95af7a8f873`  |
| 2649   | Layout 1 | `a95af7a8f873`  |
| 2644   | Layout 1 | `a95af7a8f873`  |
| 2637   | Layout 1 | `a95af7a8f873`  |
| 2629   | Layout 1 | `a95af7a8f873`  |
| 2619   | Layout 1 | `a95af7a8f873`  |
| 2612   | Layout 1 | `a95af7a8f873`  |
| 2606   | Layout 1 | `a95af7a8f873`  |
| 2602   | Layout 1 | `a95af7a8f873`  |
| 2601   | Layout 1 | `a95af7a8f873`  |
| 2592   | Layout 1 | `a95af7a8f873`  |
| 2583   | Layout 1 | `a95af7a8f873`  |
| 2575   | Layout 1 | `a95af7a8f873`  |
| 2567   | Layout 1 | `a95af7a8f873`  |
| 2560   | Layout 1 | `a95af7a8f873`  |
| 2553   | Layout 1 | `a95af7a8f873`  |
| 2545   | Layout 1 | `a95af7a8f873`  |
| 2538   | Layout 1 | `a95af7a8f873`  |
| 2529   | Layout 1 | `a95af7a8f873`  |
| 2519   | Layout 1 | `a95af7a8f873`  |
| 2513   | Layout 1 | `a95af7a8f873`  |
| 2510   | Layout 1 | `a95af7a8f873`  |
| 2507   | Layout 1 | `a95af7a8f873`  |
| 2503   | Layout 1 | `a95af7a8f873`  |
| 2498   | Layout 1 | `a95af7a8f873`  |
| 2492   | Layout 1 | `a95af7a8f873`  |
| 2487   | Layout 1 | `a95af7a8f873`  |
| 2480   | Layout 1 | `a95af7a8f873`  |
| 2474   | Layout 1 | `a95af7a8f873`  |
| 2468   | Layout 1 | `a95af7a8f873`  |
| 2460   | Layout 1 | `a95af7a8f873`  |
| 2453   | Layout 1 | `a95af7a8f873`  |
| 2444   | Layout 1 | `a95af7a8f873`  |
| 2438   | Layout 1 | `a95af7a8f873`  |
| 2434   | Layout 1 | `a95af7a8f873`  |
| 2429   | Layout 1 | `a95af7a8f873`  |
| 2421   | Layout 1 | `a95af7a8f873`  |
| 2414   | Layout 1 | `a95af7a8f873`  |
| 2407   | Layout 1 | `a95af7a8f873`  |
| 2401   | Layout 1 | `a95af7a8f873`  |
| 2397   | Layout 1 | `a95af7a8f873`  |
| 2393   | Layout 1 | `a95af7a8f873`  |
| 2384   | Layout 1 | `a95af7a8f873`  |
| 2378   | Layout 1 | `a95af7a8f873`  |
| 2372   | Layout 1 | `a95af7a8f873`  |
| 2358   | Layout 1 | `a95af7a8f873`  |
| 2352   | Layout 1 | `a95af7a8f873`  |
| 2347   | Layout 1 | `a95af7a8f873`  |
| 2343   | Layout 1 | `a95af7a8f873`  |
| 2335   | Layout 1 | `a95af7a8f873`  |
| 2327   | Layout 1 | `a95af7a8f873`  |
| 2324   | Layout 1 | `a95af7a8f873`  |
| 2319   | Layout 1 | `a95af7a8f873`  |
| 2313   | Layout 1 | `a95af7a8f873`  |
| 2308   | Layout 1 | `a95af7a8f873`  |
| 2302   | Layout 1 | `a95af7a8f873`  |
| 2295   | Layout 1 | `a95af7a8f873`  |
| 2290   | Layout 1 | `a95af7a8f873`  |
| 2284   | Layout 1 | `a95af7a8f873`  |
| 2276   | Layout 1 | `a95af7a8f873`  |
| 2269   | Layout 1 | `a95af7a8f873`  |
| 2259   | Layout 1 | `a95af7a8f873`  |
| 2250   | Layout 1 | `a95af7a8f873`  |
| 2243   | Layout 1 | `a95af7a8f873`  |
| 2235   | Layout 1 | `a95af7a8f873`  |
| 2229   | Layout 1 | `a95af7a8f873`  |
| 2224   | Layout 1 | `a95af7a8f873`  |
| 2218   | Layout 1 | `a95af7a8f873`  |
| 2215   | Layout 1 | `a95af7a8f873`  |
| 2207   | Layout 1 | `a95af7a8f873`  |
| 2203   | Layout 1 | `a95af7a8f873`  |
| 2196   | Layout 1 | `a95af7a8f873`  |
| 2192   | Layout 1 | `a95af7a8f873`  |
| 2189   | Layout 1 | `a95af7a8f873`  |
| 2183   | Layout 1 | `a95af7a8f873`  |
| 2179   | Layout 1 | `a95af7a8f873`  |
| 2171   | Layout 1 | `a95af7a8f873`  |
| 2163   | Layout 1 | `a95af7a8f873`  |
| 2156   | Layout 1 | `a95af7a8f873`  |
| 2151   | Layout 1 | `a95af7a8f873`  |
| 2147   | Layout 1 | `a95af7a8f873`  |
| 2142   | Layout 1 | `a95af7a8f873`  |
| 2138   | Layout 1 | `a95af7a8f873`  |
| 2134   | Layout 1 | `a95af7a8f873`  |
| 2130   | Layout 1 | `a95af7a8f873`  |
| 2122   | Layout 1 | `a95af7a8f873`  |
| 2107   | Layout 1 | `a95af7a8f873`  |
| 2098   | Layout 1 | `a95af7a8f873`  |
| 2089   | Layout 1 | `a95af7a8f873`  |
| 2081   | Layout 1 | `a95af7a8f873`  |
| 2073   | Layout 1 | `a95af7a8f873`  |
| 2067   | Layout 1 | `a95af7a8f873`  |
| 2063   | Layout 1 | `a95af7a8f873`  |
| 2059   | Layout 1 | `a95af7a8f873`  |
| 2052   | Layout 1 | `a95af7a8f873`  |
| 2044   | Layout 1 | `a95af7a8f873`  |
| 2039   | Layout 1 | `a95af7a8f873`  |
| 2032   | Layout 1 | `a95af7a8f873`  |
| 2025   | Layout 1 | `a95af7a8f873`  |
| 2011   | Layout 1 | `a95af7a8f873`  |
| 2005   | Layout 1 | `a95af7a8f873`  |
| 2000   | Layout 1 | `a95af7a8f873`  |
| 1996   | Layout 1 | `a95af7a8f873`  |
| 1991   | Layout 1 | `a95af7a8f873`  |
| 1985   | Layout 1 | `a95af7a8f873`  |
| 1980   | Layout 1 | `a95af7a8f873`  |
| 1969   | Layout 1 | `a95af7a8f873`  |
| 1964   | Layout 1 | `a95af7a8f873`  |
| 1958   | Layout 1 | `a95af7a8f873`  |
| 1950   | Layout 1 | `a95af7a8f873`  |
| 1945   | Layout 1 | `a95af7a8f873`  |
| 1937   | Layout 1 | `a95af7a8f873`  |
| 1933   | Layout 1 | `a95af7a8f873`  |
| 1927   | Layout 1 | `a95af7a8f873`  |
| 1921   | Layout 1 | `a95af7a8f873`  |
| 1914   | Layout 1 | `a95af7a8f873`  |
| 1908   | Layout 1 | `a95af7a8f873`  |
| 1897   | Layout 1 | `a95af7a8f873`  |
| 1892   | Layout 1 | `a95af7a8f873`  |
| 1886   | Layout 1 | `a95af7a8f873`  |
| 1881   | Layout 1 | `a95af7a8f873`  |
| 1871   | Layout 1 | `a95af7a8f873`  |
| 1866   | Layout 1 | `a95af7a8f873`  |
| 1862   | Layout 1 | `a95af7a8f873`  |
| 1854   | Layout 1 | `a95af7a8f873`  |
| 1846   | Layout 1 | `a95af7a8f873`  |
| 1838   | Layout 1 | `a95af7a8f873`  |
| 1832   | Layout 1 | `a95af7a8f873`  |
| 1826   | Layout 1 | `a95af7a8f873`  |
| 1822   | Layout 1 | `a95af7a8f873`  |
| 1818   | Layout 1 | `a95af7a8f873`  |
| 1804   | Layout 1 | `a95af7a8f873`  |
| 1794   | Layout 1 | `a95af7a8f873`  |
| 1790   | Layout 1 | `a95af7a8f873`  |
| 1784   | Layout 1 | `a95af7a8f873`  |
| 1774   | Layout 1 | `a95af7a8f873`  |
| 1771   | Layout 1 | `a95af7a8f873`  |
| 1762   | Layout 1 | `a95af7a8f873`  |
| 1759   | Layout 1 | `a95af7a8f873`  |
| 1754   | Layout 1 | `a95af7a8f873`  |
| 1749   | Layout 1 | `a95af7a8f873`  |
| 1743   | Layout 1 | `a95af7a8f873`  |
| 1737   | Layout 1 | `a95af7a8f873`  |
| 1731   | Layout 1 | `a95af7a8f873`  |
| 1725   | Layout 1 | `a95af7a8f873`  |
| 1717   | Layout 1 | `a95af7a8f873`  |
| 1710   | Layout 1 | `a95af7a8f873`  |
| 1704   | Layout 1 | `a95af7a8f873`  |
| 1698   | Layout 1 | `a95af7a8f873`  |
| 1690   | Layout 1 | `a95af7a8f873`  |
| 1685   | Layout 1 | `a95af7a8f873`  |
| 1680   | Layout 1 | `a95af7a8f873`  |
| 1674   | Layout 1 | `a95af7a8f873`  |
| 1668   | Layout 1 | `a95af7a8f873`  |
| 1659   | Layout 1 | `a95af7a8f873`  |
| 1649   | No file  | `a95af7a8f873`  |
| 1642   | No file  | `a95af7a8f873`  |
| 1636   | No file  | `a95af7a8f873`  |
| 1628   | No file  | `a95af7a8f873`  |
| 1622   | No file  | `a95af7a8f873`  |
| 1614   | No file  | `a95af7a8f873`  |
| 1608   | No file  | `a95af7a8f873`  |
| 1602   | No file  | `a95af7a8f873`  |
| 1598   | No file  | `a95af7a8f873`  |
| 1594   | No file  | `a95af7a8f873`  |
| 1590   | No file  | `a95af7a8f873`  |
| 1587   | No file  | `a95af7a8f873`  |
| 1584   | No file  | `a95af7a8f873`  |
| 1579   | No file  | `a95af7a8f873`  |
| 1572   | No file  | `a95af7a8f873`  |
| 1565   | No file  | `a95af7a8f873`  |
| 1559   | No file  | `a95af7a8f873`  |
| 1554   | No file  | `a95af7a8f873`  |
| 1547   | No file  | `a95af7a8f873`  |
| 1537   | No file  | `a95af7a8f873`  |
| 1529   | No file  | `a95af7a8f873`  |
| 1524   | No file  | `a95af7a8f873`  |
| 1519   | No file  | `a95af7a8f873`  |
| 1509   | No file  | `a95af7a8f873`  |
| 1506   | No file  | `a95af7a8f873`  |
| 1504   | No file  | `a95af7a8f873`  |
| 1500   | No file  | `a95af7a8f873`  |
| 1493   | No file  | `a95af7a8f873`  |
| 1489   | No file  | `a95af7a8f873`  |
| 1485   | No file  | `a95af7a8f873`  |
| 1481   | No file  | `a95af7a8f873`  |
| 1474   | No file  | `a95af7a8f873`  |
| 1466   | No file  | `a95af7a8f873`  |
| 1462   | No file  | `a95af7a8f873`  |
| 1459   | No file  | `a95af7a8f873`  |
| 1453   | No file  | `a95af7a8f873`  |
| 1450   | No file  | `a95af7a8f873`  |
| 1445   | No file  | `a95af7a8f873`  |
| 1439   | No file  | `a95af7a8f873`  |
| 1433   | No file  | `a95af7a8f873`  |
| 1430   | No file  | `a95af7a8f873`  |
| 1426   | No file  | `a95af7a8f873`  |
| 1421   | No file  | `a95af7a8f873`  |
| 1417   | No file  | `a95af7a8f873`  |
| 1416   | No file  | `a95af7a8f873`  |
| 1409   | No file  | `a95af7a8f873`  |
| 1405   | No file  | `a95af7a8f873`  |
| 1401   | No file  | `a95af7a8f873`  |
| 1396   | No file  | `a95af7a8f873`  |
| 1391   | No file  | `a95af7a8f873`  |
| 1390   | No file  | `a95af7a8f873`  |
| 1386   | No file  | `a95af7a8f873`  |
| 1381   | No file  | `a95af7a8f873`  |
| 1379   | No file  | `a95af7a8f873`  |
| 1372   | No file  | `a95af7a8f873`  |
| 1366   | No file  | `a95af7a8f873`  |
| 1364   | No file  | `a95af7a8f873`  |
| 1363   | No file  | `a95af7a8f873`  |
| 1360   | No file  | `a95af7a8f873`  |
| 1358   | No file  | `a95af7a8f873`  |
| 1355   | No file  | `a95af7a8f873`  |
| 1351   | No file  | `a95af7a8f873`  |
| 1348   | No file  | `a95af7a8f873`  |
| 1346   | No file  | `a95af7a8f873`  |
| 1341   | No file  | `a95af7a8f873`  |
| 1340   | No file  | `a95af7a8f873`  |
| 1338   | No file  | `a95af7a8f873`  |
| 1335   | No file  | `a95af7a8f873`  |
| 1333   | No file  | `a95af7a8f873`  |
| 1329   | No file  | `a95af7a8f873`  |
| 1327   | No file  | `a95af7a8f873`  |
| 1324   | No file  | `a95af7a8f873`  |
| 1321   | No file  | `a95af7a8f873`  |
| 1319   | No file  | `a95af7a8f873`  |
| 1318   | No file  | `a95af7a8f873`  |
| 1316   | No file  | `a95af7a8f873`  |
| 1313   | No file  | `a95af7a8f873`  |
| 1311   | No file  | `a95af7a8f873`  |
| 1309   | No file  | `a95af7a8f873`  |
| 1304   | No file  | `a95af7a8f873`  |
| 1292   | No file  | `a95af7a8f873`  |
| 1286   | No file  | `a95af7a8f873`  |
| 1280   | No file  | `a95af7a8f873`  |
| 1276   | No file  | `a95af7a8f873`  |
| 1267   | No file  | `a95af7a8f873`  |
| 1261   | No file  | `a95af7a8f873`  |
| 1256   | No file  | `a95af7a8f873`  |
| 1250   | No file  | `a95af7a8f873`  |
| 1246   | No file  | `a95af7a8f873`  |
| 1239   | No file  | `a95af7a8f873`  |
| 1230   | No file  | `a95af7a8f873`  |
| 1226   | No file  | `a95af7a8f873`  |
| 1220   | No file  | `a95af7a8f873`  |
| 1217   | No file  | `a95af7a8f873`  |
| 1211   | No file  | `a95af7a8f873`  |
| 1210   | No file  | `a95af7a8f873`  |
| 1208   | No file  | `a95af7a8f873`  |
| 1203   | No file  | `a95af7a8f873`  |
| 1197   | No file  | `a95af7a8f873`  |
| 1194   | No file  | `a95af7a8f873`  |
| 1192   | No file  | `a95af7a8f873`  |
| 1187   | No file  | `a95af7a8f873`  |
| 1183   | No file  | `a95af7a8f873`  |
| 1177   | No file  | `a95af7a8f873`  |
| 1173   | No file  | `a95af7a8f873`  |
| 1167   | No file  | `a95af7a8f873`  |
| 1164   | No file  | `a95af7a8f873`  |
| 1156   | No file  | `a95af7a8f873`  |
| 1149   | No file  | `a95af7a8f873`  |
| 1144   | No file  | `a95af7a8f873`  |
| 1137   | No file  | `a95af7a8f873`  |
| 1132   | No file  | `a95af7a8f873`  |
| 1127   | No file  | `a95af7a8f873`  |
| 1122   | No file  | `a95af7a8f873`  |
| 1118   | No file  | `a95af7a8f873`  |
| 1114   | No file  | `a95af7a8f873`  |
| 1109   | No file  | `a95af7a8f873`  |
| 1102   | No file  | `a95af7a8f873`  |
| 1096   | No file  | `a95af7a8f873`  |
| 1088   | No file  | `a95af7a8f873`  |
| 1081   | No file  | `a95af7a8f873`  |
| 1076   | No file  | `a95af7a8f873`  |
| 1069   | No file  | `a95af7a8f873`  |
| 1064   | No file  | `a95af7a8f873`  |
| 1058   | No file  | `a95af7a8f873`  |
| 1051   | No file  | `a95af7a8f873`  |
| 1044   | No file  | `a95af7a8f873`  |
| 1036   | No file  | `a95af7a8f873`  |
| 1026   | No file  | `a95af7a8f873`  |
| 1016   | No file  | `a95af7a8f873`  |
| 1009   | No file  | `a95af7a8f873`  |
| 1005   | No file  | `a95af7a8f873`  |
| 1000   | No file  | `a95af7a8f873`  |
| 998    | No file  | `a95af7a8f873`  |
| 990    | No file  | `a95af7a8f873`  |
| 979    | No file  | `a95af7a8f873`  |
| 972    | No file  | `a95af7a8f873`  |
| 963    | No file  | `a95af7a8f873`  |
| 955    | No file  | `a95af7a8f873`  |
| 946    | No file  | `a95af7a8f873`  |
| 938    | No file  | `a95af7a8f873`  |
| 927    | No file  | `a95af7a8f873`  |
| 911    | No file  | `a95af7a8f873`  |
| 904    | No file  | `a95af7a8f873`  |
| 899    | No file  | `a95af7a8f873`  |
| 894    | No file  | `a95af7a8f873`  |
| 885    | No file  | `a95af7a8f873`  |
| 879    | No file  | `a95af7a8f873`  |
| 872    | No file  | `a95af7a8f873`  |
| 864    | No file  | `a95af7a8f873`  |
| 855    | No file  | `a95af7a8f873`  |
| 853    | No file  | `a95af7a8f873`  |
| 845    | No file  | `a95af7a8f873`  |
| 837    | No file  | `a95af7a8f873`  |
| 829    | No file  | `a95af7a8f873`  |
| 822    | No file  | `a95af7a8f873`  |
| 814    | No file  | `a95af7a8f873`  |
| 805    | No file  | `a95af7a8f873`  |
| 794    | No file  | `a95af7a8f873`  |
| 787    | No file  | `a95af7a8f873`  |
| 780    | No file  | `a95af7a8f873`  |
| 771    | No file  | `a95af7a8f873`  |
| 760    | No file  | `a95af7a8f873`  |
| 748    | No file  | `a95af7a8f873`  |
| 741    | No file  | `a95af7a8f873`  |
| 736    | No file  | `a95af7a8f873`  |
| 731    | No file  | `a95af7a8f873`  |
| 723    | No file  | `a95af7a8f873`  |
| 711    | No file  | `a95af7a8f873`  |
| 707    | No file  | `a95af7a8f873`  |
| 697    | No file  | `a95af7a8f873`  |
| 689    | No file  | `a95af7a8f873`  |
| 683    | No file  | `a95af7a8f873`  |
| 678    | No file  | `a95af7a8f873`  |
| 670    | No file  | `a95af7a8f873`  |
| 661    | No file  | `a95af7a8f873`  |
| 656    | No file  | `a95af7a8f873`  |
| 652    | No file  | `a95af7a8f873`  |
| 643    | No file  | `a95af7a8f873`  |
| 637    | No file  | `a95af7a8f873`  |
| 630    | No file  | `a95af7a8f873`  |
| 627    | No file  | `a95af7a8f873`  |
| 621    | No file  | `a95af7a8f873`  |
| 617    | No file  | `a95af7a8f873`  |
| 615    | No file  | `a95af7a8f873`  |
| 606    | No file  | `a95af7a8f873`  |
| 599    | No file  | `a95af7a8f873`  |
| 592    | No file  | `a95af7a8f873`  |
| 586    | No file  | `a95af7a8f873`  |
| 577    | No file  | `a95af7a8f873`  |
| 569    | No file  | `a95af7a8f873`  |
| 561    | No file  | `a95af7a8f873`  |
| 554    | No file  | `a95af7a8f873`  |
| 542    | No file  | `a95af7a8f873`  |
| 532    | No file  | `a95af7a8f873`  |
| 531    | No file  | `a95af7a8f873`  |
| 526    | No file  | `a95af7a8f873`  |
| 521    | No file  | `a95af7a8f873`  |
| 517    | No file  | `a95af7a8f873`  |
| 510    | No file  | `a95af7a8f873`  |
| 508    | No file  | `a95af7a8f873`  |
| 504    | No file  | `a95af7a8f873`  |
| 497    | No file  | `a95af7a8f873`  |
| 491    | No file  | `a95af7a8f873`  |
| 485    | No file  | `a95af7a8f873`  |
| 478    | No file  | `a95af7a8f873`  |
| 472    | No file  | `a95af7a8f873`  |
| 466    | No file  | `a95af7a8f873`  |
| 457    | No file  | `a95af7a8f873`  |
| 452    | No file  | `a95af7a8f873`  |
| 449    | No file  | `a95af7a8f873`  |
| 435    | No file  | `a95af7a8f873`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                     |
| --------------------- | -------- | ------------------------ |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field                     | Notes                                                    |
| ------------------- | -------------- | ------------------------- | -------------------------------------------------------- |
| `+0x00`             | char[4]        | magic                     | ASCII `PABR`                                             |
| `+0x04`             | u32            | row_count                 | Number of rows                                           |
| `+0x08`             | Row[row_count] | rows                      | See Row; byte-packed                                     |
| `rows+0x00`         | u32            | anger_point_per_death     | `200` on clients 1784 and 3482                           |
| `rows+0x04`         | u32            | max_anger_point           | `10000`; `ToClient_GetMaxAngerPoint()`                   |
| `rows+0x08`         | u32            | anger_point_per_kill      | `100` on clients 1784 and 3482                           |
| `rows+0x0C`         | u32            | increase_point            | `100` on clients 1784 and 3482                           |
| `rows+0x10`         | u32            | decrease_survival_percent | `900000` (90% on the 1,000,000 = 100% scale)             |
| `rows+0x14`         | u32            | decrease_survival_point   | `100` on clients 1784 and 3482                           |
| `rows+0x18`         | u32            | increase_survival_percent | `500000` (50%)                                           |
| `rows+0x1C`         | u32            | increase_survival_point   | `200` on clients 1784 and 3482                           |
| `rows+0x20`         | String Table   | string_table              | See String Table                                         |
| `string_table+0x00` | u32            | table_start               | Offset of the string table, where the eight u32 end      |
| `string_table+0x04` | u32            | zero                      | Always `0`                                               |

### Row (8 bytes)

| Offset  | Type | Field                     | Notes                                                                       |
| ------- | ---- | ------------------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16  | skill_no                  | `skilltype.dbss` skill number; one row each                                 |
| `+0x02` | u32  | resource_point            | Cost in the resource; `10000` on the resource type `1` rows, else `0`       |
| `+0x06` | u8   | siege_anger_skill_type    | `2`, `3` or `4`; see Skills                                                 |
| `+0x07` | u8   | siege_skill_resource_type | `1` on the two rows that cost Spirit of Battle, else `0`                    |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Skills

Client 3482, in file order, with the LOC type 10 skill name. Every
`resource_point` is `0` but the two type `1` rows.

| `skill_no` | Name                     | `siege_anger_skill_type` | `siege_skill_resource_type` |
| ---------- | ------------------------ | ------------------------ | --------------------------- |
| 65216      | Breath of Life           | 3                        | 1                           |
| 62846      | BreezyVoyage             | 4                        | 0                           |
| 65227      | Blessing of Battle       | 3                        | 1                           |
| 65225      | Battle Command to Gather | 3                        | 0                           |
| 65033      | Call of the Lord         | 2                        | 0                           |
| 65202      | Boost Morale             | 3                        | 0                           |
| 65106      | Horrors of Battle        | 3                        | 0                           |
| 62845      | Seaforge Blessing        | 4                        | 0                           |
| 65108      | Battle Reorganization I  | 3                        | 0                           |
| 65109      | Frenzied Fighter         | 3                        | 0                           |
| 65111      | Intimidating Force       | 3                        | 0                           |
| 62848      | Admiral's Rally          | 4                        | 0                           |
| 65209      | Healing Touch            | 3                        | 0                           |
| 65211      | Battle Reorganization II | 3                        | 0                           |
| 62847      | Seawatch Pulse           | 4                        | 0                           |

Client 1784 has the 11 rows with types `2` and `3`, in the same order;
client 3482 adds the four type `4` skills `62845` to `62848`.

## Field Names

The `SiegeAngerSkill` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `SkillNo`, `ResourcePoint`, `SkillType` and
`ResourceType`, and its 11 rows match the 11 rows of the client 1784 file
in order and value (11 of 11). That server's dump (client 1784) names the
members `SiegeAngerSkillStaticStatus _skillNo`, `_resourcePoint`,
`_siegeAngerSkillType` and `_siegeSkillResourceType`; the field names are
these members.

The eight u32 after the rows are the `SiegeAngerPoint` sheet (client 1784,
one row). The dump checks its columns in the order
`AngerPointPerDeath`, `MaxAngerPoint`, `AngerPointPerKill`,
`IncreasePoint`, `DecreaseSurvivalPercent`, `DecreasesurvivalPoint`,
`IncreaseSurvivalPercent`, `IncreaseSurvivalPoint`, then the four
distance columns. In that order the sheet's values are the client 1784
file's eight u32 (8 of 8); in the sheet's own column order
(`MaxAngerPoint` first) only five of eight match. `anger_point_per_kill`
and `increase_point` are both `100` on every client checked, so their
order rests on the dump alone. The four distance columns
(`AngerPointDeathDistance` to `AngerPointEffectiveCastleDistance`, `6500`
each in the sheet) are not in this file.

The client Lua of client 3482 reads `ToClient_GetMaxAngerPoint()` and
`ToClient_GetCostPointSiegeAngerSkill(skillNo)` and shows a skill's cost
as cost / maximum when `ToClient_SiegeSkillResourceType(skillNo)` is
`__eSiegeSkillResourceType_SiegeAngerPoint`
(`panel_tooltip_skillgroup_1.luac`). The gauge tooltip
`LUA_ANGRYPOINT_DESC` reads "Can obtain by fighting in Node/Conquest
Wars. Consume Spirit of Battle to cast certain Guild Skills."

## Notes

- The two `resource_point` `10000` rows cost 100% of `max_anger_point`.
- The type `4` skills (Seaforge Blessing, Admiral's Rally and two more)
  have Blue Battlefield names.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  one line per skill with its name, and the eight gauge values (stored
  once) on every line, the two rates as percentages.

## Open Questions

### Skill Type and Resource Type Values

`siege_anger_skill_type` is `2` (Call of the Lord), `3` (the Node War and
Conquest War guild skills) or `4` (four Blue Battlefield skills). The client
Lua has no `__eSiegeAngerSkillType` constant and the 2016 PDB no enum, so
the values have no names. For `siege_skill_resource_type` the Lua only
names `__eSiegeSkillResourceType_SiegeAngerPoint`, without its value; the
two rows that cost the gauge hold `1`.
