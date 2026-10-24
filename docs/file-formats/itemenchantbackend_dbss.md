# `itemenchantbackend.dbss` Format

## Purpose

The back part of every [`itemenchant.dbss`](itemenchant_dbss.md) block: for
each (item, enchant level) the bytes from Message Tail `+0x2B` to the end of
the block, which holds `item_access_level`, the undecoded remainder, the
packed key and the crystal group. The front part, from the key to
`life_restrict_type`, is in
[`itemenchantbackendtest.dbss`](itemenchantbackendtest_dbss.md); that doc
has how the three files fit together. `itemenchantbackendoffset.dbss` indexes
the blocks with the keys of `itemenchantoffset.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes       | Records            | Row bytes                    |
| ------ | -------------- | ------- | ------------------------------- | ----------- | ------------------ | ---------------------------- |
| 1      | 1964 and later | 3483    | `itemenchantbackend.dbss`       | 126,919,140 | 169,345 Block      | 320 to 4,484, 749 on average |
| 1      | 1964 and later | 3483    | `itemenchantbackendoffset.dbss` | 2,032,160   | 169,345 Offset Row | 12                           |

| Layout | File                            | Known                | Unknown               |
| ------ | ------------------------------- | -------------------- | --------------------- |
| 1      | `itemenchantbackend.dbss`       | 1,185,419 B (0.9%)   | 125,733,721 B (99.1%) |
| 1      | `itemenchantbackendoffset.dbss` | 2,032,160 B (100.0%) | 0 B (0.0%)            |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `7ad94f669fb5`  |
| 3482   | Layout 1 | `7ad94f669fb5`  |
| 3474   | Layout 1 | `7ad94f669fb5`  |
| 3473   | Layout 1 | `7ad94f669fb5`  |
| 3464   | Layout 1 | `7ad94f669fb5`  |
| 3458   | Layout 1 | `7ad94f669fb5`  |
| 3454   | Layout 1 | `7ad94f669fb5`  |
| 3444   | Layout 1 | `7ad94f669fb5`  |
| 3435   | Layout 1 | `7ad94f669fb5`  |
| 3426   | Layout 1 | `7ad94f669fb5`  |
| 3418   | Layout 1 | `7ad94f669fb5`  |
| 3412   | Layout 1 | `7ad94f669fb5`  |
| 3402   | Layout 1 | `7ad94f669fb5`  |
| 3396   | Layout 1 | `7ad94f669fb5`  |
| 3387   | Layout 1 | `7ad94f669fb5`  |
| 3381   | Layout 1 | `7ad94f669fb5`  |
| 3373   | Layout 1 | `7ad94f669fb5`  |
| 3364   | Layout 1 | `7ad94f669fb5`  |
| 3356   | Layout 1 | `7ad94f669fb5`  |
| 3349   | Layout 1 | `7ad94f669fb5`  |
| 3342   | Layout 1 | `7ad94f669fb5`  |
| 3335   | Layout 1 | `7ad94f669fb5`  |
| 3326   | Layout 1 | `7ad94f669fb5`  |
| 3321   | Layout 1 | `7ad94f669fb5`  |
| 3314   | Layout 1 | `7ad94f669fb5`  |
| 3303   | Layout 1 | `7ad94f669fb5`  |
| 3302   | Layout 1 | `7ad94f669fb5`  |
| 3293   | Layout 1 | `7ad94f669fb5`  |
| 3283   | Layout 1 | `7ad94f669fb5`  |
| 3275   | Layout 1 | `7ad94f669fb5`  |
| 3267   | Layout 1 | `7ad94f669fb5`  |
| 3258   | Layout 1 | `7ad94f669fb5`  |
| 3251   | Layout 1 | `7ad94f669fb5`  |
| 3242   | Layout 1 | `7ad94f669fb5`  |
| 3235   | Layout 1 | `7ad94f669fb5`  |
| 3229   | Layout 1 | `7ad94f669fb5`  |
| 3212   | Layout 1 | `7ad94f669fb5`  |
| 3203   | Layout 1 | `7ad94f669fb5`  |
| 3193   | Layout 1 | `7ad94f669fb5`  |
| 3186   | Layout 1 | `7ad94f669fb5`  |
| 3177   | Layout 1 | `7ad94f669fb5`  |
| 3169   | Layout 1 | `7ad94f669fb5`  |
| 3158   | Layout 1 | `7ad94f669fb5`  |
| 3151   | Layout 1 | `7ad94f669fb5`  |
| 3144   | Layout 1 | `7ad94f669fb5`  |
| 3133   | Layout 1 | `7ad94f669fb5`  |
| 3125   | Layout 1 | `7ad94f669fb5`  |
| 3118   | Layout 1 | `7ad94f669fb5`  |
| 3111   | Layout 1 | `7ad94f669fb5`  |
| 3103   | Layout 1 | `7ad94f669fb5`  |
| 3095   | Layout 1 | `7ad94f669fb5`  |
| 3086   | Layout 1 | `7ad94f669fb5`  |
| 3072   | Layout 1 | `7ad94f669fb5`  |
| 3062   | Layout 1 | `7ad94f669fb5`  |
| 3052   | Layout 1 | `7ad94f669fb5`  |
| 3045   | Layout 1 | `7ad94f669fb5`  |
| 3037   | Layout 1 | `7ad94f669fb5`  |
| 3030   | Layout 1 | `7ad94f669fb5`  |
| 3021   | Layout 1 | `7ad94f669fb5`  |
| 3012   | Layout 1 | `7ad94f669fb5`  |
| 3002   | Layout 1 | `7ad94f669fb5`  |
| 2995   | Layout 1 | `7ad94f669fb5`  |
| 2987   | Layout 1 | `7ad94f669fb5`  |
| 2978   | Layout 1 | `7ad94f669fb5`  |
| 2970   | Layout 1 | `7ad94f669fb5`  |
| 2959   | Layout 1 | `7ad94f669fb5`  |
| 2951   | Layout 1 | `7ad94f669fb5`  |
| 2942   | Layout 1 | `7ad94f669fb5`  |
| 2935   | Layout 1 | `7ad94f669fb5`  |
| 2932   | Layout 1 | `7ad94f669fb5`  |
| 2923   | Layout 1 | `7ad94f669fb5`  |
| 2919   | Layout 1 | `7ad94f669fb5`  |
| 2907   | Layout 1 | `7ad94f669fb5`  |
| 2900   | Layout 1 | `7ad94f669fb5`  |
| 2891   | Layout 1 | `7ad94f669fb5`  |
| 2882   | Layout 1 | `7ad94f669fb5`  |
| 2872   | Layout 1 | `7ad94f669fb5`  |
| 2863   | Layout 1 | `7ad94f669fb5`  |
| 2855   | Layout 1 | `7ad94f669fb5`  |
| 2849   | Layout 1 | `7ad94f669fb5`  |
| 2844   | Layout 1 | `7ad94f669fb5`  |
| 2834   | Layout 1 | `7ad94f669fb5`  |
| 2825   | Layout 1 | `7ad94f669fb5`  |
| 2819   | Layout 1 | `7ad94f669fb5`  |
| 2811   | Layout 1 | `7ad94f669fb5`  |
| 2803   | Layout 1 | `7ad94f669fb5`  |
| 2794   | Layout 1 | `7ad94f669fb5`  |
| 2783   | Layout 1 | `7ad94f669fb5`  |
| 2774   | Layout 1 | `7ad94f669fb5`  |
| 2765   | Layout 1 | `7ad94f669fb5`  |
| 2756   | Layout 1 | `7ad94f669fb5`  |
| 2750   | Layout 1 | `7ad94f669fb5`  |
| 2743   | Layout 1 | `7ad94f669fb5`  |
| 2736   | Layout 1 | `7ad94f669fb5`  |
| 2726   | Layout 1 | `7ad94f669fb5`  |
| 2717   | Layout 1 | `7ad94f669fb5`  |
| 2709   | Layout 1 | `7ad94f669fb5`  |
| 2703   | Layout 1 | `7ad94f669fb5`  |
| 2695   | Layout 1 | `7ad94f669fb5`  |
| 2684   | Layout 1 | `7ad94f669fb5`  |
| 2672   | Layout 1 | `7ad94f669fb5`  |
| 2665   | Layout 1 | `7ad94f669fb5`  |
| 2657   | Layout 1 | `7ad94f669fb5`  |
| 2649   | Layout 1 | `7ad94f669fb5`  |
| 2644   | Layout 1 | `7ad94f669fb5`  |
| 2637   | Layout 1 | `7ad94f669fb5`  |
| 2629   | Layout 1 | `7ad94f669fb5`  |
| 2619   | Layout 1 | `7ad94f669fb5`  |
| 2612   | Layout 1 | `7ad94f669fb5`  |
| 2606   | Layout 1 | `7ad94f669fb5`  |
| 2602   | Layout 1 | `7ad94f669fb5`  |
| 2601   | Layout 1 | `7ad94f669fb5`  |
| 2592   | Layout 1 | `7ad94f669fb5`  |
| 2583   | Layout 1 | `7ad94f669fb5`  |
| 2575   | Layout 1 | `7ad94f669fb5`  |
| 2567   | Layout 1 | `7ad94f669fb5`  |
| 2560   | Layout 1 | `7ad94f669fb5`  |
| 2553   | Layout 1 | `7ad94f669fb5`  |
| 2545   | Layout 1 | `7ad94f669fb5`  |
| 2538   | Layout 1 | `7ad94f669fb5`  |
| 2529   | Layout 1 | `7ad94f669fb5`  |
| 2519   | Layout 1 | `7ad94f669fb5`  |
| 2513   | Layout 1 | `7ad94f669fb5`  |
| 2510   | Layout 1 | `7ad94f669fb5`  |
| 2507   | Layout 1 | `7ad94f669fb5`  |
| 2503   | Layout 1 | `7ad94f669fb5`  |
| 2498   | Layout 1 | `7ad94f669fb5`  |
| 2492   | Layout 1 | `7ad94f669fb5`  |
| 2487   | Layout 1 | `7ad94f669fb5`  |
| 2480   | Layout 1 | `7ad94f669fb5`  |
| 2474   | Layout 1 | `7ad94f669fb5`  |
| 2468   | Layout 1 | `7ad94f669fb5`  |
| 2460   | Layout 1 | `7ad94f669fb5`  |
| 2453   | Layout 1 | `7ad94f669fb5`  |
| 2444   | Layout 1 | `7ad94f669fb5`  |
| 2438   | Layout 1 | `7ad94f669fb5`  |
| 2434   | Layout 1 | `7ad94f669fb5`  |
| 2429   | Layout 1 | `7ad94f669fb5`  |
| 2421   | Layout 1 | `7ad94f669fb5`  |
| 2414   | Layout 1 | `7ad94f669fb5`  |
| 2407   | Layout 1 | `7ad94f669fb5`  |
| 2401   | Layout 1 | `7ad94f669fb5`  |
| 2397   | Layout 1 | `7ad94f669fb5`  |
| 2393   | Layout 1 | `7ad94f669fb5`  |
| 2384   | Layout 1 | `7ad94f669fb5`  |
| 2378   | Layout 1 | `7ad94f669fb5`  |
| 2372   | Layout 1 | `7ad94f669fb5`  |
| 2358   | Layout 1 | `7ad94f669fb5`  |
| 2352   | Layout 1 | `7ad94f669fb5`  |
| 2347   | Layout 1 | `7ad94f669fb5`  |
| 2343   | Layout 1 | `7ad94f669fb5`  |
| 2335   | Layout 1 | `7ad94f669fb5`  |
| 2327   | Layout 1 | `7ad94f669fb5`  |
| 2324   | Layout 1 | `7ad94f669fb5`  |
| 2319   | Layout 1 | `7ad94f669fb5`  |
| 2313   | Layout 1 | `7ad94f669fb5`  |
| 2308   | Layout 1 | `7ad94f669fb5`  |
| 2302   | Layout 1 | `7ad94f669fb5`  |
| 2295   | Layout 1 | `7ad94f669fb5`  |
| 2290   | Layout 1 | `7ad94f669fb5`  |
| 2284   | Layout 1 | `7ad94f669fb5`  |
| 2276   | Layout 1 | `7ad94f669fb5`  |
| 2269   | Layout 1 | `7ad94f669fb5`  |
| 2259   | Layout 1 | `7ad94f669fb5`  |
| 2250   | Layout 1 | `7ad94f669fb5`  |
| 2243   | Layout 1 | `7ad94f669fb5`  |
| 2235   | Layout 1 | `7ad94f669fb5`  |
| 2229   | Layout 1 | `7ad94f669fb5`  |
| 2224   | Layout 1 | `7ad94f669fb5`  |
| 2218   | Layout 1 | `7ad94f669fb5`  |
| 2215   | Layout 1 | `7ad94f669fb5`  |
| 2207   | Layout 1 | `7ad94f669fb5`  |
| 2203   | Layout 1 | `7ad94f669fb5`  |
| 2196   | Layout 1 | `7ad94f669fb5`  |
| 2192   | Layout 1 | `7ad94f669fb5`  |
| 2189   | Layout 1 | `7ad94f669fb5`  |
| 2183   | Layout 1 | `7ad94f669fb5`  |
| 2179   | Layout 1 | `7ad94f669fb5`  |
| 2171   | Layout 1 | `7ad94f669fb5`  |
| 2163   | Layout 1 | `7ad94f669fb5`  |
| 2156   | Layout 1 | `7ad94f669fb5`  |
| 2151   | Layout 1 | `7ad94f669fb5`  |
| 2147   | Layout 1 | `7ad94f669fb5`  |
| 2142   | Layout 1 | `7ad94f669fb5`  |
| 2138   | Layout 1 | `7ad94f669fb5`  |
| 2134   | Layout 1 | `7ad94f669fb5`  |
| 2130   | Layout 1 | `7ad94f669fb5`  |
| 2122   | Layout 1 | `7ad94f669fb5`  |
| 2107   | Layout 1 | `7ad94f669fb5`  |
| 2098   | Layout 1 | `7ad94f669fb5`  |
| 2089   | Layout 1 | `7ad94f669fb5`  |
| 2081   | Layout 1 | `7ad94f669fb5`  |
| 2073   | Layout 1 | `7ad94f669fb5`  |
| 2067   | Layout 1 | `7ad94f669fb5`  |
| 2063   | Layout 1 | `7ad94f669fb5`  |
| 2059   | Layout 1 | `7ad94f669fb5`  |
| 2052   | Layout 1 | `7ad94f669fb5`  |
| 2044   | Layout 1 | `7ad94f669fb5`  |
| 2039   | Layout 1 | `7ad94f669fb5`  |
| 2032   | Layout 1 | `7ad94f669fb5`  |
| 2025   | Layout 1 | `7ad94f669fb5`  |
| 2011   | Layout 1 | `7ad94f669fb5`  |
| 2005   | Layout 1 | `7ad94f669fb5`  |
| 2000   | Layout 1 | `7ad94f669fb5`  |
| 1996   | Layout 1 | `7ad94f669fb5`  |
| 1991   | Layout 1 | `7ad94f669fb5`  |
| 1985   | Layout 1 | `7ad94f669fb5`  |
| 1980   | Layout 1 | `7ad94f669fb5`  |
| 1969   | Layout 1 | `7ad94f669fb5`  |
| 1964   | Layout 1 | `7ad94f669fb5`  |
| 1958   | No file  | `7ad94f669fb5`  |
| 1950   | No file  | `7ad94f669fb5`  |
| 1945   | No file  | `7ad94f669fb5`  |
| 1937   | No file  | `7ad94f669fb5`  |
| 1933   | No file  | `7ad94f669fb5`  |
| 1927   | No file  | `7ad94f669fb5`  |
| 1921   | No file  | `7ad94f669fb5`  |
| 1914   | No file  | `7ad94f669fb5`  |
| 1908   | No file  | `7ad94f669fb5`  |
| 1897   | No file  | `7ad94f669fb5`  |
| 1892   | No file  | `7ad94f669fb5`  |
| 1886   | No file  | `7ad94f669fb5`  |
| 1881   | No file  | `7ad94f669fb5`  |
| 1871   | No file  | `7ad94f669fb5`  |
| 1866   | No file  | `7ad94f669fb5`  |
| 1862   | No file  | `7ad94f669fb5`  |
| 1854   | No file  | `7ad94f669fb5`  |
| 1846   | No file  | `7ad94f669fb5`  |
| 1838   | No file  | `7ad94f669fb5`  |
| 1832   | No file  | `7ad94f669fb5`  |
| 1826   | No file  | `7ad94f669fb5`  |
| 1822   | No file  | `7ad94f669fb5`  |
| 1818   | No file  | `7ad94f669fb5`  |
| 1804   | No file  | `7ad94f669fb5`  |
| 1794   | No file  | `7ad94f669fb5`  |
| 1790   | No file  | `7ad94f669fb5`  |
| 1784   | No file  | `7ad94f669fb5`  |
| 1774   | No file  | `7ad94f669fb5`  |
| 1771   | No file  | `7ad94f669fb5`  |
| 1762   | No file  | `7ad94f669fb5`  |
| 1759   | No file  | `7ad94f669fb5`  |
| 1754   | No file  | `7ad94f669fb5`  |
| 1749   | No file  | `7ad94f669fb5`  |
| 1743   | No file  | `7ad94f669fb5`  |
| 1737   | No file  | `7ad94f669fb5`  |
| 1731   | No file  | `7ad94f669fb5`  |
| 1725   | No file  | `7ad94f669fb5`  |
| 1717   | No file  | `7ad94f669fb5`  |
| 1710   | No file  | `7ad94f669fb5`  |
| 1704   | No file  | `7ad94f669fb5`  |
| 1698   | No file  | `7ad94f669fb5`  |
| 1690   | No file  | `7ad94f669fb5`  |
| 1685   | No file  | `7ad94f669fb5`  |
| 1680   | No file  | `7ad94f669fb5`  |
| 1674   | No file  | `7ad94f669fb5`  |
| 1668   | No file  | `7ad94f669fb5`  |
| 1659   | No file  | `7ad94f669fb5`  |
| 1649   | No file  | `7ad94f669fb5`  |
| 1642   | No file  | `7ad94f669fb5`  |
| 1636   | No file  | `7ad94f669fb5`  |
| 1628   | No file  | `7ad94f669fb5`  |
| 1622   | No file  | `7ad94f669fb5`  |
| 1614   | No file  | `7ad94f669fb5`  |
| 1608   | No file  | `7ad94f669fb5`  |
| 1602   | No file  | `7ad94f669fb5`  |
| 1598   | No file  | `7ad94f669fb5`  |
| 1594   | No file  | `7ad94f669fb5`  |
| 1590   | No file  | `7ad94f669fb5`  |
| 1587   | No file  | `7ad94f669fb5`  |
| 1584   | No file  | `7ad94f669fb5`  |
| 1579   | No file  | `7ad94f669fb5`  |
| 1572   | No file  | `7ad94f669fb5`  |
| 1565   | No file  | `7ad94f669fb5`  |
| 1559   | No file  | `7ad94f669fb5`  |
| 1554   | No file  | `7ad94f669fb5`  |
| 1547   | No file  | `7ad94f669fb5`  |
| 1537   | No file  | `7ad94f669fb5`  |
| 1529   | No file  | `7ad94f669fb5`  |
| 1524   | No file  | `7ad94f669fb5`  |
| 1519   | No file  | `7ad94f669fb5`  |
| 1509   | No file  | `7ad94f669fb5`  |
| 1506   | No file  | `7ad94f669fb5`  |
| 1504   | No file  | `7ad94f669fb5`  |
| 1500   | No file  | `7ad94f669fb5`  |
| 1493   | No file  | `7ad94f669fb5`  |
| 1489   | No file  | `7ad94f669fb5`  |
| 1485   | No file  | `7ad94f669fb5`  |
| 1481   | No file  | `7ad94f669fb5`  |
| 1474   | No file  | `7ad94f669fb5`  |
| 1466   | No file  | `7ad94f669fb5`  |
| 1462   | No file  | `7ad94f669fb5`  |
| 1459   | No file  | `7ad94f669fb5`  |
| 1453   | No file  | `7ad94f669fb5`  |
| 1450   | No file  | `7ad94f669fb5`  |
| 1445   | No file  | `7ad94f669fb5`  |
| 1439   | No file  | `7ad94f669fb5`  |
| 1433   | No file  | `7ad94f669fb5`  |
| 1430   | No file  | `7ad94f669fb5`  |
| 1426   | No file  | `7ad94f669fb5`  |
| 1421   | No file  | `7ad94f669fb5`  |
| 1417   | No file  | `7ad94f669fb5`  |
| 1416   | No file  | `7ad94f669fb5`  |
| 1409   | No file  | `7ad94f669fb5`  |
| 1405   | No file  | `7ad94f669fb5`  |
| 1401   | No file  | `7ad94f669fb5`  |
| 1396   | No file  | `7ad94f669fb5`  |
| 1391   | No file  | `7ad94f669fb5`  |
| 1390   | No file  | `7ad94f669fb5`  |
| 1386   | No file  | `7ad94f669fb5`  |
| 1381   | No file  | `7ad94f669fb5`  |
| 1379   | No file  | `7ad94f669fb5`  |
| 1372   | No file  | `7ad94f669fb5`  |
| 1366   | No file  | `7ad94f669fb5`  |
| 1364   | No file  | `7ad94f669fb5`  |
| 1363   | No file  | `7ad94f669fb5`  |
| 1360   | No file  | `7ad94f669fb5`  |
| 1358   | No file  | `7ad94f669fb5`  |
| 1355   | No file  | `7ad94f669fb5`  |
| 1351   | No file  | `7ad94f669fb5`  |
| 1348   | No file  | `7ad94f669fb5`  |
| 1346   | No file  | `7ad94f669fb5`  |
| 1341   | No file  | `7ad94f669fb5`  |
| 1340   | No file  | `7ad94f669fb5`  |
| 1338   | No file  | `7ad94f669fb5`  |
| 1335   | No file  | `7ad94f669fb5`  |
| 1333   | No file  | `7ad94f669fb5`  |
| 1329   | No file  | `7ad94f669fb5`  |
| 1327   | No file  | `7ad94f669fb5`  |
| 1324   | No file  | `7ad94f669fb5`  |
| 1321   | No file  | `7ad94f669fb5`  |
| 1319   | No file  | `7ad94f669fb5`  |
| 1318   | No file  | `7ad94f669fb5`  |
| 1316   | No file  | `7ad94f669fb5`  |
| 1313   | No file  | `7ad94f669fb5`  |
| 1311   | No file  | `7ad94f669fb5`  |
| 1309   | No file  | `7ad94f669fb5`  |
| 1304   | No file  | `7ad94f669fb5`  |
| 1292   | No file  | `7ad94f669fb5`  |
| 1286   | No file  | `7ad94f669fb5`  |
| 1280   | No file  | `7ad94f669fb5`  |
| 1276   | No file  | `7ad94f669fb5`  |
| 1267   | No file  | `7ad94f669fb5`  |
| 1261   | No file  | `7ad94f669fb5`  |
| 1256   | No file  | `7ad94f669fb5`  |
| 1250   | No file  | `7ad94f669fb5`  |
| 1246   | No file  | `7ad94f669fb5`  |
| 1239   | No file  | `7ad94f669fb5`  |
| 1230   | No file  | `7ad94f669fb5`  |
| 1226   | No file  | `7ad94f669fb5`  |
| 1220   | No file  | `7ad94f669fb5`  |
| 1217   | No file  | `7ad94f669fb5`  |
| 1211   | No file  | `7ad94f669fb5`  |
| 1210   | No file  | `7ad94f669fb5`  |
| 1208   | No file  | `7ad94f669fb5`  |
| 1203   | No file  | `7ad94f669fb5`  |
| 1197   | No file  | `7ad94f669fb5`  |
| 1194   | No file  | `7ad94f669fb5`  |
| 1192   | No file  | `7ad94f669fb5`  |
| 1187   | No file  | `7ad94f669fb5`  |
| 1183   | No file  | `7ad94f669fb5`  |
| 1177   | No file  | `7ad94f669fb5`  |
| 1173   | No file  | `7ad94f669fb5`  |
| 1167   | No file  | `7ad94f669fb5`  |
| 1164   | No file  | `7ad94f669fb5`  |
| 1156   | No file  | `7ad94f669fb5`  |
| 1149   | No file  | `7ad94f669fb5`  |
| 1144   | No file  | `7ad94f669fb5`  |
| 1137   | No file  | `7ad94f669fb5`  |
| 1132   | No file  | `7ad94f669fb5`  |
| 1127   | No file  | `7ad94f669fb5`  |
| 1122   | No file  | `7ad94f669fb5`  |
| 1118   | No file  | `7ad94f669fb5`  |
| 1114   | No file  | `7ad94f669fb5`  |
| 1109   | No file  | `7ad94f669fb5`  |
| 1102   | No file  | `7ad94f669fb5`  |
| 1096   | No file  | `7ad94f669fb5`  |
| 1088   | No file  | `7ad94f669fb5`  |
| 1081   | No file  | `7ad94f669fb5`  |
| 1076   | No file  | `7ad94f669fb5`  |
| 1069   | No file  | `7ad94f669fb5`  |
| 1064   | No file  | `7ad94f669fb5`  |
| 1058   | No file  | `7ad94f669fb5`  |
| 1051   | No file  | `7ad94f669fb5`  |
| 1044   | No file  | `7ad94f669fb5`  |
| 1036   | No file  | `7ad94f669fb5`  |
| 1026   | No file  | `7ad94f669fb5`  |
| 1016   | No file  | `7ad94f669fb5`  |
| 1009   | No file  | `7ad94f669fb5`  |
| 1005   | No file  | `7ad94f669fb5`  |
| 1000   | No file  | `7ad94f669fb5`  |
| 998    | No file  | `7ad94f669fb5`  |
| 990    | No file  | `7ad94f669fb5`  |
| 979    | No file  | `7ad94f669fb5`  |
| 972    | No file  | `7ad94f669fb5`  |
| 963    | No file  | `7ad94f669fb5`  |
| 955    | No file  | `7ad94f669fb5`  |
| 946    | No file  | `7ad94f669fb5`  |
| 938    | No file  | `7ad94f669fb5`  |
| 927    | No file  | `7ad94f669fb5`  |
| 911    | No file  | `7ad94f669fb5`  |
| 904    | No file  | `7ad94f669fb5`  |
| 899    | No file  | `7ad94f669fb5`  |
| 894    | No file  | `7ad94f669fb5`  |
| 885    | No file  | `7ad94f669fb5`  |
| 879    | No file  | `7ad94f669fb5`  |
| 872    | No file  | `7ad94f669fb5`  |
| 864    | No file  | `7ad94f669fb5`  |
| 855    | No file  | `7ad94f669fb5`  |
| 853    | No file  | `7ad94f669fb5`  |
| 845    | No file  | `7ad94f669fb5`  |
| 837    | No file  | `7ad94f669fb5`  |
| 829    | No file  | `7ad94f669fb5`  |
| 822    | No file  | `7ad94f669fb5`  |
| 814    | No file  | `7ad94f669fb5`  |
| 805    | No file  | `7ad94f669fb5`  |
| 794    | No file  | `7ad94f669fb5`  |
| 787    | No file  | `7ad94f669fb5`  |
| 780    | No file  | `7ad94f669fb5`  |
| 771    | No file  | `7ad94f669fb5`  |
| 760    | No file  | `7ad94f669fb5`  |
| 748    | No file  | `7ad94f669fb5`  |
| 741    | No file  | `7ad94f669fb5`  |
| 736    | No file  | `7ad94f669fb5`  |
| 731    | No file  | `7ad94f669fb5`  |
| 723    | No file  | `7ad94f669fb5`  |
| 711    | No file  | `7ad94f669fb5`  |
| 707    | No file  | `7ad94f669fb5`  |
| 697    | No file  | `7ad94f669fb5`  |
| 689    | No file  | `7ad94f669fb5`  |
| 683    | No file  | `7ad94f669fb5`  |
| 678    | No file  | `7ad94f669fb5`  |
| 670    | No file  | `7ad94f669fb5`  |
| 661    | No file  | `7ad94f669fb5`  |
| 656    | No file  | `7ad94f669fb5`  |
| 652    | No file  | `7ad94f669fb5`  |
| 643    | No file  | `7ad94f669fb5`  |
| 637    | No file  | `7ad94f669fb5`  |
| 630    | No file  | `7ad94f669fb5`  |
| 627    | No file  | `7ad94f669fb5`  |
| 621    | No file  | `7ad94f669fb5`  |
| 617    | No file  | `7ad94f669fb5`  |
| 615    | No file  | `7ad94f669fb5`  |
| 606    | No file  | `7ad94f669fb5`  |
| 599    | No file  | `7ad94f669fb5`  |
| 592    | No file  | `7ad94f669fb5`  |
| 586    | No file  | `7ad94f669fb5`  |
| 577    | No file  | `7ad94f669fb5`  |
| 569    | No file  | `7ad94f669fb5`  |
| 561    | No file  | `7ad94f669fb5`  |
| 554    | No file  | `7ad94f669fb5`  |
| 542    | No file  | `7ad94f669fb5`  |
| 532    | No file  | `7ad94f669fb5`  |
| 531    | No file  | `7ad94f669fb5`  |
| 526    | No file  | `7ad94f669fb5`  |
| 521    | No file  | `7ad94f669fb5`  |
| 517    | No file  | `7ad94f669fb5`  |
| 510    | No file  | `7ad94f669fb5`  |
| 508    | No file  | `7ad94f669fb5`  |
| 504    | No file  | `7ad94f669fb5`  |
| 497    | No file  | `7ad94f669fb5`  |
| 491    | No file  | `7ad94f669fb5`  |
| 485    | No file  | `7ad94f669fb5`  |
| 478    | No file  | `7ad94f669fb5`  |
| 472    | No file  | `7ad94f669fb5`  |
| 466    | No file  | `7ad94f669fb5`  |
| 457    | No file  | `7ad94f669fb5`  |
| 452    | No file  | `7ad94f669fb5`  |
| 449    | No file  | `7ad94f669fb5`  |
| 435    | No file  | `7ad94f669fb5`  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                                                     |
| ------------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `itemenchantbackendoffset.dbss` | Required | Maps the packed key to a block offset and size                                           |
| `languagedata_en.loc`           | Optional | Item name for the item ID (`str_type=0`)                                                 |
| `jewelgroupstaticstatus.bss`    | Optional | Crystal group name and preset limit for `crystal_group`; without it the column shows the number |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes |
| ------- | ------------ | ------ | ----- |
| `+0x00` | u32          | count  | Block count, matching the companion |
| `+0x04` | Block[count] | blocks | Contiguous, in the order of the companion rows; the last block ends at the end of the file |

### Block (variable: 54 bytes, size from `itemenchantbackendoffset.dbss`)

The offsets in `itemenchant.dbss` are Message Tail `+0x2B` for `unknown_00`
and `+0x5A` for `item_access_level`; the remainder and the two fields at
the end are the same bytes there.

| Offset     | Type        | Field             | Notes |
| ---------- | ----------- | ----------------- | ----- |
| `+0x00`    | bytes[47]   | unknown_00        | `unknown_2b` in `itemenchant.dbss`. Bytes `0x03` to `0x2D` are `0x77` in all 70,826 base blocks (client 3483); bytes `0x00` to `0x02` are `0x77` in 67,056 of them, and hold small values such as `0x18 0x19` in the rest |
| `+0x2F`    | u8          | item_access_level | 2016 `_itemAccessLevel`, see Field Names in `itemenchant_dbss.md`. On client 3483: `0` (31,713 base items), `1` (21,179), `10` (12,389), `99` (3,204), `20` (2,298), and `15`, `19` and `40` on 41 more |
| `+0x30`    | bytes[rest] | unknown_30        | Undecoded, `unknown_after_message_tail` in `itemenchant.dbss`; 266 to 4,430 bytes (client 3483) |
| `end-0x06` | u32         | key               | The packed key of the offset row, `enchant_level << 24 \| item_id`, in every block (client 3483); `key_dup` in `itemenchant.dbss` |
| `end-0x02` | u16         | crystal_group     | The crystal's [jewelgroupstaticstatus.bss](jewelgroupstaticstatus_bss.md) group; `0xFFFF` on everything else and on every higher level |

### `itemenchantbackendoffset.dbss`

The layout of `itemenchantoffset.dbss`, with the same keys in the same
order (169,345 rows on client 3483).

| Offset              | Type              | Field        | Notes |
| ------------------- | ----------------- | ------------ | ----- |
| `+0x00`             | char[4]           | magic        | `PABR` (ASCII) |
| `+0x04`             | u32               | count        | Number of rows |
| `+0x08`             | Offset Row[count] | rows         | `count` × 12-byte rows |
| `rows+0x00`         | String Table      | string_table | The PABR string table, here with no strings |
| `string_table+0x00` | u32               | end_of_rows  | Equals `8 + count × 12` |
| `string_table+0x04` | u32               | zero         | Always zero |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes |
| ------- | ---- | ----------- | ----- |
| `+0x00` | u32  | key         | Packed item ID and enchant level, see Key Packing in `itemenchant_dbss.md` |
| `+0x04` | u32  | data_offset | Byte offset of the block in `itemenchantbackend.dbss` |
| `+0x08` | u32  | data_size   | Block length in bytes |

Rows are contiguous: `data_offset + data_size` of one row equals the next
row's `data_offset`. For every key, `data_size` is the `itemenchant.dbss`
block size less the `itemenchantbackendtest.dbss` block size (client 3483).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` in observed data |
| `+0x04` | pstr[string_count] | strings      | PABR string-table entries |

## Notes

- The doc check fits Layout 1 back to client 1964 because the block is
  mostly `bytes[rest]`: on those clients it confirms the offset rows and the
  key at `end-0x06` only. Where the split point and `item_access_level` sit
  in their blocks is checked on client 3483 only; the `itemenchant.dbss`
  layout before client 3473 is not documented.
- The `itemenchant.dbss` doc decodes nothing between `item_access_level`
  and `key_dup` beyond the scan for `second_string`, so this file's known
  bytes are the 7 named ones per block. What the remainder holds, and why
  the client data stores the blocks a second time split in two, are open
  (Open Questions in `itemenchant_dbss.md` and
  `itemenchantbackendtest_dbss.md`).
