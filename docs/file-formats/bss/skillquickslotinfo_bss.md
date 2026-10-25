# `skillquickslotinfo.bss` Format

## Purpose

The skill each class has in its quick slots: one row per class type with
20 slots, each a skill number or empty. On client 3482 every class with
an entry fills slots 2 to 6 with five early skills (Warrior: Charging
Thrust I, Shield Charge I, Ground Slash I, Spinning Slash I, Scars of
Dusk).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records                  | Row bytes |
| ------ | -------------- | ------------------------ | ----- | ------------------------ | --------- |
| 1      | 1109 and later | `skillquickslotinfo.bss` | 7,776 | 1,940 Slot, 97 Class Row | 4         |

| Layout | File                     | Known           | Unknown         |
| ------ | ------------------------ | --------------- | --------------- |
| 1      | `skillquickslotinfo.bss` | 3,896 B (50.1%) | 3,880 B (49.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fa0e74e583fe`  |
| 3482   | Layout 1 | `fa0e74e583fe`  |
| 3474   | Layout 1 | `fa0e74e583fe`  |
| 3473   | Layout 1 | `fa0e74e583fe`  |
| 3464   | Layout 1 | `fa0e74e583fe`  |
| 3458   | Layout 1 | `fa0e74e583fe`  |
| 3454   | Layout 1 | `fa0e74e583fe`  |
| 3444   | Layout 1 | `fa0e74e583fe`  |
| 3435   | Layout 1 | `fa0e74e583fe`  |
| 3426   | Layout 1 | `fa0e74e583fe`  |
| 3418   | Layout 1 | `fa0e74e583fe`  |
| 3412   | Layout 1 | `fa0e74e583fe`  |
| 3402   | Layout 1 | `fa0e74e583fe`  |
| 3396   | Layout 1 | `fa0e74e583fe`  |
| 3387   | Layout 1 | `fa0e74e583fe`  |
| 3381   | Layout 1 | `fa0e74e583fe`  |
| 3373   | Layout 1 | `fa0e74e583fe`  |
| 3364   | Layout 1 | `fa0e74e583fe`  |
| 3356   | Layout 1 | `fa0e74e583fe`  |
| 3349   | Layout 1 | `fa0e74e583fe`  |
| 3342   | Layout 1 | `fa0e74e583fe`  |
| 3335   | Layout 1 | `fa0e74e583fe`  |
| 3326   | Layout 1 | `fa0e74e583fe`  |
| 3321   | Layout 1 | `fa0e74e583fe`  |
| 3314   | Layout 1 | `fa0e74e583fe`  |
| 3303   | Layout 1 | `fa0e74e583fe`  |
| 3302   | Layout 1 | `fa0e74e583fe`  |
| 3293   | Layout 1 | `fa0e74e583fe`  |
| 3283   | Layout 1 | `fa0e74e583fe`  |
| 3275   | Layout 1 | `fa0e74e583fe`  |
| 3267   | Layout 1 | `fa0e74e583fe`  |
| 3258   | Layout 1 | `fa0e74e583fe`  |
| 3251   | Layout 1 | `fa0e74e583fe`  |
| 3242   | Layout 1 | `fa0e74e583fe`  |
| 3235   | Layout 1 | `fa0e74e583fe`  |
| 3229   | Layout 1 | `fa0e74e583fe`  |
| 3212   | Layout 1 | `fa0e74e583fe`  |
| 3203   | Layout 1 | `fa0e74e583fe`  |
| 3193   | Layout 1 | `fa0e74e583fe`  |
| 3186   | Layout 1 | `fa0e74e583fe`  |
| 3177   | Layout 1 | `fa0e74e583fe`  |
| 3169   | Layout 1 | `fa0e74e583fe`  |
| 3158   | Layout 1 | `fa0e74e583fe`  |
| 3151   | Layout 1 | `fa0e74e583fe`  |
| 3144   | Layout 1 | `fa0e74e583fe`  |
| 3133   | Layout 1 | `fa0e74e583fe`  |
| 3125   | Layout 1 | `fa0e74e583fe`  |
| 3118   | Layout 1 | `fa0e74e583fe`  |
| 3111   | Layout 1 | `fa0e74e583fe`  |
| 3103   | Layout 1 | `fa0e74e583fe`  |
| 3095   | Layout 1 | `fa0e74e583fe`  |
| 3086   | Layout 1 | `fa0e74e583fe`  |
| 3072   | Layout 1 | `fa0e74e583fe`  |
| 3062   | Layout 1 | `fa0e74e583fe`  |
| 3052   | Layout 1 | `fa0e74e583fe`  |
| 3045   | Layout 1 | `fa0e74e583fe`  |
| 3037   | Layout 1 | `fa0e74e583fe`  |
| 3030   | Layout 1 | `fa0e74e583fe`  |
| 3021   | Layout 1 | `fa0e74e583fe`  |
| 3012   | Layout 1 | `fa0e74e583fe`  |
| 3002   | Layout 1 | `fa0e74e583fe`  |
| 2995   | Layout 1 | `fa0e74e583fe`  |
| 2987   | Layout 1 | `fa0e74e583fe`  |
| 2978   | Layout 1 | `fa0e74e583fe`  |
| 2970   | Layout 1 | `fa0e74e583fe`  |
| 2959   | Layout 1 | `fa0e74e583fe`  |
| 2951   | Layout 1 | `fa0e74e583fe`  |
| 2942   | Layout 1 | `fa0e74e583fe`  |
| 2935   | Layout 1 | `fa0e74e583fe`  |
| 2932   | Layout 1 | `fa0e74e583fe`  |
| 2923   | Layout 1 | `fa0e74e583fe`  |
| 2919   | Layout 1 | `fa0e74e583fe`  |
| 2907   | Layout 1 | `fa0e74e583fe`  |
| 2900   | Layout 1 | `fa0e74e583fe`  |
| 2891   | Layout 1 | `fa0e74e583fe`  |
| 2882   | Layout 1 | `fa0e74e583fe`  |
| 2872   | Layout 1 | `fa0e74e583fe`  |
| 2863   | Layout 1 | `fa0e74e583fe`  |
| 2855   | Layout 1 | `fa0e74e583fe`  |
| 2849   | Layout 1 | `fa0e74e583fe`  |
| 2844   | Layout 1 | `fa0e74e583fe`  |
| 2834   | Layout 1 | `fa0e74e583fe`  |
| 2825   | Layout 1 | `fa0e74e583fe`  |
| 2819   | Layout 1 | `fa0e74e583fe`  |
| 2811   | Layout 1 | `fa0e74e583fe`  |
| 2803   | Layout 1 | `fa0e74e583fe`  |
| 2794   | Layout 1 | `fa0e74e583fe`  |
| 2783   | Layout 1 | `fa0e74e583fe`  |
| 2774   | Layout 1 | `fa0e74e583fe`  |
| 2765   | Layout 1 | `fa0e74e583fe`  |
| 2756   | Layout 1 | `fa0e74e583fe`  |
| 2750   | Layout 1 | `fa0e74e583fe`  |
| 2743   | Layout 1 | `fa0e74e583fe`  |
| 2736   | Layout 1 | `fa0e74e583fe`  |
| 2726   | Layout 1 | `fa0e74e583fe`  |
| 2717   | Layout 1 | `fa0e74e583fe`  |
| 2709   | Layout 1 | `fa0e74e583fe`  |
| 2703   | Layout 1 | `fa0e74e583fe`  |
| 2695   | Layout 1 | `fa0e74e583fe`  |
| 2684   | Layout 1 | `fa0e74e583fe`  |
| 2672   | Layout 1 | `fa0e74e583fe`  |
| 2665   | Layout 1 | `fa0e74e583fe`  |
| 2657   | Layout 1 | `fa0e74e583fe`  |
| 2649   | Layout 1 | `fa0e74e583fe`  |
| 2644   | Layout 1 | `fa0e74e583fe`  |
| 2637   | Layout 1 | `fa0e74e583fe`  |
| 2629   | Layout 1 | `fa0e74e583fe`  |
| 2619   | Layout 1 | `fa0e74e583fe`  |
| 2612   | Layout 1 | `fa0e74e583fe`  |
| 2606   | Layout 1 | `fa0e74e583fe`  |
| 2602   | Layout 1 | `fa0e74e583fe`  |
| 2601   | Layout 1 | `fa0e74e583fe`  |
| 2592   | Layout 1 | `fa0e74e583fe`  |
| 2583   | Layout 1 | `fa0e74e583fe`  |
| 2575   | Layout 1 | `fa0e74e583fe`  |
| 2567   | Layout 1 | `fa0e74e583fe`  |
| 2560   | Layout 1 | `fa0e74e583fe`  |
| 2553   | Layout 1 | `fa0e74e583fe`  |
| 2545   | Layout 1 | `fa0e74e583fe`  |
| 2538   | Layout 1 | `fa0e74e583fe`  |
| 2529   | Layout 1 | `fa0e74e583fe`  |
| 2519   | Layout 1 | `fa0e74e583fe`  |
| 2513   | Layout 1 | `fa0e74e583fe`  |
| 2510   | Layout 1 | `fa0e74e583fe`  |
| 2507   | Layout 1 | `fa0e74e583fe`  |
| 2503   | Layout 1 | `fa0e74e583fe`  |
| 2498   | Layout 1 | `fa0e74e583fe`  |
| 2492   | Layout 1 | `fa0e74e583fe`  |
| 2487   | Layout 1 | `fa0e74e583fe`  |
| 2480   | Layout 1 | `fa0e74e583fe`  |
| 2474   | Layout 1 | `fa0e74e583fe`  |
| 2468   | Layout 1 | `fa0e74e583fe`  |
| 2460   | Layout 1 | `fa0e74e583fe`  |
| 2453   | Layout 1 | `fa0e74e583fe`  |
| 2444   | Layout 1 | `fa0e74e583fe`  |
| 2438   | Layout 1 | `fa0e74e583fe`  |
| 2434   | Layout 1 | `fa0e74e583fe`  |
| 2429   | Layout 1 | `fa0e74e583fe`  |
| 2421   | Layout 1 | `fa0e74e583fe`  |
| 2414   | Layout 1 | `fa0e74e583fe`  |
| 2407   | Layout 1 | `fa0e74e583fe`  |
| 2401   | Layout 1 | `fa0e74e583fe`  |
| 2397   | Layout 1 | `fa0e74e583fe`  |
| 2393   | Layout 1 | `fa0e74e583fe`  |
| 2384   | Layout 1 | `fa0e74e583fe`  |
| 2378   | Layout 1 | `fa0e74e583fe`  |
| 2372   | Layout 1 | `fa0e74e583fe`  |
| 2358   | Layout 1 | `fa0e74e583fe`  |
| 2352   | Layout 1 | `fa0e74e583fe`  |
| 2347   | Layout 1 | `fa0e74e583fe`  |
| 2343   | Layout 1 | `fa0e74e583fe`  |
| 2335   | Layout 1 | `fa0e74e583fe`  |
| 2327   | Layout 1 | `fa0e74e583fe`  |
| 2324   | Layout 1 | `fa0e74e583fe`  |
| 2319   | Layout 1 | `fa0e74e583fe`  |
| 2313   | Layout 1 | `fa0e74e583fe`  |
| 2308   | Layout 1 | `fa0e74e583fe`  |
| 2302   | Layout 1 | `fa0e74e583fe`  |
| 2295   | Layout 1 | `fa0e74e583fe`  |
| 2290   | Layout 1 | `fa0e74e583fe`  |
| 2284   | Layout 1 | `fa0e74e583fe`  |
| 2276   | Layout 1 | `fa0e74e583fe`  |
| 2269   | Layout 1 | `fa0e74e583fe`  |
| 2259   | Layout 1 | `fa0e74e583fe`  |
| 2250   | Layout 1 | `fa0e74e583fe`  |
| 2243   | Layout 1 | `fa0e74e583fe`  |
| 2235   | Layout 1 | `fa0e74e583fe`  |
| 2229   | Layout 1 | `fa0e74e583fe`  |
| 2224   | Layout 1 | `fa0e74e583fe`  |
| 2218   | Layout 1 | `fa0e74e583fe`  |
| 2215   | Layout 1 | `fa0e74e583fe`  |
| 2207   | Layout 1 | `fa0e74e583fe`  |
| 2203   | Layout 1 | `fa0e74e583fe`  |
| 2196   | Layout 1 | `fa0e74e583fe`  |
| 2192   | Layout 1 | `fa0e74e583fe`  |
| 2189   | Layout 1 | `fa0e74e583fe`  |
| 2183   | Layout 1 | `fa0e74e583fe`  |
| 2179   | Layout 1 | `fa0e74e583fe`  |
| 2171   | Layout 1 | `fa0e74e583fe`  |
| 2163   | Layout 1 | `fa0e74e583fe`  |
| 2156   | Layout 1 | `fa0e74e583fe`  |
| 2151   | Layout 1 | `fa0e74e583fe`  |
| 2147   | Layout 1 | `fa0e74e583fe`  |
| 2142   | Layout 1 | `fa0e74e583fe`  |
| 2138   | Layout 1 | `fa0e74e583fe`  |
| 2134   | Layout 1 | `fa0e74e583fe`  |
| 2130   | Layout 1 | `fa0e74e583fe`  |
| 2122   | Layout 1 | `fa0e74e583fe`  |
| 2107   | Layout 1 | `fa0e74e583fe`  |
| 2098   | Layout 1 | `fa0e74e583fe`  |
| 2089   | Layout 1 | `fa0e74e583fe`  |
| 2081   | Layout 1 | `fa0e74e583fe`  |
| 2073   | Layout 1 | `fa0e74e583fe`  |
| 2067   | Layout 1 | `fa0e74e583fe`  |
| 2063   | Layout 1 | `fa0e74e583fe`  |
| 2059   | Layout 1 | `fa0e74e583fe`  |
| 2052   | Layout 1 | `fa0e74e583fe`  |
| 2044   | Layout 1 | `fa0e74e583fe`  |
| 2039   | Layout 1 | `fa0e74e583fe`  |
| 2032   | Layout 1 | `fa0e74e583fe`  |
| 2025   | Layout 1 | `fa0e74e583fe`  |
| 2011   | Layout 1 | `fa0e74e583fe`  |
| 2005   | Layout 1 | `fa0e74e583fe`  |
| 2000   | Layout 1 | `fa0e74e583fe`  |
| 1996   | Layout 1 | `fa0e74e583fe`  |
| 1991   | Layout 1 | `fa0e74e583fe`  |
| 1985   | Layout 1 | `fa0e74e583fe`  |
| 1980   | Layout 1 | `fa0e74e583fe`  |
| 1969   | Layout 1 | `fa0e74e583fe`  |
| 1964   | Layout 1 | `fa0e74e583fe`  |
| 1958   | Layout 1 | `fa0e74e583fe`  |
| 1950   | Layout 1 | `fa0e74e583fe`  |
| 1945   | Layout 1 | `fa0e74e583fe`  |
| 1937   | Layout 1 | `fa0e74e583fe`  |
| 1933   | Layout 1 | `fa0e74e583fe`  |
| 1927   | Layout 1 | `fa0e74e583fe`  |
| 1921   | Layout 1 | `fa0e74e583fe`  |
| 1914   | Layout 1 | `fa0e74e583fe`  |
| 1908   | Layout 1 | `fa0e74e583fe`  |
| 1897   | Layout 1 | `fa0e74e583fe`  |
| 1892   | Layout 1 | `fa0e74e583fe`  |
| 1886   | Layout 1 | `fa0e74e583fe`  |
| 1881   | Layout 1 | `fa0e74e583fe`  |
| 1871   | Layout 1 | `fa0e74e583fe`  |
| 1866   | Layout 1 | `fa0e74e583fe`  |
| 1862   | Layout 1 | `fa0e74e583fe`  |
| 1854   | Layout 1 | `fa0e74e583fe`  |
| 1846   | Layout 1 | `fa0e74e583fe`  |
| 1838   | Layout 1 | `fa0e74e583fe`  |
| 1832   | Layout 1 | `fa0e74e583fe`  |
| 1826   | Layout 1 | `fa0e74e583fe`  |
| 1822   | Layout 1 | `fa0e74e583fe`  |
| 1818   | Layout 1 | `fa0e74e583fe`  |
| 1804   | Layout 1 | `fa0e74e583fe`  |
| 1794   | Layout 1 | `fa0e74e583fe`  |
| 1790   | Layout 1 | `fa0e74e583fe`  |
| 1784   | Layout 1 | `fa0e74e583fe`  |
| 1774   | Layout 1 | `fa0e74e583fe`  |
| 1771   | Layout 1 | `fa0e74e583fe`  |
| 1762   | Layout 1 | `fa0e74e583fe`  |
| 1759   | Layout 1 | `fa0e74e583fe`  |
| 1754   | Layout 1 | `fa0e74e583fe`  |
| 1749   | Layout 1 | `fa0e74e583fe`  |
| 1743   | Layout 1 | `fa0e74e583fe`  |
| 1737   | Layout 1 | `fa0e74e583fe`  |
| 1731   | Layout 1 | `fa0e74e583fe`  |
| 1725   | Layout 1 | `fa0e74e583fe`  |
| 1717   | Layout 1 | `fa0e74e583fe`  |
| 1710   | Layout 1 | `fa0e74e583fe`  |
| 1704   | Layout 1 | `fa0e74e583fe`  |
| 1698   | Layout 1 | `fa0e74e583fe`  |
| 1690   | Layout 1 | `fa0e74e583fe`  |
| 1685   | Layout 1 | `fa0e74e583fe`  |
| 1680   | Layout 1 | `fa0e74e583fe`  |
| 1674   | Layout 1 | `fa0e74e583fe`  |
| 1668   | Layout 1 | `fa0e74e583fe`  |
| 1659   | Layout 1 | `fa0e74e583fe`  |
| 1649   | Layout 1 | `fa0e74e583fe`  |
| 1642   | Layout 1 | `fa0e74e583fe`  |
| 1636   | Layout 1 | `fa0e74e583fe`  |
| 1628   | Layout 1 | `fa0e74e583fe`  |
| 1622   | Layout 1 | `fa0e74e583fe`  |
| 1614   | Layout 1 | `fa0e74e583fe`  |
| 1608   | Layout 1 | `fa0e74e583fe`  |
| 1602   | Layout 1 | `fa0e74e583fe`  |
| 1598   | Layout 1 | `fa0e74e583fe`  |
| 1594   | Layout 1 | `fa0e74e583fe`  |
| 1590   | Layout 1 | `fa0e74e583fe`  |
| 1587   | Layout 1 | `fa0e74e583fe`  |
| 1584   | Layout 1 | `fa0e74e583fe`  |
| 1579   | Layout 1 | `fa0e74e583fe`  |
| 1572   | Layout 1 | `fa0e74e583fe`  |
| 1565   | Layout 1 | `fa0e74e583fe`  |
| 1559   | Layout 1 | `fa0e74e583fe`  |
| 1554   | Layout 1 | `fa0e74e583fe`  |
| 1547   | Layout 1 | `fa0e74e583fe`  |
| 1537   | Layout 1 | `fa0e74e583fe`  |
| 1529   | Layout 1 | `fa0e74e583fe`  |
| 1524   | Layout 1 | `fa0e74e583fe`  |
| 1519   | Layout 1 | `fa0e74e583fe`  |
| 1509   | Layout 1 | `fa0e74e583fe`  |
| 1506   | Layout 1 | `fa0e74e583fe`  |
| 1504   | Layout 1 | `fa0e74e583fe`  |
| 1500   | Layout 1 | `fa0e74e583fe`  |
| 1493   | Layout 1 | `fa0e74e583fe`  |
| 1489   | Layout 1 | `fa0e74e583fe`  |
| 1485   | Layout 1 | `fa0e74e583fe`  |
| 1481   | Layout 1 | `fa0e74e583fe`  |
| 1474   | Layout 1 | `fa0e74e583fe`  |
| 1466   | Layout 1 | `fa0e74e583fe`  |
| 1462   | Layout 1 | `fa0e74e583fe`  |
| 1459   | Layout 1 | `fa0e74e583fe`  |
| 1453   | Layout 1 | `fa0e74e583fe`  |
| 1450   | Layout 1 | `fa0e74e583fe`  |
| 1445   | Layout 1 | `fa0e74e583fe`  |
| 1439   | Layout 1 | `fa0e74e583fe`  |
| 1433   | Layout 1 | `fa0e74e583fe`  |
| 1430   | Layout 1 | `fa0e74e583fe`  |
| 1426   | Layout 1 | `fa0e74e583fe`  |
| 1421   | Layout 1 | `fa0e74e583fe`  |
| 1417   | Layout 1 | `fa0e74e583fe`  |
| 1416   | Layout 1 | `fa0e74e583fe`  |
| 1409   | Layout 1 | `fa0e74e583fe`  |
| 1405   | Layout 1 | `fa0e74e583fe`  |
| 1401   | Layout 1 | `fa0e74e583fe`  |
| 1396   | Layout 1 | `fa0e74e583fe`  |
| 1391   | Layout 1 | `fa0e74e583fe`  |
| 1390   | Layout 1 | `fa0e74e583fe`  |
| 1386   | Layout 1 | `fa0e74e583fe`  |
| 1381   | Layout 1 | `fa0e74e583fe`  |
| 1379   | Layout 1 | `fa0e74e583fe`  |
| 1372   | Layout 1 | `fa0e74e583fe`  |
| 1366   | Layout 1 | `fa0e74e583fe`  |
| 1364   | Layout 1 | `fa0e74e583fe`  |
| 1363   | Layout 1 | `fa0e74e583fe`  |
| 1360   | Layout 1 | `fa0e74e583fe`  |
| 1358   | Layout 1 | `fa0e74e583fe`  |
| 1355   | Layout 1 | `fa0e74e583fe`  |
| 1351   | Layout 1 | `fa0e74e583fe`  |
| 1348   | Layout 1 | `fa0e74e583fe`  |
| 1346   | Layout 1 | `fa0e74e583fe`  |
| 1341   | Layout 1 | `fa0e74e583fe`  |
| 1340   | Layout 1 | `fa0e74e583fe`  |
| 1338   | Layout 1 | `fa0e74e583fe`  |
| 1335   | Layout 1 | `fa0e74e583fe`  |
| 1333   | Layout 1 | `fa0e74e583fe`  |
| 1329   | Layout 1 | `fa0e74e583fe`  |
| 1327   | Layout 1 | `fa0e74e583fe`  |
| 1324   | Layout 1 | `fa0e74e583fe`  |
| 1321   | Layout 1 | `fa0e74e583fe`  |
| 1319   | Layout 1 | `fa0e74e583fe`  |
| 1318   | Layout 1 | `fa0e74e583fe`  |
| 1316   | Layout 1 | `fa0e74e583fe`  |
| 1313   | Layout 1 | `fa0e74e583fe`  |
| 1311   | Layout 1 | `fa0e74e583fe`  |
| 1309   | Layout 1 | `fa0e74e583fe`  |
| 1304   | Layout 1 | `fa0e74e583fe`  |
| 1292   | Layout 1 | `fa0e74e583fe`  |
| 1286   | Layout 1 | `fa0e74e583fe`  |
| 1280   | Layout 1 | `fa0e74e583fe`  |
| 1276   | Layout 1 | `fa0e74e583fe`  |
| 1267   | Layout 1 | `fa0e74e583fe`  |
| 1261   | Layout 1 | `fa0e74e583fe`  |
| 1256   | Layout 1 | `fa0e74e583fe`  |
| 1250   | Layout 1 | `fa0e74e583fe`  |
| 1246   | Layout 1 | `fa0e74e583fe`  |
| 1239   | Layout 1 | `fa0e74e583fe`  |
| 1230   | Layout 1 | `fa0e74e583fe`  |
| 1226   | Layout 1 | `fa0e74e583fe`  |
| 1220   | Layout 1 | `fa0e74e583fe`  |
| 1217   | Layout 1 | `fa0e74e583fe`  |
| 1211   | Layout 1 | `fa0e74e583fe`  |
| 1210   | Layout 1 | `fa0e74e583fe`  |
| 1208   | Layout 1 | `fa0e74e583fe`  |
| 1203   | Layout 1 | `fa0e74e583fe`  |
| 1197   | Layout 1 | `fa0e74e583fe`  |
| 1194   | Layout 1 | `fa0e74e583fe`  |
| 1192   | Layout 1 | `fa0e74e583fe`  |
| 1187   | Layout 1 | `fa0e74e583fe`  |
| 1183   | Layout 1 | `fa0e74e583fe`  |
| 1177   | Layout 1 | `fa0e74e583fe`  |
| 1173   | Layout 1 | `fa0e74e583fe`  |
| 1167   | Layout 1 | `fa0e74e583fe`  |
| 1164   | Layout 1 | `fa0e74e583fe`  |
| 1156   | Layout 1 | `fa0e74e583fe`  |
| 1149   | Layout 1 | `fa0e74e583fe`  |
| 1144   | Layout 1 | `fa0e74e583fe`  |
| 1137   | Layout 1 | `fa0e74e583fe`  |
| 1132   | Layout 1 | `fa0e74e583fe`  |
| 1127   | Layout 1 | `fa0e74e583fe`  |
| 1122   | Layout 1 | `fa0e74e583fe`  |
| 1118   | Layout 1 | `fa0e74e583fe`  |
| 1114   | Layout 1 | `fa0e74e583fe`  |
| 1109   | Layout 1 | `fa0e74e583fe`  |
| 1102   | No file  | `fa0e74e583fe`  |
| 1096   | No file  | `fa0e74e583fe`  |
| 1088   | No file  | `fa0e74e583fe`  |
| 1081   | No file  | `fa0e74e583fe`  |
| 1076   | No file  | `fa0e74e583fe`  |
| 1069   | No file  | `fa0e74e583fe`  |
| 1064   | No file  | `fa0e74e583fe`  |
| 1058   | No file  | `fa0e74e583fe`  |
| 1051   | No file  | `fa0e74e583fe`  |
| 1044   | No file  | `fa0e74e583fe`  |
| 1036   | No file  | `fa0e74e583fe`  |
| 1026   | No file  | `fa0e74e583fe`  |
| 1016   | No file  | `fa0e74e583fe`  |
| 1009   | No file  | `fa0e74e583fe`  |
| 1005   | No file  | `fa0e74e583fe`  |
| 1000   | No file  | `fa0e74e583fe`  |
| 998    | No file  | `fa0e74e583fe`  |
| 990    | No file  | `fa0e74e583fe`  |
| 979    | No file  | `fa0e74e583fe`  |
| 972    | No file  | `fa0e74e583fe`  |
| 963    | No file  | `fa0e74e583fe`  |
| 955    | No file  | `fa0e74e583fe`  |
| 946    | No file  | `fa0e74e583fe`  |
| 938    | No file  | `fa0e74e583fe`  |
| 927    | No file  | `fa0e74e583fe`  |
| 911    | No file  | `fa0e74e583fe`  |
| 904    | No file  | `fa0e74e583fe`  |
| 899    | No file  | `fa0e74e583fe`  |
| 894    | No file  | `fa0e74e583fe`  |
| 885    | No file  | `fa0e74e583fe`  |
| 879    | No file  | `fa0e74e583fe`  |
| 872    | No file  | `fa0e74e583fe`  |
| 864    | No file  | `fa0e74e583fe`  |
| 855    | No file  | `fa0e74e583fe`  |
| 853    | No file  | `fa0e74e583fe`  |
| 845    | No file  | `fa0e74e583fe`  |
| 837    | No file  | `fa0e74e583fe`  |
| 829    | No file  | `fa0e74e583fe`  |
| 822    | No file  | `fa0e74e583fe`  |
| 814    | No file  | `fa0e74e583fe`  |
| 805    | No file  | `fa0e74e583fe`  |
| 794    | No file  | `fa0e74e583fe`  |
| 787    | No file  | `fa0e74e583fe`  |
| 780    | No file  | `fa0e74e583fe`  |
| 771    | No file  | `fa0e74e583fe`  |
| 760    | No file  | `fa0e74e583fe`  |
| 748    | No file  | `fa0e74e583fe`  |
| 741    | No file  | `fa0e74e583fe`  |
| 736    | No file  | `fa0e74e583fe`  |
| 731    | No file  | `fa0e74e583fe`  |
| 723    | No file  | `fa0e74e583fe`  |
| 711    | No file  | `fa0e74e583fe`  |
| 707    | No file  | `fa0e74e583fe`  |
| 697    | No file  | `fa0e74e583fe`  |
| 689    | No file  | `fa0e74e583fe`  |
| 683    | No file  | `fa0e74e583fe`  |
| 678    | No file  | `fa0e74e583fe`  |
| 670    | No file  | `fa0e74e583fe`  |
| 661    | No file  | `fa0e74e583fe`  |
| 656    | No file  | `fa0e74e583fe`  |
| 652    | No file  | `fa0e74e583fe`  |
| 643    | No file  | `fa0e74e583fe`  |
| 637    | No file  | `fa0e74e583fe`  |
| 630    | No file  | `fa0e74e583fe`  |
| 627    | No file  | `fa0e74e583fe`  |
| 621    | No file  | `fa0e74e583fe`  |
| 617    | No file  | `fa0e74e583fe`  |
| 615    | No file  | `fa0e74e583fe`  |
| 606    | No file  | `fa0e74e583fe`  |
| 599    | No file  | `fa0e74e583fe`  |
| 592    | No file  | `fa0e74e583fe`  |
| 586    | No file  | `fa0e74e583fe`  |
| 577    | No file  | `fa0e74e583fe`  |
| 569    | No file  | `fa0e74e583fe`  |
| 561    | No file  | `fa0e74e583fe`  |
| 554    | No file  | `fa0e74e583fe`  |
| 542    | No file  | `fa0e74e583fe`  |
| 532    | No file  | `fa0e74e583fe`  |
| 531    | No file  | `fa0e74e583fe`  |
| 526    | No file  | `fa0e74e583fe`  |
| 521    | No file  | `fa0e74e583fe`  |
| 517    | No file  | `fa0e74e583fe`  |
| 510    | No file  | `fa0e74e583fe`  |
| 508    | No file  | `fa0e74e583fe`  |
| 504    | No file  | `fa0e74e583fe`  |
| 497    | No file  | `fa0e74e583fe`  |
| 491    | No file  | `fa0e74e583fe`  |
| 485    | No file  | `fa0e74e583fe`  |
| 478    | No file  | `fa0e74e583fe`  |
| 472    | No file  | `fa0e74e583fe`  |
| 466    | No file  | `fa0e74e583fe`  |
| 457    | No file  | `fa0e74e583fe`  |
| 452    | No file  | `fa0e74e583fe`  |
| 449    | No file  | `fa0e74e583fe`  |
| 435    | No file  | `fa0e74e583fe`  |

<!-- versions:end -->

## Companion Files

None. Class names come from LOC type 21 and skill names from LOC type 10.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                   | Field        | Notes                                                    |
| ------------------- | ---------------------- | ------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]                | magic        | `PABR`                                                   |
| `+0x04`             | Class Row[..table_start] | rows       | No row count: row `n` is class type `n`; 97 rows on client 3482, 82 on client 1784 |
| `rows+0x00`         | String Table           | string_table | See String Table                                         |
| `EOF-0x08`          | u32                    | table_start  | Offset of the string table, where `rows` ends            |
| `EOF-0x04`          | u32                    | zero         | Always `0`                                               |

### Class Row (80 bytes)

| Offset  | Type     | Field | Notes                                        |
| ------- | -------- | ----- | -------------------------------------------- |
| `+0x00` | Slot[20] | slots | Quick slots 0 to 19 in order; see Slot       |

### Slot (4 bytes)

| Offset  | Type | Field      | Notes                                                          |
| ------- | ---- | ---------- | -------------------------------------------------------------- |
| `+0x00` | u16  | skill_no   | Skill number, LOC type `10`; `0` in an empty slot              |
| `+0x02` | u16  | unknown_02 | `1` in every filled slot and `0` in every empty one (clients 1784 and 3482) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482                   |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `SkillQuickSlot_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `ClassType`, `SkillNo` and `SlotNo`, one
row per filled slot (a `ClassType` of `28, 31` fills Wizard and Witch). Read
with the row as `ClassType` and the slot as `SlotNo`, its 115 slots match
the 115 filled slots of the official client 1784 file on `SkillNo` (115 of
115) and all 115 of client 3482, which adds classes 6, 7, 15, 30, 33 and
35 (145 filled slots). The developer workbook of the same server
(`datasheet_skillquickslot.xlsm`) adds the note columns
`#PcLevel_ForLearning` (the level that learns the skill) and
`#SkillName`, and a memo that marks rows "expected to give a poor early
experience" for change.

The 2016 `gc::QuickSlot` is a `pa::Array` of 20 `value_type`, which is why
a row has 20 slots; its slot holds a `gc::SkillKey` (u32), an item key and
a position, not the 4 bytes here.

## Notes

- The other rows are all zero: on client 3482 rows 3, 13, 14, 18, 22, 32
  (Seraph), 34 and 36 to 96.
- The slot is a skill number with the `1` in the high half, the reverse of
  the skill key `skill_no << 16 | level` of `skill.dbss`. Whether
  `unknown_02` is the skill level is open.

## Open Questions

### When the Client Places These Skills

The workbook memo and `#PcLevel_ForLearning` point at the quick slots a new
character starts with, but no client Lua of client 3482 names the table.
Whether the skills go into the slots at creation or when the skill is
learned is open.

### What Fixes the Row Count

The file has 32 rows on client 1156, 82 on clients 1230 to 2107, 87 on
clients 2313 to 3251 and 97 from client 3474; `instancedungeonskillinfo.bss`
has the same count from client 1636 on, while `ui_skillgroup_*.bss` keeps
101 class slots. LOC type 21 names class types up to 100 on client 3482,
so the count is not the number of named class types.
