# `pearlusedchallengegroup.bss` Format

## Purpose

The groups of Pearl spending challenges in the Pearl Shop window
`panel_ingamecashshop_moonblessing_all`: each row names
a group's main challenge and lists the challenges of the group. A group
appears once per challenge in it, so client 3483 has 33 rows for 7
groups: five weekly event groups of four challenges (`[Event] Use 5,000
Pearls` to `[Event] Use 20,000 Pearls`, August 2021), one of seven and one
of six (`Spend 800 Pearls` to `Spend 44,000 Pearls`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes | Records | Row bytes               |
| ------ | -------------- | ----------------------------- | ----- | ------- | ----------------------- |
| 1      | 1659 and later | `pearlusedchallengegroup.bss` | 680   | 33 Row  | 18 to 24, 20 on average |

| Layout | File                          | Known         | Unknown       |
| ------ | ----------------------------- | ------------- | ------------- |
| 1      | `pearlusedchallengegroup.bss` | 548 B (80.6%) | 132 B (19.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `59656d185f4a`  |
| 3482   | Layout 1 | `59656d185f4a`  |
| 3474   | Layout 1 | `59656d185f4a`  |
| 3473   | Layout 1 | `59656d185f4a`  |
| 3464   | Layout 1 | `59656d185f4a`  |
| 3458   | Layout 1 | `59656d185f4a`  |
| 3454   | Layout 1 | `59656d185f4a`  |
| 3444   | Layout 1 | `59656d185f4a`  |
| 3435   | Layout 1 | `59656d185f4a`  |
| 3426   | Layout 1 | `59656d185f4a`  |
| 3418   | Layout 1 | `59656d185f4a`  |
| 3412   | Layout 1 | `59656d185f4a`  |
| 3402   | Layout 1 | `59656d185f4a`  |
| 3396   | Layout 1 | `59656d185f4a`  |
| 3387   | Layout 1 | `59656d185f4a`  |
| 3381   | Layout 1 | `59656d185f4a`  |
| 3373   | Layout 1 | `59656d185f4a`  |
| 3364   | Layout 1 | `59656d185f4a`  |
| 3356   | Layout 1 | `59656d185f4a`  |
| 3349   | Layout 1 | `59656d185f4a`  |
| 3342   | Layout 1 | `59656d185f4a`  |
| 3335   | Layout 1 | `59656d185f4a`  |
| 3326   | Layout 1 | `59656d185f4a`  |
| 3321   | Layout 1 | `59656d185f4a`  |
| 3314   | Layout 1 | `59656d185f4a`  |
| 3303   | Layout 1 | `59656d185f4a`  |
| 3302   | Layout 1 | `59656d185f4a`  |
| 3293   | Layout 1 | `59656d185f4a`  |
| 3283   | Layout 1 | `59656d185f4a`  |
| 3275   | Layout 1 | `59656d185f4a`  |
| 3267   | Layout 1 | `59656d185f4a`  |
| 3258   | Layout 1 | `59656d185f4a`  |
| 3251   | Layout 1 | `59656d185f4a`  |
| 3242   | Layout 1 | `59656d185f4a`  |
| 3235   | Layout 1 | `59656d185f4a`  |
| 3229   | Layout 1 | `59656d185f4a`  |
| 3212   | Layout 1 | `59656d185f4a`  |
| 3203   | Layout 1 | `59656d185f4a`  |
| 3193   | Layout 1 | `59656d185f4a`  |
| 3186   | Layout 1 | `59656d185f4a`  |
| 3177   | Layout 1 | `59656d185f4a`  |
| 3169   | Layout 1 | `59656d185f4a`  |
| 3158   | Layout 1 | `59656d185f4a`  |
| 3151   | Layout 1 | `59656d185f4a`  |
| 3144   | Layout 1 | `59656d185f4a`  |
| 3133   | Layout 1 | `59656d185f4a`  |
| 3125   | Layout 1 | `59656d185f4a`  |
| 3118   | Layout 1 | `59656d185f4a`  |
| 3111   | Layout 1 | `59656d185f4a`  |
| 3103   | Layout 1 | `59656d185f4a`  |
| 3095   | Layout 1 | `59656d185f4a`  |
| 3086   | Layout 1 | `59656d185f4a`  |
| 3072   | Layout 1 | `59656d185f4a`  |
| 3062   | Layout 1 | `59656d185f4a`  |
| 3052   | Layout 1 | `59656d185f4a`  |
| 3045   | Layout 1 | `59656d185f4a`  |
| 3037   | Layout 1 | `59656d185f4a`  |
| 3030   | Layout 1 | `59656d185f4a`  |
| 3021   | Layout 1 | `59656d185f4a`  |
| 3012   | Layout 1 | `59656d185f4a`  |
| 3002   | Layout 1 | `59656d185f4a`  |
| 2995   | Layout 1 | `59656d185f4a`  |
| 2987   | Layout 1 | `59656d185f4a`  |
| 2978   | Layout 1 | `59656d185f4a`  |
| 2970   | Layout 1 | `59656d185f4a`  |
| 2959   | Layout 1 | `59656d185f4a`  |
| 2951   | Layout 1 | `59656d185f4a`  |
| 2942   | Layout 1 | `59656d185f4a`  |
| 2935   | Layout 1 | `59656d185f4a`  |
| 2932   | Layout 1 | `59656d185f4a`  |
| 2923   | Layout 1 | `59656d185f4a`  |
| 2919   | Layout 1 | `59656d185f4a`  |
| 2907   | Layout 1 | `59656d185f4a`  |
| 2900   | Layout 1 | `59656d185f4a`  |
| 2891   | Layout 1 | `59656d185f4a`  |
| 2882   | Layout 1 | `59656d185f4a`  |
| 2872   | Layout 1 | `59656d185f4a`  |
| 2863   | Layout 1 | `59656d185f4a`  |
| 2855   | Layout 1 | `59656d185f4a`  |
| 2849   | Layout 1 | `59656d185f4a`  |
| 2844   | Layout 1 | `59656d185f4a`  |
| 2834   | Layout 1 | `59656d185f4a`  |
| 2825   | Layout 1 | `59656d185f4a`  |
| 2819   | Layout 1 | `59656d185f4a`  |
| 2811   | Layout 1 | `59656d185f4a`  |
| 2803   | Layout 1 | `59656d185f4a`  |
| 2794   | Layout 1 | `59656d185f4a`  |
| 2783   | Layout 1 | `59656d185f4a`  |
| 2774   | Layout 1 | `59656d185f4a`  |
| 2765   | Layout 1 | `59656d185f4a`  |
| 2756   | Layout 1 | `59656d185f4a`  |
| 2750   | Layout 1 | `59656d185f4a`  |
| 2743   | Layout 1 | `59656d185f4a`  |
| 2736   | Layout 1 | `59656d185f4a`  |
| 2726   | Layout 1 | `59656d185f4a`  |
| 2717   | Layout 1 | `59656d185f4a`  |
| 2709   | Layout 1 | `59656d185f4a`  |
| 2703   | Layout 1 | `59656d185f4a`  |
| 2695   | Layout 1 | `59656d185f4a`  |
| 2684   | Layout 1 | `59656d185f4a`  |
| 2672   | Layout 1 | `59656d185f4a`  |
| 2665   | Layout 1 | `59656d185f4a`  |
| 2657   | Layout 1 | `59656d185f4a`  |
| 2649   | Layout 1 | `59656d185f4a`  |
| 2644   | Layout 1 | `59656d185f4a`  |
| 2637   | Layout 1 | `59656d185f4a`  |
| 2629   | Layout 1 | `59656d185f4a`  |
| 2619   | Layout 1 | `59656d185f4a`  |
| 2612   | Layout 1 | `59656d185f4a`  |
| 2606   | Layout 1 | `59656d185f4a`  |
| 2602   | Layout 1 | `59656d185f4a`  |
| 2601   | Layout 1 | `59656d185f4a`  |
| 2592   | Layout 1 | `59656d185f4a`  |
| 2583   | Layout 1 | `59656d185f4a`  |
| 2575   | Layout 1 | `59656d185f4a`  |
| 2567   | Layout 1 | `59656d185f4a`  |
| 2560   | Layout 1 | `59656d185f4a`  |
| 2553   | Layout 1 | `59656d185f4a`  |
| 2545   | Layout 1 | `59656d185f4a`  |
| 2538   | Layout 1 | `59656d185f4a`  |
| 2529   | Layout 1 | `59656d185f4a`  |
| 2519   | Layout 1 | `59656d185f4a`  |
| 2513   | Layout 1 | `59656d185f4a`  |
| 2510   | Layout 1 | `59656d185f4a`  |
| 2507   | Layout 1 | `59656d185f4a`  |
| 2503   | Layout 1 | `59656d185f4a`  |
| 2498   | Layout 1 | `59656d185f4a`  |
| 2492   | Layout 1 | `59656d185f4a`  |
| 2487   | Layout 1 | `59656d185f4a`  |
| 2480   | Layout 1 | `59656d185f4a`  |
| 2474   | Layout 1 | `59656d185f4a`  |
| 2468   | Layout 1 | `59656d185f4a`  |
| 2460   | Layout 1 | `59656d185f4a`  |
| 2453   | Layout 1 | `59656d185f4a`  |
| 2444   | Layout 1 | `59656d185f4a`  |
| 2438   | Layout 1 | `59656d185f4a`  |
| 2434   | Layout 1 | `59656d185f4a`  |
| 2429   | Layout 1 | `59656d185f4a`  |
| 2421   | Layout 1 | `59656d185f4a`  |
| 2414   | Layout 1 | `59656d185f4a`  |
| 2407   | Layout 1 | `59656d185f4a`  |
| 2401   | Layout 1 | `59656d185f4a`  |
| 2397   | Layout 1 | `59656d185f4a`  |
| 2393   | Layout 1 | `59656d185f4a`  |
| 2384   | Layout 1 | `59656d185f4a`  |
| 2378   | Layout 1 | `59656d185f4a`  |
| 2372   | Layout 1 | `59656d185f4a`  |
| 2358   | Layout 1 | `59656d185f4a`  |
| 2352   | Layout 1 | `59656d185f4a`  |
| 2347   | Layout 1 | `59656d185f4a`  |
| 2343   | Layout 1 | `59656d185f4a`  |
| 2335   | Layout 1 | `59656d185f4a`  |
| 2327   | Layout 1 | `59656d185f4a`  |
| 2324   | Layout 1 | `59656d185f4a`  |
| 2319   | Layout 1 | `59656d185f4a`  |
| 2313   | Layout 1 | `59656d185f4a`  |
| 2308   | Layout 1 | `59656d185f4a`  |
| 2302   | Layout 1 | `59656d185f4a`  |
| 2295   | Layout 1 | `59656d185f4a`  |
| 2290   | Layout 1 | `59656d185f4a`  |
| 2284   | Layout 1 | `59656d185f4a`  |
| 2276   | Layout 1 | `59656d185f4a`  |
| 2269   | Layout 1 | `59656d185f4a`  |
| 2259   | Layout 1 | `59656d185f4a`  |
| 2250   | Layout 1 | `59656d185f4a`  |
| 2243   | Layout 1 | `59656d185f4a`  |
| 2235   | Layout 1 | `59656d185f4a`  |
| 2229   | Layout 1 | `59656d185f4a`  |
| 2224   | Layout 1 | `59656d185f4a`  |
| 2218   | Layout 1 | `59656d185f4a`  |
| 2215   | Layout 1 | `59656d185f4a`  |
| 2207   | Layout 1 | `59656d185f4a`  |
| 2203   | Layout 1 | `59656d185f4a`  |
| 2196   | Layout 1 | `59656d185f4a`  |
| 2192   | Layout 1 | `59656d185f4a`  |
| 2189   | Layout 1 | `59656d185f4a`  |
| 2183   | Layout 1 | `59656d185f4a`  |
| 2179   | Layout 1 | `59656d185f4a`  |
| 2171   | Layout 1 | `59656d185f4a`  |
| 2163   | Layout 1 | `59656d185f4a`  |
| 2156   | Layout 1 | `59656d185f4a`  |
| 2151   | Layout 1 | `59656d185f4a`  |
| 2147   | Layout 1 | `59656d185f4a`  |
| 2142   | Layout 1 | `59656d185f4a`  |
| 2138   | Layout 1 | `59656d185f4a`  |
| 2134   | Layout 1 | `59656d185f4a`  |
| 2130   | Layout 1 | `59656d185f4a`  |
| 2122   | Layout 1 | `59656d185f4a`  |
| 2107   | Layout 1 | `59656d185f4a`  |
| 2098   | Layout 1 | `59656d185f4a`  |
| 2089   | Layout 1 | `59656d185f4a`  |
| 2081   | Layout 1 | `59656d185f4a`  |
| 2073   | Layout 1 | `59656d185f4a`  |
| 2067   | Layout 1 | `59656d185f4a`  |
| 2063   | Layout 1 | `59656d185f4a`  |
| 2059   | Layout 1 | `59656d185f4a`  |
| 2052   | Layout 1 | `59656d185f4a`  |
| 2044   | Layout 1 | `59656d185f4a`  |
| 2039   | Layout 1 | `59656d185f4a`  |
| 2032   | Layout 1 | `59656d185f4a`  |
| 2025   | Layout 1 | `59656d185f4a`  |
| 2011   | Layout 1 | `59656d185f4a`  |
| 2005   | Layout 1 | `59656d185f4a`  |
| 2000   | Layout 1 | `59656d185f4a`  |
| 1996   | Layout 1 | `59656d185f4a`  |
| 1991   | Layout 1 | `59656d185f4a`  |
| 1985   | Layout 1 | `59656d185f4a`  |
| 1980   | Layout 1 | `59656d185f4a`  |
| 1969   | Layout 1 | `59656d185f4a`  |
| 1964   | Layout 1 | `59656d185f4a`  |
| 1958   | Layout 1 | `59656d185f4a`  |
| 1950   | Layout 1 | `59656d185f4a`  |
| 1945   | Layout 1 | `59656d185f4a`  |
| 1937   | Layout 1 | `59656d185f4a`  |
| 1933   | Layout 1 | `59656d185f4a`  |
| 1927   | Layout 1 | `59656d185f4a`  |
| 1921   | Layout 1 | `59656d185f4a`  |
| 1914   | Layout 1 | `59656d185f4a`  |
| 1908   | Layout 1 | `59656d185f4a`  |
| 1897   | Layout 1 | `59656d185f4a`  |
| 1892   | Layout 1 | `59656d185f4a`  |
| 1886   | Layout 1 | `59656d185f4a`  |
| 1881   | Layout 1 | `59656d185f4a`  |
| 1871   | Layout 1 | `59656d185f4a`  |
| 1866   | Layout 1 | `59656d185f4a`  |
| 1862   | Layout 1 | `59656d185f4a`  |
| 1854   | Layout 1 | `59656d185f4a`  |
| 1846   | Layout 1 | `59656d185f4a`  |
| 1838   | Layout 1 | `59656d185f4a`  |
| 1832   | Layout 1 | `59656d185f4a`  |
| 1826   | Layout 1 | `59656d185f4a`  |
| 1822   | Layout 1 | `59656d185f4a`  |
| 1818   | Layout 1 | `59656d185f4a`  |
| 1804   | Layout 1 | `59656d185f4a`  |
| 1794   | Layout 1 | `59656d185f4a`  |
| 1790   | Layout 1 | `59656d185f4a`  |
| 1784   | Layout 1 | `59656d185f4a`  |
| 1774   | Layout 1 | `59656d185f4a`  |
| 1771   | Layout 1 | `59656d185f4a`  |
| 1762   | Layout 1 | `59656d185f4a`  |
| 1759   | Layout 1 | `59656d185f4a`  |
| 1754   | Layout 1 | `59656d185f4a`  |
| 1749   | Layout 1 | `59656d185f4a`  |
| 1743   | Layout 1 | `59656d185f4a`  |
| 1737   | Layout 1 | `59656d185f4a`  |
| 1731   | Layout 1 | `59656d185f4a`  |
| 1725   | Layout 1 | `59656d185f4a`  |
| 1717   | Layout 1 | `59656d185f4a`  |
| 1710   | Layout 1 | `59656d185f4a`  |
| 1704   | Layout 1 | `59656d185f4a`  |
| 1698   | Layout 1 | `59656d185f4a`  |
| 1690   | Layout 1 | `59656d185f4a`  |
| 1685   | Layout 1 | `59656d185f4a`  |
| 1680   | Layout 1 | `59656d185f4a`  |
| 1674   | Layout 1 | `59656d185f4a`  |
| 1668   | Layout 1 | `59656d185f4a`  |
| 1659   | Layout 1 | `59656d185f4a`  |
| 1649   | No file  | `59656d185f4a`  |
| 1642   | No file  | `59656d185f4a`  |
| 1636   | No file  | `59656d185f4a`  |
| 1628   | No file  | `59656d185f4a`  |
| 1622   | No file  | `59656d185f4a`  |
| 1614   | No file  | `59656d185f4a`  |
| 1608   | No file  | `59656d185f4a`  |
| 1602   | No file  | `59656d185f4a`  |
| 1598   | No file  | `59656d185f4a`  |
| 1594   | No file  | `59656d185f4a`  |
| 1590   | No file  | `59656d185f4a`  |
| 1587   | No file  | `59656d185f4a`  |
| 1584   | No file  | `59656d185f4a`  |
| 1579   | No file  | `59656d185f4a`  |
| 1572   | No file  | `59656d185f4a`  |
| 1565   | No file  | `59656d185f4a`  |
| 1559   | No file  | `59656d185f4a`  |
| 1554   | No file  | `59656d185f4a`  |
| 1547   | No file  | `59656d185f4a`  |
| 1537   | No file  | `59656d185f4a`  |
| 1529   | No file  | `59656d185f4a`  |
| 1524   | No file  | `59656d185f4a`  |
| 1519   | No file  | `59656d185f4a`  |
| 1509   | No file  | `59656d185f4a`  |
| 1506   | No file  | `59656d185f4a`  |
| 1504   | No file  | `59656d185f4a`  |
| 1500   | No file  | `59656d185f4a`  |
| 1493   | No file  | `59656d185f4a`  |
| 1489   | No file  | `59656d185f4a`  |
| 1485   | No file  | `59656d185f4a`  |
| 1481   | No file  | `59656d185f4a`  |
| 1474   | No file  | `59656d185f4a`  |
| 1466   | No file  | `59656d185f4a`  |
| 1462   | No file  | `59656d185f4a`  |
| 1459   | No file  | `59656d185f4a`  |
| 1453   | No file  | `59656d185f4a`  |
| 1450   | No file  | `59656d185f4a`  |
| 1445   | No file  | `59656d185f4a`  |
| 1439   | No file  | `59656d185f4a`  |
| 1433   | No file  | `59656d185f4a`  |
| 1430   | No file  | `59656d185f4a`  |
| 1426   | No file  | `59656d185f4a`  |
| 1421   | No file  | `59656d185f4a`  |
| 1417   | No file  | `59656d185f4a`  |
| 1416   | No file  | `59656d185f4a`  |
| 1409   | No file  | `59656d185f4a`  |
| 1405   | No file  | `59656d185f4a`  |
| 1401   | No file  | `59656d185f4a`  |
| 1396   | No file  | `59656d185f4a`  |
| 1391   | No file  | `59656d185f4a`  |
| 1390   | No file  | `59656d185f4a`  |
| 1386   | No file  | `59656d185f4a`  |
| 1381   | No file  | `59656d185f4a`  |
| 1379   | No file  | `59656d185f4a`  |
| 1372   | No file  | `59656d185f4a`  |
| 1366   | No file  | `59656d185f4a`  |
| 1364   | No file  | `59656d185f4a`  |
| 1363   | No file  | `59656d185f4a`  |
| 1360   | No file  | `59656d185f4a`  |
| 1358   | No file  | `59656d185f4a`  |
| 1355   | No file  | `59656d185f4a`  |
| 1351   | No file  | `59656d185f4a`  |
| 1348   | No file  | `59656d185f4a`  |
| 1346   | No file  | `59656d185f4a`  |
| 1341   | No file  | `59656d185f4a`  |
| 1340   | No file  | `59656d185f4a`  |
| 1338   | No file  | `59656d185f4a`  |
| 1335   | No file  | `59656d185f4a`  |
| 1333   | No file  | `59656d185f4a`  |
| 1329   | No file  | `59656d185f4a`  |
| 1327   | No file  | `59656d185f4a`  |
| 1324   | No file  | `59656d185f4a`  |
| 1321   | No file  | `59656d185f4a`  |
| 1319   | No file  | `59656d185f4a`  |
| 1318   | No file  | `59656d185f4a`  |
| 1316   | No file  | `59656d185f4a`  |
| 1313   | No file  | `59656d185f4a`  |
| 1311   | No file  | `59656d185f4a`  |
| 1309   | No file  | `59656d185f4a`  |
| 1304   | No file  | `59656d185f4a`  |
| 1292   | No file  | `59656d185f4a`  |
| 1286   | No file  | `59656d185f4a`  |
| 1280   | No file  | `59656d185f4a`  |
| 1276   | No file  | `59656d185f4a`  |
| 1267   | No file  | `59656d185f4a`  |
| 1261   | No file  | `59656d185f4a`  |
| 1256   | No file  | `59656d185f4a`  |
| 1250   | No file  | `59656d185f4a`  |
| 1246   | No file  | `59656d185f4a`  |
| 1239   | No file  | `59656d185f4a`  |
| 1230   | No file  | `59656d185f4a`  |
| 1226   | No file  | `59656d185f4a`  |
| 1220   | No file  | `59656d185f4a`  |
| 1217   | No file  | `59656d185f4a`  |
| 1211   | No file  | `59656d185f4a`  |
| 1210   | No file  | `59656d185f4a`  |
| 1208   | No file  | `59656d185f4a`  |
| 1203   | No file  | `59656d185f4a`  |
| 1197   | No file  | `59656d185f4a`  |
| 1194   | No file  | `59656d185f4a`  |
| 1192   | No file  | `59656d185f4a`  |
| 1187   | No file  | `59656d185f4a`  |
| 1183   | No file  | `59656d185f4a`  |
| 1177   | No file  | `59656d185f4a`  |
| 1173   | No file  | `59656d185f4a`  |
| 1167   | No file  | `59656d185f4a`  |
| 1164   | No file  | `59656d185f4a`  |
| 1156   | No file  | `59656d185f4a`  |
| 1149   | No file  | `59656d185f4a`  |
| 1144   | No file  | `59656d185f4a`  |
| 1137   | No file  | `59656d185f4a`  |
| 1132   | No file  | `59656d185f4a`  |
| 1127   | No file  | `59656d185f4a`  |
| 1122   | No file  | `59656d185f4a`  |
| 1118   | No file  | `59656d185f4a`  |
| 1114   | No file  | `59656d185f4a`  |
| 1109   | No file  | `59656d185f4a`  |
| 1102   | No file  | `59656d185f4a`  |
| 1096   | No file  | `59656d185f4a`  |
| 1088   | No file  | `59656d185f4a`  |
| 1081   | No file  | `59656d185f4a`  |
| 1076   | No file  | `59656d185f4a`  |
| 1069   | No file  | `59656d185f4a`  |
| 1064   | No file  | `59656d185f4a`  |
| 1058   | No file  | `59656d185f4a`  |
| 1051   | No file  | `59656d185f4a`  |
| 1044   | No file  | `59656d185f4a`  |
| 1036   | No file  | `59656d185f4a`  |
| 1026   | No file  | `59656d185f4a`  |
| 1016   | No file  | `59656d185f4a`  |
| 1009   | No file  | `59656d185f4a`  |
| 1005   | No file  | `59656d185f4a`  |
| 1000   | No file  | `59656d185f4a`  |
| 998    | No file  | `59656d185f4a`  |
| 990    | No file  | `59656d185f4a`  |
| 979    | No file  | `59656d185f4a`  |
| 972    | No file  | `59656d185f4a`  |
| 963    | No file  | `59656d185f4a`  |
| 955    | No file  | `59656d185f4a`  |
| 946    | No file  | `59656d185f4a`  |
| 938    | No file  | `59656d185f4a`  |
| 927    | No file  | `59656d185f4a`  |
| 911    | No file  | `59656d185f4a`  |
| 904    | No file  | `59656d185f4a`  |
| 899    | No file  | `59656d185f4a`  |
| 894    | No file  | `59656d185f4a`  |
| 885    | No file  | `59656d185f4a`  |
| 879    | No file  | `59656d185f4a`  |
| 872    | No file  | `59656d185f4a`  |
| 864    | No file  | `59656d185f4a`  |
| 855    | No file  | `59656d185f4a`  |
| 853    | No file  | `59656d185f4a`  |
| 845    | No file  | `59656d185f4a`  |
| 837    | No file  | `59656d185f4a`  |
| 829    | No file  | `59656d185f4a`  |
| 822    | No file  | `59656d185f4a`  |
| 814    | No file  | `59656d185f4a`  |
| 805    | No file  | `59656d185f4a`  |
| 794    | No file  | `59656d185f4a`  |
| 787    | No file  | `59656d185f4a`  |
| 780    | No file  | `59656d185f4a`  |
| 771    | No file  | `59656d185f4a`  |
| 760    | No file  | `59656d185f4a`  |
| 748    | No file  | `59656d185f4a`  |
| 741    | No file  | `59656d185f4a`  |
| 736    | No file  | `59656d185f4a`  |
| 731    | No file  | `59656d185f4a`  |
| 723    | No file  | `59656d185f4a`  |
| 711    | No file  | `59656d185f4a`  |
| 707    | No file  | `59656d185f4a`  |
| 697    | No file  | `59656d185f4a`  |
| 689    | No file  | `59656d185f4a`  |
| 683    | No file  | `59656d185f4a`  |
| 678    | No file  | `59656d185f4a`  |
| 670    | No file  | `59656d185f4a`  |
| 661    | No file  | `59656d185f4a`  |
| 656    | No file  | `59656d185f4a`  |
| 652    | No file  | `59656d185f4a`  |
| 643    | No file  | `59656d185f4a`  |
| 637    | No file  | `59656d185f4a`  |
| 630    | No file  | `59656d185f4a`  |
| 627    | No file  | `59656d185f4a`  |
| 621    | No file  | `59656d185f4a`  |
| 617    | No file  | `59656d185f4a`  |
| 615    | No file  | `59656d185f4a`  |
| 606    | No file  | `59656d185f4a`  |
| 599    | No file  | `59656d185f4a`  |
| 592    | No file  | `59656d185f4a`  |
| 586    | No file  | `59656d185f4a`  |
| 577    | No file  | `59656d185f4a`  |
| 569    | No file  | `59656d185f4a`  |
| 561    | No file  | `59656d185f4a`  |
| 554    | No file  | `59656d185f4a`  |
| 542    | No file  | `59656d185f4a`  |
| 532    | No file  | `59656d185f4a`  |
| 531    | No file  | `59656d185f4a`  |
| 526    | No file  | `59656d185f4a`  |
| 521    | No file  | `59656d185f4a`  |
| 517    | No file  | `59656d185f4a`  |
| 510    | No file  | `59656d185f4a`  |
| 508    | No file  | `59656d185f4a`  |
| 504    | No file  | `59656d185f4a`  |
| 497    | No file  | `59656d185f4a`  |
| 491    | No file  | `59656d185f4a`  |
| 485    | No file  | `59656d185f4a`  |
| 478    | No file  | `59656d185f4a`  |
| 472    | No file  | `59656d185f4a`  |
| 466    | No file  | `59656d185f4a`  |
| 457    | No file  | `59656d185f4a`  |
| 452    | No file  | `59656d185f4a`  |
| 449    | No file  | `59656d185f4a`  |
| 435    | No file  | `59656d185f4a`  |

<!-- versions:end -->

## Companion Files

None. The handler names each challenge with LOC type 48 from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows, one per grouped challenge     |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 10 bytes + challenge keys)

| Offset  | Type                   | Field              | Notes                                                            |
| ------- | ---------------------- | ------------------ | ---------------------------------------------------------------- |
| `+0x00` | u16                    | main_challenge_key | The group's challenge with the highest Pearl goal; one of `challenge_keys` |
| `+0x02` | u32                    | unknown_02         | `2` on the event groups, `1` on the other two; see Open Questions |
| `+0x06` | u32                    | challenge_count    | Number of `challenge_keys`                                       |
| `+0x0A` | u16[challenge_count]   | challenge_keys     | The group's challenges in key order (LOC type 48)                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Groups

The groups of client 3483 with their LOC type 48 names and event periods.

| `main_challenge_key` | `challenge_keys` | `unknown_02` | Rows | Challenges                                              |
| -------------------- | ---------------- | ------------ | ---- | ------------------------------------------------------- |
| 2984                 | 2981 to 2984     | 2            | 4    | [Event] Use 5,000 to 20,000 Pearls, Aug 2 to 8, 2021    |
| 2988                 | 2985 to 2988     | 2            | 4    | The same, Aug 9 to 15, 2021                             |
| 2992                 | 2989 to 2992     | 2            | 4    | The same, Aug 16 to 22, 2021                            |
| 2996                 | 2993 to 2996     | 2            | 4    | The same, Aug 23 to 29, 2021                            |
| 3000                 | 2997 to 3000     | 2            | 4    | The same, Aug 30 to Sep 5, 2021                         |
| 4200                 | 4200 to 4206     | 1            | 7    | Spend 44,000 Pearls (`4200`) down to Spend 800 Pearls (`4206`) |
| 4177                 | 4177 to 4182     | 1            | 6    | Spend 44,000 Pearls (`4177`) down to Spend 800 Pearls (`4182`) |

Client 1784 has the five event groups only (20 rows).

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
the groups; its `Challenge_Table` sheet has the event challenges `2981` to
`3000` (Type `9`, CompleteConditionType `10`, ConditionParam1 `5000` to
`20000` Pearls) and confirms `challenge_keys` as challenge keys. The Lua of
client 3482 maps a challenge to its group with
`ToClient_getPearlUsedChallengeMainNo(challengeKey)` and counts the group's
resets with `ToClient_currentPearlUsedChallengeResetCount` and
`ToClient_maxPearlUsedChallengeResetCount` on the key it returns; the
first field of each row is a challenge of the group, so it takes the name
`main_challenge_key`.

## Notes

- The rows of one group are identical and carry no key of their own. The
  row count equals the sum of the groups' challenge counts (33, that is 5
  x 4 plus 7 plus 6, on client 3483), so the file holds one row per
  challenge in a group.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/enchantshop_tables.py`:
  the main challenge and the challenge list, each key with its LOC type 48
  name.

## Open Questions

### What `unknown_02` Counts

`unknown_02` is `2` on the five event groups and `1` on the groups `4200`
and `4177`. The Lua reads one more number per group,
`ToClient_maxPearlUsedChallengeResetCount(mainNo)`, the cap on the reset
button; it is a lead the data cannot confirm without a reset count shown
in game. The `ResetType` (`4`) and `ResetValue` (`0`) of the event
challenges in the client 1784 `Challenge_Table` do not match it.
