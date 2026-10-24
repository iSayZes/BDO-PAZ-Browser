# `yachtdicecard.dbss` Format

## Purpose

A second Yar! card list: each row is one card with a symbol and an eye
value from `1` to `10`, and no picture. Unlike the
[`yachtbasecard.dbss`](yachtbasecard_dbss.md) cards, no other Yar! table
names these keys. `yachtdicecardoffset.dbss` is the index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ------------- | --------- |
| 1      | 1614 and later | 3483    | `yachtdicecard.dbss`       | 404   | 40 Row        | 10        |
| 1      | 1614 and later | 3483    | `yachtdicecardoffset.dbss` | 484   | 40 Offset Row | 12        |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 1      | `yachtdicecard.dbss`       | 404 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtdicecardoffset.dbss` | 484 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `5bf04d4bedf5`  |
| 3482   | Layout 1 | `5bf04d4bedf5`  |
| 3474   | Layout 1 | `5bf04d4bedf5`  |
| 3473   | Layout 1 | `5bf04d4bedf5`  |
| 3464   | Layout 1 | `5bf04d4bedf5`  |
| 3458   | Layout 1 | `5bf04d4bedf5`  |
| 3454   | Layout 1 | `5bf04d4bedf5`  |
| 3444   | Layout 1 | `5bf04d4bedf5`  |
| 3435   | Layout 1 | `5bf04d4bedf5`  |
| 3426   | Layout 1 | `5bf04d4bedf5`  |
| 3418   | Layout 1 | `5bf04d4bedf5`  |
| 3412   | Layout 1 | `5bf04d4bedf5`  |
| 3402   | Layout 1 | `5bf04d4bedf5`  |
| 3396   | Layout 1 | `5bf04d4bedf5`  |
| 3387   | Layout 1 | `5bf04d4bedf5`  |
| 3381   | Layout 1 | `5bf04d4bedf5`  |
| 3373   | Layout 1 | `5bf04d4bedf5`  |
| 3364   | Layout 1 | `5bf04d4bedf5`  |
| 3356   | Layout 1 | `5bf04d4bedf5`  |
| 3349   | Layout 1 | `5bf04d4bedf5`  |
| 3342   | Layout 1 | `5bf04d4bedf5`  |
| 3335   | Layout 1 | `5bf04d4bedf5`  |
| 3326   | Layout 1 | `5bf04d4bedf5`  |
| 3321   | Layout 1 | `5bf04d4bedf5`  |
| 3314   | Layout 1 | `5bf04d4bedf5`  |
| 3303   | Layout 1 | `5bf04d4bedf5`  |
| 3302   | Layout 1 | `5bf04d4bedf5`  |
| 3293   | Layout 1 | `5bf04d4bedf5`  |
| 3283   | Layout 1 | `5bf04d4bedf5`  |
| 3275   | Layout 1 | `5bf04d4bedf5`  |
| 3267   | Layout 1 | `5bf04d4bedf5`  |
| 3258   | Layout 1 | `5bf04d4bedf5`  |
| 3251   | Layout 1 | `5bf04d4bedf5`  |
| 3242   | Layout 1 | `5bf04d4bedf5`  |
| 3235   | Layout 1 | `5bf04d4bedf5`  |
| 3229   | Layout 1 | `5bf04d4bedf5`  |
| 3212   | Layout 1 | `5bf04d4bedf5`  |
| 3203   | Layout 1 | `5bf04d4bedf5`  |
| 3193   | Layout 1 | `5bf04d4bedf5`  |
| 3186   | Layout 1 | `5bf04d4bedf5`  |
| 3177   | Layout 1 | `5bf04d4bedf5`  |
| 3169   | Layout 1 | `5bf04d4bedf5`  |
| 3158   | Layout 1 | `5bf04d4bedf5`  |
| 3151   | Layout 1 | `5bf04d4bedf5`  |
| 3144   | Layout 1 | `5bf04d4bedf5`  |
| 3133   | Layout 1 | `5bf04d4bedf5`  |
| 3125   | Layout 1 | `5bf04d4bedf5`  |
| 3118   | Layout 1 | `5bf04d4bedf5`  |
| 3111   | Layout 1 | `5bf04d4bedf5`  |
| 3103   | Layout 1 | `5bf04d4bedf5`  |
| 3095   | Layout 1 | `5bf04d4bedf5`  |
| 3086   | Layout 1 | `5bf04d4bedf5`  |
| 3072   | Layout 1 | `5bf04d4bedf5`  |
| 3062   | Layout 1 | `5bf04d4bedf5`  |
| 3052   | Layout 1 | `5bf04d4bedf5`  |
| 3045   | Layout 1 | `5bf04d4bedf5`  |
| 3037   | Layout 1 | `5bf04d4bedf5`  |
| 3030   | Layout 1 | `5bf04d4bedf5`  |
| 3021   | Layout 1 | `5bf04d4bedf5`  |
| 3012   | Layout 1 | `5bf04d4bedf5`  |
| 3002   | Layout 1 | `5bf04d4bedf5`  |
| 2995   | Layout 1 | `5bf04d4bedf5`  |
| 2987   | Layout 1 | `5bf04d4bedf5`  |
| 2978   | Layout 1 | `5bf04d4bedf5`  |
| 2970   | Layout 1 | `5bf04d4bedf5`  |
| 2959   | Layout 1 | `5bf04d4bedf5`  |
| 2951   | Layout 1 | `5bf04d4bedf5`  |
| 2942   | Layout 1 | `5bf04d4bedf5`  |
| 2935   | Layout 1 | `5bf04d4bedf5`  |
| 2932   | Layout 1 | `5bf04d4bedf5`  |
| 2923   | Layout 1 | `5bf04d4bedf5`  |
| 2919   | Layout 1 | `5bf04d4bedf5`  |
| 2907   | Layout 1 | `5bf04d4bedf5`  |
| 2900   | Layout 1 | `5bf04d4bedf5`  |
| 2891   | Layout 1 | `5bf04d4bedf5`  |
| 2882   | Layout 1 | `5bf04d4bedf5`  |
| 2872   | Layout 1 | `5bf04d4bedf5`  |
| 2863   | Layout 1 | `5bf04d4bedf5`  |
| 2855   | Layout 1 | `5bf04d4bedf5`  |
| 2849   | Layout 1 | `5bf04d4bedf5`  |
| 2844   | Layout 1 | `5bf04d4bedf5`  |
| 2834   | Layout 1 | `5bf04d4bedf5`  |
| 2825   | Layout 1 | `5bf04d4bedf5`  |
| 2819   | Layout 1 | `5bf04d4bedf5`  |
| 2811   | Layout 1 | `5bf04d4bedf5`  |
| 2803   | Layout 1 | `5bf04d4bedf5`  |
| 2794   | Layout 1 | `5bf04d4bedf5`  |
| 2783   | Layout 1 | `5bf04d4bedf5`  |
| 2774   | Layout 1 | `5bf04d4bedf5`  |
| 2765   | Layout 1 | `5bf04d4bedf5`  |
| 2756   | Layout 1 | `5bf04d4bedf5`  |
| 2750   | Layout 1 | `5bf04d4bedf5`  |
| 2743   | Layout 1 | `5bf04d4bedf5`  |
| 2736   | Layout 1 | `5bf04d4bedf5`  |
| 2726   | Layout 1 | `5bf04d4bedf5`  |
| 2717   | Layout 1 | `5bf04d4bedf5`  |
| 2709   | Layout 1 | `5bf04d4bedf5`  |
| 2703   | Layout 1 | `5bf04d4bedf5`  |
| 2695   | Layout 1 | `5bf04d4bedf5`  |
| 2684   | Layout 1 | `5bf04d4bedf5`  |
| 2672   | Layout 1 | `5bf04d4bedf5`  |
| 2665   | Layout 1 | `5bf04d4bedf5`  |
| 2657   | Layout 1 | `5bf04d4bedf5`  |
| 2649   | Layout 1 | `5bf04d4bedf5`  |
| 2644   | Layout 1 | `5bf04d4bedf5`  |
| 2637   | Layout 1 | `5bf04d4bedf5`  |
| 2629   | Layout 1 | `5bf04d4bedf5`  |
| 2619   | Layout 1 | `5bf04d4bedf5`  |
| 2612   | Layout 1 | `5bf04d4bedf5`  |
| 2606   | Layout 1 | `5bf04d4bedf5`  |
| 2602   | Layout 1 | `5bf04d4bedf5`  |
| 2601   | Layout 1 | `5bf04d4bedf5`  |
| 2592   | Layout 1 | `5bf04d4bedf5`  |
| 2583   | Layout 1 | `5bf04d4bedf5`  |
| 2575   | Layout 1 | `5bf04d4bedf5`  |
| 2567   | Layout 1 | `5bf04d4bedf5`  |
| 2560   | Layout 1 | `5bf04d4bedf5`  |
| 2553   | Layout 1 | `5bf04d4bedf5`  |
| 2545   | Layout 1 | `5bf04d4bedf5`  |
| 2538   | Layout 1 | `5bf04d4bedf5`  |
| 2529   | Layout 1 | `5bf04d4bedf5`  |
| 2519   | Layout 1 | `5bf04d4bedf5`  |
| 2513   | Layout 1 | `5bf04d4bedf5`  |
| 2510   | Layout 1 | `5bf04d4bedf5`  |
| 2507   | Layout 1 | `5bf04d4bedf5`  |
| 2503   | Layout 1 | `5bf04d4bedf5`  |
| 2498   | Layout 1 | `5bf04d4bedf5`  |
| 2492   | Layout 1 | `5bf04d4bedf5`  |
| 2487   | Layout 1 | `5bf04d4bedf5`  |
| 2480   | Layout 1 | `5bf04d4bedf5`  |
| 2474   | Layout 1 | `5bf04d4bedf5`  |
| 2468   | Layout 1 | `5bf04d4bedf5`  |
| 2460   | Layout 1 | `5bf04d4bedf5`  |
| 2453   | Layout 1 | `5bf04d4bedf5`  |
| 2444   | Layout 1 | `5bf04d4bedf5`  |
| 2438   | Layout 1 | `5bf04d4bedf5`  |
| 2434   | Layout 1 | `5bf04d4bedf5`  |
| 2429   | Layout 1 | `5bf04d4bedf5`  |
| 2421   | Layout 1 | `5bf04d4bedf5`  |
| 2414   | Layout 1 | `5bf04d4bedf5`  |
| 2407   | Layout 1 | `5bf04d4bedf5`  |
| 2401   | Layout 1 | `5bf04d4bedf5`  |
| 2397   | Layout 1 | `5bf04d4bedf5`  |
| 2393   | Layout 1 | `5bf04d4bedf5`  |
| 2384   | Layout 1 | `5bf04d4bedf5`  |
| 2378   | Layout 1 | `5bf04d4bedf5`  |
| 2372   | Layout 1 | `5bf04d4bedf5`  |
| 2358   | Layout 1 | `5bf04d4bedf5`  |
| 2352   | Layout 1 | `5bf04d4bedf5`  |
| 2347   | Layout 1 | `5bf04d4bedf5`  |
| 2343   | Layout 1 | `5bf04d4bedf5`  |
| 2335   | Layout 1 | `5bf04d4bedf5`  |
| 2327   | Layout 1 | `5bf04d4bedf5`  |
| 2324   | Layout 1 | `5bf04d4bedf5`  |
| 2319   | Layout 1 | `5bf04d4bedf5`  |
| 2313   | Layout 1 | `5bf04d4bedf5`  |
| 2308   | Layout 1 | `5bf04d4bedf5`  |
| 2302   | Layout 1 | `5bf04d4bedf5`  |
| 2295   | Layout 1 | `5bf04d4bedf5`  |
| 2290   | Layout 1 | `5bf04d4bedf5`  |
| 2284   | Layout 1 | `5bf04d4bedf5`  |
| 2276   | Layout 1 | `5bf04d4bedf5`  |
| 2269   | Layout 1 | `5bf04d4bedf5`  |
| 2259   | Layout 1 | `5bf04d4bedf5`  |
| 2250   | Layout 1 | `5bf04d4bedf5`  |
| 2243   | Layout 1 | `5bf04d4bedf5`  |
| 2235   | Layout 1 | `5bf04d4bedf5`  |
| 2229   | Layout 1 | `5bf04d4bedf5`  |
| 2224   | Layout 1 | `5bf04d4bedf5`  |
| 2218   | Layout 1 | `5bf04d4bedf5`  |
| 2215   | Layout 1 | `5bf04d4bedf5`  |
| 2207   | Layout 1 | `5bf04d4bedf5`  |
| 2203   | Layout 1 | `5bf04d4bedf5`  |
| 2196   | Layout 1 | `5bf04d4bedf5`  |
| 2192   | Layout 1 | `5bf04d4bedf5`  |
| 2189   | Layout 1 | `5bf04d4bedf5`  |
| 2183   | Layout 1 | `5bf04d4bedf5`  |
| 2179   | Layout 1 | `5bf04d4bedf5`  |
| 2171   | Layout 1 | `5bf04d4bedf5`  |
| 2163   | Layout 1 | `5bf04d4bedf5`  |
| 2156   | Layout 1 | `5bf04d4bedf5`  |
| 2151   | Layout 1 | `5bf04d4bedf5`  |
| 2147   | Layout 1 | `5bf04d4bedf5`  |
| 2142   | Layout 1 | `5bf04d4bedf5`  |
| 2138   | Layout 1 | `5bf04d4bedf5`  |
| 2134   | Layout 1 | `5bf04d4bedf5`  |
| 2130   | Layout 1 | `5bf04d4bedf5`  |
| 2122   | Layout 1 | `5bf04d4bedf5`  |
| 2107   | Layout 1 | `5bf04d4bedf5`  |
| 2098   | Layout 1 | `5bf04d4bedf5`  |
| 2089   | Layout 1 | `5bf04d4bedf5`  |
| 2081   | Layout 1 | `5bf04d4bedf5`  |
| 2073   | Layout 1 | `5bf04d4bedf5`  |
| 2067   | Layout 1 | `5bf04d4bedf5`  |
| 2063   | Layout 1 | `5bf04d4bedf5`  |
| 2059   | Layout 1 | `5bf04d4bedf5`  |
| 2052   | Layout 1 | `5bf04d4bedf5`  |
| 2044   | Layout 1 | `5bf04d4bedf5`  |
| 2039   | Layout 1 | `5bf04d4bedf5`  |
| 2032   | Layout 1 | `5bf04d4bedf5`  |
| 2025   | Layout 1 | `5bf04d4bedf5`  |
| 2011   | Layout 1 | `5bf04d4bedf5`  |
| 2005   | Layout 1 | `5bf04d4bedf5`  |
| 2000   | Layout 1 | `5bf04d4bedf5`  |
| 1996   | Layout 1 | `5bf04d4bedf5`  |
| 1991   | Layout 1 | `5bf04d4bedf5`  |
| 1985   | Layout 1 | `5bf04d4bedf5`  |
| 1980   | Layout 1 | `5bf04d4bedf5`  |
| 1969   | Layout 1 | `5bf04d4bedf5`  |
| 1964   | Layout 1 | `5bf04d4bedf5`  |
| 1958   | Layout 1 | `5bf04d4bedf5`  |
| 1950   | Layout 1 | `5bf04d4bedf5`  |
| 1945   | Layout 1 | `5bf04d4bedf5`  |
| 1937   | Layout 1 | `5bf04d4bedf5`  |
| 1933   | Layout 1 | `5bf04d4bedf5`  |
| 1927   | Layout 1 | `5bf04d4bedf5`  |
| 1921   | Layout 1 | `5bf04d4bedf5`  |
| 1914   | Layout 1 | `5bf04d4bedf5`  |
| 1908   | Layout 1 | `5bf04d4bedf5`  |
| 1897   | Layout 1 | `5bf04d4bedf5`  |
| 1892   | Layout 1 | `5bf04d4bedf5`  |
| 1886   | Layout 1 | `5bf04d4bedf5`  |
| 1881   | Layout 1 | `5bf04d4bedf5`  |
| 1871   | Layout 1 | `5bf04d4bedf5`  |
| 1866   | Layout 1 | `5bf04d4bedf5`  |
| 1862   | Layout 1 | `5bf04d4bedf5`  |
| 1854   | Layout 1 | `5bf04d4bedf5`  |
| 1846   | Layout 1 | `5bf04d4bedf5`  |
| 1838   | Layout 1 | `5bf04d4bedf5`  |
| 1832   | Layout 1 | `5bf04d4bedf5`  |
| 1826   | Layout 1 | `5bf04d4bedf5`  |
| 1822   | Layout 1 | `5bf04d4bedf5`  |
| 1818   | Layout 1 | `5bf04d4bedf5`  |
| 1804   | Layout 1 | `5bf04d4bedf5`  |
| 1794   | Layout 1 | `5bf04d4bedf5`  |
| 1790   | Layout 1 | `5bf04d4bedf5`  |
| 1784   | Layout 1 | `5bf04d4bedf5`  |
| 1774   | Layout 1 | `5bf04d4bedf5`  |
| 1771   | Layout 1 | `5bf04d4bedf5`  |
| 1762   | Layout 1 | `5bf04d4bedf5`  |
| 1759   | Layout 1 | `5bf04d4bedf5`  |
| 1754   | Layout 1 | `5bf04d4bedf5`  |
| 1749   | Layout 1 | `5bf04d4bedf5`  |
| 1743   | Layout 1 | `5bf04d4bedf5`  |
| 1737   | Layout 1 | `5bf04d4bedf5`  |
| 1731   | Layout 1 | `5bf04d4bedf5`  |
| 1725   | Layout 1 | `5bf04d4bedf5`  |
| 1717   | Layout 1 | `5bf04d4bedf5`  |
| 1710   | Layout 1 | `5bf04d4bedf5`  |
| 1704   | Layout 1 | `5bf04d4bedf5`  |
| 1698   | Layout 1 | `5bf04d4bedf5`  |
| 1690   | Layout 1 | `5bf04d4bedf5`  |
| 1685   | Layout 1 | `5bf04d4bedf5`  |
| 1680   | Layout 1 | `5bf04d4bedf5`  |
| 1674   | Layout 1 | `5bf04d4bedf5`  |
| 1668   | Layout 1 | `5bf04d4bedf5`  |
| 1659   | Layout 1 | `5bf04d4bedf5`  |
| 1649   | Layout 1 | `5bf04d4bedf5`  |
| 1642   | Layout 1 | `5bf04d4bedf5`  |
| 1636   | Layout 1 | `5bf04d4bedf5`  |
| 1628   | Layout 1 | `5bf04d4bedf5`  |
| 1622   | Layout 1 | `5bf04d4bedf5`  |
| 1614   | Layout 1 | `5bf04d4bedf5`  |
| 1608   | No file  | `5bf04d4bedf5`  |
| 1602   | No file  | `5bf04d4bedf5`  |
| 1598   | No file  | `5bf04d4bedf5`  |
| 1594   | No file  | `5bf04d4bedf5`  |
| 1590   | No file  | `5bf04d4bedf5`  |
| 1587   | No file  | `5bf04d4bedf5`  |
| 1584   | No file  | `5bf04d4bedf5`  |
| 1579   | No file  | `5bf04d4bedf5`  |
| 1572   | No file  | `5bf04d4bedf5`  |
| 1565   | No file  | `5bf04d4bedf5`  |
| 1559   | No file  | `5bf04d4bedf5`  |
| 1554   | No file  | `5bf04d4bedf5`  |
| 1547   | No file  | `5bf04d4bedf5`  |
| 1537   | No file  | `5bf04d4bedf5`  |
| 1529   | No file  | `5bf04d4bedf5`  |
| 1524   | No file  | `5bf04d4bedf5`  |
| 1519   | No file  | `5bf04d4bedf5`  |
| 1509   | No file  | `5bf04d4bedf5`  |
| 1506   | No file  | `5bf04d4bedf5`  |
| 1504   | No file  | `5bf04d4bedf5`  |
| 1500   | No file  | `5bf04d4bedf5`  |
| 1493   | No file  | `5bf04d4bedf5`  |
| 1489   | No file  | `5bf04d4bedf5`  |
| 1485   | No file  | `5bf04d4bedf5`  |
| 1481   | No file  | `5bf04d4bedf5`  |
| 1474   | No file  | `5bf04d4bedf5`  |
| 1466   | No file  | `5bf04d4bedf5`  |
| 1462   | No file  | `5bf04d4bedf5`  |
| 1459   | No file  | `5bf04d4bedf5`  |
| 1453   | No file  | `5bf04d4bedf5`  |
| 1450   | No file  | `5bf04d4bedf5`  |
| 1445   | No file  | `5bf04d4bedf5`  |
| 1439   | No file  | `5bf04d4bedf5`  |
| 1433   | No file  | `5bf04d4bedf5`  |
| 1430   | No file  | `5bf04d4bedf5`  |
| 1426   | No file  | `5bf04d4bedf5`  |
| 1421   | No file  | `5bf04d4bedf5`  |
| 1417   | No file  | `5bf04d4bedf5`  |
| 1416   | No file  | `5bf04d4bedf5`  |
| 1409   | No file  | `5bf04d4bedf5`  |
| 1405   | No file  | `5bf04d4bedf5`  |
| 1401   | No file  | `5bf04d4bedf5`  |
| 1396   | No file  | `5bf04d4bedf5`  |
| 1391   | No file  | `5bf04d4bedf5`  |
| 1390   | No file  | `5bf04d4bedf5`  |
| 1386   | No file  | `5bf04d4bedf5`  |
| 1381   | No file  | `5bf04d4bedf5`  |
| 1379   | No file  | `5bf04d4bedf5`  |
| 1372   | No file  | `5bf04d4bedf5`  |
| 1366   | No file  | `5bf04d4bedf5`  |
| 1364   | No file  | `5bf04d4bedf5`  |
| 1363   | No file  | `5bf04d4bedf5`  |
| 1360   | No file  | `5bf04d4bedf5`  |
| 1358   | No file  | `5bf04d4bedf5`  |
| 1355   | No file  | `5bf04d4bedf5`  |
| 1351   | No file  | `5bf04d4bedf5`  |
| 1348   | No file  | `5bf04d4bedf5`  |
| 1346   | No file  | `5bf04d4bedf5`  |
| 1341   | No file  | `5bf04d4bedf5`  |
| 1340   | No file  | `5bf04d4bedf5`  |
| 1338   | No file  | `5bf04d4bedf5`  |
| 1335   | No file  | `5bf04d4bedf5`  |
| 1333   | No file  | `5bf04d4bedf5`  |
| 1329   | No file  | `5bf04d4bedf5`  |
| 1327   | No file  | `5bf04d4bedf5`  |
| 1324   | No file  | `5bf04d4bedf5`  |
| 1321   | No file  | `5bf04d4bedf5`  |
| 1319   | No file  | `5bf04d4bedf5`  |
| 1318   | No file  | `5bf04d4bedf5`  |
| 1316   | No file  | `5bf04d4bedf5`  |
| 1313   | No file  | `5bf04d4bedf5`  |
| 1311   | No file  | `5bf04d4bedf5`  |
| 1309   | No file  | `5bf04d4bedf5`  |
| 1304   | No file  | `5bf04d4bedf5`  |
| 1292   | No file  | `5bf04d4bedf5`  |
| 1286   | No file  | `5bf04d4bedf5`  |
| 1280   | No file  | `5bf04d4bedf5`  |
| 1276   | No file  | `5bf04d4bedf5`  |
| 1267   | No file  | `5bf04d4bedf5`  |
| 1261   | No file  | `5bf04d4bedf5`  |
| 1256   | No file  | `5bf04d4bedf5`  |
| 1250   | No file  | `5bf04d4bedf5`  |
| 1246   | No file  | `5bf04d4bedf5`  |
| 1239   | No file  | `5bf04d4bedf5`  |
| 1230   | No file  | `5bf04d4bedf5`  |
| 1226   | No file  | `5bf04d4bedf5`  |
| 1220   | No file  | `5bf04d4bedf5`  |
| 1217   | No file  | `5bf04d4bedf5`  |
| 1211   | No file  | `5bf04d4bedf5`  |
| 1210   | No file  | `5bf04d4bedf5`  |
| 1208   | No file  | `5bf04d4bedf5`  |
| 1203   | No file  | `5bf04d4bedf5`  |
| 1197   | No file  | `5bf04d4bedf5`  |
| 1194   | No file  | `5bf04d4bedf5`  |
| 1192   | No file  | `5bf04d4bedf5`  |
| 1187   | No file  | `5bf04d4bedf5`  |
| 1183   | No file  | `5bf04d4bedf5`  |
| 1177   | No file  | `5bf04d4bedf5`  |
| 1173   | No file  | `5bf04d4bedf5`  |
| 1167   | No file  | `5bf04d4bedf5`  |
| 1164   | No file  | `5bf04d4bedf5`  |
| 1156   | No file  | `5bf04d4bedf5`  |
| 1149   | No file  | `5bf04d4bedf5`  |
| 1144   | No file  | `5bf04d4bedf5`  |
| 1137   | No file  | `5bf04d4bedf5`  |
| 1132   | No file  | `5bf04d4bedf5`  |
| 1127   | No file  | `5bf04d4bedf5`  |
| 1122   | No file  | `5bf04d4bedf5`  |
| 1118   | No file  | `5bf04d4bedf5`  |
| 1114   | No file  | `5bf04d4bedf5`  |
| 1109   | No file  | `5bf04d4bedf5`  |
| 1102   | No file  | `5bf04d4bedf5`  |
| 1096   | No file  | `5bf04d4bedf5`  |
| 1088   | No file  | `5bf04d4bedf5`  |
| 1081   | No file  | `5bf04d4bedf5`  |
| 1076   | No file  | `5bf04d4bedf5`  |
| 1069   | No file  | `5bf04d4bedf5`  |
| 1064   | No file  | `5bf04d4bedf5`  |
| 1058   | No file  | `5bf04d4bedf5`  |
| 1051   | No file  | `5bf04d4bedf5`  |
| 1044   | No file  | `5bf04d4bedf5`  |
| 1036   | No file  | `5bf04d4bedf5`  |
| 1026   | No file  | `5bf04d4bedf5`  |
| 1016   | No file  | `5bf04d4bedf5`  |
| 1009   | No file  | `5bf04d4bedf5`  |
| 1005   | No file  | `5bf04d4bedf5`  |
| 1000   | No file  | `5bf04d4bedf5`  |
| 998    | No file  | `5bf04d4bedf5`  |
| 990    | No file  | `5bf04d4bedf5`  |
| 979    | No file  | `5bf04d4bedf5`  |
| 972    | No file  | `5bf04d4bedf5`  |
| 963    | No file  | `5bf04d4bedf5`  |
| 955    | No file  | `5bf04d4bedf5`  |
| 946    | No file  | `5bf04d4bedf5`  |
| 938    | No file  | `5bf04d4bedf5`  |
| 927    | No file  | `5bf04d4bedf5`  |
| 911    | No file  | `5bf04d4bedf5`  |
| 904    | No file  | `5bf04d4bedf5`  |
| 899    | No file  | `5bf04d4bedf5`  |
| 894    | No file  | `5bf04d4bedf5`  |
| 885    | No file  | `5bf04d4bedf5`  |
| 879    | No file  | `5bf04d4bedf5`  |
| 872    | No file  | `5bf04d4bedf5`  |
| 864    | No file  | `5bf04d4bedf5`  |
| 855    | No file  | `5bf04d4bedf5`  |
| 853    | No file  | `5bf04d4bedf5`  |
| 845    | No file  | `5bf04d4bedf5`  |
| 837    | No file  | `5bf04d4bedf5`  |
| 829    | No file  | `5bf04d4bedf5`  |
| 822    | No file  | `5bf04d4bedf5`  |
| 814    | No file  | `5bf04d4bedf5`  |
| 805    | No file  | `5bf04d4bedf5`  |
| 794    | No file  | `5bf04d4bedf5`  |
| 787    | No file  | `5bf04d4bedf5`  |
| 780    | No file  | `5bf04d4bedf5`  |
| 771    | No file  | `5bf04d4bedf5`  |
| 760    | No file  | `5bf04d4bedf5`  |
| 748    | No file  | `5bf04d4bedf5`  |
| 741    | No file  | `5bf04d4bedf5`  |
| 736    | No file  | `5bf04d4bedf5`  |
| 731    | No file  | `5bf04d4bedf5`  |
| 723    | No file  | `5bf04d4bedf5`  |
| 711    | No file  | `5bf04d4bedf5`  |
| 707    | No file  | `5bf04d4bedf5`  |
| 697    | No file  | `5bf04d4bedf5`  |
| 689    | No file  | `5bf04d4bedf5`  |
| 683    | No file  | `5bf04d4bedf5`  |
| 678    | No file  | `5bf04d4bedf5`  |
| 670    | No file  | `5bf04d4bedf5`  |
| 661    | No file  | `5bf04d4bedf5`  |
| 656    | No file  | `5bf04d4bedf5`  |
| 652    | No file  | `5bf04d4bedf5`  |
| 643    | No file  | `5bf04d4bedf5`  |
| 637    | No file  | `5bf04d4bedf5`  |
| 630    | No file  | `5bf04d4bedf5`  |
| 627    | No file  | `5bf04d4bedf5`  |
| 621    | No file  | `5bf04d4bedf5`  |
| 617    | No file  | `5bf04d4bedf5`  |
| 615    | No file  | `5bf04d4bedf5`  |
| 606    | No file  | `5bf04d4bedf5`  |
| 599    | No file  | `5bf04d4bedf5`  |
| 592    | No file  | `5bf04d4bedf5`  |
| 586    | No file  | `5bf04d4bedf5`  |
| 577    | No file  | `5bf04d4bedf5`  |
| 569    | No file  | `5bf04d4bedf5`  |
| 561    | No file  | `5bf04d4bedf5`  |
| 554    | No file  | `5bf04d4bedf5`  |
| 542    | No file  | `5bf04d4bedf5`  |
| 532    | No file  | `5bf04d4bedf5`  |
| 531    | No file  | `5bf04d4bedf5`  |
| 526    | No file  | `5bf04d4bedf5`  |
| 521    | No file  | `5bf04d4bedf5`  |
| 517    | No file  | `5bf04d4bedf5`  |
| 510    | No file  | `5bf04d4bedf5`  |
| 508    | No file  | `5bf04d4bedf5`  |
| 504    | No file  | `5bf04d4bedf5`  |
| 497    | No file  | `5bf04d4bedf5`  |
| 491    | No file  | `5bf04d4bedf5`  |
| 485    | No file  | `5bf04d4bedf5`  |
| 478    | No file  | `5bf04d4bedf5`  |
| 472    | No file  | `5bf04d4bedf5`  |
| 466    | No file  | `5bf04d4bedf5`  |
| 457    | No file  | `5bf04d4bedf5`  |
| 452    | No file  | `5bf04d4bedf5`  |
| 449    | No file  | `5bf04d4bedf5`  |
| 435    | No file  | `5bf04d4bedf5`  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                                                     |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `yachtdicecardoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows have one fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `40` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (10 bytes)

