# `skillfusionslotlist.bss` Format

## Purpose

The Skill Enhancement choices of each class, grouped by slot: one row per
class type with five slots, each a list of
[`skillfusion.dbss`](skillfusion_dbss.md) keys. On client 3482 every class
offers two enhanced skills in each of slots 0, 1 and 2 (Warrior slot 0:
Seismic Strike or Frenzied Spear); slots 3 and 4 are empty.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records                 | Row bytes               |
| ------ | -------------- | ------- | ------------------------- | ------ | ----------------------- | ----------------------- |
| 1      | 1246 and later | 3483    | `skillfusionslotlist.bss` | 41,204 | 505 Slot, 101 Class Row | 4 to 260, 82 on average |

| Layout | File                      | Known             | Unknown    |
| ------ | ------------------------- | ----------------- | ---------- |
| 1      | `skillfusionslotlist.bss` | 41,204 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `ca2c37519b0f`  |
| 3482   | Layout 1 | `ca2c37519b0f`  |
| 3474   | Layout 1 | `ca2c37519b0f`  |
| 3473   | Layout 1 | `ca2c37519b0f`  |
| 3464   | Layout 1 | `ca2c37519b0f`  |
| 3458   | Layout 1 | `ca2c37519b0f`  |
| 3454   | Layout 1 | `ca2c37519b0f`  |
| 3444   | Layout 1 | `ca2c37519b0f`  |
| 3435   | Layout 1 | `ca2c37519b0f`  |
| 3426   | Layout 1 | `ca2c37519b0f`  |
| 3418   | Layout 1 | `ca2c37519b0f`  |
| 3412   | Layout 1 | `ca2c37519b0f`  |
| 3402   | Layout 1 | `ca2c37519b0f`  |
| 3396   | Layout 1 | `ca2c37519b0f`  |
| 3387   | Layout 1 | `ca2c37519b0f`  |
| 3381   | Layout 1 | `ca2c37519b0f`  |
| 3373   | Layout 1 | `ca2c37519b0f`  |
| 3364   | Layout 1 | `ca2c37519b0f`  |
| 3356   | Layout 1 | `ca2c37519b0f`  |
| 3349   | Layout 1 | `ca2c37519b0f`  |
| 3342   | Layout 1 | `ca2c37519b0f`  |
| 3335   | Layout 1 | `ca2c37519b0f`  |
| 3326   | Layout 1 | `ca2c37519b0f`  |
| 3321   | Layout 1 | `ca2c37519b0f`  |
| 3314   | Layout 1 | `ca2c37519b0f`  |
| 3303   | Layout 1 | `ca2c37519b0f`  |
| 3302   | Layout 1 | `ca2c37519b0f`  |
| 3293   | Layout 1 | `ca2c37519b0f`  |
| 3283   | Layout 1 | `ca2c37519b0f`  |
| 3275   | Layout 1 | `ca2c37519b0f`  |
| 3267   | Layout 1 | `ca2c37519b0f`  |
| 3258   | Layout 1 | `ca2c37519b0f`  |
| 3251   | Layout 1 | `ca2c37519b0f`  |
| 3242   | Layout 1 | `ca2c37519b0f`  |
| 3235   | Layout 1 | `ca2c37519b0f`  |
| 3229   | Layout 1 | `ca2c37519b0f`  |
| 3212   | Layout 1 | `ca2c37519b0f`  |
| 3203   | Layout 1 | `ca2c37519b0f`  |
| 3193   | Layout 1 | `ca2c37519b0f`  |
| 3186   | Layout 1 | `ca2c37519b0f`  |
| 3177   | Layout 1 | `ca2c37519b0f`  |
| 3169   | Layout 1 | `ca2c37519b0f`  |
| 3158   | Layout 1 | `ca2c37519b0f`  |
| 3151   | Layout 1 | `ca2c37519b0f`  |
| 3144   | Layout 1 | `ca2c37519b0f`  |
| 3133   | Layout 1 | `ca2c37519b0f`  |
| 3125   | Layout 1 | `ca2c37519b0f`  |
| 3118   | Layout 1 | `ca2c37519b0f`  |
| 3111   | Layout 1 | `ca2c37519b0f`  |
| 3103   | Layout 1 | `ca2c37519b0f`  |
| 3095   | Layout 1 | `ca2c37519b0f`  |
| 3086   | Layout 1 | `ca2c37519b0f`  |
| 3072   | Layout 1 | `ca2c37519b0f`  |
| 3062   | Layout 1 | `ca2c37519b0f`  |
| 3052   | Layout 1 | `ca2c37519b0f`  |
| 3045   | Layout 1 | `ca2c37519b0f`  |
| 3037   | Layout 1 | `ca2c37519b0f`  |
| 3030   | Layout 1 | `ca2c37519b0f`  |
| 3021   | Layout 1 | `ca2c37519b0f`  |
| 3012   | Layout 1 | `ca2c37519b0f`  |
| 3002   | Layout 1 | `ca2c37519b0f`  |
| 2995   | Layout 1 | `ca2c37519b0f`  |
| 2987   | Layout 1 | `ca2c37519b0f`  |
| 2978   | Layout 1 | `ca2c37519b0f`  |
| 2970   | Layout 1 | `ca2c37519b0f`  |
| 2959   | Layout 1 | `ca2c37519b0f`  |
| 2951   | Layout 1 | `ca2c37519b0f`  |
| 2942   | Layout 1 | `ca2c37519b0f`  |
| 2935   | Layout 1 | `ca2c37519b0f`  |
| 2932   | Layout 1 | `ca2c37519b0f`  |
| 2923   | Layout 1 | `ca2c37519b0f`  |
| 2919   | Layout 1 | `ca2c37519b0f`  |
| 2907   | Layout 1 | `ca2c37519b0f`  |
| 2900   | Layout 1 | `ca2c37519b0f`  |
| 2891   | Layout 1 | `ca2c37519b0f`  |
| 2882   | Layout 1 | `ca2c37519b0f`  |
| 2872   | Layout 1 | `ca2c37519b0f`  |
| 2863   | Layout 1 | `ca2c37519b0f`  |
| 2855   | Layout 1 | `ca2c37519b0f`  |
| 2849   | Layout 1 | `ca2c37519b0f`  |
| 2844   | Layout 1 | `ca2c37519b0f`  |
| 2834   | Layout 1 | `ca2c37519b0f`  |
| 2825   | Layout 1 | `ca2c37519b0f`  |
| 2819   | Layout 1 | `ca2c37519b0f`  |
| 2811   | Layout 1 | `ca2c37519b0f`  |
| 2803   | Layout 1 | `ca2c37519b0f`  |
| 2794   | Layout 1 | `ca2c37519b0f`  |
| 2783   | Layout 1 | `ca2c37519b0f`  |
| 2774   | Layout 1 | `ca2c37519b0f`  |
| 2765   | Layout 1 | `ca2c37519b0f`  |
| 2756   | Layout 1 | `ca2c37519b0f`  |
| 2750   | Layout 1 | `ca2c37519b0f`  |
| 2743   | Layout 1 | `ca2c37519b0f`  |
| 2736   | Layout 1 | `ca2c37519b0f`  |
| 2726   | Layout 1 | `ca2c37519b0f`  |
| 2717   | Layout 1 | `ca2c37519b0f`  |
| 2709   | Layout 1 | `ca2c37519b0f`  |
| 2703   | Layout 1 | `ca2c37519b0f`  |
| 2695   | Layout 1 | `ca2c37519b0f`  |
| 2684   | Layout 1 | `ca2c37519b0f`  |
| 2672   | Layout 1 | `ca2c37519b0f`  |
| 2665   | Layout 1 | `ca2c37519b0f`  |
| 2657   | Layout 1 | `ca2c37519b0f`  |
| 2649   | Layout 1 | `ca2c37519b0f`  |
| 2644   | Layout 1 | `ca2c37519b0f`  |
| 2637   | Layout 1 | `ca2c37519b0f`  |
| 2629   | Layout 1 | `ca2c37519b0f`  |
| 2619   | Layout 1 | `ca2c37519b0f`  |
| 2612   | Layout 1 | `ca2c37519b0f`  |
| 2606   | Layout 1 | `ca2c37519b0f`  |
| 2602   | Layout 1 | `ca2c37519b0f`  |
| 2601   | Layout 1 | `ca2c37519b0f`  |
| 2592   | Layout 1 | `ca2c37519b0f`  |
| 2583   | Layout 1 | `ca2c37519b0f`  |
| 2575   | Layout 1 | `ca2c37519b0f`  |
| 2567   | Layout 1 | `ca2c37519b0f`  |
| 2560   | Layout 1 | `ca2c37519b0f`  |
| 2553   | Layout 1 | `ca2c37519b0f`  |
| 2545   | Layout 1 | `ca2c37519b0f`  |
| 2538   | Layout 1 | `ca2c37519b0f`  |
| 2529   | Layout 1 | `ca2c37519b0f`  |
| 2519   | Layout 1 | `ca2c37519b0f`  |
| 2513   | Layout 1 | `ca2c37519b0f`  |
| 2510   | Layout 1 | `ca2c37519b0f`  |
| 2507   | Layout 1 | `ca2c37519b0f`  |
| 2503   | Layout 1 | `ca2c37519b0f`  |
| 2498   | Layout 1 | `ca2c37519b0f`  |
| 2492   | Layout 1 | `ca2c37519b0f`  |
| 2487   | Layout 1 | `ca2c37519b0f`  |
| 2480   | Layout 1 | `ca2c37519b0f`  |
| 2474   | Layout 1 | `ca2c37519b0f`  |
| 2468   | Layout 1 | `ca2c37519b0f`  |
| 2460   | Layout 1 | `ca2c37519b0f`  |
| 2453   | Layout 1 | `ca2c37519b0f`  |
| 2444   | Layout 1 | `ca2c37519b0f`  |
| 2438   | Layout 1 | `ca2c37519b0f`  |
| 2434   | Layout 1 | `ca2c37519b0f`  |
| 2429   | Layout 1 | `ca2c37519b0f`  |
| 2421   | Layout 1 | `ca2c37519b0f`  |
| 2414   | Layout 1 | `ca2c37519b0f`  |
| 2407   | Layout 1 | `ca2c37519b0f`  |
| 2401   | Layout 1 | `ca2c37519b0f`  |
| 2397   | Layout 1 | `ca2c37519b0f`  |
| 2393   | Layout 1 | `ca2c37519b0f`  |
| 2384   | Layout 1 | `ca2c37519b0f`  |
| 2378   | Layout 1 | `ca2c37519b0f`  |
| 2372   | Layout 1 | `ca2c37519b0f`  |
| 2358   | Layout 1 | `ca2c37519b0f`  |
| 2352   | Layout 1 | `ca2c37519b0f`  |
| 2347   | Layout 1 | `ca2c37519b0f`  |
| 2343   | Layout 1 | `ca2c37519b0f`  |
| 2335   | Layout 1 | `ca2c37519b0f`  |
| 2327   | Layout 1 | `ca2c37519b0f`  |
| 2324   | Layout 1 | `ca2c37519b0f`  |
| 2319   | Layout 1 | `ca2c37519b0f`  |
| 2313   | Layout 1 | `ca2c37519b0f`  |
| 2308   | Layout 1 | `ca2c37519b0f`  |
| 2302   | Layout 1 | `ca2c37519b0f`  |
| 2295   | Layout 1 | `ca2c37519b0f`  |
| 2290   | Layout 1 | `ca2c37519b0f`  |
| 2284   | Layout 1 | `ca2c37519b0f`  |
| 2276   | Layout 1 | `ca2c37519b0f`  |
| 2269   | Layout 1 | `ca2c37519b0f`  |
| 2259   | Layout 1 | `ca2c37519b0f`  |
| 2250   | Layout 1 | `ca2c37519b0f`  |
| 2243   | Layout 1 | `ca2c37519b0f`  |
| 2235   | Layout 1 | `ca2c37519b0f`  |
| 2229   | Layout 1 | `ca2c37519b0f`  |
| 2224   | Layout 1 | `ca2c37519b0f`  |
| 2218   | Layout 1 | `ca2c37519b0f`  |
| 2215   | Layout 1 | `ca2c37519b0f`  |
| 2207   | Layout 1 | `ca2c37519b0f`  |
| 2203   | Layout 1 | `ca2c37519b0f`  |
| 2196   | Layout 1 | `ca2c37519b0f`  |
| 2192   | Layout 1 | `ca2c37519b0f`  |
| 2189   | Layout 1 | `ca2c37519b0f`  |
| 2183   | Layout 1 | `ca2c37519b0f`  |
| 2179   | Layout 1 | `ca2c37519b0f`  |
| 2171   | Layout 1 | `ca2c37519b0f`  |
| 2163   | Layout 1 | `ca2c37519b0f`  |
| 2156   | Layout 1 | `ca2c37519b0f`  |
| 2151   | Layout 1 | `ca2c37519b0f`  |
| 2147   | Layout 1 | `ca2c37519b0f`  |
| 2142   | Layout 1 | `ca2c37519b0f`  |
| 2138   | Layout 1 | `ca2c37519b0f`  |
| 2134   | Layout 1 | `ca2c37519b0f`  |
| 2130   | Layout 1 | `ca2c37519b0f`  |
| 2122   | Layout 1 | `ca2c37519b0f`  |
| 2107   | Layout 1 | `ca2c37519b0f`  |
| 2098   | Layout 1 | `ca2c37519b0f`  |
| 2089   | Layout 1 | `ca2c37519b0f`  |
| 2081   | Layout 1 | `ca2c37519b0f`  |
| 2073   | Layout 1 | `ca2c37519b0f`  |
| 2067   | Layout 1 | `ca2c37519b0f`  |
| 2063   | Layout 1 | `ca2c37519b0f`  |
| 2059   | Layout 1 | `ca2c37519b0f`  |
| 2052   | Layout 1 | `ca2c37519b0f`  |
| 2044   | Layout 1 | `ca2c37519b0f`  |
| 2039   | Layout 1 | `ca2c37519b0f`  |
| 2032   | Layout 1 | `ca2c37519b0f`  |
| 2025   | Layout 1 | `ca2c37519b0f`  |
| 2011   | Layout 1 | `ca2c37519b0f`  |
| 2005   | Layout 1 | `ca2c37519b0f`  |
| 2000   | Layout 1 | `ca2c37519b0f`  |
| 1996   | Layout 1 | `ca2c37519b0f`  |
| 1991   | Layout 1 | `ca2c37519b0f`  |
| 1985   | Layout 1 | `ca2c37519b0f`  |
| 1980   | Layout 1 | `ca2c37519b0f`  |
| 1969   | Layout 1 | `ca2c37519b0f`  |
| 1964   | Layout 1 | `ca2c37519b0f`  |
| 1958   | Layout 1 | `ca2c37519b0f`  |
| 1950   | Layout 1 | `ca2c37519b0f`  |
| 1945   | Layout 1 | `ca2c37519b0f`  |
| 1937   | Layout 1 | `ca2c37519b0f`  |
| 1933   | Layout 1 | `ca2c37519b0f`  |
| 1927   | Layout 1 | `ca2c37519b0f`  |
| 1921   | Layout 1 | `ca2c37519b0f`  |
| 1914   | Layout 1 | `ca2c37519b0f`  |
| 1908   | Layout 1 | `ca2c37519b0f`  |
| 1897   | Layout 1 | `ca2c37519b0f`  |
| 1892   | Layout 1 | `ca2c37519b0f`  |
| 1886   | Layout 1 | `ca2c37519b0f`  |
| 1881   | Layout 1 | `ca2c37519b0f`  |
| 1871   | Layout 1 | `ca2c37519b0f`  |
| 1866   | Layout 1 | `ca2c37519b0f`  |
| 1862   | Layout 1 | `ca2c37519b0f`  |
| 1854   | Layout 1 | `ca2c37519b0f`  |
| 1846   | Layout 1 | `ca2c37519b0f`  |
| 1838   | Layout 1 | `ca2c37519b0f`  |
| 1832   | Layout 1 | `ca2c37519b0f`  |
| 1826   | Layout 1 | `ca2c37519b0f`  |
| 1822   | Layout 1 | `ca2c37519b0f`  |
| 1818   | Layout 1 | `ca2c37519b0f`  |
| 1804   | Layout 1 | `ca2c37519b0f`  |
| 1794   | Layout 1 | `ca2c37519b0f`  |
| 1790   | Layout 1 | `ca2c37519b0f`  |
| 1784   | Layout 1 | `ca2c37519b0f`  |
| 1774   | Layout 1 | `ca2c37519b0f`  |
| 1771   | Layout 1 | `ca2c37519b0f`  |
| 1762   | Layout 1 | `ca2c37519b0f`  |
| 1759   | Layout 1 | `ca2c37519b0f`  |
| 1754   | Layout 1 | `ca2c37519b0f`  |
| 1749   | Layout 1 | `ca2c37519b0f`  |
| 1743   | Layout 1 | `ca2c37519b0f`  |
| 1737   | Layout 1 | `ca2c37519b0f`  |
| 1731   | Layout 1 | `ca2c37519b0f`  |
| 1725   | Layout 1 | `ca2c37519b0f`  |
| 1717   | Layout 1 | `ca2c37519b0f`  |
| 1710   | Layout 1 | `ca2c37519b0f`  |
| 1704   | Layout 1 | `ca2c37519b0f`  |
| 1698   | Layout 1 | `ca2c37519b0f`  |
| 1690   | Layout 1 | `ca2c37519b0f`  |
| 1685   | Layout 1 | `ca2c37519b0f`  |
| 1680   | Layout 1 | `ca2c37519b0f`  |
| 1674   | Layout 1 | `ca2c37519b0f`  |
| 1668   | Layout 1 | `ca2c37519b0f`  |
| 1659   | Layout 1 | `ca2c37519b0f`  |
| 1649   | Layout 1 | `ca2c37519b0f`  |
| 1642   | Layout 1 | `ca2c37519b0f`  |
| 1636   | Layout 1 | `ca2c37519b0f`  |
| 1628   | Layout 1 | `ca2c37519b0f`  |
| 1622   | Layout 1 | `ca2c37519b0f`  |
| 1614   | Layout 1 | `ca2c37519b0f`  |
| 1608   | Layout 1 | `ca2c37519b0f`  |
| 1602   | Layout 1 | `ca2c37519b0f`  |
| 1598   | Layout 1 | `ca2c37519b0f`  |
| 1594   | Layout 1 | `ca2c37519b0f`  |
| 1590   | Layout 1 | `ca2c37519b0f`  |
| 1587   | Layout 1 | `ca2c37519b0f`  |
| 1584   | Layout 1 | `ca2c37519b0f`  |
| 1579   | Layout 1 | `ca2c37519b0f`  |
| 1572   | Layout 1 | `ca2c37519b0f`  |
| 1565   | Layout 1 | `ca2c37519b0f`  |
| 1559   | Layout 1 | `ca2c37519b0f`  |
| 1554   | Layout 1 | `ca2c37519b0f`  |
| 1547   | Layout 1 | `ca2c37519b0f`  |
| 1537   | Layout 1 | `ca2c37519b0f`  |
| 1529   | Layout 1 | `ca2c37519b0f`  |
| 1524   | Layout 1 | `ca2c37519b0f`  |
| 1519   | Layout 1 | `ca2c37519b0f`  |
| 1509   | Layout 1 | `ca2c37519b0f`  |
| 1506   | Layout 1 | `ca2c37519b0f`  |
| 1504   | Layout 1 | `ca2c37519b0f`  |
| 1500   | Layout 1 | `ca2c37519b0f`  |
| 1493   | Layout 1 | `ca2c37519b0f`  |
| 1489   | Layout 1 | `ca2c37519b0f`  |
| 1485   | Layout 1 | `ca2c37519b0f`  |
| 1481   | Layout 1 | `ca2c37519b0f`  |
| 1474   | Layout 1 | `ca2c37519b0f`  |
| 1466   | Layout 1 | `ca2c37519b0f`  |
| 1462   | Layout 1 | `ca2c37519b0f`  |
| 1459   | Layout 1 | `ca2c37519b0f`  |
| 1453   | Layout 1 | `ca2c37519b0f`  |
| 1450   | Layout 1 | `ca2c37519b0f`  |
| 1445   | Layout 1 | `ca2c37519b0f`  |
| 1439   | Layout 1 | `ca2c37519b0f`  |
| 1433   | Layout 1 | `ca2c37519b0f`  |
| 1430   | Layout 1 | `ca2c37519b0f`  |
| 1426   | Layout 1 | `ca2c37519b0f`  |
| 1421   | Layout 1 | `ca2c37519b0f`  |
| 1417   | Layout 1 | `ca2c37519b0f`  |
| 1416   | Layout 1 | `ca2c37519b0f`  |
| 1409   | Layout 1 | `ca2c37519b0f`  |
| 1405   | Layout 1 | `ca2c37519b0f`  |
| 1401   | Layout 1 | `ca2c37519b0f`  |
| 1396   | Layout 1 | `ca2c37519b0f`  |
| 1391   | Layout 1 | `ca2c37519b0f`  |
| 1390   | Layout 1 | `ca2c37519b0f`  |
| 1386   | Layout 1 | `ca2c37519b0f`  |
| 1381   | Layout 1 | `ca2c37519b0f`  |
| 1379   | Layout 1 | `ca2c37519b0f`  |
| 1372   | Layout 1 | `ca2c37519b0f`  |
| 1366   | Layout 1 | `ca2c37519b0f`  |
| 1364   | Layout 1 | `ca2c37519b0f`  |
| 1363   | Layout 1 | `ca2c37519b0f`  |
| 1360   | Layout 1 | `ca2c37519b0f`  |
| 1358   | Layout 1 | `ca2c37519b0f`  |
| 1355   | Layout 1 | `ca2c37519b0f`  |
| 1351   | Layout 1 | `ca2c37519b0f`  |
| 1348   | Layout 1 | `ca2c37519b0f`  |
| 1346   | Layout 1 | `ca2c37519b0f`  |
| 1341   | Layout 1 | `ca2c37519b0f`  |
| 1340   | Layout 1 | `ca2c37519b0f`  |
| 1338   | Layout 1 | `ca2c37519b0f`  |
| 1335   | Layout 1 | `ca2c37519b0f`  |
| 1333   | Layout 1 | `ca2c37519b0f`  |
| 1329   | Layout 1 | `ca2c37519b0f`  |
| 1327   | Layout 1 | `ca2c37519b0f`  |
| 1324   | Layout 1 | `ca2c37519b0f`  |
| 1321   | Layout 1 | `ca2c37519b0f`  |
| 1319   | Layout 1 | `ca2c37519b0f`  |
| 1318   | Layout 1 | `ca2c37519b0f`  |
| 1316   | Layout 1 | `ca2c37519b0f`  |
| 1313   | Layout 1 | `ca2c37519b0f`  |
| 1311   | Layout 1 | `ca2c37519b0f`  |
| 1309   | Layout 1 | `ca2c37519b0f`  |
| 1304   | Layout 1 | `ca2c37519b0f`  |
| 1292   | Layout 1 | `ca2c37519b0f`  |
| 1286   | Layout 1 | `ca2c37519b0f`  |
| 1280   | Layout 1 | `ca2c37519b0f`  |
| 1276   | Layout 1 | `ca2c37519b0f`  |
| 1267   | Layout 1 | `ca2c37519b0f`  |
| 1261   | Layout 1 | `ca2c37519b0f`  |
| 1256   | Layout 1 | `ca2c37519b0f`  |
| 1250   | Layout 1 | `ca2c37519b0f`  |
| 1246   | Layout 1 | `ca2c37519b0f`  |
| 1239   | No file  | `ca2c37519b0f`  |
| 1230   | No file  | `ca2c37519b0f`  |
| 1226   | No file  | `ca2c37519b0f`  |
| 1220   | No file  | `ca2c37519b0f`  |
| 1217   | No file  | `ca2c37519b0f`  |
| 1211   | No file  | `ca2c37519b0f`  |
| 1210   | No file  | `ca2c37519b0f`  |
| 1208   | No file  | `ca2c37519b0f`  |
| 1203   | No file  | `ca2c37519b0f`  |
| 1197   | No file  | `ca2c37519b0f`  |
| 1194   | No file  | `ca2c37519b0f`  |
| 1192   | No file  | `ca2c37519b0f`  |
| 1187   | No file  | `ca2c37519b0f`  |
| 1183   | No file  | `ca2c37519b0f`  |
| 1177   | No file  | `ca2c37519b0f`  |
| 1173   | No file  | `ca2c37519b0f`  |
| 1167   | No file  | `ca2c37519b0f`  |
| 1164   | No file  | `ca2c37519b0f`  |
| 1156   | No file  | `ca2c37519b0f`  |
| 1149   | No file  | `ca2c37519b0f`  |
| 1144   | No file  | `ca2c37519b0f`  |
| 1137   | No file  | `ca2c37519b0f`  |
| 1132   | No file  | `ca2c37519b0f`  |
| 1127   | No file  | `ca2c37519b0f`  |
| 1122   | No file  | `ca2c37519b0f`  |
| 1118   | No file  | `ca2c37519b0f`  |
| 1114   | No file  | `ca2c37519b0f`  |
| 1109   | No file  | `ca2c37519b0f`  |
| 1102   | No file  | `ca2c37519b0f`  |
| 1096   | No file  | `ca2c37519b0f`  |
| 1088   | No file  | `ca2c37519b0f`  |
| 1081   | No file  | `ca2c37519b0f`  |
| 1076   | No file  | `ca2c37519b0f`  |
| 1069   | No file  | `ca2c37519b0f`  |
| 1064   | No file  | `ca2c37519b0f`  |
| 1058   | No file  | `ca2c37519b0f`  |
| 1051   | No file  | `ca2c37519b0f`  |
| 1044   | No file  | `ca2c37519b0f`  |
| 1036   | No file  | `ca2c37519b0f`  |
| 1026   | No file  | `ca2c37519b0f`  |
| 1016   | No file  | `ca2c37519b0f`  |
| 1009   | No file  | `ca2c37519b0f`  |
| 1005   | No file  | `ca2c37519b0f`  |
| 1000   | No file  | `ca2c37519b0f`  |
| 998    | No file  | `ca2c37519b0f`  |
| 990    | No file  | `ca2c37519b0f`  |
| 979    | No file  | `ca2c37519b0f`  |
| 972    | No file  | `ca2c37519b0f`  |
| 963    | No file  | `ca2c37519b0f`  |
| 955    | No file  | `ca2c37519b0f`  |
| 946    | No file  | `ca2c37519b0f`  |
| 938    | No file  | `ca2c37519b0f`  |
| 927    | No file  | `ca2c37519b0f`  |
| 911    | No file  | `ca2c37519b0f`  |
| 904    | No file  | `ca2c37519b0f`  |
| 899    | No file  | `ca2c37519b0f`  |
| 894    | No file  | `ca2c37519b0f`  |
| 885    | No file  | `ca2c37519b0f`  |
| 879    | No file  | `ca2c37519b0f`  |
| 872    | No file  | `ca2c37519b0f`  |
| 864    | No file  | `ca2c37519b0f`  |
| 855    | No file  | `ca2c37519b0f`  |
| 853    | No file  | `ca2c37519b0f`  |
| 845    | No file  | `ca2c37519b0f`  |
| 837    | No file  | `ca2c37519b0f`  |
| 829    | No file  | `ca2c37519b0f`  |
| 822    | No file  | `ca2c37519b0f`  |
| 814    | No file  | `ca2c37519b0f`  |
| 805    | No file  | `ca2c37519b0f`  |
| 794    | No file  | `ca2c37519b0f`  |
| 787    | No file  | `ca2c37519b0f`  |
| 780    | No file  | `ca2c37519b0f`  |
| 771    | No file  | `ca2c37519b0f`  |
| 760    | No file  | `ca2c37519b0f`  |
| 748    | No file  | `ca2c37519b0f`  |
| 741    | No file  | `ca2c37519b0f`  |
| 736    | No file  | `ca2c37519b0f`  |
| 731    | No file  | `ca2c37519b0f`  |
| 723    | No file  | `ca2c37519b0f`  |
| 711    | No file  | `ca2c37519b0f`  |
| 707    | No file  | `ca2c37519b0f`  |
| 697    | No file  | `ca2c37519b0f`  |
| 689    | No file  | `ca2c37519b0f`  |
| 683    | No file  | `ca2c37519b0f`  |
| 678    | No file  | `ca2c37519b0f`  |
| 670    | No file  | `ca2c37519b0f`  |
| 661    | No file  | `ca2c37519b0f`  |
| 656    | No file  | `ca2c37519b0f`  |
| 652    | No file  | `ca2c37519b0f`  |
| 643    | No file  | `ca2c37519b0f`  |
| 637    | No file  | `ca2c37519b0f`  |
| 630    | No file  | `ca2c37519b0f`  |
| 627    | No file  | `ca2c37519b0f`  |
| 621    | No file  | `ca2c37519b0f`  |
| 617    | No file  | `ca2c37519b0f`  |
| 615    | No file  | `ca2c37519b0f`  |
| 606    | No file  | `ca2c37519b0f`  |
| 599    | No file  | `ca2c37519b0f`  |
| 592    | No file  | `ca2c37519b0f`  |
| 586    | No file  | `ca2c37519b0f`  |
| 577    | No file  | `ca2c37519b0f`  |
| 569    | No file  | `ca2c37519b0f`  |
| 561    | No file  | `ca2c37519b0f`  |
| 554    | No file  | `ca2c37519b0f`  |
| 542    | No file  | `ca2c37519b0f`  |
| 532    | No file  | `ca2c37519b0f`  |
| 531    | No file  | `ca2c37519b0f`  |
| 526    | No file  | `ca2c37519b0f`  |
| 521    | No file  | `ca2c37519b0f`  |
| 517    | No file  | `ca2c37519b0f`  |
| 510    | No file  | `ca2c37519b0f`  |
| 508    | No file  | `ca2c37519b0f`  |
| 504    | No file  | `ca2c37519b0f`  |
| 497    | No file  | `ca2c37519b0f`  |
| 491    | No file  | `ca2c37519b0f`  |
| 485    | No file  | `ca2c37519b0f`  |
| 478    | No file  | `ca2c37519b0f`  |
| 472    | No file  | `ca2c37519b0f`  |
| 466    | No file  | `ca2c37519b0f`  |
| 457    | No file  | `ca2c37519b0f`  |
| 452    | No file  | `ca2c37519b0f`  |
| 449    | No file  | `ca2c37519b0f`  |
| 435    | No file  | `ca2c37519b0f`  |

