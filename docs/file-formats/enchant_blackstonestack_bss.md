# `enchant_blackstonestack.bss` Format

## Purpose

The items the Enhancement window takes in exchange for Enhancement Chance
(failstacks): one row per item with a list of steps, each step the item
count it costs and the Enhancement Chance it gives. On client 3483 the
three rows are Primordial Black Stone (+110 to +200), Black Stone (+5 to
+45) and Crystallized Despair (+50 to +100); the LOC type 0 descriptions
of Black Stone and Primordial Black Stone name the same ranges ("Exchange
a set amount to increase your Enhancement Chance in the Enhancement
window").

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes | Records         | Row bytes |
| ------ | -------------- | ----------------------------- | ----- | --------------- | --------- |
| 1      | 1649 and later | `enchant_blackstonestack.bss` | 456   | 25 Stack, 3 Row | 16        |

| Layout | File                          | Known          | Unknown    |
| ------ | ----------------------------- | -------------- | ---------- |
| 1      | `enchant_blackstonestack.bss` | 456 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `09faf74d02a9`  |
| 3482   | Layout 1 | `09faf74d02a9`  |
| 3474   | Layout 1 | `09faf74d02a9`  |
| 3473   | Layout 1 | `09faf74d02a9`  |
| 3464   | Layout 1 | `09faf74d02a9`  |
| 3458   | Layout 1 | `09faf74d02a9`  |
| 3454   | Layout 1 | `09faf74d02a9`  |
| 3444   | Layout 1 | `09faf74d02a9`  |
| 3435   | Layout 1 | `09faf74d02a9`  |
| 3426   | Layout 1 | `09faf74d02a9`  |
| 3418   | Layout 1 | `09faf74d02a9`  |
| 3412   | Layout 1 | `09faf74d02a9`  |
| 3402   | Layout 1 | `09faf74d02a9`  |
| 3396   | Layout 1 | `09faf74d02a9`  |
| 3387   | Layout 1 | `09faf74d02a9`  |
| 3381   | Layout 1 | `09faf74d02a9`  |
| 3373   | Layout 1 | `09faf74d02a9`  |
| 3364   | Layout 1 | `09faf74d02a9`  |
| 3356   | Layout 1 | `09faf74d02a9`  |
| 3349   | Layout 1 | `09faf74d02a9`  |
| 3342   | Layout 1 | `09faf74d02a9`  |
| 3335   | Layout 1 | `09faf74d02a9`  |
| 3326   | Layout 1 | `09faf74d02a9`  |
| 3321   | Layout 1 | `09faf74d02a9`  |
| 3314   | Layout 1 | `09faf74d02a9`  |
| 3303   | Layout 1 | `09faf74d02a9`  |
| 3302   | Layout 1 | `09faf74d02a9`  |
| 3293   | Layout 1 | `09faf74d02a9`  |
| 3283   | Layout 1 | `09faf74d02a9`  |
| 3275   | Layout 1 | `09faf74d02a9`  |
| 3267   | Layout 1 | `09faf74d02a9`  |
| 3258   | Layout 1 | `09faf74d02a9`  |
| 3251   | Layout 1 | `09faf74d02a9`  |
| 3242   | Layout 1 | `09faf74d02a9`  |
| 3235   | Layout 1 | `09faf74d02a9`  |
| 3229   | Layout 1 | `09faf74d02a9`  |
| 3212   | Layout 1 | `09faf74d02a9`  |
| 3203   | Layout 1 | `09faf74d02a9`  |
| 3193   | Layout 1 | `09faf74d02a9`  |
| 3186   | Layout 1 | `09faf74d02a9`  |
| 3177   | Layout 1 | `09faf74d02a9`  |
| 3169   | Layout 1 | `09faf74d02a9`  |
| 3158   | Layout 1 | `09faf74d02a9`  |
| 3151   | Layout 1 | `09faf74d02a9`  |
| 3144   | Layout 1 | `09faf74d02a9`  |
| 3133   | Layout 1 | `09faf74d02a9`  |
| 3125   | Layout 1 | `09faf74d02a9`  |
| 3118   | Layout 1 | `09faf74d02a9`  |
| 3111   | Layout 1 | `09faf74d02a9`  |
| 3103   | Layout 1 | `09faf74d02a9`  |
| 3095   | Layout 1 | `09faf74d02a9`  |
| 3086   | Layout 1 | `09faf74d02a9`  |
| 3072   | Layout 1 | `09faf74d02a9`  |
| 3062   | Layout 1 | `09faf74d02a9`  |
| 3052   | Layout 1 | `09faf74d02a9`  |
| 3045   | Layout 1 | `09faf74d02a9`  |
| 3037   | Layout 1 | `09faf74d02a9`  |
| 3030   | Layout 1 | `09faf74d02a9`  |
| 3021   | Layout 1 | `09faf74d02a9`  |
| 3012   | Layout 1 | `09faf74d02a9`  |
| 3002   | Layout 1 | `09faf74d02a9`  |
| 2995   | Layout 1 | `09faf74d02a9`  |
| 2987   | Layout 1 | `09faf74d02a9`  |
| 2978   | Layout 1 | `09faf74d02a9`  |
| 2970   | Layout 1 | `09faf74d02a9`  |
| 2959   | Layout 1 | `09faf74d02a9`  |
| 2951   | Layout 1 | `09faf74d02a9`  |
| 2942   | Layout 1 | `09faf74d02a9`  |
| 2935   | Layout 1 | `09faf74d02a9`  |
| 2932   | Layout 1 | `09faf74d02a9`  |
| 2923   | Layout 1 | `09faf74d02a9`  |
| 2919   | Layout 1 | `09faf74d02a9`  |
| 2907   | Layout 1 | `09faf74d02a9`  |
| 2900   | Layout 1 | `09faf74d02a9`  |
| 2891   | Layout 1 | `09faf74d02a9`  |
| 2882   | Layout 1 | `09faf74d02a9`  |
| 2872   | Layout 1 | `09faf74d02a9`  |
| 2863   | Layout 1 | `09faf74d02a9`  |
| 2855   | Layout 1 | `09faf74d02a9`  |
| 2849   | Layout 1 | `09faf74d02a9`  |
| 2844   | Layout 1 | `09faf74d02a9`  |
| 2834   | Layout 1 | `09faf74d02a9`  |
| 2825   | Layout 1 | `09faf74d02a9`  |
| 2819   | Layout 1 | `09faf74d02a9`  |
| 2811   | Layout 1 | `09faf74d02a9`  |
| 2803   | Layout 1 | `09faf74d02a9`  |
| 2794   | Layout 1 | `09faf74d02a9`  |
| 2783   | Layout 1 | `09faf74d02a9`  |
| 2774   | Layout 1 | `09faf74d02a9`  |
| 2765   | Layout 1 | `09faf74d02a9`  |
| 2756   | Layout 1 | `09faf74d02a9`  |
| 2750   | Layout 1 | `09faf74d02a9`  |
| 2743   | Layout 1 | `09faf74d02a9`  |
| 2736   | Layout 1 | `09faf74d02a9`  |
| 2726   | Layout 1 | `09faf74d02a9`  |
| 2717   | Layout 1 | `09faf74d02a9`  |
| 2709   | Layout 1 | `09faf74d02a9`  |
| 2703   | Layout 1 | `09faf74d02a9`  |
| 2695   | Layout 1 | `09faf74d02a9`  |
| 2684   | Layout 1 | `09faf74d02a9`  |
| 2672   | Layout 1 | `09faf74d02a9`  |
| 2665   | Layout 1 | `09faf74d02a9`  |
| 2657   | Layout 1 | `09faf74d02a9`  |
| 2649   | Layout 1 | `09faf74d02a9`  |
| 2644   | Layout 1 | `09faf74d02a9`  |
| 2637   | Layout 1 | `09faf74d02a9`  |
| 2629   | Layout 1 | `09faf74d02a9`  |
| 2619   | Layout 1 | `09faf74d02a9`  |
| 2612   | Layout 1 | `09faf74d02a9`  |
| 2606   | Layout 1 | `09faf74d02a9`  |
| 2602   | Layout 1 | `09faf74d02a9`  |
| 2601   | Layout 1 | `09faf74d02a9`  |
| 2592   | Layout 1 | `09faf74d02a9`  |
| 2583   | Layout 1 | `09faf74d02a9`  |
| 2575   | Layout 1 | `09faf74d02a9`  |
| 2567   | Layout 1 | `09faf74d02a9`  |
| 2560   | Layout 1 | `09faf74d02a9`  |
| 2553   | Layout 1 | `09faf74d02a9`  |
| 2545   | Layout 1 | `09faf74d02a9`  |
| 2538   | Layout 1 | `09faf74d02a9`  |
| 2529   | Layout 1 | `09faf74d02a9`  |
| 2519   | Layout 1 | `09faf74d02a9`  |
| 2513   | Layout 1 | `09faf74d02a9`  |
| 2510   | Layout 1 | `09faf74d02a9`  |
| 2507   | Layout 1 | `09faf74d02a9`  |
| 2503   | Layout 1 | `09faf74d02a9`  |
| 2498   | Layout 1 | `09faf74d02a9`  |
| 2492   | Layout 1 | `09faf74d02a9`  |
| 2487   | Layout 1 | `09faf74d02a9`  |
| 2480   | Layout 1 | `09faf74d02a9`  |
| 2474   | Layout 1 | `09faf74d02a9`  |
| 2468   | Layout 1 | `09faf74d02a9`  |
| 2460   | Layout 1 | `09faf74d02a9`  |
| 2453   | Layout 1 | `09faf74d02a9`  |
| 2444   | Layout 1 | `09faf74d02a9`  |
| 2438   | Layout 1 | `09faf74d02a9`  |
| 2434   | Layout 1 | `09faf74d02a9`  |
| 2429   | Layout 1 | `09faf74d02a9`  |
| 2421   | Layout 1 | `09faf74d02a9`  |
| 2414   | Layout 1 | `09faf74d02a9`  |
| 2407   | Layout 1 | `09faf74d02a9`  |
| 2401   | Layout 1 | `09faf74d02a9`  |
| 2397   | Layout 1 | `09faf74d02a9`  |
| 2393   | Layout 1 | `09faf74d02a9`  |
| 2384   | Layout 1 | `09faf74d02a9`  |
| 2378   | Layout 1 | `09faf74d02a9`  |
| 2372   | Layout 1 | `09faf74d02a9`  |
| 2358   | Layout 1 | `09faf74d02a9`  |
| 2352   | Layout 1 | `09faf74d02a9`  |
| 2347   | Layout 1 | `09faf74d02a9`  |
| 2343   | Layout 1 | `09faf74d02a9`  |
| 2335   | Layout 1 | `09faf74d02a9`  |
| 2327   | Layout 1 | `09faf74d02a9`  |
| 2324   | Layout 1 | `09faf74d02a9`  |
| 2319   | Layout 1 | `09faf74d02a9`  |
| 2313   | Layout 1 | `09faf74d02a9`  |
| 2308   | Layout 1 | `09faf74d02a9`  |
| 2302   | Layout 1 | `09faf74d02a9`  |
| 2295   | Layout 1 | `09faf74d02a9`  |
| 2290   | Layout 1 | `09faf74d02a9`  |
| 2284   | Layout 1 | `09faf74d02a9`  |
| 2276   | Layout 1 | `09faf74d02a9`  |
| 2269   | Layout 1 | `09faf74d02a9`  |
| 2259   | Layout 1 | `09faf74d02a9`  |
| 2250   | Layout 1 | `09faf74d02a9`  |
| 2243   | Layout 1 | `09faf74d02a9`  |
| 2235   | Layout 1 | `09faf74d02a9`  |
| 2229   | Layout 1 | `09faf74d02a9`  |
| 2224   | Layout 1 | `09faf74d02a9`  |
| 2218   | Layout 1 | `09faf74d02a9`  |
| 2215   | Layout 1 | `09faf74d02a9`  |
| 2207   | Layout 1 | `09faf74d02a9`  |
| 2203   | Layout 1 | `09faf74d02a9`  |
| 2196   | Layout 1 | `09faf74d02a9`  |
| 2192   | Layout 1 | `09faf74d02a9`  |
| 2189   | Layout 1 | `09faf74d02a9`  |
| 2183   | Layout 1 | `09faf74d02a9`  |
| 2179   | Layout 1 | `09faf74d02a9`  |
| 2171   | Layout 1 | `09faf74d02a9`  |
| 2163   | Layout 1 | `09faf74d02a9`  |
| 2156   | Layout 1 | `09faf74d02a9`  |
| 2151   | Layout 1 | `09faf74d02a9`  |
| 2147   | Layout 1 | `09faf74d02a9`  |
| 2142   | Layout 1 | `09faf74d02a9`  |
| 2138   | Layout 1 | `09faf74d02a9`  |
| 2134   | Layout 1 | `09faf74d02a9`  |
| 2130   | Layout 1 | `09faf74d02a9`  |
| 2122   | Layout 1 | `09faf74d02a9`  |
| 2107   | Layout 1 | `09faf74d02a9`  |
| 2098   | Layout 1 | `09faf74d02a9`  |
| 2089   | Layout 1 | `09faf74d02a9`  |
| 2081   | Layout 1 | `09faf74d02a9`  |
| 2073   | Layout 1 | `09faf74d02a9`  |
| 2067   | Layout 1 | `09faf74d02a9`  |
| 2063   | Layout 1 | `09faf74d02a9`  |
| 2059   | Layout 1 | `09faf74d02a9`  |
| 2052   | Layout 1 | `09faf74d02a9`  |
| 2044   | Layout 1 | `09faf74d02a9`  |
| 2039   | Layout 1 | `09faf74d02a9`  |
| 2032   | Layout 1 | `09faf74d02a9`  |
| 2025   | Layout 1 | `09faf74d02a9`  |
| 2011   | Layout 1 | `09faf74d02a9`  |
| 2005   | Layout 1 | `09faf74d02a9`  |
| 2000   | Layout 1 | `09faf74d02a9`  |
| 1996   | Layout 1 | `09faf74d02a9`  |
| 1991   | Layout 1 | `09faf74d02a9`  |
| 1985   | Layout 1 | `09faf74d02a9`  |
| 1980   | Layout 1 | `09faf74d02a9`  |
| 1969   | Layout 1 | `09faf74d02a9`  |
| 1964   | Layout 1 | `09faf74d02a9`  |
| 1958   | Layout 1 | `09faf74d02a9`  |
| 1950   | Layout 1 | `09faf74d02a9`  |
| 1945   | Layout 1 | `09faf74d02a9`  |
| 1937   | Layout 1 | `09faf74d02a9`  |
| 1933   | Layout 1 | `09faf74d02a9`  |
| 1927   | Layout 1 | `09faf74d02a9`  |
| 1921   | Layout 1 | `09faf74d02a9`  |
| 1914   | Layout 1 | `09faf74d02a9`  |
| 1908   | Layout 1 | `09faf74d02a9`  |
| 1897   | Layout 1 | `09faf74d02a9`  |
| 1892   | Layout 1 | `09faf74d02a9`  |
| 1886   | Layout 1 | `09faf74d02a9`  |
| 1881   | Layout 1 | `09faf74d02a9`  |
| 1871   | Layout 1 | `09faf74d02a9`  |
| 1866   | Layout 1 | `09faf74d02a9`  |
| 1862   | Layout 1 | `09faf74d02a9`  |
| 1854   | Layout 1 | `09faf74d02a9`  |
| 1846   | Layout 1 | `09faf74d02a9`  |
| 1838   | Layout 1 | `09faf74d02a9`  |
| 1832   | Layout 1 | `09faf74d02a9`  |
| 1826   | Layout 1 | `09faf74d02a9`  |
| 1822   | Layout 1 | `09faf74d02a9`  |
| 1818   | Layout 1 | `09faf74d02a9`  |
| 1804   | Layout 1 | `09faf74d02a9`  |
| 1794   | Layout 1 | `09faf74d02a9`  |
| 1790   | Layout 1 | `09faf74d02a9`  |
| 1784   | Layout 1 | `09faf74d02a9`  |
| 1774   | Layout 1 | `09faf74d02a9`  |
| 1771   | Layout 1 | `09faf74d02a9`  |
| 1762   | Layout 1 | `09faf74d02a9`  |
| 1759   | Layout 1 | `09faf74d02a9`  |
| 1754   | Layout 1 | `09faf74d02a9`  |
| 1749   | Layout 1 | `09faf74d02a9`  |
| 1743   | Layout 1 | `09faf74d02a9`  |
| 1737   | Layout 1 | `09faf74d02a9`  |
| 1731   | Layout 1 | `09faf74d02a9`  |
| 1725   | Layout 1 | `09faf74d02a9`  |
| 1717   | Layout 1 | `09faf74d02a9`  |
| 1710   | Layout 1 | `09faf74d02a9`  |
| 1704   | Layout 1 | `09faf74d02a9`  |
| 1698   | Layout 1 | `09faf74d02a9`  |
| 1690   | Layout 1 | `09faf74d02a9`  |
| 1685   | Layout 1 | `09faf74d02a9`  |
| 1680   | Layout 1 | `09faf74d02a9`  |
| 1674   | Layout 1 | `09faf74d02a9`  |
| 1668   | Layout 1 | `09faf74d02a9`  |
| 1659   | Layout 1 | `09faf74d02a9`  |
| 1649   | Layout 1 | `09faf74d02a9`  |
| 1642   | No file  | `09faf74d02a9`  |
| 1636   | No file  | `09faf74d02a9`  |
| 1628   | No file  | `09faf74d02a9`  |
| 1622   | No file  | `09faf74d02a9`  |
| 1614   | No file  | `09faf74d02a9`  |
| 1608   | No file  | `09faf74d02a9`  |
| 1602   | No file  | `09faf74d02a9`  |
| 1598   | No file  | `09faf74d02a9`  |
| 1594   | No file  | `09faf74d02a9`  |
| 1590   | No file  | `09faf74d02a9`  |
| 1587   | No file  | `09faf74d02a9`  |
| 1584   | No file  | `09faf74d02a9`  |
| 1579   | No file  | `09faf74d02a9`  |
| 1572   | No file  | `09faf74d02a9`  |
| 1565   | No file  | `09faf74d02a9`  |
| 1559   | No file  | `09faf74d02a9`  |
| 1554   | No file  | `09faf74d02a9`  |
| 1547   | No file  | `09faf74d02a9`  |
| 1537   | No file  | `09faf74d02a9`  |
| 1529   | No file  | `09faf74d02a9`  |
| 1524   | No file  | `09faf74d02a9`  |
| 1519   | No file  | `09faf74d02a9`  |
| 1509   | No file  | `09faf74d02a9`  |
| 1506   | No file  | `09faf74d02a9`  |
| 1504   | No file  | `09faf74d02a9`  |
| 1500   | No file  | `09faf74d02a9`  |
| 1493   | No file  | `09faf74d02a9`  |
| 1489   | No file  | `09faf74d02a9`  |
| 1485   | No file  | `09faf74d02a9`  |
| 1481   | No file  | `09faf74d02a9`  |
| 1474   | No file  | `09faf74d02a9`  |
| 1466   | No file  | `09faf74d02a9`  |
| 1462   | No file  | `09faf74d02a9`  |
| 1459   | No file  | `09faf74d02a9`  |
| 1453   | No file  | `09faf74d02a9`  |
| 1450   | No file  | `09faf74d02a9`  |
| 1445   | No file  | `09faf74d02a9`  |
| 1439   | No file  | `09faf74d02a9`  |
| 1433   | No file  | `09faf74d02a9`  |
| 1430   | No file  | `09faf74d02a9`  |
| 1426   | No file  | `09faf74d02a9`  |
| 1421   | No file  | `09faf74d02a9`  |
| 1417   | No file  | `09faf74d02a9`  |
| 1416   | No file  | `09faf74d02a9`  |
| 1409   | No file  | `09faf74d02a9`  |
| 1405   | No file  | `09faf74d02a9`  |
| 1401   | No file  | `09faf74d02a9`  |
| 1396   | No file  | `09faf74d02a9`  |
| 1391   | No file  | `09faf74d02a9`  |
| 1390   | No file  | `09faf74d02a9`  |
| 1386   | No file  | `09faf74d02a9`  |
| 1381   | No file  | `09faf74d02a9`  |
| 1379   | No file  | `09faf74d02a9`  |
| 1372   | No file  | `09faf74d02a9`  |
| 1366   | No file  | `09faf74d02a9`  |
| 1364   | No file  | `09faf74d02a9`  |
| 1363   | No file  | `09faf74d02a9`  |
| 1360   | No file  | `09faf74d02a9`  |
| 1358   | No file  | `09faf74d02a9`  |
| 1355   | No file  | `09faf74d02a9`  |
| 1351   | No file  | `09faf74d02a9`  |
| 1348   | No file  | `09faf74d02a9`  |
| 1346   | No file  | `09faf74d02a9`  |
| 1341   | No file  | `09faf74d02a9`  |
| 1340   | No file  | `09faf74d02a9`  |
| 1338   | No file  | `09faf74d02a9`  |
| 1335   | No file  | `09faf74d02a9`  |
| 1333   | No file  | `09faf74d02a9`  |
| 1329   | No file  | `09faf74d02a9`  |
| 1327   | No file  | `09faf74d02a9`  |
| 1324   | No file  | `09faf74d02a9`  |
| 1321   | No file  | `09faf74d02a9`  |
| 1319   | No file  | `09faf74d02a9`  |
| 1318   | No file  | `09faf74d02a9`  |
| 1316   | No file  | `09faf74d02a9`  |
| 1313   | No file  | `09faf74d02a9`  |
| 1311   | No file  | `09faf74d02a9`  |
| 1309   | No file  | `09faf74d02a9`  |
| 1304   | No file  | `09faf74d02a9`  |
| 1292   | No file  | `09faf74d02a9`  |
| 1286   | No file  | `09faf74d02a9`  |
| 1280   | No file  | `09faf74d02a9`  |
| 1276   | No file  | `09faf74d02a9`  |
| 1267   | No file  | `09faf74d02a9`  |
| 1261   | No file  | `09faf74d02a9`  |
| 1256   | No file  | `09faf74d02a9`  |
| 1250   | No file  | `09faf74d02a9`  |
| 1246   | No file  | `09faf74d02a9`  |
| 1239   | No file  | `09faf74d02a9`  |
| 1230   | No file  | `09faf74d02a9`  |
| 1226   | No file  | `09faf74d02a9`  |
| 1220   | No file  | `09faf74d02a9`  |
| 1217   | No file  | `09faf74d02a9`  |
| 1211   | No file  | `09faf74d02a9`  |
| 1210   | No file  | `09faf74d02a9`  |
| 1208   | No file  | `09faf74d02a9`  |
| 1203   | No file  | `09faf74d02a9`  |
| 1197   | No file  | `09faf74d02a9`  |
| 1194   | No file  | `09faf74d02a9`  |
| 1192   | No file  | `09faf74d02a9`  |
| 1187   | No file  | `09faf74d02a9`  |
| 1183   | No file  | `09faf74d02a9`  |
| 1177   | No file  | `09faf74d02a9`  |
| 1173   | No file  | `09faf74d02a9`  |
| 1167   | No file  | `09faf74d02a9`  |
| 1164   | No file  | `09faf74d02a9`  |
| 1156   | No file  | `09faf74d02a9`  |
| 1149   | No file  | `09faf74d02a9`  |
| 1144   | No file  | `09faf74d02a9`  |
| 1137   | No file  | `09faf74d02a9`  |
| 1132   | No file  | `09faf74d02a9`  |
| 1127   | No file  | `09faf74d02a9`  |
| 1122   | No file  | `09faf74d02a9`  |
| 1118   | No file  | `09faf74d02a9`  |
| 1114   | No file  | `09faf74d02a9`  |
| 1109   | No file  | `09faf74d02a9`  |
| 1102   | No file  | `09faf74d02a9`  |
| 1096   | No file  | `09faf74d02a9`  |
| 1088   | No file  | `09faf74d02a9`  |
| 1081   | No file  | `09faf74d02a9`  |
| 1076   | No file  | `09faf74d02a9`  |
| 1069   | No file  | `09faf74d02a9`  |
| 1064   | No file  | `09faf74d02a9`  |
| 1058   | No file  | `09faf74d02a9`  |
| 1051   | No file  | `09faf74d02a9`  |
| 1044   | No file  | `09faf74d02a9`  |
| 1036   | No file  | `09faf74d02a9`  |
| 1026   | No file  | `09faf74d02a9`  |
| 1016   | No file  | `09faf74d02a9`  |
| 1009   | No file  | `09faf74d02a9`  |
| 1005   | No file  | `09faf74d02a9`  |
| 1000   | No file  | `09faf74d02a9`  |
| 998    | No file  | `09faf74d02a9`  |
| 990    | No file  | `09faf74d02a9`  |
| 979    | No file  | `09faf74d02a9`  |
| 972    | No file  | `09faf74d02a9`  |
| 963    | No file  | `09faf74d02a9`  |
| 955    | No file  | `09faf74d02a9`  |
| 946    | No file  | `09faf74d02a9`  |
| 938    | No file  | `09faf74d02a9`  |
| 927    | No file  | `09faf74d02a9`  |
| 911    | No file  | `09faf74d02a9`  |
| 904    | No file  | `09faf74d02a9`  |
| 899    | No file  | `09faf74d02a9`  |
| 894    | No file  | `09faf74d02a9`  |
| 885    | No file  | `09faf74d02a9`  |
| 879    | No file  | `09faf74d02a9`  |
| 872    | No file  | `09faf74d02a9`  |
| 864    | No file  | `09faf74d02a9`  |
| 855    | No file  | `09faf74d02a9`  |
| 853    | No file  | `09faf74d02a9`  |
| 845    | No file  | `09faf74d02a9`  |
| 837    | No file  | `09faf74d02a9`  |
| 829    | No file  | `09faf74d02a9`  |
| 822    | No file  | `09faf74d02a9`  |
| 814    | No file  | `09faf74d02a9`  |
| 805    | No file  | `09faf74d02a9`  |
| 794    | No file  | `09faf74d02a9`  |
| 787    | No file  | `09faf74d02a9`  |
| 780    | No file  | `09faf74d02a9`  |
| 771    | No file  | `09faf74d02a9`  |
| 760    | No file  | `09faf74d02a9`  |
| 748    | No file  | `09faf74d02a9`  |
| 741    | No file  | `09faf74d02a9`  |
| 736    | No file  | `09faf74d02a9`  |
| 731    | No file  | `09faf74d02a9`  |
| 723    | No file  | `09faf74d02a9`  |
| 711    | No file  | `09faf74d02a9`  |
| 707    | No file  | `09faf74d02a9`  |
| 697    | No file  | `09faf74d02a9`  |
| 689    | No file  | `09faf74d02a9`  |
| 683    | No file  | `09faf74d02a9`  |
| 678    | No file  | `09faf74d02a9`  |
| 670    | No file  | `09faf74d02a9`  |
| 661    | No file  | `09faf74d02a9`  |
| 656    | No file  | `09faf74d02a9`  |
| 652    | No file  | `09faf74d02a9`  |
| 643    | No file  | `09faf74d02a9`  |
| 637    | No file  | `09faf74d02a9`  |
| 630    | No file  | `09faf74d02a9`  |
| 627    | No file  | `09faf74d02a9`  |
| 621    | No file  | `09faf74d02a9`  |
| 617    | No file  | `09faf74d02a9`  |
| 615    | No file  | `09faf74d02a9`  |
| 606    | No file  | `09faf74d02a9`  |
| 599    | No file  | `09faf74d02a9`  |
| 592    | No file  | `09faf74d02a9`  |
| 586    | No file  | `09faf74d02a9`  |
| 577    | No file  | `09faf74d02a9`  |
| 569    | No file  | `09faf74d02a9`  |
| 561    | No file  | `09faf74d02a9`  |
| 554    | No file  | `09faf74d02a9`  |
| 542    | No file  | `09faf74d02a9`  |
| 532    | No file  | `09faf74d02a9`  |
| 531    | No file  | `09faf74d02a9`  |
| 526    | No file  | `09faf74d02a9`  |
| 521    | No file  | `09faf74d02a9`  |
| 517    | No file  | `09faf74d02a9`  |
| 510    | No file  | `09faf74d02a9`  |
| 508    | No file  | `09faf74d02a9`  |
| 504    | No file  | `09faf74d02a9`  |
| 497    | No file  | `09faf74d02a9`  |
| 491    | No file  | `09faf74d02a9`  |
| 485    | No file  | `09faf74d02a9`  |
| 478    | No file  | `09faf74d02a9`  |
| 472    | No file  | `09faf74d02a9`  |
| 466    | No file  | `09faf74d02a9`  |
| 457    | No file  | `09faf74d02a9`  |
| 452    | No file  | `09faf74d02a9`  |
| 449    | No file  | `09faf74d02a9`  |
| 435    | No file  | `09faf74d02a9`  |

<!-- versions:end -->

## Companion Files

None. The handler names each item with LOC type 0 from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of items                               |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 12 bytes + stacks)

