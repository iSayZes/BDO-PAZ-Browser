# `petfeedcount.bss` Format

## Purpose

The number of pet feed items: items whose use is `ContentsType_PetFeed`
(`CppEnums.ContentsEventType` `13`). The value sits in the slot where a
PABR table keeps its record count. On client 3474 it is `10`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File               | Bytes | Records        | Row bytes |
| ------ | ------------- | ------------------ | ----- | -------------- | --------- |
| 1      | 805 and later | `petfeedcount.bss` | 20    | 1 String Table | 4         |

| Layout | File               | Known         | Unknown    |
| ------ | ------------------ | ------------- | ---------- |
| 1      | `petfeedcount.bss` | 20 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `b4c66cc6089b`  |
| 3482   | Layout 1             | `b4c66cc6089b`  |
| 3474   | Layout 1             | `b4c66cc6089b`  |
| 3473   | Layout 1             | `b4c66cc6089b`  |
| 3464   | Layout 1             | `b4c66cc6089b`  |
| 3458   | Layout 1             | `b4c66cc6089b`  |
| 3454   | Layout 1             | `b4c66cc6089b`  |
| 3444   | Layout 1             | `b4c66cc6089b`  |
| 3435   | Layout 1             | `b4c66cc6089b`  |
| 3426   | Layout 1             | `b4c66cc6089b`  |
| 3418   | Layout 1             | `b4c66cc6089b`  |
| 3412   | Layout 1             | `b4c66cc6089b`  |
| 3402   | Layout 1             | `b4c66cc6089b`  |
| 3396   | Layout 1             | `b4c66cc6089b`  |
| 3387   | Layout 1             | `b4c66cc6089b`  |
| 3381   | Layout 1             | `b4c66cc6089b`  |
| 3373   | Layout 1             | `b4c66cc6089b`  |
| 3364   | Layout 1             | `b4c66cc6089b`  |
| 3356   | Layout 1             | `b4c66cc6089b`  |
| 3349   | Layout 1             | `b4c66cc6089b`  |
| 3342   | Layout 1             | `b4c66cc6089b`  |
| 3335   | Layout 1             | `b4c66cc6089b`  |
| 3326   | Layout 1             | `b4c66cc6089b`  |
| 3321   | Layout 1             | `b4c66cc6089b`  |
| 3314   | Layout 1             | `b4c66cc6089b`  |
| 3303   | Layout 1             | `b4c66cc6089b`  |
| 3302   | Layout 1             | `b4c66cc6089b`  |
| 3293   | Layout 1             | `b4c66cc6089b`  |
| 3283   | Layout 1             | `b4c66cc6089b`  |
| 3275   | Layout 1             | `b4c66cc6089b`  |
| 3267   | Layout 1             | `b4c66cc6089b`  |
| 3258   | Layout 1             | `b4c66cc6089b`  |
| 3251   | Layout 1             | `b4c66cc6089b`  |
| 3242   | Layout 1             | `b4c66cc6089b`  |
| 3235   | Layout 1             | `b4c66cc6089b`  |
| 3229   | Layout 1             | `b4c66cc6089b`  |
| 3212   | Layout 1             | `b4c66cc6089b`  |
| 3203   | Layout 1             | `b4c66cc6089b`  |
| 3193   | Layout 1             | `b4c66cc6089b`  |
| 3186   | Layout 1             | `b4c66cc6089b`  |
| 3177   | Layout 1             | `b4c66cc6089b`  |
| 3169   | Layout 1             | `b4c66cc6089b`  |
| 3158   | Layout 1             | `b4c66cc6089b`  |
| 3151   | Layout 1             | `b4c66cc6089b`  |
| 3144   | Layout 1             | `b4c66cc6089b`  |
| 3133   | Layout 1             | `b4c66cc6089b`  |
| 3125   | Layout 1             | `b4c66cc6089b`  |
| 3118   | Layout 1             | `b4c66cc6089b`  |
| 3111   | Layout 1             | `b4c66cc6089b`  |
| 3103   | Layout 1             | `b4c66cc6089b`  |
| 3095   | Layout 1             | `b4c66cc6089b`  |
| 3086   | Layout 1             | `b4c66cc6089b`  |
| 3072   | Layout 1             | `b4c66cc6089b`  |
| 3062   | Layout 1             | `b4c66cc6089b`  |
| 3052   | Layout 1             | `b4c66cc6089b`  |
| 3045   | Layout 1             | `b4c66cc6089b`  |
| 3037   | Layout 1             | `b4c66cc6089b`  |
| 3030   | Layout 1             | `b4c66cc6089b`  |
| 3021   | Layout 1             | `b4c66cc6089b`  |
| 3012   | Layout 1             | `b4c66cc6089b`  |
| 3002   | Layout 1             | `b4c66cc6089b`  |
| 2995   | Layout 1             | `b4c66cc6089b`  |
| 2987   | Layout 1             | `b4c66cc6089b`  |
| 2978   | Layout 1             | `b4c66cc6089b`  |
| 2970   | Layout 1             | `b4c66cc6089b`  |
| 2959   | Layout 1             | `b4c66cc6089b`  |
| 2951   | Layout 1             | `b4c66cc6089b`  |
| 2942   | Layout 1             | `b4c66cc6089b`  |
| 2935   | Layout 1             | `b4c66cc6089b`  |
| 2932   | Layout 1             | `b4c66cc6089b`  |
| 2923   | Layout 1             | `b4c66cc6089b`  |
| 2919   | Layout 1             | `b4c66cc6089b`  |
| 2907   | Layout 1             | `b4c66cc6089b`  |
| 2900   | Layout 1             | `b4c66cc6089b`  |
| 2891   | Layout 1             | `b4c66cc6089b`  |
| 2882   | Layout 1             | `b4c66cc6089b`  |
| 2872   | Layout 1             | `b4c66cc6089b`  |
| 2863   | Layout 1             | `b4c66cc6089b`  |
| 2855   | Layout 1             | `b4c66cc6089b`  |
| 2849   | Layout 1             | `b4c66cc6089b`  |
| 2844   | Layout 1             | `b4c66cc6089b`  |
| 2834   | Layout 1             | `b4c66cc6089b`  |
| 2825   | Layout 1             | `b4c66cc6089b`  |
| 2819   | Layout 1             | `b4c66cc6089b`  |
| 2811   | Layout 1             | `b4c66cc6089b`  |
| 2803   | Layout 1             | `b4c66cc6089b`  |
| 2794   | Layout 1             | `b4c66cc6089b`  |
| 2783   | Layout 1             | `b4c66cc6089b`  |
| 2774   | Layout 1             | `b4c66cc6089b`  |
| 2765   | Layout 1             | `b4c66cc6089b`  |
| 2756   | Layout 1             | `b4c66cc6089b`  |
| 2750   | Layout 1             | `b4c66cc6089b`  |
| 2743   | Layout 1             | `b4c66cc6089b`  |
| 2736   | Layout 1             | `b4c66cc6089b`  |
| 2726   | Layout 1             | `b4c66cc6089b`  |
| 2717   | Layout 1             | `b4c66cc6089b`  |
| 2709   | Layout 1             | `b4c66cc6089b`  |
| 2703   | Layout 1             | `b4c66cc6089b`  |
| 2695   | Layout 1             | `b4c66cc6089b`  |
| 2684   | Layout 1             | `b4c66cc6089b`  |
| 2672   | Layout 1             | `b4c66cc6089b`  |
| 2665   | Layout 1             | `b4c66cc6089b`  |
| 2657   | Layout 1             | `b4c66cc6089b`  |
| 2649   | Layout 1             | `b4c66cc6089b`  |
| 2644   | Layout 1             | `b4c66cc6089b`  |
| 2637   | Layout 1             | `b4c66cc6089b`  |
| 2629   | Layout 1             | `b4c66cc6089b`  |
| 2619   | Layout 1             | `b4c66cc6089b`  |
| 2612   | Layout 1             | `b4c66cc6089b`  |
| 2606   | Layout 1             | `b4c66cc6089b`  |
| 2602   | Layout 1             | `b4c66cc6089b`  |
| 2601   | Layout 1             | `b4c66cc6089b`  |
| 2592   | Layout 1             | `b4c66cc6089b`  |
| 2583   | Layout 1             | `b4c66cc6089b`  |
| 2575   | Layout 1             | `b4c66cc6089b`  |
| 2567   | Layout 1             | `b4c66cc6089b`  |
| 2560   | Layout 1             | `b4c66cc6089b`  |
| 2553   | Layout 1             | `b4c66cc6089b`  |
| 2545   | Layout 1             | `b4c66cc6089b`  |
| 2538   | Layout 1             | `b4c66cc6089b`  |
| 2529   | Layout 1             | `b4c66cc6089b`  |
| 2519   | Layout 1             | `b4c66cc6089b`  |
| 2513   | Layout 1             | `b4c66cc6089b`  |
| 2510   | Layout 1             | `b4c66cc6089b`  |
| 2507   | Layout 1             | `b4c66cc6089b`  |
| 2503   | Layout 1             | `b4c66cc6089b`  |
| 2498   | Layout 1             | `b4c66cc6089b`  |
| 2492   | Layout 1             | `b4c66cc6089b`  |
| 2487   | Layout 1             | `b4c66cc6089b`  |
| 2480   | Layout 1             | `b4c66cc6089b`  |
| 2474   | Layout 1             | `b4c66cc6089b`  |
| 2468   | Layout 1             | `b4c66cc6089b`  |
| 2460   | Layout 1             | `b4c66cc6089b`  |
| 2453   | Layout 1             | `b4c66cc6089b`  |
| 2444   | Layout 1             | `b4c66cc6089b`  |
| 2438   | Layout 1             | `b4c66cc6089b`  |
| 2434   | Layout 1             | `b4c66cc6089b`  |
| 2429   | Layout 1             | `b4c66cc6089b`  |
| 2421   | Layout 1             | `b4c66cc6089b`  |
| 2414   | Layout 1             | `b4c66cc6089b`  |
| 2407   | Layout 1             | `b4c66cc6089b`  |
| 2401   | Layout 1             | `b4c66cc6089b`  |
| 2397   | Layout 1             | `b4c66cc6089b`  |
| 2393   | Layout 1             | `b4c66cc6089b`  |
| 2384   | Layout 1             | `b4c66cc6089b`  |
| 2378   | Layout 1             | `b4c66cc6089b`  |
| 2372   | Layout 1             | `b4c66cc6089b`  |
| 2358   | Layout 1             | `b4c66cc6089b`  |
| 2352   | Layout 1             | `b4c66cc6089b`  |
| 2347   | Layout 1             | `b4c66cc6089b`  |
| 2343   | Layout 1             | `b4c66cc6089b`  |
| 2335   | Layout 1             | `b4c66cc6089b`  |
| 2327   | Layout 1             | `b4c66cc6089b`  |
| 2324   | Layout 1             | `b4c66cc6089b`  |
| 2319   | Layout 1             | `b4c66cc6089b`  |
| 2313   | Layout 1             | `b4c66cc6089b`  |
| 2308   | Layout 1             | `b4c66cc6089b`  |
| 2302   | Layout 1             | `b4c66cc6089b`  |
| 2295   | Layout 1             | `b4c66cc6089b`  |
| 2290   | Layout 1             | `b4c66cc6089b`  |
| 2284   | Layout 1             | `b4c66cc6089b`  |
| 2276   | Layout 1             | `b4c66cc6089b`  |
| 2269   | Layout 1             | `b4c66cc6089b`  |
| 2259   | Layout 1             | `b4c66cc6089b`  |
| 2250   | Layout 1             | `b4c66cc6089b`  |
| 2243   | Layout 1             | `b4c66cc6089b`  |
| 2235   | Layout 1             | `b4c66cc6089b`  |
| 2229   | Layout 1             | `b4c66cc6089b`  |
| 2224   | Layout 1             | `b4c66cc6089b`  |
| 2218   | Layout 1             | `b4c66cc6089b`  |
| 2215   | Layout 1             | `b4c66cc6089b`  |
| 2207   | Layout 1             | `b4c66cc6089b`  |
| 2203   | Layout 1             | `b4c66cc6089b`  |
| 2196   | Layout 1             | `b4c66cc6089b`  |
| 2192   | Layout 1             | `b4c66cc6089b`  |
| 2189   | Layout 1             | `b4c66cc6089b`  |
| 2183   | Layout 1             | `b4c66cc6089b`  |
| 2179   | Layout 1             | `b4c66cc6089b`  |
| 2171   | Layout 1             | `b4c66cc6089b`  |
| 2163   | Layout 1             | `b4c66cc6089b`  |
| 2156   | Layout 1             | `b4c66cc6089b`  |
| 2151   | Layout 1             | `b4c66cc6089b`  |
| 2147   | Layout 1             | `b4c66cc6089b`  |
| 2142   | Layout 1             | `b4c66cc6089b`  |
| 2138   | Layout 1             | `b4c66cc6089b`  |
| 2134   | Layout 1             | `b4c66cc6089b`  |
| 2130   | Layout 1             | `b4c66cc6089b`  |
| 2122   | Layout 1             | `b4c66cc6089b`  |
| 2107   | Layout 1             | `b4c66cc6089b`  |
| 2098   | Layout 1             | `b4c66cc6089b`  |
| 2089   | Layout 1             | `b4c66cc6089b`  |
| 2081   | Layout 1             | `b4c66cc6089b`  |
| 2073   | Layout 1             | `b4c66cc6089b`  |
| 2067   | Layout 1             | `b4c66cc6089b`  |
| 2063   | Layout 1             | `b4c66cc6089b`  |
| 2059   | Layout 1             | `b4c66cc6089b`  |
| 2052   | Layout 1             | `b4c66cc6089b`  |
| 2044   | Layout 1             | `b4c66cc6089b`  |
| 2039   | Layout 1             | `b4c66cc6089b`  |
| 2032   | Layout 1             | `b4c66cc6089b`  |
| 2025   | Layout 1             | `b4c66cc6089b`  |
| 2011   | Layout 1             | `b4c66cc6089b`  |
| 2005   | Layout 1             | `b4c66cc6089b`  |
| 2000   | Layout 1             | `b4c66cc6089b`  |
| 1996   | Layout 1             | `b4c66cc6089b`  |
| 1991   | Layout 1             | `b4c66cc6089b`  |
| 1985   | Layout 1             | `b4c66cc6089b`  |
| 1980   | Layout 1             | `b4c66cc6089b`  |
| 1969   | Layout 1             | `b4c66cc6089b`  |
| 1964   | Layout 1             | `b4c66cc6089b`  |
| 1958   | Layout 1             | `b4c66cc6089b`  |
| 1950   | Layout 1             | `b4c66cc6089b`  |
| 1945   | Layout 1             | `b4c66cc6089b`  |
| 1937   | Layout 1             | `b4c66cc6089b`  |
| 1933   | Layout 1             | `b4c66cc6089b`  |
| 1927   | Layout 1             | `b4c66cc6089b`  |
| 1921   | Layout 1             | `b4c66cc6089b`  |
| 1914   | Layout 1             | `b4c66cc6089b`  |
| 1908   | Layout 1             | `b4c66cc6089b`  |
| 1897   | Layout 1             | `b4c66cc6089b`  |
| 1892   | Layout 1             | `b4c66cc6089b`  |
| 1886   | Layout 1             | `b4c66cc6089b`  |
| 1881   | Layout 1             | `b4c66cc6089b`  |
| 1871   | Layout 1             | `b4c66cc6089b`  |
| 1866   | Layout 1             | `b4c66cc6089b`  |
| 1862   | Layout 1             | `b4c66cc6089b`  |
| 1854   | Layout 1             | `b4c66cc6089b`  |
| 1846   | Layout 1             | `b4c66cc6089b`  |
| 1838   | Layout 1             | `b4c66cc6089b`  |
| 1832   | Layout 1             | `b4c66cc6089b`  |
| 1826   | Layout 1             | `b4c66cc6089b`  |
| 1822   | Layout 1             | `b4c66cc6089b`  |
| 1818   | Layout 1             | `b4c66cc6089b`  |
| 1804   | Layout 1             | `b4c66cc6089b`  |
| 1794   | Layout 1             | `b4c66cc6089b`  |
| 1790   | Layout 1             | `b4c66cc6089b`  |
| 1784   | Layout 1             | `b4c66cc6089b`  |
| 1774   | Layout 1             | `b4c66cc6089b`  |
| 1771   | Layout 1             | `b4c66cc6089b`  |
| 1762   | Layout 1             | `b4c66cc6089b`  |
| 1759   | Layout 1             | `b4c66cc6089b`  |
| 1754   | Layout 1             | `b4c66cc6089b`  |
| 1749   | Layout 1             | `b4c66cc6089b`  |
| 1743   | Layout 1             | `b4c66cc6089b`  |
| 1737   | Layout 1             | `b4c66cc6089b`  |
| 1731   | Layout 1             | `b4c66cc6089b`  |
| 1725   | Layout 1             | `b4c66cc6089b`  |
| 1717   | Layout 1             | `b4c66cc6089b`  |
| 1710   | Layout 1             | `b4c66cc6089b`  |
| 1704   | Layout 1             | `b4c66cc6089b`  |
| 1698   | Layout 1             | `b4c66cc6089b`  |
| 1690   | Layout 1             | `b4c66cc6089b`  |
| 1685   | Layout 1             | `b4c66cc6089b`  |
| 1680   | Layout 1             | `b4c66cc6089b`  |
| 1674   | Layout 1             | `b4c66cc6089b`  |
| 1668   | Layout 1             | `b4c66cc6089b`  |
| 1659   | Layout 1             | `b4c66cc6089b`  |
| 1649   | Layout 1             | `b4c66cc6089b`  |
| 1642   | Layout 1             | `b4c66cc6089b`  |
| 1636   | Layout 1             | `b4c66cc6089b`  |
| 1628   | Layout 1             | `b4c66cc6089b`  |
| 1622   | Layout 1             | `b4c66cc6089b`  |
| 1614   | Layout 1             | `b4c66cc6089b`  |
| 1608   | Layout 1             | `b4c66cc6089b`  |
| 1602   | Layout 1             | `b4c66cc6089b`  |
| 1598   | Layout 1             | `b4c66cc6089b`  |
| 1594   | Layout 1             | `b4c66cc6089b`  |
| 1590   | Layout 1             | `b4c66cc6089b`  |
| 1587   | Layout 1             | `b4c66cc6089b`  |
| 1584   | Layout 1             | `b4c66cc6089b`  |
| 1579   | Layout 1             | `b4c66cc6089b`  |
| 1572   | Layout 1             | `b4c66cc6089b`  |
| 1565   | Layout 1             | `b4c66cc6089b`  |
| 1559   | Layout 1             | `b4c66cc6089b`  |
| 1554   | Layout 1             | `b4c66cc6089b`  |
| 1547   | Layout 1             | `b4c66cc6089b`  |
| 1537   | Layout 1             | `b4c66cc6089b`  |
| 1529   | Layout 1             | `b4c66cc6089b`  |
| 1524   | Layout 1             | `b4c66cc6089b`  |
| 1519   | Layout 1             | `b4c66cc6089b`  |
| 1509   | Layout 1             | `b4c66cc6089b`  |
| 1506   | Layout 1             | `b4c66cc6089b`  |
| 1504   | Layout 1             | `b4c66cc6089b`  |
| 1500   | Layout 1             | `b4c66cc6089b`  |
| 1493   | Layout 1             | `b4c66cc6089b`  |
| 1489   | Layout 1             | `b4c66cc6089b`  |
| 1485   | Layout 1             | `b4c66cc6089b`  |
| 1481   | Layout 1             | `b4c66cc6089b`  |
| 1474   | Layout 1             | `b4c66cc6089b`  |
| 1466   | Layout 1             | `b4c66cc6089b`  |
| 1462   | Layout 1             | `b4c66cc6089b`  |
| 1459   | Layout 1             | `b4c66cc6089b`  |
| 1453   | Layout 1             | `b4c66cc6089b`  |
| 1450   | Layout 1             | `b4c66cc6089b`  |
| 1445   | Layout 1             | `b4c66cc6089b`  |
| 1439   | Layout 1             | `b4c66cc6089b`  |
| 1433   | Layout 1             | `b4c66cc6089b`  |
| 1430   | Layout 1             | `b4c66cc6089b`  |
| 1426   | Layout 1             | `b4c66cc6089b`  |
| 1421   | Layout 1             | `b4c66cc6089b`  |
| 1417   | Layout 1             | `b4c66cc6089b`  |
| 1416   | Layout 1             | `b4c66cc6089b`  |
| 1409   | Layout 1             | `b4c66cc6089b`  |
| 1405   | Layout 1             | `b4c66cc6089b`  |
| 1401   | Layout 1             | `b4c66cc6089b`  |
| 1396   | Layout 1             | `b4c66cc6089b`  |
| 1391   | Layout 1             | `b4c66cc6089b`  |
| 1390   | Layout 1             | `b4c66cc6089b`  |
| 1386   | Layout 1             | `b4c66cc6089b`  |
| 1381   | Layout 1             | `b4c66cc6089b`  |
| 1379   | Layout 1             | `b4c66cc6089b`  |
| 1372   | Layout 1             | `b4c66cc6089b`  |
| 1366   | Layout 1             | `b4c66cc6089b`  |
| 1364   | Layout 1             | `b4c66cc6089b`  |
| 1363   | Layout 1             | `b4c66cc6089b`  |
| 1360   | Layout 1             | `b4c66cc6089b`  |
| 1358   | Layout 1             | `b4c66cc6089b`  |
| 1355   | Layout 1             | `b4c66cc6089b`  |
| 1351   | Layout 1             | `b4c66cc6089b`  |
| 1348   | Layout 1             | `b4c66cc6089b`  |
| 1346   | Layout 1             | `b4c66cc6089b`  |
| 1341   | Layout 1             | `b4c66cc6089b`  |
| 1340   | Layout 1             | `b4c66cc6089b`  |
| 1338   | Layout 1             | `b4c66cc6089b`  |
| 1335   | Layout 1             | `b4c66cc6089b`  |
| 1333   | Layout 1             | `b4c66cc6089b`  |
| 1329   | Layout 1             | `b4c66cc6089b`  |
| 1327   | Layout 1             | `b4c66cc6089b`  |
| 1324   | Layout 1             | `b4c66cc6089b`  |
| 1321   | Layout 1             | `b4c66cc6089b`  |
| 1319   | Layout 1             | `b4c66cc6089b`  |
| 1318   | Layout 1             | `b4c66cc6089b`  |
| 1316   | Layout 1             | `b4c66cc6089b`  |
| 1313   | Layout 1             | `b4c66cc6089b`  |
| 1311   | Layout 1             | `b4c66cc6089b`  |
| 1309   | Layout 1             | `b4c66cc6089b`  |
| 1304   | Layout 1             | `b4c66cc6089b`  |
| 1292   | Layout 1             | `b4c66cc6089b`  |
| 1286   | Layout 1             | `b4c66cc6089b`  |
| 1280   | Layout 1             | `b4c66cc6089b`  |
| 1276   | Layout 1             | `b4c66cc6089b`  |
| 1267   | Layout 1             | `b4c66cc6089b`  |
| 1261   | Layout 1             | `b4c66cc6089b`  |
| 1256   | Layout 1             | `b4c66cc6089b`  |
| 1250   | Layout 1             | `b4c66cc6089b`  |
| 1246   | Layout 1             | `b4c66cc6089b`  |
| 1239   | Layout 1             | `b4c66cc6089b`  |
| 1230   | Layout 1             | `b4c66cc6089b`  |
| 1226   | Layout 1             | `b4c66cc6089b`  |
| 1220   | Layout 1             | `b4c66cc6089b`  |
| 1217   | Layout 1             | `b4c66cc6089b`  |
| 1211   | Layout 1             | `b4c66cc6089b`  |
| 1210   | Layout 1             | `b4c66cc6089b`  |
| 1208   | Layout 1             | `b4c66cc6089b`  |
| 1203   | Layout 1             | `b4c66cc6089b`  |
| 1197   | Layout 1             | `b4c66cc6089b`  |
| 1194   | Layout 1             | `b4c66cc6089b`  |
| 1192   | Layout 1             | `b4c66cc6089b`  |
| 1187   | Layout 1             | `b4c66cc6089b`  |
| 1183   | Layout 1             | `b4c66cc6089b`  |
| 1177   | Layout 1             | `b4c66cc6089b`  |
| 1173   | Layout 1             | `b4c66cc6089b`  |
| 1167   | Layout 1             | `b4c66cc6089b`  |
| 1164   | Layout 1             | `b4c66cc6089b`  |
| 1156   | Layout 1             | `b4c66cc6089b`  |
| 1149   | Layout 1             | `b4c66cc6089b`  |
| 1144   | Layout 1             | `b4c66cc6089b`  |
| 1137   | Layout 1             | `b4c66cc6089b`  |
| 1132   | Layout 1             | `b4c66cc6089b`  |
| 1127   | Layout 1             | `b4c66cc6089b`  |
| 1122   | Layout 1             | `b4c66cc6089b`  |
| 1118   | Layout 1             | `b4c66cc6089b`  |
| 1114   | Layout 1             | `b4c66cc6089b`  |
| 1109   | Layout 1             | `b4c66cc6089b`  |
| 1102   | Layout 1             | `b4c66cc6089b`  |
| 1096   | Layout 1             | `b4c66cc6089b`  |
| 1088   | Layout 1             | `b4c66cc6089b`  |
| 1081   | Layout 1             | `b4c66cc6089b`  |
| 1076   | Layout 1             | `b4c66cc6089b`  |
| 1069   | Layout 1             | `b4c66cc6089b`  |
| 1064   | Layout 1             | `b4c66cc6089b`  |
| 1058   | Layout 1             | `b4c66cc6089b`  |
| 1051   | Layout 1             | `b4c66cc6089b`  |
| 1044   | Layout 1             | `b4c66cc6089b`  |
| 1036   | Layout 1             | `b4c66cc6089b`  |
| 1026   | Layout 1             | `b4c66cc6089b`  |
| 1016   | Layout 1             | `b4c66cc6089b`  |
| 1009   | Layout 1             | `b4c66cc6089b`  |
| 1005   | Layout 1             | `b4c66cc6089b`  |
| 1000   | Layout 1             | `b4c66cc6089b`  |
| 998    | Layout 1             | `b4c66cc6089b`  |
| 990    | Layout 1             | `b4c66cc6089b`  |
| 979    | Layout 1             | `b4c66cc6089b`  |
| 972    | Layout 1             | `b4c66cc6089b`  |
| 963    | Layout 1             | `b4c66cc6089b`  |
| 955    | Layout 1             | `b4c66cc6089b`  |
| 946    | Layout 1             | `b4c66cc6089b`  |
| 938    | Layout 1             | `b4c66cc6089b`  |
| 927    | Layout 1             | `b4c66cc6089b`  |
| 911    | Layout 1             | `b4c66cc6089b`  |
| 904    | Layout 1             | `b4c66cc6089b`  |
| 899    | Layout 1             | `b4c66cc6089b`  |
| 894    | Layout 1             | `b4c66cc6089b`  |
| 885    | Layout 1             | `b4c66cc6089b`  |
| 879    | Layout 1             | `b4c66cc6089b`  |
| 872    | Layout 1             | `b4c66cc6089b`  |
| 864    | Layout 1             | `b4c66cc6089b`  |
| 855    | Layout 1             | `b4c66cc6089b`  |
| 853    | Layout 1             | `b4c66cc6089b`  |
| 845    | Layout 1             | `b4c66cc6089b`  |
| 837    | Layout 1             | `b4c66cc6089b`  |
| 829    | Layout 1             | `b4c66cc6089b`  |
| 822    | Layout 1             | `b4c66cc6089b`  |
| 814    | Layout 1             | `b4c66cc6089b`  |
| 805    | Layout 1             | `b4c66cc6089b`  |
| 794    | No documented layout | `b4c66cc6089b`  |
| 787    | No documented layout | `b4c66cc6089b`  |
| 780    | No documented layout | `b4c66cc6089b`  |
| 771    | No documented layout | `b4c66cc6089b`  |
| 760    | No documented layout | `b4c66cc6089b`  |
| 748    | No file              | `b4c66cc6089b`  |
| 741    | No file              | `b4c66cc6089b`  |
| 736    | No file              | `b4c66cc6089b`  |
| 731    | No file              | `b4c66cc6089b`  |
| 723    | No file              | `b4c66cc6089b`  |
| 711    | No file              | `b4c66cc6089b`  |
| 707    | No file              | `b4c66cc6089b`  |
| 697    | No file              | `b4c66cc6089b`  |
| 689    | No file              | `b4c66cc6089b`  |
| 683    | No file              | `b4c66cc6089b`  |
| 678    | No file              | `b4c66cc6089b`  |
| 670    | No file              | `b4c66cc6089b`  |
| 661    | No file              | `b4c66cc6089b`  |
| 656    | No file              | `b4c66cc6089b`  |
| 652    | No file              | `b4c66cc6089b`  |
| 643    | No file              | `b4c66cc6089b`  |
| 637    | No file              | `b4c66cc6089b`  |
| 630    | No file              | `b4c66cc6089b`  |
| 627    | No file              | `b4c66cc6089b`  |
| 621    | No file              | `b4c66cc6089b`  |
| 617    | No file              | `b4c66cc6089b`  |
| 615    | No file              | `b4c66cc6089b`  |
| 606    | No file              | `b4c66cc6089b`  |
| 599    | No file              | `b4c66cc6089b`  |
| 592    | No file              | `b4c66cc6089b`  |
| 586    | No file              | `b4c66cc6089b`  |
| 577    | No file              | `b4c66cc6089b`  |
| 569    | No file              | `b4c66cc6089b`  |
| 561    | No file              | `b4c66cc6089b`  |
| 554    | No file              | `b4c66cc6089b`  |
| 542    | No file              | `b4c66cc6089b`  |
| 532    | No file              | `b4c66cc6089b`  |
| 531    | No file              | `b4c66cc6089b`  |
| 526    | No file              | `b4c66cc6089b`  |
| 521    | No file              | `b4c66cc6089b`  |
| 517    | No file              | `b4c66cc6089b`  |
| 510    | No file              | `b4c66cc6089b`  |
| 508    | No file              | `b4c66cc6089b`  |
| 504    | No file              | `b4c66cc6089b`  |
| 497    | No file              | `b4c66cc6089b`  |
| 491    | No file              | `b4c66cc6089b`  |
| 485    | No file              | `b4c66cc6089b`  |
| 478    | No file              | `b4c66cc6089b`  |
| 472    | No file              | `b4c66cc6089b`  |
| 466    | No file              | `b4c66cc6089b`  |
| 457    | No file              | `b4c66cc6089b`  |
| 452    | No file              | `b4c66cc6089b`  |
| 449    | No file              | `b4c66cc6089b`  |
| 435    | No file              | `b4c66cc6089b`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field           | Notes                                                      |
| ------------------- | ------------ | --------------- | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic           | ASCII `PABR`                                               |
| `+0x04`             | u32          | feed_item_count | Number of pet feed items; see Field Names                  |
| `+0x08`             | String Table | string_table    | See String Table                                           |
| `string_table+0x00` | u32          | table_start     | Offset of the string table; `0x08` on every client checked |
| `string_table+0x04` | u32          | zero            | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