<!-- versions:end -->

## Companion Files

None. Class names come from LOC type 21 and skill names from LOC type 10;
the main and sub skill of each choice are in `skillfusion.dbss`.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset      | Type                     | Field        | Notes                                                         |
| ----------- | ------------------------ | ------------ | ------------------------------------------------------------- |
| `+0x00`     | char[4]                  | magic        | `PABR`                                                        |
| `+0x04`     | Class Row[..table_start] | rows         | No row count: row `n` is class type `n`; 101 rows on clients 1784 and 3482 |
| `rows+0x00` | String Table             | string_table | See String Table                                              |
| `EOF-0x08`  | u32                      | table_start  | Offset of the string table, where `rows` ends                 |
| `EOF-0x04`  | u32                      | zero         | Always `0`                                                    |

### Class Row (variable: 0 bytes + slots)

| Offset  | Type    | Field | Notes                              |
| ------- | ------- | ----- | ---------------------------------- |
| `+0x00` | Slot[5] | slots | Slots 0 to 4 in order; see Slot    |

### Slot (variable: 4 bytes + keys)

| Offset  | Type                         | Field                  | Notes                                                       |
| ------- | ---------------------------- | ---------------------- | ----------------------------------------------------------- |
| `+0x00` | u32                          | skill_fusion_key_count | Number of keys; `0` for an empty slot                       |
| `+0x04` | u32[skill_fusion_key_count]  | skill_fusion_keys      | `skillfusion.dbss` keys, skill keys `skill_no << 16 \| level` (level `1`) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482         |
| `+0x04` | pstr[string_count] | strings      | No field reads a string              |

