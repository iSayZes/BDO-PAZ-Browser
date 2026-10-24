# `manufacturecondition.dbss` Format

## Purpose

Processing actions: each record names one tab of the processing window
(`MANUFACTURE_HEAT`, `REPAIR_ITEM` and the rest) and holds two condition
scripts, one that decides whether the tab shows and one that decides whether
it can be used. The record key is the hash of the action name, the same
`action_hash` that [`manufacture.bss`](manufacture_bss.md) stores on each
recipe row.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records      | Row bytes                |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------ | ------------------------ |
| 1      | 1346 and later | 3483    | `manufacturecondition.dbss`       | 1,183 | 14 Record    | 72 to 123, 84 on average |
| 1      | 1346 and later | 3483    | `manufactureconditionoffset.dbss` | 172   | 14 Index Row | 12                       |

| Layout | File                              | Known            | Unknown    |
| ------ | --------------------------------- | ---------------- | ---------- |
| 1      | `manufacturecondition.dbss`       | 1,183 B (100.0%) | 0 B (0.0%) |
| 1      | `manufactureconditionoffset.dbss` | 172 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `ec8881b24434`  |
| 3482   | Layout 1             | `ec8881b24434`  |
| 3474   | Layout 1             | `ec8881b24434`  |
| 3473   | Layout 1             | `ec8881b24434`  |
| 3464   | Layout 1             | `ec8881b24434`  |
| 3458   | Layout 1             | `ec8881b24434`  |
| 3454   | Layout 1             | `ec8881b24434`  |
| 3444   | Layout 1             | `ec8881b24434`  |
| 3435   | Layout 1             | `ec8881b24434`  |
| 3426   | Layout 1             | `ec8881b24434`  |
| 3418   | Layout 1             | `ec8881b24434`  |
| 3412   | Layout 1             | `ec8881b24434`  |
| 3402   | Layout 1             | `ec8881b24434`  |
| 3396   | Layout 1             | `ec8881b24434`  |
| 3387   | Layout 1             | `ec8881b24434`  |
| 3381   | Layout 1             | `ec8881b24434`  |
| 3373   | Layout 1             | `ec8881b24434`  |
| 3364   | Layout 1             | `ec8881b24434`  |
| 3356   | Layout 1             | `ec8881b24434`  |
| 3349   | Layout 1             | `ec8881b24434`  |
| 3342   | Layout 1             | `ec8881b24434`  |
| 3335   | Layout 1             | `ec8881b24434`  |
| 3326   | Layout 1             | `ec8881b24434`  |
| 3321   | Layout 1             | `ec8881b24434`  |
| 3314   | Layout 1             | `ec8881b24434`  |
| 3303   | Layout 1             | `ec8881b24434`  |
| 3302   | Layout 1             | `ec8881b24434`  |
| 3293   | Layout 1             | `ec8881b24434`  |
| 3283   | Layout 1             | `ec8881b24434`  |
| 3275   | Layout 1             | `ec8881b24434`  |
| 3267   | Layout 1             | `ec8881b24434`  |
| 3258   | Layout 1             | `ec8881b24434`  |
| 3251   | Layout 1             | `ec8881b24434`  |
| 3242   | Layout 1             | `ec8881b24434`  |
| 3235   | Layout 1             | `ec8881b24434`  |
| 3229   | Layout 1             | `ec8881b24434`  |
| 3212   | Layout 1             | `ec8881b24434`  |
| 3203   | Layout 1             | `ec8881b24434`  |
| 3193   | Layout 1             | `ec8881b24434`  |
| 3186   | Layout 1             | `ec8881b24434`  |
| 3177   | Layout 1             | `ec8881b24434`  |
| 3169   | Layout 1             | `ec8881b24434`  |
| 3158   | Layout 1             | `ec8881b24434`  |
| 3151   | Layout 1             | `ec8881b24434`  |
| 3144   | Layout 1             | `ec8881b24434`  |
| 3133   | Layout 1             | `ec8881b24434`  |
| 3125   | Layout 1             | `ec8881b24434`  |
| 3118   | Layout 1             | `ec8881b24434`  |
| 3111   | Layout 1             | `ec8881b24434`  |
| 3103   | Layout 1             | `ec8881b24434`  |
| 3095   | Layout 1             | `ec8881b24434`  |
| 3086   | Layout 1             | `ec8881b24434`  |
| 3072   | Layout 1             | `ec8881b24434`  |
| 3062   | Layout 1             | `ec8881b24434`  |
| 3052   | Layout 1             | `ec8881b24434`  |
| 3045   | Layout 1             | `ec8881b24434`  |
| 3037   | Layout 1             | `ec8881b24434`  |
| 3030   | Layout 1             | `ec8881b24434`  |
| 3021   | Layout 1             | `ec8881b24434`  |
| 3012   | Layout 1             | `ec8881b24434`  |
| 3002   | Layout 1             | `ec8881b24434`  |
| 2995   | Layout 1             | `ec8881b24434`  |
| 2987   | Layout 1             | `ec8881b24434`  |
| 2978   | Layout 1             | `ec8881b24434`  |
| 2970   | Layout 1             | `ec8881b24434`  |
| 2959   | Layout 1             | `ec8881b24434`  |
| 2951   | Layout 1             | `ec8881b24434`  |
| 2942   | Layout 1             | `ec8881b24434`  |
| 2935   | Layout 1             | `ec8881b24434`  |
| 2932   | Layout 1             | `ec8881b24434`  |
| 2923   | Layout 1             | `ec8881b24434`  |
| 2919   | Layout 1             | `ec8881b24434`  |
| 2907   | Layout 1             | `ec8881b24434`  |
| 2900   | Layout 1             | `ec8881b24434`  |
| 2891   | Layout 1             | `ec8881b24434`  |
| 2882   | Layout 1             | `ec8881b24434`  |
| 2872   | Layout 1             | `ec8881b24434`  |
| 2863   | Layout 1             | `ec8881b24434`  |
| 2855   | Layout 1             | `ec8881b24434`  |
| 2849   | Layout 1             | `ec8881b24434`  |
| 2844   | Layout 1             | `ec8881b24434`  |
| 2834   | Layout 1             | `ec8881b24434`  |
| 2825   | Layout 1             | `ec8881b24434`  |
| 2819   | Layout 1             | `ec8881b24434`  |
| 2811   | Layout 1             | `ec8881b24434`  |
| 2803   | Layout 1             | `ec8881b24434`  |
| 2794   | Layout 1             | `ec8881b24434`  |
| 2783   | Layout 1             | `ec8881b24434`  |
| 2774   | Layout 1             | `ec8881b24434`  |
| 2765   | Layout 1             | `ec8881b24434`  |
| 2756   | Layout 1             | `ec8881b24434`  |
| 2750   | Layout 1             | `ec8881b24434`  |
| 2743   | Layout 1             | `ec8881b24434`  |
| 2736   | Layout 1             | `ec8881b24434`  |
| 2726   | Layout 1             | `ec8881b24434`  |
| 2717   | Layout 1             | `ec8881b24434`  |
| 2709   | Layout 1             | `ec8881b24434`  |
| 2703   | Layout 1             | `ec8881b24434`  |
| 2695   | Layout 1             | `ec8881b24434`  |
| 2684   | Layout 1             | `ec8881b24434`  |
| 2672   | Layout 1             | `ec8881b24434`  |
| 2665   | Layout 1             | `ec8881b24434`  |
| 2657   | Layout 1             | `ec8881b24434`  |
| 2649   | Layout 1             | `ec8881b24434`  |
| 2644   | Layout 1             | `ec8881b24434`  |
| 2637   | Layout 1             | `ec8881b24434`  |
| 2629   | Layout 1             | `ec8881b24434`  |
| 2619   | Layout 1             | `ec8881b24434`  |
| 2612   | Layout 1             | `ec8881b24434`  |
| 2606   | Layout 1             | `ec8881b24434`  |
| 2602   | Layout 1             | `ec8881b24434`  |
| 2601   | Layout 1             | `ec8881b24434`  |
| 2592   | Layout 1             | `ec8881b24434`  |
| 2583   | Layout 1             | `ec8881b24434`  |
| 2575   | Layout 1             | `ec8881b24434`  |
| 2567   | Layout 1             | `ec8881b24434`  |
| 2560   | Layout 1             | `ec8881b24434`  |
| 2553   | Layout 1             | `ec8881b24434`  |
| 2545   | Layout 1             | `ec8881b24434`  |
| 2538   | Layout 1             | `ec8881b24434`  |
| 2529   | Layout 1             | `ec8881b24434`  |
| 2519   | Layout 1             | `ec8881b24434`  |
| 2513   | Layout 1             | `ec8881b24434`  |
| 2510   | Layout 1             | `ec8881b24434`  |
| 2507   | Layout 1             | `ec8881b24434`  |
| 2503   | Layout 1             | `ec8881b24434`  |
| 2498   | Layout 1             | `ec8881b24434`  |
| 2492   | Layout 1             | `ec8881b24434`  |
| 2487   | Layout 1             | `ec8881b24434`  |
| 2480   | Layout 1             | `ec8881b24434`  |
| 2474   | Layout 1             | `ec8881b24434`  |
| 2468   | Layout 1             | `ec8881b24434`  |
| 2460   | Layout 1             | `ec8881b24434`  |
| 2453   | Layout 1             | `ec8881b24434`  |
| 2444   | Layout 1             | `ec8881b24434`  |
| 2438   | Layout 1             | `ec8881b24434`  |
| 2434   | Layout 1             | `ec8881b24434`  |
| 2429   | Layout 1             | `ec8881b24434`  |
| 2421   | Layout 1             | `ec8881b24434`  |
| 2414   | Layout 1             | `ec8881b24434`  |
| 2407   | Layout 1             | `ec8881b24434`  |
| 2401   | Layout 1             | `ec8881b24434`  |
| 2397   | Layout 1             | `ec8881b24434`  |
| 2393   | Layout 1             | `ec8881b24434`  |
| 2384   | Layout 1             | `ec8881b24434`  |
| 2378   | Layout 1             | `ec8881b24434`  |
| 2372   | Layout 1             | `ec8881b24434`  |
| 2358   | Layout 1             | `ec8881b24434`  |
| 2352   | Layout 1             | `ec8881b24434`  |
| 2347   | Layout 1             | `ec8881b24434`  |
| 2343   | Layout 1             | `ec8881b24434`  |
| 2335   | Layout 1             | `ec8881b24434`  |
| 2327   | Layout 1             | `ec8881b24434`  |
| 2324   | Layout 1             | `ec8881b24434`  |
| 2319   | Layout 1             | `ec8881b24434`  |
| 2313   | Layout 1             | `ec8881b24434`  |
| 2308   | Layout 1             | `ec8881b24434`  |
| 2302   | Layout 1             | `ec8881b24434`  |
| 2295   | Layout 1             | `ec8881b24434`  |
| 2290   | Layout 1             | `ec8881b24434`  |
| 2284   | Layout 1             | `ec8881b24434`  |
| 2276   | Layout 1             | `ec8881b24434`  |
| 2269   | Layout 1             | `ec8881b24434`  |
| 2259   | Layout 1             | `ec8881b24434`  |
| 2250   | Layout 1             | `ec8881b24434`  |
| 2243   | Layout 1             | `ec8881b24434`  |
| 2235   | Layout 1             | `ec8881b24434`  |
| 2229   | Layout 1             | `ec8881b24434`  |
| 2224   | Layout 1             | `ec8881b24434`  |
| 2218   | Layout 1             | `ec8881b24434`  |
| 2215   | Layout 1             | `ec8881b24434`  |
| 2207   | Layout 1             | `ec8881b24434`  |
| 2203   | Layout 1             | `ec8881b24434`  |
| 2196   | Layout 1             | `ec8881b24434`  |
| 2192   | Layout 1             | `ec8881b24434`  |
| 2189   | Layout 1             | `ec8881b24434`  |
| 2183   | Layout 1             | `ec8881b24434`  |
| 2179   | Layout 1             | `ec8881b24434`  |
| 2171   | Layout 1             | `ec8881b24434`  |
| 2163   | Layout 1             | `ec8881b24434`  |
| 2156   | Layout 1             | `ec8881b24434`  |
| 2151   | Layout 1             | `ec8881b24434`  |
| 2147   | Layout 1             | `ec8881b24434`  |
| 2142   | Layout 1             | `ec8881b24434`  |
| 2138   | Layout 1             | `ec8881b24434`  |
| 2134   | Layout 1             | `ec8881b24434`  |
| 2130   | Layout 1             | `ec8881b24434`  |
| 2122   | Layout 1             | `ec8881b24434`  |
| 2107   | Layout 1             | `ec8881b24434`  |
| 2098   | Layout 1             | `ec8881b24434`  |
| 2089   | Layout 1             | `ec8881b24434`  |
| 2081   | Layout 1             | `ec8881b24434`  |
| 2073   | Layout 1             | `ec8881b24434`  |
| 2067   | Layout 1             | `ec8881b24434`  |
| 2063   | Layout 1             | `ec8881b24434`  |
| 2059   | Layout 1             | `ec8881b24434`  |
| 2052   | Layout 1             | `ec8881b24434`  |
| 2044   | Layout 1             | `ec8881b24434`  |
| 2039   | Layout 1             | `ec8881b24434`  |
| 2032   | Layout 1             | `ec8881b24434`  |
| 2025   | Layout 1             | `ec8881b24434`  |
| 2011   | Layout 1             | `ec8881b24434`  |
| 2005   | Layout 1             | `ec8881b24434`  |
| 2000   | Layout 1             | `ec8881b24434`  |
| 1996   | Layout 1             | `ec8881b24434`  |
| 1991   | Layout 1             | `ec8881b24434`  |
| 1985   | Layout 1             | `ec8881b24434`  |
| 1980   | Layout 1             | `ec8881b24434`  |
| 1969   | Layout 1             | `ec8881b24434`  |
| 1964   | Layout 1             | `ec8881b24434`  |
| 1958   | Layout 1             | `ec8881b24434`  |
| 1950   | Layout 1             | `ec8881b24434`  |
| 1945   | Layout 1             | `ec8881b24434`  |
| 1937   | Layout 1             | `ec8881b24434`  |
| 1933   | Layout 1             | `ec8881b24434`  |
| 1927   | Layout 1             | `ec8881b24434`  |
| 1921   | Layout 1             | `ec8881b24434`  |
| 1914   | Layout 1             | `ec8881b24434`  |
| 1908   | Layout 1             | `ec8881b24434`  |
| 1897   | Layout 1             | `ec8881b24434`  |
| 1892   | Layout 1             | `ec8881b24434`  |
| 1886   | Layout 1             | `ec8881b24434`  |
| 1881   | Layout 1             | `ec8881b24434`  |
| 1871   | Layout 1             | `ec8881b24434`  |
| 1866   | Layout 1             | `ec8881b24434`  |
| 1862   | Layout 1             | `ec8881b24434`  |
| 1854   | Layout 1             | `ec8881b24434`  |
| 1846   | Layout 1             | `ec8881b24434`  |
| 1838   | Layout 1             | `ec8881b24434`  |
| 1832   | Layout 1             | `ec8881b24434`  |
| 1826   | Layout 1             | `ec8881b24434`  |
| 1822   | Layout 1             | `ec8881b24434`  |
| 1818   | Layout 1             | `ec8881b24434`  |
| 1804   | Layout 1             | `ec8881b24434`  |
| 1794   | Layout 1             | `ec8881b24434`  |
| 1790   | Layout 1             | `ec8881b24434`  |
| 1784   | Layout 1             | `ec8881b24434`  |
| 1774   | Layout 1             | `ec8881b24434`  |
| 1771   | Layout 1             | `ec8881b24434`  |
| 1762   | Layout 1             | `ec8881b24434`  |
| 1759   | Layout 1             | `ec8881b24434`  |
| 1754   | Layout 1             | `ec8881b24434`  |
| 1749   | Layout 1             | `ec8881b24434`  |
| 1743   | Layout 1             | `ec8881b24434`  |
| 1737   | Layout 1             | `ec8881b24434`  |
| 1731   | Layout 1             | `ec8881b24434`  |
| 1725   | Layout 1             | `ec8881b24434`  |
| 1717   | Layout 1             | `ec8881b24434`  |
| 1710   | Layout 1             | `ec8881b24434`  |
| 1704   | Layout 1             | `ec8881b24434`  |
| 1698   | Layout 1             | `ec8881b24434`  |
| 1690   | Layout 1             | `ec8881b24434`  |
| 1685   | Layout 1             | `ec8881b24434`  |
| 1680   | Layout 1             | `ec8881b24434`  |
| 1674   | Layout 1             | `ec8881b24434`  |
| 1668   | Layout 1             | `ec8881b24434`  |
| 1659   | Layout 1             | `ec8881b24434`  |
| 1649   | Layout 1             | `ec8881b24434`  |
| 1642   | Layout 1             | `ec8881b24434`  |
| 1636   | Layout 1             | `ec8881b24434`  |
| 1628   | Layout 1             | `ec8881b24434`  |
| 1622   | Layout 1             | `ec8881b24434`  |
| 1614   | Layout 1             | `ec8881b24434`  |
| 1608   | Layout 1             | `ec8881b24434`  |
| 1602   | Layout 1             | `ec8881b24434`  |
| 1598   | Layout 1             | `ec8881b24434`  |
| 1594   | Layout 1             | `ec8881b24434`  |
| 1590   | Layout 1             | `ec8881b24434`  |
| 1587   | Layout 1             | `ec8881b24434`  |
| 1584   | Layout 1             | `ec8881b24434`  |
| 1579   | Layout 1             | `ec8881b24434`  |
| 1572   | Layout 1             | `ec8881b24434`  |
| 1565   | Layout 1             | `ec8881b24434`  |
| 1559   | Layout 1             | `ec8881b24434`  |
| 1554   | Layout 1             | `ec8881b24434`  |
| 1547   | Layout 1             | `ec8881b24434`  |
| 1537   | Layout 1             | `ec8881b24434`  |
| 1529   | Layout 1             | `ec8881b24434`  |
| 1524   | Layout 1             | `ec8881b24434`  |
| 1519   | Layout 1             | `ec8881b24434`  |
| 1509   | Layout 1             | `ec8881b24434`  |
| 1506   | Layout 1             | `ec8881b24434`  |
| 1504   | Layout 1             | `ec8881b24434`  |
| 1500   | Layout 1             | `ec8881b24434`  |
| 1493   | Layout 1             | `ec8881b24434`  |
| 1489   | Layout 1             | `ec8881b24434`  |
| 1485   | Layout 1             | `ec8881b24434`  |
| 1481   | Layout 1             | `ec8881b24434`  |
| 1474   | Layout 1             | `ec8881b24434`  |
| 1466   | Layout 1             | `ec8881b24434`  |
| 1462   | Layout 1             | `ec8881b24434`  |
| 1459   | Layout 1             | `ec8881b24434`  |
| 1453   | Layout 1             | `ec8881b24434`  |
| 1450   | Layout 1             | `ec8881b24434`  |
| 1445   | Layout 1             | `ec8881b24434`  |
| 1439   | Layout 1             | `ec8881b24434`  |
| 1433   | Layout 1             | `ec8881b24434`  |
| 1430   | Layout 1             | `ec8881b24434`  |
| 1426   | Layout 1             | `ec8881b24434`  |
| 1421   | Layout 1             | `ec8881b24434`  |
| 1417   | Layout 1             | `ec8881b24434`  |
| 1416   | Layout 1             | `ec8881b24434`  |
| 1409   | Layout 1             | `ec8881b24434`  |
| 1405   | Layout 1             | `ec8881b24434`  |
| 1401   | Layout 1             | `ec8881b24434`  |
| 1396   | Layout 1             | `ec8881b24434`  |
| 1391   | Layout 1             | `ec8881b24434`  |
| 1390   | Layout 1             | `ec8881b24434`  |
| 1386   | Layout 1             | `ec8881b24434`  |
| 1381   | Layout 1             | `ec8881b24434`  |
| 1379   | Layout 1             | `ec8881b24434`  |
| 1372   | Layout 1             | `ec8881b24434`  |
| 1366   | Layout 1             | `ec8881b24434`  |
| 1364   | Layout 1             | `ec8881b24434`  |
| 1363   | Layout 1             | `ec8881b24434`  |
| 1360   | Layout 1             | `ec8881b24434`  |
| 1358   | Layout 1             | `ec8881b24434`  |
| 1355   | Layout 1             | `ec8881b24434`  |
| 1351   | Layout 1             | `ec8881b24434`  |
| 1348   | Layout 1             | `ec8881b24434`  |
| 1346   | Layout 1             | `ec8881b24434`  |
| 1341   | No documented layout | `ec8881b24434`  |
| 1340   | No documented layout | `ec8881b24434`  |
| 1338   | No documented layout | `ec8881b24434`  |
| 1335   | No documented layout | `ec8881b24434`  |
| 1333   | No documented layout | `ec8881b24434`  |
| 1329   | No documented layout | `ec8881b24434`  |
| 1327   | No documented layout | `ec8881b24434`  |
| 1324   | No documented layout | `ec8881b24434`  |
| 1321   | No documented layout | `ec8881b24434`  |
| 1319   | No documented layout | `ec8881b24434`  |
| 1318   | No documented layout | `ec8881b24434`  |
| 1316   | No documented layout | `ec8881b24434`  |
| 1313   | No documented layout | `ec8881b24434`  |
| 1311   | No documented layout | `ec8881b24434`  |
| 1309   | No documented layout | `ec8881b24434`  |
| 1304   | No documented layout | `ec8881b24434`  |
| 1292   | No documented layout | `ec8881b24434`  |
| 1286   | No documented layout | `ec8881b24434`  |
| 1280   | No documented layout | `ec8881b24434`  |
| 1276   | No documented layout | `ec8881b24434`  |
| 1267   | No file              | `ec8881b24434`  |
| 1261   | No file              | `ec8881b24434`  |
| 1256   | No file              | `ec8881b24434`  |
| 1250   | No file              | `ec8881b24434`  |
| 1246   | No file              | `ec8881b24434`  |
| 1239   | No file              | `ec8881b24434`  |
| 1230   | No file              | `ec8881b24434`  |
| 1226   | No file              | `ec8881b24434`  |
| 1220   | No file              | `ec8881b24434`  |
| 1217   | No file              | `ec8881b24434`  |
| 1211   | No file              | `ec8881b24434`  |
| 1210   | No file              | `ec8881b24434`  |
| 1208   | No file              | `ec8881b24434`  |
| 1203   | No file              | `ec8881b24434`  |
| 1197   | No file              | `ec8881b24434`  |
| 1194   | No file              | `ec8881b24434`  |
| 1192   | No file              | `ec8881b24434`  |
| 1187   | No file              | `ec8881b24434`  |
| 1183   | No file              | `ec8881b24434`  |
| 1177   | No file              | `ec8881b24434`  |
| 1173   | No file              | `ec8881b24434`  |
| 1167   | No file              | `ec8881b24434`  |
| 1164   | No file              | `ec8881b24434`  |
| 1156   | No file              | `ec8881b24434`  |
| 1149   | No file              | `ec8881b24434`  |
| 1144   | No file              | `ec8881b24434`  |
| 1137   | No file              | `ec8881b24434`  |
| 1132   | No file              | `ec8881b24434`  |
| 1127   | No file              | `ec8881b24434`  |
| 1122   | No file              | `ec8881b24434`  |
| 1118   | No file              | `ec8881b24434`  |
| 1114   | No file              | `ec8881b24434`  |
| 1109   | No file              | `ec8881b24434`  |
| 1102   | No file              | `ec8881b24434`  |
| 1096   | No file              | `ec8881b24434`  |
| 1088   | No file              | `ec8881b24434`  |
| 1081   | No file              | `ec8881b24434`  |
| 1076   | No file              | `ec8881b24434`  |
| 1069   | No file              | `ec8881b24434`  |
| 1064   | No file              | `ec8881b24434`  |
| 1058   | No file              | `ec8881b24434`  |
| 1051   | No file              | `ec8881b24434`  |
| 1044   | No file              | `ec8881b24434`  |
| 1036   | No file              | `ec8881b24434`  |
| 1026   | No file              | `ec8881b24434`  |
| 1016   | No file              | `ec8881b24434`  |
| 1009   | No file              | `ec8881b24434`  |
| 1005   | No file              | `ec8881b24434`  |
| 1000   | No file              | `ec8881b24434`  |
| 998    | No file              | `ec8881b24434`  |
| 990    | No file              | `ec8881b24434`  |
| 979    | No file              | `ec8881b24434`  |
| 972    | No file              | `ec8881b24434`  |
| 963    | No file              | `ec8881b24434`  |
| 955    | No file              | `ec8881b24434`  |
| 946    | No file              | `ec8881b24434`  |
| 938    | No file              | `ec8881b24434`  |
| 927    | No file              | `ec8881b24434`  |
| 911    | No file              | `ec8881b24434`  |
| 904    | No file              | `ec8881b24434`  |
| 899    | No file              | `ec8881b24434`  |
| 894    | No file              | `ec8881b24434`  |
| 885    | No file              | `ec8881b24434`  |
| 879    | No file              | `ec8881b24434`  |
| 872    | No file              | `ec8881b24434`  |
| 864    | No file              | `ec8881b24434`  |
| 855    | No file              | `ec8881b24434`  |
| 853    | No file              | `ec8881b24434`  |
| 845    | No file              | `ec8881b24434`  |
| 837    | No file              | `ec8881b24434`  |
| 829    | No file              | `ec8881b24434`  |
| 822    | No file              | `ec8881b24434`  |
| 814    | No file              | `ec8881b24434`  |
| 805    | No file              | `ec8881b24434`  |
| 794    | No file              | `ec8881b24434`  |
| 787    | No file              | `ec8881b24434`  |
| 780    | No file              | `ec8881b24434`  |
| 771    | No file              | `ec8881b24434`  |
| 760    | No file              | `ec8881b24434`  |
| 748    | No file              | `ec8881b24434`  |
| 741    | No file              | `ec8881b24434`  |
| 736    | No file              | `ec8881b24434`  |
| 731    | No file              | `ec8881b24434`  |
| 723    | No file              | `ec8881b24434`  |
| 711    | No file              | `ec8881b24434`  |
| 707    | No file              | `ec8881b24434`  |
| 697    | No file              | `ec8881b24434`  |
| 689    | No file              | `ec8881b24434`  |
| 683    | No file              | `ec8881b24434`  |
| 678    | No file              | `ec8881b24434`  |
| 670    | No file              | `ec8881b24434`  |
| 661    | No file              | `ec8881b24434`  |
| 656    | No file              | `ec8881b24434`  |
| 652    | No file              | `ec8881b24434`  |
| 643    | No file              | `ec8881b24434`  |
| 637    | No file              | `ec8881b24434`  |
| 630    | No file              | `ec8881b24434`  |
| 627    | No file              | `ec8881b24434`  |
| 621    | No file              | `ec8881b24434`  |
| 617    | No file              | `ec8881b24434`  |
| 615    | No file              | `ec8881b24434`  |
| 606    | No file              | `ec8881b24434`  |
| 599    | No file              | `ec8881b24434`  |
| 592    | No file              | `ec8881b24434`  |
| 586    | No file              | `ec8881b24434`  |
| 577    | No file              | `ec8881b24434`  |
| 569    | No file              | `ec8881b24434`  |
| 561    | No file              | `ec8881b24434`  |
| 554    | No file              | `ec8881b24434`  |
| 542    | No file              | `ec8881b24434`  |
| 532    | No file              | `ec8881b24434`  |
| 531    | No file              | `ec8881b24434`  |
| 526    | No file              | `ec8881b24434`  |
| 521    | No file              | `ec8881b24434`  |
| 517    | No file              | `ec8881b24434`  |
| 510    | No file              | `ec8881b24434`  |
| 508    | No file              | `ec8881b24434`  |
| 504    | No file              | `ec8881b24434`  |
| 497    | No file              | `ec8881b24434`  |
| 491    | No file              | `ec8881b24434`  |
| 485    | No file              | `ec8881b24434`  |
| 478    | No file              | `ec8881b24434`  |
| 472    | No file              | `ec8881b24434`  |
| 466    | No file              | `ec8881b24434`  |
| 457    | No file              | `ec8881b24434`  |
| 452    | No file              | `ec8881b24434`  |
| 449    | No file              | `ec8881b24434`  |
| 435    | No file              | `ec8881b24434`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                                              |
| --------------------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `manufactureconditionoffset.dbss` | Optional | `action_hash -> (data_offset, data_size)` index, see below; the records can be walked without it   |
| `languagedata_en.loc`             | Optional | The window's name of each action (LOC type 37), as in [`manufacture.bss` Actions](manufacture_bss.md#actions) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                           |
| ------- | ------------- | ------- | ----------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `14` on client 3474          |
| `+0x04` | Record[count] | records | Back to back to the end of the file; see Record |

