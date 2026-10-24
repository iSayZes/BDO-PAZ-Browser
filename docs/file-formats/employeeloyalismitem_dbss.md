# `employeeloyalismitem.dbss` Format

## Purpose

Items that restore a sailor's condition. The file names and the client code call sailors "employees" and their condition "loyalism" or "loyalty" (`충성도` in the sheet comments); the English client text says "Sailor Condition". Each row is one item, whether it restores condition points or cures a sick sailor, and how much it restores. The sailor management window at a Wharf Manager lists these items when you restore a sailor. Companion `employeeloyalismitemoffset.dbss` lists where every row sits.

On client 3474 the file has 4 rows: Chowder (`+100` condition), Raisin Bread (`+1`), Elixir of Regeneration and Tears of the Star (cure a sick sailor, condition to 100%).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------ | --------- |
| 1      | 1267 and later | 3483    | `employeeloyalismitem.dbss`       | 40    | 4 Row        | 9         |
| 1      | 1267 and later | 3483    | `employeeloyalismitemoffset.dbss` | 52    | 4 Offset Row | 12        |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `employeeloyalismitem.dbss`       | 40 B (100.0%) | 0 B (0.0%) |
| 1      | `employeeloyalismitemoffset.dbss` | 52 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `244d44dd3f24`  |
| 3482   | Layout 1 | `244d44dd3f24`  |
| 3474   | Layout 1 | `244d44dd3f24`  |
| 3473   | Layout 1 | `244d44dd3f24`  |
| 3464   | Layout 1 | `244d44dd3f24`  |
| 3458   | Layout 1 | `244d44dd3f24`  |
| 3454   | Layout 1 | `244d44dd3f24`  |
| 3444   | Layout 1 | `244d44dd3f24`  |
| 3435   | Layout 1 | `244d44dd3f24`  |
| 3426   | Layout 1 | `244d44dd3f24`  |
| 3418   | Layout 1 | `244d44dd3f24`  |
| 3412   | Layout 1 | `244d44dd3f24`  |
| 3402   | Layout 1 | `244d44dd3f24`  |
| 3396   | Layout 1 | `244d44dd3f24`  |
| 3387   | Layout 1 | `244d44dd3f24`  |
| 3381   | Layout 1 | `244d44dd3f24`  |
| 3373   | Layout 1 | `244d44dd3f24`  |
| 3364   | Layout 1 | `244d44dd3f24`  |
| 3356   | Layout 1 | `244d44dd3f24`  |
| 3349   | Layout 1 | `244d44dd3f24`  |
| 3342   | Layout 1 | `244d44dd3f24`  |
| 3335   | Layout 1 | `244d44dd3f24`  |
| 3326   | Layout 1 | `244d44dd3f24`  |
| 3321   | Layout 1 | `244d44dd3f24`  |
| 3314   | Layout 1 | `244d44dd3f24`  |
| 3303   | Layout 1 | `244d44dd3f24`  |
| 3302   | Layout 1 | `244d44dd3f24`  |
| 3293   | Layout 1 | `244d44dd3f24`  |
| 3283   | Layout 1 | `244d44dd3f24`  |
| 3275   | Layout 1 | `244d44dd3f24`  |
| 3267   | Layout 1 | `244d44dd3f24`  |
| 3258   | Layout 1 | `244d44dd3f24`  |
| 3251   | Layout 1 | `244d44dd3f24`  |
| 3242   | Layout 1 | `244d44dd3f24`  |
| 3235   | Layout 1 | `244d44dd3f24`  |
| 3229   | Layout 1 | `244d44dd3f24`  |
| 3212   | Layout 1 | `244d44dd3f24`  |
| 3203   | Layout 1 | `244d44dd3f24`  |
| 3193   | Layout 1 | `244d44dd3f24`  |
| 3186   | Layout 1 | `244d44dd3f24`  |
| 3177   | Layout 1 | `244d44dd3f24`  |
| 3169   | Layout 1 | `244d44dd3f24`  |
| 3158   | Layout 1 | `244d44dd3f24`  |
| 3151   | Layout 1 | `244d44dd3f24`  |
| 3144   | Layout 1 | `244d44dd3f24`  |
| 3133   | Layout 1 | `244d44dd3f24`  |
| 3125   | Layout 1 | `244d44dd3f24`  |
| 3118   | Layout 1 | `244d44dd3f24`  |
| 3111   | Layout 1 | `244d44dd3f24`  |
| 3103   | Layout 1 | `244d44dd3f24`  |
| 3095   | Layout 1 | `244d44dd3f24`  |
| 3086   | Layout 1 | `244d44dd3f24`  |
| 3072   | Layout 1 | `244d44dd3f24`  |
| 3062   | Layout 1 | `244d44dd3f24`  |
| 3052   | Layout 1 | `244d44dd3f24`  |
| 3045   | Layout 1 | `244d44dd3f24`  |
| 3037   | Layout 1 | `244d44dd3f24`  |
| 3030   | Layout 1 | `244d44dd3f24`  |
| 3021   | Layout 1 | `244d44dd3f24`  |
| 3012   | Layout 1 | `244d44dd3f24`  |
| 3002   | Layout 1 | `244d44dd3f24`  |
| 2995   | Layout 1 | `244d44dd3f24`  |
| 2987   | Layout 1 | `244d44dd3f24`  |
| 2978   | Layout 1 | `244d44dd3f24`  |
| 2970   | Layout 1 | `244d44dd3f24`  |
| 2959   | Layout 1 | `244d44dd3f24`  |
| 2951   | Layout 1 | `244d44dd3f24`  |
| 2942   | Layout 1 | `244d44dd3f24`  |
| 2935   | Layout 1 | `244d44dd3f24`  |
| 2932   | Layout 1 | `244d44dd3f24`  |
| 2923   | Layout 1 | `244d44dd3f24`  |
| 2919   | Layout 1 | `244d44dd3f24`  |
| 2907   | Layout 1 | `244d44dd3f24`  |
| 2900   | Layout 1 | `244d44dd3f24`  |
| 2891   | Layout 1 | `244d44dd3f24`  |
| 2882   | Layout 1 | `244d44dd3f24`  |
| 2872   | Layout 1 | `244d44dd3f24`  |
| 2863   | Layout 1 | `244d44dd3f24`  |
| 2855   | Layout 1 | `244d44dd3f24`  |
| 2849   | Layout 1 | `244d44dd3f24`  |
| 2844   | Layout 1 | `244d44dd3f24`  |
| 2834   | Layout 1 | `244d44dd3f24`  |
| 2825   | Layout 1 | `244d44dd3f24`  |
| 2819   | Layout 1 | `244d44dd3f24`  |
| 2811   | Layout 1 | `244d44dd3f24`  |
| 2803   | Layout 1 | `244d44dd3f24`  |
| 2794   | Layout 1 | `244d44dd3f24`  |
| 2783   | Layout 1 | `244d44dd3f24`  |
| 2774   | Layout 1 | `244d44dd3f24`  |
| 2765   | Layout 1 | `244d44dd3f24`  |
| 2756   | Layout 1 | `244d44dd3f24`  |
| 2750   | Layout 1 | `244d44dd3f24`  |
| 2743   | Layout 1 | `244d44dd3f24`  |
| 2736   | Layout 1 | `244d44dd3f24`  |
| 2726   | Layout 1 | `244d44dd3f24`  |
| 2717   | Layout 1 | `244d44dd3f24`  |
| 2709   | Layout 1 | `244d44dd3f24`  |
| 2703   | Layout 1 | `244d44dd3f24`  |
| 2695   | Layout 1 | `244d44dd3f24`  |
| 2684   | Layout 1 | `244d44dd3f24`  |
| 2672   | Layout 1 | `244d44dd3f24`  |
| 2665   | Layout 1 | `244d44dd3f24`  |
| 2657   | Layout 1 | `244d44dd3f24`  |
| 2649   | Layout 1 | `244d44dd3f24`  |
| 2644   | Layout 1 | `244d44dd3f24`  |
| 2637   | Layout 1 | `244d44dd3f24`  |
| 2629   | Layout 1 | `244d44dd3f24`  |
| 2619   | Layout 1 | `244d44dd3f24`  |
| 2612   | Layout 1 | `244d44dd3f24`  |
| 2606   | Layout 1 | `244d44dd3f24`  |
| 2602   | Layout 1 | `244d44dd3f24`  |
| 2601   | Layout 1 | `244d44dd3f24`  |
| 2592   | Layout 1 | `244d44dd3f24`  |
| 2583   | Layout 1 | `244d44dd3f24`  |
| 2575   | Layout 1 | `244d44dd3f24`  |
| 2567   | Layout 1 | `244d44dd3f24`  |
| 2560   | Layout 1 | `244d44dd3f24`  |
| 2553   | Layout 1 | `244d44dd3f24`  |
| 2545   | Layout 1 | `244d44dd3f24`  |
| 2538   | Layout 1 | `244d44dd3f24`  |
| 2529   | Layout 1 | `244d44dd3f24`  |
| 2519   | Layout 1 | `244d44dd3f24`  |
| 2513   | Layout 1 | `244d44dd3f24`  |
| 2510   | Layout 1 | `244d44dd3f24`  |
| 2507   | Layout 1 | `244d44dd3f24`  |
| 2503   | Layout 1 | `244d44dd3f24`  |
| 2498   | Layout 1 | `244d44dd3f24`  |
| 2492   | Layout 1 | `244d44dd3f24`  |
| 2487   | Layout 1 | `244d44dd3f24`  |
| 2480   | Layout 1 | `244d44dd3f24`  |
| 2474   | Layout 1 | `244d44dd3f24`  |
| 2468   | Layout 1 | `244d44dd3f24`  |
| 2460   | Layout 1 | `244d44dd3f24`  |
| 2453   | Layout 1 | `244d44dd3f24`  |
| 2444   | Layout 1 | `244d44dd3f24`  |
| 2438   | Layout 1 | `244d44dd3f24`  |
| 2434   | Layout 1 | `244d44dd3f24`  |
| 2429   | Layout 1 | `244d44dd3f24`  |
| 2421   | Layout 1 | `244d44dd3f24`  |
| 2414   | Layout 1 | `244d44dd3f24`  |
| 2407   | Layout 1 | `244d44dd3f24`  |
| 2401   | Layout 1 | `244d44dd3f24`  |
| 2397   | Layout 1 | `244d44dd3f24`  |
| 2393   | Layout 1 | `244d44dd3f24`  |
| 2384   | Layout 1 | `244d44dd3f24`  |
| 2378   | Layout 1 | `244d44dd3f24`  |
| 2372   | Layout 1 | `244d44dd3f24`  |
| 2358   | Layout 1 | `244d44dd3f24`  |
| 2352   | Layout 1 | `244d44dd3f24`  |
| 2347   | Layout 1 | `244d44dd3f24`  |
| 2343   | Layout 1 | `244d44dd3f24`  |
| 2335   | Layout 1 | `244d44dd3f24`  |
| 2327   | Layout 1 | `244d44dd3f24`  |
| 2324   | Layout 1 | `244d44dd3f24`  |
| 2319   | Layout 1 | `244d44dd3f24`  |
| 2313   | Layout 1 | `244d44dd3f24`  |
| 2308   | Layout 1 | `244d44dd3f24`  |
| 2302   | Layout 1 | `244d44dd3f24`  |
| 2295   | Layout 1 | `244d44dd3f24`  |
| 2290   | Layout 1 | `244d44dd3f24`  |
| 2284   | Layout 1 | `244d44dd3f24`  |
| 2276   | Layout 1 | `244d44dd3f24`  |
| 2269   | Layout 1 | `244d44dd3f24`  |
| 2259   | Layout 1 | `244d44dd3f24`  |
| 2250   | Layout 1 | `244d44dd3f24`  |
| 2243   | Layout 1 | `244d44dd3f24`  |
| 2235   | Layout 1 | `244d44dd3f24`  |
| 2229   | Layout 1 | `244d44dd3f24`  |
| 2224   | Layout 1 | `244d44dd3f24`  |
| 2218   | Layout 1 | `244d44dd3f24`  |
| 2215   | Layout 1 | `244d44dd3f24`  |
| 2207   | Layout 1 | `244d44dd3f24`  |
| 2203   | Layout 1 | `244d44dd3f24`  |
| 2196   | Layout 1 | `244d44dd3f24`  |
| 2192   | Layout 1 | `244d44dd3f24`  |
| 2189   | Layout 1 | `244d44dd3f24`  |
| 2183   | Layout 1 | `244d44dd3f24`  |
| 2179   | Layout 1 | `244d44dd3f24`  |
| 2171   | Layout 1 | `244d44dd3f24`  |
| 2163   | Layout 1 | `244d44dd3f24`  |
| 2156   | Layout 1 | `244d44dd3f24`  |
| 2151   | Layout 1 | `244d44dd3f24`  |
| 2147   | Layout 1 | `244d44dd3f24`  |
| 2142   | Layout 1 | `244d44dd3f24`  |
| 2138   | Layout 1 | `244d44dd3f24`  |
| 2134   | Layout 1 | `244d44dd3f24`  |
| 2130   | Layout 1 | `244d44dd3f24`  |
| 2122   | Layout 1 | `244d44dd3f24`  |
| 2107   | Layout 1 | `244d44dd3f24`  |
| 2098   | Layout 1 | `244d44dd3f24`  |
| 2089   | Layout 1 | `244d44dd3f24`  |
| 2081   | Layout 1 | `244d44dd3f24`  |
| 2073   | Layout 1 | `244d44dd3f24`  |
| 2067   | Layout 1 | `244d44dd3f24`  |
| 2063   | Layout 1 | `244d44dd3f24`  |
| 2059   | Layout 1 | `244d44dd3f24`  |
| 2052   | Layout 1 | `244d44dd3f24`  |
| 2044   | Layout 1 | `244d44dd3f24`  |
| 2039   | Layout 1 | `244d44dd3f24`  |
| 2032   | Layout 1 | `244d44dd3f24`  |
| 2025   | Layout 1 | `244d44dd3f24`  |
| 2011   | Layout 1 | `244d44dd3f24`  |
| 2005   | Layout 1 | `244d44dd3f24`  |
| 2000   | Layout 1 | `244d44dd3f24`  |
| 1996   | Layout 1 | `244d44dd3f24`  |
| 1991   | Layout 1 | `244d44dd3f24`  |
| 1985   | Layout 1 | `244d44dd3f24`  |
| 1980   | Layout 1 | `244d44dd3f24`  |
| 1969   | Layout 1 | `244d44dd3f24`  |
| 1964   | Layout 1 | `244d44dd3f24`  |
| 1958   | Layout 1 | `244d44dd3f24`  |
| 1950   | Layout 1 | `244d44dd3f24`  |
| 1945   | Layout 1 | `244d44dd3f24`  |
| 1937   | Layout 1 | `244d44dd3f24`  |
| 1933   | Layout 1 | `244d44dd3f24`  |
| 1927   | Layout 1 | `244d44dd3f24`  |
| 1921   | Layout 1 | `244d44dd3f24`  |
| 1914   | Layout 1 | `244d44dd3f24`  |
| 1908   | Layout 1 | `244d44dd3f24`  |
| 1897   | Layout 1 | `244d44dd3f24`  |
| 1892   | Layout 1 | `244d44dd3f24`  |
| 1886   | Layout 1 | `244d44dd3f24`  |
| 1881   | Layout 1 | `244d44dd3f24`  |
| 1871   | Layout 1 | `244d44dd3f24`  |
| 1866   | Layout 1 | `244d44dd3f24`  |
| 1862   | Layout 1 | `244d44dd3f24`  |
| 1854   | Layout 1 | `244d44dd3f24`  |
| 1846   | Layout 1 | `244d44dd3f24`  |
| 1838   | Layout 1 | `244d44dd3f24`  |
| 1832   | Layout 1 | `244d44dd3f24`  |
| 1826   | Layout 1 | `244d44dd3f24`  |
| 1822   | Layout 1 | `244d44dd3f24`  |
| 1818   | Layout 1 | `244d44dd3f24`  |
| 1804   | Layout 1 | `244d44dd3f24`  |
| 1794   | Layout 1 | `244d44dd3f24`  |
| 1790   | Layout 1 | `244d44dd3f24`  |
| 1784   | Layout 1 | `244d44dd3f24`  |
| 1774   | Layout 1 | `244d44dd3f24`  |
| 1771   | Layout 1 | `244d44dd3f24`  |
| 1762   | Layout 1 | `244d44dd3f24`  |
| 1759   | Layout 1 | `244d44dd3f24`  |
| 1754   | Layout 1 | `244d44dd3f24`  |
| 1749   | Layout 1 | `244d44dd3f24`  |
| 1743   | Layout 1 | `244d44dd3f24`  |
| 1737   | Layout 1 | `244d44dd3f24`  |
| 1731   | Layout 1 | `244d44dd3f24`  |
| 1725   | Layout 1 | `244d44dd3f24`  |
| 1717   | Layout 1 | `244d44dd3f24`  |
| 1710   | Layout 1 | `244d44dd3f24`  |
| 1704   | Layout 1 | `244d44dd3f24`  |
| 1698   | Layout 1 | `244d44dd3f24`  |
| 1690   | Layout 1 | `244d44dd3f24`  |
| 1685   | Layout 1 | `244d44dd3f24`  |
| 1680   | Layout 1 | `244d44dd3f24`  |
| 1674   | Layout 1 | `244d44dd3f24`  |
| 1668   | Layout 1 | `244d44dd3f24`  |
| 1659   | Layout 1 | `244d44dd3f24`  |
| 1649   | Layout 1 | `244d44dd3f24`  |
| 1642   | Layout 1 | `244d44dd3f24`  |
| 1636   | Layout 1 | `244d44dd3f24`  |
| 1628   | Layout 1 | `244d44dd3f24`  |
| 1622   | Layout 1 | `244d44dd3f24`  |
| 1614   | Layout 1 | `244d44dd3f24`  |
| 1608   | Layout 1 | `244d44dd3f24`  |
| 1602   | Layout 1 | `244d44dd3f24`  |
| 1598   | Layout 1 | `244d44dd3f24`  |
| 1594   | Layout 1 | `244d44dd3f24`  |
| 1590   | Layout 1 | `244d44dd3f24`  |
| 1587   | Layout 1 | `244d44dd3f24`  |
| 1584   | Layout 1 | `244d44dd3f24`  |
| 1579   | Layout 1 | `244d44dd3f24`  |
| 1572   | Layout 1 | `244d44dd3f24`  |
| 1565   | Layout 1 | `244d44dd3f24`  |
| 1559   | Layout 1 | `244d44dd3f24`  |
| 1554   | Layout 1 | `244d44dd3f24`  |
| 1547   | Layout 1 | `244d44dd3f24`  |
| 1537   | Layout 1 | `244d44dd3f24`  |
| 1529   | Layout 1 | `244d44dd3f24`  |
| 1524   | Layout 1 | `244d44dd3f24`  |
| 1519   | Layout 1 | `244d44dd3f24`  |
| 1509   | Layout 1 | `244d44dd3f24`  |
| 1506   | Layout 1 | `244d44dd3f24`  |
| 1504   | Layout 1 | `244d44dd3f24`  |
| 1500   | Layout 1 | `244d44dd3f24`  |
| 1493   | Layout 1 | `244d44dd3f24`  |
| 1489   | Layout 1 | `244d44dd3f24`  |
| 1485   | Layout 1 | `244d44dd3f24`  |
| 1481   | Layout 1 | `244d44dd3f24`  |
| 1474   | Layout 1 | `244d44dd3f24`  |
| 1466   | Layout 1 | `244d44dd3f24`  |
| 1462   | Layout 1 | `244d44dd3f24`  |
| 1459   | Layout 1 | `244d44dd3f24`  |
| 1453   | Layout 1 | `244d44dd3f24`  |
| 1450   | Layout 1 | `244d44dd3f24`  |
| 1445   | Layout 1 | `244d44dd3f24`  |
| 1439   | Layout 1 | `244d44dd3f24`  |
| 1433   | Layout 1 | `244d44dd3f24`  |
| 1430   | Layout 1 | `244d44dd3f24`  |
| 1426   | Layout 1 | `244d44dd3f24`  |
| 1421   | Layout 1 | `244d44dd3f24`  |
| 1417   | Layout 1 | `244d44dd3f24`  |
| 1416   | Layout 1 | `244d44dd3f24`  |
| 1409   | Layout 1 | `244d44dd3f24`  |
| 1405   | Layout 1 | `244d44dd3f24`  |
| 1401   | Layout 1 | `244d44dd3f24`  |
| 1396   | Layout 1 | `244d44dd3f24`  |
| 1391   | Layout 1 | `244d44dd3f24`  |
| 1390   | Layout 1 | `244d44dd3f24`  |
| 1386   | Layout 1 | `244d44dd3f24`  |
| 1381   | Layout 1 | `244d44dd3f24`  |
| 1379   | Layout 1 | `244d44dd3f24`  |
| 1372   | Layout 1 | `244d44dd3f24`  |
| 1366   | Layout 1 | `244d44dd3f24`  |
| 1364   | Layout 1 | `244d44dd3f24`  |
| 1363   | Layout 1 | `244d44dd3f24`  |
| 1360   | Layout 1 | `244d44dd3f24`  |
| 1358   | Layout 1 | `244d44dd3f24`  |
| 1355   | Layout 1 | `244d44dd3f24`  |
| 1351   | Layout 1 | `244d44dd3f24`  |
| 1348   | Layout 1 | `244d44dd3f24`  |
| 1346   | Layout 1 | `244d44dd3f24`  |
| 1341   | Layout 1 | `244d44dd3f24`  |
| 1340   | Layout 1 | `244d44dd3f24`  |
| 1338   | Layout 1 | `244d44dd3f24`  |
| 1335   | Layout 1 | `244d44dd3f24`  |
| 1333   | Layout 1 | `244d44dd3f24`  |
| 1329   | Layout 1 | `244d44dd3f24`  |
| 1327   | Layout 1 | `244d44dd3f24`  |
| 1324   | Layout 1 | `244d44dd3f24`  |
| 1321   | Layout 1 | `244d44dd3f24`  |
| 1319   | Layout 1 | `244d44dd3f24`  |
| 1318   | Layout 1 | `244d44dd3f24`  |
| 1316   | Layout 1 | `244d44dd3f24`  |
| 1313   | Layout 1 | `244d44dd3f24`  |
| 1311   | Layout 1 | `244d44dd3f24`  |
| 1309   | Layout 1 | `244d44dd3f24`  |
| 1304   | Layout 1 | `244d44dd3f24`  |
| 1292   | Layout 1 | `244d44dd3f24`  |
| 1286   | Layout 1 | `244d44dd3f24`  |
| 1280   | Layout 1 | `244d44dd3f24`  |
| 1276   | Layout 1 | `244d44dd3f24`  |
| 1267   | Layout 1 | `244d44dd3f24`  |
| 1261   | No file  | `244d44dd3f24`  |
| 1256   | No file  | `244d44dd3f24`  |
| 1250   | No file  | `244d44dd3f24`  |
| 1246   | No file  | `244d44dd3f24`  |
| 1239   | No file  | `244d44dd3f24`  |
| 1230   | No file  | `244d44dd3f24`  |
| 1226   | No file  | `244d44dd3f24`  |
| 1220   | No file  | `244d44dd3f24`  |
| 1217   | No file  | `244d44dd3f24`  |
| 1211   | No file  | `244d44dd3f24`  |
| 1210   | No file  | `244d44dd3f24`  |
| 1208   | No file  | `244d44dd3f24`  |
| 1203   | No file  | `244d44dd3f24`  |
| 1197   | No file  | `244d44dd3f24`  |
| 1194   | No file  | `244d44dd3f24`  |
| 1192   | No file  | `244d44dd3f24`  |
| 1187   | No file  | `244d44dd3f24`  |
| 1183   | No file  | `244d44dd3f24`  |
| 1177   | No file  | `244d44dd3f24`  |
| 1173   | No file  | `244d44dd3f24`  |
| 1167   | No file  | `244d44dd3f24`  |
| 1164   | No file  | `244d44dd3f24`  |
| 1156   | No file  | `244d44dd3f24`  |
| 1149   | No file  | `244d44dd3f24`  |
| 1144   | No file  | `244d44dd3f24`  |
| 1137   | No file  | `244d44dd3f24`  |
| 1132   | No file  | `244d44dd3f24`  |
| 1127   | No file  | `244d44dd3f24`  |
| 1122   | No file  | `244d44dd3f24`  |
| 1118   | No file  | `244d44dd3f24`  |
| 1114   | No file  | `244d44dd3f24`  |
| 1109   | No file  | `244d44dd3f24`  |
| 1102   | No file  | `244d44dd3f24`  |
| 1096   | No file  | `244d44dd3f24`  |
| 1088   | No file  | `244d44dd3f24`  |
| 1081   | No file  | `244d44dd3f24`  |
| 1076   | No file  | `244d44dd3f24`  |
| 1069   | No file  | `244d44dd3f24`  |
| 1064   | No file  | `244d44dd3f24`  |
| 1058   | No file  | `244d44dd3f24`  |
| 1051   | No file  | `244d44dd3f24`  |
| 1044   | No file  | `244d44dd3f24`  |
| 1036   | No file  | `244d44dd3f24`  |
| 1026   | No file  | `244d44dd3f24`  |
| 1016   | No file  | `244d44dd3f24`  |
| 1009   | No file  | `244d44dd3f24`  |
| 1005   | No file  | `244d44dd3f24`  |
| 1000   | No file  | `244d44dd3f24`  |
| 998    | No file  | `244d44dd3f24`  |
| 990    | No file  | `244d44dd3f24`  |
| 979    | No file  | `244d44dd3f24`  |
| 972    | No file  | `244d44dd3f24`  |
| 963    | No file  | `244d44dd3f24`  |
| 955    | No file  | `244d44dd3f24`  |
| 946    | No file  | `244d44dd3f24`  |
| 938    | No file  | `244d44dd3f24`  |
| 927    | No file  | `244d44dd3f24`  |
| 911    | No file  | `244d44dd3f24`  |
| 904    | No file  | `244d44dd3f24`  |
| 899    | No file  | `244d44dd3f24`  |
| 894    | No file  | `244d44dd3f24`  |
| 885    | No file  | `244d44dd3f24`  |
| 879    | No file  | `244d44dd3f24`  |
| 872    | No file  | `244d44dd3f24`  |
| 864    | No file  | `244d44dd3f24`  |
| 855    | No file  | `244d44dd3f24`  |
| 853    | No file  | `244d44dd3f24`  |
| 845    | No file  | `244d44dd3f24`  |
| 837    | No file  | `244d44dd3f24`  |
| 829    | No file  | `244d44dd3f24`  |
| 822    | No file  | `244d44dd3f24`  |
| 814    | No file  | `244d44dd3f24`  |
| 805    | No file  | `244d44dd3f24`  |
| 794    | No file  | `244d44dd3f24`  |
| 787    | No file  | `244d44dd3f24`  |
| 780    | No file  | `244d44dd3f24`  |
| 771    | No file  | `244d44dd3f24`  |
| 760    | No file  | `244d44dd3f24`  |
| 748    | No file  | `244d44dd3f24`  |
| 741    | No file  | `244d44dd3f24`  |
| 736    | No file  | `244d44dd3f24`  |
| 731    | No file  | `244d44dd3f24`  |
| 723    | No file  | `244d44dd3f24`  |
| 711    | No file  | `244d44dd3f24`  |
| 707    | No file  | `244d44dd3f24`  |
| 697    | No file  | `244d44dd3f24`  |
| 689    | No file  | `244d44dd3f24`  |
| 683    | No file  | `244d44dd3f24`  |
| 678    | No file  | `244d44dd3f24`  |
| 670    | No file  | `244d44dd3f24`  |
| 661    | No file  | `244d44dd3f24`  |
| 656    | No file  | `244d44dd3f24`  |
| 652    | No file  | `244d44dd3f24`  |
| 643    | No file  | `244d44dd3f24`  |
| 637    | No file  | `244d44dd3f24`  |
| 630    | No file  | `244d44dd3f24`  |
| 627    | No file  | `244d44dd3f24`  |
| 621    | No file  | `244d44dd3f24`  |
| 617    | No file  | `244d44dd3f24`  |
| 615    | No file  | `244d44dd3f24`  |
| 606    | No file  | `244d44dd3f24`  |
| 599    | No file  | `244d44dd3f24`  |
| 592    | No file  | `244d44dd3f24`  |
| 586    | No file  | `244d44dd3f24`  |
| 577    | No file  | `244d44dd3f24`  |
| 569    | No file  | `244d44dd3f24`  |
| 561    | No file  | `244d44dd3f24`  |
| 554    | No file  | `244d44dd3f24`  |
| 542    | No file  | `244d44dd3f24`  |
| 532    | No file  | `244d44dd3f24`  |
| 531    | No file  | `244d44dd3f24`  |
| 526    | No file  | `244d44dd3f24`  |
| 521    | No file  | `244d44dd3f24`  |
| 517    | No file  | `244d44dd3f24`  |
| 510    | No file  | `244d44dd3f24`  |
| 508    | No file  | `244d44dd3f24`  |
| 504    | No file  | `244d44dd3f24`  |
| 497    | No file  | `244d44dd3f24`  |
| 491    | No file  | `244d44dd3f24`  |
| 485    | No file  | `244d44dd3f24`  |
| 478    | No file  | `244d44dd3f24`  |
| 472    | No file  | `244d44dd3f24`  |
| 466    | No file  | `244d44dd3f24`  |
| 457    | No file  | `244d44dd3f24`  |
| 452    | No file  | `244d44dd3f24`  |
| 449    | No file  | `244d44dd3f24`  |
| 435    | No file  | `244d44dd3f24`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                           |
| --------------------------------- | -------- | ---------------------------------------------- |
| `employeeloyalismitemoffset.dbss` | Required | `item_id -> (offset, size)` of every row       |
| `languagedata_en.loc`             | Optional | Item names (LOC type 0, `str_id1` = `item_id`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                 |
| ------- | ---------- | ----- | --------------------- |
| `+0x00` | u32        | count | Number of rows        |
| `+0x04` | Row[count] | rows  | See Row               |

The rows fill the file exactly: 4 + 4 x 9 = 40 bytes on client 3474.

### Row (9 bytes)

| Offset  | Type | Field          | Notes                                                                        |
| ------- | ---- | -------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u8   | loyalism_type  | `0` restores condition points, `1` cures a sick sailor; see Loyalism Type    |
| `+0x01` | u32  | item_id        | The item used; row key                                                       |
| `+0x05` | u32  | recovery_value | Type `0`: condition points. Type `1`: rate on the 1,000,000 = 100% scale     |

### `employeeloyalismitemoffset.dbss`

Bare offset table into `employeeloyalismitem.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                             |
| ------- | ----------------- | ----- | ------------------------------------------------- |
| `+0x00` | u32               | count | Number of offset rows; equals the main file count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                    |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                      |
| ------- | ---- | ----------- | -------------------------------------------------------------------------- |
| `+0x00` | u32  | item_id     | Key of the row it points at                                                |
| `+0x04` | u32  | data_offset | Absolute byte offset in `employeeloyalismitem.dbss` of the row's first byte (`loyalism_type`) |
| `+0x08` | u32  | data_size   | Always 9                                                                   |

The offset points at `loyalism_type`, so the key the row repeats sits at `data_offset + 1`. The parser reads the main file through these rows and checks that every row holds the key of the offset row that points at it.

## Loyalism Type

`loyalism_type` is the client's `__eEmployeeLoyalismType`. The client Lua names its two members, and the developer comment on the sheet's `Type` column (see Field Names) gives the numbers: `0 : 일반 회복` ("normal recovery") and `1 : 탈주한 선원 회복` ("recovery of a deserted sailor").

| Value | Lua name                                | Effect                                                               |
| ----- | --------------------------------------- | -------------------------------------------------------------------- |
| 0     | `__eEmployeeLoyalismType_Loyalty`       | Adds `recovery_value` condition points                               |
| 1     | `__eEmployeeLoyalismType_resurrection`  | Cures a sick sailor and sets condition to `recovery_value` (a rate)  |

In `panel_window_sailormanager_all_1.luac` the Restore button of a sailor in the `__eEmployeeState_Escape` state opens the item list with `__eEmployeeLoyalismType_resurrection`, every other sailor with `__eEmployeeLoyalismType_Loyalty`. `panel_window_sailormanager_all_2.luac` shows the `+N` value (`ToClient_getRecoveryValue(type, itemKey)`) on the item slot only for `Loyalty`, and the bulk restore in `panel_window_sailormanager_all_4.luac` uses `Loyalty` and skips sailors in the escape state. The English client calls the escape state sick: "Sick sailors cannot recover their health."

## Field Names

The names follow the `Employee_Loyalism` sheet of a private server's `DataSheets.bexcel` on client 1784 (`Type`, `RecoveryItemKey`, `RecoveryCount`, in this order). Its 4 rows equal the 4 rows of the live file value by value (client 3474), and the client 1784 file is byte for byte the same as the client 3474 file.

| Column            | Field            | Developer comment (sheet in the private server's `DataSheet_EmployeeDataTable.xlsx`) |
| ----------------- | ---------------- | ------------------------------------------------------------------------------------- |
| `Type`            | `loyalism_type`  | `선원의 충성도 회복 타입` ("sailor condition recovery type"), see Loyalism Type        |
| `RecoveryItemKey` | `item_id`        | `선원 충성도 회복 아이템키 설정` ("sailor condition recovery item key")                |
| `RecoveryCount`   | `recovery_value` | `타입 0 : 절대값` ("type 0: absolute value"), `타입 1 : 10000 ~ 1000000입력하며, 1 (%)` ("type 1: enter 10000 to 1000000, 1%" per 10000) |

`recovery_value` keeps the meaning, not the sheet's word "count": the Lua reads it through `ToClient_getRecoveryValue`.

## Notes

- The item texts agree with the values (LOC type 0, `str_id4` 1, client 3474): Chowder (6394, `100`) "Recover 100 Sailor Condition", Raisin Bread (6398, `1`) "Recover 1 Sailor Condition", Elixir of Regeneration (6395, `1000000`) "Cures one sailor, Recovers condition to 100%", Tears of the Star (320083, `1000000`) "Recover 1 Sick Sailor, Recover Sailor Condition to 100%".
- The 2016 PDB has no `Loyalism` names; sailors came to the game later.
- `employeeloyalismitemetc.bss` (32 bytes, PABR) shares the stem but has its own layout, see [employeeloyalismitemetc](employeeloyalismitemetc_bss.md).
