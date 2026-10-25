# `variedprice.bss` Format

## Purpose

The Central Market price ranges. A PABR list of price ranges; each row
gives the range's first and last price, the price step inside the range
and two counts the market uses for listings in that range. On client 3482
it holds 23 ranges, from `0` to `499` silver up to `10,000,000,000,000`
silver and more, with a price step of `1` silver in the first range and
`100,000,000,000` in the last.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File              | Bytes | Records | Row bytes |
| ------ | -------------- | ----------------- | ----- | ------- | --------- |
| 2      | 1127 and later | `variedprice.bss` | 940   | 23 Row  | 40        |
| 1      | 1109 to 1122   | `variedprice.bss` | 756   | 23 Row  | 32        |

| Layout | File              | Known          | Unknown    |
| ------ | ----------------- | -------------- | ---------- |
| 2      | `variedprice.bss` | 940 B (100.0%) | 0 B (0.0%) |
| 1      | `variedprice.bss` | 756 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `2d14420a1247`  |
| 3482   | Layout 2 | `2d14420a1247`  |
| 3474   | Layout 2 | `2d14420a1247`  |
| 3473   | Layout 2 | `2d14420a1247`  |
| 3464   | Layout 2 | `2d14420a1247`  |
| 3458   | Layout 2 | `2d14420a1247`  |
| 3454   | Layout 2 | `2d14420a1247`  |
| 3444   | Layout 2 | `2d14420a1247`  |
| 3435   | Layout 2 | `2d14420a1247`  |
| 3426   | Layout 2 | `2d14420a1247`  |
| 3418   | Layout 2 | `2d14420a1247`  |
| 3412   | Layout 2 | `2d14420a1247`  |
| 3402   | Layout 2 | `2d14420a1247`  |
| 3396   | Layout 2 | `2d14420a1247`  |
| 3387   | Layout 2 | `2d14420a1247`  |
| 3381   | Layout 2 | `2d14420a1247`  |
| 3373   | Layout 2 | `2d14420a1247`  |
| 3364   | Layout 2 | `2d14420a1247`  |
| 3356   | Layout 2 | `2d14420a1247`  |
| 3349   | Layout 2 | `2d14420a1247`  |
| 3342   | Layout 2 | `2d14420a1247`  |
| 3335   | Layout 2 | `2d14420a1247`  |
| 3326   | Layout 2 | `2d14420a1247`  |
| 3321   | Layout 2 | `2d14420a1247`  |
| 3314   | Layout 2 | `2d14420a1247`  |
| 3303   | Layout 2 | `2d14420a1247`  |
| 3302   | Layout 2 | `2d14420a1247`  |
| 3293   | Layout 2 | `2d14420a1247`  |
| 3283   | Layout 2 | `2d14420a1247`  |
| 3275   | Layout 2 | `2d14420a1247`  |
| 3267   | Layout 2 | `2d14420a1247`  |
| 3258   | Layout 2 | `2d14420a1247`  |
| 3251   | Layout 2 | `2d14420a1247`  |
| 3242   | Layout 2 | `2d14420a1247`  |
| 3235   | Layout 2 | `2d14420a1247`  |
| 3229   | Layout 2 | `2d14420a1247`  |
| 3212   | Layout 2 | `2d14420a1247`  |
| 3203   | Layout 2 | `2d14420a1247`  |
| 3193   | Layout 2 | `2d14420a1247`  |
| 3186   | Layout 2 | `2d14420a1247`  |
| 3177   | Layout 2 | `2d14420a1247`  |
| 3169   | Layout 2 | `2d14420a1247`  |
| 3158   | Layout 2 | `2d14420a1247`  |
| 3151   | Layout 2 | `2d14420a1247`  |
| 3144   | Layout 2 | `2d14420a1247`  |
| 3133   | Layout 2 | `2d14420a1247`  |
| 3125   | Layout 2 | `2d14420a1247`  |
| 3118   | Layout 2 | `2d14420a1247`  |
| 3111   | Layout 2 | `2d14420a1247`  |
| 3103   | Layout 2 | `2d14420a1247`  |
| 3095   | Layout 2 | `2d14420a1247`  |
| 3086   | Layout 2 | `2d14420a1247`  |
| 3072   | Layout 2 | `2d14420a1247`  |
| 3062   | Layout 2 | `2d14420a1247`  |
| 3052   | Layout 2 | `2d14420a1247`  |
| 3045   | Layout 2 | `2d14420a1247`  |
| 3037   | Layout 2 | `2d14420a1247`  |
| 3030   | Layout 2 | `2d14420a1247`  |
| 3021   | Layout 2 | `2d14420a1247`  |
| 3012   | Layout 2 | `2d14420a1247`  |
| 3002   | Layout 2 | `2d14420a1247`  |
| 2995   | Layout 2 | `2d14420a1247`  |
| 2987   | Layout 2 | `2d14420a1247`  |
| 2978   | Layout 2 | `2d14420a1247`  |
| 2970   | Layout 2 | `2d14420a1247`  |
| 2959   | Layout 2 | `2d14420a1247`  |
| 2951   | Layout 2 | `2d14420a1247`  |
| 2942   | Layout 2 | `2d14420a1247`  |
| 2935   | Layout 2 | `2d14420a1247`  |
| 2932   | Layout 2 | `2d14420a1247`  |
| 2923   | Layout 2 | `2d14420a1247`  |
| 2919   | Layout 2 | `2d14420a1247`  |
| 2907   | Layout 2 | `2d14420a1247`  |
| 2900   | Layout 2 | `2d14420a1247`  |
| 2891   | Layout 2 | `2d14420a1247`  |
| 2882   | Layout 2 | `2d14420a1247`  |
| 2872   | Layout 2 | `2d14420a1247`  |
| 2863   | Layout 2 | `2d14420a1247`  |
| 2855   | Layout 2 | `2d14420a1247`  |
| 2849   | Layout 2 | `2d14420a1247`  |
| 2844   | Layout 2 | `2d14420a1247`  |
| 2834   | Layout 2 | `2d14420a1247`  |
| 2825   | Layout 2 | `2d14420a1247`  |
| 2819   | Layout 2 | `2d14420a1247`  |
| 2811   | Layout 2 | `2d14420a1247`  |
| 2803   | Layout 2 | `2d14420a1247`  |
| 2794   | Layout 2 | `2d14420a1247`  |
| 2783   | Layout 2 | `2d14420a1247`  |
| 2774   | Layout 2 | `2d14420a1247`  |
| 2765   | Layout 2 | `2d14420a1247`  |
| 2756   | Layout 2 | `2d14420a1247`  |
| 2750   | Layout 2 | `2d14420a1247`  |
| 2743   | Layout 2 | `2d14420a1247`  |
| 2736   | Layout 2 | `2d14420a1247`  |
| 2726   | Layout 2 | `2d14420a1247`  |
| 2717   | Layout 2 | `2d14420a1247`  |
| 2709   | Layout 2 | `2d14420a1247`  |
| 2703   | Layout 2 | `2d14420a1247`  |
| 2695   | Layout 2 | `2d14420a1247`  |
| 2684   | Layout 2 | `2d14420a1247`  |
| 2672   | Layout 2 | `2d14420a1247`  |
| 2665   | Layout 2 | `2d14420a1247`  |
| 2657   | Layout 2 | `2d14420a1247`  |
| 2649   | Layout 2 | `2d14420a1247`  |
| 2644   | Layout 2 | `2d14420a1247`  |
| 2637   | Layout 2 | `2d14420a1247`  |
| 2629   | Layout 2 | `2d14420a1247`  |
| 2619   | Layout 2 | `2d14420a1247`  |
| 2612   | Layout 2 | `2d14420a1247`  |
| 2606   | Layout 2 | `2d14420a1247`  |
| 2602   | Layout 2 | `2d14420a1247`  |
| 2601   | Layout 2 | `2d14420a1247`  |
| 2592   | Layout 2 | `2d14420a1247`  |
| 2583   | Layout 2 | `2d14420a1247`  |
| 2575   | Layout 2 | `2d14420a1247`  |
| 2567   | Layout 2 | `2d14420a1247`  |
| 2560   | Layout 2 | `2d14420a1247`  |
| 2553   | Layout 2 | `2d14420a1247`  |
| 2545   | Layout 2 | `2d14420a1247`  |
| 2538   | Layout 2 | `2d14420a1247`  |
| 2529   | Layout 2 | `2d14420a1247`  |
| 2519   | Layout 2 | `2d14420a1247`  |
| 2513   | Layout 2 | `2d14420a1247`  |
| 2510   | Layout 2 | `2d14420a1247`  |
| 2507   | Layout 2 | `2d14420a1247`  |
| 2503   | Layout 2 | `2d14420a1247`  |
| 2498   | Layout 2 | `2d14420a1247`  |
| 2492   | Layout 2 | `2d14420a1247`  |
| 2487   | Layout 2 | `2d14420a1247`  |
| 2480   | Layout 2 | `2d14420a1247`  |
| 2474   | Layout 2 | `2d14420a1247`  |
| 2468   | Layout 2 | `2d14420a1247`  |
| 2460   | Layout 2 | `2d14420a1247`  |
| 2453   | Layout 2 | `2d14420a1247`  |
| 2444   | Layout 2 | `2d14420a1247`  |
| 2438   | Layout 2 | `2d14420a1247`  |
| 2434   | Layout 2 | `2d14420a1247`  |
| 2429   | Layout 2 | `2d14420a1247`  |
| 2421   | Layout 2 | `2d14420a1247`  |
| 2414   | Layout 2 | `2d14420a1247`  |
| 2407   | Layout 2 | `2d14420a1247`  |
| 2401   | Layout 2 | `2d14420a1247`  |
| 2397   | Layout 2 | `2d14420a1247`  |
| 2393   | Layout 2 | `2d14420a1247`  |
| 2384   | Layout 2 | `2d14420a1247`  |
| 2378   | Layout 2 | `2d14420a1247`  |
| 2372   | Layout 2 | `2d14420a1247`  |
| 2358   | Layout 2 | `2d14420a1247`  |
| 2352   | Layout 2 | `2d14420a1247`  |
| 2347   | Layout 2 | `2d14420a1247`  |
| 2343   | Layout 2 | `2d14420a1247`  |
| 2335   | Layout 2 | `2d14420a1247`  |
| 2327   | Layout 2 | `2d14420a1247`  |
| 2324   | Layout 2 | `2d14420a1247`  |
| 2319   | Layout 2 | `2d14420a1247`  |
| 2313   | Layout 2 | `2d14420a1247`  |
| 2308   | Layout 2 | `2d14420a1247`  |
| 2302   | Layout 2 | `2d14420a1247`  |
| 2295   | Layout 2 | `2d14420a1247`  |
| 2290   | Layout 2 | `2d14420a1247`  |
| 2284   | Layout 2 | `2d14420a1247`  |
| 2276   | Layout 2 | `2d14420a1247`  |
| 2269   | Layout 2 | `2d14420a1247`  |
| 2259   | Layout 2 | `2d14420a1247`  |
| 2250   | Layout 2 | `2d14420a1247`  |
| 2243   | Layout 2 | `2d14420a1247`  |
| 2235   | Layout 2 | `2d14420a1247`  |
| 2229   | Layout 2 | `2d14420a1247`  |
| 2224   | Layout 2 | `2d14420a1247`  |
| 2218   | Layout 2 | `2d14420a1247`  |
| 2215   | Layout 2 | `2d14420a1247`  |
| 2207   | Layout 2 | `2d14420a1247`  |
| 2203   | Layout 2 | `2d14420a1247`  |
| 2196   | Layout 2 | `2d14420a1247`  |
| 2192   | Layout 2 | `2d14420a1247`  |
| 2189   | Layout 2 | `2d14420a1247`  |
| 2183   | Layout 2 | `2d14420a1247`  |
| 2179   | Layout 2 | `2d14420a1247`  |
| 2171   | Layout 2 | `2d14420a1247`  |
| 2163   | Layout 2 | `2d14420a1247`  |
| 2156   | Layout 2 | `2d14420a1247`  |
| 2151   | Layout 2 | `2d14420a1247`  |
| 2147   | Layout 2 | `2d14420a1247`  |
| 2142   | Layout 2 | `2d14420a1247`  |
| 2138   | Layout 2 | `2d14420a1247`  |
| 2134   | Layout 2 | `2d14420a1247`  |
| 2130   | Layout 2 | `2d14420a1247`  |
| 2122   | Layout 2 | `2d14420a1247`  |
| 2107   | Layout 2 | `2d14420a1247`  |
| 2098   | Layout 2 | `2d14420a1247`  |
| 2089   | Layout 2 | `2d14420a1247`  |
| 2081   | Layout 2 | `2d14420a1247`  |
| 2073   | Layout 2 | `2d14420a1247`  |
| 2067   | Layout 2 | `2d14420a1247`  |
| 2063   | Layout 2 | `2d14420a1247`  |
| 2059   | Layout 2 | `2d14420a1247`  |
| 2052   | Layout 2 | `2d14420a1247`  |
| 2044   | Layout 2 | `2d14420a1247`  |
| 2039   | Layout 2 | `2d14420a1247`  |
| 2032   | Layout 2 | `2d14420a1247`  |
| 2025   | Layout 2 | `2d14420a1247`  |
| 2011   | Layout 2 | `2d14420a1247`  |
| 2005   | Layout 2 | `2d14420a1247`  |
| 2000   | Layout 2 | `2d14420a1247`  |
| 1996   | Layout 2 | `2d14420a1247`  |
| 1991   | Layout 2 | `2d14420a1247`  |
| 1985   | Layout 2 | `2d14420a1247`  |
| 1980   | Layout 2 | `2d14420a1247`  |
| 1969   | Layout 2 | `2d14420a1247`  |
| 1964   | Layout 2 | `2d14420a1247`  |
| 1958   | Layout 2 | `2d14420a1247`  |
| 1950   | Layout 2 | `2d14420a1247`  |
| 1945   | Layout 2 | `2d14420a1247`  |
| 1937   | Layout 2 | `2d14420a1247`  |
| 1933   | Layout 2 | `2d14420a1247`  |
| 1927   | Layout 2 | `2d14420a1247`  |
| 1921   | Layout 2 | `2d14420a1247`  |
| 1914   | Layout 2 | `2d14420a1247`  |
| 1908   | Layout 2 | `2d14420a1247`  |
| 1897   | Layout 2 | `2d14420a1247`  |
| 1892   | Layout 2 | `2d14420a1247`  |
| 1886   | Layout 2 | `2d14420a1247`  |
| 1881   | Layout 2 | `2d14420a1247`  |
| 1871   | Layout 2 | `2d14420a1247`  |
| 1866   | Layout 2 | `2d14420a1247`  |
| 1862   | Layout 2 | `2d14420a1247`  |
| 1854   | Layout 2 | `2d14420a1247`  |
| 1846   | Layout 2 | `2d14420a1247`  |
| 1838   | Layout 2 | `2d14420a1247`  |
| 1832   | Layout 2 | `2d14420a1247`  |
| 1826   | Layout 2 | `2d14420a1247`  |
| 1822   | Layout 2 | `2d14420a1247`  |
| 1818   | Layout 2 | `2d14420a1247`  |
| 1804   | Layout 2 | `2d14420a1247`  |
| 1794   | Layout 2 | `2d14420a1247`  |
| 1790   | Layout 2 | `2d14420a1247`  |
| 1784   | Layout 2 | `2d14420a1247`  |
| 1774   | Layout 2 | `2d14420a1247`  |
| 1771   | Layout 2 | `2d14420a1247`  |
| 1762   | Layout 2 | `2d14420a1247`  |
| 1759   | Layout 2 | `2d14420a1247`  |
| 1754   | Layout 2 | `2d14420a1247`  |
| 1749   | Layout 2 | `2d14420a1247`  |
| 1743   | Layout 2 | `2d14420a1247`  |
| 1737   | Layout 2 | `2d14420a1247`  |
| 1731   | Layout 2 | `2d14420a1247`  |
| 1725   | Layout 2 | `2d14420a1247`  |
| 1717   | Layout 2 | `2d14420a1247`  |
| 1710   | Layout 2 | `2d14420a1247`  |
| 1704   | Layout 2 | `2d14420a1247`  |
| 1698   | Layout 2 | `2d14420a1247`  |
| 1690   | Layout 2 | `2d14420a1247`  |
| 1685   | Layout 2 | `2d14420a1247`  |
| 1680   | Layout 2 | `2d14420a1247`  |
| 1674   | Layout 2 | `2d14420a1247`  |
| 1668   | Layout 2 | `2d14420a1247`  |
| 1659   | Layout 2 | `2d14420a1247`  |
| 1649   | Layout 2 | `2d14420a1247`  |
| 1642   | Layout 2 | `2d14420a1247`  |
| 1636   | Layout 2 | `2d14420a1247`  |
| 1628   | Layout 2 | `2d14420a1247`  |
| 1622   | Layout 2 | `2d14420a1247`  |
| 1614   | Layout 2 | `2d14420a1247`  |
| 1608   | Layout 2 | `2d14420a1247`  |
| 1602   | Layout 2 | `2d14420a1247`  |
| 1598   | Layout 2 | `2d14420a1247`  |
| 1594   | Layout 2 | `2d14420a1247`  |
| 1590   | Layout 2 | `2d14420a1247`  |
| 1587   | Layout 2 | `2d14420a1247`  |
| 1584   | Layout 2 | `2d14420a1247`  |
| 1579   | Layout 2 | `2d14420a1247`  |
| 1572   | Layout 2 | `2d14420a1247`  |
| 1565   | Layout 2 | `2d14420a1247`  |
| 1559   | Layout 2 | `2d14420a1247`  |
| 1554   | Layout 2 | `2d14420a1247`  |
| 1547   | Layout 2 | `2d14420a1247`  |
| 1537   | Layout 2 | `2d14420a1247`  |
| 1529   | Layout 2 | `2d14420a1247`  |
| 1524   | Layout 2 | `2d14420a1247`  |
| 1519   | Layout 2 | `2d14420a1247`  |
| 1509   | Layout 2 | `2d14420a1247`  |
| 1506   | Layout 2 | `2d14420a1247`  |
| 1504   | Layout 2 | `2d14420a1247`  |
| 1500   | Layout 2 | `2d14420a1247`  |
| 1493   | Layout 2 | `2d14420a1247`  |
| 1489   | Layout 2 | `2d14420a1247`  |
| 1485   | Layout 2 | `2d14420a1247`  |
| 1481   | Layout 2 | `2d14420a1247`  |
| 1474   | Layout 2 | `2d14420a1247`  |
| 1466   | Layout 2 | `2d14420a1247`  |
| 1462   | Layout 2 | `2d14420a1247`  |
| 1459   | Layout 2 | `2d14420a1247`  |
| 1453   | Layout 2 | `2d14420a1247`  |
| 1450   | Layout 2 | `2d14420a1247`  |
| 1445   | Layout 2 | `2d14420a1247`  |
| 1439   | Layout 2 | `2d14420a1247`  |
| 1433   | Layout 2 | `2d14420a1247`  |
| 1430   | Layout 2 | `2d14420a1247`  |
| 1426   | Layout 2 | `2d14420a1247`  |
| 1421   | Layout 2 | `2d14420a1247`  |
| 1417   | Layout 2 | `2d14420a1247`  |
| 1416   | Layout 2 | `2d14420a1247`  |
| 1409   | Layout 2 | `2d14420a1247`  |
| 1405   | Layout 2 | `2d14420a1247`  |
| 1401   | Layout 2 | `2d14420a1247`  |
| 1396   | Layout 2 | `2d14420a1247`  |
| 1391   | Layout 2 | `2d14420a1247`  |
| 1390   | Layout 2 | `2d14420a1247`  |
| 1386   | Layout 2 | `2d14420a1247`  |
| 1381   | Layout 2 | `2d14420a1247`  |
| 1379   | Layout 2 | `2d14420a1247`  |
| 1372   | Layout 2 | `2d14420a1247`  |
| 1366   | Layout 2 | `2d14420a1247`  |
| 1364   | Layout 2 | `2d14420a1247`  |
| 1363   | Layout 2 | `2d14420a1247`  |
| 1360   | Layout 2 | `2d14420a1247`  |
| 1358   | Layout 2 | `2d14420a1247`  |
| 1355   | Layout 2 | `2d14420a1247`  |
| 1351   | Layout 2 | `2d14420a1247`  |
| 1348   | Layout 2 | `2d14420a1247`  |
| 1346   | Layout 2 | `2d14420a1247`  |
| 1341   | Layout 2 | `2d14420a1247`  |
| 1340   | Layout 2 | `2d14420a1247`  |
| 1338   | Layout 2 | `2d14420a1247`  |
| 1335   | Layout 2 | `2d14420a1247`  |
| 1333   | Layout 2 | `2d14420a1247`  |
| 1329   | Layout 2 | `2d14420a1247`  |
| 1327   | Layout 2 | `2d14420a1247`  |
| 1324   | Layout 2 | `2d14420a1247`  |
| 1321   | Layout 2 | `2d14420a1247`  |
| 1319   | Layout 2 | `2d14420a1247`  |
| 1318   | Layout 2 | `2d14420a1247`  |
| 1316   | Layout 2 | `2d14420a1247`  |
| 1313   | Layout 2 | `2d14420a1247`  |
| 1311   | Layout 2 | `2d14420a1247`  |
| 1309   | Layout 2 | `2d14420a1247`  |
| 1304   | Layout 2 | `2d14420a1247`  |
| 1292   | Layout 2 | `2d14420a1247`  |
| 1286   | Layout 2 | `2d14420a1247`  |
| 1280   | Layout 2 | `2d14420a1247`  |
| 1276   | Layout 2 | `2d14420a1247`  |
| 1267   | Layout 2 | `2d14420a1247`  |
| 1261   | Layout 2 | `2d14420a1247`  |
| 1256   | Layout 2 | `2d14420a1247`  |
| 1250   | Layout 2 | `2d14420a1247`  |
| 1246   | Layout 2 | `2d14420a1247`  |
| 1239   | Layout 2 | `2d14420a1247`  |
| 1230   | Layout 2 | `2d14420a1247`  |
| 1226   | Layout 2 | `2d14420a1247`  |
| 1220   | Layout 2 | `2d14420a1247`  |
| 1217   | Layout 2 | `2d14420a1247`  |
| 1211   | Layout 2 | `2d14420a1247`  |
| 1210   | Layout 2 | `2d14420a1247`  |
| 1208   | Layout 2 | `2d14420a1247`  |
| 1203   | Layout 2 | `2d14420a1247`  |
| 1197   | Layout 2 | `2d14420a1247`  |
| 1194   | Layout 2 | `2d14420a1247`  |
| 1192   | Layout 2 | `2d14420a1247`  |
| 1187   | Layout 2 | `2d14420a1247`  |
| 1183   | Layout 2 | `2d14420a1247`  |
| 1177   | Layout 2 | `2d14420a1247`  |
| 1173   | Layout 2 | `2d14420a1247`  |
| 1167   | Layout 2 | `2d14420a1247`  |
| 1164   | Layout 2 | `2d14420a1247`  |
| 1156   | Layout 2 | `2d14420a1247`  |
| 1149   | Layout 2 | `2d14420a1247`  |
| 1144   | Layout 2 | `2d14420a1247`  |
| 1137   | Layout 2 | `2d14420a1247`  |
| 1132   | Layout 2 | `2d14420a1247`  |
| 1127   | Layout 2 | `2d14420a1247`  |
| 1122   | Layout 1 | `2d14420a1247`  |
| 1118   | Layout 1 | `2d14420a1247`  |
| 1114   | Layout 1 | `2d14420a1247`  |
| 1109   | Layout 1 | `2d14420a1247`  |
| 1102   | No file  | `2d14420a1247`  |
| 1096   | No file  | `2d14420a1247`  |
| 1088   | No file  | `2d14420a1247`  |
| 1081   | No file  | `2d14420a1247`  |
| 1076   | No file  | `2d14420a1247`  |
| 1069   | No file  | `2d14420a1247`  |
| 1064   | No file  | `2d14420a1247`  |
| 1058   | No file  | `2d14420a1247`  |
| 1051   | No file  | `2d14420a1247`  |
| 1044   | No file  | `2d14420a1247`  |
| 1036   | No file  | `2d14420a1247`  |
| 1026   | No file  | `2d14420a1247`  |
| 1016   | No file  | `2d14420a1247`  |
| 1009   | No file  | `2d14420a1247`  |
| 1005   | No file  | `2d14420a1247`  |
| 1000   | No file  | `2d14420a1247`  |
| 998    | No file  | `2d14420a1247`  |
| 990    | No file  | `2d14420a1247`  |
| 979    | No file  | `2d14420a1247`  |
| 972    | No file  | `2d14420a1247`  |
| 963    | No file  | `2d14420a1247`  |
| 955    | No file  | `2d14420a1247`  |
| 946    | No file  | `2d14420a1247`  |
| 938    | No file  | `2d14420a1247`  |
| 927    | No file  | `2d14420a1247`  |
| 911    | No file  | `2d14420a1247`  |
| 904    | No file  | `2d14420a1247`  |
| 899    | No file  | `2d14420a1247`  |
| 894    | No file  | `2d14420a1247`  |
| 885    | No file  | `2d14420a1247`  |
| 879    | No file  | `2d14420a1247`  |
| 872    | No file  | `2d14420a1247`  |
| 864    | No file  | `2d14420a1247`  |
| 855    | No file  | `2d14420a1247`  |
| 853    | No file  | `2d14420a1247`  |
| 845    | No file  | `2d14420a1247`  |
| 837    | No file  | `2d14420a1247`  |
| 829    | No file  | `2d14420a1247`  |
| 822    | No file  | `2d14420a1247`  |
| 814    | No file  | `2d14420a1247`  |
| 805    | No file  | `2d14420a1247`  |
| 794    | No file  | `2d14420a1247`  |
| 787    | No file  | `2d14420a1247`  |
| 780    | No file  | `2d14420a1247`  |
| 771    | No file  | `2d14420a1247`  |
| 760    | No file  | `2d14420a1247`  |
| 748    | No file  | `2d14420a1247`  |
| 741    | No file  | `2d14420a1247`  |
| 736    | No file  | `2d14420a1247`  |
| 731    | No file  | `2d14420a1247`  |
| 723    | No file  | `2d14420a1247`  |
| 711    | No file  | `2d14420a1247`  |
| 707    | No file  | `2d14420a1247`  |
| 697    | No file  | `2d14420a1247`  |
| 689    | No file  | `2d14420a1247`  |
| 683    | No file  | `2d14420a1247`  |
| 678    | No file  | `2d14420a1247`  |
| 670    | No file  | `2d14420a1247`  |
| 661    | No file  | `2d14420a1247`  |
| 656    | No file  | `2d14420a1247`  |
| 652    | No file  | `2d14420a1247`  |
| 643    | No file  | `2d14420a1247`  |
| 637    | No file  | `2d14420a1247`  |
| 630    | No file  | `2d14420a1247`  |
| 627    | No file  | `2d14420a1247`  |
| 621    | No file  | `2d14420a1247`  |
| 617    | No file  | `2d14420a1247`  |
| 615    | No file  | `2d14420a1247`  |
| 606    | No file  | `2d14420a1247`  |
| 599    | No file  | `2d14420a1247`  |
| 592    | No file  | `2d14420a1247`  |
| 586    | No file  | `2d14420a1247`  |
| 577    | No file  | `2d14420a1247`  |
| 569    | No file  | `2d14420a1247`  |
| 561    | No file  | `2d14420a1247`  |
| 554    | No file  | `2d14420a1247`  |
| 542    | No file  | `2d14420a1247`  |
| 532    | No file  | `2d14420a1247`  |
| 531    | No file  | `2d14420a1247`  |
| 526    | No file  | `2d14420a1247`  |
| 521    | No file  | `2d14420a1247`  |
| 517    | No file  | `2d14420a1247`  |
| 510    | No file  | `2d14420a1247`  |
| 508    | No file  | `2d14420a1247`  |
| 504    | No file  | `2d14420a1247`  |
| 497    | No file  | `2d14420a1247`  |
| 491    | No file  | `2d14420a1247`  |
| 485    | No file  | `2d14420a1247`  |
| 478    | No file  | `2d14420a1247`  |
| 472    | No file  | `2d14420a1247`  |
| 466    | No file  | `2d14420a1247`  |
| 457    | No file  | `2d14420a1247`  |
| 452    | No file  | `2d14420a1247`  |
| 449    | No file  | `2d14420a1247`  |
| 435    | No file  | `2d14420a1247`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of price ranges                        |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (40 bytes)

