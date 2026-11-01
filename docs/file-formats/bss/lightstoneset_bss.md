# `lightstoneset.bss` Format

## Purpose

The Lightstone sets: each row names three or four Lightstones that, slotted
into Artifacts together, apply a set effect. A row holds the set ID, the
passive skill that carries the effect, the member Lightstone item IDs and the
Korean name and effect text. A table after the rows lists which Lightstone
items count as which member, so an Amplified Lightstone completes a set like
its base Lightstone.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes  | Records                         | Row bytes               |
| ------ | -------------- | ------------------- | ------ | ------------------------------- | ----------------------- |
| 1      | 2970 and later | `lightstoneset.bss` | 30,209 | 165 Set Row, 105 Substitute Row | 26 to 30, 29 on average |

| Layout | File                | Known             | Unknown    |
| ------ | ------------------- | ----------------- | ---------- |
| 1      | `lightstoneset.bss` | 30,209 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `1a27c73b0938`  |
| 3482   | Layout 1             | `1a27c73b0938`  |
| 3474   | Layout 1             | `1a27c73b0938`  |
| 3473   | Layout 1             | `1a27c73b0938`  |
| 3464   | Layout 1             | `1a27c73b0938`  |
| 3458   | Layout 1             | `1a27c73b0938`  |
| 3454   | Layout 1             | `1a27c73b0938`  |
| 3444   | Layout 1             | `1a27c73b0938`  |
| 3435   | Layout 1             | `1a27c73b0938`  |
| 3426   | Layout 1             | `1a27c73b0938`  |
| 3418   | Layout 1             | `1a27c73b0938`  |
| 3412   | Layout 1             | `1a27c73b0938`  |
| 3402   | Layout 1             | `1a27c73b0938`  |
| 3396   | Layout 1             | `1a27c73b0938`  |
| 3387   | Layout 1             | `1a27c73b0938`  |
| 3381   | Layout 1             | `1a27c73b0938`  |
| 3373   | Layout 1             | `1a27c73b0938`  |
| 3364   | Layout 1             | `1a27c73b0938`  |
| 3356   | Layout 1             | `1a27c73b0938`  |
| 3349   | Layout 1             | `1a27c73b0938`  |
| 3342   | Layout 1             | `1a27c73b0938`  |
| 3335   | Layout 1             | `1a27c73b0938`  |
| 3326   | Layout 1             | `1a27c73b0938`  |
| 3321   | Layout 1             | `1a27c73b0938`  |
| 3314   | Layout 1             | `1a27c73b0938`  |
| 3303   | Layout 1             | `1a27c73b0938`  |
| 3302   | Layout 1             | `1a27c73b0938`  |
| 3293   | Layout 1             | `1a27c73b0938`  |
| 3283   | Layout 1             | `1a27c73b0938`  |
| 3275   | Layout 1             | `1a27c73b0938`  |
| 3267   | Layout 1             | `1a27c73b0938`  |
| 3258   | Layout 1             | `1a27c73b0938`  |
| 3251   | Layout 1             | `1a27c73b0938`  |
| 3242   | Layout 1             | `1a27c73b0938`  |
| 3235   | Layout 1             | `1a27c73b0938`  |
| 3229   | Layout 1             | `1a27c73b0938`  |
| 3212   | Layout 1             | `1a27c73b0938`  |
| 3203   | Layout 1             | `1a27c73b0938`  |
| 3193   | Layout 1             | `1a27c73b0938`  |
| 3186   | Layout 1             | `1a27c73b0938`  |
| 3177   | Layout 1             | `1a27c73b0938`  |
| 3169   | Layout 1             | `1a27c73b0938`  |
| 3158   | Layout 1             | `1a27c73b0938`  |
| 3151   | Layout 1             | `1a27c73b0938`  |
| 3144   | Layout 1             | `1a27c73b0938`  |
| 3133   | Layout 1             | `1a27c73b0938`  |
| 3125   | Layout 1             | `1a27c73b0938`  |
| 3118   | Layout 1             | `1a27c73b0938`  |
| 3111   | Layout 1             | `1a27c73b0938`  |
| 3103   | Layout 1             | `1a27c73b0938`  |
| 3095   | Layout 1             | `1a27c73b0938`  |
| 3086   | Layout 1             | `1a27c73b0938`  |
| 3072   | Layout 1             | `1a27c73b0938`  |
| 3062   | Layout 1             | `1a27c73b0938`  |
| 3052   | Layout 1             | `1a27c73b0938`  |
| 3045   | Layout 1             | `1a27c73b0938`  |
| 3037   | Layout 1             | `1a27c73b0938`  |
| 3030   | Layout 1             | `1a27c73b0938`  |
| 3021   | Layout 1             | `1a27c73b0938`  |
| 3012   | Layout 1             | `1a27c73b0938`  |
| 3002   | Layout 1             | `1a27c73b0938`  |
| 2995   | Layout 1             | `1a27c73b0938`  |
| 2987   | Layout 1             | `1a27c73b0938`  |
| 2978   | Layout 1             | `1a27c73b0938`  |
| 2970   | Layout 1             | `1a27c73b0938`  |
| 2959   | No documented layout | `1a27c73b0938`  |
| 2951   | No documented layout | `1a27c73b0938`  |
| 2942   | No documented layout | `1a27c73b0938`  |
| 2935   | No documented layout | `1a27c73b0938`  |
| 2932   | No documented layout | `1a27c73b0938`  |
| 2923   | No documented layout | `1a27c73b0938`  |
| 2919   | No documented layout | `1a27c73b0938`  |
| 2907   | No documented layout | `1a27c73b0938`  |
| 2900   | No documented layout | `1a27c73b0938`  |
| 2891   | No documented layout | `1a27c73b0938`  |
| 2882   | No documented layout | `1a27c73b0938`  |
| 2872   | No documented layout | `1a27c73b0938`  |
| 2863   | No documented layout | `1a27c73b0938`  |
| 2855   | No documented layout | `1a27c73b0938`  |
| 2849   | No documented layout | `1a27c73b0938`  |
| 2844   | No documented layout | `1a27c73b0938`  |
| 2834   | No documented layout | `1a27c73b0938`  |
| 2825   | No documented layout | `1a27c73b0938`  |
| 2819   | No documented layout | `1a27c73b0938`  |
| 2811   | No documented layout | `1a27c73b0938`  |
| 2803   | No documented layout | `1a27c73b0938`  |
| 2794   | No documented layout | `1a27c73b0938`  |
| 2783   | No documented layout | `1a27c73b0938`  |
| 2774   | No documented layout | `1a27c73b0938`  |
| 2765   | No documented layout | `1a27c73b0938`  |
| 2756   | No documented layout | `1a27c73b0938`  |
| 2750   | No documented layout | `1a27c73b0938`  |
| 2743   | No documented layout | `1a27c73b0938`  |
| 2736   | No documented layout | `1a27c73b0938`  |
| 2726   | No documented layout | `1a27c73b0938`  |
| 2717   | No documented layout | `1a27c73b0938`  |
| 2709   | No documented layout | `1a27c73b0938`  |
| 2703   | No documented layout | `1a27c73b0938`  |
| 2695   | No documented layout | `1a27c73b0938`  |
| 2684   | No documented layout | `1a27c73b0938`  |
| 2672   | No documented layout | `1a27c73b0938`  |
| 2665   | No documented layout | `1a27c73b0938`  |
| 2657   | No documented layout | `1a27c73b0938`  |
| 2649   | No documented layout | `1a27c73b0938`  |
| 2644   | No documented layout | `1a27c73b0938`  |
| 2637   | No documented layout | `1a27c73b0938`  |
| 2629   | No documented layout | `1a27c73b0938`  |
| 2619   | No documented layout | `1a27c73b0938`  |
| 2612   | No documented layout | `1a27c73b0938`  |
| 2606   | No documented layout | `1a27c73b0938`  |
| 2602   | No documented layout | `1a27c73b0938`  |
| 2601   | No documented layout | `1a27c73b0938`  |
| 2592   | No documented layout | `1a27c73b0938`  |
| 2583   | No documented layout | `1a27c73b0938`  |
| 2575   | No documented layout | `1a27c73b0938`  |
| 2567   | No documented layout | `1a27c73b0938`  |
| 2560   | No documented layout | `1a27c73b0938`  |
| 2553   | No documented layout | `1a27c73b0938`  |
| 2545   | No documented layout | `1a27c73b0938`  |
| 2538   | No documented layout | `1a27c73b0938`  |
| 2529   | No documented layout | `1a27c73b0938`  |
| 2519   | No documented layout | `1a27c73b0938`  |
| 2513   | No documented layout | `1a27c73b0938`  |
| 2510   | No documented layout | `1a27c73b0938`  |
| 2507   | No documented layout | `1a27c73b0938`  |
| 2503   | No documented layout | `1a27c73b0938`  |
| 2498   | No documented layout | `1a27c73b0938`  |
| 2492   | No documented layout | `1a27c73b0938`  |
| 2487   | No documented layout | `1a27c73b0938`  |
| 2480   | No documented layout | `1a27c73b0938`  |
| 2474   | No documented layout | `1a27c73b0938`  |
| 2468   | No documented layout | `1a27c73b0938`  |
| 2460   | No documented layout | `1a27c73b0938`  |
| 2453   | No documented layout | `1a27c73b0938`  |
| 2444   | No documented layout | `1a27c73b0938`  |
| 2438   | No documented layout | `1a27c73b0938`  |
| 2434   | No documented layout | `1a27c73b0938`  |
| 2429   | No documented layout | `1a27c73b0938`  |
| 2421   | No documented layout | `1a27c73b0938`  |
| 2414   | No documented layout | `1a27c73b0938`  |
| 2407   | No documented layout | `1a27c73b0938`  |
| 2401   | No documented layout | `1a27c73b0938`  |
| 2397   | No documented layout | `1a27c73b0938`  |
| 2393   | No documented layout | `1a27c73b0938`  |
| 2384   | No documented layout | `1a27c73b0938`  |
| 2378   | No documented layout | `1a27c73b0938`  |
| 2372   | No documented layout | `1a27c73b0938`  |
| 2358   | No documented layout | `1a27c73b0938`  |
| 2352   | No documented layout | `1a27c73b0938`  |
| 2347   | No documented layout | `1a27c73b0938`  |
| 2343   | No documented layout | `1a27c73b0938`  |
| 2335   | No documented layout | `1a27c73b0938`  |
| 2327   | No documented layout | `1a27c73b0938`  |
| 2324   | No documented layout | `1a27c73b0938`  |
| 2319   | No documented layout | `1a27c73b0938`  |
| 2313   | No documented layout | `1a27c73b0938`  |
| 2308   | No documented layout | `1a27c73b0938`  |
| 2302   | No documented layout | `1a27c73b0938`  |
| 2295   | No documented layout | `1a27c73b0938`  |
| 2290   | No documented layout | `1a27c73b0938`  |
| 2284   | No documented layout | `1a27c73b0938`  |
| 2276   | No documented layout | `1a27c73b0938`  |
| 2269   | No documented layout | `1a27c73b0938`  |
| 2259   | No documented layout | `1a27c73b0938`  |
| 2250   | No documented layout | `1a27c73b0938`  |
| 2243   | No documented layout | `1a27c73b0938`  |
| 2235   | No documented layout | `1a27c73b0938`  |
| 2229   | No documented layout | `1a27c73b0938`  |
| 2224   | No documented layout | `1a27c73b0938`  |
| 2218   | No documented layout | `1a27c73b0938`  |
| 2215   | No documented layout | `1a27c73b0938`  |
| 2207   | No documented layout | `1a27c73b0938`  |
| 2203   | No documented layout | `1a27c73b0938`  |
| 2196   | No documented layout | `1a27c73b0938`  |
| 2192   | No documented layout | `1a27c73b0938`  |
| 2189   | No documented layout | `1a27c73b0938`  |
| 2183   | No documented layout | `1a27c73b0938`  |
| 2179   | No documented layout | `1a27c73b0938`  |
| 2171   | No documented layout | `1a27c73b0938`  |
| 2163   | No documented layout | `1a27c73b0938`  |
| 2156   | No documented layout | `1a27c73b0938`  |
| 2151   | No documented layout | `1a27c73b0938`  |
| 2147   | No documented layout | `1a27c73b0938`  |
| 2142   | No documented layout | `1a27c73b0938`  |
| 2138   | No documented layout | `1a27c73b0938`  |
| 2134   | No documented layout | `1a27c73b0938`  |
| 2130   | No documented layout | `1a27c73b0938`  |
| 2122   | No documented layout | `1a27c73b0938`  |
| 2107   | No documented layout | `1a27c73b0938`  |
| 2098   | No documented layout | `1a27c73b0938`  |
| 2089   | No documented layout | `1a27c73b0938`  |
| 2081   | No documented layout | `1a27c73b0938`  |
| 2073   | No documented layout | `1a27c73b0938`  |
| 2067   | No documented layout | `1a27c73b0938`  |
| 2063   | No documented layout | `1a27c73b0938`  |
| 2059   | No documented layout | `1a27c73b0938`  |
| 2052   | No documented layout | `1a27c73b0938`  |
| 2044   | No documented layout | `1a27c73b0938`  |
| 2039   | No documented layout | `1a27c73b0938`  |
| 2032   | No documented layout | `1a27c73b0938`  |
| 2025   | No documented layout | `1a27c73b0938`  |
| 2011   | No documented layout | `1a27c73b0938`  |
| 2005   | No documented layout | `1a27c73b0938`  |
| 2000   | No documented layout | `1a27c73b0938`  |
| 1996   | No documented layout | `1a27c73b0938`  |
| 1991   | No documented layout | `1a27c73b0938`  |
| 1985   | No documented layout | `1a27c73b0938`  |
| 1980   | No documented layout | `1a27c73b0938`  |
| 1969   | No documented layout | `1a27c73b0938`  |
| 1964   | No documented layout | `1a27c73b0938`  |
| 1958   | No documented layout | `1a27c73b0938`  |
| 1950   | No documented layout | `1a27c73b0938`  |
| 1945   | No documented layout | `1a27c73b0938`  |
| 1937   | No documented layout | `1a27c73b0938`  |
| 1933   | No documented layout | `1a27c73b0938`  |
| 1927   | No documented layout | `1a27c73b0938`  |
| 1921   | No documented layout | `1a27c73b0938`  |
| 1914   | No documented layout | `1a27c73b0938`  |
| 1908   | No documented layout | `1a27c73b0938`  |
| 1897   | No documented layout | `1a27c73b0938`  |
| 1892   | No documented layout | `1a27c73b0938`  |
| 1886   | No documented layout | `1a27c73b0938`  |
| 1881   | No documented layout | `1a27c73b0938`  |
| 1871   | No documented layout | `1a27c73b0938`  |
| 1866   | No documented layout | `1a27c73b0938`  |
| 1862   | No documented layout | `1a27c73b0938`  |
| 1854   | No documented layout | `1a27c73b0938`  |
| 1846   | No documented layout | `1a27c73b0938`  |
| 1838   | No documented layout | `1a27c73b0938`  |
| 1832   | No documented layout | `1a27c73b0938`  |
| 1826   | No documented layout | `1a27c73b0938`  |
| 1822   | No documented layout | `1a27c73b0938`  |
| 1818   | No documented layout | `1a27c73b0938`  |
| 1804   | No documented layout | `1a27c73b0938`  |
| 1794   | No documented layout | `1a27c73b0938`  |
| 1790   | No documented layout | `1a27c73b0938`  |
| 1784   | No file              | `1a27c73b0938`  |
| 1774   | No file              | `1a27c73b0938`  |
| 1771   | No file              | `1a27c73b0938`  |
| 1762   | No file              | `1a27c73b0938`  |
| 1759   | No file              | `1a27c73b0938`  |
| 1754   | No file              | `1a27c73b0938`  |
| 1749   | No file              | `1a27c73b0938`  |
| 1743   | No file              | `1a27c73b0938`  |
| 1737   | No file              | `1a27c73b0938`  |
| 1731   | No file              | `1a27c73b0938`  |
| 1725   | No file              | `1a27c73b0938`  |
| 1717   | No file              | `1a27c73b0938`  |
| 1710   | No file              | `1a27c73b0938`  |
| 1704   | No file              | `1a27c73b0938`  |
| 1698   | No file              | `1a27c73b0938`  |
| 1690   | No file              | `1a27c73b0938`  |
| 1685   | No file              | `1a27c73b0938`  |
| 1680   | No file              | `1a27c73b0938`  |
| 1674   | No file              | `1a27c73b0938`  |
| 1668   | No file              | `1a27c73b0938`  |
| 1659   | No file              | `1a27c73b0938`  |
| 1649   | No file              | `1a27c73b0938`  |
| 1642   | No file              | `1a27c73b0938`  |
| 1636   | No file              | `1a27c73b0938`  |
| 1628   | No file              | `1a27c73b0938`  |
| 1622   | No file              | `1a27c73b0938`  |
| 1614   | No file              | `1a27c73b0938`  |
| 1608   | No file              | `1a27c73b0938`  |
| 1602   | No file              | `1a27c73b0938`  |
| 1598   | No file              | `1a27c73b0938`  |
| 1594   | No file              | `1a27c73b0938`  |
| 1590   | No file              | `1a27c73b0938`  |
| 1587   | No file              | `1a27c73b0938`  |
| 1584   | No file              | `1a27c73b0938`  |
| 1579   | No file              | `1a27c73b0938`  |
| 1572   | No file              | `1a27c73b0938`  |
| 1565   | No file              | `1a27c73b0938`  |
| 1559   | No file              | `1a27c73b0938`  |
| 1554   | No file              | `1a27c73b0938`  |
| 1547   | No file              | `1a27c73b0938`  |
| 1537   | No file              | `1a27c73b0938`  |
| 1529   | No file              | `1a27c73b0938`  |
| 1524   | No file              | `1a27c73b0938`  |
| 1519   | No file              | `1a27c73b0938`  |
| 1509   | No file              | `1a27c73b0938`  |
| 1506   | No file              | `1a27c73b0938`  |
| 1504   | No file              | `1a27c73b0938`  |
| 1500   | No file              | `1a27c73b0938`  |
| 1493   | No file              | `1a27c73b0938`  |
| 1489   | No file              | `1a27c73b0938`  |
| 1485   | No file              | `1a27c73b0938`  |
| 1481   | No file              | `1a27c73b0938`  |
| 1474   | No file              | `1a27c73b0938`  |
| 1466   | No file              | `1a27c73b0938`  |
| 1462   | No file              | `1a27c73b0938`  |
| 1459   | No file              | `1a27c73b0938`  |
| 1453   | No file              | `1a27c73b0938`  |
| 1450   | No file              | `1a27c73b0938`  |
| 1445   | No file              | `1a27c73b0938`  |
| 1439   | No file              | `1a27c73b0938`  |
| 1433   | No file              | `1a27c73b0938`  |
| 1430   | No file              | `1a27c73b0938`  |
| 1426   | No file              | `1a27c73b0938`  |
| 1421   | No file              | `1a27c73b0938`  |
| 1417   | No file              | `1a27c73b0938`  |
| 1416   | No file              | `1a27c73b0938`  |
| 1409   | No file              | `1a27c73b0938`  |
| 1405   | No file              | `1a27c73b0938`  |
| 1401   | No file              | `1a27c73b0938`  |
| 1396   | No file              | `1a27c73b0938`  |
| 1391   | No file              | `1a27c73b0938`  |
| 1390   | No file              | `1a27c73b0938`  |
| 1386   | No file              | `1a27c73b0938`  |
| 1381   | No file              | `1a27c73b0938`  |
| 1379   | No file              | `1a27c73b0938`  |
| 1372   | No file              | `1a27c73b0938`  |
| 1366   | No file              | `1a27c73b0938`  |
| 1364   | No file              | `1a27c73b0938`  |
| 1363   | No file              | `1a27c73b0938`  |
| 1360   | No file              | `1a27c73b0938`  |
| 1358   | No file              | `1a27c73b0938`  |
| 1355   | No file              | `1a27c73b0938`  |
| 1351   | No file              | `1a27c73b0938`  |
| 1348   | No file              | `1a27c73b0938`  |
| 1346   | No file              | `1a27c73b0938`  |
| 1341   | No file              | `1a27c73b0938`  |
| 1340   | No file              | `1a27c73b0938`  |
| 1338   | No file              | `1a27c73b0938`  |
| 1335   | No file              | `1a27c73b0938`  |
| 1333   | No file              | `1a27c73b0938`  |
| 1329   | No file              | `1a27c73b0938`  |
| 1327   | No file              | `1a27c73b0938`  |
| 1324   | No file              | `1a27c73b0938`  |
| 1321   | No file              | `1a27c73b0938`  |
| 1319   | No file              | `1a27c73b0938`  |
| 1318   | No file              | `1a27c73b0938`  |
| 1316   | No file              | `1a27c73b0938`  |
| 1313   | No file              | `1a27c73b0938`  |
| 1311   | No file              | `1a27c73b0938`  |
| 1309   | No file              | `1a27c73b0938`  |
| 1304   | No file              | `1a27c73b0938`  |
| 1292   | No file              | `1a27c73b0938`  |
| 1286   | No file              | `1a27c73b0938`  |
| 1280   | No file              | `1a27c73b0938`  |
| 1276   | No file              | `1a27c73b0938`  |
| 1267   | No file              | `1a27c73b0938`  |
| 1261   | No file              | `1a27c73b0938`  |
| 1256   | No file              | `1a27c73b0938`  |
| 1250   | No file              | `1a27c73b0938`  |
| 1246   | No file              | `1a27c73b0938`  |
| 1239   | No file              | `1a27c73b0938`  |
| 1230   | No file              | `1a27c73b0938`  |
| 1226   | No file              | `1a27c73b0938`  |
| 1220   | No file              | `1a27c73b0938`  |
| 1217   | No file              | `1a27c73b0938`  |
| 1211   | No file              | `1a27c73b0938`  |
| 1210   | No file              | `1a27c73b0938`  |
| 1208   | No file              | `1a27c73b0938`  |
| 1203   | No file              | `1a27c73b0938`  |
| 1197   | No file              | `1a27c73b0938`  |
| 1194   | No file              | `1a27c73b0938`  |
| 1192   | No file              | `1a27c73b0938`  |
| 1187   | No file              | `1a27c73b0938`  |
| 1183   | No file              | `1a27c73b0938`  |
| 1177   | No file              | `1a27c73b0938`  |
| 1173   | No file              | `1a27c73b0938`  |
| 1167   | No file              | `1a27c73b0938`  |
| 1164   | No file              | `1a27c73b0938`  |
| 1156   | No file              | `1a27c73b0938`  |
| 1149   | No file              | `1a27c73b0938`  |
| 1144   | No file              | `1a27c73b0938`  |
| 1137   | No file              | `1a27c73b0938`  |
| 1132   | No file              | `1a27c73b0938`  |
| 1127   | No file              | `1a27c73b0938`  |
| 1122   | No file              | `1a27c73b0938`  |
| 1118   | No file              | `1a27c73b0938`  |
| 1114   | No file              | `1a27c73b0938`  |
| 1109   | No file              | `1a27c73b0938`  |
| 1102   | No file              | `1a27c73b0938`  |
| 1096   | No file              | `1a27c73b0938`  |
| 1088   | No file              | `1a27c73b0938`  |
| 1081   | No file              | `1a27c73b0938`  |
| 1076   | No file              | `1a27c73b0938`  |
| 1069   | No file              | `1a27c73b0938`  |
| 1064   | No file              | `1a27c73b0938`  |
| 1058   | No file              | `1a27c73b0938`  |
| 1051   | No file              | `1a27c73b0938`  |
| 1044   | No file              | `1a27c73b0938`  |
| 1036   | No file              | `1a27c73b0938`  |
| 1026   | No file              | `1a27c73b0938`  |
| 1016   | No file              | `1a27c73b0938`  |
| 1009   | No file              | `1a27c73b0938`  |
| 1005   | No file              | `1a27c73b0938`  |
| 1000   | No file              | `1a27c73b0938`  |
| 998    | No file              | `1a27c73b0938`  |
| 990    | No file              | `1a27c73b0938`  |
| 979    | No file              | `1a27c73b0938`  |
| 972    | No file              | `1a27c73b0938`  |
| 963    | No file              | `1a27c73b0938`  |
| 955    | No file              | `1a27c73b0938`  |
| 946    | No file              | `1a27c73b0938`  |
| 938    | No file              | `1a27c73b0938`  |
| 927    | No file              | `1a27c73b0938`  |
| 911    | No file              | `1a27c73b0938`  |
| 904    | No file              | `1a27c73b0938`  |
| 899    | No file              | `1a27c73b0938`  |
| 894    | No file              | `1a27c73b0938`  |
| 885    | No file              | `1a27c73b0938`  |
| 879    | No file              | `1a27c73b0938`  |
| 872    | No file              | `1a27c73b0938`  |
| 864    | No file              | `1a27c73b0938`  |
| 855    | No file              | `1a27c73b0938`  |
| 853    | No file              | `1a27c73b0938`  |
| 845    | No file              | `1a27c73b0938`  |
| 837    | No file              | `1a27c73b0938`  |
| 829    | No file              | `1a27c73b0938`  |
| 822    | No file              | `1a27c73b0938`  |
| 814    | No file              | `1a27c73b0938`  |
| 805    | No file              | `1a27c73b0938`  |
| 794    | No file              | `1a27c73b0938`  |
| 787    | No file              | `1a27c73b0938`  |
| 780    | No file              | `1a27c73b0938`  |
| 771    | No file              | `1a27c73b0938`  |
| 760    | No file              | `1a27c73b0938`  |
| 748    | No file              | `1a27c73b0938`  |
| 741    | No file              | `1a27c73b0938`  |
| 736    | No file              | `1a27c73b0938`  |
| 731    | No file              | `1a27c73b0938`  |
| 723    | No file              | `1a27c73b0938`  |
| 711    | No file              | `1a27c73b0938`  |
| 707    | No file              | `1a27c73b0938`  |
| 697    | No file              | `1a27c73b0938`  |
| 689    | No file              | `1a27c73b0938`  |
| 683    | No file              | `1a27c73b0938`  |
| 678    | No file              | `1a27c73b0938`  |
| 670    | No file              | `1a27c73b0938`  |
| 661    | No file              | `1a27c73b0938`  |
| 656    | No file              | `1a27c73b0938`  |
| 652    | No file              | `1a27c73b0938`  |
| 643    | No file              | `1a27c73b0938`  |
| 637    | No file              | `1a27c73b0938`  |
| 630    | No file              | `1a27c73b0938`  |
| 627    | No file              | `1a27c73b0938`  |
| 621    | No file              | `1a27c73b0938`  |
| 617    | No file              | `1a27c73b0938`  |
| 615    | No file              | `1a27c73b0938`  |
| 606    | No file              | `1a27c73b0938`  |
| 599    | No file              | `1a27c73b0938`  |
| 592    | No file              | `1a27c73b0938`  |
| 586    | No file              | `1a27c73b0938`  |
| 577    | No file              | `1a27c73b0938`  |
| 569    | No file              | `1a27c73b0938`  |
| 561    | No file              | `1a27c73b0938`  |
| 554    | No file              | `1a27c73b0938`  |
| 542    | No file              | `1a27c73b0938`  |
| 532    | No file              | `1a27c73b0938`  |
| 531    | No file              | `1a27c73b0938`  |
| 526    | No file              | `1a27c73b0938`  |
| 521    | No file              | `1a27c73b0938`  |
| 517    | No file              | `1a27c73b0938`  |
| 510    | No file              | `1a27c73b0938`  |
| 508    | No file              | `1a27c73b0938`  |
| 504    | No file              | `1a27c73b0938`  |
| 497    | No file              | `1a27c73b0938`  |
| 491    | No file              | `1a27c73b0938`  |
| 485    | No file              | `1a27c73b0938`  |
| 478    | No file              | `1a27c73b0938`  |
| 472    | No file              | `1a27c73b0938`  |
| 466    | No file              | `1a27c73b0938`  |
| 457    | No file              | `1a27c73b0938`  |
| 452    | No file              | `1a27c73b0938`  |
| 449    | No file              | `1a27c73b0938`  |
| 435    | No file              | `1a27c73b0938`  |

