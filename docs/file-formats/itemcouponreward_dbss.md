# `itemcouponreward.dbss` Format

## Purpose

Item coupon reward table placeholder. On client 3464 the file declares zero
records: a u32 count of `0` followed by 12 zero bytes. The server-side source
is the `ImperialTradeReward` sheet, which gives the coupon drop for selling an
item by one of four sale types; see Field Names for the row the server reads.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | ------- | --------- |
| 1      | 1346 and later | 3483    | `itemcouponreward.dbss`       | 16    | -       | -         |
| 1      | 1346 and later | 3483    | `itemcouponrewardoffset.dbss` | 20    | -       | -         |

| Layout | File                          | Known       | Unknown      |
| ------ | ----------------------------- | ----------- | ------------ |
| 1      | `itemcouponreward.dbss`       | 4 B (25.0%) | 12 B (75.0%) |
| 1      | `itemcouponrewardoffset.dbss` | 4 B (20.0%) | 16 B (80.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `72f1fff0ef70`  |
| 3482   | Layout 1             | `72f1fff0ef70`  |
| 3474   | Layout 1             | `72f1fff0ef70`  |
| 3473   | Layout 1             | `72f1fff0ef70`  |
| 3464   | Layout 1             | `72f1fff0ef70`  |
| 3458   | Layout 1             | `72f1fff0ef70`  |
| 3454   | Layout 1             | `72f1fff0ef70`  |
| 3444   | Layout 1             | `72f1fff0ef70`  |
| 3435   | Layout 1             | `72f1fff0ef70`  |
| 3426   | Layout 1             | `72f1fff0ef70`  |
| 3418   | Layout 1             | `72f1fff0ef70`  |
| 3412   | Layout 1             | `72f1fff0ef70`  |
| 3402   | Layout 1             | `72f1fff0ef70`  |
| 3396   | Layout 1             | `72f1fff0ef70`  |
| 3387   | Layout 1             | `72f1fff0ef70`  |
| 3381   | Layout 1             | `72f1fff0ef70`  |
| 3373   | Layout 1             | `72f1fff0ef70`  |
| 3364   | Layout 1             | `72f1fff0ef70`  |
| 3356   | Layout 1             | `72f1fff0ef70`  |
| 3349   | Layout 1             | `72f1fff0ef70`  |
| 3342   | Layout 1             | `72f1fff0ef70`  |
| 3335   | Layout 1             | `72f1fff0ef70`  |
| 3326   | Layout 1             | `72f1fff0ef70`  |
| 3321   | Layout 1             | `72f1fff0ef70`  |
| 3314   | Layout 1             | `72f1fff0ef70`  |
| 3303   | Layout 1             | `72f1fff0ef70`  |
| 3302   | Layout 1             | `72f1fff0ef70`  |
| 3293   | Layout 1             | `72f1fff0ef70`  |
| 3283   | Layout 1             | `72f1fff0ef70`  |
| 3275   | Layout 1             | `72f1fff0ef70`  |
| 3267   | Layout 1             | `72f1fff0ef70`  |
| 3258   | Layout 1             | `72f1fff0ef70`  |
| 3251   | Layout 1             | `72f1fff0ef70`  |
| 3242   | Layout 1             | `72f1fff0ef70`  |
| 3235   | Layout 1             | `72f1fff0ef70`  |
| 3229   | Layout 1             | `72f1fff0ef70`  |
| 3212   | Layout 1             | `72f1fff0ef70`  |
| 3203   | Layout 1             | `72f1fff0ef70`  |
| 3193   | Layout 1             | `72f1fff0ef70`  |
| 3186   | Layout 1             | `72f1fff0ef70`  |
| 3177   | Layout 1             | `72f1fff0ef70`  |
| 3169   | Layout 1             | `72f1fff0ef70`  |
| 3158   | Layout 1             | `72f1fff0ef70`  |
| 3151   | Layout 1             | `72f1fff0ef70`  |
| 3144   | Layout 1             | `72f1fff0ef70`  |
| 3133   | Layout 1             | `72f1fff0ef70`  |
| 3125   | Layout 1             | `72f1fff0ef70`  |
| 3118   | Layout 1             | `72f1fff0ef70`  |
| 3111   | Layout 1             | `72f1fff0ef70`  |
| 3103   | Layout 1             | `72f1fff0ef70`  |
| 3095   | Layout 1             | `72f1fff0ef70`  |
| 3086   | Layout 1             | `72f1fff0ef70`  |
| 3072   | Layout 1             | `72f1fff0ef70`  |
| 3062   | Layout 1             | `72f1fff0ef70`  |
| 3052   | Layout 1             | `72f1fff0ef70`  |
| 3045   | Layout 1             | `72f1fff0ef70`  |
| 3037   | Layout 1             | `72f1fff0ef70`  |
| 3030   | Layout 1             | `72f1fff0ef70`  |
| 3021   | Layout 1             | `72f1fff0ef70`  |
| 3012   | Layout 1             | `72f1fff0ef70`  |
| 3002   | Layout 1             | `72f1fff0ef70`  |
| 2995   | Layout 1             | `72f1fff0ef70`  |
| 2987   | Layout 1             | `72f1fff0ef70`  |
| 2978   | Layout 1             | `72f1fff0ef70`  |
| 2970   | Layout 1             | `72f1fff0ef70`  |
| 2959   | Layout 1             | `72f1fff0ef70`  |
| 2951   | Layout 1             | `72f1fff0ef70`  |
| 2942   | Layout 1             | `72f1fff0ef70`  |
| 2935   | Layout 1             | `72f1fff0ef70`  |
| 2932   | Layout 1             | `72f1fff0ef70`  |
| 2923   | Layout 1             | `72f1fff0ef70`  |
| 2919   | Layout 1             | `72f1fff0ef70`  |
| 2907   | Layout 1             | `72f1fff0ef70`  |
| 2900   | Layout 1             | `72f1fff0ef70`  |
| 2891   | Layout 1             | `72f1fff0ef70`  |
| 2882   | Layout 1             | `72f1fff0ef70`  |
| 2872   | Layout 1             | `72f1fff0ef70`  |
| 2863   | Layout 1             | `72f1fff0ef70`  |
| 2855   | Layout 1             | `72f1fff0ef70`  |
| 2849   | Layout 1             | `72f1fff0ef70`  |
| 2844   | Layout 1             | `72f1fff0ef70`  |
| 2834   | Layout 1             | `72f1fff0ef70`  |
| 2825   | Layout 1             | `72f1fff0ef70`  |
| 2819   | Layout 1             | `72f1fff0ef70`  |
| 2811   | Layout 1             | `72f1fff0ef70`  |
| 2803   | Layout 1             | `72f1fff0ef70`  |
| 2794   | Layout 1             | `72f1fff0ef70`  |
| 2783   | Layout 1             | `72f1fff0ef70`  |
| 2774   | Layout 1             | `72f1fff0ef70`  |
| 2765   | Layout 1             | `72f1fff0ef70`  |
| 2756   | Layout 1             | `72f1fff0ef70`  |
| 2750   | Layout 1             | `72f1fff0ef70`  |
| 2743   | Layout 1             | `72f1fff0ef70`  |
| 2736   | Layout 1             | `72f1fff0ef70`  |
| 2726   | Layout 1             | `72f1fff0ef70`  |
| 2717   | Layout 1             | `72f1fff0ef70`  |
| 2709   | Layout 1             | `72f1fff0ef70`  |
| 2703   | Layout 1             | `72f1fff0ef70`  |
| 2695   | Layout 1             | `72f1fff0ef70`  |
| 2684   | Layout 1             | `72f1fff0ef70`  |
| 2672   | Layout 1             | `72f1fff0ef70`  |
| 2665   | Layout 1             | `72f1fff0ef70`  |
| 2657   | Layout 1             | `72f1fff0ef70`  |
| 2649   | Layout 1             | `72f1fff0ef70`  |
| 2644   | Layout 1             | `72f1fff0ef70`  |
| 2637   | Layout 1             | `72f1fff0ef70`  |
| 2629   | Layout 1             | `72f1fff0ef70`  |
| 2619   | Layout 1             | `72f1fff0ef70`  |
| 2612   | Layout 1             | `72f1fff0ef70`  |
| 2606   | Layout 1             | `72f1fff0ef70`  |
| 2602   | Layout 1             | `72f1fff0ef70`  |
| 2601   | Layout 1             | `72f1fff0ef70`  |
| 2592   | Layout 1             | `72f1fff0ef70`  |
| 2583   | Layout 1             | `72f1fff0ef70`  |
| 2575   | Layout 1             | `72f1fff0ef70`  |
| 2567   | Layout 1             | `72f1fff0ef70`  |
| 2560   | Layout 1             | `72f1fff0ef70`  |
| 2553   | Layout 1             | `72f1fff0ef70`  |
| 2545   | Layout 1             | `72f1fff0ef70`  |
| 2538   | Layout 1             | `72f1fff0ef70`  |
| 2529   | Layout 1             | `72f1fff0ef70`  |
| 2519   | Layout 1             | `72f1fff0ef70`  |
| 2513   | Layout 1             | `72f1fff0ef70`  |
| 2510   | Layout 1             | `72f1fff0ef70`  |
| 2507   | Layout 1             | `72f1fff0ef70`  |
| 2503   | Layout 1             | `72f1fff0ef70`  |
| 2498   | Layout 1             | `72f1fff0ef70`  |
| 2492   | Layout 1             | `72f1fff0ef70`  |
| 2487   | Layout 1             | `72f1fff0ef70`  |
| 2480   | Layout 1             | `72f1fff0ef70`  |
| 2474   | Layout 1             | `72f1fff0ef70`  |
| 2468   | Layout 1             | `72f1fff0ef70`  |
| 2460   | Layout 1             | `72f1fff0ef70`  |
| 2453   | Layout 1             | `72f1fff0ef70`  |
| 2444   | Layout 1             | `72f1fff0ef70`  |
| 2438   | Layout 1             | `72f1fff0ef70`  |
| 2434   | Layout 1             | `72f1fff0ef70`  |
| 2429   | Layout 1             | `72f1fff0ef70`  |
| 2421   | Layout 1             | `72f1fff0ef70`  |
| 2414   | Layout 1             | `72f1fff0ef70`  |
| 2407   | Layout 1             | `72f1fff0ef70`  |
| 2401   | Layout 1             | `72f1fff0ef70`  |
| 2397   | Layout 1             | `72f1fff0ef70`  |
| 2393   | Layout 1             | `72f1fff0ef70`  |
| 2384   | Layout 1             | `72f1fff0ef70`  |
| 2378   | Layout 1             | `72f1fff0ef70`  |
| 2372   | Layout 1             | `72f1fff0ef70`  |
| 2358   | Layout 1             | `72f1fff0ef70`  |
| 2352   | Layout 1             | `72f1fff0ef70`  |
| 2347   | Layout 1             | `72f1fff0ef70`  |
| 2343   | Layout 1             | `72f1fff0ef70`  |
| 2335   | Layout 1             | `72f1fff0ef70`  |
| 2327   | Layout 1             | `72f1fff0ef70`  |
| 2324   | Layout 1             | `72f1fff0ef70`  |
| 2319   | Layout 1             | `72f1fff0ef70`  |
| 2313   | Layout 1             | `72f1fff0ef70`  |
| 2308   | Layout 1             | `72f1fff0ef70`  |
| 2302   | Layout 1             | `72f1fff0ef70`  |
| 2295   | Layout 1             | `72f1fff0ef70`  |
| 2290   | Layout 1             | `72f1fff0ef70`  |
| 2284   | Layout 1             | `72f1fff0ef70`  |
| 2276   | Layout 1             | `72f1fff0ef70`  |
| 2269   | Layout 1             | `72f1fff0ef70`  |
| 2259   | Layout 1             | `72f1fff0ef70`  |
| 2250   | Layout 1             | `72f1fff0ef70`  |
| 2243   | Layout 1             | `72f1fff0ef70`  |
| 2235   | Layout 1             | `72f1fff0ef70`  |
| 2229   | Layout 1             | `72f1fff0ef70`  |
| 2224   | Layout 1             | `72f1fff0ef70`  |
| 2218   | Layout 1             | `72f1fff0ef70`  |
| 2215   | Layout 1             | `72f1fff0ef70`  |
| 2207   | Layout 1             | `72f1fff0ef70`  |
| 2203   | Layout 1             | `72f1fff0ef70`  |
| 2196   | Layout 1             | `72f1fff0ef70`  |
| 2192   | Layout 1             | `72f1fff0ef70`  |
| 2189   | Layout 1             | `72f1fff0ef70`  |
| 2183   | Layout 1             | `72f1fff0ef70`  |
| 2179   | Layout 1             | `72f1fff0ef70`  |
| 2171   | Layout 1             | `72f1fff0ef70`  |
| 2163   | Layout 1             | `72f1fff0ef70`  |
| 2156   | Layout 1             | `72f1fff0ef70`  |
| 2151   | Layout 1             | `72f1fff0ef70`  |
| 2147   | Layout 1             | `72f1fff0ef70`  |
| 2142   | Layout 1             | `72f1fff0ef70`  |
| 2138   | Layout 1             | `72f1fff0ef70`  |
| 2134   | Layout 1             | `72f1fff0ef70`  |
| 2130   | Layout 1             | `72f1fff0ef70`  |
| 2122   | Layout 1             | `72f1fff0ef70`  |
| 2107   | Layout 1             | `72f1fff0ef70`  |
| 2098   | Layout 1             | `72f1fff0ef70`  |
| 2089   | Layout 1             | `72f1fff0ef70`  |
| 2081   | Layout 1             | `72f1fff0ef70`  |
| 2073   | Layout 1             | `72f1fff0ef70`  |
| 2067   | Layout 1             | `72f1fff0ef70`  |
| 2063   | Layout 1             | `72f1fff0ef70`  |
| 2059   | Layout 1             | `72f1fff0ef70`  |
| 2052   | Layout 1             | `72f1fff0ef70`  |
| 2044   | Layout 1             | `72f1fff0ef70`  |
| 2039   | Layout 1             | `72f1fff0ef70`  |
| 2032   | Layout 1             | `72f1fff0ef70`  |
| 2025   | Layout 1             | `72f1fff0ef70`  |
| 2011   | Layout 1             | `72f1fff0ef70`  |
| 2005   | Layout 1             | `72f1fff0ef70`  |
| 2000   | Layout 1             | `72f1fff0ef70`  |
| 1996   | Layout 1             | `72f1fff0ef70`  |
| 1991   | Layout 1             | `72f1fff0ef70`  |
| 1985   | Layout 1             | `72f1fff0ef70`  |
| 1980   | Layout 1             | `72f1fff0ef70`  |
| 1969   | Layout 1             | `72f1fff0ef70`  |
| 1964   | Layout 1             | `72f1fff0ef70`  |
| 1958   | Layout 1             | `72f1fff0ef70`  |
| 1950   | Layout 1             | `72f1fff0ef70`  |
| 1945   | Layout 1             | `72f1fff0ef70`  |
| 1937   | Layout 1             | `72f1fff0ef70`  |
| 1933   | Layout 1             | `72f1fff0ef70`  |
| 1927   | Layout 1             | `72f1fff0ef70`  |
| 1921   | Layout 1             | `72f1fff0ef70`  |
| 1914   | Layout 1             | `72f1fff0ef70`  |
| 1908   | Layout 1             | `72f1fff0ef70`  |
| 1897   | Layout 1             | `72f1fff0ef70`  |
| 1892   | Layout 1             | `72f1fff0ef70`  |
| 1886   | Layout 1             | `72f1fff0ef70`  |
| 1881   | Layout 1             | `72f1fff0ef70`  |
| 1871   | Layout 1             | `72f1fff0ef70`  |
| 1866   | Layout 1             | `72f1fff0ef70`  |
| 1862   | Layout 1             | `72f1fff0ef70`  |
| 1854   | Layout 1             | `72f1fff0ef70`  |
| 1846   | Layout 1             | `72f1fff0ef70`  |
| 1838   | Layout 1             | `72f1fff0ef70`  |
| 1832   | Layout 1             | `72f1fff0ef70`  |
| 1826   | Layout 1             | `72f1fff0ef70`  |
| 1822   | Layout 1             | `72f1fff0ef70`  |
| 1818   | Layout 1             | `72f1fff0ef70`  |
| 1804   | Layout 1             | `72f1fff0ef70`  |
| 1794   | Layout 1             | `72f1fff0ef70`  |
| 1790   | Layout 1             | `72f1fff0ef70`  |
| 1784   | Layout 1             | `72f1fff0ef70`  |
| 1774   | Layout 1             | `72f1fff0ef70`  |
| 1771   | Layout 1             | `72f1fff0ef70`  |
| 1762   | Layout 1             | `72f1fff0ef70`  |
| 1759   | Layout 1             | `72f1fff0ef70`  |
| 1754   | Layout 1             | `72f1fff0ef70`  |
| 1749   | Layout 1             | `72f1fff0ef70`  |
| 1743   | Layout 1             | `72f1fff0ef70`  |
| 1737   | Layout 1             | `72f1fff0ef70`  |
| 1731   | Layout 1             | `72f1fff0ef70`  |
| 1725   | Layout 1             | `72f1fff0ef70`  |
| 1717   | Layout 1             | `72f1fff0ef70`  |
| 1710   | Layout 1             | `72f1fff0ef70`  |
| 1704   | Layout 1             | `72f1fff0ef70`  |
| 1698   | Layout 1             | `72f1fff0ef70`  |
| 1690   | Layout 1             | `72f1fff0ef70`  |
| 1685   | Layout 1             | `72f1fff0ef70`  |
| 1680   | Layout 1             | `72f1fff0ef70`  |
| 1674   | Layout 1             | `72f1fff0ef70`  |
| 1668   | Layout 1             | `72f1fff0ef70`  |
| 1659   | Layout 1             | `72f1fff0ef70`  |
| 1649   | Layout 1             | `72f1fff0ef70`  |
| 1642   | Layout 1             | `72f1fff0ef70`  |
| 1636   | Layout 1             | `72f1fff0ef70`  |
| 1628   | Layout 1             | `72f1fff0ef70`  |
| 1622   | Layout 1             | `72f1fff0ef70`  |
| 1614   | Layout 1             | `72f1fff0ef70`  |
| 1608   | Layout 1             | `72f1fff0ef70`  |
| 1602   | Layout 1             | `72f1fff0ef70`  |
| 1598   | Layout 1             | `72f1fff0ef70`  |
| 1594   | Layout 1             | `72f1fff0ef70`  |
| 1590   | Layout 1             | `72f1fff0ef70`  |
| 1587   | Layout 1             | `72f1fff0ef70`  |
| 1584   | Layout 1             | `72f1fff0ef70`  |
| 1579   | Layout 1             | `72f1fff0ef70`  |
| 1572   | Layout 1             | `72f1fff0ef70`  |
| 1565   | Layout 1             | `72f1fff0ef70`  |
| 1559   | Layout 1             | `72f1fff0ef70`  |
| 1554   | Layout 1             | `72f1fff0ef70`  |
| 1547   | Layout 1             | `72f1fff0ef70`  |
| 1537   | Layout 1             | `72f1fff0ef70`  |
| 1529   | Layout 1             | `72f1fff0ef70`  |
| 1524   | Layout 1             | `72f1fff0ef70`  |
| 1519   | Layout 1             | `72f1fff0ef70`  |
| 1509   | Layout 1             | `72f1fff0ef70`  |
| 1506   | Layout 1             | `72f1fff0ef70`  |
| 1504   | Layout 1             | `72f1fff0ef70`  |
| 1500   | Layout 1             | `72f1fff0ef70`  |
| 1493   | Layout 1             | `72f1fff0ef70`  |
| 1489   | Layout 1             | `72f1fff0ef70`  |
| 1485   | Layout 1             | `72f1fff0ef70`  |
| 1481   | Layout 1             | `72f1fff0ef70`  |
| 1474   | Layout 1             | `72f1fff0ef70`  |
| 1466   | Layout 1             | `72f1fff0ef70`  |
| 1462   | Layout 1             | `72f1fff0ef70`  |
| 1459   | Layout 1             | `72f1fff0ef70`  |
| 1453   | Layout 1             | `72f1fff0ef70`  |
| 1450   | Layout 1             | `72f1fff0ef70`  |
| 1445   | Layout 1             | `72f1fff0ef70`  |
| 1439   | Layout 1             | `72f1fff0ef70`  |
| 1433   | Layout 1             | `72f1fff0ef70`  |
| 1430   | Layout 1             | `72f1fff0ef70`  |
| 1426   | Layout 1             | `72f1fff0ef70`  |
| 1421   | Layout 1             | `72f1fff0ef70`  |
| 1417   | Layout 1             | `72f1fff0ef70`  |
| 1416   | Layout 1             | `72f1fff0ef70`  |
| 1409   | Layout 1             | `72f1fff0ef70`  |
| 1405   | Layout 1             | `72f1fff0ef70`  |
| 1401   | Layout 1             | `72f1fff0ef70`  |
| 1396   | Layout 1             | `72f1fff0ef70`  |
| 1391   | Layout 1             | `72f1fff0ef70`  |
| 1390   | Layout 1             | `72f1fff0ef70`  |
| 1386   | Layout 1             | `72f1fff0ef70`  |
| 1381   | Layout 1             | `72f1fff0ef70`  |
| 1379   | Layout 1             | `72f1fff0ef70`  |
| 1372   | Layout 1             | `72f1fff0ef70`  |
| 1366   | Layout 1             | `72f1fff0ef70`  |
| 1364   | Layout 1             | `72f1fff0ef70`  |
| 1363   | Layout 1             | `72f1fff0ef70`  |
| 1360   | Layout 1             | `72f1fff0ef70`  |
| 1358   | Layout 1             | `72f1fff0ef70`  |
| 1355   | Layout 1             | `72f1fff0ef70`  |
| 1351   | Layout 1             | `72f1fff0ef70`  |
| 1348   | Layout 1             | `72f1fff0ef70`  |
| 1346   | Layout 1             | `72f1fff0ef70`  |
| 1341   | No documented layout | `72f1fff0ef70`  |
| 1340   | No documented layout | `72f1fff0ef70`  |
| 1338   | No documented layout | `72f1fff0ef70`  |
| 1335   | No documented layout | `72f1fff0ef70`  |
| 1333   | No documented layout | `72f1fff0ef70`  |
| 1329   | No documented layout | `72f1fff0ef70`  |
| 1327   | No documented layout | `72f1fff0ef70`  |
| 1324   | No documented layout | `72f1fff0ef70`  |
| 1321   | No documented layout | `72f1fff0ef70`  |
| 1319   | No documented layout | `72f1fff0ef70`  |
| 1318   | No documented layout | `72f1fff0ef70`  |
| 1316   | No documented layout | `72f1fff0ef70`  |
| 1313   | No documented layout | `72f1fff0ef70`  |
| 1311   | No documented layout | `72f1fff0ef70`  |
| 1309   | No documented layout | `72f1fff0ef70`  |
| 1304   | No documented layout | `72f1fff0ef70`  |
| 1292   | No documented layout | `72f1fff0ef70`  |
| 1286   | No documented layout | `72f1fff0ef70`  |
| 1280   | No documented layout | `72f1fff0ef70`  |
| 1276   | No documented layout | `72f1fff0ef70`  |
| 1267   | No documented layout | `72f1fff0ef70`  |
| 1261   | No documented layout | `72f1fff0ef70`  |
| 1256   | No documented layout | `72f1fff0ef70`  |
| 1250   | No file              | `72f1fff0ef70`  |
| 1246   | No file              | `72f1fff0ef70`  |
| 1239   | No file              | `72f1fff0ef70`  |
| 1230   | No file              | `72f1fff0ef70`  |
| 1226   | No file              | `72f1fff0ef70`  |
| 1220   | No file              | `72f1fff0ef70`  |
| 1217   | No file              | `72f1fff0ef70`  |
| 1211   | No file              | `72f1fff0ef70`  |
| 1210   | No file              | `72f1fff0ef70`  |
| 1208   | No file              | `72f1fff0ef70`  |
| 1203   | No file              | `72f1fff0ef70`  |
| 1197   | No file              | `72f1fff0ef70`  |
| 1194   | No file              | `72f1fff0ef70`  |
| 1192   | No file              | `72f1fff0ef70`  |
| 1187   | No file              | `72f1fff0ef70`  |
| 1183   | No file              | `72f1fff0ef70`  |
| 1177   | No file              | `72f1fff0ef70`  |
| 1173   | No file              | `72f1fff0ef70`  |
| 1167   | No file              | `72f1fff0ef70`  |
| 1164   | No file              | `72f1fff0ef70`  |
| 1156   | No file              | `72f1fff0ef70`  |
| 1149   | No file              | `72f1fff0ef70`  |
| 1144   | No file              | `72f1fff0ef70`  |
| 1137   | No file              | `72f1fff0ef70`  |
| 1132   | No file              | `72f1fff0ef70`  |
| 1127   | No file              | `72f1fff0ef70`  |
| 1122   | No file              | `72f1fff0ef70`  |
| 1118   | No file              | `72f1fff0ef70`  |
| 1114   | No file              | `72f1fff0ef70`  |
| 1109   | No file              | `72f1fff0ef70`  |
| 1102   | No file              | `72f1fff0ef70`  |
| 1096   | No file              | `72f1fff0ef70`  |
| 1088   | No file              | `72f1fff0ef70`  |
| 1081   | No file              | `72f1fff0ef70`  |
| 1076   | No file              | `72f1fff0ef70`  |
| 1069   | No file              | `72f1fff0ef70`  |
| 1064   | No file              | `72f1fff0ef70`  |
| 1058   | No file              | `72f1fff0ef70`  |
| 1051   | No file              | `72f1fff0ef70`  |
| 1044   | No file              | `72f1fff0ef70`  |
| 1036   | No file              | `72f1fff0ef70`  |
| 1026   | No file              | `72f1fff0ef70`  |
| 1016   | No file              | `72f1fff0ef70`  |
| 1009   | No file              | `72f1fff0ef70`  |
| 1005   | No file              | `72f1fff0ef70`  |
| 1000   | No file              | `72f1fff0ef70`  |
| 998    | No file              | `72f1fff0ef70`  |
| 990    | No file              | `72f1fff0ef70`  |
| 979    | No file              | `72f1fff0ef70`  |
| 972    | No file              | `72f1fff0ef70`  |
| 963    | No file              | `72f1fff0ef70`  |
| 955    | No file              | `72f1fff0ef70`  |
| 946    | No file              | `72f1fff0ef70`  |
| 938    | No file              | `72f1fff0ef70`  |
| 927    | No file              | `72f1fff0ef70`  |
| 911    | No file              | `72f1fff0ef70`  |
| 904    | No file              | `72f1fff0ef70`  |
| 899    | No file              | `72f1fff0ef70`  |
| 894    | No file              | `72f1fff0ef70`  |
| 885    | No file              | `72f1fff0ef70`  |
| 879    | No file              | `72f1fff0ef70`  |
| 872    | No file              | `72f1fff0ef70`  |
| 864    | No file              | `72f1fff0ef70`  |
| 855    | No file              | `72f1fff0ef70`  |
| 853    | No file              | `72f1fff0ef70`  |
| 845    | No file              | `72f1fff0ef70`  |
| 837    | No file              | `72f1fff0ef70`  |
| 829    | No file              | `72f1fff0ef70`  |
| 822    | No file              | `72f1fff0ef70`  |
| 814    | No file              | `72f1fff0ef70`  |
| 805    | No file              | `72f1fff0ef70`  |
| 794    | No file              | `72f1fff0ef70`  |
| 787    | No file              | `72f1fff0ef70`  |
| 780    | No file              | `72f1fff0ef70`  |
| 771    | No file              | `72f1fff0ef70`  |
| 760    | No file              | `72f1fff0ef70`  |
| 748    | No file              | `72f1fff0ef70`  |
| 741    | No file              | `72f1fff0ef70`  |
| 736    | No file              | `72f1fff0ef70`  |
| 731    | No file              | `72f1fff0ef70`  |
| 723    | No file              | `72f1fff0ef70`  |
| 711    | No file              | `72f1fff0ef70`  |
| 707    | No file              | `72f1fff0ef70`  |
| 697    | No file              | `72f1fff0ef70`  |
| 689    | No file              | `72f1fff0ef70`  |
| 683    | No file              | `72f1fff0ef70`  |
| 678    | No file              | `72f1fff0ef70`  |
| 670    | No file              | `72f1fff0ef70`  |
| 661    | No file              | `72f1fff0ef70`  |
| 656    | No file              | `72f1fff0ef70`  |
| 652    | No file              | `72f1fff0ef70`  |
| 643    | No file              | `72f1fff0ef70`  |
| 637    | No file              | `72f1fff0ef70`  |
| 630    | No file              | `72f1fff0ef70`  |
| 627    | No file              | `72f1fff0ef70`  |
| 621    | No file              | `72f1fff0ef70`  |
| 617    | No file              | `72f1fff0ef70`  |
| 615    | No file              | `72f1fff0ef70`  |
| 606    | No file              | `72f1fff0ef70`  |
| 599    | No file              | `72f1fff0ef70`  |
| 592    | No file              | `72f1fff0ef70`  |
| 586    | No file              | `72f1fff0ef70`  |
| 577    | No file              | `72f1fff0ef70`  |
| 569    | No file              | `72f1fff0ef70`  |
| 561    | No file              | `72f1fff0ef70`  |
| 554    | No file              | `72f1fff0ef70`  |
| 542    | No file              | `72f1fff0ef70`  |
| 532    | No file              | `72f1fff0ef70`  |
| 531    | No file              | `72f1fff0ef70`  |
| 526    | No file              | `72f1fff0ef70`  |
| 521    | No file              | `72f1fff0ef70`  |
| 517    | No file              | `72f1fff0ef70`  |
| 510    | No file              | `72f1fff0ef70`  |
| 508    | No file              | `72f1fff0ef70`  |
| 504    | No file              | `72f1fff0ef70`  |
| 497    | No file              | `72f1fff0ef70`  |
| 491    | No file              | `72f1fff0ef70`  |
| 485    | No file              | `72f1fff0ef70`  |
| 478    | No file              | `72f1fff0ef70`  |
| 472    | No file              | `72f1fff0ef70`  |
| 466    | No file              | `72f1fff0ef70`  |
| 457    | No file              | `72f1fff0ef70`  |
| 452    | No file              | `72f1fff0ef70`  |
| 449    | No file              | `72f1fff0ef70`  |
| 435    | No file              | `72f1fff0ef70`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                 |
| ----------------------------- | -------- | -------------------------------------------------------------------- |
| `itemcouponrewardoffset.dbss` | Optional | Offset companion; its count does not match the bytes that follow it |

The handler reads only the main file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

This layout covers only `count = 0`. No record structure can be inferred
because the file holds no records.

| Offset  | Type      | Field      | Notes                                 |
| ------- | --------- | ---------- | ------------------------------------- |
| `+0x00` | u32       | count      | Number of records; `0` on client 3464 |
| `+0x04` | bytes[12] | unknown_04 | All zero on client 3464               |

### `itemcouponrewardoffset.dbss`

20 bytes on client 3464: `04 00 00 00` followed by 16 zero bytes. The count
does not drive the bytes after it.

| Offset  | Type | Field      | Notes              |
| ------- | ---- | ---------- | ------------------ |
| `+0x00` | u32  | count      | `4` on client 3464 |
| `+0x04` | u32  | unknown_04 | `0` on client 3464 |
| `+0x08` | u32  | unknown_08 | `0` on client 3464 |
| `+0x0C` | u32  | unknown_0c | `0` on client 3464 |
| `+0x10` | u32  | unknown_10 | `0` on client 3464 |

Every other bare offset companion has rows of key, u32 offset and u32 size
(9 bytes for `carriagespecoffset.dbss`, 10 for `guildbossoffset.dbss`, 12 for
`itemcollectionscrolloffset.dbss`). Four such rows need at least 36 bytes, so
the 16 bytes after the count are not four offset rows.

## Field Names

The file holds no rows, so these names come from the server and are not
read by the handler. They apply once a client ships rows.

The server dump of a private server on client 1784 (`Instance_dumpFull.exe`)
loads `gc::ItemCouponRewardStaticStatus` rows twice. Its getter
`ItemCouponRewardStaticStatusManager::getXXX(type, key)` (VA `0x140b21080`)
looks the key up in a per-type map of (offset, size) pairs, opens the
`ItemCouponReward` binary at that offset and hands the bytes to the row reader
(VA `0x140b206d0`). The `ImperialTradeReward` sheet of
`DataSheet_CouponReward.xlsm` is loaded by the loop at VA `0x1408b8570`
(`DataSheets.bexcel` has no copy of that sheet; the server tables of a
private server on client 519 have it as `ImperialTradeReward` with the same four columns). Both
loaders write the same members, and the 2016 client's PDB names them:

| File offset | Type | Field                  | Member  | 2016 PDB member      | Sheet column         |
| ----------- | ---- | ---------------------- | ------- | -------------------- | -------------------- |
| `+0x00`     | u32  | `key`                  | `+0x00` | `_key`               | `Key`                |
| `+0x04`     | u16  | `coupon_drop_item_key` | `+0x0C` | `_couponDropItemKey` | `RewardDropGroupKey` |
| `+0x06`     | u8   | `coupon_type`          | `+0x04` | `_couponType`        | `Type`               |
| `+0x07`     | u32  | `reward_rate`          | `+0x08` | `_rewardRate`        | `ExchangeRate`       |

The row is 11 bytes. The file order differs from the member order, so the
file offsets rest on the row reader alone. Member `+0x10` is
`_couponDropItem`, a `gc::ItemMainGroupStaticStatus` pointer the server
links from `coupon_drop_item_key`; the file does not store it.

The row check (VA `0x140b1fd60`) logs "Type is wrong" when `coupon_type` is
`4` or more, "`_couponDropItemKey` is missing" when the drop key is `0`, and
"`_rewardRate` is abnormal" when the rate is above 1,000,000, so the rate is
in parts per million. The link step (VA `0x140b20130`) looks `key` up as an
item key for types 0, 2 and 3 ("coupon item does not exist in the item
table") and skips that check for type 1. For every type it then resolves
`coupon_drop_item_key` as a main drop group ("coupon reward item
MainDropGroup does not exist").

`coupon_type` is `gc::ECouponType` from the 2016 PDB. The sheet's Korean
comment on `Type` says which sale it counts, and on `Key` that selling the
item with that key gives the coupon:

| ID  | Enum                          | Sheet comment                                            |
| --- | ----------------------------- | -------------------------------------------------------- |
| 0   | `ECouponType_TerritorySupply` | Imperial delivery, imperial crafting or fishing delivery |
| 1   | `ECouponType_Vehicle`         | Horse delivery                                           |
| 2   | `ECouponType_NpcWorking`      | House crafting                                           |
| 3   | `ECouponType_Trade`           | General trade                                            |

`ECouponType_Max` is `4`. The 2016 manager holds `pa::Array<..., 4> _list`,
one map per type, and the 1784 manager adds four offset maps after them;
`getXXX` returns nothing for a type of `4` or more.

On the private server's client 1784 data, the sheet holds 2,038 rows of all
four types, and its compiled `itemcouponreward.dbss` and
`itemcouponrewardoffset.dbss` hold the same 16 and 20 bytes as client 3464.
The rows stay on the server. `global_define_cpp_enum.luac` has no coupon
type enum.

## Notes

- `python browser.py --list *coupon*` shows `coupon.dbss` and
  `couponoffset.dbss` as the only other coupon tables; they are separate files
  with their own layout.
- The client Lua has no reference to the table. `widget/coupon/coupon.luac`
  only forwards `FromClient_UseCouponItem(itemWhereType, slotNo)` to
  `ToClient_RegisterCoupon`.
- The other empty DBSS tables ([empty](empty_dbss.md)) are 4 bytes, and
  their offset companions are 4 bytes with a count of `0`. This file is the
  only one with bytes after the count.
- `EmptyTableHandler` previews it like those tables and raises an error when
  `count` is not `0`, so a client that ships records shows up as a parse
  error. `itemcouponrewardoffset.dbss` gets a raw view of its u32 words
  (`_dbss/itemcouponreward/`) until its layout is known.

## Open Questions

### One Block per Coupon Type

The 12 zero bytes after the count in `itemcouponreward.dbss` and the four
zero words after the `4` in `itemcouponrewardoffset.dbss` match no row
layout. The `4` equals `ECouponType_Max`, and the 1784 server keeps one row
map and one offset map per coupon type (Field Names). Read as one block per
type, each a u32 row count and its rows, both files fit exactly with every
block empty:

- `itemcouponreward.dbss`: four row counts of `0` and no block count, the
  shape of [actionexp](actionexp_dbss.md), 4 x 4 = 16 bytes.
- `itemcouponrewardoffset.dbss`: a block count of `4`, then four row counts
  of `0`, the shape of `lifeexpoffset.dbss` in [lifeexp](lifeexp_dbss.md),
  4 + 4 x 4 = 20 bytes.

The server dump reads rows only through `getXXX`, and no reader of either
file's header was found in it, so the words keep their `unknown_<offset>`
names. A client that ships rows would confirm the blocks.