| Offset  | Type | Field                    | Notes                                                                                       |
| ------- | ---- | ------------------------ | ------------------------------------------------------------------------------------------- |
| `+0x00` | u64  | start_range_price        | First price of the range, in silver; one more than the previous row's `end_range_price`     |
| `+0x08` | u64  | end_range_price          | Last price of the range; `9,223,372,036,854,775,807` (2^63 - 1) on the last row             |
| `+0x10` | u64  | unit_price               | Price step inside the range                                                                 |
| `+0x18` | u64  | pass_bidding_count       | `100` up to `999,999` silver, then falling to `3` from `50,000,000,000`                     |
| `+0x20` | u64  | world_market_price_point | 12 times `pass_bidding_count` on every row: `1200` for `100`, `36` for `3`                    |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### Row (32 bytes)

| Offset  | Type | Field              | Notes                        |
| ------- | ---- | ------------------ | ---------------------------- |
| `+0x00` | u64  | start_range_price  | Same as Layout 2             |
| `+0x08` | u64  | end_range_price    | Same as Layout 2             |
| `+0x10` | u64  | unit_price         | Same as Layout 2             |
| `+0x18` | u64  | pass_bidding_count | Same as Layout 2             |

## Field Names

The names are the `StartRangePrice`, `EndRangePrice`, `UnitPrice`,
`PassBiddingCount` and `WorldMarketPricePoint` columns of the
`WorldMarketVariedPrice` sheet of a private server's `DataSheets.bexcel` on
client 1784, in that order. The client 1784 file and the client 3482 file
hold the same 23 rows, and 22 of 23 match the sheet on all five columns.
The last row has an `EndRangePrice` of `0` on the sheet and `2^63 - 1` in
the file, so an empty upper bound compiles to the largest i64. The
`WorldMarketVariedPrice` table of a private server on client 519 has the
first four columns and the same 23 ranges, the shape of Layout 1, which
has no `world_market_price_point`.

## Notes

- The rows run in price order, and each `start_range_price` is the
  previous row's `end_range_price` plus one.
- `unit_price` is a power of ten or five times a power of ten in every
  range: `1`, `5`, `10`, `50`, ... `100,000,000,000`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/server_tables.py`.

## Open Questions

### What the Two Counts Do

`pass_bidding_count` and `world_market_price_point` keep their sheet names,
but the client Lua names neither, so what the market does with them is
open. On client 3482 `world_market_price_point` is 12 times
`pass_bidding_count` on all 23 rows, so one may be derived from the other.