<!-- versions:end -->

## Companion Files

The file is self-contained. The handler reads these through shared lookups:

| File                  | Required | Role                                                                    |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Set name and effect (LOC type 113, `str_id1` = set ID), item names (type 0) |
| `skill.dbss`          | Optional | The buffs of the set skill at level 1 (`SKILL_BUFFS` lookup index)      |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The PABR string table layout of `buffsimply.bss` (`_common/pabr_strings.py`),
with variable-size rows and a second table between the rows and the strings.

| Offset              | Type                 | Field        | Notes                                                       |
| ------------------- | -------------------- | ------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                                |
| `+0x04`             | u32                  | count        | Number of sets; 165 on client 3464                          |
| `+0x08`             | Set Row[count]       | sets         | See Set Row                                                 |
| `sets+0x00`         | Substitute Table     | substitutes  | See Substitute Table                                        |
| `substitutes+0x00`  | String Table         | string_table | See String Table                                            |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where the substitute table ends |
| `string_table+0x04` | u32                  | zero         | Always 0                                                    |

On client 3464 the walk over 165 sets and 105 substitute rows ends at
`0x162A`, the stored `table_start`.

### Set Row (variable: 14 bytes + member IDs)

Fields are unaligned.

| Offset            | Type              | Field        | Notes                                                                  |
| ----------------- | ----------------- | ------------ | ---------------------------------------------------------------------- |
| `+0x00`           | u32               | set_id       | Unique; LOC type 113 `str_id1`, and the number in the skill name       |
| `+0x04`           | u16               | skill_no     | Passive skill of the set effect; unique                                |
| `+0x06`           | u32               | member_count | `3` or `4` on client 3464                                              |
| `+0x0A`           | u32[member_count] | member_ids   | Lightstone item IDs, ascending; a stone may repeat                     |
| `member_ids+0x00` | u32               | text_ref     | String table index of the Korean name and effect; equals the row index |