### Record (variable: 32 bytes + name and condition text)

| Offset                          | Type  | Field                   | Notes                                                                                   |
| ------------------------------- | ----- | ----------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`                         | u32   | action_hash             | lookup3 `hashlittle` of the `action_name` bytes with seed `0xC5EDE`; the index key      |
| `+0x04`                         | str8  | action_name             | The processing window's `actionName`; the index's `data_offset` points here             |
| `action_name+0x00`              | u32   | action_hash_dup         | Equal to `action_hash` in every record                                                  |
| `action_name+0x04`              | str16 | check_visible_condition | Script that decides whether the action's tab shows; empty on 2 records (client 3474)    |
| `check_visible_condition+0x00`  | str16 | check_enable_condition  | Script that decides whether the tab can be used; empty on 11 records (client 3474)      |

`action_hash` is the hash `manufacture.bss` documents under
[`action_hash`](manufacture_bss.md#action_hash): `_common/string_hash.py`'s
`hashlittle` over the ASCII name, so `MANUFACTURE_HEAT` hashes to
`0x1B6F02F1`. It matches all 14 records on clients 3474 and 1784.

### `manufactureconditionoffset.dbss`

| Offset  | Type             | Field | Notes                                         |
| ------- | ---------------- | ----- | --------------------------------------------- |
| `+0x00` | u32              | count | Equals the `manufacturecondition.dbss` count  |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row           |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | action_hash | Record key                              |
| `+0x04` | u32  | data_offset | Record start + 4, at `action_name`      |
| `+0x08` | u32  | data_size   | Record size - 4                         |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The rows
are not in file order; on client 3474 every row matches the record walked
from the start of the file.

## Field Names

The record is the `ManufactureCondition_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, with the columns `ActionName`,
`CheckVisibleCondition` and `CheckEnableCondition`. A `<null>` cell is
stored as an empty string (count `0`). The sheet's second column,
`가공 액션 명` (the action's Korean name), is not in the file.

| Field                   | Column                  | Shared names, same value                      |
| ----------------------- | ----------------------- | --------------------------------------------- |
| action_name             | `ActionName`            | 14 of 14 (client 1784), 14 of 14 (client 3474) |
| check_visible_condition | `CheckVisibleCondition` | 14 of 14 (client 1784), 14 of 14 (client 3474) |
| check_enable_condition  | `CheckEnableCondition`  | 14 of 14 (client 1784), 14 of 14 (client 3474) |

The client Lua uses the same split. `PaGlobal_Manufacture_All_UpdateVisibleRadioButton`
in `panel_window_manufacture_all_3.luac` shows each action tab by
`isVisibleManufactureAction(actionName)`, then sets each shown tab active or
grayed out (`SetMonoTone`) by `isEnableManufactureAction(actionName)`.

## Conditions

All five scripts in the file (client 3474):

| Script                                   | Field                   | Actions                                                       |
| ---------------------------------------- | ----------------------- | ------------------------------------------------------------- |
| `getlevel()>0`                           | check_visible_condition | 11: every action except Filtering, Drying and Collect rainwater |
| `getlevel()>99`                          | check_visible_condition | Collect rainwater (`MANUFACTURE_RAINWATER`)                   |
| `getKnowledge(6558)`                     | check_enable_condition  | Repair (`REPAIR_ITEM`); knowledge 6558 is Repair (LOC type 34) |
| `getWeatherFactor(WindForce,0)>300;`     | check_enable_condition  | Filtering (`MANUFACTURE_THINNING`)                            |
| `getWeatherFactor(RainAmount,0)<100000;` | check_enable_condition  | Drying (`MANUFACTURE_DRY`)                                    |

Filtering and Drying have an empty `check_visible_condition`; every other
action has an empty `check_enable_condition` except Repair. `getlevel()>99`
reads as a lock on the Collect rainwater tab, which the window still lists
in `MANUFACTURE_INFO` (`panel_window_manufacture_all.luac`).

The window adds checks of its own on top of the file: Repair also needs an
anvil nearby (`isNearInstallation(eType_Anvil)`), and contents groups `22`
and `285` hide the Imperial Cuisine, Imperial Alchemy and Manufacture tabs
when closed.

## Notes

- The 14 action names are the 12 of the `manufacture.bss` string table plus
  `REPAIR_ITEM` and `MANUFACTURE_RAINWATER`, which have no recipe rows. Every
  action a `manufacture.bss` row uses has a record here.
- The records are sorted by neither hash nor name, and not in the sheet's
  row order.
- Both files are byte for byte the same on clients 1784 and 3474.

## Open Questions

### Weather Factor Scale

Drying needs `getWeatherFactor(RainAmount,0)<100000` and Filtering needs
`getWeatherFactor(WindForce,0)>300`. The world map node window
(`panel_worldmap_nodeinfo_renew.luac`) reads rain through
`getWeatherInfoByWaypoint(eWSFT_RAIN_AMOUNT, ...)` as a fraction, with `0.3`
and `0.6` as its medium and heavy thresholds, so `100000` is on another
scale. No client Lua or data file shows the scale `getWeatherFactor` returns
or what its second argument `0` selects.
