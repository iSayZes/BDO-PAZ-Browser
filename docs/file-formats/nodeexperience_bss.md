# `nodeexperience.bss` Format

## Purpose

EXP table of the node levels: the EXP a node needs to go from one node level to the next. Players raise a node's level on the world map by investing Energy ("Energy can be consumed to increase a Node's level."). One 15-byte row per level, levels 0 to 20 on client 3464.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                 | Bytes | Records      | Row bytes |
| ------ | ------------- | ------- | -------------------- | ----- | ------------ | --------- |
| 1      | 805 and later | 3483    | `nodeexperience.bss` | 335   | 21 Level Row | 15        |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 1      | `nodeexperience.bss` | 335 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `af1ab0bf8359`  |
| 3482   | Layout 1             | `af1ab0bf8359`  |
| 3474   | Layout 1             | `af1ab0bf8359`  |
| 3473   | Layout 1             | `af1ab0bf8359`  |
| 3464   | Layout 1             | `af1ab0bf8359`  |
| 3458   | Layout 1             | `af1ab0bf8359`  |
| 3454   | Layout 1             | `af1ab0bf8359`  |
| 3444   | Layout 1             | `af1ab0bf8359`  |
| 3435   | Layout 1             | `af1ab0bf8359`  |
| 3426   | Layout 1             | `af1ab0bf8359`  |
| 3418   | Layout 1             | `af1ab0bf8359`  |
| 3412   | Layout 1             | `af1ab0bf8359`  |
| 3402   | Layout 1             | `af1ab0bf8359`  |
| 3396   | Layout 1             | `af1ab0bf8359`  |
| 3387   | Layout 1             | `af1ab0bf8359`  |
| 3381   | Layout 1             | `af1ab0bf8359`  |
| 3373   | Layout 1             | `af1ab0bf8359`  |
| 3364   | Layout 1             | `af1ab0bf8359`  |
| 3356   | Layout 1             | `af1ab0bf8359`  |
| 3349   | Layout 1             | `af1ab0bf8359`  |
| 3342   | Layout 1             | `af1ab0bf8359`  |
| 3335   | Layout 1             | `af1ab0bf8359`  |
| 3326   | Layout 1             | `af1ab0bf8359`  |
| 3321   | Layout 1             | `af1ab0bf8359`  |
| 3314   | Layout 1             | `af1ab0bf8359`  |
| 3303   | Layout 1             | `af1ab0bf8359`  |
| 3302   | Layout 1             | `af1ab0bf8359`  |
| 3293   | Layout 1             | `af1ab0bf8359`  |
| 3283   | Layout 1             | `af1ab0bf8359`  |
| 3275   | Layout 1             | `af1ab0bf8359`  |
| 3267   | Layout 1             | `af1ab0bf8359`  |
| 3258   | Layout 1             | `af1ab0bf8359`  |
| 3251   | Layout 1             | `af1ab0bf8359`  |
| 3242   | Layout 1             | `af1ab0bf8359`  |
| 3235   | Layout 1             | `af1ab0bf8359`  |
| 3229   | Layout 1             | `af1ab0bf8359`  |
| 3212   | Layout 1             | `af1ab0bf8359`  |
| 3203   | Layout 1             | `af1ab0bf8359`  |
| 3193   | Layout 1             | `af1ab0bf8359`  |
| 3186   | Layout 1             | `af1ab0bf8359`  |
| 3177   | Layout 1             | `af1ab0bf8359`  |
| 3169   | Layout 1             | `af1ab0bf8359`  |
| 3158   | Layout 1             | `af1ab0bf8359`  |
| 3151   | Layout 1             | `af1ab0bf8359`  |
| 3144   | Layout 1             | `af1ab0bf8359`  |
| 3133   | Layout 1             | `af1ab0bf8359`  |
| 3125   | Layout 1             | `af1ab0bf8359`  |
| 3118   | Layout 1             | `af1ab0bf8359`  |
| 3111   | Layout 1             | `af1ab0bf8359`  |
| 3103   | Layout 1             | `af1ab0bf8359`  |
| 3095   | Layout 1             | `af1ab0bf8359`  |
| 3086   | Layout 1             | `af1ab0bf8359`  |
| 3072   | Layout 1             | `af1ab0bf8359`  |
| 3062   | Layout 1             | `af1ab0bf8359`  |
| 3052   | Layout 1             | `af1ab0bf8359`  |
| 3045   | Layout 1             | `af1ab0bf8359`  |
| 3037   | Layout 1             | `af1ab0bf8359`  |
| 3030   | Layout 1             | `af1ab0bf8359`  |
| 3021   | Layout 1             | `af1ab0bf8359`  |
| 3012   | Layout 1             | `af1ab0bf8359`  |
| 3002   | Layout 1             | `af1ab0bf8359`  |
| 2995   | Layout 1             | `af1ab0bf8359`  |
| 2987   | Layout 1             | `af1ab0bf8359`  |
| 2978   | Layout 1             | `af1ab0bf8359`  |
| 2970   | Layout 1             | `af1ab0bf8359`  |
| 2959   | Layout 1             | `af1ab0bf8359`  |
| 2951   | Layout 1             | `af1ab0bf8359`  |
| 2942   | Layout 1             | `af1ab0bf8359`  |
| 2935   | Layout 1             | `af1ab0bf8359`  |
| 2932   | Layout 1             | `af1ab0bf8359`  |
| 2923   | Layout 1             | `af1ab0bf8359`  |
| 2919   | Layout 1             | `af1ab0bf8359`  |
| 2907   | Layout 1             | `af1ab0bf8359`  |
| 2900   | Layout 1             | `af1ab0bf8359`  |
| 2891   | Layout 1             | `af1ab0bf8359`  |
| 2882   | Layout 1             | `af1ab0bf8359`  |
| 2872   | Layout 1             | `af1ab0bf8359`  |
| 2863   | Layout 1             | `af1ab0bf8359`  |
| 2855   | Layout 1             | `af1ab0bf8359`  |
| 2849   | Layout 1             | `af1ab0bf8359`  |
| 2844   | Layout 1             | `af1ab0bf8359`  |
| 2834   | Layout 1             | `af1ab0bf8359`  |
| 2825   | Layout 1             | `af1ab0bf8359`  |
| 2819   | Layout 1             | `af1ab0bf8359`  |
| 2811   | Layout 1             | `af1ab0bf8359`  |
| 2803   | Layout 1             | `af1ab0bf8359`  |
| 2794   | Layout 1             | `af1ab0bf8359`  |
| 2783   | Layout 1             | `af1ab0bf8359`  |
| 2774   | Layout 1             | `af1ab0bf8359`  |
| 2765   | Layout 1             | `af1ab0bf8359`  |
| 2756   | Layout 1             | `af1ab0bf8359`  |
| 2750   | Layout 1             | `af1ab0bf8359`  |
| 2743   | Layout 1             | `af1ab0bf8359`  |
| 2736   | Layout 1             | `af1ab0bf8359`  |
| 2726   | Layout 1             | `af1ab0bf8359`  |
| 2717   | Layout 1             | `af1ab0bf8359`  |
| 2709   | Layout 1             | `af1ab0bf8359`  |
| 2703   | Layout 1             | `af1ab0bf8359`  |
| 2695   | Layout 1             | `af1ab0bf8359`  |
| 2684   | Layout 1             | `af1ab0bf8359`  |
| 2672   | Layout 1             | `af1ab0bf8359`  |
| 2665   | Layout 1             | `af1ab0bf8359`  |
| 2657   | Layout 1             | `af1ab0bf8359`  |
| 2649   | Layout 1             | `af1ab0bf8359`  |
| 2644   | Layout 1             | `af1ab0bf8359`  |
| 2637   | Layout 1             | `af1ab0bf8359`  |
| 2629   | Layout 1             | `af1ab0bf8359`  |
| 2619   | Layout 1             | `af1ab0bf8359`  |
| 2612   | Layout 1             | `af1ab0bf8359`  |
| 2606   | Layout 1             | `af1ab0bf8359`  |
| 2602   | Layout 1             | `af1ab0bf8359`  |
| 2601   | Layout 1             | `af1ab0bf8359`  |
| 2592   | Layout 1             | `af1ab0bf8359`  |
| 2583   | Layout 1             | `af1ab0bf8359`  |
| 2575   | Layout 1             | `af1ab0bf8359`  |
| 2567   | Layout 1             | `af1ab0bf8359`  |
| 2560   | Layout 1             | `af1ab0bf8359`  |
| 2553   | Layout 1             | `af1ab0bf8359`  |
| 2545   | Layout 1             | `af1ab0bf8359`  |
| 2538   | Layout 1             | `af1ab0bf8359`  |
| 2529   | Layout 1             | `af1ab0bf8359`  |
| 2519   | Layout 1             | `af1ab0bf8359`  |
| 2513   | Layout 1             | `af1ab0bf8359`  |
| 2510   | Layout 1             | `af1ab0bf8359`  |
| 2507   | Layout 1             | `af1ab0bf8359`  |
| 2503   | Layout 1             | `af1ab0bf8359`  |
| 2498   | Layout 1             | `af1ab0bf8359`  |
| 2492   | Layout 1             | `af1ab0bf8359`  |
| 2487   | Layout 1             | `af1ab0bf8359`  |
| 2480   | Layout 1             | `af1ab0bf8359`  |
| 2474   | Layout 1             | `af1ab0bf8359`  |
| 2468   | Layout 1             | `af1ab0bf8359`  |
| 2460   | Layout 1             | `af1ab0bf8359`  |
| 2453   | Layout 1             | `af1ab0bf8359`  |
| 2444   | Layout 1             | `af1ab0bf8359`  |
| 2438   | Layout 1             | `af1ab0bf8359`  |
| 2434   | Layout 1             | `af1ab0bf8359`  |
| 2429   | Layout 1             | `af1ab0bf8359`  |
| 2421   | Layout 1             | `af1ab0bf8359`  |
| 2414   | Layout 1             | `af1ab0bf8359`  |
| 2407   | Layout 1             | `af1ab0bf8359`  |
| 2401   | Layout 1             | `af1ab0bf8359`  |
| 2397   | Layout 1             | `af1ab0bf8359`  |
| 2393   | Layout 1             | `af1ab0bf8359`  |
| 2384   | Layout 1             | `af1ab0bf8359`  |
| 2378   | Layout 1             | `af1ab0bf8359`  |
| 2372   | Layout 1             | `af1ab0bf8359`  |
| 2358   | Layout 1             | `af1ab0bf8359`  |
| 2352   | Layout 1             | `af1ab0bf8359`  |
| 2347   | Layout 1             | `af1ab0bf8359`  |
| 2343   | Layout 1             | `af1ab0bf8359`  |
| 2335   | Layout 1             | `af1ab0bf8359`  |
| 2327   | Layout 1             | `af1ab0bf8359`  |
| 2324   | Layout 1             | `af1ab0bf8359`  |
| 2319   | Layout 1             | `af1ab0bf8359`  |
| 2313   | Layout 1             | `af1ab0bf8359`  |
| 2308   | Layout 1             | `af1ab0bf8359`  |
| 2302   | Layout 1             | `af1ab0bf8359`  |
| 2295   | Layout 1             | `af1ab0bf8359`  |
| 2290   | Layout 1             | `af1ab0bf8359`  |
| 2284   | Layout 1             | `af1ab0bf8359`  |
| 2276   | Layout 1             | `af1ab0bf8359`  |
| 2269   | Layout 1             | `af1ab0bf8359`  |
| 2259   | Layout 1             | `af1ab0bf8359`  |
| 2250   | Layout 1             | `af1ab0bf8359`  |
| 2243   | Layout 1             | `af1ab0bf8359`  |
| 2235   | Layout 1             | `af1ab0bf8359`  |
| 2229   | Layout 1             | `af1ab0bf8359`  |
| 2224   | Layout 1             | `af1ab0bf8359`  |
| 2218   | Layout 1             | `af1ab0bf8359`  |
| 2215   | Layout 1             | `af1ab0bf8359`  |
| 2207   | Layout 1             | `af1ab0bf8359`  |
| 2203   | Layout 1             | `af1ab0bf8359`  |
| 2196   | Layout 1             | `af1ab0bf8359`  |
| 2192   | Layout 1             | `af1ab0bf8359`  |
| 2189   | Layout 1             | `af1ab0bf8359`  |
| 2183   | Layout 1             | `af1ab0bf8359`  |
| 2179   | Layout 1             | `af1ab0bf8359`  |
| 2171   | Layout 1             | `af1ab0bf8359`  |
| 2163   | Layout 1             | `af1ab0bf8359`  |
| 2156   | Layout 1             | `af1ab0bf8359`  |
| 2151   | Layout 1             | `af1ab0bf8359`  |
| 2147   | Layout 1             | `af1ab0bf8359`  |
| 2142   | Layout 1             | `af1ab0bf8359`  |
| 2138   | Layout 1             | `af1ab0bf8359`  |
| 2134   | Layout 1             | `af1ab0bf8359`  |
| 2130   | Layout 1             | `af1ab0bf8359`  |
| 2122   | Layout 1             | `af1ab0bf8359`  |
| 2107   | Layout 1             | `af1ab0bf8359`  |
| 2098   | Layout 1             | `af1ab0bf8359`  |
| 2089   | Layout 1             | `af1ab0bf8359`  |
| 2081   | Layout 1             | `af1ab0bf8359`  |
| 2073   | Layout 1             | `af1ab0bf8359`  |
| 2067   | Layout 1             | `af1ab0bf8359`  |
| 2063   | Layout 1             | `af1ab0bf8359`  |
| 2059   | Layout 1             | `af1ab0bf8359`  |
| 2052   | Layout 1             | `af1ab0bf8359`  |
| 2044   | Layout 1             | `af1ab0bf8359`  |
| 2039   | Layout 1             | `af1ab0bf8359`  |
| 2032   | Layout 1             | `af1ab0bf8359`  |
| 2025   | Layout 1             | `af1ab0bf8359`  |
| 2011   | Layout 1             | `af1ab0bf8359`  |
| 2005   | Layout 1             | `af1ab0bf8359`  |
| 2000   | Layout 1             | `af1ab0bf8359`  |
| 1996   | Layout 1             | `af1ab0bf8359`  |
| 1991   | Layout 1             | `af1ab0bf8359`  |
| 1985   | Layout 1             | `af1ab0bf8359`  |
| 1980   | Layout 1             | `af1ab0bf8359`  |
| 1969   | Layout 1             | `af1ab0bf8359`  |
| 1964   | Layout 1             | `af1ab0bf8359`  |
| 1958   | Layout 1             | `af1ab0bf8359`  |
| 1950   | Layout 1             | `af1ab0bf8359`  |
| 1945   | Layout 1             | `af1ab0bf8359`  |
| 1937   | Layout 1             | `af1ab0bf8359`  |
| 1933   | Layout 1             | `af1ab0bf8359`  |
| 1927   | Layout 1             | `af1ab0bf8359`  |
| 1921   | Layout 1             | `af1ab0bf8359`  |
| 1914   | Layout 1             | `af1ab0bf8359`  |
| 1908   | Layout 1             | `af1ab0bf8359`  |
| 1897   | Layout 1             | `af1ab0bf8359`  |
| 1892   | Layout 1             | `af1ab0bf8359`  |
| 1886   | Layout 1             | `af1ab0bf8359`  |
| 1881   | Layout 1             | `af1ab0bf8359`  |
| 1871   | Layout 1             | `af1ab0bf8359`  |
| 1866   | Layout 1             | `af1ab0bf8359`  |
| 1862   | Layout 1             | `af1ab0bf8359`  |
| 1854   | Layout 1             | `af1ab0bf8359`  |
| 1846   | Layout 1             | `af1ab0bf8359`  |
| 1838   | Layout 1             | `af1ab0bf8359`  |
| 1832   | Layout 1             | `af1ab0bf8359`  |
| 1826   | Layout 1             | `af1ab0bf8359`  |
| 1822   | Layout 1             | `af1ab0bf8359`  |
| 1818   | Layout 1             | `af1ab0bf8359`  |
| 1804   | Layout 1             | `af1ab0bf8359`  |
| 1794   | Layout 1             | `af1ab0bf8359`  |
| 1790   | Layout 1             | `af1ab0bf8359`  |
| 1784   | Layout 1             | `af1ab0bf8359`  |
| 1774   | Layout 1             | `af1ab0bf8359`  |
| 1771   | Layout 1             | `af1ab0bf8359`  |
| 1762   | Layout 1             | `af1ab0bf8359`  |
| 1759   | Layout 1             | `af1ab0bf8359`  |
| 1754   | Layout 1             | `af1ab0bf8359`  |
| 1749   | Layout 1             | `af1ab0bf8359`  |
| 1743   | Layout 1             | `af1ab0bf8359`  |
| 1737   | Layout 1             | `af1ab0bf8359`  |
| 1731   | Layout 1             | `af1ab0bf8359`  |
| 1725   | Layout 1             | `af1ab0bf8359`  |
| 1717   | Layout 1             | `af1ab0bf8359`  |
| 1710   | Layout 1             | `af1ab0bf8359`  |
| 1704   | Layout 1             | `af1ab0bf8359`  |
| 1698   | Layout 1             | `af1ab0bf8359`  |
| 1690   | Layout 1             | `af1ab0bf8359`  |
| 1685   | Layout 1             | `af1ab0bf8359`  |
| 1680   | Layout 1             | `af1ab0bf8359`  |
| 1674   | Layout 1             | `af1ab0bf8359`  |
| 1668   | Layout 1             | `af1ab0bf8359`  |
| 1659   | Layout 1             | `af1ab0bf8359`  |
| 1649   | Layout 1             | `af1ab0bf8359`  |
| 1642   | Layout 1             | `af1ab0bf8359`  |
| 1636   | Layout 1             | `af1ab0bf8359`  |
| 1628   | Layout 1             | `af1ab0bf8359`  |
| 1622   | Layout 1             | `af1ab0bf8359`  |
| 1614   | Layout 1             | `af1ab0bf8359`  |
| 1608   | Layout 1             | `af1ab0bf8359`  |
| 1602   | Layout 1             | `af1ab0bf8359`  |
| 1598   | Layout 1             | `af1ab0bf8359`  |
| 1594   | Layout 1             | `af1ab0bf8359`  |
| 1590   | Layout 1             | `af1ab0bf8359`  |
| 1587   | Layout 1             | `af1ab0bf8359`  |
| 1584   | Layout 1             | `af1ab0bf8359`  |
| 1579   | Layout 1             | `af1ab0bf8359`  |
| 1572   | Layout 1             | `af1ab0bf8359`  |
| 1565   | Layout 1             | `af1ab0bf8359`  |
| 1559   | Layout 1             | `af1ab0bf8359`  |
| 1554   | Layout 1             | `af1ab0bf8359`  |
| 1547   | Layout 1             | `af1ab0bf8359`  |
| 1537   | Layout 1             | `af1ab0bf8359`  |
| 1529   | Layout 1             | `af1ab0bf8359`  |
| 1524   | Layout 1             | `af1ab0bf8359`  |
| 1519   | Layout 1             | `af1ab0bf8359`  |
| 1509   | Layout 1             | `af1ab0bf8359`  |
| 1506   | Layout 1             | `af1ab0bf8359`  |
| 1504   | Layout 1             | `af1ab0bf8359`  |
| 1500   | Layout 1             | `af1ab0bf8359`  |
| 1493   | Layout 1             | `af1ab0bf8359`  |
| 1489   | Layout 1             | `af1ab0bf8359`  |
| 1485   | Layout 1             | `af1ab0bf8359`  |
| 1481   | Layout 1             | `af1ab0bf8359`  |
| 1474   | Layout 1             | `af1ab0bf8359`  |
| 1466   | Layout 1             | `af1ab0bf8359`  |
| 1462   | Layout 1             | `af1ab0bf8359`  |
| 1459   | Layout 1             | `af1ab0bf8359`  |
| 1453   | Layout 1             | `af1ab0bf8359`  |
| 1450   | Layout 1             | `af1ab0bf8359`  |
| 1445   | Layout 1             | `af1ab0bf8359`  |
| 1439   | Layout 1             | `af1ab0bf8359`  |
| 1433   | Layout 1             | `af1ab0bf8359`  |
| 1430   | Layout 1             | `af1ab0bf8359`  |
| 1426   | Layout 1             | `af1ab0bf8359`  |
| 1421   | Layout 1             | `af1ab0bf8359`  |
| 1417   | Layout 1             | `af1ab0bf8359`  |
| 1416   | Layout 1             | `af1ab0bf8359`  |
| 1409   | Layout 1             | `af1ab0bf8359`  |
| 1405   | Layout 1             | `af1ab0bf8359`  |
| 1401   | Layout 1             | `af1ab0bf8359`  |
| 1396   | Layout 1             | `af1ab0bf8359`  |
| 1391   | Layout 1             | `af1ab0bf8359`  |
| 1390   | Layout 1             | `af1ab0bf8359`  |
| 1386   | Layout 1             | `af1ab0bf8359`  |
| 1381   | Layout 1             | `af1ab0bf8359`  |
| 1379   | Layout 1             | `af1ab0bf8359`  |
| 1372   | Layout 1             | `af1ab0bf8359`  |
| 1366   | Layout 1             | `af1ab0bf8359`  |
| 1364   | Layout 1             | `af1ab0bf8359`  |
| 1363   | Layout 1             | `af1ab0bf8359`  |
| 1360   | Layout 1             | `af1ab0bf8359`  |
| 1358   | Layout 1             | `af1ab0bf8359`  |
| 1355   | Layout 1             | `af1ab0bf8359`  |
| 1351   | Layout 1             | `af1ab0bf8359`  |
| 1348   | Layout 1             | `af1ab0bf8359`  |
| 1346   | Layout 1             | `af1ab0bf8359`  |
| 1341   | Layout 1             | `af1ab0bf8359`  |
| 1340   | Layout 1             | `af1ab0bf8359`  |
| 1338   | Layout 1             | `af1ab0bf8359`  |
| 1335   | Layout 1             | `af1ab0bf8359`  |
| 1333   | Layout 1             | `af1ab0bf8359`  |
| 1329   | Layout 1             | `af1ab0bf8359`  |
| 1327   | Layout 1             | `af1ab0bf8359`  |
| 1324   | Layout 1             | `af1ab0bf8359`  |
| 1321   | Layout 1             | `af1ab0bf8359`  |
| 1319   | Layout 1             | `af1ab0bf8359`  |
| 1318   | Layout 1             | `af1ab0bf8359`  |
| 1316   | Layout 1             | `af1ab0bf8359`  |
| 1313   | Layout 1             | `af1ab0bf8359`  |
| 1311   | Layout 1             | `af1ab0bf8359`  |
| 1309   | Layout 1             | `af1ab0bf8359`  |
| 1304   | Layout 1             | `af1ab0bf8359`  |
| 1292   | Layout 1             | `af1ab0bf8359`  |
| 1286   | Layout 1             | `af1ab0bf8359`  |
| 1280   | Layout 1             | `af1ab0bf8359`  |
| 1276   | Layout 1             | `af1ab0bf8359`  |
| 1267   | Layout 1             | `af1ab0bf8359`  |
| 1261   | Layout 1             | `af1ab0bf8359`  |
| 1256   | Layout 1             | `af1ab0bf8359`  |
| 1250   | Layout 1             | `af1ab0bf8359`  |
| 1246   | Layout 1             | `af1ab0bf8359`  |
| 1239   | Layout 1             | `af1ab0bf8359`  |
| 1230   | Layout 1             | `af1ab0bf8359`  |
| 1226   | Layout 1             | `af1ab0bf8359`  |
| 1220   | Layout 1             | `af1ab0bf8359`  |
| 1217   | Layout 1             | `af1ab0bf8359`  |
| 1211   | Layout 1             | `af1ab0bf8359`  |
| 1210   | Layout 1             | `af1ab0bf8359`  |
| 1208   | Layout 1             | `af1ab0bf8359`  |
| 1203   | Layout 1             | `af1ab0bf8359`  |
| 1197   | Layout 1             | `af1ab0bf8359`  |
| 1194   | Layout 1             | `af1ab0bf8359`  |
| 1192   | Layout 1             | `af1ab0bf8359`  |
| 1187   | Layout 1             | `af1ab0bf8359`  |
| 1183   | Layout 1             | `af1ab0bf8359`  |
| 1177   | Layout 1             | `af1ab0bf8359`  |
| 1173   | Layout 1             | `af1ab0bf8359`  |
| 1167   | Layout 1             | `af1ab0bf8359`  |
| 1164   | Layout 1             | `af1ab0bf8359`  |
| 1156   | Layout 1             | `af1ab0bf8359`  |
| 1149   | Layout 1             | `af1ab0bf8359`  |
| 1144   | Layout 1             | `af1ab0bf8359`  |
| 1137   | Layout 1             | `af1ab0bf8359`  |
| 1132   | Layout 1             | `af1ab0bf8359`  |
| 1127   | Layout 1             | `af1ab0bf8359`  |
| 1122   | Layout 1             | `af1ab0bf8359`  |
| 1118   | Layout 1             | `af1ab0bf8359`  |
| 1114   | Layout 1             | `af1ab0bf8359`  |
| 1109   | Layout 1             | `af1ab0bf8359`  |
| 1102   | No file              | `af1ab0bf8359`  |
| 1096   | No file              | `af1ab0bf8359`  |
| 1088   | No file              | `af1ab0bf8359`  |
| 1081   | No file              | `af1ab0bf8359`  |
| 1076   | No file              | `af1ab0bf8359`  |
| 1069   | No file              | `af1ab0bf8359`  |
| 1064   | No file              | `af1ab0bf8359`  |
| 1058   | No file              | `af1ab0bf8359`  |
| 1051   | No file              | `af1ab0bf8359`  |
| 1044   | No file              | `af1ab0bf8359`  |
| 1036   | No file              | `af1ab0bf8359`  |
| 1026   | No file              | `af1ab0bf8359`  |
| 1016   | No file              | `af1ab0bf8359`  |
| 1009   | No file              | `af1ab0bf8359`  |
| 1005   | No file              | `af1ab0bf8359`  |
| 1000   | No file              | `af1ab0bf8359`  |
| 998    | No file              | `af1ab0bf8359`  |
| 990    | No file              | `af1ab0bf8359`  |
| 979    | No file              | `af1ab0bf8359`  |
| 972    | No file              | `af1ab0bf8359`  |
| 963    | No file              | `af1ab0bf8359`  |
| 955    | No file              | `af1ab0bf8359`  |
| 946    | No file              | `af1ab0bf8359`  |
| 938    | No file              | `af1ab0bf8359`  |
| 927    | No file              | `af1ab0bf8359`  |
| 911    | No file              | `af1ab0bf8359`  |
| 904    | No file              | `af1ab0bf8359`  |
| 899    | No file              | `af1ab0bf8359`  |
| 894    | No file              | `af1ab0bf8359`  |
| 885    | No file              | `af1ab0bf8359`  |
| 879    | No file              | `af1ab0bf8359`  |
| 872    | No file              | `af1ab0bf8359`  |
| 864    | No file              | `af1ab0bf8359`  |
| 855    | No file              | `af1ab0bf8359`  |
| 853    | No file              | `af1ab0bf8359`  |
| 845    | No file              | `af1ab0bf8359`  |
| 837    | No file              | `af1ab0bf8359`  |
| 829    | Layout 1             | `af1ab0bf8359`  |
| 822    | Layout 1             | `af1ab0bf8359`  |
| 814    | Layout 1             | `af1ab0bf8359`  |
| 805    | Layout 1             | `af1ab0bf8359`  |
| 794    | No documented layout | `af1ab0bf8359`  |
| 787    | No documented layout | `af1ab0bf8359`  |
| 780    | No documented layout | `af1ab0bf8359`  |
| 771    | No documented layout | `af1ab0bf8359`  |
| 760    | No documented layout | `af1ab0bf8359`  |
| 748    | No documented layout | `af1ab0bf8359`  |
| 741    | No documented layout | `af1ab0bf8359`  |
| 736    | No documented layout | `af1ab0bf8359`  |
| 731    | No documented layout | `af1ab0bf8359`  |
| 723    | No documented layout | `af1ab0bf8359`  |
| 711    | No documented layout | `af1ab0bf8359`  |
| 707    | No documented layout | `af1ab0bf8359`  |
| 697    | No documented layout | `af1ab0bf8359`  |
| 689    | No documented layout | `af1ab0bf8359`  |
| 683    | No documented layout | `af1ab0bf8359`  |
| 678    | No documented layout | `af1ab0bf8359`  |
| 670    | No documented layout | `af1ab0bf8359`  |
| 661    | No documented layout | `af1ab0bf8359`  |
| 656    | No documented layout | `af1ab0bf8359`  |
| 652    | No documented layout | `af1ab0bf8359`  |
| 643    | No documented layout | `af1ab0bf8359`  |
| 637    | No documented layout | `af1ab0bf8359`  |
| 630    | No documented layout | `af1ab0bf8359`  |
| 627    | No documented layout | `af1ab0bf8359`  |
| 621    | No documented layout | `af1ab0bf8359`  |
| 617    | No documented layout | `af1ab0bf8359`  |
| 615    | No documented layout | `af1ab0bf8359`  |
| 606    | No documented layout | `af1ab0bf8359`  |
| 599    | No documented layout | `af1ab0bf8359`  |
| 592    | No documented layout | `af1ab0bf8359`  |
| 586    | No documented layout | `af1ab0bf8359`  |
| 577    | No documented layout | `af1ab0bf8359`  |
| 569    | No documented layout | `af1ab0bf8359`  |
| 561    | No documented layout | `af1ab0bf8359`  |
| 554    | No documented layout | `af1ab0bf8359`  |
| 542    | No documented layout | `af1ab0bf8359`  |
| 532    | No documented layout | `af1ab0bf8359`  |
| 531    | No documented layout | `af1ab0bf8359`  |
| 526    | No documented layout | `af1ab0bf8359`  |
| 521    | No documented layout | `af1ab0bf8359`  |
| 517    | No documented layout | `af1ab0bf8359`  |
| 510    | No documented layout | `af1ab0bf8359`  |
| 508    | No documented layout | `af1ab0bf8359`  |
| 504    | No documented layout | `af1ab0bf8359`  |
| 497    | No documented layout | `af1ab0bf8359`  |
| 491    | No documented layout | `af1ab0bf8359`  |
| 485    | No documented layout | `af1ab0bf8359`  |
| 478    | No documented layout | `af1ab0bf8359`  |
| 472    | No documented layout | `af1ab0bf8359`  |
| 466    | No documented layout | `af1ab0bf8359`  |
| 457    | No documented layout | `af1ab0bf8359`  |
| 452    | No documented layout | `af1ab0bf8359`  |
| 449    | No documented layout | `af1ab0bf8359`  |
| 435    | No documented layout | `af1ab0bf8359`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