## Field Names

No sheet has the table's shape; it is `skillfusion.dbss` grouped by class
and `slot_no`. Every key in rows 0 to 50 is a `skillfusion.dbss` key whose
`slot_no` is the slot it sits in: 192 of 192 keys on client 3482, and on
client 1784 the 138 keys of the `SkillFusion` sheet of a private server's
`DataSheets.bexcel`, whose `SlotNo` matches 138 of 138. The list order is
not the sheet's `OrderNo`: on client 3482, 60 of the 96 class lists hold
order `1` first.

## Notes

- The skill window reads the table by class type and slot:
  `panel_window_skillgroup_all_1.luac` (client 3482) loops `index` from `0`
  to `__eSkillFusionSlotMaxCount - 1` and calls
  `ToClient_getFusionSkillNoByClassType(classType, index, 0)`, the first
  choice of each slot. The enum's value is not in the Lua.
- Rows 51 to 100 are the hero class types of LOC type 21 (`51` Cliff, `52`
  Jordine, ... `69` Orwen, then `[PH]` placeholders from `70`). Each holds
  the same three lists: every key of that slot over all classes, 64 keys on
  client 3482 and 46 on client 1784.
- On client 3482 rows 0 to 12, 15 to 17, 19 to 21 and 23 to 35 hold keys:
  32 classes. Client 1784 fills 27 rows below 51, row 6 with four keys per
  slot and the others with two.

## Open Questions

### Why the Hero Rows Hold Every Key

Rows 51 to 100 hold all classes' keys of each slot, while the class rows
below 51 without keys (13, 14, 18 and 22 on client 3482) stay empty.
Whether a hero character can pick any class's enhancement is not in the
Lua.