The skill confirms the set ID: LOC type 10 names skill `55078` "Set 2 -
[Well-prepared]" and skill `47521` "Set 182 - [The Wild: Edania]", and
`skill.dbss` gives skill `55078` level 1 the three buffs whose LOC type 5
first lines are the three effect lines of set 2. On client 3464 the level 1
rank of every set skill has one buff per effect line.

The text is the Korean source of the LOC type 113 row:
`<PAColor0xffd2ffad>[준비된 자]<PAOldColor>\n전투 경험치 획득량 +50%\n...`.
The first line is the name in brackets and colour, each further line one
effect. Line breaks are stored as the two characters `\` and `n`
(`_common/inline_text.py`).

### Substitute Table (variable: 4 bytes + rows)

| Offset  | Type                  | Field | Notes                         |
| ------- | --------------------- | ----- | ----------------------------- |
| `+0x00` | u32                   | count | Number of substitute rows     |
| `+0x04` | Substitute Row[count] | rows  | See Substitute Row            |

### Substitute Row (8 bytes)

| Offset  | Type | Field     | Notes                                                       |
| ------- | ---- | --------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_id   | A Lightstone item ID; unique                                |
| `+0x04` | u32  | member_id | The member item ID it counts as in `member_ids`             |

On client 3464 there are 105 rows: 53 map every member item to itself, and
52 map an Amplified Lightstone (`member_id + 200`, such as `758203`
Amplified Lightstone of Fire: Predation) to its base Lightstone. The rows are
in no sorted order. Garmoth's Lightstone sets page lists each member as "Any
of" the base and the Amplified Lightstone, which matches these rows.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Notes

- The sets with four members come first, then the sets with three, each
  group in ascending `set_id`.
- Set IDs run from 1 to 182 with 17 gaps (30, 51 to 55, 64, 66, 70, 72, 73,
  77 to 80, 164, 173). LOC type 113 still has a row for each gap
  (`[Blacksmith's Blessing]`, `[Brown Bear]`), so these are sets the client
  no longer has.
- The 21 substitute rows from `764201` to `764221` (Lightstone of Flora
  `+200`) name items with no LOC type 0 name and no item icon on client 3464;
  In-Game Checks has a test for whether they exist.
- Iridescent Lightstone (`766101`) is a member of 50 sets, always as the
  last stone.
- The `LIGHTSTONE_SETS` lookup index (`build_lightstone_set_index()` in
  `parser.py`) maps each member and substitute item ID to the sets it counts
  toward, so the [itemenchant.dbss](../dbss/itemenchant_dbss.md) Lightstone Sets
  column lists them without opening this file.
- The LOC type 113 name of set 96 repeats itself: `[Drills: Blight-Fallen]
  [Drills: Blight-Fallen]`, while the skill name is `Set 96 - [Drills:
  Blight-Fallen]`.
- Cross-check against Garmoth's Lightstone sets page (combat sets only): all
  83 sets it lists have the same members, and the first effect tier values
  equal the LOC type 113 values. Its two further columns, "Including
  Lightstone Effects" and "Including Amplified Lightstone Effects", hold
  values this file does not have.
- The Artifact window and tooltip Lua (`panel_window_artifacts_all`,
  `panel_equiment_artifactstooltip`) get the active set through
  `ToClient_getLightStoneSet`, `ToClient_getLightStoneSetByInvenSlotNo` and
  `ToClient_getLightStoneSetByFromLifeEquipSlotNo` and write it to the set
  option text.

## In-Game Checks

### Amplified Lightstones of Flora

Needs item (all):

- [Lightstone of Flora: Wildlife](https://bdocodex.com/us/item/764001/), or any other Lightstone of Flora (`764001` to `764021`)
- [Crystallized Energy of Endtimes](https://bdocodex.com/us/item/821252/) x30
- [Magical Shard](https://bdocodex.com/us/item/4918/) x50
- [Magical Lightstone Crystal](https://bdocodex.com/us/item/766108/) x100

The LOC description of Crystallized Energy of Endtimes gives the Amplified
Lightstone recipe: Heating "Lightstone (any type) x1" with the three
materials above. Heat a Lightstone of Flora with them. If it gives an
Amplified Lightstone of Flora (item `764001` + 200 = `764201` for Wildlife),
the 21 substitute rows from `764201` to `764221` are live items whose name
and icon the client lacks. If Heating rejects a Flora Lightstone, they are
rows for items the game does not hand out.
