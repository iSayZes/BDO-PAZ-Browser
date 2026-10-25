# `petgrade.dbss` Format

## Purpose

Maps each (species, variant) pet combination to a grade value, one record per pair. 21 `pet.dbss` records have a pair with no grade record. Values 1–5 map to known grade labels; value 6 remains unconfirmed.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records        | Row bytes |
| ------ | -------------- | --------------------- | ----- | -------------- | --------- |
| 1      | 1346 and later | `petgrade.dbss`       | 3,388 | 282 Record     | 12        |
| 1      | 1346 and later | `petgradeoffset.dbss` | 3,388 | 282 Offset Row | 12        |

| Layout | File                  | Known           | Unknown         |
| ------ | --------------------- | --------------- | --------------- |
| 1      | `petgrade.dbss`       | 2,260 B (66.7%) | 1,128 B (33.3%) |
| 1      | `petgradeoffset.dbss` | 2,824 B (83.4%) | 564 B (16.6%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `2ea64e09fd22`  |
| 3482   | Layout 1             | `2ea64e09fd22`  |
| 3474   | Layout 1             | `2ea64e09fd22`  |
| 3473   | Layout 1             | `2ea64e09fd22`  |
| 3464   | Layout 1             | `2ea64e09fd22`  |
| 3458   | Layout 1             | `2ea64e09fd22`  |
| 3454   | Layout 1             | `2ea64e09fd22`  |
| 3444   | Layout 1             | `2ea64e09fd22`  |
| 3435   | Layout 1             | `2ea64e09fd22`  |
| 3426   | Layout 1             | `2ea64e09fd22`  |
| 3418   | Layout 1             | `2ea64e09fd22`  |
| 3412   | Layout 1             | `2ea64e09fd22`  |
| 3402   | Layout 1             | `2ea64e09fd22`  |
| 3396   | Layout 1             | `2ea64e09fd22`  |
| 3387   | Layout 1             | `2ea64e09fd22`  |
| 3381   | Layout 1             | `2ea64e09fd22`  |
| 3373   | Layout 1             | `2ea64e09fd22`  |
| 3364   | Layout 1             | `2ea64e09fd22`  |
| 3356   | Layout 1             | `2ea64e09fd22`  |
| 3349   | Layout 1             | `2ea64e09fd22`  |
| 3342   | Layout 1             | `2ea64e09fd22`  |
| 3335   | Layout 1             | `2ea64e09fd22`  |
| 3326   | Layout 1             | `2ea64e09fd22`  |
| 3321   | Layout 1             | `2ea64e09fd22`  |
| 3314   | Layout 1             | `2ea64e09fd22`  |
| 3303   | Layout 1             | `2ea64e09fd22`  |
| 3302   | Layout 1             | `2ea64e09fd22`  |
| 3293   | Layout 1             | `2ea64e09fd22`  |
| 3283   | Layout 1             | `2ea64e09fd22`  |
| 3275   | Layout 1             | `2ea64e09fd22`  |
| 3267   | Layout 1             | `2ea64e09fd22`  |
| 3258   | Layout 1             | `2ea64e09fd22`  |
| 3251   | Layout 1             | `2ea64e09fd22`  |
| 3242   | Layout 1             | `2ea64e09fd22`  |
| 3235   | Layout 1             | `2ea64e09fd22`  |
| 3229   | Layout 1             | `2ea64e09fd22`  |
| 3212   | Layout 1             | `2ea64e09fd22`  |
| 3203   | Layout 1             | `2ea64e09fd22`  |
| 3193   | Layout 1             | `2ea64e09fd22`  |
| 3186   | Layout 1             | `2ea64e09fd22`  |
| 3177   | Layout 1             | `2ea64e09fd22`  |
| 3169   | Layout 1             | `2ea64e09fd22`  |
| 3158   | Layout 1             | `2ea64e09fd22`  |
| 3151   | Layout 1             | `2ea64e09fd22`  |
| 3144   | Layout 1             | `2ea64e09fd22`  |
| 3133   | Layout 1             | `2ea64e09fd22`  |
| 3125   | Layout 1             | `2ea64e09fd22`  |
| 3118   | Layout 1             | `2ea64e09fd22`  |
| 3111   | Layout 1             | `2ea64e09fd22`  |
| 3103   | Layout 1             | `2ea64e09fd22`  |
| 3095   | Layout 1             | `2ea64e09fd22`  |
| 3086   | Layout 1             | `2ea64e09fd22`  |
| 3072   | Layout 1             | `2ea64e09fd22`  |
| 3062   | Layout 1             | `2ea64e09fd22`  |
| 3052   | Layout 1             | `2ea64e09fd22`  |
| 3045   | Layout 1             | `2ea64e09fd22`  |
| 3037   | Layout 1             | `2ea64e09fd22`  |
| 3030   | Layout 1             | `2ea64e09fd22`  |
| 3021   | Layout 1             | `2ea64e09fd22`  |
| 3012   | Layout 1             | `2ea64e09fd22`  |
| 3002   | Layout 1             | `2ea64e09fd22`  |
| 2995   | Layout 1             | `2ea64e09fd22`  |
| 2987   | Layout 1             | `2ea64e09fd22`  |
| 2978   | Layout 1             | `2ea64e09fd22`  |
| 2970   | Layout 1             | `2ea64e09fd22`  |
| 2959   | Layout 1             | `2ea64e09fd22`  |
| 2951   | Layout 1             | `2ea64e09fd22`  |
| 2942   | Layout 1             | `2ea64e09fd22`  |
| 2935   | Layout 1             | `2ea64e09fd22`  |
| 2932   | Layout 1             | `2ea64e09fd22`  |
| 2923   | Layout 1             | `2ea64e09fd22`  |
| 2919   | Layout 1             | `2ea64e09fd22`  |
| 2907   | Layout 1             | `2ea64e09fd22`  |
| 2900   | Layout 1             | `2ea64e09fd22`  |
| 2891   | Layout 1             | `2ea64e09fd22`  |
| 2882   | Layout 1             | `2ea64e09fd22`  |
| 2872   | Layout 1             | `2ea64e09fd22`  |
| 2863   | Layout 1             | `2ea64e09fd22`  |
| 2855   | Layout 1             | `2ea64e09fd22`  |
| 2849   | Layout 1             | `2ea64e09fd22`  |
| 2844   | Layout 1             | `2ea64e09fd22`  |
| 2834   | Layout 1             | `2ea64e09fd22`  |
| 2825   | Layout 1             | `2ea64e09fd22`  |
| 2819   | Layout 1             | `2ea64e09fd22`  |
| 2811   | Layout 1             | `2ea64e09fd22`  |
| 2803   | Layout 1             | `2ea64e09fd22`  |
| 2794   | Layout 1             | `2ea64e09fd22`  |
| 2783   | Layout 1             | `2ea64e09fd22`  |
| 2774   | Layout 1             | `2ea64e09fd22`  |
| 2765   | Layout 1             | `2ea64e09fd22`  |
| 2756   | Layout 1             | `2ea64e09fd22`  |
| 2750   | Layout 1             | `2ea64e09fd22`  |
| 2743   | Layout 1             | `2ea64e09fd22`  |
| 2736   | Layout 1             | `2ea64e09fd22`  |
| 2726   | Layout 1             | `2ea64e09fd22`  |
| 2717   | Layout 1             | `2ea64e09fd22`  |
| 2709   | Layout 1             | `2ea64e09fd22`  |
| 2703   | Layout 1             | `2ea64e09fd22`  |
| 2695   | Layout 1             | `2ea64e09fd22`  |
| 2684   | Layout 1             | `2ea64e09fd22`  |
| 2672   | Layout 1             | `2ea64e09fd22`  |
| 2665   | Layout 1             | `2ea64e09fd22`  |
| 2657   | Layout 1             | `2ea64e09fd22`  |
| 2649   | Layout 1             | `2ea64e09fd22`  |
| 2644   | Layout 1             | `2ea64e09fd22`  |
| 2637   | Layout 1             | `2ea64e09fd22`  |
| 2629   | Layout 1             | `2ea64e09fd22`  |
| 2619   | Layout 1             | `2ea64e09fd22`  |
| 2612   | Layout 1             | `2ea64e09fd22`  |
| 2606   | Layout 1             | `2ea64e09fd22`  |
| 2602   | Layout 1             | `2ea64e09fd22`  |
| 2601   | Layout 1             | `2ea64e09fd22`  |
| 2592   | Layout 1             | `2ea64e09fd22`  |
| 2583   | Layout 1             | `2ea64e09fd22`  |
| 2575   | Layout 1             | `2ea64e09fd22`  |
| 2567   | Layout 1             | `2ea64e09fd22`  |
| 2560   | Layout 1             | `2ea64e09fd22`  |
| 2553   | Layout 1             | `2ea64e09fd22`  |
| 2545   | Layout 1             | `2ea64e09fd22`  |
| 2538   | Layout 1             | `2ea64e09fd22`  |
| 2529   | Layout 1             | `2ea64e09fd22`  |
| 2519   | Layout 1             | `2ea64e09fd22`  |
| 2513   | Layout 1             | `2ea64e09fd22`  |
| 2510   | Layout 1             | `2ea64e09fd22`  |
| 2507   | Layout 1             | `2ea64e09fd22`  |
| 2503   | Layout 1             | `2ea64e09fd22`  |
| 2498   | Layout 1             | `2ea64e09fd22`  |
| 2492   | Layout 1             | `2ea64e09fd22`  |
| 2487   | Layout 1             | `2ea64e09fd22`  |
| 2480   | Layout 1             | `2ea64e09fd22`  |
| 2474   | Layout 1             | `2ea64e09fd22`  |
| 2468   | Layout 1             | `2ea64e09fd22`  |
| 2460   | Layout 1             | `2ea64e09fd22`  |
| 2453   | Layout 1             | `2ea64e09fd22`  |
| 2444   | Layout 1             | `2ea64e09fd22`  |
| 2438   | Layout 1             | `2ea64e09fd22`  |
| 2434   | Layout 1             | `2ea64e09fd22`  |
| 2429   | Layout 1             | `2ea64e09fd22`  |
| 2421   | Layout 1             | `2ea64e09fd22`  |
| 2414   | Layout 1             | `2ea64e09fd22`  |
| 2407   | Layout 1             | `2ea64e09fd22`  |
| 2401   | Layout 1             | `2ea64e09fd22`  |
| 2397   | Layout 1             | `2ea64e09fd22`  |
| 2393   | Layout 1             | `2ea64e09fd22`  |
| 2384   | Layout 1             | `2ea64e09fd22`  |
| 2378   | Layout 1             | `2ea64e09fd22`  |
| 2372   | Layout 1             | `2ea64e09fd22`  |
| 2358   | Layout 1             | `2ea64e09fd22`  |
| 2352   | Layout 1             | `2ea64e09fd22`  |
| 2347   | Layout 1             | `2ea64e09fd22`  |
| 2343   | Layout 1             | `2ea64e09fd22`  |
| 2335   | Layout 1             | `2ea64e09fd22`  |
| 2327   | Layout 1             | `2ea64e09fd22`  |
| 2324   | Layout 1             | `2ea64e09fd22`  |
| 2319   | Layout 1             | `2ea64e09fd22`  |
| 2313   | Layout 1             | `2ea64e09fd22`  |
| 2308   | Layout 1             | `2ea64e09fd22`  |
| 2302   | Layout 1             | `2ea64e09fd22`  |
| 2295   | Layout 1             | `2ea64e09fd22`  |
| 2290   | Layout 1             | `2ea64e09fd22`  |
| 2284   | Layout 1             | `2ea64e09fd22`  |
| 2276   | Layout 1             | `2ea64e09fd22`  |
| 2269   | Layout 1             | `2ea64e09fd22`  |
| 2259   | Layout 1             | `2ea64e09fd22`  |
| 2250   | Layout 1             | `2ea64e09fd22`  |
| 2243   | Layout 1             | `2ea64e09fd22`  |
| 2235   | Layout 1             | `2ea64e09fd22`  |
| 2229   | Layout 1             | `2ea64e09fd22`  |
| 2224   | Layout 1             | `2ea64e09fd22`  |
| 2218   | Layout 1             | `2ea64e09fd22`  |
| 2215   | Layout 1             | `2ea64e09fd22`  |
| 2207   | Layout 1             | `2ea64e09fd22`  |
| 2203   | Layout 1             | `2ea64e09fd22`  |
| 2196   | Layout 1             | `2ea64e09fd22`  |
| 2192   | Layout 1             | `2ea64e09fd22`  |
| 2189   | Layout 1             | `2ea64e09fd22`  |
| 2183   | Layout 1             | `2ea64e09fd22`  |
| 2179   | Layout 1             | `2ea64e09fd22`  |
| 2171   | Layout 1             | `2ea64e09fd22`  |
| 2163   | Layout 1             | `2ea64e09fd22`  |
| 2156   | Layout 1             | `2ea64e09fd22`  |
| 2151   | Layout 1             | `2ea64e09fd22`  |
| 2147   | Layout 1             | `2ea64e09fd22`  |
| 2142   | Layout 1             | `2ea64e09fd22`  |
| 2138   | Layout 1             | `2ea64e09fd22`  |
| 2134   | Layout 1             | `2ea64e09fd22`  |
| 2130   | Layout 1             | `2ea64e09fd22`  |
| 2122   | Layout 1             | `2ea64e09fd22`  |
| 2107   | Layout 1             | `2ea64e09fd22`  |
| 2098   | Layout 1             | `2ea64e09fd22`  |
| 2089   | Layout 1             | `2ea64e09fd22`  |
| 2081   | Layout 1             | `2ea64e09fd22`  |
| 2073   | Layout 1             | `2ea64e09fd22`  |
| 2067   | Layout 1             | `2ea64e09fd22`  |
| 2063   | Layout 1             | `2ea64e09fd22`  |
| 2059   | Layout 1             | `2ea64e09fd22`  |
| 2052   | Layout 1             | `2ea64e09fd22`  |
| 2044   | Layout 1             | `2ea64e09fd22`  |
| 2039   | Layout 1             | `2ea64e09fd22`  |
| 2032   | Layout 1             | `2ea64e09fd22`  |
| 2025   | Layout 1             | `2ea64e09fd22`  |
| 2011   | Layout 1             | `2ea64e09fd22`  |
| 2005   | Layout 1             | `2ea64e09fd22`  |
| 2000   | Layout 1             | `2ea64e09fd22`  |
| 1996   | Layout 1             | `2ea64e09fd22`  |
| 1991   | Layout 1             | `2ea64e09fd22`  |
| 1985   | Layout 1             | `2ea64e09fd22`  |
| 1980   | Layout 1             | `2ea64e09fd22`  |
| 1969   | Layout 1             | `2ea64e09fd22`  |
| 1964   | Layout 1             | `2ea64e09fd22`  |
| 1958   | Layout 1             | `2ea64e09fd22`  |
| 1950   | Layout 1             | `2ea64e09fd22`  |
| 1945   | Layout 1             | `2ea64e09fd22`  |
| 1937   | Layout 1             | `2ea64e09fd22`  |
| 1933   | Layout 1             | `2ea64e09fd22`  |
| 1927   | Layout 1             | `2ea64e09fd22`  |
| 1921   | Layout 1             | `2ea64e09fd22`  |
| 1914   | Layout 1             | `2ea64e09fd22`  |
| 1908   | Layout 1             | `2ea64e09fd22`  |
| 1897   | Layout 1             | `2ea64e09fd22`  |
| 1892   | Layout 1             | `2ea64e09fd22`  |
| 1886   | Layout 1             | `2ea64e09fd22`  |
| 1881   | Layout 1             | `2ea64e09fd22`  |
| 1871   | Layout 1             | `2ea64e09fd22`  |
| 1866   | Layout 1             | `2ea64e09fd22`  |
| 1862   | Layout 1             | `2ea64e09fd22`  |
| 1854   | Layout 1             | `2ea64e09fd22`  |
| 1846   | Layout 1             | `2ea64e09fd22`  |
| 1838   | Layout 1             | `2ea64e09fd22`  |
| 1832   | Layout 1             | `2ea64e09fd22`  |
| 1826   | Layout 1             | `2ea64e09fd22`  |
| 1822   | Layout 1             | `2ea64e09fd22`  |
| 1818   | Layout 1             | `2ea64e09fd22`  |
| 1804   | Layout 1             | `2ea64e09fd22`  |
| 1794   | Layout 1             | `2ea64e09fd22`  |
| 1790   | Layout 1             | `2ea64e09fd22`  |
| 1784   | Layout 1             | `2ea64e09fd22`  |
| 1774   | Layout 1             | `2ea64e09fd22`  |
| 1771   | Layout 1             | `2ea64e09fd22`  |
| 1762   | Layout 1             | `2ea64e09fd22`  |
| 1759   | Layout 1             | `2ea64e09fd22`  |
| 1754   | Layout 1             | `2ea64e09fd22`  |
| 1749   | Layout 1             | `2ea64e09fd22`  |
| 1743   | Layout 1             | `2ea64e09fd22`  |
| 1737   | Layout 1             | `2ea64e09fd22`  |
| 1731   | Layout 1             | `2ea64e09fd22`  |
| 1725   | Layout 1             | `2ea64e09fd22`  |
| 1717   | Layout 1             | `2ea64e09fd22`  |
| 1710   | Layout 1             | `2ea64e09fd22`  |
| 1704   | Layout 1             | `2ea64e09fd22`  |
| 1698   | Layout 1             | `2ea64e09fd22`  |
| 1690   | Layout 1             | `2ea64e09fd22`  |
| 1685   | Layout 1             | `2ea64e09fd22`  |
| 1680   | Layout 1             | `2ea64e09fd22`  |
| 1674   | Layout 1             | `2ea64e09fd22`  |
| 1668   | Layout 1             | `2ea64e09fd22`  |
| 1659   | Layout 1             | `2ea64e09fd22`  |
| 1649   | Layout 1             | `2ea64e09fd22`  |
| 1642   | Layout 1             | `2ea64e09fd22`  |
| 1636   | Layout 1             | `2ea64e09fd22`  |
| 1628   | Layout 1             | `2ea64e09fd22`  |
| 1622   | Layout 1             | `2ea64e09fd22`  |
| 1614   | Layout 1             | `2ea64e09fd22`  |
| 1608   | Layout 1             | `2ea64e09fd22`  |
| 1602   | Layout 1             | `2ea64e09fd22`  |
| 1598   | Layout 1             | `2ea64e09fd22`  |
| 1594   | Layout 1             | `2ea64e09fd22`  |
| 1590   | Layout 1             | `2ea64e09fd22`  |
| 1587   | Layout 1             | `2ea64e09fd22`  |
| 1584   | Layout 1             | `2ea64e09fd22`  |
| 1579   | Layout 1             | `2ea64e09fd22`  |
| 1572   | Layout 1             | `2ea64e09fd22`  |
| 1565   | Layout 1             | `2ea64e09fd22`  |
| 1559   | Layout 1             | `2ea64e09fd22`  |
| 1554   | Layout 1             | `2ea64e09fd22`  |
| 1547   | Layout 1             | `2ea64e09fd22`  |
| 1537   | Layout 1             | `2ea64e09fd22`  |
| 1529   | Layout 1             | `2ea64e09fd22`  |
| 1524   | Layout 1             | `2ea64e09fd22`  |
| 1519   | Layout 1             | `2ea64e09fd22`  |
| 1509   | Layout 1             | `2ea64e09fd22`  |
| 1506   | Layout 1             | `2ea64e09fd22`  |
| 1504   | Layout 1             | `2ea64e09fd22`  |
| 1500   | Layout 1             | `2ea64e09fd22`  |
| 1493   | Layout 1             | `2ea64e09fd22`  |
| 1489   | Layout 1             | `2ea64e09fd22`  |
| 1485   | Layout 1             | `2ea64e09fd22`  |
| 1481   | Layout 1             | `2ea64e09fd22`  |
| 1474   | Layout 1             | `2ea64e09fd22`  |
| 1466   | Layout 1             | `2ea64e09fd22`  |
| 1462   | Layout 1             | `2ea64e09fd22`  |
| 1459   | Layout 1             | `2ea64e09fd22`  |
| 1453   | Layout 1             | `2ea64e09fd22`  |
| 1450   | Layout 1             | `2ea64e09fd22`  |
| 1445   | Layout 1             | `2ea64e09fd22`  |
| 1439   | Layout 1             | `2ea64e09fd22`  |
| 1433   | Layout 1             | `2ea64e09fd22`  |
| 1430   | Layout 1             | `2ea64e09fd22`  |
| 1426   | Layout 1             | `2ea64e09fd22`  |
| 1421   | Layout 1             | `2ea64e09fd22`  |
| 1417   | Layout 1             | `2ea64e09fd22`  |
| 1416   | Layout 1             | `2ea64e09fd22`  |
| 1409   | Layout 1             | `2ea64e09fd22`  |
| 1405   | Layout 1             | `2ea64e09fd22`  |
| 1401   | Layout 1             | `2ea64e09fd22`  |
| 1396   | Layout 1             | `2ea64e09fd22`  |
| 1391   | Layout 1             | `2ea64e09fd22`  |
| 1390   | Layout 1             | `2ea64e09fd22`  |
| 1386   | Layout 1             | `2ea64e09fd22`  |
| 1381   | Layout 1             | `2ea64e09fd22`  |
| 1379   | Layout 1             | `2ea64e09fd22`  |
| 1372   | Layout 1             | `2ea64e09fd22`  |
| 1366   | Layout 1             | `2ea64e09fd22`  |
| 1364   | Layout 1             | `2ea64e09fd22`  |
| 1363   | Layout 1             | `2ea64e09fd22`  |
| 1360   | Layout 1             | `2ea64e09fd22`  |
| 1358   | Layout 1             | `2ea64e09fd22`  |
| 1355   | Layout 1             | `2ea64e09fd22`  |
| 1351   | Layout 1             | `2ea64e09fd22`  |
| 1348   | Layout 1             | `2ea64e09fd22`  |
| 1346   | Layout 1             | `2ea64e09fd22`  |
| 1341   | No documented layout | `2ea64e09fd22`  |
| 1340   | No documented layout | `2ea64e09fd22`  |
| 1338   | No documented layout | `2ea64e09fd22`  |
| 1335   | No documented layout | `2ea64e09fd22`  |
| 1333   | No documented layout | `2ea64e09fd22`  |
| 1329   | No documented layout | `2ea64e09fd22`  |
| 1327   | No documented layout | `2ea64e09fd22`  |
| 1324   | No documented layout | `2ea64e09fd22`  |
| 1321   | No documented layout | `2ea64e09fd22`  |
| 1319   | No documented layout | `2ea64e09fd22`  |
| 1318   | No documented layout | `2ea64e09fd22`  |
| 1316   | No documented layout | `2ea64e09fd22`  |
| 1313   | No documented layout | `2ea64e09fd22`  |
| 1311   | No documented layout | `2ea64e09fd22`  |
| 1309   | No documented layout | `2ea64e09fd22`  |
| 1304   | No documented layout | `2ea64e09fd22`  |
| 1292   | No documented layout | `2ea64e09fd22`  |
| 1286   | No documented layout | `2ea64e09fd22`  |
| 1280   | No file              | `2ea64e09fd22`  |
| 1276   | No file              | `2ea64e09fd22`  |
| 1267   | No documented layout | `2ea64e09fd22`  |
| 1261   | No documented layout | `2ea64e09fd22`  |
| 1256   | No file              | `2ea64e09fd22`  |
| 1250   | No file              | `2ea64e09fd22`  |
| 1246   | No file              | `2ea64e09fd22`  |
| 1239   | No file              | `2ea64e09fd22`  |
| 1230   | No file              | `2ea64e09fd22`  |
| 1226   | No file              | `2ea64e09fd22`  |
| 1220   | No file              | `2ea64e09fd22`  |
| 1217   | No file              | `2ea64e09fd22`  |
| 1211   | No file              | `2ea64e09fd22`  |
| 1210   | No file              | `2ea64e09fd22`  |
| 1208   | No file              | `2ea64e09fd22`  |
| 1203   | No file              | `2ea64e09fd22`  |
| 1197   | No file              | `2ea64e09fd22`  |
| 1194   | No file              | `2ea64e09fd22`  |
| 1192   | No file              | `2ea64e09fd22`  |
| 1187   | No file              | `2ea64e09fd22`  |
| 1183   | No file              | `2ea64e09fd22`  |
| 1177   | No file              | `2ea64e09fd22`  |
| 1173   | No file              | `2ea64e09fd22`  |
| 1167   | No file              | `2ea64e09fd22`  |
| 1164   | No file              | `2ea64e09fd22`  |
| 1156   | No file              | `2ea64e09fd22`  |
| 1149   | No file              | `2ea64e09fd22`  |
| 1144   | No file              | `2ea64e09fd22`  |
| 1137   | No file              | `2ea64e09fd22`  |
| 1132   | No file              | `2ea64e09fd22`  |
| 1127   | No file              | `2ea64e09fd22`  |
| 1122   | No file              | `2ea64e09fd22`  |
| 1118   | No file              | `2ea64e09fd22`  |
| 1114   | No file              | `2ea64e09fd22`  |
| 1109   | No file              | `2ea64e09fd22`  |
| 1102   | No file              | `2ea64e09fd22`  |
| 1096   | No file              | `2ea64e09fd22`  |
| 1088   | No file              | `2ea64e09fd22`  |
| 1081   | No file              | `2ea64e09fd22`  |
| 1076   | No file              | `2ea64e09fd22`  |
| 1069   | No file              | `2ea64e09fd22`  |
| 1064   | No file              | `2ea64e09fd22`  |
| 1058   | No file              | `2ea64e09fd22`  |
| 1051   | No file              | `2ea64e09fd22`  |
| 1044   | No file              | `2ea64e09fd22`  |
| 1036   | No file              | `2ea64e09fd22`  |
| 1026   | No file              | `2ea64e09fd22`  |
| 1016   | No file              | `2ea64e09fd22`  |
| 1009   | No file              | `2ea64e09fd22`  |
| 1005   | No file              | `2ea64e09fd22`  |
| 1000   | No file              | `2ea64e09fd22`  |
| 998    | No file              | `2ea64e09fd22`  |
| 990    | No file              | `2ea64e09fd22`  |
| 979    | No file              | `2ea64e09fd22`  |
| 972    | No file              | `2ea64e09fd22`  |
| 963    | No file              | `2ea64e09fd22`  |
| 955    | No file              | `2ea64e09fd22`  |
| 946    | No file              | `2ea64e09fd22`  |
| 938    | No file              | `2ea64e09fd22`  |
| 927    | No file              | `2ea64e09fd22`  |
| 911    | No file              | `2ea64e09fd22`  |
| 904    | No file              | `2ea64e09fd22`  |
| 899    | No file              | `2ea64e09fd22`  |
| 894    | No file              | `2ea64e09fd22`  |
| 885    | No file              | `2ea64e09fd22`  |
| 879    | No file              | `2ea64e09fd22`  |
| 872    | No file              | `2ea64e09fd22`  |
| 864    | No file              | `2ea64e09fd22`  |
| 855    | No file              | `2ea64e09fd22`  |
| 853    | No file              | `2ea64e09fd22`  |
| 845    | No file              | `2ea64e09fd22`  |
| 837    | No file              | `2ea64e09fd22`  |
| 829    | No file              | `2ea64e09fd22`  |
| 822    | No file              | `2ea64e09fd22`  |
| 814    | No file              | `2ea64e09fd22`  |
| 805    | No file              | `2ea64e09fd22`  |
| 794    | No file              | `2ea64e09fd22`  |
| 787    | No file              | `2ea64e09fd22`  |
| 780    | No file              | `2ea64e09fd22`  |
| 771    | No file              | `2ea64e09fd22`  |
| 760    | No file              | `2ea64e09fd22`  |
| 748    | No file              | `2ea64e09fd22`  |
| 741    | No file              | `2ea64e09fd22`  |
| 736    | No file              | `2ea64e09fd22`  |
| 731    | No file              | `2ea64e09fd22`  |
| 723    | No file              | `2ea64e09fd22`  |
| 711    | No file              | `2ea64e09fd22`  |
| 707    | No file              | `2ea64e09fd22`  |
| 697    | No file              | `2ea64e09fd22`  |
| 689    | No file              | `2ea64e09fd22`  |
| 683    | No file              | `2ea64e09fd22`  |
| 678    | No file              | `2ea64e09fd22`  |
| 670    | No file              | `2ea64e09fd22`  |
| 661    | No file              | `2ea64e09fd22`  |
| 656    | No file              | `2ea64e09fd22`  |
| 652    | No file              | `2ea64e09fd22`  |
| 643    | No file              | `2ea64e09fd22`  |
| 637    | No file              | `2ea64e09fd22`  |
| 630    | No file              | `2ea64e09fd22`  |
| 627    | No file              | `2ea64e09fd22`  |
| 621    | No file              | `2ea64e09fd22`  |
| 617    | No file              | `2ea64e09fd22`  |
| 615    | No file              | `2ea64e09fd22`  |
| 606    | No file              | `2ea64e09fd22`  |
| 599    | No file              | `2ea64e09fd22`  |
| 592    | No file              | `2ea64e09fd22`  |
| 586    | No file              | `2ea64e09fd22`  |
| 577    | No file              | `2ea64e09fd22`  |
| 569    | No file              | `2ea64e09fd22`  |
| 561    | No file              | `2ea64e09fd22`  |
| 554    | No file              | `2ea64e09fd22`  |
| 542    | No file              | `2ea64e09fd22`  |
| 532    | No file              | `2ea64e09fd22`  |
| 531    | No file              | `2ea64e09fd22`  |
| 526    | No file              | `2ea64e09fd22`  |
| 521    | No file              | `2ea64e09fd22`  |
| 517    | No file              | `2ea64e09fd22`  |
| 510    | No file              | `2ea64e09fd22`  |
| 508    | No file              | `2ea64e09fd22`  |
| 504    | No file              | `2ea64e09fd22`  |
| 497    | No file              | `2ea64e09fd22`  |
| 491    | No file              | `2ea64e09fd22`  |
| 485    | No file              | `2ea64e09fd22`  |
| 478    | No file              | `2ea64e09fd22`  |
| 472    | No file              | `2ea64e09fd22`  |
| 466    | No file              | `2ea64e09fd22`  |
| 457    | No file              | `2ea64e09fd22`  |
| 452    | No file              | `2ea64e09fd22`  |
| 449    | No file              | `2ea64e09fd22`  |
| 435    | No file              | `2ea64e09fd22`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                               |
| ---------------------- | -------- | -------------------------------------------------- |
| `petgradeoffset.dbss`  | Required | `(species,variant) → (data_offset, data_size)` lookup |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                                          |
| ------- | ------------- | ------- | -------------------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records (observed: 203 before 2026-09-27, 282 after) |
| `+0x04` | Record[count] | records | See Record                                                     |

### Record (12 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | key         | `(species << 8) \| variant`; low byte = variant, high byte = species |
| `+0x02` | u16  | unknown_02  | Always 0                                                           |
| `+0x04` | u16  | key_dup     | Duplicate of `key`                                                 |
| `+0x06` | u16  | unknown_06  | Always 0                                                           |
| `+0x08` | u32  | grade       | Pet grade for this (species, variant): 1 Classic, 2 Rare, 3 Premium, 4 Event, 5 Special, see In-Game Checks |

> The combined key is `(species << 8) | variant`, stored as a u16 followed by a zero u16. This matches the key format used in `petgradeoffset.dbss`.

### `petgradeoffset.dbss`

Provides O(1) lookup by (species, variant) key, one entry per main-file record.

| Offset  | Type              | Field | Notes                            |
| ------- | ----------------- | ----- | -------------------------------- |
| `+0x00` | u32               | count | Must equal `petgrade.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                   |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                    |
| ------- | ---- | ----------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | key         | `(species << 8) \| variant`; low byte = variant, high byte = species     |
| `+0x02` | u16  | unknown_02  | Always 0                                                                 |
| `+0x04` | u32  | data_offset | Absolute byte offset in `petgrade.dbss` past the 4-byte key prefix      |
| `+0x08` | u32  | data_size   | Always 8 (= record size minus the 4-byte key prefix)                    |

`record_start = data_offset - 4` gives the position of the full 12-byte record in the main file.
The parser reads `key` and `unknown_02` as one u32 (`parse_bare_u32_offset_rows()`).

## Joining with pet.dbss

To enrich a `pet.dbss` record with its `grade`:

```python
lookup_key = (species << 8) | variant  # both from pet.dbss record
grade = grade_map.get((species, variant), None)
```

where `grade_map` is built from `petgradeoffset.dbss` as `{(species, variant): grade}`.

## Notes

- Before the 2026-09-27 client update: 203 (species, variant) pairs for 1,782 pet records, about 8.8 records per pair across pet tiers. After it: 282 pairs for 2,009 pet records; all 79 new pairs have grade 2.
- `grade` observed range: 1–6. Values 1–5 map to Classic, Rare, Premium, Event, Special: the order of `_gradeStrConfig` in `panel_window_petfusion_all.luac` (`LUA_PETCOMPOSE_SAME_GRADETYPE_CLASSIC_TITLE`, `_LIMITED_` shown as "RARE", `_PREMIUM_`, `_EVENT_`, `_SPECIAL_`). Grade 4 is Kuku, Young Rauno, Young Fogan and Young Pomi. Value 6 remains unconfirmed.
- Record order in the main file differs from offset file order (the offset file is an arbitrary-order index, not sequential).
- The key encoding `(species << 8) | variant` appears only in this file pair; `pet.dbss` stores `variant` and `species` as separate bytes at `+0x02` and `+0x03`.

## In-Game Checks

### Grade Value 6

Needs item (all):

- [[Pet] Pit-A-Pat Mole](https://bdocodex.com/us/item/47983/)
- [[Pet] Young Crimson Dragon](https://bdocodex.com/us/item/18480/)

Values 1 to 5 map to the five fusion window grade titles, but the Lua lists no sixth title, and only the 5 Mole records carry value 6. They are the Pit-A-Pat Mole (item 47983, pets 55749 to 55752 and 56594). bdocodex (2026-10-07) shows the Pit-A-Pat Mole as Type: Special. Its pet type follows this field, since it shows Young Rauno (grade 4) as Event and Young Crimson Dragon (grade 5) as Special, but it could map 6 to Special by its own fallback. Its item page also says the Mole "can only be Exchanged with pets of the same kind", a line the Young Crimson Dragon page does not carry.

Put the Pit-A-Pat Mole in the pet exchange window and read the grade title, then try to add the Young Crimson Dragon. A Special title and an accepted Dragon mean 6 is a second Special value. No title, or a window that takes only other Moles, means 6 is a grade of its own that the fusion window has no title for.