`feed_item_count` equals the number of items with contents event type `13`
on both clients where the items could be counted:

| Client | `feed_item_count` | Items with event type `13` | Source of the item count                          |
| ------ | ----------------- | -------------------------- | ------------------------------------------------- |
| 1784   | `11`              | 11                         | `ContentsEventType` of the `Item_Table` sheet     |
| 3474   | `10`              | 10                         | `contents_event_type` of `itemenchant.dbss` base blocks |

The `Item_Table` sheet is the one in a private server's `DataSheets.bexcel`
on client 1784, whose compiled `binary/petfeedcount.bss` holds `11` as the
client 1784 archive does. On client 3474 the ten items are `17728`, `18041`,
`18408`, `18409`, `18963`, `54016`, `54017`, `54018`, `757431` and `830088`
(`contents_event_type` at `unknown_61+0x25` of
[`itemenchant.dbss`](../dbss/itemenchant_dbss.md)). The enum value comes from
`global_define_cpp_enum.luac`: `ContentsType_PetFeed = 13`.

Clients 2107 to 3251 hold `11`, `12`, `12` and `10` (clients 2107, 2519,
3002, 3251); their item tables were not counted.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 0A 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00`.
- The server dump of the private server on client 1784 reads `petFeedCount`
  in `ItemEnchantStaticStatusManager::readFromBinary()`, next to
  `itemMaxLevel` and `itemEnchantOffset`, and logs "Can't Find petFeedCount"
  when the file is missing. The value so belongs to the item tables.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`.

## Open Questions

### Feed Bar Size

The pet window (`panel_window_petlist_all.luac`, client 3474) creates
`ToClient_Pet_GetFeedStaticItemCount() * 2` feed slots and fills them from
`ToClient_Pet_GetFeedItemCount()`, the feed items the player holds. Whether
`ToClient_Pet_GetFeedStaticItemCount()` returns `feed_item_count` or counts
the items itself is not visible in the Lua.