| Offset  | Type               | Field               | Notes                                              |
| ------- | ------------------ | ------------------- | -------------------------------------------------- |
| `+0x00` | u32                | need_stack_item_key | The item the steps consume (LOC type 0); unique per file |
| `+0x04` | u64                | stack_count         | Number of `stacks`                                 |
| `+0x0C` | Stack[stack_count] | stacks              | See Stack; rising `stack` order                    |

### Stack (16 bytes)

| Offset  | Type     | Field                 | Notes                                                        |
| ------- | -------- | --------------------- | ------------------------------------------------------------ |
| `+0x00` | u64      | need_stack_item_count | Count of `need_stack_item_key` the step costs                |
| `+0x08` | u32      | stack                 | Enhancement Chance the step gives                            |
| `+0x0C` | bytes[4] | padding_0c            | Alignment of the entry to 8 bytes; see Notes                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Stacks

The rows of client 3483, in file order.

| `need_stack_item_key` | Item                  | Steps (`need_stack_item_count`: `stack`)                                    |
| --------------------- | --------------------- | --------------------------------------------------------------------------- |
| 820934                | Primordial Black Stone | 25: 110, 35: 120, 45: 130, 60: 140, 75: 150, 90: 160, 105: 170, 125: 180, 145: 190, 170: 200 |
| 16001                 | Black Stone           | 5: 5, 12: 10, 21: 15, 33: 20, 53: 25, 84: 30, 136: 35, 230: 40, 406: 45     |
| 8411                  | Crystallized Despair  | 4: 50, 8: 60, 15: 70, 25: 80, 35: 90, 50: 100                               |

Client 1784 has two rows, `16002` and `16001`, each with the six steps from
5: 5 to 84: 30.

## Field Names

The names follow the `Enchant_BlackStoneStack` sheet of a private server's
`DataSheets.bexcel` on client 1784: columns `NeedStackItemkey`,
`NeedStackItemCount` and `Stack`, 12 rows. Every step of the client 1784
file matches a sheet row on all three columns (12 of 12: six steps each for
`16001` and `16002`). The sheet has one row per step; the file groups the
steps of one item into a row.

## Notes

- `padding_0c` is the alignment gap of an in-memory entry (u64 count, u32
  stack, then 4 bytes up to the 16-byte size). The official files hold
  left-over bytes there: `b5 02 00 00` on most steps of client 3483, `00 00
  00 00`, `ce 00 00 00` and `b4 02 00 00` on the first step of each row,
  and `84 00 00 00` on client 1784. The same sheet rows compiled by the
  private server's tools on client 1784 write `00 00 00 00` on every step.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/enchantshop_tables.py`:
  the item with its icon and LOC name, then each step as item count and
  Enhancement Chance.