`PABR` magic, a u32 row count, the rows, then the 12-byte PABR trailer. 335 bytes on client 3464 (21 rows).

| Offset     | Type                 | Field        | Notes                                  |
| ---------- | -------------------- | ------------ | -------------------------------------- |
| `+0x00`    | char[4]              | magic        | `PABR` (ASCII)                         |
| `+0x04`    | u32                  | row_count    | 21 on client 3464                      |
| `+0x08`    | Level Row[row_count] | rows         | `row_count` rows of 15 bytes, level 0 first |
| `EOF-0x0C` | u32                  | string_count | `0`: the empty PABR string table       |
| `EOF-0x08` | u32                  | end_of_data  | Byte offset right after the last row (`0x143` on client 3464) |
| `EOF-0x04` | u32                  | zero         | `0`                                    |

The parser checks that `8 + row_count x 15` equals `end_of_data` and that the trailer closes the file.

### Level Row (15 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u8   | is_integrity  | `0` on the level 0 row, `1` on every other row; see Field Names |
| `+0x01` | u32  | node_exp_type | `0` on every row (client 3474); see Field Names              |
| `+0x05` | i16  | level         | Node level; equals the row index                             |
| `+0x07` | i64  | exp           | EXP to go from `level` to `level + 1` (Notes)                |