| Offset  | Type | Field        | Notes                                                         |
| ------- | ---- | ------------ | ------------------------------------------------------------- |
| `+0x00` | u32  | card_key     | Card key; unique per row                                      |
| `+0x04` | u32  | card_key_dup | Equal to `card_key` in every row; the offset file points here |
| `+0x08` | u8   | symbol       | Card symbol, `1` to `4`, as in `yachtbasecard.dbss`           |
| `+0x09` | u8   | eye          | Eye value, `1` to `10`                                        |

On client 3474 the 40 rows hold keys 31 to 70: symbol 1 with eyes 1 to 10
on keys 31 to 40, symbol 2 on 41 to 50, 3 on 51 to 60 and 4 on 61 to 70.
The rows are not in key order: keys 70 down to 64, 47 down to 32, 63
down to 48, then 31 (clients 1784 and 3474).

### `yachtdicecardoffset.dbss`

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `yachtdicecard.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row  |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                          |
| ------- | ---- | ----------- | ---------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                    |
| `+0x04` | u32  | data_offset | Row start + 4, at `card_key_dup`               |
| `+0x08` | u32  | data_size   | The row without its leading key: `6`           |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order, and every index row points at the row with
its key (clients 1784 and 3474).

## Field Names

The `DiceCardList` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `DicecardIndex` (`card_key`), `Symbol`
(`symbol`) and `Eye` (`eye`). Its 40 rows match the 40 rows of clients 1784
and 3474 in every column. The file writes the key twice: once as the index
key, once inside the row.

## Notes

- Clients 1784 and 3474 ship the same `yachtdicecard.dbss` and
  `yachtdicecardoffset.dbss`, byte for byte.
- `yachtdice.dbss` lists only cards 1 to 30, and the `#참조` sheet of the
  same workbook has no note for `DiceCardList`.

## Open Questions

### What Reads These Cards

No client table names keys 31 to 70: `yachtdice.dbss` lists the
`yachtbasecard.dbss` keys 1 to 30, and the client Lua reads cards only
through the dice (`ToClient_getYachtDiceCardWrapper(index, faceIndex,
isMyTurn)`). The eyes `7` to `10` fit no hand rank of `yachthandrank.bss`,
whose eye checks stop at `6`. Whether the server deals these cards in some
mode, or the list is unused, is open.