## Field Names

The 2016 client with debug symbols holds the row as
`gc::NodeExperienceStaticStatus` (24 bytes): bool `_isIntegrity` at `+0`,
int `_nodeExpType` at `+4`, short `_nodeLevel` at `+8` and `__int64`
`_requiredExperience` at `+0x10`. The file stores the four members in that
order without the padding. A private server on client 1784 loads the same
struct from its `NodeEXP_Table` sheet (loader at VA `0x1408c20e0`): `Level`
into `_nodeLevel`, `RequireEXP` into `_requiredExperience` and `Type` into
`_nodeExpType` (setter VA `0x140bb0a7d`); the register step indexes the
manager's per-type lists by `_nodeExpType`. Its own `nodeexperience.bss`
matches the sheet on all 11 rows.

`_isIntegrity` has no sheet column. The setter writes `0`, and the
integrity pass (VA `0x140bb1050`) sets it to `1` on every row after the
first while it checks that the needed EXP never falls ("required EXP cannot
be smaller than the previous level's"). That is the `0` on level 0 and `1`
on every other row of both clients. The loader also rejects a row with a
needed EXP below 1, which is why level 0 holds `1`.

## Notes

- The world map node menu (`grand_worldmap_nodemenu.luac`, decompiled with unluac) draws the node level bar as `ToClient_GetNodeExperience_s64(nodeKey) / ToClient_GetNeedExperienceToNextNodeLevel_s64(nodeKey)` and shows `Lv. <level>/<ToClient_GetNodeMaxLevel()>`, so the EXP restarts at 0 on every level, as in [skillexperience](skillexperience_dbss.md). Both getters return s64, which matches the i64 `exp`.
- The row direction (row N is the EXP from N to N + 1) follows `skillexperience.dbss` and `lifeexp.dbss`. The values are not cumulative totals: levels 19 and 20 both hold 200,000, which as totals would make level 20 free.
- `panel_personalicon_left_remaster.luac` counts a node as invested only when `0 < ToClient_GetNodeLevel(wayPointKey)`, so level 0 is a node with no investment. The level 0 row needs 1 EXP and is the only row with `is_integrity` `0`. The node menu never shows level 0 in game; a node shows level 1 as its lowest level.
- The node menu invests Energy in steps of 10: `InvestNodeLevelExecute` multiplies the number pad value by 10 and sends it with `ToClient_RequestIncreaseExperienceNodeByCharacterIndex`; the number pad max is `floor(character Energy / 10)`. The server turns Energy into node EXP; no client Lua or data file holds the rate. The client 1784 server dump sets `100` in the `gc::NodeExperienceStaticStatusManager` constructor (VA `0x1401c032b`), in the member the 2016 PDB names `const __int64 _increasePerWP`.
- 1 Energy = 100 node EXP, so a level needs `exp / 100` Energy. Checked in game on three levels: level 1 to 2 took 100 Energy (10,000 EXP), level 2 to 3 took 200 (20,000) and level 3 to 4 took 400 (40,000). Level 1 to 20 is 2,070,000 EXP, or 20,700 Energy.
- Curve on client 3464: level 0 needs 1, level 1 needs 10,000 and level 2 needs 20,000; from level 3 each level needs 40,000 + 10,000 x (N - 3), up to 200,000 at level 19. Level 20, the last row, holds 200,000 again.
- The node menu shows `Lv. N/20` in game, so `ToClient_GetNodeMaxLevel()` returns 20 and the level 20 row is the cap; its 200,000 is never needed.
- The trailer is the one of [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md) and [fitnessmaxlevel](fitnessmaxlevel_bss.md).
